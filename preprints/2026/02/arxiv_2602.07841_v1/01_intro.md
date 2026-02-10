---
authors:
- Cheng Zhang
doc_id: arxiv:2602.07841v1
family_id: arxiv:2602.07841
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: "A Quadratic Link between Out-of-Sample \U0001D445² and Directional Accuracy"
url_abs: http://arxiv.org/abs/2602.07841v1
url_html: https://arxiv.org/html/2602.07841v1
venue: arXiv q-fin
version: 1
year: 2026
---


\nameCheng Zhang
CONTACT Cheng Zhang. Email: zhangcheng01@hbpu.edu.cn; ORCID: https://orcid.org/0000-0002-4150-3371

###### Abstract

This study provides a novel perspective on the metric disconnect phenomenon in financial time series forecasting through an analytical link that reconciles the out-of-sample R2R^{2} (ROOS2R^{2}\_{\text{OOS}}) and directional accuracy (DA). In particular, using the random walk model as a baseline and assuming that sign correctness is independent of realized magnitude, we show that these two metrics exhibit a quadratic relationship for MSE-optimal point forecasts. For point forecasts with modest DA, the theoretical value of ROOS2R^{2}\_{\text{OOS}} is intrinsically negligible. Thus, a negative empirical ROOS2R^{2}\_{\text{OOS}} is expected if the model is suboptimal or affected by finite sample noise.

Word Count: [2200]

###### keywords:

Point Forecasting; Out-of-Sample R2R^{2}; Directional Accuracy; Metric Disconnect

{jelcode}

C52; C53; G17

## 1 Introduction

