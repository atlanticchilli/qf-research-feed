---
authors:
- Abdulrahman Alswaidan
- Jeffrey D. Varner
doc_id: arxiv:2603.10202v1
family_id: arxiv:2603.10202
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics:
  A Discrete-State Approach with Jump-Diffusion'
url_abs: http://arxiv.org/abs/2603.10202v1
url_html: https://arxiv.org/html/2603.10202v1
venue: arXiv q-fin
version: 1
year: 2026
---


Abdulrahman Alswaidan
Cornell UniversityRobert Frederick Smith School of Chemical and Biomolecular EngineeringIthacaNY14853USA
 and 
Jeffrey Varner
Cornell UniversityRobert Frederick Smith School of Chemical and Biomolecular EngineeringIthacaNY14853USA
[jdv27@cornell.edu](2603.10202v1/mailto:jdv27@cornell.edu)

###### Abstract.

Generating synthetic financial time series that preserve the statistical properties of real market data is essential for stress testing, risk model validation, and scenario design, yet existing approaches, from parametric models to deep generative networks, struggle to simultaneously reproduce the heavy-tailed distributions, negligible linear autocorrelation, and persistent volatility clustering that characterize empirical equity data. We propose a hybrid hidden Markov framework that discretizes continuous excess growth rates into Laplace quantile-defined market states and augments the regime-switching process with a Poisson-driven jump-duration mechanism to enforce realistic tail-state dwell times. Parameters are estimated by direct transition counting, avoiding the Baum-Welch EM algorithm entirely. We evaluate synthetic data quality using three complementary metrics: Kolmogorov-Smirnov and Anderson-Darling goodness-of-fit pass rates for distributional fidelity, and ACF mean absolute error for temporal structure preservation. Applied to ten years of SPY data across 1,000 simulated paths, the framework achieves KS and AD pass rates exceeding 97% and 91% in-sample and 94% out-of-sample (full calendar year 2025), partially reproducing the ARCH effect that standard regime-switching models miss. No single model dominates all quality dimensions: GARCH(1,1) reproduces volatility clustering more accurately but fails distributional tests (5.5% KS pass rate), while the standard HMM without jumps achieves higher distributional fidelity but cannot generate persistent high-volatility regimes. The proposed hybrid framework offers the best joint quality profile across distributional, temporal, and tail-coverage metrics among the parametric models evaluated. A Single-Index Model extension propagates the SPY factor path to a 424-asset universe, enabling scalable correlated synthetic path generation while preserving cross-sectional correlation structure.

Synthetic Data Quality, Time Series Generation, Hidden Markov Model, Jump-Diffusion, Volatility Clustering, Regime-Switching, Stylized Facts, Distributional Fidelity

††copyright: none

## 1. Introduction

