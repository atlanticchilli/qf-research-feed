---
authors:
- Haoyi Zhang
- Tianyi Zhu
doc_id: arxiv:2510.26727v1
family_id: arxiv:2510.26727
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Neither Consent nor Property: A Policy Lab for Data Law'
url_abs: http://arxiv.org/abs/2510.26727v1
url_html: https://arxiv.org/html/2510.26727v1
venue: arXiv q-fin
version: 1
year: 2025
---


Haoyi Zhang1, 
  
Tianyi Zhu1,

(1Law School, Peking University
  
The authors have contributed equally.
  
<<zhanghaoyi,tianyizhu>@law.pku.edu.cn>
  
)

###### Abstract

This paper makes the opaque data market in the AI economy empirically legible for the first time, constructing a computational testbed to address a core epistemic failure: regulators governing a market defined by structural opacity, fragile price discovery, and brittle technical safeguards that have paralyzed traditional empirics and fragmented policy. The pipeline begins with multi-year fieldwork to extract the market’s hidden logic, and then embeds these grounded behaviors into a high-fidelity ABM, parameterized via a novel LLM-based discrete-choice experiment that captures the preferences of unsurveyable populations. The pipeline is validated against reality, reproducing observed trade patterns. This policy laboratory delivers clear, counter-intuitive results. First, property-style relief is a false promise: “anonymous-data” carve-outs expand trade but ignore risk, causing aggregate welfare to collapse once external harms are priced in. Second, social welfare peaks when the downstream buyer internalizes the full substantive risk. This least-cost avoider approach induces efficient safeguards, simultaneously raising welfare and sustaining trade, and provides a robust empirical foundation for the legal drift toward two-sided reachability. The contribution is a reproducible pipeline designed to end the reliance on intuition. It converts qualitative insight into testable, comparative policy experiments, obsoleting armchair conjecture by replacing it with controlled evidence on how legal rules actually shift risk and surplus. This is the forward-looking engine that moves the field from competing intuitions to direct, computational analysis.

*K*eywords Data market ⋅\cdot
Data law ⋅\cdot
Comparative institutional analysis ⋅\cdot
Computational social science ⋅\cdot
Agent-based modeling

JEL classification C63 ⋅\cdot
D47 ⋅\cdot
D61 ⋅\cdot
K11 ⋅\cdot
K12 ⋅\cdot
K24

## 1 Introduction

