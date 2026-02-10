---
authors:
- Murad Farzulla
doc_id: arxiv:2602.07046v1
family_id: arxiv:2602.07046
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Sentiment Without Structure Differential Market Responses to Infrastructure
  vs Regulatory Events in Cryptocurrency Markets
url_abs: http://arxiv.org/abs/2602.07046v1
url_html: https://arxiv.org/html/2602.07046v1
venue: arXiv q-fin
version: 1
year: 2026
---


Murad Farzulla1,2
  
1 King’s College London
  
2 [Dissensus AI](https://dissensus.ai)
  
[ORCID: 0009-0002-7164-8704](https://orcid.org/0009-0002-7164-8704)

(February 2026
  
Corresponding Author: [murad@dissensus.ai](mailto:murad@dissensus.ai))

###### Abstract

We investigate differential market responses to infrastructure versus regulatory events in cryptocurrency markets using event study methodology with 4-category event classification. From 50 candidate events (2019–2025), 31 meet inclusion criteria across Bitcoin, Ethereum, Solana, and Cardano. We employ constant mean and market-adjusted models with event-level block bootstrap confidence intervals that properly account for cross-sectional correlation.

Our primary comparison focuses on negative-valence events: infrastructure failures (8 events) versus regulatory enforcement (7 events). Infrastructure failures produce mean Cumulative Abnormal Return (CAR) of −7.6%-7.6\% (95% CI: [−25.8%,+11.3%][-25.8\%,+11.3\%]) and regulatory enforcement produces mean CAR of −11.1%-11.1\% (CI: [−31.0%,+10.7%][-31.0\%,+10.7\%]). The difference of +3.6+3.6 percentage points has CI [−25.3%,+30.9%][-25.3\%,+30.9\%], p=0.81p=0.81—a null finding indicating markets respond similarly to both shock types when controlling for valence.

Robustness checks confirm consistent results across window specifications, leave-one-out exclusion of major events (FTX, Terra), and alternative market model specifications. The 4-category classification addresses prior conflation of upgrades with failures. This exploratory analysis should be treated as hypothesis-generating.

Keywords: Cryptocurrency, Event Study, Regulation, Infrastructure Risk, Block Bootstrap

JEL Codes: G14, G18, G23

Acknowledgements. The author acknowledges Claude (Anthropic) for assistance with pipeline development and technical writing. All errors, omissions, and interpretive limitations remain the author’s responsibility.

Data & Code Availability. Reproducible code and data are available at <https://github.com/studiofarzulla/sentiment-without-structure>. Analysis conducted in Python 3.11 using NumPy 1.26, SciPy 1.12, and pandas 2.1. All statistical tests use two-sided α=0.05\alpha=0.05; bootstrap CIs are percentile-based with B=5,000B=5{,}000 replications.

## 1 Introduction

Do cryptocurrency markets respond differently to infrastructure failures versus regulatory enforcement? This paper investigates differential market responses using a 4-category event classification that addresses prior conflation of positive and negative events within each type. This study extends prior work on asymmetric volatility response to cryptocurrency shocks (Farzulla, [2025](https://arxiv.org/html/2602.07046v1#bib.bib13)) by focusing on return-level comparisons rather than conditional variance dynamics.

Prior work analyzing infrastructure vs regulatory events often pooled heterogeneous events: halvings (positive infrastructure) with exchange collapses (negative infrastructure), ETF approvals (positive regulatory) with SEC lawsuits (negative regulatory) (Auer and Claessens, [2018](https://arxiv.org/html/2602.07046v1#bib.bib2); Shanaev et al., [2020](https://arxiv.org/html/2602.07046v1#bib.bib30)). This conflation can obscure meaningful comparisons.

We adopt a cleaner design:

* •

  Infra\_Negative: Exchange failures, hacks, collapses (10 events; 8 analyzed∗)
* •

  Infra\_Positive: Protocol upgrades, halvings (6 events)
* •

  Reg\_Negative: Securities and Exchange Commission (SEC) lawsuits, country bans (7 events)
* •

  Reg\_Positive: Exchange-traded fund (ETF) approvals, regulatory clarity (8 events)

∗Two early events (QuadrigaCX 2019, Binance hack 2019) lack sufficient pre-event estimation data.

Our primary comparison tests whether markets respond differently to negative infrastructure events versus negative regulatory events—both represent shocks of similar valence.

Hypothesis specified ex ante (enforcement capacity): Infrastructure failures should produce larger negative CARs than regulatory enforcement because regulators lack direct power over decentralized systems.

### 1.1 Preview of Results

1. 1.

   Infrastructure failures (N=8 analyzed events): Mean CAR =−7.6%=-7.6\%, 95% CI [−25.8%,+11.3%][-25.8\%,+11.3\%]
2. 2.

   Regulatory enforcement (N=7 events): Mean CAR =−11.1%=-11.1\%, 95% CI [−31.0%,+10.7%][-31.0\%,+10.7\%]
3. 3.

   Category Difference (Δ\Delta): +3.6+3.6 pp, CI [−25.3%,+30.9%][-25.3\%,+30.9\%], p=0.81p=0.81
4. 4.

   Window sensitivity: Consistent negative sign across [0,+1][0,+1] to [−5,+30][-5,+30]
5. 5.

   Leave-one-out: Robust to FTX/Terra exclusion (no sign flip)
6. 6.

   Market model: BTC and equal-weighted (EW) proxy confirm results

Bottom line: Event-level block bootstrap (which properly accounts for cross-sectional correlation) produces wide confidence intervals crossing zero. We find no significant difference between infrastructure failures and regulatory enforcement—the effect size is small and statistically indistinguishable from zero with only 8 vs 7 analyzed events.

### 1.2 Contributions

This paper makes three contributions:

1. 1.

   Methodological: We develop a 4-category event classification (infrastructure/regulatory ×\times positive/negative) that enables cleaner hypothesis tests than prior conflated approaches.
2. 2.

   Robustness: We provide market model robustness (BTC as proxy) and pre-event anticipation analysis to address placebo anomalies and information leakage concerns.
3. 3.

   Empirical: We find no significant difference between infrastructure failures and regulatory enforcement in market response—the enforcement capacity hypothesis remains neither confirmed nor rejected, requiring larger samples or alternative identification strategies.

## 2 Literature Review

### 2.1 Event Studies in Cryptocurrency Markets

Event study methodology has been applied to cryptocurrency markets by Auer and Claessens ([2018](https://arxiv.org/html/2602.07046v1#bib.bib2)) and Lucey et al. ([2022](https://arxiv.org/html/2602.07046v1#bib.bib22)), with comprehensive surveys provided by Kothari and Warner ([2007](https://arxiv.org/html/2602.07046v1#bib.bib20)). The foundational event study framework established by MacKinlay ([1997](https://arxiv.org/html/2602.07046v1#bib.bib24)) has been adapted to cryptocurrency settings, though these studies typically find significant abnormal returns around major announcements but rarely distinguish between event types systematically. Recent work has examined regulatory impacts across multiple jurisdictions (Chokor and Alfieri, [2021](https://arxiv.org/html/2602.07046v1#bib.bib9); Koenraadt and Leung, [2024](https://arxiv.org/html/2602.07046v1#bib.bib18); Cumming et al., [2025](https://arxiv.org/html/2602.07046v1#bib.bib11)), generally finding negative market reactions to restrictive regulation.

Auer and Claessens ([2020](https://arxiv.org/html/2602.07046v1#bib.bib3)) provide a comprehensive analysis of regulatory events affecting Bitcoin prices, finding heterogeneous effects depending on regulatory stance (favorable vs unfavorable). More recently, Saggu et al. ([2025](https://arxiv.org/html/2602.07046v1#bib.bib29)) examine SEC classification decisions specifically, finding significant price impacts from securities designations—their named-token approach (analyzing XRP directly for Ripple events) offers cleaner identification than our spillover-based design. Our contribution extends this literature by comparing regulatory events to infrastructure events within a unified framework, and by employing a 4-category classification that separates positive from negative valence within each event type.

Recent methodological advances highlight identification challenges. Goldsmith-Pinkham and Lyu ([2025](https://arxiv.org/html/2602.07046v1#bib.bib14)) show factor model misspecification can bias estimates when treatment and control assets load differently on omitted factors. Casini and McCloskey ([2025](https://arxiv.org/html/2602.07046v1#bib.bib8)) develop “shock dominance” tests for high-frequency settings. For few-cluster inference, MacKinnon et al. ([2023](https://arxiv.org/html/2602.07046v1#bib.bib25)) recommend conservative approaches including the Ibragimov and Müller ([2010](https://arxiv.org/html/2602.07046v1#bib.bib15)) t-test—a method we employ.

### 2.2 Market Microstructure

Cryptocurrency microstructure differs from traditional markets (Makarov and Schoar, [2020](https://arxiv.org/html/2602.07046v1#bib.bib26)). Aste ([2019](https://arxiv.org/html/2602.07046v1#bib.bib1)) provides foundational analysis of dependency and causality structures across nearly two thousand cryptocurrencies, demonstrating that prices are significantly correlated with social sentiment and that major assets like Bitcoin occupy central positions in price correlation networks while playing marginal roles in sentiment networks. This asymmetry between price and sentiment network centrality motivates our focus on how different shock types propagate through market structure. The development of systematic benchmarks such as CRIX (Trimborn and Härdle, [2018](https://arxiv.org/html/2602.07046v1#bib.bib31)) has enabled rigorous market-wide analysis, while indices capturing regulatory-specific risk such as CRRIX (Ni et al., [2025](https://arxiv.org/html/2602.07046v1#bib.bib27)) demonstrate that policy news systematically impacts crypto market dynamics. The absence of designated market makers, 24/7 trading, and cross-exchange fragmentation complicate event study inference. Exchange hacks and regulatory news have been shown to significantly impact Bitcoin volatility (Lyócsa et al., [2020](https://arxiv.org/html/2602.07046v1#bib.bib23)), with spillover effects across international markets (Borri and Shakhnov, [2020](https://arxiv.org/html/2602.07046v1#bib.bib6)). We focus on returns, leaving liquidity extensions to future work.

### 2.3 Infrastructure vs Regulatory Distinction

The distinction between infrastructure and regulatory events is novel to this literature. We define:

Infrastructure events: Direct mechanical impact on transaction execution, custody, protocol functionality, or exchange operations. Examples: exchange failures (Mt. Gox, FTX) with documented systemic contagion effects (Jalan and Matkovskyy, [2023](https://arxiv.org/html/2602.07046v1#bib.bib16); Conlon et al., [2024](https://arxiv.org/html/2602.07046v1#bib.bib10)), protocol failures such as the Terra/UST algorithmic stablecoin collapse (Liu et al., [2023](https://arxiv.org/html/2602.07046v1#bib.bib21); Badev and Watsky, [2023](https://arxiv.org/html/2602.07046v1#bib.bib4)), and network incidents.

Regulatory events: Changes to legal status, enforcement actions, or policy without direct infrastructure impact. Examples: SEC lawsuits, country bans, ETF approvals.

## 3 Data and Event Identification

### 3.1 Event Sample

We identify events through systematic criteria designed to capture economically significant shocks while maintaining statistical validity:

1. 1.

   Impact threshold: Events must satisfy at least one of: (a) same-day absolute BTC return >5%>5\%, (b) 3-day absolute return >5%>5\%, (c) estimated financial impact >$​100>\mathdollar 100 million, or (d) affected user base >100,000>100{,}000 individuals. This captures both market-moving events and significant infrastructure failures that may not immediately reflect in prices.
2. 2.

   Identifiable date: Event has precise announcement or occurrence date with ±1\pm 1 day precision. For gradual events (e.g., Terra depeg), we use the date of first major price discontinuity.
3. 3.

   Public documentation: Event documented in major news sources (CoinDesk, The Block), regulatory filings (SEC, DOJ), or official company communications.
4. 4.

   Event separation: Minimum 7 days between events to avoid overlapping event windows. Events within 30 days are flagged for potential confounding but retained in sample with overlap indicators.

From 50 candidate events (2019–2025), we exclude 3 corporate announcements (Tesla BTC purchase, Coinbase IPO, Taproot upgrade) and reclassify the remaining 47 into 4 categories. Of these, 31 meet our impact threshold criteria. Two early events (QuadrigaCX, Binance 2019 hack) lack sufficient pre-event estimation data due to data availability constraints. Table [1](https://arxiv.org/html/2602.07046v1#S3.T1 "Table 1 ‣ 3.1 Event Sample ‣ 3 Data and Event Identification ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets") summarizes the final sample.

Table 1: Event Sample by 4-Category Classification

|  |  |  |  |
| --- | --- | --- | --- |
| Category | N Events | N Analyzeda | Mean CAR |
| Infra\_Negative | 10 | 8 | −7.6%-7.6\% |
| Infra\_Positive | 6 | 6 | +8.8%+8.8\% |
| Reg\_Negative | 7 | 7 | −11.1%-11.1\% |
| Reg\_Positive | 8 | 8 | −14.3%-14.3\% |
| Excluded | 3 | — | — |
| a Events with sufficient estimation window data (250 days). | | | |
| --- | --- | --- | --- |

Infra\_Negative: FTX (2022-11) (Jalan and Matkovskyy, [2023](https://arxiv.org/html/2602.07046v1#bib.bib16)), Terra (2022-05) (Liu et al., [2023](https://arxiv.org/html/2602.07046v1#bib.bib21)), Celsius (2022-06), Black Thursday (2020-03), Bybit hack (2025-02), BNB bridge hack, Poly hack, Binance hack, QuadrigaCX, USDC depeg.

Reg\_Negative: SEC v. Ripple (2020-12), China bans (2021-05, 2021-09), Kazakhstan shutdown, SEC v. Binance/Coinbase (2023-06), Binance/CZ settlement.

Excluded: Tesla BTC purchase, Coinbase listing, Taproot (corporate/minor).

### 3.2 Asset Universe

We analyze 4 assets with sufficient data: BTC, ETH, SOL, ADA. This yields 118 event-asset observations after excluding cases with insufficient estimation window data.

### 3.3 Price Data

Daily open-high-low-close-volume (OHLCV) data from Binance (2019-01-01 to 2026-01-29). Returns computed as log-differences of closing prices.

Time zone alignment: Daily close prices use Binance’s UTC 00:00 close. Event dates reflect UTC timestamps from news sources (Reuters, Bloomberg, official announcements). For events with intraday timing (e.g., SEC filing at 16:00 EST), we use the first full UTC trading day following the announcement.

## 4 Methodology

### 4.1 Event Study Design

We follow standard event study methodology (MacKinlay, [1997](https://arxiv.org/html/2602.07046v1#bib.bib24)) with adaptations for cryptocurrency markets:

Estimation window: 250 trading days (or 120 minimum for newer assets).

Gap window: 30 days pre-event excluded to avoid anticipation contamination.

Event window: [−5,+30][-5,+30] days around event date (robustness: [−1,+5][-1,+5], [−5,+60][-5,+60]).

### 4.2 Return Models

Notation: Throughout, subscript ii indexes assets (i∈{BTC, ETH, SOL, ADA}i\in\{\text{BTC, ETH, SOL, ADA}\}), tt indexes trading days relative to event date (t=0t=0 is the event day), and jj indexes events. Hats (⋅^\hat{\cdot}) denote estimated parameters; bars (⋅¯\bar{\cdot}) denote sample means.

Capped Returns. Following standard practice for cryptocurrency event studies, we winsorize daily returns at ±50%\pm 50\% to limit the influence of extreme outliers while preserving economically meaningful variation. For catastrophic events like Terra/LUNA (where LUNA collapsed from $80 to $0.01), uncapped returns would produce CARs exceeding −1000%-1000\%, violating standard regression assumptions and dominating all statistical inference. Capping at ±50%\pm 50\% per day retains these events in the sample while maintaining statistical validity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R~i​t=max⁡(min⁡(Ri​t,0.50),−0.50)\tilde{R}\_{it}=\max(\min(R\_{it},0.50),-0.50) |  | (1) |

Primary: Constant Mean Model. Following MacKinlay ([1997](https://arxiv.org/html/2602.07046v1#bib.bib24)), we use a constant mean model as our primary specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​Ri​t=R~i​t−R¯iAR\_{it}=\tilde{R}\_{it}-\bar{R}\_{i} |  | (2) |

where A​Ri​tAR\_{it} denotes the Abnormal Return for asset ii on day tt, and R¯i\bar{R}\_{i} is estimated from the 250-day estimation window using capped returns.

Robustness: Market Model. To address potential bull market drift (which could cause positive placebo CARs), we also estimate a market model using BTC as proxy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​Ri​t=Ri​t−(α^i+β^i​RB​T​C,t)AR\_{it}=R\_{it}-(\hat{\alpha}\_{i}+\hat{\beta}\_{i}R\_{BTC,t}) |  | (3) |

where α^i\hat{\alpha}\_{i} and β^i\hat{\beta}\_{i} are estimated via ordinary least squares (OLS) in the estimation window. For BTC itself, we use constant mean.

Cumulative abnormal returns over event window [τ1,τ2][\tau\_{1},\tau\_{2}] (where τ1\tau\_{1} and τ2\tau\_{2} denote days relative to the event date):

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​A​Ri​(τ1,τ2)=∑t=τ1τ2A​Ri​tCAR\_{i}(\tau\_{1},\tau\_{2})=\sum\_{t=\tau\_{1}}^{\tau\_{2}}AR\_{it} |  | (4) |

### 4.3 Statistical Inference

Critical issue: Degrees of freedom inflation. Standard event study inference pools asset-event observations as i.i.d. With 10 events ×\times 4 assets = 40 observations, a naive t-test uses N=40N=40 when the true degrees of freedom is closer to N=10N=10 (events). This inflates statistical power artificially.

Solution: Event-level block bootstrap. We implement a block bootstrap that resamples entire events with replacement, keeping all assets within each event together. This respects the cross-sectional correlation of returns within an event (Cameron et al., [2008](https://arxiv.org/html/2602.07046v1#bib.bib7); Petersen, [2009](https://arxiv.org/html/2602.07046v1#bib.bib28)). Event-induced variance—a well-documented phenomenon where announcement days exhibit elevated volatility (Boehmer et al., [1991](https://arxiv.org/html/2602.07046v1#bib.bib5))—further motivates our conservative inference approach:

1. 1.

   Compute CAR for each event-asset pair
2. 2.

   Within-event averaging: Compute event-level CAR by averaging across assets within each event—this ensures each event receives equal weight regardless of asset coverage
3. 3.

   Bootstrap: resample event IDs (not individual observations)
4. 4.

   Compute mean of event-level CARs for each bootstrap sample
5. 5.

   Repeat 5,000 times for confidence intervals

Weighting clarification: We verified results under both observation-weighted (pooling all asset-CARs) and event-equal-weighted (averaging within events first) bootstrap schemes. Results are nearly identical: Infra mean CAR shifts from −7.55%-7.55\% to −7.94%-7.94\%, Reg from −11.11%-11.11\% to −9.41%-9.41\%, with DiD p-values of 0.81 vs 0.93. The null finding is robust to weighting specification.

Kolari-Pynnonen adjustment: For reference, we also report KP-adjusted t-statistics that account for cross-sectional correlation (Kolari and Pynnonen, [2010](https://arxiv.org/html/2602.07046v1#bib.bib19)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | tK​P=tu​n​a​d​j1+(N−1)​ρ¯t\_{KP}=\frac{t\_{unadj}}{\sqrt{1+(N-1)\bar{\rho}}} |  | (5) |

where ρ¯\bar{\rho} is average cross-sectional correlation of abnormal returns. However, the bootstrap confidence intervals provide more conservative inference.

### 4.4 Pre-Registration and Specification Transparency

Event windows ([−5,+30][-5,+30] primary, [−1,+5][-1,+5] and [−5,+60][-5,+60] robustness), return capping (±50%\pm 50\%), and the bootstrap procedure were specified prior to computing final results but were not formally pre-registered. Event selection criteria evolved iteratively during data collection as we encountered edge cases (e.g., gradual vs sudden failures). We report all specifications tested; no tests were conducted and suppressed. The 4-category classification was developed after initial data exploration revealed conflation issues in 2-category (infrastructure/regulatory) approaches.

### 4.5 Category Comparison

Our primary test compares mean CARs between infrastructure and regulatory events:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ=C​A​R¯i​n​f​r​a−C​A​R¯r​e​g\Delta=\overline{CAR}\_{infra}-\overline{CAR}\_{reg} |  | (6) |

with event-level block bootstrap confidence intervals. Note this is a difference in means, not a true difference-in-differences estimator (which would require panel structure with treatment/control groups observed pre/post). The bootstrap resamples events within each group independently, then computes the difference.

## 5 Results

### 5.1 Primary Analysis: Negative Events Only

Our primary comparison controls for event valence by comparing only negative-valence events. Table [2](https://arxiv.org/html/2602.07046v1#S5.T2 "Table 2 ‣ 5.1 Primary Analysis: Negative Events Only ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets") presents results with event-level block bootstrap confidence intervals.

Table 2: Primary Comparison: Negative Events Only (Block Bootstrap)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Infra\_Neg | Reg\_Neg | Δ\Delta |
| N events (analyzed)b | 8 | 7 | — |
| N observationsc | 31 | 27 | 58 |
| Mean CAR | −7.6%-7.6\% | −11.1%-11.1\% | +3.6+3.6 pp |
| Bootstrap 95% CI | [−25.8%-25.8\%, +11.3%+11.3\%] | [−31.0%-31.0\%, +10.7%+10.7\%] | [−25.3%-25.3\%, +30.9%+30.9\%] |
| Bootstrap SE | 9.5%9.5\% | 10.7%10.7\% | 14.3%14.3\% |
| Bootstrap p-value | 0.43 | 0.31 | 0.81 |
| Note: CI crosses zero for all comparisons. Results shown use observation-weighted bootstrap. | | | |
| --- | --- | --- | --- |
| Event-equal-weighted bootstrap yields similar results: Infra −7.9%-7.9\%, Reg −9.4%-9.4\%, Δ=+1.5\Delta=+1.5 pp, p=0.93p=0.93. | | | |
| b Events with sufficient estimation data; 2 infrastructure events excluded (QuadrigaCX, Binance ’19). | | | |
| c N observations = event-asset pairs; some events predate SOL/ADA price availability. | | | |

Key finding: Bootstrap confidence intervals are substantially wider than naive t-test would suggest. The category difference (Δ=+3.6\Delta=+3.6 pp) has a 95% CI of [−25.3%-25.3\%, +30.9%+30.9\%], comfortably crossing zero (p=0.81p=0.81). This is a null finding: we cannot distinguish between infrastructure failures and regulatory enforcement in terms of market response.

Model robustness: Since the placebo test indicates mild positive drift under constant mean (p=0.08p=0.08), we verify robustness using the market model (Section [5.3](https://arxiv.org/html/2602.07046v1#S5.SS3 "5.3 Market Model Robustness ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets")). Under market model specification: C​A​RI​n​f​r​a​\_​N​e​g=−3.0%CAR\_{Infra\\_Neg}=-3.0\%, C​A​RR​e​g​\_​N​e​g=−10.3%CAR\_{Reg\\_Neg}=-10.3\%, yielding Δ=+7.3\Delta=+7.3 pp. The larger point estimate reflects market model’s correction for bull market drift, but remains economically small and directionally consistent with the null finding. Both specifications fail to reject H0:Δ=0H\_{0}:\Delta=0.

### 5.2 Secondary Analysis: Positive Events

Positive events show interesting patterns (Table [3](https://arxiv.org/html/2602.07046v1#S5.T3 "Table 3 ‣ 5.2 Secondary Analysis: Positive Events ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets")):

Table 3: Secondary Comparison: Positive Events

|  | Infra\_Pos | Reg\_Pos |
| --- | --- | --- |
| Mean CAR | +8.83%+8.83\% | −14.27%-14.27\% |
| N observations | 21 | 31 |

Notably, “positive” regulatory events (ETF approvals, clarity) produce negative mean CARs (−14.3%-14.3\%). This counterintuitive finding—the “Reg\_Positive puzzle”—warrants detailed investigation.

Event-by-event breakdown: Of 8 Reg\_Positive events:

* •

  6 negative CARs: El Salvador BTC legal tender (−56%-56\%), BITO ETF launch (−27%-27\%), BlackRock spot ETF approval (−10%-10\%), SEC drops Ripple (−8%-8\%), Wyoming DAO law (−5%-5\%), MiCA passage (−2%-2\%)
* •

  2 positive CARs: BlackRock ETF filing (+18%+18\%), US crypto executive order (+4%+4\%)

Confounding analysis: 4 of 8 events (50%) have overlapping negative events within 30 days:

* •

  El Salvador (2021-06-09): overlaps China mining ban (2021-05-19)
* •

  BlackRock spot approval (2024-01-10): overlaps Grayscale selling pressure
* •

  SEC drops Ripple (2025-02): overlaps Bybit hack (2025-02-21)
* •

  BITO ETF (2021-10-19): overlaps China crypto ban (2021-09-24)

Potential mechanisms: This “positive news, negative returns” pattern may reflect: (1) sell the news dynamics after price run-ups in anticipation (pre-event CARs for Reg\_Positive average −25.8%-25.8\%, suggesting heavy front-running), (2) overlapping negative shocks dominating the event window, (3) regulatory clarity reducing speculative premium by eliminating upside optionality, or (4) realized events underperforming market expectations. The high overlap rate (50%) suggests mechanism (2) contributes substantially, but disentangling these effects requires finer-grained identification—potentially intraday analysis or synthetic control methods to isolate treatment effects.

### 5.3 Market Model Robustness

To address potential bull market drift, we re-estimate using a market model with BTC as proxy:

Table 4: Market Model Results by Category

|  |  |  |
| --- | --- | --- |
| Category | Mean CAR | N siga |
| Infra\_Negative | −3.0%-3.0\% | 3/31 |
| Reg\_Negative | −10.3%-10.3\% | 4/27 |
| Infra\_Positive | +4.7%+4.7\% | 1/21 |
| Reg\_Positive | −7.7%-7.7\% | 0/31 |
| a Asset-event observations with |C​A​R|>2​σ|CAR|>2\sigma (individual 5% level). | | |
| --- | --- | --- |

Market-adjusted CARs are attenuated but directionally consistent. Mean betas (vs BTC): ETH ≈0.97\approx 0.97, SOL ≈1.10\approx 1.10, ADA ≈0.99\approx 0.99—close to unity, confirming high crypto market correlation.

Category difference under market model: For negative events, ΔM​M=−3.0%−(−10.3%)=+7.3\Delta\_{MM}=-3.0\%-(-10.3\%)=+7.3 pp, compared to ΔC​M=+3.6\Delta\_{CM}=+3.6 pp under constant mean. The market model’s larger point estimate reflects correction for bull market drift (evident in placebo test p=0.08p=0.08), but both specifications yield the same inference: no statistically significant difference between event categories.

### 5.4 Cross-Asset Heterogeneity

To examine whether infrastructure and regulatory events affect assets differentially, we decompose CARs by individual cryptocurrency (Table [5](https://arxiv.org/html/2602.07046v1#S5.T5 "Table 5 ‣ 5.4 Cross-Asset Heterogeneity ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets")).

Table 5: Cross-Asset Heterogeneity: CAR by Event Type and Asset

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Event Type | BTC | ETH | SOL | ADA | Spreada |
| Infra\_Negative | −7.2%-7.2\% | −9.1%-9.1\% | −8.9%-8.9\% | −9.4%-9.4\% | 2.2 pp |
| Reg\_Negative | −6.4%-6.4\% | −14.2%-14.2\% | −11.8%-11.8\% | −12.1%-12.1\% | 7.8 pp |
| a Spread = max −- min CAR across assets (measures cross-asset heterogeneity). | | | | | |

Key observation: Regulatory events show greater cross-asset heterogeneity (spread = 7.8 pp) than infrastructure events (spread = 2.2 pp). BTC exhibits muted regulatory response (−6.4%-6.4\%) relative to ETH, SOL, and ADA (−11.8%-11.8\% to −14.2%-14.2\%). This pattern is consistent with BTC’s “digital gold” narrative insulating it from regulatory uncertainty that more directly threatens smart contract platforms and their DeFi ecosystems. Infrastructure failures produce uniform responses across assets—consistent with systemic contagion through correlated liquidations.

### 5.5 Pre-Event Anticipation

We compute CAR in the [−30,−1][-30,-1] window to detect information leakage:

Table 6: Pre-Event CAR by Category

| Category | Pre-CAR |
| --- | --- |
| Infra\_Negative | −12.5%-12.5\% |
| Infra\_Positive | −4.1%-4.1\% |
| Reg\_Negative | −0.2%-0.2\% |
| Reg\_Positive | −25.8%-25.8\% |

No significant difference in anticipation between infrastructure and regulatory events (Welch’s t=0.94t=0.94, p=0.35p=0.35).

### 5.6 Window Sensitivity

We test robustness across tighter event windows to verify effects are not driven by long-window drift:

Table 7: Window Sensitivity Analysis

|  |  |  |  |
| --- | --- | --- | --- |
| Window | Infra\_Neg | Reg\_Neg | Sign Consistent |
| [0,+1][0,+1] | −6.1%-6.1\% | −5.8%-5.8\% | ✓ |
| [0,+3][0,+3] | −6.9%-6.9\% | −10.2%-10.2\% | ✓ |
| [0,+5][0,+5] | −7.7%-7.7\% | −12.8%-12.8\% | ✓ |
| [−5,+30][-5,+30] | −5.2%-5.2\% | −8.1%-8.1\% | ✓ |
| Note: Mean CARs shown; inference in main text uses event-level bootstrap. | | |  |

Both event types show consistent negative sign across all windows. Notably, shorter windows ([0,+5][0,+5] and tighter) show significant negative CARs that dilute in the longer [−5,+30][-5,+30] window—suggesting the immediate impact is real but becomes noisier over time.

### 5.7 Leave-One-Out: Major Events

FTX and Terra dominate the infrastructure category—consistent with high-frequency studies documenting exceptional volatility during these collapses (Esparcia et al., [2024](https://arxiv.org/html/2602.07046v1#bib.bib12)). We test sensitivity to their exclusion:

Table 8: Leave-One-Out Analysis: Major Infrastructure Events

| Exclusion | Leave-One-Out CAR | Change | Sign Flip? |
| --- | --- | --- | --- |
| Baseline (8 analyzed) | −7.6%-7.6\% | — | — |
| Excl. FTX | −4.50%-4.50\% | +40.4%+40.4\% | No |
| Excl. Terra | −2.66%-2.66\% | +64.7%+64.7\% | No |

Excluding FTX or Terra changes magnitude substantially but does not flip the sign. Results are robust to outlier exclusion.

### 5.8 Alternative Market Proxy

As additional robustness, we re-estimate using an equal-weighted (EW) market index with leave-one-out construction (excluding the asset being analyzed from the market proxy). Table [9](https://arxiv.org/html/2602.07046v1#S5.T9 "Table 9 ‣ 5.8 Alternative Market Proxy ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets") presents full results by category.

Table 9: Equal-Weighted Market Model Results by Category

|  |  |  |  |
| --- | --- | --- | --- |
| Category | Mean CAR | N sig.a | N obs |
| Infra\_Negative | −0.6%-0.6\% | 3/31 | 31 |
| Reg\_Negative | −5.4%-5.4\% | 4/27 | 27 |
| Infra\_Positive | +4.7%+4.7\% | 1/21 | 21 |
| Reg\_Positive | −7.7%-7.7\% | 0/31 | 31 |
| a Observations with |C​A​R|>2​σ|CAR|>2\sigma. EW market uses leave-one-out construction. | | | |
| --- | --- | --- | --- |

Market-adjusted CARs are attenuated compared to constant mean model but remain directionally consistent. The category difference (Δ\Delta) shrinks but the null finding persists: infrastructure and regulatory events remain statistically indistinguishable.

### 5.9 Placebo Test

We generate 200 pseudo-events by randomly sampling dates (2019–2025) that do not overlap with real events (±30\pm 30 days excluded). Pseudo-events are stratified to match the weekday distribution of actual events. Each pseudo-event receives the same window structure [−5,+30][-5,+30] as the main analysis.

Placebo results: Mean CAR =+2.1%=+2.1\%, p=0.08p=0.08. Borderline non-significant, indicating constant mean model adequately controls for systematic drift, though slight positive bias suggests bull market effects may attenuate measured CARs.

### 5.10 Exact Permutation Test

As robustness to bootstrap inference with small N, we conduct an exact permutation test for H0: no difference between infrastructure and regulatory event CARs. With 8 infrastructure and 7 regulatory events yielding valid CARs, there are (158)=6,435\binom{15}{8}=6{,}435 possible group assignments. The observed difference of +1.5+1.5 pp yields an exact two-tailed p=0.93p=0.93, confirming the bootstrap result (p=0.81p=0.81): no significant difference between event types.

### 5.11 Winsorization Sensitivity

To address concerns about the ±50%\pm 50\% return cap, we re-estimate results across four winsorization levels (Table [10](https://arxiv.org/html/2602.07046v1#S5.T10 "Table 10 ‣ 5.11 Winsorization Sensitivity ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets")).

Table 10: Winsorization Sensitivity Analysis

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Cap Level | Infra\_Neg | Reg\_Neg | Δ\Delta | p-value | Null? |
| ±30%\pm 30\% | −5.0%-5.0\% | −7.8%-7.8\% | +2.8+2.8 pp | 0.85 | ✓ |
| ±50%\pm 50\% (baseline) | −5.8%-5.8\% | −8.1%-8.1\% | +2.3+2.3 pp | 0.88 | ✓ |
| ±75%\pm 75\% | −5.2%-5.2\% | −8.1%-8.1\% | +3.0+3.0 pp | 0.84 | ✓ |
| Uncapped | −5.2%-5.2\% | −8.1%-8.1\% | +3.0+3.0 pp | 0.84 | ✓ |
| Note: Δ\Delta = Infra - Reg. Null = 95% CI crosses zero. All levels confirm null finding. | | | | | |

Results are robust to winsorization specification. The similarity between ±75%\pm 75\% and uncapped results suggests extreme returns are rare in our sample.

### 5.12 Event Selection Bias

A reviewer concern: the return threshold (|BTC|>5%|\text{BTC}|>5\%) conditions on the outcome variable. Table [11](https://arxiv.org/html/2602.07046v1#S5.T11 "Table 11 ‣ 5.12 Event Selection Bias ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets") decomposes events by selection criterion.

Table 11: Event Selection Criteria Breakdown

|  |  |  |  |
| --- | --- | --- | --- |
| Category | Exogenousa | Return Thresholdb | Total |
| Infra\_Negative | 9 | 1 | 10 |
| Reg\_Negative | 6 | 1 | 7 |
| a Known major event, selected regardless of return. | | | |
| --- | --- | --- | --- |
| b Selected primarily due to |BTC|>5%|\text{BTC}|>5\% return threshold. | | | |

The vast majority (15/17 = 88%) of negative events are “exogenous”—known major events identified through news documentation and financial impact criteria, not return thresholds. Re-estimating on exogenous-only events yields:

* •

  Exogenous Infra\_Negative (N=9): CAR =−13.7%=-13.7\%
* •

  Exogenous Reg\_Negative (N=6): CAR =−6.6%=-6.6\%
* •

  Δ=−7.2\Delta=-7.2 pp, p=0.61p=0.61

The null finding holds in the exogenous-only subsample (p=0.61p=0.61), confirming that event selection on return thresholds does not drive results.

### 5.13 Non-Overlapping Events Robustness

A reviewer concern: 17 event pairs fall within 30 days of each other, potentially confounding inference. We address this via two approaches (Table [12](https://arxiv.org/html/2602.07046v1#S5.T12 "Table 12 ‣ 5.13 Non-Overlapping Events Robustness ‣ 5 Results ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets")).

Table 12: Non-Overlap Robustness Checks

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Approach | N Infra | N Reg | Δ\Delta | p-value | Null? |
| Baseline (all events, [−5,+30][-5,+30]) | 8 | 7 | +3.6+3.6 pp | 0.81 | ✓ |
| Independent events only | 6 | 2 | −8.8-8.8 pp | 0.83 | ✓ |
| Short window [0,+5][0,+5] | 9 | 7 | +4.9+4.9 pp | 0.48 | ✓ |
| Independent + short window | 6 | 2 | −1.1-1.1 pp | 0.94 | ✓ |
| Note: “Independent” = no overlapping events within 30 days. All approaches confirm null. | | | | | |
| --- | --- | --- | --- | --- | --- |

The short window [0,+5][0,+5] specification produces tighter confidence intervals (reduced contamination from post-event drift), yet the null finding persists. Even the most conservative specification (independent events with short window) yields p=0.94p=0.94. Overlap does not explain away the null result.

### 5.14 Few-Cluster Inference: Ibragimov-Müller Test

With only 8 vs 7 events, standard bootstrap may be unreliable. Following Ibragimov and Müller ([2010](https://arxiv.org/html/2602.07046v1#bib.bib15)) and MacKinnon et al. ([2023](https://arxiv.org/html/2602.07046v1#bib.bib25)), we apply a simple t-test on event-level mean CARs—treating each event as an independent cluster.

Results: Infra\_Negative mean CAR =−7.9%=-7.9\% (N=8 events), Reg\_Negative mean CAR =−9.4%=-9.4\% (N=7 events). Difference =+1.5=+1.5 pp, t=0.09t=0.09, p=0.93p=0.93, 95% CI [−32.5%,+35.4%][-32.5\%,+35.4\%].

The IM test converges with bootstrap inference (pb​o​o​t​s​t​r​a​p=0.81p\_{bootstrap}=0.81, pI​M=0.93p\_{IM}=0.93), providing triangulation that the null finding is robust to few-cluster concerns.

### 5.15 Black Thursday Sensitivity

A reviewer concern: the March 2020 “Black Thursday” crash was a global macro liquidation event (COVID panic affecting all asset classes), not a crypto-specific infrastructure failure. We test sensitivity to this classification choice:

* •

  With Black Thursday (N=8 events): Infra CAR =−7.9%=-7.9\%, Δ=+1.5\Delta=+1.5 pp, p=0.92p=0.92
* •

  Excluding Black Thursday (N=7 events): Infra CAR =−6.2%=-6.2\%, Δ=+3.2\Delta=+3.2 pp, p=0.81p=0.81

Black Thursday contributes a −20.3%-20.3\% CAR to the infrastructure category (other events average −6.2%-6.2\%). However, exclusion does not change inference: the null finding is robust to this classification choice. Both specifications yield CIs crossing zero with p>0.80p>0.80.

### 5.16 Infrastructure Subtype Heterogeneity

Infrastructure events span distinct failure modes: exchange collapses (FTX, Celsius, QuadrigaCX), protocol failures (Terra/UST), bridge/hack events (BNB bridge, Poly Network, Binance ’19, Bybit), and market-wide liquidations (Black Thursday, USDC depeg). We examine whether these subtypes produce different CARs:

* •

  Exchange collapses (N=3: FTX, Celsius, QuadrigaCX∗): Mean CAR =−23.3%=-23.3\%
* •

  Protocol failures (N=1: Terra): Mean CAR =−40.5%=-40.5\%
* •

  Hacks/exploits (N=4: BNB bridge, Poly, Binance∗, Bybit): Mean CAR =+4.8%=+4.8\%
* •

  Liquidation cascades (N=2: Black Thursday, USDC depeg): Mean CAR =−5.4%=-5.4\%

∗Insufficient estimation data; excluded from analysis but shown for completeness.

Pattern: Exchange and protocol failures produce severe negative CARs (−23%-23\% to −41%-41\%), while hacks/exploits produce positive mean CAR (+4.8%+4.8\%). This counterintuitive result for hacks may reflect: (1) recovery of stolen funds (Poly returned $600M), (2) “any publicity” effect, or (3) small N noise. With only 1–4 events per subtype, formal statistical tests are not meaningful. Future work with larger samples could examine whether markets price different infrastructure failure modes distinctly.

## 6 Discussion

### 6.1 What the Data Actually Show

The enforcement capacity hypothesis predicted infrastructure failures would have larger negative effects than regulatory enforcement. Our data show:

* •

  Infrastructure failures: CAR =−7.6%=-7.6\%, 95% CI [−25.8%,+11.3%][-25.8\%,+11.3\%]
* •

  Regulatory enforcement: CAR =−11.1%=-11.1\%, 95% CI [−31.0%,+10.7%][-31.0\%,+10.7\%]
* •

  Difference: +3.6+3.6 pp, 95% CI [−25.3%,+30.9%][-25.3\%,+30.9\%], p=0.81p=0.81

Interpretation: We cannot distinguish between the two event types statistically. Both produce similar negative returns. The enforcement capacity hypothesis is not confirmed, but neither is the alternative that regulatory events have larger effects.

### 6.2 Theoretical Framework: Bounded vs Unbounded Uncertainty

Important caveat: The following is post-hoc speculation for hypothesis-generation, not a finding. This constitutes HARKing—the framework was developed after observing results. Causal claims require prospective testing.

The similar market responses to infrastructure and regulatory events—despite their fundamentally different mechanisms—may be understood through Knight’s ([1921](https://arxiv.org/html/2602.07046v1#bib.bib17)) distinction between risk (quantifiable probability distributions) and uncertainty (unknowable future states).

Infrastructure failures represent bounded uncertainty:

* •

  Quantifiable losses: When FTX collapses, the missing customer funds ($8B) are eventually documented (Jalan and Matkovskyy, [2023](https://arxiv.org/html/2602.07046v1#bib.bib16); Conlon et al., [2024](https://arxiv.org/html/2602.07046v1#bib.bib10)). Terra’s death spiral destroyed $40B in identifiable value (Liu et al., [2023](https://arxiv.org/html/2602.07046v1#bib.bib21); Badev and Watsky, [2023](https://arxiv.org/html/2602.07046v1#bib.bib4)).
* •

  Observable contagion: Credit exposures propagate through known counterparty networks (Three Arrows →\to Celsius →\to BlockFi) (Conlon et al., [2024](https://arxiv.org/html/2602.07046v1#bib.bib10)).
* •

  Recovery mechanisms exist: Bankruptcy proceedings, protocol forks, and insurance funds provide resolution paths.
* •

  Timeline bounded: Infrastructure crises typically resolve within weeks to months.

Regulatory events introduce unbounded uncertainty:

* •

  Enforcement scope unknown: SEC lawsuits against Ripple, Binance, and Coinbase each took 2–4 years to resolve, with uncertain outcomes throughout.
* •

  Precedent effects unclear: A ruling against one token creates unknown implications for structurally similar assets.
* •

  Policy trajectory uncertain: Regulatory stance shifts with administrations, personnel changes, and political winds.
* •

  Timeline unbounded: Regulatory uncertainty can persist indefinitely—the SEC has never provided clear classification criteria.

Implication for similar CARs: If markets price both shock types similarly despite different mechanisms, it may reflect: (1) offsetting effects where bounded infrastructure losses are acute but recoverable, while unbounded regulatory uncertainty persists but is less immediately devastating, or (2) market participants simply responding to negative sentiment regardless of source.

Testable prediction: If this framework is correct, infrastructure CARs should mean-revert faster than regulatory CARs over 60–90 day windows as uncertainty resolves. Our data are insufficient to test this—a limitation for future work with longer event windows.

### 6.3 Limitations

1. 1.

   Statistical power: With only 8 vs 7 events (not 31 vs 27 observations), the true degrees of freedom are very low. Bootstrap CI width of ±25%\pm 25\% reflects this uncertainty.

   Power calculation: Observed effect size d=Δ/σp​o​o​l​e​d=0.036/0.27≈0.13d=\Delta/\sigma\_{pooled}=0.036/0.27\approx 0.13. Using the standard two-sample t-test power formula with α=0.05\alpha=0.05 and 1−β=0.801-\beta=0.80:

   |  |  |  |
   | --- | --- | --- |
   |  | Np​e​r​g​r​o​u​p=2​(z1−α/2+z1−βd)2=2​(1.96+0.840.13)2≈930N\_{per\ group}=2\left(\frac{z\_{1-\alpha/2}+z\_{1-\beta}}{d}\right)^{2}=2\left(\frac{1.96+0.84}{0.13}\right)^{2}\approx 930 |  |

   The minimum detectable effect (MDE) at 80% power with N=8N=8 vs 77 events is:

   |  |  |  |
   | --- | --- | --- |
   |  | M​D​E=(z1−α/2+z1−β)×σp​o​o​l​e​d×1/n1+1/n2=2.80×0.27×0.53≈40%MDE=(z\_{1-\alpha/2}+z\_{1-\beta})\times\sigma\_{pooled}\times\sqrt{1/n\_{1}+1/n\_{2}}=2.80\times 0.27\times 0.53\approx 40\% |  |

   Our observed difference of 3.6 pp is far below the 40% MDE threshold. This study is therefore best interpreted as exploratory rather than confirmatory; the wide confidence intervals reflect genuine uncertainty rather than precise null effects. We can only detect very large differences (>40>40 pp) with current sample size.
2. 2.

   Single exchange data: All prices from Binance OHLCV. Platform-specific biases (outages during high-volatility periods, regional restrictions, listing/delisting timing) may affect results. Multi-venue analysis using aggregated price indices (e.g., CoinGecko volume-weighted average, Kaiko composite) would strengthen robustness. Binance-specific events (Binance hack, SEC v. Binance, Binance/CZ settlement) may have differential Binance price impacts compared to other exchanges—cross-venue analysis could decompose direct vs spillover effects.
3. 3.

   Daily frequency: Events often unfold intraday; daily windows invite contamination from adjacent news cycles. Higher-frequency analysis could reduce overlap and timing noise.
4. 4.

   Asset universe: We analyze BTC, ETH, SOL, ADA—large-cap assets experiencing spillover effects. We exclude directly named tokens in regulatory actions (e.g., XRP in SEC v. Ripple). This design choice captures broad market response but bypasses direct treatment effects, potentially attenuating measured regulatory impacts.
5. 5.

   Event dating: For gradual events (e.g., Terra depeg), dating by “first major price discontinuity” partially conditions on the outcome. News-timestamped approaches could mitigate this concern.
6. 6.

   Sample period: 2019–2025 may not generalize to different market regimes.
7. 7.

   Factor model specification: Our constant mean and single-factor market models may suffer from omitted factor bias (Goldsmith-Pinkham and Lyu, [2025](https://arxiv.org/html/2602.07046v1#bib.bib14)). Synthetic control methods (e.g., gsynth or PCA-based counterfactuals) could construct more sophisticated donor pools, potentially improving counterfactual estimation. However, with only 4 assets and high cross-asset correlation (ρ≈0.8\rho\approx 0.8–0.950.95), donor pool construction is constrained. We leave synthetic control analysis to future work with broader asset universes.
8. 8.

   Event heterogeneity: Even within categories, events vary substantially (FTX vs QuadrigaCX scale differs 100x). Leave-one-out analysis confirms FTX/Terra exclusion changes magnitude by 40–65% but does not flip sign.
9. 9.

   Overlapping events: 17 event pairs within 30 days may confound. Reg\_Positive anomaly (6/8 negative) may be partially explained by overlapping negative events.
10. 10.

    Survivorship bias: Partially addressed via capped returns, but assets with complete collapse (LUNA post-failure) cannot contribute multi-day CARs after becoming illiquid.

### 6.4 Implications

For researchers: The 4-category classification is a methodological improvement. Future studies should distinguish positive/negative within infrastructure/regulatory.

For investors: Neither event type clearly dominates in market impact when controlling for valence. Both infrastructure failures and regulatory enforcement produce roughly 8–11% negative CARs.

For regulators: No evidence that regulatory announcements have muted effects. Markets do respond to regulatory uncertainty.

## 7 Conclusion

This paper provides a methodological improvement to cryptocurrency event studies through 4-category classification (infrastructure/regulatory ×\times positive/negative), enabling cleaner hypothesis tests than prior conflated approaches.

Main finding: When comparing only negative-valence events, this exploratory analysis finds no statistically significant difference between infrastructure failures (CAR =−7.6%=-7.6\%) and regulatory enforcement (CAR =−11.1%=-11.1\%). The difference of 3.6 percentage points is indistinguishable from zero (p=0.81p=0.81, bootstrap), though with only 8 vs 7 events, confidence intervals are wide (±25%\pm 25\%).

What this means: The enforcement capacity hypothesis—that infrastructure events should dominate regulatory events—is neither confirmed nor rejected. These exploratory findings suggest markets respond similarly to both shock types when controlling for valence, though definitive conclusions await larger samples.

Robustness: Results are confirmed across multiple specifications: (1) market model with BTC and EW proxies, (2) exact permutation test (p=0.93p=0.93), (3) alternative winsorization levels (±30%\pm 30\% to uncapped), (4) exogenous-only event subsample (p=0.61p=0.61), (5) pre-event analysis showing no differential anticipation, (6) non-overlapping events only (p=0.83p=0.83), (7) short window [0,+5][0,+5] (p=0.48p=0.48), and (8) Ibragimov-Müller few-cluster test (p=0.93p=0.93).

Future research: Larger event samples (power analysis suggests N≈3,000N\approx 3{,}000 per category for 80% power), pre-registered hypotheses, non-overlapping event windows, and multi-venue price data are needed for confirmatory tests. The “uncertainty resolution” interpretation (Section 6.2) remains speculative pending prospective testing. Named-token analysis à la Saggu et al. ([2025](https://arxiv.org/html/2602.07046v1#bib.bib29))—examining directly treated assets (e.g., XRP in SEC v. Ripple) rather than spillovers—offers a promising identification strategy.

## Appendix A Full Event Sample

Table [13](https://arxiv.org/html/2602.07046v1#A1.T13 "Table 13 ‣ Appendix A Full Event Sample ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets") lists all negative-valence events meeting our selection criteria, with selection criterion and overlap status. Selection criteria: “Exogenous” = included via major event status or news impact threshold only; “Return” = included due to |RB​T​C|>5%|R\_{BTC}|>5\% on event day; “Both” = met both criteria. Overlap: events within 30 days of another event.

Table 13: Full Event List: Negative Events

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Date | Event | Category | Selection | Overlap |
| Infrastructure Negative (N=10, analyzed=8) | | | | |
| 2019-02-15 | QuadrigaCX collapse | Infra\_Neg | Exogenous | — |
| 2019-05-07 | Binance hack ’19 | Infra\_Neg | Exogenous | — |
| 2020-03-12 | Black Thursday | Infra\_Neg | Both | — |
| 2021-08-10 | Poly Network hack | Infra\_Neg | Both | EIP-1559 |
| 2022-05-09 | Terra/UST crash | Infra\_Neg | Both | — |
| 2022-06-12 | Celsius freeze | Infra\_Neg | Both | — |
| 2022-10-06 | BNB bridge hack | Infra\_Neg | Exogenous | ETH Merge |
| 2022-11-11 | FTX bankruptcy | Infra\_Neg | Both | — |
| 2023-03-10 | USDC depeg (SVB) | Infra\_Neg | Both | — |
| 2025-02-21 | Bybit hack | Infra\_Neg | Exogenous | SEC drops |
| Regulatory Negative (N=7, all analyzed) | | | | |
| 2020-12-22 | SEC v. Ripple | Reg\_Neg | Exogenous | ETH2 Beacon |
| 2021-05-19 | China mining ban | Reg\_Neg | Both | SV BTC legal |
| 2021-09-24 | China crypto ban | Reg\_Neg | Exogenous | BITO ETF |
| 2022-01-05 | Kazakhstan shutdown | Reg\_Neg | Both | — |
| 2023-06-05 | SEC v. Binance | Reg\_Neg | Exogenous | SEC v. CB |
| 2023-06-06 | SEC v. Coinbase | Reg\_Neg | Both | BlackRock |
| 2023-11-21 | Binance/CZ $4.3B | Reg\_Neg | Exogenous | — |
| Note: 2 infrastructure events (QuadrigaCX, Binance ’19) lack 250-day estimation windows. | | | | |

## Appendix B Full 31-Event Sample

Table LABEL:tab:full\_31\_events lists all 31 events meeting our selection criteria across all four categories. Events are sorted by date within category.

Table 14: Complete Event Sample (N=31)

| Date | Event | Category | CAR | N Assets |
| --- | --- | --- | --- | --- |
| Infrastructure Negative (N=10, analyzed=8) | | | | |
| 2019-02-15 | QuadrigaCX collapse | Infra\_Neg | — | 0∗ |
| 2019-05-07 | Binance hack ’19 | Infra\_Neg | — | 0∗ |
| 2020-03-12 | Black Thursday | Infra\_Neg | −20.3%-20.3\% | 3 |
| 2021-08-10 | Poly Network hack | Infra\_Neg | +34.1%+34.1\% | 4 |
| 2022-05-09 | Terra/UST crash | Infra\_Neg | −40.5%-40.5\% | 4 |
| 2022-06-12 | Celsius freeze | Infra\_Neg | −25.9%-25.9\% | 4 |
| 2022-10-06 | BNB bridge hack | Infra\_Neg | +22.7%+22.7\% | 4 |
| 2022-11-11 | FTX bankruptcy | Infra\_Neg | −28.1%-28.1\% | 4 |
| 2023-03-10 | USDC depeg (SVB) | Infra\_Neg | +15.4%+15.4\% | 4 |
| 2025-02-21 | Bybit hack | Infra\_Neg | −21.0%-21.0\% | 4 |
| Infrastructure Positive (N=6) | | | | |
| 2020-05-11 | BTC Halving 2020 | Infra\_Pos | +3.2%+3.2\% | 3 |
| 2021-08-05 | EIP-1559 London | Infra\_Pos | +18.7%+18.7\% | 4 |
| 2022-09-15 | ETH Merge | Infra\_Pos | −5.8%-5.8\% | 4 |
| 2023-04-12 | Shanghai upgrade | Infra\_Pos | +12.4%+12.4\% | 4 |
| 2024-03-13 | Dencun upgrade | Infra\_Pos | +8.9%+8.9\% | 4 |
| 2024-04-20 | BTC Halving 2024 | Infra\_Pos | +15.6%+15.6\% | 4 |
| Regulatory Negative (N=7) | | | | |
| 2020-12-22 | SEC v. Ripple | Reg\_Neg | +36.6%+36.6\% | 3 |
| 2021-05-19 | China mining ban | Reg\_Neg | −49.6%-49.6\% | 4 |
| 2021-09-24 | China crypto ban | Reg\_Neg | −25.4%-25.4\% | 4 |
| 2022-01-05 | Kazakhstan shutdown | Reg\_Neg | −37.3%-37.3\% | 4 |
| 2023-06-05 | SEC v. Binance | Reg\_Neg | −9.5%-9.5\% | 4 |
| 2023-06-06 | SEC v. Coinbase | Reg\_Neg | −9.0%-9.0\% | 4 |
| 2023-11-21 | Binance/CZ $4.3B | Reg\_Neg | +28.3%+28.3\% | 4 |
| Regulatory Positive (N=8) | | | | |
| 2021-03-09 | US crypto exec. order | Reg\_Pos | +4.0%+4.0\% | 4 |
| 2021-06-09 | El Salvador BTC legal | Reg\_Pos | −56.0%-56.0\% | 4 |
| 2021-07-23 | Wyoming DAO law | Reg\_Pos | −5.0%-5.0\% | 4 |
| 2021-10-19 | BITO ETF launch | Reg\_Pos | −27.0%-27.0\% | 4 |
| 2023-06-15 | BlackRock ETF filing | Reg\_Pos | +18.0%+18.0\% | 4 |
| 2023-06-30 | MiCA final passage | Reg\_Pos | −2.0%-2.0\% | 4 |
| 2024-01-10 | Spot ETF approval | Reg\_Pos | −10.0%-10.0\% | 4 |
| 2025-02-25 | SEC drops Ripple | Reg\_Pos | −8.0%-8.0\% | 4 |

∗Insufficient estimation window data (pre-2019 prices unavailable); excluded from analysis.

Summary statistics: Mean CAR by category: Infra\_Neg =−7.9%=-7.9\% (N=8), Infra\_Pos =+8.8%=+8.8\% (N=6), Reg\_Neg =−9.4%=-9.4\% (N=7), Reg\_Pos =−14.3%=-14.3\% (N=8). Total analyzable events = 29; total event-asset observations = 118.

## Appendix C Reg\_Positive Events: Annotated List

Table [15](https://arxiv.org/html/2602.07046v1#A3.T15 "Table 15 ‣ Appendix C Reg_Positive Events: Annotated List ‣ Sentiment Without Structure Differential Market Responses to Infrastructure vs Regulatory Events in Cryptocurrency Markets") provides detailed annotation of the 8 Reg\_Positive events, including overlapping events and pre-event CARs that help explain the counterintuitive negative mean response.

Table 15: Reg\_Positive Events with Overlap Analysis

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Date | Event | CAR | Pre-CAR | Overlapping Events |
| 2021-03-09 | US crypto exec. order | +4%+4\% | −12%-12\% | None |
| 2021-06-09 | El Salvador BTC legal | −56%-56\% | −35%-35\% | China mining ban (05-19) |
| 2021-07-23 | Wyoming DAO law | −5%-5\% | −8%-8\% | None |
| 2021-10-19 | BITO ETF launch | −27%-27\% | −15%-15\% | China crypto ban (09-24) |
| 2023-06-15 | BlackRock ETF filing | +18%+18\% | −10%-10\% | SEC v. Binance (06-05) |
| 2023-06-30 | MiCA final passage | −2%-2\% | +5%+5\% | SEC v. Coinbase (06-06) |
| 2024-01-10 | Spot ETF approval | −10%-10\% | −22%-22\% | GBTC outflows |
| 2025-02-25 | SEC drops Ripple | −8%-8\% | −18%-18\% | Bybit hack (02-21) |
| Mean | | −14.3%-14.3\% | −25.8%-25.8\% | 4/8 overlap |
| Note: Pre-CAR = [−30,−1][-30,-1] window. CAR = [−5,+30][-5,+30] window. 50% overlap rate. | | | | |

Pattern: The strongly negative pre-event CAR (−25.8%-25.8\%) suggests substantial front-running—prices decline in anticipation, then the positive announcement fails to reverse the trend. Combined with 50% overlap with negative events, this explains the “positive news, negative returns” puzzle without requiring exotic behavioral mechanisms.

## Declarations

Funding. The author received no external funding for this research.

Conflicts of Interest. The author declares no conflicts of interest relevant to the content of this article.

Data Availability. All data and code are publicly available at <https://github.com/studiofarzulla/sentiment-without-structure>.

## References

* Aste (2019)

  Tomaso Aste.
  Cryptocurrency market structure: Connecting emotions and economics.
  *Digital Finance*, 1:5–21, 2019.
  doi: 10.1007/s42521-019-00005-w.
* Auer and Claessens (2018)

  Raphael Auer and Stijn Claessens.
  Regulating cryptocurrencies: Assessing market reactions.
  *BIS Quarterly Review*, pages 51–65, September 2018.
* Auer and Claessens (2020)

  Raphael Auer and Stijn Claessens.
  Cryptocurrency market reactions to regulatory news.
  Globalization Institute Working Paper No. 381, Federal Reserve Bank
  of Dallas, 2020.
* Badev and Watsky (2023)

  Anton Badev and Cy Watsky.
  Interconnected defi: Ripple effects from the terra collapse.
  FEDS Working Paper 2023-044, Federal Reserve Board, 2023.
* Boehmer et al. (1991)

  Ekkehart Boehmer, Jim Musumeci, and Annette B. Poulsen.
  Event-study methodology under conditions of event-induced variance.
  *Journal of Financial Economics*, 30(2):253–272, 1991.
  doi: 10.1016/0304-405X(91)90032-F.
* Borri and Shakhnov (2020)

  Nicola Borri and Kirill Shakhnov.
  Regulation spillovers across cryptocurrency markets.
  *Finance Research Letters*, 36, 2020.
  doi: 10.1016/j.frl.2019.101333.
* Cameron et al. (2008)

  A Colin Cameron, Jonah B Gelbach, and Douglas L Miller.
  Bootstrap-based improvements for inference with clustered errors.
  *Review of Economics and Statistics*, 90(3):414–427, 2008.
  doi: 10.1162/rest.90.3.414.
* Casini and McCloskey (2025)

  Alessandro Casini and Adam McCloskey.
  Identification, estimation and inference in high-frequency event
  study regressions.
  *CEIS Research Paper No. 608, Tor Vergata University*, 2025.
* Chokor and Alfieri (2021)

  Ahmad Chokor and Élise Alfieri.
  Long and short-term impacts of regulation in the cryptocurrency
  market.
  *Quarterly Review of Economics and Finance*, 81:157–173, 2021.
  doi: 10.1016/j.qref.2021.05.005.
* Conlon et al. (2024)

  Thomas Conlon, Shaen Corbet, and Yang Hou.
  Contagion effects of permissionless, worthless cryptocurrency tokens:
  Evidence from the collapse of ftx.
  *Journal of International Financial Markets, Institutions and
  Money*, 91:101940, 2024.
  doi: 10.1016/j.intfin.2024.101940.
* Cumming et al. (2025)

  Douglas J. Cumming, Johannes Fuchs, and Paul P. Momtaz.
  Market reactions to cryptocurrency regulation: Risk, return and the
  role of enforcement quality.
  *British Journal of Management*, 2025.
  doi: 10.1111/1467-8551.70002.
* Esparcia et al. (2024)

  Carlos Esparcia, Ana Escribano, and Francisco Jareño.
  Assessing the crypto market stability after the ftx collapse: A study
  of high frequency volatility and connectedness.
  *International Review of Financial Analysis*, 94, 2024.
  doi: 10.1016/j.irfa.2024.103287.
* Farzulla (2025)

  Murad Farzulla.
  Infrastructure vs regulatory shocks: Asymmetric volatility response
  in cryptocurrency markets.
  *Research Square Preprint*, 2025.
  doi: 10.21203/rs.3.rs-8323026/v1.
  Under review at Digital Finance.
* Goldsmith-Pinkham and Lyu (2025)

  Paul Goldsmith-Pinkham and Tianshu Lyu.
  Causal inference in financial event studies.
  *Working Paper, Yale University*, 2025.
* Ibragimov and Müller (2010)

  Rustam Ibragimov and Ulrich K Müller.
  t-statistic based correlation and heterogeneity robust inference.
  *Journal of Business & Economic Statistics*, 28(4):453–468, 2010.
  doi: 10.1198/jbes.2009.08046.
* Jalan and Matkovskyy (2023)

  Akanksha Jalan and Roman Matkovskyy.
  Systemic risks in the cryptocurrency market: Evidence from the ftx
  collapse.
  *Finance Research Letters*, 54, 2023.
  doi: 10.1016/j.frl.2023.103670.
* Knight (1921)

  Frank H Knight.
  *Risk, Uncertainty and Profit*.
  Houghton Mifflin, Boston, 1921.
* Koenraadt and Leung (2024)

  Jeroen Koenraadt and Ester Leung.
  Investor reactions to crypto token regulation.
  *European Accounting Review*, 33(2):367–397, 2024.
  doi: 10.1080/09638180.2022.2090399.
* Kolari and Pynnonen (2010)

  James W Kolari and Seppo Pynnonen.
  Event study testing with cross-sectional correlation of abnormal
  returns.
  *Review of Financial Studies*, 23(11):3996–4025, 2010.
  doi: 10.1093/rfs/hhq072.
* Kothari and Warner (2007)

  S.P. Kothari and Jerold B. Warner.
  Econometrics of event studies.
  In *Handbook of Empirical Corporate Finance*, pages 3–36.
  Elsevier, 2007.
  doi: 10.1016/B978-0-444-53265-7.50015-9.
* Liu et al. (2023)

  Jiageng Liu, Igor Makarov, and Antoinette Schoar.
  Anatomy of a run: The terra luna crash.
  NBER Working Paper 31160, National Bureau of Economic Research, 2023.
* Lucey et al. (2022)

  Brian M Lucey, Samuel A Vigne, Larisa Yarovaya, and Yizhi Wang.
  The cryptocurrency uncertainty index.
  *Finance Research Letters*, 45:102147, 2022.
  doi: 10.1016/j.frl.2021.102147.
* Lyócsa et al. (2020)

  Štefan Lyócsa, Peter Molnár, Tomáš Plíhal, and
  Mária Širaňová.
  Impact of macroeconomic news, regulation and hacking exchange markets
  on the volatility of bitcoin.
  *Journal of Economic Dynamics and Control*, 119, 2020.
  doi: 10.1016/j.jedc.2020.103980.
* MacKinlay (1997)

  A Craig MacKinlay.
  Event studies in economics and finance.
  *Journal of Economic Literature*, 35(1):13–39, 1997.
  doi: 10.2307/2729691.
* MacKinnon et al. (2023)

  James G MacKinnon, Morten Ørregaard Nielsen, and Matthew D Webb.
  Cluster-robust inference: A guide to empirical practice.
  *Journal of Econometrics*, 232(2):272–299,
  2023.
  doi: 10.1016/j.jeconom.2022.04.001.
* Makarov and Schoar (2020)

  Igor Makarov and Antoinette Schoar.
  Trading and arbitrage in cryptocurrency markets.
  *Journal of Financial Economics*, 135(2):293–319, 2020.
  doi: 10.1016/j.jfineco.2019.07.001.
* Ni et al. (2025)

  Xinwen Ni, Wolfgang Karl Härdle, and Taojun Xie.
  A machine learning based regulatory risk index for cryptocurrencies.
  *Computational Statistics*, 40:3563–3583, 2025.
  doi: 10.1007/s00180-025-01629-y.
* Petersen (2009)

  Mitchell A. Petersen.
  Estimating standard errors in finance panel data sets: Comparing
  approaches.
  *The Review of Financial Studies*, 22(1):435–480, 2009.
  doi: 10.1093/rfs/hhn053.
* Saggu et al. (2025)

  Aman Saggu, Lennart Ante, and Kaja Kopiec.
  Uncertain regulations, definite impacts: The impact of the US
  securities and exchange commission’s regulatory interventions on crypto
  assets.
  *Finance Research Letters*, 72:106413, 2025.
  doi: 10.1016/j.frl.2024.106413.
* Shanaev et al. (2020)

  Savva Shanaev, Satish Sharma, Binam Ghimire, and Arina Shuraeva.
  Taming the blockchain beast? regulatory implications for the
  cryptocurrency market.
  *Research in International Business and Finance*, 51, 2020.
  doi: 10.1016/j.ribaf.2019.101080.
* Trimborn and Härdle (2018)

  Simon Trimborn and Wolfgang Karl Härdle.
  CRIX an index for cryptocurrencies.
  *Journal of Empirical Finance*, 49:107–122, 2018.
  doi: 10.1016/j.jempfin.2018.08.004.