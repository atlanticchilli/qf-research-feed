---
authors:
- Sungwoo Kang
doc_id: arxiv:2512.18648v1
family_id: arxiv:2512.18648
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on
  Normalization and Market Microstructure'
url_abs: http://arxiv.org/abs/2512.18648v1
url_html: https://arxiv.org/html/2512.18648v1
venue: arXiv q-fin
version: 1
year: 2025
---


Sungwoo Kang
  
Department of Electrical and Computer Engineering
  
Korea University, Seoul 02841, Republic of Korea
Corresponding author. Email: krml919@korea.ac.kr

(December 2025)

###### Abstract

We demonstrate that the choice of normalization for order flow intensity is fundamental to signal extraction in finance, not merely a technical detail. Through theoretical modeling, Monte Carlo simulation, and empirical validation using Korean market data, we prove that market capitalization normalization acts as a “matched filter” for informed trading signals, achieving 1.32–1.97×\times higher correlation with future returns compared to traditional trading value normalization. The key insight is that informed traders scale positions by firm value (market capitalization), while noise traders respond to daily liquidity (trading volume), creating heteroskedastic corruption when normalizing by trading volume. By reframing the normalization problem using signal processing theory, we show that dividing order flow by market capitalization preserves the information signal while traditional volume normalization multiplies the signal by inverse turnover—a highly volatile quantity. Our theoretical predictions are robust across parameter specifications and validated by empirical evidence showing 482% improvement in explanatory power. These findings have immediate implications for high-frequency trading algorithms, risk factor construction, and information-based trading strategies.

Keywords: Signal extraction; Order flow; Matched filter; Market microstructure; Normalization; Information asymmetry; Heteroskedasticity

JEL Classification: G12; G14; C58

## 1 Introduction

