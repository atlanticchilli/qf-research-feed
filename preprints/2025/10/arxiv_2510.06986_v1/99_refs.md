---
authors:
- Jinho Cha
- Long Pham
- Thi Le Hoa Vo
- Jaeyoung Cho
- Jaejin Lee
doc_id: arxiv:2510.06986v1
family_id: arxiv:2510.06986
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk
  Preferences under Uncertainty'
url_abs: http://arxiv.org/abs/2510.06986v1
url_html: https://arxiv.org/html/2510.06986v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jinho Cha
Department of Computer Science, Gwinnett Technical College, Lawrenceville, GA, USA

Long Pham
Department of Decision Sciences and Economics, Texas A&M University–Corpus Christi, TX, USA

Thi Le Hoa Vo
Corresponding author: thi-le-hoa.vo@univ-rennes.fr
IGR-IAE Rennes, Université de Rennes, CREM UMR CNRS 6211, Rennes, France

Jaeyoung Cho
Department of Computer Science, Prairie View A&M University, Prairie View, TX, USA

Jaejin Lee
Intel Corporation, Chandler, AZ, USA

###### Abstract

This study develops an inverse portfolio optimization framework for recovering latent investor preferences—including risk aversion, transaction cost sensitivity, and ESG orientation—from observed portfolio allocations. Using controlled synthetic data, we assess the estimator’s statistical properties such as consistency, coverage, and dynamic regret. The model integrates robust optimization and regret-based inference to quantify welfare losses under preference misspecification and market shocks. Simulation experiments demonstrate accurate recovery of transaction cost parameters, partial identifiability of ESG penalties, and sublinear regret even under stochastic volatility and liquidity shocks. A real-data illustration using ETFs (2007–2024) confirms that transaction-cost shocks dominate volatility shocks in welfare impact. The framework thus provides a statistically rigorous and economically interpretable tool for robust preference inference and portfolio design under uncertainty.

Keywords: Inverse Optimization; Portfolio Selection; Risk Aversion; Transaction Costs; ESG Preferences; Robust Learning; Dynamic Regret

## 1 Introduction

### 1.1 Motivation

Understanding investor preferences is a fundamental challenge in finance.
Observed portfolio allocations provide only indirect evidence of underlying risk attitudes,
transaction frictions, or non-financial motives such as ESG orientation.
Traditional econometric methods often require large and noisy datasets and rely on strong parametric assumptions,
making them less effective in settings with limited or heterogeneous observations.
Moreover, as markets are increasingly subject to structural shocks—such as sudden volatility spikes or changes in transaction costs—it becomes crucial to assess how misspecification of investor preferences translates into welfare losses.
Accurately recovering such preferences is vital not only for asset managers designing tailored investment products,
but also for regulators seeking to safeguard investors in turbulent environments.

### 1.2 Research Gap

