---
authors:
- Roberto Garrone
doc_id: arxiv:2601.05924v1
family_id: arxiv:2601.05924
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Geopolitical and Institutional Constraints on Adaptive Market Efficiency A
  Feasibility Diagnostic for Robust Portfolio Construction
url_abs: http://arxiv.org/abs/2601.05924v1
url_html: https://arxiv.org/html/2601.05924v1
venue: arXiv q-fin
version: 1
year: 2026
---


Roberto Garrone
  
Preprint
  

Roberto Garrone
  
University of Salford, Salford, UK
  
University Sapienza Unitelma, Rome, Italy
  
University of Milan-Bicocca, Milan, Italy
  
roberto.garrone@unimib.it

(January 9, 2026)

###### Abstract

This paper develops a structural framework for characterizing the informational feasibility of financial markets under heterogeneous institutional and geopolitical conditions. Departing from the assumption of uniform and time-invariant market efficiency, we conceptualize adaptive efficiency as a localized and state-dependent property emerging from the interaction between economic scale, institutional enforcement, and geopolitical embedding. To operationalize this perspective, we introduce the Geopolitical–Adaptive Efficiency Ratio (GAER), a descriptive cross-sectional indicator measuring the concentration of adaptive-efficiency-supporting mass within institutionally and geopolitically central assets. GAER is not a return-predictive signal, factor, or regime classifier. Instead, it functions as a diagnostic boundary condition, delimiting the domain in which ranking-based, robustness-oriented portfolio construction methods are plausibly applicable.

The framework integrates insights from adaptive market theory, institutional economics, and political economy, linking disclosure continuity, liquidity provision, and enforcement credibility to the persistence of informational signals in asset prices. It is intended for portfolio researchers and practitioners employing robustness-oriented and constraint-aware methods rather than return-forecasting models. We formalize GAER, discuss its theoretical properties, and illustrate its interpretation using verosimilar global equity data. Applications include universe conditioning, cross-market comparability, stress-period diagnostics, and feasibility checks for factor-based strategies. By separating where adaptive efficiency plausibly holds from how portfolios should be constructed, this paper provides a conceptual foundation for constraint-aware financial modeling and complements robustness-oriented portfolio construction frameworks without relying on forecast-driven assumptions or parametric optimization.

Keywords:
adaptive market efficiency; institutional quality; geopolitical risk;
informational feasibility; portfolio construction; robustness;
market structure; liquidity; non-predictive diagnostics.

## 1 Introduction: Localizing Adaptive Market Efficiency

