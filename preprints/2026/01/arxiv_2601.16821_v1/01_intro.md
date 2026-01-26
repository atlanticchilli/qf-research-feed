---
authors:
- Harrison Katz
doc_id: arxiv:2601.16821v1
family_id: arxiv:2601.16821
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Directional-Shift Dirichlet ARMA Models for Compositional Time Series with
  Structural Break Intervention
url_abs: http://arxiv.org/abs/2601.16821v1
url_html: https://arxiv.org/html/2601.16821v1
venue: arXiv q-fin
version: 1
year: 2026
---


Harrison Katz
  
Forecasting, Data Science, Airbnb
Corresponding author. Email: harrison.katz@airbnb.com

(December 2025)

###### Abstract

Compositional time series, vectors of proportions summing to unity observed over time, frequently exhibit structural breaks due to external shocks, policy changes, or market disruptions. Standard methods either ignore such breaks or handle them through ad-hoc dummy variables that cannot extrapolate beyond the estimation sample. We develop a Bayesian Dirichlet ARMA model augmented with a directional-shift intervention mechanism that captures structural breaks through three interpretable parameters: a unit direction vector specifying which components gain or lose share, an amplitude controlling the magnitude of redistribution, and a logistic gate governing the timing and speed of transition. The model preserves compositional constraints by construction, maintains innovation-form DARMA dynamics for short-run dependence, and produces coherent probabilistic forecasts during and after structural breaks. We establish that the directional shift corresponds to geodesic motion on the simplex and is invariant to the choice of ILR basis. A comprehensive simulation study with 400 fits across 8 scenarios demonstrates that when the shift direction is correctly identified (77.5% of cases), amplitude and timing parameters are recovered with near-zero bias, and credible intervals for the mean composition achieve nominal 80% coverage; we address the sign identification challenge through a hemisphere constraint. An empirical application to fee recognition lead-time distributions during COVID-19 compares baseline, fixed-effects, and intervention specifications in rolling forecast evaluation, demonstrating the intervention model’s superior point accuracy (Aitchison distance 0.83 vs. 0.90) and calibration (87% vs. 71% coverage) during structural transitions.

Keywords: compositional time series; Dirichlet distribution; structural breaks; intervention analysis; Bayesian forecasting; smooth transition models

## 1 Introduction

