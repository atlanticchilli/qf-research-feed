#!/usr/bin/env python3
import os, re, json, pathlib, datetime as dt
import requests, feedparser, frontmatter
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ========= CONFIG =========
QFIN_QUERY = "cat:q-fin.*"            # q-fin.PM/TR/ST etc. Keep broad for POC
MAX_RESULTS = 25                      # pull latest N items
DAYS_BACK = 3                         # small buffer
OUT_ROOT = pathlib.Path("preprints")
# ==========================

def arxiv_feed_url():
    return (
        "http://export.arxiv.org/api/query"
        f"?search_query={QFIN_QUERY}"
        "&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={MAX_RESULTS}"
    )

def html_sources(arxiv_id_with_v):
    return [
        f"https://arxiv.org/html/{arxiv_id_with_v}",  # official arXiv HTML if available
        f"https://ar5iv.org/html/{arxiv_id_with_v}",  # fallback renderer
    ]

def fetch_html(arxiv_id_with_v):
    for url in html_sources(arxiv_id_with_v):
        try:
            r = requests.get(url, timeout=20)
            if r.status_code == 200 and len(r.text) > 2000:
                return url, r.text
        except requests.RequestException:
            pass
    return None, None

def sanitize(s):
    return re.sub(r"\s+", " ", (s or "")).strip()

def split_sections(markdown_text):
    sections, current_title, buf = [], "01_intro", []
    for line in markdown_text.splitlines():
        if re.match(r"^#\s+", line):
            if buf:
                sections.append((current_title, "\n".join(buf)))
                buf = []
            title = re.sub(r"^#\s+", "", line).lower()
            if "method" in title: current_title = "02_method"
            elif "result" in title: current_title = "03_results"
            elif "discussion" in title or "conclusion" in title: current_title = "04_discussion"
            elif "referen" in title: current_title = "99_refs"
            else: current_title = "01_intro"
        else:
            buf.append(line)
    if buf:
        sections.append((current_title, "\n".join(buf)))
    return sections or [("01_intro", markdown_text)]

def mark_previous_versions_not_current(root_dir, family_id, new_version_int):
    """
    Find older version folders for the same family_id and flip is_current=false in their meta.json and md front-matter.
    Non-destructive, safe.
    """
    fam = family_id.replace("arxiv:", "")
    for p in pathlib.Path(root_dir).rglob(f"arxiv_{fam}_v*"):
        # match vN
        m = re.search(r"_v(\d+)$", p.name)
        if not m: continue
        v = int(m.group(1))
        if v >= new_version_int:  # skip current or newer (shouldn't happen)
            continue

        meta = p / "meta.json"
        if meta.exists():
            try:
                obj = json.loads(meta.read_text(encoding="utf-8"))
                if obj.get("is_current") is True:
                    obj["is_current"] = False
                    meta.write_text(json.dumps(obj, indent=2), encoding="utf-8")
            except Exception:
                pass

        # also flip front-matter in known md files
        for mdfile in ["01_intro.md","02_method.md","03_results.md","04_discussion.md","99_refs.md"]:
            f = p / mdfile
            if f.exists():
                try:
                    post = frontmatter.load(f)
                    if post.get("is_current", True):
                        post["is_current"] = False
                        f.write_text(frontmatter.dumps(post), encoding="utf-8")
                except Exception:
                    pass

def main():
    feed = feedparser.parse(arxiv_feed_url())
    for e in feed.entries:
        abs_url = e.id  # e.g., https://arxiv.org/abs/2402.08954v1
        m = re.search(r"/abs/([0-9]{4}\.[0-9]{5})(v\d+)?$", abs_url)
        if not m:
            continue
        base = m.group(1)                 # 2402.08954
        version = m.group(2) or "v1"      # v1
        arxiv_id_with_v = f"{base}{version}"
        family_id = base

        # destination path
        year = e.published_parsed.tm_year if e.get("published_parsed") else dt.datetime.utcnow().year
        month = e.published_parsed.tm_mon if e.get("published_parsed") else dt.datetime.utcnow().month
        dst = OUT_ROOT / f"{year:04d}" / f"{month:02d}" / f"arxiv_{base}_{version}"

        # idempotency guard: if meta.json exists, skip (already ingested)
        if (dst / "meta.json").exists():
            print(f"[skip] exists: {dst}")
            continue

        html_url, html = fetch_html(arxiv_id_with_v)
        if not html:
            print(f"[skip] no HTML found for {arxiv_id_with_v}")
            continue

        soup = BeautifulSoup(html, "html.parser")
        title = sanitize(soup.title.text if soup.title else e.title)
        authors = []
        if "authors" in e:
            for a in e.authors:
                nm = a.name if isinstance(a, dict) else getattr(a, "name", None)
                if nm: authors.append(nm)
        authors = list(dict.fromkeys(authors))

        body = soup.find("body") or soup
        for tag in body.select("header, nav, footer"): tag.decompose()
        markdown_text = md(str(body), heading_style="ATX")

        sections = split_sections(markdown_text)
        dst.mkdir(parents=True, exist_ok=True)

        # common front-matter
        fm_common = {
            "doc_id": f"arxiv:{arxiv_id_with_v}",
            "family_id": f"arxiv:{family_id}",
            "title": title,
            "venue": "arXiv q-fin",
            "version": int(version.replace("v","")),
            "year": year,
            "authors": authors,
            "taxonomy": {
                "asset_classes": [],
                "horizons": [],
                "alpha_families": [],
                "themes": []
            },
            "url_abs": abs_url,
            "url_html": html_url,
            "is_current": True
        }

        # write sectioned MD
        for key, content in sections:
            filename = f"{key}.md"
            post = frontmatter.Post(content, **fm_common)
            (dst / filename).write_text(frontmatter.dumps(post), encoding="utf-8")

        # meta.json (normalized)
        (dst / "meta.json").write_text(json.dumps({
            "doc_id": fm_common["doc_id"],
            "family_id": fm_common["family_id"],
            "title": fm_common["title"],
            "venue": fm_common["venue"],
            "version": fm_common["version"],
            "year": fm_common["year"],
            "authors": fm_common["authors"],
            "url_abs": fm_common["url_abs"],
            "url_html": fm_common["url_html"],
            "is_current": True
        }, indent=2), encoding="utf-8")

        # mark previous versions as not current (safe, non-destructive)
        mark_previous_versions_not_current(OUT_ROOT, fm_common["family_id"], fm_common["version"])

        print(f"[ok] {arxiv_id_with_v} → {dst}")

if __name__ == "__main__":
    main()
