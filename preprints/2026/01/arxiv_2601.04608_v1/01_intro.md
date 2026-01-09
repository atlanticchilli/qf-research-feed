---
authors:
- Jinjun Liu
- Ming-Yen Cheng
doc_id: arxiv:2601.04608v1
family_id: arxiv:2601.04608
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine
  Learning Approach'
url_abs: http://arxiv.org/abs/2601.04608v1
url_html: https://arxiv.org/html/2601.04608v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jinjun Liu
Department of Mathematics, Hong Kong Baptist University.
Email: 22482865@life.hkbu.edu.hk
  
Ming-Yen Cheng
Department of Mathematics, Hong Kong Baptist University.
Email: chengmingyen@hkbu.edu.hk

(January 8, 2026)

###### Abstract

Global asset prices are interconnected through sovereign bond yield curve dynamics, with U.S. Treasuries serving as the benchmark for global interest-rate pricing. Even for U.S. Treasuries—the most liquid and data-dependent fixed-income instruments—yields are noisy and shaped by policy communication, evolving supply–demand conditions, and behavioral forces. In such environments, forecast users face material downside risk when making decisions under policy uncertainty and market stress.
We study U.S. Treasury yield curve forecasting under distributional uncertainty and recast forecasting as an operations-research and managerial decision problem in which the forecaster selects a rule to minimize worst-case expected loss over admissible forecast-error distributions. We propose a distributionally robust ensemble forecasting framework that integrates parametric factor models with high-dimensional nonparametric machine learning models through adaptive forecast combinations.
The framework has three ML/AI components. A rolling-window Factor-Augmented Dynamic Nelson–Siegel (FADNS) model captures level, slope, and curvature dynamics using principal components from economic indicators. Random Forest models capture nonlinear interactions among economic drivers and lagged Treasury yields. Distributionally robust forecast-combination schemes aggregate heterogeneous forecasts under moment uncertainty, penalizing downside tail risk via expected shortfall and stabilizing second-moment estimation through ridge-regularized covariance matrices. The severity of the worst-case criterion is adjustable, allowing the forecaster to regulate robustness against forecast errors.
Using monthly data, we evaluate out-of-sample forecasts across maturities and horizons from one to twelve months ahead. Adaptive combinations outperform at short horizons, while Random Forest forecasts dominate at longer horizons. Extensions to global sovereign bond yields confirm the stability and generalizability of the proposed framework.

This is a preprint. The paper is currently under review.

Keywords: distributionally robust optimization; adaptive forecast combination; random forests; factor-augmented Dynamic Nelson–Siegel model

## 1 Introduction

Modeling and forecasting interest rates have long been central to financial market valuation, policy analysis, and decision-making. Global asset prices are interconnected through sovereign bond yield curve dynamics, with U.S. Treasury yields serving as the benchmark for global interest-rate pricing. The valuation of U.S. Treasury securities is inherently data dependent and shaped by monetary and fiscal policy stances, macroeconomic and financial conditions, and evolving supply–demand dynamics. In recent years, yield dynamics have exhibited heightened volatility, reflecting increased policy uncertainty, greater sensitivity to central bank communication, and amplified market reactions.
In this environment, hedge funds frequently employ leveraged derivative positions to express views on future interest rate paths, while central banks closely monitor these exposures because of their implications for market liquidity and financial stability. Yield curve movements directly affect these positions and inform the decisions of both market participants and policymakers. As a result, robust yield curve forecasting has become critical under heightened uncertainty.

