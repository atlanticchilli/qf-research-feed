---
authors:
- Christopher Cameron
doc_id: arxiv:2602.19892v1
family_id: arxiv:2602.19892
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit
  Maturity Structure'
url_abs: http://arxiv.org/abs/2602.19892v1
url_html: https://arxiv.org/html/2602.19892v1
venue: arXiv q-fin
version: 1
year: 2026
---


Christopher Cameron
  
christopher.cameron@treasury.gov
The author is with the U.S. Department of the Treasury, Office of Debt Management. The
analysis and
conclusions set forth in this paper are those of the author, and do not necessarily reflect those of or
indicate concurrence by other members of the Treasury staff, Treasury’s senior officials, the Treasury Department, or the United
States government.

(February 12, 2026)

###### Abstract

This paper describes a discrete-time model of regularly-issued sovereign debt dynamics under a deficit-driven nominal
debt growth regime that explicitly accounts for granular maturity. New
issuance follows fixed allocations across a finite maturity ladder, and the government budget constraint determines total borrowing endogenously. In the
deterministic baseline, we identify a sustainability condition for convergence to a steady-state and
derive closed-form steady portfolio shares, as well as key metrics for steady cost and risk (proxied as one-period
rollover ratio). Extending the model to a
stochastic recurrence equation (SRE) driven by interest rates and (normalized) deficits that
are stationary and mean-reverting, and
using a future-cashflow state representation of debt, we
identify an analogous condition for ergodic convergence
to a unique invariant distribution. This implies that metrics calculated by
Monte Carlo debt simulations driven by factors with these properties will recover the ergodic means of the underlying
system, independently
of initial conditions, provided the simulation horizon is sufficiently long. Analytical formulae for expectations of
certain key metrics under this invariant
distribution are derived, and agreement with simulation is observed. We find that the
introduction of stochastic interest-rate/deficit correlation into the framework
leads to intuitive correction terms to their deterministic-baseline counterparts.

## 1 Introduction

