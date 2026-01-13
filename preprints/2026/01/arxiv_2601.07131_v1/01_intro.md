---
authors:
- Sungwoo Kang
doc_id: arxiv:2601.07131v1
family_id: arxiv:2601.07131
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor
  Flow Prediction'
url_abs: http://arxiv.org/abs/2601.07131v1
url_html: https://arxiv.org/html/2601.07131v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sungwoo Kang
  
Department of Electrical and Computer Engineering
  
Korea University, Seoul 02841, Republic of Korea
  
krml919@korea.ac.kr

(January 9, 2026)

###### Abstract

The application of machine learning to financial prediction has accelerated dramatically, yet the conditions under which complex models outperform simple alternatives remain poorly understood. This paper investigates whether advanced signal processing and deep learning techniques can extract predictive value from investor order flows beyond what simple feature engineering achieves. Using a comprehensive dataset of 2.79 million observations spanning 2,439 Korean equities from 2020–2024, we apply three methodologies: Independent Component Analysis (ICA) to recover latent market drivers, Wavelet Coherence analysis to characterize multi-scale correlation structure, and Long Short-Term Memory (LSTM) networks with attention mechanisms for non-linear prediction. Our results reveal a striking finding: a parsimonious linear model using market capitalization-normalized flows (“Matched Filter” preprocessing) achieves a Sharpe ratio of 1.30 and cumulative return of 272.6%, while the full ICA-Wavelet-LSTM pipeline generates a Sharpe ratio of only 0.07 with a cumulative return of −5.1%-5.1\%. The raw LSTM model collapsed to predicting the unconditional mean, achieving a hit rate of 47.5%—worse than random. We conclude that in low signal-to-noise financial environments, domain-specific feature engineering yields substantially higher marginal returns than algorithmic complexity. These findings establish important boundary conditions for the application of deep learning to financial prediction.

Keywords: Machine Learning, Deep Learning, Investor Flows, Feature Engineering, Order Flow, LSTM, Independent Component Analysis, Wavelet Analysis, Korean Stock Market

JEL Classification: G11, G12, G14, C45, C58

## 1 Introduction

The application of machine learning (ML) to financial markets has experienced explosive growth over the past decade. Practitioners and academics alike have embraced increasingly sophisticated algorithms—from random forests and gradient boosting to deep neural networks and transformer architectures—in pursuit of predictive alpha. This “complexity arms race” is predicated on the assumption that financial markets contain non-linear patterns too subtle for traditional linear models to detect, and that sufficiently powerful algorithms can learn these patterns from historical data.