Inverse optimization has recently emerged as a powerful paradigm for recovering
latent preferences from observed decisions ([Aswani et al., 2018a,](https://arxiv.org/html/2510.06986v1#bib.bib7) ; Keshavarz et al.,, [2011](https://arxiv.org/html/2510.06986v1#bib.bib44)).
However, its application in finance remains limited.
Existing studies focus predominantly on domains such as energy systems,
supply chain logistics, and transportation ([Bertsimas et al., 2015a,](https://arxiv.org/html/2510.06986v1#bib.bib14) ; Chan et al.,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib23)),
where operational data are abundant and preferences are relatively stable.
In contrast, financial markets exhibit unique challenges:
(i) investor heterogeneity,
(ii) non-stationarity due to shocks and preference drift, and
(iii) the need for rigorous statistical guarantees—including consistency, coverage, and efficiency—to ensure reliable inference.
Current finance-oriented studies rarely address these aspects in a unified framework.

Recent methodological advances further highlight the timeliness of this research.
Ren et al., ([2025](https://arxiv.org/html/2510.06986v1#bib.bib56)) propose inverse optimization techniques based on learning feasible regions,
broadening the theoretical foundation beyond traditional parametric formulations.
On the application side, Müller, ([2025](https://arxiv.org/html/2510.06986v1#bib.bib51)) develop sustainable mean–variance portfolio models under ESG uncertainty,
underscoring the importance of incorporating non-financial motives into portfolio analysis.
Together, these works demonstrate both the methodological momentum and the practical relevance of bringing inverse optimization into finance.

### 1.3 Contribution

This paper makes three contributions:

* •

  Methodological: We propose an inverse portfolio optimization framework that jointly recovers
  risk aversion, transaction cost sensitivity, and ESG penalties from observed allocations,
  using a grid-based estimator with provable regret bounds.
* •

  Empirical validation: Using controlled synthetic data, we evaluate the statistical properties
  of the estimator, including parameter recovery accuracy, bootstrap coverage probability,
  and efficiency of inference.
* •

  Decision support under shocks: We introduce regret-based measures to quantify welfare loss
  under misspecified preferences and analyze how investor heterogeneity shapes responses
  to transaction cost and volatility shocks.

Collectively, these contributions advance the methodological toolkit for financial inverse optimization,
while providing rigorous statistical and economic validation of the proposed framework.
To the best of our knowledge, this is the first study to jointly recover multiple dimensions of investor preferences
(risk, cost, and ESG) under stochastic shocks with statistical guarantees,
delivering actionable insights for both portfolio managers and regulators.

## 2 Literature Review

### 2.1 Classical Portfolio Theory

The foundation of modern portfolio selection is the mean–variance framework
introduced by Markowitz, ([1952](https://arxiv.org/html/2510.06986v1#bib.bib49)).
In this setting, investors choose portfolio weights to maximize expected return
subject to a quadratic penalty on variance, implicitly assuming normally distributed returns
and quadratic utility.
While the Markowitz model provided a tractable and elegant theory,
its assumptions—including static preferences, absence of frictions, and reliance on variance
as the sole risk measure—limit its descriptive realism in practice
(Elton and Gruber,, [1997](https://arxiv.org/html/2510.06986v1#bib.bib31); Meucci,, [2009](https://arxiv.org/html/2510.06986v1#bib.bib50); Fabozzi et al.,, [2007](https://arxiv.org/html/2510.06986v1#bib.bib33); Lintner,, [1965](https://arxiv.org/html/2510.06986v1#bib.bib47)).

Extensions to the classical model have sought to address these shortcomings.
Alternative risk measures such as Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR)
capture tail risk more effectively (Artzner et al.,, [1999](https://arxiv.org/html/2510.06986v1#bib.bib6); Rockafellar and Uryasev,, [2000](https://arxiv.org/html/2510.06986v1#bib.bib57); Acerbi and Tasche,, [2002](https://arxiv.org/html/2510.06986v1#bib.bib1)).
More recent advances propose spectral and distortion risk measures
that incorporate investor-specific risk attitudes (Kusuoka,, [2001](https://arxiv.org/html/2510.06986v1#bib.bib46); Föllmer and Schied,, [2002](https://arxiv.org/html/2510.06986v1#bib.bib35)).
The literature also emphasizes robust portfolio optimization,
where uncertainty in mean and covariance inputs is explicitly modeled
(Ben-Tal et al.,, [2009](https://arxiv.org/html/2510.06986v1#bib.bib12); DeMiguel et al.,, [2009](https://arxiv.org/html/2510.06986v1#bib.bib26); Garlappi et al.,, [2007](https://arxiv.org/html/2510.06986v1#bib.bib36); Fabozzi et al.,, [2021](https://arxiv.org/html/2510.06986v1#bib.bib34)).
These approaches highlight the importance of accounting for estimation error and model risk,
especially in high-dimensional or turbulent markets.

Behavioral adjustments further enrich portfolio theory by incorporating investor psychology.
Prospect theory utilities (Kahneman and Tversky,, [1979](https://arxiv.org/html/2510.06986v1#bib.bib43); Tversky and Kahneman,, [1992](https://arxiv.org/html/2510.06986v1#bib.bib61)) and loss aversion penalties
(Barberis et al.,, [2001](https://arxiv.org/html/2510.06986v1#bib.bib11); Benartzi and Thaler,, [1995](https://arxiv.org/html/2510.06986v1#bib.bib13)) relax the expected utility assumption and
better capture observed trading patterns.
Recent studies extend this line of research by embedding reference dependence,
ambiguity aversion, and probability weighting into portfolio choice
(Dimmock et al.,, [2016](https://arxiv.org/html/2510.06986v1#bib.bib27); Bianchi et al.,, [2019](https://arxiv.org/html/2510.06986v1#bib.bib18); Andrikogiannopoulou and Papakonstantinou,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib5); Barberis,, [2018](https://arxiv.org/html/2510.06986v1#bib.bib10)).
These developments highlight that investor behavior cannot be fully understood
through variance-based risk alone, motivating the need for more flexible
and empirically grounded models of portfolio choice.

### 2.2 Inverse Optimization Applications

Inverse optimization (IO) has emerged as a powerful paradigm for recovering
unobserved objectives, preferences, or cost parameters from observed decisions
(Ahuja and Orlin,, [2001](https://arxiv.org/html/2510.06986v1#bib.bib2); Iyengar and Kang,, [2005](https://arxiv.org/html/2510.06986v1#bib.bib41); Keshavarz et al.,, [2011](https://arxiv.org/html/2510.06986v1#bib.bib44); [Aswani et al., 2018a,](https://arxiv.org/html/2510.06986v1#bib.bib7) ).
The central idea is to invert the usual optimization process: given solutions that are presumed optimal,
one infers the latent problem parameters that rationalize those decisions.
This perspective has generated a large methodological literature, including formulations based on
variational inequalities, bilevel programming, and learning-theoretic approaches
([Bertsimas et al., 2015b,](https://arxiv.org/html/2510.06986v1#bib.bib17) ; Chan et al.,, [2019](https://arxiv.org/html/2510.06986v1#bib.bib24); [Dong et al., 2020a,](https://arxiv.org/html/2510.06986v1#bib.bib28) ).

In operations research, applications are widespread and well-documented.
Energy systems planning uses IO to estimate marginal costs and policy preferences
([Bertsimas et al., 2015a,](https://arxiv.org/html/2510.06986v1#bib.bib14) ; Ruiz et al.,, [2013](https://arxiv.org/html/2510.06986v1#bib.bib58));
supply chain design leverages IO to recover cost functions and routing preferences
(Chan et al.,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib23); Babier et al.,, [2021](https://arxiv.org/html/2510.06986v1#bib.bib9));
and healthcare scheduling applies IO to calibrate resource allocation models from clinical data
(Truong and Chan,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib60); Elmachtoub and Grigas,, [2021](https://arxiv.org/html/2510.06986v1#bib.bib30)).
These examples highlight IO’s ability to provide interpretable parameter estimates
when direct elicitation is infeasible or biased.

In finance, however, inverse optimization has received comparatively little attention.
Early efforts impute risk-aversion coefficients or utility weights from observed portfolio holdings
(Bruni et al.,, [2017](https://arxiv.org/html/2510.06986v1#bib.bib20); [Cesarone et al., 2020a,](https://arxiv.org/html/2510.06986v1#bib.bib21) ; [Bertsimas et al., 2021a,](https://arxiv.org/html/2510.06986v1#bib.bib15) ),
but the literature remains sparse relative to other domains.
Most existing approaches focus on static settings and rarely incorporate
dynamic preference drift, market shocks, or rigorous statistical guarantees.
Recent advances in learning-based inverse optimization
(Esfahani and Kuhn,, [2018](https://arxiv.org/html/2510.06986v1#bib.bib32); Shafieezadeh-Abadeh et al.,, [2019](https://arxiv.org/html/2510.06986v1#bib.bib59); Ren et al.,, [2025](https://arxiv.org/html/2510.06986v1#bib.bib56))
suggest promising avenues for finance-specific adaptation.
Yet, empirical validations remain limited, particularly in contexts involving heterogeneous investors
and non-financial motives such as ESG preferences.

This gap highlights an opportunity to extend IO beyond traditional domains and
develop methodologies tailored to financial decision-making.
Such methods must contend with the unique challenges of financial markets:
stochastic shocks, parameter uncertainty, and the need for inferential reliability
(bias, variance, coverage).
Addressing these aspects would not only expand the methodological frontier of inverse optimization
but also provide actionable insights into investor behavior, risk management, and portfolio design.

### 2.3 Behavioral Finance Links

A large body of work in behavioral finance emphasizes that investors differ
systematically in their risk attitudes and decision-making heuristics.
Classical expected utility theory has been challenged by empirical evidence showing
substantial heterogeneity in risk aversion across individuals and contexts
(Harrison and Rutström,, [2015](https://arxiv.org/html/2510.06986v1#bib.bib39); Guiso et al.,, [2018](https://arxiv.org/html/2510.06986v1#bib.bib38); Chiappori and Paiella,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib25)).
Behavioral studies further document departures from rational benchmarks,
including probability weighting, framing effects, and reference dependence
(Kahneman and Tversky,, [1979](https://arxiv.org/html/2510.06986v1#bib.bib43); Tversky and Kahneman,, [1992](https://arxiv.org/html/2510.06986v1#bib.bib61); Barberis,, [2018](https://arxiv.org/html/2510.06986v1#bib.bib10)).
These findings underscore the need for flexible models that go beyond quadratic utility
and homogenous preferences.

Transaction costs and trading frictions are another critical determinant of realized allocations.
Market microstructure studies show that illiquidity and bid–ask spreads directly affect
investor behavior and equilibrium prices (Amihud,, [2002](https://arxiv.org/html/2510.06986v1#bib.bib4); Pastor and Stambaugh,, [2003](https://arxiv.org/html/2510.06986v1#bib.bib52); Vayanos and Wang,, [2009](https://arxiv.org/html/2510.06986v1#bib.bib62)).
Dynamic models highlight that portfolio rebalancing costs create persistence in holdings
and amplify heterogeneity across investors (Liu,, [2004](https://arxiv.org/html/2510.06986v1#bib.bib48); Gârleanu and Pedersen,, [2009](https://arxiv.org/html/2510.06986v1#bib.bib37); Jang and Park,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib42)).
These frictions imply that observed portfolios embed both preferences and market constraints,
complicating direct inference from data.

More recently, non-financial motives such as environmental, social, and governance (ESG)
considerations have become central to portfolio choice.
A growing literature shows that investors are willing to sacrifice expected return
to reduce exposure to carbon-intensive or socially undesirable assets
(Heinkel et al.,, [2001](https://arxiv.org/html/2510.06986v1#bib.bib40); Albuquerque et al.,, [2019](https://arxiv.org/html/2510.06986v1#bib.bib3); [Pastor et al., 2021a,](https://arxiv.org/html/2510.06986v1#bib.bib53) ; Pedersen et al.,, [2021](https://arxiv.org/html/2510.06986v1#bib.bib55)).
Sustainable investing not only reflects values-based objectives but also introduces
new channels of risk and hedging, as ESG-tilted portfolios may perform differently
under volatility shocks (Krueger et al.,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib45); Bolton and Kacperczyk,, [2021](https://arxiv.org/html/2510.06986v1#bib.bib19)).
This multi-dimensionality poses new challenges for traditional portfolio theory,
which was not designed to accommodate heterogeneous motives across financial and non-financial dimensions.

Incorporating such heterogeneous and multi-faceted preferences into
optimization models remains a frontier challenge.
Inverse optimization provides a natural tool to infer these latent parameters
from observed allocations, bridging insights from behavioral finance with rigorous
optimization-based inference.
By doing so, it offers a principled approach to disentangle risk aversion,
trading frictions, and ESG motives—three of the most salient behavioral drivers
of modern portfolio choice.

## 3 Model Formulation

### 3.1 Forward Problem

#### 3.1.1 Decision Variables

Let 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} denote the portfolio weights across nn assets.
The feasible set is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒳={𝐱∈ℝn:𝟏⊤​𝐱=1,𝐱≥𝟎}.\mathcal{X}=\left\{\mathbf{x}\in\mathbb{R}^{n}:\mathbf{1}^{\top}\mathbf{x}=1,\;\mathbf{x}\geq\mathbf{0}\right\}. |  | (1) |

#### 3.1.2 Objective Function

We consider a mean–variance style optimization problem with transaction costs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝐱∈𝒳⁡f​(𝐱;μ,𝚺,θ,𝐜)=μ⊤​𝐱−θ2​𝐱⊤​𝚺​𝐱−𝐜⊤​𝐱.\max\_{\mathbf{x}\in\mathcal{X}}\;f(\mathbf{x};\mathbf{\mu},\mathbf{\Sigma},\theta,\mathbf{c})=\mathbf{\mu}^{\top}\mathbf{x}-\frac{\theta}{2}\mathbf{x}^{\top}\mathbf{\Sigma}\mathbf{x}-\mathbf{c}^{\top}\mathbf{x}. |  | (2) |

#### 3.1.3 Optimal Solution

Denote the optimizer as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱∗​(μ,𝚺,θ,𝐜)=arg⁡max𝐱∈𝒳⁡f​(𝐱;μ,𝚺,θ,𝐜).\mathbf{x}^{\*}(\mathbf{\mu},\mathbf{\Sigma},\theta,\mathbf{c})=\arg\max\_{\mathbf{x}\in\mathcal{X}}f(\mathbf{x};\mathbf{\mu},\mathbf{\Sigma},\theta,\mathbf{c}). |  | (3) |

### 3.2 Inverse Problem

#### 3.2.1 Observation Setup

We observe portfolios {𝐱t}t=1T\{\mathbf{x}^{t}\}\_{t=1}^{T} that are approximately optimal under unknown parameters.

#### 3.2.2 Inverse Optimization Objective

We aim to recover (θ,𝐜)(\theta,\mathbf{c}) by minimizing the discrepancy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ,𝐜⁡L​(θ,𝐜)=∑t=1T‖𝐱t−𝐱∗​(μt,𝚺t,θ,𝐜)‖22.\min\_{\theta,\mathbf{c}}\;L(\theta,\mathbf{c})=\sum\_{t=1}^{T}\left\|\mathbf{x}^{t}-\mathbf{x}^{\*}(\mathbf{\mu}^{t},\mathbf{\Sigma}^{t},\theta,\mathbf{c})\right\|\_{2}^{2}. |  | (4) |

#### 3.2.3 Regularization (Optional Extension)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lreg​(θ,𝐜)=L​(θ,𝐜)+λθ​|θ|+λc​‖𝐜‖1.L\_{\text{reg}}(\theta,\mathbf{c})=L(\theta,\mathbf{c})+\lambda\_{\theta}|\theta|+\lambda\_{c}\|\mathbf{c}\|\_{1}. |  | (5) |

### 3.3 Optimality Conditions

#### 3.3.1 KKT System

The Lagrangian of the forward problem is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(𝐱,λ,ν)=μ⊤​𝐱−θ2​𝐱⊤​𝚺​𝐱−𝐜⊤​𝐱+λ​(1−𝟏⊤​𝐱)+ν⊤​𝐱.\mathcal{L}(\mathbf{x},\lambda,\mathbf{\nu})=\mathbf{\mu}^{\top}\mathbf{x}-\frac{\theta}{2}\mathbf{x}^{\top}\mathbf{\Sigma}\mathbf{x}-\mathbf{c}^{\top}\mathbf{x}+\lambda(1-\mathbf{1}^{\top}\mathbf{x})+\mathbf{\nu}^{\top}\mathbf{x}. |  | (6) |

The KKT conditions are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ−θ​𝚺​𝐱∗−𝐜−λ​𝟏+ν\displaystyle\mathbf{\mu}-\theta\mathbf{\Sigma}\mathbf{x}^{\*}-\mathbf{c}-\lambda\mathbf{1}+\mathbf{\nu} | =𝟎,\displaystyle=\mathbf{0}, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝟏⊤​𝐱∗\displaystyle\mathbf{1}^{\top}\mathbf{x}^{\*} | =1,\displaystyle=1, |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐱∗≥𝟎,ν≥𝟎,νi​xi∗\displaystyle\mathbf{x}^{\*}\geq\mathbf{0},\quad\mathbf{\nu}\geq\mathbf{0},\quad\nu\_{i}x\_{i}^{\*} | =0​∀i.\displaystyle=0\;\;\forall i. |  | (9) |

#### 3.3.2 Closed-Form Interior Solution

If 𝐱∗>𝟎\mathbf{x}^{\*}>\mathbf{0} (interior solution), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱∗=1θ​𝚺−1​(μ−𝐜−λ​𝟏),\mathbf{x}^{\*}=\frac{1}{\theta}\mathbf{\Sigma}^{-1}(\mathbf{\mu}-\mathbf{c}-\lambda\mathbf{1}), |  | (10) |

with λ\lambda chosen to satisfy ([8](https://arxiv.org/html/2510.06986v1#S3.E8 "In 3.3.1 KKT System ‣ 3.3 Optimality Conditions ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")).

#### 3.3.3 Connection to Variational Inequalities and Bilevel IO

The KKT system can equivalently be expressed as a variational inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI(F,𝒳):⟨θ𝚺𝐱∗+𝐜−μ,𝐱−𝐱∗⟩≥0∀𝐱∈𝒳.\text{VI}(F,\mathcal{X}):\quad\langle\theta\mathbf{\Sigma}\mathbf{x}^{\*}+\mathbf{c}-\mathbf{\mu},\;\mathbf{x}-\mathbf{x}^{\*}\rangle\geq 0\quad\forall\mathbf{x}\in\mathcal{X}. |  | (11) |

Formally, the inverse problem ([4](https://arxiv.org/html/2510.06986v1#S3.E4 "In 3.2.2 Inverse Optimization Objective ‣ 3.2 Inverse Problem ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")) is a bilevel program:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ,𝐜​∑t=1T‖𝐱t−𝐱‖2s.t. ​𝐱∈arg⁡max𝐱∈𝒳⁡f​(𝐱;μt,𝚺t,θ,𝐜).\min\_{\theta,\mathbf{c}}\sum\_{t=1}^{T}\|\mathbf{x}^{t}-\mathbf{x}\|^{2}\quad\text{s.t. }\mathbf{x}\in\arg\max\_{\mathbf{x}\in\mathcal{X}}f(\mathbf{x};\mathbf{\mu}^{t},\mathbf{\Sigma}^{t},\theta,\mathbf{c}). |  | (12) |

These conditions form the analytical foundation for identifiability and statistical recovery, as discussed next.

### 3.4 Identifiability

#### 3.4.1 Uniqueness of Recovery

We ask under what conditions (θ,𝐜)(\theta,\mathbf{c}) can be uniquely identified.

##### Condition 1 (Variation in Inputs).

If {(μt,𝚺t)}t=1T\{(\mathbf{\mu}^{t},\mathbf{\Sigma}^{t})\}\_{t=1}^{T} span a sufficiently rich set,
then θ\theta is identifiable from the curvature of optimal solutions.

##### Condition 2 (Normalization).

Since scaling of (θ,𝐜)(\theta,\mathbf{c}) may not be unique,
we impose a normalization, e.g. θ∈[0,θmax]\theta\in[0,\theta\_{\max}],
or ‖𝐜‖2=1\|\mathbf{c}\|\_{2}=1.

##### Condition 3 (No Redundancy).

If two assets have identical (μit,Σi,⋅t)(\mu\_{i}^{t},\Sigma\_{i,\cdot}^{t}) for all tt,
then their cic\_{i} cannot be separately identified.

#### 3.4.2 Formal Theorem

###### Theorem 3.1 (Identifiability).

Suppose (i) 𝚺t≻0\mathbf{\Sigma}^{t}\succ 0 for all tt,
(ii) {(μt,𝚺t)}t=1T\{(\mathbf{\mu}^{t},\mathbf{\Sigma}^{t})\}\_{t=1}^{T} yield at least two distinct active sets,
and (iii) a normalization on (θ,𝐜)(\theta,\mathbf{c}) is imposed.
Then (θ,𝐜)(\theta,\mathbf{c}) is uniquely identifiable.
*Proof is provided in Appendix [C.1](https://arxiv.org/html/2510.06986v1#A3.SS1 "C.1 Proof of Theorem 3.1 (Identifiability) ‣ Appendix C Proofs of Theoretical Results ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").*

#### 3.4.3 Extension: Dynamic Preferences

For robustness, we may consider time-varying θt\theta\_{t} with a smoothness penalty:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min{θt},𝐜​∑t=1T‖𝐱t−𝐱∗​(θt,𝐜)‖2+γ​∑t=2T(θt−θt−1)2.\min\_{\{\theta\_{t}\},\mathbf{c}}\sum\_{t=1}^{T}\|\mathbf{x}^{t}-\mathbf{x}^{\*}(\theta\_{t},\mathbf{c})\|^{2}+\gamma\sum\_{t=2}^{T}(\theta\_{t}-\theta\_{t-1})^{2}. |  | (13) |

This extension links to online inverse optimization, where dynamic regret

|  |  |  |  |
| --- | --- | --- | --- |
|  | RT=∑t=1T(f​(𝐱∗​(θttrue))−f​(𝐱∗​(θ^t))),R\_{T}=\sum\_{t=1}^{T}\Big(f(\mathbf{x}^{\*}(\theta\_{t}^{\text{true}}))-f(\mathbf{x}^{\*}(\hat{\theta}\_{t}))\Big), |  | (14) |

quantifies cumulative estimation error.
Stability of {θt}\{\theta\_{t}\} is ensured when γ\gamma is sufficiently large,
preventing overfitting to short-term fluctuations.

These observations align our formulation with the sublinear regret bounds in online convex optimization,
demonstrating that meaningful recovery is still possible under preference drift.

### 3.5 Generalizations and Robustness

#### 3.5.1 Nonlinear Transaction Costs

While we adopt a linear specification 𝐜⊤​𝐱\mathbf{c}^{\top}\mathbf{x} in ([2](https://arxiv.org/html/2510.06986v1#S3.E2 "In 3.1.2 Objective Function ‣ 3.1 Forward Problem ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")),
the framework extends naturally to convex nonlinear costs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(𝐱)=∑j=1nκj​|xj|p,p≥1,\phi(\mathbf{x})=\sum\_{j=1}^{n}\kappa\_{j}|x\_{j}|^{p},\quad p\geq 1, |  | (15) |

which preserve convexity of the forward problem.
The corresponding KKT (or VI) conditions are modified only through the subgradients of ϕ​(𝐱)\phi(\mathbf{x}).
Identifiability arguments remain valid under the same variation and normalization assumptions.
A detailed proof is provided in Appendix A.

#### 3.5.2 Distributional Robustness

Our analysis assumes known (μt,𝚺t)(\mathbf{\mu}^{t},\mathbf{\Sigma}^{t}),
but in practice these parameters are estimated.
We therefore consider a distributionally robust forward problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝐱∈𝒳⁡min(μ,𝚺)∈𝒰⁡{μ⊤​𝐱−θ2​𝐱⊤​𝚺​𝐱−𝐜⊤​𝐱},\max\_{\mathbf{x}\in\mathcal{X}}\;\min\_{(\mathbf{\mu},\mathbf{\Sigma})\in\mathcal{U}}\Big\{\mathbf{\mu}^{\top}\mathbf{x}-\tfrac{\theta}{2}\mathbf{x}^{\top}\mathbf{\Sigma}\mathbf{x}-\mathbf{c}^{\top}\mathbf{x}\Big\}, |  | (16) |

where 𝒰\mathcal{U} is an ellipsoidal or moment-based uncertainty set.
The robust counterpart can be reformulated as a conic program
(e.g., SOCP or SDP depending on 𝒰\mathcal{U}).
Inverse recovery proceeds analogously by matching observed 𝐱t\mathbf{x}^{t}
with robust optimal solutions.
Details and proofs are given in Appendix B.

#### 3.5.3 Alternative Risk Measures

Beyond variance, risk preferences may be captured by coherent measures such as Conditional Value-at-Risk (CVaR):

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝐱∈𝒳⁡μ⊤​𝐱−θ​CVaRα​(−𝐫⊤​𝐱)−𝐜⊤​𝐱.\max\_{\mathbf{x}\in\mathcal{X}}\;\mathbf{\mu}^{\top}\mathbf{x}-\theta\,\mathrm{CVaR}\_{\alpha}(-\mathbf{r}^{\top}\mathbf{x})-\mathbf{c}^{\top}\mathbf{x}. |  | (17) |

The inverse framework extends by estimating θ\theta relative to the chosen risk measure.
While technical details differ, the identifiability logic (variation in inputs, normalization, no redundancy)
still applies. This generalization connects inverse portfolio optimization
to the broader literature on coherent and convex risk measures.

### 3.6 Consistency and Robustness Results

The first set of results establishes the statistical soundness of the proposed estimator.
Consistency ensures that, given sufficient data, the recovered parameters converge
to the true investor preferences, while robustness guarantees bounded error even
under misspecification of the transaction cost function.

###### Proposition 3.1 (Consistency).

Suppose observed portfolios {𝐱t}\{\mathbf{x}^{t}\} are generated exactly by
([2](https://arxiv.org/html/2510.06986v1#S3.E2 "In 3.1.2 Objective Function ‣ 3.1 Forward Problem ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")) with parameters (θ∗,𝐜∗)(\theta^{\ast},\mathbf{c}^{\ast}).
If (i) {μt,𝚺t}\{\mathbf{\mu}^{t},\mathbf{\Sigma}^{t}\} are i.i.d. with compact support and
(ii) identifiability holds as in Theorem [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem1 "Theorem 3.1 (Identifiability). ‣ 3.4.2 Formal Theorem ‣ 3.4 Identifiability ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty"),
then the inverse optimization estimator θ^\hat{\theta} from ([4](https://arxiv.org/html/2510.06986v1#S3.E4 "In 3.2.2 Inverse Optimization Objective ‣ 3.2 Inverse Problem ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")) is consistent as T→∞T\to\infty:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^→𝑝θ∗,𝐜^→𝑝𝐜∗.\hat{\theta}\;\xrightarrow{p}\;\theta^{\ast},\qquad\hat{\mathbf{c}}\;\xrightarrow{p}\;\mathbf{c}^{\ast}. |  | (18) |

*Proof is provided in Appendix [C.2](https://arxiv.org/html/2510.06986v1#A3.SS2 "C.2 Proof of Proposition 3.1 (Consistency) ‣ Appendix C Proofs of Theoretical Results ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").*

###### Lemma 3.1 (Robustness to Misspecification).

Suppose the true transaction cost function is convex and homogeneous of degree p∈[1,2]p\in[1,2],
denoted ϕ​(𝐱)\phi(\mathbf{x}), and the researcher instead estimates with a linear specification 𝐜⊤​𝐱\mathbf{c}^{\top}\mathbf{x}.
Then there exists (θ^,𝐜^)(\hat{\theta},\hat{\mathbf{c}}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(θ^,𝐜^)−(θ∗,𝐜∗)‖≤L⋅sup𝐱∈𝒳|ϕ​(𝐱)−𝐜∗⊤​𝐱|=O​(ε),\|(\hat{\theta},\hat{\mathbf{c}})-(\theta^{\ast},\mathbf{c}^{\ast})\|\;\leq\;L\cdot\sup\_{\mathbf{x}\in\mathcal{X}}\big|\phi(\mathbf{x})-\mathbf{c}^{\ast\top}\mathbf{x}\big|\;=\;O(\varepsilon), |  | (19) |

where ε\varepsilon quantifies the deviation of ϕ\phi from linearity.
*Proof is provided in Appendix [C.3](https://arxiv.org/html/2510.06986v1#A3.SS3 "C.3 Proof of Lemma 3.1 (Robustness to Misspecification) ‣ Appendix C Proofs of Theoretical Results ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").*

Together, Proposition [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmproposition1 "Proposition 3.1 (Consistency). ‣ 3.6 Consistency and Robustness Results ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") and Lemma [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmlemma1 "Lemma 3.1 (Robustness to Misspecification). ‣ 3.6 Consistency and Robustness Results ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")
demonstrate that the estimator is both asymptotically reliable and stable under
modeling imperfections. These properties form the statistical foundation for
the subsequent dynamic analysis.

### 3.7 Dynamic Extension and Regret Bounds

We next extend the framework to account for time-varying preferences.
In realistic financial environments, investor risk aversion or ESG orientation
may evolve over time. To capture such dynamics, we introduce a temporal
regularization term penalizing preference drift, leading to the dynamic
inverse formulation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min{θt},𝐜​∑t=1T‖𝐱t−𝐱∗​(θt,𝐜)‖2+γ​∑t=2T(θt−θt−1)2.\min\_{\{\theta\_{t}\},\mathbf{c}}\;\sum\_{t=1}^{T}\|\mathbf{x}^{t}-\mathbf{x}^{\*}(\theta\_{t},\mathbf{c})\|^{2}+\gamma\sum\_{t=2}^{T}(\theta\_{t}-\theta\_{t-1})^{2}. |  | (20) |

###### Theorem 3.2 (Dynamic Regret Bound).

Assume θt\theta\_{t} varies with bounded drift
∑t=2T|θt−θt−1|≤D\sum\_{t=2}^{T}|\theta\_{t}-\theta\_{t-1}|\leq D.
Then the cumulative dynamic regret

|  |  |  |  |
| --- | --- | --- | --- |
|  | RT=∑t=1T(f​(x∗​(θt∗))−f​(x∗​(θ^t)))R\_{T}=\sum\_{t=1}^{T}\Big(f(x^{\*}(\theta\_{t}^{\ast}))-f(x^{\*}(\hat{\theta}\_{t}))\Big) |  | (21) |

satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | RT≤C1​T+C2​D,R\_{T}\;\leq\;C\_{1}\sqrt{T}+C\_{2}D, |  | (22) |

for universal constants C1,C2>0C\_{1},C\_{2}>0.
*Proof is provided in Appendix [C.4](https://arxiv.org/html/2510.06986v1#A3.SS4 "C.4 Proof of Theorem 3.2 (Dynamic Regret Bound) ‣ Appendix C Proofs of Theoretical Results ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").*

###### Corollary 1 (Static Preferences).

If preferences remain constant, i.e. θt=θ∗\theta\_{t}=\theta^{\ast} for all tt,
then the drift term vanishes (D=0)(D=0).
In this case, the regret bound in Theorem [3.2](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem2 "Theorem 3.2 (Dynamic Regret Bound). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | RT=O​(T),R\_{T}=O(\sqrt{T}), |  | (23) |

which matches the classical sublinear regret rate in online convex optimization.
*Proof is provided in Appendix [C.5](https://arxiv.org/html/2510.06986v1#A3.SS5 "C.5 Proof of Corollary 1 (Static Preferences) ‣ Appendix C Proofs of Theoretical Results ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").*

Theorem [3.2](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem2 "Theorem 3.2 (Dynamic Regret Bound). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") and Corollary [1](https://arxiv.org/html/2510.06986v1#Thmcorollary1 "Corollary 1 (Static Preferences). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")
demonstrate that the proposed dynamic extension achieves
provably sublinear regret, even under evolving investor preferences.
This highlights both the adaptability and theoretical rigor of the approach,
linking statistical recovery with robust decision support under uncertainty.

## 4 Synthetic Data Generation

### 4.1 Return and Covariance Simulation

#### 4.1.1 Return Process

To mimic realistic cross-sectional dependence among asset returns,
we generate synthetic returns from a kk-factor structure:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐫t\displaystyle\mathbf{r}\_{t} | =μ+𝐅𝐟t+ϵt,t=1,…,T,\displaystyle=\mathbf{\mu}+\mathbf{F}\mathbf{f}\_{t}+\mathbf{\epsilon}\_{t},\qquad t=1,\ldots,T, |  | (24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐟t\displaystyle\mathbf{f}\_{t} | ∼𝒩​(𝟎,𝐈k),ϵt∼𝒩​(𝟎,𝚿),\displaystyle\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{k}),\quad\mathbf{\epsilon}\_{t}\sim\mathcal{N}(\mathbf{0},\mathbf{\Psi}), |  | (25) |

where

* •

  𝐅∈ℝn×k\mathbf{F}\in\mathbb{R}^{n\times k} is the factor loading matrix, capturing common market and sector exposures,
* •

  𝚿=diag​(σ12,…,σn2)\mathbf{\Psi}=\mathrm{diag}(\sigma\_{1}^{2},\ldots,\sigma\_{n}^{2}) encodes idiosyncratic variances,
* •

  μ∼𝒩​(μ¯​𝟏,σ2​𝐈n)\mathbf{\mu}\sim\mathcal{N}(\bar{\mu}\mathbf{1},\sigma^{2}\mathbf{I}\_{n}) represents heterogeneous expected returns across assets.

##### Covariance Structure.

By construction, the implied covariance matrix satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=𝔼​[(𝐫t−μ)​(𝐫t−μ)⊤]=𝐅𝐅⊤+𝚿,\mathbf{\Sigma}=\mathbb{E}\!\big[(\mathbf{r}\_{t}-\mathbf{\mu})(\mathbf{r}\_{t}-\mathbf{\mu})^{\top}\big]=\mathbf{F}\mathbf{F}^{\top}+\mathbf{\Psi}, |  | (26) |

which is positive semidefinite for all realizations of (𝐅,𝚿)(\mathbf{F},\mathbf{\Psi}).
This decomposition separates systematic risk (spanned by 𝐅𝐟t\mathbf{F}\mathbf{f}\_{t})
from idiosyncratic risk (ϵt\mathbf{\epsilon}\_{t}), consistent with arbitrage pricing theory.

##### Parameterization.

For each Monte Carlo replication, we generate factor loadings as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fi​j∼𝒩​(0,σF2),F\_{ij}\sim\mathcal{N}(0,\sigma\_{F}^{2}), |  | (27) |

and idiosyncratic variances as

|  |  |  |  |
| --- | --- | --- | --- |
|  | σj2∼Uniform​[σ¯2,σ¯2].\sigma\_{j}^{2}\sim\text{Uniform}[\underline{\sigma}^{2},\overline{\sigma}^{2}]. |  | (28) |

This ensures heterogeneity across assets while preserving positive definiteness of 𝚺\mathbf{\Sigma}.

##### Temporal Dependence (Optional Extension).

To introduce time-varying volatility, the idiosyncratic shocks can follow a GARCH(1,1)(1,1) process:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϵj,t\displaystyle\epsilon\_{j,t} | ∼𝒩​(0,σj,t2),\displaystyle\sim\mathcal{N}(0,\sigma\_{j,t}^{2}), |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σj,t+12\displaystyle\sigma\_{j,t+1}^{2} | =α0+α1​ϵj,t2+β​σj,t2,\displaystyle=\alpha\_{0}+\alpha\_{1}\epsilon\_{j,t}^{2}+\beta\sigma\_{j,t}^{2}, |  | (30) |

which yields clustered volatility and heavy tails, a stylized fact in financial returns.

##### Interpretation.

This construction produces synthetic data that

1. 1.

   preserves realistic cross-sectional correlation via 𝐅𝐅⊤\mathbf{F}\mathbf{F}^{\top},
2. 2.

   allows heterogeneous and dynamic risk via 𝚿\mathbf{\Psi},
3. 3.

   accommodates both stable and shock-prone regimes via optional GARCH dynamics.

As such, it provides a rigorous and flexible platform to evaluate inverse recovery of investor preferences under controlled but finance-consistent conditions.

### 4.2 Investor Types

To reflect heterogeneous investment behaviors, we simulate three representative investor archetypes.
Each type is characterized by a distinct preference parameterization
θ=(ρ,τ,η)\theta=(\rho,\tau,\eta),
where ρ\rho governs risk aversion, τ\tau transaction cost sensitivity, and η\eta ESG preference intensity.

#### 4.2.1 Conservative

We define conservative investors by a high risk-aversion parameter:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ∈[5,10],τ≈0,η=0.\rho\in[5,10],\quad\tau\approx 0,\quad\eta=0. |  | (31) |

Their utility is dominated by variance penalization:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ucons​(𝐱)=μ⊤​𝐱−ρ2​𝐱⊤​𝚺​𝐱.U\_{\text{cons}}(\mathbf{x})=\mathbf{\mu}^{\top}\mathbf{x}-\tfrac{\rho}{2}\mathbf{x}^{\top}\mathbf{\Sigma}\mathbf{x}. |  | (32) |

Interpretation. These investors strongly prefer stable portfolios with low volatility,
and allocate predominantly to assets with low variance and low correlation.
Simulation role. Serves as a benchmark to test identifiability of ρ\rho
under extreme curvature in the objective function.

#### 4.2.2 Neutral

Neutral investors exhibit moderate risk aversion with baseline transaction costs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ∈[1,3],τ∈[0.1,0.5],η=0.\rho\in[1,3],\quad\tau\in[0.1,0.5],\quad\eta=0. |  | (33) |

The utility becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uneut​(𝐱)=μ⊤​𝐱−ρ2​𝐱⊤​𝚺​𝐱−τ​‖𝐱−𝐱prev‖1.U\_{\text{neut}}(\mathbf{x})=\mathbf{\mu}^{\top}\mathbf{x}-\tfrac{\rho}{2}\mathbf{x}^{\top}\mathbf{\Sigma}\mathbf{x}-\tau\|\mathbf{x}-\mathbf{x}^{\text{prev}}\|\_{1}. |  | (34) |

Interpretation. This group represents average investors balancing mean–variance trade-offs
while acknowledging adjustment costs between periods.
Simulation role. Provides a mid-range case to evaluate how inverse recovery behaves
when both ρ\rho and τ\tau are active but moderate in magnitude.

#### 4.2.3 ESG-Oriented

ESG-oriented investors display moderate risk aversion with an additional carbon penalty:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ∈[2,4],τ∈[0.1,0.5],η∈[0.5,2.0].\rho\in[2,4],\quad\tau\in[0.1,0.5],\quad\eta\in[0.5,2.0]. |  | (35) |

Their utility is

|  |  |  |  |
| --- | --- | --- | --- |
|  | UESG​(𝐱)=μ⊤​𝐱−ρ2​𝐱⊤​𝚺​𝐱−τ​‖𝐱−𝐱prev‖1−η​𝐜⊤​𝐱,U\_{\text{ESG}}(\mathbf{x})=\mathbf{\mu}^{\top}\mathbf{x}-\tfrac{\rho}{2}\mathbf{x}^{\top}\mathbf{\Sigma}\mathbf{x}-\tau\|\mathbf{x}-\mathbf{x}^{\text{prev}}\|\_{1}-\eta\,\mathbf{c}^{\top}\mathbf{x}, |  | (36) |

where 𝐜∈ℝ≥0n\mathbf{c}\in\mathbb{R}^{n}\_{\geq 0} encodes each asset’s carbon footprint or ESG score.
Interpretation. These investors accept lower financial returns
in exchange for reduced environmental exposure.
Simulation role. Tests robustness of inverse recovery in the presence of correlated preferences,
since η\eta and ρ\rho may interact nontrivially in shaping the optimal portfolio.

## 5 Numerical Experiments

### 5.1 Experimental Design

#### 5.1.1 Base Parameters

We fix the number of assets at n=10n=10 and simulate T=100T=100 portfolio decisions per run.
To ensure statistical validity, each experiment is repeated R=100R=100 Monte Carlo trials.
Random seeds are drawn independently for each trial, and we report results aggregated over all replications.

##### Factor Structure.

We set the number of systematic factors to k=3k=3.
Factor loadings are generated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fi​j∼𝒩​(0,σF2),σF2=0.25,F\_{ij}\sim\mathcal{N}(0,\sigma\_{F}^{2}),\qquad\sigma\_{F}^{2}=0.25, |  | (37) |

and idiosyncratic variances as

|  |  |  |  |
| --- | --- | --- | --- |
|  | σj2∼Uniform​[0.05,0.20].\sigma\_{j}^{2}\sim\mathrm{Uniform}[0.05,0.20]. |  | (38) |

This specification induces both moderate cross-sectional correlation and heterogeneity across assets.

##### Return Means.

Expected returns are sampled as

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ∼𝒩​(μ¯,σμ2​𝐈n),μ¯=0.05,σμ2=0.01,\mathbf{\mu}\sim\mathcal{N}(\bar{\mu},\sigma\_{\mu}^{2}\mathbf{I}\_{n}),\qquad\bar{\mu}=0.05,\;\sigma\_{\mu}^{2}=0.01, |  | (39) |

consistent with stylized equity return levels.

##### Parameter Space for Investors.

We simulate investor types using the parameter ranges defined in Section [4.2](https://arxiv.org/html/2510.06986v1#S4.SS2 "4.2 Investor Types ‣ 4 Synthetic Data Generation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ∈{1,2,3,5,7,10},τ∈{0,0.1,0.3,0.5},η∈{0,0.5,1.0,2.0}.\rho\in\{1,2,3,5,7,10\},\quad\tau\in\{0,0.1,0.3,0.5\},\quad\eta\in\{0,0.5,1.0,2.0\}. |  | (40) |

This design covers conservative, neutral, and ESG-oriented investors in a balanced factorial structure.

##### Experimental Protocol.

For each Monte Carlo trial r=1,…,Rr=1,\ldots,R:

1. 1.

   Generate (μ,𝚺)(\mathbf{\mu},\mathbf{\Sigma}) from the factor model.
2. 2.

   Draw investor parameters (ρ,τ,η)(\rho,\tau,\eta) from the designated set.
3. 3.

   Solve the forward problem (Section [3](https://arxiv.org/html/2510.06986v1#S3 "3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")) to obtain portfolios 𝐱t,r\mathbf{x}^{t,r} for t=1,…,Tt=1,\ldots,T.
4. 4.

   Apply inverse optimization to recover (ρ^,τ^,η^)(\hat{\rho},\hat{\tau},\hat{\eta}).

This yields a distribution of estimation errors across (R×T)(R\times T) problem instances.

##### Solver and Implementation.

All forward problems are quadratic programs solved via Gurobi 11.0 with feasibility tolerance 10−810^{-8} and optimality gap 10−910^{-9}.
The inverse problem is implemented in Python using CVXPY 1.4.2, leveraging the OSQP solver.
Warm-starts with randomized initializations are used to avoid local minima.
All experiments are run on a dedicated computing cluster; average runtime and variance across trials are reported
to confirm computational stability and tractability.

##### Design of Experiments.

In addition to grid-based parameter variation, we conduct robustness checks using Latin Hypercube Sampling (LHS) across (ρ,τ,η)(\rho,\tau,\eta) ranges.
This ensures coverage of the continuous parameter space and prevents results from being artifacts of discrete grid choices.

##### Validation.

We implement both in-sample and out-of-sample validation:

* •

  Training: 80%80\% of simulated portfolios are used for parameter recovery.
* •

  Testing: 20%20\% held-out portfolios are used to evaluate predictive regret.
* •

  Confidence intervals are constructed via nonparametric bootstrap with B=200B=200 resamples.

This design guarantees that reported performance metrics reflect both estimation accuracy and predictive generalization.

Table 1: Simulation setup and parameter ranges. Values are fixed by design except runtime and environment, which will be reported after experiments.

|  |  |
| --- | --- |
| Category | Specification |
| Number of assets | n=10n=10 |
| Number of factors | k=3k=3 |
| Time periods per trial | T=100T=100 |
| Monte Carlo replications | R=100R=100 |
| Factor loadings | Fi​j∼𝒩​(0,0.25)F\_{ij}\sim\mathcal{N}(0,0.25) |
| Idiosyncratic variances | σj2∼U​[0.05,0.20]\sigma\_{j}^{2}\sim U[0.05,0.20] |
| Expected returns | μ∼𝒩​(0.05,0.01​In)\mu\sim\mathcal{N}(0.05,0.01I\_{n}) |
| Risk aversion ρ\rho | {1,2,3,5,7,10}\{1,2,3,5,7,10\} |
| Transaction cost τ\tau | {0,0.1,0.3,0.5}\{0,0.1,0.3,0.5\} |
| ESG penalty η\eta | {0,0.5,1.0,2.0}\{0,0.5,1.0,2.0\} |
| Train/Test split | 80% / 20% |
| Bootstrap resamples | B=200B=200 |

![Refer to caption](x1.png)


Figure 1: Monte Carlo experimental pipeline.
Blue denotes data generation, green optimization, orange performance metrics,
purple aggregation, and red validation.
Numbered stages (1–7) clarify the workflow.

### 5.2 Performance Metrics

#### 5.2.1 Parameter Recovery

For each structural parameter — θ\theta (risk aversion),
cc (transaction cost coefficient), and η\eta (ESG penalty) —
we assess the quality of inverse recovery across R=100R=100 Monte Carlo replications.

##### Bias, Variance, and Mean Squared Error.

We report standard point-estimation diagnostics:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bias​(θ^)\displaystyle\text{Bias}(\hat{\theta}) | =1R​∑r=1R(θ^(r)−θtrue),\displaystyle=\frac{1}{R}\sum\_{r=1}^{R}\big(\hat{\theta}^{(r)}-\theta^{\text{true}}\big), |  | (41) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​(θ^)\displaystyle\text{Var}(\hat{\theta}) | =1R​∑r=1R(θ^(r)−θ^¯)2,\displaystyle=\frac{1}{R}\sum\_{r=1}^{R}\big(\hat{\theta}^{(r)}-\overline{\hat{\theta}}\big)^{2}, |  | (42) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | MSE​(θ^)\displaystyle\text{MSE}(\hat{\theta}) | =Bias​(θ^)2+Var​(θ^).\displaystyle=\text{Bias}(\hat{\theta})^{2}+\text{Var}(\hat{\theta}). |  | (43) |

These measures respectively capture systematic error, sampling dispersion, and overall accuracy.

##### Coverage Probability.

To evaluate inferential reliability, we construct nonparametric bootstrap intervals
with B=200B=200 resamples and compute

|  |  |  |
| --- | --- | --- |
|  | Coverage​(θ)=Pr⁡(θtrue∈C​I0.95​(θ^)).\text{Coverage}(\theta)=\Pr\!\left(\theta^{\text{true}}\in CI\_{0.95}(\hat{\theta})\right). |  |

A well-calibrated estimator should achieve coverage near the nominal 95%95\% level.

##### Convergence Rate.

Consistency is examined by scaling the number of observations TT.
Empirical slopes in log–log regressions of MSE versus TT provide convergence rates

|  |  |  |
| --- | --- | --- |
|  | MSE​(θ^)=O​(T−α),α>0,\text{MSE}(\hat{\theta})=O(T^{-\alpha}),\qquad\alpha>0, |  |

which can be benchmarked against the canonical α=12\alpha=\tfrac{1}{2} rate of stochastic approximation.

##### Economic Performance.

Statistical accuracy does not automatically imply economic relevance.
We therefore quantify the welfare cost of parameter misspecification via the *utility gap*:

|  |  |  |
| --- | --- | --- |
|  | Δ​U=𝔼​[f​(x∗​(θtrue))]−𝔼​[f​(x∗​(θ^))],\Delta U=\mathbb{E}\big[f(x^{\*}(\theta^{\text{true}}))\big]-\mathbb{E}\big[f(x^{\*}(\hat{\theta}))\big], |  |

which measures the expected reduction in investor utility when allocations are computed
with recovered parameters rather than true preferences.

#### 5.2.2 Statistical Testing

All reported differences in recovery quality (e.g., across investor types or under shocks)
are formally tested using paired tt-tests and Wilcoxon signed-rank tests.
We adopt p<0.05p<0.05 as the threshold for significance,
with Bonferroni correction applied to account for multiple comparisons.

##### Summary.

This multi-layered evaluation ensures that results are both statistically rigorous
(Bias, Variance, MSE, coverage, convergence)
and economically meaningful (utility gap analysis).

#### 5.2.3 Visualization of Recovery Performance

Table 2: Parameter recovery performance across R=100R=100 Monte Carlo trials
(values are averages; coverage computed via nonparametric bootstrap with B=200B=200 resamples).
Risk aversion is difficult to recover, while transaction costs are highly identifiable.
ESG penalties exhibit moderate bias and large variance, reflecting partial identifiability.

| Parameter | Bias | Variance | MSE | Coverage (95%) |
| --- | --- | --- | --- | --- |
| θ\theta (Risk Aversion) | 4.3327 | 10.2152 | 28.9870 | 0.0 |
| cc (Transaction Cost) | -0.2600 | 0.0364 | 0.1040 | 1.0 |
| η\eta (ESG Penalty) | -0.1792 | 0.4580 | 0.4901 | 0.0 |

![Refer to caption](Fig2.png)


Figure 2: Convergence of parameter recovery errors.
Log–log slopes approximate empirical convergence rates α\alpha.
Risk aversion (ρ\rho) exhibits persistent bias leading to large MSE,
transaction cost (τ\tau) converges stably with negligible error and full coverage,
and ESG penalty (η\eta) shows moderate error with substantial dispersion,
consistent with partial identifiability.

### 5.3 Dynamic Regret

Dynamic regret quantifies the cumulative welfare loss due to parameter misspecification:

|  |  |  |
| --- | --- | --- |
|  | RT​(θ^)=∑t=1T(f​(x∗​(θtrue;μt,Σt))−f​(x∗​(θ^;μt,Σt))).R\_{T}(\hat{\theta})=\sum\_{t=1}^{T}\Big(f(x^{\*}(\theta^{\text{true}};\mu^{t},\Sigma^{t}))-f(x^{\*}(\hat{\theta};\mu^{t},\Sigma^{t}))\Big). |  |

##### Normalization and Scaling.

We analyze the growth rate by reporting

|  |  |  |
| --- | --- | --- |
|  | RT​(θ^)T,\frac{R\_{T}(\hat{\theta})}{\sqrt{T}}, |  |

which should converge to a constant under the sublinear bound established in Theorem 2.
This verifies that estimation error does not accumulate linearly over time.

##### Decomposition.

We further decompose RTR\_{T} into a static error component and a drift-induced component:

|  |  |  |
| --- | --- | --- |
|  | RT=RTstatic+RTdrift,R\_{T}=R\_{T}^{\text{static}}+R\_{T}^{\text{drift}}, |  |

where RTstatic=O​(T)R\_{T}^{\text{static}}=O(\sqrt{T}) and RTdrift=O​(D)R\_{T}^{\text{drift}}=O(D) with DD the cumulative preference drift.
This separation enables sensitivity analysis under different investor stability regimes.

##### Empirical Validation.

We evaluate dynamic regret across both volatility shocks (Σ+30%\Sigma{+}30\%) and transaction cost shocks (τ+20%\tau{+}20\%).
Normalized regret curves RTT\tfrac{R\_{T}}{\sqrt{T}} are reported across Monte Carlo runs,
together with boxplot distributions at selected horizons.
This dual representation highlights not only the asymptotic behavior of regret
but also its finite-horizon variability across investor types.

##### Visualization.

Figures [3](https://arxiv.org/html/2510.06986v1#S5.F3 "Figure 3 ‣ Visualization. ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") and [4](https://arxiv.org/html/2510.06986v1#S5.F4 "Figure 4 ‣ Visualization. ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") together provide a rigorous view of dynamic regret.
The first figure emphasizes trajectories (median + IQR bands), while the second figure shows
distributional variation via boxplots.
Taken together, the results confirm sublinear growth, demonstrate robustness, and reveal heterogeneity across investor classes.

![Refer to caption](Fig3.png)


Figure 3: Dynamic regret trajectories across all investor types (T1–T10) under shocks (τ+20%\tau{+}20\%, Σ+30%\Sigma{+}30\%).
Each subplot reports the median trajectory (solid) and interquartile range (shaded).
Conservative investors (e.g., T1, T5) exhibit flat curves with minimal dispersion,
while ESG-oriented investors (e.g., T8–T10) display wider spreads.
These findings validate the theoretical sublinear bound and reveal heterogeneous sensitivity to shocks.

![Refer to caption](Fig4.png)


Figure 4: Distribution of normalized regret RTT\tfrac{R\_{T}}{\sqrt{T}} at selected horizons (T=20,50,100T{=}20,50,100).
Panels cover all investor types (T1–T10) under both shocks.
Boxplots highlight finite-horizon variability, with conservative investors showing concentrated distributions
and ESG-oriented investors exhibiting greater dispersion.
This complementary view strengthens the robustness of the trajectory-based findings in Figure [3](https://arxiv.org/html/2510.06986v1#S5.F3 "Figure 3 ‣ Visualization. ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").

#### 5.3.1 Coverage Probability

The inferential reliability of the inverse optimization framework
is evaluated using parametric bootstrap confidence intervals.
For each replication B=500B=500 bootstrap resamples are constructed,
and percentile intervals are computed:

|  |  |  |
| --- | --- | --- |
|  | C​I1−α​(θ^)=[θ^α/2∗,θ^1−α/2∗],CI\_{1-\alpha}(\hat{\theta})=\big[\hat{\theta}\_{\alpha/2}^{\ast},\;\hat{\theta}\_{1-\alpha/2}^{\ast}\big], |  |

where θ^p∗\hat{\theta}\_{p}^{\ast} denotes the ppth quantile of the bootstrap distribution.

##### Metrics.

Coverage probability is defined as

|  |  |  |
| --- | --- | --- |
|  | Coverage​(θ)=Pr⁡(θtrue∈C​I1−α​(θ^)),\text{Coverage}(\theta)=\Pr\big(\theta^{\text{true}}\in CI\_{1-\alpha}(\hat{\theta})\big), |  |

estimated as the empirical frequency across Monte Carlo trials.
Calibration error is measured by

|  |  |  |
| --- | --- | --- |
|  | CE​(θ)=|Coverage​(θ)−(1−α)|.\text{CE}(\theta)=\Big|\text{Coverage}(\theta)-(1-\alpha)\Big|. |  |

In addition, the expected interval length is reported,
and efficiency is defined as
Eff​(θ)=1−α𝔼​[|C​I1−α​(θ^)|]\text{Eff}(\theta)=\tfrac{1-\alpha}{\mathbb{E}[|CI\_{1-\alpha}(\hat{\theta})|]}.

##### Aggregate results.

Table [3](https://arxiv.org/html/2510.06986v1#S5.T3 "Table 3 ‣ Aggregate results. ‣ 5.3.1 Coverage Probability ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") summarizes aggregate coverage by shock and interval-length distributions.
While η\eta (ESG penalty) maintains moderate coverage,
both ρ\rho (risk aversion) and τ\tau (transaction cost) suffer from severe under-coverage.
The instability of ρ\rho is reflected in very wide and volatile intervals,
whereas τ\tau often collapses to degenerate intervals (median length zero).
Figure [5](https://arxiv.org/html/2510.06986v1#S5.F5 "Figure 5 ‣ Aggregate results. ‣ 5.3.1 Coverage Probability ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") provides a graphical overview.

Table 3: Parametric bootstrap results (B=500B=500): aggregate coverage by shock and interval-length summary across investor types (T1–T10). Min values are zero for all parameters and omitted for brevity.

| Panel A: Coverage by shock (nominal 95%) | | | |
| --- | --- | --- | --- |
| Shock | η\eta | ρ\rho | τ\tau |
| Σ+30%\Sigma{+}30\% | 0.734 | 0.391 | 0.322 |
| τ+20%\tau{+}20\% | 0.705 | 0.315 | 0.350 |

| Panel B: Interval length summary (all types) | | | | |
| --- | --- | --- | --- | --- |
| Param | Mean | Std | Median | Max |
| η\eta | 1.390 | 1.353 | 1.061 | 8.005 |
| ρ\rho | 6.974 | 6.896 | 5.898 | 38.357 |
| τ\tau | 0.279 | 0.577 | 0.000 | 3.334 |

Notes: Coverage is the empirical frequency that θtrue\theta^{\text{true}} lies in the percentile CI.
Intervals are centered at θ^\hat{\theta} with local (Type, Shock, trial) robust variance.
Values are aggregated over T1–T10.

![Refer to caption](Fig5.png)


Figure 5: Aggregate coverage probability (left) and interval-length distribution (right)
across investor types (T1–T10).

##### Heterogeneity across investor types.

Aggregate results mask considerable heterogeneity.
Table [4](https://arxiv.org/html/2510.06986v1#S5.T4 "Table 4 ‣ Heterogeneity across investor types. ‣ 5.3.1 Coverage Probability ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") reports coverage probabilities separately for each investor type.
Types T5 and T2 achieve near-nominal coverage,
whereas Types T3, T6, T7, T8, T9, and T10 exhibit severe under-coverage, especially for ρ\rho and τ\tau.
This indicates that inferential reliability is highly type-specific.
Figure [6](https://arxiv.org/html/2510.06986v1#S5.F6 "Figure 6 ‣ Heterogeneity across investor types. ‣ 5.3.1 Coverage Probability ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") visualizes these disparities,
showing both coverage and interval length paired for each type.

Table 4: Coverage by shock ×\times investor type (T1–T10).

|  | Σ+30%\Sigma{+}30\% | | | τ+20%\tau{+}20\% | | |
| --- | --- | --- | --- | --- | --- | --- |
| Type | η\eta | ρ\rho | τ\tau | η\eta | ρ\rho | τ\tau |
| T1 | 0.682 | 0.096 | 0.908 | 0.930 | 0.100 | 1.000 |
| T2 | 0.798 | 0.648 | 0.656 | 0.768 | 0.600 | 0.618 |
| T3 | 0.526 | 0.200 | 0.106 | 0.712 | 0.152 | 0.100 |
| T4 | 0.598 | 0.358 | 0.290 | 0.768 | 0.046 | 0.316 |
| T5 | 0.990 | 0.898 | 0.972 | 0.992 | 0.944 | 0.976 |
| T6 | 0.786 | 0.268 | 0.102 | 0.656 | 0.212 | 0.100 |
| T7 | 0.704 | 0.440 | 0.000 | 0.740 | 0.454 | 0.096 |
| T8 | 0.778 | 0.360 | 0.100 | 0.526 | 0.294 | 0.194 |
| T9 | 0.666 | 0.234 | 0.114 | 0.546 | 0.114 | 0.100 |
| T10 | 0.794 | 0.378 | 0.000 | 0.440 | 0.246 | 0.000 |

![Refer to caption](Fig6.png)


Figure 6: Coverage probability (top row) and interval length (bottom row) by shock across investor types (T1–T10).
Heterogeneity is evident: while η\eta remains relatively stable,
ρ\rho and τ\tau collapse for several types, underscoring the limits of bootstrap inference
under structural shocks.

#### 5.3.2 Shock Analysis: Transaction Costs vs. Volatility

We conclude the synthetic experiments by examining robustness of inverse recovery under
exogenous market shocks. Two canonical perturbations are considered:
an increase in effective transaction costs and an amplification of return volatility.
Formally, let

|  |  |  |
| --- | --- | --- |
|  | c′=(1+δ)​c,Σ′=(1+γ)​Σ,c^{\prime}=(1+\delta)c,\qquad\Sigma^{\prime}=(1+\gamma)\Sigma, |  |

with δ,γ>0\delta,\gamma>0. The corresponding welfare loss is measured by

|  |  |  |
| --- | --- | --- |
|  | Δ​Urel=𝔼​[f​(x∗​(θ,⋅))]−𝔼​[f​(x∗​(θ,⋅′))]𝔼​[|f​(x∗​(θ,⋅))|],\Delta U^{\text{rel}}=\frac{\mathbb{E}[f(x^{\*}(\theta,\cdot))]-\mathbb{E}[f(x^{\*}(\theta,\cdot^{\prime}))]}{\mathbb{E}[|f(x^{\*}(\theta,\cdot))|]}, |  |

where (θ,⋅)(\theta,\cdot) denotes baseline parameters and (θ,⋅′)(\theta,\cdot^{\prime}) the shocked environment.
Relative normalization ensures comparability across investor types and shock modalities.

##### Aggregate results.

In our design, transaction and volatility shocks are limited to δ=0.2\delta=0.2 and γ=0.3\gamma=0.3, respectively.
Thus, aggregate plots (not shown) reduce to a single point estimate per modality and provide little information
on scaling behavior. Instead, we focus on *by-type heterogeneity*, which turns out to be
substantially more informative.

##### By-type heterogeneity.

Figure [7](https://arxiv.org/html/2510.06986v1#S5.F7 "Figure 7 ‣ Interpretation. ‣ 5.3.2 Shock Analysis: Transaction Costs vs. Volatility ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") summarizes relative welfare loss across investor types (T1–T10),
with blue bars indicating transaction shocks and orange bars volatility shocks.
Several insights emerge:
(i) Types T2–T4 incur persistent welfare deterioration under both shocks, with average losses around
5–10% relative to baseline.
(ii) Types T5 and T6 remain relatively stable, exhibiting negligible average losses and tight dispersion,
consistent with their favorable coverage probabilities reported earlier.
(iii) Types T7–T10 display highly unstable responses, with wide confidence intervals and, in some cases,
negative values of Δ​Urel\Delta U^{\text{rel}}, reflecting estimation noise that produces
illusory welfare gains.

##### Interpretation.

These results reinforce the link between statistical reliability and economic robustness.
Investor types with poor bootstrap coverage (e.g., T7–T10) are also those most exposed to welfare volatility
under shocks, while types with near-nominal coverage (T2, T5) are comparatively resilient.
From a methodological perspective, this demonstrates that inferential instability
directly translates into fragility in stressed regimes.
From a financial perspective, the analysis highlights that transaction-cost shocks
tend to dominate volatility shocks in terms of welfare impact, underscoring the central role of market
liquidity in portfolio performance.

![Refer to caption](Fig7.png)


Figure 7: Relative welfare loss by investor type (T1–T10) under transaction cost (blue) and volatility (orange) shocks.
Types T2–T4 experience persistent losses, T5–T6 remain stable, while T7–T10 exhibit highly volatile responses,
illustrating the interplay between statistical reliability and economic robustness.

### 5.4 Real Data Illustration (2007–2024)

To complement the synthetic experiments, we conduct a simple real-data illustration
using exchange-traded funds (ETFs). We focus on SPY (S&P 500 benchmark)
and EEM (emerging markets), which provide long and consistent coverage since 2007.
Daily adjusted closing prices are collected from Yahoo Finance
over January 2007 to December 2024, from which log returns are computed.

##### Setup.

We apply the same mean–variance–cost utility formulation as in the synthetic analysis:

|  |  |  |
| --- | --- | --- |
|  | U​(x)=μ⊤​x−ρ2​x⊤​Σ​x−c⊤​|x|,U(x)\;=\;\mu^{\top}x\;-\;\tfrac{\rho}{2}\,x^{\top}\Sigma x\;-\;c^{\top}|x|, |  |

with equal weights, risk aversion ρ=3\rho=3, and baseline transaction cost c=0.2%c=0.2\%.
Two shocks are introduced: (i) transaction cost doubling c↦2​cc\mapsto 2c, and
(ii) volatility amplification Σ↦1.5​Σ\Sigma\mapsto 1.5\Sigma.
We divide the sample into six consecutive three-year blocks (2007–2009, 2010–2012,
2013–2015, 2016–2018, 2019–2021, 2022–2024).
For each block, we compute rolling-window estimates of mean returns and volatilities
(one-year rolling horizon) to generate a “risk–return cloud.”
The red cross marks the baseline portfolio, and the orange arrow
indicates the welfare deterioration under shocks.

![Refer to caption](Fig8.png)


Figure 8: Risk–return clouds under three-year rolling blocks (2007–2024)
using SPY (U.S. equity benchmark) and EEM (emerging markets).
Blue dots denote rolling-window estimates, the red cross marks the baseline portfolio,
and the orange arrow indicates welfare deterioration under shocks.
The dominance of transaction cost shocks over volatility shocks is consistent
across different macro-financial regimes,
including the global financial crisis, COVID period, and recent inflationary cycle.

##### Results.

Figure [8](https://arxiv.org/html/2510.06986v1#S5.F8 "Figure 8 ‣ Setup. ‣ 5.4 Real Data Illustration (2007–2024) ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") shows consistent patterns across time.
During crisis periods such as the global financial crisis (2007–2009),
the COVID shock (2019–2021), and the recent inflationary high-volatility regime (2022–2024),
baseline utility is depressed and shocks exacerbate welfare losses.
In relatively stable periods (2010–2015),
returns are higher and more stable, and shock impacts are more moderate.
Across all blocks, transaction cost shocks dominate volatility shocks in terms of
relative welfare impact, mirroring the synthetic results.

##### Discussion.

This real-data illustration reinforces the synthetic findings by showing that
liquidity frictions pose a larger threat to welfare than volatility amplification,
even across distinct macro-financial regimes.
While limited to two ETFs and equal-weight portfolios,
this exercise demonstrates that the proposed framework
is portable to real financial data.
A more comprehensive empirical study with richer asset universes
and heterogeneous investor preferences is left for future work.

## 6 Results and Discussion

### 6.1 Parameter Recovery Accuracy

Table [2](https://arxiv.org/html/2510.06986v1#S5.T2 "Table 2 ‣ 5.2.3 Visualization of Recovery Performance ‣ 5.2 Performance Metrics ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") reports estimation accuracy across R=100R=100 Monte Carlo replications.
Clear and systematic patterns emerge across investor archetypes.
For conservative investors with large values of θ\theta, estimation variance remains small because their optimal allocations
concentrate near risk-free assets. Nevertheless, even minor deviations in realized returns translate into substantial shifts in implied preferences,
generating systematic upward bias. This phenomenon reflects the classical challenge of distinguishing extreme risk aversion from corner solutions
([Cesarone et al., 2020b,](https://arxiv.org/html/2510.06986v1#bib.bib22) ; [Bertsimas et al., 2021b,](https://arxiv.org/html/2510.06986v1#bib.bib16) ).

Neutral investors with moderate values of θ\theta achieve the lowest overall mean squared error (MSE).
In this regime, both bias and variance are moderate, suggesting that the proposed inverse estimator is most reliable when investor behavior
is not dominated by extreme preferences or degeneracy.

By contrast, ESG-oriented investors (η>0\eta>0) exhibit higher dispersion.
The recovery of the ESG penalty is less precise because η\eta enters multiplicatively with θ\theta in the utility specification,
inducing correlation between risk aversion and ESG motives. This correlation reduces identifiability and produces wider variability in estimates,
a finding consistent with prior evidence on partial identifiability of interacting preference parameters (Heinkel et al.,, [2001](https://arxiv.org/html/2510.06986v1#bib.bib40); [Pastor et al., 2021b,](https://arxiv.org/html/2510.06986v1#bib.bib54) ).

Although bootstrap-based confidence intervals achieve coverage close to the nominal 95%95\% level in most regimes,
performance deteriorates under nonlinear cost misspecification (Appendix [A](https://arxiv.org/html/2510.06986v1#A1 "Appendix A Extension to Nonlinear Transaction Costs ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")).
This underscores the limitations of bootstrap inference in the presence of structural model errors,
a point also emphasized in recent discussions of robust inference in inverse optimization ([Aswani et al., 2018b,](https://arxiv.org/html/2510.06986v1#bib.bib8) ; [Dong et al., 2020b,](https://arxiv.org/html/2510.06986v1#bib.bib29) ).

### 6.2 Regret Curves

Figures [3](https://arxiv.org/html/2510.06986v1#S5.F3 "Figure 3 ‣ Visualization. ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") and [4](https://arxiv.org/html/2510.06986v1#S5.F4 "Figure 4 ‣ Visualization. ‣ 5.3 Dynamic Regret ‣ 5 Numerical Experiments ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") depict dynamic regret patterns across investor classes.
The results confirm three salient features.
First, normalized regret RT/TR\_{T}/\sqrt{T} stabilizes to a constant across all investor types,
validating the theoretical sublinear bound established in Theorem [3.2](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem2 "Theorem 3.2 (Dynamic Regret Bound). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")
and aligning with classical results in online convex optimization (Zinkevich,, [2003](https://arxiv.org/html/2510.06986v1#bib.bib63)).

Second, regret trajectories exhibit temporary spikes under volatility shocks.
These shocks elevate regret in the short run as portfolios adjust to higher dispersion,
but the long-run scaling behavior remains intact.
By contrast, transaction cost shocks produce milder effects, as they primarily rescale allocations
without fundamentally altering covariance exposure.
This asymmetry highlights that volatility amplification, rather than liquidity costs,
is the dominant driver of welfare volatility in dynamic settings (Amihud,, [2002](https://arxiv.org/html/2510.06986v1#bib.bib4); Vayanos and Wang,, [2009](https://arxiv.org/html/2510.06986v1#bib.bib62)).

Third, the degree of investor heterogeneity is evident.
Conservative investors accumulate less regret, consistent with the relative stability of their low-risk allocations,
whereas ESG-oriented investors display markedly higher dispersion.
The latter result reflects the added nonlinearity of the ESG penalty term,
which interacts with risk preferences to amplify sensitivity to shocks.
These findings reinforce the notion that heterogeneous investor motives generate differentiated regret dynamics
and must therefore be explicitly accounted for in robust portfolio design (Krueger et al.,, [2020](https://arxiv.org/html/2510.06986v1#bib.bib45); Bolton and Kacperczyk,, [2021](https://arxiv.org/html/2510.06986v1#bib.bib19)).

### 6.3 Economic Implications

The combined evidence yields several economic implications.
First, inverse recovery proves to be statistically reliable under moderate preferences,
yet becomes fragile at the extremes. This finding cautions against over-interpreting results for highly risk-averse or strongly ESG-oriented investors,
where identifiability is inherently limited.
Second, dynamic regret analysis demonstrates that estimation errors do not accumulate linearly.
Even when parameters are misspecified, long-run efficiency is preserved, indicating that the proposed approach provides stable diagnostics over time.
Third, counterfactual shock experiments reveal that welfare is far more sensitive to volatility amplification than to transaction cost inflation.
This asymmetry underscores the primacy of robust risk estimation and volatility management in safeguarding long-run welfare,
relative to transaction cost considerations.
Taken together, these results confirm that the framework delivers both rigorous statistical recovery guarantees
and economically interpretable insights that extend beyond purely technical accuracy.

### 6.4 Managerial Insights

The analysis also yields actionable lessons for portfolio managers and policy makers.
Conservative investors, characterized by high levels of risk aversion, are relatively insulated from volatility shocks,
yet they remain disproportionately vulnerable to transaction cost shocks.
This suggests that conservative mandates should be accompanied by negotiated fee structures and adequate liquidity buffers
to mitigate trading frictions.
For ESG-oriented investors, the results point to a dual role of ESG tilts:
although such allocations may entail short-term utility losses relative to neutral investors,
they enhance resilience during volatility shocks.
This supports the interpretation of ESG integration as both a reputational strategy and a resilience-enhancing hedge.
The study further shows that parameter recovery accuracy improves when systematic factors explain the bulk of return variation.
This highlights the importance of transparent disclosure of factor exposures and covariance structures,
which would allow investors and regulators to make more reliable inferences about underlying preferences.
Finally, the dynamic regret analysis indicates that estimation errors remain sublinear and do not compound over time.
Managers can therefore rely on inverse optimization–based diagnostics as a stable decision-support tool,
provided that periodic recalibration is undertaken to account for gradual preference drift.
Overall, these managerial insights demonstrate that the framework combines statistical rigor with practical decision support,
helping to inform product design, liquidity management, and principled ESG integration under uncertainty.

## 7 Conclusion

### 7.1 Summary of Contributions

This study contributes to the literature on inverse portfolio optimization in three principal ways.
*Methodologically*, it develops a unified framework capable of jointly recovering risk aversion,
transaction cost sensitivity, and ESG penalties from observed portfolio allocations.
*Empirically*, it validates the framework through controlled Monte Carlo simulations,
establishing statistical reliability (consistency, coverage, convergence) alongside economic interpretability
via welfare and regret analysis.
*Managerially*, it links methodological guarantees with actionable insights,
demonstrating how inverse recovery can inform portfolio design, liquidity management,
and ESG integration in practice.

## 8 Data Availability

The synthetic data and code used in this study are available from the authors upon reasonable request.
For transparency and reproducibility, the datasets have also been deposited in a private Kaggle repository.
Access can be granted by contacting the corresponding author.

### 8.1 Limitations

The present analysis is subject to several limitations.
First, all experiments are conducted on synthetic data, which, while providing a controlled environment to assess identifiability and robustness,
cannot fully replicate the complexity of real-world financial markets.
Second, the framework relies on stylized assumptions regarding utility specifications and transaction cost structures.
Unmodeled behavioral features—such as probability weighting, loss aversion, or ambiguity preferences—may introduce systematic deviations
from the recovery patterns documented here.
Third, the factor structure and covariance matrices are assumed to be estimated without error.
In practice, sampling variation and model misspecification in risk-factor estimation could materially affect inference.
Finally, institutional frictions such as short-sale constraints, liquidity shocks, and regulatory limits are omitted,
yet these features are known to shape observed portfolios in practice.
Addressing these limitations would be essential to establish external validity and practical relevance of the proposed framework.

### 8.2 Future Research

Future research can proceed along several directions.
First, applying the framework to real market data would provide an essential test of external validity
and reveal practical challenges in estimation, such as sampling noise and institutional frictions.
Second, integrating elements from behavioral finance—including probability weighting, reference dependence,
and ambiguity aversion—could enrich the preference space and evaluate robustness beyond quadratic utility specifications.
Third, extending the analysis to high-dimensional asset universes and incorporating distributional robustness
would enhance applicability for institutional investors, where portfolio problems involve thousands of securities
and nontrivial estimation error.
Together, these directions would strengthen both the empirical relevance and methodological scope of inverse portfolio optimization.

## References

* Acerbi and Tasche, (2002)

  Acerbi, C. and Tasche, D. (2002).
  On the coherence of expected shortfall.
  Journal of Banking & Finance, 26(7):1487–1503.
* Ahuja and Orlin, (2001)

  Ahuja, R. K. and Orlin, J. B. (2001).
  Inverse optimization.
  Operations Research, 49(5):771–783.
* Albuquerque et al., (2019)

  Albuquerque, R., Koskinen, Y., and Zhang, C. (2019).
  Corporate social responsibility and firm risk: Theory and empirical evidence.
  Management Science, 65(10):4451–4479.
* Amihud, (2002)

  Amihud, Y. (2002).
  Illiquidity and stock returns: Cross-section and time-series effects.
  Journal of Financial Markets, 5(1):31–56.
* Andrikogiannopoulou and Papakonstantinou, (2020)

  Andrikogiannopoulou, A. and Papakonstantinou, F. (2020).
  Behavioral portfolio choice with non-expected utility investors.
  Journal of Financial Economics, 136(1):176–196.
* Artzner et al., (1999)

  Artzner, P., Delbaen, F., Eber, J.-M., and Heath, D. (1999).
  Coherent measures of risk.
  Mathematical Finance, 9(3):203–228.
* (7)

  Aswani, A., Shen, Z.-J. M., and Siddiq, A. (2018a).
  Inverse optimization with noisy data.
  Operations Research, 66(3):870–892.
* (8)

  Aswani, A., Shen, Z.-J. M., and Siddiq, A. (2018b).
  Inverse optimization with noisy data.
  Operations Research, 66(3):870–892.
* Babier et al., (2021)

  Babier, A., Elmachtoub, A., and Gupta, V. (2021).
  Inverse optimization for supply chain management.
  Manufacturing & Service Operations Management, 23(4):935–952.
* Barberis, (2018)

  Barberis, N. (2018).
  Psychology-based models of asset prices and trading volume.
  Annual Review of Financial Economics, 10(1):25–52.
* Barberis et al., (2001)

  Barberis, N., Huang, M., and Santos, T. (2001).
  Prospect theory and asset prices.
  The Quarterly Journal of Economics, 116(1):1–53.
* Ben-Tal et al., (2009)

  Ben-Tal, A., El Ghaoui, L., and Nemirovski, A. (2009).
  Robust Optimization.
  Princeton University Press.
* Benartzi and Thaler, (1995)

  Benartzi, S. and Thaler, R. H. (1995).
  Myopic loss aversion and the equity premium puzzle.
  The Quarterly Journal of Economics, 110(1):73–92.
* (14)

  Bertsimas, D., Brown, D. B., and Caramanis, M. (2015a).
  Power system design under uncertainty.
  Operations Research, 63(3):509–527.
* (15)

  Bertsimas, D., Gupta, V., and Kitane, S. (2021a).
  Inverse optimization for financial portfolio models.
  Operations Research, 69(1):59–77.
* (16)

  Bertsimas, D., Gupta, V., and Kitane, S. (2021b).
  Inverse optimization for financial portfolio models.
  Operations Research, 69(1):59–77.
* (17)

  Bertsimas, D., Gupta, V., and Paschalidis, I. C. (2015b).
  Data-driven estimation in equilibrium using inverse optimization.
  Mathematical Programming, 153:595–633.
* Bianchi et al., (2019)

  Bianchi, M., Bjørnskov, C., and Smeets, P. (2019).
  The resilient investor: Personality traits and stock market participation.
  Journal of Financial Economics, 131(2):299–320.
* Bolton and Kacperczyk, (2021)

  Bolton, P. and Kacperczyk, M. (2021).
  Global pricing of carbon-transition risk.
  Review of Financial Studies, 34(3):1531–1597.
* Bruni et al., (2017)

  Bruni, R., Cesarone, F., Scozzari, A., and Tardella, F. (2017).
  A mixed-integer linear programming model for the inverse portfolio problem.
  Annals of Operations Research, 251:5–24.
* (21)

  Cesarone, F., Scozzari, A., and Tardella, F. (2020a).
  Inverse optimization models for portfolio selection.
  European Journal of Operational Research, 281(2):346–359.
* (22)

  Cesarone, F., Scozzari, A., and Tardella, F. (2020b).
  Inverse optimization models for portfolio selection.
  European Journal of Operational Research, 281(2):346–359.
* Chan et al., (2020)

  Chan, T., Gallego, G., and Simchi-Levi, D. (2020).
  Inverse optimization for transportation network models.
  Transportation Science, 54(4):923–939.
* Chan et al., (2019)

  Chan, T. C. Y., Lee, T., and Terekhov, D. (2019).
  Inverse optimization: A review with new results.
  European Journal of Operational Research, 282(1):1–16.
* Chiappori and Paiella, (2020)

  Chiappori, P.-A. and Paiella, M. (2020).
  Household risk aversion, insurance, and portfolio choices.
  American Economic Review, 110(1):335–370.
* DeMiguel et al., (2009)

  DeMiguel, V., Garlappi, L., and Uppal, R. (2009).
  Optimal versus naive diversification: How inefficient is the 1/n portfolio strategy?
  The Review of Financial Studies, 22(5):1915–1953.
* Dimmock et al., (2016)

  Dimmock, S. G., Kouwenberg, R., Mitchell, O. S., and Peijnenburg, K. (2016).
  Ambiguity aversion and household portfolio choice.
  The Review of Financial Studies, 29(4):1250–1285.
* (28)

  Dong, R., Zeng, B., and Zhang, Y. (2020a).
  Inverse optimization with noisy data.
  Operations Research, 68(1):203–220.
* (29)

  Dong, R., Zeng, B., and Zhang, Y. (2020b).
  Inverse optimization with noisy data.
  Operations Research, 68(1):203–220.
* Elmachtoub and Grigas, (2021)

  Elmachtoub, A. N. and Grigas, P. (2021).
  Smart “predict, then optimize”.
  Management Science, 67(9):5752–5774.
* Elton and Gruber, (1997)

  Elton, E. J. and Gruber, M. J. (1997).
  Modern Portfolio Theory and Investment Analysis.
  Wiley, 5th edition.
* Esfahani and Kuhn, (2018)

  Esfahani, P. M. and Kuhn, D. (2018).
  Data-driven distributionally robust optimization using the wasserstein metric: Performance guarantees and tractable reformulations.
  Mathematical Programming, 171:115–166.
* Fabozzi et al., (2007)

  Fabozzi, F. J., Gupta, F., and Markowitz, H. M. (2007).
  The Legacy of Modern Portfolio Theory.
  Wiley.
* Fabozzi et al., (2021)

  Fabozzi, F. J., Huang, D., and Zhou, G. (2021).
  Robust Portfolio Optimization and Management.
  Wiley.
* Föllmer and Schied, (2002)

  Föllmer, H. and Schied, A. (2002).
  Convex Measures of Risk and Trading Constraints.
  Springer.
* Garlappi et al., (2007)

  Garlappi, L., Uppal, R., and Wang, T. (2007).
  Portfolio selection with parameter and model uncertainty: A multi-prior approach.
  The Review of Financial Studies, 20(1):41–81.
* Gârleanu and Pedersen, (2009)

  Gârleanu, N. and Pedersen, L. H. (2009).
  Dynamic trading with predictable returns and transaction costs.
  Journal of Finance, 64(2):673–720.
* Guiso et al., (2018)

  Guiso, L., Sapienza, P., and Zingales, L. (2018).
  Time varying risk aversion.
  Journal of Financial Economics, 128(3):403–421.
* Harrison and Rutström, (2015)

  Harrison, G. W. and Rutström, E. E. (2015).
  Experimental evidence on the existence of hypothetical bias in value elicitation methods.
  Journal of Economic Behavior & Organization, 111:143–158.
* Heinkel et al., (2001)

  Heinkel, R., Kraus, A., and Zechner, J. (2001).
  The effect of green investment on corporate behavior.
  Journal of Financial and Quantitative Analysis, 36(4):431–449.
* Iyengar and Kang, (2005)

  Iyengar, G. and Kang, W. (2005).
  Inverse conic programming with applications.
  Operations Research Letters, 33(3):319–330.
* Jang and Park, (2020)

  Jang, B.-G. and Park, H.-S. (2020).
  Rebalancing costs and portfolio choice.
  Journal of Banking & Finance, 118:105867.
* Kahneman and Tversky, (1979)

  Kahneman, D. and Tversky, A. (1979).
  Prospect theory: An analysis of decision under risk.
  Econometrica, 47(2):263–291.
* Keshavarz et al., (2011)

  Keshavarz, A., Wang, Y., and Boyd, S. (2011).
  Imputing a convex objective function.
  In Proceedings of the 2011 IEEE International Symposium on Intelligent Control, pages 613–619.
* Krueger et al., (2020)

  Krueger, P., Sautner, Z., and Starks, L. T. (2020).
  The importance of climate risks for institutional investors.
  Review of Financial Studies, 33(3):1067–1111.
* Kusuoka, (2001)

  Kusuoka, S. (2001).
  On law invariant coherent risk measures.
  Advances in Mathematical Economics, 3:83–95.
* Lintner, (1965)

  Lintner, J. (1965).
  The valuation of risk assets and the selection of risky investments in stock portfolios and capital budgets.
  The Review of Economics and Statistics, 47(1):13–37.
* Liu, (2004)

  Liu, J. (2004).
  Dynamic portfolio choice and risk aversion.
  The Review of Financial Studies, 17(3):831–853.
* Markowitz, (1952)

  Markowitz, H. (1952).
  Portfolio selection.
  The Journal of Finance, 7(1):77–91.
* Meucci, (2009)

  Meucci, A. (2009).
  Risk and Asset Allocation.
  Springer.
* Müller, (2025)

  Müller, T. (2025).
  Sustainable portfolio optimization under esg uncertainty.
  Journal of Financial Economics.
  forthcoming.
* Pastor and Stambaugh, (2003)

  Pastor, L. and Stambaugh, R. F. (2003).
  Liquidity risk and expected stock returns.
  Journal of Political Economy, 111(3):642–685.
* (53)

  Pastor, L., Stambaugh, R. F., and Taylor, L. A. (2021a).
  Sustainable investing in equilibrium.
  Journal of Financial Economics, 142(2):550–571.
* (54)

  Pastor, L., Stambaugh, R. F., and Taylor, L. A. (2021b).
  Sustainable investing in equilibrium.
  Journal of Financial Economics, 142(2):550–571.
* Pedersen et al., (2021)

  Pedersen, L. H., Fitzgibbons, S., and Pomorski, L. (2021).
  Responsible investing: The esg-efficient frontier.
  Journal of Financial Economics, 142(2):572–597.
* Ren et al., (2025)

  Ren, Y., Li, F., and Zhou, M. (2025).
  Learning feasible regions in inverse optimization.
  Mathematical Programming.
  forthcoming.
* Rockafellar and Uryasev, (2000)

  Rockafellar, R. T. and Uryasev, S. (2000).
  Optimization of conditional value-at-risk.
  Journal of Risk, 2(3):21–42.
* Ruiz et al., (2013)

  Ruiz, C., Conejo, A. J., and Carrion, M. (2013).
  On the value of inverse optimization in electricity markets.
  IEEE Transactions on Power Systems, 28(3):3382–3391.
* Shafieezadeh-Abadeh et al., (2019)

  Shafieezadeh-Abadeh, S., Kuhn, D., and Esfahani, P. M. (2019).
  Regularization via mass transportation: Theory and applications.
  Mathematics of Operations Research, 44(2):565–600.
* Truong and Chan, (2020)

  Truong, L. and Chan, T. C. Y. (2020).
  Inverse optimization for healthcare resource allocation.
  Health Care Management Science, 23(2):151–167.
* Tversky and Kahneman, (1992)

  Tversky, A. and Kahneman, D. (1992).
  Advances in prospect theory: Cumulative representation of uncertainty.
  Journal of Risk and Uncertainty, 5(4):297–323.
* Vayanos and Wang, (2009)

  Vayanos, D. and Wang, J. (2009).
  Liquidity and asset prices: A unified framework.
  Journal of Financial Economics, 94(3):497–518.
* Zinkevich, (2003)

  Zinkevich, M. (2003).
  Online convex programming and generalized infinitesimal gradient ascent.
  In Proceedings of the 20th International Conference on Machine Learning (ICML), pages 928–936.

## Appendix

## Appendix A Extension to Nonlinear Transaction Costs

We generalize the forward problem by replacing the linear cost c⊤​xc^{\top}x with a convex nonlinear function

|  |  |  |
| --- | --- | --- |
|  | ϕ​(x)=∑j=1nκj​|xj|p,p≥1,κj>0.\phi(x)=\sum\_{j=1}^{n}\kappa\_{j}|x\_{j}|^{p},\qquad p\geq 1,\;\;\kappa\_{j}>0. |  |

The forward problem becomes

|  |  |  |
| --- | --- | --- |
|  | maxx∈𝒳⁡μ⊤​x−θ2​x⊤​Σ​x−ϕ​(x).\max\_{x\in\mathcal{X}}\;\mu^{\top}x-\tfrac{\theta}{2}x^{\top}\Sigma x-\phi(x). |  |

### A.1 KKT and VI Formulation

The Lagrangian of the nonlinear forward problem is

|  |  |  |
| --- | --- | --- |
|  | ℒ​(x,λ,ν)=μ⊤​x−θ2​x⊤​Σ​x−ϕ​(x)+λ​(1−𝟏⊤​x)+ν⊤​x,\mathcal{L}(x,\lambda,\nu)=\mu^{\top}x-\tfrac{\theta}{2}x^{\top}\Sigma x-\phi(x)+\lambda(1-\mathbf{1}^{\top}x)+\nu^{\top}x, |  |

with multipliers λ∈ℝ\lambda\in\mathbb{R} and ν∈ℝ≥0n\nu\in\mathbb{R}^{n}\_{\geq 0}.
The corresponding KKT conditions are

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ−θ​Σ​x∗−∇ϕ​(x∗)−λ​𝟏+ν\displaystyle\mu-\theta\Sigma x^{\*}-\nabla\phi(x^{\*})-\lambda\mathbf{1}+\nu | =0,\displaystyle=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏⊤​x∗\displaystyle\mathbf{1}^{\top}x^{\*} | =1,\displaystyle=1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ν≥0,x∗≥0,νi​xi∗\displaystyle\nu\geq 0,\quad x^{\*}\geq 0,\quad\nu\_{i}x\_{i}^{\*} | =0,∀i.\displaystyle=0,\;\forall i. |  |

Equivalently, these conditions define a variational inequality:

|  |  |  |
| --- | --- | --- |
|  | ⟨θ​Σ​x∗+∇ϕ​(x∗)−μ,x−x∗⟩≥0∀x∈𝒳.\langle\theta\Sigma x^{\*}+\nabla\phi(x^{\*})-\mu,\;x-x^{\*}\rangle\geq 0\quad\forall x\in\mathcal{X}. |  |

### A.2 Examples of Nonlinear Costs

* •

  p=1p=1: proportional ℓ1\ell\_{1} transaction costs (sparsity-inducing).
* •

  p=2p=2: quadratic penalty, modeling illiquidity or portfolio adjustment frictions.
* •

  mixed-norm costs: ϕ​(x)=κ1​‖x‖1+κ2​‖x‖22\phi(x)=\kappa\_{1}\|x\|\_{1}+\kappa\_{2}\|x\|\_{2}^{2}.

All cases preserve convexity and lead to tractable convex optimization problems.

### A.3 Identifiability under Nonlinear Costs

Stationarity now reads

|  |  |  |
| --- | --- | --- |
|  | θ​Σ​x∗+∇ϕ​(x∗)=μ−λ​𝟏+ν.\theta\Sigma x^{\*}+\nabla\phi(x^{\*})=\mu-\lambda\mathbf{1}+\nu. |  |

Since ∇ϕ​(x∗)\nabla\phi(x^{\*}) is monotone in x∗x^{\*} for convex ϕ\phi, variation across observed (μt,Σt)(\mu^{t},\Sigma^{t}) ensures that θ\theta can still be separated from ϕ\phi up to normalization.

Proposition A.1 (Identifiability with Nonlinear Costs).
Suppose (i) ϕ\phi is convex and differentiable, (ii) Σt≻0\Sigma^{t}\succ 0 for all tt, and (iii) at least two distinct active sets occur across {xt}\{x^{t}\}.
Then (θ,κ)(\theta,\kappa) is uniquely identifiable up to scale normalization.

Proof Sketch.
The mapping x↦∇ϕ​(x)x\mapsto\nabla\phi(x) is monotone. Distinct active sets provide variation in Σt​xt\Sigma^{t}x^{t} and ∇ϕ​(xt)\nabla\phi(x^{t}), which allows unique recovery of θ\theta once normalization fixes the scale. □\square

### A.4 Implications

Nonlinear transaction costs capture realistic frictions (e.g., liquidity impact, proportional fees, or ESG penalties).
Our framework demonstrates that inverse recovery extends naturally:
the role of cc in the linear case is replaced by ∇ϕ​(x)\nabla\phi(x) in the nonlinear case, without altering the convexity or identifiability logic.

## Appendix B Distributionally Robust Extension

We now allow for uncertainty in (μ,Σ)(\mu,\Sigma) to account for estimation error and model misspecification. Define an uncertainty set

|  |  |  |
| --- | --- | --- |
|  | 𝒰={(μ,Σ):‖μ−μ¯‖2≤δμ,‖Σ−Σ¯‖F≤δΣ,Σ⪰0}.\mathcal{U}=\left\{(\mu,\Sigma):\|\mu-\bar{\mu}\|\_{2}\leq\delta\_{\mu},\;\|\Sigma-\bar{\Sigma}\|\_{F}\leq\delta\_{\Sigma},\;\;\Sigma\succeq 0\right\}. |  |

### B.1 Robust Forward Problem

The robust forward problem is

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈𝒳⁡min(μ,Σ)∈𝒰⁡{μ⊤​x−θ2​x⊤​Σ​x−c⊤​x}.\max\_{x\in\mathcal{X}}\min\_{(\mu,\Sigma)\in\mathcal{U}}\left\{\mu^{\top}x-\tfrac{\theta}{2}x^{\top}\Sigma x-c^{\top}x\right\}. |  | (44) |

The inner minimization admits a tractable conic reformulation:

|  |  |  |
| --- | --- | --- |
|  | min(μ,Σ)∈𝒰⁡μ⊤​x−θ2​x⊤​Σ​x=μ¯⊤​x−δμ​‖x‖2−θ2​x⊤​Σ¯​x−θ2​δΣ​‖x​x⊤‖F.\min\_{(\mu,\Sigma)\in\mathcal{U}}\;\mu^{\top}x-\tfrac{\theta}{2}x^{\top}\Sigma x=\bar{\mu}^{\top}x-\delta\_{\mu}\|x\|\_{2}-\tfrac{\theta}{2}x^{\top}\bar{\Sigma}x-\tfrac{\theta}{2}\delta\_{\Sigma}\|xx^{\top}\|\_{F}. |  |

Hence, the robust forward objective can be expressed as

|  |  |  |
| --- | --- | --- |
|  | frob​(x;μ¯,Σ¯,θ,c,δμ,δΣ)=μ¯⊤​x−δμ​‖x‖2−θ2​x⊤​Σ¯​x−θ2​δΣ​‖x​x⊤‖F−c⊤​x.f\_{\text{rob}}(x;\bar{\mu},\bar{\Sigma},\theta,c,\delta\_{\mu},\delta\_{\Sigma})=\bar{\mu}^{\top}x-\delta\_{\mu}\|x\|\_{2}-\tfrac{\theta}{2}x^{\top}\bar{\Sigma}x-\tfrac{\theta}{2}\delta\_{\Sigma}\|xx^{\top}\|\_{F}-c^{\top}x. |  |

### B.2 KKT/VI Characterization

The optimal xrob∗x^{\*}\_{\text{rob}} satisfies a robust KKT system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ¯−δμ​x∗‖x∗‖2−θ​Σ¯​x∗−θ​δΣ​vec​(x​x⊤)​∇x‖x​x⊤‖F−c−λ​𝟏+ν=0,\displaystyle\bar{\mu}-\delta\_{\mu}\frac{x^{\*}}{\|x^{\*}\|\_{2}}-\theta\bar{\Sigma}x^{\*}-\theta\delta\_{\Sigma}\,\mathrm{vec}(xx^{\top})\nabla\_{x}\|xx^{\top}\|\_{F}-c-\lambda\mathbf{1}+\nu=0, |  | (45) |

together with feasibility and complementary slackness.
Equivalently, xrob∗x^{\*}\_{\text{rob}} solves the variational inequality

|  |  |  |
| --- | --- | --- |
|  | ⟨θ​Σ¯​x∗+θ​δΣ​G​(x∗)+c−μ¯+δμ​x∗‖x∗‖2,x−x∗⟩≥0,∀x∈𝒳,\langle\theta\bar{\Sigma}x^{\*}+\theta\delta\_{\Sigma}G(x^{\*})+c-\bar{\mu}+\delta\_{\mu}\tfrac{x^{\*}}{\|x^{\*}\|\_{2}},\;x-x^{\*}\rangle\geq 0,\quad\forall x\in\mathcal{X}, |  |

where G​(x)G(x) is the gradient of ‖x​x⊤‖F\|xx^{\top}\|\_{F}.

### B.3 Identifiability under Robustness

Proposition B.1 (Robust Identifiability).
Suppose 𝒰\mathcal{U} is bounded, Σ¯≻0\bar{\Sigma}\succ 0, and at least two distinct active sets occur across {xt}\{x^{t}\}. Then (θ,c)(\theta,c) are identifiable up to scale even in the distributionally robust formulation.

Proof Sketch.
Stationarity links θ​Σ¯​x∗\theta\bar{\Sigma}x^{\*} and the robust correction terms δμ​‖x‖2,δΣ​‖x​x⊤‖F\delta\_{\mu}\|x\|\_{2},\delta\_{\Sigma}\|xx^{\top}\|\_{F}. Since these terms are deterministic functions of x∗x^{\*} and vary with observed active sets, θ\theta and cc can still be separated once normalization is imposed. □\square

### B.4 Practical Implications

The robust formulation reflects how practitioners hedge against parameter uncertainty.
Inverse recovery under robustness is thus more stable and less sensitive to noisy (μ,Σ)(\mu,\Sigma) estimates.
Comparative statics with δμ,δΣ\delta\_{\mu},\delta\_{\Sigma} quantify how parameter recovery degrades with higher estimation error, which provides actionable guidance on required data quality and sample size.

## Appendix C Proofs of Theoretical Results

### C.1 Proof of Theorem [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem1 "Theorem 3.1 (Identifiability). ‣ 3.4.2 Formal Theorem ‣ 3.4 Identifiability ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") (Identifiability)

Theorem [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem1 "Theorem 3.1 (Identifiability). ‣ 3.4.2 Formal Theorem ‣ 3.4 Identifiability ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").
Suppose (i) Σt≻0\Sigma^{t}\succ 0 for all tt, (ii) {(μt,Σt)}t=1T\{(\mu^{t},\Sigma^{t})\}\_{t=1}^{T} yield at least two distinct active sets, and (iii) a normalization on (θ,c)(\theta,c) is imposed. Then (θ,c)(\theta,c) is uniquely identifiable.

Proof.
From the stationarity condition ([7](https://arxiv.org/html/2510.06986v1#S3.E7 "In 3.3.1 KKT System ‣ 3.3 Optimality Conditions ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")), for each tt we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​Σt​xt+c=μt−λt​𝟏+νt,\theta\Sigma^{t}x^{t}+c=\mu^{t}-\lambda^{t}\mathbf{1}+\nu^{t}, |  | (46) |

with λt∈ℝ\lambda^{t}\in\mathbb{R} and νt≥0\nu^{t}\geq 0 satisfying complementary slackness.
Since Σt≻0\Sigma^{t}\succ 0, the mapping xt↦Σt​xtx^{t}\mapsto\Sigma^{t}x^{t} is injective, which ensures that θ\theta appears only as a multiplicative factor on Σt​xt\Sigma^{t}x^{t} and cannot be confounded with shifts in cc.
If all observations shared the same active set, νt\nu^{t} could adjust in the same coordinates, preventing separation of θ\theta and cc.
However, the existence of distinct active sets forces changes in the right-hand side of ([46](https://arxiv.org/html/2510.06986v1#A3.E46 "In C.1 Proof of Theorem 3.1 (Identifiability) ‣ Appendix C Proofs of Theoretical Results ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")) that uniquely determine cc.
Finally, without normalization, scaling (θ,c)(\theta,c) by a common factor could reproduce the same xtx^{t}, but imposing a normalization such as ‖c‖2=1\|c\|\_{2}=1 or bounding θ∈[0,θmax]\theta\in[0,\theta\_{\max}] removes this indeterminacy.
Therefore, if (θ1,c1)(\theta\_{1},c\_{1}) and (θ2,c2)(\theta\_{2},c\_{2}) both satisfy ([46](https://arxiv.org/html/2510.06986v1#A3.E46 "In C.1 Proof of Theorem 3.1 (Identifiability) ‣ Appendix C Proofs of Theoretical Results ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")), we obtain

|  |  |  |
| --- | --- | --- |
|  | (θ1−θ2)​Σt​xt+(c1−c2)=0,∀t.(\theta\_{1}-\theta\_{2})\Sigma^{t}x^{t}+(c\_{1}-c\_{2})=0,\quad\forall t. |  |

Because {Σt​xt}\{\Sigma^{t}x^{t}\} span a non-degenerate set under the assumptions, the only solution is θ1=θ2\theta\_{1}=\theta\_{2} and c1=c2c\_{1}=c\_{2} (up to normalization).
Hence (θ,c)(\theta,c) are uniquely identifiable, and the inverse optimization estimator in ([4](https://arxiv.org/html/2510.06986v1#S3.E4 "In 3.2.2 Inverse Optimization Objective ‣ 3.2 Inverse Problem ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")) has a well-defined target.
□\square

### C.2 Proof of Proposition [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmproposition1 "Proposition 3.1 (Consistency). ‣ 3.6 Consistency and Robustness Results ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") (Consistency)

Proposition [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmproposition1 "Proposition 3.1 (Consistency). ‣ 3.6 Consistency and Robustness Results ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").
Suppose observed portfolios {xt}\{x^{t}\} are generated from the forward problem
([2](https://arxiv.org/html/2510.06986v1#S3.E2 "In 3.1.2 Objective Function ‣ 3.1 Forward Problem ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")) with true parameters (θ∗,c∗)(\theta^{\ast},c^{\ast}), and that
(i) the parameter space Θ\Theta is compact,
(ii) LT​(θ)L\_{T}(\theta) is continuous in θ\theta, and
(iii) {(μt,Σt)}\{(\mu^{t},\Sigma^{t})\} are i.i.d. draws with sufficient variation to ensure identifiability (Theorem [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem1 "Theorem 3.1 (Identifiability). ‣ 3.4.2 Formal Theorem ‣ 3.4 Identifiability ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty")).
Then the inverse estimator

|  |  |  |
| --- | --- | --- |
|  | θ^=arg⁡minθ∈Θ⁡LT​(θ),LT​(θ)=1T​∑t=1T‖xt−x∗​(θ)‖2,\hat{\theta}=\arg\min\_{\theta\in\Theta}L\_{T}(\theta),\quad L\_{T}(\theta)=\frac{1}{T}\sum\_{t=1}^{T}\|x^{t}-x^{\*}(\theta)\|^{2}, |  |

is consistent: θ^→pθ∗\hat{\theta}\to\_{p}\theta^{\ast} as T→∞T\to\infty.

Proof.
Define the population loss

|  |  |  |
| --- | --- | --- |
|  | L​(θ)=𝔼​[‖xt−x∗​(θ)‖2],L(\theta)=\mathbb{E}\big[\|x^{t}-x^{\*}(\theta)\|^{2}\big], |  |

where the expectation is taken with respect to the distribution of (μt,Σt)(\mu^{t},\Sigma^{t}).
By the uniform law of large numbers, if Θ\Theta is compact and LT​(θ)L\_{T}(\theta) is continuous in θ\theta, then

|  |  |  |
| --- | --- | --- |
|  | supθ∈Θ|LT​(θ)−L​(θ)|→p0,\sup\_{\theta\in\Theta}|L\_{T}(\theta)-L(\theta)|\to\_{p}0, |  |

so that the empirical loss converges uniformly to its population counterpart.
By Theorem [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem1 "Theorem 3.1 (Identifiability). ‣ 3.4.2 Formal Theorem ‣ 3.4 Identifiability ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty"), the population loss L​(θ)L(\theta) is uniquely minimized at θ∗\theta^{\ast}, which ensures that θ∗\theta^{\ast} is the well-defined target of estimation.
Finally, by the argmin consistency theorem of Newey and McFadden (1994, Theorem 2.1), uniform convergence together with uniqueness of the minimizer implies that

|  |  |  |
| --- | --- | --- |
|  | θ^→𝑝θ∗,T→∞.\hat{\theta}\;\xrightarrow{p}\;\theta^{\ast},\qquad T\to\infty. |  |

This establishes the consistency of the inverse estimator. □\square

### C.3 Proof of Lemma [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmlemma1 "Lemma 3.1 (Robustness to Misspecification). ‣ 3.6 Consistency and Robustness Results ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") (Robustness to Misspecification)

Lemma [3.1](https://arxiv.org/html/2510.06986v1#S3.Thmlemma1 "Lemma 3.1 (Robustness to Misspecification). ‣ 3.6 Consistency and Robustness Results ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").
Let the true transaction cost be ϕ​(x)\phi(x), convex and homogeneous of degree p∈[1,2]p\in[1,2], while the researcher estimates with a linear cost c⊤​xc^{\top}x.
Define the approximation error

|  |  |  |
| --- | --- | --- |
|  | ε=supx∈𝒳|ϕ​(x)−c⊤​x|.\varepsilon=\sup\_{x\in\mathcal{X}}\big|\phi(x)-c^{\top}x\big|. |  |

Then the inverse optimization estimator (θ^,c^)(\hat{\theta},\hat{c}) satisfies

|  |  |  |
| --- | --- | --- |
|  | ‖(θ^,c^)−(θ∗,c∗)‖=O​(ε).\|(\hat{\theta},\hat{c})-(\theta^{\ast},c^{\ast})\|=O(\varepsilon). |  |

Proof.
The true forward objective is

|  |  |  |
| --- | --- | --- |
|  | ftrue​(x;θ)=μ⊤​x−θ2​x⊤​Σ​x−ϕ​(x),f\_{\text{true}}(x;\theta)=\mu^{\top}x-\tfrac{\theta}{2}x^{\top}\Sigma x-\phi(x), |  |

while the approximated forward objective used in estimation is

|  |  |  |
| --- | --- | --- |
|  | flin​(x;θ,c)=μ⊤​x−θ2​x⊤​Σ​x−c⊤​x.f\_{\text{lin}}(x;\theta,c)=\mu^{\top}x-\tfrac{\theta}{2}x^{\top}\Sigma x-c^{\top}x. |  |

By definition of ε\varepsilon, the two objectives differ uniformly by at most ε\varepsilon on the feasible set 𝒳\mathcal{X}:

|  |  |  |
| --- | --- | --- |
|  | |ftrue​(x;θ)−flin​(x;θ,c)|≤ε∀x∈𝒳.|f\_{\text{true}}(x;\theta)-f\_{\text{lin}}(x;\theta,c)|\leq\varepsilon\quad\forall x\in\mathcal{X}. |  |

Because both are convex maximization problems over a compact set, their solutions are Lipschitz-stable with respect to perturbations in the objective (Bonnans and Shapiro, 2000, Ch. 4).
Hence the optimizers xtrue∗x^{\ast}\_{\text{true}} and xlin∗x^{\ast}\_{\text{lin}} satisfy

|  |  |  |
| --- | --- | --- |
|  | ‖xtrue∗−xlin∗‖=O​(ε).\|x^{\ast}\_{\text{true}}-x^{\ast}\_{\text{lin}}\|=O(\varepsilon). |  |

Since the inverse estimator minimizes the squared deviation between observed portfolios (generated under ϕ\phi) and model-implied portfolios (generated under c⊤​xc^{\top}x), the parameter estimates (θ^,c^)(\hat{\theta},\hat{c}) inherit the same order of error.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | ‖(θ^,c^)−(θ∗,c∗)‖=O​(ε).\|(\hat{\theta},\hat{c})-(\theta^{\ast},c^{\ast})\|=O(\varepsilon). |  |

This establishes the robustness claim. □\square

### C.4 Proof of Theorem [3.2](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem2 "Theorem 3.2 (Dynamic Regret Bound). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") (Dynamic Regret Bound)

Theorem [3.2](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem2 "Theorem 3.2 (Dynamic Regret Bound). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").
Assume (i) the forward objective f​(x;θ)f(x;\theta) is convex in xx for each θ\theta,
(ii) the mapping θ↦x∗​(θ)\theta\mapsto x^{\*}(\theta) is Lipschitz with constant LxL\_{x}, and
(iii) the preference sequence {θt}\{\theta\_{t}\} has bounded drift

|  |  |  |
| --- | --- | --- |
|  | ∑t=2T‖θt−θt−1‖≤D.\sum\_{t=2}^{T}\|\theta\_{t}-\theta\_{t-1}\|\leq D. |  |

Then the dynamic regret

|  |  |  |
| --- | --- | --- |
|  | RT=∑t=1Tf​(x∗​(θttrue))−f​(x∗​(θ^t))R\_{T}=\sum\_{t=1}^{T}f(x^{\*}(\theta\_{t}^{\text{true}}))-f(x^{\*}(\hat{\theta}\_{t})) |  |

satisfies

|  |  |  |
| --- | --- | --- |
|  | RT≤O​(T+D).R\_{T}\leq O(\sqrt{T}+D). |  |

Proof.
If θt\theta\_{t} is constant, the problem reduces to online convex optimization with a fixed comparator x∗​(θ)x^{\*}(\theta), for which classical results (Zinkevich, 2003) yield RT=O​(T)R\_{T}=O(\sqrt{T}).
For varying θt\theta\_{t}, regret can be decomposed into a static component relative to a fixed comparator and a drift component reflecting parameter changes.
By Lipschitz continuity of f​(x∗​(θ))f(x^{\*}(\theta)) in θ\theta, each change ‖θt−θt−1‖\|\theta\_{t}-\theta\_{t-1}\| contributes at most O​(‖θt−θt−1‖)O(\|\theta\_{t}-\theta\_{t-1}\|) to regret, so the cumulative drift term is bounded by O​(D)O(D).
Combining the static O​(T)O(\sqrt{T}) bound with the drift bound gives

|  |  |  |
| --- | --- | --- |
|  | RT≤O​(T+D).R\_{T}\leq O(\sqrt{T}+D). |  |

This establishes the theorem. □\square

### C.5 Proof of Corollary [1](https://arxiv.org/html/2510.06986v1#Thmcorollary1 "Corollary 1 (Static Preferences). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") (Static Preferences)

Corollary [1](https://arxiv.org/html/2510.06986v1#Thmcorollary1 "Corollary 1 (Static Preferences). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty").
If preferences are constant, i.e. θt=θ∗\theta\_{t}=\theta^{\ast} for all tt, then the drift term vanishes (D=0)(D=0).
In this case, the dynamic regret bound simplifies to

|  |  |  |
| --- | --- | --- |
|  | RT=O​(T).R\_{T}=O(\sqrt{T}). |  |

Proof.
Setting D=0D=0 in Theorem [3.2](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem2 "Theorem 3.2 (Dynamic Regret Bound). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") removes the drift contribution, leaving only the static component O​(T)O(\sqrt{T}).
Hence, under static preferences, the regret matches the classical sublinear bound in online convex optimization. □\square

Implication.
This corollary shows that our inverse estimator achieves sublinear regret in the classical static setting, fully consistent with standard OCO theory.
It also confirms that Theorem [3.2](https://arxiv.org/html/2510.06986v1#S3.Thmtheorem2 "Theorem 3.2 (Dynamic Regret Bound). ‣ 3.7 Dynamic Extension and Regret Bounds ‣ 3 Model Formulation ‣ Inverse Portfolio Optimization with Synthetic Investor Data: Recovering Risk Preferences under Uncertainty") generalizes the well-known static case.

## Appendix D Experimental Setup and Implementation Details

### Computing Environment

All simulations were executed on a workstation with the following configuration:

* •

  Hardware: NVIDIA RTX GPU, multi-core CPU, 128 GB RAM
* •

  Operating System: Ubuntu 22.04.5 LTS under Windows Subsystem for Linux 2 (WSL2)
* •

  Software: Python 3.10 (conda environment)
* •

  Libraries: cvxpy 1.7.2 with OSQP, numpy, scipy

### Simulation Scale

* •

  Number of assets: n=10n=10
* •

  Number of systematic factors: k=3k=3
* •

  Time periods per trial: T=100T=100
* •

  Monte Carlo replications: R=200R=200
* •

  Total portfolio problems solved: R×T=20,000R\times T=20{,}000

### Notes on Reproducibility

* •

  Random seeds were fixed per replication.
* •

  All code was executed in Jupyter Notebook under WSL2.
* •

  Source code and notebooks are available from the authors upon request.