---
authors:
- Harrison Katz
doc_id: arxiv:2602.18358v1
family_id: arxiv:2602.18358
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian
  Compositional Time Series Approach Using Platform Booking Data'
url_abs: http://arxiv.org/abs/2602.18358v1
url_html: https://arxiv.org/html/2602.18358v1
venue: arXiv q-fin
version: 1
year: 2026
---


Harrison E. Katz
[harrison.katz@airbnb.com](mailto:harrison.katz@airbnb.com)
Data Science, Forecasting, Airbnb Inc., San Francisco, CA, USA

###### Abstract

Understanding how the composition of guest origin markets evolves over time is critical for destination marketing organizations, hospitality businesses, and tourism planners. We develop and apply Bayesian Dirichlet autoregressive moving average (BDARMA) models to forecast the compositional dynamics of guest origin market shares using proprietary Airbnb booking data spanning 2017–2024 across four major destination regions. Our analysis reveals substantial pandemic-induced structural breaks in origin composition, with heterogeneous recovery patterns across markets. The BDARMA framework achieves the lowest average forecast error across all destination regions, outperforming standard benchmarks including naïve forecasts, exponential smoothing, and SARIMA on log-ratio transformed data. For EMEA destinations, BDARMA achieves 23% lower forecast error than naïve methods, with statistically significant improvements. By modeling compositions directly on the simplex with a Dirichlet likelihood and incorporating seasonal variation in both mean and precision parameters, our approach produces coherent forecasts that respect the unit-sum constraint while capturing complex temporal dependencies. The methodology provides destination stakeholders with probabilistic forecasts of source market shares, enabling more informed strategic planning for marketing resource allocation, infrastructure investment, and crisis response.

###### keywords:

Compositional time series , Tourism demand forecasting , Bayesian methods , Dirichlet distribution , Airbnb , Source markets , COVID-19

††journal: Tourism Management

## 1 Introduction

