---
authors:
- Chang Chen
- Duy-Minh Dang
doc_id: arxiv:2603.06563v1
family_id: arxiv:2603.06563
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Convergence of Neural Network Policies for Risk–Reward Optimization
url_abs: http://arxiv.org/abs/2603.06563v1
url_html: https://arxiv.org/html/2603.06563v1
venue: arXiv q-fin
version: 1
year: 2026
---


Chang Chen
School of Mathematics and Physics, The University of Queensland, St Lucia, Brisbane 4072, Australia ([chang.chen1@student.uq.edu.au](2603.06563v1/mailto:chang.chen1@student.uq.edu.au)).
  
Duy-Minh Dang
School of Mathematics and Physics, The University of Queensland, St Lucia, Brisbane 4072, Australia ([duyminh.dang@uq.edu.au](2603.06563v1/mailto:duyminh.dang@uq.edu.au)).

###### Abstract

We develop a neural-network framework for multi-period risk–reward
stochastic control problems with constrained two-step feedback policies that
may be discontinuous in the state.
We allow a broad class of objectives built on a
finite-dimensional performance vector, including terminal and path-dependent
statistics, with risk functionals admitting auxiliary-variable optimization
representations (e.g. Conditional Value-at-Risk and buffered probability of
exceedance) and optional moment dependence.
Our approach parametrizes the two-step policy using two coupled feedforward
networks with constraint-enforcing output layers, reducing the constrained control
problem to unconstrained training over network parameters.
Under mild regularity conditions, we prove that the
empirical optimum of the NN-parametrized objective
converges in probability to the true optimal value as network capacity and
training sample size increase. The proof is modular, separating
policy approximation, propagation through the controlled recursion, and
preservation under the scalarized risk–reward objective.
Numerical experiments confirm the predicted convergence-in-probability behavior, show close agreement between learned and reference control heat maps, and demonstrate out-of-sample robustness on a large independent scenario set.

Keywords.
neural networks, policy approximation, risk–reward optimization, convergence analysis

MSC2020.
93E20, 68T07, 90C15, 62G05

## 1 Introduction

Discrete-intervention stochastic control problems arise whenever decisions are made at a finite set of intervention times and the system evolves stochastically between interventions. In many applications, decisions are subject to pointwise constraints (e.g. feasibility, budgets, or operational limits),
and the objective function encodes a trade-off between a notion of reward and a notion of risk. This includes settings with two-step constrained interventions at each time (e.g. a pre-decision adjustment followed by a post-decision allocation), as well as terminal and discrete-time path-dependent performance criteria. Such problems arise broadly in finance and insurance, economics, and engineering.

