---
authors:
- Hamidah Oderinwale
- Anna Kazlauskas
doc_id: arxiv:2510.24990v1
family_id: arxiv:2510.24990
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Economics of AI Training Data: A Research Agenda'
url_abs: http://arxiv.org/abs/2510.24990v1
url_html: https://arxiv.org/html/2510.24990v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hamidah Oderinwale and Anna Kazlauskas
  
Open Data Labs
  
{hamidah, anna}@opendatalabs.xyz

(October 2025)

###### Abstract

Despite data’s central role in AI production, it remains the least understood input. As AI labs exhaust public data and turn to proprietary sources with deals reaching hundreds of millions of dollars, research across computer science, economics, law, and policy has fragmented. We establish data economics as a coherent field through three contributions. First, we characterize data’s distinctive properties (nonrivalry, context-dependence, and emergent rivalry through contamination) and trace historical precedents for market formation in commodities like oil and grain. Second, we present systematic documentation of AI training data deals from 2020 to 2025, revealing persistent market fragmentation, five distinct pricing mechanisms (from per-unit licensing to commissioning), and that most deals exclude original creators from compensation. Third, we propose a formal hierarchy of exchangeable data units (token, record, dataset, corpus, stream) and argue for data’s explicit representation in production functions. Building on these foundations, we outline four open research problems foundational to data economics: measuring context-dependent value, balancing governance with privacy, estimating data’s contribution to production, and designing mechanisms for heterogeneous, compositional goods.

## 1 Introduction

