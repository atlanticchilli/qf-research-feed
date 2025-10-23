---
authors:
- Šimon Trlifaj
doc_id: arxiv:2510.19377v1
family_id: arxiv:2510.19377
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Government Transparency Affects Innovation: Evidence from Wireless Products'
url_abs: http://arxiv.org/abs/2510.19377v1
url_html: https://arxiv.org/html/2510.19377v1
venue: arXiv q-fin
version: 1
year: 2025
---


Šimon Trlifaj, Central European University11endnote: 1Thanks to Cristina Corduneanu-Huci, Michael Dorsch, Mihaly Fazekas, Yian Yin, Shane M. Greenstein, Heesang Ryu, Joachim Henkel, Minyuan Zhao, Paul Heidhues, Jo Seldeslachts, Pierre Fleckinger, Mimra Wanda, Reinhilde Veugelers, Jannis Kück, Dirk Czarnitzki, David Cerero-Guerra, Agnes Batory, Bence Hamrak and participants of the 2024 Competition and Innovation Summer School, 2025 CEU Annual Doctoral Conference, 2025 Munich Summer Institute, and 2025 International Conference on Science of Science and Innovation for valuable feedback. Special thanks to Reza Biazaran, Krista Witanowski and their colleagues at FCC for clarifications on FCC practices. This project has been supported by grants from the Czech Fulbright Commission and the Central European University. Its contents are the sole responsibility of the author and may not represent the views of these institutions.

(October 22, 2025)

###### Abstract

Does government transparency affect innovation? I evaluate the launch of a government database with detailed technical information on the universe of wireless-enabled products on the U.S. market (N 347 thousand). The results show the launch approximately doubled the use of new technologies in the following ten years, an indicator of follow-on innovation. The increase affected both products in the same and new product classes, suggesting novelty; waned over several years, potentially due to an increase in secrecy and patenting; and boosted foreign more than U.S. domestic competitors. These results highlight the importance of information for private sector innovation.

#### JEL

O30, O33, O38

## 1 Introduction

