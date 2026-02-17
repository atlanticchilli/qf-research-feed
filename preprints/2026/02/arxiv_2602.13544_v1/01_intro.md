---
authors:
- Min Dai
- Yuchao Dong
- Yanwei Jia
- Xun Yu Zhou
doc_id: arxiv:2602.13544v1
family_id: arxiv:2602.13544
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2602.13544v1
url_html: https://arxiv.org/html/2602.13544v1
venue: arXiv q-fin
version: 1
year: 2026
---

\OneAndAHalfSpacedXI\TheoremsNumberedThrough\ECRepeatTheorems\EquationsNumberedThrough\MANUSCRIPTNO

MS-0000-0000.00

\RUNAUTHOR

Dai et al.

\RUNTITLE

Merton’s Problem with Recursive Perturbed Utility

\TITLE

Merton’s Problem with Recursive Perturbed Utility

\ARTICLEAUTHORS\AUTHOR

Min Dai
\AFFDepartment of Applied Mathematics and School of Accounting and Finance, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong. \EMAILmindai@polyu.edu.hk \AUTHORYuchao Dong
\AFFKey Laboratory of Intelligent Computing and Applications (Tongji University), Ministry of Education and School of Mathematical Sciences, Tongji University, Shanghai 200092, China. \EMAILycdong@tongji.edu.cn
\AUTHORYanwei Jia
\AFFDepartment of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Shatin, New Territories, Hong Kong. \EMAILyanweijia@cuhk.edu.hk
\AUTHORXun Yu Zhou
\AFFDepartment of Industrial Engineering and Operations Research & Data Science Institute, Columbia University, New York, NY 10027, USA. \EMAILxz2574@columbia.edu

\ABSTRACT

