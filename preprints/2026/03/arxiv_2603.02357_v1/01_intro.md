---
authors:
- Xiaochun Liu
- Richard Luger
doc_id: arxiv:2603.02357v1
family_id: arxiv:2603.02357
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2603.02357v1
url_html: https://arxiv.org/html/2603.02357v1
venue: arXiv q-fin
version: 1
year: 2026
---

Title:


Content selection saved. Describe the issue below:

Description:

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.02357v1[econ.EM] 02 Mar 2026

Quantile-based modeling of scale dynamics in financial returns for Value-at-Risk and Expected Shortfall forecasting

*This is the author accepted manuscript.*

*Accepted for publication in International Journal of Forecasting.*

*DOI:* 10.1016/j.ijforecast.2025.12.002

Xiaochun Liu\*\*\*Department of Economics, Finance and Legal Studies, Culverhouse College of Business, University of Alabama, Tuscaloosa, AL 35487, USA. *E-mail address:* xliu121@ua.edu. and Richard Luger†††Corresponding author. Department of Finance, Insurance and Real Estate, Laval University, Quebec City, Quebec G1V 0A6, Canada.
*E-mail address:* richard.luger@fsa.ulaval.ca.

Abstract: We introduce a semiparametric approach for forecasting Value-at-Risk (VaR) and Expected Shortfall (ES) by modeling the conditional scale of financial returns, defined as the difference between two specified quantiles, via restricted quantile regression. Focusing on downside risk, VaR is derived from the left-tail quantile of rescaled returns, and ES is approximated by averaging quantiles below the VaR level. The method delivers robust, distribution-free estimates of extreme losses and captures skewness, heavy tails, and leverage effects. Simulation experiments and empirical analysis show that it often outperforms established models, including GARCH and joint VaR-ES conditional-quantile approaches. An application to daily returns on major international stock indices, spanning the COVID-19 period, highlights its effectiveness in capturing risk dynamics.

JEL classification: C14, C22, G17, G32

Keywords: Conditional scale dynamics, CAViaR models, Multiple quantiles, Robust risk estimation, Financial risk forecasting

## 1 Introduction

Forecasting risk measures such as Value-at-Risk (VaR) and Expected Shortfall (ES) is crucial for financial institutions, risk managers, and regulators. VaR, which estimates a conditional quantile in the lower tail of the return distribution, has long been a standard tool for assessing potential losses.
Specifically, the VaR for period tt at probability level α\alpha is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRrt​(α)=Qrt​(α|ℐt−1),\text{VaR}\_{r\_{t}}(\alpha)=Q\_{r\_{t}}(\alpha\,|\,\mathcal{I}\_{t-1}), |  | (1) |

where rtr\_{t} denotes the asset return at time tt and Qrt​(α|ℐt−1)Q\_{r\_{t}}(\alpha\,|\,\mathcal{I}\_{t-1}) is the α\alphath conditional quantile given the information set ℐt−1\mathcal{I}\_{t-1}.
However, VaR has notable limitations, particularly its inability to account for extreme losses beyond the quantile threshold defined by
α\alpha, and its potential failure to capture diversification benefits (Embrechts et al., [2002](#bib.bib20 "Correlation and dependence in risk management: properties and pitfalls")).
This is because VaR is not a coherent risk measure; it does not satisfy the property of subadditivity, meaning that the VaR of a combined portfolio can exceed the sum of the VaRs of its individual components. As a result, VaR may inadequately reflect the benefits of diversification.

In contrast, ES is a coherent risk measure, addressing these shortcomings by estimating the expected loss beyond the VaR threshold and, in particular, satisfying
subadditivity (Artzner et al., [1999](#bib.bib4 "Coherent measures of risk"); Acerbi and Tasche, [2002](#bib.bib1 "On the coherence of expected shortfall")). Conditional on information ℐt−1\mathcal{I}\_{t-1}, ES for period tt at probability level α\alpha is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESrt​(α)=𝔼​[rt|rt≤VaRrt​(α),ℐt−1],\text{ES}\_{r\_{t}}(\alpha)=\mathbb{E}[r\_{t}\,|\,r\_{t}\leq\text{VaR}\_{r\_{t}}(\alpha),\,\mathcal{I}\_{t-1}], |  | (2) |

providing the average loss when rtr\_{t} falls below the VaR threshold in ([1](#S1.E1 "In 1 Introduction")). This makes ES a more theoretically sound measure that incentivizes diversification and better accounts for extreme risks.
Recognizing these advantages, the Basel Committee, through its Basel III framework and the Fundamental Review of the Trading Book (FRTB), has replaced VaR with ES as the primary metric for market risk capital requirements (Basel Committee on Banking Supervision, [2019](#bib.bib5 "Minimum capital requirements for market risk")).
This regulatory shift underscores the need for robust ES forecasting models that can accurately quantify tail risk under changing market conditions.

ES forecasts can often be derived as a natural extension of many VaR forecasting methods. Nonparametric approaches, including historical simulation and kernel density estimation, generate density forecasts from which both VaR and ES predictions can be obtained. Similarly, parametric methods, typically based on models for the conditional variance, such as GARCH specifications combined with a precise assumption about the conditional return distribution, provide concurrent forecasts for both risk measures.

A prominent semiparametric method for VaR forecasting is quantile regression, specifically the Conditional Autoregressive VaR (CAViaR) models of Engle and Manganelli ([2004](#bib.bib21 "CAViaR: conditional autoregressive Value at Risk by regression quantiles")), which model the conditional quantile directly without relying on specific distributional assumptions.
Let yt=rt−μty\_{t}=r\_{t}-\mu\_{t}, where μt\mu\_{t} represents the conditional location of returns, often assumed to be zero, a constant, or a dynamic process such as AR(1), as in Kuester et al. ([2006](#bib.bib35 "Value-at-Risk Prediction: A Comparison of Alternative Strategies")). A first-order symmetric absolute value (SAV) CAViaR specification is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qyt​(α|ℐt−1)=ω​(α)+β​(α)​Qyt−1​(α|ℐt−2)+γ​(α)​|yt−1|,Q\_{y\_{t}}(\alpha\,|\,\mathcal{I}\_{t-1})=\omega(\alpha)+\beta(\alpha)Q\_{y\_{t-1}}(\alpha\,|\,\mathcal{I}\_{t-2})+\gamma(\alpha)\lvert y\_{t-1}\rvert, |  | (3) |

with the VaR in ([1](#S1.E1 "In 1 Introduction")) given by Qrt​(α|ℐt−1)=μt+Qyt​(α|ℐt−1)Q\_{r\_{t}}(\alpha\,|\,\mathcal{I}\_{t-1})=\mu\_{t}+Q\_{y\_{t}}(\alpha\,|\,\mathcal{I}\_{t-1}).
This model treats positive and negative deviations of yt−1y\_{t-1} symmetrically, relying solely on |yt−1|\lvert y\_{t-1}\rvert and thereby implicitly responding to volatility symmetrically. Alternatively, an asymmetric slope (AS) CAViaR specification is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qyt​(α|ℐt−1)=\displaystyle Q\_{y\_{t}}(\alpha\,|\,\mathcal{I}\_{t-1})= | ω​(α)+β​(α)​Qyt−1​(α|ℐt−2)+(γ+​(α)​𝟙​{yt−1>0}+γ−​(α)​𝟙​{yt−1≤0})​|yt−1|,\displaystyle\,\omega(\alpha)+\beta(\alpha)Q\_{y\_{t-1}}(\alpha\,|\,\mathcal{I}\_{t-2})+\big(\gamma\_{+}(\alpha)\mathds{1}\{y\_{t-1}>0\}+\gamma\_{-}(\alpha)\mathds{1}\{y\_{t-1}\leq 0\}\big)|y\_{t-1}|, |  | (4) |

where 𝟙​{⋅}\mathds{1}\{\cdot\} denotes the indicator function.
This formulation allows the model to capture asymmetries in the conditional quantile dynamics by adjusting the slope based on whether the previous centered return was positive or negative, thus making it sensitive to directional changes in past returns.
The CAViaR models in ([3](#S1.E3 "In 1 Introduction")) and ([4](#S1.E4 "In 1 Introduction")) allow the dynamics of Qyt​(α|ℐt−1)Q\_{y\_{t}}(\alpha\,|\,\mathcal{I}\_{t-1}) to vary across different probability levels α\alpha and have shown strong performance in empirical studies of VaR forecast accuracy (see, e.g., Şener et al., [2012](#bib.bib48 "Ranking the predictive performances of value-at-risk estimation methods")). However, while CAViaR models excel in predicting VaR, they do not inherently provide a mechanism for generating ES forecasts, as they focus solely on a particular quantile of the return distribution.

Recent advances in risk forecasting have focused on methods that jointly estimate VaR and ES, leveraging the fact that these two risk measures are jointly elicitable (Fissler and Ziegel, [2016](#bib.bib23 "Higher order elicitability and Osband’s principle")). A risk measure is said to be elicitable if it can be uniquely identified as the minimizer of a well-defined expected loss function, also known as a scoring function. In simpler terms, an elicitable risk measure can be evaluated and compared using a loss function that ranks different forecasting methods based on their accuracy. While ES is not elicitable on its own, the joint elicitability of VaR and ES allows for their simultaneous estimation and evaluation using a common loss function. This property has been pivotal in recent developments in financial risk forecasting.

Taylor ([2019](#bib.bib52 "Forecasting value at risk and expected shortfall using a semiparametric approach based on the asymmetric Laplace distribution")) proposes a joint VaR-ES model based on the asymmetric Laplace (AL) distribution, where the VaR component is modeled using a CAViaR specification.
This approach uses the AL density to construct a likelihood function, whose maximization is equivalent to minimizing a strictly consistent Fissler and Ziegel ([2016](#bib.bib23 "Higher order elicitability and Osband’s principle")) scoring function.
Similarly, Patton et al. ([2019](#bib.bib46 "Dynamic semiparametric models for expected shortfall (and Value-at-Risk)")) introduce a semiparametric approach within the Generalized Autoregressive Score (GAS) framework of Creal et al. ([2013](#bib.bib14 "GENERALIZED autoregressive score models with applications")), which also exploits the Fissler and Ziegel ([2016](#bib.bib23 "Higher order elicitability and Osband’s principle")) class of loss functions. Their GAS model dynamically adjusts both VaR and ES estimates based on past observations, specifically reacting to VaR violations while reverting to a long-run mean in the absence of breaches.

In this paper, we introduce a novel semiparametric CAViaR-based framework for forecasting VaR and ES, which we term the Quantile-based Scale Dynamics (QbSD) approach.
The QbSD framework extends the widely used GARCH class by replacing the conditional standard deviation with a conditional scale—a measure analogous to the interquartile range (IQR), but more flexible as it is based on the difference between two specified quantiles of the return distribution, similar to Taylor ([2005](#bib.bib51 "Generating volatility forecasts from value at risk estimates")).
To model the dynamics of the conditional scale, QbSD employs global CAViaR specifications in which persistence parameters are shared across quantiles to ensure parsimony, while local parameters account for level-specific adjustments. Parameter constraints enforce non-crossing quantile ordering and strictly positive scale values, ensuring internal consistency and robust tail risk estimation.

Beyond its theoretical advantages, the QbSD approach aligns with practical needs in financial risk management. Financial institutions rely on multiple model validations in modern risk management frameworks, particularly for stress-testing and regulatory reporting under Basel III guidelines. Given its flexibility and lack of reliance on specific distributional assumptions, QbSD can serve as a complementary tool for financial institutions in benchmarking VaR and ES estimates against conventional models. This is particularly relevant in periods of financial distress, where traditional parametric models may struggle to adapt to evolving risk dynamics. Furthermore, by providing more accurate tail risk estimates, QbSD can aid institutions in regulatory capital calculations and internal risk monitoring, supporting more resilient decision-making.

To achieve this, QbSD models the dynamics of conditional quantiles, enabling a structured estimation of both VaR and ES.
Specifically, VaR is estimated from the left-tail quantile of the rescaled returns, while ES is approximated by averaging quantiles across probability levels below the VaR threshold.
This approach leverages the representation of ES as the integral of conditional quantiles across the left tail of the distribution up to the VaR probability level (see, e.g., Acerbi and Tasche, [2002](#bib.bib1 "On the coherence of expected shortfall")).
As a result, the method delivers valid, well-ordered risk estimates across all probability levels, including those in the extreme tails of the distribution.

This approach shares similarities with the Filtered Historical Simulation (FHS) method described by Christoffersen ([2012](#bib.bib13 "Elements of financial risk management"), Section 6.4), which first applies a volatility model—typically a GARCH specification with an assumed innovation distribution—to filter historical returns. FHS then standardizes the returns by dividing them by the conditional volatility estimates, and subsequently computes the quantiles of these residuals to estimate VaR. The average residual loss beyond the VaR estimate is used to calculate ES. In contrast, the semiparametric QbSD approach does not rely on a specific distributional assumption. Instead, it models the conditional scale dynamics using restricted CAViaR specifications, offering a robust and distribution-free framework for forecasting VaR and ES.

The remainder of the paper is organized as follows. Section 2 develops the QbSD approach for forecasting VaR and ES. Section 3 presents simulation experiments designed to evaluate the performance of the proposed method across a range of market conditions. In Section 4, we assess the QbSD method’s effectiveness through an empirical application, using daily returns from major international stock indices, including the volatile period surrounding the COVID-19 pandemic. Finally, Section 5 concludes the paper. Additional numerical and empirical results are provided in the Supplementary material.

## 2 Quantile-based modeling

### 2.1 Background

Consider first the unconditional distribution of asset returns and suppose it belongs to the location-scale family, so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=μ+s​εt,r\_{t}=\mu+s\varepsilon\_{t}, |  | (5) |

where μ\mu is the location parameter, s>0s>0 is the scale parameter, and εt\varepsilon\_{t} is an i.i.d. innovation with distribution function FεF\_{\varepsilon} and zero location.

There are several ways to define the scale parameter. A commonly used one is the standard deviation, which is based on moments. Despite its widespread usage, the standard deviation is sensitive to the presence of outliers and may even be undefined or infinite for distributions with heavy tails. This sensitivity arises from the fact that the standard deviation has a zero breakdown point, meaning that even a single outlier can significantly distort the estimate (see Huber and Ronchetti, [2009](#bib.bib31 "Robust statistics"), Ch. 5). In contrast, scale estimators based on interquantile ranges have non-zero breakdown points, making them more robust to outliers and extreme values, which are common in financial return data.111Kim and White ([2004](#bib.bib34 "On more robust estimation of skewness and kurtosis")) also advocate using quantiles to estimate characteristics of return distributions, focusing on robust measures for capturing skewness and kurtosis. Through simulations, they demonstrate that empirical moment-based estimators are significantly more sensitive to outliers. See also White et al. ([2010](#bib.bib53 "Modeling autoregressive conditional skewness and kurtosis with multi-quantile CAViaR")) and Ghysels ([2014](#bib.bib26 "Conditional skewness with quantile regression models: SoFiE presidential address and a tribute to Hal White")).

With the location-scale representation in ([5](#S2.E5 "In 2.1 Background ‣ 2 Quantile-based modeling")), the ppth quantile of the unconditional return distribution is Qrt​(p)=μ+s​Fε−1​(p)Q\_{r\_{t}}(p)=\mu+sF\_{\varepsilon}^{{}^{-1}}(p). Let 0<p<0.50<p<0.5 be a chosen quantile level. Following Taylor ([2005](#bib.bib51 "Generating volatility forecasts from value at risk estimates")), consider the quantile at the (1−p)(1-p)th level as a natural and compelling counterpart.
Even when μ\mu is unknown, we can obtain ss as

|  |  |  |  |
| --- | --- | --- | --- |
|  | s=Qrt​(1−p)−Qrt​(p)cp,s=\frac{Q\_{r\_{t}}(1-p)-Q\_{r\_{t}}(p)}{c\_{p}}, |  | (6) |

where cp=Fε−1​(1−p)−Fε−1​(p)c\_{p}=F\_{\varepsilon}^{-1}(1-p)-F\_{\varepsilon}^{-1}(p) is a scaling term. Note that when rt∼N​(μ,σ2)r\_{t}\sim N(\mu,\sigma^{2}), then ([6](#S2.E6 "In 2.1 Background ‣ 2 Quantile-based modeling")) yields s=σs=\sigma. The quantity IQR=Qrt​(0.75)−Qrt​(0.25)\text{IQR}=Q\_{r\_{t}}(0.75)-Q\_{r\_{t}}(0.25) is the well-known *interquartile range*, which takes the form in ([6](#S2.E6 "In 2.1 Background ‣ 2 Quantile-based modeling")) by setting cp=1c\_{p}=1.
Another measure that fits this format is the Pearson and Tukey ([1965](#bib.bib47 "Approximate means and standard deviations based on distances between percentage points of frequency curves")) scale measure that uses p=0.05p=0.05 and cp=q0​(1−p)−q0​(p)c\_{p}=q\_{0}(1-p)-q\_{0}(p), where q0​(p)q\_{0}(p) is the ppth quantile of the standard normal distribution. See Taylor ([2005](#bib.bib51 "Generating volatility forecasts from value at risk estimates")) and Kotz and van Dorp ([2005](#bib.bib38 "A link between two-sided power and asymmetric Laplace distributions: with applications to mean and variance approximations"), Table 1) for other examples.

### 2.2 Conditional dynamics

We extend the basic specification in ([5](#S2.E5 "In 2.1 Background ‣ 2 Quantile-based modeling")) to allow the location and scale parameters to be conditionally dynamic so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=μt+st​εt,r\_{t}=\mu\_{t}+s\_{t}\varepsilon\_{t}, |  | (7) |

where μt\mu\_{t} and st>0s\_{t}>0 are functions of past information, ℐt−1\mathcal{I}\_{t-1}.
This structure mirrors the typical GARCH framework, where both the conditional mean and the conditional standard deviation evolve over time based on past information.
In the following, we focus primarily on first-order specifications when modeling the dynamics in μt\mu\_{t} and sts\_{t}.
While higher lag orders can be taken into account if required, such specifications are widely favored and commonly used in practice.

In some applications, it may be reasonable to set μt\mu\_{t} to zero or to assume that μt=μ\mu\_{t}=\mu, as done in Taylor ([2019](#bib.bib52 "Forecasting value at risk and expected shortfall using a semiparametric approach based on the asymmetric Laplace distribution")).
However, autocorrelation in financial returns is often non-negligible (Kuester et al., [2006](#bib.bib35 "Value-at-Risk Prediction: A Comparison of Alternative Strategies")).
This property can be incorporated into our quantile-based modeling framework by allowing the returns to have a time-varying conditional median of the form
μt=Qrt​(0.5|ℐt−1)\mu\_{t}=Q\_{r\_{t}}(0.5\,|\,\mathcal{I}\_{t-1}), which may be captured by a quantile autoregression (QAR) model, as proposed by Koenker and Xiao ([2006](#bib.bib37 "Quantile autoregression")).
For example, a first-order QAR model is formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qrt​(0.5|ℐt−1)=μ+ϕ​rt−1,Q\_{r\_{t}}(0.5\,|\,\mathcal{I}\_{t-1})=\mu+\phi r\_{t-1}, |  | (8) |

where μ\mu represents a baseline median, and ϕ\phi captures the impact of rt−1r\_{t-1} on the current period’s median.

Our analysis concentrates on downside market risk. Accordingly, we define 0<τ≤0.050<\tau\leq 0.05, where τ\tau
represents the typical left-tail region of interest in financial risk management, capturing extreme losses.
We then set τ≤p<0.5\tau\leq p<0.5, where pp specifies the quantile levels used to construct the scale measure.
Consider the conditional version of ([6](#S2.E6 "In 2.1 Background ‣ 2 Quantile-based modeling")) written here as

|  |  |  |  |
| --- | --- | --- | --- |
|  | st=st​(p)=Qrt​(1−p|ℐt−1)−Qrt​(p|ℐt−1)cp,s\_{t}=s\_{t}(p)=\frac{Q\_{r\_{t}}(1-p\,|\,\mathcal{I}\_{t-1})-Q\_{r\_{t}}(p\,|\,\mathcal{I}\_{t-1})}{c\_{p}}, |  | (9) |

where cp=Fε−1​(1−p)−Fε−1​(p)c\_{p}=F\_{\varepsilon}^{-1}(1-p)-F\_{\varepsilon}^{-1}(p) is a time-invariant scaling term, as before.222As Taylor ([2005](#bib.bib51 "Generating volatility forecasts from value at risk estimates")) observes, estimating scale (or volatility) using the interval between tail quantiles shares similarities with range-based volatility estimation (e.g., Parkinson, [1980](#bib.bib45 "The extreme value method for estimating the variance of the rate of return"); Garman and Klass, [1980](#bib.bib25 "On the estimation of security price volatilities from historical data"); Alizadeh et al., [2002](#bib.bib2 "Range-based estimation of stochastic volatility models")). This class of methods relies on the difference between the highest and lowest log prices, which essentially correspond to the quantiles at 1−p=11-p=1 and p=0p=0, respectively. 
It is interesting to note here again that sts\_{t}
is invariant to the specific process governing μt\mu\_{t} in ([7](#S2.E7 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")).
We can then express the model specification as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=μt+st∗​εt∗,st∗=Qyt​(1−p|ℐt−1)−Qyt​(p|ℐt−1),\begin{split}r\_{t}&=\mu\_{t}+s\_{t}^{\ast}\varepsilon\_{t}^{\ast},\\ s\_{t}^{\ast}&=Q\_{y\_{t}}(1-p\,|\,\mathcal{I}\_{t-1})-Q\_{y\_{t}}(p\,|\,\mathcal{I}\_{t-1}),\end{split} |  | (10) |

where yt=rt−μty\_{t}=r\_{t}-\mu\_{t} and εt∗=yt/st∗=εt/cp\varepsilon\_{t}^{\ast}=y\_{t}/s\_{t}^{\ast}=\varepsilon\_{t}/c\_{p} is simply a rescaled version of εt\varepsilon\_{t}.
The τ\tauth conditional quantile of yt=st∗​εt∗y\_{t}=s\_{t}^{\ast}\varepsilon\_{t}^{\ast} is given by Qyt​(τ|ℐt−1)=st∗​Fε∗−1​(τ)Q\_{y\_{t}}(\tau\,|\,\mathcal{I}\_{t-1})=s\_{t}^{\ast}F^{-1}\_{\varepsilon^{\ast}}(\tau), where Fε∗−1​(τ)F^{-1}\_{\varepsilon^{\ast}}(\tau) is a constant.
Similar to the conditional standard deviation in a GARCH model, st∗s\_{t}^{\ast} serves as a common factor across quantiles, ensuring coherence and building dependence between them in a parsimonious manner.

To model the dynamics of st∗s^{\ast}\_{t}, we draw a parallel with the absolute value GARCH model of Taylor:1986 and Schwert ([1990](#bib.bib50 "Stock volatility and the crash of ’87")), which captures the conditional standard deviation using past absolute deviations. We assume

|  |  |  |  |
| --- | --- | --- | --- |
|  | st∗=ω+β​st−1∗+γ​|yt−1|,s^{\ast}\_{t}=\omega+\beta s^{\ast}\_{t-1}+\gamma|y\_{t-1}|, |  | (11) |

so that the scale of returns adjusts dynamically in a manner similar to the absolute value GARCH framework.
Observing that st−j∗​Fε∗−1​(k)=Qyt−j​(k|ℐt−j−1)s\_{t-j}^{\ast}F^{-1}\_{\varepsilon^{\ast}}(k)=Q\_{y\_{t-j}}(k\,|\,\mathcal{I}\_{t-j-1}), we adopt
the approach of Xiao and Koenker ([2009](#bib.bib76 "Conditional quantile estimation for generalized autoregressive conditional heteroscedasticity models")), who use an absolute value GARCH structure, to express the two key quantiles in ([10](#S2.E10 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) with the following global SAV CAViaR structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qyt​(k|ℐt−1)=ω​(k)+(β+γ​|εt−1∗|)​Qyt−1​(k|ℐt−2),Q\_{y\_{t}}(k\,|\,\mathcal{I}\_{t-1})=\omega(k)+\big(\beta+\gamma|\varepsilon\_{t-1}^{\ast}|\big)Q\_{y\_{t-1}}(k\,|\,\mathcal{I}\_{t-2}), |  | (12) |

for both k=pk=p and k=1−pk=1-p, subject to ω​(p)<ω​(1−p)\omega(p)<\omega(1-p), β≥0\beta\geq 0, and γ≥0\gamma\geq 0. These restrictions ensure non-crossing quantiles and guarantee st∗>0s^{\ast}\_{t}>0 in ([10](#S2.E10 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")), provided the recursion begins with Qy1​(p|ℐ0)<Qy1​(1−p|ℐ0)Q\_{y\_{1}}(p\,|\,\mathcal{I}\_{0})<Q\_{y\_{1}}(1-p\,|\,\mathcal{I}\_{0}).
Here, the persistence parameters β\beta and γ\gamma are global, meaning they do not vary with kk, while ω​(k)=ω​Fε∗−1​(k)\omega(k)=\omega F^{-1}\_{\varepsilon^{\ast}}(k) is local and dependent on the quantile level kk.

As an alternative to ([11](#S2.E11 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")), we also consider a threshold-based specification, similar to the threshold GARCH model of Zakoïan ([1994](#bib.bib54 "Threshold heteroskedastic models")):

|  |  |  |
| --- | --- | --- |
|  | st∗=ω+β​st−1∗+(γ+​𝟙​{yt−1>0}+γ−​𝟙​{yt−1≤0})​|yt−1|,s^{\ast}\_{t}=\omega+\beta s^{\ast}\_{t-1}+\big(\gamma\_{+}\mathds{1}\{y\_{t-1}>0\}+\gamma\_{-}\mathds{1}\{y\_{t-1}\leq 0\}\big)|y\_{t-1}|, |  |

which allows st∗s^{\ast}\_{t} to respond differently to positive and negative values of yt−1y\_{t-1}.
This leads to the following global AS CAViaR structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qyt​(k|ℐt−1)=ω​(k)+(β+(γ+​𝟙​{yt−1>0}+γ−​𝟙​{yt−1≤0})​|εt−1∗|)​Qyt−1​(k|ℐt−2),Q\_{y\_{t}}(k\,|\,\mathcal{I}\_{t-1})=\omega(k)+\Big(\beta+\big(\gamma\_{+}\mathds{1}\{y\_{t-1}>0\}+\gamma\_{-}\mathds{1}\{y\_{t-1}\leq 0\}\big)|\varepsilon\_{t-1}^{\ast}|\Big)Q\_{y\_{t-1}}(k\,|\,\mathcal{I}\_{t-2}), |  | (13) |

for both k=pk=p and k=1−pk=1-p, subject to ω​(p)<ω​(1−p)\omega(p)<\omega(1-p), β≥0\beta\geq 0, γ+≥0\gamma\_{+}\geq 0, and γ−≥0\gamma\_{-}\geq 0.
Here, β\beta, γ+\gamma\_{+}, and γ−\gamma\_{-} are global parameters.
This specification allows an asymmetric response in the conditional quantile process, capturing the differing impacts of positive and negative past shocks.
Empirical studies by Nelson ([1991](#bib.bib43 "Conditional heteroskedasticity in asset returns: a new approach")), Glosten et al. ([1993](#bib.bib27 "On the relation between the expected value and the volatility of the nominal excess return on stocks")), and Engle and Ng ([1993](#bib.bib22 "Measuring and testing the impact of news on volatility")), among others, provide strong evidence that asymmetry is crucial for accurately modeling volatility dynamics, as negative stock returns are typically associated with greater increases in return volatility. This justifies the inclusion of an asymmetric term in financial time series models such as the AS CAViaR.
For simplicity, the notation in ([3](#S1.E3 "In 1 Introduction")), ([4](#S1.E4 "In 1 Introduction")), ([8](#S2.E8 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")), ([12](#S2.E12 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")), and ([13](#S2.E13 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) omits the dependence on the involved parameters.

For estimation purposes, we recommend the following sequential strategy: (i) estimate the parameters of ([8](#S2.E8 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) and obtain the
fitted values μ^t=Q^rt​(0.5|ℐt−1)\hat{\mu}\_{t}=\hat{Q}\_{r\_{t}}(0.5\,|\,\mathcal{I}\_{t-1}), and then (ii) estimate the parameters of the CAViaR specifications
with μt\mu\_{t} replaced by μ^t\hat{\mu}\_{t}.
While this approach may not be as statistically efficient as joint estimation, it offers the advantage of being simpler and more numerically robust.
We begin with the estimation of the QAR model.
Let 𝜽k{\bm{\theta}}\_{k} represent the parameter vector for ([8](#S2.E8 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) with k=0.5k=0.5.
The estimate 𝜽^k\hat{\bm{\theta}}\_{k} can be obtained by solving the minimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝜽k​∑tρk​[rt−Qrt​(k|ℐt−1)],\min\_{\bm{\theta}\_{k}}\sum\_{t}\rho\_{k}\big[r\_{t}-Q\_{r\_{t}}(k\,|\,\mathcal{I}\_{t-1})\big], |  | (14) |

where ρk​[u]=u​(k−𝟙​{u≤0})\rho\_{k}[u]=u(k-\mathds{1}\{u\leq 0\}) is the quantile regression “check” loss function (Koenker and Bassett, [1978](#bib.bib36 "Regression quantiles")).

The estimation of ([12](#S2.E12 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) and ([13](#S2.E13 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) proceeds with restricted quantile regression.
When fitting these CAViaR specifications to data, a choice needs to be made for the initial value Qy1​(k|ℐ0)Q\_{y\_{1}}(k\,|\,\mathcal{I}\_{0}).
A simple and reasonable approach is to set Qy1​(k|ℐ0)=Q^y​(k)Q\_{y\_{1}}(k\,|\,\mathcal{I}\_{0})=\hat{Q}\_{y}(k), the corresponding sample quantile.
This choice ensures that all subsequent conditional quantiles will satisfy the non-crossing condition, both in and out of sample.
For instance, in the case of ([12](#S2.E12 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")), the parameter estimates for 𝜽=(ω​(p),ω​(1−p),β,γ)′\bm{\theta}=\big(\omega(p),\omega(1-p),\beta,\gamma\big)^{\prime} are found by solving:

|  |  |  |
| --- | --- | --- |
|  | min𝜽​∑k∈{p,1−p}∑tρk​[yt−Qyt​(k|ℐt−1)]subject to ​{ω​(p)<ω​(1−p),β≥0,γ≥0,\begin{split}&\min\_{{\bm{\theta}}}\sum\_{k\in\{p,1-p\}}\sum\_{t}\rho\_{k}\left[y\_{t}-Q\_{y\_{t}}(k\,|\,\mathcal{I}\_{t-1})\right]\\ &\mbox{subject to }\left\{\begin{array}[]{l}\omega(p)<\omega(1-p),\\ \beta\geq 0,\,\gamma\geq 0,\\ \end{array}\right.\end{split} |  |

with Qy1​(k|ℐ0)=Q^y​(k)Q\_{y\_{1}}(k\,|\,\mathcal{I}\_{0})=\hat{Q}\_{y}(k), for k∈{p,1−p}k\in\{p,1-p\}. Note that the constraints apply only to the model parameters, without involving the data.
The estimation of ([13](#S2.E13 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) follows a similar procedure, with the constraint on γ\gamma replaced by γ+≥0\gamma\_{+}\geq 0 and γ−≥0\gamma\_{-}\geq 0.

With the estimated parameters, the fitted value of st∗=s^t∗​(p){s}\_{t}^{\ast}=\hat{s}\_{t}^{\ast}(p) in ([10](#S2.E10 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) is calculated as

|  |  |  |
| --- | --- | --- |
|  | s^t∗​(p)=Q^yt​(1−p|ℐt−1)−Q^yt​(p|ℐt−1).\hat{s}\_{t}^{\ast}(p)=\hat{Q}\_{y\_{t}}(1-p\,|\,\mathcal{I}\_{t-1})-\hat{Q}\_{y\_{t}}(p\,|\,\mathcal{I}\_{t-1}). |  |

Then, using the fitted location μ^t\hat{\mu}\_{t} and scale numerator s^t∗​(p)\hat{s}\_{t}^{\ast}(p), it is natural to use the unconditional quantiles of
ε^t∗​(p)=(rt−μ^t)/s^t∗​(p)\hat{\varepsilon}\_{t}^{\ast}(p)=(r\_{t}-\hat{\mu}\_{t})/\hat{s}\_{t}^{\ast}(p) as estimates for Fε∗​(p)−1​(τ)F\_{\varepsilon^{\ast}(p)}^{-1}(\tau), since we are not assuming any particular distribution for εt\varepsilon\_{t} in ([7](#S2.E7 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")).
The estimated left-tail τ\tau-quantile of the conditional return distribution is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q^rt​(τ,p|ℐt−1)=μ^t+s^t∗​(p)​F^ε∗​(p)−1​(τ),\hat{Q}\_{r\_{t}}(\tau,p\,|\,\mathcal{I}\_{t-1})=\hat{\mu}\_{t}+\hat{s}\_{t}^{\ast}(p)\hat{F}\_{\varepsilon^{\ast}(p)}^{-1}(\tau), |  | (15) |

for 0<τ≤0.050<\tau\leq 0.05.

### 2.3 Estimating VaR

We estimate the VaR in ([1](#S1.E1 "In 1 Introduction")) based on the left-tail quantile of the conditional return distribution. In our quantile-based framework, the VaR estimate for a given probability level α\alpha is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR^rt​(α,p)=Q^rt​(α,p|ℐt−1),\widehat{\text{VaR}}\_{r\_{t}}(\alpha,p)=\hat{Q}\_{r\_{t}}(\alpha,p\,|\,\mathcal{I}\_{t-1}), |  | (16) |

where Q^rt​(α,p|ℐt−1)\hat{Q}\_{r\_{t}}(\alpha,p\,|\,\mathcal{I}\_{t-1}) is derived from the dynamic quantile estimate in ([15](#S2.E15 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")), evaluated at τ=α\tau=\alpha.

While the VaR estimate in ([16](#S2.E16 "In 2.3 Estimating VaR ‣ 2 Quantile-based modeling")) can be computed for a given value of pp, relying on a single scale-defining quantile level may lead to inefficiencies. Since the seminal work of Pearson and Tukey ([1965](#bib.bib47 "Approximate means and standard deviations based on distances between percentage points of frequency curves")), it has been well understood that using the interval between symmetric tail quantiles to estimate standard deviation is influenced by the skewness and kurtosis of the distribution. Furthermore, as early as Mosteller ([1946](#bib.bib41 "On some useful “inefficient” statistics")), it was suggested that interquantile range-based estimates of standard deviation could be improved by considering multiple quantile pairs. Building on these insights, we extend this principle to VaR estimation by computing estimates across multiple quantile levels and aggregating the results using an averaging scheme.

Specifically, we define a set of scale-defining quantile levels 𝒫\mathcal{P} and compute VaR for each p∈𝒫p\in\mathcal{P}. The final VaR estimate is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR^rt​(α)=1|𝒫|​∑p∈𝒫VaR^rt​(α,p),\widehat{\text{VaR}}\_{r\_{t}}(\alpha)=\frac{1}{|\mathcal{P}|}\sum\_{p\in\mathcal{P}}\widehat{\text{VaR}}\_{r\_{t}}(\alpha,p), |  | (17) |

where |𝒫||\mathcal{P}| denotes the number of quantile levels used. For our implementation, we use the set 𝒫={0.05,0.10,0.15,0.20,0.25}\mathcal{P}=\{0.05,0.10,0.15,0.20,0.25\}. While this choice is somewhat ad hoc, it corresponds to the relatively more robust values reported in Huber and Ronchetti ([2009](#bib.bib31 "Robust statistics"), Exhibit 5.4) for estimating scale using interquantile ranges.

We also considered alternative methods, such as using a single quantile level or aggregating via the median across 𝒫\mathcal{P}. However, simulations indicate that averaging yields greater stability and lower overall estimation error. This approach mitigates fluctuations in tail behavior and enhances out-of-sample performance, particularly for heavy-tailed distributions. A detailed comparison of these methods is provided in Section A of the Supplementary material.

### 2.4 Approximating ES

The ES in ([2](#S1.E2 "In 1 Introduction")) represents the conditional expectation of loss, given that the loss has exceeded the VaR threshold at a specified probability level α\alpha.
As shown by Acerbi and Tasche ([2002](#bib.bib1 "On the coherence of expected shortfall")), among others, ES can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESrt​(α)=1α​∫0αQrt​(τ|ℐt−1)​𝑑τ,\text{ES}\_{r\_{t}}(\alpha)=\frac{1}{\alpha}\int\_{0}^{\alpha}{Q}\_{r\_{t}}(\tau\,|\,\mathcal{I}\_{t-1})\,d\tau, |  | (18) |

where Qrt​(τ|ℐt−1){Q}\_{r\_{t}}(\tau\,|\,\mathcal{I}\_{t-1}) represents the conditional quantile for τ≤α\tau\leq\alpha.

To compute this integral in practice, we approximate it using a sum over NN equally spaced subdivisions between 0 and α\alpha, similar to a Riemann sum approximation:

|  |  |  |
| --- | --- | --- |
|  | ES~rt​(α,p,N)=1N​∑i=1NQ^rt​(τi,p|ℐt−1),\widetilde{\text{ES}}\_{r\_{t}}(\alpha,p,N)=\frac{1}{N}\sum\_{i=1}^{N}\hat{Q}\_{r\_{t}}(\tau\_{i},p\,|\,\mathcal{I}\_{t-1}), |  |

where τi=i​α/N\tau\_{i}=i\alpha/N for i=1,…,Ni=1,\ldots,N, and each Q^rt​(τi,p|ℐt−1)\hat{Q}\_{r\_{t}}(\tau\_{i},p\,|\,\mathcal{I}\_{t-1}) is the corresponding quantile estimate from ([15](#S2.E15 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")).

As with VaR, we compute ES for several values of pp to obtain a more robust estimate. Specifically, for each fixed NN, we take the average ES across different quantile levels pp:

|  |  |  |
| --- | --- | --- |
|  | ES^rt​(α,N)=1|𝒫|​∑p∈𝒫ES~rt​(α,p,N).\widehat{\text{ES}}\_{r\_{t}}(\alpha,N)=\frac{1}{|\mathcal{P}|}\sum\_{p\in\mathcal{P}}\widetilde{\text{ES}}\_{r\_{t}}(\alpha,p,N). |  |

This averaging process reduces estimation errors associated with any single pp, leading to a more efficient and reliable ES estimate.
The order of operations is important: by first approximating the integral over τ\tau before averaging across pp, the quantiles used in each ES~rt​(α,p,N)\widetilde{\text{ES}}\_{r\_{t}}(\alpha,p,N) share a consistent scale structure. Averaging across pp only afterward preserves the internal coherence of each quantile specification and avoids mixing quantiles constructed under differing scale definitions.

Rather than fixing NN a priori, we employ an adaptive selection method. We initialize with N=4N=4 and iteratively increase it, computing ES at each step. The iteration stops when successive averaged ES estimates stabilize within a predefined tolerance level ϵ\epsilon:

|  |  |  |
| --- | --- | --- |
|  | |ES^rt​(α,N)−ES^rt​(α,N−1)|<ϵ,\big|\widehat{\text{ES}}\_{r\_{t}}(\alpha,N)-\widehat{\text{ES}}\_{r\_{t}}(\alpha,N-1)\big|<\epsilon, |  |

where we set ϵ=0.0001\epsilon=0.0001 in our implementation. This ensures sufficient numerical accuracy while avoiding unnecessary computations. The stabilized ES estimate is denoted ES^rt​(α)\widehat{\text{ES}}\_{r\_{t}}(\alpha).

An important advantage of the QbSD approach is its ability to prevent inconsistencies common in tail risk estimation. Specifically, it avoids: (i) quantile crossings, (ii) crossings among ES values at different probability levels, and (iii) crossings between quantiles and their corresponding ES values.
This method ensures valid, well-ordered risk estimates across all probability levels α\alpha, even in the extreme tails of the distribution.

## 3 Simulation experiments

In this section, we investigate the accuracy of the proposed QbSD approach with respect to the one-step-ahead VaR and ES forecasts at probability level α\alpha.
The performance of the QbSD models is evaluated using mean absolute error (MAE) and root mean squared error (RMSE), and compared to several benchmark models, including GARCH and joint VaR-ES models. The analysis also assesses the models’ ability to capture skewness, heavy tails, and leverage effects in financial returns.

### 3.1 Simulation design

The data-generating process (DGP) is the asymmetric power ARCH (APARCH) model of Ding et al. ([1993](#bib.bib18 "A long memory property of stock market returns and a new model")), specified as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=σt​εt,σtδ=ω+β​σt−1δ+γ​(|rt−1|−θ​rt−1)δ,\begin{split}r\_{t}&=\sigma\_{t}\varepsilon\_{t},\\ \sigma\_{t}^{\delta}&=\omega+\beta\sigma\_{t-1}^{\delta}+\gamma(|r\_{t-1}|-\theta r\_{t-1})^{\delta},\end{split} |  | (19) |

where ω,β,γ,δ>0\omega,\beta,\gamma,\delta>0 and −1<θ<1-1<\theta<1. The innovations εt\varepsilon\_{t} follow the skewed tt-distribution of Hansen ([1994](#bib.bib29 "Autoregressive conditional density estimation")).
This model nests several well-known specifications as special cases. In particular, when δ=2\delta=2 and θ=0\theta=0, the model reduces to a standard GARCH model.
When δ=1\delta=1, it becomes the absolute value GARCH model of Taylor:1986 and Schwert ([1990](#bib.bib50 "Stock volatility and the crash of ’87")), which implies direct CAViaR representations for the conditional quantiles (Xiao and Koenker, [2009](#bib.bib76 "Conditional quantile estimation for generalized autoregressive conditional heteroscedasticity models")).
Furthermore, when θ≠0\theta\neq 0, the model implies an asymmetric response of volatility to past returns. When θ>0\theta>0, this asymmetry takes the form of a leverage effect, whereby negative returns have a larger impact on future volatility than positive returns of the same magnitude (Black, [1976](#bib.bib9 "Studies of stock price volatility changes"); Christie, [1982](#bib.bib11 "The stochastic behavior of common stock variances: value, leverage and interest rate effects"); French et al., [1987](#bib.bib24 "Expected stock returns and volatility")).

The density function of the innovation term εt\varepsilon\_{t} appearing in ([19](#S3.E19 "In 3.1 Simulation design ‣ 3 Simulation experiments")) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | fε​(x;v,λ)={b​c​(1+1v−2​(b​x+a1−λ)2)−(v+1)/2, if ​x≤−a/bb​c​(1+1v−2​(b​x+a1+λ)2)−(v+1)/2, if ​x>−a/bf\_{\varepsilon}(x;v,\lambda)=\left\{\begin{array}[]{ll}bc\left(1+\frac{1}{v-2}\left(\frac{bx+a}{1-\lambda}\right)^{2}\right)^{-(v+1)/2},&\mbox{ if }x\leq-a/b\\[8.61108pt] bc\left(1+\frac{1}{v-2}\left(\frac{bx+a}{1+\lambda}\right)^{2}\right)^{-(v+1)/2},&\mbox{ if }x>-a/b\end{array}\right. |  | (20) |

where the constants aa, bb, and cc are themselves defined as

|  |  |  |
| --- | --- | --- |
|  | a=4​λ​c​v−2v−1,b=1+3​λ2−a2,c=Γ​(v+12)π​(v−2)​Γ​(v2),a=4\lambda c\frac{v-2}{v-1},\quad b=\sqrt{1+3\lambda^{2}-a^{2}},\quad c=\frac{\Gamma(\frac{v+1}{2})}{\sqrt{\pi(v-2)}\Gamma(\frac{v}{2})}, |  |

and the parameters v>2v>2 and −1<λ<1-1<\lambda<1 represent the degrees of freedom and the asymmetry of the distribution, respectively.
The skewed tt-distribution has a mean of zero and unit variance.
When λ=0\lambda=0, it reduces to a standardized version of the traditional Student-tt distribution. A positive λ\lambda implies right skewness. Financial returns typically have a higher probability of large negative returns than large positive ones, corresponding to left skewness (λ<0\lambda<0).

The distribution in ([20](#S3.E20 "In 3.1 Simulation design ‣ 3 Simulation experiments")) is piecewise-defined around its mode at x=−a/bx=-a/b, which separates the left and right parts of the density and plays an important role in the derivation of VaR and ES. Jondeau and Rockinger ([2003](#bib.bib32 "Conditional volatility, skewness, and kurtosis: existence, persistence, and comovements")) show that the associated cumulative distribution function (CDF) is defined by

|  |  |  |
| --- | --- | --- |
|  | Fε​(x;v,λ)={(1−λ)​F𝒯​(b​x+a1−λ​vv−2;v), if ​x≤−a/b(1+λ)​F𝒯​(b​x+a1+λ​vv−2;v)−λ, if ​x>−a/bF\_{\varepsilon}(x;v,\lambda)=\left\{\begin{array}[]{ll}(1-\lambda)F\_{\mathcal{T}}\left(\frac{bx+a}{1-\lambda}\sqrt{\frac{v}{v-2}};v\right),&\mbox{ if }x\leq-a/b\\[8.61108pt] (1+\lambda)F\_{\mathcal{T}}\left(\frac{bx+a}{1+\lambda}\sqrt{\frac{v}{v-2}};v\right)-\lambda,&\mbox{ if }x>-a/b\\[8.61108pt] \end{array}\right. |  |

where F𝒯​(x;v)F\_{\mathcal{T}}(x;v) is the CDF of the Student-tt distribution with vv degrees of freedom, and the quantile function of the skewed tt-distribution is given by

|  |  |  |
| --- | --- | --- |
|  | Fε−1​(u;v,λ)={1b​((1−λ)​v−2v​F𝒯−1​(u1−λ;v)−a), if ​u≤1−λ21b​((1+λ)​v−2v​F𝒯−1​(u+λ1+λ;v)−a), if ​u>1−λ2.F\_{\varepsilon}^{-1}(u;v,\lambda)=\left\{\begin{array}[]{ll}\frac{1}{b}\left((1-\lambda)\sqrt{\frac{v-2}{v}}F\_{\mathcal{T}}^{-1}\left(\frac{u}{1-\lambda};v\right)-a\right),&\mbox{ if }u\leq\frac{1-\lambda}{2}\\[8.61108pt] \frac{1}{b}\left((1+\lambda)\sqrt{\frac{v-2}{v}}F\_{\mathcal{T}}^{-1}\left(\frac{u+\lambda}{1+\lambda};v\right)-a\right),&\mbox{ if }u>\frac{1-\lambda}{2}.\\[8.61108pt] \end{array}\right. |  |

Under this DGP, both the VaR and ES of rtr\_{t} are proportional to σt\sigma\_{t}. The true one-step-ahead VaR forecast is
VaRrt+1​(α;v,λ)=σt+1​Fε−1​(α;v,λ)\text{VaR}\_{r\_{t+1}}(\alpha;v,\lambda)=\sigma\_{t+1}F\_{\varepsilon}^{-1}(\alpha;v,\lambda)
and the true one-step-ahead ES forecast is
ESrt+1​(α;v,λ)=σt+1​ESε​(α;v,λ),\text{ES}\_{r\_{t+1}}(\alpha;v,\lambda)=\sigma\_{t+1}\text{ES}\_{\varepsilon}(\alpha;v,\lambda),
where the ES for [Hansen](#bib.bib29 "Autoregressive conditional density estimation")’s ([1994](#bib.bib29 "Autoregressive conditional density estimation")) skewed tt-distribution is given by Patton et al. ([2019](#bib.bib46 "Dynamic semiparametric models for expected shortfall (and Value-at-Risk)")) as333The expression in Appendix B.4 of Patton et al. ([2019](#bib.bib46 "Dynamic semiparametric models for expected shortfall (and Value-at-Risk)")) contains some typos. It can be verified, either analytically or by simulation, that ([21](#S3.E21 "In 3.1 Simulation design ‣ 3 Simulation experiments")) is the correct ES expression for Hansen’s skewed tt-distribution. In the second branch of ([21](#S3.E21 "In 3.1 Simulation design ‣ 3 Simulation experiments")), the parameters are flipped to (v,−λ)(v,-\lambda) (so the constants change to a2,b2a\_{2},b\_{2} accordingly) when evaluating ESε∗\text{ES}^{\ast}\_{\varepsilon}. The prefactor (1−α)/α(1-\alpha)/\alpha converts that right-tail ES at level 1−α1-\alpha back to the desired left-tail level α\alpha.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESε​(α;v,λ)={ESε∗​(α;v,λ), if ​Fε−1​(α;v,λ)≤−a/b1−αα​ESε∗​(1−α;v,−λ), if ​Fε−1​(α;v,λ)>−a/b\text{ES}\_{\varepsilon}(\alpha;v,\lambda)=\left\{\begin{array}[]{ll}\text{ES}^{\ast}\_{\varepsilon}(\alpha;v,\lambda),&\mbox{ if }F\_{\varepsilon}^{-1}(\alpha;v,\lambda)\leq-a/b\\ \frac{1-\alpha}{\alpha}\text{ES}^{\ast}\_{\varepsilon}(1-\alpha;v,-\lambda),&\mbox{ if }F\_{\varepsilon}^{-1}(\alpha;v,\lambda)>-a/b\end{array}\right. |  | (21) |

with

|  |  |  |
| --- | --- | --- |
|  | ESε∗​(α;v,λ)=α~α​(1−λ)​(−ab+1−λb​ES𝒯​(α~;v))\text{ES}^{\ast}\_{\varepsilon}(\alpha;v,\lambda)=\frac{\tilde{\alpha}}{\alpha}(1-\lambda)\Big(-\frac{a}{b}+\frac{1-\lambda}{b}\text{ES}\_{\mathcal{T}}(\tilde{\alpha};v)\Big) |  |

and

|  |  |  |
| --- | --- | --- |
|  | α~=Fε​(b1−λ​(Fε−1​(α;v,λ)+ab);v,0).\tilde{\alpha}=F\_{\varepsilon}\bigg(\frac{b}{1-\lambda}\Big(F\_{\varepsilon}^{-1}(\alpha;v,\lambda)+\frac{a}{b}\Big);v,0\bigg). |  |

Here ES𝒯​(α;v)\text{ES}\_{\mathcal{T}}(\alpha;v) is the ES for a Student-tt distribution, standardized to have unit variance, given by

|  |  |  |
| --- | --- | --- |
|  | ES𝒯​(α;v)=−1α​f𝒯​(qα;v)​(v+qα2v−1)​v−2v,\text{ES}\_{\mathcal{T}}(\alpha;v)=-\frac{1}{\alpha}f\_{\mathcal{T}}(q\_{\alpha};v)\Big(\frac{v+q\_{\alpha}^{2}}{v-1}\Big)\sqrt{\frac{v-2}{v}}, |  |

where f𝒯​(x;v)f\_{\mathcal{T}}(x;v) and qα=F𝒯−1​(α;v)q\_{\alpha}=F\_{\mathcal{T}}^{-1}(\alpha;v) are, respectively, the density and α\alpha-quantile of the Student-tt distribution with vv degrees of freedom (Broda and Paolella, [2011](#bib.bib10 "Expected shortfall for distributions in finance"); Dobrev et al., [2017](#bib.bib19 "Accurate evaluation of expected shortfall for linear portfolios with elliptically distributed risk factors")).

In the DGP outlined in ([19](#S3.E19 "In 3.1 Simulation design ‣ 3 Simulation experiments")), we set the parameters as follows: ω=0.05\omega=0.05, β=0.85\beta=0.85, γ=0.10\gamma=0.10, and δ=1.5\delta=1.5, while allowing θ\theta to take values in {0,0.5}\{0,0.5\}. For the skewed tt-distribution in ([20](#S3.E20 "In 3.1 Simulation design ‣ 3 Simulation experiments")), we select v∈{5,20}v\in\{5,20\} to represent different tail thicknesses, with v=5v=5 corresponding to heavy tails and v=20v=20 representing thinner tails. We use λ∈{0,−0.5}\lambda\in\{0,-0.5\} to capture different levels of skewness, with λ=0\lambda=0 indicating no skewness and λ=−0.5\lambda=-0.5 implying left skewness.
The sample size is set to T=1250T=1250, which corresponds to roughly five years of daily returns and matches the primary rolling-window length used in our empirical application.
The results presented in the main text focus on this baseline case; additional simulations for T∈{250,2500}T\in\{250,2500\} are reported in Section B of the Supplementary material.
We consider three probability levels for the forecasts: α∈{0.01,0.025,0.05}\alpha\in\{0.01,0.025,0.05\}. The choice of δ=1.5\delta=1.5 allows us to explore a setting where the power parameter lies between the standard GARCH model (δ=2\delta=2) and the absolute value GARCH model (δ=1\delta=1).444This value of δ\delta is close to the estimate of 1.431.43 reported by Ding et al. ([1993](#bib.bib18 "A long memory property of stock market returns and a new model")) in their study of S&P 500 returns.
We set θ∈{0,0.5}\theta\in\{0,0.5\} to explore the role of asymmetry in volatility dynamics. As noted earlier, θ=0\theta=0 yields a symmetric response, while θ=0.5\theta=0.5 introduces a leverage effect.

For each DGP configuration, we evaluate the forecasting accuracy by computing the MAE and the RMSE across all 1,000 generated return series. These metrics allow us to compare the performance of the models in capturing the true one-step-ahead VaR and ES forecasts.
In our simulations, we consider the QbSD model with the two global CAViaR specifications in ([12](#S2.E12 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")) and ([13](#S2.E13 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")).
Consistent with the simulation DGP in ([19](#S3.E19 "In 3.1 Simulation design ‣ 3 Simulation experiments")), all QbSD and benchmark models, presented next, assume a zero location for returns.
This assumption simplifies the modeling process, allowing us to focus on volatility and tail risk dynamics.

### 3.2 Benchmark models

To assess the performance of our QbSD models, we compare them with several established models commonly used in financial risk forecasting.
The benchmarks include the VaR and ES forecasts from the standard GARCH model, the asymmetric GJR-GARCH model (Glosten et al., [1993](#bib.bib27 "On the relation between the expected value and the volatility of the nominal excess return on stocks")), and the EGARCH model (Nelson, [1991](#bib.bib43 "Conditional heteroskedasticity in asset returns: a new approach")), each with normal innovations. Additionally, for the GARCH and GJR-GARCH models, we consider alternative distributional assumptions for the innovations, including the Student-tt distribution and [Hansen](#bib.bib29 "Autoregressive conditional density estimation")’s ([1994](#bib.bib29 "Autoregressive conditional density estimation")) more general
skewed tt-distribution.555We consider the EGARCH model only with normal innovations, as it tends to exhibit instability when applied with tt-distributed errors (Nelson, [1991](#bib.bib43 "Conditional heteroskedasticity in asset returns: a new approach"), p. 365).

We also include the joint VaR-ES model proposed by Taylor ([2019](#bib.bib52 "Forecasting value at risk and expected shortfall using a semiparametric approach based on the asymmetric Laplace distribution")), which employs a pseudo-maximum likelihood estimation approach based on the AL density function for the joint estimation of VaR and ES. The conditional AL density function is given by

|  |  |  |
| --- | --- | --- |
|  | f​(rt)=(α−1)ESt​exp⁡((rt−VaRt)​(α−𝟙​{rt≤VaRt})α​ESt),f(r\_{t})=\frac{(\alpha-1)}{\text{ES}\_{t}}\exp\left(\frac{\left(r\_{t}-\text{VaR}\_{t}\right)\left(\alpha-\mathds{1}\{r\_{t}\leq\text{VaR}\_{t}\}\right)}{\alpha\text{ES}\_{t}}\right), |  |

where VaRt\text{VaR}\_{t} is modeled using either the SAV or AS CAViaR specifications from expressions ([3](#S1.E3 "In 1 Introduction")) and ([4](#S1.E4 "In 1 Introduction")), with yty\_{t} replaced by rtr\_{t} under the mean zero assumption. The complete model includes two alternative specifications for the dynamics of the ES:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESt=(1+exp⁡(γ0))​VaRt\text{ES}\_{t}=\left(1+\exp(\gamma\_{0})\right)\text{VaR}\_{t} |  | (22) |

or

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESt=VaRt−xt,\text{ES}\_{t}=\text{VaR}\_{t}-x\_{t}, |  | (23) |

where xtx\_{t} follows a dynamic updating process:

|  |  |  |
| --- | --- | --- |
|  | xt={γ0+γ1​(VaRt−1−rt−1)+γ2​xt−1,if​rt−1≤VaRt−1xt−1,otherwise.x\_{t}=\begin{cases}\gamma\_{0}+\gamma\_{1}(\text{VaR}\_{t-1}-r\_{t-1})+\gamma\_{2}x\_{t-1},&\text{if}\;r\_{t-1}\leq\text{VaR}\_{t-1}\\ x\_{t-1},&\text{otherwise}.\end{cases} |  |

This formulation provides a smooth adjustment to the magnitude of exceedances beyond the VaR, dynamically updating based on past returns and exceedances.

To differentiate between the two AL-based specifications, we use the notation “ALMult.\text{AL}\_{\text{Mult.}}” for the multiplicative version in ([22](#S3.E22 "In 3.2 Benchmark models ‣ 3 Simulation experiments")), where ES is modeled as a multiple of VaR, and “ALAR\text{AL}\_{\text{AR}}” for the autoregressive version in ([23](#S3.E23 "In 3.2 Benchmark models ‣ 3 Simulation experiments")). For these AL-based models, we further indicate the choice of VaR specification using the suffixes “-SAV” for the SAV CAViaR model in ([3](#S1.E3 "In 1 Introduction")) and “-AS” for the AS CAViaR model in ([4](#S1.E4 "In 1 Introduction")). For example, ALMult.\text{AL}\_{\text{Mult.}}-SAV refers to the multiplicative AL-based model with the SAV CAViaR specification.
The QbSD models, in contrast, rely on global CAViaR specifications, where the scale dynamics are shared across quantiles. Here, the suffix “-gSAV” denotes the global SAV CAViaR specification ([12](#S2.E12 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")), while “-gAS” refers to the global AS CAViaR specification ([13](#S2.E13 "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling")). For example, QbSD-gSAV refers to the QbSD model with the global SAV CAViaR specification.

In addition to the quantile-based models, we also consider the one-factor GAS model proposed by Patton et al. ([2019](#bib.bib46 "Dynamic semiparametric models for expected shortfall (and Value-at-Risk)")), which provides an alternative framework for jointly modeling VaR and ES.
This model is based on the following member of the Fissler and Ziegel ([2016](#bib.bib23 "Higher order elicitability and Osband’s principle")) class of loss functions:

|  |  |  |
| --- | --- | --- |
|  | LFZ0​(rt,VaRt,ESt)=−1α​ESt​𝟙​{rt≤VaRt}​(VaRt−rt)+VaRtESt+log⁡(−ESt)−1.L\_{\text{FZ0}}(r\_{t},\text{VaR}\_{t},\text{ES}\_{t})=-\frac{1}{\alpha\text{ES}\_{t}}\mathds{1}\{r\_{t}\leq\text{VaR}\_{t}\}(\text{VaR}\_{t}-r\_{t})+\frac{\text{VaR}\_{t}}{\text{ES}\_{t}}+\log(-\text{ES}\_{t})-1. |  |

The FZ0\text{FZ}\_{0} loss function is strictly consistent for the pair (VaR, ES). Although the loss itself is not homogeneous of degree zero—due to the log⁡(−ESt)\log(-\text{ES}\_{t}) term—the differences in loss values between competing forecasts are. This ensures that forecast rankings based on average loss are invariant to positive scaling of both returns and risk measures.

The joint specification for VaR and ES is

|  |  |  |
| --- | --- | --- |
|  | VaRt=ζ​exp⁡(κt),ESt=ξ​exp⁡(κt),with​ξ<ζ<0,\text{VaR}\_{t}=\zeta\exp(\kappa\_{t}),\quad\text{ES}\_{t}=\xi\exp(\kappa\_{t}),\quad\text{with}\ \xi<\zeta<0, |  |

where the common factor κt\kappa\_{t} evolves dynamically as

|  |  |  |
| --- | --- | --- |
|  | κt=ω+β​κt−1+γ​gt−1,\kappa\_{t}=\omega+\beta\kappa\_{t-1}+\gamma g\_{t-1}, |  |

and the score function gtg\_{t}, derived from the FZ0 loss function, is given by

|  |  |  |
| --- | --- | --- |
|  | gt=−1ESt​(1α​𝟙​{rt≤VaRt}​rt−ESt).g\_{t}=-\frac{1}{\text{ES}\_{t}}\left(\frac{1}{\alpha}\mathds{1}\{r\_{t}\leq\text{VaR}\_{t}\}r\_{t}-\text{ES}\_{t}\right). |  |

This approach dynamically updates both VaR and ES based on the information in past losses.666Since the Hessian of the FZ0 loss is constant, the scaling matrix in the GAS framework of Creal et al. ([2013](#bib.bib14 "GENERALIZED autoregressive score models with applications")) can be set to one without loss of generality. This simplifies estimation while preserving the model’s essential dynamics. Following Patton et al. ([2019](#bib.bib46 "Dynamic semiparametric models for expected shortfall (and Value-at-Risk)")), we set ω=0\omega=0 for identification and estimate the model by minimizing the average FZ0 loss.

These competing models offer a range of benchmarks for evaluating the forecasting performance of the QbSD models. In the next section, we present the simulation results and assess how well each model captures key features of financial returns across the various DGP configurations.
It is interesting to note that none of the models exactly matches the DGP in ([19](#S3.E19 "In 3.1 Simulation design ‣ 3 Simulation experiments")), which makes the forecasting task more challenging and offers a stricter test of adaptability.

### 3.3 Numerical results

This section presents the forecasting results for the QbSD and benchmark models across the simulation scenarios. Tables 1–4 report out-of-sample one-step-ahead VaR and ES accuracy (MAE and RMSE) under symmetric and asymmetric volatility dynamics.

Table 1 reports VaR forecast accuracy with no leverage (symmetric volatility dynamics). Parametric GARCH-family models with correctly specified innovations (Student-tt under symmetry; skew-tt under left skew) lead across configurations. With symmetric innovations (v=20,λ=0v=20,\lambda=0), GARCH/GJR with Student-tt is best across α\alpha (e.g., MAE 0.071,0.054,0.0440.071,0.054,0.044; RMSE 0.095,0.073,0.0590.095,0.073,0.059), while QbSD-gSAV is competitive but not top. With left skewness (v=20,λ=−0.5v=20,\lambda=-0.5), skew-tt dominates (e.g., GJR-skew-tt MAE 0.098,0.068,0.0490.098,0.068,0.049; RMSE 0.132,0.093,0.0690.132,0.093,0.069), with only minor differences between GARCH and GJR. Under heavier tails (v=5v=5), the pattern persists: when λ=0\lambda=0, GARCH/GJR-tt remains best (MAE 0.103,0.068,0.0500.103,0.068,0.050; RMSE 0.143,0.097,0.0720.143,0.097,0.072); when λ=−0.5\lambda=-0.5, GJR-GARCH with skew-tt leads (MAE 0.145,0.084,0.0540.145,0.084,0.054; RMSE 0.213,0.134,0.0930.213,0.134,0.093). Across all blocks, QbSD-gSAV improves on AL-based and GAS alternatives but trails the best-specified GARCH variants.

Turning to ES under symmetric volatility (Table 2), the same ordering emerges: matching the innovation distribution to the DGP is pivotal. In the symmetric case (v=20,λ=0v=20,\lambda=0), GARCH/GJR-tt attains the lowest errors (MAE 0.100,0.075,0.0600.100,0.075,0.060; RMSE 0.129,0.099,0.0810.129,0.099,0.081). Introducing left skewness (v=20,λ=−0.5v=20,\lambda=-0.5) shifts the frontier to skew-tt (GJR-skew-tt MAE 0.146,0.105,0.0800.146,0.105,0.080; RMSE 0.191,0.140,0.1080.191,0.140,0.108). Under heavier tails (v=5v=5), Student-tt remains best when λ=0\lambda=0 (MAE 0.180,0.118,0.0860.180,0.118,0.086; RMSE 0.241,0.162,0.1200.241,0.162,0.120), while skew-tt variants lead for λ=−0.5\lambda=-0.5 (e.g., GJR-skew-tt MAE 0.117,0.173,0.1170.117,0.173,0.117; RMSE 0.174,0.247,0.3830.174,0.247,0.383). AL-based and GAS models are consistently less accurate.

Table 3 reports VaR accuracy with leverage (θ=0.5\theta=0.5). QbSD-gAS delivers the lowest errors in most configurations featuring skewness and/or heavy tails. For example, at v=20,λ=−0.5v=20,\lambda=-0.5, it is best across α\alpha (MAE 0.172,0.125,0.0960.172,0.125,0.096; RMSE 0.238,0.183,0.1380.238,0.183,0.138). In the heavy-tailed but symmetric case (v=5,λ=0v=5,\lambda=0), QbSD-gAS is generally strongest, with EGARCH edging it at α=2.5%\alpha=2.5\% (MAE 0.1050.105 vs. 0.1100.110). Under heavy tails with left skewness (v=5,λ=−0.5v=5,\lambda=-0.5), GJR-skew-tt attains the lowest MAE (0.233,0.152,0.1080.233,0.152,0.108), with QbSD-gAS close behind. A notable exception is the thin-tailed, symmetric DGP (v=20,λ=0v=20,\lambda=0), where EGARCH dominates (MAE 0.105,0.075,0.0620.105,0.075,0.062; RMSE 0.148,0.107,0.0860.148,0.107,0.086).

Table 4 presents ES accuracy with leverage. QbSD-gAS leads in most configurations. It is best across α\alpha at v=20,λ=−0.5v=20,\lambda=-0.5 (MAE 0.235,0.174,0.1400.235,0.174,0.140; RMSE 0.314,0.238,0.1950.314,0.238,0.195) and at v=5,λ=0v=5,\lambda=0 (MAE 0.292,0.186,0.1360.292,0.186,0.136). In the heavy-tailed, left-skewed case v=5,λ=−0.5v=5,\lambda=-0.5, GJR-skew-tt has the edge (MAE 0.388,0.263,0.1910.388,0.263,0.191; RMSE 0.526,0.352,0.2560.526,0.352,0.256). For the thin-tailed symmetric DGP v=20,λ=0v=20,\lambda=0, EGARCH is competitive and surpasses QbSD-gAS at higher α\alpha (e.g., MAE 0.113,0.0860.113,0.086 and RMSE 0.157,0.1220.157,0.122 at 2.5%2.5\% and 5%5\%, vs. QbSD-gAS 0.125,0.1030.125,0.103 and 0.165,0.1370.165,0.137); QbSD-gAS is slightly better at 1%1\% (MAE 0.1650.165 vs. 0.1670.167).

Overall, the evidence suggests a clear division: when volatility responds symmetrically and the innovation distribution is correctly specified (e.g., appropriately heavy-tailed or skewed), parametric GARCH variants set the benchmark for VaR and ES; once leverage/asymmetry matters, allowing asymmetric-slope (gAS) scale dynamics is pivotal—the proposed QbSD-gAS specification is typically strongest, particularly for ES, with EGARCH competitive and occasionally best in thin-tailed symmetric settings. Across these scenarios, AL-based and GAS models remain less accurate. We next examine whether these patterns carry over to international stock index returns.

## 4 Empirical Application

We evaluate one-day-ahead VaR and ES forecasts for the daily log returns of the S&P 500, DJIA, NASDAQ, EURO STOXX 50, FTSE 100, DAX, CAC 40, and TSX stock indices. The daily adjusted closing prices for these indices were obtained from Yahoo Finance, spanning October 4, 2002, to February 2, 2024, across indices. Due to differences in trading days and data availability, the number of observations initially varies across the series.

To ensure comparability across stock indices, we standardized the sample size to match the index with the shortest available data. Specifically, the EURO STOXX 50 has the shortest sample, starting on October 21, 2002, and containing 5,357 daily observations, ending on February 2, 2024. For consistency, we truncated the data for indices with longer samples by counting backward from February 2, 2024, to retain exactly 5,357 observations for each index. This adjustment implies the following starting dates: October 22, 2002, for the S&P 500, DJIA, and NASDAQ; October 21, 2002, for the EURO STOXX 50; November 18, 2002, for the FTSE 100; January 3, 2003, for the DAX; February 27, 2003, for the CAC 40; and October 4, 2002, for the TSX. As returns are calculated as first differences of log prices, this sample size yields 5,356 daily return observations for all indices.

Figure 1 illustrates the time series of daily log returns (in percentages) for the S&P 500, DJIA, NASDAQ, and EURO STOXX 50 indices, each exhibiting notable spikes in volatility during significant economic events such as the 2008 financial crisis and the COVID-19 pandemic. Figure 2 shows the daily log returns for the FTSE 100, DAX, CAC 40, and TSX indices, which similarly exhibit heightened volatility during periods of financial stress.

We use a rolling window of R=1250R=1250 estimation observations (approximately five trading years) to produce one-day-ahead forecasts for VaR and ES. This choice balances sampling variability against responsiveness to structural change.
Model parameters are estimated using the most recent 1,250 observations, and forecasts are updated daily as the window moves through the sample period. Given the common sample of 5,356 daily returns, this setup leaves an out-of-sample evaluation period of 4,106 observations. We forecast VaR and ES at probability levels of 1%, 2.5%, and 5%. The 1% and 5% levels are widely used in the literature, whereas the 2.5% level corresponds to the regulatory standard for ES adopted under Basel III. We also examined alternative rolling-window sizes of R=250R=250 and R=2500R=2500. To maintain focus in the main text, we present results for the 1,250-observation window, while these alternative specifications appear in Section C of the Supplementary material.

We evaluate a total of twenty-eight competing risk models for forecasting VaR and ES, including: (i) fourteen GARCH-type models (GARCH and GJR-GARCH with normal, Student-tt, and [Hansen](#bib.bib29 "Autoregressive conditional density estimation") skew-tt innovations under zero or AR(1) conditional means, plus EGARCH with normal innovations under zero or AR(1) means), (ii) two GAS variants with zero and AR(1) means (Patton et al., [2019](#bib.bib46 "Dynamic semiparametric models for expected shortfall (and Value-at-Risk)")), (iii) eight AL-based models following Taylor ([2019](#bib.bib52 "Forecasting value at risk and expected shortfall using a semiparametric approach based on the asymmetric Laplace distribution")) (SAV and AS CAViaR for VaR dynamics, multiplicative and autoregressive specifications for ES dynamics, each under zero or AR(1) means), and (iv) four QbSD models (gSAV and gAS scale dynamics under zero or QAR(1) conditional medians).

In the following tables, we use the prefixes “AR-” and “QAR-” to denote an AR(1) conditional mean and a QAR(1) conditional median, respectively; models without a prefix assume a zero conditional location.

### 4.1 Evaluation of VaR forecasts

We evaluate the accuracy of VaR forecasts using the model confidence set (MCS) procedure of Hansen et al. ([2011](#bib.bib30 "The model confidence set")), which identifies a subset of models that are not significantly outperformed at a given confidence level. The MCS framework is particularly useful in a multi-model comparison setting, as it does not require selecting a single best model but instead acknowledges model uncertainty by retaining all models that cannot be statistically eliminated.

Following [Hansen et al.](#bib.bib30 "The model confidence set")’s ([2011](#bib.bib30 "The model confidence set")) suggestion, we apply the range-based procedure using the maximum absolute tt-statistic, which iteratively removes the model with the largest loss difference relative to the others until only models that cannot be statistically distinguished from the best-performing ones remain. The final MCS consists of models that survive this elimination process at the chosen confidence level.777Specifically, we base the MCS on the TR,ℳT\_{R,\mathcal{M}} test statistic developed by Hansen et al. ([2011](#bib.bib30 "The model confidence set"), Section 3.1.2) and compute it with 1,000 bootstrap iterations using the R package ‘MCS’ (Bernardi and Catania, [2018](#bib.bib7 "The model confidence set package for R")).

The test statistic is computed using the quantile score loss, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(rt+1,VaRt+1)=(rt+1−VaRt+1)​(α−𝟙​{rt+1≤VaRt+1}),S(r\_{t+1},\text{VaR}\_{t+1})=\left(r\_{t+1}-\text{VaR}\_{t+1}\right)\left(\alpha-\mathds{1}\left\{r\_{t+1}\leq\text{VaR}\_{t+1}\right\}\right), |  | (24) |

where rt+1r\_{t+1} is the realized return and VaRt+1\text{VaR}\_{t+1} is the predicted VaR at a given probability level α\alpha.
This loss function is asymmetric and penalizes underpredictions more heavily than overpredictions, making it well suited to the evaluation of downside risk.

Tables 5–7 present the MCS results for 1%, 2.5%, and 5% VaR forecasts across the eight international stock indices. Models excluded from the 90% MCS (ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\*}) for a given index are left blank.
The remaining models are ranked by their average quantile score tt-statistics; the “#” column counts the number of indices for which a model remains in the MCS, while the “Avg. rank” and “Final rank” summarize overall performance.

For the 1% tail (Table 5), QbSD-gAS attains the best overall rank and appears in the MCS for all eight indices; its closest competitors are GARCH variants with skew-tt innovations (GJR-GARCH-skew-tt, GARCH-skew-tt), followed by GJR-GARCH-tt, while AL-based specifications generally trail.
At 2.5% (Table 6), QbSD-gAS again ranks first overall (in the MCS for all eight indices), with AL-based models featuring AS dynamics (ALMult.{}\_{\text{Mult.}}-AS, AR-ALMult.{}\_{\text{Mult.}}-AS) close behind; among GARCH-type models, skew-tt remains the most competitive and EGARCH sits in the upper middle of the table.
By 5% (Table 7), QbSD-gAS still leads, EGARCH moves into second place, ALMult.{}\_{\text{Mult.}}-AS and the QAR-driven QbSD-gAS (QAR-QbSD-gAS) remain prominent, and skew-tt GARCH variants continue to perform well.

Across probability levels, the symmetric QbSD specification (QbSD-gSAV) underperforms its asymmetric counterpart, underscoring the value of allowing an asymmetric scale response in practice. Within the GARCH family, skew-tt innovations generally improve performance at tighter tails (1% and 2.5%), whereas the strong showing of EGARCH at 5% suggests that volatility asymmetry can partly compensate when attention shifts away from the far tail.

While these results provide important insights into tail-risk quantile prediction, a fuller assessment requires joint evaluation of VaR and ES, which we consider next.

### 4.2 Joint evaluation of VaR and ES forecasts

To jointly evaluate VaR and ES forecasts, we use the AL log score proposed by Taylor ([2019](#bib.bib52 "Forecasting value at risk and expected shortfall using a semiparametric approach based on the asymmetric Laplace distribution")). This scoring rule is specifically designed to assess both VaR and ES, reflecting their joint elicitability. The AL log score is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(rt+1,μt+1,VaRt+1,ESt+1)=\displaystyle S(r\_{t+1},\mu\_{t+1},\text{VaR}\_{t+1},\text{ES}\_{t+1})= | −log⁡(α−1ESt+1−μt+1)\displaystyle-\log\left(\frac{\alpha-1}{\text{ES}\_{t+1}-\mu\_{t+1}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(rt+1−VaRt+1)​(α−𝟙​{rt+1≤VaRt+1})α​(ESt+1−μt+1),\displaystyle-\frac{(r\_{t+1}-\text{VaR}\_{t+1})(\alpha-\mathds{1}\{r\_{t+1}\leq\text{VaR}\_{t+1}\})}{\alpha(\text{ES}\_{t+1}-\mu\_{t+1})}, |  | (25) |

where μt+1\mu\_{t+1} is the model’s conditional mean and ESt+1<μt+1\text{ES}\_{t+1}<\mu\_{t+1} is required.
This proper scoring rule penalizes both the incidence and severity of forecast errors in the left tail, encouraging accurate joint predictions of VaR and ES.

Tables 8–10 summarize the MCS rankings under AL log scores. At the 1% tail (Table 8), the best overall performer is AR-GJR-GARCH-skew-tt, with QbSD-gAS a close second; both appear in the MCS for all eight indices. Other skew-tt GARCH variants (GARCH-skew-tt, GJR-GARCH-skew-tt) are also highly competitive, whereas AL-based specifications sit further down the table.
At 2.5% (Table 9), leadership shifts to QbSD-gAS, which ranks first overall and is included in the MCS for all eight indices. AL-based models with asymmetric VaR dynamics (AS CAViaR), namely ALMult.{}\_{\text{Mult.}}-AS and AR-ALMult.{}\_{\text{Mult.}}-AS, are close followers, with skew-tt GARCH entries forming the next tier.
By 5% (Table 10), QbSD-gAS again takes the top spot (in the MCS for all indices), followed by ALAR{}\_{\text{AR}}-AS and ALMult.{}\_{\text{Mult.}}-AS; the QAR-driven QAR-QbSD-gAS also ranks near the front. Skew-tt GARCH specifications remain competitive, while EGARCH occupies an upper-mid-table position.

Taken together, these results indicate that joint VaR-ES forecasting favors models that accommodate asymmetric tail dynamics. QbSD-gAS is consistently among the best across tail levels and leads at 2.5% and 5%, while skew-tt GARCH variants are particularly strong at the most extreme tail (1%). AL-based models with AS CAViaR VaR dynamics provide robust competitors at 2.5% and 5%, reinforcing the importance of allowing asymmetry in the VaR/ES system.

## 5 Conclusion

This paper introduced QbSD for forecasting VaR and ES: a semiparametric, distribution-free approach that models conditional scale via restricted quantile regression and accommodates skewness, heavy tails, and leverage—features that intensify during periods of market stress.

Across simulations and international equity indices, a consistent picture emerges. In simulation designs without leverage, parametric GARCH models with heavy-tailed or skewed innovation distributions set a high benchmark for both VaR and ES; Student-tt and skew-tt specifications are especially effective.
With leverage, allowing asymmetric-slope quantile dynamics is pivotal: QbSD-gAS is frequently among the best, particularly for ES, while for VaR, EGARCH and skew-tt GJR-GARCH can also be highly competitive depending on the tail level and distributional setting.

In the empirical evaluation with a five-year rolling window (R=1250R=1250), QbSD-gAS is the clearest overall performer for VaR under quantile-score MCS: it attains the best average rank at 1%, 2.5%, and 5% across the eight indices, with skew-tt GARCH variants forming the next tier and EGARCH rising near the front at 5%. When VaR and ES are assessed jointly via AL log scores, performance at the most extreme tail (1%) tilts toward skew-tt GARCH (AR-GJR-GARCH-skew-tt), with QbSD-gAS a close second; at 2.5% and 5%, QbSD-gAS leads, and AL-based specifications with AS CAViaR VaR dynamics (both multiplicative and autoregressive ES linkages) are robust followers.

Two practical lessons follow.
First, asymmetry helps—but not all asymmetries are equal: QbSD-gAS delivers the most consistent improvements; skew-tt innovations help when empirical skewness is material; and EGARCH’s volatility asymmetry tends to help when return innovations are near-symmetric with relatively light tails, whereas GJR’s benefits appear mainly when combined with skew-tt under skewed, heavy-tailed conditions.
Second, the preferred specification varies with the tail probability and the evaluation target: skew-tt GARCH may perform well at the far tail (1%) under joint VaR-ES scoring, whereas QbSD-gAS provides the most consistent gains across tail levels for VaR and remains among the leaders at 2.5% and 5% in the joint evaluation.

Overall, QbSD—especially with asymmetric-slope (gAS) quantile dynamics—offers a robust, flexible addition to the risk-management toolkit. Its distribution-free construction, strong showing under leverage and during turbulent periods, and straightforward extensibility to log-location-scale settings (e.g., strictly positive losses such as credit losses and insurance claims) make it well suited for practical deployment.

## Acknowledgments

We thank the editor, Dick van Dijk, the associate editor, and an anonymous reviewer for their constructive feedback and insightful suggestions.
Richard Luger is supported in part by funding from the Social Sciences and Humanities Research Council of Canada.

## Data and code availability

The data and code needed to reproduce the results presented in this paper are available at https://github.com/richardluger/QbSD.
The code is written in R with C++ functions for computational efficiency.

## References

* C. Acerbi and D. Tasche (2002)
  On the coherence of expected shortfall.
  Journal of Banking & Finance 26 (7),  pp. 1487–1503.
  Cited by: [§1](#S1.p2.3 "1 Introduction"),
  [§1](#S1.p9.1 "1 Introduction"),
  [§2.4](#S2.SS4.p1.1 "2.4 Approximating ES ‣ 2 Quantile-based modeling").
* S. Alizadeh, M. W. Brandt, and F. X. Diebold (2002)
  Range-based estimation of stochastic volatility models.
  Journal of Finance 57 (3),  pp. 1047–1091.
  Cited by: [footnote 2](#footnote2a "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* P. Artzner, F. Delbaen, J. Eber, and D. Heath (1999)
  Coherent measures of risk.
  Mathematical Finance 9 (3),  pp. 203–228.
  Cited by: [§1](#S1.p2.3 "1 Introduction").
* Basel Committee on Banking Supervision (2019)
  Minimum capital requirements for market risk.
  BCBS Final Standard
  Technical Report BIS/BCBS 457, Bank for International Settlements, Basel.
  External Links: [Link](https://www.bis.org/bcbs/publ/d457.pdf)
  Cited by: [§1](#S1.p2.4 "1 Introduction").
* M. Bernardi and L. Catania (2018)
  The model confidence set package for R.
  International Journal of Computational Economics and Econometrics 8 (2),  pp. 144–158.
  Cited by: [footnote 7](#footnote7 "In 4.1 Evaluation of VaR forecasts ‣ 4 Empirical Application").
* F. Black (1976)
  Studies of stock price volatility changes.
  In Proceedings of the American Statistical Association, Business and Economic Statistics Section,
   pp. 177–181.
  Cited by: [§3.1](#S3.SS1.p1.9 "3.1 Simulation design ‣ 3 Simulation experiments").
* S.A. Broda and M.S. Paolella (2011)
  Expected shortfall for distributions in finance.
  In Statistical Tools for Finance and Insurance, P. Cizek, W.K. Härdle, and R. Weron (Eds.),
  Cited by: [§3.1](#S3.SS1.p4.12 "3.1 Simulation design ‣ 3 Simulation experiments").
* A. A. Christie (1982)
  The stochastic behavior of common stock variances: value, leverage and interest rate effects.
  Journal of Financial Economics 10 (4),  pp. 407–432.
  Cited by: [§3.1](#S3.SS1.p1.9 "3.1 Simulation design ‣ 3 Simulation experiments").
* P. Christoffersen (2012)
  Elements of financial risk management.
  2nd edition, Academic Press, Amsterdam.
  Cited by: [§1](#S1.p10.1 "1 Introduction").
* D. Creal, S. J. Koopman, and A. Lucas (2013)
  GENERALIZED autoregressive score models with applications.
  Journal of Applied Econometrics 28 (5),  pp. 777–795.
  Cited by: [§1](#S1.p6.1 "1 Introduction"),
  [footnote 6](#footnote6 "In 3.2 Benchmark models ‣ 3 Simulation experiments").
* Z. Ding, C. W. J. Granger, and R. F. Engle (1993)
  A long memory property of stock market returns and a new model.
  Journal of Empirical Finance 1 (1),  pp. 83–106.
  Cited by: [§3.1](#S3.SS1.p1.10 "3.1 Simulation design ‣ 3 Simulation experiments"),
  [footnote 4](#footnote4 "In 3.1 Simulation design ‣ 3 Simulation experiments").
* D. Dobrev, T. D. Nesmith, and D. H. Oh (2017)
  Accurate evaluation of expected shortfall for linear portfolios with elliptically distributed risk factors.
  Journal of Risk and Financial Management 10 (1),  pp. Article 5.
  Cited by: [§3.1](#S3.SS1.p4.12 "3.1 Simulation design ‣ 3 Simulation experiments").
* P. Embrechts, A. J. McNeil, and D. Straumann (2002)
  Correlation and dependence in risk management: properties and pitfalls.
  In Risk Management: Value at Risk and Beyond, M.A.H. Dempster (Ed.),
   pp. 176–223.
  Cited by: [§1](#S1.p1.8 "1 Introduction").
* R. F. Engle and S. Manganelli (2004)
  CAViaR: conditional autoregressive Value at Risk by regression quantiles.
  Journal of Business & Economic Statistics 22 (4),  pp. 367–381.
  Cited by: [§1](#S1.p4.2 "1 Introduction").
* R. F. Engle and V. K. Ng (1993)
  Measuring and testing the impact of news on volatility.
  Journal of Finance 48 (5),  pp. 1749–1778.
  Cited by: [§2.2](#S2.SS2.p5.11 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* T. Fissler and J.F. Ziegel (2016)
  Higher order elicitability and Osband’s principle.
  Annals of Statistics 44 (4),  pp. 1680–1707.
  Cited by: [§1](#S1.p5.1 "1 Introduction"),
  [§1](#S1.p6.1 "1 Introduction"),
  [§3.2](#S3.SS2.p4.3 "3.2 Benchmark models ‣ 3 Simulation experiments").
* K. R. French, G. W. Schwert, and R. F. Stambaugh (1987)
  Expected stock returns and volatility.
  Journal of Financial Economics 19 (1),  pp. 3–29.
  Cited by: [§3.1](#S3.SS1.p1.9 "3.1 Simulation design ‣ 3 Simulation experiments").
* M. B. Garman and M. J. Klass (1980)
  On the estimation of security price volatilities from historical data.
  Journal of Business 53 (1),  pp. 67–78.
  Cited by: [footnote 2](#footnote2a "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* E. Ghysels (2014)
  Conditional skewness with quantile regression models: SoFiE presidential address and a tribute to Hal White.
  Journal of Financial Econometrics 12 (4),  pp. 620–644.
  Cited by: [footnote 1](#footnote1a "In 2.1 Background ‣ 2 Quantile-based modeling").
* L. R. Glosten, R. Jagannathan, and D. E. Runkle (1993)
  On the relation between the expected value and the volatility of the nominal excess return on stocks.
  Journal of Finance 48 (5),  pp. 1779–1801.
  Cited by: [§2.2](#S2.SS2.p5.11 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling"),
  [§3.2](#S3.SS2.p1.2 "3.2 Benchmark models ‣ 3 Simulation experiments").
* B.E. Hansen (1994)
  Autoregressive conditional density estimation.
  International Economic Review 35 (3),  pp. 705–730.
  Cited by: [§3.1](#S3.SS1.p1.9 "3.1 Simulation design ‣ 3 Simulation experiments"),
  [§3.1](#S3.SS1.p4.5 "3.1 Simulation design ‣ 3 Simulation experiments"),
  [§3.2](#S3.SS2.p1.2 "3.2 Benchmark models ‣ 3 Simulation experiments"),
  [§4](#S4.p5.2 "4 Empirical Application").
* P. R. Hansen, A. Lunde, and J. M. Nason (2011)
  The model confidence set.
  Econometrica 79 (2),  pp. 453–497.
  Cited by: [§4.1](#S4.SS1.p1.1 "4.1 Evaluation of VaR forecasts ‣ 4 Empirical Application"),
  [§4.1](#S4.SS1.p2.1 "4.1 Evaluation of VaR forecasts ‣ 4 Empirical Application"),
  [footnote 7](#footnote7 "In 4.1 Evaluation of VaR forecasts ‣ 4 Empirical Application").
* P. J. Huber and E. Ronchetti (2009)
  Robust statistics.
  2nd edition, Wiley, Hoboken, N.J..
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 Background ‣ 2 Quantile-based modeling"),
  [§2.3](#S2.SS3.p3.4 "2.3 Estimating VaR ‣ 2 Quantile-based modeling").
* E. Jondeau and M. Rockinger (2003)
  Conditional volatility, skewness, and kurtosis: existence, persistence, and comovements.
  Journal of Economic Dynamics & Control 27 (10),  pp. 1699–1737.
  Cited by: [§3.1](#S3.SS1.p3.1 "3.1 Simulation design ‣ 3 Simulation experiments").
* T. Kim and H. White (2004)
  On more robust estimation of skewness and kurtosis.
  Finance Research Letters 1 (1),  pp. 56–73.
  Cited by: [footnote 1](#footnote1a "In 2.1 Background ‣ 2 Quantile-based modeling").
* R. Koenker and G. Bassett (1978)
  Regression quantiles.
  Econometrica 46 (1),  pp. 33–50.
  Cited by: [§2.2](#S2.SS2.p6.7 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* R. Koenker and Z. Xiao (2006)
  Quantile autoregression.
  Journal of the American Statistical Association 101 (475),  pp. 980–990.
  Cited by: [§2.2](#S2.SS2.p2.3 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* S. Kotz and J. van Dorp (2005)
  A link between two-sided power and asymmetric Laplace distributions: with applications to mean and variance approximations.
  Statistics & Probability Letters 71 (4),  pp. 383–394.
  Cited by: [§2.1](#S2.SS1.p3.15 "2.1 Background ‣ 2 Quantile-based modeling").
* K. Kuester, S. Mittnik, and M. S. Paolella (2006)
  Value-at-Risk Prediction: A Comparison of Alternative Strategies.
  Journal of Financial Econometrics 4 (1),  pp. 53–89.
  Cited by: [§1](#S1.p4.2 "1 Introduction"),
  [§2.2](#S2.SS2.p2.3 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* F. Mosteller (1946)
  On some useful “inefficient” statistics.
  Annals of Mathematical Statistics 17 (4),  pp. 377–408.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Estimating VaR ‣ 2 Quantile-based modeling").
* D. B. Nelson (1991)
  Conditional heteroskedasticity in asset returns: a new approach.
  Econometrica 59 (2),  pp. 347–370.
  Cited by: [§2.2](#S2.SS2.p5.11 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling"),
  [§3.2](#S3.SS2.p1.2 "3.2 Benchmark models ‣ 3 Simulation experiments"),
  [footnote 5](#footnote5 "In 3.2 Benchmark models ‣ 3 Simulation experiments").
* M. Parkinson (1980)
  The extreme value method for estimating the variance of the rate of return.
  Journal of Business 53 (1),  pp. 61–65.
  Cited by: [footnote 2](#footnote2a "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* A.J. Patton, J.F. Ziegel, and R. Chen (2019)
  Dynamic semiparametric models for expected shortfall (and Value-at-Risk).
  Journal of Econometrics 211 (2),  pp. 388–413.
  Cited by: [§1](#S1.p6.1 "1 Introduction"),
  [§3.1](#S3.SS1.p4.5 "3.1 Simulation design ‣ 3 Simulation experiments"),
  [§3.2](#S3.SS2.p4.3 "3.2 Benchmark models ‣ 3 Simulation experiments"),
  [§3.2](#S3.SS2.p5.3 "3.2 Benchmark models ‣ 3 Simulation experiments"),
  [§4](#S4.p5.2 "4 Empirical Application"),
  [footnote 3](#footnote3 "In 3.1 Simulation design ‣ 3 Simulation experiments").
* E. Pearson and J. Tukey (1965)
  Approximate means and standard deviations based on distances between percentage points of frequency curves.
  Biometrika 52 (3/4),  pp. 533–546.
  Cited by: [§2.1](#S2.SS1.p3.15 "2.1 Background ‣ 2 Quantile-based modeling"),
  [§2.3](#S2.SS3.p2.1 "2.3 Estimating VaR ‣ 2 Quantile-based modeling").
* G. W. Schwert (1990)
  Stock volatility and the crash of ’87.
  Review of Financial Studies 3 (1),  pp. 77–102.
  Cited by: [§2.2](#S2.SS2.p4.1 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling"),
  [§3.1](#S3.SS1.p1.9 "3.1 Simulation design ‣ 3 Simulation experiments").
* E. Şener, S. Baronyan, and L. Ali Mengütürk (2012)
  Ranking the predictive performances of value-at-risk estimation methods.
  International Journal of Forecasting 28 (4),  pp. 849–873.
  Cited by: [§1](#S1.p4.8 "1 Introduction").
* J.W. Taylor (2019)
  Forecasting value at risk and expected shortfall using a semiparametric approach based on the asymmetric Laplace distribution.
  Journal of Business & Economic Statistics 37 (1),  pp. 121–133.
  Cited by: [§1](#S1.p6.1 "1 Introduction"),
  [§2.2](#S2.SS2.p2.3 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling"),
  [§3.2](#S3.SS2.p2.5 "3.2 Benchmark models ‣ 3 Simulation experiments"),
  [§4.2](#S4.SS2.p1.3 "4.2 Joint evaluation of VaR and ES forecasts ‣ 4 Empirical Application"),
  [§4](#S4.p5.2 "4 Empirical Application").
* J. W. Taylor (2005)
  Generating volatility forecasts from value at risk estimates.
  Management Science 51 (5),  pp. 712–725.
  Cited by: [§1](#S1.p7.1 "1 Introduction"),
  [§2.1](#S2.SS1.p3.15 "2.1 Background ‣ 2 Quantile-based modeling"),
  [§2.1](#S2.SS1.p3.6 "2.1 Background ‣ 2 Quantile-based modeling"),
  [footnote 2](#footnote2a "In 2.2 Conditional dynamics ‣ 2 Quantile-based modeling").
* H. White, T. Kim, and S. Manganelli (2010)
  Modeling autoregressive conditional skewness and kurtosis with multi-quantile CAViaR.
  In Volatility and Time Series Econometrics: Essays in Honor of Robert F. Engle, T. Bollerslev, J. Russell, and M. Watson (Eds.),
  Cited by: [footnote 1](#footnote1a "In 2.1 Background ‣ 2 Quantile-based modeling").
* Z. Xiao and R. Koenker (2009)
  Conditional quantile estimation for generalized autoregressive conditional heteroscedasticity models.
  Journal of the American Statistical Association 104,  pp. 1696–1712.
  Cited by: [§2.2](#S2.SS2.p4.2 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling"),
  [§3.1](#S3.SS1.p1.9 "3.1 Simulation design ‣ 3 Simulation experiments").
* J.-M. Zakoïan (1994)
  Threshold heteroskedastic models.
  Journal of Economic Dynamics and Control 18,  pp. 931–955.
  Cited by: [§2.2](#S2.SS2.p5.12 "2.2 Conditional dynamics ‣ 2 Quantile-based modeling").

Table 1. VaR forecast accuracy when there are no leverage effects

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.105 | 0.079 | 0.061 |  | 0.134 | 0.095 | 0.071 |  | 0.148 | 0.094 | 0.066 |  | 0.201 | 0.119 | 0.080 |
| QbSD-gAS |  | 0.118 | 0.088 | 0.070 |  | 0.143 | 0.102 | 0.079 |  | 0.157 | 0.102 | 0.075 |  | 0.207 | 0.125 | 0.086 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.153 | 0.101 | 0.073 |  | 0.220 | 0.136 | 0.097 |  | 0.226 | 0.129 | 0.083 |  | 0.344 | 0.180 | 0.114 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.154 | 0.102 | 0.075 |  | 0.218 | 0.137 | 0.102 |  | 0.229 | 0.132 | 0.085 |  | 0.345 | 0.187 | 0.122 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.187 | 0.115 | 0.085 |  | 0.258 | 0.157 | 0.112 |  | 0.280 | 0.151 | 0.097 |  | 0.390 | 0.214 | 0.133 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.187 | 0.118 | 0.089 |  | 0.260 | 0.163 | 0.119 |  | 0.280 | 0.156 | 0.103 |  | 0.394 | 0.223 | 0.142 |
| GAS |  | 0.283 | 0.204 | 0.160 |  | 0.338 | 0.236 | 0.165 |  | 0.340 | 0.225 | 0.151 |  | 0.429 | 0.252 | 0.163 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.086 | 0.056 | 0.044 |  | 0.477 | 0.303 | 0.180 |  | 0.241 | 0.087 | 0.082 |  | 0.766 | 0.367 | 0.153 |
| Student-tt |  | 0.071 | 0.054 | 0.044 |  | 0.392 | 0.285 | 0.195 |  | 0.103 | 0.068 | 0.050 |  | 0.602 | 0.370 | 0.218 |
| Skew-tt |  | 0.080 | 0.060 | 0.047 |  | 0.099 | 0.068 | 0.049 |  | 0.111 | 0.073 | 0.053 |  | 0.150 | 0.087 | 0.055 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.086 | 0.056 | 0.044 |  | 0.477 | 0.303 | 0.180 |  | 0.241 | 0.087 | 0.082 |  | 0.765 | 0.367 | 0.153 |
| Student-tt |  | 0.071 | 0.054 | 0.044 |  | 0.392 | 0.285 | 0.195 |  | 0.103 | 0.068 | 0.050 |  | 0.602 | 0.369 | 0.218 |
| Skew-tt |  | 0.080 | 0.059 | 0.047 |  | 0.098 | 0.068 | 0.049 |  | 0.111 | 0.073 | 0.053 |  | 0.145 | 0.084 | 0.054 |
| EGARCH |  | 0.093 | 0.066 | 0.054 |  | 0.480 | 0.306 | 0.182 |  | 0.245 | 0.099 | 0.093 |  | 0.772 | 0.367 | 0.152 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.136 | 0.101 | 0.079 |  | 0.173 | 0.123 | 0.094 |  | 0.197 | 0.126 | 0.091 |  | 0.266 | 0.161 | 0.112 |
| QbSD-gAS |  | 0.154 | 0.115 | 0.093 |  | 0.186 | 0.134 | 0.105 |  | 0.212 | 0.137 | 0.102 |  | 0.274 | 0.170 | 0.119 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.221 | 0.134 | 0.100 |  | 0.311 | 0.187 | 0.133 |  | 0.332 | 0.184 | 0.118 |  | 0.524 | 0.237 | 0.168 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.225 | 0.136 | 0.102 |  | 0.313 | 0.186 | 0.140 |  | 0.326 | 0.185 | 0.119 |  | 0.516 | 0.267 | 0.173 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.259 | 0.153 | 0.114 |  | 0.349 | 0.212 | 0.153 |  | 0.396 | 0.209 | 0.133 |  | 0.539 | 0.300 | 0.188 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.251 | 0.156 | 0.119 |  | 0.359 | 0.219 | 0.160 |  | 0.409 | 0.211 | 0.140 |  | 0.546 | 0.318 | 0.197 |
| GAS |  | 0.380 | 0.270 | 0.214 |  | 0.438 | 0.313 | 0.216 |  | 0.493 | 0.320 | 0.206 |  | 0.609 | 0.366 | 0.261 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.106 | 0.074 | 0.060 |  | 0.493 | 0.317 | 0.194 |  | 0.270 | 0.124 | 0.123 |  | 0.802 | 0.400 | 0.193 |
| Student-tt |  | 0.095 | 0.073 | 0.059 |  | 0.410 | 0.298 | 0.207 |  | 0.143 | 0.097 | 0.072 |  | 0.625 | 0.386 | 0.231 |
| Skew-tt |  | 0.106 | 0.080 | 0.063 |  | 0.132 | 0.093 | 0.070 |  | 0.153 | 0.102 | 0.075 |  | 0.224 | 0.139 | 0.095 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.106 | 0.074 | 0.060 |  | 0.493 | 0.317 | 0.194 |  | 0.270 | 0.125 | 0.123 |  | 0.801 | 0.399 | 0.193 |
| Student-tt |  | 0.095 | 0.073 | 0.059 |  | 0.410 | 0.298 | 0.207 |  | 0.143 | 0.097 | 0.072 |  | 0.625 | 0.386 | 0.231 |
| Skew-tt |  | 0.106 | 0.080 | 0.063 |  | 0.132 | 0.093 | 0.069 |  | 0.153 | 0.103 | 0.075 |  | 0.213 | 0.134 | 0.093 |
| EGARCH |  | 0.121 | 0.087 | 0.070 |  | 0.502 | 0.325 | 0.201 |  | 0.292 | 0.144 | 0.131 |  | 0.814 | 0.407 | 0.191 |

Notes: This table reports the MAE in Panel A and the RMSE in Panel B of various VaR forecasting models. The results are based on 1,000 replications for each configuration of the APARCH model in ([19](#S3.E19 "In 3.1 Simulation design ‣ 3 Simulation experiments")) with innovations following the skewed tt-distribution in ([20](#S3.E20 "In 3.1 Simulation design ‣ 3 Simulation experiments")).
There are no leverage effects (θ=0\theta=0). Bolded values indicate the model with the lowest error.



Table 2. ES forecast accuracy when there are no leverage effects

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.143 | 0.106 | 0.085 |  | 0.189 | 0.134 | 0.107 |  | 0.265 | 0.164 | 0.118 |  | 0.370 | 0.222 | 0.156 |
| QbSD-gAS |  | 0.154 | 0.117 | 0.096 |  | 0.196 | 0.142 | 0.114 |  | 0.275 | 0.171 | 0.126 |  | 0.376 | 0.228 | 0.161 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.188 | 0.125 | 0.092 |  | 0.271 | 0.173 | 0.126 |  | 0.339 | 0.196 | 0.126 |  | 0.527 | 0.281 | 0.182 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.210 | 0.142 | 0.108 |  | 0.292 | 0.196 | 0.142 |  | 0.373 | 0.219 | 0.147 |  | 0.551 | 0.315 | 0.211 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.228 | 0.146 | 0.108 |  | 0.317 | 0.206 | 0.148 |  | 0.392 | 0.225 | 0.145 |  | 0.571 | 0.319 | 0.210 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.233 | 0.155 | 0.116 |  | 0.327 | 0.222 | 0.158 |  | 0.413 | 0.240 | 0.159 |  | 0.583 | 0.345 | 0.227 |
| GAS |  | 0.341 | 0.258 | 0.203 |  | 0.416 | 0.307 | 0.220 |  | 0.474 | 0.323 | 0.221 |  | 0.628 | 0.393 | 0.256 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.146 | 0.094 | 0.067 |  | 0.689 | 0.501 | 0.367 |  | 0.631 | 0.322 | 0.163 |  | 1.463 | 0.898 | 0.563 |
| Student-tt |  | 0.100 | 0.075 | 0.060 |  | 0.489 | 0.394 | 0.315 |  | 0.180 | 0.118 | 0.086 |  | 0.945 | 0.656 | 0.470 |
| Skew-tt |  | 0.110 | 0.083 | 0.067 |  | 0.147 | 0.106 | 0.080 |  | 0.190 | 0.126 | 0.091 |  | 0.122 | 0.179 | 0.122 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.146 | 0.095 | 0.067 |  | 0.689 | 0.501 | 0.367 |  | 0.631 | 0.322 | 0.163 |  | 1.463 | 0.898 | 0.563 |
| Student-tt |  | 0.100 | 0.075 | 0.060 |  | 0.489 | 0.394 | 0.315 |  | 0.180 | 0.118 | 0.086 |  | 0.945 | 0.656 | 0.470 |
| Skew-tt |  | 0.110 | 0.083 | 0.067 |  | 0.146 | 0.105 | 0.080 |  | 0.190 | 0.127 | 0.092 |  | 0.117 | 0.173 | 0.117 |
| EGARCH |  | 0.150 | 0.100 | 0.075 |  | 0.693 | 0.504 | 0.370 |  | 0.637 | 0.327 | 0.169 |  | 1.470 | 0.904 | 0.568 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.185 | 0.138 | 0.112 |  | 0.240 | 0.172 | 0.138 |  | 0.340 | 0.215 | 0.157 |  | 0.463 | 0.285 | 0.205 |
| QbSD-gAS |  | 0.201 | 0.153 | 0.126 |  | 0.254 | 0.185 | 0.149 |  | 0.352 | 0.227 | 0.168 |  | 0.473 | 0.294 | 0.211 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.265 | 0.169 | 0.126 |  | 0.382 | 0.237 | 0.173 |  | 0.482 | 0.277 | 0.179 |  | 0.770 | 0.401 | 0.262 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.291 | 0.197 | 0.147 |  | 0.408 | 0.267 | 0.195 |  | 0.521 | 0.309 | 0.209 |  | 0.763 | 0.444 | 0.304 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.313 | 0.193 | 0.143 |  | 0.429 | 0.276 | 0.200 |  | 0.536 | 0.306 | 0.198 |  | 0.760 | 0.439 | 0.289 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.312 | 0.210 | 0.155 |  | 0.439 | 0.300 | 0.219 |  | 0.555 | 0.330 | 0.221 |  | 0.792 | 0.480 | 0.319 |
| GAS |  | 0.452 | 0.345 | 0.275 |  | 0.536 | 0.405 | 0.288 |  | 0.716 | 0.459 | 0.304 |  | 0.921 | 0.558 | 0.395 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.168 | 0.114 | 0.085 |  | 0.707 | 0.517 | 0.382 |  | 0.658 | 0.349 | 0.192 |  | 1.507 | 0.934 | 0.596 |
| Student-tt |  | 0.129 | 0.099 | 0.081 |  | 0.515 | 0.414 | 0.330 |  | 0.241 | 0.162 | 0.120 |  | 0.982 | 0.682 | 0.489 |
| Skew-tt |  | 0.145 | 0.111 | 0.090 |  | 0.192 | 0.140 | 0.108 |  | 0.255 | 0.172 | 0.127 |  | 0.183 | 0.262 | 0.411 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.168 | 0.115 | 0.085 |  | 0.707 | 0.517 | 0.382 |  | 0.658 | 0.349 | 0.192 |  | 1.506 | 0.933 | 0.595 |
| Student-tt |  | 0.129 | 0.099 | 0.081 |  | 0.515 | 0.414 | 0.330 |  | 0.241 | 0.162 | 0.120 |  | 0.982 | 0.682 | 0.489 |
| Skew-tt |  | 0.145 | 0.110 | 0.089 |  | 0.191 | 0.140 | 0.108 |  | 0.256 | 0.173 | 0.127 |  | 0.174 | 0.247 | 0.383 |
| EGARCH |  | 0.184 | 0.130 | 0.099 |  | 0.717 | 0.526 | 0.390 |  | 0.678 | 0.369 | 0.213 |  | 1.524 | 0.948 | 0.606 |

Notes: This table reports the MAE in Panel A and the RMSE in Panel B for various ES forecasting models. See Table 1 for a description of the simulation setup.
The results are based on simulations without leverage effects (θ=0\theta=0). Bolded values indicate the model with the lowest error.



Table 3. VaR forecast accuracy in the presence of leverage effects

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.214 | 0.170 | 0.139 |  | 0.271 | 0.212 | 0.166 |  | 0.240 | 0.170 | 0.130 |  | 0.324 | 0.220 | 0.159 |
| QbSD-gAS |  | 0.124 | 0.093 | 0.075 |  | 0.172 | 0.125 | 0.096 |  | 0.170 | 0.110 | 0.080 |  | 0.255 | 0.159 | 0.109 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.260 | 0.187 | 0.148 |  | 0.347 | 0.242 | 0.184 |  | 0.326 | 0.200 | 0.144 |  | 0.473 | 0.273 | 0.188 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.261 | 0.189 | 0.148 |  | 0.351 | 0.244 | 0.187 |  | 0.330 | 0.202 | 0.144 |  | 0.480 | 0.277 | 0.199 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.198 | 0.127 | 0.093 |  | 0.299 | 0.184 | 0.135 |  | 0.312 | 0.164 | 0.106 |  | 0.482 | 0.254 | 0.163 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.204 | 0.131 | 0.098 |  | 0.305 | 0.193 | 0.142 |  | 0.304 | 0.169 | 0.109 |  | 0.480 | 0.267 | 0.176 |
| GAS |  | 0.391 | 0.264 | 0.174 |  | 0.605 | 0.386 | 0.247 |  | 0.447 | 0.254 | 0.164 |  | 0.751 | 0.397 | 0.239 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.202 | 0.163 | 0.135 |  | 0.539 | 0.346 | 0.215 |  | 0.299 | 0.172 | 0.149 |  | 0.879 | 0.413 | 0.180 |
| Student-tt |  | 0.200 | 0.162 | 0.134 |  | 0.440 | 0.326 | 0.231 |  | 0.221 | 0.162 | 0.126 |  | 0.682 | 0.420 | 0.249 |
| Skew-tt |  | 0.205 | 0.165 | 0.135 |  | 0.211 | 0.160 | 0.124 |  | 0.226 | 0.166 | 0.128 |  | 0.239 | 0.155 | 0.109 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.194 | 0.156 | 0.128 |  | 0.538 | 0.345 | 0.214 |  | 0.295 | 0.164 | 0.142 |  | 0.879 | 0.413 | 0.180 |
| Student-tt |  | 0.200 | 0.162 | 0.134 |  | 0.440 | 0.326 | 0.231 |  | 0.221 | 0.162 | 0.126 |  | 0.682 | 0.420 | 0.249 |
| Skew-tt |  | 0.205 | 0.165 | 0.135 |  | 0.211 | 0.160 | 0.124 |  | 0.227 | 0.166 | 0.128 |  | 0.233 | 0.152 | 0.108 |
| EGARCH |  | 0.105 | 0.075 | 0.062 |  | 0.558 | 0.356 | 0.213 |  | 0.262 | 0.105 | 0.099 |  | 0.901 | 0.430 | 0.179 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.283 | 0.225 | 0.185 |  | 0.363 | 0.283 | 0.224 |  | 0.330 | 0.235 | 0.180 |  | 0.451 | 0.326 | 0.230 |
| QbSD-gAS |  | 0.166 | 0.126 | 0.101 |  | 0.238 | 0.183 | 0.138 |  | 0.250 | 0.178 | 0.130 |  | 0.437 | 0.333 | 0.222 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.346 | 0.252 | 0.198 |  | 0.479 | 0.335 | 0.254 |  | 0.465 | 0.282 | 0.204 |  | 0.753 | 0.412 | 0.285 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.361 | 0.255 | 0.197 |  | 0.510 | 0.341 | 0.256 |  | 0.463 | 0.287 | 0.205 |  | 0.722 | 0.409 | 0.292 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.272 | 0.175 | 0.129 |  | 0.419 | 0.267 | 0.199 |  | 0.460 | 0.235 | 0.161 |  | 0.738 | 0.397 | 0.272 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.303 | 0.181 | 0.136 |  | 0.433 | 0.283 | 0.209 |  | 0.436 | 0.244 | 0.162 |  | 0.725 | 0.408 | 0.284 |
| GAS |  | 0.503 | 0.345 | 0.227 |  | 0.800 | 0.547 | 0.356 |  | 0.684 | 0.350 | 0.218 |  | 1.307 | 0.627 | 0.397 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.264 | 0.215 | 0.180 |  | 0.622 | 0.411 | 0.265 |  | 0.377 | 0.239 | 0.213 |  | 1.027 | 0.500 | 0.231 |
| Student-tt |  | 0.268 | 0.216 | 0.177 |  | 0.522 | 0.390 | 0.281 |  | 0.312 | 0.229 | 0.177 |  | 0.804 | 0.500 | 0.303 |
| Skew-tt |  | 0.273 | 0.220 | 0.179 |  | 0.278 | 0.211 | 0.164 |  | 0.320 | 0.234 | 0.179 |  | 0.326 | 0.212 | 0.150 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.255 | 0.207 | 0.173 |  | 0.620 | 0.409 | 0.263 |  | 0.365 | 0.231 | 0.209 |  | 1.027 | 0.500 | 0.231 |
| Student-tt |  | 0.268 | 0.216 | 0.177 |  | 0.522 | 0.390 | 0.281 |  | 0.312 | 0.229 | 0.177 |  | 0.804 | 0.500 | 0.303 |
| Skew-tt |  | 0.274 | 0.220 | 0.179 |  | 0.278 | 0.211 | 0.164 |  | 0.319 | 0.234 | 0.179 |  | 0.317 | 0.208 | 0.147 |
| EGARCH |  | 0.148 | 0.107 | 0.086 |  | 0.647 | 0.428 | 0.273 |  | 0.334 | 0.160 | 0.136 |  | 1.132 | 0.584 | 0.287 |

Notes: This table reports the MAE in Panel A and the RMSE in Panel B for various VaR forecasting models. See Table 1 for a description of the simulation setup. The results are based on simulations with leverage effects (θ=0.5\theta=0.5).
Bolded values indicate the model with the lowest error.



Table 4. ES forecast accuracy in the presence of leverage effects

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.253 | 0.208 | 0.179 |  | 0.335 | 0.268 | 0.223 |  | 0.354 | 0.248 | 0.193 |  | 0.510 | 0.342 | 0.257 |
| QbSD-gAS |  | 0.165 | 0.125 | 0.103 |  | 0.235 | 0.174 | 0.140 |  | 0.292 | 0.186 | 0.136 |  | 0.445 | 0.279 | 0.198 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.304 | 0.229 | 0.189 |  | 0.414 | 0.303 | 0.244 |  | 0.450 | 0.283 | 0.208 |  | 0.680 | 0.403 | 0.287 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.329 | 0.253 | 0.201 |  | 0.449 | 0.335 | 0.266 |  | 0.488 | 0.323 | 0.225 |  | 0.733 | 0.457 | 0.341 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.245 | 0.158 | 0.116 |  | 0.369 | 0.234 | 0.179 |  | 0.442 | 0.241 | 0.157 |  | 0.697 | 0.381 | 0.256 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.262 | 0.180 | 0.138 |  | 0.403 | 0.275 | 0.217 |  | 0.454 | 0.267 | 0.181 |  | 0.752 | 0.442 | 0.316 |
| GAS |  | 0.475 | 0.336 | 0.232 |  | 0.730 | 0.522 | 0.329 |  | 0.598 | 0.369 | 0.235 |  | 1.062 | 0.619 | 0.365 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.255 | 0.207 | 0.175 |  | 0.780 | 0.566 | 0.416 |  | 0.663 | 0.367 | 0.228 |  | 1.687 | 1.033 | 0.644 |
| Student-tt |  | 0.249 | 0.205 | 0.175 |  | 0.539 | 0.441 | 0.357 |  | 0.325 | 0.239 | 0.188 |  | 1.063 | 0.743 | 0.532 |
| Skew-tt |  | 0.253 | 0.210 | 0.178 |  | 0.279 | 0.218 | 0.179 |  | 0.335 | 0.245 | 0.192 |  | 0.405 | 0.272 | 0.197 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.247 | 0.199 | 0.168 |  | 0.779 | 0.565 | 0.415 |  | 0.661 | 0.364 | 0.223 |  | 1.687 | 1.033 | 0.644 |
| Student-tt |  | 0.249 | 0.205 | 0.175 |  | 0.539 | 0.441 | 0.357 |  | 0.325 | 0.239 | 0.188 |  | 1.063 | 0.743 | 0.532 |
| Skew-tt |  | 0.254 | 0.210 | 0.178 |  | 0.279 | 0.218 | 0.178 |  | 0.334 | 0.245 | 0.193 |  | 0.388 | 0.263 | 0.191 |
| EGARCH |  | 0.167 | 0.113 | 0.086 |  | 0.804 | 0.586 | 0.430 |  | 0.682 | 0.349 | 0.180 |  | 1.711 | 1.055 | 0.664 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.338 | 0.279 | 0.239 |  | 0.450 | 0.359 | 0.299 |  | 0.473 | 0.339 | 0.266 |  | 0.675 | 0.464 | 0.356 |
| QbSD-gAS |  | 0.215 | 0.165 | 0.137 |  | 0.314 | 0.238 | 0.195 |  | 0.392 | 0.266 | 0.204 |  | 0.672 | 0.465 | 0.357 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.404 | 0.312 | 0.252 |  | 0.580 | 0.422 | 0.335 |  | 0.641 | 0.403 | 0.294 |  | 1.071 | 0.590 | 0.423 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.443 | 0.342 | 0.270 |  | 0.664 | 0.474 | 0.391 |  | 0.682 | 0.447 | 0.334 |  | 1.110 | 0.684 | 0.587 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.328 | 0.216 | 0.162 |  | 0.513 | 0.336 | 0.262 |  | 0.619 | 0.333 | 0.232 |  | 1.015 | 0.563 | 0.404 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.376 | 0.250 | 0.192 |  | 0.571 | 0.404 | 0.335 |  | 0.611 | 0.380 | 0.260 |  | 1.183 | 0.675 | 0.602 |
| GAS |  | 0.623 | 0.438 | 0.304 |  | 0.991 | 0.724 | 0.467 |  | 0.936 | 0.529 | 0.317 |  | 1.809 | 0.950 | 0.578 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.330 | 0.270 | 0.230 |  | 0.880 | 0.650 | 0.487 |  | 0.772 | 0.449 | 0.295 |  | 1.955 | 1.202 | 0.759 |
| Student-tt |  | 0.331 | 0.274 | 0.233 |  | 0.643 | 0.525 | 0.427 |  | 0.456 | 0.337 | 0.266 |  | 1.251 | 0.874 | 0.630 |
| Skew-tt |  | 0.340 | 0.280 | 0.237 |  | 0.367 | 0.288 | 0.235 |  | 0.468 | 0.345 | 0.272 |  | 0.562 | 0.372 | 0.269 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.319 | 0.260 | 0.222 |  | 0.878 | 0.648 | 0.486 |  | 0.759 | 0.437 | 0.285 |  | 1.954 | 1.202 | 0.758 |
| Student-tt |  | 0.331 | 0.274 | 0.233 |  | 0.643 | 0.525 | 0.427 |  | 0.456 | 0.337 | 0.266 |  | 1.251 | 0.874 | 0.630 |
| Skew-tt |  | 0.338 | 0.279 | 0.237 |  | 0.367 | 0.288 | 0.261 |  | 0.469 | 0.346 | 0.271 |  | 0.526 | 0.352 | 0.256 |
| EGARCH |  | 0.219 | 0.157 | 0.122 |  | 0.912 | 0.676 | 0.507 |  | 0.765 | 0.421 | 0.244 |  | 2.077 | 1.309 | 0.851 |

Notes: This table reports the MAE in Panel A and the RMSE in Panel B for various ES forecasting models. See Table 1 for a description of the simulation setup. The results are based on simulations with leverage effects (θ=0.5\theta=0.5).
Bolded values indicate the model with the lowest error.

Table 5. Ranking of 1% VaR forecasting models based on the MCS procedure using quantile scores

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 16 | 1 | 3 | 7 | 2 | 1 | 1 | 1 | 8 | 4.0 | 1 |
| GJR-GARCH-skew-tt | 15 | 6 | 12 | 4 | 7 | 8 | 3 | 4 | 8 | 7.4 | 2 |
| GARCH-skew-tt | 20 | 3 | 2 | 2 | 9 | 6 | 16 | 6 | 8 | 8.0 | 3 |
| GJR-GARCH-tt | 7 | 7 | 11 | 1 | 20 | 2 | 2 | 15 | 8 | 8.1 | 4 |
| AR-GJR-GARCH-skew-tt | 1 | 5 | 7 | 3 | 10 | 18 | 12 | 9 | 8 | 8.1 | 5 |
| AR-GARCH-skew-tt | 13 | 9 | 1 | 8 | 11 | 4 | 15 | 8 | 8 | 8.6 | 6 |
| AR-GJR-GARCH-tt | 2 | 2 | 10 | 6 | 19 | 7 | 11 | 21 | 8 | 9.8 | 7 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 4 | 10 | 16 | 20 | 4 | 12 | 14 | 2 | 8 | 10.2 | 8 |
| QAR-QbSD-gAS | 6 | 4 | 22 | 5 | 1 | 14 | 28 | 3 | 8 | 10.4 | 9 |
| ALMult.{}\_{\text{Mult.}}-AS | 8 | 17 | 14 | 21 | 3 | 13 | 4 | 5 | 8 | 10.6 | 10 |
| AR-ALAR{}\_{\text{AR}}-AS | 18 | 8 | 13 | 14 | 5 | 11 | 9 | 11 | 8 | 11.1 | 11 |
| ALAR{}\_{\text{AR}}-AS | 14 | 18 | 15 | 19 | 6 | 10 | 5 | 7 | 8 | 11.8 | 12 |
| GARCH-tt | 5 | 13 | 8 | 12 | 22 | 3 | 18 | 14 | 8 | 11.9 | 13 |
| AR-GARCH-tt | 3 | 11 | 9 | 9 | 21 | 20 | 13 | 22 | 8 | 13.5 | 14 |
| ALMult.{}\_{\text{Mult.}}-SAV | 12 | 19 | 5 | 16 | 16 | 19 | 6 | 20 | 8 | 14.1 | 15 |
| QAR-QbSD-gSAV | 27 | 21 | 25 | 10 | 8 | 5 | 7 | 10 | 8 | 14.1 | 16 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 9 | 14 | 6 | 17 | 18 | 22 | 10 | 19 | 8 | 14.4 | 17 |
| EGARCH | 21 | 15 | 18 | 11 | 14 | 16 | 19 | 12 | 8 | 15.8 | 18 |
| ALAR{}\_{\text{AR}}-SAV | 22 | 24 | 4 | 18 | 13 | 17 | 17 | 17 | 8 | 16.5 | 19 |
| AR-ALAR{}\_{\text{AR}}-SAV | 10 | 12 | 17 | 24 | 15 | 21 | 20 | 18 | 8 | 17.1 | 20 |
| QbSD-gSAV |  | 28 | 26 | 15 | 12 | 9 | 8 | 13 | 7 | 17.4 | 21 |
| AR-EGARCH | 19 | 16 | 19 | 13 | 17 | 26 | 21 | 16 | 8 | 18.4 | 22 |
| GAS | 11 | 22 | 20 | 27 | 23 | 27 | 24 | 23 | 8 | 22.1 | 23 |
| AR-GAS | 17 | 20 | 21 |  | 24 |  | 25 | 24 | 6 | 23.4 | 24 |
| GARCH-normal | 24 | 23 | 24 | 23 | 25 | 23 | 23 |  | 7 | 24.1 | 25 |
| GJR-GARCH-normal | 23 | 25 | 23 | 22 |  | 24 | 22 |  | 6 | 24.4 | 26 |
| AR-GJR-GARCH-normal | 25 | 26 | 28 | 25 |  | 15 | 26 |  | 6 | 25.1 | 27 |
| AR-GARCH-normal | 26 | 27 | 27 | 26 |  | 25 | 27 |  | 6 | 26.8 | 28 |

Notes: A model that is excluded from ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast} for a given stock index is left blank in the table. The remaining models in
ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast} are ranked based on their quantile score tt-statistics, with lower values indicating better performance. The column “#” represents the number of stock indices (out of 8) for which the model is included in ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast}. The “Avg. rank” column reports the average rank across all stock indices, where models eliminated from ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast} were assigned a rank of 28. The “Final rank” column orders models from best to worst based on their average rank, summarizing their relative forecasting performance across stock indices. The rolling-window size is R=1250R=1250.



Table 6. Ranking of 2.5% VaR forecasting models based on the MCS procedure using quantile scores

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 2 | 1 | 1 | 16 | 1 | 1 | 1 | 3 | 8 | 3.2 | 1 |
| ALMult.{}\_{\text{Mult.}}-AS | 9 | 3 | 2 | 9 | 2 | 2 | 2 | 2 | 8 | 3.9 | 2 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 6 | 4 | 6 | 8 | 3 | 3 | 3 | 1 | 8 | 4.2 | 3 |
| ALAR{}\_{\text{AR}}-AS | 7 | 5 | 4 | 4 | 8 | 4 | 8 | 5 | 8 | 5.6 | 4 |
| GJR-GARCH-skew-tt | 4 | 8 | 5 | 6 | 12 | 7 | 7 | 8 | 8 | 7.1 | 5 |
| QAR-QbSD-gAS | 1 | 2 | 23 | 2 | 6 | 5 | 15 | 4 | 8 | 7.2 | 6 |
| GARCH-skew-tt | 3 | 6 | 7 | 1 | 10 | 8 | 19 | 7 | 8 | 7.6 | 7 |
| EGARCH | 10 | 7 | 8 | 12 | 5 | 11 | 12 | 6 | 8 | 8.9 | 8 |
| AR-ALAR{}\_{\text{AR}}-AS | 12 | 12 | 3 | 11 | 4 | 10 | 26 | 13 | 8 | 11.4 | 9 |
| GJR-GARCH-tt | 13 | 9 | 10 | 13 | 15 | 16 | 10 | 11 | 8 | 12.1 | 10 |
| ALMult.{}\_{\text{Mult.}}-SAV | 18 | 16 | 17 | 5 | 11 | 20 | 4 | 9 | 8 | 12.5 | 11 |
| AR-GJR-GARCH-skew-tt | 5 | 13 | 11 | 19 | 14 | 9 | 17 | 15 | 8 | 12.9 | 12 |
| AR-EGARCH | 16 | 11 | 22 | 15 | 7 | 12 | 21 | 10 | 8 | 14.2 | 13 |
| GARCH-tt | 11 | 10 | 12 | 26 | 16 | 17 | 11 | 12 | 8 | 14.4 | 14 |
| AR-GARCH-skew-tt | 8 | 19 | 9 | 22 | 17 | 6 | 20 | 14 | 8 | 14.4 | 15 |
| ALAR{}\_{\text{AR}}-SAV | 25 | 17 | 14 | 7 | 23 | 21 | 5 | 19 | 8 | 16.4 | 16 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 14 | 20 | 19 | 3 | 19 | 22 | 6 |  | 7 | 16.4 | 17 |
| GJR-GARCH-normal | 21 | 18 | 13 | 14 | 22 | 23 | 13 | 18 | 8 | 17.8 | 18 |
| QAR-QbSD-gSAV | 27 | 22 | 25 | 10 | 13 | 18 | 16 | 16 | 8 | 18.4 | 19 |
| GARCH-normal | 22 | 15 | 20 | 17 | 18 | 25 | 14 | 17 | 8 | 18.5 | 20 |
| AR-GJR-GARCH-tt | 15 | 14 | 15 | 20 | 20 | 15 | 22 |  | 7 | 18.6 | 21 |
| QbSD-gSAV |  | 26 | 18 | 9 | 13 | 9 |  |  | 5 | 19.9 | 22 |
| AR-ALAR{}\_{\text{AR}}-SAV | 20 | 21 | 18 | 21 | 24 | 19 | 18 |  | 7 | 21.1 | 23 |
| AR-GARCH-tt | 17 | 24 | 16 | 25 | 21 | 26 | 23 |  | 7 | 22.5 | 24 |
| AR-GJR-GARCH-normal | 19 | 25 | 21 | 24 |  | 14 | 24 |  | 6 | 22.9 | 25 |
| AR-GARCH-normal | 23 | 26 | 24 | 23 | 25 | 24 | 25 |  | 7 | 24.8 | 26 |
| GAS | 24 | 23 |  |  |  |  |  |  | 2 | 26.9 | 27 |
| AR-GAS | 26 | 27 |  |  |  |  |  |  | 2 | 27.6 | 28 |

Notes: For explanations, see notes of Table 5.



Table 7. Ranking of 5% VaR forecasting models based on the MCS procedure using quantile scores

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 1 | 1 | 1 | 12 | 1 | 1 | 1 | 3 | 8 | 2.6 | 1 |
| EGARCH | 3 | 3 | 2 | 2 | 2 | 4 | 6 | 5 | 8 | 3.4 | 2 |
| ALMult.{}\_{\text{Mult.}}-AS | 4 | 19 | 3 | 4 | 5 | 7 | 3 | 1 | 8 | 5.8 | 3 |
| QAR-QbSD-gAS | 2 | 2 | 6 | 14 | 4 | 2 | 12 | 4 | 8 | 5.8 | 4 |
| AR-EGARCH | 11 | 4 | 14 | 7 | 3 | 5 | 7 | 12 | 8 | 7.9 | 5 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 18 | 11 | 11 | 9 | 8 | 3 | 4 | 2 | 8 | 8.2 | 6 |
| GJR-GARCH-skew-tt | 10 | 8 | 4 | 6 | 12 | 10 | 13 | 8 | 8 | 8.9 | 7 |
| GARCH-skew-tt | 9 | 5 | 5 | 10 | 10 | 14 | 15 | 9 | 8 | 9.6 | 8 |
| ALAR{}\_{\text{AR}}-AS | 20 | 18 | 15 | 1 | 7 | 6 | 5 | 7 | 8 | 9.9 | 9 |
| GJR-GARCH-normal | 7 | 10 | 10 | 3 | 21 | 11 | 10 | 10 | 8 | 10.2 | 10 |
| ALAR{}\_{\text{AR}}-AS | 17 | 20 | 16 | 17 | 6 | 8 | 2 | 6 | 8 | 11.5 | 11 |
| GJR-GARCH-tt | 6 | 6 | 12 | 22 | 9 | 16 | 8 | 14 | 8 | 11.6 | 12 |
| GARCH-tt | 8 | 7 | 9 | 25 | 11 | 17 | 9 | 13 | 8 | 12.4 | 13 |
| GARCH-normal | 12 | 9 | 13 | 16 | 16 | 13 | 11 | 11 | 8 | 12.6 | 14 |
| AR-GJR-GARCH-skew-tt | 5 | 15 | 7 | 21 | 18 | 18 | 16 |  | 7 | 16.0 | 15 |
| AR-GARCH-skew-tt | 13 | 16 | 8 | 24 | 17 | 15 | 22 |  | 7 | 17.9 | 16 |
| AR-GJR-GARCH-tt | 15 | 12 | 17 | 23 | 14 | 20 | 18 |  | 7 | 18.4 | 17 |
| AR-GARCH-normal | 16 | 17 | 18 | 18 | 20 | 12 | 21 |  | 7 | 18.8 | 18 |
| AR-GJR-GARCH-normal | 19 | 13 | 20 | 20 | 24 | 9 | 17 |  | 7 | 18.8 | 19 |
| AR-GARCH-tt | 14 | 14 | 19 | 26 | 15 | 22 | 20 |  | 7 | 19.8 | 20 |
| QbSD-gSAV | 25 | 21 | 22 | 19 | 13 | 25 | 14 | 19 | 8 | 19.8 | 21 |
| ALMult.{}\_{\text{Mult.}}-SAV | 26 |  | 26 | 8 | 22 | 26 | 19 | 17 | 7 | 21.5 | 22 |
| QAR-QbSD-gSAV | 22 |  | 24 | 15 | 19 | 21 |  | 18 | 6 | 21.9 | 23 |
| ALAR{}\_{\text{AR}}-SAV | 27 |  | 27 | 11 | 23 | 23 |  | 15 | 6 | 22.8 | 24 |
| AR-ALAR{}\_{\text{AR}}-SAV |  | 21 | 21 | 5 |  | 19 |  |  | 3 | 23.1 | 25 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 24 |  | 23 | 13 |  | 24 |  | 20 | 5 | 24.5 | 26 |
| AR-GAS | 23 |  | 25 |  |  | 27 |  | 16 | 4 | 25.4 | 27 |
| GAS | 21 |  | 28 | 27 |  |  |  | 3 | 3 | 27.0 | 28 |

Notes: For explanations, see notes of Table 5.



Table 8. Ranking of 1% VaR and ES forecasting models based on the MCS procedure using AL log scores

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| AR-GJR-GARCH-skew-tt | 1 | 5 | 3 | 1 | 3 | 3 | 8 | 11 | 8 | 4.4 | 1 |
| QbSD-gAS | 9 | 4 | 6 | 8 | 6 | 1 | 1 | 1 | 8 | 4.5 | 2 |
| GARCH-skew-tt | 3 | 2 | 1 | 3 | 4 | 5 | 14 | 10 | 8 | 5.2 | 3 |
| GJR-GARCH-skew-tt | 12 | 3 | 4 | 4 | 5 | 6 | 2 | 9 | 8 | 5.6 | 4 |
| QAR-QbSD-gAS | 4 | 1 | 22 | 7 | 1 | 12 | 4 | 4 | 8 | 6.9 | 5 |
| AR-ALAR{}\_{\text{AR}}-AS | 5 | 8 | 11 | 11 | 12 | 7 | 7 | 5 | 8 | 8.2 | 6 |
| AR-GARCH-skew-tt | 2 | 16 | 2 | 10 | 8 | 2 | 16 | 12 | 8 | 8.5 | 7 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 6 | 6 | 12 | 16 | 9 | 11 | 12 | 2 | 8 | 9.2 | 8 |
| QAR-QbSD-gSAV | 21 | 15 | 18 | 2 | 2 | 4 | 6 | 6 | 8 | 9.2 | 9 |
| ALMult.{}\_{\text{Mult.}}-AS | 7 | 18 | 10 | 17 | 10 | 14 | 5 | 3 | 8 | 10.5 | 10 |
| ALAR{}\_{\text{AR}}-AS | 11 | 14 | 13 | 12 | 7 | 13 | 9 | 8 | 8 | 10.9 | 11 |
| GJR-GARCH-tt | 17 | 9 | 15 | 6 | 21 | 8 | 3 | 18 | 8 | 12.1 | 12 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 10 | 10 | 5 | 19 | 15 | 20 | 15 | 14 | 8 | 13.5 | 13 |
| AR-GJR-GARCH-tt | 14 | 7 | 16 | 5 | 19 | 10 | 10 |  | 7 | 13.6 | 14 |
| AR-ALAR{}\_{\text{AR}}-SAV | 8 | 11 | 7 | 20 | 13 | 16 | 22 | 15 | 8 | 14.0 | 15 |
| ALMult.{}\_{\text{Mult.}}-SAV | 13 | 17 | 8 | 18 | 16 | 19 | 13 | 13 | 8 | 14.6 | 16 |
| GARCH-tt | 18 | 12 | 14 | 14 | 22 | 9 | 18 | 17 | 8 | 15.5 | 17 |
| ALAR{}\_{\text{AR}}-SAV | 16 | 19 | 9 | 15 | 14 | 17 | 20 | 16 | 8 | 15.8 | 18 |
| QbSD-gSAV | 24 | 20 | 19 | 13 | 11 | 15 | 17 | 7 | 8 | 15.8 | 19 |
| AR-GARCH-tt | 15 | 13 | 17 | 9 | 20 | 18 | 11 |  | 7 | 16.4 | 20 |
| GAS | 19 |  | 21 |  | 17 | 21 | 19 | 20 | 6 | 21.6 | 21 |
| EGARCH | 23 | 23 | 20 | 21 | 23 | 22 |  | 19 | 7 | 22.4 | 22 |
| AR-GAS | 20 | 21 | 24 |  | 18 |  | 21 |  | 5 | 23.5 | 23 |
| AR-EGARCH | 22 | 22 | 23 | 22 | 24 |  |  |  | 5 | 24.6 | 24 |
| GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 25 |
| GJR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 26 |
| AR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 27 |
| AR-GJR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 28 |

Notes:
A model that is excluded from ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast} for a given stock index is left blank in the table. The remaining models in ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast} are ranked based on their AL log score tt-statistics, with lower values indicating better performance. The column “#” represents the number of stock indices (out of 8) for which the model is included in ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast}. The “Avg. rank” column reports the average rank across all stock indices, where models eliminated from ℳ^90%∗\widehat{\mathcal{M}}\_{90\%}^{\ast} were assigned a rank of 28. The “Final rank” column orders models from best to worst based on their average rank, summarizing their relative forecasting performance across stock indices. The rolling-window size is R=1250R=1250.



Table 9. Ranking of 2.5% VaR and ES forecasting models based on the MCS procedure using AL log scores

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 5 | 2 | 3 | 12 | 1 | 1 | 1 | 1 | 8 | 3.2 | 1 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 7 | 8 | 8 | 4 | 4 | 2 | 3 | 4 | 8 | 5.0 | 2 |
| ALMult.{}\_{\text{Mult.}}-AS | 11 | 7 | 6 | 8 | 2 | 3 | 2 | 2 | 8 | 5.1 | 3 |
| QAR-QbSD-gAS | 1 | 1 | 18 | 2 | 3 | 8 | 4 | 5 | 8 | 5.2 | 4 |
| GJR-GARCH-skew-tt | 4 | 6 | 1 | 3 | 9 | 7 | 6 |  | 7 | 8.0 | 5 |
| ALAR{}\_{\text{AR}}-AS | 9 | 3 | 5 | 9 |  | 4 | 5 | 3 | 7 | 8.2 | 6 |
| GARCH-skew-tt | 2 | 5 | 4 | 5 | 8 | 6 | 14 |  | 7 | 9.0 | 7 |
| AR-ALAR{}\_{\text{AR}}-AS | 8 | 4 | 2 | 15 | 15 | 10 | 17 | 6 | 8 | 9.6 | 8 |
| AR-GJR-GARCH-skew-tt | 3 | 9 | 9 | 11 | 11 | 9 | 9 |  | 7 | 11.1 | 9 |
| QAR-QbSD-gSAV | 14 | 13 | 14 | 1 | 5 | 11 | 8 |  | 7 | 11.8 | 10 |
| AR-GARCH-skew-tt | 6 | 12 | 7 | 13 | 12 | 5 | 15 |  | 7 | 12.2 | 11 |
| ALMult.{}\_{\text{Mult.}}-SAV | 13 | 14 | 12 | 10 | 6 | 17 | 10 |  | 7 | 13.8 | 12 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 10 | 18 | 11 | 6 | 10 | 15 | 12 |  | 7 | 13.8 | 13 |
| ALAR{}\_{\text{AR}}-SAV | 17 | 15 | 13 | 7 | 13 | 14 | 11 |  | 7 | 14.8 | 14 |
| AR-ALAR{}\_{\text{AR}}-SAV | 12 | 17 | 10 | 14 | 14 | 12 | 13 |  | 7 | 15.0 | 15 |
| GJR-GARCH-tt | 16 | 10 | 15 | 16 | 16 | 18 | 16 |  | 7 | 16.9 | 16 |
| QbSD-gSAV |  | 22 | 22 | 18 | 7 | 13 | 7 |  | 6 | 18.1 | 17 |
| AR-GJR-GARCH-tt | 18 | 11 | 19 | 17 | 19 | 16 | 19 |  | 7 | 18.4 | 18 |
| GARCH-tt | 15 | 16 | 16 | 22 | 17 | 19 | 18 |  | 7 | 18.9 | 19 |
| EGARCH | 19 | 19 | 17 | 19 | 18 | 21 |  |  | 6 | 21.1 | 20 |
| AR-GARCH-tt | 21 | 20 | 20 | 20 |  | 20 | 20 |  | 6 | 22.1 | 21 |
| AR-EGARCH | 20 | 21 | 21 | 21 | 20 | 22 |  |  | 6 | 22.6 | 22 |
| GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 23 |
| GJR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 24 |
| AR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 25 |
| AR-GJR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 26 |
| GAS |  |  |  |  |  |  |  |  | 0 | 28.0 | 27 |
| AR-GAS |  |  |  |  |  |  |  |  | 0 | 28.0 | 28 |

Notes: For explanations, see notes of Table 8.



Table 10. Ranking of 5% VaR and ES forecasting models based on the MCS procedure using AL log scores

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 2 | 1 | 1 | 5 | 1 | 1 | 1 | 2 | 8 | 1.8 | 1 |
| ALAR{}\_{\text{AR}}-AS | 3 | 4 | 2 | 13 | 4 | 2 | 2 | 3 | 8 | 4.1 | 2 |
| ALMult.{}\_{\text{Mult.}}-AS | 4 | 6 | 5 | 3 | 3 | 5 | 4 | 4 | 8 | 4.2 | 3 |
| QAR-QbSD-gAS | 1 | 2 | 14 | 4 | 2 | 4 | 6 | 1 | 8 | 4.2 | 4 |
| AR-ALAR{}\_{\text{AR}}-AS | 10 | 9 | 7 | 1 | 5 | 6 | 5 | 5 | 8 | 6.0 | 5 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 7 | 15 | 11 | 2 | 11 | 3 | 3 | 6 | 8 | 7.2 | 6 |
| GARCH-skew-tt | 6 | 5 | 4 | 10 | 7 | 8 |  | 9 | 7 | 9.6 | 7 |
| GJR-GARCH-skew-tt | 9 | 7 | 3 | 8 | 9 | 7 |  | 8 | 7 | 9.9 | 8 |
| EGARCH | 15 | 3 | 9 | 9 | 10 | 12 |  | 7 | 7 | 11.6 | 9 |
| AR-GJR-GARCH-skew-tt | 5 | 8 | 6 | 15 | 12 | 11 |  |  | 6 | 14.1 | 10 |
| QAR-QbSD-gSAV | 11 | 16 | 10 | 6 | 6 | 9 |  |  | 6 | 14.2 | 11 |
| AR-GARCH-skew-tt | 8 | 10 | 8 | 16 | 13 | 10 |  |  | 6 | 15.1 | 12 |
| GJR-GARCH-tt | 12 | 12 | 13 | 18 | 17 | 16 |  |  | 6 | 18.0 | 13 |
| AR-EGARCH | 20 | 11 | 16 | 14 | 14 | 14 |  |  | 6 | 18.1 | 14 |
| AR-ALAR{}\_{\text{AR}}-SAV | 16 | 18 | 18 | 11 | 22 | 13 |  |  | 6 | 19.2 | 15 |
| GARCH-tt | 13 | 13 | 12 | 26 | 18 | 17 |  |  | 6 | 19.4 | 16 |
| ALAR{}\_{\text{AR}}-SAV | 21 | 22 | 24 | 17 | 15 | 18 |  | 11 | 7 | 19.5 | 17 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 17 |  | 15 | 7 | 21 | 15 |  |  | 5 | 19.9 | 18 |
| AR-GJR-GARCH-tt | 14 | 14 | 22 | 19 | 20 | 19 |  |  | 6 | 20.5 | 19 |
| ALMult.{}\_{\text{Mult.}}-SAV |  | 20 | 11 | 16 | 22 |  | 10 | 5 | 5 | 20.5 | 20 |
| AR-GARCH-tt | 18 | 17 | 23 | 22 | 19 | 20 |  |  | 6 | 21.9 | 21 |
| QbSD-gSAV | 22 | 20 |  | 20 | 8 | 21 |  |  | 5 | 21.9 | 22 |
| GJR-GARCH-normal | 19 | 21 | 19 | 21 |  | 25 |  |  | 5 | 23.6 | 23 |
| AR-GJR-GARCH-normal |  | 19 |  | 24 |  | 23 |  |  | 3 | 25.8 | 24 |
| AR-GAS | 24 |  | 17 |  |  |  |  |  | 2 | 26.1 | 25 |
| GAS | 23 |  | 21 |  |  |  |  |  | 2 | 26.5 | 26 |
| GARCH-normal |  |  | 22 |  | 26 |  |  |  | 2 | 27.1 | 27 |
| AR-GARCH-normal |  |  | 25 | 25 |  | 25 |  |  | 2 | 27.1 | 28 |

Notes: For explanations, see notes of Table 8.

Figure 1: Time series plots of the daily log returns for the S&P 500, DJIA, NASDAQ, and EURO STOXX 50 indices over the sample period. Each plot represents the percentage daily returns computed from adjusted closing prices.

![Refer to caption](2603.02357v1/x1.png)


(a)

![Refer to caption](2603.02357v1/x2.png)


(b)

![Refer to caption](2603.02357v1/x3.png)


(c)

![Refer to caption](2603.02357v1/x4.png)


(d)




Figure 2: Time series plots of the daily log returns for the FTSE 100, DAX, CAC 40, and TSX indices over the sample period. Each plot displays percentage daily returns based on adjusted closing prices.

![Refer to caption](2603.02357v1/x5.png)


(a)

![Refer to caption](2603.02357v1/x6.png)


(b)

![Refer to caption](2603.02357v1/x7.png)


(c)

![Refer to caption](2603.02357v1/x8.png)


(d)

Supplementary material for:

Quantile-based modeling of scale dynamics in financial returns for Value-at-Risk and Expected Shortfall forecasting

Xiaochun Liu and Richard Luger

## Section A

Tables A1–A12 present comparisons of the mean absolute error (MAE) and root mean squared error (RMSE) for the QbSD forecasting approach,
examining the impact of the scale-defining quantile level pp on the computation of VaR and ES.
Specifically, we consider forecasts based on: (i) individual values of p∈{0.05,0.10,0.15,0.20,0.25}p\in\{0.05,0.10,0.15,0.20,0.25\}; (ii) the mean over these pp values; and (iii) the median over them.

The results are obtained from 1,000 replications for each configuration of the asymmetric power ARCH model with innovations drawn from the skewed tt-distribution, as specified in the main text.
The lowest MAE and RMSE values in each table are highlighted in bold.

Overall, the results in Tables A1–A12 suggest that combining forecasts over multiple quantile levels pp—either by taking the mean or, typically to a slightly lesser degree, the median—tends to yield lower forecast errors than relying on a single pp in isolation. This advantage of averaging is most noticeable when TT is relatively small (e.g., T=250T=250; see especially Tables A1–A4), where individual-pp estimates exhibit higher variability. As TT increases to 1250 (Tables A5–A8) or 2500 (Tables A9–A12), the performance gap narrows, yet the multi-pp strategies remain competitive or superior under most DGP configurations.

Although occasional scenarios arise where an individual pp may match or slightly outperform the combined forecasts (e.g., p=0.10p=0.10 in Table A7), no single pp exhibits consistent dominance across the wide range of parameter settings (leverage θ\theta, tail thickness vv, skewness λ\lambda) or sample sizes TT. Consequently, our findings recommend the “mean over pp” method as a robust, practically simple strategy for balancing estimation accuracy and stability in quantile-based VaR and ES forecasting.

Table A1. VaR forecasting results with the QbSD approach when θ=0\theta=0 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.243 | 0.181 | 0.146 |  | 0.304 | 0.222 | 0.173 |  | 0.328 | 0.214 | 0.158 |  | 0.436 | 0.269 | 0.189 |
| p=0.10p=0.10 |  | 0.235 | 0.172 | 0.138 |  | 0.281 | 0.204 | 0.157 |  | 0.318 | 0.206 | 0.148 |  | 0.402 | 0.251 | 0.173 |
| p=0.15p=0.15 |  | 0.228 | 0.170 | 0.139 |  | 0.287 | 0.206 | 0.161 |  | 0.318 | 0.209 | 0.149 |  | 0.407 | 0.252 | 0.177 |
| p=0.20p=0.20 |  | 0.237 | 0.181 | 0.149 |  | 0.297 | 0.220 | 0.171 |  | 0.319 | 0.212 | 0.158 |  | 0.422 | 0.260 | 0.185 |
| p=0.25p=0.25 |  | 0.246 | 0.190 | 0.152 |  | 0.302 | 0.225 | 0.176 |  | 0.325 | 0.220 | 0.159 |  | 0.427 | 0.265 | 0.186 |
| Mean over pp |  | 0.215 | 0.159 | 0.130 |  | 0.272 | 0.197 | 0.154 |  | 0.298 | 0.193 | 0.140 |  | 0.394 | 0.241 | 0.169 |
| Median over pp |  | 0.222 | 0.164 | 0.134 |  | 0.277 | 0.202 | 0.157 |  | 0.308 | 0.198 | 0.143 |  | 0.401 | 0.247 | 0.171 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.265 | 0.196 | 0.160 |  | 0.329 | 0.233 | 0.182 |  | 0.349 | 0.228 | 0.174 |  | 0.460 | 0.280 | 0.199 |
| p=0.10p=0.10 |  | 0.259 | 0.190 | 0.156 |  | 0.307 | 0.220 | 0.173 |  | 0.340 | 0.227 | 0.168 |  | 0.421 | 0.268 | 0.188 |
| p=0.15p=0.15 |  | 0.266 | 0.203 | 0.166 |  | 0.314 | 0.230 | 0.181 |  | 0.344 | 0.228 | 0.171 |  | 0.423 | 0.269 | 0.189 |
| p=0.20p=0.20 |  | 0.275 | 0.213 | 0.175 |  | 0.326 | 0.244 | 0.196 |  | 0.354 | 0.240 | 0.181 |  | 0.440 | 0.283 | 0.207 |
| p=0.25p=0.25 |  | 0.291 | 0.228 | 0.183 |  | 0.342 | 0.257 | 0.205 |  | 0.371 | 0.256 | 0.190 |  | 0.450 | 0.291 | 0.211 |
| Mean over pp |  | 0.238 | 0.178 | 0.146 |  | 0.288 | 0.211 | 0.168 |  | 0.315 | 0.208 | 0.155 |  | 0.402 | 0.251 | 0.180 |
| Median over pp |  | 0.247 | 0.185 | 0.152 |  | 0.297 | 0.219 | 0.172 |  | 0.324 | 0.214 | 0.161 |  | 0.412 | 0.258 | 0.184 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.308 | 0.232 | 0.188 |  | 0.388 | 0.291 | 0.228 |  | 0.422 | 0.287 | 0.214 |  | 0.567 | 0.370 | 0.267 |
| p=0.10p=0.10 |  | 0.305 | 0.228 | 0.184 |  | 0.360 | 0.268 | 0.206 |  | 0.417 | 0.282 | 0.204 |  | 0.518 | 0.341 | 0.232 |
| p=0.15p=0.15 |  | 0.290 | 0.222 | 0.180 |  | 0.363 | 0.269 | 0.212 |  | 0.410 | 0.280 | 0.203 |  | 0.532 | 0.344 | 0.240 |
| p=0.20p=0.20 |  | 0.306 | 0.238 | 0.194 |  | 0.381 | 0.287 | 0.225 |  | 0.415 | 0.287 | 0.212 |  | 0.549 | 0.357 | 0.255 |
| p=0.25p=0.25 |  | 0.318 | 0.253 | 0.202 |  | 0.390 | 0.299 | 0.235 |  | 0.422 | 0.301 | 0.215 |  | 0.565 | 0.368 | 0.262 |
| Mean over pp |  | 0.276 | 0.208 | 0.169 |  | 0.346 | 0.257 | 0.201 |  | 0.386 | 0.260 | 0.188 |  | 0.513 | 0.330 | 0.231 |
| Median over pp |  | 0.283 | 0.214 | 0.175 |  | 0.353 | 0.265 | 0.205 |  | 0.394 | 0.267 | 0.192 |  | 0.520 | 0.336 | 0.232 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.338 | 0.256 | 0.208 |  | 0.414 | 0.302 | 0.240 |  | 0.454 | 0.308 | 0.240 |  | 0.587 | 0.374 | 0.274 |
| p=0.10p=0.10 |  | 0.339 | 0.252 | 0.207 |  | 0.390 | 0.286 | 0.223 |  | 0.449 | 0.305 | 0.229 |  | 0.545 | 0.366 | 0.251 |
| p=0.15p=0.15 |  | 0.348 | 0.266 | 0.217 |  | 0.405 | 0.300 | 0.238 |  | 0.454 | 0.308 | 0.230 |  | 0.565 | 0.363 | 0.253 |
| p=0.20p=0.20 |  | 0.363 | 0.287 | 0.232 |  | 0.426 | 0.325 | 0.259 |  | 0.477 | 0.329 | 0.244 |  | 0.597 | 0.390 | 0.283 |
| p=0.25p=0.25 |  | 0.394 | 0.317 | 0.250 |  | 0.453 | 0.350 | 0.278 |  | 0.512 | 0.367 | 0.264 |  | 0.606 | 0.400 | 0.289 |
| Mean over pp |  | 0.311 | 0.236 | 0.191 |  | 0.371 | 0.273 | 0.217 |  | 0.415 | 0.280 | 0.207 |  | 0.529 | 0.338 | 0.239 |
| Median over pp |  | 0.324 | 0.246 | 0.201 |  | 0.381 | 0.285 | 0.222 |  | 0.426 | 0.289 | 0.217 |  | 0.544 | 0.349 | 0.244 |



Table A2. ES forecasting results with the QbSD approach when θ=0\theta=0 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.325 | 0.238 | 0.191 |  | 0.424 | 0.299 | 0.232 |  | 0.551 | 0.344 | 0.246 |  | 0.762 | 0.458 | 0.315 |
| p=0.10p=0.10 |  | 0.311 | 0.226 | 0.180 |  | 0.395 | 0.275 | 0.212 |  | 0.537 | 0.332 | 0.234 |  | 0.732 | 0.429 | 0.290 |
| p=0.15p=0.15 |  | 0.303 | 0.221 | 0.176 |  | 0.395 | 0.280 | 0.215 |  | 0.532 | 0.332 | 0.236 |  | 0.729 | 0.431 | 0.293 |
| p=0.20p=0.20 |  | 0.311 | 0.229 | 0.185 |  | 0.409 | 0.291 | 0.225 |  | 0.530 | 0.331 | 0.237 |  | 0.739 | 0.445 | 0.305 |
| p=0.25p=0.25 |  | 0.319 | 0.241 | 0.195 |  | 0.413 | 0.297 | 0.234 |  | 0.538 | 0.341 | 0.246 |  | 0.744 | 0.447 | 0.306 |
| Mean over pp |  | 0.293 | 0.211 | 0.167 |  | 0.387 | 0.269 | 0.206 |  | 0.519 | 0.317 | 0.221 |  | 0.724 | 0.424 | 0.285 |
| Median over pp |  | 0.302 | 0.217 | 0.172 |  | 0.393 | 0.275 | 0.210 |  | 0.526 | 0.323 | 0.227 |  | 0.728 | 0.429 | 0.289 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.353 | 0.260 | 0.210 |  | 0.457 | 0.327 | 0.254 |  | 0.578 | 0.368 | 0.266 |  | 0.805 | 0.494 | 0.343 |
| p=0.10p=0.10 |  | 0.337 | 0.252 | 0.203 |  | 0.424 | 0.301 | 0.234 |  | 0.549 | 0.350 | 0.255 |  | 0.749 | 0.449 | 0.310 |
| p=0.15p=0.15 |  | 0.340 | 0.259 | 0.212 |  | 0.426 | 0.307 | 0.242 |  | 0.557 | 0.357 | 0.260 |  | 0.744 | 0.450 | 0.312 |
| p=0.20p=0.20 |  | 0.346 | 0.268 | 0.221 |  | 0.431 | 0.319 | 0.255 |  | 0.555 | 0.362 | 0.270 |  | 0.748 | 0.462 | 0.327 |
| p=0.25p=0.25 |  | 0.355 | 0.281 | 0.234 |  | 0.447 | 0.332 | 0.268 |  | 0.571 | 0.378 | 0.282 |  | 0.770 | 0.476 | 0.336 |
| Mean over pp |  | 0.311 | 0.233 | 0.189 |  | 0.403 | 0.286 | 0.226 |  | 0.528 | 0.331 | 0.238 |  | 0.734 | 0.437 | 0.300 |
| Median over pp |  | 0.321 | 0.241 | 0.197 |  | 0.410 | 0.294 | 0.231 |  | 0.539 | 0.338 | 0.246 |  | 0.741 | 0.444 | 0.306 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.406 | 0.302 | 0.242 |  | 0.526 | 0.383 | 0.302 |  | 0.683 | 0.440 | 0.321 |  | 0.943 | 0.591 | 0.420 |
| p=0.10p=0.10 |  | 0.395 | 0.294 | 0.237 |  | 0.488 | 0.352 | 0.274 |  | 0.665 | 0.426 | 0.311 |  | 0.885 | 0.539 | 0.375 |
| p=0.15p=0.15 |  | 0.378 | 0.282 | 0.227 |  | 0.489 | 0.352 | 0.276 |  | 0.656 | 0.420 | 0.305 |  | 0.893 | 0.544 | 0.379 |
| p=0.20p=0.20 |  | 0.390 | 0.296 | 0.242 |  | 0.507 | 0.369 | 0.291 |  | 0.656 | 0.421 | 0.310 |  | 0.913 | 0.562 | 0.395 |
| p=0.25p=0.25 |  | 0.408 | 0.312 | 0.256 |  | 0.518 | 0.380 | 0.304 |  | 0.672 | 0.436 | 0.321 |  | 0.930 | 0.577 | 0.408 |
| Mean over pp |  | 0.366 | 0.270 | 0.216 |  | 0.477 | 0.340 | 0.265 |  | 0.637 | 0.400 | 0.288 |  | 0.881 | 0.534 | 0.370 |
| Median over pp |  | 0.376 | 0.277 | 0.223 |  | 0.485 | 0.347 | 0.270 |  | 0.647 | 0.407 | 0.294 |  | 0.886 | 0.538 | 0.374 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.441 | 0.332 | 0.270 |  | 0.561 | 0.410 | 0.323 |  | 0.719 | 0.471 | 0.350 |  | 0.981 | 0.617 | 0.437 |
| p=0.10p=0.10 |  | 0.432 | 0.328 | 0.266 |  | 0.527 | 0.381 | 0.299 |  | 0.705 | 0.458 | 0.339 |  | 0.923 | 0.568 | 0.402 |
| p=0.15p=0.15 |  | 0.440 | 0.339 | 0.277 |  | 0.534 | 0.391 | 0.312 |  | 0.711 | 0.464 | 0.343 |  | 0.934 | 0.574 | 0.405 |
| p=0.20p=0.20 |  | 0.448 | 0.352 | 0.293 |  | 0.550 | 0.413 | 0.335 |  | 0.717 | 0.480 | 0.360 |  | 0.945 | 0.596 | 0.429 |
| p=0.25p=0.25 |  | 0.478 | 0.384 | 0.322 |  | 0.576 | 0.439 | 0.359 |  | 0.745 | 0.513 | 0.390 |  | 0.981 | 0.621 | 0.447 |
| Mean over pp |  | 0.402 | 0.305 | 0.248 |  | 0.504 | 0.364 | 0.287 |  | 0.669 | 0.429 | 0.314 |  | 0.905 | 0.551 | 0.385 |
| Median over pp |  | 0.416 | 0.316 | 0.259 |  | 0.512 | 0.373 | 0.296 |  | 0.684 | 0.439 | 0.324 |  | 0.915 | 0.561 | 0.394 |



Table A3. VaR forecasting results with the QbSD approach when θ=0.5\theta=0.5 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.327 | 0.252 | 0.206 |  | 0.415 | 0.314 | 0.245 |  | 0.401 | 0.277 | 0.206 |  | 0.553 | 0.355 | 0.259 |
| p=0.10p=0.10 |  | 0.316 | 0.241 | 0.195 |  | 0.397 | 0.295 | 0.231 |  | 0.380 | 0.257 | 0.190 |  | 0.514 | 0.333 | 0.237 |
| p=0.15p=0.15 |  | 0.316 | 0.243 | 0.197 |  | 0.404 | 0.301 | 0.235 |  | 0.381 | 0.257 | 0.192 |  | 0.528 | 0.338 | 0.238 |
| p=0.20p=0.20 |  | 0.324 | 0.247 | 0.202 |  | 0.423 | 0.316 | 0.248 |  | 0.388 | 0.266 | 0.195 |  | 0.536 | 0.347 | 0.245 |
| p=0.25p=0.25 |  | 0.333 | 0.255 | 0.205 |  | 0.442 | 0.327 | 0.258 |  | 0.402 | 0.273 | 0.202 |  | 0.574 | 0.367 | 0.264 |
| Mean over pp |  | 0.303 | 0.231 | 0.187 |  | 0.390 | 0.291 | 0.228 |  | 0.369 | 0.249 | 0.184 |  | 0.510 | 0.326 | 0.233 |
| Median over pp |  | 0.307 | 0.232 | 0.190 |  | 0.395 | 0.294 | 0.231 |  | 0.373 | 0.250 | 0.186 |  | 0.515 | 0.330 | 0.235 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.283 | 0.213 | 0.172 |  | 0.388 | 0.276 | 0.222 |  | 0.380 | 0.252 | 0.193 |  | 0.546 | 0.344 | 0.250 |
| p=0.10p=0.10 |  | 0.272 | 0.207 | 0.167 |  | 0.354 | 0.257 | 0.203 |  | 0.357 | 0.238 | 0.177 |  | 0.505 | 0.318 | 0.226 |
| p=0.15p=0.15 |  | 0.288 | 0.220 | 0.178 |  | 0.369 | 0.269 | 0.215 |  | 0.365 | 0.245 | 0.184 |  | 0.510 | 0.317 | 0.233 |
| p=0.20p=0.20 |  | 0.304 | 0.233 | 0.189 |  | 0.388 | 0.288 | 0.230 |  | 0.379 | 0.258 | 0.195 |  | 0.525 | 0.336 | 0.244 |
| p=0.25p=0.25 |  | 0.327 | 0.253 | 0.205 |  | 0.416 | 0.315 | 0.252 |  | 0.399 | 0.270 | 0.201 |  | 0.557 | 0.361 | 0.262 |
| Mean over pp |  | 0.257 | 0.196 | 0.160 |  | 0.339 | 0.248 | 0.199 |  | 0.335 | 0.222 | 0.168 |  | 0.482 | 0.302 | 0.218 |
| Median over pp |  | 0.266 | 0.199 | 0.164 |  | 0.350 | 0.257 | 0.205 |  | 0.343 | 0.227 | 0.170 |  | 0.490 | 0.306 | 0.226 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.441 | 0.347 | 0.285 |  | 0.571 | 0.440 | 0.345 |  | 0.549 | 0.396 | 0.300 |  | 0.766 | 0.528 | 0.387 |
| p=0.10p=0.10 |  | 0.417 | 0.326 | 0.267 |  | 0.526 | 0.402 | 0.319 |  | 0.512 | 0.366 | 0.274 |  | 0.707 | 0.485 | 0.348 |
| p=0.15p=0.15 |  | 0.420 | 0.331 | 0.271 |  | 0.548 | 0.421 | 0.331 |  | 0.512 | 0.365 | 0.278 |  | 0.740 | 0.497 | 0.351 |
| p=0.20p=0.20 |  | 0.437 | 0.342 | 0.278 |  | 0.569 | 0.443 | 0.350 |  | 0.532 | 0.380 | 0.281 |  | 0.733 | 0.500 | 0.353 |
| p=0.25p=0.25 |  | 0.449 | 0.354 | 0.282 |  | 0.604 | 0.466 | 0.362 |  | 0.571 | 0.395 | 0.297 |  | 0.849 | 0.551 | 0.394 |
| Mean over pp |  | 0.401 | 0.314 | 0.255 |  | 0.522 | 0.403 | 0.318 |  | 0.500 | 0.353 | 0.265 |  | 0.707 | 0.477 | 0.339 |
| Median over pp |  | 0.406 | 0.317 | 0.262 |  | 0.534 | 0.409 | 0.322 |  | 0.502 | 0.351 | 0.268 |  | 0.711 | 0.487 | 0.343 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.378 | 0.291 | 0.240 |  | 0.523 | 0.383 | 0.318 |  | 0.517 | 0.356 | 0.281 |  | 0.762 | 0.513 | 0.393 |
| p=0.10p=0.10 |  | 0.365 | 0.284 | 0.228 |  | 0.476 | 0.363 | 0.286 |  | 0.484 | 0.342 | 0.250 |  | 0.690 | 0.486 | 0.344 |
| p=0.15p=0.15 |  | 0.391 | 0.303 | 0.244 |  | 0.512 | 0.387 | 0.309 |  | 0.499 | 0.329 | 0.252 |  | 0.772 | 0.483 | 0.357 |
| p=0.20p=0.20 |  | 0.421 | 0.328 | 0.266 |  | 0.547 | 0.411 | 0.330 |  | 0.550 | 0.367 | 0.278 |  | 0.815 | 0.516 | 0.378 |
| p=0.25p=0.25 |  | 0.456 | 0.367 | 0.296 |  | 0.595 | 0.470 | 0.367 |  | 0.605 | 0.396 | 0.295 |  | 0.815 | 0.546 | 0.393 |
| Mean over pp |  | 0.340 | 0.262 | 0.214 |  | 0.454 | 0.342 | 0.276 |  | 0.455 | 0.302 | 0.229 |  | 0.675 | 0.443 | 0.322 |
| Median over pp |  | 0.356 | 0.270 | 0.225 |  | 0.479 | 0.363 | 0.290 |  | 0.468 | 0.310 | 0.236 |  | 0.702 | 0.459 | 0.342 |



Table A4. ES forecasting results with the QbSD approach when θ=0.5\theta=0.5 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.420 | 0.324 | 0.266 |  | 0.557 | 0.414 | 0.329 |  | 0.654 | 0.425 | 0.314 |  | 0.945 | 0.585 | 0.412 |
| p=0.10p=0.10 |  | 0.401 | 0.309 | 0.254 |  | 0.527 | 0.392 | 0.311 |  | 0.619 | 0.398 | 0.291 |  | 0.888 | 0.539 | 0.379 |
| p=0.15p=0.15 |  | 0.396 | 0.308 | 0.254 |  | 0.537 | 0.399 | 0.316 |  | 0.611 | 0.393 | 0.289 |  | 0.907 | 0.553 | 0.386 |
| p=0.20p=0.20 |  | 0.401 | 0.314 | 0.259 |  | 0.549 | 0.412 | 0.329 |  | 0.625 | 0.403 | 0.298 |  | 0.913 | 0.563 | 0.397 |
| p=0.25p=0.25 |  | 0.409 | 0.323 | 0.266 |  | 0.566 | 0.431 | 0.344 |  | 0.635 | 0.414 | 0.306 |  | 0.942 | 0.593 | 0.423 |
| Mean over pp |  | 0.385 | 0.298 | 0.244 |  | 0.524 | 0.387 | 0.307 |  | 0.608 | 0.388 | 0.284 |  | 0.894 | 0.540 | 0.376 |
| Median over pp |  | 0.391 | 0.301 | 0.246 |  | 0.529 | 0.390 | 0.308 |  | 0.613 | 0.392 | 0.286 |  | 0.902 | 0.544 | 0.378 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.382 | 0.281 | 0.227 |  | 0.544 | 0.386 | 0.301 |  | 0.629 | 0.401 | 0.292 |  | 0.948 | 0.591 | 0.416 |
| p=0.10p=0.10 |  | 0.357 | 0.268 | 0.216 |  | 0.490 | 0.349 | 0.272 |  | 0.584 | 0.370 | 0.269 |  | 0.883 | 0.535 | 0.373 |
| p=0.15p=0.15 |  | 0.366 | 0.279 | 0.227 |  | 0.507 | 0.363 | 0.285 |  | 0.590 | 0.376 | 0.276 |  | 0.888 | 0.538 | 0.372 |
| p=0.20p=0.20 |  | 0.377 | 0.293 | 0.242 |  | 0.511 | 0.377 | 0.301 |  | 0.595 | 0.387 | 0.288 |  | 0.891 | 0.550 | 0.387 |
| p=0.25p=0.25 |  | 0.402 | 0.316 | 0.264 |  | 0.538 | 0.407 | 0.331 |  | 0.613 | 0.406 | 0.304 |  | 0.913 | 0.572 | 0.414 |
| Mean over pp |  | 0.337 | 0.253 | 0.207 |  | 0.475 | 0.337 | 0.266 |  | 0.566 | 0.353 | 0.256 |  | 0.869 | 0.518 | 0.360 |
| Median over pp |  | 0.347 | 0.261 | 0.212 |  | 0.487 | 0.348 | 0.273 |  | 0.575 | 0.360 | 0.262 |  | 0.874 | 0.524 | 0.364 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.557 | 0.437 | 0.364 |  | 0.746 | 0.565 | 0.458 |  | 0.851 | 0.576 | 0.438 |  | 1.246 | 0.801 | 0.586 |
| p=0.10p=0.10 |  | 0.522 | 0.408 | 0.340 |  | 0.694 | 0.521 | 0.421 |  | 0.795 | 0.529 | 0.400 |  | 1.147 | 0.728 | 0.530 |
| p=0.15p=0.15 |  | 0.523 | 0.412 | 0.343 |  | 0.715 | 0.539 | 0.434 |  | 0.788 | 0.526 | 0.397 |  | 1.180 | 0.749 | 0.541 |
| p=0.20p=0.20 |  | 0.540 | 0.428 | 0.356 |  | 0.732 | 0.559 | 0.453 |  | 0.812 | 0.545 | 0.412 |  | 1.207 | 0.762 | 0.549 |
| p=0.25p=0.25 |  | 0.547 | 0.436 | 0.364 |  | 0.764 | 0.591 | 0.480 |  | 0.843 | 0.572 | 0.433 |  | 1.300 | 0.843 | 0.613 |
| Mean over pp |  | 0.506 | 0.396 | 0.328 |  | 0.689 | 0.520 | 0.419 |  | 0.782 | 0.519 | 0.389 |  | 1.167 | 0.734 | 0.527 |
| Median over pp |  | 0.512 | 0.400 | 0.333 |  | 0.701 | 0.528 | 0.425 |  | 0.790 | 0.522 | 0.391 |  | 1.174 | 0.740 | 0.532 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.489 | 0.372 | 0.305 |  | 0.705 | 0.517 | 0.414 |  | 0.813 | 0.537 | 0.403 |  | 1.270 | 0.812 | 0.593 |
| p=0.10p=0.10 |  | 0.467 | 0.357 | 0.294 |  | 0.639 | 0.467 | 0.373 |  | 0.751 | 0.491 | 0.366 |  | 1.146 | 0.714 | 0.515 |
| p=0.15p=0.15 |  | 0.482 | 0.374 | 0.310 |  | 0.676 | 0.499 | 0.401 |  | 0.770 | 0.498 | 0.368 |  | 1.185 | 0.745 | 0.536 |
| p=0.20p=0.20 |  | 0.510 | 0.404 | 0.337 |  | 0.691 | 0.519 | 0.422 |  | 0.797 | 0.534 | 0.403 |  | 1.205 | 0.768 | 0.563 |
| p=0.25p=0.25 |  | 0.547 | 0.442 | 0.375 |  | 0.744 | 0.579 | 0.478 |  | 0.837 | 0.577 | 0.439 |  | 1.267 | 0.817 | 0.600 |
| Mean over pp |  | 0.439 | 0.333 | 0.274 |  | 0.619 | 0.449 | 0.359 |  | 0.727 | 0.464 | 0.340 |  | 1.125 | 0.689 | 0.491 |
| Median over pp |  | 0.454 | 0.346 | 0.284 |  | 0.640 | 0.469 | 0.375 |  | 0.745 | 0.475 | 0.349 |  | 1.144 | 0.705 | 0.509 |



Table A5. VaR forecasting results with the QbSD approach when θ=0\theta=0 and T=1250T=1250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.106 | 0.080 | 0.064 |  | 0.138 | 0.099 | 0.077 |  | 0.152 | 0.099 | 0.073 |  | 0.208 | 0.126 | 0.087 |
| p=0.10p=0.10 |  | 0.106 | 0.078 | 0.061 |  | 0.135 | 0.094 | 0.072 |  | 0.148 | 0.092 | 0.065 |  | 0.201 | 0.117 | 0.079 |
| p=0.15p=0.15 |  | 0.108 | 0.079 | 0.062 |  | 0.136 | 0.096 | 0.073 |  | 0.149 | 0.094 | 0.066 |  | 0.201 | 0.119 | 0.081 |
| p=0.20p=0.20 |  | 0.109 | 0.081 | 0.064 |  | 0.139 | 0.097 | 0.075 |  | 0.149 | 0.094 | 0.067 |  | 0.201 | 0.119 | 0.082 |
| p=0.25p=0.25 |  | 0.115 | 0.088 | 0.068 |  | 0.143 | 0.103 | 0.079 |  | 0.151 | 0.099 | 0.070 |  | 0.202 | 0.121 | 0.083 |
| Mean over pp |  | 0.101 | 0.075 | 0.059 |  | 0.132 | 0.092 | 0.071 |  | 0.142 | 0.089 | 0.063 |  | 0.196 | 0.115 | 0.079 |
| Median over pp |  | 0.103 | 0.076 | 0.060 |  | 0.133 | 0.093 | 0.072 |  | 0.144 | 0.090 | 0.064 |  | 0.198 | 0.116 | 0.079 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.117 | 0.088 | 0.071 |  | 0.144 | 0.106 | 0.082 |  | 0.163 | 0.108 | 0.081 |  | 0.213 | 0.133 | 0.093 |
| p=0.10p=0.10 |  | 0.116 | 0.086 | 0.069 |  | 0.142 | 0.102 | 0.077 |  | 0.156 | 0.101 | 0.073 |  | 0.207 | 0.127 | 0.086 |
| p=0.15p=0.15 |  | 0.116 | 0.087 | 0.069 |  | 0.142 | 0.101 | 0.077 |  | 0.156 | 0.100 | 0.073 |  | 0.204 | 0.125 | 0.084 |
| p=0.20p=0.20 |  | 0.123 | 0.092 | 0.072 |  | 0.147 | 0.103 | 0.080 |  | 0.160 | 0.104 | 0.075 |  | 0.205 | 0.123 | 0.086 |
| p=0.25p=0.25 |  | 0.129 | 0.099 | 0.079 |  | 0.150 | 0.112 | 0.087 |  | 0.163 | 0.108 | 0.078 |  | 0.205 | 0.126 | 0.088 |
| Mean over pp |  | 0.109 | 0.081 | 0.064 |  | 0.136 | 0.096 | 0.073 |  | 0.148 | 0.094 | 0.068 |  | 0.197 | 0.118 | 0.081 |
| Median over pp |  | 0.110 | 0.082 | 0.065 |  | 0.137 | 0.097 | 0.073 |  | 0.150 | 0.096 | 0.069 |  | 0.199 | 0.120 | 0.082 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.139 | 0.107 | 0.085 |  | 0.182 | 0.133 | 0.103 |  | 0.204 | 0.134 | 0.099 |  | 0.275 | 0.169 | 0.119 |
| p=0.10p=0.10 |  | 0.135 | 0.102 | 0.080 |  | 0.175 | 0.123 | 0.093 |  | 0.192 | 0.121 | 0.087 |  | 0.265 | 0.155 | 0.105 |
| p=0.15p=0.15 |  | 0.137 | 0.103 | 0.081 |  | 0.175 | 0.125 | 0.094 |  | 0.194 | 0.124 | 0.088 |  | 0.264 | 0.158 | 0.106 |
| p=0.20p=0.20 |  | 0.141 | 0.107 | 0.084 |  | 0.178 | 0.127 | 0.097 |  | 0.199 | 0.126 | 0.090 |  | 0.265 | 0.158 | 0.108 |
| p=0.25p=0.25 |  | 0.151 | 0.115 | 0.090 |  | 0.184 | 0.133 | 0.102 |  | 0.201 | 0.130 | 0.092 |  | 0.264 | 0.159 | 0.109 |
| Mean over pp |  | 0.129 | 0.097 | 0.076 |  | 0.168 | 0.119 | 0.090 |  | 0.186 | 0.117 | 0.083 |  | 0.256 | 0.151 | 0.102 |
| Median over pp |  | 0.131 | 0.098 | 0.077 |  | 0.170 | 0.121 | 0.092 |  | 0.189 | 0.118 | 0.084 |  | 0.258 | 0.152 | 0.103 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.154 | 0.118 | 0.095 |  | 0.190 | 0.140 | 0.108 |  | 0.216 | 0.145 | 0.109 |  | 0.283 | 0.178 | 0.126 |
| p=0.10p=0.10 |  | 0.150 | 0.114 | 0.090 |  | 0.185 | 0.134 | 0.101 |  | 0.205 | 0.133 | 0.097 |  | 0.271 | 0.168 | 0.114 |
| p=0.15p=0.15 |  | 0.150 | 0.114 | 0.090 |  | 0.185 | 0.134 | 0.102 |  | 0.204 | 0.132 | 0.097 |  | 0.270 | 0.166 | 0.112 |
| p=0.20p=0.20 |  | 0.159 | 0.121 | 0.096 |  | 0.190 | 0.138 | 0.105 |  | 0.213 | 0.140 | 0.102 |  | 0.269 | 0.165 | 0.113 |
| p=0.25p=0.25 |  | 0.170 | 0.132 | 0.104 |  | 0.193 | 0.146 | 0.112 |  | 0.215 | 0.144 | 0.105 |  | 0.267 | 0.166 | 0.117 |
| Mean over pp |  | 0.139 | 0.106 | 0.083 |  | 0.174 | 0.126 | 0.095 |  | 0.193 | 0.124 | 0.090 |  | 0.257 | 0.156 | 0.106 |
| Median over pp |  | 0.141 | 0.107 | 0.084 |  | 0.175 | 0.127 | 0.095 |  | 0.196 | 0.126 | 0.091 |  | 0.258 | 0.157 | 0.107 |



Table A6. ES forecasting results with the QbSD approach when θ=0\theta=0 and T=1250T=1250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute er ror | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.144 | 0.105 | 0.087 |  | 0.191 | 0.137 | 0.109 |  | 0.263 | 0.164 | 0.121 |  | 0.367 | 0.222 | 0.160 |
| p=0.10p=0.10 |  | 0.139 | 0.102 | 0.085 |  | 0.184 | 0.131 | 0.105 |  | 0.254 | 0.155 | 0.114 |  | 0.357 | 0.213 | 0.151 |
| p=0.15p=0.15 |  | 0.140 | 0.104 | 0.087 |  | 0.183 | 0.131 | 0.106 |  | 0.251 | 0.156 | 0.115 |  | 0.356 | 0.213 | 0.151 |
| p=0.20p=0.20 |  | 0.142 | 0.106 | 0.087 |  | 0.187 | 0.133 | 0.107 |  | 0.253 | 0.157 | 0.115 |  | 0.356 | 0.213 | 0.150 |
| p=0.25p=0.25 |  | 0.148 | 0.111 | 0.092 |  | 0.191 | 0.137 | 0.111 |  | 0.255 | 0.158 | 0.117 |  | 0.356 | 0.214 | 0.150 |
| Mean over pp |  | 0.136 | 0.100 | 0.082 |  | 0.181 | 0.128 | 0.103 |  | 0.248 | 0.151 | 0.111 |  | 0.353 | 0.210 | 0.148 |
| Median over pp |  | 0.137 | 0.101 | 0.083 |  | 0.183 | 0.129 | 0.104 |  | 0.250 | 0.152 | 0.112 |  | 0.355 | 0.211 | 0.148 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.153 | 0.114 | 0.096 |  | 0.198 | 0.143 | 0.116 |  | 0.271 | 0.170 | 0.129 |  | 0.377 | 0.231 | 0.168 |
| p=0.10p=0.10 |  | 0.149 | 0.113 | 0.094 |  | 0.194 | 0.140 | 0.113 |  | 0.261 | 0.163 | 0.123 |  | 0.366 | 0.221 | 0.160 |
| p=0.15p=0.15 |  | 0.147 | 0.113 | 0.093 |  | 0.189 | 0.138 | 0.112 |  | 0.255 | 0.161 | 0.121 |  | 0.360 | 0.216 | 0.157 |
| p=0.20p=0.20 |  | 0.153 | 0.118 | 0.098 |  | 0.194 | 0.142 | 0.115 |  | 0.260 | 0.165 | 0.125 |  | 0.357 | 0.215 | 0.155 |
| p=0.25p=0.25 |  | 0.160 | 0.124 | 0.104 |  | 0.195 | 0.146 | 0.119 |  | 0.263 | 0.168 | 0.126 |  | 0.354 | 0.216 | 0.156 |
| Mean over pp |  | 0.140 | 0.106 | 0.088 |  | 0.185 | 0.133 | 0.107 |  | 0.251 | 0.155 | 0.116 |  | 0.354 | 0.211 | 0.152 |
| Median over pp |  | 0.142 | 0.107 | 0.089 |  | 0.186 | 0.133 | 0.108 |  | 0.253 | 0.155 | 0.117 |  | 0.356 | 0.212 | 0.153 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.184 | 0.138 | 0.115 |  | 0.247 | 0.180 | 0.146 |  | 0.335 | 0.215 | 0.160 |  | 0.469 | 0.289 | 0.209 |
| p=0.10p=0.10 |  | 0.177 | 0.132 | 0.109 |  | 0.233 | 0.168 | 0.134 |  | 0.316 | 0.199 | 0.146 |  | 0.446 | 0.271 | 0.193 |
| p=0.15p=0.15 |  | 0.179 | 0.133 | 0.111 |  | 0.234 | 0.170 | 0.137 |  | 0.319 | 0.202 | 0.149 |  | 0.444 | 0.272 | 0.194 |
| p=0.20p=0.20 |  | 0.182 | 0.138 | 0.115 |  | 0.238 | 0.173 | 0.139 |  | 0.320 | 0.206 | 0.153 |  | 0.444 | 0.272 | 0.195 |
| p=0.25p=0.25 |  | 0.191 | 0.146 | 0.121 |  | 0.242 | 0.177 | 0.143 |  | 0.321 | 0.204 | 0.152 |  | 0.442 | 0.271 | 0.193 |
| Mean over pp |  | 0.172 | 0.127 | 0.105 |  | 0.229 | 0.164 | 0.132 |  | 0.312 | 0.195 | 0.143 |  | 0.440 | 0.266 | 0.189 |
| Median over pp |  | 0.174 | 0.129 | 0.107 |  | 0.231 | 0.166 | 0.133 |  | 0.314 | 0.197 | 0.144 |  | 0.442 | 0.267 | 0.190 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.197 | 0.151 | 0.127 |  | 0.251 | 0.187 | 0.152 |  | 0.346 | 0.225 | 0.172 |  | 0.472 | 0.295 | 0.217 |
| p=0.10p=0.10 |  | 0.191 | 0.146 | 0.122 |  | 0.246 | 0.180 | 0.145 |  | 0.329 | 0.211 | 0.159 |  | 0.456 | 0.281 | 0.204 |
| p=0.15p=0.15 |  | 0.189 | 0.144 | 0.121 |  | 0.244 | 0.179 | 0.145 |  | 0.327 | 0.209 | 0.157 |  | 0.448 | 0.277 | 0.201 |
| p=0.20p=0.20 |  | 0.198 | 0.154 | 0.128 |  | 0.248 | 0.184 | 0.150 |  | 0.333 | 0.218 | 0.164 |  | 0.447 | 0.276 | 0.201 |
| p=0.25p=0.25 |  | 0.208 | 0.163 | 0.137 |  | 0.248 | 0.187 | 0.152 |  | 0.332 | 0.217 | 0.164 |  | 0.441 | 0.272 | 0.198 |
| Mean over pp |  | 0.180 | 0.136 | 0.113 |  | 0.233 | 0.170 | 0.138 |  | 0.318 | 0.201 | 0.150 |  | 0.439 | 0.267 | 0.193 |
| Median over pp |  | 0.181 | 0.137 | 0.115 |  | 0.234 | 0.171 | 0.138 |  | 0.320 | 0.202 | 0.151 |  | 0.441 | 0.268 | 0.194 |



Table A7. VaR forecasting results with the QbSD approach when θ=0.5\theta=0.5 and T=1250T=1250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.226 | 0.180 | 0.147 |  | 0.286 | 0.218 | 0.171 |  | 0.252 | 0.180 | 0.138 |  | 0.339 | 0.224 | 0.162 |
| p=0.10p=0.10 |  | 0.225 | 0.178 | 0.145 |  | 0.286 | 0.218 | 0.170 |  | 0.250 | 0.173 | 0.132 |  | 0.339 | 0.222 | 0.157 |
| p=0.15p=0.15 |  | 0.230 | 0.181 | 0.148 |  | 0.289 | 0.220 | 0.172 |  | 0.252 | 0.176 | 0.135 |  | 0.342 | 0.225 | 0.160 |
| p=0.20p=0.20 |  | 0.231 | 0.183 | 0.149 |  | 0.291 | 0.223 | 0.174 |  | 0.250 | 0.177 | 0.134 |  | 0.339 | 0.225 | 0.162 |
| p=0.25p=0.25 |  | 0.235 | 0.185 | 0.151 |  | 0.296 | 0.226 | 0.178 |  | 0.255 | 0.180 | 0.139 |  | 0.342 | 0.226 | 0.163 |
| Mean over pp |  | 0.225 | 0.178 | 0.145 |  | 0.284 | 0.217 | 0.169 |  | 0.247 | 0.173 | 0.132 |  | 0.333 | 0.219 | 0.156 |
| Median over pp |  | 0.226 | 0.179 | 0.146 |  | 0.284 | 0.217 | 0.169 |  | 0.248 | 0.174 | 0.133 |  | 0.335 | 0.220 | 0.157 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.128 | 0.099 | 0.080 |  | 0.177 | 0.133 | 0.103 |  | 0.175 | 0.119 | 0.087 |  | 0.258 | 0.164 | 0.114 |
| p=0.10p=0.10 |  | 0.126 | 0.097 | 0.077 |  | 0.171 | 0.129 | 0.098 |  | 0.170 | 0.113 | 0.082 |  | 0.248 | 0.159 | 0.108 |
| p=0.15p=0.15 |  | 0.130 | 0.098 | 0.079 |  | 0.177 | 0.131 | 0.101 |  | 0.170 | 0.111 | 0.082 |  | 0.251 | 0.163 | 0.112 |
| p=0.20p=0.20 |  | 0.134 | 0.103 | 0.081 |  | 0.180 | 0.134 | 0.103 |  | 0.176 | 0.116 | 0.084 |  | 0.252 | 0.163 | 0.112 |
| p=0.25p=0.25 |  | 0.140 | 0.109 | 0.087 |  | 0.186 | 0.142 | 0.110 |  | 0.176 | 0.118 | 0.086 |  | 0.254 | 0.165 | 0.114 |
| Mean over pp |  | 0.120 | 0.092 | 0.072 |  | 0.164 | 0.124 | 0.094 |  | 0.161 | 0.106 | 0.076 |  | 0.239 | 0.152 | 0.104 |
| Median over pp |  | 0.121 | 0.093 | 0.074 |  | 0.167 | 0.125 | 0.095 |  | 0.164 | 0.107 | 0.078 |  | 0.242 | 0.155 | 0.106 |
| Panel B: Root mean square d error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.297 | 0.236 | 0.193 |  | 0.383 | 0.294 | 0.228 |  | 0.345 | 0.246 | 0.188 |  | 0.461 | 0.312 | 0.220 |
| p=0.10p=0.10 |  | 0.299 | 0.238 | 0.193 |  | 0.385 | 0.295 | 0.228 |  | 0.333 | 0.236 | 0.178 |  | 0.465 | 0.309 | 0.216 |
| p=0.15p=0.15 |  | 0.305 | 0.243 | 0.198 |  | 0.392 | 0.300 | 0.232 |  | 0.340 | 0.241 | 0.183 |  | 0.474 | 0.316 | 0.219 |
| p=0.20p=0.20 |  | 0.307 | 0.245 | 0.200 |  | 0.395 | 0.305 | 0.236 |  | 0.340 | 0.244 | 0.185 |  | 0.477 | 0.320 | 0.224 |
| p=0.25p=0.25 |  | 0.309 | 0.247 | 0.202 |  | 0.401 | 0.308 | 0.240 |  | 0.345 | 0.246 | 0.187 |  | 0.483 | 0.323 | 0.228 |
| Mean over pp |  | 0.297 | 0.236 | 0.193 |  | 0.382 | 0.293 | 0.227 |  | 0.331 | 0.235 | 0.178 |  | 0.456 | 0.304 | 0.212 |
| Median over pp |  | 0.299 | 0.238 | 0.194 |  | 0.383 | 0.294 | 0.227 |  | 0.333 | 0.236 | 0.179 |  | 0.458 | 0.305 | 0.212 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.174 | 0.140 | 0.110 |  | 0.248 | 0.190 | 0.145 |  | 0.245 | 0.170 | 0.125 |  | 0.371 | 0.239 | 0.166 |
| p=0.10p=0.10 |  | 0.167 | 0.132 | 0.102 |  | 0.235 | 0.180 | 0.133 |  | 0.230 | 0.157 | 0.112 |  | 0.347 | 0.228 | 0.151 |
| p=0.15p=0.15 |  | 0.175 | 0.135 | 0.107 |  | 0.244 | 0.183 | 0.139 |  | 0.228 | 0.155 | 0.111 |  | 0.366 | 0.240 | 0.162 |
| p=0.20p=0.20 |  | 0.181 | 0.144 | 0.113 |  | 0.248 | 0.188 | 0.143 |  | 0.238 | 0.162 | 0.116 |  | 0.361 | 0.242 | 0.163 |
| p=0.25p=0.25 |  | 0.187 | 0.152 | 0.120 |  | 0.259 | 0.203 | 0.155 |  | 0.237 | 0.163 | 0.119 |  | 0.371 | 0.249 | 0.172 |
| Mean over pp |  | 0.159 | 0.126 | 0.098 |  | 0.225 | 0.172 | 0.129 |  | 0.215 | 0.146 | 0.103 |  | 0.334 | 0.218 | 0.145 |
| Median over pp |  | 0.160 | 0.127 | 0.099 |  | 0.228 | 0.173 | 0.130 |  | 0.218 | 0.147 | 0.104 |  | 0.345 | 0.223 | 0.151 |



Table A8. ES forecasting results with the QbSD approach when θ=0.5\theta=0.5 and T=1250T=1250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.272 | 0.223 | 0.190 |  | 0.360 | 0.284 | 0.237 |  | 0.377 | 0.266 | 0.206 |  | 0.539 | 0.357 | 0.268 |
| p=0.10p=0.10 |  | 0.270 | 0.222 | 0.188 |  | 0.357 | 0.283 | 0.236 |  | 0.368 | 0.257 | 0.198 |  | 0.534 | 0.354 | 0.265 |
| p=0.15p=0.15 |  | 0.273 | 0.225 | 0.191 |  | 0.358 | 0.285 | 0.237 |  | 0.368 | 0.259 | 0.200 |  | 0.530 | 0.353 | 0.267 |
| p=0.20p=0.20 |  | 0.276 | 0.227 | 0.193 |  | 0.362 | 0.288 | 0.240 |  | 0.368 | 0.259 | 0.201 |  | 0.530 | 0.353 | 0.267 |
| p=0.25p=0.25 |  | 0.282 | 0.231 | 0.196 |  | 0.368 | 0.292 | 0.244 |  | 0.374 | 0.265 | 0.205 |  | 0.531 | 0.355 | 0.268 |
| Mean over pp |  | 0.270 | 0.222 | 0.189 |  | 0.355 | 0.282 | 0.235 |  | 0.365 | 0.256 | 0.198 |  | 0.529 | 0.349 | 0.262 |
| Median over pp |  | 0.271 | 0.223 | 0.190 |  | 0.355 | 0.282 | 0.234 |  | 0.367 | 0.257 | 0.199 |  | 0.527 | 0.349 | 0.262 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.173 | 0.129 | 0.107 |  | 0.246 | 0.180 | 0.144 |  | 0.299 | 0.190 | 0.142 |  | 0.455 | 0.281 | 0.203 |
| p=0.10p=0.10 |  | 0.164 | 0.124 | 0.104 |  | 0.231 | 0.171 | 0.138 |  | 0.282 | 0.179 | 0.134 |  | 0.432 | 0.265 | 0.193 |
| p=0.15p=0.15 |  | 0.163 | 0.125 | 0.104 |  | 0.232 | 0.173 | 0.141 |  | 0.277 | 0.176 | 0.132 |  | 0.431 | 0.267 | 0.196 |
| p=0.20p=0.20 |  | 0.170 | 0.131 | 0.108 |  | 0.236 | 0.177 | 0.145 |  | 0.281 | 0.182 | 0.137 |  | 0.427 | 0.265 | 0.196 |
| p=0.25p=0.25 |  | 0.175 | 0.136 | 0.113 |  | 0.239 | 0.181 | 0.149 |  | 0.277 | 0.179 | 0.136 |  | 0.420 | 0.262 | 0.193 |
| Mean over pp |  | 0.158 | 0.118 | 0.098 |  | 0.224 | 0.164 | 0.133 |  | 0.272 | 0.170 | 0.126 |  | 0.420 | 0.256 | 0.186 |
| Median over pp |  | 0.159 | 0.119 | 0.099 |  | 0.225 | 0.166 | 0.134 |  | 0.273 | 0.172 | 0.128 |  | 0.421 | 0.258 | 0.188 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.361 | 0.297 | 0.253 |  | 0.481 | 0.382 | 0.319 |  | 0.507 | 0.362 | 0.282 |  | 0.732 | 0.490 | 0.370 |
| p=0.10p=0.10 |  | 0.360 | 0.297 | 0.253 |  | 0.482 | 0.384 | 0.320 |  | 0.487 | 0.348 | 0.270 |  | 0.728 | 0.490 | 0.368 |
| p=0.15p=0.15 |  | 0.367 | 0.304 | 0.259 |  | 0.488 | 0.390 | 0.326 |  | 0.494 | 0.354 | 0.276 |  | 0.718 | 0.488 | 0.370 |
| p=0.20p=0.20 |  | 0.369 | 0.305 | 0.260 |  | 0.491 | 0.392 | 0.328 |  | 0.497 | 0.356 | 0.278 |  | 0.717 | 0.490 | 0.372 |
| p=0.25p=0.25 |  | 0.372 | 0.308 | 0.263 |  | 0.493 | 0.395 | 0.331 |  | 0.499 | 0.359 | 0.280 |  | 0.720 | 0.495 | 0.376 |
| Mean over pp |  | 0.358 | 0.296 | 0.252 |  | 0.477 | 0.380 | 0.318 |  | 0.487 | 0.347 | 0.270 |  | 0.705 | 0.475 | 0.359 |
| Median over pp |  | 0.361 | 0.298 | 0.254 |  | 0.478 | 0.381 | 0.318 |  | 0.488 | 0.348 | 0.271 |  | 0.702 | 0.474 | 0.358 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.230 | 0.177 | 0.149 |  | 0.327 | 0.246 | 0.201 |  | 0.389 | 0.256 | 0.197 |  | 0.612 | 0.386 | 0.286 |
| p=0.10p=0.10 |  | 0.215 | 0.166 | 0.139 |  | 0.309 | 0.231 | 0.188 |  | 0.362 | 0.236 | 0.180 |  | 0.566 | 0.356 | 0.263 |
| p=0.15p=0.15 |  | 0.217 | 0.169 | 0.142 |  | 0.312 | 0.237 | 0.194 |  | 0.356 | 0.233 | 0.178 |  | 0.570 | 0.368 | 0.276 |
| p=0.20p=0.20 |  | 0.226 | 0.177 | 0.149 |  | 0.319 | 0.243 | 0.200 |  | 0.367 | 0.243 | 0.187 |  | 0.565 | 0.366 | 0.275 |
| p=0.25p=0.25 |  | 0.232 | 0.185 | 0.155 |  | 0.325 | 0.251 | 0.209 |  | 0.359 | 0.239 | 0.184 |  | 0.565 | 0.370 | 0.279 |
| Mean over pp |  | 0.206 | 0.158 | 0.132 |  | 0.298 | 0.223 | 0.182 |  | 0.348 | 0.224 | 0.170 |  | 0.548 | 0.344 | 0.254 |
| Median over pp |  | 0.208 | 0.160 | 0.134 |  | 0.299 | 0.224 | 0.183 |  | 0.350 | 0.226 | 0.172 |  | 0.552 | 0.351 | 0.261 |



Table A9. VaR forecasting results with the QbSD approach when θ=0\theta=0 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.078 | 0.059 | 0.046 |  | 0.100 | 0.073 | 0.054 |  | 0.116 | 0.075 | 0.054 |  | 0.150 | 0.095 | 0.063 |
| p=0.10p=0.10 |  | 0.078 | 0.058 | 0.045 |  | 0.098 | 0.072 | 0.052 |  | 0.112 | 0.072 | 0.050 |  | 0.147 | 0.090 | 0.059 |
| p=0.15p=0.15 |  | 0.080 | 0.059 | 0.045 |  | 0.100 | 0.073 | 0.053 |  | 0.115 | 0.071 | 0.050 |  | 0.149 | 0.092 | 0.060 |
| p=0.20p=0.20 |  | 0.082 | 0.061 | 0.048 |  | 0.104 | 0.074 | 0.056 |  | 0.115 | 0.073 | 0.052 |  | 0.151 | 0.092 | 0.061 |
| p=0.25p=0.25 |  | 0.086 | 0.067 | 0.052 |  | 0.107 | 0.079 | 0.060 |  | 0.120 | 0.078 | 0.056 |  | 0.154 | 0.095 | 0.063 |
| Mean over pp |  | 0.076 | 0.056 | 0.043 |  | 0.097 | 0.070 | 0.052 |  | 0.111 | 0.070 | 0.049 |  | 0.145 | 0.089 | 0.058 |
| Median over pp |  | 0.077 | 0.057 | 0.044 |  | 0.098 | 0.071 | 0.052 |  | 0.112 | 0.071 | 0.050 |  | 0.146 | 0.090 | 0.059 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.086 | 0.066 | 0.052 |  | 0.104 | 0.078 | 0.058 |  | 0.122 | 0.081 | 0.059 |  | 0.155 | 0.101 | 0.067 |
| p=0.10p=0.10 |  | 0.085 | 0.065 | 0.051 |  | 0.103 | 0.077 | 0.057 |  | 0.117 | 0.078 | 0.055 |  | 0.149 | 0.094 | 0.062 |
| p=0.15p=0.15 |  | 0.087 | 0.067 | 0.053 |  | 0.105 | 0.078 | 0.058 |  | 0.119 | 0.078 | 0.057 |  | 0.152 | 0.096 | 0.064 |
| p=0.20p=0.20 |  | 0.092 | 0.070 | 0.056 |  | 0.110 | 0.081 | 0.062 |  | 0.124 | 0.082 | 0.060 |  | 0.155 | 0.097 | 0.065 |
| p=0.25p=0.25 |  | 0.097 | 0.076 | 0.059 |  | 0.115 | 0.089 | 0.067 |  | 0.129 | 0.086 | 0.062 |  | 0.158 | 0.102 | 0.069 |
| Mean over pp |  | 0.082 | 0.063 | 0.049 |  | 0.101 | 0.076 | 0.056 |  | 0.115 | 0.075 | 0.054 |  | 0.146 | 0.093 | 0.061 |
| Median over pp |  | 0.083 | 0.063 | 0.050 |  | 0.101 | 0.076 | 0.056 |  | 0.116 | 0.076 | 0.054 |  | 0.148 | 0.094 | 0.061 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.103 | 0.077 | 0.060 |  | 0.130 | 0.094 | 0.070 |  | 0.161 | 0.105 | 0.075 |  | 0.201 | 0.126 | 0.085 |
| p=0.10p=0.10 |  | 0.102 | 0.075 | 0.058 |  | 0.127 | 0.090 | 0.067 |  | 0.154 | 0.100 | 0.071 |  | 0.194 | 0.118 | 0.078 |
| p=0.15p=0.15 |  | 0.105 | 0.078 | 0.060 |  | 0.130 | 0.094 | 0.070 |  | 0.158 | 0.101 | 0.072 |  | 0.200 | 0.122 | 0.081 |
| p=0.20p=0.20 |  | 0.108 | 0.081 | 0.063 |  | 0.135 | 0.096 | 0.072 |  | 0.161 | 0.103 | 0.075 |  | 0.201 | 0.121 | 0.081 |
| p=0.25p=0.25 |  | 0.114 | 0.087 | 0.069 |  | 0.138 | 0.103 | 0.078 |  | 0.163 | 0.107 | 0.077 |  | 0.206 | 0.128 | 0.086 |
| Mean over pp |  | 0.099 | 0.074 | 0.057 |  | 0.126 | 0.090 | 0.067 |  | 0.152 | 0.097 | 0.069 |  | 0.194 | 0.118 | 0.078 |
| Median over pp |  | 0.101 | 0.074 | 0.057 |  | 0.127 | 0.091 | 0.068 |  | 0.154 | 0.099 | 0.070 |  | 0.195 | 0.119 | 0.078 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.113 | 0.086 | 0.068 |  | 0.137 | 0.101 | 0.076 |  | 0.167 | 0.111 | 0.082 |  | 0.211 | 0.135 | 0.091 |
| p=0.10p=0.10 |  | 0.112 | 0.085 | 0.068 |  | 0.134 | 0.098 | 0.074 |  | 0.164 | 0.108 | 0.079 |  | 0.201 | 0.124 | 0.083 |
| p=0.15p=0.15 |  | 0.116 | 0.089 | 0.072 |  | 0.138 | 0.102 | 0.077 |  | 0.165 | 0.109 | 0.081 |  | 0.204 | 0.127 | 0.086 |
| p=0.20p=0.20 |  | 0.124 | 0.096 | 0.076 |  | 0.145 | 0.106 | 0.081 |  | 0.176 | 0.119 | 0.087 |  | 0.207 | 0.127 | 0.086 |
| p=0.25p=0.25 |  | 0.129 | 0.100 | 0.080 |  | 0.152 | 0.115 | 0.088 |  | 0.178 | 0.119 | 0.087 |  | 0.213 | 0.135 | 0.091 |
| Mean over pp |  | 0.108 | 0.083 | 0.065 |  | 0.131 | 0.096 | 0.073 |  | 0.160 | 0.105 | 0.076 |  | 0.197 | 0.122 | 0.082 |
| Median over pp |  | 0.110 | 0.084 | 0.067 |  | 0.132 | 0.096 | 0.072 |  | 0.162 | 0.106 | 0.077 |  | 0.199 | 0.123 | 0.082 |



Table A10. ES forecasting results with the QbSD approach when θ=0\theta=0 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.106 | 0.080 | 0.066 |  | 0.140 | 0.104 | 0.084 |  | 0.203 | 0.131 | 0.097 |  | 0.277 | 0.173 | 0.128 |
| p=0.10p=0.10 |  | 0.104 | 0.078 | 0.064 |  | 0.137 | 0.101 | 0.081 |  | 0.197 | 0.126 | 0.092 |  | 0.271 | 0.167 | 0.122 |
| p=0.15p=0.15 |  | 0.104 | 0.079 | 0.065 |  | 0.138 | 0.102 | 0.082 |  | 0.196 | 0.125 | 0.092 |  | 0.272 | 0.169 | 0.124 |
| p=0.20p=0.20 |  | 0.106 | 0.081 | 0.066 |  | 0.140 | 0.105 | 0.084 |  | 0.198 | 0.127 | 0.093 |  | 0.273 | 0.171 | 0.125 |
| p=0.25p=0.25 |  | 0.112 | 0.087 | 0.071 |  | 0.145 | 0.109 | 0.088 |  | 0.204 | 0.131 | 0.096 |  | 0.277 | 0.173 | 0.127 |
| Mean over pp |  | 0.102 | 0.077 | 0.062 |  | 0.136 | 0.101 | 0.081 |  | 0.195 | 0.124 | 0.091 |  | 0.271 | 0.168 | 0.123 |
| Median over pp |  | 0.102 | 0.078 | 0.063 |  | 0.137 | 0.101 | 0.082 |  | 0.196 | 0.125 | 0.092 |  | 0.271 | 0.169 | 0.124 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.113 | 0.088 | 0.072 |  | 0.143 | 0.108 | 0.087 |  | 0.207 | 0.138 | 0.103 |  | 0.284 | 0.180 | 0.132 |
| p=0.10p=0.10 |  | 0.111 | 0.086 | 0.071 |  | 0.140 | 0.105 | 0.084 |  | 0.202 | 0.133 | 0.098 |  | 0.272 | 0.170 | 0.123 |
| p=0.15p=0.15 |  | 0.112 | 0.088 | 0.072 |  | 0.142 | 0.107 | 0.086 |  | 0.200 | 0.132 | 0.098 |  | 0.272 | 0.170 | 0.125 |
| p=0.20p=0.20 |  | 0.115 | 0.091 | 0.075 |  | 0.145 | 0.111 | 0.090 |  | 0.201 | 0.135 | 0.101 |  | 0.274 | 0.172 | 0.126 |
| p=0.25p=0.25 |  | 0.122 | 0.097 | 0.080 |  | 0.152 | 0.117 | 0.095 |  | 0.208 | 0.140 | 0.104 |  | 0.279 | 0.177 | 0.129 |
| Mean over pp |  | 0.107 | 0.083 | 0.068 |  | 0.137 | 0.103 | 0.083 |  | 0.197 | 0.130 | 0.096 |  | 0.271 | 0.168 | 0.123 |
| Median over pp |  | 0.108 | 0.084 | 0.069 |  | 0.138 | 0.104 | 0.084 |  | 0.198 | 0.131 | 0.097 |  | 0.272 | 0.169 | 0.124 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.135 | 0.105 | 0.086 |  | 0.177 | 0.132 | 0.106 |  | 0.263 | 0.177 | 0.132 |  | 0.349 | 0.224 | 0.165 |
| p=0.10p=0.10 |  | 0.132 | 0.102 | 0.083 |  | 0.173 | 0.128 | 0.102 |  | 0.254 | 0.168 | 0.125 |  | 0.340 | 0.215 | 0.157 |
| p=0.15p=0.15 |  | 0.135 | 0.104 | 0.086 |  | 0.176 | 0.131 | 0.106 |  | 0.257 | 0.170 | 0.127 |  | 0.344 | 0.220 | 0.162 |
| p=0.20p=0.20 |  | 0.138 | 0.108 | 0.088 |  | 0.181 | 0.135 | 0.109 |  | 0.261 | 0.174 | 0.131 |  | 0.344 | 0.219 | 0.161 |
| p=0.25p=0.25 |  | 0.144 | 0.114 | 0.094 |  | 0.186 | 0.140 | 0.114 |  | 0.265 | 0.176 | 0.132 |  | 0.351 | 0.225 | 0.166 |
| Mean over pp |  | 0.130 | 0.100 | 0.081 |  | 0.173 | 0.128 | 0.103 |  | 0.254 | 0.167 | 0.124 |  | 0.340 | 0.215 | 0.158 |
| Median over pp |  | 0.131 | 0.101 | 0.082 |  | 0.174 | 0.129 | 0.104 |  | 0.255 | 0.169 | 0.126 |  | 0.340 | 0.216 | 0.159 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.146 | 0.114 | 0.095 |  | 0.182 | 0.138 | 0.111 |  | 0.269 | 0.184 | 0.139 |  | 0.359 | 0.232 | 0.172 |
| p=0.10p=0.10 |  | 0.144 | 0.112 | 0.093 |  | 0.179 | 0.135 | 0.108 |  | 0.265 | 0.180 | 0.135 |  | 0.346 | 0.220 | 0.161 |
| p=0.15p=0.15 |  | 0.147 | 0.116 | 0.097 |  | 0.182 | 0.139 | 0.112 |  | 0.265 | 0.180 | 0.136 |  | 0.346 | 0.222 | 0.164 |
| p=0.20p=0.20 |  | 0.154 | 0.123 | 0.103 |  | 0.188 | 0.145 | 0.116 |  | 0.275 | 0.191 | 0.145 |  | 0.349 | 0.224 | 0.164 |
| p=0.25p=0.25 |  | 0.159 | 0.128 | 0.107 |  | 0.196 | 0.153 | 0.124 |  | 0.277 | 0.193 | 0.146 |  | 0.355 | 0.230 | 0.169 |
| Mean over pp |  | 0.139 | 0.110 | 0.091 |  | 0.176 | 0.134 | 0.107 |  | 0.261 | 0.177 | 0.133 |  | 0.342 | 0.218 | 0.159 |
| Median over pp |  | 0.142 | 0.112 | 0.093 |  | 0.177 | 0.134 | 0.107 |  | 0.262 | 0.178 | 0.134 |  | 0.343 | 0.219 | 0.160 |



Table A11. VaR forecasting results with the QbSD approach when θ=0.5\theta=0.5 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.212 | 0.174 | 0.141 |  | 0.262 | 0.206 | 0.162 |  | 0.229 | 0.171 | 0.130 |  | 0.293 | 0.203 | 0.147 |
| p=0.10p=0.10 |  | 0.214 | 0.174 | 0.141 |  | 0.262 | 0.205 | 0.162 |  | 0.230 | 0.169 | 0.129 |  | 0.293 | 0.202 | 0.147 |
| p=0.15p=0.15 |  | 0.217 | 0.176 | 0.144 |  | 0.266 | 0.208 | 0.164 |  | 0.233 | 0.172 | 0.132 |  | 0.297 | 0.206 | 0.150 |
| p=0.20p=0.20 |  | 0.217 | 0.178 | 0.145 |  | 0.265 | 0.209 | 0.165 |  | 0.235 | 0.173 | 0.133 |  | 0.298 | 0.205 | 0.150 |
| p=0.25p=0.25 |  | 0.222 | 0.180 | 0.147 |  | 0.270 | 0.212 | 0.169 |  | 0.239 | 0.176 | 0.135 |  | 0.303 | 0.209 | 0.153 |
| Mean over pp |  | 0.214 | 0.174 | 0.142 |  | 0.263 | 0.206 | 0.163 |  | 0.231 | 0.170 | 0.130 |  | 0.293 | 0.202 | 0.147 |
| Median over pp |  | 0.216 | 0.175 | 0.143 |  | 0.264 | 0.206 | 0.164 |  | 0.232 | 0.172 | 0.131 |  | 0.294 | 0.203 | 0.148 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.099 | 0.075 | 0.061 |  | 0.138 | 0.103 | 0.079 |  | 0.135 | 0.092 | 0.068 |  | 0.200 | 0.132 | 0.092 |
| p=0.10p=0.10 |  | 0.099 | 0.076 | 0.059 |  | 0.136 | 0.102 | 0.077 |  | 0.132 | 0.090 | 0.066 |  | 0.191 | 0.125 | 0.086 |
| p=0.15p=0.15 |  | 0.101 | 0.080 | 0.063 |  | 0.138 | 0.105 | 0.081 |  | 0.133 | 0.090 | 0.066 |  | 0.193 | 0.128 | 0.088 |
| p=0.20p=0.20 |  | 0.106 | 0.083 | 0.067 |  | 0.144 | 0.110 | 0.084 |  | 0.139 | 0.095 | 0.070 |  | 0.201 | 0.133 | 0.091 |
| p=0.25p=0.25 |  | 0.114 | 0.090 | 0.072 |  | 0.153 | 0.118 | 0.091 |  | 0.145 | 0.099 | 0.072 |  | 0.206 | 0.135 | 0.095 |
| Mean over pp |  | 0.096 | 0.075 | 0.059 |  | 0.133 | 0.102 | 0.078 |  | 0.129 | 0.087 | 0.063 |  | 0.188 | 0.124 | 0.085 |
| Median over pp |  | 0.097 | 0.076 | 0.060 |  | 0.136 | 0.103 | 0.079 |  | 0.130 | 0.088 | 0.064 |  | 0.190 | 0.126 | 0.087 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.288 | 0.234 | 0.191 |  | 0.365 | 0.285 | 0.223 |  | 0.335 | 0.244 | 0.186 |  | 0.436 | 0.300 | 0.216 |
| p=0.10p=0.10 |  | 0.287 | 0.232 | 0.189 |  | 0.362 | 0.282 | 0.222 |  | 0.326 | 0.238 | 0.182 |  | 0.431 | 0.296 | 0.213 |
| p=0.15p=0.15 |  | 0.292 | 0.237 | 0.194 |  | 0.367 | 0.287 | 0.226 |  | 0.330 | 0.242 | 0.186 |  | 0.436 | 0.299 | 0.216 |
| p=0.20p=0.20 |  | 0.294 | 0.238 | 0.195 |  | 0.366 | 0.287 | 0.226 |  | 0.332 | 0.242 | 0.186 |  | 0.437 | 0.298 | 0.216 |
| p=0.25p=0.25 |  | 0.303 | 0.245 | 0.201 |  | 0.375 | 0.292 | 0.231 |  | 0.343 | 0.252 | 0.193 |  | 0.449 | 0.306 | 0.220 |
| Mean over pp |  | 0.289 | 0.234 | 0.192 |  | 0.363 | 0.283 | 0.223 |  | 0.328 | 0.240 | 0.184 |  | 0.431 | 0.295 | 0.212 |
| Median over pp |  | 0.290 | 0.235 | 0.192 |  | 0.365 | 0.284 | 0.224 |  | 0.329 | 0.241 | 0.184 |  | 0.432 | 0.296 | 0.213 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.134 | 0.101 | 0.082 |  | 0.191 | 0.140 | 0.109 |  | 0.194 | 0.129 | 0.096 |  | 0.300 | 0.199 | 0.140 |
| p=0.10p=0.10 |  | 0.133 | 0.101 | 0.080 |  | 0.188 | 0.140 | 0.107 |  | 0.188 | 0.127 | 0.092 |  | 0.284 | 0.184 | 0.126 |
| p=0.15p=0.15 |  | 0.139 | 0.107 | 0.086 |  | 0.196 | 0.147 | 0.113 |  | 0.189 | 0.126 | 0.093 |  | 0.301 | 0.195 | 0.132 |
| p=0.20p=0.20 |  | 0.146 | 0.114 | 0.091 |  | 0.206 | 0.153 | 0.117 |  | 0.201 | 0.135 | 0.099 |  | 0.312 | 0.199 | 0.136 |
| p=0.25p=0.25 |  | 0.161 | 0.127 | 0.102 |  | 0.217 | 0.166 | 0.128 |  | 0.215 | 0.146 | 0.108 |  | 0.321 | 0.207 | 0.146 |
| Mean over pp |  | 0.131 | 0.101 | 0.080 |  | 0.188 | 0.140 | 0.107 |  | 0.186 | 0.123 | 0.090 |  | 0.288 | 0.185 | 0.127 |
| Median over pp |  | 0.133 | 0.102 | 0.082 |  | 0.191 | 0.142 | 0.109 |  | 0.187 | 0.124 | 0.091 |  | 0.298 | 0.192 | 0.132 |



Table A12. ES forecasting results with the QbSD approach when θ=0.5\theta=0.5 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.250 | 0.212 | 0.183 |  | 0.320 | 0.263 | 0.223 |  | 0.326 | 0.242 | 0.193 |  | 0.449 | 0.317 | 0.246 |
| p=0.10p=0.10 |  | 0.251 | 0.212 | 0.182 |  | 0.319 | 0.262 | 0.222 |  | 0.323 | 0.241 | 0.191 |  | 0.444 | 0.314 | 0.243 |
| p=0.15p=0.15 |  | 0.254 | 0.215 | 0.185 |  | 0.322 | 0.265 | 0.224 |  | 0.327 | 0.244 | 0.194 |  | 0.446 | 0.317 | 0.245 |
| p=0.20p=0.20 |  | 0.256 | 0.216 | 0.186 |  | 0.324 | 0.266 | 0.224 |  | 0.326 | 0.244 | 0.194 |  | 0.447 | 0.317 | 0.245 |
| p=0.25p=0.25 |  | 0.260 | 0.219 | 0.188 |  | 0.330 | 0.271 | 0.229 |  | 0.331 | 0.247 | 0.197 |  | 0.456 | 0.323 | 0.249 |
| Mean over pp |  | 0.252 | 0.212 | 0.183 |  | 0.321 | 0.263 | 0.223 |  | 0.323 | 0.242 | 0.192 |  | 0.445 | 0.315 | 0.243 |
| Median over pp |  | 0.252 | 0.213 | 0.184 |  | 0.322 | 0.264 | 0.224 |  | 0.324 | 0.243 | 0.193 |  | 0.446 | 0.316 | 0.244 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.128 | 0.099 | 0.082 |  | 0.182 | 0.140 | 0.113 |  | 0.226 | 0.151 | 0.112 |  | 0.348 | 0.226 | 0.166 |
| p=0.10p=0.10 |  | 0.125 | 0.097 | 0.081 |  | 0.179 | 0.137 | 0.113 |  | 0.216 | 0.145 | 0.107 |  | 0.328 | 0.212 | 0.157 |
| p=0.15p=0.15 |  | 0.125 | 0.099 | 0.083 |  | 0.179 | 0.139 | 0.115 |  | 0.213 | 0.143 | 0.107 |  | 0.328 | 0.213 | 0.159 |
| p=0.20p=0.20 |  | 0.133 | 0.105 | 0.088 |  | 0.185 | 0.143 | 0.118 |  | 0.221 | 0.150 | 0.113 |  | 0.334 | 0.218 | 0.162 |
| p=0.25p=0.25 |  | 0.142 | 0.113 | 0.095 |  | 0.196 | 0.154 | 0.126 |  | 0.229 | 0.156 | 0.116 |  | 0.340 | 0.224 | 0.167 |
| Mean over pp |  | 0.123 | 0.095 | 0.080 |  | 0.177 | 0.135 | 0.112 |  | 0.214 | 0.143 | 0.105 |  | 0.327 | 0.212 | 0.157 |
| Median over pp |  | 0.124 | 0.096 | 0.081 |  | 0.177 | 0.137 | 0.113 |  | 0.213 | 0.143 | 0.106 |  | 0.330 | 0.214 | 0.159 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD-gSAV model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.338 | 0.287 | 0.248 |  | 0.441 | 0.365 | 0.308 |  | 0.457 | 0.346 | 0.276 |  | 0.640 | 0.462 | 0.360 |
| p=0.10p=0.10 |  | 0.336 | 0.285 | 0.246 |  | 0.438 | 0.362 | 0.304 |  | 0.450 | 0.340 | 0.271 |  | 0.630 | 0.454 | 0.354 |
| p=0.15p=0.15 |  | 0.342 | 0.290 | 0.251 |  | 0.443 | 0.367 | 0.309 |  | 0.456 | 0.345 | 0.276 |  | 0.632 | 0.458 | 0.357 |
| p=0.20p=0.20 |  | 0.344 | 0.292 | 0.253 |  | 0.443 | 0.367 | 0.309 |  | 0.456 | 0.345 | 0.276 |  | 0.631 | 0.458 | 0.357 |
| p=0.25p=0.25 |  | 0.354 | 0.301 | 0.260 |  | 0.453 | 0.376 | 0.316 |  | 0.470 | 0.356 | 0.286 |  | 0.645 | 0.468 | 0.365 |
| Mean over pp |  | 0.339 | 0.288 | 0.249 |  | 0.439 | 0.364 | 0.306 |  | 0.453 | 0.342 | 0.274 |  | 0.627 | 0.454 | 0.353 |
| Median over pp |  | 0.339 | 0.288 | 0.249 |  | 0.441 | 0.365 | 0.307 |  | 0.455 | 0.344 | 0.275 |  | 0.629 | 0.455 | 0.355 |
| QbSD-gAS model |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Individual values of pp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p=0.05p=0.05 |  | 0.170 | 0.133 | 0.111 |  | 0.246 | 0.190 | 0.156 |  | 0.304 | 0.209 | 0.156 |  | 0.485 | 0.326 | 0.244 |
| p=0.10p=0.10 |  | 0.167 | 0.130 | 0.109 |  | 0.242 | 0.188 | 0.155 |  | 0.293 | 0.201 | 0.150 |  | 0.450 | 0.301 | 0.225 |
| p=0.15p=0.15 |  | 0.172 | 0.136 | 0.115 |  | 0.246 | 0.193 | 0.160 |  | 0.288 | 0.199 | 0.150 |  | 0.457 | 0.312 | 0.235 |
| p=0.20p=0.20 |  | 0.181 | 0.145 | 0.122 |  | 0.257 | 0.202 | 0.166 |  | 0.301 | 0.211 | 0.160 |  | 0.471 | 0.322 | 0.243 |
| p=0.25p=0.25 |  | 0.195 | 0.159 | 0.136 |  | 0.269 | 0.215 | 0.178 |  | 0.318 | 0.225 | 0.171 |  | 0.481 | 0.332 | 0.253 |
| Mean over pp |  | 0.165 | 0.130 | 0.110 |  | 0.240 | 0.187 | 0.154 |  | 0.290 | 0.199 | 0.149 |  | 0.452 | 0.304 | 0.228 |
| Median over pp |  | 0.167 | 0.131 | 0.111 |  | 0.242 | 0.189 | 0.156 |  | 0.290 | 0.199 | 0.149 |  | 0.461 | 0.313 | 0.236 |

## Section B

Tables B1–B8 report one-step-ahead VaR/ES forecast errors (MAE, RMSE) for the proposed QbSD models (gSAV, gAS) and benchmarks (skew-tt GARCH/GJR/EGARCH, AL-based joint VaR-ES, and GAS) across data-generating designs varying by T∈{250,2500}T\in\{250,2500\}, v∈{5,20}v\in\{5,20\}, λ∈{0,−0.5}\lambda\in\{0,-0.5\}, θ∈{0,0.5}\theta\in\{0,0.5\}, and α∈{0.01,0.025,0.05}\alpha\in\{0.01,0.025,0.05\}. Minima are bolded.

For T=250T=250 without leverage (Tables B1–B2), conventional GARCH-type models dominate. With symmetric innovations, Normal/Student-tt GARCH/GJR achieve most minima; under left-skew, their skew-tt counterparts lead. QbSD models are competitive but rarely best, while AL-based estimators and GAS trail.

Introducing leverage at T=250T=250 (Tables B3–B4) shifts the lead within the GARCH family: EGARCH frequently attains the lowest errors in symmetric cases, and skew-tt GARCH/GJR often prevail under skewed or heavy-tailed DGPs. QbSD-gAS improves relative to QbSD-gSAV but seldom displaces the top GARCH variants at this sample size.

With larger samples and no leverage (Tables B5–B6, T=2500T=2500, θ=0\theta=0), GARCH/GJR remain the primary winners. Student-tt specifications account for many minima under symmetry and heavy tails, whereas skew-tt versions excel when λ=−0.5\lambda=-0.5. QbSD narrows the gap but generally does not surpass the best GARCH-type models here.

With larger samples under leverage (Tables B7–B8, T=2500T=2500, θ=0.5\theta=0.5), QbSD-gAS delivers many of the lowest ES MAE/RMSE values across α\alpha and (v,λ)(v,\lambda) settings, outperforming AL and GAS and often surpassing standard GARCH models. Two caveats remain: (i) under symmetric innovations, EGARCH can match or exceed QbSD-gAS for ES RMSE at some α\alpha (e.g., v=20v=20, λ=0\lambda=0 at 2.5%2.5\% and 5%5\%); and (ii) for VaR the best model can shift with tail level—EGARCH under symmetry and skew-tt GJR-GARCH/GARCH under skewed, heavy-tailed designs—while QbSD-gAS remains the most robust ES performer under leverage.

Overall, while GARCH-type models (especially skew-tt and EGARCH) are very strong at T=250T=250 and in several T=2500T=2500 designs without leverage, QbSD-gAS becomes particularly effective for ES once leverage is present and the sample is large, delivering broad gains except in the most extreme skew/heavy-tail scenario. AL-based estimators and GAS underperform across configurations.

Table B1. VaR forecasting results when θ=0\theta=0 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.218 | 0.165 | 0.131 |  | 0.281 | 0.198 | 0.154 |  | 0.300 | 0.193 | 0.138 |  | 0.403 | 0.239 | 0.167 |
| QbSD-gAS |  | 0.241 | 0.182 | 0.147 |  | 0.304 | 0.216 | 0.169 |  | 0.318 | 0.208 | 0.153 |  | 0.431 | 0.259 | 0.180 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.314 | 0.225 | 0.174 |  | 0.435 | 0.307 | 0.227 |  | 0.473 | 0.287 | 0.197 |  | 0.661 | 0.414 | 0.267 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.313 | 0.228 | 0.178 |  | 0.437 | 0.308 | 0.235 |  | 0.462 | 0.287 | 0.201 |  | 0.645 | 0.412 | 0.266 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.378 | 0.267 | 0.200 |  | 0.503 | 0.355 | 0.260 |  | 0.537 | 0.338 | 0.233 |  | 0.770 | 0.479 | 0.318 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.378 | 0.271 | 0.202 |  | 0.499 | 0.362 | 0.268 |  | 0.532 | 0.339 | 0.232 |  | 0.747 | 0.471 | 0.316 |
| GAS |  | 0.351 | 0.264 | 0.202 |  | 0.448 | 0.315 | 0.232 |  | 0.717 | 0.333 | 0.231 |  | 0.595 | 0.377 | 0.284 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.146 | 0.114 | 0.094 |  | 0.479 | 0.311 | 0.196 |  | 0.284 | 0.158 | 0.133 |  | 0.776 | 0.390 | 0.199 |
| Student-tt |  | 0.151 | 0.115 | 0.093 |  | 0.415 | 0.298 | 0.205 |  | 0.227 | 0.145 | 0.104 |  | 0.618 | 0.378 | 0.225 |
| Skew-tt |  | 0.165 | 0.124 | 0.097 |  | 0.201 | 0.138 | 0.101 |  | 0.245 | 0.153 | 0.107 |  | 0.329 | 0.181 | 0.111 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.147 | 0.115 | 0.095 |  | 0.479 | 0.311 | 0.196 |  | 0.286 | 0.160 | 0.136 |  | 0.776 | 0.390 | 0.197 |
| Student-tt |  | 0.149 | 0.114 | 0.092 |  | 0.414 | 0.297 | 0.206 |  | 0.227 | 0.145 | 0.104 |  | 0.618 | 0.377 | 0.225 |
| Skew-tt |  | 0.165 | 0.124 | 0.098 |  | 0.203 | 0.140 | 0.102 |  | 0.247 | 0.156 | 0.110 |  | 0.338 | 0.188 | 0.116 |
| EGARCH |  | 0.188 | 0.149 | 0.123 |  | 0.515 | 0.342 | 0.224 |  | 0.343 | 0.209 | 0.167 |  | 0.835 | 0.447 | 0.246 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.281 | 0.216 | 0.173 |  | 0.361 | 0.259 | 0.206 |  | 0.400 | 0.265 | 0.196 |  | 0.568 | 0.343 | 0.245 |
| QbSD-gAS |  | 0.308 | 0.235 | 0.192 |  | 0.392 | 0.284 | 0.225 |  | 0.435 | 0.283 | 0.215 |  | 0.655 | 0.384 | 0.281 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.416 | 0.301 | 0.237 |  | 0.600 | 0.419 | 0.318 |  | 0.694 | 0.407 | 0.292 |  | 1.039 | 0.684 | 0.433 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.407 | 0.306 | 0.245 |  | 0.597 | 0.424 | 0.332 |  | 0.649 | 0.407 | 0.296 |  | 0.952 | 0.616 | 0.413 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.492 | 0.363 | 0.267 |  | 0.661 | 0.508 | 0.349 |  | 0.733 | 0.462 | 0.330 |  | 1.157 | 0.720 | 0.725 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.493 | 0.368 | 0.272 |  | 0.650 | 0.521 | 0.354 |  | 0.727 | 0.485 | 0.350 |  | 1.031 | 0.690 | 0.472 |
| GAS |  | 0.714 | 0.410 | 0.282 |  | 0.815 | 0.597 | 0.461 |  | 8.371 | 0.750 | 0.488 |  | 1.010 | 0.708 | 0.773 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.188 | 0.152 | 0.127 |  | 0.515 | 0.345 | 0.227 |  | 0.341 | 0.225 | 0.203 |  | 0.826 | 0.444 | 0.261 |
| Student-tt |  | 0.203 | 0.156 | 0.126 |  | 0.460 | 0.331 | 0.233 |  | 0.321 | 0.208 | 0.150 |  | 0.676 | 0.414 | 0.257 |
| Skew-tt |  | 0.221 | 0.167 | 0.131 |  | 0.295 | 0.206 | 0.147 |  | 0.346 | 0.218 | 0.155 |  | 0.485 | 0.278 | 0.177 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.191 | 0.154 | 0.129 |  | 0.515 | 0.345 | 0.227 |  | 0.346 | 0.232 | 0.211 |  | 0.823 | 0.441 | 0.258 |
| Student-tt |  | 0.201 | 0.155 | 0.125 |  | 0.460 | 0.331 | 0.235 |  | 0.320 | 0.207 | 0.150 |  | 0.676 | 0.414 | 0.257 |
| Skew-tt |  | 0.221 | 0.167 | 0.132 |  | 0.285 | 0.199 | 0.145 |  | 0.345 | 0.219 | 0.157 |  | 0.497 | 0.288 | 0.184 |
| EGARCH |  | 0.253 | 0.204 | 0.168 |  | 0.570 | 0.393 | 0.270 |  | 0.432 | 0.296 | 0.249 |  | 0.909 | 0.523 | 0.330 |



Table B2. ES forecasting results when θ=0\theta=0 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.300 | 0.219 | 0.174 |  | 0.407 | 0.283 | 0.219 |  | 0.522 | 0.322 | 0.229 |  | 0.745 | 0.437 | 0.298 |
| QbSD-gAS |  | 0.322 | 0.241 | 0.195 |  | 0.432 | 0.306 | 0.238 |  | 0.545 | 0.342 | 0.246 |  | 0.779 | 0.466 | 0.321 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.391 | 0.280 | 0.211 |  | 0.551 | 0.389 | 0.294 |  | 0.687 | 0.417 | 0.277 |  | 0.995 | 0.626 | 0.410 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.384 | 0.291 | 0.227 |  | 0.536 | 0.395 | 0.303 |  | 0.644 | 0.428 | 0.297 |  | 0.925 | 0.622 | 0.427 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.467 | 0.333 | 0.248 |  | 0.636 | 0.452 | 0.334 |  | 0.765 | 0.472 | 0.328 |  | 1.111 | 0.691 | 0.472 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.458 | 0.324 | 0.252 |  | 0.615 | 0.438 | 0.325 |  | 0.729 | 0.460 | 0.323 |  | 1.027 | 0.640 | 0.440 |
| GAS |  | 0.440 | 0.330 | 0.267 |  | 0.577 | 0.416 | 0.323 |  | 0.980 | 0.483 | 0.337 |  | 0.938 | 0.616 | 0.458 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.197 | 0.152 | 0.124 |  | 0.687 | 0.502 | 0.372 |  | 0.636 | 0.351 | 0.215 |  | 1.461 | 0.904 | 0.577 |
| Student-tt |  | 0.206 | 0.158 | 0.128 |  | 0.535 | 0.422 | 0.334 |  | 0.410 | 0.265 | 0.188 |  | 0.984 | 0.678 | 0.483 |
| Skew-tt |  | 0.225 | 0.171 | 0.138 |  | 0.302 | 0.215 | 0.163 |  | 0.446 | 0.286 | 0.201 |  | 0.654 | 0.401 | 0.265 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.199 | 0.153 | 0.125 |  | 0.686 | 0.502 | 0.372 |  | 0.638 | 0.353 | 0.217 |  | 1.462 | 0.904 | 0.577 |
| Student-tt |  | 0.204 | 0.156 | 0.127 |  | 0.535 | 0.421 | 0.334 |  | 0.410 | 0.265 | 0.188 |  | 0.982 | 0.676 | 0.482 |
| Skew-tt |  | 0.225 | 0.172 | 0.139 |  | 0.304 | 0.217 | 0.163 |  | 0.446 | 0.288 | 0.203 |  | 0.642 | 0.393 | 0.260 |
| EGARCH |  | 0.243 | 0.193 | 0.162 |  | 0.727 | 0.538 | 0.404 |  | 0.699 | 0.409 | 0.268 |  | 1.524 | 0.962 | 0.632 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.378 | 0.282 | 0.227 |  | 0.510 | 0.361 | 0.281 |  | 0.672 | 0.424 | 0.307 |  | 0.993 | 0.602 | 0.417 |
| QbSD-gAS |  | 0.410 | 0.309 | 0.253 |  | 0.552 | 0.396 | 0.311 |  | 0.736 | 0.467 | 0.340 |  | 1.171 | 0.707 | 0.493 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.498 | 0.363 | 0.289 |  | 0.730 | 0.519 | 0.406 |  | 0.968 | 0.564 | 0.406 |  | 1.687 | 0.985 | 0.672 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.502 | 0.384 | 0.311 |  | 0.716 | 0.528 | 0.414 |  | 0.842 | 0.589 | 0.431 |  | 1.268 | 0.884 | 0.631 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.594 | 0.437 | 0.333 |  | 0.803 | 0.604 | 0.446 |  | 0.993 | 0.624 | 0.453 |  | 1.589 | 0.994 | 0.989 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.590 | 0.428 | 0.340 |  | 0.780 | 0.590 | 0.435 |  | 0.956 | 0.643 | 0.462 |  | 1.373 | 0.888 | 0.708 |
| GAS |  | 0.875 | 0.494 | 0.371 |  | 0.950 | 0.740 | 0.474 |  | 9.766 | 0.979 | 0.652 |  | 1.342 | 1.124 | 1.098 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.242 | 0.193 | 0.163 |  | 0.724 | 0.538 | 0.406 |  | 0.689 | 0.403 | 0.270 |  | 1.515 | 0.952 | 0.625 |
| Student-tt |  | 0.276 | 0.212 | 0.173 |  | 0.602 | 0.471 | 0.373 |  | 0.582 | 0.376 | 0.269 |  | 1.089 | 0.743 | 0.529 |
| Skew-tt |  | 0.300 | 0.230 | 0.186 |  | 0.436 | 0.316 | 0.242 |  | 0.629 | 0.406 | 0.287 |  | 0.959 | 0.591 | 0.397 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.246 | 0.196 | 0.165 |  | 0.724 | 0.538 | 0.406 |  | 0.690 | 0.407 | 0.275 |  | 1.512 | 0.950 | 0.622 |
| Student-tt |  | 0.274 | 0.210 | 0.171 |  | 0.602 | 0.470 | 0.371 |  | 0.580 | 0.375 | 0.268 |  | 1.093 | 0.747 | 0.533 |
| Skew-tt |  | 0.299 | 0.230 | 0.186 |  | 0.421 | 0.305 | 0.232 |  | 0.622 | 0.403 | 0.287 |  | 0.974 | 0.603 | 0.407 |
| EGARCH |  | 0.318 | 0.260 | 0.219 |  | 0.784 | 0.593 | 0.456 |  | 0.779 | 0.492 | 0.351 |  | 1.599 | 1.033 | 0.702 |



Table B3. VaR forecasting results when θ=0.5\theta=0.5 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.302 | 0.226 | 0.185 |  | 0.396 | 0.289 | 0.229 |  | 0.373 | 0.243 | 0.181 |  | 0.545 | 0.344 | 0.240 |
| QbSD-gAS |  | 0.262 | 0.196 | 0.159 |  | 0.357 | 0.260 | 0.204 |  | 0.356 | 0.232 | 0.172 |  | 0.547 | 0.331 | 0.235 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.420 | 0.296 | 0.234 |  | 0.592 | 0.419 | 0.308 |  | 0.573 | 0.354 | 0.244 |  | 0.866 | 0.554 | 0.357 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.419 | 0.301 | 0.239 |  | 0.594 | 0.421 | 0.318 |  | 0.567 | 0.350 | 0.251 |  | 0.823 | 0.528 | 0.348 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.441 | 0.305 | 0.225 |  | 0.656 | 0.433 | 0.341 |  | 0.612 | 0.390 | 0.252 |  | 0.954 | 0.584 | 0.395 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.445 | 0.318 | 0.231 |  | 0.653 | 0.448 | 0.344 |  | 0.604 | 0.387 | 0.260 |  | 0.958 | 0.603 | 0.402 |
| GAS |  | 0.483 | 0.336 | 0.248 |  | 0.756 | 0.522 | 0.355 |  | 0.591 | 0.393 | 0.251 |  | 0.946 | 0.576 | 0.401 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.244 | 0.199 | 0.165 |  | 0.565 | 0.374 | 0.244 |  | 0.355 | 0.232 | 0.195 |  | 0.920 | 0.466 | 0.241 |
| Student-tt |  | 0.255 | 0.201 | 0.163 |  | 0.488 | 0.358 | 0.255 |  | 0.320 | 0.215 | 0.159 |  | 0.717 | 0.447 | 0.273 |
| Skew-tt |  | 0.263 | 0.205 | 0.165 |  | 0.294 | 0.214 | 0.165 |  | 0.329 | 0.220 | 0.161 |  | 0.384 | 0.233 | 0.157 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.234 | 0.190 | 0.157 |  | 0.560 | 0.369 | 0.240 |  | 0.352 | 0.223 | 0.186 |  | 0.916 | 0.464 | 0.239 |
| Student-tt |  | 0.253 | 0.200 | 0.162 |  | 0.487 | 0.357 | 0.254 |  | 0.316 | 0.214 | 0.159 |  | 0.717 | 0.446 | 0.272 |
| Skew-tt |  | 0.263 | 0.205 | 0.165 |  | 0.294 | 0.215 | 0.165 |  | 0.330 | 0.223 | 0.164 |  | 0.384 | 0.232 | 0.156 |
| EGARCH |  | 0.213 | 0.172 | 0.143 |  | 0.582 | 0.386 | 0.252 |  | 0.368 | 0.226 | 0.185 |  | 0.944 | 0.507 | 0.285 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.393 | 0.304 | 0.250 |  | 0.534 | 0.403 | 0.324 |  | 0.520 | 0.344 | 0.265 |  | 1.032 | 0.690 | 0.411 |
| QbSD-gAS |  | 0.395 | 0.290 | 0.238 |  | 0.575 | 0.417 | 0.331 |  | 0.643 | 0.411 | 0.308 |  | 1.670 | 0.782 | 0.515 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.561 | 0.403 | 0.320 |  | 0.820 | 0.586 | 0.447 |  | 0.867 | 0.529 | 0.363 |  | 1.663 | 1.173 | 0.648 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.555 | 0.414 | 0.325 |  | 0.832 | 0.580 | 0.456 |  | 0.838 | 0.529 | 0.381 |  | 1.290 | 0.909 | 0.547 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.594 | 0.469 | 0.311 |  | 0.908 | 0.607 | 0.531 |  | 0.925 | 0.873 | 0.382 |  | 1.332 | 0.908 | 0.695 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.607 | 0.493 | 0.317 |  | 0.896 | 0.634 | 0.484 |  | 0.858 | 0.816 | 0.395 |  | 1.470 | 1.022 | 0.734 |
| GAS |  | 0.758 | 0.617 | 0.336 |  | 1.258 | 1.040 | 0.518 |  | 1.344 | 1.110 | 0.443 |  | 1.883 | 1.041 | 0.851 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.332 | 0.273 | 0.229 |  | 0.662 | 0.450 | 0.305 |  | 0.468 | 0.336 | 0.292 |  | 1.115 | 0.583 | 0.319 |
| Student-tt |  | 0.348 | 0.275 | 0.224 |  | 0.586 | 0.435 | 0.317 |  | 0.454 | 0.307 | 0.228 |  | 0.900 | 0.588 | 0.383 |
| Skew-tt |  | 0.360 | 0.283 | 0.224 |  | 0.412 | 0.300 | 0.228 |  | 0.464 | 0.312 | 0.230 |  | 0.569 | 0.352 | 0.242 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.320 | 0.262 | 0.219 |  | 0.652 | 0.442 | 0.297 |  | 0.462 | 0.331 | 0.289 |  | 1.107 | 0.578 | 0.317 |
| Student-tt |  | 0.347 | 0.275 | 0.222 |  | 0.433 | 0.433 | 0.315 |  | 0.447 | 0.304 | 0.227 |  | 0.899 | 0.587 | 0.383 |
| Skew-tt |  | 0.360 | 0.283 | 0.226 |  | 0.413 | 0.301 | 0.229 |  | 0.474 | 0.323 | 0.239 |  | 0.568 | 0.347 | 0.236 |
| EGARCH |  | 0.298 | 0.242 | 0.201 |  | 0.681 | 0.467 | 0.320 |  | 0.481 | 0.342 | 0.293 |  | 1.106 | 0.626 | 0.413 |



Table B4. ES forecasting results when θ=0.5\theta=0.5 and T=250T=250

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.396 | 0.300 | 0.243 |  | 0.540 | 0.397 | 0.314 |  | 0.633 | 0.402 | 0.289 |  | 0.984 | 0.594 | 0.413 |
| QbSD-gAS |  | 0.348 | 0.258 | 0.209 |  | 0.497 | 0.356 | 0.280 |  | 0.595 | 0.376 | 0.273 |  | 0.979 | 0.589 | 0.410 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.512 | 0.373 | 0.294 |  | 0.741 | 0.524 | 0.398 |  | 0.816 | 0.507 | 0.352 |  | 1.324 | 0.800 | 0.557 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.501 | 0.382 | 0.307 |  | 0.730 | 0.534 | 0.426 |  | 0.771 | 0.505 | 0.362 |  | 1.198 | 0.769 | 0.537 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.542 | 0.384 | 0.285 |  | 0.826 | 0.569 | 0.439 |  | 0.859 | 0.552 | 0.362 |  | 1.358 | 0.872 | 0.599 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.530 | 0.384 | 0.290 |  | 0.806 | 0.561 | 0.426 |  | 0.818 | 0.520 | 0.362 |  | 1.287 | 0.814 | 0.564 |
| GAS |  | 0.595 | 0.439 | 0.328 |  | 0.950 | 0.692 | 0.484 |  | 0.849 | 0.588 | 0.382 |  | 1.463 | 0.909 | 0.633 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.301 | 0.249 | 0.213 |  | 0.804 | 0.591 | 0.442 |  | 0.710 | 0.417 | 0.283 |  | 1.729 | 1.071 | 0.685 |
| Student-tt |  | 0.332 | 0.265 | 0.219 |  | 0.621 | 0.495 | 0.396 |  | 0.541 | 0.364 | 0.269 |  | 1.119 | 0.780 | 0.561 |
| Skew-tt |  | 0.341 | 0.271 | 0.221 |  | 0.413 | 0.309 | 0.244 |  | 0.553 | 0.374 | 0.275 |  | 0.312 | 0.452 | 0.312 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.292 | 0.239 | 0.204 |  | 0.799 | 0.586 | 0.438 |  | 0.713 | 0.416 | 0.278 |  | 1.724 | 1.067 | 0.682 |
| Student-tt |  | 0.329 | 0.262 | 0.216 |  | 0.624 | 0.494 | 0.395 |  | 0.531 | 0.359 | 0.266 |  | 1.117 | 0.778 | 0.561 |
| Skew-tt |  | 0.340 | 0.271 | 0.223 |  | 0.412 | 0.310 | 0.244 |  | 0.546 | 0.372 | 0.276 |  | 0.313 | 0.454 | 0.313 |
| EGARCH |  | 0.271 | 0.218 | 0.185 |  | 0.824 | 0.609 | 0.456 |  | 0.746 | 0.436 | 0.288 |  | 1.739 | 1.090 | 0.715 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.518 | 0.395 | 0.326 |  | 0.738 | 0.540 | 0.433 |  | 0.909 | 0.566 | 0.411 |  | 2.831 | 1.513 | 0.963 |
| QbSD-gAS |  | 0.506 | 0.389 | 0.315 |  | 0.792 | 0.577 | 0.458 |  | 1.101 | 0.700 | 0.503 |  | 3.575 | 1.994 | 1.261 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.673 | 0.498 | 0.399 |  | 1.004 | 0.726 | 0.578 |  | 1.297 | 0.826 | 0.555 |  | 3.951 | 1.726 | 1.266 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.653 | 0.506 | 0.405 |  | 0.986 | 0.703 | 0.572 |  | 1.072 | 0.711 | 0.510 |  | 1.737 | 1.143 | 0.771 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.717 | 0.542 | 0.391 |  | 1.109 | 0.775 | 0.659 |  | 1.269 | 1.080 | 0.562 |  | 2.212 | 1.712 | 1.136 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.707 | 0.550 | 0.382 |  | 1.084 | 0.757 | 0.567 |  | 1.120 | 0.875 | 0.515 |  | 1.984 | 1.306 | 0.803 |
| GAS |  | 0.905 | 0.725 | 0.446 |  | 1.480 | 1.229 | 0.711 |  | 1.688 | 1.362 | 0.626 |  | 3.622 | 1.643 | 1.367 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.403 | 0.337 | 0.291 |  | 0.921 | 0.689 | 0.525 |  | 0.835 | 0.529 | 0.385 |  | 2.058 | 1.289 | 0.838 |
| Student-tt |  | 0.451 | 0.359 | 0.299 |  | 0.743 | 0.594 | 0.480 |  | 0.787 | 0.522 | 0.383 |  | 1.358 | 0.966 | 0.714 |
| Skew-tt |  | 0.466 | 0.371 | 0.303 |  | 0.583 | 0.435 | 0.342 |  | 0.796 | 0.531 | 0.390 |  | 1.054 | 0.670 | 0.466 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.390 | 0.325 | 0.280 |  | 0.910 | 0.680 | 0.517 |  | 0.827 | 0.522 | 0.379 |  | 2.049 | 1.282 | 0.832 |
| Student-tt |  | 0.450 | 0.359 | 0.298 |  | 0.750 | 0.592 | 0.478 |  | 0.761 | 0.510 | 0.377 |  | 1.356 | 0.966 | 0.713 |
| Skew-tt |  | 0.465 | 0.371 | 0.306 |  | 0.586 | 0.436 | 0.343 |  | 0.792 | 0.536 | 0.398 |  | 1.061 | 0.674 | 0.465 |
| EGARCH |  | 0.369 | 0.304 | 0.259 |  | 0.940 | 0.707 | 0.542 |  | 0.853 | 0.543 | 0.395 |  | 2.007 | 1.268 | 0.845 |



Table B5. VaR forecasting results when θ=0\theta=0 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.078 | 0.057 | 0.046 |  | 0.099 | 0.070 | 0.054 |  | 0.112 | 0.071 | 0.052 |  | 0.150 | 0.090 | 0.062 |
| QbSD-gAS |  | 0.088 | 0.066 | 0.053 |  | 0.107 | 0.077 | 0.059 |  | 0.121 | 0.079 | 0.058 |  | 0.154 | 0.095 | 0.065 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.109 | 0.071 | 0.052 |  | 0.148 | 0.093 | 0.067 |  | 0.168 | 0.092 | 0.060 |  | 0.235 | 0.127 | 0.079 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.111 | 0.073 | 0.054 |  | 0.150 | 0.097 | 0.070 |  | 0.169 | 0.097 | 0.064 |  | 0.242 | 0.133 | 0.088 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.124 | 0.081 | 0.058 |  | 0.173 | 0.108 | 0.077 |  | 0.192 | 0.107 | 0.068 |  | 0.278 | 0.149 | 0.092 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.125 | 0.083 | 0.060 |  | 0.175 | 0.110 | 0.082 |  | 0.197 | 0.111 | 0.071 |  | 0.284 | 0.159 | 0.103 |
| GAS |  | 0.275 | 0.191 | 0.143 |  | 0.323 | 0.203 | 0.139 |  | 0.326 | 0.210 | 0.144 |  | 0.374 | 0.221 | 0.135 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.074 | 0.045 | 0.035 |  | 0.466 | 0.294 | 0.172 |  | 0.225 | 0.068 | 0.077 |  | 0.747 | 0.348 | 0.135 |
| Student-tt |  | 0.055 | 0.042 | 0.034 |  | 0.380 | 0.276 | 0.189 |  | 0.078 | 0.053 | 0.040 |  | 0.592 | 0.361 | 0.211 |
| Skew-tt |  | 0.058 | 0.045 | 0.036 |  | 0.076 | 0.053 | 0.040 |  | 0.082 | 0.055 | 0.041 |  | 0.119 | 0.072 | 0.048 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.074 | 0.045 | 0.035 |  | 0.466 | 0.294 | 0.172 |  | 0.225 | 0.069 | 0.077 |  | 0.745 | 0.347 | 0.135 |
| Student-tt |  | 0.055 | 0.042 | 0.034 |  | 0.380 | 0.276 | 0.189 |  | 0.078 | 0.053 | 0.040 |  | 0.592 | 0.361 | 0.211 |
| Skew-tt |  | 0.059 | 0.045 | 0.036 |  | 0.076 | 0.053 | 0.040 |  | 0.082 | 0.055 | 0.041 |  | 0.112 | 0.068 | 0.045 |
| EGARCH |  | 0.075 | 0.048 | 0.040 |  | 0.472 | 0.299 | 0.176 |  | 0.230 | 0.070 | 0.080 |  | 0.761 | 0.355 | 0.132 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.104 | 0.076 | 0.061 |  | 0.131 | 0.092 | 0.071 |  | 0.153 | 0.098 | 0.073 |  | 0.202 | 0.124 | 0.089 |
| QbSD-gAS |  | 0.119 | 0.090 | 0.073 |  | 0.143 | 0.103 | 0.080 |  | 0.167 | 0.111 | 0.083 |  | 0.221 | 0.142 | 0.100 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.150 | 0.094 | 0.069 |  | 0.209 | 0.124 | 0.089 |  | 0.247 | 0.129 | 0.084 |  | 0.363 | 0.188 | 0.117 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.153 | 0.098 | 0.071 |  | 0.214 | 0.131 | 0.094 |  | 0.255 | 0.140 | 0.096 |  | 0.375 | 0.201 | 0.146 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.176 | 0.111 | 0.078 |  | 0.246 | 0.149 | 0.106 |  | 0.285 | 0.154 | 0.096 |  | 0.424 | 0.220 | 0.134 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.177 | 0.113 | 0.081 |  | 0.252 | 0.153 | 0.115 |  | 0.303 | 0.165 | 0.103 |  | 0.451 | 0.238 | 0.161 |
| GAS |  | 0.355 | 0.256 | 0.191 |  | 0.452 | 0.267 | 0.182 |  | 0.506 | 0.305 | 0.206 |  | 0.524 | 0.305 | 0.185 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.090 | 0.061 | 0.051 |  | 0.478 | 0.304 | 0.182 |  | 0.247 | 0.101 | 0.115 |  | 0.774 | 0.370 | 0.162 |
| Student-tt |  | 0.077 | 0.060 | 0.049 |  | 0.394 | 0.286 | 0.197 |  | 0.119 | 0.084 | 0.064 |  | 0.610 | 0.374 | 0.221 |
| Skew-tt |  | 0.081 | 0.063 | 0.051 |  | 0.107 | 0.078 | 0.059 |  | 0.125 | 0.087 | 0.065 |  | 0.182 | 0.143 | 0.096 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.091 | 0.062 | 0.052 |  | 0.478 | 0.304 | 0.182 |  | 0.248 | 0.102 | 0.115 |  | 0.769 | 0.367 | 0.163 |
| Student-tt |  | 0.077 | 0.060 | 0.049 |  | 0.394 | 0.286 | 0.197 |  | 0.119 | 0.084 | 0.064 |  | 0.610 | 0.374 | 0.221 |
| Skew-tt |  | 0.081 | 0.063 | 0.051 |  | 0.107 | 0.078 | 0.059 |  | 0.125 | 0.087 | 0.065 |  | 0.184 | 0.118 | 0.081 |
| EGARCH |  | 0.103 | 0.069 | 0.055 |  | 0.490 | 0.314 | 0.190 |  | 0.268 | 0.105 | 0.103 |  | 0.805 | 0.389 | 0.166 |



Table B6. ES forecasting results when θ=0\theta=0 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.104 | 0.079 | 0.064 |  | 0.138 | 0.100 | 0.081 |  | 0.199 | 0.126 | 0.092 |  | 0.278 | 0.172 | 0.123 |
| QbSD-gAS |  | 0.113 | 0.086 | 0.072 |  | 0.144 | 0.107 | 0.087 |  | 0.202 | 0.131 | 0.097 |  | 0.280 | 0.173 | 0.126 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.134 | 0.088 | 0.066 |  | 0.187 | 0.118 | 0.088 |  | 0.253 | 0.140 | 0.090 |  | 0.368 | 0.199 | 0.128 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.157 | 0.109 | 0.082 |  | 0.216 | 0.148 | 0.105 |  | 0.297 | 0.175 | 0.115 |  | 0.446 | 0.253 | 0.157 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.156 | 0.100 | 0.073 |  | 0.219 | 0.136 | 0.101 |  | 0.286 | 0.158 | 0.101 |  | 0.417 | 0.229 | 0.146 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.173 | 0.116 | 0.087 |  | 0.243 | 0.157 | 0.115 |  | 0.335 | 0.191 | 0.122 |  | 0.471 | 0.269 | 0.166 |
| GAS |  | 0.332 | 0.240 | 0.188 |  | 0.390 | 0.261 | 0.190 |  | 0.442 | 0.295 | 0.214 |  | 0.535 | 0.323 | 0.206 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.136 | 0.083 | 0.056 |  | 0.676 | 0.490 | 0.357 |  | 0.618 | 0.308 | 0.148 |  | 1.443 | 0.880 | 0.546 |
| Student-tt |  | 0.075 | 0.057 | 0.047 |  | 0.473 | 0.382 | 0.305 |  | 0.132 | 0.088 | 0.065 |  | 0.932 | 0.646 | 0.461 |
| Skew-tt |  | 0.079 | 0.061 | 0.049 |  | 0.110 | 0.080 | 0.062 |  | 0.137 | 0.092 | 0.068 |  | 0.220 | 0.140 | 0.097 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.136 | 0.084 | 0.056 |  | 0.676 | 0.490 | 0.357 |  | 0.619 | 0.309 | 0.148 |  | 1.440 | 0.877 | 0.544 |
| Student-tt |  | 0.076 | 0.057 | 0.047 |  | 0.473 | 0.382 | 0.305 |  | 0.132 | 0.088 | 0.065 |  | 0.932 | 0.646 | 0.471 |
| Skew-tt |  | 0.079 | 0.061 | 0.049 |  | 0.110 | 0.080 | 0.062 |  | 0.137 | 0.092 | 0.068 |  | 0.206 | 0.132 | 0.091 |
| EGARCH |  | 0.138 | 0.084 | 0.058 |  | 0.683 | 0.496 | 0.363 |  | 0.630 | 0.317 | 0.150 |  | 1.460 | 0.894 | 0.557 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.138 | 0.105 | 0.086 |  | 0.180 | 0.132 | 0.107 |  | 0.257 | 0.169 | 0.125 |  | 0.355 | 0.225 | 0.163 |
| QbSD-gAS |  | 0.152 | 0.119 | 0.099 |  | 0.189 | 0.143 | 0.116 |  | 0.266 | 0.179 | 0.135 |  | 0.369 | 0.237 | 0.178 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.184 | 0.118 | 0.087 |  | 0.260 | 0.160 | 0.119 |  | 0.350 | 0.192 | 0.125 |  | 0.531 | 0.286 | 0.187 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.217 | 0.154 | 0.110 |  | 0.306 | 0.206 | 0.142 |  | 0.480 | 0.267 | 0.162 |  | 0.751 | 0.421 | 0.223 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.214 | 0.139 | 0.099 |  | 0.303 | 0.188 | 0.142 |  | 0.397 | 0.223 | 0.143 |  | 0.594 | 0.325 | 0.215 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.245 | 0.163 | 0.117 |  | 0.348 | 0.219 | 0.157 |  | 0.531 | 0.298 | 0.167 |  | 0.764 | 0.419 | 0.236 |
| GAS |  | 0.434 | 0.321 | 0.250 |  | 0.545 | 0.346 | 0.282 |  | 0.668 | 0.426 | 0.300 |  | 0.750 | 0.459 | 0.282 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.152 | 0.099 | 0.071 |  | 0.691 | 0.502 | 0.368 |  | 0.641 | 0.328 | 0.169 |  | 1.486 | 0.909 | 0.569 |
| Student-tt |  | 0.102 | 0.079 | 0.066 |  | 0.492 | 0.396 | 0.316 |  | 0.190 | 0.132 | 0.100 |  | 0.962 | 0.667 | 0.476 |
| Skew-tt |  | 0.107 | 0.084 | 0.069 |  | 0.150 | 0.113 | 0.089 |  | 0.199 | 0.139 | 0.105 |  | 0.399 | 0.263 | 0.187 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.153 | 0.100 | 0.072 |  | 0.691 | 0.502 | 0.368 |  | 0.642 | 0.329 | 0.170 |  | 1.479 | 0.903 | 0.565 |
| Student-tt |  | 0.102 | 0.080 | 0.066 |  | 0.492 | 0.396 | 0.316 |  | 0.190 | 0.132 | 0.100 |  | 0.962 | 0.667 | 0.476 |
| Skew-tt |  | 0.107 | 0.084 | 0.069 |  | 0.150 | 0.113 | 0.089 |  | 0.198 | 0.138 | 0.105 |  | 0.321 | 0.212 | 0.152 |
| EGARCH |  | 0.168 | 0.113 | 0.082 |  | 0.705 | 0.514 | 0.378 |  | 0.669 | 0.351 | 0.186 |  | 1.524 | 0.940 | 0.594 |

Table B7. VaR forecasting results when θ=0.5\theta=0.5 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.209 | 0.168 | 0.137 |  | 0.258 | 0.202 | 0.161 |  | 0.226 | 0.166 | 0.127 |  | 0.296 | 0.204 | 0.150 |
| QbSD-gAS |  | 0.096 | 0.072 | 0.057 |  | 0.135 | 0.099 | 0.077 |  | 0.130 | 0.086 | 0.063 |  | 0.196 | 0.126 | 0.088 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.227 | 0.174 | 0.140 |  | 0.292 | 0.212 | 0.167 |  | 0.267 | 0.176 | 0.130 |  | 0.373 | 0.228 | 0.157 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.228 | 0.175 | 0.142 |  | 0.292 | 0.215 | 0.170 |  | 0.267 | 0.179 | 0.134 |  | 0.393 | 0.238 | 0.171 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.135 | 0.090 | 0.068 |  | 0.204 | 0.132 | 0.097 |  | 0.211 | 0.114 | 0.077 |  | 0.352 | 0.180 | 0.117 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.138 | 0.093 | 0.072 |  | 0.207 | 0.138 | 0.107 |  | 0.209 | 0.120 | 0.085 |  | 0.360 | 0.197 | 0.142 |
| GAS |  | 0.370 | 0.239 | 0.155 |  | 0.597 | 0.345 | 0.210 |  | 0.430 | 0.236 | 0.141 |  | 0.720 | 0.340 | 0.204 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.204 | 0.167 | 0.139 |  | 0.526 | 0.336 | 0.207 |  | 0.287 | 0.172 | 0.154 |  | 0.857 | 0.401 | 0.168 |
| Student-tt |  | 0.206 | 0.168 | 0.138 |  | 0.427 | 0.316 | 0.223 |  | 0.226 | 0.169 | 0.131 |  | 0.672 | 0.414 | 0.245 |
| Skew-tt |  | 0.207 | 0.168 | 0.138 |  | 0.201 | 0.157 | 0.124 |  | 0.227 | 0.169 | 0.131 |  | 0.221 | 0.151 | 0.110 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.195 | 0.158 | 0.132 |  | 0.526 | 0.336 | 0.207 |  | 0.287 | 0.164 | 0.146 |  | 0.857 | 0.401 | 0.167 |
| Student-tt |  | 0.206 | 0.168 | 0.138 |  | 0.427 | 0.316 | 0.223 |  | 0.226 | 0.169 | 0.131 |  | 0.672 | 0.414 | 0.245 |
| Skew-tt |  | 0.207 | 0.169 | 0.138 |  | 0.201 | 0.157 | 0.124 |  | 0.228 | 0.169 | 0.131 |  | 0.218 | 0.150 | 0.109 |
| EGARCH |  | 0.086 | 0.058 | 0.048 |  | 0.548 | 0.348 | 0.206 |  | 0.247 | 0.079 | 0.087 |  | 0.893 | 0.420 | 0.161 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.283 | 0.227 | 0.185 |  | 0.357 | 0.279 | 0.220 |  | 0.317 | 0.235 | 0.180 |  | 0.447 | 0.311 | 0.229 |
| QbSD-gAS |  | 0.133 | 0.100 | 0.079 |  | 0.197 | 0.146 | 0.113 |  | 0.193 | 0.134 | 0.101 |  | 0.327 | 0.238 | 0.176 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.308 | 0.234 | 0.188 |  | 0.416 | 0.296 | 0.232 |  | 0.389 | 0.252 | 0.185 |  | 0.596 | 0.349 | 0.241 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.312 | 0.237 | 0.190 |  | 0.413 | 0.304 | 0.237 |  | 0.402 | 0.263 | 0.190 |  | 0.689 | 0.381 | 0.271 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.189 | 0.128 | 0.096 |  | 0.296 | 0.193 | 0.147 |  | 0.317 | 0.178 | 0.122 |  | 0.641 | 0.299 | 0.214 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.193 | 0.135 | 0.105 |  | 0.309 | 0.209 | 0.174 |  | 0.317 | 0.208 | 0.146 |  | 0.656 | 0.371 | 0.345 |
| GAS |  | 0.479 | 0.319 | 0.206 |  | 0.920 | 0.461 | 0.289 |  | 0.872 | 0.324 | 0.195 |  | 1.454 | 0.521 | 0.342 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.273 | 0.224 | 0.188 |  | 0.616 | 0.406 | 0.261 |  | 0.388 | 0.263 | 0.239 |  | 1.018 | 0.488 | 0.237 |
| Student-tt |  | 0.279 | 0.226 | 0.186 |  | 0.515 | 0.386 | 0.278 |  | 0.344 | 0.256 | 0.198 |  | 0.818 | 0.511 | 0.311 |
| Skew-tt |  | 0.281 | 0.227 | 0.186 |  | 0.284 | 0.219 | 0.172 |  | 0.349 | 0.258 | 0.199 |  | 0.374 | 0.250 | 0.177 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.264 | 0.216 | 0.182 |  | 0.616 | 0.406 | 0.261 |  | 0.384 | 0.257 | 0.233 |  | 1.017 | 0.488 | 0.236 |
| Student-tt |  | 0.279 | 0.226 | 0.186 |  | 0.515 | 0.386 | 0.278 |  | 0.343 | 0.255 | 0.198 |  | 0.819 | 0.511 | 0.311 |
| Skew-tt |  | 0.281 | 0.227 | 0.186 |  | 0.284 | 0.219 | 0.172 |  | 0.350 | 0.259 | 0.199 |  | 0.364 | 0.246 | 0.175 |
| EGARCH |  | 0.123 | 0.084 | 0.066 |  | 0.637 | 0.416 | 0.260 |  | 0.311 | 0.125 | 0.112 |  | 1.164 | 0.593 | 0.279 |



Table B8. ES forecasting results when θ=0.5\theta=0.5 and T=2500T=2500

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | v=20v=20, λ=0\lambda=0 | | |  | v=20v=20, λ=−0.5\lambda=-0.5 | | |  | v=5v=5, λ=0\lambda=0 | | |  | v=5v=5, λ=−0.5\lambda=-0.5 | | |
|  | α=\alpha= | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |  | 0.01 | 0.025 | 0.05 |
| Panel A: Mean absolute error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.251 | 0.208 | 0.178 |  | 0.319 | 0.259 | 0.217 |  | 0.326 | 0.236 | 0.185 |  | 0.459 | 0.319 | 0.243 |
| QbSD-gAS |  | 0.123 | 0.095 | 0.078 |  | 0.178 | 0.135 | 0.109 |  | 0.216 | 0.142 | 0.106 |  | 0.335 | 0.216 | 0.157 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.273 | 0.216 | 0.184 |  | 0.359 | 0.273 | 0.226 |  | 0.377 | 0.251 | 0.191 |  | 0.547 | 0.346 | 0.249 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.294 | 0.236 | 0.194 |  | 0.392 | 0.315 | 0.252 |  | 0.423 | 0.290 | 0.210 |  | 0.664 | 0.422 | 0.307 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.166 | 0.113 | 0.086 |  | 0.252 | 0.168 | 0.131 |  | 0.313 | 0.169 | 0.115 |  | 0.522 | 0.280 | 0.187 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.192 | 0.138 | 0.109 |  | 0.299 | 0.216 | 0.172 |  | 0.355 | 0.212 | 0.145 |  | 0.593 | 0.362 | 0.252 |
| GAS |  | 0.455 | 0.310 | 0.209 |  | 0.737 | 0.462 | 0.281 |  | 0.572 | 0.332 | 0.211 |  | 1.030 | 0.508 | 0.311 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.254 | 0.208 | 0.178 |  | 0.763 | 0.553 | 0.405 |  | 0.652 | 0.353 | 0.219 |  | 1.664 | 1.010 | 0.626 |
| Student-tt |  | 0.251 | 0.210 | 0.180 |  | 0.522 | 0.427 | 0.346 |  | 0.319 | 0.241 | 0.193 |  | 1.051 | 0.732 | 0.524 |
| Skew-tt |  | 0.252 | 0.211 | 0.181 |  | 0.254 | 0.206 | 0.172 |  | 0.321 | 0.243 | 0.194 |  | 0.350 | 0.245 | 0.184 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.245 | 0.199 | 0.169 |  | 0.764 | 0.553 | 0.405 |  | 0.659 | 0.356 | 0.217 |  | 1.664 | 1.010 | 0.626 |
| Student-tt |  | 0.251 | 0.210 | 0.180 |  | 0.522 | 0.427 | 0.346 |  | 0.319 | 0.241 | 0.193 |  | 1.051 | 0.732 | 0.524 |
| Skew-tt |  | 0.252 | 0.211 | 0.181 |  | 0.254 | 0.206 | 0.172 |  | 0.321 | 0.243 | 0.194 |  | 0.340 | 0.240 | 0.181 |
| EGARCH |  | 0.151 | 0.095 | 0.068 |  | 0.792 | 0.576 | 0.422 |  | 0.672 | 0.338 | 0.161 |  | 1.708 | 1.048 | 0.655 |
| Panel B: Root mean squared error | | | | | | | | | | | | | | | | |
| QbSD approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QbSD-gSAV |  | 0.341 | 0.281 | 0.240 |  | 0.450 | 0.359 | 0.299 |  | 0.459 | 0.333 | 0.263 |  | 0.715 | 0.491 | 0.372 |
| QbSD-gAS |  | 0.169 | 0.133 | 0.110 |  | 0.255 | 0.195 | 0.159 |  | 0.297 | 0.204 | 0.157 |  | 0.494 | 0.342 | 0.261 |
| AL approach |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ALMult.\text{AL}\_{\text{Mult.}}-SAV |  | 0.373 | 0.292 | 0.248 |  | 0.517 | 0.385 | 0.317 |  | 0.557 | 0.363 | 0.276 |  | 0.883 | 0.705 | 0.384 |
| ALAR\text{AL}\_{\text{AR}}-SAV |  | 0.394 | 0.321 | 0.257 |  | 0.568 | 0.458 | 0.357 |  | 0.613 | 0.408 | 0.294 |  | 1.157 | 0.705 | 0.521 |
| ALMult.\text{AL}\_{\text{Mult.}}-AS |  | 0.231 | 0.162 | 0.123 |  | 0.367 | 0.246 | 0.198 |  | 0.456 | 0.259 | 0.179 |  | 0.853 | 0.458 | 0.347 |
| ALAR\text{AL}\_{\text{AR}}-AS |  | 0.278 | 0.194 | 0.154 |  | 0.455 | 0.330 | 0.258 |  | 0.563 | 0.348 | 0.211 |  | 1.021 | 0.675 | 0.405 |
| GAS |  | 0.586 | 0.415 | 0.272 |  | 1.056 | 0.632 | 0.389 |  | 1.029 | 0.464 | 0.287 |  | 1.973 | 0.844 | 0.475 |
| GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.337 | 0.278 | 0.239 |  | 0.874 | 0.644 | 0.481 |  | 0.772 | 0.456 | 0.310 |  | 1.967 | 1.197 | 0.747 |
| Student-tt |  | 0.341 | 0.285 | 0.244 |  | 0.629 | 0.517 | 0.421 |  | 0.485 | 0.367 | 0.294 |  | 1.268 | 0.888 | 0.641 |
| Skew-tt |  | 0.344 | 0.286 | 0.245 |  | 0.365 | 0.292 | 0.242 |  | 0.495 | 0.373 | 0.298 |  | 0.605 | 0.418 | 0.310 |
| GJR-GARCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal |  | 0.327 | 0.269 | 0.231 |  | 0.874 | 0.644 | 0.481 |  | 0.772 | 0.453 | 0.305 |  | 1.966 | 1.196 | 0.747 |
| Student-tt |  | 0.341 | 0.285 | 0.244 |  | 0.629 | 0.517 | 0.421 |  | 0.485 | 0.367 | 0.294 |  | 1.269 | 0.889 | 0.641 |
| Skew-tt |  | 0.343 | 0.286 | 0.245 |  | 0.365 | 0.292 | 0.242 |  | 0.496 | 0.374 | 0.298 |  | 0.572 | 0.404 | 0.302 |
| EGARCH |  | 0.195 | 0.133 | 0.099 |  | 0.904 | 0.666 | 0.496 |  | 0.756 | 0.403 | 0.218 |  | 2.146 | 1.348 | 0.872 |

## Section C

This appendix reports additional rolling-window evaluations with R=250R=250 and R=2500R=2500. Tables C1–C12 present 90% Model Confidence Set (MCS) rankings for VaR and joint VaR-ES at the 1%, 2.5%, and 5% levels.

Across windows, indices, and tails, the quantile-based scale-dynamics class performs very strongly overall. QbSD-gAS is the front-runner with R=250R=250: it ranks first in most VaR and joint VaR-ES exercises and is almost always in the top two. Its QAR extension (QAR-QbSD-gAS) typically follows closely-often finishing in the top three—but its long-window 1% VaR results slip on a few indices (see Table C7).

With the short window (R=250R=250), patterns are clear. For VaR-only (quantile scores; Tables C1–C3), QbSD-gAS is the *overall* top performer at 1%, 2.5%, and 5%. For joint VaR-ES (AL log scores; Tables C4–C6), skewed-tt GARCH/GJR lead at 1% (Table C4) with QbSD-gAS a close second, while QbSD-gAS returns to the top at 2.5% and 5% (Tables C5–C6).

With the long window (R=2500R=2500), leadership varies by tail and score. For VaR (Tables C7–C9), AL-based specifications dominate at 1% (Table C7), QbSD-gAS ranks first at 2.5% (Table C8), and at 5% EGARCH narrowly takes the lead, with QbSD-gAS essentially tied on average but second in the final ranking (Table C9); note that both have the same average rank (1.9), with QbSD-gAS recording more #1 finishes (4 of 8) while EGARCH is slightly more uniform across indices. For joint VaR-ES (Tables C10–C12), AL-based specifications lead at 1% and 2.5% (Tables C10–C11), whereas QbSD-gAS regains first place at 5% (Table C12).

Among benchmarks, skewed-tt GARCH/GJR are the strongest non-QbSD competitors and are frequently retained in the MCS, especially for R=250R=250 and in VaR-only comparisons. Normal-based GARCH variants generally underperform on average, with two caveats: (i) EGARCH is a strong contender at 5% VaR for R=2500R=2500 (Table C9), and (ii) GJR-GARCH-normal is competitive at R=250R=250 for 2.5% and 5% VaR (Tables C2–C3). Within the AL-based family, AS specifications consistently outperform their SAV counterparts. The gSAV variant of QbSD (QbSD-gSAV) typically trails QbSD-gAS, while QAR-QbSD-gSAV most often attains mid-table results.

Overall, these results align with the paper’s main finding: QbSD-gAS is frequently the strongest—especially with the short window—and remains consistently competitive across indices and tail levels under the long window; QAR-QbSD-gAS is often close behind. At the extreme tail and with long windows, AL-based variants tend to lead, and EGARCH is a notable runner-up at 5% VaR.

Table C1. Ranking of 1% VaR forecasting models using the MCS procedure with quantile scores, rolling window R=250R=250

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 2 | 4 | 2 | 1 | 2 | 1 | 1 | 4 | 8 | 2.1 | 1 |
| QAR-QbSD-gAS | 5 | 6 | 6 | 7 | 1 | 5 | 2 | 1 | 8 | 4.1 | 2 |
| GARCH-skew-tt | 1 | 1 | 1 | 10 | 3 | 11 | 4 | 3 | 8 | 4.2 | 3 |
| GJR-GARCH-skew-tt | 3 | 3 | 5 | 2 | 5 | 10 | 6 | 2 | 8 | 4.5 | 4 |
| GJR-GARCH-tt | 10 | 2 | 9 | 4 | 8 | 3 | 7 | 8 | 8 | 6.4 | 5 |
| AR-GARCH-skew-tt | 6 | 5 | 4 | 5 | 4 | 12 | 12 | 5 | 8 | 6.6 | 6 |
| GARCH-tt | 4 | 9 | 8 | 8 | 11 | 2 | 5 | 9 | 8 | 7.0 | 7 |
| AR-GJR-GARCH-skew-tt | 7 | 8 | 7 | 3 | 7 | 8 | 15 | 6 | 8 | 7.6 | 8 |
| AR-GJR-GARCH-tt | 9 | 7 | 3 | 12 | 6 | 6 | 9 | 10 | 8 | 7.8 | 9 |
| AR-GARCH-tt | 8 | 10 | 10 | 13 | 9 | 4 | 10 | 11 | 8 | 9.4 | 10 |
| GJR-GARCH-normal | 11 | 11 | 14 | 14 | 10 | 9 | 3 | 12 | 8 | 10.5 | 11 |
| QAR-QbSD-gSAV | 15 |  | 11 | 9 | 14 | 7 | 16 | 7 | 7 | 13.4 | 12 |
| QbSD-gSAV | 21 | 19 | 12 | 6 | 12 | 13 | 17 | 13 | 8 | 14.1 | 13 |
| AR-GJR-GARCH-normal | 18 | 18 |  | 17 | 16 | 17 | 11 | 14 | 7 | 17.4 | 14 |
| GAS | 13 | 16 |  | 19 | 17 | 20 | 14 | 15 | 7 | 17.8 | 15 |
| AR-GAS | 16 | 17 | 13 | 11 |  | 18 | 13 |  | 6 | 18.0 | 16 |
| GARCH-normal | 19 | 24 |  | 15 | 18 | 15 | 8 |  | 6 | 19.4 | 17 |
| EGARCH | 20 | 23 |  | 21 | 13 | 16 | 20 |  | 6 | 21.1 | 18 |
| AR-EGARCH | 23 | 27 |  |  | 15 | 14 | 19 |  | 5 | 22.8 | 19 |
| AR-GARCH-normal |  | 26 |  | 16 |  | 19 | 18 |  | 4 | 23.9 | 20 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 17 | 14 |  | 20 |  |  |  |  | 3 | 23.9 | 21 |
| AR-ALAR{}\_{\text{AR}}-AS |  | 12 |  | 18 |  |  |  |  | 2 | 24.8 | 22 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 14 | 20 |  |  |  |  |  |  | 2 | 25.2 | 23 |
| AR-ALAR{}\_{\text{AR}}-SAV | 12 | 22 |  |  |  |  |  |  | 2 | 25.2 | 24 |
| ALAR{}\_{\text{AR}}-SAV |  | 13 |  |  |  |  |  |  | 1 | 26.1 | 25 |
| ALMult.{}\_{\text{Mult.}}-SAV |  | 15 |  |  |  |  |  |  | 1 | 26.4 | 26 |
| ALAR{}\_{\text{AR}}-AS | 22 | 21 |  |  |  |  |  |  | 2 | 26.4 | 27 |
| ALMult.{}\_{\text{Mult.}}-AS |  | 25 |  |  |  |  |  |  | 1 | 27.6 | 28 |



Table C2. Ranking of 2.5% VaR forecasting models using the MCS procedure with quantile scores, rolling window R=250R=250

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 8 | 1.4 | 1 |
| GARCH-skew-tt | 3 | 2 | 2 | 4 | 4 | 6 | 8 | 3 | 8 | 4.0 | 2 |
| QAR-QbSD-gAS | 1 | 5 | 18 | 3 | 1 | 4 | 2 | 1 | 8 | 4.4 | 3 |
| GJR-GARCH-normal | 5 | 4 | 5 | 11 | 3 | 2 | 3 | 7 | 8 | 5.0 | 4 |
| GARCH-tt | 8 | 7 | 7 | 9 | 9 | 5 | 4 | 9 | 8 | 7.2 | 5 |
| GJR-GARCH-tt | 11 | 6 | 9 | 10 | 7 | 3 | 5 | 8 | 8 | 7.4 | 6 |
| GJR-GARCH-skew-tt | 4 | 3 | 3 | 5 | 6 | 8 |  | 4 | 7 | 7.6 | 7 |
| AR-GARCH-skew-tt | 7 | 8 | 8 | 8 | 8 | 9 |  | 6 | 7 | 10.2 | 8 |
| AR-GJR-GARCH-skew-tt | 6 | 10 | 6 | 7 | 12 | 10 |  | 5 | 7 | 10.5 | 9 |
| GARCH-normal | 13 | 9 | 10 | 12 | 10 | 11 | 6 |  | 7 | 12.4 | 10 |
| AR-GJR-GARCH-normal | 10 | 11 | 16 | 16 |  | 12 | 7 | 11 | 7 | 13.9 | 11 |
| AR-GARCH-tt | 9 | 12 | 11 | 13 | 14 | 14 |  |  | 6 | 16.1 | 12 |
| AR-GJR-GARCH-tt | 12 | 14 | 4 | 14 | 15 | 15 |  |  | 6 | 16.2 | 13 |
| EGARCH | 15 | 17 | 12 | 17 | 5 | 13 |  |  | 6 | 16.9 | 14 |
| AR-EGARCH | 14 | 20 | 14 |  | 11 | 7 |  |  | 5 | 18.8 | 15 |
| QAR-QbSD-gSAV | 18 | 18 | 15 | 2 | 13 |  |  |  | 5 | 18.8 | 16 |
| QbSD-gSAV | 25 | 13 | 13 | 6 |  |  |  |  | 4 | 21.1 | 17 |
| AR-GARCH-normal | 16 | 15 |  | 15 |  | 20 |  |  | 3 | 23.2 | 18 |
| GAS | 24 |  | 17 | 18 |  |  |  |  | 3 | 24.9 | 19 |
| AR-GAS | 27 |  |  |  |  | 10 |  |  | 2 | 25.6 | 20 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 22 |  |  |  |  | 16 |  |  | 2 | 25.8 | 21 |
| ALMult.{}\_{\text{Mult.}}-AS |  | 16 |  |  |  |  |  |  | 1 | 26.5 | 22 |
| ALAR{}\_{\text{AR}}-SAV | 17 |  |  |  |  |  |  |  | 1 | 26.6 | 23 |
| ALAR{}\_{\text{AR}}-AS | 26 | 19 |  |  |  |  |  |  | 2 | 26.6 | 24 |
| AR-ALAR{}\_{\text{AR}}-SAV | 19 |  |  |  |  |  |  |  | 1 | 26.9 | 25 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 20 |  |  |  |  |  |  |  | 1 | 27.0 | 26 |
| ALMult.{}\_{\text{Mult.}}-SAV | 21 |  |  |  |  |  |  |  | 1 | 27.1 | 27 |
| AR-ALAR{}\_{\text{AR}}-AS | 23 |  |  |  |  |  |  |  | 1 | 27.4 | 28 |



Table C3. Ranking of 5% VaR forecasting models using the MCS procedure with quantile scores, rolling window R=250R=250

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 3 | 1 | 2 | 1 | 1 | 1 | 1 | 3 | 8 | 1.6 | 1 |
| QAR-QbSD-gAS | 1 | 2 | 6 | 3 | 2 | 2 |  | 1 | 7 | 5.6 | 2 |
| GARCH-skew-tt | 4 | 3 | 1 | 2 | 6 | 6 |  | 2 | 7 | 6.5 | 3 |
| GJR-GARCH-normal | 2 | 4 | 4 | 5 | 4 | 3 |  | 7 | 7 | 7.1 | 4 |
| GJR-GARCH-skew-tt | 5 | 5 | 3 | 4 | 12 | 10 |  | 6 | 7 | 9.1 | 5 |
| EGARCH | 7 | 13 | 5 | 13 | 3 | 5 |  | 8 | 7 | 10.2 | 6 |
| GARCH-tt | 12 | 8 | 9 | 7 | 11 | 7 |  | 12 | 7 | 11.8 | 7 |
| AR-EGARCH | 6 | 16 | 7 | 17 | 5 | 4 |  | 13 | 7 | 12.0 | 8 |
| GJR-GARCH-tt | 13 | 7 | 8 | 9 | 15 | 8 |  | 10 | 7 | 12.2 | 9 |
| AR-GJR-GARCH-skew-tt | 9 | 9 | 14 | 14 | 7 | 13 |  | 4 | 7 | 12.2 | 10 |
| GARCH-normal | 8 | 6 | 11 | 11 | 10 | 17 |  | 9 | 7 | 12.5 | 11 |
| AR-GARCH-skew-tt | 11 | 10 | 12 | 16 | 8 | 11 |  | 5 | 7 | 12.6 | 12 |
| AR-GJR-GARCH-normal | 10 | 11 | 13 | 12 | 14 | 9 |  | 11 | 7 | 13.5 | 13 |
| AR-GJR-GARCH-tt | 14 | 18 | 10 | 15 | 9 | 14 |  |  | 6 | 17.0 | 14 |
| AR-GARCH-normal | 16 | 12 | 15 | 10 | 16 | 15 |  |  | 6 | 17.5 | 15 |
| AR-GARCH-tt | 15 | 15 | 17 | 18 | 13 | 12 |  |  | 6 | 18.2 | 16 |
| QAR-QbSD-gSAV | 17 | 19 | 16 | 8 |  | 16 |  |  | 5 | 20.0 | 17 |
| QbSD-gSAV |  | 20 | 18 | 6 |  | 18 |  |  | 4 | 21.8 | 18 |
| AR-ALMult.{}\_{\text{Mult.}}-AS |  | 14 |  |  |  |  |  |  | 1 | 26.2 | 19 |
| ALMult.{}\_{\text{Mult.}}-AS |  | 17 |  |  |  |  |  |  | 1 | 26.6 | 20 |
| GAS | 18 |  |  |  |  |  |  |  | 1 | 26.8 | 21 |
| ALMult.{}\_{\text{Mult.}}-SAV |  |  |  |  |  |  | 19 |  | 1 | 26.9 | 22 |
| AR-ALAR{}\_{\text{AR}}-AS |  | 21 |  |  |  |  |  |  | 1 | 27.1 | 23 |
| AR-GAS |  |  |  |  |  |  |  |  | 0 | 28.0 | 24 |
| ALAR{}\_{\text{AR}}-SAV |  |  |  |  |  |  |  |  | 0 | 28.0 | 25 |
| ALAR{}\_{\text{AR}}-AS |  |  |  |  |  |  |  |  | 0 | 28.0 | 26 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV |  |  |  |  |  |  |  |  | 0 | 28.0 | 27 |
| AR-ALAR{}\_{\text{AR}}-SAV |  |  |  |  |  |  |  |  | 0 | 28.0 | 28 |



Table C4. Ranking of 1% VaR and ES forecasting models based on the MCS procedure using AL log scores, rolling window R=250R=250

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| GJR-GARCH-skew-tt | 2 | 4 | 2 | 1 | 13 | 11 | 3 | 2 | 8 | 4.8 | 1 |
| QbSD-gAS | 9 | 2 | 6 | 5 | 6 | 1 | 1 | 10 | 8 | 5.0 | 2 |
| GARCH-skew-tt | 1 | 1 | 1 | 3 | 9 | 13 | 4 | 9 | 8 | 5.1 | 3 |
| QAR-QbSD-gAS | 8 | 7 | 7 | 16 | 1 | 5 | 2 | 1 | 8 | 5.9 | 4 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 6 | 3 | 5 | 9 | 8 | 7 | 9 | 3 | 8 | 6.2 | 5 |
| ALMult.{}\_{\text{Mult.}}-AS | 10 | 8 | 3 | 10 | 10 | 12 | 10 | 4 | 8 | 8.4 | 6 |
| ALMult.{}\_{\text{Mult.}}-SAV | 5 | 6 |  | 12 | 3 | 4 | 7 | 5 | 7 | 8.8 | 7 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 3 | 5 | 18 | 8 | 5 | 3 | 6 |  | 7 | 9.5 | 8 |
| AR-GJR-GARCH-skew-tt | 11 | 11 | 9 | 2 | 14 | 10 | 17 | 7 | 8 | 10.1 | 9 |
| AR-ALAR{}\_{\text{AR}}-AS | 4 |  | 4 | 7 | 4 | 6 | 5 |  | 6 | 10.8 | 10 |
| AR-GARCH-skew-tt | 14 | 12 | 8 | 14 | 11 | 14 | 20 | 6 | 8 | 12.4 | 11 |
| QAR-QbSD-gSAV | 19 | 17 | 12 | 13 | 16 | 9 | 11 | 8 | 8 | 13.1 | 12 |
| ALAR{}\_{\text{AR}}-AS | 7 |  | 11 | 19 | 12 | 8 | 8 |  | 6 | 15.1 | 13 |
| AR-ALAR{}\_{\text{AR}}-SAV | 13 | 10 |  | 6 | 7 | 2 |  |  | 5 | 15.2 | 14 |
| QbSD-gSAV | 20 | 18 | 14 | 4 | 15 | 17 | 12 |  | 7 | 16.0 | 15 |
| GJR-GARCH-tt | 17 | 13 | 15 | 11 | 18 | 15 | 14 |  | 7 | 16.4 | 16 |
| GARCH-tt | 15 | 15 | 16 | 15 | 19 | 16 | 13 |  | 7 | 17.1 | 17 |
| AR-GJR-GARCH-tt | 18 | 14 | 10 | 17 | 17 | 19 | 19 |  | 7 | 17.8 | 18 |
| AR-GARCH-tt | 16 | 16 | 13 | 18 | 20 | 18 | 22 |  | 7 | 18.9 | 19 |
| ALAR{}\_{\text{AR}}-SAV | 12 | 9 |  |  | 2 |  | 21 |  | 4 | 19.5 | 20 |
| AR-GAS | 21 |  | 19 |  |  | 21 | 15 |  | 3 | 24.4 | 21 |
| GJR-GARCH-normal |  |  |  |  | 21 | 20 | 16 |  | 3 | 24.6 | 22 |
| GAS | 22 |  | 17 |  |  |  | 18 |  | 3 | 24.6 | 23 |
| AR-GJR-GARCH-normal |  |  |  |  |  |  | 23 |  | 1 | 27.4 | 24 |
| GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 25 |
| EGARCH |  |  |  |  |  |  |  |  | 0 | 28.0 | 26 |
| AR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 27 |
| AR-EGARCH |  |  |  |  |  |  |  |  | 0 | 28.0 | 28 |



Table C5. Ranking of 2.5% VaR and ES forecasting models based on the MCS procedure using AL log scores, rolling window R=250R=250

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 2 | 1 | 2 | 2 | 7 | 1 | 1 | 7 | 8 | 2.9 | 1 |
| QAR-QbSD-gAS | 1 | 6 | 7 | 11 | 1 | 2 | 5 | 1 | 8 | 4.2 | 2 |
| GARCH-skew-tt | 3 | 2 | 1 | 6 |  | 7 | 9 | 4 | 7 | 7.5 | 3 |
| GJR-GARCH-skew-tt | 4 | 3 | 3 | 4 |  | 9 | 10 | 3 | 7 | 8.0 | 4 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 6 |  | 5 | 9 | 6 | 5 | 7 | 2 | 7 | 8.5 | 5 |
| ALMult.{}\_{\text{Mult.}}-AS | 8 | 7 | 6 | 7 | 3 | 4 | 8 |  | 7 | 8.9 | 6 |
| QAR-QbSD-gSAV | 12 | 11 | 12 | 1 |  | 13 | 14 | 8 | 7 | 12.4 | 7 |
| AR-GJR-GARCH-skew-tt | 9 | 8 | 8 | 5 |  | 12 |  | 6 | 6 | 13.0 | 8 |
| AR-GARCH-skew-tt | 11 | 9 | 10 | 10 |  | 11 |  | 5 | 6 | 14.0 | 9 |
| ALAR{}\_{\text{AR}}-AS | 13 | 12 |  |  | 5 | 6 | 2 |  | 5 | 15.2 | 10 |
| AR-ALAR{}\_{\text{AR}}-AS | 21 |  | 4 | 8 |  | 3 | 6 |  | 5 | 15.8 | 11 |
| QbSD-gSAV | 16 | 13 | 16 | 3 |  | 14 | 11 |  | 6 | 16.1 | 12 |
| GJR-GARCH-tt | 18 | 10 | 14 | 13 |  | 8 | 13 |  | 6 | 16.5 | 13 |
| GARCH-tt | 15 | 15 | 13 | 12 |  | 10 | 12 |  | 6 | 16.6 | 14 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 5 | 4 | 9 |  | 4 |  |  |  | 4 | 16.8 | 15 |
| ALMult.{}\_{\text{Mult.}}-SAV | 7 | 5 |  |  | 8 |  | 4 |  | 4 | 17.0 | 16 |
| ALAR{}\_{\text{AR}}-SAV | 14 |  |  |  | 2 |  | 3 |  | 3 | 19.9 | 17 |
| AR-GJR-GARCH-tt | 19 |  | 11 | 14 |  | 16 |  |  | 4 | 21.5 | 18 |
| AR-GARCH-tt | 17 |  | 17 | 15 |  | 17 |  |  | 4 | 22.2 | 19 |
| GJR-GARCH-normal | 20 |  | 15 |  |  | 15 |  |  | 3 | 23.8 | 20 |
| AR-ALAR{}\_{\text{AR}}-SAV | 10 | 14 |  |  |  |  |  |  | 2 | 24.0 | 21 |
| GAS |  |  | 18 |  |  |  |  |  | 1 | 26.8 | 22 |
| AR-GJR-GARCH-normal |  | 19 |  |  |  |  |  |  | 1 | 26.9 | 23 |
| GARCH-normal |  | 20 |  |  |  |  |  |  | 1 | 27.0 | 24 |
| EGARCH |  |  |  |  |  |  |  |  | 0 | 28.0 | 25 |
| AR-GARCH-normal |  |  |  |  |  |  |  |  | 0 | 28.0 | 26 |
| AR-EGARCH |  |  |  |  |  |  |  |  | 0 | 28.0 | 27 |
| AR-GAS |  |  |  |  |  |  |  |  | 0 | 28.0 | 28 |



Table C6. Ranking of 5% VaR and ES forecasting models based on the MCS procedure using AL log scores, rolling window R=250R=250

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | 8 | 2.4 | 1 |
| QAR-QbSD-gAS | 1 | 4 | 6 | 6 | 1 | 5 | 8 | 1 | 8 | 4.0 | 2 |
| ALMult.{}\_{\text{Mult.}}-AS | 5 | 5 | 5 | 8 | 5 | 9 | 5 | 4 | 8 | 5.8 | 3 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 4 |  | 4 | 7 | 6 | 8 | 7 | 3 | 7 | 8.4 | 4 |
| GARCH-skew-tt | 6 | 3 | 2 | 3 |  |  |  | 6 | 5 | 13.0 | 5 |
| GJR-GARCH-skew-tt | 7 | 6 | 3 | 2 |  |  |  | 7 | 5 | 13.6 | 6 |
| ALMult.{}\_{\text{Mult.}}-SAV | 3 | 2 |  |  | 4 | 6 |  |  | 4 | 15.9 | 7 |
| AR-GARCH-skew-tt | 8 | 9 | 9 | 10 |  |  |  | 9 | 5 | 16.1 | 8 |
| AR-ALAR{}\_{\text{AR}}-AS |  |  | 7 |  | 4 | 6 | 2 | 4 | 4 | 16.4 | 9 |
| AR-GJR-GARCH-skew-tt | 10 |  | 8 | 9 |  |  |  | 8 | 4 | 18.4 | 10 |
| ALAR{}\_{\text{AR}}-AS |  |  |  |  | 3 | 4 | 5 | 3 | 4 | 19.0 | 11 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV |  |  |  |  | 3 | 7 | 3 |  | 3 | 19.1 | 12 |
| GARCH-tt | 9 | 10 | 14 | 11 |  |  |  |  | 4 | 19.5 | 13 |
| GJR-GARCH-tt | 16 | 7 | 12 | 12 |  |  |  |  | 4 | 19.9 | 14 |
| GJR-GARCH-normal | 13 | 8 | 13 | 14 |  |  |  |  | 4 | 20.0 | 15 |
| QAR-QbSD-gSAV | 15 |  | 10 | 4 |  |  |  |  | 3 | 21.1 | 16 |
| AR-ALAR{}\_{\text{AR}}-SAV |  |  |  |  | 2 | 2 |  |  | 2 | 21.5 | 17 |
| AR-GJR-GARCH-tt | 12 |  | 11 | 15 |  |  |  |  | 3 | 22.2 | 18 |
| QbSD-gSAV |  |  |  | 5 |  |  |  |  | 1 | 25.1 | 19 |
| AR-GARCH-tt | 11 |  |  |  |  |  |  |  | 1 | 25.9 | 20 |
| GARCH-normal |  |  | 13 |  |  |  |  |  | 1 | 26.1 | 21 |
| AR-GJR-GARCH-normal | 14 |  |  |  |  |  |  |  | 1 | 26.2 | 22 |
| AR-GARCH-normal |  |  | 16 |  |  |  |  |  | 1 | 26.5 | 23 |
| EGARCH |  |  |  |  |  |  |  |  | 0 | 28.0 | 24 |
| AR-EGARCH |  |  |  |  |  |  |  |  | 0 | 28.0 | 25 |
| GAS |  |  |  |  |  |  |  |  | 0 | 28.0 | 26 |
| AR-GAS |  |  |  |  |  |  |  |  | 0 | 28.0 | 27 |
| ALAR{}\_{\text{AR}}-SAV |  |  |  |  |  |  |  |  | 0 | 28.0 | 28 |



Table C7. Ranking of 1% VaR forecasting models using the MCS procedure with quantile scores, rolling window R=2500R=2500

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| AR-ALAR{}\_{\text{AR}}-AS | 1 | 1 | 1 | 9 | 3 | 4 | 6 | 5 | 8 | 3.8 | 1 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 7 | 9 | 6 | 14 | 6 | 6 | 4 | 2 | 8 | 6.8 | 2 |
| ALMult.{}\_{\text{Mult.}}-AS | 18 | 2 | 7 | 17 | 4 | 2 | 3 | 3 | 8 | 7.0 | 3 |
| ALAR{}\_{\text{AR}}-AS | 4 | 8 | 9 | 13 | 2 | 20 | 2 | 4 | 8 | 7.8 | 4 |
| QbSD-gAS |  | 6 | 25 | 1 | 1 | 1 | 1 | 6 | 7 | 8.6 | 5 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 2 | 3 | 3 | 16 | 16 | 18 | 7 | 8 | 8 | 9.1 | 6 |
| GJR-GARCH-skew-tt | 17 | 7 | 11 | 3 | 8 | 8 | 14 | 16 | 8 | 10.5 | 7 |
| ALMult.{}\_{\text{Mult.}}-SAV | 5 | 12 | 4 | 6 | 15 | 21 | 10 | 11 | 8 | 10.5 | 8 |
| AR-ALAR{}\_{\text{AR}}-SAV | 3 | 4 | 2 | 25 | 11 | 17 | 13 | 12 | 8 | 10.9 | 9 |
| AR-GJR-GARCH-skew-tt | 8 | 5 | 15 | 8 | 13 | 10 | 18 | 13 | 8 | 11.2 | 10 |
| GARCH-skew-tt | 13 | 17 | 13 | 7 | 10 | 5 | 15 | 14 | 8 | 11.8 | 11 |
| AR-GARCH-skew-tt | 9 | 10 | 10 | 10 | 14 | 9 | 17 | 15 | 8 | 11.8 | 12 |
| ALAR{}\_{\text{AR}}-SAV | 6 | 11 | 5 | 23 | 12 | 19 | 16 | 10 | 8 | 12.8 | 13 |
| QAR-QbSD-gAS | 26 | 13 |  | 22 | 5 | 3 | 5 | 1 | 7 | 12.9 | 14 |
| GARCH-tt | 11 | 14 | 19 | 2 | 17 | 11 | 8 | 22 | 8 | 13.0 | 15 |
| EGARCH | 19 | 20 | 14 | 5 | 21 | 13 | 20 | 7 | 8 | 14.9 | 16 |
| AR-GJR-GARCH-tt | 10 | 19 | 16 | 24 | 18 | 7 | 12 | 24 | 8 | 16.2 | 17 |
| AR-GARCH-tt | 16 | 18 | 17 | 15 | 20 | 15 | 11 | 23 | 8 | 16.9 | 18 |
| GJR-GARCH-tt | 12 | 15 | 20 | 26 | 19 | 14 | 9 | 21 | 8 | 17.0 | 19 |
| QAR-QbSD-gSAV | 25 | 16 | 21 | 11 | 9 | 16 | 23 | 17 | 8 | 17.2 | 20 |
| QbSD-gSAV |  | 23 | 24 | 4 | 7 | 26 | 22 | 19 | 7 | 19.1 | 21 |
| AR-EGARCH | 21 | 22 | 18 | 12 | 22 | 27 | 27 | 9 | 8 | 19.8 | 22 |
| GAS | 14 | 25 | 12 |  | 27 | 12 | 26 |  | 6 | 21.5 | 23 |
| GJR-GARCH-normal | 22 | 24 | 22 | 19 | 25 | 22 | 19 | 20 | 8 | 21.6 | 24 |
| AR-GAS | 15 | 21 | 8 |  | 23 | 28 | 25 |  | 6 | 22.0 | 25 |
| GARCH-normal | 20 | 26 | 23 | 18 | 24 | 23 | 21 |  | 7 | 22.9 | 26 |
| AR-GJR-GARCH-normal | 24 | 28 | 26 | 21 | 28 | 24 | 28 | 18 | 8 | 24.6 | 27 |
| AR-GARCH-normal | 23 | 27 | 27 | 20 | 26 | 25 | 24 |  | 7 | 25.0 | 28 |



Table C8. Ranking of 2.5% VaR forecasting models using the MCS procedure with quantile scores, rolling window R=2500R=2500

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 8 | 1.6 | 1 |
| ALMult.{}\_{\text{Mult.}}-AS | 3 | 4 | 3 | 6 | 7 | 5 | 1 | 1 | 8 | 3.8 | 2 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 4 | 1 | 7 | 4 | 4 | 4 | 6 | 6 | 8 | 4.5 | 3 |
| ALAR{}\_{\text{AR}}-AS | 2 | 3 | 2 | 15 | 5 | 3 | 4 | 3 | 8 | 4.6 | 4 |
| EGARCH | 6 | 5 | 10 | 1 | 6 | 6 | 3 | 7 | 8 | 5.5 | 5 |
| AR-ALAR{}\_{\text{AR}}-AS | 5 | 22 | 4 | 5 | 3 | 1 | 5 | 4 | 8 | 6.1 | 6 |
| QAR-QbSD-gAS | 7 | 11 | 24 | 7 | 2 | 7 |  | 5 | 7 | 11.4 | 7 |
| GJR-GARCH-normal | 17 | 6 | 15 | 21 | 14 | 14 | 7 | 10 | 8 | 13.0 | 8 |
| AR-EGARCH | 8 | 15 | 19 | 3 | 8 | 23 |  | 8 | 7 | 14.0 | 9 |
| ALMult.{}\_{\text{Mult.}}-SAV | 9 | 7 | 9 | 14 | 17 | 25 | 9 |  | 7 | 14.8 | 10 |
| GARCH-skew-tt | 10 | 16 | 11 | 10 | 11 | 8 |  |  | 6 | 15.2 | 11 |
| GARCH-normal | 13 | 12 | 18 | 20 | 16 | 15 | 8 |  | 7 | 16.2 | 12 |
| GJR-GARCH-skew-tt | 15 | 14 | 12 | 16 | 10 | 9 |  |  | 6 | 16.5 | 13 |
| GARCH-tt | 12 | 9 | 13 | 13 | 15 | 16 |  |  | 6 | 16.8 | 14 |
| ALAR{}\_{\text{AR}}-SAV | 18 | 8 | 8 | 12 | 22 | 26 |  |  | 6 | 18.8 | 15 |
| GJR-GARCH-tt | 14 | 10 | 14 | 18 | 21 | 18 |  |  | 6 | 18.9 | 16 |
| AR-GJR-GARCH-skew-tt | 11 | 17 | 21 | 17 | 20 | 12 |  |  | 6 | 19.2 | 17 |
| AR-GARCH-skew-tt | 23 | 20 | 20 | 11 | 19 | 11 |  |  | 6 | 20.0 | 18 |
| GAS |  | 13 |  | 27 | 9 | 22 |  | 9 | 5 | 20.5 | 19 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 16 | 18 | 5 | 19 | 27 | 24 |  |  | 6 | 20.6 | 20 |
| QbSD-gSAV | 26 | 26 |  | 9 | 12 | 10 |  |  | 5 | 20.9 | 21 |
| QAR-QbSD-gSAV | 25 | 23 | 25 | 8 | 13 | 17 |  |  | 6 | 20.9 | 22 |
| AR-GJR-GARCH-tt | 19 | 24 | 17 | 24 | 18 | 13 |  |  | 6 | 21.4 | 23 |
| AR-ALAR{}\_{\text{AR}}-SAV | 22 | 19 | 6 | 22 | 25 | 27 |  |  | 6 | 22.1 | 24 |
| AR-GJR-GARCH-normal | 20 | 28 | 22 | 26 | 24 | 19 |  | 12 | 7 | 22.4 | 25 |
| AR-GARCH-tt | 24 | 25 | 16 | 23 | 23 | 21 |  |  | 6 | 23.5 | 26 |
| AR-GARCH-normal | 21 | 27 | 23 | 25 | 26 | 20 |  |  | 6 | 24.8 | 27 |
| AR-GAS | 27 | 21 |  |  |  | 28 |  | 11 | 4 | 24.9 | 28 |



Table C9. Ranking of 5% VaR forecasting models using the MCS procedure with quantile scores, rolling window R=2500R=2500

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| EGARCH | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 8 | 1.9 | 1 |
| QbSD-gAS | 1 | 1 | 1 | 3 | 1 | 2 | 3 | 3 | 8 | 1.9 | 2 |
| ALMult.{}\_{\text{Mult.}}-AS | 4 | 4 | 3 | 5 | 5 | 3 | 4 | 6 | 8 | 4.2 | 3 |
| ALAR{}\_{\text{AR}}-AS | 6 | 3 | 15 | 6 | 3 | 5 | 1 | 5 | 8 | 5.5 | 4 |
| QAR-QbSD-gAS | 7 | 7 | 6 | 4 | 6 | 8 | 11 | 1 | 8 | 6.2 | 5 |
| AR-EGARCH | 8 | 6 | 4 | 1 | 11 | 6 | 7 | 8 | 8 | 6.4 | 6 |
| AR-ALAR{}\_{\text{AR}}-AS | 3 | 5 | 26 | 8 | 4 | 4 | 5 | 4 | 8 | 7.4 | 7 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 5 | 8 | 5 | 7 | 21 | 7 | 6 | 7 | 8 | 8.2 | 8 |
| GJR-GARCH-normal | 16 | 12 | 11 |  | 10 | 9 | 14 | 9 | 7 | 13.6 | 9 |
| GARCH-normal | 15 | 14 | 13 |  | 12 | 10 | 15 |  | 6 | 16.9 | 10 |
| GARCH-tt | 18 | 18 | 14 |  | 8 | 15 | 13 |  | 6 | 17.8 | 11 |
| GJR-GARCH-tt | 20 | 19 | 12 |  | 7 | 16 | 12 |  | 6 | 17.8 | 12 |
| GJR-GARCH-skew-tt | 10 | 9 | 7 |  | 13 | 20 |  |  | 5 | 17.9 | 13 |
| AR-GJR-GARCH-normal | 9 | 21 | 17 |  | 25 | 12 | 21 | 11 | 7 | 18.0 | 14 |
| GARCH-skew-tt | 12 | 10 | 9 |  | 14 | 22 | 22 |  | 6 | 18.1 | 15 |
| QbSD-gSAV | 22 | 16 | 20 | 13 | 15 |  | 8 |  | 6 | 18.8 | 16 |
| AR-GJR-GARCH-tt | 17 | 26 | 24 |  | 9 | 14 | 18 |  | 6 | 20.5 | 17 |
| GAS |  |  | 28 | 9 | 28 | 17 | 16 | 10 | 6 | 20.5 | 18 |
| ALAR{}\_{\text{AR}}-SAV | 21 | 17 | 16 | 12 | 23 |  | 17 |  | 6 | 20.2 | 19 |
| AR-GARCH-normal | 13 | 20 | 19 |  | 22 | 13 | 20 |  | 6 | 20.4 | 20 |
| AR-GAS |  | 13 | 27 |  | 17 | 11 | 9 |  | 5 | 20.1 | 21 |
| AR-GJR-GARCH-skew-tt | 11 | 11 | 10 |  | 16 | 19 |  |  | 5 | 18.9 | 22 |
| ALMult.{}\_{\text{Mult.}}-SAV | 26 | 24 | 21 | 10 | 20 |  | 10 |  | 6 | 20.9 | 23 |
| AR-GARCH-tt | 19 | 27 | 22 |  | 18 | 18 | 19 |  | 6 | 22.4 | 24 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 24 | 23 | 18 | 11 | 26 |  | 23 |  | 6 | 22.6 | 25 |
| QAR-QbSD-gSAV | 23 | 22 | 23 |  | 20 |  | 22 |  | 5 | 24.9 | 26 |
| AR-ALAR{}\_{\text{AR}}-SAV | 25 | 25 | 25 |  | 27 |  |  |  | 4 | 26.8 | 27 |



Table C10. Ranking of 1% VaR and ES forecasting models based on the MCS procedure using AL log scores, rolling window R=2500R=2500

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| AR-ALAR{}\_{\text{AR}}-AS | 1 | 6 | 1 | 10 | 1 | 4 | 3 | 5 | 8 | 3.9 | 1 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 6 | 1 | 6 | 12 | 4 | 5 | 2 | 8 | 8 | 5.5 | 2 |
| QbSD-gAS | 15 | 3 | 14 | 4 | 2 | 3 | 4 | 1 | 8 | 5.8 | 3 |
| ALMult.{}\_{\text{Mult.}}-AS | 12 | 2 | 11 | 14 | 3 | 1 | 6 | 4 | 8 | 6.6 | 4 |
| GJR-GARCH-skew-tt | 9 | 7 | 7 | 2 | 5 | 7 | 7 | 16 | 8 | 7.5 | 5 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 2 | 5 | 3 | 15 | 12 | 16 | 9 | 7 | 8 | 8.6 | 6 |
| QAR-QbSD-gAS | 11 | 4 |  | 11 | 11 | 2 | 5 | 3 | 7 | 9.4 | 7 |
| GARCH-skew-tt | 7 | 20 | 8 | 7 | 7 | 6 | 8 | 15 | 8 | 9.8 | 8 |
| ALMult.{}\_{\text{Mult.}}-SAV | 4 | 12 | 4 | 9 | 13 | 18 | 12 | 6 | 8 | 9.8 | 9 |
| ALAR{}\_{\text{AR}}-AS | 13 | 9 |  | 13 | 6 | 14 | 1 | 2 | 7 | 10.8 | 10 |
| AR-GJR-GARCH-skew-tt | 5 | 8 | 12 | 5 | 15 | 10 | 18 | 18 | 8 | 11.4 | 11 |
| AR-ALAR{}\_{\text{AR}}-SAV | 3 | 19 | 2 | 18 | 10 | 20 | 10 | 10 | 8 | 11.5 | 12 |
| AR-GARCH-skew-tt | 10 | 11 | 10 | 8 | 16 | 9 | 16 | 17 | 8 | 12.1 | 13 |
| ALAR{}\_{\text{AR}}-SAV | 8 | 13 | 5 | 20 | 14 | 19 | 11 | 9 | 8 | 12.4 | 14 |
| QAR-QbSD-gSAV | 21 | 10 | 13 | 6 | 9 | 15 | 15 | 13 | 8 | 12.8 | 15 |
| GARCH-tt | 16 | 14 | 15 | 3 | 18 | 11 | 13 | 20 | 8 | 13.8 | 16 |
| QbSD-gSAV | 23 | 21 | 17 | 1 | 8 | 17 | 17 | 11 | 8 | 14.4 | 17 |
| GJR-GARCH-tt | 17 | 15 | 20 | 22 | 19 | 12 | 14 | 19 | 8 | 17.2 | 18 |
| AR-GJR-GARCH-tt | 19 | 16 | 18 | 21 | 17 | 8 | 20 | 21 | 8 | 17.5 | 19 |
| AR-GARCH-tt | 20 | 18 | 19 | 16 | 20 | 13 | 19 | 22 | 8 | 18.4 | 20 |
| AR-GAS | 14 | 17 | 9 |  | 21 |  | 22 |  | 5 | 20.9 | 21 |
| GAS | 18 | 24 | 16 |  | 22 | 21 | 21 |  | 6 | 22.2 | 22 |
| EGARCH | 22 | 22 |  | 17 |  | 22 |  | 12 | 5 | 22.4 | 23 |
| AR-EGARCH |  | 23 |  | 19 |  | 23 |  | 14 | 4 | 23.9 | 24 |
| GJR-GARCH-normal |  |  |  | 24 |  | 24 |  | 23 | 3 | 26.4 | 25 |
| GARCH-normal |  |  |  | 23 |  | 25 |  |  | 2 | 27.0 | 26 |
| AR-GARCH-normal |  |  |  | 25 |  |  |  |  | 1 | 27.6 | 27 |
| AR-GJR-GARCH-normal |  |  |  |  |  |  |  | 26 | 1 | 27.8 | 28 |



Table C11. Ranking of 2.5% VaR and ES forecasting models based on the MCS procedure using AL log scores, rolling window R=2500R=2500

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 1 | 2 | 6 | 1 | 1 | 1 | 4 | 5 | 8 | 2.6 | 1 |
| ALMult.{}\_{\text{Mult.}}-AS | 6 | 3 | 1 | 3 | 6 | 4 | 2 | 2 | 8 | 3.4 | 2 |
| QbSD-gAS | 5 | 1 | 8 | 2 | 3 | 5 | 5 | 1 | 8 | 3.8 | 3 |
| QAR-QbSD-gAS | 3 | 4 | 12 | 5 | 5 | 6 | 6 | 3 | 8 | 5.5 | 4 |
| ALAR{}\_{\text{AR}}-AS | 2 | 5 | 4 | 21 | 4 | 2 | 3 | 6 | 8 | 5.9 | 5 |
| AR-ALAR{}\_{\text{AR}}-AS | 4 | 20 | 9 | 4 | 2 | 3 | 1 | 4 | 8 | 5.9 | 6 |
| GJR-GARCH-skew-tt | 10 | 6 | 11 | 7 | 9 | 8 | 12 |  | 7 | 11.4 | 7 |
| ALMult.{}\_{\text{Mult.}}-SAV | 7 | 7 | 5 | 6 | 13 | 18 | 8 |  | 7 | 11.5 | 8 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 8 | 10 | 3 | 10 | 17 | 16 | 9 |  | 7 | 12.6 | 9 |
| GARCH-skew-tt | 9 | 19 | 10 | 9 | 10 | 7 | 11 |  | 7 | 12.9 | 10 |
| ALAR{}\_{\text{AR}}-SAV | 13 | 12 | 7 | 17 | 8 | 21 | 7 |  | 7 | 14.1 | 11 |
| AR-GJR-GARCH-skew-tt | 11 | 8 | 16 | 14 | 15 | 11 | 14 |  | 7 | 14.6 | 12 |
| AR-GARCH-skew-tt | 18 | 11 | 15 | 12 | 16 | 9 | 15 |  | 7 | 15.5 | 13 |
| AR-ALAR{}\_{\text{AR}}-SAV | 12 | 26 | 2 | 18 | 7 | 22 | 10 |  | 7 | 15.6 | 14 |
| EGARCH | 19 | 9 |  | 11 | 23 | 19 | 13 | 7 | 7 | 16.1 | 15 |
| QAR-QbSD-gSAV | 14 | 16 | 17 | 8 | 12 | 10 |  |  | 6 | 16.6 | 16 |
| GARCH-tt | 15 | 14 | 13 | 16 | 18 | 15 | 16 |  | 7 | 16.9 | 17 |
| GJR-GARCH-tt | 16 | 15 | 14 | 19 | 21 | 17 |  |  | 6 | 19.8 | 18 |
| QbSD-gSAV | 23 | 22 |  | 13 | 14 | 12 | 18 |  | 6 | 19.8 | 19 |
| AR-GJR-GARCH-tt | 17 | 17 | 19 | 22 | 19 | 13 |  |  | 6 | 20.4 | 20 |
| AR-EGARCH | 20 | 13 |  | 15 | 24 | 23 | 17 |  | 6 | 21.0 | 21 |
| AR-GARCH-tt | 21 | 18 | 18 | 20 | 22 | 20 |  |  | 6 | 21.9 | 22 |
| GAS |  | 23 | 20 | 27 | 11 | 14 |  |  | 5 | 22.4 | 23 |
| AR-GAS | 22 | 24 | 21 |  | 20 | 26 |  |  | 5 | 24.6 | 24 |
| GJR-GARCH-normal |  | 21 |  | 24 |  | 24 |  | 23 | 3 | 26.1 | 25 |
| GARCH-normal |  | 25 |  | 23 |  | 25 |  |  | 3 | 26.6 | 26 |
| AR-GARCH-normal |  |  |  | 25 |  |  |  |  | 1 | 27.6 | 27 |
| AR-GJR-GARCH-normal |  |  |  | 26 |  | 27 |  |  | 2 | 27.6 | 28 |



Table C12. Ranking of 5% VaR and ES forecasting models based on the MCS procedure using AL log scores, rolling window R=2500R=2500

|  | S&P | DJIA | NASDAQ | STOXX | FTSE | DAX | CAC | TSX | # | Avg. | Final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rank | rank |
| QbSD-gAS | 2 | 2 | 2 | 1 | 1 | 5 | 3 | 2 | 8 | 2.2 | 1 |
| ALMult.{}\_{\text{Mult.}}-AS | 3 | 1 | 1 | 4 | 4 | 1 | 4 | 4 | 8 | 2.8 | 2 |
| ALAR{}\_{\text{AR}}-AS | 5 | 8 | 14 | 8 | 3 | 3 | 1 | 3 | 8 | 5.6 | 3 |
| QAR-QbSD-gAS | 4 | 3 | 20 | 2 | 6 | 6 | 5 | 1 | 8 | 5.9 | 4 |
| AR-ALAR{}\_{\text{AR}}-AS | 11 | 7 | 5 | 20 | 2 | 4 | 2 | 6 | 8 | 7.1 | 5 |
| AR-ALMult.{}\_{\text{Mult.}}-AS | 1 | 6 | 8 | 5 | 5 | 2 |  | 5 | 7 | 7.5 | 6 |
| EGARCH | 9 | 4 | 22 | 6 | 8 | 7 |  | 7 | 7 | 11.4 | 7 |
| AR-EGARCH | 12 | 5 | 25 | 3 | 11 | 8 |  | 8 | 7 | 12.5 | 8 |
| GJR-GARCH-skew-tt | 7 | 9 | 3 | 12 | 16 | 13 |  |  | 6 | 14.5 | 9 |
| GARCH-skew-tt | 8 | 11 | 4 | 9 | 17 | 15 |  |  | 6 | 15.0 | 10 |
| AR-GJR-GARCH-skew-tt | 6 | 10 | 10 | 16 | 18 | 11 |  |  | 6 | 15.9 | 11 |
| GARCH-tt | 10 | 13 | 16 | 10 | 15 | 12 |  |  | 6 | 16.5 | 12 |
| QAR-QbSD-gSAV | 15 | 12 | 11 | 7 | 12 | 22 |  |  | 6 | 16.9 | 13 |
| AR-GARCH-skew-tt | 17 | 14 | 7 | 14 | 19 | 16 |  |  | 6 | 17.9 | 14 |
| GJR-GARCH-tt | 13 | 15 | 17 | 18 | 13 | 14 |  |  | 6 | 18.2 | 15 |
| AR-GJR-GARCH-tt | 14 | 18 | 24 | 21 | 14 | 10 |  |  | 6 | 19.6 | 16 |
| AR-ALMult.{}\_{\text{Mult.}}-SAV | 18 | 20 | 6 | 13 | 24 | 24 |  |  | 6 | 20.1 | 17 |
| ALAR{}\_{\text{AR}}-SAV | 20 | 17 | 12 | 22 | 9 |  |  |  | 5 | 20.5 | 18 |
| AR-ALAR{}\_{\text{AR}}-SAV | 21 | 23 | 9 | 19 | 10 |  |  |  | 5 | 20.8 | 19 |
| AR-GARCH-tt | 16 | 19 | 23 | 17 | 21 | 17 |  |  | 6 | 21.1 | 20 |
| ALMult.{}\_{\text{Mult.}}-SAV | 19 | 16 | 13 | 15 | 22 |  |  |  | 5 | 21.1 | 21 |
| QbSD-gSAV | 22 | 21 | 21 | 11 | 20 | 23 |  |  | 6 | 21.8 | 22 |
| GAS |  |  | 15 |  | 23 | 9 |  |  | 3 | 23.4 | 23 |
| GJR-GARCH-normal | 25 | 22 | 19 | 23 | 25 | 18 |  |  | 6 | 23.5 | 24 |
| AR-GAS |  | 25 | 18 |  | 7 |  |  |  | 3 | 23.8 | 25 |
| GARCH-normal | 23 | 24 |  | 24 |  | 19 |  |  | 4 | 25.2 | 26 |
| AR-GJR-GARCH-normal | 24 | 26 |  | 26 |  | 20 |  |  | 4 | 26.0 | 27 |
| AR-GARCH-normal | 26 | 27 |  | 25 |  | 21 |  |  | 4 | 26.4 | 28 |

BETA