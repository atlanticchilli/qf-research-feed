---
authors:
- Roberto Garrone
doc_id: arxiv:2601.08721v1
family_id: arxiv:2601.08721
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Feasibility-First Satellite Integration in Robust Portfolio Architectures
url_abs: http://arxiv.org/abs/2601.08721v1
url_html: https://arxiv.org/html/2601.08721v1
venue: arXiv q-fin
version: 1
year: 2026
---


Roberto Garrone
  
University of Salford, Salford, UK
  
University Sapienza Unitelma, Rome, Italy
  
University of Milan-Bicocca, Milan, Italy
  
roberto.garrone@unimib.it

(January 11, 2026)

###### Abstract

The integration of thematic satellite allocations into core-satellite portfolio architectures is commonly approached using factor exposures, discretionary convictions, or backtested performance, with feasibility assessed primarily through liquidity screens or market-impact considerations. While such approaches may be appropriate at institutional scale, they are ill-suited to small portfolios and robustness-oriented allocation frameworks, where dominant constraints arise not from return predictability or trading capacity, but from fixed costs, irreversibility risk, and governance complexity.

This paper develops a feasibility-first, non-predictive framework for satellite integration that is explicitly scale-aware. We formalize four nested feasibility layers (physical, economic, structural, and epistemic) that jointly determine whether a satellite allocation is admissible. Physical feasibility ensures implementability under concave market-impact laws; economic feasibility suppresses noise-dominated reallocations via cost-dominance threshold constraints; structural feasibility bounds satellite size through an explicit optionality budget defined by tolerable loss under thesis failure; and epistemic feasibility limits satellite breadth and dispersion through an entropy-based complexity budget.

Within this hierarchy, structural optionality is identified as the primary design principle for thematic satellites, with the remaining layers acting as robustness lenses rather than optimization criteria. The framework yields closed-form feasibility bounds on satellite size, turnover, and breadth without reliance on return forecasts, factor premia, or backtested performance, providing a disciplined basis for integrating thematic satellites into small, robustness-oriented portfolios.

Keywords:
core–satellite portfolios; thematic investing; feasibility constraints; structural optionality; robustness-oriented allocation; market impact; portfolio governance; entropy-based complexity; small portfolios; non-predictive frameworks.

## 1 Introduction