Generating synthetic financial time series that faithfully preserve the statistical properties of real market data is a central challenge in quantitative finance and data quality research. High-fidelity synthetic data are essential for stress testing risk models against plausible but unobserved market scenarios, validating portfolio optimization algorithms, and augmenting limited training sets for machine learning pipelines (Assefa et al., [2020](#bib.bib24 "Generating synthetic data in finance: opportunities, challenges and pitfalls"); Jordon et al., [2022](#bib.bib58 "Synthetic data – what, why and how?")). Yet the quality requirements for financial synthetic data are unusually demanding: empirical equity excess growth rates exhibit three well-documented statistical regularities, namely heavy-tailed (leptokurtic) distributions, negligible linear autocorrelation in raw returns, and persistent volatility clustering, that any generative framework must simultaneously reproduce to be considered statistically faithful (Mandelbrot, [1963](#bib.bib3 "The Variation of Certain Speculative Prices"); Cont, [2001](#bib.bib4 "Empirical properties of asset returns: stylized facts and statistical issues"); Stenger et al., [2024](#bib.bib60 "Thinking in categories: A survey on assessing the quality for time series synthesis")). These domain-specific quality criteria, often called stylized facts, serve as the benchmark against which the fidelity of synthetic financial data must be evaluated.

Existing generative approaches address these quality requirements from different angles but each falls short on at least one dimension. GARCH-family models (Engle, [1982](#bib.bib10 "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation"); Bollerslev, [1986](#bib.bib11 "Generalized Autoregressive Conditional Heteroscedasticity")) capture conditional variance dynamics but do not explicitly represent discrete market regimes or sudden jumps in volatility. Stochastic-volatility and jump-diffusion models (Heston, [1993](#bib.bib13 "A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options"); Merton, [1976](#bib.bib14 "Option Pricing When Underlying Stock Returns Are Discontinuous")) enrich tail behavior but lack a mechanism for volatility persistence after jumps. Deep generative models, including recurrent neural networks (Hochreiter and Schmidhuber, [1997](#bib.bib32 "Long Short-Term Memory"); Fischer and Krauss, [2018](#bib.bib33 "Deep learning with long short-term memory networks for financial market predictions")) and generative adversarial networks (Takahashi et al., [2019](#bib.bib47 "Modeling financial time-series with generative adversarial networks"); Kwon and Lee, [2024](#bib.bib21 "Can GANs Learn the Stylized Facts of Financial Time Series?"); Yoon et al., [2019](#bib.bib57 "Time-series generative adversarial networks")), can learn complex distributions from data but struggle to reproduce temporal dependence structures, particularly volatility clustering, unless the network architecture is specifically designed to capture them (Stenger et al., [2024](#bib.bib60 "Thinking in categories: A survey on assessing the quality for time series synthesis")). Hidden Markov models (HMMs) and related regime-switching frameworks offer a probabilistic structure for non-stationary market behavior through latent state dynamics (Rabiner and Juang, [1986](#bib.bib7 "An introduction to hidden Markov models")), yet standard HMM specifications fail to generate persistent high-volatility regimes, leading to overly rapid reversion following extreme events and poor temporal quality in the synthetic output (Rydén et al., [1998](#bib.bib8 "Stylized facts of daily return series and the hidden Markov model"); Bulla and Bulla, [2006](#bib.bib9 "Stylized facts of financial time series and hidden semi-Markov models")). Bridging this gap requires a generative framework that preserves both distributional fidelity and temporal structure while remaining computationally scalable.

We address this challenge by developing a hybrid HMM framework that discretizes continuous excess growth rates into quantile-based regimes and augments the resulting Markov process with a two-parameter Poisson jump-duration mechanism that forces the model to dwell in high-volatility tail states for empirically realistic durations, connecting gradual price evolution with sudden large moves identified by jump-detection methods (Au Yeung et al., [2020](#bib.bib18 "Jump detection in financial time series using machine learning algorithms")). By partitioning excess growth rates into quantile-defined states via a Laplace cumulative distribution function, we enable direct frequentist counting of regime transitions, bypassing the iterative Baum-Welch algorithm (and its sensitivity to starting values) entirely, making the framework scalable to a 424-asset synthetic data pipeline. We evaluate synthetic data quality using five complementary metrics: Kolmogorov-Smirnov (KS) and Anderson-Darling (AD) pass rates for distributional fidelity, Wasserstein-1 and Hellinger distances for effect-size quantification, and autocorrelation function mean absolute error (ACF-MAE) for temporal structure preservation, all reported with standard errors. Using ten years of SPY data (2014–2024) for training and 249 trading days (full calendar year 2025) for out-of-sample testing, we demonstrate KS and AD pass rates of 97.6% and 91.3% in-sample and 94.4% and 95.1% out-of-sample across 1,000 simulated paths, with volatility clustering preserved in both windows. A Single-Index Model factor extension (Sharpe, [1963](#bib.bib42 "A simplified model for portfolio analysis")) propagates the univariate SPY engine to the full 424-asset universe in a single generative pass, preserving cross-sectional correlation structure. We find that the jump-duration extension substantially improves the reproduction of persistent high-volatility regimes relative to standard regime-switching models, though the improvement is partial: approximately 24% of simulated paths contain jump episodes, shifting the ensemble ACF toward the empirical profile without fully matching it. The framework does not dominate all quality dimensions; GARCH(1,1) achieves lower ACF error, and the standard HMM without jumps attains higher distributional pass rates. The contribution is a balanced quality profile that avoids the severe failures each alternative exhibits on its weakest dimension.

![Refer to caption](2603.10202v1/x1.png)

Four-panel figure showing SPY daily excess growth rate stylized facts: (a) histogram with heavy tails compared to a Gaussian fit, (b) Q-Q plot showing leptokurtic departures from normality, (c) autocorrelation function of raw returns showing near-zero values, and (d) autocorrelation function of absolute returns showing slow decay characteristic of volatility clustering.

Figure 1. Empirical stylized facts of SPY daily excess growth rates (2014–2024).
Panel (a) shows the leptokurtic marginal distribution; the Laplace fit substantially outperforms
the Gaussian. Panel (b) confirms heavy tails via a normal Q-Q plot. Panels (c) and (d)
contrast the near-zero autocorrelation of raw returns (consistent with the efficient markets
hypothesis) against the persistent autocorrelation of absolute returns, motivating the
jump-duration extension.

## 2. Related Work

Research on reproducing the canonical stylized facts of financial markets divides into two broad paradigms: bottom-up agent-based models, which derive return dynamics from the simulated interaction of heterogeneous agents, and top-down data-driven models, which fit statistical structures directly to observed return series. In the bottom-up tradition, stylized facts emerge from collective behavior rather than being assumed. Lux and Marchesi (Lux and Marchesi, [1999](#bib.bib55 "Scaling and criticality in a stochastic multi-agent model of a financial market")) showed that a two-type fundamentalist-chartist population reproduces heavy tails and volatility clustering as emergent properties, Cont and Bouchaud (Cont and Bouchaud, [2000](#bib.bib54 "Herd behavior and aggregate fluctuations in financial markets")) demonstrated that a simple random-graph herding structure alone is sufficient to generate fat-tailed return distributions, and Chen, Tan, and Zheng (Chen et al., [2015](#bib.bib50 "Agent-based model with multi-level herding for complex financial systems")) showed that multi-level herding simultaneously reproduces sector structure and volatility clustering. The minority game of Challet and Zhang (Challet and Zhang, [1997](#bib.bib52 "Emergence of cooperation and organization in an evolutionary game")) introduced the paradigm of bounded-rational agents competing via strategic coordination, a framework subsequently shown to produce non-Gaussian fluctuations, and Farmer and Joshi (Farmer and Joshi, [2002](#bib.bib51 "The price dynamics of common trading strategies")) demonstrated that standard trading strategies simultaneously deployed by many agents endogenously generate volatility clustering and excess kurtosis without any exogenous noise assumption. LeBaron (LeBaron, [2006](#bib.bib53 "Agent-based computational finance")) surveys this class of models systematically; Arthur (Arthur, [2021](#bib.bib48 "Foundations of complexity economics")) provides a recent synthesis arguing that heterogeneous agent interactions give rise to phenomena inaccessible to equilibrium theory, and Farmer (Farmer, [2025](#bib.bib49 "Quantitative agent-based models: a promising alternative for macroeconomics")) demonstrates that quantitative ABMs can produce time-series predictions competitive with mainstream macroeconomic models. While mechanistically compelling, agent-based models can be challenging to calibrate directly to a specific asset’s return history and can be computationally demanding to deploy as practical synthetic data generators. Top-down models take the complementary approach: rather than explaining the origins of stylized facts, they specify statistical structures that match how those facts appear in data. GARCH, jump-diffusion processes, HMMs, and deep generative architectures all belong to this family; the subsections below survey each in turn, as they form the direct context for the present work.

### 2.1. Stylized facts and the limitations of parametric models

The quantitative study of financial market dynamics has been shaped by a tension between tractable theoretical frameworks and the empirical complexity of observed data. The Black-Scholes-Merton option pricing model (Black and Scholes, [1973](#bib.bib44 "The pricing of options and corporate liabilities")) and the geometric Brownian motion (GBM) paradigm embedded within it assume that log-returns are independently and identically distributed Gaussian random variables, producing asset prices that move smoothly (no sudden jumps) with fixed-size random fluctuations and thin tails that assign negligible probability to extreme moves. These properties carry well-known practical advantages: closed-form option prices, simple portfolio variance calculations, and minimal data requirements. However, the Gaussian diffusion paradigm conflicts with a broad set of empirical regularities documented well before the model’s widespread adoption. Mandelbrot (Mandelbrot, [1963](#bib.bib3 "The Variation of Certain Speculative Prices")) demonstrated that speculative price changes exhibit heavy tails far beyond Gaussian predictions, a property long characterized in statistics as leptokurtosis. Fama (Fama, [1970](#bib.bib2 "Efficient Capital Markets: A Review of Theory and Empirical Work")) reviewed evidence that raw return series display negligible linear autocorrelation, consistent with the efficient markets hypothesis. Yet Schwert (Schwert, [1989](#bib.bib5 "Why Does Stock Market Volatility Change Over Time?")) and others documented that the magnitude of returns exhibits substantial positive autocorrelation decaying slowly over time: large price changes tend to be followed by large changes regardless of sign, a pattern referred to as volatility clustering. Cont (Cont, [2001](#bib.bib4 "Empirical properties of asset returns: stylized facts and statistical issues")) provides a systematic review confirming these regularities across asset classes, geographic markets, and sampling frequencies. Collectively, leptokurtosis, the absence of return predictability, and volatility clustering define the benchmark against which any model of market dynamics must be evaluated.

The most influential class of models designed to address volatility clustering within the Gaussian framework is the autoregressive conditional heteroscedasticity (ARCH) family introduced by Engle (Engle, [1982](#bib.bib10 "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation")), generalized by Bollerslev (Bollerslev, [1986](#bib.bib11 "Generalized Autoregressive Conditional Heteroscedasticity")) to the GARCH(p,q) specification in which the conditional variance depends on both past squared residuals and past conditional variances. GARCH models are parsimonious and widely used, but they have well-documented limitations. Heavy tails must be injected by choosing a fat-tailed noise distribution (e.g., Student-t); the model itself does not produce them. There is no representation of discrete market regimes or sudden jumps. Volatility persistence is controlled by a single decay parameter, so the model cannot distinguish between a calm market that slowly heats up and a sudden crash that lingers (Diebold and Inoue, [2001](#bib.bib45 "Long memory and regime switching")). Stochastic volatility models (Stein and Stein, [1991](#bib.bib12 "Stock price distributions with stochastic volatility: an analytic approach"); Heston, [1993](#bib.bib13 "A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options")) model volatility as a hidden quantity that evolves randomly over time, addressing some of these shortcomings, but require computationally intensive estimation and their parameters do not directly correspond to observable market states. An alternative approach to modeling fat tails and discontinuous price behavior is the explicit introduction of Poisson-driven jumps into the asset price process. Merton (Merton, [1976](#bib.bib14 "Option Pricing When Underlying Stock Returns Are Discontinuous")) added a compound Poisson jump component to GBM, producing a Gaussian-mixture marginal distribution that directly addresses leptokurtosis, and Kou (Kou, [2002](#bib.bib15 "A Jump-Diffusion Model for Option Pricing")) extended this framework with asymmetric jump sizes to capture the empirical pattern that crashes tend to be sharper than rallies. Jump-diffusion models are particularly relevant in equity markets, where macroeconomic announcements, earnings surprises, and geopolitical events generate discrete large-magnitude price movements (Au Yeung et al., [2020](#bib.bib18 "Jump detection in financial time series using machine learning algorithms")). However, in their standard form, jump-diffusion models do not provide a mechanism for volatility persistence: the post-jump volatility immediately returns to its baseline level, absent a separate stochastic volatility component.

### 2.2. Hidden Markov models and regime-switching

Hidden Markov models (HMMs) provide a probabilistic framework for non-stationary time series in which the observed data are generated by a process that switches among a discrete set of latent states according to Markov dynamics. The Baum-Welch expectation-maximization algorithm for maximum-likelihood estimation of emission and transition parameters was introduced by Baum, Petrie, Soules, and Weiss (Baum et al., [1970](#bib.bib6 "A maximization technique occurring in the statistical analysis of probabilistic functions of Markov chains")); Rabiner and Juang (Rabiner and Juang, [1986](#bib.bib7 "An introduction to hidden Markov models")) provided the influential tutorial that brought HMMs to widespread attention in engineering and applied science. Hamilton (Hamilton, [1989](#bib.bib41 "A new approach to the economic analysis of nonstationary time series and the business cycle")) applied the regime-switching HMM to macroeconomic time series, demonstrating that U.S. GNP growth is well described by a two-state model with distinct expansion and recession regimes, establishing the template for latent-state modeling of financial time series. The identification of time-varying market regimes has since become a central application of HMMs in finance, with uses ranging from stock return modeling and volatility forecasting (Rossi and Gallo, [2006](#bib.bib17 "Volatility estimation via hidden Markov models")) to stock trading strategies (Nguyen, [2018](#bib.bib19 "Hidden Markov Model for Stock Trading")).

Rydén, Teräsvirta, and Åsbrink (Rydén et al., [1998](#bib.bib8 "Stylized facts of daily return series and the hidden Markov model")) provided an influential systematic evaluation of HMM specifications against the stylized facts of daily return series, showing that simple Gaussian-emission HMMs with a small number of states could reproduce leptokurtosis and the absence of return autocorrelation, but failed to generate the observed volatility clustering; the ACF of absolute returns under standard HMMs decayed far too rapidly relative to empirical data. This diagnostic limitation identified the core structural gap that the present study addresses. Bulla and Bulla (Bulla and Bulla, [2006](#bib.bib9 "Stylized facts of financial time series and hidden semi-Markov models")) advanced this line of inquiry by considering hidden semi-Markov models, in which the time spent in each state can follow a flexible distribution rather than the simple memoryless (geometric) decay of standard Markov chains, and showed that this extension substantially improves the reproduction of volatility clustering by allowing the model to remain in high-volatility states for realistic durations. A persistent practical limitation of both standard and semi-Markov HMM approaches is the computational burden of maximum-likelihood estimation via the EM algorithm, particularly when the number of states is large or the asset universe is broad: the Baum-Welch procedure requires iterative forward-backward passes and may converge to local maxima depending on initialization. The present study addresses this limitation by replacing EM with direct frequentist counting of transitions between quantile-defined states, an approach that is computationally trivial and free of initialization sensitivity.

### 2.3. Synthetic data generation and deep generative models

The generation of synthetic financial time series has attracted increasing attention both as a practical tool for augmenting limited data, testing risk models, and stress testing portfolios, and as a benchmark for evaluating generative model quality. Assefa et al. (Assefa et al., [2020](#bib.bib24 "Generating synthetic data in finance: opportunities, challenges and pitfalls")) survey the opportunities, challenges, and pitfalls of synthetic data generation in finance, noting that stylized-facts reproduction is the primary criterion for evaluating statistical quality and that naive generative approaches tend to fail on at least one of the three core stylized facts. The rise of generative adversarial networks (GANs) prompted several investigations into whether deep learning architectures could learn these properties from data. Takahashi, Chen, and Tanaka-Ishii (Takahashi et al., [2019](#bib.bib47 "Modeling financial time-series with generative adversarial networks")) showed that standard GAN architectures produce synthetic return sequences that visually resemble financial time series but fail to reproduce ACF structure precisely; Kwon and Lee (Kwon and Lee, [2024](#bib.bib21 "Can GANs Learn the Stylized Facts of Financial Time Series?")) provided a careful evaluation against the stylized-facts checklist, finding that while GANs match marginal distributions reasonably well, capturing temporal dependence structures, particularly volatility clustering, remains challenging unless the architecture is specifically designed to learn them. Foundation models for Markov jump processes (Berghaus et al., [2024](#bib.bib23 "Foundation inference models for Markov jump processes")) offer a complementary perspective in which large-scale pretrained inference networks can be applied to new process instances without retraining, but their application to financial time series generation remains an open research direction.

Against this backdrop, the hybrid HMM framework of the present study occupies a distinct position: it is explicitly designed around the structural properties known to generate stylized facts, uses an interpretable discrete-state representation that can be audited and stress-tested, and achieves strong statistical fidelity with minimal computational overhead. The empirical estimation procedure avoids the training instability and data requirements of deep generative models, while the jump-duration mechanism provides a principled solution to the volatility-clustering limitation of standard HMMs. These properties make the framework particularly well-suited for risk management and stress-testing pipelines, where interpretability and computational reproducibility are as important as statistical fidelity.

### 2.4. Factor models and multi-asset extensions

Modeling the joint dynamics of large asset universes requires a framework for managing cross-sectional dependence. The Single-Index Model (SIM) of Sharpe (Sharpe, [1963](#bib.bib42 "A simplified model for portfolio analysis")) provides the canonical linear factor decomposition: each asset’s excess return is decomposed into a common market factor component and an idiosyncratic residual, drastically reducing the number of parameters needed compared with a full multivariate model. The SIM remains foundational in portfolio construction and risk management despite the availability of richer multi-factor models such as Fama-French (Fama and French, [1993](#bib.bib43 "Common risk factors in the returns on stocks and bonds")), because its simplicity enables transparent attribution and scalable computation. Existing HMM-based work in finance has been predominantly univariate, focusing on single-asset or single-index regime identification. Applications to individual equities (Nguyen, [2018](#bib.bib19 "Hidden Markov Model for Stock Trading")), volatility modeling (Rossi and Gallo, [2006](#bib.bib17 "Volatility estimation via hidden Markov models")), and macro time series (Hamilton, [1989](#bib.bib41 "A new approach to the economic analysis of nonstationary time series and the business cycle"); Kim and Nelson, [1999](#bib.bib46 "Has the U.S. economy become more stable? A Bayesian approach based on a Markov-switching model of the business cycle")) collectively demonstrate the utility of latent state representations but leave open the question of how HMM-derived generative models can be extended to large cross-sections of assets in a computationally tractable way. Mixture hidden Markov models (Dias et al., [2010](#bib.bib22 "Mixture Hidden Markov Models in Finance Research")) offer a partial solution by allowing multiple assets to share a common latent state structure, but estimating such models jointly across hundreds of assets is computationally demanding. An alternative approach to multi-asset dependence modeling uses copulas, which separate the specification of marginal distributions from the dependence structure (Embrechts et al., [2002](#bib.bib62 "Correlation and dependence in risk management: properties and pitfalls"); Cherubini et al., [2004](#bib.bib63 "Copula methods in finance")). Copula-based generators can capture nonlinear and tail dependence that linear factor models miss, and they have been applied extensively in credit risk and portfolio simulation. However, copula estimation becomes computationally demanding in high dimensions, and the choice of copula family introduces additional model selection complexity. The present study addresses the multi-asset challenge through a complementary route by combining the univariate HMM framework with the SIM factor decomposition: the hybrid HMM is estimated on the SPY index, which serves as the market-factor generator, and asset-level paths are reconstructed via the linear SIM projection. This construction exploits the fact that most of the shared volatility clustering across equities is driven by the broad market, yielding a scalable generative pipeline for a 424-asset universe that inherits the stylized-facts fidelity of the HMM without requiring joint estimation of a high-dimensional model.

## 3. Methods

### Data.

The empirical foundation of this study was a dataset composed of 424 United States-listed equities and exchange-traded funds spanning 10 years (2014-2024). A pipeline was developed to support the automated construction of excess growth rate models for any ticker within this dataset, allowing for batch simulation and stress testing across market sectors. To validate the performance of this pipeline, we focused our analysis on the single-asset SPY, which tracked the Standard & Poor’s (S&P) 500 index. The data included daily open, high, low, and close prices along with volume-weighted average price metrics (VWAP). For training purposes, the first 2,766 observations constituted the in-sample dataset, spanning from January 3, 2014, to December 31, 2024. A subsequent 249 trading days, from January 2 to December 31, 2025, were reserved for out-of-sample testing to assess model generalizability.

### Excess growth rate calculation.

We computed the excess growth rate Gi,jG\_{i,j} for ticker ii between time period j−1→jj-1\rightarrow{j} for a given equity price series Pi,jP\_{i,j} (units: dollars per share (USD/share)). To measure how much each stock’s growth exceeded a risk-free baseline, we defined the excess growth rate as:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | Gi,j≡(1Δ​t)⋅ln⁡(Pi,jPi,j−1)−rfG\_{i,j}\equiv\left(\frac{1}{\Delta t}\right)\cdot\ln\left(\frac{P\_{i,j}}{P\_{i,j-1}}\right)-r\_{f} |  |

where Δ​t\Delta t represented the time step set to 1/2521/252 for daily data (units: years), and rfr\_{f} denoted the constant continuously compounded risk-free rate (units: year-1) derived from Separate Trading of Registered Interest and Principal of Securities (STRIPS) bond yields observed on September 10, 2025. Unlike a simple return, the excess growth rate has units of inverse time (year-1) and directly quantifies the premium earned above a continuously compounded risk-free benchmark; log growth rates are also time-additive, making them consistent with a continuous compounding framework. While rfr\_{f} varied dynamically over the sample period, we used a constant proxy to isolate the volatility patterns in the data without adding noise from interest rate movements.

### Discrete hidden Markov model.

We defined the hidden Markov model using the tuple ℳ=(𝒮,𝒪,𝐓,𝐄,π¯)\mathcal{M}=(\mathcal{S},\mathcal{O},\mathbf{T},\mathbf{E},\bar{\pi}) (Rabiner and Juang, [1986](#bib.bib7 "An introduction to hidden Markov models")). The hidden state St∈𝒮={1,…,N}S\_{t}\in\mathcal{S}=\{1,\dots,N\} represented market mood regimes and was defined by quantile bins of a fitted cumulative distribution function (CDF) for the excess growth rate series. The observation space 𝒪⊂ℝ\mathcal{O}\subset\mathbb{R} consisted of continuous excess growth rate values, the transition matrix 𝐓\mathbf{T} governed regime-to-regime dynamics, the emission model 𝐄\mathbf{E} was parameterized by state-conditional Student-t distributions, and π¯\bar{\pi} denoted the stationary distribution. The state-conditional observation model specified that the excess growth rate, given hidden state kk, followed a location-scale Student-t distribution with ν=5\nu=5 degrees of freedom:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | Gt∣St=k∼μk+σk⋅tν,ν=5.G\_{t}\mid S\_{t}=k\sim\mu\_{k}+\sigma\_{k}\cdot t\_{\nu},\qquad\nu=5. |  |

To map observations to hidden states during estimation, we defined quantile boundaries Qk=FL−1​(k/N;μL,bL)Q\_{k}=F\_{L}^{-1}(k/N;\mu\_{L},b\_{L}) for k∈{1,…,N−1}k\in\{1,\dots,N-1\}, with Q0=−∞Q\_{0}=-\infty and QN=+∞Q\_{N}=+\infty so that the partition covers the full support of the distribution. An observation was assigned to state kk when Qk−1<Gt≤QkQ\_{k-1}<G\_{t}\leq Q\_{k}.

The Laplace distribution was chosen for state partitioning rather than for emission modeling. Its sharper peak at the mean better matched the concentration of small price movements observed in the SPY dataset (Mandelbrot, [1963](#bib.bib3 "The Variation of Certain Speculative Prices"); Toth and Jones, [2019](#bib.bib30 "Against the Norm: Modeling Daily Stock Returns with the Laplace Distribution"); Cont, [2001](#bib.bib4 "Empirical properties of asset returns: stylized facts and statistical issues"); Kotz et al., [2001](#bib.bib29 "The Laplace Distribution and Generalizations: A Revisit with Applications to Communications, Economics, Engineering, and Finance")), and its closed-form quantile function supported the 424-ticker pipeline without iterative numerical optimization (Bilmes, [1998](#bib.bib20 "A Gentle Tutorial of the EM Algorithm and its Application to Parameter Estimation for Gaussian Mixture and Hidden Markov Models")). The quantile boundaries were derived from a parametric Laplace fit and therefore did not enforce equal counts per bin in the historical data; instead, they provided a partition of the distribution that preserved tail shape. By using the Laplace distribution to define the bins, the model established a baseline characterization of the return distribution’s shape before the transition dynamics and jump mechanism were layered on top (Kou, [2002](#bib.bib15 "A Jump-Diffusion Model for Option Pricing")). The emission distribution within each state, however, was a location-scale Student-t with ν=5\nu=5 degrees of freedom, chosen because its heavier tails relative to the Normal distribution better reproduced the observed excess kurtosis of the growth rate series (a sensitivity analysis over ν∈{3,4,5,6,7,8,10,15,30,∞}\nu\in\{3,4,5,6,7,8,10,15,30,\infty\} identified ν=5\nu=5 as the value that minimized the kurtosis gap without degrading distributional fidelity; ν=∞\nu=\infty recovers the Normal baseline).

We estimated the transition matrix 𝐓\mathbf{T} through direct frequentist counting rather than iterative optimization. This approach differed from the traditional expectation-maximization (EM) algorithm used for parameter estimation in Gaussian mixture and hidden Markov models (Bilmes, [1998](#bib.bib20 "A Gentle Tutorial of the EM Algorithm and its Application to Parameter Estimation for Gaussian Mixture and Hidden Markov Models")). However, the discrete state assignments allowed for straightforward counting of observed transitions between regimes, making the approach both conceptually simple and free of initialization sensitivity. A consequence of direct counting was that empirical transition matrices often had low probabilities for exiting central states into tail states, which caused models to lose the effect of volatility clustering too quickly (Bulla and Bulla, [2006](#bib.bib9 "Stylized facts of financial time series and hidden semi-Markov models")). We corrected this by adding jump parameters ϵ\epsilon, representing the probability of a jump event, and λ\lambda, representing the mean duration, along with a tail-state selection rule. Tail-states were defined as 𝒮b​o​t​t​o​m={1,…,Nt​a​i​l}\mathcal{S}\_{bottom}=\{1,\dots,N\_{tail}\} and 𝒮t​o​p={N−Nt​a​i​l+1,…,N}\mathcal{S}\_{top}=\{N-N\_{tail}+1,\dots,N\}, where Nt​a​i​lN\_{tail} was user-configurable. If a jump was triggered, the jump-duration KK was sampled from a Poisson distribution such that K∼Poisson​(λ)K\sim\text{Poisson}(\lambda), which was standard for modeling independent events in fixed intervals (Glasserman, [2003](#bib.bib16 "Monte Carlo Methods in Financial Engineering")). During these KK steps, the standard Markovian transitions were overridden to target tail-states, with a user-configurable bias pn​e​gp\_{neg} (default 0.52) that favored negative-tail states to reproduce gain/loss asymmetry.

1122⋯\cdotskk⋯\cdotsN−1N\!-\!1NNμk+σk⋅t5\mu\_{k}\!+\!\sigma\_{k}\cdot t\_{5} emissionPoisson clockprob. ϵ\epsilonjump triggeredK∼Pois​(λ)K\!\sim\!\mathrm{Pois}(\lambda) forced stepsK∼Pois​(λ)K\!\sim\!\mathrm{Pois}(\lambda) forced steps𝒮−\mathcal{S}\_{-} (bottom tail)𝒮+\mathcal{S}\_{+} (top tail)state indexprob. 1−ϵ1\!-\!\epsilon

Diagram of the HMM-WJ architecture showing a linear chain of hidden states from state 1 (red, bottom tail) through middle states to state N (blue, top tail). Thin bidirectional arrows represent normal Markov transitions. A dashed arrow from a middle state points upward to a Poisson clock node labeled epsilon, which then directs flow into either the bottom-tail (red) or top-tail (blue) state sets for K steps before returning to normal Markov transitions. Small bell curves above each state represent the state-conditional Student-t emission distribution.

Figure 2. Architecture of the Hybrid Hidden Markov Model with Jump-Diffusion (HMM-WJ).
At each step the chain transitions according to the empirical transition matrix 𝐓\mathbf{T}
(probability 1−ϵ1-\epsilon, thin bidirectional arrows) or enters a Poisson jump episode
(probability ϵ\epsilon, dashed upward arrow to the Poisson clock).
During a jump episode the active state is forced to the bottom tail set 𝒮−\mathcal{S}\_{-}
(red, lowest-valued states) or the top tail set 𝒮+\mathcal{S}\_{+} (blue, highest-valued states)
for K∼Poisson​(λ)K\!\sim\!\mathrm{Poisson}(\lambda) consecutive steps before normal Markovian evolution
resumes. Small bell curves above each state depict the state-conditional
location-scale Student-t (ν=5\nu=5) emission distribution. Tail sets are defined as the
NtailN\_{\rm tail} lowest- and highest-quantile states under the Laplace quantile partition.

To characterize the excess growth rates within each regime, we parameterized the emission model with location-scale Student-t distributions μk+σk⋅t5\mu\_{k}+\sigma\_{k}\cdot t\_{5}, where μk\mu\_{k} and σk\sigma\_{k} were the sample mean and standard deviation of observations assigned to state kk. During simulation, when the model was in state kk, the continuous excess growth rate (G^t\hat{G}\_{t}) was sampled from the corresponding local distribution. This hybrid approach ensured that the model captured sudden large price moves while keeping smooth variation within each regime (Kou, [2002](#bib.bib15 "A Jump-Diffusion Model for Option Pricing")). The fitted Laplace CDF closely matched the empirical CDF for SPY, and the empirical transition matrix exhibited a dominant near-diagonal band reflecting short-range regime persistence (Figure [S1](#Sx4.F1 "Figure S1 ‣ S1. Fitted model internals ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), Online Appendix S1). Critically, under pure Markovian dynamics the model exited extreme (tail) states after only 1–2 steps on average, far shorter than the multi-week volatile episodes observed in real markets. This rapid reversion was the core limitation that motivated the jump-duration extension.

### Growth rate generation.

The basic sampling procedure for the HMM (without jumps) proceeded as follows. The stationary distribution π¯\bar{\pi}, representing the long-run probability of occupying each regime, satisfies the balance equation π¯=π¯​𝐓\bar{\pi}=\bar{\pi}\mathbf{T} and was estimated numerically by raising the transition matrix to a large power (𝐓50\mathbf{T}^{50}) (Hamilton, [2018](#bib.bib26 "Regime Switching Models"); Grinstead and Snell, [1997](#bib.bib28 "Introduction to Probability")). An initial hidden state was drawn from X0∼π¯X\_{0}\sim\bar{\pi}, then for each subsequent step n=1,…,Tn=1,\dots,T: (i) the next hidden state was sampled from the transition row Xn∼𝐓Xn−1,⋅X\_{n}\sim\mathbf{T}\_{X\_{n-1},\,\cdot}, and (ii) an observation was sampled from the emission distribution On∼𝐄XnO\_{n}\sim\mathbf{E}\_{X\_{n}}. This produced a sequence of hidden states {X1,…,XT}\{X\_{1},\dots,X\_{T}\} and corresponding observations {O1,…,OT}\{O\_{1},\dots,O\_{T}\}.

### Hyperparameter optimization via grid search.

To identify the optimal jump probability (ϵ\epsilon) and mean jump duration (λ\lambda) (Merton, [1976](#bib.bib14 "Option Pricing When Underlying Stock Returns Are Discontinuous"); Kou, [2002](#bib.bib15 "A Jump-Diffusion Model for Option Pricing")), we implemented a multi-objective grid search that minimized the discrepancy between historical and simulated market signatures. The error function targeted two stylized facts (Cont, [2001](#bib.bib4 "Empirical properties of asset returns: stylized facts and statistical issues"); Rydén et al., [1998](#bib.bib8 "Stylized facts of daily return series and the hidden Markov model")): volatility clustering, measured as the sum of squared errors between the observed and simulated autocorrelation function (ACF) of absolute excess growth rates (Schwert, [1989](#bib.bib5 "Why Does Stock Market Volatility Change Over Time?")) up to a lag of L=252L=252 trading days (approximately one trading year); and leptokurtosis, captured by a penalty term on the global kurtosis (Mandelbrot, [1963](#bib.bib3 "The Variation of Certain Speculative Prices")).

We defined the objective function J​(ϵ,λ)J(\epsilon,\lambda) as:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | J​(ϵ,λ)=∑τ=1L(ACFo​b​s​(τ)−ACF¯s​i​m​(τ))2+wK​(Ko​b​s−K¯s​i​m)2J(\epsilon,\lambda)=\sum\_{\tau=1}^{L}\left(\text{ACF}\_{obs}(\tau)-\overline{\text{ACF}}\_{sim}(\tau)\right)^{2}+w\_{K}\left(K\_{obs}-\overline{K}\_{sim}\right)^{2} |  |

where ACFo​b​s​(τ)\text{ACF}\_{obs}(\tau) and Ko​b​sK\_{obs} represented the empirical absolute growth autocorrelation at lag τ\tau and the global kurtosis, respectively. The simulated equivalents, ACF¯s​i​m​(τ)\overline{\text{ACF}}\_{sim}(\tau) and K¯s​i​m\overline{K}\_{sim}, were averaged across 200 independent synthetic paths of 2,766 trading days per grid point (Glasserman, [2003](#bib.bib16 "Monte Carlo Methods in Financial Engineering")). We set the kurtosis penalty weight to wK=0.20w\_{K}=0.20 to balance tail behavior against the temporal ACF term. The grid search explored ϵ\epsilon values from 10−410^{-4} to 2.5×10−22.5\times 10^{-2} and λ\lambda values from 1010 to 160160. The full computational procedure is detailed in Algorithm [4](#alg4 "Algorithm 4 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").

### Statistical validation metrics

To assess whether synthetic paths were statistically consistent with empirical data, we applied two nonparametric goodness-of-fit tests to the marginal distributions of simulated excess growth rate sequences. For each of the 1,000 simulated paths, the empirical cumulative distribution function (CDF) of the simulated sequence was compared against the empirical CDF of the historical in-sample or out-of-sample observations.

The Kolmogorov-Smirnov (KS) statistic is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | DK​S=supx|Fn​(x)−Fm​(x)|D\_{KS}=\sup\_{x}\left\lvert F\_{n}(x)-F\_{m}(x)\right\rvert |  |

where FnF\_{n} and FmF\_{m} denote the empirical CDFs of the observed and simulated sequences of lengths nn and mm, respectively (Kolmogorov, [1933](#bib.bib38 "Sulla determinazione empirica di una legge di distribuzione"); Smirnov, [1948](#bib.bib39 "Table for estimating the goodness of fit of empirical distributions")). The null hypothesis of distributional equivalence is rejected at significance level α\alpha when DK​SD\_{KS} exceeds the critical value c​(α)​(n+m)/(n​m)c(\alpha)\sqrt{(n+m)/(nm)}.

The Anderson-Darling (AD) statistic places greater weight on the distributional tails than the KS test. The original one-sample form (Anderson and Darling, [1952](#bib.bib40 "Asymptotic theory of certain “goodness of fit” criteria based on stochastic processes")) measures deviation from a fully specified reference CDF F0F\_{0}:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | A2=−n−∑i=1n2​i−1n​[ln⁡F0​(X(i))+ln⁡(1−F0​(X(n+1−i)))]A^{2}=-n-\sum\_{i=1}^{n}\frac{2i-1}{n}\left[\ln F\_{0}(X\_{(i)})+\ln\left(1-F\_{0}(X\_{(n+1-i)})\right)\right] |  |

where X(1)≤⋯≤X(n)X\_{(1)}\leq\cdots\leq X\_{(n)} are the order statistics of the sample. In this study, we applied the two-sample Anderson-Darling test, which replaces F0F\_{0} with the empirical CDF of the observed SPY series; critical values are obtained from the kk-sample variant of [Anderson and Darling](#bib.bib40 "Asymptotic theory of certain “goodness of fit” criteria based on stochastic processes") as implemented in the HypothesisTests.jl library. The AD test is particularly suited for assessing tail-distributional fidelity, which is the primary concern for risk management applications.

We reported the pass rate as the proportion of the 1,000 simulated paths for which the null hypothesis of distributional equivalence was not rejected at the α=0.05\alpha=0.05 significance level. A pass rate above 95 percent indicated that the synthetic paths were, in aggregate, statistically indistinguishable from the historical data under that test. Pass rates were reported separately for the in-sample and out-of-sample windows and for both model variants (HMM without jumps and the hybrid HMM with jumps). Both KS and AD tests assume i.i.d. observations; because volatility clustering induces positive autocorrelation in the tail-indicator process 𝟏​(Gt≤x)\mathbf{1}(G\_{t}\leq x), the effective sample size is smaller than TT and reported p-values may be slightly miscalibrated. The continuous distance metrics below are unaffected by this assumption.

### Continuous distributional distance metrics

Binary pass rates summarize distributional fidelity but discard information about the magnitude of any discrepancy. The Wasserstein-1 distance (W1W\_{1}) and the Hellinger distance (HH) were computed alongside KS and AD to provide continuous, effect-size measures that do not depend on sample size.

The Wasserstein-1 distance measures the minimum work required to transform one distribution into the other, where work is distance times probability mass moved. For two equal-length empirical samples with order statistics x(1)≤⋯≤x(T)x\_{(1)}\leq\cdots\leq x\_{(T)} and y(1)≤⋯≤y(T)y\_{(1)}\leq\cdots\leq y\_{(T)}, the one-dimensional Wasserstein-1 distance is:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | W1=1T​∑i=1T|x(i)−y(i)|W\_{1}=\frac{1}{T}\sum\_{i=1}^{T}\left\lvert x\_{(i)}-y\_{(i)}\right\rvert |  |

W1W\_{1} is expressed in the same units as the data (daily excess growth rates) and equals zero only when the empirical distributions are identical. Because it is computed from sorted order statistics, the temporal ordering of observations is irrelevant; smaller values indicate closer distributional agreement across the full quantile range.

The Hellinger distance measures distributional overlap and is bounded in [0,1][0,1], with H=0H=0 indicating identical distributions and H=1H=1 indicating completely disjoint support. Given normalized histogram estimates {pk}k=1K\{p\_{k}\}\_{k=1}^{K} and {qk}k=1K\{q\_{k}\}\_{k=1}^{K} of the observed and simulated marginal densities over a common KK-bin grid:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | H​(P,Q)=12​∑k=1K(pk−qk)2H(P,Q)=\frac{1}{\sqrt{2}}\sqrt{\sum\_{k=1}^{K}\left(\sqrt{p\_{k}}-\sqrt{q\_{k}}\right)^{2}} |  |

The bounded scale makes HH directly comparable across models and evaluation windows without rescaling. Histograms were constructed on the common support of observed and simulated samples using K=50K=50 equal-width bins. Both W1W\_{1} and HH were computed path-by-path and averaged across the 1,000 paths; standard errors were estimated as std/npaths\mathrm{std}/\sqrt{n\_{\mathrm{paths}}}.

### Temporal fidelity metric

While KS and AD tests assess marginal distributional quality, they are insensitive to temporal dependence. To measure how well a generator reproduced volatility clustering, we defined the autocorrelation mean absolute error (ACF-MAE) as:

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | ACF-MAE=1L​∑τ=1L|ρ^|G|obs​(τ)−ρ^|G|sim​(τ)|\text{ACF-MAE}=\frac{1}{L}\sum\_{\tau=1}^{L}\left\lvert\widehat{\rho}\_{|G|}^{\,\text{obs}}(\tau)-\widehat{\rho}\_{|G|}^{\,\text{sim}}(\tau)\right\rvert |  |

where ρ^|G|obs​(τ)\widehat{\rho}\_{|G|}^{\,\text{obs}}(\tau) and ρ^|G|sim​(τ)\widehat{\rho}\_{|G|}^{\,\text{sim}}(\tau) are the sample autocorrelations of the absolute excess growth rate series |Gt||G\_{t}| at lag τ\tau for the observed and simulated paths, respectively, and L=252L=252 (one trading year). An i.i.d. generator produces ρ^|G|sim​(τ)≈0\widehat{\rho}\_{|G|}^{\,\text{sim}}(\tau)\approx 0 for all τ>0\tau>0, so its ACF-MAE equals the mean level of the observed autocorrelation function; lower values indicate better reproduction of empirical volatility persistence.

### Single-Index Factor Model extension

The framework described above applied to any individual asset ticker within the 424-asset dataset. To generalize synthetic path generation to a correlated multi-asset setting without fitting a separate HMM for each asset, we exploited the linear factor structure of the Single-Index Model (SIM) (Sharpe, [1963](#bib.bib42 "A simplified model for portfolio analysis")). The SIM expresses the excess growth rate of asset ii at time tt as:

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | Gi,t=αi+βi⋅GSPY,t+ηi,t,ηi,t∼i.i.d.𝒩​(0,ση,i2)G\_{i,t}=\alpha\_{i}+\beta\_{i}\cdot G\_{\text{SPY},t}+\eta\_{i,t},\qquad\eta\_{i,t}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\mathcal{N}(0,\sigma\_{\eta,i}^{2}) |  |

where GSPY,tG\_{\text{SPY},t} denotes the SPY excess growth rate at time tt, βi\beta\_{i} measures the systematic sensitivity of asset ii to the index, αi\alpha\_{i} is the idiosyncratic drift, and ηi,t\eta\_{i,t} is a zero-mean idiosyncratic shock assumed independent across assets and time. The parameters (αi,βi,ση,i2)(\alpha\_{i},\beta\_{i},\sigma\_{\eta,i}^{2}) were estimated via ordinary least squares on the in-sample time series for each asset ii.

Synthetic multi-asset paths were generated in three steps. First, the hybrid HMM produced a single synthetic SPY excess growth rate path {G^SPY,t}t=1T\{\hat{G}\_{\text{SPY},t}\}\_{t=1}^{T} using the regime-switching and jump-duration mechanism described above. Second, for each asset ii, an idiosyncratic shock sequence {η^i,t}\{\hat{\eta}\_{i,t}\} was drawn independently from 𝒩​(0,σ^η,i2)\mathcal{N}(0,\hat{\sigma}\_{\eta,i}^{2}). Third, the synthetic excess growth rate for asset ii was recovered as:

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | G^i,t=α^i+β^i⋅G^SPY,t+η^i,t.\hat{G}\_{i,t}=\hat{\alpha}\_{i}+\hat{\beta}\_{i}\cdot\hat{G}\_{\text{SPY},t}+\hat{\eta}\_{i,t}. |  |

This construction preserved the cross-sectional correlation structure induced by the common factor while maintaining the regime-switching and jump-diffusion dynamics of the index. The resulting 424-dimensional synthetic path could be used for stress testing, portfolio risk assessment, and scenario generation across the full asset universe in a single generative pass, avoiding the curse of dimensionality that would accompany a full multivariate HMM.

### Simulation algorithm

Algorithm [1](#alg1 "Algorithm 1 ‣ Simulation algorithm ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") details the core jump-diffusion simulation procedure; the remaining pipeline stages (model construction, state decoding, and hyperparameter grid search) are provided in Online Appendix S4.

Algorithm 1  Hybrid jump-diffusion simulation with persistent volatility

0:  Model parameters 𝐓,π¯,ϵ,λ,Nt​a​i​l,pn​e​g\mathbf{T},\bar{\pi},\epsilon,\lambda,N\_{tail},p\_{neg}, Total Steps MM

0:  Simulated state sequence S1:MS\_{1:M}

1:  Define tail-states 𝒮b​o​t​t​o​m={1,…,Nt​a​i​l}\mathcal{S}\_{bottom}=\{1,\dots,N\_{tail}\} and 𝒮t​o​p={N−Nt​a​i​l+1,…,N}\mathcal{S}\_{top}=\{N-N\_{tail}+1,\dots,N\}.

2:  Sample initial state S1∼Categorical​(π¯)S\_{1}\sim\text{Categorical}(\bar{\pi}).

3:  Set c​o​u​n​t​e​r←2counter\leftarrow 2.

4:  while c​o​u​n​t​e​r≤Mcounter\leq M do

5:   Sample u∼Uniform​(0,1)u\sim\text{Uniform}(0,1).

6:   if u<ϵu<\epsilon then

7:    Sample jump-duration K∼Poisson​(λ)K\sim\text{Poisson}(\lambda).

8:    for j=1j=1 to KK while c​o​u​n​t​e​r≤Mcounter\leq M do

9:     Sample w∼Uniform​(0,1)w\sim\text{Uniform}(0,1).

10:     if w<pn​e​gw<p\_{neg} then

11:      Sc​o​u​n​t​e​r∼Uniform​(𝒮b​o​t​t​o​m)S\_{counter}\sim\text{Uniform}(\mathcal{S}\_{bottom}) {Bias toward negative-tail events}

12:     else

13:      Sc​o​u​n​t​e​r∼Uniform​(𝒮t​o​p)S\_{counter}\sim\text{Uniform}(\mathcal{S}\_{top})

14:     end if

15:     c​o​u​n​t​e​r←c​o​u​n​t​e​r+1counter\leftarrow counter+1.

16:    end for

17:   else

18:    Sample Sc​o​u​n​t​e​r∼Categorical​(𝐓Sc​o​u​n​t​e​r−1,:)S\_{counter}\sim\text{Categorical}(\mathbf{T}\_{S\_{counter-1},:}).

19:    c​o​u​n​t​e​r←c​o​u​n​t​e​r+1counter\leftarrow counter+1.

20:   end if

21:  end while

22:  return S1:MS\_{1:M}

## 4. Empirical Study

### 4.1. Descriptive statistics and stylized facts

Descriptive statistics for the SPY daily excess growth rate series confirmed that the three canonical stylized facts were present in both the in-sample (2014–2024, T=2,766T=2{,}766) and out-of-sample (2025, T=249T=249) windows (Table [1](#S4.T1 "Table 1 ‣ 4.1. Descriptive statistics and stylized facts ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). Excess kurtosis (kurtosis minus 3, so that a Gaussian distribution has a value of zero) reached 7.7 (IS) and 6.9 (OoS), and the Jarque-Bera normality test was rejected (p<0.001p<0.001) in both windows, confirming leptokurtosis. The Ljung-Box test on |Gt||G\_{t}| was rejected (p<0.001p<0.001) in both windows, confirming persistent volatility clustering. The Ljung-Box test on raw returns GtG\_{t} was also formally rejected (p<0.001p<0.001 IS, p=0.019p=0.019 OoS); while this indicates statistically detectable linear autocorrelation, the effect is small in magnitude at daily frequency and is consistent with the broad EMH literature, which documents that return predictability is weak rather than strictly absent (Fama, [1970](#bib.bib2 "Efficient Capital Markets: A Review of Theory and Empirical Work")). Any faithful generative model must reproduce leptokurtosis, the ARCH effect, and the near-absence of large-magnitude return predictability simultaneously.

Table 1. Descriptive statistics and stylized-facts tests for SPY daily excess growth rates.
In-sample: 2014–2024 (T=2,766T=2{,}766); out-of-sample: 2025 (T=249T=249).
Gaussian and Laplace columns show MLE fits to the in-sample data.
JB = Jarque-Bera normality test.
LB = Ljung-Box autocorrelation test at lag 20.
∗ denotes rejection at α=0.05\alpha=0.05.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Statistic | IS Observed | OoS Observed | Gaussian | Laplace |
| Mean (annualized, %) | 6.31 | 11.60 | 6.31 | 14.19 |
| Std Dev (annualized, %) | 214.50 | 220.62 | 214.46 | 205.93 |
| Skewness | −0.753-0.753 | −1.093-1.093 | 0 | 0 |
| Excess Kurtosis | 7.715 | 6.867 | 0 | 3 |
| JB normality test | reject∗ (p<0.001p<0.001) | reject∗ (p<0.001p<0.001) | n/a | n/a |
| LB test on GtG\_{t} (lag 20) | reject∗ (p<0.001p<0.001) | reject∗ (p=0.019p=0.019) | n/a | n/a |
| LB test on |Gt||G\_{t}| (lag 20) | reject∗ (p<0.001p<0.001) | reject∗ (p<0.001p<0.001) | n/a | n/a |

### 4.2. Jump hyperparameter optimization and state resolution

A multi-objective grid search over ϵ∈[10−4, 2.5×10−2]\epsilon\in[10^{-4},\,2.5\times 10^{-2}] and λ∈[10, 160]\lambda\in[10,\,160], with 200 simulated paths per grid point, identified the optimal values ϵ∗=10−4\epsilon^{\*}=10^{-4} and λ∗=100\lambda^{\*}=100 (Figure [S2](#Sx4.F2 "Figure S2 ‣ S2. Hyperparameter grid search landscape ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), Online Appendix S2). The optimal λ∗=100\lambda^{\*}=100 was an interior point of the λ\lambda grid, confirming that the mean jump duration was identifiable from data; ϵ∗=10−4\epsilon^{\*}=10^{-4} fell at the lower boundary of the ϵ\epsilon grid, indicating that the data consistently preferred rarer tail-entry events over the range explored. At these optimal values, the ACF of |Gt||G\_{t}| closely tracked the observed SPY ACF across lags 1–252, confirming that the jump mechanism partially reproduced the empirical ARCH effect.

The primary analysis used N=100N=100 states, but a sensitivity study over N∈{30,60,90,100,150,200}N\in\{30,60,90,100,150,200\} showed that the framework was robust to the choice of state resolution across a wide range (Table [T1](#Sx4.T1 "Table T1 ‣ S3. State resolution sensitivity ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), Online Appendix S3). KS and AD pass rates remained stable for both HMM-NJ (≥\geq98.9% KS, ≥\geq97.9% AD) and HMM-WJ (≥\geq96.0% KS, ≥\geq88.6% AD), while ACF-MAE for HMM-WJ improved slightly from 0.057 at N=30N=30 to 0.049 at N=200N=200. State-occupancy diagnostics confirmed that every state at N≤200N\leq 200 contained at least 7 observations, ensuring adequate statistical support per state under the Laplace equal-probability partition. At N=350N=350, however, certain states were never visited in the historical record, leaving zero transition probabilities that prevented the model from reaching all states, which established a practical upper bound on state resolution.

### 4.3. In-sample distributional and temporal quality

We generated 1,000 synthetic paths of 2,766 trading days from each of eight generators and evaluated them against the observed SPY series using two-sample KS and AD tests at α=0.05\alpha=0.05, along with the Wasserstein-1 distance, Hellinger distance, kurtosis matching, ACF fidelity, novelty, diversity, and quantile coverage (Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")).

#### Baseline anchors.

We included three non-structured baselines and one semi-Markov baseline to bracket the quality landscape. Bootstrap resampling of the training data served as a non-parametric upper bound: we observed 100.0% KS and 99.7% AD pass rates with 100% quantile coverage, but this generator simply recycled observed values and could not produce genuinely new distributional structure (0 estimated parameters). The Gaussian i.i.d. baseline (MLE fit) achieved 0.0% KS and 0.0% AD pass rates, which confirmed that a symmetric thin-tailed model was categorically inadequate for heavy-tailed equity returns. The Laplace i.i.d. baseline fared better at 44.0% (SE 1.6) KS and 43.3% (SE 1.6) AD, which showed that matching the tail decay rate alone recovered roughly half the distributional quality; the remaining gap reflected the regime-dependent variation that a single Laplace distribution could not capture. The hidden semi-Markov model (HSMM) baseline, implemented following [Bulla and Bulla](#bib.bib9 "Stylized facts of financial time series and hidden semi-Markov models") with K=8K=8 Laplace quantile states, negative-binomial dwell-time distributions, and Student-t(ν=5\nu=5) emissions, achieved 82.0% (SE 1.2) KS and 42.5% (SE 1.6) AD in-sample. A sweep over K∈{3,4,5,6,8}K\in\{3,4,5,6,8\} selected K=8K=8 as the best-performing configuration; at all KK values, the empirical dwell times averaged only 1.1–1.8 steps per state, which meant the negative-binomial distributions collapsed to geometric (memoryless) behavior and the HSMM reduced to a standard coarse-state HMM. This confirmed that explicit dwell-time modeling alone could not reproduce the observed volatility clustering when state resolution was too coarse for accurate distributional matching, and too fine for meaningful dwell-time structure. The GRU neural baseline, a 2-layer gated recurrent unit trained autoregressively on the IS series with a Gaussian output head (37,954 trainable parameters), exhibited the inverse failure mode: it achieved the second-lowest ACF-MAE of any model (0.036, behind only GARCH at 0.031) but catastrophically failed distributional tests (0.6% KS, 0.2% AD) with a Wasserstein-1 distance of 0.421, worse than all models except Gaussian. The GRU learned the temporal dynamics of returns effectively but suffered from variance collapse: simulated standard deviation was 30% below the observed value, and excess kurtosis fell to 5.7 against an observed 7.7. This pattern, strong temporal fidelity paired with poor marginal fit, is the mirror image of the HMM-NJ tradeoff and illustrates the difficulty of simultaneously capturing both quality dimensions with a single modeling paradigm.

#### Distributional fidelity.

We evaluated KS/AD pass rates and kurtosis matching for the five structured models (Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). GARCH(1,1) achieved IS KS and AD pass rates of only 5.5% (SE 0.7) and 1.9% (SE 0.4), which indicated that the GARCH marginal distribution was systematically inconsistent with the observed data despite its well-known volatility clustering properties. The HSMM occupied a middle ground (82.0% KS, 42.5% AD), outperforming GARCH and Laplace but falling well short of the HMM variants; its coarse 8-state partition could not capture the full shape of the growth rate distribution, as reflected by a simulated kurtosis of 4.8 against an observed 7.7 (38% gap) and only 68.7% quantile coverage. HMM-NJ achieved 99.7% (SE 0.2) and 99.1% (SE 0.3), and HMM-WJ achieved 97.6% (SE 0.5) and 91.3% (SE 0.9). Both HMM variants adequately captured the observed heavy-tailed distribution, though HMM-WJ’s pass rates were 2–8 percentage points lower than HMM-NJ’s, a cost of the jump mechanism which occasionally distorted the marginal distribution by overweighting tail states during jump episodes. Simulated excess kurtosis told a complementary story: the observed value was 7.7, GARCH overshot at 8.2 (SE 0.37) with high variance across paths, while HMM-NJ and HMM-WJ produced 8.1 (SE 0.14) and 7.6 (SE 0.14) respectively. The Student-t(ν=5\nu=5) emissions closely matched the observed kurtosis (within 2% for HMM-WJ), a substantial improvement over Normal emissions which underestimated kurtosis by approximately 29%; a sensitivity analysis over ν∈{3,…,30,∞}\nu\in\{3,\dots,30,\infty\} confirmed that ν=5\nu=5 minimized the kurtosis gap without degrading other metrics. Quantile coverage reinforced these findings: Bootstrap, HMM-NJ, and HMM-WJ all achieved 100% coverage of the 1st–99th empirical percentiles, while Gaussian covered only 13.1%, Laplace 37.4%, GARCH 29.3%, and HSMM 68.7%, which indicated systematic tail misspecification in all non-HMM parametric generators (Figure [3](#S4.F3 "Figure 3 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel c).

#### Continuous distributional distances.

To complement the binary KS and AD pass rates with effect-size information that does not depend on sample size, we computed the Wasserstein-1 distance W1W\_{1} and the Hellinger distance HH for each simulated path against the observed SPY series (Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). W1W\_{1} quantifies the average absolute displacement between the sorted empirical quantiles of the simulated and observed distributions (Eq. [6](#S3.E6 "In Continuous distributional distance metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")), expressed in units of daily excess growth rates; HH measures distributional overlap on a bounded [0,1][0,1] scale (Eq. [7](#S3.E7 "In Continuous distributional distance metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")), where zero indicates identical distributions and one indicates disjoint support. In-sample, both metrics confirmed the ordering established by KS and AD: Bootstrap achieved the lowest values (W1=0.062W\_{1}=0.062, H=0.042H=0.042), followed by HMM-NJ (W1=0.081W\_{1}=0.081, H=0.073H=0.073) and then HMM-WJ (W1=0.101W\_{1}=0.101, H=0.075H=0.075), with Laplace, GARCH, and Gaussian progressively larger. HMM-NJ’s lower W1W\_{1} relative to HMM-WJ reflected the same distributional cost of the jump mechanism observed in the pass rates: enforcing tail-state persistence improved temporal fidelity at the expense of marginal fit. Out-of-sample, the continuous metrics revealed a pattern obscured by binary pass rates: GARCH’s W1W\_{1} increased sharply from 0.304 (IS) to 0.507 (OoS), making it the worst-performing model out-of-sample by a wide margin and worse even than the Gaussian baseline (OoS W1=0.452W\_{1}=0.452). This deterioration occurred despite GARCH recovering to an 80.3% KS pass rate out-of-sample, a recovery driven by reduced test power at T=249T=249 rather than genuine distributional fidelity. GARCH’s simulated kurtosis collapsed to 1.6 against an observed 6.9, a tail misspecification that W1W\_{1} captured directly while the binary pass rate obscured it. By contrast, HMM-NJ and HMM-WJ maintained the lowest W1W\_{1} among parametric models both in-sample and out-of-sample (OoS W1=0.258W\_{1}=0.258 and 0.2820.282 respectively), with Hellinger distances clustering narrowly between 0.207 and 0.210, confirming robust generalization to the held-out window.

#### Temporal fidelity.

We measured temporal quality using the mean absolute error of ACF​(|Gt|)\text{ACF}(|G\_{t}|) over lags 1–252. Bootstrap, Gaussian, and Laplace all produced an ACF-MAE of 0.060, which was expected because i.i.d. draws destroy all temporal dependence by construction. GARCH achieved the lowest ACF-MAE (0.031, SE 0.001) because its variance equation was explicitly designed to match autocorrelation structure; however, this advantage came at the cost of distributional fidelity, a tradeoff that the quality metrics exposed directly. HMM-NJ scored 0.059 (SE<{}<0.001), essentially indistinguishable from the i.i.d. floor, which confirmed that the standard transition matrix alone was structurally incapable of generating persistent volatility clustering (Figure [3](#S4.F3 "Figure 3 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel b). The GRU achieved 0.036 (SE<{}<0.001), the second-lowest ACF-MAE overall, demonstrating that the recurrent architecture effectively captured short-range temporal dependencies; however, this came at the cost of catastrophic distributional failure (0.6% KS pass rate). HMM-WJ scored 0.052 (SE<{}<0.001), the only non-GARCH, non-neural model to reduce ACF-MAE meaningfully below the i.i.d. baseline, though the gap to GARCH remained substantial (0.052 vs. 0.031). The improvement arose because approximately 24% of HMM-WJ paths contained at least one Poisson jump event that sustained ACF​(|Gt|)\text{ACF}(|G\_{t}|) decay across all lags, while the remaining 76% behaved identically to HMM-NJ. Importantly, the jump frequency is continuously tunable: increasing ϵ\epsilon produces more jump-containing paths and further reduces ACF-MAE, at the cost of degrading distributional fidelity. The grid search selected ϵ∗=10−4\epsilon^{\*}=10^{-4} because this value minimized the joint objective over both temporal and distributional quality (Equation [3](#S3.E3 "In Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")), meaning the 24% jump rate was the empirically optimal operating point for SPY, not a structural ceiling. The jump-duration mechanism was therefore the structural feature responsible for partially reproducing the ARCH effect, with its strength directly controlled by ϵ\epsilon.

#### Novelty, diversity, and parsimony.

We computed novelty (mean correlation distance to the observed series) and diversity (mean pairwise correlation distance among synthetic paths) to verify that the generators produced genuinely new, non-redundant scenarios. All seven models scored between 0.984 and 0.985 on both IS metrics, which confirmed that no generator memorized the training data and that synthetic paths were mutually independent. This uniformity was expected: all generators produced stochastic paths that were uncorrelated with any specific historical realization. Finally, HMM-WJ achieved the best joint distributional and temporal quality among all parametric models with four scalar parameters requiring explicit estimation: the Laplace location μL\mu\_{L} and scale bLb\_{L} (MLE), and the jump hyperparameters ϵ\epsilon and λ\lambda (grid search). The N×NN\times N transition matrix is a non-parametric empirical estimate obtained by direct counting and is therefore not a free parameter in the modeling sense. This compares favorably in interpretability with GARCH (three scalar parameters: ω\omega, α\alpha, β\beta) and Gaussian/Laplace baselines (two parameters each), though the transition matrix does add complexity that is not reflected in the scalar parameter count.

Table 2. In-sample and out-of-sample model comparison for SPY (1,000 simulated paths,
significance level α=0.05\alpha=0.05).
Bootstrap: i.i.d. resample of training data.
Gaussian/Laplace: i.i.d. draws from MLE-fitted distributions.
GARCH: GARCH(1,1) estimated by quasi-maximum likelihood.
GRU: 2-layer gated recurrent unit (Cho et al., [2014](#bib.bib1 "Learning phrase representations using RNN encoder-decoder for statistical machine translation")) with Gaussian output head (autoregressive generation).
HSMM: hidden semi-Markov model with K=8K=8 Laplace quantile states,
negative-binomial dwell times, and Student-t(ν=5\nu=5) emissions (Bulla and Bulla, [2006](#bib.bib9 "Stylized facts of financial time series and hidden semi-Markov models")).
HMM-NJ: hidden Markov model (N=100N=100 states) without jumps.
HMM-WJ: hybrid model with Poisson jump-duration extension.
ACF-MAE: mean absolute error of the ACF of |Gt||G\_{t}| over lags 1–252.
Wasserstein-1: mean absolute difference of sorted empirical quantiles (Eq. [6](#S3.E6 "In Continuous distributional distance metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")); units are daily excess growth rates.
Hellinger: histogram-based distributional overlap distance in [0,1][0,1] (Eq. [7](#S3.E7 "In Continuous distributional distance metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")); H=0H=0 is identical, H=1H=1 is disjoint.
Novelty: mean correlation distance 1−|ρ|1-|\rho| between each synthetic path and the observed series.
Diversity: mean pairwise correlation distance among synthetic paths.
Coverage: fraction of 99 empirical quantiles (1st–99th) falling within the
[5th, 95th] percentile envelope of the corresponding synthetic quantiles.
Standard errors in parentheses: binomial SE for pass rates,
std/n\text{std}/\!\sqrt{n} for kurtosis, novelty, Wasserstein-1, and Hellinger,
bootstrap SE (B=500B=500) for ACF-MAE, diversity, and coverage.
Arrows indicate preferred direction: ↑\uparrow higher is better,
↓\downarrow lower is better, ≈\approx closer to observed is better.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metric | Bootstrap | Gaussian | Laplace | GARCH(1,1) | GRU | HSMM | HMM-NJ | HMM-WJ |
| In-sample: 2,766 trading days (2014–2024) | | | | | | | | |
| KS pass rate (%) ↑\uparrow | 100.0 (<<0.1) | 0.0 (<<0.1) | 44.0 (1.6) | 5.5 (0.7) | 0.6 (0.2) | 82.0 (1.2) | 99.7 (0.2) | 97.6 (0.5) |
| AD pass rate (%) ↑\uparrow | 99.7 (0.2) | 0.0 (<<0.1) | 43.3 (1.6) | 1.9 (0.4) | 0.2 (0.1) | 42.5 (1.6) | 99.1 (0.3) | 91.3 (0.9) |
| Excess kurtosis (observed) | 7.715 | | | | | | | |
| Excess kurtosis (simulated) ≈\approx | 7.6 (0.08) | −-0.0 (<<0.01) | 3.0 (0.02) | 8.2 (0.37) | 5.7 (0.16) | 4.8 (0.08) | 8.1 (0.14) | 7.6 (0.14) |
| ACF-MAE ↓\downarrow | 0.060 (<<0.001) | 0.060 (<<0.001) | 0.060 (<<0.001) | 0.031 (0.001) | 0.036 (<<0.001) | 0.059 (<<0.001) | 0.059 (<<0.001) | 0.052 (<<0.001) |
| Novelty ↑\uparrow | 0.985 (<<0.001) | 0.984 (<<0.001) | 0.985 (<<0.001) | 0.985 (<<0.001) | 0.984 (<<0.001) | 0.985 (<<0.001) | 0.985 (<<0.001) | 0.984 (<<0.001) |
| Diversity ↑\uparrow | 0.985 (<<0.001) | 0.985 (<<0.001) | 0.985 (<<0.001) | 0.985 (<<0.001) | 0.984 (<<0.001) | 0.985 (<<0.001) | 0.984 (<<0.001) | 0.984 (<<0.001) |
| Coverage (%) ↑\uparrow | 100.0 (<<0.1) | 13.1 (0.1) | 37.4 (1.5) | 29.3 (1.4) | 17.2 (0.5) | 68.7 (1.1) | 100.0 (<<0.1) | 100.0 (<<0.1) |
| Wasserstein-1 ↓\downarrow | 0.062 (0.001) | 0.399 (0.001) | 0.138 (0.001) | 0.304 (0.006) | 0.421 (0.003) | 0.176 (0.001) | 0.081 (0.001) | 0.101 (0.001) |
| Hellinger dist ↓\downarrow | 0.042 (<<0.001) | 0.148 (<<0.001) | 0.072 (<<0.001) | 0.100 (0.001) | 0.134 (0.001) | 0.113 (<<0.001) | 0.073 (<<0.001) | 0.075 (<<0.001) |
| Out-of-sample: 249 trading days (2025) | | | | | | | | |
| KS pass rate (%) ↑\uparrow | 97.4 (0.5) | 62.2 (1.5) | 88.0 (1.0) | 80.3 (1.3) | 71.8 (1.4) | 96.2 (0.6) | 96.7 (0.6) | 94.4 (0.7) |
| AD pass rate (%) ↑\uparrow | 98.5 (0.4) | 46.3 (1.6) | 92.9 (0.8) | 72.0 (1.4) | 44.8 (1.6) | 96.7 (0.6) | 96.7 (0.6) | 95.1 (0.7) |
| Excess kurtosis (observed) | 6.867 | | | | | | | |
| Excess kurtosis (simulated) ≈\approx | 6.0 (0.18) | −-0.0 (<<0.01) | 2.7 (0.05) | 1.6 (0.07) | 2.9 (0.10) | 4.1 (0.13) | 6.4 (0.22) | 6.1 (0.13) |
| ACF-MAE ↓\downarrow | 0.043 (<<0.001) | 0.043 (<<0.001) | 0.043 (<<0.001) | 0.026 (<<0.001) | 0.033 (<<0.001) | 0.042 (<<0.001) | 0.041 (<<0.001) | 0.039 (<<0.001) |
| Novelty ↑\uparrow | 0.949 (0.001) | 0.950 (0.001) | 0.952 (0.001) | 0.951 (0.001) | 0.945 (0.001) | 0.948 (0.001) | 0.948 (0.001) | 0.946 (0.001) |
| Diversity ↑\uparrow | 0.950 (<<0.001) | 0.949 (<<0.001) | 0.949 (<<0.001) | 0.950 (<<0.001) | 0.947 (<<0.001) | 0.949 (<<0.001) | 0.948 (<<0.001) | 0.948 (<<0.001) |
| Coverage (%) ↑\uparrow | 100.0 (<<0.1) | 36.4 (1.9) | 74.7 (1.0) | 96.0 (1.3) | 77.8 (2.9) | 100.0 (0.2) | 100.0 (<<0.1) | 100.0 (<<0.1) |
| Wasserstein-1 ↓\downarrow | 0.232 (0.002) | 0.452 (0.002) | 0.263 (0.002) | 0.507 (0.018) | 0.488 (0.005) | 0.287 (0.002) | 0.258 (0.002) | 0.282 (0.006) |
| Hellinger dist ↓\downarrow | 0.205 (0.001) | 0.235 (0.001) | 0.211 (0.001) | 0.232 (0.001) | 0.240 (0.001) | 0.239 (0.001) | 0.207 (0.001) | 0.210 (0.001) |
| Parameters estimated111The N×NN\times N transition matrix in HMM-NJ and HMM-WJ is computed by direct counting of observed state transitions; it is a sufficient statistic of the data, not a fitted parameter. The counts listed here reflect only the scalar parameters requiring estimation (MLE or grid search). | 0 | 2 | 2 | 3 | 37,954 | 18 | 2 | 4 |



![Refer to caption](2603.10202v1/x2.png)

Three-panel figure comparing generative models for SPY. Panel (a) shows marginal density histograms of excess growth rates with KS pass rates annotated; HMM variants closely match the empirical heavy-tailed distribution while GARCH and Gaussian fail. Panel (b) shows autocorrelation functions of absolute returns at lags 1 to 252; HMM-WJ reproduces slow ACF decay while HMM-NJ and i.i.d. baselines collapse near zero. Panel (c) shows tail Q-Q plots at the 0.1st through 99.9th percentile region; HMM-WJ provides the closest quantile match in the extremes.

Figure 3. Head-to-head in-sample model comparison for SPY (N=100N=100, 1,000 simulated paths).
Panel (a): marginal density of excess growth rates with IS KS pass rates annotated.
GARCH(1,1) fails the two-sample KS test on 95% of paths (pass rate 5.5%), indicating a
systematic shape mismatch with the empirical distribution. Both HMM variants pass at
rates ≥97%\geq\!97\%, confirming that the Student-t emission structure adequately captures the observed
heavy tails. Out-of-sample, HMM-WJ maintains 94% KS pass rate, though HMM-NJ
achieves a higher 97%; GARCH recovers partially (OoS 80%).
Panel (b): autocorrelation function of absolute excess growth rates,
ACF​(|Gt|)\mathrm{ACF}(|G\_{t}|), at lags 1–252 (shaded bands: 10th–90th percentile across paths).
HMM-NJ is structurally incapable of producing persistent volatility clustering:
without a jump mechanism the latent states are i.i.d. conditional on the Markov chain,
so ACF​(|Gt|)≈0\mathrm{ACF}(|G\_{t}|)\approx 0 for all lags beyond one (dotted curve).
HMM-WJ generates a *mixture* of two path families under the same model:
approximately 76% of IS paths contain no Poisson jump and therefore behave
identically to HMM-NJ (dashed curve, near zero); the remaining ∼\sim24% of paths
contain at least one jump event and sustain substantial ACF​(|Gt|)\mathrm{ACF}(|G\_{t}|) decay
across all lags (solid navy curve ±\pm band).
The jump frequency, and hence the fraction of the ensemble exhibiting slow ACF decay, is
controlled by the tail-entry probability ϵ\epsilon, making the volatility-clustering strength
directly tunable.
Panel (c): tail Q-Q plot at the 0.1st–99.9th percentile region; HMM-WJ provides the
closest mean quantile match in the extreme tails.

### 4.4. Out-of-sample evaluation

We evaluated all eight generators on a held-out window of 249 trading days (January 2 through December 31, 2025) using the same metrics as the in-sample analysis (Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). Because the OoS window was roughly one-ninth as long as the training set, all two-sample tests had lower statistical power; pass rates therefore rose mechanically across every model, and the meaningful comparison was relative ranking rather than absolute level.

#### Baselines and distributional fidelity.

We observed that Bootstrap resampling achieved OoS KS and AD pass rates of 97.4% (SE 0.5) and 98.5% (SE 0.4), remaining near the ceiling. The Gaussian baseline rose from 0% IS to 62.2% (SE 1.5) KS and 46.3% (SE 1.6) AD, and Laplace from 44% IS to 88.0% (SE 1.0) KS and 92.9% (SE 0.8) AD; these improvements reflected the reduced test power, not genuine distributional fit, as confirmed by their kurtosis values (Gaussian 0.0, Laplace 2.7 against an observed 6.9). GARCH recovered to 80.3% (SE 1.3) KS and 72.0% (SE 1.4) AD, but its simulated kurtosis collapsed to 1.6, which indicated that GARCH failed to preserve tail behavior outside the training window. The GRU rose to 71.8% (SE 1.4) KS and 44.8% (SE 1.6) AD, with a Wasserstein-1 of 0.488 that was the second worst among all models, confirming that the variance collapse observed in-sample persisted out-of-sample. HMM-NJ achieved 96.7% (SE 0.6) and 96.7% (SE 0.6), and HMM-WJ achieved 94.4% (SE 0.7) and 95.1% (SE 0.7), with simulated kurtosis of 6.4 and 6.1 respectively against an observed 6.9. Both HMM variants generalized robustly, though the OoS ordering reversed the IS pattern: HMM-NJ now outperformed HMM-WJ on both pass rates and on Wasserstein-1 (0.258 vs. 0.282), and the HSMM achieved the highest OoS AD pass rate (96.7%) among all parametric models. This reversal suggested that the IS-calibrated jump parameters introduced a mild form of overfitting to the training window’s temporal structure, slightly degrading OoS marginal fit.

#### Coverage, temporal fidelity, novelty, and diversity.

Quantile coverage separated the models: Bootstrap, HMM-NJ, and HMM-WJ maintained 100%, GARCH recovered to 96.0% (from 29.3% IS), and Laplace reached 74.7%, while Gaussian remained low at 36.4%. OoS ACF-MAE values were lower across the board because the shorter window reduced autocorrelation estimation precision: Bootstrap, Gaussian, and Laplace all scored 0.043, GARCH achieved 0.026, HMM-NJ 0.041, and HMM-WJ 0.039. The gap between HMM-NJ and HMM-WJ narrowed from 0.007 IS to 0.002 OoS, which reflected reduced ACF estimation power rather than convergence in temporal quality. Novelty and diversity remained uniformly high across all models (0.948–0.952), confirming that no generator memorized the training data even in a shorter evaluation window.

#### Summary of model tradeoffs.

Across the full metric suite, no single model dominated all quality dimensions simultaneously (Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). GARCH(1,1) achieved the best temporal fidelity (ACF-MAE 0.031 IS, 0.026 OoS) but the worst distributional fit among parametric models (5.5% IS KS). The GRU achieved the second-best temporal fidelity (0.036 IS, 0.033 OoS) but the worst distributional fit overall (0.6% IS KS, W1=0.421W\_{1}=0.421), demonstrating that even a flexible neural architecture with nearly 38,000 trainable parameters could not jointly capture both the marginal distribution and the temporal structure of equity returns. HMM-NJ achieved the highest distributional pass rates (99.7% IS KS) and the lowest Wasserstein-1 distance (0.081 IS, 0.258 OoS) but could not reproduce volatility clustering at all (ACF-MAE at the i.i.d. floor). HMM-WJ occupied the Pareto frontier between these extremes: it was the only model to reduce ACF-MAE below the i.i.d. baseline while maintaining distributional pass rates above 91%, though it was not best-in-class on either dimension individually. This tradeoff was inherent to the jump mechanism, which improved temporal fidelity by forcing tail-state persistence at a measurable cost to marginal distributional fit.

To verify that these findings were not specific to the SPY market factor, we fitted standalone HMM-NJ and HMM-WJ models to three individual equities with distinct risk profiles: NVDA (high-beta technology), JNJ (low-beta health care), and JPM (moderate-beta financials). In-sample KS pass rates exceeded 91% for all tickers under both model variants. The grid search selected ϵ∗=10−4\epsilon^{\*}=10^{-4} for all three assets, but the optimal jump duration λ∗\lambda^{\*} varied systematically: λ∗=160\lambda^{\*}=160 for NVDA and JPM (assets with pronounced volatility clustering) versus λ∗=30\lambda^{\*}=30 for JNJ (a defensive stock with shorter-lived volatility episodes). This pattern suggested that the jump mechanism automatically calibrated to each asset’s clustering intensity, with λ\lambda scaling with the persistence of tail-state occupancy (Online Appendix S5, Table [T2](#Sx4.T2 "Table T2 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")).

Nonetheless, the out-of-sample period exposed the stationarity assumption embedded in the IS-calibrated jump parameters. The distribution of KS pp-values shifted leftward from IS to OoS, reflecting the expected distributional degradation when stationary parameters were applied to a period with elevated macro uncertainty (Figure [4](#S4.F4 "Figure 4 ‣ Summary of model tradeoffs. ‣ 4.4. Out-of-sample evaluation ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panels a–b). The observed ACF of |Gt||G\_{t}| in the 2025 window exceeded the HMM-WJ simulation band at medium-to-long lags, indicating that (ϵ∗,λ∗)(\epsilon^{\*},\lambda^{\*}) underestimated the frequency and persistence of volatility episodes in this period and that the jump parameters were regime-dependent (Figure [4](#S4.F4 "Figure 4 ‣ Summary of model tradeoffs. ‣ 4.4. Out-of-sample evaluation ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel d). Despite this ACF gap, the observed marginal density remained within the simulation envelope, confirming adequate distributional coverage even under regime shift (Figure [4](#S4.F4 "Figure 4 ‣ Summary of model tradeoffs. ‣ 4.4. Out-of-sample evaluation ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel c).

![Refer to caption](2603.10202v1/x3.png)

Four-panel statistical validation figure for HMM-WJ. Panel (a) shows in-sample KS p-value histograms across 1000 simulated paths, uniformly distributed indicating good fit. Panel (b) shows out-of-sample KS p-value histograms, still broadly uniform. Panel (c) compares the in-sample and out-of-sample marginal density of simulated paths against the observed SPY distribution with the simulation envelope shown. Panel (d) shows the ACF of absolute returns for in-sample and out-of-sample windows, with HMM-WJ simulation band compared to the observed SPY ACF.

Figure 4. Statistical validation of HMM-WJ (N=100N=100, 1,000 simulated paths, α=0.05\alpha=0.05).
Panels (a) and (b) show the distribution of two-sample KS pp-values in-sample and
out-of-sample, respectively; a well-calibrated generative model produces pp-values that are
approximately uniform above the significance threshold. The leftward shift from (a) to (b)
reflects the expected distributional degradation when stationary parameters are applied to a
regime with elevated macro uncertainty.
Panel (c) shows the out-of-sample marginal density fan chart; the observed density (dashed red)
falls within the 10th–90th percentile simulation envelope, confirming adequate distributional
coverage despite the regime shift.
Panel (d) shows the ACF of |Gt||G\_{t}| in the out-of-sample window. The observed ACF (dashed red)
exceeds the simulation band at medium-to-long lags, indicating that the 2025 test period
exhibited stronger volatility clustering than the IS-calibrated jump parameters
(ϵ∗,λ∗)(\epsilon^{\*},\lambda^{\*}) predict. This gap provides direct evidence that the jump
hyperparameters are regime-dependent and motivates the time-varying extensions discussed in
Section [5](#S5 "5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").

### 4.5. Multi-asset extension

We propagated HMM-WJ SPY paths through a Single-Index Model for 424 S&P 500 constituents, with G^i,t=α^i+β^i​GSPY,t+η^i,t\hat{G}\_{i,t}=\hat{\alpha}\_{i}+\hat{\beta}\_{i}G\_{{\rm SPY},t}+\hat{\eta}\_{i,t} estimated by OLS on the training window and idiosyncratic shocks drawn by resampling empirical residuals. This yielded a median IS KS pass rate of 66.7% and a mean of 58.4% across the universe (Figure [5](#S5.F5 "Figure 5 ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel b; Table [3](#S4.T3 "Table 3 ‣ 4.5. Multi-asset extension ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). These rates were lower than the 97.6% achieved for SPY alone and reflected the well-known limitation that a single-factor linear decomposition with symmetric residuals could not fully capture asset-specific tail behavior, skewness, or sector-level dynamics. The SIM Ri2R^{2}\_{i} varied widely across GICS sectors, from near-zero for defensive and low-correlation names to above 0.8 for broad-market ETFs (Figure [5](#S5.F5 "Figure 5 ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel a), and the degradation in KS pass rate concentrated among assets with low Ri2R^{2}\_{i}. High-β\beta assets closely tracking SPY retained pass rates above 80%, which suggested that the HMM-WJ generative engine was not the bottleneck; the limiting factor was the expressiveness of the factor model (Figure [5](#S5.F5 "Figure 5 ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel c).

Out-of-sample KS pass rates across 417 surviving assets reached a mean of 82.1% and a median of 91.8%, confirming that the SIM extension generalized to the test window (Table [3](#S4.T3 "Table 3 ‣ 4.5. Multi-asset extension ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). The correlation-distance distribution between simulated and historical paths yielded a mean distance of 1−ρ≈1.01-\rho\approx 1.0, which confirmed that the framework produced temporally independent realisations rather than tracking specific historical events, consistent with its role as a scenario generation tool rather than a forecasting instrument (Figure [4](#S4.F4 "Figure 4 ‣ Summary of model tradeoffs. ‣ 4.4. Out-of-sample evaluation ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")).

Table 3. Cross-sectional summary statistics for the Single-Index Model (SIM) extension
across S&P 500 constituents. Individual asset paths are generated as
G^i,t=α^i+β^i​GSPY,t+η^i,t\hat{G}\_{i,t}=\hat{\alpha}\_{i}+\hat{\beta}\_{i}G\_{{\rm SPY},t}+\hat{\eta}\_{i,t}
where GSPY,tG\_{{\rm SPY},t} is drawn from HMM-WJ (N=100N=100) simulated paths
and η^i,t\hat{\eta}\_{i,t} is resampled from empirical residuals.
KS pass rates computed over 1,000 paths at α=0.05\alpha=0.05.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Statistic | Mean | Median | 5th pct | 95th pct |
| In-sample (424 assets, 2,766 trading days, 2014–2024) | | | | |
| KS pass rate (%) | 58.4 | 66.7 | 2.5 | 96.0 |
| SIM R2R^{2} | 0.298 | 0.295 | 0.107 | 0.507 |
| β^\hat{\beta} (factor loading) | 1.066 | 1.086 | 0.480 | 1.657 |
| α^\hat{\alpha} (intercept) | −0.0328-0.0328 | −0.0196-0.0196 | −0.2037-0.2037 | 0.0964 |
| Out-of-sample (417 assets, 249 trading days, 2025) | | | | |
| KS pass rate (%) | 82.1 | 91.8 | 23.8 | 99.0 |
| SIM R2R^{2} | 0.142 | 0.142 | −0.169-0.169 | 0.479 |
| β^\hat{\beta} (factor loading) | 1.064 | 1.084 | 0.482 | 1.660 |
| α^\hat{\alpha} (intercept) | −0.0320-0.0320 | −0.0186-0.0186 | −0.2035-0.2035 | 0.0965 |

## 5. Discussion

The empirical results established that the hybrid HMM framework generates synthetic equity paths whose distributional and temporal properties closely match those of historical data, both in-sample and out-of-sample. In this section we interpret the key findings, discuss their practical implications, and identify the limitations that inform the scope of these conclusions.

![Refer to caption](2603.10202v1/x4.png)

Three-panel figure showing the multi-asset SIM extension across 424 S&P 500 constituents. Panel (a) shows a bar chart of SIM regression R-squared values by GICS sector, indicating fit quality of the single-factor decomposition. Panel (b) shows a histogram of KS pass rates across all 424 assets, with most assets achieving acceptable distributional fidelity. Panel (c) shows representative marginal density comparisons for three individual assets spanning a wide range of systematic risk exposure, each comparing the observed and simulated excess growth rate distributions.

Figure 5. Multi-asset extension via the Single-Index Model (SIM) across 424 S&P 500
constituents. Panel (a) summarizes the SIM regression fit quality by GICS sector.
Panel (b) shows that KS distributional consistency is maintained across the full asset
universe when paths are generated via the factor structure
G^i,t=α^i+β^i​GSPY,t+η^i,t\hat{G}\_{i,t}=\hat{\alpha}\_{i}+\hat{\beta}\_{i}G\_{{\rm SPY},t}+\hat{\eta}\_{i,t}.
Panel (c) illustrates representative marginal density comparisons for three assets spanning
a wide range of systematic risk exposure.

### 5.1. The role of the jump-duration mechanism

The comparison between HMM-NJ and HMM-WJ isolated the contribution of the Poisson jump-duration mechanism. Without jumps, the Markov chain transitioned out of tail states within one to two steps on average, producing an ACF of |Gt||G\_{t}| that decayed too quickly and failing to reproduce the volatility clustering observed in the data. Introducing jumps forced the model to dwell in high-volatility regimes for empirically realistic durations, and approximately 24% of simulated paths contained at least one such episode, sufficient to shift the ensemble-level ACF toward the empirical profile. This result is consistent with the broader literature on regime-switching models, where standard HMM specifications have repeatedly been found to undergenerate volatility persistence (Rydén et al., [1998](#bib.bib8 "Stylized facts of daily return series and the hidden Markov model"); Bulla and Bulla, [2006](#bib.bib9 "Stylized facts of financial time series and hidden semi-Markov models")), and it demonstrated that a minimal two-parameter extension (ϵ\epsilon, λ\lambda) could substantially mitigate the issue without the computational overhead of hierarchical or semi-Markov alternatives. The HSMM baseline (Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")) provided a direct test of the semi-Markov approach proposed by Bulla and Bulla ([2006](#bib.bib9 "Stylized facts of financial time series and hidden semi-Markov models")). Despite using the same Student-t emissions and a sweep over K∈{3,4,5,6,8}K\in\{3,4,5,6,8\} states with negative-binomial dwell-time distributions, the HSMM achieved only 82.0% IS KS pass rate (vs. 97.6% for HMM-WJ) and an ACF-MAE of 0.059, identical to the i.i.d. floor. The fundamental limitation was structural: with K=8K=8 states, empirical dwell times averaged only 1.1–1.8 steps, too short for the negative-binomial distribution to depart meaningfully from geometric (memoryless) behavior. The semi-Markov approach requires coarse states to generate long dwell times, but coarse states sacrifice distributional resolution; our framework resolves this tradeoff by maintaining fine state resolution (N=100N=100) for distributional fidelity while using the jump mechanism to enforce tail-state persistence externally. Notably, the jump-duration mechanism’s advantage over the semi-Markov approach is not an artifact of the Student-t emission upgrade: even under the original Gaussian emissions, HMM-WJ achieved 97.0% IS KS (vs. 82.0% for HSMM) and an ACF-MAE of 0.052 (vs. 0.059), with only 4 estimated parameters compared with 18 (Table [T3](#Sx4.T3 "Table T3 ‣ S6. Emission distribution and semi-Markov comparison ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") in Online Appendix S6). This confirmed that the structural advantage of the jump mechanism, maintaining fine state resolution for distributional fidelity while enforcing tail-state persistence externally, was independent of the emission distribution choice. The cross-asset analysis (Online Appendix S5) reinforced this interpretation: the grid search selected λ∗=160\lambda^{\*}=160 for NVDA and JPM (assets with pronounced volatility clustering) but only λ∗=30\lambda^{\*}=30 for JNJ (a defensive stock with shorter-lived volatility episodes), indicating that λ\lambda adapted automatically to each asset’s clustering intensity. For JNJ, the jump mechanism contributed almost no improvement over the standard HMM (ACF-MAE 0.027→\to0.026), consistent with the expectation that assets with weak volatility clustering exhibit less persistent tail-state occupancy and therefore require shorter, or fewer, jump episodes.

The tradeoff between distributional fidelity and temporal structure, visible across the full model comparison, deserves emphasis. HMM-WJ was not best-in-class on any single metric: HMM-NJ achieved higher distributional pass rates and lower Wasserstein-1 distances both in-sample and out-of-sample; GARCH and the GRU achieved substantially lower ACF-MAE; and in the OoS window, both HMM-NJ and the HSMM achieved higher KS and AD pass rates than HMM-WJ (Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")). The GRU baseline was particularly instructive: despite nearly 38,000 trainable parameters, the autoregressive neural architecture learned temporal dynamics effectively (IS ACF-MAE of 0.036, second only to GARCH) but suffered from variance collapse that reduced simulated standard deviation by 30% and drove the IS KS pass rate below 1%. This failure mode, where flexible function approximation captures autocorrelation structure but fails to preserve the marginal distribution, is the mirror image of the HMM-NJ pattern and illustrates why jointly capturing both quality dimensions remains a fundamental challenge for synthetic financial data generation. The value of HMM-WJ lay in avoiding the severe failures that each alternative exhibited on its weakest dimension. GARCH(1,1) achieved the lowest ACF-MAE because its variance equation was explicitly parameterized to match autocorrelation dynamics, yet its marginal distribution was systematically inconsistent with the data (IS KS pass rate of 5.5%). The hybrid HMM reversed this tradeoff: the Student-t emissions delivered high distributional fidelity, and the jump mechanism provided sufficient temporal structure. Neither model dominated on all metrics simultaneously, but the HMM framework provided a more balanced quality profile for synthetic data applications where both distributional and temporal fidelity matter. Crucially, the volatility-clustering strength of HMM-WJ is not fixed: increasing ϵ\epsilon raises the fraction of paths that contain jump episodes and drives ACF-MAE toward zero, while decreasing ϵ\epsilon recovers the pure Markov baseline. The grid search selected the value of ϵ\epsilon that jointly optimized temporal and distributional fidelity, so the observed ACF-MAE reflects the best achievable balance for SPY rather than a structural limitation of the mechanism.

The Wasserstein-1 and Hellinger distances exposed a further weakness of GARCH that binary pass rates obscured. Out-of-sample, GARCH’s W1W\_{1} increased from 0.304 (IS) to 0.507 (OoS), making it the worst-performing model out-of-sample and worse even than the Gaussian i.i.d. baseline (W1=0.452W\_{1}=0.452). This deterioration occurred despite GARCH recovering to an 80.3% OoS KS pass rate, a recovery driven by reduced test power at T=249T=249 rather than genuine distributional fidelity, and an artifact of the binary pass-rate framing that W1W\_{1} avoids. The underlying cause was GARCH’s simulated kurtosis collapsing to 1.6 OoS against an observed 6.9, indicating that the IS-calibrated variance parameters failed to preserve tail behavior outside the training window. By contrast, HMM-NJ and HMM-WJ maintained the lowest W1W\_{1} among parametric models in both windows (OoS W1=0.258W\_{1}=0.258 and 0.2820.282 respectively), with Hellinger distances of 0.207 and 0.210, confirming that the Student-t emission structure generalized robustly to a regime with elevated macro uncertainty where GARCH’s parametric assumptions broke down.

### 5.2. Practical implications

The proposed framework offers practical utility for both risk management and the broader synthetic data community. Generative models that reproduce the stylized facts of financial markets enable stress testing under market regimes that are statistically plausible but not historically observed, addressing a key limitation of scenario libraries derived solely from empirical records. The interpretable regime structure, where each hidden state corresponds to a quantile-defined segment of the excess growth rate distribution, facilitates communication between quantitative analysts and risk managers; states can be labeled (e.g., crash, bear, neutral, bull, rally) and linked to economic narratives. The model’s computational efficiency further supports Monte Carlo-based risk metrics such as Value-at-Risk and Conditional Value-at-Risk at scale across large asset universes (Glasserman, [2003](#bib.bib16 "Monte Carlo Methods in Financial Engineering")).

The avoidance of the Baum-Welch EM algorithm, made possible by the quantile-based state partition that explicitly assigns each observation to a hidden state, eliminates convergence sensitivity to initialization and reduces computational cost. This property matters for large-scale pipelines: fitting the model to 424 assets requires only empirical counting and a two-parameter grid search, making it feasible to regenerate synthetic scenarios on a daily or weekly cadence as new data arrive. For synthetic data applications where privacy is a concern, such as sharing simulated portfolios or stress-test scenarios with external parties, the framework offers implicit privacy protection through its generative structure: synthetic paths are sampled from the learned Markov chain and emission distribution rather than perturbed copies of historical records. The novelty and diversity metrics in Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") confirm that no simulated path is a near-replica of the training data (novelty >0.98>0.98), and paths are mutually dissimilar (diversity >0.98>0.98). While these properties reduce the risk of memorization, the framework does not provide formal differential privacy guarantees (Dwork, [2006](#bib.bib61 "Differential privacy")); quantifying membership inference risk and integrating calibrated noise mechanisms remain directions for future work (Stadler et al., [2022](#bib.bib64 "Synthetic data – anonymisation groundhog day")).

More broadly, the quality evaluation methodology demonstrated here, combining binary distributional fidelity tests (KS, AD) with continuous distance metrics (W1W\_{1}, Hellinger) and temporal structure metrics (ACF-MAE), and reporting standard errors across Monte Carlo ensembles, provides a reusable template for assessing synthetic time series quality in other domains where temporal dependence structures are critical to downstream applications (Stenger et al., [2024](#bib.bib60 "Thinking in categories: A survey on assessing the quality for time series synthesis")).

### 5.3. Limitations

Several limitations inform the interpretation of these results. First, the model assumes stationarity of the transition matrix and jump hyperparameters across the full in-sample window. The out-of-sample ACF analysis (Figure [4](#S4.F4 "Figure 4 ‣ Summary of model tradeoffs. ‣ 4.4. Out-of-sample evaluation ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), panel d) provided direct evidence of this limitation: the IS-calibrated (ϵ∗,λ∗)(\epsilon^{\*},\lambda^{\*}) underestimated volatility clustering persistence in the 2025 test window, consistent with the elevated macro uncertainty of that period. Structural breaks in market microstructure, such as those accompanying regulatory changes or the COVID-19 shock, may not be adequately captured by a single static transition matrix.

Second, the quantile-based state partition is fixed at estimation time and does not adapt to evolving volatility regimes, potentially overweighting the central mass relative to the tails during prolonged market stress. Third, the Single-Index Model extension imposes a linear, single-factor decomposition whose median IS KS pass rate of 66.7% across 424 assets confirmed that it could not fully capture asset-specific tail behavior, skewness, or sector dynamics (Sharpe, [1963](#bib.bib42 "A simplified model for portfolio analysis"); Fama and French, [1993](#bib.bib43 "Common risk factors in the returns on stocks and bonds")); however, the architecture is modular, and replacing the SIM with a richer factor specification would not require modifying the underlying Markov chain machinery. Finally, the out-of-sample evaluation covers a single 249-day window (full calendar year 2025), which limits the statistical power of out-of-sample inference; a rolling evaluation would provide a more robust assessment of generalization performance.

The two-sample KS and AD tests assume i.i.d. observations, but each simulated path exhibits temporal dependence by construction: volatility clustering induces positive autocorrelation in the tail-indicator process 𝟏​(Gt≤x)\mathbf{1}(G\_{t}\leq x), reducing the effective sample size below TT and potentially inflating pass rates slightly relative to what a block-bootstrap calibration would produce. The Wasserstein-1 and Hellinger distances in Table [2](#S4.T2 "Table 2 ‣ Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") carry no such sampling-distribution assumption and produce a consistent model ordering, corroborating the fidelity conclusions independently of this caveat.

## 6. Conclusion

We developed a hybrid hidden Markov model that generated synthetic equity paths whose statistical properties closely matched real market data across multiple quality dimensions simultaneously. No single model in our comparison dominated all metrics: GARCH(1,1) reproduced volatility clustering more accurately, and the standard HMM without jumps achieved higher distributional pass rates, but each exhibited severe failures on its weakest dimension. The hybrid framework occupied the Pareto frontier between distributional fidelity and temporal structure. The model partitioned excess growth rates into quantile-defined regimes and augmented normal regime-switching with a Poisson jump-duration mechanism that forced the model to linger in extreme states, partially reproducing the volatility clustering that standard HMMs miss. Applied to SPY over a ten-year training window and validated out-of-sample on the full calendar year 2025, the framework achieved in-sample KS pass rates of 97.6% and AD pass rates of 91.3%, with 94.4% and 95.1% out-of-sample, though these rates were 2–3 percentage points below the jump-free HMM-NJ variant, reflecting the distributional cost of enforcing tail-state persistence. The jump mechanism, governed by only two scalar hyperparameters, was the structural feature responsible for generating persistent high-volatility regimes, and the direct frequentist estimation strategy eliminated the computational cost and initialization sensitivity of the EM algorithm. A Single-Index Model extension scaled the approach to a 424-asset universe, providing a baseline for multi-asset synthetic scenario generation.

Several extensions follow naturally. Time-varying transition matrices, estimated via rolling windows or Bayesian online learning, would allow the model to adapt to structural regime shifts. Replacing the single-factor SIM with multi-factor specifications such as the Fama-French three- or five-factor model (Fama and French, [1993](#bib.bib43 "Common risk factors in the returns on stocks and bonds")), principal-component-based factor structures, or nonlinear residual generators could substantially improve asset-level distributional fidelity. Adaptive state definitions based on density clustering rather than fixed quantiles could improve tail coverage during crisis periods. Finally, embedding the hybrid HMM as the generative component within a portfolio optimization loop, where synthetic scenarios drive tail-risk objectives, would provide an end-to-end application of the framework.

## Conflict of Interest Statement

The authors declare that the research was conducted without any commercial or financial relationships that could potentially create a conflict of interest.

## Author Contributions

J.V. directed the study. A.A. developed the model and simulation code, conducted the in-sample and out-of-sample analysis, and generated the figures. Both authors edited and reviewed the final manuscript.

## Data Availability Statement

The model code, simulation scripts, training and testing data are available under a Massachusetts Institute of Technology (MIT) license from the GitHub repository: <https://github.com/varnerlab/HMM-w-jumps-paper.git>

## References

* T. W. Anderson and D. A. Darling (1952)
  Asymptotic theory of certain “goodness of fit” criteria based on stochastic processes.
  The Annals of Mathematical Statistics 23 (2),  pp. 193–212.
  Cited by: [§3](#S3.SSx6.p3.1 "Statistical validation metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx6.p3.4 "Statistical validation metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* W. B. Arthur (2021)
  Foundations of complexity economics.
  Nature Reviews Physics 3,  pp. 136–145.
  External Links: [Document](https://dx.doi.org/10.1038/s42254-020-00273-3)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* S. A. Assefa, D. Dervovic, M. Mahfouz, R. E. Tillman, P. Reddy, and M. Veloso (2020)
  Generating synthetic data in finance: opportunities, challenges and pitfalls.
  In Proceedings of the First ACM International Conference on AI in Finance,
   pp. 1–8.
  External Links: [Document](https://dx.doi.org/10.1145/3383455.3422554)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.3](#S2.SS3.p1.1 "2.3. Synthetic data generation and deep generative models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. F. K. Au Yeung, Z. Wei, K. Y. Chan, H. Y. K. Lau, and K. C. Yiu (2020)
  Jump detection in financial time series using machine learning algorithms.
  Soft Computing 24 (3),  pp. 1789–1801.
  External Links: [Document](https://dx.doi.org/10.1007/s00500-019-04006-2)
  Cited by: [§1](#S1.p3.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* L. E. Baum, T. Petrie, G. Soules, and N. Weiss (1970)
  A maximization technique occurring in the statistical analysis of probabilistic functions of Markov chains.
  The Annals of Mathematical Statistics 41 (1),  pp. 164–171.
  External Links: [Document](https://dx.doi.org/10.1214/aoms/1177697196)
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2. Hidden Markov models and regime-switching ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* D. Berghaus, K. Cvejoski, P. Seifner, C. Ojeda, and R. J. Sanchez (2024)
  Foundation inference models for Markov jump processes.
  In Proceedings of the 38th International Conference on Neural Information Processing Systems,
   pp. 129407–129442.
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3. Synthetic data generation and deep generative models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. A. Bilmes (1998)
  A Gentle Tutorial of the EM Algorithm and its Application to Parameter Estimation for Gaussian Mixture and Hidden Markov Models.
  International Computer Science Institute.
  Cited by: [§3](#S3.SSx3.p2.4 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx3.p3.10 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* F. Black and M. Scholes (1973)
  The pricing of options and corporate liabilities.
  Journal of Political Economy 81 (3),  pp. 637–654.
  External Links: [Document](https://dx.doi.org/10.1086/260062)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* T. Bollerslev (1986)
  Generalized Autoregressive Conditional Heteroscedasticity.
  Journal of Econometrics 31 (3),  pp. 307–327.
  External Links: [Document](https://dx.doi.org/10.1016/0304-4076%2886%2990063-1)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. Bulla and I. Bulla (2006)
  Stylized facts of financial time series and hidden semi-Markov models.
  Computational Statistics & Data Analysis 51 (4),  pp. 2192–2209.
  External Links: [Document](https://dx.doi.org/10.1016/j.csda.2006.07.021)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.2](#S2.SS2.p2.1 "2.2. Hidden Markov models and regime-switching ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx3.p3.10 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§4.3](#S4.SS3.SSS0.Px1.p1.5 "Baseline anchors. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [Table 2](#S4.T2 "In Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [Table 2](#S4.T2.28.14 "In Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§5.1](#S5.SS1.p1.10 "5.1. The role of the jump-duration mechanism ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* D. Challet and Y.-C. Zhang (1997)
  Emergence of cooperation and organization in an evolutionary game.
  Physica A: Statistical Mechanics and its Applications 246 (3–4),  pp. 407–418.
  External Links: [Document](https://dx.doi.org/10.1016/S0378-4371%2897%2900419-6)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. J. Chen, L. Tan, and B. Zheng (2015)
  Agent-based model with multi-level herding for complex financial systems.
  Scientific Reports 5,  pp. 8399.
  External Links: [Document](https://dx.doi.org/10.1038/srep08399)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* U. Cherubini, E. Luciano, and W. Vecchiato (2004)
  Copula methods in finance.
   John Wiley & Sons.
  External Links: ISBN 9780470863459
  Cited by: [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* K. Cho, B. van Merrienboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio (2014)
  Learning phrase representations using RNN encoder-decoder for statistical machine translation.
  arXiv preprint arXiv:1406.1078.
  Cited by: [Table 2](#S4.T2 "In Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [Table 2](#S4.T2.28.14 "In Novelty, diversity, and parsimony. ‣ 4.3. In-sample distributional and temporal quality ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative Finance 1 (2),  pp. 223–236.
  External Links: [Document](https://dx.doi.org/10.1080/713665670)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.1](#S2.SS1.p1.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx3.p2.4 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx5.p1.3 "Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* R. Cont and J. Bouchaud (2000)
  Herd behavior and aggregate fluctuations in financial markets.
  Macroeconomic Dynamics 4 (2),  pp. 170–196.
  External Links: [Document](https://dx.doi.org/10.1017/S1365100500015029)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. G. Dias, J. K. Vermunt, and S. Ramos (2010)
  Mixture Hidden Markov Models in Finance Research.
  In Advances in Data Analysis, Data Handling and Business Intelligence,
   pp. 451–459.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-642-01044-6%5F41)
  Cited by: [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* F. X. Diebold and A. Inoue (2001)
  Long memory and regime switching.
  Journal of Econometrics 105 (1–2),  pp. 131–159.
  External Links: [Document](https://dx.doi.org/10.1016/S0304-4076%2801%2900073-2)
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* C. Dwork (2006)
  Differential privacy.
  In Automata, Languages and Programming (ICALP),
  Lecture Notes in Computer Science, Vol. 4052,  pp. 1–12.
  External Links: [Document](https://dx.doi.org/10.1007/11787006%5F1)
  Cited by: [§5.2](#S5.SS2.p2.2 "5.2. Practical implications ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* P. Embrechts, A. J. McNeil, and D. Straumann (2002)
  Correlation and dependence in risk management: properties and pitfalls.
  In Risk Management: Value at Risk and Beyond,
   pp. 176–223.
  External Links: [Document](https://dx.doi.org/10.1017/CBO9780511615337.008)
  Cited by: [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* R. F. Engle (1982)
  Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation.
  Econometrica 50 (4),  pp. 987–1007.
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* E. F. Fama and K. R. French (1993)
  Common risk factors in the returns on stocks and bonds.
  Journal of Financial Economics 33 (1),  pp. 3–56.
  External Links: [Document](https://dx.doi.org/10.1016/0304-405X%2893%2990023-5)
  Cited by: [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§5.3](#S5.SS3.p2.1 "5.3. Limitations ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§6](#S6.p2.1 "6. Conclusion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* E. F. Fama (1970)
  Efficient Capital Markets: A Review of Theory and Empirical Work.
  The Journal of Finance 25 (2),  pp. 383–417.
  External Links: [Document](https://dx.doi.org/10.2307/2325486)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§4.1](#S4.SS1.p1.8 "4.1. Descriptive statistics and stylized facts ‣ 4. Empirical Study ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. D. Farmer and S. Joshi (2002)
  The price dynamics of common trading strategies.
  Journal of Economic Behavior & Organization 49 (2),  pp. 149–171.
  External Links: [Document](https://dx.doi.org/10.1016/S0167-2681%2802%2900065-3)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. D. Farmer (2025)
  Quantitative agent-based models: a promising alternative for macroeconomics.
  Oxford Review of Economic Policy 41 (2),  pp. 571–590.
  External Links: [Document](https://dx.doi.org/10.1093/oxrep/graf027)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* T. Fischer and C. Krauss (2018)
  Deep learning with long short-term memory networks for financial market predictions.
  European Journal of Operational Research 270 (2),  pp. 654–669.
  External Links: [Document](https://dx.doi.org/10.1016/j.ejor.2017.11.054)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* P. Glasserman (2003)
  Monte Carlo Methods in Financial Engineering.
   Springer.
  External Links: [Document](https://dx.doi.org/10.1007/978-0-387-21617-1)
  Cited by: [§3](#S3.SSx3.p3.10 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx5.p2.13 "Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§5.2](#S5.SS2.p1.1 "5.2. Practical implications ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* C. M. Grinstead and J. L. Snell (1997)
  Introduction to Probability.
   American Mathematical Society.
  Cited by: [§3](#S3.SSx4.p1.9 "Growth rate generation. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. D. Hamilton (1989)
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  Econometrica 57 (2),  pp. 357–384.
  External Links: [Document](https://dx.doi.org/10.2307/1912559)
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2. Hidden Markov models and regime-switching ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. D. Hamilton (2018)
  Regime Switching Models.
  The New Palgrave Dictionary of Economics,  pp. 11421–11426.
  External Links: [Document](https://dx.doi.org/10.1057/978-1-349-95189-5%5F2459)
  Cited by: [§3](#S3.SSx4.p1.9 "Growth rate generation. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* S. L. Heston (1993)
  A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options.
  The Review of Financial Studies 6 (2),  pp. 327–343.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/6.2.327)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* S. Hochreiter and J. Schmidhuber (1997)
  Long Short-Term Memory.
  Neural Computation 9 (8),  pp. 1735–1780.
  External Links: [Document](https://dx.doi.org/10.1162/neco.1997.9.8.1735)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. Jordon, L. Szpruch, F. Houssiau, M. Bottarelli, G. Cherubin, C. Maple, S. N. Cohen, and A. Weller (2022)
  Synthetic data – what, why and how?.
  arXiv preprint arXiv:2205.03257.
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* C. Kim and C. R. Nelson (1999)
  Has the U.S. economy become more stable? A Bayesian approach based on a Markov-switching model of the business cycle.
  The Review of Economics and Statistics 81 (4),  pp. 608–616.
  External Links: [Document](https://dx.doi.org/10.1162/003465399558472)
  Cited by: [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* A. N. Kolmogorov (1933)
  Sulla determinazione empirica di una legge di distribuzione.
  Giornale dell’Istituto Italiano degli Attuari 4,  pp. 83–91.
  Cited by: [§3](#S3.SSx6.p2.7 "Statistical validation metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* S. Kotz, T. J. Kozubowski, and K. Podgórski (2001)
  The Laplace Distribution and Generalizations: A Revisit with Applications to Communications, Economics, Engineering, and Finance.
   Birkhauser.
  External Links: ISBN 9780817641665
  Cited by: [§3](#S3.SSx3.p2.4 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* S. G. Kou (2002)
  A Jump-Diffusion Model for Option Pricing.
  Management Science 48 (8),  pp. 1086–1101.
  External Links: [Document](https://dx.doi.org/10.1287/mnsc.48.8.1086.166)
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx3.p2.4 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx3.p4.6 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx5.p1.3 "Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* S. Kwon and Y. Lee (2024)
  Can GANs Learn the Stylized Facts of Financial Time Series?.
  In Proceedings of the 5th ACM International Conference on AI in Finance,
   pp. 126–133.
  External Links: [Document](https://dx.doi.org/10.1145/3677052.3698661)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.3](#S2.SS3.p1.1 "2.3. Synthetic data generation and deep generative models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* B. LeBaron (2006)
  Agent-based computational finance.
  In Handbook of Computational Economics, L. Tesfatsion and K. L. Judd (Eds.),
  Vol. 2,  pp. 1187–1233.
  External Links: [Document](https://dx.doi.org/10.1016/S1574-0021%2805%2902024-1)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* T. Lux and M. Marchesi (1999)
  Scaling and criticality in a stochastic multi-agent model of a financial market.
  Nature 397,  pp. 498–500.
  External Links: [Document](https://dx.doi.org/10.1038/17290)
  Cited by: [§2](#S2.p1.1 "2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* B. Mandelbrot (1963)
  The Variation of Certain Speculative Prices.
  The Journal of Business 36 (4),  pp. 394–419.
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.1](#S2.SS1.p1.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx3.p2.4 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx5.p1.3 "Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* R. C. Merton (1976)
  Option Pricing When Underlying Stock Returns Are Discontinuous.
  Journal of Financial Economics 3 (1-2),  pp. 125–144.
  External Links: [Document](https://dx.doi.org/10.1016/0304-405X%2876%2990022-2)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx5.p1.3 "Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* N. Nguyen (2018)
  Hidden Markov Model for Stock Trading.
  International Journal of Financial Studies 6 (2),  pp. 36.
  External Links: [Document](https://dx.doi.org/10.3390/ijfs6020036)
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2. Hidden Markov models and regime-switching ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* L. Rabiner and B. Juang (1986)
  An introduction to hidden Markov models.
  IEEE ASSP Magazine 3 (1),  pp. 4–16.
  External Links: [Document](https://dx.doi.org/10.1109/MASSP.1986.1165342)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.2](#S2.SS2.p1.1 "2.2. Hidden Markov models and regime-switching ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx3.p1.8 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* A. Rossi and G. M. Gallo (2006)
  Volatility estimation via hidden Markov models.
  Journal of Empirical Finance 13 (2),  pp. 203–230.
  External Links: [Document](https://dx.doi.org/10.1016/j.jempfin.2005.09.003)
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2. Hidden Markov models and regime-switching ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* T. Rydén, T. Teräsvirta, and S. Åsbrink (1998)
  Stylized facts of daily return series and the hidden Markov model.
  Journal of Applied Econometrics 13 (3),  pp. 217–244.
  External Links: [Document](https://dx.doi.org/10.1002/%28SICI%291099-1255%28199805/06%2913%3A3%3C217%3A%3AAID-JAE476%3E3.0.CO%3B2-V)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.2](#S2.SS2.p2.1 "2.2. Hidden Markov models and regime-switching ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx5.p1.3 "Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§5.1](#S5.SS1.p1.10 "5.1. The role of the jump-duration mechanism ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* G. W. Schwert (1989)
  Why Does Stock Market Volatility Change Over Time?.
  The Journal of Finance 44 (5),  pp. 1115–1153.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1989.tb02647.x)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx5.p1.3 "Hyperparameter optimization via grid search. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* W. F. Sharpe (1963)
  A simplified model for portfolio analysis.
  Management Science 9 (2),  pp. 277–293.
  External Links: [Document](https://dx.doi.org/10.1287/mnsc.9.2.277)
  Cited by: [§1](#S1.p3.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.4](#S2.SS4.p1.1 "2.4. Factor models and multi-asset extensions ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§3](#S3.SSx9.p1.2 "Single-Index Factor Model extension ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§5.3](#S5.SS3.p2.1 "5.3. Limitations ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* N. Smirnov (1948)
  Table for estimating the goodness of fit of empirical distributions.
  The Annals of Mathematical Statistics 19 (2),  pp. 279–281.
  Cited by: [§3](#S3.SSx6.p2.7 "Statistical validation metrics ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* T. Stadler, B. Oprisanu, and C. Troncoso (2022)
  Synthetic data – anonymisation groundhog day.
  In 31st USENIX Security Symposium (USENIX Security 22),
   pp. 1451–1468.
  Cited by: [§5.2](#S5.SS2.p2.2 "5.2. Practical implications ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* E. M. Stein and J. C. Stein (1991)
  Stock price distributions with stochastic volatility: an analytic approach.
  The Review of Financial Studies 4 (4),  pp. 727–752.
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1. Stylized facts and the limitations of parametric models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* M. Stenger, A. Bauer, T. Prantl, R. Leppich, N. Hudson, K. Chard, I. Foster, and S. Kounev (2024)
  Thinking in categories: A survey on assessing the quality for time series synthesis.
  Journal of Data and Information Quality 16 (2),  pp. 1–32.
  External Links: [Document](https://dx.doi.org/10.1145/3666006)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§5.2](#S5.SS2.p3.1 "5.2. Practical implications ‣ 5. Discussion ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* S. Takahashi, Y. Chen, and K. Tanaka-Ishii (2019)
  Modeling financial time-series with generative adversarial networks.
  Physica A: Statistical Mechanics and its Applications 527,  pp. 121261.
  External Links: [Document](https://dx.doi.org/10.1016/j.physa.2019.121261)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"),
  [§2.3](#S2.SS3.p1.1 "2.3. Synthetic data generation and deep generative models ‣ 2. Related Work ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* D. Toth and B. Jones (2019)
  Against the Norm: Modeling Daily Stock Returns with the Laplace Distribution.
  arXiv preprint arXiv:1906.10325.
  Cited by: [§3](#S3.SSx3.p2.4 "Discrete hidden Markov model. ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").
* J. Yoon, D. Jarrett, and M. van der Schaar (2019)
  Time-series generative adversarial networks.
  In Advances in Neural Information Processing Systems,
  Vol. 32.
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion").

## Online Appendix

### S1. Fitted model internals

This section visualizes the internal components of the fitted HMM-WJ model for SPY with N=100N=100 states.
We constructed the model by fitting a Laplace distribution to the observed excess growth rate series (2014–2024, 2,766 trading days), partitioning the support into NN equal-probability quantile bins, and estimating the 100×100100\times 100 transition matrix from consecutive state assignments (Algorithm [2](#alg2 "Algorithm 2 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion")).
Figure [S1](#Sx4.F1 "Figure S1 ‣ S1. Fitted model internals ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") displays three diagnostics.
Panel (a) confirms that the Laplace marginal closely matches the empirical CDF, validating the distributional assumption underlying the state partition.
Panel (b) reveals the banded structure of the transition matrix: most probability mass concentrates near the diagonal, reflecting the tendency of markets to transition between adjacent states rather than making large jumps.
Panel (c) exposes the key limitation of the pure Markov dynamics: the natural residence time 1/(1−Tk​k)1/(1-T\_{kk}) for every state, including the extreme tails, is only 1–2 steps.
This is far too short to reproduce the persistent volatility clustering observed in equity returns, motivating the Poisson jump-duration mechanism described in Section 3.3 of the main text.

![Refer to caption](2603.10202v1/x5.png)

Three-panel figure showing fitted HMM internals for SPY with N=100 states. Panel (a) overlays the fitted Laplace CDF on the empirical CDF with 99 vertical lines marking quantile boundaries. Panel (b) displays the 100-by-100 empirical transition matrix as a heatmap in log base 10 color scale, revealing a dominant near-diagonal band. Panel (c) plots expected natural residence time per state on a log scale, with bottom-tail states (1 to 5) shaded red and top-tail states (96 to 100) shaded teal; a dashed horizontal line marks the optimal mean jump duration of 100 steps.

Figure S1. Fitted model internals for SPY with N=100N=100 states.
Panel (a) overlays the fitted Laplace CDF on the empirical CDF; the 99 vertical lines mark the
equal-probability quantile boundaries that define the NN hidden states. The close agreement
confirms that the Laplace distribution is an accurate marginal model for the excess growth rate
data.
Panel (b) displays the empirical transition matrix 𝐓\mathbf{T} in log10\log\_{10} color scale;
the dominant near-diagonal band reflects short-range regime persistence.
Panel (c) plots the expected natural residence time 1/(1−Tk​k)1/(1-T\_{kk}) for each state on a
log10\log\_{10} scale, with the bottom tail set 𝒮−\mathcal{S}\_{-} (states 1–5, red shading) and
top tail set 𝒮+\mathcal{S}\_{+} (states 96–100, teal shading) highlighted. Under pure Markovian
dynamics every state, including the tail states, exits within 1–2 steps on average, far too
quickly to reproduce empirical volatility clustering. The dashed horizontal line marks the mean
mean jump duration λ∗=100\lambda^{\*}=100 steps at the grid-search optimum, quantifying the
two-order-of-magnitude gap between natural residence times and the jump-duration mechanism.

### S2. Hyperparameter grid search landscape

The jump mechanism introduces two hyperparameters: the tail-entry probability ϵ\epsilon and the mean jump duration λ\lambda.
We selected these via the multi-objective grid search described in Algorithm [4](#alg4 "Algorithm 4 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), sweeping ϵ∈[10−4,2.5×10−2]\epsilon\in[10^{-4},2.5\times 10^{-2}] (eight points) and λ∈[10,160]\lambda\in[10,160] (nine points) with 200 simulated paths per grid point.
The objective J​(ϵ,λ)J(\epsilon,\lambda) balances two terms: the squared error between observed and simulated absolute-return ACFs (lags 1–252) and a kurtosis penalty weighted by wK=0.20w\_{K}=0.20.
Figure [S2](#Sx4.F2 "Figure S2 ‣ S2. Hyperparameter grid search landscape ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") presents the results.
Panel (a) shows that JJ is well-behaved over the grid, with a clear minimum confirming that the two hyperparameters are jointly identifiable from data.
The optimal values (ϵ∗=10−4,λ∗=100)(\epsilon^{\*}=10^{-4},\lambda^{\*}=100) indicate that the data favor rare but long-lived tail excursions; ϵ∗\epsilon^{\*} falls at the lower boundary of the ϵ\epsilon grid, while λ∗\lambda^{\*} is an interior optimum.
Panel (b) validates that the ACF of |Gt||G\_{t}| at these optimal parameters closely tracks the observed SPY autocorrelation structure, with the simulated 10th–90th percentile envelope (computed from 500 paths) enveloping the empirical curve over the full 252-lag horizon.

![Refer to caption](2603.10202v1/x6.png)

Two-panel figure showing the hyperparameter grid search results. Panel (a) is a heatmap of the objective function J in log base 10 scale over the epsilon-lambda grid, with a red star marking the optimal pair at epsilon-star equals 1e-4 and lambda-star equals 100; the minimum sits at the lower boundary of the epsilon grid and at an interior point of the lambda grid. Panel (b) shows the ACF of absolute returns computed from 500 jump-containing paths at the optimal parameters, with the 10th to 90th percentile band shaded and the mean curve compared against the observed SPY ACF and 95 percent significance band.

Figure S2. Hyperparameter grid search over (ϵ,λ)(\epsilon,\lambda) for SPY (N=100N=100, 200 paths per
grid point).
Panel (a): heatmap of the objective function J​(ϵ,λ)J(\epsilon,\lambda) in log10\log\_{10} scale over
the full search grid (ϵ∈[10−4,2.5×10−2]\epsilon\in[10^{-4},2.5\times 10^{-2}], λ∈[10,160]\lambda\in[10,160]);
the red star marks the optimal pair (ϵ∗=10−4,λ∗=100)(\epsilon^{\*}=10^{-4},\lambda^{\*}=100).
The clear minimum confirms that the jump hyperparameters are jointly identifiable from data;
ϵ∗\epsilon^{\*} sits at the lower boundary of the search grid, indicating that smaller tail-entry
probabilities are consistently preferred.
Panel (b): ACF of |Gt||G\_{t}| at the optimal parameters computed from 500 jump-containing paths
(10th–90th percentile band shaded; mean curve solid navy) compared with the SPY observed ACF
(dashed red) and the 95% significance band (dotted black).

### S3. State resolution sensitivity

A natural concern is whether the model’s performance depends critically on the choice of NN, the number of discrete states.
To investigate this, we re-estimated the full pipeline (Laplace fit, quantile partition, transition matrix, and, for HMM-WJ, the grid search over ϵ\epsilon and λ\lambda) for N∈{30,60,90,100,150,200}N\in\{30,60,90,100,150,200\} and evaluated each configuration on 1,000 simulated in-sample paths.
Table [T1](#Sx4.T1 "Table T1 ‣ S3. State resolution sensitivity ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") reports KS and AD pass rates at the α=0.05\alpha=0.05 level along with ACF-MAE (mean absolute error of the absolute-return ACF over lags 1–252).
Standard errors are computed via the binomial formula for pass rates and bootstrap resampling (B=500B=500) for ACF-MAE.

For HMM-NJ, distributional fidelity is uniformly high across all resolutions (KS ≥98.9%\geq 98.9\%, AD ≥97.9%\geq 97.9\%), confirming that the Laplace quantile partition produces well-calibrated marginals regardless of NN.
ACF-MAE is effectively constant at 0.059, reflecting the absence of any volatility-clustering mechanism.
For HMM-WJ, KS pass rates remain above 96% across all NN, while AD pass rates range from 88.6% (N=200N=200) to 96.8% (N=30N=30).
The slight decline at high NN is expected: finer partitions produce more sparsely populated tail states, making the Anderson-Darling test (which weights tail discrepancies heavily) more sensitive.
Crucially, ACF-MAE improves monotonically from 0.057 (N=30N=30) to 0.049 (N=200N=200), demonstrating that the jump mechanism’s ability to reproduce volatility clustering strengthens with finer state resolution.
The operating point N=100N=100 balances these two effects, achieving strong performance on all three metrics simultaneously.

Table T1. Sensitivity of model performance to state resolution NN.
All metrics computed over 1,000 simulated in-sample paths at α=0.05\alpha=0.05.
ACF-MAE = mean absolute error of the ACF of |Gt||G\_{t}| over lags 1–252.
Standard errors in parentheses: binomial SE for pass rates,
bootstrap SE (B=500B=500) for ACF-MAE.

| Model | NN | KS pass (%) | AD pass (%) | ACF-MAE |
| --- | --- | --- | --- | --- |
| HMM-NJ | 200 | 99.6 (0.2) | 98.5 (0.4) | 0.059 |
| HMM-NJ | 150 | 99.6 (0.2) | 98.4 (0.4) | 0.059 |
| HMM-NJ | 100 | 99.0 (0.3) | 98.8 (0.3) | 0.059 |
| HMM-NJ | 90 | 99.4 (0.2) | 98.1 (0.4) | 0.059 |
| HMM-NJ | 60 | 99.4 (0.2) | 98.1 (0.4) | 0.059 |
| HMM-NJ | 30 | 98.9 (0.3) | 97.9 (0.5) | 0.059 |
| HMM-WJ | 200 | 96.0 (0.6) | 88.6 (1.0) | 0.049 |
| HMM-WJ | 150 | 96.9 (0.5) | 88.8 (1.0) | 0.050 |
| HMM-WJ | 100 | 96.8 (0.6) | 91.7 (0.9) | 0.053 |
| HMM-WJ | 90 | 97.4 (0.5) | 91.0 (0.9) | 0.052 |
| HMM-WJ | 60 | 96.8 (0.6) | 92.4 (0.8) | 0.054 |
| HMM-WJ | 30 | 98.0 (0.4) | 96.8 (0.6) | 0.057 |

### S4. Additional algorithms

The main text presents Algorithm [1](#alg1 "Algorithm 1 ‣ Simulation algorithm ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion"), which generates synthetic state sequences from the fitted HMM with jump-duration dynamics.
The three algorithms below detail the remaining stages of the computational pipeline.
Algorithm [2](#alg2 "Algorithm 2 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") describes model construction: fitting a Laplace distribution to the observed excess growth rates, partitioning the support into NN equal-probability bins, assigning each observation to a discrete state, and estimating the transition matrix by row-normalizing the state-to-state count matrix.
Algorithm [3](#alg3 "Algorithm 3 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") converts a simulated discrete state sequence back into continuous excess growth rates by sampling from a location-scale Student-t distribution (ν=5\nu=5) within each state, parameterized by the state-conditional sample mean and standard deviation.
Algorithm [4](#alg4 "Algorithm 4 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") performs the multi-objective grid search over the jump hyperparameters (ϵ,λ)(\epsilon,\lambda), minimizing a composite objective that penalizes both ACF mismatch and kurtosis deviation relative to the observed series.

### S5. Cross-asset generalization

To assess whether the framework generalized beyond the SPY market factor, we fitted standalone HMM-NJ and HMM-WJ models to three individual equities spanning distinct risk profiles: NVDA (high-beta technology), JNJ (low-beta health care), and JPM (moderate-beta financials). Each ticker was fitted independently using the same N=100N=100 Laplace quantile partition and the same grid search procedure described in Section 3.3 of the main text, with 1,000 simulated paths evaluated against the observed series.

Table [T2](#Sx4.T2 "Table T2 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") reports the results. In-sample KS pass rates exceeded 91% for all three tickers under both HMM-NJ and HMM-WJ, confirming that the Student-t emission structure captured the marginal distribution of individual equities with diverse tail characteristics. The grid search selected ϵ∗=10−4\epsilon^{\*}=10^{-4} for all three assets, with λ∗=160\lambda^{\*}=160 for NVDA and JPM (long-lived volatility episodes) and λ∗=30\lambda^{\*}=30 for JNJ (shorter episodes consistent with its weaker volatility clustering). HMM-WJ reduced ACF-MAE relative to HMM-NJ for NVDA (0.043→\to0.028) and JPM (0.045→\to0.032), while JNJ showed minimal improvement (0.027→\to0.026), consistent with its lower baseline autocorrelation in absolute returns.

Out-of-sample performance varied across tickers. NVDA maintained strong distributional fidelity (KS 97.1%, AD 95.6%), while JNJ and JPM showed more pronounced OoS degradation (KS 70–77%), reflecting asset-specific regime shifts in 2025 that the stationary IS-calibrated parameters could not fully capture. These results confirmed that the HMM-WJ framework was not specific to ETFs or broad market indices; it generalized to individual equities, with the grid search automatically adapting the jump parameters to each asset’s volatility dynamics.

Table T2. Cross-asset generalization of HMM-NJ and HMM-WJ to individual equities (N=100N=100, 1,000 simulated paths, α=0.05\alpha=0.05). Each ticker was fitted independently with a per-asset grid search over (ϵ,λ)(\epsilon,\lambda). Standard errors in parentheses: binomial SE for pass rates, std/n\text{std}/\!\sqrt{n} for kurtosis, bootstrap SE (B=500B=500) for ACF-MAE.

| Ticker | Model | KS pass (%) | AD pass (%) | Excess kurtosis | ACF-MAE |
| --- | --- | --- | --- | --- | --- |
| In-sample (2,766 trading days, 2014–2024) | | | | | |
|  |  |  |  | Observed: 5.0 |  |
| NVDA | HMM-NJ | 99.3 (0.3) | 99.1 (0.3) | 4.4 (0.02) | 0.043 (<<0.001) |
| NVDA | HMM-WJ | 91.7 (0.9) | 77.5 (1.3) | 4.1 (0.03) | 0.028 (0.001) |
|  |  |  |  | Observed: 8.7 |  |
| JNJ | HMM-NJ | 99.8 (0.1) | 99.2 (0.3) | 6.8 (0.04) | 0.027 (<<0.001) |
| JNJ | HMM-WJ | 99.8 (0.1) | 99.1 (0.3) | 6.7 (0.04) | 0.026 (<<0.001) |
|  |  |  |  | Observed: 8.0 |  |
| JPM | HMM-NJ | 99.6 (0.2) | 99.3 (0.3) | 6.7 (0.03) | 0.045 (<<0.001) |
| JPM | HMM-WJ | 92.8 (0.8) | 79.6 (1.3) | 6.3 (0.03) | 0.032 (0.001) |
| Out-of-sample (249 trading days, 2025) | | | | | |
|  |  |  |  | Observed: 7.0 |  |
| NVDA | HMM-NJ | 99.0 (0.3) | 97.7 (0.5) | 3.8 (0.07) | 0.039 (<<0.001) |
| NVDA | HMM-WJ | 97.1 (0.5) | 95.6 (0.6) | 3.7 (0.07) | 0.037 (<<0.001) |
|  |  |  |  | Observed: 6.4 |  |
| JNJ | HMM-NJ | 73.2 (1.4) | 59.4 (1.6) | 5.5 (0.11) | 0.034 (<<0.001) |
| JNJ | HMM-WJ | 70.3 (1.4) | 59.7 (1.6) | 5.6 (0.11) | 0.034 (<<0.001) |
|  |  |  |  | Observed: 6.7 |  |
| JPM | HMM-NJ | 77.6 (1.3) | 78.1 (1.3) | 5.9 (0.09) | 0.032 (<<0.001) |
| JPM | HMM-WJ | 76.9 (1.3) | 76.4 (1.3) | 5.8 (0.09) | 0.031 (<<0.001) |

Algorithm 2  Empirical hidden Markov model construction via Laplace partitioning

0:  Price history P1:TP\_{1:T}, Risk-free rate rfr\_{f}, Number of states NN

0:  Transition matrix 𝐓\mathbf{T}, Quantile boundaries 𝒬\mathcal{Q}

1:  Compute excess growth rates Rt=1Δ​t​ln⁡(Pt/Pt−1)−rfR\_{t}=\frac{1}{\Delta t}\ln(P\_{t}/P\_{t-1})-r\_{f} for all tt.

2:  Fit Laplace parameters (μL,bL)(\mu\_{L},b\_{L}) to the series 𝐑\mathbf{R} using maximum-likelihood estimation.

3:  Define interior boundaries Qk=FL−1​(k/N;μL,bL)Q\_{k}=F\_{L}^{-1}(k/N;\mu\_{L},b\_{L}) for k∈{1,…,N−1}k\in\{1,\dots,N-1\}, where FL−1F\_{L}^{-1} is the inverse CDF of the Laplace distribution.

4:  Set finite outer bounds Q0=FL−1​(0.001;μL,bL)Q\_{0}=F\_{L}^{-1}(0.001;\mu\_{L},b\_{L}) and QN=FL−1​(0.999;μL,bL)Q\_{N}=F\_{L}^{-1}(0.999;\mu\_{L},b\_{L}).

5:  Assign each excess growth rate RtR\_{t} to a discrete state st∈{1,…,N}s\_{t}\in\{1,\dots,N\} based on the boundaries in 𝒬={Qk}\mathcal{Q}=\{Q\_{k}\}.

6:  Initialize count matrix 𝐂∈ℝN×N\mathbf{C}\in\mathbb{R}^{N\times N} and transition matrix 𝐓∈ℝN×N\mathbf{T}\in\mathbb{R}^{N\times N} with zeros.

7:  for t=1t=1 to T−1T-1 do

8:   Identify transition i=sti=s\_{t} to j=st+1j=s\_{t+1}.

9:   𝐂i,j←𝐂i,j+1\mathbf{C}\_{i,j}\leftarrow\mathbf{C}\_{i,j}+1.

10:  end for

11:  for i=1i=1 to NN do

12:   𝐓i,:←𝐂i,:/∑j=1N𝐂i,j\mathbf{T}\_{i,:}\leftarrow\mathbf{C}\_{i,:}/\sum\_{j=1}^{N}\mathbf{C}\_{i,j} {Row-wise normalization}

13:  end for

14:  return 𝐓,𝒬\mathbf{T},\mathcal{Q}

Algorithm 3  State decoding and continuous excess growth rate reconstruction

0:  Simulated state sequence S1:MS\_{1:M}, Encoded training observations, Degrees of freedom ν=5\nu=5

0:  Reconstructed continuous excess growth rates R^1:M\hat{R}\_{1:M}

1:  for k=1k=1 to NN do

2:   Set μk=mean​({Gt:Sttrain=k})\mu\_{k}=\text{mean}(\{G\_{t}:S\_{t}^{\text{train}}=k\}).

3:   Set σk=std​({Gt:Sttrain=k})\sigma\_{k}=\text{std}(\{G\_{t}:S\_{t}^{\text{train}}=k\}).

4:  end for

5:  Initialize the reconstructed excess growth rate vector 𝐆^\mathbf{\hat{G}} of length MM.

6:  for t=1t=1 to MM do

7:   Retrieve the simulated state k=Stk=S\_{t}.

8:   Sample G^t=μk+σk⋅Z\hat{G}\_{t}=\mu\_{k}+\sigma\_{k}\cdot Z, where Z∼tνZ\sim t\_{\nu}.

9:  end for

10:  return G^1:M\hat{G}\_{1:M}

Algorithm 4  Multi-objective grid search for jump hyperparameters

0:  Observed growth rates 𝐑o​b​s\mathbf{R}\_{obs}, ACF max lag L=252L=252, Number of paths P=200P=200, Time steps M=2766M=2766

0:  Grid: ϵ∈{10−4,2.5×10−4,5×10−4,10−3,2.5×10−3,5×10−3,10−2,2.5×10−2}\epsilon\in\{10^{-4},2.5\times 10^{-4},5\times 10^{-4},10^{-3},2.5\times 10^{-3},5\times 10^{-3},10^{-2},2.5\times 10^{-2}\}, λ∈{10,25,40,55,70,85,100,130,160}\lambda\in\{10,25,40,55,70,85,100,130,160\}

0:  Kurtosis penalty weight wK=0.20w\_{K}=0.20

0:  Optimal jump hyperparameters (ϵ∗,λ∗)(\epsilon^{\*},\lambda^{\*})

1:  Calculate observed absolute ACF: Ao​b​s​(τ)=ACF​(|𝐑o​b​s|,τ)A\_{obs}(\tau)=\text{ACF}(|\mathbf{R}\_{obs}|,\tau) for τ∈{1,…,L}\tau\in\{1,\dots,L\}.

2:  Calculate observed global kurtosis: Ko​b​s=Kurtosis​(𝐑o​b​s)K\_{obs}=\text{Kurtosis}(\mathbf{R}\_{obs}).

3:  Initialize minimum error Em​i​n←∞E\_{min}\leftarrow\infty.

4:  for each ϵ\epsilon in grid space do

5:   for each λ\lambda in grid space do

6:    Initialize simulated ACF accumulator 𝐀s​u​m←𝟎\mathbf{A}\_{sum}\leftarrow\mathbf{0} and kurtosis accumulator Ks​u​m←0K\_{sum}\leftarrow 0.

7:    for p=1p=1 to PP do

8:     Simulate path using Algorithm [1](#alg1 "Algorithm 1 ‣ Simulation algorithm ‣ 3. Methods ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") to obtain state sequence S1:MS\_{1:M}.

9:     Decode sequence using Algorithm [3](#alg3 "Algorithm 3 ‣ S5. Cross-asset generalization ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") to obtain continuous rates 𝐑^(p)\mathbf{\hat{R}}^{(p)}.

10:     𝐀s​u​m​(τ)←𝐀s​u​m​(τ)+ACF​(|𝐑^(p)|,τ)\mathbf{A}\_{sum}(\tau)\leftarrow\mathbf{A}\_{sum}(\tau)+\text{ACF}(|\mathbf{\hat{R}}^{(p)}|,\tau) for all τ\tau.

11:     Ks​u​m←Ks​u​m+Kurtosis​(𝐑^(p))K\_{sum}\leftarrow K\_{sum}+\text{Kurtosis}(\mathbf{\hat{R}}^{(p)}).

12:    end for

13:    Compute ensemble averages: A¯s​i​m​(τ)=𝐀s​u​m​(τ)/P\overline{A}\_{sim}(\tau)=\mathbf{A}\_{sum}(\tau)/P and K¯s​i​m=Ks​u​m/P\overline{K}\_{sim}=K\_{sum}/P.

14:    Compute objective: J=∑τ=1L(Ao​b​s​(τ)−A¯s​i​m​(τ))2+wK​(Ko​b​s−K¯s​i​m)2J=\sum\_{\tau=1}^{L}\left(A\_{obs}(\tau)-\overline{A}\_{sim}(\tau)\right)^{2}+w\_{K}\left(K\_{obs}-\overline{K}\_{sim}\right)^{2}.

15:    if J<Em​i​nJ<E\_{min} then

16:     Em​i​n←JE\_{min}\leftarrow J

17:     (ϵ∗,λ∗)←(ϵ,λ)(\epsilon^{\*},\lambda^{\*})\leftarrow(\epsilon,\lambda)

18:    end if

19:   end for

20:  end for

21:  return ϵ∗,λ∗\epsilon^{\*},\lambda^{\*}

### S6. Emission distribution and semi-Markov comparison

Table [T3](#Sx4.T3 "Table T3 ‣ S6. Emission distribution and semi-Markov comparison ‣ Online Appendix ‣ Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion") isolates the contributions of the emission distribution and the persistence mechanism by comparing three model variants on SPY: the HSMM baseline (K=8K=8 states, negative-binomial dwell times, Student-t emissions), HMM-WJ with the original Gaussian emissions (N=100N=100), and HMM-WJ with Student-t emissions (N=100N=100). The comparison confirms that HMM-WJ dominates the HSMM on distributional fidelity regardless of emission choice, and that the Student-t upgrade provides incremental improvements in tail reproduction (excess kurtosis closer to observed) and marginal fit (higher KS and AD pass rates).

Table T3. Three-way comparison isolating the emission distribution and persistence mechanism for SPY (N=100N=100 for HMM-WJ, K=8K=8 for HSMM; 1,000 simulated paths, α=0.05\alpha=0.05). Standard errors in parentheses.

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | HSMM | HMM-WJ | HMM-WJ |
|  | (Student-tt) | (Gaussian) | (Student-tt) |
| States | K=8K=8 | N=100N=100 | N=100N=100 |
| Parameters | 18 | 4 | 4 |
| In-sample (2,766 trading days, 2014–2024) | | | |
| KS pass rate (%) | 82.0 (1.2) | 97.0 (0.5) | 97.6 (0.5) |
| AD pass rate (%) | 42.5 (1.6) | 90.5 (0.9) | 91.3 (0.9) |
| Excess kurtosis | 4.8 (0.08) | 5.5 (0.03) | 7.6 (0.14) |
| ACF-MAE | 0.059 (<<0.001) | 0.052 (<<0.001) | 0.052 (<<0.001) |
| Wasserstein-1 | 0.176 (0.001) | 0.101 (0.002) | 0.101 (0.001) |
| Hellinger | 0.113 (<<0.001) | 0.076 (<<0.001) | 0.075 (<<0.001) |
| Out-of-sample (249 trading days, 2025) | | | |
| KS pass rate (%) | 96.2 (0.6) | 95.0 (0.7) | 94.4 (0.7) |
| AD pass rate (%) | 96.7 (0.6) | 95.9 (0.6) | 95.1 (0.7) |
| Excess kurtosis | 4.1 (0.13) | 4.9 (0.08) | 6.1 (0.13) |
| ACF-MAE | 0.042 (<<0.001) | 0.040 (<<0.001) | 0.039 (<<0.001) |
| Wasserstein-1 | 0.287 (0.002) | 0.275 (0.005) | 0.282 (0.006) |
| Hellinger | 0.239 (0.001) | 0.212 (0.001) | 0.210 (0.001) |

BETA