The classical Merton investment problem predicts deterministic, state-dependent portfolio rules; however, laboratory and field evidence suggests that individuals often prefer randomized decisions leading to stochastic and noisy choices. Fudenberg et al. ([2015](https://arxiv.org/html/2602.13544v1#bib.bib20)) develop the additive perturbed utility theory to explain the preference for randomization in the static setting, which, however, becomes ill-posed or intractable in the dynamic setting.
We introduce the recursive perturbed utility (RPU), a special stochastic differential utility that incorporates an entropy-based preference for randomization into a recursive aggregator. RPU endogenizes the intertemporal trade-off between utilities from randomization and bequest via a discounting term dependent on past accumulated randomization, thereby avoiding excessive randomization and yielding a well-posed problem. In a general Markovian incomplete market with CRRA preferences, we prove that the RPU-optimal portfolio policy (in terms of the risk exposure ratio) is Gaussian and can be expressed in closed form, independent of wealth. Its variance is inversely proportional to risk aversion and stock volatility, while its mean is based on the solution to a partial differential equation. Moreover, the mean is the sum of a myopic term and an intertemporal hedging term (against market incompleteness) that intertwines with policy randomization.
Finally, we carry out an asymptotic expansion in terms of the perturbed utility weight to show that the optimal mean policy deviates from the classical Merton policy at first order, while the associated relative wealth loss is of a higher order, quantifying the financial cost of the preference for randomization.

\KEYWORDS

Merton’s problem; preference for randomization; recursive perturbed utility; biased stochastic policy

## 1 Introduction

Merton’s continuous-time investment problem (Merton, [1969](https://arxiv.org/html/2602.13544v1#bib.bib40)) is a cornerstone of intertemporal portfolio choice. It provides a tractable framework for characterizing optimal investment decisions and has been extended to a variety of preference specifications with rich economic implications. A common conclusion arising from these models is that a rational, risk-averse investor follows a deterministic function of time and state, also called a portfolio policy or rule.111Here “state” includes observable variables including portfolio worth, known factors and stock prices. Thus, one can predict investor behavior deterministically based on these models. However, experimental and empirical evidence suggests that people sometimes favor or even crave “randomized” and noisy choices, with examples ranging from sushi omakase222“Omakase”, meaning in Japanese “to entrust”, originally refers to a set sushi course whose contents are completely determined by the chef based on his/her observation of an individual customer. Therefore, the surprise from the revelation of each sushi dish is a major fun part of the dining experience. Nowadays, omakase meals popular in many countries are often pre-announced set menus, thereby losing their original feature (and excitement) of randomization. and “blind boxes”333Also called “mystery boxes”, blind boxes are curated, randomized packages sold for a fixed price, containing undisclosed items ranging from electronics and collectibles to clothing and snack boxes. The ultra-popular Labubu figures produced by Pop Mart are such an example. to portfolio allocations. In other words, the same individual does not necessarily repeat the same choice when faced with the same problem. This leads to stochastic choice and randomized policies. Fudenberg et al. ([2015](https://arxiv.org/html/2602.13544v1#bib.bib20)) propose and develop the *additive perturbed utility* (APU) for *static* choice problems, which is expected utility plus a perturbation over choice probabilities. This perturbation captures an inherent desire to randomize, consistent also with the behavioral literature (Hey and Carbone, [1995](https://arxiv.org/html/2602.13544v1#bib.bib25); Dwenger et al., [2018](https://arxiv.org/html/2602.13544v1#bib.bib16); Miao and Zhong, [2018](https://arxiv.org/html/2602.13544v1#bib.bib41); Permana, [2020](https://arxiv.org/html/2602.13544v1#bib.bib42); Agranov and Ortoleva, [2017](https://arxiv.org/html/2602.13544v1#bib.bib1), [2025](https://arxiv.org/html/2602.13544v1#bib.bib2)).
The most widely used perturbation is the *entropy* function, which produces the logit/Luce stochastic choice when the choice set is finite (Luce et al., [1959](https://arxiv.org/html/2602.13544v1#bib.bib35); Anderson et al., [1992](https://arxiv.org/html/2602.13544v1#bib.bib3)).444For finite choice sets, APU connects to discrete-choice and random-utility models (McFadden, [1974](https://arxiv.org/html/2602.13544v1#bib.bib38), [2001](https://arxiv.org/html/2602.13544v1#bib.bib39); Anderson et al., [1992](https://arxiv.org/html/2602.13544v1#bib.bib3); Berry, [1994](https://arxiv.org/html/2602.13544v1#bib.bib7); Machina, [1985](https://arxiv.org/html/2602.13544v1#bib.bib36); Mattsson and Weibull, [2002](https://arxiv.org/html/2602.13544v1#bib.bib37); Feng et al., [2017](https://arxiv.org/html/2602.13544v1#bib.bib19)) and has been extended to multi-period settings (Hotz and Miller, [1993](https://arxiv.org/html/2602.13544v1#bib.bib26); Hotz et al., [1994](https://arxiv.org/html/2602.13544v1#bib.bib27)).

In this paper, we
extend APU to the dynamic setting inherent for Merton’s problem. Now that the control is continuum-valued, this extension from static to dynamic is by no means straightforward. Indeed, randomizing portfolios does not generate direct monetary payoffs; rather, the perturbation term is a non-monetary component of the preference in addition to the bequest utility (of the terminal wealth). Because portfolio choices are made continuously over time, the agent accrues a *flow* of utility from randomization, analogous to the flow utility from consumption in the classical Merton consumption-investment problem.555In this paper we do not consider consumption so as to stay focused on the randomization utility flow. 
With this in mind, our first result shows that the dynamic counterpart of APU in the Merton setting is ill-posed when risk aversion is not sufficiently strong: the agent can drive the payoff to infinity by increasing the choice variance without bound. Two forces, specific to the dynamic setting, are behind this pathology. First, with a continuous control, the entropy-based randomization can deliver unbounded perturbation payoffs, unlike the bounded entropy in finite choice sets. Second, the intertemporal trade-off between randomization and investment fundamentally differs from the familiar trade-off between consumption and investment. Consumption sacrifices future wealth growth; randomization, by contrast, leaves the *expected* growth rate unchanged while increasing volatility. Risk aversion, if too low, is therefore insufficient to deter excessive randomization. Moreover, even when risk aversion is sufficiently large to restore well-posedness, the additive model fails to yield tractable solutions—even in the Black-Scholes setting with constant-relative-risk-aversion (CRRA) preferences—making it difficult to characterize and analyze optimal policies.

These failures highlight more nuanced intertemporal interactions between utilities from randomization and from investment than the APU can capture. We therefore propose the *recursive perturbed utility* (RPU), inspired by recursive utility developed by Epstein and Zin ([1989](https://arxiv.org/html/2602.13544v1#bib.bib18)) in discrete time and by Duffie and Epstein ([1992](https://arxiv.org/html/2602.13544v1#bib.bib15)) in continuous time. While recursive utility was introduced to separate risk aversion from the elasticity of intertemporal substitution in consumption, our goal is to *endogenize* the effect of the entropy perturbation. The form of RPU resembles the Uzawa utility (Uzawa, [1968](https://arxiv.org/html/2602.13544v1#bib.bib44)), which captures habit formation through an endogenous discount rate affected by past consumption.666See Bergman ([1985](https://arxiv.org/html/2602.13544v1#bib.bib6)) for economic and financial implications of Uzawa preferences.
In our setting, past randomization influences the agent’s current preference in the form of time preference: the perturbation induces *endogenous discounting* that dampens the flow of utility from further randomization as the latter accumulates over time. In other words, RPU gives rise to a history-dependent time preference
on randomization, such that the more or longer the investor has randomized in the past, the less weight
she places on current randomization.

We study Merton’s problem in an incomplete Markovian stock market with exogenous stochastic factors (e.g., Wachter [2002](https://arxiv.org/html/2602.13544v1#bib.bib45); Liu [2007](https://arxiv.org/html/2602.13544v1#bib.bib34); Chacko and Viceira [2005](https://arxiv.org/html/2602.13544v1#bib.bib9)) and CRRA utilities within the RPU framework featuring entropy perturbations. We prove that the optimal portfolio (in terms of the risk exposure ratio) policy must follow a Gaussian distribution that is dependent on the stochastic factors but independent of wealth. The variance of this policy admits a closed-form expression, which is inversely proportional to both relative risk aversion and the instantaneous variance of stock returns. Thus, higher risk aversion or higher market volatility reduces choice noise. Meanwhile, the optimal mean is dependent only on time and factor, characterized by a partial differential equation (PDE). In general, the mean decomposes into a myopic term (that depends on risk aversion and the stock’s instantaneous return-risk trade-off but is *independent* of the randomization) and an intertemporal hedging term (that captures the hedging need due to market incompleteness and its correlation with the randomization). In complete markets or when the stock and factor move independently, the hedging term vanishes and the mean optimal policy is purely myopic, coinciding with the classical Merton solution. A notable special case is log utility (unit relative risk aversion), in which intertemporal hedging is absent, and RPU collapses to APU yielding a mean optimal policy identical to the Merton benchmark.777See Dai et al. ([2023](https://arxiv.org/html/2602.13544v1#bib.bib10)) for a related result in the context of entropy-regularized reinforcement learning with log utility.

In general, however, RPU biases the optimal mean relative to the classical Merton benchmark (without randomization). We quantify this effect via an asymptotic expansion in the perturbation weight (called the “*temperature*”). The deviation of the optimal mean from the classical Merton policy is first order in temperature, while the associated relative wealth loss from adopting the RPU-optimal policy (versus the classical benchmark) is of higher order. This in turn provides a transparent measure of the financial cost associated with the preference for randomized choices.

It is worth noting that the perturbed utility with entropy function has been widely used in the reinforcement learning (RL) literature, albeit with a different name “entropy regularization”, as seen in works such as Ziebart et al. ([2008](https://arxiv.org/html/2602.13544v1#bib.bib50)); Haarnoja et al. ([2018](https://arxiv.org/html/2602.13544v1#bib.bib22)); Zhao et al. ([2019](https://arxiv.org/html/2602.13544v1#bib.bib49)) for the discrete-time setting and Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)) for the continuous-time one, among many others. The resulting optimal policies take the form of a Gibbs measure. However, the purposes of introducing randomized policies and entropy regularization for RL are conceptually and fundamentally different: the aim is to design algorithms to solve decision-making problems in a data-driven way, often without knowledge of the environment’s probabilistic structure. The entropy term is added to the reward function as an explicit incentive to encourage exploration by randomizing choices, with the ultimate goal to balance exploration (learning) and exploitation (optimization).

By contrast, our paper follows Fudenberg et al. ([2015](https://arxiv.org/html/2602.13544v1#bib.bib20)) and employs entropy to capture humans’ intrinsic preference for randomization.888Fudenberg et al. ([2015](https://arxiv.org/html/2602.13544v1#bib.bib20)) discuss also APU as a way to tackle payoff uncertainty; see Section 5 therein and the related references cited. However, no model parameter unavailability is involved. We study and characterize optimal behaviors under this perturbed utility paradigm by assuming the investor is rational and possesses full knowledge of the market model. Here, stochastic choices do not arise from the need to explore, but rather from a genuine preference for randomization.999A companion paper (Dai et al., [2025a](https://arxiv.org/html/2602.13544v1#bib.bib11)) studies the Merton problem from the RL and computational perspective. It introduces an auxiliary problem with a class of Gaussian policies solvable by RL algorithms and proves that its optimal policy can be used to recover the optimal (deterministic) policy to the original Merton problem. Additionally, several other works take this exploratory framework to devise RL algorithms applied to portfolio selection or stock execution problems, such as Wang and Zhou ([2020](https://arxiv.org/html/2602.13544v1#bib.bib48)); Wang et al. ([2023](https://arxiv.org/html/2602.13544v1#bib.bib46)); Huang et al. ([2025](https://arxiv.org/html/2602.13544v1#bib.bib30)). The purpose of this strand of literature is fundamentally different from that of the present paper.

Different motivations aside, the mathematical framework for incorporating stochastic policies and entropy functions in continuous time is premised upon the same notion of relaxed controls introduced by Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)). Numerous subsequent works have laid the mathematical foundations for randomized controls in continuous time. For example, Bender and Thuan ([2026](https://arxiv.org/html/2602.13544v1#bib.bib5)) and Jia et al. ([2026](https://arxiv.org/html/2602.13544v1#bib.bib32)) confirm that state processes obtained by randomizing decisions at discrete time grids converge weakly to the so-called exploratory state process in Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)) as the sampling frequency approaches infinity. Tang et al. ([2022](https://arxiv.org/html/2602.13544v1#bib.bib43)) establish the well-posedness of the Hamilton-Jacobi-Bellman equation associated with the exploratory formulation in Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)) by a viscosity solution approach. The framework has also been extended to mean-field games (Guo et al., [2022](https://arxiv.org/html/2602.13544v1#bib.bib21)), optimal stopping problems (Dianetti et al., [2025](https://arxiv.org/html/2602.13544v1#bib.bib14); Dai et al., [2025b](https://arxiv.org/html/2602.13544v1#bib.bib13)), risk-sensitive problems (Jia, [2024](https://arxiv.org/html/2602.13544v1#bib.bib31)), and time-inconsistent problems (Dai et al., [2023](https://arxiv.org/html/2602.13544v1#bib.bib10)). All these papers adopt the additive form, directly adding the entropy function as a running reward.
Other forms of regularization or perturbation functions in continuous time have been studied by Han et al. ([2023](https://arxiv.org/html/2602.13544v1#bib.bib23)), but they remain restricted to the additive form.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2602.13544v1#S2 "2 Problem Formulation") presents the market setup, formulates Merton’s problem and motivates the recursive additive entropy utility. Section [3](https://arxiv.org/html/2602.13544v1#S3 "3 Theoretical Analysis") proves the optimality of Gaussian randomized policy and discusses conditions under which the policy is biased or unbiased. The section further provides an asymptotic analysis of the impact of the primary temperature parameter. Finally, Section [4](https://arxiv.org/html/2602.13544v1#S4 "4 Conclusions") concludes. Additional results and discussions are provided in the appendix.

## 2 Problem Formulation

### 2.1 Market Environment and Investment Objective

Consider a financial market with two available investment assets: a risk-free bond offering a constant interest rate rr and a risky stock (or market index). The stock price process StS\_{t} evolves according to the stochastic differential equation (SDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=μ​(t,Xt)​d​t+σ​(t,Xt)​d​Bt,S0=s0,\frac{\mathrm{d}S\_{t}}{S\_{t}}=\mu(t,X\_{t})\mathrm{d}t+\sigma(t,X\_{t})\mathrm{d}B\_{t},\ S\_{0}=s\_{0}, |  | (1) |

where BB denotes a one-dimensional Brownian motion. The instantaneous return rate μt≡μ​(t,Xt)\mu\_{t}\equiv\mu(t,X\_{t}) and volatility σt≡σ​(t,Xt)\sigma\_{t}\equiv\sigma(t,X\_{t}) both depend on an observable stochastic market factor process XtX\_{t}. The dynamics of XtX\_{t} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=m​(t,Xt)​d​t+ν​(t,Xt)​[ρ​d​Bt+1−ρ2​d​B~t],X0=x0,\mathrm{d}X\_{t}=m(t,X\_{t})\mathrm{d}t+\nu(t,X\_{t})[\rho\mathrm{d}B\_{t}+\sqrt{1-\rho^{2}}\mathrm{d}\tilde{B}\_{t}],\ X\_{0}=x\_{0}, |  | (2) |

where B~\tilde{B} is an independent one-dimensional Brownian motion, and ρ∈(−1,1)\rho\in(-1,1) is a constant representing the correlation between the stock return and the market factor changes. As a result, the market is generally incomplete. We focus on the Markovian setting, where the functions μ​(⋅,⋅)\mu(\cdot,\cdot), σ​(⋅,⋅)\sigma(\cdot,\cdot), m​(⋅,⋅)m(\cdot,\cdot), and ν​(⋅,⋅)\nu(\cdot,\cdot) are deterministic and continuous in both tt and xx such that the SDEs ([1](https://arxiv.org/html/2602.13544v1#S2.E1 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation"))-([2](https://arxiv.org/html/2602.13544v1#S2.E2 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")) admit a unique weak solution. This market environment is sufficiently general to encompass many widely studied incomplete market models as special cases—for example, the Gaussian mean return model and the stochastic volatility model examined in Wachter ([2002](https://arxiv.org/html/2602.13544v1#bib.bib45)), Liu ([2007](https://arxiv.org/html/2602.13544v1#bib.bib34)), Chacko and Viceira ([2005](https://arxiv.org/html/2602.13544v1#bib.bib9)); Dai et al. ([2021](https://arxiv.org/html/2602.13544v1#bib.bib12)), among others.101010We assume there is only one stock and one factor for notational simplicity. There is no essential difficulty in extending to the multi-stock/factor case.

The investor’s actions are represented as a scalar-valued non-anticipative process a={at}t∈[0,T)a=\{a\_{t}\}\_{t\in[0,T)}, where ata\_{t} denotes the fraction of total wealth allocated to the stock at time tt. The associated self-financing wealth process WaW^{a} evolves according to the SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​WtaWta=[r+(μ​(t,Xt)−r)​at]​d​t+σ​(t,Xt)​at​d​Bt,W0a=w0.\frac{\mathrm{d}W\_{t}^{a}}{W^{a}\_{t}}=[r+(\mu(t,X\_{t})-r)a\_{t}]\mathrm{d}t+\sigma(t,X\_{t})a\_{t}\mathrm{d}B\_{t},\ \ W\_{0}^{a}=w\_{0}. |  | (3) |

It is important to note that the solvency constraint Wta≥0W\_{t}^{a}\geq 0 almost surely for all t∈[0,T]t\in[0,T], is automatically satisfied for any square integrable aa.
The classical Merton investment problem seeks to maximize the expected bequest utility of terminal wealth WTaW\_{T}^{a} by selecting an appropriate strategy aa:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxa⁡𝔼​[U​(WTa)],\max\_{a}\mathbb{E}\left[U(W\_{T}^{a})\right], |  | (4) |

subject to the dynamics ([2](https://arxiv.org/html/2602.13544v1#S2.E2 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation"))-([3](https://arxiv.org/html/2602.13544v1#S2.E3 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")), where U​(⋅)U(\cdot) is the utility function.

In the main text, we focus on the constant relative risk aversion (CRRA) utility, given by

|  |  |  |
| --- | --- | --- |
|  | U​(w)=w1−γ−11−γ,U(w)=\frac{w^{1-\gamma}-1}{1-\gamma}, |  |

where 1≠γ>01\neq\gamma>0 is the relative risk aversion parameter. The additive constant “−11−γ-\frac{1}{1-\gamma}” does not affect the preference reflected; we include it here for two reasons. First, the form converges to the log utility as γ→1\gamma\rightarrow 1. Second, including the constant will properly reflect the magnitude of the bequest utility when we combine it with the preference for randomization in Section [2.3](https://arxiv.org/html/2602.13544v1#S2.SS3 "2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation"). The case for the constant absolute risk aversion (CARA) utility function will be discussed in Appendix [6](https://arxiv.org/html/2602.13544v1#S6 "6 CARA Utility").

### 2.2 Preference for Randomization

As it stands, the classical Merton problem leads to a *deterministic* optimal (feedback) policy. The agent has no appetite for randomization because it would increase the uncertainty in wealth, which is unfavored by risk aversion. Therefore, to capture the preference for randomization, we need to add reward for randomization explicitly into the objective function. Moreover, with randomized choices, the resulting law of motion of the wealth process described by ([3](https://arxiv.org/html/2602.13544v1#S2.E3 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")) will also be fundamentally altered because ata\_{t} will now be randomly sampled from a distribution that is independent of the market randomness (Bt,B~tB\_{t},\tilde{B}\_{t}). The resulting mathematical formulation is put forward and coined as the “exploratory formulation” for general stochastic control problems by Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)) in the reinforcement learning (RL) context. We now adapt that formulation to the Merton problem.

The central idea of this formulation is to describe the portfolio rules using a probability distribution for randomization. Specifically, suppose the investor selects her action (portfolio) at time tt by sampling from a probability distribution 𝝅t\boldsymbol{\pi}\_{t}, where
{𝝅t}t∈[0,T]=:𝝅\{\boldsymbol{\pi}\_{t}\}\_{t\in[0,T]}=:\boldsymbol{\pi} is a distribution-valued process referred to as a randomized control. Under such a control, the exploratory or randomized dynamics of the wealth process are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Wt𝝅Wt𝝅=[r+(μ​(t,Xt)−r)​Mean⁡(𝝅t)]​d​t+σ​(t,Xt)​[Mean⁡(𝝅t)​d​Bt+Var⁡(𝝅t)​d​B¯t],W0𝝅=w0,\frac{\mathrm{d}W^{\boldsymbol{\pi}}\_{t}}{W^{\boldsymbol{\pi}}\_{t}}=\left[r+(\mu(t,X\_{t})-r)\operatorname{Mean}(\boldsymbol{\pi}\_{t})\right]\mathrm{d}t+\sigma(t,X\_{t})\left[\operatorname{Mean}(\boldsymbol{\pi}\_{t})\mathrm{d}B\_{t}+\sqrt{\operatorname{Var}(\boldsymbol{\pi}\_{t})}\mathrm{d}\bar{B}\_{t}\right],\ W^{\boldsymbol{\pi}}\_{0}=w\_{0}, |  | (5) |

where B¯\bar{B} is another Brownian motion, independent of both BB and B~\tilde{B}, representing the additional randomness introduced into the wealth process due to randomization. Equation ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) shows that randomization effectively raises the volatility of the resulting wealth process, and Mean⁡(𝝅t)\operatorname{Mean}(\boldsymbol{\pi}\_{t}) plays a similar role as ata\_{t} in the classical dynamics ([3](https://arxiv.org/html/2602.13544v1#S2.E3 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")). Intuitively, W𝝅W^{\boldsymbol{\pi}} can be viewed as the “average” of infinitely many wealth processes generated by portfolio processes repeatedly sampled from the same randomized control 𝝅\boldsymbol{\pi}.
Another interpretation of W𝝅W^{\boldsymbol{\pi}} is the weak limit of wealth processes under piecewise constant portfolios where the portfolios are sampled from 𝝅\boldsymbol{\pi} only at discrete time points, as the mesh size of the sampling grid tends to zero; see Bender and Thuan ([2026](https://arxiv.org/html/2602.13544v1#bib.bib5)) and Jia et al. ([2026](https://arxiv.org/html/2602.13544v1#bib.bib32)).
The derivation of ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) is analogous to that in Dai et al. ([2023](https://arxiv.org/html/2602.13544v1#bib.bib10)) and Dai et al. ([2025a](https://arxiv.org/html/2602.13544v1#bib.bib11)); see a detailed explanation in Appendix A of Dai et al. ([2025a](https://arxiv.org/html/2602.13544v1#bib.bib11)) and Jia et al. ([2026](https://arxiv.org/html/2602.13544v1#bib.bib32)) for how ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) can be viewed as the limit of sampling randomized choice at a high frequency.

Second, to describe the preference for randomization, we adopt the entropy function to measure the level of randomness associated with a distribution 𝝅\boldsymbol{\pi}, denoted as ℋ​(𝝅)=−∫ℝ𝝅​(a)​log⁡𝝅​(a)​da\mathcal{H}(\boldsymbol{\pi})=-\int\_{\mathbb{R}}\boldsymbol{\pi}(a)\log\boldsymbol{\pi}(a)\mathrm{d}a (known as the differential entropy).111111Here we implicitly assume 𝝅\boldsymbol{\pi} to be absolutely continuous with respect to the Lebesgue measure so that the entropy can be properly defined. For Merton’s problem, the simplest way seems to be just adding running APU from randomization to the bequest utility, leading to the maximization of the following objective:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0Tλ​ℋ​(𝝅s)​ds+U​(WT𝝅)],\mathbb{E}\left[\int\_{0}^{T}\lambda\mathcal{H}(\boldsymbol{\pi}\_{s})\mathrm{d}s+U(W\_{T}^{\boldsymbol{\pi}})\right], |  | (6) |

where λ>0\lambda>0 is the temperature parameter representing the importance of randomization relative to the bequest utility, and {λ​ℋ​(𝝅t)}t∈[0,T]\{\lambda\mathcal{H}(\boldsymbol{\pi}\_{t})\}\_{t\in[0,T]} is the flow of utility from randomization. The form ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) is a direct adaptation of the APU arising from the static setting of Fudenberg et al. ([2015](https://arxiv.org/html/2602.13544v1#bib.bib20)); it has also been chosen in the RL context by many algorithms as an incentive for exploration (e.g., Ziebart et al. [2008](https://arxiv.org/html/2602.13544v1#bib.bib50); Haarnoja et al. [2018](https://arxiv.org/html/2602.13544v1#bib.bib22) among many others).

As it turns out, however, it is difficult to analyze the randomized Merton problem under the objective ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")), where a closed-form solution is unavailable even for the Black-Scholes market with the CRRA utility (see Appendix [5.1](https://arxiv.org/html/2602.13544v1#S5.SS1 "5.1 Constant Temperature ‣ 5 Different Temperature Schemes") for explanations). Even worse, Proposition [2.1](https://arxiv.org/html/2602.13544v1#S2.Thmtheorem1 "Proposition 2.1 ‣ 2.2 Preference for Randomization ‣ 2 Problem Formulation") below shows that the problem with the objective ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) is ill-posed if risk aversion is not sufficiently strong.

###### Proposition 2.1

If γ∈(0,1)\gamma\in(0,1), then the problem with the objective functional ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")), subject to the wealth dynamics ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")), is ill-posed with an infinite optimal value.

###### Proof 2.2

Proof.
When γ∈(0,1)\gamma\in(0,1), U​(w)>−11−γU(w)>-\frac{1}{1-\gamma} for any w>0w>0. We consider a simple policy 𝛑t=𝒩​(0,v)\boldsymbol{\pi}\_{t}=\mathcal{N}(0,v), where v>0v>0 is a constant. Then the objective function in ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) is greater than λ​T2​log⁡(2​π​e​v)−11−γ\frac{\lambda T}{2}\log(2\pi ev)-\frac{1}{1-\gamma}. Letting v→∞v\to\infty causes the objective value to diverge to infinity.
∎

The intuition of Proposition [2.1](https://arxiv.org/html/2602.13544v1#S2.Thmtheorem1 "Proposition 2.1 ‣ 2.2 Preference for Randomization ‣ 2 Problem Formulation") is that when the investor is not sufficiently risk-averse, there is not enough deterrence from over-randomization while the utility from the entropy term can be unbounded. Indeed, the proof of the proposition indicates that the problem becomes ill-posed whenever the bequest utility UU is bounded from below. Hence, a naïve APU is not appropriate in the Merton setting to yield reasonable economic predictions. To remedy this problem, we introduce a different type of perturbed utility for randomization.

### 2.3 Recursive Perturbation Utility

Let a function λ​(⋅,⋅)>0\lambda(\cdot,\cdot)>0 be exogenously given, called a primary temperature function (it will be taken as a constant in Section [3.3](https://arxiv.org/html/2602.13544v1#S3.SS3 "3.3 An Asymptotic Analysis on 𝜆 ‣ 3 Theoretical Analysis")).
Define by J𝝅={Jt𝝅}t∈[0,T]J^{\boldsymbol{\pi}}=\{J^{\boldsymbol{\pi}}\_{t}\}\_{t\in[0,T]} the following recursive (entropy) perturbed utility (RPU) under a given randomized control 𝝅\boldsymbol{\pi}, which is an {ℱt}t∈[0,T]\{\mathcal{F}\_{t}\}\_{t\in[0,T]}-adapted process satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt𝝅=𝔼​[∫tTλ​(s,Xs)​[(1−γ)​Js𝝅+1]​ℋ​(𝝅s)​ds+U​(WT𝝅)|ℱt],J^{\boldsymbol{\pi}}\_{t}=\mathbb{E}\left[\int\_{t}^{T}\lambda(s,X\_{s})[(1-\gamma)J\_{s}^{\boldsymbol{\pi}}+1]\mathcal{H}(\boldsymbol{\pi}\_{s})\mathrm{d}s+U(W\_{T}^{\boldsymbol{\pi}})\Big|\mathcal{F}\_{t}\right], |  | (7) |

where W𝝅W^{\boldsymbol{\pi}} is the wealth process under 𝝅{\boldsymbol{\pi}}, determined by ([2](https://arxiv.org/html/2602.13544v1#S2.E2 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")) and ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")), and {ℱ}⊔∈[′,𝒯]\{\cal F\}\_{t\in[0,T]} is the filtration generated by 𝐁:=(B,B¯,B~)⊤\mathbf{B}:=(B,\bar{B},\tilde{B})^{\top}.

The recursive form ([7](https://arxiv.org/html/2602.13544v1#S2.E7 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")) effectively weighs the entropy utility endogenously: The term λ​(t,Xt)​[(1−γ)​Jt𝝅+1]\lambda(t,X\_{t})\left[(1-\gamma)J\_{t}^{\boldsymbol{\pi}}+1\right] can be viewed as a utility-dependent weight on randomization determined in a recursive way. Notice that when γ=1\gamma=1 (corresponding to the log utility function), the weight on the entropy term becomes independent of the utility, and ([7](https://arxiv.org/html/2602.13544v1#S2.E7 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")) further reduces to ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) when λ​(t,x)≡λ\lambda(t,x)\equiv\lambda, i.e., the APU.

Under some proper assumptions (e.g., in El Karoui et al. [1997](https://arxiv.org/html/2602.13544v1#bib.bib17)), J𝝅J^{\boldsymbol{\pi}}, which is an ℱt{\cal F}\_{t}-adapted process, solves the following backward stochastic differential equation (BSDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Jt𝝅=−λt​ℋ​(𝝅t)​[(1−γ)​Jt𝝅+1]​d​t+𝐙t𝝅⋅d​𝐁t,JT𝝅=U​(WT𝝅),\mathrm{d}J\_{t}^{\boldsymbol{\pi}}=-\lambda\_{t}\mathcal{H}(\boldsymbol{\pi}\_{t})\left[(1-\gamma)J\_{t}^{\boldsymbol{\pi}}+1\right]\mathrm{d}t+\mathbf{Z}^{\boldsymbol{\pi}}\_{t}\cdot\mathrm{d}\mathbf{B}\_{t},\ J\_{T}^{\boldsymbol{\pi}}=U({W\_{T}^{\boldsymbol{\pi}}}), |  | (8) |

where (and henceforth) λt≡λ​(t,Xt)\lambda\_{t}\equiv\lambda(t,X\_{t}) and the notation ⋅\cdot denotes the inner product. As explained in the Introduction, our formulation is motivated by the notion of “recursive utility” in the economics literature (Epstein and Zin, [1989](https://arxiv.org/html/2602.13544v1#bib.bib18); Duffie and Epstein, [1992](https://arxiv.org/html/2602.13544v1#bib.bib15)), with consumption being the counterpart of randomization. In particular, the negative “d​t\mathrm{d}t” term in ([8](https://arxiv.org/html/2602.13544v1#S2.E8 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")), as a function of 𝝅t\boldsymbol{\pi}\_{t} and Jt𝝅J^{\boldsymbol{\pi}}\_{t}, can be written as f​(𝝅,J,λ)=λ​ℋ​(𝝅)−[−λ​(1−γ)​ℋ​(𝝅)]​Jf(\boldsymbol{\pi},J,\lambda)=\lambda\mathcal{H}(\boldsymbol{\pi})-\left[-\lambda(1-\gamma)\mathcal{H}(\boldsymbol{\pi})\right]J. This term is the “aggregator” in the recursive utility jargon, while the term −λ​(1−γ)​ℋ​(𝝅)-\lambda(1-\gamma)\mathcal{H}(\boldsymbol{\pi}) corresponds to the discount rate that depreciates the future utility JJ into today’s value.

We can formalize the above discussion to show a time preference on randomization implied by the definition of J𝝅J^{\boldsymbol{\pi}}, in the same way as the Uzawa utility (Uzawa, [1968](https://arxiv.org/html/2602.13544v1#bib.bib44)) for consumption. Indeed, we explicitly solve ([7](https://arxiv.org/html/2602.13544v1#S2.E7 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt𝝅=𝔼​[∫tTe−∫ts−λτ​(1−γ)​ℋ​(𝝅τ)​d​τ​λs​ℋ​(𝝅s)​ds+e−∫tT−λτ​(1−γ)​ℋ​(𝝅τ)​d​τ​U​(WT𝝅)|ℱt].J\_{t}^{\boldsymbol{\pi}}=\mathbb{E}\left[\int\_{t}^{T}e^{-\int\_{t}^{s}-\lambda\_{\tau}(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{\tau})\mathrm{d}\tau}\lambda\_{s}\mathcal{H}(\boldsymbol{\pi}\_{s})\mathrm{d}s+e^{-\int\_{t}^{T}-\lambda\_{\tau}(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{\tau})\mathrm{d}\tau}U(W\_{T}^{\boldsymbol{\pi}})\Big|\mathcal{F}\_{t}\right]. |  | (9) |

This expression implies that the current weight on randomization depends on past randomization.
Specifically,
the (endogenous) temperature parameter for randomization now (compared to ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation"))) becomes λs​e−∫0s−λτ​(1−γ)​ℋ​(𝝅τ)​d​τ\lambda\_{s}e^{-\int\_{0}^{s}-\lambda\_{\tau}(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{\tau})\mathrm{d}\tau}. In other words, at any time ss, a discount e−∫0s−λτ​(1−γ)​ℋ​(𝝅τ)​d​τe^{-\int\_{0}^{s}-\lambda\_{\tau}(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{\tau})\mathrm{d}\tau} is applied to ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")). Moreover, empirical studies indicate that the typical risk-aversion parameter γ>1\gamma>1 (see, e.g., Kydland and Prescott [1982](https://arxiv.org/html/2602.13544v1#bib.bib33)), rendering −λτ​(1−γ)>0-\lambda\_{\tau}(1-\gamma)>0. This implies that the more the investor has randomized in the past, the less weight she places on current randomization, which is intuitive and sensible. Next, consider a small risk aversion γ∈(0,1)\gamma\in(0,1), where the discounting factor becomes negative, which seems to incentivize larger randomization. However, there is a similar discount applied to the bequest utility. So, as randomization increases, the constant part of the bequest utility “−11−γ-\frac{1}{1-\gamma}”, which now is a negative number, will go even more negative. This introduces a proper trade-off between randomization and bequest utility even when risk aversion is weak, avoiding the ill-posedness that occurs in the APU case.

Technically, the modified objective function ([9](https://arxiv.org/html/2602.13544v1#S2.E9 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")) makes our model mathematically tractable, as will be shown in the subsequent analysis.

Henceforth denote μt≡μ​(t,Xt)\mu\_{t}\equiv\mu(t,X\_{t}) and σt≡σ​(t,Xt)\sigma\_{t}\equiv\sigma(t,X\_{t}). We are now ready to formulate our RPU Merton problem, by first formally introducing the set of admissible controls.

###### Definition 2.3

An ℱt\mathcal{F}\_{t}-adapted, probability-density-valued process 𝛑={𝛑s,0≤s≤T}\boldsymbol{\pi}=\{\boldsymbol{\pi}\_{s},0\leq s\leq T\} is called an (open-loop) admissible control, if

1. (i)

   for each 0≤s≤T0\leq s\leq T, 𝝅s∈𝒫​(ℝ)\boldsymbol{\pi}\_{s}\in\mathcal{P}(\mathbb{R}) a.s., where 𝒫​(ℝ)\mathcal{P}(\mathbb{R}) is the set of all probability densities on real numbers;
2. (ii)

   𝔼[∫0T|σs|2(Mean(𝝅s)2+Var(𝝅s))ds]+𝔼[∫0T|μsMean(𝝅s)|ds]<∞\mathbb{E}\left[\int\_{0}^{T}|\sigma\_{s}|^{2}(\operatorname{Mean}(\boldsymbol{\pi}\_{s})^{2}+\operatorname{Var}(\boldsymbol{\pi}\_{s}))\mathrm{d}s\right]+\mathbb{E}\left[\int\_{0}^{T}|\mu\_{s}\operatorname{Mean}(\boldsymbol{\pi}\_{s})|\mathrm{d}s\right]<\infty;
3. (iii)

   𝔼​[e∫0T2​λs​|1−γ|​|ℋ​(𝝅s)|​𝑑s]+𝔼​[|U​(WT𝝅)|2]<∞,\mathbb{E}\left[e^{\int\_{0}^{T}2\lambda\_{s}|1-\gamma||\mathcal{H}(\boldsymbol{\pi}\_{s})|ds}\right]+\mathbb{E}\left[|U(W^{\boldsymbol{\pi}}\_{T})|^{2}\right]<\infty,
   where {Xs}s∈[0,T]\{X\_{s}\}\_{s\in[0,T]} and {Ws𝝅}s∈[0,T]\{W^{\boldsymbol{\pi}}\_{s}\}\_{s\in[0,T]} satisfy ([2](https://arxiv.org/html/2602.13544v1#S2.E2 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")) and ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")), respectively.

Given an admissible control 𝝅\boldsymbol{\pi} and an initial state pair (w0,x0)(w\_{0},x\_{0}), we define the recursive utility Jt𝝅J\_{t}^{\boldsymbol{\pi}} through ([7](https://arxiv.org/html/2602.13544v1#S2.E7 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")),
where {Xt}t∈[0,T]\{X\_{t}\}\_{t\in[0,T]} and {Wt𝝅}t∈[0,T]\{W\_{t}^{\boldsymbol{\pi}}\}\_{t\in[0,T]} solve ([2](https://arxiv.org/html/2602.13544v1#S2.E2 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")) and ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")), respectively. A technical question with the above definition is whether the entropy term in ([7](https://arxiv.org/html/2602.13544v1#S2.E7 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")) has a positive weight, which is answered by the following proposition. Hence, our RPU indeed incentivizes randomization.

###### Proposition 2.4

For any admissible control 𝛑\boldsymbol{\pi}, we have (1−γ)​Jt𝛑+1>0(1-\gamma)J^{\boldsymbol{\pi}}\_{t}+1>0 almost surely.

###### Proof 2.5

Proof.
Recall that RPU satisfies the BSDE ([8](https://arxiv.org/html/2602.13544v1#S2.E8 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")). Given an admissible control 𝛑\boldsymbol{\pi}, the condition (i​i)(ii) in Definition [2.3](https://arxiv.org/html/2602.13544v1#S2.Thmtheorem3 "Definition 2.3 ‣ 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation") guarantees that the solution to ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) exists, and can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt𝝅=w0exp{∫0t\displaystyle W\_{t}^{\boldsymbol{\pi}}=w\_{0}\exp\bigg\{\int\_{0}^{t} | [r+(μs−r)Mean(𝝅s)+12σs2(Mean(𝝅s)2+Var(𝝅s))]ds\displaystyle\left[r+(\mu\_{s}-r)\operatorname{Mean}(\boldsymbol{\pi}\_{s})+\frac{1}{2}\sigma\_{s}^{2}\left(\operatorname{Mean}(\boldsymbol{\pi}\_{s})^{2}+\operatorname{Var}(\boldsymbol{\pi}\_{s})\right)\right]\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σs[Mean(𝝅s)dBs+Var⁡(𝝅s)dB¯s]}>0.\displaystyle+\sigma\_{s}\left[\operatorname{Mean}(\boldsymbol{\pi}\_{s})\mathrm{d}B\_{s}+\sqrt{\operatorname{Var}(\boldsymbol{\pi}\_{s})}\mathrm{d}\bar{B}\_{s}\right]\bigg\}>0. |  |

In addition, ([8](https://arxiv.org/html/2602.13544v1#S2.E8 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")) is a linear BSDE, and the condition (i​i​i)(iii) in Definition [2.3](https://arxiv.org/html/2602.13544v1#S2.Thmtheorem3 "Definition 2.3 ‣ 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation") ensures that U​(WT𝛑)U(W\_{T}^{\boldsymbol{\pi}}) and {λ​(t,Xt)​ℋ​(𝛑t)}t∈[0,T]\{\lambda(t,X\_{t})\mathcal{H}(\boldsymbol{\pi}\_{t})\}\_{t\in[0,T]} are respectively square-integrable random variable and process. Hence by El Karoui et al. ([1997](https://arxiv.org/html/2602.13544v1#bib.bib17), Proposition 2.2), ([8](https://arxiv.org/html/2602.13544v1#S2.E8 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")) admits a unique square-integrable solution.

Define Y~t𝛑:=(1−γ)​Jt𝛑+1\tilde{Y}^{\boldsymbol{\pi}}\_{t}:=(1-\gamma)J\_{t}^{\boldsymbol{\pi}}+1. Applying Itô’s lemma, we obtain that Y~𝛑\tilde{Y}^{\boldsymbol{\pi}} solves the following BSDE:

|  |  |  |
| --- | --- | --- |
|  | d​Y~t𝝅=−(1−γ)​λ​(t,Xt)​ℋ​(𝝅t)​Y~t𝝅​d​t+(1−γ)​𝐙~t𝝅⋅d​𝐁t,Y~T𝝅=(WT𝝅)1−γ>0.\mathrm{d}\tilde{Y}^{\boldsymbol{\pi}}\_{t}=-(1-\gamma)\lambda(t,X\_{t})\mathcal{H}(\boldsymbol{\pi}\_{t})\tilde{Y}^{\boldsymbol{\pi}}\_{t}\mathrm{d}t+(1-\gamma)\tilde{\mathbf{Z}}^{\boldsymbol{\pi}}\_{t}\cdot\mathrm{d}\mathbf{B}\_{t},\ \tilde{Y}^{\boldsymbol{\pi}}\_{T}=({W\_{T}^{\boldsymbol{\pi}}})^{1-\gamma}>0. |  |

From the comparison principle of linear BSDEs (see El Karoui et al. [1997](https://arxiv.org/html/2602.13544v1#bib.bib17), Corollary 2.2), it follows that Y~t𝛑>0\tilde{Y}^{\boldsymbol{\pi}}\_{t}>0 almost surely.∎

To apply dynamic programming to problem ([7](https://arxiv.org/html/2602.13544v1#S2.E7 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")), we further restrict our attention to feedback policies. A (randomized) feedback policy (or simply a policy) 𝝅=𝝅​(⋅,⋅,⋅)\boldsymbol{\pi}=\boldsymbol{\pi}(\cdot,\cdot,\cdot) is a density-valued function of time and state,
under which ([2](https://arxiv.org/html/2602.13544v1#S2.E2 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")) and ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) become a Markovian system. For any initial time tt and initial state (w,x)(w,x), a policy 𝝅\boldsymbol{\pi} induces the open-loop control 𝝅s=𝝅​(s,Ws𝝅,Xs)\boldsymbol{\pi}\_{s}=\boldsymbol{\pi}(s,W\_{s}^{\boldsymbol{\pi}},X\_{s}), where {Xs}s∈[t,T]\{X\_{s}\}\_{s\in[t,T]} and {Ws𝝅}s∈[t,T]\{W\_{s}^{\boldsymbol{\pi}}\}\_{s\in[t,T]} are the solutions to the corresponding Markovian system given Wt𝝅=wW\_{t}^{\boldsymbol{\pi}}=w and Xt=xX\_{t}=x. Denote by Π\Pi the set of policies that induce admissible open-loop controls.

Given 𝝅∈Π\boldsymbol{\pi}\in\Pi, define its value function V𝝅​(⋅,⋅,⋅)V^{\boldsymbol{\pi}}(\cdot,\cdot,\cdot) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V𝝅​(t,w,x):=\displaystyle V^{\boldsymbol{\pi}}(t,w,x)= | 𝔼​[∫tTe−∫ts−λ​(1−γ)​ℋ​(𝝅τ)​d​τ​λ​ℋ​(𝝅s)​ds+e−∫tT−λ​(1−γ)​ℋ​(𝝅τ)​d​τ​U​(WT𝝅)|Wt𝝅=w,Xt=x],\displaystyle\mathbb{E}\big[\int\_{t}^{T}e^{-\int\_{t}^{s}-\lambda(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{\tau})\mathrm{d}\tau}\lambda\mathcal{H}(\boldsymbol{\pi}\_{s})\mathrm{d}s+e^{-\int\_{t}^{T}-\lambda(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{\tau})\mathrm{d}\tau}U(W\_{T}^{\boldsymbol{\pi}})\Big|W\_{t}^{\boldsymbol{\pi}}=w,X\_{t}=x\big], |  | (10) |
|  |  | (t,w,x)∈[0,T]×ℝ+×ℝ.\displaystyle\;\;\;\;(t,w,x)\in[0,T]\times{\mathbb{R}}\_{+}\times{\mathbb{R}}. |  |

The Feynman-Kac formula yields that this function satisfies the PDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂V𝝅​(t,w,x)∂t\displaystyle\frac{\partial V^{\boldsymbol{\pi}}(t,w,x)}{\partial t} | +(r+(μ​(t,x)−r)​Mean⁡(𝝅​(t,w,x)))​w​Vw𝝅​(t,w,x)\displaystyle+\Big(r+\big(\mu(t,x)-r\big)\operatorname{Mean}\left(\boldsymbol{\pi}(t,w,x)\right)\Big)wV^{\boldsymbol{\pi}}\_{w}(t,w,x) |  | (11) |
|  |  | +12σ2(t,x)(Mean(𝝅(t,w,x))2+Var(𝝅(t,w,x)))w2Vw​w𝝅(t,w,x)\displaystyle+\frac{1}{2}\sigma^{2}(t,x)\Big(\operatorname{Mean}\left(\boldsymbol{\pi}(t,w,x)\right)^{2}+\operatorname{Var}\left(\boldsymbol{\pi}(t,w,x)\right)\Big)w^{2}V^{\boldsymbol{\pi}}\_{ww}(t,w,x) |  |
|  |  | +m​(t,x)​Vx𝝅​(t,w,x)+12​ν2​(t,x)​Vx​x𝝅​(t,w,x)+ρ​ν​(t,x)​σ​(t,x)​Mean⁡(𝝅)​w​Vx​w𝝅​(t,w,x)\displaystyle+m(t,x)V^{\boldsymbol{\pi}}\_{x}(t,w,x)+\frac{1}{2}\nu^{2}(t,x)V^{\boldsymbol{\pi}}\_{xx}(t,w,x)+\rho\nu(t,x)\sigma(t,x)\operatorname{Mean}(\boldsymbol{\pi})wV^{\boldsymbol{\pi}}\_{xw}(t,w,x) |  |
|  |  | +λ​(t,x)​ℋ​(𝝅​(t,w,x))​[(1−γ)​V𝝅​(t,w,x)+1]=0,V𝝅​(T,w,x)=U​(w).\displaystyle+\lambda(t,x)\mathcal{H}\left(\boldsymbol{\pi}(t,w,x)\right)\big[(1-\gamma)V^{\boldsymbol{\pi}}(t,w,x)+1\big]=0,\ V^{\boldsymbol{\pi}}(T,w,x)=U(w). |  |

Using the relation between BSDEs and PDEs, we can represent the recursive utility J𝝅J^{\boldsymbol{\pi}} via the value function V𝝅V^{\boldsymbol{\pi}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt𝝅=V𝝅​(t,Wt𝝅,Xt),a.s.,t∈[0,T],J\_{t}^{\boldsymbol{\pi}}=V^{\boldsymbol{\pi}}(t,W\_{t}^{\boldsymbol{\pi}},X\_{t}),\;\;\mbox{a.s.},\;\;\;t\in[0,T], |  | (12) |

where {Xt}t∈[0,T]\{X\_{t}\}\_{t\in[0,T]} and {Wt𝝅}t∈[0,T]\{W^{\boldsymbol{\pi}}\_{t}\}\_{t\in[0,T]} satisfy ([2](https://arxiv.org/html/2602.13544v1#S2.E2 "In 2.1 Market Environment and Investment Objective ‣ 2 Problem Formulation")) and ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")) with W0𝝅=w0W\_{0}^{\boldsymbol{\pi}}=w\_{0} and X0=x0X\_{0}=x\_{0}, respectively.

Finally, we define the optimal value function as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,w,x):=sup𝝅∈ΠJ𝝅​(t,w,x),(t,w,x)∈[0,T]×ℝ+×ℝ.V(t,w,x):=\sup\_{\boldsymbol{\pi}\in\Pi}J^{\boldsymbol{\pi}}(t,w,x),\;\;(t,w,x)\in[0,T]\times{\mathbb{R}}\_{+}\times{\mathbb{R}}. |  | (13) |

## 3 Theoretical Analysis

### 3.1 Gaussian Randomization

It is straightforward, as in Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)), to derive that the optimal value function VV satisfies the following HJB equation via dynamic programming:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∂V∂t+sup𝝅∈𝒫​(ℝ){(r+(μ(t,x)−r)Mean(𝝅))wVw+12σ2(t,x)(Mean(𝝅)2+Var(𝝅))w2Vw​w\displaystyle\frac{\partial V}{\partial t}+\sup\_{\boldsymbol{\pi}\in\mathcal{P}(\mathbb{R})}\Bigg\{\Big(r+\big(\mu(t,x)-r\big)\operatorname{Mean}(\boldsymbol{\pi})\Big)wV\_{w}+\frac{1}{2}\sigma^{2}(t,x)\Big(\operatorname{Mean}(\boldsymbol{\pi})^{2}+\operatorname{Var}(\boldsymbol{\pi})\Big)w^{2}V\_{ww} |  | (14) |
|  |  | +m(t,x)Vx+12ν2(t,x)Vx​x+ρν(t,x)σ(t,x)Mean(𝝅)wVw​x+λ(t,x)ℋ(𝝅)[(1−γ)V+1]}=0,\displaystyle+m(t,x)V\_{x}+\frac{1}{2}\nu^{2}(t,x)V\_{xx}+\rho\nu(t,x)\sigma(t,x)\operatorname{Mean}(\boldsymbol{\pi})wV\_{wx}+\lambda(t,x)\mathcal{H}(\boldsymbol{\pi})\big[(1-\gamma)V+1\big]\Bigg\}=0, |  |

with the terminal condition V​(T,w,x)=U​(w)=w1−γ−11−γV(T,w,x)=U(w)=\frac{w^{1-\gamma}-1}{1-\gamma}.

At first glance, equation ([14](https://arxiv.org/html/2602.13544v1#S3.E14 "In 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) is a highly nonlinear PDE and appears hard to analyze. However, we can reduce it to a simpler PDE based on which the optimal randomized policy can be explicitly represented.

###### Theorem 3.1

Suppose uu is a classical solution of the following PDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂u∂t\displaystyle\frac{\partial u}{\partial t} | +(1−γ)​r+m​(t,x)​ux+12​ν2​(t,x)​(ux​x+ux2)+(1−γ)​λ​(t,x)2​log⁡2​π​λ​(t,x)γ​σ2​(t,x)\displaystyle+(1-\gamma)r+m(t,x)u\_{x}+\frac{1}{2}\nu^{2}(t,x)(u\_{xx}+u\_{x}^{2})+\frac{(1-\gamma)\lambda(t,x)}{2}\log\frac{2\pi\lambda(t,x)}{\gamma\sigma^{2}(t,x)} |  | (15) |
|  |  | +1−γ2​γ​[(μ​(t,x)−r)2σ2​(t,x)+2​ρ​(μ​(t,x)−r)​ν​(t,x)σ​(t,x)​ux+ρ2​ν2​(t,x)​ux2]=0,\displaystyle+\frac{1-\gamma}{2\gamma}\left[\frac{\big(\mu(t,x)-r\big)^{2}}{\sigma^{2}(t,x)}+\frac{2\rho\big(\mu(t,x)-r\big)\nu(t,x)}{\sigma(t,x)}u\_{x}+\rho^{2}\nu^{2}(t,x)u\_{x}^{2}\right]=0, |  |

with the terminal condition u​(T,x)=0u(T,x)=0, and the derivatives of uu up to the second order have polynomial growth. Let 𝛑∗​(t,x)\boldsymbol{\pi}^{\*}(t,x) be a normal distribution with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mean⁡(𝝅∗​(t,x))=μ​(t,x)−rγ​σ2​(t,x)+ρ​ν​(t,x)γ​σ​(t,x)​ux​(t,x),Var⁡(𝝅∗​(t,x))=λ​(t,x)γ​σ2​(t,x).\operatorname{Mean}(\boldsymbol{\pi}^{\*}(t,x))=\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}+\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}(t,x),\ \operatorname{Var}(\boldsymbol{\pi}^{\*}(t,x))=\frac{\lambda(t,x)}{\gamma\sigma^{2}(t,x)}. |  | (16) |

If 𝛑∗∈Π\boldsymbol{\pi}^{\*}\in\Pi, then it is the optimal randomized policy. Furthermore, the optimal value function is V​(t,w,x)=w1−γ​eu​(t,x)−11−γV(t,w,x)=\frac{w^{1-\gamma}e^{u(t,x)}-1}{1-\gamma}.

###### Proof 3.2

Proof.
First, let us show how to deduce ([16](https://arxiv.org/html/2602.13544v1#S3.E16 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) from ([14](https://arxiv.org/html/2602.13544v1#S3.E14 "In 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")).
Note that the “supermum” in ([14](https://arxiv.org/html/2602.13544v1#S3.E14 "In 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) can be achieved via a two-stage optimization procedure: first maximize over distributions with a fixed mean and variance pair, and then maximize over all possible such pairs. For the first problem, the entropy is maximized at a normal distribution with the fixed mean and variance, with the maximum entropy value ℋ​(𝛑)=12​log⁡(2​π​e​Var⁡(𝛑))\mathcal{H}(\boldsymbol{\pi})=\frac{1}{2}\log\big(2\pi e\operatorname{Var}(\boldsymbol{\pi})\big) where Var⁡(𝛑)\operatorname{Var}(\boldsymbol{\pi}) is the given fixed variance. Therefore, ([14](https://arxiv.org/html/2602.13544v1#S3.E14 "In 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) can be simplified as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∂V∂t+supMean⁡(𝝅),Var⁡(𝝅){(r+(μ(t,x)−r)Mean(𝝅))wVw+12σ2(t,x)(Mean(𝝅)2+Var(𝝅))w2Vw​w\displaystyle\frac{\partial V}{\partial t}+\sup\_{\operatorname{Mean}(\boldsymbol{\pi}),\operatorname{Var}(\boldsymbol{\pi})}\Bigg\{\Big(r+\big(\mu(t,x)-r\big)\operatorname{Mean}(\boldsymbol{\pi})\Big)wV\_{w}+\frac{1}{2}\sigma^{2}(t,x)\Big(\operatorname{Mean}(\boldsymbol{\pi})^{2}+\operatorname{Var}(\boldsymbol{\pi})\Big)w^{2}V\_{ww} |  | (17) |
|  |  | +m(t,x)Vx+12ν2(t,x)Vx​x+ρν(t,x)σ(t,x)Mean(𝝅)wVw​x+λ​(t,x)2log(2πeVar(𝝅))[(1−γ)V+1]}=0.\displaystyle+m(t,x)V\_{x}+\frac{1}{2}\nu^{2}(t,x)V\_{xx}+\rho\nu(t,x)\sigma(t,x)\operatorname{Mean}(\boldsymbol{\pi})wV\_{wx}+\frac{\lambda(t,x)}{2}\log\big(2\pi e\operatorname{Var}(\boldsymbol{\pi})\big)\big[(1-\gamma)V+1\big]\Bigg\}=0. |  |

To analyze the above PDE, we start with the ansatz that V​(t,w,x)=w1−γ1−γ​v​(t,x)−11−γV(t,w,x)=\frac{w^{1-\gamma}}{1-\gamma}v(t,x)-\frac{1}{1-\gamma} for some function vv. Then ([17](https://arxiv.org/html/2602.13544v1#S3.E17 "In Proof 3.2 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | w1−γ1−γ∂v∂t+supMean⁡(𝝅),Var⁡(𝝅){(r+(μ(t,x)−r)Mean(𝝅))w1−γv−γ2σ2(t,x)(Mean(𝝅)2+Var(𝝅))w1−γv\displaystyle\frac{w^{1-\gamma}}{1-\gamma}\frac{\partial v}{\partial t}+\sup\_{\operatorname{Mean}(\boldsymbol{\pi}),\operatorname{Var}(\boldsymbol{\pi})}\Bigg\{\Big(r+\big(\mu(t,x)-r\big)\operatorname{Mean}(\boldsymbol{\pi})\Big)w^{1-\gamma}v-\frac{\gamma}{2}\sigma^{2}(t,x)\Big(\operatorname{Mean}(\boldsymbol{\pi})^{2}+\operatorname{Var}(\boldsymbol{\pi})\Big)w^{1-\gamma}v |  | (18) |
|  |  | +m(t,x)w1−γ1−γvx+12ν2(t,x)w1−γ1−γvx​x+ρν(t,x)σ(t,x)Mean(𝝅)w1−γvx+λ​(t,x)2log(2πeVar(𝝅))w1−γv}=0.\displaystyle+m(t,x)\frac{w^{1-\gamma}}{1-\gamma}v\_{x}+\frac{1}{2}\nu^{2}(t,x)\frac{w^{1-\gamma}}{1-\gamma}v\_{xx}+\rho\nu(t,x)\sigma(t,x)\operatorname{Mean}(\boldsymbol{\pi})w^{1-\gamma}v\_{x}+\frac{\lambda(t,x)}{2}\log\big(2\pi e\operatorname{Var}(\boldsymbol{\pi})\big)w^{1-\gamma}v\Bigg\}=0. |  |

If v>0v>0 (to be verified later), then the first-order conditions of the maximization problem on the left-hand side of the above equation yield the maximizers

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mean⁡(𝝅∗)=μ​(t,x)−rγ​σ2​(t,x)+ρ​ν​(t,x)​vx​(t,x)γ​σ​(t,x)​v​(t,x),Var⁡(𝝅∗)=λ​(t,x)γ​σ2​(t,x).\operatorname{Mean}(\boldsymbol{\pi}^{\*})=\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}+\frac{\rho\nu(t,x)v\_{x}(t,x)}{\gamma\sigma(t,x)v(t,x)},\;\;\;\operatorname{Var}(\boldsymbol{\pi}^{\*})=\frac{\lambda(t,x)}{\gamma\sigma^{2}(t,x)}. |  | (19) |

Plugging the above into ([18](https://arxiv.org/html/2602.13544v1#S3.E18 "In Proof 3.2 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) and
canceling the term w1−γw^{1-\gamma}, we have that vv satisfies the following nonlinear PDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂v∂t\displaystyle\frac{\partial v}{\partial t} | +(1−γ)​r​v+m​(t,x)​vx+12​ν2​(t,x)​vx​x+(1−γ)​λ​(t,x)​v2​log⁡2​π​λ​(t,x)γ​σ2​(t,x)\displaystyle+(1-\gamma)rv+m(t,x)v\_{x}+\frac{1}{2}\nu^{2}(t,x)v\_{xx}+\frac{(1-\gamma)\lambda(t,x)v}{2}\log\frac{2\pi\lambda(t,x)}{\gamma\sigma^{2}(t,x)} |  | (20) |
|  |  | +1−γ2​γ​[(μ​(t,x)−r)2σ2​(t,x)​v+2​ρ​(μ​(t,x)−r)​ν​(t,x)σ​(t,x)​vx+ρ2​ν2​(t,x)​vx2v]=0,\displaystyle+\frac{1-\gamma}{2\gamma}\Big[\frac{\big(\mu(t,x)-r\big)^{2}}{\sigma^{2}(t,x)}v+\frac{2\rho\big(\mu(t,x)-r\big)\nu(t,x)}{\sigma(t,x)}v\_{x}+\rho^{2}\nu^{2}(t,x)\frac{v\_{x}^{2}}{v}\Big]=0, |  |

with the terminal condition v​(T,x)=1v(T,x)=1.

Letting uu be the solution to ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")), we can directly verify that v​(t,x)=eu​(t,x)>0v(t,x)=e^{u(t,x)}>0 solves ([20](https://arxiv.org/html/2602.13544v1#S3.E20 "In Proof 3.2 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")). The desired expression ([16](https://arxiv.org/html/2602.13544v1#S3.E16 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) now follows from ([19](https://arxiv.org/html/2602.13544v1#S3.E19 "In Proof 3.2 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")).

Next we prove that the policy with ([16](https://arxiv.org/html/2602.13544v1#S3.E16 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) is optimal and V​(t,w,x)=w1−γ​eu​(t,x)−11−γV(t,w,x)=\frac{w^{1-\gamma}e^{u(t,x)}-1}{1-\gamma} is the optimal value function.
Denote Kt𝛑=∫0tλ​(s,Xs)​(1−γ)​ℋ​(𝛑s)​dsK\_{t}^{\boldsymbol{\pi}}=\int\_{0}^{t}\lambda(s,X\_{s})(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{s})\mathrm{d}s. Apply Itô’s formula to eKt​V​(t,Wt𝛑,Xt)e^{K\_{t}}V(t,W^{\boldsymbol{\pi}}\_{t},X\_{t}) to get

|  |  |  |
| --- | --- | --- |
|  | d​(eKt𝝅​V​(t,Wt𝝅,Xt))={∂V∂t+[r+(μ(t,Xt)−r)Mean(𝝅t)]Wt𝝅Vw+m(t,Xt)Vx+12σ2(t,Xt)[Mean(𝝅t)2+Var(𝝅t)](Wt𝝅)2Vw​w+12ν2(t,Xt)Vx​x+ρν(t,Xt)σ(t,Xt)Mean(𝝅t)Wt𝝅Vw+λ(1−γ)ℋ(𝝅t)V}eKt𝝅dt+{[σ(t,Xt)Mean(𝝅t)Wt𝝅Vw+ρν(t,Xt)Vx]dBt+1−ρ2ν(t,Xt)VxdB~t+Var⁡(𝝅t)σ(t,Xt)Wt𝝅VwdB¯t}eKt𝝅.\begin{split}&\mathrm{d}\left(e^{K\_{t}^{\boldsymbol{\pi}}}V(t,W^{\boldsymbol{\pi}}\_{t},X\_{t})\right)\\ =&\bigg\{\frac{\partial V}{\partial t}+\left[r+(\mu(t,X\_{t})-r)\operatorname{Mean}(\boldsymbol{\pi}\_{t})\right]W^{\boldsymbol{\pi}}\_{t}V\_{w}+m(t,X\_{t})V\_{x}+\frac{1}{2}\sigma^{2}(t,X\_{t})\left[\operatorname{Mean}(\boldsymbol{\pi}\_{t})^{2}+\operatorname{Var}(\boldsymbol{\pi}\_{t})\right](W^{\boldsymbol{\pi}}\_{t})^{2}V\_{ww}\\ &+\frac{1}{2}\nu^{2}(t,X\_{t})V\_{xx}+\rho\nu(t,X\_{t})\sigma(t,X\_{t})\operatorname{Mean}(\boldsymbol{\pi}\_{t})W^{\boldsymbol{\pi}}\_{t}V\_{w}+\lambda(1-\gamma)\mathcal{H}(\boldsymbol{\pi}\_{t})V\bigg\}e^{K\_{t}^{\boldsymbol{\pi}}}\mathrm{d}t\\ &+\bigg\{\left[\sigma(t,X\_{t})\operatorname{Mean}(\boldsymbol{\pi}\_{t})W^{\boldsymbol{\pi}}\_{t}V\_{w}+\rho\nu(t,X\_{t})V\_{x}\right]\mathrm{d}B\_{t}\\ &+\sqrt{1-\rho^{2}}\nu(t,X\_{t})V\_{x}\mathrm{d}\tilde{B}\_{t}+\sqrt{\operatorname{Var}(\boldsymbol{\pi}\_{t})}\sigma(t,X\_{t})W^{\boldsymbol{\pi}}\_{t}V\_{w}\mathrm{d}\bar{B}\_{t}\bigg\}e^{K\_{t}^{\boldsymbol{\pi}}}.\end{split} |  |

Define a sequence of stopping times τn=inf{t≥0:|Xt|∨(Wt𝛑)1−γ∨eKt𝛑≥n}\tau\_{n}=\inf\{t\geq 0:|X\_{t}|\vee(W\_{t}^{\boldsymbol{\pi}})^{1-\gamma}\vee e^{K\_{t}^{\boldsymbol{\pi}}}\geq n\}.
Then by ([17](https://arxiv.org/html/2602.13544v1#S3.E17 "In Proof 3.2 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | eKT∧τn𝝅​V​(T∧τn,WT∧τn𝝅,XT∧τn)−V​(0,W0𝝅,X0)\displaystyle e^{K\_{T\wedge\tau\_{n}}^{\boldsymbol{\pi}}}V(T\wedge\tau\_{n},W^{\boldsymbol{\pi}}\_{T\wedge\tau\_{n}},X\_{T\wedge\tau\_{n}})-V(0,W^{\boldsymbol{\pi}}\_{0},X\_{0}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∫0T∧τn−λ(s,Xs)ℋ(𝝅s)eKs𝝅ds+eKs𝝅(Ws𝝅)1−γeu​(s,Xs){[σ(s,Xs)Mean(𝝅s)+ρν(s,Xs)ux​(s,Xs)1−γ]dBs\displaystyle\int\_{0}^{T\wedge\tau\_{n}}-\lambda(s,X\_{s})\mathcal{H}(\boldsymbol{\pi}\_{s})e^{K\_{s}^{\boldsymbol{\pi}}}\mathrm{d}s+e^{K\_{s}^{\boldsymbol{\pi}}}(W^{\boldsymbol{\pi}}\_{s})^{1-\gamma}e^{u(s,X\_{s})}\bigg\{\left[\sigma(s,X\_{s})\operatorname{Mean}(\boldsymbol{\pi}\_{s})+\rho\nu(s,X\_{s})\frac{u\_{x}(s,X\_{s})}{1-\gamma}\right]\mathrm{d}B\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−ρ2ν(s,Xs)ux​(s,Xs)1−γdB~s+Var⁡(𝝅s)σ(s,Xs)dB¯s},\displaystyle+\sqrt{1-\rho^{2}}\nu(s,X\_{s})\frac{u\_{x}(s,X\_{s})}{1-\gamma}\mathrm{d}\tilde{B}\_{s}+\sqrt{\operatorname{Var}(\boldsymbol{\pi}\_{s})}\sigma(s,X\_{s})\mathrm{d}\bar{B}\_{s}\bigg\}, |  |

while “==” holds when 𝛑=𝛑∗\boldsymbol{\pi}=\boldsymbol{\pi}^{\*} as given in ([16](https://arxiv.org/html/2602.13544v1#S3.E16 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")).

Recall that uu and its derivatives have polynomial growth in xx; hence we have an estimate about the quadratic variation term above

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼[∫0T∧τne2​Ks𝝅(Ws𝝅)2​(1−γ)e2​u​(s,Xs){[σ(s,Xs)Mean(𝝅s)+ρν(s,Xs)ux​(s,Xs)1−γ]2\displaystyle\mathbb{E}\Bigg[\int\_{0}^{T\wedge\tau\_{n}}e^{2K\_{s}^{\boldsymbol{\pi}}}(W^{\boldsymbol{\pi}}\_{s})^{2(1-\gamma)}e^{2u(s,X\_{s})}\bigg\{\left[\sigma(s,X\_{s})\operatorname{Mean}(\boldsymbol{\pi}\_{s})+\rho\nu(s,X\_{s})\frac{u\_{x}(s,X\_{s})}{1-\gamma}\right]^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ρ2)ν2(s,Xs)ux2​(s,Xs)(1−γ)2+Var(𝝅s)σ2(s,Xs)}ds]\displaystyle+(1-\rho^{2})\nu^{2}(s,X\_{s})\frac{u\_{x}^{2}(s,X\_{s})}{(1-\gamma)^{2}}+\operatorname{Var}(\boldsymbol{\pi}\_{s})\sigma^{2}(s,X\_{s})\bigg\}\mathrm{d}s\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼[∫0TCn{σ2(s,Xs)[Mean(𝝅s)2+Var(𝝅s)]+1}ds]\displaystyle\mathbb{E}\left[\int\_{0}^{T}C\_{n}\bigg\{\sigma^{2}(s,X\_{s})\left[\operatorname{Mean}(\boldsymbol{\pi}\_{s})^{2}+\operatorname{Var}(\boldsymbol{\pi}\_{s})\right]+1\bigg\}\mathrm{d}s\right] |  |

for some constants Cn>0C\_{n}>0.
Therefore, the expectations of the corresponding stochastic integrals are all 0. When 𝛑\boldsymbol{\pi} is admissible, by the condition (i​iii) in Definition [2.3](https://arxiv.org/html/2602.13544v1#S2.Thmtheorem3 "Definition 2.3 ‣ 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation"), we deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | V​(0,w0,x0)\displaystyle V(0,w\_{0},x\_{0}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | 𝔼​[eKT∧τn𝝅​V​(T∧τn,WT∧τn𝝅,XT∧τn)+∫0T∧τnλ​(s,Xs)​ℋ​(𝝅s)​eKs𝝅​ds]\displaystyle\mathbb{E}\left[e^{K\_{T\wedge\tau\_{n}}^{\boldsymbol{\pi}}}V(T\wedge\tau\_{n},W^{\boldsymbol{\pi}}\_{T\wedge\tau\_{n}},X\_{T\wedge\tau\_{n}})+\int\_{0}^{T\wedge\tau\_{n}}\lambda(s,X\_{s})\mathcal{H}(\boldsymbol{\pi}\_{s})e^{K\_{s}^{\boldsymbol{\pi}}}\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[eKT∧τn𝝅​(WT∧τn𝝅)1−γ1−γ​eu​(T∧τn,XT∧τn)−eKT∧τn𝝅1−γ+∫0T∧τnλ​(s,Xs)​ℋ​(𝝅s)​eKs𝝅​ds]\displaystyle\mathbb{E}\left[e^{K\_{T\wedge\tau\_{n}}^{\boldsymbol{\pi}}}\frac{(W^{\boldsymbol{\pi}}\_{T\wedge\tau\_{n}})^{1-\gamma}}{1-\gamma}e^{u(T\wedge\tau\_{n},X\_{T\wedge\tau\_{n}})}-\frac{e^{K\_{T\wedge\tau\_{n}}^{\boldsymbol{\pi}}}}{1-\gamma}+\int\_{0}^{T\wedge\tau\_{n}}\lambda(s,X\_{s})\mathcal{H}(\boldsymbol{\pi}\_{s})e^{K\_{s}^{\boldsymbol{\pi}}}\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[eKT𝝅​(WT𝝅)1−γ1−γ​𝟙{τn>T}+eKτn𝝅​(Wτn𝝅)1−γ1−γ​eu​(τn,Xτn)​𝟙{τn≤T}−eKT∧τn𝝅1−γ+∫0T∧τnλ​(s,Xs)​ℋ​(𝝅s)​eKs𝝅​ds].\displaystyle\mathbb{E}\left[e^{K\_{T}^{\boldsymbol{\pi}}}\frac{(W^{\boldsymbol{\pi}}\_{T})^{1-\gamma}}{1-\gamma}\mathbbm{1}\_{\{\tau\_{n}>T\}}+e^{K\_{\tau\_{n}}^{\boldsymbol{\pi}}}\frac{(W^{\boldsymbol{\pi}}\_{\tau\_{n}})^{1-\gamma}}{1-\gamma}e^{u(\tau\_{n},X\_{\tau\_{n}})}\mathbbm{1}\_{\{\tau\_{n}\leq T\}}-\frac{e^{K\_{T\wedge\tau\_{n}}^{\boldsymbol{\pi}}}}{1-\gamma}+\int\_{0}^{T\wedge\tau\_{n}}\lambda(s,X\_{s})\mathcal{H}(\boldsymbol{\pi}\_{s})e^{K\_{s}^{\boldsymbol{\pi}}}\mathrm{d}s\right]. |  |

By the condition (i​i​iiii) in Definition [2.3](https://arxiv.org/html/2602.13544v1#S2.Thmtheorem3 "Definition 2.3 ‣ 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[∫0Tλ​(t,Xt)​|ℋ​(𝝅t)|​eKt𝝅​dt]≤𝔼​[∫0Tλ​(t,Xt)​|ℋ​(𝝅t)|​e∫0tλ​|1−γ|​|ℋ​(𝝅s)|​ds​dt]\displaystyle\mathbb{E}\left[\int\_{0}^{T}\lambda(t,X\_{t})|\mathcal{H}(\boldsymbol{\pi}\_{t})|e^{K\_{t}^{\boldsymbol{\pi}}}\mathrm{d}t\right]\leq\mathbb{E}\left[\int\_{0}^{T}\lambda(t,X\_{t})|\mathcal{H}(\boldsymbol{\pi}\_{t})|e^{\int\_{0}^{t}\lambda|1-\gamma||\mathcal{H}(\boldsymbol{\pi}\_{s})|\mathrm{d}s}\mathrm{d}t\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​[∫0Tλ​(t,Xt)​|ℋ​(𝝅t)|​dt​e∫0Tλ​|1−γ|​|ℋ​(𝝅s)|​ds]\displaystyle\mathbb{E}\left[\int\_{0}^{T}\lambda(t,X\_{t})|\mathcal{H}(\boldsymbol{\pi}\_{t})|\mathrm{d}te^{\int\_{0}^{T}\lambda|1-\gamma||\mathcal{H}(\boldsymbol{\pi}\_{s})|\mathrm{d}s}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (𝔼​[(∫0Tλ​(t,Xt)​|ℋ​(𝝅t)|​dt)2])1/2​(𝔼​[e∫0T2​λ​|1−γ|​|ℋ​(𝝅s)|​ds])1/2<∞,\displaystyle\left(\mathbb{E}\left[\left(\int\_{0}^{T}\lambda(t,X\_{t})|\mathcal{H}(\boldsymbol{\pi}\_{t})|\mathrm{d}t\right)^{2}\right]\right)^{1/2}\left(\mathbb{E}\left[e^{\int\_{0}^{T}2\lambda|1-\gamma||\mathcal{H}(\boldsymbol{\pi}\_{s})|\mathrm{d}s}\right]\right)^{1/2}<\infty, |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[eKT𝝅​(WT𝝅)1−γ]≤(𝔼​[e∫0T2​λ​|1−γ|​|ℋ​(𝝅s)|​ds])1/2​(𝔼​[(WT𝝅)2−2​γ])1/2<∞.\mathbb{E}\left[e^{K^{\boldsymbol{\pi}}\_{T}}(W^{\boldsymbol{\pi}}\_{T})^{1-\gamma}\right]\leq\left(\mathbb{E}\left[e^{\int\_{0}^{T}2\lambda|1-\gamma||\mathcal{H}(\boldsymbol{\pi}\_{s})|\mathrm{d}s}\right]\right)^{1/2}\left(\mathbb{E}\left[(W^{\boldsymbol{\pi}}\_{T})^{2-2\gamma}\right]\right)^{1/2}<\infty. |  |

Taking lim supn→∞\limsup\_{n\to\infty}, we conclude from the dominated convergence theorem and Fatou’s lemma that

|  |  |  |
| --- | --- | --- |
|  | V​(0,w0,x0)≥𝔼​[eKT𝝅​U​(WT𝝅)+∫0Tλ​(s,Xs)​ℋ​(𝝅s)​eKs𝝅​ds]=J0𝝅.V(0,w\_{0},x\_{0})\geq\mathbb{E}\left[e^{K\_{T}^{\boldsymbol{\pi}}}U(W\_{T}^{\boldsymbol{\pi}})+\int\_{0}^{T}\lambda(s,X\_{s})\mathcal{H}(\boldsymbol{\pi}\_{s})e^{K\_{s}^{\boldsymbol{\pi}}}\mathrm{d}s\right]=J\_{0}^{\boldsymbol{\pi}}. |  |

To show “==” for 𝛑∗\boldsymbol{\pi}^{\*}, we can directly verify that Vt=V​(t,Wt𝛑∗,Xt)V\_{t}=V(t,W\_{t}^{\boldsymbol{\pi}^{\*}},X\_{t}) satisfies the BSDE ([8](https://arxiv.org/html/2602.13544v1#S2.E8 "In 2.3 Recursive Perturbation Utility ‣ 2 Problem Formulation")), and hence VtV\_{t} is the recursive utility process under 𝛑∗\boldsymbol{\pi}^{\*}. This completes our proof.
∎

Some remarks are in order. First,
the optimal randomized policy follows Gaussian with its mean and variance explicitly given via the PDE ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")), even if the current setup is neither LQ nor mean-variance. The policy variance depends only on the exogenously given primary temperature function λ\lambda, the risk aversion parameter γ\gamma, and the instantaneous variance function σ2\sigma^{2}. A larger primary temperature increases the level of randomization, while a greater risk aversion or volatility reduces it. These results are mathematically consistent with those in Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)) and Dai et al. ([2023](https://arxiv.org/html/2602.13544v1#bib.bib10)), even though in a different context (i.e., RL), who consider an LQ control and an equilibrium mean-variance criterion, respectively. Second, the mean of the optimal policy consists of two parts: a myopic part μ​(t,x)−rγ​σ2​(t,x)\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)} independent of randomization, and a hedging part represented by

|  |  |  |
| --- | --- | --- |
|  | ρ​ν​(t,x)γ​σ​(t,x)​ux​(t,x)=Cov⁡(d​Xt,d​log⁡St)Var⁡(d​log⁡St)​ux​(t,Xt).\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}(t,x)=\frac{\operatorname{Cov}(\mathrm{d}X\_{t},\mathrm{d}\log S\_{t})}{\operatorname{Var}(\mathrm{d}\log S\_{t})}u\_{x}(t,X\_{t}). |  |

Note that hedging is needed due to the presence of the factor XX even in the classical Merton setting; yet the level of hedging is altered by the agent randomization because uu depends on the choice of λ\lambda via the PDE ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")).
As a result, unlike the previous works (e.g., Wang et al. [2020](https://arxiv.org/html/2602.13544v1#bib.bib47), Wang and Zhou [2020](https://arxiv.org/html/2602.13544v1#bib.bib48), and Dai et al. [2023](https://arxiv.org/html/2602.13544v1#bib.bib10)) where the optimal policies depend on randomization only through variance and are thus unbiased, the optimal policies here are generally biased and the degree of biasedness depends on that of randomization. We will investigate this feature in more detail in the following subsections. Finally,
the resulting weight of randomization in the objective function is λ​(t,x)​[(1−γ)​V​(t,w,x)+1]=λ​(t,x)​w1−γ​eu​(t,x)>0\lambda(t,x)[(1-\gamma)V(t,w,x)+1]=\lambda(t,x)w^{1-\gamma}e^{u(t,x)}>0. When λ​(t,x)\lambda(t,x) is a constant and γ=1\gamma=1, u≡0u\equiv 0 is the solution to ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) and, as a consequence, the weight reduces to a constant as in the APU objective ([6](https://arxiv.org/html/2602.13544v1#S2.E6 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")).

### 3.2 When is the Optimal Randomized Policy Unbiased?

When λ≡0\lambda\equiv 0, the optimal Gaussian distribution in Theorem [3.1](https://arxiv.org/html/2602.13544v1#S3.Thmtheorem1 "Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis") degenerates into the Dirac measure concentrating on the mean, μ​(t,x)−rγ​σ2​(t,x)+ρ​ν​(t,x)γ​σ​(t,x)​ux​(t,x)\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}+\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}(t,x), where uu solves ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) with λ≡0\lambda\equiv 0. This is Merton’s strategy for the classical problem (in the incomplete market) without preference for randomization. We refer to the case λ≡0\lambda\equiv 0 as the “classical case” in the rest of this paper. As we have pointed out, unlike the existing results, the mean of the optimal randomized policy does not generally coincide with that of the classical counterpart due to an interaction between randomization and hedging.121212One should, however, note that biased exploratory/randomized policies are common in the RL literature for various reasons. For example, the ϵ\epsilon-greedy policy is a convex combination of the (classically) optimal one and a purely random policy; hence it is biased.

There are, however, special circumstances even in our setting where the optimal Gaussian policy becomes unbiased.
According to ([16](https://arxiv.org/html/2602.13544v1#S3.E16 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")), the part that causes biases is the hedging demand, ρ​ν​(t,x)γ​σ​(t,x)​ux​(t,x)\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}(t,x).
Hence, if ν≡0\nu\equiv 0 or ρ=0\rho=0 (i.e., the factor XX is deterministic or evolves independently from the stock price), then this part vanishes and the optimal policy becomes unbiased. In these cases, changes in the market factor do not affect the stock return or there is no hedging need against the factor, and thus a myopic policy irrelevant to our choice of λ\lambda is dynamically optimal.
Next, note that the only difference between the classical and RPU problems is reflected by the extra term (1−γ)​λ​(t,x)2​log⁡2​π​λ​(t,x)γ​σ2​(t,x)\frac{(1-\gamma)\lambda(t,x)}{2}\log\frac{2\pi\lambda(t,x)}{\gamma\sigma^{2}(t,x)} in the PDE ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")). If γ=1\gamma=1 (log-utility), then, for any choice of the function λ\lambda, this extra term vanishes, and hence the unbiasedness holds.
More generally, if one chooses λ\lambda such that
λ​(t,x)​log⁡2​π​λ​(t,x)γ​σ2​(t,x)\lambda(t,x)\log\frac{2\pi\lambda(t,x)}{\gamma\sigma^{2}(t,x)} is independent of xx, then, taking derivative in xx on both sides of ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) yields that uxu\_{x} satisfies the same PDE regardless of whether λ=0\lambda=0 or not. This in turn implies that the hedging part ρ​ν​(t,x)γ​σ​(t,x)​ux​(t,x)\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}(t,x) is independent of λ\lambda, leading to the unbiasedness of the optimal Gaussian policy.

A discussion of the unbiasedness will also be given from the BSDE perspective in Appendix [7](https://arxiv.org/html/2602.13544v1#S7 "7 A BSDE Perspective").

### 3.3 An Asymptotic Analysis on λ\lambda

The preference for randomization induces a different objective function for the investor and in general makes the optimal policy biased. In particular, randomization increases the uncertainty of the wealth process and thus lowers the bequest utility. It is interesting to investigate the financial losses due to this preference for randomization and quantify the impact of such a bias. We carry out this investigation by an asymptotic analysis on the PDE ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) in the small parameter λ\lambda, which is henceforth assumed to be a constant (instead of a function) λ​(t,x)≡λ\lambda(t,x)\equiv\lambda, leading to asymptotic expansions of the optimal policy along with its value function.

We denote by u(0)u^{(0)} the solution to ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) with λ=0\lambda=0 and by V(0)V^{(0)} the optimal value function for the classical problem (i.e., when λ=0\lambda=0).
It follows from Theorem [3.1](https://arxiv.org/html/2602.13544v1#S3.Thmtheorem1 "Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis") that V(0)​(t,w,x)=w1−γ​eu(0)​(t,x)−11−γV^{(0)}(t,w,x)=\frac{w^{1-\gamma}e^{u^{(0)}(t,x)}-1}{1-\gamma}. For any λ>0\lambda>0, let 𝝅∗\boldsymbol{\pi}^{\*} be the optimal randomized policy, and V(λ)V^{(\lambda)} be the value function of the original non-randomized problem under the deterministic policy that is the mean of 𝝅∗\boldsymbol{\pi}^{\*}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V(λ)​(t,w,x)=𝔼​[U​(WT𝝅∗^)|Wt𝝅∗^=w,Xt=x],V^{(\lambda)}(t,w,x)=\mathbb{E}\left[U\left(W\_{T}^{\widehat{\boldsymbol{\pi}^{\*}}}\right)\Big|W\_{t}^{\widehat{\boldsymbol{\pi}^{\*}}}=w,X\_{t}=x\right], |  | (21) |

where 𝝅∗^​(t,x)=𝒩​(Mean⁡(𝝅∗​(t,x)),0)\widehat{\boldsymbol{\pi}^{\*}}(t,x)=\mathcal{N}\left(\operatorname{Mean}\left(\boldsymbol{\pi}^{\*}(t,x)\right),0\right).

The results of our asymptotic analysis involve several functions, among which
u(1)u^{(1)} and u(2)u^{(2)} are respectively the solutions of the following PDEs:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∂u(1)∂t+m​(t,x)​ux(1)+12​ν2​(t,x)​ux​x(1)+1−γ2​log⁡2​πγ​σ2​(t,x)\displaystyle\frac{\partial u^{(1)}}{\partial t}+m(t,x)u^{(1)}\_{x}+\frac{1}{2}\nu^{2}(t,x)u^{(1)}\_{xx}+\frac{1-\gamma}{2}\log\frac{2\pi}{\gamma\sigma^{2}(t,x)} |  | (22) |
|  |  | +(1−γ)​ρ​ν​(t,x)​σ​(t,x)​μ​(t,x)−r+ρ​ν​(t,x)​σ​(t,x)​ux(0)γ​σ2​(t,x)​ux(1)=0,u(1)​(T,x)=0,\displaystyle+(1-\gamma)\rho\nu(t,x)\sigma(t,x)\frac{\mu(t,x)-r+\rho\nu(t,x)\sigma(t,x)u\_{x}^{(0)}}{\gamma\sigma^{2}(t,x)}u\_{x}^{(1)}=0,\ u^{(1)}(T,x)=0, |  |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∂u(2)∂t+m​(t,x)​ux(2)+12​ν2​(t,x)​ux​x(2)+1−γ2​γ​ρ2​ν2​(t,x)​ux(1)2\displaystyle\frac{\partial u^{(2)}}{\partial t}+m(t,x)u^{(2)}\_{x}+\frac{1}{2}\nu^{2}(t,x)u^{(2)}\_{xx}+\frac{1-\gamma}{2\gamma}\rho^{2}\nu^{2}(t,x){u\_{x}^{(1)}}^{2} |  | (23) |
|  |  | +(1−γ)​ρ​ν​(t,x)​σ​(t,x)​μ​(t,x)−r+ρ​ν​(t,x)​σ​(t,x)​ux(0)γ​σ2​(t,x)​ux(2)=0,u(2)​(T,x)=0.\displaystyle+(1-\gamma)\rho\nu(t,x)\sigma(t,x)\frac{\mu(t,x)-r+\rho\nu(t,x)\sigma(t,x)u\_{x}^{(0)}}{\gamma\sigma^{2}(t,x)}u\_{x}^{(2)}=0,\ u^{(2)}(T,x)=0. |  |

Moreover, ϕ(2)\phi^{(2)} is the solution to the PDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ϕ(2)∂t\displaystyle\frac{\partial\phi^{(2)}}{\partial t} | +m​(t,x)​ϕx(2)+12​ν2​(t,x)​(ϕx​x(2)+2​ux(0)​ϕx(2))\displaystyle+m(t,x)\phi^{(2)}\_{x}+\frac{1}{2}\nu^{2}(t,x)(\phi^{(2)}\_{xx}+2u^{(0)}\_{x}\phi^{(2)}\_{x}) |  | (24) |
|  |  | +(1−γ)​ρ​ν​(t,x)γ​σ​(t,x)​[μ​(t,x)−r+ρ​ν​(t,x)​σ​(t,x)​ux(0)]​ϕx(2)\displaystyle+\frac{(1-\gamma)\rho\nu(t,x)}{\gamma\sigma(t,x)}\big[\mu(t,x)-r+\rho\nu(t,x)\sigma(t,x)u^{(0)}\_{x}\big]\phi^{(2)}\_{x} |  |
|  |  | −(1−γ)​ρ2​ν2​(t,x)2​γ​ux(1)2=0,ϕ(2)​(T,x)=0.\displaystyle-\frac{(1-\gamma)\rho^{2}\nu^{2}(t,x)}{2\gamma}{u^{(1)}\_{x}}^{2}=0,\ \phi^{(2)}(T,x)=0. |  |

###### Lemma 3.3

The solution uu of ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) admits the following Taylor expansion with respect to λ\lambda:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(t,x)=u(0)​(t,x)+(1−γ)​(T−t)2​λ​log⁡λ+λ​u(1)​(t,x)+λ2​u(2)​(t,x)+O​(λ3).u(t,x)=u^{(0)}(t,x)+\frac{(1-\gamma)(T-t)}{2}\lambda\log\lambda+\lambda u^{(1)}(t,x)+\lambda^{2}u^{(2)}(t,x)+O(\lambda^{3}). |  | (25) |

###### Proof 3.4

Proof.
The expansion ([25](https://arxiv.org/html/2602.13544v1#S3.E25 "In Lemma 3.3 ‣ 3.3 An Asymptotic Analysis on 𝜆 ‣ 3 Theoretical Analysis")) is motivated by observing that the λ\lambda terms in ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) are 1−γ2​λ​log⁡λ\frac{1-\gamma}{2}\lambda\log\lambda plus O​(λ)O(\lambda).
Plugging uu with the expansion into ([3.1](https://arxiv.org/html/2602.13544v1#S3.Thmtheorem1 "Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")), using the equation of u(0)u^{(0)} and equating the λ\lambda and λ2\lambda^{2} terms in the resulting equation, we easily derive
the equations ([22](https://arxiv.org/html/2602.13544v1#S3.E22 "In 3.3 An Asymptotic Analysis on 𝜆 ‣ 3 Theoretical Analysis")) and ([23](https://arxiv.org/html/2602.13544v1#S3.E23 "In 3.3 An Asymptotic Analysis on 𝜆 ‣ 3 Theoretical Analysis")).
∎

The policy that coincides with the mean of the optimal randomized policy is sub-optimal for the classical Merton problem due to randomization, which can be considered as a loss in the initial wealth.
For each fixed initial time-factor pair (t,x)(t,x), we define the equivalent relative wealth loss to be Δ=Δ​(t,x)\Delta=\Delta(t,x) such that the investor is indifferent between obtaining the optimal value without the preference for randomization with initial endowment w​(1−Δ)w(1-\Delta) and getting the value of the mean policy, Mean⁡(𝝅∗)\operatorname{Mean}(\boldsymbol{\pi}^{\*}), with initial endowment ww. That is, Δ\Delta is such that V(0)​(t,w​(1−Δ),x)=V(λ)​(t,w,x)V^{(0)}\big(t,w(1-\Delta),x\big)=V^{(\lambda)}(t,w,x). The equivalent relative wealth loss Δ\Delta measures the relative cost that the agent is willing to pay for the pleasure of randomization.

The following theorem quantifies the bias of the optimal randomized policy, the relative loss of utility, and the equivalent relative wealth loss, all in terms of λ\lambda asymptotically.

###### Theorem 3.5

The asymptotic expansion of the mean of the optimal randomized policy is

|  |  |  |
| --- | --- | --- |
|  | Mean⁡(𝝅∗​(t,x))=a∗​(t,x)+λ​ρ​ν​(t,x)γ​σ​(t,x)​ux(1)​(t,x)+O​(λ2),\operatorname{Mean}(\boldsymbol{\pi}^{\*}(t,x))=a^{\*}(t,x)+\lambda\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}^{(1)}(t,x)+O(\lambda^{2}), |  |

where a∗a^{\*} is the optimal policy for the classical case. Moreover, we have

|  |  |  |
| --- | --- | --- |
|  | V(λ)​(t,w,x)=w1−γ1−γ​exp⁡(u(0)​(t,x)+λ2​ϕ(2)​(t,x)+O​(λ3))−11−γ,V^{(\lambda)}(t,w,x)=\frac{w^{1-\gamma}}{1-\gamma}\exp\left(u^{(0)}(t,x)+\lambda^{2}\phi^{(2)}(t,x)+O(\lambda^{3})\right)-\frac{1}{1-\gamma}, |  |

along with the relative utility loss

|  |  |  |
| --- | --- | --- |
|  | |V(λ)​(t,w,x)−V(0)​(t,w,x)V(0)​(t,w,x)|=λ2​|ϕ(2)​(t,x)|⋅|1+1(1−γ)​V(0)​(t,w,x)|+O​(λ3).\Big|\frac{V^{(\lambda)}(t,w,x)-V^{(0)}(t,w,x)}{V^{(0)}(t,w,x)}\Big|=\lambda^{2}|\phi^{(2)}(t,x)|\cdot\Big|1+\frac{1}{(1-\gamma)V^{(0)}(t,w,x)}\Big|+O(\lambda^{3}). |  |

Finally, the equivalent relative wealth loss is

|  |  |  |
| --- | --- | --- |
|  | Δ​(t,x)=−λ2​ϕ(2)​(t,x)1−γ+O​(λ3).\Delta(t,x)=-\frac{\lambda^{2}\phi^{(2)}(t,x)}{1-\gamma}+O(\lambda^{3}). |  |

###### Proof 3.6

Proof.
Theorem [3.1](https://arxiv.org/html/2602.13544v1#S3.Thmtheorem1 "Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis") along with Lemma [3.3](https://arxiv.org/html/2602.13544v1#S3.Thmtheorem3 "Lemma 3.3 ‣ 3.3 An Asymptotic Analysis on 𝜆 ‣ 3 Theoretical Analysis") imply that the mean of the optimal randomized policy is expanded as

|  |  |  |  |
| --- | --- | --- | --- |
|  | a(λ)​(t,x):=\displaystyle a^{(\lambda)}(t,x)= | μ​(t,x)−rγ​σ2​(t,x)+ρ​ν​(t,x)γ​σ​(t,x)​[ux(0)​(t,x)+λ​ux(1)​(t,x)+λ2​ux(2)​(t,x)+O​(λ3)]\displaystyle\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}+\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}\big[u^{(0)}\_{x}(t,x)+\lambda u^{(1)}\_{x}(t,x)+\lambda^{2}u^{(2)}\_{x}(t,x)+O(\lambda^{3})\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a∗​(t,x)+λ​ρ​ν​(t,x)γ​σ​(t,x)​ux(1)​(t,x)+λ2​ρ​ν​(t,x)γ​σ​(t,x)​ux(2)​(t,x)+O​(λ3),\displaystyle a^{\*}(t,x)+\lambda\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}^{(1)}(t,x)+\lambda^{2}\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u\_{x}^{(2)}(t,x)+O(\lambda^{3}), |  |

where a∗​(t,x)=μ​(t,x)−rγ​σ2​(t,x)+ρ​ν​(t,x)γ​σ​(t,x)​ux(0)​(t,x)a^{\*}(t,x)=\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}+\frac{\rho\nu(t,x)}{\gamma\sigma(t,x)}u^{(0)}\_{x}(t,x) is the optimal policy for the classical case.

Recall that V(λ)V^{(\lambda)} is the value function of the classical problem under the deterministic policy a(λ)a^{(\lambda)}. By the Feynman-Kac formula, V(λ)V^{(\lambda)} satisfies the PDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt(λ)+\displaystyle V^{(\lambda)}\_{t}+ | (r+(μ​(t,x)−r)​aλ​(t,x))​w​Vw(λ)+12​σ2​(t,x)​aλ2​(t,x)​w2​Vw​w(λ)\displaystyle\Big(r+\big(\mu(t,x)-r\big)a^{\lambda}(t,x)\Big)wV^{(\lambda)}\_{w}+\frac{1}{2}\sigma^{2}(t,x){a^{\lambda}}^{2}(t,x)w^{2}V^{(\lambda)}\_{ww} |  | (26) |
|  |  | +m​(t,x)​Vx(λ)+12​ν2​(t,x)​Vx​x(λ)+ρ​ν​(t,x)​σ​(t,x)​a(λ)​(t,x)​w​Vw​x(λ)=β​V(λ),\displaystyle+m(t,x)V^{(\lambda)}\_{x}+\frac{1}{2}\nu^{2}(t,x)V^{(\lambda)}\_{xx}+\rho\nu(t,x)\sigma(t,x)a^{(\lambda)}(t,x)wV^{(\lambda)}\_{wx}=\beta V^{(\lambda)}, |  |

with the terminal condition V(λ)​(T,w,x)=U​(w)=w1−γ−11−γV^{(\lambda)}(T,w,x)=U(w)=\frac{w^{1-\gamma}-1}{1-\gamma}. Conjecturing V(λ)​(t,w,x)=w1−γ−11−γ​exp⁡{ψ(λ)​(t,x)}+φ(λ)​(t,x)V^{(\lambda)}(t,w,x)=\frac{w^{1-\gamma}-1}{1-\gamma}\exp\{\psi^{(\lambda)}(t,x)\}+\varphi^{(\lambda)}(t,x) and putting it to ([26](https://arxiv.org/html/2602.13544v1#S3.E26 "In Proof 3.6 ‣ 3.3 An Asymptotic Analysis on 𝜆 ‣ 3 Theoretical Analysis")), we obtain −11−γ​exp⁡{ψ(λ)​(t,x)}+φ(λ)​(t,x)=−e−β​(T−t)1−γ-\frac{1}{1-\gamma}\exp\{\psi^{(\lambda)}(t,x)\}+\varphi^{(\lambda)}(t,x)=-\frac{e^{-\beta(T-t)}}{1-\gamma}, where ψ(λ)\psi^{(\lambda)} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψt(λ)\displaystyle\psi^{(\lambda)}\_{t} | +m​(t,x)​ψx(λ)+12​ν2​(t,x)​(ψx​x(λ)+ψx(λ)2)+(1−γ)​ρ​ν​(t,x)​σ​(t,x)​a(λ)​(t,x)​ψx(λ)\displaystyle+m(t,x)\psi^{(\lambda)}\_{x}+\frac{1}{2}\nu^{2}(t,x)(\psi^{(\lambda)}\_{xx}+{\psi^{(\lambda)}\_{x}}^{2})+(1-\gamma)\rho\nu(t,x)\sigma(t,x)a^{(\lambda)}(t,x)\psi^{(\lambda)}\_{x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[(1−γ)​r−β]+(1−γ)​[(μ​(t,x)−r)​a(λ)​(t,x)−γ2​σ2​(t,x)​a(λ)2​(t,x)]=0,ψ(λ)​(T,x)=0.\displaystyle+[(1-\gamma)r-\beta]+(1-\gamma)\big[(\mu(t,x)-r)a^{(\lambda)}(t,x)-\frac{\gamma}{2}\sigma^{2}(t,x){a^{(\lambda)}}^{2}(t,x)\big]=0,\ \psi^{(\lambda)}(T,x)=0. |  |

However, when λ=0\lambda=0, ψ(0)=u(0)\psi^{(0)}=u^{(0)}, which motivates us to expand ψ(λ)=u(0)+λ​ϕ(1)+λ2​ϕ(2)+O​(λ3)\psi^{(\lambda)}=u^{(0)}+\lambda\phi^{(1)}+\lambda^{2}\phi^{(2)}+O(\lambda^{3}). Substituting this to the above equation, we deduce that ϕ(1)\phi^{(1)} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt(1)\displaystyle\phi^{(1)}\_{t} | +m​(t,x)​ϕx(1)+12​ν2​(t,x)​(ϕx​x(1)+2​ux(0)​ϕx(1))\displaystyle+m(t,x)\phi^{(1)}\_{x}+\frac{1}{2}\nu^{2}(t,x)(\phi^{(1)}\_{xx}+2u^{(0)}\_{x}\phi^{(1)}\_{x}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−γ)​ρ​ν​(t,x)γ​σ​(t,x)​[μ​(t,x)−r+ρ​ν​(t,x)​σ​(t,x)​ux(0)]​ϕx(1)=0,ϕ(1)​(T,x)=0.\displaystyle+\frac{(1-\gamma)\rho\nu(t,x)}{\gamma\sigma(t,x)}\big[\mu(t,x)-r+\rho\nu(t,x)\sigma(t,x)u^{(0)}\_{x}\big]\phi^{(1)}\_{x}=0,\ \phi^{(1)}(T,x)=0. |  |

Because ϕ(1)≡0\phi^{(1)}\equiv 0 is a solution to this linear PDE, it can be easily checked that ([24](https://arxiv.org/html/2602.13544v1#S3.E24 "In 3.3 An Asymptotic Analysis on 𝜆 ‣ 3 Theoretical Analysis")) is the equation satisfied by ϕ(2)\phi^{(2)}. The proof is complete.
∎

Even though the policy bias is of order O​(λ)O(\lambda), both the relative utility loss and the equivalent relative wealth loss are of order O​(λ2)O(\lambda^{2}). So
financial and utility losses due to preference for randomization are of higher order of the policy deviation.

## 4 Conclusions

This paper aims to address the prevalent appetite for randomization in a dynamic setting of Merton’s problem. We introduce the RPU with entropy functions to represent the preference for stochastic choices, and prove that the optimal policy is Gaussian in a general Markovian incomplete market with CRRA bequest utility. The mean of the Gaussian policy generally differs from the classical Merton solution due to intertemporal hedging demand. An asymptotic expansion in temperature quantifies the deviation of the optimal mean from the classical benchmark and the associated wealth loss as the financial cost of the preference for randomization.

This work opens the gate to several directions of interesting future research. For example, dynamic and recursive preference for randomization calls for more solid micro-economics underpinning. This includes, among others, extending the current framework to include consumption which would allow a reexamination of RPU, and conducting empirical analysis that could help quantify the preference for randomization and assess whether RPU can better explain asset pricing and consumption patterns. It is also interesting to investigate the model-free, RL setting of the current problem, where randomization is out of both necessity (for exploration) and pleasure (for additional utility). In such a setting, how to distinguish and disentangle these two and how do they interact? Along a different line, for Barberis’ model of optimal exit from casino gambling (Barberis, [2012](https://arxiv.org/html/2602.13544v1#bib.bib4)) featuring Kahneman and Tversky’s cumulative prospective theory (CPT), He et al. ([2017](https://arxiv.org/html/2602.13544v1#bib.bib24)) and Hu et al. ([2023](https://arxiv.org/html/2602.13544v1#bib.bib28)) show that allowing randomized strategies strictly improves the optimal CPT value and they attribute this to the non-concavity of the S-shaped utility function in CPT. This suggests that preference for randomization may be implicitly captured by certain non-concave preferences without having to add explicitly a perturbed utility. Technically, it would be valuable to inquire the impact of alternative perturbed functions such as the Tsallis or Rényi entropy and/or alterative bequest utility functions beyond CRRA/CARA, as well as to study RPU for general stochastic control problems.

## Acknowledgments

Dai acknowledges the support of Hong Kong GRF (15213422 & 15217123), The Hong Kong Polytechnic University Research Grants (P0039114, P0042456, P0042708, and P0045342), and the National Natural Science Foundation of China (72432005). Dong is supported by the National Natural Science Foundation of China (12071333 & 12101458). Jia acknowledges the support of The Chinese University of Hong Kong start-up grant. Zhou is supported by a start-up grant and the Nie Center for Intelligent Asset Management at Columbia University. His work is also part of a Columbia-CityU/HK collaborative project that is supported by the InnoHK Initiative, The Government of the HKSAR, and the AIFT Lab.

## References

* Agranov and Ortoleva (2017)

  Agranov M, Ortoleva P (2017) Stochastic choice and preferences for
  randomization. *Journal of Political Economy* 125(1):40–68.
* Agranov and Ortoleva (2025)

  Agranov M, Ortoleva P (2025) Ranges of randomization. *Review of Economics
  and Statistics* 1–12.
* Anderson et al. (1992)

  Anderson SP, De Palma A, Thisse JF (1992) *Discrete Choice Theory of
  Product Differentiation* (MIT press).
* Barberis (2012)

  Barberis N (2012) A model of casino gambling. *Management Science*
  58(1):35–51.
* Bender and Thuan (2026)

  Bender C, Thuan NT (2026) Continuous time reinforcement learning: a random
  measure approach. *Stochastic Processes and their Applications,
  forthcoming* .
* Bergman (1985)

  Bergman YZ (1985) Time preference and capital asset pricing models.
  *Journal of Financial Economics* 14(1):145–159.
* Berry (1994)

  Berry ST (1994) Estimating discrete-choice models of product differentiation.
  *The RAND Journal of Economics* 242–262.
* Ceballos-Lira et al. (2010)

  Ceballos-Lira MJ, Macias-Diaz JE, Villa J (2010) A generalization of Osgood’s
  test and a comparison criterion for integral equations with noise.
  *arXiv preprint arXiv:1012.1843* .
* Chacko and Viceira (2005)

  Chacko G, Viceira LM (2005) Dynamic consumption and portfolio choice with
  stochastic volatility in incomplete markets. *The Review of Financial
  Studies* 18(4):1369–1402.
* Dai et al. (2023)

  Dai M, Dong Y, Jia Y (2023) Learning equilibrium mean-variance strategy.
  *Mathematical Finance* 33(4):1166–1212.
* Dai et al. (2025a)

  Dai M, Dong Y, Jia Y, Zhou XY (2025a) Data-driven Merton’s
  strategies via policy randomization. *arXiv preprint arXiv:2312.11797* .
* Dai et al. (2021)

  Dai M, Jin H, Kou S, Xu Y (2021) A dynamic mean-variance analysis for log
  returns. *Management Science* 67(2):1093–1108.
* Dai et al. (2025b)

  Dai M, Sun Y, Xu ZQ, Zhou XY (2025b) Learning to optimally stop
  diffusion processes, with financial applications. *Management Science,
  forthcoming* .
* Dianetti et al. (2025)

  Dianetti J, Dumitrescu R, Ferrari G, Xu R (2025) Entropy regularization in
  mean-field games of optimal stopping. *arXiv preprint arXiv:2509.18821*
  .
* Duffie and Epstein (1992)

  Duffie D, Epstein LG (1992) Stochastic differential utility.
  *Econometrica* 353–394.
* Dwenger et al. (2018)

  Dwenger N, Kübler D, Weizsäcker G (2018) Flipping a coin: Evidence from
  university applications. *Journal of Public Economics* 167:240–250.
* El Karoui et al. (1997)

  El Karoui N, Peng S, Quenez MC (1997) Backward stochastic differential
  equations in finance. *Mathematical Finance* 7(1):1–71.
* Epstein and Zin (1989)

  Epstein LG, Zin SE (1989) Substitution, risk aversion, and the temporal
  behavior of consumption and asset returns: A theoretical framework.
  *Econometrica* 57(4):937–969.
* Feng et al. (2017)

  Feng G, Li X, Wang Z (2017) On the relation between several discrete choice
  models. *Operations Research* 65(6):1516–1525.
* Fudenberg et al. (2015)

  Fudenberg D, Iijima R, Strzalecki T (2015) Stochastic choice and revealed
  perturbed utility. *Econometrica* 83(6):2371–2409.
* Guo et al. (2022)

  Guo X, Xu R, Zariphopoulou T (2022) Entropy regularization for mean field games
  with learning. *Mathematics of Operations Research* 47(4):3239–3260.
* Haarnoja et al. (2018)

  Haarnoja T, Zhou A, Abbeel P, Levine S (2018) Soft actor-critic: Off-policy
  maximum entropy deep reinforcement learning with a stochastic actor.
  *International Conference on Machine Learning*, 1861–1870 (PMLR).
* Han et al. (2023)

  Han X, Wang R, Zhou XY (2023) Choquet regularization for continuous-time
  reinforcement learning. *SIAM Journal on Control and Optimization*
  61(5):2777–2801.
* He et al. (2017)

  He XD, Hu S, Obłój J, Zhou XY (2017) Path-dependent and randomized
  strategies in barberis’ casino gambling model. *Operations Research*
  65(1):97–103.
* Hey and Carbone (1995)

  Hey JD, Carbone E (1995) Stochastic choice with deterministic preferences: An
  experimental investigation. *Economics Letters* 47(2):161–167.
* Hotz and Miller (1993)

  Hotz VJ, Miller RA (1993) Conditional choice probabilities and the estimation
  of dynamic models. *The Review of Economic Studies* 60(3):497–529.
* Hotz et al. (1994)

  Hotz VJ, Miller RA, Sanders S, Smith J (1994) A simulation estimator for
  dynamic models of discrete choice. *The Review of Economic Studies*
  61(2):265–289.
* Hu et al. (2023)

  Hu S, Obłój J, Zhou XY (2023) A casino gambling model under cumulative
  prospect theory: analysis and algorithm. *Management Science*
  69(4):2474–2496.
* Hu et al. (2005)

  Hu Y, Imkeller P, Müller M, et al. (2005) Utility maximization in
  incomplete markets. *The Annals of Applied Probability*
  15(3):1691–1712.
* Huang et al. (2025)

  Huang Y, Jia Y, Zhou XY (2025) Mean–variance portfolio selection by
  continuous-time reinforcement learning: Algorithms, regret analysis, and
  empirical study. *arXiv preprint arXiv:2412.16175* .
* Jia (2024)

  Jia Y (2024) Continuous-time risk-sensitive reinforcement learning via
  quadratic variation penalty. *arXiv preprint arXiv:2404.12598* .
* Jia et al. (2026)

  Jia Y, Ouyang D, Zhang Y (2026) Accuracy of discretely sampled stochastic
  policies in continuous-time reinforcement learning. *SIAM Journal on
  Control and Optimization, forthcoming* .
* Kydland and Prescott (1982)

  Kydland FE, Prescott EC (1982) Time to build and aggregate fluctuations.
  *Econometrica* 1345–1370.
* Liu (2007)

  Liu J (2007) Portfolio selection in stochastic environments. *The Review
  of Financial Studies* 20(1):1–39.
* Luce et al. (1959)

  Luce RD, et al. (1959) *Individual Choice Behavior*, volume 4 (Wiley New
  York).
* Machina (1985)

  Machina MJ (1985) Stochastic choice functions generated from deterministic
  preferences over lotteries. *The Economic Journal* 95(379):575–594.
* Mattsson and Weibull (2002)

  Mattsson LG, Weibull JW (2002) Probabilistic choice and procedurally bounded
  rationality. *Games and Economic Behavior* 41(1):61–78.
* McFadden (1974)

  McFadden D (1974) The measurement of urban travel demand. *Journal of
  Public Economics* 3(4):303–328.
* McFadden (2001)

  McFadden D (2001) Economic choices. *American Economic Review*
  91(3):351–378.
* Merton (1969)

  Merton RC (1969) Lifetime portfolio selection under uncertainty: The
  continuous-time case. *The Review of Economics and Statistics* 247–257.
* Miao and Zhong (2018)

  Miao B, Zhong S (2018) Probabilistic social preference: how Machina’s mom
  randomizes her choice. *Economic Theory* 65(1):1–24.
* Permana (2020)

  Permana Y (2020) Why do people prefer randomisation? an experimental
  investigation. *Theory and Decision* 88(1):73–96.
* Tang et al. (2022)

  Tang W, Zhang YP, Zhou XY (2022) Exploratory HJB equations and their
  convergence. *SIAM Journal on Control and Optimization*
  60(6):3191–3216.
* Uzawa (1968)

  Uzawa H (1968) Time preference, the consumption function, and optimum asset
  holdings. *Value, capital and growth: Papers in honor of Sir John
  Hicks*, 485–504 (The University of Edinburgh Press, Edinburgh).
* Wachter (2002)

  Wachter JA (2002) Portfolio and consumption decisions under mean-reverting
  returns: An exact solution for complete markets. *Journal of Financial
  and Quantitative Analysis* 37(1):63–91.
* Wang et al. (2023)

  Wang B, Gao X, Li L (2023) Reinforcement learning for continuous-time optimal
  execution: actor-critic algorithm and error analysis. *Available at
  SSRN* .
* Wang et al. (2020)

  Wang H, Zariphopoulou T, Zhou XY (2020) Reinforcement learning in continuous
  time and space: A stochastic control approach. *Journal of Machine
  Learning Research* 21(198):1–34.
* Wang and Zhou (2020)

  Wang H, Zhou XY (2020) Continuous-time mean–variance portfolio selection: A
  reinforcement learning framework. *Mathematical Finance*
  30(4):1273–1308.
* Zhao et al. (2019)

  Zhao R, Sun X, Tresp V (2019) Maximum entropy-regularized multi-goal
  reinforcement learning. *International Conference on Machine Learning*,
  7553–7562 (PMLR).
* Ziebart et al. (2008)

  Ziebart BD, Maas AL, Bagnell JA, Dey AK (2008) Maximum entropy inverse
  reinforcement learning. *AAAI*, volume 8, 1433–1438 (Chicago, IL, USA).

{APPENDICES}

## 5 Different Temperature Schemes

In this section we discuss two alternative temperature schemes for weighing the entropy utility, and explain the drawbacks of these formulations compared with our recursive formulation.

### 5.1 Constant Temperature

With the exploratory dynamics given in ([5](https://arxiv.org/html/2602.13544v1#S2.E5 "In 2.2 Preference for Randomization ‣ 2 Problem Formulation")), if we were to use a constant temperature as in Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)) with the objective function

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫tTλ​ℋ​(𝝅s)​ds+U​(WT𝝅)|Wt𝝅=w,Xt=x],\mathbb{E}\left[\int\_{t}^{T}\lambda\mathcal{H}(\boldsymbol{\pi}\_{s})\mathrm{d}s+U(W\_{T}^{\boldsymbol{\boldsymbol{\pi}}})\Big|W\_{t}^{\boldsymbol{\pi}}=w,X\_{t}=x\right], |  |

then the associated HJB equation would be

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∂V∂t+sup𝝅{(r+(μ(t,x)−r)Mean(𝝅))wVw+12σ2(t,x)(Mean(𝝅)2+Var(𝝅))w2Vw​w\displaystyle\frac{\partial V}{\partial t}+\sup\_{\boldsymbol{\pi}}\Bigg\{\Big(r+\big(\mu(t,x)-r\big)\operatorname{Mean}(\boldsymbol{\pi})\Big)wV\_{w}+\frac{1}{2}\sigma^{2}(t,x)\Big(\operatorname{Mean}(\boldsymbol{\pi})^{2}+\operatorname{Var}(\boldsymbol{\pi})\Big)w^{2}V\_{ww} |  | (27) |
|  |  | +m(t,x)Vx+12ν2(t,x)Vx​x+ρν(t,x)σ(t,x)Mean(𝝅)wVw​x+λℋ(𝝅)}=0,\displaystyle+m(t,x)V\_{x}+\frac{1}{2}\nu^{2}(t,x)V\_{xx}+\rho\nu(t,x)\sigma(t,x)\operatorname{Mean}(\boldsymbol{\pi})wV\_{wx}+\lambda\mathcal{H}(\boldsymbol{\pi})\Bigg\}=0, |  |

with the terminal condition V​(T,w,x)=U​(w)=w1−γ−11−γV(T,w,x)=U(w)=\frac{w^{1-\gamma}-1}{1-\gamma}.

Similar to Wang et al. ([2020](https://arxiv.org/html/2602.13544v1#bib.bib47)), we can solve the maximization problem on the left-hand side of ([27](https://arxiv.org/html/2602.13544v1#S5.E27 "In 5.1 Constant Temperature ‣ 5 Different Temperature Schemes")) and apply the verification theorem to conclude that the optimal policy is a normal distribution with mean

|  |  |  |
| --- | --- | --- |
|  | (μ​(t,x)−r)​Vw−σ2​(t,x)​w​Vw​w+ρ​ν​(t,x)​Vw​x−σ​(t,x)​w​Vw​w,\frac{\big(\mu(t,x)-r\big)V\_{w}}{-\sigma^{2}(t,x)wV\_{ww}}+\frac{\rho\nu(t,x)V\_{wx}}{-\sigma(t,x)wV\_{ww}}, |  |

and variance

|  |  |  |
| --- | --- | --- |
|  | λ−σ2​(t,x)​w2​Vw​w.\frac{\lambda}{-\sigma^{2}(t,x)w^{2}V\_{ww}}. |  |

Plugging the above into ([27](https://arxiv.org/html/2602.13544v1#S5.E27 "In 5.1 Constant Temperature ‣ 5 Different Temperature Schemes")), the equation becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∂V∂t+r​w​Vw+m​(t,x)​Vx+12​ν2​(t,x)​Vx​x+λ2​log⁡2​π\displaystyle\frac{\partial V}{\partial t}+rwV\_{w}+m(t,x)V\_{x}+\frac{1}{2}\nu^{2}(t,x)V\_{xx}+\frac{\lambda}{2}\log 2\pi |  | (28) |
|  |  | −((μ​(t,x)−r)​Vw+ρ​ν​(t,x)​σ​(t,x)​Vw​x)22​σ2​(t,x)​Vw​w+λ2​log⁡λ−σ2​(t,x)​w2​Vw​w=0.\displaystyle-\frac{\bigg(\big(\mu(t,x)-r\big)V\_{w}+\rho\nu(t,x)\sigma(t,x)V\_{wx}\bigg)^{2}}{2\sigma^{2}(t,x)V\_{ww}}+\frac{\lambda}{2}\log\frac{\lambda}{-\sigma^{2}(t,x)w^{2}V\_{ww}}=0. |  |

To our best knowledge, this PDE generally admits neither a separable nor a closed-form solution due to a lack of the homothetic property. As a result, analytical forms of the optimal value function and optimal policy are both unavailable, making it hard to carry out further theoretical analysis such as a comparative study and sensitivity analysis.

### 5.2 Wealth-Dependent Temperature

In order to obtain a simpler HJB equation, we could consider a wealth-dependent temperature parameter. For example, for CRRA utility, we could take λ​(t,w,x)=λ​w1−γ\lambda(t,w,x)=\lambda w^{1-\gamma} where γ≠1\gamma\neq 1. The derivations of ([27](https://arxiv.org/html/2602.13544v1#S5.E27 "In 5.1 Constant Temperature ‣ 5 Different Temperature Schemes")) and ([28](https://arxiv.org/html/2602.13544v1#S5.E28 "In 5.1 Constant Temperature ‣ 5 Different Temperature Schemes")) are similar by replacing λ\lambda with λ​w1−γ\lambda w^{1-\gamma}. With this wealth-dependent weighting scheme, the problem becomes homothetic in wealth with degree 1−γ1-\gamma; hence the value function admits the form V​(t,w,x)=w1−γ​v​(t,x)1−γ+g​(t)V(t,w,x)=\frac{w^{1-\gamma}v(t,x)}{1-\gamma}+g(t), where gg and vv satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (1−γ)​g′−(1−γ)​g=∂v∂t+m​vx+ν22​vx​x,g​(T,x)=−11−γ,\displaystyle(1-\gamma)g^{\prime}-(1-\gamma)g=\frac{\partial v}{\partial t}+mv\_{x}+\frac{\nu^{2}}{2}v\_{xx},\ g(T,x)=-\frac{1}{1-\gamma}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂v∂t+(1−γ)​r​v+m​vx+ν22​vx​x+λ​1−γ2​log⁡2​πγ​σ2​v+(1−γ)​((μ−r)​v+ρ​ν​σ​vx)22​γ​σ2​v,v​(T,x)=1.\displaystyle\frac{\partial v}{\partial t}+(1-\gamma)rv+mv\_{x}+\frac{\nu^{2}}{2}v\_{xx}+\lambda\frac{1-\gamma}{2}\log\frac{2\pi}{\gamma\sigma^{2}v}+\frac{(1-\gamma)\big((\mu-r)v+\rho\nu\sigma v\_{x}\big)^{2}}{2\gamma\sigma^{2}v},\ v(T,x)=1. |  |

Consequently, the optimal policy is a normal distribution with mean μ​(t,x)−rγ​σ2​(t,x)+ρ​ν​(t,x)​vx​(t,x)γ​σ​(t,x)​v​(t,x)\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}+\frac{\rho\nu(t,x)v\_{x}(t,x)}{\gamma\sigma(t,x)v(t,x)} and variance λγ​σ2​(t,x)​v​(t,x)\frac{\lambda}{\gamma\sigma^{2}(t,x)v(t,x)}.

The major difference between this formulation and the recursive one is that there is an extra term v​(t,x)v(t,x) in the denominator of the optimal variance of the former, which may result in an arbitrarily large randomization variance within a finite time period and consequently the non-existence of an optimal policy. For example, in the Black-Scholes case (m,ν≡0m,\nu\equiv 0), vv is independent of xx and satisfies an ODE whose solution will reach 0 with some choice of the coefficients. Specifically, v​(t)=φ​(T−t)v(t)=\varphi(T-t), where φ\varphi satisfies an ODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ′​(τ)=(1−γ)​((r+(μ−r)22​γ​σ2)​φ​(τ)+λ2​log⁡2​π​λγ​σ2−λ2​log⁡φ​(τ)),φ​(0)=1.\varphi^{\prime}(\tau)=(1-\gamma)\Big((r+\frac{(\mu-r)^{2}}{2\gamma\sigma^{2}})\varphi(\tau)+\frac{\lambda}{2}\log\frac{2\pi\lambda}{\gamma\sigma^{2}}-\frac{\lambda}{2}\log\varphi(\tau)\Big),\ \varphi(0)=1. |  | (29) |

We have the following theorem.

###### Theorem 5.1

If γ>1\gamma>1 and r+(μ−r)22​γ​σ2+λ2​log⁡2​π​λγ​σ2<0r+\frac{(\mu-r)^{2}}{2\gamma\sigma^{2}}+\frac{\lambda}{2}\log\frac{2\pi\lambda}{\gamma\sigma^{2}}<0, then the solution to ([29](https://arxiv.org/html/2602.13544v1#S5.E29 "In 5.2 Wealth-Dependent Temperature ‣ 5 Different Temperature Schemes")) reaches 0 in a finite time.

###### Proof 5.2

Proof.
Consider an ODE y′=F​(y)y^{\prime}=F(y) with the initial condition y​(0)=1y(0)=1, where F​(x)=a​x+b−c​log⁡xF(x)=ax+b-c\log x with some constants a,ba,b and cc. Let y​(τ)=e−z​(τ)y(\tau)=e^{-z(\tau)}. Then zz satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | z′=−ez​F​(e−z)=−a−b​ez−c​z​ez,z​(0)=0.z^{\prime}=-e^{z}F(e^{-z})=-a-be^{z}-cze^{z},\ z(0)=0. |  | (30) |

If F​(x)<0F(x)<0 for any x∈(0,1]x\in(0,1] or zz is increasing, then applying the Osgood test (c.f., Ceballos-Lira et al. [2010](https://arxiv.org/html/2602.13544v1#bib.bib8)) we conclude that the solution of ([30](https://arxiv.org/html/2602.13544v1#S5.E30 "In Proof 5.2 ‣ 5.2 Wealth-Dependent Temperature ‣ 5 Different Temperature Schemes")) explodes at time τe=−∫0∞1a+b​ez+c​z​ez​dz\tau\_{e}=-\int\_{0}^{\infty}\frac{1}{a+be^{z}+cze^{z}}\mathrm{d}z.
The desired result now follows from the fact that y→0y\to 0 is equivalent to z→∞z\to\infty.
∎

## 6 CARA Utility

The RPU also works for the CARA utility, for which we use the dollar amount invested in the risky asset as the control (portfolio) variable, and denote by 𝝅\boldsymbol{\pi} the corresponding probability-density-valued control. The wealth process under 𝝅\boldsymbol{\pi} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Wt𝝅=[r​Wt𝝅+(μ​(t,Xt)−r)​Mean⁡(𝝅t)]​d​t+σ​(t,Xt)​[Mean⁡(𝝅t)​d​Bt+Var⁡(𝝅t)​d​B¯t].\mathrm{d}W^{\boldsymbol{\pi}}\_{t}=\left[rW^{\boldsymbol{\pi}}\_{t}+(\mu(t,X\_{t})-r)\operatorname{Mean}(\boldsymbol{\pi}\_{t})\right]\mathrm{d}t+\sigma(t,X\_{t})\left[\operatorname{Mean}(\boldsymbol{\pi}\_{t})\mathrm{d}B\_{t}+\sqrt{\operatorname{Var}(\boldsymbol{\pi}\_{t})}\mathrm{d}\bar{B}\_{t}\right]. |  | (31) |

Consider the following regularized objective function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt𝝅:=𝔼​[∫tT−λ​Js𝝅​ℋ​(𝝅s)​d​s+U​(WT𝝅)|ℱt],J^{\boldsymbol{\pi}}\_{t}:=\mathbb{E}\left[\int\_{t}^{T}-\lambda J\_{s}^{\boldsymbol{\pi}}\mathcal{H}(\boldsymbol{\pi}\_{s})\mathrm{d}s+U(W\_{T}^{\boldsymbol{\pi}})\Big|\mathcal{F}\_{t}\right], |  | (32) |

where U​(x)=−1γ​e−γ​xU(x)=-\frac{1}{\gamma}e^{-\gamma x}. Under this recursive weighting scheme, the optimal policy is given by

|  |  |  |
| --- | --- | --- |
|  | 𝝅∗​(t,x)=𝒩​((μ​(t,x)−rγ​σ2​(t,x)−ρ​ν​(t,x)σ​(t,x)​ux​(t,x))​e−r​(T−t),λγ2​σ2​(t,x)​e−2​r​(T−t)),\boldsymbol{\pi}^{\*}(t,x)=\mathcal{N}\bigg(\big(\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}-\frac{\rho\nu(t,x)}{\sigma(t,x)}u\_{x}(t,x)\big)e^{-r(T-t)},\frac{\lambda}{\gamma^{2}\sigma^{2}(t,x)}e^{-2r(T-t)}\bigg), |  |

where uu satisfies

|  |  |  |
| --- | --- | --- |
|  | ut+m​(t,x)​ux+12​ν2​(t,x)​(−γ​ux2+ux​x)+γ​σ2​(t,x)2​(μ​(t,x)−rγ​σ2​(t,x)−ρ​ν​(t,x)σ​(t,x)​ux)2\displaystyle u\_{t}+m(t,x)u\_{x}+\frac{1}{2}\nu^{2}(t,x)(-\gamma u\_{x}^{2}+u\_{xx})+\frac{\gamma\sigma^{2}(t,x)}{2}\left(\frac{\mu(t,x)-r}{\gamma\sigma^{2}(t,x)}-\frac{\rho\nu(t,x)}{\sigma(t,x)}u\_{x}\right)^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | +λ2​γ​log⁡2​π​λγ2​σ2​(t,x)​e2​r​(T−t)=0,u​(T,x)=0,\displaystyle+\frac{\lambda}{2\gamma}\log\frac{2\pi\lambda}{\gamma^{2}\sigma^{2}(t,x)e^{2r(T-t)}}=0,\ \ \ u(T,x)=0, |  |

and the associated optimal value function is V​(t,w,x)=−1γ​exp⁡(−γ​u​(t,x)−γ​er​(T−t)​w)V(t,w,x)=-\frac{1}{\gamma}\exp(-\gamma u(t,x)-\gamma e^{r(T-t)}w). Hence we can develop a theory parallel to the CRRA utility. Details are left to the interested readers.

## 7 A BSDE Perspective

The optimal portfolio processes with parameter λ\lambda in the RPU problem can also be characterized by a BSDE.

###### Theorem 7.1

Suppose the following quadratic BSDE admits a unique solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Yt∗(λ)=−{(1−γ)​[λ2​log⁡2​π​λγ​σt2+r+(μt−r+ρ​σt​Zt∗(λ))22​γ​σt2]+12​Zt∗(λ)2}​d​t+Zt∗(λ)​d​BtX,YT∗(λ)=0.\left\{\begin{aligned} \mathrm{d}Y\_{t}^{\*(\lambda)}=&-\Bigg\{(1-\gamma)\Big[\frac{\lambda}{2}\log\frac{2\pi\lambda}{\gamma\sigma\_{t}^{2}}+r+\frac{(\mu\_{t}-r+\rho\sigma\_{t}Z^{\*(\lambda)}\_{t})^{2}}{2\gamma\sigma\_{t}^{2}}\Big]+\frac{1}{2}{Z\_{t}^{\*(\lambda)}}^{2}\Bigg\}\mathrm{d}t+Z\_{t}^{\*(\lambda)}\mathrm{d}B\_{t}^{X},\\ Y^{\*(\lambda)}\_{T}=&0.\end{aligned}\right. |  | (33) |

Then the optimal randomized control is given by

|  |  |  |
| --- | --- | --- |
|  | 𝝅t∗(λ)=𝒩​(μt−r+ρ​σt​Zt∗(λ)γ​σt2,λγ​σt2).\boldsymbol{\pi}^{\*(\lambda)}\_{t}=\mathcal{N}\Big(\frac{\mu\_{t}-r+\rho\sigma\_{t}Z^{\*(\lambda)}\_{t}}{\gamma\sigma^{2}\_{t}},\frac{\lambda}{\gamma\sigma\_{t}^{2}}\Big). |  |

The solution to BSDE ([33](https://arxiv.org/html/2602.13544v1#S7.E33 "In Theorem 7.1 ‣ 7 A BSDE Perspective")) corresponds to the PDE ([15](https://arxiv.org/html/2602.13544v1#S3.E15 "In Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis")) in Theorem [3.1](https://arxiv.org/html/2602.13544v1#S3.Thmtheorem1 "Theorem 3.1 ‣ 3.1 Gaussian Randomization ‣ 3 Theoretical Analysis").
The process Y∗(λ)Y^{\*(\lambda)} can be interpreted as an auxiliary process in the martingale duality theory, which stipulates that

|  |  |  |
| --- | --- | --- |
|  | (Vt𝝅+∫0tλ​ℋ​(𝝅s)​[(1−γ)​Vs𝝅+1]​ds)​eYt∗(λ)\left(V^{\boldsymbol{\pi}}\_{t}+\int\_{0}^{t}\lambda\mathcal{H}(\boldsymbol{\pi}\_{s})\big[(1-\gamma)V^{\boldsymbol{\pi}}\_{s}+1\big]\mathrm{d}s\right)e^{Y\_{t}^{\*(\lambda)}} |  |

is a supermartingale for any portfolio control 𝝅t\boldsymbol{\pi}\_{t} and a martingale when 𝝅t=𝝅t∗(λ)\boldsymbol{\pi}\_{t}=\boldsymbol{\pi}^{\*(\lambda)}\_{t}, where Vt𝝅=wt𝝅1−γ1−γ​eYt∗(λ)−11−γV^{\boldsymbol{\pi}}\_{t}=\frac{{w\_{t}^{\boldsymbol{\pi}}}^{1-\gamma}}{1-\gamma}e^{Y\_{t}^{\*(\lambda)}}-\frac{1}{1-\gamma} is the value function evaluated along the optimal wealth trajectories. Moreover,
when λ=0\lambda=0, the above result reduces to the classical one which was first derived by Hu et al. ([2005](https://arxiv.org/html/2602.13544v1#bib.bib29)).

The BSDE ([33](https://arxiv.org/html/2602.13544v1#S7.E33 "In Theorem 7.1 ‣ 7 A BSDE Perspective")) offers important insights about the connection between the classical problem (λ=0\lambda=0) and the RPU (λ>0\lambda>0), some of them consistent with the unbiasedness discussion in Subsection [3.2](https://arxiv.org/html/2602.13544v1#S3.SS2 "3.2 When is the Optimal Randomized Policy Unbiased? ‣ 3 Theoretical Analysis"). First, the only difference between the two problems is the extra term, (1−γ)​λ2​log⁡2​π​λγ​σt2\frac{(1-\gamma)\lambda}{2}\log\frac{2\pi\lambda}{\gamma\sigma\_{t}^{2}}, in the driver of ([33](https://arxiv.org/html/2602.13544v1#S7.E33 "In Theorem 7.1 ‣ 7 A BSDE Perspective")). This term becomes a deterministic function of tt when γ=1\gamma=1 (log-utility) or when σt\sigma\_{t} is deterministic, in which case Z∗(λ)=Z∗(0)Z^{\*(\lambda)}=Z^{\*(0)}.131313This is because, in general, if (Yt,Zt)(Y\_{t},Z\_{t}) satisfies a BSDE d​Yt=−f​(t,Xt,Zt)​d​t+Zt​d​BtX\mathrm{d}Y\_{t}=-f(t,X\_{t},Z\_{t})\mathrm{d}t+Z\_{t}\mathrm{d}B^{X}\_{t} with YT=F​(XT)Y\_{T}=F(X\_{T}), then (Yt+C​(t),Zt)(Y\_{t}+C(t),Z\_{t}) solves the BSDE d​Y~t=−[c​(t)+f​(t,Xt,Z~t)]​d​t+Z~t​d​BtX\mathrm{d}\tilde{Y}\_{t}=-\big[c(t)+f(t,X\_{t},\tilde{Z}\_{t})\big]\mathrm{d}t+\tilde{Z}\_{t}\mathrm{d}B^{X}\_{t} with Y~T=F​(XT)\tilde{Y}\_{T}=F(X\_{T}), where cc is a given deterministic function of tt and C​(t)=∫tTc​(s)​dsC(t)=\int\_{t}^{T}c(s)\mathrm{d}s. Hence Z=Z~Z=\tilde{Z} follows from the uniqueness of solution. Hence the optimal solution of the RPU problem has a mean that coincides with the classical solution, or the former is unbiased. Incidentally, this is consistent with an earlier result of Dai et al. ([2023](https://arxiv.org/html/2602.13544v1#bib.bib10)) in the mean-variance analysis for the log utility. Second, when ρ=0\rho=0, i.e., the market factors evolve independently from the stock price, the optimal randomized policy is also unbiased, even if Z∗(λ)≠Z∗(0)Z^{\*(\lambda)}\neq Z^{\*(0)} in general. This is intuitive because hedging is not necessary in this case. A special case is when the market factor XX is deterministic, in which case the source of randomness BtXB^{X}\_{t} vanishes leading to Z∗(λ)=Z∗(0)=0Z^{\*(\lambda)}=Z^{\*(0)}=0 and hence the optimal randomization is unbiased.
Otherwise, optimal policies are in general biased in stochastic volatility models when σt\sigma\_{t} is a function of the stochastic factor process XtX\_{t} and the power of the utility γ≠1\gamma\neq 1.