Regulators are governing the AI economy in the dark. The market for data, its essential input, is so shrouded in opacity that it is impossible to govern effectively. This fundamental lack of visibility—not knowing who trades what, on what terms, or with what risk—is the root cause of the current policy chaos, which has fragmented into a mutually inconsistent toolkit of consent gates and liability rules (Solove,, [2013](https://arxiv.org/html/2510.26727v1#bib.bib52); Viljoen,, [2021](https://arxiv.org/html/2510.26727v1#bib.bib64); Citron and Solove,, [2022](https://arxiv.org/html/2510.26727v1#bib.bib11); Acquisti et al.,, [2015](https://arxiv.org/html/2510.26727v1#bib.bib2)). This paper confronts this regulatory blindness directly, proposes to turn on the lights. We develop an advanced, LLM-based Discrete-Choice Experiment (DCE) and Agent-Based Modeling (ABM) to simulate the data market in its entirety. This “computational testbed” provides the first clear view of how data transactions unfold, enabling researchers to finally move from speculation to empirical observation of which legal institutions truly work.

This epistemic void is no accident, it is a structural barrier. Traditional empirical tools falter in data markets because the underlying trades are both legally sensitive and systematically obscured. Regulators themselves have documented this opacity: the U.S. Federal Trade Commission’s in-depth study revealed sprawling, brokered pipelines with “limited transparency into who trades what, with whom, and on what terms.” This observability problem is even more acute in other jurisdictions. In China, a pronounced “compliance chill” following headline penalties, such as the Cyberspace Administration’s $1.2 billion fine against Didi, has pushed transactions further behind closed doors, frustrating any attempt at systematic measurement.

Even if this veil of opacity could be pierced, the market itself is built on a flawed foundation. The core economics of data inherently undermine efficient price discovery: its non-rival nature allows the same dataset to be used by multiple firms at once (Jones and Tonetti,, [2020](https://arxiv.org/html/2510.26727v1#bib.bib29)), pervasive externalities mean one party’s disclosure can impose unpriced costs on others, and Arrow’s information paradox dictates that quality cannot be valued ex ante without revealing the information itself. Compounding this market failure is a technical one: the chief legal safeguard, “anonymization,” routinely fails. Landmark studies show that putatively anonymous data can be readily re-identified, casting serious doubt on policies, such as GDPR Recital 26, that rely on this fragile premise (Sweeney,, [2000](https://arxiv.org/html/2510.26727v1#bib.bib55), [2001](https://arxiv.org/html/2510.26727v1#bib.bib56), [2002](https://arxiv.org/html/2510.26727v1#bib.bib57); Narayanan and Shmatikov,, [2008](https://arxiv.org/html/2510.26727v1#bib.bib37); Rocher et al.,, [2019](https://arxiv.org/html/2510.26727v1#bib.bib47)).

To build a model of a market so opaque, one must first uncover the hidden logic of its actors. Lacking access to confidential deal files, we conducted multi-year fieldwork to elicit the decision rules that firms actually use. Our findings reveal two critical, empirically grounded behaviors. On the demand side, buyers substitute reputation and relational signals for price discovery to navigate quality uncertainty, a mechanism predicted by classic theories of information asymmetry. On the supply side, sellers’ reservation prices co-move directly with perceived enforcement salience, as the risk of sanctions rises, so too does their willingness-to-accept. These core principles, reputation-based trust and risk-adjusted pricing, form the foundational logic of our agent-based model, ensuring our simulation reflects how the data market operates in reality, not just in theory.

To translate our field-informed rules into a testable model, we aim to break the empirical impasse that has stalled legal analysis of data markets. This paper pioneers a two-stage computational pipeline to do what traditional legal and empirical methods cannot: build a testable, behaviorally-grounded model of an opaque market. Our first innovation is to generate the missing preference data from the ground up. To parameterize agents without access to impossible-to-survey populations, we deploy a DCE using large language models, leveraging mounting evidence that LLMs can serve as “silicon samples” to credibly reproduce human preference distributions when elite populations are unreachable (Wang et al.,, [2024](https://arxiv.org/html/2510.26727v1#bib.bib65); Rathje et al.,, [2024](https://arxiv.org/html/2510.26727v1#bib.bib45); [Ziems et al., 2024a,](https://arxiv.org/html/2510.26727v1#bib.bib69) ; [Park et al., 2023a,](https://arxiv.org/html/2510.26727v1#bib.bib39) ). We ground this cutting-edge elicitation in classic econometric rigor, using the Train-McFadden tradition to recover precise attribute weights (McFadden,, [1972](https://arxiv.org/html/2510.26727v1#bib.bib34); Train,, [2009](https://arxiv.org/html/2510.26727v1#bib.bib61)).

Our second innovation is to embed these parameterized agents into an ABM that functions as a high-fidelity policy laboratory (Abar et al.,, [2017](https://arxiv.org/html/2510.26727v1#bib.bib1); Groeneveld et al.,, [2017](https://arxiv.org/html/2510.26727v1#bib.bib21); Railsback and Grimm,, [2019](https://arxiv.org/html/2510.26727v1#bib.bib44)). This is precisely what the field has lacked: a tool to move beyond static, brittle equilibrium models. This ABM allows us to simulate the complex, emergent effects of toggling rival legal regimes, from consent gates to liability rules, and record their impact on total welfare. We validate not by “predicting a single world,” but by testing the comparative statics of institutional design, thereby providing a powerful, new, and empirically-driven engine for legal theory.

For the first time, our computational laboratory moves the fragmented data-governance debate from the darkness of intuition to the light of direct, controlled comparison. Where policymakers have been forced to guess at the trade-offs of mutually inconsistent regimes, our model places them side-by-side in a simulated world to see what actually works (Ohm,, [2010](https://arxiv.org/html/2510.26727v1#bib.bib38)). The results are unequivocal, delivering a clear comparative-institutions message. First, property-style relief expands trade but fails to reliably raise welfare. Regimes that treat “anonymous” data as outside the law (like GDPR Recital 26) or rely on consent-gating predictably lower sellers’ costs. They do so, however, by removing the damages backstop that would otherwise discipline risky exchanges. The resulting trades fail to internalize the harm mass from re-identification, causing aggregate welfare to collapse once these social costs are deducted (MIT Sloan Ideas,, [2024](https://arxiv.org/html/2510.26727v1#bib.bib36)).

Our second and most counterintuitive result is that social welfare peaks when the buyer internalizes the full substantive risk. Across a wide grid of liability splits, assigning this component to the buyer simultaneously raises welfare and increases trade. The mechanism tracks classic law-and-economics: liability must rest with the least-cost avoider. In data trades, the downstream user controls post-acquisition safeguards and is best positioned to cheaply attenuate risk. Shifting liability to that locus induces efficient investment in care. Notably, this finding aligns perfectly with the legal trend toward two-sided reachability, from the GDPR’s direct liability for processors (Art. 82) to HIPAA’s for “Business Associates”. In short, our model “de-romanticizes” seller-only regimes, providing a robust empirical foundation for doctrines that make buyers legally reachable.

This paper, in short, provides an engine for seeing in the dark. We replace a debate mired in darkness and theoretical conjecture with the first clear, comparative light. We constructed this laboratory precisely because the field’s most critical questions, from property versus liability to risk versus access, could not be answered, only argued. Therefore, We are trying to build the computational laboratory that the fragmented data-governance debate has been missing, and the following sections detail the construction. By moving from field-informed decision rules to a high-fidelity, agent-based simulation, we hope a fundamental shift would happen in the entire debate: from competing intuitions to direct, comparative institutional analysis. In other words, the policymaking that has proceeded on guesswork, could now be brought into the light.

## 2 Institutional background

AI’s appetite for data is now a first-order economic fact, but the market for the most valuable inputs (clinical, financial, and other high-stakes institutional datasets) functions poorly. The reasons are structural: data are nonrival and re-usable, their value depends on uncertain complements and future uses, and the very act of disclosure complicates pricing (Arrow’s information paradox). At the same time, the standard safety valve “anonymization” is fragile under modern re-identification techniques, so externalities from downstream misuse remain material. In short, the canonical conditions that enable price discovery and welfare-enhancing exchange—well-defined marginal value, separable harms, and observability—are systematically violated in data markets.

Public policy has tried two broad playbooks. In the European Union, lawmakers have pursued access-mandate and intermediation strategies. The Data Act (Regulation (EU) 2023/2854) compels data holders, in defined circumstances, to make usage data accessible to users and third parties on fair, reasonable and non-discriminatory (FRAND) terms, and establishes guardrails for business-to-business sharing and switching costs, an explicit bid to pry open silos where bargaining alone has failed. Complementing this, the Data Governance Act creates a licensing and neutrality regime for “data intermediation services,” attempting to build trusted plumbing for reuse without fully reallocating entitlements.

China’s response has emphasized state-orchestrated market making. Since late 2021, dozens of municipal and provincial data exchanges (e.g., the Shanghai Data Exchange) have been launched with public sponsorship to standardize listings, vet counterparties, and broker trades, in parallel with top-down initiatives, from the 2022 “Twenty Data Measures” and, in 2023, the creation of a National Data Administration, to define “data as a factor of production” and accelerate circulation. This architecture reflects a doctrinal bet that clearer rights, standardized contracts, and visible marketplaces would transform latent supply into transactions (Ye and Zhu,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib67)).

The early record is mixed. Reviews of leading Chinese exchanges find limited trading activity, supply bottlenecks for sensitive/high-value datasets, and heavy reliance on government-coordinated deals, despite ambitious listing catalogs and strong headline demand from AI developers. Even where platforms report cumulative transaction tallies, closer analysis suggests volumes are modest relative to the size of the digital economy and concentrated in low-risk or state-brokered verticals. In effect, the infrastructure for a market exists, but the propensity to sell remains low for institutions that hold the most consequential data.
These outcomes are not accidental—they flow from the economics and governance of institutional data. First, because data are nonrival and option-like, ex ante valuation is noisy and depends on complements (algorithms, compute, domain fit) that buyers and sellers cannot fully contract on; Arrow’s paradox implies that efficient pricing often requires disclosure that undermines bargaining positions. Second, externalities from re-identification and misuse are hard to bound to the transactors, making private prices a poor proxy for social cost. Third, opacity of brokered pipelines means even regulators struggle to observe real trading practices or monitor risk, hampering doctrinal calibration. Together, these frictions help explain why high-value institutional data seldom reach open markets even when legal access rights or trading venues are created: rational holders resist one-off sales that sever control over future uses while exposing them to tail risk (He,, [2024](https://arxiv.org/html/2510.26727v1#bib.bib23)).

Against this backdrop, governments continue to refine institutional plumbing. The EU’s intermediation framework seeks to professionalize trust via neutrality duties, while China iterates on exchange governance and national coordination to standardize assetization and circulation. Yet the central dilemma remains: without a behaviorally explicit understanding of how rules reshape matching, pricing, and externalities in actual trades, prescriptions talk past each other. Our study takes this institutional status quo as the starting point and asks, within a unified, observable transactional environment, which legal designs actually increase participation and maximize welfare once externalities are priced.

## 3 Empirical design

### 3.1 Agent-based modeling

Current scholarship on data and privacy law largely remains grounded in traditional doctrinal approaches focused on legal interpretation and regulatory analysis. Most studies addressing these issues rely primarily on qualitative description and speculative reasoning, with limited engagement with theories and methods from decision science or computational modeling. To date, few works have examined the decision-making mechanisms and market behaviors of data sellers and buyers within the framework of computational social science—particularly through the use of agent-based modeling and simulation—to explore how legal rules interact with market dynamics. Although recent years have witnessed a gradual rise in quantitative research within interdisciplinary law and economics and empirical legal studies journals, mainstream quantitative analyses continue to rely predominantly on econometric techniques derived from classical statistics (Goldsmith and Vermeule,, [2002](https://arxiv.org/html/2510.26727v1#bib.bib20); Eisenberg,, [2010](https://arxiv.org/html/2510.26727v1#bib.bib16)). Some scholars have incorporated theories and methods from evolutionary game theory, social network analysis, and related fields into multi-agent systems to simulate complex social phenomena such as group decision-making (Fernández-Villaverde et al.,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib17); Sen et al.,, [2025](https://arxiv.org/html/2510.26727v1#bib.bib49)). Although this line of research generally lies outside the domain of legal studies, the models and methodologies developed therein provide valuable methodological references for examining law-related behavioral and institutional dynamics.

In fact, multi-agent systems (MAS), as a cutting-edge branch of distributed artificial intelligence, provide an exceptionally suitable modeling framework for the simulation and analysis of law and economic issues. An agent refers to a software entity endowed with autonomy, responsiveness, rational reasoning, and social interaction capabilities, pursuing the maximization of its own utility. A multi-agent system consists of multiple such agents that communicate and interact with one another, generating patterns of cooperation while also dynamically engaging with their surrounding environment. Through these interactions, agents both shape and adapt to their environment, leading to processes of mutual adaptation and co-evolution among agents and between agents and their environment.

In recent years, MAS has been increasingly adopted across international academia. Beyond the natural sciences and engineering, they have found wide application in social, economic, and military domains to simulate human behavior, conceptual change, and the evolution of cooperative relationships. Fundamentally, multi-agent systems are distributed rather than centralized: no single authoritative entity governs the interactions among agents. Instead, coordination emerges through decentralized communication and interaction, leading to self-organization and self-evolution. This decentralized structure resonates with the civil law principle of private autonomy.

At the same time, emerging legal issues such as data transactions—often characterized by regulatory uncertainty or even “illegal emergence” (Hu,, [2024](https://arxiv.org/html/2510.26727v1#bib.bib27))—lack clear normative guidance, rendering the strategic behavior of actors particularly crucial in shaping market outcomes. Although distributed, multi-agent systems are not fragmented. Their design and study seek to organize multiple agents in an integrated manner, establishing behavioral interaction rules, communication protocols, and coordination mechanisms that enable collective problem-solving beyond the capacity of any individual agent or linear aggregation of agents. This structure bears a striking resemblance to the market mechanism emphasized in microeconomics. Accordingly, multi-agent systems provide innovative perspectives, models, and methodologies for advancing research in law and economics.

Just as mainstream quantitative research methods in the social sciences must primarily rely on quasi-natural experiments aimed at causal inference—supplemented, at most, by rigorously ethically reviewed randomized controlled trials—rather than the large-scale laboratory experiments typical of the natural sciences, empirical examination of how legal systems shape data trading markets cannot be directly tested in the real world. On the one hand, modifications to legal rules or their application must adhere to strict constitutional and judicial procedures; on the other, legal norms and judicial authority carry profound societal implications and cannot be altered lightly. As a result, exploring complex social science questions—such as how legal institutions influence the structure and efficiency of data markets—proves difficult within conventional experimental paradigms. Conducting controlled, replicable experiments in real-world legal contexts is often impractical, unethical, or prohibitively costly. Consequently, mainstream legal research has tended to rely on qualitative reasoning and speculative analysis, complemented by quantitative studies grounded in econometric or behavioral approaches.

This paper seeks to “return” to the paradigm of experimental science by employing agent-based artificial intelligence models and computer-based simulations to construct a virtual experimental environment. Within this computational framework, ceteris paribus conditions can be strictly maintained, allowing for the parallel testing of different legal systems and liability allocation schemes to observe their long-term impacts on data markets and social welfare. Through this approach, the paper aims to provide both conceptual and computational foundations for the design of legal regulatory frameworks and the prediction of evolutionary trends in data transactions.

### 3.2 The model

This paper develops an agent-based model of the data trading market through a comprehensive modeling process that integrates mechanism analysis, institutional modeling, economic modeling, and computational implementation, thereby enabling experimental analysis. First, we construct a simulation sandbox by spatially partitioning China’s economy into a set of hexagonal cells. Second, we assign buyer and seller agents across these cells according to their respective socio-economic characteristics and spatial distributions. Third, we formalize the behavioral rules governing agent interactions—specifically their processes of searching, matching, and negotiation—through which the overall system dynamically evolves over time.

#### 3.2.1 The geographical sandbox

Our first step is to divide China’s economy—excluding Hong Kong, Macao, and Taiwan due to the distinctiveness of their legal jurisdictions—into 14,526 hexagonal cells, each with a radius of 20 kilometers and representing a potential industrial cluster, as shown in Fig. [1](https://arxiv.org/html/2510.26727v1#S3.F1 "Fig. 1 ‣ 3.2.1 The geographical sandbox ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law"). Compared with triangle or square grids, hexagons ensure equal distances to all six neighboring cells, minimizing directional bias and better approximating circular areas such as market catchments, commuting zones, or diffusion fronts, thus providing the most balanced and isotropic way to discretize continuous space. In economic geography, the use of hex grids also follows from the central place theory, which shows that under conditions of uniform population and transport costs, market areas tend to form hexagonal patterns (van Meeteren and Poorthuis,, [2018](https://arxiv.org/html/2510.26727v1#bib.bib63)). The 20-kilometer radius approximates the distance an individual worker can typically commute within 30 minutes, corresponding to the functional radius of contemporary urban areas (Marchetti,, [1994](https://arxiv.org/html/2510.26727v1#bib.bib33)). Accordingly, each hexagonal cell can be interpreted as a spatial unit within which industries operate under intra-city dynamics.

![Refer to caption](x1.png)

Fig. 1: Hexagonal grid with 20 km radius

Note: The dark blue lines indicate the boundaries of municipal administrative units.

#### 3.2.2 Agents: Buyers

We propose a buyer’s WTP incorporates multiple factors, ensuring each element is grounded in economic theory and empirical findings. Following Berry et al., ([1995](https://arxiv.org/html/2510.26727v1#bib.bib8)), we set a random coefficient logit model

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​j​tBuyer=f​(xi​t)⋅β​xj+τ​sj+γ​zi+ϕ​(sj×zi)−αi​pi​j​t−κ​ln⁡(1+di​j)+εi​j​t\begin{split}U^{\text{Buyer}}\_{ijt}=&f(x\_{it})\cdot\beta x\_{j}+\tau s\_{j}+\gamma z\_{i}+\phi(s\_{j}\times z\_{i})\\ &-\alpha\_{i}p\_{ijt}-\kappa\ln(1+d\_{ij})+\varepsilon\_{ijt}\end{split} |  | (1) |

on buyer ii’s utility Ui​j​tB​u​y​e​rU^{Buyer}\_{ijt} on dataset xjx\_{j} provided by seller jj at time tt, with random coefficient αi\alpha\_{i} captures how the utility of dataset xjx\_{j} for buyer ii depends on the price pi​j​tp\_{ijt}. sjs\_{j}, xjx\_{j}, ziz\_{i}, and di​jd\_{ij} represent observable features.

1. Seller’s institutional strength.
The first factor sjs\_{j} we introduce is seller jj’s institutional strength or tier. This is a novel and important component of our model. We posit that the seller’s reputation and category serve as a crucial signal of data quality and reliability. This hypothesis is informed by a key observation from multi years field research: in real-world data markets, buyers often struggle to assess the exact value and quality of a dataset before purchase (value of data highly depends on the siuation). There is pervasive uncertainty about data value, sometimes referred to as the “data value uncertainty” problem. In fact, classic information economics (Arrow’s information paradox) tells us that a buyer cannot fully evaluate information goods like data without first having them, but once acquired, the data’s value is revealed. Because data cannot be fully disclosed or tested pre-sale, buyers face a lemon’s problem where they fear overpaying for low-quality data.

Our model addresses this by recognizing that, in practice, buyers resort to indirect valuation heuristics. One critical heuristic is to judge the data by the seller’s identity. A dataset offered by a top-tier, reputable institution (say a renowned national hospital) will inspire higher willingness to pay than a dataset from a small unknown provider, even if the datasets are ostensibly similar. This is consistent with theories of signaling and reputation: when product quality is uncertain, observable signals like the seller’s credibility or brand substantially influence buyer valuations (Cabral and Hortacsu,, [2010](https://arxiv.org/html/2510.26727v1#bib.bib9)). Indeed, empirical studies find that under quality uncertainty, buyers lean heavily on brand or reputation cues and are willing to pay price premiums for trusted sources (Tadelis,, [2016](https://arxiv.org/html/2510.26727v1#bib.bib58); Einav et al.,, [2016](https://arxiv.org/html/2510.26727v1#bib.bib15); [Li et al., 2020a,](https://arxiv.org/html/2510.26727v1#bib.bib31) ).

In our context, prior research on data transactions has often tried to price data solely by its attributes, largely failing because they ignored how deals are actually made. By contrast, our approach acknowledges that buyers “price” the data by pricing the seller, which is effectively using the seller’s tier as a proxy for data quality and as a risk-mitigation strategy, thus brings our model closer to reality. In our application, sellers are classified from S1S\_{1} (lowest tier) up to S5S\_{5} (highest tier) based on their scale and capabilities(for example, S1S\_{1} denotes a grassroots community hospital, while S5S\_{5} denotes a national hub hospital at the apex of the healthcare system). It captures the intuitive and observed behavior that data from, say, a prestigious Level S5S\_{5} hospital is expected to be more valuable (more comprehensive, accurate, and trustworthy) than data from an S1S\_{1} community clinic, and buyers’ willingness to pay reflects that expectation.

2. Data volume and diminishing returns.
A buyer with very little data initially will derive high marginal benefit from acquiring additional data, whereas a buyer who already has vast datasets sees a smaller incremental benefit. This assumption is rooted in both economic theory (the law of diminishing marginal returns) and the empirical reality of machine learning: early data greatly improve model performance, but beyond a certain threshold, each extra data yields smaller improvements (Hestness et al.,, [2017](https://arxiv.org/html/2510.26727v1#bib.bib24); Kaplan et al.,, [2020](https://arxiv.org/html/2510.26727v1#bib.bib30); Hoffmann et al.,, [2022](https://arxiv.org/html/2510.26727v1#bib.bib25)). We include this component to ensure the model mirrors realistic data valuation behavior: under equal data quality, larger quantities command higher prices, but with a tapering effect. This aligns with general economic intuition (more of a good increases utility, but at a decreasing rate) and is supported by recent studies on data value which find that accuracy gains from additional data eventually face diminishing returns.

Therefore, we define f​(xi)⋅xj,tf(x\_{i})\cdot x\_{j,t} represents the utility gain from the quantity of data obtained. Here xj,tx\_{j,t} is the volume of data that seller jj offers at time tt, and xix\_{i} is the volume of data buyer ii already possesses. We define f​(xi)f(x\_{i}) as a diminishing marginal utility function of the buyer’s existing data holdings. In particular, one can think of f​(xi)f(x\_{i}) as an increasing concave function like f​(xi)=e−ρ​xif(x\_{i})=e^{-\rho x\_{i}}. In other words, f​(xi)f(x\_{i}) decreases as xix\_{i} grows, reflecting that once a buyer’s data repository has reached a substantial size, their urgency or marginal willingness-to-pay for yet more data tapers off. Thus, a buyer’s base utility from a dataset of size xj,tx\_{j,t} is f​(xi)×xj,tf(x\_{i})\times x\_{j,t}, so that a big data purchase is more valuable when the buyer truly needs data, and slightly less so when the buyer already has abundant data.

3. Geographical Distance.
Proximity lowers transaction costs and builds trust, which in turn increases the likelihood and value of a data transaction. Even in data markets, which are often thought to be global, spatial and social proximity can facilitate communication, repeat interactions, and better information flow about the data being exchanged. Prior research in economic sociology and network theory has shown that closer geographic distance fosters stronger information-sharing networks and trust between trading partners. For example, Uzzi’s study of New York’s Garment District found that firms located nearer to each other formed richer relationships and transacted more easily, due to frequent interaction and reduced information asymmetries (Uzzi,, [1996](https://arxiv.org/html/2510.26727v1#bib.bib62)).

In our context, a buyer located near a seller might more easily verify data quality (perhaps via on-site visits or shared community ties) and face lower coordination costs, thereby deriving greater utility (or less disutility) from the exchange. Empirical evidence also supports this: geographic proximity fosters trust and information sharing, offering competitive advantages in business dealings (Petersen and Rajan,, [2002](https://arxiv.org/html/2510.26727v1#bib.bib41); Sorenson and Stuart,, [2001](https://arxiv.org/html/2510.26727v1#bib.bib53); Audretsch and Feldman,, [1996](https://arxiv.org/html/2510.26727v1#bib.bib6)). By contrast, a large distance can introduce communication delays, unfamiliarity, and legal or jurisdictional complications, effectively reducing a buyer’s expected utility from the deal (Porter,, [1998](https://arxiv.org/html/2510.26727v1#bib.bib42)).

Therefore, we include the term −κ​ln⁡(1+di​j)-\kappa\ln(1+d\_{ij}) to capture the effect of physical or geographic distance between buyer ii and seller jj on the transaction utility. Here di​jd\_{ij} is the distance between the two parties, and we use ln⁡(1+d)\ln(1+d) to allow a diminishing effect of distance, and to handle zero distance gracefully. We include the distance term with a negative sign (through −κ<0-\kappa<0) to reflect this impediment of distance – the farther apart the buyer and seller, the lower the buyer’s net utility (all else equal), which is consistent with gravity models of trade and countless studies highlighting distance as a barrier to transactions.

4. Price sensitivity heterogeneity.
Rather than assume all buyers react identically to price, we allow heterogeneous αi\alpha\_{i} across buyers. This reflects the well-documented fact that different buyers respond differently to prices for the same good. For example, a large tech firm is likely less sensitive to price changes than a small startup, due to larger budgets and strategic needs. In discrete-choice demand models, incorporating such heterogeneity in price coefficients is standard, as it improves realism and fit.

We therefore treat αi\alpha\_{i} as a random coefficient (to be estimated via a hierarchical Bayesian approach rather than a simple OLS), allowing us to recover a distribution of price sensitivities across buyers rather than a single average. This approach is common in industrial organization and marketing science, and acknowledges that even for a homogenous product, buyers’ valuation of price varies widely (Allenby and Rossi,, [1998](https://arxiv.org/html/2510.26727v1#bib.bib3); Duvvuri et al.,, [2007](https://arxiv.org/html/2510.26727v1#bib.bib14)). By estimating a distribution of αi\alpha\_{i}, our model captures this real-world variation and aligns with classical structural econometric practices. In short, higher-tier buyers are modeled with a lower effective αi\alpha\_{i} (dampened price sensitivity), which makes the WTP less negatively affected by price. A realistic feature given that, in practice, enterprise-level buyers do not abandon purchases over small price differences as easily as cash-constrained buyers.

5. Buyer’s firm tier and budget constraint.
Analogous to sellers, we categorize each buyer ii’s own capability tier as ziz\_{i} (with coefficient γ\gamma). Buyers are grouped from z1z\_{1} (lowest) to z5z\_{5} (highest) based on their technological prowess and market position. For instance, a z1z\_{1} buyer might be a small AI start-up that mainly offers integration services and lacks proprietary algorithms, whereas a z5z\_{5} buyer could be a “national strategic” tech company with cutting-edge R&D and substantial market power. We include ziz\_{i} to control for the notion that stronger buyers derive systematically different utility from data purchases. A high-tier buyer often has superior data analytics infrastructure and complementary assets, meaning they can extract more value from any given dataset.

Moreover, incorporating ziz\_{i} also implicitly brings in the effect of budget constraints and scale. In our design, each buyer tier z1z\_{1} (lowest) to z5z\_{5} (highest) is associated with an approximate data procurement budget band. We set z1z\_{1} have a budget on the order of 10,000, whereas z5z\_{5} can spend around 10 million or more annually on data). We base these budget magnitudes on observed firm sizes. For example, it’s not unreasonable for a tech giant with annual revenue in the hundreds of billions to allocate on the order of 10 million for data purchases. Empirical distributions of firm sizes and expenditures are highly skewed (approximately log-normal or Pareto-tailed), so differences of one or two orders of magnitude in budget between tiers are quite realistic. By drawing each tier’s budget from a log-scale range (z1z\_{1} through z5z\_{5} increasing by 10 times each level), we acknowledge the heavy-tailed nature of the industry (many small buyers with tiny budgets and a few very large buyers with massive budgets). In sum, ziz\_{i} serves as a proxy for the buyer’s overall capacity to acquire and utilize data. A higher ziz\_{i} means the buyer not only can pay more (relaxed budget constraint) but also likely values the data more in their operations, which justifies a positive contribution to WTP.

6. Buyer-seller interaction.
In addition to the individual effects of buyer and seller tiers, we include an interaction term sj×zis\_{j}\times z\_{i} with coefficient ϕ\phi. This term allows for complementarity or mismatch effects between the characteristics of the buyer and seller. Our hypothesis is that the utility impact of a seller’s tier may depend on the buyer’s own tier, and vice versa. For example, a top-tier tech firm z5z\_{5} acquiring data from a top-tier hospital s5s\_{5} might generate especially high synergy. This is because the advanced buyer can fully exploit the rich dataset from the elite seller, perhaps yielding insights or products of great value. In contrast, if a small z1z\_{1} startup obtained that same s5s\_{5} dataset, it might lack the resources to use the data effectively, resulting in comparatively lower realized utility.

This reasoning suggests a positive interaction ϕ>0\phi>0 would mean that high–high pairings (strong buyer with strong seller) produce more than additive utility, whereas low–low pairings might be the only feasible matches at the other end. This pattern is reminiscent of assortative matching in economics, where agents of similar “quality” tend to partner with each other. Indeed, there is evidence of positive assortative matching by capability. Studies of exporter–importer matches finds that because of complementarity, only high-capability exporters can match with high-capability importers (Benguria,, [2021](https://arxiv.org/html/2510.26727v1#bib.bib7); Sugita et al.,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib54)). By analogy, in our data market, a cutting-edge AI firm is more likely to do business (and derive high utility) with a top-tier data provider, whereas a modest buyer and a modest seller may suffice for each other’s needs. Including the interaction term sj×zis\_{j}\times z\_{i} allows our model to capture such nuances. It recognizes that the ”fit” between buyer and seller matters: a well-resourced buyer can unlock extra value from a high-quality data source, reflected in a higher WTP when both sjs\_{j} and ziz\_{i} are large, whereas for a lower-tier buyer that same high-quality source might be less of a game-changer. This term is an exploratory addition to see if there is evidence of synergy (or incompatibility) in the matching of buyers and sellers in the data market.

7. Action strategy. Putting these together, the buyer’s willingness to pay on dataset xjx\_{j} at time tt is given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | WTPi​j​t=f​(xi​t)⋅β​xj+τ​sj+γ​zi+ϕ​(sj×zi)−κ​ln⁡(1+di​j)αi.\text{WTP}\_{ijt}=\frac{f(x\_{it})\cdot\beta x\_{j}+\tau s\_{j}+\gamma z\_{i}+\phi(s\_{j}\times z\_{i})-\kappa\ln(1+d\_{ij})}{\alpha\_{i}}. |  | (2) |

In each period tt, buyers iterate through all the unconnected sellers and compute a willingnness to pay (WTPi​j​t\text{WTP}\_{ijt}) for each seller jj. Each buyer then selects the seller jj with the highest WTPi​j​t\text{WTP}\_{ijt} among all potential sellers and attempts to establish a connection. Once connectionns are formed—according to the action strategy outlinend in Algorithm [2](https://arxiv.org/html/2510.26727v1#alg2 "Algorithm 2 ‣ 3.2.3 Agents: Sellers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law")—the paired agents negotiate a transaction price pi​j​tp\_{ijt}. A deal is executed if the negotiated price does not exceed the buyer’s budget constraint. The detailed action strategy of buyers is presented in Algorithm [1](https://arxiv.org/html/2510.26727v1#alg1 "Algorithm 1 ‣ 3.2.2 Agents: Buyers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law").

Algorithm 1  Buyer’s action strategy

STEP\_BUYER(b, s)

WTPi​j​t←UBuyer​(bi,sj)\text{WTP}\_{ijt}\leftarrow U^{\text{Buyer}}(b\_{i},\ s\_{j}) for sj∈{connected=0}s\_{j}\in\{\textbf{connected}=0\}

select sjs\_{j} if WTPi​j​t=maxj∈Seller⁡(WTP)\text{WTP}\_{ijt}=\max\_{j\in\textbf{Seller}}(\text{WTP})

connected ←\leftarrow [STEP\_SELLER(b, s)](https://arxiv.org/html/2510.26727v1#alg2 "Algorithm 2 ‣ 3.2.3 Agents: Sellers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law")

if connected:

if WTPi​j​t≤WTAj​t\text{WTP}\_{ijt}\leq\text{WTA}\_{jt}:

return

else:

pi​j​t←p∈[WTAj​t,WTPi​j​t]p\_{ijt}\leftarrow p\in[\text{WTA}\_{jt},\text{WTP}\_{ijt}]

if pi​j​t>mi​tp\_{ijt}>m\_{it}:

return

else:

xi​t=xi,t−1+xjx\_{it}=x\_{i,t-1}+x\_{j}

mi​t=mi,t−1−pi​j​tm\_{it}=m\_{i,t-1}-p\_{ijt}

return

else:

return

Note: b and s denote individual buyer and seller agents, respectively. Seller denotes the set of sellers. connected is a Boolean indicator representing the connection status between a buyer and a seller. mi​tm\_{it} denotes the remaining budget of buyer ii at time tt.

#### 3.2.3 Agents: Sellers

On the supply side, we also specify a utility (profit) function for the seller and derive a corresponding willingness-to-accept (WTA)—essentially the minimum price the seller is willing to accept for the data. While the buyer’s utility above is the more complex part of the model, it is important to note how sellers’ considerations enter, especially via costs and risks. In our model, a seller jj’s net utility from selling data (inside a logit framework) is modeled as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​j​tSeller=αj​pi​t−(c0+c1​sj+c2​xj+β1​Rj+β2​Ej​t)+εj​t,U\_{ijt}^{\text{Seller}}=\alpha\_{j}p\_{it}-(c\_{0}+c\_{1}s\_{j}+c\_{2}x\_{j}+\beta\_{1}R\_{j}+\beta\_{2}E\_{jt})+\varepsilon\_{jt}, |  | (3) |

where pi​tp\_{it} is the price paid by buyer ii, and the terms in parentheses represent the seller’s costs or disutility from the transaction. Here αj\alpha\_{j} s a seller-specific random coefficient on price. Analogous to buyers’ random coefficient αi\alpha\_{i}, it captures how strongly the seller values additional revenue. We generally assume sellers are fairly insensitive to a single transaction’s price beyond its profit, so αj\alpha\_{j} may not vary as much as buyers’ do. The cost terms are as follows.

1. Baseline and volume-dependent cost.
Selling data is not costless for the seller (Radauer,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib43)). c0c\_{0} represents fixed costs, for example, the overhead of setting up a data transfer, the opportunity cost of diverting managerial attention, or a base level of discomfort in sharing data. c2​xj,tc\_{2}x\_{j,t} is a variable cost proportional to the volume of data sold. This could capture the computational and labor effort to prepare and deliver a larger dataset, or the notion that giving away a bigger chunk of one’s data asset entails a greater loss of competitive advantage. In short, the more data is transacted, the higher the cost to the seller, due both to direct handling costs and the growing potential harm of releasing a large dataset. This is consistent with standard cost structures where larger transactions incur higher marginal costs (or require greater compensation).

2. Transaction risk.
We introduce a factor RjR\_{j} to denote the risk level associated with the data transaction for the seller. Not all data trades are equally safe; some data, if shared, can lead to significant negative consequences. We categorize risk into 3 levels, Low, Medium, High based on the potential negative externalities or liabilities. For example, a low-risk data exchange might cause only minimal, controllable issues if misused, whereas a high-risk exchange could entail serious public safety or privacy breaches, imagine selling highly sensitive personal health data, which, if leaked or misused, could trigger a public outcry or lawsuits.

Higher risk RjR\_{j} effectively increases the seller’s disutility from the transaction, since the seller bears a chance of facing reputation damage, legal liability, or moral cost if the data is misused. Thus βR×Rj\beta\_{R}\times R\_{j} in the cost function would be positive—a seller requires a higher price to be willing to undertake a high-risk sale. Including a risk term is important in a law and economics context: it aligns with the idea that when transactions impose potential harm or expected costs (even probabilistically), the selling party will demand compensation for that risk (a form of private risk premium) (Simpson et al.,, [2021](https://arxiv.org/html/2510.26727v1#bib.bib50); [Li et al., 2020b,](https://arxiv.org/html/2510.26727v1#bib.bib32) ). This is analogous to how a supplier of a hazardous product would charge more to offset liability risk. Although difficult to measure directly, we incorporate discrete risk levels to acknowledge this factor in data markets (Meier et al.,, [2024](https://arxiv.org/html/2510.26727v1#bib.bib35)). It reflects findings that lack of trust and fear of negative outcomes can stymie data sharing, because sellers are more hesitant and demand higher WTA when the perceived risk is high (Gefen et al.,, [2019](https://arxiv.org/html/2510.26727v1#bib.bib19); Skatova et al.,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib51); Wang et al.,, [2021](https://arxiv.org/html/2510.26727v1#bib.bib66)).

3. Regulatory enforcement.
In tandem with risk, we include EjE\_{j} to represent the strength of regulatory enforcement in the environment. This factor is segmented (Weak, Moderate, Strong) based on how strictly data regulations (privacy laws, cybersecurity laws, etc.) are enforced by authorities. Strong enforcement means there are serious consequences if the data transaction violates any law or policy, or instance, robust audits, frequent inspections, and harsh penalties for non-compliance. We expect βE×Ej>0\beta\_{E}\times E\_{j}>0 as well: in jurisdictions or scenarios with aggressive enforcement, sellers will be much more cautious about selling data (especially personal or sensitive data) and will only do so at a higher price to justify the risk. This is well grounded in reality. Sellers are markedly more cautious because downside risks are now large, salient, and routine. Headline penalties, like the EU’s €1.2B fine against Meta and China’s $1.2B fine against Didi, establish a billion-dollar risk ceiling. This is not just an outlier phenomenon; sustained, multi-million-dollar enforcement under GDPR and U.S. HIPAA (e.g., Anthem’s $16M) makes eight-figure penalties a recurring operational cost. Compounded by massive, recurring compliance outlays, sellers rationally internalize this exposure by demanding higher reservation prices or declining risky transactions altogether.

Such punitive potential clearly affects a firm’s calculus: a seller in a strict regulatory regime will factor in the expected cost of possible penalties. Effectively, strong enforcement raises the seller’s reservation price. Our model captures this by adding the EjE\_{j} term: under E3E\_{3} (strong enforcement), the cost term is higher, leading to a larger WTA. Conversely, if enforcement is weak or toothless as E1E\_{1}, sellers face less expected penalty cost and can afford a lower WTA. This approach echoes the economic principle that agents respond to expected legal sanctions, higher probability or severity of punishment necessitates greater compensation for taking the action.

4. Seller’s own institutional tier.
In data transaction, the seller’s institutional tier sjs\_{j} proxies for a bundle of institution-intrinsic factors that raise the shadow cost of supply even when volume xjx\_{j}, deal-specific risk RR, and ambient enforcement Ej​tE\_{jt} are held constant. First, high-tier sellers possess stronger outside options. They can internalize larger benefits from exclusive in-house use, downstream collaborations, or future monetization, so releasing data destroys more private rents and thus requires higher compensation. Second, reputation capital makes disclosure costlier at the top. Elite hospitals and platforms bear greater expected losses from brand damage, patient or user backlash, and professional scrutiny. Therefore, they demand a premium for incremental exposure even if legal sanctions are unchanged. Third, governance overhead rises with tier. Rigorous provenance curation, quality control, ethics review, security and audit pipelines are more extensive in leading institutions, inflating both fixed and variable sharing costs beyond what xjx\_{j} alone captures. Interpreted this way, c1​sjc\_{1}s\_{j} isolates capability- and reputation-based cost and rent components, while RjR\_{j} and Ej​tE\_{jt} continue to represent transaction- and regime-level hazards, avoiding double counting. The specification yields clear empirical content: conditional on xjx\_{j}, RjR\_{j}, and Ej​tE\_{jt} higher-tier sellers should exhibit higher reservation prices.

5. Risk-enforcement interaction.
To capture how regulation regimes transform latent hazards into expected costs, we augment the seller’s reservation price with a risk–enforcement interaction. Including Rj​Ej​tR\_{j}E\_{jt} reflects a standard law-and-economics intuition: risk becomes costly to the seller to the extent it is enforced. In data transactions, many harms (re-identification, leakage, unlawful reuse) are probabilistic and partly externalized. Strong enforcement converts those latent harms into internalized expected penalties through higher detection probability, stricter auditing, and more severe sanctions. Conversely, when enforcement is weak, even high intrinsic risk may not translate into comparable private cost. This specification also avoids double counting: RjR\_{j} captures the transaction’s inherent hazard, Ej​tE\_{j}t captures the surrounding intensity of regulation control, and the interaction Rj​Ej​tR\_{j}E\_{jt} captures how the very same hazard is priced under different regulatory environments.

6. Action strategy. Putting these together, the seller’s minimum acceptable price (willingness to accept, WTA) can be derived from the condition Uj​tSeller=0U\_{jt}^{\text{Seller}}=0 (indifference to trading or not). Solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | αj​pi​j​t=c0+c1​sj+c2​xj+β1​Rj+β2​Ej​t+δ​Rj​Ej​t\alpha\_{j}p\_{ijt}=c\_{0}+c\_{1}s\_{j}+c\_{2}x\_{j}+\beta\_{1}R\_{j}+\beta\_{2}E\_{jt}+\delta R\_{j}E\_{jt} |  | (4) |

gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | WTAj​t=c0+c1​sj+c2​xj+β1​Rj+β2​Ej​t+δ​Rj​Ej​tαj.\text{WTA}\_{jt}=\frac{c\_{0}+c\_{1}s\_{j}+c\_{2}x\_{j}+\beta\_{1}R\_{j}+\beta\_{2}E\_{jt}+\delta R\_{j}E\_{jt}}{\alpha\_{j}}. |  | (5) |

This formula shows that a seller will set a higher floor price for transactions that are costly, risky, or legally perilous. It resonates with the intuition that data suppliers need to be compensated for both direct costs and indirect expected costs (like risk of sanctions). Notably, many of the seller-side coefficients mirror those in the buyer utility. (e.g., xjx\_{j} appears for both sides, reflecting that volume affects both benefit to buyer and cost to seller). However, the enforcement (EE) and risk (RR) variables are uniquely pertinent to the legal-economic environment of the seller, underlining our paper’s focus on law and economics interplay in data markets.

Through interactions with buyers and exogenous market environment, each seller’s action strategy involves sensing, decision-making, and updating, as outlined in Algorithm [2](https://arxiv.org/html/2510.26727v1#alg2 "Algorithm 2 ‣ 3.2.3 Agents: Sellers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law"). In each period tt, sellers update their WTA by recalculating it under the renewed enforcement intensity Ej​tE\_{jt} and comparing the result with the previous transaction price pj,t−1p\_{j,t-1}; the higher value is adopted as the new WTAj​t\text{WTA}\_{jt}. Each seller then selects, from the set of received buyer offers, the buyer with the highest WTP and communicates this choice back to the buyers.

Algorithm 2  Seller’s action strategy

STEP\_SELLER(b, s)

WTAj​t←USeller​(bi,sj)\text{WTA}\_{jt}\leftarrow U^{\text{Seller}}(b\_{i},\ s\_{j}) with Ej​tE\_{jt}

WTAj​t←max⁡{WTAj​t,pj,t−1}\text{WTA}\_{jt}\leftarrow\max\{\text{WTA}\_{jt},\ p\_{j,t-1}\}

select bib\_{i} if WTPi​j​t=maxbi∈Received⁡(WTP)\text{WTP}\_{ijt}=\max\_{b\_{i}\in\textbf{Received}}(\text{WTP})

return (bib\_{i}, connected)

  

Note: b and s denote individual buyer and seller agents, respectively. Ej​tE\_{j}t denotes the enforcement intensity on seller jj at time tt. Received denote the set of potential buyers. connected is a Boolean indicator representing the connection status between a buyer and a seller.

#### 3.2.4 External environment

1. Volume-indexed assignment of transaction risk.
In the model, the risk class attached to a data sale is not a fixed attribute of the seller or the contract. Instead, it is an environmental label that reflects how regulators, counterparties, and technical auditors would probabilistically perceive the hazard of a contemplated transfer given the scale of data involved. Formally, we treat the seller’s risk level R∈{1,2,3}R\in\{1,2,3\} as a discrete, ordered outcome that is randomly drawn conditional on the seller’s data volume xjx\_{j}. The economics intuition is straightforward: larger datasets expand the attack surface through greater likelihood and scope of leakage, and raise the third-party exposure from re-identification. Hence, holding all else equal, larger xjx\_{j} should be associated with a higher probability of being classified as medium or high risk. We implement this mapping with an ordered logit. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | zR​(xj)=ln⁡(1+xjscale),scale>0z\_{R}(x\_{j})=\ln\left(1+\frac{x\_{j}}{\text{scale}}\right),\quad\text{scale}>0 |  | (6) |

a monotone, concave transform that tempers extreme volumes and yields stable probabilities across heterogeneous sellers. The ordered logit then assigns probabilities to R=1,2,3R=1,2,3 using a slope (intensity) parameter γ=R​\_​l​o​g​i​t​\_​g​a​m​m​a>0\gamma=R\\_logit\\_gamma>0 and two cut points c1<c2c\_{1}<c\_{2} (R\_logit\_cuts):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡(R=3∣xj)=σ​(γ​[zR​(xj)−c2]),Pr⁡(R=2∣xj)=σ​(γ​[zR​(xj)−c1])−Pr⁡(R=3∣xj),Pr⁡(R=1∣xj)=1−Pr⁡(R=2∣xj)−Pr⁡(R=3∣xj),\begin{split}&\Pr(R=3\mid x\_{j})=\sigma(\gamma[z\_{R}(x\_{j})-c\_{2}]),\\ &\Pr(R=2\mid x\_{j})=\sigma(\gamma[z\_{R}(x\_{j})-c\_{1}])-\Pr(R=3\mid x\_{j}),\\ &\Pr(R=1\mid x\_{j})=1-\Pr(R=2\mid x\_{j})-\Pr(R=3\mid x\_{j}),\end{split} |  | (7) |

where σ​(u)=11+e−u\sigma(u)=\frac{1}{1+e^{-u}}.

Two design choices make this assignment data-adaptive rather than ad hoc. First, the scaling constant s​c​a​l​e=R​\_​l​o​g​i​t​\_​s​c​a​l​escale=R\\_logit\\_scale is calibrated from the cross-section of sellers, using the median of positive xjx\_{j}, anchoring zRz\_{R} near zero for a typical seller and preventing extreme volumes from mechanically saturating the top risk class. Second, the cut points (c1,c2)(c\_{1},c\_{2}) are set endogenously to the market’s volume distribution. We take the 33rd and 67th percentiles of zRz\_{R} across all sellers. This yields an baseline: in an otherwise uninformative environment, roughly one third of sellers would fall into each risk tier; as volumes shift (e.g., because entry brings many small sellers, or consolidation yields a few very large ones), the induced risk mix adjusts mechanically rather than by manual re-tuning.

Economically, the specification implies testable predictions. Holding seller tier sjs\_{j} and enforcement Ej​tE\_{j}t fixed, thicker right tails in the market’s xjx\_{j} distribution push mass toward higher RR, raising average WTA and reducing marginal trade at the top end. Tightening γ\gamma (a steeper slope) amplifies this effect, yielding more convex risk premia in volume. Conversely, if market development lowers typical package sizes (a left shift in xjx\_{j}), the induced downgrading of RR relaxes sellers’ reservation prices and expands feasible trades—precisely the margin along which data minimization, sampling, or purpose-limited access policies are expected to improve welfare.

2. Activity-indexed enforcement intensity.
Whereas the intrinsic transaction risk RjR\_{j} is an exogenous label tied to a seller’s own data volume and assigned once at entry, enforcement intensity Ej​t∈{1,2,3}E\_{jt}\in\{1,2,3\} is modeled as a dynamic, locally endogenous state that evolves with market activity in the seller’s surroundings. The economic intuition is that regulators, auditors, platforms, and public scrutiny allocate attention where the probability and salience of violations are highest. In data markets, that attention is not uniformly distributed: spatial and temporal “hot spots” emerge as volumes concentrate, raising detection probabilities, tightening audits, and increasing the expected private cost of non-compliance. We capture this by letting Ej​tE\_{j}t be re-classified each period via an ordered logit that depends on recent neighborhood trade volume.

At initialization (t=0)(t=0), there is no history, so all sellers start at the baseline Ej​0=1E\_{j0}=1. At the beginning of each subsequent period, the model computes, for every seller jj, a windowed neighborhood total of traded data: the sum of all package sizes xx transacted in jj’s own cell plus its geometrically adjacent cells over the last EwindowE\_{\text{window}} periods. If this total is zero, enforcement remains at the baseline Ej​t=1E\_{jt}=1. Otherwise, the total is converted into a concave, monotone score

|  |  |  |  |
| --- | --- | --- | --- |
|  | zE=ln⁡(1+totalscale),z\_{E}=\ln\left(1+\frac{\text{total}}{\text{scale}}\right), |  | (8) |

which tempers extreme spikes while preserving rank. This score is mapped to probabilities for E∈{1,2,3}E\in\{1,2,3\} through an ordered-logit link with slope γE>0\gamma\_{E}>0 and cut points c1(E)<c2(E)c\_{1}^{(E)}<c\_{2}^{(E)}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡(E=3∣zE)=σ​(γE​[zE−c2(E)]),Pr⁡(E=2∣zE)=σ​(γE​[zE−c1(E)])−Pr⁡(E=3∣zE),Pr⁡(E=1∣zE)=1−Pr⁡(E=2∣zE)−Pr⁡(E=3∣zE),\begin{split}&\Pr(E=3\mid z\_{E})=\sigma(\gamma\_{E}[z\_{E}-c\_{2}^{(E)}]),\\ &\Pr(E=2\mid z\_{E})=\sigma(\gamma\_{E}[z\_{E}-c\_{1}^{(E)}])-\Pr(E=3\mid z\_{E}),\\ &\Pr(E=1\mid z\_{E})=1-\Pr(E=2\mid z\_{E})-\Pr(E=3\mid z\_{E}),\end{split} |  | (9) |

with σ​(u)=(1+e−u)−1\sigma(u)=(1+e^{-u})^{-1}. A seller’s Ej​tE\_{j}t for the current step is a single draw from this categorical distribution.This adaptive calibration lets the enforcement landscape track endogenous changes in congestion. As activity clusters or disperses, the implied thresholds shift without manual tuning. Economically, this specification formalizes a local feedback mechanism between market conduct and legal exposure. Concentrated trading raises zEz\_{E}, which increases the probability of being classified at E=2​or​E=3E=2\ \text{or}\ E=3, thereby internalizing a greater portion of social monitoring and sanction risk into sellers’ reservation prices in the next round. The model thus embeds the comparative statics that policy makers care about: increases in neighborhood volume raise expected enforcement, and the risk–enforcement complementarity (β3>0)(\beta\_{3}>0) ensures that this bite is strongest precisely where intrinsic hazards are high. Unlike a fixed-penalty assumption, the activity-indexed Ej​tE\_{j}t captures how regulatory capacity, platform audits, and public attention endogenously follow the market, yielding a lawful channel through which local congestion begets stricter oversight and, in turn, reshapes equilibrium prices, participation, and spatial patterns of trade.

#### 3.2.5 Spatial distribution of agents

To ensure that our agent-based model accurately reflects the read-world industrial landscape and maintains the practical relevance of its geographic sandbox, agents are allocated across the hexagonal grid based on the actual spatial distribution of industries. On the buyer side, we compiled data on the number of artificial intelligence enterprises registered inn each county and district across mainland China and projected these counts onto the cells using an equal distribution method within each administrative region. On the seller side, we identified top-tier hospitals through their points of interest (POI) coordinates and calculated the number of such hospitals within each cell, using this measure as a proxy for the spatial distribution of medical resources.

We applied the Jenks, ([1963](https://arxiv.org/html/2510.26727v1#bib.bib28)) natural breaks classification algorithm to divide the industrial and medical resources attributes of the cell grid into six tiers. Without loss of generality, we simplified the agent distribution in the model as follows: Tier 0 contains no agents; Tier 1 contains one Level-1 agent; Tier 2 contains one Level-1 agent and one Level-2 agent; and so forth, with Tier 5 containing one agent from each level, from Level 1 through Level 5. The spatial distribution of buyer and seller agents are shown in Fig. [2](https://arxiv.org/html/2510.26727v1#S3.F2 "Fig. 2 ‣ 3.2.5 Spatial distribution of agents ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law").

![Refer to caption](x2.png)

Fig. 2: Distribution of agents

Note: The graphs illustrate the spatial distribution of buyer and seller agents, with colors indicating the number of agents within each cell, respectively.

#### 3.2.6 Interaction cycles

At time t=0t=0, the spatial positions and attributes of all agents are initialized according to the predefined rules. The exogenous enforcement intensity is initially set at a low level (E=1E=1). In each subsequent period tt, the system evolves following the process outlined in Algorithm [3](https://arxiv.org/html/2510.26727v1#alg3 "Algorithm 3 ‣ 3.2.6 Interaction cycles ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law"). Periodically, the enforcement intensity EE of each cell is probabilistically updated based on the transaction frequency within that cell and its six adjacent cells during the preceding period—the greater the local transaction volume, the higher the likelihood that the enforcement intensity will be elevated. Based on the updated enforcement intensity, each seller recalculates its transaction cost ctc\_{t} at time tt and compares it with the previous transaction price pj,t−1p\_{j,t-1}, adopting the higher value as its new willingness to accept (WTA). Each buyer ii then initiates the offer process by selecting, from all unengaged sellers, the seller jj with the highest willingness to pay (WTPj​i​t\text{WTP}\_{jit}) and issuing an offer. Each seller, in turn, chooses from the received offers the buyer with the highest WTPi​j​t\text{WTP}\_{ijt} to enter negotiation. The transaction price pi​j​tp\_{ijt} is determined as a convex combination

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​j​t=sjzi+sj×WTPi​j​t+zizi+sj×WTAj​tp\_{ijt}=\frac{s\_{j}}{z\_{i}+s\_{j}}\times\text{WTP}\_{ijt}+\frac{z\_{i}}{z\_{i}+s\_{j}}\times\text{WTA}\_{jt} |  | (10) |

of the buyer’s and seller’s valuations, reflecting their relative bargaining power

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ=sjzi+sj, 1−λ=zizi+sj.\lambda=\frac{s\_{j}}{z\_{i}+s\_{j}},\ 1-\lambda=\frac{z\_{i}}{z\_{i}+s\_{j}}. |  | (11) |

If the negotiated price does not exceed the buyer’s remaining budget constraint mi​tm\_{it}, the transaction is executed.

Algorithm 3  Process of the multi-agent system

STEP\_MODEL(Buyer, Seller)

E←E∈{1,2,3}E\leftarrow E\in\{1,2,3\} if t=tE×k,k∈Zt=t\_{E}\times k,\ k\in\textbf{Z}

WTAj​t←max⁡{cj​t,pj,t−1}\text{WTA}\_{jt}\leftarrow\max\{c\_{jt},\ p\_{j,t-1}\} for j∈Sellerj\in\textbf{Seller}

[STEP\_BUYER(b, s)](https://arxiv.org/html/2510.26727v1#alg1 "Algorithm 1 ‣ 3.2.2 Agents: Buyers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law");

[STEP\_SELLER(b, s)](https://arxiv.org/html/2510.26727v1#alg2 "Algorithm 2 ‣ 3.2.3 Agents: Sellers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law") for b,s∈Buyer,Seller\textbf{b},\ \textbf{s}\in\textbf{Buyer},\ \textbf{Seller}

DATA\_COLLECT(tt)

t=t+1t=t+1

return

  

Note: Buyer and Seller denote the sets of buyer and seller agents in the model, respectively. The parameter tEt\_{E} represents the frequency with which enforcement intensity is recalculated. DATA\_COLLECT is a function used to record measurement indicators throughout the simulation process.

#### 3.2.7 Key performance indicators

We use trades, volume, buyer surplus, seller surplus, externality, and total welfare as the ABM’s key performance indicators because together they span the full efficiency–distribution–harm triad that law and economics evaluation requires. The number of trades captures the extensive margin—how often the market clears under a legal rule—while volume measures the intensive margin—how much is transacted conditional on clearing. Prices are endogenous in our model, so private benefits are best summarized as buyer surplus (WTP−p\text{WTP}-p) and seller surplus (p−WTAp-\text{WTA}), which decompose who captures the gains from trade and reveal rule-induced transfers. Because many legal interventions aim to manage spillovers, we track externality as the quantified harm to third parties not internalized by the contracting pair. Finally, total welfare aggregates these components (buyer ++ seller surplus −- externality), providing a Kaldor–Hicks benchmark for overall efficiency. This KPI set maps directly onto the model’s mechanisms—matching, bargaining, budgets, risk, and enforcement—and allows principled comparison of regimes that may raise throughput without raising welfare, or shift surplus without changing total output.

## 4 Calibration

### 4.1 LLM-based DCE calibration

#### 4.1.1 Data constraints

Calibrating an agent-based model of data transactions requires preference primitives that are empirically defensible and behaviorally interpretable. In our setting, these include WTP on buyer and WTA on seller side, along with how they shift with data scale xx, seller capability sjs\_{j}, and institutional conditions (R,E)(R,E). In mature product markets, such parameters can be disciplined by transaction microdata, field experiments, or regulatory disclosures. By contrast, data brokerage is structurally opaque. Transactions are bilateral and private, pricing is often bundled or NDA-constrained, and there is no public panel of prices/quantities or counterpart attributes at scale. As a result, there is no direct market evidence against which to anchor the key elasticities and interaction terms that drive welfare and policy counterfactuals in an ABM of the data economy.

Substitutes perform poorly. Hand-tuned parameters or “calibration by convenience” invite researcher degrees of freedom. Conclusions risk reflecting priors rather than behavior, weakening external validity and legal-policy relevance. Brute-force parameter sweeps are not a remedy. High-dimensional ABMs make exhaustive search computationally prohibitive, and a large share of the parameter space is economically nonsensical, which is far from plausible institutional or technological regimes. Moreover, assembling large human samples of relevant actors (e.g., hundreds of AI firms as buyers and hospitals/banks as sellers) for controlled experimentation is practically and ethically infeasible. This is because even expert elicitations seldom yield the volume or structure needed to identify interaction effects such as R×ER\times E.

Due to data constraints, we need to find a new method that is transparent (auditable prompts and seeds), reproducible (rerunnable instruments), and structurally informative (attributes mapped to interpretable primitives), without presupposing unavailable market data. This motivates our choice to precede simulation with a DCE conducted on a large language model (LLM) treated as a proxy subject. The DCE yields internally consistent choice data that discipline signs, elasticities, and interaction terms before those parameters are embedded in agents and propagated through the ABM.

#### 4.1.2 LLM model choice

A rapidly accumulating literature now shows that state-of-the-art LLMs are competent “silicon participant” in exactly the kinds of scenario and discrete-choice tasks we use. In psychology and management, a large replication study re-ran 156 published vignette experiments on three frontier LLMs and recovered 73–81% of main effects and 46–63% of interaction effects (with the well-noted caveat of effect-size inflation), demonstrating that randomized factorial manipulations are reliably reflected in LLM responses (Cui et al.,, [2025](https://arxiv.org/html/2510.26727v1#bib.bib12)). In political science, Argyle et al. establish “algorithmic fidelity,” showing that LLMs can be conditioned to emulate specific human subpopulations—enabling the heterogeneity analyses our persona-based WTA/WTP design requires (Argyle et al.,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib4)). In economics, Horton formalizes homo silicus and demonstrates that LLMs, given endowments and constraints, reproduce classic experimental regularities and can stand in as simulated subjects for ex-ante design and calibration (Horton,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib26)). In computational social science, Ziems et al. conclude that LLMs can augment experimental pipelines under clear prompting and evaluation protocols ([Ziems et al., 2024b,](https://arxiv.org/html/2510.26727v1#bib.bib70) ). Beyond replication, HCI and simulation work demonstrates that LLM-driven agents generate believable individual decisions and emergent social behavior in multi-agent environments, which aligns with our pipeline of calibrate via DCE, then simulate via ABM under legal-institutional treatments ([Park et al., 2023b,](https://arxiv.org/html/2510.26727v1#bib.bib40) ; Gao et al.,, [2024](https://arxiv.org/html/2510.26727v1#bib.bib18)).

We field the DCE on DeepSeek because recent peer-reviewed evaluations document frontier-level reasoning and competitive performance with proprietary models in tasks that are structurally analogous to social-science vignette and choice experiments. First, the DeepSeek-R1 program introduced a reinforcement-learning framework that materially improves multi-step reasoning—with evidence published in Nature—thereby supporting reliability on multi-attribute trade-offs central to discrete-choice designs (Guo et al.,, [2025](https://arxiv.org/html/2510.26727v1#bib.bib22)). Second, independent studies like decision-support evaluations show DeepSeek-V3 and R1 performing on par with, and in some settings better than, GPT-4o/Gemini on decision tasks. These prove that DeepSeek is an applied proxy for the type of structured judgment we elicit in WTA/WTP experiments (Sandmann et al.,, [2025](https://arxiv.org/html/2510.26727v1#bib.bib48); Zhang et al.,, [2025](https://arxiv.org/html/2510.26727v1#bib.bib68)).

We selected the DeepSeek as the primary instrument for the Discrete Choice Experiment due to a combination of its architectural design, demonstrated performance, and methodological transparency. The model’s core strength lies in its ”reasoning-first” orientation, which is a direct result of a reinforcement learning pipeline explicitly engineered to enhance multi-step logical inference for tasks in mathematics, coding, and structured problem-solving. This training encourages the model to generate explicit ”chain-of-thought” processes, effectively ”thinking aloud” as it works through a problem, which provides a transparent window into the decision-making calculus for our multi-attribute choice tasks. This inherent reasoning capability translates to highly competitive performance, with independent benchmarks showing DeepSeek performing on par with, and in some cases exceeding, leading proprietary models on complex decision-making tasks. Its proficiency in applied domains, such as clinical decision support where it must navigate multi-stage reasoning under constraints, serves as an informative proxy for its ability to handle the structured economic trade-offs in our experimental setting. Finally, from a legal-methodological standpoint, the availability of detailed technical reports and model checkpoints enhances the replicability of our study, allowing for independent verification and stress.

#### 4.1.3 Strengths

The LLM-enabled DCE offers a suite of methodological advantages that directly address the challenges of calibrating agent-based models in data-scarce environments, aligning with the evidentiary standards of law and economics. Foremost among these is its purpose-built replicability and auditability. The entire experimental protocol, including prompts, randomization seeds, and model parameters, is fixed ex ante and logged. This yields a complete calibration audit trail, allowing any researcher to re-field the survey and reproduce the estimated preference primitives. Such procedural transparency is rarely attainable with ad-hoc parameter tuning or opaque expert elicitation.

Furthermore, the experimental design provides strong identification and structural interpretability. Because attributes such as price, data scale xx, and the institutional environment (L,E)(L,E) are experimentally manipulated, the recovered parameters are directly interpretable in welfare-economic terms. The design isolates the specific effects of price sensitivity, capability gradients, scale effects (including diminishing-returns curvature), and legal-enforcement interactions—precisely the primitives the ABM requires to generate policy-relevant counterfactuals. This approach is also highly efficient and scalable. LLM respondents enable the rapid, large-NN collection of large, internally consistent datasets at a low cost, avoiding the recruitment and compliance frictions of large human panels. This allows for the estimation of full parameter distributions for heterogeneous agent types, a critical feature for realistic simulation.

From a diagnostic perspective, the methodology offers transparency for methodological scrutiny. The use of structured outputs and the elicitation of concise, free-text rationales for each choice permit a granular, post-hoc audit of the model’s decision logic. This “reasoning trace” strengthens the credibility of the calibration in legal and policy settings that demand explainability. The estimated primitives are also directly portable to the simulation, mapping one-to-one into agent decision rules and endowing the ABM with empirically-grounded, heterogeneous preferences. In an opaque market where observational microdata are unavailable, this approach provides a proportionate and documentable alternative to speculative parameterization. The net effect is a calibration method that replaces subjective priors with experimentally disciplined, reproducible primitives, thereby improving the credibility of downstream legal-economic counterfactuals.

### 4.2 Experimental design

This section details the stated-preference DCE we use to generate empirically disciplined primitives for calibrating the ABM of data transactions. The DCE treats a LLM as a proxy respondent under tightly controlled conditions. By systematically varying legally and economically salient attributes of hypothetical transactions, the design identifies the marginal effects needed to parameterize seller costs, buyer utilities, and their sensitivities to institutional environments.

The experimental design operationalizes the core economic and legal dimensions of a data transaction through a set of systematically varied attributes and levels. The fundamental terms of each transaction are defined by data scale (xj​tx\_{jt}), representing the volume of records, and price (PP). Data scale is treated as a continuous variable, drawn from a logarithmic grid to effectively probe for curvature in agent utility functions, and is varied independently of price to isolate pure quantity effects from monetary compensation. The price attribute is framed as either an offered payment to elicit sellers’ WTA or a posted price to elicit buyers’ WTP, with levels spanning a realistic range conditional on data scale to enable robust monotonicity checks. To account for market heterogeneity, we introduce seller capability (sjs\_{j}), a five-tier categorical measure reflecting a seller’s governance, data standardization, and delivery reliability (s1s\_{1} to s5s\_{5}). These tiers correspond to increasingly stringent operational practices and provide the necessary variation to estimate quality-related cost parameters and to stratify the agent population in the subsequent ABM. Central to the law-and-economics inquiry are the institutional attributes of Risk (RR) and Enforcement (EE). Risk is a three-level factor capturing the ex ante ambiguity of rules and potential for disputes, while enforcement is a three-level factor reflecting the ex post supervisory intensity and expected penalties. The design incorporates a full factorial 3×33\times 3 grid for these two attributes, ensuring complete coverage of the institutional interaction (R×ER\times E). This allows for the precise identification of the interaction’s effect on seller costs (δ\delta) and institutional shifts in buyer frictions (Φ\Phi), which are key parameters for simulating policy counterfactuals.

To instantiate ABM heterogeneity, we use persona conditioning: before any choice tasks, the LLM receives a concise role description. For example, “s3s\_{3} hospital data seller with enterprise-grade governance”, or “z4z\_{4} AI buyer with a large legacy dataset xix\_{i}”. Personas encode objectives and constraints (budget, service guarantees, regulatory posture) without revealing hypotheses. Buyer personas set baseline stocks xix\_{i} to recover the curvature of f​(xi)​(tested against​f​(xi)=e−ρ​xi)f(x\_{i})(\text{tested against}f(x\_{i})=e^{-\rho x\_{i}}). Seller personas fix sjs\_{j} to recover c1c\_{1} and institutional sensitivity.

To ensure the robustness of our findings and address known sensitivities of LLMs, we implemented a rigorous protocol for data collection. Each LLM instance completes a randomized sequence of choice sets. We employ both paraphrase randomization at the item level (varying the phrasing of vignettes) and order randomization across the choice sets to control for potential framing and order effects. For each choice, we also elicit a brief, free-text rationale (constrained to ≤20\leq 20 words) to create a “reasoning trace.” This trace provides a transparent, auditable record of the model’s decision logic, offering a diagnostic advantage over human-subject studies where reasoning is often a post-hoc rationalization.The entire experimental apparatus is designed for perfect reproducibility. All prompts, randomization seeds, model identifiers, and instruments are version-controlled. All outputs, including the discrete choices and textual rationales, are captured in a structured, machine-readable schema. This comprehensive protocol transforms the DCE into a fully auditable calibration trail, allowing any researcher to re-run the experiment on the same model release to independently reproduce the parameter estimates that form the foundation of our agent-based model.

### 4.3 Posterior estimation

#### 4.3.1 Specifications

Following Eq.([1](https://arxiv.org/html/2510.26727v1#S3.E1 "In 3.2.2 Agents: Buyers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law")), buyer ii’s utility for choices j∈{A,B,C}j\in\{A,\ B,\ C\} in round tt is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​j​t=ASCj⏟alt. constants+f​(xi​t)⋅β​xj⏟quantity return+τ​sj+γ​zi+ϕ​(sj×zi)⏟buyer and seller levels−αi​pi​t⏟price−κ​ln⁡(1+di​j)⏟distance+εi​j​t,\begin{split}U\_{ijt}&=\underbrace{\text{ASC}\_{j}}\_{\text{alt. constants}}+\underbrace{f(x\_{it})\cdot\beta x\_{j}}\_{\text{quantity return}}+\underbrace{\tau s\_{j}+\gamma z\_{i}+\phi(s\_{j}\times z\_{i})}\_{\text{buyer and seller levels}}\\ &-\underbrace{\alpha\_{i}p\_{it}}\_{\text{price}}-\underbrace{\kappa\ln(1+d\_{ij})}\_{\text{distance}}+\varepsilon\_{ijt},\end{split} |  | (12) |

with f​(xi​t)=exp⁡(−ρ​xi​t)f(x\_{it})=\exp(-\rho x\_{it}), εi​j​t∼i.i.d.EV1\varepsilon\_{ijt}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\text{EV}\_{1}. We take one common random coefficient on price pi​tp\_{it}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αi=softplus​(αiraw)=log⁡(1+eαiraw),\alpha\_{i}=\text{softplus}(\alpha\_{i}^{\text{raw}})=\log(1+e^{\alpha\_{i}^{\text{raw}}}), |  | (13) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | αiraw∼𝒩​(μα,σα2),\alpha\_{i}^{\text{raw}}\sim\mathcal{N}(\mu\_{\alpha},\sigma\_{\alpha}^{2}), |  | (14) |

and γ​zi\gamma z\_{i} loads only on choices AA or BB (outside option CC has 0). Set ASCC≡0\text{ASC}\_{C}\equiv 0. The multinomial logit (MNL) probability is given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡(yi​t=j|θ,αi)=eUi​j​t∑k∈{A,B,C}​eUi​k​t,\Pr(y\_{it}=j\ |\ \theta,\alpha\_{i})=\frac{e^{U\_{ijt}}}{\sum\_{k\in\{A,B,C\}e^{U\_{ikt}}}}, |  | (15) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ={ρ,β,τ,γ,ϕ,κ,γ,ASCA,ASCB}.\theta=\{\rho,\beta,\tau,\gamma,\phi,\kappa,\gamma,\text{ASC}\_{A},\text{ASC}\_{B}\}. |  | (16) |

Conditional on αi\alpha\_{i}, buyer ii’s likelihood over TiT\_{i} tasks is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒi​(θ,αi)=∏t=1TiPr⁡(yi​t|θ,αi).\mathcal{L}\_{i}(\theta,\alpha\_{i})=\prod\_{t=1}^{T\_{i}}\Pr(y\_{it}\ |\ \theta,\alpha\_{i}). |  | (17) |

Marginalizing the random coefficient yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒi​(θ,μα,σα)=∫ℒi​(θ,α)​p​(α|μα,σα)​𝑑α,\mathcal{L}\_{i}(\theta,\mu\_{\alpha},\sigma\_{\alpha})=\int\mathcal{L}\_{i}(\theta,\alpha)p(\alpha\ |\ \mu\_{\alpha},\sigma\_{\alpha})d\alpha, |  | (18) |

an nonlinear, highly non-Gaussian integral with no closed-form solutions.

Similarly, on the seller’s side, we let the latent accept utility of seller jj facing offer pi​j​tp\_{ijt} from buyer ii at time tt be

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​j​t=αj​pi​j​t⏟price−(c0+c1​sj+c2​xj+βR​Rj+βE​Ej​t+δ​Rj​Ej​t)⏟generalized cost+εi​j​t\begin{split}U\_{ijt}=\underbrace{\alpha\_{j}p\_{ijt}}\_{\text{price}}-\underbrace{(c\_{0}+c\_{1}s\_{j}+c\_{2}x\_{j}+\beta\_{R}R\_{j}+\beta\_{E}E\_{jt}+\delta R\_{j}E\_{jt})}\_{\text{generalized cost}}+\varepsilon\_{ijt}\end{split} |  | (19) |

following Eq. ([3](https://arxiv.org/html/2510.26727v1#S3.E3 "In 3.2.3 Agents: Sellers ‣ 3.2 The model ‣ 3 Empirical design ‣ Neither Consent nor Property: A Policy Lab for Data Law")), where εi​j​t∼i.i.d.EV1\varepsilon\_{ijt}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\text{EV}\_{1}. We normalize the utility of outside option “reject” to 0, therefore the acceptance probability is the logit

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡(Ai​j​t=1|αj,θ)=eUi​j​t1+eUi​j​t,θ={c0,c1,c2,βR,βE,δ},\Pr(A\_{ijt}=1\ |\ \alpha\_{j},\theta)=\frac{e^{U\_{ijt}}}{1+e^{U\_{ijt}}},\ \theta=\{c\_{0},c\_{1},c\_{2},\beta\_{R},\beta\_{E},\delta\}, |  | (20) |

with a random coefficient

|  |  |  |  |
| --- | --- | --- | --- |
|  | αj=softplus​(αjraw),αjraw∼𝒩​(μα,σα2).\alpha\_{j}=\text{softplus}(\alpha\_{j}^{\text{raw}}),\ \alpha\_{j}^{\text{raw}}\sim\mathcal{N}(\mu\_{\alpha},\sigma\_{\alpha}^{2}). |  | (21) |

Therefore, the marginal likelihood ℒi​(θ,μα,σα)\mathcal{L}\_{i}(\theta,\mu\_{\alpha},\sigma\_{\alpha}) has no closed form either.

#### 4.3.2 The Markov Chain Monte Carlo method

Since closed-form solutions do not exist for the likelihood integrals, we apply the Markov Chain Monte Carlo (MCMC) method to obtain a faithful joint posterior over the structural parameters and random effects. The estimated coefficients on buyer’s WTP and seller’s WTA are reported in Table [1](https://arxiv.org/html/2510.26727v1#S4.T1 "Table 1 ‣ 4.3.2 The Markov Chain Monte Carlo method ‣ 4.3 Posterior estimation ‣ 4 Calibration ‣ Neither Consent nor Property: A Policy Lab for Data Law") and Table [2](https://arxiv.org/html/2510.26727v1#S4.T2 "Table 2 ‣ 4.3.2 The Markov Chain Monte Carlo method ‣ 4.3 Posterior estimation ‣ 4 Calibration ‣ Neither Consent nor Property: A Policy Lab for Data Law"). On the buyer side, the 95% HDI for the coefficients ρ\rho, β\beta, τ\tau, and κ\kappa do not include zero or narrowly touching zero, suggesting positive directions of these coefficients, while the directions of γ\gamma and ϕ\phi are uncertain. On the seller side, the posterior distributions of c1c\_{1} and δ\delta include zero within their 95% HDI, indicating uncertainty about the direction of effects. Therefore, the buyer’s utility function effectively collapses to the simpler form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​j​tBuyer=e−ρ​xi​t​β​xj+τ​sj−αi​pi​j​t−κ​ln⁡(1+di​j),U^{\text{Buyer}}\_{ijt}=e^{-\rho x\_{it}}\beta x\_{j}+\tau s\_{j}-\alpha\_{i}p\_{ijt}-\kappa\ln(1+d\_{ij}), |  | (22) |

with estimated coefficients ρ^\hat{\rho}, β^\hat{\beta}, τ^\hat{\tau}, μ^α\hat{\mu}\_{\alpha}, σ^α\hat{\sigma}\_{\alpha}, and κ^\hat{\kappa}, while the seller’s utility function is practically indistinguishable from the model

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​j​tSeller=αj​pi​j​t−(c0+c2​xj+βR​Rj+βE​Ej​t),U^{\text{Seller}}\_{ijt}=\alpha\_{j}p\_{ijt}-(c\_{0}+c\_{2}x\_{j}+\beta\_{R}R\_{j}+\beta\_{E}E\_{jt}), |  | (23) |

with estimated coefficients c^0\hat{c}\_{0}, c^2\hat{c}\_{2}, β^R\hat{\beta}\_{R}, and β^E\hat{\beta}\_{E}.

Table 1: Calibration on buyer’s WTP

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Coefficient | Mean | 95% HDI | MCSEMean\text{MCSE}\_{\text{Mean}} | MCSESD\text{MCSE}\_{\text{SD}} | ESSBulk\text{ESS}\_{\text{Bulk}} | ESSTail\text{ESS}\_{\text{Tail}} | R^\hat{R} |
| ρ\rho | |  | | --- | | 0.0087 | | (0.0068) | | [0,0.0207] | 0.0001 | 0.0001 | 10743 | 6010 | 1.0005 |
| β\beta | |  | | --- | | 0.8093 | | (0.0329) | | [0.7463,0.8703] | 0.0003 | 0.0003 | 15028 | 9440 | 1 |
| τ\tau | |  | | --- | | 0.454 | | (0.0378) | | [0.3807,0.5234] | 0.0004 | 0.0003 | 8482 | 9443 | 1.0007 |
| γ\gamma | |  | | --- | | 0.0698 | | (0.0755) | | [-0.0736,0.2095] | 0.0008 | 0.0006 | 8081 | 9516 | 1.0008 |
| ϕ\phi | |  | | --- | | -0.0282 | | (0.0183) | | [-0.0628,0.0052] | 0.0002 | 0.0001 | 9051 | 9868 | 1.0006 |
| μα\mu\_{\alpha} | |  | | --- | | 0.6461 | | (0.0615) | | [0.5297,0.7595] | 0.0005 | 0.0005 | 15547 | 9762 | 1 |
| σα\sigma\_{\alpha} | |  | | --- | | 0.0204 | | (0.0153) | | [0,0.0485] | 0.0002 | 0.0001 | 7691 | 6167 | 0.9999 |
| κ\kappa | |  | | --- | | 1.2212 | | (0.0252) | | [1.1751,1.2702] | 0.0002 | 0.0002 | 18875 | 10182 | 1.0002 |

Note: The table reports posterior estimates obtained via Markov Chain Monte Carlo sampling. The discrete choice model was estimated using 4 parallel chains, with 3,000 tuning iterations followed by 3,000 posterior draws per chain (for a total of 12,000 retained samples). Standard deviations are in parentheses.




Table 2: Calibration on seller’s WTA

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Coefficient | Mean | 95% HDI | MCSEMean\text{MCSE}\_{\text{Mean}} | MCSESD\text{MCSE}\_{\text{SD}} | ESSBulk\text{ESS}\_{\text{Bulk}} | ESSTail\text{ESS}\_{\text{Tail}} | R^\hat{R} |
| c0c\_{0} | |  | | --- | | 4.883 | | (0.327) | | [4.255,5.536] | 0.004 | 0.002 | 8580 | 8656 | 1 |
| c1c\_{1} | |  | | --- | | 0.007 | | (0.02) | | [-0.033,0.045] | 0 | 0 | 23219 | 10280 | 1 |
| c2c\_{2} | |  | | --- | | 0.32 | | (0.033) | | [0.253,0.385] | 0 | 0 | 23219 | 10280 | 1 |
| βR\beta\_{R} | |  | | --- | | 0.708 | | (0.105) | | [0.498,0.911] | 0.001 | 0.001 | 9038 | 8950 | 1 |
| βE\beta\_{E} | |  | | --- | | 2.976 | | (0.17) | | [2.637,3.303] | 0.002 | 0.001 | 8851 | 9212 | 1 |
| δ\delta | |  | | --- | | -0.161 | | (0.083) | | [-0.325,0.003] | 0.001 | 0.001 | 8732 | 8750 | 1 |
| μα\mu\_{\alpha} | |  | | --- | | 0.727 | | (0.015) | | [0.697,0.754] | 0 | 0 | 21112 | 10019 | 1 |
| σα\sigma\_{\alpha} | |  | | --- | | 0.432 | | (0.012) | | [0.41,0.456] | 0 | 0 | 6118 | 8825 | 1 |

Note: The table reports posterior estimates obtained via Markov Chain Monte Carlo sampling. The discrete choice model was estimated using 4 parallel chains, with 3,000 tuning iterations followed by 3,000 posterior draws per chain (for a total of 12,000 retained samples). Standard deviations are in parentheses.

## 5 Validation

We validate our agent-based modeling of the data transaction market along the external validation against stylized facts, spatial-temporal regularities, and empirical macro-level evidence on the real-world data transactions.

Fig. [3](https://arxiv.org/html/2510.26727v1#S6.F3 "Fig. 3 ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") presents visual evidence on external validity. Three spatial patterns reproduced by our baseline model (to be discussed in detail in Subsection [6.1.1](https://arxiv.org/html/2510.26727v1#S6.SS1.SSS1 "6.1.1 Seller-centric liability (baseline rule) ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law")) align with well-documented regularities in China’s data and AI activity: (1) Coastal concentration—trade arcs cluster in the Yangtze River Delta (Shanghai-Hangzhou-Nanjing-Suzhou region), Pearl River Delta (Guangzhou-Shenzhen region), and Beijing-Tianjin corridor; (2) Distance decay—the share of intra-region trades exceeds inter-region trades; (3) Hub formation—cities with higher seeded levels accumulate higher flow (visible as hub-and-spoke bundles). A small set of coastal buyer cells acts as hubs that source nationally, drawing transactions from dispersed inland sellers. Visually, this appears as star-shaped bundles of arcs converging on a few coastal nodes. This pattern is consistent with a core-periphery demand structure: capital-intensive coastal markets aggregate demand, leaving smaller, peripheral buyers to transact locally or not at all. For temporal dynamics, the four snapshots of Fig. [3](https://arxiv.org/html/2510.26727v1#S6.F3 "Fig. 3 ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") reveal early exploration and later consolidation. By t=25t=25, there are many exploratory intra-region arcs; by t=t= 50–100, a set of inter-region arcs emerges. These trends are consistent with the market dynamics in geographical economics (Rauch,, [1999](https://arxiv.org/html/2510.26727v1#bib.bib46)).

Fig. [4](https://arxiv.org/html/2510.26727v1#S6.F4 "Fig. 4 ‣ 6.1.2 Institutional design: platform-mediated exchange ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") depicts another regime tested in our simulations—the platform-mediated exchange model (to be discussed in detail in Subsection [6.1.2](https://arxiv.org/html/2510.26727v1#S6.SS1.SSS2 "6.1.2 Institutional design: platform-mediated exchange ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law")). Although publicly available data on on-exchange transactions remain limited, a widely cited external estimate suggests that such transactions account for less than 4% of all data trades (Dai,, [2023](https://arxiv.org/html/2510.26727v1#bib.bib13)). This indicates that the effectiveness of the on-exchange regime is likely constrained, which is consistent with the visual similarity of trade arcs in Fig. [3](https://arxiv.org/html/2510.26727v1#S6.F3 "Fig. 3 ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") and Fig. [4](https://arxiv.org/html/2510.26727v1#S6.F4 "Fig. 4 ‣ 6.1.2 Institutional design: platform-mediated exchange ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law"). More importantly, in our simulations of the platform-mediated exchange model, the average share of on-exchange trading reached 3.58%, closely matching external estimates and thereby reinforcing the external validity of our model.

## 6 Results

Here we treat institutional design as a policy experiment in a simulated market. Agent-based computational economics provides a natural “digital policy laboratory” for this task: it models decentralized search, matching, bargaining, and compliance as they actually unfold among heterogeneous actors, and it lets us observe emergent market formation under alternative legal rules that would be analytically brittle in closed-form models. We follow the policy-analysis strand of the ABM literature in using the platform to run controlled counterfactuals, holding primitives fixed while switching the governing rule, so that differences in outcomes can be causally attributed to institutional design rather than to shocks or composition effects (Tesfatsion,, [2002](https://arxiv.org/html/2510.26727v1#bib.bib59), [2006](https://arxiv.org/html/2510.26727v1#bib.bib60); Arthur,, [2021](https://arxiv.org/html/2510.26727v1#bib.bib5)).

Our comparison spans the baseline seller-centric liability regime, a platform-mediated exchange (big data exchange), and five legal rules that reassign entitlement and liability in different ways. By holding agent preferences fixed while systematically altering the governing rules, we can causally attribute emergent differences in market outcomes: total welfare, trade volume, and match frequency to institutional design. Crucially, our welfare metric is adapted for information goods by explicitly deducting the externalized harms of data misuse, providing a more accurate measure of social value than laissez-faire price signals alone. This approach provides a transparent bridge from the doctrinal choices available to policymakers, framed in the Calabresi and Melamed, ([1972](https://arxiv.org/html/2510.26727v1#bib.bib10)) tradition, to their measurable market consequences, revealing which rules genuinely improve efficiency and which merely reassign costs without creating value. All the legal regimes to be compared are presented in Table [3](https://arxiv.org/html/2510.26727v1#S6.T3 "Table 3 ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law").

Methodologically, the chapter proceeds as a sequence of policy counterfactuals. For each rule, we simulate market dynamics to steady-state (or a long finite horizon), then compute welfare and participation metrics, comparing them to the baseline. ABM is suited to this because it accommodates heterogeneous beliefs about value and risk, networked matching, endogenous enforcement intensity, and feedback between governance and participation, features that standard equilibrium-first approaches often must suppress. The goal is pragmatic: to reveal where institutional re-design improves efficiency and robustness in data trade, and where it merely reassigns incidence without efficiency gains, providing a transparent bridge between doctrinal choices and measurable market consequences.

Table 3: Legal regimes to be compared

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Group I: Seller-borne liability | | Group II: Public / third-party externalization | | | Group III: Buyer-shared liability | |
| Rule | [Seller-centric liability](https://arxiv.org/html/2510.26727v1#S6.SS1.SSS1 "6.1.1 Seller-centric liability (baseline rule) ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") | [Platform-mediated exchange](https://arxiv.org/html/2510.26727v1#S6.SS1.SSS2 "6.1.2 Institutional design: platform-mediated exchange ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") | [Low-risk carve-out](https://arxiv.org/html/2510.26727v1#S6.SS2.SSS1 "6.2.1 Rule 1: Low-risk carve-out (exemption for 𝑅=1) ‣ 6.2 Group 𝐼⁢𝐼: Public / third-party externalization ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") | [Informed consent](https://arxiv.org/html/2510.26727v1#S6.SS2.SSS2 "6.2.2 Rule 2: Informed consent (data-subject property-rule gate) ‣ 6.2 Group 𝐼⁢𝐼: Public / third-party externalization ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") | [Risk immunity](https://arxiv.org/html/2510.26727v1#S6.SS2.SSS3 "6.2.3 Rule 3: Seller-entitlement property rule (risk immunity) ‣ 6.2 Group 𝐼⁢𝐼: Public / third-party externalization ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") | [Dividing risk liability](https://arxiv.org/html/2510.26727v1#S6.SS4.SSS1 "6.4.1 Rule 4: Buyer-shared risk (risk-only sharing) ‣ 6.4 Group 𝐼⁢𝐼⁢𝐼: Buyer-shared liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") | [Dividing all liability](https://arxiv.org/html/2510.26727v1#S6.SS4.SSS2 "6.4.2 Rule 5: Two-sided liability split (risk + enforcement) ‣ 6.4 Group 𝐼⁢𝐼⁢𝐼: Buyer-shared liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") |
| Feature | Seller bears 100% liability for Risk (R) & Enforcement (E). | Sellers bear 100% liability for R & E. Optional exchange exists; sellers join with probability. | Liability depends on data risk (R). Low-risk (R=1) sellers are exempt from R & E costs. | Sellers must get user consent for market access; consent exempts from R cost. | Sellers get blanket immunity from R liability; still bear E liability. | Liability for Risk (R) divided. Seller bears 100% of E liability. | Liability for both R and E divided. |
|  |  |  |  |  |  |  |  |
| Risk cost (RR) | Internalized by Seller. | Internalized by Seller | Externalized if R=1R=1; Internalized if R>1R>1. | Externalized if consent. | Fully externalized. | Divided between Buyer & Seller. | Divided between Buyer & Seller. |
|  |  |  |  |  |  |  |  |
| Enforcement cost (EE) | Internalized by Seller. | Internalized by Seller | Externalized if R=1R=1; Internalized if R>1R>1. | Internalized by Seller. | Internalized by Seller. | Internalized by Seller. | Divided between Buyer & Seller. |
|  |  |  |  |  |  |  |  |
| Seller WTA | WTAj​t\text{WTA}\_{jt} | 1.03∗WTAj​t1.03\*\text{WTA}\_{jt} | R=1R=1: (c0+c1​xj)/αi(c\_{0}+c\_{1}x\_{j})/\alpha\_{i} | WTAj​t−βR​R\text{WTA}\_{jt}-\beta\_{R}R | Risk removed. | Risk divided. | RR & EE divided. |
|  |  |  |  |  |  |  |  |
| Buyer WTP | WTPi​j​t\text{WTP}\_{ijt} | WTPi​j​t+κ​ln⁡(1+di​j)\text{WTP}\_{ijt}+\kappa\ln(1+d\_{ij}) | WTPi​j​t\text{WTP}\_{ijt} | WTPi​j​t\text{WTP}\_{ijt} | WTPi​j​t\text{WTP}\_{ijt} | WTPi​j​t\text{WTP}\_{ijt} −- s​h​a​r​e%×Rshare\%\times R | WTPi​j​t\text{WTP}\_{ijt} −- s​h​a​r​e%×(R+E)share\%\times(R+E) |
|  |  |  |  |  |  |  |  |
| Market access | All sellers. | All sellers. | All sellers. | Sellers with consent. | All sellers. | All sellers. | All sellers. |
|  |  |  |  |  |  |  |  |
| Externality | No. | No. | Yes, when R=1R=1. | Yes. | Yes. | No. | No. |
|  |  |  |  |  |  |  |  |
| Total welfare | CS + PS | CS + PS | CS + PS - Ext | CS + PS - Ext | CS + PS - Ext | CS + PS | CS + PS |

### 6.1 Group II: Seller-borne liability

This family of regimes assigns primary legal exposure to the data controller, typically the seller, who determines the purposes and means of processing. Consequently, liability for unlawful processing, security failings, and compensable harms is internalized e​x​a​n​t​eexante in the seller’s reservation price. This model mirrors the seller-centric architecture of major data protection laws. The GDPR, for instance, establishes a baseline where controllers face compensation claims and administrative fines, thereby making price the primary carrier of legal risk in decentralized bargaining. Within this framework, a platform or marketplace may lower search and coordination costs, but it does not absorb the incidence of liability. The seller remains the focal point of legal accountability and passes the expected cost of risk through to the price.

![Refer to caption](x3.png)


(a)

![Refer to caption](x4.png)


(b)

![Refer to caption](x5.png)


(c)

![Refer to caption](x6.png)


(d)

Fig. 3: Trade arcs between buyer and seller cells in the baseline market model

Note: Arcs connect the centroids of the buyer and seller hexagons for each realized deal in the simulation. Line width scales with the traded data volume xjx\_{j}; color denotes the price as configured. Only records with a “deal” status within the specified time filter are drawn.

#### 6.1.1 Seller-centric liability (baseline rule)

In our comparison, the baseline is a seller-centric (controller-centric) liability regime: the party that determines the purposes and means of processing and releases the dataset internalizes legal exposure for unlawful processing and downstream misuse. This is a classic liability-rule baseline. Date exchange is permitted, and violations are priced ex post through compensation and administrative sanctions that fall primarily on the controller. This maps closely to current doctrine and practice. Under GDPR, data subjects may claim compensation from a controller (or, in narrower cases, a processor) for material or non-material damage caused by an infringement (Art. 82). Recent CJEU rulings clarify that damages require proof of actual harm (not mere infringement), shaping the controller’s expected liability calculus. Supervisory authorities separately impose administrative fines (Arts. 83–84). Processors can also face public enforcement or contractual liability, but guidance emphasizes the controller’s primary responsibility for compliance and for appointing competent processors.

Enforcement practice in China is consistent with this incidence. The Didi case illustrates how large data holders can be sanctioned for privacy and security violations at scale: in 2022, the Cyberspace Administration of China announced a $1.2 billion penalty—widely noted as the largest to date—for unlawful personal-information handling and related violations, with analysis emphasizing that turnover-based penalty framework of China’s Personal Information Protection Law (PIPL) underpinned the outcome. This is a concrete instance of seller-side risk being internalized and priced through public enforcement. Forthcoming secondary rules (e.g., the Regulations on Network Data Security Management, effective 1 Jan 2025) further elaborate compliance obligations and enforcement tooling, tightening the environment in which controllers operate and thereby raising the expected-enforcement component that rational sellers pass through into price.

We implement this baseline by embedding legal risk in price. The seller’s reservation price (WTA) includes an intrinsic hazard term capturing expected private and compensatory costs from re-identification or misuse (our βR​R\beta\_{R}R), and an enforcement intensity term capturing detection probabilities and sanction severity (our βE​E\beta\_{E}E). Buyers do not model liability directly. They face it indirectly via price and contractual access constraints, so trade occurs only when private value exceeds a risk-loaded WTA.

Analytically, three features follow. First, decentralized bargaining governs matching and price formation—no platform or regulator pre-sets terms or bears incidence. Second, incidence is legally mediated. Changes in damage standards or enforcement pressure shift WTAs and participation through RR and EE. Third, under credible enforcement, liability is internalized, so there is no liability externality to subtract in welfare accounting: total welfare is the sum of producer and consumer surplus. This seller-centric benchmark provides the clean counterfactual against which our following institutional designs are evaluated.

#### 6.1.2 Institutional design: platform-mediated exchange

By a platform-mediated exchange we mean a trading venue that standardizes discovery, access, and governance for data products while leaving primary compliance and liability with the provider—a liability-preserving overlay on decentralized bargaining rather than a shift in legal incidence. Economically, the platform lowers search and coordination costs (catalogs, subscription rails, access controls, logging, and audit trails), increases verifiability (usage metering, provenance disclosure), and supplies rulebooks and screening that raise the expected quality of matches. However, the price still carries the provider’s legal risk, because the platform does not step into the shoes of a controller for the listing. This is how major commercial data marketplaces and public “data platform” frameworks operate in practice.

Contemporary data marketplace platforms are structured to function as conduits, consistently placing legal liability on the data providers rather than absorbing it themselves. Major platforms, from Snowflake and AWS Data Exchange to Databricks and Google’s Analytics Hub, contractually obligate data providers to be responsible for the legality and compliance of their data products. This market practice aligns with emerging regulatory frameworks like the EU’s Data Governance Act, which defines ”data intermediation services” as neutral facilitators designed to build trust, not to become liability sinks or data-exploiting principals. In effect, while these platforms provide sophisticated coordination and governance, they do not assume the provider’s underlying legal exposure.

A comparable architecture has emerged in China’s exchange-led data-elements market. The Shanghai Data Exchange is chartered as a quasi-public institution to provide infrastructure, conformity assessment, and supervisory tooling for data deals; its Security & Compliance Guidelines require trading parties to ensure transactions are controllable, risks preventable, responsibilities traceable, and compliance auditable, and empower the exchange to vet qualifications, review supplier compliance reports, disclose summaries to market participants, and conduct random audits across the transaction lifecycle. The municipal implementation rules similarly frame exchanges as rule-setting venues that record, review, and patrol transactions, while the substantive duties and sanctions that matter for expected liability continue to flow from the Data Security Law, Cybersecurity Law, and PIPL to the data handlers themselves. In other words, the exchange raises procedural assurance and reduces frictions but preserves provider-side incidence, matching how our model treats the platform: it modifies the “transaction technology” (e.g., reducing effective distance/search costs; adding small platform fees) without changing who internalizes risk.

Therefore, the primary effects of platform mediation are to improve market efficiency and governance while maintaining the existing liability structure. Platforms enhance matching efficiency and contractability by providing standard forms, identity management, and continuous auditing. They also induce greater observability and traceability of conduct, which can tighten expected enforcement even without a formal change in liability rules. Crucially, however, the incidence of liability remains with the providers and subscribers, a principle confirmed by both marketplace terms and neutrality-based intermediary statutes. In welfare terms, the platform’s value is derived from shrinking coordination costs and information asymmetries, not from offloading legal risk. Consequently, while prices still embed the seller’s risk and enforcement premia, the standardization of search, screening, and assurance at scale can materially shift market participation, transaction volumes, and the spatial patterns of trade.

![Refer to caption](x7.png)

Fig. 4: Trade arcs in platform-mediated exchange (t=100t=100)

Note: Arcs connect the centroids of the buyer and seller hexagons for each realized deal in the simulation. Line width scales with the traded data volume xjx\_{j}; color denotes the price as configured. Only records with a “deal” status within the specified time filter are drawn.

#### 6.1.3 Model comparisons

We estimate an average treatment effect of the platform-mediated exchange (PME) rule by regressing each outcome on a PME dummy indicator with random seed and time fixed effects,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ys​t=α+β⋅P​M​E+υs+ξt+εs​t,Y\_{st}=\alpha+\beta\cdot PME+\upsilon\_{s}+\xi\_{t}+\varepsilon\_{st}, |  | (24) |

interpreting β\beta as the within-seed, within-time change relative to the baseline rule. Table [4](https://arxiv.org/html/2510.26727v1#S6.T4 "Table 4 ‣ 6.1.3 Model comparisons ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") shows that PME’s coefficients are small and statistically indistinguishable from zero for all five metrics—number of trades, volume traded, buyer surplus, seller surplus, and total welfare. The 95% confidence intervals are tight around zero, implying that any systematic effect, if present, is economically modest. Fixed effects absorb seed heterogeneity and common time shocks, so the non-results are not an artifact of cross-sectional composition.

Table 4: Effect of the platform-mediated exchange

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | |  | | --- | | (1) | | Trades | | |  | | --- | | (2) | | Volume traded | | |  | | --- | | (3) | | Buyer surplus | | |  | | --- | | (4) | | Seller surplus | | |  | | --- | | (5) | | Total welfare | |
| Rule | | | | | |
| PME | |  | | --- | | 0.01 | | (0.014) | | |  | | --- | | 0.424 | | (0.522) | | |  | | --- | | 0.052 | | (0.076) | | |  | | --- | | 0.057 | | (0.085) | | |  | | --- | | 0.109 | | (0.161) | |
| Constant | |  | | --- | | 0.245\*\*\* | | (0.007) | | |  | | --- | | 7.776\*\*\* | | (0.261) | | |  | | --- | | 0.858\*\*\* | | (0.038) | | |  | | --- | | 0.929\*\*\* | | (0.042) | | |  | | --- | | 1.787\*\*\* | | (0.080) | |
| F−F-value | 0.53 | 0.66 | 0.46 | 0.46 | 0.46 |
| R2R^{2} | 0.213 | 0.181 | 0.135 | 0.136 | 0.136 |
| Observations | 6,000 | 6,000 | 6,000 | 6,000 | 6,000 |
| Time FE | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Seed FE | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |

Note: PME is a dummy variable for the platform-mediated exchange rule. The baseline rule is dropped as reference. Robust standard errors, clustered at seed level, are reported in parentheses. \*, \*\*, \*\*\* denote significance level 10%, 5%, and 1%.

The raincloud plots in Fig. [5](https://arxiv.org/html/2510.26727v1#S6.F5 "Fig. 5 ‣ 6.1.3 Model comparisons ‣ 6.1 Group 𝐼: Seller-borne liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") provide a distributional cross-check. Across panels (a)-(c), the half violins for the PME condition appear slightly right-shifted with fatter upper tails, but the boxplot notches—an approximate 95% interval for the median—substantially overlap with the baseline. Jittered points confirm that extreme realizations occur under both rules, with PME producing a few very high-volume or high-welfare runs but no robust median gain. Visually, therefore, the distributional evidence coheres with the regression results: PME does not lift central tendency, even if it occasionally enables large matches.

![Refer to caption](x8.png)

Fig. 5: Models with liability on sellers (t=100t=100)

Note: Each panel shows a raincloud for the two groups on the indicated metric. For each group, the half-violin (right side) depicts the kernel density (probability distribution) of observations; width is proportional to estimated density. The boxplot (centered, notched) overlays the median (line), interquartile range (box), and whiskers extending to 1.5×\timesIQR; notches provide an approximate 95% confidence interval for the median. Jittered points (left) display individual observations to show sample size and dispersion. Colors are consistent across panels to identify groups.

These findings suggest that, instituting a platform intermediary—holding risk and enforcement parameters constant—does not by itself expand the feasible contract set in a way that predictably increases trade counts or surplus. Put differently, information and matching services supplied by the platform do not relax the binding constraints that matter most for average outcomes. The platform seems to help a small set of pairs consummate large deals (upper-tail mass), but those episodic gains are offset elsewhere, leaving mean welfare unchanged.

### 6.2 Group I​III: Public / third-party externalization

This family of regimes seeks to expand data transactions by removing or relaxing a seller’s legal exposure when certain ex ante conditions are met. These conditions, such as a dataset qualifying as anonymous or the presence of valid informed consent, function as legal safe harbors that allow transactions to proceed without the price embedding the full expected cost of potential harm. In practice, the law creates bright-line distinctions for this purpose. For example, GDPR’s Recital 26 takes genuinely anonymized data outside the scope of data protection law, while U.S. health privacy law permits the use of de-identified data under HIPAA’s Safe Harbor provisions. Analytically, however, these designs shift a portion of the liability mass onto third parties or the public, as the contracting parties do not internalize the full harm term once these status or consent-based gates are satisfied.

#### 6.2.1 Rule 1: Low-risk carve-out (exemption for R=1R=1)

By a“low-risk carve-out” we mean a rule under which datasets that meet an ex-ante low-risk or anonymous status are treated as outside the data-protection/liability regime. In doctrinal terms this maps most closely to anonymization exemption: once information is no longer “about an identifiable person,” the core duties and compensation exposure do not apply. The European template is GDPR Recital 26, which states that the principles of data protection “do not apply to anonymous information,” i.e., data rendered such that the data subject is not or no longer identifiable. UK ICO guidance repeats the practical consequence, “once data is anonymised, it falls outside the scope of data protection law.” Health law provides an even more operationalized analogue. HIPAA recognizes two de-identification routes, one is Safe Harbor (removal of 18 specified identifiers) and the ohter is Expert Determination. After which the information is no longer Protected Health Information and may be used and disclosed without HIPAA’s restrictions (notwithstanding a residual, non-zero re-identification risk). U.S. general privacy law follows suit: CCPA/CPRA define and generally exempt “deidentified” data from consumer-rights obligations, subject to reasonableness standards for technical and organizational controls. China’s PIPL draws the same structural boundary. “Anonymization” is processing that makes identification impossible and irreversible. Once anonymized, the dataset is no longer personal information, and PIPL’s duties fall away.

For our following analysis, three characteristics are salient. First, the carve-out is a status decision made before bargaining, not a price adjustment within bargaining: legal risk turns discontinuously on whether the dataset qualifies as anonymous/low-risk under the applicable test (means “reasonably likely” to re-identify under GDPR; enumerated identifiers or expert attestation under HIPAA), and this status is what market participants contract around.

![Refer to caption](x9.png)

Fig. 6: Trade arcs in low-risk carve-out (t=100t=100)

Note: Arcs connect the centroids of the buyer and seller hexagons for each realized deal in the simulation. Line width scales with the traded data volume xjx\_{j}; color denotes the price as configured. Only records with a “deal” status within the specified time filter are drawn.

#### 6.2.2 Rule 2: Informed consent (data-subject property-rule gate)

By “informed consent” we mean the familiar rule that processing is lawful only if the right-holder—the data subject—grants ex ante permission that is freely given, specific, informed, and unambiguous. In doctrinal terms, consent is defined in GDPR Article 4(11) and elaborated by the European Data Protection Board. It must be a clear affirmative act and remains invalid where choice is coerced or bundled; supervisory practice further rejects pre-ticked boxes and stresses that imbalances of power (e.g., employer/employee, dominant platforms) can vitiate “freely given.” This consent-centric logic extends beyond Europe, appearing in various sectoral and state laws globally. The active agreement standard for cookie consent, for instance, was affirmed by the CJEU’s Planet49 judgment under the ePrivacy regime. In the United States, a fragmented state-law landscape is converging on a similar principle, increasingly requiring opt-in consent for “sensitive” data and specific uses like targeted advertising, even as regulators debate the validity of “consent-or-pay” models for other processing. Similarly, China’s PIPL establishes consent as a primary lawful basis and mandates separate, specific consent for processing sensitive information and for cross-border data transfers. Across these jurisdictions, enforcement bulletins consistently cite missing or defective consent as a core violation, underscoring a global trend toward requiring explicit and meaningful user agreement for data processing.

The character of consent is best understood as a property rule rather than a liability rule. It functions as an ex ante access gate that conditions whether a data transaction may occur at all, not as an ex post price term for adjusting damages. Where valid consent is absent, the transaction is legally impermissible. In practice, this gatekeeper function imposes non-trivial transaction costs on data controllers, including the operational burdens of obtaining, refreshing, and recording consent, as well as handling withdrawals and segmenting data by purpose. These costs selectively filter the set of economically viable trades and confer a competitive advantage to actors with robust consent management operations.

Our simulations implement this familiar consent rule in an explicitly institutional way. Reflecting its role as a legal gatekeeper under frameworks like GDPR and PIPL, only consent-cleared sellers are visible and tradable in the model. This implementation captures the practical treatment of consent as a device that clears rights for substantive risks but not for procedural oversight. We model this by reducing the seller’s objective-risk loading in the price while preserving their exposure to enforcement intensity. This approach yields clear comparative statics against a seller-centric baseline: consent constrains market access ex ante, lowers offered prices for compliant sellers, and alters welfare by potentially externalizing residual risk if the legal system treats consent-cleared trades as outside the scope of substantive liability. This model is consistent with the dual nature of consent in the real world. While consent is the canonical basis for processing, regulators actively police its validity and scope. The unlawfulness of cookie banners without active choice, the scrutiny of “consent-or-pay” models, and regulatory sanctions for defective consent all demonstrate that the gate is not absolute.

![Refer to caption](x10.png)

Fig. 7: Trade arcs in informed consent (t=100t=100)

Note: Arcs connect the centroids of the buyer and seller hexagons for each realized deal in the simulation. Line width scales with the traded data volume xjx\_{j}; color denotes the price as configured. Only records with a “deal” status within the specified time filter are drawn.

#### 6.2.3 Rule 3: Seller-entitlement property rule (risk immunity)

This regime conceptualizes the data seller’s position through the lens of a property rule, in the tradition of Calabresi and Melamed, ([1972](https://arxiv.org/html/2510.26727v1#bib.bib10)). The provider holds an entitlement not merely to transact but to do so while being immunized from ex post liability for substantive harms arising from the dataset’s inherent risk profile. This stands in contrast to a liability rule, under which the provider would remain exposed to court-assessed damages after a harm occurs. In our model, this property-rule protection is implemented by removing the objective risk premium from the seller’s WTA, while preserving their exposure to procedural and compliance costs. The economic trade-off is stark: immunizing sellers creates stronger ex ante supply incentives and lower transaction prices, but it does so by externalizing the potential for third-party harms, such as privacy loss or misuse, which must then be addressed by separate public regulation or insurance mechanisms.

This principle of provider-side immunization is not merely theoretical but finds practical application in diverse legal contexts, where policymakers have created liability shields to stimulate socially beneficial data flows. In the United States, for instance, the Cybersecurity Information Sharing Act of 2015 provides a clear statutory template by granting private entities liability protection when sharing cyber threat indicators, expressly to overcome the chilling effect of legal exposure. A broader analogue exists in open data regimes, such as the EU’s framework encouraging public-sector data release with minimal constraints. Here, liability is functionally shifted to downstream users through license disclaimers, shielding the original provider from risks associated with reuse and prioritizing access over provider liability. Across these varied examples, the underlying policy is consistent: a deliberate trade-off that reduces provider liability to unlock data supply, even in the face of uncertain externalities.

The distinctive feature of this provider-immunization regime, relative to our baseline liability rule, is the non-internalization of risk costs by the transacting parties. Prices fall because the objective risk premium is stripped from the seller’s WTA. Consequently, the burden of governing residual, third-party harms shifts from the contracting parties to public law and platform-level controls, such as procedural enforcement and post-hoc sanctions. The ultimate welfare effect therefore hinges on a critical trade-off: whether the production and value gains from increased data supply and reuse outweigh the costs of these externalized harms. Our simulations operationalize this “risk immunity” as a policy design lever, demonstrating that while it can increase match rates and realized value in high-uncertainty environments, its net benefit is contingent on the presence of strong complementary institutions—such as ex ante standards and exchange oversight—to curb negative spillovers.

![Refer to caption](x11.png)

Fig. 8: Trade arcs in risk immunity (t=100t=100)

Note: Arcs connect the centroids of the buyer and seller hexagons for each realized deal in the simulation. Line width scales with the traded data volume xjx\_{j}; color denotes the price as configured. Only records with a “deal” status within the specified time filter are drawn.

### 6.3 Model comparisons

We estimate the within-seed, within-time average treatment effect of each rule—informed consent (IC), low-risk carve-out (LRCO), and risk immunity (RI)—relative to the baseline by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ys​t=α+β1⋅I​C+β2⋅L​R​C​O+β3⋅R​I+υs+ξt+εs​t.Y\_{st}=\alpha+\beta\_{1}\cdot IC+\beta\_{2}\cdot LRCO+\beta\_{3}\cdot RI+\upsilon\_{s}+\xi\_{t}+\varepsilon\_{st}. |  | (25) |

Coefficients β\beta are therefore causal contrasts within the simulated economies, purged of time shocks and seed heterogeneity. One representative simulation run for each model is visualized in Fig. [6](https://arxiv.org/html/2510.26727v1#S6.F6 "Fig. 6 ‣ 6.2.1 Rule 1: Low-risk carve-out (exemption for 𝑅=1) ‣ 6.2 Group 𝐼⁢𝐼: Public / third-party externalization ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law"), [7](https://arxiv.org/html/2510.26727v1#S6.F7 "Fig. 7 ‣ 6.2.2 Rule 2: Informed consent (data-subject property-rule gate) ‣ 6.2 Group 𝐼⁢𝐼: Public / third-party externalization ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law"), and [8](https://arxiv.org/html/2510.26727v1#S6.F8 "Fig. 8 ‣ 6.2.3 Rule 3: Seller-entitlement property rule (risk immunity) ‣ 6.2 Group 𝐼⁢𝐼: Public / third-party externalization ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law"). The statistical results are shown in Table [5](https://arxiv.org/html/2510.26727v1#S6.T5 "Table 5 ‣ 6.3 Model comparisons ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law").

Table 5: Effects of third-party externalization rules

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | |  | | --- | | (1) | | Trades | | |  | | --- | | (2) | | Volume traded | | |  | | --- | | (3) | | Buyer surplus | | |  | | --- | | (4) | | Seller surplus | | |  | | --- | | (5) | | Externality | | |  | | --- | | (6) | | Total welfare | |
| Rule | | | | | | |
| IC | |  | | --- | | -0.145\*\*\* | | (0.012) | | |  | | --- | | -5.663\*\*\* | | (0.432) | | |  | | --- | | -0.606\*\*\* | | (0.061) | | |  | | --- | | -0.706\*\*\* | | (0.073) | | |  | | --- | | 0.205\*\*\* | | (0.013) | | |  | | --- | | -1.517\*\*\* | | (0.133) | |
| LRCO | |  | | --- | | 0.015 | | (0.014) | | |  | | --- | | 0.528 | | (0.601) | | |  | | --- | | 0.009 | | (0.074) | | |  | | --- | | 0.018 | | (0.097) | | |  | | --- | | 0.010\*\*\* | | (0.002) | | |  | | --- | | 0.016 | | (0.170) | |
| RI | |  | | --- | | 0.078\*\*\* | | (0.016) | | |  | | --- | | 2.290\*\*\* | | (0.613) | | |  | | --- | | 0.359\*\*\* | | (0.104) | | |  | | --- | | 0.407\*\*\* | | (0.128) | | |  | | --- | | 0.663\*\*\* | | (0.027) | | |  | | --- | | 0.103 | | (0.225) | |
| Constant | |  | | --- | | 0.245\*\*\* | | (0.009) | | |  | | --- | | 7.776\*\*\* | | (0.353) | | |  | | --- | | 0.858\*\*\* | | (0.052) | | |  | | --- | | 0.929\*\*\* | | (0.064) | | |  | | --- | | 0.000 | | – | | |  | | --- | | 1.787\*\*\* | | (0.115) | |
| F−F-value | 98.92 | 157.96 | 131.09 | 142.48 | 326.57 | 162.63 |
| R2R^{2} | 0.194 | 0.158 | 0.107 | 0.103 | 0.177 | 0.101 |
| Observations | 12,000 | 12,000 | 12,000 | 12,000 | 12,000 | 12,000 |
| Time FE | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Seed FE | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |

Note: IC, LRCO, and RI are dummy variables for the informed consent, low-risk carve-out, and risk immunity rule, respectively. The baseline rule is dropped as reference. Robust standard errors, clustered at seed level, are reported in parentheses. \*, \*\*, \*\*\* denote significance level 10%, 5%, and 1%.

The informed consent rule reduces market activity and welfare across the board. The average treatment effects on all of the six metrics are significantly negative. Fig. [9](https://arxiv.org/html/2510.26727v1#S6.F9 "Fig. 9 ‣ 6.3 Model comparisons ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") echoes this: the IC rainclouds are sharply left-shifted with compressed IQRs, indicating both lower central tendency and reduced dispersion. Economically, this stringent ex ante consent condition tightens the feasible-contract set, therefore lower both sides’ surplus.

For the low-risk carve-out rule, the coefficients are small and statistically indistinguishable from zero on all outcomes. The rainclouds sit close to baseline, with overlapping notches and similar tails. Substantively, targeting low-risk transactions for lighter treatment does not move the aggregate needle: most gains available at low risk were already realizable under baseline matching and budgets; any incremental matches are offset by selection and price adjustments elsewhere. From a regulatory design perspective, LRCO appears least distortive—it avoids IC’s output losses without generating much additional harm—but it also does not deliver systematic average gains.

The risk immunity rule produces broad-based increases on trades, volume, buyer surplus and seller surplus. Fig. [9](https://arxiv.org/html/2510.26727v1#S6.F9 "Fig. 9 ‣ 6.3 Model comparisons ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") shows clear right-shifts with fatter upper tails, especially for trades and volume. The same treatment also raises measured externalities, yielding statistically indistinguishable total welfare and indicating a classic scale-harm trade-off: removing liability frictions expands the contracting set and deepens matches, but at the cost of greater third-party exposure. In Calabresi and Melamed, ([1972](https://arxiv.org/html/2510.26727v1#bib.bib10)) terms, RI mimics a strong property-rule protection for sellers: it enlarges the size of the pie and the frequency of trades, while shifting part of the expected loss to parties outside the contract.

![Refer to caption](x12.png)

Fig. 9: Models with externality on third party (t=100t=100)

Note: Each panel shows a raincloud for the four groups on the indicated metric. For each group, the half-violin (right side) depicts the kernel density (probability distribution) of observations; width is proportional to estimated density. The boxplot (centered, notched) overlays the median (line), interquartile range (box), and whiskers extending to 1.5×\timesIQR; notches provide an approximate 95% confidence interval for the median. Jittered points (left) display individual observations to show sample size and dispersion. Colors are consistent across panels to identify groups.

### 6.4 Group I​I​IIII: Buyer-shared liability

In this final family of regimes, liability is no longer concentrated solely on the seller. Instead, the buyer is treated as a legally reachable actor who shares in the potential costs of data-related harms. This model directly reflects contemporary legal doctrine, where data processors under GDPR, joint controllers, and “Business Associate” under HIPAA all bear direct liability. Economically, this approach keeps the full liability mass inside the transaction, reassigning the incidence of risk toward the party best placed to mitigate it. This creates powerful incentives for buyers to invest in post-acquisition governance, as they now internalize a meaningful share of both the substantive risk of harm and the exposure to enforcement.

#### 6.4.1 Rule 4: Buyer-shared risk (risk-only sharing)

By “buyer-shared risk” we mean a regime in which the objective harm risk attached to a dataset (our RR component) is allocated across buyer and seller, while the seller continues to bear the enforcement-intensity channel (our EE component). Economically, the seller’s reservation price internalizes only its contracted share of RR (lowering WTA relative to the baseline), and the buyer discounts its willingness-to-pay by the remainder (lowering WTP), so the full expected harm remains inside the dyad rather than spilling onto third parties, only the incidence shifts. This structure has clear doctrinal and market analogues. Contract practice mirrors this legal architecture: contemporary data-processing agreements frequently include bespoke risk-sharing and indemnity baskets for privacy/security incidents—allocating who pays for notification, remediation, and third-party claims—so that harm risk is anticipated and priced ex ante by both sides.

This buyer-shared risk regime has three salient features for our analysis. Its primary distinction from carve-outs or immunities is the internalization of expected harm within the bargain by design. This ensures that welfare remains a function of consumer and producer surplus, while prices and market participation dynamically reallocate based on the negotiated split of risk. This internalization directly creates stronger incentive alignment on the demand side, as buyers who bear a portion of the risk have a direct economic reason to invest in downstream safeguards like access controls and data minimization. This regime is sustained by a crucial institutional complementarity between public and private law. Public law, such as the EU’s GDPR or the U.S. HIPAA, defines the minimum liability floor by making downstream actors legally reachable. Private law then builds upon this foundation, using instruments like data processing agreements and indemnities to set the precise economic split of that risk. Emerging regulations like the EU Data Act further reinforce this by policing unfair contractual terms and pushing parties toward allocations that place risk on the actor best positioned to mitigate it. In short, this model reflects the world increasingly seen in practice: regulators establish downstream liability, contracts divide the resulting costs, and prices transmit that allocation into market outcomes, all without offloading the risk of harm onto the public.

![Refer to caption](x13.png)

Fig. 10: Trade arcs in buyer-shared risk (t=100t=100)

Note: Arcs connect the centroids of the buyer and seller hexagons for each realized deal in the simulation. Line width scales with the traded data volume xjx\_{j}; color denotes the price as configured. Only records with a “deal” status within the specified time filter are drawn.

#### 6.4.2 Rule 5: Two-sided liability split (risk ++ enforcement)

This regime treats data exchange as a two-sided incidence problem: both the substantive harm risk attached to the dataset (our RR component) and the enforcement exposure driven by auditability, detectability, and sanction severity (our EE term) are allocated across buyer and seller and priced ex ante into both parties’ offers. Economically, the seller’s WTA embeds only its contracted shares of RR and EE, while the buyer discounts WTP by its complementary shares. The entire expected loss remains inside the dyad, but its incidence is no longer controller-only. This captures a legal architecture in which downstream acquirers are not mere “price takers,” but actors who can be reached by regulators and claimants—and therefore rationally invest in compliance and safeguards when they internalize part of RR and EE.Contemporary law and practice provide clear anchors for this two-sided liability allocation. Under the GDPR, for instance, data processors can be held directly liable for breaching their specific duties, and data subjects may seek compensation from either the controller or the processor under a joint and several liability framework (Art. 82). Regulators have confirmed this by fining processors in their own right, establishing that downstream parties bear public-law exposure, not just contractual risk. A parallel evolution occurred in US sectoral law, where HIPAA moved to impose direct liability on its “Business Associates,” creating a template where the data recipient shares both substantive and enforcement risk.

This joint liability regime has two features that are salient for our analysis. First, it improves incentive alignment on the demand side. Once buyers expect to bear a portion of both the harm risk (RR) and the enforcement exposure (EE), they have a direct economic motivation to invest in downstream controls—such as data minimization, access governance, and incident response—rather than free-riding on seller precautions. This aligns perfectly with established legal doctrines like joint-controller and processor liability, which have been validated by observed fines against downstream parties.Second, because the full liability mass remains internal to the bargain, the welfare accounting is confined to consumer and producer surplus without a third-party externality term. Instead of externalizing risk, this regime causes prices, matching, and participation levels to become sensitive to the negotiated split of liability and to each party’s comparative advantage in mitigating risk and enforcement costs. This model is both empirically plausible and normatively attractive, supported by policy instruments that constrain unfair allocations (e.g., the EU Data Act) and credible enforcement against both parties. In sum, our simulation operationalizes the world regulators have built, where buyers are reachable by claims and contracts then divide the costs. By varying this incidence parametrically, our model can reveal when shifting liability to the buyer creates value by unlocking superior mitigation, and when it merely reassigns cost without efficiency gains.

![Refer to caption](x14.png)

Fig. 11: Trade arcs in two-sided liability split (t=100t=100)

Note: Arcs connect the centroids of the buyer and seller hexagons for each realized deal in the simulation. Line width scales with the traded data volume xjx\_{j}; color denotes the price as configured. Only records with a “deal” status within the specified time filter are drawn.

#### 6.4.3 Model comparisons

We exploit within-seed and within-time variation in the buyer’s liability share, s​h​a​r​e∈[0,1]share\in[0,1] and estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ys​t=α+β⋅s​h​a​r​e+υs+ξt+εs​t.Y\_{st}=\alpha+\beta\cdot share+\upsilon\_{s}+\xi\_{t}+\varepsilon\_{st}. |  | (26) |

The two regimes discussed above are studied: (i) Buyer-shared risk (RR only) and (ii) Buyer-shared risk and enforcement (RR & EE). The coefficient β\beta identifies the average marginal effect of moving the buyer’s share from 0 to 1 on the outcome YY, holding seed and time factors constant. One representative simulation run for each model is visualized in Fig. [10](https://arxiv.org/html/2510.26727v1#S6.F10 "Fig. 10 ‣ 6.4.1 Rule 4: Buyer-shared risk (risk-only sharing) ‣ 6.4 Group 𝐼⁢𝐼⁢𝐼: Buyer-shared liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law"), and [11](https://arxiv.org/html/2510.26727v1#S6.F11 "Fig. 11 ‣ 6.4.2 Rule 5: Two-sided liability split (risk + enforcement) ‣ 6.4 Group 𝐼⁢𝐼⁢𝐼: Buyer-shared liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law").

According to Table [6](https://arxiv.org/html/2510.26727v1#S6.T6 "Table 6 ‣ 6.4.3 Model comparisons ‣ 6.4 Group 𝐼⁢𝐼⁢𝐼: Buyer-shared liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law"), both regimes show statistically positive throughput elasticities, but the effect is stronger when buyers also share enforcement. A full shift of share from 0→10\rightarrow 1 under the risk-only regime raises trades by 0.021 (p<0.05p<0.05) and volume traded by 1.060 (p<0.01p<0.01). Under the RR & EE rule, the corresponding effects are 0.070 (p<0.01p<0.01) and 1.629 (p<0.01p<0.01). The fitted lines in Fig. [12](https://arxiv.org/html/2510.26727v1#S6.F12 "Fig. 12 ‣ 6.4.3 Model comparisons ‣ 6.4 Group 𝐼⁢𝐼⁢𝐼: Buyer-shared liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") reproduce these slopes with tight 95% bands through regressions without fixed effect and cluster-robust standard errors, visually confirming a monotone increase. Economically, asking buyers to internnalize a larger slice of downside (and, under RR & EE, enforcement frictions as well) screens in higher-type buyers and reassures sellers, reducing bargaining failure and expanding the feasible-contract set.

Table 6: Effects of buyer-side liability splits

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Buyer-shared risk | | | | | Buyer-shared risk and enforcement | | | | |
|  | |  | | --- | | (1) | | Trades | | |  | | --- | | (2) | | Volume traded | | |  | | --- | | (3) | | Buyer surplus | | |  | | --- | | (4) | | Seller surplus | | |  | | --- | | (5) | | Total welfare | | |  | | --- | | (6) | | Trades | | |  | | --- | | (7) | | Volume traded | | |  | | --- | | (8) | | Buyer surplus | | |  | | --- | | (9) | | Seller surplus | | |  | | --- | | (10) | | Total welfare | |
| Share | |  | | --- | | 0.021\*\* | | (0.009) | | |  | | --- | | 1.060\*\* | | (0.440) | | |  | | --- | | 0.128\* | | (0.069) | | |  | | --- | | 0.177\*\* | | (0.082) | | |  | | --- | | 0.305\* | | (0.150) | | |  | | --- | | 0.070\*\*\* | | (0.011) | | |  | | --- | | 1.629\*\*\* | | (0.387) | | |  | | --- | | 0.035 | | (0.065) | | |  | | --- | | 0.078 | | (0.080) | | |  | | --- | | 0.113 | | (0.145) | |
| Constant | |  | | --- | | 0.242\*\*\* | | (0.004) | | |  | | --- | | 8.086\*\*\* | | (0.220) | | |  | | --- | | 0.922\*\*\* | | (0.035) | | |  | | --- | | 0.998\*\*\* | | (0.041) | | |  | | --- | | 1.920\*\*\* | | (0.075) | | |  | | --- | | 0.246\*\*\* | | (0.006) | | |  | | --- | | 8.245\*\*\* | | (0.194) | | |  | | --- | | 0.948\*\*\* | | (0.033) | | |  | | --- | | 1.040\*\*\* | | (0.040) | | |  | | --- | | 1.988\*\*\* | | (0.072) | |
| F−F-value | 5.60 | 5.80 | 3.46 | 4.70 | 4.13 | 38.49 | 17.69 | 0.29 | 0.95 | 0.61 |
| R2R^{2} | 0.211 | 0.163 | 0.134 | 0.131 | 0.133 | 0.213 | 0.166 | 0.136 | 0.133 | 0.135 |
| Observations | 33,000 | 33,000 | 33,000 | 33,000 | 33,000 | 33,000 | 33,000 | 33,000 | 33,000 | 33,000 |
| Time FE | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Seed FE | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |

Note: Share is a continuous variable representing the buyer’s share of liability. In the baseline model, share is set to be 0. Robust standard errors, clustered at seed level, are reported in parentheses. \*, \*\*, \*\*\* denote significance level 10%, 5%, and 1%.



![Refer to caption](x15.png)

Fig. 12: Effects of buyer-side liability splits on throughput indicators

Note: Each panel plots binned scatter points of the indicated metric against the mid-bin center of buyer liability share. In both panels, the fitted lines and shaded 95% OLS confidence intervals are estimated on the full sample using buyer’s liability share as the regressor and the corresponding outcome. Colors denote policy regimes and are consistent across panels.

For surplus distribution, the two rules exhibit heterogeneity on treatment effects. Under the risk-only rule, s​h​a​r​eshare is associated with higher private surplus: a 0.128 (p<0.10p<0.10) increase on buyer surplus and a 0.177 (p<0.05p<0.05) increase on seller surplus. Once enforcement is also shifted to buyers (the RR & EE rule), these surplus gains attenuate and lose significance. A natural interpretation is that while greater buyer skin-in-the-game induces more trades, cost pass-through and price adjustment transfer part of the gains, leaving neither side’s per-trade surplus systematically higher. In other words, enforcement sharing acts like a tax on the matched pair that is offset by increased match frequency rather than larger rents.

![Refer to caption](x16.png)

Fig. 13: Effects of buyer-side liability splits on welfare

Note: The figure plots binned scatter points of total welfare against the mid-bin center of buyer liability share. The fitted lines and shaded 95% OLS confidence intervals are estimated on the full sample using buyer’s liability share as the regressor and total welfare as outcome. Colors denote policy regimes and are consistent across panels.

The total welfare regression mirrors this tradeoff. The risk-only rule yields a positive welfare slope of 0.305 (p∼0.05p\sim 0.05), consistent with more matches and modest surplus increases on both sides. Under the RR & EE rule, however, the welfare slope drops to be indistinguishable from zero. Fig. [13](https://arxiv.org/html/2510.26727v1#S6.F13 "Fig. 13 ‣ 6.4.3 Model comparisons ‣ 6.4 Group 𝐼⁢𝐼⁢𝐼: Buyer-shared liability ‣ 6 Results ‣ Neither Consent nor Property: A Policy Lab for Data Law") shows the same pattern: both fitted lines slope upward, but the blue (risk-only) line is steeper, whereas the lavender (RR & EE) line is flatter with a wide confidence interval. Thus, shifting risk to buyers tends to scale the pie, but layering enforcement burdens on buyers converts some of those gains into compliance costs, leaving average welfare statistically unchanged.

At the same time, magnitudes are economically meaningful at realistic movements in s​h​a​r​eshare. A move from 0 to 0.5 increases expected trades by ≈0.01\approx 0.01 (risk-only) and ≈0.035\approx 0.035 (RR & EE) per period; and volume by ≈0.53\approx 0.53 and ≈0.81\approx 0.81 per period, respectively—consistent with the visual “upward tilt” of binned points. The results imply that allocating some risk to buyers (without imposing enforcement costs) is Pareto-leaning in expectation: more trades, higher volume, and weakly higher total welfare. However, adding enforcement sharing further boosts throughput, but not welfare on average—suggesting that the extra compliance burden largely relabels gains rather than creating new surplus. Converting the throughput dividend into welfare would require complementary measures.

Therefore, increasing buyers’ liability share is shown to be an effective quantity lever—especially when coupled with enforcement—but only the risk-sharing (risk-only) version translates into statistically detectable welfare gains. The risk-and-enforcement version appears to reallocate rather than expand surplus: it brings more matches to fruition, yet leaves mean buyer, seller, and total surplus statistically flat once compliance costs are internalized.

## 7 Conclusion

Our results are best understood as a “Neptune moment” for legal empiricism. In 1846, Le Verrier’s calculations told observers where to point their telescopes. In our case, the “darkness” of fieldwork first hinted at an anomaly: sophisticated buyers quietly assuming downstream risk, a private ordering the literature had ignored. But it was the ABM that “pointed the telescope,” moving this practice from a mere curiosity to a public-welfare solution. Our model provided the calculations, demonstrating why this buyer-heavy design is welfare-maximizing in a market defined by uncertainty.

The analogy is not that theory replaces evidence, but that a disciplined model illuminates what evidence to trust. A closer parallel is the Giffen good: a theoretical curiosity for decades, it required a specific, controlled experiment to finally prove its existence in the real world. Our ABM functions as that precise experiment. It isolates the variable of institutional design and confirms what standard priors had obscured. The broader lesson is epistemic, and profound: Practice does not merely implement theory, it often prefigures it.

Our simulation, therefore, does not invent a new rule. It provides the missing doctrinal foundation for a rule that practitioners and advanced legal frameworks are already converging upon. The “least-cost avoider” logic we observed in our fieldwork is the same logic driving direct liability for processors under the GDPR and for business associates under HIPAA. Our contribution, then, is to unify these threads. We provide the first behaviorally-grounded, comparative evidence that these “two-sided reachability” moves are not merely equitable. They are, in a market defined by risk, the efficient path forward.

This paper, in the end, offers another new answer to a fundamental challenge: What is the role of social scientists in the age of AI? We refuse to wait passively for computer scientists to define our field. Instead, we demonstrate how to actively adopt and integrate these new tools to forge a complete, novel empirical paradigm. For too long, AI’s role in social science has been confined to two paths: knowledge synthesis or data processing. Our work charts a clear “third path”: using AI, specifically LLMs, as the core engine for computational simulation and empirical inquiry itself.

This methodological breakthrough is twofold. First, it overcomes the field’s traditional limitations: data scarcity, resource constraints, and the inability to access elite populations. Second, it builds a complete “field-to-verification” pipeline. Without fieldwork, we would not know what variables mattered for our utility function. Without the LLM-DCE, we could not quantify it. And without the ABM, we could never have verified this practice-born theory in the light. Our research is far from perfect, but it has, at least, lit a candle. Our work is not the destination, but we hope it is a path cleared in the wilderness. For a field in transformation, its value may lie not in having arrived, but in proving that a way forward does, indeed, exist.

## Acknowledgements

The authors express their sincere gratitude to Yifan Zhong, Haojun Li, Zhaowei Zhang, and Yuchuan Tian for their generous support in providing computing resources.

## References

* Abar et al., (2017)

  Abar, S., Theodoropoulos, G. K., Lemarinier, P., and O’Hare, G. M. (2017).
  Agent based modelling and simulation tools: A review of the state-of-art software.
  Computer Science Review, 24:13–33.
* Acquisti et al., (2015)

  Acquisti, A., Brandimarte, L., and Loewenstein, G. (2015).
  Privacy and human behavior in the age of information.
  Science, 347(6221):509–514.
* Allenby and Rossi, (1998)

  Allenby, G. M. and Rossi, P. E. (1998).
  Marketing models of consumer heterogeneity.
  Journal of Econometrics, 89(1–2):57–78.
* Argyle et al., (2023)

  Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., and Wingate, D. (2023).
  Out of one, many: Using language models to simulate human samples.
  Political Analysis, 31(3):337–351.
* Arthur, (2021)

  Arthur, W. B. (2021).
  Foundations of complexity economics.
  Nature Reviews Physics, 3(2):136–145.
* Audretsch and Feldman, (1996)

  Audretsch, D. B. and Feldman, M. P. (1996).
  R&d spillovers and the geography of innovation and production.
  American Economic Review, 86(3):630–640.
* Benguria, (2021)

  Benguria, F. (2021).
  The matching and sorting of exporting and importing firms: Theory and evidence.
  Journal of International Economics, 131:103459.
  Develops GE model with heterogeneous exporters/importers and matched data; documents sorting patterns consistent with complementarities.
* Berry et al., (1995)

  Berry, S., Levinsohn, J., and Pakes, A. (1995).
  Automobile prices in market equilibrium.
  Econometrica, 63(4):841–890.
* Cabral and Hortacsu, (2010)

  Cabral, L. and Hortacsu, A. (2010).
  The dynamics of seller reputation: Evidence from ebay.
  The journal of industrial economics, 58(1):54–78.
* Calabresi and Melamed, (1972)

  Calabresi, G. and Melamed, A. D. (1972).
  Property rules, liability rules, and inalienability: one view of the cathedral.
  In Modern Understandings of Liberty and Property, pages 139–178. Routledge.
* Citron and Solove, (2022)

  Citron, D. K. and Solove, D. J. (2022).
  Privacy harms.
  BUL Rev., 102:793.
* Cui et al., (2025)

  Cui, Z., Li, N., and Zhou, H. (2025).
  A large-scale replication of scenario-based experiments in psychology and management using large language models.
  Nature Computational Science, 5:627–634.
* Dai, (2023)

  Dai, X. (2023).
  Safe harbor rules as legal technology: Principles and prospects.
  The Jurist, (02):31–46+192.
* Duvvuri et al., (2007)

  Duvvuri, S., Ansari, A., and Gupta, S. (2007).
  Consumers’ price sensitivities across complementary categories.
  Management Science, 53(12):1933–1945.
* Einav et al., (2016)

  Einav, L., Farronato, C., and Levin, J. (2016).
  Peer-to-peer markets.
  Annual Review of Economics, 8(1):615–635.
* Eisenberg, (2010)

  Eisenberg, T. (2010).
  The origins, nature, and promise of empirical legal studies and a response to concerns.
* Fernández-Villaverde et al., (2023)

  Fernández-Villaverde, J., Koyama, M., Lin, Y., and Sng, T.-H. (2023).
  The fractured-land hypothesis\*.
  The Quarterly Journal of Economics, 138(2):1173–1231.
* Gao et al., (2024)

  Gao, C., Lan, X., Li, N., et al. (2024).
  Large language models empowered agent-based modeling and simulation: a survey and perspectives.
  Humanities and Social Sciences Communications, 11:1259.
* Gefen et al., (2019)

  Gefen, G., Ben-Porat, O., Tennenholtz, M., and Yom-Tov, E. (2019).
  Privacy, altruism, and experience: Estimating the perceived value of internet data for medical uses.
  arXiv preprint arXiv:1906.08562.
  Participants demanded higher compensation when data were linked to more severe/riskiest conditions.
* Goldsmith and Vermeule, (2002)

  Goldsmith, J. and Vermeule, A. (2002).
  Empirical methodology and legal scholarship.
  The University of Chicago Law Review, 69(1):153–167.
* Groeneveld et al., (2017)

  Groeneveld, J., Müller, B., Buchmann, C. M., Dressler, G., Guo, C., Hase, N., Hoffmann, F., John, F., Klassert, C., Lauf, T., et al. (2017).
  Theoretical foundations of human decision-making in agent-based land use models–a review.
  Environmental modelling & software, 87:39–48.
* Guo et al., (2025)

  Guo, D., Yang, D., Zhang, H., et al. (2025).
  Deepseek-r1 incentivizes reasoning in llms through reinforcement learning.
  Nature, 645:633–638.
* He, (2024)

  He, A. (2024).
  Data marketplaces and governance: Lessons from china.
  Centre for International Governance Innovation (CIGI) Online.
* Hestness et al., (2017)

  Hestness, J., Narang, S., Ardalani, N., Diamos, G., Jun, H., Kianinejad, H., Patwary, M. M. A., Yang, Y., and Zhou, Y. (2017).
  Deep learning scaling is predictable, empirically.
  arXiv preprint arXiv:1712.00409.
* Hoffmann et al., (2022)

  Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., de Las Casas, D., Hendricks, L. A., Welbl, J., Clark, A., et al. (2022).
  Training compute-optimal large language models.
  In Advances in Neural Information Processing Systems (NeurIPS).
* Horton, (2023)

  Horton, J. J. (2023).
  Large language models as simulated economic agents: What can we learn from homo silicus?
  Technical report, National Bureau of Economic Research.
* Hu, (2024)

  Hu, L. (2024).
  Dynamics in Chinese Digital Commons: Law, Technology, and Governance.
  Routledge.
* Jenks, (1963)

  Jenks, G. F. (1963).
  Generalization in statistical mapping.
  Annals of the Association of American Geographers, 53(1):15–26.
* Jones and Tonetti, (2020)

  Jones, C. I. and Tonetti, C. (2020).
  Nonrivalry and the economics of data.
  American Economic Review, 110(9):2819–2858.
* Kaplan et al., (2020)

  Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., and Amodei, D. (2020).
  Scaling laws for neural language models.
  arXiv preprint arXiv:2001.08361.
* (31)

  Li, L., Tadelis, S., and Zhou, X. (2020a).
  Buying reputation as a signal of quality: Evidence from an online marketplace.
  The RAND Journal of Economics, 51(4):965–988.
* (32)

  Li, X., Lin, Z., Wu, X., and Zhang, J. (2020b).
  Valuing personal data with privacy consideration.
  Information Systems Frontiers, 22(5):1203–1216.
  Formalizes valuation with privacy risk; higher risk implies higher reservation prices.
* Marchetti, (1994)

  Marchetti, C. (1994).
  Anthropological invariants in travel behavior.
  Technological Forecasting and Social Change, 47(1):75–88.
* McFadden, (1972)

  McFadden, D. (1972).
  Conditional logit analysis of qualitative choice behavior.
* Meier et al., (2024)

  Meier, Y., Krause, A., and Haas, A. (2024).
  The privacy calculus revisited: An empirical investigation of risk and benefit tradeoffs.
  Communication Research, 51(4):1046–1071.
  Meta-evidence that perceived risk reduces disclosure; consistent with higher WTA under higher risk.
* MIT Sloan Ideas, (2024)

  MIT Sloan Ideas (2024).
  GDPR reduced firms’ data and computation use.
  MIT Sloan Ideas Made to Matter.
  Reports firm-level declines in data storage and computation after GDPR.
* Narayanan and Shmatikov, (2008)

  Narayanan, A. and Shmatikov, V. (2008).
  Robust de-anonymization of large sparse datasets.
  In 2008 IEEE Symposium on Security and Privacy (sp 2008), pages 111–125. IEEE.
* Ohm, (2010)

  Ohm, P. (2010).
  Broken promises of privacy: Responding to the surprising failure of anonymization.
  UCLA Law Review, 57:1701–1777.
* (39)

  Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023a).
  Generative agents: Interactive simulacra of human behavior.
  In Proceedings of the 36th annual acm symposium on user interface software and technology, pages 1–22.
* (40)

  Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023b).
  Generative agents: Interactive simulacra of human behavior.
  In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology, UIST ’23, New York, NY, USA. Association for Computing Machinery.
* Petersen and Rajan, (2002)

  Petersen, M. A. and Rajan, R. G. (2002).
  Does distance still matter? the information revolution in small business lending.
  The Journal of Finance, 57(6):2533–2570.
* Porter, (1998)

  Porter, M. E. (1998).
  Clusters and the new economics of competition.
  Harvard Business Review, 76(6):77–90.
* Radauer, (2023)

  Radauer, A. (2023).
  The possibilities and limits of trade secrets to protect data in agri-food value chains.
  Journal of Business Economics, 93(3):297–330.
  Analyzes risks and governance costs of sharing proprietary datasets; highlights trade-secret leakage risks.
* Railsback and Grimm, (2019)

  Railsback, S. F. and Grimm, V. (2019).
  Agent-based and individual-based modeling: a practical introduction.
  Princeton university press.
* Rathje et al., (2024)

  Rathje, S., Mirea, D.-M., Sucholutsky, I., Marjieh, R., Robertson, C. E., and Van Bavel, J. J. (2024).
  Gpt is an effective tool for multilingual psychological text analysis.
  Proceedings of the National Academy of Sciences, 121(34):e2308950121.
* Rauch, (1999)

  Rauch, J. E. (1999).
  Networks versus markets in international trade.
  Journal of International Economics, 48(1):7–35.
* Rocher et al., (2019)

  Rocher, L., Hendrickx, J. M., and De Montjoye, Y.-A. (2019).
  Estimating the success of re-identifications in incomplete datasets using generative models.
  Nature communications, 10(1):3069.
* Sandmann et al., (2025)

  Sandmann, S., Heggselmann, S., Pujarski, M., et al. (2025).
  Benchmark evaluation of deepseek large language models in clinical decision-making.
  Nature Medicine, 31:2546–2549.
* Sen et al., (2025)

  Sen, R., Dubey, A., Mukhopadhyay, A., Samaranayake, S., and Laszka, A. (2025).
  Moveod: Synthesizing origin-destination commute distribution from u.s. census data.
* Simpson et al., (2021)

  Simpson, E., Larbey, M., Regan, T., et al. (2021).
  Understanding the barriers and facilitators to sharing patient-generated health data: A scoping review.
  Journal of the American Medical Informatics Association, 28(11):2436–2450.
  Trust, privacy, and security concerns are recurrent barriers to data sharing.
* Skatova et al., (2023)

  Skatova, A. et al. (2023).
  Unpacking privacy: Valuation of personal data protection.
  PLOS ONE, 18(5):e0285075.
  Shows widespread willingness to pay to avoid sharing; implies higher compensation demanded as perceived risk rises.
* Solove, (2013)

  Solove, D. J. (2013).
  Introduction: Privacy self-management and the consent dilemma.
  Harvard law review, 126(7):1880–1903.
* Sorenson and Stuart, (2001)

  Sorenson, O. and Stuart, T. E. (2001).
  Syndication networks and the spatial distribution of venture capital investments.
  American Journal of Sociology, 106(6):1546–1588.
* Sugita et al., (2023)

  Sugita, Y., Teshima, K., and Seira, E. (2023).
  Assortative matching of exporters and importers.
  The Review of Economics and Statistics, 105(6):1544–1561.
  Shows Beckerian positive assortative matching between exporters and importers using Mexico–U.S. apparel trade during liberalization.
* Sweeney, (2000)

  Sweeney, L. (2000).
  Simple demographics often identify people uniquely.
  Health (San Francisco), 671(2000):1–34.
* Sweeney, (2001)

  Sweeney, L. (2001).
  Information explosion.
  Confidentiality, disclosure, and data access: Theory and practical applications for statistical agencies, pages 43–74.
* Sweeney, (2002)

  Sweeney, L. (2002).
  k-anonymity: A model for protecting privacy.
  International journal of uncertainty, fuzziness and knowledge-based systems, 10(05):557–570.
* Tadelis, (2016)

  Tadelis, S. (2016).
  Reputation and feedback systems in online platform markets.
  Annual review of economics, 8(1):321–340.
* Tesfatsion, (2002)

  Tesfatsion, L. (2002).
  Agent-based computational economics: Growing economies from the bottom up.
  Artificial life, 8(1):55–82.
* Tesfatsion, (2006)

  Tesfatsion, L. (2006).
  Agent-based computational economics: A constructive approach to economic theory.
  Handbook of computational economics, 2:831–880.
* Train, (2009)

  Train, K. E. (2009).
  Discrete choice methods with simulation.
  Cambridge university press.
* Uzzi, (1996)

  Uzzi, B. (1996).
  The sources and consequences of embeddedness for the economic performance of organizations: The network effect.
  American Sociological Review, 61(4):674–698.
* van Meeteren and Poorthuis, (2018)

  van Meeteren, M. and Poorthuis, A. (2018).
  Christaller and “big data”’: recalibrating central place theory via the geoweb.
  Urban Geography, 39(1):122–148.
* Viljoen, (2021)

  Viljoen, S. (2021).
  A relational theory of data governance.
  The Yale Law Journal, pages 573–654.
* Wang et al., (2024)

  Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., et al. (2024).
  A survey on large language model based autonomous agents.
  Frontiers of Computer Science, 18(6):186345.
* Wang et al., (2021)

  Wang, M., Sähl, J., et al. (2021).
  The willingness to risk others’ privacy for monetary and time rewards: An experimental study.
  SSRN Electronic Journal.
  Elicits WTA to place privacy at risk; compensation rises with perceived risk of disclosure.
* Ye and Zhu, (2023)

  Ye, J. and Zhu, J. (2023).
  China moves towards digital economy dream with national data bureau.
  Reuters.
* Zhang et al., (2025)

  Zhang, Z., Wang, X., Yi, M., Wang, M., Bai, F., Zheng, Z., Kang, Y., and Yang, Y. (2025).
  Policon: Evaluating llms on achieving diverse political consensus objectives.
* (69)

  Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., and Yang, D. (2024a).
  Can large language models transform computational social science?
  Computational Linguistics, 50(1):237–291.
* (70)

  Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., and Yang, D. (2024b).
  Can large language models transform computational social science?
  Computational Linguistics, 50(1):237–291.

## Supplementary material

The code and data underlying this study will be made publicly available upon acceptance at <https://github.com/haoyizhang720/Data-Market-ABM>.