A seminal contribution in this literature is the parsimonious yield curve representation proposed by Nelson and Siegel ([1987](https://arxiv.org/html/2601.04608v1#bib.bib15)), which characterizes the cross section of yields through level, slope, and curvature factors. Building on this structure, Diebold and Li ([2006](https://arxiv.org/html/2601.04608v1#bib.bib11)) introduced a dynamic version of the Nelson–Siegel model, demonstrating its strong empirical performance in yield curve forecasting. Subsequent extensions have sought to enrich the informational content of these models by incorporating macroeconomic variables. In particular, the Factor–Augmented Dynamic Nelson–Siegel (FADNS) framework integrates latent yield factors with principal components extracted from macroeconomic indicators, thereby enhancing explanatory power and forecast performance (Fernandes and Vieira [2019](https://arxiv.org/html/2601.04608v1#bib.bib12)).
Despite these advances, increasing model complexity does not necessarily translate into improved out-of-sample performance. High-dimensional predictive environments are inherently subject to estimation error and feature noise, which can offset the potential gains from incorporating additional predictors. Using random matrix theory, Cartea et al. ([2025](https://arxiv.org/html/2601.04608v1#bib.bib39)) show that both out-of-sample predictive accuracy and risk-adjusted performance can deteriorate monotonically beyond an optimal level of model complexity.

Ensemble learning methods have gained prominence as flexible tools for capturing nonlinear relationships in economic data. The Random Forest algorithm introduced by Breiman ([2001](https://arxiv.org/html/2601.04608v1#bib.bib7)) provides a powerful nonparametric approach based on aggregating decision trees constructed from subsampled data. Recent theoretical work has established asymptotic properties of Random Forest estimators in high-dimensional settings, clarifying their behavior under increasing dimensionality (Chi et al. [2022](https://arxiv.org/html/2601.04608v1#bib.bib9)). Understanding model predictions is essential in many decision-making applications, yet state-of-the-art predictive accuracy is often achieved by complex models that are difficult to interpret. To address the resulting tension between accuracy and interpretability, Lundberg and Lee ([2017](https://arxiv.org/html/2601.04608v1#bib.bib1)) propose SHAP (SHapley Additive exPlanations), a unified framework for feature attribution that represents a model prediction as an additive decomposition of feature contributions relative to a baseline value. Grounded in cooperative game theory, SHAP assigns each feature a Shapley value that satisfies desirable axioms such as efficiency, symmetry, dummy, and additivity, ensuring a unique and consistent attribution of predictive contributions. Because the framework is model-agnostic, SHAP provides a theoretically principled approach to interpreting predictions from machine learning models, including ensemble methods such as Random Forests.

Forecast combination offers a principled approach to aggregating information across heterogeneous models. Early contributions include thick modeling (Granger and Jeon [2004](https://arxiv.org/html/2601.04608v1#bib.bib13)) and persistence-based combination schemes (Aiolfi and Timmermann [2006](https://arxiv.org/html/2601.04608v1#bib.bib2)), which demonstrate that combining forecasts from diverse models can improve predictive accuracy. In the context of yield curve forecasting, Caldeira et al. ([2016](https://arxiv.org/html/2601.04608v1#bib.bib8)) provide a comprehensive analysis of combination methods, including equal-weighted, ordinary least squares, and rank-based schemes. A large literature has further developed adaptive and theoretically grounded combination methods, such as minimum-variance (Granger and Ramanathan [1984](https://arxiv.org/html/2601.04608v1#bib.bib35)), stacking (Wolpert [1992](https://arxiv.org/html/2601.04608v1#bib.bib36), Breiman [1996](https://arxiv.org/html/2601.04608v1#bib.bib37)), and exponential reweighting (Yang [2004](https://arxiv.org/html/2601.04608v1#bib.bib21)). More recent work extends these ideas to high-dimensional and non-Gaussian environments, emphasizing robustness to heavy-tailed forecast errors (Jiang et al. [2025](https://arxiv.org/html/2601.04608v1#bib.bib38)).

Most forecast combination methods rely on parametric assumptions on forecast error distributions and plug-in estimates of second moments. In economic and financial applications, these assumptions are frequently violated, and moment estimates can be unreliable in finite samples. As a result, forecast combinations based on misspecified error distributions may yield unstable weights and misleading performance assessments.
These limitations motivate a distributionally robust optimization (DRO) perspective. Rather than assuming a known probability law, DRO seeks decisions that perform well against the worst-case distribution within a prescribed ambiguity set. Delage and Ye ([2010](https://arxiv.org/html/2601.04608v1#bib.bib41)) introduce moment-based ambiguity sets that explicitly allow uncertainty in both the mean and covariance and show that the resulting distributionally robust stochastic programs are tractable. Their approach constructs finite-sample confidence regions for moments using concentration inequalities, yielding ellipsoidal bounds on the mean and semidefinite bounds on the covariance that contain the true moments with high probability. Decisions derived under these ambiguity sets are therefore robust to estimation error and consistent as sample size increases.
Subsequent work has extended DRO to conditional settings. Nguyen et al. ([2020](https://arxiv.org/html/2601.04608v1#bib.bib42)) propose a distributionally robust approach to local nonparametric conditional estimation using Wasserstein ambiguity sets, with a primary focus on estimating conditional statistics rather than optimizing decisions. Nguyen et al. ([2024](https://arxiv.org/html/2601.04608v1#bib.bib43)) further develop tractable distributionally robust conditional decision-making models with side information, formulating mean–variance and mean–CVaR problems under optimal transport–based ambiguity sets.

Despite these advances, most of the forecasting literature—particularly in high-dimensional time series—addresses distributional uncertainty primarily as an estimation problem, emphasizing dimension reduction, factor construction, and inference under heavy-tailed data and limited sample sizes. Less attention is paid to the decision-theoretic implications of forecast uncertainty for downstream users of forecasts.
We therefore recast forecasting from an operations research perspective. Under model and distributional uncertainty, forecasting can be formulated as a min–max decision problem, in which the forecaster selects a forecasting rule to minimize worst-case expected loss over a set of admissible forecast-error distributions. In the proposed framework, the severity of this worst-case criterion is not fixed but is explicitly adjustable within the forecasting algorithm, allowing the forecaster to regulate the degree of robustness imposed against forecast errors. From this viewpoint, robustness and stability—rather than optimality under a single presumed data-generating process—are primary objectives. Robust and stable forecasts reduce the downside risk faced by agents who rely on them, a consideration that is especially important in high-dimensional settings where estimation uncertainty is pervasive.

Building on this perspective, we propose a distributionally robust ensemble framework for U.S. Treasury yield curve forecasting that integrates parametric and nonparametric models through adaptive forecast combination. Unlike standard DRO approaches that explicitly solve minimax optimization problems over ambiguity sets, our framework enforces robustness directly at the level of forecast-error losses. Downside tail risk is penalized via expected shortfall (ES), while instability in second-moment estimation is mitigated through ridge-regularized covariance matrices. Forecast combination weights are determined using adaptive reweighting rules, yielding stable, tail-aware combinations without imposing parametric assumptions on forecast-error distributions. Empirical results and robustness checks demonstrate that the proposed framework delivers stable and competitive forecasting performance across U.S. and global sovereign bond markets.

## 2 Methodology

### 2.1 Data

#### 2.1.1 U.S. Treasury Yields

We use zero-coupon equivalent yields on U.S. Treasury securities obtained from the LSEG Reuters Workspace. The sample spans January 2006 to August 2025 at a monthly frequency and covers 15 maturities ranging from 3 months to 30 years (end-of-month observations).
To assess the stability of yield curve dynamics over time, we implement a two-stage structural break detection procedure. First, for each maturity, we apply the cumulative sum (CUSUM) test of Brown et al. ([1975](https://arxiv.org/html/2601.04608v1#bib.bib23)) to examine the null hypothesis of parameter constancy. The null is strongly rejected across all maturities (p<0.001p<0.001), indicating the presence of structural instability.
Second, we identify the timing of structural breaks using the Pruned Exact Linear Time (PELT) algorithm with a radial basis function (RBF) cost specification (Truong et al. [2020](https://arxiv.org/html/2601.04608v1#bib.bib24)). Breakpoints are selected by minimizing a penalized objective function with penalty parameter set to 10. Appendix Table in E-companion summarizes the estimated break dates for each maturity.

The identified breakpoints align with well-documented economic events. Early breaks between 2000 and 2002 are concentrated in medium- and long-term maturities and coincide with the burst of the dot-com bubble and the 2001 recession. A break around 2005 corresponds to the Federal Reserve’s pre-crisis tightening cycle. A pronounced and system-wide break occurs in late 2008, reflecting the global financial crisis and the onset of unconventional monetary policy. Subsequent breaks in 2010–2011 align with the European sovereign debt crisis and the downgrade of U.S. sovereign credit, particularly affecting long-term yields. Later breaks capture major regime shifts, including the initial phase of monetary policy normalization in 2015, balance sheet reduction and rate hikes in 2017, the COVID-19 shock in 2020, and the transition from quantitative easing to quantitative tightening during the aggressive tightening cycle beginning in mid 2022.

#### 2.1.2 Economic Indicators

We compile a panel of 111 macroeconomic and financial indicators from the LSEG Reuters Workspace Key Economic Indicators page, covering a broad cross-section of price and inflation, labor markets, real activity, leading indicators, business conditions and surveys, household and personal sector, housing market, external sector, financial conditions and interest rates, as well as treasury supply and capital flows. All series are observed at a monthly frequency. Quarterly variables are converted to monthly frequency using linear interpolation. The full list of variables is provided in the E-Companion (Tables EC.1–EC.7).

To extract the dominant common factors underlying yield curve movements, we apply principal component analysis (PCA) to the standardized indicator panel. Prior to factor extraction, stationarity of each series is assessed using the Augmented Dickey–Fuller (ADF) test (Dickey and Fuller [1979](https://arxiv.org/html/2601.04608v1#bib.bib10)). Nonstationary variables are transformed by first differencing to ensure stability.
Table in E-Companion reports the results. The first principal component explains approximately 23% of the total variance, while the second component accounts for an additional 12%. The first ten principal components together explain 72.5% of the total variation in the indicator panel. Appendix Table in E-Companion reports the variables with the highest correlations with the first two principal components.
Several data limitations should be noted. First, interpolating quarterly variables to monthly frequency may smooth short-run fluctuations and attenuate cyclical dynamics. Second, the analysis relies on the final release data to ensure data quality rather than first release data. While this choice improves data consistency, it may limit the information available to real-time forecasters.

### 2.2 Factor–Augmented Dynamic Nelson Siegel (FADNS) Family

#### 2.2.1 Dynamic Nelson–Siegel (DNS) Model

The Dynamic Nelson–Siegel (DNS) model serves as the benchmark specification for modeling and forecasting the U.S. Treasury yield curve. Following Diebold and Li ([2006](https://arxiv.org/html/2601.04608v1#bib.bib11)), the yield at time tt and maturity τ\tau is represented as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | yt​(τ)\displaystyle y\_{t}(\tau) | =β1​t+β2​t​(1−e−λ​τλ​τ)\displaystyle=\beta\_{1t}+\beta\_{2t}\left(\frac{1-e^{-\lambda\tau}}{\lambda\tau}\right) |  | (2.1) |
|  |  | +β3​t​(1−e−λ​τλ​τ−e−λ​τ)+εt​(τ),\displaystyle\quad+\beta\_{3t}\left(\frac{1-e^{-\lambda\tau}}{\lambda\tau}-e^{-\lambda\tau}\right)+\varepsilon\_{t}(\tau), |  |

where yt​(τ)y\_{t}(\tau) denotes the observed zero-coupon yield, εt​(τ)\varepsilon\_{t}(\tau) is a mean-zero measurement error, and the decay parameter is fixed at λ=0.0609\lambda=0.0609, consistent with the empirical literature.

The latent factor vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt\displaystyle\beta\_{t} | =[β1​tβ2​tβ3​t]⊤\displaystyle=\begin{bmatrix}\beta\_{1t}&\beta\_{2t}&\beta\_{3t}\end{bmatrix}^{\!\top} |  |

captures the level, slope, and curvature components of the yield curve. The factor dynamics are governed by a first-order vector autoregressive process,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | βt+1\displaystyle\beta\_{t+1} | =c+Φ​βt+ηt,\displaystyle=c+\Phi\beta\_{t}+\eta\_{t}, |  | (2.2a) |
|  | ηt\displaystyle\eta\_{t} | ∼𝒩​(0,Ση),\displaystyle\sim\mathcal{N}(0,\Sigma\_{\eta}), |  | (2.2b) |

where cc is an intercept vector and Φ\Phi is the autoregressive coefficient matrix.

At each time tt, the factor vector βt\beta\_{t} is obtained by cross-sectional least squares, minimizing the squared forecast errors across N=15N=15 observed maturities. The VAR(1) parameters in Equation ([2.2a](https://arxiv.org/html/2601.04608v1#S2.E2.1 "In 2.2 ‣ 2.2.1 Dynamic Nelson–Siegel (DNS) Model ‣ 2.2 Factor–Augmented Dynamic Nelson Siegel (FADNS) Family ‣ 2 Methodology ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach")) are estimated using a rolling window of w=60w=60 monthly observations.

To assess multi-horizon predictive performance, the DNS model is extended from one-step-ahead forecasts to recursive hh-step-ahead forecasts for horizons
h∈{1,3,6,9,12}h\in\{1,3,6,9,12\} months.
Conditional on information available at time tt, the hh-step-ahead factor forecasts are generated by iterating the estimated VAR(1) process,

|  |  |  |
| --- | --- | --- |
|  | β^t+h|t=∑j=0h−1Φj​c+Φh​βt.\hat{\beta}\_{t+h|t}=\sum\_{j=0}^{h-1}\Phi^{j}c+\Phi^{h}\beta\_{t}. |  |

The corresponding yield forecasts y^t+h|t​(τ)\hat{y}\_{t+h|t}(\tau) are obtained by substituting β^t+h|t\hat{\beta}\_{t+h|t} into Equation ([2.1](https://arxiv.org/html/2601.04608v1#S2.E1 "In 2.2.1 Dynamic Nelson–Siegel (DNS) Model ‣ 2.2 Factor–Augmented Dynamic Nelson Siegel (FADNS) Family ‣ 2 Methodology ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach")).
For each rolling window, factor loadings are estimated, the state dynamics are fitted, and out-of-sample yield forecasts are produced. The window is then advanced by one month and the process repeated until the end of the sample.
Forecast errors for maturity τ\tau and horizon hh are defined as

|  |  |  |
| --- | --- | --- |
|  | et+h​(τ)=yt+h​(τ)−y^t+h|t​(τ),e\_{t+h}(\tau)=y\_{t+h}(\tau)-\hat{y}\_{t+h|t}(\tau), |  |

and forecast accuracy is evaluated using the root mean squared forecast error (RMSFE),

|  |  |  |
| --- | --- | --- |
|  | RMSFEh​(τ)=1T−w−h​∑t=wT−het+h​(τ)2,\displaystyle\text{RMSFE}\_{h}(\tau)=\sqrt{\frac{1}{T-w-h}\sum\_{t=w}^{T-h}e\_{t+h}(\tau)^{2}}, |  |

where TT denotes the total number of monthly observations. The complete estimation and forecasting procedure is summarized in E-Companion Algorithm.

#### 2.2.2 Factor–Augmented Dynamic Nelson–Siegel (FADNS) Model

The factor–augmented Dynamic Nelson–Siegel (FADNS) model introduced by Fernandes and Vieira ([2019](https://arxiv.org/html/2601.04608v1#bib.bib12)) extends the benchmark DNS framework by augmenting the DNS factor dynamics with 2 principal components extracted from a high-dimensional panel of economic indicators with an expanding window. We introduce a rolling-window version of the FADNS model incorporating economic information from past 60 months(w=60w=60). Let Zt∈ℝpZ\_{t}\in\mathbb{R}^{p} denote the vector of economic indicators observed at month tt, where p=111p=111. The DNS factors (β1​t,β2​t,β3​t)(\beta\_{1t},\beta\_{2t},\beta\_{3t}) represent the level, slope, and curvature components of the yield curve and are estimated cross-sectionally across N=15N=15 maturities.
Considering the release of many key economic data is lagging 1 month, only lagged predictor information is used to reflect data availability. Specifically, at forecast origin tt, the information set is defined as

|  |  |  |
| --- | --- | --- |
|  | ℐt={Zt−1,Zt−2,…,Zt−w}.\mathcal{I}\_{t}=\{Z\_{t-1},Z\_{t-2},\ldots,Z\_{t-w}\}. |  |

Within each rolling window, each predictor series is tested for stationarity using the Augmented Dickey–Fuller (ADF) test. Series that fail to reject the unit-root null at the 10% significance level are differenced once; stationary series are retained in levels. All transformed predictors are standardized to zero mean and unit variance, yielding standardized vectors Z~t−j\tilde{Z}\_{t-j} for j=1,…,wj=1,\ldots,w.

Principal component analysis (PCA) is applied within each rolling window to the standardized lagged predictor block
{Z~t−w,…,Z~t−1}\{\tilde{Z}\_{t-w},\ldots,\tilde{Z}\_{t-1}\}.
Let Σ^Z,t\hat{\Sigma}\_{Z,t} denote the sample covariance matrix computed from this block.
Denote by {(vj,t,λj,t)}j=1p\{(v\_{j,t},\lambda\_{j,t})\}\_{j=1}^{p} the eigenvector–eigenvalue pairs of Σ^Z,t\hat{\Sigma}\_{Z,t}, ordered by decreasing eigenvalues.
To eliminate sign indeterminacy across rolling windows, eigenvectors are aligned by enforcing sign consistency with those estimated in the previous window.
The jjth principal component available at time tt is constructed using only information dated t−1t-1 and earlier,

|  |  |  |
| --- | --- | --- |
|  | PCj,t=vj,t⊤​Z~t−1,j=1,…,k,\displaystyle\mathrm{PC}\_{j,t}=v\_{j,t}^{\top}\tilde{Z}\_{t-1},\qquad j=1,\ldots,k, |  |

where kk denotes the number of retained components and is set to k∈{1,2,…,10}k\in\{1,2,\ldots,10\}.
The vector of economic factors is defined as

|  |  |  |
| --- | --- | --- |
|  | Ft(k)=[PC1,t⋯PCk,t]⊤∈ℝk.F\_{t}^{(k)}=\begin{bmatrix}\mathrm{PC}\_{1,t}&\cdots&\mathrm{PC}\_{k,t}\end{bmatrix}^{\top}\in\mathbb{R}^{k}. |  |

At each time tt, the DNS factors (β1​t,β2​t,β3​t)(\beta\_{1t},\beta\_{2t},\beta\_{3t}) are estimated cross-sectionally from observed yields.
The augmented state vector is then defined as

|  |  |  |
| --- | --- | --- |
|  | Xt(k)=[β1​tβ2​tβ3​tFt(k)⊤]⊤∈ℝ3+k.X\_{t}^{(k)}=\begin{bmatrix}\beta\_{1t}&\beta\_{2t}&\beta\_{3t}&F\_{t}^{(k)\top}\end{bmatrix}^{\top}\in\mathbb{R}^{3+k}. |  |

The joint dynamics of the augmented state vector are modeled using a first-order vector autoregression,

|  |  |  |
| --- | --- | --- |
|  | Xt+1(k)=c(k)+Φ(k)​Xt(k),X\_{t+1}^{(k)}=c^{(k)}+\Phi^{(k)}X\_{t}^{(k)}, |  |

where c(k)c^{(k)} is an intercept vector and Φ(k)\Phi^{(k)} is a coefficient matrix.
For each rolling window, the VAR(1) model is estimated using the sample
{Xt−w+1(k),…,Xt(k)}\{X\_{t-w+1}^{(k)},\ldots,X\_{t}^{(k)}\}.
Multi-horizon forecasts are generated recursively by iterating the estimated VAR forward hh steps for
h∈{1,3,6,9,12}h\in\{1,3,6,9,12\}.
At each horizon, the forecasted DNS factors (β1,t+h|t,β2,t+h|t,β3,t+h|t)(\beta\_{1,t+h|t},\beta\_{2,t+h|t},\beta\_{3,t+h|t}) are mapped into yield forecasts using the Nelson–Siegel measurement equation [2.1](https://arxiv.org/html/2601.04608v1#S2.E1 "In 2.2.1 Dynamic Nelson–Siegel (DNS) Model ‣ 2.2 Factor–Augmented Dynamic Nelson Siegel (FADNS) Family ‣ 2 Methodology ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach").
The procedure is repeated for k=1,…,10k=1,\ldots,10. Forecast accuracy is evaluated using maturity-specific root mean squared forecast errors. The full estimation and forecasting procedure is summarized in E-Companion Algorithm.

### 2.3 Random Forest Family

Random Forests (RF), introduced by Breiman ([2001](https://arxiv.org/html/2601.04608v1#bib.bib7)), is an ensemble of decision trees built from independently randomized training procedures whose predictions are aggregated to produce a stable, non-overfitting predictor. In
this paper, RF serves as a high-dimensional, nonparametric benchmark for
forecasting U.S. Treasury yields. In contrast to the FADNS framework, which
imposes a parametric term-structure representation and linear state dynamics, RF
approximates conditional expectations through recursive partitioning of the
predictor space and ensemble averaging.
Fix a maturity τ\tau and a forecast horizon
h∈{1,3,6,9,12}h\in\{1,3,6,9,12\}. Let yt​(τ)y\_{t}(\tau) denote the end-of-month yield, and let
Zt∈ℝpZ\_{t}\in\mathbb{R}^{p} denote a vector of economic indicators observed at time tt.
Predictors are constructed to respect real-time data availability using
asymmetric lag conventions. Economic indicators are lagged one month relative to
yields and enter with lag indices

|  |  |  |
| --- | --- | --- |
|  | ℒZ={1,…,60},\mathcal{L}\_{Z}=\{1,\ldots,60\}, |  |

while the yield block includes the contemporaneous yield and its lags,

|  |  |  |
| --- | --- | --- |
|  | ℒy={0,…,59}.\mathcal{L}\_{y}=\{0,\ldots,59\}. |  |

The resulting predictor vector is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt\displaystyle W\_{t} | =(Zt−ℓ)ℓ∈ℒZ∪(yt−ℓ​(τ))ℓ∈ℒy,\displaystyle=\bigl(Z\_{t-\ell}\bigr)\_{\ell\in\mathcal{L}\_{Z}}\;\cup\;\bigl(y\_{t-\ell}(\tau)\bigr)\_{\ell\in\mathcal{L}\_{y}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt\displaystyle\qquad W\_{t} | ∈ℝdW,dW=60​(p+1).\displaystyle\in\mathbb{R}^{d\_{W}},\qquad d\_{W}=0(p+1). |  |

Within each rolling window, both predictors and the response variable are
rescaled using min–max normalization computed over the corresponding training
sample. Specifically, for any scalar training variable
us∈ℝu\_{s}\in\mathbb{R} (either a component of WsW\_{s} or the response
ys+h​(τ)y\_{s+h}(\tau)), the normalized value is given by

|  |  |  |
| --- | --- | --- |
|  | us,norm=us−minr∈ℐt⁡urmaxr∈ℐt⁡ur−minr∈ℐt⁡ur,s∈ℐt,u\_{s,\mathrm{norm}}=\frac{u\_{s}-\min\limits\_{r\in\mathcal{I}\_{t}}u\_{r}}{\max\limits\_{r\in\mathcal{I}\_{t}}u\_{r}-\min\limits\_{r\in\mathcal{I}\_{t}}u\_{r}},\qquad s\in\mathcal{I}\_{t}, |  |

where ℐt={t−59,…,t}\mathcal{I}\_{t}=\{t-59,\ldots,t\} denotes the rolling training window.
Predictions are subsequently transformed back to the original scale using the
inverse mapping.

For each forecast horizon hh, forecasting is formulated as the direct
nonparametric regression model

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt+h​(τ)\displaystyle y\_{t+h}(\tau) | =gh,τ​(Wt)+εt+h,\displaystyle=g\_{h,\tau}(W\_{t})+\varepsilon\_{t+h}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(εt+h∣Wt)\displaystyle\mathbb{E}\!\left(\varepsilon\_{t+h}\mid W\_{t}\right) | =0.\displaystyle=0. |  |

where gh,τ:[0,1]dW→ℝg\_{h,\tau}:[0,1]^{d\_{W}}\to\mathbb{R} is an unknown measurable regression
function.

Each base learner is a regression tree grown using the CART algorithm.
Trees are constructed by recursively partitioning the predictor space into
axis-aligned cells.
Consider a generic node TT with index set

|  |  |  |
| --- | --- | --- |
|  | ℐT={s∈ℐt:Ws∈T}.\mathcal{I}\_{T}=\{\,s\in\mathcal{I}\_{t}:\;W\_{s}\in T\,\}. |  |

The node prediction is the sample mean

|  |  |  |
| --- | --- | --- |
|  | y¯T=1|ℐT|​∑s∈ℐTys+h​(τ),\bar{y}\_{T}=\frac{1}{|\mathcal{I}\_{T}|}\sum\_{s\in\mathcal{I}\_{T}}y\_{s+h}(\tau), |  |

and node impurity is measured by the mean squared error

|  |  |  |
| --- | --- | --- |
|  | Impurity​(T)=1|ℐT|​∑s∈ℐT(ys+h​(τ)−y¯T)2.\mathrm{Impurity}(T)=\frac{1}{|\mathcal{I}\_{T}|}\sum\_{s\in\mathcal{I}\_{T}}\bigl(y\_{s+h}(\tau)-\bar{y}\_{T}\bigr)^{2}. |  |

A candidate split at node TT is defined by a coordinate
j∈{1,…,dW}j\in\{1,\ldots,d\_{W}\} and threshold c∈(0,1)c\in(0,1), inducing child nodes

|  |  |  |
| --- | --- | --- |
|  | TL={w∈T:wj≤c},TR={w∈T:wj>c}.T\_{L}=\{\,w\in T:\;w\_{j}\leq c\,\},\qquad T\_{R}=\{\,w\in T:\;w\_{j}>c\,\}. |  |

The split is evaluated by the impurity reduction

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δsk​(j,c∣T)\displaystyle\Delta\_{\mathrm{sk}}(j,c\mid T) | =Impurity​(T)−|ℐTL||ℐT|​Impurity​(TL)\displaystyle=\mathrm{Impurity}(T)-\frac{|\mathcal{I}\_{T\_{L}}|}{|\mathcal{I}\_{T}|}\,\mathrm{Impurity}(T\_{L}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −|ℐTR||ℐT|​Impurity​(TR).\displaystyle\quad-\frac{|\mathcal{I}\_{T\_{R}}|}{|\mathcal{I}\_{T}|}\,\mathrm{Impurity}(T\_{R}). |  |

and the optimal split maximizes
Δsk​(j,c∣T)\Delta\_{\mathrm{sk}}(j,c\mid T) over the admissible set
𝒜​(T)\mathcal{A}(T).
Equivalently, defining the sum of squared errors

|  |  |  |
| --- | --- | --- |
|  | SSE​(T)=∑s∈ℐT(ys+h​(τ)−y¯T)2,\mathrm{SSE}(T)=\sum\_{s\in\mathcal{I}\_{T}}\bigl(y\_{s+h}(\tau)-\bar{y}\_{T}\bigr)^{2}, |  |

maximizing Δsk​(j,c∣T)\Delta\_{\mathrm{sk}}(j,c\mid T) is equivalent to maximizing

|  |  |  |
| --- | --- | --- |
|  | SSE​(T)−SSE​(TL)−SSE​(TR),\mathrm{SSE}(T)-\mathrm{SSE}(T\_{L})-\mathrm{SSE}(T\_{R}), |  |

which is the standard CART splitting rule.

Tree growth is subject to data-driven regularization through minimum leaf size
and depth constraints. The number of trees, minimum node size,
maximum depth, feature subsampling rule, and bootstrap usage are selected via
randomized cross-validation within each rolling window. Specifically, for each
forecast origin, a randomized search over the hyperparameter space is conducted
using a fixed number of cross-validation folds.
The rolling-window procedure advances one month at a time, producing direct
out-of-sample forecasts for each maturity and horizon. The entire estimation is
repeated under 10 independent random seeds to account for algorithmic
variability. Final forecast accuracy is evaluated by aggregating results across
seeds.
The complete rolling-window direct RF forecasting procedure is summarized in
E-Companion Algorithm.

### 2.4 Forecast Combination

To enhance predictive robustness and exploit complementary information across forecasting models, we combine MM candidate forecasts drawn from
candidate models using a comprehensive set of
forecast combination schemes. At each forecast origin tt, a non-negative weight
vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt\displaystyle w\_{t} | =(w1​t,…,wM​t)′∈ΔM,\displaystyle=(w\_{1t},\ldots,w\_{Mt})^{\prime}\in\Delta\_{M}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔM\displaystyle\Delta\_{M} | :={w∈ℝ+M:𝟏′​w=1}.\displaystyle=\bigl\{\,w\in\mathbb{R}^{M}\_{+}:\mathbf{1}^{\prime}w=1\,\bigr\}. |  |

is selected based on historical forecast performance.

Let y^m,t\hat{y}\_{m,t} denote the forecast produced by model mm and let YtY\_{t} be
the realized outcome. The combined forecast and its corresponding forecast
error are defined as

|  |  |  |
| --- | --- | --- |
|  | y^t(c)=∑m=1Mwm,t​y^m,t,et(c)=Yt−y^t(c).\hat{y}^{(c)}\_{t}=\sum\_{m=1}^{M}w\_{m,t}\hat{y}\_{m,t},\qquad e^{(c)}\_{t}=Y\_{t}-\hat{y}^{(c)}\_{t}. |  |

All weights are estimated separately for each maturity–horizon pair (τ,h)(\tau,h)
using a rolling window of length W=24W=24 months.

#### 2.4.1 Classic Weighting Schemes

##### (1) Equal-Weight Averaging (FC–EW).

As a benchmark, equal-weight averaging assigns identical weight to all models,

|  |  |  |
| --- | --- | --- |
|  | wm,t=1M,m=1,…,M.w\_{m,t}=\frac{1}{M},\qquad m=1,\ldots,M. |  |

This method is free of estimation error and serves as a baseline in the
presence of model uncertainty.

##### (2) Rank-Based Averaging (FC–RANK).

Models are ranked according to their rolling root-mean-squared forecast error,

|  |  |  |
| --- | --- | --- |
|  | RMSFE^m,t=1W​∑j=t−Wt−1em,j2.\widehat{\mathrm{RMSFE}}\_{m,t}=\sqrt{\frac{1}{W}\sum\_{j=t-W}^{t-1}e\_{m,j}^{2}}. |  |

Let rm,tr\_{m,t} denote the rank of model mm, with r=1r=1 assigned to the model with
the smallest RMSFE. Weights are then defined as

|  |  |  |
| --- | --- | --- |
|  | wm,t=rm,t−1∑k=1Mrk,t−1,w\_{m,t}=\frac{r\_{m,t}^{-1}}{\sum\_{k=1}^{M}r\_{k,t}^{-1}}, |  |

assigning higher weight to more accurate models while preserving diversification.

##### (3) Inverse-RMSE Averaging (FC–RMSE).

This performance-based scheme assigns weights inversely proportional
to historical RMSFE magnitudes,

|  |  |  |
| --- | --- | --- |
|  | wm,t=RMSFE^m,t−1∑k=1MRMSFE^k,t−1.w\_{m,t}=\frac{\widehat{\mathrm{RMSFE}}\_{m,t}^{-1}}{\sum\_{k=1}^{M}\widehat{\mathrm{RMSFE}}\_{k,t}^{-1}}. |  |

This approach places stronger emphasis on absolute forecast accuracy.

##### (4) Winner–Take–All Selection (FC–MSE).

This method assigns full weight to the single best-performing model in the
rolling window. Let

|  |  |  |
| --- | --- | --- |
|  | m∗=arg⁡minm⁡MSE^m,t,m^{\ast}=\arg\min\_{m}\widehat{\mathrm{MSE}}\_{m,t}, |  |

where MSE^m,t\widehat{\mathrm{MSE}}\_{m,t} denotes the rolling mean squared forecast
error. The weight vector is given by

|  |  |  |
| --- | --- | --- |
|  | wm,t={1,m=m∗,0,m≠m∗.w\_{m,t}=\begin{cases}1,&m=m^{\ast},\\ 0,&m\neq m^{\ast}.\end{cases} |  |

While potentially optimal in hindsight, this approach is sensitive to sampling
variation.

##### (5) OLS-Screened Averaging (FC–OLS).

This scheme first screens models based on recent performance and then applies
ordinary least squares averaging to the selected subset. Let
q=⌊0.3​M⌋q=\lfloor 0.3M\rfloor denote the number of models selected with the lowest rolling RMSE, with all nonselected models receiving zero weight.
Define the average forecast error across all models at time jj as

|  |  |  |
| --- | --- | --- |
|  | e¯j=1M​∑m=1Mem,j.\bar{e}\_{j}=\frac{1}{M}\sum\_{m=1}^{M}e\_{m,j}. |  |

Let E(q),jE\_{(q),j} denote the vector of forecast errors of the selected models.
OLS coefficients b∈ℝqb\in\mathbb{R}^{q} are obtained from

|  |  |  |
| --- | --- | --- |
|  | minb⁡1W​∑j=t−Wt−1(e¯j−E(q),j′​b)2.\min\_{b}\frac{1}{W}\sum\_{j=t-W}^{t-1}\bigl(\bar{e}\_{j}-E\_{(q),j}^{\prime}b\bigr)^{2}. |  |

Final combination weights are proportional to the absolute coefficients,

|  |  |  |
| --- | --- | --- |
|  | wm,t=|bm|∑k=1q|bk|,w\_{m,t}=\frac{|b\_{m}|}{\sum\_{k=1}^{q}|b\_{k}|}, |  |

.

#### 2.4.2 Variance- and Risk-Minimizing Combination

Let tt denote the forecast origin and let WW be the length of the rolling
evaluation window. For each j∈{t−W,…,t−1}j\in\{t-W,\ldots,t-1\}, define the vector of
forecast errors across the MM candidate models as

|  |  |  |
| --- | --- | --- |
|  | Ej:=(e1,j,…,eM,j)∈ℝ1×M.E\_{j}:=(e\_{1,j},\ldots,e\_{M,j})\in\mathbb{R}^{1\times M}. |  |

Stacking these vectors yields the rolling forecast-error matrix

|  |  |  |
| --- | --- | --- |
|  | E=[Et−W⋮Et−1]∈ℝW×M.E=\begin{bmatrix}E\_{t-W}\\ \vdots\\ E\_{t-1}\end{bmatrix}\in\mathbb{R}^{W\times M}. |  |

All methods in this subsection select weights
w∈ΔM:={w∈ℝ+M:𝟏′​w=1}w\in\Delta\_{M}:=\{w\in\mathbb{R}^{M}\_{+}:\mathbf{1}^{\prime}w=1\}.
In our empirical implementation, we set W=24W=24 months and require a minimum of
five observations before updating weights.

##### (6) Minimum-Variance Averaging (FC–MV).

This method selects combination weights by minimizing the variance of the
combined forecast error,

|  |  |  |
| --- | --- | --- |
|  | minw∈ΔM⁡w⊤​Σ^λ​w,\min\_{w\in\Delta\_{M}}\;w^{\top}\widehat{\Sigma}\_{\lambda}w, |  |

where

|  |  |  |
| --- | --- | --- |
|  | Σ^=Cov​(E),Σ^λ=Σ^+λ​IM.\widehat{\Sigma}=\mathrm{Cov}(E),\qquad\widehat{\Sigma}\_{\lambda}=\widehat{\Sigma}+\lambda I\_{M}. |  |

Here Σ^\widehat{\Sigma} is the sample covariance matrix of rolling forecast
errors, computed after demeaning. The ridge adjustment with
λ=10−6\lambda=10^{-6} stabilizes matrix inversion in the presence of strong
cross-model dependence. The unconstrained solution admits the closed-form
expression

|  |  |  |
| --- | --- | --- |
|  | w^t=Σ^λ−1​𝟏𝟏′​Σ^λ−1​𝟏.\widehat{w}\_{t}=\frac{\widehat{\Sigma}\_{\lambda}^{-1}\mathbf{1}}{\mathbf{1}^{\prime}\widehat{\Sigma}\_{\lambda}^{-1}\mathbf{1}}. |  |

In implementation, the Moore–Penrose pseudoinverse is used for numerical
stability, and the resulting weights are projected onto the simplex to enforce
non-negativity and unit-sum constraints.

##### (7) Stacking Regression (FC–STACK).

Stacking regression selects weights by minimizing the empirical mean squared
prediction error of the combined forecast over the rolling window,

|  |  |  |
| --- | --- | --- |
|  | minw∈ΔM⁡1W​∑j=t−Wt−1(Ej​w)2.\min\_{w\in\Delta\_{M}}\frac{1}{W}\sum\_{j=t-W}^{t-1}\bigl(E\_{j}w\bigr)^{2}. |  |

Equivalently, defining the empirical second-moment matrix

|  |  |  |
| --- | --- | --- |
|  | S^=1W​E⊤​E,\widehat{S}=\frac{1}{W}E^{\top}E, |  |

the problem can be written as the convex quadratic program

|  |  |  |
| --- | --- | --- |
|  | minw∈ΔM⁡w⊤​S^​w.\min\_{w\in\Delta\_{M}}\;w^{\top}\widehat{S}w. |  |

Unlike minimum-variance averaging, stacking regression does not demean forecast
errors and therefore penalizes both variance and bias of the combined
forecast. The resulting convex program is solved numerically using Sequential
Least Squares Quadratic Programming (SLSQP), with inverse-RMSE weights used as a
fallback in the event of numerical nonconvergence.

##### (8) Penalized Least-Absolute-Deviation Averaging (FC–LAD).

To achieve robustness against heavy-tailed forecast errors and outliers, we
employ penalized least-absolute-deviation (LAD) averaging inspired by Jiang et al. ([2025](https://arxiv.org/html/2601.04608v1#bib.bib38)). The estimator solves

|  |  |  |
| --- | --- | --- |
|  | minw∈ΔM⁡{1W​∑j=t−Wt−1|Ej​w|+ϕnW​ 1′​w},\min\_{w\in\Delta\_{M}}\left\{\frac{1}{W}\sum\_{j=t-W}^{t-1}\bigl|E\_{j}w\bigr|+\frac{\phi\_{n}}{W}\,\mathbf{1}^{\prime}w\right\}, |  |

The penalty parameter ϕn\phi\_{n} = 0.02
is fixed across maturities and horizons to avoid
overfitting. Introducing slack variables uj≥0u\_{j}\geq 0 such that

|  |  |  |
| --- | --- | --- |
|  | uj≥|Ej​w|,j=t−W,…,t−1,u\_{j}\geq|E\_{j}w|,\qquad j=t-W,\ldots,t-1, |  |

the problem can be equivalently expressed as the linear program

|  |  |  |  |
| --- | --- | --- | --- |
|  | minw,u\displaystyle\min\_{w,u} | 1W​𝟏′​u+ϕnW​𝟏′​w\displaystyle\frac{1}{W}\mathbf{1}^{\prime}u+\frac{\phi\_{n}}{W}\mathbf{1}^{\prime}w |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | −E​w≤u,E​w≤u,\displaystyle-Ew\leq u,\quad Ew\leq u, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | w≥0,u≥0,𝟏′​w=1,\displaystyle w\geq 0,\quad u\geq 0,\quad\mathbf{1}^{\prime}w=1, |  |

which is solved using a high-precision linear programming solver.

#### 2.4.3 Aggregate Forecast Through Exponential Reweighting (AFTER)

.
Following Yang ([2004](https://arxiv.org/html/2601.04608v1#bib.bib21)), we consider dynamic forecast combination
methods based on exponential reweighting of recent forecast errors. Let
em,te\_{m,t} denote the forecast error of model mm at time tt. The combination
weights are updated recursively according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | wm,t\displaystyle w\_{m,t} | =wm,t−1​v^m,t−1−1/2​exp⁡(−em,t−122​v^m,t−1)∑k=1Mwk,t−1​v^k,t−1−1/2​exp⁡(−ek,t−122​v^k,t−1),\displaystyle=\frac{w\_{m,t-1}\,\hat{v}\_{m,t-1}^{-1/2}\exp\!\left(-\frac{e\_{m,t-1}^{2}}{2\hat{v}\_{m,t-1}}\right)}{\sum\_{k=1}^{M}w\_{k,t-1}\,\hat{v}\_{k,t-1}^{-1/2}\exp\!\left(-\frac{e\_{k,t-1}^{2}}{2\hat{v}\_{k,t-1}}\right)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | m=1,…,M.\displaystyle\qquad m=1,\ldots,M. |  |

with initialization wm,0=1/Mw\_{m,0}=1/M.

Let L∈ℕL\in\mathbb{N} denote the lookback window length used for dynamic
reweighting. In the empirical analysis, we set L=20L=20 and require at least five
observations before updating weights. Define

|  |  |  |
| --- | --- | --- |
|  | st:=max⁡{1,t−L}.s\_{t}:=\max\{1,\,t-L\}. |  |

At each time tt, all quantities are computed using historical forecast errors
{em,j}j=stt−1\{e\_{m,j}\}\_{j=s\_{t}}^{t-1}. Variance estimates are truncated below by a small
positive constant for numerical stability.
We consider three AFTER specifications, which differ only in the construction of
the variance term v^m,t\hat{v}\_{m,t}.

##### (9) AFTER with Rolling Variance (AFTER–Rolling).

The forecast-error variance is estimated using a rolling sample variance,

|  |  |  |
| --- | --- | --- |
|  | v^m,t=Var​(em,st,…,em,t−1).\hat{v}\_{m,t}=\mathrm{Var}\!\left(e\_{m,s\_{t}},\ldots,e\_{m,t-1}\right). |  |

##### (10) AFTER with EWMA Variance (AFTER–EWMA).

The variance is estimated using an exponentially weighted moving average of past
squared forecast errors,

|  |  |  |
| --- | --- | --- |
|  | v^m,t=(1−λ)​∑j=stt−1λt−1−j​em,j2,\hat{v}\_{m,t}=(1-\lambda)\sum\_{j=s\_{t}}^{t-1}\lambda^{\,t-1-j}e\_{m,j}^{2}, |  |

where the decay parameter λ∈(0,1)\lambda\in(0,1) is assumed constant across maturities and forecast horizons.

##### (11) AFTER under Homoskedastic Errors (AFTER–Simplified).

We also consider a homoskedastic benchmark in which the variance term is treated
as constant and omitted from the update rule. The weights are updated according
to

|  |  |  |
| --- | --- | --- |
|  | wm,t=wm,t−1​exp⁡(−12​∑j=stt−1em,j2)∑k=1Mwk,t−1​exp⁡(−12​∑j=stt−1ek,j2).w\_{m,t}=\frac{w\_{m,t-1}\exp\!\left(-\frac{1}{2}\sum\_{j=s\_{t}}^{t-1}e\_{m,j}^{2}\right)}{\sum\_{k=1}^{M}w\_{k,t-1}\exp\!\left(-\frac{1}{2}\sum\_{j=s\_{t}}^{t-1}e\_{k,j}^{2}\right)}. |  |

Across all specifications, AFTER assigns larger weights to models with smaller
recent forecast errors, with the degree of adaptivity governed by the lookback
window LL and the variance specification.

#### 2.4.4 Distributionally Robust Forecast Combination(DRO).

Rather than relying on plug-in estimates of forecast error moments, which can be
unstable in short rolling samples, we consider distributionally robust forecast
combination schemes that explicitly penalize tail losses and instability in
second-moment estimates. This design is motivated by the insight of
Delage and Ye ([2010](https://arxiv.org/html/2601.04608v1#bib.bib41)) that, under moment uncertainty, worst-case
distributions inflate tail risk and variance. Accordingly, our DRO-based
procedures downweight models exhibiting poor tail behavior or unstable covariance
structures, resulting in more stable combination weights in finite samples.
Let ek,je\_{k,j} denote the forecast error of model kk at time jj. For each
forecast origin tt, losses are evaluated over a rolling window
j∈{t−W,…,t−1}j\in\{t-W,\ldots,t-1\} with W=24W=24.

##### (12) Tail-Robust DRO via Expected Shortfall (FC–DRO–ES).

To guard against downside risk in forecast errors, we define a model-specific
tail-risk loss based on expected shortfall (ES). For each model kk, the rolling
loss is computed as

|  |  |  |
| --- | --- | --- |
|  | LkES(t)=ESα(ek,j:j=t−W,…,t−1),L\_{k}^{\mathrm{ES}}(t)=\mathrm{ES}\_{\alpha}\!\left(e\_{k,j}:j=t-W,\ldots,t-1\right), |  |

Here ESα​(⋅)\mathrm{ES}\_{\alpha}(\cdot) denotes the empirical expected shortfall at
level α\alpha= 0.10, defined as follows. Let
{x1,…,xW}\{x\_{1},\ldots,x\_{W}\} denote a sample of forecast errors and let
qαq\_{\alpha} be the empirical α\alpha-quantile,

|  |  |  |
| --- | --- | --- |
|  | qα=inf{x∈ℝ:1W​∑j=1W𝟏​{xj≤x}≥α}.q\_{\alpha}=\inf\left\{x\in\mathbb{R}:\frac{1}{W}\sum\_{j=1}^{W}\mathbf{1}\{x\_{j}\leq x\}\geq\alpha\right\}. |  |

The expected shortfall is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα​(x1,…,xW)\displaystyle\mathrm{ES}\_{\alpha}(x\_{1},\ldots,x\_{W}) | =1|ℐα|​∑j∈ℐαxj,\displaystyle=\frac{1}{|\mathcal{I}\_{\alpha}|}\sum\_{j\in\mathcal{I}\_{\alpha}}x\_{j}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐα\displaystyle\mathcal{I}\_{\alpha} | ={j:xj≤qα}.\displaystyle=\{\,j:x\_{j}\leq q\_{\alpha}\,\}. |  |

Weights are obtained via exponential reweighting,

|  |  |  |
| --- | --- | --- |
|  | wk,t=exp⁡(η​L~kES​(t))∑m=1Mexp⁡(η​L~mES​(t)),w\_{k,t}=\frac{\exp\!\bigl(\eta\,\tilde{L}\_{k}^{\mathrm{ES}}(t)\bigr)}{\sum\_{m=1}^{M}\exp\!\bigl(\eta\,\tilde{L}\_{m}^{\mathrm{ES}}(t)\bigr)}, |  |

where L~kES​(t)=LkES​(t)−minm⁡LmES​(t)\tilde{L}\_{k}^{\mathrm{ES}}(t)=L\_{k}^{\mathrm{ES}}(t)-\min\_{m}L\_{m}^{\mathrm{ES}}(t)
is a numerically stabilized loss and η>0\eta>0 controls the degree of robustness.
In the empirical analysis, we fix η=5.0\eta=5.0.

##### (13) Regularized Mean–Variance Combination (FC–DRMV).

To mitigate
sensitivity to covariance estimation error, we consider a regularized
mean–variance formulation that penalizes uncertainty in second-moment
estimation with ridge regularization on the covariance matrix.
Let Σt\Sigma\_{t} denote the sample covariance matrix of forecast errors computed
over a rolling window of length W=24W=24. We obtain combination weights by solving

|  |  |  |
| --- | --- | --- |
|  | minw∈ΔM⁡w⊤​(Σt+τ​IM)​w,\min\_{w\in\Delta\_{M}}\;w^{\top}(\Sigma\_{t}+\tau I\_{M})w, |  |

where τ>0\tau>0 is a regularization parameter. The solution admits the closed-form
expression

|  |  |  |
| --- | --- | --- |
|  | wt=(Σt+τ​IM)−1​𝟏𝟏⊤​(Σt+τ​IM)−1​𝟏.w\_{t}=\frac{(\Sigma\_{t}+\tau I\_{M})^{-1}\mathbf{1}}{\mathbf{1}^{\top}(\Sigma\_{t}+\tau I\_{M})^{-1}\mathbf{1}}. |  |

In the empirical implementation, we set τ=0.05\tau=0.05. The ridge term τ​IM\tau I\_{M}
stabilizes weight selection when covariance estimates are noisy or nearly
singular.

##### (14) Hybrid Loss Combination with Accuracy and Tail Risk (FC–MIX).

To balance average forecast accuracy with robustness to extreme forecast errors,
we consider a hybrid loss that combines mean squared error and tail risk. For
each model kk, the rolling loss is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | LkMIX​(t)\displaystyle L\_{k}^{\mathrm{MIX}}(t) | =(1−λ)​MSEk​(t)+λ​ESα​(Ek,t),\displaystyle=(1-\lambda)\,\mathrm{MSE}\_{k}(t)+\lambda\,\mathrm{ES}\_{\alpha}\!\left(E\_{k,t}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ek,t\displaystyle E\_{k,t} | ={ek,j2:j=t−W,…,t−1}.\displaystyle=\{\,e\_{k,j}^{2}:j=t-W,\ldots,t-1\,\}. |  |

where MSEk​(t)\mathrm{MSE}\_{k}(t) denotes the rolling mean squared forecast error and
ESα​(⋅)\mathrm{ES}\_{\alpha}(\cdot) is the empirical expected shortfall at level
α=0.10\alpha=0.10. The parameter λ∈[0,1]\lambda\in[0,1] controls the trade-off between
average forecast accuracy and sensitivity to downside tail risk.
Combination weights are obtained via exponential reweighting,

|  |  |  |
| --- | --- | --- |
|  | wk,t=exp⁡(η​L~kMIX​(t))∑m=1Mexp⁡(η​L~mMIX​(t)),w\_{k,t}=\frac{\exp\!\bigl(\eta\,\tilde{L}\_{k}^{\mathrm{MIX}}(t)\bigr)}{\sum\_{m=1}^{M}\exp\!\bigl(\eta\,\tilde{L}\_{m}^{\mathrm{MIX}}(t)\bigr)}, |  |

where the stabilized loss is defined as

|  |  |  |
| --- | --- | --- |
|  | L~kMIX​(t)=LkMIX​(t)−minm=1,…,M⁡LmMIX​(t).\tilde{L}\_{k}^{\mathrm{MIX}}(t)=L\_{k}^{\mathrm{MIX}}(t)-\min\_{m=1,\ldots,M}L\_{m}^{\mathrm{MIX}}(t). |  |

This normalization leaves relative weights unchanged and improves numerical
stability of the exponential reweighting. In the empirical analysis, we set
λ=0.5\lambda=0.5, η=5.0\eta=5.0.

The complete forecast combination procedure is summarized in
E-Companion Algorithm.

## 3 Results

### 3.1 Model Performance Analysis

#### 3.1.1 Random Forest Famiily

To evaluate predictive performance, we conduct 10 independent Random Forest runs with different random seeds and report Root Mean Square Forecast Errors (RMSFE), expressed in basis points (bps, 0.01%).
Appendix Table [1](https://arxiv.org/html/2601.04608v1#A1.T1 "Table 1 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") reports the mean RMSFE across maturities and forecast horizons (1–12 months ahead), with the corresponding [min,max][\min,\max] range across runs shown beneath each mean.
The RF model delivers stable forecast accuracy across horizons, with RMSFE remaining broadly flat from one-month to twelve-month horizons for all maturities. No systematic deterioration in forecast accuracy is observed as the forecast horizon increases, indicating that multi-step forecasting does not materially amplify forecast error.

Across maturities, short-end yields (3M–6M) exhibit the largest RMSFE, averaging around 24–25 bps, reflecting higher short-rate volatility. Forecast errors decline steadily along the curve, with long-dated maturities (20Y–30Y) achieving the lowest RMSFE, at approximately 13–14 bps. Overall, the RF model exhibits strong cross-maturity robustness and limited horizon sensitivity.

#### 3.1.2 FADNS Family

DNS results in Appendix Table [2](https://arxiv.org/html/2601.04608v1#A1.T2 "Table 2 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") and FADNS results in Table [3](https://arxiv.org/html/2601.04608v1#A1.T3 "Table 3 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach"), [4](https://arxiv.org/html/2601.04608v1#A1.T4 "Table 4 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach"), [5](https://arxiv.org/html/2601.04608v1#A1.T5 "Table 5 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach"), [6](https://arxiv.org/html/2601.04608v1#A1.T6 "Table 6 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") and [7](https://arxiv.org/html/2601.04608v1#A1.T7 "Table 7 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") report RMSFE across maturities and forecast horizons from one to twelve months ahead.
Appendix Table [8](https://arxiv.org/html/2601.04608v1#A1.T8 "Table 8 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") shows that best number of PCA factors for each maturity and horizon.

First, forecast accuracy under the DNS model deteriorates monotonically with the forecast horizon. RMSFE increases from approximately 25–40 bps at the one-month horizon to above 100 bps by six months and exceeds 130 bps at the twelve-month horizon for most maturities. This behavior is uniform across the yield curve and reflects cumulative error propagation under recursive multi-step forecasting in low-dimensional term-structure models.

Second, augmenting DNS with economic indicators through the FADNS framework improves short-horizon performance. At the one-month horizon, FADNS models incorporating rolling PCA factors constructed from economic indicators consistently reduce RMSFE relative to DNS across maturities. The gains are most pronounced at short and intermediate maturities, where RMSFE declines by roughly 5–15 bps compared to the baseline DNS model. For the one-month-ahead horizon, the FADNS model achieves forecast performance comparable to that of the Random Forest models.

Third, although FADNS improves near-term forecasts, it does not eliminate error accumulation inherent in recursive long-horizon forecasting. While FADNS continues to outperform DNS at the three-month horizon, forecast errors increase rapidly beyond six months for all PCA specifications. At the nine- and twelve-month horizons, RMSFE exceeds 150 bps at the short end of the curve and remains above 120 bps even at long maturities. The results are much worse than random forest models.

#### 3.1.3 Forecast Combination

Tables [9](https://arxiv.org/html/2601.04608v1#A1.T9 "Table 9 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach"), [10](https://arxiv.org/html/2601.04608v1#A1.T10 "Table 10 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") report RMSFE for a broad set of forecast combination methods applied to two model pools: (i) Random Forest (RF) models only, and (ii) a hybrid pool consisting of 10 FADNS and 10 RF models. Several systematic patterns emerge.

When forecast combinations are constructed exclusively from RF models, performance differences across combination rules are modest. Overall, forecast accuracy remains stable across maturities, with RMSFE increasing gradually along the curve but exhibiting limited sensitivity to the choice of combination method. This result reflects the strong baseline performance and low cross-model dispersion within the RF ensemble.

In contrast, combining forecasts from the heterogeneous FADNS+RF pool substantially increases the relevance of the combination rule.
Robust combination methods deliver systematically improved performance in the hybrid setting. Rank-based weighting (FC–RANK), LAD combinations (FC–LAD), and Distributionally Robust approaches (FC–DRO–ES, FC–DRO–MIX, FC–DRMV) consistently achieve lower RMSFE across most maturities. These methods effectively mitigate the influence of high-error FADNS forecasts while preserving the strong predictive content of RF models.

Overall, the results indicate that the effectiveness of forecast combination critically depends on cross-model heterogeneity. Adaptive distributionally robust weighting schemes are essential when combining structurally different forecasting models.

### 3.2 Forecast Combination Dynamics over Time

Figure [3](https://arxiv.org/html/2601.04608v1#A1.F3 "Figure 3 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") presents the time-series dynamics of one-month-ahead forecast errors for the hybrid RF–FADNS forecast combinations across the entire U.S. Treasury yield curve. Each subfigure corresponds to a specific maturity and reports forecast errors generated by four classes of combination schemes: distributionally robust (DRO) combinations, AFTER-type adaptive methods, variance-risk minimization strategies, and classic forecast combinations.

During periods of extreme market stress—most notably the COVID-19 shock in early 2020 and the transition from quantitative easing to quantitative tightening during the aggressive monetary tightening cycle beginning in mid-2022—forecast errors increase sharply across all maturities. The magnitude and persistence of these spikes, however, vary substantially across forecast-combination methods. Distributionally robust combinations exhibit markedly smoother error dynamics during these episodes, with lower volatility and faster mean reversion than alternative approaches.

Robustness gains from distributionally robust combinations are particularly pronounced at longer maturities, where forecast uncertainty is amplified by persistent macroeconomic and policy risks. In this segment of the yield curve, DRO-based combinations deliver consistently more stable error paths, while adaptive methods display higher variance and greater sensitivity to transient shocks. Overall, the results indicate that distributionally robust forecast combinations provide superior stability both during extreme market events and along the long end of the yield curve.

### 3.3 Weight Dynamics under Distributionally Robust Forecast Combinations

Figures [4](https://arxiv.org/html/2601.04608v1#A1.F4 "Figure 4 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach"), [5](https://arxiv.org/html/2601.04608v1#A1.F5 "Figure 5 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach"), and [6](https://arxiv.org/html/2601.04608v1#A1.F6 "Figure 6 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") illustrate the time-varying weight dynamics of the three distributionally robust forecast combination schemes. For each Treasury maturity, the figures report the evolution of aggregate weights assigned to the Random Forest (RF) forecast group and the FADNS-based forecast group at the one-month horizon.

Across all three DRO specifications, a common pattern emerges: forecast weights are reallocated rapidly during periods of extreme market stress, including the COVID-19 shock in 2020 and the monetary policy regime shift associated with the aggressive tightening cycle beginning in mid-2022. During these episodes, the relative importance of RF and FADNS forecasts adjusts sharply and persistently, in contrast to the smoother and more stable weight paths observed during tranquil periods.

This behavior reflects the core objective of distributionally robust optimization. When forecast errors undergo abrupt changes in scale or distributional characteristics, DRO schemes down-weight models that perform poorly under worst-case loss considerations and reallocate weight toward forecasts that offer greater protection against downside risk. As a result, the balance between the RF and FADNS forecast groups responds quickly to new information.

Overall, the evidence suggests that the dynamic weighting behavior induced by distributionally robust combinations is well suited for robust decision making in the presence of extreme events and structural change.

## 4 Predictive Stability and Robustness

### 4.1 U.S. Benchmark Treasury Yield Curve

We evaluate the Random Forest (RF) model on the U.S. benchmark Treasury yield curve using monthly data from Jan 2010 to August 2025, chosen to ensure comparability with the cross-country analysis in the subsequent robustness check. The FADNS model is not applied because it is restricted to zero-coupon yields, whereas benchmark long-maturity Treasury yields are coupon-bearing. Forecasts are generated jointly across maturities using a multi-output specification. Two independent RF runs with different random seeds (8270 and 1860) are conducted, and forecast accuracy is evaluated using RMSFE at horizons of 1, 3, 6, 9, and 12 months. As shown in Table in E-Companion, forecast accuracy is stable across horizons and seeds, with one-month RMSFE ranging from 30-35 basis points at the short end to 17-18 basis points at the 30-year maturity.

We then compare the multi-output Random Forest with a single-maturity specification in which each yield is forecast independently using the same predictor set, rolling window, and hyperparameter search procedure. The results, reported in E-Companion, indicate that the joint multi-output specification delivers lower RMSFE across most maturities and forecast horizons though the gains are modest.

We next examine the effect of augmenting the predictor set with Treasury International Capital (TIC) variables, which become available starting in September 2014. Specifically, we include U.S. TIC: Gross External Debt Position and U.S. General Government Gross External Debt Position to capture cross-border Treasury supply–demand dynamics. The inclusion of these variables necessarily shortens the effective estimation sample.
Figure [1](https://arxiv.org/html/2601.04608v1#A1.F1 "Figure 1 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") reports the change in RMSFE relative to the baseline specification without TIC variables. Negative values indicate forecast accuracy improvements. The most pronounced gains are observed at the 30-year maturity for the 12-month-ahead forecast horizon. Nevertheless, given the reduced sample length, the estimated effects of TIC variables should be interpreted with caution, as their contribution may not be apparent in finite samples.

#### 4.1.1 SHAP-Based Interpretation

We use SHAP (Lundberg and Lee [2017](https://arxiv.org/html/2601.04608v1#bib.bib1)) to interpret predictions from the multi-output Random Forest model. For each forecast horizon h∈{1,3,6,9,12}h\in\{1,3,6,9,12\}, random seed, and yield maturity, SHAP values are computed for all predictors and summarized by mean absolute values.
To obtain global feature importance measures that are robust across the yield curve, SHAP values are aggregated across maturities for fixed horizons and seeds. Specifically,

|  |  |  |
| --- | --- | --- |
|  | GlobalSHAPj​(h,s)=1|𝒯|​∑τ∈𝒯𝔼​[|ϕj​(τ,h,s)|],\text{GlobalSHAP}\_{j}(h,s)=\frac{1}{|\mathcal{T}|}\sum\_{\tau\in\mathcal{T}}\mathbb{E}\!\left[\left|\phi\_{j}(\tau,h,s)\right|\right], |  |

where ϕj​(τ,h,s)\phi\_{j}(\tau,h,s) denotes the SHAP value of feature jj for maturity τ\tau at horizon hh and seed ss. Features are ranked by GlobalSHAPj​(h,s)\text{GlobalSHAP}\_{j}(h,s), and comparisons across horizons and seeds are used to assess the stability of predictive drivers.

Figure [2](https://arxiv.org/html/2601.04608v1#A1.F2 "Figure 2 ‣ Appendix A Appendix A: Tables and Figures ‣ Forecasting the U.S. Treasury Yield Curve: A Distributionally Robust Machine Learning Approach") reports maturity-averaged global SHAP values for the Random Forest model across forecast horizons h∈{1,3,6,9,12}h\in\{1,3,6,9,12\} and two independent random seeds. Feature importance rankings are highly stable across seeds, indicating that the inferred explanatory structure is robust to initialization and sampling variation. The set of influential predictors exhibits systematic horizon dependence: short-horizon forecasts place greater weight on high-frequency real activity indicators, while medium- and long-horizon forecasts increasingly emphasize slower-moving macroeconomic fundamentals, including price indices, income and consumption measures, and balance-sheet variables. Inflation-related price indices and labor market indicators rank among the most important predictors at all horizons, consistent with the Federal Reserve’s dual mandate, while financial conditions variables become more prominent at longer horizons, suggesting a gradual transmission to treasury yields.

### 4.2 Extension to Global Sovereign Bond

We extend the Random Forest forecasting framework to a cross-country setting by examining 10-year benchmark government bond yields for a set of major economies, including Canada, China, Germany, Japan, Malaysia, the United Kingdom, and the United States(All data are obtained from the same source as the U.S. data. The full list of variables is provided in the E-Companion (Tables EC.1–EC.7).The evaluation sample begins in January 2010, and forecasts are generated at horizons h∈{1,3,6,9,12}h\in\{1,3,6,9,12\} using the same model specification and multiple random seeds as in the U.S. Benchmark Treasury Yield Curve. Table in E-Companion reports mean root mean squared forecast error (RMSFE) results in basis points.

Forecast accuracy varies substantially across countries. China and Japan exhibit the lowest RMSFE levels across all horizons, while the United Kingdom and the United States display comparatively higher forecast errors, consistent with differences in interest rate environments and yield volatility. For most countries, RMSFE remains broadly stable across forecast horizons. Overall, RMSFE levels ranging from approximately 15 to 45 basis points indicate that the Random Forest model delivers robust predictive performance in an international context and generalizes well across global sovereign bond markets.

## 5 Conclusion

This paper develops a distributionally robust ensemble framework for U.S. Treasury yield curve forecasting that integrates a rolling-window Factor-Augmented Dynamic Nelson–Siegel (FADNS) model with high-dimensional Random Forest (RF) forecasts through adaptive forecast combination. A central contribution is a distributionally robust combination scheme that penalizes downside risk from machine-learning forecasts using expected shortfall while stabilizing second-moment estimation through ridge-regularized covariance matrices, thereby providing a robust foundation for decision making under policy uncertainty and market stress. To the best of our knowledge, this is the first framework to incorporate distributionally robust optimization directly into ensemble forecasting of the U.S. Treasury yield curve, unifying machine learning, robust optimization, and managerial decision making under uncertainty.

Empirical results based on monthly data and forecast horizons from one to twelve months show that adaptive combinations outperform individual models at short horizons, whereas RF forecasts dominate at medium and longer horizons. Beyond gains in forecast accuracy, the framework demonstrates how machine learning and robust optimization can jointly support more stable financial and business decisions under policy uncertainty and market stress. In particular, RF models capture complex nonlinear relationships, while distributionally robust optimization disciplines their use by controlling worst-case forecast losses. These benefits are most pronounced at short horizons, where tail risk and forecast instability are most costly, and during extreme events such as the COVID-19 shock and the post-2022 monetary tightening cycle.

Several limitations remain. Forecast performance depends on predictor availability and timeliness, as data publication lags and missing information can affect short-horizon forecasts in high-dimensional settings. In addition, while SHAP-based interpretability provides useful diagnostic insights, it does not identify causal drivers of yield curve movements. Finally, Root Mean Squared Forecast Error (RMSFE) may not fully capture performance differences across interest rate regimes or asymmetric loss considerations.

Future research may address these limitations by developing forecasting methods that explicitly account for publication delays and missing information, extending SHAP interpretability to dynamic and decision-dependent settings, and constructing distributionally robust confidence regions for yield curve forecasts. More broadly, the framework extends beyond Random Forests to alternative machine learning architectures, including deep learning models, where distributionally robust optimization can help stabilize highly flexible learners under distributional shifts. The framework also generalizes to other global, liquid asset classes beyond sovereign bonds and is applicable to portfolio management settings.

## References

* Lundberg and Lee (2017)

  Lundberg, S. M., and S.-I. Lee.
  2017.
  A unified approach to interpreting model predictions.
  Advances in Neural Information Processing Systems, 30, 4765–4774.
* Aiolfi and Timmermann (2006)

  Aiolfi, M., and A. Timmermann.
  2006.
  Persistence in forecasting performance and conditional combination strategies.
  Journal of Econometrics, 135 (1–2), 31–53.
* Albuquerque et al. (2022)

  Albuquerque, P. H. M., Y. Peng, and J. P. F. Silva.
  2022.
  Making the whole greater than the sum of its parts: A literature review of ensemble methods for financial time series forecasting.
  Journal of Forecasting, 41 (8), 1701–1724.
* Ang and Piazzesi (2003)

  Ang, A., and M. Piazzesi.
  2003.
  A no-arbitrage vector autoregression of term structure dynamics with macroeconomic and latent variables.
  Journal of Monetary Economics, 50 (4), 745–787.
* Bates and Granger (1969)

  Bates, J. M., and C. W. J. Granger.
  1969.
  The combination of forecasts.
  Operations Research Quarterly, 20 (4), 451–468.
* Botchkarev (2019)

  Botchkarev, A.
  2019.
  Performance metrics (error measures) in machine learning regression, forecasting and prognostics: Properties and typology.
  Interdisciplinary Journal of Information, Knowledge, and Management, 14, 45–79.
* Breiman (2001)

  Breiman, L.
  2001.
  Random forests.
  Machine Learning, 45 (1), 5–32.
* Caldeira et al. (2016)

  Caldeira, J., G. Clemente, and T. Rebbeck.
  2016.
  Forecast combination in the term structure of interest rates: Are machine learning and bagging able to improve.
  Journal of Forecasting, 35 (4), 323–340.
* Chi et al. (2022)

  Chi, C.-M., P. Vossler, Y. Fan, and J. Lv.
  2022.
  Asymptotic properties of high-dimensional random forests.
  arXiv preprint arXiv:2004.13953.
* Dickey and Fuller (1979)

  Dickey, D. A., and W. A. Fuller.
  1979.
  Distribution of the estimators for autoregressive time series with a unit root.
  Journal of the American Statistical Association, 74 (366), 427–431.
* Diebold and Li (2006)

  Diebold, F. X., and C. Li.
  2006.
  Forecasting the term structure of government bond yields.
  Journal of Econometrics, 130 (2), 337–364.
* Fernandes and Vieira (2019)

  Fernandes, C., and F. Vieira.
  2019.
  A dynamic Nelson–Siegel model with forward-looking macroeconomic factors for the yield curve in the U.S.
  Journal of Economic Dynamics and Control, 106, 103720.
* Granger and Jeon (2004)

  Granger, C. W. J., and Y. Jeon.
  2004.
  Thick modeling.
  Economic Modelling, 21 (2), 323–343.
* Healy and Jia (2023)

  Healy, C., and C. Jia.
  2023.
  Monetary policy since the onset of the COVID-19 pandemic: A path-dependent interpretation.
  Federal Reserve Bank of Cleveland Economic Commentary, 2023-12.
* Nelson and Siegel (1987)

  Nelson, C. R., and A. F. Siegel.
  1987.
  Parsimonious modeling of yield curves.
  Journal of Business, 60 (4), 473–489.
* Said and Dickey (1984)

  Said, S. E., and D. A. Dickey.
  1984.
  Testing for unit roots in autoregressive-moving average models of unknown order.
  Biometrika, 71 (3), 599–607.
* Scott (1992)

  Scott, D. W.
  1992.
  Multivariate Density Estimation: Theory, Practice, and Visualization.
  John Wiley & Sons, New York.
* Stock and Watson (2002)

  Stock, J. H., and M. W. Watson.
  2002.
  Forecasting using principal components from a large number of predictors.
  Journal of the American Statistical Association, 97 (460), 1167–1179.
* Swanson and Xiong (2018)

  Swanson, N. R., and W. Xiong.
  2018.
  Big data analytics in economics: What have we learned so far, and where should we go from here?
  Canadian Journal of Economics, 51 (3), 695–746.
* Wang et al. (2023)

  Wang, X., R. J. Hyndman, F. Li, and Y. Kang.
  2023.
  Forecast combinations: An over 50-year review.
  International Journal of Forecasting, 39, 1518–1547.
* Yang (2004)

  Yang, Y.
  2004.
  Combining forecasting procedures: Some theoretical results.
  Econometric Theory, 20 (1), 176–222.
* Zou and Yang (2004)

  Zou, H., and Y. Yang.
  2004.
  Combining time series models for forecasting.
  International Journal of Forecasting, 20 (1), 69–84.
* Brown et al. (1975)

  Brown, R. L., J. Durbin, and J. M. Evans.
  1975.
  Techniques for testing the constancy of regression relationships over time.
  Journal of the Royal Statistical Society: Series B (Methodological), 37 (2), 149–163.
* Truong et al. (2020)

  Truong, C., L. Oudre, and N. Vayatis.
  2020.
  Selective review of offline change point detection methods.
  Signal Processing, 167, 107299.
* Freund and Schapire (1997)

  Freund, Y., and R. E. Schapire.
  1997.
  A decision-theoretic generalization of on-line learning and an application to boosting.
  Journal of Computer and System Sciences, 55 (1), 119–139.
* Schapire (1990)

  Schapire, R. E.
  1990.
  The strength of weak learnability.
  Machine Learning, 5 (2), 197–227.
* Freund and Schapire (1996)

  Freund, Y., and R. E. Schapire.
  1996.
  Experiments with a new boosting algorithm.
  Proceedings of the Thirteenth International Conference on Machine Learning, 148–156.
* Freund and Schapire (1999)

  Freund, Y., and R. E. Schapire.
  1999.
  Large margin classification using the perceptron algorithm.
  Machine Learning, 37, 277–296.
* Bai and Ng (2006)

  Bai, J., and S. Ng.
  2006.
  Evaluating latent and observed factors in macroeconomics and finance.
  Journal of Econometrics, 131 (1–2), 507–537.
* Timmermann (2006)

  Timmermann, A.
  2006.
  Forecast combinations.
  Handbook of Economic Forecasting, 1, 135–196.
* Aiolfi and Timmermann (2006)

  Aiolfi, M., and A. Timmermann.
  2006.
  Persistence in forecasting performance and conditional combination strategies.
  Journal of Econometrics, 135 (1–2), 31–53.
* Bates and Granger (1969)

  Bates, J. M., and C. W. J. Granger.
  1969.
  The combination of forecasts.
  Operations Research Quarterly, 20 (4), 451–468.
* Granger and Jeon (2004)

  Granger, C. W. J., and Y. Jeon.
  2004.
  Thick modeling.
  Economic Modelling, 21 (2), 323–343.
* Lundberg and Lee (2017)

  Lundberg, S. M., and S.-I. Lee.
  2017.
  A unified approach to interpreting model predictions.
  Advances in Neural Information Processing Systems, 30, 4765–4774.
* Granger and Ramanathan (1984)

  Granger, C. W. J., and R. Ramanathan.
  1984.
  Improved methods of combining forecasts.
  Journal of Forecasting, 3 (2), 197–204.
* Wolpert (1992)

  Wolpert, D. H.
  1992.
  Stacked generalization.
  Neural Networks, 5 (2), 241–259.
* Breiman (1996)

  Breiman, L.
  1996.
  Stacked regressions.
  Machine Learning, 24 (1), 49–64.
* Jiang et al. (2025)

  Jiang, X., Y. Lv, Q. Li, and M.-Y. Cheng.
  2025.
  Robust model averaging prediction of longitudinal response with ultrahigh-dimensional covariates.
  Journal of the Royal Statistical Society: Series B (Statistical Methodology), 87 (2), 337–361.
* Cartea et al. (2025)

  Cartea, Á., L. Jin, and Z. Shi.
  2025.
  The limited virtue of complexity in a noisy world.
  University of Oxford and Imperial College London Working Paper.
* Janzing et al. (2020)

  Janzing, D., L. Minorics, and P. Blöbaum.
  2020.
  Feature relevance quantification in explainable AI: A causal problem.
  Proceedings of the 23rd International Conference on Artificial Intelligence and Statistics, 2907–2916.
* Delage and Ye (2010)

  Delage, E., and Y. Ye.
  2010.
  Distributionally robust optimization under moment uncertainty with application to data-driven problems.
  Operations Research, 58 (3), 595–612.
* Nguyen et al. (2020)

  Nguyen, V. A., F. Zhang, J. Blanchet, E. Delage, and Y. Ye.
  2020.
  Distributionally robust local non-parametric conditional estimation.
  arXiv preprint arXiv:2010.05373.
* Nguyen et al. (2024)

  Nguyen, V. A., F. Zhang, S. Wang, J. Blanchet, E. Delage, and Y. Ye.
  2024.
  Robustifying conditional portfolio decisions via optimal transport.
  Operations Research.

## Appendix A Appendix A: Tables and Figures

Table 1: RMSFE (bps) of Random Forest models across maturities and forecast horizons. Values in brackets report [min, max] across 10 runs.

| Maturity | H1 | H3 | H6 | H9 | H12 |
| --- | --- | --- | --- | --- | --- |
| 3M | 24.54 | 24.73 | 22.92 | 25.48 | 24.62 |
|  | [17.20, 32.40] | [19.94, 32.29] | [16.77, 30.53] | [15.26, 31.96] | [20.54, 32.71] |
| 6M | 24.15 | 23.62 | 25.17 | 25.45 | 24.49 |
|  | [19.48, 28.75] | [18.30, 29.71] | [21.21, 30.47] | [21.52, 29.22] | [21.90, 30.23] |
| 1Y | 22.22 | 21.80 | 22.35 | 21.26 | 22.16 |
|  | [14.20, 27.79] | [16.80, 28.06] | [16.46, 28.62] | [16.36, 28.72] | [16.29, 26.97] |
| 2Y | 18.26 | 17.93 | 18.37 | 18.24 | 19.67 |
|  | [14.34, 23.72] | [14.30, 20.20] | [14.18, 25.27] | [15.04, 27.58] | [16.82, 26.05] |
| 3Y | 17.09 | 17.13 | 16.58 | 16.92 | 17.45 |
|  | [12.69, 21.98] | [12.44, 21.78] | [12.62, 19.98] | [12.65, 22.75] | [14.60, 21.97] |
| 4Y | 16.76 | 15.61 | 15.96 | 16.55 | 15.49 |
|  | [14.19, 18.70] | [12.23, 19.11] | [13.36, 21.49] | [11.71, 20.03] | [12.33, 19.43] |
| 5Y | 17.16 | 17.45 | 15.97 | 15.27 | 16.04 |
|  | [12.19, 20.76] | [13.07, 20.70] | [11.36, 18.99] | [11.46, 17.12] | [12.32, 18.70] |
| 6Y | 17.51 | 17.53 | 17.60 | 18.52 | 17.89 |
|  | [15.29, 20.44] | [12.33, 20.83] | [13.86, 20.33] | [15.29, 21.50] | [15.22, 21.57] |
| 7Y | 15.87 | 16.56 | 16.98 | 16.27 | 16.53 |
|  | [13.28, 18.57] | [11.83, 20.60] | [13.33, 19.86] | [12.52, 19.27] | [13.70, 20.42] |
| 8Y | 14.13 | 14.11 | 14.21 | 14.69 | 14.60 |
|  | [12.00, 16.20] | [12.70, 15.60] | [11.84, 16.00] | [12.67, 18.15] | [11.31, 17.83] |
| 9Y | 15.08 | 16.48 | 14.89 | 14.79 | 14.27 |
|  | [11.83, 18.93] | [14.21, 17.92] | [12.80, 16.23] | [11.36, 18.40] | [11.76, 16.50] |
| 10Y | 15.37 | 15.10 | 16.18 | 15.00 | 15.00 |
|  | [13.42, 17.66] | [13.57, 17.22] | [14.82, 18.75] | [12.78, 18.06] | [12.42, 17.17] |
| 15Y | 13.65 | 13.27 | 13.25 | 13.09 | 12.73 |
|  | [11.51, 16.31] | [10.24, 16.03] | [11.50, 14.48] | [11.92, 14.70] | [9.53, 15.66] |
| 20Y | 13.01 | 13.41 | 12.82 | 13.02 | 12.96 |
|  | [10.68, 15.02] | [9.91, 16.16] | [10.62, 14.15] | [11.31, 14.87] | [12.10, 14.17] |
| 30Y | 13.41 | 13.99 | 13.21 | 13.02 | 12.87 |
|  | [10.85, 15.65] | [11.41, 16.39] | [10.39, 16.18] | [11.03, 16.40] | [11.02, 15.22] |




Table 2: RMSFE (bps) of the DNS model across maturities and forecast horizons.

| Maturity | H1 | H3 | H6 | H9 | H12 |
| --- | --- | --- | --- | --- | --- |
| 3M | 24.3 | 43.0 | 71.4 | 103.6 | 135.3 |
| 6M | 28.2 | 49.0 | 78.2 | 108.8 | 140.7 |
| 1Y | 34.1 | 55.8 | 83.4 | 112.1 | 143.5 |
| 2Y | 39.8 | 59.4 | 83.5 | 109.6 | 138.9 |
| 3Y | 41.3 | 59.6 | 82.2 | 106.6 | 133.3 |
| 4Y | 40.7 | 59.0 | 81.3 | 104.7 | 128.8 |
| 5Y | 38.7 | 58.1 | 81.2 | 104.0 | 126.0 |
| 6Y | 37.5 | 57.7 | 81.4 | 103.6 | 123.8 |
| 7Y | 37.0 | 57.8 | 81.8 | 103.5 | 122.2 |
| 8Y | 37.0 | 58.3 | 82.7 | 103.8 | 121.3 |
| 9Y | 37.7 | 59.3 | 83.9 | 104.6 | 120.9 |
| 10Y | 38.6 | 60.4 | 85.1 | 105.4 | 121.0 |
| 15Y | 43.5 | 65.6 | 90.0 | 108.6 | 121.3 |
| 20Y | 43.0 | 64.9 | 87.9 | 105.2 | 116.6 |
| 30Y | 35.9 | 54.0 | 71.0 | 84.5 | 94.8 |




Table 3: RMSFE (bps) of FADNS models across PCA dimensions: horizon h=1h=1 month.

| Maturity | PCA(1) | PCA(2) | PCA(3) | PCA(4) | PCA(5) | PCA(6) | PCA(7) | PCA(8) | PCA(9) | PCA(10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3M | 25.6 | 25.6 | 25.9 | 25.6 | 25.6 | 26.4 | 27.0 | 26.9 | 27.0 | 27.7 |
| 6M | 20.3 | 20.2 | 20.4 | 19.9 | 20.0 | 20.3 | 20.7 | 21.0 | 21.4 | 21.9 |
| 1Y | 23.2 | 23.1 | 23.0 | 22.4 | 22.6 | 22.1 | 22.0 | 22.6 | 22.8 | 23.0 |
| 2Y | 32.2 | 32.0 | 31.9 | 31.4 | 31.6 | 31.1 | 30.8 | 31.0 | 30.9 | 31.0 |
| 3Y | 35.7 | 35.6 | 35.5 | 35.1 | 35.2 | 35.1 | 35.0 | 35.0 | 34.8 | 34.9 |
| 4Y | 35.8 | 35.8 | 35.7 | 35.3 | 35.4 | 35.7 | 35.6 | 35.5 | 35.4 | 35.6 |
| 5Y | 33.3 | 33.3 | 33.3 | 32.9 | 33.0 | 33.6 | 33.6 | 33.5 | 33.5 | 33.7 |
| 6Y | 31.3 | 31.5 | 31.5 | 31.1 | 31.1 | 31.9 | 32.0 | 31.9 | 32.0 | 32.2 |
| 7Y | 30.0 | 30.2 | 30.3 | 29.9 | 29.8 | 30.7 | 30.9 | 31.0 | 31.1 | 31.3 |
| 8Y | 29.3 | 29.5 | 29.7 | 29.2 | 29.1 | 30.1 | 30.3 | 30.4 | 30.6 | 30.8 |
| 9Y | 29.3 | 29.4 | 29.6 | 29.1 | 29.0 | 29.9 | 30.1 | 30.4 | 30.6 | 30.7 |
| 10Y | 29.6 | 29.7 | 29.9 | 29.5 | 29.3 | 30.0 | 30.3 | 30.7 | 30.9 | 31.0 |
| 15Y | 33.8 | 33.5 | 33.9 | 33.6 | 33.3 | 33.1 | 33.5 | 34.1 | 34.4 | 34.4 |
| 20Y | 31.1 | 30.8 | 31.3 | 31.2 | 31.0 | 30.7 | 31.2 | 31.7 | 31.9 | 31.9 |
| 30Y | 28.6 | 29.0 | 29.4 | 29.7 | 29.8 | 30.7 | 31.2 | 31.0 | 30.1 | 30.4 |




Table 4: RMSFE (bps) of FADNS models across PCA dimensions: horizon h=3h=3 months.

| Maturity | PCA(1) | PCA(2) | PCA(3) | PCA(4) | PCA(5) | PCA(6) | PCA(7) | PCA(8) | PCA(9) | PCA(10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3M | 45.2 | 44.6 | 45.1 | 43.4 | 44.0 | 45.6 | 46.3 | 45.5 | 45.3 | 45.9 |
| 6M | 46.6 | 45.9 | 46.3 | 43.8 | 44.4 | 44.7 | 45.3 | 44.7 | 44.4 | 44.8 |
| 1Y | 53.6 | 53.0 | 53.2 | 50.4 | 50.8 | 50.2 | 50.5 | 50.0 | 49.1 | 49.5 |
| 2Y | 64.8 | 64.5 | 64.7 | 62.0 | 62.3 | 62.4 | 62.5 | 61.3 | 60.0 | 60.4 |
| 3Y | 68.4 | 68.4 | 68.5 | 65.9 | 66.2 | 67.1 | 67.4 | 65.8 | 64.5 | 64.9 |
| 4Y | 68.6 | 68.7 | 68.8 | 66.4 | 66.6 | 68.1 | 68.6 | 66.8 | 65.5 | 66.1 |
| 5Y | 66.8 | 67.1 | 67.3 | 64.8 | 65.0 | 66.8 | 67.5 | 65.8 | 64.6 | 65.2 |
| 6Y | 65.5 | 65.9 | 66.1 | 63.7 | 63.9 | 65.8 | 66.6 | 65.1 | 64.0 | 64.5 |
| 7Y | 64.7 | 65.0 | 65.3 | 63.0 | 63.3 | 65.1 | 66.0 | 64.7 | 63.7 | 64.3 |
| 8Y | 64.1 | 64.5 | 64.8 | 62.6 | 62.9 | 64.6 | 65.6 | 64.6 | 63.7 | 64.2 |
| 9Y | 64.0 | 64.3 | 64.7 | 62.5 | 62.9 | 64.4 | 65.5 | 64.7 | 63.9 | 64.5 |
| 10Y | 64.0 | 64.2 | 64.7 | 62.6 | 63.1 | 64.3 | 65.4 | 64.9 | 64.2 | 64.7 |
| 15Y | 65.4 | 65.2 | 65.7 | 64.3 | 65.4 | 65.3 | 66.7 | 66.7 | 66.3 | 66.8 |
| 20Y | 61.7 | 61.4 | 62.0 | 61.4 | 63.2 | 63.1 | 64.7 | 64.3 | 63.6 | 64.1 |
| 30Y | 53.2 | 53.6 | 54.6 | 55.6 | 58.5 | 60.9 | 62.4 | 60.6 | 57.9 | 58.6 |




Table 5: RMSFE (bps) of FADNS models across PCA dimensions: horizon h=6h=6 months.

| Maturity | PCA(1) | PCA(2) | PCA(3) | PCA(4) | PCA(5) | PCA(6) | PCA(7) | PCA(8) | PCA(9) | PCA(10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3M | 95.0 | 94.1 | 94.5 | 90.0 | 90.7 | 94.5 | 95.0 | 89.6 | 89.3 | 90.6 |
| 6M | 96.7 | 96.0 | 96.1 | 91.3 | 92.2 | 95.2 | 95.5 | 90.6 | 90.1 | 91.5 |
| 1Y | 103.7 | 103.6 | 103.6 | 98.7 | 99.5 | 102.2 | 102.2 | 97.4 | 96.8 | 98.4 |
| 2Y | 110.5 | 110.9 | 110.9 | 106.5 | 107.2 | 110.9 | 110.8 | 105.4 | 104.7 | 106.5 |
| 3Y | 110.2 | 111.1 | 111.3 | 106.9 | 107.4 | 112.1 | 112.2 | 106.5 | 106.1 | 107.9 |
| 4Y | 108.4 | 109.5 | 109.9 | 105.5 | 105.8 | 110.7 | 111.0 | 105.5 | 105.4 | 107.4 |
| 5Y | 105.8 | 107.1 | 107.8 | 103.1 | 103.3 | 108.0 | 108.6 | 103.7 | 103.8 | 105.8 |
| 6Y | 103.9 | 105.3 | 106.3 | 101.3 | 101.3 | 105.6 | 106.5 | 102.1 | 102.5 | 104.6 |
| 7Y | 102.5 | 103.9 | 105.1 | 100.0 | 99.8 | 103.6 | 104.8 | 101.0 | 101.7 | 103.8 |
| 8Y | 101.6 | 103.0 | 104.4 | 99.0 | 98.8 | 102.0 | 103.5 | 100.3 | 101.2 | 103.3 |
| 9Y | 101.2 | 102.5 | 103.9 | 98.5 | 98.2 | 100.7 | 102.5 | 99.9 | 101.1 | 103.1 |
| 10Y | 100.8 | 102.0 | 103.6 | 98.1 | 97.8 | 99.5 | 101.7 | 99.5 | 100.9 | 102.9 |
| 15Y | 100.8 | 101.4 | 103.2 | 97.7 | 97.9 | 97.0 | 100.4 | 99.4 | 101.1 | 102.8 |
| 20Y | 95.3 | 95.6 | 97.4 | 92.7 | 93.6 | 92.7 | 97.1 | 95.1 | 96.4 | 97.6 |
| 30Y | 82.4 | 82.6 | 84.6 | 83.1 | 84.5 | 88.9 | 93.2 | 87.4 | 85.7 | 86.0 |




Table 6: RMSFE (bps) of FADNS models across PCA dimensions: horizon h=9h=9 months.

| Maturity | PCA(1) | PCA(2) | PCA(3) | PCA(4) | PCA(5) | PCA(6) | PCA(7) | PCA(8) | PCA(9) | PCA(10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3M | 166.2 | 166.3 | 165.8 | 158.3 | 159.2 | 167.4 | 167.2 | 156.1 | 157.7 | 160.7 |
| 6M | 167.1 | 167.7 | 167.1 | 159.7 | 160.7 | 168.6 | 168.1 | 158.0 | 159.6 | 162.9 |
| 1Y | 167.9 | 169.3 | 168.6 | 161.5 | 162.6 | 170.4 | 169.7 | 159.9 | 161.6 | 165.0 |
| 2Y | 167.9 | 170.3 | 169.7 | 163.3 | 164.0 | 172.8 | 172.0 | 161.8 | 163.9 | 167.4 |
| 3Y | 164.2 | 167.1 | 166.8 | 160.7 | 160.9 | 170.1 | 169.2 | 159.4 | 162.0 | 165.5 |
| 4Y | 159.5 | 162.8 | 162.8 | 156.7 | 156.5 | 165.4 | 164.5 | 155.5 | 158.5 | 161.9 |
| 5Y | 154.7 | 158.2 | 158.5 | 152.2 | 151.5 | 159.8 | 158.8 | 151.0 | 154.5 | 158.0 |
| 6Y | 150.9 | 154.4 | 155.0 | 148.4 | 147.4 | 154.6 | 153.7 | 147.1 | 151.0 | 154.4 |
| 7Y | 147.8 | 151.4 | 152.2 | 145.2 | 143.9 | 150.1 | 149.2 | 143.8 | 148.0 | 151.4 |
| 8Y | 145.5 | 149.0 | 149.9 | 142.6 | 141.0 | 146.0 | 145.3 | 141.0 | 145.5 | 148.9 |
| 9Y | 143.9 | 147.2 | 148.3 | 140.6 | 138.8 | 142.6 | 141.9 | 138.8 | 143.6 | 146.9 |
| 10Y | 142.7 | 145.8 | 146.8 | 138.8 | 136.9 | 139.6 | 139.1 | 136.9 | 141.9 | 145.1 |
| 15Y | 138.9 | 141.0 | 141.7 | 132.5 | 130.4 | 129.0 | 129.7 | 130.0 | 135.4 | 138.1 |
| 20Y | 130.4 | 131.6 | 131.9 | 122.3 | 120.2 | 118.6 | 120.7 | 120.2 | 125.2 | 127.2 |
| 30Y | 110.2 | 110.3 | 110.0 | 103.0 | 100.3 | 106.2 | 109.6 | 102.7 | 104.6 | 104.9 |




Table 7: RMSFE (bps) of FADNS models across PCA dimensions: horizon h=12h=12 months.

| Maturity | PCA(1) | PCA(2) | PCA(3) | PCA(4) | PCA(5) | PCA(6) | PCA(7) | PCA(8) | PCA(9) | PCA(10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3M | 255.7 | 257.6 | 255.9 | 245.3 | 246.6 | 261.7 | 259.6 | 239.7 | 244.1 | 249.4 |
| 6M | 257.6 | 260.3 | 258.6 | 248.2 | 249.4 | 264.1 | 261.8 | 243.0 | 247.5 | 252.7 |
| 1Y | 257.1 | 260.7 | 259.2 | 249.4 | 250.5 | 264.7 | 262.4 | 244.1 | 248.7 | 254.1 |
| 2Y | 248.2 | 252.9 | 251.8 | 242.9 | 243.3 | 257.6 | 255.5 | 237.2 | 242.0 | 247.2 |
| 3Y | 236.5 | 241.8 | 241.1 | 232.5 | 232.2 | 246.3 | 244.1 | 226.8 | 231.9 | 236.7 |
| 4Y | 225.4 | 230.9 | 230.4 | 221.9 | 220.8 | 234.4 | 232.2 | 216.2 | 221.5 | 226.2 |
| 5Y | 214.7 | 220.2 | 219.9 | 211.1 | 209.4 | 221.9 | 219.7 | 205.6 | 211.3 | 215.8 |
| 6Y | 206.4 | 211.7 | 211.4 | 202.3 | 200.0 | 211.2 | 208.9 | 196.8 | 202.9 | 207.3 |
| 7Y | 200.0 | 205.0 | 204.6 | 194.9 | 192.2 | 202.0 | 199.9 | 189.5 | 195.9 | 200.2 |
| 8Y | 195.0 | 199.6 | 199.1 | 188.8 | 185.6 | 194.0 | 191.9 | 183.4 | 190.0 | 194.3 |
| 9Y | 191.3 | 195.4 | 194.6 | 183.7 | 180.2 | 187.1 | 185.2 | 178.3 | 185.2 | 189.4 |
| 10Y | 188.9 | 192.4 | 191.3 | 179.8 | 176.1 | 181.5 | 179.8 | 174.4 | 181.5 | 185.7 |
| 15Y | 181.6 | 182.8 | 179.7 | 165.7 | 161.8 | 161.9 | 161.4 | 160.8 | 168.3 | 172.2 |
| 20Y | 172.6 | 172.5 | 167.3 | 152.1 | 148.4 | 148.0 | 148.9 | 148.5 | 155.7 | 159.2 |
| 30Y | 149.5 | 149.4 | 141.3 | 128.8 | 124.9 | 132.7 | 135.1 | 127.9 | 132.4 | 134.95 |




Table 8: Best PCA dimension across forecast horizons by maturity (FADNS).

| Maturity | H1 | H3 | H6 | H9 | H12 |
| --- | --- | --- | --- | --- | --- |
| 3M | PCA(1) | PCA(4) | PCA(9) | PCA(8) | PCA(8) |
| 6M | PCA(4) | PCA(4) | PCA(9) | PCA(8) | PCA(8) |
| 1Y | PCA(7) | PCA(9) | PCA(9) | PCA(8) | PCA(8) |
| 2Y | PCA(7) | PCA(9) | PCA(9) | PCA(8) | PCA(8) |
| 3Y | PCA(9) | PCA(9) | PCA(9) | PCA(8) | PCA(8) |
| 4Y | PCA(4) | PCA(9) | PCA(9) | PCA(8) | PCA(8) |
| 5Y | PCA(4) | PCA(9) | PCA(4) | PCA(8) | PCA(8) |
| 6Y | PCA(4) | PCA(4) | PCA(5) | PCA(8) | PCA(8) |
| 7Y | PCA(5) | PCA(4) | PCA(5) | PCA(8) | PCA(8) |
| 8Y | PCA(5) | PCA(4) | PCA(5) | PCA(8) | PCA(8) |
| 9Y | PCA(5) | PCA(4) | PCA(5) | PCA(8) | PCA(8) |
| 10Y | PCA(5) | PCA(4) | PCA(5) | PCA(8) | PCA(8) |
| 15Y | PCA(6) | PCA(4) | PCA(6) | PCA(6) | PCA(8) |
| 20Y | PCA(6) | PCA(4) | PCA(4) | PCA(6) | PCA(6) |
| 30Y | PCA(1) | PCA(1) | PCA(1) | PCA(5) | PCA(5) |




Table 9: RMSFE (bps) of forecast combination methods (10 FADNS + 10 RF), horizon h=1h=1 month.

| Maturity | FC-EW | FC-RANK | FC-RMSE | FC-MSE | FC-OLS | FC-MV | FC-STACK | FC-LAD | AFTER (Roll.) | AFTER (EWMA) | AFTER (Simp.) | FC-DRO-ES | FC-DRO-MIX | FC-DRMV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3M | 21.55 | 21.51 | 22.03 | 23.71 | 24.54 | 24.22 | 21.93 | 22.23 | 26.93 | 28.75 | 22.84 | 23.19 | 21.18 | 21.50 |
| 6M | 15.85 | 18.92 | 16.36 | 23.39 | 22.64 | 18.06 | 20.10 | 21.30 | 18.26 | 18.98 | 17.61 | 18.20 | 15.74 | 17.01 |
| 1Y | 11.46 | 15.15 | 12.52 | 19.85 | 23.03 | 15.44 | 14.24 | 14.82 | 16.84 | 19.36 | 13.29 | 16.08 | 11.20 | 12.14 |
| 2Y | 12.79 | 11.41 | 11.14 | 16.90 | 15.86 | 23.99 | 10.74 | 10.39 | 21.48 | 24.56 | 10.42 | 15.29 | 13.85 | 9.62 |
| 3Y | 15.52 | 10.94 | 12.18 | 16.54 | 15.30 | 28.12 | 11.01 | 10.77 | 23.49 | 24.49 | 10.92 | 13.57 | 17.41 | 10.40 |
| 4Y | 15.42 | 11.02 | 11.67 | 15.83 | 15.03 | 25.82 | 10.23 | 10.15 | 25.17 | 27.06 | 10.28 | 13.34 | 17.73 | 10.31 |
| 5Y | 14.92 | 11.24 | 12.39 | 17.52 | 14.91 | 23.92 | 10.69 | 10.98 | 22.61 | 23.51 | 11.40 | 13.35 | 16.35 | 11.19 |
| 6Y | 14.79 | 12.70 | 13.36 | 17.68 | 16.51 | 23.00 | 13.05 | 14.02 | 23.07 | 23.16 | 12.68 | 14.51 | 15.68 | 12.43 |
| 7Y | 13.42 | 10.19 | 11.39 | 13.43 | 15.41 | 21.04 | 10.33 | 11.21 | 20.07 | 17.88 | 11.21 | 12.43 | 14.46 | 10.61 |
| 8Y | 12.95 | 9.44 | 9.73 | 15.68 | 13.58 | 19.66 | 9.83 | 8.44 | 18.00 | 16.89 | 10.25 | 10.70 | 14.22 | 9.18 |
| 9Y | 12.51 | 9.36 | 9.85 | 14.16 | 13.31 | 19.16 | 10.40 | 9.74 | 17.26 | 16.73 | 10.54 | 11.36 | 13.69 | 9.63 |
| 10Y | 13.11 | 10.40 | 10.62 | 16.42 | 13.50 | 18.78 | 11.70 | 11.62 | 18.45 | 16.16 | 11.26 | 11.79 | 14.25 | 10.41 |
| 15Y | 14.67 | 9.57 | 10.34 | 14.14 | 12.76 | 20.92 | 11.00 | 12.11 | 16.50 | 14.76 | 10.47 | 10.75 | 16.87 | 9.72 |
| 20Y | 13.12 | 8.38 | 8.94 | 13.46 | 12.29 | 20.87 | 9.41 | 10.12 | 12.73 | 13.41 | 9.88 | 10.11 | 14.78 | 9.25 |
| 30Y | 13.39 | 9.40 | 10.03 | 12.96 | 11.86 | 19.39 | 10.54 | 11.19 | 14.77 | 14.54 | 10.86 | 11.04 | 14.46 | 9.97 |




Table 10: RMSFE (bps) of forecast combination methods (10 RF only), horizon h=1h=1 month.

| Maturity | FC-EW | FC-RANK | FC-RMSE | FC-MSE | FC-OLS | FC-MV | FC-STACK | FC-LAD | AFTER (Roll.) | AFTER (EWMA) | AFTER (Simp.) | FC-DRO-ES | FC-DRO-MIX | FC-DRMV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3M | 23.41 | 22.03 | 22.82 | 23.07 | 21.20 | 22.13 | 21.81 | 21.91 | 23.40 | 23.30 | 22.45 | 21.96 | 23.67 | 21.38 |
| 6M | 22.93 | 21.85 | 22.82 | 21.25 | 22.45 | 22.31 | 21.59 | 23.77 | 22.75 | 22.74 | 22.60 | 22.62 | 23.01 | 22.13 |
| 1Y | 21.46 | 20.19 | 21.10 | 19.86 | 18.64 | 19.59 | 19.51 | 20.77 | 21.32 | 20.26 | 20.92 | 20.53 | 21.57 | 20.15 |
| 2Y | 18.20 | 17.55 | 17.99 | 17.88 | 17.01 | 17.81 | 17.34 | 16.99 | 17.98 | 17.95 | 18.08 | 18.02 | 18.24 | 17.60 |
| 3Y | 17.91 | 16.98 | 17.56 | 18.34 | 16.82 | 17.35 | 16.67 | 17.35 | 17.36 | 18.50 | 17.72 | 17.28 | 17.96 | 17.03 |
| 4Y | 18.44 | 18.31 | 18.43 | 18.59 | 18.31 | 18.90 | 18.92 | 18.34 | 18.17 | 18.73 | 18.42 | 18.49 | 18.45 | 18.57 |
| 5Y | 19.55 | 19.06 | 19.30 | 20.71 | 18.33 | 18.37 | 19.19 | 18.19 | 18.92 | 19.40 | 19.43 | 19.32 | 19.58 | 19.10 |
| 6Y | 20.75 | 20.73 | 20.72 | 21.47 | 20.83 | 20.45 | 21.35 | 22.36 | 20.86 | 20.80 | 20.76 | 20.85 | 20.75 | 20.74 |
| 7Y | 20.37 | 19.91 | 20.25 | 19.42 | 20.40 | 19.80 | 19.33 | 19.73 | 20.22 | 20.04 | 20.31 | 20.14 | 20.39 | 20.01 |
| 8Y | 19.84 | 20.05 | 19.85 | 21.62 | 20.89 | 19.78 | 20.04 | 20.98 | 20.05 | 20.65 | 19.86 | 19.93 | 19.84 | 19.79 |
| 9Y | 21.14 | 20.96 | 21.06 | 21.32 | 21.16 | 20.94 | 21.16 | 21.39 | 21.59 | 20.57 | 21.12 | 21.09 | 21.15 | 20.96 |
| 10Y | 22.10 | 22.12 | 22.07 | 23.31 | 22.38 | 22.32 | 22.64 | 22.17 | 22.08 | 22.64 | 22.08 | 22.11 | 22.11 | 22.00 |
| 15Y | 23.12 | 23.41 | 23.21 | 23.98 | 23.98 | 23.23 | 23.65 | 23.87 | 23.26 | 22.67 | 23.12 | 23.21 | 23.12 | 23.16 |
| 20Y | 23.92 | 23.85 | 23.88 | 24.50 | 23.56 | 23.69 | 24.02 | 24.21 | 23.82 | 23.93 | 23.91 | 23.90 | 23.92 | 23.88 |
| 30Y | 25.05 | 24.84 | 24.98 | 25.20 | 24.79 | 25.03 | 24.96 | 24.97 | 24.88 | 25.17 | 25.02 | 25.01 | 25.05 | 24.98 |




Figure 1: Comparing U.S. benchmark Treasury yield forecasts with additional Treasury supply variables (TIC).

![Refer to caption](RMSE_heatmap_improvement.png)



Figure 2: Maturity-averaged global SHAP values for the Random Forest model across forecast horizons.

![Refer to caption](GLOBAL_SHAP_COMBINED.png)



Figure 3: One-month-ahead forecast error dynamics of hybrid RF–FADNS forecast combinations across U.S. Treasury maturities.

![Refer to caption](HYBRID_ERROR_h1_ALL_TENORS_3x5.png)



Figure 4: Weight dynamics under distributionally robust mean–variance (DRMV) forecast combination.

![Refer to caption](FC-DRMV_h1_ALL_TENORS_RF_vs_FADNS_WEIGHTS_3x5.png)



Figure 5: Weight dynamics under distributionally robust expected shortfall (DRO–ES) forecast combination.

![Refer to caption](FC-DRO-ES_h1_ALL_TENORS_RF_vs_FADNS_WEIGHTS_3x5.png)



Figure 6: Weight dynamics under hybrid distributionally robust (DRO–MIX) forecast combination.

![Refer to caption](FC-DRO-MIX_h1_ALL_TENORS_RF_vs_FADNS_WEIGHTS_3x5.png)

## E-Companion

### OA.1 Additional Tables

Table OA.1: Categorized List of U.S. Macroeconomic and Financial Indicators

Category


Indicators




Prices and Inflation


Consumer Price Index (All Items), CPI Excluding Food and Energy, Producer Price Index (Final Demand), Personal Consumption Expenditures Price Index, Core PCE Price Index, Import Price Index, Export Price Index, GDP Implicit Price Deflator, Chain-Type Price Index of GDP



Labor Markets


Unemployment Rate, Unemployed Persons (16 Years and Over), Nonfarm Payroll Employment (Total Private), Nonfarm Payroll Employment (Manufacturing), Average Hourly Earnings (Total Private), Employment Cost Index (Civilian Workers), Average Weekly Hours (Total Private), Payroll Employment Diffusion Index, Initial Jobless Claims (4-Week Average), Unit Labor Costs (Business Sector), Unit Labor Costs (Nonfarm Business Sector), Output per Hour (Business Sector), Output per Hour (Nonfarm Business Sector), Business Bankruptcy Filings



Real Activity


Real Gross Domestic Product, Real Gross National Product, Industrial Production Index, Capacity Utilization Rate, Business Sales (Manufacturing and Trade), Private Domestic Fixed Investment, Factory Orders, Durable Goods Orders, Business Inventories, Inventory-to-Sales Ratios (Total Business, Manufacturing, Wholesale, Retail), Corporate Profits (with IVA and CCAdj)



Business Conditions and Surveys


ISM Manufacturing Index, ISM Non-Manufacturing Index, ISM Prices Paid Index, Chicago Purchasing Managers Index, Philadelphia Fed Manufacturing Business Outlook Survey, Empire State Manufacturing Survey, TIPP Economic Optimism Index



Leading Indicators


Conference Board Leading Economic Indicators Index, Conference Board Leading Economic Indicators (YoY), Conference Board Leading Economic Indicators (MoM), Chicago Fed National Activity Index, Chicago Fed National Activity Index (3-Month Average)



Household and Personal Sector


Personal Income, Disposable Personal Income, Real Personal Income Excluding Transfers, Personal Consumption Expenditures, Real Personal Consumption Expenditures, Personal Saving Rate, Consumer Credit Outstanding, Consumer Confidence Index (Conference Board), University of Michigan Consumer Sentiment Index



Housing Market


Housing Starts, Building Permits, New Home Sales, Existing Home Sales, NAHB Housing Market Index, FHFA House Price Index, Mortgage Delinquency Rate



External Sector


Exports of Goods and Services, Imports of Goods and Services, Trade Balance, Current Account Balance, Capital and Financial Account Balance, Real Effective Exchange Rate (BIS), Nominal Effective Exchange Rate



Financial Conditions and Interest Rates


Federal Funds Target Rate, Treasury Bill Rate (3-Month), Prime Rate Charged by Banks, Interbank Rate (3-Month, London), Monetary Base, Money Supply M1, Money Supply M2



Treasury Supply and Capital Flows


Total Public Debt Outstanding, Marketable Treasury Debt Outstanding, Non-Marketable Treasury Debt Outstanding, Treasury Bills Outstanding, Treasury Notes Outstanding, Treasury Bonds Outstanding, Treasury Inflation-Protected Securities Outstanding, Net Long-Term TIC Flows, Total Net TIC Flows, Government Budget Balance, Government Budget Balance as Percentage of GDP




Table OA.2: (Categorized List of U.K. Macroeconomic and Financial Indicators

Category


Indicators




Prices and Inflation


Consumer Price Index (All Items), Retail Price Index, GDP Implicit Price Deflator (Market Prices), Producer Price Index (Output), Producer Price Index (Input), Import Price Index, Export Price Index



Labor Markets


Unemployment Rate, Workforce Jobs (Total), Claimant Count, Average Weekly Earnings (Total Pay), Average Weekly Earnings (Regular Pay), Unit Labour Cost Index (Whole Economy), Productivity (Whole Economy)



Real Activity


Real Gross Domestic Product, Industrial Production Index, Manufacturing Output Index, Capacity Utilization (Manufacturing), New Orders Obtained (Total), Gross Operating Surplus of Corporations



Business Conditions and Surveys


Purchasing Managers’ Index (Manufacturing), Purchasing Managers’ Index (Services), Deloitte UK CFO Survey: Business Prospects, Deloitte UK CFO Survey: Financial Conditions



Leading Indicators


U.K. Composite Leading Indicator (Trend Restored), U.K. Composite Leading Indicator (Month-on-Month Change)



Household and Personal Sector


Household Disposable Income, Household Saving Ratio, Household Final Consumption Expenditure, Consumer Credit Outstanding



Housing Market


House Price Index, Mortgage Approvals, Mortgage Lending to Households



External Sector


Exports of Goods and Services, Imports of Goods and Services, Trade Balance (Goods and Services), Current Account Balance, Financial and Capital Account Balance, Gross External Debt



Financial Conditions and Interest Rates


Bank Rate (Policy Rate), Interbank Rate (3-Month), Government Bond Yield (10-Year), Monetary Aggregate M4, Government Gross Reserve Assets



Treasury Supply and Capital Flows


Public Sector Net Debt, Public Sector Net Borrowing, General Government External Liabilities, Government Budget Balance, Government Budget Balance as Percentage of GDP




Table OA.3: Categorized List of Malaysian Macroeconomic and Financial Indicators

Category


Indicators




Prices and Inflation


Consumer Price Index, GDP Implicit Price Deflator, Import Unit Value Index, Terms of Trade



Labor Markets


Job Vacancies, Capacity Utilization Rate (Manufacturing)



Real Activity


Industrial Production Index, Retail Sales, Retail Trade Index, Gross National Income, Change in Stocks



Business Conditions and Surveys


Business Conditions Index, Consumer Sentiment Index



Leading Indicators


Leading Index



Household and Personal Sector


Retail Sales, New Vehicles Registered, Housing Approvals



Housing Market


House Price Index, Housing Approvals



External Sector


Exports of Goods (FOB), Imports of Goods (CIF), Goods Trade Balance, Current Account Balance, Capital and Financial Account Balance, Gross External Debt



Financial Conditions and Interest Rates


Overnight Policy Rate (Bank Negara Malaysia), Interbank Rate (3-Month), Treasury Bill Discount Rate (3-Month), Lending Rate, Base Lending Rate, Government Bond Yield (10-Year), Money Supply (M0, M1, M2, M3), Domestic Credit to Private Sector, Bank Loans (Total)



Treasury Supply and Capital Flows


Federal Government Budget Balance, Gross International Reserves, Gross International Reserves (U.S. Dollars), Malaysian Ringgit per U.S. Dollar (Market Rate)




Table OA.4: Categorized List of Japanese Macroeconomic and Financial Indicators

Category


Indicators




Prices and Inflation


Consumer Price Index (All Items), Core Consumer Price Index (Excluding Fresh Food), GDP Implicit Price Deflator



Labor Markets


Unemployment Rate, Job Offers-to-Applicants Ratio, Total Employment, Average Monthly Cash Earnings, Labour Productivity



Real Activity


Real Gross Domestic Product, Industrial Production Index, Tertiary Industry Activity Index, Changes in Inventories, Corporate Ordinary Profits (All Industries Excluding Finance and Insurance)



Business Conditions and Surveys


Tankan Large Manufacturers Index, Tankan Large Non-Manufacturers Index, Economy Watchers Survey (Current Conditions), Economy Watchers Survey (Outlook)



Leading Indicators


Leading Composite Index, Leading Diffusion Index, Coincident Composite Index, Coincident Diffusion Index, Lagging Composite Index



Household and Personal Sector


Workers’ Household Living Expenditure, Household Consumption Expenditure, Consumer Confidence Index



Housing Market


Housing Starts, Residential Construction Orders



External Sector


Exports of Goods and Services, Imports of Goods and Services, Trade Balance, Gross External Debt, General Government External Debt



Financial Conditions and Interest Rates


Policy Interest Rate (Bank of Japan), Call Rate (Overnight), Interbank Rate (3-Month), Government Bond Yield (10-Year), Money Supply (M1, M2, M3)



Treasury Supply and Capital Flows


Central Government Budget Balance, Gold and Foreign Exchange Reserves




Table OA.5: (Categorized List of German Macroeconomic and Financial Indicators

Category


Indicators




Prices and Inflation


Consumer Price Index, Harmonized Index of Consumer Prices, GDP Implicit Price Deflator, Unit Labour Cost per Unit of Turnover



Labor Markets


Unemployment Rate, Total Employment, Population, Lending to Domestic Enterprises and Households



Real Activity


Real Gross Domestic Product, Industrial Production Index, Manufacturing Capacity Utilization, Retail Sales



Business Conditions and Surveys


IFO Business Climate Index, IFO Business Expectations Index, Consumer Confidence Indicator



Leading Indicators


Composite Leading Indicator (Trend Restored)



Household and Personal Sector


Private Consumption Expenditure, Retail Sales



Housing Market


Residential Construction Orders, Building Permits



External Sector


Exports of Goods and Services, Imports of Goods and Services, Gross External Debt, General Government Gross External Debt



Financial Conditions and Interest Rates


Policy Interest Rate (ECB), Interbank Rate (3-Month), Government Bond Yield (10-Year), Money Supply (M0, M1, M2)



Treasury Supply and Capital Flows


General Government Budget Balance, Public Debt (Total), German Contribution to Euro Area Monetary Aggregates




Table OA.6: Categorized List of Canadian Macroeconomic and Financial Indicators

Category


Indicators




Prices and Inflation


Consumer Price Index, GDP Implicit Price Deflator, Unit Labour Cost (Business Sector)



Labor Markets


Job Vacancies, Compensation per Hour Worked (Business Sector), Labour Productivity (Business Sector), Population



Real Activity


Real Gross Domestic Product (All Industries), Industrial Production, Manufacturing Output, Capacity Utilization Rate (All Industries), Corporate Net Profits (All Industries)



Business Conditions and Surveys


Ivey Purchasing Managers Index



Leading Indicators


Composite Leading Indicator



Household and Personal Sector


Household Disposable Income



Housing Market


Housing Starts, Residential Building Permits



External Sector


Exports of Goods and Services, Imports of Goods and Services, Current Account Balance, Gross External Debt, General Government External Debt



Financial Conditions and Interest Rates


Policy Interest Rate (Bank of Canada), Overnight Money Market Financing Rate, Treasury Bill Rate (3-Month), Chartered Banks Prime Rate, Government Bond Yield (10-Year), Money Supply (Monetary Base, M1+, M2, M3), S&P/TSX Composite Index



Treasury Supply and Capital Flows


Official International Reserves, Canadian Dollar per U.S. Dollar (Market Rate), Real Effective Exchange Rate (CEER)




Table OA.7: (EC.1.7) Categorized List of Chinese Macroeconomic and Financial Indicators

Category


Indicators




Prices and Inflation


Consumer Price Index, Core Consumer Price Index, Producer Price Index, Export Price Index, Terms of Trade Index



Labor Markets


Job Vacancies (Urban Areas)



Real Activity


Gross Domestic Product, Industrial Production Index, Industrial Value Added, Industrial Profits, Fixed Asset Investment (Urban Areas)



Business Conditions and Surveys


Macroeconomic Climate Index (Leading), Macroeconomic Climate Index (Coincident), Macroeconomic Climate Index (Lagging), Consumer Confidence Index



Leading Indicators


Macroeconomic Climate Index (Leading)



Household and Personal Sector


Per Capita Disposable Income (Urban Households), Household Consumption Loans (Financial Institutions)



Housing Market


Fixed Asset Investment (Urban Areas)



External Sector


Exports, Imports, Trade Balance, Gross External Debt (Total), Gross External Debt (Government), Foreign Currency Reserves



Financial Conditions and Interest Rates


Major Loan Rate (1-Year and Below), Money Supply (Currency in Circulation, M1, M2), Shanghai Stock Exchange Composite Index, Chinese Yuan per U.S. Dollar (Market Rate)



Treasury Supply and Capital Flows


Central Government Budget Balance, Total Central Government Debt




Table OA.8: RMSFE (bps) of multi-output Random Forest forecasts for U.S. Treasury yields.

| Seed | Horizon | 3M | 6M | 1Y | 2Y | 3Y | 5Y | 7Y | 10Y | 30Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8270 | 1 | 31.15 | 34.04 | 32.72 | 29.94 | 28.34 | 24.20 | 22.74 | 20.78 | 17.55 |
| 8270 | 3 | 29.75 | 32.19 | 31.20 | 28.93 | 27.47 | 23.33 | 22.34 | 20.50 | 17.30 |
| 8270 | 6 | 34.39 | 36.18 | 33.89 | 29.58 | 27.34 | 22.62 | 20.06 | 18.86 | 16.14 |
| 8270 | 9 | 32.95 | 34.46 | 32.79 | 29.94 | 27.56 | 22.38 | 20.17 | 18.63 | 16.17 |
| 8270 | 12 | 32.80 | 34.50 | 32.43 | 30.47 | 27.97 | 23.46 | 21.51 | 19.74 | 16.82 |
| 1860 | 1 | 35.21 | 36.74 | 35.48 | 31.79 | 30.09 | 25.49 | 22.86 | 20.99 | 17.83 |
| 1860 | 3 | 32.85 | 34.96 | 33.80 | 31.20 | 29.12 | 25.69 | 23.05 | 21.66 | 18.94 |
| 1860 | 6 | 34.91 | 35.25 | 33.99 | 31.28 | 29.31 | 24.47 | 21.81 | 19.86 | 17.02 |
| 1860 | 9 | 34.99 | 36.47 | 34.35 | 30.20 | 28.68 | 23.17 | 21.02 | 19.30 | 16.23 |
| 1860 | 12 | 36.98 | 38.67 | 37.17 | 33.91 | 31.21 | 26.29 | 22.47 | 20.22 | 17.33 |




Table OA.9: RMSFE (bps) of single-maturity Random Forest forecasts for U.S. Treasury yields.

| Seed | Horizon | 3M | 6M | 1Y | 2Y | 3Y | 5Y | 7Y | 10Y | 30Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8270 | 1 | 32.10 | 34.85 | 33.41 | 30.22 | 28.91 | 24.87 | 22.96 | 21.14 | 18.02 |
| 8270 | 3 | 30.62 | 33.10 | 31.98 | 29.47 | 27.83 | 23.91 | 22.61 | 20.73 | 17.58 |
| 8270 | 6 | 35.04 | 36.92 | 34.27 | 30.11 | 27.89 | 23.14 | 20.63 | 19.12 | 16.48 |
| 8270 | 9 | 33.68 | 35.21 | 33.54 | 30.42 | 28.10 | 22.91 | 20.54 | 18.97 | 16.51 |
| 8270 | 12 | 33.55 | 35.19 | 33.12 | 30.86 | 28.44 | 23.88 | 21.84 | 20.01 | 17.09 |
| 1860 | 1 | 36.02 | 37.45 | 36.11 | 32.43 | 30.88 | 26.07 | 23.35 | 21.42 | 18.21 |
| 1860 | 3 | 33.71 | 35.64 | 34.42 | 31.92 | 29.74 | 26.11 | 23.59 | 22.01 | 19.32 |
| 1860 | 6 | 35.49 | 36.18 | 34.62 | 31.77 | 29.98 | 25.01 | 22.44 | 20.31 | 17.61 |
| 1860 | 9 | 35.61 | 36.98 | 35.01 | 31.04 | 29.32 | 23.79 | 21.63 | 19.81 | 16.89 |
| 1860 | 12 | 37.54 | 39.12 | 37.88 | 34.59 | 31.94 | 26.98 | 23.11 | 20.84 | 17.94 |




Table OA.10: Random Forest forecast accuracy for global 10-year government bond yields (RMSFE in bps).

| Country | Horizon (hh) | Mean RMSFE (bps) | Min RMSFE (bps) | Max RMSFE (bps) |
| --- | --- | --- | --- | --- |
| Canada | 1 | 37.15 | 36.11 | 38.19 |
|  | 3 | 36.75 | 36.75 | 36.75 |
|  | 6 | 36.32 | 35.75 | 36.89 |
|  | 9 | 37.34 | 37.16 | 37.51 |
|  | 12 | 37.74 | 36.11 | 39.37 |
| China | 1 | 16.60 | 16.36 | 16.84 |
|  | 3 | 15.46 | 15.18 | 15.73 |
|  | 6 | 15.38 | 15.29 | 15.47 |
|  | 9 | 15.53 | 15.33 | 15.73 |
|  | 12 | 16.00 | 15.88 | 16.13 |
| Germany | 1 | 34.80 | 34.58 | 35.02 |
|  | 3 | 36.88 | 35.93 | 37.83 |
|  | 6 | 37.68 | 37.26 | 38.09 |
|  | 9 | 36.73 | 35.74 | 37.71 |
|  | 12 | 38.81 | 37.83 | 39.79 |
| Japan | 1 | 13.85 | 13.77 | 13.93 |
|  | 3 | 13.74 | 13.69 | 13.79 |
|  | 6 | 13.87 | 13.62 | 14.12 |
|  | 9 | 14.28 | 13.02 | 15.53 |
|  | 12 | 14.81 | 14.63 | 15.00 |
| Malaysia | 1 | 21.78 | 21.28 | 22.29 |
|  | 3 | 21.10 | 20.98 | 21.22 |
|  | 6 | 20.82 | 20.42 | 21.23 |
|  | 9 | 20.37 | 20.06 | 20.68 |
|  | 12 | 21.25 | 20.94 | 21.57 |
| UK | 1 | 43.33 | 42.59 | 44.08 |
|  | 3 | 43.05 | 41.27 | 44.83 |
|  | 6 | 41.84 | 40.82 | 42.85 |
|  | 9 | 44.48 | 42.08 | 46.89 |
|  | 12 | 43.98 | 43.00 | 44.97 |
| US | 1 | 44.79 | 44.67 | 44.90 |
|  | 3 | 43.16 | 42.80 | 43.52 |
|  | 6 | 42.75 | 42.36 | 43.14 |
|  | 9 | 43.97 | 43.45 | 44.49 |
|  | 12 | 43.99 | 43.41 | 44.58 |




Table OA.11: Estimated structural break dates by maturity of zero-coupon U.S. Treasury yields.

| Maturity | Break 1 | Break 2 | Break 3 | Break 4 | Break 5 | Break 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 3M | 30/09/2001 | 31/01/2005 | 31/10/2008 | 31/07/2017 | 31/01/2020 | 31/07/2022 |
| 6M | 30/09/2001 | 31/01/2005 | 31/10/2008 | 31/07/2017 | 31/01/2020 | 31/07/2022 |
| 1Y | 30/09/2001 | 31/01/2005 | 31/10/2008 | 28/02/2017 | 31/01/2020 | 31/07/2022 |
| 2Y | 30/09/2001 | 31/01/2005 | 31/10/2008 | 31/07/2022 | – | – |
| 3Y | 30/11/2000 | 31/10/2008 | 31/07/2022 | – | – | – |
| 4Y | 30/11/2000 | 31/10/2008 | 31/07/2022 | – | – | – |
| 5Y | 30/09/2001 | 31/10/2008 | 31/07/2022 | – | – | – |
| 6Y | 30/09/2001 | 31/10/2008 | 31/07/2022 | – | – | – |
| 7Y | 30/09/2001 | 31/10/2008 | 30/09/2011 | 31/07/2022 | – | – |
| 8Y | 30/09/2001 | 31/10/2008 | 30/09/2011 | 31/07/2022 | – | – |
| 9Y | 31/07/2002 | 31/10/2008 | 30/09/2011 | 31/07/2022 | – | – |
| 10Y | 31/07/2002 | 31/10/2008 | 30/09/2011 | 31/07/2022 | – | – |
| 15Y | 31/07/2002 | 31/10/2008 | 30/09/2011 | 31/08/2019 | 31/07/2022 | – |
| 20Y | 31/07/2002 | 31/10/2008 | 30/09/2011 | 31/08/2019 | 31/07/2022 | – |
| 30Y | 31/07/2002 | 31/10/2008 | 31/01/2015 | 31/07/2022 | – | – |




Table OA.12: Explained variance and cumulative explained variance of the first ten principal components.

|  |  |  |
| --- | --- | --- |
| Principal Component | Explained Variance | Cumulative Explained Variance |
| PC1 | 0.2304 | 0.2304 |
| PC2 | 0.1180 | 0.3484 |
| PC3 | 0.0977 | 0.4461 |
| PC4 | 0.0807 | 0.5267 |
| PC5 | 0.0523 | 0.5790 |
| PC6 | 0.0381 | 0.6172 |
| PC7 | 0.0372 | 0.6544 |
| PC8 | 0.0270 | 0.6814 |
| PC9 | 0.0226 | 0.7040 |
| PC10 | 0.0211 | 0.7251 |




Table OA.13: Top contributors to the first two principal components (loadings).

|  |  |  |
| --- | --- | --- |
| Variable | PC1 Loading | PC2 Loading |
| Panel A: Principal Component 1 | | |
| Exports of Goods and Services (AR, diff) | 0.800 |  |
| Imports of Goods and Services (AR, diff) | 0.794 |  |
| Gross National Product (AR, diff) | 0.770 |  |
| Gross Domestic Product (AR, diff) | 0.768 |  |
| Personal Consumption Expenditures (AR, diff) | 0.775 |  |
| Private Domestic Fixed Investment (AR, diff) | 0.757 |  |
| Commercial Bank C&I Loans (AR, diff) | 0.724 |  |
| Average Hourly Earnings, Total Private (diff) | 0.728 |  |
| Panel B: Principal Component 2 | | |
| Unemployment (16 Years and Over) |  | 0.644 |
| Unemployment Rate |  | 0.641 |
| Conference Board Leading Economic Index (diff) |  | 0.617 |
| Retail Sales and Food Services, Total (diff) |  | 0.596 |
| Interbank Rate, 3-Month (London) |  | 0.592 |
| Federal Funds Target Rate |  | 0.576 |
| Prime Rate Charged by Banks |  | 0.572 |
| Employment Cost Index, Civilian Workers (diff) |  | 0.573 |
| Treasury Bill Rate, 3-Month |  | 0.583 |

### OA.2 Algorithms

Algorithm OA.1  Rolling Diebold–Li Dynamic Nelson–Siegel (DNS) Forecasting

1:Monthly zero-coupon yields {yt​(τj)}j=1N\{y\_{t}(\tau\_{j})\}\_{j=1}^{N},
rolling window w=60w=60,
forecast horizons ℋ={1,3,6,9,12}\mathcal{H}=\{1,3,6,9,12\},
decay parameter λ=0.0609\lambda=0.0609

2:Out-of-sample yield forecasts and forecast errors

3:for t=wt=w to T−max⁡(ℋ)T-\max(\mathcal{H}) do

4:  for s=t−w+1s=t-w+1 to tt do

5:   Estimate DNS factors βs\beta\_{s} by nonlinear least squares

6:  end for

7:  Fit VAR(1) model βs+1=c+Φ​βs+ηs\beta\_{s+1}=c+\Phi\beta\_{s}+\eta\_{s}

8:  for each h∈ℋh\in\mathcal{H} do

9:   Compute β^t+h|t=∑k=0h−1Φk​c+Φh​βt\hat{\beta}\_{t+h|t}=\sum\_{k=0}^{h-1}\Phi^{k}c+\Phi^{h}\beta\_{t}

10:   for each maturity τj\tau\_{j} do

11:     Compute y^t+h|t​(τj)\hat{y}\_{t+h|t}(\tau\_{j}) via Nelson–Siegel equation

12:     Store forecast error et+h​(τj)e\_{t+h}(\tau\_{j})

13:   end for

14:  end for

15:end for

16:Compute RMSFE for each maturity and horizon




Algorithm OA.2  Rolling Factor–Augmented Dynamic Nelson–Siegel (FADNS) Forecasting

1:Monthly zero-coupon yields {yt​(τj)}j=1N\{y\_{t}(\tau\_{j})\}\_{j=1}^{N},
macroeconomic predictor panel {Zt∈ℝ111}\{Z\_{t}\in\mathbb{R}^{111}\},
rolling window w=60w=60,
number of principal components kk,
forecast horizons ℋ={1,3,6,9,12}\mathcal{H}=\{1,3,6,9,12\},
decay parameter λ=0.0609\lambda=0.0609

2:Out-of-sample yield forecasts and forecast errors

3:for t=wt=w to T−max⁡(ℋ)T-\max(\mathcal{H}) do

4:  for s=t−w+1s=t-w+1 to tt do

5:   Estimate DNS factors βs\beta\_{s} by nonlinear least squares

6:  end for

7:  Construct lagged macroeconomic predictors {Zt−w,…,Zt−1}\{Z\_{t-w},\ldots,Z\_{t-1}\}

8:  Apply unit-root filtering and standardization within the window

9:  Compute the first kk principal components Ft(k)F\_{t}^{(k)}

10:  Form augmented state vector

|  |  |  |
| --- | --- | --- |
|  | Xt(k)=(βt⊤,Ft(k)⊤)⊤X\_{t}^{(k)}=(\beta\_{t}^{\top},F\_{t}^{(k)\top})^{\top} |  |

11:  Fit VAR(1) model

|  |  |  |
| --- | --- | --- |
|  | Xs+1(k)=c(k)+Φ(k)​Xs(k)+ηs(k)X\_{s+1}^{(k)}=c^{(k)}+\Phi^{(k)}X\_{s}^{(k)}+\eta\_{s}^{(k)} |  |

12:  for each h∈ℋh\in\mathcal{H} do

13:   Compute

|  |  |  |
| --- | --- | --- |
|  | X^t+h|t(k)=∑ℓ=0h−1(Φ(k))ℓ​c(k)+(Φ(k))h​Xt(k)\hat{X}\_{t+h|t}^{(k)}=\sum\_{\ell=0}^{h-1}(\Phi^{(k)})^{\ell}c^{(k)}+(\Phi^{(k)})^{h}X\_{t}^{(k)} |  |

14:   Extract β^t+h|t\hat{\beta}\_{t+h|t} from X^t+h|t(k)\hat{X}\_{t+h|t}^{(k)}

15:   for each maturity τj\tau\_{j} do

16:     Compute y^t+h|t​(τj)\hat{y}\_{t+h|t}(\tau\_{j}) via the Nelson–Siegel equation

17:     Store forecast error et+h​(τj)e\_{t+h}(\tau\_{j})

18:   end for

19:  end for

20:end for

21:Compute RMSFE for each maturity and horizon




Algorithm OA.3  Rolling Random Forest Forecasting

1:Yield series {yt​(τ)}t=1T\{y\_{t}(\tau)\}\_{t=1}^{T} for maturity τ\tau;
macro predictors {Zt}t=1T\{Z\_{t}\}\_{t=1}^{T};
forecast horizon hh;
rolling window length W=60W=60;
set of random seeds 𝒮\mathcal{S};
hyperparameter space Θ\Theta.

2:Out-of-sample forecasts {y^t+h​(τ)}\{\hat{y}\_{t+h}(\tau)\}.

3:for each seed s∈𝒮s\in\mathcal{S} do

4:  for each forecast origin t=W,…,T−ht=W,\ldots,T-h do

5:   Construct predictor vector

|  |  |  |
| --- | --- | --- |
|  | Wt=(Zt−ℓ)ℓ=160∪(yt−ℓ​(τ))ℓ=059.W\_{t}=\big(Z\_{t-\ell}\big)\_{\ell=1}^{60}\cup\big(y\_{t-\ell}(\tau)\big)\_{\ell=0}^{59}. |  |

6:   Define the rolling training sample

|  |  |  |
| --- | --- | --- |
|  | 𝒟t,h={(Ws,ys+h​(τ)):s=t−W+1,…,t}.\mathcal{D}\_{t,h}=\{(W\_{s},y\_{s+h}(\tau)):\;s=t-W+1,\ldots,t\}. |  |

7:   Apply min–max normalization to 𝒟t,h\mathcal{D}\_{t,h}.

8:   Select hyperparameters

|  |  |  |
| --- | --- | --- |
|  | θ∗∈arg⁡minθ∈Θ⁡CV​-​MSE​(θ;𝒟t,h),\theta^{\*}\in\arg\min\_{\theta\in\Theta}\mathrm{CV\text{-}MSE}(\theta;\mathcal{D}\_{t,h}), |  |

using randomized cross-validation.

9:   Estimate a Random Forest regressor
g^h,τ(s)​(⋅)\hat{g}\_{h,\tau}^{(s)}(\cdot) on 𝒟t,h\mathcal{D}\_{t,h} with
hyperparameters θ∗\theta^{\*}.

10:   Compute the direct forecast

|  |  |  |
| --- | --- | --- |
|  | y^t+h​(τ)=g^h,τ(s)​(Wt).\hat{y}\_{t+h}(\tau)=\hat{g}\_{h,\tau}^{(s)}(W\_{t}). |  |

11:  end for

12:end for

13:return out-of-sample forecasts aggregated across seeds.




Algorithm OA.4  Forecast Combination Schemes 1-11

1:Rolling forecast errors Es:(t−1)∈ℝn×KE\_{s:(t-1)}\in\mathbb{R}^{n\times K}, n=t−sn=t-s;
ridge parameter ε\varepsilon;
OLS fraction zz;
LAD penalty ϕ\phi.

2:Weights wt∈ΔK−1w\_{t}\in\Delta^{K-1}.

3:Compute
MSEk=1n​∑u=st−1Eu,k2\mathrm{MSE}\_{k}=\frac{1}{n}\sum\_{u=s}^{t-1}E\_{u,k}^{2},
RMSEk=MSEk\mathrm{RMSE}\_{k}=\sqrt{\mathrm{MSE}\_{k}}

4:(1) FC–EW

5:wt,k=1/Kw\_{t,k}=1/K

6:(2) FC–RANK

7:Rank models by RMSEk\mathrm{RMSE}\_{k} (ascending) and set wt,k∝1/rankkw\_{t,k}\propto 1/\mathrm{rank}\_{k}

8:(3) FC–RMSE

9:wt,k∝1/max⁡(RMSEk,10−8)w\_{t,k}\propto 1/\max(\mathrm{RMSE}\_{k},10^{-8})

10:(4) FC–MSE

11:wt,k={1,k=arg⁡minj⁡MSEj,0,otherwisew\_{t,k}=\begin{cases}1,&k=\arg\min\_{j}\mathrm{MSE}\_{j},\\
0,&\text{otherwise}\end{cases}

12:(5) FC–OLS (top-zz selection)

13:Select index set 𝒦z\mathcal{K}\_{z} of the ⌈z​K⌉\lceil zK\rceil smallest RMSEk\mathrm{RMSE}\_{k}

14:Let X=Es:(t−1),𝒦zX=E\_{s:(t-1),\mathcal{K}\_{z}} and
y=1K​∑k=1KEs:(t−1),ky=\frac{1}{K}\sum\_{k=1}^{K}E\_{s:(t-1),k}

15:Fit y=X​βy=X\beta without intercept and set
w~𝒦z=|β^|\tilde{w}\_{\mathcal{K}\_{z}}=|\hat{\beta}|, w~k=0\tilde{w}\_{k}=0 for k∉𝒦zk\notin\mathcal{K}\_{z}

16:(6) FC–MV (minimum-variance)

17:Compute Σ=Cov​(Es:(t−1))\Sigma=\mathrm{Cov}(E\_{s:(t-1)})

18:w~=Σε†​𝟏/(𝟏⊤​Σε†​𝟏)\tilde{w}=\Sigma\_{\varepsilon}^{\dagger}\mathbf{1}/(\mathbf{1}^{\top}\Sigma\_{\varepsilon}^{\dagger}\mathbf{1}),
Σε=Σ+ε​I\Sigma\_{\varepsilon}=\Sigma+\varepsilon I

19:Clip w~←max⁡(w~,0)\tilde{w}\leftarrow\max(\tilde{w},0)

20:(7) FC–STACK

21:Set S=1n​Es:(t−1)⊤​Es:(t−1)S=\frac{1}{n}E\_{s:(t-1)}^{\top}E\_{s:(t-1)}

22:Solve
w~=arg⁡minw⁡12​w⊤​S​w​s.t.​ 1⊤​w=1,w≥0\tilde{w}=\arg\min\_{w}\frac{1}{2}w^{\top}Sw\;\text{s.t.}\;\mathbf{1}^{\top}w=1,\;w\geq 0

23:(8) FC–JMA

24:Solve
w~=arg⁡minw∈Δ⁡1n​∑u=st−1(∑k=1Kwk​Eu,k)2\tilde{w}=\arg\min\_{w\in\Delta}\frac{1}{n}\sum\_{u=s}^{t-1}\Big(\sum\_{k=1}^{K}w\_{k}E\_{u,k}\Big)^{2}

25:(9) FC–LAD

26:Solve the linear program over (w,ξ)(w,\xi):

|  |  |  |
| --- | --- | --- |
|  | minw≥0,ξ≥0⁡ϕn​𝟏⊤​w+1n​𝟏⊤​ξs.t.−E​w≤ξ,E​w≤ξ, 1⊤​w=1\min\_{w\geq 0,\xi\geq 0}\frac{\phi}{n}\mathbf{1}^{\top}w+\frac{1}{n}\mathbf{1}^{\top}\xi\quad\text{s.t.}\;-Ew\leq\xi,\;Ew\leq\xi,\;\mathbf{1}^{\top}w=1 |  |

27:Normalize wt=w~/(𝟏⊤​w~)w\_{t}=\tilde{w}/(\mathbf{1}^{\top}\tilde{w});
if 𝟏⊤​w~=0\mathbf{1}^{\top}\tilde{w}=0, set wt=𝟏/Kw\_{t}=\mathbf{1}/K




Algorithm OA.5  Adaptive and Distributionally Robust Forecast Combination Schemes

1:Rolling errors Es:(t−1)∈ℝn×KE\_{s:(t-1)}\in\mathbb{R}^{n\times K};
previous weights wt−1w\_{t-1};
ES level α\alpha;
robustness η\eta;
mixing parameter λ\lambda;
DRMV radius τ\tau.

2:Weights wt∈ΔK−1w\_{t}\in\Delta^{K-1}.

3:Utility: Expected Shortfall

4:For a sample xx, let qα=Quantileα​(x)q\_{\alpha}=\mathrm{Quantile}\_{\alpha}(x) and
ESα​(x)=𝔼​[x∣x≤qα]\mathrm{ES}\_{\alpha}(x)=\mathbb{E}[x\mid x\leq q\_{\alpha}]

5:(10) AFTER (rolling variance)

6:Compute vk=Var​(Es:(t−1),k)v\_{k}=\mathrm{Var}(E\_{s:(t-1),k}), clip vk←max⁡(vk,10−6)v\_{k}\leftarrow\max(v\_{k},10^{-6})

7:w~t,k=wt−1,k​exp⁡(−12​∑u=st−1Eu,k2vk)​vk−1/2\tilde{w}\_{t,k}=w\_{t-1,k}\exp\!\Big(-\frac{1}{2}\sum\_{u=s}^{t-1}\frac{E\_{u,k}^{2}}{v\_{k}}\Big)v\_{k}^{-1/2}

8:(11) AFTER (EWMA variance)

9:Compute EWMA variance vkv\_{k} from Es:(t−1),kE\_{s:(t-1),k} and clip as above

10:Apply the same update as in (10)

11:(12) FC–DRO–ES

12:Compute Lk=ESα​(Es:(t−1),k)L\_{k}=\mathrm{ES}\_{\alpha}(E\_{s:(t-1),k})

13:Stabilize Lk←Lk−minj⁡LjL\_{k}\leftarrow L\_{k}-\min\_{j}L\_{j}

14:w~t,k=exp⁡(η​Lk)\tilde{w}\_{t,k}=\exp(\eta L\_{k})

15:(13) FC–DRO–MIX

16:Compute
MSEk=1n​∑u=st−1Eu,k2\mathrm{MSE}\_{k}=\frac{1}{n}\sum\_{u=s}^{t-1}E\_{u,k}^{2},
ES2k=ESα​({Eu,k2})\mathrm{ES2}\_{k}=\mathrm{ES}\_{\alpha}(\{E\_{u,k}^{2}\})

17:Lk=(1−λ)​MSEk+λ​ES2kL\_{k}=(1-\lambda)\mathrm{MSE}\_{k}+\lambda\mathrm{ES2}\_{k}

18:Stabilize Lk←Lk−minj⁡LjL\_{k}\leftarrow L\_{k}-\min\_{j}L\_{j}

19:w~t,k=exp⁡(η​Lk)\tilde{w}\_{t,k}=\exp(\eta L\_{k})

20:(14) FC–DRMV

21:Compute Σ=Cov​(Es:(t−1))\Sigma=\mathrm{Cov}(E\_{s:(t-1)}) and Σrob=Σ+τ​I\Sigma^{\mathrm{rob}}=\Sigma+\tau I

22:w~=Σrob⁣†​𝟏/(𝟏⊤​Σrob⁣†​𝟏)\tilde{w}=\Sigma^{\mathrm{rob}\dagger}\mathbf{1}/(\mathbf{1}^{\top}\Sigma^{\mathrm{rob}\dagger}\mathbf{1})

23:Clip w~←max⁡(w~,0)\tilde{w}\leftarrow\max(\tilde{w},0)

24:Normalize wt=w~/(𝟏⊤​w~)w\_{t}=\tilde{w}/(\mathbf{1}^{\top}\tilde{w});
if 𝟏⊤​w~=0\mathbf{1}^{\top}\tilde{w}=0, set wt=𝟏/Kw\_{t}=\mathbf{1}/K