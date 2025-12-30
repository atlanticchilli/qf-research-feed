---
authors:
- Julia Kończal
- Michał Balcerek
- Krzysztof Burnecki
doc_id: arxiv:2512.22660v1
family_id: arxiv:2512.22660
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Machine learning models for predicting catastrophe bond coupons using climate
  data
url_abs: http://arxiv.org/abs/2512.22660v1
url_html: https://arxiv.org/html/2512.22660v1
venue: arXiv q-fin
version: 1
year: 2025
---


Julia Kończal

Michał Balcerek

Krzysztof Burnecki
Faculty of Pure and Applied Mathematics, Hugo Steinhaus Center,Wrocław University of Science and Technology,Wyb.
Wyspiańskiego 27,
50-370,
Wrocław,
Poland

###### Abstract

In recent years, the growing frequency and severity of natural disasters have increased the need for effective tools to manage catastrophe risk. Catastrophe (CAT) bonds allow the transfer of part of this risk to investors, offering an alternative to traditional reinsurance. This paper examines the role of climate variability in CAT bond pricing and evaluates the predictive performance of various machine learning models in forecasting CAT bond coupons. We combine features typically used in the literature with a new set of climate indicators, including Oceanic Niño Index, Arctic Oscillation, North Atlantic Oscillation, Outgoing Longwave Radiation, Pacific–North American pattern, Pacific Decadal Oscillation, Southern Oscillation Index, and sea surface temperatures. We compare the performance of linear regression with several machine learning algorithms, such as random forest, gradient boosting, extremely randomized trees, and extreme gradient boosting. Our results show that including climate-related variables improves predictive accuracy across all models, with extremely randomized trees achieving the lowest root mean squared error (RMSE). These findings suggest that large-scale climate variability has a measurable influence on CAT bond pricing and that machine learning methods can effectively capture these complex relationships.

###### keywords:

CAT bond , Climate indicators , Machine learning , Linear regression , Natural catastrophes , Forecasting

## 1 Introduction

In recent years, natural disasters have become more frequent and severe around the world, leading to significant economic losses and growing financial risks. As a result, markets have started to pay greater attention to instruments that help transfer and mitigate catastrophe-related risk. One important example is catastrophe (CAT) bonds, which allow insurers to shift part of the potential losses from extreme weather events to investors. These bonds serve as an alternative to traditional reinsurance.

A CAT bond is typically issued by an insurer or reinsurer through a special purpose vehicle (SPV) [braun2016pricing]. Investors who purchase the bond receive attractive coupon payments as long as no predefined catastrophic event (e.g., hurricane, earthquake, flood) occurs during the lifetime of the bond. However, if such an event takes place, part or all of the principal is used to cover the issuer’s losses, and investors can lose the corresponding portion of their investment. This mechanism aligns the interests of insurers seeking protection against extreme risks with investors willing to take on higher risk in exchange for higher potential returns.

Given the frequency and severity of climate-related catastrophes, accurate pricing of CAT bond coupons has become a critical challenge. Machine learning methods, which can capture nonlinear dependencies and extract patterns from large, multidimensional datasets, offer a promising alternative for pricing CAT bonds in a way that reflects evolving climate risks.

There is a vast literature on CAT bond pricing techniques. Early empirical research showed that expected loss is the main determinant of spreads at issuance, while factors such as covered territory, the identity of the sponsor, the reinsurance cycle, and corporate bond spreads also play important roles [braun2016pricing]. More recent work demonstrated that issuer effects strongly influence both CAT bond pricing and volatility, with implications for how different bond features behave across market phases and over time [chatoro2023catastrophe]. Evidence on global warming and its implications for natural catastrophe risk further suggests that climate dynamics may contribute to a systematic undervaluation of climate-related risks in CAT bond markets [morana2019climate].

Another strand of the literature has focused on modeling catastrophe losses and developing approximations for tail probabilities to improve pricing methodologies. Weak approximations for heavy-tailed loss processes have been proposed and applied to index-linked CAT bond models [burnecki2017stable]. Subsequent studies introduced pricing frameworks for multi-peril CAT bonds, modeling losses through compound non-homogeneous Poisson processes and fitting Burr, generalized extreme value, and log-normal distributions [burnecki2024pricing]. Related extensions addressed heavy-tailed and left-truncated data, demonstrating advantages of alternative estimation techniques and their relevance for CAT bond pricing [giuricich2019modelling].
Contingent-claim approaches represent another important research direction. Models based on two-dimensional semi-Markov processes with stochastic interest rates have been proposed, yielding closed-form formulas calibrated to PCS data [shao2017pricing]. Similar frameworks assumed that catastrophe losses follow compound non-homogeneous Poisson processes and relied on numerical approximations to obtain CAT bond prices [ma2013pricing].

In recent years, machine learning techniques have gained prominence in CAT bond pricing. Random forest models have been shown to significantly improve forecasts of CAT bond premia in both primary and secondary markets compared to traditional regression approaches [gotze2020improving, gotze2023forecasting, makariou2021random]. Neural networks have also been applied to the design and pricing of earthquake-related CAT bonds, highlighting the broader potential of machine learning approaches for catastrophe-linked securities [louloudis2024earthquake].

