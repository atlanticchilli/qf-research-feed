---
authors:
- Akash Deep
- Svetlozar T. Rachev
- Frank J. Fabozzi
doc_id: arxiv:2511.16563v1
family_id: arxiv:2511.16563
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral
  Asset Pricing'
url_abs: http://arxiv.org/abs/2511.16563v1
url_html: https://arxiv.org/html/2511.16563v1
venue: arXiv q-fin
version: 1
year: 2025
---


Akash Deep
Department of Mathematics and Statistics, Texas Tech University, Lubbock, TX, USA
Corresponding author: akash.deep@ttu.edu

Svetlozar T. Rachev
Department of Mathematics and Statistics, Texas Tech University, Lubbock, TX, USA

Frank J. Fabozzi
Carey Business School, Johns Hopkins University, Baltimore, MD, USA

(2025)

###### Abstract

We develop an econometric framework integrating heavy-tailed Student’s tt distributions with behavioral probability weighting while preserving infinite divisibility. Using 432,752 observations across 86 assets (2004–2024), we demonstrate Student’s tt specifications outperform Gaussian models in 88.4% of cases. Bounded probability-weighting transformations preserve mathematical properties required for dynamic pricing. Gaussian models underestimate 99% Value-at-Risk by 19.7% versus 3.2% for our specification. Joint estimation procedures identify tail and behavioral parameters with established asymptotic properties. Results provide robust inference for asset-pricing applications where heavy tails and behavioral distortions coexist.

Keywords: Behavioral Finance, Heavy-Tailed Distributions, Student’s tt Distribution, Probability Weighting, Econometric Estimation, Infinite Divisibility

## 1 Introduction

Financial return series exhibit heavy tails that systematically reject Gaussian assumptions, as first documented by [mandelbrot1963variation] and [fama1965behavior] and confirmed in subsequent econometric studies. While Student’s tt and related specifications provide better empirical fit, their integration with behavioral asset-pricing models has been limited because behavioral distortions such as probability weighting often violate conditions required for arbitrage-free pricing and continuous-time econometric analysis.

We contribute to this literature by developing an econometric framework that jointly models heavy-tailed returns and behavioral probability weighting while preserving infinite divisibility and compatibility with the Fundamental Theorem of Asset Pricing. We establish sufficient conditions under which bounded probability-weighting transformations of Student’s tt processes retain infinite divisibility, and we propose estimation procedures that allow joint identification of tail and distortion parameters, along with results on their asymptotic properties.

Empirical analysis on 432,752 daily observations across 86 assets (2004–2024) confirms the econometric relevance of our framework. Gaussian assumptions are universally rejected, and Student’s tt distributions dominate Laplace and normal alternatives in 88.4% of cases. Moreover, misspecification has substantial consequences: Gaussian models underestimate 99% Value-at-Risk by 19.7% on average, while our specification reduces errors below 3.2%.

The remainder of the paper is organized as follows. Section 2 reviews related econometric literature on heavy-tailed modeling and behavioral adjustments. Section 3 presents the theoretical framework, including conditions under which probability-weighting transformations preserve infinite divisibility. Section 4 describes the estimation and testing procedures and establishes their asymptotic properties. Section 5 reports the empirical results from model comparisons, risk backtests, and robustness checks. Section 6 discusses implications for econometric modeling and asset-pricing applications, and Section 7 concludes.

## 2 Related Econometric Literature

The econometric evidence against Gaussian return assumptions is longstanding. [mandelbrot1963variation] and [fama1965behavior] first documented leptokurtosis and excess tail probability in financial returns, findings that continue to be confirmed in high-frequency data [andersen2003modeling]. Parametric alternatives emerged through variance-mixture models [praetz1972distribution, blattberg2010comparison] and Student’s tt specifications, while subsequent work formalized their infinite-divisibility properties [kelker1971infinite, grosswald1976student]. These contributions provided the theoretical basis for integrating heavy-tailed distributions into continuous-time econometric models.

