---
authors:
- C. Evans Hedges
doc_id: arxiv:2512.03242v1
family_id: arxiv:2512.03242
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1. Introduction
url_abs: http://arxiv.org/abs/2512.03242v1
url_html: https://arxiv.org/html/2512.03242v1
venue: arXiv q-fin
version: 1
year: 2025
---

A Theoretical Framework Bridging Model Validation and Loss Ratio in Insurance

C. Evans Hedges111 Lemonade Insurance

Keywords: Model validation, Loss ratio, Insurance pricing, Business impact, Correlation, Elasticity

Abstract

This paper establishes the first analytical relationship between predictive model performance and loss ratio in insurance pricing. We derive a closed-form formula connecting the Pearson correlation between predicted and actual losses to expected loss ratio. The framework proves that model improvements exhibit diminishing marginal returns, analytically confirming the actuarial intuition to prioritize poorly performing models. We introduce the Loss Ratio Error metric for quantifying business impact across frequency, severity, and pure premium models. Simulations show reliable predictions under stated assumptions, with graceful degradation under assumption violations. This framework transforms model investment decisions from qualitative intuition to quantitative cost-benefit analysis.

## 1.  Introduction

In insurance pricing, predictive models are routinely evaluated using statistical performance metrics such as Gini coefficient, AUC, and Mean Absolute Percentage Error (MAPE). These metrics are indispensable for assessing model fit, yet they remain fundamentally disconnected from the business outcomes that ultimately matter to insurers, such as profitability and loss ratio. While prior research has documented that more predictive models tend to yield better portfolio performance through improved risk segmentation, lower adverse selection, and competitive advantage, these findings have been empirical or heuristic in nature. It was shown in frees2014insurance that Gini index is proportional to the correlation between the relativity and an out-of-sample profit. However, to our knowledge this is the only work that establishes a direct relationship between a model validation metric and loss ratio.

Translating model performance into business outcomes (profit, loss ratio, growth) is a non-trivial challenge noted throughout the literature. walch2022market provides a direct precedent for our problem framing by comparing different pricing models in commercial auto, showing empirically that better predictive models deliver both improved loss ratios and market share, but without providing analytic formulas. Industry case studies from vendors such as Earnix, Deloitte, and WTW often claim measurable loss ratio improvement from better predictive modeling (earnix2023predictive; deloitte2022insurance; wtwco2023modeling; insurity2024predict). These studies demonstrate practitioner demand for quantifiable business benefits, though their analyses remain anecdotal or simulation-based.

Despite rich literature on insurance demand elasticity (guven2013price; sherden1984auto; hao2018insurance; mossin1968aspects; rothschild1976equilibrium), actuarial model validation practices (cas2019model; lorentzen2022gini), and insurance pricing optimization (buhlmann1967experience), we find a critical gap at their intersection: no existing work provides a closed-form, quantitative connection between a model validation metric and an insurance business outcome. Prior research establishes that better predictive models can improve profitability, and it offers tools to evaluate models as well as tools to optimize pricing using those models. Yet, none of these strands has yielded an analytical framework that starts from a metric like correlation and ends with a precise estimate of percentage improvement in loss ratio.

We address this gap by developing a mathematical framework that establishes a direct relationship between a loss model’s statistical performance and an insurer’s expected loss ratio under clearly stated assumptions. The formula depends solely on model correlation, demand elasticity, and the coefficient of variation of the loss distribution. Using this framework, we prove that marginal improvements in poorly performing models have an outsized impact on loss ratio compared to equivalent improvements in well-performing models which confirms the widespread existing intuition around which predictive modeling efforts will yield the greatest business benefits.

Our framework leads to a natural new metric for evaluating model performance, the Loss Ratio Error (EL​RE\_{LR}). This metric quantifies the expected loss ratio degradation caused by poor model performance and can be computed at the level of severity, frequency, or pure premium. With this metric, as well as the framework for estimating expected loss ratio, we can now quantify the expected business impact of model improvements. This moves the conversation from qualitative (”a better model should lower our loss ratio”) to quantitative and objective (”a model with Pearson correlation of 0.3 vs 0.2 corresponds to a specific percentage improvement in loss ratio, all else equal”) providing a crucial bridge between technical modeling teams and non-technical business decision makers.

To validate the robustness of the theoretical work, we conduct comprehensive simulation studies using grid-based validation and systematic assumption violation testing, demonstrating reliable performance under stated assumptions and graceful degradation under moderate violations.

The core contributions of the following work are threefold. First, we derive a closed-form formula connecting Pearson correlation between predicted and actual losses to expected loss ratio performance. Second, we provide a proof that model improvements exhibit diminishing marginal returns, analytically supporting the widespread actuarial intuition to prioritize improvements in poorly performing models. Third, we establish practical tools including the Loss Ratio Error metric that directly measures the expected loss ratio degradation caused by poor model performance.

## 2.  Mathematical Framework

In this section, we will outline the core assumptions of our framework and derive the core loss ratio formula.

### 2.1.  Primary Assumptions