The Efficient Market Hypothesis (EMH) is commonly interpreted as implying that prices
incorporate available information rapidly and reliably across the investable universe
[[31](https://arxiv.org/html/2601.05924v1#bib.bib31), [32](https://arxiv.org/html/2601.05924v1#bib.bib32)]. Yet a long empirical tradition documents persistent deviations,
slow adjustment, and instability in the mapping from information to prices
[[40](https://arxiv.org/html/2601.05924v1#bib.bib40), [35](https://arxiv.org/html/2601.05924v1#bib.bib35)]. The Adaptive Markets Hypothesis (AMH) offers a
reconciliation: market efficiency is not a universal primitive but a conditional and
evolving property shaped by competition, learning, and market ecology
[[33](https://arxiv.org/html/2601.05924v1#bib.bib33), [34](https://arxiv.org/html/2601.05924v1#bib.bib34)]. Building on this view, the present preprint adopts an adaptive and
institutionally grounded interpretation of efficiency in which informational performance is
*local, conditional, and state-dependent*, emerging endogenously from the interaction
between institutional capacity, liquidity conditions, regulatory enforcement, and
geopolitical stability [[36](https://arxiv.org/html/2601.05924v1#bib.bib36), [37](https://arxiv.org/html/2601.05924v1#bib.bib37), [54](https://arxiv.org/html/2601.05924v1#bib.bib54)].

#### From universal postulate to feasibility question.

Under a constraint-aware perspective, efficiency is not assumed to hold uniformly; rather,
it is treated as an *emergent property of the environment* in which information is
generated, transmitted, and enforced. Informational signals are incorporated more rapidly
and reliably where market depth is high, disclosure standards are enforced, and credible
backstops reduce tail-event discontinuities [[38](https://arxiv.org/html/2601.05924v1#bib.bib38)]. Conversely, in segments
characterized by low liquidity, weaker enforcement, or institutional fragility,
informational frictions persist and price discovery becomes noisier or episodic
[[35](https://arxiv.org/html/2601.05924v1#bib.bib35), [40](https://arxiv.org/html/2601.05924v1#bib.bib40)]. This implies that the effective domain over which
adaptive efficiency holds is constrained by institutional and geopolitical conditions,
not determined solely by asset-level characteristics.

#### Geopolitics as infrastructure for informational continuity.

Institutional heterogeneity extends naturally to geopolitics. Monetary dominance,
sanctions regimes, trade fragmentation, and crisis-time interventions shape the stability
of information environments by reallocating liquidity and enforcement capacity across
jurisdictions and firms. Historically, systemic stabilizers have been unevenly applied,
with core currency areas and institutionally central markets more likely to receive
support during stress [[41](https://arxiv.org/html/2601.05924v1#bib.bib41), [44](https://arxiv.org/html/2601.05924v1#bib.bib44), [55](https://arxiv.org/html/2601.05924v1#bib.bib55)]. This asymmetry
implies that currency regimes supported by fiscal and military capacity, and globally
integrated firms operating within stable legal frameworks, tend to exhibit greater
continuity of disclosure and price discovery than markets operating outside these
structures [[44](https://arxiv.org/html/2601.05924v1#bib.bib44), [55](https://arxiv.org/html/2601.05924v1#bib.bib55)]. From this perspective, informational
efficiency is not uniform but conditioned by the stability of the surrounding
institutional and geopolitical infrastructure.

#### Firm-level implication: systemic embedding and signal persistence.

Under strong-form EMH, firm size and geopolitical embeddedness should be largely
irrelevant for informational efficiency once risk is correctly priced. In contrast, an
adaptive and institutionally grounded view predicts that large, systemically important
firms operating within stable regulatory and monetary environments benefit from more
continuous disclosure, intensive monitoring, and privileged access to liquidity,
reducing information disruption and improving signal persistence
[[52](https://arxiv.org/html/2601.05924v1#bib.bib52), [54](https://arxiv.org/html/2601.05924v1#bib.bib54), [55](https://arxiv.org/html/2601.05924v1#bib.bib55)]. Firms lacking such embedding are more exposed to
funding constraints, regulatory discontinuities, and abrupt repricing, particularly under
geopolitical or macroeconomic stress [[38](https://arxiv.org/html/2601.05924v1#bib.bib38), [40](https://arxiv.org/html/2601.05924v1#bib.bib40)]. What appear as
“anomalies” in frictionless EMH frameworks can therefore be interpreted as predictable
outcomes of heterogeneous information environments rather than transient inefficiencies.

#### Portfolio-relevant implication (without tactical claims).

These considerations matter for portfolio research because many robustness-oriented
constructions rely on relative rankings, bounded adjustments, and constrained turnover.
Such methods implicitly require a minimum degree of information stability that is not
uniformly available across assets and jurisdictions [[56](https://arxiv.org/html/2601.05924v1#bib.bib56), [57](https://arxiv.org/html/2601.05924v1#bib.bib57)].
Restricting attention to assets embedded in stable institutional and geopolitical
environments is therefore not a rejection of efficiency, but a recognition that
efficiency is unevenly distributed and must be localized. The present paper addresses
this localization problem by introducing a descriptive diagnostic that summarizes the
concentration of adaptive-efficiency-supporting conditions in the investable universe.

#### Scope and intended contribution.

This paper contributes to the portfolio construction and asset management literature by
introducing a diagnostic framework for assessing the informational feasibility of
ranking-based and robustness-oriented methods. It does not propose a new asset pricing
model, return factor, or equilibrium theory. Instead, it focuses on characterizing the
environmental conditions under which existing portfolio methodologies can be expected to
operate with stable informational inputs.

### 1.1 Research Gap and Contribution

Despite extensive advances in asset pricing, portfolio construction, and adaptive
market theory, the literature lacks a formal framework for characterizing the
*informational feasibility domain* within which robustness-oriented portfolio
methods are plausibly applicable. Existing strands of research address related
components in isolation, but do not integrate them into a coherent diagnostic layer
situated between theory and implementation.

First, classical and modern formulations of market efficiency—from the EMH to the
AMH—conceptualize efficiency as either universal in principle or evolving through
competition and learning [[31](https://arxiv.org/html/2601.05924v1#bib.bib31), [32](https://arxiv.org/html/2601.05924v1#bib.bib32), [33](https://arxiv.org/html/2601.05924v1#bib.bib33), [34](https://arxiv.org/html/2601.05924v1#bib.bib34)]. While these frameworks
acknowledge time variation and adaptation, they remain largely silent on how the
*continuity of informational processing* varies structurally across assets and
jurisdictions. Empirically observed deviations are typically attributed ex post to
frictions, behavioral effects, or limits to arbitrage [[35](https://arxiv.org/html/2601.05924v1#bib.bib35), [40](https://arxiv.org/html/2601.05924v1#bib.bib40)],
rather than treated ex ante as consequences of heterogeneous institutional and
geopolitical environments.

Second, the portfolio construction and asset management literature has developed a wide
range of robustness-oriented methods—including equal-weighting, rank-based allocations,
bounded adjustments, and constraint-aware optimizations—explicitly motivated by
estimation error, non-stationarity, and model uncertainty
[[17](https://arxiv.org/html/2601.05924v1#bib.bib17), [28](https://arxiv.org/html/2601.05924v1#bib.bib28)]. However, these approaches generally *take the
informational domain as given*, relying on liquidity or coverage screens without a
principled characterization of whether the underlying environment supports sufficiently
stable signal extraction in the first place. As a result, portfolio robustness is often
addressed at the level of allocation mechanics rather than informational feasibility.

Third, a substantial literature focuses on liquidity, trading frictions, and
implementation costs, providing sophisticated diagnostics for *economic feasibility*,
such as illiquidity measures, turnover penalties, and transaction-cost models
[[1](https://arxiv.org/html/2601.05924v1#bib.bib1), [27](https://arxiv.org/html/2601.05924v1#bib.bib27)]. While these contributions are central for
assessing realized performance, they address how portfolios can be implemented
profitably, not where adaptive efficiency plausibly holds. Informational feasibility and
economic feasibility are therefore often conflated or treated sequentially without an
explicit conceptual boundary between them.

Finally, insights from institutional economics and political economy emphasize the role
of enforcement quality, governance, and geopolitical stability in shaping market outcomes
[[36](https://arxiv.org/html/2601.05924v1#bib.bib36), [37](https://arxiv.org/html/2601.05924v1#bib.bib37), [54](https://arxiv.org/html/2601.05924v1#bib.bib54), [41](https://arxiv.org/html/2601.05924v1#bib.bib41), [44](https://arxiv.org/html/2601.05924v1#bib.bib44)].Yet these insights have rarely been operationalized into *model-agnostic diagnostics*
usable by portfolio researchers without turning geopolitical considerations into
return-predictive signals or discretionary overlays.

This paper addresses this gap by introducing the *Geopolitical–Adaptive Efficiency Ratio (GAER)*, a descriptive, cross-sectional diagnostic that summarizes the concentration of adaptive-efficiency-supporting conditions within an investable universe.
By design, GAER does not forecast returns, define regimes, or prescribe portfolio weights.
Instead, it formalizes a missing intermediate layer between theory and application: a
feasibility boundary that clarifies *where* ranking-based and robustness-oriented
portfolio methods can be expected to operate under relatively continuous informational
conditions. In doing so, the framework complements existing portfolio construction and
execution methodologies while preserving a clear separation between informational
feasibility, economic extraction, and allocation design
[[21](https://arxiv.org/html/2601.05924v1#bib.bib21), [57](https://arxiv.org/html/2601.05924v1#bib.bib57)].

### 1.2 Theoretical Grounding

The interpretation above aligns with established results in institutional and monetary
economics emphasizing that markets require enforceable contracts, credible governance,
and institutional continuity to function effectively
[[45](https://arxiv.org/html/2601.05924v1#bib.bib45), [46](https://arxiv.org/html/2601.05924v1#bib.bib46), [47](https://arxiv.org/html/2601.05924v1#bib.bib47)]. Subsequent contributions highlighted the role of
organizational scale and structure in shaping market outcomes [[48](https://arxiv.org/html/2601.05924v1#bib.bib48), [49](https://arxiv.org/html/2601.05924v1#bib.bib49)].
Keynes emphasized the role of conventions, policy support, and liquidity provision in
sustaining orderly markets under uncertainty [[50](https://arxiv.org/html/2601.05924v1#bib.bib50)], while Hayek showed that
price systems aggregate dispersed information efficiently only when legal and institutional
filters preserve signal integrity [[51](https://arxiv.org/html/2601.05924v1#bib.bib51)]. Coase provided a micro-level foundation
by demonstrating that economic activity concentrates when internal coordination reduces
transaction costs, particularly under regulatory or political fragmentation [[52](https://arxiv.org/html/2601.05924v1#bib.bib52)],
a mechanism reinforced by public choice insights on endogenous regulation and differential
enforcement [[53](https://arxiv.org/html/2601.05924v1#bib.bib53)]. Modern institutional economics links enforcement
quality and political stability to long-run economic performance [[37](https://arxiv.org/html/2601.05924v1#bib.bib37)].

## 2 Adaptive Efficiency as an Emergent Property

Under strong-form EMH, informational efficiency is often treated as homogeneous in
principle, with deviations attributed to frictions, limits to arbitrage, or behavioral
effects [[31](https://arxiv.org/html/2601.05924v1#bib.bib31), [32](https://arxiv.org/html/2601.05924v1#bib.bib32)]. Under AMH, efficiency is instead local and
state-dependent, shaped by competition, learning, and market ecology
[[33](https://arxiv.org/html/2601.05924v1#bib.bib33), [34](https://arxiv.org/html/2601.05924v1#bib.bib34)]. A central implication for applied modeling is that the stability
of informational signals is contingent on the institutional and infrastructural
environment that produces and enforces those signals.

Institutional economics provides a structural basis for this contingency. Markets require
enforceable contracts, credible governance, and continuity of rules to support reliable
information aggregation and exchange [[36](https://arxiv.org/html/2601.05924v1#bib.bib36), [37](https://arxiv.org/html/2601.05924v1#bib.bib37), [54](https://arxiv.org/html/2601.05924v1#bib.bib54)].
When enforcement weakens or becomes discontinuous, informational frictions can persist
even in liquid markets, and the mapping from fundamentals and news to prices becomes
noisier or episodic [[35](https://arxiv.org/html/2601.05924v1#bib.bib35), [38](https://arxiv.org/html/2601.05924v1#bib.bib38)].

#### Interpretation.

In this view, “efficiency” should be treated as an emergent property of an environment
rather than a binary label for an asset. This motivates a diagnostic that summarizes
where adaptive-efficiency-supporting conditions are concentrated.

## 3 Institutional and Geopolitical Determinants of Informational Stability

Beyond domestic institutional quality, geopolitics shapes the information environment
through monetary dominance, sanctions regimes, trade fragmentation, and crisis-time
interventions. Historically, systemic stabilizers and liquidity backstops have been
unevenly applied, with central currency areas and institutionally core markets more
likely to receive supportive interventions during stress
[[41](https://arxiv.org/html/2601.05924v1#bib.bib41), [44](https://arxiv.org/html/2601.05924v1#bib.bib44), [55](https://arxiv.org/html/2601.05924v1#bib.bib55)].

At the firm level, large and systemically important issuers embedded in stable legal and
monetary environments may benefit from continuous disclosure, intensive monitoring,
privileged access to liquidity, and implicit backstops—all of which reduce information
disruption and support continuity in price discovery [[54](https://arxiv.org/html/2601.05924v1#bib.bib54), [55](https://arxiv.org/html/2601.05924v1#bib.bib55)].
By contrast, assets operating in peripheral or institutionally fragile contexts may
exhibit higher discontinuity in disclosure, enforcement, and market-making capacity.

#### Implication.

If informational continuity is heterogeneous, then the effective domain over which
ranking-based methods (and other robustness-oriented approaches) can be expected to
behave predictably is also heterogeneous.

## 4 From Theory to Measurement: Defining GAER

###### Definition 1 (Geopolitical–Adaptive Efficiency Ratio (GAER)).

Let 𝒰t\mathcal{U}\_{t} denote the investable universe at time tt, and let
𝒰tcore⊆𝒰t\mathcal{U}\_{t}^{\mathrm{core}}\subseteq\mathcal{U}\_{t} denote a subset classified as
“systemically embedded” (e.g., institutionally central and/or mega-cap assets). For each
asset ii, let MCi,t\mathrm{MC}\_{i,t} denote economic scale (e.g., market capitalization),
Gi,t∈[0,1]G\_{i,t}\in[0,1] a normalized indicator of geopolitical embedding, and
Ii,t∈[0,1]I\_{i,t}\in[0,1] a normalized proxy for institutional quality relevant to information
processing. Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | GAERt=∑i∈𝒰tcoreMCi,t​Gi,t​Ii,t∑j∈𝒰tMCj,t​Gj,t​Ij,t.\mathrm{GAER}\_{t}\;=\;\frac{\sum\_{i\in\mathcal{U}^{\mathrm{core}}\_{t}}\mathrm{MC}\_{i,t}\,G\_{i,t}\,I\_{i,t}}{\sum\_{j\in\mathcal{U}\_{t}}\mathrm{MC}\_{j,t}\,G\_{j,t}\,I\_{j,t}}. |  | (1) |

The classification of the core subset 𝒰tcore\mathcal{U}\_{t}^{\mathrm{core}} is intentionally
left flexible and may reflect economic scale thresholds, institutional centrality,
or regulatory relevance, depending on the application.

By construction, GAERt∈[0,1]\mathrm{GAER}\_{t}\in[0,1]. It can be interpreted as the share of aggregate
*adaptive-efficiency-supporting mass* concentrated in the core segment of the
universe. Higher values indicate that a larger fraction of economic scale is embedded in
environments where information flows, enforcement, and liquidity provision are more
continuous and reliable.

#### State variable, not signal.

GAER is a slow-moving diagnostic summarizing structural conditions. It is not designed
for short-horizon inference, return prediction, portfolio weighting, market timing, or
dynamic exposure management. This positioning is important in light of concerns about
factor proliferation and ex post narrative fitting [[21](https://arxiv.org/html/2601.05924v1#bib.bib21)].

#### Complementarity with execution and implementation feasibility.

GAER concerns *informational feasibility*: whether adaptive efficiency is plausibly
persistent enough for ranking-based, constraint-aware constructions to be meaningful. It
does not address *economic feasibility*: whether any residual structure can be
captured after turnover, liquidity, and capital frictions. Those questions belong to
execution and implementation diagnostics (e.g., liquidity risk measures and trading-cost
frameworks) and should remain analytically distinct [[1](https://arxiv.org/html/2601.05924v1#bib.bib1), [27](https://arxiv.org/html/2601.05924v1#bib.bib27)].

## 5 Interpretation and Theoretical Properties

### 5.1 Non-claims and boundary role

GAER does not test strong-form efficiency, nor does it imply that assets outside
high-GAER environments are inefficient, mispriced, or dominated. Its interpretation is
strictly comparative and contextual: GAER indicates where adaptive-efficiency-supporting
conditions are more likely to persist with sufficient continuity to justify the use of
ranking-based and robustness-oriented methods [[33](https://arxiv.org/html/2601.05924v1#bib.bib33), [28](https://arxiv.org/html/2601.05924v1#bib.bib28)].

### 5.2 Basic properties

Let wi,t:=MCi,t​Gi,t​Ii,t≥0w\_{i,t}:=\mathrm{MC}\_{i,t}G\_{i,t}I\_{i,t}\geq 0. Then GAER is a concentration ratio:

|  |  |  |
| --- | --- | --- |
|  | GAERt=∑i∈𝒰tcorewi,t∑j∈𝒰twj,t.\mathrm{GAER}\_{t}\;=\;\frac{\sum\_{i\in\mathcal{U}\_{t}^{\mathrm{core}}}w\_{i,t}}{\sum\_{j\in\mathcal{U}\_{t}}w\_{j,t}}. |  |

Properties follow immediately:

* •

  Scale–embedding interaction. High MC\mathrm{MC} alone does not dominate if GG or II is low.
* •

  Comparability. For a fixed construction of GG and II, GAER supports cross-market comparison as a summary statistic.
* •

  Stress sensitivity. In stress episodes, shifts in MC\mathrm{MC} (relative repricing) and/or in embedding indicators may alter GAER,
  contextualizing changes in feasibility.

### 5.3 Why a diagnostic is useful even without forecasting

A large portion of robustness-oriented practice relies on cross-sectional rankings and
bounded adjustments because these are comparatively stable under estimation error
[[28](https://arxiv.org/html/2601.05924v1#bib.bib28), [17](https://arxiv.org/html/2601.05924v1#bib.bib17)]. However, even rank stability depends on the continuity
of information processing and enforcement. GAER provides a compact descriptor of that
continuity domain, without converting geopolitics into an investable signal.

## 6 Illustrative Global Snapshot

This section illustrates the interpretation of GAER using a global equity
snapshot in which the core set is defined as the top cumulative market-capitalization
subset (e.g., 75%), and the numerator aggregates MC⋅G⋅I\mathrm{MC}\cdot G\cdot I over that
set. The purpose is interpretive rather than empirical: the values reported below are
illustrative and constructed using publicly available information and qualitative approximations, with the sole aim of clarifying the mechanics and interpretation of GAER, not of providing calibrated estimates or empirical inference.

Table 1: GAER input snapshot (illustrative values; MCAP and ADV in USD billions). Core denotes the top 75% cumulative market-capitalization subset used for the numerator of GAER.

| Ticker | Reg. | MCAP | ADV | GG | II | w=MCAP⋅G⋅Iw=\mathrm{MCAP}\cdot G\cdot I | Core |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MSFT | US | 3,100 | 14.0 | 0.95 | 0.96 | 2,827.2 | ✓ |
| AAPL | US | 2,900 | 18.0 | 0.95 | 0.95 | 2,617.2 | ✓ |
| AMZN | US | 1,900 | 10.0 | 0.94 | 0.94 | 1,678.8 | ✓ |
| NVDA | US | 2,000 | 22.0 | 0.92 | 0.90 | 1,656.0 | ✓ |
| GOOGL | US | 1,800 | 9.0 | 0.93 | 0.93 | 1,556.8 | ✓ |
| META | US | 1,200 | 8.0 | 0.92 | 0.92 | 1,015.7 | ✓ |
| BRK.B | US | 900 | 1.5 | 0.95 | 0.90 | 769.5 | ✓ |
| 2222.SR | SA | 2,000 | 0.6 | 0.60 | 0.68 | 816.0 | ✓ |
| TSLA | US | 800 | 12.0 | 0.88 | 0.85 | 598.4 | ✓ |
| LLY | US | 750 | 3.5 | 0.93 | 0.88 | 613.8 | ✓ |
| AVGO | US | 700 | 4.0 | 0.93 | 0.90 | 585.9 | ✓ |
| V | US | 520 | 2.8 | 0.92 | 0.90 | 430.6 | ✓ |
| JPM | US | 500 | 3.0 | 0.90 | 0.88 | 396.0 | ✓ |
| MA | US | 470 | 2.2 | 0.92 | 0.90 | 389.2 | ✓ |
| UNH | US | 450 | 1.6 | 0.90 | 0.87 | 352.4 | ✓ |
| XOM | US | 450 | 2.5 | 0.89 | 0.86 | 344.4 | ✓ |
| JNJ | US | 430 | 2.0 | 0.91 | 0.89 | 348.3 | ✓ |
| WMT | US | 420 | 2.2 | 0.91 | 0.88 | 335.0 | ✓ |
| TSM | TW | 600 | 4.5 | 0.75 | 0.82 | 369.0 | ✓ |
| ASML | NL | 420 | 1.2 | 0.85 | 0.88 | 314.2 |  |
| PG | US | 380 | 2.0 | 0.91 | 0.88 | 304.3 |  |
| HD | US | 380 | 1.7 | 0.90 | 0.88 | 300.7 |  |
| COST | US | 360 | 1.8 | 0.91 | 0.88 | 287.7 |  |
| ORCL | US | 360 | 2.4 | 0.90 | 0.87 | 281.9 |  |
| NESN.SW | CH | 330 | 0.4 | 0.86 | 0.86 | 244.3 |  |
| 005930.KS | KR | 380 | 1.8 | 0.78 | 0.80 | 237.1 |  |
| BAC | US | 310 | 2.2 | 0.88 | 0.86 | 234.8 |  |
| KO | US | 270 | 1.6 | 0.90 | 0.87 | 211.4 |  |
| PEP | US | 260 | 1.5 | 0.90 | 0.87 | 203.6 |  |
| NFLX | US | 260 | 5.0 | 0.90 | 0.86 | 201.2 |  |
| TM | JP | 270 | 0.9 | 0.82 | 0.84 | 186.0 |  |
| ROG.SW | CH | 240 | 0.4 | 0.86 | 0.85 | 175.4 |  |
| 700.HK | HK | 320 | 1.0 | 0.70 | 0.75 | 168.0 |  |
| NOVN.SW | CH | 220 | 0.5 | 0.86 | 0.85 | 160.8 |  |
| OR.PA | FR | 230 | 0.5 | 0.83 | 0.84 | 160.4 |  |
| AZN | UK | 210 | 0.8 | 0.85 | 0.85 | 151.7 |  |
| SAP | DE | 210 | 0.7 | 0.84 | 0.85 | 150.2 |  |
| SHEL | UK | 200 | 0.9 | 0.84 | 0.84 | 141.1 |  |
| MC.PA | FR | 200 | 0.6 | 0.83 | 0.84 | 139.4 |  |
| SIE.DE | DE | 170 | 0.5 | 0.84 | 0.84 | 119.9 |  |
| HSBA | UK | 150 | 0.8 | 0.84 | 0.83 | 104.6 |  |
| RELIANCE.NS | IN | 230 | 0.7 | 0.65 | 0.70 | 104.7 |  |
| TTE | FR | 150 | 0.7 | 0.82 | 0.82 | 100.9 |  |
| SONY | JP | 150 | 0.7 | 0.80 | 0.83 | 99.6 |  |
| 9983.T | JP | 150 | 0.9 | 0.80 | 0.80 | 96.0 |  |
| TCS.NS | IN | 170 | 0.4 | 0.66 | 0.72 | 80.8 |  |
| TCEHY | CN | 400 | 2.5 | 0.55 | 0.72 | 158.4 |  |
| BABA | CN | 180 | 3.0 | 0.55 | 0.70 | 69.3 |  |
| BIDU | CN | 100 | 1.2 | 0.55 | 0.68 | 37.4 |  |
| 111GAER inputs can be sourced from standard market data providers (market capitalization, trading volume), international financial institutions (IMF, BIS), governance databases (World Bank WGI, OECD), and regulatory bodies (IOSCO, WFE). The table reports illustrative values constructed from publicly available information and qualitative normalization, not calibrated estimates. |  |  |  |  |  |  |  |

Table LABEL:tab:gaer\_hypothetical reports a GAER snapshot for a globally
diversified large-cap equity universe. The core subset—defined as the top 75% of
cumulative market capitalization—accounts for a disproportionately large share of the
weighted mass w=MCAP⋅G⋅Iw=\mathrm{MCAP}\cdot G\cdot I, resulting in a relatively high GAER
value (approximately 0.77). This concentration reflects the systematic co-location of
economic scale, liquidity, and institutional and geopolitical embedding within a limited
set of mega-capitalization firms, predominantly operating in dominant currency areas and
subject to strong disclosure standards, regulatory oversight, and market infrastructure.
Assets outside the core generally exhibit lower values of GG and/or II—often
associated with weaker geopolitical integration indicators, thinner information
environments, or less continuous enforcement—which reduces their contribution to
aggregate adaptive efficiency despite, in some cases, substantial market capitalization.
More broadly, the table illustrates that in globally diversified large-cap universes,
adaptive-efficiency-supporting mass tends to concentrate in institutionally central
issuers, leading to higher GAER values when core markets dominate price discovery
capacity, and lower values when a larger fraction of economic scale resides in weaker or
more discontinuous informational environments. In this sense, GAER summarizes the
structural concentration of conditions supportive of adaptive efficiency and provides a
transparent motivation for universe conditioning in robustness-oriented portfolio
construction, without implying return predictability or tactical allocation guidance.

## 7 Applications as Feasibility Diagnostics

### 7.1 Universe conditioning

GAER can delimit the investable universe for portfolio construction methods that rely on
relative rankings, bounded adjustments, or turnover control. When GAER is high,
restricting attention to the core subset may preserve informational continuity assumptions
without materially reducing adaptive-efficiency-supporting mass. When GAER is low, the
informational domain may violate assumptions required for reliable ranking and bounded
optimization, analogous to liquidity and coverage screens.

### 7.2 Cross-market comparability

GAER supports formal comparison of informational environments across equity universes
(e.g., U.S.-centric, developed ex-U.S., emerging markets). Differences in GAER can be
interpreted as reflecting variation in institutional depth, regulatory continuity, and
geopolitical embedding, without invoking mispricing claims.

### 7.3 Stress-period diagnostics

During macroeconomic or geopolitical stress, liquidity reallocation and repricing may
shift GAER. While GAER is not a rebalancing trigger, it can contextualize observed
changes in turnover, tracking error, or factor instability by documenting shifts in the
concentration of adaptive efficiency across the universe.

### 7.4 Feasibility checks for factor-based modeling

Factor models and cross-sectional ranking methods can be supplemented with GAER as a
feasibility covariate. Low GAER does not imply factor failure, but signals that the
information environment may be discontinuous relative to the assumptions required for
stable ranking and bounded construction [[21](https://arxiv.org/html/2601.05924v1#bib.bib21), [57](https://arxiv.org/html/2601.05924v1#bib.bib57)].

## 8 Implications for Portfolio Construction

GAER addresses the question: *where is adaptive efficiency plausibly continuous
enough to support robustness-oriented methods?* It does not prescribe portfolio weights
or define an allocation algorithm. Downstream portfolio construction can treat GAER as an
exogenous feasibility boundary and remain fully implementable without computing GAER in
real time.

#### Complementarity with friction-focused feasibility ratios.

Whereas GAER concerns informational feasibility (continuity of information processing),
implementation feasibility depends on trading frictions and capital constraints (e.g.,
liquidity costs and turnover). This paper deliberately separates the informational domain
question from economic extraction questions, which are best handled by execution and
implementation diagnostics [[1](https://arxiv.org/html/2601.05924v1#bib.bib1), [27](https://arxiv.org/html/2601.05924v1#bib.bib27)].

## 9 Limitations and Open Directions

The construction of GAER depends on the specification of the geopolitical embedding
indicator GG and the institutional quality proxy II, which necessarily involves
measurement choices and potential sensitivity to proxy selection. As a result, GAER
should be interpreted as a diagnostic framework rather than as a uniquely defined
index.

Several directions for future research follow naturally from this formulation:

* •

  systematic design and validation of proxies for geopolitical embedding and
  institutional quality;
* •

  robustness analysis with respect to alternative normalizations, weighting
  schemes, and definitions of the core asset subset;
* •

  construction of historical GAER time series to examine structural shifts in
  the concentration of adaptive-efficiency-supporting conditions across market
  regimes and crisis episodes.

The present preprint deliberately emphasizes conceptual formalization and interpretive
clarity over empirical calibration. Extensions involving calibrated implementations,
sensitivity analysis across alternative proxy choices, or explicitly time-varying
applications are left for future work. This separation is intentional: it preserves
the diagnostic and non-predictive nature of GAER and avoids conflating informational
feasibility with economic performance or portfolio outcomes.

Accordingly, the objective of this contribution is not to propose a definitive or
exhaustive index, but to introduce a reusable *measurement template* for
feasibility-aware financial modeling that can be adapted and refined as empirical
and institutional data evolve.

## 10 Conclusion

This paper argues that adaptive market efficiency is not uniformly distributed across
assets and jurisdictions because the continuity of disclosure, enforcement, and liquidity
provision is heterogeneous. GAER operationalizes this heterogeneity as a descriptive
concentration ratio, summarizing where adaptive-efficiency-supporting mass is embedded.
Properly interpreted, GAER is a diagnostic boundary condition—not a return signal—that
complements robustness-oriented and constraint-aware financial modeling. By explicitly separating informational feasibility from economic extraction and
portfolio optimization, the GAER framework provides a transparent bridge between
institutional context and applied portfolio methodology, without introducing
forecasting assumptions or discretionary geopolitical judgments.

## Reproducibility

All components of the methodology are algorithmically defined. A reference implementation requires only total-return prices, basic liquidity measures, and optional fundamental data.

## References

* Amihud [2002]

  Amihud, Y. (2002).
  Illiquidity and stock returns: Cross-section and time-series effects.
  *Journal of Financial Markets*, 5(1), 31–56.
* Ang and Bekaert [2002]

  Ang, A., and Bekaert, G. (2002).
  International asset allocation with regime shifts.
  *Review of Financial Studies*, 15(4), 1137–1187.
* Arnott et al. [2005]

  Arnott, R. D., Hsu, J., and Moore, P. (2005).
  Fundamental indexation.
  *Financial Analysts Journal*, 61(2), 83–99.
* Asness et al. [2018]

  Asness, C. S., Frazzini, A., Israel, R., and Moskowitz, T. J. (2018).
  Fact, fiction, and momentum investing.
  *Journal of Portfolio Management*, 44(1), 75–92.
* Bailey and López de Prado [2014]

  Bailey, D. H., and López de Prado, M. (2014).
  The deflated Sharpe ratio: Correcting for selection bias, backtest overfitting, and non-normality.
  *Journal of Portfolio Management*, 40(5), 94–107.
* Bodie et al. [2018]

  Bodie, Z., Kane, A., and Marcus, A. J. (2018).
  *Investments* (11th ed.).
  McGraw–Hill.
* Boyd and Vandenberghe [2004]

  Boyd, S., and Vandenberghe, L. (2004).
  *Convex Optimization*.
  Cambridge University Press.
* Brandt [2010]

  Brandt, M. W. (2010).
  Portfolio choice problems.
  In Y. Aït-Sahalia and L. P. Hansen (Eds.),
  *Handbook of Financial Econometrics: Tools and Techniques* (Vol. 1).
  North-Holland.
* Brown et al. [1992]

  Brown, S. J., Goetzmann, W. N., Ibbotson, R. G., and Ross, S. A. (1992).
  Survivorship bias in performance studies.
  *Review of Financial Studies*, 5(4), 553–580.
* Carhart [1997]

  Carhart, M. M. (1997).
  On persistence in mutual fund performance.
  *Journal of Finance*, 52(1), 57–82.
* Chen et al. [2002]

  Chen, J., Hong, H., and Stein, J. C. (2002).
  Breadth of ownership and stock returns.
  *Journal of Financial Economics*, 66(2–3), 171–205.
* Chow et al. [2011]

  Chow, T.-M., Hsu, J., Kalesnik, V., and Little, B. (2011).
  Risk-based allocation.
  *Journal of Portfolio Management*, 37(2), 40–53.
* Clarke et al. [2006]

  Clarke, R., de Silva, H., and Thorley, S. (2006).
  Minimum-variance portfolios in the U.S. equity market.
  *Journal of Portfolio Management*, 33(1), 10–24.
* Daryanani [2008]

  Daryanani, G. (2008).
  Opportunistic rebalancing: A new paradigm for wealth managers.
  *Journal of Portfolio Management*, 34(3), 8–18.
* DeMiguel et al. [2009]

  DeMiguel, V., Garlappi, L., and Uppal, R. (2009).
  Optimal versus naive diversification: How inefficient is the 1/nn portfolio strategy?
  *Review of Financial Studies*, 22(5), 1915–1953.
* Fabozzi et al. [2007]

  Fabozzi, F. J., Kolm, P. N., Pachamanova, D. A., and Focardi, S. M. (2007).
  *Robust Portfolio Optimization and Management*.
  John Wiley & Sons.
* Fernholz [2002]

  Fernholz, R. (2002).
  *Stochastic Portfolio Theory*.
  Springer.
* Ferson and Harvey [1999]

  Ferson, W. E., and Harvey, C. R. (1999).
  Conditioning variables and the cross section of stock returns.
  *Journal of Finance*, 54(4), 1325–1360.
* Frazzini et al. [2015]

  Frazzini, A., Israel, R., and Moskowitz, T. J. (2015).
  Trading costs.
  *Journal of Financial Economics*, 116(2), 369–392.
* Grinold and Kahn [2000]

  Grinold, R. C., and Kahn, R. N. (2000).
  *Active Portfolio Management* (2nd ed.).
  McGraw–Hill.
* Harvey et al. [2016]

  Harvey, C. R., Liu, Y., and Zhu, H. (2016).
  … and the cross-section of expected returns.
  *Review of Financial Studies*, 29(1), 5–68.
* Jagannathan and Ma [2003]

  Jagannathan, R., and Ma, T. (2003).
  Risk reduction in large portfolios: Why imposing the wrong constraints helps.
  *Journal of Finance*, 58(4), 1651–1684.
* Jegadeesh and Titman [1993]

  Jegadeesh, N., and Titman, S. (1993).
  Returns to buying winners and selling losers: Implications for stock market efficiency.
  *Journal of Finance*, 48(1), 65–91.
* Korajczyk and Sadka [2008]

  Korajczyk, R. A., and Sadka, R. (2008).
  Pricing the commonality across alternative measures of liquidity.
  *Journal of Financial Economics*, 87(1), 45–72.
* Michaud [1989]

  Michaud, R. O. (1989).
  The Markowitz optimization enigma: Is optimized optimal?
  *Financial Analysts Journal*, 45(1), 31–42.
* Novy-Marx [2013]

  Novy-Marx, R. (2013).
  The other side of value: The gross profitability premium.
  *Journal of Financial Economics*, 108(1), 1–28.
* Pástor and Stambaugh [2003]

  Pástor, L., and Stambaugh, R. F. (2003).
  Liquidity risk and expected stock returns.
  *Journal of Political Economy*, 111(3), 642–685.
* Pedersen [2015]

  Pedersen, L. H. (2015).
  *Efficiently Inefficient: How Smart Money Invests and Market Prices Are Determined*.
  Princeton University Press.
* Plyakha et al. [2012]

  Plyakha, Y., Uppal, R., and Vilkov, G. (2012).
  Why does an equal-weighted portfolio outperform value-weighted portfolios?
  *Review of Financial Studies*, 25(7), 2169–2201.
* Qian [2007]

  Qian, E. (2007).
  On the financial interpretation of risk contribution.
  *Journal of Portfolio Management*, 33(4), 41–51.
* Fama [1970]

  Fama, E. F. (1970).
  Efficient Capital Markets: A Review of Theory and Empirical Work.
  *Journal of Finance*, 25(2), 383–417.
* Fama [1991]

  Fama, E. F. (1991).
  Efficient Capital Markets II.
  *Journal of Finance*, 46(5), 1575–1617.
* Lo [2004]

  Lo, A. W. (2004).
  The Adaptive Markets Hypothesis.
  *Journal of Portfolio Management*, 30(5), 15–29.
* Lo [2017]

  Lo, A. W. (2017).
  *Adaptive Markets*.
  Princeton University Press.
* Stiglitz [1980]

  Stiglitz, J. E. (1980).
  On the Impossibility of Informationally Efficient Markets.
  *American Economic Review*, 70(3), 393–408.
* North [1990]

  North, D. C. (1990).
  *Institutions, Institutional Change and Economic Performance*.
  Cambridge University Press.
* Acemoglu and Robinson [2012]

  Acemoglu, D., & Robinson, J. A. (2012).
  *Why Nations Fail*.
  Crown Business.
* Chordia et al. [2008]

  Chordia, T., Roll, R., & Subrahmanyam, A. (2008).
  Liquidity and Market Efficiency.
  *Journal of Financial Economics*, 87(2), 249–268.
* Fama and French [2015]

  Fama, E. F., & French, K. R. (2015).
  A Five-Factor Asset Pricing Model.
  *Journal of Financial Economics*, 116(1), 1–22.
* Shiller [1981]

  Shiller, R. J. (1981).
  Do Stock Prices Move Too Much?
  *American Economic Review*, 71(3), 421–436.
* Kindleberger [1973]

  Kindleberger, C. P. (1973).
  *The World in Depression*.
  University of California Press.
* Gilpin [1987]

  Gilpin, R. (1987).
  *The Political Economy of International Relations*.
  Princeton University Press.
* Wallerstein [1974]

  Wallerstein, I. (1974).
  *The Modern World-System*.
  Academic Press.
* Eichengreen [2011]

  Eichengreen, B. (2011).
  *Exorbitant Privilege*.
  Oxford University Press.
* Smith [1776]

  Smith, A. (1776).
  *The Wealth of Nations*.
* Ricardo [1817]

  Ricardo, D. (1817).
  *On the Principles of Political Economy and Taxation*.
* Mill [1848]

  Mill, J. S. (1848).
  *Principles of Political Economy*.
* Marx [1867]

  Marx, K. (1867).
  *Capital, Vol. I*.
* Marshall [1890]

  Marshall, A. (1890).
  *Principles of Economics*.
* Keynes [1936]

  Keynes, J. M. (1936).
  *The General Theory of Employment, Interest and Money*.
* Hayek [1945]

  Hayek, F. A. (1945).
  The Use of Knowledge in Society.
  *American Economic Review*, 35(4), 519–530.
* Coase [1937]

  Coase, R. H. (1937).
  The Nature of the Firm.
  *Economica*, 4(16), 386–405.
* Buchanan and Tullock [1962]

  Buchanan, J. M., & Tullock, G. (1962).
  *The Calculus of Consent*.
  University of Michigan Press.
* Williamson [1985]

  Williamson, O. E. (1985).
  *The Economic Institutions of Capitalism*.
  Free Press.
* Shin [2010]

  Shin, H. S. (2010).
  *Risk and Liquidity*.
  Oxford University Press.
* DeMiguel et al. [2009]

  DeMiguel, V., Garlappi, L., & Uppal, R. (2009).
  Optimal Versus Naive Diversification.
  *Review of Financial Studies*, 22(5), 1915–1953.
* Koijen and Rossi [2019]

  Koijen, R. S. J., & Rossi, A. G. (2019).
  Fragility of Factor Investing.
  *Journal of Finance*.
* [58]

  R. Almgren and N. Chriss,
  Optimal execution of portfolio transactions.
  *Journal of Risk*, 3(2):5–39, 2001.
* [59]

  R. Engle, E. Ghysels, and B. Sohn,
  The dynamics of market liquidity.
  *Journal of Financial Economics*, 106(3):593–613, 2012.