Beyond CAT-bond–specific studies, related research in climate finance and catastrophe-linked derivatives offers insights relevant for pricing and risk assessment. Recent evidence shows that climate-change dynamics and natural disasters have measurable, heterogeneous effects on global financial markets, with climatological and biological events generating the strongest stock-market reactions and European markets displaying the highest sensitivity [pagnottoni2022climate]. Furthermore, catastrophe-linked contingent claims have been examined through more flexible derivative-pricing approaches. A discrete-time pricing model for catastrophe equity put options introduces autocorrelated and catastrophe-dependent event intensity alongside Generalized Autoregressive Conditional Heteroskedasticity (GARCH) type stochastic volatility of the underlying asset, yielding an analytical pricing formula and demonstrating an inverted-U relationship between option prices, baseline catastrophe intensity, and the speed at which past events lose influence [wang2019catastrophe].

While previous studies have examined financial, structural, and climate-related determinants of CAT bond spreads, our analysis extends this literature in two key ways. First, we investigate whether large-scale climate variability indices—such as the Oceanic Niño Index (ONI), Arctic Oscillation (AO), North Atlantic Oscillation (NAO), Outgoing Longwave Radiation (OLR), the Pacific–North American (PNA) pattern, Pacific Decadal Oscillation (PDO), and the Southern Oscillation Index (SOI)—help explain CAT bond coupons, thereby enriching the set of climate variables considered in earlier work. Second, we evaluate the predictive performance of a broader range of machine learning models beyond random forest, including Bayesian ridge regression (BR), gradient boosting regression (GB), extremely randomized trees (ETR), automatic relevance determination regression (ARD), light gradient boosting machine (LGBM), and extreme gradient boosting (XGBoost), and compare their performance to traditional approaches. Overall, our study provides new insights into how climate variability may shape pricing in the CAT bond market and assesses the value added by alternative modeling techniques.

