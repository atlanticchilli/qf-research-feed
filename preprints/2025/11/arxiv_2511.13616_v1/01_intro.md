---
authors:
- Katarzyna Maciejowska
- Arkadiusz Lipiecki
- Bartosz Uniejewski
doc_id: arxiv:2511.13616v1
family_id: arxiv:2511.13616
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Statistical and economic evaluation of forecasts in electricity markets: beyond
  RMSE and MAE'
url_abs: http://arxiv.org/abs/2511.13616v1
url_html: https://arxiv.org/html/2511.13616v1
venue: arXiv q-fin
version: 1
year: 2025
---


Katarzyna Maciejowska
[katarzyna.maciejowska@pwr.edu.pl](mailto:katarzyna.maciejowska@pwr.edu.pl)

Arkadiusz Lipiecki
[arkadiusz.lipiecki@pwr.edu.pl](mailto:arkadiusz.lipiecki@pwr.edu.pl)

Bartosz Uniejewski
[bartosz.uniejewski@pwr.edu.pl](mailto:bartosz.uniejewski@pwr.edu.pl)
Department of Operations Research and Business Intelligence
Department of Computational Social Science
Wrocław University of Science and Technology, Poland

###### Abstract

In recent years, a rapid development of forecasting methods has led to an increase in the accuracy of predictions. In the literature, forecasts are typically evaluated using metrics such as Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE). While appropriate for statistical assessment, these measures do not adequately reflect the economic value of forecasts. This study addresses the decision-making problem faced by a battery energy storage system, which must determine optimal charging and discharging times based on day-ahead electricity price forecasts.
To explore the relationship between forecast accuracy and economic value, we generate a pool of 192 forecasts. These are evaluated using seven statistical metrics that go beyond RMSE and MAE, capturing various characteristics of the predictions and associated errors. We calculate the dynamic correlation between the statistical measures and gained profits to reveal that both RMSE and MAE are only weakly correlated with revenue. In contrast, measures that assess the alignment between predicted and actual daily price curves have a stronger relationship with profitability and are thus more effective for selecting optimal forecasts.

###### keywords:

Battery Energy Storage Systems , Electricity Price Forecasting , Forecast evaluation , Power Market , Trading Strategy

††journal: Energy Conversion and Management

\undefine@key

newfloatplacement\undefine@keynewfloatname\undefine@keynewfloatfileext\undefine@keynewfloatwithin

Glossary

|  |  |
| --- | --- |
| DFL | Decision-Focused Learning |
| ARX | AutoRegressive model with eXogenous variables |
| NARX | Nonlinear AutoRegressive model with eXogenous variables |
| LEAR | LASSO-Estimated AutoRegressive model |
| BESS | Battery Energy Storage Systems |
| RES | Renewable Energy Sources |
| DA | Day-Ahead electricity market |
| VST | Variance Stabilizing Transformations |
| EE | Battery energy capacity (MWh) |
| P​o​wPow | Battery power rating (MW) |
| BB | Length of a charging block (hour) |
| ηc​h\eta^{ch} | Charging efficiency (%) |
| ηd​i​s\eta^{dis} | Discharging efficiency (%) |
| CC | Operating costs (EUR/MWh) |
| RMSE | Root Mean Square Error |
| MAE | Mean Absolute Error |
| Cov-e | Logarithm of a determinant of the covariance matrix of forecast errors |
| Corr-f | Average correlation between the observations and forecasts |
| MHD | Min-Max Hour Deviation |
| MPD | Min-Max Price Deviation |

## 1 Introduction

Forecasting electricity prices is vital for the efficient functioning of modern energy markets. For producers, accurate forecasts support generation planning and trading strategies, while large consumers use them to optimize energy use and reduce costs. Methods range from simple regression and time-series models to advanced approaches such as decision trees and neural networks, often enhanced through combination or reconciliation techniques to improve accuracy and preserve data structure.

Despite this variety, it remains unclear which forecasts deliver the greatest value for decision support. Forecast selection is commonly based on statistical accuracy measures such as Root Mean Square Error (RMSE) or Mean Absolute Error (MAE). Yet, studies show that higher accuracy does not always imply greater economic value (see [Stra:22, zar:can:bha:10, lin:zhu:wid:24, car:kar:19] among others). A key reason is the symmetry of conventional accuracy metrics, which fails to reflect the asymmetric costs of over- versus under-prediction [keb:ara:rah:2011, li:chi:2018, zha:wan:hug:2022, ser:wer:2024].

To bridge this gap, decision-focused learning (DFL) incorporates cost or profit functions directly into estimation [Zha:23, mand:etal:24, car:kar:19]. While value-oriented methods can offer advantages in practical applications, they also present a notable drawback: the resulting point forecasts often lack interpretability. Unlike RMSE- and MAE-based predictions (corresponding to the mean and median, respectively), the minimizer of a cost-oriented loss may not be intuitive [car:kar:19]. Moreover, as noted by [mand:etal:24], some DFL methods yield lower economic value than traditional approaches and require substantially greater computational effort.

In practice, many firms cannot adopt DFL because they rely on third-party forecasts and cannot alter the prediction process. These forecasts also serve multiple departments – generation, trading, risk management – each with distinct objectives and cost structures, making a single cost function unsuitable. Furthermore, predictions are often utilized as inputs to decision-oriented optimization algorithms [zym:sze:21, dre:etal:22]. Instead of calibration, firms often focus on selecting the most useful forecasts based on appropriate evaluation metrics.

As noted by [mur:1993], forecasts can be assessed from three distinct perspectives: consistency (the alignment between forecasters’ judgments and their forecasts), quality (the agreement between forecasts and actual outcomes), and value (the practical benefits gained from using the forecasts). The lack of a monotonic relationship between forecast quality and value can be attributed to the fact that certain forecast characteristics – those that influence decision-making – are often overlooked in conventional evaluation metrics. Forecast verification tends to emphasize statistical accuracy while neglecting other important dimensions, such as association, that may better reflect the forecast’s utility in a real-world context.

This study analyzes the relationship between forecast quality and economic value in energy markets, focusing on the operation of Battery Energy Storage Systems (BESS). BESS enhance grid reliability and energy management by storing surplus renewable generation and discharging when supply is scarce or prices are high. This flexibility stabilizes prices, reduces renewable curtailment, and limits reliance on costly peaking plants. BESS revenues stem from energy arbitrage – optimizing charge and discharge decisions based on predicted price patterns [sha:26] – as well as participation in ancillary service markets, including frequency regulation and voltage support [sch:sta:23].

To capture forecast properties relevant for BESS arbitrage, we construct a pool of 192 hourly day-ahead price forecasts. These include predictions from three common model types: AutoRegressive with eXogenous variables (ARX), its nonlinear variant based on artificial neural networks (NARX), and the regularized LASSO-Estimated AutoRegressive model (LEAR). The pool is further diversified through variations in model specifications, variance-stabilizing transformations, estimator types, and calibration window sizes. Forecast quality is then described by seven measures covering accuracy, error dispersion, association between predicted and actual prices, and the ability to correctly identify daily minimum and maximum hours. Finally, we relate these metrics to the economic value of forecasts, measured by profits from two exemplary BESS systems.