Heavy tails have also been linked to stochastic volatility and jump processes. [merton1976option] jump-diffusion model and [heston1993closed] stochastic volatility framework demonstrated how non-Gaussian features arise naturally in dynamic asset-pricing settings. Extensions based on Lévy processes [barndorff1997normal, eberlein1995hyperbolic, cont2003financial, schoutens2003levy] established rigorous econometric tools for modeling discontinuities and volatility clustering while maintaining arbitrage-free pricing. Recent econometric advances include time-change methods [carr2004time], realized-volatility approaches [andersen2003modeling], and jump detection tests [ait2009testing], all of which reinforce the empirical necessity of heavy-tailed specifications.

Another strand of literature emphasizes econometric testing and model comparison. [bollerslev1986generalized] GARCH model, and later EGARCH [nelson1991conditional], demonstrated how conditional heteroskedasticity generates unconditional heavy tails. [hansen2005forecast] conducted large-scale forecast comparisons, showing that models with heavy-tailed innovations systematically outperform Gaussian specifications. Extreme Value Theory methods [mcneil2000estimation] and flexible parametric distributions such as the Skewed Generalized T [bali2007conditional] have been widely employed for tail risk measurement and regulatory capital estimation.

Behavioral finance introduces additional econometric challenges. Prospect theory [kahneman2013prospect, tversky1992advances] and cumulative probability weighting imply nonlinear distortions of return distributions. While these models capture empirically observed biases, their lack of infinite divisibility often renders them inconsistent with dynamic pricing frameworks. Recent work [shirvani2021option] has shown how bounded modifications of probability weighting can be embedded in rational dynamic asset pricing models while preserving arbitrage-free conditions.

The literature just reviewed establishes three points critical to our contribution: (1) heavy tails are an econometric regularity of financial data; (2) mathematically consistent heavy-tail models exist but are rarely integrated with behavioral distortions; and (3) econometric procedures for jointly estimating tail and behavioral parameters remain underdeveloped. Our paper addresses this gap by introducing a Student’s tt-based behavioral framework that preserves infinite divisibility, provides tractable likelihood-based estimation, and improves statistical inference for risk measurement and pricing applications.

## 3 Theoretical Framework

A central requirement of econometric models in dynamic asset pricing is infinite divisibility, which ensures temporal consistency and compatibility with arbitrage-free pricing. If a return distribution is infinitely divisible, the joint distribution of returns across subperiods can be represented consistently for any partition of the time horizon.

###### Definition 1 (Infinite Divisibility).

A random variable XX is infinitely divisible if for every positive integer nn, there exist independent and identically distributed random variables X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} such that X​=𝑑​X1+X2+⋯+XnX\overset{d}{=}X\_{1}+X\_{2}+\cdots+X\_{n}.

While Gaussian and stable laws satisfy infinite divisibility, they fail to capture empirically observed return behavior. Student’s tt distributions, by contrast, are both empirically superior and mathematically admissible.

###### Theorem 1 (Student’s tt Infinite Divisibility).

All Student’s tt distributions with degrees of freedom parameter ν>0\nu>0 are infinitely divisible [grosswald1976student].

The Student’s tt distribution with location μ\mu, scale σ\sigma, and degrees of freedom ν\nu has density:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x;ν,μ,σ)=Γ​(ν+12)Γ​(ν2)​ν​π​σ​(1+(x−μ)2ν​σ2)−ν+12f(x;\nu,\mu,\sigma)=\frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)\sqrt{\nu\pi}\sigma}\left(1+\frac{(x-\mu)^{2}}{\nu\sigma^{2}}\right)^{-\frac{\nu+1}{2}} |  | (1) |

We extend this framework by introducing a behavioral adjustment operator that preserves infinite divisibility. Let Ft​(x)F\_{t}(x) denote the cumulative distribution function of a Student’s tt random variable and w:[0,1]→[0,1]w:[0,1]\to[0,1] be a probability weighting function. We define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬw​[x]=x⋅(1+θ⋅tanh⁡(β⋅(w​(Ft​(x))Ft​(x)−1)))\mathcal{B}\_{w}[x]=x\cdot\left(1+\theta\cdot\tanh\left(\beta\cdot\left(\frac{w(F\_{t}(x))}{F\_{t}(x)}-1\right)\right)\right) |  | (2) |