The management of sovereign debt portfolios is a critical aspect of fiscal policy, balancing the trade-offs between minimizing interest cost and mitigating risks associated with refinancing, operational overhead, and interest rate fluctuations. Traditional analyses of debt sustainability ([[10](https://arxiv.org/html/2602.19892v1#bib.bib10)], [[9](https://arxiv.org/html/2602.19892v1#bib.bib9)]) often either aggregate debt stock without distinguishing by maturity, overlooking the heterogeneous impacts of maturity structures on rollover needs and interest payments, or use stylized decompositions into short and long maturity buckets that elide the full maturity distribution. This
aggregation may omit details of interest to debt managers seeking to understand the granular interest-cost and risk impact of maturity selection and
issuance-size adjustments.

Popular modeling frameworks (e.g. [[3](https://arxiv.org/html/2602.19892v1#bib.bib3)], [[4](https://arxiv.org/html/2602.19892v1#bib.bib4)], [[8](https://arxiv.org/html/2602.19892v1#bib.bib8)], [[1](https://arxiv.org/html/2602.19892v1#bib.bib1)]) deploy
numerical forward debt simulations in a stochastic framework, from which averaged
metrics are calculated empirically, and tradeoffs between debt management goals explored or optimized. Such models
allow for the ability to model issuance allocations and time-periods of any desired granularity, as well as to incorporate an arbitrarily detailed set of
assumed macroeconomic factors and relationships as drivers. Because of the number of variables often involved,
and the large dimensionality of the relationships being simulated, the convenience and flexibility of such models can
come at the expense of clarity and intuition regarding the results.

In this paper, we describe an approach, first introduced in [[7](https://arxiv.org/html/2602.19892v1#bib.bib7)] and [[13](https://arxiv.org/html/2602.19892v1#bib.bib13)], to analytically bridging the gap between aggregated theory on the one hand, and
detailed but conceptually complex empirics on the other, using a disaggregated, discrete-time model of
fixed-rate debt dynamics that explicitly accounts for the full maturity ladder. Our framework tracks new and outstanding debt by vintage and tenor, with new issuances allocated according to fixed
proportions across maturities. Minimal issuance under the standard
government budget constraint endogenously fixes total new borrowing to exactly cover primary deficits, interest
payments, and maturing principal. The resulting dynamics, cast as recursion equations, allow us to analyze both
deterministic and simple stochastic frameworks, providing insights into steady-state behaviors and risk profiles of debt portfolios under regular-issuance policies.

In the deterministic baseline, we find closed-form expressions for steady-state portfolio shares in an assumed deficit-driven regime of exponentially growing
(nominal) primary deficits, equivalent to positing a sustainability condition analogous to r<gr<g ([[2](https://arxiv.org/html/2602.19892v1#bib.bib2)]). These
shares depend solely on issuance weights and the deficit growth rate, and are independent of the coupon structure (provided
deficit-growth prevails). The steady-state portfolio also has closed-form formulas for yearly interest cost and risk (proxied as the
one-period rollover fraction) that depend solely on the new-issuance allocation, steady coupons,
and the deficit growth rate.

Extending to stochastic settings, we incorporate mean-reverting interest rates and primary deficits, modeled in this case
as AR(1) processes, which can be correlated to capture countercyclical policy responses. By invoking Foster-Lyapunov drift conditions on
the resulting random-coefficient stochastic recurrence equation (SRE)
([[14](https://arxiv.org/html/2602.19892v1#bib.bib14)], [[11](https://arxiv.org/html/2602.19892v1#bib.bib11)], [[5](https://arxiv.org/html/2602.19892v1#bib.bib5)]), we
establish, again under a sustainability condition that implies deficit-driven growth, ergodic
convergence to a unique stationary distribution. Here, we use a state representation of ongoing debt issuance based on tracking all future cashflows, which preserves and exposes the underlying
linearity of the stochastic recurrence equation driving dynamics.

Ergodic convergence ensures that long-run pathwise time averages, as well as stochastic averages across multiple realizations, of the debt process driven
in this way
align with its theoretical long-term invariant distribution. It follows that for numerical debt models with the same properties, observable metrics computed from
long-horizon simulations should largely recover those of the invariant distribution, provided the simulation horizon is long enough for
mean-reversion to dominate the effect of initial conditions.

Our results have direct implications for debt-management offices (DMOs) seeking to understand the long-term cost-risk tradeoff both theoretically, and for interpreting the empirical results of numerical debt simulation,
when contemplating issuance allocation and conveying the fundamental tradeoffs and relationships between maturity selection. The model also
lays groundwork for incorporating floating-rate debt and other extensions, while also illuminating the difficulty in incorporating such
economically realistic factors as endogenous
interest rates.

The literature on sovereign debt management is extensive but often focuses on continuous-time models or aggregate dynamics.
The discrete-time, full-maturity-ladder, and future-cashflow-representation nature of the
approach described here
complements these by providing tractable closed-forms that allow for incorporation of stochastic interest rate and deficit drivers, and ergodic
analyses, while maintaining the granularity of the maturity profile, bridging theoretical rigor with practical application and computability.

The paper proceeds as follows: Section [2](https://arxiv.org/html/2602.19892v1#S2 "2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") introduces the mathematical notation
and presents the deterministic baseline model introduced in an earlier piece, derives the conditions for asymptotic convergence to a unique
steady-state, and presents key steady-state
metrics. Section [3](https://arxiv.org/html/2602.19892v1#S3 "3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") extends the model framework to incorporate stochastic, mean-reverting,
correlated interest-rates and derives the appropriate generalization for ergodic convergence to an invariant distribution. Formulae for
the key metrics
from the deterministic baseline obtain appropriate correlation adjustments. Section [4](https://arxiv.org/html/2602.19892v1#S4 "4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")
depicts numerical examples of the SRE model for a simple baseline parameter set, comparing and showing
fidelity of the results of numerical Monte Carlo simulation to
the theoretical invariant expectations of key metrics. Section [5](https://arxiv.org/html/2602.19892v1#S5 "5 Conclusions ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") concludes.

## 2 Deterministic Baseline

This section establishes the baseline deterministic model, defining the state variables, issuance rules, payment structures, and budget constraints. We derive conditions for sustainability under exponential deficit growth and obtain closed-form steady-state portfolio shares.

We largely follow the framework and notation introduced in [[7](https://arxiv.org/html/2602.19892v1#bib.bib7)].

### 2.1 Model Setup

Time is modeled in discrete periods t∈ℕ0={0,1,2,…}t\in\mathbb{N}\_{0}=\{0,1,2,\dots\}. The economy features a sovereign borrower issuing debt across a finite set of integer
maturities j=1,2,…,Mj=1,2,\dots,M, where MM is the maximum maturity in periods. All quantities are nominal where applicable, unless otherwise stated.

###### Assumption 2.1 (Debt State).

The outstanding debt at the beginning of period tt is represented by the vector

|  |  |  |
| --- | --- | --- |
|  | Qt=(Qt,1,Qt,2,…,Qt,M)⊤∈ℝM,{Q}\_{t}=(Q\_{t,1},Q\_{t,2},\dots,Q\_{t,M})^{\top}\in\mathbb{R}^{M}, |  |

where Qt,jQ\_{t,j} denotes the face amount of debt with jj periods remaining to maturity at period tt.

Debt evolves as existing obligations roll down the maturity ladder, and new issuances are added.

###### Assumption 2.2 (Issuance Policy).

Total new issuance NtN\_{t} in period tt is allocated across maturities according to fixed proportions:

|  |  |  |
| --- | --- | --- |
|  | Nt,j=fj​Nt,j=1,…,M,N\_{t,j}=f\_{j}N\_{t},\quad j=1,\dots,M, |  |

where f=(f1,…,fM)⊤{f}=(f\_{1},\dots,f\_{M})^{\top} does not depend on tt, and satisfies fj≥0f\_{j}\geq 0 and ∑j=1Mfj=1\sum\_{j=1}^{M}f\_{j}=1.

This fixed-proportion rule is a stylized debt-management issuance strategy. The steady linkage of assumed issuance allocations to the flow of
new funding needs (as opposed to the stock of existing debt) represents a DMO that
follows a stable issuance practice (such as the US, with its ‘regular & predictable’ framework) rather than one that is more opportunistic and volatile
in its debt flows and debt-management practices, or which actively attempts to modify the outstanding portfolio to guide it toward target metrics.

###### Assumption 2.3 (Coupon Payments).

A bond issued at time tt with original maturity jj pays a fixed coupon rj≥0r\_{j}\geq 0 on its face value Nt,jN\_{t,j} in periods t+1t+1 through t+jt+j, totaling jj payments.

Coupons in this model are assumed to be paid periodwise for simplicity (i.e. if the period is yearly, then
semiannual or other coupon schedules are considered to be rolled up by period). The coupon rate
itself rjr\_{j} is assumed constant for each maturity but may vary across jj to reflect a term structure. The ‘yield curve’ of rates
{rj}j=1M\{r\_{j}\}\_{j=1}^{M} can be thought of as the long-term steady yield curve assumption. Typically, this would be assumed to be upward-sloping (though
this is not essential to the basic framework); more will
be said about the importance and role of the assumed curve shape later.

Total interest payments in period tt are the sum of coupons on all outstanding debt issued
in prior periods:

|  |  |  |  |
| --- | --- | --- | --- |
|  | It=∑j=1M∑s=t−jt−1rj​Ns,j=∑j=1Mrj​fj​(∑s=1jNt−s)=∑j=1M(∑k=jMrk​fk)​Nt−j.I\_{t}=\sum\_{j=1}^{M}\sum\_{s=t-j}^{t-1}r\_{j}N\_{s,j}=\sum\_{j=1}^{M}r\_{j}f\_{j}\left(\sum\_{s=1}^{j}N\_{t-s}\right)=\sum\_{j=1}^{M}\left(\sum\_{k=j}^{M}r\_{k}f\_{k}\right)N\_{t-j}. |  | (1) |

Maturing principal in period tt is the debt issued in prior periods that reaches zero remaining maturity at period tt:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mt=Qt−1,1=∑j=1MNt−j,j=∑j=1Mfj​Nt−j.M\_{t}=Q\_{t-1,1}=\sum\_{j=1}^{M}N\_{t-j,j}=\sum\_{j=1}^{M}f\_{j}N\_{t-j}. |  | (2) |

###### Assumption 2.4 (Government Budget Identity).

The government finances the primary deficit DtD\_{t} (representing any new financing-needs),
interest ItI\_{t}, and maturing principal MtM\_{t} through new issuance NtN\_{t}:

|  |  |  |
| --- | --- | --- |
|  | Nt=Dt+It+Mt.N\_{t}=D\_{t}+I\_{t}+M\_{t}. |  |

This identity closes the model endogenously, with NtN\_{t} adjusting to meet fiscal needs. Since the maturing term MtM\_{t} and interest cost ItI\_{t} depend linearly
on quantities Ns,s<tN\_{s},s<t, this is a nonhomogenous linear recursion equation for NtN\_{t} driven
by the exogenous forcing-term DtD\_{t}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nt=Dt+It+Mt=∑j=1M((∑k=jMrk​fk)+fj)​Nt−j+DtN\_{t}=D\_{t}+I\_{t}+M\_{t}=\sum\_{j=1}^{M}\left((\sum\_{k=j}^{M}r\_{k}f\_{k})+f\_{j}\right)N\_{t-j}+D\_{t} |  | (3) |

###### Assumption 2.5 (State Evolution).

The debt state updates as:

|  |  |  |
| --- | --- | --- |
|  | Qt,M=Nt,M=fM​Nt,Qt,j=Qt−1,j+1+Nt,j=Qt−1,j+1+fj​Nt,j=1,…,M−1.Q\_{t,M}=N\_{t,M}=f\_{M}N\_{t},\quad Q\_{t,j}=Q\_{t-1,j+1}+N\_{t,j}=Q\_{t-1,j+1}+f\_{j}N\_{t},\quad j=1,\dots,M-1. |  |

In matrix form:

|  |  |  |
| --- | --- | --- |
|  | Qt=S​Qt−1+Nt​f=S​Qt−1+f​(Dt+It+Mt){Q}\_{t}=S{Q}\_{t-1}+N\_{t}{f}=S{Q}\_{t-1}+{f}(D\_{t}+I\_{t}+M\_{t}) |  |

where SS is the M×MM\times M shift matrix with Sj,j+1=1S\_{j,j+1}=1 for j=1,…,M−1j=1,\dots,M-1, and zeros elsewhere.

### 2.2 Exponential Deficits and Growth-Regime

To analyze long-run behavior, we impose structure on the primary deficit DtD\_{t}. Our assumption here is the most general one that can still plausibly
admit of a self-similar portfolio and thus a steady-state in normalized quantities.

###### Assumption 2.6 (Exponential Deficit Growth).

Primary (nominal) deficits grow exponentially:

|  |  |  |
| --- | --- | --- |
|  | Dt=D0​γt,γ:=1+g>1(g>0),D0>0.D\_{t}=D\_{0}\gamma^{t},\quad\gamma:=1+g>1\quad(g>0),\quad D\_{0}>0. |  |

In
classical debt models it may be assumed, or imposed as a sustainability constraint, that normalized quantities such as debt/GDP and/or primary
deficit/GDP converge to a sustainable long-term fixed quantity. We may connect with that literature by positing g:=γ−1g:=\gamma-1 as the assumed
long-term steady GDP growth-rate. Our assumption about DtD\_{t} then merely represents deficit-growth that maintains stable debt/GDP. While
this identification of γ\gamma with the GDP-growth factor is not essential to the basic mathematical framework used here, we note this simply to
observe that such an assumption about the trend of DtD\_{t} is (if only implicitly) not uncommon.

### 2.3 Backward Recursion and Steady-State

We now analyze the baseline recursion for NtN\_{t}. First normalize all variables by the growth trend: N~t=Nt/γt\tilde{N}\_{t}=N\_{t}/\gamma^{t}, D~t=Dt/γt=D0\tilde{D}\_{t}=D\_{t}/\gamma^{t}=D\_{0}, Q~t=Qt/γt\tilde{{Q}}\_{t}={Q}\_{t}/\gamma^{t}.

Substituting into the budget identity ([3](https://arxiv.org/html/2602.19892v1#S2.E3 "In 2.1 Model Setup ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) and normalizing yields a recurrence for the normalized new-issuance N~t\tilde{N}\_{t}:

|  |  |  |
| --- | --- | --- |
|  | N~t=D0+∑j=1Mfj​γ−j​N~t−j+∑j=1Mrj​fj​∑s=1jγ−s​N~t−s.\tilde{N}\_{t}=D\_{0}+\sum\_{j=1}^{M}f\_{j}\gamma^{-j}\tilde{N}\_{t-j}+\sum\_{j=1}^{M}r\_{j}f\_{j}\sum\_{s=1}^{j}\gamma^{-s}\tilde{N}\_{t-s}. |  |

We are interested in whether the normalized system approaches a long-term steady limit, i.e. N~t→N~∞\tilde{N}\_{t}\to\tilde{N}\_{\infty}. Such a limit must satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | N~∞\displaystyle\tilde{N}\_{\infty} | =D0+(∑j=1Mfj​γ−j+∑j=1Mrj​fj​∑s=1jγ−s)​N~∞\displaystyle=D\_{0}+\left(\sum\_{j=1}^{M}f\_{j}\gamma^{-j}+\sum\_{j=1}^{M}r\_{j}f\_{j}\sum\_{s=1}^{j}\gamma^{-s}\right)\tilde{N}\_{\infty} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =D0+(∑j=1M(∑k=jMrk​fk+fj)​γ−j)​N~∞\displaystyle=D\_{0}+\left(\sum\_{j=1}^{M}\left(\sum\_{k=j}^{M}r\_{k}f\_{k}+f\_{j}\right)\gamma^{-j}\right)\tilde{N}\_{\infty} |  |

Define the feedback function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(γ,r,f)=∑j=1M(∑k=jMrk​fk+fj)​γ−j=∑j=1Mfj​γ−j+∑j=1Mrj​fj​γ−1​1−γ−j1−γ−1.\Phi(\gamma,{r},{f})=\sum\_{j=1}^{M}\left(\sum\_{k=j}^{M}r\_{k}f\_{k}+f\_{j}\right)\gamma^{-j}=\sum\_{j=1}^{M}f\_{j}\gamma^{-j}+\sum\_{j=1}^{M}r\_{j}f\_{j}\gamma^{-1}\frac{1-\gamma^{-j}}{1-\gamma^{-1}}. |  | (4) |

###### Proposition 2.1 (Deficit-Driven Regime).

The system defined by [2.1](https://arxiv.org/html/2602.19892v1#S2.Thmassumption1 "Assumption 2.1 (Debt State). ‣ 2.1 Model Setup ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")–[2.6](https://arxiv.org/html/2602.19892v1#S2.Thmassumption6 "Assumption 2.6 (Exponential Deficit Growth). ‣ 2.2 Exponential Deficits and Growth-Regime ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") is
deficit-driven with growth rate γ\gamma if Φ​(γ,r,f)<1\Phi(\gamma,{r},{f})<1, where Φ​(⋅)\Phi(\cdot) is given by ([4](https://arxiv.org/html/2602.19892v1#S2.E4 "In 2.3 Backward Recursion and Steady-State ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")). In this case, the normalized issuance
converges to N~∞=D0/(1−Φ​(γ,r,f))>0\tilde{N}\_{\infty}=D\_{0}/(1-\Phi(\gamma,{r},{f}))>0.
In other words, for large tt, new
debt asymptotically grows at a rate Nt∼N~∞​γtN\_{t}\sim\tilde{N}\_{\infty}\gamma^{t}
that depends only on γ\gamma, the growth of deficits, not on interest rates, and
independently of initial conditions.

###### Proof.

The recurrence equation for N~t\tilde{N}\_{t} is a linear homogeneous operator on prior values {Ns}s<t\{N\_{s}\}\_{s<t} plus a constant term D0D\_{0}. Asymptotic convergence under the condition on Φ\Phi (here and below we may suppress dependence on γ,r,f\gamma,{r},{f}) can be shown directly by iterating the equation for
aggregate debt (see [[7](https://arxiv.org/html/2602.19892v1#bib.bib7)]); Φ\Phi characterizes the largest root of the associated characteristic polynomial.

Here, to facilitate the discussion below, we will
make the linear recursion explicit by defining an augmented state:

|  |  |  |
| --- | --- | --- |
|  | Xt=(N~t,N~t−1,…,N~t−(M−1))⊤∈ℝM,{X}\_{t}=(\tilde{N}\_{t},\tilde{N}\_{t-1},\dots,\tilde{N}\_{t-(M-1)})^{\top}\in\mathbb{R}^{M}, |  |

The evolution of Xt{X}\_{t} thus has the form:

|  |  |  |
| --- | --- | --- |
|  | Xt=B​Xt−1+d{X}\_{t}=B{X}\_{t-1}+{d} |  |

where

* •

  d=D0​e1d=D\_{0}{e}\_{1}, with e1=(1,0,0,…)Te\_{1}=(1,0,0,\dots)^{T}, and
* •

  the companion matrix BB is constant (in tt), depending only on {rj}\{r\_{j}\}, γ\gamma and f{f}:

  |  |  |  |
  | --- | --- | --- |
  |  | B=S+e1​bT,B=S+e\_{1}b^{T}, |  |

  where S=(δj+1,j)S=(\delta\_{j+1,j}) is an M×MM\times M shift operator containing only
  entries 11 in the first subdiagonal,
  and bj=(∑k=jMrk​fk+fj)​γ−jb\_{j}=(\sum\_{k=j}^{M}r\_{k}f\_{k}+f\_{j})\gamma^{-j}. (Note BB is a Leslie matrix, as arises
  in population ecology; many results from that field will obtain in a laddered-issuance debt model.)

The condition Φ<1\Phi<1 means that the first-row sum of BB, i.e. ∑bj\sum b\_{j}, is <1<1 (while the other row sums are
all 11 because SS is just a shift operator). BB is nonnegative and irreducible, so
by an application of the Perron-Frobenius theorem, the Φ<1\Phi<1 condition means that
the spectral radius of BB satisfies ρ​(B)<1\rho(B)<1. This ensures
that the homogeneous solution to the recursion decays from any initial condition, and
that the particular solution dominates as steady attractor. As we have seen, the limit of Xt,1=N~tX\_{t,1}=\tilde{N}\_{t}
can be written N~∞=D0/(1−Φ)\tilde{N}\_{\infty}=D\_{0}/(1-\Phi).
∎

We will see later that condition [2.1](https://arxiv.org/html/2602.19892v1#S2.Thmtheorem1 "Proposition 2.1 (Deficit-Driven Regime). ‣ 2.3 Backward Recursion and Steady-State ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") is a disaggregated analogue of ”r<gr<g” in traditional debt-sustainability
literature (i.e. if we identify g=γ−1g=\gamma-1 with the GDP growth rate).

### 2.4 Steady-State Portfolio Shares

The normalized state Q~t\tilde{Q}\_{t} evolves as:

|  |  |  |
| --- | --- | --- |
|  | Q~t,M=fM​N~t,Q~t,j=γ−1​Q~t−1,j+1+fj​N~t,j<M.\tilde{Q}\_{t,M}=f\_{M}\tilde{N}\_{t},\quad\tilde{Q}\_{t,j}=\gamma^{-1}\tilde{Q}\_{t-1,j+1}+f\_{j}\tilde{N}\_{t},\quad j<M. |  |

(Note that Q~t−1,1\tilde{Q}\_{t-1,1} is the (normalized) outstanding amount with one period remaining and so it matures at step tt.)

In steady state, Q~t,j→q~j\tilde{Q}\_{t,j}\to\tilde{q}\_{j}, yielding:

|  |  |  |
| --- | --- | --- |
|  | q~M=fM​N~∞,q~j=γ−1​q~j+1+fj​N~∞,\tilde{q}\_{M}=f\_{M}\tilde{N}\_{\infty},\quad\tilde{q}\_{j}=\gamma^{-1}\tilde{q}\_{j+1}+f\_{j}\tilde{N}\_{\infty}, |  |

where we recall N~∞=D0/(1−Φ)\tilde{N}\_{\infty}=D\_{0}/(1-\Phi).

Solving backwards:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q~j=N~∞​∑k=jMγj−k​fk.\tilde{q}\_{j}=\tilde{N}\_{\infty}\sum\_{k=j}^{M}\gamma^{j-k}f\_{k}. |  | (5) |

The aggregate normalized debt in steady-state is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q~=∑j=1Mq~j=N~∞​∑k=1Mfk​1−γ−k1−γ−1.\tilde{q}=\sum\_{j=1}^{M}\tilde{q}\_{j}=\tilde{N}\_{\infty}\sum\_{k=1}^{M}f\_{k}\frac{1-\gamma^{-k}}{1-\gamma^{-1}}. |  | (6) |

Thus, the steady-state portfolio shares are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θj=q~jq~=∑k=jMfk​γj−k∑k=1Mfk​1−γ−k1−γ−1.\theta\_{j}=\frac{\tilde{q}\_{j}}{\tilde{q}}=\frac{\sum\_{k=j}^{M}f\_{k}\gamma^{j-k}}{\sum\_{k=1}^{M}f\_{k}\frac{1-\gamma^{-k}}{1-\gamma^{-1}}}. |  | (7) |

###### Proposition 2.2 (Convergence to Steady-State Shares).

For the system defined by [2.1](https://arxiv.org/html/2602.19892v1#S2.Thmassumption1 "Assumption 2.1 (Debt State). ‣ 2.1 Model Setup ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")–[2.6](https://arxiv.org/html/2602.19892v1#S2.Thmassumption6 "Assumption 2.6 (Exponential Deficit Growth). ‣ 2.2 Exponential Deficits and Growth-Regime ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure"), under the assumption
Φ​(γ,r,f)<1\Phi(\gamma,{r},{f})<1, portfolio shares Qj,t/QtQ\_{j,t}/Q\_{t} converge to
the values θj\theta\_{j} defined in ([7](https://arxiv.org/html/2602.19892v1#S2.E7 "In 2.4 Steady-State Portfolio Shares ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")).

###### Proof.

The normalized Q~t\tilde{{Q}}\_{t} converges to q{q} by the contraction property of the backward recursion with factor γ−1<1\gamma^{-1}<1. The
ratios Qj,t/Qt=Q~j,t/∑kQ~k,tQ\_{j,t}/Q\_{t}=\tilde{Q}\_{j,t}/\sum\_{k}\tilde{Q}\_{k,t} then converge to θj\theta\_{j}, independent of initial conditions.
∎

###### Remark.

The shares ([7](https://arxiv.org/html/2602.19892v1#S2.E7 "In 2.4 Steady-State Portfolio Shares ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) depend only on f{f} and γ\gamma, not on rr. Coupons influence the condition for deficit-driven growth,
and potentially sustainability, via Φ​(γ,r,f)<1\Phi(\gamma,{r},{f})<1, but do not affect the long-run portfolio composition in deficit-driven regimes.

This deterministic baseline provides a benchmark for the stochastic extensions, for which
uncertainty introduces probabilistic risk dimensions. In the following sections
we observe some of its basic cost and risk properties.

### 2.5 Steady Interest-Cost Ratio

In the deterministic steady-state, the next-period interest-cost, as a fraction of current-face outstanding, is just the steady weighted-average coupon. Because
rates rjr\_{j} are constant by original tenor, this can be written:

|  |  |  |
| --- | --- | --- |
|  | W​A​C=∑j=1Mwj​rjWAC=\sum\_{j=1}^{M}w\_{j}r\_{j} |  |

where the weights wjw\_{j} represent
current-outstanding by original maturity, rolling up the jj prior periods of new issuance at tenor jj.

Writing wt,jw\_{t,j} to represent
the fraction of outstanding debt at period tt with original-maturity jj in steady-state, we must have

|  |  |  |
| --- | --- | --- |
|  | wt,j∝∑s=t−jt−1fj​Ns=fj​∑s=t−jt−1γs​N~s∼N~∞​fj​∑s=t−jt−1γsw\_{t,j}\propto\sum\_{s=t-j}^{t-1}f\_{j}N\_{s}=f\_{j}\sum\_{s=t-j}^{t-1}\gamma^{s}\tilde{N}\_{s}\sim\tilde{N}\_{\infty}f\_{j}\sum\_{s=t-j}^{t-1}\gamma^{s} |  |

After normalizing and cancellation we obtain explicit values for the portfolio weights that determine steady WAC:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​A​C=∑j=1Mwj​rj,wj=fj​(1−γ−j)∑k=1Mfk​(1−γ−k)WAC=\sum\_{j=1}^{M}w\_{j}r\_{j},\;w\_{j}=\frac{f\_{j}(1-\gamma^{-j})}{\sum\_{k=1}^{M}f\_{k}(1-\gamma^{-k})} |  | (8) |

### 2.6 Steady Rollover Fraction

The fraction of the deterministic baseline portfolio that rolls over each period is just θ1\theta\_{1}. Using wjw\_{j} as defined above, and substituting
into express ([7](https://arxiv.org/html/2602.19892v1#S2.E7 "In 2.4 Steady-State Portfolio Shares ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) for θ1\theta\_{1}, this can be expressed

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ1=q1q=∑k=1Mfk​γ1−k∑k=1Mfk​1−γ−k1−γ−1=∑k=1Mfk​γ−k∑k=1Mfk​1−γ−kγ−1=∑j=1Mwj​τj\theta\_{1}=\frac{q\_{1}}{q}=\frac{\sum\_{k=1}^{M}f\_{k}\gamma^{1-k}}{\sum\_{k=1}^{M}f\_{k}\frac{1-\gamma^{-k}}{1-\gamma^{-1}}}=\frac{\sum\_{k=1}^{M}f\_{k}\gamma^{-k}}{\sum\_{k=1}^{M}f\_{k}\frac{1-\gamma^{-k}}{\gamma-1}}=\sum\_{j=1}^{M}w\_{j}\tau\_{j} |  | (9) |

with τj=(γ−1)/(γj−1)\tau\_{j}=(\gamma-1)/(\gamma^{j}-1), and wjw\_{j} as defined for W​A​CWAC,

|  |  |  |
| --- | --- | --- |
|  | wj=fj​(1−γ−j)∑k=1Mfk​(1−γ−k).w\_{j}=\frac{f\_{j}(1-\gamma^{-j})}{\sum\_{k=1}^{M}f\_{k}(1-\gamma^{-k})}. |  |

(It will become apparent later why it is beneficial to express θ1\theta\_{1} in terms of ww.)

### 2.7 Relationship to Sustainability Condition

Using the preceding steady quantities, algebraic manipulation shows
the feedback function Φ​(γ,r,f)\Phi(\gamma,{r},{f}) can
be rewritten as simply Φ=(θ1+W​A​C)/(θ1+g)\Phi=(\theta\_{1}+WAC)/(\theta\_{1}+g). Hence condition [2.1](https://arxiv.org/html/2602.19892v1#S2.Thmtheorem1 "Proposition 2.1 (Deficit-Driven Regime). ‣ 2.3 Backward Recursion and Steady-State ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") for a deficit-driven regime with a unique steady-state
is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(γ,r,f)=θ1+W​A​Cθ1+g<1⇔W​A​C<g.\Phi(\gamma,{r},{f})=\frac{\theta\_{1}+WAC}{\theta\_{1}+g}<1\quad\iff\quad WAC<g. |  | (10) |

This reveals the condition for being in a deficit-driven regime as the (intuitive if not
tautological) statement that long-term deficits grow faster than steady-state compounded interest. As
noted previously this is effectively the sustainability condition ”r<gr<g” that arises in debt literature, albeit to make the linkage sharp we would need to
additionally identify gg with GDP growth as well (in our baseline framework it merely denotes deficit-growth).

In other words, if deficits grow at the same rate as GDP (no fiscal blowup), and the interest rates are such that the
sustainability condition r<gr<g is satisfied,
where r:=W​A​Cr:=WAC is the steady, long-term average interest rate on the portfolio, then
debt growth is deficit-driven, growing at the same asymptotic rate as GDP, and further, has a unique asymptotic steady-state from any initial condition.

Figure [1](https://arxiv.org/html/2602.19892v1#S2.F1 "Figure 1 ‣ 2.7 Relationship to Sustainability Condition ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") illustrates the relationship between r,fr,f, and gg (or γ\gamma) vs. Φ\Phi for simple choices of new-issue allocations.

![Refer to caption](phi1.jpg)


Figure 1: Feedback function Φ\Phi and steady W​A​CWAC formula
calculated for γ=1.045\gamma=1.045, r=(.02,.03,.05)Tr=(.02,.03,.05)^{T} under various issuance allocations. In
this example the long-tilted allocation leads to Φ>1\Phi>1 (the formula for W​A​CWAC leads to W​A​C>gWAC>g), and so
debt dynamics are interest-driven rather than deficit-driven. The other
two allocations satisfy Φ<1\Phi<1 for this γ\gamma, thus attain steady-state under deficit-driven asymptotics.

From the form ([10](https://arxiv.org/html/2602.19892v1#S2.E10 "In 2.7 Relationship to Sustainability Condition ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) of our deficit-driven (sustainability) condition we can also observe the intuitive result that, for given values of W​A​C<gWAC<g, larger
values of θ1\theta\_{1} - that is, higher yearly rollover fractions - cause the portfolio to be closer to breaching its sustainability (deficit-driven steady-state) boundary, and
convergence/pullback to the long-term trend would naturally be expected to be slower and more volatile.

### 2.8 Optimization and Frontier

In this section we describe how the preceding baseline metrics can be used to set up a simple if idealized portfolio selection problem.

Recall the expression for steady one-period rollover fraction,

|  |  |  |
| --- | --- | --- |
|  | θ1=∑j=1Mwj​τj\theta\_{1}=\sum\_{j=1}^{M}w\_{j}\tau\_{j} |  |

with τj=(γ−1)/(γj−1)\tau\_{j}=(\gamma-1)/(\gamma^{j}-1).

Note τ={τj}\tau=\{\tau\_{j}\} is uniformly decreasing in jj. Compare this
form of θ1\theta\_{1} with equation ([8](https://arxiv.org/html/2602.19892v1#S2.E8 "In 2.5 Steady Interest-Cost Ratio ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) for W​A​CWAC:

|  |  |  |
| --- | --- | --- |
|  | W​A​C=∑j=1Mwj​rjWAC=\sum\_{j=1}^{M}w\_{j}r\_{j} |  |

Typically, rr used here will be upward-sloping. One then sees in the opposite slopes of rr and τ\tau the
classical cost-risk tradeoff. Assuming cost is proxied by WAC and risk by θ1\theta\_{1}, the portfolio selection
problem reduces to selecting ff to minimize W​A​CWAC, subject to a constraint on θ1\theta\_{1}.
Given the preceding formulas, and
because
ff and ww differ only by a rescaling and renormalization (any ff can be uniquely recovered from its corresponding ww and
vice versa),
this reduces to solving for optimal accumulation weights ww to balance minimizing a weighted-sum of
rr against keeping a weighted-sum of the downward-sloping τ\tau less than a
risk-tolerance.

When framed this way, optimal issuance allocation from a steady-state viewpoint reduces to a simple linear programming
problem. If rr is upward-sloping and not too concave, as would be typical of any plausible long-term yield curve assumption, then absent further constraint the optimal
solution will inevitably place
maximum issuance weight on some intermediate or ”belly” tenor
j∗j^{\*} (or a pair of neighbor tenors). Namely, optimization will concentrate issuance on the smallest tenor (to minimize cost) such that
concentrated-issuance at that “sweet spot” tenor, or a pair of neighboring tenors if the optimal tenor is not an integer, maintains θ1\theta\_{1} at the prescribed level. Indeed, it
can be shown under these conditions that the optimal tenor is just

|  |  |  |
| --- | --- | --- |
|  | j∗=log⁡(1+(γ−1)/R)log⁡γ≈1/R,j^{\*}=\frac{\log(1+(\gamma-1)/R)}{\log\gamma}\approx 1/R, |  |

where RR is the risk tolerance for θ1\theta\_{1}, i.e. θ1≤R\theta\_{1}\leq R is the constraint. (See [[7](https://arxiv.org/html/2602.19892v1#bib.bib7)], [[13](https://arxiv.org/html/2602.19892v1#bib.bib13)].)

If nontrivial constraints are applied (such as lower- and upper-bounds on the weights fjf\_{j}) then
some blended allocation within the feasible set, and best approximating this j∗j^{\*}, meaning issuance concentrated toward the “belly” rather than short
or long, will be the optimum.

If, alternatively, rr does not have an upward-sloping structure then less can be said in general, as the simplex optimum would depend on the precise details of rr. For example, if rr is “barbelled” (such that r1r\_{1} and rMr\_{M} are small while intermediate rjr\_{j} are larger), or highly concave, then one can find it optimal for issuance to follow a “barbell” pattern as well, with higher weight on f1f\_{1} and fMf\_{M} and lower or none at intermediate tenors. (Again
see [[7](https://arxiv.org/html/2602.19892v1#bib.bib7)].) Such
an
assumption for rr would of course not be typical or parsimonious in debt modeling.

We add that absent further assumptions or established facts about the dynamics of the debt portfolio, the portfolio selection framework as described in this
section
is highly idealized, in effect answering the hypothetical
question, if rates and (normalized) deficits were constant, which allocation ff would, if permanently deployed, lead to the optimal steady portfolio. While such a framework may seem overly simplified,
we will find in the sequel that in a simple extension to a stochastic framework, to some extent many of the mathematical consequences of this baseline case can be
carried over and remain applicable
to more realistic frameworks and models, with only modest adjustment.

### 2.9 No-Growth Limit γ→1+\gamma\to 1^{+}

It is instructive to examine the asymptotic limits of these metrics and observations for the limiting case γ→1+\gamma\to 1^{+}.
We will show that the above steady metrics reduce to simple and intuitive accumulation quantities.

The steady portfolio fractions θj\theta\_{j} reduce, via (1−γ−k)/(1−γ−1)→k(1-\gamma^{-k})/(1-\gamma^{-1})\to k, to

|  |  |  |
| --- | --- | --- |
|  | θj→∑k=jMfk∑k=1Mk​fk\theta\_{j}\to\frac{\sum\_{k=j}^{M}f\_{k}}{\sum\_{k=1}^{M}kf\_{k}} |  |

Thus, the steady portfolio-share with tenor jj (under no deficit-growth) is just proportional to the fraction
of new-issuance at/above tenor jj. (The more realistic
case γ>1\gamma>1 applies a correction to this expression that preferentially weights more-recent issuance.)

For WAC, a similar reduction shows

|  |  |  |
| --- | --- | --- |
|  | W​A​C→∑jwj​rj,wj=j​fj/∑kk​fkWAC\to\sum\_{j}w\_{j}r\_{j},\quad w\_{j}=jf\_{j}/\sum\_{k}kf\_{k} |  |

Note this weights each issuance fraction fjf\_{j} by how many periods the bucket remains in the portfolio, and then normalizes. Issuances of tenor jj
from jj prior periods are present in the current portfolio, so rjr\_{j} must be counted jj times.

And for 1-period rollover, we can read off from above,

|  |  |  |
| --- | --- | --- |
|  | θ1→∑kfk/∑kk​fk=1/∑kk​fk.\theta\_{1}\to\sum\_{k}f\_{k}/\sum\_{k}kf\_{k}=1/\sum\_{k}kf\_{k}. |  |

Note this is just the reciprocal of the new-issue weighted average maturity (NWAM). Unsurprisingly, shorter-/longer-tilted new-issuance leads to a steady
portfolio with higher/lower steady periodwise rollover fraction.

And as we have seen, there is an optimal “belly” tenor given risk tolerance RR, which as γ→1\gamma\to 1
approaches j∗→1/Rj^{\*}\to 1/R.

These forms of steady accumulation metrics can be found in e.g. [[13](https://arxiv.org/html/2602.19892v1#bib.bib13)] and in
use in [[15](https://arxiv.org/html/2602.19892v1#bib.bib15)], [[16](https://arxiv.org/html/2602.19892v1#bib.bib16)]. Note that
technically these simplified formulas only
remain representative of the unique steady-state under a particular asymptotic limit γ→1,r→0\gamma\to 1,r\to 0 that
maintains Φ​(γ,r,f)<1\Phi(\gamma,{r},{f})<1.

If the condition Φ<1\Phi<1 does not hold, for example for γ\gamma sufficiently near 11 (g≈0g\approx 0), debt growth will instead generally be
interest-rate driven. Moreover there need not be a
single steady-state, as the spectral radius condition ρ​(B)<1\rho(B)<1 does not hold, so we do not have asymptotic convergence to a particular solution. There can be periodic or
otherwise non-converging debt dynamics, and those dynamics can depend on initial values.

Finally, if there is a steady-state in the non-deficit-driven case, alternate
formulas for steady portfolio metrics will apply, generally
having the same form as those given above, but with γ\gamma replaced by β:=1+W​A​C\beta:=1+WAC, where W​A​CWAC is the
endogenously-determined steady interest cost. We omit the details here as outside the scope of this piece.

## 3 Stochastic Extension

In this section we incorporate stochastic interest rates and primary deficits to better capture real-world uncertainties, allowing for
correlations that reflect economic cycles. The basic underlying structure of the model is the same as and builds on that developed in section [2](https://arxiv.org/html/2602.19892v1#S2 "2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure").

### 3.1 Stochastic Model Setup

NtN\_{t}, now stochastic, is still determined via the budget equation:

|  |  |  |
| --- | --- | --- |
|  | Nt=Dt+It+Mt,N\_{t}=D\_{t}+I\_{t}+M\_{t}, |  |

Interest payments are

|  |  |  |
| --- | --- | --- |
|  | It=∑j=1M∑k=1jrt−k,j​Nt−k,j=∑j=1Mfj​(∑k=1jrt−k,j​Nt−k)I\_{t}=\sum\_{j=1}^{M}\sum\_{k=1}^{j}r\_{t-k,j}N\_{t-k,j}=\sum\_{j=1}^{M}f\_{j}\left(\sum\_{k=1}^{j}r\_{t-k,j}N\_{t-k}\right) |  |

where rt,jr\_{t,j} represents the j−j-period interest rate applicable to debt issued in period tt. Because it is random and varies from one period to the next we cannot factor it out of the inner sum.

Maturing principal remains a summation of past issuance, now stochastic:

|  |  |  |
| --- | --- | --- |
|  | Mt=∑j=1MNt−j,j=∑j=1Mfj​Nt−jM\_{t}=\sum\_{j=1}^{M}N\_{t-j,j}=\sum\_{j=1}^{M}f\_{j}N\_{t-j} |  |

The following sections will analyze this system under simple but representative assumptions about the evolution of rt,jr\_{t,j} and DtD\_{t}.

###### Assumption 3.1 (Interest Rates).

Each maturity-specific rate follows an AR(1) process:

|  |  |  |
| --- | --- | --- |
|  | rt,j=r¯j+ϕj​(rt−1,j−r¯j)+ϵt,j,ϵt,j∼𝒩​(0,σj2),0<ϕj<1.r\_{t,j}=\bar{r}\_{j}+\phi\_{j}(r\_{t-1,j}-\bar{r}\_{j})+\epsilon\_{t,j},\quad\epsilon\_{t,j}{\sim}\mathcal{N}(0,\sigma\_{j}^{2}),\quad 0<\phi\_{j}<1. |  |

Rates here are independent across maturities for simplicity, though extensions could include cross-correlations.

###### Assumption 3.2 (Deficits).

Deficits are normalized via Dt=D~t​γtD\_{t}=\tilde{D}\_{t}\gamma^{t}, and the normalized deficit process follows:

|  |  |  |
| --- | --- | --- |
|  | D~t=D¯0+ψ​(D~t−1−D¯0)+ηt,ηt∼𝒩​(0,ς2),0<ψ<1,\tilde{D}\_{t}=\bar{D}\_{0}+\psi(\tilde{D}\_{t-1}-\bar{D}\_{0})+\eta\_{t},\quad\eta\_{t}{\sim}\mathcal{N}(0,\varsigma^{2}),\quad 0<\psi<1, |  |

This allows fluctuations around an exponentially-growing trend, with persistence ψ\psi.

###### Assumption 3.3 (Correlations).

The innovations ηt\eta\_{t} and (ϵ1,t,…,ϵM,t)⊤(\epsilon\_{1,t},\dots,\epsilon\_{M,t})^{\top} are correlated as Σj=Cov⁡(ηt,ϵj,t)=ρ​ς​σj\Sigma\_{j}=\operatorname{Cov}(\eta\_{t},\epsilon\_{j,t})=\rho\varsigma\sigma\_{j}, ρ∈(−1,1)\rho\in(-1,1).

A countercyclical assumption of negative correlations (ρ<0\rho<0) may be seen as the economically realistic one, as it
models scenarios in which high deficits (e.g., during recessions) tend to coincide
with low rates (e.g., due to monetary policy and/or safe-haven flows), dampening fiscal stress. (A more general extension of this framework could allow for a fuller correlation
matrix; here we posit scalar parametrization for simplicity.)

The system for NtN\_{t} is now a stochastic recurrence equation (SRE):

|  |  |  |
| --- | --- | --- |
|  | Nt=Dt+It+Mt=∑j=1Mfj​[(∑k=1jrt−k,j​Nt−k)+Nt−j]+Dt{N}\_{t}={D}\_{t}+{I}\_{t}+{M}\_{t}=\sum\_{j=1}^{M}f\_{j}\left[\left(\sum\_{k=1}^{j}r\_{t-k,j}N\_{t-k}\right)+N\_{t-j}\right]+{D}\_{t} |  |

This expresses the period-tt new issuance amount NtN\_{t} in terms of new deficits and prior
values Nt−kN\_{t-k}, as well as prior-period
interest rates. The rates rt−k,jr\_{t-k,j} are not constant
but realized at time of issued, and so must be retained to fully describe this recursion. One could approach this SRE by defining an augmented-state that involves not just NtN\_{t} and its lags NsN\_{s}, but prior rates rs,⋅r\_{s,\cdot} as well. Because of
the interaction terms rt−k,j​Nt−kr\_{t-k,j}N\_{t-k}, the system thus framed is not linear as in the
deterministic baseline case; it has a bilinear form and a direct analysis would require the theory of nonlinear Markov processes.

However, under an alternative state representation we can represent the system as a linear SRE.

### 3.2 Future Cashflow Representation

Rather than using NtN\_{t} (and lags) as state variables, let outstanding debt be defined by the full collection of its future cashflows.

###### Assumption 3.4 (Future Cashflows).

Denote by Yt:=(Pt,Ct)T∈ℝ2​M{Y}\_{t}:=(P\_{t},C\_{t})^{T}\in\mathbb{R}^{2M} the vector of all known and fixed
future cashflow obligations, principal (PtP\_{t}) and coupon (CtC\_{t}) payments, owing to oustanding debt
at period tt. That is, the quantity Pt,j​(j=1,…,M)P\_{t,j}(j=1,\dots,M) is the total principal amount obligated in period t+jt+j, and Ct,jC\_{t,j} the total coupon amount, due only to outstanding debt at period tt.

Debt evolution in this framing now consists of a) rolling both components of the outflow vector Yt{Y}\_{t} forward, and b) adding the effect of period-tt new issuance NtN\_{t}. This
can be written

|  |  |  |
| --- | --- | --- |
|  | Pt=S​Pt−1+Nt​fP\_{t}=SP\_{t-1}+N\_{t}f |  |

|  |  |  |
| --- | --- | --- |
|  | Ct=S​Ct−1+Nt​Rt​fC\_{t}=SC\_{t-1}+N\_{t}R\_{t}f |  |

with NtN\_{t}, f{f} representing the period-tt new-issuance amount and issue allocation (respectively), as before; S=δj,j+1S=\delta\_{j,j+1} an
upper-diagonal shift matrix; and RtR\_{t}
the matrix of coupon streams with rates struck in period tt:

|  |  |  |
| --- | --- | --- |
|  | Rt:=(rt,1rt,2rt,3…rt,M0rt,2rt,3…rt,M00rt,3…rt,M⋮⋱0…0rt,M)=(11…01…⋮⋱)⋅d​i​a​g​(rt)=U⋅d​i​a​g​(rt)R\_{t}:=\begin{pmatrix}r\_{t,1}&r\_{t,2}&r\_{t,3}&\dots&r\_{t,M}\\ 0&r\_{t,2}&r\_{t,3}&\dots&r\_{t,M}\\ 0&0&r\_{t,3}&\dots&r\_{t,M}\\ \vdots&&\ddots&&\\ 0&\dots&&0&r\_{t,M}\end{pmatrix}=\begin{pmatrix}1&1&\dots\\ 0&1&\dots\\ \vdots&&\ddots\end{pmatrix}\cdot diag(r\_{t})=U\cdot diag({r}\_{t}) |  |

Thus

|  |  |  |
| --- | --- | --- |
|  | Yt=S′​Yt−1+Nt​Rt′​f{Y}\_{t}=S^{\prime}{Y}\_{t-1}+N\_{t}R^{\prime}\_{t}{f} |  |

with

|  |  |  |
| --- | --- | --- |
|  | S′:=(S00S),Rt′:=(I,U⋅d​i​a​g​(rt))TS^{\prime}:=\begin{pmatrix}S&0\\ 0&S\end{pmatrix},\quad R^{\prime}\_{t}:=(I,U\cdot diag({r}\_{t}))^{T} |  |

Because the first entries of Pt−1P\_{t-1} and Ct−1C\_{t-1} contain precisely the amount of existing
principal and coupon cashflows due in period tt (i.e. Mt+ItM\_{t}+I\_{t} in our prior
formulation), the
new-issue amount NtN\_{t} in turn can be written linearly in the previous state,

|  |  |  |
| --- | --- | --- |
|  | Nt=Pt−1,1+Ct−1,1+Dt=eT​Yt−1+DtN\_{t}=P\_{t-1,1}+C\_{t-1,1}+D\_{t}=e^{T}{Y}\_{t-1}+D\_{t} |  |

where e=(e1T​e1T)Te=(e\_{1}^{T}\;e\_{1}^{T})^{T}.

Thus the recurrence is simply

|  |  |  |
| --- | --- | --- |
|  | Yt=Bt​Yt−1+dt{Y}\_{t}=B\_{t}{Y}\_{t-1}+d\_{t} |  |

where BtB\_{t} and dtd\_{t} are stochastic and depend on rate/deficit data at time tt, but not on the state Yt−1{Y}\_{t-1}:

|  |  |  |
| --- | --- | --- |
|  | Bt:=S′+Rt′​f​eTB\_{t}:=S^{\prime}+R^{\prime}\_{t}fe^{T} |  |

|  |  |  |
| --- | --- | --- |
|  | dt:=Dt​Rt′​fd\_{t}:=D\_{t}R^{\prime}\_{t}f |  |

This is a linear stochastic recurrence equation (SRE) for Yt{Y}\_{t}, with random coefficients BtB\_{t}, and
driven by the exogenous stochastic terms (rt,Dt)({r}\_{t},D\_{t}). (See e.g. ([[6](https://arxiv.org/html/2602.19892v1#bib.bib6)].) Taken together, the augmented
series (Yt,rt,Dt)(Y\_{t},{r}\_{t},D\_{t}) is a Markov process. Of course, because the forcing term dtd\_{t} depends on DtD\_{t} which grows like γt\gamma^{t}, this system is unbounded
and so we will need to normalize to analyze further.

### 3.3 Normalized Linear SRE and Ergodic Convergence

As in the deterministic case, define normalized quantities P~t=γ−t​Pt,C~t=γ−t​Ct,Y~t=γ−t​Yt\tilde{P}\_{t}=\gamma^{-t}P\_{t},\tilde{C}\_{t}=\gamma^{-t}C\_{t},{\tilde{Y}}\_{t}=\gamma^{-t}{Y}\_{t} and so on. The
SRE of section [3.2](https://arxiv.org/html/2602.19892v1#S3.SS2 "3.2 Future Cashflow Representation ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y~t=B~t​Y~t−1+d~t\tilde{{Y}}\_{t}=\tilde{B}\_{t}\tilde{{Y}}\_{t-1}+\tilde{d}\_{t} |  | (11) |

where B~t=γ−1​Bt=γ−1​(S′+Rt′​f​eT)\tilde{B}\_{t}=\gamma^{-1}B\_{t}=\gamma^{-1}(S^{\prime}+R^{\prime}\_{t}fe^{T}) and d~t=γ−t​Dt​Rt′​f=D~t​Rt′​f\tilde{d}\_{t}=\gamma^{-t}D\_{t}R^{\prime}\_{t}f=\tilde{D}\_{t}R^{\prime}\_{t}f. Now the forcing term d~t\tilde{d}\_{t} is stationary,
with finite mean and bounded moments, because it depends only on AR(1) processes: (normalized) deficits D~t\tilde{D}\_{t} and rates rtr\_{t}. The companion matrix B~t\tilde{B}\_{t} is
stochastic and depends on rates, but is independent of the state Y~s\tilde{Y}\_{s}.

The normalized linear SRE ([11](https://arxiv.org/html/2602.19892v1#S3.E11 "In 3.3 Normalized Linear SRE and Ergodic Convergence ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) is now in a form that allows us to establish ergodic convergence to an invariant distribution, given
a sustainability-like condition, using
standard Foster-Lyapunov drift conditions ([[14](https://arxiv.org/html/2602.19892v1#bib.bib14)],[[11](https://arxiv.org/html/2602.19892v1#bib.bib11)]).

Consider the deterministic, nonnegative expected-value dynamics Zt=C​Zt−1+bZ\_{t}=CZ\_{t-1}+b, where C:=E​(|B~t|)C:=E(|\tilde{B}\_{t}|) and b:=E​(|d~t|)b:=E(|\tilde{d}\_{t}|). Both
CC and bb
are constant, due to the stationarity of D~t\tilde{D}\_{t} and rtr\_{t}. (We emphasize that this recursion equation is merely an
associated equation introduced for the purpose of establishing
the required sustainability condition, and not descriptive of debt dynamics itself.) From
the structure of |B~t||\tilde{B}\_{t}| it is clear
this system describes the dynamics of deterministic, iterated debt-issuance as described in section [2](https://arxiv.org/html/2602.19892v1#S2 "2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure"), but with interest-rates fixed at their expected absolute-values rj∗:=E​(|r⋅,j|)r^{\*}\_{j}:=E(|r\_{\cdot,j}|).

###### Remark.

For completeness, even though in the deterministic case we assumed rj≥0r\_{j}\geq 0, here we allow for a distinction between r¯j=E​(rj)\bar{r}\_{j}=E(r\_{j}) and rj∗=E​(|rj|)r^{\*}\_{j}=E(|r\_{j}|) in recognition of the fact that by driving the rate processes
with Gaussian innovations, they may become negative. Because of this, the sustainability condition must be written in terms of E​(|rj|)E(|r\_{j}|) rather than E​(rj)E(r\_{j}), making it a slightly stronger constraint. This
distinction could be removed by stipulating a lognormal or other process for rjr\_{j} that remains nonnegative; here we have postulated Gaussian
innovations for ease of presentation.

As we saw, such a
system converges to a unique asymptotic steady-state in general if a sustainability condition holds, which in this context now takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(γ,r∗,f)=∑j=1M(∑k=jMrk∗​fk+fj)​γ−j=∑j=1Mfj​γ−j+∑j=1Mrj∗​fj​γ−1​1−γ−j1−γ−1<1.\Phi(\gamma,{r^{\*}},{f})=\sum\_{j=1}^{M}\left(\sum\_{k=j}^{M}r^{\*}\_{k}f\_{k}+f\_{j}\right)\gamma^{-j}=\sum\_{j=1}^{M}f\_{j}\gamma^{-j}+\sum\_{j=1}^{M}r^{\*}\_{j}f\_{j}\gamma^{-1}\frac{1-\gamma^{-j}}{1-\gamma^{-1}}<1. |  | (12) |

Under this condition, the homogenous solution must decay. In the future-cashflow space of the dynamics for ZtZ\_{t} this must equivalently mean the spectral radius is contractive, ρ​(C)<1\rho(C)<1. By Perron-Frobenius on the
nonnegative operator CC, there then exists a
nonnegative left eigenvector vv of CC with vT​C=ρ​(C)​vTv^{T}C=\rho(C)v^{T}, ρ​(C)<1\rho(C)<1.

Use this vv to define a Lyapunov function on the original system, V​(Y)=vT​|Y|V(Y)=v^{T}|Y|. By construction,

|  |  |  |
| --- | --- | --- |
|  | E​(V​(Y~t+1)|Y)≤vT​E​(|B~t|)​|Y|+E​(d~t)=vT​C​|Y|+vT​b=ρ​(C)​vT​|Y|+b′=ρ​(C)​V​(Y)+b′.E(V(\tilde{Y}\_{t+1})|Y)\leq v^{T}E(|\tilde{B}\_{t}|)|Y|+E(\tilde{d}\_{t})=v^{T}C|Y|+v^{T}b=\rho(C)v^{T}|Y|+b^{\prime}=\rho(C)V(Y)+b^{\prime}. |  |

where b′b^{\prime} is a constant, and ρ​(C)<1\rho(C)<1. The Foster-Lyapunov drift criterion is thus satisfied.

###### Remark.

(Minorization). Because the exogenous drivers rt,D~tr\_{t},\tilde{D}\_{t} include Gaussian innovations with full support on
ℝk\mathbb{R}^{k}, their conditional distribution given any past state, thus the affine term d~t\tilde{d}\_{t}, and therefore the transition
kernel of the update map for Y~t\tilde{Y}\_{t},
admits a density that is strictly positive on every compact set.
Therefore, every sufficiently large compact sublevel set of the Lyapunov function is a small set in the sense of Meyn–Tweedie, establishing
the required minorization condition as well.

These drift and minorization conditions establish that the system converges ergodically.

###### Proposition 3.1 (Deficit-Driven Regime and Ergodicity).

Under the sustainability condition Φ​(γ,E​(|r|),f)<1\Phi(\gamma,E(|r|),{f})<1 (equivalently, W​A​C​(E​(|r|),f,γ)<gWAC(E(|r|),f,\gamma)<g), the normalized debt process Y~t\tilde{Y}\_{t}
driven by exogenous primary-deficits growing at rate γ\gamma converges ergodically
to a unique invariant measure π\pi.

In particular, for any bounded measurable gg,

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1Tg​(Y~t)→Eπ​[g]a.s.\frac{1}{T}\sum\_{t=1}^{T}g({\tilde{Y}}\_{t})\to E\_{\pi}[g]\quad\text{a.s.} |  |

(Below, where written, E​[⋅]E[\cdot] will always denote Eπ​[⋅]E\_{\pi}[\cdot] for this invariant measure π\pi.)

###### Remark.

While here we have developed and illustrated the stochastic structure stipulating
simple AR(1) Gaussian processes for rates and deficits, the analysis can be extended and equally applied
to more realistic macro environments in which these variables are, for
example, linear functions of underlying Gaussian factors (e.g. output gap, inflation) governed by a VAR. In such settings, the normalized debt dynamics
in the future-cashflow representation
remain a linear stochastic recurrence equation driven by a stationary exogenous process, and the ergodicity and the invariant-mean results below continue
to hold with the same formulas, with E​(rt)E(r\_{t}), E​(D~t)E(\tilde{D}\_{t}) and
C​o​v​(rt,D~t)Cov(r\_{t},\tilde{D}\_{t}) interpreted as the corresponding moments implied by the macro-factor model.

What we have observed here is that in a simple but representative class of stochastic debt dynamics, under a sustainability condition that implies deficit-driven growth,
there is a unique invariant measure to which the portfolio converges ergodically (in distribution). This in particular means that pathwise time-averages of
any well-behaved (measurable) portfolio metrics in such a system recover the
corresponding functionals of the steady-state distribution.

### 3.4 Invariant Mean State

Return to the normalized, linear SRE:

|  |  |  |
| --- | --- | --- |
|  | Y~t=B~t​Y~t−1+d~t\tilde{{Y}}\_{t}=\tilde{B}\_{t}\tilde{{Y}}\_{t-1}+\tilde{d}\_{t} |  |

Assuming Φ<1\Phi<1 such that we have ergodic convergence, because B~t\tilde{B}\_{t} is independent of Y~t\tilde{Y}\_{t}, the invariant mean satisfies

|  |  |  |
| --- | --- | --- |
|  | E​(Y~)=(I−E​(B~))−1​E​(d~)E(\tilde{Y})=(I-E(\tilde{B}))^{-1}E(\tilde{d}) |  |

Here and below we may (due to invariance of Yt~\tilde{Y\_{t}} and stationarity of D~t\tilde{D}\_{t}, rtr\_{t}) suppress dependence on tt.

This system for E​(Y~)E(\tilde{Y}) is similar to the deterministic
baseline system of section [2](https://arxiv.org/html/2602.19892v1#S2 "2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure"). By its form, E​(B~)E(\tilde{B}) is the companion matrix for the deterministic system, with rates replaced by their means r¯j\bar{r}\_{j}. However,
E​(d~)E(\tilde{d}) includes interaction between rates and deficits. Recall d~=D~​R′​f\tilde{d}=\tilde{D}R^{\prime}f where R′R^{\prime} depends on rates, having the form

|  |  |  |
| --- | --- | --- |
|  | R′=(IR):=(IU⋅d​i​a​g​(r))R^{\prime}=\begin{pmatrix}I\\ R\end{pmatrix}:=\begin{pmatrix}I\\ U\cdot diag({r})\end{pmatrix} |  |

Thus

|  |  |  |
| --- | --- | --- |
|  | E​(d~)=(D0¯​IU⋅d​i​a​g​(D¯0​r¯+Σ))​f=D¯0​R¯Σ′​f,E(\tilde{d})=\begin{pmatrix}\bar{D\_{0}}I\\ U\cdot diag(\bar{D}\_{0}\bar{r}+\Sigma)\end{pmatrix}f=\bar{D}\_{0}\bar{R}^{\prime}\_{\Sigma}f, |  |

recalling that Σj=ρ​ς​σj\Sigma\_{j}=\rho\varsigma\sigma\_{j} is the covariance between D~\tilde{D} and rjr\_{j}, and writing

|  |  |  |
| --- | --- | --- |
|  | R¯Σ′=(IR¯Σ):=(IU​d​i​a​g​(r¯+Σ/D¯0))\bar{R}^{\prime}\_{\Sigma}=\begin{pmatrix}I\\ \bar{R}\_{\Sigma}\end{pmatrix}:=\begin{pmatrix}I\\ Udiag(\bar{r}+\Sigma/\bar{D}\_{0})\end{pmatrix} |  |

The inverse operator (I−E​(B~))−1(I-E(\tilde{B}))^{-1} can be represented directly due to
the form of B~\tilde{B}. Recall B~=γ−1​B\tilde{B}=\gamma^{-1}B where BB has the form of a rank-one update to a (doubled) shift operator,

|  |  |  |
| --- | --- | --- |
|  | B=S′+(R′​f)​eTB=S^{\prime}+(R^{\prime}f)e^{T} |  |

The sustainability condition Φ​(γ,r¯,f)<1\Phi(\gamma,\bar{r},f)<1 allows use of the Sherman-Morrison formula, in this context leading to
the explicit formula for the inverse,

|  |  |  |
| --- | --- | --- |
|  | (I−E​(B~))−1=T′​(I+11−Φ​R¯′​f​γ−1​h2T)(I-E(\tilde{B}))^{-1}=T^{\prime}\left(I+\frac{1}{1-\Phi}\bar{R}^{\prime}f\gamma^{-1}h\_{2}^{T}\right) |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | R¯′\displaystyle\bar{R}^{\prime} | =(I,E​(R))T=(I,U​d​i​a​g​(r¯))T,\displaystyle=(I,E(R))^{T}=(I,Udiag(\bar{r}))^{T}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | U\displaystyle U | is the upper-triangular matrix of 1s,\displaystyle\text{ is the upper-triangular matrix of 1s}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h2T\displaystyle h\_{2}^{T} | :=(hT,hT),\displaystyle:=(h^{T},h^{T}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h\displaystyle h | :=(1,γ−1,…,γ−(M−1))T,and\displaystyle:=(1,\gamma^{-1},\dots,\gamma^{-(M-1)})^{T},\text{and} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | T′\displaystyle T^{\prime} | :=(1−γ−1​S′)−1.\displaystyle:=(1-\gamma^{-1}S^{\prime})^{-1}. |  |

T′T^{\prime} in turn has the block-Toeplitz form

|  |  |  |
| --- | --- | --- |
|  | T′=(T00T),T=(1γ−1γ−2…01γ−1…001…⋮)T^{\prime}=\begin{pmatrix}T&0\\ 0&T\end{pmatrix},\quad\quad T=\begin{pmatrix}1&\gamma^{-1}&\gamma^{-2}&\dots\\ 0&1&\gamma^{-1}&\dots\\ 0&0&1&\dots\\ \vdots&&&\end{pmatrix} |  |

(The latter identity can be established by writing T=I+γ−1​S+⋯+γ−(M−1)​SM−1T=I+\gamma^{-1}S+\dots+\gamma^{-(M-1)}S^{M-1} and noting (I−γ−1​S)​T(I-\gamma^{-1}S)T is a telescoping sum, with the final term vanishing because SM=0S^{M}=0.)
Thus also h=TT​e1h=T^{T}e\_{1}.

The expected normalized state E​(Y~)E(\tilde{Y}) is then

|  |  |  |
| --- | --- | --- |
|  | E​(Y~)=(I−E​(B~))−1​E​(d~)=T′​(I+11−Φ​R¯′​f​γ−1​h2T)⋅D¯0​R¯Σ′​fE(\tilde{Y})=(I-E(\tilde{B}))^{-1}E(\tilde{d})=T^{\prime}\left(I+\frac{1}{1-\Phi}\bar{R}^{\prime}f\gamma^{-1}h\_{2}^{T}\right)\cdot\bar{D}\_{0}\bar{R}^{\prime}\_{\Sigma}f |  |

Note that γ−1​h2T​R¯Σ′​f=Φ​(r¯Σ)\gamma^{-1}h\_{2}^{T}\bar{R}^{\prime}\_{\Sigma}f=\Phi(\bar{r}\_{\Sigma}), where r¯Σ:=r¯+Σ/D¯0\bar{r}\_{\Sigma}:=\bar{r}+\Sigma/\bar{D}\_{0}, and factor it out of the second term. We find

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(Y~)\displaystyle E(\tilde{Y}) | =D¯0​T′​R¯Σ′​f+D¯0​Φ​(r¯Σ)1−Φ​(r¯)​T′​R¯′​f\displaystyle=\bar{D}\_{0}T^{\prime}\bar{R}^{\prime}\_{\Sigma}f+\bar{D}\_{0}\frac{\Phi(\bar{r}\_{\Sigma})}{1-\Phi(\bar{r})}T^{\prime}\bar{R}^{\prime}f |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =D¯01−Φ​(r¯)​T′​((1−Φ​(r¯))​R¯Σ′+Φ​(r¯Σ)​R¯′)​f.\displaystyle=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}T^{\prime}\left((1-\Phi(\bar{r}))\bar{R}^{\prime}\_{\Sigma}+\Phi(\bar{r}\_{\Sigma})\bar{R}^{\prime}\right)f. |  | (13) |

This demonstrates the expected debt-state as a linear transformation of the issuance vector ff. This transform is a linear
combination of the maturity/interest rate cumulative operators R¯′,R¯Σ′\bar{R}^{\prime},\bar{R}^{\prime}\_{\Sigma}, multiplied by the
discounting matrix T′T^{\prime} (which discounts periodwise by γ−1\gamma^{-1}). It also scales up with the normalized
expected-deficit level D¯0\bar{D}\_{0} and varies inversely with how close the average feedback Φ​(r¯)\Phi(\bar{r}) is to 11.

Note in particular that if Σ→0\Sigma\to 0 (recovering the deterministic case), so that
r¯Σ→r¯\bar{r}\_{\Sigma}\to\bar{r}
and R¯Σ→R¯\bar{R}\_{\Sigma}\to\bar{R}, this expression collapses to E​(Y~)=D¯01−Φ​(r¯)​T′​R¯′​fE(\tilde{Y})=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}T^{\prime}\bar{R}^{\prime}f, which is easily seen to be equivalent to the deterministic steady-state of
section [2](https://arxiv.org/html/2602.19892v1#S2 "2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") in future-cashflow representation, using r¯\bar{r} as the steady interest rate assumption. Expression [13](https://arxiv.org/html/2602.19892v1#S3.E13 "In 3.4 Invariant Mean State ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") therefore
has the following intuitive interpretation:

###### Proposition 3.2 (Stochastic Invariant Mean).

The invariant mean state of SRE ([11](https://arxiv.org/html/2602.19892v1#S3.E11 "In 3.3 Normalized Linear SRE and Ergodic Convergence ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")), if the sustainability condition is satisfied, is
given by ([13](https://arxiv.org/html/2602.19892v1#S3.E13 "In 3.4 Invariant Mean State ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) and differs from
the deterministic baseline of section [2](https://arxiv.org/html/2602.19892v1#S2 "2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") (using average deficits/rates) by a correction term that depends
linearly
on the correlation between interest rates and deficits.

The invariant mean state E​(Y~)E(\tilde{Y}) can be helpful in characterizing various steady portfolio metrics, analogous to those developed
in section [2](https://arxiv.org/html/2602.19892v1#S2 "2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure").

### 3.5 Invariant Maturity Distribution

The invariant maturity distribution of SRE ([11](https://arxiv.org/html/2602.19892v1#S3.E11 "In 3.3 Normalized Linear SRE and Ergodic Convergence ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) is obtained from the principal portion of E​(Y~)E(\tilde{Y}), which are just its first MM elements:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(q~)\displaystyle E(\tilde{q}) | :=(I,0)​E​(Y~)=D¯01−Φ​(r¯)​(I,0)​T′​((1−Φ​(r¯))​R¯Σ′+Φ​(r¯Σ)​R¯′)​f\displaystyle:=(I,0)E(\tilde{Y})=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}(I,0)T^{\prime}\left((1-\Phi(\bar{r}))\bar{R}^{\prime}\_{\Sigma}+\Phi(\bar{r}\_{\Sigma})\bar{R}^{\prime}\right)f |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =D¯0​(1−Φ​(r¯)+Φ​(r¯Σ))1−Φ​(r¯)​T​f\displaystyle=\frac{\bar{D}\_{0}(1-\Phi(\bar{r})+\Phi(\bar{r}\_{\Sigma}))}{1-\Phi(\bar{r})}Tf |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =D¯01−Φ​(r¯)​(1+hT​U​d​i​a​g​(Σ/D¯0)​f)​T​f.\displaystyle=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}\left(1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f\right)Tf. |  |

where we have used (I,0)​T′=(T,0)(I,0)T^{\prime}=(T,0) and (T,0)​R¯′=(T,0)​R¯Σ′=I(T,0)\bar{R}^{\prime}=(T,0)\bar{R}^{\prime}\_{\Sigma}=I.

Note that (T​f)j=∑k=jMγ−(k−j)​fk(Tf)\_{j}=\sum\_{k=j}^{M}\gamma^{-(k-j)}f\_{k}.
Comparing with ([5](https://arxiv.org/html/2602.19892v1#S2.E5 "In 2.4 Steady-State Portfolio Shares ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")), we see that the above equation has the same form as the steady normalized debt-levels qjq\_{j} obtained
in the deterministic case, up to a constant (an adjustment that scales with
rate/deficit correlation Σ\Sigma). Since
portfolio shares θ=q~/𝟏T​q~\theta=\tilde{q}/\mathbf{1}^{T}\tilde{q} are normalized debt levels scaled to add to 11, the constant cancels out and plays
no role in θ=q~/𝟏T​q~=T​f/𝟏T​T​f\theta=\tilde{q}/\mathbf{1}^{T}\tilde{q}=Tf/\mathbf{1}^{T}Tf. Thus moving to a stochastic regime with correlated, mean-reverting
rates and deficits has left steady (invariant) portfolio shares unaffected versus the deterministic baseline model.

###### Proposition 3.3 (Invariant Portfolio Shares).

The invariant portfolio shares θ\theta for the stochastic SRE ([11](https://arxiv.org/html/2602.19892v1#S3.E11 "In 3.3 Normalized Linear SRE and Ergodic Convergence ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")), provided the sustainability condition Φ​(γ,r∗,f)<1\Phi(\gamma,r^{\*},f)<1 is satisfied,
are given by the formula for deterministic steady shares in
([7](https://arxiv.org/html/2602.19892v1#S2.E7 "In 2.4 Steady-State Portfolio Shares ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")), which is equivalent to θ=T​f/𝟏T​T​f\theta=Tf/\mathbf{1}^{T}Tf, and are otherwise independent of rates, deficits, or their correlation.

### 3.6 Invariant Rollover Fraction

It also follows from the preceding that the invariant rollover fraction θ1\theta\_{1} is identical to that in the deterministic case, because
the correlation-correction cancels; we write θ1=θ1,b​a​s​e\theta\_{1}=\theta\_{1,base}
where θ1,b​a​s​e\theta\_{1,base} is given in equation ([9](https://arxiv.org/html/2602.19892v1#S2.E9 "In 2.6 Steady Rollover Fraction ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")):

|  |  |  |
| --- | --- | --- |
|  | θ1=θ1,b​a​s​e=∑j=1Mwj​τj,τj=(γ−1)/(γj−1),wj=fj​(1−γ−j)/∑kfk​(1−γ−k).\theta\_{1}=\theta\_{1,base}=\sum\_{j=1}^{M}w\_{j}\tau\_{j},\quad\tau\_{j}=(\gamma-1)/(\gamma^{j}-1),\quad w\_{j}=f\_{j}(1-\gamma^{-j})/\sum\_{k}f\_{k}(1-\gamma^{-k}). |  |

### 3.7 Invariant Debt Level

The total (normalized) debt outstanding, in the invariant steady state, is the summed entries of E​(q)E(q);

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(Q~)=𝟏T​E​(q~)=D¯01−Φ​(r¯)​(1+hT​U​d​i​a​g​(Σ/D¯0)​f)​𝟏T​T​f.E(\tilde{Q})=\mathbf{1}^{T}E(\tilde{q})=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}\left(1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f\right)\mathbf{1}^{T}Tf. |  | (14) |

Comparing with ([6](https://arxiv.org/html/2602.19892v1#S2.E6 "In 2.4 Steady-State Portfolio Shares ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) and ([7](https://arxiv.org/html/2602.19892v1#S2.E7 "In 2.4 Steady-State Portfolio Shares ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")), and
noting
(𝟏T​T)k=∑j=0k−1γ−j=1−γ−k1−γ−1(\mathbf{1}^{T}T)\_{k}=\sum\_{j=0}^{k-1}\gamma^{-j}=\frac{1-\gamma^{-k}}{1-\gamma^{-1}}, we see that the steady debt level for the SRE
formulation again differs from that for the deterministic baseline Q~b​a​s​e:=D¯01−Φ​(r¯)​𝟏T​T​f\tilde{Q}\_{base}:=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}\mathbf{1}^{T}Tf only by the correlation-linked scale
factor 1+hT​U​d​i​a​g​(Σ/D¯0)​f1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f.

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(Q~)\displaystyle E(\tilde{Q}) | =(1+hT​U​d​i​a​g​(Σ/D¯0)​f)​Q~b​a​s​e\displaystyle=(1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f)\tilde{Q}\_{base} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1+1D¯0​∑j=1M(1−γ−j1−γ−1)​fj​Σj)​Q~b​a​s​e.\displaystyle=\left(1+\frac{1}{\bar{D}\_{0}}\sum\_{j=1}^{M}\left(\frac{1-\gamma^{-j}}{1-\gamma^{-1}}\right)f\_{j}\Sigma\_{j}\right)\tilde{Q}\_{base}. |  |

When Σ=0\Sigma=0 this factor is just 11 and the deterministic baseline is recovered. Recalling
that Σj=ρ​ς​σj\Sigma\_{j}=\rho\varsigma\sigma\_{j}, the effect of correlation ρ\rho is
straightforward: if ρ<0\rho<0 (ρ>0\rho>0) then the normalized steady debt level E​(Q~)E(\tilde{Q}) is reduced (increased) from the deterministic baseline.

In particular, for the economically-realistic case ρ<0\rho<0, in which rates tend to be lower in times of higher deficits and vice versa, this model implies
a lower steady debt-level E​(Q~)<Q~b​a​s​eE(\tilde{Q})<\tilde{Q}\_{base} all else equal, as intuition would suggest.

### 3.8 Invariant Interest Cost and Ratio

The expected next-period (normalized) interest cost is given by the M+1M+1st element of E​(Y~)E(\tilde{Y}), which can be obtained by multiplying by
(0T,e1T)(0^{T},e\_{1}^{T}). Noting

|  |  |  |
| --- | --- | --- |
|  | (0T,e1T)​T′=(0T,e1T)​(T00T)=(0T​e1T​T)=(0T​hT),(0^{T},e\_{1}^{T})T^{\prime}=(0^{T},e\_{1}^{T})\begin{pmatrix}T&0\\ 0&T\end{pmatrix}=(0^{T}e\_{1}^{T}T)=(0^{T}h^{T}), |  |

we find

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​(I~)\displaystyle E(\tilde{I}) | =D¯01−Φ​(r¯)​(0,hT)​((1−Φ​(r¯))​R¯Σ′+Φ​(r¯Σ)​R¯′)​f\displaystyle=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}(0,h^{T})\left((1-\Phi(\bar{r}))\bar{R}^{\prime}\_{\Sigma}+\Phi(\bar{r}\_{\Sigma})\bar{R}^{\prime}\right)f |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =D¯01−Φ​(r¯)​hT​U​((1−Φ​(r¯))​d​i​a​g​(r¯+Σ/D¯0)+Φ​(r¯Σ)​d​i​a​g​(r¯))​f\displaystyle=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}h^{T}U\left((1-\Phi(\bar{r}))diag(\bar{r}+\Sigma/\bar{D}\_{0})+\Phi(\bar{r}\_{\Sigma})diag(\bar{r})\right)f |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =D¯01−Φ​(r¯)​hT​U​(d​i​a​g​(r¯)+(1−Φ​(r¯))​d​i​a​g​(Σ/D¯0)+(Φ​(r¯Σ)−Φ​(r¯))​d​i​a​g​(r¯))​f\displaystyle=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}h^{T}U\left(diag(\bar{r})+(1-\Phi(\bar{r}))diag(\Sigma/\bar{D}\_{0})+(\Phi(\bar{r}\_{\Sigma})-\Phi(\bar{r}))diag(\bar{r})\right)f |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =D¯01−Φ​(r¯)​hT​U​(d​i​a​g​(r¯)+(1−Φ​(r¯))​d​i​a​g​(Σ/D¯0)+(Φ​(Σ/D¯0)−Φ​(0))​d​i​a​g​(r¯))​f.\displaystyle=\frac{\bar{D}\_{0}}{1-\Phi(\bar{r})}h^{T}U\left(diag(\bar{r})+(1-\Phi(\bar{r}))diag(\Sigma/\bar{D}\_{0})+(\Phi(\Sigma/\bar{D}\_{0})-\Phi(0))diag(\bar{r})\right)f. |  | (18) |

The contribution here involving hT​U​d​i​a​g​(r¯)​fh^{T}Udiag(\bar{r})f, after normalizing by portfolio size, equates to the
steady interest cost for deterministic issuance with interest rates r¯\bar{r} (compare
equation ([8](https://arxiv.org/html/2602.19892v1#S2.E8 "In 2.5 Steady Interest-Cost Ratio ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure"))). The other terms are correlation corrections that depend linearly on Σ\Sigma. We can thus write

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(I~)\displaystyle E(\tilde{I}) | =Ib​a​s​e​(D¯0,r¯)+11−Φ​(r¯)​hT​U​((1−Φ​(r¯))​d​i​a​g​(Σ)+(Φ​(Σ)−Φ​(0))​d​i​a​g​(r¯))​f\displaystyle=I\_{base}(\bar{D}\_{0},\bar{r})+\frac{1}{1-\Phi(\bar{r})}h^{T}U\left((1-\Phi(\bar{r}))diag(\Sigma)+(\Phi(\Sigma)-\Phi(0))diag(\bar{r})\right)f |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Ib​a​s​e​(D¯0,r¯)+11−Φ​(r¯)​∑j=1M(1−γ−j1−γ−1)​fj​((1−Φ​(r¯))​Σj+(Φ​(Σ)−Φ​(0))​r¯j)\displaystyle=I\_{base}(\bar{D}\_{0},\bar{r})+\frac{1}{1-\Phi(\bar{r})}\sum\_{j=1}^{M}(\frac{1-\gamma^{-j}}{1-\gamma^{-1}})f\_{j}\left((1-\Phi(\bar{r}))\Sigma\_{j}+(\Phi(\Sigma)-\Phi(0))\bar{r}\_{j}\right) |  |

To gauge the interest cost ratio we can divide by the steady (normalized) portfolio size E​(Q~)E(\tilde{Q}) (see previous section). This gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(I~)E​(Q~)\displaystyle\frac{E(\tilde{I})}{E(\tilde{Q})} | =Ib​a​s​e+11−Φ​(r¯)​hT​U​((1−Φ​(r¯))​d​i​a​g​(Σ)+(Φ​(Σ)−Φ​(0))​d​i​a​g​(r¯))​f(1+hT​U​d​i​a​g​(Σ/D¯0)​f)​Q~b​a​s​e\displaystyle=\frac{I\_{base}+\frac{1}{1-\Phi(\bar{r})}h^{T}U((1-\Phi(\bar{r}))diag(\Sigma)+(\Phi(\Sigma)-\Phi(0))diag(\bar{r}))f}{(1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f)\tilde{Q}\_{base}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =11+hT​U​d​i​a​g​(Σ/D¯0)​f​(IQ)b​a​s​e+\displaystyle=\frac{1}{1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f}\left(\frac{I}{Q}\right)\_{base}+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | hT​U​((1−Φ​(r¯))​d​i​a​g​(Σ)+(Φ​(Σ)−Φ​(0))​d​i​a​g​(r¯))​f(1−Φ​(r¯))​(1+hT​U​d​i​a​g​(Σ/D¯0)​f)​Q~b​a​s​e\displaystyle\frac{h^{T}U\left((1-\Phi(\bar{r}))diag(\Sigma)+(\Phi(\Sigma)-\Phi(0))diag(\bar{r})\right)f}{(1-\Phi(\bar{r}))(1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f)\tilde{Q}\_{base}} |  |

Unlike in the deterministic case this is a nonlinear expression in issuance policy ff, and
its dependence on covariance Σ\Sigma may be complex and depends on the precise structure of Σ\Sigma and r¯\bar{r}.
But it is easy to see that
as Σ→0\Sigma\to 0 it reduces to the baseline expression I~b​a​s​e/Q~b​a​s​e=W​A​Cd​e​t\tilde{I}\_{base}/\tilde{Q}\_{base}=WAC\_{det}, whose formula given in ([8](https://arxiv.org/html/2602.19892v1#S2.E8 "In 2.5 Steady Interest-Cost Ratio ‣ 2 Deterministic Baseline ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")).

The deviation from the baseline is evidently not a simple linear function of Σ\Sigma.
[TODO: analyze how this depends on Σ\Sigma/r​h​orho better]

### 3.9 Implications for Issuance Policy Optimization

The ratio E​(I~)/E​(Q~)E(\tilde{I})/E(\tilde{Q}), which was used in the deterministic case, is arguably not the best indicator of interest cost in this stochastic
context. In practice (e.g. numerical models) it is probably more
common to track the ratio It/QtI\_{t}/Q\_{t}, thus ideally one would calculate E​(I~/Q~)=E​(I/Q)E(\tilde{I}/\tilde{Q})=E(I/Q) to gauge the invariant average interest cost associated
with numerical metrics. A
closed-form formula for E​(I/Q)E(I/Q) in this framework
may be unwieldly here; it evidently differs from
E​(I~)/E​(Q~)E(\tilde{I})/E(\tilde{Q}) by a Jensen effect due to convexity of 1/x1/x, and by the covariance between II and QQ (presumably positive), both effects of which
ought to lead to
E​(I/Q)>E​(I~)/E​(Q~)E(I/Q)>E(\tilde{I})/E(\tilde{Q}). The consequence is that the interest cost ratio developed above is likely to be an underestimate of interest-cost ratios
evaluated empriically and reported in a
stochastic debt-simulation setting.

However, for modest values of ρ\rho it may be possible to treat this effect as negligible, or use a first-order expansion in ρ\rho, to characterize the invariant interest cost ratio. This distinction also might have little effect
on conclusions drawn about the relative cost impact of nearby issuance strategies ff.

One might also target either I~\tilde{I} by itself (the steady
normalized interest cost) or Q~\tilde{Q} as the target metrics to gauge the cost impact of fiscal policy. While in
the deterministic case there was no mathematical difference between targeting W​A​CWAC and Q~\tilde{Q} for optimization purposes, in the stochastic
case these can differ.

These considerations suggest one of the following approaches to
incorporating the stochastic, correlated framework into the earlier optimization problem. For the
metrics:

Invariant (normalized) interest cost:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(I~)​(f)=\displaystyle E(\tilde{I})(f)= | I~b​a​s​e​(D¯0,r¯;f)+\displaystyle\tilde{I}\_{base}(\bar{D}\_{0},\bar{r};f)+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 11−Φ​(r¯)​hT​U​((1−Φ​(r¯))​d​i​a​g​(Σ)+(Φ​(Σ)−Φ​(0))​d​i​a​g​(r¯))​f\displaystyle\frac{1}{1-\Phi(\bar{r})}h^{T}U\left((1-\Phi(\bar{r}))diag(\Sigma)+(\Phi(\Sigma)-\Phi(0))diag(\bar{r})\right)f |  |

Invariant (normalized) debt level:

|  |  |  |
| --- | --- | --- |
|  | E​(Q~)​(f)=(1+hT​U​d​i​a​g​(Σ/D¯0)​f)​Q~b​a​s​e​(D¯0,r¯;f)E(\tilde{Q})(f)=(1+h^{T}Udiag(\Sigma/\bar{D}\_{0})f)\tilde{Q}\_{base}(\bar{D}\_{0},\bar{r};f) |  |

Invariant interest-cost ratio:

|  |  |  |
| --- | --- | --- |
|  | E​(I~)​(f)/E​(Q~)​(f)E(\tilde{I})(f)/E(\tilde{Q})(f) |  |

Steady rollover ratio:

|  |  |  |
| --- | --- | --- |
|  | θ1=θ1​(f)=θ1,b​a​s​e​(f),\theta\_{1}=\theta\_{1}(f)=\theta\_{1,base}(f), |  |

and given a rollover-ratio tolerance R∈(0,1)R\in(0,1),

|  |  |  |
| --- | --- | --- |
|  | minimize ​E​(Q~)​(f)​ subject to ​θ1​(f)≤R,0≤f≤1,𝟏T​f=1.\text{minimize }E(\tilde{Q})(f)\text{ subject to }\theta\_{1}(f)\leq R,\quad 0\leq f\leq 1,\quad\mathbf{1}^{T}f=1. |  |

or

|  |  |  |
| --- | --- | --- |
|  | minimize ​E​(I~)​(f)​ subject to ​θ1​(f)≤R,0≤f≤1,𝟏T​f=1.\text{minimize }E(\tilde{I})(f)\text{ subject to }\theta\_{1}(f)\leq R,\quad 0\leq f\leq 1,\quad\mathbf{1}^{T}f=1. |  |

or

|  |  |  |
| --- | --- | --- |
|  | minimize E(I~)(f)/E(Q~(f) subject to θ1(f)≤R,0≤f≤1,𝟏Tf=1.\text{minimize }E(\tilde{I})(f)/E(\tilde{Q}(f)\text{ subject to }\theta\_{1}(f)\leq R,\quad 0\leq f\leq 1,\quad\mathbf{1}^{T}f=1. |  |

Above, while I~b​a​s​e\tilde{I}\_{base} and Q~b​a​s​e\tilde{Q}\_{base} are linear in ff, their stochastic counterparts are not. So (unlike the deterministic
baseline) these objection functions do not in general lead to a linear programming problem.
However, they are nevertheless amenable to fast solutions using sequential quadratic programming or similar methods.

Also note that for realistically-modest choices of Σ\Sigma, the relative deviations of these metrics from their deterministic counterparts I~b​a​s​e\tilde{I}\_{base} and Q~b​a​s​e\tilde{Q}\_{base} are small. This suggests that
scenario-analyses of or optimization solutions for ff will be well-approximated by and only small adjustments to the deterministic baseline metrics.

### 3.10 Second-Moment And Other Metrics

While this piece focuses on first‑moment objects - such as the invariant mean of the future‑cashflow state and the resulting expressions for expected debt levels and interest cost - in a
Gaussian context the
same linear structure also delivers a well‑defined characterization of second moments. In particular, the centered state Z~t:=Y~t−E​(Y)\tilde{Z}\_{t}:=\tilde{Y}\_{t}-E(Y) satisfies a linear stochastic recurrence whose invariant covariance
C=E​(Z~t​Z~tT)C=E(\tilde{Z}\_{t}\tilde{Z}\_{t}^{T}) solves a standard Lyapunov equation of the form

|  |  |  |
| --- | --- | --- |
|  | v​e​c​(C)=(I−E​[B~t⊗B~tT])−1​v​e​c​(Gξ)vec(C)=\left(I-E[\tilde{B}\_{t}\otimes\tilde{B}\_{t}^{T}]\right)^{-1}vec(G\_{\xi}) |  |

where for ξt:=d~t−E​(d)+(B~t−E​(B))​E​(Y)\xi\_{t}:=\tilde{d}\_{t}-E(d)+(\tilde{B}\_{t}-E(B))E(Y), Gξ=E​(ξt​ξtT)G\_{\xi}=E(\xi\_{t}\xi\_{t}^{T}) is the covariance of the one‑step innovation. All components of this operator equation are
explicit functions of the means and covariances of the exogenous macro processes, and the system is numerically tractable for realistic maturity dimensions.

Similarly, tail-risk measures of the invariant distribution such as CDaR/CFaR (conditional debt-/financing-at-risk) could reduce to closed-form formulas in a Gaussian context.

A fuller
development
of these second‑moment and tail‑risk implications within this model framework is left for future work.

## 4 Numerical Examples

In this section we present illustrative examples of expected invariant metrics and stochastic simulations under
specific parameter-choices for our normalized-debt SRE.

### 4.1 Baseline parameters and metrics

Table [1](https://arxiv.org/html/2602.19892v1#S4.T1 "Table 1 ‣ 4.1 Baseline parameters and metrics ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") presents the parameters for a baseline debt-dynamics simulation. For simplicity, we assume a rolling debt-issuance policy
using three tenors (to represent short/medium/long), j=1,3,10j=1,3,10.

Table 1: Baseline Debt-Dynamics SRE Parameters

| Section | Item | Symbol | Value |
| --- | --- | --- | --- |
| Key Tenors | Issuance tenors | jj | 1,3,101,3,10 |
| Issuance Allocation |  | f1f\_{1} | 0.4 |
| New-issuance allocation | f3f\_{3} | 0.5 |
|  | f10f\_{10} | 0.1 |
| Interest Rates |  |  | .02 |
| Mean interest rates | r¯\bar{r} | .03 |
|  |  | .05 |
| Rate volatility | σ\sigma | 0.1×r¯0.1\times\bar{r} |
| Rate persistence | ϕ\phi | 0.980.98 |
| Deficits | Asymptotic deficit-growth rate | gg | .08.08 |
| Deficit-growth factor | γ\gamma | 1.081.08 |
| Mean normalized deficit | D¯0\bar{D}\_{0} | 11 |
| Normalized-deficit volatility | ς\varsigma | 0.1×D¯0=0.10.1\times\bar{D}\_{0}=0.1 |
| Deficit persistence | ψ\psi | 0.980.98 |
| Correlation | Scalar rate-deficit correlation | ρ\rho | −0.5-0.5 |

We can also immediately compute from these
parameters our key invariant metrics, using the formulas ([12](https://arxiv.org/html/2602.19892v1#S3.E12 "In 3.3 Normalized Linear SRE and Ergodic Convergence ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")), ([14](https://arxiv.org/html/2602.19892v1#S3.E14 "In 3.7 Invariant Debt Level ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")) and ([18](https://arxiv.org/html/2602.19892v1#S3.E18 "In 3.8 Invariant Interest Cost and Ratio ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure"))
developed above. The results are presented in Table [2](https://arxiv.org/html/2602.19892v1#S4.T2 "Table 2 ‣ 4.1 Baseline parameters and metrics ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure"). Note we include the calculated
feedback-function to confirm Φ<1\Phi<1 for ergodic convergence. (In Table [2](https://arxiv.org/html/2602.19892v1#S4.T2 "Table 2 ‣ 4.1 Baseline parameters and metrics ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") we approximated this
by using r¯\bar{r}
rather than r∗:=E​(|r|)r^{\*}:=E(|r|) to compute Φ\Phi, but the difference is negligible for the rate volatilities σj\sigma\_{j} assumed.)

Table 2: Selected invariant metrics of baseline SRE.

| Metric | Symbol | Value |
| --- | --- | --- |
| Feedback function | Φ​(γ,r∗,f)\Phi(\gamma,r^{\*},{f}) | ≈0.9061\approx 0.9061 |
| Expected normalized debt-level | E​(Q)E(Q) | 26.787126.7871 |
| Expected next-period interest cost | E​(I)E(I) | 1.063601.06360 |
| Invariant interest cost ratio | E​(I)/E​(Q)E(I)/E(Q) | 0.03970.0397 |
| Invariant 1-period rollover fraction | θ1=E​(q1/Q)\theta\_{1}=E(q\_{1}/Q) | 0.34920.3492 |

Finally, for numerical and Monte Carlo estimation we simulated the SRE-defined debt dynamics (in normalized form, i.e. equation ([11](https://arxiv.org/html/2602.19892v1#S3.E11 "In 3.3 Normalized Linear SRE and Ergodic Convergence ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure")))
using the parameters shown in Table [3](https://arxiv.org/html/2602.19892v1#S4.T3 "Table 3 ‣ 4.1 Baseline parameters and metrics ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure").

Table 3: Monte Carlo simulation parameters.

| Parameter | Value |
| --- | --- |
| Number of periods (simulation horizon) | 100100 |
| Number of paths (realizations) | 500500 |

### 4.2 Single-path examples

Figure [2](https://arxiv.org/html/2602.19892v1#S4.F2 "Figure 2 ‣ 4.2 Single-path examples ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") depicts QtQ\_{t} and ItI\_{t} (on dual-axis) for a single realization of the normalized SRE
to a horizon of t=100t=100, along with
the known invariant means E​(Q)E(Q) and E​(I)E(I) as dotted lines. This illustrates fluctuation around
the theoretical invariant distribution intrinsic to the system. The speed of convergence and size of the fluctuations of course
will depend on the stochastic parameters i.e. interest-rate/deficit volatility and persistence.

![Refer to caption](sim_1path.png)


Figure 2: Illustrative
single-path realization of QtQ\_{t} and ItI\_{t} (left- and right-axis, respectively) to t=100t=100 of the baseline
normalized SRE, along with their means E​(Q)E(Q) and E​(I)E(I) (dotted lines).

Figure [3](https://arxiv.org/html/2602.19892v1#S4.F3 "Figure 3 ‣ 4.2 Single-path examples ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") demonstrates a single realization of the one-period rollover ratio (Q1/Q)t(Q\_{1}/Q)\_{t}, showing that it very rapidly
settles near its theoretical long-term value.

![Refer to caption](sim_1theta1.png)


Figure 3: Single-path realization of the one-period rollover fraction (Q1/Q)t(Q\_{1}/Q)\_{t} along with its invariant mean θ1\theta\_{1} (dotted line).

### 4.3 Time averages and ergodicity

Figure [4](https://arxiv.org/html/2602.19892v1#S4.F4 "Figure 4 ‣ 4.3 Time averages and ergodicity ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") depicts the ergodicity by plotting the time-averages ∑1TQt/T\sum\_{1}^{T}Q\_{t}/T and ∑1TIt/T\sum\_{1}^{T}I\_{t}/T against
TT from various randomly-chosen initial conditions. Convergence to the analytical E​(Q)E(Q) and E​(I)E(I) is apparent.

![Refer to caption](timeAvgs.png)


Figure 4: Time-averages ∑Qt/T\sum Q\_{t}/T and ∑It/T\sum I\_{t}/T vs. TT
of QtQ\_{t} and ItI\_{t} respectively from various randomly-chosen initial conditions, along with the ergodic
means E​(Q)E(Q) and E​(I)E(I) (dotted lines).

### 4.4 Distribution of simulated metrics

Figure [5](https://arxiv.org/html/2602.19892v1#S4.F5 "Figure 5 ‣ 4.4 Distribution of simulated metrics ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure"),  [6](https://arxiv.org/html/2602.19892v1#S4.F6 "Figure 6 ‣ 4.4 Distribution of simulated metrics ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") and [7](https://arxiv.org/html/2602.19892v1#S4.F7 "Figure 7 ‣ 4.4 Distribution of simulated metrics ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") depict
fan-charts of the empirical distributions of QtQ\_{t}, ItI\_{t} and the one-period rollover ratio (Q1/Q)t(Q\_{1}/Q)\_{t} (respectively)
based on 15th and 85th percentiles, along with their medians, across the 500500 realizations. The theoretical
expectations E​(Q)E(Q), E​(I)E(I) and θ1=E​(Q1/Q)\theta\_{1}=E(Q\_{1}/Q) are again shown as dotted-lines. (In the latter case the distribution of
the rollover ratio apparently rapidly becomes
very tightly bound to θ1\theta\_{1}.)

![Refer to caption](sim_fanQ.png)


Figure 5: Fan-chart of 15th to 85th percentile of realized QtQ\_{t} paths, along with median (solid line) and theoretical E​(Q)E(Q) (dotted line).

![Refer to caption](sim_fanI.png)


Figure 6: Fan-chart of 15th to 85th percentile of realized ItI\_{t} paths, along with median (solid line) and theoretical E​(I)E(I) (dotted line).

![Refer to caption](sim_fanTheta.png)


Figure 7: Fan-chart of 15th to 85th percentile of realized (Q1/Q)t(Q\_{1}/Q)\_{t} paths, along with median (solid line) and theoretical θ1=E​(Q1/Q)\theta\_{1}=E(Q\_{1}/Q) (dotted line).

It is seen that the empirically-estimated metrics from Monte Carlo simulation bracket the true invariant expectations, as expected.

### 4.5 Cost vs. risk

Figure [8](https://arxiv.org/html/2602.19892v1#S4.F8 "Figure 8 ‣ 4.5 Cost vs. risk ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") presents a scatterplot of an ergodic-mean cost proxy E​(I)/E​(Q)E(I)/E(Q) vs. risk proxy θ1\theta\_{1} (the one-period
rollover fraction), as well as
Monte Carlo approximations to these from a N=500N=500 empirical simulation, for various representative choices of issuance
allocations f=(f1,f3,f10)Tf=(f\_{1},f\_{3},f\_{10})^{T}. These include the short/belly/long-tiled allocations depicted previously, as well as the baseline
allocation f=(0.4,0.5,0.1)Tf=(0.4,0.5,0.1)^{T} of this section.

One can see the close agreement between the results of forward-simulation and the analytical ergodic-mean formulas.

![Refer to caption](costVrisk.png)


Figure 8: Theoretical and simulated cost- vs. risk-proxy scatterplot for various new-issuance allocations. Allocations shown indicate the
percentage of new-issuance at the 1-, 3-, and 10-year tenors respectively. Here cost is
proxied by E​(I)/E​(Q)E(I)/E(Q) (expected normalized next-period interest vs. normalized debt-level), and risk is proxied by
E​(Q1/Q)=θ1E(Q\_{1}/Q)=\theta\_{1}, the expected one-period rollover fraction. Monte Carlo-approximated averages
for N=500N=500 realizations at the t=100t=100 calculation horizon
show close agreement with theoretical ergodic means computable a priori via derived analytical formulae.

### 4.6 Correlation effect

Figure [9](https://arxiv.org/html/2602.19892v1#S4.F9 "Figure 9 ‣ 4.6 Correlation effect ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") illustrates how the interest-cost ratio E​(I)/E​(Q)E(I)/E(Q) varies with the rate-deficit correlation
assumption ρ\rho. One can observe the expected result that a countercyclical policy-rate assumption (i.e. ρ<0\rho<0) leads to a lower
long-term interest-cost ratio all else equal, due to periods of higher deficits tending to coincide with those of lower interest-rates.

![Refer to caption](costVrho.png)


Figure 9: Dependence of the interest-cost ratio E​(I)/E​(Q)E(I)/E(Q) on rate-deficit correlation
assumption ρ\rho. Theoretical and Monte Carlo-approximated results (for N=50000N=50000) are shown.

Note that because the effect was so slight we have increased the number of realizations (N=50000N=50000) to better demonstrate
simulation approximations approaching
the analytical formula. For completeness, Table [4](https://arxiv.org/html/2602.19892v1#S4.T4 "Table 4 ‣ 4.6 Correlation effect ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") reports
the dependence of E​(I)/E​(Q)E(I)/E(Q) on ρ\rho for the baseline parameters and new-issuance allocation f=(0.4,0.5,0.1)Tf=(0.4,0.5,0.1)^{T} of
this section. For the baseline parameters of this section the
effect on expected invariant interest-cost ratio is about 0.040.04 basis-points (i.e. 0.0004%0.0004\%) per 10%10\% increase in ρ\rho.

Table 4: Dependence of interest-cost ratio (E​(I)/E​(Q)E(I)/E(Q)) on rate-deficit correlation assumption (ρ\rho) for baseline
model and new-issuance allocation, showing the expected directional dependence (albeit slight) that reducing ρ\rho decreases interest-cost. The
strength of this relationship could vary with other assumptions of the model such
as assumed new-issuance allocation, deficit growth trend, and the slope of the mean yield-curve.

|  |  |
| --- | --- |
| Rate-deficit correlation, ρ\rho | Invariant interest-cost ratio, E​(I)/E​(Q)E(I)/E(Q) |
| −50%-50\% | 3.9682%3.9682\% |
| −25%-25\% | 3.9691%3.9691\% |
| −0%-0\% | 3.9701%3.9701\% |
| 25%25\% | 3.9710%3.9710\% |
| 50%50\% | 3.9719%3.9719\% |

### 4.7 Optimization calculations

In this section we show results of running the optimization program described in section [3.9](https://arxiv.org/html/2602.19892v1#S3.SS9 "3.9 Implications for Issuance Policy Optimization ‣ 3 Stochastic Extension ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") on our baseline example. For
this exercise we used the simple interest-cost ratio J​(f):=E​(I)/E​(Q)J(f):=E(I)/E(Q) as objective function. (Results of using J​(f)=E​(I)J(f)=E(I) or J​(f)=E​(Q)J(f)=E(Q) were not
materially different.)

To generate a frontier, a maximum is applied to the expected one-period rollover ratio as
risk-proxy, θ1​(f)≤R\theta\_{1}(f)\leq R. A lower-bound of 5%5\% was enforced
on each of f1,f3,f10f\_{1},f\_{3},f\_{10} to avoid trivial corner solutions. The optimal allocations f∗​(R)f^{\*}(R), admissible by this critierion, that minimize
J​(f)J(f) for
R∈(0,0.5]R\in(0,0.5] were computed and are represented in Figure [10](https://arxiv.org/html/2602.19892v1#S4.F10 "Figure 10 ‣ 4.7 Optimization calculations ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure").

![Refer to caption](simpleOpt.png)


Figure 10: Optimal new-issuance allocations ff of baseline model, by maximum constraint on θ1\theta\_{1} and maintaining
f≥0.05f\geq 0.05.

The behavior of this optimization exercise is seen to
follow a ‘waterfall’ pattern familiar from the deterministic baseline model. Generally, absent any constraint (i.e. if RR is large),
optimal allocation would favor shorter borrowing (large f1f\_{1}) to minimize cost, due to the upward-sloping expected
yields r¯\bar{r}. As risk tolerance RR is reduced, the appetite
for f1f\_{1} is reduced, because it leads to too-high rollover θ1\theta\_{1}, until it reaches its minimum (5%5\% in this case).
Allocation toward the ‘belly’ f3f\_{3} becomes favored as a cost-efficient balance. Finally, as RR is reduced further, 33-period borrowing
starts to also be inefficient for satisfying the risk tolerance, and 1010-period borrowing becomes necessary.

Finally, we explored the effect of varying rate-deficit correlation ρ\rho on optimization calculations. To illustrate this potential
dependence, Figure [11](https://arxiv.org/html/2602.19892v1#S4.F11 "Figure 11 ‣ 4.7 Optimization calculations ‣ 4 Numerical Examples ‣ Long-Run Sovereign Debt Composition: An Analytic Ergodic Framework with Explicit Maturity Structure") shows
the optimal-calibrated one-period share f1f\_{1} by ρ\rho for an example case, where the constraint on one-period rollover is R=0.3R=0.3.

Results for all values of RR simulated on optimal fjf\_{j} (where nontrivial i.e. away from a corner solution) were similar. Correlation in this model may
have
a nonzero effect on optimal allocation, but it is evidently not material to issuance policy
for the parameter range governing the baseline example considered in this section.

![Refer to caption](optByRho.png)


Figure 11: Optimal one-period fraction f1f\_{1} in baseline model with rollover constraint R=0.3R=0.3, while varying rate-deficit
correlation assumption ρ\rho. An effect of this magnitude
may be influenced by numerical tolerances of the optimization, and is evidently not material for issuance policy.

## 5 Conclusions

This piece advances the understanding of non-defaulting, regular-issuance sovereign
debt dynamics by integrating a fully granular maturity structure with stochastic, correlated interest-rate
and deficit drivers in a discrete-time,
future-cashflow-representation recursion framework,
and establishing a sustainability-style condition (effectively, a particularized extension of r<gr<g) for ergodic convergence.

The future-cashflow representation used here brings clear analytical benefits: in this
state-space, debt
rollover is a shift operator; discounting (i.e. accounting/normalizing for deficit growth) is a diagonal operator; new issuance is a rank-one operator. In these coordinates
the system is a linear SRE, allowing for certain analytical results.

The ergodicity result has implications for a certain class of
Monte Carlo debt simulation models driven by stochastic, correlated fiscal and interest rate paths.
When such models conform to the conditions described in this work, their resulting calculations should approximately
recover the invariant metrics of the underlying system, provided the simulation horizon
is sufficiently large for ‘burn-in’ to wash away the effect of initial conditions. Cognizance of this property can help
practitioners to predict and interpret the output of such
models, as well as how or whether they are likely to respond to changes in the assumed drivers such as interest rates, deficits, and
their correlations.

In principle, the linear SRE structure, under Gaussian forcing, may permit analytic computation or approximation
of higher moments such as variances, tail-risk measures, or impulse responses; the focus
of this piece has been on means and steady ratios. Future work can expand on the simple, correlation-adjusted metrics listed here.

A potential avenue of improvement is to incorporate
floating-rate debt (e.g. FRNs and TIPS, in the US context)
into the model, for which the future-cashflow state representation may prove beneficial.

Another natural extension of this framework is to more explicitly allow rates and deficits to be determined jointly based on underlying
factors, as in an explicit macroeconomic model. Provided such drivers remain Gaussian (or similarly well-behaved) and the relationships linear, the
core developments and ergodicity observations described above should remain robust to such a structure.

Although the main observation here is ergodic convergence, which depended only on the feedback function, the additional
assumptions about rate/deficit behavior could
obviously affect how long the is ‘burn-in’ period and how volatile the system remains when close to equilibrium. Thus the speed of convergence
and the variance of paths around their ergodic means, and
the relationship of these behaviors to the volatility and persistence of the interest-rate
and deficit driving factors, is open for further investigation.

More challenging potential extensions to this model framework
include allowing for dynamic issuance policy, and to allow issuance policy to affect interest rates
endogenously via the well-known
supply effect. Either would disallow much of the linear machinery and analysis developed above. For
modest supply-feedback effects, it is possible the endogenity result could still be
demonstrated under an appropriate feedback criterion, and that first-order perturbative approaches could be used, but closed-form solutions
are unlikely.

The granular sustainability condition developed here, in its own right, may prove
a useful analytical tool in cross-country analysis and comparison of the fiscal and debt-management policy of sovereigns.

Ultimately, the linear SRE approach described above can help serve as a unifying backbone for modeling and practical
debt management, one that preserves analytical
clarity while accommodating the richer economic structure required for policy‑relevant debt analysis.

## References

* Belton [2018]

  Belton, T, Dawsey, K., Greenlaw, D., Li, H., Ramaswamy, S. & Sack, B.
  Optimizing the maturity structure of U.S. Treasury debt: A model-based framework.
  Brookings paper, available at <https://www.brookings.edu/articles/optimizing-the-maturity-structure-of-u-s-treasury-debt/>.
* Blanchard [2019]

  Blanchard, O. (2019).
  Public debt and low interest rates.
  *American Economic Review Papers and Proceedings*, 109, 1–24.
* Bolder [2003]

  Bolder, D. (2003)
  A Stochastic Simulation Framework for the Government of Canada’s Debt Strategy.
  *Bank of Canada Working Paper*, 2003.
* Bolder [2011]

  Bolder, D. and Deeley, S. (2011)
  The Canadian Debt-Strategy Model: An Overview of the Principal Elements.
  *Bank of Canada Working Paper*, 2011.
* Bougerol and Picard [1992]

  Bougerol, P. and Picard, N. (1992).
  Strict stationarity of generalized autoregressive processes.
  The Annals of Probability, pages 1714–1730.
* Brandt [1986]

  Brandt, A. (1986).
  The stochastic stability of autoregressive processes with random coefficients.
  *Journal of Multivariate Analysis*, 19, 1–24.
* Cameron [2018]

  Cameron, C. (2018).
  Visualizing Treasury Issuance Strategy. White paper, available at <https://ssrn.com/abstract=3120036>.
* Consiglio [2012]

  Consigliio, A. and Staino, A. (2012).
  A Stochastic Programming Model for the Optimal Issuance of Government Bonds.
  *Annals of Operations Research*, March 2012.
* Cottarelli and Jaramillo [2012]
   Cottarelli, C., & Jaramillo, L. (2012).
  Walking hand in hand: Fiscal policy and growth in advanced economies.
  IMF Working Paper WP/12/137, International Monetary Fund, May 2012.
* Escolano [2010]

  Escolano, A. (2010).
  A practical guide to public debt dynamics, fiscal sustainability, and cyclical adjustment of budgetary aggregates.
  IMF Technical Paper.
* Hairer and Mattingly [2011]
   Hairer, M., & Mattingly, J. C. (2011).
  Yet another look at Harris’ ergodic theorem for Markov chains.
  In *Probability and Mathematical Statistics*, 63, 109–117.
* Horn and Johnson [2012]

  Horn, R. A., & Johnson, C. R. (2012).
  *Matrix Analysis* (2nd ed.).
  Cambridge University Press.
* Landoni et al [2019]

  Landoni, M., Smith, W.T. & Cameron, C. (2019).
  Linking policy to outcomes: a simple framework for debt maturity management. White paper, available
  at <https://ssrn.com/abstract=3300347>.
* Meyn and Tweedie [1993]

  Meyn, S.P. and Tweedie, R.L. (1993).
  *Markov Chains and Stochastic Stability*.
  Springer-Verlag.
* TBAC [2018]

  Treasury Borrowing Advisory Committee.
  *Discussion Charts by Calendar Year, 4th Quarter
  2018.* Presentation to US Treasury, available
  at <https://home.treasury.gov/system/files/276/CombinedChargesforArchives4thqtr2018.pdf>.
* TBAC [2019]

  Treasury Borrowing Advisory Committee.
  *Discussion Charts by Calendar Year, 2nd Quarter
  2019.* Presentation to US Treasury, available
  at <https://home.treasury.gov/system/files/221/q22019CombinedChargesforArchives.pdf>.