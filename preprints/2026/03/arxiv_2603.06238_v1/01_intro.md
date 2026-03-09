---
authors:
- Jean-Loup Dupret
- Edouard Motte
doc_id: arxiv:2603.06238v1
family_id: arxiv:2603.06238
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: General Bounds on Functionals of the Lifetime under Life Table Constraints
url_abs: http://arxiv.org/abs/2603.06238v1
url_html: https://arxiv.org/html/2603.06238v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jean-Loup Dupret

Edouard Motte

###### Abstract

In life insurance, life tables are used to estimate the survival distribution of individuals from a given population. However, these tables only provide survival probabilities at integer ages but no information about the distribution of deaths between two consecutive integer values. Many actuarial quantities, such as variable annuities, are functionals of the lifetime and computing them requires full information about mortality rates. One frequent solution is to postulate fractional age assumptions or mortality rate models, but it turns out that the results of the computations strongly depend on these assumptions, which makes it difficult to generalize them. We hence derive upper and lower bounds of functionals of the lifetime with respect to mortality rates, which are compatible with the observed life table at integer ages. We derive two sets of results under distinct assumptions. In the first, we assume that each mortality trajectory is almost surely consistent with all the given one-year survival probabilities from the table. In the second, we consider a relaxed formulation that allows for deviations of the mortality rates while still being consistent in expectation with the given one-year reference survival probabilities. These distinct yet complementary approaches provide a new robust framework for managing mortality risk in life insurance. They characterize the worst- and best-case contract values over all mortality processes that remain compatible with the observed life-table information, thereby enabling insurers to quantify the impact on prices of deviations of the observed mortality rates from their mortality assumptions/models.

###### keywords:

Mortality modeling , Stochastic optimal control , Variable annuities , Life insurance , Risk management

\affiliation

[inst1]organization=Department of Mathematics and RiskLab, ETH Zurich,addressline=Rämistrasse 101,
city=Zurich,
postcode=8092,
country=Switzerland
\affiliation[inst2]organization=LIDAM-ISBA, Université Catholique de Louvain,city=Louvain-la-Neuve,
postcode=1348,
country=Belgium

## 1 Introduction