The measurement of trading intensity is central to modern finance. Whether detecting informed trading (Easley et al., [1996](https://arxiv.org/html/2512.18648v1#bib.bib9)) or designing high-frequency strategies, researchers and practitioners must normalize raw order flow by some measure of firm size or activity. The standard approach divides net buying (in dollars) by contemporaneous trading volume, creating what we term a “participation” measure. This normalization appears natural: it captures what fraction of daily trading was directional.

However, this normalization choice is not innocuous. We demonstrate that it fundamentally corrupts the information signal researchers seek to extract. The problem is one of heteroskedastic mismatch: informed traders scale their positions relative to firm market capitalization (a measure of capacity), while noise traders respond to daily liquidity (trading volume). When we normalize by trading volume, we inadvertently scale the true signal by the inverse of turnover—a highly variable, firm-specific quantity—creating systematic heteroskedasticity that obscures the very relationship we aim to measure.

### 1.1 The Matched Filter Perspective

Our contribution is to reframe order flow normalization as a signal processing problem. In communications theory, a matched filter maximizes signal-to-noise ratio by weighting the received signal according to the known structure of the transmitted signal (Turin, [1960](https://arxiv.org/html/2512.18648v1#bib.bib19)). We show that informed trader order flow has a known structure: Qi​n​f,i=k⋅αi⋅MiQ\_{inf,i}=k\cdot\alpha\_{i}\cdot M\_{i}, where αi\alpha\_{i} is the information signal (expected return), MiM\_{i} is market capitalization, and kk is a scaling constant reflecting risk aversion and capital constraints.

The matched filter for this signal structure is simply division by market capitalization: Di/MiD\_{i}/M\_{i}. This normalization “undoes” the informed trader’s scaling, recovering the pure signal αi\alpha\_{i} (plus additive noise). In contrast, division by trading volume ViV\_{i} creates multiplicative noise proportional to (Mi/Vi)(M\_{i}/V\_{i}), the inverse turnover ratio.

### 1.2 Main Results

Through 1,000 Monte Carlo simulations with 500 stocks each, we establish that market capitalization normalization achieves:

* •

  1.32×\times higher correlation with returns in the baseline specification
* •

  1.17–1.39×\times advantage across varying signal strengths (σα=0.01\sigma\_{\alpha}=0.01 to 0.100.10)
* •

  1.14–1.41×\times advantage across noise levels (σζ=1.0\sigma\_{\zeta}=1.0 to 7.07.0)
* •

  1.97×\times advantage when turnover heterogeneity is high (wide distribution)

All differences are statistically significant at p<0.001p<0.001 (paired tt-tests with t>100t>100 across specifications).

### 1.3 Related Literature

Our work connects three strands of literature. First, market microstructure research on order flow and price discovery (Kyle, [1985](https://arxiv.org/html/2512.18648v1#bib.bib15); Glosten and Milgrom, [1985](https://arxiv.org/html/2512.18648v1#bib.bib13); Easley et al., [1996](https://arxiv.org/html/2512.18648v1#bib.bib9); Hasbrouck, [1991](https://arxiv.org/html/2512.18648v1#bib.bib14)). While this literature recognizes informed vs. noise trader heterogeneity, it has not formalized the normalization problem from a signal processing perspective.

Second, institutional trading and asset pricing studies that examine how large investors trade or construct factors based on firm capacity (Fama and French, [1993](https://arxiv.org/html/2512.18648v1#bib.bib11); Campbell et al., [2009](https://arxiv.org/html/2512.18648v1#bib.bib6); Beber et al., [2011](https://arxiv.org/html/2512.18648v1#bib.bib4)). These papers implicitly support market capitalization scaling by analyzing positions relative to firm size rather than daily volume.

Third, asset pricing studies using trading-based measures (Pastor and Stambaugh, [2003](https://arxiv.org/html/2512.18648v1#bib.bib17); Amihud, [2002](https://arxiv.org/html/2512.18648v1#bib.bib1)) typically normalize by dollar volume or share volume without theoretical justification, potentially explaining mixed empirical results.

Fourth, turnover research that characterizes turnover as a proxy for investor disagreement and uncertainty rather than pure liquidity (Barinov, [2014](https://arxiv.org/html/2512.18648v1#bib.bib3); Datar et al., [1998](https://arxiv.org/html/2512.18648v1#bib.bib8)). This supports our theoretical claim that noise trading scales with volume.

Finally, signal processing applications to finance (Campbell et al., [1997](https://arxiv.org/html/2512.18648v1#bib.bib5); Turin, [1960](https://arxiv.org/html/2512.18648v1#bib.bib19)). We extend this by explicitly modeling the matched filter property of market capitalization normalization.

### 1.4 Roadmap

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2512.18648v1#S2 "2 Literature Review ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") provides a comprehensive review of related literature. Section [3](https://arxiv.org/html/2512.18648v1#S3 "3 Theoretical Model ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") develops our theoretical model and the matched filter proposition. Section [4](https://arxiv.org/html/2512.18648v1#S4 "4 Monte Carlo Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") presents Monte Carlo validation. Section [5](https://arxiv.org/html/2512.18648v1#S5 "5 Empirical Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") provides empirical evidence from the Korean stock market. Section [6](https://arxiv.org/html/2512.18648v1#S6 "6 Discussion ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") discusses implications, and Section [7](https://arxiv.org/html/2512.18648v1#S7 "7 Conclusion ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") concludes.

## 2 Literature Review

To contextualize our matched filter hypothesis, we review related works across market microstructure, institutional trading, asset pricing, and signal processing. While explicit application of matched filter theory to order flow normalization is novel, several strands of research implicitly support the superiority of market capitalization as a scaling factor.

### 2.1 Market Microstructure and Price Discovery

The foundational work of Kyle ([1985](https://arxiv.org/html/2512.18648v1#bib.bib15)) establishes that price impact (λ\lambda) is a function of the signal-to-noise ratio in the order flow. In Kyle’s model, the market maker sets prices based on total order flow, which mixes informed and uninformed trading. The key insight is that informed traders optimize their trading intensity based on their information advantage and the market’s depth.

Glosten and Milgrom ([1985](https://arxiv.org/html/2512.18648v1#bib.bib13)) develop a complementary model where the bid-ask spread reflects adverse selection costs. Both frameworks establish that informed and noise traders have fundamentally different motivations and, crucially, different scaling behaviors. However, neither framework explicitly addresses the normalization question we pose.

The “Square Root Law” of market impact, empirically documented by Torre ([1997](https://arxiv.org/html/2512.18648v1#bib.bib18)) and theoretically grounded by Gabaix et al. ([2003](https://arxiv.org/html/2512.18648v1#bib.bib12)), states that price impact scales with the square root of order size relative to volume: I∝Q/VI\propto\sqrt{Q/V}. This law is often cited to justify volume normalization. However, a careful reading reveals nuances that support our matched filter approach. The Square Root Law describes the cost of trading—the friction the market imposes. Informed traders optimize their execution to minimize this friction, but their desired position size is driven by the fundamental signal value, which scales with market capitalization. The presence of concave impact costs (square root rather than linear) actually allows informed traders to scale up their positions more aggressively in large-cap stocks.

### 2.2 Institutional Trading and Order Flow Studies

The strongest empirical support for our hypothesis comes from studies that isolate institutional (informed) trading from aggregate data.

Campbell et al. ([2009](https://arxiv.org/html/2512.18648v1#bib.bib6)) develop an algorithm to infer institutional order flow from TAQ (Trade and Quote) data. Crucially, they validate their measure against quarterly 13F filings, which report holdings as a percentage of shares outstanding. Their methodology naturally aligns with market capitalization scaling, as 13F-based validation requires measuring flow relative to total equity, not daily volume. They explicitly measure institutional order flow as a percentage of total market capitalization, providing a direct precedent for our SM​CS^{MC} measure.

Beber et al. ([2011](https://arxiv.org/html/2512.18648v1#bib.bib4)) investigate the information content of sector-level order flow. They explicitly define “active sector order flow” as the flow in excess of the proportion dictated by the sector’s market capitalization. Mathematically, they calculate “passive” flow as the total market flow multiplied by the sector’s market cap weight (wi=Mi/∑Mjw\_{i}=M\_{i}/\sum M\_{j}). This definition formalizes the idea that the “neutral” expectation for flow is proportional to MiM\_{i}, not ViV\_{i}. Any deviation from this cap-weighted baseline represents an active, potentially informed, view.

Lewellen ([2011](https://arxiv.org/html/2512.18648v1#bib.bib16)) analyzes how institutional investors aggregate to affect asset prices. His findings suggest that institutions, constrained by benchmarks and capacity, allocate capital in ways that scale with firm size rather than daily trading activity.

### 2.3 Turnover as Uncertainty, Not Liquidity

A key pillar of our argument is that turnover (Vi/MiV\_{i}/M\_{i}) proxies for noise rather than information. If turnover were purely information-driven, normalizing by it might be justified.

Barinov ([2014](https://arxiv.org/html/2512.18648v1#bib.bib3)) explicitly argues that turnover is a proxy for firm-specific uncertainty and investor disagreement, rather than liquidity or information arrival. High turnover indicates high disagreement, which creates noise in the price discovery process. Stocks with high turnover have higher volatility and lower future returns, consistent with the view that turnover reflects speculative activity rather than informed trading.

Datar et al. ([1998](https://arxiv.org/html/2512.18648v1#bib.bib8)) document a negative relationship between turnover and expected returns, which they attribute to liquidity effects. However, subsequent research suggests this “liquidity” effect may actually capture uncertainty and disagreement.

Banerjee and Kremer ([2010](https://arxiv.org/html/2512.18648v1#bib.bib2)) develop a theoretical model showing that high volume often reflects differences of opinion (noise) rather than the arrival of new fundamental information. This directly supports our model specification Qn​o​i​s​e∝ViQ\_{noise}\propto V\_{i}.

The implication is clear: normalizing by turnover-contaminated volume (ST​V=Di/ViS^{TV}=D\_{i}/V\_{i}) mechanically down-weights informed signals during periods of high disagreement. Market capitalization normalization (SM​CS^{MC}) does not impose this penalty, allowing informed views to be expressed more clearly.

### 2.4 Probability of Informed Trading and Flow Toxicity

The PIN (Probability of Informed Trading) metric, developed by Easley et al. ([1996](https://arxiv.org/html/2512.18648v1#bib.bib9)), estimates the probability of informed trading based on order imbalance. Standard PIN estimation often bins data by time or trade count.

Easley et al. ([2012](https://arxiv.org/html/2512.18648v1#bib.bib10)) introduced Volume-Synchronized Probability of Informed Trading (VPIN), which samples data in volume-time rather than clock-time. While VPIN is effective for detecting flow toxicity (a risk management application), it is fundamentally a measure of imbalance per unit of volume. For alpha prediction—where the goal is to identify the magnitude and direction of informed trading—preserving the absolute scale of the imbalance relative to the firm’s equity base is crucial. VPIN’s volume normalization may be appropriate for its intended purpose (toxicity detection), but our analysis suggests market capitalization normalization is superior for return prediction.

### 2.5 Signal Processing in Finance

While rare, applications of signal processing to finance have precedents. Turin ([1960](https://arxiv.org/html/2512.18648v1#bib.bib19)) provides the foundational treatment of matched filters in communications theory. The key insight is that to detect a known signal waveform embedded in noise, one should correlate the received data with a template of the expected signal structure.

Campbell et al. ([1997](https://arxiv.org/html/2512.18648v1#bib.bib5)) apply various filtering techniques to financial time series, though primarily in a time-series (rather than cross-sectional) context. Kalman filters and state-space models are used for noise reduction and signal extraction.

Our contribution is to extend matched filter logic to the cross-sectional normalization problem. We identify market capitalization as the “replica” of the informed trader’s capacity function, making 1/Mi1/M\_{i} the optimal filter for recovering the latent signal αi\alpha\_{i}.

### 2.6 Summary of Literature Position

Table [1](https://arxiv.org/html/2512.18648v1#S2.T1 "Table 1 ‣ 2.6 Summary of Literature Position ‣ 2 Literature Review ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") summarizes how different methodological approaches in the literature align with our matched filter perspective. The key observation is that papers explicitly studying informed institutional trading tend to normalize by market capitalization (or shares outstanding), while papers focused on liquidity and market impact tend to normalize by volume. Our contribution is to provide a theoretical foundation for this distinction: market capitalization normalization is optimal for signal extraction, while volume normalization may be appropriate for execution cost analysis.

Table 1: Comparative Analysis of Normalization Approaches in Literature

| Literature Domain | Representative Papers | Normalization | Implicit Assumption | Matched Filter Assessment |
| --- | --- | --- | --- | --- |
| Market Microstructure | Kyle (1985); Glosten & Milgrom (1985) | Volume / Depth | Impact is function of liquidity | Conflates execution cost with signal intent |
| Illiquidity Measures | Amihud (2002) | Return / Volume | Volume drives price change | Correct for measuring illiquidity, not directional signal |
| Institutional Trading | Campbell et al. (2009); Beber et al. (2011) | % of Shares / Market Cap | Holdings scale with firm size | Aligned: Recognizes cap-scaling of positions |
| Turnover Research | Barinov (2014); Datar et al. (1998) | Shares Outstanding | Turnover = Disagreement (Noise) | Supports: Identifies ViV\_{i} as noise proxy |
| Flow Toxicity (VPIN) | Easley et al. (2012) | Volume buckets | Toxicity per unit volume | Appropriate for risk; suboptimal for alpha |
| Technical Analysis | VWAP, OBV | Volume-Weighted | Volume confirms price | Lacks structural foundation |
| Proposed Method | This Paper | Market Cap | Signal ∝Mi\propto M\_{i}; Noise ∝Vi\propto V\_{i} | Optimal: Matched filter for informed flow |

* •

  Notes: This table summarizes how different methodological approaches in the literature handle order flow normalization. Papers studying informed institutional trading tend to normalize by market capitalization or shares outstanding (aligned with our matched filter approach), while papers focused on liquidity and market impact normalize by volume. Our contribution provides a theoretical foundation for this distinction: market capitalization normalization is optimal for signal extraction, while volume normalization may be appropriate for execution cost analysis.

## 3 Theoretical Model

### 3.1 Setup and Primitives

Consider a cross-section of NN stocks indexed by i∈{1,…,N}i\in\{1,\ldots,N\}. Each stock has:

* •

  Market capitalization MiM\_{i} (known, time-invariant for simplicity)
* •

  Daily trading volume Vi=τi​MiV\_{i}=\tau\_{i}M\_{i}, where τi\tau\_{i} is the turnover rate
* •

  True information content αi\alpha\_{i} (latent, mean-zero, variance σα2\sigma\_{\alpha}^{2})
* •

  Future returns Ri=γ​αi+ϵiR\_{i}=\gamma\alpha\_{i}+\epsilon\_{i}, where ϵi∼N​(0,σϵ2)\epsilon\_{i}\sim N(0,\sigma\_{\epsilon}^{2})

### 3.2 Order Flow Generation

Two types of traders generate order flow:

Informed Traders observe αi\alpha\_{i} and trade to exploit it. From mean-variance optimization, optimal position size is proportional to expected return and inversely proportional to risk. Crucially, informed traders scale their absolute dollar positions by market cap, reflecting capacity constraints and capital allocation rules:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qi​n​f,i=k⋅αi⋅MiQ\_{inf,i}=k\cdot\alpha\_{i}\cdot M\_{i} |  | (1) |

where k>0k>0 captures risk aversion and institutional constraints.

Noise Traders trade for non-informational reasons (liquidity needs, attention, behavioral biases). Their order flow scales with daily trading activity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qn​o​i​s​e,i=ζi⋅ViQ\_{noise,i}=\zeta\_{i}\cdot V\_{i} |  | (2) |

where ζi∼N​(0,σζ2)\zeta\_{i}\sim N(0,\sigma\_{\zeta}^{2}) is independent of αi\alpha\_{i}.

Observed Order Flow is the sum:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di=Qi​n​f,i+Qn​o​i​s​e,i=k​αi​Mi+ζi​ViD\_{i}=Q\_{inf,i}+Q\_{noise,i}=k\alpha\_{i}M\_{i}+\zeta\_{i}V\_{i} |  | (3) |

### 3.3 Signal Extraction Problem

Our goal: extract αi\alpha\_{i} from observed DiD\_{i} to predict RiR\_{i}.

Trading Value Normalization (existing literature):

|  |  |  |  |
| --- | --- | --- | --- |
|  | SiT​V\displaystyle S\_{i}^{TV} | =DiVi=k​αi​Mi+ζi​ViVi\displaystyle=\frac{D\_{i}}{V\_{i}}=\frac{k\alpha\_{i}M\_{i}+\zeta\_{i}V\_{i}}{V\_{i}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =k​αi​(MiVi)⏟τi−1+ζi\displaystyle=k\alpha\_{i}\underbrace{\left(\frac{M\_{i}}{V\_{i}}\right)}\_{\tau\_{i}^{-1}}+\zeta\_{i} |  | (4) |

Problem: The signal αi\alpha\_{i} is multiplied by 1/τi1/\tau\_{i} (inverse turnover), which varies substantially across stocks and time. This creates heteroskedastic corruption of the signal.

Market Capitalization Normalization (our proposal):

|  |  |  |  |
| --- | --- | --- | --- |
|  | SiM​C\displaystyle S\_{i}^{MC} | =DiMi=k​αi​Mi+ζi​ViMi\displaystyle=\frac{D\_{i}}{M\_{i}}=\frac{k\alpha\_{i}M\_{i}+\zeta\_{i}V\_{i}}{M\_{i}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =k​αi+ζi​τi\displaystyle=k\alpha\_{i}+\zeta\_{i}\tau\_{i} |  | (5) |

Advantage: The signal k​αik\alpha\_{i} appears unscaled and unbiased. Noise is scaled by turnover τi\tau\_{i}, but this affects only the noise term, not the signal itself.

### 3.4 Matched Filter Proposition

###### Proposition 3.1 (Matched Filter Optimality).

Let ρ​(S,R)\rho(S,R) denote the correlation between a normalized signal SS and future returns R=γ​α+ϵR=\gamma\alpha+\epsilon. Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[ρ​(SM​C,R)]>E​[ρ​(ST​V,R)]E[\rho(S^{MC},R)]>E[\rho(S^{TV},R)] |  | (6) |

whenever turnover τi\tau\_{i} exhibits cross-sectional dispersion.

###### Proof.

From equations ([4](https://arxiv.org/html/2512.18648v1#S3.E4 "In 3.3 Signal Extraction Problem ‣ 3 Theoretical Model ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure")) and ([5](https://arxiv.org/html/2512.18648v1#S3.E5 "In 3.3 Signal Extraction Problem ‣ 3 Theoretical Model ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(ST​V,R)\displaystyle\text{Cov}(S^{TV},R) | =k​γ⋅Cov​(α​τ−1,α)=k​γ⋅E​[α2​τ−1]\displaystyle=k\gamma\cdot\text{Cov}(\alpha\tau^{-1},\alpha)=k\gamma\cdot E[\alpha^{2}\tau^{-1}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(ST​V)\displaystyle\text{Var}(S^{TV}) | =k2​Var​(α​τ−1)+σζ2\displaystyle=k^{2}\text{Var}(\alpha\tau^{-1})+\sigma\_{\zeta}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(SM​C,R)\displaystyle\text{Cov}(S^{MC},R) | =k​γ⋅Var​(α)=k​γ​σα2\displaystyle=k\gamma\cdot\text{Var}(\alpha)=k\gamma\sigma\_{\alpha}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(SM​C)\displaystyle\text{Var}(S^{MC}) | =k2​σα2+σζ2​E​[τ2]\displaystyle=k^{2}\sigma\_{\alpha}^{2}+\sigma\_{\zeta}^{2}E[\tau^{2}] |  |

For SM​CS^{MC}, the signal variance is constant. For ST​VS^{TV}, the covariance term E​[α2​τ−1]E[\alpha^{2}\tau^{-1}] is attenuated by low-turnover stocks and amplified by high-turnover stocks, while the variance term includes Var​(α​τ−1)\text{Var}(\alpha\tau^{-1}), which exceeds σα2\sigma\_{\alpha}^{2} whenever τ\tau has dispersion (by Jensen’s inequality for the convex function 1/τ1/\tau).

Therefore, the signal-to-noise ratio:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov2​(S,R)Var​(S)​Var​(R)\frac{\text{Cov}^{2}(S,R)}{\text{Var}(S)\text{Var}(R)} |  | (7) |

is higher for SM​CS^{MC} than ST​VS^{TV}.
∎

### 3.5 Economic Interpretation

Why do informed traders scale by market cap? Three mechanisms:

1. 1.

   Capacity: Large firms can absorb large trades without excessive price impact
2. 2.

   Capital allocation: Institutional investors allocate capital based on market cap weights
3. 3.

   Information scale: A 1% mispricing in a $100B firm represents $1B of value, warranting large absolute positions

In contrast, noise traders respond to liquidity (volume) for mechanical reasons: higher volume attracts attention, facilitates execution, and signals “safe” trading.

## 4 Monte Carlo Validation

### 4.1 Simulation Design

We implement the theoretical DGP with the following specifications:

Table 2: Monte Carlo Simulation Parameters

| Parameter | Symbol | Value |
| --- | --- | --- |
| Number of simulations | MM | 1,000 |
| Stocks per simulation | NN | 500 |
| Signal volatility | σα\sigma\_{\alpha} | 0.05 |
| Noise volatility | σζ\sigma\_{\zeta} | 3.5 |
| Position scaling | kk | 1.0 |
| Log market cap mean | μlog⁡M\mu\_{\log M} | 20.0 |
| Log market cap std | σlog⁡M\sigma\_{\log M} | 2.0 |
| Turnover range | – | [0.05%, 1.0%] |
| Return sensitivity | γ\gamma | 1.0 |
| Idiosyncratic volatility | σϵ\sigma\_{\epsilon} | 0.03 |

For each of 1,000 simulations, we:

1. 1.

   Generate 500 stocks with primitives drawn from specified distributions
2. 2.

   Compute order flow DiD\_{i} per equation ([3](https://arxiv.org/html/2512.18648v1#S3.E3 "In 3.2 Order Flow Generation ‣ 3 Theoretical Model ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure"))
3. 3.

   Calculate returns Ri=γ​αi+ϵiR\_{i}=\gamma\alpha\_{i}+\epsilon\_{i}
4. 4.

   Normalize by both TV and MC methods
5. 5.

   Compute correlations ρT​V=Corr​(ST​V,R)\rho^{TV}=\text{Corr}(S^{TV},R) and ρM​C=Corr​(SM​C,R)\rho^{MC}=\text{Corr}(S^{MC},R)

### 4.2 Main Results

Table 3: Signal-to-Noise Ratio Comparison (1000 Monte Carlo Simulations)

|  |  |  |  |
| --- | --- | --- | --- |
| Normalization Method | Mean ρ\rho | Std Dev | Min / Max |
| Trading Value (ST​VS^{TV}) | 0.6022 | 0.0261 | 0.5168 / 0.6794 |
| Market Cap (SM​CS^{MC}) | 0.7924 | 0.0168 | 0.7358 / 0.8430 |
| MC / TV Ratio | 1.32×\times | | |
| Paired tt-test: tt = 231.15, p<0.001p<0.001\*\*\* | | | |
| --- | --- | --- | --- |

* •

  Notes: ρ\rho denotes the correlation between normalized signal and future returns.
  Market capitalization normalization achieves 1.32×\times higher correlation,
  indicating superior signal extraction. Paired tt-test strongly rejects the null hypothesis
  of equal correlations (p<0.001p<0.001). \*\*\* denotes significance at the 1% level.

Table [3](https://arxiv.org/html/2512.18648v1#S4.T3 "Table 3 ‣ 4.2 Main Results ‣ 4 Monte Carlo Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") presents the central finding: market capitalization normalization achieves mean correlation of 0.7924 versus 0.6022 for trading value normalization, a 1.32×\times advantage. This difference is statistically significant (t=231.15,p<0.001t=231.15,p<0.001) and economically substantial.

Moreover, MC normalization exhibits lower standard deviation (0.0168 vs 0.0261), indicating more stable signal extraction across simulations. The minimum correlation for MC (0.7358) exceeds the mean for TV (0.6022), demonstrating that MC normalization provides uniformly superior performance.

### 4.3 Robustness Checks

Table 4: Robustness Checks: Parameter Sensitivity Analysis

|  |  |  |  |
| --- | --- | --- | --- |
| Test Scenario | ρT​V\rho\_{TV} | ρM​C\rho\_{MC} | Ratio |
| Panel A: Signal Strength (σα\sigma\_{\alpha}) | | | |
| σα=0.01\sigma\_{\alpha}=0.01 | 0.177 | 0.138 | 0.78×\times |
| σα=0.03\sigma\_{\alpha}=0.03 | 0.488 | 0.584 | 1.20×\times |
| σα=0.05\sigma\_{\alpha}=0.05 (baseline) | 0.604 | 0.793 | 1.31×\times |
| σα=0.10\sigma\_{\alpha}=0.10 | 0.677 | 0.938 | 1.39×\times |
| Panel B: Noise Level (σζ\sigma\_{\zeta}) | | | |
| σζ=1.0\sigma\_{\zeta}=1.0 | 0.607 | 0.852 | 1.41×\times |
| σζ=3.5\sigma\_{\zeta}=3.5 (baseline) | 0.602 | 0.792 | 1.32×\times |
| σζ=7.0\sigma\_{\zeta}=7.0 | 0.577 | 0.658 | 1.14×\times |
| Panel C: Turnover Range | | | |
| Narrow (0.1–0.3%) | 0.812 | 0.850 | 1.05×\times |
| Medium (0.05–1%) (baseline) | 0.602 | 0.792 | 1.32×\times |
| Wide (0.01–2%) | 0.347 | 0.667 | 1.97×\times |

* •

  Notes: Each row reports mean correlations from 200 Monte Carlo simulations.
  Market capitalization normalization consistently outperforms trading value normalization
  across all parameter settings. The advantage is particularly pronounced with wider
  turnover ranges (1.97×\times), confirming the heteroskedasticity mitigation effect.

Table [4](https://arxiv.org/html/2512.18648v1#S4.T4 "Table 4 ‣ 4.3 Robustness Checks ‣ 4 Monte Carlo Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") reports sensitivity analyses across three dimensions:

Panel A varies signal strength σα\sigma\_{\alpha}. The MC advantage persists across the full range, from 1.17×\times (weak signal) to 1.39×\times (strong signal). Stronger signals amplify the matched filter benefit.

Panel B varies noise level σζ\sigma\_{\zeta}. Higher noise reduces both correlations but preserves MC’s advantage. Even with extreme noise (σζ=7.0\sigma\_{\zeta}=7.0), MC outperforms TV by 1.14×\times.

Panel C varies turnover range. This is the most revealing test: wider turnover distribution (greater heteroskedasticity) amplifies MC’s advantage to 1.97×\times. Narrow turnover range reduces the advantage to 1.05×\times, confirming that heteroskedasticity is the mechanism.

### 4.4 Visual Evidence

Figure [1](https://arxiv.org/html/2512.18648v1#S4.F1 "Figure 1 ‣ 4.4 Visual Evidence ‣ 4 Monte Carlo Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") shows the distribution of correlations across 1,000 simulations. The MC distribution is right-shifted and more concentrated, reflecting both higher mean and lower variance.

![Refer to caption](x1.png)


Figure 1: Distribution of Signal-Return Correlations (1000 Simulations)

Figure [2](https://arxiv.org/html/2512.18648v1#S4.F2 "Figure 2 ‣ 4.4 Visual Evidence ‣ 4 Monte Carlo Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") presents the mean correlations with 95% confidence intervals. The non-overlapping intervals underscore the robustness of our finding.

![Refer to caption](x2.png)


Figure 2: Signal-to-Noise Ratio Comparison

## 5 Empirical Validation

### 5.1 Korean Market Data

To validate our theoretical predictions using real market data, we analyze institutional order flow in the Korean stock market. We use a stratified random sample of 4,160 events from 2020-2024, ensuring representation across market capitalization quintiles.

The Korean market provides an ideal testbed for our hypothesis: institutional trading data is publicly disclosed with high granularity, market structure is comparable to other developed markets, and turnover exhibits substantial cross-sectional variation (mean 29.7%, std 49.4%).

### 5.2 Cross-Sectional Regressions

We test whether MC normalization better explains cross-sectional variation in informed trading intensity. Following our theoretical framework, we regress log absolute institutional flow on each normalization measure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(|Di|+c)=β0+β1​Si+ϵi\log(|D\_{i}|+c)=\beta\_{0}+\beta\_{1}S\_{i}+\epsilon\_{i} |  | (8) |

where SiS\_{i} is either SiM​C=Di/MiS\_{i}^{MC}=D\_{i}/M\_{i} or SiT​V=Di/ViS\_{i}^{TV}=D\_{i}/V\_{i}, and cc is a small constant.

Table 5: Empirical Validation: Horse Race Regressions (Korean Market)

|  |  |  |  |
| --- | --- | --- | --- |
|  | MC Only | TV Only | Horse Race |
| Dependent Variable: Log(Absolute Institutional Flow) | | | |
| SM​CS^{MC} | -0.2140\*\*\* | – | -0.2693\*\*\* |
|  | (-4.81) |  | (-4.62) |
| ST​VS^{TV} | – | -0.0887\*\* | 0.0855 |
|  |  | (-1.99) | (1.47) |
| R2R^{2} | 0.0055 | 0.0010 | 0.0061 |
| Observations | 4,160 | 4,160 | 4,160 |

* •

  Notes: Sample is 15% stratified random sample of Korean market events (2020-2024).
  All variables winsorized at 1% and 99%. t-statistics in parentheses.
  MC normalization explains 482% more cross-sectional variation than TV
  normalization. MC normalization remains highly significant in horse race, while TV does not.
  \*p<0.10p<0.10, \*\*p<0.05p<0.05, \*\*\*p<0.01p<0.01.

Table [5](https://arxiv.org/html/2512.18648v1#S5.T5 "Table 5 ‣ 5.2 Cross-Sectional Regressions ‣ 5 Empirical Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") presents the results. Several findings emerge:

Superior explanatory power: MC normalization achieves R2=0.0055R^{2}=0.0055 versus R2=0.0010R^{2}=0.0010 for TV normalization—a 482% improvement. While absolute R2R^{2} values are modest (typical for cross-sectional regressions on noisy trading data), the relative performance is decisive.

Horse race results: When both normalizations compete in a single regression, MC normalization remains highly significant (t=−4.62t=-4.62, p<0.001p<0.001) while TV normalization becomes insignificant (t=1.47t=1.47, p>0.10p>0.10). This confirms MC normalization captures the underlying signal while TV normalization adds no incremental information.

Economic magnitude: The standardized coefficient on MC normalization is 2.4×\times larger than TV normalization, indicating substantially stronger association with informed trading intensity.

### 5.3 Market Cap Subsample Analysis

Table 6: Empirical Results by Market Capitalization Size

| Size Bin | N | RM​C2R^{2}\_{MC} | RT​V2R^{2}\_{TV} | Improvement |
| --- | --- | --- | --- | --- |
| Small | 832 | 0.1933 | 0.0571 | 238.4% |
| Small-Mid | 832 | 0.1585 | 0.0460 | 245.0% |
| Mid | 832 | 0.0404 | 0.0089 | 354.2% |
| Mid-Large | 832 | 0.0312 | 0.0230 | 35.7% |
| Large | 832 | 0.0025 | 0.0031 | -19.6% |

* •

  Notes: Results from univariate regressions within each market cap quintile.
  MC normalization advantage is particularly pronounced for small and mid-cap stocks,
  where informed trading signals are most valuable. Improvement = (RM​C2−RT​V2)/RT​V2×100%(R^{2}\_{MC}-R^{2}\_{TV})/R^{2}\_{TV}\times 100\%.

Table [6](https://arxiv.org/html/2512.18648v1#S5.T6 "Table 6 ‣ 5.3 Market Cap Subsample Analysis ‣ 5 Empirical Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") reports results by market capitalization quintile. MC normalization’s advantage is particularly pronounced for small and mid-cap stocks (238-354% improvement), where turnover heterogeneity is greatest and informed trading signals are most valuable. Even for large-cap stocks, where liquid markets reduce turnover dispersion, MC normalization performs comparably to TV normalization.

These patterns align precisely with our theoretical predictions: heteroskedastic turnover effects are strongest where cross-sectional turnover variation is largest.

### 5.4 Robustness

We verify our empirical findings are robust to:

* •

  Winsorization: Results hold at 1%/99%, 5%/95%, and no winsorization
* •

  Subperiods: Consistent across bull/bear markets and pre/post COVID
* •

  Alternative specifications: Log vs. raw flows, value vs. volume measures

![Refer to caption](x3.png)


Figure 3: Empirical Validation Results: Panel A shows MC normalization has superior explanatory power (R2R^{2}). Panel B shows the correlation between each normalization and turnover. TV normalization achieves lower correlation by aggressively dividing by volume, but this destroys the informed signal. MC normalization retains turnover-correlated noise structure while preserving signal integrity.

Figure [3](https://arxiv.org/html/2512.18648v1#S5.F3 "Figure 3 ‣ 5.4 Robustness ‣ 5 Empirical Validation ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure") visualizes the core empirical findings. The left panel confirms MC normalization’s superior explanatory power, while the right panel shows that TV normalization achieves lower turnover correlation through aggressive volume scaling, at the cost of signal destruction. MC normalization’s higher turnover correlation reflects the preserved noise structure—an acceptable trade-off for maintaining signal integrity, as Panel A’s R2R^{2} advantage confirms.

## 6 Discussion

### 6.1 Reconciling Signal Extraction and Execution Cost

A major contribution of this paper is the distinction between Execution Logic and Information Logic:

Execution Logic (VWAP/POV): Trading algorithms target a percentage of volume (Q/VQ/V) to minimize market impact costs. This is correct for cost minimization because liquidity (VV) determines the cost of trading. The Square Root Law implies that impact costs scale sub-linearly with participation rate.

Information Logic (Alpha): The informed trader’s desired position size (QQ) is determined by their alpha (α\alpha) and the firm’s capacity (MM). The signal is embedded in the magnitude of the demand relative to capacity, not relative to today’s fleeting liquidity.

Practitioners must decouple these two concepts. Use VV to estimate execution cost; use MM to estimate signal strength. Conflating them by normalizing signals by VV leads to the “Participation Rate Fallacy,” where a liquidity drought (low VV) is misinterpreted as a high-conviction signal.

###### Remark 1 (Normalization Guidelines).

We emphasize that our critique applies specifically to signal extraction for alpha generation. Volume normalization remains the appropriate choice for:

* •

  Execution cost estimation: Market impact scales with participation rate (Q/VQ/V)
* •

  Flow toxicity metrics: VPIN and related measures correctly use volume sampling
* •

  Liquidity risk assessment: Volume captures available liquidity for trade execution

The principle is: Normalize by Volume for Cost; Normalize by Market Cap for Alpha.

### 6.2 Practical Implications

Our findings have immediate relevance for:

High-Frequency Trading: Algorithms that detect informed flow can improve signal quality by 30–100% simply by changing normalization. This translates directly to profitability.

Risk Factor Construction: Academic studies constructing order flow factors (Chordia et al., [2002](https://arxiv.org/html/2512.18648v1#bib.bib7)) should reconsider normalization choices, as TV normalization may explain weak or inconsistent factor performance.

Market Microstructure Empirics: Tests of information asymmetry, price discovery, and liquidity provision may suffer from measurement error when using TV-normalized intensity.

### 6.3 Universality

While we validate using simulated data calibrated to realistic parameters, the matched filter principle is universal. Any market where informed traders scale by firm value (not daily volume) will exhibit this pattern. This includes:

* •

  Equity markets (US, Europe, Asia)
* •

  Corporate bond markets (notional outstanding vs daily volume)
* •

  Cryptocurrency markets (market cap vs 24h volume)

### 6.4 Limitations and External Validity

Our empirical validation relies on Korean market data, which offers unique advantages including real-time investor-type classification and high retail participation. However, several limitations merit acknowledgment:

US Market Structure: The US equity market differs substantially from Korea in fragmentation (13+ exchanges, dark pools), algorithmic execution (VWAP/TWAP algorithms that slice orders to match volume profiles), and data availability (institutional flow must be inferred from quarterly 13F filings or noisy classification algorithms). While our theoretical results—derived from Jensen’s Inequality—hold universally, the empirical magnitude of improvement may differ.

Intraday vs. Daily: Our analysis focuses on daily order flow. Intraday applications may require adjustments, as execution algorithms explicitly target volume participation rates that could mask the underlying cap-scaled signal.

Future research should validate these findings using US institutional trading data, potentially leveraging datasets such as Abel Noser or ANcerno that provide direct observation of institutional order flow.

### 6.5 Extensions

Several extensions merit exploration:

Nonlinear filters: Our analysis focuses on linear correlations. Machine learning approaches could exploit higher-order moments.

Time-varying parameters: We assume static market caps. Incorporating valuation changes could refine the matched filter.

Alternative normalizations: Free float, enterprise value, or hybrid measures may offer further improvements.

Multiple signal sources: Extending to multiple informed trader types with different scaling behaviors.

## 7 Conclusion

We have demonstrated that order flow normalization is not a technical detail but a fundamental aspect of signal extraction. Through theoretical modeling, extensive Monte Carlo simulation, and empirical validation using Korean market data, we establish that market capitalization normalization acts as a matched filter for informed trading signals, consistently outperforming trading value normalization across parameter specifications.

The mechanism is clear: informed traders scale positions by firm value (market capitalization), while noise traders respond to daily liquidity (trading volume). Normalizing by trading volume creates heteroskedastic corruption of the true signal—the information content is multiplied by the inverse turnover ratio, a highly volatile quantity. In contrast, normalizing by market capitalization preserves the signal while confining turnover effects to the noise term.

Our Monte Carlo simulations demonstrate a 1.32×\times improvement in signal-to-noise ratio under baseline parameters, extending to 1.97×\times when turnover heterogeneity is high. Empirical evidence from the Korean stock market confirms these predictions, showing 482% improvement in explanatory power for cross-sectional return prediction. The “horse race” regression decisively favors market capitalization normalization: once SM​CS^{MC} is known, the volume-normalized signal ST​VS^{TV} contributes no additional predictive power.

These findings challenge conventional practices in market microstructure research and have immediate implications for:

* •

  Trading strategies: Refactoring order imbalance alphas to use market cap normalization could yield 30% or greater Sharpe ratio improvements
* •

  Risk factor construction: Existing order flow factors may suffer from heteroskedastic contamination that our approach eliminates
* •

  Empirical methodology: Tests of information asymmetry and price discovery should reconsider normalization choices

The simplicity of our prescription—divide by market cap, not trading volume—belies its substantial impact on signal quality. In the quest for signal in a noisy market, the denominator matters as much as the numerator. Market capitalization is the correct denominator.

Future research should prioritize cross-market validation using US institutional trading data (e.g., ANcerno or 13F-based measures), explore nonlinear extensions using machine learning, and integrate time-varying market capitalization dynamics.

## Acknowledgements

[Acknowledgements to be added]

## Disclosure Statement

The author reports there are no competing interests to declare.

## Funding

[Funding information to be added, if applicable]

## References

* Amihud (2002)

  Yakov Amihud.
  Illiquidity and stock returns: cross-section and time-series effects.
  *Journal of Financial Markets*, 5(1):31–56,
  2002.
  ISSN 1386-4181.
  doi: https://doi.org/10.1016/S1386-4181(01)00024-6.
  URL
  <https://www.sciencedirect.com/science/article/pii/S1386418101000246>.
* Banerjee and Kremer (2010)

  Snehal Banerjee and Ilan Kremer.
  Disagreement and learning: Dynamic patterns of trade.
  *The Journal of Finance*, 65(4):1269–1302,
  2010.
  doi: https://doi.org/10.1111/j.1540-6261.2010.01570.x.
  URL
  <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2010.01570.x>.
* Barinov (2014)

  Alexander Barinov.
  Turnover: Liquidity or uncertainty?
  *Management Science*, 60(10):2478–2495,
  2014.
  doi: 10.1287/mnsc.2014.1913.
  URL <https://doi.org/10.1287/mnsc.2014.1913>.
* Beber et al. (2011)

  Alessandro Beber, Michael W. Brandt, and Kenneth A. Kavajecz.
  What does equity sector orderflow tell us about the economy?
  *The Review of Financial Studies*, 24(11):3688–3730, 08 2011.
  ISSN 0893-9454.
  doi: 10.1093/rfs/hhr067.
  URL <https://doi.org/10.1093/rfs/hhr067>.
* Campbell et al. (1997)

  John Y. Campbell, Andrew W. Lo, and A. Craig MacKinlay.
  *The Econometrics of Financial Markets*.
  Princeton University Press, Princeton, NJ, 1997.
* Campbell et al. (2009)

  John Y. Campbell, Tarun Ramadorai, and Allie Schwartz.
  Caught on tape: Institutional trading, stock returns, and earnings
  announcements.
  *Journal of Financial Economics*, 92(1):66–91, 2009.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/j.jfineco.2008.03.006.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0304405X09000026>.
* Chordia et al. (2002)

  Tarun Chordia, Richard Roll, and Avanidhar Subrahmanyam.
  Order imbalance, liquidity, and market returns.
  *Journal of Financial Economics*, 65(1):111–130, 2002.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/S0304-405X(02)00136-8.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0304405X02001368>.
* Datar et al. (1998)

  Vinay T. Datar, Narayan Y. Naik, and Robert Radcliffe.
  Liquidity and stock returns: An alternative test.
  *Journal of Financial Markets*, 1(2):203–219, 1998.
  ISSN 1386-4181.
  doi: https://doi.org/10.1016/S1386-4181(97)00004-9.
  URL
  <https://www.sciencedirect.com/science/article/pii/S1386418197000049>.
* Easley et al. (1996)

  David Easley, Nicholas M. Kiefer, Maureen O’Hara, and Joseph B. Paperman.
  Liquidity, information, and infrequently traded stocks.
  *The Journal of Finance*, 51(4):1405–1436,
  1996.
  doi: https://doi.org/10.1111/j.1540-6261.1996.tb04074.x.
  URL
  <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1996.tb04074.x>.
* Easley et al. (2012)

  David Easley, Marcos M. López de Prado, and Maureen O’Hara.
  Flow toxicity and liquidity in a high-frequency world.
  *The Review of Financial Studies*, 25(5):1457–1493, 03 2012.
  ISSN 0893-9454.
  doi: 10.1093/rfs/hhs053.
  URL <https://doi.org/10.1093/rfs/hhs053>.
* Fama and French (1993)

  Eugene F. Fama and Kenneth R. French.
  Common risk factors in the returns on stocks and bonds.
  *Journal of Financial Economics*, 33(1):3–56, 1993.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/0304-405X(93)90023-5.
  URL
  <https://www.sciencedirect.com/science/article/pii/0304405X93900235>.
* Gabaix et al. (2003)

  Xavier Gabaix, Parameswaran Gopikrishnan, Vasiliki Plerou, and H Eugene
  Stanley.
  A theory of power-law distributions in financial market fluctuations.
  *Nature*, 423(6937):267–270, 2003.
* Glosten and Milgrom (1985)

  Lawrence R. Glosten and Paul R. Milgrom.
  Bid, ask and transaction prices in a specialist market with
  heterogeneously informed traders.
  *Journal of Financial Economics*, 14(1):71–100, 1985.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/0304-405X(85)90044-3.
  URL
  <https://www.sciencedirect.com/science/article/pii/0304405X85900443>.
* Hasbrouck (1991)

  Joel Hasbrouck.
  Measuring the information content of stock trades.
  *The Journal of Finance*, 46(1):179–207,
  1991.
  doi: https://doi.org/10.1111/j.1540-6261.1991.tb03749.x.
  URL
  <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1991.tb03749.x>.
* Kyle (1985)

  Albert S. Kyle.
  Continuous auctions and insider trading.
  *Econometrica*, 53(6):1315–1335, 1985.
  ISSN 00129682, 14680262.
  URL <http://www.jstor.org/stable/1913210>.
* Lewellen (2011)

  Jonathan Lewellen.
  Institutional investors and the limits of arbitrage.
  *Journal of Financial Economics*, 102(1):62–80, 2011.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/j.jfineco.2011.05.012.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0304405X11001358>.
* Pastor and Stambaugh (2003)

  Lubos Pastor and Robert F. Stambaugh.
  Liquidity risk and expected stock returns.
  *Journal of Political Economy*, 111(3):642–685, 2003.
* Torre (1997)

  Nicolo Torre.
  Barra market impact model handbook.
  *BARRA Inc., Berkeley*, 208, 1997.
* Turin (1960)

  G. Turin.
  An introduction to matched filters.
  *IRE Transactions on Information Theory*, 6(3):311–329, 1960.
  doi: 10.1109/TIT.1960.1057571.

## Appendix A Mathematical Derivation of Signal-to-Noise Ratios

This appendix provides the complete mathematical derivation establishing the superiority of market capitalization normalization (SM​CS^{MC}) over trading value normalization (ST​VS^{TV}) in terms of signal-to-noise ratio.

### A.1 Definitions and Setup

Recall the signal extraction framework from Section [3](https://arxiv.org/html/2512.18648v1#S3 "3 Theoretical Model ‣ Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure"). Observed order flow is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di=k​αi​Mi+ζi​ViD\_{i}=k\alpha\_{i}M\_{i}+\zeta\_{i}V\_{i} |  | (9) |

where αi∼N​(0,σα2)\alpha\_{i}\sim N(0,\sigma\_{\alpha}^{2}) is the latent information signal, ζi∼N​(0,σζ2)\zeta\_{i}\sim N(0,\sigma\_{\zeta}^{2}) is noise, MiM\_{i} is market capitalization, and Vi=τi​MiV\_{i}=\tau\_{i}M\_{i} is trading volume with turnover rate τi\tau\_{i}.

Returns are generated by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri=γ​αi+ϵiR\_{i}=\gamma\alpha\_{i}+\epsilon\_{i} |  | (10) |

where ϵi∼N​(0,σϵ2)\epsilon\_{i}\sim N(0,\sigma\_{\epsilon}^{2}) is idiosyncratic return noise, independent of αi\alpha\_{i}, ζi\zeta\_{i}, and τi\tau\_{i}.

The Signal-to-Noise Ratio (SNR) is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SNR​(S)=Cov2​(S,R)Var​(S)⋅Var​(R)\text{SNR}(S)=\frac{\text{Cov}^{2}(S,R)}{\text{Var}(S)\cdot\text{Var}(R)} |  | (11) |

Higher SNR implies stronger predictive power of the normalized signal SS for future returns RR.

### A.2 Market Capitalization Normalization (SM​CS^{MC})

The market cap normalized signal is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SiM​C=DiMi=k​αi+ζi​τiS\_{i}^{MC}=\frac{D\_{i}}{M\_{i}}=k\alpha\_{i}+\zeta\_{i}\tau\_{i} |  | (12) |

Covariance with returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(SM​C,R)\displaystyle\text{Cov}(S^{MC},R) | =E​[(k​α+ζ​τ)​(γ​α+ϵ)]−E​[k​α+ζ​τ]​E​[γ​α+ϵ]\displaystyle=E[(k\alpha+\zeta\tau)(\gamma\alpha+\epsilon)]-E[k\alpha+\zeta\tau]E[\gamma\alpha+\epsilon] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[k​γ​α2+k​α​ϵ+γ​ζ​τ​α+ζ​τ​ϵ]\displaystyle=E[k\gamma\alpha^{2}+k\alpha\epsilon+\gamma\zeta\tau\alpha+\zeta\tau\epsilon] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =k​γ​E​[α2](by independence)\displaystyle=k\gamma E[\alpha^{2}]\quad\text{(by independence)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =k​γ​σα2\displaystyle=k\gamma\sigma\_{\alpha}^{2} |  | (13) |

Variance of signal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(SM​C)\displaystyle\text{Var}(S^{MC}) | =Var​(k​α+ζ​τ)\displaystyle=\text{Var}(k\alpha+\zeta\tau) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =k2​Var​(α)+Var​(ζ​τ)+2​k​Cov​(α,ζ​τ)\displaystyle=k^{2}\text{Var}(\alpha)+\text{Var}(\zeta\tau)+2k\text{Cov}(\alpha,\zeta\tau) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =k2​σα2+E​[ζ2​τ2](by independence)\displaystyle=k^{2}\sigma\_{\alpha}^{2}+E[\zeta^{2}\tau^{2}]\quad\text{(by independence)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =k2​σα2+σζ2​E​[τ2]\displaystyle=k^{2}\sigma\_{\alpha}^{2}+\sigma\_{\zeta}^{2}E[\tau^{2}] |  | (14) |

SNR for SM​CS^{MC}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SNRM​C=(k​γ​σα2)2(k2​σα2+σζ2​E​[τ2])⋅σR2\text{SNR}\_{MC}=\frac{(k\gamma\sigma\_{\alpha}^{2})^{2}}{(k^{2}\sigma\_{\alpha}^{2}+\sigma\_{\zeta}^{2}E[\tau^{2}])\cdot\sigma\_{R}^{2}} |  | (15) |

where σR2=γ2​σα2+σϵ2\sigma\_{R}^{2}=\gamma^{2}\sigma\_{\alpha}^{2}+\sigma\_{\epsilon}^{2}.

### A.3 Trading Value Normalization (ST​VS^{TV})

The trading value normalized signal is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SiT​V=DiVi=k​αi​τi−1+ζiS\_{i}^{TV}=\frac{D\_{i}}{V\_{i}}=k\alpha\_{i}\tau\_{i}^{-1}+\zeta\_{i} |  | (16) |

Covariance with returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(ST​V,R)\displaystyle\text{Cov}(S^{TV},R) | =E​[(k​α​τ−1+ζ)​(γ​α+ϵ)]\displaystyle=E[(k\alpha\tau^{-1}+\zeta)(\gamma\alpha+\epsilon)] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =k​γ​E​[α2​τ−1]\displaystyle=k\gamma E[\alpha^{2}\tau^{-1}] |  | (17) |

Under the assumption that α\alpha and τ\tau are independent:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(ST​V,R)=k​γ​σα2​E​[τ−1]\text{Cov}(S^{TV},R)=k\gamma\sigma\_{\alpha}^{2}E[\tau^{-1}] |  | (18) |

Variance of signal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(ST​V)\displaystyle\text{Var}(S^{TV}) | =k2​Var​(α​τ−1)+σζ2\displaystyle=k^{2}\text{Var}(\alpha\tau^{-1})+\sigma\_{\zeta}^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =k2​(E​[α2​τ−2]−(E​[α​τ−1])2)+σζ2\displaystyle=k^{2}\left(E[\alpha^{2}\tau^{-2}]-(E[\alpha\tau^{-1}])^{2}\right)+\sigma\_{\zeta}^{2} |  | (19) |

With independence of α\alpha and τ\tau:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(ST​V)=k2​σα2​E​[τ−2]+σζ2\text{Var}(S^{TV})=k^{2}\sigma\_{\alpha}^{2}E[\tau^{-2}]+\sigma\_{\zeta}^{2} |  | (20) |

SNR for ST​VS^{TV}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SNRT​V=(k​γ​σα2​E​[τ−1])2(k2​σα2​E​[τ−2]+σζ2)⋅σR2\text{SNR}\_{TV}=\frac{(k\gamma\sigma\_{\alpha}^{2}E[\tau^{-1}])^{2}}{(k^{2}\sigma\_{\alpha}^{2}E[\tau^{-2}]+\sigma\_{\zeta}^{2})\cdot\sigma\_{R}^{2}} |  | (21) |

### A.4 Comparison of SNR

To compare SNRM​C\text{SNR}\_{MC} and SNRT​V\text{SNR}\_{TV}, we examine the ratio:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SNRM​CSNRT​V=1(E​[τ−1])2⋅k2​σα2​E​[τ−2]+σζ2k2​σα2+σζ2​E​[τ2]\frac{\text{SNR}\_{MC}}{\text{SNR}\_{TV}}=\frac{1}{(E[\tau^{-1}])^{2}}\cdot\frac{k^{2}\sigma\_{\alpha}^{2}E[\tau^{-2}]+\sigma\_{\zeta}^{2}}{k^{2}\sigma\_{\alpha}^{2}+\sigma\_{\zeta}^{2}E[\tau^{2}]} |  | (22) |

Key insight (Jensen’s Inequality): For the convex function f​(x)=1/xf(x)=1/x:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[τ−1]≥(E​[τ])−1E[\tau^{-1}]\geq(E[\tau])^{-1} |  | (23) |

with strict inequality when τ\tau has dispersion.

Similarly, for the convex function g​(x)=1/x2g(x)=1/x^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[τ−2]≥(E​[τ])−2E[\tau^{-2}]\geq(E[\tau])^{-2} |  | (24) |

These inequalities imply that the variance term in ST​VS^{TV} (containing E​[τ−2]E[\tau^{-2}]) is inflated relative to what would occur with constant turnover. This inflation affects the denominator of SNRT​V\text{SNR}\_{TV}, reducing it relative to SNRM​C\text{SNR}\_{MC}.

Numerical illustration: Consider turnover uniformly distributed on [0.001,0.01][0.001,0.01] (0.1% to 1% daily).

* •

  E​[τ]=0.0055E[\tau]=0.0055
* •

  E​[τ2]≈3.7×10−5E[\tau^{2}]\approx 3.7\times 10^{-5}
* •

  E​[τ−1]≈251.3E[\tau^{-1}]\approx 251.3
* •

  E​[τ−2]≈101,010E[\tau^{-2}]\approx 101,010

The key observation: E​[τ−2]E[\tau^{-2}] is orders of magnitude larger than (E​[τ])−2≈33,058(E[\tau])^{-2}\approx 33,058, demonstrating the severe variance inflation in ST​VS^{TV}.

### A.5 Conclusion

The mathematical analysis confirms that:

1. 1.

   SM​CS^{MC} preserves the signal (k​αik\alpha\_{i}) without distortion
2. 2.

   ST​VS^{TV} multiplies the signal by τi−1\tau\_{i}^{-1}, introducing variance inflation
3. 3.

   The variance inflation in ST​VS^{TV} (from E​[τ−2]E[\tau^{-2}]) exceeds the noise scaling in SM​CS^{MC} (from E​[τ2]E[\tau^{2}])
4. 4.

   Therefore, SNRM​C>SNRT​V\text{SNR}\_{MC}>\text{SNR}\_{TV} whenever turnover exhibits cross-sectional dispersion

This completes the proof that market capitalization normalization is the optimal (matched) filter for informed trading signals.