We denote the true expected loss for a given customer by λ\lambda. We make no assumption about the distribution of λ\lambda, other than that it is positive. While realized losses in any given policy period may be zero for customers who do not file claims, the expected loss λ\lambda represents the underlying risk and is strictly positive for all customers. We assume our loss modeling provides estimated losses for a given customer by λ^=λ​eϵ\hat{\lambda}=\lambda e^{\epsilon} where ϵ∼N​(0,σ2)\epsilon\sim N(0,\sigma^{2}). In particular, we assume that ϵ⟂λ\epsilon\perp\lambda and that ϵ\epsilon is homoskedastic in log space. This log-normal error structure is standard in actuarial modeling (frees2010regression; ohlsson2010non; goldburd2016generalized) and is the natural assumption for GLM models with log-link functions commonly used in insurance pricing (antonio2007use; wuthrich2022statistical). The independence assumption ϵ⟂λ\epsilon\perp\lambda is fundamental to well-specified predictive models and is routinely validated in actuarial practice (cas2019model).

The log-normal multiplicative error structure is particularly realistic for insurance applications where prediction errors tend to be proportional to the underlying risk level—models typically exhibit larger absolute errors for high-risk customers while maintaining reasonable relative accuracy. The independence assumption ϵ⟂λ\epsilon\perp\lambda has a natural economic interpretation: it requires that model errors be uncorrelated with the true underlying risk. Violations of this assumption indicate systematic model bias that actuaries routinely test for and correct during model validation.

We assume that our pricing plan can be simplified to a margin factor MM so that a given customer with estimated losses λ^\hat{\lambda} will be priced at p=M​λ^p=M\hat{\lambda}. This proportional pricing structure reflects a cost-plus-margin approach widely used across the industry (klugman2012loss; denuit2007actuarial).

For a given product line, we model demand using a power law conversion model. We let c​(p)c(p) denote the probability of a customer purchasing a policy at price pp. We assume that c​(p)∝p−ηc(p)\propto p^{-\eta} where η>0\eta>0 is the price elasticity. This iso-elastic demand specification has strong theoretical foundations in insurance economics: mossin1968aspects demonstrated that under expected utility theory, risk-averse consumers will purchase only partial insurance when premiums exceed actuarially fair prices, yielding downward-sloping demand curves. Power-law demand curves with constant elasticity emerge naturally from utility models with constant relative risk aversion and align with empirical evidence across insurance lines (sherden1984auto; babbel1985price; pauly2003price).

### 2.2.  Core Loss Ratio Formula

We begin by establishing a formula for the expected portfolio loss ratio.

###### Lemma 1.

For large portfolios, the expected loss ratio is given by:

|  |  |  |
| --- | --- | --- |
|  | L​R=E​[λ⋅c​(p)]E​[p⋅c​(p)]LR=\frac{E[\lambda\cdot c(p)]}{E[p\cdot c(p)]} |  |

where the expectation is taken over the population distribution of potential customers.

###### Proof.

Consider a pool of NN potential customers indexed by i=1,…,Ni=1,\ldots,N, where customer ii has true losses λi\lambda\_{i}, price pip\_{i}, and conversion probability c​(pi)c(p\_{i}). Only a subset of these customers will actually purchase policies, so we will let Xi∼Bernoulli​(c​(pi))X\_{i}\sim\text{Bernoulli}(c(p\_{i})) indicate whether customer ii converts and price pip\_{i}.

The actual portfolio loss ratio is the ratio of total realized losses to total realized revenue:

|  |  |  |
| --- | --- | --- |
|  | Portfolio LR=∑i=1Nλi​Xi∑i=1Npi​Xi.\text{Portfolio LR}=\frac{\sum\_{i=1}^{N}\lambda\_{i}X\_{i}}{\sum\_{i=1}^{N}p\_{i}X\_{i}}. |  |

Dividing both numerator and denominator by NN we get:

|  |  |  |
| --- | --- | --- |
|  | Portfolio LR=1N​∑i=1Nλi​Xi1N​∑i=1Npi​Xi.\text{Portfolio LR}=\frac{\frac{1}{N}\sum\_{i=1}^{N}\lambda\_{i}X\_{i}}{\frac{1}{N}\sum\_{i=1}^{N}p\_{i}X\_{i}}. |  |

By the law of large numbers, as N→∞N\to\infty:

|  |  |  |
| --- | --- | --- |
|  | 1N​∑i=1Nλi​Xi→E​[λ​X],\frac{1}{N}\sum\_{i=1}^{N}\lambda\_{i}X\_{i}\to E[\lambda X], |  |

and by the law of iterated expectations, we have:

|  |  |  |
| --- | --- | --- |
|  | E​[λ​X]=E​[E​[λ​X|λ]]=E​[λ​E​[X]|λ]=E​[λ​c​(p)|λ]=E​[λ​c​(p)].E[\lambda X]=E[E[\lambda X|\lambda]]=E[\lambda E[X]|\lambda]=E[\lambda c(p)|\lambda]=E[\lambda c(p)]. |  |

By a similar argument, we have:

|  |  |  |
| --- | --- | --- |
|  | 1N​∑i=1Npi​Xi→E​[p​X]=E​[p⋅c​(p)]\frac{1}{N}\sum\_{i=1}^{N}p\_{i}X\_{i}\to E[pX]=E[p\cdot c(p)] |  |

Therefore, for large portfolios, the expected loss ratio is:

|  |  |  |
| --- | --- | --- |
|  | L​R=E​[λ⋅c​(p)]E​[p⋅c​(p)]LR=\frac{E[\lambda\cdot c(p)]}{E[p\cdot c(p)]} |  |

where the expectation is taken over the population distribution of potential customers.
∎