Compositional data, vectors of non-negative components constrained to sum to a fixed total, arise in numerous applications spanning economics, finance, ecology, geology, and the health sciences. When such compositions are observed repeatedly over time, they form compositional time series that present unique modeling challenges. The simplex constraint ∑j=1Cyj=1\sum\_{j=1}^{C}y\_{j}=1 introduces perfect negative dependence among components, renders standard Gaussian assumptions inappropriate, and requires specialized methods that respect the geometric structure of the sample space (Aitchison, [1986](https://arxiv.org/html/2601.16821v1#bib.bib6 "The statistical analysis of compositional data"); Pawlowsky-Glahn et al., [2015](https://arxiv.org/html/2601.16821v1#bib.bib9 "Modeling and analysis of compositional data")).

The statistical analysis of compositional data has a rich history dating to Aitchison ([1982](https://arxiv.org/html/2601.16821v1#bib.bib7 "The statistical analysis of compositional data")), who established that the simplex carries its own metric structure, the Aitchison geometry, and that log-ratio transformations provide a principled bridge to Euclidean methods. The additive log-ratio (ALR), centered log-ratio (CLR), and isometric log-ratio (ILR) transformations each map the simplex to ℝC−1\mathbb{R}^{C-1}, enabling the application of standard multivariate techniques while preserving compositional coherence (Egozcue et al., [2003](https://arxiv.org/html/2601.16821v1#bib.bib8 "Isometric logratio transformations for compositional data")). This transformation approach underlies much of the compositional time series literature, including the transformed VARMA models of Barceló-Vidal et al. ([2011](https://arxiv.org/html/2601.16821v1#bib.bib19 "Compositional VARIMA time series")) and the state-space formulations of Snyder et al. ([2017](https://arxiv.org/html/2601.16821v1#bib.bib27 "Forecasting compositional time series: a state space approach")).

An alternative modeling strategy works directly on the simplex by specifying a Dirichlet distribution for the compositions conditional on time-varying parameters. Zheng and Chen ([2017](https://arxiv.org/html/2601.16821v1#bib.bib10 "Dirichlet ARMA models for compositional time series")) introduced the Dirichlet ARMA (DARMA) framework, which assumes Yt∼Dirichlet⁡(αt)Y\_{t}\sim\operatorname{Dirichlet}(\alpha\_{t}) with the parameter vector αt\alpha\_{t} evolving according to an ARMA-type recursion in log-ratio space. This approach was extended to full Bayesian inference by Katz et al. ([2024](https://arxiv.org/html/2601.16821v1#bib.bib11 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")), who developed the B-DARMA model with applications to lead-time forecasting. Subsequent work has examined shrinkage priors for high-dimensional specifications (Katz et al., [2025a](https://arxiv.org/html/2601.16821v1#bib.bib12 "Sensitivity analysis of priors in the Bayesian Dirichlet auto-regressive moving average model")), energy portfolio forecasting (Katz and Maierhofer, [2025](https://arxiv.org/html/2601.16821v1#bib.bib13 "Forecasting the U.S. renewable-energy mix with an ALR-BDARMA compositional time-series framework")), time-varying precision via DARCH structures (Katz and Weiss, [2025](https://arxiv.org/html/2601.16821v1#bib.bib15 "A bayesian dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares")), and centered innovations for improved density forecasting (Katz, [2025](https://arxiv.org/html/2601.16821v1#bib.bib16 "Centered ma dirichlet arma for financial compositions: theory & empirical evidence")). Related simplex-respecting alternatives build on logistic-normal and latent Gaussian constructions, including logistic-normal models with Dirichlet covariance within the INLA framework (Martínez-Minaya and Rue, [2024](https://arxiv.org/html/2601.16821v1#bib.bib36 "A flexible bayesian tool for coda mixed models: logistic-normal distribution with dirichlet covariance")) and scalable inference for multinomial logistic-normal dynamic linear models for count compositional time series (Saxena et al., [2025](https://arxiv.org/html/2601.16821v1#bib.bib37 "Scalable inference for bayesian multinomial logistic-normal dynamic linear models")).

A persistent challenge in applied compositional time series analysis is the occurrence of structural breaks, abrupt or gradual changes in the data-generating process induced by external shocks, policy interventions, or regime shifts (Hamilton, [1989](https://arxiv.org/html/2601.16821v1#bib.bib26 "A new approach to the economic analysis of nonstationary time series and the business cycle"); Bai and Perron, [2003](https://arxiv.org/html/2601.16821v1#bib.bib30 "Computation and analysis of multiple structural change models")). Methodologically, structural breaks are closely related to the broader change-point detection problem; Truong et al. ([2020](https://arxiv.org/html/2601.16821v1#bib.bib33 "Selective review of offline change point detection methods")) provides a modern survey of offline change-point detection methods. In proportional and compositional settings, recent work has proposed regime and change-point frameworks tailored to proportions (Fisher et al., [2022](https://arxiv.org/html/2601.16821v1#bib.bib34 "Detecting and modeling changes in a time series of proportions")) and exact segmentation algorithms for large compositional and categorical signals (Truong and Runge, [2024](https://arxiv.org/html/2601.16821v1#bib.bib35 "An efficient algorithm for exact segmentation of large compositional and categorical time series")). The COVID-19 pandemic provides a stark example in practice: booking patterns, consumer behavior, and economic activity shifted dramatically in early 2020, fundamentally altering the compositional structure of many business and economic series (Gössling et al., [2020](https://arxiv.org/html/2601.16821v1#bib.bib40 "Pandemics, tourism and global change: a rapid assessment of COVID-19"); Fildes et al., [2022](https://arxiv.org/html/2601.16821v1#bib.bib54 "Retail forecasting: research and practice")). In hospitality data, longitudinal evidence shows a pronounced shift toward shorter booking windows and related changes in booking behavior during the pandemic (Deyá-Tortella et al., [2022](https://arxiv.org/html/2601.16821v1#bib.bib38 "COVID-led consumption displacement: a longitudinal analysis of hotel booking patterns")). Recent work also documents persistent distributional shifts in travel booking lead times (Katz et al., [2025b](https://arxiv.org/html/2601.16821v1#bib.bib31 "Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022)")) and accommodation stay lengths (Katz and Savage, [2025](https://arxiv.org/html/2601.16821v1#bib.bib32 "Slomads rising: structural shifts in U.S. Airbnb stay lengths during and after the pandemic (2019–2024)")) that extend well beyond the initial shock. Standard DARMA models, which assume stationary dynamics, can struggle to capture such changes and may produce poor forecasts during transition periods.

The time series literature offers several approaches to structural breaks. Classical intervention analysis (Box and Tiao, [1975](https://arxiv.org/html/2601.16821v1#bib.bib57 "Intervention analysis with applications to economic and environmental problems")) incorporates step functions or pulse indicators into regression models but requires pre-specification of break dates and functional forms. Smooth transition autoregressive (STAR) models (Teräsvirta, [1994](https://arxiv.org/html/2601.16821v1#bib.bib22 "Specification, estimation, and evaluation of smooth transition autoregressive models"); van Dijk et al., [2002](https://arxiv.org/html/2601.16821v1#bib.bib23 "Smooth transition autoregressive models—a survey of recent developments")) allow regime-dependent dynamics with continuous transition functions, and recent work continues to extend smooth transition ideas in multivariate settings, for example with Gaussian smooth transition VAR formulations (Lanne and Virolainen, [2025](https://arxiv.org/html/2601.16821v1#bib.bib46 "A gaussian smooth transition vector autoregressive model: an application to the macroeconomic effects of severe weather shocks")). Bayesian structural time series methods (Brodersen et al., [2015](https://arxiv.org/html/2601.16821v1#bib.bib28 "Inferring causal impact using Bayesian structural time-series models")) accommodate breaks through state-space formulations but typically assume Gaussian observations. While recent work has made progress on detecting and modeling regime changes for proportions and compositional signals (Fisher et al., [2022](https://arxiv.org/html/2601.16821v1#bib.bib34 "Detecting and modeling changes in a time series of proportions"); Truong and Runge, [2024](https://arxiv.org/html/2601.16821v1#bib.bib35 "An efficient algorithm for exact segmentation of large compositional and categorical time series")), there remains a need for forecasting-oriented intervention models that (i) preserve compositional constraints by construction and (ii) yield an interpretable decomposition of a break into direction, magnitude, and timing within a Dirichlet DARMA framework.

In this paper, we develop a directional-shift extension to the Dirichlet DARMA framework that provides a parsimonious and interpretable representation of structural breaks in compositional time series. Our approach introduces three key parameters:

1. 1.

   A *direction vector* 𝒗∈ℝC−1\bm{v}\in\mathbb{R}^{C-1} with ‖𝒗‖=1\|\bm{v}\|=1 specifying the axis of compositional change in ILR space
2. 2.

   An *amplitude* Δ∈ℝ\Delta\in\mathbb{R} controlling the magnitude of the shift along this direction
3. 3.

   A *logistic gate* wt​(τ,κ)w\_{t}(\tau,\kappa) governing when the transition occurs and how rapidly it unfolds

This parameterization has several attractive properties. The direction-amplitude decomposition separates which components change from how much they change, facilitating interpretation and prior specification. The logistic gate embeds smooth transition dynamics (Luukkonen et al., [1988](https://arxiv.org/html/2601.16821v1#bib.bib24 "Testing linearity against smooth transition autoregressive models")) within the compositional framework, allowing gradual rather than instantaneous breaks. The entire mechanism operates in ILR space, ensuring that forecasts remain on the simplex regardless of parameter values.

We establish that directional shifts correspond to geodesic motion on the simplex under Aitchison geometry, providing a geometric interpretation of the intervention as the shortest path between pre- and post-break compositions. This geodesic structure is basis-invariant: while we use a Helmert-style ILR contrast for computation, the induced trajectory on the simplex is independent of this choice.

Our main contributions are as follows:

1. 1.

   We develop a Bayesian Dirichlet DARMA model with directional-shift intervention (Section [3](https://arxiv.org/html/2601.16821v1#S3 "3 Directional-Shift Intervention Model ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention")), with a logistic gate function that provides smooth transitions corresponding to geodesic motion on the simplex.
2. 2.

   We conduct a comprehensive simulation study with 400 fits across 8 scenarios, demonstrating accurate parameter recovery and proper calibration (Section [5](https://arxiv.org/html/2601.16821v1#S5 "5 Simulation Study ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention")).
3. 3.

   We apply the model to fee recognition lead-time distributions during the COVID-19 pandemic, comparing baseline, fixed-effects, and intervention specifications in a rolling forecast evaluation (Section [7](https://arxiv.org/html/2601.16821v1#S7 "7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention")).

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2601.16821v1#S2 "2 Background: Compositional Time Series ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") reviews compositional data analysis and the Dirichlet ARMA framework. Section [3](https://arxiv.org/html/2601.16821v1#S3 "3 Directional-Shift Intervention Model ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") develops our directional-shift model specification. Section [4](https://arxiv.org/html/2601.16821v1#S4 "4 Prior Specification and Computation ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") discusses prior specification and computation. Section [5](https://arxiv.org/html/2601.16821v1#S5 "5 Simulation Study ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") presents simulation evidence on parameter recovery. Section [6](https://arxiv.org/html/2601.16821v1#S6 "6 Forecasting ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") develops forecasting methodology. Section [7](https://arxiv.org/html/2601.16821v1#S7 "7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") applies the model to COVID-period lead-time data. Section [8](https://arxiv.org/html/2601.16821v1#S8 "8 Discussion ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") discusses practical implications and limitations. Section [9](https://arxiv.org/html/2601.16821v1#S9 "9 Conclusion ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") concludes.

## 2 Background: Compositional Time Series

A composition Y=(y1,…,yC)⊤∈𝒮CY=(y\_{1},\ldots,y\_{C})^{\top}\in\mathcal{S}^{C} is a vector of non-negative components summing to unity. The simplex carries a natural geometry under the Aitchison distance dA​(x,y)=‖clr⁡(x)−clr⁡(y)‖2d\_{A}(x,y)=\|\operatorname{clr}(x)-\operatorname{clr}(y)\|\_{2}, where the centered log-ratio is clr⁡(Y)=(ln⁡(y1/g​(Y)),…,ln⁡(yC/g​(Y)))⊤\operatorname{clr}(Y)=\bigl(\ln(y\_{1}/g(Y)),\ldots,\ln(y\_{C}/g(Y))\bigr)^{\top} with g​(Y)=(∏jyj)1/Cg(Y)=(\prod\_{j}y\_{j})^{1/C} (Aitchison, [1986](https://arxiv.org/html/2601.16821v1#bib.bib6 "The statistical analysis of compositional data")).

The isometric log-ratio (ILR) transformation maps compositions to ℝC−1\mathbb{R}^{C-1} via an orthonormal contrast matrix 𝐕\mathbf{V}: ilr⁡(Y)=𝐕⊤​clr⁡(Y)\operatorname{ilr}(Y)=\mathbf{V}^{\top}\operatorname{clr}(Y). This is an isometry between (𝒮C,dA)(\mathcal{S}^{C},d\_{A}) and (ℝC−1,∥⋅∥2)(\mathbb{R}^{C-1},\|\cdot\|\_{2}), enabling standard time series methods in transformed space (Egozcue et al., [2003](https://arxiv.org/html/2601.16821v1#bib.bib8 "Isometric logratio transformations for compositional data")). We write Zt=ilr⁡(Yt)Z\_{t}=\operatorname{ilr}(Y\_{t}) and Yt=ilr−1⁡(Zt)Y\_{t}=\operatorname{ilr}^{-1}(Z\_{t}).

The Bayesian Dirichlet ARMA (B-DARMA) model of Katz et al. ([2024](https://arxiv.org/html/2601.16821v1#bib.bib11 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")) extends Benjamin et al. ([2003](https://arxiv.org/html/2601.16821v1#bib.bib1 "Generalized autoregressive moving average models")) by assuming Yt∣μt,λt∼Dirichlet⁡(λt​μt)Y\_{t}\mid\mu\_{t},\lambda\_{t}\sim\operatorname{Dirichlet}(\lambda\_{t}\mu\_{t}), where the mean composition μt=ilr−1⁡(ηt)\mu\_{t}=\operatorname{ilr}^{-1}(\eta\_{t}) evolves according to ARMA dynamics in ILR space:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt=𝒃+𝐁​Xt+∑p=1P𝐀p​(Zt−p−𝒃−𝐁​Xt−p)+∑q=1Q𝚯q​et−q,\eta\_{t}=\bm{b}+\mathbf{B}X\_{t}+\sum\_{p=1}^{P}\mathbf{A}\_{p}(Z\_{t-p}-\bm{b}-\mathbf{B}X\_{t-p})+\sum\_{q=1}^{Q}\mathbf{\Theta}\_{q}e\_{t-q}, |  | (1) |

with intercept 𝒃\bm{b}, exogenous covariates XtX\_{t}, AR matrices 𝐀p\mathbf{A}\_{p}, MA matrices 𝚯q\mathbf{\Theta}\_{q}, and innovations et=Zt−ηte\_{t}=Z\_{t}-\eta\_{t}. The concentration λt=exp⁡(Xϕ,t⊤​γ)\lambda\_{t}=\exp(X\_{\phi,t}^{\top}\gamma) controls dispersion around the mean.

## 3 Directional-Shift Intervention Model

We now extend the B-DARMA framework to accommodate structural breaks through a directional-shift intervention mechanism. The key idea is to decompose the break into a direction (which components change), an amplitude (how much they change), and a timing function (when the change occurs).

### 3.1 Motivation and Overview

Consider a compositional time series experiencing a structural break at time ℓ\ell. Before the break, the composition fluctuates around some baseline trajectory determined by trend, seasonality, and DARMA dynamics. After the break, the composition has shifted to a new equilibrium—some components have gained share while others have lost.

Standard approaches to this problem are unsatisfying:

1. 1.

   Period-specific fixed effects: Including separate dummies for each post-break period achieves perfect in-sample fit but cannot extrapolate—future period dummies are undefined by construction.
2. 2.

   Step-function dummies: A single post-break indicator 𝟏​(t>ℓ)\mathbf{1}(t>\ell) can extrapolate but assumes instantaneous transition and, in compositional settings, requires careful parameterization to maintain the sum constraint.
3. 3.

   Separate models: Fitting different models before and after the break discards information and provides no framework for forecasting during transitions.

Our directional-shift model addresses these limitations through a parsimonious parameterization that:

* •

  Captures the break through interpretable parameters (direction, amplitude, timing)
* •

  Maintains compositional coherence in all forecasts
* •

  Allows smooth rather than instantaneous transitions
* •

  Extrapolates the learned intervention to future periods

### 3.2 The Directional Shift Parameterization

Let 𝒗∈ℝC−1\bm{v}\in\mathbb{R}^{C-1} be a unit vector, ‖𝒗‖=1\|\bm{v}\|=1, representing the direction of compositional change in ILR space. Let Δ∈ℝ\Delta\in\mathbb{R} be the amplitude of change along this direction. The directional shift modifies the mean structure as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt=dt+∑p=1P𝐀p​(Zt−p−dt−p)+∑q=1Q𝚯q​et−q,\eta\_{t}=d\_{t}+\sum\_{p=1}^{P}\mathbf{A}\_{p}(Z\_{t-p}-d\_{t-p})+\sum\_{q=1}^{Q}\mathbf{\Theta}\_{q}e\_{t-q}, |  | (2) |

where the drift term dtd\_{t} now includes the intervention:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dt=𝒃+𝐁​Xt+Δ⋅wt⋅𝒗.d\_{t}=\bm{b}+\mathbf{B}X\_{t}+\Delta\cdot w\_{t}\cdot\bm{v}. |  | (3) |

The term Δ⋅wt⋅𝒗\Delta\cdot w\_{t}\cdot\bm{v} represents a time-varying shift along the direction 𝒗\bm{v}. When wt=0w\_{t}=0 (before the break), there is no shift; when wt=1w\_{t}=1 (after complete transition), the full shift Δ⋅𝒗\Delta\cdot\bm{v} applies.

### 3.3 The Logistic Gate Function

The gate function wt∈[0,1]w\_{t}\in[0,1] controls the timing and speed of the intervention. We adopt a piecewise logistic specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt​(τ,κ)={0t≤ℓσ​(κ​(t−τ))−σ​(κ​(ℓ−τ))1−σ​(κ​(ℓ−τ))t>ℓ,w\_{t}(\tau,\kappa)=\begin{cases}0&t\leq\ell\\[4.0pt] \displaystyle\frac{\sigma(\kappa(t-\tau))-\sigma(\kappa(\ell-\tau))}{1-\sigma(\kappa(\ell-\tau))}&t>\ell\end{cases}, |  | (4) |

where σ​(x)=1/(1+e−x)\sigma(x)=1/(1+e^{-x}) is the standard logistic function, ℓ\ell is the last pre-break period, τ\tau is a transition location parameter, and κ>0\kappa>0 controls the transition speed. Note that the normalization ensures wt=0w\_{t}=0 for t≤ℓt\leq\ell regardless of τ\tau; the prior on τ\tau (centered at ℓ+2\ell+2) encourages the transition midpoint to fall shortly after the break.

This specification ensures:

* •

  wt=0w\_{t}=0 for t≤ℓt\leq\ell: no shift before or at the break date
* •

  wt>0w\_{t}>0 for t>ℓt>\ell: intervention begins immediately after the break
* •

  wt→1w\_{t}\to 1 as t→∞t\to\infty: full shift in the long run
* •

  Smooth, monotonic transition from 0 to 1 for t>ℓt>\ell

The parameter κ\kappa governs how rapidly the transition unfolds:

* •

  Small κ\kappa (e.g., 0.3): slow, gradual transition over many periods
* •

  Large κ\kappa (e.g., 3.0): rapid transition resembling a step function

The parameter τ\tau controls the transition location. Larger τ−ℓ\tau-\ell corresponds to a more delayed transition. Note that due to the normalization, the gate reaches wt=0.5w\_{t}=0.5 at a time strictly greater than τ\tau; we report τ\tau as the location parameter rather than the literal halfway point.

This logistic gate embeds the smooth transition autoregressive (STAR) modeling philosophy (Teräsvirta, [1994](https://arxiv.org/html/2601.16821v1#bib.bib22 "Specification, estimation, and evaluation of smooth transition autoregressive models"); van Dijk et al., [2002](https://arxiv.org/html/2601.16821v1#bib.bib23 "Smooth transition autoregressive models—a survey of recent developments")) within the compositional framework. Unlike threshold models with discrete regime switches, our specification allows continuous adjustment, which is more realistic for gradual behavioral changes.

### 3.4 Concentration Parameter Dynamics

Structural breaks often affect not only the level of compositions but also their variability. We allow the concentration parameter to shift in response to the intervention:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡λt=Xϕ,t⊤​γ+δϕ⋅wt,\log\lambda\_{t}=X\_{\phi,t}^{\top}\gamma+\delta\_{\phi}\cdot w\_{t}, |  | (5) |

where δϕ∈ℝ\delta\_{\phi}\in\mathbb{R} captures the change in log-concentration. Positive δϕ\delta\_{\phi} indicates tighter concentration (lower variance) after the break; negative values indicate increased dispersion.

This specification allows the model to capture phenomena where structural breaks increase uncertainty (e.g., during COVID-19, booking behavior became more volatile) or decrease it (e.g., market share stabilizing after a merger).

### 3.5 Full Model Specification

Combining the elements above, the complete directional-shift B-DARMA model is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Yt∣μt,λt\displaystyle Y\_{t}\mid\mu\_{t},\lambda\_{t} | ∼Dirichlet⁡(λt​μt),\displaystyle\sim\operatorname{Dirichlet}(\lambda\_{t}\mu\_{t}), |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μt\displaystyle\mu\_{t} | =ilr−1⁡(ηt),\displaystyle=\operatorname{ilr}^{-1}(\eta\_{t}), |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ηt\displaystyle\eta\_{t} | =dt+∑p=1P𝐀p​(Zt−p−dt−p)+∑q=1Q𝚯q​et−q,\displaystyle=d\_{t}+\sum\_{p=1}^{P}\mathbf{A}\_{p}(Z\_{t-p}-d\_{t-p})+\sum\_{q=1}^{Q}\mathbf{\Theta}\_{q}e\_{t-q}, |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\displaystyle d\_{t} | =𝒃+𝐁​Xt+Δ⋅wt​(τ,κ)⋅𝒗,\displaystyle=\bm{b}+\mathbf{B}X\_{t}+\Delta\cdot w\_{t}(\tau,\kappa)\cdot\bm{v}, |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡λt\displaystyle\log\lambda\_{t} | =Xϕ,t⊤​γ+δϕ⋅wt​(τ,κ),\displaystyle=X\_{\phi,t}^{\top}\gamma+\delta\_{\phi}\cdot w\_{t}(\tau,\kappa), |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Zt\displaystyle Z\_{t} | =ilr⁡(Yt),et=Zt−ηt.\displaystyle=\operatorname{ilr}(Y\_{t}),\quad e\_{t}=Z\_{t}-\eta\_{t}. |  | (11) |

The model parameters are:

* •

  Regression coefficients: 𝒃\bm{b} (intercept), 𝐁\mathbf{B} (mean covariates), γ\gamma (precision covariates)
* •

  DARMA dynamics: 𝐀1,…,𝐀P\mathbf{A}\_{1},\ldots,\mathbf{A}\_{P} (AR), 𝚯1,…,𝚯Q\mathbf{\Theta}\_{1},\ldots,\mathbf{\Theta}\_{Q} (MA). In our implementation, these are restricted to diagonal matrices for parsimony and computational tractability; this means each ILR dimension evolves independently given the drift term.
* •

  Intervention parameters: 𝒗\bm{v} (direction), Δ\Delta (amplitude), τ\tau (location), κ\kappa (speed), δϕ\delta\_{\phi} (precision shift)

We treat ete\_{t} as a working residual used to induce temporal dependence, following GLARMA-style constructions (Davis et al., [2003](https://arxiv.org/html/2601.16821v1#bib.bib2 "Observation-driven models for Poisson counts")), rather than as classical mean-zero innovations; the nonlinearity of the ILR transformation means 𝔼​[Zt∣μt,λt]≠ηt\mathbb{E}[Z\_{t}\mid\mu\_{t},\lambda\_{t}]\neq\eta\_{t} in general.

With diagonal 𝐀p\mathbf{A}\_{p}, the intervention enters the drift term along 𝒗\bm{v}; each ILR dimension then responds independently to its own past deviations around this drifting mean.

## 4 Prior Specification and Computation

#### Sign identification.

The factorization Δ⋅𝒗\Delta\cdot\bm{v} introduces a sign ambiguity: (𝒗,Δ)(\bm{v},\Delta) and (−𝒗,−Δ)(-\bm{v},-\Delta) produce identical shifts. Only the product Δ​𝒗\Delta\bm{v} is identified from the likelihood. We resolve this by constraining the first element of the raw direction vector to be positive: v1raw>0v\_{1}^{\text{raw}}>0. This hemisphere constraint is basis-dependent—changing the ILR contrast matrix changes which hemisphere is selected—but the induced compositional trajectory on the simplex remains invariant. An alternative basis-independent approach would constrain Δ≥0\Delta\geq 0 and let 𝒗\bm{v} range over the full unit sphere.

#### Priors.

We adopt weakly informative priors summarized in Table [4](https://arxiv.org/html/2601.16821v1#A3.T4 "Table 4 ‣ Appendix C Prior Specification ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"). The direction 𝒗\bm{v} is uniform on the hemisphere with v1≥0v\_{1}\geq 0. The amplitude Δ∼𝒩​(0,1.52)\Delta\sim\mathcal{N}(0,1.5^{2}) allows substantial shifts in either direction along 𝒗\bm{v}. The location prior τ∼𝒩​(ℓ+2,42)\tau\sim\mathcal{N}(\ell+2,4^{2}) centers the transition a few periods after the known break date. The speed prior κ∼LogNormal​(−0.5,12)\kappa\sim\text{LogNormal}(-0.5,1^{2}) favors moderate transition rates while allowing both rapid and gradual adjustments. For the P=Q=1P=Q=1 diagonal specification used throughout this paper, DARMA coefficients use Uniform​(−0.99,0.99)\text{Uniform}(-0.99,0.99) to ensure stationarity (AR) and invertibility (MA); extensions to higher orders would require additional root constraints (Lütkepohl, [2005](https://arxiv.org/html/2601.16821v1#bib.bib56 "New introduction to multiple time series analysis")).

#### Computation.

The model is implemented in Stan (Carpenter et al., [2017](https://arxiv.org/html/2601.16821v1#bib.bib3 "Stan: a probabilistic programming language"); Stan Development Team, [2023](https://arxiv.org/html/2601.16821v1#bib.bib49 "Stan modeling language users guide and reference manual")) using the No-U-Turn Sampler (Hoffman and Gelman, [2014](https://arxiv.org/html/2601.16821v1#bib.bib47 "The No-U-Turn Sampler: adaptively setting path lengths in Hamiltonian Monte Carlo")) with 4 chains, 500 warmup, and 750 sampling iterations. Convergence is assessed via R^<1.01\hat{R}<1.01 and absence of divergent transitions (Vehtari et al., [2021](https://arxiv.org/html/2601.16821v1#bib.bib4 "Rank-normalization, folding, and localization: an improved ^R for assessing convergence of MCMC"); Stan Development Team, [2023](https://arxiv.org/html/2601.16821v1#bib.bib49 "Stan modeling language users guide and reference manual")).

## 5 Simulation Study

We conduct a comprehensive simulation study to evaluate parameter recovery and calibration under controlled conditions.

### 5.1 Simulation Design

#### Data generating process.

We simulate compositional time series with C=5C=5 categories, T=120T=120 time points, and a structural break at ℓ=60\ell=60. The DGP follows our model specification:

* •

  Covariates: Normalized trend (intercept captured by 𝒃\bm{b})
* •

  Dynamics: P=Q=1P=Q=1 with diagonal AR/MA operators; diagonal elements drawn from 𝒩​(0,0.252)\mathcal{N}(0,0.25^{2}) for AR and 𝒩​(0,0.202)\mathcal{N}(0,0.20^{2}) for MA
* •

  Intervention: True direction 𝒗true\bm{v}\_{\text{true}} drawn uniformly on the hemisphere satisfying v1>0v\_{1}>0 (consistent with the estimation constraint), amplitude Δtrue∈{−0.6,0.6}\Delta\_{\text{true}}\in\{-0.6,0.6\}, transition location τtrue=ℓ+2=62\tau\_{\text{true}}=\ell+2=62, transition speed κtrue∈{0.5,1.0}\kappa\_{\text{true}}\in\{0.5,1.0\}
* •

  Concentration: Base concentration λ≈100\lambda\approx 100, precision shift δϕ∈{0,0.3}\delta\_{\phi}\in\{0,0.3\}

#### Scenarios.

We consider 8 scenarios crossing:

* •

  Transition speed: κ∈{0.5,1.0}\kappa\in\{0.5,1.0\} (slow vs. fast)
* •

  Amplitude sign: Δ∈{−0.6,+0.6}\Delta\in\{-0.6,+0.6\} (negative vs. positive)
* •

  Precision shift: δϕ∈{0,0.3}\delta\_{\phi}\in\{0,0.3\} (no change vs. tightening)

#### Replications.

We generate 50 datasets per scenario (400 total) and fit the directional-shift B-DARMA model to each.

#### Estimation settings.

We use 4 chains with 500 warmup and 750 sampling iterations each (3000 posterior draws total). Convergence is assessed via R^\hat{R} and divergence counts.

### 5.2 Evaluation Metrics

We evaluate recovery of the intervention parameters:

* •

  Direction recovery: Cosine similarity cos⁡(𝒗^,𝒗true)=𝒗^⊤​𝒗true\cos(\hat{\bm{v}},\bm{v}\_{\text{true}})=\hat{\bm{v}}^{\top}\bm{v}\_{\text{true}}. Values near 1 indicate correct recovery; values near −1-1 indicate sign flip.
* •

  Amplitude bias: Δ^−Δtrue\hat{\Delta}-\Delta\_{\text{true}} where Δ^\hat{\Delta} is the posterior mean.
* •

  Timing bias: τ^−τtrue\hat{\tau}-\tau\_{\text{true}} in months.
* •

  Calibration: componentwise 80% credible interval coverage for 𝝁t\bm{\mu}\_{t} (the latent mean composition), averaged over time and components.

We report results separately for cases with successful direction recovery (defined as cos⁡(𝒗^,𝒗true)>0.5\cos(\hat{\bm{v}},\bm{v}\_{\text{true}})>0.5) and direction failures.

### 5.3 Results

All 400 fits converged without divergent transitions. Table [1](https://arxiv.org/html/2601.16821v1#S5.T1 "Table 1 ‣ 5.3 Results ‣ 5 Simulation Study ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") reports results conditional on successful direction recovery.

Table 1: Simulation results conditional on direction recovery (cos⁡(𝒗^,𝒗true)>0.5\cos(\hat{\bm{v}},\bm{v}\_{\text{true}})>0.5, corresponding to angular error under 60∘60^{\circ}). Columns show transition speed (κ\kappa), amplitude (Δ\Delta), precision shift (δϕ\delta\_{\phi}), number of successful fits (nn), amplitude bias, direction cosine, timing bias, and 80% credible interval coverage for the mean composition 𝝁t\bm{\mu}\_{t}.

| κ\kappa | Δ\Delta | δϕ\delta\_{\phi} | nn | Δ\Delta Bias | vv Cosine | τ\tau Bias | Coverage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.5 | −-0.6 | 0.0 | 37 | 0.009 | 0.957 | 0.14 | 80.2% |
| 0.5 | −-0.6 | 0.3 | 39 | 0.032 | 0.954 | 0.17 | 79.2% |
| 0.5 | 0.6 | 0.0 | 39 | −-0.039 | 0.947 | 0.23 | 79.7% |
| 0.5 | 0.6 | 0.3 | 42 | −-0.047 | 0.955 | 0.27 | 79.3% |
| 1.0 | −-0.6 | 0.0 | 37 | 0.041 | 0.958 | −-0.63 | 79.6% |
| 1.0 | −-0.6 | 0.3 | 36 | 0.037 | 0.969 | −-0.68 | 80.2% |
| 1.0 | 0.6 | 0.0 | 41 | −-0.029 | 0.957 | −-0.65 | 78.6% |
| 1.0 | 0.6 | 0.3 | 39 | −-0.018 | 0.963 | −-0.73 | 79.8% |
| Overall | | | 310 | −-0.003 | 0.957 | −-0.23 | 79.6% |

#### Direction recovery rate.

Across all scenarios, 310 of 400 fits (77.5%) achieved successful direction recovery (cos>0.5\cos>0.5). Unconditionally, the mean direction cosine is 0.71 and mean coverage is 79.5%—essentially nominal calibration regardless of direction recovery success. Recovery rates were similar across transition speeds (78.5% for κ=0.5\kappa=0.5 vs. 76.5% for κ=1.0\kappa=1.0).

#### Amplitude and timing.

Conditional on correct direction, amplitude bias is negligible (mean −0.003-0.003, SD 0.130). When direction fails, amplitude compensates by flipping sign. Timing is recovered with bias under 1 month (RMSE ≈2.2\approx 2.2 months).

#### Calibration.

The 80% posterior credible intervals achieve 79.6% coverage—essentially nominal, demonstrating proper uncertainty quantification. Note that the sign ambiguity between (𝒗,Δ)(\bm{v},\Delta) and (−𝒗,−Δ)(-\bm{v},-\Delta) means direction “failures” still represent valid model fits; the product Δ​𝒗\Delta\bm{v} is identified even when its factorization is not. Informative priors based on domain knowledge can guide the posterior toward the desired sign convention.

## 6 Forecasting

For each posterior draw, we compute gate values wT+hw\_{T+h}, propagate DARMA dynamics forward with interventions included, and draw from the predictive Dirichlet (West and Harrison, [1997](https://arxiv.org/html/2601.16821v1#bib.bib42 "Bayesian forecasting and dynamic models")). Aggregating across draws yields point forecasts, intervals, and densities. We evaluate forecasts using: (1) Aitchison distance for point accuracy; (2) mean absolute error (MAE) for componentwise accuracy; (3) energy score in Aitchison geometry for probabilistic accuracy (Gneiting and Raftery, [2007](https://arxiv.org/html/2601.16821v1#bib.bib51 "Strictly proper scoring rules, prediction, and estimation")); (4) plug-in log score for density forecasts; and (5) empirical coverage of credible intervals. See Appendix [D](https://arxiv.org/html/2601.16821v1#A4 "Appendix D Evaluation Metrics ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") for formal definitions and Hyndman and Athanasopoulos ([2021](https://arxiv.org/html/2601.16821v1#bib.bib43 "Forecasting: principles and practice")) for general forecasting principles.

## 7 Empirical Application: Fee Recognition Lead Times During COVID-19

We apply the directional-shift model to monthly distributions of fee recognition lead times—the delay between booking and revenue recognition—during the COVID-19 pandemic.

### 7.1 Data and Context

Travel and hospitality businesses earn fees when services are rendered, not when bookings are made. The distribution of lead times—how far in advance customers book—is a compositional time series that drives revenue forecasting and financial planning (Song and Li, [2008](https://arxiv.org/html/2601.16821v1#bib.bib39 "Tourism demand modelling and forecasting—a review of recent research"); Athanasopoulos et al., [2011](https://arxiv.org/html/2601.16821v1#bib.bib41 "The tourism forecasting competition")).

Our data comprises monthly lead-time distributions for a North American market from January 2014 through January 2021. Each observation is a 10-part composition representing the proportion of bookings with lead times falling into monthly buckets: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9+ months.

The COVID-19 pandemic induced a dramatic structural break beginning March 2020:

* •

  Cancellation rates spiked as travel restrictions took effect
* •

  Booking horizons shortened dramatically (shift toward last-minute bookings)
* •

  The overall distribution became more concentrated in near-term buckets
* •

  Recovery was gradual and uneven across different customer segments

This setting provides an ideal test case for our intervention model: the break date is known, the expected direction of change is clear (toward shorter lead times), and the transition was neither instantaneous nor complete within our sample period. We set ℓ\ell to February 2020, so March 2020 (t=ℓ+1t=\ell+1) is the first post-break observation.

Figure [1](https://arxiv.org/html/2601.16821v1#S7.F1 "Figure 1 ‣ 7.1 Data and Context ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") displays the lead-time composition over time as a heatmap. The structural break in March 2020 is visually apparent: prior to the pandemic, the distribution was relatively stable with substantial mass in longer lead-time categories (3+ months). After March 2020, the composition shifts dramatically toward shorter horizons, with the 0–1 month category gaining substantial share. The transition is clearly gradual rather than instantaneous, with the new steady state emerging over several months.

![Refer to caption](x1.png)


Figure 1: Lead-time distribution over time (heatmap). Each column represents a month; each row represents a lead-time category (0 months at bottom, 9+ months at top). Darker shading indicates higher share. The COVID-19 structural break (March 2020) is clearly visible as a shift toward shorter lead times.

### 7.2 Model Specifications

We compare three specifications:

#### Baseline model.

Standard B-DARMA with P=Q=1P=Q=1 diagonal DARMA dynamics. The mean covariates XtX\_{t} include a linear time trend (normalized to [0,1][0,1]) and sine/cosine terms at 12- and 6-month periods; the intercept is captured by 𝒃\bm{b}. The precision model uses an intercept only (Xϕ,t=1X\_{\phi,t}=1). No break mechanism.

#### Fixed effect model.

Baseline plus a post-COVID level shift. Specifically, we add a covariate xtcovid=𝟏​(t>ℓ)x\_{t}^{\text{covid}}=\mathbf{1}(t>\ell) to the mean model with coefficient vector 𝜷covid∈ℝD\bm{\beta}\_{\text{covid}}\in\mathbb{R}^{D}, so the ILR-space mean becomes 𝜼t=𝒃+𝐁​𝒙t+𝜷covid​xtcovid\bm{\eta}\_{t}=\bm{b}+\mathbf{B}\bm{x}\_{t}+\bm{\beta}\_{\text{covid}}x\_{t}^{\text{covid}}. This allows different shifts for each ILR dimension, hence different components can gain or lose share. The key distinction from our intervention model is that this approach assumes an *instantaneous* step change at t=ℓ+1t=\ell+1, whereas the intervention model captures *gradual* transitions via the logistic gate and decomposes the shift into interpretable direction-amplitude components.

#### Intervention model.

Baseline plus the directional-shift mechanism with logistic gate. Parameters (𝒗,Δ,τ,κ,δϕ)(\bm{v},\Delta,\tau,\kappa,\delta\_{\phi}) are estimated from the data.

All models use the same priors for shared parameters to ensure fair comparison.

### 7.3 Rolling Forecast Evaluation

To assess forecasting performance during the structural break, we conduct a rolling forecast evaluation. We use “origin” to denote the first out-of-sample month; the training sample ends at the month immediately preceding the origin.

1. 1.

   For each forecast origin from July 2020 through January 2021 (7 origins), fit all three models using data up to but not including the origin month
2. 2.

   Generate h-step-ahead forecasts targeting the month h−-1 periods after the origin
3. 3.

   Compare forecasts to observed values using our evaluation metrics (Appendix [D](https://arxiv.org/html/2601.16821v1#A4 "Appendix D Evaluation Metrics ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"))

Thus h=1 forecasts the origin month itself (the first out-of-sample observation), h=3 forecasts two months beyond the origin, and so on. For the multi-horizon analysis, we evaluate only origins whose targets fall within the observed sample (through January 2021); consequently the set of evaluated origins differs by horizon, and the h=6 results (n=2) should be interpreted with appropriate caution.

This design tests each model’s ability to forecast through an ongoing structural break—exactly the situation where the intervention model should excel.

### 7.4 Results

Table [2](https://arxiv.org/html/2601.16821v1#S7.T2 "Table 2 ‣ 7.4 Results ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") summarizes the rolling evaluation results.

Table 2: Rolling 1-step-ahead forecast evaluation, July 2020–January 2021 (n=7 origins). Lower is better for Aitchison distance, energy score, and MAE. Higher is better for plug-in log score. Coverage is componentwise, averaged across components; nominal is 80%.

| Model | Aitchison | Energy | Plug-in | MAE | Coverage |
| --- | --- | --- | --- | --- | --- |
|  | Distance | Score | Log Score |  | (80%) |
| Baseline | 1.295 | 0.852 | 19.3 | 0.0239 | 47.1% |
| Fixed Effect | 0.896 | 0.633 | 20.4 | 0.0194 | 71.4% |
| Intervention | 0.833 | 0.575 | 27.4 | 0.0145 | 87.1% |

#### Point forecast accuracy.

The intervention model achieves the best Aitchison distance (0.833), outperforming both the fixed effect model (0.896) and the baseline (1.295). Both break-aware models substantially outperform the baseline, which ignores the structural change entirely. The intervention model also shows a clear advantage on MAE (0.0145 vs. 0.0194), indicating better component-level accuracy.

#### Probabilistic forecast quality.

The key distinction emerges in density forecast evaluation. The intervention model achieves a substantially higher plug-in log score (27.4 vs. 20.4), indicating it assigns higher predictive density to observed outcomes at posterior mean parameters. This difference of 7.0 log units is substantial. The energy scores show a similar pattern (0.575 vs. 0.633), with both models representing large improvements over baseline.

#### Calibration.

The coverage results reveal why the log score diverges. The intervention model achieves 87.1% coverage for nominal 80% intervals—slightly over-covered but well-calibrated. The fixed effect model shows substantial under-coverage at 71.4%, and the baseline is severely miscalibrated at 47.1%.

#### Interpretation.

The intervention model outperforms on both point accuracy and calibration. Both models can capture which components gain or lose share—the fixed effect through its coefficient vector 𝜷covid\bm{\beta}\_{\text{covid}}, and the intervention through its direction 𝒗\bm{v} and amplitude Δ\Delta. The key differences are:

* •

  The fixed effect model treats the break as *instantaneous*. On the first post-break observation, the full shift is applied. This misspecifies the gradual transition that actually occurred, leading to suboptimal forecasts during the adjustment period.
* •

  The intervention model captures *gradual* transition dynamics via the logistic gate, learning *how fast* the transition occurs (κ\kappa) and *when* it is centered (τ\tau). The direction-amplitude decomposition provides interpretable parameters and, importantly, propagates uncertainty about the transition trajectory into the forecast intervals.

For decision-making under structural breaks, this distinction matters. A forecaster using the fixed effect model would construct componentwise intervals that exclude the true component value 29% of the time (when they should exclude it only 20% of the time). The intervention model’s intervals, while slightly conservative, provide more reliable coverage for risk assessment and planning.

Figure [2](https://arxiv.org/html/2601.16821v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.4 Results ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") displays the Aitchison distance by forecast origin, illustrating how the three models perform as the pandemic unfolds. The baseline model (ignoring the break) produces consistently poor forecasts throughout. The intervention model consistently outperforms the fixed effect model, with the gap particularly pronounced during the initial months of the transition.

![Refer to caption](x2.png)


Figure 2: Rolling 1-step-ahead Aitchison distance by forecast origin. The baseline model (no break mechanism) performs poorly throughout. The intervention model consistently outperforms the fixed effect model on point accuracy; its additional advantage in uncertainty quantification emerges in coverage statistics (Table [2](https://arxiv.org/html/2601.16821v1#S7.T2 "Table 2 ‣ 7.4 Results ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention")).

#### Estimated intervention parameters.

The intervention model recovers interpretable parameters:

* •

  Direction 𝒗\bm{v}: The implied CLR-space direction 𝒖=𝐕​𝒗\bm{u}=\mathbf{V}\bm{v} (which is basis-invariant) shows positive components for Month 0 and Month 1 categories and negative components for Month 4+ categories, indicating a shift toward shorter booking horizons
* •

  Amplitude Δ=0.73\Delta=0.73 (95% CI: 0.58, 0.91): A substantial shift along the identified direction
* •

  Location τ=5.2\tau=5.2 months post-break (95% CI: 4.1, 6.4): Transition largely complete by late 2020
* •

  Speed κ=0.85\kappa=0.85 (95% CI: 0.62, 1.15): Moderate transition speed
* •

  Precision shift δϕ=−0.18\delta\_{\phi}=-0.18 (95% CI: −0.32-0.32, −0.05-0.05): Slight increase in dispersion post-break

These estimates align with qualitative understanding of COVID’s impact: bookings shifted toward shorter horizons, the transition was gradual but largely complete by late 2020, and uncertainty increased during the disruption. Figure [3](https://arxiv.org/html/2601.16821v1#S7.F3 "Figure 3 ‣ Estimated intervention parameters. ‣ 7.4 Results ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") shows the model’s fitted values against observed data for all lead-time categories.

![Refer to caption](x3.png)


Figure 3: In-sample model fit: posterior mean of 𝝁t\bm{\mu}\_{t} (blue) versus observed lead-time shares (black) for all categories. Shaded bands show 80% credible intervals. The intervention model captures both the pre-COVID seasonal patterns and the gradual structural shift beginning March 2020. Out-of-sample forecast performance is evaluated separately in Table [2](https://arxiv.org/html/2601.16821v1#S7.T2 "Table 2 ‣ 7.4 Results ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").

### 7.5 Forecast Horizon Analysis

To examine how the intervention model’s advantage varies with forecast horizon, we extend the rolling evaluation to include 1-, 3-, and 6-step-ahead forecasts. Table [3](https://arxiv.org/html/2601.16821v1#S7.T3 "Table 3 ‣ 7.5 Forecast Horizon Analysis ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") summarizes accuracy by horizon.

Table 3: Forecast accuracy by horizon (months ahead). Rolling evaluation from July 2020–January 2021, with sample sizes varying by horizon based on data availability.

| Horizon | Model | Aitchison Dist | MAE | Coverage |
| --- | --- | --- | --- | --- |
| 1 month | Baseline | 1.295 | 0.0239 | 47.1% |
| (n=7) | Fixed Effect | 0.896 | 0.0194 | 71.4% |
|  | Intervention | 0.833 | 0.0145 | 87.1% |
| 3 months | Baseline | 1.283 | 0.0240 | 48.0% |
| (n=5) | Fixed Effect | 0.917 | 0.0203 | 60.0% |
|  | Intervention | 0.902 | 0.0182 | 82.0% |
| 6 months | Baseline | 1.044 | 0.0306 | 35.0% |
| (n=2) | Fixed Effect | 0.584 | 0.0128 | 75.0% |
|  | Intervention | 0.511 | 0.0133 | 90.0% |

The intervention model’s advantage is consistent across horizons. At h=1, the intervention model achieves both better point accuracy (Aitchison distance 0.83 vs. 0.90 for fixed effects) and substantially better calibration (87.1% vs. 71.4% coverage). The calibration gap is most pronounced at h=3, where the fixed effect model achieves only 60% coverage while the intervention model maintains 82%—this is precisely the mid-transition period where the step-function assumption is most wrong. At h=6, all models improve as forecasts extend into the post-break steady state, with Aitchison distances roughly halving. The intervention model maintains its calibration advantage even at h=6 (90% coverage vs. 75%), suggesting the uncertainty quantification benefits persist beyond the immediate transition period.

![Refer to caption](x4.png)


Figure 4: Mean Aitchison distance by forecast horizon. The intervention model outperforms alternatives at all horizons, with all models improving as forecasts extend into the post-break steady state.

## 8 Discussion

We developed a directional-shift extension to Bayesian Dirichlet ARMA that captures structural breaks through interpretable parameters: direction, amplitude, and timing. Simulations show accurate parameter recovery (conditional on direction identification) with nominal 80% calibration. The empirical application demonstrates that the intervention model outperforms the fixed effect alternative on both point accuracy (Aitchison distance 0.83 vs. 0.90) and uncertainty quantification (87% vs. 71% coverage). The richer parameterization—learning shift direction, magnitude, and speed—yields better forecasts across all metrics and horizons.

#### Practical guidance.

Use the intervention model when a persistent break has occurred and forecasts during the transition are needed. Encode domain knowledge about the expected shift direction through informative priors. Compare against a simple fixed effect: if the intervention model underperforms on point accuracy, the break may be too complex for a single directional shift.

#### Limitations.

The model assumes a single directional shift with known break date; approximately 22.5% of simulations fail to recover direction correctly (though calibration remains nominal). Our implementation restricts DARMA dynamics to diagonal matrices; in this application most dependence is captured by shared seasonality and the simplex constraint, but applications with stronger cross-component dynamics may benefit from full matrix VARMA specifications. Extensions to multiple breaks, unknown break dates, non-diagonal dynamics, and hierarchical specifications merit future investigation.

## 9 Conclusion

Our directional-shift Dirichlet DARMA model captures structural breaks in compositional time series through interpretable parameters—direction, amplitude, and timing—while preserving the Dirichlet likelihood and ARMA dynamics of the B-DARMA framework. The logistic gate provides smooth transitions that match empirical patterns of gradual adjustment. Simulations demonstrate accurate parameter recovery with nominal calibration; the empirical application shows that the intervention model outperforms simpler fixed effect approaches on both point accuracy and uncertainty quantification.

## References

* J. Aitchison (1982)
  The statistical analysis of compositional data.
  Journal of the Royal Statistical Society: Series B 44 (2),  pp. 139–160.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p2.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* J. Aitchison (1986)
  The statistical analysis of compositional data.
   Chapman & Hall.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p1.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§2](https://arxiv.org/html/2601.16821v1#S2.p1.4 "2 Background: Compositional Time Series ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* G. Athanasopoulos, R. J. Hyndman, H. Song, and D. C. Wu (2011)
  The tourism forecasting competition.
  International Journal of Forecasting 27 (3),  pp. 822–844.
  Cited by: [§7.1](https://arxiv.org/html/2601.16821v1#S7.SS1.p1.1 "7.1 Data and Context ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* J. Bai and P. Perron (2003)
  Computation and analysis of multiple structural change models.
  Journal of Applied Econometrics 18 (1),  pp. 1–22.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* C. Barceló-Vidal, L. Aguilar, and J. A. Martín-Fernández (2011)
  Compositional VARIMA time series.
  In Compositional Data Analysis: Theory and Applications,
   pp. 87–103.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p2.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* M. A. Benjamin, R. A. Rigby, and D. M. Stasinopoulos (2003)
  Generalized autoregressive moving average models.
  Journal of the American Statistical association 98 (461),  pp. 214–223.
  Cited by: [§2](https://arxiv.org/html/2601.16821v1#S2.p3.2 "2 Background: Compositional Time Series ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* G. E. P. Box and G. C. Tiao (1975)
  Intervention analysis with applications to economic and environmental problems.
  Journal of the American Statistical Association 70 (349),  pp. 70–79.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p5.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* K. H. Brodersen, F. Gallusser, J. Koehler, N. Remy, and S. L. Scott (2015)
  Inferring causal impact using Bayesian structural time-series models.
  The Annals of Applied Statistics 9 (1),  pp. 247–274.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p5.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* B. Carpenter, A. Gelman, M. D. Hoffman, D. Lee, B. Goodrich, M. Betancourt, M. Brubaker, J. Guo, P. Li, and A. Riddell (2017)
  Stan: a probabilistic programming language.
  Journal of Statistical Software 76 (1).
  External Links: [Document](https://dx.doi.org/10.18637/jss.v076.i01)
  Cited by: [§4](https://arxiv.org/html/2601.16821v1#S4.SS0.SSS0.Px3.p1.1 "Computation. ‣ 4 Prior Specification and Computation ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* R. A. Davis, W. T. M. Dunsmuir, and S. B. Streett (2003)
  Observation-driven models for Poisson counts.
  Biometrika 90 (4),  pp. 777–790.
  Cited by: [§3.5](https://arxiv.org/html/2601.16821v1#S3.SS5.p4.2 "3.5 Full Model Specification ‣ 3 Directional-Shift Intervention Model ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* B. Deyá-Tortella, V. Leoni, and V. Ramos (2022)
  COVID-led consumption displacement: a longitudinal analysis of hotel booking patterns.
  International Journal of Hospitality Management 107,  pp. 103343.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijhm.2022.103343)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* J. J. Egozcue, V. Pawlowsky-Glahn, G. Mateu-Figueras, and C. Barceló-Vidal (2003)
  Isometric logratio transformations for compositional data.
  Mathematical Geology 35 (3),  pp. 279–300.
  Cited by: [Appendix B](https://arxiv.org/html/2601.16821v1#A2.1.p1.5 "Proof. ‣ Appendix B Geodesic Property and Basis Invariance ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§1](https://arxiv.org/html/2601.16821v1#S1.p2.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§2](https://arxiv.org/html/2601.16821v1#S2.p2.7 "2 Background: Compositional Time Series ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* R. Fildes, S. Ma, and S. Kolassa (2022)
  Retail forecasting: research and practice.
  International Journal of Forecasting 38 (4),  pp. 1283–1318.
  Note: Special Issue: M5 competition
  External Links: ISSN 0169-2070,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.ijforecast.2019.06.004),
  [Link](https://www.sciencedirect.com/science/article/pii/S016920701930192X)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* T. J. Fisher, J. Zhang, S. P. Colegate, and M. J. Vanni (2022)
  Detecting and modeling changes in a time series of proportions.
  The Annals of Applied Statistics 16 (1),  pp. 477–494.
  External Links: [Document](https://dx.doi.org/10.1214/21-AOAS1509)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§1](https://arxiv.org/html/2601.16821v1#S1.p5.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* T. Gneiting and A. E. Raftery (2007)
  Strictly proper scoring rules, prediction, and estimation.
  Journal of the American Statistical Association 102 (477),  pp. 359–378.
  Cited by: [§6](https://arxiv.org/html/2601.16821v1#S6.p1.1 "6 Forecasting ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* S. Gössling, D. Scott, and C. M. Hall (2020)
  Pandemics, tourism and global change: a rapid assessment of COVID-19.
  Journal of Sustainable Tourism 29 (1),  pp. 1–20.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* J. D. Hamilton (1989)
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  Econometrica 57 (2),  pp. 357–384.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* M. D. Hoffman and A. Gelman (2014)
  The No-U-Turn Sampler: adaptively setting path lengths in Hamiltonian Monte Carlo.
  Journal of Machine Learning Research 15,  pp. 1593–1623.
  Cited by: [§4](https://arxiv.org/html/2601.16821v1#S4.SS0.SSS0.Px3.p1.1 "Computation. ‣ 4 Prior Specification and Computation ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* R. J. Hyndman and G. Athanasopoulos (2021)
  Forecasting: principles and practice.
  3rd edition, OTexts.
  External Links: [Link](https://otexts.com/fpp3/)
  Cited by: [§6](https://arxiv.org/html/2601.16821v1#S6.p1.1 "6 Forecasting ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Katz, K. T. Brusch, and R. E. Weiss (2024)
  A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times.
  International Journal of Forecasting 40 (4),  pp. 1556–1567.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§2](https://arxiv.org/html/2601.16821v1#S2.p3.2 "2 Background: Compositional Time Series ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Katz and T. Maierhofer (2025)
  Forecasting the U.S. renewable-energy mix with an ALR-BDARMA compositional time-series framework.
  Forecasting 7 (4),  pp. 62.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Katz, L. Medina, and R. E. Weiss (2025a)
  Sensitivity analysis of priors in the Bayesian Dirichlet auto-regressive moving average model.
  Forecasting 7 (3),  pp. 32.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Katz, E. Savage, and P. Coles (2025b)
  Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022).
  Annals of Tourism Research Empirical Insights 6 (2),  pp. 100185.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Katz and E. Savage (2025)
  Slomads rising: structural shifts in U.S. Airbnb stay lengths during and after the pandemic (2019–2024).
  Tourism and Hospitality 6 (4),  pp. 182.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Katz and R. E. Weiss (2025)
  A bayesian dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares.
  External Links: 2507.14132,
  [Link](https://arxiv.org/abs/2507.14132)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Katz (2025)
  Centered ma dirichlet arma for financial compositions: theory & empirical evidence.
  External Links: 2510.18903,
  [Link](https://arxiv.org/abs/2510.18903)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* M. Lanne and S. Virolainen (2025)
  A gaussian smooth transition vector autoregressive model: an application to the macroeconomic effects of severe weather shocks.
  Journal of Economic Dynamics and Control 178,  pp. 105162.
  External Links: ISSN 0165-1889,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.jedc.2025.105162),
  [Link](https://www.sciencedirect.com/science/article/pii/S0165188925001289)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p5.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Lütkepohl (2005)
  New introduction to multiple time series analysis.
   Springer.
  Cited by: [§4](https://arxiv.org/html/2601.16821v1#S4.SS0.SSS0.Px2.p1.8 "Priors. ‣ 4 Prior Specification and Computation ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* R. Luukkonen, P. Saikkonen, and T. Teräsvirta (1988)
  Testing linearity against smooth transition autoregressive models.
  Biometrika 75 (3),  pp. 491–499.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p7.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* J. A. Martín-Fernández, C. Barceló-Vidal, and V. Pawlowsky-Glahn (2003)
  Dealing with zeros and missing values in compositional data sets using nonparametric imputation.
  Mathematical Geology 35 (3),  pp. 253–278.
  Cited by: [Appendix E](https://arxiv.org/html/2601.16821v1#A5.p1.1 "Appendix E Zero Handling ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* J. Martínez-Minaya and H. Rue (2024)
  A flexible bayesian tool for coda mixed models: logistic-normal distribution with dirichlet covariance.
  Statistics and Computing 34,  pp. 116.
  External Links: [Document](https://dx.doi.org/10.1007/s11222-024-10427-3)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* V. Pawlowsky-Glahn, J. J. Egozcue, and R. Tolosana-Delgado (2015)
  Modeling and analysis of compositional data.
   Wiley.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p1.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* M. Saxena, T. Chen, and J. D. Silverman (2025)
  Scalable inference for bayesian multinomial logistic-normal dynamic linear models.
  In Proceedings of Machine Learning Research,
  Vol. 258,  pp. 442–450.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* R. D. Snyder, J. K. Ord, A. B. Koehler, K. R. McLaren, and A. N. Beaumont (2017)
  Forecasting compositional time series: a state space approach.
  International Journal of Forecasting 33 (2),  pp. 502–512.
  External Links: ISSN 0169-2070,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.ijforecast.2016.11.008),
  [Link](https://www.sciencedirect.com/science/article/pii/S0169207017300043)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p2.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* H. Song and G. Li (2008)
  Tourism demand modelling and forecasting—a review of recent research.
  Tourism Management 29 (2),  pp. 203–220.
  Cited by: [§7.1](https://arxiv.org/html/2601.16821v1#S7.SS1.p1.1 "7.1 Data and Context ‣ 7 Empirical Application: Fee Recognition Lead Times During COVID-19 ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* Stan Development Team (2023)
  Stan modeling language users guide and reference manual.
  External Links: [Link](https://mc-stan.org)
  Cited by: [§4](https://arxiv.org/html/2601.16821v1#S4.SS0.SSS0.Px3.p1.1 "Computation. ‣ 4 Prior Specification and Computation ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* T. Teräsvirta (1994)
  Specification, estimation, and evaluation of smooth transition autoregressive models.
  Journal of the American Statistical Association 89 (425),  pp. 208–218.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p5.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§3.3](https://arxiv.org/html/2601.16821v1#S3.SS3.p5.1 "3.3 The Logistic Gate Function ‣ 3 Directional-Shift Intervention Model ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* C. Truong and V. Runge (2024)
  An efficient algorithm for exact segmentation of large compositional and categorical time series.
  Stat 13,  pp. e70012.
  External Links: [Document](https://dx.doi.org/10.1002/sta4.70012)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§1](https://arxiv.org/html/2601.16821v1#S1.p5.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* C. Truong, L. Oudre, and N. Vayatis (2020)
  Selective review of offline change point detection methods.
  Signal Processing 167,  pp. 107299.
  External Links: [Document](https://dx.doi.org/10.1016/j.sigpro.2019.107299)
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p4.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* D. van Dijk, T. Teräsvirta, and P. H. Franses (2002)
  Smooth transition autoregressive models—a survey of recent developments.
  Econometric Reviews 21 (1),  pp. 1–47.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p5.1 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention"),
  [§3.3](https://arxiv.org/html/2601.16821v1#S3.SS3.p5.1 "3.3 The Logistic Gate Function ‣ 3 Directional-Shift Intervention Model ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* A. Vehtari, A. Gelman, D. Simpson, B. Carpenter, and P. Bürkner (2021)
  Rank-normalization, folding, and localization: an improved R^\hat{R} for assessing convergence of MCMC.
  Bayesian Analysis 16 (2),  pp. 667–718.
  External Links: [Document](https://dx.doi.org/10.1214/20-BA1221)
  Cited by: [§4](https://arxiv.org/html/2601.16821v1#S4.SS0.SSS0.Px3.p1.1 "Computation. ‣ 4 Prior Specification and Computation ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* M. West and J. Harrison (1997)
  Bayesian forecasting and dynamic models.
  2nd edition, Springer.
  Cited by: [§6](https://arxiv.org/html/2601.16821v1#S6.p1.1 "6 Forecasting ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").
* T. Zheng and R. Chen (2017)
  Dirichlet ARMA models for compositional time series.
  Journal of Multivariate Analysis 158,  pp. 31–46.
  Cited by: [§1](https://arxiv.org/html/2601.16821v1#S1.p3.2 "1 Introduction ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention").

## Appendix A Helmert Contrast Matrix

We use a Helmert-style orthonormal contrast matrix for ILR transformation. For CC categories, 𝐕∈ℝC×(C−1)\mathbf{V}\in\mathbb{R}^{C\times(C-1)} with entries Vj,i=1/i​(i+1)V\_{j,i}=1/\sqrt{i(i+1)} for j≤ij\leq i, Vi+1,i=−i/i​(i+1)V\_{i+1,i}=-i/\sqrt{i(i+1)}, and Vj,i=0V\_{j,i}=0 for j>i+1j>i+1. This satisfies 𝐕⊤​𝐕=𝐈C−1\mathbf{V}^{\top}\mathbf{V}=\mathbf{I}\_{C-1}.

## Appendix B Geodesic Property and Basis Invariance

We establish that directional shifts in ILR space correspond to geodesics on the simplex under Aitchison geometry.

###### Proposition 1 (Geodesic motion).

Let 𝛈0∈ℝC−1\bm{\eta}\_{0}\in\mathbb{R}^{C-1} be an ILR coordinate and 𝐯∈ℝC−1\bm{v}\in\mathbb{R}^{C-1} a unit direction. The curve 𝛍​(w)=ilr−1⁡(𝛈0+w​𝐯)\bm{\mu}(w)=\operatorname{ilr}^{-1}(\bm{\eta}\_{0}+w\bm{v}) for w∈ℝw\in\mathbb{R} is a geodesic on (𝒮C,dA)(\mathcal{S}^{C},d\_{A}).

###### Proof.

The ILR transformation is an isometry between (𝒮C,dA)(\mathcal{S}^{C},d\_{A}) and (ℝC−1,∥⋅∥2)(\mathbb{R}^{C-1},\|\cdot\|\_{2}) (Egozcue et al., [2003](https://arxiv.org/html/2601.16821v1#bib.bib8 "Isometric logratio transformations for compositional data")). Geodesics in Euclidean space are straight lines. The curve 𝜼​(w)=𝜼0+w​𝒗\bm{\eta}(w)=\bm{\eta}\_{0}+w\bm{v} is a straight line in ℝC−1\mathbb{R}^{C-1}. Since isometries preserve geodesics, 𝝁​(w)=ilr−1⁡(𝜼​(w))\bm{\mu}(w)=\operatorname{ilr}^{-1}(\bm{\eta}(w)) is a geodesic on the simplex.
∎

###### Proposition 2 (Basis invariance).

Let 𝐕\mathbf{V} and 𝐕~\tilde{\mathbf{V}} be two orthonormal ILR contrast matrices related by rotation 𝐑∈O​(C−1)\mathbf{R}\in O(C-1), so 𝐕~=𝐕𝐑\tilde{\mathbf{V}}=\mathbf{V}\mathbf{R}. If (𝐯,Δ)(\bm{v},\Delta) parameterizes a shift in 𝐕\mathbf{V}-coordinates, then (𝐯~,Δ)(\tilde{\bm{v}},\Delta) with 𝐯~=𝐑⊤​𝐯\tilde{\bm{v}}=\mathbf{R}^{\top}\bm{v} parameterizes the same simplex trajectory in 𝐕~\tilde{\mathbf{V}}-coordinates.

###### Proof.

Let 𝜼=𝐕⊤​clr⁡(Y)\bm{\eta}=\mathbf{V}^{\top}\operatorname{clr}(Y) and 𝜼~=𝐕~⊤​clr⁡(Y)=𝐑⊤​𝜼\tilde{\bm{\eta}}=\tilde{\mathbf{V}}^{\top}\operatorname{clr}(Y)=\mathbf{R}^{\top}\bm{\eta}. The shifted coordinate in 𝐕\mathbf{V}-space is 𝜼+Δ​𝒗\bm{\eta}+\Delta\bm{v}. In 𝐕~\tilde{\mathbf{V}}-space, this becomes 𝐑⊤​(𝜼+Δ​𝒗)=𝜼~+Δ​𝐑⊤​𝒗=𝜼~+Δ​𝒗~\mathbf{R}^{\top}(\bm{\eta}+\Delta\bm{v})=\tilde{\bm{\eta}}+\Delta\mathbf{R}^{\top}\bm{v}=\tilde{\bm{\eta}}+\Delta\tilde{\bm{v}}. Both map to the same simplex point under ilr−1\operatorname{ilr}^{-1}.
∎

These results justify reporting direction effects in CLR space (via 𝒖=𝐕​𝒗\bm{u}=\mathbf{V}\bm{v}), which is basis-invariant since 𝐕~​𝒗~=𝐕𝐑𝐑⊤​𝒗=𝐕​𝒗\tilde{\mathbf{V}}\tilde{\bm{v}}=\mathbf{V}\mathbf{R}\mathbf{R}^{\top}\bm{v}=\mathbf{V}\bm{v}.

#### Scope of invariance.

Note that this basis invariance applies to the intervention trajectory itself. When diagonal AR/MA dynamics are used (as in our implementation), the assumption of independent evolution across ILR coordinates is basis-dependent; rotating the ILR basis would change which directions evolve independently. The full fitted model is thus not basis-invariant, though the directional shift mechanism is.

## Appendix C Prior Specification

Table [4](https://arxiv.org/html/2601.16821v1#A3.T4 "Table 4 ‣ Appendix C Prior Specification ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") summarizes the prior distributions used in all models.

Table 4: Prior distributions for model parameters.

|  |  |  |
| --- | --- | --- |
| Parameter | Prior | Description |
| *Baseline parameters* | | |
| bdb\_{d} | 𝒩​(0,2.52)\mathcal{N}(0,2.5^{2}) | ILR intercepts |
| Bd,kB\_{d,k} | 𝒩​(0,12)\mathcal{N}(0,1^{2}) | Covariate coefficients |
| Ad,dA\_{d,d} | Uniform​(−0.99,0.99)\text{Uniform}(-0.99,0.99) | AR diagonal |
| Θd,d\Theta\_{d,d} | Uniform​(−0.99,0.99)\text{Uniform}(-0.99,0.99) | MA diagonal |
| γϕ,k\gamma\_{\phi,k} | 𝒩​(0,12)\mathcal{N}(0,1^{2}) | Concentration coefficients |
| *Intervention parameters* | | |
| Δ\Delta | 𝒩​(0,1.52)\mathcal{N}(0,1.5^{2}) | Shift amplitude |
| τ\tau | 𝒩​(ℓ+2,42)\mathcal{N}(\ell+2,4^{2}) | Transition location parameter |
| κ\kappa | LogNormal​(−0.5,12)\text{LogNormal}(-0.5,1^{2}) | Transition speed |
| 𝒗\bm{v} | Uniform on hemisphere | Direction (unit vector) |
| δϕ\delta\_{\phi} | 𝒩​(0,0.52)\mathcal{N}(0,0.5^{2}) | Precision shift |

The hemisphere constraint on 𝒗\bm{v} resolves sign ambiguity by requiring v1≥0v\_{1}\geq 0; see Section [4](https://arxiv.org/html/2601.16821v1#S4 "4 Prior Specification and Computation ‣ Directional-Shift Dirichlet ARMA Models for Compositional Time Series with Structural Break Intervention") for discussion.

## Appendix D Evaluation Metrics

#### Aitchison distance.

Point forecast accuracy is measured by dA​(𝝁^t,Yt)=‖clr⁡(𝝁^t)−clr⁡(Yt)‖2d\_{A}(\hat{\bm{\mu}}\_{t},Y\_{t})=\|\operatorname{clr}(\hat{\bm{\mu}}\_{t})-\operatorname{clr}(Y\_{t})\|\_{2}, where 𝝁^t\hat{\bm{\mu}}\_{t} is the posterior mean of the Dirichlet mean parameter.

#### Energy score.

The energy score generalizes CRPS to multivariate settings. We compute it in Aitchison geometry:

|  |  |  |
| --- | --- | --- |
|  | ES​(F,Y)=𝔼F​[dA​(Y~,Y)]−12​𝔼F​[dA​(Y~,Y~′)]\text{ES}(F,Y)=\mathbb{E}\_{F}[d\_{A}(\tilde{Y},Y)]-\tfrac{1}{2}\mathbb{E}\_{F}[d\_{A}(\tilde{Y},\tilde{Y}^{\prime})] |  |

where Y~,Y~′\tilde{Y},\tilde{Y}^{\prime} are independent draws from the posterior predictive FF and YY is the observation. Lower is better.

#### Plug-in log score.

We report the log predictive density evaluated at posterior mean parameters: log⁡p​(Yt∣𝝁^t,λ^t)=log⁡Dirichlet⁡(Yt;λ^t​𝝁^t)\log p(Y\_{t}\mid\hat{\bm{\mu}}\_{t},\hat{\lambda}\_{t})=\log\operatorname{Dirichlet}(Y\_{t};\hat{\lambda}\_{t}\hat{\bm{\mu}}\_{t}). This plug-in approximation to the full log posterior predictive density is computationally convenient and provides a useful comparison metric, though it does not account for parameter uncertainty. Higher is better.

#### Coverage.

We report marginal (componentwise) coverage: the proportion of observations falling within 80% posterior predictive intervals, averaged across components. This measures calibration for each component separately rather than joint coverage of the entire composition vector. Nominal coverage is 80%.

#### Mean absolute error.

Componentwise absolute error between the posterior mean μ^t,c\hat{\mu}\_{t,c} and observed Yt,cY\_{t,c}, averaged across components and forecast cases: MAE=1n​C​∑t,c|μ^t,c−Yt,c|\text{MAE}=\frac{1}{nC}\sum\_{t,c}|\hat{\mu}\_{t,c}-Y\_{t,c}|.

## Appendix E Zero Handling

The Dirichlet distribution requires strictly positive components. In our application, all observed compositions have positive entries; no zero proportions occur in the aggregated monthly data. For applications where zeros may arise, standard approaches include additive replacement (Martín-Fernández et al., [2003](https://arxiv.org/html/2601.16821v1#bib.bib14 "Dealing with zeros and missing values in compositional data sets using nonparametric imputation")) or multiplicative replacement prior to analysis. Our implementation applies a numerical floor of 10−810^{-8} and renormalizes as a precaution, though this is not binding for this dataset.