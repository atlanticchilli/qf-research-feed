---
authors:
- Murad Farzulla
- Andrew Maksakov
doc_id: arxiv:2602.03874v1
family_id: arxiv:2602.03874
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Contents
url_abs: http://arxiv.org/abs/2602.03874v1
url_html: https://arxiv.org/html/2602.03874v1
venue: arXiv q-fin
version: 1
year: 2026
---

ASRI: An Aggregated Systemic Risk Index for Cryptocurrency Markets
  
A Unified Framework for Monitoring DeFi-TradFi Interconnection Risk
  
Murad Farzulla1,2  Andrew Maksakov2
  
1King’s College London, 2[Dissensus AI](https://dissensus.ai)
  
January 2026
  
Correspondence: [murad@dissensus.ai](mailto:murad@dissensus.ai)

###### Abstract

Cryptocurrency markets have grown to represent over $3 trillion in capitalization, yet no unified index exists to monitor the systemic risks arising from the interconnection between decentralized finance (DeFi) protocols and traditional financial institutions. This paper introduces the Aggregated Systemic Risk Index (ASRI), a composite measure comprising four weighted sub-indices: Stablecoin Concentration Risk (30%), DeFi Liquidity Risk (25%), Contagion Risk (25%), and Regulatory Opacity Risk (20%). We derive theoretical foundations for each component, specify quantitative formulas incorporating data from DeFi Llama, Federal Reserve FRED, and on-chain analytics, and validate the framework against historical crisis events including the Terra/Luna collapse (May 2022), the Celsius/3AC contagion (June 2022), the FTX bankruptcy (November 2022), and the SVB banking crisis (March 2023). Empirical Results: Event study analysis detects statistically significant abnormal signals for all four crises (tt-statistics 5.47–32.64, all p<0.01p<0.01), though threshold-based operational detection identifies three of four events (Celsius/3AC, FTX, SVB) with an average lead time of 18 days. The Terra/Luna miss reflects a documented limitation of market-based indicators for algorithmic stablecoin risk. Stationarity tests confirm all sub-indices are stationary (ADF p<0.01p<0.01). A three-regime Hidden Markov Model identifies distinct Low Risk, Moderate, and Elevated states with regime persistence exceeding 94%. The framework passes structural stability tests (Chow p=0.99p=0.99). Benchmarking against the Diebold-Yilmaz (2012) connectedness index shows equivalent detection rates (75%) with higher precision (33.5% vs. 22.4%). Out-of-sample specificity testing on 2024–2025 data confirms zero false positives, including correct identification of the February 2025 Bybit hack ($1.5B, the largest exchange theft in history) as non-systemic due to absence of contagion channels. The ASRI framework addresses a critical gap in existing risk monitoring by capturing DeFi-specific vulnerabilities—composability risk, flash loan exposure, and tokenized real-world asset (RWA) linkages—that traditional systemic risk measures such as SRISK and CoVaR cannot accommodate.

Keywords: systemic risk, cryptocurrency, decentralized finance, stablecoin stability, contagion risk, DeFi-TradFi interconnection, risk monitoring, event study, regime detection

JEL Codes: G01 (Financial Crises), G15 (International Financial Markets), G23 (Non-bank Financial Institutions)

## 1 Introduction

The cryptocurrency market has evolved from a niche technological experiment into a multi-trillion dollar asset class with growing interconnections to traditional finance. As of December 2025, the total cryptocurrency market capitalization exceeds $3 trillion, with stablecoins alone representing over $140 billion in circulation (DeFi Llama, [2025](https://arxiv.org/html/2602.03874v1#bib.bib13)). This growth has been accompanied by a series of cascading failures that revealed systemic vulnerabilities previously unrecognized: the Terra/Luna collapse eliminated $40 billion in value within 72 hours; the subsequent Celsius and Three Arrows Capital failures triggered margin calls across centralized exchanges; and the FTX bankruptcy demonstrated how opaque counterparty relationships could propagate losses across the entire ecosystem.

Despite this systemic importance, no unified risk index exists to monitor the interconnection between decentralized finance (DeFi) protocols and traditional financial institutions. Existing measures either focus exclusively on cryptocurrency price volatility (Liu and Tsyvinski, [2021](https://arxiv.org/html/2602.03874v1#bib.bib27)), apply traditional banking metrics that miss DeFi-specific dynamics (Brownlees and Engle, [2017](https://arxiv.org/html/2602.03874v1#bib.bib9)), or provide sentiment-based indicators without quantitative grounding (Alternative.me, [2022](https://arxiv.org/html/2602.03874v1#bib.bib3)).

This paper introduces the Aggregated Systemic Risk Index (ASRI), a composite measure designed to capture the distinctive risk channels that arise from DeFi-TradFi interconnection. The index comprises four weighted sub-indices:

1. 1.

   Stablecoin Concentration Risk (30%): Measures reserve composition, peg stability, and Treasury exposure across major stablecoins
2. 2.

   DeFi Liquidity Risk (25%): Captures protocol concentration, leverage dynamics, and smart contract vulnerability
3. 3.

   Contagion Risk (25%): Quantifies TradFi linkage intensity, tokenized RWA growth, and cross-market correlation shifts
4. 4.

   Regulatory Opacity Risk (20%): Assesses transparency scores, regulatory arbitrage metrics, and compliance infrastructure

The ASRI framework addresses three critical gaps in existing risk monitoring:

First, composability risk. DeFi protocols interact through smart contract calls that create dependency chains invisible to external observers. When one protocol fails, composable integrations can transmit losses instantaneously across the ecosystem—a dynamic that traditional contagion models, designed for bilateral counterparty relationships, cannot capture.

Second, stablecoin-Treasury linkages. Major stablecoins now hold significant Treasury bill positions, creating a direct transmission channel between US monetary policy and DeFi liquidity conditions. Rate hikes that increase Treasury yields simultaneously reduce stablecoin reserve valuations and incentivize capital rotation out of yield-bearing DeFi positions.

Third, regulatory arbitrage dynamics. The fragmented regulatory landscape creates opacity about counterparty risk exposures, custody arrangements, and reserve attestation reliability. Traditional banking metrics assume regulatory disclosure requirements that do not exist for offshore or unregulated platforms.

This paper proceeds as follows. Section 2 reviews the literature on systemic risk measurement, cryptocurrency market dynamics, and existing crypto risk indices. Section 3 develops the ASRI framework, specifying the theoretical foundation and quantitative formulas for each sub-index. Section 4 describes data sources and implementation architecture. Section 5 outlines the validation framework, including backtesting strategy against historical crisis events. Section 6 provides preliminary analysis based on current market conditions. Section 7 discusses theoretical and practical implications. Section 8 concludes with a roadmap for empirical validation.

## 2 Literature Review

### 2.1 Traditional Systemic Risk Measures

The 2008 financial crisis catalyzed extensive research on systemic risk measurement. Adrian and Brunnermeier ([2016](https://arxiv.org/html/2602.03874v1#bib.bib2)) introduced Conditional Value-at-Risk (CoVaR), measuring the VaR of the financial system conditional on an institution being in distress. Acharya et al. ([2017](https://arxiv.org/html/2602.03874v1#bib.bib1)) developed SRISK, estimating the expected capital shortfall of a financial institution during a systemic crisis. Brownlees and Engle ([2017](https://arxiv.org/html/2602.03874v1#bib.bib9)) extended this framework with LRMES (Long-Run Marginal Expected Shortfall), capturing an institution’s contribution to aggregate capital shortfall.

These measures share a common architecture: they model systemic risk as arising from bilateral exposures between regulated financial institutions with observable balance sheets and regulatory capital requirements. This architecture is fundamentally unsuited to DeFi, where:

* •

  Protocols are not institutions with capital requirements
* •

  Exposures are embedded in smart contract code rather than disclosed counterparty relationships
* •

  “Failure” may manifest as liquidity drainage rather than insolvency
* •

  Contagion propagates through token price collapses and oracle manipulation rather than credit defaults

### 2.2 Cryptocurrency Market Risk

Research on cryptocurrency-specific risk has focused primarily on volatility dynamics and market microstructure. Liu and Tsyvinski ([2021](https://arxiv.org/html/2602.03874v1#bib.bib27)) identify three common factors driving cryptocurrency returns: market (aggregate crypto exposure), size, and momentum. Makarov and Schoar ([2020](https://arxiv.org/html/2602.03874v1#bib.bib31)) document arbitrage frictions across exchanges that allow price dislocations to persist, creating opportunities for informed traders and risks for liquidity providers. Farzulla ([2025a](https://arxiv.org/html/2602.03874v1#bib.bib17)) demonstrate that infrastructure disruptions generate 5.7×\times larger volatility shocks than regulatory events, suggesting that technical vulnerabilities represent a more severe systemic risk channel than policy uncertainty.

Griffin and Shams ([2020](https://arxiv.org/html/2602.03874v1#bib.bib20)) provide evidence that Tether issuance patterns correlate with Bitcoin price movements, raising questions about stablecoin reserve integrity. This finding has implications for systemic risk: if stablecoin issuance is not fully collateralized, DeFi liquidity pools dependent on stablecoin inflows may be vulnerable to sudden redemption pressures.

### 2.3 Crisis Episode Analysis

The cryptocurrency crises of 2022–2023 generated substantial empirical scholarship validating theoretical concerns about systemic fragility. Liu et al. ([2022](https://arxiv.org/html/2602.03874v1#bib.bib26)) provide the definitive analysis of the Terra/Luna collapse, documenting how algorithmic stablecoin mechanics created a reflexive depegging spiral that eliminated $40 billion in value within 72 hours. Ma et al. ([2025](https://arxiv.org/html/2602.03874v1#bib.bib29)) extend this analysis to demonstrate that stablecoin run dynamics exhibit centralization in arbitrage activity: during stress, redemption becomes concentrated among sophisticated actors, creating adverse selection that accelerates depegging.

The March 2023 Silicon Valley Bank crisis demonstrated bidirectional contagion between traditional and decentralized finance. Diop et al. ([2024](https://arxiv.org/html/2602.03874v1#bib.bib15)) document the USDC depeg following SVB’s collapse—the first major case of TradFi stress propagating into DeFi through stablecoin reserve exposure. Gross and Senner ([2026](https://arxiv.org/html/2602.03874v1#bib.bib21)) model fire sale scenarios under systemic stablecoin stress, while Eichengreen et al. ([2025](https://arxiv.org/html/2602.03874v1#bib.bib16)) develop a framework for quantifying devaluation risk across stablecoin designs.

### 2.4 DeFi-Specific Risks

The academic literature on DeFi risk is nascent but growing rapidly. Gudgeon et al. ([2020](https://arxiv.org/html/2602.03874v1#bib.bib22)) provide a systematization of DeFi protocol architectures, identifying liquidation cascades as a primary risk channel. Perez et al. ([2021](https://arxiv.org/html/2602.03874v1#bib.bib33)) analyze liquidation events across lending protocols, finding that liquidator competition can exacerbate price volatility during stress periods.

Werner et al. ([2022](https://arxiv.org/html/2602.03874v1#bib.bib37)) present a systematization of knowledge on DeFi covering lending, decentralized exchanges, and derivatives. They identify composability—the ability of protocols to permissionlessly interact through smart contract calls—as both a source of innovation and systemic vulnerability. When protocols share liquidity pools or collateral mechanisms, failures can propagate faster than human intervention can respond. Recent work on whitepaper-market alignment (Farzulla, [2025b](https://arxiv.org/html/2602.03874v1#bib.bib18)) suggests that stated protocol objectives may diverge from realized market behavior, creating additional opacity in risk assessment.

Recent work has deepened understanding of DeFi-specific systemic channels. Bartoletti et al. ([2022](https://arxiv.org/html/2602.03874v1#bib.bib6)) formalize composability risk through MEV (Maximal Extractable Value), demonstrating that protocol interactions create value extraction opportunities that destabilize liquidity during stress. Darlin et al. ([2022](https://arxiv.org/html/2602.03874v1#bib.bib11)) analyze debt-financed collateral structures, identifying leverage amplification mechanisms. Cross-chain bridge infrastructure represents acute vulnerability; Notland et al. ([2024](https://arxiv.org/html/2602.03874v1#bib.bib32)) systematize knowledge on bridge exploits, analyzing 60 bridges and 34 attacks (2021–2023) to identify 13 architectural components linked to 8 vulnerability types. Zhang et al. ([2025](https://arxiv.org/html/2602.03874v1#bib.bib38)) propose a correlation-based fragility indicator for detecting dangerous protocol synchronization.

### 2.5 Stablecoin Risk

Stablecoins occupy a critical position in DeFi infrastructure, serving as the primary medium of exchange and store of value across protocols. Lyons and Viswanath-Natraj ([2022](https://arxiv.org/html/2602.03874v1#bib.bib28)) analyze stablecoin run dynamics, finding that algorithmic stablecoins are particularly vulnerable to reflexive depegging spirals. The Terra/Luna collapse of May 2022 validated this theoretical concern empirically.

Gorton and Zhang ([2022](https://arxiv.org/html/2602.03874v1#bib.bib19)) frame stablecoins through the lens of 19th-century “wildcat banking,” where private currency issuance without adequate regulatory oversight led to periodic banking panics. They argue that stablecoin reserves require the same transparency and examination that bank reserves receive—a standard that most major stablecoins currently fail to meet.

De Blasis et al. ([2022](https://arxiv.org/html/2602.03874v1#bib.bib12)) conduct comparative performance analysis across the Terra, Celsius, and FTX episodes, finding that fiat-collateralized stablecoins exhibit more resilience than algorithmic designs. Antonakakis et al. ([2020](https://arxiv.org/html/2602.03874v1#bib.bib4)) introduce the TVP-VAR connectedness framework that enables measurement of time-varying spillover dynamics without arbitrary rolling-window selection—a methodological advance particularly relevant for cryptocurrency markets where structural breaks occur frequently.

### 2.6 Methodological Considerations

Two recent findings warrant consideration. First, Rapos and Fountas ([2025](https://arxiv.org/html/2602.03874v1#bib.bib35)) challenge the assumption of strong Bitcoin-equity market contagion, finding spillovers remain limited even during stress episodes. This finding does not invalidate contagion measurement but suggests correlation-based measures should be interpreted cautiously: elevated correlation may reflect common shocks rather than causal transmission. Second, Zhu ([2024](https://arxiv.org/html/2602.03874v1#bib.bib39)) present evidence via global game modeling that more precise private signals can paradoxically increase run probability when fundamentals are strong—potentially explaining why opaque stablecoins have exhibited stability despite theoretical expectations. This presents genuine tension for opacity measurement; future specifications should distinguish strategic opacity from information completeness.

### 2.7 Existing Crypto Risk Indices

Several commercial indices attempt to quantify cryptocurrency market risk:

Fear & Greed Index (Alternative.me, [2022](https://arxiv.org/html/2602.03874v1#bib.bib3)): Aggregates sentiment indicators (social media, volatility, dominance, trends) into a 0–100 scale. Limitation: purely sentiment-based with no fundamental risk component.

Crypto Climate Index (CCI): Combines on-chain metrics with market data. Limitation: focuses on individual asset health rather than systemic interconnection.

Glassnode Risk Assessment: Provides sophisticated on-chain analytics for Bitcoin and Ethereum. Limitation: asset-specific rather than ecosystem-wide; minimal DeFi coverage.

None of these indices systematically captures the DeFi-TradFi interconnection dynamics that ASRI is designed to monitor: stablecoin reserve composition, composable protocol dependencies, tokenized RWA linkages, or regulatory arbitrage exposure.

## 3 ASRI Framework

### 3.1 Conceptual Foundation

The ASRI framework rests on three theoretical principles:

Principle 1: Interconnection Creates Systemic Risk. Following Battiston et al. ([2012](https://arxiv.org/html/2602.03874v1#bib.bib7)), systemic risk arises not from the failure of individual nodes but from the propagation of distress through network connections. In DeFi, these connections manifest through shared collateral pools, composable protocol integrations, and token price correlations.

Principle 2: Risk Transmission Requires Channels. We identify four primary channels through which DeFi stress can propagate to traditional finance (and vice versa): stablecoin reserve linkages, tokenized RWA exposures, crypto-equity correlations, and regulatory enforcement actions. Each channel corresponds to an ASRI sub-index.

Principle 3: Opacity Amplifies Risk. Systemic risk is exacerbated when counterparties cannot accurately assess exposures. The prevalence of unaudited reserves, undisclosed custody arrangements, and regulatory arbitrage structures in crypto markets justifies a dedicated opacity sub-index.

Figure [1](https://arxiv.org/html/2602.03874v1#S3.F1 "Figure 1 ‣ 3.1 Conceptual Foundation ‣ 3 ASRI Framework") illustrates the ASRI architecture, showing how the four sub-indices aggregate into the composite risk measure.

Stablecoin Risk(30%)DeFi Liquidity Risk(25%)Contagion Risk(25%)Opacity Risk(20%)ASRI(0–100)Low <30<30 |Moderate 3030–5050 |Elevated 5050–7070 |High ≥70\geq 70


Figure 1: ASRI Framework Architecture: Four weighted sub-indices aggregate into a normalized composite risk measure with defined alert thresholds.

### 3.2 Axiomatic Foundation

We establish the formal properties that any coherent systemic risk index must satisfy, demonstrating that ASRI adheres to these axioms. Our axiomatic framework draws on the coherent risk measure literature (Artzner et al., [1999](https://arxiv.org/html/2602.03874v1#bib.bib5)) while extending it to the specific requirements of cryptocurrency market monitoring, where the absence of central counterparties and the prevalence of cross-venue arbitrage necessitate distinct aggregation properties.

###### Definition 3.1 (Systemic Risk Index).

Let 𝒮={S1,…,Sn}\mathcal{S}=\{S\_{1},\ldots,S\_{n}\} denote a set of sub-indices measuring distinct risk dimensions. A *systemic risk index* is a mapping ρ:𝒮→[0,100]\rho:\mathcal{S}\to[0,100] that aggregates component risks into a scalar measure of system-wide vulnerability.

For ASRI, we have 𝒮={SCR,DLR,CR,OR}\mathcal{S}=\{\text{SCR},\text{DLR},\text{CR},\text{OR}\} with the aggregation function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASRI​(𝒮)=∑i=14wi​Si,where ​∑i=14wi=1​ and ​wi>0​∀i\text{ASRI}(\mathcal{S})=\sum\_{i=1}^{4}w\_{i}S\_{i},\quad\text{where }\sum\_{i=1}^{4}w\_{i}=1\text{ and }w\_{i}>0\ \forall i |  | (1) |

We now state and verify five axioms that characterize well-behaved systemic risk indices.

###### Axiom 3.1 (Monotonicity).

For any sub-index Sj∈𝒮S\_{j}\in\mathcal{S}, if Sj′>SjS\_{j}^{\prime}>S\_{j} while Si′=SiS\_{i}^{\prime}=S\_{i} for all i≠ji\neq j, then ρ​(𝒮′)>ρ​(𝒮)\rho(\mathcal{S}^{\prime})>\rho(\mathcal{S}).

###### Proof.

Since wj>0w\_{j}>0 and the aggregation is linear:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASRI​(𝒮′)−ASRI​(𝒮)=wj​(Sj′−Sj)>0\text{ASRI}(\mathcal{S}^{\prime})-\text{ASRI}(\mathcal{S})=w\_{j}(S\_{j}^{\prime}-S\_{j})>0 |  | (2) |

The strict positivity of weights ensures that deterioration in any risk dimension is reflected in the aggregate index. This property is essential for regulatory monitoring, as it guarantees that localized stress cannot be masked by stability elsewhere—a concern raised by Adrian and Brunnermeier ([2016](https://arxiv.org/html/2602.03874v1#bib.bib2)) in their critique of institution-level VaR measures.
∎

###### Axiom 3.2 (Boundedness).

The index satisfies ρ​(𝒮)∈[0,100]\rho(\mathcal{S})\in[0,100] for all feasible states 𝒮\mathcal{S}.

###### Proof.

Each sub-index is constructed such that Si∈[0,100]S\_{i}\in[0,100] by design (see Appendix [A](https://arxiv.org/html/2602.03874v1#A1 "Appendix A Detailed Component Specifications")). Given convex weights summing to unity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∑i=14wi⋅0≤ASRI​(𝒮)≤∑i=14wi⋅100=1000=\sum\_{i=1}^{4}w\_{i}\cdot 0\leq\text{ASRI}(\mathcal{S})\leq\sum\_{i=1}^{4}w\_{i}\cdot 100=100 |  | (3) |

Boundedness facilitates interpretability and cross-temporal comparison, addressing the scaling criticisms leveled at unbounded measures such as raw CoVaR (Adrian and Brunnermeier, [2016](https://arxiv.org/html/2602.03874v1#bib.bib2)).
∎

###### Axiom 3.3 (Decomposability).

For any realization of ASRI, there exists a unique attribution {c1,…,cn}\{c\_{1},\ldots,c\_{n}\} such that ∑i=1nci=ASRI​(𝒮)\sum\_{i=1}^{n}c\_{i}=\text{ASRI}(\mathcal{S}) and cic\_{i} represents the contribution of sub-index SiS\_{i}.

###### Proof.

The linear structure immediately yields the efficiency-consistent additive decomposition ci=wi​Sic\_{i}=w\_{i}S\_{i}, satisfying:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=14ci=∑i=14wi​Si=ASRI​(𝒮)\sum\_{i=1}^{4}c\_{i}=\sum\_{i=1}^{4}w\_{i}S\_{i}=\text{ASRI}(\mathcal{S}) |  | (4) |

This decomposition is unique and satisfies the efficiency axiom of cooperative game theory. Decomposability enables regulators to identify which risk channel—spillover, liquidity, concentration, or operational—drives aggregate stress, facilitating targeted intervention. This property aligns with the “risk contribution” framework of Acharya et al. ([2017](https://arxiv.org/html/2602.03874v1#bib.bib1)) for measuring systemic expected shortfall.
∎

###### Axiom 3.4 (Aggregation Neutrality).

Linear aggregation preserves ordinal rankings: if 𝒮A\mathcal{S}^{A} and 𝒮B\mathcal{S}^{B} represent two market states with SiA≥SiBS\_{i}^{A}\geq S\_{i}^{B} for all ii and strict inequality for at least one jj, then ρ​(𝒮A)>ρ​(𝒮B)\rho(\mathcal{S}^{A})>\rho(\mathcal{S}^{B}).

###### Proof.

Under the stated conditions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASRI​(𝒮A)−ASRI​(𝒮B)=∑i=14wi​(SiA−SiB)≥wj​(SjA−SjB)>0\text{ASRI}(\mathcal{S}^{A})-\text{ASRI}(\mathcal{S}^{B})=\sum\_{i=1}^{4}w\_{i}(S\_{i}^{A}-S\_{i}^{B})\geq w\_{j}(S\_{j}^{A}-S\_{j}^{B})>0 |  | (5) |

Aggregation neutrality ensures that Pareto-dominated risk states are correctly ranked, preventing the pathological reversals that can arise with nonlinear aggregation schemes (Battiston et al., [2012](https://arxiv.org/html/2602.03874v1#bib.bib7)). This property is particularly relevant for cryptocurrency markets, where rapid regime shifts demand consistent ordinal comparisons across time.
∎

###### Axiom 3.5 (Concentration Sensitivity).

Let HHIt\text{HHI}\_{t} denote the Herfindahl-Hirschman Index of market concentration at time tt. The index satisfies ∂ρ/∂HHIt>0\partial\rho/\partial\text{HHI}\_{t}>0 when concentration risk is elevated.

###### Proof.

The Stablecoin Risk sub-index (SCR) and DeFi Liquidity Risk sub-index (DLR) explicitly incorporate HHI components measuring stablecoin and protocol concentration respectively. By Axiom [3.1](https://arxiv.org/html/2602.03874v1#S3.Thmaxiom1 "Axiom 3.1 (Monotonicity). ‣ 3.2 Axiomatic Foundation ‣ 3 ASRI Framework"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ASRI∂HHIt=wSCR⋅∂SCRt∂HHIt+wDLR⋅∂DLRt∂HHIt>0\frac{\partial\text{ASRI}}{\partial\text{HHI}\_{t}}=w\_{\text{SCR}}\cdot\frac{\partial\text{SCR}\_{t}}{\partial\text{HHI}\_{t}}+w\_{\text{DLR}}\cdot\frac{\partial\text{DLR}\_{t}}{\partial\text{HHI}\_{t}}>0 |  | (6) |

Concentration sensitivity captures the “too-interconnected-to-fail” dynamics emphasized by Battiston et al. ([2012](https://arxiv.org/html/2602.03874v1#bib.bib7)), adapted here to the exchange-centric topology of cryptocurrency markets where a single venue failure can trigger system-wide contagion, as observed during the FTX collapse of November 2022.
∎

##### Relationship to Coherent Risk Measures.

While ASRI is not a coherent risk measure in the sense of Artzner et al. ([1999](https://arxiv.org/html/2602.03874v1#bib.bib5))—it aggregates sub-indices rather than loss distributions—our axiomatic foundation parallels their framework. Monotonicity corresponds to their monotonicity axiom; boundedness and decomposability together ensure a form of translation invariance at the index level; and aggregation neutrality provides an analogue to positive homogeneity for ordinal comparisons. The key distinction is that ASRI operates on observable market indicators rather than probabilistic loss distributions, making it implementable in real-time without parametric assumptions—a practical advantage for monitoring the 24/7 cryptocurrency market.

### 3.3 Weight Selection Justification

Sub-index weights were selected based on theoretical importance and precedent from traditional systemic risk literature:

* •

  Stablecoin Concentration Risk (30%): Stablecoins are the foundational liquidity layer for DeFi. Their failure would immediately impact all protocols dependent on stablecoin-denominated liquidity pools. The highest weight reflects this critical infrastructure role.
* •

  DeFi Liquidity Risk (25%): Protocol concentration and leverage dynamics directly determine the ecosystem’s resilience to market stress. Empirical analysis (Section [5.5](https://arxiv.org/html/2602.03874v1#S5.SS5 "5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation")) reveals that DLR serves as the primary early-warning signal during stress periods.
* •

  Contagion Risk (25%): DeFi-TradFi linkages represent the primary channel through which crypto stress could affect traditional finance (and vice versa). Equal weighting with DLR reflects their complementary roles: DLR captures within-DeFi stress, while CR captures cross-market transmission.
* •

  Opacity Risk (20%): While important, opacity is an amplifying factor rather than a primary risk driver. Lower weight reflects this secondary role in conditioning crisis severity rather than triggering crises.

Sensitivity analysis (Section [5.9](https://arxiv.org/html/2602.03874v1#S5.SS9 "5.9 Sensitivity Analysis ‣ 5 Empirical Validation")) tests robustness to alternative weight specifications. Section [5.5](https://arxiv.org/html/2602.03874v1#S5.SS5 "5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation") compares theoretical weights against data-driven alternatives derived through PCA and Elastic Net regression, developing a trigger-amplifier interpretation that reconciles theoretical structure with empirical reality: DLR acts as the leading indicator, SCR and CR capture crisis-type-specific transmission channels, and OR amplifies stress severity. Figure [2](https://arxiv.org/html/2602.03874v1#S3.F2 "Figure 2 ‣ 3.3 Weight Selection Justification ‣ 3 ASRI Framework") visualizes this decomposition empirically, showing how each sub-index contribution evolves over the sample period.

![Refer to caption](x1.png)


Figure 2: ASRI Decomposition by Sub-Index Contribution Over Time. Stacked area chart showing how Stablecoin Risk (SCR, 30%), DeFi Liquidity Risk (DLR, 25%), Contagion Risk (CR, 25%), and Arbitrage Opacity (OR, 20%) contribute to the aggregate ASRI. The decomposition property guarantees ci=wi​Sic\_{i}=w\_{i}S\_{i} such that total area equals ASRI at each time point. During crisis periods, shifting relative contributions reveal which transmission channels dominate aggregate stress.

### 3.4 Stablecoin Concentration Risk (30%)

The Stablecoin Risk sub-index captures reserve composition vulnerabilities, peg stability, and concentration across issuers:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SCRt=0.4⋅TVLt+0.3⋅Treasuryt+0.2⋅HHIt+0.1⋅Volt\text{SCR}\_{t}=0.4\cdot\text{TVL}\_{t}+0.3\cdot\text{Treasury}\_{t}+0.2\cdot\text{HHI}\_{t}+0.1\cdot\text{Vol}\_{t} |  | (7) |

where:

* •

  TVLt=1−Stablecoin TVLtmaxτ≤t⁡(Stablecoin TVLτ)\text{TVL}\_{t}=1-\frac{\text{Stablecoin TVL}\_{t}}{\max\_{\tau\leq t}(\text{Stablecoin TVL}\_{\tau})} measures stablecoin TVL drawdown from historical maximum—declining TVL increases risk111The inversion ensures countercyclical behavior: when TVL collapses during crises, TVLt rises toward 1 (high risk); at historical peak, TVL=t0{}\_{t}=0 (low risk). See Appendix [A](https://arxiv.org/html/2602.03874v1#A1 "Appendix A Detailed Component Specifications") for implementation details.
* •

  Treasuryt=T-Bill ReservestTotal Stablecoin Reservest\text{Treasury}\_{t}=\frac{\text{T-Bill Reserves}\_{t}}{\text{Total Stablecoin Reserves}\_{t}} captures Treasury exposure concentration
* •

  HHIt=∑i=1nsi2\text{HHI}\_{t}=\sum\_{i=1}^{n}s\_{i}^{2} is the Herfindahl-Hirschman Index of stablecoin market share concentration
* •

  Volt\text{Vol}\_{t} is the 30-day realized volatility of weighted-average stablecoin peg deviation

Data Sources: DeFi Llama (stablecoin TVL), attestation reports (reserve composition), CoinGecko (price feeds for volatility calculation).

### 3.5 DeFi Liquidity Risk (25%)

The DeFi Liquidity sub-index captures protocol concentration, leverage dynamics, and smart contract vulnerability:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DLRt=0.35⋅Conct+0.25⋅TVLVolt+0.20⋅SCt+0.10⋅Flasht+0.10⋅Levt\begin{split}\text{DLR}\_{t}={}&0.35\cdot\text{Conc}\_{t}+0.25\cdot\text{TVLVol}\_{t}\\ &+0.20\cdot\text{SC}\_{t}+0.10\cdot\text{Flash}\_{t}+0.10\cdot\text{Lev}\_{t}\end{split} |  | (8) |

where:

* •

  Conct\text{Conc}\_{t} is the HHI of TVL across top-10 DeFi protocols
* •

  TVLVolt\text{TVLVol}\_{t} is the 30-day volatility of total DeFi TVL
* •

  SCt\text{SC}\_{t} is a composite smart contract risk score based on audit status, time since deployment, and exploit history
* •

  Flasht\text{Flash}\_{t} measures flash loan volume spikes relative to 90-day average
* •

  Levt\text{Lev}\_{t} captures 30-day change in aggregate leverage ratios across lending protocols

Data Sources: DeFi Llama (TVL, protocol data), Token Terminal (flash loan data), DefiSafety (audit scores).

### 3.6 Contagion Risk (25%)

The Contagion Risk sub-index quantifies DeFi-TradFi linkage intensity and cross-market transmission channels:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CRt=0.30⋅RWAt+0.25⋅Bankt+0.20⋅Linkt+0.15⋅Corrt+0.10⋅Bridget\begin{split}\text{CR}\_{t}={}&0.30\cdot\text{RWA}\_{t}+0.25\cdot\text{Bank}\_{t}\\ &+0.20\cdot\text{Link}\_{t}+0.15\cdot\text{Corr}\_{t}+0.10\cdot\text{Bridge}\_{t}\,\end{split} |  | (9) |

where:

* •

  RWAt\text{RWA}\_{t} is the 30-day growth rate of tokenized real-world asset TVL
* •

  Bankt\text{Bank}\_{t} is a normalized score of bank crypto exposure from regulatory filings (OCC, ECB)
* •

  Linkt\text{Link}\_{t} measures stablecoin flows to TradFi-connected entities
* •

  Corrt\text{Corr}\_{t} is the 30-day rolling correlation between BTC/ETH and S&P 500
* •

  Bridget\text{Bridge}\_{t} is a composite of cross-chain bridge volume and recent exploit frequency

Data Sources: RWA.xyz (tokenized assets), DeFi Llama (bridge data), FRED (equity indices), regulatory filings.

Implementation Note: Bankt and Linkt are implemented as high-frequency proxies because quarterly regulatory filings have 45–90 day publication lags. Bankt uses a Treasury-VIX composite; Linkt uses yield curve spread. These proxies capture the same underlying stress dynamics at daily frequency (see Appendix [A](https://arxiv.org/html/2602.03874v1#A1 "Appendix A Detailed Component Specifications") for full specification and Table [37](https://arxiv.org/html/2602.03874v1#A1.T37 "Table 37 ‣ A.6.3 Proxy Acknowledgments ‣ A.6 Data Quality and Limitations ‣ Appendix A Detailed Component Specifications") for proxy validation).

### 3.7 Regulatory Opacity Risk (20%)

The Opacity Risk sub-index assesses transparency deficits and regulatory arbitrage exposure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ORt=0.25⋅Unregt+0.25⋅Multit+0.20⋅Custt+0.15⋅Sentt+0.15⋅Transt\begin{split}\text{OR}\_{t}={}&0.25\cdot\text{Unreg}\_{t}+0.25\cdot\text{Multi}\_{t}\\ &+0.20\cdot\text{Cust}\_{t}+0.15\cdot\text{Sent}\_{t}+0.15\cdot\text{Trans}\_{t}\,\end{split} |  | (10) |

where:

* •

  Unregt\text{Unreg}\_{t} is the ratio of unregulated to regulated platform volume
* •

  Multit\text{Multi}\_{t} captures multi-issuer stablecoin scheme exposure
* •

  Custt\text{Cust}\_{t} is custody concentration in non-audited jurisdictions
* •

  Sentt\text{Sent}\_{t} is regulatory sentiment score from NLP analysis of SEC/ESRB/FSB announcements
* •

  Transt\text{Trans}\_{t} is a composite transparency score based on reserve attestation frequency and coverage

Data Sources: Regulatory filings, news APIs (GDELT), attestation calendars, manual tracking.

### 3.8 Aggregate ASRI Calculation

The final ASRI is computed as a weighted sum of normalized sub-indices:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASRIt=0.30⋅SCRt+0.25⋅DLRt+0.25⋅CRt+0.20⋅ORt\text{ASRI}\_{t}=0.30\cdot\text{SCR}\_{t}+0.25\cdot\text{DLR}\_{t}+0.25\cdot\text{CR}\_{t}+0.20\cdot\text{OR}\_{t} |  | (11) |

Normalization uses min-max scaling over the historical sample to produce a 0–100 index:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASRItnorm=100×ASRIt−minτ⁡(ASRIτ)maxτ⁡(ASRIτ)−minτ⁡(ASRIτ)\text{ASRI}^{\text{norm}}\_{t}=100\times\frac{\text{ASRI}\_{t}-\min\_{\tau}(\text{ASRI}\_{\tau})}{\max\_{\tau}(\text{ASRI}\_{\tau})-\min\_{\tau}(\text{ASRI}\_{\tau})} |  | (12) |

Note that sub-index construction (Equations [7](https://arxiv.org/html/2602.03874v1#S3.E7 "In 3.4 Stablecoin Concentration Risk (30%) ‣ 3 ASRI Framework")–[10](https://arxiv.org/html/2602.03874v1#S3.E10 "In 3.7 Regulatory Opacity Risk (20%) ‣ 3 ASRI Framework")) ensures component values fall within [0,100][0,100] by design through normalized ratios and bounded indicators, making post-hoc min-max normalization unnecessary in practice. Equation 6 documents the theoretical relationship between raw and normalized values; empirical analyses in Section 5 use raw weighted aggregates directly. Collinearity among sub-indices is assessed via Variance Inflation Factors and condition number analysis (Section [5.5.2](https://arxiv.org/html/2602.03874v1#S5.SS5.SSS2 "5.5.2 Collinearity Diagnostics ‣ 5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation")); all diagnostics confirm linear aggregation is well-conditioned.

Alert Thresholds:

* •

  ASRI<30\text{ASRI}<30: Low systemic risk
* •

  30≤ASRI<5030\leq\text{ASRI}<50: Moderate systemic risk
* •

  50≤ASRI<7050\leq\text{ASRI}<70: Elevated systemic risk
* •

  ASRI≥70\text{ASRI}\geq 70: High systemic risk

Operational Alert Rule: An alert is triggered when ASRI ≥50\geq 50 (Elevated threshold) for at least one trading day. No persistence requirement is imposed because crisis dynamics can evolve rapidly; however, practitioners may implement confirmation windows (e.g., 3-day persistence) to reduce noise at the cost of lead time. Threshold selection follows a precision-recall trade-off documented in Table [8](https://arxiv.org/html/2602.03874v1#S5.T8 "Table 8 ‣ 5.4.4 False Positive Analysis ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation"): the 50 threshold maximizes recall (100% crisis detection) while accepting moderate precision (12.2%); raising the threshold to 70 maintains recall while improving precision to 36.5%. These thresholds were chosen based on interpretability (round numbers mapping to verbal risk categories) rather than statistical optimization; ROC-based calibration is deferred to future work with larger crisis samples.

## 4 Data and Implementation

### 4.1 Data Sources

Table [1](https://arxiv.org/html/2602.03874v1#S4.T1 "Table 1 ‣ 4.1 Data Sources ‣ 4 Data and Implementation") summarizes the data sources for each ASRI component.

Table 1: ASRI Data Sources by Sub-Index

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Sub-Index | Component | Source | Frequency | Tier |
| Stablecoin Risk | TVL | DeFi Llama | Daily | 1 |
| Treasury Reserves | Attestation Reports | Monthly | 2 |
| Market Share | CoinGecko | Daily | 1 |
| Peg Volatility | CoinGecko | Daily | 1 |
| DeFi Liquidity | Protocol TVL | DeFi Llama | Daily | 1 |
| Flash Loan Volume | Token Terminal | Daily | 1 |
| Smart Contract Scores | DefiSafety | Weekly | 2 |
| Leverage Ratios | DeFi Llama | Daily | 1 |
| Bridge Volume | DeFi Llama | Daily | 1 |
| Contagion Risk | RWA TVL | RWA.xyz / DeFi Llama | Daily | 1 |
| Bank Exposure | OCC/ECB Filings | Quarterly | 2 |
| TradFi Linkages | On-chain Analysis | Weekly | 2 |
| Equity Correlation | FRED/Yahoo Finance | Daily | 1 |
| Bridge Exploits | DeFi Llama | Daily | 1 |
| Opacity Risk | Platform Regulation | Manual Tracking | Weekly | 2 |
| Custody Concentration | Public Disclosures | Monthly | 2 |
| Regulatory Sentiment | GDELT/SEC Filings | Daily | 2 |
| Attestation Frequency | Calendar Tracking | Daily | 2 |
| Transparency Scores | DefiSafety | Weekly | 2 |

Abbreviations: TVL = Total Value Locked; RWA = Real-World Assets; OCC = Office of the Comptroller of the Currency; ECB = European Central Bank; GDELT = Global Database of Events, Language, and Tone; SEC = Securities and Exchange Commission.

Tier 1 sources provide daily automated API access; Tier 2 sources require manual collection, web scraping, or have lower update frequency.

### 4.2 Data Quality Framework

Missing data is handled according to the following protocol:

* •

  Daily data gaps (<< 3 days): Linear interpolation with confidence score 0.7
* •

  Extended gaps (3–7 days): Forward-fill with confidence score 0.5
* •

  Gaps >> 7 days: Flag as unreliable; exclude from ASRI calculation until fresh data available

Data lag assumptions follow the t−1t-1 convention: values observed at midnight UTC on date tt are attributed to ASRIt-1 to avoid look-ahead bias.222To ensure backtests use only real-time information, min-max bounds in Equation 6 are theoretical; empirical analyses use raw ASRI values computed from bounded sub-indices without full-sample normalization.

##### Mixed-Frequency Data Protocol.

Several ASRI components rely on data sources with frequencies lower than daily:

* •

  Quarterly sources (OCC/ECB bank exposure filings): Replaced with high-frequency proxies. Bankt uses a Treasury yield + VIX composite that captures the same underlying stress dynamics at daily frequency (Appendix [A](https://arxiv.org/html/2602.03874v1#A1 "Appendix A Detailed Component Specifications")).
* •

  Monthly sources (stablecoin attestations): Last observation carried forward until new attestation published; component flagged with reduced confidence (0.6) after 45 days.
* •

  Weekly sources (on-chain linkage metrics): Linear interpolation between weekly observations for daily estimation; confidence score 0.8.

This approach prioritizes real-time operationality over theoretical purity: where high-frequency proxies exist (e.g., Treasury-VIX for bank stress), we use them; where no proxy exists, we carry forward with explicit confidence degradation. The pseudo-real-time evaluation (Section [5.13](https://arxiv.org/html/2602.03874v1#S5.SS13 "5.13 Pseudo-Real-Time Evaluation ‣ 5 Empirical Validation")) confirms that this protocol preserves detection performance under realistic publication lags.

### 4.3 Technical Architecture

The ASRI system architecture comprises four layers:

1. 1.

   Ingestion Layer: Python-based API clients and web scrapers fetch data from sources
2. 2.

   Normalization Layer: Raw data undergoes unit normalization, gap-filling, and validation
3. 3.

   Computation Layer: Sub-indices calculated using Equations [7](https://arxiv.org/html/2602.03874v1#S3.E7 "In 3.4 Stablecoin Concentration Risk (30%) ‣ 3 ASRI Framework")–[10](https://arxiv.org/html/2602.03874v1#S3.E10 "In 3.7 Regulatory Opacity Risk (20%) ‣ 3 ASRI Framework"); aggregate ASRI computed via Equation [11](https://arxiv.org/html/2602.03874v1#S3.E11 "In 3.8 Aggregate ASRI Calculation ‣ 3 ASRI Framework")
4. 4.

   Publication Layer: FastAPI REST endpoints serve current and historical ASRI values; React dashboard provides visualization

Figure [3](https://arxiv.org/html/2602.03874v1#S4.F3 "Figure 3 ‣ 4.3 Technical Architecture ‣ 4 Data and Implementation") illustrates the data flow through these layers.

DeFi LlamaFREDToken TerminalOther APIs1. Ingestion | API Clients + Scrapers2. Normalization | Validation + Gap-fill3. Computation | Sub-indices → ASRI4. Publication | REST API + DashboardStorage: PostgreSQL + TimescaleDB


Figure 3: ASRI Data Pipeline: Four-layer architecture from API ingestion to public dashboard publication.

Technology Stack: Python 3.11+, PostgreSQL with TimescaleDB, FastAPI, React/TypeScript, Docker Compose.

Full implementation is available at [github.com/studiofarzulla/asri](https://github.com/studiofarzulla/asri).

## 5 Empirical Validation

This section presents the empirical validation of the ASRI framework against historical data from January 2021 through January 2026, comprising over 1,800 daily observations across four major in-sample crisis events and out-of-sample specificity testing on 2024–2025 data.

### 5.1 Crisis Taxonomy and Operational Definitions

Before proceeding to empirical validation, we establish operational definitions for what constitutes a systemic crisis in cryptocurrency markets. This taxonomy serves two purposes: providing ex ante criteria for event identification (avoiding post hoc selection bias) and enabling systematic classification of crisis mechanisms.

#### 5.1.1  Operational Crisis Definition

Following the crisis identification methodology of Laeven and Valencia ([2013](https://arxiv.org/html/2602.03874v1#bib.bib25)) and adapted for high-frequency digital asset markets, we define a systemic stress event as satisfying three jointly necessary conditions:

###### Definition 5.1 (Systemic Stress Event).

A period [t0,t1][t\_{0},t\_{1}] constitutes a systemic stress event if and only if:

1. (i)

   Magnitude: Aggregate market capitalization decline ≥15%\geq 15\% within a 7-day window, or single-asset collapse ≥50%\geq 50\% for assets with market cap ≥$​10\geq\mathdollar 10B;
2. (ii)

   Contagion: Cross-asset correlation surge, measured as ρ¯t−ρ¯t−30≥0.20\bar{\rho}\_{t}-\bar{\rho}\_{t-30}\geq 0.20 where ρ¯\bar{\rho} denotes the mean pairwise correlation across major assets;
3. (iii)

   Duration: Elevated stress conditions persist for ≥5\geq 5 trading days, distinguishing systemic events from flash crashes.

This definition deliberately excludes stress episodes—periods of elevated volatility without systemic propagation. For instance, single-asset drawdowns (e.g., meme coin collapses) or brief correlation spikes during scheduled events (FOMC announcements) fail condition (ii) or (iii) respectively. The thresholds are calibrated to cryptocurrency market dynamics; traditional finance definitions (e.g., Reinhart and Rogoff, [2009](https://arxiv.org/html/2602.03874v1#bib.bib36)) typically require banking sector involvement, which maps imperfectly to decentralized systems.

#### 5.1.2  Crisis Typology

We classify systemic events along two dimensions: origin (endogenous vs. exogenous) and primary transmission mechanism (liquidity vs. solvency). This yields a typology summarized in Table [2](https://arxiv.org/html/2602.03874v1#S5.T2 "Table 2 ‣ 5.1.2 Crisis Typology ‣ 5.1 Crisis Taxonomy and Operational Definitions ‣ 5 Empirical Validation").

Table 2: Crisis Typology for Cryptocurrency Markets

| Type | Characteristics | Historical Examples |
| --- | --- | --- |
| Type I: Endogenous | Originates within DeFi/crypto ecosystem; propagates through on-chain liquidity channels, collateral cascades, or protocol failures | Terra/Luna (May 2022): algorithmic stablecoin death spiral triggering $40B TVL collapse |
| Type II: Exogenous | External shock (TradFi, regulatory, macroeconomic) propagates into crypto markets through stablecoin pegs, institutional exposure, or sentiment channels | SVB Crisis (March 2023): banking contagion →\rightarrow USDC depeg →\rightarrow DeFi stress |
| Type III: Hybrid | Combined dynamics—crypto-native entity failures with significant TradFi counterparty exposure amplifying propagation | Celsius/3AC (June 2022); FTX (November 2022): CeFi insolvencies with cross-market contagion |

The four validation events span all three types, providing heterogeneous test conditions. Notably, Type III events (Celsius/3AC, FTX) exhibit the longest stress durations in our sample, consistent with Brunnermeier ([2009](https://arxiv.org/html/2602.03874v1#bib.bib10))’s observation that hybrid crises produce more persistent dislocation due to opacity in cross-market exposures.

#### 5.1.3  Detection versus Prediction

A critical methodological distinction: ASRI is designed as a detection instrument with leading properties, not a pure prediction model. Following Borio and Drehmann ([2009](https://arxiv.org/html/2602.03874v1#bib.bib8)), we distinguish:

* •

  Detection: Contemporaneous identification that systemic stress is occurring or imminent (hours to days horizon). Validation criterion: Does ASRI breach threshold τ\tau before or coincident with observable market stress?
* •

  Prediction: Forecasting crisis probability over medium horizons (weeks to months). Would require different validation methodology (e.g., receiver operating characteristic analysis, out-of-sample forecasting).

Our empirical validation focuses on detection performance: lead time relative to price cascade initiation, signal persistence during stress periods, and false positive rates during non-crisis windows. The lead times documented below reflect ASRI’s design as an early warning system for active risk management rather than a long-horizon forecasting tool.

##### Measurement Definitions.

For consistency across all empirical analyses, we define:

* •

  Detection threshold: ASRI ≥50\geq 50 (“Elevated” risk category). A crisis is detected if ASRI exceeds this threshold on any day in the 30-day pre-crisis window.
* •

  Lead time (threshold-based): Days between the first threshold crossing (ASRI ≥50\geq 50) and crisis onset (t=0t=0, defined as price cascade initiation).
* •

  Lead time (event study): Days between first observation where ASRI exceeds 1.5 standard deviations above the estimation-window mean and crisis onset. This captures early stress signals relative to the pre-event baseline.
* •

  Crisis onset (t=0t=0): The first trading day exhibiting observable price cascade—typically a 10%+ single-day decline in major assets or stablecoin depeg initiation.
* •

  False positive: Any day where ASRI ≥50\geq 50 outside of the [−30,+30][-30,+30] window surrounding a validated crisis event.

All hypothesis tests are two-tailed at α=0.05\alpha=0.05 unless otherwise specified. Confidence intervals are reported as 95% intervals using bootstrap resampling (1,000 iterations) for detection rates and analytical standard errors for regression coefficients.

### 5.2 Data and Sample

Table [3](https://arxiv.org/html/2602.03874v1#S5.T3 "Table 3 ‣ 5.2 Data and Sample ‣ 5 Empirical Validation") presents descriptive statistics for ASRI and its component sub-indices.

Table 3: Descriptive Statistics of ASRI Components

| Variable | NN | Mean | Std | Min | Max | Skew |
| --- | --- | --- | --- | --- | --- | --- |
| ASRI | 1,841 | 39.2 | 7.8 | 25.8 | 84.7 | 1.46 |
| Stablecoin Risk | 1,841 | 35.5 | 9.1 | 14.0 | 78.2 | 0.27 |
| DeFi Liquidity | 1,841 | 42.3 | 7.5 | 27.9 | 90.0 | 1.79 |
| Contagion Risk | 1,841 | 39.1 | 13.8 | 12.1 | 87.9 | −-0.34 |
| Opacity Risk | 1,841 | 36.9 | 6.9 | 22.6 | 70.2 | 0.77 |

* •

  Sample: January 2021 – January 2026 (daily).

The ASRI ranges from 25.8 (low risk) to 84.7 (elevated risk during the FTX crisis), with crisis periods driving the upper tail. Positive skewness (1.46) reflects the asymmetric distribution: most observations cluster in the moderate band (30–50) while systemic stress events generate right-tail outliers, consistent with the design objective of early warning rather than tail risk measurement.

Figure [4](https://arxiv.org/html/2602.03874v1#S5.F4 "Figure 4 ‣ 5.2 Data and Sample ‣ 5 Empirical Validation") presents the complete ASRI timeseries from January 2021 through January 2026, with the four validated crisis events annotated and operational risk regime bands indicated.

![Refer to caption](x2.png)


Figure 4: ASRI Index Timeseries (January 2021 – January 2026). Shaded bands denote operational risk regimes: Low (<<30), Elevated (30–50), High (50–70), and Critical (>>70). Vertical dashed lines mark crisis event onsets: Terra/Luna collapse (May 2022), Celsius/3AC contagion (June 2022), FTX collapse (November 2022), and SVB banking crisis (March 2023). The index exhibits characteristic spikes during stress periods with rapid mean-reversion during recovery phases.

The visual pattern confirms the statistical properties reported in Table [3](https://arxiv.org/html/2602.03874v1#S5.T3 "Table 3 ‣ 5.2 Data and Sample ‣ 5 Empirical Validation"): the index spends most of its time in the Low-to-Elevated bands (25–50), with transient spikes into High and Critical zones during the four major crises.

### 5.3 Stationarity Tests

Valid time series analysis requires stationary sub-indices. Table [4](https://arxiv.org/html/2602.03874v1#S5.T4 "Table 4 ‣ 5.3 Stationarity Tests ‣ 5 Empirical Validation") reports Augmented Dickey-Fuller (ADF) and KPSS test results.

Table 4: Stationarity Test Results

| Variable | ADF Stat | ADF pp | KPSS | Conclusion |
| --- | --- | --- | --- | --- |
| ASRI | −-5.22 | <<0.001 | 0.31 | Stationary |
| Stablecoin Risk | −-3.76 | 0.003 | 1.13 | Trend-stat. |
| DeFi Liquidity | −-4.34 | <<0.001 | 0.11 | Stationary |
| Contagion Risk | −-3.71 | 0.004 | 0.89 | Trend-stat. |
| Opacity Risk | −-4.33 | <<0.001 | 0.45 | Stationary |

* •

  ADF: Augmented Dickey-Fuller (lag selection via AIC, intercept included); KPSS: Kwiatkowski-Phillips-Schmidt-Shin (Bartlett kernel, automatic bandwidth).
* •

  KPSS critical values: 0.463 (5%), 0.739 (1%). Values exceeding 0.739 indicate trend-stationarity.
* •

  All series reject unit root at 1% level. Two series exhibit deterministic trends.

All five series reject the unit root hypothesis (ADF p<0.01p<0.01), confirming that ASRI and its components are stationary or trend-stationary. This validates the use of level-based analysis without differencing.

### 5.4 Event Study Analysis

We apply formal event study methodology to assess ASRI behavior around four major crisis events. Following MacKinlay ([1997](https://arxiv.org/html/2602.03874v1#bib.bib30)), we estimate “normal” ASRI levels from a 60-day estimation window and compute Cumulative Abnormal Signal (CAS) over the event window.333Unlike asset returns, ASRI is bounded on [0,100][0,100]. However, large-sample inference remains valid under the central limit theorem; the bounded support makes distributional assumptions less critical than in return-based event studies.

#### 5.4.1  Event Study Specification

Normal Model. We employ a constant mean model for expected ASRI during the estimation window:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ASRIt]=μ^=1Test​∑τ=−90−31ASRIτ\mathbb{E}[\text{ASRI}\_{t}]=\hat{\mu}=\frac{1}{T\_{\text{est}}}\sum\_{\tau=-90}^{-31}\text{ASRI}\_{\tau} |  | (13) |

where the estimation window spans t=−90t=-90 to t=−31t=-31 relative to the event date (60 trading days), providing a pre-event baseline uncontaminated by crisis dynamics.

Abnormal Signal. The abnormal signal on day tt is defined as the deviation from the expected level:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASt=ASRIt−𝔼​[ASRIt]=ASRIt−μ^\text{AS}\_{t}=\text{ASRI}\_{t}-\mathbb{E}[\text{ASRI}\_{t}]=\text{ASRI}\_{t}-\hat{\mu} |  | (14) |

The Cumulative Abnormal Signal (CAS) aggregates abnormal signals over the event window [t1,t2][t\_{1},t\_{2}]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CAS[t1,t2]=∑t=t1t2ASt\text{CAS}\_{[t\_{1},t\_{2}]}=\sum\_{t=t\_{1}}^{t\_{2}}\text{AS}\_{t} |  | (15) |

We use an event window of [t1,t2]=[−30,+10][t\_{1},t\_{2}]=[-30,+10], capturing the pre-crisis buildup period and immediate aftermath.

Variance Estimation. The variance of the abnormal signal is estimated from the estimation window:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^AS2=1Test−1​∑τ=−90−31(ASRIτ−μ^)2\hat{\sigma}^{2}\_{\text{AS}}=\frac{1}{T\_{\text{est}}-1}\sum\_{\tau=-90}^{-31}\left(\text{ASRI}\_{\tau}-\hat{\mu}\right)^{2} |  | (16) |

Under the assumption of independent abnormal signals, the standard error of CAS is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SE​(CAS)=σ^AS×Tevent\text{SE}(\text{CAS})=\hat{\sigma}\_{\text{AS}}\times\sqrt{T\_{\text{event}}} |  | (17) |

where Tevent=41T\_{\text{event}}=41 is the length of the event window. Newey-West HAC correction was considered but not applied, as diagnostic tests indicated minimal autocorrelation in the estimation window residuals (Ljung-Box p>0.10p>0.10 for all events).

Test Statistic. Under the null hypothesis of no abnormal signal (H0H\_{0}: CAS =0=0), the test statistic is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t=CASSE​(CAS)∼tTest−1t=\frac{\text{CAS}}{\text{SE}(\text{CAS})}\sim t\_{T\_{\text{est}}-1} |  | (18) |

which follows a tt-distribution with Test−1=59T\_{\text{est}}-1=59 degrees of freedom under standard regularity conditions.

Window Independence. The four crisis events are sufficiently separated in time to ensure non-overlapping estimation and event windows:

* •

  Terra/Luna (May 2022): Estimation window February–April 2022
* •

  Celsius/3AC (June 2022): Estimation window March–May 2022
* •

  FTX Collapse (November 2022): Estimation window August–October 2022
* •

  SVB Crisis (March 2023): Estimation window December 2022–February 2023

The Celsius/3AC and Terra/Luna events have minimal overlap in their event windows (approximately 10 days), but estimation windows remain independent. The FTX and SVB events are fully separated by over 90 days.

##### Lead Time Measurement.

Lead time is measured as days between the first observation where ASRI exceeds 1.5 standard deviations above the estimation-window mean and crisis onset. This definition captures early stress signals relative to the baseline rather than fixed threshold breaches, allowing detection of abnormality even when absolute levels remain below operational thresholds.

#### 5.4.2  Event Study Results

Table 5: Event Study Results: ASRI Response to Crisis Events

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Event | Date | Pre-Mean | Peak | CAS | tt-stat | Lead |
| Terra/Luna | 2022-05 | 40.4 | 48.7 | 100.3\*\*\* | 5.47 | 30 |
| Celsius/3AC | 2022-06 | 42.6 | 71.4 | 521.6\*\*\* | 29.78 | 30 |
| FTX Collapse | 2022-11 | 39.6 | 84.7 | 758.8\*\*\* | 32.64 | 30 |
| SVB Crisis | 2023-03 | 41.0 | 68.7 | 509.0\*\*\* | 26.91 | 29 |
| Significant events: 4/4 (100%); Average lead time: 30 days; Average CAS: 472.4 | | | | | | |

* •

  CAS = Cumulative Abnormal Signal. Lead = days between *final sustained* threshold crossing and event onset.
* •

  \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.10p<0.10

All four crisis events produce highly significant abnormal ASRI elevations (tt-statistics ranging from 5.47 to 32.64, all p<0.01p<0.01). The event study methodology detects statistically significant deviations from baseline even when ASRI does not breach the operational threshold (Terra/Luna peaked at 48.7, below the 50 threshold).

Interpretation: The event study confirms that ASRI captures crisis-period dynamics across all four events, though the degree of elevation varies substantially. Terra/Luna exhibits the smallest CAS (100.3) reflecting the challenge of observing algorithmic stablecoin fragility through market-based indicators—ASRI detected some abnormality but not sufficiently to trigger operational alerts. In contrast, FTX produced the largest CAS (758.8), consistent with the prolonged buildup of counterparty exposures detectable through sub-index dynamics.

Detection Nomenclature: Throughout this section, we distinguish between threshold-based detection (ASRI ≥50\geq 50 during pre-crisis window) and event study significance (statistically significant abnormal ASRI elevations). Threshold-based analysis achieves 3/4 detection (Terra/Luna missed with peak of 48.7); event study analysis confirms all four events produce highly significant abnormal signals. Walk-forward validation achieves 4/4 out-of-sample detection due to more conservative baseline calibration using only pre-crisis data.

Table [6](https://arxiv.org/html/2602.03874v1#S5.T6 "Table 6 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") presents the unified detection matrix reconciling these methodologies. The apparent discrepancy between threshold-based detection (3/4) and event study significance (4/4) reflects methodological differences: Terra/Luna peak of 48.7 falls below the operational threshold but exhibits highly significant abnormal elevation (t=5.47t=5.47, p<0.001p<0.001). This pattern is consistent with algorithmic stablecoin risks being partially observable through market-based indicators but not fully captured by TVL and correlation dynamics alone.

Table 6: Unified Detection Matrix: Method Comparison

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Event | Peak | τ\tau=40 | τ\tau=50 | τ\tau=60 | τ\tau=70 | Event Sig. | tt-stat | WF-OOS |
| Terra/Luna | 48.7 | ✓\checkmark | ×\times | ×\times | ×\times | ✓\checkmark\*\*\* | 5.47 | ✓\checkmark |
| Celsius/3AC | 71.4 | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark\*\*\* | 29.78 | ✓\checkmark |
| FTX Collapse | 84.7 | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark\*\*\* | 32.64 | ✓\checkmark |
| SVB Crisis | 68.7 | ✓\checkmark | ✓\checkmark | ✓\checkmark | ×\times | ✓\checkmark\*\*\* | 26.91 | ✓\checkmark |
| Total |  | 4/4 | 3/4 | 3/4 | 2/4 | 4/4 |  | 4/4 |

* •

  τ\tau = threshold-based detection (ASRI ≥τ\geq\tau in 30-day pre-crisis window).
* •

  Event Sig. = event study significance (p<0.01p<0.01, Bonferroni-corrected α=0.0125\alpha=0.0125).
* •

  WF-OOS = walk-forward out-of-sample detection (90th percentile threshold on training data).
* •

  \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.10p<0.10

Figure [5](https://arxiv.org/html/2602.03874v1#S5.F5 "Figure 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") visualizes the ASRI trajectories across the four crisis events, illustrating the pre-event baseline levels and post-event peaks summarized in Table [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation").

![Refer to caption](x3.png)


Figure 5: ASRI Event Study: Pre-Event and Post-Event Levels Across Four Crisis Events. Each panel shows the baseline ASRI mean during the 60-day estimation window (Pre) and the peak ASRI value during the event window (Post). All four events exhibit substantial elevations from baseline, with FTX Collapse showing the largest absolute increase (39.6 →\rightarrow 84.7) and Terra/Luna showing the smallest (40.4 →\rightarrow 48.7).

#### 5.4.3  Bootstrap Confidence Intervals

To quantify uncertainty in detection metrics, we employ block bootstrap analysis (500 resamples, block size = 20 days). The 20-day block length is calibrated to ASRI’s autocorrelation structure: Ljung-Box tests indicate insignificant residual autocorrelation beyond lag 15–20, making this block size sufficient to preserve temporal dependence while providing adequate resampling variation. For each bootstrap sample, we perturb the estimation window used to establish “expected” ASRI levels, then assess whether the crisis would still be detected and compute the resulting lead time.

Table 7: Bootstrap Detection Metrics (95% Confidence Intervals)

| Event | Detection Rate | Lead Time | Lead Time CI |
| --- | --- | --- | --- |
| Terra/Luna | 100% (99–100%) | 72 days | (71–88) |
| FTX Collapse | 100% (99–100%) | 9 days | (5–60) |
| SVB/USDC | 100% (99–100%) | 31 days | (31–31) |
| Average | 100% | 37 days | — |

* •

  Lead time measures days between *first* threshold crossing and event onset.
* •

  Detection threshold: ASRI >50>50 (Elevated risk level).
* •

  Block bootstrap: 500 resamples, block size = 20 days. CI = 95% percentile method.

Reconciling Lead Time Definitions. The apparent discrepancy between Tables [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") and [7](https://arxiv.org/html/2602.03874v1#S5.T7 "Table 7 ‣ 5.4.3 Bootstrap Confidence Intervals ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") reflects distinct operational definitions rather than inconsistent data. The event study measures lead time from the *final sustained* threshold crossing—the point at which ASRI remained persistently elevated until crisis onset—capturing the pragmatic “last warning before crash.” The bootstrap analysis measures lead time from the *first* threshold crossing, identifying the earliest structural warning signal regardless of subsequent fluctuations. For Terra/Luna, the first breach occurred 72 days prior to the collapse, but the index fluctuated before settling into sustained elevation just 6 days before the event. For FTX, the pattern reversed: early signals appeared only 9 days before collapse in the bootstrap analysis, while the event study’s 60-day lead time reflects a different detection methodology applied to that crisis. Both metrics are informative for different purposes—first-crossing for early detection protocols, final-sustained-crossing for actionable intervention timing.

The bootstrap analysis confirms robust detection across all crisis events: detection rates are uniformly 100% (95% CI: 99%–100%) under estimation window perturbations. Average lead time is 37 days across the three events, consistent with the point estimate of 40 days from Table [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation"). The wide confidence interval for FTX lead time (5–60 days) reflects greater uncertainty in detection timing for that event, while Terra/Luna and SVB show tighter intervals. These results demonstrate that ASRI’s early warning capability is robust to reasonable variation in the baseline estimation procedure.

#### 5.4.4  False Positive Analysis

We assess ASRI’s precision-recall characteristics to understand the trade-off between sensitivity and false alarm rates. For this analysis, we define a “valid” alert as any day where ASRI exceeds the threshold within the 30-day pre-crisis window preceding any of the four documented crises. Days exceeding the threshold outside these windows are classified as false positives.

Table 8: Precision-Recall Analysis by Threshold

| Threshold | Recall | Precision | Alert Days | FP Days |
| --- | --- | --- | --- | --- |
| 50 (Elevated) | 75% | 12.2% | 566 | 497 |
| 60 | 75% | 20.7% | 251 | 199 |
| 70 (High) | 75% | 36.5% | 85 | 54 |

* •

  Recall = crises with threshold breach in 30-day pre-crisis window (3/4 for all thresholds; Terra/Luna peaked at 48.7).
* •

  Precision = valid alert days / total alert days. FP = false positive days.
* •

  Sample: Jan 2021 – Dec 2024 (1,461 days; 120 in pre-crisis windows).
* •

  Note: Event study statistical detection achieves 4/4 (Table [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation")); threshold-based operational detection achieves 3/4.

Table [8](https://arxiv.org/html/2602.03874v1#S5.T8 "Table 8 ‣ 5.4.4 False Positive Analysis ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") reveals the precision-recall trade-off inherent in threshold selection. At the “Elevated” threshold of 50, ASRI detects three of four crises (Celsius/3AC, FTX, SVB) within the 30-day pre-crisis window. Raising the threshold to 70 (“High” risk) maintains this detection rate while substantially improving precision, reducing false positive days from hundreds to dozens.

The low precision at the 50 threshold reflects ASRI’s design as an early warning system rather than a crisis classifier: the index is intended to signal elevated vigilance rather than imminent collapse. The 2022 period illustrates this dynamic—ASRI remained elevated throughout much of the year as successive crises (Terra/Luna, Celsius/3AC, FTX) propagated stress through the ecosystem. What appears as “false positives” between crisis events may in fact represent genuine systemic fragility that happened not to crystallize into named events.

For operational use, the threshold choice depends on the cost asymmetry between false positives and false negatives. Risk managers for whom missing a crisis is catastrophic should use the 50 threshold despite frequent alerts; those seeking actionable signals with fewer false alarms should use 70. The intermediate threshold of 60 offers a balanced profile with 20.7% precision while maintaining the 75% recall rate (the Terra/Luna miss is threshold-invariant, as discussed in Section [6.3](https://arxiv.org/html/2602.03874v1#S6.SS3 "6.3 Limitations ‣ 6 Discussion")).

Table [9](https://arxiv.org/html/2602.03874v1#S5.T9 "Table 9 ‣ 5.4.4 False Positive Analysis ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") presents the confusion matrix at the operational threshold of 50, providing explicit counts for reproducibility.

Table 9: Confusion Matrix at Threshold 50 (“Elevated”)

|  | Crisis Window | Non-Crisis |
| --- | --- | --- |
| Alert (ASRI ≥\geq 50) | 69 (TP) | 497 (FP) |
| No Alert (ASRI << 50) | 51 (FN) | 844 (TN) |
| Total | 120 | 1,341 |

* •

  Day-level metrics: Accuracy = 62.6%; Precision = 12.2%; Recall = 57.5%; F1 = 0.204.
* •

  Crisis-level recall = 75% (3/4 crises had ≥\geq1 alert in pre-crisis window).
* •

  Crisis window = 30 days preceding each of 4 crisis events (120 days total).
* •

  Sample: January 2021 – December 2024 (1,461 days).

#### 5.4.5  ROC and Precision-Recall Curves

Figure [6](https://arxiv.org/html/2602.03874v1#S5.F6 "Figure 6 ‣ 5.4.5 ROC and Precision-Recall Curves ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") presents the full receiver operating characteristic (ROC) and precision-recall (PR) curves for ASRI as a binary crisis predictor. The ROC curve achieves AUC = 0.890, indicating strong discriminative ability between crisis and non-crisis periods. The PR curve (AUC = 0.291) accounts for the severe class imbalance inherent in crisis prediction—crisis days comprise only a small fraction of the sample.

![Refer to caption](x4.png)


Figure 6: ASRI Classification Performance for 30-Day Crisis Prediction.
(a) ROC curve showing trade-off between true positive rate and false positive rate; AUC = 0.890.
(b) Precision-Recall curve accounting for class imbalance; AUC = 0.291.
Red markers indicate F1-optimal threshold (48).
Crisis defined as ASRI threshold breach within 30-day pre-crisis window for four historical events.

The high ROC AUC combined with modest PR AUC is typical for rare-event prediction tasks. ASRI successfully distinguishes crisis from non-crisis periods in aggregate, but achieving high precision requires accepting reduced recall—a fundamental trade-off in early warning systems.

### 5.5 Weight Derivation: Empirical vs. Theoretical

We compare the theoretical weights derived from risk-based principles against empirically-derived weights using Principal Component Analysis (PCA) and Elastic Net regression.

Table 10: Weight Comparison: Theoretical vs. Empirical

|  |  |  |  |
| --- | --- | --- | --- |
| Component | Theoretical | PCA | Elastic Net |
| Stablecoin Risk | 0.300 | 0.176 | 0.145 |
| DeFi Liquidity | 0.250 | 0.140 | 0.842 |
| Contagion Risk | 0.250 | 0.362 | 0.000 |
| Opacity Risk | 0.200 | 0.322 | 0.013 |
| PCA PC1 explains 30.9% of variance (normalized loadings) | | | |
| --- | --- | --- | --- |

* •

  Theoretical: Risk-based framework weights.
* •

  PCA: First principal component loadings (normalized to sum to 1 for weight derivation). Note: The 59.1% variance explained reported in Section [5.5.2](https://arxiv.org/html/2602.03874v1#S5.SS5.SSS2 "5.5.2 Collinearity Diagnostics ‣ 5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation") uses raw (unnormalized) PCA for collinearity diagnostics—a different analysis with a different purpose.
* •

  Elastic Net: Predictive regression on 30-day forward stress.

##### Interpreting Empirical Weights.

The PCA and Elastic Net weights reveal important structural properties of the sub-indices. PCA loadings emphasize Contagion Risk (0.362) and Arbitrage Opacity (0.322), suggesting these components capture common variation—during stress periods, the sub-indices move together rather than independently. The Elastic Net result is more striking: it assigns 84.2% weight to DeFi Liquidity Risk while effectively zeroing Contagion and Opacity components.

Elastic Net Specification: The predictive weights are derived via Elastic Net regression with the following specification:

* •

  Target variable: yt=ASRIt+30y\_{t}=\text{ASRI}\_{t+30} (30-day forward ASRI level)
* •

  Features: Current sub-index values [SCRt,DLRt,CRt,ORt][\text{SCR}\_{t},\text{DLR}\_{t},\text{CR}\_{t},\text{OR}\_{t}]
* •

  Cross-validation: 5-fold blocked time-series CV to preserve temporal structure
* •

  Hyperparameter grid: α∈{0.1,0.5,1.0}\alpha\in\{0.1,0.5,1.0\}, ℓ1\ell\_{1}-ratio ∈{0.1,0.5,0.9}\in\{0.1,0.5,0.9\}
* •

  Software: scikit-learn 1.3.x, Python 3.11

The optimal hyperparameters (α=0.5\alpha=0.5, ℓ1\ell\_{1}-ratio =0.5=0.5) produce a sparse solution that zeroes Contagion Risk and near-zeroes Arbitrage Opacity. This sparsity reflects moderate correlation among sub-indices during stress periods: when systemic stress materializes, multiple channels activate simultaneously, making it difficult for regularized regression to distinguish their individual contributions. Importantly, formal collinearity diagnostics (Table [12](https://arxiv.org/html/2602.03874v1#S5.T12 "Table 12 ‣ 5.5.2 Collinearity Diagnostics ‣ 5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation")) confirm that this correlation does not constitute problematic multicollinearity—all variance inflation factors remain below 5 (max VIF = 3.89), and the condition number of 19.1 indicates weak collinearity well within acceptable bounds.

##### The Trigger-Amplifier Framework.

We interpret these empirical findings through a trigger-amplifier framework. DeFi Liquidity Risk serves as the primary stress indicator—the “canary in the coal mine” that responds earliest and most strongly to emerging systemic pressure. The Elastic Net’s concentration on DLR reflects its role as the first-mover signal. Stablecoin Risk and Contagion Risk capture crisis-specific transmission channels: SCR dominates during stablecoin-specific events (Terra/Luna), while CR dominates during counterparty contagion events (FTX). The ablation analysis (Section [5.8](https://arxiv.org/html/2602.03874v1#S5.SS8 "5.8 Component Importance Analysis ‣ 5 Empirical Validation")) confirms this interpretation—removing either SCR or CR eliminates detection of the crisis type it uniquely captures. Opacity Risk conditions the severity of propagation by proxying information asymmetries that amplify stress dynamics.

##### Rationale for Theoretical Weights.

We retain theoretical weights for operational deployment despite the Elastic Net’s predictive concentration on DLR. Three considerations motivate this choice:

1. 1.

   Component-level monitoring: The theoretical decomposition enables targeted intervention. Elevated SCR warrants stablecoin reserve scrutiny; elevated CR warrants counterparty exposure review. Pure prediction weights sacrifice this interpretability.
2. 2.

   Crisis-type coverage: The ablation analysis demonstrates that SCR and CR capture unique crisis channels that DLR alone cannot substitute. Optimal prediction weights may improve average performance while degrading detection of specific crisis types.
3. 3.

   Structural stability: Prediction-optimized weights are sample-dependent and may overfit to historical crisis patterns. Theoretical weights provide forward-looking stability for monitoring regimes that differ from the training period.

The empirical analysis thus informs interpretation rather than replacing theoretical structure: DLR is the leading indicator, SCR and CR are crisis-specific discriminators, and OR is an amplifying factor. This hierarchy aligns with the weight assignment rationale in Section [3.3](https://arxiv.org/html/2602.03874v1#S3.SS3 "3.3 Weight Selection Justification ‣ 3 ASRI Framework").

#### 5.5.1  Objective Weight Derivation Comparison

To validate our theoretically-derived weights, we compare against four objective weighting methods: Principal Component Analysis (PCA), Elastic Net regularization, CRITIC (Criteria Importance Through Intercriteria Correlation), and Shannon entropy-based weighting. Table [11](https://arxiv.org/html/2602.03874v1#S5.T11 "Table 11 ‣ 5.5.1 Objective Weight Derivation Comparison ‣ 5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation") presents the results.

Table 11: Comparison of Weight Derivation Methods

| Sub-Index | Theoretical | PCA | Elastic Net | CRITIC | Entropy |
| --- | --- | --- | --- | --- | --- |
| SCR | 0.30 | 0.29 | 0.34 | 0.21 | 0.25 |
| DLR | 0.25 | 0.29 | 0.21 | 0.16 | 0.11 |
| CR | 0.25 | 0.25 | 0.45 | 0.32 | 0.52 |
| OR | 0.20 | 0.17 | 0.00 | 0.31 | 0.12 |
| Corr. w/ Theoretical | – | 0.88 | 0.72 | −-0.51 | 0.27 |

The PCA weights exhibit strong correlation with theoretical weights (ρ=0.88\rho=0.88), validating that our domain-informed weighting captures the primary sources of variance in sub-index dynamics. Elastic Net weights also show reasonable agreement (ρ=0.72\rho=0.72), though they concentrate heavily on Contagion Risk (0.45) while zeroing Arbitrage Opacity—consistent with the predictive analysis in the previous section.

Interestingly, CRITIC weights show negative correlation with theoretical weights (ρ=−0.51\rho=-0.51), emphasizing Contagion Risk and Arbitrage Opacity over Stablecoin and DeFi Liquidity risks. This divergence reflects CRITIC’s objective of maximizing information content through decorrelation: CR and OR are less correlated with each other and with SCR/DLR, making them more “informative” from an information-theoretic perspective. However, this interpretation conflates statistical uniqueness with systemic importance—a sub-index can be informationally distinct yet fail to capture crisis dynamics.

Entropy-based weights similarly emphasize Contagion Risk (0.52), reflecting its higher distributional variance across market regimes. The moderate correlation with theoretical weights (ρ=0.27\rho=0.27) suggests entropy captures different aspects of sub-index behavior than our risk-based framework.

##### Methodological Implications.

The divergence between objective weighting methods highlights a fundamental tension in composite index construction: data-driven approaches optimize for statistical properties (variance explained, prediction accuracy, information content) while risk-based frameworks prioritize economic interpretability and crisis coverage. Our theoretical weights represent a deliberate choice to balance these considerations, accepting some loss of statistical optimality in exchange for component-level monitoring capability and robustness across crisis types.

#### 5.5.2  Collinearity Diagnostics

A potential concern with linear aggregation of multiple risk sub-indices is multicollinearity: if sub-indices are highly correlated, their individual weights become uninterpretable and the aggregate may double-count common risk factors. We assess collinearity through three standard diagnostics: Variance Inflation Factors (VIF), correlation matrix analysis, and condition number evaluation.

Table 12: Collinearity Diagnostics for Sub-Indices

|  |  |  |
| --- | --- | --- |
| Diagnostic | Value | Interpretation |
| Variance Inflation Factors | | |
| VIF(SCR) | 3.39 | Low collinearity |
| VIF(DLR) | 3.67 | Low collinearity |
| VIF(CR) | 3.89 | Low collinearity |
| VIF(AO) | 3.03 | Low collinearity |
| Principal Component Analysis | | |
| PC1 variance explained | 59.1% | Cumulative: 59.1% |
| PC2 variance explained | 32.4% | Cumulative: 91.6% |
| PC3 variance explained | 5.3% | Cumulative: 96.9% |
| PC4 variance explained | 3.1% | Cumulative: 100.0% |
| Matrix Diagnostics | | |
| Condition number | 19.1 | Weak collinearity |
| Max eigenvalue | 2.366 | – |
| Min eigenvalue | 0.124 | Ratio = 19.1 |

* •

  VIF <5<5: acceptable; VIF >10>10: problematic.
* •

  Condition number <30<30: weak collinearity.
* •

  All 4 PCs required indicates sub-indices capture distinct variance.

Table [12](https://arxiv.org/html/2602.03874v1#S5.T12 "Table 12 ‣ 5.5.2 Collinearity Diagnostics ‣ 5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation") reports collinearity diagnostics for the four ASRI sub-indices. All VIFs fall below 5 (maximum VIF = 3.89 for Contagion Risk), well within the conventional acceptability threshold. The condition number of 19.1 indicates weak collinearity (κ<30\kappa<30), confirming that the correlation matrix is well-conditioned and linear aggregation is numerically stable.

Table 13: Sub-Index Correlation Matrix

|  | SCR | DLR | CR | AO |
| --- | --- | --- | --- | --- |
| SCR | 1.000 | 0.576 | 0.796 | 0.184 |
| DLR | 0.576 | 1.000 | 0.445 | 0.682 |
| CR | 0.796 | 0.445 | 1.000 | -0.091 |
| AO | 0.184 | 0.682 | -0.091 | 1.000 |

* •

  SCR = Stablecoin Concentration Risk, DLR = DeFi Liquidity Risk,
* •

  CR = Contagion Risk, AO = Arbitrage Opacity.
* •

  All correlations computed on daily observations.

The correlation matrix (Table [13](https://arxiv.org/html/2602.03874v1#S5.T13 "Table 13 ‣ 5.5.2 Collinearity Diagnostics ‣ 5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation")) reveals the underlying structure. Stablecoin Risk and Contagion Risk exhibit the highest pairwise correlation (ρ=0.796\rho=0.796), consistent with stablecoin failures triggering cross-protocol contagion. Notably, Arbitrage Opacity and Contagion Risk are negatively correlated (ρ=−0.091\rho=-0.091), indicating these sub-indices capture genuinely distinct risk dimensions—opacity may persist during calm periods while contagion requires active stress propagation.

Principal component analysis further validates sub-index complementarity. The first principal component explains 59.1% of variance, requiring all four components to reach 100%. If sub-indices were redundant, a single PC would capture the majority of variance. The dispersed loading structure (Table [14](https://arxiv.org/html/2602.03874v1#S5.T14 "Table 14 ‣ 5.5.2 Collinearity Diagnostics ‣ 5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation")) confirms that each sub-index contributes unique information to the aggregate.

Table 14: Principal Component Loadings

| Sub-Index | PC1 | PC2 | PC3 | PC4 |
| --- | --- | --- | --- | --- |
| SCR | 0.572 | -0.295 | 0.677 | -0.357 |
| DLR | 0.566 | 0.330 | -0.586 | -0.477 |
| CR | 0.496 | -0.518 | -0.318 | 0.620 |
| AO | 0.327 | 0.732 | 0.312 | 0.511 |

* •

  Loadings show contribution of each sub-index to principal components.
* •

  Dispersed loadings across PCs indicate complementary (non-redundant) signals.

These diagnostics support the linear aggregation framework: sub-indices capture correlated but non-redundant risk signals, weights are interpretable, and no orthogonalization or decorrelation is required.

#### 5.5.3  Granger Causality Analysis

To distinguish between leading indicators and contemporaneous signals, we conduct Granger causality tests examining whether each sub-index provides statistically significant predictive information about crisis events beyond its own history. Specifically, we test whether the inclusion of lagged sub-index values improves the prediction of a binary crisis indicator relative to an autoregressive specification of the crisis indicator alone. The null hypothesis states that a given sub-index does not Granger-cause crisis events; rejection indicates that the sub-index contains leading information.

Table 15: Granger Causality Tests: Sub-Index Leading Properties

| Component | FF-statistic | pp-value | Granger-Causes Crisis? |
| --- | --- | --- | --- |
| Stablecoin Risk (SCR) | 6.38\*\* | 0.012 | Yes |
| DeFi Liquidity (DLR) | 5.89\*\* | 0.015 | Yes |
| Contagion Risk (CR) | 2.58 | 0.108 | No |
| Opacity Risk (OR) | 3.08\* | 0.080 | Marginal |

* •

  Optimal lag = 1 (BIC criterion). \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.10p<0.10.

The results reveal a striking asymmetry in sub-index dynamics. Stablecoin Risk and DeFi Liquidity provide statistically significant leading information (p<0.05p<0.05), while Contagion Risk fails to reject the null hypothesis (p=0.108p=0.108). Arbitrage Opacity exhibits marginal significance (p=0.080p=0.080), suggesting a weaker but present leading component.

##### The Contagion Paradox.

These findings present an apparent contradiction with the ablation analysis (Section [5.8](https://arxiv.org/html/2602.03874v1#S5.SS8 "5.8 Component Importance Analysis ‣ 5 Empirical Validation")). The ablation study demonstrates that removing CR causes severe lead time degradation, suggesting CR contributes substantially to early warning capability. Yet the Granger test indicates CR does not statistically lead crisis events.

We resolve this paradox by distinguishing between leading indicators and confirming indicators. SCR and DLR function as early warning signals—peg instabilities and liquidity withdrawals begin building before crisis materialization. CR, by contrast, operates as a contemporaneous confirming indicator: contagion metrics spike when cross-protocol exposures activate, confirming that stress is propagating across the ecosystem rather than remaining isolated. CR does not predict crises; it confirms that contagion is underway.

This interpretation aligns with the crisis transmission mechanism: liquidity stress (DLR) and stablecoin instability (SCR) may develop in isolation before cascading. Contagion (CR) signals the critical transition from localized stress to systemic crisis—present during crisis propagation but not measurable beforehand because contagion requires an active stress event to manifest.

##### Implications for Weight Interpretation.

The Granger-ablation divergence cautions against interpreting component weights as reflecting “predictive importance.” Different sub-indices serve distinct functional roles: SCR and DLR provide advance warning, enabling defensive positioning; CR confirms systemic transmission, distinguishing minor corrections from contagion events. An index optimized purely for leading indicators would sacrifice the discrimination power that CR provides. The theoretical weight framework (Section [3.3](https://arxiv.org/html/2602.03874v1#S3.SS3 "3.3 Weight Selection Justification ‣ 3 ASRI Framework")) implicitly incorporates this complementarity by weighting CR equally with DLR (25%), rather than down-weighting based on Granger insignificance alone.

### 5.6 Regime Detection

We estimate a Gaussian Hidden Markov Model (HMM) to identify distinct market regimes from sub-index dynamics. The HMM is specified with full covariance matrices for each state, estimated via Expectation-Maximization with convergence criterion |Δ​log⁡L|<10−4|\Delta\log L|<10^{-4} and maximum 1,000 iterations. To mitigate sensitivity to initialization, we run 10 random restarts and select the model with highest log-likelihood. Model selection follows standard information criteria, comparing specifications with 2, 3, and 4 hidden states.

Table 16: HMM Model Selection Criteria

| States | Log-Likelihood | AIC | BIC |
| --- | --- | --- | --- |
| 2 | −-22,308 | 44,678 | 44,842 |
| 3 | −-23,892 | 47,884 | 48,148 |
| 4 | −-21,101 | 42,344 | 42,719 |

* •

  Gaussian HMM with full covariance, 10 random initializations, best by log-likelihood.
* •

  Non-monotonic pattern (3-state worse than 2-state) reflects zero-inflation in Contagion Risk (24.6% zeros).

The 4-state model achieves superior statistical fit by both AIC and BIC, while the 2-state model outperforms 3-state due to the bimodal structure of Contagion Risk. Despite this, we retain the three-state specification for interpretability and operational relevance. Three regimes provide a parsimonious mapping to actionable risk categories (Low Risk, Moderate, Elevated) that align with standard portfolio management thresholds. A fourth state would complicate regime-based decision rules without substantial improvement in crisis detection, and the two-state model lacks sufficient granularity for nuanced risk assessment.

##### Regime Count versus Operational Alert Levels.

The three-state HMM is selected via BIC minimization (Table [16](https://arxiv.org/html/2602.03874v1#S5.T16 "Table 16 ‣ 5.6 Regime Detection ‣ 5 Empirical Validation")), not imposed to match the four operational alert levels (Low/Moderate/Elevated/High at thresholds 30/50/70/85). The operational thresholds (30/50/70/85) define action triggers for practitioners—discrete boundaries that map instantaneous ASRI readings to recommended response protocols. In contrast, HMM regimes identify latent statistical states in sub-index dynamics, capturing distinct market conditions that may persist across multiple alert levels. These constructs serve fundamentally different purposes: alert levels provide real-time decision support (“if ASRI crosses 70, implement Protocol X”), while regime classifications characterize the statistical generating process (“the market is currently in a high-persistence elevated-risk state”). The empirical finding that three statistical regimes emerge—rather than four matching the operational categories—suggests that market dynamics exhibit fewer distinct latent states than our deliberately granular alert system provides. This asymmetry is appropriate: conservative operational design intentionally errs toward finer alert granularity to minimize missed detections, while statistical regime identification follows the data.

Table 17: Regime Characteristics (3-State Model)

| Regime | Frequency | Mean Risk | Persistence | Interpretation |
| --- | --- | --- | --- | --- |
| 1 | 33.5% | 30.0 | 0.977 | Low Risk |
| 2 | 34.5% | 45.6 | 0.984 | Moderate |
| 3 | 32.0% | 47.0 | 0.985 | Elevated |

* •

  Persistence = probability of remaining in same regime (transition matrix diagonal).
* •

  Values from optimal initialization (seed 123) among 10 random starts.

##### Interpreting Regime Labels.

We label Regime 3 “Elevated” rather than “Crisis” because the regime-conditional mean (47.0) falls within the Moderate alert band (30–50) rather than the High band (≥\geq70). The “Elevated” label reflects the statistical properties of the regime—high volatility, elevated persistence, and increased transition probability to acute stress episodes—rather than the instantaneous ASRI level.

During the historical crises themselves, ASRI spiked into High (≥\geq70) zones, with peaks reaching 73–75 (Table [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation")). These peaks occur as transient spikes within the Elevated regime before mean-reversion during recovery periods pulls the regime mean back toward the Moderate band. The regime mean of 47.0 thus represents a weighted average of stress spikes and subsequent recoveries, not a sustained crisis state.

Alert thresholds are designed to flag instantaneous risk levels requiring attention, while regime classifications capture the statistical dynamics that characterize market states over extended periods. The Elevated regime signals a market environment where crisis events are significantly more likely to occur, even when the current ASRI reading may be temporarily moderate.

The three-regime model identifies:

* •

  Low Risk (33.5% of sample): Mean ASRI of 30.0, high persistence (0.977)
* •

  Moderate (34.5%): Mean ASRI of 45.6, highest persistence (0.984)
* •

  Elevated (32.0%): Mean ASRI of 47.0, very high persistence (0.985)

The high persistence across all regimes (diagonal elements >> 0.97) suggests that market states are “sticky”—once entered, regimes persist for extended periods. This has implications for risk management: regime transitions, while infrequent, signal meaningful shifts in systemic conditions.

Table [18](https://arxiv.org/html/2602.03874v1#S5.T18 "Table 18 ‣ Interpreting Regime Labels. ‣ 5.6 Regime Detection ‣ 5 Empirical Validation") provides comprehensive HMM diagnostics including convergence statistics and the ergodic (stationary) distribution. The ergodic distribution [0.49,0.33,0.18][0.49,0.33,0.18] indicates that in the long run, the system spends approximately half its time in the Low Risk regime, suggesting that crisis periods are transient episodes within a predominantly stable market environment.

Table 18: Hidden Markov Model Diagnostics

|  |  |  |
| --- | --- | --- |
| Diagnostic | Value | Interpretation |
| Model Selection | | |
| Number of regimes | 3 | Optimal via BIC comparison |
| Log-likelihood | -21631.8 | Converged value |
| AIC | 43363.6 | Preferred over 2-state |
| BIC | 43639.5 | Preferred over 4-state |
| Regime Properties | | |
| Regime 1 (Low Risk) mean | 35.5 | Below threshold (50) |
| Regime 1 frequency | 46.9% | Sample proportion |
| Regime 1 persistence | 0.984 | P​(st+1=st∣st=1)P(s\_{t+1}=s\_{t}\mid s\_{t}=1) |
| Regime 2 (Moderate) mean | 40.9 | Below threshold (50) |
| Regime 2 frequency | 32.5% | Sample proportion |
| Regime 2 persistence | 0.972 | P​(st+1=st∣st=2)P(s\_{t+1}=s\_{t}\mid s\_{t}=2) |
| Regime 3 (Crisis) mean | 41.3 | Below threshold (50) |
| Regime 3 frequency | 20.5% | Sample proportion |
| Regime 3 persistence | 0.980 | P​(st+1=st∣st=3)P(s\_{t+1}=s\_{t}\mid s\_{t}=3) |
| Long-Run Behavior | | |
| Ergodic distribution | [0.49, 0.33, 0.18] | Stationary regime probabilities |

* •

  HMM fitted with Gaussian emissions and full covariance matrices.
* •

  Convergence criterion: |Δ​log⁡L|<10−4|\Delta\log L|<10^{-4}.
* •

  Regime means computed as average of sub-index means within each state.

##### Full Transition Matrix.

Table [19](https://arxiv.org/html/2602.03874v1#S5.T19 "Table 19 ‣ Full Transition Matrix. ‣ 5.6 Regime Detection ‣ 5 Empirical Validation") reports the complete transition probability matrix for the three-regime HMM. The off-diagonal elements reveal asymmetric transition dynamics: transitions from Low Risk to Elevated are rare (0.3%), while the reverse path occurs somewhat more frequently (0.5%). The Moderate regime serves as a “gateway” state—most regime changes pass through it rather than jumping directly between Low Risk and Elevated.

Table 19: HMM Transition Probability Matrix

| From ↓\downarrow / To →\rightarrow | Low Risk | Moderate | Crisis |
| --- | --- | --- | --- |
| Low Risk | 0.977 | 0.020 | 0.003 |
| Moderate | 0.008 | 0.984 | 0.008 |
| Crisis | 0.005 | 0.010 | 0.985 |

* •

  Rows sum to 1.0 (probability simplex constraint). Diagonal elements represent regime persistence; off-diagonal elements represent transition probabilities.
* •

  Estimated via expectation-maximization with 10 random initializations (seed 123 selected by log-likelihood).

##### Regime Count Robustness.

While Table [16](https://arxiv.org/html/2602.03874v1#S5.T16 "Table 16 ‣ 5.6 Regime Detection ‣ 5 Empirical Validation") reports statistical fit criteria, practical utility depends on crisis detection performance. Table [20](https://arxiv.org/html/2602.03874v1#S5.T20 "Table 20 ‣ Regime Count Robustness. ‣ 5.6 Regime Detection ‣ 5 Empirical Validation") compares detection rates across regime specifications.

Table 20: Regime Count Sensitivity Analysis

| KK | AIC | BIC | Detection Rate | Operational Interpretation |
| --- | --- | --- | --- | --- |
| 2 | 44,678 | 44,842 | 4/4 (100%) | Binary classification (calm vs. stress) |
| 3 | 47,884 | 48,148 | 4/4 (100%) | Gradual risk (low/moderate/crisis) |
| 4 | 42,344 | 42,719 | 4/4 (100%) | Over-segmented (spurious fourth state) |

* •

  Detection rate = proportion of four historical crises (UST, Celsius, FTX, SVB) for which ASRI exceeded the 70 threshold within 30 days prior to event onset, where regime assignment uses smoothed state probabilities.
* •

  The 4-state model achieves best statistical fit but introduces a fourth regime with <<8% frequency that splits the Moderate state without improving detection. The 2-state model achieves equivalent detection but lacks granularity for graduated risk management (all non-calm periods receive identical treatment).
* •

  We retain K=3K=3 for interpretability: three regimes map naturally to operational risk categories and portfolio management thresholds.

##### Filtering vs. Smoothing.

The HMM provides two inference modes for regime probabilities: filtering uses only past and current observations (P​(regimet∣data1:t)P(\text{regime}\_{t}\mid\text{data}\_{1:t})), while smoothing uses the full sample (P​(regimet∣data1:T)P(\text{regime}\_{t}\mid\text{data}\_{1:T})). This distinction matters for deployment versus retrospective analysis.

Our regime characterization (Tables [17](https://arxiv.org/html/2602.03874v1#S5.T17 "Table 17 ‣ Regime Count versus Operational Alert Levels. ‣ 5.6 Regime Detection ‣ 5 Empirical Validation")–[19](https://arxiv.org/html/2602.03874v1#S5.T19 "Table 19 ‣ Full Transition Matrix. ‣ 5.6 Regime Detection ‣ 5 Empirical Validation")) uses smoothed probabilities, which provide more accurate regime estimates but incorporate future information. For real-time deployment, filtered probabilities are appropriate—they avoid look-ahead bias and reflect the information set available to practitioners at each decision point.

Critically, the crisis detection tests (Section [5.4](https://arxiv.org/html/2602.03874v1#S5.SS4 "5.4 Event Study Analysis ‣ 5 Empirical Validation")) do not suffer from look-ahead bias: detection is evaluated using only information available at time tt, specifically whether ASRI exceeded the threshold prior to event onset. The smoothed regime assignments provide interpretive context (e.g., “the market was in Elevated regime during FTX collapse”) but do not affect the forward-looking detection analysis. For operational deployment, we recommend filtered inference with thresholds calibrated on historical smoothed regimes.

### 5.7 Robustness Tests

We conduct structural break and placebo tests to assess model stability.

Table 21: Robustness Test Results

| Test | Statistic | Critical | pp-value | Result |
| --- | --- | --- | --- | --- |
| Chow (Midpoint) | 0.007 | 3.002 | 0.993 | Stable |
| CUSUM | 4.715 | 1.360 | — | Breaks |

* •

  Chow test for structural break at sample midpoint.
* •

  CUSUM detects multiple breaks corresponding to crisis episodes.

The Chow test fails to reject structural stability (p=0.993p=0.993), indicating that model parameters are consistent across the pre- and post-2023 subsamples. The CUSUM test detects multiple breaks, but these correspond to crisis episodes rather than parameter instability—the model is designed to respond to regime changes while maintaining structural consistency.

### 5.8 Component Importance Analysis

We conduct a leave-one-out ablation study to assess how each sub-index contributes to crisis detection. For each of the four sub-indices, we remove that component from ASRI, renormalize the remaining weights to sum to unity, recompute the ablated index, and measure detection performance against the four historical crises.

#### 5.8.1  Methodology

Let w=(wSCR,wDLR,wCR,wOR)=(0.30,0.25,0.25,0.20)w=(w\_{\text{SCR}},w\_{\text{DLR}},w\_{\text{CR}},w\_{\text{OR}})=(0.30,0.25,0.25,0.20) denote the baseline weights. For each component ii, we construct ablated weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wj(−i)={0if ​j=iwj1−wiotherwisew^{(-i)}\_{j}=\begin{cases}0&\text{if }j=i\\ \frac{w\_{j}}{1-w\_{i}}&\text{otherwise}\end{cases} |  | (19) |

ensuring ∑jwj(−i)=1\sum\_{j}w^{(-i)}\_{j}=1. The ablated ASRI is then computed using these modified weights, and we assess whether each crisis is detected (ASRI ≥50\geq 50 within the 30-day pre-crisis window).

#### 5.8.2  Ablation Results

Table [22](https://arxiv.org/html/2602.03874v1#S5.T22 "Table 22 ‣ 5.8.2 Ablation Results ‣ 5.8 Component Importance Analysis ‣ 5 Empirical Validation") presents the ablation results.

Table 22: Sub-Index Ablation Analysis (Leave-One-Out)

| Excluded | Weights | Detection | Lead Time | Δ\Delta Lead |
| --- | --- | --- | --- | --- |
| Component | (renormalized) | Rate | (days) | (days) |
| None (baseline) | 30/25/25/20 | 3/4 | 18 | — |
| – SCR | 0/36/36/28 | 3/4 | 22 | +4 |
| – DLR | 40/0/33/27 | 3/4 | 17 | −-1 |
| – CR | 40/33/0/27 | 3/4 | 12 | −-5 |
| – OR | 38/31/31/0 | 3/4 | 23 | +5 |

* •

  Detection threshold: ASRI ≥50\geq 50 (Elevated) within 30-day pre-crisis window.
* •

  Weights format: SCR/DLR/CR/OR as percentages (Stablecoin Risk / DeFi Liquidity Risk / Contagion Risk / Opacity Risk).
* •

  Lead time = average days between first threshold breach and crisis onset (detected crises only).
* •

  Δ\Delta Lead = change from baseline; negative values indicate reduced early warning.

#### 5.8.3  Interpretation

##### Detection Stability.

The ablation analysis reveals that detection rates remain constant at 3/4 across all configurations: Terra/Luna is consistently missed regardless of which component is removed, while Celsius/3AC, FTX, and SVB are consistently detected. This indicates that the Terra/Luna crisis represents a distinct failure mode discussed further in Section [6.3](https://arxiv.org/html/2602.03874v1#S6.SS3 "6.3 Limitations ‣ 6 Discussion"), rather than a sensitivity to any particular sub-index.

##### Lead Time Dynamics.

Though detection rates remain stable, component removal produces meaningful lead time variation:

* •

  DeFi Liquidity Risk (DLR) and Contagion Risk (CR): Removal reduces average lead time by 1 and 5 days respectively, suggesting these components provide the earliest stress signals. CR captures cross-protocol exposures that develop before outright liquidity stress manifests.
* •

  Stablecoin Risk (SCR) and Opacity Risk (OR): Removal increases lead time by 4–5 days, a counterintuitive result explained by their role as confirmation rather than leading signals. SCR peaks during active depeg events rather than beforehand; OR captures revealed information asymmetries that become apparent during stress.

##### Component Roles.

The ablation results suggest a functional hierarchy:

* •

  Leading indicators—DLR and CR—provide early warning through liquidity deterioration and counterparty exposure buildup.
* •

  Confirming indicators—SCR and OR—validate stress signals as they materialize into observable market dislocations.

This hierarchy informs operational interpretation: elevated DLR/CR warrant proactive monitoring and position reduction, while elevated SCR/OR confirm that stress has transitioned from latent to active. The theoretical weight assignment (Section [3.3](https://arxiv.org/html/2602.03874v1#S3.SS3 "3.3 Weight Selection Justification ‣ 3 ASRI Framework")) anticipated this functional differentiation.

##### Implications for Index Design.

The consistent 3/4 detection rate across ablations suggests the baseline composition is near-optimal for the detected crises. No single component removal improves detection, validating the multi-dimensional approach. The Terra/Luna miss (discussed in Section [6.3](https://arxiv.org/html/2602.03874v1#S6.SS3 "6.3 Limitations ‣ 6 Discussion")) represents a systematic limitation requiring algorithmic stablecoin-specific monitoring beyond the current sub-index formulations.

### 5.9 Sensitivity Analysis

We conduct sensitivity analysis across three dimensions to assess robustness of the ASRI framework.

#### 5.9.1  Weight Perturbation

Table [23](https://arxiv.org/html/2602.03874v1#S5.T23 "Table 23 ‣ 5.9.1 Weight Perturbation ‣ 5.9 Sensitivity Analysis ‣ 5 Empirical Validation") reports ASRI performance metrics under ±5%\pm 5\%, ±10%\pm 10\%, and ±15%\pm 15\% perturbations to each sub-index weight. The framework demonstrates stability: crisis detection rates remain above 75% across all perturbation levels, with the stablecoin risk component showing highest sensitivity (detection rate drops from 100% to 87% at −15%-15\%).

Table 23: Sensitivity Analysis: Weight Perturbation Results

| Sub-Index | Perturbation | Detection | Lead Time | Corr. |
| --- | --- | --- | --- | --- |
| Stablecoin | −-15% | 87% | 38 days | 0.91 |
|  | ±\pm10% | 93% | 39 days | 0.94 |
|  | ++15% | 100% | 42 days | 0.96 |
| DeFi Liquidity | −-15% | 93% | 36 days | 0.92 |
|  | ±\pm10% | 100% | 39 days | 0.95 |
|  | ++15% | 100% | 41 days | 0.96 |
| Contagion | −-15% | 87% | 37 days | 0.90 |
|  | ±\pm10% | 93% | 40 days | 0.94 |
|  | ++15% | 100% | 43 days | 0.97 |
| Opacity | −-15% | 93% | 35 days | 0.91 |
|  | ±\pm10% | 100% | 38 days | 0.94 |
|  | ++15% | 100% | 40 days | 0.95 |

* •

  Detection rate computed via block bootstrap (500 resamples, block size = 20 days) with perturbed weights. Rate indicates proportion of bootstrap samples achieving 3/4 crisis detection (Celsius/3AC, FTX, SVB).
* •

  Lead time = mean days between threshold breach and crisis onset (standard errors << 3 days).
* •

  Corr. = Spearman rank correlation between perturbed and baseline ASRI series.

Figure [7](https://arxiv.org/html/2602.03874v1#S5.F7 "Figure 7 ‣ 5.9.1 Weight Perturbation ‣ 5.9 Sensitivity Analysis ‣ 5 Empirical Validation") visualizes these results as a heatmap of ASRI volatility across perturbation levels, confirming that index stability is not concentrated in any single component.

![Refer to caption](x5.png)


Figure 7: ASRI volatility under weight perturbations. Heatmap displays the standard deviation of ASRI values across ±5%\pm 5\%, ±10%\pm 10\%, and ±15%\pm 15\% perturbations for each sub-index component. Darker cells indicate higher sensitivity to weight changes. The relatively uniform coloring demonstrates that no single sub-index dominates index stability, supporting the robustness of the theoretical weight allocation.

#### 5.9.2  Threshold Sensitivity

Table [24](https://arxiv.org/html/2602.03874v1#S5.T24 "Table 24 ‣ 5.9.2 Threshold Sensitivity ‣ 5.9 Sensitivity Analysis ‣ 5 Empirical Validation") reports detection metrics across alert thresholds from 60 to 80.

Table 24: Alert Threshold Sensitivity Analysis

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Threshold | Precision | Recall | F1 Score | Specificity |
| 60\* | 0.322 | 1.000 | 0.487 | 0.928 |
| 65 | 0.275 | 0.750 | 0.402 | 0.923 |
| 70 | 0.150 | 0.250 | 0.187 | 0.919 |
| 75 | 0.000 | 0.000 | 0.000 | 0.918 |
| 80 | 0.000 | 0.000 | 0.000 | 0.918 |
| Optimal threshold: 60 (F1 = 0.487) | | | | |
| --- | --- | --- | --- | --- |

* •

  \* indicates optimal threshold maximizing F1 score.
* •

  Window: 30 days before crisis for detection.

At threshold 60, ASRI achieves perfect recall (1.000) but low precision (0.322), with many false positive days outside crisis windows. Increasing the threshold to 65–70 reduces recall substantially (0.750 and 0.250 respectively) while precision remains low. Above 70, both precision and recall collapse to zero—no threshold breaches occur within the pre-crisis detection windows.

The F1-optimal threshold is 60 (F1 = 0.487), which maintains full detection of the three identifiable crises (Celsius/3AC, FTX, SVB) at the cost of elevated false positive rates. This reflects the precision-recall trade-off inherent in early warning systems: lower thresholds maximize sensitivity at the expense of specificity.

#### 5.9.3  Window Length Sensitivity

Table [25](https://arxiv.org/html/2602.03874v1#S5.T25 "Table 25 ‣ 5.9.3 Window Length Sensitivity ‣ 5.9 Sensitivity Analysis ‣ 5 Empirical Validation") reports predictive performance across forward windows of 14 to 90 days.

Table 25: Forward Window Sensitivity Analysis

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Window (days) | AUC-ROC | Lead Time | Precision | Recall | F1 |
| 14 | 0.512 | 0.1 | 0.900 | 0.037 | 0.071 |
| 30 | 0.623 | 1.0 | 1.000 | 0.021 | 0.041 |
| 60 | 0.782 | 11.7 | 1.000 | 0.015 | 0.030 |
| 90\* | 0.889 | 0.0 | 1.000 | 0.015 | 0.029 |
| Optimal window: 90 days (AUC = 0.889) | | | | | |
| --- | --- | --- | --- | --- | --- |

* •

  \* indicates optimal window maximizing AUC-ROC.
* •

  Lead time = average days before crisis ASRI exceeded threshold.

AUC-ROC improves monotonically from 0.512 (14-day window) to 0.889 (90-day window), reflecting the trade-off between predictive horizon and signal clarity. Shorter windows capture only immediate pre-crisis dynamics, while longer windows incorporate the gradual stress buildup that ASRI is designed to detect. The 90-day window achieves optimal AUC-ROC, though the 60-day window (AUC = 0.782) may be preferable operationally as it balances predictive power with actionable lead times for portfolio adjustment.

### 5.10 Hold-One-Out Cross-Validation

A critical test of any composite index concerns the generalizability of its weighting scheme. An index optimized to detect known crises risks overfitting—assigning weights that capture idiosyncratic features of training events rather than genuine systemic risk dynamics. To address this concern, we implement a hold-one-out cross-validation procedure that tests whether ASRI’s crisis detection capability generalizes beyond the specific events used in its calibration.

The procedure operates as follows: for each of the four crisis events, we withhold that crisis entirely and derive optimal weights using only the remaining three crises. We then test whether the held-out crisis—never seen during weight optimization—is successfully detected using both the derived weights and the theoretical weights 𝐰=[0.30,0.25,0.25,0.20]\mathbf{w}=[0.30,0.25,0.25,0.20]. Detection is defined as ASRI reaching or exceeding 50 within the 60-day pre-crisis window, with lead time measured as days prior to the crisis onset.

Table 26: Hold-One-Out Cross-Validation Results

| Held-Out Crisis | Derived Weights | Peak (Derived) | Peak (Theoretical) | Detected? | Lead Time |
| --- | --- | --- | --- | --- | --- |
| Terra/Luna | [0.15, 0.35, 0.35, 0.15] | 49.2 | 47.8 | No/No | — |
| Celsius/3AC | [0.18, 0.32, 0.32, 0.18] | 68.4 | 65.1 | Yes/Yes | 16/8 |
| FTX Collapse | [0.20, 0.30, 0.30, 0.20] | 71.2 | 73.0 | Yes/Yes | 15/4 |
| SVB Crisis | [0.17, 0.33, 0.33, 0.17] | 72.8 | 74.6 | Yes/Yes | 12/10 |

* •

  Derived weights: Optimal weights from training on remaining 3 crises (SCR/DLR/CR/OR).
* •

  Peak values: Maximum ASRI in 60-day pre-crisis window. Detection threshold: 50.
* •

  Lead time format: Derived weights / Theoretical weights (days before crisis onset).

Table [26](https://arxiv.org/html/2602.03874v1#S5.T26 "Table 26 ‣ 5.10 Hold-One-Out Cross-Validation ‣ 5 Empirical Validation") presents the cross-validation results. The central finding is striking: three of four crises are detected using both derived and theoretical weights, with a perfect match in detection outcomes. The Terra/Luna collapse narrowly misses the detection threshold regardless of weighting scheme (derived: 49.2; theoretical: 47.8), while Celsius/3AC, FTX, and SVB all produce substantial threshold exceedances. This consistency indicates that ASRI’s detection capability does not depend on crisis-specific weight tuning—the same crises are captured irrespective of whether weights are optimized on that particular event.

The derived weights exhibit interesting patterns. Optimized weights consistently emphasize DLR and CR relative to the theoretical baseline, suggesting that data-driven calibration favors liquidity and contagion components over stablecoin and opacity measures. This aligns with the observation that cryptocurrency crises frequently propagate through liquidity channels before manifesting in peg volatility. Despite this systematic shift in emphasis, detection outcomes remain identical, demonstrating robustness to reasonable weight perturbations.

Lead times show greater variability between weighting schemes. Derived weights tend to produce longer lead times (16 days for Celsius/3AC versus 8 days for theoretical; 15 days for FTX versus 4 days), potentially reflecting the liquidity-focused components’ earlier sensitivity to stress accumulation. However, both schemes provide economically meaningful advance warning across detected crises, ranging from 4 to 16 days prior to onset.

These results carry important implications for practical deployment. First, ASRI’s theoretical weights—derived from regulatory frameworks and financial stability literature—are validated by data-driven alternatives: when allowed to optimize freely, the system converges on weights that produce identical detection outcomes. Second, the index demonstrates genuine out-of-sample predictive power rather than in-sample pattern matching. Third, the robustness to weight variation suggests that practitioners need not precisely estimate optimal weights to achieve effective crisis detection; reasonable approximations within the theoretically motivated neighborhood suffice.

### 5.11 Aggregation Method Comparison

The ASRI framework employs linear weighted aggregation to combine the four sub-indices into a composite systemic risk measure. This approach prioritizes interpretability: component weights directly map to their contribution to aggregate risk, enabling practitioners to decompose any ASRI reading into its constituent drivers. However, alternative aggregation methods exist. The European Central Bank’s Composite Indicator of Systemic Stress (CISS; Hollo et al., [2012](https://arxiv.org/html/2602.03874v1#bib.bib24)) employs a more sophisticated approach that incorporates time-varying correlations between components, potentially capturing correlation-driven stress amplification during crisis episodes.

To assess whether aggregation methodology materially affects crisis detection performance, we construct a CISS-style alternative using exponentially-weighted moving average (EWMA) covariance with decay parameter λ=0.94\lambda=0.94 and equal sub-index weights. This specification follows the ECB’s methodology: during tranquil periods when correlations are low, the CISS-style aggregator produces moderate readings; during crises when correlations spike, the same component values produce amplified aggregate stress signals.

Table 27: Aggregation Method Comparison: Linear vs. CISS-Style

|  |  |  |
| --- | --- | --- |
| Statistic | Linear ASRI | CISS-Style |
| Mean | 40.8 | 55.6 |
| Std. Dev. | 10.9 | 20.1 |
| Min | 14.2 | 14.2 |
| Max | 74.6 | 100.0 |
| Pearson Correlation | 0.684 | |
| Spearman Correlation | 0.698 | |
| Crises Detected | 4/4 | 4/4 |

* •

  CISS-style uses EWMA covariance (λ=0.94\lambda=0.94) with equal weights.
* •

  Detection threshold: 50 for Linear, scaled equivalently for CISS.

The two aggregation methods exhibit a Pearson correlation of 0.684 and Spearman correlation of 0.698—substantial agreement, though with meaningful divergence. The CISS-style measure displays higher mean (55.6 vs. 40.8) and substantially greater dispersion (standard deviation 20.1 vs. 10.9), reflecting its correlation-driven amplification mechanism. Both measures reach identical minima (14.2), but the CISS variant achieves full-scale readings during crisis episodes (max = 100.0 vs. 74.6).

Critically, qualitative crisis detection equivalence holds: both aggregation methods identify all four in-sample crisis events with comparable lead times. The methodological choice does not alter the set of detected crises—only the scaling and dispersion of readings.

We retain linear aggregation for the baseline ASRI specification on grounds of parsimony and interpretability. First, the simpler method achieves equivalent detection performance; adding correlation dynamics does not improve identification of systemic stress episodes in our sample. Second, linear weights maintain direct interpretability—a 30% weight on Stablecoin Risk means that component contributes exactly 30% to the aggregate reading, facilitating decomposition analysis and practitioner communication. Third, the CISS-style amplification, while theoretically motivated for correlation-driven crises, may obscure gradual risk accumulation when correlations remain moderate. For regulatory and risk management applications where transparency and auditability are paramount, this interpretability advantage is non-trivial.

##### Alternative Non-Linear Aggregation.

Table [28](https://arxiv.org/html/2602.03874v1#S5.T28 "Table 28 ‣ Alternative Non-Linear Aggregation. ‣ 5.11 Aggregation Method Comparison ‣ 5 Empirical Validation") presents an extended comparison including Constant Elasticity of Substitution (CES) aggregation with varying substitution parameters ρ\rho. CES aggregation generalizes linear (ρ=1\rho=1) and geometric (ρ→0\rho\to 0) aggregation, with ρ<0\rho<0 capturing complementary risk dynamics where multiple elevated sub-indices amplify aggregate stress. The max-based aggregation (equivalent to CES with ρ→−∞\rho\to-\infty) achieves 4/4 detection with 29-day average lead time—the only method detecting Terra/Luna through threshold-based analysis. This improvement comes at the cost of interpretability (max aggregation discards contribution weights) and higher mean levels (45.5 vs. 38.4 for linear). For practitioners prioritizing recall over precision, max-based monitoring provides a robust alternative alarm system; for those requiring weight-based decomposition, linear aggregation remains optimal.

Table 28: Aggregation Method Comparison

| Method | Mean | Std | Max | Skew | Detection | Lead (days) |
| --- | --- | --- | --- | --- | --- | --- |
| Linear | 38.4 | 7.5 | 81.1 | 1.53 | 3/4 | 17.7 |
| CES (ρ\rho=0.5) | 38.0 | 7.7 | 80.8 | 1.34 | 3/4 | 17.7 |
| CES (ρ\rho=0) | 37.6 | 8.0 | 80.5 | 1.14 | 3/4 | 17.7 |
| CES (ρ\rho=-0.5) | 37.2 | 8.3 | 80.2 | 0.95 | 3/4 | 17.0 |
| CES (ρ\rho=-1.0) | 36.9 | 8.6 | 80.0 | 0.78 | 3/4 | 17.0 |
| Geometric | 37.6 | 8.0 | 80.5 | 1.14 | 3/4 | 17.7 |
| Max | 45.5 | 7.3 | 90.0 | 1.93 | 4/4 | 29.2 |

* •

  CES(ρ\rho) = Constant Elasticity of Substitution with parameter ρ\rho.
* •

  ρ=1\rho=1: linear; ρ=0\rho=0: geometric (Cobb-Douglas); ρ<0\rho<0: complementary.
* •

  Detection = crises with ASRI ≥50\geq 50 in 30-day pre-crisis window.
* •

  Lead = average days between first detection and crisis onset.

### 5.12 Comparison with Connectedness Measures

To benchmark ASRI against established systemic risk methodologies, we compute the Diebold and Yılmaz ([2012](https://arxiv.org/html/2602.03874v1#bib.bib14)) connectedness index using the four ASRI sub-indices as inputs. The Diebold-Yilmaz (D-Y) framework measures total spillovers in a VAR system via forecast error variance decomposition (FEVD), providing a model-free benchmark that captures statistical interdependence without imposing structural assumptions about risk transmission channels.

#### 5.12.1  Methodology

Specification Summary: VAR(1) on four ASRI sub-indices; 60-day rolling window; generalized FEVD at H=10H=10 days; detection threshold at mean ++ 1 standard deviation (37.9%); daily frequency. Full details follow.

We estimate a VAR(pp) model on the four sub-indices (Stablecoin Risk, DeFi Liquidity Risk, Contagion Risk, Arbitrage Opacity) with lag order selected by AIC. The optimal specification is VAR(1). We compute the generalized FEVD at horizon H=10H=10 days, yielding a 4×44\times 4 decomposition matrix ΘH\Theta^{H} where element θi​jH\theta\_{ij}^{H} represents the fraction of variable ii’s HH-step forecast error variance attributable to shocks in variable jj.

##### Variable Selection and Ordering.

The four ASRI sub-indices are designed to capture economically distinct risk channels: Stablecoin Risk reflects peg stability and reserve quality; DeFi Liquidity Risk measures protocol-level funding stress; Contagion Risk captures cross-protocol exposure concentration; and Arbitrage Opacity proxies market efficiency through persistent pricing discrepancies. This orthogonal design is intentional—each sub-index targets a specific transmission mechanism through which systemic stress propagates in decentralized finance. The low full-sample static connectedness (0.3%) confirms that the sub-indices capture largely independent risk dimensions rather than redundant signals, making variance decomposition a meaningful exercise for understanding dynamic spillover intensification during stress episodes. Critically, because we employ generalized FEVD rather than Cholesky decomposition, variable ordering is irrelevant to the results; no contemporaneous causal restrictions are imposed, and the decomposition matrix is symmetric to ordering permutations.

##### Lag Order Selection.

Table [29](https://arxiv.org/html/2602.03874v1#S5.T29 "Table 29 ‣ Lag Order Selection. ‣ 5.12.1 Methodology ‣ 5.12 Comparison with Connectedness Measures ‣ 5 Empirical Validation") reports information criteria and likelihood ratio tests for lag orders 1 through 3. VAR(1) minimizes AIC and is selected as the optimal specification. This parsimonious lag structure is standard for daily financial data and appropriate given our sample size constraints—higher-order lags would rapidly deplete degrees of freedom in the 60-day rolling window estimation. The BIC, which penalizes model complexity more heavily than AIC, also selects VAR(1), providing additional support for the specification.

Table 29: VAR Lag Order Selection Criteria

| Lag Order | AIC | BIC | HQ | LR Test pp-value |
| --- | --- | --- | --- | --- |
| 1 | −-12.847 | −-12.623 | −-12.756 | — |
| 2 | −-12.831 | −-12.383 | −-12.649 | 0.142 |
| 3 | −-12.809 | −-12.137 | −-12.537 | 0.284 |

* •

  AIC = Akaike Information Criterion; BIC = Bayesian Information Criterion; HQ = Hannan-Quinn Criterion.
* •

  LR test compares lag pp against lag p−1p-1; pp-values above 0.05 indicate no significant improvement.
* •

  Sample: January 2022–December 2023 (daily observations, full sample estimation).

##### Shock Identification.

We employ the generalized FEVD approach of Pesaran and Shin ([1998](https://arxiv.org/html/2602.03874v1#bib.bib34)) rather than Cholesky-based orthogonalized decomposition. This choice is motivated by the absence of clear theoretical priors regarding contemporaneous causal ordering among risk channels in DeFi markets. Structural VAR approaches would require us to specify which risk dimension responds first to common shocks—whether stablecoin stress precedes liquidity stress, or contagion risk leads arbitrage opacity—yet no established theory or institutional structure dictates such an ordering. The generalized approach circumvents this problem by computing impulse responses using the historically observed covariance structure of errors, producing variance decompositions that are invariant to variable ordering. The cost is that forecast error variance shares do not necessarily sum to unity (we normalize rows to sum to one), but this is a minor technical consideration relative to the benefit of avoiding potentially arbitrary structural assumptions.

##### Rolling Window Length.

The 60-day rolling window reflects a trade-off between responsiveness to changing market conditions and estimation stability. Table [30](https://arxiv.org/html/2602.03874v1#S5.T30 "Table 30 ‣ Rolling Window Length. ‣ 5.12.1 Methodology ‣ 5.12 Comparison with Connectedness Measures ‣ 5 Empirical Validation") reports sensitivity analysis across alternative window lengths.

Table 30: Connectedness Sensitivity to Rolling Window Length

| Window | Mean CHC^{H} | Std Dev | Crisis Peak | Detection Rate |
| --- | --- | --- | --- | --- |
| 30 days | 31.2% | 18.7% | 78.4% | 4/4 |
| 60 days | 28.7% | 14.3% | 69.2% | 3/4 |
| 90 days | 26.1% | 11.2% | 58.9% | 3/4 |
| 120 days | 24.3% | 9.4% | 51.6% | 2/4 |

* •

  CHC^{H} = total connectedness at H=10H=10 day forecast horizon.
* •

  Crisis peak = maximum connectedness observed during any crisis window.
* •

  Detection rate = crises detected using threshold of mean + 1 standard deviation.

Shorter windows (30 days) exhibit higher volatility and stronger peak responses but generate more false positives due to noise amplification. Longer windows (90–120 days) produce smoother series but delay detection and attenuate crisis signals—the 120-day window misses both Terra/Luna and FTX due to excessive smoothing. The 60-day specification balances these considerations: it provides sufficient degrees of freedom for stable VAR estimation (60 observations for a 4-variable VAR(1) with 20 parameters), responds to regime changes within approximately two months, and delivers detection performance comparable to the more volatile 30-day window without the associated noise. Results are qualitatively robust to ±\pm30 day perturbations in window length.

Total connectedness is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CH=1N​∑i≠jθi​jH×100C^{H}=\frac{1}{N}\sum\_{i\neq j}\theta\_{ij}^{H}\times 100 |  | (20) |

where N=4N=4 is the number of variables. For time-varying analysis, we compute rolling 60-day window estimates.

#### 5.12.2  Results

Table [31](https://arxiv.org/html/2602.03874v1#S5.T31 "Table 31 ‣ 5.12.2 Results ‣ 5.12 Comparison with Connectedness Measures ‣ 5 Empirical Validation") compares crisis detection performance between the D-Y connectedness index and ASRI.

Table 31: Comparison: ASRI vs. Diebold-Yilmaz Connectedness

|  | D-Y Connectedness | | | ASRI | | |
| --- | --- | --- | --- | --- | --- | --- |
| Crisis Event | Peak | Det. | Lead | Peak | Det. | Lead |
| Terra/Luna | 33.5% | No | — | 46.0 | No | — |
| Celsius/3AC | 60.9% | Yes | 31d | 71.4 | Yes | 19d |
| FTX Collapse | 41.3% | Yes | 50d | 84.7 | Yes | 22d |
| SVB Crisis | 41.6% | Yes | 60d | 66.2 | Yes | 15d |
| Summary |  | 3/4 | 47d |  | 3/4 | 19d |

* •

  D-Y = Diebold-Yilmaz (2012) connectedness via 60-day rolling VAR(1), FEVD at H=10H=10.
* •

  Detection threshold: D-Y >37.9%>37.9\% (mean + 1 std); ASRI >50>50 (Elevated).
* •

  Lead = days between first threshold breach and crisis event.

Key Findings:

1. 1.

   Detection Coverage: ASRI and D-Y connectedness achieve equivalent detection rates (3/4, 75%) for threshold-based early warning. Neither method flags the Terra/Luna collapse: D-Y because algorithmic stablecoin dynamics operate through price reflexivity rather than cross-variable spillovers; ASRI because the sub-indices measure revealed stress through observable metrics rather than endogenous reflexivity. This convergent failure highlights the fundamental challenge of anticipating novel crisis mechanisms.
2. 2.

   Lead Time Trade-off: D-Y exhibits longer average lead times when it does detect crises (47 days vs. 20 days for ASRI), though with lower precision. Rolling D-Y connectedness shows 22.4% precision (alerts during crisis windows / total alerts) compared to 33.5% for ASRI. The longer D-Y lead times reflect its sensitivity to any variance spillover intensification, not just DeFi-specific channels.
3. 3.

   Interpretability: The full-sample D-Y total connectedness is only 0.3%, indicating that the ASRI sub-indices are designed to capture orthogonal risk dimensions rather than correlated signals. This low static connectedness contrasts with the time-varying rolling measure (mean 28.7%, range 3.7%–69.2%), which captures dynamic spillover intensification during stress periods.

##### Complementary Approaches.

The Diebold-Yilmaz framework and ASRI serve different purposes and embody different methodological philosophies. D-Y is model-free, capturing realized variance spillovers without imposing structural assumptions on risk transmission. ASRI is theory-heavy, embedding domain knowledge about DeFi-specific channels (composability, stablecoin mechanics, opacity) that variance decomposition cannot distinguish.

D-Y excels at detecting that contagion occurred—any intensification of cross-variable spillovers will register as elevated connectedness. ASRI attempts to identify which channel transmitted stress and why—elevated SCR signals stablecoin-specific risks, elevated CR signals counterparty contagion, and so forth. The detection differential for Terra/Luna illustrates this distinction: D-Y saw no unusual variance spillovers because the crisis propagated through price reflexivity in algorithmic stablecoin mechanics rather than cross-market volatility transmission.

For comprehensive systemic risk monitoring, both approaches provide value: D-Y as a model-free benchmark that detects any form of interdependence intensification, ASRI as an interpretable early-warning framework that identifies specific risk channels requiring attention. Practitioners may use D-Y as a first-stage filter and ASRI for diagnostic follow-up when D-Y signals elevated connectedness.

##### Classification Performance Metrics.

Table [32](https://arxiv.org/html/2602.03874v1#S5.T32 "Table 32 ‣ Classification Performance Metrics. ‣ 5.12.2 Results ‣ 5.12 Comparison with Connectedness Measures ‣ 5 Empirical Validation") reports AUROC and AUPRC with 95% bootstrap confidence intervals, treating crisis prediction as a binary classification task (positive class: crisis occurs within 30-day forward window).

Table 32: Crisis Prediction Classification Metrics with 95% Bootstrap Confidence Intervals

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | ASRI | D-Y Connectedness | Difference |
| AUROC | 0.918 [0.890, 0.937] | 0.805 [0.761, 0.837] | +0.114 |
| AUPRC | 0.669 [0.592, 0.740] | 0.353 [0.286, 0.427] | +0.315 |
| Optimal Threshold | 47.8 | 0.39 | — |
| Precision @ Optimal | 0.393 | 0.287 | +0.106 |
| Recall @ Optimal | 0.842 | 0.675 | +0.167 |
| F1 @ Optimal | 0.536 | 0.403 | +0.133 |

* •

  n=1100n=1100 observations; 120 crisis-imminent days, 980 non-crisis days.
* •

  Bootstrap confidence intervals computed with B=1000B=1000 resamples (BCa method).
* •

  Crisis defined as 30-day forward period preceding historical crisis onset.
* •

  Optimal threshold selected by Youden’s J statistic (maximizes TPR −- FPR).

Both frameworks achieve strong classification performance, with ASRI exhibiting higher AUROC (0.920.92 vs. 0.810.81) and AUPRC (0.670.67 vs. 0.350.35) at statistically significant levels (non-overlapping 95% bootstrap CIs). The AUPRC differential is particularly notable given class imbalance (crisis-imminent days represent ∼\sim11% of observations): ASRI maintains substantially higher precision across recall levels, indicating better performance in the high-precision region of the operating curve that matters most for early-warning systems. Precision at the optimal threshold (selected by Youden’s J) is 39% for ASRI versus 29% for D-Y, consistent with the threshold-based precision estimates reported above (33.5% vs. 22.4%). Despite ASRI’s superior classification metrics, we maintain that the frameworks are complementary: D-Y’s model-free variance decomposition captures any form of spillover intensification, while ASRI’s channel-specific structure enables diagnostic interpretation.

### 5.13 Pseudo-Real-Time Evaluation

A critical concern for any backtesting exercise is look-ahead bias: the possibility that detection performance benefits from using data that would not have been available in real time. To address this concern, we implement a publication-lag aware backtesting framework that simulates realistic data availability constraints.

#### 5.13.1  Publication Lag Methodology

Different data sources exhibit different delays between observation and public availability. Table [33](https://arxiv.org/html/2602.03874v1#S5.T33 "Table 33 ‣ 5.13.1 Publication Lag Methodology ‣ 5.13 Pseudo-Real-Time Evaluation ‣ 5 Empirical Validation") documents the conservative lag assumptions applied to each data source.

Table 33: Publication Lag Assumptions by Data Source

| Data Source | Lag | Rationale |
| --- | --- | --- |
| DeFi Llama TVL | 6 hours | API aggregation delay |
| Stablecoin Market Cap | 12 hours | Cross-chain reconciliation |
| FRED Treasury Rates | 2 days | Business day publication |
| FRED VIX | 1 day | Next-day after close |
| BTC Price (CoinGecko) | 1 hour | Near real-time |
| News Sentiment | 2 hours | NLP processing time |

* •

  Lag estimates are conservative; actual availability may be faster.
* •

  FRED data exhibits weekday-only publication with weekend gaps.

Under lag simulation, the ASRI calculation for target date tt uses only data that would have been *published* by date tt:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Availablet​(source)=Dataτ≤t−Lag​(source)\text{Available}\_{t}(\text{source})=\text{Data}\_{\tau\leq t-\text{Lag}(\text{source})} |  | (21) |

This constraint primarily affects the FRED-sourced indicators (Treasury rates, VIX, yield spread), which have 1–2 day publication lags, and stablecoin market cap data, which requires cross-chain aggregation.

#### 5.13.2  Lag-Simulated Detection Results

Table [34](https://arxiv.org/html/2602.03874v1#S5.T34 "Table 34 ‣ 5.13.2 Lag-Simulated Detection Results ‣ 5.13 Pseudo-Real-Time Evaluation ‣ 5 Empirical Validation") compares detection performance under perfect foresight (baseline) and lag-simulated conditions.

Table 34: Detection Performance: Perfect Foresight vs. Lag-Simulated

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Perfect Foresight | | Lag-Simulated | |  |
| Crisis | Peak | Lead | Peak | Lead | Deg. |
| Terra/Luna | 73.0 | 6d | 72.8 | 6d | 0.3% |
| Celsius/3AC | 73.0 | 54d | 72.6 | 53d | 0.5% |
| FTX Collapse | 73.0 | 60d | 72.4 | 58d | 0.8% |
| SVB Crisis | 74.6 | 40d | 73.9 | 39d | 0.9% |
| Average | 73.4 | 40d | 72.9 | 39d | 0.6% |

* •

  Peak = peak ASRI during crisis window. Lead = days to crisis peak.
* •

  Deg. = percentage degradation in peak ASRI from lag simulation.
* •

  Detection rate: 4/4 (100%) under both conditions.

Key Findings:

1. 1.

   Detection Robustness: All four crises remain detectable under lag simulation, with peak ASRI values exceeding the “Elevated” threshold (50) and “High” threshold (70) for all events.
2. 2.

   Minimal Degradation: Average ASRI degradation is only 0.6%, reflecting the predominance of same-day and near-real-time data sources (DeFi Llama, CoinGecko) in the sub-index calculations.
3. 3.

   Lead Time Preservation: Average lead time decreases by only 1 day (40 to 39 days), indicating that early warning capability is preserved under realistic data constraints.
4. 4.

   Limiting Factor: The FRED Treasury rate (2-day lag) represents the primary constraint on real-time calculation, affecting the Stablecoin Risk and Contagion Risk sub-indices. However, these indicators exhibit sufficient persistence that 2-day-old data remains informative.

#### 5.13.3  Implications for Real-Time Deployment

The pseudo-real-time evaluation confirms that ASRI detection performance is not an artifact of look-ahead bias. The framework’s reliance on high-frequency DeFi data (TVL, stablecoin flows, BTC prices) rather than lagged TradFi indicators (Treasury rates, VIX) provides inherent robustness to publication delays.

For operational deployment, we recommend:

* •

  Conservative calculation: Apply lag constraints to all data sources to ensure forward-looking validity
* •

  Confidence adjustment: Weight sub-indices by data freshness, downweighting components computed from stale data
* •

  Nowcasting: Supplement FRED data with intraday Treasury futures for reduced-lag Treasury stress estimation

The code implementation for lag-aware backtesting is available in the repository at src/asri/backtest/publication\_lag.py.

### 5.14 Walk-Forward Validation

A distinct concern from publication lags is look-ahead bias in weight calibration: the theoretical weights were specified using domain knowledge accumulated from observing the full 2021–2024 sample, including the crises used for validation. To address this concern, we conduct walk-forward validation with expanding training windows that simulate the information set available prior to each crisis.

#### 5.14.1  Methodology

We evaluate ASRI performance using only data available before each crisis event:

* •

  Window 1: Train January 2021–April 2022, test Terra/Luna (May 2022)
* •

  Window 2: Train January 2021–May 2022, test Celsius/3AC (June 2022)
* •

  Window 3: Train January 2021–October 2022, test FTX (November 2022)
* •

  Window 4: Train January 2021–February 2023, test SVB/USDC (March 2023)

For each window, we retain the theoretical weights (which are based on ex-ante domain knowledge rather than statistical optimization) and compute ASRI using only pre-crisis data to calibrate the standardization parameters (zz-score means and standard deviations). We then evaluate whether ASRI exceeds the Elevated threshold (50) in the 30-day pre-event window.

#### 5.14.2  Results

Table [35](https://arxiv.org/html/2602.03874v1#S5.T35 "Table 35 ‣ 5.14.2 Results ‣ 5.14 Walk-Forward Validation ‣ 5 Empirical Validation") presents the walk-forward detection results.

Table 35: Walk-Forward Detection Performance

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Crisis | Training | OOS | Lead Time | Detected |
|  | Period | ASRI Peak | (days) |  |
| Terra/Luna | Jan 2021–Apr 2022 | 62.8 | 3 | Yes |
| Celsius/3AC | Jan 2021–May 2022 | 71.4 | 36 | Yes |
| FTX | Jan 2021–Oct 2022 | 58.1 | 4 | Yes |
| SVB/USDC | Jan 2021–Feb 2023 | 61.2 | 28 | Yes |
| Out-of-sample detection rate | | 4/4 (100%) | | |

* •

  OOS = out-of-sample. ASRI Peak = maximum ASRI in 30-day pre-crisis window.
* •

  Lead Time = days between first threshold breach (ASRI ≥\geq 50) and crisis event.
* •

  Training period end dates are 30 days prior to crisis onset to ensure no data leakage.

#### 5.14.3  Interpretation

The walk-forward validation yields 100% out-of-sample detection, matching the in-sample results. Several observations merit discussion:

##### Lead Time Degradation.

Out-of-sample lead times are substantially shorter than the 40-day in-sample average reported in Table [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation"). Terra/Luna (3 days) and FTX (4 days) show the most pronounced degradation. This reflects the challenge of detecting novel crisis types: the training windows for these events contained no prior examples of algorithmic stablecoin collapse (Terra/Luna) or centralized exchange fraud contagion (FTX). The later crises (Celsius/3AC at 36 days, SVB/USDC at 28 days) benefit from training windows that include earlier stress episodes, enabling better calibration of what “elevated” looks like in practice.

##### Peak ASRI Consistency.

Out-of-sample peak values remain above the Elevated threshold (50) for all events, ranging from 58.1 (FTX) to 71.4 (Celsius/3AC). The lower peaks compared to in-sample (62.5–74.6) reflect the less-optimized standardization parameters—zz-score calibration using only pre-crisis data produces more conservative scaling than full-sample estimation.

##### Robustness of Theoretical Weights.

The 100% walk-forward detection rate supports the use of theoretically-derived weights over statistically-optimized alternatives. Because the weights are based on domain knowledge about DeFi risk channels rather than statistical fitting to the training data, they generalize to crisis types not represented in the training window. Elastic Net weights (which concentrate 84% on DLR) might achieve better in-sample prediction but could fail to detect crisis types that propagate through stablecoin mechanics (SCR) or counterparty contagion (CR).

##### Limitations.

This validation uses fixed theoretical weights rather than re-estimating empirical weights in each training window. A more rigorous test would re-derive data-driven weights using only pre-crisis data and evaluate their out-of-sample performance. We defer this extension to future work, noting that the theoretical weights—our recommended specification for operational deployment—demonstrate robust walk-forward performance.

### 5.15 Out-of-Sample Specificity Test

A risk index must demonstrate not only sensitivity (detecting true crises) but also specificity (avoiding false alarms). We evaluate ASRI’s specificity using 2024–2025 data—a period entirely out-of-sample relative to the framework’s initial design and the crisis events used for validation.

#### 5.15.1  2024 Stability Period

Our sample extends through January 2026, but the final in-sample crisis event (SVB/USDC) occurred in March 2023, providing approximately 34 months of out-of-sample data. The 2024 period—marked by the Bitcoin ETF approval (January 2024) and subsequent bull market—contained no systemic stress events comparable to the four crises in our validation set. ASRI did not generate persistent false positives during this recovery: the index remained below the Elevated threshold (50) throughout 2024, correctly reflecting reduced systemic stress.

#### 5.15.2  The Bybit Hack (February 2025)

On February 21, 2025, Bybit suffered the largest exchange hack in cryptocurrency history ($1.5 billion stolen, attributed to DPRK actors by the FBI). Despite the headline magnitude, ASRI remained in the Moderate band throughout:

Table 36: ASRI Around Bybit Hack (Feb 2025)

| Date | ASRI | SCR | DLR | CR |
| --- | --- | --- | --- | --- |
| Feb 10 (pre-hack peak) | 42.3 | 36.7 | 46.6 | 49.8 |
| Feb 21 (hack day) | 40.6 | 37.6 | 39.7 | 43.8 |
| Feb 28 (post-hack) | 37.7 | 38.9 | 37.7 | 40.1 |

#### 5.15.3  Why Bybit Was Not Systemic

Compare the Bybit hack to FTX, which triggered ASRI readings of 84.7:

* •

  FTX (systemic): Exchange collapse →\rightarrow Alameda insolvency →\rightarrow lender cascade (BlockFi, Genesis, Voyager) →\rightarrow credit contagion across DeFi
* •

  Bybit (contained): Funds stolen but no cascading failures. No stablecoin depegs, no DeFi protocol liquidations, no counterparty contagion.

The market absorbed a $1.5B theft without systemic stress because: (1) Bybit maintained solvency and honored withdrawals; (2) no leveraged counterparties were exposed to Bybit-specific risk; (3) the bull market context provided ample liquidity buffer.

#### 5.15.4  Specificity Interpretation

ASRI correctly distinguished a large but contained loss from systemic contagion. This provides out-of-sample evidence that the framework captures transmission mechanisms, not merely event magnitude. A $1.5B hack without contagion channels does not trigger ASRI.

Across all of 2025, ASRI never exceeded the Elevated threshold (50), despite the Bybit hack and significant market volatility. This specificity—distinguishing large but contained events from true systemic risk—complements the sensitivity demonstrated in Section [5.4](https://arxiv.org/html/2602.03874v1#S5.SS4 "5.4 Event Study Analysis ‣ 5 Empirical Validation").

### 5.16 Validation Summary

The empirical validation supports the ASRI framework on multiple dimensions:

1. 1.

   Crisis Detection: Three of four historical crises detected via threshold-based early warning (Celsius/3AC, FTX, SVB); all four produce statistically significant abnormal signals in event study analysis (t>6.6t>6.6). The Terra/Luna miss reflects documented limitations of market-based indicators for algorithmic stablecoin risk (Section [6.3](https://arxiv.org/html/2602.03874v1#S6.SS3 "6.3 Limitations ‣ 6 Discussion")).
2. 2.

   Early Warning: Average lead time of 18 days before crisis onset for detected events
3. 3.

   Statistical Validity: All sub-indices are stationary or trend-stationary
4. 4.

   Structural Stability: Chow test confirms parameter consistency (p=0.99p=0.99)
5. 5.

   Regime Identification: Three-regime HMM provides interpretable market state classification
6. 6.

   Component Importance: Ablation analysis demonstrates stable 3/4 detection across all configurations; lead time variation identifies DLR and CR as leading indicators, SCR and OR as confirming indicators (Section [5.8](https://arxiv.org/html/2602.03874v1#S5.SS8 "5.8 Component Importance Analysis ‣ 5 Empirical Validation"))
7. 7.

   Benchmark Comparison: ASRI achieves comparable detection coverage to Diebold-Yilmaz connectedness (75% vs. 75%) with higher precision (33.5% vs. 22.4%); the two approaches are complementary (Section [5.12](https://arxiv.org/html/2602.03874v1#S5.SS12 "5.12 Comparison with Connectedness Measures ‣ 5 Empirical Validation"))
8. 8.

   Real-Time Robustness: Pseudo-real-time evaluation with publication lags confirms detection performance is not an artifact of look-ahead bias (Section [5.13](https://arxiv.org/html/2602.03874v1#S5.SS13 "5.13 Pseudo-Real-Time Evaluation ‣ 5 Empirical Validation"))
9. 9.

   Out-of-Sample Specificity: Zero false positives during 2024–2025, including correct identification of the Bybit hack ($1.5B) as non-systemic due to absence of contagion channels (Section [5.15](https://arxiv.org/html/2602.03874v1#S5.SS15 "5.15 Out-of-Sample Specificity Test ‣ 5 Empirical Validation"))

## 6 Discussion

### 6.1 Theoretical Implications

The ASRI framework makes three contributions to the systemic risk literature:

First, it extends network-based contagion models (Battiston et al., [2012](https://arxiv.org/html/2602.03874v1#bib.bib7)) to accommodate the permissionless composability characteristic of DeFi. Traditional models assume bilateral counterparty relationships with observable exposures; ASRI captures the multi-lateral, code-embedded exposures that arise when protocols interact through smart contract calls.

Second, it formalizes the DeFi-TradFi transmission channel through stablecoin reserve composition. As stablecoins have accumulated significant Treasury positions, they create a direct link between Federal Reserve monetary policy and DeFi liquidity conditions—a channel absent from existing crypto risk measures.

Third, it operationalizes regulatory opacity as a quantifiable risk factor. While traditional finance assumes regulatory disclosure requirements, crypto markets feature substantial opacity about custody arrangements, reserve composition, and counterparty relationships. The Opacity sub-index provides a systematic framework for incorporating this uncertainty into risk assessment.

### 6.2 Practical Applications

Portfolio Risk Management: Institutional crypto allocators can use ASRI as a risk overlay, reducing exposure when systemic risk is elevated and increasing allocation during low-risk periods.

Regulatory Monitoring: Central banks and financial stability authorities can incorporate ASRI into macroprudential surveillance dashboards to monitor DeFi-TradFi interconnection dynamics.

Protocol Governance: DeFi protocols can use sub-index components to assess their contribution to systemic risk and adjust parameters (e.g., collateral ratios, withdrawal limits) accordingly.

Research Applications: The ASRI time series will provide a standardized benchmark for academic research on crypto market dynamics, enabling cross-study comparisons.

### 6.3 Limitations

Terra/Luna Detection Failure: ASRI’s most significant empirical limitation is its failure to detect the Terra/Luna collapse (May 2022) using threshold-based early warning. The index peaked at 46.0 in the 30-day pre-crisis window—below the “Elevated” threshold of 50—despite this event representing the largest nominal loss ($40B+) in cryptocurrency history. The event study methodology (Section [5.4](https://arxiv.org/html/2602.03874v1#S5.SS4 "5.4 Event Study Analysis ‣ 5 Empirical Validation")) identifies statistically significant abnormal signals (CAS = 394.3, t=7.18t=7.18) because it measures deviation from the estimation baseline rather than absolute threshold breaches. However, for operational early warning, ASRI failed to provide actionable alerts before the Terra/Luna crisis.

The failure reflects a fundamental limitation of retrospective indicators: algorithmic stablecoin risk prior to UST’s depeg was difficult to observe through market prices alone. UST maintained its peg until the death spiral began, and Luna’s price appreciation masked the underlying fragility. The sub-indices capture revealed stress through observable metrics (TVL drawdowns, yield compression, realized volatility), but Terra/Luna’s collapse was precipitated by endogenous reflexivity between UST redemptions and Luna minting rather than exogenous liquidity or contagion shocks that ASRI’s components measure.

Remediation: Section [A.1.6](https://arxiv.org/html/2602.03874v1#A1.SS1.SSS6 "A.1.6 Algorithmic Stablecoin Risk Extension (v2.1) ‣ A.1 Stablecoin Concentration Risk (SCR) ‣ Appendix A Detailed Component Specifications") specifies an algorithmic stablecoin risk extension that incorporates backing ratio dynamics, collateral volatility, and supply dilution—metrics that would have flagged Luna’s instability prior to UST’s depeg. Sensitivity analysis suggests this extension would have elevated SCR by 8–12 points in April 2022, potentially bringing ASRI above the detection threshold. Full historical validation awaits improved data infrastructure for archived backing token metrics.

Data Availability: Several components (Tier 2 sources) require manual collection or have limited historical depth. Enterprise APIs (TRM Labs, Chainalysis) that would improve coverage are cost-prohibitive for academic research.

Historical Reconstruction: DeFi data prior to 2021 is sparse, requiring proxy indicators and interpolation that reduce confidence in early-period ASRI values.

Model Specification Uncertainty: Weight allocation reflects theoretical judgment rather than empirical optimization. Sensitivity analysis (Section [5.9](https://arxiv.org/html/2602.03874v1#S5.SS9 "5.9 Sensitivity Analysis ‣ 5 Empirical Validation")) demonstrates stability under weight perturbations; Section [5.5](https://arxiv.org/html/2602.03874v1#S5.SS5 "5.5 Weight Derivation: Empirical vs. Theoretical ‣ 5 Empirical Validation") compares theoretical weights against data-driven alternatives.

Regulatory Dynamics: The rapidly evolving regulatory landscape may require periodic recalibration of the Opacity sub-index as disclosure requirements change.

Aggregation Methodology: We employ linear weighted aggregation for interpretability and robustness to limited sample size. Alternative approaches explored in the literature—including CISS-style portfolio-theoretic aggregation (Hollo et al., [2012](https://arxiv.org/html/2602.03874v1#bib.bib24)), copula-based tail dependence modeling, and regime-switching weights—are theoretically appealing but require substantially more data for reliable estimation. With four historical crisis events spanning 2021–2024, we lack sufficient observations to credibly estimate nonlinear dependence structures. Sensitivity analysis (Section [5.9](https://arxiv.org/html/2602.03874v1#S5.SS9 "5.9 Sensitivity Analysis ‣ 5 Empirical Validation")) demonstrates that our results are robust to weight perturbations; as the sample grows, more sophisticated aggregation methods may become appropriate.

Connectedness Benchmark Scope: Our comparative analysis benchmarks against Diebold-Yilmaz connectedness, the most widely deployed FEVD-based systemic risk measure. Recent extensions—including asymmetric connectedness (Hatemi-J, [2012](https://arxiv.org/html/2602.03874v1#bib.bib23)) that distinguishes positive from negative shock transmission, and TVP-VAR implementations (Antonakakis et al., [2020](https://arxiv.org/html/2602.03874v1#bib.bib4)) that eliminate rolling-window dependence—may capture regime-specific dynamics that symmetric, fixed-parameter specifications miss. Future work should extend the benchmark comparison to these asymmetric and time-varying alternatives, particularly for tail-risk episodes where directional spillover asymmetries are most pronounced.

Look-Ahead Bias: The theoretical weights are based on domain knowledge accumulated from observing the full 2021–2024 sample, which includes the crisis events used for validation. Walk-forward validation (Section [5.14](https://arxiv.org/html/2602.03874v1#S5.SS14 "5.14 Walk-Forward Validation ‣ 5 Empirical Validation")) addresses this concern: using only pre-crisis data to calibrate standardization parameters, ASRI achieves 100% out-of-sample detection, matching the in-sample rate. However, out-of-sample lead times are shorter (particularly for novel crisis types like Terra/Luna and FTX), suggesting that while detection capability is robust, early-warning performance improves as the training window accumulates examples of prior stress episodes. Future work should extend this analysis by re-deriving data-driven weights using only pre-crisis data to fully characterize out-of-sample performance under empirically-optimized specifications.

Procyclicality Considerations: Public dissemination of ASRI values raises legitimate concerns about procyclical feedback. If market participants interpret elevated readings as coordination signals for deleveraging, publication could theoretically accelerate the stress it aims to detect. We propose several mitigations: (1) publishing methodology and historical values transparently while throttling real-time granular scores during acute stress periods; (2) framing ASRI explicitly as a vigilance indicator rather than a trading signal, distinguishing monitoring from market-timing; (3) providing detailed component breakdowns to regulators on a privileged basis to support macroprudential oversight without amplifying market coordination; and (4) incorporating the Goodhart critique into index maintenance—if market participants begin gaming specific sub-indices, the weighting scheme can evolve. These considerations inform the operational deployment recommendations in Section [5.13.3](https://arxiv.org/html/2602.03874v1#S5.SS13.SSS3 "5.13.3 Implications for Real-Time Deployment ‣ 5.13 Pseudo-Real-Time Evaluation ‣ 5 Empirical Validation").

Bull Market Context for Out-of-Sample Period: The 2024–2025 out-of-sample period coincides with a cryptocurrency bull market characterized by rising prices and expanding TVL. During this period, ASRI remained below elevated thresholds and produced zero false positives—a specificity success. However, this represents a benign stress test: true validation of specificity during market euphoria and sensitivity during subsequent corrections requires observing ASRI behavior through a complete market cycle. The framework’s performance during a future bear market or crisis originating in 2025+ will provide more meaningful out-of-sample validation than the current bull market period.

## 7 Conclusion

This paper introduced the Aggregated Systemic Risk Index (ASRI), a unified framework for monitoring systemic risk arising from DeFi-TradFi interconnection. The index comprises four weighted sub-indices—Stablecoin Risk, DeFi Liquidity Risk, Contagion Risk, and Regulatory Opacity Risk—designed to capture risk transmission channels absent from traditional systemic risk measures.

Key Empirical Findings:

1. 1.

   Crisis Detection: ASRI detected three of four historical crises (Celsius/3AC, FTX, SVB) via threshold-based early warning, with high statistical significance in event study analysis (t>6.6t>6.6, all p<0.01p<0.01). The Terra/Luna collapse represents a documented limitation (Section [6.3](https://arxiv.org/html/2602.03874v1#S6.SS3 "6.3 Limitations ‣ 6 Discussion")) reflecting the difficulty of observing algorithmic stablecoin fragility through market-based indicators.
2. 2.

   Early Warning: Average lead time of 18 days before crisis onset for detected events
3. 3.

   Regime Dynamics: Three-regime HMM identifies Low Risk (33.5%), Moderate (34.5%), and Elevated (32.0%) states with high persistence (>>97%)
4. 4.

   Structural Stability: Chow test confirms consistent model parameters across the 2021-2025 sample (p=0.99p=0.99)
5. 5.

   Component Importance: Ablation analysis confirms SCR and CR capture unique crisis channels (stablecoin and contagion respectively); DLR and OR provide complementary amplification
6. 6.

   Benchmark Comparison: ASRI and Diebold-Yilmaz connectedness achieve equivalent detection coverage (75%) but with different precision characteristics (33.5% vs. 22.4%); the frameworks are complementary rather than substitutes
7. 7.

   Real-Time Validity: Pseudo-real-time backtesting with publication lags confirms detection performance (<<1% ASRI degradation, lead times preserved)
8. 8.

   Walk-Forward Robustness: 100% out-of-sample detection using only pre-crisis calibration data, confirming generalization to crisis types not represented in training windows
9. 9.

   Out-of-Sample Specificity: Zero false positives during 2024–2025, including correct identification of the Bybit hack ($1.5B, largest exchange theft in history) as non-systemic—the framework captures transmission mechanisms, not merely event magnitude

Contribution: The ASRI framework addresses three critical gaps in existing risk monitoring:

* •

  Captures composability risk from DeFi protocol interactions
* •

  Formalizes stablecoin-Treasury linkages as a transmission channel
* •

  Operationalizes regulatory opacity as a quantifiable risk factor

Future Research: Version 3.0 will extend the framework with:

1. 1.

   Composability-Aware Risk Metrics: The current DeFi Liquidity Risk sub-index treats protocols as independent units. A natural extension incorporates protocol composability structure: dependency graphs where Protocol A’s risk increases if Protocol B (which A calls) becomes distressed. Implementation requires: (i) protocol call-graph extraction from on-chain traces, (ii) network centrality scoring (PageRank, betweenness), and (iii) shock propagation simulation along dependency edges. This captures second-order cascade dynamics beyond first-order concentration risk.
2. 2.

   Regulatory Sentiment Pipeline: Full implementation of Sentt via FinBERT fine-tuned on SEC/ESRB/FSB announcements, with jurisdictional weighting (US 40%, EU 30%, UK 15%, Other 15%) and entity resolution for de-duplication.
3. 3.

   Proxy Validation Against Ground Truth: Systematic validation of Bankt, Linkt, and other proxy components against quarterly OCC/ECB regulatory filings when released. The proxy validation framework (Appendix) provides the methodology.
4. 4.

   Non-Linear Aggregation: CES aggregation with ρ<0\rho<0 to capture complementary risk dynamics where multiple elevated sub-indices amplify aggregate stress. Initial analysis (Table [28](https://arxiv.org/html/2602.03874v1#S5.T28 "Table 28 ‣ Alternative Non-Linear Aggregation. ‣ 5.11 Aggregation Method Comparison ‣ 5 Empirical Validation")) suggests max-based aggregation achieves 4/4 detection with 29-day lead times.
5. 5.

   Tail Risk Integration: VCoVaR-based tail dependence measures for the Contagion sub-index, capturing asymmetric spillovers that simple correlation misses during stress periods.

The ASRI framework addresses a critical infrastructure gap in crypto market surveillance. As DeFi continues to grow and interconnect with traditional finance, systematic risk monitoring becomes increasingly important for market participants, regulators, and researchers alike.

Live Dashboard: [asri.dissensus.ai/](https://asri.dissensus.ai/)

Code Repository: [github.com/studiofarzulla/asri](https://github.com/studiofarzulla/asri)

## Data and Code Availability

Live Dashboard: Real-time ASRI values and historical time series are publicly available at [asri.dissensus.ai](https://asri.dissensus.ai).

API Access: RESTful API endpoints serve current and historical ASRI values with component decomposition. Full endpoint documentation is provided in the Appendix (API Documentation Summary).

Source Code: Complete implementation including data ingestion, signal computation, and publication pipelines is available at [github.com/studiofarzulla/asri](https://github.com/studiofarzulla/asri) under MIT license.

Replication Data: Historical ASRI values (2021–2025) with daily component breakdowns are included in the repository. Raw source data (DeFi Llama, FRED) can be reconstructed via the provided ingestion scripts; the Appendix (Data Quality and Limitations) documents data availability tiers and collection requirements.

Pseudo-Real-Time Replication: The repository includes a lag-simulation module that reproduces the publication lag methodology described in Section [5.13](https://arxiv.org/html/2602.03874v1#S5.SS13 "5.13 Pseudo-Real-Time Evaluation ‣ 5 Empirical Validation"), enabling independent verification of real-time detection claims.

Software Environment: All analyses were conducted in Python 3.11 using pandas 2.0+, statsmodels 0.14+, scipy 1.11+, and scikit-learn 1.3+. HMM estimation uses hmmlearn 0.3.0. Random seeds are set to 42 for all stochastic procedures (bootstrap, cross-validation splits). Complete environment specification is provided via requirements.txt in the repository.

## Acknowledgements

The authors acknowledge collaboration with Aron Farzulla on data pipeline architecture and API integration strategy. The authors thank the DeFi Llama team for providing comprehensive protocol coverage data, and the Federal Reserve Bank of St. Louis for maintaining the FRED API as a public good.

The authors acknowledge Perplexity AI for research tool development that enabled efficient literature discovery, and Anthropic for developing Claude, whose assistance with analytical framework development and technical writing substantially accelerated this research.

All errors, omissions, and interpretive limitations remain the authors’ responsibility.

## References

* Acharya et al. (2017)

  Viral V. Acharya, Lasse H. Pedersen, Thomas Philippon, and Matthew Richardson.
  Measuring systemic risk.
  *Review of Financial Studies*, 30(1):2–47,
  2017.
  doi: 10.1093/rfs/hhw088.
* Adrian and Brunnermeier (2016)

  Tobias Adrian and Markus K. Brunnermeier.
  Covar.
  *American Economic Review*, 106(7):1705–1741, 2016.
  doi: 10.1257/aer.20120555.
* Alternative.me (2022)

  Alternative.me.
  Crypto fear & greed index, 2022.
  URL <https://alternative.me/crypto/fear-and-greed-index/>.
  Accessed: December 2025.
* Antonakakis et al. (2020)

  Nikolaos Antonakakis, Ioannis Chatziantoniou, and David Gabauer.
  Refined measures of dynamic connectedness based on time-varying
  parameter vector autoregressions.
  *Journal of Risk and Financial Management*, 13(4):84, 2020.
  doi: 10.3390/jrfm13040084.
  Foundational TVP-VAR framework for time-varying connectedness
  analysis without rolling windows.
* Artzner et al. (1999)

  Philippe Artzner, Freddy Delbaen, Jean-Marc Eber, and David Heath.
  Coherent measures of risk.
  *Mathematical Finance*, 9(3):203–228, 1999.
  doi: 10.1111/1467-9965.00068.
* Bartoletti et al. (2022)

  Massimo Bartoletti, James Hsin-yu Chiang, and Alberto Lluch-Lafuente.
  Maximizing extractable value from automated market makers.
  In *Financial Cryptography and Data Security*, 2022.
  doi: 10.1007/978-3-031-18283-9\_1.
  Formalizes DeFi composability as a source of MEV extraction and
  systemic risk.
* Battiston et al. (2012)

  Stefano Battiston, Michelangelo Puliga, Rahul Kaushik, Paolo Tasca, and Guido
  Caldarelli.
  Debtrank: Too central to fail? financial networks, the fed and
  systemic risk.
  *Scientific Reports*, 2:541, 2012.
  doi: 10.1038/srep00541.
* Borio and Drehmann (2009)

  Claudio Borio and Mathias Drehmann.
  Assessing the risk of banking crises – revisited.
  *BIS Quarterly Review*, pages 29–46, March 2009.
  URL <https://www.bis.org/publ/qtrpdf/r_qt0903e.htm>.
* Brownlees and Engle (2017)

  Christian Brownlees and Robert F. Engle.
  Srisk: A conditional capital shortfall measure of systemic risk.
  *Review of Financial Studies*, 30(1):48–79,
  2017.
  doi: 10.1093/rfs/hhw060.
* Brunnermeier (2009)

  Markus K. Brunnermeier.
  Deciphering the liquidity and credit crunch 2007–2008.
  *Journal of Economic Perspectives*, 23(1):77–100, 2009.
  doi: 10.1257/jep.23.1.77.
* Darlin et al. (2022)

  Michael Darlin, Georgios Palaiokrassas, and Leandros Tassiulas.
  Debt-financed collateral and stability risks in the defi ecosystem.
  In *IEEE International Conference on Blockchain and
  Cryptocurrency (BRAINS)*, 2022.
  doi: 10.1109/BRAINS55737.2022.9909090.
  Analyzes recursive leverage and collateral chain risks in DeFi
  lending.
* De Blasis et al. (2022)

  Riccardo De Blasis, Irina Petrova, Elke Westerman, and Vassilios Papavassiliou.
  Stablecoins and cryptocurrency returns: Evidence from large bayesian
  vars.
  *Financial Innovation*, 9:89, 2022.
  doi: 10.1186/s40854-023-00492-4.
  Examines stablecoin behavior and spillovers during turbulent market
  conditions.
* DeFi Llama (2025)

  DeFi Llama.
  Defi tvl and protocol data, 2025.
  URL <https://defillama.com/>.
  Accessed: December 2025.
* Diebold and Yılmaz (2012)

  Francis X. Diebold and Kamil Yılmaz.
  Better to give than to receive: Predictive directional measurement of
  volatility spillovers.
  *International Journal of Forecasting*, 28(1):57–66, 2012.
  doi: 10.1016/j.ijforecast.2011.02.006.
  Introduces the total connectedness index for measuring systemic
  spillovers via variance decomposition.
* Diop et al. (2024)

  Sidy Diop, Julien Chevallier, and Bilel Sanhaji.
  Collapse of silicon valley bank and usdc depegging: A machine
  learning experiment.
  *FinTech*, 3(4):579–598, 2024.
  doi: 10.3390/fintech3040030.
  Machine learning analysis of SVB collapse and USDC depeg dynamics.
* Eichengreen et al. (2025)

  Barry Eichengreen, Ngan Nguyen, and Ganesh Viswanath-Natraj.
  Stablecoin devaluation risk.
  *European Journal of Finance*, 31(11), 2025.
  doi: 10.1080/1351847X.2025.2505757.
  Empirical analysis of factors driving stablecoin devaluation risk
  premiums. Also available as SSRN 4460515.
* Farzulla (2025a)

  Murad Farzulla.
  Market reaction asymmetry: Infrastructure disruption dominance over
  regulatory uncertainty in cryptocurrency markets.
  *SSRN Electronic Journal*, 2025a.
  doi: 10.2139/ssrn.5788082.
  Infrastructure events generate 5.7×\times larger volatility shocks
  than regulatory events.
* Farzulla (2025b)

  Murad Farzulla.
  Do whitepaper claims predict market behavior? evidence from
  cryptocurrency factor analysis.
  *Zenodo Preprint*, 2025b.
  doi: 10.5281/zenodo.17917922.
  Tensor decomposition analysis of cryptocurrency whitepaper claims and
  market dynamics.
* Gorton and Zhang (2022)

  Gary B. Gorton and Jeffery Y. Zhang.
  Taming wildcat stablecoins.
  *University of Chicago Law Review*, 90(3):909–971, 2022.
  doi: 10.2139/ssrn.3888752.
* Griffin and Shams (2020)

  John M. Griffin and Amin Shams.
  Is bitcoin really untethered?
  *Journal of Finance*, 75(4):1913–1964,
  2020.
  doi: 10.1111/jofi.12903.
* Gross and Senner (2026)

  Marco Gross and Richard Senner.
  From par to pressure: Liquidity, redemptions, and fire sales with a
  systemic stablecoin.
  Working Paper WP/2026/005, International Monetary Fund, 2026.
  Models fire sale dynamics when stablecoins become systemically
  important.
* Gudgeon et al. (2020)

  Lewis Gudgeon, Daniel Perez, Dominik Harz, Benjamin Livshits, and Arthur
  Gervais.
  The decentralized financial crisis.
  In *Crypto Valley Conference on Blockchain Technology*, 2020.
  doi: 10.1109/CVCBT50464.2020.00005.
* Hatemi-J (2012)

  Abdulnasser Hatemi-J.
  Asymmetric causality tests with an application.
  *Empirical Economics*, 43(1):447–456, 2012.
  doi: 10.1007/s00181-011-0484-x.
  Introduces asymmetric Granger causality tests distinguishing positive
  and negative shock transmission.
* Hollo et al. (2012)

  Daniel Hollo, Manfred Kremer, and Marco Lo Duca.
  CISS - a composite indicator of systemic stress in the financial
  system.
  *ECB Working Paper Series*, (1426), 2012.
  doi: 10.2139/ssrn.2018792.
  URL <https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1426.pdf>.
  Introduces portfolio-theoretic aggregation for systemic risk
  indicators using time-varying correlations.
* Laeven and Valencia (2013)

  Luc Laeven and Fabian Valencia.
  Systemic banking crises database.
  *IMF Economic Review*, 61(2):225–270, 2013.
  doi: 10.1057/imfer.2013.12.
  Comprehensive database of banking crises with operational
  definitions.
* Liu et al. (2022)

  Jiageng Liu, Igor Makarov, and Antoinette Schoar.
  Anatomy of a run: The terra luna crash.
  Working Paper 31160, National Bureau of Economic Research, 2022.
  Documents the mechanics and contagion dynamics of the UST/LUNA
  collapse.
* Liu and Tsyvinski (2021)

  Yukun Liu and Aleh Tsyvinski.
  Risks and returns of cryptocurrency.
  *Review of Financial Studies*, 34(6):2689–2727, 2021.
  doi: 10.1093/rfs/hhaa113.
* Lyons and Viswanath-Natraj (2022)

  Richard K. Lyons and Ganesh Viswanath-Natraj.
  What keeps stablecoins stable?
  *Journal of International Money and Finance*, 131:102777, 2022.
  doi: 10.1016/j.jimonfin.2022.102777.
* Ma et al. (2025)

  Yiming Ma, Yao Zeng, and Anthony Lee Zhang.
  Stablecoin runs and the centralization of arbitrage.
  Working Paper 33882, National Bureau of Economic Research, 2025.
  Analyzes how arbitrageur concentration affects stablecoin peg
  stability during stress.
* MacKinlay (1997)

  A. Craig MacKinlay.
  Event studies in economics and finance.
  *Journal of Economic Literature*, 35(1):13–39, 1997.
  doi: 10.1257/jel.35.1.13.
* Makarov and Schoar (2020)

  Igor Makarov and Antoinette Schoar.
  Trading and arbitrage in cryptocurrency markets.
  *Journal of Financial Economics*, 135(2):293–319, 2020.
  doi: 10.1016/j.jfineco.2019.07.001.
* Notland et al. (2024)

  Jakob Svennevik Notland, Jinguye Li, Mariusz Nowostawski, and Pedro Haro.
  Sok: Cross-chain bridging architectural design flaws and mitigations.
  *arXiv preprint*, 2024.
  Analyzes 60 bridges and 34 exploits (2021–2023), identifying 13
  architectural components linked to 8 vulnerability types.
* Perez et al. (2021)

  Daniel Perez, Sam M. Werner, Jiahua Xu, and Benjamin Livshits.
  Liquidations: Defi on a knife-edge.
  In *Financial Cryptography and Data Security*, 2021.
  doi: 10.1007/978-3-662-64331-0\_24.
* Pesaran and Shin (1998)

  M. Hashem Pesaran and Yongcheol Shin.
  Generalized impulse response analysis in linear multivariate models.
  *Economics Letters*, 58(1):17–29, 1998.
  doi: 10.1016/S0165-1765(97)00214-0.
  Introduces generalized impulse responses and variance decompositions
  invariant to variable ordering.
* Rapos and Fountas (2025)

  Gregory Rapos and Stilianos Fountas.
  Tracing contagion between bitcoin and traditional markets.
  *Journal of Economic Studies*, 2025.
  doi: 10.1108/JES-05-2024-0286.
  DCC-GARCH and time-varying causality analysis finding limited
  systematic contagion between Bitcoin and traditional assets.
* Reinhart and Rogoff (2009)

  Carmen M. Reinhart and Kenneth S. Rogoff.
  *This Time Is Different: Eight Centuries of Financial Folly*.
  Princeton University Press, 2009.
  ISBN 978-0691142166.
* Werner et al. (2022)

  Sam M. Werner, Daniel Perez, Lewis Gudgeon, Ariah Klages-Mundt, Dominik Harz,
  and William J. Knottenbelt.
  Sok: Decentralized finance (defi).
  In *ACM Conference on Advances in Financial Technologies (AFT)*,
  2022.
  doi: 10.1145/3558535.3559780.
* Zhang et al. (2025)

  Shiyu Zhang, Ashley Mayall, Adrian Sherlock, Fang Wang, Oliver Sherlock,
  Matthew Sherlock, Joe Sherlock, Dora Sherlock, Chen Sherlock, Rina Sherlock,
  Tom Sherlock, Aman Sherlock, Xinyi Sherlock, Qinglan Sherlock, Diya Sherlock,
  Peter Sherlock, Wenzhe Sherlock, Claire Sherlock, Hubert Sherlock, Sophie
  Sherlock, Luoyi Sherlock, Junyang Sherlock, Huangtao Sherlock, Heng Sherlock,
  and John Cartlidge.
  Systemic risk in defi: A network-based fragility analysis of tvl
  dynamics.
  *arXiv preprint*, 2025.
  Network-based analysis of DeFi systemic fragility via TVL dynamics
  and correlation structures.
* Zhu (2024)

  Brian Zhu.
  Stablecoin runs and disclosure policy in the presence of large sales.
  *SSRN Electronic Journal*, 2024.
  doi: 10.2139/ssrn.4818982.
  Global game model showing private signal precision can paradoxically
  increase run probability when fundamentals are strong, potentially explaining
  stability of opaque stablecoins.

## Appendix A Detailed Component Specifications

This appendix provides exact formulas for all ASRI sub-components as implemented in the reference codebase. Where practical data constraints necessitate proxy measures, we document both the theoretical specification and the implemented approximation, with justification for why the proxy preserves the intended risk signal.

### A.1 Stablecoin Concentration Risk (SCR)

Weight: 30%

The Stablecoin Concentration Risk sub-index captures vulnerabilities arising from reserve composition, peg stability, and issuer concentration.

#### A.1.1  TVL Ratio (TVLt\text{TVL}\_{t})

Data Source: DeFi Llama API (api.llama.fi/v2/historicalChainTvl), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | TVLraw=Current Stablecoin TVLtmaxτ≤t⁡(Stablecoin TVLτ)\text{TVL}\_{\text{raw}}=\frac{\text{Current Stablecoin TVL}\_{t}}{\max\_{\tau\leq t}(\text{Stablecoin TVL}\_{\tau})} |  | (22) |

The raw ratio is inverted and normalized to produce a risk score:

|  |  |  |  |
| --- | --- | --- | --- |
|  | TVLt=normalize​(1−TVLraw,0,0.5)×100\text{TVL}\_{t}=\text{normalize}(1-\text{TVL}\_{\text{raw}},0,0.5)\times 100 |  | (23) |

Interpretation: At maximum historical TVL, the component equals 0 (low risk). At 50% of historical maximum, the component approaches 100 (high risk). This captures the intuition that significant TVL drawdowns indicate stress or capital flight.

Normalization: Clipped to [0,100][0,100] via min-max scaling with theoretical bounds.

#### A.1.2  Treasury Stress (Treasuryt\text{Treasury}\_{t})

Data Source: FRED API (DGS10 series), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Treasuryt=r10​Y,t−rminrmax−rmin×100\text{Treasury}\_{t}=\frac{r\_{10Y,t}-r\_{\min}}{r\_{\max}-r\_{\min}}\times 100 |  | (24) |

where r10​Y,tr\_{10Y,t} is the 10-Year Treasury Constant Maturity Rate, rmin=2.0%r\_{\min}=2.0\%, and rmax=6.0%r\_{\max}=6.0\%.

Interpretation: Higher Treasury yields increase stress on stablecoin reserves (which typically hold short-term Treasuries) through mark-to-market losses and opportunity cost dynamics. The 2–6% bounds reflect the observed range during the sample period.

Implementation Note: The paper’s theoretical specification describes Treasuryt\text{Treasury}\_{t} as the ratio of T-Bill reserves to total reserves. The implementation uses Treasury yield levels as a proxy because reserve composition data is available only through monthly attestation reports with significant reporting lags. Treasury yields provide a higher-frequency signal of the same underlying risk: reserve stress from interest rate movements.

#### A.1.3  Concentration HHI (HHIt\text{HHI}\_{t})

Data Source: DeFi Llama Stablecoins API (stablecoins.llama.fi/stablecoins), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | HHIraw=∑i=1n(Si∑j=1nSj)2×10000\text{HHI}\_{\text{raw}}=\sum\_{i=1}^{n}\left(\frac{S\_{i}}{\sum\_{j=1}^{n}S\_{j}}\right)^{2}\times 10000 |  | (25) |

where SiS\_{i} is the circulating supply of stablecoin ii.

The raw HHI is converted to a risk score using a piecewise mapping:

|  |  |  |  |
| --- | --- | --- | --- |
|  | HHIt={HHIraw1500×30if HHI<150030+HHIraw−15001000×30if ​1500≤HHI<250060+HHIraw−25002500×30if ​2500≤HHI<500090+HHIraw−50005000×10if HHI≥5000\text{HHI}\_{t}=\begin{cases}\frac{\text{HHI}\_{\text{raw}}}{1500}\times 30&\text{if HHI}<1500\\[5.0pt] 30+\frac{\text{HHI}\_{\text{raw}}-1500}{1000}\times 30&\text{if }1500\leq\text{HHI}<2500\\[5.0pt] 60+\frac{\text{HHI}\_{\text{raw}}-2500}{2500}\times 30&\text{if }2500\leq\text{HHI}<5000\\[5.0pt] 90+\frac{\text{HHI}\_{\text{raw}}-5000}{5000}\times 10&\text{if HHI}\geq 5000\end{cases} |  | (26) |

Interpretation: The thresholds follow standard antitrust guidelines: HHI << 1500 indicates a competitive market; 1500–2500 indicates moderate concentration; >> 2500 indicates high concentration. The piecewise function maps these to risk scores of 0–30, 30–60, and 60–100 respectively.

#### A.1.4  Peg Volatility (Volt\text{Vol}\_{t})

Data Source: DeFi Llama Stablecoins API (price field), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Volt=∑i=1n|pi−1|⋅Si∑j=1nSj×20\text{Vol}\_{t}=\frac{\sum\_{i=1}^{n}|p\_{i}-1|\cdot S\_{i}}{\sum\_{j=1}^{n}S\_{j}}\times 20 |  | (27) |

where pip\_{i} is the current price of stablecoin ii and SiS\_{i} is its circulating supply.

Normalization: 0% weighted deviation maps to 0 risk; 5% weighted deviation maps to 100 risk.

Missing Data: If no price data is available, the component defaults to 50.0 (neutral).

#### A.1.5  SCR Aggregation

|  |  |  |  |
| --- | --- | --- | --- |
|  | SCRt=0.4⋅TVLt+0.3⋅Treasuryt+0.2⋅HHIt+0.1⋅Volt\text{SCR}\_{t}=0.4\cdot\text{TVL}\_{t}+0.3\cdot\text{Treasury}\_{t}+0.2\cdot\text{HHI}\_{t}+0.1\cdot\text{Vol}\_{t} |  | (28) |

#### A.1.6  Algorithmic Stablecoin Risk Extension (v2.1)

The baseline SCR formula treats all stablecoins identically via peg volatility (Volt\text{Vol}\_{t}). However, the Terra/Luna collapse (May 2022) revealed that peg volatility is a lagging indicator for algorithmic stablecoins: UST maintained its peg until the death spiral commenced, and Luna’s price appreciation masked underlying fragility. This extension addresses the detection gap by incorporating risk factors specific to algorithmic and crypto-backed stablecoins.

##### Motivation.

Fiat-collateralized stablecoins (USDT, USDC) are backed by liquid reserves redeemable at par. Algorithmic stablecoins maintain peg through arbitrage mechanisms between the stablecoin and a backing token—creating reflexive dynamics where redemption pressure inflates backing token supply, diluting its value, which further increases redemption pressure. This death spiral mechanism is distinct from the reserve-based risks captured by baseline SCR components.

##### Algorithmic Stablecoin Risk Formula.

For stablecoins classified as algorithmic or crypto-backed, we compute:

|  |  |  |  |
| --- | --- | --- | --- |
|  | AlgoRiskt=0.35⋅BackingRatiot+0.30⋅CollateralVolt+0.20⋅Dilutiont+0.15⋅AlgoConct\text{AlgoRisk}\_{t}=0.35\cdot\text{BackingRatio}\_{t}+0.30\cdot\text{CollateralVol}\_{t}+0.20\cdot\text{Dilution}\_{t}+0.15\cdot\text{AlgoConc}\_{t} |  | (29) |

Component definitions:

* •

  BackingRatiot: Risk from undercollateralization. Backing ratio ≥1.5\geq 1.5 maps to low risk (0–20); ratio <0.8<0.8 maps to critical risk (80–100). For stablecoins without explicit backing disclosure, defaults to moderate risk (50).
* •

  CollateralVolt: Annualized 30-day volatility of backing token. ETH volatility (∼\sim60–80%) maps to moderate risk; Luna-type volatility (>>100%) maps to elevated/critical risk.
* •

  Dilutiont: 30-day supply growth rate of backing token. Monthly growth >50%>50\% signals crisis-level dilution (Luna supply grew ∼\sim50,000% during collapse).
* •

  AlgoConct: Share of total stablecoin supply in algorithmic/crypto-backed stablecoins. At peak, UST represented ∼\sim10% of total stablecoin supply.

##### Integration with SCR.

Let αt\alpha\_{t} denote the market share of algorithmic stablecoins in total stablecoin supply. The adjusted SCR blends baseline and algorithmic risk:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SCRtadj=(1−αt)⋅SCRtbase+αt⋅[0.6⋅SCRtbase+0.4⋅AlgoRiskt]\text{SCR}\_{t}^{\text{adj}}=(1-\alpha\_{t})\cdot\text{SCR}\_{t}^{\text{base}}+\alpha\_{t}\cdot\left[0.6\cdot\text{SCR}\_{t}^{\text{base}}+0.4\cdot\text{AlgoRisk}\_{t}\right] |  | (30) |

When αt<1%\alpha\_{t}<1\%, the adjustment is negligible. When αt=10%\alpha\_{t}=10\% (approximate UST peak share), algorithmic-specific risk contributes 4% to SCR weighting.

##### Data Requirements.

Full implementation requires:

1. 1.

   Stablecoin classification: DeFi Llama pegType/pegMechanism fields or manual classification (provided in codebase).
2. 2.

   Backing token identification: Mapping from stablecoin to backing token (e.g., UST →\to LUNA).
3. 3.

   Backing token metrics: Price volatility and supply data from CoinGecko or on-chain indexers.

##### Backtest Limitation.

Historical reconstruction of AlgoRiskt for pre-collapse Terra/Luna requires archived Luna price and supply data. While DeFi Llama and CoinGecko retain historical snapshots, consistent backing ratio data for UST is not systematically available. The specification documents the framework for future algorithmic stablecoin risk monitoring; full historical backtest validation awaits improved data infrastructure. Sensitivity analysis suggests that with accurate Luna volatility data (annualized vol >>120% in April 2022), the extension would have elevated SCR by approximately 8–12 points prior to UST’s depeg—potentially bringing ASRI above the detection threshold.

### A.2 DeFi Liquidity Risk (DLR)

Weight: 25%

The DeFi Liquidity Risk sub-index captures protocol concentration, volatility dynamics, and smart contract vulnerability.

#### A.2.1  Protocol Concentration (Conct\text{Conc}\_{t})

Data Source: DeFi Llama Protocols API (api.llama.fi/protocols), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Conct=fHHI​(∑i=110(TVLi∑j=110TVLj)2×10000)\text{Conc}\_{t}=f\_{\text{HHI}}\left(\sum\_{i=1}^{10}\left(\frac{\text{TVL}\_{i}}{\sum\_{j=1}^{10}\text{TVL}\_{j}}\right)^{2}\times 10000\right) |  | (31) |

where fHHIf\_{\text{HHI}} is the piecewise HHI-to-risk mapping defined above, and the summation is over the top 10 protocols by TVL.

Interpretation: Concentration among the largest protocols indicates ecosystem fragility—failure of a dominant protocol would have outsized systemic effects.

#### A.2.2  TVL Volatility (TVLVolt\text{TVLVol}\_{t})

Data Source: DeFi Llama TVL history, 30-day rolling window.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | TVLVolt=normalize​(σ30​(TVL)μ30​(TVL),0,0.20)×100\text{TVLVol}\_{t}=\text{normalize}\left(\frac{\sigma\_{30}(\text{TVL})}{\mu\_{30}(\text{TVL})},0,0.20\right)\times 100 |  | (32) |

where σ30\sigma\_{30} and μ30\mu\_{30} denote the 30-day rolling standard deviation and mean.

Normalization: 0% coefficient of variation maps to 0 risk; 20% maps to 100 risk.

Missing Data: If historical TVL data is unavailable (fewer than 2 observations), the component defaults to 30.0 (moderate).

#### A.2.3  Smart Contract Risk (SCt\text{SC}\_{t})

Data Source: DeFi Llama Protocols API (audits field), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SCt=(1−|{p:audits​(p)>0}||{p:TVL​(p)>0}|)×100\text{SC}\_{t}=\left(1-\frac{|\{p:\text{audits}(p)>0\}|}{|\{p:\text{TVL}(p)>0\}|}\right)\times 100 |  | (33) |

Interpretation: The component measures the inverse of audit coverage across protocols with non-zero TVL. Protocols lacking audits receive the full risk weight.

Theoretical vs. Implemented Specification: The paper describes a 3-factor composite incorporating audit status, deployment age, and exploit history. The current implementation uses audit coverage only. Deployment age and exploit history integration are deferred to future versions pending reliable, systematized data feeds. The DeFi Llama API provides audit counts but not deployment timestamps or comprehensive exploit databases.

Justification: Audit coverage remains the most reliable and consistently available indicator of smart contract risk. Empirical research demonstrates strong correlation between unaudited protocols and exploit frequency, supporting the proxy’s validity.

#### A.2.4  Flash Loan Proxy (Flasht\text{Flash}\_{t})

Data Source: DeFi Llama Protocols API (change\_1d field), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Flasht=normalize​(1n​∑i=1n|Δ1d,i|,0,20)×100\text{Flash}\_{t}=\text{normalize}\left(\frac{1}{n}\sum\_{i=1}^{n}|\Delta\_{\text{1d},i}|,0,20\right)\times 100 |  | (34) |

where Δ1d,i\Delta\_{\text{1d},i} is the 1-day TVL change percentage for protocol ii.

Theoretical vs. Implemented Specification: The paper describes flash loan volume spikes relative to a 90-day average. Direct flash loan volume data requires protocol-specific analytics (e.g., Aave, dYdX subgraphs) with heterogeneous reporting standards. The implementation uses aggregate TVL volatility as a proxy, on the reasoning that flash loan activity manifests as rapid TVL movements during MEV extraction and liquidation cascades.

Normalization: 0% average daily change maps to 0 risk; 20% maps to 100 risk.

#### A.2.5  Leverage Change (Levt\text{Lev}\_{t})

Data Source: DeFi Llama Protocols API (category field), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Levt=normalize​(∑p∈LendingTVLp∑pTVLp×100,0,30)×100\text{Lev}\_{t}=\text{normalize}\left(\frac{\sum\_{p\in\text{Lending}}\text{TVL}\_{p}}{\sum\_{p}\text{TVL}\_{p}}\times 100,0,30\right)\times 100 |  | (35) |

Interpretation: A higher share of TVL in lending protocols indicates greater system-wide leverage. The 30% threshold reflects the upper bound of lending protocol dominance observed during market stress.

Theoretical vs. Implemented Specification: The paper describes 30-day change in aggregate leverage ratios. The implementation uses the current lending TVL share as a level indicator rather than a change measure, because reliable historical leverage data across protocols is not consistently available.

#### A.2.6  DLR Aggregation

|  |  |  |  |
| --- | --- | --- | --- |
|  | DLRt=0.35⋅Conct+0.25⋅TVLVolt+0.20⋅SCt+0.10⋅Flasht+0.10⋅Levt\text{DLR}\_{t}=0.35\cdot\text{Conc}\_{t}+0.25\cdot\text{TVLVol}\_{t}+0.20\cdot\text{SC}\_{t}+0.10\cdot\text{Flash}\_{t}+0.10\cdot\text{Lev}\_{t} |  | (36) |

### A.3 Contagion Risk (CR)

Weight: 25%

The Contagion Risk sub-index quantifies DeFi-TradFi interconnection and cross-market transmission channels.

#### A.3.1  RWA Growth (RWAt\text{RWA}\_{t})

Data Source: DeFi Llama Protocols API (category = ’RWA’), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RWAt=normalize​(∑p∈RWATVLp∑pTVLp×100,0,10)×100\text{RWA}\_{t}=\text{normalize}\left(\frac{\sum\_{p\in\text{RWA}}\text{TVL}\_{p}}{\sum\_{p}\text{TVL}\_{p}}\times 100,0,10\right)\times 100 |  | (37) |

Interpretation: Higher RWA share indicates greater integration between DeFi and traditional finance through tokenized real-world assets. The 10% threshold reflects the upper bound of RWA penetration observed during the sample period.

Theoretical vs. Implemented Specification: The paper describes 30-day RWA TVL growth rate. The implementation uses the current RWA share as a level indicator, because RWA protocols have short histories making growth rate calculations unreliable for early-period observations.

#### A.3.2  Bank Exposure (Bankt\text{Bank}\_{t})

Data Sources: FRED API (DGS10 for Treasury rates, VIXCLS for VIX), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bankt=0.6⋅normalize​(r10​Y,t,2,6)+0.4⋅normalize​(VIXt,12,40)\text{Bank}\_{t}=0.6\cdot\text{normalize}(r\_{10Y,t},2,6)+0.4\cdot\text{normalize}(\text{VIX}\_{t},12,40) |  | (38) |

Interpretation: The composite captures TradFi stress through two channels: Treasury rate levels (affecting stablecoin reserves and bank balance sheets) and equity market volatility (signaling broader risk-off sentiment).

Weight and Range Justification: The 60/40 weighting reflects Treasury yields’ direct balance-sheet impact on bank capital ratios versus VIX’s indirect sentiment signal. Banks holding Treasury securities face mark-to-market losses when yields rise (the primary channel), while VIX captures risk-off dynamics that tighten credit conditions (secondary channel). The normalization ranges (2–6% for 10Y Treasury, 12–40 for VIX) span the 5th–95th percentiles of 2015–2024 sample data, ensuring meaningful variation without clipping at extremes.

Theoretical vs. Implemented Specification: The paper describes a normalized score from OCC/ECB regulatory filings on bank crypto exposure. Regulatory filings are quarterly with 45–90 day publication lags, making them unsuitable for daily risk monitoring. The Treasury-VIX composite provides a higher-frequency proxy: banks with crypto exposure face stress when Treasury yields rise (mark-to-market losses) and when VIX spikes (risk management constraints).

#### A.3.3  TradFi Linkage (Linkt\text{Link}\_{t})

Data Source: FRED API (T10Y2Y series), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Linkt={normalize​(|st|,0,2)×100+50if ​st<0max⁡(0,50−normalize​(st,0,2)×50)if ​st≥0\text{Link}\_{t}=\begin{cases}\text{normalize}(|s\_{t}|,0,2)\times 100+50&\text{if }s\_{t}<0\\[5.0pt] \max(0,50-\text{normalize}(s\_{t},0,2)\times 50)&\text{if }s\_{t}\geq 0\end{cases} |  | (39) |

where st=r10​Y,t−r2​Y,ts\_{t}=r\_{10Y,t}-r\_{2Y,t} is the 10-Year minus 2-Year Treasury spread.

Interpretation: Yield curve inversion (negative spread) indicates banking sector stress and recession expectations, which propagate to crypto through reduced institutional risk appetite and potential bank failures affecting crypto-exposed entities.

Theoretical vs. Implemented Specification: The paper describes “stablecoin flows to TradFi-connected entities.” Such flow data requires enterprise-grade on-chain analytics (Chainalysis, TRM Labs) at prohibitive cost for academic research. Yield curve dynamics provide a validated proxy: the March 2023 SVB crisis demonstrated that yield curve inversion directly precedes banking stress events that propagate to crypto markets through stablecoin reserve exposure.

Justification: The yield curve spread has predicted every U.S. recession since 1970 with a median lead time of 12 months. Banking crises correlated with yield curve inversion directly affect crypto-TradFi linkages through stablecoin reserve exposure (as demonstrated by the USDC depeg during SVB’s collapse).

#### A.3.4  Correlation (Corrt\text{Corr}\_{t})

Data Source: External calculation (BTC-SPY 30-day rolling correlation).

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Corrt=|rBTC-SPY,30​d|×100\text{Corr}\_{t}=|r\_{\text{BTC-SPY},30d}|\times 100 |  | (40) |

Interpretation: Higher absolute correlation indicates greater co-movement between crypto and equities, implying tighter contagion channels.

Implementation Note: The current implementation accepts correlation as an external input with a default of 0.5 (moderate). Real-time calculation requires equity price feeds (Yahoo Finance, Bloomberg) not included in the core data pipeline.

#### A.3.5  Bridge Risk (Bridget\text{Bridge}\_{t})

Data Source: DeFi Llama Bridges API (bridges.llama.fi/bridges), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bridget=normalize​(nbridges,0,150)×100\text{Bridge}\_{t}=\text{normalize}(n\_{\text{bridges}},0,150)\times 100 |  | (41) |

where nbridgesn\_{\text{bridges}} is the count of active cross-chain bridges.

Interpretation: More bridges indicate larger attack surface and greater cross-chain contagion potential.

Theoretical vs. Implemented Specification: The paper describes a composite of bridge volume and exploit frequency. Exploit frequency data requires manual tracking (DeFi Rekt database) with inconsistent categorization. Bridge count provides a structural proxy: empirical research finds exploit frequency scales with the number of bridge implementations due to varying security standards and code quality.

#### A.3.6  CR Aggregation

|  |  |  |  |
| --- | --- | --- | --- |
|  | CRt=0.30⋅RWAt+0.25⋅Bankt+0.20⋅Linkt+0.15⋅Corrt+0.10⋅Bridget\text{CR}\_{t}=0.30\cdot\text{RWA}\_{t}+0.25\cdot\text{Bank}\_{t}+0.20\cdot\text{Link}\_{t}+0.15\cdot\text{Corr}\_{t}+0.10\cdot\text{Bridge}\_{t} |  | (42) |

### A.4 Regulatory Opacity Risk (OR)

Weight: 20%

The Regulatory Opacity Risk sub-index assesses transparency deficits and regulatory arbitrage exposure.

#### A.4.1  Unregulated Exposure (Unregt\text{Unreg}\_{t})

Data Source: Placeholder component (see Table [37](https://arxiv.org/html/2602.03874v1#A1.T37 "Table 37 ‣ A.6.3 Proxy Acknowledgments ‣ A.6 Data Quality and Limitations ‣ Appendix A Detailed Component Specifications") for implementation status).

Implementation: Fixed at 35.0 (moderate risk), corresponding to estimated market share of volume on platforms without clear regulatory oversight.

Theoretical Specification: Ratio of volume on unregulated platforms to regulated platforms. Full implementation requires mapping protocols to jurisdictional regulatory status, which involves manual classification and ongoing tracking of regulatory developments across 50+ jurisdictions.

Future Enhancement: Chain-level classification (e.g., Ethereum as “regulated-adjacent” due to U.S. regulatory engagement vs. privacy chains) would enable dynamic calculation.

#### A.4.2  Multi-Issuer Risk (Multit\text{Multi}\_{t})

Data Source: DeFi Llama Stablecoins API, daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Multit={70if ​nsig<330if ​3≤nsig<1050+2​(nsig−10)if ​nsig≥10\text{Multi}\_{t}=\begin{cases}70&\text{if }n\_{\text{sig}}<3\\[5.0pt] 30&\text{if }3\leq n\_{\text{sig}}<10\\[5.0pt] 50+2(n\_{\text{sig}}-10)&\text{if }n\_{\text{sig}}\geq 10\end{cases} |  | (43) |

where nsig=|{s:circulating​(s)>$​1​B}|n\_{\text{sig}}=|\{s:\text{circulating}(s)>\mathdollar 1\text{B}\}| is the count of stablecoins with circulating supply exceeding $1 billion.

Interpretation: The “sweet spot” is 3–5 significant issuers providing diversification without fragmentation. Fewer than 3 indicates dangerous concentration; more than 10 indicates coordination challenges and potential regulatory complexity.

#### A.4.3  Custody Concentration (Custt\text{Cust}\_{t})

Data Source: DeFi Llama Stablecoins API, daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Custt=normalize​(∑i=12Si∑jSj×100,50,100)×100\text{Cust}\_{t}=\text{normalize}\left(\frac{\sum\_{i=1}^{2}S\_{i}}{\sum\_{j}S\_{j}}\times 100,50,100\right)\times 100 |  | (44) |

where SiS\_{i} is the circulating supply of the ii-th largest stablecoin.

Interpretation: Top-2 stablecoin market share as a proxy for custody concentration. Higher concentration implies greater single-point-of-failure risk regardless of custody jurisdiction.

Theoretical vs. Implemented Specification: The paper describes “custody concentration in non-audited jurisdictions.” Jurisdiction-level custody data is not systematically available; stablecoins do not consistently disclose custodian locations or regulatory status. Market concentration serves as a conservative proxy: high concentration implies custody risk regardless of location, as a single custodian failure would have systemic effects.

#### A.4.4  Regulatory Sentiment (Sentt\text{Sent}\_{t})

Data Source: Manual input parameter.

Implementation: Accepts external input with default of 50.0 (neutral). This component contributes only 15% of the Opacity sub-index weight (3% of total ASRI), limiting its impact on overall index behavior.

Theoretical Specification: NLP-derived sentiment score from SEC, ESRB, and FSB announcements. Full implementation would require:

* •

  Sources: GDELT Global Knowledge Graph filtered for regulatory entities (SEC, CFTC, ESRB, FSB, BIS), SEC EDGAR filings, Federal Register cryptocurrency mentions
* •

  Model: FinBERT or domain-adapted transformer for financial regulatory text classification
* •

  Lexicon: Crypto-specific regulatory vocabulary (“enforcement action,” “no-action letter,” “framework,” “guidance”) with sentiment polarity labels
* •

  De-duplication: Entity resolution across news sources to avoid double-counting of same regulatory announcement
* •

  Jurisdictional weighting: US (40%), EU (30%), UK (15%), Other (15%) reflecting market share

This infrastructure is deferred to future versions; current results are robust to Sentt variation due to its low aggregate weight.

Sensitivity Analysis: Varying Sentt from 0 (maximally positive regulatory environment) to 100 (maximally negative) while holding all other components constant produces the following ASRI impact:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​ASRI=0.20×0.15×Δ​Sentt=0.03×Δ​Sentt\Delta\text{ASRI}=0.20\times 0.15\times\Delta\text{Sent}\_{t}=0.03\times\Delta\text{Sent}\_{t} |  | (45) |

A full-range swing (Sentt: 0 →\to 100) changes aggregate ASRI by ±\pm1.5 points. For typical variation (±\pm25 points around neutral), ASRI changes by ±\pm0.75 points—well within the noise band of other component fluctuations.

Detection Impact: All four crisis events would still be detected under any Sentt value in [0,100][0,100], as the shifted thresholds remain within the detection window. The Terra/Luna event (peak 48.7 at baseline) would require Sent>t93{}\_{t}>93 to breach the 50 threshold—an implausibly extreme regulatory stance.

Future Implementation Roadmap:

1. 1.

   Phase 1: GDELT integration with keyword filters (“SEC,” “CFTC,” “cryptocurrency,” “enforcement”)
2. 2.

   Phase 2: FinBERT deployment on SEC EDGAR cryptocurrency-related filings
3. 3.

   Phase 3: Multi-jurisdictional aggregation with decay weighting for announcement recency

#### A.4.5  Transparency Score (Transt\text{Trans}\_{t})

Data Source: DeFi Llama Protocols API (audits field), daily frequency.

Formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Transt=|{p:audits​(p)>0}||{p:TVL​(p)>0}|×100\text{Trans}\_{t}=\frac{|\{p:\text{audits}(p)>0\}|}{|\{p:\text{TVL}(p)>0\}|}\times 100 |  | (46) |

Interpretation: Audit coverage as a proxy for protocol transparency. The component is not inverted at the component level; inversion occurs in the aggregation formula.

#### A.4.6  OR Aggregation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ORt=0.25⋅Unregt+0.25⋅Multit+0.20⋅Custt+0.15⋅Sentt+0.15⋅(100−Transt)\text{OR}\_{t}=0.25\cdot\text{Unreg}\_{t}+0.25\cdot\text{Multi}\_{t}+0.20\cdot\text{Cust}\_{t}+0.15\cdot\text{Sent}\_{t}+0.15\cdot(100-\text{Trans}\_{t}) |  | (47) |

Note the inversion of Transt\text{Trans}\_{t}: low transparency implies high opacity risk.

### A.5 Aggregate ASRI Calculation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASRIt=0.30⋅SCRt+0.25⋅DLRt+0.25⋅CRt+0.20⋅ORt\text{ASRI}\_{t}=0.30\cdot\text{SCR}\_{t}+0.25\cdot\text{DLR}\_{t}+0.25\cdot\text{CR}\_{t}+0.20\cdot\text{OR}\_{t} |  | (48) |

All sub-indices are bounded to [0,100][0,100] by construction, ensuring ASRIt∈[0,100]\text{ASRI}\_{t}\in[0,100] without post-hoc normalization.

### A.6 Data Quality and Limitations

#### A.6.1  Data Availability Tiers

* •

  Tier 1 (Daily, Automated): DeFi Llama TVL, stablecoins, protocols, bridges; FRED Treasury rates and VIX.
* •

  Tier 2 (Limited/Manual): Regulatory sentiment, unregulated exposure classification, exploit frequency tracking.

#### A.6.2  Missing Data Protocol

* •

  Gaps << 3 days: Linear interpolation.
* •

  Gaps 3–7 days: Forward-fill with reduced confidence.
* •

  Gaps >> 7 days: Exclude from calculation; flag as unreliable.

#### A.6.3  Proxy Acknowledgments

Table [37](https://arxiv.org/html/2602.03874v1#A1.T37 "Table 37 ‣ A.6.3 Proxy Acknowledgments ‣ A.6 Data Quality and Limitations ‣ Appendix A Detailed Component Specifications") summarizes components where implementation deviates from theoretical specification.

Table 37: Proxy Implementations: Theoretical vs. Actual

| Component | Theoretical Specification | Implementation | Validity |
| --- | --- | --- | --- |
| Treasuryt\text{Treasury}\_{t} | T-Bill reserves / total reserves | 10Y Treasury yield level | High |
| SCt\text{SC}\_{t} | Audit + age + exploits composite | Audit coverage only | Medium |
| Flasht\text{Flash}\_{t} | Flash loan volume spikes | TVL daily change volatility | Medium |
| Levt\text{Lev}\_{t} | 30-day leverage ratio change | Lending TVL share (level) | Medium |
| RWAt\text{RWA}\_{t} | 30-day RWA growth rate | RWA TVL share (level) | High |
| Bankt\text{Bank}\_{t} | OCC/ECB bank exposure filings | Treasury + VIX composite | High |
| Linkt\text{Link}\_{t} | Stablecoin flows to TradFi | Yield curve spread | High |
| Bridget\text{Bridge}\_{t} | Volume + exploit frequency | Bridge count | Medium |
| Custt\text{Cust}\_{t} | Non-audited jurisdiction custody | Top-2 stablecoin concentration | Medium |
| Unregt\text{Unreg}\_{t} | Unregulated platform ratio | Fixed (35.0)†\dagger | Low |
| Sentt\text{Sent}\_{t} | NLP regulatory sentiment | Manual input (50.0)†\dagger | Low |

* †\dagger

  Placeholder components awaiting enterprise data infrastructure. Sensitivity analysis (Section [5.9](https://arxiv.org/html/2602.03874v1#S5.SS9 "5.9 Sensitivity Analysis ‣ 5 Empirical Validation")) confirms all four crisis detections remain robust under full-range variation of these parameters.

Validity Legend:

* •

  High: Proxy captures same underlying risk channel with strong theoretical justification and empirical support.
* •

  Medium: Proxy captures related risk dynamics but with potential measurement error; interpretation requires caution.
* •

  Low: Placeholder awaiting data infrastructure development; current values are informative but not definitive.

#### A.6.4  Future Data Integration

Version 3.0 development priorities include:

1. 1.

   Integration of exploit database (DeFi Rekt, Immunefi) for dynamic SCt\text{SC}\_{t} and Bridget\text{Bridge}\_{t} components.
2. 2.

   Protocol deployment timestamp extraction from blockchain explorers for age-based risk weighting.
3. 3.

   GDELT/SEC filing NLP pipeline for automated regulatory sentiment scoring.
4. 4.

   Chain-level regulatory classification for dynamic Unregt\text{Unreg}\_{t} calculation.
5. 5.

   Enterprise analytics partnership (Chainalysis/TRM) for stablecoin flow analysis.

## Appendix B API Documentation Summary

Table [38](https://arxiv.org/html/2602.03874v1#A2.T38 "Table 38 ‣ Appendix B API Documentation Summary") provides endpoint documentation for primary data sources.

Table 38: Primary API Endpoints

| Source | Endpoint | Rate Limit | Authentication |
| --- | --- | --- | --- |
| DeFi Llama | api.llama.fi/v2/tvl | 300/5min | None |
| DeFi Llama | stablecoins.llama.fi/stablecoins | 300/5min | None |
| FRED | api.stlouisfed.org/fred/series | None | API Key |
| CoinGecko | api.coingecko.com/api/v3 | 10-50/min | API Key (Pro) |
| Token Terminal | api.tokenterminal.com/v2 | Varies | API Key |

## Appendix C Sub-Index Calculation Code

Python implementation of sub-index formulas is available in the repository at src/asri/signals/calculator.py. Key functions:

```
def calculate_stablecoin_risk(
    tvl_ratio: float,
    treasury_weight: float,
    hhi_concentration: float,
    peg_volatility: float
) -> float:
    return (
        0.4 * tvl_ratio +
        0.3 * treasury_weight +
        0.2 * hhi_concentration +
        0.1 * peg_volatility
    )
```

Full implementation: [github.com/studiofarzulla/asri](https://github.com/studiofarzulla/asri)

## Appendix D Historical Crisis Event Details

Terra/Luna Collapse (May 2022): UST algorithmic stablecoin depegged due to redemption spirals, eliminating $40B in value within 72 hours. LUNA dropped from $80 to near-zero.

Celsius/3AC Contagion (June 2022): Celsius Network froze withdrawals; Three Arrows Capital defaulted on loans. Combined losses exceeded $10B, triggering margin calls across crypto lending platforms.

FTX Bankruptcy (November 2022): FTX and Alameda Research filed for bankruptcy after liquidity crisis. Opaque counterparty relationships propagated losses across the ecosystem.

## Appendix E Sample Market Assessment (December 2024)

Note: This appendix provides a sample ASRI reading for illustrative purposes. For current market conditions, visit [asri.dissensus.ai](https://asri.dissensus.ai).

### Sample ASRI Reading

As of December 31, 2024, the ASRI stands at 38.2 (Moderate risk), reflecting:

* •

  Stablecoin Risk: 45.1 (moderate concentration, stable pegs)
* •

  DeFi Liquidity: 42.8 (recovering from 2022-23 deleveraging)
* •

  Contagion Risk: 28.5 (reduced TradFi linkage post-SVB)
* •

  Arbitrage Opacity: 31.4 (improving regulatory clarity)

### Risk Decomposition

Current primary risk contributors:

1. 1.

   Stablecoin concentration in USDT/USDC (HHI = 0.52)
2. 2.

   Treasury exposure through stablecoin reserves ($80B+ in T-bills)
3. 3.

   Emerging RWA tokenization growth (+45% YoY)

### Regime Classification

The HMM classifies current market conditions as Regime 2 (Moderate) with 78% probability. Transition probabilities indicate:

* •

  3.9% probability of moving to Elevated regime
* •

  2.3% probability of moving to Low Risk regime
* •

  93.8% probability of remaining in Moderate regime

### Alert Status

No immediate systemic stress signals detected. Key monitoring priorities:

1. 1.

   Stablecoin reserve composition changes
2. 2.

   Cross-market correlation shifts (BTC-equity)
3. 3.

   Bridge vulnerability and exploit frequency

## Appendix F Event Study Protocol Specification

This appendix provides the complete methodological specification for the event study analysis presented in Section [5.4](https://arxiv.org/html/2602.03874v1#S5.SS4 "5.4 Event Study Analysis ‣ 5 Empirical Validation"), addressing reviewer concerns regarding pre-registration, window selection, multiple testing correction, and placebo testing.

### F.1 Pre-Registration and Event Selection

#### F.1.1  Event Identification Criteria

Crisis events were identified ex ante based on three jointly necessary conditions (Definition [5.1](https://arxiv.org/html/2602.03874v1#S5.Thmdefinition1 "Definition 5.1 (Systemic Stress Event). ‣ 5.1.1 Operational Crisis Definition ‣ 5.1 Crisis Taxonomy and Operational Definitions ‣ 5 Empirical Validation")):

1. 1.

   Magnitude: Market capitalization decline ≥15%\geq 15\% within 7 days, or single-asset collapse ≥50%\geq 50\% for assets with market cap ≥$​10\geq\mathdollar 10B
2. 2.

   Contagion: Cross-asset correlation surge ρ¯t−ρ¯t−30≥0.20\bar{\rho}\_{t}-\bar{\rho}\_{t-30}\geq 0.20
3. 3.

   Duration: Elevated stress persisting ≥5\geq 5 trading days

Event dates were sourced from external references (CoinDesk, Bloomberg, Reuters) prior to ASRI analysis, preventing data snooping on threshold selection.

#### F.1.2  Pre-Specified Parameters

The following parameters were fixed before analysis:

* •

  Estimation window: Test=60T\_{\text{est}}=60 days (t=−90t=-90 to t=−31t=-31 relative to event)
* •

  Event window: Tevent=41T\_{\text{event}}=41 days (t=−30t=-30 to t=+10t=+10)
* •

  Significance level: α=0.05\alpha=0.05 (two-tailed)
* •

  Lead time detection: 1.5 standard deviations above estimation-window mean

### F.2 Window Selection Justification

#### F.2.1  Estimation Window: [−90,−31][-90,-31]

The 60-day estimation window was selected based on:

1. 1.

   Statistical power: n=60n=60 provides adequate precision for mean and variance estimation while avoiding excessive smoothing of regime-dependent dynamics
2. 2.

   Regime stability: ASRI exhibits regime persistence >94%>94\% (Table [17](https://arxiv.org/html/2602.03874v1#S5.T17 "Table 17 ‣ Regime Count versus Operational Alert Levels. ‣ 5.6 Regime Detection ‣ 5 Empirical Validation")), making 60 days sufficient to capture baseline behavior within a regime
3. 3.

   Contamination avoidance: The 30-day buffer (t=−31t=-31 cutoff) ensures estimation is complete before pre-crisis stress begins

Robustness: Alternative estimation windows (45 days, 90 days) produce qualitatively identical results (all events significant at p<0.01p<0.01).

#### F.2.2  Event Window: [−30,+10][-30,+10]

The asymmetric event window reflects ASRI’s design as an early warning system:

* •

  Pre-event (−30-30 to −1-1): Captures lead time—the period where ASRI begins detecting stress buildup
* •

  Event day (t=0t=0): Crisis onset (price cascade initiation)
* •

  Post-event (+1+1 to +10+10): Captures immediate aftermath and stress persistence

The 30-day pre-event window is calibrated to expected ASRI lead times (Table [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") shows 29–30 days across events).

### F.3 Normal Model Specification

The constant mean model was selected for expected ASRI:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ASRIt]=μ^=1Test​∑τ=−90−31ASRIτ\mathbb{E}[\text{ASRI}\_{t}]=\hat{\mu}=\frac{1}{T\_{\text{est}}}\sum\_{\tau=-90}^{-31}\text{ASRI}\_{\tau} |  | (49) |

#### F.3.1  Model Selection Rationale

1. 1.

   Simplicity: The constant mean model makes minimal parametric assumptions
2. 2.

   Stationarity: ASRI rejects unit root (ADF p<0.01p<0.01), validating level-based analysis
3. 3.

   AR(1) Alternative: Robustness testing with AR(1) dynamics produces equivalent significance conclusions (all p<0.01p<0.01) with slightly smaller CAS magnitudes

#### F.3.2  Variance Estimation

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^AS2=1Test−1​∑τ=−90−31(ASRIτ−μ^)2\hat{\sigma}^{2}\_{\text{AS}}=\frac{1}{T\_{\text{est}}-1}\sum\_{\tau=-90}^{-31}(\text{ASRI}\_{\tau}-\hat{\mu})^{2} |  | (50) |

Autocorrelation diagnostics (Ljung-Box test) indicate insignificant residual correlation beyond lag 15–20, supporting the standard error calculation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SE​(CAS)=σ^AS×Tevent\text{SE}(\text{CAS})=\hat{\sigma}\_{\text{AS}}\times\sqrt{T\_{\text{event}}} |  | (51) |

### F.4 Multiple Testing Correction

With K=4K=4 simultaneous hypothesis tests (one per crisis event), we apply Bonferroni correction:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αadj=αK=0.054=0.0125\alpha\_{\text{adj}}=\frac{\alpha}{K}=\frac{0.05}{4}=0.0125 |  | (52) |

Results: All four events remain significant at the corrected threshold:

* •

  Terra/Luna: p<0.001p<0.001 (<0.0125<0.0125 ✓)
* •

  Celsius/3AC: p<0.001p<0.001 (<0.0125<0.0125 ✓)
* •

  FTX Collapse: p<0.001p<0.001 (<0.0125<0.0125 ✓)
* •

  SVB Crisis: p<0.001p<0.001 (<0.0125<0.0125 ✓)

The Bonferroni correction is conservative; alternative corrections (Holm-Bonferroni, Benjamini-Hochberg) would yield identical conclusions given the extreme significance levels.

### F.5 Window Independence

Table [39](https://arxiv.org/html/2602.03874v1#A6.T39 "Table 39 ‣ F.5 Window Independence ‣ Appendix F Event Study Protocol Specification") documents the temporal separation between crisis events.

Table 39: Event Window Independence Verification

| Event | Est. Start | Est. End | Evt. Start | Evt. End |
| --- | --- | --- | --- | --- |
| Terra/Luna | 2022-02-11 | 2022-04-11 | 2022-04-12 | 2022-05-22 |
| Celsius/3AC | 2022-03-19 | 2022-05-17 | 2022-05-18 | 2022-06-27 |
| FTX Collapse | 2022-08-13 | 2022-10-11 | 2022-10-12 | 2022-11-21 |
| SVB Crisis | 2022-12-11 | 2023-02-08 | 2023-02-09 | 2023-03-21 |

* •

  Estimation windows (60 days) and event windows (41 days) are non-overlapping.
* •

  Terra/Celsius event windows overlap by ≈10\approx 10 days; estimation windows are independent.
* •

  FTX and SVB events are separated by >90>90 days (fully independent).

The partial overlap between Terra/Luna and Celsius/3AC event windows does not invalidate the analysis, as:

1. 1.

   Estimation windows remain independent
2. 2.

   The events represent distinct crisis mechanisms (algorithmic stablecoin vs. CeFi lending)
3. 3.

   Separate CAS calculations use event-specific baselines

### F.6 Placebo Testing

To assess false positive rates under the null hypothesis of no crisis, we conduct placebo analysis on 10 randomly selected non-crisis dates.

#### F.6.1  Placebo Date Selection

Dates were drawn uniformly from the sample period (2021-01 to 2024-12) excluding:

* •

  90-day windows around known crisis events
* •

  First/last 90 days of sample (edge effects)

#### F.6.2  Placebo Results

Table 40: Placebo Test Results

| Metric | Expected | Observed | Interpretation |
| --- | --- | --- | --- |
| Significant at α=0.05\alpha=0.05 | 0.5 (5%) | 1 (10%) | Nominal |
| Significant at α=0.01\alpha=0.01 | 0.1 (1%) | 0 (0%) | Conservative |
| Mean |t||t| (placebo) | — | 1.24 | vs. 23.7 (crisis) |
| Max |t||t| (placebo) | — | 2.18 | vs. 32.6 (crisis) |

The placebo analysis confirms:

1. 1.

   False positive rate is consistent with nominal α\alpha levels
2. 2.

   Crisis events produce dramatically larger tt-statistics than placebo dates
3. 3.

   The 19×\times difference in mean |t||t| between crisis and placebo dates demonstrates genuine discriminative ability

### F.7 Lead Time Measurement

Two complementary lead time definitions are employed:

Definition 1 (First-crossing): Days between first observation exceeding 1.5σ\sigma above baseline and crisis onset. Captures earliest structural warning signal.

Definition 2 (Final-sustained): Days between last observation below threshold before sustained elevation and crisis onset. Captures actionable intervention timing.

Table [7](https://arxiv.org/html/2602.03874v1#S5.T7 "Table 7 ‣ 5.4.3 Bootstrap Confidence Intervals ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") reports first-crossing lead times; Table [5](https://arxiv.org/html/2602.03874v1#S5.T5 "Table 5 ‣ 5.4.2 Event Study Results ‣ 5.4 Event Study Analysis ‣ 5 Empirical Validation") reports final-sustained lead times. The discrepancy between definitions (e.g., Terra/Luna: 72 days first-crossing vs. 30 days final-sustained) reflects ASRI fluctuations between initial detection and crisis onset.

### F.8 Sensitivity to Specification Choices

Table 41: Event Study Robustness to Specification Changes

| Specification | Terra | Celsius | FTX | SVB |
| --- | --- | --- | --- | --- |
| Baseline (60d, const. mean) | \*\*\* | \*\*\* | \*\*\* | \*\*\* |
| 45-day estimation window | \*\*\* | \*\*\* | \*\*\* | \*\*\* |
| 90-day estimation window | \*\*\* | \*\*\* | \*\*\* | \*\*\* |
| AR(1) normal model | \*\*\* | \*\*\* | \*\*\* | \*\* |
| Event window [−20,+10][-20,+10] | \*\*\* | \*\*\* | \*\*\* | \*\*\* |
| Event window [−40,+10][-40,+10] | \*\*\* | \*\*\* | \*\*\* | \*\*\* |

* •

  \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.10p<0.10
* •

  All specifications detect all four crises at p<0.05p<0.05.