The increasing popularity of thematic investing—particularly in areas such as artificial intelligence, digital infrastructure, and technological transformation—has led to widespread adoption of core–satellite portfolio architectures [[1](https://arxiv.org/html/2601.08721v1#bib.bib1), [2](https://arxiv.org/html/2601.08721v1#bib.bib2)]. In these frameworks, a diversified core is complemented by one or more thematic satellites intended to capture long-horizon structural trends. While this design is intuitively appealing, the integration of satellites remains weakly formalized in the academic literature, especially for small portfolios and robustness-oriented allocation schemes[[5](https://arxiv.org/html/2601.08721v1#bib.bib5), [7](https://arxiv.org/html/2601.08721v1#bib.bib7)].

Most existing approaches implicitly treat satellites as scaled-down versions of active strategies: weights are selected using factor exposures, thematic classifications, or discretionary convictions, and feasibility is assessed primarily through liquidity screens or backtested performance. This treatment conflates three conceptually distinct questions:
(i) whether a thematic exposure is economically meaningful,
(ii) whether it can be implemented robustly at a given portfolio scale, and
(iii) whether its integration preserves the governance and interpretability[[18](https://arxiv.org/html/2601.08721v1#bib.bib18)] of the overall portfolio.

This paper argues that, for small core–satellite portfolios, the dominant constraints on satellite integration are not return predictability, factor structure, or even market impact, but rather feasibility constraints operating at multiple layers: physical, economic, balance-sheet, and epistemic. When portfolio scale is modest, standard market-microstructure constraints are typically slack, while fixed costs, irreversibility risk, and complexity dominate. As a result, optimization-based or signal-driven satellite constructions often introduce fragility without commensurate benefits.

We therefore propose a feasibility-first framework for satellite integration, designed to complement robustness-oriented core allocations such as those employed in SMDT-type architectures. The framework formalizes four nested feasibility layers:

* •

  Physical feasibility, ensuring that satellite trades are admissible under concave market-impact laws;
* •

  Economic feasibility, suppressing noise-dominated reallocations via cost-dominance threshold constraints;
* •

  Structural feasibility, bounding satellite size through a structural optionality budget defined by tolerable loss if the thematic thesis fails;
* •

  Epistemic feasibility, limiting satellite breadth and dispersion via an entropy-based complexity budget.

Within this hierarchy, we argue that structural optionality provides the most natural primary design principle for thematic satellites. Satellites are treated not as continuously optimized return engines, but as bounded, slow-moving exposures representing long-horizon optionality on structural change. The remaining feasibility layers act as robustness lenses, ensuring that physical implementability, economic significance, and governance discipline are preserved.

Importantly, the framework is non-predictive by construction. It does not assume that thematic assets earn abnormal returns, nor does it rely on factor premia, timing signals, or backtested performance. Instead, it specifies the conditions under which a satellite allocation is admissible—in the sense that it does not undermine the robustness, interpretability, or survivability of the portfolio—irrespective of realized outcomes.

By separating feasibility from forecasting, this paper contributes a missing intermediate layer between high-level portfolio architecture and asset-level allocation, and provides a principled basis for integrating thematic satellites into small, robustness-oriented portfolios.

### 1.1 Research gap and contribution

Despite the practical ubiquity of core–satellite portfolio architectures, the academic
treatment of satellite integration remains weakly formalized, particularly for
*small* portfolios and robustness-oriented allocation schemes. Existing approaches
typically assess satellite feasibility through one of three lenses: factor exposure and
optimization [[5](https://arxiv.org/html/2601.08721v1#bib.bib5), [7](https://arxiv.org/html/2601.08721v1#bib.bib7)], thematic classification and
performance attribution [[24](https://arxiv.org/html/2601.08721v1#bib.bib24)], or liquidity and market-impact
capacity [[13](https://arxiv.org/html/2601.08721v1#bib.bib13), [14](https://arxiv.org/html/2601.08721v1#bib.bib14)]. These approaches implicitly assume that
feasibility is either ensured by construction or becomes binding only at institutional
scale. As a result, the literature leaves a conceptual gap between high-level portfolio
architecture and asset-level allocation: it lacks a *theme-agnostic, scale-aware*
definition of satellite *admissibility* that is independent of return forecasting.

This gap is especially salient in the small-portfolio regime that motivates the present
study. At modest scale, concave market-impact constraints are often non-binding for liquid
assets [[15](https://arxiv.org/html/2601.08721v1#bib.bib15)], while the dominant constraints arise elsewhere. Fixed
trading frictions and discrete execution imply that frequent micro-rebalancing is
economically dominated by noise rather than information
[[16](https://arxiv.org/html/2601.08721v1#bib.bib16)]. Thematic exposure introduces irreversibility risk,
making the cost of being wrong asymmetric and balance-sheet relevant
[[17](https://arxiv.org/html/2601.08721v1#bib.bib17)]. In addition, portfolio breadth and dispersion are constrained
by governance, monitoring, and interpretability capacity rather than by diversification
theory alone [[18](https://arxiv.org/html/2601.08721v1#bib.bib18), [19](https://arxiv.org/html/2601.08721v1#bib.bib19)]. Although these constraints are widely
recognized in practice, they are rarely integrated into a single, formal framework that
yields explicit, ex ante design bounds for satellite allocations.

This paper addresses that gap by reframing satellite integration as a
*feasibility-first* problem rather than a predictive or optimization problem. We make
three distinct contributions. First, we reinterpret satellite allocations as
*structural optionality* instead of scaled-down active strategies or thematic bets,
explicitly bounding exposure by tolerable loss under thesis failure, consistent with
theories of commitment and irreversibility under uncertainty
[[17](https://arxiv.org/html/2601.08721v1#bib.bib17)]. Second, we introduce a hierarchical feasibility framework that
separates physical, economic, structural, and epistemic constraints, clarifying which
constraints bind at small portfolio scales and why, and reflecting robustness-oriented
critiques of optimization under limited action resolution and governance capacity
[[5](https://arxiv.org/html/2601.08721v1#bib.bib5), [23](https://arxiv.org/html/2601.08721v1#bib.bib23)]. Third, we derive closed-form feasibility bounds on
satellite size, turnover, and breadth that do not rely on alpha estimates, factor premia,
or backtested performance.

By separating feasibility from forecasting, the proposed framework provides a principled
intermediate layer between portfolio architecture and asset-level allocation. The approach
complements robustness-oriented core constructions, such as SMDT-style architectures, and
is compatible with domain conditioning based on institutional and informational continuity,
as captured by GAER-type diagnostics [[21](https://arxiv.org/html/2601.08721v1#bib.bib21), [22](https://arxiv.org/html/2601.08721v1#bib.bib22)]. In this sense, the
contribution is not a new return model, but a clarification of when thematic satellites can
be integrated without undermining robustness, interpretability, or survivability.

## 2 Related Work

### 2.1 Factor investing and robustness-oriented allocation

A large literature studies factor-based portfolio construction, documenting cross-sectional return patterns associated with characteristics such as value, size, momentum, profitability, and investment. While factor models provide a powerful descriptive and organizational framework, their practical implementation has increasingly emphasized robustness, estimation error, and turnover control rather than pure mean–variance optimality.

This shift has motivated approaches such as equal-weighting, rank-based allocations, bounded tilts, and constraint-aware optimization, all of which seek to reduce sensitivity to parameter uncertainty and non-stationarity. Importantly, these methods implicitly assume a minimum degree of informational continuity and economic feasibility across the investable universe. However, the literature typically treats the domain of applicability of such methods as given, relying on liquidity screens or coverage thresholds rather than explicit feasibility diagnostics.

The present paper does not propose an alternative factor model, nor does it evaluate factor premia. Instead, it addresses a logically prior question: under what conditions can satellite allocations be added to a robustness-oriented core without violating feasibility constraints that factor models leave implicit?

### 2.2 Thematic investing and thematic ETFs

Thematic investing has grown rapidly, particularly through the proliferation of thematic ETFs targeting technologies, industries, or narratives such as artificial intelligence, robotics, clean energy, or genomics. The academic and practitioner literature on thematic strategies largely focuses on classification schemes, exposure mapping, and performance evaluation, often emphasizing long-horizon growth narratives or innovation cycles.

A recurring concern in this literature is that thematic portfolios tend to exhibit high concentration, elevated turnover, and sensitivity to capital flows. Empirical studies document that thematic ETF performance is often strongly correlated with investor flows, raising questions about whether observed returns reflect structural growth or transient demand effects. Moreover, thematic indices typically rebalance mechanically based on classification changes, introducing implicit trading rules that may be poorly aligned with portfolio scale or investor objectives.

Our framework differs fundamentally in perspective. We do not attempt to design or evaluate thematic portfolios as standalone products. Instead, we treat thematic exposure as a satellite component embedded within a broader portfolio architecture, whose primary role is to express bounded optionality rather than to maximize exposure to a narrative. From this standpoint, the relevant question is not whether a theme outperforms, but whether its inclusion is feasible given portfolio scale, governance capacity, and tolerance for irreversibility.

### 2.3 Market impact, liquidity, and implementation constraints

Market impact models and liquidity-based capacity constraints play a central role in the literature on portfolio implementation, particularly for large institutional investors. Concave impact laws—most prominently the square-root law—provide a well-established framework for bounding feasible trade sizes as a function of average daily volume and turnover.

While these results are essential at scale, their relevance diminishes sharply for small portfolios. At modest AUM levels, impact-based constraints are typically slack for liquid assets, and implementation feasibility is dominated by fixed costs, spreads, and governance considerations rather than by price impact. Nonetheless, impact models remain a necessary outer feasibility layer, ensuring physical admissibility of trades.

This paper incorporates market-impact constraints explicitly, but treats them as necessary but generally non-binding conditions in the small-portfolio regime. The contribution lies in identifying and formalizing the additional feasibility layers that become binding precisely when impact does not.

### 2.4 Portfolio governance, complexity, and bounded rationality

A smaller but growing literature emphasizes the role of governance, monitoring costs, and bounded rationality in portfolio management. From this perspective, overly complex portfolios may underperform not because of market frictions, but because they exceed the decision-maker’s capacity to monitor, interpret, and act consistently.

Entropy-based measures of portfolio concentration and diversification have been proposed as descriptive tools, but are rarely used as explicit constraints. We extend this idea by introducing an entropy budget as a feasibility condition, bounding the incremental complexity introduced by satellite allocations. This provides a formal link between portfolio structure and governance capacity, which is particularly relevant for small investors and decentralized decision environments.

## 3 Generalized Satellite Design under Feasibility Discipline

### 3.1 Objective and scope

The objective of the satellite component is to capture *structural adoption rents*
associated with a well-defined long-horizon theme (e.g., artificial intelligence,
energy transition, digital infrastructure, defense modernization, healthcare platforms),
while avoiding exposure to short-term hype, early-stage venture dynamics, or fragile
thematic beta.

The satellite is therefore designed as *bounded structural optionality* rather than
as an actively optimized or signal-driven strategy. The emphasis is on feasibility,
institutional embedding, and persistence of cash-flow extraction, not on thematic
completeness or narrative purity.

### 3.2 Allocation size and risk framing

The satellite allocation is bounded ex ante as a fraction of total portfolio value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α∈[αmin,αmax],αmax∈[0.10,0.15],\alpha\in[\alpha\_{\min},\alpha\_{\max}],\qquad\alpha\_{\max}\in[0.10,0.15], |  | (1) |

with the effective value of α\alpha determined by the structural optionality budget
(Section [5.3](https://arxiv.org/html/2601.08721v1#S5.SS3 "5.3 Approach III: Structural Feasibility (Optionality Budget) ‣ 5 Four Feasibility Approaches for Satellite Integration ‣ Feasibility-First Satellite Integration in Robust Portfolio Architectures")). Satellite sizing is *risk-budgeted rather than
conviction-weighted*: exposure reflects tolerable loss under thesis failure, not subjective
confidence in the theme.

### 3.3 Eligible asset universe

Let 𝒯\mathcal{T} denote a thematic hypothesis (e.g., increased AI compute intensity,
electrification, digitization of public services). The eligible satellite universe is
restricted to assets that satisfy both:

1. 1.

   Thematic relevance: the theme contributes materially to long-run demand,
   pricing power, or cost advantage;
2. 2.

   Domain feasibility: assets belong to the GAER-admissible domain,
   𝒰GAER\mathcal{U}\_{\text{GAER}}.

Formally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮𝒯⊆𝒰GAER,\mathcal{S}\_{\mathcal{T}}\subseteq\mathcal{U}\_{\text{GAER}}, |  | (2) |

ensuring that the satellite does not attempt to compensate for adverse institutional,
regulatory, or geopolitical conditions through thematic exposure.

### 3.4 Generalized tier structure

To preserve feasibility purity and governance clarity, the satellite is organized into
tiers reflecting *where and how* structural rents are extracted along the thematic
value chain. The tiering principle is generic and applies to any theme.

##### Tier A — Hard constraints and bottlenecks.

Assets controlling capital-intensive, scarce, or regulated bottlenecks that are necessary
for the theme to scale. These entities typically exhibit high barriers to entry, systemic
relevance, and strong institutional embedding.

##### Tier B — Platforms and rent extractors.

Assets that intermediate, orchestrate, or monetize the theme through platforms, networks,
or long-duration contractual relationships. Rents arise from pricing power, lock-in, or
ecosystem control rather than from speculative end-demand.

##### Tier C — Embedded adopters.

Assets for which the theme enhances margins, efficiency, or switching costs without being
the primary revenue driver. Adoption is gradual, persistent, and complementary to existing
business models.

This tiered decomposition abstracts from sector labels and instead reflects the economic
role played by each asset within the thematic diffusion process.

### 3.5 Internal weighting rules

Internal satellite weights are determined by parsimonious, rule-based schemes rather than
optimization. Let KAK\_{A}, KBK\_{B}, and KCK\_{C} denote the number of constituents in Tiers A, B,
and C, respectively, with K=KA+KB+KCK=K\_{A}+K\_{B}+K\_{C}.

Weights are assigned as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi={αK⋅κA,i∈Tier A,αK,i∈Tier B,αK⋅κC,i∈Tier C,w\_{i}=\begin{cases}\frac{\alpha}{K}\cdot\kappa\_{A},&i\in\text{Tier A},\\[6.0pt] \frac{\alpha}{K},&i\in\text{Tier B},\\[6.0pt] \frac{\alpha}{K}\cdot\kappa\_{C},&i\in\text{Tier C},\end{cases} |  | (3) |

where κA≥1\kappa\_{A}\geq 1, κC≤1\kappa\_{C}\leq 1, and normalization ensures ∑iwi=α\sum\_{i}w\_{i}=\alpha.
This implements equal-weighting within tiers with an optional mild tilt toward upstream
constraints and away from downstream adopters.

### 3.6 Rebalancing discipline

Rebalancing is intentionally infrequent and governance-driven. The default schedule is
annual or semi-annual. Rebalancing is *not* triggered by price momentum, valuation
signals, or short-term thematic news.

Adjustments are permitted only upon identifiable *structural breaks*, including:

* •

  regulatory or policy regime shifts affecting the theme;
* •

  supply-side discontinuities or constraint realignments;
* •

  institutional or geopolitical changes altering GAER admissibility;
* •

  technological standardization events that relocate rents across tiers.

Absent such events, the satellite remains unchanged.

### 3.7 Explicit exclusions

Across themes, certain asset categories are excluded from satellite eligibility by design,
independently of expected returns or thematic relevance.
Table [1](https://arxiv.org/html/2601.08721v1#S3.T1 "Table 1 ‣ 3.7 Explicit exclusions ‣ 3 Generalized Satellite Design under Feasibility Discipline ‣ Feasibility-First Satellite Integration in Robust Portfolio Architectures") summarizes the asset categories that are excluded from
satellite eligibility based on feasibility considerations.

| Excluded category | Rationale |
| --- | --- |
| Pure-play early-stage firms | Venture-like risk and regime fragility |
| Small-cap thematic specialists | Liquidity, disclosure, and impact constraints |
| Regime-opaque jurisdictions | Institutional and geopolitical discontinuity |
| Thematic ETFs | Factor dilution and mechanically induced turnover |

Table 1: Asset categories excluded from thematic satellite eligibility.
Exclusions are based on feasibility considerations rather than return
expectations, reflecting constraints related to liquidity, governance,
and regime stability.

These exclusions reinforce the principle that the satellite is not a vehicle for thematic
completeness, but a controlled expression of feasibility-consistent optionality.

### 3.8 Interpretation

The generalized satellite framework applies uniformly across themes by focusing on
*economic role* rather than narrative labels. By combining GAER-based domain
conditioning with tiered exposure, bounded optionality, and disciplined rebalancing,
the satellite remains compatible with robustness-oriented core allocations and preserves
the interpretability and survivability of the overall portfolio.

## 4 Worked Examples: Applying the Tiered Satellite Framework

This section provides two worked examples illustrating how the generalized, feasibility-first
satellite framework applies to distinct structural themes. The examples are intentionally
non-exhaustive and non-optimizing, and are presented to demonstrate transferability of the
tier logic across domains.

### 4.1 Artificial Intelligence

#### 4.1.1 Thematic hypothesis

The artificial intelligence theme is defined narrowly as the long-horizon diffusion of
compute-intensive and data-driven technologies across production, services, and public
infrastructure. The objective is to capture *structural adoption rents* arising from
bottlenecks, platform control, and switching costs, rather than short-term valuation
re-rating or speculative innovation cycles.

#### 4.1.2 Eligible universe and GAER conditioning

The AI satellite universe is restricted to AI *enablers* that satisfy GAER domain
admissibility:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮AI⊆𝒰GAER.\mathcal{S}\_{\text{AI}}\subseteq\mathcal{U}\_{\text{GAER}}. |  | (4) |

This excludes firms whose AI exposure depends on fragile funding conditions, opaque
disclosure, or discontinuous regulatory regimes.

#### 4.1.3 Tiered decomposition

##### Tier A — Compute and infrastructure bottlenecks.

This tier includes firms controlling capital-intensive and scarce components required for
AI scaling, such as advanced semiconductors, lithography, and foundry capacity. Rents arise
from monopoly-like positions, extreme capital intensity, and systemic relevance. These
assets are typically embedded within U.S., EU, or allied institutional cores and benefit
from implicit backstops in stress scenarios.

##### Tier B — Platforms and rent extractors.

This tier includes firms monetizing AI through cloud platforms, enterprise software stacks,
and ecosystem control. Rents are extracted via pricing power over compute, APIs, and
long-duration enterprise contracts rather than end-user hype.

##### Tier C — Embedded enterprise adopters.

This tier includes firms for which AI adoption increases switching costs, margins, or
operational efficiency without being the primary revenue driver. Adoption is gradual and
persistent, aligning well with low-turnover satellite design.

#### 4.1.4 Sizing, weights, and rebalancing

Satellite size αAI\alpha\_{\text{AI}} is determined by the structural optionality budget:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αAI≤LDmax,\alpha\_{\text{AI}}\leq\frac{L}{D\_{\max}}, |  | (5) |

with internal weights assigned by equal-weighting within tiers and an optional mild tilt
favoring Tier A over Tier C. Rebalancing is annual or semi-annual and occurs only upon
identifiable structural breaks (e.g., export controls, foundry access, or regulatory regime
changes). Price momentum and short-term AI news do not trigger rebalancing.

#### 4.1.5 Explicit exclusions

Excluded from the AI satellite are pure-play AI startups, small-cap AI software firms,
AI-themed ETFs, and AI exposures in geopolitically discontinuous jurisdictions. These
exclusions reflect feasibility purity rather than thematic completeness.

### 4.2 Defense and Security Modernization

#### 4.2.1 Thematic hypothesis

The defense theme is defined as the long-horizon modernization of military, security, and
dual-use infrastructure driven by geopolitical realignment, alliance commitments, and
technological upgrading. The objective is to capture persistent rents associated with
defense procurement, systems integration, and embedded security requirements, rather than
cyclical conflict escalation or short-term budget announcements.

#### 4.2.2 Eligible universe and GAER conditioning

Defense-related candidates are restricted to GAER-admissible jurisdictions characterized by
stable procurement processes, transparent budgeting, and alliance-based security
commitments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮DEF⊆𝒰GAER.\mathcal{S}\_{\text{DEF}}\subseteq\mathcal{U}\_{\text{GAER}}. |  | (6) |

This excludes defense exposure in opaque regimes, ad hoc national champions, or jurisdictions
with discontinuous contract enforcement.

#### 4.2.3 Tiered decomposition

##### Tier A — Hard constraints and strategic bottlenecks.

This tier includes firms controlling capital-intensive and strategically critical assets,
such as prime contractors, shipyards, aerospace manufacturing capacity, and munitions
production. Rents arise from long-duration contracts, limited competition, and systemic
importance to national security.

##### Tier B — Systems integrators and platforms.

This tier includes firms specializing in systems integration, avionics, command-and-control,
cybersecurity, and ISR (intelligence, surveillance, reconnaissance) platforms. Rents are
derived from integration complexity, certification barriers, and long-term service
agreements.

##### Tier C — Embedded defense and security suppliers.

This tier includes firms providing software, logistics, maintenance, and dual-use
technologies embedded within broader defense systems. Adoption is incremental and persistent,
supporting low-turnover satellite structures.

#### 4.2.4 Sizing, weights, and rebalancing

Satellite size αDEF\alpha\_{\text{DEF}} is set via the same structural optionality budget used
for other themes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αDEF≤LDmax.\alpha\_{\text{DEF}}\leq\frac{L}{D\_{\max}}. |  | (7) |

Internal weights follow equal-weighting within tiers with an optional tilt toward Tier A.
Rebalancing is infrequent and triggered only by structural changes, such as alliance
reconfiguration, procurement regime shifts, or institutional realignments affecting GAER
admissibility.

#### 4.2.5 Explicit exclusions

Excluded from the defense satellite are small-cap defense specialists with limited contract
visibility, speculative cybersecurity startups, firms reliant on single-country conflict
exposure, and defense-themed ETFs. These exclusions avoid liquidity risk, governance opacity,
and mechanically induced turnover.

### 4.3 Cross-theme interpretation

Across both AI and defense, the same feasibility-first logic applies: exposure is organized
around constraint location, institutional embedding, and rent persistence rather than
sector labels or narratives. This demonstrates that the tiered satellite framework is
theme-agnostic and can be applied uniformly to structurally distinct domains while remaining
compatible with SMDT-style robustness and GAER-based domain conditioning.

## 5 Four Feasibility Approaches for Satellite Integration

Satellite integration is formulated as a feasibility problem rather than a forecasting or factor-extraction problem. We introduce four complementary approaches that operate at distinct layers of admissibility. A satellite allocation is considered admissible only if it satisfies all four criteria; the binding criterion depends on portfolio scale and governance context. Figure [1](https://arxiv.org/html/2601.08721v1#S5.F1 "Figure 1 ‣ 5 Four Feasibility Approaches for Satellite Integration ‣ Feasibility-First Satellite Integration in Robust Portfolio Architectures") summarizes the hierarchical structure of feasibility constraints used to assess satellite admissibility.

Physical feasibilityImpact admissibility under concave market–impact laws
Economic feasibility (Cost-Dominance Threshold)Suppression of noise-dominated and friction-driven reallocations
Structural feasibility (Optionality budget)Bounding exposure by tolerable loss under thematic failure
Epistemic feasibility (Entropy / governance)Limiting breadth and dispersion to preserve interpretability


Figure 1: Feasibility hierarchy for satellite integration.
Satellite admissibility is evaluated through a sequence of nested constraints:
physical feasibility, economic feasibility (Cost-Dominance Threshold),
structural feasibility (optionality budget), and epistemic feasibility
(entropy and governance). A satellite allocation is admissible only if all
lower-level constraints are satisfied.

### 5.1 Approach I: Physical Feasibility (Market Impact)

Purpose. Ensure that satellite trades are physically implementable under concave market-impact laws. This layer is essential at scale, and provides an outer admissibility envelope at any scale.

Primitive constraint. Let ViV\_{i} denote dollar ADV and QiQ\_{i} the dollar notional traded in asset ii at rebalancing. Assume a concave impact law

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ii=c​(QiVi)δ,0<δ<1,I\_{i}\;=\;c\left(\frac{Q\_{i}}{V\_{i}}\right)^{\delta},\qquad 0<\delta<1, |  | (8) |

with Qi≈A​wi​τiQ\_{i}\approx A\,w\_{i}\,\tau\_{i}, where AA is AUM, wiw\_{i} is the target weight, and τi∈[0,1]\tau\_{i}\in[0,1] is turnover fraction at the rebalance.

Feasibility bound. Imposing Ii≤I¯iI\_{i}\leq\bar{I}\_{i} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi≤ViA​τi​(I¯ic)1/δ.w\_{i}\;\leq\;\frac{V\_{i}}{A\,\tau\_{i}}\left(\frac{\bar{I}\_{i}}{c}\right)^{1/\delta}. |  | (9) |

A commonly used specialization is a participation cap Qi/Vi≤ϕQ\_{i}/V\_{i}\leq\phi, implying

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi≤ϕ​ViA​τi.w\_{i}\;\leq\;\frac{\phi\,V\_{i}}{A\,\tau\_{i}}. |  | (10) |

### 5.2 Approach II: Economic Feasibility (Cost-Dominance Threshold)

Purpose. Suppress rebalancing actions whose economic effect is dominated by fixed frictions and noise, thereby controlling turnover and ticket fragmentation in small portfolios.

Primitive constraint. Let CrtC\_{\mathrm{rt}} denote round-trip trading costs (in bps) for the relevant trading path (spread, commissions, and any FX conversions), and let ε\varepsilon denote a minimum economically meaningful portfolio effect (in bps). A weight change Δ​w\Delta w is admissible only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​w​Crt≥ε.\Delta w\,C\_{\mathrm{rt}}\;\geq\;\varepsilon. |  | (11) |

Feasibility bounds. Define the minimum meaningful weight change

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​wmin=εCrt.\Delta w\_{\min}\;=\;\frac{\varepsilon}{C\_{\mathrm{rt}}}. |  | (12) |

For a satellite sleeve of size α\alpha (fraction of total portfolio), this implies a natural upper bound on satellite breadth (coarse-graining):

|  |  |  |  |
| --- | --- | --- | --- |
|  | K≤αΔ​wmin,K\;\leq\;\frac{\alpha}{\Delta w\_{\min}}, |  | (13) |

under the design rule that each active satellite constituent must carry at least Δ​wmin\Delta w\_{\min} weight (within the total portfolio) to avoid noise-dominated trades.

### 5.3 Approach III: Structural Feasibility (Optionality Budget)

Purpose. Bound satellite size by balance-sheet tolerance under thesis failure. This approach treats the satellite as bounded, slow-moving structural optionality rather than a continuously optimized return engine.

Primitive constraint. Let α\alpha denote the satellite share of the total portfolio, DmaxD\_{\max} a conservative maximum plausible drawdown of the satellite under thesis failure, and LL the maximum acceptable total-portfolio loss attributable to the satellite.

Feasibility bound. The structural optionality budget is

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​Dmax≤L⟹α≤LDmax.\alpha\,D\_{\max}\;\leq\;L\qquad\Longrightarrow\qquad\alpha\;\leq\;\frac{L}{D\_{\max}}. |  | (14) |

Once α\alpha is fixed, internal satellite weights can be chosen by parsimonious rules (e.g., equal-weight across a small set) to preserve interpretability and reduce model dependence.

### 5.4 Approach IV: Epistemic Feasibility (Entropy / Complexity Budget)

Purpose. Limit incremental complexity (monitoring, interpretability, and governance burden) introduced by satellites. This is particularly relevant for small portfolios where decision capacity is a binding resource.

Primitive constraint. Define portfolio weight entropy

|  |  |  |  |
| --- | --- | --- | --- |
|  | H=−∑j=1Nwj​log⁡wj,H\;=\;-\sum\_{j=1}^{N}w\_{j}\log w\_{j}, |  | (15) |

and impose an entropy increment budget Δ​Hmax\Delta H\_{\max}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Htotal−Hcore≤Δ​Hmax.H\_{\mathrm{total}}-H\_{\mathrm{core}}\;\leq\;\Delta H\_{\max}. |  | (16) |

Feasibility bound. For a satellite of total weight α\alpha distributed equally across KK names, the incremental entropy is approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Hsat≈−α​log⁡(αK).\Delta H\_{\mathrm{sat}}\approx-\alpha\log\!\left(\frac{\alpha}{K}\right). |  | (17) |

Imposing Δ​Hsat≤Δ​Hmax\Delta H\_{\mathrm{sat}}\leq\Delta H\_{\max} yields an upper bound on breadth:

|  |  |  |  |
| --- | --- | --- | --- |
|  | K≤α​exp⁡(Δ​Hmaxα).K\;\leq\;\alpha\exp\!\left(\frac{\Delta H\_{\max}}{\alpha}\right). |  | (18) |

### 5.5 Comparative Summary

Table [2](https://arxiv.org/html/2601.08721v1#S5.T2 "Table 2 ‣ 5.5 Comparative Summary ‣ 5 Four Feasibility Approaches for Satellite Integration ‣ Feasibility-First Satellite Integration in Robust Portfolio Architectures") compares the four approaches by constraint
type, required inputs, binding regime, and typical design implication for
small core–satellite portfolios.

| Approach | Feasibility layer | Primitive inputs | Typically binding when | Main design implication |
| --- | --- | --- | --- | --- |
| I. Market impact | Physical implementability | ADV ViV\_{i}; turnover τi\tau\_{i}; AUM AA; impact cap I¯\bar{I} (or participation ϕ\phi) | Large AUM and/or high turnover; thin liquidity | Liquidity-weighted caps on wiw\_{i}; penalize frequent rebalancing |
| II. Cost-Dominance Threshold | Economic significance of trades | Round-trip costs CrtC\_{\mathrm{rt}}; minimum effect ε\varepsilon; sleeve size α\alpha | Small portfolios; fragmented tickets; high relative frictions | Coarse-grained satellites; upper bound on KK; suppress micro-rebalances |
| III. Optionality budget | Balance-sheet survivability | Satellite share α\alpha; thesis-failure drawdown DmaxD\_{\max}; loss tolerance LL | Whenever thesis risk is salient; preference for explicit loss bounds | Explicit upper bound on α\alpha; satellites interpreted as bounded optionality |
| IV. Entropy budget | Epistemic / governance capacity | Entropy increment Δ​Hmax\Delta H\_{\max}; sleeve size α\alpha; breadth KK | Limited monitoring capacity; desire for interpretability | Upper bound on KK and dispersion; discourages pseudo-diversification |

Table 2: Comparison of four feasibility approaches for satellite integration.
The approaches are complementary and may be treated as nested admissibility layers:
physical →\rightarrow economic →\rightarrow structural →\rightarrow epistemic.

Each feasibility layer imposes a distinct design constraint and excludes
specific classes of assumptions that are common in predictive or
optimization-based approaches.
Table [3](https://arxiv.org/html/2601.08721v1#S5.T3 "Table 3 ‣ 5.5 Comparative Summary ‣ 5 Four Feasibility Approaches for Satellite Integration ‣ Feasibility-First Satellite Integration in Robust Portfolio Architectures") provides a concise mapping between
feasibility layers, their economic interpretation, and the portfolio
dimensions they constrain.

| Feasibility layer | Economic interpretation | What it bounds | What it does not assume |
| --- | --- | --- | --- |
| Physical feasibility | Impact admissibility under concave market impact | Trade size per rebalance | Return predictability or alpha |
| Economic feasibility | Noise suppression via cost dominance | Turnover and action frequency | Timing skill or signal strength |
| Structural feasibility | Irreversibility and balance-sheet risk | Maximum satellite weight | Growth forecasts or theme success |
| Epistemic feasibility | Governance and interpretability capacity | Number of names and dispersion | Optimal diversification or factor structure |

Table 3: Interpretation of feasibility layers and associated design bounds.
The table summarizes the economic meaning of each feasibility layer, the
portfolio dimension it constrains, and the assumptions it explicitly does not
rely on.

### 5.6 Alternative criteria and minimal completeness

A natural question is whether alternative feasibility criteria could replace or dominate
the hierarchical framework proposed in this paper. The portfolio construction literature
offers several candidate approaches, including liquidity- or capacity-based sizing rules
[[13](https://arxiv.org/html/2601.08721v1#bib.bib13), [14](https://arxiv.org/html/2601.08721v1#bib.bib14)], volatility or drawdown-based risk budgets
[[7](https://arxiv.org/html/2601.08721v1#bib.bib7), [9](https://arxiv.org/html/2601.08721v1#bib.bib9)], belief-weighted or Bayesian exposure schemes
[[11](https://arxiv.org/html/2601.08721v1#bib.bib11)], and governance heuristics based on discretionary limits.
Each of these addresses a subset of the constraints relevant to satellite integration.

Liquidity- and impact-based criteria provide necessary conditions for physical
implementability, but are typically non-binding at the small portfolio scales considered
here and do not address economic significance, irreversibility risk, or governance
capacity [[15](https://arxiv.org/html/2601.08721v1#bib.bib15)]. Volatility- or tail-risk budgets quantify stochastic
variability but conflate reversible market fluctuations with structural loss under thematic
failure [[17](https://arxiv.org/html/2601.08721v1#bib.bib17)]. Belief- or scenario-weighted approaches reintroduce
forecasting assumptions and subjective priors, undermining robustness and auditability
[[5](https://arxiv.org/html/2601.08721v1#bib.bib5), [21](https://arxiv.org/html/2601.08721v1#bib.bib21)]. Informal governance heuristics capture
practical constraints but lack formal structure and cannot be translated into explicit,
auditable design bounds [[18](https://arxiv.org/html/2601.08721v1#bib.bib18)].

The feasibility hierarchy developed in this paper does not reject these perspectives;
rather, it subsumes them where appropriate. Physical feasibility encompasses standard
liquidity and market-impact constraints [[13](https://arxiv.org/html/2601.08721v1#bib.bib13), [14](https://arxiv.org/html/2601.08721v1#bib.bib14)]. Economic
feasibility formalizes the suppression of noise-dominated actions implied by fixed trading
frictions [[16](https://arxiv.org/html/2601.08721v1#bib.bib16)]. Structural feasibility captures
irreversibility and balance-sheet risk in a model-free manner consistent with real-options
logic [[17](https://arxiv.org/html/2601.08721v1#bib.bib17)]. Epistemic feasibility renders governance and
interpretability constraints explicit through a complexity budget, in line with concerns
about belief fragility and overextension [[18](https://arxiv.org/html/2601.08721v1#bib.bib18), [19](https://arxiv.org/html/2601.08721v1#bib.bib19)]. Within
the stated scope, alternative criteria either collapse to one of these layers or introduce
additional assumptions—most commonly predictive beliefs—that the present framework
deliberately excludes.

This observation motivates the following proposition.

###### Proposition 1 (Minimal completeness of the feasibility hierarchy).

Consider the class of satellite-integration frameworks that satisfy the following
conditions: (i) feasibility is assessed ex ante and independently of return forecasting
[[5](https://arxiv.org/html/2601.08721v1#bib.bib5)]; (ii) admissibility is scale-aware and applicable in the
small-portfolio regime [[15](https://arxiv.org/html/2601.08721v1#bib.bib15)]; (iii) structural loss under thematic
failure is bounded explicitly [[17](https://arxiv.org/html/2601.08721v1#bib.bib17)]; and (iv) governance and
interpretability constraints are treated as first-order design considerations
[[18](https://arxiv.org/html/2601.08721v1#bib.bib18)].

Within this class, any feasibility criterion for satellite allocations can be represented
as, or reduced to, a combination of physical, economic, structural, and epistemic
constraints as defined in this paper. No strictly weaker subset of these constraints yields
the same admissibility guarantees, and any strictly stronger framework necessarily
introduces additional assumptions beyond feasibility, such as predictive beliefs or
model-dependent valuation [[21](https://arxiv.org/html/2601.08721v1#bib.bib21), [22](https://arxiv.org/html/2601.08721v1#bib.bib22)].

Proposition [1](https://arxiv.org/html/2601.08721v1#Thmproposition1 "Proposition 1 (Minimal completeness of the feasibility hierarchy). ‣ 5.6 Alternative criteria and minimal completeness ‣ 5 Four Feasibility Approaches for Satellite Integration ‣ Feasibility-First Satellite Integration in Robust Portfolio Architectures") does not claim optimality in a return-maximizing
sense. Rather, it characterizes the feasibility hierarchy as a minimally complete design
layer: removing any constraint weakens admissibility guarantees, while adding further
structure moves the framework beyond feasibility and into forecasting or optimization.

## 6 Integrated Feasibility Strategy and Compatibility with SMDT–GAER

This section operationalizes satellite integration as a multi-layer feasibility problem.
Rather than selecting satellites via return forecasts, factor premia, or backtested
performance, we treat satellite exposure as *bounded optionality* subject to four
nested admissibility constraints: physical, economic, structural, and epistemic. The
resulting strategy is compatible with the SMDT architecture and with GAER-based universe
conditioning, because it preserves the separation between (i) informational feasibility
(domain), (ii) portfolio feasibility (implementation), and (iii) allocation rules (weights).

### 6.1 Strategy overview: a four-layer admissibility cascade

Let the total portfolio AUM be AA and let the satellite sleeve weight be α∈(0,1)\alpha\in(0,1),
so that satellite AUM is As=α​AA\_{s}=\alpha A. Let 𝒮\mathcal{S} denote the candidate satellite
set, with weights {wi}i∈𝒮\{w\_{i}\}\_{i\in\mathcal{S}} summing to α\alpha.

We implement the satellite through a cascade of feasibility filters:

1. 1.

   GAER domain constraint (informational admissibility).
   Restrict candidates to a GAER-admissible domain 𝒰GAER\mathcal{U}\_{\text{GAER}} (e.g., stable
   institutional embedding, disclosure/enforcement, geopolitical continuity). The satellite
   is defined *within* this domain rather than used to redefine the domain.
2. 2.

   Structural feasibility (primary sizing).
   Choose α\alpha using an explicit structural optionality budget that bounds loss under
   thesis failure.
3. 3.

   Epistemic feasibility (complexity budgeting).
   Given α\alpha, bound breadth K=|𝒮|K=|\mathcal{S}| and dispersion by an entropy budget.
4. 4.

   Economic feasibility (action resolution).
   Enforce Cost-Dominance Threshold to suppress noise-dominated reallocations and
   fragmented tickets.
5. 5.

   Physical feasibility (impact validation).
   Verify that concave market-impact bounds are satisfied for all planned trades; at small
   scale this is typically slack but remains a necessary outer admissibility check.

The ordering above is intentional: for small portfolios, structural and epistemic bounds
typically dominate; economic bounds discipline turnover; physical bounds provide a final
outer envelope.

### 6.2 Layer definitions and binding constraints

##### (0) GAER conditioning (domain).

Let 𝒰\mathcal{U} be the investable universe and 𝒰GAER⊆𝒰\mathcal{U}\_{\text{GAER}}\subseteq\mathcal{U}
the GAER-admissible subset. Satellite candidates must satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮⊆𝒰GAER.\mathcal{S}\subseteq\mathcal{U}\_{\text{GAER}}. |  | (19) |

This preserves the interpretation of GAER as a *domain feasibility diagnostic* rather
than a return signal.

##### (1) Structural optionality budget (sizing).

Let DmaxD\_{\max} be a conservative maximum drawdown of the satellite sleeve under thesis
failure, and let LL be the maximum acceptable loss contribution (fraction of total
portfolio) attributable to the satellite. Require

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​Dmax≤L⟹α≤LDmax.\alpha D\_{\max}\leq L\qquad\Longrightarrow\qquad\boxed{\alpha\leq\frac{L}{D\_{\max}}.} |  | (20) |

This yields a transparent upper bound on thematic exposure independent of liquidity,
turnover, or predictive assumptions.

##### (2) Entropy / complexity budget (breadth and dispersion).

Define weight entropy H=−∑jwj​log⁡wjH=-\sum\_{j}w\_{j}\log w\_{j} and impose an incremental budget
Δ​Hmax\Delta H\_{\max} for the satellite:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Htotal−Hcore≤Δ​Hmax.H\_{\text{total}}-H\_{\text{core}}\leq\Delta H\_{\max}. |  | (21) |

For a satellite of total weight α\alpha spread equally across KK names,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Hsat≈−α​log⁡(αK).\Delta H\_{\text{sat}}\approx-\alpha\log\!\left(\frac{\alpha}{K}\right). |  | (22) |

Imposing Δ​Hsat≤Δ​Hmax\Delta H\_{\text{sat}}\leq\Delta H\_{\max} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | K≤αexp(Δ​Hmaxα).\boxed{K\leq\alpha\exp\!\left(\frac{\Delta H\_{\max}}{\alpha}\right).} |  | (23) |

This constraint formalizes governance capacity and discourages pseudo-diversification in
small portfolios.

##### (3) Cost-Dominance Threshold (turnover control).

Let CrtC\_{\mathrm{rt}} denote round-trip trading costs (bps) and let ε\varepsilon denote a
minimum economically meaningful portfolio effect (bps). A weight change Δ​w\Delta w is
admissible only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​w​Crt≥ε⟹Δwmin=εCrt.\Delta w\,C\_{\mathrm{rt}}\geq\varepsilon\qquad\Longrightarrow\qquad\boxed{\Delta w\_{\min}=\frac{\varepsilon}{C\_{\mathrm{rt}}}.} |  | (24) |

This suppresses frequent micro-rebalances and forces coarse-grained, auditable actions.
Given sleeve size α\alpha, a sufficient practical bound on breadth is

|  |  |  |  |
| --- | --- | --- | --- |
|  | K≤αΔ​wmin\boxed{K\leq\frac{\alpha}{\Delta w\_{\min}}} |  | (25) |

under the design rule that each active satellite constituent carries at least
Δ​wmin\Delta w\_{\min} total-portfolio weight.

##### (4) Market-impact admissibility (physical validation).

Let ViV\_{i} denote ADV and QiQ\_{i} traded notional at rebalance. Under concave impact

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ii=c​(QiVi)δ,0<δ<1,I\_{i}=c\left(\frac{Q\_{i}}{V\_{i}}\right)^{\delta},\qquad 0<\delta<1, |  | (26) |

with Qi≈A​|winew−wiold|Q\_{i}\approx A\,|w\_{i}^{\text{new}}-w\_{i}^{\text{old}}| (or A​wi​τiAw\_{i}\tau\_{i} as an envelope),
imposing Ii≤I¯iI\_{i}\leq\bar{I}\_{i} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi≤ViA​τi(I¯ic)1/δ,\boxed{w\_{i}\leq\frac{V\_{i}}{A\,\tau\_{i}}\left(\frac{\bar{I}\_{i}}{c}\right)^{1/\delta},} |  | (27) |

or, under a participation cap Qi/Vi≤ϕQ\_{i}/V\_{i}\leq\phi,

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi≤ϕ​ViA​τi.\boxed{w\_{i}\leq\frac{\phi V\_{i}}{A\,\tau\_{i}}.} |  | (28) |

### 6.3 Operational procedure (algorithmic template)

The integrated strategy can be implemented with the following template:

1. 1.

   Domain selection. Construct 𝒰GAER\mathcal{U}\_{\text{GAER}} and restrict the
   candidate satellite list accordingly.
2. 2.

   Set the optionality budget. Choose (L,Dmax)(L,D\_{\max}) and set
   α=min⁡{αpolicy,L/Dmax}\alpha=\min\{\alpha\_{\text{policy}},L/D\_{\max}\}, where αpolicy\alpha\_{\text{policy}} is an
   ex ante policy cap.
3. 3.

   Set complexity budget. Choose Δ​Hmax\Delta H\_{\max} and derive an admissible
   breadth KK; specify a parsimonious weighting rule (e.g., equal-weight, capped weights).
4. 4.

   Set action resolution. Choose (Crt,ε)(C\_{\mathrm{rt}},\varepsilon) and compute
   Δ​wmin\Delta w\_{\min}; enforce no-trade regions and minimum ticket sizes consistent with
   Δ​wmin\Delta w\_{\min}.
5. 5.

   Validate impact. Using ADV estimates ViV\_{i}, verify that planned trades satisfy
   impact/participation bounds. If any name fails, adjust KK, reduce α\alpha, or replace
   the name with a higher-ADV proxy.

### 6.4 Compatibility with SMDT

The four-layer strategy is compatible with SMDT because it respects SMDT’s separation
between *robust allocation rules* and *feasibility constraints*. SMDT-type cores
typically rely on low-estimation-error constructions (e.g., equal-weight baselines and
bounded tilts) and treat turnover as a central friction. The present satellite framework
does not introduce predictive signals into the core; it adds an outer governance layer
that:
(i) bounds satellite size via explicit loss tolerance (structural optionality),
(ii) bounds complexity (entropy),
(iii) bounds turnover via Cost-Dominance Threshold, and
(iv) verifies physical implementability via impact laws.
Therefore, the satellite remains an add-on that does not alter the internal logic of the
core weighting scheme.

### 6.5 Compatibility with GAER

GAER is interpreted as a *domain conditioning diagnostic* that characterizes the
institutional and informational environment in which robust, rank-based, or bounded-tilt
strategies remain feasible. The present satellite framework is compatible with GAER
because it:

1. 1.

   Treats GAER as an *ex ante admissibility filter* defining 𝒰GAER\mathcal{U}\_{\text{GAER}},
   not as an expected-return signal or timing device;
2. 2.

   Applies satellite feasibility constraints *within* 𝒰GAER\mathcal{U}\_{\text{GAER}},
   thereby avoiding the misinterpretation of the satellite as a mechanism to “override”
   domain feasibility;
3. 3.

   Reinforces the core implication of GAER: the persistence of informational signals
   and the continuity of price discovery are prerequisites for robustness-oriented
   allocations.

### 6.6 Discussion: which constraints bind in small portfolios?

In small core–satellite portfolios, market-impact bounds derived from concave impact laws
are typically slack for liquid assets, and thus serve primarily as a validation layer.
By contrast, (i) cost-dominance threshold constraints, (ii) structural optionality
budgets, and (iii) entropy budgets are often binding, because they encode the practical
dominants at small scale: fixed frictions, tolerable loss under thesis failure, and
governance capacity. This explains why feasibility-first satellite integration can remain
non-predictive while still producing actionable and auditable design bounds on satellite
size, turnover, and breadth.

### 6.7 Scope and limitations

The framework developed in this paper is intentionally non-predictive and does not make
claims about the return performance of thematic satellites relative to benchmarks or
alternative allocation schemes. Parameter choices such as impact tolerances, loss budgets,
entropy limits, or cost-dominance threshold parameters are treated as policy inputs rather
than estimated quantities, and are therefore not calibrated within the paper. The worked
examples are illustrative mappings of the proposed feasibility logic to representative
themes and should not be interpreted as security recommendations or as evidence of
outperformance. Finally, while the analysis is motivated by small core–satellite
portfolios, the framework does not seek to characterize optimal behavior at large
institutional scale, where different constraints may bind. These limitations are
deliberate: the contribution of the paper is to formalize a missing feasibility layer for
satellite integration, not to propose a new predictive model or optimization criterion.

## Appendix A Calibration Notes and Design Parameters

This appendix clarifies the role of calibration choices in the proposed feasibility-first
framework. All parameters introduced in the main text are treated as *design and
governance inputs*, not as estimated quantities, and are therefore not calibrated using
historical return data, factor regressions, or optimization criteria.

### A.1 Impact and participation parameters

Parameters such as the impact tolerance I¯\bar{I}, the participation cap ϕ\phi, and the
impact exponent δ\delta enter the physical feasibility layer as *outer admissibility
checks*. At the portfolio scales motivating this study, these constraints are typically
slack for liquid assets and are included primarily to ensure physical implementability
rather than to optimize execution costs. Reasonable parameter ranges can be informed by
execution practice or market conventions, but precise calibration is not required for the
framework to operate.

### A.2 Cost-Dominance Threshold parameters

The cost-dominance threshold parameters ε\varepsilon and round-trip cost proxy
CrtC\_{\mathrm{rt}} define the economic resolution of admissible trades. These parameters are
interpreted as governance tolerances reflecting the decision-maker’s willingness to act in
the presence of fixed frictions and noise. In practice, they can be set conservatively to
suppress frequent micro-adjustments; their role is to induce coarse-grained behavior rather
than to fine-tune performance.

### A.3 Structural optionality budgets

The loss tolerance LL and maximum plausible drawdown DmaxD\_{\max} used to size satellite
exposure are policy choices reflecting balance-sheet risk preferences and irreversibility
concerns under thesis failure. They are not intended to approximate probabilistic risk
measures such as volatility or value-at-risk. Different investors may select different
values depending on mandate and horizon; the framework is agnostic to these choices and
simply translates them into explicit bounds on satellite size.

### A.4 Entropy and complexity budgets

The entropy increment Δ​Hmax\Delta H\_{\max} is introduced as a proxy for governance,
interpretability, and monitoring capacity. It does not represent informational efficiency
in a statistical sense, nor does it aim to optimize diversification. Instead, it provides a
transparent mechanism to bound satellite breadth and dispersion relative to portfolio scale.
As with other parameters, Δ​Hmax\Delta H\_{\max} is selected ex ante and held fixed over time.

### A.5 Interpretation

Taken together, these parameters define a feasibility envelope rather than a calibrated
model. Their purpose is to make implicit governance and implementation constraints explicit
and auditable, not to maximize expected returns. Consequently, different parameter choices
will lead to different admissible satellite designs, but the qualitative structure of the
feasibility hierarchy—and the resulting separation between feasibility and forecasting—
remains unchanged.

## References

* Brinson et al. [1986]

  Brinson, G. P., Hood, L. R., and Beebower, G. L.
  Determinants of portfolio performance.
  *Financial Analysts Journal*, 42(4):39–44, 1986.
* Ilmanen and Kizer [2012]

  Ilmanen, A. and Kizer, J.
  The death of diversification has been greatly exaggerated.
  *Journal of Portfolio Management*, 38(3):15–27, 2012.
* Amenc et al. [2011]

  Amenc, N., Goltz, F., Martellini, L., and Retkowsky, P.
  Efficient indexation: An alternative to cap-weighted indices.
  *Journal of Investment Management*, 9(4):1–23, 2011.
* Blitz [2014]

  Blitz, D.
  Factor investing revisited.
  *Journal of Portfolio Management*, 40(2):45–55, 2014.
* Michaud [1989]

  Michaud, R. O.
  The Markowitz optimization enigma: Is optimized optimal?
  *Financial Analysts Journal*, 45(1):31–42, 1989.
* Jobson and Korkie [1980]

  Jobson, J. D. and Korkie, B.
  Estimation for Markowitz efficient portfolios.
  *Journal of the American Statistical Association*, 75(371):544–554, 1980.
* DeMiguel et al. [2009]

  DeMiguel, V., Garlappi, L., and Uppal, R.
  Optimal versus naive diversification.
  *Review of Financial Studies*, 22(5):1915–1953, 2009.
* Arnott et al. [2005]

  Arnott, R. D., Hsu, J., and Moore, P.
  Fundamental indexation.
  *Financial Analysts Journal*, 61(2):83–99, 2005.
* Clarke et al. [2013]

  Clarke, R., de Silva, H., and Thorley, S.
  Risk parity, maximum diversification, and minimum variance.
  *Journal of Portfolio Management*, 39(3):39–53, 2013.
* Barberis et al. [2018]

  Barberis, N., Shleifer, A., and Vishny, R.
  A survey of behavioral finance.
  *Handbook of the Economics of Finance*, 1:1053–1128, 2018.
* Pástor and Veronesi [2015]

  Pástor, L. and Veronesi, P.
  Learning in financial markets.
  *Annual Review of Financial Economics*, 7:361–381, 2015.
* Kyle [1985]

  Kyle, A. S.
  Continuous auctions and insider trading.
  *Econometrica*, 53(6):1315–1335, 1985.
* Almgren and Chriss [2001]

  Almgren, R. and Chriss, N.
  Optimal execution of portfolio transactions.
  *Journal of Risk*, 3(2):5–39, 2001.
* Tóth et al. [2011]

  Tóth, B., Eisler, Z., and Bouchaud, J.-P.
  The square-root impact law.
  *Physical Review E*, 83(5):056110, 2011.
* Bouchaud et al. [2018]

  Bouchaud, J.-P., Bonart, J., Donier, J., and Gould, M.
  Trades, quotes and prices.
  *Cambridge University Press*, 2018.
* Constantinides [1986]

  Constantinides, G. M.
  Capital market equilibrium with transaction costs.
  *Journal of Political Economy*, 94(4):842–862, 1986.
* Dixit and Pindyck [1994]

  Dixit, A. K. and Pindyck, R. S.
  *Investment under Uncertainty*.
  Princeton University Press, 1994.
* Gennaioli et al. [2018]

  Gennaioli, N., Shleifer, A., and Vishny, R.
  *A Crisis of Beliefs*.
  Princeton University Press, 2018.
* Cochrane [2011]

  Cochrane, J. H.
  Presidential address: Discount rates.
  *Journal of Finance*, 66(4):1047–1108, 2011.
* Maillard et al. [2010]

  Maillard, S., Roncalli, T., and Teiletche, J.
  The properties of equally weighted risk contribution portfolios.
  *Journal of Portfolio Management*, 36(4):60–70, 2010.
* Lo [2004]

  Lo, A. W.
  The adaptive markets hypothesis.
  *Journal of Portfolio Management*, 30(5):15–29, 2004.
* Shiller [2003]

  Shiller, R. J.
  From efficient markets theory to behavioral finance.
  *Journal of Economic Perspectives*, 17(1):83–104, 2003.
* Chorin and Hald [2009]

  Chorin, A. J. and Hald, O. H.
  Stochastic tools in mathematics and science.
  *Surveys in Applied Mathematics*, Springer, 2009.
* Bender et al. [2018]

  Bender, J., Hammond, P., Mok, J., and Phillips, B.
  Can thematic investing add value?
  *Journal of Portfolio Management*, 44(5):83–94, 2018.