Governments have long shaped the information environment in which firms innovate. Venetian medieval laws constrained the movement of glass workers to maintain a technological lead (Amato, [1997](https://arxiv.org/html/2510.19377v1#bib.bib1)). 18th-century British parliamentary rewards system actively encouraged innovation disclosure, paying the inventor Thomas Lombe for exhibiting silk working machines in the Tower of London (Burrell and Kelly, [2015](https://arxiv.org/html/2510.19377v1#bib.bib13)). The 1999 U.S. American Inventor’s Protection Act accelerated the disclosure of patent applications, and likely increased technology diffusion (Hegde et al., [2023](https://arxiv.org/html/2510.19377v1#bib.bib31)). Today, support for open access innovation, calls for algorithmic transparency, as well as recent closures of U.S. government websites (Gotfredsen, [2025](https://arxiv.org/html/2510.19377v1#bib.bib25)) likewise likely impact innovation.

The effects of transparency regulations on innovation may be large, given how heavily firms rely on secrecy in innovation. Surveys consistently find that firms rely on secrecy and lead time more than patenting in almost all industries across countries (Levin et al., [1987](https://arxiv.org/html/2510.19377v1#bib.bib36); Arundel, [2001](https://arxiv.org/html/2510.19377v1#bib.bib5); Cohen et al., [2000](https://arxiv.org/html/2510.19377v1#bib.bib16); Hall et al., [2014](https://arxiv.org/html/2510.19377v1#bib.bib27)). In a 1994 U.S. survey—closest to the focus of this paper—Cohen et al. ([2000](https://arxiv.org/html/2510.19377v1#bib.bib16), p. 33) finds that R&D laboratories in the communication equipment industry report patents effective as an appropriation mechanism for 26 percent of their products (midpoint mean, N 34), compared to 47 and 66 percent for secrecy and lead time. The role of patents is somewhat stronger in computers and electronic equipment industries, but all industries relevant to this analysis report secrecy as more effective than patents in product innovation. Any regulatory requirements to disclose information about new products may thus affect a major innovation appropriation mechanism.

In this paper, I use a unique dataset of wireless-capable products to study the effects of government transparency on follow-on innovation. The empirical setup has two advantages: it covers the universe of all wireless-capable products introduced to the U.S. market, making it possible to observe the majority of products not protected by a patent, and it includes detailed technical description of each product, making it possible to track the use of specific technologies. Wireless-enabled products represent the most high-tech electronic products today, and the U.S. market is representative to the frontier of technology globally, making the analysis broadly relevant.

I study the effects of a 1998 government transparency shock that made this documentation available on the internet, and its effect on follow-on innovation by competitors and on the originator firm. I primarily rely on a difference-in-differences design for causal identification, which differentiates between follow-on innovation by competitors (who benefit from transparency) and by the originator firm (which does not). I supplement this approach with regression-discontinuity design for robustness and extensions to originator firm behavior.

The results show a sizable positive effect of the transparency shock on follow-on innovation, including products in new categories, heightened business dynamism in terms of market entry and exit, and increased international competition that benefited U.S. firms at least as much as Non-U.S. firms. Governments typically do not prioritize supporting innovation with policies that affect information availability, such as those concerning algorithmic transparency, AI regulations, medical device databases, or restrictions on non-compete agreements.

## 2 Prior literature

Information is central to the economics of innovation, to a point where seminal work conceptualizes innovation as information (Nelson, [1959](https://arxiv.org/html/2510.19377v1#bib.bib39); Arrow, [1962](https://arxiv.org/html/2510.19377v1#bib.bib4); Stiglitz, [1999](https://arxiv.org/html/2510.19377v1#bib.bib48)), and formal models focus on firms observing inventions of their competitors (Williams, [2017](https://arxiv.org/html/2510.19377v1#bib.bib52); Hall et al., [2014](https://arxiv.org/html/2510.19377v1#bib.bib27)).

Empirically, undisclosed innovation is difficult to observe as the proliferation of secrecy obfuscates the role of information in innovation. Most prior work relies on innovation observable in patents, in which firms voluntarily disclose their inventions in exchange for legal protection (Hall and Harhoff, [2012](https://arxiv.org/html/2510.19377v1#bib.bib28)). Various study designs have leveraged variation in the costs of information access and the timing of disclosure to estimate the effects of patent disclosure on innovation. Cox ([2019](https://arxiv.org/html/2510.19377v1#bib.bib18)) document an increase in patenting after 1734 U.K. patent disclosure requirement (restricted to London, where patent descriptions were stored), and Furman et al. ([2021](https://arxiv.org/html/2510.19377v1#bib.bib24)) find a similar increase in U.S. locations where a patent library had opened between 1995 and 1997. Gross ([2023](https://arxiv.org/html/2510.19377v1#bib.bib26)) find a significant decrease in follow-on innovation due to delayed grant and publication of patents due to a Second World War patent secrecy program, and (Rassenfosse et al., [2024](https://arxiv.org/html/2510.19377v1#bib.bib43)) find a similar decrease in patents subject to an analogous Cold War-era program. Multiple studies analyze the effects of the 1999 U.S. American Inventors Protection Act (AIPA), which accelerated patent application disclosure, and find positive effects on follow-on innovation and patent licensing (Hegde and Luo, [2018](https://arxiv.org/html/2510.19377v1#bib.bib32); Kim and Valentine, [2021](https://arxiv.org/html/2510.19377v1#bib.bib34); Baruffaldi and Simeth, [2020](https://arxiv.org/html/2510.19377v1#bib.bib6); Hegde et al., [2023](https://arxiv.org/html/2510.19377v1#bib.bib31)).

These findings provide consistent evidence of a positive effect of patent disclosure on follow-on innovation. However, they are limited to the minority of inventions that are (eventually) patented, which skews toward large firms in certain industries (Levin et al., [1987](https://arxiv.org/html/2510.19377v1#bib.bib36); Arundel, [2001](https://arxiv.org/html/2510.19377v1#bib.bib5); Cohen et al., [2000](https://arxiv.org/html/2510.19377v1#bib.bib16); Hall et al., [2014](https://arxiv.org/html/2510.19377v1#bib.bib27)). Disclosure in patent documents is also a strategic choice and is complicated due to the willful infringement doctrine, which discourages inventors from reading patents (Sandrik, [2021](https://arxiv.org/html/2510.19377v1#bib.bib46)). The effects of disclosure on innovation are thus confounded by market entry, self-selection, and strategic signaling.

A fruitful approach to overcoming the limitations of patent data relies on firms having to disclose their products when entering a market. Moser ([2005](https://arxiv.org/html/2510.19377v1#bib.bib37)) relies on product data from 19th-century World’s Fairs, which arguably covered most high-tech inventions globally, (Argente et al., [2021](https://arxiv.org/html/2510.19377v1#bib.bib2)) relies on barcode readers in stores to measure innovation in retail products. These studies confirm that most inventions were not patented, but did not evaluate the effects of disclosure on innovation. The open access movement provided some variation in science and innovation disclosure. Recent studies on open access mandates find a positive effect on follow-on innovation, relying mostly on patent and academic publications data (Bryan and Ozcan, [2021](https://arxiv.org/html/2510.19377v1#bib.bib11); Staudt, [2020](https://arxiv.org/html/2510.19377v1#bib.bib47)), although its broader impact is disputed (Probst et al., [2023](https://arxiv.org/html/2510.19377v1#bib.bib42)). Berkes and Nencka ([2024](https://arxiv.org/html/2510.19377v1#bib.bib9)) leverage variation in public library openings and find a sizable positive effect of library openings on future patenting. Closer to product market effects, Murray et al. ([2016](https://arxiv.org/html/2510.19377v1#bib.bib38)) find a positive effect of lower costs of access to genetically modified mice on entry of new researchers and exploration of more diverse research paths. Finally, in a simultaneous study, Kim et al. ([2024](https://arxiv.org/html/2510.19377v1#bib.bib33)) use a subset of the dataset used here to study the effects of open-source drivers on downstream Wifi router supply chains.

This paper expands this literature by estimating the causal effects of government-mandated transparency on follow-on innovation outside of the patent system, inclusive of all products irrespective of intellectual property protections, and in a large high-tech industry. Broadly, it contributes to the literature on follow-on innovation and innovation spillovers, previously mostly limited to patent data (Bloom et al., [2013](https://arxiv.org/html/2510.19377v1#bib.bib10); Sampat and Williams, [2019](https://arxiv.org/html/2510.19377v1#bib.bib45)), and to literature on the effects of government transparency, previously mostly limited to public-sector effects (Porumbescu et al., [2022](https://arxiv.org/html/2510.19377v1#bib.bib41); Corduneanu-Huci and Trlifaj, [2024](https://arxiv.org/html/2510.19377v1#bib.bib17)).

## 3 Wireless products regulation

The empirical setup originates with the Federal Communication Commission (FCC), a U.S. government agency responsible for regulating wireless-enabled products since the 1934 adoption of Section 302 of the Communications Act, following an increase in incidents of interference of unrelated devices such as cash machines and TV receivers (Knapp and Wall, [1997](https://arxiv.org/html/2510.19377v1#bib.bib35)).

The FCC’s equipment authorization program is a major regulatory instrument in this effort. It requires any firm marketing a product that could interfere with electromagnetic spectra to comply with strict technical rules and document compliance in an application to the FCC, which then grants authorization for product marketing. In the late 1990s, the period of focus of this paper, these products included hearing aids, domestic and industrial remote controllers, pagers, mobile phones, microwaves, and alarm systems. Today, many digital products of daily use are under the regulation, including smartphones and personal computers, wireless headphones, home appliances, cars and even some light bulbs. In 2022 alone, about 32 thousand of new products were authorized.

The documents submitted to the FCC in this regulatory process contain detailed information about the product and its producer. The purpose of this disclosure is for consumers, engineers, and regulatory agencies to be able to verify that marketed devices meet regulatory standards. Today, the documents are publicly accessible on the FCC’s website (this was not always the case, as I elaborate later).22endnote: 2Available at <https://www.fcc.gov/oet/ea/fccid>. They represent a detailed overview of the most recent developments in the universe of all wireless-capable products introduced to the U.S. market, which is representative of the frontier of wireless technological development globally. The website is a valuable resource for reporting on product introductions (Weatherbed and Lawler, [2024](https://arxiv.org/html/2510.19377v1#bib.bib51), e.g.), and the user manuals from this database are widely circulated on the internet. To my knowledge, the dataset is presented here for the first time in an academic study, apart from (Kim et al., [2024](https://arxiv.org/html/2510.19377v1#bib.bib33)), who contemporaneously use it to analyze the effects of open-source drivers on Wifi router supply chains.

## 4 Dataset construction

I construct the dataset by web-scraping the universe of all product applications submitted to the FCC from 1981 to 2021 from FCC’s website. I start with firm identification based on a cleaned name and country and a list of all products and application dates of each firm.33endnote: 3I use Application ID instead of the better known FCC ID as a unit of analysis. About 20 percent of products contain more than one regulated wireless-capable device under different class or technology. To avoid a multi-level data structure, I perform all analysis on the Application ID level. For each product, I code its *Class* and the vector of frequencies it operates on. *NewFrequency* is a binary variable equal to 1 if the product uses a combination of frequencies not used by any prior product. The analysis primarily focuses on the subset of new products containing new frequencies.

As the primary outcome variable, I count the future products that used the same combination of frequencies within 5 years after the introduction of the focal product, *ForwardUse*.44endnote: 4Robustness checks include three and seven year definitions. The count approximates the follow-on use of a narrowly defined technology after its introduction in the new product. The approach is akin to identifying innovative products based on new product characteristics (Argente and Yeh, [2022](https://arxiv.org/html/2510.19377v1#bib.bib3)) or tracking future patent applications in a narrow patent class (Bell et al., [2018](https://arxiv.org/html/2510.19377v1#bib.bib7); Rigby, [2015](https://arxiv.org/html/2510.19377v1#bib.bib44); Hall et al., [2001](https://arxiv.org/html/2510.19377v1#bib.bib29)). Compared to FCC product classes, which are broad and of which there are only about a hundred in the dataset, using frequency combinations generates thousands of unique narrow technology combinations in the period of interest. Based on a manual review of the data, products using the same set of frequencies are often closely related: for example, they may be two wireless crane controllers or two phones with identical wireless connectivity but different designs (see examples below).

I count separately the future frequency use by the originator firm that applied for the first product (*ForwardUse, Originator*) and by other firms (*ForwardUse, Treatment*). There are about five times as many future uses by competitors as by the originator. Among competitors’ future use, I split the count between products by incumbents and new entrants (*Incumbent*, *Entrant*), products in the same class as the original product and in a different class (*InClass*, *OutClass*). Depending on whether the follow-on product was introduced by a country that joined the World Trade Organization (WTO) prior to 1998, I further split the count by domestic, foreign WTO and foreign non-WTO firms (*Domestic*, *Foreign (Non-)WTO*), and the combination of these splits.55endnote: 5Dates of accession taken from <http://web.archive.org/web/20251021112700/https://www.wto.org/english/res_e/booksp_e/sli_e/4wtomembers.pdf>.

The FCC requires each applicant to submit documentation including external and internal photos, block diagram, schematics, parts list, technical description, list of operation frequencies, and a form listing product classification, applicant details, and product description. I code *Post* equal to 1 if these documents were made available online by the transparency shock. The applicant can claim confidentiality on some of the documents if they contain a trade secret or confidential information.66endnote: 6The FCC distinguishes between short- and long-term confidentiality. I disregard short-term confidentiality because it is highly correlated with long-term confidentiality and its effect is time-limited. Documents that may be designated as long-term confidential include: schematics, block diagrams, operational descriptions, parts lists, and tune-up information; and, in rare cases, internal photos and the user manual. The applicant must justify the request in a letter and pay a fee that, in 1998, amounted to 130 dollars. (Federal Communications Commission, [1998a](https://arxiv.org/html/2510.19377v1#bib.bib22)). Applications classified for national security reasons are under a stricter regime, and are not available in this dataset here. I code *Secrecy* as a binary variable equal to 1 if the applicant claimed confidentiality. Even if the applicant claims confidentiality, some of the documents remain publicly available—an increase in information compared to the prior period. For this reason and to avoid overestimating the effects of transparency due to self-selection, even applications claiming secrecy are considered as being affected by the transparency shock in the post period.

To control for confounding variables discussed below, I code *Internet* as a binary variable equal to 1 if the product uses frequency that is associated with 3G, 4G or wifi internet connectivity (details in Appendix LABEL:apx:sec:internet). I also code products that were subject to deregulation by mapping the deregulated FCC rules (details in Appendix LABEL:apx:sec:deregulated). I further match the dataset to USPTO / PatentsView data by firm cleaned name and country. I only consider U.S. patents even for foreign applicants, because the U.S. is the place of marketing of products under FCC regulation, and any potential infringement falls under the jurisdiction of the USPTO. *RecentPatent* is a binary variable equal to 1 if the firm applied for at least one patent within three years prior to the FCC application.

As alternative outcomes, S​u​r​v​i​v​a​ly,iSurvival\_{y,i} equals 1 if the firm introduced a product y years after product ii or later and *NextPatent* and *NextSecrecy* equal to 1 if the firm had a recent patent or claimed secrecy in their next FCC application, respectively. Table LABEL:apx:tab:summary provides summary statistics.

### 4.1 Product examples

![Refer to caption](figures/figure_exhibits1.png)

Figure 1: Product example, FCC ID CBFCRANET1

Excerpts from documentation submitted to the FCC as part of the equipment authorization process, and available online: A) external photos, B) test results, C) user manual excerpt, D) schematics.



![Refer to caption](figures/figure_exhibits2.png)

Figure 2: Product example, FCC ID A3LSCH855

Excerpts from documentation submitted to the FCC as part of the equipment authorization process, and available online: A) external photos, B) test results, C) user manual excerpt. Schematics were claimed confidential by the applicant.

Two product examples illustrate the contents of the dataset. The product with FCC ID CBFCRANET1 is a crane control transmitter applied for by Control Chief Corporation, U.S., on October 5, 1998. It operates on one frequency, 433–434 MHz, a previously unused range. Four other products used this frequency within the next five years, one receiver by the same company, and another three products by different companies for similar use (‘industrial remote control‘ transceivers and receivers, for example). Seven exhibits of this application are available online (see Figure [1](https://arxiv.org/html/2510.19377v1#S4.F1 "Figure 1 ‣ 4.1 Product examples ‣ 4 Dataset construction ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") for excerpts). The firm did not claim secrecy on the exhibits, nor did it apply for a patent in the three years prior.

The product with FCC ID A3LSCH855 is a flip phone applied for by Samsung Electronics, U.S., on July 18, 2000. It uses three frequencies, two at 824–849 MHz and one at 825–848 MHz. The combination of frequencies is not new, as Sony Electronics, Germany, used it in a phone a year earlier. 32 exhibits from this application are available online (see Figure [2](https://arxiv.org/html/2510.19377v1#S4.F2 "Figure 2 ‣ 4.1 Product examples ‣ 4 Dataset construction ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") for excerpts); three additional exhibits are claimed confidential by Samsung: the block diagram, schematics, and circuit description. The firm applied for a patent in the three years prior.

## 5 Transparency shock

In 1998, the FCC implemented several changes to streamline the authorization process. These changes were presented at a 1997 IEEE conference (Knapp and Wall, [1997](https://arxiv.org/html/2510.19377v1#bib.bib35)), shown for public consultation (Federal Communications Commission, [1997a](https://arxiv.org/html/2510.19377v1#bib.bib20), [b](https://arxiv.org/html/2510.19377v1#bib.bib21)) and enacted in two orders (Federal Communications Commission, [1998a](https://arxiv.org/html/2510.19377v1#bib.bib22), [b](https://arxiv.org/html/2510.19377v1#bib.bib23)). As the main change of interest, the FCC digitalized the application process, and launched a publicly available website that details all products authorized by the FCC—the very website that I web-scraped in the data construction process.

In addition to digitalizing the application process, the FCC made available all prior product authorizations going back to 1981. In a key difference, only basic technical information became available for products authorized prior to digitization, whereas products authorized since digitization include all exhibits in PDF format, except those claimed confidential by the applicant. The digitalization was voluntary in the first year of the announcement, but compliance built fast: just eight months after, virtually all applications were submitted digitally.77endnote: 7An alternative explanation of the fast uptake is that FCC staff was scanning remaining paper applications to PDFs, as they indicated in their decision (Federal Communications Commission, [1998b](https://arxiv.org/html/2510.19377v1#bib.bib23), p. 11,333). In either case, the effect was that from November 1998, exhibits of virtually all applications were available on the website.

The policy shock did not change the public-access regime of the authorizations or the technical requirements. The information available online since the digitization had been available before through individual requests, as the FCC stated in response to concerns about confidentiality raised during the public consultation (Federal Communications Commission, [1998a](https://arxiv.org/html/2510.19377v1#bib.bib22)). The option to claim secrecy on some documents had also been available since before the policy change, but few applicants used it. In 1993, five years prior to the changes, only nine percent of applications claimed secrecy. This increased dramatically in the years leading up to and after the policy shock. Five years after the change, in 2003, 71 percent of applicants claimed secrecy (see Figure LABEL:apx:fig:secrecy\_patenting). Note that any reduction in the effects of the transparency shock due to this increase in secrecy would bias the results downward, as the empirical strategy treats all products in the post period as being exposed to the transparency shock, including those claiming confidentiality. Indeed, the results will show that as the use of secrecy increases following the transparency shock, the effects of the transparency shock diminish.

The availability of data on secrecy and the increase in its use in the late 1990s initially sparked my interest in FCC transparency policies during this period. I conceptualize the transparency policy change as a lowering of the costs of information about products regulated by the FCC, and estimate the effects of this cost reduction on the follow-on use of technologies described in the submitted documents. Detailed information on the most recent wireless-capable products became instantly available for anyone with internet connectivity, right from the moment of marketing. The simultaneous increase in the use of secrecy, patenting, and other appropriation mechanisms (Hall et al., [2014](https://arxiv.org/html/2510.19377v1#bib.bib27)), could signify a strategic response of firms that moderated the effect of the information availability over time. Next, I estimate the causal effect of the transparency shock on follow-on innovation, and provide some evidence on the strategic responses. Figure [3](https://arxiv.org/html/2510.19377v1#S5.F3 "Figure 3 ‣ 5 Transparency shock ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") presents the timeline of events, including several related changes during this period that I outline in the next section.

![Refer to caption](figures/figure_timeline.png)


Figure 3: Timeline of relevant events.

### 5.1 Empirical context

Several other changes occurred during the relevant time period that contextualize the transparency shock, and risk conflating the estimates of its effects. The founding of the WTO in 1995 and the accession of various countries in the subsequent decade establishes a potential confounder. The trade liberalization associated with the WTO may have had various effects: it may have increased the introduction of foreign follow-on products by both the originator and competitor, increased originator product introduction by non-U.S. firms, or increased product introduction as a follow-on to a U.S. products. These changes are not time invariant, but the two empirical strategies should limit their impact and elucidate the robustness of the results.

In the difference-in-differences design, follow-on products introduced by both the originator (control) and the competitor (treatment) would be affected similarly by the time-variant changes. A potential issue arises if the originator and competitor are located in countries affected differently by trade liberalization. Sub-population results in table[4](https://arxiv.org/html/2510.19377v1#S7.T4 "Table 4 ‣ 7.2 Foreign and domestic competition ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") elucidate these cross-country patterns. For the most conservative estimation, it estimates follow-on innovation by competitors in the same country as the originator, including on a subset of U.S. originators only (column 3). It also shows results of U.S. competitors following-on a non-U.S. originator (column 4), where the impact of trade liberalization would bias the estimates downwards. The table further splits foreign competitor products by early (prior to 1998) WTO membership, and isolates follow-on products from China and Taiwan (columns 2 and 3). As most countries acceded to the WTO in 1995, any major change in follow-on use of new frequency combinations should be observable in the pre-period. The dynamic treatment plot in figure [4](https://arxiv.org/html/2510.19377v1#S7.F4 "Figure 4 ‣ 7.3 Temporal dynamics and firm response ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") shows few deviations in pre-trends since three years prior to the transparency shock, which corresponds to the founding of WTO.

The regression discontinuity design puts the most weight on observations near the cutt-off date. This lays two to three years after most countries joined the WTO in 1995 and 1996, and three to four years prior to the accession of China and Taiwan in 2001 and 2002. The second event is of particular concern, as it was associated with an increase in imports into the U.S. Table LABEL:apx:tab:diff\_no\_china\_taiwan shows main results excluding firms from China and Taiwan from the analysis, both as originators and as competitors. All these results, discussed in detail later, show significant, if reduced, effect on follow-on product introduction by domestic and early WTO members.

Domestically, the Electronic Freedom of Information Act of 1996 mandated government agencies to publish specific records electronically by the end of 1999 (U.S.C., [1996a](https://arxiv.org/html/2510.19377v1#bib.bib49)). I did not find any changes in FCC policies beyond the transparency changes detailed above. The Telecommunications Act of 1996 significantly revised the original 1934 law, focusing on enabling market entry in internet telecommunications services markets and increasing interoperability and standardization. It did not directly change the technical requirements in the product authorization process, but an amendment to Section 302 enabled the delegation of equipment testing and certification to private laboratories (U.S.C., [1996b](https://arxiv.org/html/2510.19377v1#bib.bib50); Emeritz, [1996](https://arxiv.org/html/2510.19377v1#bib.bib19)). This meant that the mandatory testing documentation firms submit in their authorization applications became more often provided by an external testing provider. The causal identification strategies outlined below are robust to the effects of these changes, as products applied for in the treatment and control groups and in the pre- and post-periods would be affected equally by this change.

The American Inventor’s Protection Act (AIPA) of 1999 accelerated disclosure of patent applications. Prior literature found a positive effect on follow-on innovation which may have spilled-over to products that use patented technologies in the dataset (Hegde and Luo, [2018](https://arxiv.org/html/2510.19377v1#bib.bib32); Kim and Valentine, [2021](https://arxiv.org/html/2510.19377v1#bib.bib34); Baruffaldi and Simeth, [2020](https://arxiv.org/html/2510.19377v1#bib.bib6); Hegde et al., [2023](https://arxiv.org/html/2510.19377v1#bib.bib31)). I control for this effect with a binary variable *AIPA* equal 1 for applications submitted by applicants with recent patents on or after its effective date of November 29, 2000.

A second set of changes the FCC implemented in 1998 changed the regulatory regime of several product categories, mainly by deregulating some products that do not actively emit electromagnetic signal (Federal Communications Commission, [1997a](https://arxiv.org/html/2510.19377v1#bib.bib20), [1998a](https://arxiv.org/html/2510.19377v1#bib.bib22)). The deregulated products no longer had to acquire prior authorization from the FCC unless the firm submitted an application voluntarily. This implies that such products would stop appearing in the dataset. To avoid conflation from a selection bias stemming from the co-occurrence of the two events, I mapped regulatory changes to product categories and excluded all deregulated product from the analysis, including those submitted prior to the policy change. See Appendix LABEL:apx:sec:deregulated for details and validation of the process.

The period of interest also saw the entry of the first wireless internet-connected devices. To control for the effects of this development, I map the frequencies of 3G, 4G and Wifi technologies, and code *Internet* as a binary variable equal 1 if the product had internet capability. Appendix LABEL:apx:sec:internet lists these frequencies and details the process.

## 6 Empirical strategy

I evaluate the effect of transparency on follow-on innovation on a subset of products that introduced a previously unused frequency combination (*NewFrequency* = 1). I estimate the causal effect of a product application having exhibits published online, *Post*, on the number of products that use the new frequency combination in the next five years (*ForwardUse*).

Simply regressing *Post* on *ForwardUse* would be insufficient for this purpose. Selection into the transparency treatment in the uptake period is voluntary and could bias the estimates. For example, more innovative firms might more likely introduce new frequencies and voluntarily use the digitalized submission process; or they could try to avoid disclosure associated with digitalization. A time-dependent confounder could affect the outcome in the pre- or post-period and bias the results. To overcome these challenges, I use two causal identification strategies: difference-in-differences and regression discontinuity designs. The difference-in-differences design enables estimating the change over time and on sub-populations. The regression discontinuity design enables estimating effects on alternative outcomes.

### 6.1 Difference-in-differences

The difference-in-differences strategy leverages the fact that the transparency shock provides new information only to competitors and not the originator firm. It differentiates between *which firm* introduces the follow-on product: whereas the originator already knows the details of its product’s technologies and does not benefit from it being available online, the competitor gains new information from the increased transparency. The shock affects forward use of the frequency only by the competitors (treatment) and not the originator (control). Formally:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L​o​g​(F​o​r​w​a​r​d​U​s​ei,c)\displaystyle Log(ForwardUse\_{i,c}) | =α+β1⋅P​o​s​ti⋅T​r​e​a​t​m​e​n​tc\displaystyle=\alpha+\beta\_{1}\cdot Post\_{i}\cdot Treatment\_{c} |  | (1) |
|  | +\displaystyle+ | f​β2⋅P​o​s​ti+β3⋅T​r​e​a​t​m​e​n​tc+β4⋅I​n​t​e​r​n​e​ti\displaystyle f\beta\_{2}\cdot Post\_{i}+\beta\_{3}\cdot Treatment\_{c}+\beta\_{4}\cdot Internet\_{i} |  |
|  | (+\displaystyle(+ | β4⋅AIPAi+β5⋅Treatmentc⋅AIPAi)+γi¯⋅P​r​o​d​u​c​ti¯+εi,c\displaystyle\beta\_{4}\cdot AIPA\_{i}+\beta\_{5}\cdot Treatment\_{c}\cdot AIPA\_{i})+\bar{\gamma\_{i}}\cdot\bar{Product\_{i}}+\varepsilon\_{i,c} |  |

where F​o​r​w​a​r​d​U​s​ei,cForwardUse\_{i,c} denotes the count of products that used the frequency combination first used by product ii five years post its application date. For each product, I calculate F​o​r​w​a​r​d​U​s​eForwardUse separately for the originator (c=0c=0, control) and competitors (treatment, c=1c=1). P​o​s​tiPost\_{i} indicates if the product was registered in the pre-period (before March 1, 1998) or post-period (after October 31, 1998). T​r​e​a​t​m​e​n​tcTreatment\_{c} denotes the treatment group, forward use by competitors. A​I​P​Ai⋅T​r​e​a​t​m​e​n​tAIPA\_{i}\cdot Treatment and A​I​P​AiAIPA\_{i} control for the effects of AIPA whenever I include observations in its implementation period.

P​r​o​d​u​c​ti¯\bar{Product\_{i}} denotes a vector of product random effects which I add to absorb the effects of product-level characteristics and time-determined policy changes. I use random effects instead of fixed effects because of the limited number of observations per unit, the over-dispersion of the outcome variable, and the convergence issues with fixed effects models. The random effects partially pool information across products to generate stable conservative coefficient estimates (Clark and Linzer, [2015](https://arxiv.org/html/2510.19377v1#bib.bib15); Bell et al., [2019](https://arxiv.org/html/2510.19377v1#bib.bib8)).

As the outcome variable is an over-dispersed count, I use a negative-binomial model. I cluster standard errors on the frequency level. 88endnote: 8In a rare case, more than one product is introduced on the same date with the same new frequency combinations. I keep both products. As I expect the effect to differ in time, I present results from observations two, four, and ten years post the uptake period, with four years in the pre-period. I also estimate the dynamic treatment effect, where I interact the treatment group with year-fixed effects. Finally, I include a binary-outcome logistic regression and non-zero observations negative binomial regression with fixed effects as a robustness check.

The causal identification rests on the assumption of parallel trends: absent the transparency shock, the forward use of newly introduced frequency combinations would evolve similarly for the applicant and competitors. I cannot directly test this assumption. However, linear pre-trends in Table LABEL:apx:tab:diff\_time (Wing et al., [2018](https://arxiv.org/html/2510.19377v1#bib.bib53)) and staggered regression plots in Figure [4](https://arxiv.org/html/2510.19377v1#S7.F4 "Figure 4 ‣ 7.3 Temporal dynamics and firm response ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") do not show significant pre-trends.

The presence of spillovers could cause a violation of the parallel trends assumption in the post-period. Increased product market entry by competitors could affect the original firm’s product introduction. This could either induce the firm to introduce further products to keep up with the competition, biasing the estimates negatively, or drive the firm out of the technology, biasing the estimates positively. The next section describes a regression discontinuity design, where I substitute the outcome variable, and show that the transparency shock had no significant effect on forward use by the originator (despite a potential negative effect on firm survival). As the forward use by the original firm serves as the baseline in the difference-in-differences, this result provides evidence that the average spillover effect is insignificant. The regression discontinuity design on the main outcome of interest also has the advantage of not relying on a control group, serving as a further validation of the findings.

### 6.2 Discontinuity

I leverage the sharp discontinuity in the availability of information for products registered just before and after the transparency shock. Whereas products authorized in February 1998 did not have exhibits available online, over 90 percent of products authorized in April did, and so did virtually all products authorized in November of the same year. When other firms developed their products, they had significantly more information on the latter products, even though they were registered just a few weeks later. I compare products just before (control) and after the transparency shock (treatment). Formally:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Yi\displaystyle\hskip 0.0ptY\_{i} | =α+β1⋅P​o​s​ti⋅D​i​s​t​a​n​c​ei+β2⋅P​o​s​ti+β3​D​i​s​t​a​n​c​ei+εi\displaystyle=\alpha+\beta\_{1}\cdot Post\_{i}\cdot Distance\_{i}+\beta\_{2}\cdot Post\_{i}+\beta\_{3}Distance\_{i}+\varepsilon\_{i} |  | (2) |

where tt is time in weeks, and YiY\_{i} is the weekly mean of one of the following values over products jj introduced in the week tt: L​o​g​(F​o​r​w​a​r​d​U​s​e,T​r​e​a​t​m​e​n​tj+0.01)Log(ForwardUse,Treatment\_{j}+0.01), L​o​g​(F​o​r​w​a​r​d​U​s​e,S​e​l​fj+0.01)Log(ForwardUse,Self\_{j}+0.01), N​e​x​t​S​e​c​r​e​c​yjNextSecrecy\_{j}, N​e​x​t​P​a​t​e​n​tjNextPatent\_{j}, and S​u​r​v​i​v​a​ly,jSurvival\_{y,j} for y∈{1,3,5}y\in\{1,3,5\} (see above for definitions). P​o​s​tiPost\_{i} denotes the treatment period, D​i​s​t​a​n​c​eiDistance\_{i} denotes the running variable, measuring the number of weeks until or from the treatment.

I use the sharp regression discontinuity design, which fits a non-parametric local regression following Calonico et al. ([2015](https://arxiv.org/html/2510.19377v1#bib.bib14)). I rely on robust estimates and report results from polynomials of degree one (main), two, and three, and let the algorithm choose optimal bandwidth from ten years of observations prior and post the shock, and use a triangular kernel.

The uptake period complicates the discontinuity design (Noack and Rothe, [2023](https://arxiv.org/html/2510.19377v1#bib.bib40)). Excluding observations from the uptake period (so-called donut model) risks introducing artificial discontinuity and noise. Including observations from the uptake period risks underestimating the treatment effects, because treatment was incomplete. Thanks to the fast uptake (over 90 percent in April 1998), this downward bias might be limited. I present results from both approaches, which are broadly consistent. I refer to estimates from the specifications inclusive of the treatment period as the main (conservative) results.

I further test the significance of the findings by estimating the main model for each outcome variable on 6,942 placebo dates. These are all dates from ten years prior to and post the true event, excluding one year closest on each side. I then calculate the bootstrapped P value by comparing the coefficient sizes of the true event and the placebo estimations.

## 7 Results

Table 1: Main difference-in-difference regression results

|  |  |  |  |
| --- | --- | --- | --- |
| Dependent variable: | ForwardUse | | |
| Bandwidth (years): | Two | Four | Ten |
| Model: | (1) | (2) | (3) |
| Variables |  |  |  |
| Post ×\times Treatment | 0.869\*\*\* | 1.323\*\*\* | 0.755\*\*\* |
|  | (0.225) | (0.216) | (0.189) |
| Random effects |  |  |  |
| Product | Yes | Yes | Yes |
|  | [1.09] | [1.04] | [1.014] |
| Fixed effects |  |  |  |
| Treatment | Yes | Yes | Yes |
| Post | Yes | Yes | Yes |
| Internet | Yes | Yes | Yes |
| AIPA |  | Yes | Yes |
| AIPA ×\times Treatment |  | Yes | Yes |
| Fit statistics |  |  |  |
| Observations | 4,466 | 7,324 | 23,484 |
| Underlying products | 2,233 | 3,662 | 11,742 |
| R2R^{2} marginal | 0.188 | 0.282 | 0.185 |
| R2R^{2} conditional | 0.480 | 0.508 | 0.429 |
| AIC | 6228.2 | 11024.0 | 29527.9 |
| BIC | 6273.1 | 11086.1 | 29600.5 |
| Over-dispersion | 0.187 | 0.136 | 0.124 |

Results of the main difference-in-difference specifications, estimated on observations four years prior and two, four, and ten years post the uptake period, uptake period observations omitted. Follow-on products by originator firm in the pre-treatment period constitute the baseline. Random effects standard deviation in squared brackets, standard errors clustered at the product level.

\* p <0.1<0.1, \*\* p <0.05<0.05, \*\*\* p <0.01<0.01

The difference-in-differences results show a statistically significant and meaningful increase in follow-on innovation among products exposed to the transparency treatment using both methods. The main model, summarized in table [1](https://arxiv.org/html/2510.19377v1#S7.T1 "Table 1 ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") estimates that the transparency shock increased the use of new technologies by e​x​p​(0.755)=2.13exp(0.755)=2.13 about 113 percent (P << 0.01) for products introduced in the following ten years (column 5), or about twice compared to what it would have been absent the transparency shock. These effects are larger (276 percent, P << 0.01) when considering products introduced four years after the transparency shock (column 3). Controlling for AIPA has no significant effect on the coefficient size.

Table 2: Regression discontinuity design results, forward use

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Dependent variable: | FordwardUse, Treatment | | | | | |
| Uptake period: | Included | | | Omitted | | |
| Polynomial: | Linear | Quadratic | Cubic | Linear | Quadratic | Cubic |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Estimates |  |  |  |  |  |  |
| Conventional | 1.066\*\*\* | 1.319\*\*\* | 1.437\*\*\* | 0.602\*\* | 2.375\*\*\* | 3.041\*\*\* |
|  | (0.268) | (0.331) | (0.355) | (0.270) | (0.701) | (0.845) |
| Bias-corrected | 1.185\*\*\* | 1.433\*\*\* | 1.503\*\*\* | 0.628\*\* | 2.657\*\*\* | 3.289\*\*\* |
|  | (0.268) | (0.331) | (0.355) | (0.270) | (0.701) | (0.845) |
| Robust | 1.185\*\*\* | 1.433\*\*\* | 1.503\*\*\* | 0.628\* | 2.657\*\*\* | 3.289\*\*\* |
|  | (0.297) | (0.361) | (0.386) | (0.336) | (0.756) | (0.916) |
| Bandwidth (weeks) | 98 | 131 | 200 | 128 | 109 | 166 |
| Bandwidth type | Optimal | Optimal | Optimal | Optimal | Optimal | Optimal |
| Kernel type | Triangular | Triangular | Triangular | Triangular | Triangular | Triangular |

Linear (1, 4), quadratic (2, 5), and cubic (3, 6) discontinuity estimates of the effect of the policy change on forward use by competitors. The uptake period included with discontinuity on March 1, 1998 (1–3) and excluded with discontinuity on July 1, 1998 (4–6).
  
\* p <0.1<0.1, \*\* p <0.05<0.05, \*\*\* p <0.01<0.01

The discontinuity regression results, presented in table [5](https://arxiv.org/html/2510.19377v1#S7.T5 "Table 5 ‣ 7.3 Temporal dynamics and firm response ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products"), show a similarly sized increase in follow-on use of a technology introduced just after the policy shift compared to those introduced just before. Considering the robust linear polynomial results (column 1), the transparency treatment increased the number of follow-on products by 83 percent (P << 0.01). The results are consistent in magnitude across the degrees of polynomials, although statistical significance decreases with the degree three polynomial. Discontinuity plots in Figure LABEL:apx:fig:rdd\_main also show a sudden increase in the follow-on use by competitors. In the placebo test, the main result of 0.829 is higher than 97.1 percent of placebo runs.

A series of robustness checks confirm this main result. Table [5](https://arxiv.org/html/2510.19377v1#S7.T5 "Table 5 ‣ 7.3 Temporal dynamics and firm response ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products")A shows no statistically significant change in forward use by the original firm. The coefficients are positive but statistically insignificant (bootstrapped P 0.16 for the main coefficient of 0.25). This supports the assumption of no negative spillovers from the treatment group in the difference-in-differences design that would inflate the main result.

Next, I estimate two complementary specifications: table LABEL:apx:tab:diff\_logit shows the results of a logistic regression with a binary outcome (indicating if at least one further product used the frequency combination), and table LABEL:apx:tab:diff\_nonzero shows the results of a negative-binomial regression estimated only on products with at least one follow-on innovation, using product fixed effects instead of random effects. The product fixed effects absorb all the product-level constant variables included in the main specification. Further, table LABEL:apx:tab:diff\_time shows results of the main model with linear time pre-trends, and table LABEL:apx:tab:diff\_dependent\_var shows results with variations on the dependent variable definition to count three, five (main), and seven years of forward use.

All these robustness checks are consistent with the main findings. Treated products have a higher probability of at least one follow-up product in the same frequency (table LABEL:apx:tab:diff\_logit), and the count is higher among those with at least one follow-up (table LABEL:apx:tab:diff\_nonzero). The linear time pre-trend is insignificant and does not significantly change the main coefficient of interest (table LABEL:apx:tab:diff\_time). Variations on the dependent variable definition (table LABEL:apx:tab:diff\_dependent\_var) result in comparable estimates, with the three-year definition showing a smaller effect and the seven-year definition resulting in a larger effect. Together, these results consistently show that the transparency shock meaningfully increased the introduction of new products in narrowly defined technologies.

### 7.1 Novelty and class

Table 3: Difference-in-differences, class

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Dependent variable: | ForwardUse | | | |
| Bandwidth (years): | Four | | | |
| Model: | (1) | (2) | (3) | (4) |
| Product subsample: |  |  | U.S. | Non-U.S. |
| Variables |  |  |  |  |
| Post ×\times NewEntrant | 1.249\*\*\* |  |  |  |
|  | (0.162) |  |  |  |
| Post ×\times NewClassEntrant | 1.072\*\*\* |  |  |  |
|  | (0.199) |  |  |  |
| Post ×\times Incumbent | 1.043\*\*\* |  |  |  |
|  | (0.201) |  |  |  |
| Post ×\times Domestic, InClass |  | 0.695\*\*\* | 0.289 | 2.190\*\*\* |
|  |  | (0.226) | (0.254) | (0.485) |
| Post ×\times Domestic, OutClass |  | 0.980\*\*\* | 0.522\* | 2.771\*\*\* |
|  |  | (0.246) | (0.276) | (0.590) |
| Post ×\times Foreign, InClass |  | 1.573\*\*\* | 1.208\*\*\* | 1.929\*\*\* |
|  |  | (0.225) | (0.280) | (0.379) |
| Post ×\times Foreign, OutClass |  | 1.278\*\*\* | 0.833\*\*\* | 1.598\*\*\* |
|  |  | (0.236) | (0.297) | (0.392) |
| Random effects |  |  |  |  |
| Product | Yes | Yes | Yes | Yes |
|  | [2.79] | [2.78] | [2.99] | [2.36] |
| Fixed effects |  |  |  |  |
| Post | Yes | Yes | Yes | Yes |
| Internet | Yes | Yes | Yes | Yes |
| AIPA | Yes | Yes | Yes | Yes |
| NewEntrant + NewClassEntrant + Incumbent | Yes |  |  |  |
| AIPA ×\times NewEntrant | Yes |  |  |  |
| AIPA ×\times NewClassEntrant | Yes |  |  |  |
| AIPA ×\times Incumbent | Yes |  |  |  |
| Domestic, InClass + Domestic, OutClass |  | Yes | Yes | Yes |
| Foreign, InClass + Foreign, OutClass |  | Yes | Yes | Yes |
| AIPA ×\times Domestic, InClass |  | Yes | Yes | Yes |
| AIPA ×\times Domestic, OutClass |  | Yes | Yes | Yes |
| AIPA ×\times Foreign, InClass |  | Yes | Yes | Yes |
| AIPA ×\times Foreign, OutClass |  | Yes | Yes | Yes |
| Fit statistics |  |  |  |  |
| Observations | 14,648 | 18,310 | 12,260 | 6,050 |
| Underlying products | 3,662 | 3,662 | 2,452 | 1,210 |
| R2R^{2} marginal | 0.072 | 0.031 | 0.022 | 0.164 |
| R2R^{2} conditional | 0.903 | 0.849 | 0.876 | 0.821 |
| AIC | 14474.8 | 16459.7 | 9259.7 | 6914.8 |
| BIC | 14588.7 | 16600.4 | 9393.2 | 7035.6 |
| Over-dispersion | 1.1 | 0.385 | 0.496 | 0.349 |

Results of the sub-population difference-in-differences specifications of (1) new entrants, new entrants in class, and incumbent, (2) domestic and foreign in class and out class, (3) – on a subset of U.S. products, (4) – on a subset of non-U.S. products. ForwardUse by the originator in the pre-treatment period constitutes the baseline.

To investigate what kinds of products and firms drive the increase in follow-on use of the technologies, I turn to sub-population analysis within the difference-in-differences approach. Table [3](https://arxiv.org/html/2510.19377v1#S7.T3 "Table 3 ‣ 7.1 Novelty and class ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") shows results of models that split the treatment group count by incumbency, country, and new class. To highlight the differences, all models use the four year bandwidth that showed strongest results in the main specification.

Column (1) analyzes if the transparency shock favored new entrants by splitting the outcome between new entrants (firms with no prior products), new entrants in class (firms with prior products but not in the focal product’s class) and incumbents (firms with prior products in the same class). It shows no statistically significant differences between these groups (two-tail P 0.42 and 0.49 between new entrants and incumbents, and between new entrants and new class entrants, respectively), indicating that both incumbents and new entrants increased their use of new technologies.

Adding a split by foreign and domestic enhances the pattern of category competition (columns 2–4). Overall, the transparency shock increased product introduction both in the same class as the focal product and in another class by a similar magnitude (P 0.39 and 0.4 within domestic and foreign firms, respectively, column 2). This suggests that the follow-on innovation included not only mere copies of the focal product but also an innovative step, proxied by a change of classification. However, the results suggest this differs by country. For products introduced by U.S. firms (column 3), the highest increase in forward use was among foreign products in class. For non-U.S. firms (column 4), it was among domestic products in another class. The results are underpowered for systematic comparisons but suggest that follow-on innovation to U.S. products was more likely in the form of foreign copies, while follow-on innovation to non-U.S. products was more likely in the form of domestic novel products.

### 7.2 Foreign and domestic competition

Table 4: Difference-in-differences, foreign competitors

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Dependent variable: | ForwardUse | | | |
| Bandwidth (years): | Four | | | |
| Model: | (1) | (2) | (3) | (4) |
| Product subsample: |  |  | U.S. | Non-U.S. |
| Variables |  |  |  |  |
|  | (1) | (2) | (3) | (4) |
| Post ×\times Domestic | 0.8210.821\*\*\* | 0.8010.801\*\*\* | 0.3890.389\* | 2.5842.584\*\*\* |
|  | (0.1980.198) | (0.2010.201) | (0.2230.223) | (0.4330.433) |
| Post ×\times Foreign, early WTO | 1.2391.239\*\*\* | 1.2191.219\*\*\* | 0.5890.589\*\* | 2.3112.311\*\*\* |
|  | (0.1990.199) | (0.2030.203) | (0.2470.247) | (0.4440.444) |
| Post ×\times Foreign, China |  | 1.7591.759\*\*\* | 1.9201.920\*\*\* |  |
|  |  | (0.4080.408) | (0.6690.669) |  |
| Post ×\times Foreign, Taiwan |  | 2.4042.404\*\*\* | 2.5462.546\*\*\* |  |
|  |  | (0.2990.299) | (0.3950.395) |  |
| Post ×\times Foreign, U.S. |  |  |  | 1.5321.532\*\*\* |
|  |  |  |  | (0.3560.356) |
| Post ×\times Foreign, other | 2.3252.325\*\*\* | 19.06819.068 | −1.500-1.500 | 2.3112.311\*\*\* |
|  | (0.2740.274) | (10 567.25210\,567.252) | (3624.2263624.226) | (0.4440.444) |
| Random effects |  |  |  |  |
| Product | Yes | Yes | Yes | Yes |
|  | [2.83] | [2.85] | [3.01] | [3.02] |
| Fixed effects |  |  |  |  |
| Post | Yes | Yes | Yes | Yes |
| Internet | Yes | Yes | Yes | Yes |
| AIPA | Yes | Yes | Yes | Yes |
| Foreign, Domestic | Yes | Yes | Yes | Yes |
| Foreign, early WTO | Yes | Yes | Yes | Yes |
| Foreign, other | Yes | Yes | Yes | Yes |
| Foreign, China |  | Yes | Yes |  |
| Foreign, Taiwan |  | Yes | Yes |  |
| Foreign, U.S. |  |  |  | Yes |
| Foreign, Domestic ×\times AIPA | Yes | Yes | Yes | Yes |
| Foreign, early WTO ×\times AIPA | Yes | Yes | Yes | Yes |
| Foreign, other ×\times AIPA | Yes | Yes | Yes | Yes |
| Foreign, China ×\times AIPA |  | Yes | Yes |  |
| Foreign, Taiwan ×\times AIPA |  | Yes | Yes |  |
| Foreign, U.S. ×\times AIPA |  |  |  | Yes |
| Fit statistics |  |  |  |  |
| Observations | 14.64814.648 | 21.97221.972 | 14.71214.712 | 6.0506.050 |
| Underlying products | 3.6623.662 | 3.6623.662 | 2.4522.452 | 1.2101.210 |
| R2R^{2} marginal | 0.0640.064 | 0.8050.805 | 0.8550.855 | 0.0870.087 |
| R2R^{2} conditional | 0.8640.864 | 0.9710.971 | 0.9820.982 | 0.8790.879 |
| AIC | 15 154.215\,154.2 | 15 670.015\,670.0 | 8705.28705.2 | 6726.16726.1 |
| BIC | 15 268.115\,268.1 | 15 837.915\,837.9 | 8864.88864.8 | 6846.86846.8 |
| Over-dispersion | 0.549 | 0.502 | 0.726 | 0.53 |

Results of the sub-population difference-in-differences specifications of (1) new entrants, new entrants in class, and incumbent, (2) domestic and foreign, (3) domestic on a subset of U.S. products, (4) domestic, U.S., and non-U.S. foreign on a subset of non-U.S. products (5) domestic and foreign in class and out class, (6) – on a subset of U.S. products, (7) – on a subset of non-U.S. products. ForwardUse by the originator in the pre-treatment period constitutes the baseline.

Table [4](https://arxiv.org/html/2510.19377v1#S7.T4 "Table 4 ‣ 7.2 Foreign and domestic competition ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") analyzes the differentiated impact on domestic and foreign firms. Column (1) shows that domestic firms, early WTO members, and other foreign firms increased their use of new technologies, but the second two significantly more than the first. While domestic firms increased their product introduction by e​x​p​(0.821)=2.27exp(0.821)=2.27 or 127 percent, early WTO members by e​x​p​(1.239)=2.45exp(1.239)=2.45 or 245 percent, and competitors from foreign countries by e​x​p​(2.325)=10.23exp(2.325)=10.23, or 923 percent. Column (2) shows that this is mainly driven by firms in China and Taiwan as the coefficient on other foreign countries becomes insignificant.

Further details emerge in a split between products introduced by U.S. and non-U.S. firms. U.S. firms show lower, although still significant (P 0.08) increase in domestic follow-on use of e​x​p​(0.389)=1.48exp(0.389)=1.48 or 48 percent, and in early WTO members of e​x​p​(0.589)=1.8exp(0.589)=1.8 or 80 percent. Here, too, the main increase is driven by products from China and Taiwan, with a magnitude comparable to the whole sample (P 0.84 and 0.77, respectively). Among products introduced by Non-U.S. firms (column 4), the difference between early WTO members and domestic forward use diminishes (P 0.66). Interestingly, the magnitude of the increase in follow-on use by U.S. firms with respect to products by non-U.S. firms is higher than with respect to domestic firms (column 3, P 0.01) and comparable to the increase in follow-on use by Chinese firms with respect to products introduced by U.S. firms (P 0.61). The nominally highest effect of e​x​p​(2.584)=13.23exp(2.584)=13.23, or 1,325 percent, is among domestic competitors of products by non-U.S. originators.

Together, this shows that the transparency shock had the weakest impact domestically in the U.S., and the strongest impact domestically outside the U.S. and internationally. This may be because U.S. firms had been able to access the relevant information through other channels prior to the transparency shock. Trade liberalization may have magnified these effects but is unlikely to have driven them. The significant coefficients on domestic competitors show that the transparency also affected competitors that did not benefit from trade liberalization compared to the originator, and the large coefficients on early WTO members show a significant differentiated effect also among countries that had joined several years prior to the transparency shock. Excluding China and Taiwan from the sample yields results of smaller magnitude but still significant and large in size (table LABEL:apx:tab:diff\_no\_china\_taiwan. Finally, the regression discontinuity results, mostly based on observations that do not coincide with WTO accession, show consistent results.

### 7.3 Temporal dynamics and firm response

![Refer to caption](figures/figure_diff_dynamic.png)

Figure 4: Time-dynamic treatment effect.

Point and 95 percent confidence interval estimates of T​r​e​a​t​m​e​n​t​Y​e​a​r×T​r​e​a​t​m​e​n​tTreatmentYear\times Treatment interaction terms. Standard errors binned at product level. Baseline at year -1, year 0 represents uptake period and is omitted from the main model.

The positive effect of transparency on forward use varies in time. Figure [4](https://arxiv.org/html/2510.19377v1#S7.F4 "Figure 4 ‣ 7.3 Temporal dynamics and firm response ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") shows the increase in future use peaking in the fourth year with an average increase in use of 661 percent among domestic competitors, or over seven times. In time, the significance wanes, and drops to no effect eight years after the transparency shock. I interpret these dynamics as resulting from two mechanisms, both due to the transparency shock being largely unexpected. The transparency shock did not stem from a change in access regime. The documents made available on the website had been available to the public before but required individual requests; the launch of the website merely affected the mode and costs of access. I speculate that adjusting to the possibilities of this access explains the gradual uptake in the increase of forward use, as competitors made use of the availability of information on the most recent products. To counter this, originators became more protective of their technologies and employed innovation appropriation mechanisms to counter the increased transparency.

Table 5: Regression discontinuity design results: originator, secrecy, and patenting

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| A) Dependent variable: | FordwardUse, Originator | | | | | |
| Uptake period: | Included | | | Omitted | | |
| Polynomial: | Linear | Quadratic | Cubic | Linear | Quadratic | Cubic |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Estimates |  |  |  |  |  |  |
| Conventional | 0.196 | 0.271 | 0.081 | 0.131 | 0.290 | 0.021 |
|  | (0.195) | (0.208) | (0.275) | (0.279) | (0.311) | (0.599) |
| Bias-corrected | 0.250 | 0.304 | 0.020 | 0.189 | 0.328 | -0.075 |
|  | (0.195) | (0.208) | (0.275) | (0.279) | (0.311) | (0.599) |
| Robust | 0.250 | 0.304 | 0.020 | 0.189 | 0.328 | -0.075 |
|  | (0.229) | (0.235) | (0.297) | (0.350) | (0.367) | (0.692) |
| Bandwidth (weeks) | 116 | 230 | 193 | 102 | 206 | 178 |
| Bandwidth type | Optimal | Optimal | Optimal | Optimal | Optimal | Optimal |
| Kernel type | Triangular | Triangular | Triangular | Triangular | Triangular | Triangular |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| B) Dependent variable: | NextSecrecy | | | | | |
| Uptake period: | Included | | | Omitted | | |
| Polynomial: | Linear | Quadratic | Cubic | Linear | Quadratic | Cubic |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Estimates |  |  |  |  |  |  |
| Conventional | 0.098\* | 0.105\* | 0.117\* | 0.069 | 0.102 | 0.167 |
|  | (0.053) | (0.060) | (0.068) | (0.071) | (0.108) | (0.162) |
| Bias-corrected | 0.111\*\* | 0.119\*\* | 0.121\* | 0.072 | 0.123 | 0.189 |
|  | (0.053) | (0.060) | (0.068) | (0.071) | (0.108) | (0.162) |
| Robust | 0.111\* | 0.119\* | 0.121 | 0.072 | 0.123 | 0.189 |
|  | (0.063) | (0.066) | (0.074) | (0.088) | (0.126) | (0.187) |
| Bandwidth (weeks) | 141 | 236 | 296 | 153 | 189 | 220 |
| Bandwidth type | Optimal | Optimal | Optimal | Optimal | Optimal | Optimal |
| Kernel type | Triangular | Triangular | Triangular | Triangular | Triangular | Triangular |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| C) Dependent variable: | NextPatent | | | | | |
| Uptake period: | Included | | | Omitted | | |
| Polynomial: | Linear | Quadratic | Cubic | Linear | Quadratic | Cubic |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Estimates |  |  |  |  |  |  |
| Conventional | 0.109\*\* | 0.091 | 0.082 | 0.148\* | 0.159 | 0.149 |
|  | (0.053) | (0.076) | (0.084) | (0.086) | (0.109) | (0.150) |
| Bias-corrected | 0.122\*\* | 0.079 | 0.064 | 0.161\* | 0.151 | 0.125 |
|  | (0.053) | (0.076) | (0.084) | (0.086) | (0.109) | (0.150) |
| Robust | 0.122\* | 0.079 | 0.064 | 0.161 | 0.151 | 0.125 |
|  | (0.063) | (0.086) | (0.092) | (0.108) | (0.130) | (0.172) |
| Bandwidth (weeks) | 184 | 190 | 271 | 121 | 202 | 258 |
| Bandwidth type | Optimal | Optimal | Optimal | Optimal | Optimal | Optimal |
| Kernel type | Triangular | Triangular | Triangular | Triangular | Triangular | Triangular |

Linear (1, 4), quadratic (2, 5), and cubic (3, 6) discontinuity estimates of the effect of the policy change on (C) patenting in the next application and (B) secrecy in the next application. The uptake period included with discontinuity on March 1, 1998 (1–3) and excluded with discontinuity on July 1, 1998 (4–6).
  
\* p <0.1<0.1, \*\* p <0.05<0.05, \*\*\* p <0.01<0.01




Table 6: Regression discontinuity design results: survival

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| A) Dependent variable: | Survival, 1 year | | | | | |
| Uptake period: | Included | | | Omitted | | |
| Polynomial: | Linear | Quadratic | Cubic | Linear | Quadratic | Cubic |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Estimates |  |  |  |  |  |  |
| Conventional | -0.085\*\* | -0.110\*\* | -0.134\*\* | -0.100\*\* | -0.350\*\*\* | -0.454\*\*\* |
|  | (0.038) | (0.049) | (0.055) | (0.051) | (0.105) | (0.140) |
| Bias-corrected | -0.082\*\* | -0.123\*\* | -0.142\*\* | -0.093\* | -0.398\*\*\* | -0.503\*\*\* |
|  | (0.038) | (0.049) | (0.055) | (0.051) | (0.105) | (0.140) |
| Robust | -0.082\* | -0.123\*\* | -0.142\*\* | -0.093 | -0.398\*\*\* | -0.503\*\*\* |
|  | (0.045) | (0.053) | (0.059) | (0.063) | (0.117) | (0.150) |
| Bandwidth (weeks) | 157 | 172 | 181 | 140 | 119 | 160 |
| Bandwidth type | Optimal | Optimal | Optimal | Optimal | Optimal | Optimal |
| Kernel type | Triangular | Triangular | Triangular | Triangular | Triangular | Triangular |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| B) Dependent variable: | Survival, 3 years | | | | | |
| Uptake period: | Included | | | Omitted | | |
| Polynomial: | Linear | Quadratic | Cubic | Linear | Quadratic | Cubic |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Estimates |  |  |  |  |  |  |
| Conventional | -0.082\*\* | -0.121\*\* | -0.129\* | -0.120\*\* | -0.342\*\* | -0.323\*\* |
|  | (0.041) | (0.059) | (0.067) | (0.053) | (0.144) | (0.157) |
| Bias-corrected | -0.083\*\* | -0.140\*\* | -0.132\* | -0.111\*\* | -0.393\*\*\* | -0.374\*\* |
|  | (0.041) | (0.059) | (0.067) | (0.053) | (0.144) | (0.157) |
| Robust | -0.083\* | -0.140\*\* | -0.132\* | -0.111\* | -0.393\*\* | -0.374\*\* |
|  | (0.049) | (0.065) | (0.074) | (0.065) | (0.160) | (0.168) |
| Bandwidth (weeks) | 155 | 148 | 194 | 149 | 118 | 192 |
| Bandwidth type | Optimal | Optimal | Optimal | Optimal | Optimal | Optimal |
| Kernel type | Triangular | Triangular | Triangular | Triangular | Triangular | Triangular |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| C) Dependent variable: | Survival, 5 years | | | | | |
| Uptake period: | Included | | | Omitted | | |
| Polynomial: | Linear | Quadratic | Cubic | Linear | Quadratic | Cubic |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Estimates |  |  |  |  |  |  |
| Conventional | -0.099\*\* | -0.128\*\* | -0.149\*\* | -0.102\* | -0.178 | -0.284\*\* |
|  | (0.046) | (0.058) | (0.068) | (0.061) | (0.138) | (0.140) |
| Bias-corrected | -0.110\*\* | -0.143\*\* | -0.164\*\* | -0.100 | -0.228\* | -0.317\*\* |
|  | (0.046) | (0.058) | (0.068) | (0.061) | (0.138) | (0.140) |
| Robust | -0.110\*\* | -0.143\*\* | -0.164\*\* | -0.100 | -0.228 | -0.317\*\* |
|  | (0.054) | (0.064) | (0.074) | (0.076) | (0.154) | (0.156) |
| Bandwidth (weeks) | 132 | 170 | 205 | 146 | 130 | 226 |
| Bandwidth type | Optimal | Optimal | Optimal | Optimal | Optimal | Optimal |
| Kernel type | Triangular | Triangular | Triangular | Triangular | Triangular | Triangular |

Linear (1, 4), quadratic (2, 5), and cubic (3, 6) discontinuity estimates of the effect of the policy change on the survival of firms after (A) one, (B) three, and (C) five years. The uptake period included with discontinuity on March 1, 1998 (1–3) and excluded with discontinuity on July 1, 1998 (4–6).
  
\* p <0.1<0.1, \*\* p <0.05<0.05, \*\*\* p <0.01<0.01

The increase in the use of secrecy and patenting by firms during the relevant period suggests originators became protective of their inventions (see figure LABEL:apx:fig:secrecy\_patenting). A trend in the use of secrecy predates the transparency shock, complicating causal attribution. I tackle this limitation using the regression discontinuity design and evaluate if the transparency shock sharply increased the use of secrecy and recent patents in the *next* product submission. Table [5](https://arxiv.org/html/2510.19377v1#S7.T5 "Table 5 ‣ 7.3 Temporal dynamics and firm response ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") shows that secrecy (panel B) and patenting (panel C) in the subsequent product increased by approximately 11 and 12 percent, respectively (conventional estimates significant at the 90 percent level, bootstrapped P 0.02 and 0.04, respectively). This increase suggests a strategic shift toward innovation appropriation among firms proximate to the transparency shock cutoff.

Originator firms may seek appropriation mechanisms to mitigate potential negative consequences of increased access to their technology, such as heightened competition leading to market share and profit losses. I evaluate whether the transparency shock decreased the survival of affected firms using a regression discontinuity design. Table [6](https://arxiv.org/html/2510.19377v1#S7.T6 "Table 6 ‣ 7.3 Temporal dynamics and firm response ‣ 7 Results ‣ Government Transparency Affects Innovation: Evidence from Wireless Products") indicates that the survival of firms exposed to the transparency shock decreased by 8 and 11 percent after one and five years, respectively (statistically significant at 90 and 95 percent levels; bootstrapped P 0.06 and 0.08). These results suggest that transparency exposure may have increased market exit in subsequent years, potentially driven by heightened competition. Across these alternative outcome results, the donut specification with an omitted uptake period (columns 4–6 on each panel) yields broadly consistent results.

## 8 Conclusion

Government regulations affect the information environment in which firms innovate. To elucidate this dynamic, I test the causal effects of increased regulatory transparency on follow-on innovation. I focus on a late-1990s transparency shock that decreased the costs of accessing detailed technical information about all wireless-enabled devices marketed in the U.S., a globally representative high-tech industry.

The results indicate that government transparency increased business dynamism, as evidenced by increased market entry and exit, and facilitated the adoption of new technologies. The estimated negative effect on the survival of the original firm exposes a familiar tension in innovation policy: eased access to a new technology benefits competitors and consumers but may hinder the original firm’s ability to offset the costs of developing the technology in the first place (Hall et al., [2014](https://arxiv.org/html/2510.19377v1#bib.bib27)). In the long term, this dynamic may discourage innovation. These considerations preclude an unequivocally positive evaluation of increased transparency’s overall effects on innovation, as such an evaluation necessitates modeling firms’ strategic responses within a dynamic equilibrium of the altered information environment (Hall and Sena, [2017](https://arxiv.org/html/2510.19377v1#bib.bib30); Bryan and Williams, [2021](https://arxiv.org/html/2510.19377v1#bib.bib12)).

The main message from my analysis is that government transparency can have large effects on business innovation in ways that are typically not at the forefront of policy debates on transparency. As of this writing, the FCC product database remains unaffected by the discontinuations, although numerous other government websites have been terminated (Gotfredsen, [2025](https://arxiv.org/html/2510.19377v1#bib.bib25)). The findings highlight the information frictions present in innovation markets, and the power of government interventions in shaping the information environment in which firms innovate. Even regulations not directly aimed at supporting innovation can generate significant unintended effects by influencing information costs. As governments consider policies affecting information availability—such as algorithmic transparency, AI regulations, or restrictions on non-compete agreements—these results suggest potential secondary effects on innovation, even when this is not the primary objective.

## References

* Amato (1997)

  Amato, I. (1997).
  Island of Glass.
  MRS Bulletin 22(12), 54.
* Argente et al. (2021)

  Argente, D., S. Baslandze, D. Hanley, and S. Moreira (2021).
  Patents to Products: Product Innovation and Firm Dynamics.
  SSRN Electronic Journal.
* Argente and Yeh (2022)

  Argente, D. and C. Yeh (2022, February).
  Product Life Cycle, Learning, and Nominal Shocks.
  The Review of Economic Studies 89(6), 2992–3054.
  \_eprint: https://academic.oup.com/restud/article-pdf/89/6/2992/46869705/rdac004.pdf.
* Arrow (1962)

  Arrow, K. J. (1962).
  Economic Welfare and the Allocation of Resources for Invention.
  In The Rate and Direction of Inventive Activity: Economic and Social Factors. Princeton University Press.
* Arundel (2001)

  Arundel, A. (2001, April).
  The relative effectiveness of patents and secrecy for appropriation.
  Research Policy 30(4), 611–624.
* Baruffaldi and Simeth (2020)

  Baruffaldi, S. H. and M. Simeth (2020, May).
  Patents and knowledge diffusion: The effect of early disclosure.
  Research Policy 49(4), 103927.
* Bell et al. (2018)

  Bell, A., R. Chetty, X. Jaravel, N. Petkova, and J. Van Reenen (2018, November).
  Who Becomes an Inventor in America? The Importance of Exposure to Innovation\*.
  The Quarterly Journal of Economics 134(2), 647–713.
  \_eprint: https://academic.oup.com/qje/article-pdf/134/2/647/28289414/qjy028.pdf.
* Bell et al. (2019)

  Bell, A., M. Fairbrother, and K. Jones (2019, March).
  Fixed and random effects models: making an informed choice.
  Quality & Quantity 53(2), 1051–1074.
* Berkes and Nencka (2024)

  Berkes, E. and P. Nencka (2024, April).
  Knowledge Access: The Effects of Carnegie Libraries on Innovation.
  The Review of Economics and Statistics, 1–45.
* Bloom et al. (2013)

  Bloom, N., M. Schankerman, and J. Van Reenen (2013).
  Identifying technology spillovers and product market rivalry.
  Econometrica 81(4), 1347–1393.
  Publisher: Wiley Online Library.
* Bryan and Ozcan (2021)

  Bryan, K. A. and Y. Ozcan (2021, December).
  The Impact of Open Access Mandates on Invention.
  The Review of Economics and Statistics 103(5), 954–967.
* Bryan and Williams (2021)

  Bryan, K. A. and H. L. Williams (2021, August).
  Innovation: Market Failures and Public Policies.
  Working Paper 29173, National Bureau of Economic Research.
  Series: Working Paper Series.
* Burrell and Kelly (2015)

  Burrell, R. and C. Kelly (2015, November).
  Parliamentary Rewards and the Evolution of the Patent System.
  The Cambridge Law Journal 74(3), 423–449.
* Calonico et al. (2015)

  Calonico, S., M. Cattaneo, D., and R. Titiunik (2015).
  rdrobust: An R Package for Robust Nonparametric Inference in Regression-Discontinuity Designs.
  The R Journal 7(1), 38.
* Clark and Linzer (2015)

  Clark, T. S. and D. A. Linzer (2015).
  Should I Use Fixed or Random Effects?
  Political Science Research and Methods 3(2), 399–408.
* Cohen et al. (2000)

  Cohen, W., R. Nelson, and J. Walsh (2000, February).
  Protecting Their Intellectual Assets: Appropriability Conditions and Why U.S. Manufacturing Firms Patent (or Not).
  Technical Report w7552, National Bureau of Economic Research, Cambridge, MA.
* Corduneanu-Huci and Trlifaj (2024)

  Corduneanu-Huci, C. and S. Trlifaj (2024).
  Freedom of Information Acts (FOIAs) and Government Accountability.
  In Elgar Encyclopedia of Corruption and Society, Elgar Encyclopedia of Corruption and Society. Edward Elgar.
* Cox (2019)

  Cox, G. W. (2019, November).
  Patent disclosure and England’s early industrial revolution.
  European Review of Economic History 24(3), 447–467.
  \_eprint: https://academic.oup.com/ereh/article-pdf/24/3/447/33550976/hez012.pdf.
* Emeritz (1996)

  Emeritz, R. E. (Ed.) (1996).
  The Telecommunications Act of 1996: law & legislative history.
  Bethesda, Md.: Pike & Fischer.
* Federal Communications Commission (1997a)

  Federal Communications Commission (1997a).
  FCC Record 1997-5150, Volume 13.
  Washington D.C.: Government Printing Office.
* Federal Communications Commission (1997b)

  Federal Communications Commission (1997b).
  FCC Record 1997-8743, Volume 13.
  Washington D.C.: Government Printing Office.
* Federal Communications Commission (1998a)

  Federal Communications Commission (1998a).
  FCC Record 1998-11322, Volume 13.
  Washington D.C.: Government Printing Office.
* Federal Communications Commission (1998b)

  Federal Communications Commission (1998b).
  FCC Record 1998-11415, Volume 13.
  Washington D.C.: Government Printing Office.
* Furman et al. (2021)

  Furman, J. L., M. Nagler, and M. Watzinger (2021, November).
  Disclosure and Subsequent Innovation: Evidence from the Patent Depository Library Program.
  American Economic Journal: Economic Policy 13(4), 239–70.
* Gotfredsen (2025)

  Gotfredsen, S. G. (2025, February).
  Fighting the Great Federal Website Purge.
  Columbia Journalism Review.
* Gross (2023)

  Gross, D. P. (2023, April).
  The Hidden Costs of Securing Innovation: The Manifold Impacts of Compulsory Invention Secrecy.
  Management Science 69(4), 2318–2338.
* Hall et al. (2014)

  Hall, B., C. Helmers, M. Rogers, and V. Sena (2014).
  The Choice between Formal and Informal Intellectual Property: A Review.
  Journal of Economic Literature 52(2), 375–423.
* Hall and Harhoff (2012)

  Hall, B. H. and D. Harhoff (2012, September).
  Recent Research on the Economics of Patents.
  Annual Review of Economics 4(1), 541–565.
* Hall et al. (2001)

  Hall, B. H., A. B. Jaffe, and M. Trajtenberg (2001, October).
  The NBER Patent Citation Data File: Lessons, Insights and Methodological Tools.
  Working Paper 8498, National Bureau of Economic Research.
  Series: Working Paper Series.
* Hall and Sena (2017)

  Hall, B. H. and V. Sena (2017).
  Appropriability mechanisms, innovation, and productivity: evidence from the UK.
  Economics of Innovation and New Technology 26(1-2), 42–62.
* Hegde et al. (2023)

  Hegde, D., K. Herkenhoff, and C. Zhu (2023, July).
  Patent Publication and Innovation.
  Journal of Political Economy 131(7), 1845–1903.
* Hegde and Luo (2018)

  Hegde, D. and H. Luo (2018).
  Patent publication and the market for ideas.
  Management Science 64(2), 652–672.
  Publisher: INFORMS.
* Kim et al. (2024)

  Kim, D. Y., R. Fontana, and S. Greenstein (2024).
  Open Devices and Slices: Evidence from Wi-Fi Equipment.
  SSRN Electronic Journal.
* Kim and Valentine (2021)

  Kim, J. and K. Valentine (2021, April).
  The innovation consequences of mandatory patent disclosures.
  Journal of Accounting and Economics 71(2-3), 101381.
* Knapp and Wall (1997)

  Knapp, J. and A. Wall (1997).
  Considerations for streamlining the FCC equipment authorization program.
  In IEEE 1997, EMC, Austin Style. IEEE 1997 International Symposium on Electromagnetic Compatibility. Symposium Record (Cat. No.97CH36113), Austin, TX, USA, pp. 23–28. IEEE.
* Levin et al. (1987)

  Levin, R. C., A. K. Klevorick, R. R. Nelson, S. G. Winter, R. Gilbert, and Z. Griliches (1987).
  Appropriating the returns from industrial research and development.
  Brookings papers on economic activity 1987(3), 783–831.
* Moser (2005)

  Moser, P. (2005, August).
  How Do Patent Laws Influence Innovation? Evidence from Nineteenth-Century World’s Fairs.
  American Economic Review 95(4), 1214–1236.
* Murray et al. (2016)

  Murray, F., P. Aghion, M. Dewatripont, J. Kolev, and S. Stern (2016, February).
  Of Mice and Academics: Examining the Effect of Openness on Innovation.
  American Economic Journal: Economic Policy 8(1), 212–252.
* Nelson (1959)

  Nelson, R. R. (1959).
  The Simple Economics of Basic Scientific Research.
  Journal of Political Economy 67(3), 297–306.
* Noack and Rothe (2023)

  Noack, C. and C. Rothe (2023, August).
  Donut Regression Discontinuity Designs.
  arXiv:2308.14464 [econ].
* Porumbescu et al. (2022)

  Porumbescu, G., A. Meijer, and S. Grimmelikhuijsen (2022).
  Government transparency: State of the art and new perspectives.
  Cambridge University Press.
* Probst et al. (2023)

  Probst, B., P. M. Lohmann, A. Kontoleon, and L. D. Anadón (2023, October).
  The impact of open access mandates on scientific research and technological development in the U.S.
  iScience 26(10), 107740.
* Rassenfosse et al. (2024)

  Rassenfosse, G. d., G. Pellegrino, and E. Raiteri (2024).
  Do patents enable disclosure? Evidence from the invention secrecy act.
  International Journal of Industrial Organization 92, 103044.
* Rigby (2015)

  Rigby, D. L. (2015, November).
  Technological Relatedness and Knowledge Space: Entry and Exit of US Cities from Patent Classes.
  Regional Studies 49(11), 1922–1937.
* Sampat and Williams (2019)

  Sampat, B. and H. L. Williams (2019, January).
  How Do Patents Affect Follow-On Innovation? Evidence from the Human Genome.
  American Economic Review 109(1), 203–236.
* Sandrik (2021)

  Sandrik, K. (2021).
  An Empirical Study: Willful Infringement & Enhanced Damages in Patent Law After Halo.
  Michigan Technology Law Review (28.1), 61.
* Staudt (2020)

  Staudt, J. (2020, April).
  Mandating access: assessing the NIH’s public access policy.
  Economic policy 35(102), 269–304.
  Place: England.
* Stiglitz (1999)

  Stiglitz, J. E. (1999, July).
  Knowledge as a Global Public Good.
  In I. Kaul, I. Grunberg, and M. Stern (Eds.), Global Public Goods. Oxford University Press.
* U.S.C. (1996a)

  U.S.C. (1996a).
  Electronic Freedom of Information Act.
* U.S.C. (1996b)

  U.S.C. (1996b).
  The Telecommunications Act of 1996.
* Weatherbed and Lawler (2024)

  Weatherbed, J. and R. Lawler (2024).
  What’s this new mystery Nintendo device?
  The Verge.
* Williams (2017)

  Williams, H. L. (2017).
  How Do Patents Affect Research Investments?
  Annual Review of Economics 9(1), 441–469.
* Wing et al. (2018)

  Wing, C., K. Simon, and R. A. Bello-Gomez (2018).
  Designing Difference in Difference Studies: Best Practices for Public Health Policy Research.
  Annual Review of Public Health 39(Volume 39, 2018), 453–469.
  Publisher: Annual Reviews Type: Journal Article.