The two most common approaches to mortality modeling in life insurance rely either on fractional age assumptions or mortality rate models. Each provides a way to derive survival probabilities over continuous time, yet both come with inherent limitations.
  
  
(i) Fractional age assumptions. In practice, life insurers and pension funds often rely on life tables, which provide the survival probabilities of individuals at integer ages. However, many actuarial quantities (life annuities, variable annuities, or other functionals of the lifetime) depend on the full distribution of survival times, which requires information about the distribution of deaths between integer ages. To address this, actuaries introduce fractional age assumptions that interpolate survival probabilities between successive integer ages, see Chapter 3.6 of Bowers et al. ([1997](#bib.bib25 "Actuarial mathematics")) and Chapter 3 of Dickson et al. ([2020](#bib.bib2 "Actuarial mathematics for life contingent risks")). The most common assumptions are the uniform distribution of deaths (UDD) assuming that deaths occur uniformly over each one-year interval; the constant force of mortality (CFM) with an exponential decay of the survival function within each interval; and the Balducci assumption under which the probability of death decreases linearly with time over each year. Each of these assumptions produces a different continuous-time survival distribution consistent with the same life table at integer ages. However, since life tables provide no information about the actual distribution of deaths between integer ages, the resulting actuarial quantities depend heavily on the chosen assumption, which introduces a structural source of model risk that is rarely quantified by insurers.
  
  
(ii) Mortality rate models. An alternative approach to fractional age assumptions is to model mortality continuously in time through a mortality rate, or force of mortality, μx​(t)\mu\_{x}(t) at initial age xx
and to derive the corresponding survival function Sx​(t)=exp⁡(−∫0tμx​(s)​𝑑s)S\_{x}(t)=\exp\left(-\int\_{0}^{t}\mu\_{x}(s)ds\right). Deterministic mortality laws, such as the Gompertz–Makeham (Gompertz, [1825](#bib.bib16 "On the nature of the function expressive of the law of human mortality, and on a new mode of determining the value of life contingencies"), Makeham, [1860](#bib.bib17 "On the law of mortality and the construction of annuity tables")) or Heligman–Pollard models (Heligman and Pollard, [1980](#bib.bib18 "The age pattern of mortality")), model μx​(t)\mu\_{x}(t) as a smooth function of time tt and provide analytical tractability for pricing and reserving purposes. More recent developments have introduced stochastic mortality models to capture systematic longevity trends and uncertainty in future mortality evolution. Notable examples include the Lee–Carter models (Lee and Carter, [1992](#bib.bib19 "Modeling and forecasting U.S. mortality"), Booth et al., [2002](#bib.bib33 "Applying Lee-Carter under conditions of variable mortality decline"), Renshaw and Haberman, [2003](#bib.bib29 "Lee–Carter mortality forecasting with age-specific enhancement")), the Cairns–Blake–Dowd (CBD) model (Cairns et al., [2006](#bib.bib20 "A two-factor model for stochastic mortality with parameter uncertainty: theory and calibration"), [2009](#bib.bib31 "A quantitative comparison of stochastic mortality models using data from England and Wales and the United States")), and cohort-based extensions such as the Renshaw–Haberman model (Renshaw and Haberman, [2006](#bib.bib21 "A cohort-based extension to the Lee–Carter model for mortality reduction factors"), Currie, [2006](#bib.bib34 "Smoothing and forecasting mortality rates with P-splines")) or multi-population approaches (Li and Lee, [2005](#bib.bib22 "Coherent mortality forecasts for a group of populations: an extension of the Lee–Carter model")), see also Plat ([2009](#bib.bib32 "On stochastic mortality modeling")) and Basellini et al. ([2023](#bib.bib23 "Thirty years on: a review of the Lee–Carter method for forecasting mortality")) for a thorough review on stochastic mortality modeling. These models specify continuous-time dynamics for mortality rates, enabling longevity risk management in a probabilistic framework. While both deterministic and stochastic mortality rate models define survival probabilities continuously for all t≥0t\geq 0, they are inherently model-based: their dynamics rely on parametric and structural assumptions about the underlying mortality process. Consequently, computed actuarial functionals of the lifetime depend strongly on these modeling choices, and different specifications can lead to substantially different valuations of life-contingent liabilities.
  
  
In this paper, we propose a framework that avoids both sources of model misspecification, namely, the arbitrary choice of fractional age assumption and the structural assumptions of mortality rate models. Instead, we derive upper and lower bounds for actuarial functionals of the lifetime that are compatible with the observed life table at integer ages. Our approach characterizes all possible mortality rates consistent with these discrete data points, and determines the corresponding optimal values of actuarial quantities such as variable annuities. We present two complementary formulations: a strict setting in which each mortality path must match almost surely all the one-year survival probabilities given by the reference life table, and a relaxed (more realistic) setting in which this constraint only holds in expectation, allowing for mortality trajectories to deviate while still being consistent on average with each one-year tabulated survival probabilities. More precisely, for a fixed maturity T>0T>0 and a risk-neutral measure ℚ\mathbb{Q}, we aim at solving stochastic control problems of the form

|  |  |  |
| --- | --- | --- |
|  | supμ∈𝒜𝔼ℚ​[F​(T,μ,A,r)]andinfμ∈𝒜𝔼ℚ​[F​(T,μ,A,r)],\sup\_{\mu\in\mathcal{A}}\mathbb{E}^{\mathbb{Q}}\left[F(T,\mu,A,r)\right]\quad\ \text{and}\quad\ \inf\_{\mu\in\mathcal{A}}\mathbb{E}^{\mathbb{Q}}\left[F(T,\mu,A,r)\right], |  |

for some functional FF of the lifetime111Strictly speaking, functional of the mortality rates, but we interchangeably use these terms when it is clear from the context. μ=(μt)0≤t≤T\mu=(\mu\_{t})\_{0\leq t\leq T}, investment fund A=(At)0≤t≤TA=(A\_{t})\_{0\leq t\leq T}, and interest rates r=(rt)0≤t≤Tr=(r\_{t})\_{0\leq t\leq T}. The strict setting of Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") will define the set of admissible controls 𝒜\mathcal{A} such as to match almost surely the given survival probabilities over each integer year from the life table. As this strict setting effectively leads to deterministic optimal mortality rates, we then consider in Section [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") a relaxed setting where the admissible set 𝒜\mathcal{A} is such that this constraint only holds in expectation. However, the resulting control problems then tend to be ill-posed, and similar to Avellaneda and Paras ([1996](#bib.bib40 "Managing the volatility risk of portfolios of derivative securities: the Lagrangian uncertain volatility model")) or Li and Szimayer ([2011](#bib.bib10 "The uncertain mortality intensity framework: pricing and hedging unit-linked life insurance contracts")), we need to further restrict this set 𝒜\mathcal{A} to bounded controls from below and above by time-dependent functions consistent with the life table. We establish asymptotic results showing that, as the set of bounded controls expands, the solutions to the restricted problems converge to the solution of the unrestricted problems.
  
  
These two distinct yet complementary approaches let us derive general bounds for functionals of the lifetime that are compatible with observed life tables, enabling insurers to quantify the worst- and best-case contract prices resulting from deviations of the observed mortality rates from their mortality assumptions/models. This framework is therefore not a pricing engine, but instead provides a novel robust and model-free risk management tool to quantify the sensitivity of life-contingent valuations to within-year mortality uncertainty. We highlight that ’model-free’ refers here to the mortality component: no explicit mortality model is ever imposed. A financial model is still required for valuation, see Section [3](#S3 "3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), but the bounds derived in Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") (strict setting) and [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") (relaxed setting) directly generalize to more complex financial dynamics. Numerical experiments in Section [6](#S6 "6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") further illustrate and support these findings.

## 2 Mortality modeling

Let (Ω,𝒢,ℙ)(\Omega,\mathcal{G},\mathbb{P}) a probability space on which is defined the random variable T0:Ω→ℝ+T\_{0}:\Omega\to\mathbb{R}^{+} describing the future lifetime of a new born child. Let x>0x>0, then Tx:=(T0−x​∣T0>​x):Ω→ℝ+T\_{x}:=\left(T\_{0}-x\,\mid\,T\_{0}>x\right):\Omega\to\mathbb{R}\_{+} denotes the random variable describing the future lifetime of a person aged xx. We consider in this paper a general framework where the lifetime is a mixed random variable with both discrete and continuous components. The cumulative distribution function (CDF) and survival function of TxT\_{x} are given by

|  |  |  |
| --- | --- | --- |
|  | qxt:=ℙ​[Tx≤t]=Fx​(t)andpxt:=ℙ​[Tx>t]=Sx​(t).{}\_{t}q\_{x}:=\mathbb{P}[T\_{x}\leq t]=F\_{x}(t)\quad\text{and}\quad{}\_{t}p\_{x}:=\mathbb{P}[T\_{x}>t]=S\_{x}(t)\,. |  |

By definition, Fx​(t)F\_{x}(t) is non-decreasing, right-continuous, and satisfies Fx​(0)=0F\_{x}(0)=0 with limt→∞Fx​(t)=1\lim\_{t\to\infty}F\_{x}(t)=1. Similarly, Sx​(t)S\_{x}(t) is non-increasing, right-continuous, and satisfies Sx​(0)=1S\_{x}(0)=1 with limt→∞Sx​(t)=0\lim\_{t\to\infty}S\_{x}(t)=0. pxt{}\_{t}p\_{x} is then the survival probability of an xx-year old individual till age x+tx+t , and qxt{}\_{t}q\_{x} his probability of dying before attaining time tt. Furthermore, knowing the individual is still alive at age x+tx+t, we write its survival probability to age s+ts+t, s≥ts\geq t, as px+ts−t=ℙ​[Tx>s+t​|Tx>​t]{}\_{s-t}p\_{x+t}=\mathbb{P}[T\_{x}>s+t\,|\,T\_{x}>t]. For an absolutely continuous random variable TxT\_{x}, the probability density function (pdf) of TxT\_{x} is given by
fx​(t)=−d​Sx​(t)/d​tf\_{x}(t)=-dS\_{x}(t)/dt and we define the force of mortality μx,c​(t)\mu\_{x,c}(t) as the conditional density function of TxT\_{x} at exact age x+tx+t given survival to that age,

|  |  |  |
| --- | --- | --- |
|  | μx,c​(t)=fx​(t)/Sx​(t)=−d​ln⁡Sx​(t)/d​t,\mu\_{x,c}(t)=f\_{x}(t)/S\_{x}(t)=-d\ln S\_{x}(t)/dt\,, |  |

which is a continuous map μx,c:ℝ+→ℝ+\mu\_{x,c}:\mathbb{R}^{+}\to\mathbb{R}^{+}. Clearly, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | pxt=exp⁡(−∫0tμx,c​(s)​𝑑s).{}\_{t}p\_{x}=\exp\left(-\int\_{0}^{t}\mu\_{x,c}(s)ds\right)\,\vskip 5.69054pt. |  | (2.1) |

On the other hand, if TxT\_{x} is a discrete random variable taking values 0<t0<t1<…∈ℝ+0<t\_{0}<t\_{1}<\ldots\in\mathbb{R}^{+} with associated probability function fx​(tj)=ℙ​(Tx=tj)f\_{x}(t\_{j})=\mathbb{P}(T\_{x}=t\_{j}) for j∈ℕj\in\mathbb{N}, the probability of survival is

|  |  |  |
| --- | --- | --- |
|  | pxt=∑j:tj>tfx​(tj).{}\_{t}p\_{x}=\sum\_{j\,:\,t\_{j}>t}f\_{x}(t\_{j})\,. |  |

The (discrete) mortality rate μx,d:ℝ+→[0,1]\mu\_{x,d}:\mathbb{R}^{+}\to[0,1] is then defined accordingly as the conditional death probability at time tjt\_{j} given that the individual has survived to tjt\_{j},

|  |  |  |  |
| --- | --- | --- | --- |
|  | μx,d​(tj)=ℙ​(Tx=tj∣Tx≥tj)=fx​(tj)Sx​(tj−),\mu\_{x,d}(t\_{j})=\mathbb{P}\left(T\_{x}=t\_{j}\,\mid\,T\_{x}\geq t\_{j}\right)=\frac{f\_{x}(t\_{j})}{S\_{x}(t\_{j}^{-})}\,, |  | (2.2) |

where Sx​(t−)=lims→t−Sx​(s)S\_{x}(t^{-})=\lim\_{s\to t^{-}}S\_{x}(s). When it is clear from the context, we simplify the notation of the discrete mortality process μx,j:=μx,d​(tj)\mu\_{x,j}:=\mu\_{x,d}(t\_{j}). Corresponding to ([2.1](#S2.E1 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), the survival probabilities can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | pxt=∏j:tj≤t(1−μx,j)andfx​(tj)=μx,j​∏i=1j−1(1−μx,i).{}\_{t}p\_{x}=\prod\_{j\,:\,t\_{j}\leq t}(1-\mu\_{x,j})\quad\text{and}\quad f\_{x}(t\_{j})=\mu\_{x,j}\prod\_{i=1}^{j-1}(1-\mu\_{x,i})\,. |  | (2.3) |

As in the continuous case, the discrete hazard process (μx,j)j∈ℕ(\mu\_{x,j})\_{j\in\mathbb{N}} uniquely determines the distribution of the lifetime TxT\_{x}.
  
  
More generally, the distribution of TxT\_{x} may have both discrete and continuous components. In this case, the mortality rate can be defined to have continuous component μx,c​(t)\mu\_{x,c}(t) and discrete components μx,0,μx,1,…\mu\_{x,0},\mu\_{x,1},\ldots at the discrete times t0,t1,…t\_{0},t\_{1},\ldots. From Kalbfleisch and Prentice ([2002](#bib.bib1 "The statistical analysis of failure time data")), the survival probability can then be rewritten

|  |  |  |  |
| --- | --- | --- | --- |
|  | pxt=exp⁡(−∫0tμx,c​(s)​𝑑s)​∏j:tj≤t(1−μx,j),{}\_{t}p\_{x}=\exp\left(-\int\_{0}^{t}\mu\_{x,c}(s)ds\right)\prod\_{j\,:\,t\_{j}\leq t}(1-\mu\_{x,j})\,, |  | (2.4) |

and as before, the conditional probability of death over [t,t+d​t)[t,t+dt)
is given by the hazard measure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[Tx∈[t,t+d​t)∣Tx≥t]={μx,j,t=tj,j=0,1,2,…μx,c​(t)​d​t, otherwise.\mathbb{P}[T\_{x}\in[t,t+dt)\mid T\_{x}\geq t]=\begin{cases}\mu\_{x,j},&t=t\_{j},\quad j=0,1,2,\ldots\\ \mu\_{x,c}(t)\,dt,&\text{ otherwise.}\end{cases}\vskip 5.69054pt |  | (2.5) |

Instead of the deterministic setting ([2.4](#S2.E4 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), we allow in this work for stochastic mortality intensity. Specifically, we consider a continuous-time component μx,c=(μx,c​(t))0≤t≤T\mu\_{x,c}=(\mu\_{x,c}(t))\_{0\leq t\leq T} and a discrete-time component μx,d=(μx,d​(τj))j∈ℕ\mu\_{x,d}=(\mu\_{x,d}(\tau\_{j}))\_{j\in\mathbb{N}}. Both processes are assumed to be adapted to the filtration 𝔾:=(𝒢t)0≤t≤T\mathbb{G}:=(\mathcal{G}\_{t})\_{0\leq t\leq T} such that 𝒢T⊂𝒢\mathcal{G}\_{T}\subset\mathcal{G}, with (τj)j∈ℕ(\tau\_{j})\_{j\in\mathbb{N}} a strictly increasing sequence of 𝔾\mathbb{G}-stopping time with 0<τ0<τ1<⋯0<\tau\_{0}<\tau\_{1}<\cdots a.s. (replacing the deterministic time tjt\_{j}) and the jump size μx,j=μx,d​(τj)∈[0,1]\mu\_{x,j}=\mu\_{x,d}(\tau\_{j})\in[0,1] being 𝒢τj\mathcal{G}\_{\tau\_{j}}-measurable for each jj. We then extend ([2.4](#S2.E4 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) using

|  |  |  |  |
| --- | --- | --- | --- |
|  | pxt=𝔼​[exp⁡(−∫0tμx,c​(s)​𝑑s)​∏j:τj≤t(1−μx,j)|𝒢0],{}\_{t}p\_{x}=\mathbb{E}\hskip-1.42262pt\left[\exp\left(-\int\_{0}^{t}\mu\_{x,c}(s)ds\right)\hskip-1.42262pt\prod\_{j\,:\,\tau\_{j}\leq t}(1-\mu\_{x,j})\ \Big|\ \mathcal{G}\_{0}\right], |  | (2.6) |

and the probability of survival till time TT being alive at time t+xt+x,

|  |  |  |  |
| --- | --- | --- | --- |
|  | px+tT−t=𝔼​[exp⁡(−∫tTμx,c​(s)​𝑑s)​∏j:t<τj≤T(1−μx,j)|𝒢t].{}\_{T-t}p\_{x+t}=\mathbb{E}\hskip-1.42262pt\left[\exp\left(-\int\_{t}^{T}\mu\_{x,c}(s)ds\right)\hskip-1.42262pt\prod\_{j\,:\,t<\tau\_{j}\leq T}(1-\mu\_{x,j})\ \Big|\ \mathcal{G}\_{t}\right]. |  | (2.7) |

Finally, we assume that we are given some life table which is described as follows. Let us have a group of l0l\_{0} new born children. Then, for 𝟙i​(x)\mathds{1}\_{i}(x) indicating the survival of the new born child number ii to age xx,
L​(x):=∑i=1l0𝟙i​(x)L(x):=\sum\_{i=1}^{l\_{0}}\mathds{1}\_{i}(x) is a random variable denoting the number of children alive at age xx. For every i=1,…,l0i=1,\ldots,l\_{0} and with p0x:=ℙ​[𝟙i​(x)=1]{}\_{x}p\_{0}:=\mathbb{P}[\mathds{1}\_{i}(x)=1], the expectation of L​(x)L(x) is

|  |  |  |
| --- | --- | --- |
|  | lx:=𝔼​[L​(x)]=𝔼​[∑i=1l0𝟙i​(x)]=l0⋅p0x,l\_{x}:=\mathbb{E}[L(x)]=\mathbb{E}\left[\sum\_{i=1}^{l\_{0}}\mathds{1}\_{i}(x)\right]=l\_{0}\cdot{}\_{x}p\_{0}\,, |  |

which is precisely the quantity reported in the life table. More generally, we have for any integer j∈ℕj\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | lx+j=l0⋅p0x+j=l0⋅p0x⋅pxj=lx⋅pxj.l\_{x+j}=l\_{0}\cdot{}\_{x+j}p\_{0}=l\_{0}\cdot{}\_{x}p\_{0}\cdot{}\_{j}p\_{x}=l\_{x}\cdot{}\_{j}p\_{x}\,. |  | (2.8) |

Therefore, we can equivalently consider that the given life table provides us with pxj=lx+j/lx{}\_{j}p\_{x}=l\_{x+j}/l\_{x} for j∈ℕj\in\mathbb{N}, and thus only specifies the survival function of ⌊T​(x)⌋\lfloor T(x)\rfloor. However, many actuarial products are functionals of the lifetime, and require full information on the the survival function of T​(x)T(x), i.e. on pxt{}\_{t}p\_{x} for all t∈ℝ+t\in\mathbb{R}^{+}. The insurer must then postulate an analytic form for the mortality rates (Gompertz-Makeham, Lee-Carter, CBD, etc.) or adopt a fractional age assumption in addition to the given life tables. We refer to Chapters 2 and 3 of Dickson et al. ([2020](#bib.bib2 "Actuarial mathematics for life contingent risks")) for a thorough review on mortality modeling, and give here a brief reminder of the three main fractional age assumptions. Given a fixed x=0,1,…x=0,1,\ldots and222We restrict t∈[0,1)t\in[0,1) since w.l.o.g. when t>1t>1, we can always rewrite pxt=px⌊t⌋⋅px+⌊t⌋t′{}\_{t}p\_{x}={}\_{\lfloor t\rfloor}p\_{x}\cdot{}\_{t^{\prime}}p\_{x+\lfloor t\rfloor} with t′=t−⌊t⌋∈(0,1)t^{\prime}=t-\lfloor t\rfloor\in(0,1).  t∈[0,1)t\in[0,1), we have

* •

  Uniform distribution of deaths (UDD),

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | pxt=1−t⋅(1−px1).{}\_{t}p\_{x}=1-t\cdot(1-{}\_{1}p\_{x})\,. |  | (2.9) |
* •

  Constant force of mortality (CFM),

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | pxt=e−t⋅μx​(0)=(px1)t.{}\_{t}p\_{x}=e^{-t\cdot\mu\_{x}(0)}=({}\_{1}p\_{x})^{t}\,. |  | (2.10) |
* •

  Balducci approximation,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | pxt=px1t+(1−t)⋅px1.{}\_{t}p\_{x}=\frac{{}\_{1}p\_{x}}{t+(1-t)\cdot{}\_{1}p\_{x}}\,. |  | (2.11) |

## 3 The financial market

We then consider the following financial framework for illustrating purposes, as the contract bounds derived in Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") can be extended directly to other and more complex (Markovian) financial dynamics333This is straightforward by adapting the contract price CtC\_{t} in Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and the coefficients of the HJB equations in Section [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").. The interest rate and stock processes, (rt)0≤t≤T\left(r\_{t}\right)\_{0\leq t\leq T} and (St)0≤t≤T\left(S\_{t}\right)\_{0\leq t\leq T} are defined on (Ω,ℱ,𝔽:=(ℱt)0≤t≤T,ℚ)(\Omega,\mathcal{F},\mathbb{F}:=(\mathcal{F}\_{t})\_{0\leq t\leq T},\mathbb{Q}) generated by 𝐖ℚ=(Wt1,ℚ,Wt2,ℚ)0≤t≤T⊤\mathbf{W}^{\mathbb{Q}}=\left(W\_{t}^{1,\mathbb{Q}},W\_{t}^{2,\mathbb{Q}}\right)\_{0\leq t\leq T}^{\top} :

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(Strt)=(rt​Stκ​(θ​(t)−rt))​d​t+(St​σS​𝐞1⊤σr​𝐞2⊤)​Σ​d​𝐖tℚ,d\,\binom{\,S\_{t}\,}{r\_{t}}=\binom{r\_{t}S\_{t}}{\ \kappa\left(\theta(t)-r\_{t}\right)\ }\,dt+\binom{\ S\_{t}\,\sigma\_{S}\,\mathbf{e}\_{1}^{\top}\ }{\sigma\_{r}\,\mathbf{e}\_{2}^{\top}}\,\Sigma\,d\mathbf{W}^{\mathbb{Q}}\_{t}\,, |  | (3.1) |

where 𝐞1⊤=(1,0),𝐞2⊤=(0,1).Σ\mathbf{e}\_{1}^{\top}=(1,0),\mathbf{e}\_{2}^{\top}=(0,1).\ \Sigma is the Cholesky decomposition of the correlation matrix between the stock and the interest rate,

|  |  |  |
| --- | --- | --- |
|  | Σ=(10ρ1−ρ2),Σ​Σ⊤=(1ρρ1),\Sigma=\left(\begin{array}[]{cc}1&0\\ \rho&\sqrt{1-\rho^{2}}\end{array}\right),\ \quad\Sigma\Sigma^{\top}=\left(\begin{array}[]{cc}1&\rho\\ \rho&1\end{array}\right), |  |

where ρ∈(−1,1)\rho\in(-1,1) is the stock-rate correlation. The cash account is Bt=exp⁡(∫0trs​𝑑s)B\_{t}=\exp\left(\int\_{0}^{t}r\_{s}ds\right) and the zero-coupon (ZC) bond P​(t,T)=𝔼ℚ​[e−∫tTrs​𝑑s|ℱt]P(t,T)=\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}r\_{s}ds}\,\big|\,\mathcal{F}\_{t}\right]. Then this financial market is complete and we know that there exists a unique density process (Zt)0≤t≤T(Z\_{t})\_{0\leq t\leq T} defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt:=d​ℚd​ℙ|ℱt,0≤t≤T.Z\_{t}:=\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|\_{\mathcal{F}\_{t}},\quad 0\leq t\leq T. |  | (3.2) |

Note that the mortality rate processes μx,c,μx,d\mu\_{x,c},\mu\_{x,d} (and thus the random future lifetime TxT\_{x}) are not assumed independent from the financial assets (rt)0≤t≤T\left(r\_{t}\right)\_{0\leq t\leq T} and (St)0≤t≤T\left(S\_{t}\right)\_{0\leq t\leq T}, see Assumption [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"). The parameters are κ,σS,σr>0\kappa,\sigma\_{S},\sigma\_{r}>0 and θ​(t)\theta(t) is a function of time, chosen to match the yield curve

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​(t)=1κ​∂∂t​f​(0,t)+f​(0,t)+σr22​κ2​(1−e−2​κ​t),\theta(t)=\frac{1}{\kappa}\frac{\partial}{\partial t}f(0,t)+f(0,t)+\frac{\sigma\_{r}^{2}}{2\kappa^{2}}\left(1-e^{-2\kappa t}\right), |  | (3.3) |

where f​(0,t)=−∂tln⁡P​(0,t)f(0,t)=-\partial\_{t}\ln P(0,t) is the instantaneous forward rate.
With this specification, the interest rate model can be fitted on a standalone basis. The next standard proposition, see e.g. Hainaut ([2024](#bib.bib6 "Valuation of guaranteed minimum accumulation benefits (GMABs) with physics-inspired neural networks")), reminds the price of a ZC bond in this model.

###### Proposition 3.1.

The price at time tt of a zero-coupon bond of maturity T≥tT\geq t, is given by

|  |  |  |
| --- | --- | --- |
|  | P​(t,T)=exp⁡(−B​(t,T)​rt+ln⁡P​(0,T)P​(0,t)+B​(t,T)​f​(0,t)−σr24​κ3​(1−e−2​κ​t)​B​(t,T)2),P(t,T)=\exp\left(-B(t,T)r\_{t}+\ln\frac{P(0,T)}{P(0,t)}+B(t,T)f(0,t)-\frac{\sigma\_{r}^{2}}{4\kappa^{3}}\left(1-e^{-2\kappa t}\right)B(t,T)^{2}\right), |  |

where
B​(t,T)=1κ​(1−e−κ​(T−t))B(t,T)=\frac{1}{\kappa}\left(1-e^{-\kappa(T-t)}\right). Consequently, under the risk-neutral measure ℚ\mathbb{Q}, we obtain the bond price dynamics as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​P​(t,T)P​(t,T)=rt​d​t−B​(t,T)​σr​𝐞2⊤​Σ​d​𝐖tℚ.\frac{dP(t,T)}{P(t,T)}=r\_{t}dt-B(t,T)\,\sigma\_{r}\,\mathbf{e}\_{2}^{\top}\Sigma\,d\mathbf{W}^{\mathbb{Q}}\_{t}\,. |  | (3.4) |

The policyholder’s premium is then invested in a fund (At)0≤t≤T(A\_{t})\_{0\leq t\leq T} composed of cash, stocks and ZC bonds. More precisely, the insurer invests constant percentages πS\pi\_{S} in stocks, πP\pi\_{P} in bonds and 1−πS−πP1-\pi\_{S}-\pi\_{P} in cash (𝝅=(πS,πP)∈[0,1]2\bm{\pi}=(\pi\_{S},\pi\_{P})\in[0,1]^{2} and πS+πP≤1)\left.\pi\_{S}+\pi\_{P}\leq 1\right).
The fund is self-financed (no exogenous infusion or withdrawal of money) and its instantaneous return is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​AtAt=πS​d​StSt+πP​d​P​(t,T)P​(t,T)+(1−πS−πP)​rt​d​t.\frac{dA\_{t}}{A\_{t}}=\pi\_{S}\frac{dS\_{t}}{S\_{t}}+\pi\_{P}\frac{dP(t,T)}{P(t,T)}+(1-\pi\_{S}-\pi\_{P})\,r\_{t}dt\,. |  | (3.5) |

If we remember Equation ([3.1](#S3.E1 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([3.4](#S3.E4 "In Proposition 3.1. ‣ 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), we infer that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​AtAt\displaystyle\frac{dA\_{t}}{A\_{t}} | =rt​d​t+πS​σS​𝐞1⊤​Σ​d​𝐖tℚ−πP​σr​B​(t,T)​𝐞2⊤​Σ​d​𝐖tℚ\displaystyle=r\_{t}dt+\pi\_{S}\sigma\_{S}\mathbf{e}\_{1}^{\top}\Sigma\,d\mathbf{W}^{\mathbb{Q}}\_{t}-\pi\_{P}\sigma\_{r}B(t,T)\,\mathbf{e}\_{2}^{\top}\Sigma\,d\mathbf{W}^{\mathbb{Q}}\_{t} |  | (3.6) |
|  |  | =rt​d​t+(πS​σS​𝐞1⊤−πP​σr​B​(t,T)​𝐞2⊤)​Σ​d​𝐖tℚ.\displaystyle=r\_{t}dt+\left(\pi\_{S}\sigma\_{S}\mathbf{e}\_{1}^{\top}-\pi\_{P}\sigma\_{r}B(t,T)\,\mathbf{e}\_{2}^{\top}\right)\Sigma\,d\mathbf{W}^{\mathbb{Q}}\_{t}\,. |  |

Let us consider for now the pricing of a financial derivative with payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(AT,GT)=max⁡{AT,GT}=GT+(AT−GT)+.H(A\_{T},G\_{T})=\max\{A\_{T},G\_{T}\}=G\_{T}+(A\_{T}-G\_{T})\_{+}\,. |  | (3.7) |

A typical choice in the following consists in GT=A0​erg​TG\_{T}=A\_{0}e^{r\_{g}T} for rg≥0r\_{g}\geq 0 a minimum guaranteed return. The price of this contract with maturity TT is equal to the expected discounted cash-flow under the risk-neutral measure ℚ\mathbb{Q},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct​(T,GT)=𝔼ℚ​[e−∫tTrs​𝑑s​H​(AT,GT)|ℱt].C\_{t}(T,G\_{T})=\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}r\_{s}ds}\,H(A\_{T},G\_{T})\,\big|\,\mathcal{F}\_{t}\right]. |  | (3.8) |

The next Proposition follows from Hainaut ([2024](#bib.bib6 "Valuation of guaranteed minimum accumulation benefits (GMABs) with physics-inspired neural networks")) and gives us the price of this contract.

###### Proposition 3.2.

The contract’s price CtC\_{t} for t≤Tt\leq T is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct​(T,GT)=GT​P​(t,T)+At​Φ​(−d1​(t))−GT​P​(t,T)​Φ​(−d2​(t)),C\_{t}(T,G\_{T})=G\_{T}P(t,T)+A\_{t}\Phi(-d\_{1}(t))-G\_{T}P(t,T)\Phi(-d\_{2}(t))\,, |  | (3.9) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d1​(t)\displaystyle d\_{1}(t) | =d2​(t)−σY​(t,T),d2​(t)=ln⁡(GT​P​(t,T)At)+12​σY2​(t,T)σY​(t,T),\displaystyle=d\_{2}(t)-\sigma\_{Y}(t,T)\ ,\quad\ \ d\_{2}(t)=\frac{\ln(\frac{G\_{T}P(t,T)}{A\_{t}})+\frac{1}{2}\sigma^{2}\_{Y}(t,T)}{\sigma\_{Y}(t,T)}\,, |  | (3.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σY2​(t,T)\displaystyle\sigma^{2}\_{Y}(t,T) | =∫tT(B​(s,T)​σr​𝐞2⊤​Σ+𝝅⊤​𝚺F​(s))​(B​(s,T)​σr​Σ⊤​𝐞2+𝚺F⊤​(s)​𝝅)​𝑑s,\displaystyle=\int\_{t}^{T}\left(B(s,T)\sigma\_{r}\mathbf{e}\_{2}^{\top}\Sigma+\bm{\pi}^{\top}\bm{\Sigma}\_{F}(s)\right)\left(B(s,T)\sigma\_{r}\Sigma^{\top}\mathbf{e}\_{2}+\bm{\Sigma}\_{F}^{\top}(s)\bm{\pi}\right)ds\,, |  | (3.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚺F​(s)\displaystyle\bm{\Sigma}\_{F}(s) | =(σS0−ρ​σr​B​(s,T)−1−ρ2​σr​B​(s,T)).\displaystyle=\left(\begin{array}[]{cc}\sigma\_{S}&0\\ -\rho\sigma\_{r}B(s,T)&-\sqrt{1-\rho^{2}}\,\sigma\_{r}B\left(s,T\right)\end{array}\right). |  | (3.14) |

Note that ([3.11](#S3.E11 "In Proposition 3.2. ‣ 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) can be obtained in closed-form, see Appendix B and C of Hainaut ([2024](#bib.bib6 "Valuation of guaranteed minimum accumulation benefits (GMABs) with physics-inspired neural networks")).

## 4 Bounds on variable annuities: almost sure matching of the life tables

In this section, we first derive bounds for three variable annuity products with respect to mortality rates, while enforcing strict consistency with the observed life tables. Accordingly, we assume that the total force of mortality available for each integer year xx (or equivalently, each one-year survival probability) is given by the life table (lx)(l\_{x}) in ([2.8](#S2.E8 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and we then restrict attention to admissible mortality trajectories that reproduce almost surely each of these prescribed annual quantities, see constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).
  
  
Let us assume that we are given a cohort of individuals aged xx at time t=0t=0 and the augmented filtration ℍ=(ℋt)0≤t≤T\mathbb{H}=(\mathcal{H}\_{t})\_{0\leq t\leq T} given by ℋt:=ℱt∨𝒢t\mathcal{H}\_{t}:=\mathcal{F}\_{t}\vee\mathcal{G}\_{t}. We require the two following standard assumptions throughout the rest of the manuscript.

###### Assumption 4.1.

The random variable TxT\_{x} satisfies for t≤s≤T,t\leq s\leq T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Tx>s∣ℋs∨{Tx>t})=e−∫tsμx,c​(u)​𝑑u​∏j:t<τj≤s(1−μx,j).\mathbb{P}(T\_{x}>s\mid\mathcal{H}\_{s}\vee\{T\_{x}>t\})=e^{-\int\_{t}^{s}\mu\_{x,c}(u)du}\hskip-5.69054pt\prod\_{j\,:\,t<\tau\_{j}\leq s}\hskip-5.69054pt(1-\mu\_{x,j})\,. |  | (4.1) |

This property is an extension of the doubly stochastic (Cox) property, see Cox and Isham ([1980](#bib.bib30 "Point processes")).

###### Assumption 4.2.

In the combined financial-actuarial market, we assume that ℚ\mathbb{Q} corresponds to the Minimal Martingale Measure (MMM) (Schweizer, [1991](#bib.bib38 "Option hedging for semimartingales"), [1995](#bib.bib39 "On the minimal martingale measure and the Möllmer-Schweizer decomposition")). Under this assumption, the density of the change of measure is such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚd​ℙ|ℋt=Zt,0≤t≤T,\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|\_{\mathcal{H}\_{t}}=Z\_{t},\quad 0\leq t\leq T, |  | (4.2) |

where (Zt)0≤t≤T(Z\_{t})\_{0\leq t\leq T} is the unique density process defined by ([3.2](#S3.E2 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).

Several arguments support the use of the MMM. In particular, in the valuation and hedging of variable annuities, Møller ([1998](#bib.bib35 "Risk-minimizing hedging strategies for unit-linked life insurance contracts"), [2001](#bib.bib36 "Risk-minimizing hedging strategies for insurance payment processes")) and Ceci et al. ([2017](#bib.bib37 "Unit-linked life insurance policies: optimal hedging in partially observable market models")) show that, within the framework of local risk-minimization, the fair value of variables annuities can be expressed as the discounted expectation of its payoff under the MMM. Hence, this measure arises naturally in incomplete markets, where perfect replication is not feasible, and it provides the pricing rule consistent with the locally risk-minimizing hedging strategy. The MMM is also mathematically tractable: its construction relies solely on the orthogonal decomposition of the discounted price process. Moreover, under the MMM, no additional mortality risk premium is introduced. More precisely, since the mortality intensity may be correlated with traded assets, its drift is adjusted under the MMM, which induces a change in the dynamic but not in the functional form of the mortality intensity. Although the choice of the martingale measure in Assumption [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") appears arbitrary, it is in fact the most natural one in our setting as we have no prior knowledge regarding the mortality rates μ\mu. Other martingale measures could be considered but would require additional modeling choices, such as the mortality risk process (λt)0≤t≤T(\lambda\_{t})\_{0\leq t\leq T}, with λt>−1\lambda\_{t}>-1 a.s., which determines the pricing mortality under ℚ\mathbb{Q} as μtℚ=(1+λt)​μt\mu^{\mathbb{Q}}\_{t}=(1+\lambda\_{t})\mu\_{t} for all 0≤t≤T0\leq t\leq T, as well as assumptions on any other stochastic factors that could influence the dynamics of mortality process.
  
  
Assumption [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") justifies to introduce our general objective functional as the expectation under ℚ\mathbb{Q} of a given functional FF of the lifetime (equivalently, of the mortality rates), account value (At)0≤t≤T(A\_{t})\_{0\leq t\leq T} and interest rate (rt)0≤t≤T(r\_{t})\_{0\leq t\leq T}, as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtμ=𝔼ℚ​[F​(T,μx,c,μx,d,A,r)∣ℋt],t∈[0,T].V^{\mu}\_{t}=\mathbb{E}^{\mathbb{Q}}\left[F(T,\mu\_{x,c},\mu\_{x,d},A,r)\mid\mathcal{H}\_{t}\right],\qquad t\in[0,T]. |  | (4.3) |

Our objective is to derive lower and upper bounds for VtμV^{\mu}\_{t} over a prescribed class of mortality models consistent with a given life table (lx)x∈ℕ(l\_{x})\_{x\in\mathbb{N}} described by ([2.8](#S2.E8 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). To this end, we consider the continuous-time force of mortality μx,c=(μx,c​(t))0≤t≤T\mu\_{x,c}=(\mu\_{x,c}(t))\_{0\leq t\leq T} as a control process taking values in a given compact set 𝕄⊂[0,+∞)\mathbb{M}\subset[0,+\infty), and we let ℳ\mathcal{M} be a given family of such continuous ℍ\mathbb{H}-adapted controls μx,c\mu\_{x,c}.
In addition, we consider the discrete process μx,d=(τ0,τ1,…;μx,0,μx,1,…)∈𝒱\mu\_{x,d}=(\tau\_{0},\tau\_{1},\ldots;\mu\_{x,0},\mu\_{x,1},\ldots)\in\mathcal{V} as a given impulse control, where 𝒱\mathcal{V} is the set of admissible impulse controls μx,d\mu\_{x,d} such that 0<τ0<τ1<…≤T0<\tau\_{0}<\tau\_{1}<\ldots\leq T (a.s.) are ℍ\mathbb{H}-stopping times and μx,j∈[0,1]\mu\_{x,j}\in[0,1] are ℋτj\mathcal{H}\_{\tau\_{j}}-measurable for all j≥0j\geq 0. We then call μ:=(μx,c,μx,d)\mu:=(\mu\_{x,c},\mu\_{x,d}) a combined control.
Finally, we assume that we are given a set 𝒲⊂ℳ×𝒱\mathcal{W}\subset\mathcal{M}\times\mathcal{V} of admissible combined controls μ\mu, such that VtμV^{\mu}\_{t} is well-defined for all t∈[0,T]t\in[0,T] and such that the life-table constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) below is satisfied.
  
Note that we do not only want the force of mortality to be consistent with the final survival probability px+tT−t{}\_{T-t}p\_{x+t}, but with all intermediate one-year survival probabilities at integer ages between x+tx+t and x+Tx+T. This can be seen writing for t,T∈ℝ+t,T\in\mathbb{R}^{+},

|  |  |  |
| --- | --- | --- |
|  | px+tT−t=px+t⌈t⌉−t×px+⌈t⌉1×px+1+⌈t⌉1×⋯×px+j+⌈t⌉1×⋯×px+⌊T⌋T−⌊T⌋.{}\_{T-t}p\_{x+t}={}\_{\lceil t\rceil-t}p\_{x+t}\times{}\_{1}p\_{x+\lceil t\rceil}\times{}\_{1}p\_{x+1+\lceil t\rceil}\times\cdots\times{}\_{1}p\_{x+j+\lceil t\rceil}\times\cdots\times{}\_{T-\lfloor T\rfloor}p\_{x+\lfloor T\rfloor}\,. |  |

All the one-year survival probabilities px+j+⌈t⌉1{}\_{1}p\_{x+j+\lceil t\rceil}, j=0,…,⌊T⌋−⌈t⌉−1j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1, can be observed from the given life table ([2.8](#S2.E8 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^j:=px+j+⌈t⌉1=lx+j+⌈t⌉+1lx+j+⌈t⌉.\hat{p}\_{j}:={}\_{1}p\_{x+j+\lceil t\rceil}=\frac{l\_{x+j+\lceil t\rceil+1}}{l\_{x+j+\lceil t\rceil}}. |  | (4.4) |

Hence, we obtain444Additional constraints from the observed life table (such as fractional age assumptions or from expert knowledge) can also be imposed on px+t⌈t⌉−t{}\_{\lceil t\rceil-t}p\_{x+t} and px+⌊T⌋T−⌊T⌋{}\_{T-\lfloor T\rfloor}p\_{x+\lfloor T\rfloor}. Alternatively, we simply assume in the following that these extremal survival probabilities are fixed to 11 and cannot be controlled in our framework through μ\mu.

|  |  |  |  |
| --- | --- | --- | --- |
|  | px+tT−t=px+t⌈t⌉−t×p^0×p^1×⋯×p^j×⋯×px+⌊T⌋T−⌊T⌋.{}\_{T-t}p\_{x+t}={}\_{\lceil t\rceil-t}p\_{x+t}\times\hat{p}\_{0}\times\hat{p}\_{1}\times\cdots\times\hat{p}\_{j}\times\cdots\times{}\_{T-\lfloor T\rfloor}p\_{x+\lfloor T\rfloor}. |  | (4.5) |

Therefore, in the strict setting of this section, admissible mortality controls μ∈𝒲\mu\in\mathcal{W} are required to strictly match these observed p^j\hat{p}\_{j}’s. Specifically, for each j=0,…,⌊T⌋−⌈t⌉−1j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡(−∫⌈t⌉+j⌈t⌉+j+1μx,c​(s)​𝑑s)​∏i:⌈t⌉+j<τi≤⌈t⌉+j+1(1−μx,i)=p^j,ℙ−a.s.\exp\left(-\int\_{\lceil t\rceil+j}^{\lceil t\rceil+j+1}\mu\_{x,c}(s)ds\right)\hskip-3.69885pt\prod\_{i\,:\,\lceil t\rceil+j<\tau\_{i}\leq\lceil t\rceil+j+1}\hskip-11.38109pt(1-\mu\_{x,i})=\hat{p}\_{j}\,,\quad\mathbb{P}-\text{a.s.} |  | (4.6) |

The aim of this Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") is then to find the upper bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=supμ∈𝒲𝔼ℚ​[F​(μx,c,μx,d,A,r)∣ℋt],\bar{V}\_{t}=\sup\_{\mu\in\mathcal{W}}\mathbb{E}^{\mathbb{Q}}\left[F(\mu\_{x,c},\mu\_{x,d},A,r)\mid\mathcal{H}\_{t}\right], |  | (4.7) |

and the lower bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=infμ∈𝒲𝔼ℚ​[F​(μx,c,μx,d,A,r)∣ℋt],\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=\inf\_{\mu\in\mathcal{W}}\mathbb{E}^{\mathbb{Q}}\left[F(\mu\_{x,c},\mu\_{x,d},A,r)\mid\mathcal{H}\_{t}\right], |  | (4.8) |

of functionals of the lifetime over all admissible mortality controls. We then denote, if they exist, the corresponding optimal mortality controls μ¯∗,μ¯∗∈𝒲\bar{\mu}^{\*},\underline{\mu\mkern-4.0mu}\mkern 4.0mu^{\*}\in\mathcal{W} attaining these bounds, i.e. V¯t=Vtμ¯∗\bar{V}\_{t}=V^{\bar{\mu}^{\*}}\_{t} and V¯t=Vtμ¯∗\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=V^{\underline{\mu\mkern-4.0mu}\mkern 4.0mu^{\*}}\_{t}.
  
  
Moreover, we emphasize that this pathwise constraint is quite strong in practice: it requires almost surely that every realized mortality path matches the annual survival probabilities p^j\hat{p}\_{j} from the life table, essentially leading to deterministic optimal rates μ¯∗,μ¯∗\bar{\mu}^{\*},\underline{\mu\mkern-4.0mu}\mkern 4.0mu^{\*} (see Propositions [4.3](#S4.ThmTheorem3 "Proposition 4.3 (GMAB bounds). ‣ 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")–[4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")–[4.5](#S4.ThmTheorem5 "Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") below). While a constraint in expectation would be more natural, a naive implementation of the resulting control problem appears to be ill-posed. We address this issue in Section [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), by appropriately relaxing this constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and specifying the corresponding set of admissible (bounded) controls. In the following subsections, we study the upper and lower bounds of three different types of variables annuities: GMAB, GMIB and GMDB. Proofs are deferred in [A](#A1 "Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").

### 4.1. Guaranteed Minimum Accumulation Benefits

Guaranteed Minimum Accumulation Benefits (GMAB) are retirement savings products which promises in case of survival, the maximum between investments and a guaranteed capital. The contract is subscribed by an individual aged xx and guarantees at expiry date TT a payout equal to the maximum between the guaranteed capital GTA=A0​erg​TG^{A}\_{T}=A\_{0}e^{r\_{g}T} and the fund ATA\_{T}, in the event of survival. The payout in case of survival is then given by ([3.7](#S3.E7 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). Assuming survival to time tt555We slightly abuse notation throughout the manuscript by conditioning on ℋt\mathcal{H}\_{t} instead of ℋt∨{Tx>t}\mathcal{H}\_{t}\vee\{T\_{x}>t\}., the fair value of such a policy at time tt is denoted by VtμV^{\mu}\_{t} and equal to the expected discounted cash-flows under ℚ\mathbb{Q},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtμ\displaystyle V^{\mu}\_{t} | =𝔼ℚ​[e−∫tTrs​𝑑s​ 1{Tx>T}​H​(AT,GTA)|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}r\_{s}ds}\,\mathds{1}\_{\{T\_{x}>T\}}\,H(A\_{T},G^{A}\_{T})\ \big|\ \mathcal{H}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ​[𝔼ℚ​[e−∫tTrs​𝑑s​ 1{Tx>T}​H​(AT,GTA)|ℋT]|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}r\_{s}ds}\,\mathds{1}\_{\{T\_{x}>T\}}\,H(A\_{T},G^{A}\_{T})\ \big|\ \mathcal{H}\_{T}\right]\,\Big|\ \mathcal{H}\_{t}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼ℚ​[e−∫tT(rs+μx,c​(s))​𝑑s​∏j:t<τj≤T(1−μx,j)​H​(AT,GTA)|ℋt],\displaystyle=\mathbb{E}^{\mathbb{Q}}\bigg[\,e^{-\int\_{t}^{T}(r\_{s}+\mu\_{x,c}(s))ds}\hskip-5.69054pt\prod\_{j\,:\,t<\tau\_{j}\leq T}\hskip-5.69054pt(1-\mu\_{x,j})\,H(A\_{T},G^{A}\_{T})\ \big|\ \mathcal{H}\_{t}\,\bigg], |  | (4.9) |

using Assumptions [4.1](#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"). Note that in general
Vtμ≠𝔼ℚ​[𝟙Tx>T|𝒢t]​Ct​(T,GTA)=px+tT−t​Ct​(T,GTA)V^{\mu}\_{t}\neq\mathbb{E}^{\mathbb{Q}}[\mathds{1}\_{T\_{x}>T}\,|\,\mathcal{G}\_{t}]\,C\_{t}(T,G^{A}\_{T})={}\_{T-t}p\_{x+t}\,C\_{t}(T,G^{A}\_{T}) since μ\mu is not assumed independent from AA and rr. We then derive the GMAB upper bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=supμ∈𝒲𝔼ℚ​[e−∫tT(rs+μx,c​(s))​𝑑s​∏j:t<τj≤T(1−μx,j)​H​(AT,GTA)|ℋt],\bar{V}\_{t}=\sup\_{\mu\in\mathcal{W}}\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}(r\_{s}+\mu\_{x,c}(s))ds}\hskip-5.69054pt\prod\_{j\,:\,t<\tau\_{j}\leq T}\hskip-5.69054pt(1-\mu\_{x,j})\,H(A\_{T},G^{A}\_{T})\ \big|\ \mathcal{H}\_{t}\right], |  | (4.10) |

and GMAB lower bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=infμ∈𝒲𝔼ℚ​[e−∫tT(rs+μx,c​(s))​𝑑s​∏j:t<τj≤T(1−μx,j)​H​(AT,GTA)|ℋt].\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=\inf\_{\mu\in\mathcal{W}}\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}(r\_{s}+\mu\_{x,c}(s))ds}\hskip-5.69054pt\prod\_{j\,:\,t<\tau\_{j}\leq T}\hskip-5.69054pt(1-\mu\_{x,j})\,H(A\_{T},G^{A}\_{T})\ \big|\ \mathcal{H}\_{t}\right]. |  | (4.11) |

However, these GMAB bounds are trivial as any force of mortality μ∈𝒲\mu\in\mathcal{W}–thereby satisfying ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–leads to the same price Vtμ=VtV^{\mu}\_{t}=V\_{t}, since the contract’s value only depends on the total survival probability px+tT−t{}\_{T-t}p\_{x+t} given by ([4.5](#S4.E5 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). In fact, the exact death time of an individual in each one-year period does not change the contract’s value VtμV^{\mu}\_{t} as in any case, a deceased policyholder will not receive the terminal payoff H​(AT,GTA)H(A\_{T},G^{A}\_{T}). In other words, the GMAB does not depend on the exact path of the mortality process, as summarized in the following proposition.

###### Proposition 4.3 (GMAB bounds).

For the GMAB contract ([4.9](#S4.E9 "In 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), each admissible control μ∈𝒲\mu\in\mathcal{W} is an optimal control μ¯∗\bar{\mu}^{\*} of ([4.10](#S4.E10 "In 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and μ¯∗\underline{\mu\mkern-4.0mu}\mkern 4.0mu^{\*} of ([4.11](#S4.E11 "In 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). The GMAB price then satisfies for each μ∈𝒲\mu\in\mathcal{W},

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=Vtμ=px+tT−t​Ct​(T,GTA),\bar{V}\_{t}=V^{\mu}\_{t}={}\_{T-t}p\_{x+t}\,C\_{t}(T,G^{A}\_{T})\,, |  | (4.12) |

and, respectively,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=Vtμ=px+tT−t​Ct​(T,GTA).\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=V^{\mu}\_{t}={}\_{T-t}p\_{x+t}\,C\_{t}(T,G^{A}\_{T})\,. |  | (4.13) |

where px+tT−t{}\_{T-t}p\_{x+t} is given by ([4.5](#S4.E5 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).

This Proposition [4.3](#S4.ThmTheorem3 "Proposition 4.3 (GMAB bounds). ‣ 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") is still valid when considering any form of payoff H​(AT,GTA)H(A\_{T},G^{A}\_{T}) for the GMAB ([4.9](#S4.E9 "In 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), by adjusting the price Ct​(T,GTA)C\_{t}(T,G^{A}\_{T}) in ([4.12](#S4.E12 "In Proposition 4.3 (GMAB bounds). ‣ 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))-([4.13](#S4.E13 "In Proposition 4.3 (GMAB bounds). ‣ 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). Even though the bounds on the GMAB are trivial, they lay the foundations for studying the following more complex variable annuities.

### 4.2. Guaranteed Minimum Income Benefit

We now consider the following variant of Guaranteed Minimum Income Benefits (GMIB) where an individual aged xx continuously receives a guaranteed rate rg>0r\_{g}>0 on the initial investment A0A\_{0} as long as he is alive, plus a bonus rate proportional to the excess return of the fund AtA\_{t} over the pre-specified guarantee GtI=A0​erg​tG^{I}\_{t}=A\_{0}e^{r\_{g}t}. The exact payoff is given by666one could also consider continuously-compounded rates with H~​(At,GtI)=A0​(rg​erg​(T−t)+1A0​(At−GtI)+)\widetilde{H}(A\_{t},G^{I}\_{t})=A\_{0}\left(r\_{g}e^{r\_{g}(T-t)}+\frac{1}{A\_{0}}(A\_{t}-G^{I}\_{t})\_{+}\right)\,
since ∫tTrg​erg​(T−s)​𝑑s=erg​(T−t)−1\int\_{t}^{T}r\_{g}e^{r\_{g}(T-s)}ds=e^{r\_{g}(T-t)}-1.

|  |  |  |  |
| --- | --- | --- | --- |
|  | H~​(At,GtI)=A0​(rg+1A0​(At−GtI)+).\widetilde{H}(A\_{t},G^{I}\_{t})=A\_{0}\left(r\_{g}+\frac{1}{A\_{0}}(A\_{t}-G^{I}\_{t})\_{+}\right)\,. |  | (4.14) |

Proposition [3.2](#S3.ThmTheorem2 "Proposition 3.2. ‣ 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") can be straightforwardly adapted to obtain as contract price for s≥ts\geq t, the sum of a ZC bond and a European call,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct​(s,GsI)\displaystyle C\_{t}(s,G^{I}\_{s}) | =𝔼ℚ​[e−∫tsru​𝑑u​H~​(As,GsI)|ℱt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{s}r\_{u}du}\,\widetilde{H}(A\_{s},G^{I}\_{s})\,\big|\,\mathcal{F}\_{t}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =A0​rg​P​(t,s)+At​Φ​(−d1​(t))−GsI​P​(t,s)​Φ​(−d2​(t)).\displaystyle=A\_{0}r\_{g}P(t,s)+A\_{t}\Phi(-d\_{1}(t))-G^{I}\_{s}P(t,s)\Phi(-d\_{2}(t)). |  | (4.15) |

Again, the exact form of the payoff H~\widetilde{H} is chosen here solely for analytical convenience in solving the optimization ([4.17](#S4.E17 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([4.18](#S4.E18 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and does not restrict the generality of our analysis as Proposition [4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") below remains valid for any positive payoff H~\widetilde{H}, provided that the corresponding price Ct​(s,GsI)C\_{t}(s,G^{I}\_{s}) is adjusted accordingly. The fair value of such a policy, denoted by VtμV^{\mu}\_{t}, is again equal to the expected discounted cash-flows under the risk neutral measure ℚ\mathbb{Q},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtμ\displaystyle V^{\mu}\_{t} | =𝔼ℚ​[∫tTe−∫tsru​𝑑u​ 1Tx>s​H~​(As,GsI)​𝑑s|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}\hskip-2.84526pte^{-\int\_{t}^{s}r\_{u}du}\,\mathds{1}\_{T\_{x}>s}\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \Big|\ \mathcal{H}\_{t}\right]\hskip-1.99168pt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ​[∫tTe−∫tsru​𝑑u​px+ts−t​H~​(As,GsI)​𝑑s|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}\hskip-2.84526pte^{-\int\_{t}^{s}r\_{u}du}\,{}\_{s-t}p\_{x+t}\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \Big|\ \mathcal{H}\_{t}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼ℚ​[∫tTe−∫ts(ru+μx,c​(u))​𝑑u​∏j:t<τj≤s(1−μx,j)​H~​(As,GsI)​d​s|ℋt],\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}e^{-\int\_{t}^{s}(r\_{u}+\mu\_{x,c}(u))du}\hskip-5.69054pt\prod\_{j\,:\,t<\tau\_{j}\leq s}\hskip-5.69054pt(1-\mu\_{x,j})\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \Big|\ \mathcal{H}\_{t}\right], |  | (4.16) |

under Assumptions [4.1](#S4.ThmTheorem1 "Assumption 4.1. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"). The upper bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=supμ∈𝒲𝔼ℚ​[∫tTe−∫ts(ru+μx,c​(u))​𝑑u​∏j:t<τj≤s(1−μx,j)​H~​(As,GsI)​d​s|ℋt],\bar{V}\_{t}=\sup\_{\mu\in\mathcal{W}}\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}e^{-\int\_{t}^{s}(r\_{u}+\mu\_{x,c}(u))du}\hskip-5.69054pt\prod\_{j\,:\,t<\tau\_{j}\leq s}\hskip-5.69054pt(1-\mu\_{x,j})\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \Big|\ \mathcal{H}\_{t}\right], |  | (4.17) |

and lower bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=infμ∈𝒲𝔼ℚ​[∫tTe−∫ts(ru+μx,c​(u))​𝑑u​∏j:t<τj≤s(1−μx,j)​H~​(As,GsI)​d​s|ℋt],\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=\inf\_{\mu\in\mathcal{W}}\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}e^{-\int\_{t}^{s}(r\_{u}+\mu\_{x,c}(u))du}\hskip-5.69054pt\prod\_{j\,:\,t<\tau\_{j}\leq s}\hskip-5.69054pt(1-\mu\_{x,j})\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \Big|\ \mathcal{H}\_{t}\right], |  | (4.18) |

of the GMIB contract ([4.16](#S4.E16 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) are again such that the constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) from the given life table holds and are derived in the following proposition.

###### Proposition 4.4 (GMIB bounds).

(i) Upper bound.
The optimal control μ¯∗=(μ¯x,c∗,μ¯x,d∗)\bar{\mu}^{\*}=(\bar{\mu}^{\*}\_{x,c},\bar{\mu}^{\*}\_{x,d}) for the upper bound V¯t\bar{V}\_{t} is given by

|  |  |  |
| --- | --- | --- |
|  | μ¯x,c∗​(t)≡0,μ¯x,d∗={(τ¯j∗,μ¯x,j∗)}j=0,…,⌊T⌋−⌈t⌉−1,\bar{\mu}^{\*}\_{x,c}(t)\equiv 0,\qquad\bar{\mu}^{\*}\_{x,d}=\{(\bar{\tau}\_{j}^{\*},\bar{\mu}\_{x,j}^{\*})\}\_{j=0,\dots,\lfloor T\rfloor-\lceil t\rceil-1}, |  |

with intervention times and jump sizes

|  |  |  |
| --- | --- | --- |
|  | τ¯j∗=⌈t⌉+j+1,μ¯x,j∗=1−p^j.\bar{\tau}\_{j}^{\*}=\lceil t\rceil+j+1,\qquad\bar{\mu}\_{x,j}^{\*}=1-\hat{p}\_{j}. |  |

Moreover, the upper bound satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=∫tTp¯x+t∗s−t​Ct​(s,GsI)​𝑑s,\bar{V}\_{t}=\int\_{t}^{T}{}\_{s-t}\bar{p}^{\*}\_{x+t}\,C\_{t}(s,G\_{s}^{I})\,ds, |  | (4.19) |

where the induced survival probability is deterministic and is equal to

|  |  |  |  |
| --- | --- | --- | --- |
|  | p¯x+t∗s−t=∏j∈ℕ:⌈t⌉+j+1≤sp^j,{}\_{s-t}\bar{p}^{\*}\_{x+t}=\prod\_{j\in\mathbb{N}:\,\lceil t\rceil+j+1\leq s}\hat{p}\_{j}, |  | (4.20) |

for s∈[t,T]s\in[t,T] (with the convention ∏∅:=1\prod\_{\emptyset}:=1).

(ii) Lower bound.
The lower bound V¯t:=infμ∈𝒲Vtμ\underline{V}\_{t}:=\inf\_{\mu\in\mathcal{W}}V\_{t}^{\mu} is not attained in 𝒲\mathcal{W}. However, there exists a sequence of admissible controls {μ(n)}n≥1⊂𝒲\{\mu^{(n)}\}\_{n\geq 1}\subset\mathcal{W} such that Vtμ(n)↓V¯tV\_{t}^{\mu^{(n)}}\downarrow\underline{V}\_{t} and whose discrete intervention times satisfy τj(n)↓⌈t⌉+j\tau^{(n)}\_{j}\downarrow\lceil t\rceil+j with μx,j(n)=1−p^j\mu^{(n)}\_{x,j}=1-\hat{p}\_{j} for each j=0,…,⌊T⌋−⌈t⌉−1j=0,\dots,\lfloor T\rfloor-\lceil t\rceil-1 and with μx,c(n)≡0\mu\_{x,c}^{(n)}\equiv 0. This lower bound V¯t\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t} then satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=∫tTp¯x+t∗s−t​Ct​(s,GsI)​𝑑s,\displaystyle\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=\int\_{t}^{T}{}\_{s-t}\underline{p\mkern-4.0mu}\mkern 4.0mu^{\*}\_{x+t}\,C\_{t}(s,G^{I}\_{s})\,ds\,, |  | (4.21) |

where for s∈[t,T]s\in[t,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | p¯x+t∗s−t=∏j∈ℕ:⌈t⌉+j<sp^j.\displaystyle{}\_{s-t}\underline{p\mkern-4.0mu}\mkern 4.0mu^{\*}\_{x+t}=\prod\_{j\in\mathbb{N}\,:\,\lceil t\rceil+j<s}\hat{p}\_{j}\,. |  | (4.22) |

We can extend Proposition [4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") to more general payoffs by allowing H~\widetilde{H} to be negative, e.g. if rg∈ℝr\_{g}\in\mathbb{R}. The existence and uniqueness of each τj∗\tau^{\*}\_{j} then depend on the growth and convexity properties of the ℋt\mathcal{H}\_{t}-conditional expectation in ([4.16](#S4.E16 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). Naturally, when τj∗\tau^{\*}\_{j} is unique, we obtain directly from constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) with μx,c∗≡0\mu^{\*}\_{x,c}\equiv 0 that μx,j∗=1−p^j\mu^{\*}\_{x,j}=1-\hat{p}\_{j}. Even when τj∗\tau^{\*}\_{j} is not unique, choosing arbitrarily any such τj∗\tau^{\*}\_{j} with μx,j∗=1−p^j\mu^{\*}\_{x,j}=1-\hat{p}\_{j} remains sufficient in our setting, since we are anyway only concerned with the upper and lower bounds V¯t\bar{V}\_{t}, V¯t\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t} (the observed mortality being not controllable in practice).
Moreover, we also note for the lower bound V¯t\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t} in Proposition [4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") (ii) that p¯x+t∗s−t\displaystyle{}\_{s-t}\underline{p\mkern-4.0mu}\mkern 4.0mu^{\*}\_{x+t} is left-continuous in ss and hence not a proper survival function (no minimizer τ¯j∗\underline{\tau\mkern-4.0mu}\mkern 4.0mu^{\*}\_{j}). Importantly, the absence of minimizer is again not an issue in our framework, since the observed mortality cannot be controlled in practice. We are in fact only interested in the worst-case contract value V¯t\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}, which allows the insurer to quantify the maximum potential loss arising from deviations of the realized mortality rates from her chosen mortality assumption/model. If needed, however, p¯x+t∗s−t\displaystyle{}\_{s-t}\underline{p\mkern-4.0mu}\mkern 4.0mu^{\*}\_{x+t} can always be used in practice as an approximate optimal survival probability.

### 4.3. Guaranteed Minimum Death Benefits

Guaranteed Minimum Death Benefits (GMDB) ensure that if the policyholder dies before the contract’s maturity, their beneficiaries will receive at least a guaranteed minimum amount, even if the investment’s performance is lower. The payout H^\widehat{H} in case of death at time s≥ts\geq t is then defined similarly as in ([3.7](#S3.E7 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) using GsD=A0​erg​sG^{D}\_{s}=A\_{0}e^{r\_{g}s},

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^​(As,GsD)=max⁡{As,GsD}=GsD+(As−GsD)+,\widehat{H}(A\_{s},G^{D}\_{s})=\max\{A\_{s},G^{D}\_{s}\}=G^{D}\_{s}+(A\_{s}-G^{D}\_{s})\_{+}\,, |  | (4.23) |

with GsD>0G^{D}\_{s}>0, and whose price Ct​(s,GsD)C\_{t}(s,G^{D}\_{s}) at time t≤st\leq s is given in Proposition [3.2](#S3.ThmTheorem2 "Proposition 3.2. ‣ 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"). The fair value of such a policy can be written using ([2.5](#S2.E5 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([2.6](#S2.E6 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtμ\displaystyle V^{\mu}\_{t} | =𝔼ℚ​[∫tTe−∫tsru​𝑑u​px+ts−−t​(μx,c​(s)+∑j∈ℕμx,j​δ​(s−τj))​H^​(As,GsD)​𝑑s|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}du}\,{}\_{s^{-}-t}p\_{x+t}\left(\mu\_{x,c}(s)+\sum\_{j\in\mathbb{N}}\mu\_{x,j}\,\delta(s-\tau\_{j})\right)\widehat{H}(A\_{s},G^{D}\_{s})\,ds\ \Big|\ \mathcal{H}\_{t}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼ℚ​[∫tTe−∫ts(ru+μx,c​(u))​𝑑u​(∏j:t<τj<s(1−μx,j))​(μx,c​(s)+∑j∈ℕμx,j​δ​(s−τj))​H^​(As,GsD)​𝑑s|ℋt]\displaystyle\hskip-13.65732pt=\mathbb{E}^{\mathbb{Q}}\hskip-1.99168pt\left[\hskip-1.13809pt\int\_{t}^{T}\hskip-3.41432pte^{-\int\_{t}^{s}(r\_{u}+\mu\_{x,c}(u))du}\hskip-1.70717pt\left(\prod\_{j\,:\,t<\tau\_{j}<s}\hskip-7.11317pt(1-\mu\_{x,j})\right)\hskip-2.41849pt\hskip-1.42262pt\left(\hskip-1.42262pt\mu\_{x,c}(s)+\sum\_{j\in\mathbb{N}}\mu\_{x,j}\,\delta(s-\tau\_{j})\hskip-2.13394pt\right)\hskip-2.41849pt\widehat{H}(A\_{s},G^{D}\_{s})\,ds\,\Big|\,\mathcal{H}\_{t}\right] |  | (4.24) |

where δ​(⋅)\delta(\cdot) is the Dirac measure at zero. We again aim at deriving the upper bound V¯t=supμ∈𝒲Vtμ\bar{V}\_{t}=\sup\_{\mu\in\mathcal{W}}V^{\mu}\_{t} and lower bound V¯t=infμ∈𝒲Vtμ\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=\inf\_{\mu\in\mathcal{W}}V^{\mu}\_{t} subject to the constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), where the supremum is taken with respect to both the continuous and the discrete components of the force of mortality.

###### Proposition 4.5 (GMDB bounds).

Assume that for all s∈[t,T]s\in[t,T], rg≥f​(t,s)r\_{g}\geq f(t,s) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt​α​(t)−θ​(t)​(α​(t)+(T−t))≤0,withα​(t)=e−κ​(T−t)−1κ≤0.r\_{t}\alpha(t)-\theta(t)\big(\alpha(t)+(T-t)\big)\leq 0,\quad\text{with}\quad\alpha(t)=\frac{e^{-\kappa(T-t)}-1}{\kappa}\leq 0. |  | (4.25) |

(i) Upper bound.
The optimal control for V¯t:=supμ∈𝒲Vtμ\bar{V}\_{t}:=\sup\_{\mu\in\mathcal{W}}V\_{t}^{\mu} is given by

|  |  |  |
| --- | --- | --- |
|  | μ¯x,c∗​(t)≡0,μ¯x,d∗={(τ¯j∗,μ¯x,j∗)}j=0,…,⌊T⌋−⌈t⌉−1,\bar{\mu}^{\*}\_{x,c}(t)\equiv 0,\qquad\bar{\mu}^{\*}\_{x,d}=\{(\bar{\tau}\_{j}^{\*},\bar{\mu}\_{x,j}^{\*})\}\_{j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1}, |  |

with intervention times and jump sizes

|  |  |  |
| --- | --- | --- |
|  | τ¯j∗=⌈t⌉+j+1,μ¯x,j∗=1−p^j.\bar{\tau}\_{j}^{\*}=\lceil t\rceil+j+1,\qquad\bar{\mu}\_{x,j}^{\*}=1-\hat{p}\_{j}. |  |

The corresponding upper bound is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=∑j=0⌊T⌋−⌈t⌉−1Ct​(⌈t⌉+j+1,G⌈t⌉+j+1D)​(1−p^j)​∏i<jp^i.\bar{V}\_{t}=\sum\_{j=0}^{\lfloor T\rfloor-\lceil t\rceil-1}C\_{t}(\lceil t\rceil+j+1,G^{D}\_{\lceil t\rceil+j+1})\,(1-\hat{p}\_{j})\,\prod\_{i<j}\hat{p}\_{i}. |  | (4.26) |

(ii) Lower bound.
The lower bound V¯t:=infμ∈𝒲Vtμ\underline{V}\_{t}:=\inf\_{\mu\in\mathcal{W}}V\_{t}^{\mu} is not attained in 𝒲\mathcal{W}. However, there exists a sequence of admissible controls {μ(n)}n≥1⊂𝒲\{\mu^{(n)}\}\_{n\geq 1}\subset\mathcal{W} such that Vtμ(n)↓V¯tV\_{t}^{\mu^{(n)}}\downarrow\underline{V}\_{t} and whose discrete intervention times satisfy τj(n)↓⌈t⌉+j\tau^{(n)}\_{j}\downarrow\lceil t\rceil+j with μx,j(n)=1−p^j\mu^{(n)}\_{x,j}=1-\hat{p}\_{j} for each j=0,…,⌊T⌋−⌈t⌉−1j=0,\dots,\lfloor T\rfloor-\lceil t\rceil-1 and with μx,c(n)≡0\mu\_{x,c}^{(n)}\equiv 0. This lower bound V¯t\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t} then satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t=∑j=0⌊T⌋−⌈t⌉−1Ct​(⌈t⌉+j,G⌈t⌉+jD)​(1−p^j)​∏i<jp^i.\displaystyle\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=\sum\_{j=0}^{\lfloor T\rfloor-\lceil t\rceil-1}C\_{t}(\lceil t\rceil+j,G^{D}\_{\lceil t\rceil+j})\,(1-\hat{p}\_{j})\,\prod\_{i<j}\,\hat{p}\_{i}\,. |  | (4.27) |

This case differs from the GMIB ([4.16](#S4.E16 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), where the policyholder continuously receives benefits while alive. In contrast, we here optimize the single, lump-sump benefit paid at the time of death and thus directly the contract price Ct​(τ,GτD)C\_{t}(\tau,G^{D}\_{\tau}), see the proof [A.3](#A1.SS3 "A.3. Proof of Proposition 4.5 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"). Moreover, Proposition [3.2](#S3.ThmTheorem2 "Proposition 3.2. ‣ 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") provides an analytical formula for Ct​(τ,GτD)C\_{t}(\tau,G^{D}\_{\tau}), which allows us to efficiently compute ([4.26](#S4.E26 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([4.27](#S4.E27 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). We also note that the assumption rg≥f​(t,s)r\_{g}\geq f(t,s) for all s∈[t,T]s\in[t,T] is a strong but practically relevant for GMDB contracts and makes this guarantee attractive for risk-averse policyholders. Although this proposition is stated under rather strong assumptions (necessary to obtain analytical expressions), these conditions can be relaxed but the corresponding optimal bounds then have to be computed numerically. Indeed, for more general payoffs H^​(As,GsD)\widehat{H}(A\_{s},G^{D}\_{s}) or when the assumptions rg≥f​(t,s)r\_{g}\geq f(t,s) and ([4.25](#S4.E25 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) do not hold, one can always use numerical techniques to solve the optimal stopping problems

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg​max/minτ∈𝒯(⌈t⌉+j,⌈t⌉+j+1]⁡𝔼ℚ​[e−∫tτrs​𝑑s​H^​(Aτ,GτD)|ℋt]\operatorname\*{arg\,max/min}\_{\tau\in\mathcal{T}\_{(\lceil t\rceil+j,\lceil t\rceil+j+1]}}\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{\tau}r\_{s}ds}\,\widehat{H}(A\_{\tau},G^{D}\_{\tau})\ \big|\ \mathcal{H}\_{t}\right] |  | (4.28) |

for each j=0,…,⌊T⌋−⌈t⌉−1j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1 as it is equivalent to the numerical pricing of ⌊T⌋−⌊t⌋\lfloor T\rfloor-\lfloor t\rfloor American options; see Cox et al. ([1979](#bib.bib3 "Option pricing: a simplified approach")) and Longstaff and Schwartz ([2001](#bib.bib7 "Valuing American options by simulation: A simple least-squares approach")). In the case this optimal intervention time τj∗\tau^{\*}\_{j} solving ([4.28](#S4.E28 "In 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) is not unique, we can then again simply choose arbitrarily one such τj∗\tau^{\*}\_{j} as we are only interested in practice in the bounds V¯t\bar{V}\_{t} (or V¯t\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}), and not the mortality rate μ∗\mu^{\*} itself.
  
  
As mentioned, the strict matching condition ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) with the given life table ([2.8](#S2.E8 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) is a strong setting, since in practice the observed mortality over each one-year period j=0,…,⌊T⌋−⌈t⌉−1j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1 will deviate from the tabulated p^j\hat{p}\_{j}. Theoretically, this almost-sure matching of the life tables also restricts the generality of the results in Propositions [4.3](#S4.ThmTheorem3 "Proposition 4.3 (GMAB bounds). ‣ 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")–[4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")–[4.5](#S4.ThmTheorem5 "Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") as we systematically obtain deterministic optimal mortality rates μ∗\mu^{\*}.
Section [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") will then relax the set of admissible controls and consider a more general framework, where this strict a.s. matching of the life table will be replaced by a constraint in expectation. This will allow us to consider a more realistic framework where mortality rate trajectories can deviate from the life table while still being consistent on average. Combining Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") will provide robust tools for managing the mortality risk of general variable annuities.

## 5 Bounds on variable annuities: matching life tables in expectation

In this section, we aim to derive worst- and best-case prices of variable annuities for mortality rate models that remain consistent with the initial life table but under weaker constraints. As mentioned above, we adopt a less restrictive constraint that requires only a matching of the initial life table in expectation. Moreover, the mortality intensity is assumed to be a general progressively measurable process with no explicit discrete component. Therefore, in this section, consistency is ensured by assuming that, for a given age xx, the mortality intensity μx\mu\_{x} is now a general positive progressively measurable process that satisfies the following constraints from ([2.7](#S2.E7 "In 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​(e−∫0jμx​(s)​𝑑s)=p^xj,j=1,⋯,n.\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right)={}\_{j}\hat{p}\_{x},\quad j=1,\cdots,n. |  | (5.1) |

where p^xj{}\_{j}\hat{p}\_{x} is again a tabulated value defined by,

|  |  |  |
| --- | --- | --- |
|  | p^xj:=∏i=0j−1p^i{}\_{j}\hat{p}\_{x}:=\prod\_{i=0}^{j-1}\hat{p}\_{i} |  |

with p^i:=px+i1=lx+i+1/lx+i\hat{p}\_{i}:={}\_{1}p\_{x+i}=l\_{x+i+1}/l\_{x+i}, see ([4.4](#S4.E4 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([4.5](#S4.E5 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). In that context, under Assumption [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), we aim to solve the following stochastic control problems associated to the worst- and best-case prices defined as777In contrast to the previous section, we adopt a general formulation based on the full combined product, since the dynamic programming approach used to solve the control problem wouldbe essentially the same if each product (GMAB, GMIB, GMDB) were formulated separately. See Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") for the definition of each payoff HH, H~\widetilde{H}, H^\widehat{H}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | supμx∈𝒜𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s],\displaystyle\sup\_{\mu\_{x}\in\mathcal{A}}\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G^{A}\_{T})+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G^{I}\_{s})+\mu\_{x}(s)\widehat{H}(A\_{s},G^{D}\_{s})\right)ds\Bigg], |  | (5.2) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | infμx∈𝒜𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s],\displaystyle\inf\_{\mu\_{x}\in\mathcal{A}}\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G^{A}\_{T})+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G^{I}\_{s})+\mu\_{x}(s)\widehat{H}(A\_{s},G^{D}\_{s})\right)ds\Bigg], |  | (5.3) |

with T=nT=n, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜:={μx:[0,T]×Ω→ℝ+prog. measurable process such that 𝔼ℙ(e−∫0jμx​(s)​𝑑s)=p^xj,j=1,⋯,n.}.\small\mathcal{A}:=\left\{\mu\_{x}:[0,T]\times\Omega\rightarrow\mathbb{R}^{+}\penalty 10000\ \text{prog. measurable process such that }\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right)={}\_{j}\hat{p}\_{x},\quad j=1,\cdots,n.\right\}. |  | (5.4) |

Depending on the structure of the payoff functional, those problems are potentially ill-posed or not tractable. That is why we decide to consider a regularized version of those problems, by restricting the set of admissible controls. For δ>0\delta>0, we introduce the admissible set of bounded controls 𝒜b​o​u​n​d​e​dδ\mathcal{A}^{\delta}\_{bounded} defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜b​o​u​n​d​e​dδ:=𝒜∩{μx:[0,T]×Ω→ℝ+such that for all t≤T,(μx,a(t)−δ)+≤μx(t)≤μx,a(t)+δa.s.},\small\mathcal{A}^{\delta}\_{bounded}:=\mathcal{A}\cap\left\{\mu\_{x}:[0,T]\times\Omega\rightarrow\mathbb{R}^{+}\penalty 10000\ \text{such that for all }t\leq T,\penalty 10000\ ({\mu\_{x,a}}(t)-\delta)\_{+}\leq\mu\_{x}(t)\leq{\mu\_{x,a}}(t)+\delta\penalty 10000\ a.s.\right\}, |  | (5.5) |

with μx,a​(t)\mu\_{x,a}(t) an a priori time-dependent mortality rate consistent with the initial observed life table such that e−∫0jμx,a​(t)​𝑑t=p^xj,e^{-\int\_{0}^{j}\mu\_{x,a}(t)dt}={}\_{j}\hat{p}\_{x}, for j=1,⋯,nj=1,\cdots,n888Typically, μx,a\mu\_{x,a} is obtained by a fractional age assumption.. In this setting, the stochastic control problems become

|  |  |  |  |
| --- | --- | --- | --- |
|  | supμx∈𝒜b​o​u​n​d​e​dδ𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s],\displaystyle\hskip-2.84526pt\sup\_{\mu\_{x}\in\mathcal{A}^{\delta}\_{bounded}}\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\int\_{0}^{T}\hskip-2.84526pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G^{I}\_{s})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg], |  | (5.6) |

and,

|  |  |  |  |
| --- | --- | --- | --- |
|  | infμx∈𝒜b​o​u​n​d​e​dδ𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s].\displaystyle\hskip-2.84526pt\inf\_{\mu\_{x}\in\mathcal{A}^{\delta}\_{bounded}}\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\int\_{0}^{T}\hskip-2.84526pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg]. |  | (5.7) |

Since we assume that the controls in the set 𝒜b​o​u​n​d​e​dδ\mathcal{A}^{\delta}\_{bounded} are bounded below and above by time-dependent functions consistent with the initial life table then, we can directly deduce that the problems ([5.6](#S5.E6 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([5.7](#S5.E7 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) are well-posed. Moreover, Proposition [5.4](#S5.ThmTheorem4 "Proposition 5.4. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") below shows that as δ→∞\delta\to\infty, the solutions to the regularized problems converge to the corresponding solutions of the original worst-case and best-case pricing problems.

The regularized control problems in ([5.6](#S5.E6 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([5.7](#S5.E7 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) share similarities with the framework of Li and Szimayer ([2011](#bib.bib10 "The uncertain mortality intensity framework: pricing and hedging unit-linked life insurance contracts")). However, rather than only assuming boundedness of the controlled process, we introduce the expectation constraints ([5.1](#S5.E1 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) to ensure consistency with observed life tables. In this sense, the problems are also closely connected to Avellaneda and Paras ([1996](#bib.bib40 "Managing the volatility risk of portfolios of derivative securities: the Lagrangian uncertain volatility model")), who derived bounds on financial derivative prices under volatility uncertainty while maintaining consistency with observed vanilla option prices. For the sake of clarity, we will mainly consider the problem related to the worst-case price, but similar developments can be deduced in the same manner for the problem related to the best case price. Using a dual approach, as done for instance in Motte and Hainaut ([2025](#bib.bib15 "Efficient hedging of life insurance portfolio for loss-averse insurers")), we can show that the stochastic control problem ([5.6](#S5.E6 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) is equivalent to the following problem (see proof of Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") below):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | inf𝝀∈ℝnsupμx∈𝒜~b​o​u​n​d​e​dδ𝔼ℚ[\displaystyle\inf\_{\boldsymbol{\lambda}\in\mathbb{R}^{n}}\hskip-1.42262pt\sup\_{\mu\_{x}\in\tilde{\mathcal{A}}^{\delta}\_{bounded}}\hskip-5.69054pt\mathbb{E}^{\mathbb{Q}}\Bigg[ | e−∫0T(ru+μx​(u))​𝑑uH(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u(H~(As,GsI)+μx(s)H^(As,GsD))ds]\displaystyle e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})\hskip-1.42262pt+\hskip-2.27621pt\int\_{0}^{T}\hskip-3.98337pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-1.42262pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})\hskip-1.42262pt+\hskip-1.42262pt\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\hskip-1.42262pt\right)ds\Bigg] |  | (5.8) |
|  |  | −∑j=1nλj​[𝔼ℙ​(e−∫0jμx​(s)​𝑑s)−p^xj],\displaystyle-\sum\_{j=1}^{n}\lambda\_{j}\left[\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right)-{}\_{j}\hat{p}\_{x}\right], |  |

with 𝝀:=(λ1,⋯,λn)∈ℝn\boldsymbol{\lambda}:=(\lambda\_{1},\cdots,\lambda\_{n})\in\mathbb{R}^{n} and, for δ>0\delta>0,

|  |  |  |
| --- | --- | --- |
|  | 𝒜~b​o​u​n​d​e​dδ:={μx:[0,T]×Ω→ℝ+s.t. for all t≤T,(μx,a(t)−δ)+≤μx(t)≤μx,a(t)+δa.s.}.\tilde{\mathcal{A}}^{\delta}\_{bounded}:=\left\{\mu\_{x}:[0,T]\times\Omega\rightarrow\mathbb{R}^{+}\penalty 10000\ \text{s.t.\ for all }t\leq T,\penalty 10000\ ({\mu\_{x,a}}(t)-\delta)\_{+}\leq\mu\_{x}(t)\leq{\mu\_{x,a}}(t)+\delta\penalty 10000\ a.s.\right\}. |  |

Let us show how to solve the inner problem using a dynamic programming approach. To this end, we assume that the unique change of measure process (Zt)0≤t≤T(Z\_{t})\_{0\leq t\leq T} defined by ([3.2](#S3.E2 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt:=exp⁡(−∫0t(μS−rsσS)​𝑑Ws1,ℙ−12​∫0t(μS−rsσS)2​𝑑s),0≤t≤T,Z\_{t}:=\exp\left(-\int\_{0}^{t}\left(\frac{\mu\_{S}-r\_{s}}{\sigma\_{S}}\right)d{W}\_{s}^{1,\mathbb{P}}-\frac{1}{2}\int\_{0}^{t}\left(\frac{\mu\_{S}-r\_{s}}{\sigma\_{S}}\right)^{2}ds\right),\quad 0\leq t\leq T, |  | (5.9) |

with μS\mu\_{S} the drift of the stock under the real measure ℙ\mathbb{P} and W1,ℙ{W}^{1,\mathbb{P}} a standard Brownian motion defined on ℙ\mathbb{P} such that

|  |  |  |
| --- | --- | --- |
|  | Wt1,ℙ:=Wt1,ℚ−∫0t(μS−rsσS)​𝑑s,0≤t≤T,{W}^{1,\mathbb{P}}\_{t}:=W^{1,\mathbb{Q}}\_{t}-\int\_{0}^{t}\left(\frac{\mu\_{S}-r\_{s}}{\sigma\_{S}}\right)ds,\quad 0\leq t\leq T, |  |

with W1,ℚ{W}^{1,\mathbb{Q}} the standard Brownian motion defined on ℚ\mathbb{Q} from Section [3](#S3 "3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").

###### Remark 5.1.

In our framework, we consider a complete financial market, which guarantees the uniqueness of the risk-neutral measure ℚ\mathbb{Q}.
Under ℚ\mathbb{Q}, the stock price (St)0≤t≤T(S\_{t})\_{0\leq t\leq T} has a drift equal to the short rate (rt)0≤t≤T(r\_{t})\_{0\leq t\leq T}, as required for arbitrage-free pricing.
For the short rate (rt)0≤t≤T(r\_{t})\_{0\leq t\leq T}, the change of measure from the physical measure ℙ\mathbb{P} to ℚ\mathbb{Q} generally involves a market price of risk (λtr)0≤t≤T(\lambda^{r}\_{t})\_{0\leq t\leq T}, which is calibrated in practice to match observed prices of traded instruments, such as zero-coupon bonds. For simplicity and consistency with Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), we assume that λtr=0\lambda^{r}\_{t}=0 for all 0≤t≤T0\leq t\leq T but other choices of (λtr)0≤t≤T(\lambda^{r}\_{t})\_{0\leq t\leq T} could be made.

Let us define the process Z~=(Z~t)0≤t≤T\tilde{Z}=(\tilde{Z}\_{t})\_{0\leq t\leq T} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~t:=e−∫0trs​𝑑s​Zt,0≤t≤T,\tilde{Z}\_{t}:=e^{-\int\_{0}^{t}r\_{s}ds}Z\_{t},\quad 0\leq t\leq T, |  | (5.10) |

with ZZ defined by ([5.9](#S5.E9 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). For 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, the inner problem in ([5.8](#S5.E8 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) can be rewritten as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supμx∈𝒜~b​o​u​n​d​e​dδ𝔼ℚ[\displaystyle\sup\_{\mu\_{x}\in\tilde{\mathcal{A}}^{\delta}\_{bounded}}\mathbb{E}^{\mathbb{Q}}\Bigg[ | e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)−∑j=1nλjZ~j​e−∫0j(rs+μx​(s))​𝑑s\displaystyle e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})-\sum\_{j=1}^{n}\frac{\lambda\_{j}}{\tilde{Z}\_{j}}e^{-\int\_{0}^{j}(r\_{s}+\mu\_{x}(s))ds} |  | (5.11) |
|  |  | +∫0Te−∫0s(ru+μx​(u))​𝑑u(H~(As,GsI)+μx(s)H^(As,GsD))ds].\displaystyle+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg]. |  |

To solve this control problem, for 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, we introduce the following value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯​(t,a,r,z;𝝀)=supμx∈𝒜~b​o​u​n​d​e​dδ​(t,T)\displaystyle\bar{v}(t,a,r,z;\boldsymbol{\lambda})=\hskip-2.84526pt\sup\_{\mu\_{x}\in\tilde{\mathcal{A}}^{\delta}\_{bounded}(t,T)}\hskip-2.84526pt | 𝔼t,a,r,zℚ[e−∫tT(ru+μx​(u))​𝑑uF(AT,GTA)−∑j=⌈t⌉nλjZ~je−∫tj(rs+μx​(s))​𝑑s\displaystyle\mathbb{E}\_{t,a,r,z}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{t}^{T}(r\_{u}+\mu\_{x}(u))du}F(A\_{T},G\_{T}^{A})-\sum\_{j=\lceil t\rceil}^{n}\frac{\lambda\_{j}}{\tilde{Z}\_{j}}e^{-\int\_{t}^{j}(r\_{s}+\mu\_{x}(s))ds} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫tTe−∫ts(ru+μx​(u))​𝑑u(H~(As,GsI)+μx(s)H(As,GsD))ds],\displaystyle\hskip-0.56905pt+\hskip-1.42262pt\int\_{t}^{T}\hskip-3.41432pte^{-\int\_{t}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-1.42262pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)H(A\_{s},G\_{s}^{D})\right)\hskip-0.85358ptds\Bigg],\hskip-2.84526pt |  | (5.12) |

where 𝔼t,a,r,zℚ(.)\mathbb{E}^{\mathbb{Q}}\_{t,a,r,z}(.) denotes the conditional expectation given At=aA\_{t}=a, rt=rr\_{t}=r, Z~t=z\tilde{Z}\_{t}=z, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜b​o​u​n​d​e​dδ(t,T):={μx:[t,T]×Ω→ℝ+s.t. for all s∈[t,T],(μx,a(s)−δ)+≤μx(t)≤μx,a(s)+δa.s.}.\small\mathcal{A}^{\delta}\_{bounded}(t,T):=\left\{\mu\_{x}:[t,T]\times\Omega\rightarrow\mathbb{R}^{+}\penalty 10000\ \text{s.t.\ for all }s\in[t,T],\penalty 10000\ ({\mu\_{x,a}}(s)-\delta)\_{+}\leq\mu\_{x}(t)\leq{\mu\_{x,a}}(s)+\delta\penalty 10000\ a.s.\right\}. |  | (5.13) |

Let us define Aδ​(t)A^{\delta}(t) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aδ​(t):=[(μx,a​(t)−δ)+,μx,a​(t)+δ],t≤T.A^{\delta}(t):=[(\mu\_{x,a}(t)-\delta)\_{+},\mu\_{x,a}(t)+\delta],\quad t\leq T. |  | (5.14) |

Classical results from dynamic programming (see for instance Touzi ([2012](#bib.bib13 "Optimal stochastic control, stochastic target problems, and backward sde"))) suggest that the value function associated to the inner problem solves the following Hamilton-Jacobi-Bellman (HJB) equation, for t∈(j−1,j)t\in({j-1},j), j=1,…,nj=1,...,n:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supμx∈Aδ​(t)[ℒt,a,r,z​v¯​(t,a,r,z;𝝀)+H~​(a,GtI)+μx​(H^​(a,GtD)−v¯​(t,a,r,z;𝝀))]=0,\displaystyle\sup\_{\mu\_{x}\in A^{\delta}(t)}\left[\mathcal{L}\_{t,a,r,z}\bar{v}(t,a,r,z;\boldsymbol{\lambda})+\widetilde{H}(a,G\_{t}^{I})+\mu\_{x}\left(\widehat{H}(a,G\_{t}^{D})-\bar{v}(t,a,r,z;\boldsymbol{\lambda})\right)\right]=0, |  | (5.15) |

with boundary conditions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | v¯​(n,a,r,z;𝝀)=H​(a,GtnA)−λnz,\displaystyle\bar{v}(n,a,r,z;\boldsymbol{\lambda})=H(a,G\_{t\_{n}}^{A})-\frac{\lambda\_{n}}{z}, |  | (5.16) |
|  |  | v¯​(j−,a,r,z;𝝀)=v¯​(j+,a,r,z;𝝀)−λjz,j=1,…,n−1,\displaystyle\bar{v}({j}^{-},a,r,z;\boldsymbol{\lambda})=\bar{v}({j}^{+},a,r,z;\boldsymbol{\lambda})-\frac{\lambda\_{j}}{z},\quad j=1,.,n-1, |  |

where ℒt,a,r,z\mathcal{L}\_{t,a,r,z} is the classical generator associated with (At)0≤t≤T(A\_{t})\_{0\leq t\leq T} given by ([3.6](#S3.E6 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), (rt)0≤t≤T(r\_{t})\_{0\leq t\leq T} given by ([3.1](#S3.E1 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), and (Z~t)0≤t≤T(\tilde{Z}\_{t})\_{0\leq t\leq T} given by ([5.10](#S5.E10 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).
Since ([5.15](#S5.E15 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) depends linearly on μ\mu, we deduce that, for j=1,⋯,nj=1,\cdots,n and t∈(j−1,j)t\in({j-1},{j}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | supμx∈Aδ​(t)\displaystyle\sup\_{\mu\_{x}\in A^{\delta}(t)} | μx​(H^​(a,GtD)−v¯​(t,a,r,z;𝝀))=\displaystyle\mu\_{x}\left(\widehat{H}(a,G\_{t}^{D})-\bar{v}(t,a,r,z;\boldsymbol{\lambda})\right)= |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | {(H^​(a,GtD)−v¯​(t,a,r,z;𝝀))​(μx,a​(t)−δ)+,if ​H^​(a,GtD)<v¯​(t,a,r,z;𝝀),(H^​(a,GtD)−v¯​(t,a,r,z;𝝀))​(μx,a​(t)+δ),if ​H^​(a,GtD)≥v¯​(t,a,r,z;𝝀).\displaystyle\begin{cases}\left(\widehat{H}(a,G\_{t}^{D})-\bar{v}(t,a,r,z;\boldsymbol{\lambda})\right)\left(\mu\_{x,a}(t)-\delta\right)\_{+},&\text{if }\widehat{H}(a,G\_{t}^{D})<\bar{v}(t,a,r,z;\boldsymbol{\lambda}),\\ \left(\widehat{H}(a,G\_{t}^{D})-\bar{v}(t,a,r,z;\boldsymbol{\lambda})\right)\left(\mu\_{x,a}(t)+\delta\right),&\text{if }\widehat{H}(a,G\_{t}^{D})\geq\bar{v}(t,a,r,z;\boldsymbol{\lambda}).\end{cases} |  |

Therefore, the maximizer μ¯x∗\bar{\mu}\_{x}^{\*} is given by, for j=1,⋯,nj=1,\cdots,n and t∈(j−1,j)t\in({j-1},{j}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ¯x∗​(t,a,r,z;𝝀)={(μx,a​(t)−δ)+,if ​H^​(a,GtD)<v¯​(t,a,r,z;𝝀),(μx,a​(t)+δ),if ​H^​(a,GtD)≥v¯​(t,a,r,z;𝝀).\displaystyle{\bar{\mu}}\_{x}^{\*}(t,a,r,z;\boldsymbol{\lambda})=\begin{cases}(\mu\_{x,a}(t)-\delta)\_{+},&\text{if }\widehat{H}(a,G\_{t}^{D})<\bar{v}(t,a,r,z;\boldsymbol{\lambda}),\\ (\mu\_{x,a}(t)+\delta),&\text{if }\widehat{H}(a,G\_{t}^{D})\geq\bar{v}(t,a,r,z;\boldsymbol{\lambda}).\end{cases} |  | (5.17) |

Plugging this into the HJB equation ([5.15](#S5.E15 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), we deduce that candidate value function satisfies the following nonlinear PDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℒt,a,r,z​v¯​(t,a,r,z;𝝀)+H~​(a,GtI)+μ¯x∗​(t,a,r,z;𝝀)​(H^​(a,GtD)−v¯​(t,a,r,z;𝝀))=0,\displaystyle\mathcal{L}\_{t,a,r,z}\bar{v}(t,a,r,z;\boldsymbol{\lambda})+\widetilde{H}(a,G\_{t}^{I})+{\bar{\mu}}\_{x}^{\*}(t,a,r,z;\boldsymbol{\lambda})\left(\widehat{H}(a,G\_{t}^{D})-\bar{v}(t,a,r,z;\boldsymbol{\lambda})\right)=0, |  | (5.18) |

with boundary conditions given by ([5.16](#S5.E16 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).

Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") shows that under mild regularity assumptions, the candidate value function solution of the HJB equation is effectively the solution to the regularized inner control problem associated to the worst case price. Proposition [5.3](#S5.ThmTheorem3 "Proposition 5.3. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") derives an analogue result for the the best case problem. Finally, Proposition [5.4](#S5.ThmTheorem4 "Proposition 5.4. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") shows that the solutions of the regularized problems converge toward the solutions of the original worst- and best-case problems given by ([5.2](#S5.E2 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([5.3](#S5.E3 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). Proofs are once again deferred in [A](#A1 "Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").

###### Proposition 5.2.

For any 𝛌∈ℝn\bm{\lambda}\in\mathbb{R}^{n}, let assume that there exists v¯​(t,a,r,z;𝛌)∈C1,2,2,2\bar{v}(t,a,r,z;\boldsymbol{\lambda})\in C^{1,2,2,2} solution to ([5.18](#S5.E18 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). Then, v¯​(t,a,r,z;𝛌)\bar{v}(t,a,r,z;\boldsymbol{\lambda}) solves the stochastic control problem ([5](#S5.Ex4 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), and the associated optimal mortality rate is given by ([5.17](#S5.E17 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). In particular, for 𝛌∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, v¯​(0,A0,r0,Z0;𝛌)\bar{v}(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}) solves the initial inner problem such that

|  |  |  |
| --- | --- | --- |
|  | v¯​(0,A0,r0,Z0;𝝀)\displaystyle\bar{v}(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}) |  |
|  |  |  |
| --- | --- | --- |
|  | =supμx∈𝒜~b​o​u​n​d​e​dδ𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle=\hskip-1.42262pt\sup\_{\mu\_{x}\in\tilde{\mathcal{A}}^{\delta}\_{bounded}}\hskip-2.84526pt\mathbb{E}^{\mathbb{Q}}\Bigg[e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\hskip-1.99168pt\int\_{0}^{T}\hskip-2.84526pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-1.13809pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-1.13809ptds\Bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | −∑j=1nλj​𝔼ℙ​(e−∫0jμx​(s)​𝑑s).\displaystyle\hskip 56.9055pt-\sum\_{j=1}^{n}\lambda\_{j}\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right). |  |

Moreover, the infimum of 𝛌↦(v¯​(0,A0,r0,Z0;𝛌)+∑j=1nλj​p^xj)\boldsymbol{\lambda}\mapsto\left(\bar{v}(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda})+\sum\_{j=1}^{n}\lambda\_{j}\,{}\_{j}\hat{p}\_{x}\right) over 𝛌∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n} is attained at some 𝛌∗∈ℝn\boldsymbol{\lambda}^{\*}\in\mathbb{R}^{n}; hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯∗​(0,A0,r0,Z0):=v¯​(0,A0,r0,Z0;𝝀∗)+∑j=1nλj∗​p^xj=min𝝀∈ℝn⁡[v¯​(0,A0,r0,Z0;𝝀)+∑j=1nλj​p^xj],\bar{v}\_{\*}(0,A\_{0},r\_{0},Z\_{0}):=\bar{v}(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}^{\*})+\sum\_{j=1}^{n}\lambda^{\*}\_{j}\,{}\_{j}\hat{p}\_{x}=\min\_{\boldsymbol{\lambda}\in\mathbb{R}^{n}}\left[\bar{v}(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda})+\sum\_{j=1}^{n}\lambda\_{j}\,{}\_{j}\hat{p}\_{x}\right], |  | (5.19) |

is well-defined and is the solution of the regularized worst-case price problem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v¯∗(0,A0,r0,Z0)=supμx∈𝒜b​o​u​n​d​e​dδ𝔼ℚ[\displaystyle\bar{v}\_{\*}(0,A\_{0},r\_{0},Z\_{0})=\sup\_{\mu\_{x}\in\mathcal{A}^{\delta}\_{bounded}}\mathbb{E}^{\mathbb{Q}}\Bigg[ | e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)\displaystyle\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A}) |  | (5.20) |
|  |  | +∫0Te−∫0s(ru+μx​(u))​𝑑u(H~(As,GsI)+μx(s)H^(As,GsD))ds].\displaystyle+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg]. |  |

###### Proposition 5.3.

For any 𝛌∈ℝn\bm{\lambda}\in\mathbb{R}^{n}, let assume that, there exists v¯​(t,a,r,z;𝛌)∈C1,2,2,2\underline{v\mkern-4.0mu}\mkern 4.0mu(t,a,r,z;\boldsymbol{\lambda})\in C^{1,2,2,2} solution to the following nonlinear PDE, for t∈(j−1,j),t\in({j-1},j), j=1,…,nj=1,...,n,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℒt,a,r,z​v¯​(t,a,r,z;𝝀)+H~​(a,GtI)+μ¯x∗​(t,a,r,z;𝝀)​(H^​(a,GtD)−v¯​(t,a,r,z;𝝀))=0,\displaystyle\mathcal{L}\_{t,a,r,z}\underline{v\mkern-4.0mu}\mkern 4.0mu(t,a,r,z;\boldsymbol{\lambda})+\widetilde{H}(a,G\_{t}^{I})+{\underline{\mu\mkern-4.0mu}\mkern 4.0mu}\_{x}^{\*}(t,a,r,z;\boldsymbol{\lambda})\left(\widehat{H}(a,G\_{t}^{D})-\underline{v\mkern-4.0mu}\mkern 4.0mu(t,a,r,z;\boldsymbol{\lambda})\right)=0, |  | (5.21) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ¯x∗​(t,a,r,z;𝝀)={(μx,a​(t)−δ)+,if ​H^​(a,GtD)>v¯​(t,a,r,z;𝝀),(μx,a​(t)+δ),if ​H^​(a,GtD)≤v¯​(t,a,r,z;𝝀),\displaystyle{\underline{\mu\mkern-4.0mu}\mkern 4.0mu}\_{x}^{\*}(t,a,r,z;\boldsymbol{\lambda})=\begin{cases}(\mu\_{x,a}(t)-\delta)\_{+},&\text{if }\widehat{H}(a,G\_{t}^{D})>\underline{v\mkern-4.0mu}\mkern 4.0mu(t,a,r,z;\boldsymbol{\lambda}),\\ (\mu\_{x,a}(t)+\delta),&\text{if }\widehat{H}(a,G\_{t}^{D})\leq\underline{v\mkern-4.0mu}\mkern 4.0mu(t,a,r,z;\boldsymbol{\lambda}),\end{cases} |  | (5.22) |

that satisfies the following boundary conditions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | v¯​(n,a,r,z;𝝀)=H​(a,GtnA)+λnz,\displaystyle\underline{v\mkern-4.0mu}\mkern 4.0mu(n,a,r,z;\boldsymbol{\lambda})=H(a,G\_{t\_{n}}^{A})+\frac{\lambda\_{n}}{z}, |  | (5.23) |
|  |  | v¯​(j−,a,r,z;𝝀)=v¯​(j+,a,r,z;𝝀)+λjz,j=1,…,n−1.\displaystyle\underline{v\mkern-4.0mu}\mkern 4.0mu(j^{-},a,r,z;\boldsymbol{\lambda})=\underline{v\mkern-4.0mu}\mkern 4.0mu(j^{+},a,r,z;\boldsymbol{\lambda})+\frac{\lambda\_{j}}{z},\quad j=1,.,n-1. |  |

Then, for 𝛌∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, v¯​(0,A0,r0,Z0;𝛌)\underline{v\mkern-4.0mu}\mkern 4.0mu(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}) solves the initial inner problem such that

|  |  |  |
| --- | --- | --- |
|  | v¯​(0,A0,r0,Z0;𝝀)\displaystyle\underline{v\mkern-4.0mu}\mkern 4.0mu(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}) |  |
|  |  |  |
| --- | --- | --- |
|  | =infμx∈𝒜~b​o​u​n​d​e​dδ𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle=\hskip-1.99168pt\inf\_{\mu\_{x}\in\tilde{\mathcal{A}}^{\delta}\_{bounded}}\hskip-3.69885pt\mathbb{E}^{\mathbb{Q}}\Bigg[e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\hskip-1.42262pt\int\_{0}^{T}\hskip-3.1298pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-0.7113pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-0.7113ptds\Bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | +∑j=1nλj​𝔼ℙ​(e−∫0jμx​(s)​𝑑s).\displaystyle\hskip 56.9055pt+\sum\_{j=1}^{n}\lambda\_{j}\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right). |  |

Moreover, the supremum of 𝛌↦(v¯​(0,A0,r0,Z0;𝛌)−∑j=1nλj​p^xj)\boldsymbol{\lambda}\mapsto\left(\underline{v\mkern-4.0mu}\mkern 4.0mu(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda})-\sum\_{j=1}^{n}\lambda\_{j}\,{}\_{j}\hat{p}\_{x}\right) over 𝛌∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n} is attained at some 𝛌∗∈ℝn\boldsymbol{\lambda}^{\*}\in\mathbb{R}^{n}; hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯∗​(0,A0,r0,Z0):=v¯​(0,A0,r0,Z0;𝝀∗)−∑j=1nλj∗​p^xj=max𝝀>0⁡[v¯​(0,A0,r0,Z0;𝝀)−∑j=1nλj​p^xj],\underline{v\mkern-4.0mu}\mkern 4.0mu\_{\*}(0,A\_{0},r\_{0},Z\_{0}):=\underline{v\mkern-4.0mu}\mkern 4.0mu(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}^{\*})-\sum\_{j=1}^{n}\lambda^{\*}\_{j}\,{}\_{j}\hat{p}\_{x}=\max\_{\boldsymbol{\lambda}>0}\left[\underline{v\mkern-4.0mu}\mkern 4.0mu(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda})-\sum\_{j=1}^{n}\lambda\_{j}{}\_{j}\hat{p}\_{x}\right], |  | (5.24) |

is well-defined and is the solution of the regularized best-case price problem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v¯∗(0,A0,r0,Z0)=infμx∈𝒜b​o​u​n​d​e​dδ𝔼ℚ[\displaystyle\underline{v\mkern-4.0mu}\mkern 4.0mu\_{\*}(0,A\_{0},r\_{0},Z\_{0})=\inf\_{\mu\_{x}\in\mathcal{A}^{\delta}\_{bounded}}\mathbb{E}^{\mathbb{Q}}\Bigg[ | e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)\displaystyle\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A}) |  | (5.25) |
|  |  | +∫0Te−∫0s(ru+μx​(u))​𝑑u(H~(As,GsI)+μx(s)H^(As,GsD))ds].\displaystyle+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg]. |  |

###### Proof.

The proof follows by arguments analogous to the proof of Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
∎

###### Proposition 5.4.

Let us assume that the assumptions of Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and [5.3](#S5.ThmTheorem3 "Proposition 5.3. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") are satisfied. For δ>0\delta>0, let v¯∗δ​(0,A0,r0,Z0)\bar{v}^{\delta}\_{\*}(0,A\_{0},r\_{0},Z\_{0}) and v¯∗δ​(0,A0,r0,Z0)\underline{v\mkern-4.0mu}\mkern 4.0mu^{\delta}\_{\*}(0,A\_{0},r\_{0},Z\_{0}) denote the solution to the worst- and best-case price problems given by ([5.6](#S5.E6 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([5.7](#S5.E7 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). Moreover, let 𝒜~\tilde{\mathcal{A}} be the set of bounded controls belonging to 𝒜\mathcal{A}. Then, we have that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supμx∈𝒜~𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\sup\_{\mu\_{x}\in\tilde{\mathcal{A}}}\mathbb{E}^{\mathbb{Q}}\Bigg[e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\hskip-1.42262pt\int\_{0}^{T}\hskip-2.84526pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-1.13809pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-1.13809ptds\Bigg] |  | (5.26) |
|  |  | =limδ→∞v¯∗δ​(0,A0,r0,Z0),\displaystyle\hskip 14.22636pt=\lim\_{\delta\to\infty}\bar{v}^{\delta}\_{\*}(0,A\_{0},r\_{0},Z\_{0}), |  |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | infμx∈𝒜~𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\inf\_{\mu\_{x}\in\tilde{\mathcal{A}}}\mathbb{E}^{\mathbb{Q}}\Bigg[e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\hskip-1.42262pt\int\_{0}^{T}\hskip-3.41432pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-1.13809pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-1.13809ptds\Bigg] |  | (5.27) |
|  |  | =limδ→∞v¯∗δ​(0,A0,r0,Z0).\displaystyle\hskip 14.22636pt=\lim\_{\delta\to\infty}\underline{v\mkern-4.0mu}\mkern 4.0mu^{\delta}\_{\*}(0,A\_{0},r\_{0},Z\_{0}). |  |

## 6 Numerical experiments

Since our method in Section [4](#S4 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and [5](#S5 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") does not rely on any specific mortality modeling assumptions, the resulting bounds provided below are the most general one can obtain using the
available information (provided that the mortality rates over each one-year period are consistent with the given table). These bounds are therefore of high practical interest for insurers, as they naturally provide a range within which the contract price should lie. Any price outside this range is either not consistent with the life tables or with the assumed financial market. Finally, these results allow the insurer to directly quantify its worst-case loss or best-case gain in case of deviation of the observed mortality from the chosen fractional-age/mortality rate assumption. The results are based on the Belgian female life table.

### 6.1. Strict bounds

The parameters used in this section are
A0=100A\_{0}=100, rg=0.03r\_{g}=0.03, r0=0.01r\_{0}=0.01, πS=0.6\pi\_{S}=0.6, πP=0.2\pi\_{P}=0.2, σS=0.2\sigma\_{S}=0.2, σr=0.02\sigma\_{r}=0.02, ρ=0.3\rho=0.3, and κ=0.1\kappa=0.1.
The mean-reversion interest rate level θ​(t)\theta(t) is obtained from ([3.3](#S3.E3 "In 3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) by specifying the instantaneous forward rate as

|  |  |  |
| --- | --- | --- |
|  | f​(0,t)=b+c​e−a​t+d​a​t​e−a​t,a,b,c,d∈ℝ,f(0,t)=b+ce^{-at}+date^{-at},\qquad a,b,c,d\in\mathbb{R}, |  |

with yield-curve parameters a=0.015a=0.015, b=−0.0105b=-0.0105, c=0.02c=0.02, and d=0.75d=0.75.
We first depict in Figure [6.1](#S6.F1 "Figure 6.1 ‣ 6.1. Strict bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") the survival probabilities pxt{}\_{t}p\_{x} at age x=40x=40 and x=100x=100 for t∈[0,5]t\in[0,5]. Naturally, at lower age xx, we see that the specific choice of fractional age assumption has almost no impact on the survival probabilities, while we observe higher discrepancies for x=100x=100. By contrast, the GMIB- and GMDB-induced optimal survival curves p¯x∗t{}\_{t}\bar{p}^{\*}\_{x} and p¯x∗t{}\_{t}\underline{p\mkern-4.0mu}\mkern 4.0mu^{\*}\_{x}, given by ([4.20](#S4.E20 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), deviate significantly from all the fractional age assumptions.

![Refer to caption](2603.06238v1/x1.png)

![Refer to caption](2603.06238v1/x2.png)

Figure 6.1: Comparison of survival probabilities pxt{}\_{t}p\_{x} at age x=40x=40 (left) and x=100x=100 (right) over time t∈[0,5]t\in[0,5], using the fractional age assumptions ([2.9](#S2.E9 "In 1st item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))-([2.11](#S2.E11 "In 3rd item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and optimal GMIB (and GMDB) p¯x∗t{}\_{t}\bar{p}^{\*}\_{x} (’Sup’), p¯x∗t{}\_{t}\underline{p\mkern-4.0mu}\mkern 4.0mu^{\*}\_{x} (’Inf’) from Eqs. ([4.20](#S4.E20 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).



![Refer to caption](2603.06238v1/x3.png)

![Refer to caption](2603.06238v1/x4.png)

![Refer to caption](2603.06238v1/x5.png)

Figure 6.2: GMIB contract price VtμV^{\mu}\_{t} at t=0t=0 for different maturities TT with initial age x=40x=40 (top left), x=60x=60 (top right) and x=80x=80 (bottom). Results are shown under the fractional-age assumptions ([2.9](#S2.E9 "In 1st item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([2.11](#S2.E11 "In 3rd item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), together with the GMIB upper bound V¯0\bar{V}\_{0} (’Sup’) and lower bound V¯0\underline{V\mkern-4.0mu}\mkern 4.0mu\_{0} (’Inf’) from Eqs. ([4.19](#S4.E19 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([4.21](#S4.E21 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).



![Refer to caption](2603.06238v1/x6.png)

![Refer to caption](2603.06238v1/x7.png)

![Refer to caption](2603.06238v1/x8.png)

Figure 6.3: GMDB contract price VtμV^{\mu}\_{t} at t=0t=0 for different maturities TT with initial age x=40x=40 (top left), x=60x=60 (top right) and x=80x=80 (bottom). Results are shown under the fractional-age assumptions ([2.9](#S2.E9 "In 1st item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([2.11](#S2.E11 "In 3rd item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), together with the GMDB upper bound V¯0\bar{V}\_{0} (’Sup’) and lower bound V¯0\underline{V\mkern-4.0mu}\mkern 4.0mu\_{0} (’Inf’) from Eqs. ([4.26](#S4.E26 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([4.27](#S4.E27 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).

We then study the strict bounds of the GMIB contract in Figure [6.2](#S6.F2 "Figure 6.2 ‣ 6.1. Strict bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"). For younger policyholders (smaller initial age xx), the upper-left plot shows that the insurer’s exposure to deviations of mortality within each one-year period from the chosen fractional-age assumption is moderate, at least for relatively short maturities TT (while remaining consistent with the tabulated survival probabilities p^j\hat{p}\_{j}’s). In contrast, for older policyholders (bottom plot) or for longer maturities, this mortality risk becomes much more significant, as deviations within each one-year period from the fractional-age assumption lead to a stronger impact on the GMIB value. We also observe that the choice among the three fractional-age assumptions ([2.9](#S2.E9 "In 1st item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([2.11](#S2.E11 "In 3rd item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) has virtually no impact on the contract price. All these observations are confirmed for the GMDB bounds in Figure [6.3](#S6.F3 "Figure 6.3 ‣ 6.1. Strict bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"). Bounds for the GMAB contract are not depicted as they are trivial in the strict pathwise setting, see Proposition [4.3](#S4.ThmTheorem3 "Proposition 4.3 (GMAB bounds). ‣ 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").

### 6.2. Relaxed bounds

For clarity, in this section we consider a deterministic interest rate r=0.01r=0.01 and set the market price of risk to zero (μS=r\mu\_{S}=r), which reduces the Hamilton–Jacobi–Bellman (HJB) equations from four state variables to only two. While this simplification ignores stochastic interest rate effects, the qualitative behavior of bounds is expected to remain similar in the full four-state formulation. The other parameters used in the numerical examples are the same as in Section [6.1](#S6.SS1 "6.1. Strict bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") above with δ=1\delta=1. Moreover, the a priori time-dependent mortality rate μx,a\mu\_{x,a} is given by the Balducci approximation. We compare different variable annuities prices:

* •

  Prices obtained by using the Balducci approximation,
* •

  Worst- and best-case prices by imposing expected constraints only at maturity TT,
* •

  Worst- and best-case prices by imposing expected constraints for each intermediate maturities j≤Tj\leq T,
* •

  Worst- and best-case prices by imposing almost surely constraints for each intermediate maturities j≤Tj\leq T.

Figures [6.4](#S6.F4 "Figure 6.4 ‣ 6.2. Relaxed bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), [6.5](#S6.F5 "Figure 6.5 ‣ 6.2. Relaxed bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and [6.6](#S6.F6 "Figure 6.6 ‣ 6.2. Relaxed bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") display the upper and lower bounds (worst- and best-cases prices) for GMAB, GMIB, and GMDB for policyholder ages x=40,60,80x=40,60,80. Comparing expected bounds with almost-sure bounds, it is clear that the expected bounds are less restrictive, as they only enforce average behavior over time rather than across all possible mortality trajectories. Consequently, the expected bounds are always wider than the almost-sure bounds. Note that for GMAB, the almost-sure bounds coincide with the price under Balducci approximation, so they are not displayed; for GMIB and GMDB, the almost-sure bounds are tighter and lie closer to the baseline.

Moreover, we observe that adding additional constraints at intermediate times further narrows the bounds, as they restrict extreme mortality trajectories that would otherwise satisfy the final maturity condition but produce very high or very low liabilities along the path. The effect of these intermediate-time constraints is stronger for GMIB and GMDB than for GMAB because GMIB and GMDB payoffs depend on survival or death at intermediate times, whereas GMAB depends primarily on survival at maturity TT.

We also observe asymmetry in the bounds, when comparing upper and lower bounds to the baseline. This asymmetry depends on the nature of the payoff. For survival-contingent products such as GMIB and GMAB, the lower bounds are typically far below the baseline, reflecting the strong impact of higher mortality on survival-dependent liabilities, while the upper bounds remain closer. For death-contingent products such as GMDB, the opposite pattern is observed: the upper bounds lie far above the baseline, as higher mortality increases the present value of death benefits, whereas the lower bounds remain near the baseline, since reductions in mortality have limited effect. Those asymmetrical effects are reduced for older ages, as survival probabilities decrease.

![Refer to caption](2603.06238v1/Figs/GMAB_40.png)

![Refer to caption](2603.06238v1/Figs/GMAB_60.png)

![Refer to caption](2603.06238v1/Figs/GMAB_80.png)

Figure 6.4: GMAB contract price for different maturities T∈{1,2,3,5,7,10,15}T\in\{1,2,3,5,7,10,15\} with initial age x=40x=40 (top left), x=60x=60. (top right) and x=80x=80 (bottom). Results are shown under the Balducci assumption ([2.11](#S2.E11 "In 3rd item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), together with the optimal relaxed bounds from Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") – [5.3](#S5.ThmTheorem3 "Proposition 5.3. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")



![Refer to caption](2603.06238v1/Figs/GMIB_40.png)

![Refer to caption](2603.06238v1/Figs/GMIB_60.png)

![Refer to caption](2603.06238v1/Figs/GMIB_80.png)

Figure 6.5: GMIB contract price for different maturities T∈{1,2,3,5,7,10,15}T\in\{1,2,3,5,7,10,15\} with initial age x=40x=40 (top left), x=60x=60. (top right) and x=80x=80 (bottom). Results are shown under the Balducci assumption ([2.11](#S2.E11 "In 3rd item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), together with the optimal relaxed bounds from Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")–[5.3](#S5.ThmTheorem3 "Proposition 5.3. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and a.s. bounds from Eqs. ([4.19](#S4.E19 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([4.21](#S4.E21 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))



![Refer to caption](2603.06238v1/Figs/GMDB_40.png)

![Refer to caption](2603.06238v1/Figs/GMDB_60.png)

![Refer to caption](2603.06238v1/Figs/GMDB_80.png)

Figure 6.6: GMDB contract price for different maturities T∈{1,2,3,5,7,10,15}T\in\{1,2,3,5,7,10,15\} with initial age x=40x=40 (top left), x=60x=60. (top right) and x=80x=80 (bottom). Results are shown under the Balducci assumption ([2.11](#S2.E11 "In 3rd item ‣ 2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), together with the optimal relaxed bounds from Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")–[5.3](#S5.ThmTheorem3 "Proposition 5.3. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") and a.s. bounds from Eqs. ([4.26](#S4.E26 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"))–([4.27](#S4.E27 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")).

We also check the convergence of the upper and lower bounds with expected constraints only at maturity, as δ→∞\delta\to\infty. Figure [6.7](#S6.F7 "Figure 6.7 ‣ 6.2. Relaxed bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") displays the upper and lower bond prices for x=60x=60 and T=5T=5, plotted as functions of δ>0\delta>0. As expected, we observe a relative fast convergence as δ\delta increases, confirming the theoretical result of Proposition [5.4](#S5.ThmTheorem4 "Proposition 5.4. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").

![Refer to caption](2603.06238v1/Figs/GMAB_60_delta.png)

![Refer to caption](2603.06238v1/Figs/GMIB_60_delta.png)

![Refer to caption](2603.06238v1/Figs/GMDB_60_delta.png)

Figure 6.7:  Optimal relaxed bounds from Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")–[5.3](#S5.ThmTheorem3 "Proposition 5.3. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") with expected constraint only at maturity TT as functions of δ>0\delta>0, for GMAB, GMIB and GMDB contract prices with initial age x=60x=60 and maturity T=5T=5.

We conclude this numerical section with some remarks on the computational aspects of the problem and the methodological choices adopted in its resolution. The original control problems are formulated as a four-dimensional HJB equations with multiple time constraints on [0,T][0,T]. This leads to a sequence of recursive HJB equations, which becomes computationally very demanding, especially for large maturities. In addition, the numerical resolution requires solving a high-dimensional static optimization problem with respect to 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, which further increases the computational burden and slows convergence. To ensure tractable computation and reliable numerical results, we decide to reduce the state space to two variables. The full four-dimensional formulation, with stochastic interest rates, could in principle be addressed using modern deep-learning-based methods for high-dimensional control problems instead of the finite-difference scheme used above, see for example Cheridito et al. ([2025](#bib.bib27 "Deep learning for continuous-time stochastic control with jumps")), Dupret and Hainaut ([2026](#bib.bib26 "Deep learning for high-dimensional continuous-time stochastic optimal control without explicit solution")), which are specifically designed to handle such large systems of recursive HJB equations. Let us also note that the previous section provides alternative almost-sure bounds obtained under stronger and less realistic assumptions. Although more restrictive, these bounds are fast to compute and can be derived directly. They thus serve as useful a priori estimates and sanity checks for the numerical results.

## 7 Conclusion

This paper addresses a structural source of model risk in life insurance: life tables provide survival probabilities at integer ages but leave the within-year timing of deaths unspecified, even though many life-contingent liabilities (e.g. variable annuities) depend on the full continuous-time lifetime distribution. Rather than postulating a fractional-age assumption (UDD/CFM/Balducci) or a parametric (deterministic or stochastic) mortality rate model, we develop a model-free mortality framework that characterizes the set of admissible mortality intensities compatible with the tabulated one-year survival probabilities and then derives sharp upper and lower bounds for actuarial functionals over that set. We present two distinct yet complementary approaches. In the strict (pathwise) matching regime, admissible mortality trajectories must reproduce each observed one-year survival probability almost surely. Because strict matching is often too restrictive empirically and lead to deterministic optimal mortality rates, we then study a relaxed regime where life-table constraints are matched in expectation. To avoid the control problem to be ill-posed, we introduce a regularized admissible set around a baseline mortality intensity consistent with the table, and solve the resulting robust control problem via a dual formulation with Lagrange multipliers and dynamic programming. Numerical experiments confirm intuitive patterns: (i) expectation-based bounds are wider than almost-sure bounds; (ii) adding intermediate-time constraints tightens bounds substantially for GMIB/GMDB; and (iii) the bound asymmetry depends on whether the payoff is survival- or death-contingent, with the effect diminishing at very old ages as survival probabilities shrink. Overall, the proposed bounds provide a practical, model-free mortality risk-management layer on top of any chosen financial model.

## Appendix A Proofs

### A.1. Proof of Proposition [4.3](#S4.ThmTheorem3 "Proposition 4.3 (GMAB bounds). ‣ 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")

###### Proof.

Using ([4.9](#S4.E9 "In 4.1. Guaranteed Minimum Accumulation Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) and ([4.5](#S4.E5 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), we have that for every μ∈𝒲\mu\in\mathcal{W},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtμ\displaystyle V^{\mu}\_{t} | =𝔼ℚ​[(∏j=0⌊T⌋−⌈t⌉−1p^j)​e−∫tTrs​𝑑s​H​(AT,GTA)|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\left(\hskip-0.28453pt\prod\_{j=0}^{\lfloor T\rfloor-\lceil t\rceil-1}\hskip-2.84526pt\hat{p}\_{j}\right)e^{-\int\_{t}^{T}r\_{s}ds}\,H(A\_{T},G^{A}\_{T})\ \big|\ \mathcal{H}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =px+tT−t​𝔼ℚ​[e−∫tTrs​𝑑s​H​(AT,GTA)|ℋt].\displaystyle={}\_{T-t}p\_{x+t}\,\mathbb{E}^{\mathbb{Q}}\bigg[\,e^{-\int\_{t}^{T}r\_{s}ds}\,H(A\_{T},G^{A}\_{T})\ \big|\ \mathcal{H}\_{t}\,\bigg]\,. |  |

Under Assumption [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), 𝔼ℚ​[X|ℋt]=𝔼ℚ​[X|ℱt]\mathbb{E}^{\mathbb{Q}}[X\,|\,\mathcal{H}\_{t}]=\mathbb{E}^{\mathbb{Q}}[X\,|\,\mathcal{F}\_{t}] for any ℱT\mathcal{F}\_{T}-measurable integrable XX. Then,

|  |  |  |
| --- | --- | --- |
|  | Vtμ=px+tT−t​Ct​(T,GTA).V^{\mu}\_{t}={}\_{T-t}p\_{x+t}\,C\_{t}(T,G^{A}\_{T})\,. |  |

As the survival probability px+tT−t{}\_{T-t}p\_{x+t} is known and given by ([4.5](#S4.E5 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), the objective functional VtμV^{\mu}\_{t} does not depend on the underlying mortality control μ∈𝒲\mu\in\mathcal{W}. Therefore, any admissible μ\mu is a maximizer and minimizer of VtμV^{\mu}\_{t} and we find V¯t=V¯t=Vtμ\bar{V}\_{t}=\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t}=V^{\mu}\_{t}.
∎

### A.2. Proof of Proposition [4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")

###### Proof.

(i) Upper bound.
Fix the interval (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1] for some j=0,…,⌊T⌋−⌈t⌉−1j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1. The life-table constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) forces the total survival factor over (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1] to be p^j\hat{p}\_{j}.
Since H~≥0\widetilde{H}\geq 0, the integrand

|  |  |  |
| --- | --- | --- |
|  | s↦e−∫tsru​𝑑u​H~​(As,GsI)s\mapsto e^{-\int\_{t}^{s}r\_{u}\,du}\,\widetilde{H}(A\_{s},G\_{s}^{I}) |  |

is nonnegative. Let 𝒯(a,b]\mathcal{T}\_{(a,b]} denote the set of ℍ\mathbb{H}-stopping times on (a,b](a,b]. Therefore, for any τ1,τ2∈𝒯(⌈t⌉+j,⌈t⌉+j+1]\tau\_{1},\tau\_{2}\in\mathcal{T}\_{(\lceil t\rceil+j,\lceil t\rceil+j+1]} with τ1≤τ2\tau\_{1}\leq\tau\_{2} a.s.,

|  |  |  |
| --- | --- | --- |
|  | ∫aτ1e−∫tsru​𝑑u​H~​(As,GsI)​𝑑s≤∫aτ2e−∫tsru​𝑑u​H~​(As,GsI)​𝑑s,a.s.\int\_{a}^{\tau\_{1}}e^{-\int\_{t}^{s}r\_{u}\,du}\,\widetilde{H}(A\_{s},G\_{s}^{I})\,ds\leq\int\_{a}^{\tau\_{2}}e^{-\int\_{t}^{s}r\_{u}\,du}\,\widetilde{H}(A\_{s},G\_{s}^{I})\,ds\,,\quad\text{a.s.} |  |

Taking conditional expectations given ℋt\mathcal{H}\_{t} leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[∫⌈t⌉+jτ1e−∫tsru​𝑑u​H~​(As,GsI)​𝑑s|ℋt]≤𝔼ℚ​[∫⌈t⌉+jτ2e−∫tsru​𝑑u​H~​(As,GsI)​𝑑s|ℋt].\mathbb{E}^{\mathbb{Q}}\left[\int\_{\lceil t\rceil+j}^{\tau\_{1}}e^{-\int\_{t}^{s}r\_{u}du}\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \big|\ \mathcal{H}\_{t}\right]\leq\mathbb{E}^{\mathbb{Q}}\left[\int\_{\lceil t\rceil+j}^{\tau\_{2}}e^{-\int\_{t}^{s}r\_{u}du}\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \big|\ \mathcal{H}\_{t}\right]. |  | (A.1) |

Hence the conditional expected accumulated discounted payoff ([A.1](#A1.E1 "In Proof. ‣ A.2. Proof of Proposition 4.22 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) over (⌈t⌉+j,τ](\lceil t\rceil+j,\tau] is maximized by taking τ=⌈t⌉+j+1\tau=\lceil t\rceil+j+1.
Consequently, we have from ([4.16](#S4.E16 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) that VtμV\_{t}^{\mu} is maximized when all the mortality mass available on the interval (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1] is assigned at time ⌈t⌉+j+1\lceil t\rceil+j+1. This is achieved by setting μ¯x,c∗≡0\bar{\mu}\_{x,c}^{\*}\equiv 0 (since continuous process with values in a compact set) and choosing a single discrete intervention on each (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1] at τ¯j∗=⌈t⌉+j+1\bar{\tau}\_{j}^{\*}=\lceil t\rceil+j+1. The life-table constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) then directly leads to the optimal jump size μ¯x,j∗=1−p^j\bar{\mu}\_{x,j}^{\*}=1-\hat{p}\_{j}.
  
We can hence rewrite the optimal survival probability

|  |  |  |
| --- | --- | --- |
|  | p¯x+t∗s−t=∏j:τ¯j∗≤sp^j=∏j:⌈t⌉+j+1≤sp^j,\displaystyle{}\_{s-t}\bar{p}^{\*}\_{x+t}=\prod\_{j\,:\,\bar{\tau}^{\*}\_{j}\leq s}\hat{p}\_{j}=\prod\_{j\,:\,\lceil t\rceil+j+1\leq s}\hat{p}\_{j}\,, |  |

with ∏∅:=1\prod\_{\emptyset}:=1. As μ¯∗\bar{\mu}^{\*} (and hence p¯x+t∗s−t{}\_{s-t}\bar{p}^{\*}\_{x+t}) is fixed and deterministic, we find for V¯t\bar{V}\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t\displaystyle\bar{V}\_{t} | =𝔼ℚ​[∫tTe−∫tsru​𝑑u​p¯x+t∗s−t​H~​(As,GsI)​𝑑s|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}du}{}\_{s-t}\bar{p}^{\*}\_{x+t}\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \big|\ \mathcal{H}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tTp¯x+t∗s−t​𝔼ℚ​[e−∫tsru​𝑑u​H~​(As,GsI)|ℋt]​𝑑s\displaystyle=\int\_{t}^{T}{}\_{s-t}\bar{p}^{\*}\_{x+t}\,\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{s}r\_{u}du}\,\widetilde{H}(A\_{s},G^{I}\_{s})\ \big|\ \mathcal{H}\_{t}\right]ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫tTp¯x+t∗s−t​Ct​(s,GsI)​𝑑s,\displaystyle=\int\_{t}^{T}{}\_{s-t}\bar{p}^{\*}\_{x+t}\,C\_{t}(s,G^{I}\_{s})\,ds\,, |  | (A.2) |

where Ct​(s,GsI)C\_{t}(s,G^{I}\_{s}) is given by ([4.15](#S4.E15 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) using again Assumption [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").

(ii) Lower bound.
To minimize VtμV\_{t}^{\mu} under ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) on each (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1], the same monotonicity argument shows that the conditional expected accumulated discounted payoff over (⌈t⌉+j,τ](\lceil t\rceil+j,\tau] is minimized by taking τ\tau as small as possible. Since μx,c\mu\_{x,c} is continuous and takes value in a compact set, the infimum corresponds to μ¯x,c∗≡0\underline{\mu\mkern-4.0mu}\mkern 4.0mu^{\*}\_{x,c}\equiv 0 and τ=⌈t⌉+j\tau=\lceil t\rceil+j. However, ⌈t⌉+j∉(⌈t⌉+j,⌈t⌉+j+1]\lceil t\rceil+j\notin(\lceil t\rceil+j,\lceil t\rceil+j+1], hence no minimizer exists in the admissible set 𝒯(⌈t⌉+j,⌈t⌉+j+1]\mathcal{T}\_{(\lceil t\rceil+j,\lceil t\rceil+j+1]}.
Instead, for each j=0,…,⌊T⌋−⌈t⌉−1j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1, let τj(n)∈𝒯(⌈t⌉+j,⌈t⌉+j+1]\tau\_{j}^{(n)}\in\mathcal{T}\_{(\lceil t\rceil+j,\lceil t\rceil+j+1]} be a sequence such that τj(n)↓⌈t⌉+j\tau\_{j}^{(n)}\downarrow\lceil t\rceil+j a.s. Define admissible controls μ(n)∈𝒲\mu^{(n)}\in\mathcal{W} by setting μx,c(n)≡0\mu\_{x,c}^{(n)}\equiv 0 and placing the discrete jump on (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1] at time τj(n)\tau\_{j}^{(n)} with size μx,j(n)=1−p^j\mu^{(n)}\_{x,j}=1-\hat{p}\_{j} for each jj.
Then the corresponding survival probabilities px+tμ(n)s−t{}\_{s-t}p^{\mu^{(n)}}\_{x+t} decrease pointwise for n→∞n\to\infty to the deterministic limit

|  |  |  |
| --- | --- | --- |
|  | p¯x+t∗s−t=∏j:⌈t⌉+j<s(1−μx,j)=∏j:⌈t⌉+j<sp^j.{}\_{s-t}\underline{p}^{\*}\_{x+t}=\prod\_{j:\,\lceil t\rceil+j<s}\hskip-7.11317pt(1-\mu\_{x,j})=\prod\_{j:\,\lceil t\rceil+j<s}\hat{p}\_{j}\,. |  |

Then, from equation ([4.16](#S4.E16 "In 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), we write

|  |  |  |
| --- | --- | --- |
|  | Vtμ(n)=𝔼ℚ​[∫tTe−∫tsru​𝑑u​∏j:t<τj(n)≤s(1−μx,j)​H~​(As,GsI)​d​s|ℋt].V^{\mu^{(n)}}\_{t}=\mathbb{E}^{\mathbb{Q}}\left[\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}\,du}\hskip-5.69054pt\prod\_{j\,:\,t<\tau^{(n)}\_{j}\leq s}\hskip-5.69054pt(1-\mu\_{x,j})\,\widetilde{H}(A\_{s},G^{I}\_{s})\,ds\ \big|\ \mathcal{H}\_{t}\right]. |  |

By dominated convergence (using μx,j∈[0,1]\mu\_{x,j}\in[0,1] and 𝔼ℚ​[∫0T|H~​(As,GsI)|​𝑑s]<∞\mathbb{E}^{\mathbb{Q}}[\int\_{0}^{T}|\widetilde{H}(A\_{s},G\_{s}^{I})|ds]<\infty), we have as n→∞n\to\infty,

|  |  |  |
| --- | --- | --- |
|  | Vtμ(n)↓𝔼ℚ[∫tTe−∫tsru​𝑑up¯x+t∗s−tH~(As,GsI)ds|ℋt]=:V¯t.V\_{t}^{\mu^{(n)}}\downarrow\mathbb{E}^{\mathbb{Q}}\!\left[\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}\,du}\,{}\_{s-t}\underline{p}^{\*}\_{x+t}\,\widetilde{H}(A\_{s},G\_{s}^{I})\,ds\,\Big|\,\mathcal{H}\_{t}\right]=:\underline{V}\_{t}. |  |

Finally, since p¯x+t∗s−t{}\_{s-t}\underline{p}^{\*}\_{x+t} is deterministic, we obtain as in (i),

|  |  |  |
| --- | --- | --- |
|  | V¯t=∫tTp¯x+t∗s−t​Ct​(s,GsI)​𝑑s,\underline{V}\_{t}=\int\_{t}^{T}{}\_{s-t}\underline{p}^{\*}\_{x+t}\,C\_{t}(s,G\_{s}^{I})\,ds, |  |

which concludes the proof.

∎

### A.3. Proof of Proposition [4.5](#S4.ThmTheorem5 "Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")

###### Proof.

(i) Upper bound.
Fix the interval (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1] for some j=0,…,⌊T⌋−⌈t⌉−1j=0,\ldots,\lfloor T\rfloor-\lceil t\rceil-1. Let again 𝒯(a,b]\mathcal{T}\_{(a,b]} denote the set of ℍ\mathbb{H}-stopping times on (a,b](a,b]. Therefore, for any τ∈𝒯(⌈t⌉+j,⌈t⌉+j+1]\tau\in\mathcal{T}\_{(\lceil t\rceil+j,\lceil t\rceil+j+1]}, we can rewrite the expected discounted payoff at time of death τ\tau by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[e−∫tτrs​𝑑s​H^​(Aτ,GτD)|ℋt]\displaystyle\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{\tau}r\_{s}ds}\,\widehat{H}(A\_{\tau},G^{D}\_{\tau})\ \big|\ \mathcal{H}\_{t}\right] |  | (A.3) |
|  |  |  |
| --- | --- | --- |
|  | =𝔼ℚ​[e−∫tτrs​𝑑s​(GτD+(Aτ−GτD)+)|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{\tau}r\_{s}ds}\left(G^{D}\_{\tau}+(A\_{\tau}-G^{D}\_{\tau})\_{+}\right)\big|\ \mathcal{H}\_{t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼ℚ​[e−∫tτrs​𝑑s​GτD|ℋt]+𝔼ℚ​[e−∫tτrs​𝑑s​(Aτ−GτD)+|ℋt].\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{\tau}r\_{s}ds}\,G^{D}\_{\tau}\big|\ \mathcal{H}\_{t}\right]+\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{\tau}r\_{s}ds}(A\_{\tau}-G^{D}\_{\tau})\_{+}\big|\ \mathcal{H}\_{t}\right]. |  |

Denoting P~​(t,s):=𝔼ℚ​[e−∫tsru​𝑑u​GsD|ℋt]=P​(t,s)​GsD=A0​P​(t,s)​erg​s\widetilde{P}(t,s):=\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{s}r\_{u}du}G^{D}\_{s}\big|\ \mathcal{H}\_{t}\right]=P(t,s)G^{D}\_{s}=A\_{0}P(t,s)e^{r\_{g}s}, we have under the assumption rg≥f​(t,s)r\_{g}\geq f(t,s) for all s∈[t,T]s\in[t,T], that P~​(t,s)\widetilde{P}(t,s) is increasing in ss. This is indeed direct from

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂sP~​(t,s)=P​(t,s)​A0​erg​s​(−f​(t,s)+rg)≥0,\partial\_{s}\widetilde{P}(t,s)=P(t,s)A\_{0}e^{r\_{g}s}(-f(t,s)+r\_{g})\geq 0\,, |  | (A.4) |

since ∂sP​(t,s)=−f​(t,s)​P​(t,s)\partial\_{s}P(t,s)=-f(t,s)P(t,s). Moreover, under assumption ([4.25](#S4.E25 "In Proposition 4.5 (GMDB bounds). ‣ 4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), it is shown in Battauz and Rotondi ([2022](#bib.bib4 "American options and stochastic interest rates")) that early exercise in an American call is never optimal and hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg​maxτ∈𝒯(⌈t⌉+j,⌈t⌉+j+1]⁡𝔼ℚ​[e−∫tτrs​𝑑s​(Aτ−GτD)+|ℋt]=⌈t⌉+j+1.\operatorname\*{arg\,max}\_{\tau\in\mathcal{T}\_{(\lceil t\rceil+j,\lceil t\rceil+j+1]}}\mathbb{E}^{\mathbb{Q}}\left[e^{-\int\_{t}^{\tau}r\_{s}ds}(A\_{\tau}-G^{D}\_{\tau})\_{+}\big|\ \mathcal{H}\_{t}\right]=\lceil t\rceil+j+1\,. |  | (A.5) |

From the two statements above, we have shown that s↦Ct​(s,GsD):=𝔼ℚ​[e−∫tsru​𝑑u​H^​(As,GsD)∣ℋt]s\mapsto C\_{t}(s,G^{D}\_{s}):=\mathbb{E}^{\mathbb{Q}}[e^{-\int\_{t}^{s}r\_{u}du}\,\widehat{H}(A\_{s},G^{D}\_{s})\mid\mathcal{H}\_{t}] is nondecreasing on each year interval (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1].
Therefore, using the same monotonicity argument ([A.1](#A1.E1 "In Proof. ‣ A.2. Proof of Proposition 4.22 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) as in Proposition [4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), we conclude that τ¯j∗=⌈t⌉+j+1\bar{\tau}^{\*}\_{j}=\lceil t\rceil+j+1 and μ¯x,c∗​(t)≡0\bar{\mu}^{\*}\_{x,c}(t)\equiv 0. The life-table constraint ([4.6](#S4.E6 "In 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) gives us directly the associated intervention size μ¯x,j∗=1−p^j\bar{\mu}^{\*}\_{x,j}=1-\hat{p}\_{j}. Since μ¯∗\bar{\mu}^{\*} is deterministic and from Assumption [4.2](#S4.ThmTheorem2 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"), we obtain the following upper bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯t\displaystyle\bar{V}\_{t} | =𝔼ℚ​[∑j=0⌊T⌋−⌈t⌉−1e−∫tτj∗ru​𝑑u​(∏i<j(1−μx,i∗))​μx,j∗​H^​(Aτj∗,Gτj∗D)|ℋt]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\sum\_{j=0}^{\lfloor T\rfloor-\lceil t\rceil-1}e^{-\int\_{t}^{\tau^{\*}\_{j}}r\_{u}\,du}\left(\prod\_{i<j}(1-\mu^{\*}\_{x,i})\right)\mu^{\*}\_{x,j}\,\widehat{H}(A\_{\tau^{\*}\_{j}},G^{D}\_{\tau^{\*}\_{j}})\,\Big|\,\mathcal{H}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=0⌊T⌋−⌈t⌉−1Ct​(⌈t⌉+j+1,G⌈t⌉+j+1D)​μx,j∗​∏i<j(1−μx,i∗)\displaystyle=\sum\_{j=0}^{\lfloor T\rfloor-\lceil t\rceil-1}C\_{t}(\lceil t\rceil+j+1,G^{D}\_{\lceil t\rceil+j+1})\,\mu^{\*}\_{x,j}\,\prod\_{i<j}\,(1-\mu^{\*}\_{x,i})\, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=0⌊T⌋−⌈t⌉−1Ct​(⌈t⌉+j+1j,G⌈t⌉+j+1D)​(1−p^j)​∏i<jp^i.\displaystyle=\sum\_{j=0}^{\lfloor T\rfloor-\lceil t\rceil-1}C\_{t}(\lceil t\rceil+j+1\_{j},G^{D}\_{\lceil t\rceil+j+1})\,(1-\hat{p}\_{j})\,\prod\_{i<j}\,\hat{p}\_{i}\,.\vskip 5.69054pt |  |

(ii) Lower bound.   The lower bound V¯t\underline{V\mkern-4.0mu}\mkern 4.0mu\_{t} follows directly from Proposition [4.22](#S4.E22 "In Proposition 4.4 (GMIB bounds). ‣ 4.2. Guaranteed Minimum Income Benefit ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") (ii) and from the fact that s↦Ct​(s,GsD):=𝔼ℚ​[e−∫tsru​𝑑u​H^​(As,GsD)∣ℋt]s\mapsto C\_{t}(s,G^{D}\_{s}):=\mathbb{E}^{\mathbb{Q}}[e^{-\int\_{t}^{s}r\_{u}du}\,\widehat{H}(A\_{s},G^{D}\_{s})\mid\mathcal{H}\_{t}] is nondecreasing on each year interval (⌈t⌉+j,⌈t⌉+j+1](\lceil t\rceil+j,\lceil t\rceil+j+1] as shown above in [A.3](#A1.SS3 "A.3. Proof of Proposition 4.5 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints") (i).
∎

### A.4. Proof of Proposition [5.2](#S5.ThmTheorem2 "Proposition 5.2. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")

###### Proof.

(Step 1). First, we prove the equivalence between the original problem and the dual problem. For μ∈𝒜b​o​u​n​d​e​dδ\mu\in\mathcal{A}\_{bounded}^{\delta}, we have that, for any 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑j=1nλj​[𝔼ℙ​(e−∫0jμx​(s)​𝑑s)−p^xj].\displaystyle-\sum\_{j=1}^{n}\lambda\_{j}\left[\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right)-{}\_{j}\hat{p}\_{x}\right]. |  |

Hence, we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | supμx∈𝒜b​o​u​n​d​e​dδ𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\sup\_{\mu\_{x}\in\mathcal{A}^{\delta}\_{bounded}}\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\int\_{0}^{T}e^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)ds\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | inf𝝀∈ℝnsupμ∈𝒜~b​o​u​n​d​e​dδ𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\inf\_{\boldsymbol{\lambda}\in\mathbb{R}^{n}}\hskip-1.42262pt\sup\_{\mu\in\tilde{\mathcal{A}}^{\delta}\_{bounded}}\hskip-5.12149pt\mathbb{E}^{\mathbb{Q}}\Bigg[e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})+\hskip-1.42262pt\int\_{0}^{T}\hskip-3.55658pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-1.13809pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-1.13809ptds\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑j=1nλj​[𝔼ℙ​(e−∫0jμx​(s)​𝑑s)−p^xj].\displaystyle\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ -\sum\_{j=1}^{n}\lambda\_{j}\left[\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right)-{}\_{j}\hat{p}\_{x}\right]. |  |

For 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, let us define the inner functional V​(𝝀)V(\boldsymbol{\lambda}) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(𝝀):=supμx∈𝒜~b​o​u​n​d​e​dδ\displaystyle\hskip-2.84526ptV(\boldsymbol{\lambda})\hskip-1.42262pt=\hskip-5.406pt\sup\_{\mu\_{x}\in\tilde{\mathcal{A}}^{\delta}\_{bounded}} | 𝔼ℚ​[e−∫0T(ru+μx​(u))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\mathbb{E}^{\mathbb{Q}}\Bigg[e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u))du}H(A\_{T},G\_{T}^{A})\hskip-1.42262pt+\hskip-1.42262pt\int\_{0}^{T}\hskip-4.2679pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-1.42262pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-1.42262ptds\Bigg] |  | (A.6) |
|  |  | −∑j=1nλj​𝔼ℙ​(e−∫0jμx​(s)​𝑑s)\displaystyle-\sum\_{j=1}^{n}\lambda\_{j}\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}(s)ds}\right) |  |

As the set of admissible controls 𝒜~b​o​u​n​d​e​dδ\tilde{\mathcal{A}}^{\delta}\_{bounded} is convex and closed, we deduce that there exists an optimal control μ∗(.;𝝀)∈𝒜~b​o​u​n​d​e​dδ\mu^{\*}(.;\boldsymbol{\lambda})\in\tilde{\mathcal{A}}^{\delta}\_{bounded} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝝀):=\displaystyle V(\boldsymbol{\lambda}):= | 𝔼ℚ​[e−∫0T(ru+μx∗​(u;𝝀))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx∗​(u;𝝀))​𝑑u​(H~​(As,GsI)+μx∗​(s;𝝀)​H^​(As,GsD))​𝑑s]\displaystyle\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}^{\*}(u;\boldsymbol{\lambda}))du}H(A\_{T},G\_{T}^{A})+\hskip-1.42262pt\int\_{0}^{T}\hskip-4.2679pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}^{\*}(u;\boldsymbol{\lambda}))du}\hskip-0.99585pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}^{\*}(s;\boldsymbol{\lambda})\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-0.7113ptds\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑j=1nλj​𝔼ℙ​(e−∫0jμx∗​(s;𝝀)​𝑑s).\displaystyle-\sum\_{j=1}^{n}\lambda\_{j}\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}^{\*}(s;\boldsymbol{\lambda})ds}\right). |  |

Moreover, the functional 𝝀↦(V​(𝝀)+∑j=1nλj​p^xj)\boldsymbol{\lambda}\mapsto\left(V(\boldsymbol{\lambda})+\sum\_{j=1}^{n}\lambda\_{j}{}\_{j}\hat{p}\_{x}\right) is convex, there exists 𝝀∗∈ℝn\boldsymbol{\lambda}^{\*}\in\mathbb{R}^{n} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝝀>0V​(𝝀)+∑j=1nλj​p^xj\displaystyle\inf\_{\boldsymbol{\lambda}>0}V(\boldsymbol{\lambda})+\sum\_{j=1}^{n}\lambda\_{j}{}\_{j}\hat{p}\_{x} | =min𝝀>0⁡V​(𝝀)+∑j=1nλj​p^xj=V​(𝝀∗)+∑j=1nλj∗​p^xj,\displaystyle=\min\_{\boldsymbol{\lambda}>0}V(\boldsymbol{\lambda})+\sum\_{j=1}^{n}\lambda\_{j}{}\_{j}\hat{p}\_{x}=V(\boldsymbol{\lambda}^{\*})+\sum\_{j=1}^{n}\lambda\_{j}^{\*}{}\_{j}\hat{p}\_{x}, |  |

and using the first order condition (FOC), we also have that 𝝀∗\boldsymbol{\lambda}^{\*} is such that999Since for all 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, μ∗​(𝝀)∈𝒜~b​o​u​n​d​e​dδ\mu^{\*}(\boldsymbol{\lambda})\in\tilde{\mathcal{A}}^{\delta}\_{bounded}, we know that, for all t≤Tt\leq T, (μx,a​(t)−δ)+≤μx∗​(t;𝝀)≤μx,a​(t)+δ(\mu\_{x,a}(t)-\delta)\_{+}\leq\mu\_{x}^{\*}(t;\boldsymbol{\lambda})\leq\mu\_{x,a}(t)+\delta, then, for j=1,…,nj=1,...,n, inf𝝀∈ℝn𝔼ℙ​(e−∫0jμx∗​(t;𝝀)​𝑑t)≤p^xj≤sup𝝀∈ℝn𝔼ℙ​(e−∫0jμx∗​(t;𝝀)​𝑑t)\inf\_{\boldsymbol{\lambda}\in\mathbb{R}^{n}}\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}^{\*}(t;\boldsymbol{\lambda})dt}\right)\leq{}\_{j}\hat{p}\_{x}\leq\sup\_{\boldsymbol{\lambda}\in\mathbb{R}^{n}}\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}^{\*}(t;\boldsymbol{\lambda})dt}\right) and by continuity of the functional, we deduce the the existence of 𝝀∗∈ℝn\boldsymbol{\lambda}^{\*}\in\mathbb{R}^{n} that satisfies the FOC.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​(e−∫0jμx∗​(s;𝝀∗)​𝑑s)=p^xj,j=1,…,n.\mathbb{E}^{\mathbb{P}}\left(e^{-\int\_{0}^{j}\mu\_{x}^{\*}(s;\boldsymbol{\lambda}^{\*})ds}\right)={}\_{j}\hat{p}\_{x},\quad j=1,...,n. |  | (A.7) |

Since μx∗(.;𝝀∗)\mu\_{x}^{\*}(.;\boldsymbol{\lambda}^{\*}) satisfies ([A.7](#A1.E7 "In Proof. ‣ A.4. Proof of Proposition 5.2 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), we have that μx∗(.;𝝀∗)∈𝒜b​o​u​n​d​e​dδ\mu\_{x}^{\*}(.;\boldsymbol{\lambda}^{\*})\in\mathcal{A}\_{bounded}^{\delta} and thus the solution of the original problem is such that

|  |  |  |
| --- | --- | --- |
|  | supμx∈𝒜b​o​u​n​d​e​dδ𝔼ℚ​[e−∫0T(ru+μx(u)du​H​(AT,GTA)+∫0Te−∫0s(ru+μx​(u))​𝑑u​(H~​(As,GsI)+μx​(s)​H^​(As,GsD))​𝑑s]\displaystyle\hskip-5.69054pt\sup\_{\mu\_{x}\in\mathcal{A}^{\delta}\_{bounded}}\hskip-4.2679pt\mathbb{E}^{\mathbb{Q}}\Bigg[\,e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}(u)du}H(A\_{T},G\_{T}^{A})\hskip-0.7113pt+\hskip-1.42262pt\int\_{0}^{T}\hskip-4.2679pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}(u))du}\hskip-0.99585pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}(s)\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-0.99585ptds\Bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =min𝝀>0⁡V​(𝝀)+∑j=1nλj​p^xj\displaystyle\hskip 4.2679pt=\min\_{\boldsymbol{\lambda}>0}V(\boldsymbol{\lambda})+\sum\_{j=1}^{n}\lambda\_{j}{}\_{j}\hat{p}\_{x} |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼ℚ​[e−∫0T(ru+μx∗​(u;𝝀∗))​𝑑u​H​(AT,GTA)+∫0Te−∫0s(ru+μx∗​(u;𝝀∗))​𝑑u​(H~​(As,GsI)+μx∗​(s;𝝀∗)​H^​(As,GsD))​𝑑s]\displaystyle\hskip 4.2679pt=\mathbb{E}^{\mathbb{Q}}\Bigg[e^{-\int\_{0}^{T}(r\_{u}+\mu\_{x}^{\*}(u;\boldsymbol{\lambda}^{\*}))du}H(A\_{T},G\_{T}^{A})\hskip-0.99585pt+\hskip-1.42262pt\int\_{0}^{T}\hskip-4.2679pte^{-\int\_{0}^{s}(r\_{u}+\mu\_{x}^{\*}(u;\boldsymbol{\lambda}^{\*}))du}\hskip-0.99585pt\left(\widetilde{H}(A\_{s},G\_{s}^{I})+\mu\_{x}^{\*}(s;\boldsymbol{\lambda}^{\*})\widehat{H}(A\_{s},G\_{s}^{D})\right)\hskip-0.99585ptds\Bigg] |  |

(Step 2). To conclude to proof, it remains to prove that, for any 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, v¯​(0,A0,r0,Z0;𝝀)\bar{v}(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}) is equal to V​(𝝀)V(\boldsymbol{\lambda}) defined by ([A.6](#A1.E6 "In Proof. ‣ A.4. Proof of Proposition 5.2 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")). Since we assume that there exists v¯​(t,a,r,z;𝝀)∈C1,2,2,2\bar{v}(t,a,r,z;\boldsymbol{\lambda})\in C^{1,2,2,2} solution to ([5.18](#S5.E18 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) that satisfies boundary conditions given by ([5.16](#S5.E16 "In 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")), then using classical results from dynamic programming (see for instance Touzi ([2012](#bib.bib13 "Optimal stochastic control, stochastic target problems, and backward sde"))) or by adapting the arguments used in the proof of (Li and Szimayer, [2011](#bib.bib10 "The uncertain mortality intensity framework: pricing and hedging unit-linked life insurance contracts"), Theorem 1) in the context of an uncertainty mortality control problem, it follows that v¯​(t,a,r,z;𝝀)\bar{v}(t,a,r,z;\boldsymbol{\lambda}) solving the HJB equation solves the stochastic control problem ([5](#S5.Ex4 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝝀)=\displaystyle V(\boldsymbol{\lambda})= | v¯​(0,A0,r0,Z0;𝝀),\displaystyle\bar{v}(0,A\_{0},r\_{0},Z\_{0};\boldsymbol{\lambda}), |  |

and the proof is complete.
∎

### A.5. Proof of Proposition [5.4](#S5.ThmTheorem4 "Proposition 5.4. ‣ 5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints")

###### Proof.

To prove the statement, we must show that

|  |  |  |
| --- | --- | --- |
|  | 𝒜~=⋃δ>0𝒜b​o​u​n​d​e​dδ.\tilde{\mathcal{A}}=\bigcup\_{\delta>0}\mathcal{A}^{\delta}\_{bounded}. |  |

Obviously, we have that

|  |  |  |
| --- | --- | --- |
|  | ⋃δ>0𝒜b​o​u​n​d​e​dδ⊆𝒜~.\bigcup\_{\delta>0}\mathcal{A}^{\delta}\_{bounded}\subseteq\tilde{\mathcal{A}}. |  |

Let us prove that

|  |  |  |
| --- | --- | --- |
|  | 𝒜~⊆⋃δ>0𝒜b​o​u​n​d​e​dδ.\tilde{\mathcal{A}}\subseteq\bigcup\_{\delta>0}\mathcal{A}^{\delta}\_{bounded}. |  |

Formally, we have to prove that for all μx∈𝒜~\mu\_{x}\in\tilde{\mathcal{A}}, there exists δ>0\delta>0 such that μx∈𝒜b​o​u​n​d​e​dδ\mu\_{x}\in\mathcal{A}^{\delta}\_{bounded}. For a given μx∈𝒜~\mu\_{x}\in\tilde{\mathcal{A}}, define

|  |  |  |
| --- | --- | --- |
|  | Y​(ω):=supt∈[0,T]|μx​(t;ω)−μx,a​(t)|.Y(\omega):=\sup\_{t\in[0,T]}\big|\mu\_{x}(t;\omega)-\mu\_{x,a}(t)\big|. |  |

Since we assume that μx∈𝒜~\mu\_{x}\in\tilde{\mathcal{A}}, then

|  |  |  |
| --- | --- | --- |
|  | Y​(ω)<+∞.Y(\omega)<+\infty. |  |

Consequently, for μx∈𝒜~\mu\_{x}\in\tilde{\mathcal{A}}, we can choose

|  |  |  |
| --- | --- | --- |
|  | δ:=ess​supω⁡Y​(ω)<∞,\delta:=\operatorname{ess\,sup}\_{\omega}Y(\omega)<\infty, |  |

which implies μx∈𝒜boundedδ\mu\_{x}\in\mathcal{A}^{\delta}\_{\mathrm{bounded}}. Since μx\mu\_{x} was arbitrary, we conclude that

|  |  |  |
| --- | --- | --- |
|  | ⋃δ>0𝒜boundedδ=𝒜~.\bigcup\_{\delta>0}\mathcal{A}^{\delta}\_{\mathrm{bounded}}=\tilde{\mathcal{A}}. |  |

∎

Disclosure statement The authors declare that they have no conflict of interest.
  
Funding details This work was supported by the Swiss National Science Foundation (SNSF) under Grant no. 10003723. Edouard Motte is a FRIA grantee of the Fonds de la Recherche Scientifique - FNRS, Belgium.
  
Author contributions Jean-Loup Dupret: Conceptualization, Formal analysis, Investigation, Methodology, Writing.
Edouard Motte: Formal analysis, Investigation, Validation, Visualization, Writing.

## References

* M. Avellaneda and A. Paras (1996)
  Managing the volatility risk of portfolios of derivative securities: the Lagrangian uncertain volatility model.
  Applied Mathematical Finance 3 (1),  pp. 21–52.
  Cited by: [§1](#S1.p1.15 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"),
  [§5](#S5.p2.1 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* U. Basellini, C. G. Camarda, and H. Booth (2023)
  Thirty years on: a review of the Lee–Carter method for forecasting mortality.
  International Journal of Forecasting 39 (3),  pp. 1033–1049.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* A. Battauz and F. Rotondi (2022)
  American options and stochastic interest rates.
  Computational Management Science 19 (4),  pp. 567–604.
  Cited by: [§A.3](#A1.SS3.1.p1.13 "Proof. ‣ A.3. Proof of Proposition 4.5 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* H. Booth, J. Maindonald, and L. Smith (2002)
  Applying Lee-Carter under conditions of variable mortality decline.
  Population Studies 56 (3),  pp. 325–336.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* N. L. Bowers, H. U. Gerber, J. C. Hickman, D. A. Jones, and C. J. Nesbitt (1997)
  Actuarial mathematics.
  2nd edition, Society of Actuaries, Schaumburg, IL.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* A. J.G. Cairns, D. Blake, and K. Dowd (2006)
  A two-factor model for stochastic mortality with parameter uncertainty: theory and calibration.
  Journal of Risk and Insurance 73 (4),  pp. 687–718.
  External Links: [Document](https://dx.doi.org/10.1111/j.1539-6975.2006.00195.x)
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* A. J. Cairns, D. Blake, K. Dowd, G. D. Coughlan, D. Epstein, A. Ong, and I. Balevich (2009)
  A quantitative comparison of stochastic mortality models using data from England and Wales and the United States.
  North American Actuarial Journal 13 (1),  pp. 1–35.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* C. Ceci, K. Colaneri, and A. Cretarola (2017)
  Unit-linked life insurance policies: optimal hedging in partially observable market models.
  Insurance: Mathematics and Economics 76,  pp. 149–163.
  Cited by: [§4](#S4.p3.10 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* P. Cheridito, J. Dupret, and D. Hainaut (2025)
  Deep learning for continuous-time stochastic control with jumps.
  arXiv preprint arXiv:2505.15602.
  Cited by: [§6.2](#S6.SS2.p6.2 "6.2. Relaxed bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* D. R. Cox and V. Isham (1980)
  Point processes.
  1st edition, Routledge, New York.
  External Links: [Document](https://dx.doi.org/10.1201/9780203743034),
  ISBN 9780203743034,
  [Link](https://doi.org/10.1201/9780203743034)
  Cited by: [§4](#S4.p2.1 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* J. C. Cox, S. A. Ross, and M. Rubinstein (1979)
  Option pricing: a simplified approach.
  Journal of financial Economics 7 (3),  pp. 229–263.
  Cited by: [§4.3](#S4.SS3.p2.17 "4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* I. D. Currie (2006)
  Smoothing and forecasting mortality rates with P-splines.
  Talk given at the Institute of Actuaries 10.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* D. C. Dickson, M. R. Hardy, and H. R. Waters (2020)
  Actuarial mathematics for life contingent risks.
   Cambridge University Press.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"),
  [§2](#S2.p2.18 "2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* J. Dupret and D. Hainaut (2026)
  Deep learning for high-dimensional continuous-time stochastic optimal control without explicit solution.
  Operations Research Ahead of print.
  Cited by: [§6.2](#S6.SS2.p6.2 "6.2. Relaxed bounds ‣ 6 Numerical experiments ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* B. Gompertz (1825)
  On the nature of the function expressive of the law of human mortality, and on a new mode of determining the value of life contingencies.
  Philosophical Transactions of the Royal Society of London 115,  pp. 513–583.
  External Links: [Document](https://dx.doi.org/10.1098/rstl.1825.0026)
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* D. Hainaut (2024)
  Valuation of guaranteed minimum accumulation benefits (GMABs) with physics-inspired neural networks.
  Annals of Actuarial Science 18 (2),  pp. 442–473.
  Cited by: [§3](#S3.p1.16 "3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"),
  [§3](#S3.p2.13 "3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"),
  [§3](#S3.p3.1 "3 The financial market ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* L. Heligman and J. H. Pollard (1980)
  The age pattern of mortality.
  Journal of the Institute of Actuaries 107 (1),  pp. 49–80.
  External Links: [Document](https://dx.doi.org/10.1017/S0020268100040257)
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* J. D. Kalbfleisch and R. L. Prentice (2002)
  The statistical analysis of failure time data.
   John Wiley & Sons.
  Cited by: [§2](#S2.p1.43 "2 Mortality modeling ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* R. D. Lee and L. R. Carter (1992)
  Modeling and forecasting U.S. mortality.
  Journal of the American Statistical Association 87 (419),  pp. 659–671.
  External Links: [Document](https://dx.doi.org/10.2307/2290201)
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* J. Li and A. Szimayer (2011)
  The uncertain mortality intensity framework: pricing and hedging unit-linked life insurance contracts.
  Insurance: Mathematics and Economics 49 (3),  pp. 471–486.
  Cited by: [§A.4](#A1.SS4.1.p1.16 "Proof. ‣ A.4. Proof of Proposition 5.2 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"),
  [§1](#S1.p1.15 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"),
  [§5](#S5.p2.1 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* N. Li and R. D. Lee (2005)
  Coherent mortality forecasts for a group of populations: an extension of the Lee–Carter model.
  Demography 42 (3),  pp. 575–594.
  External Links: [Document](https://dx.doi.org/10.1353/dem.2005.0021)
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* F. A. Longstaff and E. S. Schwartz (2001)
  Valuing American options by simulation: A simple least-squares approach.
  The review of financial studies 14 (1),  pp. 113–147.
  Cited by: [§4.3](#S4.SS3.p2.17 "4.3. Guaranteed Minimum Death Benefits ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* W. Makeham (1860)
  On the law of mortality and the construction of annuity tables.
  Journal of the Institute of Actuaries 8 (6),  pp. 301–310.
  External Links: [Document](https://dx.doi.org/10.1017/S204616580000126X)
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* T. Møller (1998)
  Risk-minimizing hedging strategies for unit-linked life insurance contracts.
  ASTIN Bulletin: The Journal of the IAA 28 (1),  pp. 17–47.
  Cited by: [§4](#S4.p3.10 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* T. Møller (2001)
  Risk-minimizing hedging strategies for insurance payment processes.
  Finance and Stochastics 5 (4),  pp. 419–446.
  Cited by: [§4](#S4.p3.10 "4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* E. Motte and D. Hainaut (2025)
  Efficient hedging of life insurance portfolio for loss-averse insurers.
  Insurance: Mathematics and Economics,  pp. 103116.
  Cited by: [§5](#S5.p2.1 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* R. Plat (2009)
  On stochastic mortality modeling.
  Insurance: Mathematics and Economics 45 (3),  pp. 393–404.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* A. E. Renshaw and S. Haberman (2003)
  Lee–Carter mortality forecasting with age-specific enhancement.
  Insurance: Mathematics and Economics 33 (2),  pp. 255–272.
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* A. E. Renshaw and S. Haberman (2006)
  A cohort-based extension to the Lee–Carter model for mortality reduction factors.
  Insurance: Mathematics and Economics 38 (3),  pp. 556–570.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2005.12.001)
  Cited by: [§1](#S1.p1.8 "1 Introduction ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* M. Schweizer (1991)
  Option hedging for semimartingales.
  Stochastic processes and their Applications 37 (2),  pp. 339–363.
  Cited by: [Assumption 4.2](#S4.ThmTheorem2.p1.1.1 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* M. Schweizer (1995)
  On the minimal martingale measure and the Möllmer-Schweizer decomposition.
  Stochastic analysis and applications 13 (5),  pp. 573–599.
  Cited by: [Assumption 4.2](#S4.ThmTheorem2.p1.1.1 "Assumption 4.2. ‣ 4 Bounds on variable annuities: almost sure matching of the life tables ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").
* N. Touzi (2012)
  Optimal stochastic control, stochastic target problems, and backward sde.
  Vol. 29, Springer Science & Business Media.
  Cited by: [§A.4](#A1.SS4.1.p1.16 "Proof. ‣ A.4. Proof of Proposition 5.2 ‣ Appendix A Proofs ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints"),
  [§5](#S5.p7.8 "5 Bounds on variable annuities: matching life tables in expectation ‣ General Bounds on Functionals of the Lifetime under Life Table Constraints").

BETA