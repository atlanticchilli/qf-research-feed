---
authors:
- Marc Schmitt
doc_id: arxiv:2602.03903v1
family_id: arxiv:2602.03903
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary
  Portfolio VaR'
url_abs: http://arxiv.org/abs/2602.03903v1
url_html: https://arxiv.org/html/2602.03903v1
venue: arXiv q-fin
version: 1
year: 2026
---


Marc Schmitt

###### Abstract

Risk forecasts drive trading constraints and capital allocation, yet losses are nonstationary and regime-dependent. This paper studies sequential one-sided VaR control via conformal calibration. I propose regime-weighted conformal risk control (RWC), which calibrates a safety buffer from past forecast errors using exponential time decay and regime-similarity weights from regime features. RWC is model-agnostic and wraps any conditional quantile forecaster to target a desired exceedance rate. Finite-sample coverage is established under weighted exchangeability, and approximation bounds are derived under smoothly drifting regimes. On the CRSP U.S. equity portfolio, time-weighted conformal calibration is a strong default under drift, while regime weighting can improve regime-conditional stability in some settings with modest conservativeness changes.

conformal prediction, risk control, nonstationarity, finance, time series

## 1 Introduction

Forecasting and controlling tail risk in financial markets is notoriously difficult.
Return distributions are heavy-tailed, exhibit volatility clustering, and shift over time; even if the conditional distribution is well-modeled within a regime, it can drift rapidly during crises or structural change. Moreover, this nonstationarity is often regime-structured: volatility and tail behavior cluster into persistent states (e.g., calm vs stress), as in regime-switching models (Hamilton, [1989](https://arxiv.org/html/2602.03903v1#bib.bib32 "A new approach to the economic analysis of nonstationary time series and the business cycle"); Gray, [1996](https://arxiv.org/html/2602.03903v1#bib.bib31 "Modeling the conditional distribution of interest rates as a regime-switching process"); Engle and Rangel, [2008](https://arxiv.org/html/2602.03903v1#bib.bib41 "The spline-garch model for low-frequency volatility and its global macroeconomic causes")). As a result, value-at-risk (VaR) forecasts can be miscalibrated, with realized VaR exceedance rates deviating substantially from nominal targets, especially in stress periods (Berkowitz and O’Brien, [2002](https://arxiv.org/html/2602.03903v1#bib.bib37 "How accurate are value-at-risk models at commercial banks?")). These calibration failures matter because VaR-type constraints directly affect leverage and risk-taking (Basak and Shapiro, [2001](https://arxiv.org/html/2602.03903v1#bib.bib38 "Value-at-risk-based risk management: optimal policies and asset prices"); Adrian and Shin, [2014](https://arxiv.org/html/2602.03903v1#bib.bib39 "Procyclical leverage and value-at-risk")).

Conformal prediction is appealing for risk control because it can wrap black-box forecasters and provide finite-sample guarantees under exchangeability. However, financial data are sequential and nonstationary, so classical conformal validity can fail under time dependence and distribution shift. Prior work addresses covariate shift via importance weighting (Tibshirani et al., [2019](https://arxiv.org/html/2602.03903v1#bib.bib47 "Conformal prediction under covariate shift")), sequential nonstationarity via adaptive updates (Gibbs and Candès, [2021](https://arxiv.org/html/2602.03903v1#bib.bib12 "Adaptive conformal inference under distribution shift")), and dynamics in time series (Xu and Xie, [2021](https://arxiv.org/html/2602.03903v1#bib.bib15 "Conformal prediction interval for dynamic time-series")).
In finance, drift is pervasive and often regime-structured, so calibration should remain stable within regimes. This work is complementary to Conformal Risk Control (Angelopoulos et al., [2024](https://arxiv.org/html/2602.03903v1#bib.bib25 "Conformal risk control")), which controls the expected value of a monotone loss functional. In contrast, sequential one-sided quantile risk (VaR exceedances) is targeted in nonstationary, regime-structured time series and calibration is adapted by recency and regime-similarity weighting of conformity scores.

Recency weighting alone often stabilizes calibration under drift: the resulting time-weighted conformal calibration (TWC) is a strong, computationally simple default. Building on this, RWC adds regime-similarity weighting to target regime-conditional calibration when market conditions recur (e.g., volatility regimes), at the cost of reducing the effective calibration sample size. This leads to a natural empirical question: when does regime weighting improve stability beyond time weighting, and what is the conservativeness tradeoff?

#### Contributions.

* •

  Sequential VaR control under nonstationarity is formalized and metrics for regime-conditional calibration are proposed.
* •

  RWC is introduced, combining recency and regime-similarity weighting to adapt conformal calibration to drift.
* •

  Finite-sample guarantees under weighted exchangeability are proved and error is bounded under smoothly drifting regime-conditional distributions.
* •

  TWC is a strong default, while regime weighting can improve regime-conditional stability with modest additional conservativeness.

## 2 Background and related work

Conformal prediction provides finite-sample marginal coverage guarantees under exchangeability (Vovk et al., [2005](https://arxiv.org/html/2602.03903v1#bib.bib7 "Algorithmic learning in a random world"); Shafer and Vovk, [2008](https://arxiv.org/html/2602.03903v1#bib.bib8 "A tutorial on conformal prediction")). For regression, conformalized quantile regression (CQR) yields adaptive, heteroscedastic intervals by conformalizing estimated conditional quantiles (Romano et al., [2019](https://arxiv.org/html/2602.03903v1#bib.bib11 "Conformalized quantile regression")). This provides a direct template for conformalizing quantile forecasts; a one-sided VaR bound can be viewed as a sequential, tail-focused analogue in which an additive safety buffer is calibrated on a (1−α)(1-\alpha) quantile forecaster. Weighted conformal methods extend this framework to certain forms of distribution shift by computing weighted quantiles of past conformity scores, often using density-ratio weights (Tibshirani et al., [2019](https://arxiv.org/html/2602.03903v1#bib.bib47 "Conformal prediction under covariate shift")). The same weighted conformal mechanism is adopted, but weights are derived from recency and regime similarity rather than density ratios, which underpins the weighted-exchangeability guarantee.

Recent work generalizes conformal prediction from coverage guarantees to risk control.
Conformal Risk Control (CRC) controls the expectation of a monotone loss functional and discusses variants under distribution shift (Angelopoulos et al., [2024](https://arxiv.org/html/2602.03903v1#bib.bib25 "Conformal risk control"); Snell and Griffiths, [2025](https://arxiv.org/html/2602.03903v1#bib.bib2 "Conformal prediction as Bayesian quadrature")).
This setting differs in both objective and structure: sequential control of VaR exceedances in nonstationary financial time series is targeted, specialization is to one-sided quantile bounds, and adaptation is achieved by localizing the calibration score distribution toward relevant historical observations.

Nonstationarity has been explicitly addressed in sequential and time-series conformal inference. Adaptive conformal inference (ACI) dynamically adjusts the effective miscoverage level to maintain calibration under drift (Gibbs and Candès, [2021](https://arxiv.org/html/2602.03903v1#bib.bib12 "Adaptive conformal inference under distribution shift")), and ACI is used as a primary baseline. In contrast, the target exceedance level is kept fixed and adaptation is achieved by reweighting the calibration scores. For time series, EnbPI provides bootstrap-based conformal intervals for dynamic sequences (Xu and Xie, [2021](https://arxiv.org/html/2602.03903v1#bib.bib15 "Conformal prediction interval for dynamic time-series")), with subsequent work developing sequential predictive conformal inference (Xu and Xie, [2023](https://arxiv.org/html/2602.03903v1#bib.bib17 "Sequential predictive conformal inference for time series")). Related approaches cast sequential conformal calibration as a control problem, using feedback mechanisms to track recent miscoverage (Angelopoulos et al., [2023](https://arxiv.org/html/2602.03903v1#bib.bib18 "Conformal pid control for time series prediction")); this approach instead emphasizes relevance-based localization via time decay and regime similarity.

A growing theoretical literature studies conformal guarantees beyond exchangeability.
General validity results justify asymmetric and weighted conformal constructions in drifting or non-i.i.d. settings (Barber et al., [2023](https://arxiv.org/html/2602.03903v1#bib.bib14 "Conformal prediction beyond exchangeability")), providing a principled foundation for recency- and regime-weighted calibration.
Online analyses further characterize conformal inference under arbitrary sequential distribution shifts (Gibbs and Candès, [2024](https://arxiv.org/html/2602.03903v1#bib.bib13 "Conformal inference for online prediction with arbitrary distribution shifts")), offering a complementary perspective on nonstationary deployment.

Exact distribution-free conditional coverage is fundamentally impossible in general (Barber et al., [2021](https://arxiv.org/html/2602.03903v1#bib.bib20 "The limits of distribution-free conditional predictive inference")), motivating practical forms of localized or group-conditional calibration. Localized conformal prediction adapts score distributions to neighborhoods in feature space (Guan, [2023](https://arxiv.org/html/2602.03903v1#bib.bib21 "Conformal prediction with localization")), while class-conditional conformal methods provide stratified coverage across groups (Ding et al., [2023](https://arxiv.org/html/2602.03903v1#bib.bib22 "Class-conditional conformal prediction with many classes")).
Regime-weighted calibration can be viewed as a continuous analogue of such stratification, designed to stabilize exceedance rates across recurring market regimes.

Finally, VaR is a quantile-based tail risk measure widely used in practice, while CVaR (expected shortfall) captures tail severity (Rockafellar and Uryasev, [2000](https://arxiv.org/html/2602.03903v1#bib.bib33 "Optimization of conditional value-at-risk"); Engle and Manganelli, [2004](https://arxiv.org/html/2602.03903v1#bib.bib3 "CAViaR: conditional autoregressive value at risk by regression quantiles")). Empirical studies document systematic VaR model failures, particularly during stress periods (Berkowitz and O’Brien, [2002](https://arxiv.org/html/2602.03903v1#bib.bib37 "How accurate are value-at-risk models at commercial banks?")), motivating calibration layers that remain reliable under nonstationarity. Standard VaR backtests evaluate unconditional exceedance rates and independence (Kupiec, [1995](https://arxiv.org/html/2602.03903v1#bib.bib34 "Techniques for verifying the accuracy of risk measurement models"); Christoffersen, [1998](https://arxiv.org/html/2602.03903v1#bib.bib35 "Evaluating interval forecasts")).
This focus is complementary: predictive VaR bounds targeting a desired exceedance level are constructed and stability across regimes is emphasized.

## 3 Problem setup: sequential portfolio risk control

A time series of covariates and portfolio losses is observed:

|  |  |  |
| --- | --- | --- |
|  | (xt,yt)∈𝒳×𝒴,t=1,2,…,T,(x\_{t},y\_{t})\in\mathcal{X}\times\mathcal{Y},\qquad t=1,2,\dots,T, |  |

where xtx\_{t} summarizes information available at time tt (e.g., recent returns, realized volatility), and yty\_{t} is the realized next-period portfolio loss (e.g., yt=−rtporty\_{t}=-r^{\text{port}}\_{t} for one-day return rtportr^{\text{port}}\_{t}).
Let α∈(0,1)\alpha\in(0,1) denote a target miscoverage level (e.g., α=0.01\alpha=0.01 for 99% VaR control).
A one-sided VaR bound at level 1−α1-\alpha is a function Ut​(xt)U\_{t}(x\_{t}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(yt≤Ut​(xt))≥1−α.\mathbb{P}\big(y\_{t}\leq U\_{t}(x\_{t})\big)\geq 1-\alpha. |  | (1) |

In nonstationary settings, the distribution of (xt,yt)(x\_{t},y\_{t}) may vary with tt.
Procedures are therefore studied that aim to keep empirical exceedance rates close to α\alpha over time and within market regimes.

#### Timing convention (causality).

Throughout, xtx\_{t} denotes the information set available *strictly before* the loss yty\_{t} is realized.
For daily close-to-close data, yty\_{t} is the loss over trading day tt (i.e., from day t−1t{-}1 close to day tt close), so yt=−rtporty\_{t}=-r^{\text{port}}\_{t} with rtportr^{\text{port}}\_{t} the t−1→tt{-}1\to t return.
All components of xtx\_{t} (and regime features zt=g​(xt)z\_{t}=g(x\_{t})) are computed using data available up through day t−1t{-}1.
Thus the procedure observes xtx\_{t}, outputs Ut​(xt)U\_{t}(x\_{t}), and only then observes yty\_{t}, matching Algorithm [1](https://arxiv.org/html/2602.03903v1#alg1 "Algorithm 1 ‣ Finite-sample correction (optional). ‣ 4.2 Weighted conformal quantile ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").

#### Base quantile forecaster.

Let q^t=ft​(xt)\hat{q}\_{t}=f\_{t}(x\_{t}) denote a prediction of the conditional (1−α)(1-\alpha)-quantile of yty\_{t} produced by an arbitrary forecaster ftf\_{t} trained on past data (e.g., rolling-window quantile regression, GARCH-based VaR).
Conformal risk control constructs an adjusted bound

|  |  |  |
| --- | --- | --- |
|  | Ut=q^t+c^t,U\_{t}=\hat{q}\_{t}+\hat{c}\_{t}, |  |

where c^t\hat{c}\_{t} is a data-driven safety buffer calibrated from past forecast errors.

#### Conformity scores.

The one-sided conformity score at time tt is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | st:=yt−q^t,s\_{t}:=y\_{t}-\hat{q}\_{t}, |  | (2) |

so that large positive sts\_{t} indicates the base model under-predicted tail risk.
A conformal adjustment c^t\hat{c}\_{t} is typically a high quantile of past scores {si}\{s\_{i}\}.

## 4 Method: Regime-weighted conformal calibration

RWC is introduced, which calibrates c^t\hat{c}\_{t} using a weighted quantile of past conformity scores. The weights emphasize (i) recency, to adapt under drift, and (ii) regime similarity, to improve regime-conditional stability when conditions recur.

### 4.1 Regime representation and weighting

Let zt=g​(xt)∈ℝdz\_{t}=g(x\_{t})\in\mathbb{R}^{d} be a *regime embedding* computed from covariates, intended to capture market conditions such as volatility level and trend. In experiments, interpretable regime features are used, but gg can be any fixed mapping.

For a current time tt and a calibration index i<ti<t, assign weight

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi​(t)∝exp⁡(−λ​(t−i))⏟recency⋅Kh​(zi,zt)⏟regime similarity,w\_{i}(t)\propto\underbrace{\exp\!\big(-\lambda(t-i)\big)}\_{\text{recency}}\cdot\underbrace{K\_{h}\!\big(z\_{i},z\_{t}\big)}\_{\text{regime similarity}}, |  | (3) |

where λ≥0\lambda\geq 0 is a decay rate and KhK\_{h} is a positive kernel (e.g., Gaussian) with bandwidth hh:

|  |  |  |
| --- | --- | --- |
|  | Kh​(zi,zt)=exp⁡(−12​h2​‖zi−zt‖2).K\_{h}(z\_{i},z\_{t})=\exp\!\Big(-\tfrac{1}{2h^{2}}\left\lVert z\_{i}-z\_{t}\right\rVert^{2}\Big). |  |

Thus recent scores and scores from similar regimes receive higher weight.

#### Preprocessing of regime features.

Because KhK\_{h} depends on Euclidean distances, each coordinate of ztz\_{t} is standardized to zero mean and unit variance using training-period statistics (to avoid test leakage), and the same transform is applied at validation and test time. Bandwidths hh are reported in standardized units.

#### Weighted conformal inference.

Importance-weighted conformal calibration corrects covariate shift by weighting scores via density ratios (Tibshirani et al., [2019](https://arxiv.org/html/2602.03903v1#bib.bib47 "Conformal prediction under covariate shift")). More broadly, conformal validity can extend beyond exchangeability via carefully designed asymmetric weighting schemes (Barber et al., [2023](https://arxiv.org/html/2602.03903v1#bib.bib14 "Conformal prediction beyond exchangeability")). In RWC, time decay prioritizes recent history under drift, while kernel similarity localizes calibration to comparable market regimes.

### 4.2 Weighted conformal quantile

#### Calibration index set.

Let mm be the maximum calibration-buffer size. At time tt, let ℐt⊂{1,…,t−1}\mathcal{I}\_{t}\subset\{1,\dots,t-1\} denote the available score indices just before issuing the time-tt bound. The recent window used is

|  |  |  |
| --- | --- | --- |
|  | ℐt:={i:max⁡{1,t−m}≤i≤t−1}.\mathcal{I}\_{t}:=\{\,i:\max\{1,\,t-m\}\leq i\leq t-1\,\}. |  |

When t−1<mt-1<m, this reduces to ℐt={1,…,t−1}\mathcal{I}\_{t}=\{1,\dots,t-1\}. Conformalized bounds are issued once ℐt\mathcal{I}\_{t} is nonempty; denote the first such time by t0t\_{0}.

#### Weighted quantile threshold.

Given scores {si}i∈ℐt\{s\_{i}\}\_{i\in\mathcal{I}\_{t}} and unnormalized weights {wi​(t)}i∈ℐt\{w\_{i}(t)\}\_{i\in\mathcal{I}\_{t}} from ([3](https://arxiv.org/html/2602.03903v1#S4.E3 "Equation 3 ‣ 4.1 Regime representation and weighting ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")), define normalized weights w~i​(t):=wi​(t)/∑j∈ℐtwj​(t)\tilde{w}\_{i}(t):=w\_{i}(t)\big/\sum\_{j\in\mathcal{I}\_{t}}w\_{j}(t).
RWC sets

|  |  |  |  |
| --- | --- | --- | --- |
|  | c^t:=Q1−αw~​(t)​({si}i∈ℐt),\hat{c}\_{t}:=Q^{\tilde{w}(t)}\_{1-\alpha}\Big(\{s\_{i}\}\_{i\in\mathcal{I}\_{t}}\Big), |  | (4) |

the weighted (1−α)(1-\alpha)-quantile of the score distribution (using the standard “smallest cc such that cumulative weight ≥1−α\geq 1-\alpha” definition; see [Appendix A](https://arxiv.org/html/2602.03903v1#A1 "Appendix A Implementation details ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")).
Finally, output Ut=q^t+c^tU\_{t}=\hat{q}\_{t}+\hat{c}\_{t}.

#### Finite-sample correction (optional).

For exact finite-sample validity as in [Theorem 5.2](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem2 "Theorem 5.2 (Finite-sample weighted coverage). ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"), one can replace the level 1−α1-\alpha in ([4](https://arxiv.org/html/2602.03903v1#S4.E4 "Equation 4 ‣ Weighted quantile threshold. ‣ 4.2 Weighted conformal quantile ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")) by the inflated level ρt\rho\_{t} in ([5](https://arxiv.org/html/2602.03903v1#S5.E5 "Equation 5 ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")). In experiments, 1−α1-\alpha is used; when the total calibration weight WtW\_{t} (or neff​(t)n\_{\mathrm{eff}}(t)) is large, the difference is typically negligible.

Algorithm 1  RWC: Regime-Weighted Conformal VaR

1: Input: target α\alpha; base forecaster ftf\_{t}; calibration size mm; decay λ\lambda; kernel KhK\_{h}; regime map gg; ESS threshold nminn\_{\min}

2: Initialize empty buffers for past scores {si}\{s\_{i}\} and embeddings {zi}\{z\_{i}\}

3: for t=t0,t0+1,…,Tt=t\_{0},t\_{0}{+}1,\dots,T do

4:  Observe covariates xtx\_{t} (available before yty\_{t}) and compute zt=g​(xt)z\_{t}=g(x\_{t})

5:  Train/update base model ftf\_{t} on past data; predict q^t=ft​(xt)\hat{q}\_{t}=f\_{t}(x\_{t})

6:  Form weights wi​(t)∝exp⁡(−λ​(t−i))⋅Kh​(zi,zt)w\_{i}(t)\propto\exp(-\lambda(t-i))\cdot K\_{h}(z\_{i},z\_{t}) for i∈ℐti\in\mathcal{I}\_{t}

7:  Normalize w~i​(t)←wi​(t)/∑j∈ℐtwj​(t)\tilde{w}\_{i}(t)\leftarrow w\_{i}(t)\big/\sum\_{j\in\mathcal{I}\_{t}}w\_{j}(t)

8:  Compute neff​(t)←1/∑i∈ℐtw~i​(t)2n\_{\mathrm{eff}}(t)\leftarrow 1\big/\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)^{2}

9:  if neff​(t)<nminn\_{\mathrm{eff}}(t)<n\_{\min} then

10:   Set Kh≡1K\_{h}\equiv 1 for this step (fallback to time-only weights) and recompute w~i​(t)∝exp⁡(−λ​(t−i))\tilde{w}\_{i}(t)\propto\exp(-\lambda(t-i))

11:  end if

12:  Compute c^t←Q1−αw~​(t)​({si}i∈ℐt)\hat{c}\_{t}\leftarrow Q^{\tilde{w}(t)}\_{1-\alpha}\!\left(\{s\_{i}\}\_{i\in\mathcal{I}\_{t}}\right)

13:  Output VaR bound Ut=q^t+c^tU\_{t}=\hat{q}\_{t}+\hat{c}\_{t}

14:  Observe loss yty\_{t} and compute score st=yt−q^ts\_{t}=y\_{t}-\hat{q}\_{t}

15:  Append (st,zt)(s\_{t},z\_{t}) to buffers; keep only most recent mm entries

16: end for

### 4.3 Baselines

RWC is compared to three sequential conformal calibrators:
(i) SWC: sliding-window conformal with an unweighted window of the last mm scores;
(ii) TWC: time-weighted conformal using only recency weights (set Kh≡1K\_{h}\equiv 1);
(iii) ACI (Gibbs and Candès, [2021](https://arxiv.org/html/2602.03903v1#bib.bib12 "Adaptive conformal inference under distribution shift")): adaptive conformal inference that updates an effective miscoverage level to track drift.

## 5 Theory

Classical conformal guarantees rely on exchangeability, which is typically violated by dependent and drifting financial time series. Still, exact finite-sample results under idealized symmetry assumptions are useful as a benchmark: they clarify how weighting yields validity and connect RWC to weighted conformal prediction (Tibshirani et al., [2019](https://arxiv.org/html/2602.03903v1#bib.bib47 "Conformal prediction under covariate shift")) and conformal validity beyond exchangeability (Barber et al., [2023](https://arxiv.org/html/2602.03903v1#bib.bib14 "Conformal prediction beyond exchangeability")). Two results are therefore presented: (1) an exact finite-sample statement under weighted exchangeability; and (2) an approximate regime-conditional bound under smooth drift, making explicit the localization–variance tradeoff induced by kernel weights. Proofs are in the appendix.

### 5.1 Exact coverage under weighted exchangeability

#### Notation.

Fix time tt and calibration index set ℐt⊂{1,…,t−1}\mathcal{I}\_{t}\subset\{1,\dots,t-1\}.
Let wi​(t)≥0w\_{i}(t)\geq 0 be the (unnormalized) weights in ([3](https://arxiv.org/html/2602.03903v1#S4.E3 "Equation 3 ‣ 4.1 Regime representation and weighting ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")) for i∈ℐti\in\mathcal{I}\_{t}, and define

|  |  |  |
| --- | --- | --- |
|  | Wt:=∑i∈ℐtwi​(t),w¯i​(t):=wi​(t)Wt.W\_{t}:=\sum\_{i\in\mathcal{I}\_{t}}w\_{i}(t),\qquad\bar{w}\_{i}(t):=\frac{w\_{i}(t)}{W\_{t}}. |  |

Let wt​(t)w\_{t}(t) denote the test-time weight for the current point; for ([3](https://arxiv.org/html/2602.03903v1#S4.E3 "Equation 3 ‣ 4.1 Regime representation and weighting ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")), wt​(t)=1w\_{t}(t)=1.
For a finite-sample correction analogous to the usual (m+1)(m{+}1) conformal adjustment, use the inflated level

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt:=min⁡{1,(1−α)​(1+wt​(t)Wt)}.\rho\_{t}\;:=\;\min\!\left\{1,\;(1-\alpha)\Big(1+\frac{w\_{t}(t)}{W\_{t}}\Big)\right\}. |  | (5) |

Define the weighted threshold

|  |  |  |  |
| --- | --- | --- | --- |
|  | c^t:=Qρtw¯​(t)​({si}i∈ℐt),\hat{c}\_{t}\;:=\;Q^{\bar{w}(t)}\_{\rho\_{t}}\Big(\{s\_{i}\}\_{i\in\mathcal{I}\_{t}}\Big), |  | (6) |

and output Ut=q^t+c^tU\_{t}=\hat{q}\_{t}+\hat{c}\_{t}.

###### Assumption 5.1 (Weighted exchangeability).

Fix time tt.
Conditional on (xt,zt)(x\_{t},z\_{t}), the collection {(si,wi​(t))}i∈ℐt∪{(st,wt​(t))}\{(s\_{i},w\_{i}(t))\}\_{i\in\mathcal{I}\_{t}}\cup\{(s\_{t},w\_{t}(t))\} is weighted exchangeable in the sense of Tibshirani et al. ([2019](https://arxiv.org/html/2602.03903v1#bib.bib47 "Conformal prediction under covariate shift")).

###### Theorem 5.2 (Finite-sample weighted coverage).

Under Assumption [5.1](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem1 "Assumption 5.1 (Weighted exchangeability). ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"), the RWC bound Ut=q^t+c^tU\_{t}=\hat{q}\_{t}+\hat{c}\_{t} with c^t\hat{c}\_{t} defined in ([6](https://arxiv.org/html/2602.03903v1#S5.E6 "Equation 6 ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")) satisfies

|  |  |  |
| --- | --- | --- |
|  | ℙ​(yt≤Ut|xt,zt)≥1−α.\mathbb{P}\big(y\_{t}\leq U\_{t}\,\big|\,x\_{t},z\_{t}\big)\geq 1-\alpha. |  |

#### Remark (relation to the implementation).

If one uses ρt=1−α\rho\_{t}=1-\alpha instead of ([5](https://arxiv.org/html/2602.03903v1#S5.E5 "Equation 5 ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")), the difference is typically negligible when WtW\_{t} (or the effective sample size) is large, but [Theorem 5.2](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem2 "Theorem 5.2 (Finite-sample weighted coverage). ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") uses the standard finite-sample correction.

### 5.2 Regime-conditional coverage under drift

Exact exchangeability is unrealistic for finance. The approximation error is therefore analyzed when score distributions vary smoothly across regimes and drift gradually over time, so that emphasizing recent and regime-similar calibration points yields near-valid coverage.

###### Assumption 5.3 (Smooth regime drift and gradual time variation).

Let Ft​(u∣z)F\_{t}(u\mid z) denote the conditional CDF of the score sts\_{t} given zt=zz\_{t}=z.
There exist constants Lz,Lt>0L\_{z},L\_{t}>0 such that for all z,z′∈ℝdz,z^{\prime}\in\mathbb{R}^{d} and all u∈ℝu\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | |Ft(u∣z)−Ft(u∣z′)|≤Lz∥z−z′∥.\big|F\_{t}(u\mid z)-F\_{t}(u\mid z^{\prime})\big|\leq L\_{z}\|z-z^{\prime}\|. |  |

Moreover, for all i<ti<t and all u∈ℝu\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | |Fi(u∣zt)−Ft(u∣zt)|≤Lt|t−i|.\big|F\_{i}(u\mid z\_{t})-F\_{t}(u\mid z\_{t})\big|\leq L\_{t}|t-i|. |  |

Finally, {zt}\{z\_{t}\} is bounded and the kernel KhK\_{h} is Lipschitz and concentrates its mass within ‖zi−zt‖=O​(h)\|z\_{i}-z\_{t}\|=O(h) under the normalized weights.

#### Effective weighted sample size.

Let w¯i​(t)\bar{w}\_{i}(t) denote the normalized calibration weights and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | neff​(t):=1∑i∈ℐtw¯i​(t)2.n\_{\mathrm{eff}}(t):=\frac{1}{\sum\_{i\in\mathcal{I}\_{t}}\bar{w}\_{i}(t)^{2}}. |  | (7) |

###### Theorem 5.4 (Approximate regime-conditional coverage under smooth drift (informal)).

Under Assumption [5.3](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem3 "Assumption 5.3 (Smooth regime drift and gradual time variation). ‣ 5.2 Regime-conditional coverage under drift ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") and mild regularity of the weighted quantile estimator, RWC achieves

|  |  |  |
| --- | --- | --- |
|  | ℙ​(yt≤Ut∣zt)≥1−α−εt,\mathbb{P}\!\left(y\_{t}\leq U\_{t}\mid z\_{t}\right)\geq 1-\alpha-\varepsilon\_{t}, |  |

where the coverage gap admits a decomposition

|  |  |  |
| --- | --- | --- |
|  | εt=O​(Lz​h)+O​(Lt​τt)+O​(1neff​(t)),\varepsilon\_{t}\;=\;O(L\_{z}h)\;+\;O\!\Big(L\_{t}\,\tau\_{t}\Big)\;+\;O\!\left(\sqrt{\frac{1}{n\_{\mathrm{eff}}(t)}}\right), |  |

with τt:=∑i∈ℐtw¯i​(t)​(t−i)\tau\_{t}:=\sum\_{i\in\mathcal{I}\_{t}}\bar{w}\_{i}(t)\,(t-i) the effective lag under the normalized weights (for TWC this depends only on recency; for RWC it reflects both recency and regime similarity). The stochastic term corresponds to concentration of the weighted empirical CDF and holds under independence and, more generally, under sufficiently weak dependence (e.g., mixing conditions) up to log factors.

#### Discussion.

[Theorem 5.4](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem4 "Theorem 5.4 (Approximate regime-conditional coverage under smooth drift (informal)). ‣ Effective weighted sample size. ‣ 5.2 Regime-conditional coverage under drift ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") motivates choosing hh small enough to localize to similar regimes while maintaining a sufficiently large neff​(t)n\_{\mathrm{eff}}(t). The recency parameter λ\lambda controls the effective memory, trading off faster adaptation against increased variance. In practice, (λ,h,m)(\lambda,h,m) are tuned on a validation period to balance calibration, regime stability, and conservativeness.

## 6 Experiments

### 6.1 Data and portfolio

#### Data.

Daily U.S. equity data from the CRSP value-weighted market index
(accessed via WRDS) are used, spanning 1990-03-30 through 2024-12-31 (8755 trading days).
CRSP is the benchmark dataset in empirical asset pricing and risk management,
providing survivorship-bias-free coverage, accurate return adjustments for
dividends and other corporate actions, and a long, internally consistent
historical record spanning multiple business cycles and crisis regimes. These
properties make CRSP particularly well suited for evaluating tail-risk control
and calibration stability under nonstationarity. The daily loss is defined as

|  |  |  |
| --- | --- | --- |
|  | yt=−rtport,y\_{t}=-r^{\text{port}}\_{t}, |  |

where rtportr^{\text{port}}\_{t} denotes the portfolio return at time tt.

#### Sample period and splits.

A chronological split is adopted: training (1990-03-30–2011-01-31), validation (2011-02-01–2018-01-16), and test (2018-01-17–2024-12-31). The test period contains N=1751N=1751 observations. Unless otherwise stated, all tables report test-period results (e.g., Table [5](https://arxiv.org/html/2602.03903v1#S6.T5 "Table 5 ‣ Effective sample size and effective memory. ‣ 6.5 Diagnostics and Sensitivity ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")). Rolling exceedance plots show the full sample, with the test start marked by a vertical dotted line.

#### Regimes.

Market regimes are represented using interpretable features from lagged returns and evaluation is stratified by realized-volatility quintiles. Concretely, the regime embedding ztz\_{t} is built from 21-day realized volatility and 5-day mean absolute returns (definitions and preprocessing in Appendix [A](https://arxiv.org/html/2602.03903v1#A1 "Appendix A Implementation details ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")).

#### Hyperparameter tuning.

Conformal hyperparameters are tuned on the validation period via grid search. For each candidate setting the validation exceedance rate Exc^val\widehat{\mathrm{Exc}}\_{\mathrm{val}} and the maximum 1-year rolling exceedance RollMax^val\widehat{\mathrm{RollMax}}\_{\mathrm{val}} (252 trading days) are computed, and hyperparameters are selected by minimizing
|Exc^val−α|+0.5​max⁡{0,RollMax^val−α}.|\widehat{\mathrm{Exc}}\_{\mathrm{val}}-\alpha|+0.5\max\{0,\widehat{\mathrm{RollMax}}\_{\mathrm{val}}-\alpha\}.
For SWC/TWC/RWC grids m∈{252,504,756}m\in\{252,504,756\}, λ∈{0.002,0.005,0.01}\lambda\in\{0.002,0.005,0.01\}, and h∈{0.5,1,2}h\in\{0.5,1,2\} (RWC only) are used. For ACI, m=252m=252 is set and γ∈{0.002,0.005,0.01,0.02}\gamma\in\{0.002,0.005,0.01,0.02\} is tuned using the same objective. Selected hyperparameters are reported in Table [7](https://arxiv.org/html/2602.03903v1#A1.T7 "Table 7 ‣ Regime embedding used in experiments. ‣ Appendix A Implementation details ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"). For RWC an ESS safeguard is also applied: if neff​(t)<nminn\_{\mathrm{eff}}(t)<n\_{\min}, a fallback to time-only (TWC) weights is used for that step (nmin=100n\_{\min}=100 for the GBDT base and nmin=30n\_{\min}=30 for the HS base).

### 6.2 Models and calibrators

#### Base forecasters.

Two representative base VaR forecasters are considered: (i) *historical simulation* (HS), a rolling empirical (1−α)(1-\alpha) quantile of past losses; and (ii) *gradient boosting quantile regression* (GBDT), fit on a rolling window of covariates. Each forecaster outputs q^t\hat{q}\_{t}, an estimate of the (1−α)(1-\alpha)-quantile of yty\_{t}.

#### Conformal wrappers.

SWC, TWC, ACI (Gibbs and Candès, [2021](https://arxiv.org/html/2602.03903v1#bib.bib12 "Adaptive conformal inference under distribution shift")), and RWC are applied to each base model.

### 6.3 Metrics

The following are reported: (i) overall exceedance rate 1T​∑t𝟏​{yt>Ut}\frac{1}{T}\sum\_{t}\mathbf{1}\{y\_{t}>U\_{t}\}; (ii) exceedance rate by regime (realized-volatility quintiles); (iii) average bound tightness 1T​∑tUt\frac{1}{T}\sum\_{t}U\_{t} (lower is tighter, subject to calibration); (iv) rolling 1-year exceedance rates; and (v) standard VaR backtests on exceedance indicators: Kupiec UC and Christoffersen IND/CC (Kupiec, [1995](https://arxiv.org/html/2602.03903v1#bib.bib34 "Techniques for verifying the accuracy of risk measurement models"); Christoffersen, [1998](https://arxiv.org/html/2602.03903v1#bib.bib35 "Evaluating interval forecasts")).

### 6.4 Results

Out-of-sample 99% VaR control (α=0.01\alpha=0.01) is reported on the CRSP value-weighted market index. [Table 1](https://arxiv.org/html/2602.03903v1#S6.T1 "In 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") summarizes overall calibration and tightness, [Table 2](https://arxiv.org/html/2602.03903v1#S6.T2 "In Calibration stability over time (Figure 1). ‣ 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") reports regime-stratified exceedances, and [Figure 1](https://arxiv.org/html/2602.03903v1#S6.F1 "In Calibration and tightness (Table 1). ‣ 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") visualizes rolling one-year exceedance rates over time (GBDT base; the HS analogue is in [Figure 2](https://arxiv.org/html/2602.03903v1#A1.F2 "In Regime embedding used in experiments. ‣ Appendix A Implementation details ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")).

Table 1: Test-set exceedance results for 99% VaR (α=0.01\alpha=0.01) on the CRSP value-weighted index. Panel A uses a gradient boosting quantile base forecaster; Panel B uses historical simulation.

Panel A: Gradient boosting base (GBDT)

| Method | Exceedance (%) | Avg. VaR (bps) |
| --- | --- | --- |
| Base quantile model | 5.31 | 146 |
| SWC (rolling) | 1.37 | 182 |
| ACI | 1.14 | 200 |
| TWC (time decay) | 1.09 | 165 |
| RWC (time + regime) | 1.14 | 155 |

Panel B: Historical simulation base (HS)

| Method | Exceedance (%) | Avg. VaR (bps) |
| --- | --- | --- |
| Base quantile model | 1.71 | 317 |
| SWC (rolling) | 1.60 | 358 |
| ACI | 1.26 | 426 |
| TWC (time decay) | 1.48 | 339 |
| RWC (time + regime) | 1.09 | 247 |

#### Calibration and tightness ([Table 1](https://arxiv.org/html/2602.03903v1#S6.T1 "In 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")).

With the GBDT base (Panel A), the uncalibrated forecaster severely undercovers (5.31% exceedance at a 1% target). All wrappers bring exceedances close to target: SWC (1.37%), ACI (1.14%), TWC (1.09%), and RWC (1.14%). Differences are mainly in tightness: ACI is looser (Avg. VaR 200 bps) than weighted-quantile methods, while RWC matches ACI’s exceedance with a tighter average bound (155 bps). TWC is closest to target on average (1.09%) with Avg. VaR 165 bps.
With the HS base (Panel B), the uncalibrated model also undercovers (1.71%). Here regime weighting changes both calibration and tightness: RWC reduces exceedance to 1.09% while tightening the average bound (247 bps), compared to TWC (1.48%, 339 bps), SWC (1.60%, 358 bps), and ACI (1.26%, 426 bps), suggesting regime localization can matter when the base model is less adaptive.

![Refer to caption](figures/fig1_rolling_exceedance_shaded_gbdt.png)


Figure 1: Rolling 1-year exceedance rate for 99% VaR (α=0.01\alpha=0.01) on the CRSP value-weighted index (GBDT base). The dashed horizontal line indicates the target exceedance level. The dotted vertical line marks the start of the test period. Shaded regions indicate the 2008–2009 financial crisis and the 2020 COVID shock.

#### Calibration stability over time ([Figure 1](https://arxiv.org/html/2602.03903v1#S6.F1 "In Calibration and tightness (Table 1). ‣ 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")).

Average exceedance can mask transient miscalibration, which is particularly relevant for risk management. Rolling one-year exceedance rates therefore provide a stability diagnostic. Across the full sample, all methods vary over time (consistent with regime shifts), but conformal wrappers keep rolling exceedances much closer to the 1% target than an uncalibrated forecaster would. Methods emphasizing recency or feedback (TWC, ACI) tend to adapt more quickly, while stronger localization (RWC) can yield tighter bounds but may exhibit larger fluctuations when weights concentrate on a small subset of past observations. At α=1%\alpha=1\%, rolling 252-day exceedance rates are inherently noisy—each additional exceedance shifts the curve by 1/252≈0.4%1/252\approx 0.4\%—so spikes are interpreted mainly as a stability signal.

Table 2: Test-set exceedance rate (%) by realized-volatility quintile (Panel A: GBDT base; Panel B: HS base).

Panel A: Gradient boosting base (GBDT)

| Vol quintile | n | SWC | ACI | TWC | RWC |
| --- | --- | --- | --- | --- | --- |
| 0 | 351 | 0.28 | 0.57 | 0.28 | 1.14 |
| 1 | 350 | 1.43 | 1.43 | 0.57 | 0.29 |
| 2 | 350 | 1.14 | 0.86 | 0.86 | 0.86 |
| 3 | 350 | 1.71 | 1.14 | 1.43 | 1.14 |
| 4 | 350 | 2.29 | 1.71 | 2.29 | 2.29 |

Panel B: Historical simulation base (HS)

| Vol quintile | n | SWC | ACI | TWC | RWC |
| --- | --- | --- | --- | --- | --- |
| 0 | 351 | 0.00 | 0.00 | 0.00 | 0.00 |
| 1 | 350 | 0.57 | 0.57 | 0.57 | 0.57 |
| 2 | 350 | 1.43 | 0.86 | 1.43 | 0.86 |
| 3 | 350 | 2.29 | 1.71 | 1.71 | 1.14 |
| 4 | 350 | 3.71 | 3.14 | 3.71 | 2.86 |

#### Regime-conditional exceedance ([Table 2](https://arxiv.org/html/2602.03903v1#S6.T2 "In Calibration stability over time (Figure 1). ‣ 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")).

With the GBDT base (Panel A), exceedances rise with realized volatility for all methods, and the top-volatility quintile remains above the 1% target even after calibration. ACI is lowest in the top quintile (1.71%), while SWC/TWC/RWC are at 2.29%. In low-volatility regimes, methods tend to be conservative; for example in quintile 0, SWC/TWC are at 0.28% and ACI at 0.57%, while RWC is closer to target at 1.14% but slightly overshoots. Overall, with a flexible base forecaster, recency weighting and feedback-style adaptation appear to dominate incremental gains from regime similarity in stress.
With the HS base (Panel B), regime weighting shows its clearest benefit in stress: in the top volatility quintile, RWC reduces exceedance to 2.86% versus 3.14% (ACI) and 3.71% (SWC/TWC). This is consistent with bias–variance tradeoffs: when the base model adapts slowly, emphasizing regime-similar history can reduce systematic undercoverage in high-volatility states.

#### When does regime weighting help?

The mixed behavior across base forecasters aligns with the localization–variance tradeoff in [Theorem 5.4](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem4 "Theorem 5.4 (Approximate regime-conditional coverage under smooth drift (informal)). ‣ Effective weighted sample size. ‣ 5.2 Regime-conditional coverage under drift ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"). Regime weighting can reduce bias by emphasizing regimes closer to the current ztz\_{t} (the O​(Lz​h)O(L\_{z}h) term), but can increase variance by reducing the effective sample size neff​(t)n\_{\mathrm{eff}}(t) (the O​(1/neff​(t))O(\sqrt{1/n\_{\mathrm{eff}}(t)}) term). When the base model is already flexible (GBDT), time decay alone often tracks much of the drift, so additional localization may mostly reduce neff​(t)n\_{\mathrm{eff}}(t) and increase quantile noise. When the base model is simpler (HS), bias reduction from regime localization can dominate, improving both average and stress-regime calibration. Practically, this motivates TWC as a robust default, with RWC as a targeted option when regime-conditional stability is a priority.

### 6.5 Diagnostics and Sensitivity

Table 3: Regime-stability summary derived from volatility-quintile exceedances ([Table 2](https://arxiv.org/html/2602.03903v1#S6.T2 "In Calibration stability over time (Figure 1). ‣ 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")). Metrics are in percentage points (pp) relative to the target exceedance level α=0.01\alpha=0.01 (1%).

Panel A: GBDT base

| Method | Reg-MAE (pp) | Reg-MaxDev (pp) | Reg-Std (pp) |
| --- | --- | --- | --- |
| SWC | 0.66 | 1.29 | 0.66 |
| ACI | 0.37 | 0.71 | 0.40 |
| TWC | 0.60 | 1.29 | 0.71 |
| RWC | 0.49 | 1.29 | 0.65 |

Panel B: HS base

| Method | Reg-MAE (pp) | Reg-MaxDev (pp) | Reg-Std (pp) |
| --- | --- | --- | --- |
| SWC | 1.17 | 2.71 | 1.31 |
| ACI | 0.89 | 2.14 | 1.09 |
| TWC | 1.06 | 2.71 | 1.27 |
| RWC | 0.71 | 1.86 | 0.96 |

#### Regime-stability summary.

Volatility-quintile exceedances ([Table 2](https://arxiv.org/html/2602.03903v1#S6.T2 "In Calibration stability over time (Figure 1). ‣ 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")) provide a stratified view of calibration; to summarize stability in one line per method, let e^k\hat{e}\_{k} be the exceedance rate (in %) in volatility quintile k∈{0,…,4}k\in\{0,\dots,4\} and let e⋆=1e^{\star}=1 be the target (in % units). Define Δk=e^k−e⋆\Delta\_{k}=\hat{e}\_{k}-e^{\star} (percentage points). Reg-MAE =15​∑k|Δk|=\frac{1}{5}\sum\_{k}|\Delta\_{k}|, Reg-MaxDev =maxk⁡|Δk|=\max\_{k}|\Delta\_{k}|, and Reg-Std =Std​({Δk}k)=\mathrm{Std}(\{\Delta\_{k}\}\_{k}) are reported.

Table 4: Diagnostics for weighted calibration. We report effective weighted sample size neff​(t)n\_{\mathrm{eff}}(t) and effective memory τt\tau\_{t} (days) over the test period, summarizing the localization–variance tradeoff in [Theorem 5.4](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem4 "Theorem 5.4 (Approximate regime-conditional coverage under smooth drift (informal)). ‣ Effective weighted sample size. ‣ 5.2 Regime-conditional coverage under drift ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").

Panel A: GBDT base

mm
Method


med
neffn\_{\mathrm{eff}}


p10
neffn\_{\mathrm{eff}}


med
τ\tau (days)


p90
τ\tau (days)


252
SWC
252.0
252.0
126.5
126.5

252
ACI
252.0
252.0
126.5
126.5

756
TWC
382.2
382.2
182.8
182.8

756
RWC
271.1
186.1
174.4
199.5

Panel B: HS base

mm
Method


med
neffn\_{\mathrm{eff}}


p10
neffn\_{\mathrm{eff}}


med
τ\tau (days)


p90
τ\tau (days)


252
SWC
252.0
252.0
126.5
126.5

252
ACI
252.0
252.0
126.5
126.5

756
TWC
199.8
199.8
100.1
100.1

756
RWC
180.8
151.4
96.0
103.6

#### Effective sample size and effective memory.

To connect empirical behavior to [Theorem 5.4](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem4 "Theorem 5.4 (Approximate regime-conditional coverage under smooth drift (informal)). ‣ Effective weighted sample size. ‣ 5.2 Regime-conditional coverage under drift ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"), Table [4](https://arxiv.org/html/2602.03903v1#S6.T4 "Table 4 ‣ Regime-stability summary. ‣ 6.5 Diagnostics and Sensitivity ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") summarizes neff​(t)n\_{\mathrm{eff}}(t) and effective memory τt\tau\_{t} over the test period. Stronger localization (smaller hh in RWC) concentrates weights on fewer past observations, lowering neff​(t)n\_{\mathrm{eff}}(t) (more quantile noise) and altering τt\tau\_{t} (the effective temporal horizon). These diagnostics help identify when regime weighting is beneficial versus overly variable.

Table 5: VaR backtesting diagnostics on the test period: Kupiec unconditional coverage (UC) and Christoffersen independence (IND) and conditional coverage (CC) tests applied to exceedance indicators. Note: Kupiec’s UC statistic depends only on the total number of exceedances (given NN), so methods with the same exceedance count can share identical UC values even if violation timing differs.

Panel A: GBDT base

Method
Exceedance (%)
Avg. VaR (bps)
N
Exc
LRuc
puc
LRind
pind
LRcc
pcc


Base
5.31
146
1751
93
162.94
2.57e-37
6.36
0.012
169.31
1.72e-37

SWC
1.37
182
1751
24
2.18
0.140
4.12
0.042
6.30
0.043

ACI
1.14
200
1751
20
0.34
0.559
0.46
0.496
0.80
0.669

TWC
1.09
165
1751
19
0.12
0.724
1.64
0.201
1.76
0.414

RWC
1.14
155
1751
20
0.34
0.559
1.47
0.225
1.81
0.404

Panel B: HS base

Method
Exceedance (%)
Avg. VaR (bps)
N
Exc
LRuc
puc
LRind
pind
LRcc
pcc


Base
1.71
317
1751
30
7.42
0.006
2.61
0.106
10.03
0.007

SWC
1.60
358
1751
28
5.37
0.021
6.80
0.009
12.17
0.002

ACI
1.26
426
1751
22
1.08
0.300
9.57
0.002
10.65
0.005

TWC
1.48
339
1751
26
3.62
0.057
3.56
0.059
7.18
0.028

RWC
1.09
247
1751
19
0.12
0.724
5.85
0.016
5.98
0.050

#### Backtesting diagnostics.

As a secondary check, standard VaR backtests are applied to test-period exceedance indicators (Table [5](https://arxiv.org/html/2602.03903v1#S6.T5 "Table 5 ‣ Effective sample size and effective memory. ‣ 6.5 Diagnostics and Sensitivity ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")). These tests complement average exceedance by detecting systematic miscoverage (UC) and clustering of violations (IND/CC). In nonstationary financial data, strict independence is best viewed as a diagnostic rather than a hard requirement; the primary objective is sequential exceedance control and regime-conditional stability.

Table 6: Bandwidth sweep ablation for RWC: decreasing hh strengthens regime localization; as h→∞h\to\infty, RWC reduces to its time-weighted limit (TWC with the same m,λm,\lambda).

Panel A: GBDT base

Setting
Exceed (%)
Avg. VaR (bps)
Top-vol Exceed (%)
median neffn\_{\mathrm{eff}}
p10 neffn\_{\mathrm{eff}}


hh = 0.5
1.20
152
2.29
231.1
122.1

hh = 1
1.14
155
2.29
271.1
186.1

hh = 2
1.31
152
2.57
343.1
302.2

hh = ∞\infty (TWC limit)
1.09
165
2.29
382.2
382.2

Panel B: HS base

Setting
Exceed (%)
Avg. VaR (bps)
Top-vol Exceed (%)
median neffn\_{\mathrm{eff}}
p10 neffn\_{\mathrm{eff}}


hh = 0.5
1.48
212
3.71
99.0
44.6

hh = 1
1.09
209
3.71
142.2
80.9

hh = 2
1.09
247
2.86
180.8
151.4

hh = ∞\infty (TWC limit)
1.48
339
3.71
199.8
199.8

#### Bandwidth sweep.

Regime-localization strength is ablated by sweeping the kernel bandwidth hh while holding (m,λ)(m,\lambda) fixed. As h→∞h\to\infty, the regime-similarity term becomes constant and RWC reduces to the corresponding time-weighted limit (TWC with the same m,λm,\lambda). The sweep uses the same ESS safeguard: when hh is small and neff​(t)<nminn\_{\mathrm{eff}}(t)<n\_{\min}, the procedure reverts to time-only weights for that step. Table [6](https://arxiv.org/html/2602.03903v1#S6.T6 "Table 6 ‣ Backtesting diagnostics. ‣ 6.5 Diagnostics and Sensitivity ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR") reports overall exceedance, average tightness, stress-regime exceedance (top volatility quintile), and neffn\_{\mathrm{eff}} summaries across bandwidths, making the localization–variance tradeoff explicit. To isolate the effect of hh, the h=∞h=\infty row corresponds to the *TWC limit under fixed (m,λ)(m,\lambda)* and may differ from separately tuned TWC results in [Table 1](https://arxiv.org/html/2602.03903v1#S6.T1 "In 6.4 Results ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").

## 7 Limitations

The guarantees rely on assumptions (weighted exchangeability or smooth drift) that are only approximations in real markets. The focus is on one-step-ahead risk for a liquid equity index; extending to multi-period horizons, illiquid assets, or portfolios with market impact introduces additional dependence and feedback effects. Finally, CRSP is proprietary; reproducible code and data-pull scripts are provided for credentialed users.

Because exact distribution-free conditional coverage is impossible in general (Barber et al., [2021](https://arxiv.org/html/2602.03903v1#bib.bib20 "The limits of distribution-free conditional predictive inference")), regime-conditional guarantees are necessarily approximate and depend on the informativeness of the regime embedding ztz\_{t} and the effective local sample size induced by the weights.

## 8 Conclusion

Sequential one-sided VaR control under nonstationarity and regime structure via conformal calibration is studied. RWC is introduced, which calibrates additive safety buffers using time decay and optional regime-similarity weighting, enabling regime-aware calibration while remaining model agnostic. Empirically, TWC is a strong default under drift, and regime weighting can further improve regime-conditional stability in some settings with modest changes in conservativeness. Overall, conformal calibration provides a practical and modular reliability layer for financial risk forecasting pipelines.

## Impact Statement

This work aims to improve the reliability of statistical risk controls used in financial decision-making. Better-calibrated tail risk estimates may reduce the likelihood of excessive risk-taking and improve resilience to market stress. However, risk models can also be used to scale leverage; if misused, they may contribute to systemic risk. Transparent evaluation across regimes is therefore emphasized, and code and data construction details are released to facilitate auditing and responsible deployment.

## References

* T. Adrian and H. S. Shin (2014)
  Procyclical leverage and value-at-risk.
  The Review of Financial Studies 27 (2),  pp. 373–403.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hht068)
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p1.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* A. N. Angelopoulos, S. Bates, A. Fisch, L. Lei, and T. Schuster (2024)
  Conformal risk control.
  In International Conference on Learning Representations,
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p2.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§2](https://arxiv.org/html/2602.03903v1#S2.p2.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* A. N. Angelopoulos, E. J. Candès, and R. J. Tibshirani (2023)
  Conformal pid control for time series prediction.
  In Advances in Neural Information Processing Systems,
  Vol. 36,  pp. 23047–23074.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p3.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani (2021)
  The limits of distribution-free conditional predictive inference.
  Information and Inference: A Journal of the IMA.
  External Links: [Document](https://dx.doi.org/10.1093/imaiai/iaaa017)
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p5.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§7](https://arxiv.org/html/2602.03903v1#S7.p2.1 "7 Limitations ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani (2023)
  Conformal prediction beyond exchangeability.
  The Annals of Statistics 51 (2),  pp. 816–845.
  External Links: [Document](https://dx.doi.org/10.1214/23-AOS2276)
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p4.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§4.1](https://arxiv.org/html/2602.03903v1#S4.SS1.SSS0.Px2.p1.1 "Weighted conformal inference. ‣ 4.1 Regime representation and weighting ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§5](https://arxiv.org/html/2602.03903v1#S5.p1.1 "5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* S. Basak and A. Shapiro (2001)
  Value-at-risk-based risk management: optimal policies and asset prices.
  The Review of Financial Studies 14 (2),  pp. 371–405.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/14.2.371)
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p1.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* J. Berkowitz and J. O’Brien (2002)
  How accurate are value-at-risk models at commercial banks?.
  The Journal of Finance 57 (3),  pp. 1093–1111.
  External Links: [Document](https://dx.doi.org/10.1111/1540-6261.00455)
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p1.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§2](https://arxiv.org/html/2602.03903v1#S2.p6.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* P. F. Christoffersen (1998)
  Evaluating interval forecasts.
  International Economic Review 39 (4),  pp. 841–862.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p6.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§6.3](https://arxiv.org/html/2602.03903v1#S6.SS3.p1.2 "6.3 Metrics ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* L. Ding, U. Hébert-Johnson, R. Wang, and R. J. Tibshirani (2023)
  Class-conditional conformal prediction with many classes.
  In Advances in Neural Information Processing Systems,
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p5.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* R. F. Engle and S. Manganelli (2004)
  CAViaR: conditional autoregressive value at risk by regression quantiles.
  Journal of Business & Economic Statistics 22 (4),  pp. 367–381.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p6.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* R. F. Engle and J. G. Rangel (2008)
  The spline-garch model for low-frequency volatility and its global macroeconomic causes.
  The Review of Financial Studies 21 (3),  pp. 1187–1222.
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p1.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* I. Gibbs and E. J. Candès (2021)
  Adaptive conformal inference under distribution shift.
  In Advances in Neural Information Processing Systems,
  Vol. 34,  pp. 1660–1672.
  Cited by: [Appendix A](https://arxiv.org/html/2602.03903v1#A1.SS0.SSS0.Px5.p1.3 "ACI baseline details. ‣ Appendix A Implementation details ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§1](https://arxiv.org/html/2602.03903v1#S1.p2.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§2](https://arxiv.org/html/2602.03903v1#S2.p3.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§4.3](https://arxiv.org/html/2602.03903v1#S4.SS3.p1.2 "4.3 Baselines ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§6.2](https://arxiv.org/html/2602.03903v1#S6.SS2.SSS0.Px2.p1.1 "Conformal wrappers. ‣ 6.2 Models and calibrators ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* I. Gibbs and E. J. Candès (2024)
  Conformal inference for online prediction with arbitrary distribution shifts.
  Journal of Machine Learning Research 25 (86),  pp. 1–36.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p4.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* S. F. Gray (1996)
  Modeling the conditional distribution of interest rates as a regime-switching process.
  Journal of Financial Economics 42 (1),  pp. 27–62.
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p1.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* L. Guan (2023)
  Conformal prediction with localization.
  Biometrika 110 (1).
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p5.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* J. D. Hamilton (1989)
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  Econometrica 57 (2),  pp. 357–384.
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p1.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* P. H. Kupiec (1995)
  Techniques for verifying the accuracy of risk measurement models.
  Journal of Derivatives 3 (2),  pp. 73–84.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p6.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§6.3](https://arxiv.org/html/2602.03903v1#S6.SS3.p1.2 "6.3 Metrics ‣ 6 Experiments ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* R. T. Rockafellar and S. Uryasev (2000)
  Optimization of conditional value-at-risk.
  Journal of Risk 2 (3),  pp. 21–41.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p6.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* Y. Romano, E. Patterson, and E. J. Candès (2019)
  Conformalized quantile regression.
  In Advances in Neural Information Processing Systems,
  Vol. 32,  pp. 3538–3548.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p1.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* G. Shafer and V. Vovk (2008)
  A tutorial on conformal prediction.
  Journal of Machine Learning Research 9,  pp. 371–421.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p1.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* J. C. Snell and T. L. Griffiths (2025)
  Conformal prediction as Bayesian quadrature.
  In Proceedings of the 42nd International Conference on Machine Learning, A. Singh, M. Fazel, D. Hsu, S. Lacoste-Julien, F. Berkenkamp, T. Maharaj, K. Wagstaff, and J. Zhu (Eds.),
  Proceedings of Machine Learning Research, Vol. 267,  pp. 56068–56084.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p2.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* R. J. Tibshirani, R. Foygel Barber, E. J. Candès, and A. Ramdas (2019)
  Conformal prediction under covariate shift.
  Advances in Neural Information Processing Systems 32.
  Cited by: [Appendix B](https://arxiv.org/html/2602.03903v1#A2.SS0.SSS0.Px1.p1.4 "Proof sketch for Theorem 5.2. ‣ Appendix B Proofs ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [Appendix B](https://arxiv.org/html/2602.03903v1#A2.SS0.SSS0.Px3.p1.5 "Remark (finite-sample correction). ‣ Appendix B Proofs ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§1](https://arxiv.org/html/2602.03903v1#S1.p2.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§2](https://arxiv.org/html/2602.03903v1#S2.p1.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§4.1](https://arxiv.org/html/2602.03903v1#S4.SS1.SSS0.Px2.p1.1 "Weighted conformal inference. ‣ 4.1 Regime representation and weighting ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [Assumption 5.1](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem1.p1.3 "Assumption 5.1 (Weighted exchangeability). ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§5](https://arxiv.org/html/2602.03903v1#S5.p1.1 "5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* V. Vovk, A. Gammerman, and G. Shafer (2005)
  Algorithmic learning in a random world.
   Springer, New York.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p1.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* C. Xu and Y. Xie (2021)
  Conformal prediction interval for dynamic time-series.
  In Proceedings of the 38th International Conference on Machine Learning,
  Proceedings of Machine Learning Research, Vol. 139,  pp. 11559–11569.
  Cited by: [§1](https://arxiv.org/html/2602.03903v1#S1.p2.1 "1 Introduction ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"),
  [§2](https://arxiv.org/html/2602.03903v1#S2.p3.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").
* C. Xu and Y. Xie (2023)
  Sequential predictive conformal inference for time series.
  In Proceedings of the 40th International Conference on Machine Learning,
  Proceedings of Machine Learning Research, Vol. 202,  pp. 38707–38727.
  Cited by: [§2](https://arxiv.org/html/2602.03903v1#S2.p3.1 "2 Background and related work ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").

## Appendix A Implementation details

#### Weighted quantile and finite-sample correction.

Given values v1,…,vnv\_{1},\dots,v\_{n} and nonnegative weights w~i\tilde{w}\_{i} summing to one, the weighted γ\gamma-quantile is

|  |  |  |
| --- | --- | --- |
|  | Qγw~​({vi}):=inf{q∈ℝ:∑i=1nw~i​𝟏​{vi≤q}≥γ}.Q^{\tilde{w}}\_{\gamma}(\{v\_{i}\}):=\inf\left\{q\in\mathbb{R}:\sum\_{i=1}^{n}\tilde{w}\_{i}\mathbf{1}\{v\_{i}\leq q\}\geq\gamma\right\}. |  |

We implement this via sorting viv\_{i} and accumulating the sorted weights until the cumulative mass exceeds γ\gamma.

At time tt, let wi​(t)≥0w\_{i}(t)\geq 0 be the unnormalized calibration weights for i∈ℐti\in\mathcal{I}\_{t} (as in ([3](https://arxiv.org/html/2602.03903v1#S4.E3 "Equation 3 ‣ 4.1 Regime representation and weighting ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"))),
and define Wt:=∑i∈ℐtwi​(t)W\_{t}:=\sum\_{i\in\mathcal{I}\_{t}}w\_{i}(t) and normalized weights w~i​(t):=wi​(t)/Wt\tilde{w}\_{i}(t):=w\_{i}(t)/W\_{t}.
Let wt​(t)w\_{t}(t) denote the weight assigned to the current test point (for ([3](https://arxiv.org/html/2602.03903v1#S4.E3 "Equation 3 ‣ 4.1 Regime representation and weighting ‣ 4 Method: Regime-weighted conformal calibration ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")), wt​(t)=1w\_{t}(t)=1).
For exact finite-sample weighted conformal coverage (Theorem [5.2](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem2 "Theorem 5.2 (Finite-sample weighted coverage). ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")) one can use the inflated level

|  |  |  |
| --- | --- | --- |
|  | ρt:=min⁡{1,(1−α)​(1+wt​(t)Wt)},\rho\_{t}:=\min\left\{1,\;(1-\alpha)\Big(1+\frac{w\_{t}(t)}{W\_{t}}\Big)\right\}, |  |

and set c^t:=Qρtw~​(t)​({si}i∈ℐt)\hat{c}\_{t}:=Q^{\tilde{w}(t)}\_{\rho\_{t}}(\{s\_{i}\}\_{i\in\mathcal{I}\_{t}}) and Ut:=q^t+c^tU\_{t}:=\hat{q}\_{t}+\hat{c}\_{t}.
In the experiments we use ρt=1−α\rho\_{t}=1-\alpha for simplicity; when WtW\_{t} (or neff​(t)n\_{\mathrm{eff}}(t)) is large the practical difference is negligible.

#### Effective weighted sample size and effective memory.

We define the effective weighted sample size

|  |  |  |
| --- | --- | --- |
|  | neff​(t):=1∑i∈ℐtw~i​(t)2,n\_{\mathrm{eff}}(t):=\frac{1}{\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)^{2}}, |  |

and the effective lag (effective memory) under the normalized weights

|  |  |  |
| --- | --- | --- |
|  | τt:=∑i∈ℐtw~i​(t)​(t−i).\tau\_{t}:=\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)\,(t-i). |  |

#### ESS safeguard (implementation).

Regime localization can concentrate weights on a small subset of past observations, reducing the effective calibration sample size
neff​(t)=1/∑i∈ℐtw~i​(t)2n\_{\mathrm{eff}}(t)=1\big/\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)^{2}
and increasing quantile-estimation variance (cf. Theorem 5.4).
To prevent unstable calibration when locally relevant history is limited, we apply an ESS safeguard:
if neff​(t)<nminn\_{\mathrm{eff}}(t)<n\_{\min} we drop the regime kernel for that step (set Kh≡1K\_{h}\equiv 1) and compute the calibration quantile using time-only weights (i.e., the TWC weights) for that step.
In our experiments we use nmin=100n\_{\min}=100 for the GBDT base and nmin=30n\_{\min}=30 for the HS base.

#### Regime embedding used in experiments.

In all experiments we use a two-dimensional regime embedding zt=(RV21t,MAR5t)z\_{t}=(\mathrm{RV21}\_{t},\mathrm{MAR5}\_{t}) computed from lagged portfolio returns:

|  |  |  |
| --- | --- | --- |
|  | RV21t:=252​Std​(rt−21:t−1port),MAR5t:=15​∑j=15|rt−jport|.\mathrm{RV21}\_{t}:=\sqrt{252}\,\mathrm{Std}\!\left(r^{\text{port}}\_{t-21:t-1}\right),\qquad\\ \mathrm{MAR5}\_{t}:=\frac{1}{5}\sum\_{j=1}^{5}\left|r^{\text{port}}\_{t-j}\right|. |  |

Both features use only information available up through time t−1t{-}1 (consistent with the timing convention in Section 3). Before computing KhK\_{h}, each coordinate of ztz\_{t} is standardized to zero mean and unit variance using pre-test statistics.

![Refer to caption](figures/fig1_rolling_exceedance_shaded_hs.png)


Figure 2: Rolling 1-year exceedance rate for 99% VaR (α=0.01\alpha=0.01) on the CRSP value-weighted index (HS base). The dashed horizontal line indicates the target exceedance level. The dotted vertical line marks the start of the test period. Shaded regions indicate the 2008–2009 financial crisis and the 2020 COVID shock.




Table 7: Hyperparameters used in the main experiments (selected on the validation period).
For TWC, h=∞h=\infty denotes no regime weighting (Kh≡1K\_{h}\equiv 1).
For SWC/ACI, λ\lambda and hh are not used (uniform weights within the sliding window).
For RWC we additionally use an effective-sample-size safeguard: if neff​(t)<neff,minn\_{\mathrm{eff}}(t)<n\_{\mathrm{eff,min}},
we fall back to TWC weights for that time tt.

| Base | Method | mm | λ\lambda | hh | γ\gamma (ACI) | neff,minn\_{\mathrm{eff,min}} |
| --- | --- | --- | --- | --- | --- | --- |
| GBDT | SWC | 252 | – | – | – | – |
| GBDT | TWC | 756 | 0.005 | ∞\infty | – | – |
| GBDT | RWC | 756 | 0.005 | 1.0 | – | 100 |
| GBDT | ACI | 252 | – | – | 0.005 | – |
| HS | SWC | 252 | – | – | – | – |
| HS | TWC | 756 | 0.010 | ∞\infty | – | – |
| HS | RWC | 756 | 0.010 | 2.0 | – | 30 |
| HS | ACI | 252 | – | – | 0.002 | – |

#### ACI baseline details.

We implement ACI following Gibbs and Candès ([2021](https://arxiv.org/html/2602.03903v1#bib.bib12 "Adaptive conformal inference under distribution shift")) using a sliding calibration window of size m=252m=252 and an adaptive miscoverage level αt\alpha\_{t}.
Initialize αt0=α\alpha\_{t\_{0}}=\alpha and update

|  |  |  |
| --- | --- | --- |
|  | αt+1=Π[αmin,αmax]​(αt+γ​(α−𝟏​{yt>Ut})),\alpha\_{t+1}=\Pi\_{[\alpha\_{\min},\alpha\_{\max}]}\!\left(\alpha\_{t}+\gamma\left(\alpha-\mathbf{1}\{y\_{t}>U\_{t}\}\right)\right), |  |

where Π\Pi clips to [αmin,αmax][\alpha\_{\min},\alpha\_{\max}] (we use αmin=10−4\alpha\_{\min}=10^{-4} and αmax=0.2\alpha\_{\max}=0.2) and γ\gamma is tuned on validation using the same criterion as above.
At time tt, ACI computes c^t\hat{c}\_{t} as the empirical (1−αt)(1-\alpha\_{t})-quantile of the last mm conformity scores.

## Appendix B Proofs

#### Proof sketch for Theorem [5.2](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem2 "Theorem 5.2 (Finite-sample weighted coverage). ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").

Fix time tt and condition on (xt,zt)(x\_{t},z\_{t}). Under weighted exchangeability (Assumption [5.1](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem1 "Assumption 5.1 (Weighted exchangeability). ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")), the joint distribution of the weighted multiset
{(si,wi​(t))}i∈ℐt∪{(st,wt​(t))}\{(s\_{i},w\_{i}(t))\}\_{i\in\mathcal{I}\_{t}}\cup\{(s\_{t},w\_{t}(t))\} is invariant to permutations.
Following Tibshirani et al. ([2019](https://arxiv.org/html/2602.03903v1#bib.bib47 "Conformal prediction under covariate shift")), define the (randomized) weighted conformal pp-value for the one-sided score as

|  |  |  |
| --- | --- | --- |
|  | pt:=∑i∈ℐtwi​(t)​ 1​{si≥st}+wt​(t)​UWt+wt​(t),p\_{t}:=\frac{\sum\_{i\in\mathcal{I}\_{t}}w\_{i}(t)\,\mathbf{1}\{s\_{i}\geq s\_{t}\}\;+\;w\_{t}(t)\,U}{W\_{t}+w\_{t}(t)}, |  |

where U∼Unif​(0,1)U\sim\mathrm{Unif}(0,1) is independent and breaks ties. Weighted exchangeability implies ptp\_{t} is super-uniform, i.e., ℙ​(pt≤α∣xt,zt)≤α\mathbb{P}(p\_{t}\leq\alpha\mid x\_{t},z\_{t})\leq\alpha. Equivalently, with probability at least 1−α1-\alpha, the test score sts\_{t} is not in the upper α\alpha-tail of the weighted empirical distribution.
The choice of ρt\rho\_{t} in ([5](https://arxiv.org/html/2602.03903v1#S5.E5 "Equation 5 ‣ Notation. ‣ 5.1 Exact coverage under weighted exchangeability ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")) (implemented in Appendix [A](https://arxiv.org/html/2602.03903v1#A1 "Appendix A Implementation details ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR")) corresponds exactly to the acceptance region {pt>α}\{p\_{t}>\alpha\},
which yields ℙ​(st≤c^t∣xt,zt)≥1−α\mathbb{P}(s\_{t}\leq\hat{c}\_{t}\mid x\_{t},z\_{t})\geq 1-\alpha. Since st=yt−q^ts\_{t}=y\_{t}-\hat{q}\_{t}, the event st≤c^ts\_{t}\leq\hat{c}\_{t} is equivalent to yt≤q^t+c^t=Uty\_{t}\leq\hat{q}\_{t}+\hat{c}\_{t}=U\_{t}, proving the claim.

#### Proof sketch for Theorem [5.4](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem4 "Theorem 5.4 (Approximate regime-conditional coverage under smooth drift (informal)). ‣ Effective weighted sample size. ‣ 5.2 Regime-conditional coverage under drift ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR").

Let

|  |  |  |
| --- | --- | --- |
|  | F^tw​(u):=∑i∈ℐtw~i​(t)​ 1​{si≤u}\hat{F}^{w}\_{t}(u):=\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)\,\mathbf{1}\{s\_{i}\leq u\} |  |

be the weighted empirical CDF of scores, and compare it to the target conditional score CDF Ft​(u∣zt)F\_{t}(u\mid z\_{t}).

*(Bias due to regime mismatch and time drift.)*
Add and subtract Fi​(u∣zt)F\_{i}(u\mid z\_{t}) and apply the triangle inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼[F^tw(u)]−Ft(u∣zt)|≤\displaystyle\Big|\mathbb{E}\!\big[\hat{F}^{w}\_{t}(u)\big]-F\_{t}(u\mid z\_{t})\Big|\;\leq | ∑i∈ℐtw~i(t)|Fi(u∣zi)−Fi(u∣zt)|\displaystyle\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)\,\Big|F\_{i}(u\mid z\_{i})-F\_{i}(u\mid z\_{t})\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑i∈ℐtw~i(t)|Fi(u∣zt)−Ft(u∣zt)|.\displaystyle+\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)\,\Big|F\_{i}(u\mid z\_{t})-F\_{t}(u\mid z\_{t})\Big|. |  |

By Assumption [5.3](https://arxiv.org/html/2602.03903v1#S5.Thmtheorem3 "Assumption 5.3 (Smooth regime drift and gradual time variation). ‣ 5.2 Regime-conditional coverage under drift ‣ 5 Theory ‣ Taming Tail Risk in Financial Markets: Conformal Risk Control for Nonstationary Portfolio VaR"), the first term is bounded by
Lz​∑i∈ℐtw~i​(t)​‖zi−zt‖=O​(Lz​h)L\_{z}\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)\|z\_{i}-z\_{t}\|=O(L\_{z}h) (kernel concentration), and the second term is bounded by
Lt​∑i∈ℐtw~i​(t)​(t−i)=Lt​τtL\_{t}\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)(t-i)=L\_{t}\,\tau\_{t} (by definition).
Thus the bias is of order O​(Lz​h)+O​(Lt​τt)O(L\_{z}h)+O(L\_{t}\tau\_{t}).

*(Stochastic term controlled by effective sample size.)*
For each fixed uu, F^tw​(u)\hat{F}^{w}\_{t}(u) is a weighted average of bounded random variables. Under conditional independence (or sufficiently weak dependence, e.g. standard mixing), concentration for weighted sums yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |F^tw​(u)−𝔼​[F^tw​(u)]|\displaystyle\Big|\hat{F}^{w}\_{t}(u)-\mathbb{E}\!\big[\hat{F}^{w}\_{t}(u)\big]\Big| | =O​(∑i∈ℐtw~i​(t)2)\displaystyle=O\!\left(\sqrt{\sum\_{i\in\mathcal{I}\_{t}}\tilde{w}\_{i}(t)^{2}}\right) | =O​(1neff​(t)),\displaystyle=O\!\left(\sqrt{\frac{1}{n\_{\mathrm{eff}}(t)}}\right), |  |

up to log factors for uniform-in-uu control.

*(CDF error ⇒\Rightarrow quantile error ⇒\Rightarrow coverage gap.)*
Under mild regularity (e.g., local continuity / positive slope of Ft(⋅∣zt)F\_{t}(\cdot\mid z\_{t}) near the target quantile),
a bound on supu|F^tw(u)−Ft(u∣zt)|\sup\_{u}\big|\hat{F}^{w}\_{t}(u)-F\_{t}(u\mid z\_{t})\big| implies a corresponding bound on the weighted-quantile error for c^t\hat{c}\_{t}
and hence on ℙ​(st≤c^t∣zt)\mathbb{P}(s\_{t}\leq\hat{c}\_{t}\mid z\_{t}).
Translating back via st=yt−q^ts\_{t}=y\_{t}-\hat{q}\_{t} yields the stated coverage bound with
εt=O​(Lz​h)+O​(Lt​τt)+O​(1/neff​(t))\varepsilon\_{t}=O(L\_{z}h)+O(L\_{t}\tau\_{t})+O\!\big(\sqrt{1/n\_{\mathrm{eff}}(t)}\big).

#### Remark (finite-sample correction).

Weighted conformal validity statements typically use a small finite-sample correction to the quantile level that depends on the total calibration weight WtW\_{t}
(and the test-point weight), analogous to the (m+1)(m{+}1) correction in standard conformal prediction (Tibshirani et al., [2019](https://arxiv.org/html/2602.03903v1#bib.bib47 "Conformal prediction under covariate shift")).
In our experiments we use the simpler level 1−α1-\alpha; when WtW\_{t} (or neff​(t)n\_{\mathrm{eff}}(t)) is large, the difference is negligible.