Data remains the least understood of the three inputs to the still vaguely defined AI production function, even as scaling laws [[1](https://arxiv.org/html/2510.24990v1#bib.bib1)] highlight its role in driving frontier capabilities alongside compute and algorithms. Most economic research on AI has emphasized macro outcomes such as labor and productivity effects, while neglecting the production side [[2](https://arxiv.org/html/2510.24990v1#bib.bib2)].111See also Reuel et al.’s *Open Problems in Technical AI Governance* [[3](https://arxiv.org/html/2510.24990v1#bib.bib3)] for related governance-level questions, though their focus is institutional rather than economic.

In every technological revolution, understanding production-side economics has been prerequisite for understanding economic impact. During industrialization, understanding labor organization and supply chains was essential. During electrification, understanding energy infrastructure mattered. For AI, the same principle applies: we cannot understand its economic impact without understanding how it is produced. Yet current AI economics research focuses primarily on downstream effects, while treating the production function as a black box.222See Anthropic’s Economic Index and Economic Futures Project [[4](https://arxiv.org/html/2510.24990v1#bib.bib4), [5](https://arxiv.org/html/2510.24990v1#bib.bib5)], Stripe’s Economics of AI Fellowship [[6](https://arxiv.org/html/2510.24990v1#bib.bib6)], and OpenAI’s GDPval benchmark [[7](https://arxiv.org/html/2510.24990v1#bib.bib7)] as representative examples.

This paper does not attempt to fully characterize AI’s production function or resolve how data should be valued and allocated. Instead, it lays the groundwork for a formal field of data economics by: (1) documenting how data is currently exchanged and priced, (2) developing preliminary frameworks for representing data as a distinct factor of production, and (3) identifying open problems whose resolution would advance data economics as a field.

While foundation models have ingested much of the public internet [[8](https://arxiv.org/html/2510.24990v1#bib.bib8)], they use less than 0.01% of the world’s available data [[9](https://arxiv.org/html/2510.24990v1#bib.bib9)]—roughly 99% remains as “dark data” [[10](https://arxiv.org/html/2510.24990v1#bib.bib10)] in proprietary databases, behind login walls, and in domain-specific corpora. As labs exhaust public data and turn toward proprietary sources—with deals reaching tens to hundreds of millions of dollars (see Table LABEL:tab:data-deals)—formal frameworks for understanding data’s economic role remain underdeveloped despite growing activity across AI research, economics, law, and policy. These efforts rarely speak to one another.

This paper consolidates disparate insights into a coherent research agenda. Section 2 establishes why data resists standard economic treatment. Section 3 proposes a hierarchy of exchangeable units. Section 4 documents current pricing mechanisms. Section 5 sketches how data enters production functions. Section 6 identifies foundational research problems for data economics as an emerging field.

## 2 Why data resists standardization: Properties, precedents, and the state of research

Before examining how data is currently exchanged or how it might be integrated into production models, we must understand why it resists the market mechanisms that work for traditional factors of production. This section establishes three foundations: data’s unique economic properties, historical precedents showing how heterogeneous assets became standardized, and the current state of research attempting to bridge these gaps.

### 2.1 Economic properties and barriers to standardization

Data is quite different from traditional commodities. It is nonrivalrous in principle: its reuse does not diminish its supply, and only partially excludable, since access can be restricted but copies are easily made. However, contamination effects (dataset aging, adversarial poisoning, benchmark leakage, preference leakage) and overuse create practical rivalry, reducing future utility [[11](https://arxiv.org/html/2510.24990v1#bib.bib11), [12](https://arxiv.org/html/2510.24990v1#bib.bib12), [13](https://arxiv.org/html/2510.24990v1#bib.bib13), [14](https://arxiv.org/html/2510.24990v1#bib.bib14)]. While nonrival in principle, data has become effectively excludable as consent protocols restrict crawling and AI use [[15](https://arxiv.org/html/2510.24990v1#bib.bib15)].

Two barriers prevent data from following the standardization path that other heterogeneous assets have taken. First, the verification paradox: quality and suitability cannot be assessed without examining data, yet examination enables copying, creating severe adverse selection where sellers cannot credibly signal quality and buyers cannot distinguish high-quality from low-quality data without access [[16](https://arxiv.org/html/2510.24990v1#bib.bib16)]. The problem is particularly acute for data because, unlike physical goods, inspection grants perfect replication rather than mere knowledge. Second, legal opacity: data’s legal status (licensing rights, copyright clearance, consent validity) cannot be verified through inspection alone and remains uncertain even after investigation, as evidenced by ongoing disputes over data use and the difficulty in scaling standardized licensing agreements [[17](https://arxiv.org/html/2510.24990v1#bib.bib17)]. Together, the verification paradox and legal opacity create substantial obstacles to standardization—intermediaries and brokers become essential gatekeepers, raising transaction costs and fragmenting markets.

Beyond these verification barriers, data’s value is highly context-dependent: it varies by buyer holdings, application, and combination with other datasets, and its highly differentiated nature prevents uniform pricing even when quality and legality are established [[18](https://arxiv.org/html/2510.24990v1#bib.bib18)].

### 2.2 Historical precedents: How heterogeneous assets became standardized

Data’s heterogeneity is often cited as a barrier to treating it as a tradable asset. Yet history shows that even highly heterogeneous resources can become measurable and tradable through the development of standards, exchanges, and verification mechanisms when economic pressure demands it.

Consider the corporate form itself. As railroads required unprecedented capital in the mid-19th century, the limited liability corporation emerged to make ownership divisible [[19](https://arxiv.org/html/2510.24990v1#bib.bib19), [20](https://arxiv.org/html/2510.24990v1#bib.bib20)]. Companies—with distinct management, assets, and competitive positions—were transformed into standardized shares through listing requirements, accounting standards, and metrics like P/E ratios.

This pattern repeats across commodities. Grain markets suffered chronic quality disputes until USDA grading and futures contracts imposed standardization [[21](https://arxiv.org/html/2510.24990v1#bib.bib21)]. Oil moved from chaotic local trade to global benchmarks through standards and reference prices [[22](https://arxiv.org/html/2510.24990v1#bib.bib22)]. Table 1 traces this pattern across asset classes.

Table 1: Historical asset market development: From heterogeneity to standardization

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Asset Class | Mechanism | Developer | Date(s) | Outcome |
| Corporate Equity | Limited liability corporations and standardized shares: divisible ownership with formalized listing requirements | Railroad companies; New York Stock Exchange | 1850s–1860s | Enabled capital mobilization and liquid markets for company ownership |
| Agriculture | Grain futures and warehouse receipts: standardized grading and storage contracts | Chicago Board of Trade (CBOT) | 1848 | Stabilized food supply chains and enabled hedging against harvest volatility |
| Oil | Futures contracts and spot benchmarks: standardized delivery and pricing | Joseph Leiter; Chicago Board of Trade (CBOT); later NYMEX, OPEC | 1870s–1900s | Shifted oil from local commodity to globally benchmarked and traded resource |
| Data | Emerging proposals for standardized data valuation, licensing, and registries | Being established | 2020s–Present | Transforming data from byproduct to recognized capital asset |

### 2.3 The state of research on data economics

Research on data’s economic role spans computer science, economics, law, and policy, with each discipline contributing distinct but largely non-overlapping insights. While each stream has advanced understanding within its domain, fragmentation creates challenges to answering to answering fundamental questions about measurement, valuation, and market design.

Technical foundations from AI research. Machine learning research has established empirical scaling laws demonstrating predictable relationships between training data volume, compute resources, and model performance [[23](https://arxiv.org/html/2510.24990v1#bib.bib23)]. Work on data quality and curation reveals that not all data contributes equally—heterogeneity creates variation in marginal value. However, this research measures contribution in technical metrics (perplexity, accuracy) rather than economic units (prices, marginal products), leaving a translation gap.

Economic theory on nonrivalry and market structure. Economics research has focused on data’s distinctive properties as a nonrival good. Jones and Tonetti [[24](https://arxiv.org/html/2510.24990v1#bib.bib24)] show that nonrivalry generates increasing returns to scale and creates tension between private incentives and social efficiency. Farboodi and Veldkamp [[25](https://arxiv.org/html/2510.24990v1#bib.bib25)] model data as endogenously valuable information. Analysis of market structure reveals how information asymmetries impede exchange: Bergemann and Bonatti [[26](https://arxiv.org/html/2510.24990v1#bib.bib26)] show that uncertainty about data value creates adverse selection; Santesteban and Longpre [[27](https://arxiv.org/html/2510.24990v1#bib.bib27)] document how heterogeneity creates barriers to entry that concentrate market power.

Legal and regulatory frameworks. Privacy regulations like GDPR establish individual rights over personal data but without mechanisms for collective action or market exchange [[28](https://arxiv.org/html/2510.24990v1#bib.bib28)]. Legal scholarship has proposed alternatives: Delacroix and Lawrence [[29](https://arxiv.org/html/2510.24990v1#bib.bib29)] advocate bottom-up data trusts for collective governance; Pentland [[30](https://arxiv.org/html/2510.24990v1#bib.bib30)] proposes treating data as tradable capital. While some implementations are emerging, scalable governance structures with robust enforcement mechanisms and standardized metrics remain underdeveloped.

Persistent gaps. Three challenges emerge: (1) no consensus on appropriate units for measuring and pricing data—AI research measures tokens and parameters; economics discusses datasets and streams; regulation addresses individual records; (2) incomplete understanding of how data quality, quantity, and combination affect value, particularly how datasets combine to create value; (3) production function frameworks do not adequately represent data as a distinct input or capture its complementarities with compute and labor. Addressing these gaps requires synthesis across disciplines and innovation in measurement standards and exchange mechanisms.

## 3 Data as a composable unit of production

No consensus exists on the appropriate units for measuring, pricing, or exchanging data. AI research measures tokens; economics discusses datasets; regulation addresses individual records. Table [2](https://arxiv.org/html/2510.24990v1#S3.T2 "Table 2 ‣ 3 Data as a composable unit of production ‣ The Economics of AI Training Data: A Research Agenda") proposes a unified hierarchy of exchangeable units and maps how different pricing mechanisms emerge at each level. While not yet standardized in practice, this provides a conceptual foundation for understanding different pricing mechanisms and exchange arrangements.

Table 2: Atomic hierarchy of data as exchangeable units.33footnotetext: These units can also be aggregated collectively, introducing another dimension of exchange where data from different sources is pooled and transacted as a shared asset [[30](https://arxiv.org/html/2510.24990v1#bib.bib30)].

| Level | Unit of Exchange | Description | Typical Market Form |
| --- | --- | --- | --- |
| Token | Smallest processable data fragment (e.g., tokenized text or scalar input) | Divisible and composable333Token-level pricing is now being operationalized through infrastructure such as Stripe’s usage-based billing API, which meters and charges per-token consumption via LLM proxies including OpenRouter, Cloudflare, Vercel, and Helicone. See also Coyle (2024) for broader economic-measurement framing.; traded implicitly (e.g., through inference pricing); value tied to marginal compute cost. | API pricing. |
| Record | Single observation or labeled example | Atomic contribution to learning; verification costly, so exchanged in bulk or via labor markets. | Labeling platforms. |
| Dataset | Curated collection of records | Main tradable unit; value depends on quality, format, and domain specificity. | Licensing, benchmarks. |
| Corpus | Aggregate of datasets | Compositional scale good; returns to diversity and coverage. | Pretraining corpora. |
| Stream | Continuous, time-ordered feed | Dynamic input monetized by flow or access rather than ownership. | Telemetry, feeds. |

## 4 Data in exchange: Transacting and pricing mechanisms

Despite data’s growing economic importance, the heterogeneity established in Section [2](https://arxiv.org/html/2510.24990v1#S2 "2 Why data resists standardization: Properties, precedents, and the state of research ‣ The Economics of AI Training Data: A Research Agenda") fundamentally obstructs standardized pricing. Transactions remain predominantly bilateral and bespoke, negotiated case by case based on data type, buyer context, and evolving legal boundaries. Most data transactions remain private; the examples documented here come from public announcements, company filings, and media reports, providing an incomplete but representative picture of market activity. Table LABEL:tab:data-pricing-alignment maps principal pricing mechanisms to the data units established in Table [2](https://arxiv.org/html/2510.24990v1#S3.T2 "Table 2 ‣ 3 Data as a composable unit of production ‣ The Economics of AI Training Data: A Research Agenda"). Table LABEL:tab:data-deals in the Appendix provides systematic documentation of AI training data deals from 2020-2025, including deal structure, compensation terms, and exclusivity provisions across modalities.

Table 3: Alignment between data units and pricing mechanisms

|  |  |  |  |
| --- | --- | --- | --- |
| Pricing Mechanism | Applicable Unit(s) | Economic Logic | Examples |
| Per-unit pricing | Token, Record | Price proportional to usage volume or access frequency; reflects marginal processing or annotation cost. | HarperCollins books ($5k/title), indie music tracks (€0.30–€2/track), video footage ($1–4/min) |
| Aggregate licensing | Dataset, Corpus, Stream | Payment for time-limited access rights to curated or proprietary data; includes both one-time and recurring subscriptions. Ownership remains with licensor. | News Corp–OpenAI ($250M+ over 5 years), Reddit–Google ($60M/year), Dotdash Meredith–OpenAI ($16M/year) |
| Service-based pricing | Record, Dataset | Payment for data transformation processes such as annotation, cleaning, or validation applied to existing data. | Scale AI annotation platforms, data aggregation services |
| Commissioning | Dataset, Corpus | Upfront funding for new data collection or creation tailored to buyer specifications; pays for production process rather than existing assets. | Mercor expert-generated domain data ($450M ARR), custom video collection for vision models |
| Open commons | All units | Public datasets funded through government, research mandates, or voluntary contribution; provide competitive baseline for commercial markets. | LAION/Common Crawl, Protein Data Bank |

Per-unit pricing charges per discrete unit: licensing books at US$5,000 each with 50/50 author splits, music at €0.30–€2.00 per track, and videos at US$1–4 per minute. This mechanism prevails when units are clearly delineated, value per unit is consistent, and intermediaries (publishers, platforms) can aggregate creator content and negotiate on their behalf.

Aggregate licensing dominates large-scale enterprise deals: buyers pay fixed fees for time-limited access to curated corpora or feeds. Most licenses are non-exclusive—providers retain ownership and monetize simultaneous access to multiple buyers, but exclusivity like the News Corp deal commands price premiums. Deals frequently include hybrid components: News Corp receives both cash and substantial OpenAI API credits. These hybrid payments create lock-in: as providers integrate APIs into production systems, switching costs rise and relationships entrench.

Service-based pricing bundles data with transformation labor: platforms like Scale AI compensate crowd workers for annotation and curation, transforming raw data into labeled training sets. Buyers pay platforms for curated, quality-verified datasets. Platforms take a fee for coordination, quality assurance, and liability, then pay individual annotators.

Commissioning pays for *new* data creation when required corpora don’t exist. Mercor (US$450 million ARR) connects AI labs with domain experts to generate specialized training data [[31](https://arxiv.org/html/2510.24990v1#bib.bib31)]; independent video creators supply custom footage to AI video labs. Pricing typically follows a consulting model: hourly rate for expert labor plus upcharge for the platform providing coordination, curation and quality assurance.

Open commons as competitive baseline. Public datasets—LAION/Common Crawl for text and images, ESA’s Copernicus satellite data, the Protein Data Bank for structural biology, and publicly funded research data from institutions like Germany’s DLR—provide a competitive floor for commercial data markets. These commons exist due to public funding, regulatory mandates, or voluntary contribution, and serve as substitutes that discipline pricing in private markets. Recognition of data as a national strategic asset has accelerated investment in high-quality scientific datasets [[32](https://arxiv.org/html/2510.24990v1#bib.bib32)], further expanding the commons baseline.

Implicit data exchanges constitute a fifth, often-overlooked category. Here, platforms provide free or subsidized services—language models trained on conversations, recommendation systems trained on user behavior—in exchange for data rights outlined in the terms of service. Critically, this differs from advertising: users are not the product sold to advertisers; rather, their data inputs are harvested to train AI models sold to third parties. Reddit’s retrospective licensing of user-generated content to Google (US$60 million annually) exemplifies the pattern: platforms accumulate vast corpora through terms-of-service data grants, then monetize that corpus.

Data deals generally exclude most data creators: of 24 major deals in Table LABEL:tab:data-deals, only 7 compensate the original creator of the data, while the remaining 17 (News Corp’s journalists, Reddit’s users, Wiley’s researchers) reward only intermediaries. This stems from scale barriers—individual creators lack negotiating power, falling below labs’ minimum thresholds. Platforms aggregate user content and capture revenues. Le Monde’s 25% journalist revenue share, achieved through union leverage, remains a notable exception. Emerging data unions are experimenting with collective bargaining to address this, though implementation remains nascent. Per-unit pricing and commissioning do allow direct creator payments—HarperCollins’ 50/50 author splits, indie music at €0.30–€2 per track, Mercor’s expert hourly rates.

## 5 Representing data in the production function

Having established data’s properties, its role in exchange, and the pricing mechanisms that govern transactions, we now address how data should be represented in economic production functions. Current growth and production models do not explicitly include data as a distinct factor, yet AI production depends heavily on it. This section outlines why explicit representation matters and what fundamental unknowns remain unresolved.

### 5.1 The framework

Current production function formulations do not explicitly model data as a distinct input. Rather than proposing a specific functional form, we argue that data should be treated as a distinct input. We represent this conceptually as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y=f​(K,L,D,A)Y=f(K,L,D,A) |  | (1) |

where YY represents output, KK is capital (including compute infrastructure), LL is labor, DD is data, and AA captures technology and algorithmic efficiency. This notation indicates that data should be treated as a distinct factor of production rather than subsumed under capital, labor, or technology—but does not commit to a specific functional form, parametrization, or substitution elasticities.

Data could theoretically be incorporated into existing terms: as capital KK (an acquired asset), labor LL (effort in collection and processing), or technology AA (information improving productivity). However, doing so obscures data’s distinctive properties: nonrivalry, context-dependence, and emergent rivalry through contamination and staleness. Data behaves fundamentally differently from traditional inputs.

Unlike capital, it does not depreciate through use but may lose value through replication or obsolescence. Unlike labor, it can be used simultaneously by multiple producers without depletion. Unlike pure technology, data must be acquired—often at significant cost—and exhibits heterogeneity such that composition and complementarities affect its marginal contribution. Explicit representation enables analysis of data markets, optimal investment, and measurement of data’s contribution to productivity growth. We remain agnostic about whether data follows Cobb-Douglas, CES, or other functional forms—that is an empirical question subsequent research should address. Our contribution here is establishing that data should appear explicitly in production function representations rather than being absorbed into other terms.

Making data explicit in the production function reveals several key dimensions worth understanding as the field develops.

Data’s contribution depends on how it combines with other factors. We observe both complementarity and substitutability. Frontiers in AI demonstrate strong complementarity: training state-of-the-art models requires both massive amounts of data and unprecedented compute. To some extent, firms can substitute compute for data through synthetic data generation, although it cannot fully replace diverse, real-world data for capturing edge cases and novel domains. The elasticities of these relationships, and how they vary by domain and task, remain empirically undetermined, but trade offs exist in practice in industry.

Returns to scale on data represent another critical dimension. Empirical computer science research on language model training demonstrates that performance improves as a power law in dataset size, with exponents typically between 0.3 and 0.5 [[23](https://arxiv.org/html/2510.24990v1#bib.bib23), [1](https://arxiv.org/html/2510.24990v1#bib.bib1)], suggesting diminishing marginal returns from a model performance perspective. However, these estimates rest on limited data regimes, as researchers face a “data wall” around 15 trillion tokens of public internet text [[8](https://arxiv.org/html/2510.24990v1#bib.bib8)], beyond which empirical evidence becomes sparse. We do not know whether diminishing returns hold beyond this boundary, whether specialized or high-quality data exhibits different characteristics, or whether technical scaling laws map to economic returns once quality effects, network dynamics, and contamination risks are factored in.

![Refer to caption](media/image3.png)


Figure 1: Three stylized models for data’s contribution to AI production: diminishing returns (capital-like), sustained or increasing returns with quality, and inverted-U under contamination or overuse.

Data’s role differs across the machine learning pipeline. Pre-training predominantly uses large-scale publicly available datasets, where volume drives value. Post-training prioritizes high-quality curated datasets commanding premium prices. Inference generates continuous user feedback. This creates segmented markets with distinct pricing dynamics, but whether these reflect fundamental features of AI production or contingencies of current technology remains unclear.

![Refer to caption](media/image2.png)


Figure 2: Machine learning pipeline showing data’s distinct roles across pre-training, fine-tuning, and inference stages.

## 6 Open Problems in Data Economics

This paper establishes a framework for understanding data as a distinct factor of production with unique economic properties: nonrivalry, context-dependence, composability, and emergent rivalry through contamination. We have shown how data can be decomposed into exchangeable units, documented the pricing mechanisms that govern current transactions, and argued for explicit representation in production functions. However, building a complete theory of data economics requires sustained empirical and theoretical work across multiple disciplines.

We conclude by posing foundational questions that emerge from this framework. These questions are interdisciplinary by nature—addressing them requires collaboration among economists, computer scientists, legal scholars, and policymakers. Progress on these questions will determine whether data markets can function efficiently and whether we can properly account for data’s contribution to economic growth.

1. How do we measure and value data when its worth depends on context, composition, and who has access?

Data’s value is not intrinsic but depends on what other data exists, how it will be used, and who can access it. The same dataset has different value for different buyers with different existing corpora and different applications, and depends on which other buyers have already accessed the dataset. Exclusive access commands premium pricing; value degrades as access spreads. Technical metrics (tokens, records) do not map to economic value; quality is task-specific and compositional. Addressing this requires developing measurement frameworks that capture context-dependence, valuation models under interdependent preferences, and mechanisms for price discovery when inspection enables copying.

2. What property rights and governance mechanisms support efficient data allocation while preserving privacy and preventing monopolization?

Individual ownership (GDPR-style) protects privacy but makes efficient pooling challenging; platform ownership enables scale but concentrates control; open commons maximize access but reduce incentives for data creators to contribute and may limit sustainability. Data’s nonrivalry means multiple parties can use the same data simultaneously, but excludability is essential for market formation. Addressing this requires legal frameworks for data rights (law), institutional designs for data trusts and cooperatives (mechanism design), technical infrastructure for privacy-preserving computation and provenance tracking (computer science), and welfare analysis of alternative governance regimes (policy/economics). Historical precedents show that property rights choices had lasting effects on market structure for oil, spectrum, and other assets; the choices we make for data will similarly shape long-run outcomes.

3. How do we empirically estimate data’s contribution to production and productivity?

We have argued that data should appear explicitly in production functions rather than being absorbed into capital, labor, or technology. But we have not specified what functional form data takes, how it enters production, or what its mathematical properties are. Building this theory requires specifying whether data follows Cobb-Douglas, CES, or other functional forms; deriving the marginal product of data and its elasticities with other inputs; and working through the implications for substitution, complementarity, and returns to scale. An ideal starting point would be empirical data on what training datasets each AI firm uses, their model performance, and revenue outcomes—this would enable both theory development and direct estimation.

Such firm-level data does not exist publicly. Progress instead requires combining controlled experiments isolating data’s causal effects on model performance, natural experiments where data access varies, and evidence on firms’ data investment decisions. These can answer concrete questions: How does model performance scale with dataset size and composition? Where do diminishing returns emerge? Can compute and labor substitute for data, or is data complementary and constraining? Do relationships differ across pre-training versus fine-tuning? Once empirical patterns emerge, they can guide theoretical specification and lead toward a functioning theory of data as a production input.

4. Can we design markets and mechanisms for heterogeneous, compositional goods?

Data’s value depends on buyers’ existing holdings and how datasets combine in training—not on the dataset in isolation. Buyers cannot assess value without examining data, but examination makes copying possible. Attribution is computationally intractable when models train on millions of sources. These challenges require developing new market mechanisms that handle interdependent valuations and compositional effects (mechanism design), standards for provenance and quality certification that enable price discovery without full inspection (institutional design), attribution methods that are theoretically sound and computationally feasible (computer science and economics), and minimal infrastructure for market formation without centralizing control (policy and industry coordination). Historical precedents show that market formation for grain, oil, and equities required developing measurement standards and exchange institutions; data markets need analogous infrastructure.

## 7 Conclusion

Data has become the decisive input shaping AI production, competition, and growth, yet it remains the least formalized in economic analysis. This paper outlines the foundations for a field of data economics: representing data as a distinct factor of production, documenting how it is priced and exchanged, and defining the open problems that must be solved for efficient markets to emerge.

Progress now depends on bridging theory, empirical economics, computer science, and institutional design. Economists must formalize production functions that capture data’s nonrival and compositional nature; computer scientists must quantify its contribution to performance and develop verifiable provenance systems; legal and policy scholars must construct governance frameworks that balance privacy, efficiency, and competition. None of these tasks can succeed in isolation.

The formation of data economics will determine how value in the AI economy is measured, traded, and distributed. As data takes its place alongside labor and capital as a primary scarce input, the stakes are not just about optimizing AI production but about deciding who owns the means of intelligence itself.

## References

* Hoffmann et al. [2022]

  Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al.
  Training compute-optimal large language models.
  *arXiv preprint arXiv:2203.15556*, 2022.
* Huang et al. [2021]

  Lihua Huang, Yifan Dou, Yezheng Liu, Jinzhao Wang, Gang Chen, Xiaoyang Zhang, and Runyin Wang.
  Toward a research framework to conceptualize data as a factor of production: The data marketplace perspective.
  *Fundam. Res.*, 1(5):586–594, 2021.
* Reuel et al. [2025]

  Anka Reuel, Ben Bucknall, Stephen Casper, Tim Fist, Lisa Soder, Onni Aarne, Lewis Hammond, Lujain Ibrahim, Alan Chan, Peter Wills, Markus Anderljung, Ben Garfinkel, Lennart Heim, Andrew Trask, Gabriel Mukobi, Rylan Schaeffer, Mauricio Baker, Sara Hooker, Irene Solaiman, Alexandra Sasha Luccioni, Nitarshan Rajkumar, Nicolas Moës, Jeffrey Ladish, David Bau, Paul Bricman, Neel Guha, Jessica Newman, Yoshua Bengio, Tobin South, Alex Pentland, Sanmi Koyejo, Mykel J. Kochenderfer, and Robert Trager.
  Open problems in technical ai governance, 2025.
  URL <https://arxiv.org/abs/2407.14981>.
* Anthropic [2024a]

  Anthropic.
  Economic index geography.
  <https://www.anthropic.com/research/economic-index-geography>, 2024a.
  Accessed: 2025-10-07.
* Anthropic [2024b]

  Anthropic.
  Economic futures project.
  <https://www.anthropic.com/economic-futures>, 2024b.
  Accessed: 2025-10-07.
* Stripe [2024]

  Stripe.
  Economics of ai fellowship.
  <https://stripe.events/fellowship>, 2024.
  Accessed: 2025-10-07.
* OpenAI [2024]

  OpenAI.
  Gdpval: Evaluating model capabilities on economically valuable tasks.
  <https://openai.com/index/gdpval/>, 2024.
  Accessed: 2025-10-07.
* Villalobos et al. [2024]

  Pablo Villalobos, Anson Ho, Jaime Sevilla, Tamay Besiroglu, Lennart Heim, and Marius Hobbhahn.
  Will we run out of data? limits of llm scaling based on human-generated data.
  <https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data>, 2024.
  Accessed: 2025-10-07.
* OpenMined [2025]

  OpenMined.
  Ai is trained and evaluated on less than 0.01% of the world’s data.
  <https://openmined.org/>, 2025.
  Accessed: 2025-10-07.
* Wikipedia contributors [2025]

  Wikipedia contributors.
  Dark data.
  <https://en.wikipedia.org/wiki/Dark_data>, 2025.
  Accessed: 2025-10-07.
* Zhang et al. [2024]

  Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Charlotte Zhuang, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, and Summer Yue.
  A careful examination of large language model performance on grade school arithmetic, 2024.
  URL <https://arxiv.org/abs/2405.00332>.
  Examines benchmark contamination and memorization in arithmetic reasoning tasks.
* Choi et al. [2025]

  Minseok Choi, Sangwoo Lee, Taewook Kim, Joonseok Park, Minjoon Kim, Heewon Kim, Kyungjae Lee, and Dongha Kim.
  How contaminated is your benchmark? quantifying and mitigating data leakage in llm evaluation, 2025.
  URL <https://arxiv.org/abs/2502.00678>.
  Proposes systematic methods to detect benchmark leakage and quantify contamination in evaluation datasets.
* Li et al. [2025]

  Xiang Li, Tianhao Wang, Kai Chen, Yikai Wu, Jiaming Zhao, and Yuchen Zhu.
  Preference leakage: A contamination problem in llm-as-a-judge, 2025.
  URL <https://arxiv.org/abs/2502.01534>.
  Identifies feedback loop contamination in human preference data for LLM-as-a-judge pipelines.
* Huang et al. [2023]

  Siyuan Huang, Yihan Zhu, Zekun Wang, Ming Xue, and Zhenhua He.
  Data poisoning in deep learning: A survey, 2023.
  URL <https://arxiv.org/abs/2302.10149>.
  Comprehensive survey of adversarial data poisoning attacks and defenses in deep learning.
* Longpre et al. [2024]

  Shayne Longpre, Nisan Stiennon, Colin Raffel, Sara Hooker, and Yacine Jernite.
  Consent in the age of large language models: The case for data dignity, 2024.
  URL <https://arxiv.org/abs/2410.11294>.
  Analyzes consent-based data access protocols and their implications for AI training data supply.
* Akerlof [1970]

  George A. Akerlof.
  The market for "lemons": Quality uncertainty and the market mechanism.
  *The Quarterly Journal of Economics*, 84(3):488–500, 1970.
  doi: 10.2307/1879431.
* Mathews and Ropes & Gray LLP [2025]

  Manav Mathews and Ropes & Gray LLP.
  A tale of three cases: How fair use is playing out in ai copyright lawsuits.
  <https://www.ropesgray.com/en/insights/alerts/2025/07/a-tale-of-three-cases-how-fair-use-is-playing-out-in-ai-copyright-lawsuits>, 2025.
  Published July 6, 2025.
* Cohen et al. [2016]

  Maxime Cohen, Ilan Lobel, and Renato Paes Leme.
  Feature-based dynamic pricing.
  In *Proceedings of the 2016 ACM Conference on Economics and Computation (EC ’16)*, pages 647–664. ACM, 2016.
  URL <https://research.google/pubs/feature-based-dynamic-pricing/>.
* not specified in snippet [2018]

  Author not specified in snippet.
  A brief history of the corporate form and why it matters.
  *Fordham Journal of Corporate & Financial Law*, 2018.
  URL <https://news.law.fordham.edu/jcfl/2018/11/18/a-brief-history-of-the-corporate-form-and-why-it-matters/#_ednref25>.
  Accessed October 27.
* Harvard Business School [2010]

  Baker Library Historical Collections Harvard Business School.
  New levels of capitalism: Finance - railroads and the transformation of capitalism, 2010.
  URL <https://www.library.hbs.edu/hc/railroads/finance.html>.
  Accessed October 27, 2025.
* United States Department of Agriculture [2025]

  Economic Research Service United States Department of Agriculture.
  State agricultural trade by country of origin and destination, 2025.
  URL <https://ers.usda.gov/publications/pub-details?pubid=45732>.
  Accessed October 27, 2025.
* Stern and Imsirovic [2020]

  Jonathan Stern and Adi Imsirovic.
  A comparative history of oil and gas markets and prices: Is 2020 just an extreme cyclical event or an acceleration of the energy transition?
  Energy insight 68, Oxford Institute for Energy Studies, April 2020.
  URL <https://www.oxfordenergy.org/wpcms/wp-content/uploads/2020/04/Insight-68-A-Comparative-History-of-Oil-and-Gas-Markets-and-Prices.pdf>.
* Kaplan et al. [2020]

  Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei.
  Scaling laws for neural language models.
  *arXiv preprint arXiv:2001.08361*, 2020.
  URL <https://arxiv.org/abs/2001.08361>.
* Jones and Tonetti [2020]

  Charles I. Jones and Christopher Tonetti.
  Nonrivalry and the economics of data.
  *American Economic Review*, 110(9):2819–2858, 2020.
  doi: 10.1257/aer.20191330.
* Farboodi and Veldkamp [2021]

  Maryam Farboodi and Laura Veldkamp.
  Long-run growth of financial data technology.
  *American Economic Review*, 111(8):2485–2523, 2021.
* Bergemann and Bonatti [2024]

  Dirk Bergemann and Alessandro Bonatti.
  Data markets and the economics of information flow.
  *Annual Review of Economics*, 16:129–155, 2024.
* Santesteban and Longpre [2020]

  Cristian Santesteban and Shayne Longpre.
  How big data confers market power to big tech: Leveraging the perspective of data science.
  *Antitrust Bull.*, 65(3):459–485, September 2020.
* Acquisti et al. [2016]

  Alessandro Acquisti, Curtis Taylor, and Liad Wagman.
  The economics of privacy.
  *Journal of Economic Literature*, 54(2):442–492, 2016.
* Delacroix and Lawrence [2019]

  Sylvie Delacroix and Neil D. Lawrence.
  Bottom-up data trusts: disturbing the ’one size fits all’ approach to data governance.
  *International Data Privacy Law*, 9(4):236–252, 2019.
  doi: 10.1093/idpl/ipz014.
* Pentland [2020]

  Alex Pentland.
  *Building the New Economy: Data as Capital*.
  MIT Press, Cambridge, MA, 2020.
  URL <https://mitpress.mit.edu/9780262539736/building-the-new-economy/>.
* Zeff and Team [2025]

  Maxwell Zeff and TechCrunch Editorial Team.
  Sources: Ai training startup mercor eyes $10b+ valuation on $450m run rate.
  *TechCrunch*, September 2025.
  URL <https://techcrunch.com/2025/09/09/sources-ai-training-startup-mercor-eyes-10b-valuation-on-450m-run-rate/>.
  Mercor, a startup connecting AI labs with domain experts for model training, was reportedly in talks to raise Series C funding at a $10B valuation.
* Office of Science and Technology Policy [2025]

  Office of Science and Technology Policy.
  America’s ai action plan.
  Technical report, The White House, Executive Office of the President, July 2025.
  URL <https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf>.
  Released under the directive "Winning the AI Race".
* CB Insights [2024]

  CB Insights.
  Ai content licensing deals.
  <https://www.cbinsights.com/research/ai-content-licensing-deals/>, 2024.
  Accessed: 2025-10-27.

## 8 Appendix

Table 4: AI Content Licensing and Data Deals (2020–2025)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # | Modality | Date | Provider | Buyer | Data Type | Reported Terms | Compensated? | Exclusive? | Pricing Mech. | Notable Details | Source(s) |
| 1 | Text | 2 024-05-22 | News Corp | OpenAI | News archive & publisher content (WSJ, The Times, NY Post) | >>US$250M / 5 yrs | No | Yes | Access licensing | Largest journalism-AI deal; cash + credits [[33](https://arxiv.org/html/2510.24990v1#bib.bib33)] | [NewsCorp, WSJ](https://investors.newscorp.com/news-releases/news-release-details/news-corp-and-openai-sign-landmark-multi-year-global-partnership) |
| 2 | Text | 2 024-02-22 | Reddit | Google | Social-media UGC feed | ≈\approxUS$60M / yr | No | No | Volume-based access | Recurring API access for search & training [[33](https://arxiv.org/html/2510.24990v1#bib.bib33)] | [Reuters, The Verge](https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/) |
| 3 | Text | 2024-05 | Dotdash Meredith | OpenAI | Magazine & digital-media archives | ≥\geqUS$16M / yr (fixed) | No | No | Access licensing (base + variable) | Includes legacy magazine brands [[33](https://arxiv.org/html/2510.24990v1#bib.bib33)] | [Axios](https://www.axios.com/2024/05/22/openai-news-corp-content-licensing-deal) |
| 4 | Text | 2024-11 | HarperCollins | Microsoft | Non-fiction book titles (AI training rights) | US$5K / title; 50/50 split | Yes | No | Per-unit licensing | Early per-book pricing benchmark; limits verbatim output | [Authors Guild](https://authorsguild.org/news/harpercollins-ai-licensing-deal/) |
| 5 | Text | 2023 | Taylor & Francis | Microsoft | Academic journals / textbooks | ≈\approxUS$10M | Unclear | No | Access licensing (restricted) | License for academic content [[33](https://arxiv.org/html/2510.24990v1#bib.bib33)] | [The Bookseller](https://www.thebookseller.com/news/wiley-set-to-earn-44m-from-ai-rights-deals-confirms-no-opt-out-for-authors) |
| 6 | Text (Scientific) | 2024 | Wiley | Anthropic, AWS, Perplexity | Scientific content + metadata | US$23M (2025 Proxy filing) | No | No | Limited-term structured license | Controlled-environment use [[33](https://arxiv.org/html/2510.24990v1#bib.bib33)] | [Wiley Proxy](https://s27.q4cdn.com/812717746/files/doc_downloads/2025/2025-Proxy-Statement.pdf) |
| 7 | Image/Video | 2021–2024 | Shutterstock | Meta, OpenAI, Google, Apple | Stock images + video + metadata | US$25–30M per deal (multi-yr) | Partial | No | Hybrid per-unit + access | Used for multimodal training; includes royalty fund | [VentureBeat](https://venturebeat.com/ai/apples-25-50-million-shutterstock-deal-highlights-fierce-competition-for-ai-training-data/) |
| 8 | Image | 2024 | Freepik | Unnamed AI firms | ≈\approx200M stock images | ≈\approxUS$6M (2–4¢/image) | No | No | Per-unit micro-licensing | Large-scale low-cost imagery for pre-training | [Reuters](https://www.reuters.com/technology/inside-big-techs-underground-race-buy-ai-training-data-2024-04-05/) |
| 9 | Image/Text | 2020–2023 | LAION / Common Crawl | Open model builders | Image-caption datasets + web crawls | No cash value | N/A | No | Commons / open-source | Foundational datasets (LAION-5B, Falcon, etc.) | [LAION](https://laion.ai/blog/laion-5b/) |
| 10 | Text (Media) | 2025-05 | Le Monde | OpenAI, Perplexity | News content licensing deal | Undisclosed (25% rev share to journalists) | Yes | No | Access licensing | First to share AI revenue directly with journalists | [Le Monde](https://www.lemonde.fr/en/media/article/2025/06/09/le-monde-group-s-2024-accounts-mark-a-landmark-year_6742164_22.html) |
| 11 | Audio | 2025-07 | SourceAudio | ElevenLabs, Music.AI | Pre-cleared songs for AI training | US$10M (multi-year deal) | Yes | No | Access licensing | Access to millions of licensed tracks | [Record of the Day](https://www.recordoftheday.com/news-and-press/sourceaudio-teams-up-with-elevenlabs-as-preferred-partner-for-ai-music-licensing) |
| 12 | Audio | 2024 | UMG, Warner | AI music startups (Suno, Mubert) | Music catalog rights (audio + lyrics) | Undisclosed | Unclear | No | Access licensing (music/audio) | Pilot licensing framework for generative music | [MBW](https://www.musicbusinessworldwide.com/universal-warner-explore-ai-licensing-pacts-2024/) |
| 13 | Audio | 2024 | Audius + indie labels | EU generative-music firms | Independent tracks & stems | €0.30−€2.00\text{\texteuro 0.30}-\text{\texteuro 2.00} / track | Yes | No | Per-unit micro-licensing | Emerging artist-level licensing model | [Billboard](https://www.billboard.com/pro/audius-eu-ai-music-licensing-deals-2024/) |
| 14 | Video | 2025-01 | YouTube creators | OpenAI, Meta | Unpublished creator videos | ≈\approxUS$5M total (US$1–4 / min) | Yes | No | Per-unit licensing (video minutes) | AI labs buying unpublished creator content | [PetaPixel](https://petapixel.com/2025/01/13/ai-companies-are-paying-content-creators-for-their-unpublished-videos/) |
| 15 | Video | 2023–24 | Independent creators | Runway, Pika Labs | Professional/unpublished video footage | ≈\approxUS$1–4 / min (est.) | Yes | No | Per-unit licensing | Used for vision-language model training | [The Decoder](https://the-decoder.com/openai-and-google-are-buying-youtubers-unpublished-videos-for-up-to-4-per-minute/) |
| 16 | Satellite | 2020–24 | Planet Labs | Agriculture / gov AI firms | Daily Earth observation imagery | ≈\approxUS$180M annual rev | No | No | Subscription access licensing | Used for climate, agriculture & defense models | [Planet Labs](https://investors.planet.com/financials/annual-reports/) |
| 17 | Health/Biotech | 2024 | Tempus | Pharma & AI firms | Anonymized patient/genomic data | US$200M / 3 yrs | No | No | Access licensing | Training medical LLMs; 40% YoY growth [[33](https://arxiv.org/html/2510.24990v1#bib.bib33)] | [CB Insights](https://www.cbinsights.com/company/tempus-labs) |
| 18 | Corporate | 2025-06 | Scale AI | Meta | Equity stake for data services | US$14.3B for 49% stake | Variable | Yes | Strategic acquisition | Largest single data-related AI deal; Scale valued $29B | [CNBC, FT](https://www.cnbc.com/2025/06/14/meta-invests-14b-scale-ai.html) |
| 19 | Corporate | 2025-04 | Informatica | Salesforce | Cloud data integration platform | ≈\approxUS$8B | N/A | Yes | Full acquisition | Boosts enterprise AI data pipeline capabilities | [TechCrunch](https://techcrunch.com/2025/04/12/salesforce-to-acquire-informatica-for-8b/) |
| 20 | Legal/Books | 2025-09-05 | Authors & Publishers (class) | Anthropic | Books (unauthorized) | US$1.5B settlement (≈\approxUS$3K/book) | Yes | N/A | Legal settlement | Class action requiring data deletion & future limits | [Reuters, WIRED](https://www.reuters.com/technology/anthropic-settlement-authors-2025-09-06/) |
| 21 | Text | 2025-08 | CuriosityStream | AI partners | Factual/documentary video library | US$20–30M / yr | No | No | Access licensing (subscription/API feed) | ≈\approx25% of 2025 revenue | [SEC Filing](https://app.quotemedia.com/data/downloadFiling?webmasterId=131387&ref=319353889&type=PDF&symbol=CURI&companyName=CuriosityStream+Inc.&formType=10-Q&dateFiled=2025-08-06) |
| 22 | Text | 2025 | New York Times | Amazon | Editorial news (NYT Cooking, The Athletic) | US$20–25M / yr | No | No | Access licensing | Enables Alexa to use Times content for summaries & training | [GeekWire](https://www.geekwire.com/2025/report-amazon-to-pay-at-least-20m-a-year-in-ai-content-deal-with-new-york-times/) |
| 23 | Text | 2025 H1 | Chegg | AI partners | Expert-written Q&A pairs (homework help database) | US$11M (H1 2025) | Unclear | No | Access licensing | New revenue stream; <<5% of library | [SEC Filing](https://www.sec.gov/Archives/edgar/data/1364954/000136495425000049/a9901-financialresultsq120.htm) |
| 24 | Commissioning | 2022–2025 | Mercor | Mult. AI Labs | Domain expert talent for AI model training (RLHF, fine-tuning) | ≈\approxUS$450M ARR | Yes | No | Commissioning / Service-based | Rapid growth; "Switzerland" provider | [TechCrunch](https://techcrunch.com/2025/09/09/sources-ai-training-startup-mercor-eyes-10b-valuation-on-450m-run-rate/) |