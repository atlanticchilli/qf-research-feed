---
authors:
- Vladimír Holý
doc_id: arxiv:2510.09785v1
family_id: arxiv:2510.09785
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2510.09785v1
url_html: https://arxiv.org/html/2510.09785v1
venue: arXiv q-fin
version: 1
year: 2025
---

The Pitfalls of Continuous Heavy-Tailed Distributions in High-Frequency Data Analysis

Vladimír Holý

Prague University of Economics and Business

Winston Churchill Square 4, 130 67 Prague 3, Czechia

[vladimir.holy@vse.cz](mailto:vladimir.holy@vse.cz)

Abstract:
We address the challenges of modeling high-frequency integer price changes in financial markets using continuous distributions, particularly the Student’s t-distribution. We demonstrate that traditional GARCH models, which rely on continuous distributions, are ill-suited for high-frequency data due to the discreteness of price changes. We propose a modification to the maximum likelihood estimation procedure that accounts for the discrete nature of observations while still using continuous distributions. Our approach involves modeling the log-likelihood in terms of intervals corresponding to the rounding of continuous price changes to the nearest integer. The findings highlight the importance of adjusting for discreteness in volatility analysis and provide a framework for incroporating any continuous distribution for modeling high-frequency prices.

Keywords: High-Frequency Data, GARCH Model, Score-Driven Model, Student’s t-Distribution.

JEL Codes: C22, C58, G12.

## 1 Introduction

