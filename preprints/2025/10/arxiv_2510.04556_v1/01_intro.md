---
authors:
- Alexej Brauer
- Paul Menzel
doc_id: arxiv:2510.04556v1
family_id: arxiv:2510.04556
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Gini-based Model Monitoring: A General Framework with an Application to Non-life
  Insurance Pricing'
url_abs: http://arxiv.org/abs/2510.04556v1
url_html: https://arxiv.org/html/2510.04556v1
venue: arXiv q-fin
version: 1
year: 2025
---


\fnmAlexej \surBrauer \orcidhttps://orcid.org/0009-0009-4001-016X
[brauer.alexej@gmail.com](mailto:brauer.alexej@gmail.com)
  
\fnmPaul \surMenzel
[paul.menzel@tum.de](mailto:paul.menzel@tum.de)
[

###### Abstract

In a dynamic landscape where portfolios and environments evolve,
maintaining the accuracy of pricing models is critical.
To the best of our knowledge, this is the first study to systematically examine
concept drift in non-life insurance pricing.
We (i) provide an overview of the relevant literature and commonly used
methodologies, clarify the distinction between virtual drift and concept drift,
and explain their implications for long-run model performance; (ii) review and
formalize common performance measures, including the Gini index and deviance
loss, and articulate their interpretation; (iii) derive the asymptotic
distribution of the Gini index, enabling valid inference and hypothesis
testing; and (iv) present a standardized monitoring procedure that indicates
when refitting is warranted.
We illustrate the framework using a modified real-world portfolio with induced
concept drift and discuss practical considerations and pitfalls.

###### keywords:

non-life insurance, concept drift, model monitoring, gini

11footnotetext: Author Contribution: A. Brauer led conceptualization, framework design, methodology,
software implementation,
investigation, most visualizations, and manuscript drafting, and contributed to
the formal asymptotic analysis; P. Menzel led the formal asymptotic analysis
and contributed to software, methodology, one visualization, and manuscript
revision; both authors performed validation, critical review, and approved the
final manuscript.

Statements and Declarations:

Competing Interests:
The authors have no conflicts of interest to declare that are relevant to the
content of this article.

## 1 Introduction

In non-life insurance pricing, common tasks include predicting claim frequency,
estimating claim severity, and modeling binary demand outcomes such as
conversion prediction.
Maintaining the accuracy of those models over time is a critical challenge in a
dynamic landscape of evolving portfolios and market conditions.
In this context, two key terms are often encountered: model monitoring
and model comparison.
These two terms are frequently used in the actuarial context of developing
pricing models.
The term model monitoring, also referred to as backtesting,
pertains to testing a single model on at least two different datasets.
This can occur either during the development phase, using training and
validation/holdout data, or during the monitoring phase, using holdout data
from the model update period versus new data from the current period.
In contrast, model comparison is the process of comparing two
different models on the same dataset to determine which one performs better.
A schematic representation of both terms is given in Fig.
[1](https://arxiv.org/html/2510.04556v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").

![Refer to caption](x1.png)


Figure 1: Schematic representation of the Model Monitoring (left)
and Model Comparison Framework (right).
To visually distinguish datasets, the Apache Parquet logo color has been
modified from its original design.
The Apache Parquet logo is a trademark of the Apache Software Foundation.

In this work, we focus on model monitoring, which is often underemphasized
in the actuarial literature yet is crucial for updating and maintaining
pricing models over time.
To the best of our knowledge, this is the first study to explicitly examine
data drift in insurance pricing models; accordingly, we provide an overview of
the relevant literature and a monitoring framework tailored to actuarial
pricing practice.
In contrast, model comparison is a more static process, typically
performed during development to select the best model from a set of candidates
(e.g., different covariates, hyperparameters, or algorithms).
  
  
However, when many models are in use, maintaining them can be very
time-consuming and costly.
And more importantly, a complete refitting of a pricing model often leads to
changes in the feature contributions of the different risk factors due to the
inherent correlation between the covariates in the training data and in smaller
models due to statistical noise.
  
This can lead to significant changes in the pricing of individual policies,
particularly for segments that are not well-represented in the training data.
Such changes are often undesirable from a business perspective, as they can
lead to unstable pricing and dissatisfaction among customers.
  
  
For this reason, model updates are often performed on a fixed time schedule,
such as every one or two years, rather than being based on performance metrics.
This, however, can lead to unnecessary updates and a suboptimal cost-benefit
ratio in the model update process, as time might have been better spent on
updating another model.
Moreover, performing updates on a fixed time schedule can result in slow
adaptation to changing market environments.
  
  
Therefore, this work concentrates on the model monitoring aspect.
We establish the theoretical foundations for key evaluation metrics, notably
deriving an asymptotic distribution for the sample Gini index.
Based on this, we introduce a framework for assessing and monitoring the
temporal robustness of non-life insurance pricing models to guide decisions on
model refitting.
For practical applicability, we present an illustrative example based on a
modified real-world dataset in which we inject controlled levels of concept
drift and discuss practical considerations and common pitfalls for real-world
implementation.

### 1.1 Organization of this manuscript

In Sect.
[2](https://arxiv.org/html/2510.04556v1#S2 "2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), we outline the theoretical background, review the relevant literature, and discuss virtual drift and real concept drift (see Sect. [2.1](https://arxiv.org/html/2510.04556v1#S2.SS1 "2.1 Virtual-Drift and Concept-Drift ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")).
Sect.
[2.2](https://arxiv.org/html/2510.04556v1#S2.SS2 "2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") develops the theoretical foundations, covering auto-calibration, evaluation metrics and their properties, and derives the asymptotic distribution of the sample Gini index.
Sect.
[3](https://arxiv.org/html/2510.04556v1#S3 "3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") introduces a hypothesis-testing framework for monitoring models over time, detailed in Sect. [3.1](https://arxiv.org/html/2510.04556v1#S3.SS1 "3.1 General Framework for Model Monitoring ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
Sect.
[3.2](https://arxiv.org/html/2510.04556v1#S3.SS2 "3.2 Illustration example ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") illustrates the framework using a modified real-world insurance dataset, and Sect. [3.3](https://arxiv.org/html/2510.04556v1#S3.SS3 "3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") discusses practical considerations and common pitfalls.
Finally, Sect.
[4](https://arxiv.org/html/2510.04556v1#S4 "4 Conclusion ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") concludes with a discussion and an outlook on future work.

## 2 Theoretical Background and Related Work

This section establishes the foundational concepts, definitions, and notation
used throughout the paper.
Unless specified otherwise: We assume a sufficiently rich probability space
(Ω,𝒜,ℙ)(\Omega,\mathcal{A},\mathbb{P}) that supports all objects used in this
manuscript.
Random variables on this space are denoted by uppercase letters, e.g., XX,
with their realizations in lowercase, e.g., xx.
As a convention, we use bold uppercase letters to represent random vectors and
lowercase bold letters for their realizations.
For instance, we denote a random vector by 𝐗=(X1,X2,…,Xm)⊤\mathbf{X}=(X\_{1},X\_{2},\dots,X\_{m})^{\top}, and its realization by 𝐱=(x1,x2,…,xm)⊤\mathbf{x}=(x\_{1},x\_{2},\dots,x\_{m})^{\top}, where m∈ℕm\in\mathbb{N}.
We denote the cumulative distribution function (cdf) for a real-valued random
vector 𝐗\mathbf{X}, by F𝐗F\_{\mathbf{X}}.
  
As is common in regression modelling, we consider a random pair (Y,𝐗)(Y,\mathbf{X})
on the probability space introduced above, where YY is a non‑negative
real-valued response with finite mean and 𝐗\mathbf{X} denotes the covariate
vector.
Following the notation in [[31](https://arxiv.org/html/2510.04556v1#bib.bib31)], we denote the family of
potential distributions of (Y,𝐗)(Y,\mathbf{X}) as ℱ\mathcal{F}, the conditional
cdf of YY given 𝐗\mathbf{X} as FY∣𝐗F\_{Y\mid\mathbf{X}} and the conditional
mean functional TT as

|  |  |  |  |
| --- | --- | --- | --- |
|  | FY∣𝐗↦T(FY∣𝐗)=𝔼[Y|𝐗]=:μ†(𝐗).F\_{Y\mid\mathbf{X}}\mapsto T(F\_{Y\mid\mathbf{X}})=\mathbb{E}[Y|\mathbf{X}]=:\mu^{\dagger}(\mathbf{X}). |  | (1) |

The main goal in supervised learning is to estimate this true regression
function μ†​(⋅)\mu^{\dagger}(\cdot) from a given dataset DD of realizations.
We denote this estimator by μ^​(⋅)\hat{\mu}(\cdot).
  
We consider here the following notation for datasets D={(yi,𝐱i,vi)}i=1nD={\{\left(y\_{i},\mathbf{x}\_{i},v\_{i}\right)\}}\_{i=1}^{n}, comprising nn observations.
For each observation ii, yiy\_{i} is the response variable, 𝐱i\mathbf{x}\_{i} is a
kk-dimensional vector of covariates, and vi>0v\_{i}>0 represents the exposure.
The elements in the covariate vector 𝐱i\mathbf{x}\_{i} can be either numerical or
categorical.
Throughout this paper, we use i∈{1,…,n}i\in\{1,\ldots,n\} to index observations and
j∈{1,…,k}j\in\{1,\ldots,k\} to index covariates, unless specified otherwise.

### 2.1 Virtual-Drift and Concept-Drift

The usual assumption in statistics is that we draw our data from
i.i.d.\mathrm{i.i.d.} random tuples (Yi,𝐗i)(Y\_{i},\mathbf{X}\_{i}), i∈{1,…,n}i\in\{1,\ldots,n\},
having the same distribution as (Y,𝐗)(Y,\mathbf{X}).
The common further assumption is that the data-generating process is
stationary, i.e., that the distribution of (Y,𝐗)(Y,\mathbf{X}) does not change
over time.
In non-life insurance modeling, one often trains a model on data from a given
period (e.g., years 2020-2023) and assumes this data is under global trend
assumptions representative of a later period (e.g., 2025), when the model will
be used in production.
However, while this assumption is typically reasonable when comparing training
and holdout datasets drawn from the same period, it is frequently violated in
production datasets due to changes in the underlying population, customer
behavior, the data-collection process, and — last but not least — the
real-world environment.
  
  
Related Work History: Detecting changes in the underlying data-generating process has been studied
extensively for decades (see, e.g., [[27](https://arxiv.org/html/2510.04556v1#bib.bib27), [29](https://arxiv.org/html/2510.04556v1#bib.bib29)]) and
remains an active area of research.
Although work evolves in parallel across several communities, a key
consolidation is provided by the survey articles [[13](https://arxiv.org/html/2510.04556v1#bib.bib13)] and
[[19](https://arxiv.org/html/2510.04556v1#bib.bib19)], which systematize methods, clarify definitions (e.g.,
virtual vs.
real concept drift), and summarize the
state of the art up to 2014 and 2019, respectively.
We adopt their terminology in what follows.
  
More recent advances and surveys include: for scenarios where data labeling is
challenging, see, e.g., [[1](https://arxiv.org/html/2510.04556v1#bib.bib1)]; for neural
networks, see, e.g., the survey [[24](https://arxiv.org/html/2510.04556v1#bib.bib24)]; for data drift
detection in large-scale systems, see [[20](https://arxiv.org/html/2510.04556v1#bib.bib20)]; and more
recently for drift detection using deep neural networks and autoencoders, see
[[16](https://arxiv.org/html/2510.04556v1#bib.bib16)].
For a formulation of drift as a distribution process and a survey of the
literature on unsupervised drift detection, the authors refer to
[[14](https://arxiv.org/html/2510.04556v1#bib.bib14)].
  
  
Terminology: Because the terminology is more prevalent in the machine learning community—for
example, in online learning of classification tasks, and process mining —and less so in actuarial science,
we provide a brief overview of the terminology in an actuarial context.
  
As [[13](https://arxiv.org/html/2510.04556v1#bib.bib13)] describe in their survey, the literature uses many
different terms to refer to changes in the data-generating process over time.
Common expressions include data drift, covariate shift,
virtual shift, temporary drift, sampling shift,
feature change, concept drift, conditional change
and real concept drift.
We also note that terminology is not used consistently across the literature.
  
For consistency, we follow the definitions of [[13](https://arxiv.org/html/2510.04556v1#bib.bib13)] and
distinguish two main types of drift: virtual drift and
real concept drift.
Here, virtual drift refers to changes in the distribution of the
features 𝐗\mathbf{X}, i.e., F𝐗F\_{\mathbf{X}}, and, importantly, occurs without
changing the conditional distribution FY∣𝐗F\_{Y\mid\mathbf{X}}; thus the true
regression function μ†​(𝐗)\mu^{\dagger}(\mathbf{X})
([1](https://arxiv.org/html/2510.04556v1#S2.E1 "In 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")) remains unchanged.
By contrast, real concept drift refers to changes in the conditional
distribution FY∣𝐗F\_{Y\mid\mathbf{X}} and thus in the true regression function
μ†​(𝐗)\mu^{\dagger}(\mathbf{X}).
Notably, this change in the conditional distribution can occur with or without
a change in F𝐗F\_{\mathbf{X}}.
Table [1](https://arxiv.org/html/2510.04556v1#S2.T1 "Table 1 ‣ 2.1 Virtual-Drift and Concept-Drift ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") summarizes the definitions and common
alternative names for virtual drift and real concept drift
used in the literature.

Table 1: virtual drift and the real concept drift:

|  |  |  |
| --- | --- | --- |
|  | virtual drift | real concept drift |
| Definition | Changes in F𝐗F\_{\mathbf{X}} | Changes in FY∣𝐗F\_{Y\mid\mathbf{X}} |
|  | without changing FY∣𝐗F\_{Y\mid\mathbf{X}} |  |
| Also called | data drift, | data drift, |
| in literature | virtual shift, | conditional change, |
| sometimes | temporary drift, | concept drift, |
|  | sampling shift, |  |
|  | feature change |  |
|  | covariate shift |  |

Furthermore, we refer to changes in the distribution of the features
F𝐗F\_{\mathbf{X}} as covariate drift; note that this can result in
either virtual drift or real concept drift.
  
  
The authors acknowledge that detecting virtual drift is very important in
the insurance industry for understanding how the portfolio evolves over time.
However, our interest lies in changes in predictive performance over time and
in identifying when a model should be updated; accordingly, we restrict
attention to real concept drift rather than virtual drift.
The phenomenon in which the predictive performance of a deployed model degrades
over time is often referred to in the literature as model drift.
  
  
While we now establish the different drift terms,
it is important to note, that even if only a virtual drift occurs
(i.e., no change in the true regression function μ†​(𝐗)\mu^{\dagger}(\mathbf{X})),
there can still be an actual change in the performance of the estimator
of the regression function (i.e., the model μ^​(𝐗)\hat{\mu}(\mathbf{X})).
This is because the model μ^​(𝐗)\hat{\mu}(\mathbf{X}) may not be trained on a
sufficiently rich data set and thus may not generalize well.
If the exposure of new data increases in regions where the model performs
poorly, its performance will degrade.
While insufficient data coverage is an important issue, in the following
theoretical section we focus on real concept drift and therefore
assume that the model is trained on a sufficiently large data set.
  
  
Real Concept Drift Types: There are typically 4 types of reasons
distinguished for real concept drift
discussed in the literature.
These are sudden or abrupt drift, gradual drift,
incremental drift, and recurrent drift (see
[[19](https://arxiv.org/html/2510.04556v1#bib.bib19)] for a comprehensive overview and visualization).
In this manuscript, we focus on the first three types of drift.
  
  
Concept Drift Detection Method Types:
There are several methods for detecting real concept drift that can be broadly
categorized into the following four main families.
These are:

* •

  Data Distribution-based Methods:
  Typical examples of such methods involve computing distribution distance
  measures such as Kolmogorov-Smirnov, Wasserstein metric, Kullback-Leibler divergence
  and Jensen-Shannon metric between the old data and the new
  data.
  See, for example, Section 4.3 of [[14](https://arxiv.org/html/2510.04556v1#bib.bib14)].
* •

  Dimensionality Reduction-Based Methods:
  Another common approach is to compare reconstruction errors obtained via PCA or
  autoencoders.
  Furthermore, domain classifier approaches are often used in this context, in
  which one trains a classifier to distinguish between old and new data.
  If the classifier performs well, it indicates a significant difference between
  the two distributions, suggesting the presence of covariate drift.
  See, for example, [[24](https://arxiv.org/html/2510.04556v1#bib.bib24)].
* •

  Error Rate-Based Methods: These algorithms
  are typically used for classification tasks and are designed to monitor a
  predictive model’s performance across time windows.
  When a statistically significant change in the error rate is detected, a drift
  alarm is triggered.
  Very influential examples include the Drift Detection Method (DDM)
  [[12](https://arxiv.org/html/2510.04556v1#bib.bib12)], the Statistical Test of Equal Proportions (STEPD)
  [[22](https://arxiv.org/html/2510.04556v1#bib.bib22)], and the Adaptive Windowing (ADWIN)
  [[2](https://arxiv.org/html/2510.04556v1#bib.bib2)].
* •

  Multiple Hypothesis Methods:
  These drift detection methods combine multiple different algorithms either in parallel
  or in a hierarchical manner to detect drift.
  See, for example, Section 3.2.3 in [[19](https://arxiv.org/html/2510.04556v1#bib.bib19)].

The approach in this manuscript follows the tradition of the error rate-based
methods DDM and STEPD but adapts it from classification to regression in
insurance: instead of traditional classification error measures, we monitor the
Gini index for non-classification tasks and derive its asymptotic properties to
enable statistical tests.

### 2.2 Auto-Calibration, Metrics and their Properties

Since auto-calibration is a crucial requirement for our monitoring framework
and the upcoming asymptotic proof, we first define it in Section
[2.2.1](https://arxiv.org/html/2510.04556v1#S2.SS2.SSS1 "2.2.1 Auto-Calibration ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
Furthermore, given its popularity in the actuarial literature, we briefly
describe the deviance loss and highlight its key limitations for model
monitoring.
We then introduce the Gini index in Section [2.2.3](https://arxiv.org/html/2510.04556v1#S2.SS2.SSS3 "2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), on which we
build our monitoring framework.

#### 2.2.1 Auto-Calibration

We require the auto-calibration property for our monitoring framework.
Like described in [[17](https://arxiv.org/html/2510.04556v1#bib.bib17)] and
[[33](https://arxiv.org/html/2510.04556v1#bib.bib33)], we define it as follows:

###### Definition 1 (Auto-Calibration).

A random variable ZZ is an auto-calibrated forecast of a random variable YY if

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y∣Z]=Z​a.s..\mathbb{E}[Y\mid Z]=Z\quad\text{a.s.}. |  |

Furthermore, a regression function μ^​(⋅)\hat{\mu}(\cdot) is called auto-calibrated for YY if

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^​(𝐗)=𝔼​[Y∣μ^​(𝐗)]​a.s..\hat{\mu}(\mathbf{X})=\mathbb{E}[Y\mid\hat{\mu}(\mathbf{X})]\quad\text{a.s.}. |  | (2) |

In insurance pricing, auto-calibration is a valuable property of a regression
function, as pointed out by [[31](https://arxiv.org/html/2510.04556v1#bib.bib31)], because it ensures that
each price cohort μ^​(𝐗)\hat{\mu}(\mathbf{X}) is, on average, self‑financing; that
is, μ^​(𝐗)\hat{\mu}(\mathbf{X}) covers the cohort’s expected claims, thus avoiding
cross‑financing.
Another valuable implication of auto-calibration is that it ensures the
regression function μ^​(⋅)\hat{\mu}(\cdot) is unbiased at the portfolio level,
which is a minimal requirement for insurance pricing.
  
  
It follows from the definition of μ†​(⋅)\mu^{\dagger}(\cdot) (see [1](https://arxiv.org/html/2510.04556v1#S2.E1 "In 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")) and the tower rule, the
true regression function μ†​(𝐗)=𝔼​[Y∣𝐗]\mu^{\dagger}(\mathbf{X})=\mathbb{E}[Y\mid\mathbf{X}]
is an auto‑calibrated forecast of YY.
  
  
Furthermore, it is important to emphasize that, in general, neither modern
machine learning methods nor the industry‑standard GLMs are auto‑calibrated or
unbiased at the portfolio level.
  
However, when using the canonical link function, we can ensure unbiasedness at
the portfolio level for GLMs (see e.g.
Proposition 4.1 in [[6](https://arxiv.org/html/2510.04556v1#bib.bib6)]).
  
To assess auto-calibration in practice, one may test whether the empirical
concentration and Lorenz curves coincide, which (for unbiased estimators) is
equivalent to testing auto-calibration (see Section 4 of
[[10](https://arxiv.org/html/2510.04556v1#bib.bib10)]).
In the case of a discrete, finite regression function, one can also apply one
of the three test statistics with known asymptotic distributions under
auto-calibration proposed by [[32](https://arxiv.org/html/2510.04556v1#bib.bib32)].
These procedures detect systematic deviations of predictions from observed
outcomes across different segments of the data.
  
To improve the model’s calibration, one can apply a transformation to
the model prediction.
By doing so, we define the balance-corrected version of the prediction
μ^B​C​(⋅)\hat{\mu}\_{BC}(\cdot) as μ^B​C​(𝐗)=𝔼​[Y|μ^​(𝐗)]\hat{\mu}\_{BC}(\mathbf{X})=\mathbb{E}[Y|\hat{\mu}(\mathbf{X})] (see Section 5.1 in [[9](https://arxiv.org/html/2510.04556v1#bib.bib9)]
and Remarks 7.18 in [[33](https://arxiv.org/html/2510.04556v1#bib.bib33)]).
This transformation helps restore the auto-calibration property, ensuring that
the estimator remains reliable and accurate across varying data conditions.

#### 2.2.2 Deviance loss

Given the popularity of generalized linear models (GLMs)
[[21](https://arxiv.org/html/2510.04556v1#bib.bib21)] in the insurance industry, the deviance loss is
widely used as a loss measure in the non‑life insurance literature for
model comparison.
This also holds beyond the GLM framework; see, e.g.,
[[33](https://arxiv.org/html/2510.04556v1#bib.bib33), [25](https://arxiv.org/html/2510.04556v1#bib.bib25), [4](https://arxiv.org/html/2510.04556v1#bib.bib4), [15](https://arxiv.org/html/2510.04556v1#bib.bib15), [26](https://arxiv.org/html/2510.04556v1#bib.bib26)].
  
  
Since these terms are sometimes confused,
we briefly clarify the difference between the deviance and the deviance loss.
The deviance is usually defined in the GLM framework as the following
difference between two log-likelihoods.

###### Definition 2 (Deviance).

The deviance is then defined as the following difference between the log-likelihoods:

|  |  |  |
| --- | --- | --- |
|  | D¯​(y,y^)=2​φ​[ℓ​(𝜷^max)−ℓ​(𝜷^)].\displaystyle\bar{D}(y,\hat{y})=2\varphi[\ell(\hat{\boldsymbol{\beta}}\_{\max})-\ell(\hat{\boldsymbol{\beta}})]. |  |

Where φ\varphi is the dispersion parameter and ℓ​(⋅)\ell(\cdot) denotes the
log-likelihood of the chosen GLM family.
Here ℓ​(𝜷^max)\ell(\hat{\boldsymbol{\beta}}\_{\max}) denotes the log-likelihood of the
saturated model, and ℓ​(𝜷^)\ell(\hat{\boldsymbol{\beta}}) denotes the
log-likelihood of the model of interest.

The deviance loss, in turn, can be defined as a scaled version of the deviance:

###### Definition 3 (Deviance loss).

|  |  |  |
| --- | --- | --- |
|  | D​(y,y^)=1n​φ​D¯​(y,y^),\displaystyle D(y,\hat{y})=\frac{1}{n\varphi}\bar{D}(y,\hat{y}), |  |

where nn is the number of observations.

Typically, the deviance loss is preferred for model comparison over
the deviance because the latter scales with the number of observations.
Another way to express the deviance loss is as a weighted sum of unit deviances
(see Equations (4.8) and (4.9) in [[33](https://arxiv.org/html/2510.04556v1#bib.bib33)]).

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(y,y^)=1n​∑i=1nviφ​d​(yi,y^i)\displaystyle D(y,\hat{y})=\frac{1}{n}\sum\_{i=1}^{n}\frac{v\_{i}}{\varphi}d(y\_{i},\hat{y}\_{i}) |  | (3) |

Here, the unit deviance can be interpreted as a statistic that quantifies the
discrepancy between the prediction y^i\hat{y}\_{i} and the actual observation
yiy\_{i}.
See Chapter 4 in [[33](https://arxiv.org/html/2510.04556v1#bib.bib33)] for more details and examples
regarding the different underlying distributions.
  
  
The deviance loss is an important statistic for GLMs because maximizing the
likelihood function corresponds to minimizing the deviance loss (see Corollary
4.5 in [[33](https://arxiv.org/html/2510.04556v1#bib.bib33)]).
Moreover, it is a strictly consistent scoring function that measures how well
the model fits the data relative to the saturated model.
  
  
However, although very useful for model comparison, the deviance loss
has several disadvantages when used for model monitoring:

* •

  First, it is sensitive to outliers, which can trigger false alarms when tracking model performance over time.
* •

  Second, it lacks an absolute scale; its magnitude is not directly interpretable across datasets.
* •

  Third, it is, in practice, highly sensitive to differences in the data preparation process between datasets.
  While this is usually not limiting for model comparison, where the
  same dataset and data preparation are used for all models, it is undesirable
  for model monitoring.
  See also Pitfall B in Section [3.3](https://arxiv.org/html/2510.04556v1#S3.SS3 "3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") for a
  commonly underestimated change in the deviance due to data preparation.

For this reason, we instead advocate the Gini index as the primary metric in
the following monitoring framework.

#### 2.2.3 Gini Index

The Gini index is a rank-based metric that quantifies how well a model
discriminates between different outcomes.
It is popular in the machine learning community for model comparison.
In the actuarial community, however, it is less widely used, partly because it
is, in general, not a strictly consistent scoring function; optimizing it
(i.e., maximizing it) does not necessarily lead to the best model in regards to
the true regression function μ†​(𝐗)\mu^{\dagger}(\mathbf{X}).
Our decision to use the Gini index as a monitoring measure is inspired by the
results of [[10](https://arxiv.org/html/2510.04556v1#bib.bib10)] and [[31](https://arxiv.org/html/2510.04556v1#bib.bib31)], where the
former provides a framework for detecting auto-calibration and the latter shows
that the Gini index is a strictly consistent scoring function within the class
of auto-calibrated regression models.
We follow the notation and definitions of [[31](https://arxiv.org/html/2510.04556v1#bib.bib31)].
  
  
Before defining the Gini index, we note that there is not only one definition
in the literature.
For example, in [[10](https://arxiv.org/html/2510.04556v1#bib.bib10)] the Gini index is defined purely via
the Lorenz curve, which depends only on the predictions and not on the response
variable YY.
This definition is popular and widely used in economics.
In [[15](https://arxiv.org/html/2510.04556v1#bib.bib15)], a version of the Gini index is provided to
compare tariff structures between two models by evaluating their respective
Lorenz curves.
However, in the machine learning community, the Gini index is commonly defined
via the Cumulative Accuracy Profile (CAP) curve.
The CAP curve depends on both the predictions μ^​(𝐗)\hat{\mu}(\mathbf{X}) and the
response variable YY.
We use the latter definition in this manuscript.
An overview of the different definitions and their relationships under
autocalibration is given in [[31](https://arxiv.org/html/2510.04556v1#bib.bib31)].
  
  
We begin by introducing the CAP.

###### Definition 4 (Cumulative accuracy profile).

Let α∈(0,1)\alpha\in(0,1).
The CAP is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CAPY,μ^​(𝐗)⁡(α):=1𝔼​[Y]​𝔼​[Y​𝟙{μ^​(𝐗)>Fμ^​(𝐗)−1​(1−α)}]∈[0,1].\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha):=\frac{1}{\mathbb{E}[Y]}\mathbb{E}\left[Y\mathbbm{1}\_{\left\{\hat{\mu}(\mathbf{X})>F^{-1}\_{\hat{\mu}(\mathbf{X})}(1-\alpha)\right\}}\right]\in[0,1]. |  | (4) |

Where μ^​(𝐗)\hat{\mu}(\mathbf{X}) is assumed to have a continuous distribution
function Fμ^​(𝐗)F\_{\hat{\mu}(\mathbf{X})} for all (Y,𝐗)∼F∈ℱ(Y,\mathbf{X})\sim F\in\mathcal{F}.
Furthermore, Fμ^​(𝐗)−1F^{-1}\_{\hat{\mu}(\mathbf{X})} denotes the left-continuous
inverse of Fμ^​(𝐗)F\_{\hat{\mu}(\mathbf{X})}.

Note that the concentration curve CC\operatorname{CC}, which is more popular in the insurance community
(see Definition 3.1 in [[8](https://arxiv.org/html/2510.04556v1#bib.bib8)]), is related to the CAP via
CAPY,μ^​(𝐗)⁡(α)=1−CCY,μ^​(𝐗)⁡(1−α)\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha)=1-\operatorname{CC}\_{Y,\hat{\mu}(\mathbf{X})}(1-\alpha).

###### Definition 5 (Gini index).

Using the CAP, the Gini index GY,μ^​(𝐗)G\_{Y,\hat{\mu}(\mathbf{X})} is defined for
μ^​(𝐗)\hat{\mu}(\mathbf{X}) and YY, assuming they have continuous distribution
functions Fμ^​(𝐗)F\_{\hat{\mu}(\mathbf{X})}
and FYF\_{Y}, respectively, as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | GY,μ^​(𝐗):=∫01CAPY,μ^​(𝐗)⁡(α)​𝑑α−12∫01CAPY,Y⁡(α)​𝑑α−12.G\_{Y,\hat{\mu}(\mathbf{X})}:=\frac{\int\_{0}^{1}\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha)\,d\alpha-\frac{1}{2}}{\int\_{0}^{1}\operatorname{CAP}\_{Y,Y}(\alpha)\,d\alpha-\frac{1}{2}}. |  | (5) |

Analogously to [[31](https://arxiv.org/html/2510.04556v1#bib.bib31)], we provide a geometric visualization
of the two CAP curves and the areas corresponding to the integrals in Figure
[2](https://arxiv.org/html/2510.04556v1#S2.F2 "Figure 2 ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") and Equation ([6](https://arxiv.org/html/2510.04556v1#S2.E6 "In 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")).

![Refer to caption](GeometricInterpretationGini.png)


Figure 2: Geometric visualization of the Gini index.

In Figure [2](https://arxiv.org/html/2510.04556v1#S2.F2 "Figure 2 ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") the curve
CAPY,μ^​(𝐗)⁡(α)\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha) is referred to as the CAP
curve, and CAPY,Y⁡(α)\operatorname{CAP}\_{Y,Y}(\alpha) is referred to as the Best CAP curve, for all
α∈(0,1)\alpha\in(0,1).
The integral from 0 to 1 of CAPY,μ^​(𝐗)⁡(α)\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha) equals the
area under the CAP curve, i.e. the sum of areas A+CA+C.
Similarly, the integral from 0 to 1 of CAPY,Y⁡(α)\operatorname{CAP}\_{Y,Y}(\alpha) equals the area
under the Best CAP curve, i.e. the sum of areas A+B+CA+B+C.
Using these interpretations and the fact that area C=12C=\tfrac{1}{2},
we obtain the geometric interpretation of the Gini index:

|  |  |  |  |
| --- | --- | --- | --- |
|  | GY,μ^​(𝐗)=∫01CAPY,μ^​(𝐗)⁡(α)​𝑑α−12∫01CAPY,Y⁡(α)​𝑑α−12=A+C−CA+B+C−C=AA+B.\displaystyle G\_{Y,\hat{\mu}(\mathbf{X})}=\frac{\int\_{0}^{1}\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha)d\alpha-\frac{1}{2}}{\int\_{0}^{1}\operatorname{CAP}\_{Y,Y}(\alpha)d\alpha-\frac{1}{2}}=\frac{A+C-C}{A+B+C-C}=\frac{A}{A+B}. |  | (6) |

  
  

Asymptotic Normality of the Gini Index:
Because the Gini index will be used in our monitoring framework, it is of
practical importance to understand its distribution.
An asymptotic normality result for the economic Gini index is provided by
Section 3 in [[7](https://arxiv.org/html/2510.04556v1#bib.bib7)].
This inspired us to prove the asymptotic normality of the machine learning Gini
defined in Definition [5](https://arxiv.org/html/2510.04556v1#Thmdefinition5 "Definition 5 (Gini index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
We first state the theorem and then provide the proof.

###### Theorem 1 (Asymptotic Normality of the Gini Index).

Assume (Yi,𝐗i)∼F∈ℱ(Y\_{i},\mathbf{X}\_{i})\sim F\in\mathcal{F} i.i.d.\mathrm{i.i.d.} and let μ^​(⋅)\hat{\mu}(\cdot) be an auto-calibrated estimator.
Suppose 𝔼​[Y]<∞\mathbb{E}[Y]<\infty and 𝔼​[μ^​(𝐗)]<∞\mathbb{E}[\hat{\mu}(\mathbf{X})]<\infty.
Further assume that YY and μ^​(𝐗)\hat{\mu}(\mathbf{X}) have continuous
distribution functions FYF\_{Y} and Fμ^​(𝐗)F\_{\hat{\mu}(\mathbf{X})}, respectively.
Let the combined distribution function of (Y,μ^​(𝐗))(Y,\hat{\mu}(\mathbf{X})) be
denoted by FY,μ^​(𝐗)F\_{Y,\hat{\mu}(\mathbf{X})} and the Gini index
GY,μ^​(𝐗)G\_{Y,\hat{\mu}(\mathbf{X})} be defined as in Definition [5](https://arxiv.org/html/2510.04556v1#Thmdefinition5 "Definition 5 (Gini index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
  
Then there is a functional TT such that the Gini index can be written as T​(FY,μ^​(𝐗))=GY,μ^​(𝐗)T(F\_{Y,\hat{\mu}(\mathbf{X})})=G\_{Y,\hat{\mu}(\mathbf{X})} and the plug in estimator
G^Y,μ^​(𝐗):=T​(F^Y,μ^​(𝐗))\hat{G}\_{Y,\hat{\mu}(\mathbf{X})}:=T(\hat{F}\_{Y,\hat{\mu}(\mathbf{X})})
for the Gini index is asymptotically normal distributed.
Specifically it holds for some σ2>0\sigma^{2}>0, that

|  |  |  |
| --- | --- | --- |
|  | n​(G^Y,μ^​(𝐗)−GY,μ^​(𝐗))→𝑑N​(0,σ2).\sqrt{n}(\hat{G}\_{Y,\hat{\mu}(\mathbf{X})}-G\_{Y,\hat{\mu}(\mathbf{X})})\xrightarrow{d}N(0,\sigma^{2}). |  |

We provide here a sketch of the proof; full details are given in the Appendix.

###### Proof sketch.

First represent the Gini index as a statistical functional TT.
Then show that TT is Hadamard differentiable at FY,μ^​(𝐗)F\_{Y,\hat{\mu}(\mathbf{X})}.
And finally, combine the empirical-process convergence n​(F^Y,μ^​(𝐗)−FY,μ^​(𝐗))↝𝔾F\sqrt{n}\bigl(\hat{F}\_{Y,\hat{\mu}(\mathbf{X})}-F\_{Y,\hat{\mu}(\mathbf{X})}\bigr)\rightsquigarrow\mathbb{G}\_{F} with the
functional Delta Method to obtain
n​(G^Y,μ^​(𝐗)−GY,μ^​(𝐗))→𝑑N​(0,σ2)\sqrt{n}\bigl(\hat{G}\_{Y,\hat{\mu}(\mathbf{X})}-G\_{Y,\hat{\mu}(\mathbf{X})}\bigr)\xrightarrow{d}N(0,\sigma^{2}).
∎

For the full proof, see Appendix [A](https://arxiv.org/html/2510.04556v1#A1 "Appendix A Proof of Theorem 1 ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
  
  
Because the joint distribution (Y,𝐗)∼F∈ℱ(Y,\mathbf{X})\sim F\in\mathcal{F} is
generally unknown in practice, we use empirical distribution functions to
estimate the Gini index.
The empirical CAP is defined
as follows (see Equation (4.12) in [[30](https://arxiv.org/html/2510.04556v1#bib.bib30)]):

###### Definition 6 (Empirical cumulative accuracy profile).

By first ordering and relabeling the observation YiY\_{i} to Y(i)Y\_{(i)}
based on the order statistics of the predictions,
μ^​(𝐗(1))<μ^​(𝐗(2))<⋯<μ^​(𝐗(n))\hat{\mu}(\mathbf{X}\_{(1)})<\hat{\mu}(\mathbf{X}\_{(2)})<\dots<\hat{\mu}(\mathbf{X}\_{(n)}), the empirical CAP is defined as:

|  |  |  |
| --- | --- | --- |
|  | CAP^Y,μ^​(𝐗)​(α)=1∑i=1nYi​∑i=⌈(1−α)​n⌉+1nY(i).\widehat{\operatorname{CAP}}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha)=\frac{1}{\sum\_{i=1}^{n}Y\_{i}}\sum\_{i=\lceil(1-\alpha)n\rceil+1}^{n}Y\_{(i)}. |  |

Note that CAP^Y,μ^​(𝐗)​(α)\widehat{\operatorname{CAP}}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha) depends on
the predictions μ^​(𝐗)\hat{\mu}(\mathbf{X}) via the ordering,
since each observation Y(i)Y\_{(i)} corresponds to the ii-th smallest predicted value
μ^​(𝐗(i))\hat{\mu}(\mathbf{X}\_{(i)}) among {μ^​(𝐗l)}l=1n\{\hat{\mu}(\mathbf{X}\_{l})\}\_{l=1}^{n}.
Using Definition [6](https://arxiv.org/html/2510.04556v1#Thmdefinition6 "Definition 6 (Empirical cumulative accuracy profile). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), we define the empirical version of the Gini index as:

###### Definition 7 (Empirical Gini index).

The empirical Gini index is defined as follows.

|  |  |  |
| --- | --- | --- |
|  | G^Y,μ^​(𝐗)=∫01CAP^Y,μ^​(𝐗)​(α)​𝑑α−12∫01CAP^Y,Y​(α)​𝑑α−12.\widehat{G}\_{Y,\hat{\mu}(\mathbf{X})}=\frac{\int\_{0}^{1}\widehat{\operatorname{CAP}}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha)d\alpha-\frac{1}{2}}{\int\_{0}^{1}\widehat{\operatorname{CAP}}\_{Y,Y}(\alpha)d\alpha-\frac{1}{2}}. |  |

We note that we do not explicitly derive the asymptotic variance of the Gini
index described in Theorem [1](https://arxiv.org/html/2510.04556v1#Thmtheorem1 "Theorem 1 (Asymptotic Normality of the Gini Index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
However, because we show that the limiting distribution is normal and we assume
that the observations from a fixed time point are i.i.d., we can assume that a
bootstrap approach is consistent (see Section 4.3 in
[[33](https://arxiv.org/html/2510.04556v1#bib.bib33)]).
Therefore, we estimate the parameters of the asymptotic normal
distribution via the following bootstrap approach:

1. 1.

   Step: Generate nn predictions μ^​(𝐗i)\hat{\mu}(\mathbf{X}\_{i}) for i=1,…,ni=1,\ldots,n.
2. 2.

   Step: Generate BB bootstrap samples of size nn by sampling with replacement from the set of tuples {(Yi,μ^​(𝐗i))}i=1n\{(Y\_{i},\hat{\mu}(\mathbf{X}\_{i}))\}\_{i=1}^{n}.
3. 3.

   Step: For each bootstrap sample b=1,…,Bb=1,\ldots,B, calculate the empirical Gini index G^Y,μ^​(𝐗)(b)\widehat{G}\_{Y,\hat{\mu}(\mathbf{X})}^{(b)}.
4. 4.

   Step: Estimate the asymptotic mean and standard deviation of the Gini index on the provided dataset using the bootstrap samples.

Note that this is not similar to bootstrap estimation
of the generalization error because we are not refitting
the model on each bootstrap sample.
  
  
To provide a visual illustration of the (asymptotic) normality of the Gini
index, we follow the steps above for a very popular dataset and model in non-life
insurance literature which is described in Section [3.2](https://arxiv.org/html/2510.04556v1#S3.SS2 "3.2 Illustration example ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
  
  
We applied the bootstrap steps described above to the holdout of this dataset and the fitted GLM model.
In Figure [3](https://arxiv.org/html/2510.04556v1#S2.F3 "Figure 3 ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), we show histograms of the bootstrap
Gini indices for varying numbers of bootstrap samples BB (left) and varying
holdout sample sizes nn (right).

![Refer to caption](x2.png)


(a) B=500B=500 and n=64978n=64978

![Refer to caption](x3.png)


(b) B=10000B=10000 and n=500n=500

![Refer to caption](x4.png)


(c) B=1000B=1000 and n=64978n=64978

![Refer to caption](x5.png)


(d) B=10000B=10000 and n=10000n=10000

![Refer to caption](x6.png)


(e) B=10000B=10000 and n=64978n=64978

![Refer to caption](x7.png)


(f) B=10000B=10000 and n=64978n=64978

Figure 3: Histograms of the bootstrap Gini indices for varying numbers of bootstrap samples BB (left) and varying holdout sample sizes nn (right).

As expected, the histograms approximate a normal distribution, and the
approximation improves with larger bootstrap sample sizes BB.
Furthermore, the standard deviation decreases with larger holdout sample sizes
nn.
This aligns with intuition for model monitoring frameworks: if the holdout
sample size is small, the model was likely trained on a small dataset, and the
model error (as measured by the Gini index) should also be more volatile.
  
Using the results established in this section, we outline a model monitoring framework in
the next section.

## 3 Model monitoring framework and practical considerations

First, we will outline our general framework for model monitoring and then we
will provide common pitfalls and practical considerations.

### 3.1 General Framework for Model Monitoring

On one hand, it is also important not to miss a necessary update of a model in
order to maintain the model’s performance.
But on the other hand, as noted in the introduction, the model update process
is time-consuming, complex, and may introduce instability into the pricing
model; therefore, changes should not be made lightly.
This, in turn, prompts the question of whether an update is needed.
  
  
We first outline the model update process to clarify which information is
available at the decision point.
We do this by providing an example of an annual model update process with a
fixed window size, though the same logic applies to other update frequencies.
In a typical annual cycle, the incumbent model is either recalibrated with new
data or replaced by a newly developed model that incorporates the latest data.
Because models are trained on prior-year data while data from the update year
is not yet fully observed or validated, a lag arises.
This lag is further increased by the time required for model development,
validation and governance.
Therefore, in an annual cycle, a one-year lag can arise.
Consequently, the most recent data used to train or assess the model comes from
the year preceding the update.
  
In Figure [4](https://arxiv.org/html/2510.04556v1#S3.F4 "Figure 4 ‣ 3.1 General Framework for Model Monitoring ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), an example timeline of
a model update cycle in 2024 is shown.

202020212022202320242025training dataμ^2024\hat{\mu}\_{2024} development and deploymentprediction period


Figure 4: Example timeline of a model update cycle in 2024.
The index 20242024 in μ^2024\hat{\mu}\_{2024} indicates the year in which the model is
developed.

…\ldots…\ldots202420252026Decision:
μ^2024\hat{\mu}\_{2024} redeployment or
μ^2025\hat{\mu}\_{2025} development and deployment?prediction period


Figure 5: Example timeline for decision-making in 2025.
The index 20242024 in μ^2024\hat{\mu}\_{2024} indicates the year in which the model is
developed.

In this example, claim data from 2020–2023 is used to train a model.
The model μ^2024​(⋅)\hat{\mu}\_{2024}(\cdot) is then developed in 2024 without using any
2024 data for training or validation.
This model is subsequently deployed to predict, e.g., claim counts for 2025.
  
The question we seek to answer in the 2025 update cycle is whether the model
created in 2024 μ^2024\hat{\mu}\_{2024} using data from 2020–2023 can be reused
(with minor recalibration) and deployed in 2025 to produce predictions for
2026, or whether a new model, μ^2025\hat{\mu}\_{2025}, should be developed.
An illustration of this timeline is shown in Figure
[5](https://arxiv.org/html/2510.04556v1#S3.F5 "Figure 5 ‣ 3.1 General Framework for Model Monitoring ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
This decision should be made in 2025, when data for 2024 becomes available.
To guide this decision, we first compute, following Section
[2.2.3](https://arxiv.org/html/2510.04556v1#S2.SS2.SSS3 "2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), the mean
𝔼^​[GY,μ^2024​(𝐗)o​l​d​-​d​a​t​a]\hat{\mathbb{E}}\left[G\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{old\text{-}data}\right] and
standard deviation
σ^​[GY,μ^2024​(𝐗)o​l​d​-​d​a​t​a]\hat{\sigma}\left[G\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{old\text{-}data}\right]
of the Gini index on the training-period holdout dataset.
We then compute the Gini index on a similarly sized dataset from 2024
G^Y,μ^2024​(𝐗)n​e​w​-​d​a​t​a\widehat{G}\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{new\text{-}data}.
We can then apply the following hypothesis test.
Under the assumption of no real concept drift, the Gini index on the
new data should come from the same distribution as the holdout Gini values from
the training period, i.e., under the null hypothesis H0H\_{0}.
  
Null hypothesis:

|  |  |  |
| --- | --- | --- |
|  | H0:G^Y,μ^2024​(𝐗)n​e​w−d​a​t​a∼𝒩​(𝔼^​[GY,μ^2024​(𝐗)o​l​d​-​d​a​t​a],σ^​[GY,μ^2024​(𝐗)o​l​d​-​d​a​t​a]2).H\_{0}:\;\widehat{G}\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{new-data}\sim\mathcal{N}\left(\hat{\mathbb{E}}\left[G\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{old\text{-}data}\right],\hat{\sigma}\left[G\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{old\text{-}data}\right]^{2}\right). |  |

Test statistic:

|  |  |  |
| --- | --- | --- |
|  | z=G^Y,μ^2024​(𝐗)n​e​w​-​d​a​t​a−𝔼^​[GY,μ^2024​(𝐗)o​l​d​-​d​a​t​a]σ^​[GY,μ^2024​(𝐗)o​l​d​-​d​a​t​a].z\;=\;\frac{\widehat{G}\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{new\text{-}data}-\hat{\mathbb{E}}\left[G\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{old\text{-}data}\right]}{\hat{\sigma}\left[G\_{Y,\hat{\mu}\_{2024}(\mathbf{X})}^{old\text{-}data}\right]}. |  |

p-value (two-sided):

|  |  |  |
| --- | --- | --- |
|  | p= 2​(1−Φ​(|z|)),p\;=\;2\left(1-\Phi(|z|)\right), |  |

where Φ​(⋅)\Phi(\cdot) is the standard normal CDF.
We decide at level α\alpha to reject H0H\_{0} if p<αp<\alpha (equivalently, if
|z|>Φ−1​(1−α2)|z|>\Phi^{-1}(1-\frac{\alpha}{2})); otherwise, we fail to reject H0H\_{0}.
Regarding interpretation, the test statistic zz measures changes in Gini
performance in standard-deviation units; negative values (z<0z<0) indicate
deterioration and positive values indicate improvement.
For example, a zz-value of −1-1 (corresponding to a p-value of ≈0.32\approx 0.32) means that the Gini performance on the new data is one standard
deviation worse than the average Gini performance in the training period.
A zz-value of −1.96-1.96 (corresponding to a p-value of ≈0.05\approx 0.05)
means that the Gini performance on the new data is nearly two standard
deviations worse than the average Gini performance in the holdout of the
training period.
  
  
Note that this is a two-sided test, as we want to detect both deterioration and
improvement in model performance, one can also use a one-sided test if only
deterioration is of interest.
  
  
In the next section, we present a simple illustrative example; subsequently,
we discuss practical considerations.

### 3.2 Illustration example

To provide a simple illustrative example of the above-mentioned monitoring
framework, we use a very popular dataset and model in non-life insurance.
Just as MNIST is the de facto “hello world” dataset in computer
vision (see, e.g., [[1](https://arxiv.org/html/2510.04556v1#bib.bib1)]), the FreMTPL2freq
[[11](https://arxiv.org/html/2510.04556v1#bib.bib11)] dataset becomes the de facto “hello
world” dataset for non-life insurance pricing.
It is a well-known French motor third-party liability (MTPL) claim-frequency
dataset that is widely used in the actuarial literature for benchmarking and
interpreting new methods (see, e.g., [[18](https://arxiv.org/html/2510.04556v1#bib.bib18)],
[[25](https://arxiv.org/html/2510.04556v1#bib.bib25)], [[33](https://arxiv.org/html/2510.04556v1#bib.bib33)],
[[4](https://arxiv.org/html/2510.04556v1#bib.bib4)], [[15](https://arxiv.org/html/2510.04556v1#bib.bib15)]).
We use version 1.0-8 of the dataset, as in the cited literature.
  
  
Since the dataset is already well documented in the literature, we briefly
summarize where the data exploration, preprocessing, and model-fitting steps
can be found.
For data exploration, we refer to the tutorial by Noll et al.
[[23](https://arxiv.org/html/2510.04556v1#bib.bib23)].
Furthermore, we use the same data-cleaning process described in Appendix B of
[[33](https://arxiv.org/html/2510.04556v1#bib.bib33)].
For data preparation, we follow the same feature engineering as in Section
5.3.4 of [[33](https://arxiv.org/html/2510.04556v1#bib.bib33)].
For the train/test split, we apply the same split used by most manuscripts that
use this dataset, as described in Listing 5.2 of
[[33](https://arxiv.org/html/2510.04556v1#bib.bib33)].
The test set contains 67,801 observations, whereas the training set contains
610,206.
  
We fit the same Poisson GLM with a log link as
GLM3 in Section 5.3.4 of [[33](https://arxiv.org/html/2510.04556v1#bib.bib33)] on the training dataset.
The unpenalized GLM is fitted with the scikit-learn API [[5](https://arxiv.org/html/2510.04556v1#bib.bib5)]
using the Newton–Cholesky solver.
We verified that this GLM matches the one reported in the literature by
computing the Poisson deviance on the holdout dataset and comparing it to the
published value.
  
  
Finally, to ensure that systematic time-splitting is not an issue in the upcoming
analysis (see Pitfall B in Section [3.3](https://arxiv.org/html/2510.04556v1#S3.SS3 "3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")),
we pre-aggregate the holdout dataset.
We do this as a precaution because it is unclear whether the column “IDpol”
is a true policyholder identifier or a time-period-policyholder identifier
created by the data provider.
We pre-aggregate at the level of unique covariate combinations (i.e., across
all covariates used in the model) so that each covariate combination appears
only once, along with its total exposure, total claim count, and corresponding
exposure-weighted prediction.
After this aggregation, the observation count of the holdout dataset decreases
only slightly to 64,978.
  
  
The above-mentioned GLM3 depends on several covariates, including
the driver’s age (DrivAge in the dataset), which we use to
simulate concept drift.
To illustrate the monitoring framework, we create a new dataset by augmenting
the holdout dataset and simulating concept drift.
We do this by artificially redistributing a fixed number of claims across
different age groups while keeping the total claim count constant.
Specifically, we transfer 100 claims in Scenario 1, 150 claims in Scenario 2,
and 200 claims in Scenario 3 (approximately 3.8%, 5.7%, and 7.56% of all
claims in the holdout dataset, respectively) from drivers aged 25–35 years to
drivers aged 35–45 years.
  
This simulation mimics a setting in which claim frequencies shift between
demographic groups over time, for example due to changing driving behaviors
within specific age cohorts.
  
For the claim reduction, we randomly sample policyholders in the younger age
group with at least one claim and reduce their claim count by one.
For the claim increase, we randomly sample policyholders in the older age group
(regardless of their original claim count) and increase their claim count by
one.
  
This redistribution creates a detectable shift in the age-specific
claim frequency pattern while maintaining the overall portfolio claim count,
allowing us to assess the sensitivity of our monitoring framework to localized
distributional changes.
Figure [6](https://arxiv.org/html/2510.04556v1#S3.F6 "Figure 6 ‣ 3.2 Illustration example ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") visualizes the changes introduced by this
procedure.
  
In each plot, bars represent exposure, the blue line shows predicted claim
frequency, and the green line shows observed claim frequency.
Subfigure (a) shows the original claim frequency by age; (b)–(d) show
progressively more severe claim redistributions from the driver age group
(25–35) to (35–45) years for Scenarios 1–3.
  
By construction, the overall observed claim frequency is unchanged.
However, the observed age-specific claim frequencies do change due to the
redistribution.
In contrast, the model’s predicted claim frequency remains unchanged—both
overall and by age group, because policyholder features do not change.

![Refer to caption](x8.png)


(a) Without changes
  
Gini=0.3779\begin{aligned} \text{Gini}=\phantom{-}&0.3779\\[-4.0pt]
\phantom{z\text{-statistic}=-}&\phantom{0.0000}\end{aligned}

![Refer to caption](x9.png)


(b) Scenario 1
  
Gini=0.3638p​-value=0.2007z​-statistic=−1.2794\begin{aligned} \text{Gini}=\phantom{-}&0.3638\\[-4.0pt]
p\text{-value}=\phantom{-}&0.2007\\[-4.0pt]
z\text{-statistic}=-&1.2794\end{aligned}

![Refer to caption](x10.png)


(c) Scenario 2
  
Gini=0.3568p​-value=0.0538z​-statistic=−1.9285\begin{aligned} \text{Gini}=\phantom{-}&0.3568\\[-4.0pt]
p\text{-value}=\phantom{-}&0.0538\\[-4.0pt]
z\text{-statistic}=-&1.9285\end{aligned}

![Refer to caption](x11.png)


(d) Scenario 3
  
Gini=0.3518p​-value=0.0173z​-statistic=−2.3805\begin{aligned} \text{Gini}=\phantom{-}&0.3518\\[-4.0pt]
p\text{-value}=\phantom{-}&0.0173\\[-4.0pt]
z\text{-statistic}=-&2.3805\end{aligned}

Figure 6: Illustrative example showing the effect of induced concept drift by redistributing claims between age groups.

We apply the framework introduced in Section
[3.1](https://arxiv.org/html/2510.04556v1#S3.SS1 "3.1 General Framework for Model Monitoring ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") by calculating the Gini index
on both the original holdout dataset and the modified datasets from Scenario 1
and Scenario 2.
Using the bootstrap procedure described in Section [2.2.3](https://arxiv.org/html/2510.04556v1#S2.SS2.SSS3 "2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), we
estimate the parameters of the null distribution (σ=0.0109\sigma=0.0109) and
subsequently compute the pp-values and zz-statistics as outlined in Section
[3.1](https://arxiv.org/html/2510.04556v1#S3.SS1 "3.1 General Framework for Model Monitoring ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
  
  
The results reveal that in Scenario 1, the pp-value is 0.20070.2007 and the
zz-statistic is −1.2794-1.2794, indicating a decrease in model performance of more
than one standard deviation from the baseline.
In the more severe Scenario 2, the pp-value drops to 0.05380.0538 and the
zz-statistic reaches −1.9285-1.9285, corresponding to a decrease of nearly two
standard deviations, while the even more severe Scenario 3 yields a pp-value
of 0.01730.0173 and a zz-statistic of −2.3805-2.3805.
These findings demonstrate that more pronounced concept drift leads to stronger
statistical evidence of model deterioration (indicated by lower pp-values) and
larger negative zz-statistics.
Moreover, they suggest that practitioners may benefit from adopting more
conservative significance thresholds than the conventional level of 0.050.05 when
monitoring models.

### 3.3 Practical Considerations and Pitfalls

In this section, we discuss practical considerations for implementing the
proposed framework and summarize common pitfalls.
We first list actionable setup recommendations, then a short checklist of basic
pitfalls, and finally detail advanced pitfalls and their mitigations.
  
  
Practical considerations (setup and process):

  
  
Significance level and monitoring frequency:
Regarding the choice of significance level α\alpha, we deliberately choose not
to recommend adopting a fixed level such as the commonly used α=0.05\alpha=0.05.
The reason is that, in a model-monitoring context, the decision to replace a
model typically involves a trade-off between performance considerations vs.
stability and implementation costs, which is highly dependent on the specific
business context.
As mentioned above, the annual monitoring frequency is only an example; in
reality, the monitoring cycle may vary depending on the model’s purpose as well
as the business, implementation, and regulatory contexts.
  
  
Regarding the types of real concept drift:
Depending on the detection of real concept drift type (see Section
[2.1](https://arxiv.org/html/2510.04556v1#S2.SS1 "2.1 Virtual-Drift and Concept-Drift ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")), one may use different holdout samples to
estimate the mean and standard deviation of the Gini index based on the
training period.
For example, in the case of sudden drift, one might use a holdout
sample consisting only of the most recent training year to estimate the mean
and standard deviation of the Gini index.
In cases of gradual drift or incremental drift, one might
compute separate mean and standard deviation estimates for each training year’s
holdout set, and conducting the hypothesis test separately for each year using
its corresponding estimates.
If recurrent drift due to seasonality is already known (e.g.,
weather-related monthly patterns), one should apply the above approach to
datasets restricted to the relevant seasonal periods.
  
  
Exposure considerations in Gini calculation:
Two related issues deserve attention.
First, predictions must be adjusted for exposure (e.g., predicted counts =
model prediction ×\times exposure) so that predictions and observations are on
the same scale.
Second, when constructing the CAP curve, decide whether the x‑axis should
accumulate observations (count weighting) or exposure (exposure weighting).
In either case, due to Pitfall B (see below), it may be necessary to
preaggregate the dataset at the policyholder level or at the level of unique
covariate combinations (i.e., all covariates used in the model).
  
If the goal is to study the conditional distribution FY∣𝐗F\_{Y\mid\mathbf{X}}
independently of F𝐗F\_{\mathbf{X}}, using observation counts as weights can be
reasonable.
If, on the other hand, one wants observations with larger exposure to
contribute proportionally to the ranking and to the area under the CAP curve,
consider exposure weighting.
  
Note that the choice of weighting can materially affect the Gini index.
As an illustration, Figure
[7](https://arxiv.org/html/2510.04556v1#S3.F7 "Figure 7 ‣ 3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") shows two CAP curves for
the same dataset and model (discussed in Section
[3.2](https://arxiv.org/html/2510.04556v1#S3.SS2 "3.2 Illustration example ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")) : one using observation counts weighting
(left) and the other using exposure weighting (right).

![Refer to caption](x12.png)


(a) Using observation counts weighting.
  
Gini =0.38=0.38

![Refer to caption](x13.png)


(b) Using exposure weighting.
  
Gini =0.10=0.10

The upper exposure decile contains:

10.0%10.0\% of the total exposure

34.74%34.74\% of the number of policies

14.29%14.29\% of the total response

Figure 7: CAP curves using observation counts weighting (left) vs. exposure weighting (right).
The upper exposure decile is marked light red.
The dataset’s total number of observations is 64,978, total exposure is 35,967,
and total response (claim count) is 2,645.

It is important to note that we used the same number of observations and
adjusted the predictions for exposure in both cases, so the ordering of
observations is identical.
The only difference is the weighting of the x-axis in the CAP curve.
  
A substantial difference in the Gini index is clearly visible 0.380.38 versus
0.100.10 depending on the weighting choice.
To illustrate why this occurs, we also report the composition of the upper
exposure decile (i.e., the top 10% of the right x-axis).
This decile corresponds to the 10% of total exposure with the lowest-ranked
model predictions.
Under exposure weighting, the upper decile contains 10.0%10.0\% of the total
exposure but represents 34.74%34.74\% of all observations and 14.29%14.29\% of the
total response.
This suggests that many observations with small exposure generated claims.
Such a situation can occur, for example, when a claim represents a total loss
of the vehicle, which typically leads to policy cancellation; and therefore
smaller exposure as a result.
I.e. the response influences the exposure.
Because one often wishes to weigh those observations higher (despite their
small exposure), one may reasonably prefer observation-count weighting over
exposure weighting in such cases.
  
In summary, the choice of weighting can materially affect the Gini
index and must be applied consistently.
  
  
Some pitfalls are often overlooked: while they matter less in model comparison
settings, they can have a material impact in model-monitoring applications.
  
  
Basic pitfalls (quick checklist):

* •

  Not using the holdout, but instead using the training data from the training period to estimate the parameters of the null distribution.
* •

  Not considering exposure weights in the prediction.
* •

  Not recognizing that exposure alone carries substantial explanatory power when interpreting the Gini index.
  (Consequently, a mean model that accounts for exposure can considerably
  outperform a random benchmark.)
* •

  Not removing observations with zero exposure. (These will change the deviance and Gini measure depending on the implementation, due to their impact on the observation count.)
* •

  Not ensuring model autocalibration during training (especially for ML-models like GBMs or NNs).
* •

  Not considering the Gini’s limitations when reapplying a model: The Gini is rank-based; it does not detect systematic level shifts (e.g., uniformly
  over- or under-predicting frequency).
  So when reapplying the model, always complement the Gini comparison with a
  level check and calibration.
* •

  Not using at least as many observations in the new data as were used for the bootstrap approach.
  This is crucial for ensuring the validity of the statistical tests, since the
  distribution of the test statistic is affected by sample size.

Advanced pitfalls (details and remedies):

  
  
Pitfall A: Implications of sorting ties in Gini calculation.
Note that in the Definitions [4](https://arxiv.org/html/2510.04556v1#Thmdefinition4 "Definition 4 (Cumulative accuracy profile). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") and [5](https://arxiv.org/html/2510.04556v1#Thmdefinition5 "Definition 5 (Gini index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), we assume
that μ^​(𝐗)\hat{\mu}(\mathbf{X}) has a continuous distribution.
By contrast, the empirical Definitions [6](https://arxiv.org/html/2510.04556v1#Thmdefinition6 "Definition 6 (Empirical cumulative accuracy profile). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") and
[7](https://arxiv.org/html/2510.04556v1#Thmdefinition7 "Definition 7 (Empirical Gini index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") do not require this assumption.
However, this can have material implications for the empirical Gini.
In the empirical definition of the Gini index (see Definition
[7](https://arxiv.org/html/2510.04556v1#Thmdefinition7 "Definition 7 (Empirical Gini index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")), the sorting is based only on the predicted
values μ^​(𝐗)\hat{\mu}(\mathbf{X}).
Thus if the model is very small, the number of unique predicted values can be
very small as well, and thus the sorting of the dataset effectively divides the
data into just a few blocks.
The CAP curve, and therefore the Gini, may then depend strongly on how
observations within each tie are ordered.
Because the empirical definition does not prescribe a tie-breaking rule,
different implementations e.g. original order, random permutation, secondary
sort by the observation, can yield noticeably different results.
  
In the following, we illustrate a scenario with limited data, where a small
model with only a few covariates may be the only reasonable choice.
For this purpose, we fitted a small GLM to the dataset discussed in Section
[3.2](https://arxiv.org/html/2510.04556v1#S3.SS2 "3.2 Illustration example ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
This GLM uses only a single categorical covariate with four unique values (we
binned the numerical variable DrivAge into 4 buckets).
To better visualize the impact, we took the above-mentioned dataset.
and reduced it to only those observations with exposure vi=1v\_{i}=1.
Since the model is so small and the exposure is uniformly equal to 1, sorting
by the predictions partitions the data into exactly four blocks with tied
predicted values within each block.
  
We visualize the CAP curves for different tie-breaking methods in the case of
prediction ties in Figure [8](https://arxiv.org/html/2510.04556v1#S3.F8 "Figure 8 ‣ 3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
If observations with tied predicted values are sorted in random order (see (a)
in Figure [8](https://arxiv.org/html/2510.04556v1#S3.F8 "Figure 8 ‣ 3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")), this yields a plausible CAP
curve and a Gini index of about 0.050.05, consistent with the limited
discriminatory power of such a small model.
When ties are ordered in the best possible way (see (b) in Figure
[8](https://arxiv.org/html/2510.04556v1#S3.F8 "Figure 8 ‣ 3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")), the Gini index increases to about
0.310.31.
Finally, if ties are ordered in the worst possible way (see (c) in Figure
[8](https://arxiv.org/html/2510.04556v1#S3.F8 "Figure 8 ‣ 3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")), the Gini index becomes negative,
around −0.21-0.21.
This would normally indicate that the model performs worse than random
guessing, which is clearly not the case here, since there is no negative
correlation between predictions and outcomes.
Thus, the Gini index can vary substantially depending on how sortation is
handled.
For this reason, we do not recommend using best- or worst-case sortation,
especially when the model produces only a small number of unique prediction
values.

![Refer to caption](x14.png)


(a) Random sort within ties.
  
Gini =0.05=0.05

![Refer to caption](x15.png)


(b) Best sort within ties.
  
Gini =0.31=0.31

![Refer to caption](x16.png)


(c) Worst sort within ties.
  
Gini =−0.21=-0.21

Figure 8: CAP curves for a small GLM with different sorting methods for observations with tied predicted values.



![Refer to caption](x17.png)


(a) Random sort within ties.
  
Gini =0.40=0.40

![Refer to caption](x18.png)


(b) Best sort within ties.
  
Gini =0.40=0.40

![Refer to caption](x19.png)


(c) Worst sort within ties.
  
Gini =0.40=0.40

Figure 9: CAP curves for a bigger GLM with different sorting methods for observations with tied predicted values.

This issue should arise only in small models with few covariates or in
datasets with limited diversity.
To illustrate, if we use the model described in Section
[3.2](https://arxiv.org/html/2510.04556v1#S3.SS2 "3.2 Illustration example ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing") with higher discriminatory power on the same
restricted dataset, we obtain a Gini index of about 0.400.40, independent of the
sorting method used; see Figure [9](https://arxiv.org/html/2510.04556v1#S3.F9 "Figure 9 ‣ 3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
  
Recommendation.
As a practical solution, we suggest investing slightly more computation:
compute the Gini index twice, once using the best-case and once using the
worst-case ordering within ties, and use the average of these two values.
For the small model, this yields a Gini index of about 0.050.05, identical to
that from random tie-breaking but without dependence on a random seed.
This approach does not adversely affect larger models with more unique
predicted values.
  
  
Pitfall B: Implications of Time‑split.
The following aspect of the ETL pipeline for model-monitoring is often
underestimated: In claim-frequency modeling, one typically works with datasets
𝒟\mathcal{D} in which each row represents a specific time period for a
policyholder.
Even if a policy’s covariates do not change, typical ETL pipelines will split
these time periods for various reasons.
This means that a policyholder’s record is split into multiple rows
representing shorter intervals (keeping the covariates unchanged, adjusting the
exposure, and setting the target variable according to whether a claim occurred
in the sub-interval), yielding a new dataset 𝒟′\mathcal{D}^{\prime}.
One reason for such time splitting is to simplify reporting: it is desirable to
have at most one claim per row, so that the claim date and other information
about the response can be stored in that row (which would not easily be
possible in traditional data structures if multiple claims occurred during the
period and were aggregated).
  
This new dataset 𝒟′\mathcal{D}^{\prime} has the same average claim frequency, the same
total number of claims, and the same total exposure ∑i=1nvi\sum\_{i=1}^{n}v\_{i}.
Moreover, by inspecting the score equations, one can easily show that, e.g., in
the Poisson GLM case, such a time‑period split does not affect the model fit;
i.e., the same GLM coefficients result regardless of whether the model was
fitted to the dataset before time‑period splitting 𝒟\mathcal{D} or after time
splitting to 𝒟′\mathcal{D}^{\prime}.
For this reason, ETL pipelines might incorporate many time splits so that the
dataset can be reused for various purposes.
While this may not affect the model selection process (such as in GLM
modeling), it can have a large impact on the model monitoring process, because
the Gini and deviance loss can change dramatically when time splits are
applied, especially if those splits depend on the response.
  
To illustrate this issue, we provide an extreme example using the
dataset and model described in Section [3.2](https://arxiv.org/html/2510.04556v1#S3.SS2 "3.2 Illustration example ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
We applied a time-period split such that each claim is represented by exactly
one row with an exposure of one day (1/365 of a year).
In the case of rows with multiple claims, we created multiple one-day rows,
each containing exactly one claim.
The remaining exposure was assigned to an additional row with zero claims.
We fitted the same model to this new dataset and obtained the same coefficients
as before (up to numerical precision).
However, the Gini index dropped from 0.380.38 to −0.99-0.99, and the Poisson
deviance loss increased from 24.941⋅10−224.941\cdot 10^{-2} to 65.224⋅10−265.224\cdot 10^{-2}.
The reason for this dramatic change can be clearly seen in the CAP curve shown
in Figure [10](https://arxiv.org/html/2510.04556v1#S3.F10 "Figure 10 ‣ 3.3 Practical Considerations and Pitfalls ‣ 3 Model monitoring framework and practical considerations ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").

![Refer to caption](x20.png)


(a) Before extreme time-splitting.
  
Gini =0.38=0.38
  
Poisson deviance loss =24.941⋅10−2=24.941\cdot 10^{-2}

![Refer to caption](x21.png)


(b) After extreme time-splitting.
  
Gini =−0.99=-0.99
  
Poisson deviance loss =65.224⋅10−2=65.224\cdot 10^{-2}

Figure 10: CAP curves before extreme time-splitting (left) vs. after extreme time-splitting (right).

Due to the time-period split, the predictions are scaled by unrealistically
small exposures; consequently, the ordering of observations changes
substantially, leading to very different metrics.
Since time-period splitting is routinely performed for various reasons in large
ETL processes, this extreme example illustrates a potential pitfall:
underestimating the effect of ETL changes that do not affect the model fit but
do affect the model-monitoring process.
  
Recommendation.
To avoid this pitfall, we suggest preaggregating the dataset before using it in
a model-monitoring context, at least at the policyholder level or at
the level of unique covariate combinations (i.e., all covariates used in the
model).
This will add a small amount of computation to the ETL pipeline for the
monitoring process but will also reduce model inference time because the
dataset will be smaller.

## 4 Conclusion

This paper provides a systematic examination of concept drift
in non-life insurance pricing and a statistically grounded monitoring framework.
A comprehensive overview of the relevant literature on concept drift is
provided and contextualized in the actuarial setting.
We derive the asymptotic distribution of the Gini index to enable valid
inference and hypothesis testing.
Building on this, we propose a standardized monitoring procedure that signals
when refitting is warranted and illustrate its practical use on a modified
real-world portfolio in which we inject controlled levels of concept drift.
We highlight implementation considerations and several pitfalls for model
monitoring and model comparison.
  
Provided predictions are assessed under an auto-calibration perspective,
the framework is model-agnostic and applies not just for GLMs but equally
to modern machine-learning models such as tree ensembles and neural networks.
In practice, the approach supports transparent and repeatable monitoring and
governance, helping prioritize refitting efforts where they create the most
value.
  
Methodologically, several extensions are promising and warrant exploration in
future research.
Different windowing designs and adaptive schemes could be investigated to
improve responsiveness and robustness.
Recurrent drift deserves special attention, particularly in long-term business.
In addition, combining multiple concept drift detection methods with
dimensionality-reduction diagnostics could improve attribution and reveal the
drivers of drift.
While the focus of our work is on drift detection, future work could benchmark
drift-adaptation strategies for pricing, including windowing-based updates,
ensemble methods, and continual learning to maintain performance while
preserving valuable prior knowledge.
  
We hope these contributions encourage systematic, drift-aware monitoring and
stimulate further research on adaptive actuarial modeling.

## References

* \bibcommenthead
* Ackerman et al [2021]

  Ackerman S, Raz O, Zalmanovici M, et al (2021) Automatically detecting data
  drift in machine learning classifiers. [10.48550/arXiv.2111.05672](https:/doi.org/10.48550/arXiv.2111.05672)
* Bifet and Gavaldà [2007]

  Bifet A, Gavaldà R (2007) Learning from Time-Changing Data with
  Adaptive Windowing. In: Proceedings of the 2007 SIAM International
  Conference on Data Mining (SDM). Proceedings, Society for Industrial
  and Applied Mathematics, p 443–448, [10.1137/1.9781611972771.42](https:/doi.org/10.1137/1.9781611972771.42)
* Billingsley [1999]

  Billingsley P (1999) Convergence of Probability Measures. John Wiley &
  Sons, Ltd, [10.1002/9780470316962](https:/doi.org/10.1002/9780470316962)
* Brauer [2024]

  Brauer A (2024) Enhancing actuarial non-life pricing models via transformers.
  European Actuarial Journal 14(3):991–1012. [10.1007/s13385-024-00388-2](https:/doi.org/10.1007/s13385-024-00388-2)
* Buitinck et al [2013]

  Buitinck L, Louppe G, Blondel M, et al (2013) API design for machine learning
  software: experiences from the scikit-learn project. In: ECML PKDD Workshop:
  Languages for Data Mining and Machine Learning, pp 108–122
* Charpentier [2024]

  Charpentier A (2024) Insurance, biases, discrimination and fairness. Springer
  Actuarial, Springer, Cham, [10.1007/978-3-031-49783-4](https:/doi.org/10.1007/978-3-031-49783-4)
* Davidson [2009]

  Davidson R (2009) Reliable inference for the Gini index. Journal of
  Econometrics 150(1):30–40. [10.1016/j.jeconom.2008.11.004](https:/doi.org/10.1016/j.jeconom.2008.11.004)
* Denuit et al [2019]

  Denuit M, Sznajder D, Trufin J (2019) Model selection based on Lorenz and
  concentration curves, Gini indices and convex order. Insurance: Mathematics
  and Economics 89:128–139. [10.1016/j.insmatheco.2019.09.001](https:/doi.org/10.1016/j.insmatheco.2019.09.001)
* Denuit et al [2021]

  Denuit M, Charpentier A, Trufin J (2021) Autocalibration and
  Tweedie-dominance for insurance pricing with machine learning. Insurance:
  Mathematics and Economics 101:485–497.
  [10.1016/j.insmatheco.2021.09.001](https:/doi.org/10.1016/j.insmatheco.2021.09.001)
* Denuit et al [2024]

  Denuit M, Huyghe J, Trufin J, et al (2024) Testing for auto-calibration with
  Lorenz and Concentration curves. Insurance: Mathematics and Economics
  117:130–139. [10.1016/j.insmatheco.2024.04.003](https:/doi.org/10.1016/j.insmatheco.2024.04.003)
* Dutang and Charpentier [2018]

  Dutang C, Charpentier A (2018) CASdatasets: Insurance datasets.
  URL <http://dutangc.free.fr/pub/RRepos/>, r package version 1.0–8
* Gama et al [2004]

  Gama J, Medas P, Castillo G, et al (2004) Learning with Drift Detection.
  In: Bazzan ALC, Labidi S (eds) Advances in Artificial Intelligence –
  SBIA 2004. Springer, Berlin, Heidelberg, pp 286–295,
  [10.1007/978-3-540-28645-5\_29](https:/doi.org/10.1007/978-3-540-28645-5_29)
* Gama et al [2014]

  Gama J, Žliobaitė I, Bifet A, et al (2014) A survey on concept drift
  adaptation. ACM Comput Surv 46(4):44:1–44:37. [10.1145/2523813](https:/doi.org/10.1145/2523813)
* Hinder et al [2024]

  Hinder F, Vaquet V, Hammer B (2024) One or two things we know about concept
  drift—a survey on monitoring in evolving environments. Part A:
  detecting concept drift. Frontiers in Artificial Intelligence 7.
  [10.3389/frai.2024.1330257](https:/doi.org/10.3389/frai.2024.1330257), publisher: Frontiers
* Holvoet et al [2025]

  Holvoet F, Antonio K, Henckaerts R (2025) Neural Networks for Insurance
  Pricing with Frequency and Severity Data: A Benchmark Study
  from Data Preprocessing to Technical Tariff. North American Actuarial
  Journal 29(3):519–562. [10.1080/10920277.2025.2451860](https:/doi.org/10.1080/10920277.2025.2451860)
* Hu et al [2025]

  Hu L, Lu Y, Feng Y (2025) Concept Drift Detection Based on Deep
  Neural Networks and Autoencoders. Applied Sciences 15(6):3056.
  [10.3390/app15063056](https:/doi.org/10.3390/app15063056), publisher: MDPI AG
* Krüger and Ziegel [2021]

  Krüger F, Ziegel JF (2021) Generic conditions for forecast dominance. Journal
  of Business & Economic Statistics 39(4):972–983.
  [10.1080/07350015.2020.1741376](https:/doi.org/10.1080/07350015.2020.1741376)
* Lorentzen and Mayer [2020]

  Lorentzen C, Mayer M (2020) Peeking into the Black Box: An Actuarial
  Case Study for Interpretable Machine Learning.
  [10.2139/ssrn.3595944](https:/doi.org/10.2139/ssrn.3595944)
* Lu et al [2019]

  Lu J, Liu A, Dong F, et al (2019) Learning under Concept Drift: A
  Review. IEEE Transactions on Knowledge and Data Engineering
  31(12):2346–2363. [10.1109/TKDE.2018.2876857](https:/doi.org/10.1109/TKDE.2018.2876857)
* Mallick et al [2022]

  Mallick A, Hsieh K, Arzani B, et al (2022) Matchmaker: Data Drift
  Mitigation in Machine Learning for Large-Scale Systems.
  Proceedings of Machine Learning and Systems 4:77–94.
  URL <https://proceedings.mlsys.org/paper_files/paper/2022/hash/069a002768bcb31509d4901961f23b3c-Abstract.html>
* Nelder and Wedderburn [1972]

  Nelder JA, Wedderburn RWM (1972) Generalized Linear Models. Journal of the
  Royal Statistical Society Series A (General) 135(3):370–384.
  [10.2307/2344614](https:/doi.org/10.2307/2344614), publisher: [Royal Statistical Society, Wiley]
* Nishida and Yamauchi [2007]

  Nishida K, Yamauchi K (2007) Detecting Concept Drift Using Statistical
  Testing. In: Corruble V, Takeda M, Suzuki E (eds) Discovery Science.
  Springer, Berlin, Heidelberg, pp 264–269, [10.1007/978-3-540-75488-6\_27](https:/doi.org/10.1007/978-3-540-75488-6_27)
* Noll et al [2020]

  Noll A, Salzmann R, Wuthrich MV (2020) Case Study: French Motor
  Third-Party Liability Claims. [10.2139/ssrn.3164764](https:/doi.org/10.2139/ssrn.3164764)
* Rabanser et al [2019]

  Rabanser S, Günnemann S, Lipton Z (2019) Failing loudly: An empirical study
  of methods for detecting dataset shift. Advances in Neural Information
  Processing Systems 32
* Richman and Wüthrich [2023]

  Richman R, Wüthrich MV (2023) LocalGLMnet: interpretable deep learning for
  tabular data. Scandinavian Actuarial Journal 2023(1):71–95.
  [10.1080/03461238.2022.2081816](https:/doi.org/10.1080/03461238.2022.2081816), publisher: Taylor & Francis
* Richman et al [2025]

  Richman R, Scognamiglio S, Wüthrich MV (2025) The credibility transformer.
  European Actuarial Journal 15(2):345–379. [10.1007/s13385-025-00413-y](https:/doi.org/10.1007/s13385-025-00413-y)
* Schlimmer and Granger [1986]

  Schlimmer JC, Granger RH (1986) Beyond incremental processing: tracking concept
  drift. In: Proceedings of the Fifth AAAI National Conference on Artificial
  Intelligence. AAAI Press, AAAI’86, p 502–507
* Van Der Vaart and Wellner [2023]

  Van Der Vaart AW, Wellner JA (2023) Weak Convergence and Empirical
  Processes: With Applications to Statistics. Springer Series in
  Statistics, Springer International Publishing, Cham,
  [10.1007/978-3-031-29040-4](https:/doi.org/10.1007/978-3-031-29040-4)
* Widmer and Kubat [1996]

  Widmer G, Kubat M (1996) Learning in the presence of concept drift and hidden
  contexts. Machine Learning 23(1):69–101. [10.1007/BF00116900](https:/doi.org/10.1007/BF00116900)
* Wuthrich et al [2025]

  Wuthrich MV, Richman R, Avanzi B, et al (2025) AI Tools for Actuaries.
  [10.2139/ssrn.5162304](https:/doi.org/10.2139/ssrn.5162304)
* Wüthrich [2023]

  Wüthrich MV (2023) Model selection with Gini indices under auto-calibration.
  European Actuarial Journal 13(1):469–477. [10.1007/s13385-022-00339-9](https:/doi.org/10.1007/s13385-022-00339-9)
* Wüthrich [2025]

  Wüthrich MV (2025) Auto-calibration tests for discrete finite regression
  functions. European Actuarial Journal 15(1):335–341.
  [10.1007/s13385-025-00410-1](https:/doi.org/10.1007/s13385-025-00410-1)
* Wüthrich and Merz [2023]

  Wüthrich MV, Merz M (2023) Statistical foundations of actuarial learning and
  its applications. Springer Actuarial, Springer, Cham, Switzerland,
  [10.1007/978-3-031-12409-9](https:/doi.org/10.1007/978-3-031-12409-9)

## Appendix A Proof of Theorem [1](https://arxiv.org/html/2510.04556v1#Thmtheorem1 "Theorem 1 (Asymptotic Normality of the Gini Index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")

First we recall the theorem:

###### Theorem 2 (Asymptotic Normality of the Gini Index).

Assume (Yi,𝐗i)∼F∈ℱ(Y\_{i},\mathbf{X}\_{i})\sim F\in\mathcal{F} i.i.d.\mathrm{i.i.d.}
and let μ^​(⋅)\hat{\mu}(\cdot) be an auto-calibrated estimator.
Suppose 𝔼​[Y]<∞\mathbb{E}[Y]<\infty and 𝔼​[μ^​(𝐗)]<∞\mathbb{E}[\hat{\mu}(\mathbf{X})]<\infty.
Further assume that YY and μ^​(𝐗)\hat{\mu}(\mathbf{X}) have continuous
distribution functions FYF\_{Y} and Fμ^​(𝐗)F\_{\hat{\mu}(\mathbf{X})}, respectively.
Let the combined distribution function of (Y,μ^​(𝐗))(Y,\hat{\mu}(\mathbf{X})) be
denoted by FY,μ^​(𝐗)F\_{Y,\hat{\mu}(\mathbf{X})} and the Gini index
GY,μ^​(𝐗)G\_{Y,\hat{\mu}(\mathbf{X})} be defined as in Definition [5](https://arxiv.org/html/2510.04556v1#Thmdefinition5 "Definition 5 (Gini index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").
  
Then there is a functional TT such that the Gini index can be written as T​(FY,μ^​(𝐗))=GY,μ^​(𝐗)T(F\_{Y,\hat{\mu}(\mathbf{X})})=G\_{Y,\hat{\mu}(\mathbf{X})} and the plug in estimator
G^Y,μ^​(𝐗):=T​(F^Y,μ^​(𝐗))\hat{G}\_{Y,\hat{\mu}(\mathbf{X})}:=T(\hat{F}\_{Y,\hat{\mu}(\mathbf{X})})
for the Gini index is asymptotically normal distributed.
Specifically it holds for some σ2>0\sigma^{2}>0, that

|  |  |  |
| --- | --- | --- |
|  | n​(G^Y,μ^​(𝐗)−GY,μ^​(𝐗))→𝑑N​(0,σ2).\sqrt{n}(\hat{G}\_{Y,\hat{\mu}(\mathbf{X})}-G\_{Y,\hat{\mu}(\mathbf{X})})\xrightarrow{d}N(0,\sigma^{2}). |  |

As mentioned in Section [2.2.3](https://arxiv.org/html/2510.04556v1#S2.SS2.SSS3 "2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing"), the proof is carried out in the following
three steps.

1. 1.

   Represent the Gini index as a statistical functional TT.
2. 2.

   Show that TT is Hadamard differentiable at FY,μ^​(𝐗)F\_{Y,\hat{\mu}(\mathbf{X})}.
3. 3.

   Combine the empirical-process convergence n​(F^Y,μ^​(𝐗)−FY,μ^​(𝐗))↝𝔾F\sqrt{n}\bigl(\hat{F}\_{Y,\hat{\mu}(\mathbf{X})}-F\_{Y,\hat{\mu}(\mathbf{X})}\bigr)\rightsquigarrow\mathbb{G}\_{F} with the
   functional Delta Method to obtain
   n​(G^Y,μ^​(𝐗)−GY,μ^​(𝐗))→𝑑N​(0,σ2)\sqrt{n}\bigl(\hat{G}\_{Y,\hat{\mu}(\mathbf{X})}-G\_{Y,\hat{\mu}(\mathbf{X})}\bigr)\xrightarrow{d}N(0,\sigma^{2}).

We carry out these steps of the proof in the following subsections.

###### Proof of Theorem [1](https://arxiv.org/html/2510.04556v1#Thmtheorem1 "Theorem 1 (Asymptotic Normality of the Gini Index). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing").

### A.1 Gini Index as a Statistical Functional T

In the following, we adapt techniques from [[7](https://arxiv.org/html/2510.04556v1#bib.bib7)], as
well as insights from Proposition 4.1 in [[31](https://arxiv.org/html/2510.04556v1#bib.bib31)].
Recall that the Gini index is formally defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | GY,μ^​(𝐗):=∫01CAPY,μ^​(𝐗)⁡(α)​𝑑α−12∫01CAPY,Y⁡(α)​𝑑α−12.G\_{Y,\hat{\mu}(\mathbf{X})}:=\frac{\int\_{0}^{1}\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha)\,d\alpha-\frac{1}{2}}{\int\_{0}^{1}\operatorname{CAP}\_{Y,Y}(\alpha)\,d\alpha-\frac{1}{2}}. |  | (7) |

We start by reformulating the numerator.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01CAPY,μ^​(𝐗)⁡(α)​𝑑α−12\displaystyle\int\_{0}^{1}\operatorname{CAP}\_{Y,\hat{\mu}(\mathbf{X})}(\alpha)d\alpha-\frac{1}{2} | =Def. [4](https://arxiv.org/html/2510.04556v1#Thmdefinition4 "Definition 4 (Cumulative accuracy profile). ‣ 2.2.3 Gini Index ‣ 2.2 Auto-Calibration, Metrics and their Properties ‣ 2 Theoretical Background and Related Work ‣ Gini-based Model Monitoring: A General Framework with an Application to Non-life Insurance Pricing")​∫011𝔼​[Y]​𝔼​[Y​𝟙{μ^​(𝐗)>Fμ^​(𝐗)−1​(1−α)}]​𝑑α−12\displaystyle\overset{\text{Def. \ref{def:CAP}}}{=}\int\_{0}^{1}\frac{1}{\mathbb{E}[Y]}\mathbb{E}\left[Y\mathbbm{1}\_{\left\{\hat{\mu}(\mathbf{X})>F^{-1}\_{\hat{\mu}(\mathbf{X})}(1-\alpha)\right\}}\right]d\alpha-\frac{1}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1)​∫011𝔼​[Y]​𝔼​[𝔼​[Y​𝟙{μ^​(𝐗)>Fμ^​(𝐗)−1​(1−α)}|𝐗]]​𝑑α−12\displaystyle\overset{(1)}{=}\int\_{0}^{1}\frac{1}{\mathbb{E}[Y]}\mathbb{E}\left[\mathbb{E}\left[Y\mathbbm{1}\_{\left\{\hat{\mu}(\mathbf{X})>F^{-1}\_{\hat{\mu}(\mathbf{X})}(1-\alpha)\right\}}\bigg|\ \mathbf{X}\right]\right]d\alpha-\frac{1}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2)​∫011𝔼​[Y]​𝔼​[𝔼​[Y∣𝐗]​𝟙{μ^​(𝐗)>Fμ^​(𝐗)−1​(1−α)}]​𝑑α−12\displaystyle\overset{(2)}{=}\int\_{0}^{1}\frac{1}{\mathbb{E}[Y]}\mathbb{E}\left[\mathbb{E}\left[Y\mid\mathbf{X}\right]\mathbbm{1}\_{\left\{\hat{\mu}(\mathbf{X})>F^{-1}\_{\hat{\mu}(\mathbf{X})}(1-\alpha)\right\}}\right]d\alpha-\frac{1}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(3)​∫011𝔼​[Y]​𝔼​[μ^​(𝐗)​𝟙{μ^​(𝐗)>Fμ^​(𝐗)−1​(1−α)}]​𝑑α−12\displaystyle\overset{(3)}{=}\int\_{0}^{1}\frac{1}{\mathbb{E}[Y]}\mathbb{E}\left[\hat{\mu}(\mathbf{X})\mathbbm{1}\_{\left\{\hat{\mu}(\mathbf{X})>F^{-1}\_{\hat{\mu}(\mathbf{X})}(1-\alpha)\right\}}\right]d\alpha-\frac{1}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(4)​1𝔼​[Y]​∫01∫0∞μ​𝟙{μ>Fμ^​(𝐗)−1​(1−α)}​𝑑Fμ^​(𝐗)​(μ)​𝑑α−12\displaystyle\overset{(4)}{=}\frac{1}{\mathbb{E}[Y]}\int\_{0}^{1}\int\_{0}^{\infty}\mu\mathbbm{1}\_{\left\{\mu>F^{-1}\_{\hat{\mu}(\mathbf{X})}(1-\alpha)\right\}}dF\_{\hat{\mu}(\mathbf{X})}(\mu)\ d\alpha-\frac{1}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(5)​1𝔼​[Y]​∫0∞μ​∫1−Fμ^​(𝐗)​(μ)1𝑑α​𝑑Fμ^​(𝐗)​(μ)−12\displaystyle\overset{(5)}{=}\frac{1}{\mathbb{E}[Y]}\int\_{0}^{\infty}\mu\int\_{1-F\_{\hat{\mu}(\mathbf{X})}(\mu)}^{1}d\alpha\ dF\_{\hat{\mu}(\mathbf{X})}(\mu)-\frac{1}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(6)​1𝔼​[Y]​∫0∞μ​Fμ^​(𝐗)​(μ)​𝑑Fμ^​(𝐗)​(μ)−12\displaystyle\overset{(6)}{=}\frac{1}{\mathbb{E}[Y]}\int\_{0}^{\infty}\mu F\_{\hat{\mu}(\mathbf{X})}(\mu)\ dF\_{\hat{\mu}(\mathbf{X})}(\mu)-\frac{1}{2} |  |

The arguments rely on the tower property (1), basic properties of conditional
expectations (2), the fact that the regression function is auto-calibrated (3),
formulation of the expectation as a Riemann-Stieltjes integral (4),
interchanging the order of integration and using that Fμ^−1F^{-1}\_{\hat{\mu}} is
non-decreasing and left-continuous (5) and finally evaluating the inner
integral (6).
  
  
For the denominator, we can follow similar steps and obtain:

|  |  |  |
| --- | --- | --- |
|  | ∫01CAPY,Y⁡(α)​𝑑α−12=1𝔼​[Y]​∫0∞y​FY​(y)​𝑑FY​(y)−12.\int\_{0}^{1}\operatorname{CAP}\_{Y,Y}(\alpha)d\alpha-\frac{1}{2}=\frac{1}{\mathbb{E}[Y]}\int\_{0}^{\infty}yF\_{Y}(y)\ dF\_{Y}(y)-\frac{1}{2}. |  |

Using the expressions for the numerator and denominator derived above, we can
now express the Gini index as their ratio and reformulate it as follows.

|  |  |  |  |
| --- | --- | --- | --- |
|  | GY,μ^​(𝐗)\displaystyle G\_{Y,\hat{\mu}(\mathbf{X})} | =1𝔼​[Y]​∫0∞μ​Fμ^​(𝐗)​(μ)​𝑑Fμ^​(𝐗)​(μ)−121𝔼​[Y]​∫0∞y​FY​(y)​𝑑FY​(y)−12\displaystyle=\frac{\frac{1}{\mathbb{E}[Y]}\int\_{0}^{\infty}\mu F\_{\hat{\mu}(\mathbf{X})}(\mu)\,dF\_{\hat{\mu}(\mathbf{X})}(\mu)-\frac{1}{2}}{\frac{1}{\mathbb{E}[Y]}\int\_{0}^{\infty}yF\_{Y}(y)\,dF\_{Y}(y)-\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1)​∫0∞2​μ​Fμ^​(𝐗)​(μ)​𝑑Fμ^​(𝐗)​(μ)−𝔼​[Y]∫0∞2​y​FY​(y)​𝑑FY​(y)−𝔼​[Y]\displaystyle\overset{(1)}{=}\frac{\int\_{0}^{\infty}2\mu F\_{\hat{\mu}(\mathbf{X})}(\mu)\,dF\_{\hat{\mu}(\mathbf{X})}(\mu)-\mathbb{E}[Y]}{\int\_{0}^{\infty}2yF\_{Y}(y)\,dF\_{Y}(y)-\mathbb{E}[Y]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2)​∫0∞2​μ​Fμ^​(𝐗)​(μ)​𝑑Fμ^​(𝐗)​(μ)−𝔼​[μ^​(𝐗)]∫0∞2​y​FY​(y)​𝑑FY​(y)−𝔼​[Y]\displaystyle\overset{(2)}{=}\frac{\int\_{0}^{\infty}2\mu F\_{\hat{\mu}(\mathbf{X})}(\mu)\,dF\_{\hat{\mu}(\mathbf{X})}(\mu)-\mathbb{E}[\hat{\mu}(\mathbf{X})]}{\int\_{0}^{\infty}2yF\_{Y}(y)\,dF\_{Y}(y)-\mathbb{E}[Y]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(3)​∫0∞2​μ​Fμ^​(𝐗)​(μ)​𝑑Fμ^​(𝐗)​(μ)−∫0∞μ​𝑑Fμ^​(𝐗)​(μ)∫0∞2​y​FY​(y)​𝑑FY​(y)−∫0∞y​𝑑FY​(y)\displaystyle\overset{(3)}{=}\frac{\int\_{0}^{\infty}2\mu F\_{\hat{\mu}(\mathbf{X})}(\mu)\,dF\_{\hat{\mu}(\mathbf{X})}(\mu)-\int\_{0}^{\infty}\mu\,dF\_{\hat{\mu}(\mathbf{X})}(\mu)}{\int\_{0}^{\infty}2yF\_{Y}(y)\,dF\_{Y}(y)-\int\_{0}^{\infty}y\,dF\_{Y}(y)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(4)​∫0∞(2​μ​Fμ^​(𝐗)​(μ)−μ)​𝑑Fμ^​(𝐗)​(μ)∫0∞(2​y​FY​(y)−y)​𝑑FY​(y)\displaystyle\overset{(4)}{=}\frac{\int\_{0}^{\infty}\left(2\mu F\_{\hat{\mu}(\mathbf{X})}(\mu)-\mu\right)\,dF\_{\hat{\mu}(\mathbf{X})}(\mu)}{\int\_{0}^{\infty}\left(2yF\_{Y}(y)-y\right)\,dF\_{Y}(y)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(5)​∫[0,∞)2[2​μ​(∫[0,∞)2𝟙{t∈[0,μ]}​𝑑F(μ^​(𝐗),Y)​(t,s))−μ]​𝑑F(μ^​(𝐗),Y)​(μ,y)∫[0,∞)2[2​y​(∫[0,∞)2𝟙{s∈[0,y]}​𝑑F(μ^​(𝐗),Y)​(t,s))−y]​𝑑F(μ^​(𝐗),Y)​(μ,y)\displaystyle\overset{(5)}{=}\frac{\int\_{[0,\infty)^{2}}\left[2\mu\left(\int\_{[0,\infty)^{2}}\mathbbm{1}\_{\left\{t\in[0,\mu]\right\}}\,dF\_{(\hat{\mu}(\mathbf{X}),Y)}(t,s)\right)-\mu\right]\,dF\_{(\hat{\mu}(\mathbf{X}),Y)}(\mu,y)}{\int\_{[0,\infty)^{2}}\left[2y\left(\int\_{[0,\infty)^{2}}\mathbbm{1}\_{\left\{s\in[0,y]\right\}}\,dF\_{(\hat{\mu}(\mathbf{X}),Y)}(t,s)\right)-y\right]\,dF\_{(\hat{\mu}(\mathbf{X}),Y)}(\mu,y)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T1​(F(μ^​(𝐗),Y))T2​(F(μ^​(𝐗),Y))=:T(F(μ^​(𝐗),Y)).\displaystyle=\frac{T\_{1}(F\_{(\hat{\mu}(\mathbf{X}),Y)})}{T\_{2}(F\_{(\hat{\mu}(\mathbf{X}),Y)})}=:T(F\_{(\hat{\mu}(\mathbf{X}),Y)}). |  |

Here we multiply the numerator and denominator by 2​𝔼​[Y]2\mathbb{E}[Y] in (1), use the fact
that auto-calibration implies unbiasedness in (2), rewrite the expectations as
Riemann-Stieltjes integrals in (3), combine the integrands in (4), and finally
express the distribution functions in terms of the joint distribution in (5).
This completes the first step of the proof, as we express the Gini index as a
functional TT of the joint distribution function F(μ^​(𝐗),Y)F\_{(\hat{\mu}(\mathbf{X}),Y)}.

### A.2 Hadamard-Differentiability of the Functional T

Before we start, we refer to Section 3.10 in [[28](https://arxiv.org/html/2510.04556v1#bib.bib28)]
regarding Hadamard-differentiability.
Let 𝔉\mathfrak{F} be the normed linear spaces of all linear combinations of
CDF’s of random variables with finite expectation.
  
  
Note that the functional TT can be expressed as the ratio of two functionals T1T\_{1} and T2T\_{2},
where T1T\_{1} is the numerator and T2T\_{2} is the denominator of TT.
  
  
We examine the denominator T2T\_{2} and represent it
as a functional T~2​(⋅)\tilde{T}\_{2}(\cdot) of FYF\_{Y} that is Hadamard-differentiable at FYF\_{Y}.
The same arguments apply to the numerator T1T\_{1}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | T2​(F(μ^​(𝐗),Y))\displaystyle T\_{2}(F\_{\left(\hat{\mu}(\mathbf{X}),Y\right)}) | =∫[0,∞)2[2​y​(∫[0,∞)2𝟙{s∈[0,y]}​𝑑F(μ^​(𝐗),Y)​(t,s))−y]​𝑑F(μ^​(𝐗),Y)​(μ,y)\displaystyle=\int\_{[0,\infty)^{2}}\left[2y\left(\int\_{[0,\infty)^{2}}\mathbbm{1}\_{\left\{s\in[0,y]\right\}}\,dF\_{(\hat{\mu}(\mathbf{X}),Y)}(t,s)\right)-y\right]\,dF\_{(\hat{\mu}(\mathbf{X}),Y)}(\mu,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞2yFY(y)−ydFY(y)=:T~2(FY),\displaystyle=\int\_{0}^{\infty}2yF\_{Y}(y)-y\ dF\_{Y}(y)=:\tilde{T}\_{2}(F\_{Y}), |  |

We can split T~2​(FY)\tilde{T}\_{2}(F\_{Y}) into two functionals T~2,a\tilde{T}\_{2,a} and T~2,b\tilde{T}\_{2,b} such that T~2​(FY)=T~2,a​(FY)−T~2,b​(FY)\tilde{T}\_{2}(F\_{Y})=\tilde{T}\_{2,a}(F\_{Y})-\tilde{T}\_{2,b}(F\_{Y}) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | T~2,a​(FY)\displaystyle\tilde{T}\_{2,a}(F\_{Y}) | :=∫0∞2​y​FY​(y)​𝑑FY​(y),\displaystyle=\int\_{0}^{\infty}2yF\_{Y}(y)\,dF\_{Y}(y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | T~2,b​(FY)\displaystyle\tilde{T}\_{2,b}(F\_{Y}) | :=∫0∞y​𝑑FY​(y).\displaystyle=\int\_{0}^{\infty}y\,dF\_{Y}(y). |  |

By showing that both T~2,a\tilde{T}\_{2,a} and T~2,b\tilde{T}\_{2,b} are
Hadamard-differentiable at FYF\_{Y}, we
show that T~2\tilde{T}\_{2} is Hadamard-differentiable at FYF\_{Y} by the Chain Rule (Lemma 3.10.9 in [[28](https://arxiv.org/html/2510.04556v1#bib.bib28)]).
  
  
Recall that a functional T:𝔉→ℝT:\mathfrak{F}\rightarrow\mathbb{R} is called Hadamard-differentiable
at FYF\_{Y} if there is a continuous linear map TFY′:𝔉→ℝT^{\prime}\_{F\_{Y}}:\mathfrak{F}\rightarrow\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | supH∈K,FY+t​H∈𝔉‖T​(FY+t​H)−T​(FY)t−T′​(H)‖→0, as ​t→0,\displaystyle\sup\limits\_{H\in K,\ F\_{Y}+tH\in\mathfrak{F}}\left\lVert\frac{T(F\_{Y}+tH)-T(F\_{Y})}{t}-T^{\prime}(H)\right\rVert\rightarrow 0,\text{ as }t\to 0, |  |

for every compact K⊂𝔉K\subset\mathfrak{F} (see Equation (3.10.1) in [[28](https://arxiv.org/html/2510.04556v1#bib.bib28)]).
  
  
For T~2,b\tilde{T}\_{2,b} we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T~2,b​(FY+t​H)−T~2,b​(FY)t\displaystyle\frac{\tilde{T}\_{2,b}(F\_{Y}+tH)-\tilde{T}\_{2,b}(F\_{Y})}{t} | =1t​(∫0∞y​d​(FY​(y)+t​H​(y))−∫0∞y​𝑑FY​(y))\displaystyle=\frac{1}{t}\left(\int\_{0}^{\infty}y\,d(F\_{Y}(y)+tH(y))-\int\_{0}^{\infty}y\,dF\_{Y}(y)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞y​𝑑H​(y).\displaystyle=\int\_{0}^{\infty}y\,dH(y). |  |

Setting T~2,b′​(H):=∫0∞y​𝑑H​(y)\tilde{T}^{\prime}\_{2,b}(H):=\int\_{0}^{\infty}y\,dH(y), it is left to
show that T~2,b′\tilde{T}^{\prime}\_{2,b} is a continuous linear map.
Linearity follows directly from the linearity of the Riemann-Stieltjes
integral.
To show continuity, we need to show that for a sequence Hn→HH\_{n}\to H in
𝔉\mathfrak{F} it holds that T~2,b′​(Hn)→T~2,b′​(H)\tilde{T}^{\prime}\_{2,b}(H\_{n})\to\tilde{T}^{\prime}\_{2,b}(H).

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞\displaystyle\lim\_{n\to\infty} | |T~2,b′​(Hn)−T~2,b′​(H)|=limn→∞|∫0∞y​𝑑Hn​(y)−∫0∞y​𝑑H​(y)|\displaystyle\left|\tilde{T}^{\prime}\_{2,b}(H\_{n})-\tilde{T}^{\prime}\_{2,b}(H)\right|=\lim\_{n\to\infty}\left|\int\_{0}^{\infty}y\,dH\_{n}(y)-\int\_{0}^{\infty}y\,dH(y)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1)​limn→∞|∫0∞y​d​(Hn​(y)−H​(y))|\displaystyle\overset{(1)}{=}\lim\limits\_{n\to\infty}\left|\int\_{0}^{\infty}y\ d(H\_{n}(y)-H(y))\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2)​limn→∞|∫0my​d​(Hn​(y)−H​(y))+∫m∞y​d​(Hn​(y)−H​(y))|\displaystyle\overset{(2)}{=}\lim\limits\_{n\to\infty}\left|\int\_{0}^{m}y\ d(H\_{n}(y)-H(y))+\int\_{m}^{\infty}y\ d(H\_{n}(y)-H(y))\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(3)​limn→∞|[y​(Hn​(y)−H​(y))]0m−∫0mHn​(y)−H​(y)​d​y+∫m∞y​d​(Hn​(y)−H​(y))|\displaystyle\overset{(3)}{=}\lim\limits\_{n\to\infty}\left|\big[y(H\_{n}(y)-H(y))\big]\_{0}^{m}-\int\_{0}^{m}H\_{n}(y)-H(y)\ dy+\int\_{m}^{\infty}y\ d(H\_{n}(y)-H(y))\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(4)​limn→∞|m​(Hn​(m)−H​(m))|+limn→∞|∫0mHn​(y)−H​(y)​d​y|+limn→∞|∫m∞y​d​(Hn​(y)−H​(y))|\displaystyle\overset{(4)}{\leq}\lim\limits\_{n\to\infty}\left|m(H\_{n}(m)-H(m))\right|+\lim\limits\_{n\to\infty}\left|\int\_{0}^{m}H\_{n}(y)-H(y)\ dy\right|+\lim\limits\_{n\to\infty}\left|\int\_{m}^{\infty}y\ d(H\_{n}(y)-H(y))\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(5)​limn→∞|∫m∞y​d​(Hn​(y)−H​(y))|\displaystyle\overset{(5)}{=}\lim\limits\_{n\to\infty}\left|\int\_{m}^{\infty}y\ d(H\_{n}(y)-H(y))\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(6)​limn→∞|∫m∞y​𝑑Hn​(y)|+limn→∞|∫m∞y​𝑑H​(y)|,\displaystyle\overset{(6)}{\leq}\lim\limits\_{n\to\infty}\left|\int\_{m}^{\infty}y\ dH\_{n}(y)\right|+\lim\limits\_{n\to\infty}\left|\int\_{m}^{\infty}y\ dH(y)\right|, |  |

where we use the linearity of the integral in (1), split the integral at some point mm (2),
use integration by parts in (3), and apply the triangle inequality in (4).
The first two terms vanish because the supremum of |Hn​(y)−H​(y)||H\_{n}(y)-H(y)| converges to
zero for Hn→HH\_{n}\to H and (6) uses again the triangle inequality.
Finally note that HnH\_{n} and HH are in 𝔉\mathfrak{F}, so they can be
represented as linear combinations of CDF’s with finite expectation.
Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫m∞y​𝑑H​(y)=∫m∞y​d​(∑i=1k^λ^i​H^i​(y))=∑i=1k^λ^i​∫m∞y​𝑑H^i​(y).\int\_{m}^{\infty}y\ dH(y)=\int\_{m}^{\infty}y\ d\left(\sum\_{i=1}^{\hat{k}}\hat{\lambda}\_{i}\hat{H}\_{i}(y)\right)=\sum\_{i=1}^{\hat{k}}\hat{\lambda}\_{i}\int\_{m}^{\infty}y\ d\hat{H}\_{i}(y). |  | (8) |

Furthermore, with the same argument as in the proof of Theorem 3.5 in
[[3](https://arxiv.org/html/2510.04556v1#bib.bib3)], we can state for a given ϵ\epsilon there
is an mm such that ∫m∞y​𝑑H^i​(y)<ϵ\int\_{m}^{\infty}y\ d\hat{H}\_{i}(y)<\epsilon for
all i=1,…,k^i=1,\ldots,\hat{k}.
And therefore there is a constant CC s.t.
|∫m∞y​𝑑H​(y)|<ϵ​C\left|\int\_{m}^{\infty}y\ dH(y)\right|<\epsilon C.
Since we can apply the same argument to the integral with respect to HnH\_{n}, we can conclude
that

|  |  |  |
| --- | --- | --- |
|  | limn→∞|T~2,b′​(Hn)−T~2,b′​(H)|≤ϵ​C~.\lim\_{n\to\infty}\left|\tilde{T}^{\prime}\_{2,b}(H\_{n})-\tilde{T}^{\prime}\_{2,b}(H)\right|\leq\epsilon\tilde{C}. |  |

But since ϵ\epsilon is arbitrary, we show the continuity of
T~2,b′\tilde{T}^{\prime}\_{2,b}.
  
  
For T~2,a\tilde{T}\_{2,a} we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T~2,a​(FY+t​H)−T~2,a​(FY)t\displaystyle\frac{\tilde{T}\_{2,a}(F\_{Y}+tH)-\tilde{T}\_{2,a}(F\_{Y})}{t} | =1t​(∫0∞2​y​(FY​(y)+t​H​(y))​d​(FY​(y)+t​H​(y))−∫0∞2​y​FY​(y)​𝑑FY​(y))\displaystyle=\frac{1}{t}\left(\int\_{0}^{\infty}2y(F\_{Y}(y)+tH(y))\,d(F\_{Y}(y)+tH(y))-\int\_{0}^{\infty}2yF\_{Y}(y)\,dF\_{Y}(y)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞2​y​H​(y)​𝑑FY​(y)+∫0∞2​y​FY​(y)​𝑑H​(y)+t​∫0∞2​y​H​(y)​𝑑H​(y).\displaystyle=\int\_{0}^{\infty}2yH(y)\,dF\_{Y}(y)+\int\_{0}^{\infty}2yF\_{Y}(y)\,dH(y)+t\int\_{0}^{\infty}2yH(y)\,dH(y). |  |

Setting T~2,a′​(H):=∫0∞2​y​H​(y)​𝑑FY​(y)+∫0∞2​y​FY​(y)​𝑑H​(y)\tilde{T}^{\prime}\_{2,a}(H):=\int\_{0}^{\infty}2yH(y)\,dF\_{Y}(y)+\int\_{0}^{\infty}2yF\_{Y}(y)\,dH(y), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | supH∈K,FY+t​H∈𝔉\displaystyle\sup\limits\_{H\in K,\ F\_{Y}+tH\in\mathfrak{F}} | |T2,a​(FY+t​H)−T2,a​(FY)t−T2,a′​(H)|=supH∈K,FY+t​H∈𝔉|t​∫0∞2​y​H​(y)​𝑑H​(y)|\displaystyle\left|\frac{T\_{2,a}(F\_{Y}+tH)-T\_{2,a}(F\_{Y})}{t}-T\_{2,a}^{\prime}(H)\right|=\sup\limits\_{H\in K,\ F\_{Y}+tH\in\mathfrak{F}}\left|t\int\_{0}^{\infty}2yH(y)\,dH(y)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(1)​2​|t|​C1​supH∈K|∫0∞y​𝑑H​(y)|\displaystyle\overset{(1)}{\leq}2\left|t\right|C\_{1}\sup\limits\_{H\in K}\left|\int\_{0}^{\infty}y\,dH(y)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(2)​2​|t|​C1​C2→0, as ​t→0,\displaystyle\overset{(2)}{\leq}2\left|t\right|C\_{1}C\_{2}\rightarrow 0,\text{ as }t\to 0, |  |

where (1) uses the fact that HH is a linear combination of CDF’s and therefore bounded by some constant C1C\_{1},
and (2) uses that HH is a linear combination of CDF’s with finite expectation and therefore ∫0∞y​𝑑H​(y)\int\_{0}^{\infty}y\,dH(y) is bounded by some constant C2C\_{2}.
  
  
So it is left to show that T~2,a′\tilde{T}^{\prime}\_{2,a} is a continuous linear map.
Linearity follows again directly from the linearity of the Riemann-Stieltjes
integral.
To show continuity, we need to show that for a sequence Hn→HH\_{n}\to H in
𝔉\mathfrak{F} it holds that T~2,a′​(Hn)→T~2,a′​(H)\tilde{T}^{\prime}\_{2,a}(H\_{n})\to\tilde{T}^{\prime}\_{2,a}(H).

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞\displaystyle\lim\_{n\to\infty} | |T~2,a′​(Hn)−T~2,a′​(H)|\displaystyle\left|\tilde{T}^{\prime}\_{2,a}(H\_{n})-\tilde{T}^{\prime}\_{2,a}(H)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limn→∞|∫0∞2​y​Hn​(y)​𝑑FY​(y)+∫0∞2​y​FY​(y)​𝑑Hn​(y)\displaystyle=\lim\_{n\to\infty}\Bigg|\int\_{0}^{\infty}2yH\_{n}(y)\,dF\_{Y}(y)+\int\_{0}^{\infty}2yF\_{Y}(y)\,dH\_{n}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0∞2yH(y)dFY(y)−∫0∞2yFY(y)dH(y)|\displaystyle\phantom{=\lim\_{n\to\infty}\Bigg|}-\int\_{0}^{\infty}2yH(y)\,dF\_{Y}(y)-\int\_{0}^{\infty}2yF\_{Y}(y)\,dH(y)\Bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤limn→∞|∫0∞2​y​(Hn​(y)−H​(y))​𝑑FY​(y)|+limn→∞|∫0∞2​y​FY​(y)​d​(Hn​(y)−H​(y))|.\displaystyle\leq\lim\_{n\to\infty}\left|\int\_{0}^{\infty}2y(H\_{n}(y)-H(y))\,dF\_{Y}(y)\right|+\lim\_{n\to\infty}\left|\int\_{0}^{\infty}2yF\_{Y}(y)\,d(H\_{n}(y)-H(y))\right|. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1)​limn→∞|∫0∞2​y​(Hn​(y)−H​(y))​𝑑FY​(y)|\displaystyle\overset{(1)}{=}\lim\_{n\to\infty}\left|\int\_{0}^{\infty}2y(H\_{n}(y)-H(y))\,dF\_{Y}(y)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(2)​limn→∞supy|Hn​(y)−H​(y)|⋅|∫0∞2​y​𝑑FY​(y)|=0,\displaystyle\overset{(2)}{\leq}\lim\_{n\to\infty}\sup\limits\_{y}\left|H\_{n}(y)-H(y)\right|\cdot\left|\int\_{0}^{\infty}2y\,dF\_{Y}(y)\right|=0, |  |

where (1) uses that FYF\_{Y} is bounded and the same arguments as in T2,b′T^{\prime}\_{2,b} to show that the second term vanishes,
and (2) uses that FYF\_{Y} is a CDF with finite expectation and therefore ∫0∞2​y​𝑑FY​(y)\int\_{0}^{\infty}2y\,dF\_{Y}(y) is finite.
  
  
We have shown that both T~2,a\tilde{T}\_{2,a} and T~2,b\tilde{T}\_{2,b} are Hadamard-differentiable at FYF\_{Y},
and therefore T~2\tilde{T}\_{2} is Hadamard-differentiable at FYF\_{Y}.
By applying the same arguments to T1T\_{1}, we conclude that T1T\_{1} is
Hadamard-differentiable at F(μ^​(𝐗),Y)F\_{\left(\hat{\mu}(\mathbf{X}),Y\right)}.
Finally, by the Chain Rule (Lemma 3.10.9 in [[28](https://arxiv.org/html/2510.04556v1#bib.bib28)]), we
conclude that T=T1T2T=\frac{T\_{1}}{T\_{2}} is Hadamard-differentiable at
F(μ^​(𝐗),Y)F\_{\left(\hat{\mu}(\mathbf{X}),Y\right)}.
Note T2​(F(μ^​(𝐗),Y))>0T\_{2}\left(F\_{\left(\hat{\mu}(\mathbf{X}),Y\right)}\right)>0, because
∫01CAPY,Y⁡(α)​𝑑α−12>0\int\_{0}^{1}\operatorname{CAP}\_{Y,Y}(\alpha)d\alpha-\frac{1}{2}>0 and 𝔼​[Y]\mathbb{E}[Y] is
finite.
  
  
We conclude that the Gini index GY,μ^​(𝐗)G\_{Y,\hat{\mu}(\mathbf{X})} can be represented as a functional TT that is Hadamard-differentiable at F(μ^​(𝐗),Y)F\_{\left(\hat{\mu}(\mathbf{X}),Y\right)}.

### A.3 Application of the Functional Delta Method

Using Example 2.1.3 and 2.8.2 Donsker Theorem from
[[28](https://arxiv.org/html/2510.04556v1#bib.bib28)] for the empirical distribution function with
(Yi,μ^​(𝐗i))(Y\_{i},\hat{\mu}(\mathbf{X}\_{i})) i.i.d.\mathrm{i.i.d.}, it holds that

|  |  |  |
| --- | --- | --- |
|  | n​(F^Y,μ^​(𝐗)−FY,μ^​(𝐗))→𝑑𝔾,\displaystyle\sqrt{n}\left(\hat{F}\_{Y,\hat{\mu}(\mathbf{X})}-F\_{Y,\hat{\mu}(\mathbf{X})}\right)\xrightarrow{d}\mathbb{G}, |  |

where 𝔾\mathbb{G} is a tight, Borel measurable Gaussian process with mean zero, called *Brownian bridge*.
  
  
Finally, we apply the delta method (Theorem 3.10.4 [[28](https://arxiv.org/html/2510.04556v1#bib.bib28)]) to conclude:

|  |  |  |
| --- | --- | --- |
|  | n​(G^Y,μ^​(𝐗)−GY,μ^​(𝐗))→𝑑T′​(𝔾),\displaystyle\sqrt{n}\left(\hat{G}\_{Y,\hat{\mu}(\mathbf{X})}-G\_{Y,\hat{\mu}(\mathbf{X})}\right)\xrightarrow{d}T^{\prime}(\mathbb{G}), |  |

where T′​(FY,μ^​(𝐗))T^{\prime}(F\_{Y,\hat{\mu}(\mathbf{X})}) is the Hadamard derivative of the Gini index at FY,μ^​(𝐗)F\_{Y,\hat{\mu}(\mathbf{X})}, which is (per definition of the Hadamard derivative) a continuous and linear functional.
By applying Lemma 3.10.8 in [[28](https://arxiv.org/html/2510.04556v1#bib.bib28)] we observe that
T′​(𝔾)T^{\prime}(\mathbb{G}) is again normally distributed, since it is a linear functional
of the Gaussian process 𝔾\mathbb{G}.
Thus we finally conclude that the Gini index is asymptotically normal.

∎