Neural networks (NNs) provide a flexible framework for approximating feedback policies in settings where dynamic-programming discretizations become expensive or infeasible. An increasingly studied approach is to parameterize the policy directly and optimize an empirical objective via stochastic gradient methods. This idea underlies a rapidly developing literature on NN-based policy approximation for stochastic control and related problems [[6](#bib.bib6), [18](#bib.bib18), [1](#bib.bib1), [23](#bib.bib23), [27](#bib.bib27), [15](#bib.bib15), [2](#bib.bib2), [12](#bib.bib12)].
Following the terminology in [[14](#bib.bib14)], these approaches can be divided into two categories: global-in-time and local-in-time. In a global-in-time approach,
the control over all decision times is determined by solving a single training problem at the initial time (even if the parametrization uses multiple time-indexed subnetworks), as in, e.g. [[6](#bib.bib6), [18](#bib.bib18), [1](#bib.bib1), [23](#bib.bib23), [27](#bib.bib27)]. In contrast, local-in-time methods follow a backward-induction structure and train time-indexed approximations sequentially, typically using a separate network (or parameter set) at each decision time [[15](#bib.bib15), [2](#bib.bib2)]. In this sense, local-in-time implementations are often described as stacked NN schemes, since they stack one approximator per decision time and fit them step-by-step (see also [[26](#bib.bib26)]). From a broader viewpoint, both paradigms are instances of policy function approximation for stochastic control [[22](#bib.bib22)].

A central question for these approaches concerns the convergence pipeline: how approximation of feedback maps by NNs propagates through the controlled state recursion and, in turn, through a risk–reward objective, and whether the resulting empirical training problem is consistent, i.e. converges to the true optimum as the training sample size and NN capacity increase.
A key technical difficulty is that learned policies are evaluated at moving inputs, since the controlled state is itself generated by the learned policy.
A convenient sufficient route in discrete-time convergence analyses is to assume global continuity of the optimal feedback rule in the state variable and to invoke uniform approximation over the relevant feature domain; see, for example, [[27](#bib.bib27)].

While appropriate when continuity is structurally justified, this strategy does not directly accommodate constrained controls that naturally exhibit discontinuities, a common feature of practical intervention problems. Even in low-dimensional models, binding constraints can induce threshold/bang–bang feedback rules, so sup-norm uniform approximation is not the right notion for discontinuous targets
and continuity at moving inputs can fail on the discontinuity set.

This paper develops a convergence framework for discrete-intervention risk–reward control that remains valid in the presence of such discontinuities, and separates the approximation, propagation, and objective layers of the argument. Our setting accommodates a broad class of scalarized risk–reward objectives, including path-dependent criteria, auxiliary-variable (multi-level) risk representations,
as well as moment dependence. As is standard in global-in-time policy approximation,
our analysis is formulated at the initial time. For objectives that are separable in the dynamic-programming sense, this yields the time-consistent optimal strategy; for nonseparable risk–reward criteria, it yields the corresponding optimal pre-commitment strategy.

Our main contributions are as follows.

* •

  We formulate a discrete-intervention control problem with a two-step feedback policy evaluated at pre- and post-decision times. This captures settings where a pre-decision adjustment (e.g. withdrawal/consumption/liquidation) is coupled with a post-decision allocation step, with both actions subject to pointwise constraints.
* •

  We represent a broad class of risk-reward objectives via a finite-dimensional performance vector extracted from the controlled recursion, allowing terminal and discrete-time path-dependent statistics. The risk functional can be specified through auxiliary-variable optimization representations (e.g. Conditional Value-at-Risk and buffered probability of exceedance), as well as path-based measures such as realized quadratic variation, with optional higher-moment dependence. This yields a modular objective class within our convergence framework.
* •

  We parameterize the two policy components by feedforward NNs equipped with constraint-enforcing output layers (e.g. interval and simplex maps), so feasibility holds by construction while the optimization is unconstrained in the NN weights.
* •

  We replace global continuity requirements with a weaker “null discontinuity” condition: the optimal feedback maps may be discontinuous provided their discontinuity sets are hit with probability zero under the optimal controlled state at intervention times. Using a probabilistic moving-input stability argument (based on the Portmanteau theorem [[5](#bib.bib5)]), we propagate NN approximation through the controlled recursion without requiring global continuity of the optimizer.
* •

  Under compact-domain regularity conditions, we prove that the empirical optimum of the NN-parametrized objective converges in probability to the true optimal value as NN capacity and training sample size increase. The argument is modular, separating (i) approximation within the admissible policy class, (ii) propagation through the controlled recursion under moving-input stability, (iii) preservation under a general scalarized risk–reward functional, and (iv) a uniform law of large numbers for the empirical objective.

Numerical experiments on a representative Defined Contribution decumulation problem, in which withdrawals and allocations are constrained and the computed optimal withdrawal policy exhibits bang–bang structure, are benchmarked against a provably convergent low-dimensional grid-based reference value.
In addition to the predicted convergence-in-probability behavior as NN capacity and training sample size increase, the learned withdrawal and allocation heat maps show excellent agreement with the reference policies, and these conclusions remain stable under evaluation on a large independent out-of-sample scenario set.

## 2 Problem formulation

### 2.1 Probability space and intervention times

We work on a complete filtered probability space
(Ω,ℱ,{ℱt}0≤t≤T,ℙ)\big(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{0\leq t\leq T},\mathbb{P}\big),
satisfying the usual conditions on a finite horizon T>0T>0.
Within this probabilistic framework, decisions are made at a predetermined, equally spaced set of intervention times

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯={tm:tm=m​Δ​t,m=0,…,M},Δ​t=T/M,\mathcal{T}=\{t\_{m}:\ t\_{m}=m\Delta t,\ m=0,\ldots,M\},\qquad\Delta t=T/M, |  | (2.1) |

where t0=0t\_{0}=0 is the initial time.111Equal spacing is assumed for notational simplicity; the analysis extends directly to any fixed finite set of intervention times.
At each tm∈𝒯t\_{m}\in\mathcal{T}, we distinguish a pre-decision time tm−t\_{m}^{-} and a post-decision time tm+t\_{m}^{+}.
With the shorthand t−:=t−ϵt^{-}:=t-\epsilon and t+:=t+ϵt^{+}:=t+\epsilon (as ϵ→0+\epsilon\to 0^{+}), we write
fm−:=limϵ→0+f​(tm−ϵ)f\_{m^{-}}:=\lim\_{\epsilon\to 0^{+}}f(t\_{m}-\epsilon) and
fm+:=limϵ→0+f​(tm+ϵ)f\_{m^{+}}:=\lim\_{\epsilon\to 0^{+}}f(t\_{m}+\epsilon).

### 2.2 Exogenous input process

Fix an integer da≥1d\_{a}\geq 1.
Let Ym:=(Ym(i))i=1da∈ℝdaY\_{m}:=(Y\_{m}^{(i)})\_{i=1}^{d\_{a}}\in\mathbb{R}^{d\_{a}} denote an exogenous input (or shock) vector at each tm∈𝒯t\_{m}\in\mathcal{T}.
Then {Ym}m=1M\{Y\_{m}\}\_{m=1}^{M} defines an ℝda\mathbb{R}^{d\_{a}}-valued discrete-time stochastic process adapted to
{ℱtm−}m=1M\{\mathcal{F}\_{t\_{m}^{-}}\}\_{m=1}^{M}, where YmY\_{m} is realized over [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}] and observed at time tm−t\_{m}^{-}.
We write this process as YY, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y:={Ym}m=1M,Ym:=(Ym(i))i=1da.Y:=\{Y\_{m}\}\_{m=1}^{M},\qquad Y\_{m}:=(Y\_{m}^{(i)})\_{i=1}^{d\_{a}}. |  | (2.2) |

Assume 𝔼​[‖Ym‖]<∞\mathbb{E}[\|Y\_{m}\|]<\infty for each m∈{1,…,M}m\in\{1,\ldots,M\},
where ∥⋅∥\|\cdot\| denotes a fixed norm on ℝda\mathbb{R}^{d\_{a}}.

### 2.3 State, admissible controls, and controlled dynamics

We consider a scalar controlled state process {W​(t)}0≤t≤T\{W(t)\}\_{0\leq t\leq T}.
As feature (state) variables, we use time and the current state value,

|  |  |  |
| --- | --- | --- |
|  | ϕ​(t):=(t,W​(t)),𝒟ϕ:=[0,T]×ℝ.\phi(t):=(t,W(t)),\qquad\mathcal{D}\_{\phi}:=[0,T]\times\mathbb{R}. |  |

A two-step feedback control is a pair 𝒫=(q,p)\mathcal{P}=(q,p) of Borel measurable maps

|  |  |  |
| --- | --- | --- |
|  | q:𝒟ϕ→ℝ,p:𝒟ϕ→ℝda,q:\mathcal{D}\_{\phi}\to\mathbb{R},\qquad p:\mathcal{D}\_{\phi}\to\mathbb{R}^{d\_{a}}, |  |

where qq is applied at the pre-decision times tm−t\_{m}^{-} for m=0,…,Mm=0,\ldots,M, and
pp is applied at the post-decision times tm+t\_{m}^{+} for m=0,…,M−1m=0,\ldots,M-1
(i.e. no post-decision action is taken at tM+t\_{M}^{+}). In many applications, qq represents a pre-decision state adjustment (injection or extraction) and pp an allocation of a scalar resource among dad\_{a} components, but our analysis only uses measurability and the pointwise constraints below.

Pointwise constraints.
We impose (i) an interval-type constraint on the pre-decision action qq and (ii) a simplex-type constraint on the post-decision action pp.
For given constants qmin≤qmaxq\_{\min}\leq q\_{\max}, define the admissible pre-decision set map

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒵q​(w)={[qmin,qmax],if ​w≥qmax,[qmin,w],if ​qmin<w<qmax,{qmin},if ​w≤qmin.\mathcal{Z}\_{q}(w)=\begin{cases}\left[q\_{\min},\,q\_{\max}\right],&\text{if }w\geq q\_{\max},\\[2.0pt] \left[q\_{\min},\,w\right],&\text{if }q\_{\min}<w<q\_{\max},\\[2.0pt] \left\{q\_{\min}\right\},&\text{if }w\leq q\_{\min}.\end{cases} |  | (2.3) |

Admissible post-decision actions lie in the simplex

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒵p={z∈ℝda:zi≥0,∑i=1dazi=1}.\mathcal{Z}\_{p}=\big\{z\in\mathbb{R}^{d\_{a}}:\ z\_{i}\geq 0,\ \sum\_{i=1}^{d\_{a}}z\_{i}=1\big\}. |  | (2.4) |

Accordingly, define the admissible policy classes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒢q\displaystyle\mathcal{G}\_{q} | ={q:𝒟ϕ→ℝ|q is Borel measurable and q(t,w)∈𝒵q(w)∀(t,w)∈𝒟ϕ},\displaystyle=\left\{q:\mathcal{D}\_{\phi}\to\mathbb{R}\ \middle|\ q\text{ is Borel measurable and }q(t,w)\in\mathcal{Z}\_{q}(w)\ \forall(t,w)\in\mathcal{D}\_{\phi}\right\}, |  | (2.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒢p\displaystyle\mathcal{G}\_{p} | ={p:𝒟ϕ→ℝda|p is Borel measurable and p(t,w)∈𝒵p∀(t,w)∈𝒟ϕ},\displaystyle=\left\{p:\mathcal{D}\_{\phi}\to\mathbb{R}^{d\_{a}}\ \middle|\ p\text{ is Borel measurable and }p(t,w)\in\mathcal{Z}\_{p}\ \forall(t,w)\in\mathcal{D}\_{\phi}\right\}, |  | (2.6) |

and the admissible control pairs

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢={𝒫=(q,p):q∈𝒢q,p∈𝒢p}.\mathcal{G}=\left\{\mathcal{P}=(q,p):\ q\in\mathcal{G}\_{q},\ p\in\mathcal{G}\_{p}\right\}. |  | (2.7) |

Controlled recursion at intervention times.
Given 𝒫∈𝒢\mathcal{P}\in\mathcal{G} and the exogenous input process YY, let
{W​(t;𝒫,Y)}0≤t≤T\{W(t;\mathcal{P},Y)\}\_{0\leq t\leq T} denote the induced controlled state process.
When the dependence on (𝒫,Y)(\mathcal{P},Y) is understood, we write W​(t)≡W​(t;𝒫,Y)W(t)\equiv W(t;\mathcal{P},Y). We also write W​(T+;𝒫,Y)W(T^{+};\mathcal{P},Y) for the terminal post-decision state immediately after the final
pre-decision action at time TT (if any).

Fix measurable update maps

|  |  |  |
| --- | --- | --- |
|  | Uq:[0,T]×ℝ×ℝ→ℝ,Up:[0,T]×ℝ×ℝda×ℝda→ℝ.U\_{q}:[0,T]\times\mathbb{R}\times\mathbb{R}\to\mathbb{R},\qquad U\_{p}:[0,T]\times\mathbb{R}\times\mathbb{R}^{d\_{a}}\times\mathbb{R}^{d\_{a}}\to\mathbb{R}. |  |

Given 𝒫∈𝒢\mathcal{P}\in\mathcal{G} and YY, we define the induced controlled state sequence recursively by

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(tm+;𝒫,Y)=Uq​(tm,W​(tm−;𝒫,Y),q​(tm−,W​(tm−;𝒫,Y))),W(t\_{m}^{+};\mathcal{P},Y)=U\_{q}\left(t\_{m},\;W(t\_{m}^{-};\mathcal{P},Y),\;q\left(t\_{m}^{-},W(t\_{m}^{-};\mathcal{P},Y)\right)\right), |  | (2.8) |

for m=0,…,Mm=0,\ldots,M, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(tm+1−;𝒫,Y)=Up​(tm,W​(tm+;𝒫,Y),p​(tm+,W​(tm+;𝒫,Y)),Ym+1),W(t\_{m+1}^{-};\mathcal{P},Y)=U\_{p}\left(t\_{m},\;W(t\_{m}^{+};\mathcal{P},Y),\;p\left(t\_{m}^{+},W(t\_{m}^{+};\mathcal{P},Y)\right),\;Y\_{m+1}\right), |  | (2.9) |

for m=0,…,M−1m=0,\ldots,M-1, with initial condition W​(t0−)=w0W(t\_{0}^{-})=w\_{0}.
We interpret W​(T+;𝒫,Y)W(T^{+};\mathcal{P},Y) as the terminal post-decision state after the final pre-decision action at T=tMT=t\_{M}.
We write W​(tm±):=W​(tm±;𝒫,Y)W(t\_{m}^{\pm}):=W(t\_{m}^{\pm};\mathcal{P},Y) whenever no confusion can arise.

###### Remark 2.1 (Well-posedness of the controlled recursion).

Fix 𝒫∈𝒢\mathcal{P}\in\mathcal{G} and YY.
Starting from W​(t0−)=w0W(t\_{0}^{-})=w\_{0}, the update rules ([2.8](#S2.E8 "Equation 2.8 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))–([2.9](#S2.E9 "Equation 2.9 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))
define recursively a unique finite sequence {W​(tm−),W​(tm+)}m=0M\{W(t\_{m}^{-}),W(t\_{m}^{+})\}\_{m=0}^{M} whenever the maps UqU\_{q} and UpU\_{p} are measurable.
The convergence analysis later only uses measurability and continuity of these updates on bounded sets, and it allows piecewise-defined dynamics (e.g. regime switching) provided the realized recursion is continuous in the current state and action variables on the relevant bounded domain.

### 2.4 Risk–reward objective

Throughout, 𝔼𝒫w0,t0−​[⋅]\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}[\cdot] denotes expectation under ℙ\mathbb{P} with respect to the probability law induced by applying the control pair 𝒫\mathcal{P}, conditional on the initial condition W​(t0−)=w0W(t\_{0}^{-})=w\_{0}. The only source of randomness is the exogenous process YY.

Because the horizon is finite and actions are applied only at the finite intervention set 𝒯\mathcal{T}, we consider a broad class of risk–reward objectives that can be expressed in terms of a finite-dimensional random performance vector constructed from the controlled state sequence and the realized actions at the intervention times.
Specifically, for any 𝒫\mathcal{P} and YY, we define a finite-dimensional performance vector
S​(𝒫,Y)∈ℝdS(\mathcal{P},Y)\in\mathbb{R}^{d} by collecting a chosen subset of the controlled state and action variables at the intervention times, for example

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | S(𝒫,Y):=(\displaystyle S(\mathcal{P},Y)=\Big( | (W​(tm−;𝒫,Y))m=0M,(W​(tm+;𝒫,Y))m=0M,\displaystyle\big(W(t\_{m}^{-};\mathcal{P},Y)\big)\_{m=0}^{M},\;\big(W(t\_{m}^{+};\mathcal{P},Y)\big)\_{m=0}^{M},\; |  | (2.10) |
|  |  | (q(tm−,W(tm−;𝒫,Y)))m=0M,(p(tm+,W(tm+;𝒫,Y)))m=0M−1),\displaystyle\big(q(t\_{m}^{-},W(t\_{m}^{-};\mathcal{P},Y))\big)\_{m=0}^{M},\;\big(p(t\_{m}^{+},W(t\_{m}^{+};\mathcal{P},Y))\big)\_{m=0}^{M-1}\Big), |  |

where d<∞d<\infty depends on the selected components (in particular, d≤3​(M+1)+M​dad\leq 3(M+1)+Md\_{a} for the collection displayed in ([2.10](#S2.E10 "Equation 2.10 ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))).222The specific contents of SS can be adapted to the application; the only requirement for the convergence pipeline is that SS is a finite-dimensional measurable functional of the controlled recursion.

#### 2.4.1 Reward

Given the performance vector S​(𝒫,Y)S(\mathcal{P},Y), the reward component of the objective is defined as the expected value of a measurable function of SS.
Let ℛ:ℝd→ℝ\mathcal{R}:\mathbb{R}^{d}\to\mathbb{R} be measurable and define the reward functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥ℛ​(w0,t0−;𝒫):=𝔼𝒫w0,t0−​[ℛ​(S​(𝒫,Y))].\mathcal{J}\_{\mathcal{R}}(w\_{0},t\_{0}^{-};\mathcal{P}):=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[\,\mathcal{R}(S(\mathcal{P},Y))\,\big]. |  | (2.11) |

Here S​(𝒫,Y)∈ℝdS(\mathcal{P},Y)\in\mathbb{R}^{d} is a user-chosen finite-dimensional vector of terminal and/or path-dependent statistics of the controlled state/action sequence (e.g. terminal state and selected intermediate values).
This template covers, for example:

* •

  *Terminal rewards:* 
  Choose S​(𝒫,Y):=W​(T+)∈ℝS(\mathcal{P},Y):=W(T^{+})\in\mathbb{R}.
  Let ℛ:ℝ→ℝ\mathcal{R}:\mathbb{R}\to\mathbb{R} be defined by ℛ​(s)=U​(s)\mathcal{R}(s)=U(s),
  where U:ℝ→ℝU:\mathbb{R}\to\mathbb{R} is a given measurable payoff/utility function.
  Then ℛ​(S​(𝒫,Y))=U​(W​(T+))\mathcal{R}\big(S(\mathcal{P},Y)\big)=U\!\left(W(T^{+})\right).
  As a special case, taking U​(s)=sU(s)=s yields the linear terminal reward
  ℛ​(S​(𝒫,Y))=W​(T+)\mathcal{R}\big(S(\mathcal{P},Y)\big)=W(T^{+}).
* •

  *Cumulative adjustment rewards:*
  Choose S​(𝒫,Y):=(q​(tm−,W​(tm−)))m=0M∈ℝM+1S(\mathcal{P},Y):=\left(q\!\left(t\_{m}^{-},W(t\_{m}^{-})\right)\right)\_{m=0}^{M}\in\mathbb{R}^{M+1}.
  Let ℛ:ℝM+1→ℝ\mathcal{R}:\mathbb{R}^{M+1}\to\mathbb{R} be defined by
  ℛ​(s)=∑m=0Msm\mathcal{R}(s)=\sum\_{m=0}^{M}s\_{m}.
  Then
  ℛ​(S​(𝒫,Y))=∑m=0Mqm​(⋅)\mathcal{R}\big(S(\mathcal{P},Y)\big)=\sum\_{m=0}^{M}q\_{m}(\cdot).
  In a pension setting, qm​(⋅)q\_{m}(\cdot) may represent the withdrawal at time tmt\_{m}, so 𝔼​[∑m=0Mqm​(⋅)]\mathbb{E}\!\big[\sum\_{m=0}^{M}q\_{m}(\cdot)\big] is the cumulative expected withdrawals over the horizon.
* •

  *Quadratic / one-sided quadratic criteria [[30](#bib.bib30), [9](#bib.bib9)]:*
  Choose S​(𝒫,Y):=W​(T+)∈ℝS(\mathcal{P},Y):=W(T^{+})\in\mathbb{R}.
  Let ℛ:ℝ→ℝ\mathcal{R}:\mathbb{R}\to\mathbb{R} be defined by
  ℛ​(s)=−(s−κ)2\mathcal{R}(s)=-(s-\kappa)^{2} or
  ℛ​(s)=−(min⁡{s−κ,0})2+λ​s\mathcal{R}(s)=-(\min\{s-\kappa,0\})^{2}+\lambda s,
  with target level κ∈ℝ\kappa\in\mathbb{R} and weight λ≥0\lambda\geq 0.
  Then ℛ​(S​(𝒫,Y))=−(W​(T+)−κ)2\mathcal{R}\big(S(\mathcal{P},Y)\big)=-(W(T^{+})-\kappa)^{2}
  or
  ℛ​(S​(𝒫,Y))=−(min⁡{W​(T+)−κ,0})2+λ​W​(T+)\mathcal{R}\big(S(\mathcal{P},Y)\big)=-(\min\{W(T^{+})-\kappa,0\})^{2}+\lambda\,W(T^{+}).

#### 2.4.2 Risk

We represent a broad class of risk measures using an auxiliary variable ξ∈Ξ\xi\in\Xi (e.g. a threshold in tail-risk criteria), where Ξ⊆ℝ\Xi\subseteq\mathbb{R} is an auxiliary-variable domain. Some risk measures also depend on moments of the performance vector; to accommodate this, we allow an optional moment mapping. Specifically, let Ψ:ℝd→ℝdΨ\Psi:\mathbb{R}^{d}\to\mathbb{R}^{d\_{\Psi}} be measurable and define the (finite-dimensional) moment vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | S¯​(𝒫):=𝔼𝒫w0,t0−​[Ψ​(S​(𝒫,Y))]∈ℝdΨ.\bar{S}(\mathcal{P}):=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[\,\Psi(S(\mathcal{P},Y))\,\big]\in\mathbb{R}^{d\_{\Psi}}. |  | (2.12) |

(If moment-dependence is not needed, take dΨ=0d\_{\Psi}=0 and suppress S¯\bar{S} below.)
Let ℒ:Ξ×ℝd×ℝdΨ→ℝ\mathcal{L}:\Xi\times\mathbb{R}^{d}\times\mathbb{R}^{d\_{\Psi}}\to\mathbb{R} be measurable. Define the risk functional by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥ℒ​(w0,t0−;𝒫):=supξ∈Ξ𝔼𝒫w0,t0−​[ℒ​(ξ,S​(𝒫,Y),S¯​(𝒫))].\mathcal{J}\_{\mathcal{L}}(w\_{0},t\_{0}^{-};\mathcal{P}):=\sup\_{\xi\in\Xi}\,\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[\,\mathcal{L}(\xi,S(\mathcal{P},Y),\bar{S}(\mathcal{P}))\,\big]. |  | (2.13) |

This template includes, for example:

* •

  *Rockafellar–Uryasev CVaR of the terminal state [[25](#bib.bib25)]:*
  Choose S​(𝒫,Y):=W​(T+)∈ℝS(\mathcal{P},Y):=W(T^{+})\in\mathbb{R} and take Ξ=ℝ\Xi=\mathbb{R}.
  No moment dependence is needed (take dΨ=0d\_{\Psi}=0 and suppress S¯\bar{S}).
  Let ℒ:Ξ×ℝ→ℝ\mathcal{L}:\Xi\times\mathbb{R}\to\mathbb{R} be defined by
  ℒ​(ξ,s)=ξ+1α​min⁡{s−ξ,0}\mathcal{L}(\xi,s)=\xi+\frac{1}{\alpha}\min\{s-\xi,0\} for α∈(0,1)\alpha\in(0,1).
  Then
  𝒥ℒ​(w0,t0−;𝒫)=supξ∈ℝ𝔼𝒫w0,t0−​[ξ+1α​min⁡{W​(T+)−ξ, 0}]\mathcal{J}\_{\mathcal{L}}(w\_{0},t\_{0}^{-};\mathcal{P})=\sup\_{\xi\in\mathbb{R}}\,\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\left[\xi+\frac{1}{\alpha}\min\!\left\{W(T^{+})-\xi,\,0\right\}\right], corresponding to CVaRα​(W​(T+))\mathrm{CVaR}\_{\alpha}\!\big(W(T^{+})\big) (under the gain-based convention).
* •

  *Buffered probability of exceedance (bPoE) [[10](#bib.bib10), [19](#bib.bib19)]:*
  Choose S​(𝒫,Y):=W​(T+)∈ℝS(\mathcal{P},Y):=W(T^{+})\in\mathbb{R} and fix a threshold level D∈ℝD\in\mathbb{R}.
  Take Ξ:=(D,∞)\Xi:=(D,\infty) and no moment dependence (set dΨ=0d\_{\Psi}=0).
  Define ℒ:Ξ×ℝ→ℝ\mathcal{L}:\Xi\times\mathbb{R}\to\mathbb{R} by
  ℒ​(ξ,s):=−max⁡(1−s−Dξ−D, 0)\mathcal{L}(\xi,s):=-\max\!\left(1-\frac{s-D}{\xi-D},\,0\right) for ξ∈Ξ\xi\in\Xi.
  Then
  𝒥ℒ​(w0,t0−;𝒫)=supξ∈(D,∞)𝔼𝒫w0,t0−​[−max⁡(1−W​(T+)−Dξ−D, 0)]\mathcal{J}\_{\mathcal{L}}(w\_{0},t\_{0}^{-};\mathcal{P})=\sup\_{\xi\in(D,\infty)}\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[-\max\!\big(1-\tfrac{W(T^{+})-D}{\xi-D},\,0\big)\big], which corresponds to −bPoED​(W​(T+))-\mathrm{bPoE}\_{D}(W(T^{+})) via the standard inf\inf-representation in [[10](#bib.bib10), [19](#bib.bib19)].
* •

  *Quadratic variation risk [[28](#bib.bib28)]:*
  Choose S​(𝒫,Y):=(W​(tm+))m=0M−1∪(W​(tm+1−))m=0M−1∈ℝ2​MS(\mathcal{P},Y):=\big(W(t\_{m}^{+})\big)\_{m=0}^{M-1}\,\cup\,\big(W(t\_{m+1}^{-})\big)\_{m=0}^{M-1}\in\mathbb{R}^{2M}, i.e.,
  S​(𝒫,Y)=(s0,…,s2​M−1)S(\mathcal{P},Y)=(s\_{0},\ldots,s\_{2M-1}) with sm=W​(tm+)s\_{m}=W(t\_{m}^{+}) and sM+m=W​(tm+1−)s\_{M+m}=W(t\_{m+1}^{-}) for m=0,…,M−1m=0,\ldots,M-1.
  Take Ξ={0}\Xi=\{0\} and set dΨ=0d\_{\Psi}=0.
  Define ℒ:Ξ×ℝ2​M→ℝ\mathcal{L}:\Xi\times\mathbb{R}^{2M}\to\mathbb{R} by
  ℒ​(0,s)=−∑m=0M−1(sM+m−sm)2\mathcal{L}(0,s)=-\sum\_{m=0}^{M-1}\big(s\_{M+m}-s\_{m}\big)^{2}.
  Then 𝒥ℒ​(w0,t0−;𝒫)=𝔼𝒫w0,t0−​[ℒ​(0,S​(𝒫,Y))]\mathcal{J}\_{\mathcal{L}}(w\_{0},t\_{0}^{-};\mathcal{P})=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[\mathcal{L}(0,S(\mathcal{P},Y))\big].
* •

  *Variance (via an auxiliary variable):*
  Choose S​(𝒫,Y):=W​(T+)∈ℝS(\mathcal{P},Y):=W(T^{+})\in\mathbb{R} and take Ξ=ℝ\Xi=\mathbb{R}.
  Let ℒ:Ξ×ℝ→ℝ\mathcal{L}:\Xi\times\mathbb{R}\to\mathbb{R} be defined by ℒ​(ξ,s)=−(s−ξ)2\mathcal{L}(\xi,s)=-(s-\xi)^{2}.
  Then

  |  |  |  |
  | --- | --- | --- |
  |  | 𝒥ℒ​(w0,t0−;𝒫)=supξ∈ℝ𝔼𝒫w0,t0−​[−(W​(T+)−ξ)2]=−Var​(W​(T+)).\mathcal{J}\_{\mathcal{L}}(w\_{0},t\_{0}^{-};\mathcal{P})=\sup\_{\xi\in\mathbb{R}}\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[-(W(T^{+})-\xi)^{2}\big]=-\mathrm{Var}\!\big(W(T^{+})\big). |  |
* •

  *Semi-variance around the mean:*
  Choose S​(𝒫,Y):=W​(T+)∈ℝS(\mathcal{P},Y):=W(T^{+})\in\mathbb{R} and take Ξ={0}\Xi=\{0\}.
  Let Ψ:ℝ→ℝ\Psi:\mathbb{R}\to\mathbb{R} be defined by Ψ​(s)=s\Psi(s)=s, so that
  S¯​(𝒫)=𝔼𝒫w0,t0−​[W​(T+)]\bar{S}(\mathcal{P})=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[W(T^{+})\big].
  Define ℒ:Ξ×ℝ×ℝ→ℝ\mathcal{L}:\Xi\times\mathbb{R}\times\mathbb{R}\to\mathbb{R} by
  ℒ(0,s,s¯)=−min{s−s¯,0}2\mathcal{L}(0,s,\bar{s})=-\min\{s-\bar{s},0\}^{2}.
  Then

  |  |  |  |
  | --- | --- | --- |
  |  | 𝒥ℒ(w0,t0−;𝒫)=𝔼𝒫w0,t0−[−min{W(T+)−S¯(𝒫), 0}2],S¯(𝒫)=𝔼𝒫w0,t0−[W(T+)].\mathcal{J}\_{\mathcal{L}}(w\_{0},t\_{0}^{-};\mathcal{P})=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\left[-\min\!\left\{W(T^{+})-\bar{S}(\mathcal{P}),\,0\right\}^{2}\right],\quad\bar{S}(\mathcal{P})=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[W(T^{+})\big]. |  |

#### 2.4.3 Scalarized risk–reward objective

Fix a scalarization parameter γ>0\gamma>0 and define the scalarized criterion function

|  |  |  |
| --- | --- | --- |
|  | ℋ​(ξ,s,s¯):=ℛ​(s)+γ​ℒ​(ξ,s,s¯),(ξ,s,s¯)∈Ξ×ℝd×ℝdΨ.\mathcal{H}(\xi,s,\bar{s}):=\mathcal{R}(s)+\gamma\,\mathcal{L}(\xi,s,\bar{s}),\qquad(\xi,s,\bar{s})\in\Xi\times\mathbb{R}^{d}\times\mathbb{R}^{d\_{\Psi}}. |  |

For (ξ,𝒫)∈Ξ×𝒢(\xi,\mathcal{P})\in\Xi\times\mathcal{G}, define the corresponding scalarized objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(w0,t0−;ξ,𝒫):=𝔼𝒫w0,t0−​[ℋ​(ξ,S​(𝒫,Y),S¯​(𝒫))],V\left(w\_{0},t\_{0}^{-};\xi,\mathcal{P}\right):=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\left[\mathcal{H}\left(\xi,S(\mathcal{P},Y),\bar{S}(\mathcal{P})\right)\right], |  | (2.14) |

and the value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(w0,t0−):=sup𝒫∈𝒢,ξ∈ΞV​(w0,t0−;ξ,𝒫).V(w\_{0},t\_{0}^{-}):=\sup\_{\mathcal{P}\in\mathcal{G},\ \xi\in\Xi}\,V\left(w\_{0},t\_{0}^{-};\xi,\mathcal{P}\right). |  | (2.15) |

###### Remark 2.2 (Pre-commitment vs. time-consistent formulations).

The criterion ([2.14](#S2.E14 "Equation 2.14 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))–([2.15](#S2.E15 "Equation 2.15 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) is posed at the initial time t0−t\_{0}^{-}: the decision maker selects (ξ,𝒫)∈Ξ×𝒢(\xi,\mathcal{P})\in\Xi\times\mathcal{G} to maximize V​(w0,t0−;ξ,𝒫)V(w\_{0},t\_{0}^{-};\xi,\mathcal{P}) and then applies the resulting feedback maps 𝒫=(q,p)\mathcal{P}=(q,p) at all subsequent intervention times.

If the objective is separable in the dynamic-programming sense (i.e. it admits a recursive Bellman representation), this formulation coincides with the usual time-consistent optimal strategy. Otherwise, the objective is time-inconsistent and the solution corresponds to the optimal pre-commitment strategy.

### 2.5 Standing assumptions for the risk–reward control problem

This subsection collects regularity conditions on the risk-reward control problem
([2.14](#S2.E14 "Equation 2.14 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))-([2.15](#S2.E15 "Equation 2.15 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))
used in the convergence analysis.

###### Assumption 2.1 (Regularity conditions).

The following conditions hold.

1. (R1)

   (Bounded state.)
   There exist finite constants wmin<wmaxw\_{\min}<w\_{\max} such that, for every admissible 𝒫∈𝒢\mathcal{P}\in\mathcal{G},

   |  |  |  |
   | --- | --- | --- |
   |  | wmin≤W​(tm±;𝒫,Y)≤wmaxa.s.,m=0,…,M.w\_{\min}\leq W(t\_{m}^{\pm};\mathcal{P},Y)\leq w\_{\max}\quad\text{a.s.},\qquad m=0,\ldots,M. |  |
2. (R2)

   (Continuity of the update maps.)
   The map UqU\_{q} is continuous on

   |  |  |  |
   | --- | --- | --- |
   |  | [0,T]×[wmin,wmax]×[qmin,qmax][0,T]\times[w\_{\min},w\_{\max}]\times[q\_{\min},q\_{\max}] |  |

   and, for every r>0r>0, the map UpU\_{p} is continuous on

   |  |  |  |
   | --- | --- | --- |
   |  | [0,T]×[wmin,wmax]×𝒵p×{y∈ℝda:‖y‖≤r}.[0,T]\times[w\_{\min},w\_{\max}]\times\mathcal{Z}\_{p}\times\{y\in\mathbb{R}^{d\_{a}}:\ \|y\|\leq r\}. |  |
3. (R3)

   (Existence of an optimizer.)
   There exist (𝒫∗,ξ∗)∈𝒢×Ξ(\mathcal{P}^{\ast},\xi^{\ast})\in\mathcal{G}\times\Xi attaining the supremum in ([2.15](#S2.E15 "Equation 2.15 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), with 𝒫∗=(q∗,p∗)\mathcal{P}^{\ast}=(q^{\ast},p^{\ast}).
4. (R4)

   (Almost-sure continuity under the optimal policy.)
   For each mm, define

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Dq,m\displaystyle D\_{q,m} | :={w∈[wmin,wmax]:w↦q∗​(tm−,w)​is discontinuous at ​w},\displaystyle:=\big\{w\in[w\_{\min},w\_{\max}]:w\mapsto q^{\ast}(t\_{m}^{-},w)\ \text{is discontinuous at }w\big\}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | m=0,…,M,\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad m=0,\ldots,M, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Dp,m\displaystyle D\_{p,m} | :={w∈[wmin,wmax]:w↦p∗​(tm+,w)​is discontinuous at ​w},\displaystyle:=\big\{w\in[w\_{\min},w\_{\max}]:w\mapsto p^{\ast}(t\_{m}^{+},w)\ \text{is discontinuous at }w\big\}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | m=0,…,M−1,\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad m=0,\ldots,M-1, |  |

   with discontinuity for p∗p^{\ast} understood componentwise.
   Assume that these discontinuity sets are
   ℙ\mathbb{P}-null under the optimal state at the intervention times, i.e.

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ℙ​(W​(tm−;𝒫∗,Y)∈Dq,m)\displaystyle\mathbb{P}\!\left(W(t\_{m}^{-};\mathcal{P}^{\ast},Y)\in D\_{q,m}\right) | =0,m=0,…,M, and\displaystyle=0,\quad m=0,\ldots,M,\quad\text{ and } |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ℙ​(W​(tm+;𝒫∗,Y)∈Dp,m)\displaystyle\mathbb{P}\!\left(W(t\_{m}^{+};\mathcal{P}^{\ast},Y)\in D\_{p,m}\right) | =0,m=0,…,M−1.\displaystyle=0,\quad m=0,\ldots,M-1. |  |
5. (R5)

   (Moment map regularity.)
   Assume Ψ\Psi is continuous on 𝒵\mathcal{Z},
   where 𝒵⊂ℝd\mathcal{Z}\subset\mathbb{R}^{d}
   is a compact set such that the vector S​(𝒫,Y)∈𝒵S(\mathcal{P},Y)\in\mathcal{Z} a.s. for all 𝒫∈𝒢\mathcal{P}\in\mathcal{G}
   (see Section [2.6](#S2.SS6 "2.6 Discussion of Assumption 2.1 ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") for a sufficient construction of 𝒵\mathcal{Z}).
6. (R6)

   (Compactness of the auxiliary-variable domain.)
   Assume that Ξ⊂ℝ\Xi\subset\mathbb{R} is nonempty and compact.
7. (R7)

   (Regularity of scalarized criterion function.)
   Let 𝒵¯:=conv​(Ψ​(𝒵))⊂ℝdΨ\bar{\mathcal{Z}}:=\mathrm{conv}(\Psi(\mathcal{Z}))\subset\mathbb{R}^{d\_{\Psi}}, where 𝒵\mathcal{Z} is the compact set from (R5) and conv​(⋅)\mathrm{conv}(\cdot) denotes the convex hull.

   Assume the functional ℋ:Ξ×ℝd×ℝdΨ→ℝ\mathcal{H}:\Xi\times\mathbb{R}^{d}\times\mathbb{R}^{d\_{\Psi}}\to\mathbb{R} is continuous in (ξ,s,s¯)(\xi,s,\bar{s}) on Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}}.

   In particular, since Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}} is compact, ℋ\mathcal{H} is bounded on Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}}.

### 2.6 Discussion of Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") ensures that convergence of the NN feedback controls propagates through the controlled recursion via continuity of the update maps, induces convergence of the finite-dimensional performance/moment vectors, and is preserved under the scalarized objective through continuity and compact-domain uniformity. Most conditions are local/compact-domain regularity statements, with compactness used mainly to obtain boundedness and uniform continuity needed for uniform laws of large numbers (ULLN).

Regarding (R1).
The uniform bounds on W​(tm±;𝒫,Y)W(t\_{m}^{\pm};\mathcal{P},Y) are strong but often natural in applications with physical or contractual state constraints (e.g. storage with capacity limits, state processes with reflecting/truncating mechanisms, or state updates that enforce admissible ranges by construction). In settings where the state is not globally bounded, one can sometimes replace (R1) by straightforward localization arguments [[26](#bib.bib26), [15](#bib.bib15)], but this may complicate the continuity and uniform-convergence steps in subsequent proofs.

Regarding (R2).
Continuity is needed in all arguments of the update maps UqU\_{q} and UpU\_{p} that enter the recursion. In particular, the post-decision update ([2.9](#S2.E9 "Equation 2.9 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))
depends explicitly on the exogenous input Ym+1Y\_{m+1}. The continuity requirement for UpU\_{p} does not assume that YmY\_{m} is bounded; instead, it ensures continuity at all finite realizations of Ym+1Y\_{m+1}. If, in a particular application, one has an a.s. bound ‖Ym‖≤r0\|Y\_{m}\|\leq r\_{0} for some finite r0>0r\_{0}>0, then it suffices to assume continuity only on the set {y∈ℝda:‖y‖≤r0}\{y\in\mathbb{R}^{d\_{a}}:\ \|y\|\leq r\_{0}\}. Moreover, if UqU\_{q} or UpU\_{p} are piecewise-defined (e.g. due to regime switching), it suffices that the realized recursion is continuous in the current state and action variables on the relevant bounded regime.

Regarding (R3).
Existence of an optimizer (𝒫∗,ξ∗)(\mathcal{P}^{\ast},\xi^{\ast}) is a standard standing assumption in convergence results for value functions: it lets us compare the NN value against an attained optimum. If an optimizer fails to exist, many arguments can be adapted by working with an ε\varepsilon-optimal sequence (𝒫ε,ξε)(\mathcal{P}^{\varepsilon},\xi^{\varepsilon}) [[3](#bib.bib3)]. We keep (R3) to avoid additional bookkeeping.

Regarding (R4).
This condition permits discontinuous optimal feedback maps (e.g. threshold/bang–bang rules) provided the optimal state does not hit their discontinuity sets with positive probability at intervention times. It is strictly weaker than assuming continuity of q∗​(tm−,⋅)q^{\ast}(t\_{m}^{-},\cdot) and p∗​(tm+,⋅)p^{\ast}(t\_{m}^{+},\cdot) on [wmin,wmax][w\_{\min},w\_{\max}]. Technically, it is the minimal condition needed to apply extended continuous-mapping arguments in the decision and state convergence proofs (see Lemmas [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")–[4.3](#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Convergence of the controlled state sequence ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

Regarding (R5).
A simple sufficient way to ensure the existence of a compact set 𝒵\mathcal{Z} in (R5) is to combine:
(i) the uniform state bounds W​(tm±)∈[wmin,wmax]W(t\_{m}^{\pm})\in[w\_{\min},w\_{\max}] a.s. for all mm and all 𝒫∈𝒢\mathcal{P}\in\mathcal{G}, and
(ii) the action constraints q​(t,w)∈𝒵q​(w)⊂[qmin,qmax]q(t,w)\in\mathcal{Z}\_{q}(w)\subset[q\_{\min},q\_{\max}] and p​(t,w)∈𝒵pp(t,w)\in\mathcal{Z}\_{p} as stated in ([2.3](#S2.E3 "Equation 2.3 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))-([2.4](#S2.E4 "Equation 2.4 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
Because S​(𝒫,Y)S(\mathcal{P},Y) is finite-dimensional and built from finitely many state/action components at the intervention times, these bounds imply that every coordinate of S​(𝒫,Y)S(\mathcal{P},Y) is a.s. bounded uniformly over 𝒫∈𝒢\mathcal{P}\in\mathcal{G}, hence S​(𝒫,Y)S(\mathcal{P},Y) takes values in a compact product set, which can be taken as 𝒵\mathcal{Z}.

Regarding (R6).
Compactness of Ξ\Xi is mainly a technical convenience: combined with continuity of ℋ\mathcal{H} on Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}}, it implies (i) boundedness of ℋ\mathcal{H} on this domain and (ii) uniform continuity properties (e.g. uniform continuity in the s¯\bar{s}-argument uniformly over (ξ,s)∈Ξ×𝒵(\xi,s)\in\Xi\times\mathcal{Z}) that simplify subsequent proofs.
In many standard auxiliary-variable representations, it is without loss of optimality to take Ξ\Xi compact, since boundedness of the relevant performance statistic typically allows restricting ξ\xi to a compact interval.

In the examples below, XX denotes the scalar performance statistic entering the auxiliary-variable representation (e.g. a coordinate of S​(𝒫,Y)S(\mathcal{P},Y), hence a.s. bounded once (R5) holds). For the Rockafellar–Uryasev representation of CVaR​(X)\mathrm{CVaR}(X), any optimizer ξ∗\xi^{\ast} lies in [xmin,xmax][x\_{\min},x\_{\max}], so one may take Ξ=[xmin,xmax]\Xi=[x\_{\min},x\_{\max}]. Likewise, for the auxiliary-variable representation of variance,
supξ∈ℝ𝔼​[−(X−ξ)2]\sup\_{\xi\in\mathbb{R}}\mathbb{E}[-(X-\xi)^{2}], the optimizer is ξ∗=𝔼​[X]∈[xmin,xmax]\xi^{\ast}=\mathbb{E}[X]\in[x\_{\min},x\_{\max}], so the search may be restricted to a compact interval.
For bPoE-type representations with the constraint ξ>D\xi>D, one can similarly restrict Ξ\Xi to a compact interval [ξ¯,ξ¯]⊂(D,∞)[\,\underline{\xi},\,\overline{\xi}\,]\subset(D,\infty)
that contains an optimizer.

More generally, it suffices that for each (s,s¯)∈𝒵×𝒵¯(s,\bar{s})\in\mathcal{Z}\times\bar{\mathcal{Z}} the map ξ↦ℋ​(ξ,s,s¯)\xi\mapsto\mathcal{H}(\xi,s,\bar{s}) is coercive, in the sense that ℋ​(ξ,s,s¯)→−∞\mathcal{H}(\xi,s,\bar{s})\to-\infty as |ξ|→∞|\xi|\to\infty uniformly over (s,s¯)(s,\bar{s}) on compact sets. In this case the maximizer over ξ\xi must lie in some bounded interval, and one may replace Ξ\Xi by a compact interval containing all optimizers [[24](#bib.bib24)].

Regarding (R7).
Recall the moment vector S¯​(𝒫):=𝔼​[Ψ​(S​(𝒫,Y))]\bar{S}(\mathcal{P}):=\mathbb{E}[\Psi(S(\mathcal{P},Y))] defined in ([2.12](#S2.E12 "Equation 2.12 ‣ 2.4.2 Risk ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")). Then S¯​(𝒫)∈𝒵¯\bar{S}(\mathcal{P})\in\bar{\mathcal{Z}} for all 𝒫∈𝒢\mathcal{P}\in\mathcal{G}, where 𝒵¯:=conv​(Ψ​(𝒵))\bar{\mathcal{Z}}:=\mathrm{conv}(\Psi(\mathcal{Z})), so the third argument of ℋ\mathcal{H} ranges over 𝒵¯\bar{\mathcal{Z}}.
To see this, note that (R5) gives S​(𝒫,Y)∈𝒵S(\mathcal{P},Y)\in\mathcal{Z} a.s. for each 𝒫∈𝒢\mathcal{P}\in\mathcal{G}, hence Ψ​(S​(𝒫,Y))∈Ψ​(𝒵)\Psi(S(\mathcal{P},Y))\in\Psi(\mathcal{Z}) a.s. Since Ψ\Psi is continuous on the compact set 𝒵\mathcal{Z}, the image Ψ​(𝒵)\Psi(\mathcal{Z}) is compact. In finite dimensions, conv​(Ψ​(𝒵))\mathrm{conv}(\Psi(\mathcal{Z})) is also compact, and because it is convex and contains Ψ​(𝒵)\Psi(\mathcal{Z}), it contains the expectation of any Ψ​(𝒵)\Psi(\mathcal{Z})-valued random vector; in particular, S¯​(𝒫)=𝔼​[Ψ​(S​(𝒫,Y))]∈𝒵¯\bar{S}(\mathcal{P})=\mathbb{E}[\Psi(S(\mathcal{P},Y))]\in\bar{\mathcal{Z}}.

With (R6)–(R7), continuity of ℋ\mathcal{H} on the compact set Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}} yields boundedness and the uniform continuity properties used in the subsequent proofs involving ULLN.

## 3 A neural network approach

We approximate the two-step feedback control 𝒫=(q,p)\mathcal{P}=(q,p) by two interacting fully connected FNNs: a scalar network for the pre-decision action qq and a vector network for the post-decision action pp.
The pointwise constraints ([2.3](#S2.E3 "Equation 2.3 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))–([2.4](#S2.E4 "Equation 2.4 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) are enforced by customized output-layer maps, yielding an unconstrained optimization problem over the network parameters.

### 3.1 Preliminaries

We use standard fully connected FNNs (multilayer perceptrons), i.e. compositions of affine maps and nonlinear activations.

###### Definition 3.1 (Feedforward neural network).

Consider a fully connected multilayer FNN with LL hidden layers. Layers are indexed by
l∈{0,1,…,L+1}l\in\{0,1,\ldots,L+1\}, where l=0l=0 is the input layer and l=L+1l=L+1 is the output
layer. Let νl∈ℕ\nu\_{l}\in\mathbb{N} be the number of nodes in layer ll. The function
F:ℝν0→ℝνL+1F:\mathbb{R}^{\nu\_{0}}\to\mathbb{R}^{\nu\_{L+1}} computed by the FNN is

|  |  |  |  |
| --- | --- | --- | --- |
|  | F=AL+1∘(ψL∘AL)∘⋯∘(ψ1∘A1),F=A\_{L+1}\circ(\psi\_{L}\circ A\_{L})\circ\cdots\circ(\psi\_{1}\circ A\_{1}), |  | (3.1) |

where Al​(x)=βl​x+blA\_{l}(x)=\beta\_{l}x+b\_{l} is affine with weights βl∈ℝνl×νl−1\beta\_{l}\in\mathbb{R}^{\nu\_{l}\times\nu\_{l-1}}
and bias bl∈ℝνlb\_{l}\in\mathbb{R}^{\nu\_{l}}, and ψl:ℝνl→ℝνl\psi\_{l}:\mathbb{R}^{\nu\_{l}}\to\mathbb{R}^{\nu\_{l}} is the
activation function for l=1,…,Ll=1,\ldots,L. No activation is applied at the output layer.

We collect all trainable parameters (weights and biases) as
θ=(βl,bl)l=1,…,L+1∈ℝη\theta=(\beta\_{l},b\_{l})\_{l=1,\ldots,L+1}\in\mathbb{R}^{\eta},
where η\eta denotes the total number of trainable parameters of the network.

For notational simplicity, we take all hidden layers to have the same width ν\nu and use the sigmoid activation
in each hidden layer. Let {ν(n)}n∈ℕ\{\nu^{(n)}\}\_{n\in\mathbb{N}} be a strictly increasing sequence with ν(n)→∞\nu^{(n)}\to\infty as n→∞n\to\infty. For each nn, let 𝒬n\mathcal{Q}\_{n} denote the class of FNNs
of the form ([3.1](#S3.E1 "Equation 3.1 ‣ Definition 3.1 (Feedforward neural network). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) with hidden-layer width ν(n)\nu^{(n)} (and fixed depth LL). Then
𝒬n⊆𝒬n+1\mathcal{Q}\_{n}\subseteq\mathcal{Q}\_{n+1}.

The next theorem states a universal approximation property in the probabilistic form convenient for our analysis.
Throughout, ∥⋅∥\|\cdot\| denotes a fixed norm on ℝd\mathbb{R}^{d} (with ambient dimension clear from context).

###### Theorem 3.1 (Universal approximation for a random input [[13](#bib.bib13), Thm. 2.4 and Cor. 2.7]).

Let XX be an ℝν0\mathbb{R}^{\nu\_{0}}-valued random variable and let
f:ℝν0→ℝdf:\mathbb{R}^{\nu\_{0}}\to\mathbb{R}^{d} be Borel measurable. Then there exists a sequence
{Fn}n∈ℕ\{F\_{n}\}\_{n\in\mathbb{N}}, where Fn=F​(⋅;θn)∈𝒬nF\_{n}=F(\cdot;\theta\_{n})\in\mathcal{Q}\_{n}, such that
for all ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | limn→∞ℙ​(‖Fn​(X)−f​(X)‖>ε)=0.\lim\_{n\to\infty}\mathbb{P}\!\left(\big\|F\_{n}(X)-f(X)\big\|>\varepsilon\right)=0. |  |

To encode constraints, we apply (measurable) customized maps at the output layer. The next lemma records that convergence in probability is preserved under composition with mappings that are continuous at the limit point almost surely.

###### Lemma 3.2 (Composition with (a.s.-continuous) activations).

Let XX be an ℝν0\mathbb{R}^{\nu\_{0}}-valued random variable. Let f:ℝν0→ℝdf:\mathbb{R}^{\nu\_{0}}\to\mathbb{R}^{d} and
ψ:ℝd→ℝk\psi:\mathbb{R}^{d}\to\mathbb{R}^{k} be measurable. Define the set of discontinuity points of ψ\psi by

|  |  |  |
| --- | --- | --- |
|  | Dψ:={y∈ℝd:y↦ψ​(y)​is discontinuous at ​y},D\_{\psi}:=\Big\{y\in\mathbb{R}^{d}:\ y\mapsto\psi(y)\ \text{is discontinuous at }y\Big\}, |  |

and assume that ℙ​(f​(X)∈Dψ)=0\mathbb{P}\!\left(f(X)\in D\_{\psi}\right)=0.
Then there exists a sequence {Fn}n∈ℕ\{F\_{n}\}\_{n\in\mathbb{N}} with
Fn=F​(⋅;θn)∈𝒬nF\_{n}=F(\cdot;\theta\_{n})\in\mathcal{Q}\_{n} such that, for all ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | limn→∞ℙ​(‖ψ​(Fn​(X))−ψ​(f​(X))‖>ε)=0.\lim\_{n\to\infty}\mathbb{P}\!\left(\big\|\psi\!\left(F\_{n}(X)\right)-\psi\!\left(f(X)\right)\big\|>\varepsilon\right)=0. |  |

A proof of Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2 (Composition with (a.s.-continuous) activations). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") is given in Appendix [A](#A1 "Appendix A Proof of Lemma 3.2 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

In practice, it is often convenient to use standard activations with open output ranges (e.g. sigmoid, softmax), which cannot represent boundary values exactly. The next lemma justifies approximation when the target range includes boundary points.

###### Lemma 3.3 (Boundary approximation via open-range activations).

Let XX be an ℝν0\mathbb{R}^{\nu\_{0}}-valued random variable and let g:ℝν0→[a,b]Ng:\mathbb{R}^{\nu\_{0}}\to[a,b]^{N} be measurable.
Let ψ:ℝN→(a,b)N\psi:\mathbb{R}^{N}\to(a,b)^{N} be continuous and assume that ψ\psi admits a measurable right inverse
ψr−1:(a,b)N→ℝN\psi^{-1}\_{r}:(a,b)^{N}\to\mathbb{R}^{N}, i.e. ψ∘ψr−1=Id(a,b)N\psi\circ\psi^{-1}\_{r}=\mathrm{Id}\_{(a,b)^{N}}.
Then, there exists a sequence {Fn}n∈ℕ\{F\_{n}\}\_{n\in\mathbb{N}} with
Fn=F​(⋅;θn)∈𝒬nF\_{n}=F(\cdot;\theta\_{n})\in\mathcal{Q}\_{n} such that, for all ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | limn→∞ℙ​(‖ψ​(Fn​(X))−g​(X)‖>ε)=0.\lim\_{n\to\infty}\mathbb{P}\!\left(\big\|\psi\!\left(F\_{n}(X)\right)-g(X)\big\|>\varepsilon\right)=0. |  |

For a proof of Lemma [3.3](#S3.Thmtheorem3 "Lemma 3.3 (Boundary approximation via open-range activations). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), see Appendix [B](#A2 "Appendix B Proof of Lemma 3.3 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

### 3.2 Pre-decision network

Let z~​(⋅;θq,n):𝒟ϕ→ℝ\widetilde{z}(\cdot;\theta\_{q,n}):\mathcal{D}\_{\phi}\to\mathbb{R} be an FNN of the form ([3.1](#S3.E1 "Equation 3.1 ‣ Definition 3.1 (Feedforward neural network). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), where
θq,n\theta\_{q,n} denotes its trainable parameter vector. To enforce the state-dependent interval constraint
q​(t,w)∈𝒵q​(w)q(t,w)\in\mathcal{Z}\_{q}(w) from ([2.3](#S2.E3 "Equation 2.3 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), we use the customized output map

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψq​(w,z):=qmin+range​(w)​σ​(z),range​(w):=max⁡(min⁡(qmax,w)−qmin, 0),\psi\_{q}(w,z):=q\_{\min}+\mathrm{range}(w)\,\sigma(z),\quad\mathrm{range}(w):=\max\!\big(\min(q\_{\max},w)-q\_{\min},\,0\big), |  | (3.2) |

where σ​(z):=(1+e−z)−1\sigma(z):=(1+e^{-z})^{-1} is the sigmoid function.
The resulting pre-decision network is

|  |  |  |  |
| --- | --- | --- | --- |
|  | q^​(t,w;θq,n):=ψq​(w,z~​(t,w;θq,n)).\widehat{q}(t,w;\theta\_{q,n}):=\psi\_{q}\!\big(w,\widetilde{z}(t,w;\theta\_{q,n})\big). |  | (3.3) |

By construction, q^​(t,w;θq,n)∈𝒵q​(w)\widehat{q}(t,w;\theta\_{q,n})\in\mathcal{Z}\_{q}(w) for all (t,w)∈𝒟ϕ(t,w)\in\mathcal{D}\_{\phi}.

The next theorem records a probabilistic approximation result for q^\widehat{q} at a random feature input.

###### Theorem 3.4.

Let X=(t,w)X=(t,w) be a 𝒟ϕ\mathcal{D}\_{\phi}-valued random variable. Then there exists a sequence of networks
{q^​(⋅;θq,n∗)}n∈ℕ\{\widehat{q}(\cdot;\theta\_{q,n}^{\ast})\}\_{n\in\mathbb{N}}
such that, for all ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | limn→∞ℙ​(|q^​(X;θq,n∗)−q∗​(X)|>ε)=0,\lim\_{n\to\infty}\mathbb{P}\!\left(\left|\widehat{q}(X;\theta\_{q,n}^{\ast})-q^{\ast}(X)\right|>\varepsilon\right)=0, |  |

where q∗q^{\ast} is any admissible target map (in particular, the optimal pre-decision control).

A full detail proof of Theorem [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") is given in Appendix [C](#A3 "Appendix C Proof of Theorem 3.4 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

### 3.3 Post-decision network

Let p~​(⋅;θp,n):𝒟ϕ→ℝda\widetilde{p}(\cdot;\theta\_{p,n}):\mathcal{D}\_{\phi}\to\mathbb{R}^{d\_{a}} be an FNN of the form ([3.1](#S3.E1 "Equation 3.1 ‣ Definition 3.1 (Feedforward neural network). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
To enforce the simplex constraint ([2.4](#S2.E4 "Equation 2.4 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), we apply the softmax map ψp=(ψpi)i=1da\psi\_{p}=(\psi\_{p}^{i})\_{i=1}^{d\_{a}},
defined componentwise by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψpi​(z):=ezi∑j=1daezj,z∈ℝda,i=1,…,da.\psi\_{p}^{i}(z):=\frac{e^{z\_{i}}}{\sum\_{j=1}^{d\_{a}}e^{z\_{j}}},\qquad z\in\mathbb{R}^{d\_{a}},\ i=1,\ldots,d\_{a}. |  | (3.4) |

The resulting post-decision network is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^​(t,w;θp,n):=ψp​(p~​(t,w;θp,n)).\widehat{p}(t,w;\theta\_{p,n}):=\psi\_{p}\!\left(\widetilde{p}(t,w;\theta\_{p,n})\right). |  | (3.5) |

By construction, p^​(t,w;θp,n)∈𝒵p\widehat{p}(t,w;\theta\_{p,n})\in\mathcal{Z}\_{p} for all (t,w)∈𝒟ϕ(t,w)\in\mathcal{D}\_{\phi}.

###### Theorem 3.5.

Let XX be a 𝒟ϕ\mathcal{D}\_{\phi}-valued random variable. Then there exists a sequence of networks
{p^​(⋅;θp,n∗)}n∈ℕ\{\widehat{p}(\cdot;\theta\_{p,n}^{\ast})\}\_{n\in\mathbb{N}}
such that, for all ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | limn→∞ℙ​(‖p^​(X;θp,n∗)−p∗​(X)‖>ε)=0,\lim\_{n\to\infty}\mathbb{P}\!\left(\big\|\widehat{p}(X;\theta\_{p,n}^{\ast})-p^{\ast}(X)\big\|>\varepsilon\right)=0, |  |

where p∗p^{\ast} is any admissible target map (in particular, the optimal post-decision control).

A full detail proof of Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") is given in Appendix [D](#A4 "Appendix D Proof of Theorem 3.5 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

### 3.4 NN-parametrized objective

For a fixed architecture index nn, corresponding to hidden-layer width ν(n)\nu^{(n)}, we introduce the
NN parametrization of control pairs

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫^​(Θn):=(q^​(⋅;θq,n),p^​(⋅;θp,n)),whereΘn:=(θq,n,θp,n)∈ℝϑ(n).\widehat{\mathcal{P}}(\Theta\_{n}):=\left(\widehat{q}(\cdot;\theta\_{q,n}),\widehat{p}(\cdot;\theta\_{p,n})\right),\quad\text{where}\quad\Theta\_{n}:=(\theta\_{q,n},\theta\_{p,n})\in\mathbb{R}^{\vartheta^{(n)}}. |  | (3.6) |

Here, q^​(⋅)\widehat{q}(\cdot) and p^​(⋅)\widehat{p}(\cdot) are defined in ([3.3](#S3.E3 "Equation 3.3 ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) and ([3.5](#S3.E5 "Equation 3.5 ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), respectively. The total number of parameters
is ϑ(n):=ηq(n)+ηp(n)\vartheta^{(n)}:=\eta\_{q}^{(n)}+\eta\_{p}^{(n)},
where ηq(n)\eta\_{q}^{(n)} and ηp(n)\eta\_{p}^{(n)} denote the numbers of trainable parameters in the withdrawal and allocation networks, respectively.
Let 𝒢^n\widehat{\mathcal{G}}\_{n} be the resulting class of
NN control pairs, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢^n:={𝒫^​(Θn):Θn∈ℝϑ(n)}.\widehat{\mathcal{G}}\_{n}:=\left\{\widehat{\mathcal{P}}(\Theta\_{n}):\Theta\_{n}\in\mathbb{R}^{\vartheta^{(n)}}\right\}. |  | (3.7) |

Given Θn\Theta\_{n} and YY, let {W​(tm−;Θn,Y),W​(tm+;Θn,Y)}m=0M\{W(t\_{m}^{-};\Theta\_{n},Y),W(t\_{m}^{+};\Theta\_{n},Y)\}\_{m=0}^{M}
be the state sequence induced by applying 𝒫^​(Θn)\widehat{\mathcal{P}}(\Theta\_{n}) in the recursion
([2.8](#S2.E8 "Equation 2.8 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))–([2.9](#S2.E9 "Equation 2.9 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), i.e. with qq and pp replaced by q^\widehat{q} and p^\widehat{p}.
Define the corresponding performance vector

|  |  |  |
| --- | --- | --- |
|  | S​(Θn,Y):=S​(𝒫^​(Θn),Y)S(\Theta\_{n},Y):=S(\widehat{\mathcal{P}}(\Theta\_{n}),Y) |  |

as in ([2.10](#S2.E10 "Equation 2.10 ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")). For moment dependence, define also

|  |  |  |  |
| --- | --- | --- | --- |
|  | S¯​(Θn):=𝔼𝒫^​(Θn)w0,t0−​[Ψ​(S​(Θn,Y))]∈ℝdΨ,\bar{S}(\Theta\_{n}):=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\widehat{\mathcal{P}}(\Theta\_{n})}\!\big[\,\Psi(S(\Theta\_{n},Y))\,\big]\in\mathbb{R}^{d\_{\Psi}}, |  | (3.8) |

as in ([2.12](#S2.E12 "Equation 2.12 ‣ 2.4.2 Risk ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) (and if dΨ=0d\_{\Psi}=0, suppress S¯\bar{S} and Ψ\Psi).

Replacing 𝒫\mathcal{P} by 𝒫^​(Θn)\widehat{\mathcal{P}}(\Theta\_{n}) in ([2.14](#S2.E14 "Equation 2.14 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) yields the NN objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | VN​N(w0,t0−;ξ,Θn):=𝔼𝒫^​(Θn)w0,t0−[ℋ(ξ,S(Θn,Y),S¯(Θn))],V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n}):=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\widehat{\mathcal{P}}(\Theta\_{n})}\!\big[\mathcal{H}\big(\xi,S(\Theta\_{n},Y),\bar{S}(\Theta\_{n})\big)\big], |  | (3.9) |

and the associated NN value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | VN​N​(w0,t0−):=supΘn∈ℝϑ(n),ξ∈ΞVN​N​(w0,t0−;ξ,Θn).V\_{NN}(w\_{0},t\_{0}^{-}):=\sup\_{\Theta\_{n}\in\mathbb{R}^{\vartheta^{(n)}},\ \xi\in\Xi}V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n}). |  | (3.10) |

Since the constraints are enforced by the output maps ([3.2](#S3.E2 "Equation 3.2 ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) and ([3.4](#S3.E4 "Equation 3.4 ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), the optimization in
([3.10](#S3.E10 "Equation 3.10 ‣ 3.4 NN-parametrized objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) is unconstrained over the parameter space.

### 3.5 Empirical objective

In computation, expectations are approximated by sample averaging over i.i.d. realizations of the exogenous input process.
Let Y(1),…,Y(K)Y^{(1)},\ldots,Y^{(K)} be i.i.d. copies of YY,
where, for each k∈{1,…,K}k\in\{1,\ldots,K\},
Y(k)={Ym(k)}m=1MY^{(k)}=\{Y\_{m}^{(k)}\}\_{m=1}^{M}, is a full exogenous path.
We define the dataset

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒴K={Y(k):k=1,…,K}.\mathcal{Y}\_{K}=\{Y^{(k)}:\ k=1,\ldots,K\}. |  | (3.11) |

For each kk, let S(k)​(Θn):=S​(Θn,Y(k))S^{(k)}(\Theta\_{n}):=S(\Theta\_{n},Y^{(k)}) denote the realized performance vector. We estimate S¯\bar{S} by the sample average

|  |  |  |  |
| --- | --- | --- | --- |
|  | S¯^K​(Θn):=1K​∑k=1KΨ​(S(k)​(Θn))∈ℝdΨ.\widehat{\bar{S}}\_{K}(\Theta\_{n}):=\frac{1}{K}\sum\_{k=1}^{K}\Psi\!\left(S^{(k)}(\Theta\_{n})\right)\in\mathbb{R}^{d\_{\Psi}}. |  | (3.12) |

The empirical objective is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^N​N​(w0,t0−;ξ,Θn,𝒴K)\displaystyle\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K}) | :=1K​∑k=1Kℋ​(ξ,S(k)​(Θn),S¯^K​(Θn)),\displaystyle:=\frac{1}{K}\sum\_{k=1}^{K}\mathcal{H}\!\left(\xi,\ S^{(k)}(\Theta\_{n}),\ \widehat{\bar{S}}\_{K}(\Theta\_{n})\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1K​∑k=1K(ℛ​(S(k)​(Θn))+γ​ℒ​(ξ,S(k)​(Θn),S¯^K​(Θn))),\displaystyle=\frac{1}{K}\sum\_{k=1}^{K}\Big(\mathcal{R}\!\left(S^{(k)}(\Theta\_{n})\right)+\gamma\,\mathcal{L}\!\left(\xi,\ S^{(k)}(\Theta\_{n}),\ \widehat{\bar{S}}\_{K}(\Theta\_{n})\right)\Big), |  | (3.13) |

and the corresponding empirical value function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^N​N​(w0,t0−;𝒴K):=supΘn∈ℝϑ(n),ξ∈ΞV^N​N​(w0,t0−;ξ,Θn,𝒴K).\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}):=\sup\_{\Theta\_{n}\in\mathbb{R}^{\vartheta^{(n)}},\ \xi\in\Xi}\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K}). |  | (3.14) |

###### Remark 3.6 (Training algorithm).

In the convergence analysis below, we assume that the chosen training algorithm attains a global optimizer of
([3.14](#S3.E14 "Equation 3.14 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")). In practice, gradient-based methods may converge only to stationary points; we adopt this standing assumption to focus on approximation and estimation errors rather than optimization error.

## 4 Convergence analysis

This section analyzes how NN parametrization of the optimal two-step feedback control propagate through the controlled recursion and into the generalized risk–reward objective.
Throughout, we work under Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"). Let (𝒫∗,ξ∗)∈𝒢×Ξ(\mathcal{P}^{\ast},\xi^{\ast})\in\mathcal{G}\times\Xi be an optimizer as in
Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R3), where 𝒫∗=(q∗,p∗)\mathcal{P}^{\ast}=(q^{\ast},p^{\ast}).
For each architecture index nn, let
Θn∗=(θq,n∗,θp,n∗)\Theta\_{n}^{\ast}=(\theta\_{q,n}^{\ast},\theta\_{p,n}^{\ast})
denote NN parameters producing a pre-decision action network q^​(⋅;θq,n∗)\widehat{q}(\cdot;\theta\_{q,n}^{\ast}) and a post-decision action network p^​(⋅;θp,n∗)\widehat{p}(\cdot;\theta\_{p,n}^{\ast}) that approximate the optimal controls q∗q^{\ast} and p∗p^{\ast} in probability at random feature inputs, as provided by Theorems [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")–[3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

We adopt the shorthand

|  |  |  |  |
| --- | --- | --- | --- |
|  | W∗​(tm±):=W​(tm±;𝒫∗,Y),W(n)​(tm±):=W​(tm±;Θn∗,Y),W^{\ast}(t\_{m}^{\pm}):=W(t\_{m}^{\pm};\mathcal{P}^{\ast},Y),\qquad W^{(n)}(t\_{m}^{\pm}):=W(t\_{m}^{\pm};\Theta\_{n}^{\ast},Y), |  | (4.1) |

for the optimal and NN-induced state variables at intervention times.

### 4.1 Convergence of optimal actions

Lemmas [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") and [4.2](#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")
below show that, at decision times, if the NN-induced state process converges to the optimal controlled state process, then the corresponding NN actions converge to the optimal actions.

###### Lemma 4.1.

Suppose Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") holds.
Let {q^​(⋅;θq,n∗)}n∈ℕ\{\widehat{q}(\cdot;\theta\_{q,n}^{\ast})\}\_{n\in\mathbb{N}} be the pre-decision action network sequence from
Theorem [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"). Fix m∈{0,1,…,M}m\in\{0,1,\ldots,M\}.
If

|  |  |  |
| --- | --- | --- |
|  | W(n)​(tm−)→𝑃W∗​(tm−)as ​n→∞,W^{(n)}(t\_{m}^{-})\xrightarrow{P}W^{\ast}(t\_{m}^{-})\qquad\text{as }n\to\infty, |  |

then

|  |  |  |
| --- | --- | --- |
|  | q^​(tm−,W(n)​(tm−);θq,n∗)→𝑃q∗​(tm−,W∗​(tm−))as ​n→∞.\widehat{q}\big(t\_{m}^{-},\,W^{(n)}(t\_{m}^{-});\theta\_{q,n}^{\ast}\big)\xrightarrow{P}q^{\ast}\!\left(t\_{m}^{-},\,W^{\ast}(t\_{m}^{-})\right)\qquad\text{as }n\to\infty. |  |

###### Proof of Lemma [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

Fix mm and write Wm(n):=W(n)​(tm−)W\_{m}^{(n)}:=W^{(n)}(t\_{m}^{-}) and Wm∗:=W∗​(tm−)W\_{m}^{\ast}:=W^{\ast}(t\_{m}^{-}).
By the triangle inequality,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |q^​(tm−,Wm(n);θq,n∗)−q∗​(tm−,Wm∗)|\displaystyle\big|\widehat{q}(t\_{m}^{-},W\_{m}^{(n)};\theta\_{q,n}^{\ast})-q^{\ast}(t\_{m}^{-},W\_{m}^{\ast})\big| | ≤|q^​(tm−,Wm(n);θq,n∗)−q∗​(tm−,Wm(n))|\displaystyle\leq\big|\widehat{q}(t\_{m}^{-},W\_{m}^{(n)};\theta\_{q,n}^{\ast})-q^{\ast}(t\_{m}^{-},W\_{m}^{(n)})\big| |  | (4.2) |
|  |  | +|q∗​(tm−,Wm(n))−q∗​(tm−,Wm∗)|.\displaystyle\qquad+\big|q^{\ast}(t\_{m}^{-},W\_{m}^{(n)})-q^{\ast}(t\_{m}^{-},W\_{m}^{\ast})\big|. |  |

By Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R4),
ℙ​(Wm∗∈Dq,m)=0\mathbb{P}(W\_{m}^{\ast}\in D\_{q,m})=0, i.e. w↦q∗​(tm−,w)w\mapsto q^{\ast}(t\_{m}^{-},w) is continuous at Wm∗W\_{m}^{\ast} almost surely.
Since Wm(n)→𝑃Wm∗W\_{m}^{(n)}\xrightarrow{P}W\_{m}^{\ast} by assumption, the extended continuous mapping theorem yields
q∗​(tm−,Wm(n))→𝑃q∗​(tm−,Wm∗)q^{\ast}(t\_{m}^{-},W\_{m}^{(n)})\xrightarrow{P}q^{\ast}(t\_{m}^{-},W\_{m}^{\ast}).
So the second term on the rhs of ([4.2](#S4.E2 "Equation 4.2 ‣ Proof of Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) vanishes in probability.

For the first term on the rhs, we handle the nn-dependent input as follows.
Let μm\mu\_{m} denote the law of Wm∗W\_{m}^{\ast} under ℙ\mathbb{P}. Since μm​(Dq,m)=0\mu\_{m}(D\_{q,m})=0, by outer regularity of μm\mu\_{m}
there exist open sets {Uj}j∈ℕ\{U\_{j}\}\_{j\in\mathbb{N}} such that

|  |  |  |
| --- | --- | --- |
|  | Dq,m⊂Uj,μm​(Uj)<1j,μm​(∂Uj)=0.D\_{q,m}\subset U\_{j},\qquad\mu\_{m}(U\_{j})<\frac{1}{j},\qquad\mu\_{m}(\partial U\_{j})=0. |  |

Set Kj:=[wmin,wmax]∖UjK\_{j}:=[w\_{\min},w\_{\max}]\setminus U\_{j}, which is compact. By construction Kj∩Dq,m=∅K\_{j}\cap D\_{q,m}=\emptyset,
hence w↦q∗​(tm−,w)w\mapsto q^{\ast}(t\_{m}^{-},w) is continuous on KjK\_{j}.

Fix j∈ℕj\in\mathbb{N}. By a deterministic universal approximation theorem in the
sup\sup norm [[8](#bib.bib8)],
we may choose the approximation sequence in Theorem [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supw∈Kj|q^​(tm−,w;θq,n∗)−q∗​(tm−,w)|⟶ 0as ​n→∞.\sup\_{w\in K\_{j}}\big|\widehat{q}(t\_{m}^{-},w;\theta\_{q,n}^{\ast})-q^{\ast}(t\_{m}^{-},w)\big|\;\longrightarrow\;0\qquad\text{as }n\to\infty. |  | (4.3) |

In particular, for any ε>0\varepsilon>0 there exists n​(ε,j)n(\varepsilon,j) such that for all n≥n​(ε,j)n\geq n(\varepsilon,j),

|  |  |  |
| --- | --- | --- |
|  | supw∈Kj|q^​(tm−,w;θq,n∗)−q∗​(tm−,w)|≤ε.\sup\_{w\in K\_{j}}\big|\widehat{q}(t\_{m}^{-},w;\theta\_{q,n}^{\ast})-q^{\ast}(t\_{m}^{-},w)\big|\leq\varepsilon. |  |

Hence, for such nn, using that Wm(n)∈[wmin,wmax]W\_{m}^{(n)}\in[w\_{\min},w\_{\max}] a.s. by Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R1),

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|q^​(tm−,Wm(n);θq,n∗)−q∗​(tm−,Wm(n))|>ε)≤ℙ​(Wm(n)∈Uj).\mathbb{P}\!\left(\big|\widehat{q}(t\_{m}^{-},W\_{m}^{(n)};\theta\_{q,n}^{\ast})-q^{\ast}(t\_{m}^{-},W\_{m}^{(n)})\big|>\varepsilon\right)\leq\mathbb{P}\!\left(W\_{m}^{(n)}\in U\_{j}\right). |  |

Since Wm(n)→𝑃Wm∗W\_{m}^{(n)}\xrightarrow{P}W\_{m}^{\ast} implies Wm(n)⇒Wm∗W\_{m}^{(n)}\Rightarrow W\_{m}^{\ast} and μm​(∂Uj)=0\mu\_{m}(\partial U\_{j})=0,
the Portmanteau theorem [[5](#bib.bib5)][Sec. 2] yields

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Wm(n)∈Uj)⟶μm​(Uj)<1j.\mathbb{P}(W\_{m}^{(n)}\in U\_{j})\longrightarrow\mu\_{m}(U\_{j})<\frac{1}{j}. |  |

Letting n→∞n\to\infty and then j→∞j\to\infty shows that the first term in ([4.2](#S4.E2 "Equation 4.2 ‣ Proof of Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) also vanishes in probability.
Combining both terms yields the claim.
∎

###### Lemma 4.2.

Suppose Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") holds.
Let {p^​(⋅;θp,n∗)}n∈ℕ\{\widehat{p}(\cdot;\theta\_{p,n}^{\ast})\}\_{n\in\mathbb{N}}
be the post-decision action network sequence identified in Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").
Fix m∈{0,1,…,M−1}m\in\{0,1,\ldots,M-1\}.
If

|  |  |  |
| --- | --- | --- |
|  | W(n)​(tm+)→𝑃W∗​(tm+)as ​n→∞,W^{(n)}(t\_{m}^{+})\xrightarrow{P}W^{\ast}(t\_{m}^{+})\qquad\text{as }n\to\infty, |  |

then

|  |  |  |
| --- | --- | --- |
|  | p^​(tm+,W(n)​(tm+);θp,n∗)→𝑃p∗​(tm+,W∗​(tm+))as ​n→∞.\widehat{p}\!\left(t\_{m}^{+},\,W^{(n)}(t\_{m}^{+});\theta\_{p,n}^{\ast}\right)\xrightarrow{P}p^{\ast}\!\left(t\_{m}^{+},\,W^{\ast}(t\_{m}^{+})\right)\qquad\text{as }n\to\infty. |  |

###### Proof of Lemma [4.2](#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

The proof follows the same argument as Lemma [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), with Dq,mD\_{q,m} replaced by Dp,mD\_{p,m} and |⋅||\cdot| replaced by ∥⋅∥\|\cdot\|.
∎

### 4.2 Convergence of the controlled state sequence

We now show that, when the optimal feedback controls (q∗,p∗)(q^{\ast},p^{\ast}) are approximated by the NNs from Theorems [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")–[3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), the induced controlled state sequence converges in probability to the optimal state sequence at all intervention times.

###### Lemma 4.3.

Suppose Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") holds.
Let
{q^​(⋅;θq,n∗)}n∈ℕ\{\widehat{q}(\cdot;\theta\_{q,n}^{\ast})\}\_{n\in\mathbb{N}} and
{p^​(⋅;θp,n∗)}n∈ℕ\{\widehat{p}(\cdot;\theta\_{p,n}^{\ast})\}\_{n\in\mathbb{N}}
be the NN sequences identified in Theorems [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") and [3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").
Recalling the notational convention ([4.1](#S4.E1 "Equation 4.1 ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), the NN-induced controlled state satisfies

|  |  |  |
| --- | --- | --- |
|  | W(n)​(tm±)→𝑃W∗​(tm±),as ​n→∞,m=0,…,M,W^{(n)}(t\_{m}^{\pm})~\xrightarrow{P}~W^{\ast}(t\_{m}^{\pm}),\quad\text{as }n\to\infty,\qquad m=0,\ldots,M, |  |

where tM+=T+t\_{M}^{+}=T^{+} and W​(T+;⋅,Y)W(T^{+};\cdot,Y) denotes the terminal post-decision state.

###### Proof of Lemma [4.3](#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Convergence of the controlled state sequence ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

We prove the claim by induction on m=0,1,…,M−1m=0,1,\ldots,M-1.

*Base case (m=0m=0).*
This is trivial. By construction,
W(n)​(t0−)=W​(t0−;Θn∗,Y)=w0=W​(t0−;𝒫∗,Y)=W∗​(t0−)W^{(n)}(t\_{0}^{-})=W(t\_{0}^{-};\Theta\_{n}^{\ast},Y)=w\_{0}=W(t\_{0}^{-};\mathcal{P}^{\ast},Y)=W^{\ast}(t\_{0}^{-}).

*Induction step.*
Fix m∈{0,…,M−1}m\in\{0,\ldots,M-1\} and assume that

|  |  |  |
| --- | --- | --- |
|  | W(n)​(tm−)→𝑃W∗​(tm−),as ​n→∞.W^{(n)}(t\_{m}^{-})\xrightarrow{P}W^{\ast}(t\_{m}^{-}),\quad\text{as }n\to\infty. |  |

By Lemma [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"),

|  |  |  |
| --- | --- | --- |
|  | q^​(tm−,W(n)​(tm−);θq,n∗)→𝑃q∗​(tm−,W∗​(tm−)).\widehat{q}\!\left(t\_{m}^{-},W^{(n)}(t\_{m}^{-});\theta\_{q,n}^{\ast}\right)~\xrightarrow{P}~q^{\ast}\!\left(t\_{m}^{-},W^{\ast}(t\_{m}^{-})\right). |  |

Using the pre-decision update ([2.8](#S2.E8 "Equation 2.8 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | W(n)​(tm+)\displaystyle W^{(n)}(t\_{m}^{+}) | =Uq​(tm,W(n)​(tm−),q^​(tm−,W(n)​(tm−);θq,n∗)),\displaystyle=U\_{q}\Big(t\_{m},\;W^{(n)}(t\_{m}^{-}),\;\widehat{q}\!\left(t\_{m}^{-},W^{(n)}(t\_{m}^{-});\theta\_{q,n}^{\ast}\right)\Big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | W∗​(tm+)\displaystyle W^{\ast}(t\_{m}^{+}) | =Uq​(tm,W∗​(tm−),q∗​(tm−,W∗​(tm−))).\displaystyle=U\_{q}\Big(t\_{m},\;W^{\ast}(t\_{m}^{-}),\;q^{\ast}\!\left(t\_{m}^{-},W^{\ast}(t\_{m}^{-})\right)\Big). |  |

By Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R2), UqU\_{q} is continuous on the relevant bounded domain, hence the continuous mapping theorem yields

|  |  |  |
| --- | --- | --- |
|  | W(n)​(tm+)→𝑃W∗​(tm+).W^{(n)}(t\_{m}^{+})\xrightarrow{P}W^{\ast}(t\_{m}^{+}). |  |

Next, by Lemma [4.2](#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"),

|  |  |  |
| --- | --- | --- |
|  | p^​(tm+,W(n)​(tm+);θp,n∗)→𝑃p∗​(tm+,W∗​(tm+)).\widehat{p}\!\left(t\_{m}^{+},W^{(n)}(t\_{m}^{+});\theta\_{p,n}^{\ast}\right)~\xrightarrow{P}~p^{\ast}\!\left(t\_{m}^{+},W^{\ast}(t\_{m}^{+})\right). |  |

Using the post-decision evolution update ([2.9](#S2.E9 "Equation 2.9 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | W(n)​(tm+1−)\displaystyle W^{(n)}(t\_{m+1}^{-}) | =Up​(tm,W(n)​(tm+),p^​(tm+,W(n)​(tm+);θp,n∗),Ym+1),\displaystyle=U\_{p}\Big(t\_{m},\;W^{(n)}(t\_{m}^{+}),\;\widehat{p}\!\left(t\_{m}^{+},W^{(n)}(t\_{m}^{+});\theta\_{p,n}^{\ast}\right),\;Y\_{m+1}\Big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | W∗​(tm+1−)\displaystyle W^{\ast}(t\_{m+1}^{-}) | =Up​(tm,W∗​(tm+),p∗​(tm+,W∗​(tm+)),Ym+1).\displaystyle=U\_{p}\Big(t\_{m},\;W^{\ast}(t\_{m}^{+}),\;p^{\ast}\!\left(t\_{m}^{+},W^{\ast}(t\_{m}^{+})\right),\;Y\_{m+1}\Big). |  |

Again by continuity of UpU\_{p} on bounded sets Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R2), the continuous mapping theorem (applied jointly with Ym+1Y\_{m+1}, which does not depend on nn) implies

|  |  |  |
| --- | --- | --- |
|  | W(n)​(tm+1−)→𝑃W∗​(tm+1−).W^{(n)}(t\_{m+1}^{-})\xrightarrow{P}W^{\ast}(t\_{m+1}^{-}). |  |

This completes the induction. Finally, applying Lemma [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") at m=Mm=M and the update ([2.8](#S2.E8 "Equation 2.8 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) yields

|  |  |  |
| --- | --- | --- |
|  | W(n)​(T+)=W(n)​(tM+)→𝑃W∗​(tM+)=W∗​(T+),W^{(n)}(T^{+})=W^{(n)}(t\_{M}^{+})\xrightarrow{P}W^{\ast}(t\_{M}^{+})=W^{\ast}(T^{+}), |  |

which completes the proof.
∎

### 4.3 Convergence of performance vector and objective function

We next show that, for any fixed auxiliary variable value ξ\xi,
the scalarized objective evaluated under the NN approximations of the optimal control converges to the objective under the optimal control. This uses:
(i) convergence of the NN-induced controlled recursion (Lemma [4.3](#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Convergence of the controlled state sequence ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")),
(ii) finiteness of the performance vector S​(𝒫,Y)S(\mathcal{P},Y),
(iii) continuity/boundedness of the scalarized criterion function ℋ\mathcal{H} on the relevant bounded domain (Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R7)).

###### Lemma 4.4.

Suppose Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") holds.
Let
{q^​(⋅;θq,n∗)}n∈ℕ\{\widehat{q}(\cdot;\theta\_{q,n}^{\ast})\}\_{n\in\mathbb{N}} and
{p^​(⋅;θp,n∗)}n∈ℕ\{\widehat{p}(\cdot;\theta\_{p,n}^{\ast})\}\_{n\in\mathbb{N}}
be the NN sequences identified in Theorems [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") and [3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").
Then, for any fixed ξ∈Ξ\xi\in\Xi,

|  |  |  |
| --- | --- | --- |
|  | limn→∞VN​N​(w0,t0−;ξ,Θn∗)=V​(w0,t0−;ξ,𝒫∗),\lim\_{n\to\infty}V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n}^{\ast})=V(w\_{0},t\_{0}^{-};\xi,\mathcal{P}^{\ast}), |  |

where VV is the objective ([2.14](#S2.E14 "Equation 2.14 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) and VN​NV\_{NN} is its NN-parametrized counterpart ([3.9](#S3.E9 "Equation 3.9 ‣ 3.4 NN-parametrized objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

For a proof of Lemma [4.4](#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.3 Convergence of performance vector and objective function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"),
see Appendix [E](#A5 "Appendix E Proof of Lemma 4.4 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

### 4.4 Convergence of value function

For each architecture index n∈ℕn\in\mathbb{N}, we make the dependence
of the NN-parametrized value function on the network class explicit by writing

|  |  |  |  |
| --- | --- | --- | --- |
|  | VN​N(n)​(w0,t0−):=supΘn∈ℝϑ(n),ξ∈ΞVN​N​(w0,t0−;ξ,Θn),V\_{NN}^{(n)}(w\_{0},t\_{0}^{-}):=\sup\_{\Theta\_{n}\in\mathbb{R}^{\vartheta^{(n)}},\ \xi\in\Xi}V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n}), |  | (4.4) |

where VN​N​(w0,t0−;ξ,Θn)V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n}) is defined in ([3.9](#S3.E9 "Equation 3.9 ‣ 3.4 NN-parametrized objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
We recall its empirical counterpart (based on an i.i.d. dataset 𝒴K={Y(k)}k=1K\mathcal{Y}\_{K}=\{Y^{(k)}\}\_{k=1}^{K}) given in ([3.14](#S3.E14 "Equation 3.14 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))

|  |  |  |
| --- | --- | --- |
|  | V^N​N​(w0,t0−;𝒴K):=supΘn∈ℝϑ(n),ξ∈ΞV^N​N​(w0,t0−;ξ,Θn,𝒴K),\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}):=\sup\_{\Theta\_{n}\in\mathbb{R}^{\vartheta^{(n)}},\ \xi\in\Xi}\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K}), |  |

where V^N​N​(w0,t0−;ξ,Θn,𝒴K)\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K}) is defined in ([3.13](#S3.E13 "Equation 3.13 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

The total error admits the decomposition

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |V^N​N​(w0,t0−;𝒴K)−V​(w0,t0−)|\displaystyle\big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K})-V(w\_{0},t\_{0}^{-})\big| | ≤|V^N​N​(w0,t0−;𝒴K)−VN​N(n)​(w0,t0−)|\displaystyle\leq\big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K})-V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})\big| |  | (4.5) |
|  |  | +|VN​N(n)​(w0,t0−)−V​(w0,t0−)|.\displaystyle\qquad+\big|V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})-V(w\_{0},t\_{0}^{-})\big|. |  |

The first term is the *estimation error* (sample average vs. expectation), and the second term is the *approximation error* (restriction to the NN control class).

#### 4.4.1 Vanishing approximation error

###### Theorem 4.5.

Under Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), we have

|  |  |  |
| --- | --- | --- |
|  | limn→∞|VN​N(n)​(w0,t0−)−V​(w0,t0−)|=0.\lim\_{n\to\infty}\Big|V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})-V(w\_{0},t\_{0}^{-})\Big|=0. |  |

###### Proof of Theorem [4.5](#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.4.1 Vanishing approximation error ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

For each nn, the constraint-enforcing output maps ensure that every NN control pair is admissible, hence the NN control class satisfies
𝒢^n⊆𝒢\widehat{\mathcal{G}}\_{n}\subseteq\mathcal{G}.
Therefore, VN​N(n)​(w0,t0−)=…V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})=\ldots

|  |  |  |
| --- | --- | --- |
|  | …=supΘn,ξ∈ΞV​(w0,t0−;ξ,𝒫^​(Θn))≤sup𝒫∈𝒢,ξ∈ΞV​(w0,t0−;ξ,𝒫)=V​(w0,t0−),\displaystyle\ldots=\sup\_{\Theta\_{n},\ \xi\in\Xi}V(w\_{0},t\_{0}^{-};\xi,\widehat{\mathcal{P}}(\Theta\_{n}))\leq\sup\_{\mathcal{P}\in\mathcal{G},\ \xi\in\Xi}V(w\_{0},t\_{0}^{-};\xi,\mathcal{P})=V(w\_{0},t\_{0}^{-}), |  |

so lim supn→∞VN​N(n)≤V\limsup\_{n\to\infty}V\_{NN}^{(n)}\leq V.

Let (𝒫∗,ξ∗)(\mathcal{P}^{\ast},\xi^{\ast}) be an optimizer from Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R3), and let Θn∗\Theta\_{n}^{\ast} be the NN parameter sequence identified above.
Since VN​N(n)V\_{NN}^{(n)} is a supremum over (Θn,ξ)(\Theta\_{n},\xi),

|  |  |  |
| --- | --- | --- |
|  | VN​N(n)​(w0,t0−)≥VN​N​(w0,t0−;ξ∗,Θn∗).V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})\geq V\_{NN}(w\_{0},t\_{0}^{-};\xi^{\ast},\Theta\_{n}^{\ast}). |  |

By Lemma [4.4](#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.3 Convergence of performance vector and objective function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (with ξ=ξ∗\xi=\xi^{\ast}),

|  |  |  |
| --- | --- | --- |
|  | VN​N​(w0,t0−;ξ∗,Θn∗)→V​(w0,t0−;ξ∗,𝒫∗)=V​(w0,t0−),V\_{NN}(w\_{0},t\_{0}^{-};\xi^{\ast},\Theta\_{n}^{\ast})\to V(w\_{0},t\_{0}^{-};\xi^{\ast},\mathcal{P}^{\ast})=V(w\_{0},t\_{0}^{-}), |  |

hence lim infn→∞VN​N(n)≥V\liminf\_{n\to\infty}V\_{NN}^{(n)}\geq V. Combining limsup and liminf yields the claim.
∎

#### 4.4.2 Vanishing estimation error for fixed architecture

Fix nn and let Y(1),…,Y(K)Y^{(1)},\ldots,Y^{(K)} be i.i.d. copies of YY, with dataset
𝒴K={Y(k):k=1,…,K}\mathcal{Y}\_{K}=\{Y^{(k)}:\ k=1,\ldots,K\}. The next lemma is a uniform law of large numbers (ULLN) for the empirical objective, including the case where the objective depends on the population moment S¯​(Θn)\bar{S}(\Theta\_{n}) through the sample-average estimator S¯^K​(Θn)\widehat{\bar{S}}\_{K}(\Theta\_{n}).

###### Lemma 4.6 (Uniform law of large numbers for the NN objective).

Suppose Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") holds.
Fix n∈ℕn\in\mathbb{N}.
Then

|  |  |  |
| --- | --- | --- |
|  | supΘn∈ℝϑ(n),ξ∈Ξ|V^N​N​(w0,t0−;ξ,Θn,𝒴K)−VN​N​(w0,t0−;ξ,Θn)|→𝑃0,as ​K→∞.\sup\_{\Theta\_{n}\in\mathbb{R}^{\vartheta^{(n)}},\ \xi\in\Xi}\big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K})-V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n})\big|~\xrightarrow{P}~0,\quad\text{as }K\to\infty. |  |

For a proof of Lemma [4.6](#S4.Thmtheorem6 "Lemma 4.6 (Uniform law of large numbers for the NN objective). ‣ 4.4.2 Vanishing estimation error for fixed architecture ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), see Appendix [F](#A6 "Appendix F Proof of Lemma 4.6 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

###### Theorem 4.7.

Fix n∈ℕn\in\mathbb{N}.
Under the conditions of Lemma [4.6](#S4.Thmtheorem6 "Lemma 4.6 (Uniform law of large numbers for the NN objective). ‣ 4.4.2 Vanishing estimation error for fixed architecture ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"),

|  |  |  |
| --- | --- | --- |
|  | |V^N​N​(w0,t0−;𝒴K)−VN​N(n)​(w0,t0−)|→𝑃0,as ​K→∞.\Big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K})-V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})\Big|~\xrightarrow{P}~0,\qquad\text{as }K\to\infty. |  |

###### Proof of Theorem [4.7](#S4.Thmtheorem7 "Theorem 4.7. ‣ 4.4.2 Vanishing estimation error for fixed architecture ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

Using the inequality |supf−supg|≤sup|f−g|\big|\sup f-\sup g\big|\leq\sup|f-g|, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |V^N​N(w0,t0−;𝒴K)\displaystyle\big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}) | −VN​N(n)(w0,t0−)|\displaystyle-V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})\big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supΘn,ξ∈Ξ|V^N​N​(w0,t0−;ξ,Θn,𝒴K)−VN​N​(w0,t0−;ξ,Θn)|.\displaystyle\quad\leq\sup\_{\Theta\_{n},\ \xi\in\Xi}\big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K})-V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n})\big|. |  |

The right-hand side converges to 0 in probability by Lemma [4.6](#S4.Thmtheorem6 "Lemma 4.6 (Uniform law of large numbers for the NN objective). ‣ 4.4.2 Vanishing estimation error for fixed architecture ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").
∎

#### 4.4.3 Consistency of the two-step approximation

We now state the main convergence result in the next theorem.

###### Theorem 4.8.

Suppose Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") holds and Lemma [4.6](#S4.Thmtheorem6 "Lemma 4.6 (Uniform law of large numbers for the NN objective). ‣ 4.4.2 Vanishing estimation error for fixed architecture ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") holds for each fixed nn.
Then the empirical NN value function is consistent for the true value function in the following sense:
for every ε>0\varepsilon>0 and δ>0\delta>0, there exists n¯∈ℕ\bar{n}\in\mathbb{N} such that for every n≥n¯n\geq\bar{n}
there exists K0​(n)∈ℕK\_{0}(n)\in\mathbb{N} with

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|V^N​N​(w0,t0−;𝒴K)−V​(w0,t0−)|>ε)<δ,∀K≥K0​(n).\mathbb{P}\!\left(\Big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K})-V(w\_{0},t\_{0}^{-})\Big|>\varepsilon\right)<\delta,\qquad\forall\,K\geq K\_{0}(n). |  |

###### Proof of Theorem [4.8](#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.4.3 Consistency of the two-step approximation ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

Fix ε>0\varepsilon>0 and δ>0\delta>0. By Theorem [4.5](#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.4.1 Vanishing approximation error ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), there exists n¯\bar{n} such that

|  |  |  |
| --- | --- | --- |
|  | |VN​N(n)​(w0,t0−)−V​(w0,t0−)|≤ε/2for all ​n≥n¯.\big|V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})-V(w\_{0},t\_{0}^{-})\big|\leq\varepsilon/2\qquad\text{for all }n\geq\bar{n}. |  |

Fix any such nn. By Theorem [4.7](#S4.Thmtheorem7 "Theorem 4.7. ‣ 4.4.2 Vanishing estimation error for fixed architecture ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), there exists K0​(n)K\_{0}(n) such that for all K≥K0​(n)K\geq K\_{0}(n),

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|V^N​N​(w0,t0−;𝒴K)−VN​N(n)​(w0,t0−)|>ε/2)<δ.\mathbb{P}\!\left(\Big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K})-V\_{NN}^{(n)}(w\_{0},t\_{0}^{-})\Big|>\varepsilon/2\right)<\delta. |  |

Using ([4.5](#S4.E5 "Equation 4.5 ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) then yields

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|V^N​N​(w0,t0−;𝒴K)−V​(w0,t0−)|>ε)<δ,∀K≥K0​(n),\mathbb{P}\!\left(\Big|\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K})-V(w\_{0},t\_{0}^{-})\Big|>\varepsilon\right)<\delta,\qquad\forall\,K\geq K\_{0}(n), |  |

which proves the claim.
∎

## 5 Numerical experiments

This section illustrates the convergence-in-probability results of Section [4](#S4 "4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") on a representative discrete-intervention risk–reward control problem.
Numerically, we study value-function convergence by
(i) increasing NN capacity (architecture index nn, hence enriching the NN policy class 𝒢^n\widehat{\mathcal{G}}\_{n} in ([3.7](#S3.E7 "Equation 3.7 ‣ 3.4 NN-parametrized objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))) at a fixed, large training sample size KK, and (ii) increasing the training sample size KK at a fixed, sufficiently rich NN architecture nn.

### 5.1 A decumulation optimization problem

We illustrate the full convergence pipeline using a stylized Defined Contribution (DC) retirement decumulation setting. This example is included only as an application-level illustration with interpretable interventions and controls; the analysis is not specific to finance.

##### Intervention times.

We take yearly intervention times tm=mt\_{m}=m, m=0,…,Mm=0,\ldots,M, with M=30M=30 (so Δ​t=1\Delta t=1 year). For this illustration, we abstract from mortality risk by working conditional on the retiree being alive through the fixed horizon TT,
consistent with the practitioner “plan-to-live, not to die” convention (see, e.g. [[21](#bib.bib21)]).

##### State and exogenous input process.

To obtain a concrete, nontrivial input law while keeping the state dimension low enough to compute a high-accuracy reference value via a grid-based method, we set da=2d\_{a}=2 and consider two investable assets: a risky asset and a risk-free asset.

In this setting, the scalar controlled state is the inflation-adjusted portfolio balance (i.e. the “wealth” process) {W​(t)}0≤t≤T\{W(t)\}\_{0\leq t\leq T}.
Between intervention times, the post-decision update ([2.9](#S2.E9 "Equation 2.9 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))
propagates the wealth process using a one-period gross return vector Ym+1Y\_{m+1},
m=0,…,M−1m=0,\ldots,M-1. Accordingly, Ym+1∈ℝ2Y\_{m+1}\in\mathbb{R}^{2} represents the (inflation-adjusted) gross returns of the risky and risk-free assets over the interval [tm+,tm+1−][t\_{m}^{+},t\_{m+1}^{-}] and is observed at time tm+1−t\_{m+1}^{-}.

We model Ym+1Y\_{m+1} using unit-investment (growth) processes.
Let {GtS}t∈[0,T]\{G^{S}\_{t}\}\_{t\in[0,T]} and {GtB}t∈[0,T]\{G^{B}\_{t}\}\_{t\in[0,T]} denote the inflation-adjusted values of one unit of currency invested in the risky and risk-free assets, respectively, normalized by G0S=G0B=1G^{S}\_{0}=G^{B}\_{0}=1.
Between intervention times t∈[tm+,tm+1−]t\in[t\_{m}^{+},t\_{m+1}^{-}], the risky growth process follows a one-factor Kou jump–diffusion [[17](#bib.bib17)]
and the risk-free growth process has deterministic accumulation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​GtSGt−S=(μ−λ​κ)​d​t+σ​d​Zt+d​(∑i=1πt(χi−1)),d​GtB=rf​GtB​d​t.\frac{dG^{S}\_{t}}{G^{S}\_{t^{-}}}=(\mu-\lambda\kappa)\,dt+\sigma\,dZ\_{t}+d\Big(\sum\_{i=1}^{\pi\_{t}}(\chi\_{i}-1)\Big),\qquad dG^{B}\_{t}=r\_{f}\,G^{B}\_{t}\,dt. |  | (5.1) |

Here, {Zt}\{Z\_{t}\} is Brownian motion, {πt}\{\pi\_{t}\} is a Poisson process with constant intensity λ>0\lambda>0, the jump multipliers {χi}\{\chi\_{i}\} are i.i.d., κ=𝔼​[χ−1]\kappa=\mathbb{E}[\chi-1], and {Zt}\{Z\_{t}\}, {πt}\{\pi\_{t}\}, and {χi}\{\chi\_{i}\} are mutually independent; in the Kou specification, log⁡(χ)\log(\chi) has an asymmetric double-exponential law [[17](#bib.bib17)]. We then define

|  |  |  |
| --- | --- | --- |
|  | Ym+1=(Gtm+1−S/Gtm+S,Gtm+1−B/Gtm+B),m=0,…,M−1,Y\_{m+1}=\left(G^{S}\_{t\_{m+1}^{-}}/G^{S}\_{t\_{m}^{+}},\;G^{B}\_{t\_{m+1}^{-}}/G^{B}\_{t\_{m}^{+}}\right),\qquad m=0,\ldots,M-1, |  |

and let Y={Ym}m=1MY=\{Y\_{m}\}\_{m=1}^{M}. Calibration of ([5.1](#S5.E1 "Equation 5.1 ‣ State and exogenous input process. ‣ 5.1 A decumulation optimization problem ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) is discussed in Subsection [5.2](#S5.SS2 "5.2 Calibration ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

##### Admissible two-step controls.

At each time tmt\_{m}, the control is a two-step feedback policy 𝒫=(q,p)\mathcal{P}=(q,p): given the current wealth level, the retiree first (i) chooses a withdrawal q​(tm−,W​(tm−;⋅))q(t\_{m}^{-},W(t\_{m}^{-};\cdot)) at tm−t\_{m}^{-} for m=0,…,Mm=0,\ldots,M, producing post-withdrawal wealth W​(tm+;⋅)W(t\_{m}^{+};\cdot), and then (ii) chooses portfolio weights p​(tm+,W​(tm+;⋅))p(t\_{m}^{+},W(t\_{m}^{+};\cdot)) at tm+t\_{m}^{+} for m=0,…,M−1m=0,\ldots,M-1;
no allocation occurs at tM+t\_{M}^{+}.
Withdrawals satisfy the state-dependent constraint q​(t,w)∈𝒵q​(w)q(t,w)\in\mathcal{Z}\_{q}(w) from ([2.3](#S2.E3 "Equation 2.3 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), and allocations satisfy the simplex constraint p​(t,w)∈𝒵pp(t,w)\in\mathcal{Z}\_{p} from ([2.4](#S2.E4 "Equation 2.4 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

##### Controlled recursion.

We use the recursion ([2.8](#S2.E8 "Equation 2.8 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))–([2.9](#S2.E9 "Equation 2.9 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) with the updates map

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uq​(t,w,q)=w−q,andUp​(t,w,p,y)={w​⟨p,y⟩,if ​w>0,w​y2,if ​w≤0,U\_{q}(t,w,q)=w-q,\quad\text{and}\quad U\_{p}(t,w,p,y)=\begin{cases}w\,\langle p,y\rangle,&\text{if }w>0,\\ w\,y\_{2},&\text{if }w\leq 0,\end{cases} |  | (5.2) |

where y2y\_{2} denotes the risk-free gross return component of y=(y1,y2)∈ℝ2y=(y\_{1},y\_{2})\in\mathbb{R}^{2}.
Thus, with qm​(⋅):=q​(tm−,W​(tm−))q\_{m}(\cdot):=q(t\_{m}^{-},W(t\_{m}^{-})) and
pm​(⋅):=p​(tm+,W​(tm+))p\_{m}(\cdot):=p(t\_{m}^{+},W(t\_{m}^{+})), we have, for m=0,…,M−1m=0,\ldots,M-1,

|  |  |  |
| --- | --- | --- |
|  | W​(tm+)=W​(tm−)−qm​(⋅),W​(tm+1−)={W​(tm+)​⟨pm​(⋅),Ym+1⟩,if ​W​(tm+)>0,W​(tm+)​Ym+1(2),if ​W​(tm+)≤0.W(t\_{m}^{+})=W(t\_{m}^{-})-q\_{m}(\cdot),\qquad W(t\_{m+1}^{-})=\begin{cases}W(t\_{m}^{+})\,\big\langle p\_{m}(\cdot),\,Y\_{m+1}\big\rangle,&\text{if }W(t\_{m}^{+})>0,\\[2.0pt] W(t\_{m}^{+})\,Y\_{m+1}^{(2)},&\text{if }W(t\_{m}^{+})\leq 0.\end{cases} |  |

The treatment of W​(tm+)≤0W(t\_{m}^{+})\leq 0 reflects liquidation at depletion, a practical constraint in DC decumulation plans: if withdrawals render wealth negative, allocation is halted and the wealth process thereafter follows deterministic debt accrual at the risk-free rate. The resulting recursion is piecewise-defined but continuous, consistent with the regime-switching structure in Subsection [2.6](#S2.SS6 "2.6 Discussion of Assumption 2.1 ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R2).

##### Performance vector.

We take a performance vector to be

|  |  |  |
| --- | --- | --- |
|  | S​(𝒫,Y):=((q​(tm−,W​(tm−;𝒫,Y)))m=0M,W​(T+;𝒫,Y))∈ℝM+2.S(\mathcal{P},Y):=\Big(\big(q(t\_{m}^{-},W(t\_{m}^{-};\mathcal{P},Y))\big)\_{m=0}^{M},\ \ W(T^{+};\mathcal{P},Y)\Big)\in\mathbb{R}^{M+2}. |  |

##### Reward (expected cumulative withdrawal).

Using ([2.11](#S2.E11 "Equation 2.11 ‣ 2.4.1 Reward ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), we set

|  |  |  |
| --- | --- | --- |
|  | ℛ​(S​(𝒫,Y)):=∑m=0Mq​(tm−,W​(tm−;𝒫,Y)).\mathcal{R}\big(S(\mathcal{P},Y)\big):=\sum\_{m=0}^{M}q\!\left(t\_{m}^{-},W(t\_{m}^{-};\mathcal{P},Y)\right). |  |

##### Risk (CVaR of terminal wealth).

Using the template ([2.13](#S2.E13 "Equation 2.13 ‣ 2.4.2 Risk ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) with dΨ=0d\_{\Psi}=0,
we take α=0.05\alpha=0.05 and represent CVaRα​(W​(T+))\mathrm{CVaR}\_{\alpha}(W(T^{+})) via the Rockafellar–Uryasev form [[25](#bib.bib25)]:

|  |  |  |
| --- | --- | --- |
|  | ℒ​(ξ,s):=ξ+1α​min⁡{sM+1−ξ, 0},(ξ,s)∈Ξ×ℝM+2,\mathcal{L}(\xi,s):=\xi+\frac{1}{\alpha}\min\{\,s\_{M+1}-\xi,\,0\},\qquad(\xi,s)\in\Xi\times\mathbb{R}^{M+2}, |  |

where sM+1s\_{M+1} denotes the terminal-wealth component of s=(s0,…,sM+1)s=(s\_{0},\ldots,s\_{M+1}). Then

|  |  |  |
| --- | --- | --- |
|  | 𝒥ℒ​(w0,t0−;𝒫)=supξ∈Ξ𝔼𝒫w0,t0−​[ℒ​(ξ,S​(𝒫,Y))]=CVaRα​(W​(T+))(gain-based convention).\mathcal{J}\_{\mathcal{L}}(w\_{0},t\_{0}^{-};\mathcal{P})=\sup\_{\xi\in\Xi}\,\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\left[\mathcal{L}\big(\xi,S(\mathcal{P},Y)\big)\right]=\mathrm{CVaR}\_{\alpha}\!\big(W(T^{+})\big)\quad\text{(gain-based convention)}. |  |

##### Scalarized objective.

The scalarized criterion function ([2.14](#S2.E14 "Equation 2.14 ‣ 2.4.3 Scalarized risk–reward objective ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) becomes

|  |  |  |
| --- | --- | --- |
|  | ℋ(ξ,s):=ℛ(s)+γℒ(ξ,s),γ>0.\mathcal{H}(\xi,s):=\mathcal{R}(s)+\gamma\,\mathcal{L}(\xi,s),\qquad\gamma>0. |  |

The objective and value function are then

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(w0,t0−;ξ,𝒫)=𝔼𝒫w0,t0−​[ℋ​(ξ,S​(𝒫,Y))],V​(w0,t0−)=sup𝒫∈𝒢,ξ∈ΞV​(w0,t0−;ξ,𝒫).V(w\_{0},t\_{0}^{-};\xi,\mathcal{P})=\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}\!\big[\mathcal{H}\big(\xi,S(\mathcal{P},Y)\big)\big],\quad V(w\_{0},t\_{0}^{-})\!=\!\!\!\sup\_{\mathcal{P}\in\mathcal{G},\ \xi\in\Xi}V(w\_{0},t\_{0}^{-};\xi,\mathcal{P}). |  | (5.3) |

We emphasize that the mean–CVaR objective is not dynamically separable in general; accordingly, the computed NN policy is interpreted as a pre-commitment solution (optimized at t0−t\_{0}^{-} and then implemented via fixed feedback maps thereafter).

### 5.2 Calibration

We follow the calibration approach described in [[9](#bib.bib9), [29](#bib.bib29)] using long-horizon Australian data.
The risky-asset inputs are based on monthly total returns of the ASX All Ordinaries Index (1935:01–2024:06), obtained from Bloomberg and supplemented with historical dividend-yield data where necessary [[20](#bib.bib20)].
The risk-free rate is proxied by Australian 10-year government bond yields (Bloomberg), extended with historical sources to align horizons [[7](#bib.bib7)].
All series are converted to real (inflation-adjusted) terms using CPI data from the Australian Bureau of Statistics.
The resulting annualized parameter values used in our experiments are reported in Table [5.1](#S5.T1 "Table 5.1 ‣ 5.2 Calibration ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

Table 5.1: Calibrated parameters (annualized, inflation adjusted).

| μ\mu | σ\sigma | λ\lambda | pu​pp\_{up} | η1\eta\_{1} | η2\eta\_{2} | rfr\_{f} |
| --- | --- | --- | --- | --- | --- | --- |
| 0.0774 | 0.1202 | 0.3243 | 0.3793 | 7.7209 | 5.9989 | 0.0126 |

Given these parameters, we generate i.i.d. scenario paths Y(1),…,Y(K)Y^{(1)},\ldots,Y^{(K)} by Monte Carlo (MC) simulation of ([5.1](#S5.E1 "Equation 5.1 ‣ State and exogenous input process. ‣ 5.1 A decumulation optimization problem ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) and set 𝒴K={Y(k)}k=1K\mathcal{Y}\_{K}=\{Y^{(k)}\}\_{k=1}^{K} as in ([3.11](#S3.E11 "Equation 3.11 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

### 5.3 Retirement scenario

The retirement scenario is summarized in Table [5.2](#S5.T2 "Table 5.2 ‣ 5.3 Retirement scenario ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"). The retiree selects annual withdrawals qm​(⋅)∈[qmin,qmax]q\_{m}(\cdot)\in[q\_{\min},q\_{\max}], as in ([2.3](#S2.E3 "Equation 2.3 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), and portfolio weights satisfy the simplex constraint ([2.4](#S2.E4 "Equation 2.4 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
Economically, qmaxq\_{\max} may be interpreted as a desired annual real spending level, while qminq\_{\min} is a contingency floor adopted to mitigate depletion risk; the state-dependent constraint ([2.3](#S2.E3 "Equation 2.3 ‣ 2.3 State, admissible controls, and controlled dynamics ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) then permits reductions toward qminq\_{\min} in adverse wealth states while preserving higher withdrawals when the account remains well funded.

Table 5.2: Retirement scenario. Monetary units are in thousands of real
dollar.

|  |  |
| --- | --- |
| Retiree | 65-year-old Australian male |
| Investment horizon TT | 3030 years |
| Initial wealth w0w\_{0} | 10001000 |
| Intervention times | tm=mt\_{m}=m, m=0,1,…,30m=0,1,\ldots,30 |
| Annual withdrawal range | [qmin,qmax]=[35,60]\left[q\_{\min},q\_{\max}\right]=\left[35,60\right] |
| Withdrawal decision times | m=0,1,…,30m=0,1,\ldots,30 (at tm−t\_{m}^{-}) |
| Allocation decision times | m=0,1,…,29m=0,1,\ldots,29 (at tm+t\_{m}^{+}) |
| CVaR confidence level | α=0.05\alpha=0.05 |
| Scalarization parameter | γ=1.0\gamma=1.0 |

### 5.4 Reference value

To assess numerical accuracy, we compare the NN-based empirical optimum
V^N​N​(w0,t0−;𝒴K)\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}) in ([3.14](#S3.E14 "Equation 3.14 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) against a
high-accuracy grid-based reference approximation VrefV\_{\mathrm{ref}}, computed for the same model ([5.1](#S5.E1 "Equation 5.1 ‣ State and exogenous input process. ‣ 5.1 A decumulation optimization problem ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))
and risk–reward objective ([5.3](#S5.E3 "Equation 5.3 ‣ Scalarized objective. ‣ 5.1 A decumulation optimization problem ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) using a provably convergent numerical integration method adapted from
[[10](#bib.bib10)] and specialized to include withdrawal controls.

For each fixed ξ\xi, we solve the inner (q,p)(q,p) control problem by backward recursion on a truncated state domain.
One-period conditional expectations are evaluated by a monotone quadrature rule based on a nonnegative series
representation of the 1D Kou transition density (cf. [[10](#bib.bib10)]).
To handle intervention-time maximizations efficiently, we use the fact that admissible controls depend only on (t,total wealth)(t,\text{total wealth}): at each time step, optimal withdrawals and allocations are obtained by discrete search on a 1D wealth grid, rather than by introducing additional 2D control grids at every spatial node. This substantially reduces computational cost.
Finally, we maximize over ξ∈Ξ\xi\in\Xi by a 1D search.

The truncation choices are:
(i) a risky log-domain y∈[log⁡(102)−8,log⁡(102)+8]y\in[\log(10^{2})-8,\ \log(10^{2})+8] with extended quadrature domain y†∈[log⁡(102)−16,log⁡(102)+16]y^{\dagger}\in[\log(10^{2})-16,\ \log(10^{2})+16];
(ii) a risk-free component truncated to b∈[bmin,bmax]=[−5×105, 5×105]b\in[b\_{\min},b\_{\max}]=[-5\times 10^{5},\,5\times 10^{5}];
(iii) a log-wealth grid w′=log⁡(w)∈[wmin′,wmax′]=[−10+log⁡(102), 10+log⁡(102)]w^{\prime}=\log(w)\in[w^{\prime}\_{\min},w^{\prime}\_{\max}]=[-10+\log(10^{2}),\,10+\log(10^{2})] used for the 1D searches when w>0w>0;
(for w≤0w\leq 0 the recursion follows the liquidation/debt convention ([5.2](#S5.E2 "Equation 5.2 ‣ Controlled recursion. ‣ 5.1 A decumulation optimization problem ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")));
and (iv) Ξ=[−5×105, 5×105]\Xi=[-5\times 10^{5},\,5\times 10^{5}].

We report three refinement levels: (Ny×Nb)∈{(512×512),(1024×1024),(2048×2048)}(N\_{y}\times N\_{b})\in\{(512\times 512),(1024\times 1024),(2048\times 2048)\}.
At each refinement level, the intervention-time searches use a wealth grid with Nw=4​NyN\_{w}=4N\_{y} nodes, and the outer ξ\xi-search uses Nξ=NbN\_{\xi}=N\_{b} nodes.
The resulting approximate values at (w0,t0−)=(1000,0−)(w\_{0},t\_{0}^{-})=(1000,0^{-}) are
V(512×512)=1600.08V\_{(512\times 512)}=1600.08, V(1024×1024)=1604.19V\_{(1024\times 1024)}=1604.19, and V(2048×2048)=1605.22V\_{(2048\times 2048)}=1605.22. A convergence table
is presented in Appendix [G](#A7 "Appendix G Convergence table for grid-based method in Subsection 5.4 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").
We take the finest-grid value as

|  |  |  |
| --- | --- | --- |
|  | Vref=1605.22.V\_{\mathrm{ref}}=1605.22. |  |

Note that |Vref−V(1024×1024)||V\_{\mathrm{ref}}-V\_{(1024\times 1024)}| is about 0.06%0.06\% of VrefV\_{\mathrm{ref}}), which indicates that the discretization error is negligible at the scale of the NN errors reported in Subsection [5.6](#S5.SS6 "5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

### 5.5 Training

We parameterize the two-step feedback policy 𝒫=(q,p)\mathcal{P}=(q,p) by the NN class
𝒢^n\widehat{\mathcal{G}}\_{n} defined in ([3.7](#S3.E7 "Equation 3.7 ‣ 3.4 NN-parametrized objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
For a chose architecture index nn and dataset 𝒴K\mathcal{Y}\_{K}, training maximizes the empirical objective ([3.14](#S3.E14 "Equation 3.14 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) jointly over NN parameters and the auxiliary variable ξ\xi.
Each training run initializes (θq,n,θp,n,ξ)(\theta\_{q,n},\theta\_{p,n},\xi) randomly and applies Adam to maximize V^N​N​(w0,t0−;ξ,Θn,𝒴K)\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K}) using minibatches of scenario paths from 𝒴K\mathcal{Y}\_{K}. We use separate learning rates for (θq,n,θp,n)(\theta\_{q,n},\theta\_{p,n}) and for ξ\xi, and a fixed iteration budget, consistent with the empirical objective studied in Section [4](#S4 "4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").
Representative hyperparameters are given in Table [5.3](#S5.T3 "Table 5.3 ‣ 5.5 Training ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

Table 5.3: NN hyper-parameters

|  |  |
| --- | --- |
| Iterations | 50,00050{,}000 |
| Minibatch size | 1,0001{,}000 |
| Initial Adam learning rate (NN parameters) | 0.050.05 |
| Initial Adam learning rate (auxiliary ξ\xi) | 0.040.04 |
| Weight decay (L2 penalty) | 10−410^{-4} |

In these experiments, we do not split 𝒴K\mathcal{Y}\_{K} into separate training and validation/test sets: for each run, 𝒴K\mathcal{Y}\_{K} is exactly the dataset defining the empirical objective ([3.14](#S3.E14 "Equation 3.14 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), and we report the corresponding empirical optimum V^N​N​(w0,t0−;𝒴K)\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}). This matches the objects in the convergence in probability analysis (Theorem [4.8](#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.4.3 Consistency of the two-step approximation ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
Out-of-sample robustness is discussed in Subsection [5.8](#S5.SS8 "5.8 Out-of-sample robustness ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

### 5.6 Convergence

We empirically illustrate convergence in probability by repeating the full training-and-optimization procedure under independent randomization (scenario generation and random network’s parameters initialization) and estimating tail probabilities of the error, in the spirit of Theorem [4.8](#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.4.3 Consistency of the two-step approximation ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").
Fix an experimental setting (architecture index nn and sample size KK) and perform NrunN\_{\mathrm{run}} independent runs, indexed by j=1,…,Nrunj=1,\ldots,N\_{\mathrm{run}}.
In run jj, we train the networks on a dataset 𝒴K(j)\mathcal{Y}\_{K}^{(j)} and record the resulting empirical optimum

|  |  |  |
| --- | --- | --- |
|  | V^n,K(j):=V^N​N​(w0,t0−;𝒴K(j)),\widehat{V}^{(j)}\_{n,K}\;:=\;\widehat{V}\_{NN}\!\left(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}^{(j)}\right), |  |

where V^N​N​(w0,t0−;𝒴K)\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}) is the maximized empirical objective in ([3.14](#S3.E14 "Equation 3.14 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))
(i.e. maximized over ξ∈Ξ\xi\in\Xi and NN parameters in Θn\Theta\_{n})
for the policy class 𝒢^n\widehat{\mathcal{G}}\_{n}.
For a tolerance ε>0\varepsilon>0, we estimate the tail probability
ℙ​(|V^n,K−Vref|>ε​|Vref|)\mathbb{P}\!\left(\left|\widehat{V}\_{n,K}-V\_{\mathrm{ref}}\right|>\varepsilon\,|V\_{\mathrm{ref}}|\right)
by the empirical frequency

|  |  |  |  |
| --- | --- | --- | --- |
|  | pε:=1Nrun​∑j=1Nrun𝟏​{|V^n,K(j)−Vref|>ε​|Vref|}.p\_{\varepsilon}:=\frac{1}{N\_{\mathrm{run}}}\sum\_{j=1}^{N\_{\mathrm{run}}}\mathbf{1}\Big\{\big|\widehat{V}^{(j)}\_{n,K}-V\_{\mathrm{ref}}\big|>\varepsilon\,|V\_{\mathrm{ref}}|\Big\}. |  | (5.4) |

#### 5.6.1 Increasing NN capacity

We first vary NN capacity while keeping the training sample size large, to reduce sampling noise and emphasize approximation effects.
In the notation of Section [4](#S4 "4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), NN capacity is indexed by nn; for each nn we take both networks in the two-step policy class 𝒢^n\widehat{\mathcal{G}}\_{n} to have L(n)L^{(n)} hidden layers and width ν(n)\nu^{(n)} (nodes per hidden layer).
We fix K=2.56×105K=2.56\times 10^{5} and consider

|  |  |  |
| --- | --- | --- |
|  | (L(n),ν(n))∈{(1,2),(1,5),(2,5)}.(L^{(n)},\nu^{(n)})\in\{(1,2),\ (1,5),\ (2,5)\}. |  |

For each capacity level, we fix one dataset 𝒴K\mathcal{Y}\_{K} and run Nrun=100N\_{\mathrm{run}}=100 independent trainings with different random initializations
(so the reported dispersion is conditional on this fixed scenario set).

Figure [1(a)](#S5.F1.sf1 "Figure 1(a) ‣ Figure 5.1 ‣ 5.6.1 Increasing NN capacity ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") summarizes the resulting V^n,K(j)\widehat{V}^{(j)}\_{n,K} across runs, and
Table [5.4](#S5.T4 "Table 5.4 ‣ 5.6.1 Increasing NN capacity ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") reports summary statistics and the empirical tail probabilities ([5.4](#S5.E4 "Equation 5.4 ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")). Key observations are:

* •

  As capacity increases, the distribution shifts toward VrefV\_{\mathrm{ref}} (median/mean increase), consistent with improved approximation within richer classes (cf. Theorem [4.5](#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.4.1 Vanishing approximation error ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
* •

  For fixed ε\varepsilon, the estimated tail probabilities pεp\_{\varepsilon} decrease sharply with capacity (e.g. for ε=1%\varepsilon=1\% from 0.640.64 to 0.020.02), illustrating concentration of the empirical optimum around VrefV\_{\mathrm{ref}} as approximation error decreases.

Table 5.4: Empirical convergence as NN capacity increases (fixed K=2.56×105K=2.56\times 10^{5}, Nrun=100N\_{\mathrm{run}}=100 runs; Vref=1605.22V\_{\mathrm{ref}}=1605.22); pεp\_{\varepsilon} is defined in ([5.4](#S5.E4 "Equation 5.4 ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

| (L(n),ν(n))(L^{(n)},\nu^{(n)}) | Mean (Std) | p0.5%p\_{0.5\%} | p1%p\_{1\%} | p1.5%p\_{1.5\%} | p2%p\_{2\%} | p2.5%p\_{2.5\%} |
| --- | --- | --- | --- | --- | --- | --- |
| (1,2)(1,2) | 1589.32​(5.48)1589.32\ (5.48) | 0.970.97 | 0.640.64 | 0.060.06 | 0.000.00 | 0.000.00 |
| (1,5)(1,5) | 1593.68​(6.07)1593.68\ (6.07) | 0.770.77 | 0.320.32 | 0.000.00 | 0.000.00 | 0.000.00 |
| (2,5)(2,5) | 1602.50​(4.61)1602.50\ (4.61) | 0.060.06 | 0.020.02 | 0.000.00 | 0.000.00 | 0.000.00 |



![Refer to caption](2603.06563v1/figs/boxplot_capacity.png)


(a) Increasing NN capacity (fixed K=2.56×105K=2.56\times 10^{5}).

![Refer to caption](2603.06563v1/figs/boxplot_sample_size.png)


(b) Increasing training sample size (fixed capacity (2,5)(2,5)).

Figure 5.1: Empirical optima V^n,K(j)\widehat{V}^{(j)}\_{n,K} across Nrun=100N\_{\mathrm{run}}=100 runs. Boxes show the interquartile range (25%–75%) with median line; whiskers extend to 1.5×IQR1.5\times\mathrm{IQR} and points beyond are plotted as outliers. The dashed line indicates the reference value Vref=1605.22V\_{\mathrm{ref}}=1605.22.

#### 5.6.2 Increasing training sample size

Next, we fix a sufficiently rich architecture at (L(n⋆),ν(n⋆))=(2,5)(L^{(n^{\star})},\nu^{(n^{\star})})=(2,5) and vary K∈2.56×{103,104,105}K\in 2.56\times\{10^{3},10^{4},10^{5}\} to emphasize estimation effects. For each KK, we perform Nrun=100N\_{\mathrm{run}}=100 independent runs, each with a freshly simulated dataset 𝒴K(j)\mathcal{Y}\_{K}^{(j)} and a fresh random initialization.

Table 5.5: Empirical convergence as training sample size KK increases (fixed capacity (L(n⋆),ν(n⋆))=(2,5)(L^{(n^{\star})},\nu^{(n^{\star})})=(2,5), Nrun=100N\_{\mathrm{run}}=100 runs; Vref=1605.22V\_{\mathrm{ref}}=1605.22); pεp\_{\varepsilon} is defined in ([5.4](#S5.E4 "Equation 5.4 ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

| KK | Mean (Std) | p0.5%p\_{0.5\%} | p1%p\_{1\%} | p1.5%p\_{1.5\%} | p2%p\_{2\%} | p2.5%p\_{2.5\%} |
| --- | --- | --- | --- | --- | --- | --- |
| 2.56×1032.56\times 10^{3} | 1629.41​(18.27)1629.41\ (18.27) | 0.880.88 | 0.670.67 | 0.450.45 | 0.320.32 | 0.200.20 |
| 2.56×1042.56\times 10^{4} | 1609.38​(5.20)1609.38\ (5.20) | 0.210.21 | 0.030.03 | 0.000.00 | 0.000.00 | 0.000.00 |
| 2.56×1052.56\times 10^{5} | 1607.87​(1.58)1607.87\ (1.58) | 0.000.00 | 0.000.00 | 0.000.00 | 0.000.00 | 0.000.00 |

Figure [1(b)](#S5.F1.sf2 "Figure 1(b) ‣ Figure 5.1 ‣ 5.6.1 Increasing NN capacity ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") shows that the dispersion of V^n⋆,K(j)\widehat{V}^{(j)}\_{n^{\star},K} decreases substantially as KK increases.
Table [5.5](#S5.T5 "Table 5.5 ‣ 5.6.2 Increasing training sample size ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") reports the corresponding tail probabilities ([5.4](#S5.E4 "Equation 5.4 ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")). Key observations are:

* •

  As KK increases, the interquartile range and whisker length shrink markedly, and the empirical optima concentrate near VrefV\_{\mathrm{ref}}, consistent with diminishing estimation error (cf. Theorem [4.8](#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.4.3 Consistency of the two-step approximation ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
* •

  The tail probabilities pεp\_{\varepsilon} decrease monotonically with KK (e.g. p1%p\_{1\%} drops from 0.670.67 to 0.000.00), providing a direct empirical proxy for convergence in probability of the empirical optimum.

![Refer to caption](2603.06563v1/figs/PDE_P_heatmap.png)


(a) Allocation policy (grid-based reference)

![Refer to caption](2603.06563v1/figs/NN_P_heatmap.png)


(b) Allocation policy (NN)

![Refer to caption](2603.06563v1/figs/PDE_Q_heatmap.png)


(c) Withdrawal policy (grid-based reference)

![Refer to caption](2603.06563v1/figs/NN_Q_heatmap.png)


(d) Withdrawal policy (NN)

Figure 5.2: Policy heatmap comparison.

### 5.7 Policy structure

To complement the value function convergence results in Subsection [5.6](#S5.SS6 "5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), we compare the learned feedback maps against the grid-based reference policies.
For a representative trained network (capacity (L(n⋆),ν(n⋆))=(2,5)(L^{(n^{\star})},\nu^{(n^{\star})})=(2,5) and K=2.56×105K=2.56\times 10^{5}), we evaluate the NN withdrawal map q​(tm−,w)q(t\_{m}^{-},w) and the risky-asset weight (first component) of the NN allocation map p​(tm+,w)p(t\_{m}^{+},w) over a uniform (t,w)(t,w) plotting grid. We then compare these surfaces to the corresponding grid-based reference policies computed in Subsection [5.4](#S5.SS4 "5.4 Reference value ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization").

![Refer to caption](2603.06563v1/figs/Withdrawal_slice.png)


Figure 5.3: Withdrawal slice at t=15t=15 years.

Figure [5.2](#S5.F2 "Figure 5.2 ‣ 5.6.2 Increasing training sample size ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (Panels (a) and (b)) shows that the NN allocation heatmap closely tracks the reference allocation structure across the relevant wealth region, including along typical realized wealth percentiles. More importantly, the withdrawal maps in Figure [5.2](#S5.F2 "Figure 5.2 ‣ 5.6.2 Increasing training sample size ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (Panels (c) and (d)) exhibit a pronounced quasi–bang–bang pattern: withdrawals concentrate near the bounds qminq\_{\min} and qmaxq\_{\max}, with a narrow transition region along a time-dependent boundary. The NN approximation captures this transition boundary region well, while slightly smoothing the change over a thin band, as expected when a continuous function class approximates a reference map with steep gradients or possible discontinuities.

This qualitative structure is compatible with Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R4): even if the true optimal withdrawal map is not globally continuous in wealth, any nonsmoothness would be concentrated on a lower-dimensional boundary in (t,w)(t,w). In diffusion-with-jumps return models such as ([5.1](#S5.E1 "Equation 5.1 ‣ State and exogenous input process. ‣ 5.1 A decumulation optimization problem ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), the one-period return law admits a density, making it plausible (and assumed in (R4)) that the controlled state hits such boundaries with probability zero at intervention times.
The slice plot in Figure [5.3](#S5.F3 "Figure 5.3 ‣ 5.7 Policy structure ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") provides a 1D view of the same phenomenon at a fixed time. The NN policy closely matches the grid-based threshold structure, with a narrow transition region reflecting approximation of a steep transition in the reference map by a continuous network.333A similar quasi–bang–bang pattern for constrained withdrawal controls has been reported in related numerical studies (see, e.g. [[11](#bib.bib11)]); here our emphasis is on convergence diagnostics for NN-parametrized policies and on out-of-sample robustness.

### 5.8 Out-of-sample robustness

The convergence theorems in Section [4](#S4 "4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") are stated for the empirical optimum
V^N​N​(w0,t0−;𝒴K)\widehat{V}\_{NN}(w\_{0},t\_{0}^{-};\mathcal{Y}\_{K}) (computed on the same dataset entering the empirical objective).
As a robustness check against potential overfitting concerns in finite samples, we also evaluate each trained policy on a single common independent out-of-sample dataset of size Ktest=2.56×106K\_{\mathrm{test}}=2.56\times 10^{6} scenario paths, generated under the same calibrated input law. Concretely, for run jj with trained parameters (ξ(j),θq,n(j),θp,n(j))(\xi^{(j)},\theta^{(j)}\_{q,n},\theta^{(j)}\_{p,n}), we compute an out-of-sample value estimate by plugging the trained optimizer into the sample-average functional on the test set:

|  |  |  |
| --- | --- | --- |
|  | V^n,Ktest(j):=1Ktest​∑k=1Ktestℋ​(ξ(j),S​(𝒫^n(j),Ytest(k))),𝒫^n(j):=(q^n​(⋅;θq,n(j)),p^n​(⋅;θp,n(j))),\widehat{V}^{(j)}\_{n,K\_{\mathrm{test}}}:=\frac{1}{K\_{\mathrm{test}}}\sum\_{k=1}^{K\_{\mathrm{test}}}\mathcal{H}\!\left(\xi^{(j)},\,S\!\left(\widehat{\mathcal{P}}^{(j)}\_{n},Y\_{\mathrm{test}}^{(k)}\right)\right),\qquad\widehat{\mathcal{P}}^{(j)}\_{n}:=\big(\widehat{q}\_{n}(\cdot;\theta^{(j)}\_{q,n}),\widehat{p}\_{n}(\cdot;\theta^{(j)}\_{p,n})\big), |  |

and summarize errors relative to VrefV\_{\mathrm{ref}} in the same way as ([5.4](#S5.E4 "Equation 5.4 ‣ 5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")), i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | pεtest:=1Nrun​∑j=1Nrun𝟏​{|V^n,Ktest(j)−Vref|>ε​|Vref|}.p^{\mathrm{test}}\_{\varepsilon}:=\frac{1}{N\_{\mathrm{run}}}\sum\_{j=1}^{N\_{\mathrm{run}}}\mathbf{1}\Big\{\big|\widehat{V}^{(j)}\_{n,K\_{\mathrm{test}}}-V\_{\mathrm{ref}}\big|>\varepsilon\,|V\_{\mathrm{ref}}|\Big\}. |  | (5.5) |

Because KtestK\_{\mathrm{test}} is large and common across runs, the MC noise in V^n,Ktest(j)\widehat{V}^{(j)}\_{n,K\_{\mathrm{test}}} is small and the cross-run dispersion is dominated by training variability rather than test-set noise.

Table [5.6](#S5.T6 "Table 5.6 ‣ 5.8 Out-of-sample robustness ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") reports out-of-sample results as NN capacity increases (with K=2.56×105K=2.56\times 10^{5} fixed), and Table [5.7](#S5.T7 "Table 5.7 ‣ 5.8 Out-of-sample robustness ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") reports out-of-sample results as KK increases (with capacity fixed at (L(n⋆),ν(n⋆))=(2,5)(L^{(n^{\star})},\nu^{(n^{\star})})=(2,5)). The qualitative conclusions mirror the in-sample convergence results in Subsection [5.6](#S5.SS6 "5.6 Convergence ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"): larger capacity reduces approximation error, and larger KK reduces estimation/training variability, with the out-of-sample tail probabilities rapidly collapsing toward zero at moderate sample sizes.

Table 5.6: Out-of-sample evaluation as NN capacity increases (fixed K=2.56×105K=2.56\times 10^{5}, Ktest=2.56×106K\_{\mathrm{test}}=2.56\times 10^{6}, Nrun=100N\_{\mathrm{run}}=100; Vref=1605.22V\_{\mathrm{ref}}=1605.22); pεtestp^{\mathrm{test}}\_{\varepsilon}
defined in ([5.5](#S5.E5 "Equation 5.5 ‣ 5.8 Out-of-sample robustness ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

| (L(n),ν(n))(L^{(n)},\nu^{(n)}) | Mean (Std) | p0.5%testp^{\mathrm{test}}\_{0.5\%} | p1%testp^{\mathrm{test}}\_{1\%} | p1.5%testp^{\mathrm{test}}\_{1.5\%} | p2%testp^{\mathrm{test}}\_{2\%} | p2.5%testp^{\mathrm{test}}\_{2.5\%} |
| --- | --- | --- | --- | --- | --- | --- |
| (1,2)(1,2) | 1587.50​(5.17)1587.50\ (5.17) | 1.001.00 | 0.650.65 | 0.060.06 | 0.000.00 | 0.000.00 |
| (1,5)(1,5) | 1591.86​(5.81)1591.86\ (5.81) | 0.820.82 | 0.320.32 | 0.000.00 | 0.000.00 | 0.000.00 |
| (2,5)(2,5) | 1600.76​(4.58)1600.76\ (4.58) | 0.280.28 | 0.020.02 | 0.000.00 | 0.000.00 | 0.000.00 |




Table 5.7: Out-of-sample evaluation as training sample size KK increases (fixed capacity (L(n⋆),ν(n⋆))=(2,5)(L^{(n^{\star})},\nu^{(n^{\star})})=(2,5), Ktest=2.56×106K\_{\mathrm{test}}=2.56\times 10^{6}, Nrun=100N\_{\mathrm{run}}=100; Vref=1605.22V\_{\mathrm{ref}}=1605.22); pεtestp^{\mathrm{test}}\_{\varepsilon} is defined in ([5.5](#S5.E5 "Equation 5.5 ‣ 5.8 Out-of-sample robustness ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).

| KK | Mean (Std) | p0.5%testp^{\mathrm{test}}\_{0.5\%} | p1%testp^{\mathrm{test}}\_{1\%} | p1.5%testp^{\mathrm{test}}\_{1.5\%} | p2%testp^{\mathrm{test}}\_{2\%} | p2.5%testp^{\mathrm{test}}\_{2.5\%} |
| --- | --- | --- | --- | --- | --- | --- |
| 2.56×1032.56\times 10^{3} | 1589.35​(7.02)1589.35\ (7.02) | 0.910.91 | 0.370.37 | 0.110.11 | 0.030.03 | 0.020.02 |
| 2.56×1042.56\times 10^{4} | 1604.41​(0.78)1604.41\ (0.78) | 0.000.00 | 0.000.00 | 0.000.00 | 0.000.00 | 0.000.00 |
| 2.56×1052.56\times 10^{5} | 1606.06​(0.23)1606.06\ (0.23) | 0.000.00 | 0.000.00 | 0.000.00 | 0.000.00 | 0.000.00 |

## 6 Conclusion and future work

We developed a neural-network approximation framework for discrete-intervention risk–reward stochastic control with constrained two-step feedback policies, where the optimal feedback maps may be discontinuous in the state.
By combining constraint-enforcing output maps with a moving-input stability argument (based on ℙ\mathbb{P}-null discontinuity sets), we established an end-to-end convergence pipeline: NN approximation of admissible controls propagates through the controlled recursion and a broad class of scalarized risk–reward objectives, and the resulting sample-average training problem converges.
In particular, the empirical optimum converges in probability to the true optimal value as NN capacity and the training sample size increases.
Numerical experiments on a representative decumulation problem corroborate the predicted convergence-in-probability behavior, show excellent agreement between NN and grid-based reference policies (including threshold structure), and indicate robust out-of-sample performance.

Future work includes relaxing bounded-state/compact-domain assumptions, extending the analysis beyond pre-commitment to time-consistent dynamic risk criteria, and studying richer state features and higher-dimensional action spaces.

## Appendix A Proof of Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2 (Composition with (a.s.-continuous) activations). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

By Theorem [3.1](#S3.Thmtheorem1 "Theorem 3.1 (Universal approximation for a random input [13, Thm. 2.4 and Cor. 2.7]). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), we have Fn​(X)→𝑃f​(X)F\_{n}(X)\xrightarrow{P}f(X) as n→∞n\to\infty.
By assumption, ℙ​(f​(X)∈Dψ)=0\mathbb{P}\!\left(f(X)\in D\_{\psi}\right)=0, i.e. ψ\psi is continuous at f​(X)f(X) almost surely.
Hence, by the (extended) continuous mapping theorem [[4](#bib.bib4), [16](#bib.bib16)],
ψ​(Fn​(X))→𝑃ψ​(f​(X))\psi(F\_{n}(X))\xrightarrow{P}\psi(f(X)).

## Appendix B Proof of Lemma [3.3](#S3.Thmtheorem3 "Lemma 3.3 (Boundary approximation via open-range activations). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

Fix δ∈(0,(b−a)/2)\delta\in(0,(b-a)/2) and define
Πδ:[a,b]N→(a,b)N\Pi\_{\delta}:[a,b]^{N}\to(a,b)^{N} by

|  |  |  |
| --- | --- | --- |
|  | (Πδ​(y))j:=min⁡{b−δ,max⁡{a+δ,yj}},j=1,…,N.(\Pi\_{\delta}(y))\_{j}:=\min\{b-\delta,\max\{a+\delta,y\_{j}\}\},\qquad j=1,\ldots,N. |  |

Then Πδ∘g\Pi\_{\delta}\circ g takes values in [a+δ,b−δ]N⊂(a,b)N[a+\delta,b-\delta]^{N}\subset(a,b)^{N} and
Πδ​(g​(X))→g​(X)\Pi\_{\delta}(g(X))\to g(X) a.s. as δ↓0\delta\downarrow 0. Using the measurable right inverse, set
hδ:=ψr−1∘Πδ∘g:ℝν0→ℝNh\_{\delta}:=\psi^{-1}\_{r}\circ\Pi\_{\delta}\circ g:\mathbb{R}^{\nu\_{0}}\to\mathbb{R}^{N},
which is Borel measurable. By Theorem [3.1](#S3.Thmtheorem1 "Theorem 3.1 (Universal approximation for a random input [13, Thm. 2.4 and Cor. 2.7]). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"), for each fixed δ\delta there exists a sequence
{Fn,δ}n∈ℕ\{F\_{n,\delta}\}\_{n\in\mathbb{N}} with Fn,δ∈𝒬nF\_{n,\delta}\in\mathcal{Q}\_{n} such that
Fn,δ​(X)→𝑃hδ​(X)F\_{n,\delta}(X)\xrightarrow{P}h\_{\delta}(X) as n→∞n\to\infty.
By continuity of ψ\psi and the continuous mapping theorem,

|  |  |  |
| --- | --- | --- |
|  | ψ​(Fn,δ​(X))→𝑃ψ​(hδ​(X))=Πδ​(g​(X)),as ​n→∞.\psi\!\left(F\_{n,\delta}(X)\right)\xrightarrow{P}\psi\!\left(h\_{\delta}(X)\right)=\Pi\_{\delta}(g(X)),\qquad\text{as }n\to\infty. |  |

Now choose a deterministic sequence {δj}j∈ℕ\{\delta\_{j}\}\_{j\in\mathbb{N}} with δj↓0\delta\_{j}\downarrow 0.
For each jj, by the above convergence with δ=δj\delta=\delta\_{j}, there exists an index n​(j)n(j) such that for all
n≥n​(j)n\geq n(j),

|  |  |  |
| --- | --- | --- |
|  | ℙ​(‖ψ​(Fn,δj​(X))−Πδj​(g​(X))‖>1j)<1j.\mathbb{P}\!\left(\big\|\psi(F\_{n,\delta\_{j}}(X))-\Pi\_{\delta\_{j}}(g(X))\big\|>\tfrac{1}{j}\right)<\tfrac{1}{j}. |  |

Choose n​(j)n(j) increasing in jj and define j​(n):=max⁡{j:n​(j)≤n}j(n):=\max\{j:\ n(j)\leq n\}, so j​(n)→∞j(n)\to\infty as
n→∞n\to\infty. Set

|  |  |  |
| --- | --- | --- |
|  | Fn:=Fn,δj​(n)∈𝒬n.F\_{n}:=F\_{n,\delta\_{j(n)}}\in\mathcal{Q}\_{n}. |  |

Then ψ​(Fn​(X))−Πδj​(n)​(g​(X))→𝑃0\psi(F\_{n}(X))-\Pi\_{\delta\_{j(n)}}(g(X))\xrightarrow{P}0 as n→∞n\to\infty.
Finally, by the triangle inequality,

|  |  |  |
| --- | --- | --- |
|  | ‖ψ​(Fn​(X))−g​(X)‖≤‖ψ​(Fn​(X))−Πδj​(n)​(g​(X))‖+‖Πδj​(n)​(g​(X))−g​(X)‖.\big\|\psi(F\_{n}(X))-g(X)\big\|\leq\big\|\psi(F\_{n}(X))-\Pi\_{\delta\_{j(n)}}(g(X))\big\|+\big\|\Pi\_{\delta\_{j(n)}}(g(X))-g(X)\big\|. |  |

The first term converges to 0 in probability by construction;
the second converges to 0 a.s. (hence in probability) since δj​(n)↓0\delta\_{j(n)}\downarrow 0.
This completes the proof.

## Appendix C Proof of Theorem [3.4](#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

Recall range​(w)=max⁡(min⁡(qmax,w)−qmin,0)\mathrm{range}(w)=\max(\min(q\_{\max},w)-q\_{\min},0) from ([3.2](#S3.E2 "Equation 3.2 ‣ 3.2 Pre-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")).
Since q∗q^{\ast} is admissible, q∗​(t,w)∈[qmin,qmin+range​(w)]q^{\ast}(t,w)\in[q\_{\min},\,q\_{\min}+\mathrm{range}(w)] for all (t,w)(t,w).
Define the normalized target

|  |  |  |
| --- | --- | --- |
|  | u∗​(t,w):={q∗​(t,w)−qminrange​(w),range​(w)>0,0,range​(w)=0.u^{\ast}(t,w):=\begin{cases}\dfrac{q^{\ast}(t,w)-q\_{\min}}{\mathrm{range}(w)},&\mathrm{range}(w)>0,\\[6.0pt] 0,&\mathrm{range}(w)=0.\end{cases} |  |

Then u∗u^{\ast} is measurable and u∗​(t,w)∈[0,1]u^{\ast}(t,w)\in[0,1].

Apply Lemma [3.3](#S3.Thmtheorem3 "Lemma 3.3 (Boundary approximation via open-range activations). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") with N=1N=1, [a,b]=[0,1][a,b]=[0,1], g:=u∗g:=u^{\ast}, and ψ:=σ\psi:=\sigma.
This yields a sequence of scalar FNN outputs {zn​(⋅)}n∈ℕ\{z\_{n}(\cdot)\}\_{n\in\mathbb{N}} such that
σ​(zn​(X))→𝑃u∗​(X)\sigma(z\_{n}(X))\xrightarrow{P}u^{\ast}(X) as n→∞n\to\infty.
Define

|  |  |  |
| --- | --- | --- |
|  | q^​(t′,w′;θq,n∗):=qmin+range​(w′)​σ​(zn​(t′,w′))≡ψq​(w′,zn​(t′,w′)).\widehat{q}(t^{\prime},w^{\prime};\theta\_{q,n}^{\ast}):=q\_{\min}+\mathrm{range}(w^{\prime})\,\sigma(z\_{n}(t^{\prime},w^{\prime}))\equiv\psi\_{q}\!\big(w^{\prime},z\_{n}(t^{\prime},w^{\prime})\big). |  |

Since (w,u)↦qmin+range​(w)​u(w,u)\mapsto q\_{\min}+\mathrm{range}(w)\,u is continuous and ww is part of the input,
the continuous mapping theorem implies

|  |  |  |
| --- | --- | --- |
|  | q^​(X;θq,n∗)→𝑃qmin+range​(w​(X))​u∗​(X)=q∗​(X),as ​n→∞.\widehat{q}(X;\theta\_{q,n}^{\ast})\xrightarrow{P}q\_{\min}+\mathrm{range}(w(X))\,u^{\ast}(X)=q^{\ast}(X),\qquad\text{as }n\to\infty. |  |

## Appendix D Proof of Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

We first note that p∗​(X)∈𝒵pp^{\ast}(X)\in\mathcal{Z}\_{p}.
For δ>0\delta>0, define the interiorized simplex map Πδ:𝒵p→𝒵p\Pi\_{\delta}:\mathcal{Z}\_{p}\to\mathcal{Z}\_{p} by

|  |  |  |
| --- | --- | --- |
|  | Πδ​(y):=y+δ​𝟏1+da​δ,\Pi\_{\delta}(y):=\frac{y+\delta\mathbf{1}}{1+d\_{a}\delta}, |  |

so that Πδ​(y)∈𝒵p\Pi\_{\delta}(y)\in\mathcal{Z}\_{p} and each component of Πδ​(y)\Pi\_{\delta}(y) is strictly positive.
In particular, Πδ​(p∗​(X))\Pi\_{\delta}(p^{\ast}(X)) lies in the open simplex and
Πδ​(p∗​(X))→p∗​(X)\Pi\_{\delta}(p^{\ast}(X))\to p^{\ast}(X) almost surely as δ↓0\delta\downarrow 0.

On the open simplex, the softmax map ψp\psi\_{p} in ([3.4](#S3.E4 "Equation 3.4 ‣ 3.3 Post-decision network ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")) admits the measurable right inverse

|  |  |  |
| --- | --- | --- |
|  | ψp,r−1​(y):=(log⁡yi)i=1da,y∈𝒵p,yi>0,\psi\_{p,r}^{-1}(y):=(\log y\_{i})\_{i=1}^{d\_{a}},\qquad y\in\mathcal{Z}\_{p},\ y\_{i}>0, |  |

since ∑i=1dayi=1\sum\_{i=1}^{d\_{a}}y\_{i}=1 implies ψp​(log⁡y)=y\psi\_{p}(\log y)=y.
Fix δ>0\delta>0 and define the measurable target

|  |  |  |
| --- | --- | --- |
|  | hδ​(φ):=ψp,r−1​(Πδ​(p∗​(φ)))∈ℝda,φ∈𝒟ϕ.h\_{\delta}(\varphi):=\psi\_{p,r}^{-1}\!\big(\Pi\_{\delta}(p^{\ast}(\varphi))\big)\in\mathbb{R}^{d\_{a}},\qquad\varphi\in\mathcal{D}\_{\phi}. |  |

By Theorem [3.1](#S3.Thmtheorem1 "Theorem 3.1 (Universal approximation for a random input [13, Thm. 2.4 and Cor. 2.7]). ‣ 3.1 Preliminaries ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") there exists a sequence of FNNs
p~n,δ​(⋅)∈𝒬n\widetilde{p}\_{n,\delta}(\cdot)\in\mathcal{Q}\_{n} such that
p~n,δ​(X)→𝑃hδ​(X)\widetilde{p}\_{n,\delta}(X)\xrightarrow{P}h\_{\delta}(X) as n→∞n\to\infty.
Since ψp\psi\_{p} is continuous, the continuous mapping theorem yields

|  |  |  |
| --- | --- | --- |
|  | ψp​(p~n,δ​(X))→𝑃ψp​(hδ​(X))=Πδ​(p∗​(X)),as ​n→∞.\psi\_{p}\!\left(\widetilde{p}\_{n,\delta}(X)\right)\xrightarrow{P}\psi\_{p}\!\left(h\_{\delta}(X)\right)=\Pi\_{\delta}(p^{\ast}(X)),\qquad\text{as }n\to\infty. |  |

To pass to the boundary, fix a deterministic sequence {δj}j∈ℕ\{\delta\_{j}\}\_{j\in\mathbb{N}} with δj↓0\delta\_{j}\downarrow 0.
For each jj, since ψp​(p~n,δj​(X))→𝑃Πδj​(p∗​(X))\psi\_{p}(\widetilde{p}\_{n,\delta\_{j}}(X))\xrightarrow{P}\Pi\_{\delta\_{j}}(p^{\ast}(X)) as n→∞n\to\infty,
we can choose an index n​(j)n(j) such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(‖ψp​(p~n​(j),δj​(X))−Πδj​(p∗​(X))‖>1j)<1j.\mathbb{P}\!\left(\big\|\psi\_{p}(\widetilde{p}\_{n(j),\delta\_{j}}(X))-\Pi\_{\delta\_{j}}(p^{\ast}(X))\big\|>\tfrac{1}{j}\right)<\tfrac{1}{j}. |  |

Define a full sequence {p~n}n∈ℕ\{\widetilde{p}\_{n}\}\_{n\in\mathbb{N}} by setting, for each jj,

|  |  |  |
| --- | --- | --- |
|  | p~n:=p~n​(j),δjfor all ​n​(j)≤n<n​(j+1),\widetilde{p}\_{n}:=\widetilde{p}\_{n(j),\delta\_{j}}\quad\text{for all }n(j)\leq n<n(j+1), |  |

and define p^​(φ;θp,n∗):=ψp​(p~n​(φ))\widehat{p}(\varphi;\theta\_{p,n}^{\ast}):=\psi\_{p}(\widetilde{p}\_{n}(\varphi)).
By nesting, p~n∈𝒬n\widetilde{p}\_{n}\in\mathcal{Q}\_{n} for all nn. Moreover,

|  |  |  |
| --- | --- | --- |
|  | p^​(X;θp,n∗)=ψp​(p~n​(X))→𝑃Πδj​(n)​(p∗​(X)),as ​n→∞,\widehat{p}(X;\theta\_{p,n}^{\ast})=\psi\_{p}(\widetilde{p}\_{n}(X))\xrightarrow{P}\Pi\_{\delta\_{j(n)}}(p^{\ast}(X)),\qquad\text{as }n\to\infty, |  |

with j​(n)→∞j(n)\to\infty.
Finally, since Πδj​(n)​(p∗​(X))→p∗​(X)\Pi\_{\delta\_{j(n)}}(p^{\ast}(X))\to p^{\ast}(X) almost surely (hence in probability),
the triangle inequality yields p^​(X;θp,n∗)→𝑃p∗​(X)\widehat{p}(X;\theta\_{p,n}^{\ast})\xrightarrow{P}p^{\ast}(X).

## Appendix E Proof of Lemma [4.4](#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.3 Convergence of performance vector and objective function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

Write 𝔼​[⋅]\mathbb{E}[\cdot] for 𝔼𝒫w0,t0−​[⋅]\mathbb{E}^{w\_{0},t\_{0}^{-}}\_{\mathcal{P}}[\cdot] when the control is clear from context.
Define the NN-induced and optimal performance vectors

|  |  |  |
| --- | --- | --- |
|  | S(n):=S​(Θn∗,Y),S∗:=S​(𝒫∗,Y).S^{(n)}:=S(\Theta\_{n}^{\ast},Y),\qquad S^{\ast}:=S(\mathcal{P}^{\ast},Y). |  |

Since S​(⋅,Y)S(\cdot,Y) is a finite-dimensional vector built from the intervention-time sequence
  
{W​(tm±),q​(tm−,W​(tm−)),p​(tm+,W​(tm+))}\{W(t\_{m}^{\pm}),q(t\_{m}^{-},W(t\_{m}^{-})),p(t\_{m}^{+},W(t\_{m}^{+}))\},
Lemmas [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 Convergence of optimal actions ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")–[4.3](#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Convergence of the controlled state sequence ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") imply componentwise convergence in probability, hence

|  |  |  |
| --- | --- | --- |
|  | S(n)→𝑃S∗.S^{(n)}\xrightarrow{P}S^{\ast}. |  |

For moment dependence, define

|  |  |  |
| --- | --- | --- |
|  | S¯(n):=𝔼​[Ψ​(S(n))],S¯∗:=𝔼​[Ψ​(S∗)],\bar{S}^{(n)}:=\mathbb{E}\!\left[\Psi(S^{(n)})\right],\qquad\bar{S}^{\ast}:=\mathbb{E}\!\left[\Psi(S^{\ast})\right], |  |

where Ψ\Psi is as in ([2.12](#S2.E12 "Equation 2.12 ‣ 2.4.2 Risk ‣ 2.4 Risk–reward objective ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")). By Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R5), Ψ\Psi is continuous on the compact set 𝒵\mathcal{Z} containing S​(𝒫,Y)S(\mathcal{P},Y) a.s. for all admissible 𝒫\mathcal{P}, hence Ψ\Psi is bounded on 𝒵\mathcal{Z}.
By the continuous mapping theorem, Ψ​(S(n))→𝑃Ψ​(S∗)\Psi(S^{(n)})\xrightarrow{P}\Psi(S^{\ast}), and boundedness implies uniform integrability, hence

|  |  |  |
| --- | --- | --- |
|  | S¯(n)=𝔼​[Ψ​(S(n))]⟶𝔼​[Ψ​(S∗)]=S¯∗.\bar{S}^{(n)}=\mathbb{E}[\Psi(S^{(n)})]\longrightarrow\mathbb{E}[\Psi(S^{\ast})]=\bar{S}^{\ast}. |  |

(If dΨ=0d\_{\Psi}=0, the S¯\bar{S} terms are absent and this step can be ignored.)

Now define the scalarized criterion random variables

|  |  |  |
| --- | --- | --- |
|  | ℋ(n):=ℋ​(ξ,S(n),S¯(n)),ℋ∗:=ℋ​(ξ,S∗,S¯∗).\mathcal{H}^{(n)}:=\mathcal{H}\left(\xi,S^{(n)},\bar{S}^{(n)}\right),\qquad\mathcal{H}^{\ast}:=\mathcal{H}\left(\xi,S^{\ast},\bar{S}^{\ast}\right). |  |

Since (S(n),S¯(n))→𝑃(S∗,S¯∗)(S^{(n)},\bar{S}^{(n)})\xrightarrow{P}(S^{\ast},\bar{S}^{\ast}) and ℋ\mathcal{H} is continuous on
Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}} by Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R7), the continuous mapping theorem yields
ℋ(n)→𝑃ℋ∗\mathcal{H}^{(n)}\xrightarrow{P}\mathcal{H}^{\ast}.
Moreover, by Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R7), the integrand ℋ\mathcal{H} is bounded on Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}}, so {ℋ(n)}n\{\mathcal{H}^{(n)}\}\_{n} is uniformly integrable. Therefore,
𝔼​[ℋ(n)]⟶𝔼​[ℋ∗]\mathbb{E}[\mathcal{H}^{(n)}]\longrightarrow\mathbb{E}[\mathcal{H}^{\ast}],
which is
VN​N​(w0,t0−;ξ,Θn∗)→V​(w0,t0−;ξ,𝒫∗)V\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n}^{\ast})\to V(w\_{0},t\_{0}^{-};\xi,\mathcal{P}^{\ast}).
This concludes the proof.

## Appendix F Proof of Lemma [4.6](#S4.Thmtheorem6 "Lemma 4.6 (Uniform law of large numbers for the NN objective). ‣ 4.4.2 Vanishing estimation error for fixed architecture ‣ 4.4 Convergence of value function ‣ 4 Convergence analysis ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

Write 𝔼​[⋅]\mathbb{E}[\cdot] for expectation under ℙ\mathbb{P} conditional on W​(t0−)=w0W(t\_{0}^{-})=w\_{0}. The dependence on the control parameter Θn\Theta\_{n} enters only through the measurable map Y↦S​(Θn,Y)Y\mapsto S(\Theta\_{n},Y).
Fix nn.
Recall from ([3.8](#S3.E8 "Equation 3.8 ‣ 3.4 NN-parametrized objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))–([3.12](#S3.E12 "Equation 3.12 ‣ 3.5 Empirical objective ‣ 3 A neural network approach ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))

|  |  |  |
| --- | --- | --- |
|  | S¯​(Θn):=𝔼​[Ψ​(S​(Θn,Y))]∈ℝdΨ,\bar{S}(\Theta\_{n}):=\mathbb{E}\!\big[\Psi(S(\Theta\_{n},Y))\big]\in\mathbb{R}^{d\_{\Psi}}, |  |

and its sample-average estimator based on i.i.d. copies Y(1),…,Y(K)Y^{(1)},\ldots,Y^{(K)},

|  |  |  |
| --- | --- | --- |
|  | S¯^K​(Θn):=1K​∑k=1KΨ​(S(k)​(Θn))∈ℝdΨ.\widehat{\bar{S}}\_{K}(\Theta\_{n}):=\frac{1}{K}\sum\_{k=1}^{K}\Psi\!\left(S^{(k)}(\Theta\_{n})\right)\in\mathbb{R}^{d\_{\Psi}}. |  |

We introduce the auxiliary empirical objective which uses
S¯​(Θn)\bar{S}(\Theta\_{n}) instead of S¯^K​(Θn)\widehat{\bar{S}}\_{K}(\Theta\_{n}):

|  |  |  |
| --- | --- | --- |
|  | V~N​N​(w0,t0−;ξ,Θn,𝒴K):=1K​∑k=1Kℋ​(ξ,S(k)​(Θn),S¯​(Θn)).\widetilde{V}\_{NN}(w\_{0},t\_{0}^{-};\xi,\Theta\_{n},\mathcal{Y}\_{K}):=\frac{1}{K}\sum\_{k=1}^{K}\mathcal{H}\!\left(\xi,\ S^{(k)}(\Theta\_{n}),\ \bar{S}(\Theta\_{n})\right). |  |

Then, by the triangle inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supΘn,ξ∈Ξ|V^N​N−VN​N|≤supΘn,ξ∈Ξ|V^N​N−V~N​N|+supΘn,ξ∈Ξ|V~N​N−VN​N|.\sup\_{\Theta\_{n},\xi\in\Xi}\big|\widehat{V}\_{NN}-V\_{NN}\big|\leq\sup\_{\Theta\_{n},\xi\in\Xi}\big|\widehat{V}\_{NN}-\widetilde{V}\_{NN}\big|+\sup\_{\Theta\_{n},\xi\in\Xi}\big|\widetilde{V}\_{NN}-V\_{NN}\big|. |  | (F.1) |

*Step 1: The second term on the rhs of ([F.1](#A6.E1 "Equation F.1 ‣ Appendix F Proof of Lemma 4.6 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))*
For fixed nn, the function class

|  |  |  |
| --- | --- | --- |
|  | {y↦ℋ​(ξ,S​(Θn,y),S¯​(Θn)):(ξ,Θn)∈Ξ×ℝϑ(n)}\Big\{y\mapsto\mathcal{H}\big(\xi,S(\Theta\_{n},y),\bar{S}(\Theta\_{n})\big):\ (\xi,\Theta\_{n})\in\Xi\times\mathbb{R}^{\vartheta^{(n)}}\Big\} |  |

is uniformly bounded by Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1 (Regularity conditions). ‣ 2.5 Standing assumptions for the risk–reward control problem ‣ 2 Problem formulation ‣ Convergence of Neural Network Policies for Risk–Reward Optimization") (R5)/(R7), since S​(Θn,Y)∈𝒵S(\Theta\_{n},Y)\in\mathcal{Z} a.s. for all admissible controls and S¯​(Θn)∈𝒵¯=conv​(Ψ​(𝒵))\bar{S}(\Theta\_{n})\in\bar{\mathcal{Z}}=\mathrm{conv}(\Psi(\mathcal{Z})).
Therefore a suitable ULLN (e.g. [[26](#bib.bib26), Thm. 4.3] for fixed architecture) yields

|  |  |  |
| --- | --- | --- |
|  | supΘn,ξ∈Ξ|V~N​N−VN​N|→𝑃0,as ​K→∞.\sup\_{\Theta\_{n},\xi\in\Xi}\big|\widetilde{V}\_{NN}-V\_{NN}\big|\xrightarrow{P}0,\qquad\text{as }K\to\infty. |  |

*Step 2: The first term on the rhs of ([F.1](#A6.E1 "Equation F.1 ‣ Appendix F Proof of Lemma 4.6 ‣ Convergence of Neural Network Policies for Risk–Reward Optimization"))*
By (R5)/(R7), Ψ​(𝒵)\Psi(\mathcal{Z}) is compact and 𝒵¯=conv​(Ψ​(𝒵))\bar{\mathcal{Z}}=\mathrm{conv}(\Psi(\mathcal{Z})) is compact.
Moreover, S¯^K​(Θn)∈𝒵¯=conv​(Ψ​(𝒵))\widehat{\bar{S}}\_{K}(\Theta\_{n})\in\bar{\mathcal{Z}}=\mathrm{conv}(\Psi(\mathcal{Z})) for every (K,Θn)(K,\Theta\_{n}).
Since ℋ\mathcal{H} is continuous on Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}} and the latter is compact whenever Ξ\Xi is compact
(or more generally if ℋ\mathcal{H} is uniformly continuous on Ξ×𝒵×𝒵¯\Xi\times\mathcal{Z}\times\bar{\mathcal{Z}}), ℋ\mathcal{H} is uniformly continuous in its third argument on this domain. Hence, for any ε>0\varepsilon>0 there exists δ>0\delta>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖s¯−s¯′‖≤δ⟹sup(ξ,s)∈Ξ×𝒵|ℋ​(ξ,s,s¯)−ℋ​(ξ,s,s¯′)|≤ε.\|\bar{s}-\bar{s}^{\prime}\|\leq\delta\quad\Longrightarrow\quad\sup\_{(\xi,s)\in\Xi\times\mathcal{Z}}\big|\mathcal{H}(\xi,s,\bar{s})-\mathcal{H}(\xi,s,\bar{s}^{\prime})\big|\leq\varepsilon. |  |

Therefore, on the event {supΘn‖S¯^K​(Θn)−S¯​(Θn)‖≤δ}\{\sup\_{\Theta\_{n}}\|\widehat{\bar{S}}\_{K}(\Theta\_{n})-\bar{S}(\Theta\_{n})\|\leq\delta\},

|  |  |  |
| --- | --- | --- |
|  | supΘn,ξ∈Ξ|V^N​N−V~N​N|≤ε.\sup\_{\Theta\_{n},\xi\in\Xi}\big|\widehat{V}\_{NN}-\widetilde{V}\_{NN}\big|\leq\varepsilon. |  |

Finally, since Ψ​(S​(Θn,Y))\Psi(S(\Theta\_{n},Y)) is uniformly bounded and the architecture is fixed, a ULLN applied to the class
{y↦Ψ​(S​(Θn,y))}\{y\mapsto\Psi(S(\Theta\_{n},y))\} implies

|  |  |  |
| --- | --- | --- |
|  | supΘn‖S¯^K​(Θn)−S¯​(Θn)‖→𝑃0.\sup\_{\Theta\_{n}}\big\|\widehat{\bar{S}}\_{K}(\Theta\_{n})-\bar{S}(\Theta\_{n})\big\|\xrightarrow{P}0. |  |

Combining the preceding displays yields
supΘn,ξ∈Ξ|V^N​N−V~N​N|→𝑃0\sup\_{\Theta\_{n},\xi\in\Xi}\big|\widehat{V}\_{NN}-\widetilde{V}\_{NN}\big|\xrightarrow{P}0.
Together with Step 1, this proves the claimed ULLN for V^N​N\widehat{V}\_{NN}.

## Appendix G Convergence table for grid-based method in Subsection [5.4](#S5.SS4 "5.4 Reference value ‣ 5 Numerical experiments ‣ Convergence of Neural Network Policies for Risk–Reward Optimization")

Table G.1: Convergence test for EW–CVaR problem with α=0.05\alpha=0.05 and γ=1.0\gamma=1.0.
Grid size denotes the discretization used in the numerical scheme (Ny×Nb)\left(N\_{y}\times N\_{b}\right), where NyN\_{y} is the number of nodes in the risky log-domain and NbN\_{b} is the number of nodes in the risk-free domain;
at each refinement level, the intervention-time searches use a wealth grid with Nw=4​NyN\_{w}=4N\_{y} nodes, and the outer ξ\xi-search uses Nξ=NbN\_{\xi}=N\_{b} nodes.
Units: thousands of dollars (real).

| Grid size | Value function | E​[∑mqm]/(M+1)E\left[\sum\_{m}q\_{m}\right]/\left(M+1\right) | CVaR5%​[WT]\text{CVaR}\_{5\%}\left[W\_{T}\right] | ξ∗\xi^{\ast} |
| --- | --- | --- | --- | --- |
| (512×512)\left(512\times 512\right) | 1600.081600.08 | 50.9650.96 | 20.4120.41 | 128.10128.10 |
| (1024×1024)\left(1024\times 1024\right) | 1604.191604.19 | 50.8050.80 | 29.5229.52 | 129.40129.40 |
| (2048×2048)\left(2048\times 2048\right) | 1605.221605.22 | 50.7650.76 | 31.6031.60 | 129.90129.90 |

## References

* [1]

  H. M. Soner A. M. Reppen and V. Tissot-Daguette.
  Deep stochastic optimization in finance.
  Digital Finance, 5:91–111, 2023.
* [2]

  Asma Bachouch, Charles Huré, Nicolas Langrené, and Huyên Pham.
  Deep neural networks algorithms for stochastic control problems on
  finite horizon: Numerical applications.
  Methodology and Computing in Applied Probability, 24.
* [3]

  Dimitri Bertsekas and Steven E Shreve.
  Stochastic optimal control: the discrete-time case.
  Athena Scientific, 1996.
* [4]

  Patrick Billingsley.
  Probability and Measure.
  John Wiley & Sons, New York, 3rd edition, 1995.
* [5]

  Patrick Billingsley.
  Convergence of Probability Measures.
  Wiley, 2 edition, 1999.
* [6]

  Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [7]

  Matthew Butlin, Robert Dixon, and Peter J. Lloyd.
  Statistical appendix: Selected data series, 1800–2010.
  In Simon Ville and Glenn Withers, editors, The Cambridge
  Economic History of Australia, pages 555–594. Cambridge University Press,
  2014.
* [8]

  George Cybenko.
  Approximation by superpositions of a sigmoidal function.
  Mathematics of Control, Signals and Systems, 2(4):303–314,
  1989.
* [9]

  D.-M. Dang and P.A. Forsyth.
  Better than pre-commitment mean-variance portfolio allocation
  strategies: A semi-self-financing Hamilton-Jacobi-Bellman equation
  approach.
  European Journal of Operational Research, 250(3):827–841,
  2016.
* [10]

  Duy-Minh Dang and Chang Chen.
  Multi-period mean-buffered probability of exceedance in Defined
  Contribution portfolio optimization.
  SIAM Journal on Financial Mathematics, 2026.
  to appear.
* [11]

  Peter A Forsyth.
  A stochastic control approach to defined contribution plan
  decumulation:"The nastiest, hardest problem in finance".
  North American Actuarial Journal, 26(2):227–251, 2022.
* [12]

  Jiequn Han and Weinan E.
  Deep learning approximation for stochastic control problems.
  arXiv preprint arXiv:1611.07422, 2016.
  Deep Reinforcement Learning Workshop, NIPS 2016.
* [13]

  Kurt Hornik, Maxwell Stinchcombe, and Halbert White.
  Multilayer feedforward networks are universal approximators.
  Neural Networks, 2(5):359–366, 1989.
* [14]

  Ruimeng Hu and Mathieu Laurière.
  Recent developments in machine learning methods for stochastic
  control and games.
  Numerical Algebra, Control and Optimization, 14(3):435–525,
  2024.
* [15]

  Côme Huré, Huyên Pham, Achref Bachouch, and Nicolas Langrené.
  Deep neural networks algorithms for stochastic control problems on
  finite horizon: convergence analysis.
  SIAM Journal on Numerical Analysis, 59(1):525–557, 2021.
* [16]

  Olav Kallenberg.
  Foundations of Modern Probability.
  Springer, New York, 2 edition, 2002.
* [17]

  S.G. Kou.
  A jump diffusion model for option pricing.
  Management Science, 48:1086–1101, August 2002.
* [18]

  Y. Li and P.A. Forsyth.
  A data-driven neural network approach to optimal asset allocation for
  target-based defined contribution pension plans.
  Insurance: Mathematics and Economics, 86:189–204, 2019.
* [19]

  A. Mafusalov and S. Uryasev.
  Buffered probability of exceedance: Mathematical properties and
  optimization.
  SIAM Journal on Optimization, 28(2):1077–1103, 2018.
* [20]

  T. Mathews.
  A history of Australian equities.
  Research Discussion Papers rdp2019-04, Reserve Bank of Australia,
  June 2019.
* [21]

  Wade D Pfau.
  An overview of retirement income planning.
  Journal of Financial Counseling and Planning, 29(1):114–120,
  2018.
* [22]

  W Powell.
  A universal framework for sequential decision problems.
  OR/MS Today February. https://tinyurl. com/PowellORMSfeature,
  2023.
* [23]

  A. M. Reppen and H. M. Soner.
  Deep empirical risk minimization in finance: Looking into the future.
  Mathematical Finance, 33(1):116–145, 2023.
* [24]

  R Tyrrell Rockafellar and Roger JB Wets.
  Variational analysis.
  Springer, 1998.
* [25]

  R.T. Rockafellar and S. Uryasev.
  Optimization of conditional value-at-risk.
  Journal of Risk, 2(3):21–41, 2000.
* [26]

  K. H. Tsang and H. Y. Wong.
  Deep-learning solution to portfolio selection with serially dependent
  returns.
  SIAM Journal on Financial Mathematics, 11(2):593–619, 2020.
* [27]

  Pieter M van Staden, Peter A Forsyth, and Yuying Li.
  A global-in-time neural network approach to dynamic portfolio
  optimization.
  Applied Mathematical Finance, 31(3):131–163, 2024.
* [28]

  P.M. Van Staden, D.-M. Dang, and P.A. Forsyth.
  Mean-quadratic variation portfolio optimization: A desirable
  alternative to time-consistent mean-variance optimization?
  SIAM Journal on Financial Mathematics, 10(3):815–856, 2019.
* [29]

  P.M. Van Staden, D.-M. Dang, and P.A. Forsyth.
  The surprising robustness of dynamic mean-variance portfolio
  optimization to model misspecification errors.
  European Journal of Operational Research, 289(2):774–792,
  2021.
* [30]

  X.Y. Zhou and D. Li.
  Continuous time mean variance portfolio selection: A stochastic LQ
  framework.
  Applied Mathematics and Optimization, 42:19–33, 2000.

BETA