Although originally developed to model daily volatility in financial markets, generalized autoregressive conditional heteroskedasticity (GARCH) models are also applied in high-frequency data analysis to capture intraday time-varying volatility (see, e.g., Engle, [2002](https://arxiv.org/html/2510.09785v1#bib.bib13)). Intraday volatility modeling dates back to Ghysels and Jasiak ([1998](https://arxiv.org/html/2510.09785v1#bib.bib17)), Engle ([2000](https://arxiv.org/html/2510.09785v1#bib.bib15)), and Meddahi *et al.* ([2006](https://arxiv.org/html/2510.09785v1#bib.bib25)). Over the years, the intensity of trading has gradually increased, and the discreteness of prices has become more pronounced. To address this issue of discreteness, recent literature has proposed several dynamic models based on the Skellam distribution, such as Koopman *et al.* ([2017](https://arxiv.org/html/2510.09785v1#bib.bib22)), Koopman *et al.* ([2018](https://arxiv.org/html/2510.09785v1#bib.bib23)), Alomani *et al.* ([2018](https://arxiv.org/html/2510.09785v1#bib.bib1)), Gonçalves and Mendes-Lopes ([2020](https://arxiv.org/html/2510.09785v1#bib.bib18)), Cui *et al.* ([2021](https://arxiv.org/html/2510.09785v1#bib.bib11)), Doukhan *et al.* ([2021](https://arxiv.org/html/2510.09785v1#bib.bib12)), Catania *et al.* ([2022](https://arxiv.org/html/2510.09785v1#bib.bib9)), and Holý ([2024](https://arxiv.org/html/2510.09785v1#bib.bib20)).

We take a different approach and address the issue of discreteness concerning the use of the continuous Student’s t-distribution. In Section [2](https://arxiv.org/html/2510.09785v1#S2 "2 Data and Modeling Strategy"), we outline an intraday analysis of stock price changes. For conciseness, we focus on the IBM stock; however, the empirical properties studied are widely observed across various stock markets. Empirical evidence for additional stocks is presented in Appendix [A](https://arxiv.org/html/2510.09785v1#A1 "Appendix A Evidence from Further Stocks"). In Section [3](https://arxiv.org/html/2510.09785v1#S3 "3 Unsuitability of Continuous Models"), we demonstrate that the Student’s t-distribution is unsuitable for analyzing integer price changes. The main reason is that its density function tends to degenerate into a shape of ⟂\perp, concentrated at a single point 0 with extremely heavy tails. In this sense, we build on the study of Holý ([2024](https://arxiv.org/html/2510.09785v1#bib.bib20)), in which this behavior was observed but not examined in detail. As we further show, the main risk lies in the fact that results from dynamic models estimated using various R packages may initially appear reasonable but are based on incorrect estimates. In Section [4](https://arxiv.org/html/2510.09785v1#S4 "4 Integer Model and Interval Maximum Likelihood Estimation"), we argue that continuous distributions can still be used, but they require a special method of estimation that accounts for the discrete nature of observations. We propose formulating the log-likelihood function in terms of the probabilities of continuous price changes falling into the interval corresponding to the rounding to the nearest integer that is actually observed. In Section [5](https://arxiv.org/html/2510.09785v1#S5 "5 Performance of Integer Models"), we estimate our GARCH-like model using the proposed interval maximum likelihood approach and find that it provides a comparable fit to the Skellam distribution. We conclude the paper in Section [6](https://arxiv.org/html/2510.09785v1#S6 "6 Conclusion").

The first contribution of this paper is the warning to practitioners not to rely on standard GARCH modeling with continuous distributions, especially those with heavy tails, as the results are uninformative at best and misleading at worst. The second contribution is the proposal of the simple modification to the maximum likelihood estimation procedure that accounts for the discreteness of data while still allowing the use of continuous distributions. The findings of our paper are relevant for researchers, risk managers, and traders who rely on these models for volatility forecasting, portfolio optimization, and derivative pricing.

## 2 Data and Modeling Strategy

In this study, we analyze the IBM stock traded on the New York Stock Exchange (NYSE). The IBM stock was selected because many relevant studies feature it, including Engle ([2000](https://arxiv.org/html/2510.09785v1#bib.bib15)), Liu and Maheu ([2012](https://arxiv.org/html/2510.09785v1#bib.bib24)), Catania *et al.* ([2022](https://arxiv.org/html/2510.09785v1#bib.bib9)), and Holý ([2024](https://arxiv.org/html/2510.09785v1#bib.bib20)). However, we stress that our core results are quite general, as the study revolves around two features that are widely observed across various financial markets—namely, the discreteness of price changes and the fact that zero is the most likely change. In Appendix [A](https://arxiv.org/html/2510.09785v1#A1 "Appendix A Evidence from Further Stocks"), we also report results for three additional stocks—the MCD stock traded on the NYSE, and the CSCO and MSFT stocks traded on the NASDAQ. These results are generally consistent with those for the IBM stock.

Our data sample for the IBM stock consists of tick-by-tick transactions from all 252 trading days in 2024. The data source is Refinitiv Eikon. We perform standard data cleaning steps of Barndorff-Nielsen *et al.* ([2009](https://arxiv.org/html/2510.09785v1#bib.bib3)). Specifically, we remove observations outside the standard trading hours of 9:30–16:00 EST, remove observations without recorded prices, and remove outliers with prices exceeding 10 mean absolute deviations within a rolling window of 201 observations. After data cleaning, we are left with over 15 million observations.

The tick-by-tick data have irregularly spaced observations, which pose some challenges. Engle ([2000](https://arxiv.org/html/2510.09785v1#bib.bib15)) addressed this issue by using returns divided by the square root of trade durations, thus modeling the variance per time unit. As pointed out by Holý ([2024](https://arxiv.org/html/2510.09785v1#bib.bib20)), this approach faces a significant issue for recent datasets due to the large number of zero or close-to-zero durations. Our data are recorded with millisecond precision, and 45 percent of transactions have zero durations. Although Holý ([2024](https://arxiv.org/html/2510.09785v1#bib.bib20)) proposed a model to address this issue, we decide to analyze the data at fixed frequencies for simplicity. We aggregate observations at 0.1, 1, 10, 60, and 300-second frequencies using the last tick method. We analyze price changes, i.e., the difference in successive prices in cents.

Figure [1](https://arxiv.org/html/2510.09785v1#S2.F1 "Figure 1 ‣ 2 Data and Modeling Strategy") shows the distribution of price changes. We can see that the vast majority of tick-by-tick price changes are quite small–52 percent are zero, while 98 percent lie between -10 and 10. Aggregating the prices to a 1-second frequency produces a similar distribution of price changes as the original ultra-high-frequency data. The associated data are available at <github.com/vladimirholy/continuous-high-frequency-garch>.

![Refer to caption](x1.png)


Figure 1: The distribution of price changes with the fitted density of the Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters.

## 3 Unsuitability of Continuous Models

We start our analysis by estimating volatility models based on the Student’s t-distribution for each trading day. First, we estimate a standard GARCH model of Engle ([1982](https://arxiv.org/html/2510.09785v1#bib.bib14)) and Bollerslev ([1986](https://arxiv.org/html/2510.09785v1#bib.bib7), [1987](https://arxiv.org/html/2510.09785v1#bib.bib8)), given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=μ+et,et∼t​(0,σt2,ν),σt2=ω+α​et−12+φ​σt−12.y\_{t}=\mu+e\_{t},\qquad e\_{t}\sim\mathrm{t}\left(0,\sigma\_{t}^{2},\nu\right),\qquad\sigma^{2}\_{t}=\omega+\alpha e\_{t-1}^{2}+\varphi\sigma^{2}\_{t-1}. |  | (1) |

Second, we estimate a score-driven model of Creal *et al.* ([2013](https://arxiv.org/html/2510.09785v1#bib.bib10)), also known as the generalized autoregressive score (GAS) model or dynamic conditional score (DCS) model, with a time-varying volatility parameter, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt∼t​(μ,σt2,ν),ln⁡σt2=ω+α​∇ln⁡σ2(yt−1;μ,σt−12,ν)+φ​σt−12,y\_{t}\sim\mathrm{t}\left(\mu,\sigma\_{t}^{2},\nu\right),\qquad\ln\sigma^{2}\_{t}=\omega+\alpha\nabla\_{\ln\sigma^{2}}(y\_{t-1};\mu,\sigma^{2}\_{t-1},\nu)+\varphi\sigma^{2}\_{t-1}, |  | (2) |

where ∇ln⁡σ2(yt−1;μ,σt−12,ν)\nabla\_{\ln\sigma^{2}}(y\_{t-1};\mu,\sigma^{2}\_{t-1},\nu) is the score with respect to ln⁡σ2\ln\sigma^{2}, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇ln⁡σ2(y;μ,σ2,ν)=∂lnf(y|μ,σ2,ν)∂ln⁡σ2.\nabla\_{\ln\sigma^{2}}\left(y;\mu,\sigma^{2},\nu\right)=\frac{\partial\ln f\left(y\middle|\mu,\sigma^{2},\nu\right)}{\partial\ln\sigma^{2}}. |  | (3) |

The main difference between the models is that the score-driven model reflects the shape of the Student’s t-distribution, particularly its heavy tails, in the dynamics of volatility through the score term. In the relevant literature, score-driven models are found to be superior both theoretically and empirically; see, e.g., Blasques *et al.* ([2015](https://arxiv.org/html/2510.09785v1#bib.bib5)) and Blazsek and Licht ([2020](https://arxiv.org/html/2510.09785v1#bib.bib6)). The dynamics in the score-driven model are also specified in terms of the logarithm of the scale parameter, similarly to the EGARCH model of Nelson ([1991](https://arxiv.org/html/2510.09785v1#bib.bib26)).

For the estimation, we utilize four R packages in total. The standard GARCH model is implemented in the `rugarch` package of Ghalanos ([2024](https://arxiv.org/html/2510.09785v1#bib.bib16)) and the `fGarch` package of Wuertz *et al.* ([2024](https://arxiv.org/html/2510.09785v1#bib.bib27)), while the `GAS` package of Ardia *et al.* ([2019](https://arxiv.org/html/2510.09785v1#bib.bib2)) and the `gasmodel` package of Holý ([2025](https://arxiv.org/html/2510.09785v1#bib.bib21)) provide functionality for score-driven models. We leave most arguments at their default values to showcase the basic use of these packages, especially with regard to the numerical optimizers.

The results of the estimation are reported in Table [1](https://arxiv.org/html/2510.09785v1#S3.T1 "Table 1 ‣ 3 Unsuitability of Continuous Models") for 1-second and 1-minute frequencies. While for the 1-minute frequency the results from all packages are quite similar, with a slightly better fit for the score-driven model, the results for the 1-second frequency show striking differences. The main discrepancies with regard to the parameters lie in the degrees of freedom of the Student’s t-distribution. Some packages impose a lower bound on ν\nu to ensure finite moments. The `rugarch` package has a lower bound of 2.1, the `fGarch` package 2, and the `GAS` package 4. In the `gasmodel` package, ν\nu is unbounded, i.e., it is only required to be positive. While for the first three packages the estimated values of ν\nu are close to these bounds, the `gasmodel` package estimates ν\nu with a median value of 0.220. The models with such small values of ν\nu yield an extremely high log-likelihood–with a median of 72 per observation, in contrast to about -2 for the other three packages. This behavior suggests a significant issue regarding the use of the Student’s t-distribution in this context.

Next, we focus on a simpler model with the Student’s t-distribution, in which σ2\sigma^{2} is static. Figure [2](https://arxiv.org/html/2510.09785v1#S3.F2 "Figure 2 ‣ 3 Unsuitability of Continuous Models") shows that, for all considered frequencies, the log-likelihood of the static model is maximized when ν\nu is very close to zero. In these cases, Figure [1](https://arxiv.org/html/2510.09785v1#S2.F1 "Figure 1 ‣ 2 Data and Modeling Strategy") further shows that the fitted Student’s t-distribution degenerates, with σ2\sigma^{2} approaching zero. The extremely small values of σ2\sigma^{2} and ν\nu cause the distribution to be concentrated at 0, with extremely heavy tails. Since the most likely value of price change is zero for all considered frequencies, this concentration of density at 0 leads to an explosion in the log-likelihood. The occurrence of nonzero values is then captured by the heavy tails of the distribution. No moments exist for ν≤1\nu\leq 1. The estimation of the parameters encounters numerical issues. In our case, σ2\sigma^{2} is estimated as the smallest possible positive double-precision floating-point number, 2−10742^{-1074}.
Note that, in Table [1](https://arxiv.org/html/2510.09785v1#S3.T1 "Table 1 ‣ 3 Unsuitability of Continuous Models"), when σ2\sigma^{2} is allowed to be time-varying, the numerical solver in the `gasmodel` package struggles to achieve the optimum, where σ2\sigma^{2} reaches its lowest possible value and thus remains virtually static. Figures [1](https://arxiv.org/html/2510.09785v1#S2.F1 "Figure 1 ‣ 2 Data and Modeling Strategy") and [2](https://arxiv.org/html/2510.09785v1#S3.F2 "Figure 2 ‣ 3 Unsuitability of Continuous Models") show that the lower the occurrence of zeros, the lower ν\nu must be for the log-likelihood and density at 0 to explode.

It follows that the Student’s t-distribution is unusable when exact zero values frequently occur. The results from our four packages might appear reasonable at first sight; however, all estimates in Table [1](https://arxiv.org/html/2510.09785v1#S3.T1 "Table 1 ‣ 3 Unsuitability of Continuous Models") are based on suboptimal solutions, either due to artificial bounds on ν\nu or convergence issues of the numerical solver. Neither the GARCH nor the score-driven models should be relied upon. The optimal solution, where the density takes the shape of ⟂\perp, is useless for any analysis, as it contains no meaningful information.

Table 1: The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on the Student’s t-distribution, estimated using various R packages.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | `rugarch` | `fGarch` | `GAS` | `gasmodel` | `rugarch` | `fGarch` | `GAS` | `gasmodel` |
| μ\mu | 0.000 | 0.000 | 0.002 | 0.000 | 0.106 | 0.103 | 0.117 | 0.108 |
| ω\omega | 0.027 | 0.000 | 0.000 | 0.000 | 1.878 | 1.887 | 0.007 | 0.005 |
| α\alpha | 0.119 | 1.000 | 0.043 | 1.350 | 0.072 | 0.074 | 0.188 | 0.183 |
| φ\varphi | 0.876 | 0.962 | 1.000 | 0.999 | 0.906 | 0.904 | 0.999 | 0.999 |
| ν\nu | 2.146 | 2.013 | 4.000 | 0.220 | 6.588 | 6.528 | 6.964 | 6.926 |
| AA | 0.001 | 0.002 | 0.022 | x | 0.020 | 0.020 | 0.023 | 0.022 |
| ℓ\ell | -1.903 | -1.884 | -1.992 | 72.009 | -3.574 | -3.574 | -3.572 | -3.569 |

Notes:
μ\mu – expected price difference; ω\omega – intercept in the volatility equation; α\alpha – variance/score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; AA – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell – average log-likelihood.

![Refer to caption](x2.png)


Figure 2: The log-likelihood from the fitted Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters. The dashed line represents the scale parameter at the lower bound, 2−10742^{-1074}, due to numerical precision.

## 4 Integer Model and Interval Maximum Likelihood Estimation

Fortunately, there is a simple cure for the degenerative behavior of the Student’s t-distribution on discrete data with zeros, caused by treating the observations as continuous values and maximizing the log-likelihood in the form of density: The integer observations can be considered as rounded continuous values. For example, instead of the exact value of 2, the observation should be treated as the interval (−1.5,2.5](-1.5,2.5]. In such an approach, the log-likelihood takes the form of the probability of the observed integer yy falling into its corresponding interval (y−0.5,y+0.5](y-0.5,y+0.5]. Rounding to the nearest integer is the most natural scheme for our purposes, as it produces intervals of equal length and preserves symmetry. For instance, when 0 is observed, the underlying continuous value is equally likely to have been slightly positive or slightly negative.

Let F(⋅|ν)F(\cdot|\nu) denote the cumulative distribution function of the Student’s t-distribution with ν\nu degrees of freedom. Let μt\mu\_{t} be the time-varying location parameter and σt2\sigma^{2}\_{t} the time-varying scale parameter. Let pp be the vector of parameters to be estimated, including ν\nu. The interval log-likehood function is then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ(p|y)=∑t=1nln(F(yt−μt+0.5σt|ν)−F(yt−μt−0.5σt|ν)).\ell\left(p\middle|y\right)=\sum\_{t=1}^{n}\ln\left(F\left(\frac{y\_{t}-\mu\_{t}+0.5}{\sigma\_{t}}\middle|\nu\right)-F\left(\frac{y\_{t}-\mu\_{t}-0.5}{\sigma\_{t}}\middle|\nu\right)\right). |  | (4) |

Maximizing this function leads to meaningful results, as the discreteness of the data is properly addressed.

We now turn to the specification of our proposed GARCH-like model. We base our model on the score-driven model ([2](https://arxiv.org/html/2510.09785v1#S3.E2 "In 3 Unsuitability of Continuous Models")), but modify it in several ways, similarly to Holý ([2024](https://arxiv.org/html/2510.09785v1#bib.bib20)). The location parameter is made time-varying and follows a first-order moving average process with a long-term value of zero, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=θ​(yt−1−μt−1).\mu\_{t}=\theta(y\_{t-1}-\mu\_{t-1}). |  | (5) |

This process captures the market microstructure noise, which occurs at higher frequencies; see, e.g., Hansen and Lunde ([2006](https://arxiv.org/html/2510.09785v1#bib.bib19)) for more details. Along with the empirical evidence for higher frequencies, the intercept is not included.

The scale parameter exhibits diurnal patterns of increased volatility after the market opens and, to a lesser degree, before the market closes. This pattern is estimated using smoothing splines applied to squared price changes and is incorporated into the variable sts\_{t}, which is then included in the equation for σt2\sigma^{2}\_{t}. The dynamics are captured in a separate component ete\_{t} to ensure that the autoregressive part omits the lagged value st−1s\_{t-1}. Separating ω\omega and φ\varphi also accelerates the convergence of the numerical optimization. The scale parameter then follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡σt2=ω+ln⁡s^t+et,et=α​∇ln⁡σ2(yt−1;μt−1,σt−12,ν)+φ​et−1.\ln\sigma^{2}\_{t}=\omega+\ln\hat{s}\_{t}+e\_{t},\qquad e\_{t}=\alpha\nabla\_{\ln\sigma^{2}}\left(y\_{t-1};\mu\_{t-1},\sigma^{2}\_{t-1},\nu\right)+\varphi e\_{t-1}. |  | (6) |

The score accounts for the interval structure, just as the interval log-likelihood ([4](https://arxiv.org/html/2510.09785v1#S4.E4 "In 4 Integer Model and Interval Maximum Likelihood Estimation")), and takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇ln⁡σ2(y;μ,σ2,ν)=(y−μ−0.5)f(y−μ−0.5σ|ν)−(y−μ+0.5)f(y−μ+0.5σ|ν)2σF(y−μ+0.5σ|ν)−2σF(y−μ−0.5σ|ν),\nabla\_{\ln\sigma^{2}}\left(y;\mu,\sigma^{2},\nu\right)=\frac{\left(y-\mu-0.5\right)f\left(\frac{y-\mu-0.5}{\sigma}\middle|\nu\right)-\left(y-\mu+0.5\right)f\left(\frac{y-\mu+0.5}{\sigma}\middle|\nu\right)}{2\sigma F\left(\frac{y-\mu+0.5}{\sigma}\middle|\nu\right)-2\sigma F\left(\frac{y-\mu-0.5}{\sigma}\middle|\nu\right)}, |  | (7) |

where f(⋅|ν)f(\cdot|\nu) denotes the density function of the Student’s t-distribution.

## 5 Performance of Integer Models

We estimate the proposed model using 1-second and 1-minute frequency data. We compare it with three models that have equivalent dynamics but different distributions: the normal distribution with our interval-based estimation approach, the discrete Skellam distribution, and its zero-inflated version with an additional zero-inflation parameter π\pi. For the Skellam distributions, we model the time-varying overdispersion parameter as proposed by Holý ([2024](https://arxiv.org/html/2510.09785v1#bib.bib20)).

The results are reported in Table [2](https://arxiv.org/html/2510.09785v1#S5.T2 "Table 2 ‣ 5 Performance of Integer Models"). Note that the reported log-likelihood ℓ\ell is based on probability mass functions, in contrast to the density functions in Table [1](https://arxiv.org/html/2510.09785v1#S3.T1 "Table 1 ‣ 3 Unsuitability of Continuous Models"). We observe that for the 1-second frequency, the zero-inflated Skellam model performs best, while for the 1-minute frequency, the integer Student’s t-model provides a better fit. Figure [3](https://arxiv.org/html/2510.09785v1#S5.F3 "Figure 3 ‣ 5 Performance of Integer Models") shows that the Student’s t-distribution is not flexible enough to capture price changes in 1-second frequency data, with the probabilities of -1 and 1 being overestimated and the remaining probabilities being underestimated. For 1-minute frequency, there does not appear to be a systematic bias, although the probability of 0 is underestimated.

To detect the presence of ARCH effects in the residuals, Table [2](https://arxiv.org/html/2510.09785v1#S5.T2 "Table 2 ‣ 5 Performance of Integer Models") also reports the R2 statistic from the ARCH-LM test of Engle ([1982](https://arxiv.org/html/2510.09785v1#bib.bib14)), with the maximum lag set to 10. For all models, autocorrelation in squared residuals is quite low, indicating that they capture time-varying volatility well, except for the model based on the Student’s t-distribution with 1 second frequency, for which standardized residuals cannot be obtained because the first and second moments do not exist for most days.

Table 2: The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on various integer distributions.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Normal | t | Skellam | Z-I Sk. | Normal | t | Skellam | Z-I Sk. |
| θ\theta | -0.291 | -0.028 | -0.328 | -0.612 | -0.055 | -0.059 | -0.059 | -0.056 |
| ω\omega | 2.559 | -1.378 | 1.721 | 2.432 | 4.585 | 4.333 | 4.351 | 4.345 |
| α\alpha | 0.040 | 0.084 | 0.045 | 0.074 | 0.083 | 0.113 | 0.043 | 0.042 |
| φ\varphi | 0.977 | 0.998 | 0.995 | 0.994 | 0.892 | 0.915 | 0.990 | 0.991 |
| ν\nu |  | 0.908 |  |  |  | 9.268 |  |  |
| π\pi |  |  |  | 0.492 |  |  |  | 0.011 |
| AA | 0.004 | x | 0.001 | 0.001 | 0.018 | 0.019 | 0.021 | 0.022 |
| ℓ\ell | -2.228 | -1.841 | -2.068 | -1.700 | -3.565 | -3.550 | -3.566 | -3.557 |
| AFA\_{\text{F}} | x | x | 0.002 | 0.001 | 0.024 | 0.026 | 0.025 | 0.026 |
| ℓF\ell\_{\text{F}} | x | -1.844 | -2.144 | -1.787 | -3.644 | -3.629 | -3.779 | -3.903 |

Notes:
θ\theta – moving-average coefficient; ω\omega – intercept in the volatility equation; α\alpha – score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; π\pi – zero inflation; AA, AFA\_{\text{F}} – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell, ℓF\ell\_{\text{F}} – average log-likelihood; AFA\_{\text{F}}, ℓF\ell\_{\text{F}} are evaluated on the data from the next day.

![Refer to caption](x3.png)


Figure 3: The average difference between the observed distribution of price changes and the fitted probabilities from the daily integer models based on the Student’s t-distribution.

Finally, we assess out-of-sample performance. For this purpose, we evaluate the daily models on the day following their estimation. For the Student’s t, Skellam, and zero-inflated Skellam distributions, Table [2](https://arxiv.org/html/2510.09785v1#S5.T2 "Table 2 ‣ 5 Performance of Integer Models") shows that the out-of-sample log-likelihoods are only slightly worse than their in-sample counterparts, suggesting stable behavior on a day-to-day basis. The normal distribution at 1-second frequency, however, fails to capture out-of-sample outliers on 56 percent of days, resulting in numerically zero likelihood, and is therefore unsuitable for forecasting studies. Overall, the out-of-sample results confirm the zero-inflated Skellam model as the most suitable for the 1-second frequency, and the Student’s t-distribution for the 1-minute frequency.

## 6 Conclusion

The Student’s t-distribution is unsuitable for modeling high-frequency integer price changes, as its density function degenerates into a ⟂\perp-shaped form concentrated at 0 with extremely heavy tails, providing no useful information about the data. However, we show that maximum likelihood estimation can be modified to treat these integer observations as being produced by rounding and replace them with corresponding intervals. The score-driven model with dynamic volatility based on the Student’s t-distribution, estimated using this interval approach, produces meaningful results comparable to dynamic models based on the Skellam distribution, which have been proposed in the recent literature. Our empirical analysis shows that the Student’s t-distribution is suitable for relatively lower frequencies, such as 1-minute data, but is insufficient to capture the distribution of price changes at relatively higher frequencies. However, our interval approach is in no way restricted to the Student’s t-distribution and can be applied to any continuous distribution. This opens up possibilities for future research to consider not only discrete distributions but also continuous distributions for modeling high-frequency prices.

## Funding

The work on this paper was supported by the Czech Science Foundation under project 23-06139S and the personal and professional development support program of the Faculty of Informatics and Statistics, Prague University of Economics and Business.

## References

* Alomani *et al.* (2018)

  Alomani GA, Alzaid AA, Omair MA (2018).
  “A Skellam GARCH model.”
  *Brazilian Journal of Probability and Statistics*,
  32(1), 200–214.
  ISSN 0103-0752.
  <https://doi.org/10.1214/16-bjps338>.
* Ardia *et al.* (2019)

  Ardia D, Boudt K, Catania L (2019).
  “Generalized Autoregressive Score Models in R: The GAS
  Package.”
  *Journal of Statistical Software*, 88(6), 1–28.
  ISSN 1548-7660.
  <https://doi.org/10.18637/jss.v088.i06>.
* Barndorff-Nielsen *et al.* (2009)

  Barndorff-Nielsen OE, Hansen PR, Lunde A, Shephard N (2009).
  “Realized Kernels in Practice: Trades and Quotes.”
  *Econometrics Journal*, 12(3), 1–32.
  ISSN 1368-4221.
  <https://doi.org/10.1111/j.1368-423X.2008.00275.x>.
* Blasques *et al.* (2024)

  Blasques F, Holý V, Tomanová P (2024).
  “Zero-Inflated Autoregressive Conditional Duration Model for
  Discrete Trade Durations with Excessive Zeros.”
  *Studies in Nonlinear Dynamics and Econometrics*,
  28(5), 673–702.
  ISSN 1558-3708.
  <https://doi.org/10.1515/snde-2022-0008>.
* Blasques *et al.* (2015)

  Blasques F, Koopman SJ, Lucas A (2015).
  “Information-Theoretic Optimality of Observation-Driven Time
  Series Models for Continuous Responses.”
  *Biometrika*, 102(2), 325–343.
  ISSN 0006-3444.
  <https://doi.org/10.1093/biomet/asu076>.
* Blazsek and Licht (2020)

  Blazsek S, Licht A (2020).
  “Dynamic Conditional Score Models: A Review of Their
  Applications.”
  *Applied Economics*, 52(11), 1181–1199.
  ISSN 0003-6846.
  <https://doi.org/10.1080/00036846.2019.1659498>.
* Bollerslev (1986)

  Bollerslev T (1986).
  “Generalized Autoregressive Conditional Heteroskedasticity.”
  *Journal of Econometrics*, 31(3), 307–327.
  ISSN 0304-4076.
  <https://doi.org/10.1016/0304-4076(86)90063-1>.
* Bollerslev (1987)

  Bollerslev T (1987).
  “A Conditionally Heteroskedastic Time Series Model for
  Speculative Prices and Rates of Return.”
  *Review of Economics and Statistics*, 69(3), 542–547.
  ISSN 0034-6535.
  <https://doi.org/10.2307/1925546>.
* Catania *et al.* (2022)

  Catania L, Di Mari R, Santucci de Magistris P (2022).
  “Dynamic Discrete Mixtures for High-Frequency Prices.”
  *Journal of Business & Economic Statistics*, 40(2),
  559–577.
  ISSN 0735-0015.
  <https://doi.org/10.1080/07350015.2020.1840994>.
* Creal *et al.* (2013)

  Creal D, Koopman SJ, Lucas A (2013).
  “Generalized Autoregressive Score Models with Applications.”
  *Journal of Applied Econometrics*, 28(5), 777–795.
  ISSN 0883-7252.
  <https://doi.org/10.1002/jae.1279>.
* Cui *et al.* (2021)

  Cui Y, Li Q, Zhu F (2021).
  “Modeling Z-Valued Time Series Based on New Versions of the
  Skellam INGARCH Model.”
  *Brazilian Journal of Probability and Statistics*,
  35(2), 293–314.
  ISSN 0103-0752.
  <https://doi.org/10.1214/20-bjps473>.
* Doukhan *et al.* (2021)

  Doukhan P, Khan NM, Neumann MH (2021).
  “Mixing Properties of Integer-Valued GARCH Processes.”
  *Alea - Latin American Journal of Probability and Mathematical
  Statistics*, 18(1), 401–420.
  ISSN 1980-0436.
  <https://doi.org/10.30757/alea.v18-18>.
* Engle (2002)

  Engle R (2002).
  “New Frontiers for ARCH Models.”
  *Journal of Applied Econometrics*, 17(5), 425–446.
  ISSN 0883-7252.
  <https://doi.org/10.1002/jae.683>.
* Engle (1982)

  Engle RF (1982).
  “Autoregressive Conditional Heteroscedasticity with Estimates
  of the Variance of United Kingdom Inflation.”
  *Econometrica*, 50(4), 987–1007.
  ISSN 0012-9682.
  <https://doi.org/10.2307/1912773>.
* Engle (2000)

  Engle RF (2000).
  “The Econometrics of Ultra-High-Frequency Data.”
  *Econometrica*, 68(1), 1–22.
  ISSN 0012-9682.
  <https://doi.org/10.1111/1468-0262.00091>.
* Ghalanos (2024)

  Ghalanos A (2024).
  “Package ’rugarch’.”
* Ghysels and Jasiak (1998)

  Ghysels E, Jasiak J (1998).
  “GARCH for Irregularly Spaced Financial Data: The ACD-GARCH
  Model.”
  *Studies in Nonlinear Dynamics and Econometrics*, 2(4),
  133–149.
  ISSN 1081-1826.
  <https://doi.org/10.2202/1558-3708.1035>.
* Gonçalves and Mendes-Lopes (2020)

  Gonçalves E, Mendes-Lopes N (2020).
  “Signed Compound Poisson Integer-Valued GARCH Processes.”
  *Communications in Statistics - Theory and Methods*,
  49(22), 5468–5492.
  ISSN 0361-0926.
  <https://doi.org/10.1080/03610926.2019.1619767>.
* Hansen and Lunde (2006)

  Hansen PR, Lunde A (2006).
  “Realized Variance and Market Microstructure Noise.”
  *Journal of Business & Economic Statistics*, 24(2),
  127–161.
  ISSN 0735-0015.
  <https://doi.org/10.1198/073500106000000071>.
* Holý (2024)

  Holý V (2024).
  “An Intraday GARCH Model for Discrete Price Changes and
  Irregularly Spaced Observations.”
  *Annals of Operations Research*.
  ISSN 0254-5330.
  <https://doi.org/10.1007/s10479-024-06205-z>.
* Holý (2025)

  Holý V (2025).
  “Package ’gasmodel’.”
* Koopman *et al.* (2017)

  Koopman SJ, Lit R, Lucas A (2017).
  “Intraday Stochastic Volatility in Discrete Price Changes:
  The Dynamic Skellam Model.”
  *Journal of the American Statistical Association*,
  112(520), 1490–1503.
  ISSN 0162-1459.
  <https://doi.org/10.1080/01621459.2017.1302878>.
* Koopman *et al.* (2018)

  Koopman SJ, Lit R, Lucas A, Opschoor A (2018).
  “Dynamic Discrete Copula Models for High-Frequency Stock
  Price Changes.”
  *Journal of Applied Econometrics*, 33(7), 966–985.
  ISSN 0883-7252.
  <https://doi.org/10.1002/jae.2645>.
* Liu and Maheu (2012)

  Liu C, Maheu JM (2012).
  “Intraday Dynamics of Volatility and Duration: Evidence from
  Chinese Stocks.”
  *Pacific-Basin Finance Journal*, 20(3), 329–348.
  ISSN 0927-538X.
  <https://doi.org/10.1016/j.pacfin.2011.11.001>.
* Meddahi *et al.* (2006)

  Meddahi N, Renault E, Werker B (2006).
  “GARCH and Irregularly Spaced Data.”
  *Economics Letters*, 90(2), 200–204.
  ISSN 0165-1765.
  <https://doi.org/10.1016/j.econlet.2005.07.027>.
* Nelson (1991)

  Nelson DB (1991).
  “Conditional Heteroskedasticity in Asset Returns: A New
  Approach.”
  *Econometrica*, 59(2), 347.
  ISSN 0012-9682.
  <https://doi.org/10.2307/2938260>.
* Wuertz *et al.* (2024)

  Wuertz D, Chalabi Y, Setz T, Maechler M, Boshnakov GN (2024).
  “Package ’fGarch’.”

## Appendix A Evidence from Further Stocks

To provide more general insights, we further analyze the MCD, CSCO, and MSFT stocks in addition to the IBM stock. This set of four stocks has also been analyzed, for example, by Blasques *et al.* ([2024](https://arxiv.org/html/2510.09785v1#bib.bib4)). All four stocks are components of the Dow Jones Industrial Average (DJIA). The main results regarding the degenerative behavior of the Student’s t-distribution observed for the IBM stock are also found for these three stocks. Similarly, we also observe limitations of some models in forecasting. We present the results in Figures [4](https://arxiv.org/html/2510.09785v1#A1.F4 "Figure 4 ‣ Appendix A Evidence from Further Stocks")–[12](https://arxiv.org/html/2510.09785v1#A1.F12 "Figure 12 ‣ Appendix A Evidence from Further Stocks") and Tables [3](https://arxiv.org/html/2510.09785v1#A1.T3 "Table 3 ‣ Appendix A Evidence from Further Stocks")–[8](https://arxiv.org/html/2510.09785v1#A1.T8 "Table 8 ‣ Appendix A Evidence from Further Stocks"), and discuss differences in behavior from the IBM stock below.

First, we focus on the MCD stock of McDonald’s Corporation traded on the NYSE. The number of tick observations after data cleaning is quite similar to that of IBM, with over 15 million observations. Figures [4](https://arxiv.org/html/2510.09785v1#A1.F4 "Figure 4 ‣ Appendix A Evidence from Further Stocks")–[6](https://arxiv.org/html/2510.09785v1#A1.F6 "Figure 6 ‣ Appendix A Evidence from Further Stocks") and Table [3](https://arxiv.org/html/2510.09785v1#A1.T3 "Table 3 ‣ Appendix A Evidence from Further Stocks") correspond to Figures [1](https://arxiv.org/html/2510.09785v1#S2.F1 "Figure 1 ‣ 2 Data and Modeling Strategy")–[3](https://arxiv.org/html/2510.09785v1#S5.F3 "Figure 3 ‣ 5 Performance of Integer Models") and Table [1](https://arxiv.org/html/2510.09785v1#S3.T1 "Table 1 ‣ 3 Unsuitability of Continuous Models"). In Table [4](https://arxiv.org/html/2510.09785v1#A1.T4 "Table 4 ‣ Appendix A Evidence from Further Stocks"), there is one notable difference: for the 1-minute frequency, the score coefficient is estimated as negative on most days for the normal distribution. These negative values lack a clear interpretation and are a product of overfitting, as evidenced by the out-of-sample analysis, where the model performs quite poorly.

Second, we analyze the CSCO stock of Cisco Systems, Inc., traded on the NASDAQ. The number of tick observations is almost 27 million. There is a much larger occurrence of zero values than for the IBM stock, as illustrated in Figure [7](https://arxiv.org/html/2510.09785v1#A1.F7 "Figure 7 ‣ Appendix A Evidence from Further Stocks"). Figure [8](https://arxiv.org/html/2510.09785v1#A1.F8 "Figure 8 ‣ Appendix A Evidence from Further Stocks") and Table [5](https://arxiv.org/html/2510.09785v1#A1.T5 "Table 5 ‣ Appendix A Evidence from Further Stocks") correspond to Figure [2](https://arxiv.org/html/2510.09785v1#S3.F2 "Figure 2 ‣ 3 Unsuitability of Continuous Models") and Table [1](https://arxiv.org/html/2510.09785v1#S3.T1 "Table 1 ‣ 3 Unsuitability of Continuous Models"). Table [6](https://arxiv.org/html/2510.09785v1#A1.T6 "Table 6 ‣ Appendix A Evidence from Further Stocks") shows that the estimated degrees of freedom of the Student’s t-distribution at the 1-second frequency are larger than for the IBM stock. Similar to the MCD stock, negative values of the score coefficient occur at the 1-minute frequency for the normal, Skellam, and zero-inflated Skellam distributions. The Student’s t-distribution maintains positive values but exhibits a slightly worse in-sample fit and a dramatically better out-of-sample fit. This suggests that it could be practical to impose a lower bound of zero on the score coefficient. Figure [9](https://arxiv.org/html/2510.09785v1#A1.F9 "Figure 9 ‣ Appendix A Evidence from Further Stocks") shows systematic biases at both the 1-second and 1-minute frequencies.

Third, we analyze the MSFT stock of Microsoft Corporation traded on the NASDAQ. The number of tick observations is the highest among the studied stocks, with about 90 million observations. The distributions in Figure [10](https://arxiv.org/html/2510.09785v1#A1.F10 "Figure 10 ‣ Appendix A Evidence from Further Stocks") are more spread out than those for the IBM stock. Consequently, Table [7](https://arxiv.org/html/2510.09785v1#A1.T7 "Table 7 ‣ Appendix A Evidence from Further Stocks") reports more stable results across the four R packages, with degrees of freedom estimated above 4 by all packages for the 1-second frequency. Nevertheless, these are all suboptimal solutions, as evident from Figure [11](https://arxiv.org/html/2510.09785v1#A1.F11 "Figure 11 ‣ Appendix A Evidence from Further Stocks"). Table [8](https://arxiv.org/html/2510.09785v1#A1.T8 "Table 8 ‣ Appendix A Evidence from Further Stocks") shows that at the 1-second frequency, the Student’s t-distribution performs best. At the 1-minute frequency, it is surpassed by the normal distribution with a negative score coefficient in-sample, but the Student’s t-distribution outperforms out-of-sample. The Skellam distribution, along with its zero-inflated version, is unable to capture out-of-sample values that can be quite spread out on some days, resulting in zero likelihood. Figure [12](https://arxiv.org/html/2510.09785v1#A1.F12 "Figure 12 ‣ Appendix A Evidence from Further Stocks") is consistent with Figure [3](https://arxiv.org/html/2510.09785v1#S5.F3 "Figure 3 ‣ 5 Performance of Integer Models").

![Refer to caption](x4.png)


Figure 4: The MCD stock – The distribution of price changes with the fitted density of the Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters.




Table 3: The MCD stock – The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on the Student’s t-distribution, estimated using various R packages.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | `rugarch` | `fGarch` | `GAS` | `gasmodel` | `rugarch` | `fGarch` | `GAS` | `gasmodel` |
| μ\mu | 0.002 | 0.002 | 0.003 | -0.000 | 0.097 | 0.085 | 0.089 | 0.088 |
| ω\omega | 0.556 | 0.000 | 0.001 | -0.001 | 3.362 | 3.369 | 0.007 | 0.000 |
| α\alpha | 0.123 | 1.000 | 0.062 | 2.579 | 0.063 | 0.065 | 0.179 | 0.176 |
| φ\varphi | 0.876 | 0.963 | 1.000 | 0.999 | 0.907 | 0.906 | 0.999 | 1.000 |
| ν\nu | 2.213 | 2.015 | 4.000 | 0.201 | 6.150 | 6.103 | 6.981 | 7.007 |
| AA | 0.003 | 0.004 | 0.022 | x | 0.020 | 0.020 | 0.022 | 0.022 |
| ℓ\ell | -2.514 | -2.496 | -2.548 | 41.470 | -3.862 | -3.862 | -3.861 | -3.857 |

Notes:
μ\mu – expected price difference; ω\omega – intercept in the volatility equation; α\alpha – variance/score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; AA – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell – average log-likelihood.

![Refer to caption](x5.png)


Figure 5: The MCD stock – The log-likelihood from the fitted Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters. The dashed line represents the scale parameter at the lower bound, 2−10742^{-1074}, due to numerical precision.




Table 4: The MCD stock – The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on various integer distributions.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Normal | t | Skellam | Z-I Sk. | Normal | t | Skellam | Z-I Sk. |
| θ\theta | -0.467 | -0.014 | -0.481 | -0.721 | -0.073 | -0.067 | -0.075 | -0.073 |
| ω\omega | 3.059 | -1.453 | 2.596 | 2.915 | 5.147 | 4.898 | 4.376 | 4.357 |
| α\alpha | 0.073 | 0.094 | 0.053 | 0.057 | -0.074 | 0.067 | 0.035 | 0.035 |
| φ\varphi | 0.980 | 0.999 | 0.991 | 0.995 | 0.972 | 0.946 | 1.000 | 1.000 |
| ν\nu |  | 0.674 |  |  |  | 9.161 |  |  |
| π\pi |  |  |  | 0.474 |  |  |  | 0.012 |
| AA | 0.003 | x | 0.002 | 0.001 | 0.023 | 0.023 | 0.024 | 0.024 |
| ℓ\ell | -2.668 | -2.344 | -2.570 | -2.044 | -3.821 | -3.821 | -3.870 | -3.860 |
| AFA\_{\text{F}} | x | x | 0.003 | 0.002 | 0.034 | 0.033 | 0.030 | 0.029 |
| ℓF\ell\_{\text{F}} | x | -2.365 | -2.955 | -2.373 | -5.228 | -4.101 | -4.297 | -4.441 |

Notes:
θ\theta – moving-average coefficient; ω\omega – intercept in the volatility equation; α\alpha – score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; π\pi – zero inflation; AA, AFA\_{\text{F}} – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell, ℓF\ell\_{\text{F}} – average log-likelihood; AFA\_{\text{F}}, ℓF\ell\_{\text{F}} are evaluated on the data from the next day.

![Refer to caption](x6.png)


Figure 6: The MCD stock – The average difference between the observed distribution of price changes and the fitted probabilities from the daily integer models based on the Student’s t-distribution.

![Refer to caption](x7.png)


Figure 7: The CSCO stock – The distribution of price changes with the fitted density of the Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters.




Table 5: The CSCO stock – The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on the Student’s t-distribution, estimated using various R packages.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | `rugarch` | `fGarch` | `GAS` | `gasmodel` | `rugarch` | `fGarch` | `GAS` | `gasmodel` |
| μ\mu | -0.000 | 0.000 | 0.000 | -0.000 | 0.002 | 0.000 | 0.005 | 0.000 |
| ω\omega | 0.000 | 0.000 | -0.498 | -0.004 | 0.113 | 0.113 | 0.003 | 0.000 |
| α\alpha | 0.013 | 0.516 | 1.115 | 2.314 | 0.059 | 0.060 | 0.177 | 0.173 |
| φ\varphi | 0.013 | 0.004 | 0.833 | 0.991 | 0.914 | 0.912 | 0.999 | 0.999 |
| ν\nu | 2.103 | 2.000 | 4.000 | 0.296 | 6.122 | 6.065 | 6.393 | 6.373 |
| AA | 0.001 | 0.004 | 0.004 | x | 0.021 | 0.021 | 0.024 | 0.022 |
| ℓ\ell | 1.887 | 1.876 | -0.718 | 45.858 | -2.130 | -2.130 | -2.132 | -2.126 |

Notes:
μ\mu – expected price difference; ω\omega – intercept in the volatility equation; α\alpha – variance/score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; AA – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell – average log-likelihood.

![Refer to caption](x8.png)


Figure 8: The CSCO stock – The log-likelihood from the fitted Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters. The dashed line represents the scale parameter at the lower bound, 2−10742^{-1074}, due to numerical precision.




Table 6: The CSCO stock – The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on various integer distributions.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Normal | t | Skellam | Z-I Sk. | Normal | t | Skellam | Z-I Sk. |
| θ\theta | -0.491 | -0.404 | -0.490 | -0.660 | -0.092 | -0.093 | -0.078 | -0.087 |
| ω\omega | -0.634 | -1.897 | -1.557 | -1.217 | 1.586 | 1.337 | 1.573 | 1.621 |
| α\alpha | 0.127 | 0.494 | 0.038 | 0.073 | -0.034 | 0.034 | -0.120 | -0.098 |
| φ\varphi | 0.953 | 0.736 | 0.994 | 0.992 | 0.981 | 0.963 | 0.982 | 0.988 |
| ν\nu |  | 3.717 |  |  |  | 8.505 |  |  |
| π\pi |  |  |  | 0.290 |  |  |  | 0.032 |
| AA | 0.004 | 0.005 | 0.002 | 0.001 | 0.024 | 0.024 | 0.024 | 0.024 |
| ℓ\ell | -0.962 | -0.840 | -0.841 | -0.830 | -2.093 | -2.093 | -2.086 | -2.082 |
| AFA\_{\text{F}} | x | 0.006 | 0.002 | 0.001 | 0.037 | 0.035 | 0.035 | 0.032 |
| ℓF\ell\_{\text{F}} | x | -0.843 | -0.843 | -0.831 | -3.323 | -2.360 | -4.956 | -5.506 |

Notes:
θ\theta – moving-average coefficient; ω\omega – intercept in the volatility equation; α\alpha – score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; π\pi – zero inflation; AA, AFA\_{\text{F}} – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell, ℓF\ell\_{\text{F}} – average log-likelihood; AFA\_{\text{F}}, ℓF\ell\_{\text{F}} are evaluated on the data from the next day.

![Refer to caption](x9.png)


Figure 9: The CSCO stock – The average difference between the observed distribution of price changes and the fitted probabilities from the daily integer models based on the Student’s t-distribution.

![Refer to caption](x10.png)


Figure 10: The MSFT stock – The distribution of price changes with the fitted density of the Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters.




Table 7: The MSFT stock – The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on the Student’s t-distribution, estimated using various R packages.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | `rugarch` | `fGarch` | `GAS` | `gasmodel` | `rugarch` | `fGarch` | `GAS` | `gasmodel` |
| μ\mu | 0.014 | 0.012 | 0.012 | 0.012 | 0.209 | 0.210 | 0.185 | 0.183 |
| ω\omega | 0.178 | 0.540 | 0.010 | 0.000 | 6.751 | 6.802 | 0.010 | 0.000 |
| α\alpha | 0.070 | 0.118 | 0.110 | 0.102 | 0.068 | 0.072 | 0.188 | 0.185 |
| φ\varphi | 0.916 | 0.860 | 0.995 | 0.996 | 0.909 | 0.908 | 0.999 | 0.999 |
| ν\nu | 4.334 | 4.298 | 4.268 | 4.299 | 7.080 | 6.988 | 8.176 | 8.174 |
| AA | 0.008 | 0.005 | 0.082 | 0.082 | 0.020 | 0.020 | 0.024 | 0.022 |
| ℓ\ell | -2.673 | -2.672 | -2.671 | -2.671 | -4.256 | -4.256 | -4.257 | -4.257 |

Notes:
μ\mu – expected price difference; ω\omega – intercept in the volatility equation; α\alpha – variance/score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; AA – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell – average log-likelihood.

![Refer to caption](x11.png)


Figure 11: The MSFT stock – The log-likelihood from the fitted Student’s t-distribution, using various fixed degrees of freedom and estimated scale parameters. The dashed line represents the scale parameter at the lower bound, 2−10742^{-1074}, due to numerical precision.




Table 8: The MSFT stock – The median estimated parameters, the ARCH-LM statistic, and the fitted log-likelihood from daily models based on various integer distributions.

|  | 1 Second Frequency | | | | 1 Minute Frequency | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Normal | t | Skellam | Z-I Sk. | Normal | t | Skellam | Z-I Sk. |
| θ\theta | -0.396 | -0.330 | -0.361 | -0.384 | -0.026 | -0.027 | -0.013 | -0.013 |
| ω\omega | 3.393 | 2.109 | 2.559 | 2.640 | 5.999 | 5.816 | 4.320 | 4.320 |
| α\alpha | 0.086 | 0.254 | 0.060 | 0.060 | -0.072 | 0.038 | 0.028 | 0.028 |
| φ\varphi | 0.972 | 0.927 | 0.985 | 0.985 | 0.984 | 0.969 | 0.999 | 0.999 |
| ν\nu |  | 4.605 |  |  |  | 10.700 |  |  |
| π\pi |  |  |  | 0.080 |  |  |  | 0.001 |
| AA | 0.005 | 0.013 | 0.004 | 0.003 | 0.023 | 0.023 | 0.036 | 0.037 |
| ℓ\ell | -2.774 | -2.618 | -2.672 | -2.642 | -4.224 | -4.228 | -4.352 | -4.352 |
| AFA\_{\text{F}} | x | 0.014 | 0.006 | 0.004 | 0.048 | 0.041 | x | x |
| ℓF\ell\_{\text{F}} | x | -2.628 | -2.837 | -2.813 | -6.529 | -4.710 | x | x |

Notes:
θ\theta – moving-average coefficient; ω\omega – intercept in the volatility equation; α\alpha – score coefficient; φ\varphi – autoregressive coefficient; ν\nu – degrees of freedom; π\pi – zero inflation; AA, AFA\_{\text{F}} – R2 statistic of the ARCH-LM test with lag 10; ℓ\ell, ℓF\ell\_{\text{F}} – average log-likelihood; AFA\_{\text{F}}, ℓF\ell\_{\text{F}} are evaluated on the data from the next day.

![Refer to caption](x12.png)


Figure 12: The MSFT stock – The average difference between the observed distribution of price changes and the fitted probabilities from the daily integer models based on the Student’s t-distribution.