Yet financial data differs fundamentally from the domains where deep learning has achieved its most celebrated successes. Unlike image classification, where signal-to-noise ratios (SNR) approach unity and patterns remain stable across time, financial returns exhibit SNR on the order of 1% or less, with statistical relationships that shift across market regimes (López de Prado, [2018](https://arxiv.org/html/2601.07131v1#bib.bib21)). The efficient market hypothesis suggests that any predictable pattern will be arbitraged away, leaving only noise for subsequent learners (Fama, [1970](https://arxiv.org/html/2601.07131v1#bib.bib9)). Under such conditions, the benefits of model complexity may be illusory—or worse, counterproductive through overfitting.

This paper directly confronts the question: Under what conditions do complex machine learning models outperform simple alternatives for financial prediction? We investigate this question in the context of investor order flow prediction, a domain where heterogeneous trading behavior across investor types creates potential for information extraction (Kyle, [1985](https://arxiv.org/html/2601.07131v1#bib.bib20); Hasbrouck, [1991](https://arxiv.org/html/2601.07131v1#bib.bib16)).

### 1.1 The Research Setting

We study the Korean equity market (KOSPI and KOSDAQ), which provides a uniquely rich setting for several reasons. First, the Korea Exchange (KRX) mandates disclosure of trading activity disaggregated by investor type—foreign institutions, domestic institutions, and individual (retail) investors—enabling direct observation of order flow heterogeneity. Second, these investor types exhibit markedly different trading behaviors: foreign investors are typically characterized as “smart money” with superior information (Grinblatt and Keloharju, [2000](https://arxiv.org/html/2601.07131v1#bib.bib13)), domestic institutions often follow benchmark-constrained mandates, and retail investors display behavioral biases including herding and disposition effects (Barber et al., [2009](https://arxiv.org/html/2601.07131v1#bib.bib5)). Third, the market is large and liquid enough to support meaningful out-of-sample testing, yet distinct enough from US markets to provide independent validation of methodological conclusions.

### 1.2 Methodological Approach

We construct a comprehensive pipeline that applies three distinct advanced techniques:

1. 1.

   Independent Component Analysis (ICA): We apply blind source separation to decompose the multivariate flow matrix into statistically independent latent components, hypothesizing that these will correspond to economically interpretable factors such as “Macro Risk,” “Domestic Sentiment,” and “Liquidity Provision.”
2. 2.

   Wavelet Coherence Analysis: We characterize the multi-scale correlation structure between investor types, testing whether institutional and foreign flows exhibit high coherence at fundamental (weekly) frequencies while decoupling at higher frequencies.
3. 3.

   LSTM with Attention: We train deep recurrent networks on sequences of normalized flows, employing attention mechanisms to identify which temporal lags and investor types carry predictive information.

Critically, all methods operate on flows that have been preprocessed using market capitalization normalization—a transformation we term the “Matched Filter” approach, borrowing terminology from signal processing. This normalization divides net buying by market capitalization, creating a scale-invariant measure of trading intensity that is comparable across the market cap spectrum.

### 1.3 Preview of Findings

Our results challenge the prevailing enthusiasm for complex models in finance. We find:

* •

  ICA Factor Instability: While ICA successfully extracts statistically independent components, their economic interpretation is unstable across market regimes. The primary component alternates between “Market Beta,” “Sentiment,” and “Fundamentals” interpretations across subperiods, undermining out-of-sample reliability.
* •

  Multi-Scale Coherence: Contrary to the hypothesis of intraday decoupling, investor flows show relatively uniform coherence across scales, with coherence increasing monotonically at longer horizons (0.26 at 2–4 days to 0.74 at 16–32 days).
* •

  LSTM Collapse: The LSTM model converges to predicting the unconditional mean of returns, achieving a hit rate of 47.5% (worse than a coin flip) and an information ratio of −1.36-1.36. The attention weights are uniformly distributed across lags, indicating failure to learn meaningful temporal patterns.
* •

  Simplicity Wins: A simple momentum strategy using market cap-normalized flows in a linear ranking achieves a Sharpe ratio of 1.30 and cumulative return of 272.6%, massively outperforming the ICA-based strategy (Sharpe 0.07, return −5.1%-5.1\%).

### 1.4 Contributions

This paper makes three contributions to the literature:

First, we provide rigorous empirical evidence establishing boundary conditions for the application of machine learning to financial prediction. The failure of LSTM and ICA pipelines is not due to implementation error—we verify numerical stability and hyperparameter optimization—but rather reflects a fundamental mismatch between the SNR of financial data and the data requirements of complex models.

Second, we demonstrate that the marginal contribution of sophisticated algorithms is dominated by the choice of feature representation. The “Matched Filter” normalization, grounded in market microstructure theory, captures virtually all exploitable signal. Additional model complexity destroys rather than enhances information.

Third, we contribute methodologically by documenting failure modes of ML in finance that may guide future research. The LSTM collapse to predicting the mean, the regime-dependence of ICA factors, and the monotonic coherence pattern all provide diagnostic signatures that researchers can use to assess when complex methods are inappropriate.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2601.07131v1#S2 "2 Literature Review ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") reviews related literature. Section [3](https://arxiv.org/html/2601.07131v1#S3 "3 Methodology ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") describes our data and methods. Section [4](https://arxiv.org/html/2601.07131v1#S4 "4 Empirical Results ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") presents empirical results. Section [5](https://arxiv.org/html/2601.07131v1#S5 "5 Discussion ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") discusses implications, and Section [6](https://arxiv.org/html/2601.07131v1#S6 "6 Conclusion ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") concludes.

## 2 Literature Review

Our study sits at the intersection of three literatures: market microstructure, machine learning in finance, and behavioral heterogeneity across investor types.

### 2.1 Order Flow and Price Discovery

The foundational insight that order flow contains information about future prices dates to Kyle ([1985](https://arxiv.org/html/2601.07131v1#bib.bib20)), who models a strategic informed trader whose trades reveal private information through their market impact. Glosten and Milgrom ([1985](https://arxiv.org/html/2601.07131v1#bib.bib11)) extend this to competitive market making, showing how spreads arise from adverse selection. Empirically, Hasbrouck ([1991](https://arxiv.org/html/2601.07131v1#bib.bib16)) develops the Vector Autoregression (VAR) framework for measuring information content of trades, while Amihud ([2002](https://arxiv.org/html/2601.07131v1#bib.bib1)) documents that illiquidity—closely related to order flow—predicts cross-sectional returns.

More recent work has examined the predictive content of disaggregated flows. Chordia et al. ([2002](https://arxiv.org/html/2601.07131v1#bib.bib8)) find that aggregate order imbalances predict short-horizon returns, while Barber et al. ([2009](https://arxiv.org/html/2601.07131v1#bib.bib5)) document systematic patterns in retail order flow that create predictable price pressure. In the Korean market specifically, Choe et al. ([2005](https://arxiv.org/html/2601.07131v1#bib.bib7)) provide evidence that domestic investors may possess an informational advantage, finding that foreign investors pay more for purchases and receive less for sales.

### 2.2 Machine Learning in Finance

The application of ML to asset pricing has accelerated following Gu et al. ([2020](https://arxiv.org/html/2601.07131v1#bib.bib14)), who demonstrate that ensemble methods and neural networks outperform linear models in the US cross-section. This has spurred extensive research into deep learning for return prediction (Feng et al., [2020](https://arxiv.org/html/2601.07131v1#bib.bib10); Chen et al., [2024](https://arxiv.org/html/2601.07131v1#bib.bib6)), portfolio optimization (Ban et al., [2018](https://arxiv.org/html/2601.07131v1#bib.bib3)), and risk management (Sirignano and Cont, [2019](https://arxiv.org/html/2601.07131v1#bib.bib24)).

However, a growing literature questions the reliability of these findings. Arnott et al. ([2019](https://arxiv.org/html/2601.07131v1#bib.bib2)) argue that many published ML strategies suffer from overfitting and fail out-of-sample. Harvey et al. ([2016](https://arxiv.org/html/2601.07131v1#bib.bib15)) and McLean and Pontiff ([2016](https://arxiv.org/html/2601.07131v1#bib.bib22)) document that anomaly returns decay substantially after publication, suggesting that in-sample performance may not persist. López de Prado ([2018](https://arxiv.org/html/2601.07131v1#bib.bib21)) emphasizes the non-stationarity of financial data and the dangers of applying techniques developed for stationary domains.

### 2.3 Investor Heterogeneity

The behavioral finance literature documents systematic differences across investor types. Barber and Odean ([2000](https://arxiv.org/html/2601.07131v1#bib.bib4)) find that individual investors trade excessively and underperform, while Grinblatt and Keloharju ([2000](https://arxiv.org/html/2601.07131v1#bib.bib13)) show that Finnish investors exhibit the disposition effect. Institutional investors display distinct patterns: Sias ([2004](https://arxiv.org/html/2601.07131v1#bib.bib23)) documents institutional herding, and Griffin et al. ([2003](https://arxiv.org/html/2601.07131v1#bib.bib12)) finds that momentum strategies are partially attributable to institutional buying.

In the Korean context, Kim and Wei ([2002](https://arxiv.org/html/2601.07131v1#bib.bib19)) and Jeon and Moffett ([2010](https://arxiv.org/html/2601.07131v1#bib.bib18)) examine the distinct roles of foreign versus domestic investors in price discovery. The KRX’s transparency requirements make Korea particularly suitable for studying investor heterogeneity.

### 2.4 Our Contribution

We bridge these literatures by testing whether advanced signal processing (ICA, Wavelets) and deep learning (LSTM) can extract additional predictive value from investor flows beyond simple normalization. Our finding that complexity fails establishes an important negative result: the conditions for ML success may be more restrictive in finance than previously appreciated.

## 3 Methodology

### 3.1 Data Description

Our dataset comprises daily trading records for all common stocks listed on the Korea Exchange (KOSPI and KOSDAQ) from January 2, 2020 through December 27, 2024. The data include:

* •

  Price and volume: Daily open, high, low, close prices and trading volume
* •

  Investor flows: Net buying (in KRW) by three investor categories: Foreign, Institutional (domestic), and Individual (retail)
* •

  Market capitalization: End-of-day market cap for normalization

Table [1](https://arxiv.org/html/2601.07131v1#S3.T1 "Table 1 ‣ 3.1 Data Description ‣ 3 Methodology ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") presents summary statistics.

Table 1: Data Summary Statistics

| Statistic | Value |
| --- | --- |
| Total observations | 2,788,940 |
| Unique tickers | 2,439 |
| Date range | 2020-01-02 to 2024-12-30 |
| Average daily observations | 2,266 |
| Investor categories | 3 (Foreign, Institutional, Individual) |

### 3.2 Market Capitalization Normalization: The “Matched Filter”

Raw order flow data presents a fundamental scaling problem: a 1 billion KRW purchase represents vastly different information content for a 100 billion KRW small-cap versus a 50 trillion KRW mega-cap. Following the signal processing concept of matched filtering, we normalize flows to create a scale-invariant measure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Si,tg=NetBuyi,tgMarketCapi,tS\_{i,t}^{g}=\frac{\text{NetBuy}\_{i,t}^{g}}{\text{MarketCap}\_{i,t}} |  | (1) |

where Si,tgS\_{i,t}^{g} is the normalized flow for stock ii at time tt by investor group g∈{Foreign,Institutional,Individual}g\in\{\text{Foreign},\text{Institutional},\text{Individual}\}.

This normalization has several desirable properties:

1. 1.

   Scale invariance: Flows are comparable across the market cap spectrum
2. 2.

   Economic interpretation: SS approximates the fraction of outstanding shares traded, relating directly to price impact theory (Kyle, [1985](https://arxiv.org/html/2601.07131v1#bib.bib20))
3. 3.

   Stationarity: Normalization removes the market cap growth trend that would otherwise induce non-stationarity

### 3.3 Independent Component Analysis (ICA)

We hypothesize that observed investor flows are mixtures of latent market drivers:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐗t=𝐀⋅𝐒t+ϵt\mathbf{X}\_{t}=\mathbf{A}\cdot\mathbf{S}\_{t}+\boldsymbol{\epsilon}\_{t} |  | (2) |

where 𝐗t=[StForeign,StInst,StInd]T\mathbf{X}\_{t}=[S\_{t}^{\text{Foreign}},S\_{t}^{\text{Inst}},S\_{t}^{\text{Ind}}]^{T} is the vector of observed market-aggregated flows, 𝐀\mathbf{A} is a 3×33\times 3 mixing matrix, 𝐒t\mathbf{S}\_{t} contains independent latent components, and ϵt\boldsymbol{\epsilon}\_{t} is noise.

We apply FastICA with negentropy maximization (Hyvärinen and Oja, [2000](https://arxiv.org/html/2601.07131v1#bib.bib17)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝐰⁡J​(𝐰T​𝐙t)=[𝔼​[G​(𝐰T​𝐙t)]−𝔼​[G​(ν)]]2\max\_{\mathbf{w}}J(\mathbf{w}^{T}\mathbf{Z}\_{t})=\left[\mathbb{E}[G(\mathbf{w}^{T}\mathbf{Z}\_{t})]-\mathbb{E}[G(\nu)]\right]^{2} |  | (3) |

where G​(u)=log⁡cosh⁡(u)G(u)=\log\cosh(u) is the negentropy function, 𝐙t\mathbf{Z}\_{t} is whitened data, and ν∼N​(0,1)\nu\sim N(0,1).

Component Interpretation: We correlate each extracted component (IC1, IC2, IC3) with external factors to assign economic meaning:

* •

  USD/KRW exchange rate (macro risk)
* •

  CBOE VIX (global risk appetite)
* •

  KOSPI index returns (market beta)
* •

  Earnings proxies (fundamental value)
* •

  Bid-ask spreads (liquidity/microstructure)

### 3.4 Wavelet Coherence Analysis

To characterize multi-scale correlation structure, we compute wavelet coherence between investor type pairs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γA​B2​(j)=|WA​(j)⋅WB∗​(j)|2|WA​(j)|2​|WB​(j)|2\gamma^{2}\_{AB}(j)=\frac{|W\_{A}(j)\cdot W\_{B}^{\*}(j)|^{2}}{|W\_{A}(j)|^{2}|W\_{B}(j)|^{2}} |  | (4) |

where WA​(j)W\_{A}(j) and WB​(j)W\_{B}(j) are the continuous wavelet transforms of flows AA and BB at scale jj, and ∗ denotes complex conjugate.

We use the Morlet wavelet and examine four scale bands corresponding to:

* •

  Scale 1: 2–4 trading days (high frequency)
* •

  Scale 2: 4–8 trading days (weekly)
* •

  Scale 3: 8–16 trading days (bi-weekly)
* •

  Scale 4: 16–32 trading days (monthly)

Hypothesis: Foreign and Institutional flows should exhibit high coherence at weekly scales (fundamental-driven) but low coherence at high frequencies (different execution strategies).

### 3.5 LSTM with Attention Mechanism

We model return prediction as a sequence learning problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t+1=fθ​(𝐗i,t−K:t)+ϵt+1r\_{i,t+1}=f\_{\theta}(\mathbf{X}\_{i,t-K:t})+\epsilon\_{t+1} |  | (5) |

where 𝐗i,t−K:t\mathbf{X}\_{i,t-K:t} is the sequence of normalized flows over the past K=10K=10 trading days.

Architecture:

* •

  Input: (K×3)(K\times 3) tensor of normalized flows
* •

  Layer 1: LSTM with 64 units, return sequences
* •

  Dropout: 20%
* •

  Layer 2: LSTM with 32 units
* •

  Dropout: 20%
* •

  Attention: Multi-head attention (3 heads) to weight temporal positions
* •

  Output: Dense layer predicting next-day return

Training:

* •

  Loss function: Mean Squared Error (MSE)
* •

  Optimizer: Adam with learning rate 10−310^{-3}
* •

  Regularization: Dropout, early stopping (patience = 10)
* •

  Split: 80% train, 10% validation, 10% test

Baselines:

* •

  Ridge Regression: L2L\_{2}-regularized linear model
* •

  LASSO: L1L\_{1}-regularized for feature selection

### 3.6 Strategy Evaluation

We evaluate predictive performance through both statistical and economic metrics:

Statistical:

* •

  Root Mean Squared Error (RMSE)
* •

  Pearson correlation with realized returns
* •

  Hit rate (directional accuracy)
* •

  Information Ratio: IR=r¯signalσrsignal\text{IR}=\frac{\bar{r}\_{\text{signal}}}{\sigma\_{r\_{\text{signal}}}}

Economic:

* •

  Sharpe Ratio (annualized, net of 10bp transaction costs)
* •

  Cumulative Return
* •

  Maximum Drawdown
* •

  Calmar Ratio: Return / Max Drawdown

We implement two trading strategies:

1. 1.

   Simple Momentum: Rank stocks daily by normalized flow, go long top decile, short bottom decile
2. 2.

   ICA Macro Factor: Trade based on extracted IC1 component signals

## 4 Empirical Results

### 4.1 ICA: The Elusive Latent Factors

Table [2](https://arxiv.org/html/2601.07131v1#S4.T2 "Table 2 ‣ 4.1 ICA: The Elusive Latent Factors ‣ 4 Empirical Results ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") presents the interpretation of extracted independent components based on their correlations with external factors.

Table 2: ICA Component Interpretation via External Factor Correlations

| Component | Observed Interpretation | Top Factor | Correlation | Hypothesized |
| --- | --- | --- | --- | --- |
| IC1 | Market Beta | kospi\_return | 0.368\*\*\* | Macro Risk |
| IC2 | Fundamentals | earnings\_proxy | 0.678\*\*\* | Sentiment |
| IC3 | Mixed / Weak | earnings\_proxy\_roll | 0.184\*\*\* | Liquidity |

* •

  Note: \*\*\* p<0.001p<0.001. The observed factors diverge from the hypothesized Macro/Sentiment/Liquidity structure.
* •

  IC1 correlates with Market Return rather than VIX or USD/KRW as predicted.

The results contradict our hypothesis that ICA would recover distinct Macro Risk, Sentiment, and Liquidity factors:

* •

  IC1 was hypothesized to correlate with USD/KRW (r=0.4r=0.4–0.70.7) and VIX (r=0.3r=0.3–0.60.6), capturing global macro risk. Instead, it correlates most strongly with contemporaneous KOSPI returns (r=0.37r=0.37), with near-zero correlation to USD/KRW (r=−0.073r=-0.073) and VIX (r=−0.066r=-0.066).
* •

  IC2 captures fundamentals through earnings proxies (r=0.68r=0.68), which is closer to the hypothesized Sentiment factor but not identical.
* •

  IC3 shows only weak correlations with any external factor (max r=0.18r=0.18), failing to capture the hypothesized Liquidity Provision dynamics.

Regime Instability: More concerning for practical application, the component interpretations are unstable across subperiods, as shown in Table [3](https://arxiv.org/html/2601.07131v1#S4.T3 "Table 3 ‣ 4.1 ICA: The Elusive Latent Factors ‣ 4 Empirical Results ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction").

Table 3: Robustness Check: Subperiod Stability of Latent Factors

| Period | Event | IC1 Interpretation | Correlation (Top Factor) |
| --- | --- | --- | --- |
| 2020 | COVID Crisis | Market Beta | 0.57 (kospi\_return) |
| 2021 | Recovery | Unknown | −0.50-0.50 (earnings\_proxy) |
| 2022 | Rate Hikes | Market Beta | 0.69 (kospi\_return) |
| 2023 | Calm | Market Beta | 0.73 (kospi\_return) |
| 2024 | Recent | Market Beta | −0.61-0.61 (kospi\_return) |

* •

  Note: The interpretation of IC1 shifts across regimes, with sign reversals indicating rotational ambiguity.

The sign reversals between positive and negative correlations indicate that ICA’s rotational ambiguity creates inconsistent factors across time—a fatal flaw for out-of-sample prediction. A strategy trained on 2020–2022 data would apply reversed signals in 2024.

![Refer to caption](x1.png)


(a) Extracted Independent Components

![Refer to caption](x2.png)


(b) ICA Mixing Matrix Heatmap

Figure 1: Independent Component Analysis (ICA) of Korean investor flows. Figure (a) shows the time-series of the three extracted components, while (b) illustrates the loading of each investor type onto these components.

![Refer to caption](x3.png)


Figure 2: Correlations between ICA components and external market factors (KOSPI returns, VIX, USD/KRW, etc.). IC1 shows unexpectedly high correlation with market returns rather than macro factors.

### 4.2 Wavelet Coherence: Multi-Scale Correlation Structure

Table [4](https://arxiv.org/html/2601.07131v1#S4.T4 "Table 4 ‣ 4.2 Wavelet Coherence: Multi-Scale Correlation Structure ‣ 4 Empirical Results ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") presents wavelet coherence between investor pairs across scale bands.

Table 4: Wavelet Coherence by Scale Band and Investor Pair

| Investor Pair | Scale 1 (2–4d) | Scale 2 (4–8d) | Scale 3 (8–16d) | Scale 4 (16–32d) |
| --- | --- | --- | --- | --- |
| Foreign vs Inst. | 0.261 | 0.262 | 0.302 | 0.383 |
| Foreign vs Indiv. | 0.627 | 0.632 | 0.550 | 0.532 |
| Inst. vs Indiv. | 0.738 | 0.635 | 0.659 | 0.570 |

* •

  Note: Values represent mean coherence (0–1).
* •

  Foreign-Institutional coherence increases with scale, consistent with fundamental alignment at longer horizons.
* •

  High coherence between Institutional and Individual flows at short scales suggests liquidity provision dynamics.

The results partially support the multi-scale hypothesis:

* •

  Foreign-Institutional: Coherence increases monotonically with scale (0.26 at 2–4 days to 0.38 at 16–32 days), consistent with fundamental alignment emerging at longer horizons.
* •

  Contrary to hypothesis: We expected low coherence at high frequencies and high coherence at weekly scales. Instead, we observe relatively uniform coherence with a gradual increase—no sharp transition at any particular frequency.
* •

  Unexpected pattern: Individual-Institutional coherence is highest at the shortest scale (0.74), declining at longer horizons. This may reflect institutional liquidity provision to retail flow, a dynamic opposite to our hypothesis.

The absence of distinct “islands” of high coherence at specific frequencies suggests that investor types respond to overlapping information sets across all timescales, rather than specialized processing at particular frequencies.

![Refer to caption](x4.png)


Figure 3: Wavelet Coherence between Foreign and Institutional investor flows. The coherence increases monotonically with scale, indicating stronger synchronization at fundamental rather than high-frequency horizons.

![Refer to caption](x5.png)


Figure 4: Multi-scale clustering of investor flow correlations. The results show a clear separation between high-frequency noise and lower-frequency fundamental alignment.

### 4.3 LSTM: Deep Learning Collapse

Table [5](https://arxiv.org/html/2601.07131v1#S4.T5 "Table 5 ‣ 4.3 LSTM: Deep Learning Collapse ‣ 4 Empirical Results ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") compares model performance across configurations.

Table 5: Model Performance Comparison: Simplicity vs Complexity

| Model Configuration | RMSE | Correlation | Hit Rate | Info Ratio (IR) |
| --- | --- | --- | --- | --- |
| Raw Data + LSTM | 0.0158 | −0.066-0.066 | 47.5% | −1.36-1.36 |
| Normalized (SMC{}\_{\text{MC}}) + Linear | 0.0157 | 0.121 | 47.5% | 1.53 |
| Full Pipeline (ICA+Coh+LSTM) | 0.0157 | 0.029 | 47.9% | 0.68 |

* •

  Note: The linear model with Matched Filter normalization significantly outperforms all alternatives.
* •

  Raw LSTM achieves negative correlation, indicating destructive processing.
* •

  The full pipeline improves over Raw LSTM but underperforms the simple linear baseline.

The LSTM results reveal a complete failure of deep learning:

* •

  Model collapse: The LSTM converged to predicting the unconditional mean of returns, with prediction standard deviation of exactly zero. This is the rational loss-minimizing strategy when signal-to-noise ratio is insufficient for pattern learning.
* •

  Attention failure: The attention weights are uniformly distributed (0.10 across all 10 lags), indicating the model failed to identify any temporal position as more informative than others.
* •

  Hit rate: 47.5% directional accuracy is worse than random guessing (50%), as the model’s constant prediction of near-zero returns is wrong whenever the market moves.
* •

  Negative transfer: Raw LSTM achieves negative correlation (−0.066-0.066), meaning its predictions are anti-correlated with reality. The complex model learned to destroy rather than enhance signal.

Diagnosis: The target variable (next-day returns) has mean 0.028% and standard deviation 3.49%, yielding an SNR of approximately 0.8%. This is far below the threshold at which neural networks can reliably learn patterns. With such low SNR, the optimal MSE-minimizing strategy is to predict zero (or the mean), which is exactly what the LSTM learned.

![Refer to caption](x6.png)


Figure 5: LSTM Prediction Performance. The scatter plot of predicted vs realized returns show a horizontal line at the mean, illustrating the model’s collapse to predicting the unconditional mean due to low SNR.

![Refer to caption](x7.png)


Figure 6: Multi-head Attention Weights across 10-day lookback period. The uniform distribution of weights confirms the model’s failure to identify any specific temporal patterns in the flow data.

### 4.4 The Triumph of Simplicity: Strategy Comparison

Table [6](https://arxiv.org/html/2601.07131v1#S4.T6 "Table 6 ‣ 4.4 The Triumph of Simplicity: Strategy Comparison ‣ 4 Empirical Results ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction") compares the economic performance of trading strategies.

Table 6: Strategy Performance Comparison (Annualized)

| Strategy | Total Return | Sharpe (Net) | Max Drawdown | Hit Rate |
| --- | --- | --- | --- | --- |
| Simple Momentum (Linear) | 272.6% | 1.30 | −19.1%-19.1\% | 56.5% |
| ICA Macro Factor (ML) | −5.1%-5.1\% | 0.07 | −48.9%-48.9\% | 51.1% |

* •

  Note: “Simple Momentum” uses Matched Filter normalized flows in a linear ranking.
* •

  “ICA Macro Factor” trades the extracted latent component (IC1).
* •

  Net Sharpe accounts for 10bp round-trip transaction costs.

The performance differential is striking:

* •

  Simple Momentum achieves a Sharpe ratio of 1.30 after transaction costs, with cumulative return of 272.6% over 5 years (annualized ∼\sim30%). Maximum drawdown of 19.1% yields a Calmar ratio of 1.6.
* •

  ICA Macro Factor generates a Sharpe of only 0.07—essentially zero risk-adjusted return—with a catastrophic 48.9% maximum drawdown and negative cumulative return.
* •

  The gap: The simple strategy outperforms by a factor of 18.6×\times on Sharpe ratio and delivers 278 percentage points higher cumulative return.

This result demonstrates that the alpha resides entirely in the normalization, not in the factor extraction. The “Matched Filter” preprocessing (Equation [1](https://arxiv.org/html/2601.07131v1#S3.E1 "In 3.2 Market Capitalization Normalization: The “Matched Filter” ‣ 3 Methodology ‣ The Limits of Complexity: Why Feature Engineering Beats Deep Learning in Investor Flow Prediction")) transforms raw order flow into a predictive signal. Adding ICA, wavelet features, and LSTM layers not only fails to improve performance—it actively destroys the signal.

![Refer to caption](x8.png)


Figure 7: Cumulative Returns of Simple Momentum vs ICA-based strategies. The linear strategy using normalized flows achieves 272.6% cumulative return, while the complex ICA-LSTM pipeline fails to generate positive alpha.

![Refer to caption](x9.png)


Figure 8: Robustness analysis of the Simple Momentum strategy across subperiods and market cap deciles. The strategy remains consistently profitable across various market regimes.

### 4.5 Summary of Empirical Findings

Table 7: Summary: Hypotheses vs Empirical Reality

| Hypothesis | Prediction | Finding | Verdict |
| --- | --- | --- | --- |
| ICA recovers Macro/Sentiment/ Liquidity factors | Distinct, stable components | Components are Market Beta, unstable across regimes | Not Supported |
| Coherence peaks at weekly scales | High coherence at 5–10 days, low at high frequency | Monotonic increase with scale, no peak | Partially Supported |
| LSTM beats linear models by 15–25% | Hit rate >60%>60\%, Sharpe >1.5>1.5 | Hit rate 47.5%, Sharpe N/A (collapse) | Not Supported |
| ML pipeline generates alpha | Sharpe >1.0>1.0 | Sharpe 0.07 | Not Supported |
| Normalization matters | Improved signal quality | Sharpe 1.30 (linear + normalized) | Strongly Supported |

## 5 Discussion

### 5.1 Why Normalization Works

The striking success of simple market cap normalization—versus the failure of sophisticated ML—demands explanation. We propose several mechanisms:

1. Scale Invariance and Comparability: Raw order flow data conflates signal with size. A 10 billion KRW purchase in a 50 billion KRW stock represents concentrated buying (20% of market cap), while the same purchase in a 50 trillion KRW stock is trivial (0.02%). By normalizing, we create a universal “buying pressure” measure comparable across the entire market cap spectrum. This enables cross-sectional momentum strategies that would be impossible with raw data.

2. Theoretical Grounding: The normalization aligns with Kyle ([1985](https://arxiv.org/html/2601.07131v1#bib.bib20))’s model, where price impact is proportional to order size relative to market depth, which scales with market capitalization. Our SM​CS\_{MC} measure approximates the permanent price impact of flow, making it economically meaningful.

3. Noise Reduction: Market cap normalization implicitly controls for the correlation between size and trading volume. Large-cap stocks have higher absolute trading volume but similar turnover rates; normalization removes this spurious variation.

4. Sufficient Statistic: The normalized flow may be a sufficient statistic for return prediction—containing all relevant information such that additional processing can only lose rather than gain information. This would explain why ICA and LSTM fail: they attempt to extract structure that does not exist beyond what normalization already captures.

![Refer to caption](x10.png)


Figure 9: Comparison of signal quality between Raw flows, Z-score normalization, and Market Cap normalization (Matched Filter). Market Cap normalization significantly enhances the predictive signal.

### 5.2 Why LSTM Fails

The LSTM collapse is not a bug but a rational response to the data-generating process:

1. Signal-to-Noise Ratio: With return standard deviation of 3.49% and mean of 0.028%, the SNR is approximately 0.8%. For comparison, image classification tasks have SNR approaching 1.0 (100%). Neural networks are designed for high-SNR environments; in low-SNR settings, the optimal strategy is to predict the mean.

2. Over-parameterization: Our LSTM architecture has several thousand parameters. The effective sample size for learning sequential patterns is limited by the non-stationarity of financial data—patterns that exist may last only weeks or months before disappearing. The model is massively over-parameterized relative to the information content of the data.

3. Non-stationarity: Financial relationships are not stable. The attention mechanism cannot learn “look back 3 days for foreign flow” if that relationship reverses across regimes. The uniform attention weights reflect genuine ambiguity about which lags matter.

4. Adversarial Domain: Unlike natural images, financial data is generated by profit-seeking agents who actively arbitrage predictable patterns. Any stable relationship learned by ML is simultaneously being arbitraged away by other market participants, creating an adversarial dynamic absent from domains like computer vision.

### 5.3 Boundary Conditions for ML in Finance

Our findings suggest the following conditions must hold for ML to outperform linear models in finance:

1. 1.

   Sufficient SNR: Target variable must have SNR ≳5\gtrsim 5–10%10\% for neural networks to learn meaningful patterns. Most daily return prediction tasks fail this threshold.
2. 2.

   Stationarity: Patterns must be stable over time horizons comparable to training set length. Regime changes invalidate learned relationships.
3. 3.

   High-dimensional features: ML excels when combining many weak predictors. With only 3 investor types, the feature space is too sparse for complex models to exploit.
4. 4.

   Appropriate preprocessing: Even if ML adds value, the marginal contribution is small relative to feature engineering. The “Matched Filter” captures most of the available signal.

### 5.4 Implications for Practitioners

1. Invest in Feature Engineering: The largest alpha gains come from thoughtful data representation, not algorithmic complexity. A simple linear model with superior features will beat a complex model with raw data.

2. Beware of Overfitting Diagnostics: The LSTM collapse (predicting the mean) is a diagnostic signature that the model has insufficient signal. If predictions have zero variance or attention weights are uniform, the model has failed—even if training loss is low.

3. Simple Models for Transparency: The momentum strategy’s 56.5% hit rate is economically meaningful and interpretable: stocks with high normalized buying outperform. An LSTM’s internal representations are opaque and, in this case, empty.

4. Robustness Over Sophistication: The regime instability of ICA factors demonstrates that statistical significance in-sample does not imply stability out-of-sample. Simpler methods may generalize better.

## 6 Conclusion

This paper has investigated whether advanced machine learning techniques can extract predictive value from investor order flows beyond what simple feature engineering achieves. Using comprehensive data on Korean equities spanning 2020–2024, we applied Independent Component Analysis, Wavelet Coherence, and LSTM networks with attention mechanisms—representing the state of the art in blind source separation, multi-scale signal processing, and deep sequence learning.

Our findings are unambiguous: complexity fails. The ICA factors are unstable across market regimes. The wavelet coherence patterns contradict hypothesized decoupling. The LSTM collapses to predicting the unconditional mean. Meanwhile, a simple momentum strategy using market cap-normalized flows achieves a Sharpe ratio of 1.30—outperforming the ML pipeline by a factor of nearly 20.

We conclude that in low signal-to-noise financial environments, the physicist’s tool—the “Matched Filter” normalization grounded in market microstructure theory—dominates the computer scientist’s tool. The marginal contribution of algorithmic complexity is not merely zero; it is negative, as complex models destroy rather than enhance information.

These findings establish important boundary conditions for the application of machine learning to finance. Not all data are created equal. The conditions that enable deep learning success in image and language domains—high SNR, stable patterns, abundant data—may not hold for financial return prediction. Researchers and practitioners should accordingly calibrate their expectations and methodological choices.

Future research might explore whether ML succeeds in higher-frequency settings with greater SNR, in cross-sectional rather than time-series prediction, or with substantially larger feature sets. For investor flow prediction at daily frequency, however, our verdict is clear: simplicity wins.

## References

* Amihud (2002)

  Amihud, Y. (2002).
  Illiquidity and stock returns: Cross-section and time-series effects.
  Journal of Financial Markets, 5(1), 31–56.
* Arnott et al. (2019)

  Arnott, R., Harvey, C. R., and Markowitz, H. (2019).
  A backtesting protocol in the era of machine learning.
  The Journal of Financial Data Science, 1(1), 64–74.
* Ban et al. (2018)

  Ban, G.-Y., El Karoui, N., and Lim, A. E. (2018).
  Machine learning and portfolio optimization.
  Management Science, 64(3), 1136–1154.
* Barber and Odean (2000)

  Barber, B. M., and Odean, T. (2000).
  Trading is hazardous to your wealth: The common stock investment performance of individual investors.
  The Journal of Finance, 55(2), 773–806.
* Barber et al. (2009)

  Barber, B. M., Odean, T., and Zhu, N. (2009).
  Do retail trades move markets?
  The Review of Financial Studies, 22(1), 151–186.
* Chen et al. (2024)

  Chen, L., Pelger, M., and Zhu, J. (2024).
  Deep learning in asset pricing.
  Management Science, 70(2), 714–750.
* Choe et al. (2005)

  Choe, H., Kho, B.-C., and Stulz, R. M. (2005).
  Do domestic investors have an edge? The trading experience of foreign investors in Korea.
  The Review of Financial Studies, 18(3), 795–829.
* Chordia et al. (2002)

  Chordia, T., Roll, R., and Subrahmanyam, A. (2002).
  Order imbalance, liquidity, and market returns.
  Journal of Financial Economics, 65(1), 111–130.
* Fama (1970)

  Fama, E. F. (1970).
  Efficient capital markets: A review of theory and empirical work.
  The Journal of Finance, 25(2), 383–417.
* Feng et al. (2020)

  Feng, G., Giglio, S., and Xiu, D. (2020).
  Taming the factor zoo: A test of new factors.
  The Journal of Finance, 75(3), 1327–1370.
* Glosten and Milgrom (1985)

  Glosten, L. R., and Milgrom, P. R. (1985).
  Bid, ask and transaction prices in a specialist market with heterogeneously informed traders.
  Journal of Financial Economics, 14(1), 71–100.
* Griffin et al. (2003)

  Griffin, J. M., Harris, J. H., and Topaloglu, S. (2003).
  The dynamics of institutional and individual trading.
  The Journal of Finance, 58(6), 2285–2320.
* Grinblatt and Keloharju (2000)

  Grinblatt, M., and Keloharju, M. (2000).
  The investment behavior and performance of various investor types: A study of Finland’s unique data set.
  Journal of Financial Economics, 55(1), 43–67.
* Gu et al. (2020)

  Gu, S., Kelly, B., and Xiu, D. (2020).
  Empirical asset pricing via machine learning.
  The Review of Financial Studies, 33(5), 2223–2273.
* Harvey et al. (2016)

  Harvey, C. R., Liu, Y., and Zhu, H. (2016).
  …and the cross-section of expected returns.
  The Review of Financial Studies, 29(1), 5–68.
* Hasbrouck (1991)

  Hasbrouck, J. (1991).
  Measuring the information content of stock trades.
  The Journal of Finance, 46(1), 179–207.
* Hyvärinen and Oja (2000)

  Hyvärinen, A., and Oja, E. (2000).
  Independent component analysis: Algorithms and applications.
  Neural Networks, 13(4–5), 411–430.
* Jeon and Moffett (2010)

  Jeon, J. Q., and Moffett, C. M. (2010).
  Herding by foreign investors and emerging market equity returns: Evidence from Korea.
  International Review of Economics & Finance, 19(4), 698–710.
* Kim and Wei (2002)

  Kim, W., and Wei, S.-J. (2002).
  Foreign portfolio investors before and during a crisis.
  Journal of International Economics, 56(1), 77–96.
* Kyle (1985)

  Kyle, A. S. (1985).
  Continuous auctions and insider trading.
  Econometrica, 53(6), 1315–1335.
* López de Prado (2018)

  López de Prado, M. (2018).
  Advances in Financial Machine Learning.
  John Wiley & Sons.
* McLean and Pontiff (2016)

  McLean, R. D., and Pontiff, J. (2016).
  Does academic research destroy stock return predictability?
  The Journal of Finance, 71(1), 5–32.
* Sias (2004)

  Sias, R. W. (2004).
  Institutional herding.
  The Review of Financial Studies, 17(1), 165–206.
* Sirignano and Cont (2019)

  Sirignano, J., and Cont, R. (2019).
  Universal features of price formation in financial markets: Perspectives from deep learning.
  Quantitative Finance, 19(9), 1449–1459.

## Appendix A Technical Appendix

### A.1 Data Processing Details

Missing Data Handling: Stocks with fewer than 20 trading days in any calendar year are excluded. Missing daily observations are forward-filled from the previous trading day.

Outlier Treatment: Normalized flows beyond 5 standard deviations are winsorized to ±5​σ\pm 5\sigma to prevent extreme observations from dominating results.

Universe: We exclude stocks with market cap below 50 billion KRW to ensure tradability and reliable price data.

### A.2 ICA Implementation Details

Preprocessing:

1. 1.

   Center: 𝐗~t=𝐗t−𝐗¯\tilde{\mathbf{X}}\_{t}=\mathbf{X}\_{t}-\bar{\mathbf{X}}
2. 2.

   Whiten: 𝐙t=𝚲−1/2​𝐔T​𝐗~t\mathbf{Z}\_{t}=\mathbf{\Lambda}^{-1/2}\mathbf{U}^{T}\tilde{\mathbf{X}}\_{t} where Cov​(𝐗~)=𝐔​𝚲​𝐔T\text{Cov}(\tilde{\mathbf{X}})=\mathbf{U}\mathbf{\Lambda}\mathbf{U}^{T}
3. 3.

   Apply FastICA with G​(u)=log⁡cosh⁡(u)G(u)=\log\cosh(u), max 1000 iterations

Stability Analysis: Rolling 252-day windows with 21-day step. Mixing matrix distance computed as Frobenius norm: ‖𝐀​(t)−𝐀​(t−1)‖F||\mathbf{A}(t)-\mathbf{A}(t-1)||\_{F}.

### A.3 Wavelet Coherence Implementation

Wavelet: Morlet wavelet with ω0=6\omega\_{0}=6

Scales: Dyadic scales 2j2^{j} for j∈{1,2,3,4,5}j\in\{1,2,3,4,5\} corresponding to periods of 2, 4, 8, 16, 32 days

Normalization Fix: Due to the small magnitude of normalized flows (∼10−5\sim 10^{-5}), internal Z-score normalization was applied before CWT to prevent numerical underflow in coherence computation.

### A.4 LSTM Architecture Details

```
Input Shape: (batch, 10, 3)  # 10 days, 3 investor types

Layer 1: LSTM(64 units, return_sequences=True)
         Dropout(0.2)

Layer 2: LSTM(32 units, return_sequences=False)
         Dropout(0.2)

Attention: MultiHeadAttention(num_heads=4, key_dim=32)

Output: Dense(1, activation=’linear’)

Total Parameters: ~15,000
Training: Adam(lr=0.001), MSE loss, EarlyStopping(patience=10)
Epochs Trained: 23 (stopped by early stopping)
Best Validation Loss: 0.00138
```

### A.5 Transaction Cost Assumptions

* •

  Round-trip cost: 10 basis points (5bp each way)
* •

  Slippage: Not modeled separately (assumed included in spread)
* •

  Rebalancing: Daily
* •

  Position sizing: Equal-weighted within decile portfolios

### A.6 Bootstrap Confidence Intervals

For key correlation estimates, we compute 95% confidence intervals via block bootstrap (block length = 21 days, 1000 replications). Results show mixed statistical significance for hypothesized factors:

* •

  IC1 – USD/KRW: CI = [−0.07-0.07, +0.04+0.04] (Insignificant)
* •

  IC1 – VIX: CI = [+0.02+0.02, +0.13+0.13] (Significant)
* •

  IC3 – Spread: CI = [−0.13-0.13, −0.01-0.01] (Significant)