Tourism demand forecasting has long been recognized as essential for destination planning, resource allocation, and strategic decision-making (Song et al., [2019](https://arxiv.org/html/2602.18358v1#bib.bib1 "A review of research on tourism demand forecasting: launching the annals of tourism research curated collection on tourism demand forecasting"); Li et al., [2005](https://arxiv.org/html/2602.18358v1#bib.bib2 "Tourism demand forecasting: a time varying parameter error correction model"); Witt and Witt, [1995](https://arxiv.org/html/2602.18358v1#bib.bib3 "Forecasting tourism demand: a review of empirical research")). Accurate forecasts enable destination marketing organizations (DMOs) to optimize promotional spending across source markets, allow hospitality businesses to adjust pricing and staffing, and help policymakers anticipate infrastructure needs (Song and Li, [2008](https://arxiv.org/html/2602.18358v1#bib.bib4 "Tourism demand modelling and forecasting: a review of recent research"); Assaf et al., [2019](https://arxiv.org/html/2602.18358v1#bib.bib5 "Modeling and forecasting regional tourism demand using the bayesian global vector autoregressive (bgvar) model")). While the tourism forecasting literature is extensive, the vast majority of studies focus on predicting aggregate arrivals or total expenditure (Jiao and Chen, [2019](https://arxiv.org/html/2602.18358v1#bib.bib6 "Tourism forecasting: a review of methodological developments over the last decade"); Wu et al., [2017](https://arxiv.org/html/2602.18358v1#bib.bib7 "New developments in tourism and hotel demand modeling and forecasting")). Considerably less attention has been paid to forecasting the *composition* of tourism demand—that is, how the mix of visitors from different origin markets evolves over time.

The composition of inbound tourism matters for several reasons. First, visitors from different source markets exhibit distinct spending patterns, length-of-stay distributions, and seasonal preferences (Wu et al., [2011](https://arxiv.org/html/2602.18358v1#bib.bib8 "Analyzing and forecasting tourism demand in asia and the pacific"); Divisekera, [2003](https://arxiv.org/html/2602.18358v1#bib.bib9 "A model of demand for international tourism")). Second, the marketing channels and messaging that resonate with travelers vary substantially across cultures and geographies (Song and Li, [2008](https://arxiv.org/html/2602.18358v1#bib.bib4 "Tourism demand modelling and forecasting: a review of recent research")). Third, geopolitical events, exchange rate fluctuations, and public health crises affect origin markets asymmetrically, as demonstrated vividly during the COVID-19 pandemic (Gössling et al., [2020](https://arxiv.org/html/2602.18358v1#bib.bib11 "Pandemics, tourism and global change: a rapid assessment of covid-19"); Sigala, [2020](https://arxiv.org/html/2602.18358v1#bib.bib12 "Tourism and covid-19: impacts and implications for advancing and resetting industry and research")). Understanding and forecasting compositional shifts is therefore crucial for agile destination management.

From a methodological standpoint, market share data are *compositional*: the shares of all origin markets must sum to unity, and each share is bounded between zero and one. Standard time series methods that ignore these constraints can produce incoherent forecasts—for example, predicted shares that sum to more than 100% or take negative values (Aitchison, [1986](https://arxiv.org/html/2602.18358v1#bib.bib13 "The statistical analysis of compositional data"); Pawlowsky-Glahn et al., [2015](https://arxiv.org/html/2602.18358v1#bib.bib14 "Modeling and analysis of compositional data")). The compositional data analysis literature, pioneered by Aitchison ([1982](https://arxiv.org/html/2602.18358v1#bib.bib15 "The statistical analysis of compositional data")), offers principled approaches based on log-ratio transformations that map the simplex to unconstrained Euclidean space. However, transformed approaches can obscure interpretability and may perform poorly when shares approach zero (Greenacre, [2021](https://arxiv.org/html/2602.18358v1#bib.bib16 "Compositional data analysis")).

An alternative paradigm models compositions directly using the Dirichlet distribution, which has support on the simplex and naturally enforces the unit-sum constraint. Recent advances in Bayesian compositional time series have made this approach increasingly practical. The Katz framework (Katz et al., [2024](https://arxiv.org/html/2602.18358v1#bib.bib17 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")) introduced Bayesian Dirichlet Autoregressive Moving Average (BDARMA) models for forecasting lead time distributions in the hospitality industry, demonstrating superior performance relative to both frequentist Dirichlet ARMA and transformed Gaussian approaches. Extensions have addressed time-varying volatility through Dirichlet ARCH components (Katz and Weiss, [2025](https://arxiv.org/html/2602.18358v1#bib.bib18 "A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares")), centered moving average formulations that improve numerical stability (Katz, [2025](https://arxiv.org/html/2602.18358v1#bib.bib19 "Centered MA Dirichlet ARMA for financial compositions: theory & empirical evidence")), and renewable energy mix forecasting (Katz and Maierhofer, [2025](https://arxiv.org/html/2602.18358v1#bib.bib21 "Forecasting the U.S. renewable-energy mix with an ALR-BDARMA compositional time-series framework")). Software implementation is available in the darma R package (Katz, [2024](https://arxiv.org/html/2602.18358v1#bib.bib46 "Darma: Bayesian Dirichlet ARMA models for compositional time series")).

This paper contributes to both the tourism forecasting and compositional time series literatures by developing and applying BDARMA models to forecast guest origin market shares using large-scale platform booking data. We analyze Airbnb reservations from 2017 to 2024 across four major destination regions (EMEA, North America, Asia-Pacific, and Latin America), providing what is, to our knowledge, the first application of Bayesian compositional time series methods to tourism source market forecasting.

Our empirical setting offers several advantages. First, Airbnb operates globally with standardized data collection, enabling consistent measurement across diverse markets. Second, platform booking data captures actual reservations rather than survey-based intentions or aggregate border crossing statistics, providing a direct measure of revealed demand. Third, our sample period spans the COVID-19 pandemic and subsequent recovery, allowing us to examine how compositional dynamics shifted during and after this unprecedented disruption. Prior work using Airbnb data has documented pandemic-induced changes in booking lead times (Katz et al., [2025b](https://arxiv.org/html/2602.18358v1#bib.bib22 "Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022)")) and length of stay distributions (Katz and Savage, [2025](https://arxiv.org/html/2602.18358v1#bib.bib23 "Slomads rising: structural shifts in U.S. Airbnb stay lengths during and after the pandemic (2019–2024)")), but the evolution of origin market composition has not been systematically analyzed.

We find that BDARMA models achieve the lowest average forecast error across all destination regions, substantially outperforming standard benchmarks in forecasting origin market shares. The pandemic caused dramatic compositional shifts—most notably a surge in within-region bookings at the expense of long-haul travel—with recovery trajectories that varied markedly across destination regions. Our models capture these dynamics through autoregressive and moving average terms that allow past compositions and shocks to influence current shares, while the Dirichlet likelihood ensures forecasts remain valid probability distributions. A key methodological finding is that incorporating seasonal variation in the precision parameter—not just the mean composition—substantially improves forecast accuracy.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2602.18358v1#S2 "2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") reviews related work on tourism demand forecasting, compositional data analysis, and peer-to-peer accommodation research. Section [3](https://arxiv.org/html/2602.18358v1#S3 "3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") presents the BDARMA modeling framework and estimation approach. Section [4](https://arxiv.org/html/2602.18358v1#S4 "4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") describes our Airbnb booking data and the construction of origin market compositions. Section [5](https://arxiv.org/html/2602.18358v1#S5 "5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") reports empirical findings, including model comparisons and forecast accuracy assessments. Section [6](https://arxiv.org/html/2602.18358v1#S6 "6 Discussion ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") discusses implications for destination management and directions for future research. Section [7](https://arxiv.org/html/2602.18358v1#S7 "7 Conclusion ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") concludes.

## 2 Literature Review

### 2.1 Tourism Demand Forecasting

Tourism demand forecasting has attracted substantial scholarly attention over the past three decades (Song et al., [2019](https://arxiv.org/html/2602.18358v1#bib.bib1 "A review of research on tourism demand forecasting: launching the annals of tourism research curated collection on tourism demand forecasting"); Li et al., [2005](https://arxiv.org/html/2602.18358v1#bib.bib2 "Tourism demand forecasting: a time varying parameter error correction model")). Early work relied primarily on econometric models—autoregressive distributed lag (ADL) specifications, error correction models, and time-varying parameter approaches—to relate arrivals or expenditure to economic determinants such as income, prices, and exchange rates (Song and Li, [2008](https://arxiv.org/html/2602.18358v1#bib.bib4 "Tourism demand modelling and forecasting: a review of recent research"); Witt and Witt, [1995](https://arxiv.org/html/2602.18358v1#bib.bib3 "Forecasting tourism demand: a review of empirical research")). Song and Li ([2011](https://arxiv.org/html/2602.18358v1#bib.bib41 "Tourism demand forecasting: a review of empirical research")) and Li et al. ([2006](https://arxiv.org/html/2602.18358v1#bib.bib42 "Time varying parameter and fixed parameter linear aids: an application to tourism demand forecasting")) demonstrated that incorporating cointegration and allowing for structural change improves forecast accuracy.

More recent contributions have embraced machine learning and big data. Li et al. ([2020](https://arxiv.org/html/2602.18358v1#bib.bib10 "Forecasting tourism demand with multisource big data")) showed that search query data from Google Trends can enhance short-term arrival forecasts. Wen et al. ([2019](https://arxiv.org/html/2602.18358v1#bib.bib44 "Forecasting tourist arrivals using time series, artificial neural networks, and multivariate adaptive regression splines: evidence from china")) developed hybrid models combining ARIMA with neural networks, while Assaf et al. ([2019](https://arxiv.org/html/2602.18358v1#bib.bib5 "Modeling and forecasting regional tourism demand using the bayesian global vector autoregressive (bgvar) model")) introduced Bayesian global vector autoregression (BGVAR) to capture spillovers across regional tourism markets. The tourism forecasting competition (Athanasopoulos et al., [2011](https://arxiv.org/html/2602.18358v1#bib.bib43 "The tourism forecasting competition")) provided a systematic comparison of methods, finding that simple benchmarks often remain competitive with more complex approaches.

Despite this rich literature, forecasting the *composition* of tourism demand—as opposed to aggregate levels—has received limited attention. A notable exception is the almost ideal demand system (AIDS) approach (Wu et al., [2011](https://arxiv.org/html/2602.18358v1#bib.bib8 "Analyzing and forecasting tourism demand in asia and the pacific"); Li et al., [2006](https://arxiv.org/html/2602.18358v1#bib.bib42 "Time varying parameter and fixed parameter linear aids: an application to tourism demand forecasting")), which models budget shares allocated to different tourism products or destinations. However, AIDS models focus on expenditure allocation rather than visitor origin shares, and their linear functional form does not naturally enforce simplex constraints.

### 2.2 Compositional Data Analysis

Compositional data—observations that represent parts of a whole and thus sum to a constant—arise throughout the sciences (Aitchison, [1986](https://arxiv.org/html/2602.18358v1#bib.bib13 "The statistical analysis of compositional data")). The standard approach transforms compositions via log-ratios (additive, centered, or isometric) to map the simplex to Euclidean space, after which conventional multivariate methods apply (Egozcue et al., [2003](https://arxiv.org/html/2602.18358v1#bib.bib24 "Isometric logratio transformations for compositional data analysis"); Pawlowsky-Glahn et al., [2015](https://arxiv.org/html/2602.18358v1#bib.bib14 "Modeling and analysis of compositional data")). For time series, this enables the use of vector autoregression (VAR) and related models on transformed data (Kynčlová et al., [2015](https://arxiv.org/html/2602.18358v1#bib.bib25 "Modeling compositional time series with vector autoregressive models")).

An alternative approach models compositions directly using distributions supported on the simplex. The Dirichlet distribution is the canonical choice, parameterized by a concentration vector 𝜶=(α1,…,αC)\boldsymbol{\alpha}=(\alpha\_{1},\ldots,\alpha\_{C}) with αc>0\alpha\_{c}>0. Grunwald et al. ([1993](https://arxiv.org/html/2602.18358v1#bib.bib26 "Time series of continuous proportions")) proposed Bayesian state-space models for continuous proportions, while Zheng and Cadigan ([2017](https://arxiv.org/html/2602.18358v1#bib.bib27 "Dirichlet arma models for compositional time series")) developed frequentist Dirichlet ARMA models. More recently, Katz et al. ([2024](https://arxiv.org/html/2602.18358v1#bib.bib17 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")) introduced the Bayesian Dirichlet ARMA (BDARMA) framework, which combines the Dirichlet likelihood with vector autoregressive moving average (VARMA) dynamics on the mean parameters. Extensions include volatility clustering via Dirichlet ARCH (Katz and Weiss, [2025](https://arxiv.org/html/2602.18358v1#bib.bib18 "A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares")) and extensive prior sensitivity analysis (Katz et al., [2025a](https://arxiv.org/html/2602.18358v1#bib.bib20 "Sensitivity analysis of priors in the Bayesian Dirichlet auto-regressive moving average model")).

The BDARMA framework offers several advantages for tourism applications. First, forecasts automatically satisfy simplex constraints without post-hoc normalization. Second, the Dirichlet concentration parameter provides a natural measure of forecast uncertainty—lower concentration implies greater dispersion across possible compositions. Third, the Bayesian approach yields full posterior predictive distributions, enabling probabilistic statements about future market shares.

### 2.3 Peer-to-Peer Accommodation and Platform Data

The rise of peer-to-peer (P2P) accommodation platforms, particularly Airbnb, has transformed the hospitality landscape and generated a substantial research literature (Guttentag, [2015](https://arxiv.org/html/2602.18358v1#bib.bib28 "Airbnb: disruptive innovation and the rise of an informal tourism accommodation sector"); Dolnicar, [2019](https://arxiv.org/html/2602.18358v1#bib.bib29 "A review of research into paid online peer-to-peer accommodation: launching the annals of tourism research curated collection on peer-to-peer accommodation"); Hall and Gössling, [2022](https://arxiv.org/html/2602.18358v1#bib.bib30 "Airbnb and the sharing economy: a review")). Studies have examined Airbnb’s competitive effects on hotels (Zervas et al., [2017](https://arxiv.org/html/2602.18358v1#bib.bib31 "The rise of the sharing economy: estimating the impact of airbnb on the hotel industry")), and implications for destination governance (Nieuwland and Van Melik, [2020](https://arxiv.org/html/2602.18358v1#bib.bib33 "Regulating airbnb: how cities deal with perceived negative externalities of short-term rentals")).

Platform data offer unique advantages for tourism research. Unlike official statistics that rely on border crossings or accommodation surveys, booking data capture actual reservations with precise timing and geographic detail. Several recent studies have leveraged Airbnb data to examine pandemic-era disruptions. Katz et al. ([2025b](https://arxiv.org/html/2602.18358v1#bib.bib22 "Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022)")) analyzed booking lead time distributions across major U.S. cities, finding a two-phase pattern of pandemic disruption followed by incomplete recovery. Katz and Savage ([2025](https://arxiv.org/html/2602.18358v1#bib.bib23 "Slomads rising: structural shifts in U.S. Airbnb stay lengths during and after the pandemic (2019–2024)")) documented a structural shift toward longer stays, with the share of month-plus bookings nearly doubling during COVID restrictions and remaining elevated thereafter. Sainaghi and Mauri ([2022](https://arxiv.org/html/2602.18358v1#bib.bib34 "The effects of the covid-19 crisis on airbnb: a demand-side perspective")) examined revenue impacts in Milan.

Our study contributes to this literature by examining a previously unexplored dimension of platform booking data: the evolving composition of guest origin markets. Understanding where guests come from—and how this mix changes over time—is fundamental for destination marketing yet has not been systematically analyzed at scale.

## 3 Methodology

### 3.1 The BDARMA Model

Let 𝐲t=(yt,1,…,yt,C)⊤\mathbf{y}\_{t}=(y\_{t,1},\ldots,y\_{t,C})^{\top} denote the vector of origin market shares at time tt, where yt,c≥0y\_{t,c}\geq 0 and ∑c=1Cyt,c=1\sum\_{c=1}^{C}y\_{t,c}=1. We model 𝐲t\mathbf{y}\_{t} as Dirichlet distributed conditional on time-varying parameters:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐲t∣𝝁t,ϕt∼Dirichlet​(ϕt​𝝁t),\mathbf{y}\_{t}\mid\boldsymbol{\mu}\_{t},\phi\_{t}\sim\text{Dirichlet}(\phi\_{t}\boldsymbol{\mu}\_{t}), |  | (1) |

where 𝝁t=(μt,1,…,μt,C)⊤\boldsymbol{\mu}\_{t}=(\mu\_{t,1},\ldots,\mu\_{t,C})^{\top} is the mean composition satisfying ∑c=1Cμt,c=1\sum\_{c=1}^{C}\mu\_{t,c}=1, and ϕt>0\phi\_{t}>0 is the precision (concentration) parameter. Under this parameterization, 𝔼​[𝐲t]=𝝁t\mathbb{E}[\mathbf{y}\_{t}]=\boldsymbol{\mu}\_{t} and Var​(yt,c)=μt,c​(1−μt,c)/(1+ϕt)\text{Var}(y\_{t,c})=\mu\_{t,c}(1-\mu\_{t,c})/(1+\phi\_{t}).

To model temporal dynamics, we work with the isometric log-ratio (ILR) transformation of the mean:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜼t=ILR​(𝝁t)=𝐕⊤​log⁡(𝝁t),\boldsymbol{\eta}\_{t}=\text{ILR}(\boldsymbol{\mu}\_{t})=\mathbf{V}^{\top}\log(\boldsymbol{\mu}\_{t}), |  | (2) |

where 𝐕\mathbf{V} is a (C×C−1)(C\times C-1) contrast matrix satisfying 𝐕⊤​𝐕=𝐈C−1\mathbf{V}^{\top}\mathbf{V}=\mathbf{I}\_{C-1} and 𝐕⊤​𝟏C=𝟎\mathbf{V}^{\top}\mathbf{1}\_{C}=\mathbf{0}. The ILR transformation maps the CC-part simplex to ℝC−1\mathbb{R}^{C-1} while preserving the geometry of compositional data (Egozcue et al., [2003](https://arxiv.org/html/2602.18358v1#bib.bib24 "Isometric logratio transformations for compositional data analysis")). The inverse transformation recovers 𝝁t\boldsymbol{\mu}\_{t} via the generalized softmax.

The BDARMA(P,Q)(P,Q) specification models 𝜼t\boldsymbol{\eta}\_{t} as a VARMA process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜼t=𝐗t​𝜷+∑p=1P𝐀p​(𝜼t−p−𝐗t−p​𝜷)+∑q=1Q𝐁q​ϵ~t−q,\boldsymbol{\eta}\_{t}=\mathbf{X}\_{t}\boldsymbol{\beta}+\sum\_{p=1}^{P}\mathbf{A}\_{p}(\boldsymbol{\eta}\_{t-p}-\mathbf{X}\_{t-p}\boldsymbol{\beta})+\sum\_{q=1}^{Q}\mathbf{B}\_{q}\tilde{\boldsymbol{\epsilon}}\_{t-q}, |  | (3) |

where 𝐗t\mathbf{X}\_{t} is a covariate matrix (including Fourier terms for seasonality), 𝜷\boldsymbol{\beta} contains regression coefficients, 𝐀p\mathbf{A}\_{p} are (C−1)×(C−1)(C-1)\times(C-1) autoregressive coefficient matrices, 𝐁q\mathbf{B}\_{q} are moving average coefficient matrices, and ϵ~t\tilde{\boldsymbol{\epsilon}}\_{t} are mean-centered compositional innovations. The centering adjustment, which ensures that the MA innovations have mean zero under the Dirichlet likelihood, follows Katz ([2025](https://arxiv.org/html/2602.18358v1#bib.bib19 "Centered MA Dirichlet ARMA for financial compositions: theory & empirical evidence")); technical details are provided in Appendix [A](https://arxiv.org/html/2602.18358v1#A1 "Appendix A Technical Details ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").

### 3.2 Seasonal Precision

A key modeling choice is whether the precision parameter varies over time. We allow the precision to depend on seasonal covariates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡ϕt=𝐳t⊤​𝜸,\log\phi\_{t}=\mathbf{z}\_{t}^{\top}\boldsymbol{\gamma}, |  | (4) |

where 𝐳t\mathbf{z}\_{t} includes an intercept and Fourier terms (K=6K=6 harmonics) capturing monthly seasonality. This specification allows compositional volatility to vary seasonally—for example, summer months may exhibit tighter concentration around expected shares due to more predictable travel patterns, while shoulder seasons may show greater dispersion. As we demonstrate in Section [5](https://arxiv.org/html/2602.18358v1#S5 "5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"), incorporating seasonal precision substantially improves forecast accuracy compared to constant-precision specifications.

### 3.3 Prior Specification

We adopt weakly informative priors: for the intercept and regression coefficients, we use βj∼Normal​(0,1)\beta\_{j}\sim\text{Normal}(0,1). For autoregressive coefficients, we place Normal​(0.5,0.3)\text{Normal}(0.5,0.3) priors on diagonal elements (reflecting typical persistence) and Normal​(0,0.2)\text{Normal}(0,0.2) on off-diagonal elements. Moving average coefficients receive Normal​(0,0.3)\text{Normal}(0,0.3) priors. The precision intercept has a Normal​(3,1)\text{Normal}(3,1) prior, implying moderate concentration, with seasonal coefficients receiving Normal​(0,0.5)\text{Normal}(0,0.5) priors.

### 3.4 Estimation

We estimate the model using Markov chain Monte Carlo (MCMC) via Stan (Carpenter et al., [2017](https://arxiv.org/html/2602.18358v1#bib.bib36 "Stan: a probabilistic programming language")), accessed through the darma R package (Katz, [2024](https://arxiv.org/html/2602.18358v1#bib.bib46 "Darma: Bayesian Dirichlet ARMA models for compositional time series")). We run four chains for 2,000 iterations each (1,000 warmup), yielding 4,000 posterior draws. Convergence is assessed via the R^\hat{R} statistic and effective sample size (Vehtari et al., [2021](https://arxiv.org/html/2602.18358v1#bib.bib37 "Rank-normalization, folding, and localization: an improved ^R for assessing convergence of mcmc")).

### 3.5 Forecasting and Evaluation

Given posterior draws of model parameters, we generate hh-step-ahead forecasts by iterating the VARMA recursion forward and sampling from the implied Dirichlet predictive distribution. Point forecasts are posterior means of the predictive composition; interval forecasts use posterior quantiles.

We evaluate forecast accuracy using multiple metrics. For point forecasts, we compute the mean absolute error (MAE) averaged across components. We also report Aitchison distance, a proper metric for compositional data (Aitchison et al., [1992](https://arxiv.org/html/2602.18358v1#bib.bib39 "On criteria for measures of compositional difference")), and the log predictive density (LPD) for probabilistic calibration assessment (Gneiting and Raftery, [2007](https://arxiv.org/html/2602.18358v1#bib.bib40 "Strictly proper scoring rules, prediction, and estimation")).

We compare BDARMA against several benchmarks: (i) naïve forecasts (last observation carried forward); (ii) seasonal naïve (same month previous year); (iii) rolling mean (12-month average); (iv) exponential smoothing (ETS) on ILR-transformed series; and (v) SARIMA on ILR-transformed series. For transformed benchmarks, we apply the inverse ILR to obtain simplex-valued forecasts.

Model comparison within the BDARMA family uses leave-one-out cross-validation (LOO-CV) via Pareto-smoothed importance sampling (Vehtari et al., [2017](https://arxiv.org/html/2602.18358v1#bib.bib38 "Practical bayesian model evaluation using leave-one-out cross-validation and waic")). We report the expected log pointwise predictive density (ELPD) and effective number of parameters (ploop\_{\text{loo}}). To test whether accuracy differences between methods are statistically significant, we employ the Diebold-Mariano test (Diebold and Mariano, [1995](https://arxiv.org/html/2602.18358v1#bib.bib47 "Comparing predictive accuracy")) with a heteroskedasticity and autocorrelation consistent variance estimator; details are provided in Appendix [A](https://arxiv.org/html/2602.18358v1#A1 "Appendix A Technical Details ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").

## 4 Data

### 4.1 Airbnb Booking Data

Our analysis uses reservation data from Airbnb’s global platform spanning January 2017 through December 2024. Airbnb is one of the world’s largest peer-to-peer accommodation marketplaces, operating in over 220 countries and regions with more than 8 million active listings (Airbnb, Inc., [2025](https://arxiv.org/html/2602.18358v1#bib.bib35 "Airbnb Q4 2024 shareholder letter")). The platform’s standardized booking infrastructure enables consistent measurement of guest origin and destination across diverse markets.

We extract all confirmed reservations (excluding cancellations) from Airbnb’s internal bookings database. Each reservation record includes the booking date, guest country of residence, and listing location. We aggregate daily bookings to monthly frequency to smooth high-frequency noise while preserving meaningful temporal dynamics. The full sample comprises 96 months of observations.

### 4.2 Geographic Scope

We analyze bookings into four major destination regions defined by Airbnb’s financial planning and analysis (FPA) taxonomy:

* 1.

  EMEA: Europe, Middle East, and Africa—Airbnb’s largest region by booking volume, encompassing major destinations such as France, Spain, Italy, the United Kingdom, and Germany.
* 2.

  NAMER: North America—comprising the United States and Canada, with the U.S. representing the platform’s founding market.
* 3.

  APAC: Asia-Pacific (excluding mainland China)—including Australia, Japan, South Korea, and Southeast Asian markets.
* 4.

  LATAM: Latin America—spanning Mexico, Brazil, Argentina, and other Central and South American countries.

For each destination region, we compute the monthly composition of guest origin markets. Guests are assigned to origin countries based on their registered country of residence at the time of booking.

### 4.3 Origin Market Classification

To obtain interpretable compositions, we consolidate origin countries into a manageable number of categories. For each destination region, we identify the top seven origin markets by average booking share over the sample period. Markets outside the top seven are aggregated into an “Other” category. This yields eight distinct origin categories per destination region.

For interpretive convenience, we define a booking as *within-region* if the guest’s origin country falls within the same destination region (e.g., a French guest booking in Spain, both within EMEA), and *outside-region* otherwise. This distinction serves as a proxy for short-haul versus long-haul travel patterns in our subsequent analysis.

Table [1](https://arxiv.org/html/2602.18358v1#S4.T1 "Table 1 ‣ 4.3 Origin Market Classification ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") presents descriptive statistics for each destination region, including the number of observations, origin market components, and summary statistics for compositional variability.

Table 1: Descriptive Statistics by Destination Region

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EMEA | NAMER | APAC | LATAM |
| Observations | 96 | 96 | 96 | 96 |
| Components | 8 | 8 | 8 | 8 |
| Top origin (avg. share) | FR (23.4%) | US (82.3%) | AU (21.2%) | BR (27.4%) |
| Second origin (avg. share) | GB (14.9%) | CA (9.6%) | KR (17.8%) | MX (19.7%) |
| Top origin share range | 0.18–0.41 | 0.75–0.90 | 0.15–0.28 | 0.20–0.33 |
| Mean autocorrelation | 0.89 | 0.94 | 0.87 | 0.91 |

### 4.4 Descriptive Patterns

Figure [1](https://arxiv.org/html/2602.18358v1#S4.F1 "Figure 1 ‣ 4.4 Descriptive Patterns ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") displays the evolution of origin market compositions over our sample period for each destination region. Several patterns emerge. First, compositions exhibit substantial temporal variation, with visible seasonal patterns (e.g., increased European travel to EMEA during summer months) and trend shifts. Second, the COVID-19 pandemic (beginning March 2020) caused dramatic compositional changes: within-region origin shares surged as international travel collapsed, particularly for long-haul markets. Third, the recovery from pandemic lows has been uneven across origin markets, with some shares returning to pre-pandemic levels while others show persistent deviations.

![Refer to caption](x1.png)


Figure 1: Guest origin market shares by destination region, January 2017–December 2024. Stacked area charts show the compositional evolution of the top seven origin markets plus “Other” for each destination. The vertical dashed line indicates March 2020 (onset of COVID-19 pandemic). Note the dramatic compositional shifts during 2020–2021, particularly the collapse of Chinese outbound travel to APAC and the surge in within-region bookings across all destinations.

The high autocorrelation coefficients (0.87–0.94 across regions) confirm substantial persistence in compositional shares, motivating autoregressive modeling. APAC exhibits the most dramatic compositional variation, with Chinese origin share dropping from approximately 25% pre-pandemic to under 5% during restrictions, with gradual recovery thereafter. NAMER shows the least compositional variation, with U.S.-origin bookings consistently dominating at 75–90% of the total.

Both the Dirichlet likelihood and ILR transformation require strictly positive compositional components. In our data, the minimum observed share across all region-month-origin combinations is 0.8%, occurring for the “Other” category in NAMER during peak U.S.-origin months. No exact zeros appear in the data, a consequence of aggregating large booking volumes (tens of thousands of reservations per month) where even small origin markets contribute positive counts. We therefore apply no zero-replacement or smoothing procedures.

### 4.5 Compositional Dynamics

To motivate our modeling choices, we examine temporal patterns in compositional variability. Figure [2](https://arxiv.org/html/2602.18358v1#S4.F2 "Figure 2 ‣ 4.5 Compositional Dynamics ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") plots the Herfindahl-Hirschman Index (HHI) of origin market concentration over time for each destination region. NAMER exhibits consistently high concentration (HHI ≈\approx 0.60–0.75), reflecting U.S. dominance, with a pandemic-induced spike to nearly 0.90 as Canadian cross-border travel collapsed. In contrast, EMEA, APAC, and LATAM maintain diverse origin portfolios (HHI ≈\approx 0.20) with only modest pandemic disruption. This heterogeneity in market structure explains why forecast method performance varies across regions: BDARMA’s ability to model compositional dynamics provides greater value where multiple origin markets compete.

![Refer to caption](x2.png)


Figure 2: Market concentration over time by destination region. The Herfindahl-Hirschman Index (HHI) measures origin market concentration, with higher values indicating dominance by fewer markets. NAMER exhibits consistently high concentration due to U.S. dominance, while EMEA maintains diverse origin portfolios. The vertical dashed line indicates March 2020.

Figure [3](https://arxiv.org/html/2602.18358v1#S4.F3 "Figure 3 ‣ 4.5 Compositional Dynamics ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") displays average autocorrelation functions of CLR-transformed shares by destination. All regions exhibit substantial persistence at short lags, with NAMER showing the slowest decay (lag-1 ACF ≈\approx 0.90) and EMEA the fastest (lag-1 ACF ≈\approx 0.70). APAC and LATAM display a secondary peak at lag 12, indicating seasonal patterns in composition. These autocorrelation structures motivate the AR(1) specification in our BDARMA models.

![Refer to caption](x3.png)


Figure 3: Average autocorrelation of CLR-transformed origin shares by destination region. All regions show substantial persistence, with NAMER exhibiting the slowest decay. The seasonal bump at lag 12 for APAC and LATAM motivates including Fourier terms for seasonality.

Critically, compositional variability itself exhibits seasonal patterns. Figure [4](https://arxiv.org/html/2602.18358v1#S4.F4 "Figure 4 ‣ 4.5 Compositional Dynamics ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") shows boxplots of Aitchison distance from the mean composition by calendar month for EMEA. Spring and early summer months (March–June) display substantially higher compositional dispersion than autumn months (September–October), with median Aitchison distances approximately 25% larger. This pattern reflects greater uncertainty in origin mix during shoulder seasons when travel patterns are less predictable compared to peak summer months when established seasonal flows dominate.

![Refer to caption](x4.png)


Figure 4: Seasonal pattern in compositional deviation for EMEA. Boxplots show Aitchison distance from mean composition by calendar month; red diamonds indicate monthly means. Spring and early summer months exhibit greater compositional dispersion than autumn, motivating the seasonal precision specification in our BDARMA models.

This empirical pattern directly motivates our seasonal precision specification: rather than assuming constant compositional volatility, we allow the Dirichlet precision parameter ϕt\phi\_{t} to vary with Fourier seasonal terms. As we demonstrate in Section [5](https://arxiv.org/html/2602.18358v1#S5 "5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"), this specification substantially improves forecast accuracy.

## 5 Results

### 5.1 Model Selection

We estimate BDARMA models with varying autoregressive (P∈{0,1,2}P\in\{0,1,2\}) and moving average (Q∈{0,1}Q\in\{0,1\}) orders for each destination region. All models use the ILR transformation and include Fourier terms (K=6K=6 harmonics) for both the mean composition and the precision parameter. Table [2](https://arxiv.org/html/2602.18358v1#S5.T2 "Table 2 ‣ 5.1 Model Selection ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") reports LOO-CV results for EMEA, our primary analysis region.

Table 2: Model Comparison via LOO-CV for EMEA

| Model | ELPD | SE | ploop\_{\text{loo}} | Δ\DeltaELPD |
| --- | --- | --- | --- | --- |
| BDARMA(1,1) | 1450.0 | 34.6 | 153.0 | 0.0 |
| BDARMA(2,1) | 1433.6 | 38.3 | 187.8 | −16.4-16.4 |
| BDARMA(2,0) | 1390.7 | 37.5 | 160.4 | −59.3-59.3 |
| BDARMA(1,0) | 1341.4 | 41.4 | 134.2 | −108.6-108.6 |
| BDARMA(0,1) | 1292.0 | 36.4 | 123.0 | −158.0-158.0 |

Note: ELPD = expected log pointwise predictive density (higher is better); ploop\_{\text{loo}} = effective number of parameters; Δ\DeltaELPD = difference from best model. All models use ILR transformation with K=6K=6 Fourier harmonics for both mean and precision.

The BDARMA(1,1) specification achieves the highest ELPD across all destination regions, indicating that both autoregressive and moving average components contribute to forecast performance. The inclusion of the MA(1) term consistently improves model fit, suggesting that compositional shocks have effects that persist beyond what the AR dynamics alone capture. Figure [5](https://arxiv.org/html/2602.18358v1#S5.F5 "Figure 5 ‣ 5.1 Model Selection ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") visualizes the LOO comparison for EMEA.

![Refer to caption](x5.png)


Figure 5: Model comparison via leave-one-out cross-validation for EMEA. Points indicate posterior mean ELPD; error bars show ±2\pm 2 standard errors. The BDARMA(1,1) specification achieves the highest expected log predictive density.

### 5.2 Forecast Accuracy

We evaluate forecast accuracy using rolling origin evaluation with a 3-month forecast horizon. Rolling origins begin in January 2022 and proceed in 3-month increments through October 2024, yielding 15 forecast origins with 45 total forecast observations per destination.

Table [3](https://arxiv.org/html/2602.18358v1#S5.T3 "Table 3 ‣ 5.2 Forecast Accuracy ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") presents the mean absolute error (MAE) for each method across destination regions. BDARMA achieves the lowest average MAE across all destinations (0.0072), outperforming ETS (0.0073), SARIMA (0.0079), and naïve forecasts (0.0080). For EMEA, BDARMA achieves MAE of 0.0055, representing 23% lower error than naïve forecasts (0.0072) and 6% lower than SARIMA (0.0059).

Table 3: Forecast Accuracy: Mean Absolute Error by Destination Region

| Model | EMEA | NAMER | APAC | LATAM | Average |
| --- | --- | --- | --- | --- | --- |
| BDARMA (ILR) | 0.0055 | 0.0018 | 0.0122 | 0.0092 | 0.0072 |
| SARIMA (ILR) | 0.0059 | 0.0019 | 0.0154 | 0.0085 | 0.0079 |
| ETS (ILR) | 0.0066 | 0.0020 | 0.0136 | 0.0070 | 0.0073 |
| Naïve | 0.0072 | 0.0019 | 0.0124 | 0.0104 | 0.0080 |
| Rolling Mean | 0.0070 | 0.0028 | 0.0202 | 0.0106 | 0.0101 |
| Seasonal Naïve | 0.0086 | 0.0038 | 0.0326 | 0.0115 | 0.0141 |

Note: MAE computed as the mean absolute error averaged across components and forecast horizons. Bold indicates best performance for each destination and overall. Rolling evaluation uses origins from January 2022–October 2024 with 3-month forecast horizon.

The relative performance of methods varies systematically across destinations. BDARMA excels for EMEA and APAC, where compositional dynamics are rich—these regions feature multiple origin markets with shares between 5–25%, creating scope for autoregressive patterns to improve forecasts. For NAMER, where U.S.-origin bookings dominate at over 80%, the composition is nearly constant and all methods perform similarly. For LATAM, ETS achieves the lowest MAE, suggesting that smooth trend dynamics dominate the autoregressive patterns that BDARMA targets.

Figure [6](https://arxiv.org/html/2602.18358v1#S5.F6 "Figure 6 ‣ 5.2 Forecast Accuracy ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") summarizes the forecast accuracy comparison for EMEA, showing BDARMA’s consistent advantage over benchmarks.

![Refer to caption](x6.png)


Figure 6: Forecast accuracy comparison for EMEA destination. BDARMA achieves the lowest mean absolute error, followed by SARIMA and ETS. Seasonal naïve performs poorly due to pandemic-induced structural breaks that invalidate same-month-last-year patterns.

Table [4](https://arxiv.org/html/2602.18358v1#S5.T4 "Table 4 ‣ 5.2 Forecast Accuracy ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") examines forecast accuracy by horizon for EMEA. BDARMA maintains its advantage at horizons 2 and 3, with SARIMA slightly outperforming at h=1h=1.

Table 4: Forecast Accuracy by Horizon for EMEA

| Horizon | BDARMA | SARIMA | ETS | Naïve | SNaïve |
| --- | --- | --- | --- | --- | --- |
| h=1h=1 | 0.0050 | 0.0048 | 0.0051 | 0.0054 | 0.0094 |
| h=2h=2 | 0.0057 | 0.0067 | 0.0067 | 0.0075 | 0.0089 |
| h=3h=3 | 0.0058 | 0.0062 | 0.0080 | 0.0087 | 0.0074 |

Note: Bold indicates best performance at each horizon.

A notable finding is BDARMA’s strong performance in NAMER at short horizons (Table [5](https://arxiv.org/html/2602.18358v1#S5.T5 "Table 5 ‣ 5.2 Forecast Accuracy ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data")). Despite the region’s near-constant composition, BDARMA achieves the lowest MAE at h=1h=1 (0.00098) and h=2h=2 (0.00161), outperforming all benchmarks. This suggests that even in low-variation settings, the model captures subtle dynamics that simple forecasts miss.

Table 5: Forecast Accuracy by Horizon for NAMER

| Horizon | BDARMA | SARIMA | ETS | Naïve | SNaïve |
| --- | --- | --- | --- | --- | --- |
| h=1h=1 | 0.0010 | 0.0013 | 0.0010 | 0.0010 | 0.0041 |
| h=2h=2 | 0.0016 | 0.0018 | 0.0019 | 0.0019 | 0.0036 |
| h=3h=3 | 0.0028 | 0.0026 | 0.0030 | 0.0028 | 0.0038 |

Note: Bold indicates best performance at each horizon.

### 5.3 Statistical Significance

Table [6](https://arxiv.org/html/2602.18358v1#S5.T6 "Table 6 ‣ 5.3 Statistical Significance ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") reports Diebold-Mariano test results comparing BDARMA forecasts against each benchmark for EMEA. BDARMA significantly outperforms naïve forecasts (p=0.036p=0.036) and seasonal naïve (p=0.027p=0.027). The improvement over ETS is marginally significant (p=0.081p=0.081), while the comparison with SARIMA is not statistically significant (p=0.329p=0.329).

Table 6: Diebold-Mariano Tests for EMEA (H1: BDARMA has lower error)

| Comparison | DM Statistic | pp-value | Significant |
| --- | --- | --- | --- |
| BDARMA vs. Naïve | −1.84-1.84 | 0.036 | Yes |
| BDARMA vs. SNaïve | −1.99-1.99 | 0.027 | Yes |
| BDARMA vs. ETS | −1.43-1.43 | 0.081 | No |
| BDARMA vs. SARIMA | −0.45-0.45 | 0.329 | No |

Note: One-sided tests at α=0.05\alpha=0.05. See Appendix [A](https://arxiv.org/html/2602.18358v1#A1 "Appendix A Technical Details ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") for implementation details.

Across all destination regions, BDARMA significantly outperforms seasonal naïve (p<0.05p<0.05), reflecting the breakdown of annual seasonal patterns during the pandemic recovery period. For APAC, BDARMA shows marginally significant improvement over SARIMA (p=0.075p=0.075), while comparisons with naïve and ETS are not significant.

### 5.4 Forecast Visualization

Figure [7](https://arxiv.org/html/2602.18358v1#S5.F7 "Figure 7 ‣ 5.4 Forecast Visualization ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") displays BDARMA forecasts against actuals for EMEA, focusing on the four largest origin markets (France, Great Britain, Germany, and the United States). The model captures the post-pandemic recovery dynamics, with forecast intervals (80% credible regions shown as shaded bands) providing principled uncertainty quantification derived from the Dirichlet predictive distribution.

![Refer to caption](x7.png)


Figure 7: BDARMA(1,1) forecasts versus actuals for EMEA. Solid lines show historical compositions; dashed lines show point forecasts; shaded regions indicate 80% prediction intervals; points show realized values. The model captures the post-pandemic stabilization of origin market shares.

### 5.5 Component-Level Accuracy

Table [7](https://arxiv.org/html/2602.18358v1#S5.T7 "Table 7 ‣ 5.5 Component-Level Accuracy ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") reports MAE by origin market component for EMEA. BDARMA achieves the best accuracy for the three largest origin markets: France (28% improvement over naïve), Great Britain (51% improvement), and the United States (34% improvement). These substantial gains for major components drive BDARMA’s overall advantage.

Table 7: Component-Level MAE for EMEA

| Component | Naïve | SNaïve | Rolling | ETS | SARIMA | BDARMA |
| --- | --- | --- | --- | --- | --- | --- |
| FR | 0.0127 | 0.0178 | 0.0122 | 0.0148 | 0.0103 | 0.0092 |
| GB | 0.0136 | 0.0073 | 0.0075 | 0.0083 | 0.0098 | 0.0067 |
| DE | 0.0056 | 0.0063 | 0.0056 | 0.0049 | 0.0043 | 0.0053 |
| US | 0.0064 | 0.0150 | 0.0100 | 0.0069 | 0.0078 | 0.0042 |
| ES | 0.0025 | 0.0030 | 0.0025 | 0.0025 | 0.0029 | 0.0024 |
| IT | 0.0036 | 0.0030 | 0.0025 | 0.0040 | 0.0020 | 0.0032 |
| NL | 0.0030 | 0.0018 | 0.0016 | 0.0015 | 0.0021 | 0.0015 |
| Other | 0.0100 | 0.0142 | 0.0139 | 0.0097 | 0.0077 | 0.0091 |

Note: Bold indicates best performance for each component. BDARMA achieves the best MAE for four of eight components (FR, GB, US, ES, NL tied with ETS), with particularly strong gains for the three largest origin markets.

### 5.6 Pandemic Structural Break

Figure [8](https://arxiv.org/html/2602.18358v1#S5.F8 "Figure 8 ‣ 5.6 Pandemic Structural Break ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data") illustrates the pandemic’s impact on origin market compositions by plotting deviations from pre-pandemic baseline levels (January 2019–February 2020 average) for the three most-affected origin markets in each destination region. The figure reveals substantial heterogeneity in how the pandemic reshaped tourism flows.

APAC experienced the most dramatic compositional shift: Chinese outbound travel collapsed by over 30 percentage points as China maintained strict travel restrictions, while South Korean and Australian origin shares increased to partially fill the gap. EMEA saw a surge in France-origin bookings of nearly 25 percentage points during the initial lockdown period, reflecting increased within-region travel when international borders closed. NAMER, already dominated by U.S.-origin bookings, saw this dominance intensify by an additional 15 percentage points as Canadian cross-border travel declined. LATAM exhibited a temporary spike in Brazil-origin bookings followed by gradual normalization.

![Refer to caption](x8.png)


Figure 8: Pandemic impact on origin market composition by destination region. Lines show changes in market share relative to the January 2019–February 2020 baseline for the three most-affected origin markets in each region. The vertical dashed red line indicates March 2020 (WHO pandemic declaration). Note the heterogeneous responses: APAC saw Chinese share collapse by 30 percentage points; EMEA experienced a France-origin surge of 25 percentage points; NAMER’s U.S.-origin dominance intensified; LATAM showed temporary Brazil-origin gains followed by normalization.

The poor performance of seasonal naïve forecasts across all regions (Table [3](https://arxiv.org/html/2602.18358v1#S5.T3 "Table 3 ‣ 5.2 Forecast Accuracy ‣ 5 Results ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data")) reflects this structural break: using same-month-last-year values fails when the underlying compositional regime has shifted. BDARMA’s autoregressive structure allows it to adapt to the new regime while still leveraging historical patterns through the Fourier seasonal terms.

## 6 Discussion

### 6.1 Summary of Findings

Our analysis demonstrates that BDARMA models achieve the lowest average forecast error across all destination regions, with particularly strong performance for destinations exhibiting meaningful compositional dynamics. For EMEA, BDARMA achieves 23% lower forecast error than naïve methods, with statistically significant improvement (p=0.036p=0.036). The model also significantly outperforms seasonal naïve across all regions, reflecting its ability to adapt to regime changes while still capturing underlying temporal patterns.

A key methodological finding is the importance of seasonal precision. By allowing the Dirichlet concentration parameter to vary with Fourier seasonal terms, we capture the empirical pattern documented in Figure [4](https://arxiv.org/html/2602.18358v1#S4.F4 "Figure 4 ‣ 4.5 Compositional Dynamics ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"): compositional volatility differs systematically across months, with spring and early summer showing greater dispersion than autumn. This specification substantially improved forecast accuracy compared to constant-precision alternatives, particularly for NAMER and APAC where seasonal patterns in precision are pronounced.

The BDARMA(1,1) specification consistently achieves the best in-sample fit across all destination regions, as measured by LOO-CV, indicating that both autoregressive and moving average components capture important features of compositional dynamics. The relative advantage of BDARMA varies systematically with the nature of compositional variation: it excels where multiple origin markets compete with shares in the 5–25% range (EMEA, APAC), performs comparably to simpler methods where one market dominates (NAMER), and is outperformed by ETS in settings with smooth trend dynamics (LATAM). As shown in Section [4](https://arxiv.org/html/2602.18358v1#S4 "4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"), the HHI concentration analysis (Figure [2](https://arxiv.org/html/2602.18358v1#S4.F2 "Figure 2 ‣ 4.5 Compositional Dynamics ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data")) helps explain this pattern: BDARMA provides greatest value for destinations with diverse origin portfolios where compositional dynamics are meaningful.

### 6.2 Implications for Destination Management

Our findings have several practical implications for destination marketing organizations and tourism planners:

Market-specific strategies. The substantial variation in origin market compositions across destinations underscores the need for tailored marketing approaches. A one-size-fits-all strategy that allocates promotional resources uniformly across source markets will be suboptimal. BDARMA forecasts can inform more nuanced resource allocation by predicting which origin markets are likely to grow or shrink in relative importance.

Crisis response planning. The pandemic revealed how quickly origin compositions can shift when travel restrictions differentially affect source markets. Probabilistic forecasts from BDARMA models provide uncertainty quantification that supports scenario planning and stress testing. Destination managers can assess the likely range of compositional outcomes under various recovery scenarios.

Seasonality management. The Fourier terms in our BDARMA specification capture regular seasonal patterns in both origin composition and compositional volatility—for example, increased European travel to Mediterranean destinations during summer months with tighter concentration around expected patterns. Understanding these patterns enables better alignment of marketing campaigns, staffing, and infrastructure utilization with anticipated demand composition.

Long-term strategic planning. While our forecast evaluation focused on 1–3 month horizons, the BDARMA framework can generate longer-term probabilistic projections. These can inform strategic decisions about market development, language capabilities, and partnership strategies with origin-market travel intermediaries.

### 6.3 Methodological Contributions

This study makes several methodological contributions to the tourism forecasting literature:

First, we demonstrate the applicability of Bayesian compositional time series methods to tourism demand forecasting. The Dirichlet likelihood ensures coherent forecasts that respect simplex constraints, avoiding the need for post-hoc normalization or transformation back from unconstrained space.

Second, we show that modeling seasonal variation in precision—not just mean composition—substantially improves forecast accuracy. This finding has implications beyond tourism, suggesting that compositional time series models in other domains may benefit from time-varying concentration parameters.

Third, we provide a systematic comparison of BDARMA against standard benchmarks using rolling origin evaluation. The finding that BDARMA achieves the lowest average error across all destination regions, and significantly outperforms transformed approaches (ETS and SARIMA on ILR data) for EMEA, demonstrates that the direct compositional modeling approach offers practical benefits beyond theoretical elegance.

Fourth, we document the importance of the moving average component in compositional forecasting. The consistent improvement from including MA(1) terms indicates that compositional shocks have persistent effects that pure autoregressive models miss.

### 6.4 Limitations

Several limitations should be acknowledged. First, our data capture only Airbnb bookings, which represent a subset of total accommodation demand. Origin compositions may differ for hotel guests or visitors staying with friends and relatives. Second, the forecast evaluation period coincides with pandemic recovery, which may not be representative of normal forecasting conditions. Third, we do not incorporate exogenous predictors such as exchange rates, flight capacity, or visa policies, which could potentially improve forecast accuracy. Fourth, the aggregation to regional destinations obscures within-region heterogeneity that may be important for local destination managers.

### 6.5 Future Research

Several directions for future research emerge from this study:

Exogenous predictors. Incorporating covariates such as exchange rates, airline capacity, and Google search trends could improve forecast accuracy and enable scenario analysis. The BDARMA framework accommodates exogenous regressors through the 𝐗t\mathbf{X}\_{t} covariate matrix.

Finer geographic granularity. Extending the analysis to country-level or city-level destinations would support more targeted marketing decisions, though data sparsity may require hierarchical modeling approaches.

Combined volume and composition forecasts. Integrating compositional forecasts with aggregate volume forecasts would yield complete predictions of arrivals by origin market, enabling comprehensive demand planning.

Real-time implementation. Deploying BDARMA models in operational forecasting systems with automated updating would maximize practical value for destination stakeholders.

## 7 Conclusion

This paper developed and applied Bayesian Dirichlet autoregressive moving average models to forecast the evolving composition of guest origin markets using Airbnb booking data. Our analysis of 96 months of reservations across four major destination regions demonstrates that BDARMA models achieve the lowest average forecast error across all destinations, with 23% lower error than naïve methods for EMEA and significant improvements over seasonal naïve benchmarks across all regions.

The COVID-19 pandemic caused dramatic compositional shifts—most notably the collapse of Chinese outbound travel and the surge in within-region bookings—with recovery trajectories that varied markedly across regions. Our models capture these dynamics through autoregressive and moving average terms while the Dirichlet likelihood ensures forecasts remain valid probability distributions. A key finding is that incorporating seasonal variation in the precision parameter substantially improves forecast accuracy.

The methodological contribution lies in bringing recent advances in Bayesian compositional time series to tourism demand forecasting, including the novel application of seasonal precision modeling. The empirical contribution documents substantial heterogeneity in how origin market compositions evolved during and after the pandemic, with implications for destination marketing strategy.

As tourism markets continue to evolve in response to changing travel preferences, economic conditions, and potential future disruptions, robust methods for forecasting demand composition will remain essential. The BDARMA framework offers a principled, flexible approach suited to this challenge.

## Appendix A Technical Details

### A.1 Centered MA Innovations

Under the Dirichlet likelihood, the raw log-ratio residual ϵt=ILR​(𝐲t)−𝜼t\boldsymbol{\epsilon}\_{t}=\text{ILR}(\mathbf{y}\_{t})-\boldsymbol{\eta}\_{t} does not have mean zero because 𝔼​[log⁡Yc]≠log⁡𝔼​[Yc]\mathbb{E}[\log Y\_{c}]\neq\log\mathbb{E}[Y\_{c}] for Dirichlet-distributed random variables. Specifically, if 𝐘∼Dirichlet​(ϕ​𝝁)\mathbf{Y}\sim\text{Dirichlet}(\phi\boldsymbol{\mu}), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[log⁡Yc]=ψ​(ϕ​μc)−ψ​(ϕ),\mathbb{E}[\log Y\_{c}]=\psi(\phi\mu\_{c})-\psi(\phi), |  | (5) |

where ψ​(⋅)\psi(\cdot) denotes the digamma function. This bias can distort the MA dynamics if left uncorrected.

Following Katz ([2025](https://arxiv.org/html/2602.18358v1#bib.bib19 "Centered MA Dirichlet ARMA for financial compositions: theory & empirical evidence")), we use centered innovations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ~t=ILR​(𝐲t)−𝔼​[ILR​(𝐘t)∣𝝁t,ϕt],\tilde{\boldsymbol{\epsilon}}\_{t}=\text{ILR}(\mathbf{y}\_{t})-\mathbb{E}[\text{ILR}(\mathbf{Y}\_{t})\mid\boldsymbol{\mu}\_{t},\phi\_{t}], |  | (6) |

which ensures 𝔼​[ϵ~t∣𝝁t,ϕt]=𝟎\mathbb{E}[\tilde{\boldsymbol{\epsilon}}\_{t}\mid\boldsymbol{\mu}\_{t},\phi\_{t}]=\mathbf{0}. The conditional expectation is computed by applying the ILR contrast matrix to the vector of component-wise expectations (ψ​(ϕt​μt,1)−ψ​(ϕt),…,ψ​(ϕt​μt,C)−ψ​(ϕt))⊤(\psi(\phi\_{t}\mu\_{t,1})-\psi(\phi\_{t}),\ldots,\psi(\phi\_{t}\mu\_{t,C})-\psi(\phi\_{t}))^{\top}.

### A.2 Diebold-Mariano Test Implementation

Let dt=L​(𝐲^t(1),𝐲t)−L​(𝐲^t(2),𝐲t)d\_{t}=L(\hat{\mathbf{y}}\_{t}^{(1)},\mathbf{y}\_{t})-L(\hat{\mathbf{y}}\_{t}^{(2)},\mathbf{y}\_{t}) denote the loss differential between two forecasting methods at time tt, where L​(⋅,⋅)L(\cdot,\cdot) is the componentwise MAE loss. The Diebold-Mariano statistic is

|  |  |  |  |
| --- | --- | --- | --- |
|  | DM=d¯σ^d,\text{DM}=\frac{\bar{d}}{\hat{\sigma}\_{d}}, |  | (7) |

where d¯=n−1​∑t=1ndt\bar{d}=n^{-1}\sum\_{t=1}^{n}d\_{t} and σ^d\hat{\sigma}\_{d} is computed using the Newey and West ([1987](https://arxiv.org/html/2602.18358v1#bib.bib48 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix")) heteroskedasticity and autocorrelation consistent (HAC) estimator with bandwidth ⌊h1/3⌋\lfloor h^{1/3}\rfloor to account for serial correlation induced by multi-step forecast errors.

With n=45n=45 forecast observations and h=3h=3 step maximum horizon, we use bandwidth 1. Given the moderate sample size, we report pp-values from the tn−1t\_{n-1} distribution rather than the asymptotic normal, following the finite-sample correction recommended by Diebold and Mariano ([1995](https://arxiv.org/html/2602.18358v1#bib.bib47 "Comparing predictive accuracy")).

## References

* Airbnb, Inc. (2025)
  Airbnb Q4 2024 shareholder letter.
  Note: Investor Relations
  External Links: [Link](https://investors.airbnb.com)
  Cited by: [§4.1](https://arxiv.org/html/2602.18358v1#S4.SS1.p1.1 "4.1 Airbnb Booking Data ‣ 4 Data ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* J. Aitchison, C. Barceló-Vidal, J. A. Martín-Fernández, and V. Pawlowsky-Glahn (1992)
  On criteria for measures of compositional difference.
  Mathematical Geology 24 (4),  pp. 365–379.
  Cited by: [§3.5](https://arxiv.org/html/2602.18358v1#S3.SS5.p2.1 "3.5 Forecasting and Evaluation ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* J. Aitchison (1982)
  The statistical analysis of compositional data.
  Journal of the Royal Statistical Society: Series B (Methodological) 44 (2),  pp. 139–160.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p3.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* J. Aitchison (1986)
  The statistical analysis of compositional data.
   Chapman and Hall.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p3.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p1.1 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* A. G. Assaf, G. Li, H. Song, and M. G. Tsionas (2019)
  Modeling and forecasting regional tourism demand using the bayesian global vector autoregressive (bgvar) model.
  Journal of Travel Research 58 (3),  pp. 383–397.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p1.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p2.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* G. Athanasopoulos, R. J. Hyndman, H. Song, and D. C. Wu (2011)
  The tourism forecasting competition.
  International Journal of Forecasting 27 (3),  pp. 822–844.
  Cited by: [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p2.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* B. Carpenter, A. Gelman, M. D. Hoffman, D. Lee, B. Goodrich, M. Betancourt, M. Brubaker, J. Guo, P. Li, and A. Riddell (2017)
  Stan: a probabilistic programming language.
  Journal of Statistical Software 76 (1),  pp. 1–32.
  Cited by: [§3.4](https://arxiv.org/html/2602.18358v1#S3.SS4.p1.1 "3.4 Estimation ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* F. X. Diebold and R. S. Mariano (1995)
  Comparing predictive accuracy.
  Journal of Business & Economic Statistics 13 (3),  pp. 253–263.
  Cited by: [§A.2](https://arxiv.org/html/2602.18358v1#A1.SS2.p2.4 "A.2 Diebold-Mariano Test Implementation ‣ Appendix A Technical Details ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§3.5](https://arxiv.org/html/2602.18358v1#S3.SS5.p4.1 "3.5 Forecasting and Evaluation ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* S. Divisekera (2003)
  A model of demand for international tourism.
  Annals of Tourism Research 30 (1),  pp. 31–49.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p2.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* S. Dolnicar (2019)
  A review of research into paid online peer-to-peer accommodation: launching the annals of tourism research curated collection on peer-to-peer accommodation.
  Annals of Tourism Research 75,  pp. 248–264.
  Cited by: [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p1.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* J. J. Egozcue, V. Pawlowsky-Glahn, G. Mateu-Figueras, and C. Barcelo-Vidal (2003)
  Isometric logratio transformations for compositional data analysis.
  Mathematical Geology 35 (3),  pp. 279–300.
  Cited by: [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p1.1 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§3.1](https://arxiv.org/html/2602.18358v1#S3.SS1.p2.7 "3.1 The BDARMA Model ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* T. Gneiting and A. E. Raftery (2007)
  Strictly proper scoring rules, prediction, and estimation.
  Journal of the American Statistical Association 102 (477),  pp. 359–378.
  Cited by: [§3.5](https://arxiv.org/html/2602.18358v1#S3.SS5.p2.1 "3.5 Forecasting and Evaluation ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* S. Gössling, D. Scott, and C. M. Hall (2020)
  Pandemics, tourism and global change: a rapid assessment of covid-19.
  Journal of Sustainable Tourism 29 (1),  pp. 1–20.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p2.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* M. Greenacre (2021)
  Compositional data analysis.
  Annual Review of Statistics and Its Application 8,  pp. 271–299.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p3.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* G. K. Grunwald, A. E. Raftery, and P. Guttorp (1993)
  Time series of continuous proportions.
  Journal of the Royal Statistical Society: Series B 55 (1),  pp. 103–116.
  Cited by: [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p2.2 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* D. Guttentag (2015)
  Airbnb: disruptive innovation and the rise of an informal tourism accommodation sector.
  Current Issues in Tourism 18 (12),  pp. 1192–1217.
  Cited by: [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p1.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* C. M. Hall and S. Gössling (2022)
  Airbnb and the sharing economy: a review.
  Current Issues in Tourism 25 (20),  pp. 3213–3232.
  External Links: [Document](https://dx.doi.org/10.1080/13683500.2022.2122418)
  Cited by: [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p1.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* E. X. Jiao and J. L. Chen (2019)
  Tourism forecasting: a review of methodological developments over the last decade.
  Tourism Economics 25 (3),  pp. 469–492.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p1.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz, K. T. Brusch, and R. E. Weiss (2024)
  A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times.
  International Journal of Forecasting 40 (4),  pp. 1556–1567.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p4.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p2.2 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz and T. Maierhofer (2025)
  Forecasting the U.S. renewable-energy mix with an ALR-BDARMA compositional time-series framework.
  Forecasting 7 (4),  pp. 62.
  External Links: [Document](https://dx.doi.org/10.3390/forecast7040062)
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p4.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz, L. Medina, and R. E. Weiss (2025a)
  Sensitivity analysis of priors in the Bayesian Dirichlet auto-regressive moving average model.
  Forecasting 7 (3),  pp. 32.
  External Links: [Document](https://dx.doi.org/10.3390/forecast7030032)
  Cited by: [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p2.2 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz, E. Savage, and P. Coles (2025b)
  Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022).
  Annals of Tourism Research Empirical Insights 6 (2),  pp. 100185.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p6.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p2.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz and E. Savage (2025)
  Slomads rising: structural shifts in U.S. Airbnb stay lengths during and after the pandemic (2019–2024).
  Tourism and Hospitality 6 (4),  pp. 182.
  External Links: [Document](https://dx.doi.org/10.3390/tourhosp6040182)
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p6.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p2.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz and R. E. Weiss (2025)
  A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares.
  arXiv preprint arXiv:2507.14132.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p4.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p2.2 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz (2024)
  Darma: Bayesian Dirichlet ARMA models for compositional time series.
  Note: R package version 0.1.0
  External Links: [Link](https://github.com/harrisonekatz/darma)
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p4.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§3.4](https://arxiv.org/html/2602.18358v1#S3.SS4.p1.1 "3.4 Estimation ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Katz (2025)
  Centered MA Dirichlet ARMA for financial compositions: theory & empirical evidence.
  External Links: 2510.18903,
  [Link](https://arxiv.org/abs/2510.18903)
  Cited by: [§A.1](https://arxiv.org/html/2602.18358v1#A1.SS1.p2.3 "A.1 Centered MA Innovations ‣ Appendix A Technical Details ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§1](https://arxiv.org/html/2602.18358v1#S1.p4.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§3.1](https://arxiv.org/html/2602.18358v1#S3.SS1.p3.8 "3.1 The BDARMA Model ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* P. Kynčlová, K. Hron, and P. Filzmoser (2015)
  Modeling compositional time series with vector autoregressive models.
  Journal of Forecasting 34 (4),  pp. 303–314.
  Cited by: [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p1.1 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* G. Li, H. Song, and S. F. Witt (2005)
  Tourism demand forecasting: a time varying parameter error correction model.
  Journal of Travel Research 44 (4),  pp. 396–405.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p1.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p1.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* G. Li, H. Song, and S. F. Witt (2006)
  Time varying parameter and fixed parameter linear aids: an application to tourism demand forecasting.
  International Journal of Forecasting 22 (1),  pp. 57–71.
  Cited by: [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p1.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p3.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* X. Li, B. Pan, R. Law, and X. Huang (2020)
  Forecasting tourism demand with multisource big data.
  Annals of Tourism Research 83,  pp. 102912.
  External Links: [Document](https://dx.doi.org/10.1016/j.annals.2020.102912)
  Cited by: [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p2.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* W. K. Newey and K. D. West (1987)
  A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix.
  Econometrica 55 (3),  pp. 703–708.
  Cited by: [§A.2](https://arxiv.org/html/2602.18358v1#A1.SS2.p1.6 "A.2 Diebold-Mariano Test Implementation ‣ Appendix A Technical Details ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* S. Nieuwland and R. Van Melik (2020)
  Regulating airbnb: how cities deal with perceived negative externalities of short-term rentals.
  Current Issues in Tourism 23 (7),  pp. 811–825.
  Cited by: [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p1.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* V. Pawlowsky-Glahn, J. J. Egozcue, and R. Tolosana-Delgado (2015)
  Modeling and analysis of compositional data.
   John Wiley & Sons.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p3.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p1.1 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* R. Sainaghi and A. Mauri (2022)
  The effects of the covid-19 crisis on airbnb: a demand-side perspective.
  Current Issues in Tourism 25 (4),  pp. 600–610.
  Cited by: [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p2.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* M. Sigala (2020)
  Tourism and covid-19: impacts and implications for advancing and resetting industry and research.
  Journal of Business Research 117,  pp. 312–321.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p2.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Song and G. Li (2008)
  Tourism demand modelling and forecasting: a review of recent research.
  Tourism Management 29 (2),  pp. 203–220.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p1.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§1](https://arxiv.org/html/2602.18358v1#S1.p2.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p1.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Song and G. Li (2011)
  Tourism demand forecasting: a review of empirical research.
  International Journal of Forecasting 27 (2),  pp. 503–528.
  Cited by: [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p1.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* H. Song, R. T. Qiu, and J. Park (2019)
  A review of research on tourism demand forecasting: launching the annals of tourism research curated collection on tourism demand forecasting.
  Annals of Tourism Research 75,  pp. 338–362.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p1.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p1.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* A. Vehtari, A. Gelman, and J. Gabry (2017)
  Practical bayesian model evaluation using leave-one-out cross-validation and waic.
  Statistics and Computing 27 (5),  pp. 1413–1432.
  Cited by: [§3.5](https://arxiv.org/html/2602.18358v1#S3.SS5.p4.1 "3.5 Forecasting and Evaluation ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* A. Vehtari, A. Gelman, D. Simpson, B. Carpenter, and P. Bürkner (2021)
  Rank-normalization, folding, and localization: an improved R^\hat{R} for assessing convergence of mcmc.
  Bayesian Analysis 16 (2),  pp. 667–718.
  Cited by: [§3.4](https://arxiv.org/html/2602.18358v1#S3.SS4.p1.1 "3.4 Estimation ‣ 3 Methodology ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* J. Wen, X. Liu, H. Qi, and T. Lockyer (2019)
  Forecasting tourist arrivals using time series, artificial neural networks, and multivariate adaptive regression splines: evidence from china.
  Tourism Management 71,  pp. 1–12.
  Cited by: [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p2.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* S. F. Witt and C. A. Witt (1995)
  Forecasting tourism demand: a review of empirical research.
  International Journal of Forecasting 11 (3),  pp. 447–475.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p1.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p1.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* D. C. Wu, G. Li, and H. Song (2011)
  Analyzing and forecasting tourism demand in asia and the pacific.
  Tourism Management 33 (6),  pp. 1489–1501.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p2.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data"),
  [§2.1](https://arxiv.org/html/2602.18358v1#S2.SS1.p3.1 "2.1 Tourism Demand Forecasting ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* D. C. Wu, H. Song, and S. Shen (2017)
  New developments in tourism and hotel demand modeling and forecasting.
  International Journal of Contemporary Hospitality Management 29 (1),  pp. 507–529.
  Cited by: [§1](https://arxiv.org/html/2602.18358v1#S1.p1.1 "1 Introduction ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* G. Zervas, D. Proserpio, and J. W. Byers (2017)
  The rise of the sharing economy: estimating the impact of airbnb on the hotel industry.
  Journal of Marketing Research 54 (5),  pp. 687–705.
  Cited by: [§2.3](https://arxiv.org/html/2602.18358v1#S2.SS3.p1.1 "2.3 Peer-to-Peer Accommodation and Platform Data ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").
* N. Zheng and N. Cadigan (2017)
  Dirichlet arma models for compositional time series.
  Journal of Multivariate Analysis 158,  pp. 31–46.
  Cited by: [§2.2](https://arxiv.org/html/2602.18358v1#S2.SS2.p2.2 "2.2 Compositional Data Analysis ‣ 2 Literature Review ‣ Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data").