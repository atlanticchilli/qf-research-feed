---
authors:
- Emma Hubert
- Dimitrios Lolas
- Ronnie Sircar
doc_id: arxiv:2601.05085v1
family_id: arxiv:2601.05085
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets'
url_abs: http://arxiv.org/abs/2601.05085v1
url_html: https://arxiv.org/html/2601.05085v1
venue: arXiv q-fin
version: 1
year: 2026
---


Emma Hubert
CEREMADE, Université Paris Dauphine & PSL Research University.
  
Dimitrios Lolas
Department of Operations Research & Financial Engineering, Princeton University.
  
Ronnie Sircar22footnotemark: 2

(January 7, 2026)

###### Abstract

We study the problem of forecasting and optimally trading day-ahead versus real-time (DART) price spreads in U.S. wholesale electricity markets. Building on the framework of
Galarneau-Vincent et al. ([2023](https://arxiv.org/html/2601.05085v1#bib.bib1 "Foreseeing the worst: forecasting electricity DART spikes")), we extend spike prediction from a single zone to a
multi-zone setting and treat both positive and negative DART spikes within a unified statistical model.
To translate directional signals into economically meaningful positions, we develop a
structural and market-consistent price impact model based on day-ahead bid stacks.
This yields closed-form expressions for the optimal vector of zonal INC/DEC quantities,
capturing asymmetric buy/sell impacts and cross-zone congestion effects. When applied to
NYISO, the resulting impact-aware strategy significantly improves the
risk–return profile relative to unit-size trading and highlights substantial heterogeneity
across markets and seasons.

## 1 Introduction

In U.S. wholesale electricity markets operated by Independent System Operators and Regional Transmission Organizations (ISOs/RTOs), trading is organized as a two-settlement system: a Day-Ahead Market (DAM), in which schedules and prices for the following operating day are determined, and a Real-Time Market (RTM), in which actual imbalances are settled at higher frequency. The difference between these two prices—the day-ahead real-time spread (DART)—is a central risk factor for both financial and physical market participants and can be interpreted as a market-implied forecast error up to an embedded risk premium Longstaff and Wang ([2004](https://arxiv.org/html/2601.05085v1#bib.bib19 "Electricity forward prices: a high-frequency empirical analysis")).
Large deviations often arise from transmission congestion, load forecast errors, unit commitment constraints, and network contingencies, and they can generate substantial profit opportunities for traders capable of anticipating extreme DART events.
Empirical works document that such extreme price movements are short-lived, clustered, and closely linked to binding network constraints and unexpected demand shocks Liebl ([2013](https://arxiv.org/html/2601.05085v1#bib.bib20 "Modeling and forecasting electricity spot prices: a functional data perspective")); Christensen et al. ([2012](https://arxiv.org/html/2601.05085v1#bib.bib21 "Forecasting spikes in electricity prices")); Nowotarski et al. ([2014](https://arxiv.org/html/2601.05085v1#bib.bib22 "An empirical comparison of alternative schemes for combining electricity spot price forecasts")); Sandhu et al. ([2016](https://arxiv.org/html/2601.05085v1#bib.bib24 "Forecasting day-ahead price spikes for the ontario electricity market")).

In NYISO (New York ISO) and ISO–NE (ISO New England), market participants may take purely financial day-ahead positions through virtual bidding.
An INC trade (virtual demand) of size q>0q>0 buys energy in the Day-Ahead Market at unit price PDAP^{\rm DA} and sells it back in the Real-Time Market at price PRTP^{\rm RT}, yielding a payoff (PRT−PDA)×q(P^{\rm RT}-P^{\rm DA})\times q, while a DEC trade (virtual supply) does the opposite, yielding (PDA−PRT)×q(P^{\rm DA}-P^{\rm RT})\times q.
Thus, the problem faced by a virtual market participant is simultaneously predictive and operational:

1. 1.

   reliably forecast where and when large DART spreads will occur, and
2. 2.

   translate these forecasts into profitable day-ahead positions under realistic market impact.

A growing literature studies DART spreads and virtual bidding from both predictive and structural perspectives, emphasizing the role of congestion, risk premia, and limits to arbitrage in two-settlement electricity markets Longstaff and Wang ([2004](https://arxiv.org/html/2601.05085v1#bib.bib19 "Electricity forward prices: a high-frequency empirical analysis")).
Early empirical work documents the prevalence and economic drivers of DART price deviations and the role of congestion and forecast errors in shaping these spreads Borenstein et al. ([2002](https://arxiv.org/html/2601.05085v1#bib.bib25 "Measuring market inefficiencies in California’s restructured wholesale electricity market")).
Subsequent studies examine the profitability and limits of virtual bidding strategies, emphasizing the importance of transaction costs, market power, and convergence effects.
More recently, machine-learning approaches have been applied to electricity price and DART forecasting, showing that extreme price dislocations can be predicted with economically meaningful accuracy Lago et al. ([2021](https://arxiv.org/html/2601.05085v1#bib.bib23 "Forecasting day-ahead electricity prices: a review of state-of-the-art algorithms, best practices and an open-access benchmark")); Galarneau-Vincent et al. ([2023](https://arxiv.org/html/2601.05085v1#bib.bib1 "Foreseeing the worst: forecasting electricity DART spikes")); Wang et al. ([2024](https://arxiv.org/html/2601.05085v1#bib.bib32 "Deep learning-based electricity price forecast for virtual bidding in wholesale electricity market")); Forgetta et al. ([2025](https://arxiv.org/html/2601.05085v1#bib.bib35 "Distributional forecasting of electricity DART spreads with a covariate-dependent mixture model")).
From a structural perspective, electricity prices are often modeled as arising from the intersection of aggregate supply and demand curves, with local properties of the bid stack governing price sensitivity to quantity shocks Coulon and Howison ([2009](https://arxiv.org/html/2601.05085v1#bib.bib33 "Stochastic behaviour of the electricity bid stack: from fundamental drivers to power prices")). Related structural approaches that jointly model load and price dynamics for risk management and hedging in electricity markets include Coulon et al. ([2013](https://arxiv.org/html/2601.05085v1#bib.bib34 "A model for hedging load and price risk in the Texas electricity market")).

The recent study Galarneau-Vincent et al. ([2023](https://arxiv.org/html/2601.05085v1#bib.bib1 "Foreseeing the worst: forecasting electricity DART spikes")) provides a predictive framework for identifying and trading extreme DART spikes in Long Island, the second largest zone in NYISO.
Their results demonstrate that spike forecasting is feasible and economically valuable.
However, their study has two main limitations:
(i)(i) trades are sized using a fixed quantity rather than an optimized portfolio of zonal exposures, and
(i​i)(ii) the strategy is evaluated only on a single zone.
Here, we address the central operational question faced by large traders: how to scale multi-zone virtual positions when submitting thousands of MWh into the Day-Ahead Market without eroding profits through market impact.

#### Contributions.

This paper extends the framework of Galarneau-Vincent et al. ([2023](https://arxiv.org/html/2601.05085v1#bib.bib1 "Foreseeing the worst: forecasting electricity DART spikes")) in four key directions:

1. 1.

   Multi-zone, two-sided DART spike forecasting.
   We jointly model extreme positive and negative DART spreads across all NYISO zones,
   allowing for correlated bi-directional spike dynamics across locations.
2. 2.

   A structural, economically consistent model of market impact.
   Using day-ahead bid stacks, we estimate both system-wide energy impact coefficients—capturing how net long or short virtual load shifts the DA clearing price—and zone-specific congestion sensitivities.
   This yields a linear–quadratic impact model linking trade size to expected price perturbation.
3. 3.

   Optimal scaling of virtual positions.
   We derive closed-form expressions for the profit-maximizing vector of zonal quantities, incorporating asymmetric buy/sell impacts and cross-zone interactions.
   This allows us to determine how large a trade should be in each zone, not merely whether a trade should be executed.
4. 4.

   Empirical validation at scale. When deployed on 2022–2025 out-of-sample data in multiple zones of three ISO regions—NYISO, ISO–NE and ERCOT111ERCOT does not permit virtual trading, but physical resources face analogous DART exposure when deciding whether to self-commit in the DAM.—the resulting strategy achieves substantial profitability and remains robust across market regimes, including the extreme temperatures observed during Summer 2025.

#### Model overview.

Our methodology proceeds in three stages.
First, we train in Section [3](https://arxiv.org/html/2601.05085v1#S3 "3 Empirical Performance of Benchmark Strategies ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") zone-level classifiers to forecast extreme positive and negative DART events using historical load, price, and congestion features described in Section [2](https://arxiv.org/html/2601.05085v1#S2 "2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
Second, conditional on a directional signal, we estimate the expected DART spread and the local price impact implied by the observed day-ahead bid stack (Section [4.3](https://arxiv.org/html/2601.05085v1#S4.SS3 "4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")).
Finally, we solve a quadratic optimization problem that jointly determines the optimal vector of zonal virtual positions, explicitly accounting for asymmetric system-wide and local market impact (Section [4.2](https://arxiv.org/html/2601.05085v1#S4.SS2 "4.2 Optimal zonal quantities with asymmetric energy impact ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")).
This separation between signal generation and impact-aware sizing allows predictive accuracy and economic consistency to be evaluated independently.

Overall, our results show that DART forecasting and virtual bidding must be treated as a joint problem: forecasts alone are insufficient unless paired with a principled model of price impact and a rigorous scaling rule.
By combining predictive modeling, structural analysis of bid stacks, and multi-zone optimization, this paper provides a comprehensive framework for scalable and economically consistent virtual trading in U.S. wholesale electricity markets.

## 2 Predictive Framework and Statistical Model

This section develops a unified framework for forecasting day-ahead versus real-time (DART) price spreads in U.S. wholesale electricity markets, with an empirical focus on NYISO, ISO–NE, and ERCOT. Figure [1](https://arxiv.org/html/2601.05085v1#S2.F1 "Figure 1 ‣ 2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") shows the zonal layouts for the three regions.

![Refer to caption](NYISO_zones.png)


(a) NYISO load zones.

![Refer to caption](ISONE_ZONES.jpeg)


(b) ISO–NE load zones.

![Refer to caption](ercot_zones.png)


(c) ERCOT load zones.

Figure 1: Zonal maps for NYISO, ISO–NE, and ERCOT.

### 2.1 Data Construction

For each of the three markets, we construct an hourly panel containing day-ahead and real-time prices, system and zonal load forecasts, and a set of exogenous covariates. These include lagged DART values (24h/48h), lagged load forecast errors, hour-of-day and month-of-year indicators, holiday/weekend dummies, and seasonal effects. In practice, all features are constructed using a common set of definitions, lag structures, and calendar conventions across the markets, enabling direct comparability. All market data were obtained from the public data portals of the corresponding system operators, namely ERCOT Electric Reliability Council of Texas ([2025](https://arxiv.org/html/2601.05085v1#bib.bib28 "ERCOT market data")), ISO New England ISO New England ([2025b](https://arxiv.org/html/2601.05085v1#bib.bib29 "ISO New England markets and operations data")), and NYISO New York Independent System Operator ([2025](https://arxiv.org/html/2601.05085v1#bib.bib30 "NYISO market data")). Data access and aggregation were facilitated using the GridStatus platform (<https://www.gridstatus.io>).

### 2.2 Feature Labeling

As day-ahead bids must be submitted well in advance of the operating day, all predictors are constructed using only data available strictly before the corresponding Day-Ahead Market’s gate-closure time:

|  |  |  |
| --- | --- | --- |
|  | NYISO: ​05:00,ISO–NE: ​10:30,ERCOT: ​10:00.\text{NYISO: }05{:}00,\qquad\text{ISO--NE: }10{:}30,\qquad\text{ERCOT: }10{:}00. |  |

This implies a prediction horizon between 19 and 43 hours, depending on the market, and ensures that the forecasting exercise is entirely free of look-ahead bias.

Thus, the feature vector Xt,z,m∈ℝdX\_{t,z,m}\in\mathbb{R}^{d} available at the day-ahead decision time for the operating hour tt, in zone zz of market mm, is constructed using only information available prior to the Day-Ahead Market close and consists of:
(i)(i) lagged DART values at 24h and 48h horizons;
(i​i)(ii) zonal and system-level day-ahead load forecasts;
(i​i​i)(iii) lagged zonal and system-level load forecast errors;
(i​v)(iv) calendar indicators for hour-of-day, month-of-year, and
holidays/weekends; and
(v)(v) season-of-year indicators (Winter, Summer, Shoulder).

The dimension dd corresponds to the total number of covariates after feature construction, including calendar effects, lagged price and load variables, system-level aggregates, and zone fixed effects. The exact value of dd thus depends on the market and feature availability. For example, in the NYISO application considered below, this results
in a feature dimension of d=50d=50, which is significantly larger than d=9d=9 used in Galarneau-Vincent et al. ([2023](https://arxiv.org/html/2601.05085v1#bib.bib1 "Foreseeing the worst: forecasting electricity DART spikes")). Specifically, each hourly observation is represented by a 50-dimensional feature vector XtX\_{t}. This vector concatenates four zone-level predictors—day-ahead load forecasts, lagged DART values (24h and 48h), and lagged load forecast errors—for each of the 11 zones (4×11=444\times 11=44), together with six calendar covariates encoding weekend, holiday, diurnal, and seasonal effects.

### 2.3 Spike Definition and Logistic Regression Models

Given the DART value at time tt, in zone zz of market mm, we define binary labels for negative and positive DART spikes as

|  |  |  |
| --- | --- | --- |
|  | yt,z,mneg=𝟏{DARTt,z,m≤−γneg​(m)},yt,z,mpos=𝟏{DARTt,z,m≥γpos​(m)},y^{\mathrm{neg}}\_{t,z,m}=\mathbf{1}\_{\{\mathrm{DART}\_{t,z,m}\leq-\gamma\_{\mathrm{neg}}(m)\}},\qquad y^{\mathrm{pos}}\_{t,z,m}=\mathbf{1}\_{\{\mathrm{DART}\_{t,z,m}\geq\gamma\_{\mathrm{pos}}(m)\}}, |  |

where the market-specific thresholds
γneg​(m)\gamma\_{\mathrm{neg}}(m) and γpos​(m)\gamma\_{\mathrm{pos}}(m)
are calibrated through exploratory analysis and validation.
These labels isolate the economically meaningful extremes of the DART
distribution that are most relevant for virtual trading strategies. Our first objective is to perform a logistic regression to predict DART spikes.

For each zone zz of market mm and spike type, we define the predicted spike probability at time tt as

|  |  |  |  |
| --- | --- | --- | --- |
|  | pt,z,m=ℙ​(yt,z,m=1∣Xt,z,m)=σ​(βz,m⊤​Xt,z,m),withσ​(u)=11+e−u.\displaystyle p\_{t,z,m}=\mathbb{P}(y\_{t,z,m}=1\mid X\_{t,z,m})=\sigma(\beta\_{z,m}^{\top}X\_{t,z,m}),\quad\text{with}\quad\sigma(u)=\frac{1}{1+e^{-u}}. |  | (1) |

The coefficients βz,m\beta\_{z,m} are obtained by minimizing the following cross-entropy loss for each zone zz:

|  |  |  |
| --- | --- | --- |
|  | minβ​∑t[yt,z,m​(−log⁡pt,z,m)+(1−yt,z,m)​(−log⁡(1−pt,z,m))].\min\_{\beta}\sum\_{t}{\Big[y\_{t,z,m}\left(-\log p\_{t,z,m}\right)+(1-y\_{t,z,m})\left(-\log(1-p\_{t,z,m})\right)\Big]}. |  |

Training windows differ across markets due to data availability (NYISO: 2015–2019; ISO–NE and ERCOT: 2018–2022), and a separate validation period is used to tune probability thresholds.

Model selection.
Before settling on logistic regression, we performed an extensive comparison across several supervised learning methods, including random forests, gradient-boosted trees and feed-forward neural networks Hastie et al. ([2009](https://arxiv.org/html/2601.05085v1#bib.bib26 "The elements of statistical learning: data mining, inference, and prediction")).
While some nonlinear models achieved marginally higher in-sample classification accuracy, they offered no consistent improvement in out-of-sample trading P&L.
This occurs because the spike events of interest are extremely rare and the feature set is largely linear in its predictive structure; consequently, more flexible models exhibit a tendency to overfit the noise in the training data and produce unstable probability forecasts.
Logistic regression, by contrast, delivered the most robust and interpretable out-of-sample performance across all three markets, and produced stable probability estimates that translate reliably into trading signals.
For these reasons, all subsequent results and scaling analyses are reported using the logistic models.

## 3 Empirical Performance of Benchmark Strategies

In this section, we study DART spreads and the performance of the benchmark spike-based INC/DEC strategies described below in Section [3.1](https://arxiv.org/html/2601.05085v1#S3.SS1 "3.1 Benchmark INC and DEC Strategies ‣ 3 Empirical Performance of Benchmark Strategies ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), across the three major U.S. power
markets: NYISO, ISO–NE, and ERCOT. All analyses use hourly
data and a common modeling framework, with separate classifiers for positive and negative DART spikes calibrated on a validation set and evaluated out-of-sample.

Pooling information across zones is essential in NYISO, where congestion and
losses generate substantial zonal heterogeneity. In contrast, ISO–NE and
ERCOT exhibit highly synchronized zonal DART movements, so that a single
representative zone captures most of the relevant variation.

### 3.1 Benchmark INC and DEC Strategies

Recall that pt,z,mp\_{t,z,m} denotes the predicted probability of a DART spike at time tt in zone zz of market mm, as defined in ([1](https://arxiv.org/html/2601.05085v1#S2.E1 "In 2.3 Spike Definition and Logistic Regression Models ‣ 2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")). In Galarneau-Vincent et al. ([2023](https://arxiv.org/html/2601.05085v1#bib.bib1 "Foreseeing the worst: forecasting electricity DART spikes")), a trade is executed whenever

|  |  |  |
| --- | --- | --- |
|  | pt,z,m≥τz,m,p\_{t,z,m}\geq\tau\_{z,m}, |  |

where τz,m\tau\_{z,m} is a zone-specific threshold. The predictive model used to estimate the probability pt,z,mp\_{t,z,m} of a DART spike, conditional on the feature vector Xt,z,mX\_{t,z,m}, is trained on a historical training set, while τz,m\tau\_{z,m}, γneg​(m)\gamma\_{\text{neg}}(m) and γpos​(m)\gamma\_{\text{pos}}(m) are selected to
maximize P&L on a separate validation set under unit-size trading and no price
impact. All performance results reported below are evaluated on a held-out test
set.

We study two benchmark strategies:

1. 1.

   INC-only: trade when a negative DART spike is predicted,
   earning −DARTt,z,m-\mathrm{DART}\_{t,z,m};
2. 2.

   DEC-only: trade when a positive DART spike is predicted,
   earning +DARTt,z,m+\mathrm{DART}\_{t,z,m}.

These strategies provide a clean baseline for comparing predictive performance
across markets and zones. Building on this benchmark framework, we will extend in Section [4.2](https://arxiv.org/html/2601.05085v1#S4.SS2 "4.2 Optimal zonal quantities with asymmetric energy impact ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") the
single-zone trading rule to a joint multi-zone optimization problem with
endogenous position sizing and price impact.

### 3.2 P&L in NYISO

For NYISO, we work with hourly data from 2015–2025 across eleven load zones, and
focus the discussion on six large-demand zones: CAPITL, CENTRL, LONGIL, NORTH,
NYC, and WEST. We adopt the chronological split

|  |  |  |
| --- | --- | --- |
|  | Train: ​2015​–​2019,Validation: ​2020​–​2021,Test: ​2022​–​2025.\text{Train: }2015\text{--}2019,\qquad\text{Validation: }2020\text{--}2021,\qquad\text{Test: }2022\text{--}2025. |  |

Separate logistic classifiers are fit for positive and negative DART spikes on
the training set, with spike thresholds and probability cutoffs selected on the
validation set to maximize unit-size P&L. The resulting thresholds used in the
NYISO analysis are

|  |  |  |
| --- | --- | --- |
|  | γpos=5​$/MWh,γneg=30​$/MWh.\gamma\_{\text{pos}}=5\mathdollar/\text{MWh},\qquad\gamma\_{\text{neg}}=30\mathdollar/\text{MWh}. |  |

We tune the probability cutoffs τpos\tau\_{\text{pos}} and τneg\tau\_{\text{neg}}
separately for each zone. For example, in NYC the selected cutoffs are
(τpos,τneg)=(0.75,0.9)(\tau\_{\text{pos}},\tau\_{\text{neg}})=(0.75,0.9), while for Long Island
they are (0.7,0.9)(0.7,0.9).

Figures [2](https://arxiv.org/html/2601.05085v1#S3.F2 "Figure 2 ‣ 3.2 P&L in NYISO ‣ 3 Empirical Performance of Benchmark Strategies ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")(a)–(d) report cumulative P&L over the
2022–2025 test period for INC-only and DEC-only benchmark strategies in NYC and Long Island, the two zones with the highest demand. Corresponding results for the remaining zones are presented in Figures [8](https://arxiv.org/html/2601.05085v1#A1.F8 "Figure 8 ‣ A.1 Tables and Figures for NYISO ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")(a)–(h) in the Appendix. The figures highlight pronounced cross-zonal heterogeneity: while some regions exhibit persistent profitability from DEC positions, others display stronger performance for INC trading.

![Refer to caption](NYC_INC.png)


(a) NYC — INC

![Refer to caption](NYC_DEC.png)


(b) NYC — DEC

![Refer to caption](LONGIL_INC.png)


(c) LONGIL — INC

![Refer to caption](LONGIL_DEC.png)


(d) LONGIL — DEC

Figure 2: NYISO: cumulative P&L for NYC and Long Island under the INC/DEC benchmark strategy.

Tables [5](https://arxiv.org/html/2601.05085v1#A1.T5 "Table 5 ‣ A.1 Tables and Figures for NYISO ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") and [6](https://arxiv.org/html/2601.05085v1#A1.T6 "Table 6 ‣ A.1 Tables and Figures for NYISO ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") (in the Appendix) report cumulative
P&L by zone, which we relate to the yearly mean DART spreads shown in
Table [7](https://arxiv.org/html/2601.05085v1#A1.T7 "Table 7 ‣ A.1 Tables and Figures for NYISO ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"). Zones with systematically positive DART averages
(e.g., CAPITL or, in earlier years, LONGIL) tend to favour DEC strategies,
whereas zones with negative or mixed averages (such as NYC in the post-2022
period) are more aligned with INC trading. This structural bias in the DART
distribution helps explain cross-zonal differences in profitability and
provides guidance on whether a zone is better approached with INC-only,
DEC-only, or mixed strategies.

Cross-zone dependence remains strong throughout NYISO, as shown in
Table [8](https://arxiv.org/html/2601.05085v1#A1.T8 "Table 8 ‣ A.2 DART Correlation Across Zones ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), but varies meaningfully across groups of zones.
Upstate zones exhibit particularly high correlations in DART spreads, while downstate zones
form a tightly interconnected cluster. This pattern reflects localized
congestion and loss effects superimposed on system-wide price movements, and
motivates pooling information across zones while retaining zone-specific
features in the predictive models.

### 3.3 P&L in ISO–NE

We perform a parallel analysis on ISO New England, which consists of
eight load zones, using hourly data from November 2018 to October 2025. DART
spreads across ISO–NE zones are almost perfectly correlated, as we see in Table [9](https://arxiv.org/html/2601.05085v1#A1.T9 "Table 9 ‣ A.2 DART Correlation Across Zones ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), indicating that
economically relevant variation is predominantly system-wide rather than
zonal. To avoid redundant signals, we therefore conduct the spike-prediction
and trading analysis on a single representative zone, Maine (ME).

Given the shorter sample relative to NYISO, we adopt the split

|  |  |  |
| --- | --- | --- |
|  | Train: ​2018​–​2022,Validation: ​2023,Test: ​2024​–​2025.\text{Train: }2018\text{--}2022,\qquad\text{Validation: }2023,\qquad\text{Test: }2024\text{--}2025. |  |

Separate classifiers are fit for positive and negative DART spikes, with spike
thresholds and probability cutoffs tuned on the validation set. For the Maine load zone in ISO–NE, the resulting parameters are

|  |  |  |
| --- | --- | --- |
|  | γpos=2​$/MWh,γneg=8​$/MWh,τpos=0.70,τneg=0.90.\gamma\_{\text{pos}}=2\mathdollar/\text{MWh},\qquad\gamma\_{\text{neg}}=8\mathdollar/\text{MWh},\qquad\tau\_{\text{pos}}=0.70,\qquad\tau\_{\text{neg}}=0.90. |  |

Figure [3](https://arxiv.org/html/2601.05085v1#S3.F3 "Figure 3 ‣ 3.3 P&L in ISO–NE ‣ 3 Empirical Performance of Benchmark Strategies ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") shows the cumulative P&L curves for the INC-only and
DEC-only benchmark strategies on the 2024–2025 test period. Overall performance is
weaker than in NYISO, with most profits arising from DEC trades, while INC
positions are triggered less frequently due to both the smaller negative-spike
threshold and the model’s lower predictive sharpness in this market.

![Refer to caption](MAINE_PNL_ISONE.png)


(a) Total P&L (ME).

![Refer to caption](MAINE_INC_ISONE.png)


(b) INC-only P&L.

![Refer to caption](MAINE_DEC-ISONE.png)


(c) DEC-only P&L.

Figure 3: ISO–NE MAINE zone — P&L curves for overall, INC-only, and DEC-only strategies on the 2024–2025 test period.

### 3.4 P&L in ERCOT

We next analyze ERCOT using hourly data from 2018–2025 across its four principal
load zones: North, South, West, and Houston. DART spreads across ERCOT zones are
extremely highly correlated (Table [10](https://arxiv.org/html/2601.05085v1#A1.T10 "Table 10 ‣ A.2 DART Correlation Across Zones ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")), with pairwise
correlations exceeding 0.970.97, indicating that DA–RT dynamics are effectively
system-wide. As a result, all zones generate nearly identical predictions and
trading behavior; we therefore focus on the WEST zone for
concreteness.

Given the shorter sample relative to NYISO, we adopt the split

|  |  |  |
| --- | --- | --- |
|  | Train: ​2018​–​2022,Validation: ​2023,Test: ​2024​–​2025.\text{Train: }2018\text{--}2022,\qquad\text{Validation: }2023,\qquad\text{Test: }2024\text{--}2025. |  |

Spike thresholds and probability cutoffs are tuned on the validation set. For
WEST, the resulting parameters are

|  |  |  |
| --- | --- | --- |
|  | γpos=15​$/MWh,γneg=10​$/MWh,τpos=0.75,τneg=0.90.\gamma\_{\text{pos}}=15\mathdollar/\text{MWh},\qquad\gamma\_{\text{neg}}=10\mathdollar/\text{MWh},\qquad\tau\_{\text{pos}}=0.75,\qquad\tau\_{\text{neg}}=0.90. |  |

Figure [4](https://arxiv.org/html/2601.05085v1#S3.F4 "Figure 4 ‣ 3.4 P&L in ERCOT ‣ 3 Empirical Performance of Benchmark Strategies ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports the total, INC-only, and DEC-only benchmark strategy
P&L curves on the 2024–2025 test period. Most profits arise from the DEC side,
while INC trades perform well initially but give back a large fraction of early gains.

![Refer to caption](WEST_PNL_ERCOT.png)


(a) Total P&L (WEST).

![Refer to caption](WEST_INC_ERCOT.png)


(b) INC-only P&L.

![Refer to caption](WEST_DEC_ERCOT.png)


(c) DEC-only P&L.

Figure 4: ERCOT WEST zone — P&L curves for overall, INC-only, and DEC-only strategies on the 2024–2025 test period.

### 3.5 Cross–Market Comparison

Tables [8](https://arxiv.org/html/2601.05085v1#A1.T8 "Table 8 ‣ A.2 DART Correlation Across Zones ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), [9](https://arxiv.org/html/2601.05085v1#A1.T9 "Table 9 ‣ A.2 DART Correlation Across Zones ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), and [10](https://arxiv.org/html/2601.05085v1#A1.T10 "Table 10 ‣ A.2 DART Correlation Across Zones ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")
highlight pronounced differences in cross-zonal DART dependence across markets.
In ERCOT and ISO–NE, DART spreads are almost perfectly synchronized across zones,
indicating that DA–RT deviations are driven primarily by system-wide factors.
Consequently, zone-level behaviour in these markets is largely redundant, and a
single representative zone captures most relevant variation. By contrast, NYISO
exhibits substantially weaker and more heterogeneous cross-zonal correlations,
reflecting localized congestion, losses, and transmission constraints. This
structural heterogeneity implies that DART dynamics in NYISO cannot be reduced to
a single system factor, making multi-zone modelling essential.

To provide distributional context for the spike thresholds and trading activity
across markets, Table [11](https://arxiv.org/html/2601.05085v1#A1.T11 "Table 11 ‣ A.3 NYISO, ISO–NE & ERCOT Quantiles ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports empirical
DART quantiles on the training samples for representative zones: NYISO LONGIL,
ISO–NE ME, and ERCOT WEST. NYISO exhibits heavier intermediate and upper tails,
with substantially larger 9090th–9999th percentiles relative to ISO–NE and
ERCOT.

Taken together, the heavier-tailed DART distribution in NYISO helps explain its
greater trading profitability relative to ISO–NE and ERCOT: larger and more
frequent spikes generate a richer set of economically meaningful opportunities,
on which predictive signals can be exploited more often. Differences in observed
INC and DEC activity across markets therefore reflect both underlying market
structure and the predictive sharpness of the model, rather than spike magnitudes
alone.

## 4 Optimal Trading Strategy

A central objective of this section is to determine how large our virtual trading positions should be in each NYISO zone, once a directional signal has been generated by the spike–forecasting model.
Correctly sizing trades is essential: although DART spreads create strong economic opportunities, large virtual positions mechanically shift the day-ahead clearing price through both system-level and zonal congestion effects.
Hence, to maximize profitability while avoiding excessive market impact, we require an explicit model linking trade size to DA price response.
The following subsections develop this scaling model, calibrate its parameters, and derive the optimal zonal quantities used in our strategy. For notational simplicity, we henceforth drop the market subscript mm, as the analysis in this section focuses on NYISO.

### 4.1 Price Impact Model

Let ZZ denote the number of zones and let
qt∈ℝZq\_{t}\in\mathbb{R}^{Z} be the vector of signed bidding quantities (MWh) at time tt, where
qt,z>0q\_{t,z}>0 represents an INC (virtual demand) in zone zz at time tt and
qt,z<0q\_{t,z}<0 represents a DEC (virtual supply).
For each hour tt and zone zz, denote

|  |  |  |
| --- | --- | --- |
|  | DAt,z,RTt,z∈ℝ,DARTt,z:=DAt,z−RTt,z.\text{DA}\_{t,z},\;\text{RT}\_{t,z}\in\mathbb{R},\qquad\text{DART}\_{t,z}:=\text{DA}\_{t,z}-\text{RT}\_{t,z}. |  |

The $\mathdollar-per–MWh trading edge of an INC or a DEC trade is then

|  |  |  |
| --- | --- | --- |
|  | rt,zINC=−DARTt,z,rt,zDEC=+DARTt,z.r^{\text{INC}}\_{t,z}=-\,\text{DART}\_{t,z},\qquad r^{\text{DEC}}\_{t,z}=+\,\text{DART}\_{t,z}. |  |

If a trade of size q∈ℝq\in\mathbb{R} is executed, the realized dollar P&L for side
s∈{INC,DEC}s\in\{\text{INC},\text{DEC}\} at time tt in zone zz is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πt,z(s)​(q)=q​(rt,z(s)−I​(q,t,z)),\Pi^{(s)}\_{t,z}(q)\;=\;q\Bigl(r^{(s)}\_{t,z}-I(q,t,z)\Bigr), |  | (2) |

where I​(q,t,z)I(q,t,z) is the $\mathdollar-per-MWh price impact imposed on the DA price, depending on the submitted quantity, time and zone.

Before specifying the price–impact model, we recall the standard decomposition of
day-ahead locational marginal prices (LMPs).
In all U.S. ISOs, including NYISO, ISO–NE, and ERCOT
Kumar ([2025](https://arxiv.org/html/2601.05085v1#bib.bib5 "Locational based marginal pricing")); ISO New England ([2025a](https://arxiv.org/html/2601.05085v1#bib.bib6 "FAQs: locational marginal pricing")), the day-ahead price at zone zz and hour tt can be written as

|  |  |  |
| --- | --- | --- |
|  | DAt,z=Energyt+Losst,z+Congestiont,z.{\rm DA}\_{t,z}=\text{Energy}\_{t}+\text{Loss}\_{t,z}+\text{Congestion}\_{t,z}. |  |

The energy component is system-wide, whereas losses and congestion vary across
zones due to transmission constraints and network topology. These spatial components are
precisely what generate cross-zonal heterogeneity in DART spreads and motivate a
zone-dependent treatment of price impact in our scaling model.

Virtual demand and supply bids
shift the residual demand curve and thus impact day ahead clearing prices.
Following the standard approach Almgren and Chriss ([2001](https://arxiv.org/html/2601.05085v1#bib.bib14 "Optimal execution of portfolio transactions")); Gatheral ([2010](https://arxiv.org/html/2601.05085v1#bib.bib15 "No-dynamic-arbitrage and market impact")) in
optimal execution and market impact models, see also Aïd et al. ([2016](https://arxiv.org/html/2601.05085v1#bib.bib2 "An optimal trading problem in intraday electricity markets")) for a stochastic control formulation of optimal trading with price impact in electricity markets, we approximate the zonal response of prices to aggregate traded quantity StS\_{t} by a piecewise linear function, with energy-impact coefficients
kE+k\_{\rm E}^{+} and kE−k\_{\rm E}^{-}, and a separate linear impact from the trade size qt,zq\_{t,z} in the specific zone with coefficient kzk\_{z}:

|  |  |  |
| --- | --- | --- |
|  | I​(q,t,z)=(kE+​𝟏{St≥0}+kE−​𝟏{St<0})​St+kz​qt,z,St:=∑zqt,z.I(q,t,z)=\bigl(k\_{\rm E}^{+}\mathbf{1}\_{\{S\_{t}\geq 0\}}+k\_{\rm E}^{-}\mathbf{1}\_{\{S\_{t}<0\}}\bigr)\,S\_{t}+k\_{z}\,q\_{t,z},\qquad S\_{t}:=\sum\_{z}q\_{t,z}. |  |

The motivation for the first term is that when St>0S\_{t}>0, the system takes a net INC position and moves
along the demand curve, whereas when St<0S\_{t}<0 it takes a net DEC position and moves
along the supply curve.
Since the slopes of the supply and demand curves differ, their marginal price
impacts differ as well, motivating the use of distinct energy-impact coefficients
kE+k\_{\rm E}^{+} and kE−k\_{\rm E}^{-}. We estimate these coefficients in Section [4.3](https://arxiv.org/html/2601.05085v1#S4.SS3 "4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") using aggregate supply and demand curve.

Moreover, zones in NYISO differ substantially in their typical demand levels and
exposure to transmission constraints. Large demand centers such as NYC and Long Island
tend to absorb incremental virtual positions with relatively small marginal effects on
losses and congestion, whereas smaller or more constrained zones can exhibit much larger
local price sensitivities. This motivates introducing a zone-specific local impact
coefficient kzk\_{z}, capturing how virtual demand or supply submitted bids in zone zz affect
the spatial components of day-ahead prices. In Section [4.4](https://arxiv.org/html/2601.05085v1#S4.SS4 "4.4 Estimating local impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), we
calibrate these coefficients using zonal load and price data.

### 4.2 Optimal zonal quantities with asymmetric energy impact

Each zone zz is equipped with a classifier that outputs the probability pt,zp\_{t,z} that hour tt
in zone zz experiences an INC spike (negative DART) or a DEC spike (positive DART).
After training on 2015–2019, we tune the decision thresholds τz\tau\_{z} on the 2020–2021 validation set.
At time tt, we trade in zone zz whenever

|  |  |  |
| --- | --- | --- |
|  | pt,z≥τz,p\_{t,z}\geq\tau\_{z}, |  |

and select the trade direction (INC or DEC) with the larger predicted expected payoff.

Conditional on trading, we next determine the appropriate trade size in each zone.
To this end, we estimate the conditional expected economic revenue on the validation period:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt,zINC:=𝔼​[rt,zINC∣pt,z≥τz],xt,zDEC:=𝔼​[rt,zDEC∣pt,z≥τz].x^{\mathrm{INC}}\_{t,z}:=\mathbb{E}\!\left[r^{\mathrm{INC}}\_{t,z}\mid p\_{t,z}\geq\tau\_{z}\right],\qquad x^{\mathrm{DEC}}\_{t,z}:=\mathbb{E}\!\left[r^{\mathrm{DEC}}\_{t,z}\mid p\_{t,z}\geq\tau\_{z}\right]. |  | (3) |

These zone-specific expected payoffs summarize how profitable INC and DEC trades tend to be
when the model signals a spike and executes a trade.
They form the input to the scaling optimization that determines the virtual position
allocated to each zone.

Given a fixed time tt and the selected trade direction, we collect the expected payoffs into the vector

|  |  |  |
| --- | --- | --- |
|  | xt≡(xt,1,…,xt,Z)∈ℝZ,x\_{t}\equiv(x\_{t,1},\dots,x\_{t,Z})\in\mathbb{R}^{Z}, |  |

and choose zonal quantities qt,zq\_{t,z}.

For a trade vector q∈ℝZq\in\mathbb{R}^{Z}, we define the objective function

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(q)=xt⊤​q−(kE+​𝟏{S≥0}+kE−​𝟏{S<0})​S2−∑z=1Zkz​qz2,S:=𝟏⊤​q,F(q)=\;x\_{t}^{\top}q\;-\;\bigl(k\_{\rm E}^{+}\mathbf{1}\_{\{S\geq 0\}}+k\_{\rm E}^{-}\mathbf{1}\_{\{S<0\}}\bigr)S^{2}\;-\;\sum\_{z=1}^{Z}k\_{z}q\_{z}^{2},\qquad S:=\mathbf{1}^{\top}q, |  | (4) |

which represents the expected price-impacted DART payoff of the trade qq placed at time tt.
The energy impact coefficient is sign-dependent: we use kE+k\_{\rm E}^{+} when S>0S>0 (net buy)
and kE−k\_{\rm E}^{-} when S<0S<0 (net sell).

Fix kEk\_{\rm E} (either kE+k\_{\rm E}^{+} or kE−k\_{\rm E}^{-}) and suppose the optimum is interior.
The first-order conditions of ([4](https://arxiv.org/html/2601.05085v1#S4.E4 "In 4.2 Optimal zonal quantities with asymmetric energy impact ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")) yield the following optimal zonal trade quantities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qt,z⋆=xt,z−2​kE​S2​kz.q\_{t,z}^{\star}=\frac{x\_{t,z}-2k\_{\rm E}S}{2k\_{z}}. |  | (5) |

Define

|  |  |  |
| --- | --- | --- |
|  | H:=∑z=1Z1kz,Nt:=∑z=1Zxt,zkz.H\;:=\;\sum\_{z=1}^{Z}\frac{1}{k\_{z}},\qquad N\_{t}\;:=\;\sum\_{z=1}^{Z}\frac{x\_{t,z}}{k\_{z}}. |  |

Summing ([5](https://arxiv.org/html/2601.05085v1#S4.E5 "In 4.2 Optimal zonal quantities with asymmetric energy impact ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")) over zz yields the closed-form net position

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=Nt/21+kE​H.S=\frac{N\_{t}/2}{1+k\_{\rm E}H}. |  | (6) |

We therefore obtain two interior candidate solutions:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | INC regime (S>0S>0): | S(+)=Nt/21+kE+​H,\displaystyle S^{(+)}=\frac{N\_{t}/2}{1+k\_{\rm E}^{+}H}, | qt,z(+)=xt,z−2​kE+​S(+)2​kz,\displaystyle q\_{t,z}^{(+)}=\frac{x\_{t,z}-2k\_{\rm E}^{+}S^{(+)}}{2k\_{z}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | DEC regime (S<0S<0): | S(−)=Nt/21+kE−​H,\displaystyle S^{(-)}=\frac{N\_{t}/2}{1+k\_{\rm E}^{-}H}, | qt,z(−)=xt,z−2​kE−​S(−)2​kz.\displaystyle q\_{t,z}^{(-)}=\frac{x\_{t,z}-2k\_{\rm E}^{-}S^{(-)}}{2k\_{z}}. |  |

A third possibility is that the optimum lies on the boundary where the net position is zero,
so that the energy impact term vanishes and only local impacts remain.
In this regime we solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxq∈ℝZ⁡xt⊤​q−∑z=1Zkz​qz2subject to𝟏⊤​q=0.\max\_{q\in\mathbb{R}^{Z}}\;x\_{t}^{\top}q-\sum\_{z=1}^{Z}k\_{z}q\_{z}^{2}\quad\text{subject to}\quad\mathbf{1}^{\top}q=0. |  | (7) |

Introducing a Lagrange multiplier, the optimal zonal trade quantities are given by

|  |  |  |
| --- | --- | --- |
|  | qt,z(0)=xt,z−Nt/H2​kz,S(0)=0.q\_{t,z}^{(0)}=\frac{x\_{t,z}-N\_{t}/H}{2k\_{z}},\qquad S^{(0)}=0. |  |

The optimization therefore yields three candidate solutions
qt(+),qt(−),qt(0)q^{(+)}\_{t},q^{(-)}\_{t},q^{(0)}\_{t}.
We retain qt(+)q^{(+)}\_{t} only when S(+)>0S^{(+)}>0, and qt(−)q^{(-)}\_{t} only when S(−)<0S^{(-)}<0.
The net-flat solution qt(0)q^{(0)}\_{t} is always feasible.
Among all admissible candidates, the optimal trading vector is the one that maximizes
the objective value F​(q)F(q).

### 4.3 Estimating the energy-impact coefficients

We describe system-wide price formation in the NYISO Day-Ahead Market using
aggregate supply and demand curves. Let QS​(p)Q^{\rm S}(p) and QD​(p)Q^{\rm D}(p) denote,
respectively, the total quantity supplied and demanded at price pp.
For each hour tt, the day-ahead clearing price p⋆​(t)p^{\star}(t) satisfies

|  |  |  |
| --- | --- | --- |
|  | QS​(p⋆​(t))=QD​(p⋆​(t)).Q^{\rm S}\!\bigl(p^{\star}(t)\bigr)=Q^{\rm D}\!\bigl(p^{\star}(t)\bigr). |  |

Equivalently, defining the cleared quantity

|  |  |  |
| --- | --- | --- |
|  | q⋆​(t):=QS​(p⋆​(t))=QD​(p⋆​(t)),q^{\star}(t):=Q^{\rm S}\!\bigl(p^{\star}(t)\bigr)=Q^{\rm D}\!\bigl(p^{\star}(t)\bigr), |  |

the relevant price–quantity relationship is given locally by the inverse
supply and demand curves PS​(q):=(QS)−1​(q)P^{\rm S}(q):=(Q^{\rm S})^{-1}(q) and PD​(q):=(QD)−1​(q)P^{\rm D}(q):=(Q^{\rm D})^{-1}(q)
evaluated at (q⋆​(t),p⋆​(t))(q^{\star}(t),p^{\star}(t)).
Our objective is to estimate the local slope of this
mapping at the day-ahead equilibrium. Because the bid stack is observed only as a discrete collection of bids,
we estimate these derivatives numerically using one-sided finite differences.
This approach follows the bid-stack–based price formation framework introduced in Coulon and Howison ([2009](https://arxiv.org/html/2601.05085v1#bib.bib33 "Stochastic behaviour of the electricity bid stack: from fundamental drivers to power prices")), which model s electricity prices as arising from local properties of the aggregate supply and demand curves.

A net long day-ahead position of size Δ​q>0\Delta q>0 corresponds to an exogenous
increase in aggregate demand. Operationally, the realized cleared quantity becomes

|  |  |  |
| --- | --- | --- |
|  | QS​(p+)=QD​(p+)=QD​(p⋆)+Δ​q=QS​(p⋆)+Δ​q,Q^{\rm S}(p^{+})=Q^{\rm D}(p^{+})=Q^{\rm D}(p^{\star})+\Delta q=Q^{\rm S}(p^{\star})+\Delta q, |  |

where p+p^{+} denotes the perturbed clearing price. Expanding QSQ^{\rm S} to first order
around p⋆p^{\star} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | p+−p⋆≈Δ​q(QS)′​(p⋆)> 0.p^{+}-p^{\star}\;\approx\;\frac{\Delta q}{(Q^{\rm S})^{\prime}(p^{\star})}\;>\;0. |  | (8) |

Equivalently, this corresponds to a first-order expansion of the inverse supply
curve PS​(q)P^{\rm S}(q) around q⋆q^{\star}.
Thus the buy-side price impact is governed by the local slope of the aggregate
supply curve.

We estimate kE+k\_{\rm E}^{+} by taking Δ​q=1000\Delta q=1000 MWh and averaging the resulting
finite-difference price responses across a selected set of hours within each
season and Peak/Off-Peak bucket. Specifically, we consider the Top-10 spike
hours (N=10N=10).
The resulting average buy-side impacts are reported in
Table [1](https://arxiv.org/html/2601.05085v1#S4.T1 "Table 1 ‣ 4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").

Table 1: Average linear price impact kE+($/1000k\_{E}^{+}(\mathdollar/1000MWh) induced by a +1000+1000 MWh demand shock, by season and load band: train (2015–2019) vs. test (2022–2025).

| Season | Band | Top-10 spikes (2015–2019) | Top-10 spikes (2022–2025) |
| --- | --- | --- | --- |
| Winter | Off-Peak | 17.03017.030 | 10.56110.561 |
| Winter | Peak | 23.21023.210 | 26.27026.270 |
| Summer | Off-Peak | 8.0508.050 | 66.83966.839 |
| Summer | Peak | 34.64034.640 | 46.47746.477 |
| Shoulder | Off-Peak | 1.7401.740 | 2.3422.342 |
| Shoulder | Peak | 10.48010.480 | 22.22622.226 |

Similarly, a net short position of size Δ​q<0\Delta q<0 corresponds to a shift
along the inverse demand curve. In this case, the perturbed clearing price p−p^{-}
satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | p−−p⋆≈Δ​q(QD)′​(p⋆)< 0.p^{-}-p^{\star}\;\approx\;\frac{\Delta q}{(Q^{\rm D})^{\prime}(p^{\star})}\;<\;0. |  | (9) |

The sell-side impact is thus governed by the local slope of the aggregate demand
curve. We estimate kE−k\_{\rm E}^{-} analogously using one-sided finite differences with
Δ​q=1000\Delta q=1000 MWh and the same sampling scheme.
Corresponding sell-side impacts are reported in
Table [2](https://arxiv.org/html/2601.05085v1#S4.T2 "Table 2 ‣ 4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").

Table 2: Average linear price impact kE−($/1000k\_{E}^{-}(\mathdollar/1000MWh) induced by a −1000-1000 MWh supply shock, by season and load band: train (2015–2019) vs. test (2022–2025).

| Season | Band | Top-10 spikes (2015–2019) | Top-10 spikes (2022–2025) |
| --- | --- | --- | --- |
| Winter | Off-Peak | −92.15-92.15 | −117.95-117.95 |
| Winter | Peak | −114.89-114.89 | −131.33-131.33 |
| Summer | Off-Peak | −19.73-19.73 | −24.40-24.40 |
| Summer | Peak | −45.82-45.82 | −59.11-59.11 |
| Shoulder | Off-Peak | −17.96-17.96 | −22.78-22.78 |
| Shoulder | Peak | −28.37-28.37 | −32.44-32.44 |

The parameters (kE+,kE−)(k\_{\rm E}^{+},k\_{\rm E}^{-}) should therefore be interpreted as local
average slopes of the inverse residual supply and demand curves at the
day-ahead clearing point. In general, they need not coincide: supply and demand
can exhibit markedly different slopes near equilibrium, particularly during
stressed system conditions. This naturally leads to an asymmetric price response
to buy- versus sell-side shocks.

To capture systematic variation in these slopes, we stratify the estimation by
season (Winter, Summer, Shoulder) and by load regime (Peak and Off-Peak hours),
reflecting predictable changes in system stress and bid-stack geometry.
In all subsequent optimization experiments, the system-wide impact parameters
(kE+,kE−)(k\_{\rm E}^{+},k\_{\rm E}^{-}) are estimated exclusively on the calibration sample
(2015–2019) and treated as fixed inputs when constructing optimal portfolios and
computing realized P&L over the out-of-sample test period (2022–2025). This
procedure ensures that portfolio decisions rely solely on historically available
information and that all reported profits are free of look-ahead bias. For illustration, in the calibration sample (2015–2019) the largest buy-side
impact occurs during Summer Peak hours, where a +1000+1000 MWh demand shock
raises prices by 34.6434.64 $/MWh on average,while
on the sell side, the largest impact is observed during Winter Peak hours,
where a −1000-1000 MWh supply shock lowers prices by 114.89114.89 $/MWh.

Figures [5](https://arxiv.org/html/2601.05085v1#S4.F5 "Figure 5 ‣ 4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") and [6](https://arxiv.org/html/2601.05085v1#S4.F6 "Figure 6 ‣ 4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") provide a visual illustration of the local linearity underlying this calibration. For a selection of representative hours, we plot the supply and demand curves in a neighborhood of the Day-Ahead Market intersection and compare the market-clearing price before and after an exogenous quantity shock. The dotted line in each panel corresponds to the local linear approximation used in the impact model, while the displacement between the pre- and post-shock clearing prices reflects the realized price response to the injected demand or supply. These examples illustrate how, at the relevant operating point, the bid stack is well-approximated by a linear slope, justifying the use of a linear impact specification and motivating the estimation of seasonal and load-regime–specific impact coefficients.

![Refer to caption](supply12.png)


(a) 06-01-2025

![Refer to caption](supply15.png)


(b) 06-01-2025

![Refer to caption](supply18.png)


(c) 06-01-2025

Figure 5: Supply stack and linear approximation near the DA price-setting intersection point at three different hours.



![Refer to caption](03012025.png)


(a) 03-01-2025

![Refer to caption](05012025.png)


(b) 05-01-2025

![Refer to caption](07012025.png)


(c) 07-01-2025

Figure 6: Demand stack and linear approximation near the DA price-setting intersection point at three different hours.

### 4.4 Estimating local impact coefficients

To calibrate the zone-specific impact coefficients kzk\_{z}, we estimate how forecast load affects zonal day-ahead prices in the NYISO market through the
loss and congestion components of the locational marginal price (LMP).
As a reference, we first focus on the Long Island (LONGIL) zone, which is both a large demand center
and an import-constrained load pocket in NYISO.
Its loss and congestion components reflect flows across multiple upstream interfaces and exhibit
substantial non-local transmission stress, making Long Island a natural baseline for calibrating
marginal price impact.

We regress the DA loss-minus-congestion component on the corresponding zonal forecast load separately for each zone, season, and Peak/Off-Peak bucket.
The estimated slopes, reported in Table [12](https://arxiv.org/html/2601.05085v1#A1.T12 "Table 12 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), measure the
average price impact (in $/MWh) of a +1000+1000 MWh increase in forecast load within that zone.
In Long Island, the estimated impact ranges from 4.954.95 to 7.827.82 in Shoulder,
from 5.065.06 to 17.7317.73 in Summer, and from 43.3043.30 to 43.6343.63 in Winter,
depending on the Peak/Off-Peak bucket.

Table [13](https://arxiv.org/html/2601.05085v1#A1.T13 "Table 13 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports the corresponding average forecast load by zone and season
over 2015–2021.
Zones with higher typical loads (e.g., NYC and Long Island) tend to exhibit smaller marginal price
impacts per MW, whereas smaller or more transmission-constrained zones (e.g., Millwood and Dunwoodie)
show substantially higher sensitivities. These patterns are consistent with localized load shocks
being diluted in large demand centers and amplified in smaller or constrained zones.

Guided by the regression evidence—most notably the relatively small marginal impacts in large zones
such as Long Island and NYC NYISO ([2024](https://arxiv.org/html/2601.05085v1#bib.bib11 "Locational minimum installed capacity requirements study for the 2024–2025 capability year")); Kelly Stegmann et al. ([2025](https://arxiv.org/html/2601.05085v1#bib.bib10 "Congestion price component")), and the much
larger impacts in smaller or more constrained zones—we model the local linear impact coefficients
kzk\_{z} as inversely proportional to average zonal load.
Using historical mean actual loads LzL\_{z} over 2015–2021, we calibrate

|  |  |  |
| --- | --- | --- |
|  | kz=kLONGIL​LLONGILLz,kLONGIL=0.050​$/(MWh)2,k\_{z}=k\_{\mathrm{LONGIL}}\frac{L\_{\mathrm{LONGIL}}}{L\_{z}},\qquad k\_{\mathrm{LONGIL}}=0.050\mathdollar/(\text{MW}\text{h})^{2}, |  |

so that the overall scale of the kzk\_{z} is consistent with the order of magnitude of the Long Island
Summer–Peak regression coefficients (shown in Figure [9](https://arxiv.org/html/2601.05085v1#A1.F9 "Figure 9 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") in the Appendix), while
preserving the empirical ranking of zones by size and sensitivity.
This yields the following estimates:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | kNYC\displaystyle k\_{\text{NYC}} | =0.020\displaystyle=0.020\quad | kLONGIL\displaystyle k\_{\text{LONGIL}} | =0.050\displaystyle=0.050\quad | kWEST\displaystyle k\_{\text{WEST}} | =0.067\displaystyle=0.067\quad | kCENTRL\displaystyle k\_{\text{CENTRL}} | =0.065,\displaystyle=0.065, |  |
|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | kCAPITL\displaystyle k\_{\text{CAPITL}} | =0.085\displaystyle=0.085\quad | kNORTH\displaystyle k\_{\text{NORTH}} | =0.210\displaystyle=0.210\quad | kDUNWOD\displaystyle k\_{\text{DUNWOD}} | =0.169\displaystyle=0.169\quad | kMILLWD\displaystyle k\_{\text{MILLWD}} | =0.357,\displaystyle=0.357, |  |
|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | kHUDVL\displaystyle k\_{\text{HUDVL}} | =0.105\displaystyle=0.105\quad | kMHKVL\displaystyle k\_{\text{MHKVL}} | =0.129\displaystyle=0.129\quad | kGENESE\displaystyle k\_{\text{GENESE}} | =0.103.\displaystyle=0.103.\quad |  | | |

Zones with larger average loads (e.g., NYC, LONGIL, CENTRL) therefore accommodate larger virtual
positions with lower price impact, while smaller or more constrained zones (e.g., MILLWD and NORTH)
exhibit higher sensitivity.

Finally, Table [14](https://arxiv.org/html/2601.05085v1#A1.T14 "Table 14 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports average correlations between forecast load
and the day-ahead loss and congestion components across zones.
Both components are consistently positively correlated with forecast load across all seasons and
time buckets, supporting the modeling assumption that higher forecasted load increases losses and
congestion in expectation.

## 5 Performance in NYISO

This section evaluates the empirical performance of the proposed trading strategy
when deployed in practice. All predictive models, impact parameters, and decision
thresholds are fixed based on the calibration and validation samples, and performance
is assessed out of sample on NYISO data from 2022–2025. In contrast to Section [4](https://arxiv.org/html/2601.05085v1#S4 "4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"), which focuses on model construction and optimal trade sizing, the results
reported here reflect the realized interaction between forecasting accuracy, market
impact, and cross-zonal portfolio allocation.

If the expected return in the validation set 2020–2021 is negative, we do not consider bidding for this zone, since our model was not able to give a successful prediction. Table [3](https://arxiv.org/html/2601.05085v1#S5.T3 "Table 3 ‣ 5 Performance in NYISO ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") suggests that we should not consider the North zone about INC predictions and the Long Island zone for the DEC predictions.

Table 3: Validation period (2020–2021): trade counts, average P&L (USD/MWh), and eligibility per zone.

| Zone | INC Trades | INC Avg Win | DEC Trades | DEC Avg Win |
| --- | --- | --- | --- | --- |
| NYC | 122 | 12.35 | 326 | 3.46 |
| LONGIL | 316 | 38.12 | 1705 | -1.07 |
| WEST | 152 | 5.21 | 307 | 9.76 |
| CENTRL | 36 | 2.26 | 61 | 17.41 |
| CAPITL | 75 | 0.63 | 206 | 11.00 |
| NORTH | 41 | -0.13 | 25 | 6.48 |
| DUNWOD | 49 | 7.72 | 189 | 3.03 |
| MILLWD | 56 | 18.81 | 167 | 0.82 |
| HUDVL | 47 | 3.30 | 159 | 9.92 |
| MHKVL | 33 | 2.65 | 52 | 16.47 |
| GENESE | 40 | 12.25 | 51 | 13.75 |

Notably, the optimal strategy does not trade each zone in isolation.
While the predictive model assigns to every zone–hour a directional signal
(INC for negative predicted DART and DEC for positive predicted DART),
the executed trades are determined jointly across zones.
In particular, it may allocate a position whose sign differs from
the local predicted direction.
For example, it can place a DEC in one zone while taking an INC in another,
even when both zones individually exhibit positive expected DART spreads.
This behavior is driven by the system-wide impact penalty kEk\_{\rm E}:
by taking offsetting positions, the strategy reduces aggregate exposure and
associated costs, allowing risk to be concentrated in zones where marginal
price impact is lowest.

As a result, a zone may exhibit negative realized P&L despite a correct
directional prediction.
To disentangle model accuracy from portfolio allocation effects, we therefore
report results in two complementary views.
The prediction view evaluates performance based solely on the model’s
directional signals, while the execution view reflects realized P&L
after optimization and cross-zone balancing, where we can see the results in Figure [7](https://arxiv.org/html/2601.05085v1#S5.F7 "Figure 7 ‣ 5 Performance in NYISO ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").

![Refer to caption](total.png)

![Refer to caption](inc_ex.png)


(a) INC — execution view

![Refer to caption](dec_ex.png)


(b) DEC — execution view

![Refer to caption](inc_pred.png)


(c) INC — prediction view

![Refer to caption](dec_pred.png)


(d) DEC — prediction view

Figure 7: Cumulative P&L: total (top) and by side and attribution view (bottom). All values are in USD.

Moreover, Table [15](https://arxiv.org/html/2601.05085v1#A1.T15 "Table 15 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports zone-level performance, while Table [16](https://arxiv.org/html/2601.05085v1#A1.T16 "Table 16 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") aggregates results across all zones for each test year.

Table [4](https://arxiv.org/html/2601.05085v1#S5.T4 "Table 4 ‣ 5 Performance in NYISO ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports, for each zone, the number of active trading hours, the average absolute position size, and the resulting P&L.
The largest virtual positions are taken in Long Island, which is consistent with its market characteristics: the zone combines frequent and sizable DART spikes with high average load, implying a relatively low marginal price impact per traded MWh.

Table 4: Per-zone attribution on the TEST period (2022–2025), execution view with dynamic q⋆q^{\star} and price impacts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Zone | Hours Active | Avg |q||q| (MW) | P&L (USD) |  |  |
| LONGIL | 571 | 118.70 | 6,004,480 |  |  |
| NYC | 1009 | 17.71 | 722,617 |  |  |
| MILLWD | 775 | 2.67 | 119,145 |  |  |
| GENESE | 397 | 8.91 | 118,976 |  |  |
| WEST | 1140 | 12.34 | 26,839 |  |  |
| NORTH | 160 | 3.32 | -10,806 |  |  |
| MHKVL | 426 | 12.64 | -101,829 |  |  |
| DUNWOD | 803 | 3.15 | -169,380 |  |  |
| CENTRL | 440 | 27.54 | -209,366 |  |  |
| CAPITL | 1026 | 14.34 | -355,918 |  |  |
| HUDVL | 733 | 9.10 | -384,604 |  |  |
| Total / Stats: |  |  | 5,760,154 |  |  |

A further validation of our assumptions on the energy-impact coefficients kEk\_{\rm E} comes from examining trading hours in which the strategy takes its largest day-ahead positions. On 24 June 2025—the most profitable day in the out-of-sample period—the strategy repeatedly submits large net buy (INC) positions during Summer Peak hours. Using the NYISO bid stack for these same hours, we recompute the day-ahead clearing price after shifting the residual demand curve upward by the executed quantity qtq\_{t} of MWh. This allows us to measure the realized one–sided price impact,

|  |  |  |
| --- | --- | --- |
|  | Δ​Pt=PtDA​(qt)−PtDA,\Delta P\_{t}\;=\;P^{\mathrm{DA}}\_{t}(q\_{t})-P^{\mathrm{DA}}\_{t}, |  |

and the corresponding empirical slope

|  |  |  |
| --- | --- | --- |
|  | Δ​Ptqt×1000($/MWh per 1000 MWh).\frac{\Delta P\_{t}}{q\_{t}}\times 1000\qquad(\text{\textdollar/MWh per 1000 MWh}). |  |

The results in Table [17](https://arxiv.org/html/2601.05085v1#A1.T17 "Table 17 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") show that the realized slopes lie between roughly 88 and 4141$/MWh per 1000 MWh. These magnitudes are fully consistent with the calibrated Summer–Peak coefficients kE+∈[34.64, 46.48]k\_{\rm E}^{+}\in[34.64,\,46.48]/1000MWh obtained from the perturbation experiments in Section [4.3](https://arxiv.org/html/2601.05085v1#S4.SS3 "4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"). Thus, the empirical price impact observed during the largest trading day strongly supports the validity of our linear approximation and our chosen parameter values.

### 5.1 Selective Spike Forecasting

On the 2022–2025 test period, the joint model exhibits a highly selective
forecasting behavior, characterized by high precision but low recall, as we can see from Tables [18](https://arxiv.org/html/2601.05085v1#A1.T18 "Table 18 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") and [19](https://arxiv.org/html/2601.05085v1#A1.T19 "Table 19 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
Average precision is approximately 0.300.30 for INC trades and 0.770.77 for DEC
trades, indicating relatively few false positives, while recall remains
around 0.040.04–0.050.05, meaning that only a small fraction of all realized
spike events is acted upon.
This pattern reflects a profit-oriented design: the strategy trades only
when the model assigns high confidence to extreme DART deviations, favoring
signal quality over coverage.

To assess whether the model is selecting economically relevant spikes
rather than arbitrary subsets of hours, Figures [10](https://arxiv.org/html/2601.05085v1#A1.F10 "Figure 10 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets")
and [11](https://arxiv.org/html/2601.05085v1#A1.F11 "Figure 11 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") compare the empirical distributions of realized
DART spikes with those selected by the model.
In each case, we compare both against the full sample of hours and against
the largest spike quantiles.
Across both hour-of-day and month-of-year dimensions, the model-selected
distributions align much more closely with the largest observed spikes than
with the unconditional sample.

This effect is quantified using the Jensen–Shannon (JS) divergence, a symmetric and bounded measure of dissimilarity between two probability distributions. Given distributions PP and QQ on a common support, define their mixture M=12​(P+Q)M=\tfrac{1}{2}(P+Q). The JS divergence is

|  |  |  |
| --- | --- | --- |
|  | JS(P∥Q)=12KL(P∥M)+12KL(Q∥M),\mathrm{JS}(P\|Q)=\frac{1}{2}\,\mathrm{KL}\!\left(P\middle\|M\right)+\frac{1}{2}\,\mathrm{KL}\!\left(Q\middle\|M\right), |  |

where KL​(P∥Q)=∑xP​(x)​log⁡(P​(x)Q​(x))\mathrm{KL}(P\|Q)=\sum\_{x}P(x)\log\!\big(\tfrac{P(x)}{Q(x)}\big) denotes the Kullback–Leibler divergence. We note that JS​(P∥Q)∈[0,log⁡2]\mathrm{JS}(P\|Q)\in[0,\log 2], with smaller values indicating more similar distributions Lin ([1991](https://arxiv.org/html/2601.05085v1#bib.bib27 "Divergence measures based on the Shannon entropy")).

In particular,

|  |  |  |
| --- | --- | --- |
|  | INC:JStop ​20%=0.039vs.JSall=0.094,\textbf{INC:}\quad\mathrm{JS}\_{\text{top }20\%}=0.039\quad\text{vs.}\quad\mathrm{JS}\_{\text{all}}=0.094, |  |

|  |  |  |
| --- | --- | --- |
|  | DEC:JStop ​5%=0.061vs.JSall=0.116.\textbf{DEC:}\quad\mathrm{JS}\_{\text{top }5\%}=0.061\quad\text{vs.}\quad\mathrm{JS}\_{\text{all}}=0.116. |  |

The substantially smaller divergences for the top spike quantiles show that
predicted trading hours are statistically closer to the most extreme realized
price deviations than to typical hours.
In other words, although the model captures only a small fraction of all
spikes, it disproportionately targets events that resemble the largest
historical DART dislocations, consistent with the subsequent profitability
of the trading strategy.

### 5.2 Enforcing Directional Consistency

In the baseline strategy, the portfolio optimizer is free to choose the sign of the zonal position qt,zq\_{t,z} so long as the resulting expected revenue (after impact) is positive. As a consequence, a zone can end up with an executed DEC position even in hours where the spike–forecasting model indicates a negative DART (and hence an INC position), or vice versa, because the optimizer may use offsetting positions across zones to reduce system-wide impact costs. To enforce a tighter link between forecasts and execution, we introduce a side-clipping rule: at each zone–hour we retain only the signal consistent with the predicted DART sign (INC if the model predicts negative DART, DEC if it predicts positive DART), and set all conflicting signals to zero before testing the strategy. This mechanism forces each traded hour to take positions only in the direction implied by the model’s sign prediction, while still allowing the optimizer to choose the trade size.

Figure [13](https://arxiv.org/html/2601.05085v1#A1.F13 "Figure 13 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") shows that this clipped strategy performs better on the 2022–2025 test set.
The total P&L increases relative to the unconstrained optimizer, and both the INC and DEC components become smoother and less noisy.

Table [23](https://arxiv.org/html/2601.05085v1#A1.T23 "Table 23 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports the per-zone attribution of the clipped strategy.
Restricting trades to the model-consistent direction reduces the number of active hours in some zones, but the remaining positions tend to have higher average profitability.
Long Island remains the dominant contributor, followed by New York City and Capital, reflecting the strength of DEC trades in these load pockets.

Overall, the clipped strategy preserves most of the performance of the full optimizer while improving interpretability and robustness.
By aligning trades strictly with the predicted sign of DART, it reduces contradictory positions and produces a cleaner mapping between forecasts and executed trades.

### 5.3 Restricting the Strategy to Statistically Significant Buckets

We revisit the previous strategy. However, now we split the evaluate our model by seasonality (Winter/Summer/Shoulder months)- and Peak/Off-Peak hours. Then, we
restrict attention to zone–season–band buckets that exhibit statistically
significant performance in the validation period (2020–2021).
Specifically, we retain only those buckets whose mean P&L has a tt-statistic
exceeding 22 and the number of trades is at least 5050, corresponding approximately to 95% confidence against a zero-mean null.

Under this restriction, the universe of traded zones shrinks substantially, as Tables [21](https://arxiv.org/html/2601.05085v1#A1.T21 "Table 21 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") and [22](https://arxiv.org/html/2601.05085v1#A1.T22 "Table 22 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") suggest.
On the INC side, only Long Island satisfies the significance criterion, whereas
on the DEC side the retained zones are Capital, Central, Long Island, New York
City, and West. All other zone–band combinations are excluded from trading in
the test period.

Figure [12](https://arxiv.org/html/2601.05085v1#A1.F12 "Figure 12 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") reports cumulative P&L over 2022–2025 for this
restricted strategy. As expected, total profits are slightly lower than in the
fully pooled specification, reflecting the reduced number of traded positions.
Nevertheless, performance remains strong, with the majority of gains concentrated
during the large summer 2025 spike episodes.

To assess predictive accuracy, Table [20](https://arxiv.org/html/2601.05085v1#A1.T20 "Table 20 ‣ A.4 Figures and Tables for the Optimal Trading Strategy ‣ Appendix A Appendix ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets") summarizes the fraction
of trades that coincide with realized spikes and the frequency with which the sign
of the DART spread is correctly predicted.
On the INC side, approximately 27% of trades occur during
realized positive spikes, and the model predicts the correct sign in 41% of
hours.
By contrast, DEC predictions are substantially more reliable: roughly 76% of
DEC trades coincide with negative spikes, and nearly 80% correctly predict the
spread sign.

Overall, this analysis highlights the asymmetry between INC and DEC
signals that we previously saw on Section [5.1](https://arxiv.org/html/2601.05085v1#S5.SS1 "5.1 Selective Spike Forecasting ‣ 5 Performance in NYISO ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"): while INC opportunities are sparse and harder to time reliably, DEC
signals exhibit both stronger statistical persistence and significantly higher
predictive accuracy, consistent with the validation-period evidence.

## 6 Conclusion

This paper analyzes day-ahead versus real-time (DART) spreads in U.S. organized wholesale electricity energy markets operated by Independent System Operators (ISOs),
and extends the framework of Galarneau-Vincent et al. ([2023](https://arxiv.org/html/2601.05085v1#bib.bib1 "Foreseeing the worst: forecasting electricity DART spikes")) in three main directions:
multi-zone spike forecasting, an explicitly calibrated price–impact model,
and the optimal scaling of virtual positions.
Working with NYISO, ISO–NE, and ERCOT, we construct leakage-free feature sets that
respect each ISO’s day-ahead bid deadline and estimate zone-specific logistic
regressions for both positive and negative DART spikes. The resulting models are
deliberately selective: they trade only when assigned high spike probabilities, thereby
prioritizing economic relevance over statistical coverage.

Our empirical results show that spike predictability is highly heterogeneous across
markets and zones. In ISO–NE and ERCOT, DART spreads are almost perfectly
synchronized across load zones, so a single representative node captures nearly all
useful variation. By contrast, NYISO exhibits much weaker and more dispersed
cross–zone correlations, driven by localized congestion and loss patterns. In this
environment, multi-zone modelling is essential: different zones deliver structurally
different DART distributions and support distinct INC/DEC opportunities. Long Island
emerges as the most profitable load pocket, combining frequent extreme spreads with
high average load, while several upstate zones offer weaker but still statistically
significant signals.

A central contribution of the paper is to move beyond unit-sized, impact-free backtests
and to construct an economically consistent link between trade size and expected price
response. Using historical day-ahead bid stacks, we estimate system-wide energy impact
coefficients and zone-specific congestion sensitivities, yielding a linear–quadratic
impact model for virtual load. Closed-form expressions for the optimal zonal
quantities show that portfolio-level decisions are shaped not only by local expected
revenues, but also by cross-zone interactions through the common energy component. In
particular, it can be optimal to take offsetting positions across zones in order to
concentrate risk where marginal price impact is lowest. Backtests that ignore this
feedback either overstate achievable profits or implicitly assume unrealistically small
position sizes.

From a trading perspective, the most stable opportunities arise on the DEC side.
Positive DART spikes (which generate DEC profits) occur more frequently and with greater statistical regularity, and the forecasting model identifies these events with higher precision. In contrast, INC opportunities—driven by negative DART spikes—are substantially more lucrative when they occur, but they are rarer, more volatile, and more sensitive to threshold selection and market-impact assumptions. As a result, DEC strategies deliver smoother and more persistent returns, whereas INC strategies contribute occasional but very large profit bursts. Restricting trades to directions consistent with the model’s sign prediction and to statistically significant zone–season–band buckets preserves most of the economic value while improving robustness and interpretability.

Several extensions of this study offer promising directions for further research.
First, the backtesting framework could be enriched by replacing our linear impact proxy with
realized day-ahead price perturbations computed directly from historical bid stacks, thereby
evaluating the strategy under the true system response rather than a parametric approximation.
Second, more expressive structural models of market impact—for example, piecewise-linear,
nonlinear, or congestion-regime–dependent formulations—may better capture the heterogeneity of
supply curves across zones and seasons.
Third, the economic value of the spike forecasts could be explored through alternative financial
instruments beyond virtual INC/DEC trades, such as Financial Transmission Rights (FTRs) or other
hedging products that monetize congestion patterns.
Together, these extensions would move the methodology closer to a full market-consistent execution
framework and broaden its applicability across different trading environments.

## References

* [1]
  R. Aïd, P. Gruet, and H. Pham (2016)
  An optimal trading problem in intraday electricity markets.
  Mathematics and Financial Economics 10 (1),  pp. 49–85.
  Cited by: [§4.1](https://arxiv.org/html/2601.05085v1#S4.SS1.p3.5 "4.1 Price Impact Model ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [2]
  R. Almgren and N. Chriss (2001)
  Optimal execution of portfolio transactions.
  Journal of Risk 3 (2),  pp. 5–39.
  Cited by: [§4.1](https://arxiv.org/html/2601.05085v1#S4.SS1.p3.5 "4.1 Price Impact Model ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [3]
  S. Borenstein, J. B. Bushnell, and F. A. Wolak (2002-12)
  Measuring market inefficiencies in California’s restructured wholesale electricity market.
  American Economic Review 92 (5),  pp. 1376–1405.
  External Links: [Document](https://dx.doi.org/10.1257/000282802762024557),
  [Link](https://www.aeaweb.org/articles?id=10.1257/000282802762024557)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [4]
  T. M. Christensen, S. Hurn, and K. Lindsay (2012)
  Forecasting spikes in electricity prices.
  International Journal of Forecasting 28 (2),  pp. 400–411.
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p1.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [5]
  M. Coulon and S. Howison (2009)
  Stochastic behaviour of the electricity bid stack: from fundamental drivers to power prices.
  The Journal of Energy Markets 2 (1),  pp. 29–69.
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [§4.3](https://arxiv.org/html/2601.05085v1#S4.SS3.p1.8 "4.3 Estimating the energy-impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [6]
  M. Coulon, W. B. Powell, and R. Sircar (2013)
  A model for hedging load and price risk in the Texas electricity market.
  Energy Economics 40,  pp. 976–988.
  External Links: [Document](https://dx.doi.org/10.1016/j.eneco.2013.05.020)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [7]
  Electric Reliability Council of Texas (2025)
  ERCOT market data.
  Note: <https://www.ercot.com>Accessed for Day-Ahead and Real-Time prices, load forecasts, and market data
  Cited by: [§2.1](https://arxiv.org/html/2601.05085v1#S2.SS1.p1.1 "2.1 Data Construction ‣ 2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [8]
  A. Forgetta, F. Godin, and M. Augustyniak (2025)
  Distributional forecasting of electricity DART spreads with a covariate-dependent mixture model.
  Energy Economics 144,  pp. 108332.
  External Links: ISSN 0140-9883,
  [Document](https://dx.doi.org/10.1016/j.eneco.2025.108332)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [9]
  R. Galarneau-Vincent, G. Gauthier, and F. Godin (2023)
  Foreseeing the worst: forecasting electricity DART spikes.
  Energy Economics 119,  pp. 1–18.
  External Links: [Document](https://dx.doi.org/10.1016/j.eneco.2023.106521)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.SS0.SSS0.Px1.p1.1 "Contributions. ‣ 1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [§1](https://arxiv.org/html/2601.05085v1#S1.p4.2 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [§2.2](https://arxiv.org/html/2601.05085v1#S2.SS2.p3.6 "2.2 Feature Labeling ‣ 2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [§3.1](https://arxiv.org/html/2601.05085v1#S3.SS1.p1.4 "3.1 Benchmark INC and DEC Strategies ‣ 3 Empirical Performance of Benchmark Strategies ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [§6](https://arxiv.org/html/2601.05085v1#S6.p1.1 "6 Conclusion ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets](https://arxiv.org/html/2601.05085v1#id1.id1 "Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [10]
  J. Gatheral (2010)
  No-dynamic-arbitrage and market impact.
  Quantitative Finance 10 (7),  pp. 749–759.
  Cited by: [§4.1](https://arxiv.org/html/2601.05085v1#S4.SS1.p3.5 "4.1 Price Impact Model ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [11]
  T. Hastie, R. Tibshirani, and J. Friedman (2009)
  The elements of statistical learning: data mining, inference, and prediction.
  2 edition, Springer.
  Cited by: [§2.3](https://arxiv.org/html/2601.05085v1#S2.SS3.p3.1 "2.3 Spike Definition and Logistic Regression Models ‣ 2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [12]
  ISO New England (2025)
  FAQs: locational marginal pricing.
  Note: Accessed: 2025-03
  External Links: [Link](https://www.iso-ne.com/participate/support/faq/lmp)
  Cited by: [§4.1](https://arxiv.org/html/2601.05085v1#S4.SS1.p2.2 "4.1 Price Impact Model ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [13]
  ISO New England (2025)
  ISO New England markets and operations data.
  Note: <https://www.iso-ne.com/markets-operations/markets>Accessed for Day-Ahead and Real-Time prices, load forecasts, and market data
  Cited by: [§2.1](https://arxiv.org/html/2601.05085v1#S2.SS1.p1.1 "2.1 Data Construction ‣ 2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [14]
  Kelly Stegmann, Mathangi Srinivasan Kumar, and Gina E. Craan (2025-09)
  Congestion price component.
  Technical report
   New York Independent System Operator (NYISO).
  Note: LBMP In-Depth Course, Remote Learning
  External Links: [Link](https://www.nyiso.com/documents/20142/25467833/LBMP-Congestion-Price-Component.pdf)
  Cited by: [§4.4](https://arxiv.org/html/2601.05085v1#S4.SS4.p4.2 "4.4 Estimating local impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [15]
  M. S. Kumar (2025-10)
  Locational based marginal pricing.
   New York Independent System Operator (NYISO).
  Note: New York Market Orientation Course (NYMOC), Rensselaer, NY
  External Links: [Link](https://www.nyiso.com/documents/20142/3037451/3-LMBP.pdf/f7682e03-e921-eaab-09bf-690524b5ade6)
  Cited by: [§4.1](https://arxiv.org/html/2601.05085v1#S4.SS1.p2.2 "4.1 Price Impact Model ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [16]
  J. Lago, G. Marcjasz, B. De Schutter, and R. Weron (2021)
  Forecasting day-ahead electricity prices: a review of state-of-the-art algorithms, best practices and an open-access benchmark.
  Applied Energy 293,  pp. 116983.
  External Links: ISSN 0306-2619,
  [Document](https://dx.doi.org/10.1016/j.apenergy.2021.116983)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [17]
  D. Liebl (2013)
  Modeling and forecasting electricity spot prices: a functional data perspective.
  The Annals of Applied Statistics 7 (3),  pp. 1562–1592.
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p1.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [18]
  J. Lin (1991)
  Divergence measures based on the Shannon entropy.
  IEEE Transactions on Information Theory 37 (1),  pp. 145–151.
  Cited by: [§5.1](https://arxiv.org/html/2601.05085v1#S5.SS1.p3.5 "5.1 Selective Spike Forecasting ‣ 5 Performance in NYISO ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [19]
  F. A. Longstaff and A. W. Wang (2004)
  Electricity forward prices: a high-frequency empirical analysis.
  Journal of Finance 59 (4),  pp. 1877–1900.
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p1.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets"),
  [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [20]
  New York Independent System Operator (2025)
  NYISO market data.
  Note: <https://www.nyiso.com>Accessed for Day-Ahead and Real-Time prices, load forecasts, and market data
  Cited by: [§2.1](https://arxiv.org/html/2601.05085v1#S2.SS1.p1.1 "2.1 Data Construction ‣ 2 Predictive Framework and Statistical Model ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [21]
  J. Nowotarski, E. Raviv, S. Trück, and R. Weron (2014)
  An empirical comparison of alternative schemes for combining electricity spot price forecasts.
  Energy Economics 46,  pp. 395–412.
  External Links: ISSN 0140-9883,
  [Document](https://dx.doi.org/10.1016/j.eneco.2014.07.014)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p1.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [22]
  NYISO (2024-12)
  Locational minimum installed capacity requirements study for the 2024–2025 capability year.
  Technical report
   New York Independent System Operator (NYISO).
  External Links: [Link](https://www.nyiso.com/documents/20142/42519933/2024-2025-LCR-Report.pdf)
  Cited by: [§4.4](https://arxiv.org/html/2601.05085v1#S4.SS4.p4.2 "4.4 Estimating local impact coefficients ‣ 4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [23]
  H. S. Sandhu, L. Fang, and L. Guan (2016)
  Forecasting day-ahead price spikes for the ontario electricity market.
  Electric Power Systems Research 141,  pp. 450–459.
  External Links: ISSN 0378-7796,
  [Document](https://dx.doi.org/10.1016/j.epsr.2016.08.005)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p1.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
* [24]
  X. Wang, S. K. Magableh, O. Dawaghreh, C. Wang, J. Gong, Z. Zhao, and M. H. Liao (2024)
  Deep learning-based electricity price forecast for virtual bidding in wholesale electricity market.
  External Links: 2412.00062,
  [Link](https://arxiv.org/abs/2412.00062)
  Cited by: [§1](https://arxiv.org/html/2601.05085v1#S1.p3.1 "1 Introduction ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").

## Appendix A Appendix

### A.1 Tables and Figures for NYISO

![Refer to caption](CAPITL_INC.png)


(a) CAPITL — INC

![Refer to caption](CAPITL_DEC.png)


(b) CAPITL — DEC

![Refer to caption](CENTRL_INC.png)


(c) CENTRL — INC

![Refer to caption](CENTRL_DEC.png)


(d) CENTRL — DEC

![Refer to caption](NORTH_INC.png)


(e) NORTH — INC

![Refer to caption](NORTH_DEC.png)


(f) NORTH — DEC

![Refer to caption](WEST_INC.png)


(g) WEST — INC

![Refer to caption](WEST_DEC.png)


(h) WEST — DEC

Figure 8: NYISO: cumulative P&L by zone for remaining regions under the INC/DEC benchmark strategy.




Table 5: NYISO: per-year P&L by zone (INC only benchmark strategy)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Year | CAPITL | CENTRL | LONGIL | NORTH | NYC | WEST |
| 2022 | 17,855 | 14,673 | 22,315 | 11,632 | 16,254 | 1,457 |
| 2023 | -886 | -353 | 3,163 | -2,559 | -2,582 | 679 |
| 2024 | -1,383 | 371 | 3,065 | 754 | 3,966 | 454 |
| 2025 | 8,731 | 7,409 | 24,445 | 1,776 | 23,035 | 5,162 |
| Total | 24,316 | 22,099 | 52,988 | 11,602 | 40,673 | 7,752 |




Table 6: NYISO: per-year P&L by zone (DEC only benchmark strategy)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Year | CAPITL | CENTRL | LONGIL | NORTH | NYC | WEST |
| 2022 | 10,749 | 8,287 | 6,879 | 6,427 | 8,705 | 6,082 |
| 2023 | 5,299 | 2,970 | 3,035 | 960 | 3,782 | 4,011 |
| 2024 | 6,288 | 3,057 | 5,020 | 2,135 | 2,425 | 2,100 |
| 2025 | 15,880 | 6,454 | 1,769 | 2,728 | 1,932 | 4,322 |
| Total | 38,215 | 20,768 | 16,703 | 12,250 | 16,844 | 16,516 |




Table 7: NYISO: yearly mean of DART spreads by zone

| Year | CAPITL | CENTRL | LONGIL | NORTH | NYC | WEST |
| --- | --- | --- | --- | --- | --- | --- |
| 2015 | 0.33 | 0.27 | 1.09 | 0.25 | 0.54 | -1.82 |
| 2016 | 0.67 | 0.20 | 0.67 | 0.25 | -0.02 | -0.13 |
| 2017 | 0.47 | -0.11 | 1.40 | 1.27 | 0.90 | -0.31 |
| 2018 | -0.17 | -0.49 | 0.80 | -0.54 | -1.02 | -0.01 |
| 2019 | 1.06 | 0.48 | -0.56 | -0.11 | 0.71 | -0.29 |
| 2020 | -0.08 | -0.10 | -0.08 | -0.60 | -0.60 | -0.03 |
| 2021 | 0.40 | 0.33 | -0.84 | -0.79 | 0.03 | 0.08 |
| 2022 | -2.51 | -2.10 | -2.37 | -1.56 | -2.80 | 0.58 |
| 2023 | 1.76 | 0.29 | -0.29 | 1.02 | 0.47 | 1.27 |
| 2024 | 1.38 | 0.54 | 1.20 | 0.06 | -0.09 | 0.95 |
| 2025 | 1.62 | -0.68 | -3.18 | -0.14 | -4.05 | 0.50 |

### A.2 DART Correlation Across Zones

Table 8: Correlation of DART spikes across NYISO zones (2015–2025)

|  | CAPITL | CENTRL | DUNWOD | GENESE | HUDVL | LONGIL | MHKVL | MILLWD | NORTH | NYC | WEST |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAPITL | 1.0001.000 | 0.7100.710 | 0.7780.778 | 0.6880.688 | 0.8670.867 | 0.6030.603 | 0.7180.718 | 0.8340.834 | 0.4650.465 | 0.7540.754 | 0.5620.562 |
| CENTRL | 0.7100.710 | 1.0001.000 | 0.7760.776 | 0.9870.987 | 0.8640.864 | 0.6180.618 | 0.9900.990 | 0.8270.827 | 0.7370.737 | 0.7550.755 | 0.8100.810 |
| DUNWOD | 0.7780.778 | 0.7760.776 | 1.0001.000 | 0.7590.759 | 0.9040.904 | 0.7470.747 | 0.7800.780 | 0.9660.966 | 0.5330.533 | 0.9650.965 | 0.6090.609 |
| GENESE | 0.6880.688 | 0.9870.987 | 0.7590.759 | 1.0001.000 | 0.8440.844 | 0.6060.606 | 0.9780.978 | 0.8080.808 | 0.7280.728 | 0.7380.738 | 0.7970.797 |
| HUDVL | 0.8670.867 | 0.8640.864 | 0.9040.904 | 0.8440.844 | 1.0001.000 | 0.7130.713 | 0.8640.864 | 0.9600.960 | 0.5940.594 | 0.8790.879 | 0.6790.679 |
| LONGIL | 0.6030.603 | 0.6180.618 | 0.7470.747 | 0.6060.606 | 0.7130.713 | 1.0001.000 | 0.6180.618 | 0.7440.744 | 0.4150.415 | 0.7260.726 | 0.4840.484 |
| MHKVL | 0.7180.718 | 0.9900.990 | 0.7800.780 | 0.9780.978 | 0.8640.864 | 0.6180.618 | 1.0001.000 | 0.8290.829 | 0.7840.784 | 0.7580.758 | 0.7860.786 |
| MILLWD | 0.8340.834 | 0.8270.827 | 0.9660.966 | 0.8080.808 | 0.9600.960 | 0.7440.744 | 0.8290.829 | 1.0001.000 | 0.5700.570 | 0.9350.935 | 0.6490.649 |
| NORTH | 0.4650.465 | 0.7370.737 | 0.5330.533 | 0.7280.728 | 0.5940.594 | 0.4150.415 | 0.7840.784 | 0.5700.570 | 1.0001.000 | 0.5190.519 | 0.5570.557 |
| NYC | 0.7540.754 | 0.7550.755 | 0.9650.965 | 0.7380.738 | 0.8790.879 | 0.7260.726 | 0.7580.758 | 0.9350.935 | 0.5190.519 | 1.0001.000 | 0.5930.593 |
| WEST | 0.5620.562 | 0.8100.810 | 0.6090.609 | 0.7970.797 | 0.6790.679 | 0.4840.484 | 0.7860.786 | 0.6490.649 | 0.5570.557 | 0.5930.593 | 1.0001.000 |




Table 9: Correlation of DART spreads across ISO–NE zones (2018–2025).

| Region | CT | ME | NEMASS | NH | RI | SEMASS | VT | WCMASS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CT | 1.000 | 0.988 | 0.995 | 0.996 | 0.995 | 0.995 | 0.999 | 0.998 |
| ME | 0.988 | 1.000 | 0.993 | 0.994 | 0.993 | 0.993 | 0.990 | 0.993 |
| NEMASS | 0.995 | 0.993 | 1.000 | 0.999 | 0.999 | 0.999 | 0.995 | 0.998 |
| NH | 0.996 | 0.994 | 0.999 | 1.000 | 0.999 | 0.999 | 0.997 | 0.999 |
| RI | 0.995 | 0.993 | 0.999 | 0.999 | 1.000 | 1.000 | 0.996 | 0.999 |
| SEMASS | 0.995 | 0.993 | 0.999 | 0.999 | 1.000 | 1.000 | 0.996 | 0.999 |
| VT | 0.999 | 0.990 | 0.995 | 0.997 | 0.996 | 0.996 | 1.000 | 0.999 |
| WCMASS | 0.998 | 0.993 | 0.998 | 0.999 | 0.999 | 0.999 | 0.999 | 1.000 |




Table 10: Correlation matrix of DART across ERCOT zones (2018–2025).

| Zone | NORTH | SOUTH | WEST | HOUSTON |
| --- | --- | --- | --- | --- |
| NORTH | 1.000 | 0.991 | 0.998 | 0.980 |
| SOUTH | 0.991 | 1.000 | 0.991 | 0.981 |
| WEST | 0.998 | 0.991 | 1.000 | 0.978 |
| HOUSTON | 0.980 | 0.981 | 0.978 | 1.000 |

### A.3 NYISO, ISO–NE & ERCOT Quantiles

Table 11: Empirical DART quantiles (USD/MWh) on the training sets for NYISO LONGIL, ISO–NE ME, and ERCOT WEST.

| Quantile | LONGIL (NYISO) | ME (ISO–NE) | WEST (ERCOT) |
| --- | --- | --- | --- |
| Q0.00Q\_{0.00} | -2434.97 | -109.17 | -5891.08 |
| Q0.01Q\_{0.01} | -121.57 | -29.60 | -77.20 |
| Q0.05Q\_{0.05} | -34.95 | -13.39 | -13.74 |
| Q0.10Q\_{0.10} | -16.33 | -7.10 | -7.65 |
| Q0.25Q\_{0.25} | -3.09 | -1.51 | -2.02 |
| Q0.50Q\_{0.50} | 3.98 | 1.33 | 0.97 |
| Q0.75Q\_{0.75} | 11.21 | 4.62 | 4.96 |
| Q0.90Q\_{0.90} | 20.27 | 9.31 | 11.39 |
| Q0.95Q\_{0.95} | 29.18 | 14.03 | 17.39 |
| Q0.99Q\_{0.99} | 58.25 | 27.75 | 40.39 |
| Q1.00Q\_{1.00} | 1506.76 | 69.03 | 7675.51 |

### A.4 Figures and Tables for the Optimal Trading Strategy

This subsection collects supplementary calibration results, diagnostic plots, and
robustness checks underlying the trading strategy in Section [4](https://arxiv.org/html/2601.05085v1#S4 "4 Optimal Trading Strategy ‣ Trading Electrons: Predicting DART Spread Spikes in ISO Electricity Markets").
It includes (i) price–impact estimates by season and load band,
(ii) validation and test–set execution diagnostics,
and (iii) additional performance breakdowns and distributional comparisons.

Table 12: (Loss – Congestion) impact on LMP for a +1000 MW zonal load change ($/MWh), 2015–2021.

|  | Shoulder | | Summer | | Winter | |
| --- | --- | --- | --- | --- | --- | --- |
| Zone | Off-Peak | Peak | Off-Peak | Peak | Off-Peak | Peak |
| CAPITL | 8.568.56 | 2.362.36 | −7.86-7.86 | 0.860.86 | 63.4163.41 | 79.5479.54 |
| CENTRL | 2.612.61 | 2.872.87 | −0.37-0.37 | 2.392.39 | 4.164.16 | 4.564.56 |
| DUNWOD | 3.613.61 | 9.369.36 | −5.20-5.20 | 11.3911.39 | 111.28111.28 | 104.13104.13 |
| GENESE | 1.761.76 | 1.701.70 | −0.41-0.41 | 1.211.21 | 1.491.49 | 0.040.04 |
| HUDVL | 9.519.51 | 5.915.91 | −3.51-3.51 | 5.045.04 | 68.7568.75 | 65.5165.51 |
| LONGIL | 4.954.95 | 7.827.82 | 5.065.06 | 17.7317.73 | 43.6343.63 | 43.3043.30 |
| MHKVL | 5.305.30 | 4.864.86 | −0.37-0.37 | 4.214.21 | 13.1813.18 | 18.2718.27 |
| MILLWD | 52.7052.70 | 46.1746.17 | −11.37-11.37 | 25.6925.69 | 189.06189.06 | 192.38192.38 |
| NORTH | 0.260.26 | 3.803.80 | −19.55-19.55 | −44.72-44.72 | −2.82-2.82 | −0.91-0.91 |
| NYC | −0.25-0.25 | 1.291.29 | −0.05-0.05 | 2.182.18 | 13.2113.21 | 12.2912.29 |
| WEST | 1.881.88 | 14.3614.36 | −0.54-0.54 | 25.7325.73 | 1.541.54 | 1.111.11 |




Table 13: Average forecast load (MW) by zone, season, and Peak/Off-Peak, 2015–2021.

|  | Shoulder | | Summer | | Winter | |
| --- | --- | --- | --- | --- | --- | --- |
| Zone | Off-Peak | Peak | Off-Peak | Peak | Off-Peak | Peak |
| CAPITL | 1,133.21,133.2 | 1,336.21,336.2 | 1,330.31,330.3 | 1,645.61,645.6 | 1,294.11,294.1 | 1,486.91,486.9 |
| CENTRL | 1,503.01,503.0 | 1,785.71,785.7 | 1,629.51,629.5 | 2,041.02,041.0 | 1,728.31,728.3 | 2,003.52,003.5 |
| DUNWOD | 542.8542.8 | 676.9676.9 | 706.1706.1 | 906.1906.1 | 597.4597.4 | 720.3720.3 |
| GENESE | 918.8918.8 | 1,124.11,124.1 | 1,057.91,057.9 | 1,367.41,367.4 | 1,023.31,023.3 | 1,220.31,220.3 |
| HUDVL | 879.3879.3 | 1,053.31,053.3 | 1,073.41,073.4 | 1,376.31,376.3 | 1,012.01,012.0 | 1,172.01,172.0 |
| LONGIL | 1,887.41,887.4 | 2,327.42,327.4 | 2,636.22,636.2 | 3,435.63,435.6 | 2,061.72,061.7 | 2,462.32,462.3 |
| MHKVL | 632.3632.3 | 767.0767.0 | 674.4674.4 | 866.9866.9 | 786.5786.5 | 925.6925.6 |
| MILLWD | 250.4250.4 | 309.6309.6 | 309.2309.2 | 404.6404.6 | 305.3305.3 | 362.5362.5 |
| NORTH | 499.4499.4 | 532.5532.5 | 484.8484.8 | 531.3531.3 | 586.6586.6 | 619.9619.9 |
| NYC | 4,819.94,819.9 | 6,102.06,102.0 | 6,307.26,307.2 | 7,926.57,926.5 | 5,074.95,074.9 | 6,249.16,249.1 |
| WEST | 1,479.61,479.6 | 1,734.21,734.2 | 1,637.31,637.3 | 2,004.42,004.4 | 1,624.41,624.4 | 1,872.31,872.3 |

![Refer to caption](100_random.png)


Figure 9: Scatter of (Forecasted Load,Loss+Congestion) for 100 random Summer–Peak hours in LONGIL.




Table 14: Average correlations across NYISO zones between forecast load and DA congestion/loss components, by season and Peak/Off-Peak bucket (2015–2021).

| Season – Bucket | Corr(Forecast Load, LossesDA) | Corr(Forecast Load, CongestionDA) |
| --- | --- | --- |
| Shoulder – Off-Peak | 0.317 | 0.0500.050 |
| Shoulder – Peak | 0.373 | 0.0730.073 |
| Summer – Off-Peak | 0.352 | 0.112 |
| Summer – Peak | 0.397 | 0.1770.177 |
| Winter – Off-Peak | 0.314 | 0.2390.239 |
| Winter – Peak | 0.274 | 0.2380.238 |




Table 15: Execution-view P&L by zone, aggregated over 2022–2025 (USD).

| Zone | INC (Exec) | DEC (Exec) | Total |
| --- | --- | --- | --- |
| CAPITL | -6,564 | -349,354 | -355,918 |
| CENTRL | -3,052 | -206,313 | -209,365 |
| DUNWOD | -38,177 | -131,202 | -169,379 |
| GENESE | 49,801 | 69,174 | 119,975 |
| HUDVL | -3,023 | -411,510 | -414,533 |
| LONGIL | 6,004,479 | 0 | 6,004,479 |
| MHKVL | -1,178 | -101,653 | -102,831 |
| MILLWD | 128,091 | -8,946 | 119,145 |
| NORTH | -14,361 | 3,556 | -10,805 |
| NYC | 778,698 | -56,080 | 722,618 |
| WEST | 685 | 26,153 | 26,838 |




Table 16: Yearly total P&L by view and side (USD).

| Year | INC (Exec) | DEC (Exec) | INC (Pred) | DEC (Pred) | Total (Pred) |
| --- | --- | --- | --- | --- | --- |
| 2022 | 915,311 | -201,181 | 411,226 | 302,904 | 714,130 |
| 2023 | 336,339 | -93,707 | 198,424 | 44,207 | 242,631 |
| 2024 | -185,819 | 296,156 | -68,264 | 178,601 | 110,337 |
| 2025 | 5,829,911 | -1,136,856 | 4,560,358 | 132,698 | 4,693,055 |




Table 17: Realized day-ahead price impact on 24 June 2025 for the executed net INC portfolio and the corresponding DART in Long Island (NYISO, upward shift of residual demand by qtq\_{t} MWh).

| Hour | qtq\_{t} | PtDAP^{\mathrm{DA}}\_{t} | PtDA​(qt)P^{\mathrm{DA}}\_{t}(q\_{t}) | Δ​Pt\Delta P\_{t} ($/MWh) | 1000​Δ​Pt/qt1000\,\Delta P\_{t}/q\_{t} | DART |
| --- | --- | --- | --- | --- | --- | --- |
| 15:00 | 72.672.6 | 209.41209.41 | 210.92210.92 | 1.511.51 | 20.8020.80 | −1,159.57-1,159.57 |
| 16:00 | 85.985.9 | 222.59222.59 | 224.79224.79 | 2.202.20 | 25.6125.61 | −934.65-934.65 |
| 17:00 | 159.9159.9 | 250.58250.58 | 255.90255.90 | 5.325.32 | 33.2733.27 | −3,725.93-3,725.93 |
| 18:00 | 163.1163.1 | 224.79224.79 | 226.59226.59 | 1.801.80 | 11.0411.04 | −4,372.52-4,372.52 |
| 19:00 | 163.8163.8 | 201.72201.72 | 203.14203.14 | 1.421.42 | 8.678.67 | −1,798.57-1,798.57 |
| 20:00 | 161.3161.3 | 170.00170.00 | 176.57176.57 | 6.576.57 | 40.7340.73 | −534.26-534.26 |
| 21:00 | 134.2134.2 | 153.00153.00 | 155.00155.00 | 2.002.00 | 14.9014.90 | −145.64-145.64 |




Table 18: TEST precision/recall/F1 by zone for INC predicted.

| zone | precision | recall | f1 | TP | FP | FN | TN | support\_pos | N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LONGIL | 0.270 | 0.066 | 0.107 | 154 | 417 | 2167 | 29250 | 2321 | 31988 |
| WEST | 0.216 | 0.063 | 0.097 | 71 | 257 | 1064 | 30572 | 1135 | 31964 |
| NYC | 0.291 | 0.047 | 0.080 | 75 | 183 | 1535 | 30171 | 1610 | 31964 |
| MILLWD | 0.323 | 0.042 | 0.075 | 63 | 132 | 1430 | 31851 | 1493 | 33476 |
| CAPITL | 0.309 | 0.041 | 0.072 | 73 | 163 | 1714 | 30014 | 1787 | 31964 |
| HUDVL | 0.302 | 0.041 | 0.072 | 57 | 132 | 1347 | 31940 | 1404 | 33476 |
| DUNWOD | 0.309 | 0.040 | 0.071 | 60 | 134 | 1433 | 31849 | 1493 | 33476 |
| CENTRL | 0.310 | 0.035 | 0.063 | 45 | 100 | 1230 | 30589 | 1275 | 31964 |
| GENESE | 0.314 | 0.034 | 0.062 | 43 | 94 | 1206 | 32133 | 1249 | 33476 |
| MHKVL | 0.295 | 0.033 | 0.060 | 44 | 105 | 1276 | 32051 | 1320 | 33476 |
| NORTH | 0.343 | 0.030 | 0.056 | 49 | 94 | 1564 | 30281 | 1613 | 31988 |




Table 19: TEST precision/recall/F1 by zone for DEC predicted.

| zone | precision | recall | f1 | TP | FP | FN | TN | support\_pos | N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LONGIL | 0.645 | 0.146 | 0.238 | 2035 | 1118 | 11902 | 16933 | 13937 | 31988 |
| WEST | 0.747 | 0.059 | 0.110 | 635 | 215 | 10086 | 21028 | 10721 | 31964 |
| CAPITL | 0.795 | 0.052 | 0.098 | 635 | 164 | 11584 | 19581 | 12219 | 31964 |
| NYC | 0.722 | 0.050 | 0.093 | 560 | 216 | 10723 | 20465 | 11283 | 31964 |
| DUNWOD | 0.782 | 0.040 | 0.077 | 480 | 134 | 11386 | 21476 | 11866 | 33476 |
| MILLWD | 0.776 | 0.038 | 0.073 | 453 | 131 | 11383 | 21509 | 11836 | 33476 |
| HUDVL | 0.801 | 0.037 | 0.071 | 442 | 110 | 11466 | 21458 | 11908 | 33476 |
| CENTRL | 0.786 | 0.023 | 0.046 | 235 | 64 | 9795 | 21870 | 10030 | 31964 |
| MHKVL | 0.796 | 0.020 | 0.040 | 223 | 57 | 10675 | 22521 | 10898 | 33476 |
| GENESE | 0.792 | 0.020 | 0.039 | 209 | 55 | 10338 | 22874 | 10547 | 33476 |
| NORTH | 0.776 | 0.013 | 0.025 | 125 | 36 | 9725 | 22102 | 9850 | 31988 |



![Refer to caption](top_20_hour.png)


(a) INC — Actual top 20% vs. predicted

![Refer to caption](top_5_hour.png)


(b) DEC — Actual top 5% vs. predicted

![Refer to caption](all_hour_inc.png)


(c) INC — All hours vs. predicted

![Refer to caption](all_hour_dec.png)


(d) DEC — All hours vs. predicted

Figure 10: Predicted vs. realized spike PDFs across hour of day
(test period 2022–2025).



![Refer to caption](top_20_month.png)


(a) INC — Actual top 20% vs. predicted

![Refer to caption](top_5_month.png)


(b) DEC — Actual top 5% vs. predicted

![Refer to caption](all_month_inc.png)


(c) INC — All months vs. predicted

![Refer to caption](all_month_dec.png)


(d) DEC — All months vs. predicted

Figure 11: Predicted vs. realized spike PDFs across month of year
(test period 2022–2025).



![Refer to caption](INC_NEW.png)


(a) INC

![Refer to caption](DEC_NEW.png)


(b) DEC

![Refer to caption](PNL_NEW.png)


(c) Total

Figure 12: Cumulative P&L for the restricted (statistically significant) strategy,
test period 2022–2025.




Table 20: Prediction quality on the 2022–2025 test set for the restricted strategy.

| Side | Trades | Spikes | Correct sign |
| --- | --- | --- | --- |
| INC | 571 | 154 (27.0%) | 232 (40.6%) |
| DEC | 2720 | 2065 (75.9%) | 2173 (79.9%) |




Table 21: VALID 2020–2021, INC side: mean P&L (USD/MWh) and number of trades by zone, season and band.

| Zone | W P | W O | Su P | Su O | Sh P | Sh O |
| --- | --- | --- | --- | --- | --- | --- |
| CAPITL | 16.24 (11) | – | -5.75 (57) | – | 28.11 (7) | – |
| CENTRL | -3.82 (5) | – | -2.04 (26) | – | 30.73 (5) | – |
| DUNWOD | 6.43 (7) | – | 4.95 (36) | – | 25.85 (6) | – |
| GENESE | -4.32 (5) | – | 17.47 (31) | – | -7.44 (4) | – |
| HUDVL | 15.17 (6) | – | -2.50 (36) | – | 30.81 (5) | – |
| LONGIL | 19.20 (47) | – | 44.50 (246) | – | 8.60 (23) | – |
| MHKVL | -3.73 (5) | – | -1.32 (24) | – | 34.43 (4) | – |
| MILLWD | 7.61 (7) | – | 19.64 (43) | – | 25.95 (6) | – |
| NORTH | -9.10 (6) | – | -2.34 (31) | – | 30.43 (4) | – |
| NYC | 4.31 (8) | – | 12.30 (107) | – | 22.37 (7) | – |
| WEST | 3.08 (19) | – | 5.96 (116) | – | 2.46 (17) | – |




Table 22: VALID 2020–2021, DEC side: mean P&L (USD/MWh) and number of trades by zone, season and band.

| Zone | W P | W O | Su P | Su O | Sh P | Sh O |
| --- | --- | --- | --- | --- | --- | --- |
| CAPITL | 27.94 (50) | – | 6.24 (149) | – | -8.64 (7) | – |
| CENTRL | 41.40 (7) | 21.82 (1) | 14.06 (51) | – | 16.52 (2) | – |
| DUNWOD | 29.13 (48) | – | -6.55 (134) | – | 7.45 (7) | – |
| GENESE | 36.22 (5) | 22.67 (1) | 11.26 (43) | – | 6.71 (2) | – |
| HUDVL | 31.37 (29) | – | 4.93 (125) | – | 10.36 (5) | – |
| LONGIL | 1.89 (814) | 49.54 (5) | -7.50 (655) | – | 5.61 (231) | – |
| MHKVL | 43.09 (7) | 23.22 (1) | 12.03 (43) | – | 14.43 (1) | – |
| MILLWD | 28.71 (43) | – | -9.72 (118) | – | 8.19 (6) | – |
| NORTH | 28.44 (2) | 27.61 (1) | 3.36 (18) | – | 4.24 (4) | – |
| NYC | 27.93 (66) | – | -3.08 (252) | – | 7.76 (8) | – |
| WEST | 15.06 (81) | 21.58 (1) | 7.63 (208) | – | 9.85 (17) | – |



![Refer to caption](total_clip.png)

![Refer to caption](inc_clip.png)

INC (clipped)

![Refer to caption](dec_clip.png)

DEC (clipped)

Figure 13: Cumulative P&L with side-frozen (clipped) strategy.
Top: total portfolio; bottom: INC and DEC contributions.




Table 23: Per-zone attribution of the clipped strategy on the 2022–2025 test set (execution view).

| Zone | Active hours | Avg. |q||q| (MW) | P&L (USD) |
| --- | --- | --- | --- |
| LONGIL | 570 | 118.91 | 5,692,023 |
| NYC | 464 | 21.92 | 910,936 |
| CAPITL | 777 | 10.10 | 303,353 |
| WEST | 807 | 9.89 | 242,054 |
| CENTRL | 235 | 23.66 | 189,883 |
| MILLWD | 184 | 6.23 | 147,420 |
| GENESE | 254 | 10.27 | 115,452 |
| MHKVL | 216 | 10.60 | 90,960 |
| HUDVL | 445 | 5.50 | 57,758 |
| NORTH | 28 | 5.93 | 3,531 |
| DUNWOD | 57 | 4.06 | -1,143 |
| Total | 4,037 | 26.81 (w. avg.) | 7,752,227 |