Next we prove a useful lemma relating the correlation between predicted and actual losses to the error variance and loss distribution characteristics. We begin by defining the coefficient of variation for true losses:

###### Definition 1.

The coefficient of variation for true losses is given by:

|  |  |  |
| --- | --- | --- |
|  | C​Vλ=Var​(λ)E​[λ].CV\_{\lambda}=\frac{\sqrt{\text{Var}(\lambda)}}{E[\lambda]}. |  |

###### Lemma 2.

The correlation between our predicted losses λ^\hat{\lambda} and actual losses λ\lambda is given by:

|  |  |  |
| --- | --- | --- |
|  | ρ=e−σ2/2(1+C​Vλ−2)−C​Vλ−2​e−σ2.\rho=\frac{e^{-\sigma^{2}/2}}{\sqrt{(1+CV\_{\lambda}^{-2})-CV\_{\lambda}^{-2}e^{-\sigma^{2}}}}. |  |

###### Proof.

We first compute ρ\rho by establishing the covariance and variance of our predicted losses and actual losses. We note:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(λ^,λ)\displaystyle\text{Cov}(\hat{\lambda},\lambda) | =E​[λ^​λ]−E​[λ^]​E​[λ]\displaystyle=E[\hat{\lambda}\lambda]-E[\hat{\lambda}]E[\lambda] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ2​eε]−E​[λ​eε]​E​[λ].\displaystyle=E[\lambda^{2}e^{\varepsilon}]-E[\lambda e^{\varepsilon}]E[\lambda]. |  |