where θ∈[0,0.3]\theta\in[0,0.3] controls adjustment magnitude and β>0\beta>0 determines sensitivity.

###### Theorem 2 (Preservation of Infinite Divisibility).

Let XX be an infinitely divisible Student’s tt random variable and ℬw\mathcal{B}\_{w} be the behavioral adjustment operator defined in equation (2). If the probability weighting function ww is Lipschitz continuous and θ≤0.3\theta\leq 0.3, then Y=ℬw​[X]Y=\mathcal{B}\_{w}[X] remains infinitely divisible.

This result ensures compatibility with the Fundamental Theorem of Asset Pricing and preserves tractability for likelihood-based estimation.

## 4 Estimation and Asymptotic Properties

### 4.1 Model Setup

Let RtR\_{t} denote asset returns at time tt. We assume

|  |  |  |
| --- | --- | --- |
|  | Rt∼tν​(μ,σ),R\_{t}\sim t\_{\nu}(\mu,\sigma), |  |

a Student’s tt distribution with location parameter μ\mu, scale parameter σ\sigma, and degrees of freedom ν>2\nu>2, ensuring finite variance. To capture behavioral distortions, we introduce a probability weighting operator w​(p;α)w(p;\alpha), parameterized by α∈(0,1)\alpha\in(0,1), following Prelec (1998). The behavioral-adjusted return distribution is defined by its cumulative distribution function (CDF):

|  |  |  |
| --- | --- | --- |
|  | Fb​w​(r;θ)=w​(Ft​(r;ν,μ,σ);α),F\_{bw}(r;\theta)=w(F\_{t}(r;\nu,\mu,\sigma);\alpha), |  |

where θ=(μ,σ,ν,α)\theta=(\mu,\sigma,\nu,\alpha).

Our objective is to estimate θ\theta consistently and establish asymptotic normality of the estimators.

### 4.2 Likelihood-Based Estimation

For a sample {R1,…,RT}\{R\_{1},\ldots,R\_{T}\}, the log-likelihood under the behavioral-adjusted Student’s tt distribution is

|  |  |  |
| --- | --- | --- |
|  | ℓT​(θ)=∑t=1Tlog⁡fb​w​(Rt;θ),\ell\_{T}(\theta)=\sum\_{t=1}^{T}\log f\_{bw}(R\_{t};\theta), |  |

where fb​w​(⋅;θ)f\_{bw}(\cdot;\theta) is the density implied by the weighted CDF transformation. Direct evaluation requires numerical integration; however, under Lipschitz continuity of w​(⋅;α)w(\cdot;\alpha), the transformation preserves smoothness and ensures that the likelihood is well-defined.

The maximum likelihood estimator (MLE) is given by

|  |  |  |
| --- | --- | --- |
|  | θ^T=arg⁡maxθ∈Θ⁡ℓT​(θ),\hat{\theta}\_{T}=\arg\max\_{\theta\in\Theta}\ell\_{T}(\theta), |  |

with parameter space Θ={(μ,σ,ν,α):σ>0,ν>2,α∈(0,1)}\Theta=\{(\mu,\sigma,\nu,\alpha):\sigma>0,\nu>2,\alpha\in(0,1)\}.

### 4.3 Identification

Identification of ν\nu and α\alpha requires that behavioral weighting and tail thickness affect distinct features of the distribution. The tail index is determined by ν\nu, while α\alpha alters cumulative probabilities without changing the polynomial rate of decay. Formally, if two parameter vectors θ1\theta\_{1} and θ2\theta\_{2} generate the same distribution, then both the tail index and the distortion function must coincide, ensuring point identification.

### 4.4 Asymptotic Properties

Under standard regularity conditions for MLE (compactness of Θ\Theta, Lipschitz continuity of ww, and integrability of log-likelihood derivatives), we obtain the following result:

###### Theorem 3 (Consistency and Asymptotic Normality).

Let {Rt}\{R\_{t}\} be i.i.d. returns generated from the behavioral Student’s tt model. Then:

1. 1.

   θ^T→𝑝θ0\hat{\theta}\_{T}\xrightarrow{p}\theta\_{0}, the true parameter vector.
2. 2.

   T​(θ^T−θ0)→𝑑N​(0,I​(θ0)−1)\sqrt{T}(\hat{\theta}\_{T}-\theta\_{0})\xrightarrow{d}N(0,I(\theta\_{0})^{-1}),

where I​(θ0)=𝔼​[−∇2ℓT​(θ0)]I(\theta\_{0})=\mathbb{E}[-\nabla^{2}\ell\_{T}(\theta\_{0})] is the Fisher information matrix.

The proof follows from standard M-estimation theory and is provided in Appendix A.

### 4.5 Hypothesis Testing

We consider two hypothesis tests:

* •

  Tail thickness: H0:ν=∞H\_{0}:\nu=\infty (Gaussian) versus H1:ν<∞H\_{1}:\nu<\infty. A likelihood ratio test provides a formal econometric test of Gaussian assumptions.
* •

  Behavioral distortion: H0:α=1H\_{0}:\alpha=1 (no weighting) versus H1:α∈(0,1)H\_{1}:\alpha\in(0,1). Wald or likelihood ratio tests evaluate the significance of behavioral distortions.

Both tests can be implemented with standard asymptotics, using critical values from the χ2\chi^{2} distribution. Joint testing of (ν,α)(\nu,\alpha) allows assessment of whether heavy tails and behavioral weighting both contribute significantly beyond Gaussian benchmarks.

## 5 Empirical Results

### 5.1 Data