In financial time series forecasting, the metric disconnect is a persistent phenomenon. Since the seminal work of Meese and Rogoff ([1983](https://arxiv.org/html/2602.07841v1#bib.bib10)), researchers have reported that predictive models generally cannot outperform the random walk baseline when evaluated by the mean squared error (MSE) or root mean squared error (RMSE) (Kilian and Taylor, [2003](https://arxiv.org/html/2602.07841v1#bib.bib8); Moosa, [2013](https://arxiv.org/html/2602.07841v1#bib.bib11); Petropoulos et al., [2022](https://arxiv.org/html/2602.07841v1#bib.bib12); Ellwanger and Snudden, [2023](https://arxiv.org/html/2602.07841v1#bib.bib3); Hewamalage et al., [2023](https://arxiv.org/html/2602.07841v1#bib.bib7); Zeng et al., [2023](https://arxiv.org/html/2602.07841v1#bib.bib15); Beck et al., [2025](https://arxiv.org/html/2602.07841v1#bib.bib1)). Complex models often yield negligible out-of-sample R2R^{2} (ROOS2R^{2}\_{\text{OOS}}) values, because of not only a generally low signal-to-noise ratio in the data (Welch and Goyal, [2008](https://arxiv.org/html/2602.07841v1#bib.bib14); Gu et al., [2020](https://arxiv.org/html/2602.07841v1#bib.bib5)), but also the transient nature of financial predictability, which inherently suppresses model performance (Farmer et al., [2023](https://arxiv.org/html/2602.07841v1#bib.bib4)).

In contrast, although models may perform poorly under magnitude-based metrics, they can still exhibit significant predictive power in terms of directional accuracy (DA) (Leitch and Tanner, [1991](https://arxiv.org/html/2602.07841v1#bib.bib9)). The direction of change is considered predictable even when the point value itself is not (Taylor, [2008](https://arxiv.org/html/2602.07841v1#bib.bib13); Hamilton, [2020](https://arxiv.org/html/2602.07841v1#bib.bib6)). Depending on the complexity of the markets and availability of data, the DA in financial time series forecasting typically ranges between 0.55 and 0.60 (Bustos and Pomares-Quimbaya, [2020](https://arxiv.org/html/2602.07841v1#bib.bib2)). Therefore, the evaluation of point forecasts in finance often results in poor error measures accompanied by modest DAs.

While prior studies provide empirical evidence and explanations of the metric disconnect in forecasting, a consensus on this phenomenon is that there is no inherent connection between these divergent metrics. In this study, we offer a different perspective. We posit that with the random walk model as the baseline and the assumption that the sign correctness is independent of the realized magnitude, the ROOS2R^{2}\_{\text{OOS}} of MSE-optimal point forecasts can be expressed as a quadratic function of the DA. Therefore, empirically, a modest DA corresponds to only a low theoretical value of ROOS2R^{2}\_{\text{OOS}}, and the realized value of ROOS2R^{2}\_{\text{OOS}} is expected to be negative when the model is suboptimal or affected by sampling noise, which means that the sign correctness and realized magnitude exhibit a negative sample correlation.

## 2 The Analytical Link

Consider a univariate time series yty\_{t}. The objective is to forecast the return Δ​yt=yt−yt−1\Delta y\_{t}=y\_{t}-y\_{t-1} given the information set Ωt−1\Omega\_{t-1}. Under the MSE loss function, the optimal point forecast μt\mu\_{t} is given by the conditional expectation of the future return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=𝔼​[Δ​yt∣Ωt−1].\mu\_{t}=\mathbb{E}[\Delta y\_{t}\mid\Omega\_{t-1}]. |  | (1) |

### 2.1 Point Forecast Decomposition

By definition, the realized return can be decomposed into its sign component St∈{−1,1}S\_{t}\in\{-1,1\} and its magnitude component Mt=|Δ​yt|M\_{t}=|\Delta y\_{t}|. Accordingly, the forecast is expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=𝔼​[St⋅Mt∣Ωt−1].\mu\_{t}=\mathbb{E}[S\_{t}\cdot M\_{t}\mid\Omega\_{t-1}]. |  | (2) |

Let D^t∈{−1,1}\hat{D}\_{t}\in\{-1,1\} denote the sign of the point forecast. We define the indicator of directional correctness as ItI\_{t}, where ItI\_{t} equals 1 if the forecast sign matches the realized sign and 0 otherwise. Therefore, StS\_{t} can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=D^t​(2​It−1),S\_{t}=\hat{D}\_{t}(2I\_{t}-1), |  | (3) |

and μt\mu\_{t} can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=𝔼​[D^t​(2​It−1)⋅Mt∣Ωt−1].\mu\_{t}=\mathbb{E}[\hat{D}\_{t}(2I\_{t}-1)\cdot M\_{t}\mid\Omega\_{t-1}]. |  | (4) |

To further decompose μt\mu\_{t}, we make the following assumptions:

###### Assumption 1.

ItI\_{t} is independent of MtM\_{t} given the information set Ωt−1\Omega\_{t-1}.

Assumption [1](https://arxiv.org/html/2602.07841v1#Thmassumption1 "Assumption 1. ‣ 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") implies that the model’s directional skill decouples from the volatility dynamics. Under this orthogonality, the sequence of {It}\{I\_{t}\} is statistically indistinguishable from an independent Bernoulli process. We therefore characterize the model’s directional skill by the probability pp:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[It∣Ωt−1]≡p,\mathbb{E}[I\_{t}\mid\Omega\_{t-1}]\equiv p, |  | (5) |

where p∈[0.5,1]p\in[0.5,1] represents the expected DA over the evaluation horizon.

###### Assumption 2.

The magnitude MtM\_{t} is decomposed into a conditional volatility component and a stochastic innovation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mt=σt​zt,M\_{t}=\sigma\_{t}z\_{t}, |  | (6) |

where σt\sigma\_{t} is the conditional volatility, which is Ωt−1\Omega\_{t-1}-measurable. The innovation ztz\_{t} is a stationary and ergodic process with unit mean and finite variance, and is assumed to be independent of the information set Ωt−1\Omega\_{t-1} (and thus independent of σt\sigma\_{t}).

Based on Assumptions [1](https://arxiv.org/html/2602.07841v1#Thmassumption1 "Assumption 1. ‣ 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") and [2](https://arxiv.org/html/2602.07841v1#Thmassumption2 "Assumption 2. ‣ 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy"), the MSE-optimal point forecast can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=D^t⋅(2​p−1)⋅σt​𝔼​[|zt|].\mu\_{t}=\hat{D}\_{t}\cdot(2p-1)\cdot\sigma\_{t}\mathbb{E}[|z\_{t}|]. |  | (7) |

### 2.2 The Out-of-Sample R2R^{2} Expression

We evaluate the MSE-optimal forecasts via ROOS2R^{2}\_{\text{OOS}}, with the zero-drift random walk model serving as the baseline. As the out-of-sample size increases to infinity, ROOS2R^{2}\_{\text{OOS}} converges to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ROOS2]=1−𝔼​[(Δ​yt−μt)2]𝔼​[(Δ​yt)2].\mathbb{E}[R^{2}\_{\text{OOS}}]=1-\frac{\mathbb{E}[(\Delta y\_{t}-\mu\_{t})^{2}]}{\mathbb{E}[(\Delta y\_{t})^{2}]}. |  | (8) |

For MSE-optimal point forecasts, the forecast error is orthogonal to the forecast itself. This orthogonality allows for the decomposition of the return variance into the variance of the forecast and the variance of the error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(Δ​yt)2]=𝔼​[μt2]+𝔼​[(Δ​yt−μt)2].\mathbb{E}[(\Delta y\_{t})^{2}]=\mathbb{E}[\mu\_{t}^{2}]+\mathbb{E}[(\Delta y\_{t}-\mu\_{t})^{2}]. |  | (9) |

By substituting Equation [9](https://arxiv.org/html/2602.07841v1#S2.E9 "In 2.2 The Out-of-Sample 𝑅² Expression ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") back into Equation [8](https://arxiv.org/html/2602.07841v1#S2.E8 "In 2.2 The Out-of-Sample 𝑅² Expression ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy"), 𝔼​[ROOS2]\mathbb{E}[R^{2}\_{\text{OOS}}] simplifies to the ratio of the forecast variance to the total realized variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ROOS2]=𝔼​[μt2]𝔼​[(Δ​yt)2].\mathbb{E}[R^{2}\_{\text{OOS}}]=\frac{\mathbb{E}[\mu\_{t}^{2}]}{\mathbb{E}[(\Delta y\_{t})^{2}]}. |  | (10) |

According to Equation [7](https://arxiv.org/html/2602.07841v1#S2.E7 "In 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy"), the squared forecast expectation is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[μt2]=(2​p−1)2​𝔼​[σt2]​(𝔼​[|zt|])2.\mathbb{E}[\mu\_{t}^{2}]=(2p-1)^{2}\mathbb{E}[\sigma\_{t}^{2}](\mathbb{E}[|z\_{t}|])^{2}. |  | (11) |

Based on Assumption [2](https://arxiv.org/html/2602.07841v1#Thmassumption2 "Assumption 2. ‣ 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy"), the total variance of the return is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(Δ​yt)2]=𝔼​[σt2​zt2]=𝔼​[σt2]​𝔼​[zt2].\mathbb{E}[(\Delta y\_{t})^{2}]=\mathbb{E}[\sigma\_{t}^{2}z\_{t}^{2}]=\mathbb{E}[\sigma\_{t}^{2}]\mathbb{E}[z\_{t}^{2}]. |  | (12) |

Substituting Equations [11](https://arxiv.org/html/2602.07841v1#S2.E11 "In 2.2 The Out-of-Sample 𝑅² Expression ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") and [12](https://arxiv.org/html/2602.07841v1#S2.E12 "In 2.2 The Out-of-Sample 𝑅² Expression ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") back into Equation [10](https://arxiv.org/html/2602.07841v1#S2.E10 "In 2.2 The Out-of-Sample 𝑅² Expression ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy"), we have the following proposition.

###### Proposition 1.

Under Assumptions [1](https://arxiv.org/html/2602.07841v1#Thmassumption1 "Assumption 1. ‣ 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") and [2](https://arxiv.org/html/2602.07841v1#Thmassumption2 "Assumption 2. ‣ 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy"), the expected out-of-sample R2R^{2} of MSE-optimal point forecasts follows a quadratic function of the directional probability pp:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ROOS2]=κ⋅(2​p−1)2,\mathbb{E}[R^{2}\_{\text{OOS}}]=\kappa\cdot(2p-1)^{2}, |  | (13) |

where κ\kappa is a distributional shape parameter defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ≡(𝔼​[|zt|])2𝔼​[zt2].\kappa\equiv\frac{(\mathbb{E}[|z\_{t}|])^{2}}{\mathbb{E}[z\_{t}^{2}]}. |  | (14) |

In empirical applications, substituting the realized DA and the estimated shape parameter κ^\hat{\kappa} into Eq [13](https://arxiv.org/html/2602.07841v1#S2.E13 "In Proposition 1. ‣ 2.2 The Out-of-Sample 𝑅² Expression ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") yields a theoretical benchmark for predictive performance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ROOS2=κ^​(2⋅DA−1)2,R^{2}\_{\text{OOS}}=\hat{\kappa}(2\cdot\text{DA}-1)^{2}, |  | (15) |

where κ^\hat{\kappa} is calculated by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ^=(1T​∑t∈ΩOOS|zt^|)21T​∑t∈ΩOOSzt^2.\hat{\kappa}=\frac{\left(\frac{1}{T}\sum\_{t\in\Omega\_{\text{OOS}}}|\hat{z\_{t}}|\right)^{2}}{\frac{1}{T}\sum\_{t\in\Omega\_{\text{OOS}}}\hat{z\_{t}}^{2}}. |  | (16) |

In Eq. [16](https://arxiv.org/html/2602.07841v1#S2.E16 "In 2.2 The Out-of-Sample 𝑅² Expression ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy"), TT denotes the number of observations in the out-of-sample set ΩOOS\Omega\_{\text{OOS}}, and zt^\hat{z\_{t}} is the standardized innovation defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zt^=Δ​ytσ^t,\hat{z\_{t}}=\frac{\Delta y\_{t}}{\hat{\sigma}\_{t}}, |  | (17) |

where σ^t\hat{\sigma}\_{t} is the conditional volatility estimated by the forecasting model.

## 3 Numerical Illustration

This section presents the numerical validation of the proposed theoretical link. Since predictive models for financial time series forecasting rarely yield point forecasts with high DAs, numerical validation is conducted through simulation experiments.

### 3.1 Experimental Setup

The datasets for simulations are retrieved from Stooq.com, including daily closing prices for the S&P 500 index from January 5, 1789, to January 30, 2026, and for the DJIA index from May 27, 1896, to January 30, 2026. The first 80% of each series is allocated for in-sample parameter estimation, with the remaining 20% reserved for out-of-sample evaluation.

Given that any point forecast can be expressed as the product of its sign and magnitude, we use synthetic sign forecasts with specific volatility structures, as well as a scaling factor, to construct point forecasts for simulations. Synthetic sign forecasts are generated independently of the realized return magnitude with 20 predetermined accuracy levels ranging from 0.50 to 1.00. Therefore, 100 sets of sign forecasts are generated for each DA level. In particular, we consider three types of forecasts, using the same conditional volatility estimated via a GARCH(1,1) process:

1. 1.

   Type 1 forecasts: μt=λOLS⋅D^t⋅σ^t\mu\_{t}=\lambda\_{\text{OLS}}\cdot\hat{D}\_{t}\cdot\hat{\sigma}\_{t}. The scaling factor is optimized by OLS. This approach represents the ideal condition where the forecast is MSE-optimal and satisfies Assumption [1](https://arxiv.org/html/2602.07841v1#Thmassumption1 "Assumption 1. ‣ 2.1 Point Forecast Decomposition ‣ 2 The Analytical Link ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy").
2. 2.

   Type 2 forecasts: μt=λconst⋅D^t⋅σ^t\mu\_{t}=\lambda\_{\text{const}}\cdot\hat{D}\_{t}\cdot\hat{\sigma}\_{t}. The scaling factor is a constant. This approach represents suboptimal forecasts.
3. 3.

   Type 3 forecasts: μt=λOLS⋅D^t⋅(σ^t⋅wt)\mu\_{t}=\lambda\_{\text{OLS}}\cdot\hat{D}\_{t}\cdot(\hat{\sigma}\_{t}\cdot w\_{t}). wtw\_{t} is a coefficient that is positively correlated with sign correctness. Therefore, this approach violates the independence assumption.

Although these three types of forecasts do not cover all real forecasting scenarios, they represent three mechanisms in which the point forecasts generated by any given predictive model can be categorized to one of them, with the exception of arbitrary point forecasts.

### 3.2 Experimental Results

Figures [1](https://arxiv.org/html/2602.07841v1#S3.F1 "Figure 1 ‣ 3.2 Experimental Results ‣ 3 Numerical Illustration ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") and [2](https://arxiv.org/html/2602.07841v1#S3.F2 "Figure 2 ‣ 3.2 Experimental Results ‣ 3 Numerical Illustration ‣ A Quadratic Link between Out-of-Sample 𝑅² and Directional Accuracy") present the simulation results against the theoretical benchmarks. We first estimate the distributional shape parameter κ\kappa via the out-of-sample data. In particular, κ^=0.55\hat{\kappa}=0.55 for the S&P 500 and κ^=0.48\hat{\kappa}=0.48 for the DJIA. Both estimates are significantly lower than the Gaussian baseline (κ^Gauss≈0.64\hat{\kappa}\_{\text{Gauss}}\approx 0.64), indicating that the returns are heavy-tailed.

![Refer to caption](SP500.jpg)

Figure 1: Out-of-sample R2R^{2} versus directional accuracy: S&P 500.



![Refer to caption](DJIA.jpg)

Figure 2: Out-of-sample R2R^{2} versus directional accuracy: DJIA.

Each marker indicates the out-of-sample performance of a specific set of point forecasts. In both figures, negative values of realized ROOS2R^{2}\_{\text{OOS}} are observed when DAs are modest, which is the manifestation of metric disconnect phenomena. These negative values of ROOS2R^{2}\_{\text{OOS}} are generally from type 2 forecasts, which fail to scale magnitudes dynamically with market turbulence. Moreover, the type 1 forecasts also have a negative ROOS2R^{2}\_{\text{OOS}} when the DA is modest. This is because of the random nature of simulations, which often leads to correct directional forecasts coinciding with periods of low market volatility. In addition, the large positive deviation of the type 3 forecasts from the theoretical benchmark implies a directional timing ability. However, this ability is based on oracle forecasts and is rare in real forecasting scenarios.

## 4 Conclusion

While ROOS2R^{2}\_{\text{OOS}} measures the magnitude of forecast errors, this study shows that it is fundamentally constrained by the DA. Negative values of ROOS2R^{2}\_{\text{OOS}} coupled with modest values of DA are expected when the predictive model is suboptimal or when there is a negative sample correlation between sign correctness and realized magnitude. The simulation results also validate this analytical link as an effective benchmark for examining directional timing ability.

## Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work, the author used Gemini 3 in order to improve the readability of the manuscript. After using this tool, the author reviewed and edited the content as needed and takes full responsibility for the content of the published article.

## Declaration of interest statement

The author reports that there are no competing interests to declare.

## References

* \NAT@swatrue
* Beck et al. (2025)

  Beck, N., Dovern, J., and Vogl, S.
  (2025).
  Mind the naive
  forecast! a rigorous evaluation of forecasting models for time series with
  low predictability.
  *Applied Intelligence*, *55*(6), 395.

  \NAT@swatrue
* Bustos and Pomares-Quimbaya (2020)

  Bustos, O., and Pomares-Quimbaya, A.
  (2020).
  Stock market movement forecast: A systematic review.
  *Expert Systems with Applications*, *156*, 113464.

  \NAT@swatrue
* Ellwanger and Snudden (2023)

  Ellwanger, and Snudden.
  (2023).
  Forecasts of the real price of oil revisited: Do they
  beat the random walk?
  *Journal of Banking & Finance*, *154*, 106962.

  \NAT@swatrue
* Farmer et al. (2023)

  Farmer, L., Schmidt, L., and Timmermann, A.
  (2023).
  Pockets of
  predictability.
  *The Journal of Finance*, *78*(2), 775–813.
  \NAT@swatrue
* Gu et al. (2020)

  Gu, S., Kelly, B., and Xiu, D.
  (2020).
  Empirical
  asset pricing via machine learning.
  *The Review of Financial Studies*, *33*(5), 2223–2273.
  \NAT@swatrue
* Hamilton (2020)

  Hamilton, J. D.
  (2020).
  *Time series analysis*.
  Princeton university press.
  \NAT@swatrue
* Hewamalage et al. (2023)

  Hewamalage, H., Ackermann, K., and Bergmeir, C.
  (2023).
  Forecast evaluation for data scientists: common pitfalls
  and best practices.
  *Data Mining and Knowledge Discovery*, *37*(2), 788–832.

  \NAT@swatrue
* Kilian and Taylor (2003)

  Kilian, L., and Taylor, M. P.
  (2003).
  Why is it so difficult to beat the random walk forecast
  of exchange rates?
  *Journal of International Economics*, *60*(1), 85–107.

  \NAT@swatrue
* Leitch and Tanner (1991)

  Leitch, G., and Tanner, J. E.
  (1991).
  Economic forecast evaluation: profits versus
  the conventional error measures.
  *American Economic Review*, *81*(3), 580–590.
  \NAT@swatrue
* Meese and Rogoff (1983)

  Meese, R. A., and Rogoff, K.
  (1983).
  Empirical exchange rate models of the seventies: Do they
  fit out of sample?
  *Journal of International Economics*, *14*(1-2), 3–24.
  \NAT@swatrue
* Moosa (2013)

  Moosa.
  (2013).
  Why is it so difficult to outperform the random
  walk in exchange rate forecasting?
  *Applied Economics*, 3340–3346.

  \NAT@swatrue
* Petropoulos et al. (2022)

  Petropoulos, F., Apiletti, D., Assimakopoulos, V., Babai, M. Z., Barrow, D. K., Taieb, S. B., … others
  (2022).
  Forecasting: theory
  and practice.
  *International Journal of Forecasting*, *38*(3), 705–871.

  \NAT@swatrue
* Taylor (2008)

  Taylor.
  (2008).
  *Modelling financial time
  series*.
  World Scientific.
  \NAT@swatrue
* Welch and Goyal (2008)

  Welch, I., and Goyal, A.
  (2008).
  A comprehensive look at the empirical performance
  of equity premium prediction.
  *Review of Financial Studies*, *21*(4), 1455–1508.
  \NAT@swatrue
* Zeng et al. (2023)

  Zeng, A., Chen, M., Zhang, L., and Xu, Q.
  (2023).
  Are transformers effective for time series forecasting?
  In *Proceedings of the aaai conference on artificial
  intelligence* (Vol. 37, pp. 11121–11128).