Since λ⟂ε\lambda\perp\varepsilon:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(λ^,λ)\displaystyle\text{Cov}(\hat{\lambda},\lambda) | =E​[λ2]​E​[eε]−E​[λ]2​E​[eε]\displaystyle=E[\lambda^{2}]E[e^{\varepsilon}]-E[\lambda]^{2}E[e^{\varepsilon}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =eσ2/2​Var⁡(λ).\displaystyle=e^{\sigma^{2}/2}\operatorname{Var}(\lambda). |  |

Next we observe that the variance of our predicted losses is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var⁡(λ^)\displaystyle\operatorname{Var}(\hat{\lambda}) | =E​[λ2​e2​ε]−E​[λ​eε]2\displaystyle=E[\lambda^{2}e^{2\varepsilon}]-E[\lambda e^{\varepsilon}]^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ2]​e2​σ2−E​[λ]2​eσ2\displaystyle=E[\lambda^{2}]e^{2\sigma^{2}}-E[\lambda]^{2}e^{\sigma^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Var⁡(λ)​e2​σ2+E​[λ]2​(e2​σ2−eσ2).\displaystyle=\operatorname{Var}(\lambda)e^{2\sigma^{2}}+E[\lambda]^{2}(e^{2\sigma^{2}}-e^{\sigma^{2}}). |  |

Finally, we have the full correlation expression:

|  |  |  |
| --- | --- | --- |
|  | Corr​(λ^,λ)=eσ2/2e2​σ2+E​[λ]2Var⁡(λ)​(e2​σ2−eσ2).\text{Corr}(\hat{\lambda},\lambda)=\frac{e^{\sigma^{2}/2}}{\sqrt{e^{2\sigma^{2}}+\frac{E[\lambda]^{2}}{\operatorname{Var}(\lambda)}(e^{2\sigma^{2}}-e^{\sigma^{2}})}}. |  |

Next we substitute the coefficient of variation into the correlation expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ\displaystyle\rho | =eσ2/2e2​σ2​(1+C​Vλ−2)−C​Vλ−2​eσ2\displaystyle=\frac{e^{\sigma^{2}/2}}{\sqrt{e^{2\sigma^{2}}(1+CV\_{\lambda}^{-2})-CV\_{\lambda}^{-2}e^{\sigma^{2}}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =eσ2/2eσ2​(1+C​Vλ−2)−C​Vλ−2​e−σ2\displaystyle=\frac{e^{\sigma^{2}/2}}{e^{\sigma^{2}}\sqrt{(1+CV\_{\lambda}^{-2})-CV\_{\lambda}^{-2}e^{-\sigma^{2}}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−σ2/2(1+C​Vλ−2)−C​Vλ−2​e−σ2,\displaystyle=\frac{e^{-\sigma^{2}/2}}{\sqrt{(1+CV\_{\lambda}^{-2})-CV\_{\lambda}^{-2}e^{-\sigma^{2}}}}, |  |

and we arrive at the desired result.
∎

We may now derive our core formula.

###### Theorem 1.

Under the assumptions stated in Section [2.1.](https://arxiv.org/html/2512.03242v1#S2.SS1 "2.1. Primary Assumptions ‣ 2. Mathematical Framework"), the expected loss ratio is given by:

|  |  |  |
| --- | --- | --- |
|  | L​R=1M​(1+ρ2​C​Vλ−2ρ2​(1+C​Vλ−2))2​η−12LR=\frac{1}{M}\left(\frac{1+\rho^{2}CV\_{\lambda}^{-2}}{\rho^{2}(1+CV\_{\lambda}^{-2})}\right)^{\frac{2\eta-1}{2}} |  |

where ρ=Corr​(λ^,λ)\rho=\text{Corr}(\hat{\lambda},\lambda) is the Pearson correlation between predicted and actual losses, and C​Vλ=Var​(λ)E​[λ]CV\_{\lambda}=\frac{\sqrt{\text{Var}(\lambda)}}{E[\lambda]} is the coefficient of variation for true losses.

###### Proof.

Substituting the power law conversion into the Loss Ratio formula from Lemma [1](https://arxiv.org/html/2512.03242v1#Thmlemma1 "Lemma 1. ‣ 2.2. Core Loss Ratio Formula ‣ 2. Mathematical Framework"), we can see:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​R\displaystyle LR | =E​[λ⋅c​(p)]E​[p⋅c​(p)]\displaystyle=\frac{E[\lambda\cdot c(p)]}{E[p\cdot c(p)]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ⋅c​(M​λ^)]E​[M​λ^⋅c​(M​λ^)]\displaystyle=\frac{E[\lambda\cdot c(M\hat{\lambda})]}{E[M\hat{\lambda}\cdot c(M\hat{\lambda})]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ⋅M−η​λ^−η]E​[M​λ^⋅M−η​λ^−η]\displaystyle=\frac{E[\lambda\cdot M^{-\eta}\hat{\lambda}^{-\eta}]}{E[M\hat{\lambda}\cdot M^{-\eta}\hat{\lambda}^{-\eta}]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ⋅λ^−η]M⋅E​[λ^1−η].\displaystyle=\frac{E[\lambda\cdot\hat{\lambda}^{-\eta}]}{M\cdot E[\hat{\lambda}^{1-\eta}]}. |  |

Since λ^=λ​eε\hat{\lambda}=\lambda e^{\varepsilon} and λ⟂ε\lambda\perp\varepsilon, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[λ⋅λ^−η]\displaystyle E[\lambda\cdot\hat{\lambda}^{-\eta}] | =E​[λ⋅(λ​eε)−η]\displaystyle=E[\lambda\cdot(\lambda e^{\varepsilon})^{-\eta}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ1−η​e−η​ε]\displaystyle=E[\lambda^{1-\eta}e^{-\eta\varepsilon}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ1−η]⋅E​[e−η​ε],\displaystyle=E[\lambda^{1-\eta}]\cdot E[e^{-\eta\varepsilon}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[λ^1−η]\displaystyle E[\hat{\lambda}^{1-\eta}] | =E​[(λ​eε)1−η]\displaystyle=E[(\lambda e^{\varepsilon})^{1-\eta}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ1−η​e(1−η)​ε]\displaystyle=E[\lambda^{1-\eta}e^{(1-\eta)\varepsilon}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[λ1−η]⋅E​[e(1−η)​ε].\displaystyle=E[\lambda^{1-\eta}]\cdot E[e^{(1-\eta)\varepsilon}]. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​R\displaystyle LR | =E​[λ1−η]⋅E​[e−η​ε]M⋅E​[λ1−η]⋅E​[e(1−η)​ε]\displaystyle=\frac{E[\lambda^{1-\eta}]\cdot E[e^{-\eta\varepsilon}]}{M\cdot E[\lambda^{1-\eta}]\cdot E[e^{(1-\eta)\varepsilon}]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1M⋅E​[e−η​ε]E​[e(1−η)​ε].\displaystyle=\frac{1}{M}\cdot\frac{E[e^{-\eta\varepsilon}]}{E[e^{(1-\eta)\varepsilon}]}. |  |

Taking expectation with respect to ε\varepsilon yields:

|  |  |  |
| --- | --- | --- |
|  | L​R=1M​exp⁡(12​σ2​(2​η−1)).LR=\frac{1}{M}\exp\left(\frac{1}{2}\sigma^{2}(2\eta-1)\right). |  |

Solving for eσ2e^{\sigma^{2}} using Lemma [2](https://arxiv.org/html/2512.03242v1#Thmlemma2 "Lemma 2. ‣ 2.2. Core Loss Ratio Formula ‣ 2. Mathematical Framework") we get:

|  |  |  |
| --- | --- | --- |
|  | eσ2=1+ρ2​C​Vλ−2ρ2​(1+C​Vλ−2).e^{\sigma^{2}}=\frac{1+\rho^{2}CV\_{\lambda}^{-2}}{\rho^{2}(1+CV\_{\lambda}^{-2})}. |  |

Substituting back into the loss ratio formula yields the desired result.
∎

### 2.3.  Frequency and Severity Decomposition

Many insurance pricing models separate losses into frequency and severity components. We now extend our framework to this common modeling structure.

For frequency and severity we will mirror the assumptions and notation from the loss prediction section. In particular, we use ρf,ρs,C​Vf,C​Vs\rho\_{f},\rho\_{s},CV\_{f},CV\_{s} to denote the correlation and coefficient of variation for frequency and severity respectively. Additionally for a customer, we use f^,s^,f,s\hat{f},\hat{s},f,s to denote the predicted and actual frequency and severity respectively.

As with loss prediction, we will assume that our frequency and severity models have log-normal errors with ϵf∼N​(0,σf2)\epsilon\_{f}\sim N(0,\sigma\_{f}^{2}) and ϵs∼N​(0,σs2)\epsilon\_{s}\sim N(0,\sigma\_{s}^{2}) in log space. We will additionally assume that both frequency and severity and their errors are pairwise independent. We may now state the decomposition theorem.

###### Theorem 2.

Under the assumptions listed above, the expected loss ratio is given by:

|  |  |  |
| --- | --- | --- |
|  | L​R=1M​(1+ρf2​C​Vf−2ρf2​(1+C​Vf−2))2​η−12​(1+ρs2​C​Vs−2ρs2​(1+C​Vs−2))2​η−12LR=\frac{1}{M}\left(\frac{1+\rho\_{f}^{2}CV\_{f}^{-2}}{\rho\_{f}^{2}(1+CV\_{f}^{-2})}\right)^{\frac{2\eta-1}{2}}\left(\frac{1+\rho\_{s}^{2}CV\_{s}^{-2}}{\rho\_{s}^{2}(1+CV\_{s}^{-2})}\right)^{\frac{2\eta-1}{2}} |  |

###### Proof.

First we let λ^=f^⋅s^\hat{\lambda}=\hat{f}\cdot\hat{s}. By independence of frequency and severity errors we have: λ^=λ​eϵf+ϵs\hat{\lambda}=\lambda e^{\epsilon\_{f}+\epsilon\_{s}}. Since ϵf⟂ϵs\epsilon\_{f}\perp\epsilon\_{s} we know ϵf+ϵs∼N​(0,σf2+σs2)\epsilon\_{f}+\epsilon\_{s}\sim N(0,\sigma\_{f}^{2}+\sigma\_{s}^{2}) and by work shown in Theorem [1](https://arxiv.org/html/2512.03242v1#Thmtheorem1 "Theorem 1. ‣ 2.2. Core Loss Ratio Formula ‣ 2. Mathematical Framework") we know:

|  |  |  |
| --- | --- | --- |
|  | L​R=1M​exp⁡(12​(σf2+σs2)​(2​η−1)).LR=\frac{1}{M}\exp\left(\frac{1}{2}(\sigma\_{f}^{2}+\sigma\_{s}^{2})(2\eta-1)\right). |  |

Using Lemma [2](https://arxiv.org/html/2512.03242v1#Thmlemma2 "Lemma 2. ‣ 2.2. Core Loss Ratio Formula ‣ 2. Mathematical Framework") we know:

|  |  |  |
| --- | --- | --- |
|  | e−σf2=ρf2​(1+C​Vf−2)1+ρf2​C​Vf−2,e^{-\sigma\_{f}^{2}}=\frac{\rho\_{f}^{2}(1+CV\_{f}^{-2})}{1+\rho\_{f}^{2}CV\_{f}^{-2}}, |  |

|  |  |  |
| --- | --- | --- |
|  | e−σs2=ρs2​(1+C​Vs−2)1+ρs2​C​Vs−2.e^{-\sigma\_{s}^{2}}=\frac{\rho\_{s}^{2}(1+CV\_{s}^{-2})}{1+\rho\_{s}^{2}CV\_{s}^{-2}}. |  |

Substituting these into the loss ratio formula yields the desired result.
∎

### 2.4.  Model Improvement Analysis

Having established the core loss ratio formula, we now analyze the business impact of model improvements.

###### Observation 1.

When improving a model from correlation ρo​l​d\rho\_{old} to ρn​e​w\rho\_{new}, the loss ratio improvement is:

|  |  |  |
| --- | --- | --- |
|  | L​Rn​e​wL​Ro​l​d=(ρo​l​d2+ρn​e​w2​ρo​l​d2​C​Vλ−2ρn​e​w2+ρn​e​w2​ρo​l​d2​C​Vλ−2)2​η−12\frac{LR\_{new}}{LR\_{old}}=\left(\frac{\rho\_{old}^{2}+\rho\_{new}^{2}\rho\_{old}^{2}CV\_{\lambda}^{-2}}{\rho\_{new}^{2}+\rho\_{new}^{2}\rho\_{old}^{2}CV\_{\lambda}^{-2}}\right)^{\frac{2\eta-1}{2}} |  |

###### Proof.

This follows directly from the core loss ratio formula by taking the ratio of L​Rn​e​wLR\_{new} to L​Ro​l​dLR\_{old} and substituting the respective correlation values.
∎

We note here that by Theorem [2](https://arxiv.org/html/2512.03242v1#Thmtheorem2 "Theorem 2. ‣ 2.3. Frequency and Severity Decomposition ‣ 2. Mathematical Framework"), it trivially follows that this improvement formula can be computed at the level of pure premium modeling (as stated above) as well as frequency or severity, where we need only substitute the pure premium predicted measures with the relevant component model versions, e.g. we swap ρo​l​d\rho\_{old} with ρf,o​l​d\rho\_{f,old}.

We next establish a key property regarding diminishing returns in model improvements.

###### Theorem 3.

For a fixed percentage improvement p>0p>0 in model correlation, the relative loss ratio improvement L​Ro​l​d−L​Rn​e​wL​Ro​l​d\frac{LR\_{old}-LR\_{new}}{LR\_{old}} as well as the absolute loss ratio improvement L​Ro​l​d−L​Rn​e​wLR\_{old}-LR\_{new} are both monotonically decreasing in the starting correlation ρo​l​d\rho\_{old}.

###### Proof.

We fix an improvement percentage p>0p>0. Let ρo​l​d∈(0,11+p)\rho\_{old}\in(0,\frac{1}{1+p}) and ρn​e​w=(1+p)​ρo​l​d\rho\_{new}=(1+p)\rho\_{old}. We therefore have:

|  |  |  |
| --- | --- | --- |
|  | L​Ro​l​d−L​Rn​e​wL​Ro​l​d=1−((1+p)−2+ρo​l​d2​C​Vλ−21+ρo​l​d2​C​Vλ−2)2​η−12\frac{LR\_{old}-LR\_{new}}{LR\_{old}}=1-\left(\frac{(1+p)^{-2}+\rho\_{old}^{2}CV\_{\lambda}^{-2}}{1+\rho\_{old}^{2}CV\_{\lambda}^{-2}}\right)^{\frac{2\eta-1}{2}} |  |

Taking the partial derivative with respect to ρo​l​d\rho\_{old}:

|  |  |  |
| --- | --- | --- |
|  | ∂L​Ro​l​d−L​Rn​e​wL​Ro​l​d∂ρo​l​d=−2​η−12​((1+p)−2+ρo​l​d2​C​Vλ−21+ρo​l​d2​C​Vλ−2)2​η−32​(2​ρo​l​d​C​Vλ−2​(1−(1+p)−2)(1+ρo​l​d2​C​Vλ−2)2).\frac{\partial\frac{LR\_{old}-LR\_{new}}{LR\_{old}}}{\partial\rho\_{old}}=-\frac{2\eta-1}{2}\left(\frac{(1+p)^{-2}+\rho\_{old}^{2}CV\_{\lambda}^{-2}}{1+\rho\_{old}^{2}CV\_{\lambda}^{-2}}\right)^{\frac{2\eta-3}{2}}\left(\frac{2\rho\_{old}CV\_{\lambda}^{-2}\left(1-(1+p)^{-2}\right)}{(1+\rho\_{old}^{2}CV\_{\lambda}^{-2})^{2}}\right). |  |

Since p,C​Vλ−2,ρo​l​d>0p,CV\_{\lambda}^{-2},\rho\_{old}>0, we have ∂L​Ro​l​d−L​Rn​e​wL​Ro​l​d∂ρo​l​d<0\frac{\partial\frac{LR\_{old}-LR\_{new}}{LR\_{old}}}{\partial\rho\_{old}}<0 for all ρo​l​d∈(0,11+p)\rho\_{old}\in(0,\frac{1}{1+p}). Thus, the percentage improvement in Loss Ratio is monotonically decreasing in the starting correlation ρo​l​d\rho\_{old}.

A similar argument shows that the same result holds for the absolute loss ratio improvement L​Ro​l​d−L​Rn​e​wLR\_{old}-LR\_{new}.
∎

We note here that both of the above model improvement results apply directly to frequency or severity models by a direct application of Theorem [2](https://arxiv.org/html/2512.03242v1#Thmtheorem2 "Theorem 2. ‣ 2.3. Frequency and Severity Decomposition ‣ 2. Mathematical Framework"). Practitioners can apply the improvement formulas to the relevant component model version by swapping ρ\rho with ρf\rho\_{f} or ρs\rho\_{s} and C​VλCV\_{\lambda} with C​VfCV\_{f} or C​VsCV\_{s} respectively. Additionally, the diminishing returns property holds for all model types, confirming that the highest potential impact in Loss Ratio is achieved by improving the most poorly performing model, even at the component level (assuming a similar percentage improvement in correlation is attainable).

### 2.5.  Loss Ratio Error Metric

For practical model evaluation, we introduce a metric that directly quantifies the business impact of model imperfection.

###### Definition 2 (Loss Ratio Error).

The Loss Ratio Error metric is defined as:

|  |  |  |
| --- | --- | --- |
|  | EL​R:=(1+ρ2​C​Vλ−2ρ2+ρ2​C​Vλ−2)2​η−12−1.E\_{LR}:=\left(\frac{1+\rho^{2}CV\_{\lambda}^{-2}}{\rho^{2}+\rho^{2}CV\_{\lambda}^{-2}}\right)^{\frac{2\eta-1}{2}}-1. |  |

In particular, EL​RE\_{LR} represents the fractional increase in loss ratio above the theoretical optimum due to model imperfection. If our target loss ratio is 60%60\% and our model results in a loss ratio of 70%70\%, EL​R=0.700.60−1=0.16E\_{LR}=\frac{0.70}{0.60}-1=0.16. This metric can be computed at the level of pure premium, frequency, or severity, and allows for an apples to apples comparison of model performance across different model types and business lines, provided the appropriate product specific parameters are used.

###### Observation 2 (Loss Ratio Error Properties).

The Loss Ratio Error metric has the following properties:

1. 1.

   EL​R=0E\_{LR}=0 when ρ=1\rho=1 (perfect correlation)
2. 2.

   EL​R>0E\_{LR}>0 when ρ<1\rho<1 (imperfect correlation)
3. 3.

   EL​RE\_{LR} is monotonically decreasing in ρ\rho
4. 4.

   The relationship between loss ratio and error metric is: L​R=1M​(1+EL​R)LR=\frac{1}{M}(1+E\_{LR})

## 3.  Simulation Validation

To establish empirical confidence in our theoretical framework, we conduct Monte Carlo simulations that validate the core mathematical results. Our validation addresses two critical objectives: verifying theoretical accuracy under stated assumptions across realistic parameter ranges, and quantifying performance degradation when key assumptions are moderately violated.

### 3.1.  Methodology

We implement a comprehensive validation strategy using Monte Carlo simulation with two distinct experimental designs. For core formula validation, we employ a systematic grid-based approach covering realistic insurance parameter ranges. The parameter grid spans correlation values ρ∈[0.2,0.3,0.5,0.7,0.8]\rho\in[0.2,0.3,0.5,0.7,0.8] representing poor to excellent model performance, coefficient of variation values C​V∈[1.5,2.0,2.5,3.0,3.5]CV\in[1.5,2.0,2.5,3.0,3.5] covering low-to-high loss variability, and price elasticity values η∈[0.8,1.2,1.6,2.0,2.5]\eta\in[0.8,1.2,1.6,2.0,2.5] from price-insensitive to highly elastic demand. This yields 125 parameter combinations with 5 replications each, totaling 625 simulations.

Each simulation generates synthetic portfolios of 1,000,000 potential customers with true losses λ\lambda drawn from lognormal distributions normalized to unit mean for consistent scaling. Model predictions follow λ^=λ​eε\hat{\lambda}=\lambda e^{\varepsilon} where ε∼N​(0,σ2)\varepsilon\sim N(0,\sigma^{2}) with error variance calibrated to achieve target correlation ρ\rho using the relationship derived in Lemma [2](https://arxiv.org/html/2512.03242v1#Thmlemma2 "Lemma 2. ‣ 2.2. Core Loss Ratio Formula ‣ 2. Mathematical Framework"). Customer demand follows the power-law conversion model c​(p)=(pm​i​n/p)ηc(p)=(p\_{min}/p)^{\eta} scaled so the lowest-priced customer converts with probability 1.0; this is to ensure a sufficiently large sample of converted customers. We employ an automatic resampling strategy (up to 20 attempts) to ensure at least 10,000 converted customers per simulation, providing stable empirical loss ratio estimates across all parameter combinations.

For assumption robustness testing, we systematically violate key framework assumptions using ρ=0.7\rho=0.7, C​V=2.0CV=2.0, and η=1.2\eta=1.2 as baseline parameters. Error distribution violations include t-distributed errors with degrees of freedom from 3 to 30, and skewed normal errors with skewness parameters from 0 to 15. Independence violations introduce systematic correlation between prediction errors and true losses ρε,λ∈(0,0.5)\rho\_{\varepsilon,\lambda}\in(0,0.5). For demand model violations, we implement a realistic testing approach where conversion probabilities are generated from alternative ”true” demand curves (exponential, logistic, linear), then power-law parameters η\eta are fit to these observed probabilities as practitioners would do with market data. To quantify degradation patterns, we conduct 10 replications per violation parameter using portfolios of 200,000 to 500,000 policies, enabling calculation of 95% confidence intervals for framework performance across assumption violation severity.

### 3.2.  Results

The systematic grid validation demonstrates excellent framework performance under stated assumptions. Simulation sizes range from 40,000 to 200,000 converted customers per simulation. Overall accuracy yields a median absolute percentage error of 17.59% (mean 30.18%). Performance varies systematically with parameter ranges: medium-to-high correlation models (ρ≥0.5\rho\geq 0.5) achieve strong validation with errors typically below 15%, while predictable accuracy decline occurs for extreme parameter combinations reflecting theoretical framework limitations rather than implementation issues.

Assumption robustness testing reveals hierarchical sensitivity patterns across violation types (Table [1](https://arxiv.org/html/2512.03242v1#S3.T1 "Table 1 ‣ 3.2. Results ‣ 3. Simulation Validation")). Figure [1](https://arxiv.org/html/2512.03242v1#S3.F1 "Figure 1 ‣ 3.2. Results ‣ 3. Simulation Validation") visualizes these patterns with 95% confidence intervals from 10 replications per parameter: (A) heavy-tailed errors show rapid degradation as kurtosis increases; (B) skewed errors exhibit moderate degradation; and (C) error-loss correlation violations demonstrate the critical importance of the independence assumption.

Figure 1: Framework robustness degradation under systematic assumption violations

![Refer to caption](degradation_analysis_figure.png)

The demand model results provide valuable practical insights. Linear demand shows excellent compatibility with the power-law framework when practitioners fit elasticity parameters to observed conversion data. Logistic demand shows moderate incompatibility, while exponential demand represents a substantial mismatch with power-law assumptions. This highlights the importance of validating that the true demand curve can be sufficiently approximated by a power-law model. Deviations from this assumption may significantly impact the accuracy of the framework.

Table 1: Summary of framework robustness under assumption violations

|  |  |  |
| --- | --- | --- |
| Robustness | Assumption Violation | MAPE (%) |
| Excellent | Baseline control (normal errors) | ∼\sim2–3 |
| Linear demand | ∼\sim5–6 |
| Heavy-tailed errors (df >> 20) | ∼\sim4–6 |
| Good | Heavy-tailed errors (df 10–15) | ∼\sim8–18 |
| Skewed error distributions | <<15 |
| Poor | Logistic demand | ∼\sim40–45 |
| Catastrophic | Exponential demand | ∼\sim50–60 |
| Error-loss correlation >> 0.1 | 75+ |
| Heavy-tailed errors (df << 5) | 100+ |

### 3.3.  Simulation Conclusions

Our simulations support three key findings regarding framework reliability and practical utility. First, the theoretical framework provides reliable predictions under stated assumptions, with mean absolute percentage error below 5% across realistic insurance parameter ranges. The grid-based approach confirms practical utility for quantifying business impact of model improvements, with graceful degradation under extreme parameter combinations.

Second, the framework demonstrates selective robustness to assumption violations, with clear hierarchical sensitivity patterns. The independence assumption (ε⟂λ\varepsilon\perp\lambda) emerges as absolutely critical—any violation fundamentally breaks the framework. Error distribution assumptions show moderate flexibility, tolerating skewness and moderate heavy tails but failing catastrophically under extreme heavy tails. Demand model assumptions exhibit surprising robustness to linear demand but poor tolerance for exponential demand structures.

Third, the realistic parameter fitting approach for demand model violations provides actionable guidance for practitioners. The fit elasticity parameters reveal how well alternative demand structures can be approximated by power-law models, with linear demand showing excellent compatibility and exponential demand proving incompatible. These findings enable practitioners to assess assumption validity in their specific contexts and understand the quantitative consequences of assumption violations.

## 4.  Conclusion

This work establishes an analytical framework connecting model performance metrics to business outcomes in insurance pricing. By deriving a closed-form relationship between model correlation and expected loss ratio, we address a fundamental gap that has long frustrated practitioners seeking to quantify the business value of model improvements. The framework transforms model validation from a purely statistical exercise into a direct business impact assessment, enabling data-driven decisions about model investment priorities.

The theoretical contributions are threefold. First, under specified assumptions, we prove that expected loss ratio depends on model correlation, demand elasticity, and loss distribution characteristics through a precise mathematical relationship. Second, we establish that model improvements exhibit diminishing marginal returns, providing analytical support for the widespread actuarial intuition to prioritize improvements in poorly performing models. Third, we develop practical tools including the Loss Ratio Error metric that quantify business impact at the frequency, severity, or pure premium level.

We examined the framework’s reliability through comprehensive Monte Carlo validation using grid-based testing across 125 parameter combinations and systematic assumption violation analysis. The framework demonstrated reliable predictions under stated assumptions and showed hierarchical robustness patterns under violations, from excellent resilience to linear demand and moderate heavy tails to catastrophic failure under independence violations.

Implementing this framework in practice requires estimation of three key parameters. Model correlation ρ\rho can be computed directly from validation data using standard techniques. The coefficient of variation C​VλCV\_{\lambda} follows from historical loss distributions and is readily available to most insurers. However, demand elasticity η\eta presents the greatest implementation challenge, as it must be estimated on a per-product, per-company basis through pricing experiments, market research, or econometric analysis of historical pricing and conversion data. Regulatory constraints on rate changes vary significantly by jurisdiction; while some markets restrict price experimentation, others permit A/B testing of prices, as practiced by European insurers. Where direct experimentation is limited, insurers may supplement elasticity estimation with industry benchmarks and economic modeling.

For practical implementation, we recommend a historical calibration approach that leverages existing business data. Given observed loss ratios, model correlations, and pricing margins from previous model generations for a specific product line, practitioners can invert the core formula to solve for the implied elasticity parameter η\eta. This reverse estimation should be performed using multiple historical model deployments to establish both point estimates and confidence bounds for η\eta.

Once calibrated for a product line, the framework enables prospective evaluation of model improvements. Practitioners can estimate the expected loss ratio impact of proposed modeling changes by plugging target correlation improvements into the core formula, using the historically-calibrated elasticity parameter. This transforms subjective model investment decisions into quantitative cost-benefit analysis, enabling data-driven prioritization of modeling resources across product lines and improvement opportunities once key parameters are calibrated.

Several limitations constrain the framework’s applicability. The derivation assumes power-law demand models and log-normal prediction errors, though our simulations demonstrate robustness to moderate violations of these assumptions. The framework also treats pricing as a simple cost-plus-margin exercise, ignoring competitive constraints, regulatory requirements, and sophisticated pricing strategies common in practice. Additionally, the static nature of our analysis does not capture dynamic effects such as competitive response, customer learning, or temporal changes in market conditions. Practitioners should validate core assumptions for their specific applications and monitor for assumption violations over time.

The framework opens several promising research directions. Empirical validation across different insurance lines and markets would establish the practical parameter ranges and identify systematic patterns in elasticity estimates. Extensions to multi-line portfolios could capture cross-subsidization effects and portfolio-level optimization considerations. Incorporating competitive dynamics and regulatory constraints would enhance practical relevance, while developing more sophisticated demand models could improve accuracy in markets where power-law assumptions fail. Additionally, the frequency-severity decomposition could be refined to account for dependency structures between frequency and severity predictions, and the framework could be extended to incorporate other business metrics beyond loss ratio, such as customer lifetime value or market share effects. From an operational perspective, direct integration into model assessment pipelines and business planning processes represents a natural next step, enabling automated translation of model validation metrics into loss ratio forecasts during both model development and financial planning cycles.

The gap between model validation and business quantification has persisted because it requires bridging statistical modeling, economic theory, and business strategy. While challenges remain in practical implementation, this framework provides the first analytical foundation for connecting model performance to business outcomes, moving the conversation from qualitative intuition to quantitative analysis. For an industry built on mathematical precision in risk assessment, the ability to apply similar rigor to model investment decisions represents a natural and necessary evolution.

## Acknowledgements

The author would like to thank Shane Barnes and DJ Falkson for generously sharing their time and thoughtful review, and acknowledges the support of colleagues at Lemonade Insurance.