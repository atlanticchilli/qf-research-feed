---
authors:
- Aditri
doc_id: arxiv:2601.09927v1
family_id: arxiv:2601.09927
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Efficiency versus Robustness under Tail Misspecification: Importance Sampling
  and Moment-Based VaR Bracketing'
url_abs: http://arxiv.org/abs/2601.09927v1
url_html: https://arxiv.org/html/2601.09927v1
venue: arXiv q-fin
version: 1
year: 2026
---


Aditri
  
Rutgers Business School
  
aditri.aditri@rutgers.edu

###### Abstract

Value-at-Risk (VaR) estimation at high confidence levels is inherently a rare-event problem and is particularly sensitive to tail behavior and model misspecification. This paper studies the performance of two simulation-based VaR estimation approaches, importance sampling (IS) and discrete moment matching (DMM), under controlled tail misspecification. The analysis separates the nominal model used for estimator construction from the true data-generating process used for evaluation, allowing the effects of heavy-tailed returns to be examined in a transparent and reproducible setting.

Daily returns of a broad equity market proxy are used to calibrate a nominal Gaussian model, while the true returns are generated from Student-tt distributions with varying degrees of freedom to represent increasingly heavy tails. Importance sampling is implemented via exponential tilting of the Gaussian model and VaR is estimated through likelihood-weighted root-finding. Discrete moment matching constructs deterministic lower and upper VaR bounds by enforcing a finite number of moment constraints on a discretized loss distribution.

The results demonstrate a clear trade-off between efficiency and robustness. Importance sampling produces low-variance VaR estimates under the nominal model but systematically underestimates the true VaR under heavy-tailed returns, with bias increasing at higher confidence levels and for thicker tails. Stability diagnostics such as effective sample size and weight concentration deteriorate as the estimation problem becomes more extreme. In contrast, DMM yields conservative VaR bracketing that remains robust under tail misspecification, with bounds tightening as additional moments are enforced up to a numerically feasible limit.

These findings highlight that variance reduction alone is insufficient for reliable tail risk estimation when model uncertainty is significant. Moment-based approaches provide a complementary framework by explicitly accounting for distributional ambiguity, offering robustness at the expense of efficiency. The paper provides practical diagnostic guidance for assessing the reliability of simulation-based VaR estimators under heavy-tailed market conditions.

Keywords: Value-at-Risk, Importance Sampling, Discrete Moment Matching,
Monte Carlo Simulation, Tail Risk, Model Misspecification

## 1 Introduction

Value-at-Risk (VaR) is one of the most widely used risk measures in financial risk management,
serving as both a regulatory benchmark and a practical tool for quantifying potential losses over
fixed horizons. At high confidence levels such as 99%99\% and above, VaR estimation becomes an
inherently rare-event problem: the target quantile is determined by extreme tail probabilities of
the loss distribution. From a computational standpoint, standard Monte Carlo methods can be
inefficient in this regime because only a small fraction of simulated samples fall into the relevant
tail region and therefore contribute meaningfully to the estimate.

Two broad methodological responses to this challenge motivate the present study.
The first focuses on *computational efficiency* through variance-reduction techniques, among
which importance sampling (IS) plays a central role. By changing the underlying probability
measure to make tail events occur more frequently and correcting via likelihood ratios, IS can
substantially reduce estimator variance when the change of measure is well aligned with the
structure of extreme losses. This viewpoint is emphasized in the rare-event simulation literature,
notably in the work of Glasserman, Heidelberger, and Shahabuddin, where exponential tilting is
used to efficiently estimate rare-event probabilities relevant for portfolio risk.

A second response emphasizes *robustness to distributional uncertainty* rather than sampling
efficiency. In many financial applications, the primary difficulty is not only Monte Carlo noise,
but also uncertainty about the correct tail model. It is well known that Gaussian return models
can be unrealistic for equity returns due to heavy tails, skewness, and volatility clustering; in such
settings, simulation can produce highly *precise* estimates of VaR under a misspecified model.
Discrete Moment Matching (DMM) belongs to a class of moment-based approaches that weaken
parametric assumptions: given a finite set of moment constraints, DMM constructs a discrete
distributional approximation and, more fundamentally in the formulation adopted here, produces
*bounds* on VaR over the set of all distributions consistent with the enforced moments and a
chosen discretization grid. Rather than returning a single number, DMM yields an interval that
explicitly reflects distributional ambiguity.

These perspectives highlight a key point: importance sampling and moment-based methods do not
solve the same problem. Importance sampling is designed to reduce variance when estimating tail
probabilities *under a specified nominal model*, whereas moment-based procedures are designed
to quantify tail risk *under partial distributional information*. This distinction becomes
particularly important under tail misspecification. If the nominal return model understates tail
thickness, then increasing the Monte Carlo budget or applying variance reduction can reduce
sampling error without correcting the underlying model error. In this sense, IS should be viewed
primarily as a computational efficiency enhancement rather than a remedy for model misspecification.

The objective of this paper is to provide a transparent comparison between these two approaches
in a controlled setting where tail misspecification is introduced deliberately and systematically.
We separate the *nominal* model used for estimator construction from the *true*
data-generating process used for evaluation. Daily returns of a broad equity market proxy are used
to calibrate a nominal Gaussian model, while true returns are generated from Student-tt
distributions with varying degrees of freedom to represent increasingly heavy tails. Within this
framework, IS is implemented via exponential tilting of the Gaussian model and VaR is computed
through likelihood-weighted root-finding, while DMM constructs moment-feasible VaR bounds by
enforcing finitely many moment constraints on a discretized loss distribution. This design isolates
the efficiency-robustness trade-off: IS can be highly efficient for the nominal target yet systematically
underestimate tail risk under heavy-tailed behavior, whereas DMM provides conservative bracketing
that remains meaningful under tail uncertainty at the expense of informativeness and numerical
feasibility at high moment orders.

##### Contributions.

This paper makes four contributions.
First, it provides a clear estimand-level comparison by distinguishing point estimation of VaR under
a nominal parametric model (IS) from interval-valued VaR characterization under moment-based
distributional ambiguity (DMM). Second, using a controlled simulation design that separates the
nominal Gaussian calibration from a heavy-tailed Student-tt data-generating process, it quantifies
how importance sampling remains computationally efficient while converging to the nominal-model
VaR, producing systematic underestimation of true tail risk as tails thicken and confidence levels
increase. Third, it empirically characterizes the behavior of DMM VaR bounds as additional moments
are enforced, documenting contraction of the moment-feasible set up to a numerically feasible limit
and interpreting resulting interval widths as an explicit measure of ambiguity rather than noise.
Fourth, it complements point estimates with practical diagnostics, including effective sample size
and weight concentration for IS and feasibility limits for DMM, that help assess numerical reliability
and the degree of misalignment between sampling measures, tail geometry, and distributional assumptions.

The remainder of the paper is organized as follows. Section 2 introduces the risk measure and loss
framework. Section 3 describes the data calibration and nominal return model. Section 4 presents
the heavy-tailed data-generating process used in the simulation study. Section 5 outlines the DMM
and IS VaR procedures. Section 6 describes the simulation design. Section 7 reports the empirical
findings, and Sections 8 to 9 discuss implications and conclude.

## 2 Problem Setup and Risk Measure

### 2.1 Data and Return Construction

Let {St}t=0T\{S\_{t}\}\_{t=0}^{T} denote the observed daily closing prices of QQQ over a fixed historical window, where tt indexes trading days. We define the one-day log-return by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt:=log⁡(StSt−1),t=1,…,T.R\_{t}\;:=\;\log\!\left(\frac{S\_{t}}{S\_{t-1}}\right),\qquad t=1,\dots,T. |  | (1) |

We treat {Rt}t=1T\{R\_{t}\}\_{t=1}^{T} as the calibration sample used to estimate parameters of a nominal return model.

### 2.2 Loss Variable

We consider a one-day risk horizon and define the loss random variable LL by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L:=−R,L\;:=\;-R, |  | (2) |