Our dataset comprises 432,752 daily observations from 86 assets across 25 categories spanning January 2004 to December 2024. Asset categories include US equities (large-, mid-, small-cap), international developed and emerging markets, fixed income (treasury, corporate, municipal bonds), commodities, and sector-specific exposures. Figure [1](https://arxiv.org/html/2511.16563v1#S5.F1 "Figure 1 ‣ 5.1 Data ‣ 5 Empirical Results ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing") presents our systematic research methodology.

![Refer to caption](Fig/flowchart.png)


Figure 1: Research Methodology Framework

### 5.2 Model Selection and Distributional Fit

Table [1](https://arxiv.org/html/2511.16563v1#S5.T1 "Table 1 ‣ 5.2 Model Selection and Distributional Fit ‣ 5 Empirical Results ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing") presents comprehensive summary statistics across representative asset categories, revealing systematic departures from normal distribution assumptions.

Table 1: Descriptive Statistics by Asset Category

| Asset | Category | Obs | Mean | Std Dev | Skew | Kurt | Min | Max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | US Large Cap | 5,252 | 0.0006 | 0.0121 | −0.37-0.37 | 5.68 | −0.095-0.095 | 0.110 |
| VTI | US Large Cap | 4,775 | 0.0007 | 0.0121 | −0.37-0.37 | 5.61 | −0.095-0.095 | 0.110 |
| IVV | US Large Cap | 5,252 | 0.0006 | 0.0121 | −0.37-0.37 | 5.68 | −0.095-0.095 | 0.110 |
| IJH | US Mid Cap | 5,252 | 0.0008 | 0.0146 | −0.42-0.42 | 6.71 | −0.132-0.132 | 0.128 |
| MDY | US Mid Cap | 5,673 | 0.0007 | 0.0145 | −0.44-0.44 | 7.24 | −0.132-0.132 | 0.128 |
| VO | US Mid Cap | 4,775 | 0.0008 | 0.0146 | −0.42-0.42 | 6.69 | −0.132-0.132 | 0.128 |
| VTEB | Muni Bonds | 2,799 | 0.0002 | 0.0029 | 0.024 | 4.22 | −0.024-0.024 | 0.019 |
| MUB | Muni Bonds | 4,145 | 0.0002 | 0.0030 | 0.069 | 4.14 | −0.024-0.024 | 0.022 |

Figure [2](https://arxiv.org/html/2511.16563v1#S5.F2 "Figure 2 ‣ 5.2 Model Selection and Distributional Fit ‣ 5 Empirical Results ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing") illustrates systematic departures from normality across our comprehensive dataset.

![Refer to caption](Fig/figure1_empirical_evidence.png)


Figure 2: Empirical Evidence Against Normality Assumptions. Panel A shows Q-Q plots comparing empirical quantiles to Normal distribution for representative assets. Panel B displays histogram overlays with fitted Normal (dashed) and Student’s tt (solid) densities. Panel C presents tail probability comparisons on log scale, demonstrating substantial differences between empirical data and Normal assumptions.

Gaussian assumptions are rejected at the 5% significance level for 100% of assets using Shapiro–Wilk, Jarque–Bera, Anderson–Darling, and Kolmogorov–Smirnov tests. Table [2](https://arxiv.org/html/2511.16563v1#S5.T2 "Table 2 ‣ 5.2 Model Selection and Distributional Fit ‣ 5 Empirical Results ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing") summarizes likelihood-based comparisons.

Table 2: Distribution Model Performance Comparison

| Distribution | Avg AIC | Best Model Count | Best Model % |
| --- | --- | --- | --- |
| Normal | −26,250.4-26{,}250.4 | 0 | 0.0% |
| Student’s tt | −27,815.8-27{,}815.8 | 76 | 88.4% |
| Laplace | −27,284.1-27{,}284.1 | 10 | 11.6% |

Student’s tt distributions provide the best fit in 88.4% of cases based on AIC, with an average improvement of 1,565 points over Gaussian benchmarks.

### 5.3 Parameter Estimates

Estimated degrees of freedom cluster between 4 and 7 for equity indices, reflecting pronounced tail risk, while bond exposures exhibit higher values (8–12). For the behavioral specification, estimated weighting parameters α^\hat{\alpha} average 0.78, with Wald tests rejecting H0:α=1H\_{0}:\alpha=1 in 72% of cases.

Figure [3](https://arxiv.org/html/2511.16563v1#S5.F3 "Figure 3 ‣ 5.3 Parameter Estimates ‣ 5 Empirical Results ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing") presents comprehensive model performance comparisons across asset classes.

![Refer to caption](Fig/figure2_model_performance.png)


Figure 3: Model Performance Comparison Across Asset Classes. The figure displays log-likelihood improvements of Student’s tt relative to Normal specifications across different asset categories. Box plots show distribution of improvements within each category. All asset classes exhibit substantial improvements, with equity indices showing largest gains.

### 5.4 Tail Risk Measurement

Under Gaussian assumptions, 99% VaR is underestimated by 19.7% on average, with particularly severe errors in emerging markets (24.3%) and commodities (22.1%). The behavioral Student’s tt specification reduces average errors to below 3.2%. Backtesting procedures [kupiec1995techniques, christoffersen1998evaluating] confirm that exceedance rates under our specification are statistically indistinguishable from nominal levels.

Table [3](https://arxiv.org/html/2511.16563v1#S5.T3 "Table 3 ‣ 5.4 Tail Risk Measurement ‣ 5 Empirical Results ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing") summarizes Value-at-Risk estimation errors across models and asset classes.

Table 3: Value-at-Risk Estimation Performance

|  | Normal Model | | | Behavioral Student’s tt | | |
| --- | --- | --- | --- | --- | --- | --- |
| Asset Class | Avg Err | Max Err | Viol | Avg Err | Max Err | Viol |
| US Equities | 18.3% | 31.2% | 1.8% | 2.9% | 5.1% | 1.1% |
| International Eq | 19.8% | 28.7% | 2.1% | 3.1% | 5.8% | 1.0% |
| Emerging Mkts | 24.3% | 39.4% | 2.7% | 3.4% | 6.2% | 1.2% |
| Corp Bonds | 16.2% | 22.1% | 1.5% | 2.8% | 4.9% | 0.9% |
| Commodities | 22.1% | 35.6% | 2.4% | 3.5% | 6.7% | 1.1% |
| Overall Avg | 19.7% | 31.4% | 2.1% | 3.2% | 5.7% | 1.1% |

### 5.5 Out-of-Sample Forecasting

Rolling-window forecasts using a 1,000-day estimation window show that the behavioral Student’s tt specification significantly outperforms Gaussian and Laplace benchmarks in 81% of cases based on Diebold–Mariano tests. Parameter stability checks indicate lower degrees of freedom and stronger probability weighting during crisis periods.

### 5.6 Robustness

Results are robust to: (1) alternative weighting functions [gonzalez1999shape], (2) subperiod analyses (pre-2008, post-2008, COVID-19), and (3) block bootstrap inference accounting for serial dependence.

## 6 Implications and Discussion

### 6.1 Consequences of Gaussian Misspecification

Our results confirm universal rejection of Gaussian assumptions with economically large consequences. The 19.7% average underestimation of tail risk highlights the danger of relying on Gaussian models for risk measurement, pricing, and regulatory capital calculations. This misspecification propagates into biased inference and unstable parameter estimates.

### 6.2 Econometric Value of Student’s tt Specification

The Student’s tt distribution provides a parsimonious yet flexible framework for heavy-tailed modeling. Its infinite divisibility ensures compatibility with continuous-time theory, while the degrees-of-freedom parameter offers direct control over tail behavior. The empirical dominance across diverse asset classes suggests it should serve as a baseline model for heavy-tailed inference in financial econometrics.

### 6.3 Behavioral Adjustments and Identification

Behavioral weighting parameters are statistically significant even after controlling for heavy tails, indicating that probability distortions represent a distinct phenomenon. Our framework demonstrates that behavioral features can be incorporated without sacrificing mathematical consistency, provided adjustments are properly bounded.

### 6.4 Broader Econometric Applications

The framework opens new directions including diagnostic tests for behavioral distortions, extensions to multivariate settings where heavy tails and probability weighting interact with dependence structures, and applications to high-frequency data where properties may vary dynamically.

## 7 Conclusion

This paper develops an econometric framework integrating heavy-tailed Student’s tt distributions with behavioral probability weighting while preserving infinite divisibility. We establish that bounded weighting transformations maintain the mathematical properties required for continuous-time modeling and derive likelihood-based estimation procedures with established asymptotic properties.

Empirical analysis using 432,752 observations across 86 assets demonstrates the framework’s relevance. Gaussian models are universally rejected, Student’s tt specifications dominate in 88.4% of cases, and behavioral parameters are statistically significant in 72% of assets. Gaussian misspecification leads to 19.7% underestimation of tail risk, while our specification reduces errors below 3.2%.

Future research may extend the framework to multivariate settings, time-varying parameters, and high-frequency applications where heavy tails and behavioral distortions evolve dynamically.

## Funding

No funding was received for this work.

## Data Availability

Replication materials are available at <https://github.com/akashdeepo/Heavy-Tailed-Distributions-in-Behavioral-Asset-Pricing>. The repository includes complete Jupyter notebooks, documentation, and instructions to reproduce all analyses. The implementation uses Python 3.12.11 with standard statistical libraries and can be executed on standard hardware within 2–3 hours.

## Competing Interests

No competing interest is declared.

## Author Contributions

A.D., S.T.R., and F.J.F. conceived the research framework. A.D. conducted the empirical analysis and wrote the initial manuscript. All authors contributed to the theoretical development, reviewed and edited the manuscript, and approved the final version.

## Acknowledgments

The authors thank the anonymous reviewers for their valuable suggestions.

## Appendix A Proof of Theorem [2](https://arxiv.org/html/2511.16563v1#Thmtheorem2 "Theorem 2 (Preservation of Infinite Divisibility). ‣ 3 Theoretical Framework ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing"): Preservation of Infinite Divisibility

###### Proof.

Let X∼t​(ν,μ,σ)X\sim t(\nu,\mu,\sigma) with characteristic function ϕX​(u)\phi\_{X}(u). We show that Y=ℬw​[X]Y=\mathcal{B}\_{w}[X] maintains infinite divisibility under the stated conditions.

Step 1: Boundedness Analysis.
Since tanh⁡(z)∈(−1,1)\tanh(z)\in(-1,1) for all z∈ℝz\in\mathbb{R} and θ≤0.3\theta\leq 0.3, the adjustment factor satisfies:

|  |  |  |
| --- | --- | --- |
|  | 1+θ⋅tanh⁡(β⋅(w​(Ft​(x))Ft​(x)−1))∈[0.7,1.3]1+\theta\cdot\tanh\left(\beta\cdot\left(\frac{w(F\_{t}(x))}{F\_{t}(x)}-1\right)\right)\in[0.7,1.3] |  |

Step 2: Lipschitz Continuity.
For probability weighting functions satisfying |w′​(p)|≤L|w^{\prime}(p)|\leq L for some constant L>0L>0, the behavioral adjustment operator is Lipschitz continuous. Let ft​(⋅)f\_{t}(\cdot) denote the density of the Student’s tt distribution. Then:

|  |  |  |
| --- | --- | --- |
|  | |dd​x​(w​(Ft​(x))Ft​(x))|≤L⋅ft​(x)Ft​(x)+w​(Ft​(x))⋅ft​(x)Ft​(x)2≤C\left|\frac{d}{dx}\left(\frac{w(F\_{t}(x))}{F\_{t}(x)}\right)\right|\leq\frac{L\cdot f\_{t}(x)}{F\_{t}(x)}+\frac{w(F\_{t}(x))\cdot f\_{t}(x)}{F\_{t}(x)^{2}}\leq C |  |

for some constant C>0C>0.

Step 3: Characteristic Function Analysis.
The characteristic function of YY can be written as:

|  |  |  |
| --- | --- | --- |
|  | ϕY​(u)=𝔼​[exp⁡(i​u⋅ℬw​[X])]\phi\_{Y}(u)=\mathbb{E}[\exp(iu\cdot\mathcal{B}\_{w}[X])] |  |

Since ℬw\mathcal{B}\_{w} is a bounded Lipschitz transformation, the characteristic function ϕY​(u)\phi\_{Y}(u) inherits the infinite divisibility structure from ϕX​(u)\phi\_{X}(u).

Step 4: Lévy Measure Preservation.
Under the transformation Y=ℬw​[X]Y=\mathcal{B}\_{w}[X], the Lévy measure νY\nu\_{Y} of YY is related to the Lévy measure νX\nu\_{X} of XX through:

|  |  |  |
| --- | --- | --- |
|  | νY​(B)=νX​(ℬw−1​(B))\nu\_{Y}(B)=\nu\_{X}(\mathcal{B}\_{w}^{-1}(B)) |  |

for Borel sets BB. The boundedness ensures the transformed measure satisfies the integrability condition, preserving infinite divisibility.
∎

## Appendix B Proof of Theorem [3](https://arxiv.org/html/2511.16563v1#Thmtheorem3 "Theorem 3 (Consistency and Asymptotic Normality). ‣ 4.4 Asymptotic Properties ‣ 4 Estimation and Asymptotic Properties ‣ Probability Weighting Meets Heavy Tails: An Econometric Framework for Behavioral Asset Pricing"): Consistency and Asymptotic Normality

###### Proof.

The proof follows from standard M-estimation theory.

Consistency: Under compactness of Ψ\Psi, continuity of fbehavf\_{\text{behav}} in 𝝍\boldsymbol{\psi}, and identifiability conditions, the MLE is consistent by standard arguments.

Asymptotic Normality: The score function satisfies:

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1Ts​(rt;𝝍0)→𝑑N​(0,I​(𝝍0))\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}s(r\_{t};\boldsymbol{\psi}\_{0})\xrightarrow{d}N(0,I(\boldsymbol{\psi}\_{0})) |  |

where s​(rt;𝝍)=∇𝝍ln⁡fbehav​(rt;𝝍)s(r\_{t};\boldsymbol{\psi})=\nabla\_{\boldsymbol{\psi}}\ln f\_{\text{behav}}(r\_{t};\boldsymbol{\psi}) and I​(𝝍0)I(\boldsymbol{\psi}\_{0}) is the Fisher information matrix.
∎