This paper is structured as follows. In Section [2](https://arxiv.org/html/2512.22660v1#S2 "2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") we explain the data under investigation, namely CAT bonds from the primary market. Section [3](https://arxiv.org/html/2512.22660v1#S3 "3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") introduces the climate variability variables, including ONI, AO, NAO, PDO, and OLR, as well as sea surface temperatures (SST). We explore the correlations between lagged indices and CAT bond coupons. Section [4](https://arxiv.org/html/2512.22660v1#S4 "4 Linear regression comparison ‣ 3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") is devoted to comparing two models: the one proposed in [braun2016pricing] and our extended model incorporating climate variability variables. We perform both point and interval predictions. In Section [5](https://arxiv.org/html/2512.22660v1#S5 "5 Machine learning approach ‣ 4 Linear regression comparison ‣ 3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data"), we apply seven machine learning models (RF, BR, GB, ETR, ARD, LGBM, and XGBoost) to compare the performance of thebenchmark model and ours. Finally, Section [6](https://arxiv.org/html/2512.22660v1#S6 "6 Conclusions ‣ 5 Machine learning approach ‣ 4 Linear regression comparison ‣ 3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") concludes the paper.

## 2 Data

Our dataset is collected from the primary market and consists of 734 tranches issued between June 1997 and December 2020. In Figure [1](https://arxiv.org/html/2512.22660v1#S2.F1 "Figure 1 ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") we present geographical distribution of bond issuance across countries. As we can see the dataset covers a wide range of geographic regions. It captures both developed and emerging markets. The majority of bonds in the dataset provide coverage against catastrophe risks in the United States. However, we also observe issuances linked to exposures in Europe and Asia.

![Refer to caption](mapa.png)


Figure 1: Geographical distribution of bond issuance across countries. The map presents the number of tranches issued in the primary market between June 1997 and December 2020.

Here, we distinguish three groups of explanatory variables. First, we include CAT bond-related variables obtained directly from market data (e.g., expected loss, peril type, region). Second, we incorporate macroeconomic variables introduced in [braun2016pricing], while also including additional financial market indicators (monthly returns of major equity indices and selected cryptocurrencies). Third, we incorporate a set of climate variability indices.

Table 1: Summary statistics for continuous variables in the dataset. The sample comes from the primary market and contains 734 tranches. All monetary values are expressed in millions of USD.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Mean | Std | Min | Max |
| Attachment point | 2505.3 | 3565.48 | 17.5 | 20670 |
| Attachment probability | 0.039 | 0.039 | 0.00021 | 0.23 |
| BB spread | 0.035 | 0.014 | 0.015 | 0.11 |
| Cedent tenure | 60.99 | 70.93 | 0 | 281 |
| Coverage limit | 3267.14 | 4331.26 | 65 | 25000 |
| Expected loss | 0.025 | 0.025 | 0 | 0.15 |
| Final spread price | 0.077 | 0.051 | 0.0065 | 0.49 |
| No of locations | 1.34 | 0.65 | 1 | 3 |
| No of perils | 2.37 | 1.92 | 1 | 8 |
| ROL index | 220.49 | 40.23 | 151.8 | 293.8 |
| Size | 134.28 | 123.59 | 1.8 | 1500 |
| Term | 36.38 | 12.5 | 1 | 120 |

In Table [1](https://arxiv.org/html/2512.22660v1#S2.T1 "Table 1 ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") we present summary statistics for continuous variables in our dataset. All monetary values are expressed in millions of USD. In particular, the table includes the mean, standard deviation, minimum, and maximum. The dataset contains 734 observations.

The attachment point represents the threshold above which the CAT bond begins to absorb losses. It varies across tranches, with a mean of $2505.3 million and a standard deviation of $3565.5.
Related to this, the attachment probability reflects the modelled probability that the bond will be triggered. This value ranges from nearly 0 to 23%, with a mean of 3.9%.

Turning to market indicators, the BB spread is the average spread of BB-rated corporate bonds at issuance, serving as a benchmark for market pricing conditions. In our sample, the BB spread averages 3.5%, ranging from 1.5% to 11%. Issuer-specific characteristics also play an important role. Cedent tenure measures the number of months the cedent has participated in the CAT bond market prior to a given issuance. This variable proxies for issuer experience. It ranges from 0 to 281 months, with a mean of 61 months.

The coverage limit corresponds to the maximum payout that the bond provides in the event of a qualifying catastrophe. The mean coverage limit is $3.267 billion. Expected loss reflects the actuarial loss expectation over the bond’s term. The average expected loss is 2.5%, with values ranging from 0 to 15%. The final spread price is the risk premium paid to investors, expressed as a percentage of notional. This is the dependent variable in our empirical analysis. The mean spread is 7.7%. Throughout the paper, the terms “coupon”, “spread”, and “coupon rate” are used interchangeably to denote the risk premium paid to investors over the reference rate.

We also include the Rate-on-Line (ROL) index, which is an external index that tracks average pricing in the reinsurance market. The mean value is 220.5, with a range from 151.8 to 293.8. Tranche size denotes the value of each issuance. The average is $134.3 million. Finally, the term of each bond, measured in months, reflects the contract duration. The average term is 36.4 months, with a minimum of 1 and a maximum of 120.5

Table 2: Summary statistics for binary variables. The dataset contains 734 observations. Variables in Peril type, Trigger type, and Territory type are mutually exclusive, while observations may belong to multiple categories in the Region×Peril group.

|  |  |  |
| --- | --- | --- |
| Variable | Obs. | Percentage |
| \rowcolorgray!10      Peril type | | |
| Multiperil | 408 | 55.59%55.59\% |
| Storm | 177 | 24.11%24.11\% |
| Earthquake | 127 | 17.3%17.3\% |
| Other | 22 | 3%3\% |
| \rowcolorgray!10      Trigger type | | |
| Indemnity | 316 | 43.05%43.05\% |
| Other trigger | 418 | 56.95%56.95\% |
| \rowcolorgray!10      RegionxPeril combination | | |
| USxWind | 459 | 62.53%62.53\% |
| USxEarthquake | 407 | 55.45%55.45\% |
| EuropexWind | 138 | 18.8%18.8\% |
| JapanxEarthquake | 89 | 12.13%12.13\% |
| \rowcolorgray!10      Territory type | | |
| Multiterritory | 188 | 25.61%25.61\% |
| US | 420 | 57.22%57.22\% |
| Europe | 54 | 7.36%7.36\% |
| Japan | 45 | 6.13%6.13\% |
| Other territory | 31 | 4.22%4.22\% |

In Table [2](https://arxiv.org/html/2512.22660v1#S2 "2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") we provide descriptive statistics for the binary variables. The dataset contains a total of 734 observations. The Percentage column reports the share of each category relative to all observations. Variables in the categories Peril type, Trigger type, and Territory type are mutually exclusive, whereas observations may fall into multiple categories within the Region×Peril combination group.

The Multiperil variable indicates whether a tranche covers more than one type of peril. This applies to 55.6% of bonds. Among individual peril types, storm risks are present in 24.1% of tranches, earthquake risks in 17.3%, and other perils (e.g., flood, wildfire, pandemic) in 3%. With respect to trigger mechanisms, 43.1% of bonds use an indemnity trigger, which pays out based on actual losses incurred by the issuer. The remaining 56.9% employ non-indemnity triggers, such as industry loss, parametric, or modelled loss mechanisms.

The dataset also includes several region-peril variables, indicating whether the bond covers specific combinations such as U.S. wind (62.5%), U.S. earthquake (55.5%), Europe wind (18.8%), and Japan earthquake (12.1%). Multiterritory bonds (25.6%) provide coverage across more than one geographic region, while single-region variables show that 57.2% of tranches cover the U.S., 7.4% Europe, 6.1% Japan, and 4.2% other territories (e.g., Australia, Mexico, Caribbean countries).

## 3 Climate variability variables

Climate variability indices capture large-scale, recurring patterns in ocean-atmosphere systems that influence the frequency and severity of extreme weather events worldwide. We consider 7 climate variability indicators as well as sea surface temperatures across various oceanic regions.

The first indicator we consider is the ONI, which captures SST anomalies in the central Pacific (Niño 3.4 region) [glantz2020reviewing]. The ONI is the primary measure of the El Niño–Southern Oscillation (ENSO) phenomenon, where positive values indicate El Niño conditions and negative values indicate La Niña.

Next, we include the AO, an index representing atmospheric pressure variability over the Arctic and mid-latitudes [lorenz1951seasonal]. The AO describes the strength of the polar vortex. In its positive phase, it tends to confine colder air to the polar regions, whereas its negative phase allows cold air to spill into mid-latitudes, increasing the likelihood of extreme weather in North America and Europe.

The third indicator is the NAO, which reflects pressure differences between the Azores High and the Icelandic Low [visbeck2003north]. The NAO significantly influences winter weather, storm tracks, and precipitation across the North Atlantic region, especially in Europe.

We also consider OLR, a measure of the Earth’s radiative heat loss to space [singh2022thermodynamics]. OLR serves as a proxy for tropical convection and cloud cover, with lower values generally indicating stronger convective activity and potential rainfall.

The fifth indicator is the PNA pattern, a mode of atmospheric variability associated with pressure anomalies across the North Pacific and North America [franzke2011synoptic]. The PNA affects the jet stream and plays a critical role in shaping winter climate conditions across the United States and Canada, with implications for windstorm and cold-weather risks.

Another index included in our analysis is the PDO, which tracks multi-decadal fluctuations in North Pacific sea surface temperatures [deser2010sea]. Positive and negative phases of the PDO are linked to changes in regional climate conditions such as droughts, floods, and temperature anomalies.

Finally, we examine the SOI, which measures sea-level pressure differences between Tahiti and Darwin [ranasinghe2004southern]. Like the ONI, the SOI is a core ENSO indicator, with strongly negative values corresponding to El Niño episodes.

In Figure [2](https://arxiv.org/html/2512.22660v1#S3.F2 "Figure 2 ‣ 3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") we present the correlation coefficients between CAT bond coupon and lagged values of climate indices [mantegna1999introduction]. Each index is shifted backward in time from 2 to 18 months to capture potential delayed effects. The ONI exhibits negative correlations with coupon values, with the lowest values between 9 and 14 months lag. This suggests that warmer ENSO phases might be associated with lower CAT bond coupons. The AO shows positive correlations across most lags, peaking slightly at around 3-5 months and again at 14-16 months. The NAO displays positive correlations at shorter lags (around 3-5 months) and again at 12-13 months, with a peak correlation close to 0.12. The OLR stands out as one of the most consistently positively correlated indices, especially at higher lags between 11 and 16 months, where correlations approach or exceed 0.2. Since OLR is a proxy for tropical convection and rainfall, these findings may indicate that sustained tropical activity affects perceived risk in CAT bond markets. The PNA also shows a relatively stable and positive relationship with CAT bond coupons. Correlations range from 0.05 to over 0.2.
In contrast, the PDO consistently exhibits negative correlations across all lags, with a particularly strong values at short lags between 2 and 4 months.
Finally, the SOI shows a broadly positive correlation values, especially between 5 and 15 months. Correlations peak above 0.2 around month 14. Since SOI and ONI are both ENSO-related indices, this pattern reinforces the observed link between ENSO dynamics and CAT bond pricing.

Overall, the figure reveals that OLR, SOI, and PNA exhibit the strongest and most consistent positive correlations with CAT bond coupons, particularly at lags above 10 months. This suggests that large-scale climate variability, especially those linked to tropical convection and North American atmospheric patterns, may have delayed yet measurable impacts on CAT bond pricing mechanisms. In contrast, the PDO and ONI indices are negatively or weakly correlated with spreads.

![Refer to caption](correlation_big_dataset_mean_2020.png)


Figure 2: Correlation between catastrophe bond coupon rates and lagged values of large-scale climate indices. The x-axis shows the number of months each climate index is shifted backward to capture delayed effects, while the y-axis presents the corresponding correlation coefficient.

In Figure [3](https://arxiv.org/html/2512.22660v1#S3.F3 "Figure 3 ‣ 3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") we present the correlation coefficient between catastrophe bond coupon rates and lagged SST anomalies across seven oceanic regions: World (global mean SST), Atlantic Hurricane, North Atlantic, Subpolar North Atlantic, Gulf of Mexico, Gulf of Maine, and Niño SST (Niño 3.4 region). SST values were shifted backward by 0 to 18 months to assess whether delayed oceanic thermal patterns have explanatory power for CAT bond pricing.

Taken together, the figure suggests that regional SST anomalies, particularly in the Atlantic Hurricane region, Gulf of Mexico, and North Atlantic, are more strongly correlated with CAT bond coupons than global or Niño SST indicators.

![Refer to caption](sst_mean_2020.png)


Figure 3: Correlation between catastrophe bond coupon rates and lagged SST across various oceanic regions. The xx–axis represents the number of months by which SST values are shifted backward, and the yy–axis shows the corresponding correlation coefficient.

## 4 Linear regression comparison

We compare the explanatory power of two models. The first model replicates the one proposed in [braun2016pricing], serving as a benchmark. The second is our extended model, which incorporates additional variables related to climate variability.

The benchmark model follows the original approach and includes a comprehensive set of bond-specific and structural variables. These include catastrophe bond fundamentals such as expected loss, size, term, and trigger type, as well as peril and region-specific dummies (Wind, Earthquake, Multiterritory, US, Europe, Japan, and their interactions). It also controls for issuer quality (Swiss Re, investment grade), market conditions (ROL index, BB spread).

The extended model builds upon this structure by incorporating additional variables. In particular, it includes the ROL index change, which represents the annual change in the ROL index. We also include two lagged climate indices: SOI shifted by 15 months and OLR shifted by 12 months. These additions aim to test whether climate-related variables carry additional explanatory power beyond traditional CAT bond characteristics.

For the feature selection for the extended model we used the Elastic Net regularization method [zou2005regularization]. This approach combines the L1L\_{1} penalty from Lasso regression with the L2L\_{2} penalty from Ridge regression. By balancing these two components, Elastic Net selects the most relevant predictors.
This procedure allowed us to identify the subset of climate and market variables that contributed most to explaining the variation in CAT bond coupons.
The dependent variable in both models is the final spread price, and all variables have been standardized or transformed as necessary for comparability.

The evaluation of point forecasts shows that both models perform well in terms of predictive accuracy. For the benchmark model, the OLS regression achieves mean squared error M​S​E=0.000315MSE=0.000315, mean absolute error M​A​E=0.01323MAE=0.01323, and root mean squared error R​M​S​E=0.01774RMSE=0.01774 on the test sample. For the extended model, which incorporates climate-related variables, test errors improve to M​S​E=0.000283MSE=0.000283, M​A​E=0.01279MAE=0.01279, and R​M​S​E=0.01682RMSE=0.01682. These results confirm that adding the climate indicators improves the explanatory and predictive power of the model.

In addition to point forecasts, we also conduct a probabilistic forecasting exercise to evaluate the uncertainty surrounding the predicted catastrophe bond coupons. The dataset is divided into three non-overlapping subsets in an 80:10:10 ratio. The first part is used to estimate model parameters, the second serves as a calibration window, and the third is reserved for out-of-sample testing. In the calibration window, we generate point forecasts, compute residuals, and fit a normal distribution to the forecast errors. Based on these residuals, we also calculate empirical quantiles to capture the historical distribution of forecast uncertainty. In the final test window, we produce probabilistic forecasts by adding 1,000 random draws from the fitted normal distribution to each model’s point prediction. This approach yields full predictive distributions for each observation, from which we derive probabilistic measures such as the 5th, 50th, and 95th percentiles.

To assess the quality of the probabilistic forecasts, we apply the Kupiec and Christoffersen tests for Value-at-Risk (VaR) at the 5% level, including tests for unconditional coverage (LRUC), independence (LRIND), and conditional coverage (LRCC), along with the Basel traffic-light classification [christoffersen1998evaluating, kupiec1995techniques]. For the benchmark model, the percentage of failures equals 4.35%, with L​R​U​C=0.0645LRUC=0.0645 (p=0.7995)(p=0.7995), L​R​I​N​D=0.277LRIND=0.277 (p=0.5987)(p=0.5987), and L​R​C​C=0.3415LRCC=0.3415 (p=0.843)(p=0.843), placing the model in the green Basel zone. For the extended model, the percentage of failures equals 1.45%, with L​R​U​C=2.5137LRUC=2.5137 (p=0.1129)(p=0.1129), L​R​I​N​D=0.0299LRIND=0.0299 (p=0.8628)(p=0.8628), and L​R​C​C=2.5436LRCC=2.5436 (p=0.2803)(p=0.2803), also classified as green. These outcomes suggest that both models generate well-calibrated probabilistic forecasts, with the extended model producing fewer exceedances in the lower tail. Overall, the results show that extending the model with climate-related variables improves not only point forecast accuracy but also the stability and reliability of probabilistic predictions.

## 5 Machine learning approach

We applied linear regression, which allowed us to directly compare the benchmark feature set with our proposed feature set [braun2016pricing]. In the next step, we extend this comparison by applying various machine learning models using both benchmark feature set and our own, to evaluate how different algorithms perform across the two models. We apply 7 models: Random Forest, Bayesian Ridge Regression, Gradient Boosting Regression, Extremely Randomized Trees, Automatic Relevance Determination Regression, Light Gradient Boosting Machine, and Extreme Gradient Boosting.
All models are trained on the same dataset
𝒟={(xi,yi)}i=1N\mathcal{D}=\{(x\_{i},y\_{i})\}\_{i=1}^{N},
where xi∈ℝpx\_{i}\in\mathbb{R}^{p} denotes the vector of features and yi∈ℝy\_{i}\in\mathbb{R} the target variable (CAT bond coupon).
The goal is to learn a function f:ℝp→ℝf:\mathbb{R}^{p}\rightarrow\mathbb{R} that minimizes prediction error on unseen data.

Random Forest is an ensemble method that combines multiple decision trees [james2013introduction].
Each tree is trained on a bootstrap sample of the dataset,
and at each split only a random subset of features is considered,
which helps to reduce correlation between trees.
Formally, the algorithm builds TT regression trees {ht​(x)}t=1T\{h\_{t}(x)\}\_{t=1}^{T},
and the final prediction is obtained by averaging their outputs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^​(x)=1T​∑t=1Tht​(x).\hat{y}(x)=\frac{1}{T}\sum\_{t=1}^{T}h\_{t}(x). |  | (1) |

Bayesian Ridge Regression is a linear regression model that introduces a probabilistic
framework by placing prior distributions over the model parameters [tipping2001sparse].
This approach allows automatic regularization and provides posterior distributions
instead of point estimates.
The regression model is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi=xi⊤​w+εi,εi∼𝒩​(0,α−1),y\_{i}=x\_{i}^{\top}w+\varepsilon\_{i},\quad\varepsilon\_{i}\sim\mathcal{N}(0,\alpha^{-1}), |  | (2) |

where w∈ℝpw\in\mathbb{R}^{p} is the weight vector and α\alpha denotes the noise precision.
During hyperparameter tuning, α\alpha was searched over the range
α∈[10−6,103]\alpha\in[10^{-6},10^{3}].

A zero-mean Gaussian prior is placed over the coefficients:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(w∣λ)∼𝒩​(0,λ−1​Ip),p(w\mid\lambda)\sim\mathcal{N}(0,\lambda^{-1}I\_{p}), |  | (3) |

where λ\lambda controls the strength of regularization.
The prior precision parameter was tuned over
λ∈[10−6,103]\lambda\in[10^{-6},10^{3}].

Gradient Boosting is an ensemble method that builds a strong predictor by combining
multiple weak learners (typically regression trees) in a stage-wise manner [friedman2003multiple].
Each new tree is trained to minimize the residual errors of the previous ensemble
using gradient descent in function space.
The model is expressed as an additive expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fm​(x)=∑k=1mγk​hk​(x),F\_{m}(x)=\sum\_{k=1}^{m}\gamma\_{k}h\_{k}(x), |  | (4) |

where hk​(x)h\_{k}(x) denotes the kk-th regression tree (weak learner) and γk\gamma\_{k} is its weight.
The method optimizes a differentiable loss function L​(y,F​(x))L(y,F(x)) by iteratively fitting new trees
to the negative gradient of the loss with respect to the current model predictions.
At iteration mm, the pseudo-residuals are computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri​m=−[∂L​(yi,F​(xi))∂F​(xi)]F​(x)=Fm−1​(x).r\_{im}=-\left[\frac{\partial L(y\_{i},F(x\_{i}))}{\partial F(x\_{i})}\right]\_{F(x)=F\_{m-1}(x)}. |  | (5) |

for i=1,2,…,Ni=1,2,\ldots,N.
A new regression tree hm​(x)h\_{m}(x) is fitted to the residuals {ri​m}\{r\_{im}\}.
The optimal step size γm\gamma\_{m} is obtained by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | γm=argminγ​∑i=1NL​(yi,Fm−1​(xi)+γ​hm​(xi)).\gamma\_{m}=\mathrm{argmin}\_{\gamma}\sum\_{i=1}^{N}L\big(y\_{i},F\_{m-1}(x\_{i})+\gamma h\_{m}(x\_{i})\big). |  | (6) |

The model is then updated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fm​(x)=Fm−1​(x)+ν​γm​hm​(x),F\_{m}(x)=F\_{m-1}(x)+\nu\gamma\_{m}h\_{m}(x), |  | (7) |

where ν∈(0,1]\nu\in(0,1] is the learning rate controlling the contribution of each tree.

The Extremely Randomized Trees algorithm is an ensemble method based on aggregating
a large number of randomized decision trees [geurts2006extremely].
It is related to RF but introduces additional randomization in the tree-building process.
The algorithm builds TT regression trees {ht​(x)}t=1T\{h\_{t}(x)\}\_{t=1}^{T}.
Each tree is trained on the entire dataset (unlike RF, where bootstrap samples are used).
At each split of a tree, a random subset of features M⊂{1,…,p}M\subset\{1,\dots,p\} is first selected.
For every feature in this subset, random split thresholds are then drawn uniformly from the observed range of that feature.
Among all possible splits, the algorithm chooses the one that maximizes the reduction in variance,
following a standard variance reduction criterion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(S,f,θ)=Var​(S)−|SL||S|​Var​(SL)−|SR||S|​Var​(SR),\Delta(S,f,\theta)=\mathrm{Var}(S)-\frac{|S\_{L}|}{|S|}\mathrm{Var}(S\_{L})-\frac{|S\_{R}|}{|S|}\mathrm{Var}(S\_{R}), |  | (8) |

where SS is the current sample set at a node, ff is the feature,
θ\theta is the split threshold, and SL,SRS\_{L},S\_{R} are the left and right subsets after splitting.

Automatic Relevance Determination regression is a Bayesian linear model
that extends ridge regression by placing independent priors on each coefficient [li2002bayesian].
The model is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi=xi⊤​w+εi,εi∼𝒩​(0,α−1),y\_{i}=x\_{i}^{\top}w+\varepsilon\_{i},\quad\varepsilon\_{i}\sim\mathcal{N}(0,\alpha^{-1}), |  | (9) |

where w∈ℝpw\in\mathbb{R}^{p} is the weight vector and α\alpha is the precision

In ARD, each coefficient wjw\_{j} has an individual Gaussian prior:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(w∣{λj})∼∏j=1p𝒩​(wj∣0,λj−1),p(w\mid\{\lambda\_{j}\})\sim\prod\_{j=1}^{p}\mathcal{N}(w\_{j}\mid 0,\lambda\_{j}^{-1}), |  | (10) |

where the precision parameters were tuned jointly over the range
λj∈[10−6,103]\lambda\_{j}\in[10^{-6},10^{3}].

Noise precision was included in tuning as
α∈[10−6,103]\alpha\in[10^{-6},10^{3}].
Applying Bayes’ theorem, the posterior distribution of the weights is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(w∣X,y,α,{λj})∼𝒩​(w∣μw,Σw),p(w\mid X,y,\alpha,\{\lambda\_{j}\})\sim\mathcal{N}(w\mid\mu\_{w},\Sigma\_{w}), |  | (11) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σw=(diag​(λ1,…,λp)+α​X⊤​X)−1,\Sigma\_{w}=\left(\mathrm{diag}(\lambda\_{1},\dots,\lambda\_{p})+\alpha X^{\top}X\right)^{-1}, |  | (12) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | μw=α​Σw​X⊤​y,\mu\_{w}=\alpha\Sigma\_{w}X^{\top}y, |  | (13) |

where X∈ℝN×pX\in\mathbb{R}^{N\times p} is the design matrix.

Light Gradient Boosting Machine is a gradient boosting framework
based on decision trees [kopitar2020early].
It improves upon standard gradient boosting by using optimized techniques such as
histogram-based splitting and leaf-wise tree growth.
LGBM constructs an additive model of regression trees:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fm​(x)=∑k=1mγk​hk​(x),F\_{m}(x)=\sum\_{k=1}^{m}\gamma\_{k}h\_{k}(x), |  | (14) |

where hk​(x)h\_{k}(x) is the kk-th regression tree and γk\gamma\_{k} is its weight.
At iteration mm, the objective is to minimize a differentiable loss function L​(y,F​(x))L(y,F(x)).
Using a second-order Taylor expansion, the loss is approximated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | L(m)≈∑i=1N[gi​m​hm​(xi)+12​hi​m​hm​(xi)2],L^{(m)}\approx\sum\_{i=1}^{N}\left[g\_{im}h\_{m}(x\_{i})+\tfrac{1}{2}h\_{im}h\_{m}(x\_{i})^{2}\right], |  | (15) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | gi​m=∂L​(yi,F​(xi))∂F​(xi),hi​m=∂2L​(yi,F​(xi))∂F​(xi)2g\_{im}=\frac{\partial L(y\_{i},F(x\_{i}))}{\partial F(x\_{i})},\quad h\_{im}=\frac{\partial^{2}L(y\_{i},F(x\_{i}))}{\partial F(x\_{i})^{2}} |  | (16) |

are the first and second derivatives of the loss with respect to predictions.
The optimal leaf values of the tree are computed using both gradients gi​mg\_{im}
and Hessians hi​mh\_{im}, which improves convergence compared to first-order methods.
The model is updated iteratively as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fm​(x)=Fm−1​(x)+ν​γm​hm​(x),F\_{m}(x)=F\_{m-1}(x)+\nu\gamma\_{m}h\_{m}(x), |  | (17) |

where ν∈(0,1]\nu\in(0,1] is the learning rate controlling the contribution of each tree.

Extreme Gradient Boosting is an efficient and scalable implementation
of gradient boosting that incorporates additional regularization to improve
generalization and prevent overfitting [carmona2019predicting].
It has become one of the most widely used boosting algorithms for both regression
and classification tasks.
XGBoost constructs an additive model of regression trees:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fm​(x)=∑k=1mhk​(x),F\_{m}(x)=\sum\_{k=1}^{m}h\_{k}(x), |  | (18) |

where hk​(x)h\_{k}(x) denotes the kk-th regression tree.
The training objective at iteration mm is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ(m)=∑i=1NL​(yi,Fm−1​(xi)+hm​(xi))+Ω​(hm),\mathcal{L}^{(m)}=\sum\_{i=1}^{N}L(y\_{i},F\_{m-1}(x\_{i})+h\_{m}(x\_{i}))+\Omega(h\_{m}), |  | (19) |

where L​(y,y^)L(y,\hat{y}) is a differentiable convex loss function,
and Ω​(hm)\Omega(h\_{m}) is a regularization term that penalizes model complexity.
Using a second-order Taylor expansion, the objective can be approximated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ(m)≈∑i=1N[gi​m​hm​(xi)+12​hi​m​hm​(xi)2]+Ω​(hm),\mathcal{L}^{(m)}\approx\sum\_{i=1}^{N}\left[g\_{im}h\_{m}(x\_{i})+\tfrac{1}{2}h\_{im}h\_{m}(x\_{i})^{2}\right]+\Omega(h\_{m}), |  | (20) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | gi​m=∂L​(yi,F​(xi))∂F​(xi),hi​m=∂2L​(yi,F​(xi))∂F​(xi)2.g\_{im}=\frac{\partial L(y\_{i},F(x\_{i}))}{\partial F(x\_{i})},\quad h\_{im}=\frac{\partial^{2}L(y\_{i},F(x\_{i}))}{\partial F(x\_{i})^{2}}. |  | (21) |

The regularization term is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω​(hm)=γ​T+12​λ​∑j=1Twj2,\Omega(h\_{m})=\gamma T+\frac{1}{2}\lambda\sum\_{j=1}^{T}w\_{j}^{2}, |  | (22) |

where TT is the number of leaves in the tree, wjw\_{j} is the weight of leaf jj,
γ\gamma penalizes the number of leaves, and λ\lambda controls L2L\_{2} regularization
on leaf weights.
The optimal weight for each leaf is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | wj∗=−∑i∈Ijgi​m∑i∈Ijhi​m+λ,w\_{j}^{\*}=-\frac{\sum\_{i\in I\_{j}}g\_{im}}{\sum\_{i\in I\_{j}}h\_{im}+\lambda}, |  | (23) |

where IjI\_{j} is the set of samples assigned to leaf jj.
The corresponding optimal value of the objective function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒopt(m)=−12​∑j=1T(∑i∈Ijgi​m)2∑i∈Ijhi​m+λ+γ​T.\mathcal{L}^{(m)}\_{\text{opt}}=-\frac{1}{2}\sum\_{j=1}^{T}\frac{\left(\sum\_{i\in I\_{j}}g\_{im}\right)^{2}}{\sum\_{i\in I\_{j}}h\_{im}+\lambda}+\gamma T. |  | (24) |

To ensure a fair comparison across methods, we performed hyperparameter tuning for all machine learning models. We applied a randomized search combined with 5-fold cross-validation, using the training set only. For each model, a predefined search space of hyperparameters was explored, and the configuration minimizing the cross-validated RMSE was selected. Tree-based models (RF, ETR, GB, LGBM, XGBoost) were tuned over parameters controlling tree depth, number of estimators, subsampling, and regularization strength, while linear Bayesian models (BRR and ARD) were tuned over their respective prior precision parameters. The final results reported below are based on models refitted on the full training data using the best-performing hyperparameter sets.

Table 3: Values of the RMSE calculated for the predictions on the testing set, rounded to five significant figures.

| Model | Benchmark model | Our model |
| --- | --- | --- |
| OLS | 0.018443 | 0.016823 |
| RF | 0.018844 | 0.017563 |
| BRR | 0.018447 | 0.016813 |
| GBR | 0.019155 | 0.017756 |
| ETR | 0.014161 | 0.012294\mathbf{0.012294} |
| ARD | 0.017709 | 0.017085 |
| LGBM | 0.019088 | 0.018858 |
| XGB | 0.018487 | 0.018163 |

In Table [3](https://arxiv.org/html/2512.22660v1#S5.T3 "Table 3 ‣ 5 Machine learning approach ‣ 4 Linear regression comparison ‣ 3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data") we present the RMSE on the test set
for both benchmark feature set and our proposed features, across all evaluated models. These results correspond to point forecasts, where each model provides a single predicted value
of the CAT bond coupon for each observation.
The baseline model (OLS) shows slightly lower error with our features (0.0168)
compared to benchmark (0.0184). A similar pattern can be observed for all models,
indicating that our representation generally improves predictive accuracy.
Among tree-based ensembles, the ETR algorithm achieves
the lowest overall error, with RMSE of 0.0123 for our features, which is
a notable improvement over benchmark 0.0142 (approximately 13.2%).
Other boosting methods such as Gradient Boosting, LGBM, and XGBoost
show consistent but smaller gains.
Linear Bayesian models (BRR and ARD) also benefit from our features, though
the improvement is less pronounced. Overall, the comparison demonstrates that
our feature set leads to systematically better results across a range of
algorithms, with the largest relative gain observed for ETR. We also explored probabilistic forecasts for the machine learning models using the same procedure as in the linear regression framework, and the results were consistent with those reported in Section [4](https://arxiv.org/html/2512.22660v1#S4 "4 Linear regression comparison ‣ 3 Climate variability variables ‣ 2 Data ‣ Machine learning models for predicting catastrophe bond coupons using climate data"), confirming that the inclusion of climate-related variables improved both point and probabilistic predictive performance across all approaches.

## 6 Conclusions

CAT bonds are insurance-linked securities designed to transfer catastrophe risk from insurers and reinsurers to capital market investors. Introduced in the 1990s following a series of major natural disasters, these instruments allow issuers to obtain protection against extreme losses by issuing debt that is partially or fully forgiven in the event of a qualifying catastrophe. In return, investors receive attractive coupon payments as compensation for taking on this risk. The CAT bond market has grown over the past two decades, reaching tens of billions of dollars in outstanding notional value, and has become a crucial component of global risk management and alternative reinsurance. Because CAT bonds directly link financial performance to natural hazard outcomes, their pricing reflects not only traditional financial factors but also evolving climate and environmental risks.

In this study, we investigated whether climate variability helps explain and predict CAT bond coupons. We combined standard bond- and market-related features used in the literature with climate indicators such as ONI, SOI, AO, NAO, PDO, PNA, OLR, and regional SST. Our dataset covers 734 primary-market tranches issued between June 1997 and December 2020.

Before conducting predictive modeling, we performed an extensive correlation analysis between CAT bond coupon rates and lagged values of key climate indices. The results revealed several patterns. OLR, SOI, and PNA exhibited the strongest positive correlations with CAT bond coupons, especially at lags of 10–16 months, suggesting that tropical convection and North American atmospheric variability have delayed yet measurable impacts on market pricing. In contrast, the PDO and ONI indices showed persistently negative or weak correlations, while regional SST anomalies, particularly in the Atlantic Hurricane region, Gulf of Mexico, and North Atlantic, were more strongly associated with coupon variation than global or Niño SST averages.

Building upon these insights, we compared two model specifications: a benchmark that replicates the model proposed in [braun2016pricing] and an extended feature set that extends the feature set by climate-related variables. Using an 80:10:10 split, the first window was used for estimation, the second for calibration, and the third for out-of-sample testing. For point forecasts, ordinary least squares (OLS) with the benchmark features achieved a train R2R^{2} of 0.833 and test errors of MSE =0.000315=0.000315, MAE =0.01323=0.01323, and RMSE =0.01774=0.01774. Our specification improved performance to a train R2R^{2} of 0.835 and reduced test errors to MSE =0.000283=0.000283, MAE =0.01279=0.01279, and RMSE =0.01682=0.01682. These results indicate that adding climate information improves point prediction accuracy.

Next, we compared several machine learning algorithms. Across models, the extended feature set lowered test RMSE compared to the benchmark model. Among tree-based ensembles, Extremely Randomized Trees achieved the best results, with RMSE =0.0123=0.0123 for the extended features compared with 0.01420.0142 for the benchmark features. Gradient Boosting, LightGBM, XGBoost, and Bayesian linear models (BRR, ARD) also showed smaller error values when climate variables were included. Overall, these findings confirm that flexible, nonlinear learners can effectively increase predictive accuracy.

Finally, we constructed probabilistic forecasts to quantify uncertainty around coupon predictions. Residuals from the calibration window were used to fit a normal error distribution and to compute empirical quantiles. In the test window, we generated predictive distributions by adding 1,000 Monte Carlo draws from the fitted error law to each point forecast and then evaluated 5% Value-at-Risk coverage. For the benchmark specification, the percentage of failures was 4.35%, with L​R​U​C=0.0645LRUC=0.0645 (p=0.7995)(p=0.7995), L​R​I​N​D=0.277LRIND=0.277 (p=0.5987)(p=0.5987), and L​R​C​C=0.3415LRCC=0.3415 (p=0.843)(p=0.843), yielding a Basel green classification. For the extended model, percentage of failures was 1.45%, with L​R​U​C=2.5137LRUC=2.5137 (p=0.1129)(p=0.1129), L​R​I​N​D=0.0299LRIND=0.0299 (p=0.8628)(p=0.8628), and L​R​C​C=2.5436LRCC=2.5436 (p=0.2803)(p=0.2803), also in the green zone. These results show that both models produce well-calibrated tails.

Taken together, the evidence shows that climate variability provides additional important information for CAT bond pricing and that machine learning methods can capture this information to improve both point and probabilistic forecasts. While no single model dominates every metric, the Extremely Randomized Trees seems to perform the best, making it a practical choice for forecasting CAT bond coupons.

## Acknowledgements

We would like to express our gratitude to Alexander Braun for providing access to the dataset used in this study. The work of JK and KB was supported by NCN Grant No. 2022/47/B/HS4/02139.