The results provide new insights into the link between quality and value. Traditional accuracy measures are only weakly correlated with BESS profits, echoing [zar:can:bha:10], who showed that such metrics are poor indicators of practical utility. In contrast, dispersion- and association-based measures better capture how closely forecasts follow the shape of the daily price curve and, consequently, how effectively they identify profitable charging and discharging moments. Thus, restricting evaluation to accuracy alone limits the ability to select valuable models, while incorporating alternative metrics improves forecast selection and enhances BESS profitability.

The paper is structured as follows. In Section [2](https://arxiv.org/html/2511.13616v1#S2 "2 Data ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), we present and describe the dataset; in Section [3](https://arxiv.org/html/2511.13616v1#S3 "3 Forecasting electricity prices ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), we explain the forecasting models applied in this study. Then, in Section [4](https://arxiv.org/html/2511.13616v1#S4 "4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), we lay out the methodology for evaluating the forecasts, both in terms of economic values and statistical accuracy. Next, in Section [5](https://arxiv.org/html/2511.13616v1#S5 "5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), we present and discuss the empirical results of our forecasting and trading exercises. Finally, in Section [6](https://arxiv.org/html/2511.13616v1#S6 "6 Conclusions ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), we summarize the main results and provide recommendations for forecasters aiming to capture profits in day-ahead electricity markets.

## 2 Data

![Refer to caption](Figures/dataall.png)


Figure 1: EPEX SPOT hourly day-ahead electricity prices (top), hourly day-ahead system load forecasts (upper middle), renewable generation from solar and wind sources (lower middle), and commodity prices are shown for the period from 2.1.2016 to 31.12.2024. The vertical dashed line marks the end of the 1460-day calibration window for the forecasting models and the beginning of the 2199-day out-of-sample test period.

To examine the link between statistical forecast quality and economic value, we use the German electricity market—one of Europe’s largest and most active—as a case study. Specifically, we assess how day-ahead electricity price forecasts influence the profitability of a battery energy storage system (BESS) engaged in daily arbitrage.

Our dataset combines key drivers of electricity prices and market behavior. The core series is the hourly day-ahead price for the Germany–Luxembourg bidding zone (Austria included until October 2018), sourced from the ENTSO-E transparency platform. To capture supply and demand fundamentals, we add ENTSO-E day-ahead forecasts of system load, solar generation, and aggregated wind generation (onshore and offshore), with solar and wind combined into a single renewable generation series. Broader market influences are represented by commodity futures prices for coal (API2), natural gas (TTF), crude oil (Brent), and EU emission allowances (EUA), obtained from Investing.com. All series cover 2.1.2016–31.12.2024, with a five-year out-of-sample period starting 1.1.2020 (see Figure [1](https://arxiv.org/html/2511.13616v1#S2.F1 "Figure 1 ‣ 2 Data ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE")).

Data were preprocessed for temporal and structural consistency. Variables originally reported at 15-minute resolution (e.g., load and renewables) were aggregated to hourly frequency. Daylight saving time transitions were also adjusted: missing values during the spring shift to CEST were imputed by averaging adjacent hours, while duplicated hours during the autumn return to CET were replaced with their mean.

## 3 Forecasting electricity prices

### 3.1 ARX model

In this research, we use the Autoregressive Model with Exogenous variables (ARX) popular in the EPF literature [zie:wer:18, lag:mar:des:wer:21, mac:uni:wer:23]. Since in the DA market, all prices are set at the same time via a simultaneous auction, the data does not have a typical time-series structure and therefore each hour is modeled separately. Let us denote by Yt,hY\_{t,h} the dependent variable on day tt and at hour hh, which differs across model specifications. We adopt the following structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt,h=Dt​αh+∑p∈{1,2,7}Yt−p,h​ρp,h+Xt(1)​β1,h+Xt,h(2)​β2,h+εt,h,Y\_{t,h}=D\_{t}\alpha\_{h}+\sum\_{p\in\{1,2,7\}}Y\_{t-p,h}\rho\_{p,h}+X^{(1)}\_{t}\beta\_{1,h}+X^{(2)}\_{t,h}\beta\_{2,h}+\varepsilon\_{t,h}, |  | (1) |

where DtD\_{t} is a (1×3)(1\times 3) vector of deterministic variables that includes a constant and dummies for Weekends and Mondays. The variable Yt−p,hY\_{t-p,h} is a lagged endogenous variable at hour hh from pp-days ago, and Xt(1)X^{(1)}\_{t}, Xt,h(2)X^{(2)}\_{t,h} are vectors of exogenous variables. Xt(1)X^{(1)}\_{t} is a (1×9)(1\times 9) vector that summarizes information common to all hourly contracts:

* •

  information on previous day prices: minh⁡(Pt−1,h)\min\_{h}(P\_{t-1,h}), maxh⁡(Pt−1,h)\max\_{h}(P\_{t-1,h}), P¯t−1\bar{P}\_{t-1}
* •

  information on the average forecasted level of RES and Load: R​E​S¯t\bar{RES}\_{t} and L¯t\bar{L}\_{t}
* •

  fuel and C​O2CO\_{2} allowance prices from day t−2t-2: gas (Gt−2G\_{t-2}), oil (O​i​lt−2Oil\_{t-2}), coal (Ct−2C\_{t-2}) and EUA (E​U​At−2EUA\_{t-2}).

The vector Xt,h(2)X^{(2)}\_{t,h} consists of information characteristic for an hour hh. It includes information about the TSO predictions of Load and RES generation from the current and previous day: Lt,hL\_{t,h}, R​E​St,hRES\_{t,h}, Lt−1,hL\_{t-1,h}, R​E​St−1,hRES\_{t-1,h}. The selection of exogenous variables differs slightly from popular ARX model specification ([mac:uni:wer:23]). The set is extended to accommodate recent results of [mar:etal:23], which show the importance of past information on generation structure in the price forecasting process.

#### 3.1.1 Direct model of hourly prices

ARX model is fitted to the hourly electricity prices:

|  |  |  |
| --- | --- | --- |
|  | Pt,h=Dt​αh+∑p∈{1,2,7}Pt−p,h​ρp,h+Xt(1)​β1,h+Xt,h(2)​β2,h+εt,h.P\_{t,h}=D\_{t}\alpha\_{h}+\sum\_{p\in\{1,2,7\}}P\_{t-p,h}\rho\_{p,h}+X^{(1)}\_{t}\beta\_{1,h}+X^{(2)}\_{t,h}\beta\_{2,h}+\varepsilon\_{t,h}. |  |

The model is characterized by 16 parameters: θh=[αh′,ρ1,h,ρ2,h,ρ3,h,β1,h′,β2,h′]′\theta\_{h}=[\alpha\_{h}^{\prime},\rho\_{1,h},\rho\_{2,h},\rho\_{3,h},\beta^{\prime}\_{1,h},\beta^{\prime}\_{2,h}]^{\prime} and is estimated with the Ordinary Least Squares (OLS) method.

#### 3.1.2 Model of deviation from daily mean

In this research, we consider also an alternative ARX-type model that describes separately the average daily price and the deviation of hourly prices from the daily mean.
The approach is divided into two steps: forecasting the daily average (P¯t\bar{P}\_{t}) and predicting the deviation from the mean

|  |  |  |  |
| --- | --- | --- | --- |
|  | P~t,h=Pt,h−P¯t.\tilde{P}\_{t,h}=P\_{t,h}-\bar{P}\_{t}. |  | (2) |

The model for the daily average takes the following form:

|  |  |  |
| --- | --- | --- |
|  | P¯t=Dt​α+∑p∈{1,2,7}P¯t−p​ρp+Xt(1)​β1+X¯t(2)​β2+εt,\bar{P}\_{t}=D\_{t}\alpha+\sum\_{p\in\{1,2,7\}}\bar{P}\_{t-p}\rho\_{p}+X^{(1)}\_{t}\beta\_{1}+\bar{X}^{(2)}\_{t}\beta\_{2}+\varepsilon\_{t}, |  |

where the vector X¯t(2)\bar{X}^{(2)}\_{t} includes the average daily values of the previous day’s generation structure: L¯t−1\bar{L}\_{t-1}, R​E​S¯t−1\bar{RES}\_{t-1}.

The model for deviation from the mean is designed analogously, but with hour resolution

|  |  |  |
| --- | --- | --- |
|  | P~t,h=Dt​αh+∑p∈{1,2,7}P~t−p,h​ρp,h+Xt,h(1)​β1,h+Xt,h(2)​β2,h+εt,h,\tilde{P}\_{t,h}=D\_{t}\alpha\_{h}+\sum\_{p\in\{1,2,7\}}\tilde{P}\_{t-p,h}\rho\_{p,h}+X^{(1)}\_{t,h}\beta\_{1,h}+X^{(2)}\_{t,h}\beta\_{2,h}+\varepsilon\_{t,h}, |  |

where the vector Xt,h(2)X^{(2)}\_{t,h} is the same as in the direct model of hourly prices and includes information on the generation structure from current and previous day: Lt,hL\_{t,h}, R​E​St,h{RES}\_{t,h}, Lt−1,h{L}\_{t-1,h}, R​E​St−1,h{RES}\_{t-1,h}.
The final prediction is computed as the sum of forecasts of both components.

### 3.2 NARX

The relationship between the lagged prices, exogenous variables, and the future price does not need to be linear. To forecast the prices without an explicit assumption about the transformation between the regressors and the target, we resort to artificial neural networks. To ensure that the results of our study are relatable to popular forecasting practices, we employ a shallow network consisting of a single hidden layer of 5 neurons with hyperbolic tangent activation functions, an architecture used in many previous EPF studies [mar:uni:wer:19:narx, hub:mar:wer:19, mar:uni:wer:20]. The model is trained using a Levenberg-Marquardt algorithm [hag:men:94] with a random 10% of the training window held out for early stopping. To reduce the uncertainty related to parameter estimation, the results presented in the paper correspond to the committee machine approach [mar:uni:wer:19:narx], in which a final prediction is an ensemble average of predictions obtained from ten independently trained neural networks. The regressors, calibration window lengths, and applied variance stabilizing transformations are the same as in the case of ARX models.

### 3.3 LEAR model

The next model considered is the LASSO-Estimated AutoRegressive (LEAR) model. It employs the Least Absolute Shrinkage and Selection Operator (LASSO) introduced by Tibshirani [tib:96] to automatically select the most relevant predictors for forecasting Yd,hY\_{d,h}. While numerous regularization techniques have been proposed in the literature, Uniejewski [uni:24:ORD] identified LASSO as a particularly parsimonious, robust, and high-performing method in a comprehensive evaluation of electricity price forecasting (EPF) models.

The LEAR model (both direct and for modeling the deviation from the mean) is designed to capture extensive cross-hour dependencies, enhancing its ability to represent the temporal structure of electricity prices. In contrast to the ARX model defined in Eq. ([1](https://arxiv.org/html/2511.13616v1#S3.E1 "In 3.1 ARX model ‣ 3 Forecasting electricity prices ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE")), which includes only three autoregressive terms, the LEAR specification expands this component to include past prices from all 24 hours of the previous day, two days prior, and one week prior—replacing three regressors with a total of 72.

A similar expansion is applied to the exogenous input vector Xt,h(2)X^{(2)}\_{t,h}. Instead of four regressors (two each for load and RES day-ahead forecasts), the LEAR model incorporates 96 predictors, capturing values for every hour of both the forecasted day and the previous day. This comprehensive treatment of temporal dependencies makes the LEAR model well-suited for capturing the complex dynamics of electricity price formation. Lastly, the model is expanded to include all seven dummy variables, one for each day of the week.

### 3.4 Model specifications and forecast averaging

To develop our forecasting methodology, we begin with three core model structures: ARX, NARX, and LEAR. Each model is estimated across multiple variants to account for different modeling assumptions and data transformations. These variants differ in the choice of the dependent variable, the level of parameter estimation (either pooled across all hours or separate for each hour, already describe above), the size of the calibration window, and the application of a variance stabilizing transformation. The specific choices and their implementation are described in detail in the following sections.

#### 3.4.1 Size of a calibration window

We consider seven estimation window sizes: three long windows (one, two, and four years), a medium window of 182 days, and three short windows of six, twelve, and sixteen weeks. As shown by [mar:ser:wer:18], no single calibration window is universally optimal in electricity markets. Long windows reduce estimator variance and, under stationarity, improve precision. However, structural changes (e.g., rising RES shares) and exogenous shocks (COVID-19, the war in Ukraine) often break stationarity, while price–fundamental relationships are frequently nonlinear. In such cases, short windows can be advantageous. Prior studies [hub:mar:wer:19, ser:uni:wer:19] further suggest that combining forecasts across different window lengths yields the best accuracy.

#### 3.4.2 VST data transformation

Electricity price spikes are typically driven by unpredictable weather conditions, power outages, or transmission failures [gia:gro:12]. These extreme events can significantly distort electricity price forecasts, as outliers tend to pull model coefficients toward values that fit the spikes, often at the expense of forecast accuracy during normal periods. Variance stabilizing transformations (VSTs) aim to reduce the overall variability in the data [cia:mun:zar:22], and less variable—or less spiky—input data generally enable forecasting models to produce more accurate predictions [jan:tru:wer:wol:13].

Following the approach of [uni:wer:zie:18], the electricity price and load time series are first standardized by subtracting the sample median aa and dividing by the sample median absolute deviation bb. The area hyperbolic sine (asinh) transformation is then applied to the standardized data. After forecasting in the transformed space, the inverse transformation and standardization are applied to obtain the final electricity price forecasts.

#### 3.4.3 Heterogeneous vs. pooled estimator

In this research, two types of estimators are considered. Firstly, each hour is modeled and predicted individually, so estimators of θh\theta\_{h} and θ~h\tilde{\theta}\_{h} change throughout the day. In the remaining part of the article, it is called a heterogeneous estimator as it is able to accommodate differences in price behavior across hours. Next, a pooled estimator is used that assumes that the response of prices to explanatory variables is constant during a day, so θ=θ1=…=θ24\theta=\theta\_{1}=\ldots=\theta\_{24}. The vector of parameters is estimated using market information from all 24 hours at once. It is particularly suitable for short estimation windows as it provides more data to the calibration algorithm.

Note that the LEAR model, which incorporates observations for all 24 hours of the day, uses the same set of input variables regardless of the hour being forecasted. As a result, the pooled estimation approach must be supplemented with additional variables that capture hour-specific dynamics. Compared to the heterogeneous estimation (which estimates separate models for each hour), the pooled model is augmented with seven additional regressors: electricity prices lagged by 24, 48, and 168 hours, and load and RES forecasts lagged by 0 and 24 hours.

#### 3.4.4 Forecast averaging

Forecast averaging is a very powerful post-processing method that improves the accuracy of predictions [arm:01, tim:06, ati:2020]. In the energy price forecasting literature, many different approaches have been discussed. In [mac:now:wer:16, lip:etal:2024] authors combine predictions obtained with different models, in [ser:uni:wer:19] and [hub:mar:wer:19] a single model is used and fitted to calibration windows of different sizes. Finally, [mar:etal:23] computes the average across outcomes of different realizations of neural networks. Here, we adopt the second approach and include in the pool of predictions averages of forecasts over different sizes of estimation windows.

#### 3.4.5 Summary

For each hour in the evaluation period, we prepare a pool of predictions that come from different models, model specifications, and forecast averaging. There are three models (ARX, NARX, LEAR) and eight model specifications that differ in terms of the dependent variable (models of hourly prices, Pt,hP\_{t,h}, or deviation from the daily mean, P~t,h\tilde{P}\_{t,h}), VST transformation, and type of estimator (heterogeneous, pooled). Finally, parameters of each model are estimated with data belonging to windows of different lengths: 56, 84, 112, 182, 365, 730, and 1460 days.

In this research, we consider four different pools of predictions. The first one is based on the results of ARX models and consists of 56 individual predictions and 8 forecast averages. Hence, it is built up from 64 different predictions. Analogously, pools based on NARX and LEAR models are constructed.
Finally, a large pool that consists of predictions obtained with all analyzed models, model specifications and corresponding forecast averages is analyzed. It consists of 192 forecasts and captures the diversity stemming from both, the type of a model and its specification.

## 4 Forecast evaluation

According to [mur:1993], there are three distinct types of forecast goodness: consistency (Correspondence between forecasters’ judgments and forecasts), quality (Correspondence between the forecasts and observations), and value (benefits from using the forecasts). The goal of this research is to evaluate the link between the quality and the value of electricity price point forecasts. The study is based on the analysis of the economic performance of a Battery Storage System (BESS).

### 4.1 Economic value of forecasts

In order to assess the economic value of predictions, we analyze the performance of a BESS system that places orders in the DA market.
Similar to [lin:zhu:wid:24], we assume that the BESS system is based on the grid-scale Lithium-ion batteries. The specification of an exemplary BESS is summarized by Table [1](https://arxiv.org/html/2511.13616v1#S4.T1 "Table 1 ‣ 4.1 Economic value of forecasts ‣ 4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE") that shows parameter values for two hypothetical systems: BESS-a and BESS-b. Both batteries are assumed to have the same energy capacity of 3 MWh. They differ in terms of the power ratings that are 3 MW and 1 MW, for BESS-a and BESS-b respectively. It influences the charging and discharging speed of BESS. The first system needs one hour, whereas the second one requires three hours to fully charge or discharge. The operating costs and battery efficiency are taken after [lin:zhu:wid:24].

Table 1: Specification of BESS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | BESS-a | BESS-b | Unit |
| Energy capacity | EE | 3 | 3 | MWh |
| Power rating | P​o​wPow | 3 | 1 | MW |
| Charging block | BB | 1 | 3 | hour |
| Charging efficiency | ηc​h\eta^{ch} | 98 | 98 | % |
| Discharging efficiency | ηd​i​s\eta^{dis} | 97 | 97 | % |
| Operating costs | CC | 11.63 | 11.63 | EUR/MWh |

It is assumed that BESS earns income from the arbitrage in DA market. It aims at buying energy in periods of low prices and selling at hours of high prices. In order to plan the operation, BESS needs to choose one day ahead when to trade the electricity. In this analysis, it is assumed that the charging or discharging is processed in consecutive hours (blocks of 1-3 hours). The hours are selected using the forecast of DA prices. Let us denote by hc​hh^{ch} and hd​i​sh^{dis} the selected first hour of charging and discharging blocks, respectively. Then the profit earned on the day tt can be calculated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | πtE=ηd​i​s​∑i=0B−1P​o​wi+hd​i​sd​i​s​Pt,i+hd​i​s−1ηc​h​∑i=0B−1P​o​wi+hc​hc​h​Pt,i+hc​h−2​C​E,\pi^{E}\_{t}=\eta^{dis}\sum\_{i=0}^{B-1}{Pow}^{dis}\_{i+h^{dis}}P\_{t,i+h^{dis}}-\frac{1}{\eta^{ch}}\sum\_{i=0}^{B-1}{Pow}^{ch}\_{i+h^{ch}}P\_{t,i+h^{ch}}-2CE, |  | (3) |

where P​o​whc​h{Pow}^{ch}\_{h} and P​o​whd​i​s{Pow}^{dis}\_{h} is power charged and discharged within a particular hour, and BB is the length of a charging block. Notice that due to the BESS specification, following constraints need to be satisfied P​o​whc​h≤P​o​w{Pow}^{ch}\_{h}\leq{Pow}, P​o​whd​i​s≤P​o​w{Pow}^{dis}\_{h}\leq{Pow} and

|  |  |  |
| --- | --- | --- |
|  | ∑i=0B−1P​o​wh+ic​h≤E,∑i=0B−1P​o​wh+id​i​s≤E.\sum\_{i=0}^{B-1}{Pow}^{ch}\_{h+i}\leq E,\quad\sum\_{i=0}^{B-1}{Pow}^{dis}\_{h+i}\leq E. |  |

Finally, it is assumed that the battery runs a full cycle within a day; hence, no extra energy is carried over night to be used the next day. Additionally, since the level of profits depends on the energy capacity of the battery, in the following part of the article, we report a profit per 1 MWh of trade, which is calculated as πt=πtE/E\pi\_{t}=\pi^{E}\_{t}/E.

### 4.2 Quality of forecasts

In the literature, the quality of electricity price forecasts is typically described by metrics that focus on forecast accuracy such as Root Mean Squared Errors (RMSE) or Mean Absolute Errors (MAE). They are based on forecast errors of predictions from individual hours, et,h=Pt,h−P^t,he\_{t,h}=P\_{t,h}-\hat{P}\_{t,h}. In order to obtain a single measure that describes the performance across 24 hours, results are usually combined into daily quantities. Let us denote by et=[et,1,…,et,24]e\_{t}=[e\_{t,1},\dots,e\_{t,24}] a (1×24)(1\times 24) vector of forecast errors on day tt. Then

|  |  |  |
| --- | --- | --- |
|  | RMSE=124​T​∑t=1T‖et‖22,MAE=124​T​∑t=1T‖et‖1\text{RMSE}=\sqrt{\frac{1}{24T}\sum\_{t=1}^{T}||e\_{t}||\_{2}^{2}}\;,\quad\text{MAE}=\frac{1}{24T}\sum\_{t=1}^{T}||e\_{t}||\_{1} |  |

These two traditional accuracy metrics indicate the average discrepancy between predicted and actual values. They are commonly used because they align with widely adopted loss functions in model calibration. For instance, RMSE corresponds to the loss function associated with the Least Squares estimation method, while MAE aligns with the loss function in quantile regression (specifically for estimating the median).

Despite their popularity, accuracy metrics capture only a narrow dimension of forecast performance. Fig. [2](https://arxiv.org/html/2511.13616v1#S4.F2 "Figure 2 ‣ 4.2 Quality of forecasts ‣ 4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE") illustrates this with two day-ahead forecasts that achieve identical values (RMSE=10\text{RMSE}=10, MAE=9\text{MAE}=9) but lead to very different profits: π(1)=24.68\pi^{(1)}=24.68 in the first panel versus π(2)=0.16\pi^{(2)}=0.16 in the second. From a battery owner’s perspective, their economic value is therefore fundamentally different.

![Refer to caption](Figures/example.png)


Figure 2: Examples of DA price forecasts. Setup 1 (left panel): forecasts with low dispersion and high association, leading to π(1)\pi^{(1)} = 24.68 EUR profit. Setup 2 (right panel): forecasts with high dispersion and low association, leading to π(2)\pi^{(2)} = 0.16 EUR profit. Both predictions are characterized by the same RMSE and MAE values.

The forecasts in Fig. [2](https://arxiv.org/html/2511.13616v1#S4.F2 "Figure 2 ‣ 4.2 Quality of forecasts ‣ 4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE") differ markedly. While their errors have similar magnitudes, their variability is not. The left panel tracks the daily pattern of day-ahead (DA) prices more closely than the right, making it more useful for identifying optimal charging and discharging hours. To capture such differences, we introduce three additional classes of metrics: those assessing forecast error variability, the association between forecasts and actual prices, and the ability to correctly identify the daily minimum and maximum price hours.

#### 4.2.1 Dispersion measures

Dispersion measures show how diversified the forecast errors are within a day. If all errors share the same sign, as illustrated in Fig. [2](https://arxiv.org/html/2511.13616v1#S4.F2 "Figure 2 ‣ 4.2 Quality of forecasts ‣ 4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), the predictions might not be precise, yet they are closely related to actual values. At an extreme, when errors are uniform, predictions can be simply viewed as shifted true observations. Although not accurate, such forecasts may be highly beneficial in determining the optimal time for charging and discharging BESS.

In this research, we measure the dispersion using the variance-covariance matrix of forecast errors. It is calculated as

|  |  |  |
| --- | --- | --- |
|  | Cov-e=log⁡d​e​t​Σ^,\text{Cov-e}=\log{det\hat{\Sigma}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | Σ^=1T​∑t=1Tet′​et.\hat{\Sigma}=\frac{1}{T}\sum\_{t=1}^{T}e^{\prime}\_{t}e\_{t}. |  |

Notice that if the predictions P^t,h\hat{P}\_{t,h} are unbiased and forecast errors have zero expected value, then Σ^\hat{\Sigma} is a consistent estimator of the errors’ variance-covariance matrix. Moreover, Cov-e decreases as forecast errors decline and as the correlation between errors increases. Thus, it reflects not only the dispersion but also, to some extent, the overall forecast accuracy.

#### 4.2.2 Association measure

According to [mur:1993], the association is the relationship between individual pairs of forecasts and observations. For instance, the daily price curve in left panel in Fig. [2](https://arxiv.org/html/2511.13616v1#S4.F2 "Figure 2 ‣ 4.2 Quality of forecasts ‣ 4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE") more closely mirrors the actual price fluctuation pattern compared to the curve shown in right panel in Fig. [2](https://arxiv.org/html/2511.13616v1#S4.F2 "Figure 2 ‣ 4.2 Quality of forecasts ‣ 4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE").
In this analysis, it is measured as the average correlation between actual and predicted electricity prices. It is computed as follows

|  |  |  |
| --- | --- | --- |
|  | Corr-f=1T​∑t=1Tρ​(Pt,P^t),\text{Corr-f}=\frac{1}{T}\sum\_{t=1}^{T}\rho(P\_{t},\hat{P}\_{t}), |  |

where PtP\_{t} and P^t\hat{P}\_{t} are (1×24)(1\times 24) vectors of electricity prices and their forecasts on day tt and ρ(.)\rho(.) is the Spearman correlation coefficient.

#### 4.2.3 Selection of an hour of the minimum and maximum price

The final two measures capture forecast properties directly relevant for BESS operation: the correct identification of daily minimum and maximum price hours using point forecasts P^t\hat{P}\_{t}. Let h^t(m​i​n)\hat{h}\_{t}^{(min)} and h^t(m​a​x)\hat{h}\_{t}^{(max)} denote the forecasted hours of the lowest and highest prices on day tt, and ht(m​i​n)h\_{t}^{(min)}, ht(m​a​x)h\_{t}^{(max)} their actual counterparts from observed prices PtP\_{t}.
The first measure, the Min-Max Hour Deviation (MHD), computes the average absolute difference between forecasted and actual hours:

|  |  |  |
| --- | --- | --- |
|  | MHD=1T​∑t=1T|ht(m​i​n)−h^t(m​i​n)|+|ht(m​a​x)−h^t(m​a​x)|.\text{MHD}=\frac{1}{T}\sum\_{t=1}^{T}|h\_{t}^{(min)}-\hat{h}\_{t}^{(min)}|+|h\_{t}^{(max)}-\hat{h}\_{t}^{(max)}|. |  |

From the perspective of BESS, the incorrect selection of the moment of charging or discharging has a significant impact on income only when there are substantial differences of prices in actual and the predicted hours. Therefore, we propose a second measure, based on the difference between the real maximum/minimum of price and the maximum/minimum indicated by forecasts called Min-Max Price Deviation (MPD):

|  |  |  |
| --- | --- | --- |
|  | MPD=1T​∑t=1T|Pt,ht(m​i​n)−Pt,h^​t(m​i​n)|+|Pt,ht(m​a​x)−Pt,h^t(m​a​x)|.\text{MPD}=\frac{1}{T}\sum\_{t=1}^{T}|P\_{t,h\_{t}^{(min)}}-P\_{t,\hat{h}t^{(min)}}|+|P\_{t,h\_{t}^{(max)}}-P\_{t,\hat{h}\_{t}^{(max)}}|. |  |

Since Pt,ht(m​a​x)≥Pt,ht(m​i​n)P\_{t,h\_{t}^{(max)}}\geq P\_{t,h\_{t}^{(min)}} and Pt,ht(m​i​n)≤Pt,ht(m​a​x)P\_{t,h\_{t}^{(min)}}\leq P\_{t,h\_{t}^{(max)}}, MPD can be interpreted as the average deviation in daily price spreads. It is closely related to profit loss from misidentifying charging and discharging hours, though not identical. MPD ignores storage inefficiencies and does not capture the broader dependence of profits on multiple hours for systems with a C-rating E/P​o​w<1E/Pow<1. Thus, while strongly correlated with income, MPD does not measure profit loss directly.

A related concept was introduced by [ama:etal:2023], who proposed d-RMSE, based on the difference between actual peak demand and demand at the predicted peak hour. Unlike d-RMSE, MPD uses absolute errors instead of squared errors, directly reflecting lost profits from misidentifying daily extrema, and jointly evaluates both peak and trough values.

In Fig. [2](https://arxiv.org/html/2511.13616v1#S4.F2 "Figure 2 ‣ 4.2 Quality of forecasts ‣ 4 Forecast evaluation ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), red and green bars indicate the charging and discharging hours, respectively. To assess the accuracy of hour selection, full bars represent hours chosen using actual prices, while empty bars correspond to those selected based on forecasts. The height of the bars indicates the actual price at the selected hour. It is evident that neither forecast perfectly identifies the optimal charging and discharging times. When examining the deviation from the optimal hours, the first set of predictions shows greater discrepancies: MHD(1)=6.5\text{MHD}^{(1)}=6.5 whereas MHD(2)=1.5\text{MHD}^{(2)}=1.5. Since the profit depends on the level of prices more than on the time of trade, we calculate also the second measure: MPD(1)=0.91\text{MPD}^{(1)}=0.91 and MPD(2)=13.50\text{MPD}^{(2)}=13.50 for the first and second panels, respectively. The results indicate that the second approach aligns more closely with actual profits, making it a more appropriate choice for forecast evaluation.

## 5 Empirical results

### 5.1 Profits

Let us first analyze the level of profits across the years. The BESS income depends on the price spread within a day and the ability to select the charging and discharging hours, which in turn builds upon the quality of forecasts. In order to disentangle these two features, we calculate first the profits of a BESS under the assumption of known future prices. The outcomes are called Oracle and are presented in the first column of Table [2](https://arxiv.org/html/2511.13616v1#S5.T2 "Table 2 ‣ 5.1 Profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"). Next, we consider the income of a storage utility that uses imperfect forecasts from the pool in its decision process. Table [2](https://arxiv.org/html/2511.13616v1#S5.T2 "Table 2 ‣ 5.1 Profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE") presents descriptive statistics of profits per 1 MWh of traded electricity.

Table 2: Average daily profit per 1 MWh of traded electricity: descriptive statistics

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Year | Oracle | Max | Min | Mean | Std |
| BESS-a | | | | | |
| 2020 | 6.23 | 4.32 | 0.45 | 3.38 | 0.80 |
| 2021 | 47.43 | 43.57 | 33.63 | 40.62 | 2.16 |
| 2022 | 143.18 | 134.05 | 115.52 | 129.45 | 3.97 |
| 2023 | 65.44 | 60.22 | 52.32 | 58.31 | 1.80 |
| 2024 | 109.05 | 102.57 | 83.38 | 94.37 | 3.81 |
| BESS-b | | | | | |
| 2020 | 1.70 | 0.67 | -1.73 | 0.24 | 0.36 |
| 2021 | 38.38 | 35.97 | 31.59 | 34.40 | 1.07 |
| 2022 | 122.98 | 117.25 | 107.89 | 114.91 | 2.12 |
| 2023 | 52.91 | 50.29 | 45.25 | 48.81 | 1.03 |
| 2024 | 86.33 | 81.00 | 71.74 | 77.56 | 1.58 |

For both systems, BESS-a and BESS-b, the findings indicate a strong correlation between profit levels and general electricity prices. In 2020, with relatively low prices, storage utilities found it difficult to generate any profit. In a case of known prices, BESS-a achieved 6.23 EUR/MWh, whereas BESS-b managed only 1.70 EUR/MWh. The average income level is even lower when the imperfect forecasts are used. In such a case, the average earnings decreased to 3.38 EUR/MWh and 0.24 EUR/MWh, respectively. On the contrary, in 2022 when the electricity prices reached their peak, the Oracle profits jumped to 143.18 EUR/MWh for the BESS-a system.

Furthermore, when evaluating both types of systems, it’s apparent that BESS-a generates greater profits compared to BESS-b. When the battery can be charged or discharged within one hour, it allows for achieving a lower buy- and higher sell price. Hence, the profits of Oracle and the average income of the pool decrease together with the battery power rating.

Finally, one could observe significant discrepancies between the highest and the lowest profits in the pool. In year 2020, the most profitable forecasts brought income higher by 3.87 EUR/MWh than the worst ones. In the following years, this gap for BESS-a widened, reaching 18.53 EUR/MWh and 19.19 EUR/MWh in 2022 and 2024, respectively. In these two years, the additional earnings represented between 16-23% of the minimum income. The outcomes for BESS-b exhibit the same pattern, highlighting the critical role of accurate forecast selection in the BESS decision-making.

### 5.2 Forecast evaluation and its relationship to profits

As demonstrated earlier, the selection of predictions used in the decision-making process significantly influences the profitability of BESS. This choice can be based on traditional accuracy metrics, such as RMSE and MAE, or other measures associated with the behavior of forecast errors (Cov-e) or the association between the predictions and true values (Corr-f). In this section, the relationship between measures of forecast quality and battery profits is evaluated. It can be noticed that using individual predictions, we can calculate both the income level and a measure value. Hence, there are 192 (for a big pool) or 64 (for model-based pools) pairs of values that describe the outcomes. Using this information, we calculate the Spearman correlation, which is robust to outliers and any monotonic transformation of data.

In Table [3](https://arxiv.org/html/2511.13616v1#S5.T3 "Table 3 ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), correlation coefficients between forecast quality measures and the average level of profits calculated for the whole evaluation period are presented. The first block of outcomes shows the results for BESS-a, whereas the second block represents BESS-b. The results are displayed for three sub-pools and for a big pool separately. The findings indicate that all correlations, apart from Corr-f, are negative. This implies that an increase in, for instance, Cov-e, is associated with a reduction in profits. Unlike other metrics, Corr-f is interpreted positively, meaning that a higher value of this measure corresponds to a greater income.

Table 3: The absolute value of an average Spearman correlation coefficient between profits and forecast quality measures; rolling window of 365 days

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Measure | ARX | NARX | LEAR | All |
|  | BESS-a | | | |
| RMSE | -0.401 | -0.277 | -0.060 | -0.169 |
| MAE | -0.378 | -0.377 | -0.002 | -0.172 |
| Cov-e | -0.728 | -0.861 | -0.739 | -0.780 |
| Corr-f | 0.896 | 0.843 | 0.865 | 0.802 |
| MHD | -0.820 | -0.791 | 0.794 | -0.755 |
| MPD | -0.969 | -0.965 | -0.962 | -0.964 |
|  | BESS-b | | | |
| RMSE | -0.473 | -0.344 | -0.192 | -0.347 |
| MAE | -0.453 | -0.446 | -0.138 | -0.372 |
| Cov-e | -0.712 | -0.756 | -0.671 | -0.641 |
| Corr-f | 0.903 | 0.861 | 0.909 | 0.886 |
| MHD | -0.836 | 0.786 | -0.841 | -0.835 |
| MPD | -0.927 | -0.851 | -0.915 | -0.897 |

Because the sign of the correlation coefficient varies across measures, we refer to its absolute value when comparing the strength of correlations in the following sections of the article.

Let us first analyze the results for BESS-a system and the big pool of forecasts. It becomes evident that widely used accuracy metrics, such as RMSE and MAE, show weak correlation with profits, with the absolute correlation coefficient being less, in absolute terms, than 0.20. At the same time, correlation with dispersion and association measures approaches 0.80. This highlights a substantial difference between these evaluation methods. The performance of Corr-f measure, which shows how well the forecasts reflect the within-day fluctuations of electricity prices, is worth emphasizing. The value of the correlation between Corr-f and average profits reaches 0.802.

When examining small model-based pools, becomes evident that while the overall correlation pattern is similar across pools, the strength of the correlation varies. The highest correlation is observed for the ARX and NARX models, which, notably, generate the most diverse set of predictions. For NARX, the correlation coefficient ranges from 0.27 to 0.97. In contrast, the weakest association is found with the LEAR models, where the correlation between RMSE or MAE and profits is nearly zero.

The results for BESS-b closely resemble those of BESS-a. Traditional accuracy metrics, such as RMSE and MAE, show only a weak correlation with profits; however, this relationship is slightly stronger compared to BESS-a. The overall outcomes suggest that the decision-making process in BESS-b is more complex than in BESS-a case. As a result, the financial performance of BESS-b is more dependent on accurately capturing the shape of the daily price curve – an aspect measured by Corr-f.

Finally, we examine the correlation between profits and two specialized measures designed to assess the accuracy of selecting the minimum and maximum price hours within a day: MHD and MPD.
The MHD metric penalizes deviations from the optimal charging and discharging hours. While it ranks among the better-performing indicators, its correlation with profits is weaker than that of Corr-f and comparable to Cov-e. In contrast, MPD demonstrates a significantly stronger relationship with profits, showing an average correlation of 0.96 for BESS-a and 0.90 for BESS-b. Unlike MHD, which measures time-based discrepancies, MPD assesses the difference of electricity prices between the selected and optimal hours. Given that profits are directly tied to price differences – and that the daily price curve often exhibits a ”duck” shape – MPD proves to be a more effective performance metric than MHD.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 3: Scatter plots of average daily profits for the BESS-a energy storage calculated for the entire testing set with respect to different error measures.

A more detailed illustration of the relationship between forecast quality measures and profitability is presented in Fig. [3](https://arxiv.org/html/2511.13616v1#S5.F3 "Figure 3 ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"). The figure depicts scatter plots of average daily income per 1 MWh of trade (π\pi) against various forecast evaluation metrics for the BESS-a energy storage system. In these plots, colors denote different models (blue - ARX, red - NARX, green - LEAR), shapes indicate the estimator type and model specification, and marker size reflects the length of the calibration window. Finally, a cross indicates the average of forecasts across different estimation windows.

The results confirm earlier findings of a weak correlation between RMSE/MAE and profits (top row, Fig. [3](https://arxiv.org/html/2511.13616v1#S5.F3 "Figure 3 ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE")). The scatter plots form diffuse clouds with no clear monotonic relationship, with one noticeable feature: a cluster of red points corresponding to NARX models. These results indicate that NARX provides the most accurate forecasts; however, its associated income is comparable to – or in some cases lower than – that of alternative models.

In contrast, the Cov-e and Corr-f measures (middle row, Fig. [3](https://arxiv.org/html/2511.13616v1#S5.F3 "Figure 3 ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE")) demonstrate a substantially stronger and nearly linear relationship with income. For the Corr-f metric in particular, outcomes cluster distinctly by model, with LEAR consistently yielding the highest profits.

Finally, when comparing model specifications, the pooled estimator consistently outperforms the heterogeneous estimator, generating forecasts that achieve both high predictive accuracy and strong profitability.

#### 5.2.1 Time evolution of correlation

To account for changes in correlation over time, a rolling window method is applied. The process begins by selecting the initial 365 days in the evaluation window. Within this set, the average profit is computed along with six different forecast quality metrics and their corresponding correlation coefficients. Next, the window is shifted by one day, and the whole procedure is repeated.
The time evolution of the resulting correlation coefficients is illustrated in Fig. [4](https://arxiv.org/html/2511.13616v1#S5.F4 "Figure 4 ‣ 5.2.1 Time evolution of correlation ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE") for BESS-a (upper panel) and BESS-b (lower panel), respectively. For visualization purposes, the coefficients of all metrics except Corr-f are multiplied by –1.

BESS-a

![Refer to caption](x7.png)

BESS-b

![Refer to caption](x8.png)

Figure 4: Spearman correlation between forecast quality measures and profits for the BESS-a (top panel) and BESS-b (bottom panel) energy storage. The grey line marks the average daily price of electricity.

The results reveal a clear downward trend in the correlation between RMSE or MAE and profits. Not only is the relationship between these traditional accuracy measures and income the weakest overall, but it also deteriorates over time. At the start of the evaluation period, which includes data from 2020, the correlation between MAE and profit oscillated around -0.45. By 2021, it drops for BESS-a to around -0.06, and in the final two years, it fluctuates between -0.24 and 0.12. RMSE exhibits a similar trend, with a noticeable decline in correlation over the years. This progression supports earlier conclusions that RMSE and MAE are poor indicators of profitability.

When examining the performance of a measure that captures error dispersion, several similar patterns emerge. The correlation between profits and Cov-e declined in absolute terms as electricity prices began to rise in 2021. Subsequently, these correlations recovered, even slightly surpassing their initial levels. For the BESS-a specification, the strength of correlation remained relatively strong, whereas for the BESS-b specification, it fluctuates and declines slightly over time.

In contrast to the accuracy and dispersion measures, the performance of the association measure remains stable over most of the evaluation period, oscillating around the average value reported in Table [3](https://arxiv.org/html/2511.13616v1#S5.T3 "Table 3 ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"). Only from 2023H2 the correlation between Corr-f and profits starts to fall below 0.75. On the plot it is visible as a drop in rolling correlation in 2024H2. This weakening is particularly pronounced for BESS-a, where the coefficient declines to 0.26 by the end of the sample, while for BESS-b it remains consistently above 0.62.

Finally, let us consider the results for MHD and MPD, which confirm earlier findings of the inferior performance of the hour-based metric. The correlation between MHD and profits consistently remains lower than that of MPD. Notably, there is a sharp decline in MHD performance toward the end of the sample period – dropping from 0.75 to 0.1 within a single year for BESS-a. This decline is associated with the changing shape of daily price curves. As more and more solar energy enters the system, the midday reduction of electricity prices becomes more pronounced, resulting in not just two peaks (morning and evening), but also two low-price periods (night and midday). Consequently, the lowest and highest prices are not clustered closely to each other. For example, if the actual minimum price occurs at night and the forecasted minimum is during midday, despite similar price levels, the time-based error is heavily penalized. Thus, evaluating performance based on price differences rather than hours proves to be a more robust method. The absolute value of the correlation between MPD and profits remains above 0.76 throughout the evaluation period for both BESS-a and BESS-b, and for BESS-a, it consistently exceeds 0.90.

A comparison of the upper and the lower panel in Fig. [4](https://arxiv.org/html/2511.13616v1#S5.F4 "Figure 4 ‣ 5.2.1 Time evolution of correlation ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE") reveals that both battery systems exhibit a similar overall pattern in correlation coefficients. However, some subtle differences can be observed. For BESS-b, the correlation coefficients related to dispersion and association measures tend to be more stable compared to BESS-a. Additionally, the performance of Corr-f improves in BESS-b, approaching the level of MPD, unlike in the first system. Lastly, as indicated in Table [3](https://arxiv.org/html/2511.13616v1#S5.T3 "Table 3 ‣ 5.2 Forecast evaluation and its relationship to profits ‣ 5 Empirical results ‣ Statistical and economic evaluation of forecasts in electricity markets: beyond RMSE and MAE"), while traditional accuracy measures still show the weakest correlation with profits, their relationship is slightly stronger in BESS-b than in BESS-a.

## 6 Conclusions

Managing battery storage systems requires active participation in electricity markets. The most important of these is the DA market, where bids are submitted around noon on the day prior to delivery. Consequently, BESS must make charging and discharging decisions without knowing the exact market prices in advance. In this study, we consider two hypothetical BESS configurations that have the same energy capacity but differ in power ratings. This difference significantly affects financial outcomes, as a battery with a lower power rating requires more time to fully charge or discharge, potentially forcing it to operate during less favorable price periods. Since trading decisions are made one day ahead, they must rely on price forecasts.

In this article, we construct a pool of 192 forecasts based on three widely used model types: ARX, LEAR, and NARX, which together encompass a broad family of linear and nonlinear approaches. Additionally, we consider eight different model specifications that vary according to the choice of the endogenous variable, the use of variance-stabilizing transformations, and the type of estimator (heterogeneous vs. pooled). Model parameters are estimated using rolling windows of seven different lengths. The pool is further enriched with ensemble forecasts, which average predictions across different window sizes.

The primary goal of this research is to analyze and evaluate the relationship between various measures of forecast quality and the resulting economic profit. We extend the analysis beyond traditional accuracy metrics such as RMSE and MAE, incorporating a dispersion measure (Cov-e) and an association measure (Corr-f). The dispersion measure, Cov-e, captures the variability of forecast errors throughout the day – lower dispersion indicates more consistent forecasts, which simplifies the selection of optimal charging and discharging hours. The association is assessed via the intra-day correlation between forecasted and actual prices (Corr-f). A high correlation implies that the forecast closely replicates the shape of the actual price curve, allowing the BESS to identify more accurately when to buy and sell electricity. Finally, we include two additional measures directly related to the identification of the daily minimum and maximum price hours: MHD and MPD. The first quantifies the temporal distance between predicted and actual peak/trough hours, while the second evaluates the accuracy of hour selection based on the difference in Corresponding prices.

The results of the experiment indicate that

* •

  The choice of forecasting model has a substantial influence on BESS profitability. Selecting the best-performing model can increase profits by 10–30% during 2021–2024 compared with the poorest-performing model.
* •

  The weak correlations between MAE and RMSE and profits, spanning –0.002 to –0.473, indicate that these metrics are insufficient for reliably differentiating forecast performance.
* •

  The correlation between dispersion measure, Cov-e, and profits ranges from -0.641 to -0.861, substantially outperforming traditional accuracy metrics.
* •

  The association metric, Corr-f, shows a strong correlation with profits, exceeding 0.8 in all considered pools.
* •

  Among the two measures designed to assess the accuracy of identifying hours of minimum and maximum prices, MPD exhibits a stronger correlation with profits than MHD.

The performance of the proposed evaluation metrics demonstrates that forecast properties beyond traditional accuracy significantly impact profit generation. Certain measures, such as Cov-e and Corr-f, are smooth and differentiable, making them suitable candidates for inclusion in loss functions to enhance the estimation process. Others, like MPD, can enrich model evaluation, especially when assessing newly developed forecasting methods. These findings contribute to the ongoing discussion on forecast evaluation by emphasizing the necessity of linking the quality and economic value of predictions, particularly within electricity markets.

## CRediT authorship contribution statement

Katarzyna Maciejowska: Conceptualization, Formal analysis, Methodology, Software, Investigation, Funding acquisition, Supervision, Validation, Writing – original draft
Arkadiusz Lipiecki: Formal analysis, Methodology, Software, Investigation, Visualization, Writing – original draft
Bartosz Uniejewski: Formal analysis, Methodology, Software, Investigation, Funding acquisition, Supervision, Validation, Writing – original draft

## Declaration of competing interests

The authors declare no competing interests.

## Acknowledgements

The study was partially supported by the National Science Center (NCN, Poland) through grant no. 2018/30/A/HS4/00444 (to AL), grant no. 2023/49/N/HS4/02741 (to BU) and grant no. 2019/34/E/HS4/00060 (to KM).