where RR is a generic one-day return distributed according to a model specified below. Under ([2](https://arxiv.org/html/2601.09927v1#S2.E2 "In 2.2 Loss Variable ‣ 2 Problem Setup and Risk Measure ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")), large losses correspond to large negative returns. All results in this paper are stated in “return units” (i.e., losses measured as negative log-returns). A dollar P&L loss can be recovered by a monotone transformation if needed, but is not required for the comparative study considered here.

### 2.3 Value-at-Risk as a Tail Probability Root

Fix a confidence level α∈(0,1)\alpha\in(0,1) (e.g., α=0.99\alpha=0.99). The Value-at-Risk at level α\alpha is defined as the α\alpha-quantile of the loss distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα​(L):=inf{x∈ℝ:FL​(x)≥α},FL​(x):=ℙ​(L≤x).\mathrm{VaR}\_{\alpha}(L)\;:=\;\inf\Big\{x\in\mathbb{R}:F\_{L}(x)\geq\alpha\Big\},\qquad F\_{L}(x):=\mathbb{P}(L\leq x). |  | (3) |

Equivalently, letting

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x):=ℙ​(L>x),p(x)\;:=\;\mathbb{P}(L>x), |  | (4) |

VaR is characterized as the solution of the tail probability equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(xα)= 1−α,where ​xα:=VaRα​(L).p(x\_{\alpha})\;=\;1-\alpha,\qquad\text{where }x\_{\alpha}:=\mathrm{VaR}\_{\alpha}(L). |  | (5) |

In the present setting L=−RL=-R, so the rare-event set {L>x}\{L>x\} can be expressed in terms of returns as

|  |  |  |  |
| --- | --- | --- | --- |
|  | {L>x}={−R>x}={R<−x}.\{L>x\}\;=\;\{-R>x\}\;=\;\{R<-x\}. |  | (6) |

Thus, VaR estimation at high confidence levels reduces to accurately estimating small tail probabilities of the form ℙ​(R<−x)\mathbb{P}(R<-x).

### 2.4 Objective of the Study

The goal of this paper is to compare two simulation-based approaches to
characterizing tail risk at level α\alpha, centered around the Value-at-Risk
quantity xαx\_{\alpha} defined in ([5](https://arxiv.org/html/2601.09927v1#S2.E5 "In 2.3 Value-at-Risk as a Tail Probability Root ‣ 2 Problem Setup and Risk Measure ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")):
(i) an importance sampling estimator based on an exponential change of measure applied to a Gaussian nominal model, and
(ii) a discrete moment matching estimator based on constructing a discrete approximation to the return distribution.
The comparison is performed under controlled tail misspecification by sampling returns from a heavy-tailed Student-tt data-generating process while applying estimators calibrated under a Gaussian nominal model. In short, while importance sampling targets a point estimate of xαx\_{\alpha} under the
nominal model, discrete moment matching produces interval-valued bounds that
reflect distributional ambiguity.

## 3 Nominal Model and Calibration

### 3.1 Nominal Probability Measure

Throughout this paper, VaR estimators are constructed under a *nominal* probability measure, denoted by ℙ\mathbb{P}, which serves as the assumed return model for both importance sampling and discrete moment matching. Under ℙ\mathbb{P}, the one-day return RR is modeled as Gaussian:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R∼𝒩​(μ,σ2),R\sim\mathcal{N}(\mu,\sigma^{2}), |  | (7) |

where (μ,σ)(\mu,\sigma) are unknown parameters to be estimated from historical data. This Gaussian model is not intended to be a realistic description of extreme tail behavior; rather, it provides a tractable baseline that allows the effect of variance-reduction and moment-matching techniques to be studied in isolation.

### 3.2 Parameter Estimation

Let {Rt}t=1T\{R\_{t}\}\_{t=1}^{T} denote the observed log-return sample defined in ([1](https://arxiv.org/html/2601.09927v1#S2.E1 "In 2.1 Data and Return Construction ‣ 2 Problem Setup and Risk Measure ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")). The nominal parameters (μ,σ)(\mu,\sigma) in ([7](https://arxiv.org/html/2601.09927v1#S3.E7 "In 3.1 Nominal Probability Measure ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) are estimated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^=1T​∑t=1TRt,σ^2=1T​∑t=1T(Rt−μ^)2.\hat{\mu}\;=\;\frac{1}{T}\sum\_{t=1}^{T}R\_{t},\qquad\hat{\sigma}^{2}\;=\;\frac{1}{T}\sum\_{t=1}^{T}(R\_{t}-\hat{\mu})^{2}. |  | (8) |

The variance estimator in ([8](https://arxiv.org/html/2601.09927v1#S3.E8 "In 3.2 Parameter Estimation ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) corresponds to the maximum likelihood estimator under the Gaussian assumption. This choice is consistent with the simulation-based estimators used throughout the paper, which rely on repeated sampling from the fitted nominal distribution. In particular, the use of the 1/T1/T normalization (rather than 1/(T−1)1/(T-1)) ensures that σ^2\hat{\sigma}^{2} is the likelihood-consistent variance parameter for the normal model.

### 3.3 Role of the Nominal Model

The estimated parameters (μ^,σ^)(\hat{\mu},\hat{\sigma}) define the nominal return distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | R∼𝒩​(μ^,σ^2)under ​ℙ,R\sim\mathcal{N}(\hat{\mu},\hat{\sigma}^{2})\quad\text{under }\mathbb{P}, |  | (9) |

which plays a central role in both VaR estimation methods considered in this study:

* •

  In the *importance sampling* approach, ([9](https://arxiv.org/html/2601.09927v1#S3.E9 "In 3.3 Role of the Nominal Model ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) serves as the reference distribution with respect to which likelihood ratios are computed. A tilted sampling distribution is introduced to oversample tail losses, but unbiasedness of the estimator is defined relative to ℙ\mathbb{P}.
* •

  In the *discrete moment matching* approach, the first four moments implied by ([9](https://arxiv.org/html/2601.09927v1#S3.E9 "In 3.3 Role of the Nominal Model ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) (mean, variance, skewness, and kurtosis) are matched by a discrete distribution, which is then used to approximate the loss distribution for Monte Carlo VaR estimation.

In both cases, the Gaussian nominal model is treated as the *assumed* data-generating process for the estimator, even though the true data-generating process used in the simulation experiments differs from ([9](https://arxiv.org/html/2601.09927v1#S3.E9 "In 3.3 Role of the Nominal Model ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")).

### 3.4 Closed-Form Gaussian VaR as a Pilot Estimate

Under the nominal model ([9](https://arxiv.org/html/2601.09927v1#S3.E9 "In 3.3 Role of the Nominal Model ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")), the loss variable L=−RL=-R is also Gaussian with mean −μ^-\hat{\mu} and variance σ^2\hat{\sigma}^{2}. The corresponding VaR at confidence level α\alpha admits the closed-form expression

|  |  |  |  |
| --- | --- | --- | --- |
|  | x0=VaRα(Gauss)=−(μ^+σ^​z1−α),x\_{0}\;=\;\mathrm{VaR}\_{\alpha}^{(\mathrm{Gauss})}\;=\;-\big(\hat{\mu}+\hat{\sigma}z\_{1-\alpha}\big), |  | (10) |

where z1−αz\_{1-\alpha} denotes the (1−α)(1-\alpha)-quantile of the standard normal distribution. This quantity is used as a *pilot VaR estimate* to guide the construction of the importance sampling change of measure. Importantly, ([10](https://arxiv.org/html/2601.09927v1#S3.E10 "In 3.4 Closed-Form Gaussian VaR as a Pilot Estimate ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is not treated as a final risk estimate; rather, it serves as an analytically convenient reference point that localizes the rare-event region {L>x}\{L>x\} for subsequent simulation.

### 3.5 Assumptions and Limitations

The nominal Gaussian model ([7](https://arxiv.org/html/2601.09927v1#S3.E7 "In 3.1 Nominal Probability Measure ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) rests on several simplifying assumptions:

1. 1.

   The return sequence is assumed to be independent and identically distributed.
2. 2.

   The distribution of returns is assumed to be light-tailed with finite exponential moments.
3. 3.

   Parameters (μ,σ)(\mu,\sigma) are assumed to be time-invariant over the calibration window.

These assumptions are deliberately relaxed in the simulation design by sampling returns from a heavy-tailed Student-tt distribution while retaining ([7](https://arxiv.org/html/2601.09927v1#S3.E7 "In 3.1 Nominal Probability Measure ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) as the estimator’s reference model. This deliberate mismatch allows the robustness of the VaR estimators to tail misspecification to be studied explicitly.

## 4 True Data-Generating Process

### 4.1 Distinction Between Nominal and True Measures

A central feature of this study is the deliberate separation between the *nominal* probability measure used by the VaR estimators and the *true* probability measure governing the data-generating process. While both importance sampling and discrete moment matching are constructed under the Gaussian nominal model defined in Section [3](https://arxiv.org/html/2601.09927v1#S3 "3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"), performance is evaluated under a heavy-tailed return distribution. This design allows the robustness of each estimator to tail misspecification to be assessed in a controlled manner.

To formalize this distinction, let ℙ\mathbb{P} denote the nominal Gaussian measure under which estimators are calibrated, and let ℙ⋆\mathbb{P}^{\star} denote the true probability measure under which returns are generated in the simulation experiments.

### 4.2 Student-tt Return Model

Under the true measure ℙ⋆\mathbb{P}^{\star}, one-day returns are assumed to follow a standardized Student-tt distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R⋆∼tν​(μ⋆,sν2),R^{\star}\sim t\_{\nu}(\mu^{\star},s\_{\nu}^{2}), |  | (11) |

where ν>2\nu>2 denotes the degrees of freedom, μ⋆\mu^{\star} is the location parameter, and sν2s\_{\nu}^{2} is the scale parameter. The Student-tt distribution is symmetric and heavy-tailed, with polynomial tail decay governed by ν\nu. As ν→∞\nu\to\infty, the distribution converges to a Gaussian, whereas smaller values of ν\nu correspond to increasingly heavy tails.

In all experiments, the location parameter is set equal to the nominal mean estimate,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ⋆:=μ^,\mu^{\star}:=\hat{\mu}, |  | (12) |

ensuring that misspecification arises solely from differences in tail behavior rather than shifts in central tendency.

### 4.3 Variance Matching

To isolate the effect of tail thickness, the Student-tt distribution is scaled to match the variance of the nominal Gaussian model. For ν>2\nu>2, the variance of a Student-tt random variable with scale parameter sν2s\_{\nu}^{2} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Varℙ⋆​(R⋆)=sν2​νν−2.\mathrm{Var}\_{\mathbb{P}^{\star}}(R^{\star})\;=\;s\_{\nu}^{2}\,\frac{\nu}{\nu-2}. |  | (13) |

The scale parameter is therefore chosen such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | sν2=σ^2​ν−2ν,s\_{\nu}^{2}\;=\;\hat{\sigma}^{2}\,\frac{\nu-2}{\nu}, |  | (14) |

which ensures

|  |  |  |  |
| --- | --- | --- | --- |
|  | Varℙ⋆​(R⋆)=σ^2.\mathrm{Var}\_{\mathbb{P}^{\star}}(R^{\star})\;=\;\hat{\sigma}^{2}. |  | (15) |

This variance-matching step guarantees that any differences in VaR estimation accuracy across methods are attributable to higher-order tail behavior rather than differences in volatility scaling.

### 4.4 Loss Variable Under the True Measure

As in the nominal setting, the loss variable under the true measure is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L⋆:=−R⋆.L^{\star}:=-R^{\star}. |  | (16) |

The target risk quantity in the simulation study is the true VaR,

|  |  |  |  |
| --- | --- | --- | --- |
|  | xα⋆:=inf{x:ℙ⋆​(L⋆≤x)≥α},x\_{\alpha}^{\star}\;:=\;\inf\big\{x:\mathbb{P}^{\star}(L^{\star}\leq x)\geq\alpha\big\}, |  | (17) |

which generally differs from the Gaussian VaR implied by the nominal model in Section [3](https://arxiv.org/html/2601.09927v1#S3 "3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"). In particular, for finite ν\nu, the heavy-tailed nature of the Student-tt distribution implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | xα⋆>xα(Gauss)for large ​α,x\_{\alpha}^{\star}\;>\;x\_{\alpha}^{(\mathrm{Gauss})}\qquad\text{for large }\alpha, |  | (18) |

reflecting increased tail risk relative to the Gaussian benchmark.

### 4.5 Experimental Regimes

The simulation study considers a range of degrees of freedom

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν∈{5, 7, 10},\nu\in\{5,\,7,\,10\}, |  | (19) |

spanning moderately heavy-tailed to near-Gaussian regimes. For each value of ν\nu, independent samples are generated from ([11](https://arxiv.org/html/2601.09927v1#S4.E11 "In 4.2 Student-𝑡 Return Model ‣ 4 True Data-Generating Process ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")), and VaR is estimated using methods calibrated under the nominal Gaussian model. This design enables a systematic examination of how estimator bias, variance, and stability evolve as tail thickness increases.

### 4.6 Interpretation as Controlled Misspecification

It is emphasized that the Student-tt model ([11](https://arxiv.org/html/2601.09927v1#S4.E11 "In 4.2 Student-𝑡 Return Model ‣ 4 True Data-Generating Process ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is not proposed as a realistic description of market returns. Rather, it serves as a mathematically tractable mechanism for introducing controlled deviations from Gaussian tail behavior. By holding the mean and variance fixed while varying ν\nu, the simulation framework isolates the impact of tail misspecification on VaR estimation, allowing the efficiency-robustness trade-off between importance sampling and discrete moment matching to be evaluated transparently.

## 5 Value-at-Risk Estimation Methods

This section defines the two VaR estimators studied in this paper. Throughout, α∈(0,1)\alpha\in(0,1) is fixed (e.g. α=0.99\alpha=0.99). The return random variable is denoted by RR, and the associated loss is L=−RL=-R as in ([2](https://arxiv.org/html/2601.09927v1#S2.E2 "In 2.2 Loss Variable ‣ 2 Problem Setup and Risk Measure ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")). The defining VaR equation is the tail-probability root condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(xα)=1−α,p​(x):=ℙ​(L>x)=ℙ​(R<−x),p(x\_{\alpha})=1-\alpha,\qquad p(x):=\mathbb{P}(L>x)=\mathbb{P}(R<-x), |  | (20) |

where ℙ\mathbb{P} denotes the nominal measure defined in Section [3](https://arxiv.org/html/2601.09927v1#S3 "3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing").

### 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing

#### 5.1.1 Moment Information

Let LL denote the (unknown) one-day loss random variable under the nominal measure ℙ\mathbb{P}. Suppose that the first dd raw moments of LL are available:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μr:=𝔼ℙ​[Lr],r=1,2,…,d,\mu\_{r}:=\mathbb{E}\_{\mathbb{P}}[L^{r}],\qquad r=1,2,\dots,d, |  | (21) |

with the convention μ0:=1\mu\_{0}:=1. In implementation, the moment vector (μ1,…,μd)(\mu\_{1},\ldots,\mu\_{d}) is computed from
loss samples generated under the *nominal Gaussian model* calibrated in
Section 3. The DMM procedure therefore operates under the same nominal
information set as the importance sampling estimator. When the true
data-generating process differs from the nominal model, the imposed moment
constraints may themselves be misspecified; in this case, the resulting VaR
bounds should be interpreted as robust to tail uncertainty conditional on
nominal moment information.

#### 5.1.2 Discretization Grid and Moment-Feasible Set

Fix an ordered finite grid (support) of possible loss values

|  |  |  |  |
| --- | --- | --- | --- |
|  | X0<X1<⋯<Xm,Xi∈ℝ,X\_{0}<X\_{1}<\cdots<X\_{m},\qquad X\_{i}\in\mathbb{R}, |  | (22) |

and consider discrete probability vectors

|  |  |  |  |
| --- | --- | --- | --- |
|  | p=(p0,…,pm)∈ℝm+1,pi≥0,∑i=0mpi=1.p=(p\_{0},\dots,p\_{m})\in\mathbb{R}^{m+1},\qquad p\_{i}\geq 0,\ \ \sum\_{i=0}^{m}p\_{i}=1. |  | (23) |

The *moment-feasible set* is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫d:={p∈ℝm+1:pi≥0,∑i=0mpi=1,∑i=0mXir​pi=μr,r=1,…,d}.\mathcal{P}\_{d}:=\left\{p\in\mathbb{R}^{m+1}:p\_{i}\geq 0,\ \sum\_{i=0}^{m}p\_{i}=1,\ \sum\_{i=0}^{m}X\_{i}^{r}\,p\_{i}=\mu\_{r},\ r=1,\dots,d\right\}. |  | (24) |

Any p∈𝒫dp\in\mathcal{P}\_{d} defines a discrete distribution supported on the grid {Xi}i=0m\{X\_{i}\}\_{i=0}^{m} that matches the first dd raw moments of LL exactly.

#### 5.1.3 Quantile Functional on the Grid

For a given feasible vector p∈𝒫dp\in\mathcal{P}\_{d}, define its discrete cumulative distribution function (CDF) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fp​(x):=∑i:Xi≤xpi,F\_{p}(x):=\sum\_{i:X\_{i}\leq x}p\_{i}, |  | (25) |

and define the α\alpha-quantile (VaR functional) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | hα​(p):=VaRα​(p):=inf{x∈ℝ:Fp​(x)≥α}.h\_{\alpha}(p):=\mathrm{VaR}\_{\alpha}(p):=\inf\{x\in\mathbb{R}:F\_{p}(x)\geq\alpha\}. |  | (26) |

Because the support is finite and ordered, ([26](https://arxiv.org/html/2601.09927v1#S5.E26 "In 5.1.3 Quantile Functional on the Grid ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα​(p)=Xj⋆​(p),j⋆​(p):=min⁡{j∈{0,…,m}:∑i=0jpi≥α}.\mathrm{VaR}\_{\alpha}(p)=X\_{j^{\star}(p)},\qquad j^{\star}(p):=\min\left\{j\in\{0,\dots,m\}:\ \sum\_{i=0}^{j}p\_{i}\geq\alpha\right\}. |  | (27) |

The map p↦VaRα​(p)p\mapsto\mathrm{VaR}\_{\alpha}(p) is nonlinear due to the thresholding implicit in the cumulative sums.

#### 5.1.4 DMM Output as a VaR Interval (Deterministic Bracketing)

The DMM philosophy adopted here is *distributional ambiguity given finitely many moments*. Since the true distribution of LL is unknown beyond the moment constraints, the quantile itself can vary across 𝒫d\mathcal{P}\_{d}. The tight moment-consistent VaR lower and upper bounds are defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | vα−:=infp∈𝒫dVaRα​(p),vα+:=supp∈𝒫dVaRα​(p).v^{-}\_{\alpha}:=\inf\_{p\in\mathcal{P}\_{d}}\mathrm{VaR}\_{\alpha}(p),\qquad v^{+}\_{\alpha}:=\sup\_{p\in\mathcal{P}\_{d}}\mathrm{VaR}\_{\alpha}(p). |  | (28) |

Any loss distribution consistent with ([24](https://arxiv.org/html/2601.09927v1#S5.E24 "In 5.1.2 Discretization Grid and Moment-Feasible Set ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) must satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | vα−≤VaRα​(L)≤vα+.v^{-}\_{\alpha}\leq\mathrm{VaR}\_{\alpha}(L)\leq v^{+}\_{\alpha}. |  | (29) |

Thus, the DMM method returns an *interval-valued* characterization of VaR, quantifying the range of tail risk compatible with the moment information.

#### 5.1.5 Computational Reduction via CDF Bounds

Directly optimizing ([28](https://arxiv.org/html/2601.09927v1#S5.E28 "In 5.1.4 DMM Output as a VaR Interval (Deterministic Bracketing) ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is difficult because the quantile functional is nonlinear. A standard reduction is to work with CDF bounds at fixed thresholds. For any fixed x∈ℝx\in\mathbb{R}, define the linear functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fp​(x)=∑i:Xi≤xpi,F\_{p}(x)=\sum\_{i:X\_{i}\leq x}p\_{i}, |  | (30) |

and define the moment-consistent lower and upper CDF envelopes

|  |  |  |  |
| --- | --- | --- | --- |
|  | F−​(x):=infp∈𝒫dFp​(x),F+​(x):=supp∈𝒫dFp​(x).F^{-}(x):=\inf\_{p\in\mathcal{P}\_{d}}F\_{p}(x),\qquad F^{+}(x):=\sup\_{p\in\mathcal{P}\_{d}}F\_{p}(x). |  | (31) |

Because ([30](https://arxiv.org/html/2601.09927v1#S5.E30 "In 5.1.5 Computational Reduction via CDF Bounds ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is linear in pp and 𝒫d\mathcal{P}\_{d} is defined by linear equalities/inequalities, both optimization problems in ([31](https://arxiv.org/html/2601.09927v1#S5.E31 "In 5.1.5 Computational Reduction via CDF Bounds ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) are linear programs.

The VaR bounds are then obtained by inversion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vα−=inf{x:F−​(x)≥α},vα+=inf{x:F+​(x)≥α}.v^{-}\_{\alpha}=\inf\{x:\ F^{-}(x)\geq\alpha\},\qquad v^{+}\_{\alpha}=\inf\{x:\ F^{+}(x)\geq\alpha\}. |  | (32) |

In implementation, xx is restricted to the grid {X0,…,Xm}\{X\_{0},\dots,X\_{m}\} and the inversion is computed by identifying the first grid point at which the bound crosses α\alpha.

#### 5.1.6 Assumptions and Limitations of DMM

The DMM bracketing procedure relies on:

1. 1.

   Finite-moment information: only {μr}r=1d\{\mu\_{r}\}\_{r=1}^{d} is assumed known. This choice is deliberate and defines the ambiguity set ([24](https://arxiv.org/html/2601.09927v1#S5.E24 "In 5.1.2 Discretization Grid and Moment-Feasible Set ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")).
2. 2.

   Grid restriction: feasibility and bounds are computed only over distributions supported on the fixed grid ([22](https://arxiv.org/html/2601.09927v1#S5.E22 "In 5.1.2 Discretization Grid and Moment-Feasible Set ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")). Therefore, the resulting interval ([29](https://arxiv.org/html/2601.09927v1#S5.E29 "In 5.1.4 DMM Output as a VaR Interval (Deterministic Bracketing) ‣ 5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is conditional on the discretization.
3. 3.

   Moment feasibility: for large dd the constraint system may become infeasible
   due to a combination of numerical ill-conditioning and theoretical moment
   nonexistence under heavy-tailed distributions. In particular, when the true
   data-generating process exhibits polynomial tails, higher-order moments
   implied by the nominal model may not exist under the true measure.

The method is distribution-free beyond the moment constraints, but it is not model-free in the sense that results depend on the chosen grid and the order of moments enforced.

### 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding

#### 5.2.1 Nominal Model and Tail Probability Target

Under the nominal measure ℙ\mathbb{P}, returns satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | R∼𝒩​(μ,σ2),R\sim\mathcal{N}(\mu,\sigma^{2}), |  | (33) |

with (μ,σ)(\mu,\sigma) estimated as in ([8](https://arxiv.org/html/2601.09927v1#S3.E8 "In 3.2 Parameter Estimation ‣ 3 Nominal Model and Calibration ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")). The tail probability corresponding to a loss threshold xx is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x):=ℙ​(L>x)=ℙ​(R<−x)=𝔼ℙ​[𝟏​{R<−x}].p(x):=\mathbb{P}(L>x)=\mathbb{P}(R<-x)=\mathbb{E}\_{\mathbb{P}}\!\left[\mathbf{1}\{R<-x\}\right]. |  | (34) |

VaR is defined as the solution xαx\_{\alpha} to p​(xα)=1−αp(x\_{\alpha})=1-\alpha.

#### 5.2.2 Importance Sampling Measure

To reduce variance when 1−α1-\alpha is small, importance sampling introduces an alternative sampling measure ℚθ\mathbb{Q}\_{\theta} under which the rare event {R<−x}\{R<-x\} occurs more frequently. In this paper, ℚθ\mathbb{Q}\_{\theta} is chosen as a mean-shifted Gaussian with unchanged variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R∼𝒩​(μ−θ,σ2)under ​ℚθ,θ>0.R\sim\mathcal{N}(\mu-\theta,\sigma^{2})\quad\text{under }\mathbb{Q}\_{\theta},\qquad\theta>0. |  | (35) |

This is an exponential tilting (Esscher-type) change of measure for the Gaussian family.

#### 5.2.3 Likelihood Ratio (Radon-Nikodym Derivative)

Let fℙf\_{\mathbb{P}} and fℚθf\_{\mathbb{Q}\_{\theta}} denote the densities of RR under ([33](https://arxiv.org/html/2601.09927v1#S5.E33 "In 5.2.1 Nominal Model and Tail Probability Target ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) and ([35](https://arxiv.org/html/2601.09927v1#S5.E35 "In 5.2.2 Importance Sampling Measure ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")), respectively. The likelihood ratio (Radon-Nikodym derivative) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wθ​(r):=fℙ​(r)fℚθ​(r).W\_{\theta}(r):=\frac{f\_{\mathbb{P}}(r)}{f\_{\mathbb{Q}\_{\theta}}(r)}. |  | (36) |

For Gaussian densities with identical variance and a mean shift θ\theta, the ratio is available in closed form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wθ​(r)=exp⁡(θσ2​(r−μ)+θ22​σ2).W\_{\theta}(r)=\exp\!\left(\frac{\theta}{\sigma^{2}}(r-\mu)+\frac{\theta^{2}}{2\sigma^{2}}\right). |  | (37) |

This identity is exact and is the mathematical justification for the weight computation in the code.

#### 5.2.4 Unbiased IS Estimator of the Tail Probability

By change-of-measure,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)=𝔼ℙ​[𝟏​{R<−x}]=𝔼ℚθ​[𝟏​{R<−x}​Wθ​(R)].p(x)=\mathbb{E}\_{\mathbb{P}}[\mathbf{1}\{R<-x\}]=\mathbb{E}\_{\mathbb{Q}\_{\theta}}\!\left[\mathbf{1}\{R<-x\}W\_{\theta}(R)\right]. |  | (38) |

Given i.i.d. samples R(1),…,R(N)∼𝒩​(μ−θ,σ2)R^{(1)},\dots,R^{(N)}\sim\mathcal{N}(\mu-\theta,\sigma^{2}) under ℚθ\mathbb{Q}\_{\theta}, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^IS​(x;θ):=1N​∑i=1N𝟏​{R(i)<−x}​Wθ​(R(i)).\widehat{p}\_{\mathrm{IS}}(x;\theta):=\frac{1}{N}\sum\_{i=1}^{N}\mathbf{1}\{R^{(i)}<-x\}\,W\_{\theta}(R^{(i)}). |  | (39) |

Then 𝔼ℚθ​[p^IS​(x;θ)]=p​(x)\mathbb{E}\_{\mathbb{Q}\_{\theta}}[\widehat{p}\_{\mathrm{IS}}(x;\theta)]=p(x), i.e. ([39](https://arxiv.org/html/2601.09927v1#S5.E39 "In 5.2.4 Unbiased IS Estimator of the Tail Probability ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is unbiased for the nominal tail probability p​(x)p(x).

#### 5.2.5 Tilt Selection (Glasserman-Style Heuristic)

The efficiency of ([39](https://arxiv.org/html/2601.09927v1#S5.E39 "In 5.2.4 Unbiased IS Estimator of the Tail Probability ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) depends on choosing θ\theta so that the proposal distribution places non-negligible mass near the rare-event boundary. A practical heuristic is to use the closed-form Gaussian pilot VaR

|  |  |  |  |
| --- | --- | --- | --- |
|  | x0=−(μ+σ​z1−α),x\_{0}=-(\mu+\sigma z\_{1-\alpha}), |  | (40) |

and choose θ\theta to shift the mean under ℚθ\mathbb{Q}\_{\theta} toward the boundary return level −x0-x\_{0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ−θ≈−x0⟹θ:=μ+x0.\mu-\theta\approx-x\_{0}\quad\Longrightarrow\quad\theta:=\mu+x\_{0}. |  | (41) |

This choice increases the frequency of samples satisfying R<−xR<-x when xx is near the VaR region, thereby reducing the variance of ([39](https://arxiv.org/html/2601.09927v1#S5.E39 "In 5.2.4 Unbiased IS Estimator of the Tail Probability ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) relative to naive Monte Carlo.

#### 5.2.6 VaR Computation via Root-Finding (Bracketing + Bisection)

Since p​(x)p(x) is monotone decreasing in xx, the VaR equation can be solved numerically. Define the target tail probability

|  |  |  |  |
| --- | --- | --- | --- |
|  | πα:=1−α.\pi\_{\alpha}:=1-\alpha. |  | (42) |

The IS-based VaR estimate is defined as the numerical solution to

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^IS​(x;θ)=πα.\widehat{p}\_{\mathrm{IS}}(x;\theta)=\pi\_{\alpha}. |  | (43) |

A bracketing interval [xmin,xmax][x\_{\min},x\_{\max}] is first constructed such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^IS​(xmin;θ)≥πα,p^IS​(xmax;θ)≤πα.\widehat{p}\_{\mathrm{IS}}(x\_{\min};\theta)\geq\pi\_{\alpha},\qquad\widehat{p}\_{\mathrm{IS}}(x\_{\max};\theta)\leq\pi\_{\alpha}. |  | (44) |

Given a valid bracket, bisection iteratively updates xmin,xmaxx\_{\min},x\_{\max} until xmax−xminx\_{\max}-x\_{\min} is below a tolerance. The IS VaR estimate returned by the procedure is

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR^α,IS:=xmin+xmax2.\widehat{\mathrm{VaR}}\_{\alpha,\mathrm{IS}}:=\frac{x\_{\min}+x\_{\max}}{2}. |  | (45) |

#### 5.2.7 Common Random Numbers (CRN) for Numerical Stability

Because p^IS​(x;θ)\widehat{p}\_{\mathrm{IS}}(x;\theta) is a Monte Carlo estimator, it is noisy as a function of xx. To prevent bisection from reacting to independent simulation noise at each iteration, common random numbers are used: the random number generator is reset to the same seed at each bisection evaluation, so that differences in p^IS​(x;θ)\widehat{p}\_{\mathrm{IS}}(x;\theta) across nearby xx values reflect changes in xx rather than unrelated Monte Carlo variation. This stabilizes the monotone behavior required by ([44](https://arxiv.org/html/2601.09927v1#S5.E44 "In 5.2.6 VaR Computation via Root-Finding (Bracketing + Bisection) ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")).

#### 5.2.8 Weight Stability Diagnostics

Importance sampling can fail numerically when weights become highly concentrated (weight degeneracy), leading to inflated variance and unreliable estimates. Two diagnostics are recorded.

First define normalized weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | w~i:=Wθ​(R(i))∑j=1NWθ​(R(j)),i=1,…,N.\widetilde{w}\_{i}:=\frac{W\_{\theta}(R^{(i)})}{\sum\_{j=1}^{N}W\_{\theta}(R^{(j)})},\qquad i=1,\dots,N. |  | (46) |

The effective sample size (ESS) proxy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESS:=1∑i=1Nw~i2,\mathrm{ESS}:=\frac{1}{\sum\_{i=1}^{N}\widetilde{w}\_{i}^{2}}, |  | (47) |

which lies in [1,N][1,N] and measures weight dispersion (larger is better). The maximum normalized weight share is

|  |  |  |  |
| --- | --- | --- | --- |
|  | wmax:=max1≤i≤N⁡w~i,w\_{\max}:=\max\_{1\leq i\leq N}\widetilde{w}\_{i}, |  | (48) |

which quantifies whether the estimator is dominated by a small number of extreme samples. Large values of wmaxw\_{\max} and very small values of ESS indicate potential degeneracy.

#### 5.2.9 Assumptions and Limitations of IS

The IS estimator ([39](https://arxiv.org/html/2601.09927v1#S5.E39 "In 5.2.4 Unbiased IS Estimator of the Tail Probability ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is unbiased for p​(x)p(x) under the nominal measure ℙ\mathbb{P} provided that:

1. 1.

   The proposal density fℚθf\_{\mathbb{Q}\_{\theta}} is absolutely continuous with respect to fℙf\_{\mathbb{P}} (true for Gaussian mean shifts).
2. 2.

   The likelihood ratio ([37](https://arxiv.org/html/2601.09927v1#S5.E37 "In 5.2.3 Likelihood Ratio (Radon-Nikodym Derivative) ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) is evaluated exactly and without overflow/underflow.
3. 3.

   The second moment 𝔼ℚθ​[𝟏​{R<−x}​Wθ​(R)2]\mathbb{E}\_{\mathbb{Q}\_{\theta}}\!\big[\mathbf{1}\{R<-x\}W\_{\theta}(R)^{2}\big] is finite (which holds in the Gaussian setting but can still yield severe finite-sample degeneracy for aggressive tilts).

In the misspecification experiments of Section [4](https://arxiv.org/html/2601.09927v1#S4 "4 True Data-Generating Process ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"), performance is evaluated under ℙ⋆\mathbb{P}^{\star} (Student-tt returns). In that setting, the IS procedure remains a valid estimator of the *nominal-model* VaR but may exhibit bias relative to the *true* VaR xα⋆x\_{\alpha}^{\star} because the Gaussian nominal model does not match the true tail behavior. This bias is an intended object of study and is measured explicitly in the results section.

## 6 Simulation Design

This section describes the simulation framework used to evaluate the performance of the VaR estimators defined in Section [5](https://arxiv.org/html/2601.09927v1#S5 "5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"). The design is constructed to ensure a fair and controlled comparison between importance sampling and discrete moment matching under varying degrees of tail misspecification.

### 6.1 Experimental Parameters

The simulation study considers the following fixed parameters:

* •

  Confidence level: α∈{0.99}\alpha\in\{0.99\}.
* •

  Degrees of freedom: ν∈{5,7,10}\nu\in\{5,7,10\} for the Student-tt data-generating process defined in Section [4](https://arxiv.org/html/2601.09927v1#S4 "4 True Data-Generating Process ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing").
* •

  Monte Carlo budget: NN samples per VaR evaluation (e.g. N=10,000N=10{,}000).
* •

  Number of replications: MM independent simulation runs (e.g. M=100M=100).

All reported performance metrics are computed across the MM replications.

### 6.2 Simulation Loop

For each degree of freedom ν∈{5,7,10}\nu\in\{5,7,10\} and each replication index m=1,…,Mm=1,\dots,M, the following steps are executed:

1. 1.

   Generate true returns.
   Draw an i.i.d. sample

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | R1⋆,(m),…,RT⋆,(m)∼tν​(μ^,sν2),R^{\star,(m)}\_{1},\dots,R^{\star,(m)}\_{T}\;\sim\;t\_{\nu}(\hat{\mu},s\_{\nu}^{2}), |  | (49) |

   where sν2s\_{\nu}^{2} is defined by the variance-matching condition ([14](https://arxiv.org/html/2601.09927v1#S4.E14 "In 4.3 Variance Matching ‣ 4 True Data-Generating Process ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")). This sample represents returns generated under the true measure ℙ⋆\mathbb{P}^{\star}.
2. 2.

   Compute true losses.
   Define

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Lt⋆,(m):=−Rt⋆,(m),t=1,…,T.L^{\star,(m)}\_{t}:=-R^{\star,(m)}\_{t},\qquad t=1,\dots,T. |  | (50) |
3. 3.

   Estimate nominal parameters.
   Using the return sample {Rt⋆,(m)}t=1T\{R^{\star,(m)}\_{t}\}\_{t=1}^{T}, compute the Gaussian MLEs

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | μ^(m):=1T​∑t=1TRt⋆,(m),(σ^(m))2:=1T​∑t=1T(Rt⋆,(m)−μ^(m))2.\hat{\mu}^{(m)}:=\frac{1}{T}\sum\_{t=1}^{T}R^{\star,(m)}\_{t},\qquad(\hat{\sigma}^{(m)})^{2}:=\frac{1}{T}\sum\_{t=1}^{T}(R^{\star,(m)}\_{t}-\hat{\mu}^{(m)})^{2}. |  | (51) |

   These parameters define the nominal model used by both VaR estimators in replication mm.
4. 4.

   Compute true VaR benchmark.
   The true VaR under ℙ⋆\mathbb{P}^{\star} is computed analytically using the Student-tt quantile:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | xα⋆,(m):=−(μ^(m)+sν​tν, 1−α),x\_{\alpha}^{\star,(m)}:=-\left(\hat{\mu}^{(m)}+s\_{\nu}\,t\_{\nu,\,1-\alpha}\right), |  | (52) |

   where tν, 1−αt\_{\nu,\,1-\alpha} denotes the (1−α)(1-\alpha)-quantile of a standardized Student-tt distribution with ν\nu degrees of freedom.
5. 5.

   DMM VaR estimation.
   Using the nominal moments implied by μ^(m)\hat{\mu}^{(m)} and σ^(m)\hat{\sigma}^{(m)}, the DMM procedure described in Section [5.1](https://arxiv.org/html/2601.09927v1#S5.SS1 "5.1 Discrete Moment Matching (DMM) via Moment-Feasible VaR Bracketing ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") is applied to compute lower and upper VaR bounds

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | v^α−,(m),v^α+,(m).\widehat{v}^{-,(m)}\_{\alpha},\qquad\widehat{v}^{+,(m)}\_{\alpha}. |  | (53) |

   When a point estimate is required for comparison, the midpoint

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | x^α,DMM(m):=v^α−,(m)+v^α+,(m)2\widehat{x}^{(m)}\_{\alpha,\mathrm{DMM}}:=\frac{\widehat{v}^{-,(m)}\_{\alpha}+\widehat{v}^{+,(m)}\_{\alpha}}{2} |  | (54) |

   is reported, with the interval width retained as a measure of ambiguity.
6. 6.

   IS VaR estimation.
   Using the nominal Gaussian model ([33](https://arxiv.org/html/2601.09927v1#S5.E33 "In 5.2.1 Nominal Model and Tail Probability Target ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) with parameters (μ^(m),σ^(m))(\hat{\mu}^{(m)},\hat{\sigma}^{(m)}), the IS procedure of Section [5.2](https://arxiv.org/html/2601.09927v1#S5.SS2 "5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") is applied:

   1. (a)

      Compute the pilot Gaussian VaR x0(m)x\_{0}^{(m)} via ([40](https://arxiv.org/html/2601.09927v1#S5.E40 "In 5.2.5 Tilt Selection (Glasserman-Style Heuristic) ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")).
   2. (b)

      Set the tilting parameter θ(m)\theta^{(m)} via ([41](https://arxiv.org/html/2601.09927v1#S5.E41 "In 5.2.5 Tilt Selection (Glasserman-Style Heuristic) ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")).
   3. (c)

      Solve the root equation ([43](https://arxiv.org/html/2601.09927v1#S5.E43 "In 5.2.6 VaR Computation via Root-Finding (Bracketing + Bisection) ‣ 5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")) by bracketing and bisection to obtain

      |  |  |  |  |
      | --- | --- | --- | --- |
      |  | x^α,IS(m).\widehat{x}^{(m)}\_{\alpha,\mathrm{IS}}. |  | (55) |
   4. (d)

      Record stability diagnostics: ESS and wmaxw\_{\max}.

### 6.3 Performance Metrics

For each estimator and each value of ν\nu, performance is summarized using the following metrics computed across replications m=1,…,Mm=1,\dots,M:

* •

  Bias:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Bias:=1M​∑m=1M(x^α(m)−xα⋆,(m)).\mathrm{Bias}:=\frac{1}{M}\sum\_{m=1}^{M}\left(\widehat{x}^{(m)}\_{\alpha}-x\_{\alpha}^{\star,(m)}\right). |  | (56) |
* •

  Variance:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Var:=1M−1​∑m=1M(x^α(m)−x¯α)2,x¯α:=1M​∑m=1Mx^α(m).\mathrm{Var}:=\frac{1}{M-1}\sum\_{m=1}^{M}\left(\widehat{x}^{(m)}\_{\alpha}-\overline{x}\_{\alpha}\right)^{2},\qquad\overline{x}\_{\alpha}:=\frac{1}{M}\sum\_{m=1}^{M}\widehat{x}^{(m)}\_{\alpha}. |  | (57) |
* •

  Mean squared error (MSE):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | MSE:=Bias2+Var.\mathrm{MSE}:=\mathrm{Bias}^{2}+\mathrm{Var}. |  | (58) |
* •

  IS stability diagnostics:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ESS¯:=1M​∑m=1MESS(m),w¯max:=1M​∑m=1Mwmax(m).\overline{\mathrm{ESS}}:=\frac{1}{M}\sum\_{m=1}^{M}\mathrm{ESS}^{(m)},\qquad\overline{w}\_{\max}:=\frac{1}{M}\sum\_{m=1}^{M}w\_{\max}^{(m)}. |  | (59) |

For discrete moment matching, bias, variance, and mean squared error are
reported for the midpoint of the VaR interval solely as descriptive
summaries. These quantities are not interpreted as optimality criteria, as
DMM is designed to produce interval-valued guarantees that quantify
distributional ambiguity rather than point estimates.

### 6.4 Reproducibility Considerations

All random number generators are initialized with fixed seeds at the start of each replication to ensure reproducibility. Within the IS root-finding procedure, common random numbers are used across bisection iterations, as described in Section [5.2](https://arxiv.org/html/2601.09927v1#S5.SS2 "5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"), to stabilize the monotonic behavior of the estimated tail probability.

### 6.5 Interpretation

The simulation design ensures that both estimators operate under identical nominal assumptions and identical Monte Carlo budgets. Any observed differences in bias, variance, or stability therefore reflect structural differences between importance sampling and discrete moment matching, rather than artifacts of unequal calibration or simulation effort.

## 7 Results

This section reports the empirical behavior of the VaR procedures defined in
Section [5](https://arxiv.org/html/2601.09927v1#S5 "5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") under the simulation design of
Section [6](https://arxiv.org/html/2601.09927v1#S6 "6 Simulation Design ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"). The objective is not to compare two estimators of
the same quantity, but to study how two fundamentally different approaches to
tail risk, efficient estimation under a nominal model (importance sampling)
and robust bracketing under moment ambiguity (discrete moment matching), behave
as tail thickness increases.

All performance is evaluated under the heavy-tailed Student-tt data-generating
process described in Section [4](https://arxiv.org/html/2601.09927v1#S4 "4 True Data-Generating Process ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"), while the importance sampling (IS)
procedure remains calibrated to the nominal Gaussian model described in
Section [5.2](https://arxiv.org/html/2601.09927v1#S5.SS2 "5.2 Importance Sampling (IS) via Exponential Tilting and VaR Root-Finding ‣ 5 Value-at-Risk Estimation Methods ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"). Throughout, the loss is defined as L=−RL=-R, and the VaR
level α\alpha corresponds to the (1−α)(1-\alpha) upper tail quantile of LL.

### 7.1 Baseline Behavior Under the Nominal Gaussian Model

As a preliminary validation, both IS and DMM were run under the nominal Gaussian model. In this setting, the closed-form Gaussian VaR provides an exact benchmark. The IS implementation reproduced the nominal Gaussian VaR closely, confirming the correctness of (i) the exponential tilting construction, (ii) likelihood ratio evaluation, and (iii) the bisection root-finding routine used to solve the VaR equation. Numerically, the bisection bracket remained valid throughout iterations, consistent with the monotonicity of the estimated tail probability in the loss threshold when common random numbers are used across bisection steps. This baseline check isolates subsequent performance differences under Student-tt returns as effects of tail misspecification rather than numerical implementation errors.

### 7.2 Bias Under Heavy-Tailed Data-Generating Processes

When returns are generated under Student-tt tails, systematic differences
between the two approaches emerge due to their fundamentally different targets.
For fixed confidence level α\alpha, decreasing the degrees of freedom ν\nu
increases the true VaR xα⋆x^{\star}\_{\alpha}, reflecting heavier tails.

Under these heavy-tailed scenarios, the IS procedure converges efficiently to
the VaR implied by the nominal Gaussian model, which lies below the true VaR
under ℙ⋆\mathbb{P}^{\star}. As a result, the observed negative bias relative to
xα⋆x^{\star}\_{\alpha} reflects structural model misspecification rather than
estimation error. Increasing the Monte Carlo budget reduces variance but cannot
eliminate this bias, as IS continues to target the nominal-model tail
probability rather than the true heavy-tailed tail probability.

Table [1](https://arxiv.org/html/2601.09927v1#S7.T1 "Table 1 ‣ 7.2 Bias Under Heavy-Tailed Data-Generating Processes ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") reports IS mean, standard deviation, and bias relative to the analytically computed Student-tt true VaR for ν∈{5,7,10}\nu\in\{5,7,10\} and α∈{0.990,0.995}\alpha\in\{0.990,0.995\}. The bias is negative in all settings and increases in magnitude as tails become heavier and as α\alpha increases.

Table 1: Importance sampling VaR performance under Student-tt true returns. Bias is defined as Bias=IS​\_​mean−trueVaR\mathrm{Bias}=\mathrm{IS\\_mean}-\mathrm{trueVaR}. ESS denotes the effective sample size proxy computed from normalized weights, and maxW is the maximum normalized weight share.

| ν\nu | α\alpha | trueVaR | IS\_mean | IS\_std | IS\_bias | ESS | maxW |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 0.990 | 0.0281 | 0.0252 | 0.0017 | -0.0029 | 154 | 0.056 |
| 5 | 0.995 | 0.0339 | 0.0283 | 0.0022 | -0.0056 | 91 | 0.081 |
| 7 | 0.990 | 0.0273 | 0.0246 | 0.0013 | -0.0026 | 154 | 0.056 |
| 7 | 0.995 | 0.0320 | 0.0276 | 0.0013 | -0.0044 | 91 | 0.081 |
| 10 | 0.990 | 0.0266 | 0.0249 | 0.0010 | -0.0017 | 154 | 0.056 |
| 10 | 0.995 | 0.0307 | 0.0276 | 0.0009 | -0.0030 | 91 | 0.081 |

### 7.3 Estimator Variability and Efficiency

Importance sampling yields relatively low estimator variability across replications. As shown in Table [1](https://arxiv.org/html/2601.09927v1#S7.T1 "Table 1 ‣ 7.2 Bias Under Heavy-Tailed Data-Generating Processes ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"), IS standard deviations remain below 2.5×10−32.5\times 10^{-3} even at α=0.995\alpha=0.995, and decrease as ν\nu increases (lighter tails). This behavior is consistent with the variance-reduction objective of IS: the change of measure increases the frequency of loss observations near the target tail region under the nominal model, thereby reducing Monte Carlo noise.

By contrast, DMM produces deterministic VaR *intervals* rather than a single point estimate. The width of the interval reflects distributional ambiguity given the enforced moments and the discretization grid. Empirically, the DMM lower bound increases monotonically with the number of enforced raw moments dd, while the upper bound remains nearly constant; hence the interval tightens and stabilizes as dd increases. This tightening pattern is visible in Figure [2](https://arxiv.org/html/2601.09927v1#S7.F2 "Figure 2 ‣ 7.4 Discrete Moment Matching: Bracketing, Sensitivity, and Feasibility ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") and provides a numerical consistency check that additional moment constraints reduce ambiguity.

### 7.4 Discrete Moment Matching: Bracketing, Sensitivity, and Feasibility

Figure [1](https://arxiv.org/html/2601.09927v1#S7.F1 "Figure 1 ‣ 7.4 Discrete Moment Matching: Bracketing, Sensitivity, and Feasibility ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") overlays the empirical loss CDF with the DMM VaR bounds at α=0.99\alpha=0.99. The vertical lines in the plot correspond to the DMM lower and upper VaR bounds computed at the selected moment order (reported in the code as d⋆=7d^{\star}=7) and a Monte Carlo VaR reference line. The figure provides a geometric interpretation of DMM: instead of fitting a parametric tail, the method computes quantile bounds that are compatible with the enforced moment constraints.

![Refer to caption](dmm_bracketing_cdf.png)


Figure 1: Moment-feasible VaR bracketing versus empirical loss CDF at α=0.99\alpha=0.99. The vertical lines indicate the DMM lower and upper VaR bounds at the chosen moment order and the Monte Carlo VaR reference.

Figure [2](https://arxiv.org/html/2601.09927v1#S7.F2 "Figure 2 ‣ 7.4 Discrete Moment Matching: Bracketing, Sensitivity, and Feasibility ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") shows sensitivity of the DMM VaR bounds to the number of enforced moments dd. In the reported experiment, the upper bound remains essentially unchanged while the lower bound increases with dd and stabilizes for moderate values of dd. This is consistent with contraction of the moment-feasible distribution set as additional constraints are imposed.

![Refer to caption](dmm_var_vs_d.png)


Figure 2: Sensitivity of DMM VaR bounds to moment order dd. The lower bound increases with dd and stabilizes, while the upper bound remains nearly constant.

The code additionally reports a feasibility breakdown when enforcing higher
moment orders. Feasibility holds up to d⋆=7d^{\star}=7 and fails for d≥8d\geq 8 in the
reported experiments. This behavior should be interpreted carefully.
For Student-tt distributions with degrees of freedom ν\nu, raw moments of
order r≥νr\geq\nu do not exist. In particular, when ν=5\nu=5, moments above the
fourth order are theoretically undefined.

Consequently, infeasibility at higher moment orders reflects a combination of
theoretical moment nonexistence and numerical ill-conditioning of the truncated
moment problem under discretization. The value d⋆d^{\star} should therefore be
interpreted not as an optimal moment order, but as the largest order for which
the imposed moment constraints remain both theoretically meaningful and
numerically feasible within the chosen grid.

### 7.5 Importance Sampling Stability Diagnostics

Stability diagnostics provide insight into the alignment between the IS change
of measure and the geometry of the rare-event set under the true data-generating
process. In the reported experiments, the effective sample size (ESS) is
substantially smaller than the Monte Carlo budget, with ESS decreasing from
approximately 154154 at α=0.990\alpha=0.990 to approximately 9191 at α=0.995\alpha=0.995
(Table [1](https://arxiv.org/html/2601.09927v1#S7.T1 "Table 1 ‣ 7.2 Bias Under Heavy-Tailed Data-Generating Processes ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing")). At the same time, the maximum normalized weight
share increases as α\alpha rises.

These patterns are characteristic of increasingly rare-event regimes and do
not, by themselves, imply numerical failure. Rather, they indicate that the
Gaussian exponential tilting measure becomes progressively less well aligned
with the true heavy-tailed loss distribution as confidence levels increase.

The diagnostic plots produced by the code are reported in Figures [3](https://arxiv.org/html/2601.09927v1#S7.F3 "Figure 3 ‣ 7.5 Importance Sampling Stability Diagnostics ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") to [7](https://arxiv.org/html/2601.09927v1#S7.F7 "Figure 7 ‣ 7.5 Importance Sampling Stability Diagnostics ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing"). Figure [3](https://arxiv.org/html/2601.09927v1#S7.F3 "Figure 3 ‣ 7.5 Importance Sampling Stability Diagnostics ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") shows that IS mean VaR values fall below the 45∘45^{\circ} line when plotted against the true Student-tt VaR, visually confirming systematic underestimation under tail misspecification. Figure [4](https://arxiv.org/html/2601.09927v1#S7.F4 "Figure 4 ‣ 7.5 Importance Sampling Stability Diagnostics ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") shows that the bias magnitude decreases as ν\nu increases (tails become lighter), consistent with convergence toward Gaussian behavior. Figure [6](https://arxiv.org/html/2601.09927v1#S7.F6 "Figure 6 ‣ 7.5 Importance Sampling Stability Diagnostics ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") summarizes stability degradation as α\alpha increases, and Figure [7](https://arxiv.org/html/2601.09927v1#S7.F7 "Figure 7 ‣ 7.5 Importance Sampling Stability Diagnostics ‣ 7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") highlights that the higher-confidence regime (α=0.995\alpha=0.995) is associated with both lower ESS and larger absolute bias.

![Refer to caption](is_calibration_true_vs_mean.png)


Figure 3: Calibration of IS VaR under Student-tt tails: IS mean VaR versus true VaR. The dashed line is the identity line; points below indicate underestimation.

![Refer to caption](is_bias_vs_nu.png)


Figure 4: IS bias (IS mean minus true VaR) versus degrees of freedom ν\nu. Bias magnitude decreases as tails become lighter.

![Refer to caption](is_std_vs_nu.png)


Figure 5: IS estimator variability (standard deviation across replications) versus degrees of freedom ν\nu.

![Refer to caption](is_stability_vs_alpha.png)


Figure 6: IS stability diagnostics versus confidence level α\alpha. Top: average ESS decreases from ≈154\approx 154 at α=0.990\alpha=0.990 to ≈91\approx 91 at α=0.995\alpha=0.995. Bottom: max weight share increases from ≈0.056\approx 0.056 to ≈0.081\approx 0.081, indicating stronger weight concentration at higher confidence levels.

![Refer to caption](is_tradeoff_absbias_vs_ess.png)


Figure 7: Tradeoff diagnostic: absolute bias versus ESS. The higher-confidence regime exhibits lower ESS and larger absolute bias, reflecting increased rare-event difficulty and tail-model mismatch.

### 7.6 Summary of Findings

Taken together, the empirical results highlight a clear efficiency-robustness
trade-off. Importance sampling delivers low-variance estimates of VaR under the
nominal Gaussian model and exhibits stable numerical behavior across
replications. However, under Student-tt tails, it converges efficiently to the
nominal-model VaR, which systematically understates the true tail risk; the
resulting bias increases with heavier tails and higher confidence levels.

Discrete moment matching exhibits complementary behavior. Rather than producing
a point estimate, DMM yields deterministic VaR bounds that remain valid under
tail misspecification. As additional moment constraints are imposed, the
moment-feasible ambiguity set contracts and the VaR bounds tighten up to a
theoretically and numerically feasible limit. The resulting interval width
provides an explicit measure of distributional uncertainty, avoiding spurious
precision in settings where tail behavior is difficult to specify.

## 8 Discussion

The results of Section [7](https://arxiv.org/html/2601.09927v1#S7 "7 Results ‣ Efficiency versus Robustness under Tail Misspecification: Importance Sampling and Moment-Based VaR Bracketing") highlight a fundamental trade-off in simulation-based Value-at-Risk estimation between computational efficiency and robustness to model misspecification. Although both importance sampling and discrete moment matching aim to improve upon naive Monte Carlo estimation in rare-event settings, they do so through fundamentally different mechanisms, and these differences become most apparent when tail behavior deviates from nominal modeling assumptions.

### 8.1 Efficiency Versus Robustness

Importance sampling is designed to reduce estimator variance by altering the sampling distribution so that rare events occur more frequently. When the nominal model accurately reflects the geometry of extreme losses, this approach can yield substantial efficiency gains. In the present study, importance sampling exhibits low variability and stable root-finding behavior under the Gaussian nominal model, confirming the correctness of the likelihood-ratio construction and numerical implementation.

However, the results demonstrate that variance reduction alone does not guarantee accurate risk estimation under tail misspecification. When the true return distribution exhibits heavier tails than the nominal Gaussian model, importance sampling remains efficient but converges to the *wrong target*: the nominal-model VaR rather than the true VaR under the heavy-tailed data-generating process. This bias is structural and cannot be eliminated by increasing the simulation budget, as it arises from model misspecification rather than Monte Carlo noise.

Discrete moment matching, by contrast, does not rely on a fully specified parametric model. By restricting attention to distributions that satisfy a finite set of moment constraints, DMM explicitly acknowledges distributional ambiguity. As tail thickness increases, this ambiguity manifests as wider VaR intervals, reflecting increased uncertainty rather than spurious precision. Although the resulting estimates are less efficient and more conservative, they exhibit greater robustness to deviations from Gaussian tail behavior.

### 8.2 Interpretation of Stability Diagnostics

Stability diagnostics provide additional insight into the reliability of importance sampling under misspecification. Effective sample size and maximum weight concentration measure the extent to which the estimator is dominated by a small number of weighted observations. In the experiments considered here, these diagnostics remain within acceptable ranges under moderate tail thickness but deteriorate as tails become heavier.

Importantly, weight degeneracy in this setting does not necessarily imply estimator failure in a numerical sense; rather, it serves as an early warning that the change of measure is poorly aligned with the true tail geometry. In practice, such diagnostics should be monitored alongside point estimates, particularly when importance sampling is applied in environments where tail behavior is uncertain or subject to structural breaks.

### 8.3 Implications for Market Risk Estimation

The comparative results suggest that the choice between importance sampling and moment-matching approaches should be guided by the degree of confidence in the assumed tail model. When the nominal model is believed to be approximately correct and computational efficiency is paramount, importance sampling provides a powerful tool for rare-event estimation. Conversely, when tail behavior is uncertain or potentially heavy-tailed, moment-based approaches offer a more cautious alternative that trades efficiency for robustness.

In applied risk management settings, this distinction is particularly relevant. Regulatory and internal risk measures are often computed under simplifying assumptions that may not hold during periods of market stress. The present results indicate that reliance on variance-reduction techniques alone may lead to underestimation of extreme risk if model misspecification is not explicitly addressed.

### 8.4 Limitations

The present study adopts a deliberately controlled framework in order to
isolate the efficiency–robustness trade-off between importance sampling and
moment-based VaR bracketing under tail misspecification. As a result, several
dimensions of practical risk modeling are intentionally abstracted from. First, the analysis is restricted to a univariate return setting, and the behavior of both estimators in high-dimensional portfolio contexts may differ. Second, the discrete moment matching procedure depends on the choice of loss grid and the order of moments enforced; alternative grid constructions or higher-order moments may yield different bounds. Third, the importance sampling scheme considered here is limited to simple exponential tilting of a Gaussian model; more sophisticated proposal distributions may mitigate some of the observed bias under misspecification.

Finally, while discrete moment matching yields interval-valued VaR outputs
that naturally quantify distributional ambiguity, the present study does not
address how such intervals should be translated into single capital charges
in regulatory or operational settings. Developing principled decision rules
that map ambiguity intervals into actionable risk measures remains an
important direction for future research.

## 9 Conclusion

This paper studied the performance of two simulation-based approaches to Value-at-Risk estimation, importance sampling and discrete moment matching, under controlled tail misspecification. By separating the nominal model used for estimator construction from the true data-generating process used for evaluation, the analysis isolated the impact of heavy-tailed behavior on estimator bias, variability, and numerical stability.

The results demonstrate that importance sampling, while highly efficient under correct model specification, is sensitive to misspecification of tail behavior. In heavy-tailed environments, importance sampling converges efficiently to the VaR implied by the nominal Gaussian model, which can substantially underestimate the true risk. Stability diagnostics such as effective sample size and weight concentration provide useful indicators of this mismatch but do not eliminate the underlying structural bias.

Discrete moment matching exhibits complementary behavior. By restricting attention to distributions consistent with a finite set of moment constraints, DMM produces conservative VaR estimates that remain robust under heavy-tailed data-generating processes. This robustness comes at the cost of reduced efficiency and wider uncertainty intervals, reflecting the intrinsic ambiguity associated with limited distributional information.

Taken together, these findings underscore that variance reduction alone is not sufficient for reliable tail risk estimation in the presence of model uncertainty. The choice of VaR estimation methodology should therefore reflect not only computational considerations but also the degree of confidence in the assumed tail model. In settings where tail behavior is difficult to specify or subject to structural change, moment-based approaches may offer a safer alternative to aggressively optimized importance sampling schemes.

Future work may extend this analysis to higher-dimensional portfolio settings, alternative importance sampling proposals, and dynamic models of volatility and tail risk. Nonetheless, the present study provides a transparent and reproducible framework for understanding the efficiency–robustness trade-off inherent in simulation-based VaR estimation.

## References