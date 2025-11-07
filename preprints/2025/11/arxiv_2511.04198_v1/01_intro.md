---
authors:
- Philipp C. Hornung
doc_id: arxiv:2511.04198v1
family_id: arxiv:2511.04198
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Mean-field approximations in insurance
url_abs: http://arxiv.org/abs/2511.04198v1
url_html: https://arxiv.org/html/2511.04198v1
venue: arXiv q-fin
version: 1
year: 2025
---


Philipp C. Hornung
Department of Mathematical Sciences, University of Copenhagen, Universitetsparken 5, DK-2100 Copenhagen, Denmark
[[pcho@math.ku.dk](mailto:pcho@math.ku.dk)](mailto:)
November 6, 2025

###### Abstract.

The calculation of the insurance liabilities of a cohort of dependent individuals in general requires the solution of a high-dimensional system of coupled linear forward integro-differential equations, which is infeasible for a larger cohort. However, by using a mean-field approximation, the high dimensional system of linear forward equations can be replaced by a low-dimensional system of non-linear forward integro-differential equations. We show that, subject to certain regularity conditions, the insurance liability viewed as a (conditional) expectation of a functional of an underlying jump process converges to its mean-field approximation, as the number of individuals in the cohort goes to infinity. Examples from both life- and non-life insurance illuminate the practical importance of mean-field approximations.

  

Keywords: Reserving; Non-linear forward equations; Propagation of Chaos; McKean–Vlasov Jump Process;

## 1. Introduction

When modelling the insurance liabilities of a cohort, the individual liability can depend on the other individuals’ liabilities, either because the insurance payments of one individual depend on the insurance payments of the other individuals, while the individuals themselves are independent, or because the individuals themselves are dependent. The former case was the subject of [Djehiche&Loefdahl2016], while the latter case so far has recieved little to no attention in the literature. The purpose of this paper is to remedy this fact.

We consider a cohort of nn homogeneous individuals, each with an associated jump process, where the insurance payments of each individual are given by a functional the individual’s jump process path. The insurance liability is then either the expectation of the insurance payments, or the conditional expectation of the insurance payments given the individual’s initial state or covariates. The compensators of the jump processes are assumed to be absolutely continuous with respect to the Lebesgue measure and we allow the intensity kernel to depend on collective quantities, such as cohort averages or functions thereof. Thus the individuals are dependent. When using the forward method, the calculation of the insurance liability of a single individual requires one to solve a system of linear forward integro-differential equations satisfied by the occupation or transition probabilities, and since the individuals are dependent, one would have to solve nn coupled systems of forward integro-differential equations simultaneously. This is computationally infeasible when nn is large.

One solution to this problem is to replace all collective quantities by their expectations. In this case the forward integro-differential equations become non-linear, but the dimension of the system remains the same as for a single individual and thus one can calculate the liabilities in a similar fashion as if the individuals were independent. This is called a mean-field approximation and the resulting insurance liability will be called the mean-field liability.

These mean-field approximations have been used to calculate the insurance liability for contracts that cover risks with contagion effects, such as epidemics, where the probability of infection can depend on the number of individuals in the cohort already infected, see [Francis&Steffensen2024], or cyber attacks, where the probability of a computer getting infected by a computer virus can depend on the number of infected neighbours in a network, see [FahrenwaldtEtAl2018]. Another possible example is the inclusion of collective effects across lines of business, such as the modelling of disability insurance using collective information about health insurance claims, see [Furrer&Hornung2025]. The goal of this paper is to give these approximations a solid mathematical foundation.

The non-linear equations obtained by replacing the collective quantities by their expectation are solved by the occupation- or transition probabilites of a distribution dependent jump process, which is distribution dependent in the sense that the intensity kernel depends on the distribution of the process itself. Thus by replacing the average with the mean, one changes the probabilistic model from a model of dependent individuals with a jump process to a model of independent individuals with a distribution dependent jump process and the mean-field liability can therefore be interpreted as the (conditional) expectation of a functional of a distribution-dependent jump process path.

We show that if the insurance payments are almost surely continuous and uniformly integrable functionals of jump process paths, then their expectation (the insurance liability) converges as well, both in the unconditional and under some additional assumptions in the conditional case. Additionally we prove a law of large numbers in the sense that the cohort average of insurance payments converges to the (unconditional) mean-field insurance liability when nn becomes large. This shows that the diversification effect of large cohorts persists, even though the individuals are dependent.

The key to these results is to show that for large nn, the joint distribution of the jump processes for a subcohort of kk individuals in a cohort of nn individuals converges weakly to the joint distribution of kk independent individuals with a distribution-dependent jump process. This type of weak convergence is also called chaos or propagation of chaos and was first introduced by [Kac1956], while the concept of distribution dependent processes for diffusion processes stems from [McKean1966, McKean1969]. Ever since these concepts have been further developed in many directions and have found numerous applications (for a very comprehensive review, see [Chaintron&Diez2022I, Chaintron&Diez2022II]). While the papers [Shiga&Tanaka1985] and [Djehiche&Kaj1995] provide different propagation of chaos results specifically for jump processes, the assumptions on the distribution dependence are too strict for many actuarial applications, as they do not allow for distribution dependent jump sizes. We therefore borrow some results and methods from the jump-diffusion literature. In particular, we use a coupling construction introduced by [Graham1992-2] combined with an approach used by [AndreisEtAl2018] to prove chaosticity for a class of time-inhomogenous pure jump processes with potentially unbounded jump sizes. This is sufficient for the unconditional case and in the case that the state space is countable, it is also sufficient for the conditional case.

If the state space is uncountable, this result is not enough for the conditional case and more work is required. For any fixed kk we can condition on the initial state or covariates for the first kk individuals. Under the assumption that the joint conditional distribution of the initial state or covariates of the remaining n−kn-k individuals given the inital state or covariates of the first kk individuals is chaotic, we show that the joint conditional distribution of the first kk individuals, given their intial state or covariates, converges weakly to the joint distribution of kk independent individuals, each following the conditional distribution of a non-linear jump process given the respective initial value or covariates. While this result is not surprising, it has (to the best of our knowledge) not previously received attention in the literature.

Finally we note that the mean-field liabilities considered in this paper can naturally be calculated via the forward method by solving the non-linear forward integro-differential equations for the occupation or transition probabilities of the distribution dependent jump process. Since only the initial distribution is known and the intensity kernel depends on the occupation probabilities themselves, a backwards approach appears cumbersome. If one individual’s insurance payments only depends on the other individuals’ insurance payments, while the individuals themselves are independent, then [Djehiche&Loefdahl2016] shows that a backwards approach is possible. In that case the liability can be calculated by solving a non-linear version of Thiele’s backward differential equation, which has been generalised to the non-Markovian case in [Christiansen&Djehiche2020] and the as-if-Markov case in [Christiansen&Djehiche2025].

In Section [2](https://arxiv.org/html/2511.04198v1#S2 "2. Jump processes ‣ Mean-field approximations in insurance") we introduce non-linear jump processes, and show that their conditional path-laws are equal to the path-laws of a linearised jump processes. In Section [3](https://arxiv.org/html/2511.04198v1#S3 "3. Mean-field approximation ‣ Mean-field approximations in insurance") we prove the usual chaosticity result, while we in Section [4](https://arxiv.org/html/2511.04198v1#S4 "4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") prove the conditional result. In Sections [5](https://arxiv.org/html/2511.04198v1#S5 "5. Non-life insurance applications ‣ Mean-field approximations in insurance") and [6](https://arxiv.org/html/2511.04198v1#S6 "6. Life insurance applications ‣ Mean-field approximations in insurance"), we discuss mean-field approximations for typical non-life and life insurance liabilities, verify a law of large numbers and central limit theorem followed by two illuminating examples. The individual non-life insurance payment is the aggregate claim amount, where the claim occurence rate and the claim sizes can depend on collective quantities, while the individual life insurance payments are modelled by a typical payment stream containing sojourn and transition payments.

## Notation, definitions and preliminaries

Throughout the text, we will be using some spaces and metrics which we will define here. On Rd\amsmathbb{R}^{d} we will use the metric

|  |  |  |
| --- | --- | --- |
|  | d​(x,y)=∑i=1d|xi−yi|,x,y∈Rd\displaystyle d(x,y)=\sum\_{i=1}^{d}|x\_{i}-y\_{i}|,\quad x,y\in\amsmathbb{R}^{d} |  |

and the norm

|  |  |  |
| --- | --- | --- |
|  | ‖x‖=∑i=1d|xi|,x∈Rd,\displaystyle\|x\|=\sum\_{i=1}^{d}|x\_{i}|,\quad x\in\amsmathbb{R}^{d}, |  |

where |⋅||\cdot| is the absolute value function on R\amsmathbb{R}.

Let (S,dS)(S,d\_{S}) be a Polish space. We let D​([τ,T],S)\amsmathbb{D}([\tau,T],S) be the Skorohod space of càdlàg paths t↦xtt\mapsto x\_{t} with values in SS on the time interval [τ,T][\tau,T]. On this space we will use the following two metrics. The uniform metric dUd^{U} defined as

|  |  |  |
| --- | --- | --- |
|  | dU​(x,y):=supτ≤t≤TdS​(xt,yt),x,y∈D​([τ,T],S)\displaystyle d^{U}(x,y):=\sup\_{\tau\leq t\leq T}d\_{S}(x\_{t},y\_{t}),\quad x,y\in\amsmathbb{D}([\tau,T],S) |  |

and the Skorokhod metric

|  |  |  |
| --- | --- | --- |
|  | dJ1​(x,y):=infλ∈Λ{supτ≤t≤TdS​(xλ​(t),yt)∨supτ≤t≠s≤Tlog⁡|λ​(t)−λ​(s)t−s|},\displaystyle d^{J^{1}}(x,y):=\inf\_{\lambda\in\Lambda}\bigg\{\sup\_{\tau\leq t\leq T}d\_{S}(x\_{\lambda(t)},y\_{t})\vee\sup\_{\tau\leq t\neq s\leq T}\log\bigg|\frac{\lambda(t)-\lambda(s)}{t-s}\bigg|\bigg\}, |  |

for x,y∈D​([τ,T],S)x,y\in\amsmathbb{D}([\tau,T],S). The set Λ\Lambda contains all increasing bijections on [τ,T][\tau,T]. The metric space (D​([τ,T],S),dU)(\amsmathbb{D}([\tau,T],S),d^{U}) is complete but not separable and therefore not Polish. Luckily the space (D​([τ,T],S),dJ1)(\amsmathbb{D}([\tau,T],S),d^{J\_{1}}) is Polish. Note that dJ1​(x,y)≤dU​(x,y)d^{J\_{1}}(x,y)\leq d^{U}(x,y), as the identity t↦tt\mapsto t is an element of Λ\Lambda. This implies that the topology induced by dUd^{U} is stronger than the topology induced by dJ1d^{J\_{1}}, meaning that any sequence converging in the uniform topology also converges in the J1J\_{1}-topology. Finally let H​([τ,T],S)⊂D​([τ,T],S)\amsmathbb{H}([\tau,T],S)\subset\amsmathbb{D}([\tau,T],S) be the space of piecewise constant càdlàg paths, with a finite number of jumps on a finite time interval.

Let 𝒫​(S)\mathcal{P}(S) denote the set of probability measures on SS. Let q≥1q\geq 1 and define 𝒫q\mathcal{P}^{q} as

|  |  |  |
| --- | --- | --- |
|  | 𝒫q​(S):={ρ∈𝒫​(S):∫SdS​(x0,x)q​ρ​(d​x)<∞},\displaystyle\mathcal{P}^{q}(S):=\bigg\{\rho\in\mathcal{P}(S):\,\int\_{S}d\_{S}(x\_{0},x)^{q}\rho(\mathrm{d}x)<\infty\bigg\}, |  |

where x0∈Sx\_{0}\in S is arbitrary. Note that 𝒫p​(S)⊂𝒫q​(S)⊂𝒫1​(S)\mathcal{P}^{p}(S)\subset\mathcal{P}^{q}(S)\subset\mathcal{P}^{1}(S) for p>q>1p>q>1.

On the set 𝒫1​(E)\mathcal{P}^{1}(E) we define the Wasserstein(1)-distance between two measures ρ1,ρ2∈𝒫1​(S)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(S) as

|  |  |  |
| --- | --- | --- |
|  | dW:=infX∼ρ1,Y∼ρ2E​[dS​(X,Y)],ρ1,ρ2∈𝒫1​(S).\displaystyle d\_{W}:=\inf\_{X\sim\rho\_{1},Y\sim\rho\_{2}}\amsmathbb{E}[d\_{S}(X,Y)],\quad\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(S). |  |

If (S,dS)(S,d\_{S}) is Polish, then (𝒫1​(S),dW)(\mathcal{P}^{1}(S),d\_{W}) will be Polish as well (see Th. 6.9 in [Villani2009]). We will denote the Wasserstein distance on 𝒫1​(S)\mathcal{P}^{1}(S) simply as dWd\_{W}, while we on 𝒫1​(D​([τ,T],S))\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],S)) will use dWUd\_{W}^{U} and dWJ1d\_{W}^{J\_{1}}, which are the Wasserstein(1)-distances based on dUd^{U} and dJ1d^{J\_{1}}. Note that it holds that dWJ1≤dWUd\_{W}^{J\_{1}}\leq d\_{W}^{U}.

A starting point for many proofs below is the following inequality:

|  |  |  |
| --- | --- | --- |
|  | dW​(ρ1,ρ2)≤E​[dS​(X,Y)],\displaystyle d\_{W}(\rho\_{1},\rho\_{2})\leq\amsmathbb{E}[d\_{S}(X,Y)], |  |

where X,Y:Ω→SX,Y:\Omega\rightarrow S are two random variables with X​(P)=ρ1X(\amsmathbb{P})=\rho\_{1} and Y​(P)=ρ2Y(\amsmathbb{P})=\rho\_{2}.

By the Kantorovich-Rubinstein duality it holds that the Wasserstein(1) distance on 𝒫1​(S)\mathcal{P}^{1}(S) is equal to the Kantorovich-Rubinstein distance defined as

|  |  |  |
| --- | --- | --- |
|  | dK​R​(ρ1,ρ2)=supf∈Lip(1){|∫Sf​(x)​ρ1​(d​x)−∫Sf​(x)​ρ2​(d​x)|},\displaystyle d\_{KR}(\rho\_{1},\rho\_{2})=\sup\_{f\in\text{Lip(1)}}\bigg\{\bigg|\int\_{S}f(x)\rho\_{1}(\mathrm{d}x)-\int\_{S}f(x)\rho\_{2}(\mathrm{d}x)\bigg|\bigg\}, |  |

where Lip​(1)\text{Lip}(1) is the set of Lipschitz continuous functions f:S→Rf:S\rightarrow\amsmathbb{R} with Lipschitz constant less than or equal to 1 (see p. 60 of [Villani2009]).

The Kantorovich-Rubinstein distance can be extended to to the set ℳb1​(S)\mathcal{M}^{1}\_{b}(S) given by

|  |  |  |
| --- | --- | --- |
|  | ℳb1​(S):={μ∈ℳ​(S):μ​(S)<∞​ and ​∫SdS​(x0,x)​μ​(d​x)<∞},\displaystyle\mathcal{M}^{1}\_{b}(S):=\bigg\{\mu\in\mathcal{M}(S):\,\mu(S)<\infty\text{ and }\int\_{S}d\_{S}(x\_{0},x)\mu(\mathrm{d}x)<\infty\bigg\}, |  |

by defining for μ1,μ2∈ℳb1​(S)\mu\_{1},\mu\_{2}\in\mathcal{M}\_{b}^{1}(S)

|  |  |  |
| --- | --- | --- |
|  | dK​R​(μ1,μ2):=supf∈Lip(1){|∫Sf​(x)​μ1​(d​x)−∫Sf​(x)​μ2​(d​x)|}.\displaystyle d\_{KR}(\mu\_{1},\mu\_{2}):=\sup\_{f\in\text{Lip(1)}}\bigg\{\bigg|\int\_{S}f(x)\mu\_{1}(\mathrm{d}x)-\int\_{S}f(x)\mu\_{2}(\mathrm{d}x)\bigg|\bigg\}. |  |

For x0∈Sx\_{0}\in S we can also define

|  |  |  |
| --- | --- | --- |
|  | dK​Rx0​(μ1,μ2):=supf∈Lip(1),f​(x0)=0{|∫Sf​(x)​μ1​(d​x)−∫Sf​(x)​μ2​(d​x)|}.\displaystyle d\_{KR}^{x\_{0}}(\mu\_{1},\mu\_{2}):=\sup\_{f\in\text{Lip(1)},f(x\_{0})=0}\bigg\{\bigg|\int\_{S}f(x)\mu\_{1}(\mathrm{d}x)-\int\_{S}f(x)\mu\_{2}(\mathrm{d}x)\bigg|\bigg\}. |  |

It holds that

|  |  |  |
| --- | --- | --- |
|  | dK​Rx0​(μ1,μ2)≤dK​R​(ρ1,ρ2),\displaystyle d\_{KR}^{x\_{0}}(\mu\_{1},\mu\_{2})\leq d\_{KR}(\rho\_{1},\rho\_{2}), |  |

with equality when μ1​(S)=μ2​(S)\mu\_{1}(S)=\mu\_{2}(S). In particular, if ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(E) then

|  |  |  |
| --- | --- | --- |
|  | dK​Rx0​(ρ1,ρ2)=dK​R​(ρ1,ρ2)=dW​(ρ1,ρ2).\displaystyle d\_{KR}^{x\_{0}}(\rho\_{1},\rho\_{2})=d\_{KR}(\rho\_{1},\rho\_{2})=d\_{W}(\rho\_{1},\rho\_{2}). |  |

## 2. Jump processes

Let (Ω,ℱ,F,P)(\Omega,\mathcal{F},\amsmathbb{F},\amsmathbb{P}) be a filtered probability space satisfying the usual conditions, where we write F=(ℱt)t≥0\amsmathbb{F}=(\mathcal{F}\_{t})\_{t\geq 0}. We fix a terminal time T>0T>0 and a set E⊂RdE\subset\amsmathbb{R}^{d} such that (E,d)(E,d) is a Polish space, will henceforth denote the state space of the jump processes considered here. Let h:E×E→Rdh:E\times E\rightarrow\amsmathbb{R}^{d} be given by h​(x,y)=y−xh(x,y)=y-x and set A:=h​(E,E)A:=h(E,E). Thus AA is the set of possible jump sizes.

### 2.1. Jump processes

For (τ,x)∈[0,T]×E(\tau,x)\in[0,T]\times E we consider the jump process with state space EE given by the SDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.1) |  | Xtτ,ζ\displaystyle X\_{t}^{\tau,\zeta} | =Y+∫(τ,t]×Az​Q​(d​s,d​z),\displaystyle=Y+\int\_{(\tau,t]\times A}z\,Q(ds,dz), |  |

where YY has distribution ζ∈𝒫1​(E)\zeta\in\mathcal{P}^{1}(E) and QQ is a random counting measure with state space AA and compensating measure

|  |  |  |
| --- | --- | --- |
|  | L¯​(d​t,d​z)=μt​(Xt−τ,ζ,d​z)​d​t.\displaystyle\bar{L}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(X^{\tau,\zeta}\_{t-},\mathrm{d}z)\mathrm{d}t. |  |

Here μ\mu is assumed to be a bounded kernel with first moment, that is (t,x)↦μt​(x,B)(t,x)\mapsto\mu\_{t}(x,B) is Borel-measurable for all B∈ℬ​(A)B\in\mathcal{B}(A) and B↦μt​(x,B)B\mapsto\mu\_{t}(x,B) is an element of ℳb1​(A)\mathcal{M}\_{b}^{1}(A) for all (t,x)∈[0,T]×E(t,x)\in[0,T]\times E. We can now define the bounded and Borel-measurable function λt​(x):=μt​(x,A)\lambda\_{t}(x):=\mu\_{t}(x,A) and the probability kernel rt​(x,d​z):=μt​(x,d​z)λt​(x)r\_{t}(x,\mathrm{d}z):=\frac{\mu\_{t}(x,\mathrm{d}z)}{\lambda\_{t}(x)}. Thus μt​(x,d​z)=λt​(x)​rt​(x,d​z)\mu\_{t}(x,\mathrm{d}z)=\lambda\_{t}(x)r\_{t}(x,\mathrm{d}z), where λ\lambda can be interpreted as the jump intensity, while rt​(x,d​z)r\_{t}(x,\mathrm{d}z) is the distribution of the jump sizes of Xτ,ζX^{\tau,\zeta} given that a jump occurs at time tt and that Xt−τ,ζ=xX^{\tau,\zeta}\_{t-}=x. In order for Xtτ,ζX\_{t}^{\tau,\zeta} to always take values in EE we assume that μt​(x,A∖gx−1​(E))=0\mu\_{t}(x,A\setminus g\_{x}^{-1}(E))=0 for all x∈Ex\in E, where gx:A→Rdg\_{x}:A\rightarrow\amsmathbb{R}^{d} is given by gx​(z)=x+zg\_{x}(z)=x+z.

###### Theorem 2.1.

Assume that the function λ:[0,T]×E→[0,∞)\lambda:[0,T]\times E\rightarrow[0,\infty) is Borel-measurable and that there exists a Cλ,Cr>0C\_{\lambda},C\_{r}>0 such that

|  |  |  |
| --- | --- | --- |
|  | supt∈[τ,T],x∈Eλt​(x)≤Cλandsupt∈[τ,T],x∈E∫A‖z‖​rt​(x,d​z)≤Cr.\displaystyle\sup\_{t\in[\tau,T],x\in E}\lambda\_{t}(x)\leq C\_{\lambda}\quad\text{and}\quad\sup\_{t\in[\tau,T],x\in E}\int\_{A}\|z\|\,r\_{t}(x,\mathrm{d}z)\leq C\_{r}. |  |

Then there exists a unique weak solution to the SDE ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), which is non-explosive.

###### Proof.

Let YY be a random variable with distribution ζ\zeta and let (Ti,Zi)i∈N(T\_{i},Z\_{i})\_{i\in\amsmathbb{N}} be a marked point process with associated random counting measure QQ with state space AA. We let the compensating measure of QQ, which determines the distribution of both QQ and (Ti,Zi)i∈N(T\_{i},Z\_{i})\_{i\in\amsmathbb{N}}, be given by

|  |  |  |
| --- | --- | --- |
|  | L​(d​t,d​z)=μt​(Y+∑i=1Nt−Zi,d​z)​d​t,\displaystyle L(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}\bigg(Y+\sum\_{i=1}^{N\_{t-}}Z\_{i},\mathrm{d}z\bigg)\mathrm{d}t, |  |

where Nt−:=Q​((τ,t)×A)N\_{t-}:=Q((\tau,t)\times A). This satisfies the conditions of Theorem 8.2.2 of [Last&Brandt1995], thus yielding existence an uniqueness of QQ with compensating measure LL. Let now f:E×𝒩A→H​([τ,T],E)f:E\times\mathcal{N}\_{A}\rightarrow\amsmathbb{H}([\tau,T],E) be a mapping from the space of marked point process realisations on AA into the space of jump process paths on EE given by

|  |  |  |
| --- | --- | --- |
|  | f​(Y,(Ti,Zi)i∈N)=(Y+∑i=1NtZi)t∈[τ,T].\displaystyle f(Y,(T\_{i},Z\_{i})\_{i\in\amsmathbb{N}})=\bigg(Y+\sum\_{i=1}^{N\_{t}}Z\_{i}\bigg)\_{t\in[\tau,T]}. |  |

Let πt:H​([τ,T],E)→E\pi\_{t}:\amsmathbb{H}([\tau,T],E)\rightarrow E be the time marginal projection. Then

|  |  |  |
| --- | --- | --- |
|  | Xtτ,ζ=πt​(f​(Y,(Ti,Zi)i∈N))=Y+∑i=1NtZi\displaystyle X\_{t}^{\tau,\zeta}=\pi\_{t}(f(Y,(T\_{i},Z\_{i})\_{i\in\amsmathbb{N}}))=Y+\sum\_{i=1}^{N\_{t}}Z\_{i} |  |

and since

|  |  |  |
| --- | --- | --- |
|  | L​(d​t,d​z)=μt​(πt−​(f​(Y,(Ti,Zi)i∈N)),d​z)​d​t=μt​(Xt−,d​z)​d​t,\displaystyle L(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(\pi\_{t-}(f(Y,(T\_{i},Z\_{i})\_{i\in\amsmathbb{N}})),\mathrm{d}z)\mathrm{d}t=\mu\_{t}(X\_{t-},\mathrm{d}z)\mathrm{d}t, |  |

we can conclude that Xtτ,ζ=πt​(f​(Y,(Ti,Zi)i∈N))X\_{t}^{\tau,\zeta}=\pi\_{t}(f(Y,(T\_{i},Z\_{i})\_{i\in\amsmathbb{N}})) is the unique solution of ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")).

The non-explosiveness follows, as

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖Xtτ,ζ‖]\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\tau,\zeta}\|\bigg] | ≤E​[‖Y‖]+E​[∫τT∫E‖z‖​μs​(Xs−τ,ζ,d​y)​dt]\displaystyle\leq\amsmathbb{E}[\|Y\|]+\amsmathbb{E}\bigg[\int\_{\tau}^{T}\int\_{E}\|z\|\mu\_{s}(X\_{s-}^{\tau,\zeta},\mathrm{d}y)\mathrm{d}t\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E​[‖Y‖]+Cλ​Cr​(T−τ).\displaystyle\leq\amsmathbb{E}[\|Y\|]+C\_{\lambda}C\_{r}(T-\tau). |  |

∎

The stochastic process Xτ,ζX^{\tau,\zeta} has càdlàg paths and can thus be viewed as a random variable taking values in the space D​([τ,T],E)\amsmathbb{D}([\tau,T],E) and the path-law of Xτ,ζX^{\tau,\zeta} given by Qτ,ζ:=Xτ,ζ​(P)\amsmathbb{Q}\_{\tau,\zeta}:=X^{\tau,\zeta}(\amsmathbb{P}) is an element of 𝒫1​(D​([τ,T],E))\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],E)). Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") yields existence and uniqueness of the path-law Qτ,ζ\amsmathbb{Q}\_{\tau,\zeta}.

A special case of ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) that is of particular interest is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.2) |  | Xtτ,x\displaystyle X\_{t}^{\tau,x} | =x+∫(τ,t]×Az​Q​(d​s,d​z),\displaystyle=x+\int\_{(\tau,t]\times A}z\,Q(ds,dz), |  |

with a deterministic initial starting value, corresponding to ζ=δ{x}\zeta=\delta\_{\{x\}}. Let Qτ,x=Xτ,x​(P)\amsmathbb{Q}\_{\tau,x}=X^{\tau,x}(\amsmathbb{P}). Then the familiy (Qτ,x)x∈E(\amsmathbb{Q}\_{\tau,x})\_{x\in E} constitutes a regular conditional probability of Qτ,ζ\amsmathbb{Q}\_{\tau,\zeta} given the initial value:

###### Theorem 2.2.

The familiy (Qτ,x)x∈E(\amsmathbb{Q}\_{\tau,x})\_{x\in E} constitutes a regular conditional probability of Qτ,ζ\amsmathbb{Q}\_{\tau,\zeta}. Thus it holds that

|  |  |  |
| --- | --- | --- |
|  | Qτ,ζ​(d​ω)=∫EQτ,x​(d​ω)​ζ​(d​x).\displaystyle\amsmathbb{Q}\_{\tau,\zeta}(\mathrm{d}\omega)=\int\_{E}\amsmathbb{Q}\_{\tau,x}(\mathrm{d}\omega)\zeta(\mathrm{d}x). |  |

###### Proof.

For a proof see Appendix [A](https://arxiv.org/html/2511.04198v1#A1 "Appendix A Proof of Theorems 2.2 and 2.7 ‣ Mean-field approximations in insurance"). This is the jump process version of Proposition 2.8 of [Trevisan2016].
∎

This result shows us, that the distribution of the SDE ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) conditional on the initial state being x∈Ex\in E is given by Qτ,x\amsmathbb{Q}\_{\tau,x}, which is the distribution of the SDE ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). Furthermore, we have that this conditional distribution is independent of the initial distribution ζ\zeta, meaning that the same (Qτ,x)x∈E(\amsmathbb{Q}\_{\tau,x})\_{x\in E} is a regular conditional distribution for any Qτ,ζ\amsmathbb{Q}\_{\tau,\zeta}.

When it comes to practical calculations, we are interested in the time-marginal distributions ηtτ,x:=Xtτ,x​(P)\eta\_{t}^{\tau,x}:=X^{\tau,x}\_{t}(\amsmathbb{P}) and ηtτ,ζ:=Xtτ,ζ​(P)\eta\_{t}^{\tau,\zeta}:=X^{\tau,\zeta}\_{t}(\amsmathbb{P}). The former satisfy the well-known (see [Feller1940, FeinbergEtAl2014]) integro-differential equations given by:

###### Proposition 2.3.

The law ηtτ,x\eta\_{t}^{\tau,x} satsifies the forward integro-differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​ηtτ,x​(B)=\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\eta\_{t}^{\tau,x}(B)= | ∫E∖B∫A1B​(y+z)​μt​(y,d​z)​ηtτ,x​(d​y)\displaystyle\int\_{E\setminus B}\int\_{A}\mathrm{1}\_{B}(y+z)\mu\_{t}(y,dz)\eta\_{t}^{\tau,x}(\mathrm{d}y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫B∫A1E∖B​(y+z)​μt​(y,d​z)​ηtτ,x​(d​y),\displaystyle-\int\_{B}\int\_{A}\mathrm{1}\_{E\setminus B}(y+z)\mu\_{t}(y,dz)\eta\_{t}^{\tau,x}(\mathrm{d}y), |  |

with ηττ,x​(B)=δ{x}​(B)\eta\_{\tau}^{\tau,x}(B)=\delta\_{\{x\}}(B) for t≥τt\geq\tau and x∈Ex\in E.

Theorem [2.2](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") directly implies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.3) |  | ηtτ,ζ​(B)\displaystyle\eta\_{t}^{\tau,\zeta}(B) | =∫Eηtτ,x​(B)​ζ​(d​x).\displaystyle=\int\_{E}\eta\_{t}^{\tau,x}(B)\zeta(\mathrm{d}x). |  |

As the time-marginals (ηtτ,x)x∈E(\eta\_{t}^{\tau,x})\_{x\in E} do not depend on ζ\zeta, one can easily calculate the probabilities ηtτ,ζ\eta\_{t}^{\tau,\zeta} for any ζ∈𝒫1​(E)\zeta\in\mathcal{P}^{1}(E), once (ηtτ,x)x∈E(\eta\_{t}^{\tau,x})\_{x\in E} is obtained. But by using ([2.3](https://arxiv.org/html/2511.04198v1#S2.E3 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) we can also prove that ηtτ,ζ\eta\_{t}^{\tau,\zeta} can be calculated by directly solving the following integro-differential equations:

###### Proposition 2.4.

Let B∈ℬ​(E)B\in\mathcal{B}(E). The law ηtτ,ζ\eta\_{t}^{\tau,\zeta} satsifies the forward integro-differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​ηtτ,ζ​(B)=\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\eta\_{t}^{\tau,\zeta}(B)= | ∫E∖B∫A𝟙B​(x+z)​μt​(x,d​z)​ηtτ,ζ​(d​x)\displaystyle\int\_{E\setminus B}\int\_{A}\mathds{1}\_{B}(x+z)\mu\_{t}(x,dz)\eta\_{t}^{\tau,\zeta}(\mathrm{d}x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫B∫A𝟙E∖B​(x+z)​μt​(x,d​z)​ηtτ,ζ​(d​x),\displaystyle-\int\_{B}\int\_{A}\mathds{1}\_{E\setminus B}(x+z)\mu\_{t}(x,dz)\eta\_{t}^{\tau,\zeta}(\mathrm{d}x), |  |

with ηττ,ζ​(B)=ζ​(B)\eta\_{\tau}^{\tau,\zeta}(B)=\zeta(B) for t≥τt\geq\tau and ζ∈𝒫1​(E)\zeta\in\mathcal{P}^{1}(E).

###### Proof.

By ([2.3](https://arxiv.org/html/2511.04198v1#S2.E3 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) and Proposition [2.3](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") we have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηtτ,ζ​(B)=\displaystyle\eta\_{t}^{\tau,\zeta}(B)= | ∫Eηtτ,x​(B)​ζ​(d​x)=∫Eηττ,x​ζ​(d​x)\displaystyle\int\_{E}\eta\_{t}^{\tau,x}(B)\zeta(\mathrm{d}x)=\int\_{E}\eta\_{\tau}^{\tau,x}\zeta(\mathrm{d}x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫(τ,t]∫E∖B∫A1B​(y+z)​μs​(y,d​z)​∫Eηsτ,x​(d​y)​ζ​(d​x)​ds\displaystyle+\int\_{(\tau,t]}\int\_{E\setminus B}\int\_{A}\mathrm{1}\_{B}(y+z)\mu\_{s}(y,dz)\int\_{E}\eta\_{s}^{\tau,x}(\mathrm{d}y)\zeta(\mathrm{d}x)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫(τ,t]∫B∫A1E∖B​(y+z)​μs​(y,d​z)​∫Eηsτ,x​(d​y)​ζ​(d​x)​ds\displaystyle-\int\_{(\tau,t]}\int\_{B}\int\_{A}\mathrm{1}\_{E\setminus B}(y+z)\mu\_{s}(y,dz)\int\_{E}\eta\_{s}^{\tau,x}(\mathrm{d}y)\zeta(\mathrm{d}x)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ζ​(B)+∫(τ,t]∫E∖B∫A1B​(y+z)​μs​(y,d​z)​ηsτ,ζ​(d​y)​ds\displaystyle\zeta(B)+\int\_{(\tau,t]}\int\_{E\setminus B}\int\_{A}\mathrm{1}\_{B}(y+z)\mu\_{s}(y,dz)\eta\_{s}^{\tau,\zeta}(\mathrm{d}y)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫(τ,t]∫B∫A1E∖B​(y+z)​μs​(y,d​z)​ηsτ,ζ​(d​y)​ds.\displaystyle-\int\_{(\tau,t]}\int\_{B}\int\_{A}\mathrm{1}\_{E\setminus B}(y+z)\mu\_{s}(y,dz)\eta\_{s}^{\tau,\zeta}(\mathrm{d}y)\mathrm{d}s. |  |

Differentiating with respect to tt finishes the proof.
∎

Finally we will show that it is always possible to construct a pathwise representation of ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) in terms of a marked Poisson process, in such a way, that the jump times of the driving random counting measure do not depend on the process, but are given by a homogeneous Poisson process. In this way, it is possible to construct couplings between different jump processes with the same jump times, which will be very useful in the coming proofs. The following result is the jump destination version of Theorem 9.2.2 of [Last&Brandt1995].

###### Proposition 2.5.

Let YY is a random variable with distribution ζ\zeta and set

|  |  |  |
| --- | --- | --- |
|  | Xtτ,ζ=Y+∫(τ,t]×Az​𝒩​(d​t,d​z),\displaystyle X\_{t}^{\tau,\zeta}=Y+\int\_{(\tau,t]\times A}z\,\mathcal{N}(\mathrm{d}t,\mathrm{d}z), |  |

where 𝒩\mathcal{N} is a marked Poisson process with compensating measure given by

|  |  |  |
| --- | --- | --- |
|  | L𝒩​(d​t,d​z)=Cλ​κt​(d​z,Xt−τ,ζ)​d​t\displaystyle L^{\mathcal{N}}(\mathrm{d}t,\mathrm{d}z)=C\_{\lambda}\kappa\_{t}(\mathrm{d}z,X\_{t-}^{\tau,\zeta})\mathrm{d}t |  |

and where the probability measure κt​(x,d​z)\kappa\_{t}(x,\mathrm{d}z) on AA is given by

|  |  |  |
| --- | --- | --- |
|  | κt​(x,d​z)=λt​(x)Cλ1​rt​(x,d​z)+(1−λt​(x)Cλ1)​δ{0}​(d​z).\displaystyle\kappa\_{t}(x,\mathrm{d}z)=\frac{\lambda\_{t}(x)}{C\_{\lambda}^{1}}r\_{t}(x,\mathrm{d}z)+\bigg(1-\frac{\lambda\_{t}(x)}{C\_{\lambda}^{1}}\bigg)\delta\_{\{0\}}(\mathrm{d}z). |  |

Then Xtτ,ζX\_{t}^{\tau,\zeta} is a solution of [2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") with XTiτ,ζ=XTi−τ,ζ+ZiX\_{T\_{i}}^{\tau,\zeta}=X\_{T\_{i}-}^{\tau,\zeta}+Z\_{i} and where Nt=𝒩​((τ,t]×A)N\_{t}=\mathcal{N}((\tau,t]\times A) is a homogeneous Poisson process with intensity CλC\_{\lambda}.

###### Proof.

Set Nt:=𝒩​((τ,t]×A)N\_{t}:=\mathcal{N}((\tau,t]\times A) then the compensating measure is

|  |  |  |
| --- | --- | --- |
|  | L​((τ,t]×A)=∫τtCλ​κs​(Xs−τ,ζ,A)​ds=Cλ​(t−τ),\displaystyle L((\tau,t]\times A)=\int\_{\tau}^{t}C\_{\lambda}\kappa\_{s}(X\_{s-}^{\tau,\zeta},A)\mathrm{d}s=C\_{\lambda}(t-\tau), |  |

which shows that NtN\_{t} is a homogeneous Poisson process with intensity CλC\_{\lambda}.

Set Xtτ,ζX\_{t}^{\tau,\zeta} as

|  |  |  |
| --- | --- | --- |
|  | Xtτ,ζ=Y+∫(τ,t]×Az​𝒩​(d​t,d​z),\displaystyle X\_{t}^{\tau,\zeta}=Y+\int\_{(\tau,t]\times A}z\,\mathcal{N}(\mathrm{d}t,\mathrm{d}z), |  |

Since the contribution to the integral is zero, whenever z=0z=0, we can write

|  |  |  |
| --- | --- | --- |
|  | Xtτ,ζ=Y+∫(τ,t]×Az​Q​(d​t,d​z),\displaystyle X\_{t}^{\tau,\zeta}=Y+\int\_{(\tau,t]\times A}z\,Q(\mathrm{d}t,\mathrm{d}z), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Q​(d​t,d​y)=∫(τ,T]×E𝟙A∖{0}​(z)​𝒩​(d​t,d​z).\displaystyle Q(\mathrm{d}t,\mathrm{d}y)=\int\_{(\tau,T]\times E}\mathds{1}\_{A\setminus\{0\}}(z)\mathcal{N}(\mathrm{d}t,\mathrm{d}z). |  |

The compensating measure of QQ is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | LQ​(d​t,d​y)\displaystyle L^{Q}(\mathrm{d}t,\mathrm{d}y) | =𝟙A∖{0}​(z)​L𝒩​(d​t,d​z)=𝟙A∖{0}​(z)​κt​(Xt−τ,ζ,d​z)​Cλ​d​t\displaystyle=\mathds{1}\_{A\setminus\{0\}}(z)L^{\mathcal{N}}(\mathrm{d}t,\mathrm{d}z)=\mathds{1}\_{A\setminus\{0\}}(z)\kappa\_{t}(X\_{t-}^{\tau,\zeta},\mathrm{d}z)C\_{\lambda}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λt​(Xt−τ,ζ)​rt​(Xt−τ,ζ,d​z)​d​t=μt​(Xt−τ,ζ,d​z)​d​t.\displaystyle=\lambda\_{t}(X\_{t-}^{\tau,\zeta})r\_{t}(X\_{t-}^{\tau,\zeta},\mathrm{d}z)\mathrm{d}t=\mu\_{t}(X\_{t-}^{\tau,\zeta},\mathrm{d}z)\mathrm{d}t. |  |

This shows that Xt,ζX^{t,\zeta} constructed here indeed is a solution of ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")).
∎

### 2.2. Distribution dependent jump process

Now we consider the distribution-dependent SDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.4) |  | X¯tτ,ζ\displaystyle\bar{X}\_{t}^{\tau,\zeta} | =Y+∫(τ,t]∫Az​Q¯​(d​s,d​z),\displaystyle=Y+\int\_{(\tau,t]}\int\_{A}z\,\bar{Q}(ds,dz), |  |

where YY has distribution ζ∈𝒫1​(E)\zeta\in\mathcal{P}^{1}(E) and Q¯\bar{Q} is a random counting measure with compensating measure

|  |  |  |
| --- | --- | --- |
|  | L¯​(d​t,d​z)=μt​(X¯t−τ,ζ,η¯tτ,ζ,d​z)​d​t.\displaystyle\bar{L}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(\bar{X}^{\tau,\zeta}\_{t-},\bar{\eta}\_{t}^{\tau,\zeta},\mathrm{d}z)\mathrm{d}t. |  |

Here η¯tτ,ζ:=X¯tτ,ζ​(P)\bar{\eta}\_{t}^{\tau,\zeta}:=\bar{X}\_{t}^{\tau,\zeta}(\amsmathbb{P}) debntes the law of X¯tτ,ζ\bar{X}\_{t}^{\tau,\zeta} at time tt. The notable difference to ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) is that the intensity kernel μt​(d​z,x,ρ)=λt​(x,ρ)​rt​(x,ρ,d​z)\mu\_{t}(\mathrm{d}z,x,\rho)=\lambda\_{t}(x,\rho)r\_{t}(x,\rho,\mathrm{d}z) now is allowed to be measure-dependent. As one inserts η¯tτ,ζ\bar{\eta}\_{t}^{\tau,\zeta}, the process depends on its own distribution and therefore further regularity conditions are necessary in order to obtain existence and uniqueness.

###### Assumption 1.

Assume that there exists some q≥1q\geq 1 such that:

1. (1)

   There exists Cλ,Cr>0C\_{\lambda},C\_{r}>0 such that:

   |  |  |  |
   | --- | --- | --- |
   |  | λt​(x,ρ)≤Cλand∫A‖z‖q​rt​(x,ρ,d​z)≤Cr\displaystyle\lambda\_{t}(x,\rho)\leq C\_{\lambda}\quad\text{and}\quad\int\_{A}\|z\|^{q}\,r\_{t}(x,\rho,\mathrm{d}z)\leq C\_{r} |  |

   for all t∈[0,T]t\in[0,T], x∈Ex\in E, ρ∈𝒫q​(E)\rho\in\mathcal{P}^{q}(E).
2. (2)

   There exists Cμ>0C\_{\mu}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | dK​R0​(μt​(x1,ρ1,d​z),μt​(x2,ρ2,d​z))≤Cμ​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle d\_{KR}^{0}(\mu\_{t}(x\_{1},\rho\_{1},\mathrm{d}z),\mu\_{t}(x\_{2},\rho\_{2},\mathrm{d}z))\leq C\_{\mu}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

   for all x1,x2∈Ex\_{1},x\_{2}\in E and ρ1,ρ2∈𝒫q​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{q}(E).

###### Theorem 2.6.

Let ζ∈𝒫q​(E)\zeta\in\mathcal{P}^{q}(E) and assume that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") holds. Then there exists a unique weak solution of the distribution dependent SDE ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")).

###### Proof.

Theorem [2.6](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") is a time-inhomogenous pure jump version of Theorem 2.2 in [Graham1992-2], which shows existence and uniqueness for a time-homogeneous jump diffusion process. The proof of Theorem [2.6](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") uses similar methods and is included in Appendix [B](https://arxiv.org/html/2511.04198v1#A2 "Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance").
∎

As in the jump process case, the stochastic process X¯τ,ζ\bar{X}^{\tau,\zeta} has càdlàg paths and can thus be viewed as a random variable taking values in the space D​([τ,T],E)\amsmathbb{D}([\tau,T],E) and the distribution of X¯τ,ζ\bar{X}^{\tau,\zeta} given by Q¯τ,ζ:=X¯τ,ζ​(P)\bar{\amsmathbb{Q}}\_{\tau,\zeta}:=\bar{X}^{\tau,\zeta}(\amsmathbb{P}) is an element of 𝒫1​(D​([τ,T],E))\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],E)). Theorem [2.6](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") yields existence and uniqueness of Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta}.

Similarly to ([2.2](https://arxiv.org/html/2511.04198v1#S2.E2 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), we can now for each x∈Ex\in E consider the linearised SDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.5) |  | X~tτ,x\displaystyle\widetilde{X}\_{t}^{\tau,x} | =x+∫(τ,t]∫Az​Q~​(d​t,d​z),\displaystyle=x+\int\_{(\tau,t]}\int\_{A}z\,\widetilde{Q}(\mathrm{d}t,\mathrm{d}z), |  |

where Q~\widetilde{Q} is a random counting measure with compensating measure

|  |  |  |
| --- | --- | --- |
|  | L~​(d​t,d​z)=μt​(X~t−τ,x,η¯tτ,ζ,d​z)​d​t,\displaystyle\widetilde{L}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(\widetilde{X}^{\tau,x}\_{t-},\bar{\eta}\_{t}^{\tau,\zeta},\mathrm{d}z)\mathrm{d}t, |  |

and where η¯tτ,ζ=X¯tτ,ζ​(P)\bar{\eta}\_{t}^{\tau,\zeta}=\bar{X}^{\tau,\zeta}\_{t}(\amsmathbb{P}) is considered known and fixed. The process X~τ,x\widetilde{X}^{\tau,x} thus does not depend on its own distribution, but rather on the distribution of X¯τ,ζ\bar{X}^{\tau,\zeta}. As (η¯tτ,ζ)t∈[τ,T](\bar{\eta}\_{t}^{\tau,\zeta})\_{t\in[\tau,T]} is known, we can apply Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") to get that ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) has a unique solution for all x∈Ex\in E. We write Q~τ,ζx:=X~τ,x​(P)\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}:=\widetilde{X}^{\tau,x}(\amsmathbb{P}) and now have the following analogue to Theorem [2.2](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance"):

###### Theorem 2.7.

The familiy (Q~τ,ζx)x∈E(\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x})\_{x\in E} constitutes a regular conditional distribution of Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta} given X¯ττ,ζ=x\bar{X}\_{\tau}^{\tau,\zeta}=x. Thus it holds that

|  |  |  |
| --- | --- | --- |
|  | Q¯τ,ζ​(d​ω)=∫EQ~τ,ζx​(d​ω)​ζ​(d​x).\displaystyle\bar{\amsmathbb{Q}}\_{\tau,\zeta}(\mathrm{d}\omega)=\int\_{E}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}(\mathrm{d}\omega)\zeta(\mathrm{d}x). |  |

###### Proof.

See Appendix [A](https://arxiv.org/html/2511.04198v1#A1 "Appendix A Proof of Theorems 2.2 and 2.7 ‣ Mean-field approximations in insurance").
∎

Thus we have that the conditional path-law of the distribution dependent SDE ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) given that the initial state is x∈Ex\in E is equal to Q~τ,ζx\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}, which is the path-law of the linearised SDE ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). As a consequence, the transition probabilities of X¯τ,ζ\bar{X}^{\tau,\zeta} are given by η~tτ,ζ​(x,⋅):=X~tτ,x​(P)\widetilde{\eta}\_{t}^{\tau,\zeta}(x,\cdot):=\widetilde{X}\_{t}^{\tau,x}(\amsmathbb{P}). As ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), given (η¯tζ,τ)t∈[τ,T](\bar{\eta}\_{t}^{\zeta,\tau})\_{t\in[\tau,T]}, has no distribution dependence, we can invoke Proposition [2.3](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") to conclude that, given (η¯tζ,τ)t∈[τ,T](\bar{\eta}\_{t}^{\zeta,\tau})\_{t\in[\tau,T]}, the transition probabilities η~tτ,ζ​(x,B)\widetilde{\eta}\_{t}^{\tau,\zeta}(x,B) satisfy the linear forward integro-differential equations:

###### Proposition 2.8.

Given (η¯tτ,ζ)t∈[τ,T](\bar{\eta}\_{t}^{\tau,\zeta})\_{t\in[\tau,T]} the transition probabilities ηxτ,ζ​(t,B)\eta\_{x}^{\tau,\zeta}(t,B) satisfy the forward integro-differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​η~tτ,ζ​(x,B)=\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\widetilde{\eta}\_{t}^{\tau,\zeta}(x,B)= | ∫E∖B∫A𝟙B​(y+z)​μt​(y,η¯tτ,ζ,d​z)​η~tτ,ζ​(x,d​y)\displaystyle\int\_{E\setminus B}\int\_{A}\mathds{1}\_{B}(y+z)\mu\_{t}(y,\bar{\eta}\_{t}^{\tau,\zeta},dz)\widetilde{\eta}\_{t}^{\tau,\zeta}(x,\mathrm{d}y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫B∫A𝟙E∖B​(y+z)​μt​(y,η¯tτ,ζ,d​z)​η~tτ,ζ​(x,d​y),\displaystyle-\int\_{B}\int\_{A}\mathds{1}\_{E\setminus B}(y+z)\mu\_{t}(y,\bar{\eta}\_{t}^{\tau,\zeta},dz)\widetilde{\eta}\_{t}^{\tau,\zeta}(x,\mathrm{d}y), |  |

with η~ττ,ζ​(x,⋅)=δ{x}\widetilde{\eta}\_{\tau}^{\tau,\zeta}(x,\cdot)=\delta\_{\{x\}} and x∈Ex\in E.

Note that contrary to the transition probabilities ηtτ,x\eta\_{t}^{\tau,x} of Xτ,ζX^{\tau,\zeta}, the transition probabilities η~tτ,ζ​(x,⋅)\widetilde{\eta}\_{t}^{\tau,\zeta}(x,\cdot) of X¯τ,ζ\bar{X}^{\tau,\zeta} now depend on the initial distribution ζ\zeta through (η¯tτ,ζ)t∈[τ,T](\bar{\eta}\_{t}^{\tau,\zeta})\_{t\in[\tau,T]}, and while the forward equations are linear, we need to know (η¯tτ,ζ)t∈[τ,T](\bar{\eta}\_{t}^{\tau,\zeta})\_{t\in[\tau,T]} in order to actually calculate η~tτ,ζ​(x,⋅)\widetilde{\eta}\_{t}^{\tau,\zeta}(x,\cdot).

By Theorem [2.7](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") we obtain the following analogue of ([2.3](https://arxiv.org/html/2511.04198v1#S2.E3 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.6) |  | η¯tτ,ζ​(B)\displaystyle\bar{\eta}\_{t}^{\tau,\zeta}(B) | =∫Eη~tτ,ζ​(x,B)​ζ​(d​x).\displaystyle=\int\_{E}\widetilde{\eta}\_{t}^{\tau,\zeta}(x,B)\zeta(\mathrm{d}x). |  |

Using this we get that η¯tτ,ζ\bar{\eta}\_{t}^{\tau,\zeta} satisfies the following non-linear forward integro-differential equations:

###### Proposition 2.9.

The law η¯tτ,ζ\bar{\eta}\_{t}^{\tau,\zeta} satsifies the forward integro-differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​η¯tτ,ζ​(B)=\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\bar{\eta}\_{t}^{\tau,\zeta}(B)= | ∫E∖B∫A𝟙B​(y+z)​μt​(y,η¯tτ,ζ,d​z)​ηtτ,ζ​(d​y)\displaystyle\int\_{E\setminus B}\int\_{A}\mathds{1}\_{B}(y+z)\mu\_{t}(y,\bar{\eta}^{\tau,\zeta}\_{t},dz)\eta\_{t}^{\tau,\zeta}(\mathrm{d}y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫B∫A𝟙E∖B​(y+z)​μt​(y,ηtτ,ζ,d​z)​ηtτ,ζ​(d​y)​ds.\displaystyle-\int\_{B}\int\_{A}\mathds{1}\_{E\setminus B}(y+z)\mu\_{t}(y,\eta\_{t}^{\tau,\zeta},dz)\eta\_{t}^{\tau,\zeta}(\mathrm{d}y)\mathrm{d}s. |  |

with η¯ττ,ζ​(B)=ζ​(B)\bar{\eta}\_{\tau}^{\tau,\zeta}(B)=\zeta(B) for t≥τt\geq\tau and ζ∈𝒫q​(E)\zeta\in\mathcal{P}^{q}(E).

###### Proof.

Repeat the proof of Proposition [2.4](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") using ([2.6](https://arxiv.org/html/2511.04198v1#S2.E6 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) and Proposition [2.8](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem8 "Proposition 2.8. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") instead.
∎

###### Remark 2.10.

Note that Proposition [2.9](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem9 "Proposition 2.9. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") makes no statement about uniqueness of the non-linear equations. Thus numerical solutions should be treated with care.

###### Remark 2.11.

Due to ([2.6](https://arxiv.org/html/2511.04198v1#S2.E6 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), it is also possible to replace η¯tτ,ζ\bar{\eta}\_{t}^{\tau,\zeta} with ∫Eη~tτ,ζ​(x,⋅)​ζ​(d​x)\int\_{E}\widetilde{\eta}\_{t}^{\tau,\zeta}(x,\cdot)\zeta(\mathrm{d}x) in the forward equations of Proposition [2.8](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem8 "Proposition 2.8. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance"). In that case the system becomes non-linear as well, but in that case one would be able to calculate η~tτ,ζ​(x,B)\widetilde{\eta}\_{t}^{\tau,\zeta}(x,B) directly.

###### Remark 2.12.

The forward equations of Propositions [2.8](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem8 "Proposition 2.8. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [2.9](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem9 "Proposition 2.9. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") are the pure jump equivalent of the linearised and non-linear Fokker-Planck-Kolmogorov equations known from McKean-Vlasov diffusion processes, see [Rehmeier&Roeckner2024]. Therefore we conjecture that (Q¯τ,ζ)(τ,ζ)∈[0,T]×𝒫q​(E)(\bar{\amsmathbb{Q}}\_{\tau,\zeta})\_{(\tau,\zeta)\in[0,T]\times\mathcal{P}^{q}(E)} constitutes a non-linear Markov process in the sense of [Rehmeier&Roeckner2024].

### 2.3. Jump destination specification

So far we have specified the jump process in terms of jump sizes, but in many life insurance applications it is more natural to specify the jump process in terms of jump destinations. That is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.7) |  | X¯tτ,ζ\displaystyle\bar{X}\_{t}^{\tau,\zeta} | =Y+∫(τ,t]∫E(y−X¯s−τ,ζ)​Q¯d​(d​s,d​y),\displaystyle=Y+\int\_{(\tau,t]}\int\_{E}(y-\bar{X}^{\tau,\zeta}\_{s-})\bar{Q}^{d}(ds,dy), |  |

where Q¯d\bar{Q}^{d} is a random counting measure with compensating measure

|  |  |  |
| --- | --- | --- |
|  | L¯d​(d​t,d​y)=μtd​(X¯t−τ,ζ,η¯tτ,ζ,d​y)​d​t.\displaystyle\bar{L}^{d}(\mathrm{d}t,\mathrm{d}y)=\mu\_{t}^{d}(\bar{X}^{\tau,\zeta}\_{t-},\bar{\eta}\_{t}^{\tau,\zeta},\mathrm{d}y)\mathrm{d}t. |  |

The intensity kernel μtd(x,ρ,dy)=λt(x,ρ,)rtd(x,dy)\mu\_{t}^{d}(x,\rho,\mathrm{d}y)=\lambda\_{t}(x,\rho,)r\_{t}^{d}(x,\mathrm{d}y) is a bounded kernel on (E,ℬ​(E))(E,\mathcal{B}(E)), where rtd​(x,ρ,d​y)r\_{t}^{d}(x,\rho,\mathrm{d}y) specifies the distribution of the next jump destination, given that a jump occurs at time tt and that X¯t−τ,ζ=x\bar{X}\_{t-}^{\tau,\zeta}=x. Via a change of variables argument, it is possible to switch back and forth between the jump size specification ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) and the jump destination specification ([2.7](https://arxiv.org/html/2511.04198v1#S2.E7 "In 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance")).

In order to see this let x∈Ex\in E and define gx:A→Rdg\_{x}:A\rightarrow\amsmathbb{R}^{d} as gx​(z)=x+zg\_{x}(z)=x+z and hx:E→Rdh\_{x}:E\rightarrow\amsmathbb{R}^{d} as hx​(y)=y−xh\_{x}(y)=y-x. The function hxh\_{x} takes a jump destination and maps it to a jump size, while gxg\_{x} takes a jump size and maps it to a potential jump destination. We now have the following result:

###### Proposition 2.13.

Let x∈Ex\in E and let gx:A→Rdg\_{x}:A\rightarrow\amsmathbb{R}^{d} be given by gx​(z)=x+zg\_{x}(z)=x+z. Then the solution of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) is a solution to ([2.7](https://arxiv.org/html/2511.04198v1#S2.E7 "In 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) with

|  |  |  |
| --- | --- | --- |
|  | μtd​(x,ρ,B)=μt​(x,ρ,gx−1​(B))∀B∈ℬ​(E).\displaystyle\mu^{d}\_{t}(x,\rho,B)=\mu\_{t}(x,\rho,g\_{x}^{-1}(B))\quad\forall B\in\mathcal{B}(E). |  |

Let x∈Ex\in E and let hx:E→Ah\_{x}:E\rightarrow A be given by hx​(y)=y−xh\_{x}(y)=y-x. Then the solution of ([2.7](https://arxiv.org/html/2511.04198v1#S2.E7 "In 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) is a solution to ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) with

|  |  |  |
| --- | --- | --- |
|  | μt​(x,ρ,B)=μtd​(x,ρ,hx−1​(B))∀B∈ℬ​(A).\displaystyle\mu\_{t}(x,\rho,B)=\mu^{d}\_{t}(x,\rho,h\_{x}^{-1}(B))\quad\forall B\in\mathcal{B}(A). |  |

###### Proof.

Let Nt=Q¯​([τ,t]×A)N\_{t}=\bar{Q}([\tau,t]\times A). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | X¯tτ,ζ\displaystyle\bar{X}\_{t}^{\tau,\zeta} | =∫(τ,t]×Az​Q¯​(d​s,d​z)=Y+∑iNt(X¯Ti−τ,ζ+Zi)−X¯Ti−τ,ζ\displaystyle=\int\_{(\tau,t]\times A}z\,\bar{Q}(\mathrm{d}s,\mathrm{d}z)=Y+\sum\_{i}^{N\_{t}}(\bar{X}\_{T\_{i}-}^{\tau,\zeta}+Z\_{i})-\bar{X}^{\tau,\zeta}\_{T\_{i}-} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Y+∑i=1Nt(gX¯Ti−τ,ζ​(Zi)−X¯Ti−)=Y+∫(τ,T]×E(y−X¯t−τ,ζ)​Qd​(d​t,d​y),\displaystyle=Y+\sum\_{i=1}^{N\_{t}}(g\_{\bar{X}\_{T\_{i}-}^{\tau,\zeta}}(Z\_{i})-\bar{X}\_{T\_{i}-})=Y+\int\_{(\tau,T]\times E}(y-\bar{X}\_{t-}^{\tau,\zeta})Q^{d}(\mathrm{d}t,\mathrm{d}y), |  |

where QdQ^{d} has the same jump times as QQ and marks Yi:=gX¯Ti−τ,ζ​(Zi)Y\_{i}:=g\_{\bar{X}\_{T\_{i}-}^{\tau,\zeta}}(Z\_{i}). Thus we have that

|  |  |  |
| --- | --- | --- |
|  | μtd​(x,ρ1,B)=μt​(x,ρ1,gx−1​(B)),∀B∈ℬ​(E).\displaystyle\mu^{d}\_{t}(x,\rho\_{1},B)=\mu\_{t}(x,\rho\_{1},g\_{x}^{-1}(B)),\quad\forall B\in\mathcal{B}(E). |  |

Similary let Ntd=Q¯d​([τ,t]×E)N\_{t}^{d}=\bar{Q}^{d}([\tau,t]\times E). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | X¯tτ,ζ\displaystyle\bar{X}\_{t}^{\tau,\zeta} | =Y+∫(τ,T]×E(y−X¯t−τ,ζ)​Q¯d​(d​t,d​y)=Y+∑i=1NtdhX¯Ti−τ,ζ​(Yi)\displaystyle=Y+\int\_{(\tau,T]\times E}(y-\bar{X}\_{t-}^{\tau,\zeta})\bar{Q}^{d}(\mathrm{d}t,\mathrm{d}y)=Y+\sum\_{i=1}^{N\_{t}^{d}}h\_{\bar{X}\_{T\_{i}-}^{\tau,\zeta}}(Y\_{i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Y+∫(τ,T]×Az​Q¯​(d​t,d​z),\displaystyle=Y+\int\_{(\tau,T]\times A}z\,\bar{Q}(\mathrm{d}t,\mathrm{d}z), |  |

where Q¯\bar{Q} has the same jump times as Q¯d\bar{Q}^{d} and jump marks Zi:=hX¯Ti−d​(Yi)Z\_{i}:=h\_{\bar{X}\_{T\_{i}-}^{d}}(Y\_{i}). Thus we have that

|  |  |  |
| --- | --- | --- |
|  | μt​(x,ρ,B)=μtd​(x,ρ,hx−1​(B))∀B∈ℬ​(A).\displaystyle\mu\_{t}(x,\rho,B)=\mu^{d}\_{t}(x,\rho,h\_{x}^{-1}(B))\quad\forall B\in\mathcal{B}(A). |  |

∎

This shows that if ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) exists and is unique, then the corresponding jump destination specification as given by Proposition [2.13](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem13 "Proposition 2.13. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") exists and is unique and vice versa. In particular we can prove that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") ensuring existence and uniqueness of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) is equivalent to:

###### Assumption 2.

There exists a q≥1q\geq 1 such that

1. (1)

   There exists Cλ,Cr>0C\_{\lambda},C\_{r}>0 such that:

   |  |  |  |
   | --- | --- | --- |
   |  | λt​(x,ρ)≤Cλand∫E‖y−x‖q​rtd​(x,ρ,d​y)≤Cr\displaystyle\lambda\_{t}(x,\rho)\leq C\_{\lambda}\quad\text{and}\quad\int\_{E}\|y-x\|^{q}\,r^{d}\_{t}(x,\rho,\mathrm{d}y)\leq C\_{r} |  |

   For all t∈[0,T]t\in[0,T], x∈Ex\in E, ρ∈𝒫q​(E)\rho\in\mathcal{P}^{q}(E).
2. (2)

   There exists Cμ>0C\_{\mu}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | dK​Rx2​(μtd​(x1,ρ1,d​y),μtd​(x2,ρ2,d​y))≤Cμ​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle d\_{KR}^{x\_{2}}(\mu\_{t}^{d}(x\_{1},\rho\_{1},\mathrm{d}y),\mu\_{t}^{d}(x\_{2},\rho\_{2},\mathrm{d}y))\leq C\_{\mu}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

   for all x1,x2∈Ex\_{1},x\_{2}\in E and ρ1,ρ2∈𝒫q​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{q}(E).

###### Proposition 2.14.

Let μt​(x,ρ,d​z)\mu\_{t}(x,\rho,\mathrm{d}z) satisfy Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance"). Then μtd​(x,ρ,d​y)\mu^{d}\_{t}(x,\rho,\mathrm{d}y) given by

|  |  |  |
| --- | --- | --- |
|  | μtd​(x,ρ,B)=μt​(x,ρ,gx−1​(B))∀B∈ℬ​(E),\displaystyle\mu^{d}\_{t}(x,\rho,B)=\mu\_{t}(x,\rho,g\_{x}^{-1}(B))\quad\forall B\in\mathcal{B}(E), |  |

satisfies Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance").

Let μtd​(x,ρ,d​y)\mu^{d}\_{t}(x,\rho,\mathrm{d}y) satisfy Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance"). Then μt​(x,ρ,d​z)\mu\_{t}(x,\rho,\mathrm{d}z) given by

|  |  |  |
| --- | --- | --- |
|  | μt​(x,ρ,B)=μtd​(x,ρ,hx−1​(B))∀B∈ℬ​(A).\displaystyle\mu\_{t}(x,\rho,B)=\mu^{d}\_{t}(x,\rho,h\_{x}^{-1}(B))\quad\forall B\in\mathcal{B}(A). |  |

satisfies Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance").

###### Proof.

We only prove the first statement, as the second follows by a similar argument. Given that μ\mu satisfies Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") a simple change of variable argument gives that μd\mu^{d} satisfies Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1).

In order to prove that Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(2) is satisfied, let f:E→Rf:E\rightarrow\amsmathbb{R} be Lip​(1)\text{Lip}(1) with f​(x2)=0f(x\_{2})=0. We can then write

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ef​(y)​μtd​(x,ρ,d​y)\displaystyle\int\_{E}f(y)\mu\_{t}^{d}(x,\rho,\mathrm{d}y) | =∫gx−1​(E)f​(gx​(z))​μt​(x,ρ,d​z)=∫Af~​(gx​(z))​μt​(x,ρ,d​z).\displaystyle=\int\_{g\_{x}^{-1}(E)}f(g\_{x}(z))\mu\_{t}(x,\rho,\mathrm{d}z)=\int\_{A}\widetilde{f}(g\_{x}(z))\mu\_{t}(x,\rho,\mathrm{d}z). |  |

The first equality is due to a change of variables. In order to achieve the second equality, we first have to extend ff, since ff is only defined on EE and E⊆gx​(A)E\subseteq g\_{x}(A). This can be achieved by setting f~​(y):=infx∈E{f​(x)+‖x−y‖}\widetilde{f}(y):=\inf\_{x\in E}\{f(x)+\|x-y\|\}. Note that f~\widetilde{f} still is a Lip​(1)\text{Lip}(1)-function with f~​(y)=f​(y)\widetilde{f}(y)=f(y) for all y∈Ey\in E and so f~​(x2)=0\widetilde{f}(x\_{2})=0. Thus the equality follows since μt​(x,ρ,A∖gx−1​(E))=0\mu\_{t}(x,\rho,A\setminus g\_{x}^{-1}(E))=0 and f~​(x+z)=f​(x+z)\widetilde{f}(x+z)=f(x+z) for all z∈gx−1​(E)z\in g\_{x}^{-1}(E).

Now using the above equality we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∫Ef(y)\displaystyle\bigg|\int\_{E}f(y) | μtd(x1,ρ1,dy)−∫Ef(y)μtd(x2,ρ2,dy)|\displaystyle\mu\_{t}^{d}(x\_{1},\rho\_{1},\mathrm{d}y)-\int\_{E}f(y)\mu\_{t}^{d}(x\_{2},\rho\_{2},\mathrm{d}y)\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | |∫Af~​(gx1​(z))​μt​(x1,ρ1,d​z)−∫Af~​(gx2​(z))​μt​(x2,ρ2,d​z)|\displaystyle\bigg|\int\_{A}\widetilde{f}(g\_{x\_{1}}(z))\mu\_{t}(x\_{1},\rho\_{1},\mathrm{d}z)-\int\_{A}\widetilde{f}(g\_{x\_{2}}(z))\mu\_{t}(x\_{2},\rho\_{2},\mathrm{d}z)\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | |∫Af~​(gx2​(z))​μt​(x1,ρ1,d​z)−∫Af~​(gx2​(z))​μt​(x2,ρ2,d​z)|\displaystyle\bigg|\int\_{A}\widetilde{f}(g\_{x\_{2}}(z))\mu\_{t}(x\_{1},\rho\_{1},\mathrm{d}z)-\int\_{A}\widetilde{f}(g\_{x\_{2}}(z))\mu\_{t}(x\_{2},\rho\_{2},\mathrm{d}z)\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|∫Af~​(gx1​(z))−f~​(gx2​(z))​μt​(x1,ρ1,d​z)|\displaystyle+\bigg|\int\_{A}\widetilde{f}(g\_{x\_{1}}(z))-\widetilde{f}(g\_{x\_{2}}(z))\mu\_{t}(x\_{1},\rho\_{1},\mathrm{d}z)\bigg| |  |

Note that for any f∈Lip​(1)f\in\text{Lip}(1) with f​(x2)=0f(x\_{2})=0 we have that z↦f~​(gx2​(z))z\mapsto\widetilde{f}(g\_{x\_{2}}(z)) is a Lip​(1)\text{Lip}(1)-function which is zero for z=0z=0. Thus the first term can be bounded by dK​R0​(μt​(x1,ρ1,d​z),μt​(x2,ρ2,d​z))d\_{KR}^{0}(\mu\_{t}(x\_{1},\rho\_{1},\mathrm{d}z),\mu\_{t}(x\_{2},\rho\_{2},\mathrm{d}z)).
Furthermore since (x,z)↦f~​(gx​(z))(x,z)\mapsto\widetilde{f}(g\_{x}(z)) is a Lip​(1)\text{Lip}(1)-function, applying Jensen’s inequality, Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1) and the afore mentioned Lipschitz property to the last term yields the bound Cλ​‖x1−x2‖C\_{\lambda}\|x\_{1}-x\_{2}\|. By Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(2) we thus arrive at

|  |  |  |
| --- | --- | --- |
|  | dK​Rx2​(μtd​(x1,ρ1,d​y),μtd​(x2,ρ2,d​y))≤(Cλ+Cμ)​(‖x1−x2‖+dW​(ρ1,ρ2)).\displaystyle d\_{KR}^{x\_{2}}(\mu\_{t}^{d}(x\_{1},\rho\_{1},\mathrm{d}y),\mu\_{t}^{d}(x\_{2},\rho\_{2},\mathrm{d}y))\leq(C\_{\lambda}+C\_{\mu})(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})). |  |

∎

## 3. Mean-field approximation

For any n∈Nn\in\amsmathbb{N}, let Xn=(Xℓ,n)ℓ=1,…,nX^{n}=(X^{\ell,n})\_{\ell=1,\ldots,n} be a family of stochastic processes, with state space EnE^{n}, given by the following system of SDEs

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | Xtℓ,n=Yℓ,n+∫(τ,t]×Az​Qℓ,n​(d​s,d​z),ℓ=1,…,n,\displaystyle X\_{t}^{\ell,n}=Y^{\ell,n}+\int\_{(\tau,t]\times A}z\,Q^{\ell,n}(ds,dz),\quad\ell=1,\ldots,n, |  |

where the random counting measures Qℓ,nQ^{\ell,n} have compensating measures

|  |  |  |
| --- | --- | --- |
|  | Lℓ,n​(d​t,d​z)=μt​(Xt−ℓ,n,εt−n,d​z)​d​t,ℓ=1,…,n.\displaystyle L^{\ell,n}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}z)\mathrm{d}t,\quad\ell=1,\ldots,n. |  |

The single coordinate processes Xℓ,nX^{\ell,n} only depend on the other coordinate process through their common empirical distribution εtn\varepsilon\_{t}^{n} given by

|  |  |  |
| --- | --- | --- |
|  | εtn:=1n​∑ℓ=1nδ{Xtℓ,n}.\displaystyle\varepsilon\_{t}^{n}:=\frac{1}{n}\sum\_{\ell=1}^{n}\delta\_{\{X\_{t}^{\ell,n}\}}. |  |

We assume that the probability for simultaneous jumps across ℓ\ell is zero, which makes it possible to view XnX^{n} as one SDE with values in EnE^{n} driven by a random counting measure defined on state space ⋃ℓ=1nA×{ℓ}\bigcup\_{\ell=1}^{n}A\times\{\ell\}. Thus existence and uniqueness of a solution to the system ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) is guaranteed by Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance").

Let Qτ,ζnn:=Xn​(P)\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n}:=X^{n}(\amsmathbb{P}) denote the path-law of the entire process XnX^{n} and for k<nk<n let Qτ,ζnn,k:=(X1,n,…,Xk,n)​(P)\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n,k}:=(X^{1,n},\ldots,X^{k,n})(\amsmathbb{P}) denote the marginal path-law of the first kk coordinates of the process XnX^{n}. Each coordinate can be interpreted as an individual, while XnX^{n} is the joint model for a cohort of nn individuals. The common dependence on the empirical measure can be interpreted as dependence on collective quantities, such as cohort averages. As all individuals in ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) are dependent, it is computationally infeasible to calculate any quantities of interest such as expected values of path-functionals, especially if nn is large. This would require keeping track of each individual’s state, causing the system of forward equations of Propositions [2.4](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [2.3](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") to explode in dimension. In particular, if the system of forward-equations has mm equations for one individual, then it will have mnm^{n} equations for nn individuals.

Instead we suggest to use a mean-field approximation, where we replace the empirical distribution εt−n\varepsilon\_{t-}^{n} with the law of the process, thus yielding a non-linear jump process of the form ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). In order for this to be a valid approximation we have to show that (Qτ,ζnn)n∈N(\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n})\_{n\in\amsmathbb{N}} is chaotic.

###### Definition 3.1.

Let (S,dS)(S,d\_{S}) be a Polish space, Q\amsmathbb{Q} a probability measure on SS and let (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} be sequence of exchangeable probability measures, each defined on SnS^{n}, with kk-marginals Qn,k:=Q(⋅×Sn−k)\amsmathbb{Q}^{n,k}:=\amsmathbb{Q}(\cdot\times S^{n-k}) for k<nk<n. Then the sequence (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} is Q\amsmathbb{Q}-chaotic if for any fixed k∈Nk\in\amsmathbb{N} it holds that

|  |  |  |
| --- | --- | --- |
|  | Qn,k→wk.Q⊗kas ​n→∞.\displaystyle\amsmathbb{Q}^{n,k}\stackrel{{\scriptstyle wk.}}{{\rightarrow}}\amsmathbb{Q}^{\otimes k}\quad\text{as }n\rightarrow\infty. |  |

###### Remark 3.2.

Assuming that each Qn\amsmathbb{Q}^{n} is the distribution of the random variables (X1,n,…,Xn,n)(X^{1,n},\ldots,X^{n,n}), we have that Qn\amsmathbb{Q}^{n} is exchangeable if

|  |  |  |
| --- | --- | --- |
|  | (X1,n,…,Xn,n)=d(Xσ​(1),n,…,Xσ​(n),n)\displaystyle(X^{1,n},\ldots,X^{n,n})\stackrel{{\scriptstyle d}}{{=}}(X^{\sigma(1),n},\ldots,X^{\sigma(n),n}) |  |

for each permutation σ:{1,…,n}→{1,…,n}\sigma:\{1,\ldots,n\}\rightarrow\{1,\ldots,n\}. Intuitively this means that the joint distribution of the individuals does not change when reordering them and in particular this implies that all individuals have the same marginal distribution. A sufficient, but not necessary condition for this to hold is that all individuals are independent and identically distributed.

Intuitively this means that any fixed number of individuals becomes independent and identically distributed with distribution Q\amsmathbb{Q}, when the overall number of individuals tends to infinity.

Definition [3.1](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") goes back to [Kac1956], but as chaosticity is equivalent to weak convergence of the marginals Qn,k\amsmathbb{Q}^{n,k} to the product measure Q⊗k\amsmathbb{Q}^{\otimes k}, it is possible to relate the notion of chaosticity to convergence in a metric space (see [Hauray&Mischler2014] for chaosticity in terms of different metrics). We will use the slightly stronger notion of Wasserstein(1)-chaos in the space (𝒫1​(S),dW)(\mathcal{P}^{1}(S),d\_{W}), since (ρn)n∈N⊂𝒫1​(S)(\rho\_{n})\_{n\in\amsmathbb{N}}\subset\mathcal{P}^{1}(S) converges weakly to ρ∈𝒫1​(S)\rho\in\mathcal{P}^{1}(S) if and only if limn→∞dW​(ρn,ρ)=0\lim\_{n\rightarrow\infty}d\_{W}(\rho\_{n},\rho)=0 (see Theorem 6.9 in [Villani2009]).

###### Definition 3.3.

Let (S,dS)(S,d\_{S}) be a Polish space, Q∈𝒫1​(S)\amsmathbb{Q}\in\mathcal{P}^{1}(S) a probability measure on SS and let (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} be sequence of symmetric probability measures, each defined on SnS^{n} and in 𝒫1​(Sn)\mathcal{P}^{1}(S^{n}). Then the sequence (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} is Q\amsmathbb{Q}-Wasserstein(1)-chaotic if and only if for any k∈Nk\in\amsmathbb{N} it holds that

|  |  |  |
| --- | --- | --- |
|  | limn→∞dW​(Qn,k,Q⊗k)=0,∀k∈N,\displaystyle\lim\_{n\rightarrow\infty}d\_{W}(\amsmathbb{Q}^{n,k},\amsmathbb{Q}^{\otimes k})=0,\quad\forall k\in\amsmathbb{N}, |  |

where Qn,k\amsmathbb{Q}^{n,k} denotes the marginal distribution of the first kk individuals.

###### Remark 3.4.

Note that Wasserstein(1)-chaos is stronger than the notion of chaos in Definition [3.1](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"), since we have restricted the set of probability measures to 𝒫1​(S)\mathcal{P}^{1}(S). If (S,dS)(S,d\_{S}) is a bounded metric space, then the Wasserstein(1) distance metrizes weak convergence in 𝒫​(S)\mathcal{P}(S) (the set of all probability measures on SS), see Corollary 6.13 in [Villani2009], in which case Definition [3.3](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") can be extended to hold for all of 𝒫​(S)\mathcal{P}(S).

In our case the Polish space (S,dS)(S,d\_{S}) is (D​([τ,T],E),dJ1)(\amsmathbb{D}([\tau,T],E),d^{J\_{1}}), the sequence of probability measures for which we want to prove chaosticity are the path-laws (Qτ,ζnn)n∈N(\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n})\_{n\in\amsmathbb{N}} and the measure for which we would like the sequence to be chaotic for is Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta}. Note that each Qτ,ζnn\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n} should be exchangeable in the sense of Remark [3.2](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"), which is the case, if the initial distribution ζn\zeta^{n} is exchangeable, the intensity kernels of the random counting measures Qℓ,nQ^{\ell,n} are the same for all 1≤ℓ≤n1\leq\ell\leq n and the coordinates depend on each other in a symmetric way through εt−n\varepsilon\_{t-}^{n} only. Therefore we make the following assumption:

###### Assumption 3.

There exists a q>1q>1 such that:

1. (1)

   For all n∈Nn\in\amsmathbb{N} it holds that ζn∈𝒫q​(E)\zeta^{n}\in\mathcal{P}^{q}(E).
2. (2)

   There exists ζ∈𝒫q​(E)\zeta\in\mathcal{P}^{q}(E) such that

   |  |  |  |
   | --- | --- | --- |
   |  | limn→∞dW​(ζn,k,ζ)=0∀k∈N.\displaystyle\lim\_{n\rightarrow\infty}d\_{W}(\zeta^{n,k},\zeta)=0\quad\forall k\in\amsmathbb{N}. |  |
3. (3)

   The intensity kernel μt​(x,ρ,d​z)=λt​(x,ρ)​rt​(x,ρ,d​z)\mu\_{t}(x,\rho,\mathrm{d}z)=\lambda\_{t}(x,\rho)r\_{t}(x,\rho,\mathrm{d}z) does not depend on 1≤ℓ≤n1\leq\ell\leq n.

Note that we now require q>1q>1, contrary to Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") which only requires q≥1q\geq 1. We now have the following result:

###### Theorem 3.5.

Let (Qτ,ζnn)n∈N(\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n})\_{n\in\amsmathbb{N}} be the path-law of ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) and Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta} be the path-law of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). Assume that Assumptions [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") are satisfied. Then for any fixed k∈Nk\in\amsmathbb{N}, it holds that

|  |  |  |
| --- | --- | --- |
|  | limn→∞dWJ1​(Qτ,ζnn,k,Q¯τ,ζ⊗k)=0\displaystyle\lim\_{n\rightarrow\infty}d\_{W}^{J\_{1}}(\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n,k},\bar{\amsmathbb{Q}}\_{\tau,\zeta}^{\otimes k})=0 |  |

###### Remark 3.6.

Consider the jump destination specification of ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance"))

|  |  |  |
| --- | --- | --- |
|  | Xtℓ,n=Yℓ,n+∫(τ,t]×E(y−Xs−ℓ,n)​Qdℓ,n​(d​s,d​y),ℓ=1,…,n,\displaystyle X\_{t}^{\ell,n}=Y^{\ell,n}+\int\_{(\tau,t]\times E}(y-X\_{s-}^{\ell,n})\,Q^{\ell,n}\_{d}(ds,dy),\quad\ell=1,\ldots,n, |  |

where the random counting measures Qdℓ,nQ^{\ell,n}\_{d} have compensating measures

|  |  |  |
| --- | --- | --- |
|  | Ldℓ,n​(d​t,d​y)=μtd​(Xt−ℓ,n,εt−n,d​y)​d​t,ℓ=1,…,n.\displaystyle L^{\ell,n}\_{d}(\mathrm{d}t,\mathrm{d}y)=\mu\_{t}^{d}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}y)\mathrm{d}t,\quad\ell=1,\ldots,n. |  |

By Propositions [2.13](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem13 "Proposition 2.13. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [2.14](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem14 "Proposition 2.14. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") we know that this jump destination specification satisfying Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") leads to an equivalent jump size representation ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) satisfying Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and therefore Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") is still valid for the jump destination specification.

### 3.1. Proof of Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance")

Before we begin, we will state one lemma, on which the proof heavily relies on.

###### Lemma 3.7.

Let η∈𝒫​(Rd)\eta\in\mathcal{P}(\amsmathbb{R}^{d}). Assume that mq:=∫Rd‖x‖q​η​(d​s)<∞m\_{q}:=\int\_{\amsmathbb{R}^{d}}\|x\|^{q}\eta(\mathrm{d}s)<\infty for q>1q>1 and let (Xℓ)ℓ∈N(X^{\ell})\_{\ell\in\amsmathbb{N}} be an iid sequence with Xℓ∼ηX^{\ell}\sim\eta. Then there exists a constant C​(d,q)>0C(d,q)>0 such that for all n∈Nn\in\amsmathbb{N}:

|  |  |  |
| --- | --- | --- |
|  | dW​(εn,η)≤C​(d,q)​mq1q​β​(n),\displaystyle d\_{W}(\varepsilon^{n},\eta)\leq C(d,q)m\_{q}^{\frac{1}{q}}\beta(n), |  |

where

|  |  |  |
| --- | --- | --- |
|  | β​(n)={n−12+n−q−1qif ​d=1​ and ​q≠2log⁡(1+n)n12+n−q−1qif ​d=2​ and ​q≠2n−1d+n−q−1qif ​d>2​ and ​q≠dd−1\displaystyle\beta(n)=\begin{cases}n^{-\frac{1}{2}}+n^{-\frac{q-1}{q}}&\text{if }d=1\text{ and }q\neq 2\\ \frac{\log(1+n)}{n^{\frac{1}{2}}}+n^{-\frac{q-1}{q}}&\text{if }d=2\text{ and }q\neq 2\\ n^{-\frac{1}{d}}+n^{-\frac{q-1}{q}}&\text{if }d>2\text{ and }q\neq\frac{d}{d-1}\end{cases} |  |

###### Proof.

This is corresponds to Theorem 1 in [Fournier2015] with p=1p=1.
∎

The idea of the proof is to construct a coupling between Qτ,ζnn,k\amsmathbb{Q}^{n,k}\_{\tau,\zeta^{n}} and Q¯τ,ζ⊗k\bar{\amsmathbb{Q}}\_{\tau,\zeta}^{\otimes k}, since

|  |  |  |
| --- | --- | --- |
|  | dWJ1​(Qτ,ζnn,k,Q¯τ,ζ⊗k)≤dWU​(Qτ,ζnn,k,Q¯τ,ζ⊗k)≤∑ℓ=1kE​[supτ≤t≤T‖Xtℓ,n−X¯tℓ‖].\displaystyle d\_{W}^{J\_{1}}(\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n,k},\bar{\amsmathbb{Q}}\_{\tau,\zeta}^{\otimes k})\leq d\_{W}^{U}(\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n,k},\bar{\amsmathbb{Q}}\_{\tau,\zeta}^{\otimes k})\leq\sum\_{\ell=1}^{k}\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]. |  |

Thus it suffices to show

|  |  |  |
| --- | --- | --- |
|  | limn→∞∑ℓ=1kE​[supτ≤t≤T‖Xtℓ,n−X¯tℓ‖]=0\displaystyle\lim\_{n\rightarrow\infty}\sum\_{\ell=1}^{k}\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]=0 |  |

for our choice of coupling. In particular, based on an approach of [Graham1992-2], we will use the Poisson representation of Proposition [2.5](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") to create a coupling of the system ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) and of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) with the same jump times.

For this let (Nℓ)ℓ∈N(N^{\ell})\_{\ell\in\amsmathbb{N}} be independent homogeneous Poisson processes with intensity CλC\_{\lambda} and from this we construct the marked Poisson processes 𝒩ℓ,n\mathcal{N}^{\ell,n} and 𝒩¯ℓ\bar{\mathcal{N}}^{\ell} given by

|  |  |  |
| --- | --- | --- |
|  | 𝒩ℓ,n​(B):=∑i∈N𝟙B​(Tiℓ,Ziℓ,n)​ and ​𝒩¯ℓ​(B):=∑i∈N𝟙B​(Tiℓ,Z¯iℓ),ℓ=1,…,n,\displaystyle\mathcal{N}^{\ell,n}(B):=\sum\_{i\in\amsmathbb{N}}\mathds{1}\_{B}(T\_{i}^{\ell},Z\_{i}^{\ell,n})\text{ and }\bar{\mathcal{N}}^{\ell}(B):=\sum\_{i\in\amsmathbb{N}}\mathds{1}\_{B}(T\_{i}^{\ell},\bar{Z}\_{i}^{\ell}),\quad\ell=1,\ldots,n, |  |

for B∈ℬ​([τ,T])⊗ℬ​(E)B\in\mathcal{B}([\tau,T])\otimes\mathcal{B}(E), where the marks (Ziℓ,n)i∈N(Z^{\ell,n}\_{i})\_{i\in\amsmathbb{N}} and (Z¯iℓ)i∈N(\bar{Z}^{\ell}\_{i})\_{i\in\amsmathbb{N}} are determined using the kernel

|  |  |  |
| --- | --- | --- |
|  | κt​(x,ρ,d​y)=λt​(x,ρ)Cλ1​rt​(x,ρ,d​y)+(1−λt​(x,ρ)Cλ1)​δ{0}​(d​y).\displaystyle\kappa\_{t}(x,\rho,\mathrm{d}y)=\frac{\lambda\_{t}(x,\rho)}{C\_{\lambda}^{1}}r\_{t}(x,\rho,\mathrm{d}y)+\bigg(1-\frac{\lambda\_{t}(x,\rho)}{C\_{\lambda}^{1}}\bigg)\delta\_{\{0\}}(\mathrm{d}y). |  |

That is, given Tiℓ=tT\_{i}^{\ell}=t, Xt−ℓ,nX^{\ell,n}\_{t-} and X¯t−ℓ\bar{X}^{\ell}\_{t-} we determine Ziℓ,nZ^{\ell,n}\_{i} and Z¯iℓ\bar{Z}^{\ell}\_{i} according to the optimal coupling between κt​(Xt−ℓ,n,εt−n,d​z)\kappa\_{t}(X^{\ell,n}\_{t-},\varepsilon\_{t-}^{n},\mathrm{d}z) and κt​(X¯t−ℓ,η¯t,d​z)\kappa\_{t}(\bar{X}\_{t-}^{\ell},\bar{\eta}\_{t},\mathrm{d}z). This means we have that

|  |  |  |
| --- | --- | --- |
|  | E​[‖Ziℓ,n−Z¯iℓ‖|Tiℓ=t,Xt−ℓ,n,X¯t−ℓ]=dW​(κt​(Xt−ℓ,n,εt−n,d​z),κt​(X¯t−ℓ,η¯t,d​z)).\displaystyle\amsmathbb{E}\big[\|Z\_{i}^{\ell,n}-\bar{Z}\_{i}^{\ell}\|\big|T\_{i}^{\ell}=t,X\_{t-}^{\ell,n},\bar{X}\_{t-}^{\ell}\big]=d\_{W}(\kappa\_{t}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}z),\kappa\_{t}(\bar{X}\_{t-}^{\ell},\bar{\eta}\_{t},\mathrm{d}z)). |  |

The marked Poisson processes 𝒩ℓ,n\mathcal{N}^{\ell,n} then have compensating measure

|  |  |  |
| --- | --- | --- |
|  | L𝒩ℓ,n​(d​t,d​z)=Cλ​κt​(Xt−ℓ,n,εt−n,d​z)​d​t,\displaystyle L\_{\mathcal{N}}^{\ell,n}(\mathrm{d}t,\mathrm{d}z)=C\_{\lambda}\kappa\_{t}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}z)\mathrm{d}t, |  |

where εt−n=∑ℓ=1nδ{Xt−ℓ,n}\varepsilon\_{t-}^{n}=\sum\_{\ell=1}^{n}\delta\_{\{X\_{t-}^{\ell,n}\}}, while the 𝒩¯ℓ\bar{\mathcal{N}}^{\ell} have compensating measures

|  |  |  |
| --- | --- | --- |
|  | L𝒩¯ℓ​(d​t,d​z)=Cλ​κt​(X¯t−ℓ,η¯t,d​z)​d​t.\displaystyle L\_{\bar{\mathcal{N}}}^{\ell}(\mathrm{d}t,\mathrm{d}z)=C\_{\lambda}\kappa\_{t}(\bar{X}\_{t-}^{\ell},\bar{\eta}\_{t},\mathrm{d}z)\mathrm{d}t. |  |

Let (Yℓ,n)ℓ=1,…,n(Y^{\ell,n})\_{\ell=1,\ldots,n} be from distribution ζn\zeta^{n} and let (Y¯ℓ)ℓ∈N(\bar{Y}^{\ell})\_{\ell\in\amsmathbb{N}} be iid. from distribution ζ\zeta chosen jointly from the optimal coupling between ζn\zeta^{n} and ζ⊗n\zeta^{\otimes n}. Proposition [2.5](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") then yields that the system ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) can be represented as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtℓ,n\displaystyle X\_{t}^{\ell,n} | =Yℓ,n+∫(τ,t]×Az​𝒩ℓ,n​(d​s,d​z),ℓ=1,…,n,\displaystyle=Y^{\ell,n}+\int\_{(\tau,t]\times A}z\,\mathcal{N}^{\ell,n}(ds,dz),\quad\ell=1,\ldots,n, |  |

and that XTiℓℓ,n=XTiℓ−ℓ,n+Ziℓ,nX\_{T\_{i}^{\ell}}^{\ell,n}=X\_{T\_{i}^{\ell}-}^{\ell,n}+Z\_{i}^{\ell,n} and similarly Proposition [2.5](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") yields that the system

|  |  |  |  |
| --- | --- | --- | --- |
|  | X¯tℓ\displaystyle\bar{X}\_{t}^{\ell} | =Y¯ℓ+∫(τ,t]×Az​𝒩¯ℓ​(d​s,d​z),ℓ∈N\displaystyle=\bar{Y}^{\ell}+\int\_{(\tau,t]\times A}z\,\bar{\mathcal{N}}^{\ell}(ds,dz),\quad\ell\in\amsmathbb{N} |  |

are iid. copies of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), with X¯Tiℓℓ=X¯Tiℓ−ℓ+Z¯iℓ\bar{X}\_{T\_{i}^{\ell}}^{\ell}=\bar{X}\_{T\_{i}^{\ell}-}^{\ell}+\bar{Z}\_{i}^{\ell}.

As Xℓ,nX^{\ell,n} and X¯ℓ\bar{X}^{\ell} are identically distributed across ℓ\ell we have that

|  |  |  |
| --- | --- | --- |
|  | dWU​(Qτ,ζnk,n,Qτ,ζ⊗k)≤∑ℓ=1kE​[supτ≤t≤T‖Xtℓ,n−X¯tℓ‖]=k​E​[supτ≤t≤T‖Xt1,n−X¯t1‖].\displaystyle d\_{W}^{U}(\amsmathbb{Q}\_{\tau,\zeta^{n}}^{k,n},\amsmathbb{Q}\_{\tau,\zeta}^{\otimes k})\leq\sum\_{\ell=1}^{k}\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]=k\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{1,n}-\bar{X}\_{t}^{1}\|\bigg]. |  |

Since 𝒩1,n\mathcal{N}^{1,n} and 𝒩¯1\bar{\mathcal{N}}^{1} have the same jump times as N1N^{1} we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖Xt1,n−X¯t1‖]≤\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{1,n}-\bar{X}\_{t}^{1}\|\bigg]\leq | dW​(ζn,1,ζ)+E​[∑i=1NT1‖Zi1,n−Z¯i1‖].\displaystyle d\_{W}(\zeta^{n,1},\zeta)+\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}^{1}}\|Z^{1,n}\_{i}-\bar{Z}^{1}\_{i}\|\bigg]. |  |

Due to Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(2) and from the definition of κ\kappa we get

|  |  |  |
| --- | --- | --- |
|  | dK​R​(κtn​(x1,ρ1,d​z),κt​(x2,ρ2,d​z))≤CL​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle d\_{KR}(\kappa\_{t}^{n}(x\_{1},\rho\_{1},\mathrm{d}z),\kappa\_{t}(x\_{2},\rho\_{2},\mathrm{d}z))\leq C\_{L}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

for x1,x2∈Ex\_{1},x\_{2}\in E and ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(E), where CL=CμCλC\_{L}=\frac{C\_{\mu}}{C\_{\lambda}}.
Using this and the existence of an optimal coupling we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | E[∥Zi1,n−Z¯i1∥||NT1]\displaystyle\amsmathbb{E}[\|Z^{1,n}\_{i}-\bar{Z}^{1}\_{i}\|||N\_{T}^{1}] | =E​[E​[‖Zi1,n−Z¯i1‖|NT1,Ti1,X¯Ti1−1,n,X¯Ti1−1]|NT]\displaystyle=\amsmathbb{E}[\amsmathbb{E}[\|Z^{1,n}\_{i}-\bar{Z}^{1}\_{i}\||N\_{T}^{1},T\_{i}^{1},\bar{X}\_{T\_{i}^{1}-}^{1,n},\bar{X}\_{T\_{i}^{1}-}^{1}]|N\_{T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[dK​R​(κTi1​(XTi1−1,n,εTi1−n,d​z),κTi1​(X¯Ti1−1,η¯Ti1,d​z))|NT1]\displaystyle=\amsmathbb{E}[d\_{KR}(\kappa\_{T\_{i}^{1}}(X\_{T\_{i}^{1}-}^{1,n},\varepsilon\_{T\_{i}^{1}-}^{n},\mathrm{d}z),\kappa\_{T\_{i}^{1}}(\bar{X}\_{T\_{i}^{1}-}^{1},\bar{\eta}\_{T\_{i}^{1}},\mathrm{d}z))|N\_{T}^{1}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E​[CL​‖XTi1−1,n−X¯Ti1−1‖+CL​dW​(εTi1−n,η¯Ti1)|NT1].\displaystyle\leq\amsmathbb{E}[C\_{L}\|X\_{T\_{i}^{1}-}^{1,n}-\bar{X}\_{T\_{i}^{1}-}^{1}\|+C\_{L}d\_{W}(\varepsilon\_{T\_{i}^{1}-}^{n},\bar{\eta}\_{T\_{i}^{1}})|N\_{T}^{1}]. |  |

The second equality follows, since (Zi1,n,Z¯i1)(Z\_{i}^{1,n},\bar{Z}\_{i}^{1}) are independent of NT1N\_{T}^{1}, given
  
(Ti1,XTi1−1,n,X¯Ti1−1)(T\_{i}^{1},X\_{T\_{i}^{1}-}^{1,n},\bar{X}\_{T\_{i}^{1}-}^{1}).

Thus we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[∑i=1NT1‖Zi1,n−Z¯iℓ‖]\displaystyle\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}^{1}}\|Z^{1,n}\_{i}-\bar{Z}^{\ell}\_{i}\|\bigg] | ≤Cμ​∫τTE​[supτ≤s≤t‖Xs1,n−X¯s1‖]+E​[dW​(εt−n,η¯t)]​d​t.\displaystyle\leq C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{1,n}-\bar{X}\_{s}^{1}\|\bigg]+\amsmathbb{E}[d\_{W}(\varepsilon\_{t-}^{n},\bar{\eta}\_{t})]\mathrm{d}t. |  |

Furthermore by the triangle inequality we have

|  |  |  |
| --- | --- | --- |
|  | dW​(εt−n,ηt)≤dW​(εt−n,ε¯t−n)+dW​(ε¯t−n,ηt−),\displaystyle d\_{W}(\varepsilon\_{t-}^{n},\eta\_{t})\leq d\_{W}(\varepsilon\_{t-}^{n},\bar{\varepsilon}\_{t-}^{n})+d\_{W}(\bar{\varepsilon}\_{t-}^{n},\eta\_{t-}), |  |

where ε¯tn:=1n​∑ℓ=1nδ{X¯tℓ}\bar{\varepsilon}^{n}\_{t}:=\frac{1}{n}\sum\_{\ell=1}^{n}\delta\_{\{\bar{X}\_{t}^{\ell}\}}. Lemma [B.1](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance") allows us to apply Lemma [3.7](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem7 "Lemma 3.7. ‣ 3.1. Proof of Theorem 3.5 ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") to the second distance in order to obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[dW​(εt−n,ηt−)]\displaystyle\amsmathbb{E}[d\_{W}(\varepsilon\_{t-}^{n},\eta\_{t-})] | ≤E​[1n​∑ℓ=1n‖Xt−ℓ,n−X¯t−ℓ‖]+C​β​(n)\displaystyle\leq\amsmathbb{E}\bigg[\frac{1}{n}\sum\_{\ell=1}^{n}\|X\_{t-}^{\ell,n}-\bar{X}\_{t-}^{\ell}\|\bigg]+C\beta(n) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E​[supτ≤s≤t‖Xs1,n−X¯s1‖]+C​β​(n),\displaystyle\leq\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{1,n}-\bar{X}\_{s}^{1}\|\bigg]+C\beta(n), |  |

where the sum disappears due the fact that the individuals are identically distributed. Inserting this back in the main expression we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [supτ≤t≤T‖Xtℓ,n−X¯tℓ‖]≤dW​(ζn,1,ζ)\displaystyle\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]\leq d\_{W}(\zeta^{n,1},\zeta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫τT2​Cμ​E​[supτ≤s≤t‖Xsℓ,n−X¯sℓ‖]+Cμ​C​β​(n)​d​t.\displaystyle+\int\_{\tau}^{T}2C\_{\mu}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\bar{X}\_{s}^{\ell}\|\bigg]+C\_{\mu}C\beta(n)dt. |  |

Applying Grönwalls inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [supτ≤t≤T‖Xtℓ,n−X¯tℓ‖]≤e2​Cμ​(T−τ)​(dW​(ζn,1,ζ)+Cμ​C​β​(n)​(T−τ)).\displaystyle\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]\leq e^{2C\_{\mu}(T-\tau)}(d\_{W}(\zeta^{n,1},\zeta)+C\_{\mu}C\beta(n)(T-\tau)). |  |

As limn→∞dW​(ζn,1,ζ)=0\lim\_{n\rightarrow\infty}d\_{W}(\zeta^{n,1},\zeta)=0 taking the limit n→∞n\rightarrow\infty yields the desired result.

## 4. Mean-field approximation of the conditional distribution

For insurance applications it is of particular interest, whether a similar convergence result can be obtained for the conditional path-laws of Qτ,ζnn\amsmathbb{Q}^{n}\_{\tau,\zeta^{n}}, given the initial value. Recall that by Theorem [2.2](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance"), Qτ,ζn\amsmathbb{Q}^{n}\_{\tau,\zeta} can be written as

|  |  |  |
| --- | --- | --- |
|  | Qτ,ζnn​(d​ω)=∫EnQτ,𝐱nn​(d​ω)​ζn​(d​𝐱n),\displaystyle\amsmathbb{Q}^{n}\_{\tau,\zeta^{n}}(\mathrm{d}\omega)=\int\_{E^{n}}\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}}(\mathrm{d}\omega)\zeta^{n}(\mathrm{d}\mathbf{x}^{n}), |  |

where each of the Qτ,𝐱nn\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}} is the path-law of the system

|  |  |  |
| --- | --- | --- |
|  | Xtℓ,n=xℓ+∫(τ,t]×Az​Qℓ,n​(d​s,d​z),ℓ=1,…,n\displaystyle X\_{t}^{\ell,n}=x^{\ell}+\int\_{(\tau,t]\times A}z\,Q^{\ell,n}(ds,dz),\quad\ell=1,\ldots,n |  |

with compensating measure

|  |  |  |
| --- | --- | --- |
|  | Lℓ,n​(d​t,d​z)=μt​(Xt−ℓ,n,εt−n,d​z)​d​t.\displaystyle L^{\ell,n}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}z)\mathrm{d}t. |  |

Thus (Qτ,𝐱nn)𝐱n∈En(\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}})\_{\mathbf{x}^{n}\in E^{n}} is a regular version of the joint path-law of the nn individuals given that their initial values YnY^{n} are equal to 𝐱n∈En\mathbf{x}^{n}\in E^{n}.

Recall also that by Theorem [2.7](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance"), Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta} can be written as

|  |  |  |
| --- | --- | --- |
|  | Q¯τ,ζ​(d​ω)=∫EQ~τ,ζx​(d​ω)​ζ​(d​x),\displaystyle\bar{\amsmathbb{Q}}\_{\tau,\zeta}(\mathrm{d}\omega)=\int\_{E}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}(\mathrm{d}\omega)\zeta(\mathrm{d}x), |  |

where (Q~τ,ζx)x∈E(\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x})\_{x\in E} are path-laws of ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). Thus (Q~τ,ζx)x∈E(\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x})\_{x\in E} is a regular conditional distribution of Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta} given that the initial value is xx. The question in which we are now interested in, is whether Qτ,𝐱nn\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}} can be approximated by ⨂ℓ=1nQ~τ,ζxℓn\bigotimes\_{\ell=1}^{n}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x^{n}\_{\ell}}.

Let ε𝐱n:=1n​∑ℓ=1nδ{xℓn}\varepsilon\_{\mathbf{x}^{n}}:=\frac{1}{n}\sum\_{\ell=1}^{n}\delta\_{\{x\_{\ell}^{n}\}}. According to Theorem 4.2 of [Gottlieb1998] it holds that if ε𝐱nn→ζ\varepsilon^{n}\_{\mathbf{x}^{n}}\rightarrow\zeta in 𝒫1​(E)\mathcal{P}^{1}(E), then the sequence of symmetrisations (Q^τ,𝐱n)n∈N(\widehat{\amsmathbb{Q}}\_{\tau,\mathbf{x}^{n}})\_{n\in\amsmathbb{N}} is Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta}-chaotic. The symmetrisation Q^τ,𝐱n\widehat{\amsmathbb{Q}}\_{\tau,\mathbf{x}^{n}} is defined as

|  |  |  |
| --- | --- | --- |
|  | Q^τ,𝐱n​(B):=1n!​∑σ∈ΠnQ^τ,𝐱n​(σ​(B)),B∈ℬ​(D​([τ,T],E)n),\displaystyle\widehat{\amsmathbb{Q}}\_{\tau,\mathbf{x}^{n}}(B):=\frac{1}{n!}\sum\_{\sigma\in\Pi\_{n}}\widehat{\amsmathbb{Q}}\_{\tau,\mathbf{x}^{n}}(\sigma(B)),\quad B\in\mathcal{B}(\amsmathbb{D}([\tau,T],E)^{n}), |  |

where Πn\Pi\_{n} is the set of all permutations σ\sigma of the set {1,…,n}\{1,\ldots,n\} and σ​(B):={σ​(x)|x∈B}\sigma(B):=\{\sigma(x)|x\in B\}. Thus it is not possible to relate Qτ,𝐱nn\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}} to Q~τ,ζx\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x} directly and, due to the symmetrisation, Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta} can be interpreted as the distribution of a typical individual and not of a specific individual. From Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") it is therefore not clear, whether Qτ,𝐱nn\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}} can actually be approximated by ⨂ℓ=1nQ~τ,ζxℓn\bigotimes\_{\ell=1}^{n}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x^{n}\_{\ell}}.

Nevertheless this can be shown by using a natural extension of the arguments behind Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"). As before, we assume that (ζn)n∈N(\zeta^{n})\_{n\in\amsmathbb{N}} is ζ\zeta-chaotic. Then we fix m∈Nm\in\amsmathbb{N} and 𝐱m=(xℓm)ℓ=1,…,m∈Em\mathbf{x}^{m}=(x\_{\ell}^{m})\_{\ell=1,\ldots,m}\in E^{m} and assume:

###### Assumption 4.

There exists a q>1q>1 such that:

1. (1)

   There exists a regular conditional probability distribution (ζn​(𝐱m))𝐱m∈Em⊂𝒫q​(En−m)(\zeta^{n}(\mathbf{x}^{m}))\_{\mathbf{x}^{m}\in E^{m}}\subset\mathcal{P}^{q}(E^{n-m}) of

   |  |  |  |
   | --- | --- | --- |
   |  | P((Ym+1,n,…,Yn,n)∈⋅|(Y1,n,…,Ym,n)=𝐱m).\displaystyle\amsmathbb{P}((Y^{m+1,n},\ldots,Y^{n,n})\in\cdot|(Y^{1,n},\ldots,Y^{m,n})=\mathbf{x}^{m}). |  |
2. (2)

   It holds that (ζn​(𝐱m))n∈N(\zeta^{n}(\mathbf{x}^{m}))\_{n\in\amsmathbb{N}} is ζ\zeta-chaotic in the Wasserstein sense for any 𝐱m∈Em\mathbf{x}^{m}\in E^{m}.

###### Remark 4.1.

Note that in the case of EE being countable, (ζn​(𝐱m))n∈N(\zeta^{n}(\mathbf{x}^{m}))\_{n\in\amsmathbb{N}} being ζ\zeta-chaotic is implied by the fact that the unconditional (ζn)n∈N(\zeta^{n})\_{n\in\amsmathbb{N}} is ζ\zeta-chaotic. This is therefore only a more restrictive assumption in the case that EE is not countable.

It now follows that ρn​(𝐱m)\rho^{n}(\mathbf{x}^{m}) given by ρn​(𝐱m):=δ{𝐱𝐦}⊗ζn​(𝐱m)\rho^{n}(\mathbf{x}^{m}):=\delta\_{\{\mathbf{x^{m}}\}}\otimes\zeta^{n}(\mathbf{x}^{m}) is a regular conditional probability of

|  |  |  |
| --- | --- | --- |
|  | P((Y1,n,…,Yn,n)∈⋅|(Y1,n,…,Ym,n)=𝐱m).\displaystyle\amsmathbb{P}((Y^{1,n},\ldots,Y^{n,n})\in\cdot|(Y^{1,n},\ldots,Y^{m,n})=\mathbf{x}^{m}). |  |

Using ρn​(𝐱m)\rho^{n}(\mathbf{x}^{m}) as initial distribution, we can define the system of SDEs given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.1) |  | Xtℓ,n=xℓm+∫(τ,t]×Az​Qℓ,n​(d​s,d​z),ℓ=1,…,mXtℓ,n=Yℓ,n+∫(τ,t]×Az​Qℓ,n​(d​s,d​z),ℓ=m+1,…,n.\displaystyle\begin{split}X\_{t}^{\ell,n}&=x^{m}\_{\ell}+\int\_{(\tau,t]\times A}z\,Q^{\ell,n}(ds,dz),\quad\ell=1,\ldots,m\\ X\_{t}^{\ell,n}&=Y^{\ell,n}+\int\_{(\tau,t]\times A}z\,Q^{\ell,n}(ds,dz),\quad\ell=m+1,\ldots,n.\end{split} | |  |

where the random counting measures Qℓ,nQ^{\ell,n} have compensating measures

|  |  |  |
| --- | --- | --- |
|  | Lℓ,n​(d​t,d​z)=μt​(Xt−ℓ,n,εt−n,d​z)​d​t,ℓ=1,…,n.\displaystyle L^{\ell,n}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}z)\mathrm{d}t,\quad\ell=1,\ldots,n. |  |

The difference to ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) is now that the first mm individuals have known and deterministic starting values 𝐱m∈Em\mathbf{x}^{m}\in E^{m}, while the rest have random starting values (Yℓ,n)ℓ=m+1,…,n(Y^{\ell,n})\_{\ell=m+1,\ldots,n} from distribution ζn​(𝐱m)\zeta^{n}(\mathbf{x}^{m}).

The path-law of ([4.1](https://arxiv.org/html/2511.04198v1#S4.E1 "In 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance")) denoted by Qτ,ρn​(𝐱m)n\amsmathbb{Q}^{n}\_{\tau,\rho^{n}(\mathbf{x}^{m})} now has the following relationship to the path-law Qτ,ζn\amsmathbb{Q}^{n}\_{\tau,\zeta} of ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")):

###### Proposition 4.2.

The family (Qτ,ρn​(𝐱m)n)𝐱m∈Em(\amsmathbb{Q}\_{\tau,\rho^{n}(\mathbf{x}^{m})}^{n})\_{\mathbf{x}^{m}\in E^{m}} constitutes a regular conditional distribution of Qτ,ζn\amsmathbb{Q}^{n}\_{\tau,\zeta} given (Y1,n,…,Ym,n)=𝐱m(Y^{1,n},\ldots,Y^{m,n})=\mathbf{x}^{m}. Thus it holds that

|  |  |  |
| --- | --- | --- |
|  | Qτ,ζn​(d​ω)=∫EmQτ,ρn​(𝐱m)n​(d​ω)​ζn,m​(d​𝐱m).\displaystyle\amsmathbb{Q}^{n}\_{\tau,\zeta}(\mathrm{d}\omega)=\int\_{E^{m}}\amsmathbb{Q}\_{\tau,\rho^{n}(\mathbf{x}^{m})}^{n}(\mathrm{d}\omega)\zeta^{n,m}(\mathrm{d}\mathbf{x}^{m}). |  |

###### Proof.

By Theorem [2.2](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance"), we have that

|  |  |  |
| --- | --- | --- |
|  | Qτ,ρn​(xm)n​(d​ω)=∫EnQτ,𝐱nn​(d​ω)​ρn​(xm)​(d​xn).\displaystyle\amsmathbb{Q}\_{\tau,\rho^{n}(x^{m})}^{n}(\mathrm{d}\omega)=\int\_{E^{n}}\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}}(\mathrm{d}\omega)\rho^{n}(\mathrm{x}^{m})(\mathrm{d}x^{n}). |  |

As ρn​(𝐱m)\rho^{n}(\mathbf{x}^{m}) is a regular conditional probability of

|  |  |  |
| --- | --- | --- |
|  | P((Y1,n,…,Yn,n)∈⋅|(Y1,n,…,Ym,n)=𝐱m).\displaystyle\amsmathbb{P}((Y^{1,n},\ldots,Y^{n,n})\in\cdot|(Y^{1,n},\ldots,Y^{m,n})=\mathbf{x}^{m}). |  |

it holds that

|  |  |  |
| --- | --- | --- |
|  | ζn​(d​𝐱n)=∫Emρn​(𝐱m)​ζn,m​(d​𝐱m),\displaystyle\zeta^{n}(\mathrm{d}\mathbf{x}^{n})=\int\_{E^{m}}\rho^{n}(\mathbf{x}^{m})\zeta^{n,m}(\mathrm{d}\mathbf{x}^{m}), |  |

where ζn,m\zeta^{n,m} is the marginal distribution of (Y1,n,…,Ym,n)(Y^{1,n},\ldots,Y^{m,n}). Combining these two equations, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫EmQτ,ρn​(xm)n​(d​ω)​ζn,m​(d​𝐱m)\displaystyle\int\_{E^{m}}\amsmathbb{Q}\_{\tau,\rho^{n}(x^{m})}^{n}(\mathrm{d}\omega)\zeta^{n,m}(\mathrm{d}\mathbf{x}^{m}) | =∫Em∫EnQτ,𝐱nn​(d​ω)​ρn​(xm)​(d​xn)​ζn,m​(d​𝐱m)\displaystyle=\int\_{E^{m}}\int\_{E^{n}}\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}}(\mathrm{d}\omega)\rho^{n}(\mathrm{x}^{m})(\mathrm{d}x^{n})\zeta^{n,m}(\mathrm{d}\mathbf{x}^{m}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫EnQτ,𝐱nn​(d​ω)​∫Emρn​(xm)​(d​xn)​ζn,m​(d​𝐱m)\displaystyle=\int\_{E^{n}}\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}}(\mathrm{d}\omega)\int\_{E^{m}}\rho^{n}(\mathrm{x}^{m})(\mathrm{d}x^{n})\zeta^{n,m}(\mathrm{d}\mathbf{x}^{m}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫EnQτ,𝐱nn​(d​ω)​ζn​(d​𝐱n)=Qτ,ζnn​(d​ω).\displaystyle=\int\_{E^{n}}\amsmathbb{Q}^{n}\_{\tau,\mathbf{x}^{n}}(\mathrm{d}\omega)\zeta^{n}(\mathrm{d}\mathbf{x}^{n})=\amsmathbb{Q}\_{\tau,\zeta^{n}}^{n}(\mathrm{d}\omega). |  |

∎

We can now show, that the joint path-law of the first mm individuals in the system ([4.1](https://arxiv.org/html/2511.04198v1#S4.E1 "In 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance")), denoted by Qτ,ρn​(𝐱m)n,m\amsmathbb{Q}^{n,m}\_{\tau,\rho^{n}(\mathbf{x}^{m})} converges to ⨂ℓ=1mQ~τ,ζxℓm\bigotimes\_{\ell=1}^{m}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x\_{\ell}^{m}}. This means that the mm indivuals with known initial values embedded into a large cohort of individuals with random starting values, which have a chaotic distribution, become asymptotically independent, with Q~τ,ζxℓm\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x^{m}\_{\ell}} as their marginal limiting path-law, even though they also depend on the individuals m<ℓ≤nm<\ell\leq n. Furthermore we have for any fixed k∈Nk\in\amsmathbb{N} that the joint path-law of the individuals ℓ=m+1,…,m+k\ell=m+1,\ldots,m+k of ([4.1](https://arxiv.org/html/2511.04198v1#S4.E1 "In 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance")), denoted by Qτ,ρn​(𝐱k)n,m:k\amsmathbb{Q}\_{\tau,\rho^{n}(\mathbf{x}^{k})}^{n,m:k} converges to Q¯τ,ζ⊗k\bar{\amsmathbb{Q}}\_{\tau,\zeta}^{\otimes k}, even though they also depend on the individuals 1≤ℓ≤m1\leq\ell\leq m. The intuition is, that changing the initial distribution of a finite number of individuals has no effect on the empirical distribution of the collective, when the total number of individuals tends to infinity.

###### Theorem 4.3.

Assume that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance"), [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") and [4](https://arxiv.org/html/2511.04198v1#Thmassumption4 "Assumption 4. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") are satisfied for some q>1q>1. Then for any fixed m∈Nm\in\amsmathbb{N} it holds that

|  |  |  |
| --- | --- | --- |
|  | limn→∞dWJ1​(Qτ,ρn​(𝐱m)n,m,⨂ℓ=1mQ~τ,ζxℓm)=0.\displaystyle\lim\_{n\rightarrow\infty}d\_{W}^{J\_{1}}\bigg(\amsmathbb{Q}^{n,m}\_{\tau,\rho^{n}(\mathbf{x}^{m})},\bigotimes\_{\ell=1}^{m}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x^{m}\_{\ell}}\bigg)=0. |  |

Addionally it holds for any fixed k∈Nk\in\amsmathbb{N}, that

|  |  |  |
| --- | --- | --- |
|  | limn→∞dWJ1​(Qτ,ρn​(𝐱m)n,m:k,Q¯τ,ζ⊗k)=0,∀k∈N.\displaystyle\lim\_{n\rightarrow\infty}d\_{W}^{J\_{1}}\bigg(\amsmathbb{Q}^{n,m:k}\_{\tau,\rho^{n}(\mathbf{x}^{m})},\bar{\amsmathbb{Q}}\_{\tau,\zeta}^{\otimes k}\bigg)=0,\quad\forall\,k\in\amsmathbb{N}. |  |

###### Remark 4.4.

By Propositions [2.13](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem13 "Proposition 2.13. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [2.14](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem14 "Proposition 2.14. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") we know that the jump destination specification with Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") is equivalent to ([3.1](https://arxiv.org/html/2511.04198v1#S3.E1 "In 3. Mean-field approximation ‣ Mean-field approximations in insurance")) with Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance"). Thus Theorem [4.3](https://arxiv.org/html/2511.04198v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") is still valid for the jump destination representation.

### 4.1. Proof of Theorem [4.3](https://arxiv.org/html/2511.04198v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance")

The technique behind the proof is again to use a pathwise representation based on marked Poisson processes as in the proof of Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"). Using the same independent homogeneous Poisson processes (Nℓ)ℓ∈N(N^{\ell})\_{\ell\in\amsmathbb{N}}, we will now construct three families of marked Poisson processes: 𝒩ℓ,n\mathcal{N}^{\ell,n}, 𝒩¯ℓ\bar{\mathcal{N}}^{\ell} and 𝒩~ℓ\widetilde{\mathcal{N}}^{\ell}, where the marks are chosen the same way using the kernel κt​(x,ρ,d​y)\kappa\_{t}(x,\rho,\mathrm{d}y) and the optimal coupling. The compensating measures are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L𝒩ℓ,n​(d​t,d​z)\displaystyle L\_{\mathcal{N}}^{\ell,n}(\mathrm{d}t,\mathrm{d}z) | =Cλ​κt​(Xt−ℓ,n,εt−n,d​z)​d​t\displaystyle=C\_{\lambda}\kappa\_{t}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}z)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | L𝒩¯ℓ​(d​t,d​y)\displaystyle L\_{\bar{\mathcal{N}}}^{\ell}(\mathrm{d}t,\mathrm{d}y) | =Cλ​κt​(X¯t−ℓ,η¯t,d​z)​d​t\displaystyle=C\_{\lambda}\kappa\_{t}(\bar{X}\_{t-}^{\ell},\bar{\eta}\_{t},\mathrm{d}z)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | L𝒩~ℓ​(d​t,d​y)\displaystyle L\_{\widetilde{\mathcal{N}}}^{\ell}(\mathrm{d}t,\mathrm{d}y) | =Cλ​κt​(X~t−ℓ,η¯t,d​z)​d​t.\displaystyle=C\_{\lambda}\kappa\_{t}(\widetilde{X}\_{t-}^{\ell},\bar{\eta}\_{t},\mathrm{d}z)\mathrm{d}t. |  |

Let (Yℓ,n)ℓ=1,…,n(Y^{\ell,n})\_{\ell=1,\ldots,n} be from distribution ρn​(𝐱m)\rho^{n}(\mathbf{x}^{m}). Proposition [2.5](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") then yields that the system ([4.1](https://arxiv.org/html/2511.04198v1#S4.E1 "In 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtℓ,n\displaystyle X\_{t}^{\ell,n} | =xℓm+∫(τ,t]×Az​𝒩ℓ,n​(d​s,d​z),ℓ=1,…,m,\displaystyle=x\_{\ell}^{m}+\int\_{(\tau,t]\times A}z\,\mathcal{N}^{\ell,n}(\mathrm{d}s,\mathrm{d}z),\quad\ell=1,\ldots,m, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtℓ,n\displaystyle X\_{t}^{\ell,n} | =Yℓ,n+∫(τ,t]×Az​𝒩ℓ,n​(d​s,d​z),ℓ=m+1,…,n.\displaystyle=Y^{\ell,n}+\int\_{(\tau,t]\times A}z\,\mathcal{N}^{\ell,n}(\mathrm{d}s,\mathrm{d}z),\quad\ell=m+1,\ldots,n. |  |

Thus relative to the proof of Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"), we have only changed the initial distribution of the system. The representation of (X¯tℓ)ℓ∈N(\bar{X}\_{t}^{\ell})\_{\ell\in\amsmathbb{N}} is completely unchanged from the proof of Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"). In addition, we now construct the system (X~ℓ)ℓ=1,…,m(\widetilde{X}^{\ell})\_{\ell=1,\ldots,m} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | X~tℓ\displaystyle\widetilde{X}\_{t}^{\ell} | =xℓm+∫(τ,t]×Az​𝒩~ℓ​(d​s,d​z),ℓ=1,…,m.\displaystyle=x\_{\ell}^{m}+\int\_{(\tau,t]\times A}z\,\widetilde{\mathcal{N}}^{\ell}(\mathrm{d}s,\mathrm{d}z),\quad\ell=1,\ldots,m. |  |

Proposition [2.5](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") yields that these are mm independent solutions of ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) with initial value xℓmx\_{\ell}^{m} and with X~Tiℓℓ=X~Tiℓ−ℓ+Z~iℓ\widetilde{X}\_{T\_{i}^{\ell}}^{\ell}=\widetilde{X}\_{T\_{i}^{\ell}-}^{\ell}+\widetilde{Z}\_{i}^{\ell}.

Note that for each ℓ∈{1,…,n}\ell\in\{1,\ldots,n\} and n∈Nn\in\amsmathbb{N} we have that 𝒩ℓ,n\mathcal{N}^{\ell,n}, 𝒩~ℓ\widetilde{\mathcal{N}}^{\ell} and 𝒩¯ℓ\bar{\mathcal{N}}^{\ell} have the same jump times, as both are constructed based on the same Poisson process NℓN^{\ell}. This way we have constructed a coupling between the measures Qτ,ρn​(𝐱m)n,m\amsmathbb{Q}^{n,m}\_{\tau,\rho^{n}(\mathbf{x}^{m})} and ⨂ℓ=1mQ~τ,ζxℓm\bigotimes\_{\ell=1}^{m}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x\_{\ell}^{m}} and between the measures Qτ,ρn​(𝐱m)n,m:k\amsmathbb{Q}^{n,m:k}\_{\tau,\rho^{n}(\mathbf{x}^{m})} and Q¯τ,ζ⊗k\bar{\amsmathbb{Q}}^{\otimes k}\_{\tau,\zeta}.

We start with the following lemma:

###### Lemma 4.5.

It holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [supτ≤t≤T‖X~tℓ−X¯tℓ‖]≤eCμ​(T−τ)​dW​(δ{xℓ},ζ).\displaystyle\bigg[\sup\_{\tau\leq t\leq T}\|\widetilde{X}\_{t}^{\ell}-\bar{X}\_{t}^{\ell}\|\bigg]\leq e^{C\_{\mu}(T-\tau)}d\_{W}(\delta\_{\{x^{\ell}\}},\zeta). |  |

###### Proof.

Similar to previous arguments we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖X~tℓ−X¯tℓ‖]≤\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|\widetilde{X}\_{t}^{\ell}-\bar{X}\_{t}^{\ell}\|\bigg]\leq | E​[‖xℓm−Y¯ℓ‖]+E​[∑i=1NTℓ‖Ziℓ,n−Z¯iℓ‖].\displaystyle\amsmathbb{E}[\|x\_{\ell}^{m}-\bar{Y}^{\ell}\|]+\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}^{\ell}}\|Z^{\ell,n}\_{i}-\bar{Z}^{\ell}\_{i}\|\bigg]. |  |

Using the Lipschitz property of κ\kappa and the optimal coupling construction, an argument similar the one used in the proof of Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[∑i=1NTℓ‖Z~iℓ−Z¯iℓ‖]\displaystyle\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}^{\ell}}\|\widetilde{Z}\_{i}^{\ell}-\bar{Z}^{\ell}\_{i}\|\bigg] | ≤Cμ​∫τTE​[supτ≤s≤t‖X~sℓ−X¯sℓ‖]+E​[dW​(η¯t,η¯t)]​d​t\displaystyle\leq C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|\widetilde{X}\_{s}^{\ell}-\bar{X}\_{s}^{\ell}\|\bigg]+\amsmathbb{E}[d\_{W}(\bar{\eta}\_{t},\bar{\eta}\_{t})]\mathrm{d}t |  |

As dW​(η¯t,η¯t)=0d\_{W}(\bar{\eta}\_{t},\bar{\eta}\_{t})=0 and dW​(δ{xℓ},ζ)=E​[‖xℓ−Y¯ℓ‖]d\_{W}(\delta\_{\{x^{\ell}\}},\zeta)=\amsmathbb{E}[\|x^{\ell}-\bar{Y}^{\ell}\|] we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [supτ≤t≤T‖X~tℓ−X¯tℓ‖]≤dW​(δ{xℓ},ζ)+Cμ​∫τTE​[supτ≤s≤t‖X~sℓ−X¯sℓ‖]​𝑑t.\displaystyle\bigg[\sup\_{\tau\leq t\leq T}\|\widetilde{X}\_{t}^{\ell}-\bar{X}\_{t}^{\ell}\|\bigg]\leq d\_{W}(\delta\_{\{x^{\ell}\}},\zeta)+C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|\widetilde{X}\_{s}^{\ell}-\bar{X}\_{s}^{\ell}\|\bigg]dt. |  |

An application of Grönwalls inequality finishes the proof.
∎

By similar arguments as in the proof of Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖Xtℓ,n−X~tℓ‖]≤\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\widetilde{X}\_{t}^{\ell}\|\bigg]\leq | Cμ​∫τTE​[supτ≤s≤t‖Xsℓ,n−X~sℓ‖]​dt\displaystyle C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\widetilde{X}\_{s}^{\ell}\|\bigg]\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Cμ​∫τTE​[dW​(εt−n,η¯t)]​dt.\displaystyle+C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}[d\_{W}(\varepsilon\_{t-}^{n},\bar{\eta}\_{t})]\mathrm{d}t. |  |

for ℓ=1,…,m\ell=1,\ldots,m and

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖Xtℓ,n−X¯tℓ‖]≤\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]\leq | Cμ​∫τTE​[supτ≤s≤t‖Xsℓ,n−X¯sℓ‖]​dt\displaystyle C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\bar{X}\_{s}^{\ell}\|\bigg]\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Cμ​∫τTE​[dW​(εt−n,η¯t)]​dt+dW​(ζn,1​(𝐱m),ζ)\displaystyle+C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}[d\_{W}(\varepsilon\_{t-}^{n},\bar{\eta}\_{t})]\mathrm{d}t+d\_{W}(\zeta^{n,1}(\mathbf{x}^{m}),\zeta) |  |

for ℓ=m+1,…,n\ell=m+1,\ldots,n. We then get

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [∑ℓ=1msupτ≤t≤T‖Xtℓ,n−X~tℓ‖]\displaystyle\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\widetilde{X}\_{t}^{\ell}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫τTCμ​E​[∑ℓ=1msupτ≤s≤t‖Xsℓ,n−X~sℓ‖]​𝑑t+m​∫τTCμ​E​[dW​(εt−n,ηt)]​𝑑t.\displaystyle\leq\int\_{\tau}^{T}C\_{\mu}\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\widetilde{X}\_{s}^{\ell}\|\bigg]dt+m\int\_{\tau}^{T}C\_{\mu}\amsmathbb{E}[d\_{W}(\varepsilon\_{t-}^{n},\eta\_{t})]dt. |  |

Now set

|  |  |  |
| --- | --- | --- |
|  | ε~tn:=1n​(∑ℓ=1mδX~tℓ+∑ℓ=m+1nδX¯tℓ).\displaystyle\widetilde{\varepsilon}\_{t}^{n}:=\frac{1}{n}\bigg(\sum\_{\ell=1}^{m}\delta\_{\widetilde{X}\_{t}^{\ell}}+\sum\_{\ell=m+1}^{n}\delta\_{\bar{X}\_{t}^{\ell}}\bigg). |  |

Then by the triangle inequality, we have that

|  |  |  |
| --- | --- | --- |
|  | dW​(εt−n,ηt−)≤dW​(εt−n,ε~t−n)+dW​(ε~t−n,ε¯t−n)+dW​(ε¯t−n,η¯t),\displaystyle d\_{W}(\varepsilon\_{t-}^{n},\eta\_{t-})\leq d\_{W}(\varepsilon\_{t-}^{n},\widetilde{\varepsilon}\_{t-}^{n})+d\_{W}(\widetilde{\varepsilon}\_{t-}^{n},\bar{\varepsilon}\_{t-}^{n})+d\_{W}(\bar{\varepsilon}\_{t-}^{n},\bar{\eta}\_{t}), |  |

for which we can obtain the bounds

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[dW​(εt−n,ε~t−n)]\displaystyle\amsmathbb{E}[d\_{W}(\varepsilon\_{t-}^{n},\widetilde{\varepsilon}\_{t-}^{n})] | ≤1n​E​[∑ℓ=1msupτ≤s≤t‖Xsℓ,n−X~sℓ‖]+1n​E​[∑ℓ=m+1nsupτ≤s≤t‖Xsℓ,n−X¯sℓ‖]\displaystyle\leq\frac{1}{n}\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\widetilde{X}\_{s}^{\ell}\|\bigg]+\frac{1}{n}\amsmathbb{E}\bigg[\sum\_{\ell=m+1}^{n}\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\bar{X}\_{s}^{\ell}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[dW​(ε~t−n,ε¯t−n)]\displaystyle\amsmathbb{E}[d\_{W}(\widetilde{\varepsilon}\_{t-}^{n},\bar{\varepsilon}\_{t-}^{n})] | ≤1n​∑ℓ=1mE​[supτ≤s≤t‖X~sℓ−X¯sℓ‖]≤1n​eCμ​(T−τ)​∑i=lmdW​(δ{xℓ},ζ),\displaystyle\leq\frac{1}{n}\sum\_{\ell=1}^{m}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|\widetilde{X}\_{s}^{\ell}-\bar{X}\_{s}^{\ell}\|\bigg]\leq\frac{1}{n}e^{C\_{\mu}(T-\tau)}\sum\_{i=l}^{m}d\_{W}(\delta\_{\{x^{\ell}\}},\zeta), |  |

where Lemma [4.5](https://arxiv.org/html/2511.04198v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1. Proof of Theorem 4.3 ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") implies the last inequality in the second line. By Lemma [B.1](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance") we may still apply Lemma [3.7](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem7 "Lemma 3.7. ‣ 3.1. Proof of Theorem 3.5 ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"), to obtain the bound E​[dW​(ε¯t−n,η¯t)]≤C​β​(n)\amsmathbb{E}[d\_{W}(\bar{\varepsilon}\_{t-}^{n},\bar{\eta}\_{t})]\leq C\beta(n). Setting K:=eCμ​(T−τ)​∑ℓ=1mdW​(δ{xℓ},ζ)K:=e^{C\_{\mu}(T-\tau)}\sum\_{\ell=1}^{m}d\_{W}(\delta\_{\{x^{\ell}\}},\zeta) and Δ:=T−τ\Delta:=T-\tau, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[∑ℓ=1msupτ≤t≤T‖Xtℓ,n−X~tℓ‖]≤\displaystyle\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\widetilde{X}\_{t}^{\ell}\|\bigg]\leq | ∫τTCμ​(1+mn)​E​[∑ℓ=1msupτ≤s≤t‖Xsℓ,n−X~sℓ‖]​𝑑t\displaystyle\int\_{\tau}^{T}C\_{\mu}\bigg(1+\frac{m}{n}\bigg)\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\widetilde{X}\_{s}^{\ell}\|\bigg]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫τTCμ​mn​E​[∑ℓ=m+1nsupτ≤s≤t‖Xsℓ,n−X¯sℓ‖]​𝑑t\displaystyle+\int\_{\tau}^{T}C\_{\mu}\frac{m}{n}\amsmathbb{E}\bigg[\sum\_{\ell=m+1}^{n}\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\bar{X}\_{s}^{\ell}\|\bigg]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Cμ​Δ​mn​(K+C​β​(n)​n).\displaystyle+C\_{\mu}\Delta\frac{m}{n}(K+C\beta(n)n). |  |

The goal is now to apply Grönwalls inequality, but before we do that, we have to find a bound for the expectation in the second line of the above equation. By repeating the above arguments, we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | E[∑ℓ=m+1n\displaystyle\amsmathbb{E}\bigg[\sum\_{\ell=m+1}^{n} | supτ≤t≤T∥Xtℓ,n−X¯tℓ∥]≤(n−m)dW(ζn,1(𝐱m),ζ)\displaystyle\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]\leq(n-m)d\_{W}(\zeta^{n,1}(\mathbf{x}^{m}),\zeta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫τTCμ​(1+n−mn)​E​[∑ℓ=m+1nsupτ≤s≤t‖Xsℓ,n−X¯sℓ‖]​𝑑t\displaystyle+\int\_{\tau}^{T}C\_{\mu}\bigg(1+\frac{n-m}{n}\bigg)\amsmathbb{E}\bigg[\sum\_{\ell=m+1}^{n}\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\bar{X}\_{s}^{\ell}\|\bigg]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Cμ​Δ​(n−m)​(1n​E​[∑ℓ=1msupτ≤t≤T‖Xtℓ,n−X~tℓ‖]+Kn+C​β​(n)).\displaystyle+C\_{\mu}\Delta(n-m)\bigg(\frac{1}{n}\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\widetilde{X}\_{t}^{\ell}\|\bigg]+\frac{K}{n}+C\beta(n)\bigg). |  |

Set α​(n):=dW​(ζn,1​(𝐱m),ζ)\alpha(n):=d\_{W}(\zeta^{n,1}(\mathbf{x}^{m}),\zeta). Applying Grönwalls inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [∑ℓ=m+1nsup0≤t≤T‖Xtℓ,n−X¯tℓ‖]\displaystyle\bigg[\sum\_{\ell=m+1}^{n}\sup\_{0\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​(Δ,n,m)​(n​α​(n)+Cμ​Δ​(E​[∑ℓ=1msupτ≤t≤T‖Xtℓ,n−X~ti‖]+K+C​n​β​(n))),\displaystyle\leq C\_{1}(\Delta,n,m)\Bigg(n\alpha(n)+C\_{\mu}\Delta\bigg(\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\widetilde{X}\_{t}^{i}\|\bigg]+K+Cn\beta(n)\bigg)\Bigg), |  |

where C1​(Δ,n,m):=eCμ​Δ​(1+n−mn)​(1−mn)C\_{1}(\Delta,n,m):=e^{C\_{\mu}\Delta(1+\frac{n-m}{n})}(1-\frac{m}{n}). Inserting this in the inequality further above yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E[∑ℓ=1msupτ≤t≤T\displaystyle\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq t\leq T} | ∥Xtℓ,n−X~tℓ∥]\displaystyle\|X\_{t}^{\ell,n}-\widetilde{X}\_{t}^{\ell}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | Cμ​Δ​m​(C1​(Δ,n,m)​α​(n)+C2​(Δ,n,m)​(Kn+C​β​(n)))\displaystyle C\_{\mu}\Delta m\bigg(C\_{1}(\Delta,n,m)\alpha(n)+C\_{2}(\Delta,n,m)\bigg(\frac{K}{n}+C\beta(n)\bigg)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫τTCμ​(1+mn​C2​(Δ,n,m))​E​[∑ℓ=1msupτ≤s≤t‖Xsℓ,n−X~sℓ‖]​𝑑t\displaystyle+\int\_{\tau}^{T}C\_{\mu}\bigg(1+\frac{m}{n}C\_{2}(\Delta,n,m)\bigg)\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq s\leq t}\|X\_{s}^{\ell,n}-\widetilde{X}\_{s}^{\ell}\|\bigg]dt |  |

with C2​(Δ,n,m):=1+Cμ​Δ​C1​(Δ,n,m)C\_{2}(\Delta,n,m):=1+C\_{\mu}\Delta C\_{1}(\Delta,n,m). Now a final application of Grönwalls inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [∑ℓ=1msupτ≤t≤T‖Xtl,m−X~tℓ‖]\displaystyle\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq t\leq T}\|X\_{t}^{l,m}-\widetilde{X}\_{t}^{\ell}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤eCμ​Δ​(1+mn​C2​(Δ,n,m))​Cμ​Δ​m​(C1​(Δ,m,n)​α​(n)+C2​(Δ,n,m)​(Kn+C​β​(n))).\displaystyle\leq e^{C\_{\mu}\Delta(1+\frac{m}{n}C\_{2}(\Delta,n,m))}C\_{\mu}\Delta m\Bigg(C\_{1}(\Delta,m,n)\alpha(n)+C\_{2}(\Delta,n,m)\bigg(\frac{K}{n}+C\beta(n)\bigg)\Bigg). |  |

As limn→∞dW​(ζn,1​(𝐱m),ζ)=0\lim\_{n\rightarrow\infty}d\_{W}(\zeta^{n,1}(\mathbf{x}^{m}),\zeta)=0 taking the limit n→∞n\rightarrow\infty yields

|  |  |  |
| --- | --- | --- |
|  | limn→∞dWJ1​(Qτ,ρn​(𝐱m)n,m,⨂ℓ=1mQ~τ,ζxℓm)≤limn→∞E​[∑ℓ=1msupτ≤t≤T‖Xtℓ,n−X~tℓ‖]=0.\displaystyle\lim\_{n\rightarrow\infty}d\_{W}^{J\_{1}}\bigg(\amsmathbb{Q}^{n,m}\_{\tau,\rho^{n}(\mathbf{x}^{m})},\bigotimes\_{\ell=1}^{m}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x^{m}\_{\ell}}\bigg)\leq\lim\_{n\rightarrow\infty}\amsmathbb{E}\bigg[\sum\_{\ell=1}^{m}\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\widetilde{X}\_{t}^{\ell}\|\bigg]=0. |  |

By applying the same methods, we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | E\displaystyle\amsmathbb{E} | [∑ℓ=m+1m+ksupτ≤t≤T‖Xtℓ,n−X¯tℓ‖]\displaystyle\bigg[\sum\_{\ell=m+1}^{m+k}\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C3​(Δ,n,k)​(1n​E​[∑i=1msupτ≤t≤T‖Xti,n−X~ti‖]+Kn+C​β​(n)+α​(n)Cf​Δ),\displaystyle\leq C\_{3}(\Delta,n,k)\bigg(\frac{1}{n}\amsmathbb{E}\bigg[\sum\_{i=1}^{m}\sup\_{\tau\leq t\leq T}\|X\_{t}^{i,n}-\widetilde{X}\_{t}^{i}\|\bigg]+\frac{K}{n}+C\beta(n)+\frac{\alpha(n)}{C\_{f}\Delta}\bigg), |  |

where C3​(Δ,n,k):=k​eCμ​Δ​(1+kn)​Cμ​ΔC\_{3}(\Delta,n,k):=ke^{C\_{\mu}\Delta(1+\frac{k}{n})}C\_{\mu}\Delta. Taking the limit on both sides, yields

|  |  |  |
| --- | --- | --- |
|  | limn→∞dWJ1​(Qτ,ρn​(𝐱m)n,m:k,Q¯τ,ζ⊗k)≤limn→∞E​[∑ℓ=m+1ksupτ≤t≤T‖Xtℓ,n−X¯tℓ‖]=0.\displaystyle\lim\_{n\rightarrow\infty}d\_{W}^{J\_{1}}\bigg(\amsmathbb{Q}^{n,m:k}\_{\tau,\rho^{n}(\mathbf{x}^{m})},\bar{\amsmathbb{Q}}\_{\tau,\zeta}^{\otimes k}\bigg)\leq\lim\_{n\rightarrow\infty}\amsmathbb{E}\bigg[\sum\_{\ell=m+1}^{k}\sup\_{\tau\leq t\leq T}\|X\_{t}^{\ell,n}-\bar{X}\_{t}^{\ell}\|\bigg]=0. |  |

## 5. Non-life insurance applications

In non-life insurance the main quantity of interest is the expected claim amount. If we have a cohort of nn individuals, the claim amount of each individual is modelled by

|  |  |  |
| --- | --- | --- |
|  | Wtℓ,n=∫(0,t]×Az​Qℓ,n​(d​s,d​z)=∑i=1Ntℓ,nZiℓ,n,\displaystyle W\_{t}^{\ell,n}=\int\_{(0,t]\times A}z\,Q^{\ell,n}(\mathrm{d}s,\mathrm{d}z)=\sum\_{i=1}^{N\_{t}^{\ell,n}}Z\_{i}^{\ell,n}, |  |

where Qℓ,nQ^{\ell,n} is a random counting measure. The counting process Ntℓ,n=Qℓ,n​((0,t]×A)N\_{t}^{\ell,n}=Q^{\ell,n}((0,t]\times A) can be interpreted as the number of claims, while the marks (Ziℓ,n)i∈N(Z\_{i}^{\ell,n})\_{i\in\amsmathbb{N}} are the claim sizes. The set A⊆[0,∞)A\subseteq[0,\infty) is the set of potential claim sizes. In reality the cohort is not entirely homogeneous, which is why each individual is allowed to have ℱ0\mathcal{F}\_{0}-measurable covariates Uℓ,nU^{\ell,n} taking values in the covariate space 𝒰⊆Rd′\mathcal{U}\subseteq\amsmathbb{R}^{d^{\prime}}. Let νn∈𝒫1​(𝒰n)\nu^{n}\in\mathcal{P}^{1}(\mathcal{U}^{n}) be the distribution of (Uℓ,n)ℓ=1,…,n(U^{\ell,n})\_{\ell=1,\ldots,n}. We assume that νn\nu^{n} is ν\nu-chaotic for some ν∈𝒫1​(𝒰)\nu\in\mathcal{P}^{1}(\mathcal{U}). Thus while the individuals can be heterogenous, the heterogenuity has to be sufficiently homogeneous.

This can all jointly be modelled by the process Xℓ,n=(Wℓ,n,Nℓ,n,Uℓ,n)X^{\ell,n}=(W^{\ell,n},N^{\ell,n},U^{\ell,n}) on state space E=[0,∞)×N0×𝒰E=[0,\infty)\times\amsmathbb{N}\_{0}\times\mathcal{U} defined by

|  |  |  |
| --- | --- | --- |
|  | Xtℓ,n=(Wtℓ,nNtℓ,nUtℓ,n)=(00Uℓ,n)+∫(0,t]×A(z10)​Qℓ,n​(d​s,d​z),ℓ=1,…,n,\displaystyle X\_{t}^{\ell,n}=\begin{pmatrix}W\_{t}^{\ell,n}\\ N\_{t}^{\ell,n}\\ U\_{t}^{\ell,n}\end{pmatrix}=\begin{pmatrix}0\\ 0\\ U^{\ell,n}\end{pmatrix}+\int\_{(0,t]\times A}\begin{pmatrix}z\\ 1\\ 0\end{pmatrix}Q^{\ell,n}(\mathrm{d}s,\mathrm{d}z),\quad\ell=1,\ldots,n, |  |

where Qℓ,nQ^{\ell,n} has compensating measure

|  |  |  |
| --- | --- | --- |
|  | Lℓ,n​(d​t,d​z)=μt​(Wt−ℓ,n,Nt−ℓ,n,Uℓ,n,εt−n,d​z)​d​t.\displaystyle L^{\ell,n}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(W\_{t-}^{\ell,n},N\_{t-}^{\ell,n},U^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}z)\mathrm{d}t. |  |

Here μt​(w,m,u,ρ,d​z)=λt​(w,m,u,ρ)​rt​(w,m,u,ρ,d​z)\mu\_{t}(w,m,u,\rho,\mathrm{d}z)=\lambda\_{t}(w,m,u,\rho)r\_{t}(w,m,u,\rho,\mathrm{d}z) where λ\lambda is the claim occurence intensity, while the probability measure rr is the claim size distribution. Both are allowed to depend on the covariates, which are constant over time. The initial distribution of the process X=(X1,n,…,Xn,n)X=(X^{1,n},\ldots,X^{n,n}) is now given by ζn=δ{0}⊗n⊗δ{0}⊗n⊗νn\zeta^{n}=\delta\_{\{0\}}^{\otimes n}\otimes\delta\_{\{0\}}^{\otimes n}\otimes\nu^{n} and it is clear that ζn\zeta^{n} is ζ\zeta-chaotic, where ζ:=δ{0}⊗δ{0}⊗ν\zeta:=\delta\_{\{0\}}\otimes\delta\_{\{0\}}\otimes\nu.

The main quantities of interest to be calculated are the expected claim amounts given by:

###### Definition 5.1.

The cohort-wide expected claim amount is defined as

|  |  |  |
| --- | --- | --- |
|  | V1,n​(T):=E​[WT1,n].\displaystyle V^{1,n}(T):=\amsmathbb{E}[W^{1,n}\_{T}]. |  |

The individual expected claim amount is defined as

|  |  |  |
| --- | --- | --- |
|  | V1,n​(T,u):=E​[WT1,n|U1,n=u].\displaystyle V^{1,n}(T,u):=\amsmathbb{E}[W^{1,n}\_{T}|U^{1,n}=u]. |  |

The corresponding mean-field model is given by the following distribution dependent jump process

|  |  |  |
| --- | --- | --- |
|  | X¯t=(W¯tN¯tU¯t)=(00U¯)+∫(τ,t]×A(z10)​Q¯​(d​s,d​z),\displaystyle\bar{X}\_{t}=\begin{pmatrix}\bar{W}\_{t}\\ \bar{N}\_{t}\\ \bar{U}\_{t}\end{pmatrix}=\begin{pmatrix}0\\ 0\\ \bar{U}\end{pmatrix}+\int\_{(\tau,t]\times A}\begin{pmatrix}z\\ 1\\ 0\end{pmatrix}\bar{Q}(\mathrm{d}s,\mathrm{d}z), |  |

where Q¯\bar{Q} has compensating measure

|  |  |  |
| --- | --- | --- |
|  | L¯​(d​t,d​z)=μt​(W¯t−,N¯t−,U¯,η¯t,d​z)​d​t\displaystyle\bar{L}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(\bar{W}\_{t-},\bar{N}\_{t-},\bar{U},\bar{\eta}\_{t},\mathrm{d}z)\mathrm{d}t |  |

and U¯\bar{U} has distribution ν\nu. The corresponding mean-field expected claim amounts are:

###### Definition 5.2.

The cohort-wide mean-field expected claim amount is defined as

|  |  |  |
| --- | --- | --- |
|  | V¯​(T):=E​[W¯T].\displaystyle\bar{V}(T):=\amsmathbb{E}[\bar{W}\_{T}]. |  |

The individual mean-field expected claim amount is defined as

|  |  |  |
| --- | --- | --- |
|  | V¯​(T,u):=E​[W¯T|U¯=u].\displaystyle\bar{V}(T,u):=\amsmathbb{E}[\bar{W}\_{T}|\bar{U}=u]. |  |

We now have the following result:

###### Proposition 5.3.

Let Assumptions [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") be satisfied for some q>1q>1 such that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[‖U1,n‖q]<∞\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[\|U^{1,n}\|^{q}]<\infty |  |

for the same qq. Then it holds that

|  |  |  |
| --- | --- | --- |
|  | limn→∞V1,n​(T)=V¯​(T)\displaystyle\lim\_{n\rightarrow\infty}V^{1,n}(T)=\bar{V}(T) |  |

and if additionally νn\nu^{n} satisfies Assumption [4](https://arxiv.org/html/2511.04198v1#Thmassumption4 "Assumption 4. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") we have that

|  |  |  |
| --- | --- | --- |
|  | limn→∞V1,n​(T,u)=V¯​(T,u).\displaystyle\lim\_{n\rightarrow\infty}V^{1,n}(T,u)=\bar{V}(T,u). |  |

###### Proof.

The goal is to apply Proposition [C.1](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance"). The necessary chaosticity is guaranteed by Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") and Theorem [4.3](https://arxiv.org/html/2511.04198v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance"). It remains to show that there exists an ε>0\varepsilon>0 such that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[(WT1,n)1+ε]<∞.\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[(W^{1,n}\_{T})^{1+\varepsilon}]<\infty. |  |

For this we note that by Lemma [B.1](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance") we have that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[|WT1,n|q]≤2q−1​(supn∈NE​[‖U1,n‖q]+Cr​E​[MTq])<∞,\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[|W\_{T}^{1,n}|^{q}]\leq 2^{q-1}\bigg(\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[\|U^{1,n}\|^{q}]+C\_{r}\amsmathbb{E}[M\_{T}^{q}]\bigg)<\infty, |  |

since MtM\_{t} is Poisson process with intensity CλC\_{\lambda}. As q>1q>1, the result follows.
∎

This shows that we indeed have convergence of the cohort-wide expected claim amount for one individual in the nn-individual model towards the mean-field expected claim amount, as long as the distribution of covariates is chaotic and
  
(U1,n)n∈N(U^{1,n})\_{n\in\amsmathbb{N}} is uniformly integrable. If the distribution of the covariates in addition satisfies the conditional chaosticity property required in Assumption [4](https://arxiv.org/html/2511.04198v1#Thmassumption4 "Assumption 4. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance"), then one can also use a mean-field approximation for the individual expected claim amount.

If we strengthen the moment conditions a little, then one can obtain the following law of large numbers:

###### Proposition 5.4.

Let Assumptions [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") be satisfied for some q>2q>2 such that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[‖U1,n‖q]<∞\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[\|U^{1,n}\|^{q}]<\infty |  |

for the same qq. Then it holds that

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1nWTℓ,n→L2V¯​(T).\displaystyle\frac{1}{n}\sum\_{\ell=1}^{n}W\_{T}^{\ell,n}\,\stackrel{{\scriptstyle L^{2}}}{{\rightarrow}}\,\bar{V}(T). |  |

###### Proof.

The goal is to apply Proposition [C.2](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem2 "Proposition C.2. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance"). The necessary chaosticity is guaranteed by Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") and that there exists a ε>0\varepsilon>0 such that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[(WT1,n)2+ε]<∞\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[(W^{1,n}\_{T})^{2+\varepsilon}]<\infty |  |

follows again from Lemma [B.1](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance").
∎

This shows, that as the number of individuals grows, the cohort average of the total claim size converges to the expected total claim size under the mean-field model. Thus even though the individuals are dependent and weakly heterogenous, all risk is diversified away when the portfolio is sufficiently large.

Let now σn2:=Var​(WT1,n)\sigma^{2}\_{n}:=\mathrm{Var}(W\_{T}^{1,n}) and σ2:=Var​(W¯T)\sigma^{2}:=\mathrm{Var}(\bar{W}\_{T}). Then under some additional assumptions we have the following central limit theorem:

###### Proposition 5.5.

Let Assumptions [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") be satisfied for some q>4q>4 such that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[‖U1,n‖q]<∞\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[\|U^{1,n}\|^{q}]<\infty |  |

for the same qq. Furthermore assume that

|  |  |  |
| --- | --- | --- |
|  | limn→∞n​Cov​(WT1,n,WT2,n)=0​ and ​limn→∞n​(V1,n​(T)−V¯​(T))=0.\displaystyle\lim\_{n\rightarrow\infty}n\mathrm{Cov}(W^{1,n}\_{T},W^{2,n}\_{T})=0\text{ and }\lim\_{n\rightarrow\infty}\sqrt{n}(V^{1,n}(T)-\bar{V}(T))=0. |  |

Then it holds that

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1nWTℓ,n−V¯​(T)σ→DN​(0,1).\displaystyle\frac{1}{\sqrt{n}}\sum\_{\ell=1}^{n}\frac{W\_{T}^{\ell,n}-\bar{V}(T)}{\sigma}\stackrel{{\scriptstyle D}}{{\rightarrow}}N(0,1). |  |

###### Proof.

The goal is to apply Proposition [C.3](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem3 "Proposition C.3. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance"). The necessary chaosticity is guaranteed by Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") and that there exists a ε>0\varepsilon>0 such that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[(WT1,n)4+ε]<∞\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[(W^{1,n}\_{T})^{4+\varepsilon}]<\infty |  |

is again guaranteed by Lemma [B.1](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance").
∎

Apart from a stricter moment condition on the distribution of claim sizes and the covariates, the additional assumptions require the convergence of the covariance between the total claim sizes of the two individuals to zero and the convergence of the portfolio-wide claim amount to its mean-field equivalent to be sufficiently fast. Whether this indeed is the case is very difficult to verify theoretically.

In most cases we would assume that the distribution of claim sizes has a density with respect to some measure ν\nu on AA. In that case we would have

|  |  |  |
| --- | --- | --- |
|  | rt​(w,m,u,ρ,d​z)=gtz​(w,m,u,ρ)​ν​(d​z).\displaystyle r\_{t}(w,m,u,\rho,\mathrm{d}z)=g\_{t}^{z}(w,m,u,\rho)\nu(\mathrm{d}z). |  |

The intensity kernel is then given by

|  |  |  |
| --- | --- | --- |
|  | μt​(w,m,u,ρ,d​z)=λt​(w,m,u,ρ)​gtz​(w,m,u,ρ)​ν​(d​z).\displaystyle\mu\_{t}(w,m,u,\rho,\mathrm{d}z)=\lambda\_{t}(w,m,u,\rho)g\_{t}^{z}(w,m,u,\rho)\nu(\mathrm{d}z). |  |

The following result states sufficient conditions on λ\lambda and gg in order for Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") to be satisfied. For notational simplicity, we let x=(w,m,u)x=(w,m,u).

###### Proposition 5.6.

Assume that ν∈ℳ1​(A)\nu\in\mathcal{M}^{1}(A) and that

1. (1)

   There exists Cλ>0C\_{\lambda}>0 and Cr>0C\_{r}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | λt​(x,ρ)≤Cλ​ and ​∫A|z|​gtz​(x,ρ)​ν​(d​z)≤Cr.\displaystyle\lambda\_{t}(x,\rho)\leq C\_{\lambda}\text{ and }\int\_{A}|z|g\_{t}^{z}(x,\rho)\nu(\mathrm{d}z)\leq C\_{r}. |  |

   for all x∈Ex\in E and ρ∈𝒫1​(E)\rho\in\mathcal{P}^{1}(E).
2. (2)

   There exists Cλ,L>0C\_{\lambda,L}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | |λt​(x1,ρ1)−λt​(x2,ρ2)|≤Cλ,L​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle|\lambda\_{t}(x\_{1},\rho\_{1})-\lambda\_{t}(x\_{2},\rho\_{2})|\leq C\_{\lambda,L}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

   for all x1,x2,y∈Ex\_{1},x\_{2},y\in E and ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(E).
3. (3)

   There exists a non-negative measurable function Cg​(z)C\_{g}(z) with
     
   ∫A‖z‖​Cg​(z)​ν​(d​z)<∞\int\_{A}\|z\|C\_{g}(z)\nu(\mathrm{d}z)<\infty such that

   |  |  |  |
   | --- | --- | --- |
   |  | |gtz​(x1,ρ1)−gtz​(x2,ρ2)|≤Cg​(z)​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle|g^{z}\_{t}(x\_{1},\rho\_{1})-g^{z}\_{t}(x\_{2},\rho\_{2})|\leq C\_{g}(z)(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

   for all x1,x2,y∈Ex\_{1},x\_{2},y\in E and ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(E).

Then Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") is satisfied.

###### Proof.

The first assumption directly corresponds to Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1).

In order to prove Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(2), we let ff by any Lip​(1)\text{Lip}(1)-function with f​(0)=0f(0)=0. Then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∫A\displaystyle\bigg|\int\_{A} | f(z)λt(x1,ρ1)gtz(x1,ρ1)ν(dz)−∫Af(z)λt(x2,ρ2)gtz(x2,ρ2)ν(dz)|\displaystyle f(z)\lambda\_{t}(x\_{1},\rho\_{1})g^{z}\_{t}(x\_{1},\rho\_{1})\nu(\mathrm{d}z)-\int\_{A}f(z)\lambda\_{t}(x\_{2},\rho\_{2})g^{z}\_{t}(x\_{2},\rho\_{2})\nu(\mathrm{d}z)\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∫A|f​(z)|​λt​(x1,ρ1)​|gtz​(x1,ρ1)−gtz​(x2,ρ2)|​ν​(d​z)\displaystyle\int\_{A}|f(z)|\lambda\_{t}(x\_{1},\rho\_{1})|g^{z}\_{t}(x\_{1},\rho\_{1})-g\_{t}^{z}(x\_{2},\rho\_{2})|\nu(\mathrm{d}z) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|λt​(x1,ρ1)−λt​(x2,ρ2)|​∫A|f​(z)|​gtz​(x2,ρ2)​ν​(d​z)\displaystyle+|\lambda\_{t}(x\_{1},\rho\_{1})-\lambda\_{t}(x\_{2},\rho\_{2})|\int\_{A}|f(z)|g\_{t}^{z}(x\_{2},\rho\_{2})\nu(\mathrm{d}z) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(Cλ​∫A‖z‖​Cg​(z)​ν​(d​z)+Cλ,L​Cr)​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle\leq\bigg(C\_{\lambda}\int\_{A}\|z\|C\_{g}(z)\,\nu(\mathrm{d}z)+C\_{\lambda,L}C\_{r}\bigg)(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

Taking the supremum over f∈Lip​(1)f\in\text{Lip}(1) with f​(0)=0f(0)=0 shows that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(2) is satisfied.
∎

Note that Proposition [5.6](https://arxiv.org/html/2511.04198v1#S5.Thmtheorem6 "Proposition 5.6. ‣ 5. Non-life insurance applications ‣ Mean-field approximations in insurance") does not require AA to be bounded. Hence it is possible to choose A=[0,∞)A=[0,\infty) and let gtz​(x,ρ)g\_{t}^{z}(x,\rho) be a density with respect to the Lebesgue measure on [0,∞)[0,\infty). This density can then be measure-dependent.

In order to build a model with this feature, we need to be able have sufficient conditions for when gtz​(x,ρ)g\_{t}^{z}(x,\rho) satisfies (3) of Proposition [5.6](https://arxiv.org/html/2511.04198v1#S5.Thmtheorem6 "Proposition 5.6. ‣ 5. Non-life insurance applications ‣ Mean-field approximations in insurance"). For this the following result is useful:

###### Proposition 5.7.

Let B⊆RkB\subseteq\amsmathbb{R}^{k} and let g:[0,T]×E2→Bg:[0,T]\times E^{2}\rightarrow B and assume that there exists Cg>0C\_{g}>0 and q≥1q\geq 1 such that

|  |  |  |
| --- | --- | --- |
|  | ‖g​(t,x1,y1)−g​(t,x1,y2)‖B≤Cg​(‖x1−x2‖+‖y1−y2‖),\displaystyle\|g(t,x\_{1},y\_{1})-g(t,x\_{1},y\_{2})\|\_{B}\leq C\_{g}(\|x\_{1}-x\_{2}\|+\|y\_{1}-y\_{2}\|), |  |

for all (x1,y1),(x2,y2)∈E2(x\_{1},y\_{1}),(x\_{2},y\_{2})\in E^{2} and such that

|  |  |  |
| --- | --- | --- |
|  | ‖g​(t,x,y)‖≤Cg​(1+‖y‖q)\displaystyle\|g(t,x,y)\|\leq C\_{g}(1+\|y\|^{q}) |  |

for all (t,x,y)∈[0,T]×E2(t,x,y)\in[0,T]\times E^{2}.
Define f:[0,T]×E×𝒫q​(E)→Bf:[0,T]\times E\times\mathcal{P}^{q}(E)\rightarrow B by

|  |  |  |
| --- | --- | --- |
|  | f​(t,x,ρ):=∫Eg​(t,x,y)​ρ​(d​y).\displaystyle f(t,x,\rho):=\int\_{E}g(t,x,y)\rho(\mathrm{d}y). |  |

Then ff satisfies

|  |  |  |
| --- | --- | --- |
|  | ‖f​(t,x1,ρ1)−f​(t,x2,ρ2)‖B≤Cg​(‖x1−x2‖+dW​(ρ1,ρ2)),\displaystyle\|f(t,x\_{1},\rho\_{1})-f(t,x\_{2},\rho\_{2})\|\_{B}\leq C\_{g}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})), |  |

for all x1,x2∈Ex\_{1},x\_{2}\in E and ρ1,ρ2∈𝒫q​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{q}(E).

###### Proof.

First we note, that ff is well-behaved, since we for any ρ∈𝒫q​(E)\rho\in\mathcal{P}^{q}(E) have

|  |  |  |
| --- | --- | --- |
|  | ‖f​(t,x,ρ)‖B≤∫E‖g​(t,x,y)‖B​ρ​(d​y)≤Cg​(1+∫E‖y‖q​ρ​(d​y))<∞.\displaystyle\|f(t,x,\rho)\|\_{B}\leq\int\_{E}\|g(t,x,y)\|\_{B}\rho(\mathrm{d}y)\leq C\_{g}\bigg(1+\int\_{E}\|y\|^{q}\rho(\mathrm{d}y)\bigg)<\infty. |  |

Let now π​(d​y1,d​y2)\pi(\mathrm{d}y\_{1},\mathrm{d}y\_{2}) be a probability measure on E2E^{2}, such that π​(d​y1,E)=ρ1​(d​y1)\pi(\mathrm{d}y\_{1},E)=\rho\_{1}(\mathrm{d}y\_{1}) and π​(E,d​y2)=ρ2​(d​y2)\pi(E,\mathrm{d}y\_{2})=\rho\_{2}(\mathrm{d}y\_{2}). We then have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f​(t,x1,ρ1)−f​(t,x2,ρ2)‖B\displaystyle\|f(t,x\_{1},\rho\_{1})-f(t,x\_{2},\rho\_{2})\|\_{B} | =‖∫Eg​(t,x1,y)​ρ1​(d​y)−∫Eg​(t,x2,y)​ρ2​(d​y)‖B\displaystyle=\bigg\|\int\_{E}g(t,x\_{1},y)\rho\_{1}(\mathrm{d}y)-\int\_{E}g(t,x\_{2},y)\rho\_{2}(\mathrm{d}y)\bigg\|\_{B} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖∫E2g​(t,x1,y1)−g​(t,x2,y2)​π​(d​y1,d​y2)‖B\displaystyle=\bigg\|\int\_{E^{2}}g(t,x\_{1},y\_{1})-g(t,x\_{2},y\_{2})\pi(\mathrm{d}y\_{1},\mathrm{d}y\_{2})\bigg\|\_{B} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫E2‖g​(t,x1,y1)−g​(t,x2,y2)‖B​π​(d​y1,d​y2)\displaystyle\leq\int\_{E^{2}}\|g(t,x\_{1},y\_{1})-g(t,x\_{2},y\_{2})\|\_{B}\pi(\mathrm{d}y\_{1},\mathrm{d}y\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cg​(‖x1−x2‖+∫E2‖y1−y2‖B​π​(d​y1,d​y2)).\displaystyle\leq C\_{g}\bigg(\|x\_{1}-x\_{2}\|+\int\_{E^{2}}\|y\_{1}-y\_{2}\|\_{B}\pi(\mathrm{d}y\_{1},\mathrm{d}y\_{2})\bigg). |  |

As this inequality holds for all π\pi with π​(d​y1,E)=ρ1​(d​y1)\pi(\mathrm{d}y\_{1},E)=\rho\_{1}(\mathrm{d}y\_{1}) and π​(E,d​y2)=ρ2​(d​y2)\pi(E,\mathrm{d}y\_{2})=\rho\_{2}(\mathrm{d}y\_{2}), the inequality also holds when taking the infimum over all such probability measures π\pi. Thus we have that

|  |  |  |
| --- | --- | --- |
|  | ‖f​(x1,ρ1)−f​(x2,ρ2)‖B≤Cg​(‖x1−x2‖+dW​(ρ1,ρ2)).\displaystyle\|f(x\_{1},\rho\_{1})-f(x\_{2},\rho\_{2})\|\_{B}\leq C\_{g}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})). |  |

∎

This shows that if hy:[0,T]×E×B→[0,∞)h^{y}:[0,T]\times E\times B\rightarrow[0,\infty) is Lipschitz in the second and third argument, then γy​(t,x,ρ):=hy​(t,x,f​(t,x,ρ))\gamma^{y}(t,x,\rho):=h^{y}(t,x,f(t,x,\rho)) satisfies Assumption (3) of Proposition [5.6](https://arxiv.org/html/2511.04198v1#S5.Thmtheorem6 "Proposition 5.6. ‣ 5. Non-life insurance applications ‣ Mean-field approximations in insurance").

###### Example 5.8 (Gamma-distributed claim-sizes).

We now assume that λt​(w,m,ρ)=Cλ>0\lambda\_{t}(w,m,\rho)=C\_{\lambda}>0, that is the number of claims is Poisson distributed. Furthermore we assume that A=[0,∞)A=[0,\infty) and let the claim sizes be Γ​(α,θ​(w,m,ρ))\Gamma(\alpha,\theta(w,m,\rho))-distributed. That is

|  |  |  |
| --- | --- | --- |
|  | rt​(w,m,ρ,d​z)=gtz​(w,m,ρ)​d​z,\displaystyle r\_{t}(w,m,\rho,\mathrm{d}z)=g\_{t}^{z}(w,m,\rho)\mathrm{d}z, |  |

where gtz​(w,m,ρ)=f​(z|α,θt​(ρ))g\_{t}^{z}(w,m,\rho)=f(z|\alpha,\theta\_{t}(\rho)) and where f​(z|α,θ)f(z|\alpha,\theta) is the density of a Γ​(α,θ)\Gamma(\alpha,\theta) distribution. The shape parameter α\alpha is considered fixed and thus

|  |  |  |
| --- | --- | --- |
|  | gtz​(w,m,ρ)=xα−1Γ​(α)​θ​(w,m,ρ)α​exp⁡(−xθt​(ρ))\displaystyle g\_{t}^{z}(w,m,\rho)=\frac{x^{\alpha-1}}{\Gamma(\alpha)\theta(w,m,\rho)^{\alpha}}\exp\bigg(-\frac{x}{\theta\_{t}(\rho)}\bigg) |  |

We thus allow for a measure-dependent scale parameter. In order to construct θt​(ρ)\theta\_{t}(\rho), we define the function hK:E→[0,K]h\_{K}:E\rightarrow[0,K] as

|  |  |  |
| --- | --- | --- |
|  | h​(w,m):={0when ​m=0min⁡{wm,K}when ​m≠0,\displaystyle h(w,m):=\begin{cases}0&\text{when }m=0\\ \min\{\frac{w}{m},K\}&\text{when }m\neq 0,\end{cases} |  |

for some K>0K>0. Note that this function is Lipschitz continuous. For very large KK, we can interpret hK​(Wtℓ,n,Ntℓ,n)h\_{K}(W\_{t}^{\ell,n},N\_{t}^{\ell,n}) as the average claim size of individual ℓ\ell and thus

|  |  |  |
| --- | --- | --- |
|  | m^tn:=1n​∑ℓ=1nhK​(Wtℓ,n,Ntℓ,n)\displaystyle\hat{m}^{n}\_{t}:=\frac{1}{n}\sum\_{\ell=1}^{n}h\_{K}(W\_{t}^{\ell,n},N\_{t}^{\ell,n}) |  |

as the average claim size of the entire cohort. Define m¯:𝒫1​(E)→[0,∞)\bar{m}:\mathcal{P}^{1}(E)\rightarrow[0,\infty) as

|  |  |  |
| --- | --- | --- |
|  | m¯​(ρ):=∫EhK​(v,k)​ρ​(d​v,d​k).\displaystyle\bar{m}(\rho):=\int\_{E}h\_{K}(v,k)\rho(\mathrm{d}v,\mathrm{d}k). |  |

Then m^tn=m¯​(εtn)\hat{m}^{n}\_{t}=\bar{m}(\varepsilon\_{t}^{n}). The function θt​(ρ)\theta\_{t}(\rho) is now defined as

|  |  |  |
| --- | --- | --- |
|  | θt​(ρ):=max⁡{θ¯,min⁡{u​(t)​m¯t​(ρ)α+(1−u​(t))​θ∗,θ¯}},\displaystyle\theta\_{t}(\rho):=\max\bigg\{\underline{\theta},\,\min\bigg\{u(t)\frac{\bar{m}\_{t}(\rho)}{\alpha}+(1-u(t))\theta^{\*},\,\widebar{\theta}\bigg\}\bigg\}, |  |

for 0<θ¯<θ∗<θ¯0<\underline{\theta}<\theta^{\*}<\widebar{\theta} and u:[0,T]→[0,1]u:[0,T]\rightarrow[0,1]. When inserting εtn\varepsilon\_{t}^{n} we get

|  |  |  |
| --- | --- | --- |
|  | θt​(εtn):=max⁡{θ¯,min⁡{u​(t)​m^tnα+(1−u​(t))​θ∗,θ¯}}.\displaystyle\theta\_{t}(\varepsilon\_{t}^{n}):=\max\bigg\{\underline{\theta},\,\min\bigg\{u(t)\frac{\hat{m}\_{t}^{n}}{\alpha}+(1-u(t))\theta^{\*},\,\widebar{\theta}\bigg\}\bigg\}. |  |

Given iid. observations (Yi)i=1,…,n(Y\_{i})\_{i=1,\ldots,n} from a Γ​(α,θ)\Gamma(\alpha,\theta)-distribution, the maximum-likelihood estimate for θ\theta when α\alpha is known is

|  |  |  |
| --- | --- | --- |
|  | θ^=1n​α​∑i=1nYi.\displaystyle\hat{\theta}=\frac{1}{n\alpha}\sum\_{i=1}^{n}Y\_{i}. |  |

So in that sense θt​(ρ)\theta\_{t}(\rho) can be seen as a credibility estimate between the estimated scale parameter of the portfolio and a benchmark θ∗\theta^{\*}. The parameters θ¯\underline{\theta} and θ¯\widebar{\theta} define maximum and minimum values for the scale parameter. The function uu determines how much weight is placed on the cohort estimate and it would typically be increasing, placing more weight on the cohort estimate as time goes by and more information becomes available.

We now have to ensure, that the conditions in Proposition [5.6](https://arxiv.org/html/2511.04198v1#S5.Thmtheorem6 "Proposition 5.6. ‣ 5. Non-life insurance applications ‣ Mean-field approximations in insurance") are satisfied. Since hKh\_{K} is Lipschitz and bounded, Proposition [5.7](https://arxiv.org/html/2511.04198v1#S5.Thmtheorem7 "Proposition 5.7. ‣ 5. Non-life insurance applications ‣ Mean-field approximations in insurance") yields that m¯​(ρ)\bar{m}(\rho) is Lipschitz. Hence θt​(ρ)\theta\_{t}(\rho) is Lipschitz in ρ\rho.

As gtz​(w,m,ρ):=f​(z|α,θt​(ρ))g\_{t}^{z}(w,m,\rho):=f(z|\alpha,\theta\_{t}(\rho)), it can be shown that

|  |  |  |
| --- | --- | --- |
|  | |gtz​(w1,m1,ρ1)−gtz​(w1,m2,ρ2)|≤Cg​(z)​dW​(ρ1,ρ2)\displaystyle|g\_{t}^{z}(w\_{1},m\_{1},\rho\_{1})-g\_{t}^{z}(w\_{1},m\_{2},\rho\_{2})|\leq C\_{g}(z)d\_{W}(\rho\_{1},\rho\_{2}) |  |

for all (w1,m1),(w2,m2)∈E(w\_{1},m\_{1}),(w\_{2},m\_{2})\in E and ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(E), where Cg​(z)=C​zα−1​e−z/θ¯C\_{g}(z)=Cz^{\alpha-1}e^{-z/\widebar{\theta}}. It can be seen that

|  |  |  |
| --- | --- | --- |
|  | ∫[0,∞)z​Cg​(z)​dz=θ¯α+2​α​Γ​(α+1)<∞.\displaystyle\int\_{[0,\infty)}zC\_{g}(z)\mathrm{d}z=\widebar{\theta}^{\alpha+2}\alpha\Gamma(\alpha+1)<\infty. |  |

Thus condition (3) of Proposition [5.6](https://arxiv.org/html/2511.04198v1#S5.Thmtheorem6 "Proposition 5.6. ‣ 5. Non-life insurance applications ‣ Mean-field approximations in insurance") is satisfied. The other conditions are easily checked to be true as well. This shows that the mean-field approximation is valid.

## 6. Life insurance applications

In life insurance applications the biometric risk that is insured and other quantities of interest are modelled by a jump process XX on a state space E⊆RdE\subseteq\amsmathbb{R}^{d}. Often it is most convenient to specify the model in terms of the jump destination representation and thus the cohort is modelled by

|  |  |  |
| --- | --- | --- |
|  | Xtℓ,n=Yℓ,n+∫(τ,t]×E(y−Xs−ℓ,n)​Qℓ,n​(d​s,d​a),ℓ=1,…,n,\displaystyle X\_{t}^{\ell,n}=Y^{\ell,n}+\int\_{(\tau,t]\times E}(y-X\_{s-}^{\ell,n})Q^{\ell,n}(ds,da),\quad\ell=1,\ldots,n, |  |

where the random counting measures Qℓ,nQ^{\ell,n} have compensating measures

|  |  |  |
| --- | --- | --- |
|  | Lℓ,n​(d​t,d​y)=μt​(Xt−ℓ,n,εt−n,d​y)​d​t,ℓ=1,…,n,\displaystyle L^{\ell,n}(\mathrm{d}t,\mathrm{d}y)=\mu\_{t}(X\_{t-}^{\ell,n},\varepsilon\_{t-}^{n},\mathrm{d}y)\mathrm{d}t,\quad\ell=1,\ldots,n, |  |

might be the proper description. The intial distribution of the cohort is given by ζn∈𝒫1​(En)\zeta^{n}\in\mathcal{P}^{1}(E^{n}) and it is assumed that (ζn)n∈N(\zeta^{n})\_{n\in\amsmathbb{N}} is ζ\zeta-chaotic for ζ∈𝒫1​(E)\zeta\in\mathcal{P}^{1}(E). Within this model, each individual recieves the contractual payments given by

|  |  |  |
| --- | --- | --- |
|  | Bℓ,n​(d​t)=b​(t,Xtℓ,n)​d​t+∫Eby​(t,Xt−ℓ,n)​Qℓ,n​(d​t,d​y),ℓ=1,…,n,\displaystyle B^{\ell,n}(\mathrm{d}t)=b(t,X\_{t}^{\ell,n})\mathrm{d}t+\int\_{E}b^{y}(t,X\_{t-}^{\ell,n})Q^{\ell,n}(\mathrm{d}t,\mathrm{d}y),\quad\ell=1,\ldots,n, |  |

where Qℓ,nQ^{\ell,n} is the same random counting measure which also drives Xℓ,nX^{\ell,n}. For now we only assume that the payment functions bb and (by)y∈E(b^{y})\_{y\in E} are bounded and measurable. The function bb describes the sojourn payments, while the functions (by)y∈E(b^{y})\_{y\in E} describe the transition payments. Let r:[0,T]→Rr:[0,T]\rightarrow\amsmathbb{R} be a bounded and measurable function and define the present value of future payments as

|  |  |  |
| --- | --- | --- |
|  | P​Vℓ,n​(τ):=∫τTe−∫τtr​(u)​du​Bℓ,n​(d​t).\displaystyle PV^{\ell,n}(\tau):=\int\_{\tau}^{T}e^{-\int\_{\tau}^{t}r(u)\mathrm{d}u}B^{\ell,n}(\mathrm{d}t). |  |

We can now define the following two reserves:

###### Definition 6.1.

The cohort-wide reserve is defined as

|  |  |  |
| --- | --- | --- |
|  | V1,n​(τ):=E​[P​V1,n​(τ)].\displaystyle V^{1,n}(\tau):=\amsmathbb{E}[PV^{1,n}(\tau)]. |  |

The state-wise reserve is defined as

|  |  |  |
| --- | --- | --- |
|  | V1,n​(τ,x):=E​[P​V1,n​(τ)|Xτℓ,n=x].\displaystyle V^{1,n}(\tau,x):=\amsmathbb{E}[PV^{1,n}(\tau)|X^{\ell,n}\_{\tau}=x]. |  |

The calculation of the reserves in this nn-individual model by the forward method requires the numerical solution of the forward integro-differential equations of either Proposition [2.3](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") or Proposition [2.4](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance"). These systems explode in dimension for growing nn and therefore we would like to use a mean-field approximation.

The mean-field model X¯τ,ζ\bar{X}\_{\tau,\zeta} is given by ([2.7](https://arxiv.org/html/2511.04198v1#S2.E7 "In 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). The mean-field payment process is given by

|  |  |  |
| --- | --- | --- |
|  | B¯​(d​t)=b​(t,X¯t)​d​t+∫Eby​(t,X¯t)​Q¯​(d​t,d​y),\displaystyle\bar{B}(\mathrm{d}t)=b(t,\bar{X}\_{t})\mathrm{d}t+\int\_{E}b^{y}(t,\bar{X}\_{t})\bar{Q}(\mathrm{d}t,\mathrm{d}y), |  |

and the present value of future payments in the mean-field model is given by

|  |  |  |
| --- | --- | --- |
|  | P​V¯​(τ):=∫τTe−∫τtr​(u)​du​B¯​(d​t).\displaystyle\widebar{PV}(\tau):=\int\_{\tau}^{T}e^{-\int\_{\tau}^{t}r(u)\mathrm{d}u}\bar{B}(\mathrm{d}t). |  |

Thus we can define the mean-field reserves as

###### Definition 6.2.

The cohort-wide mean-field reserve is defined as

|  |  |  |
| --- | --- | --- |
|  | V¯​(τ):=E​[P​V¯​(τ)].\displaystyle\bar{V}(\tau):=\amsmathbb{E}[\widebar{PV}(\tau)]. |  |

The state-wise mean-field reserve is defined as

|  |  |  |
| --- | --- | --- |
|  | V¯​(τ,x):=E​[P​V¯​(τ)|X¯τ=x].\displaystyle\bar{V}(\tau,x):=\amsmathbb{E}[\widebar{PV}(\tau)|\bar{X}\_{\tau}=x]. |  |

In order to prove that the nn-individual reserves indeed converge to the mean-field reserves, we will have to make the following assumptions for the processes X¯\bar{X} and X~\widetilde{X} and for the random counting measures Q1,nQ^{1,n}:

###### Assumption 5.

Let (T¯i)(\bar{T}\_{i}) and (T~i)(\widetilde{T}\_{i}) be the jump times of X¯\bar{X} and X~\widetilde{X}. Assume that:

1. (1)

   There exists ε>0\varepsilon>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | P​(⋂i∈N(‖Δ​X¯T¯i‖>ε))=P​(⋂i∈N(‖Δ​X~T~i‖>ε))=1.\displaystyle\amsmathbb{P}\bigg(\bigcap\_{i\in\amsmathbb{N}}(\|\Delta\bar{X}\_{\bar{T}\_{i}}\|>\varepsilon)\bigg)=\amsmathbb{P}\bigg(\bigcap\_{i\in\amsmathbb{N}}(\|\Delta\widetilde{X}\_{\widetilde{T}\_{i}}\|>\varepsilon)\bigg)=1. |  |
2. (2)

   It holds that supn∈NE​[(Q1,n​((τ,T]×E))p]<∞\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}\big[\big(Q^{1,n}((\tau,T]\times E)\big)^{p}\big]<\infty for all p>1p>1.

The first assumption ensures that with probability one, the norm of the jump size of the mean-field processes will always exceed ε\varepsilon. The second assumption ensures that the total number of jumps for one individual does not behave too wildly when the number of individuals increases. In particular this holds if Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1) is satisfied, see Lemma [D.4](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem4 "Lemma D.4. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance"). The following assumptions are made for the payment functions bb and byb^{y}.

###### Assumption 6.

Let (T¯i)(\bar{T}\_{i}) and (T~i)(\widetilde{T}\_{i}) be the jump times of X¯\bar{X} and X~\widetilde{X}. Assume that

1. (1)

   (t,x)↦b​(t,x)(t,x)\mapsto b(t,x) is bounded and t↦b​(t,x)t\mapsto b(t,x) has a countable number of discontinuities for all x∈Ex\in E.
2. (2)

   (t,x,y,z)↦by​(t,x,z)(t,x,y,z)\mapsto b^{y}(t,x,z) is bounded and

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | P​(⋂i∈N((T¯i,X¯T¯i−,X¯T¯i,Δ​X¯Ti)∈Jb))\displaystyle\amsmathbb{P}\bigg(\bigcap\_{i\in\amsmathbb{N}}((\bar{T}\_{i},\bar{X}\_{\bar{T}\_{i}-},\bar{X}\_{\bar{T}\_{i}},\Delta\bar{X}\_{T\_{i}})\in J\_{b})\bigg) | =0\displaystyle=0 |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | P​(⋂i∈N((T~i,X~T~i−,X~T~i,Δ​X~Ti)∈Jb))\displaystyle\amsmathbb{P}\bigg(\bigcap\_{i\in\amsmathbb{N}}((\widetilde{T}\_{i},\widetilde{X}\_{\widetilde{T}\_{i}-},\widetilde{X}\_{\widetilde{T}\_{i}},\Delta\widetilde{X}\_{T\_{i}})\in J\_{b})\bigg) | =0,\displaystyle=0, |  |

   where Jb:={(t,x,y,z):by​(t,x,z)​ discontinuous}J\_{b}:=\{(t,x,y,z):b^{y}(t,x,z)\text{ discontinuous}\}.

We now have the following result

###### Proposition 6.3.

Under Assumptions [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance"), [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"), [5](https://arxiv.org/html/2511.04198v1#Thmassumption5 "Assumption 5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") and [6](https://arxiv.org/html/2511.04198v1#Thmassumption6 "Assumption 6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") it holds that

|  |  |  |
| --- | --- | --- |
|  | limn→∞V1,n​(τ)=V¯​(τ).\displaystyle\lim\_{n\rightarrow\infty}V^{1,n}(\tau)=\bar{V}(\tau). |  |

and if additionally Assumption [4](https://arxiv.org/html/2511.04198v1#Thmassumption4 "Assumption 4. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") holds we have that

|  |  |  |
| --- | --- | --- |
|  | limn→∞V1,n​(τ,x)=V¯​(τ,x).\displaystyle\lim\_{n\rightarrow\infty}V^{1,n}(\tau,x)=\bar{V}(\tau,x). |  |

If EE is discrete and ζ​(x)>0\zeta(x)>0, Assumption [4](https://arxiv.org/html/2511.04198v1#Thmassumption4 "Assumption 4. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") is not required.

###### Proof.

See Appendix [D](https://arxiv.org/html/2511.04198v1#A4 "Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance").
∎

This shows that we indeed have convergence of the portfolio-wide nn-individual reserves towards the mean-field reserve and of the state-wise nn-individual reserve to the state-wise mean-field reserve. Furthermore we have the following law of large numbers:

###### Proposition 6.4.

Under Assumptions [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance"), [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"), [5](https://arxiv.org/html/2511.04198v1#Thmassumption5 "Assumption 5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") and [6](https://arxiv.org/html/2511.04198v1#Thmassumption6 "Assumption 6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") it holds that

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1nP​Vℓ,n​(τ)→L2V¯​(τ).\displaystyle\frac{1}{n}\sum\_{\ell=1}^{n}PV^{\ell,n}(\tau)\stackrel{{\scriptstyle L^{2}}}{{\rightarrow}}\bar{V}(\tau). |  |

If furthermore EE is discrete and ζ​(x)>0\zeta(x)>0, then

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1n𝟙{Xτℓ,n=x}​P​Vℓ,n​(τ)1n​∑ℓ=1n𝟙{Xτℓ,n=x}→PV¯​(τ,x).\displaystyle\frac{\frac{1}{n}\sum\_{\ell=1}^{n}\mathds{1}\_{\{X\_{\tau}^{\ell,n}=x\}}PV^{\ell,n}(\tau)}{\frac{1}{n}\sum\_{\ell=1}^{n}\mathds{1}\_{\{X\_{\tau}^{\ell,n}=x\}}}\stackrel{{\scriptstyle P}}{{\rightarrow}}\bar{V}(\tau,x). |  |

###### Proof.

See Appendix [D](https://arxiv.org/html/2511.04198v1#A4 "Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance").
∎

It can be seen that the portfolio average of the present value of future payments converges to the mean-field reserve when the number of individuals tends to infinity. Thus all risk is still diversified away for large portfolios, even though the individuals are dependent. For the portfolio-wide reserve we have L2L^{2} convergence, while for the state-wise reserves we only have convergence in probability.

Now set σn2:=Var​(P​V1,n​(τ))\sigma\_{n}^{2}:=\mathrm{Var}(PV^{1,n}(\tau)) and σ2:=Var​(P​V¯​(τ))\sigma^{2}:=\mathrm{Var}(\bar{PV}(\tau)). Then under some additional assumptions we have the following central limit theorem:

###### Proposition 6.5.

Assume that Assumptions [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance"), [3](https://arxiv.org/html/2511.04198v1#Thmassumption3 "Assumption 3. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance"), [5](https://arxiv.org/html/2511.04198v1#Thmassumption5 "Assumption 5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") and [6](https://arxiv.org/html/2511.04198v1#Thmassumption6 "Assumption 6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") are satisfied. Assume further, that

|  |  |  |
| --- | --- | --- |
|  | limn→∞n​Cov​(P​V1,n​(τ),P​V2,n​(τ))=0​ and ​limn→∞n​(V1,n​(τ)−V¯​(τ))=0.\displaystyle\lim\_{n\rightarrow\infty}n\mathrm{Cov}(PV^{1,n}(\tau),PV^{2,n}(\tau))=0\text{ and }\lim\_{n\rightarrow\infty}\sqrt{n}(V^{1,n}(\tau)-\bar{V}(\tau))=0. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1nP​Vℓ,n​(τ)−V¯​(τ)σ→DN​(0,1).\displaystyle\frac{1}{\sqrt{n}}\sum\_{\ell=1}^{n}\frac{PV^{\ell,n}(\tau)-\bar{V}(\tau)}{\sigma}\stackrel{{\scriptstyle D}}{{\rightarrow}}N(0,1). |  |

###### Proof.

See Appendix [D](https://arxiv.org/html/2511.04198v1#A4 "Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance").
∎

In order for this result to hold, it is required that the convergence of the covariance between P​V1,n​(τ)PV^{1,n}(\tau) and P​V2,n​(τ)PV^{2,n}(\tau) to zero and the convergence of the reserves is sufficiently fast, meaning that the individuals should become uncorrelated sufficiently fast. These convergence speeds are very difficult to verify theoretically.

In most applications we assume that the intensity kernel μt​(x,ρ,d​y)\mu\_{t}(x,\rho,\mathrm{d}y) has a density γty​(t,x,ρ)\gamma\_{t}^{y}(t,x,\rho) with respect to some measure ν\nu on EE. In that case we would have

|  |  |  |
| --- | --- | --- |
|  | μt​(x,ρ,d​y)=γty​(x,ρ)​ν​(d​y).\displaystyle\mu\_{t}(x,\rho,\mathrm{d}y)=\gamma\_{t}^{y}(x,\rho)\nu(\mathrm{d}y). |  |

The following result states sufficient conditions for γ\gamma in order for Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") to be satisfied.

###### Proposition 6.6.

Assume that

1. (1)

   There exists Cμ>0C\_{\mu}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | ∫Eγty​(x,ρ)​ν​(d​y)≤Cμ​ and ​∫E‖y‖​γty​(x,ρ)​ν​(d​y)≤Cμ.\displaystyle\int\_{E}\gamma\_{t}^{y}(x,\rho)\nu(\mathrm{d}y)\leq C\_{\mu}\text{ and }\int\_{E}\|y\|\gamma\_{t}^{y}(x,\rho)\nu(\mathrm{d}y)\leq C\_{\mu}. |  |

   for all x∈Ex\in E and ρ∈𝒫1​(E)\rho\in\mathcal{P}^{1}(E).
2. (2)

   There exists a non-negative measurable function Cγ​(y)C\_{\gamma}(y) with
     
   ∫E‖y‖​Cγ​(y)​ν​(d​y)<∞\int\_{E}\|y\|C\_{\gamma}(y)\nu(\mathrm{d}y)<\infty such that

   |  |  |  |
   | --- | --- | --- |
   |  | |γty​(x1,ρ1)−γty​(x2,ρ2)|≤Cγ​(y)​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle|\gamma^{y}\_{t}(x\_{1},\rho\_{1})-\gamma^{y}\_{t}(x\_{2},\rho\_{2})|\leq C\_{\gamma}(y)(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

   for all x1,x2,y∈Ex\_{1},x\_{2},y\in E and ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(E).

Then Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") is satisfied.

###### Proof.

The proof is similar to the proof of Proposition [6.6](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem6 "Proposition 6.6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance").
∎

###### Example 6.7 (Life insurance during epidemics).

We now consider insurance products for an individual exposed to epidemic risk. During an epidemic the probability of one individual getting infected depends heavily on how many individuals in the entire population already are infected and thus it is important to include these collective effects. As an example we are going to look at the SIRD model, where an individual can be either Susceptible to the disease, Infected by the disease, Recovered from the disease or Dead. The state space EE of the individual can thus be set to E={1,2,3,4}E=\{1,2,3,4\} (see Figure [1](https://arxiv.org/html/2511.04198v1#S6.F1 "Figure 1 ‣ Example 6.7 (Life insurance during epidemics). ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance")).

Susceptible
11


Infected
22


Recovered
33


Dead
33

Figure 1. State space E={1,2,3,4}E=\{1,2,3,4\} for the SIRD model. The arrows represent the possible transitions.

The state of the individual can be modelled as a jump process XX with intensity kernel

|  |  |  |
| --- | --- | --- |
|  | μt​(d​y,x,ρ)=γty​(x,ρ)​ν​(d​y),\displaystyle\mu\_{t}(\mathrm{d}y,x,\rho)=\gamma\_{t}^{y}(x,\rho)\nu(\mathrm{d}y), |  |

where ν\nu is the counting measure on EE and γty​(x,ρ)\gamma\_{t}^{y}(x,\rho) are transition intiensities satisfying the conditions in Proposition [6.6](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem6 "Proposition 6.6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance"). The only non-zero transition intensities are γt2​(1,ρ)\gamma\_{t}^{2}(1,\rho), γt3​(2,ρ)\gamma\_{t}^{3}(2,\rho) and γt4​(x,ρ)\gamma\_{t}^{4}(x,\rho) for x=1,2,3x=1,2,3, as indicated by Figure [1](https://arxiv.org/html/2511.04198v1#S6.F1 "Figure 1 ‣ Example 6.7 (Life insurance during epidemics). ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance"), and we assume that only the infection intensity γt2​(1,ρ)\gamma\_{t}^{2}(1,\rho) will be measure-dependent. The others are just assumed to be bounded, measurable functions of time.

In the nn-individual model we are interested in, the infection intensity takes the form:

|  |  |  |
| --- | --- | --- |
|  | γt2​(εt−n)=β1​(t)​1n​∑ℓ=1n𝟙{Xt−ℓ,n=2},\displaystyle\gamma\_{t}^{2}(\varepsilon\_{t-}^{n})=\beta\_{1}(t)\frac{1}{n}\sum\_{\ell=1}^{n}\mathds{1}\_{\{X\_{t-}^{\ell,n}=2\}}, |  |

where β1\beta\_{1} is a bounded and measurable function. It can be seen that the infection intensity increases with the proportion of individuals out the entire population which are infected. The mean-field model is then specified by using

|  |  |  |
| --- | --- | --- |
|  | γ12​(t,η¯t)=β1​(t)​η¯t​({2}),\displaystyle\gamma\_{12}(t,\bar{\eta}\_{t})=\beta\_{1}(t)\bar{\eta}\_{t}(\{2\}), |  |

where the proportion of individuals being infected is replaced by the probability of being infected.

Now we can write that γt2​(1,ρ)=β1​(t)​f​(ρ)\gamma\_{t}^{2}(1,\rho)=\beta\_{1}(t)f(\rho) where

|  |  |  |
| --- | --- | --- |
|  | f​(ρ)=∫E𝟙{2}​(y)​ρ​(d​y)=β1​(t)​ρ​({2}),\displaystyle f(\rho)=\int\_{E}\mathds{1}\_{\{2\}}(y)\rho(\mathrm{d}y)=\beta\_{1}(t)\rho(\{2\}), |  |

By Lemma [E.4](https://arxiv.org/html/2511.04198v1#A5.Thmtheorem4 "Lemma E.4. ‣ Appendix E Auxiliary results ‣ Mean-field approximations in insurance") and Proposition [5.7](https://arxiv.org/html/2511.04198v1#S5.Thmtheorem7 "Proposition 5.7. ‣ 5. Non-life insurance applications ‣ Mean-field approximations in insurance") f​(ρ)f(\rho) is Lipschitz, which implies that γt2​(1,ρ)\gamma\_{t}^{2}(1,\rho) satisfies condition (2) of Proposition [6.6](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem6 "Proposition 6.6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance"). The boundedness of the γy​(x,ρ)\gamma^{y}(x,\rho) insures that condition (1) of Proposition [6.6](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem6 "Proposition 6.6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") is satisfied and thus we can conclude that Assumption [2](https://arxiv.org/html/2511.04198v1#Thmassumption2 "Assumption 2. ‣ 2.3. Jump destination specification ‣ 2. Jump processes ‣ Mean-field approximations in insurance") is satisfied. Since every jump has a jump size of at least 1, Assumption [5](https://arxiv.org/html/2511.04198v1#Thmassumption5 "Assumption 5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") is satisfied as well. Thus as long the initial distribution of the population is chaotic we can invoke Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") to conclude chaosticity and as long as we have a payment stream satisfying Assumption [6](https://arxiv.org/html/2511.04198v1#Thmassumption6 "Assumption 6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance"), we can invoke Proposition [6.3](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem3 "Proposition 6.3. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") to conclude that the cohort-wide reserve converges to the mean-field reserve and since the state space EE is discrete, we can conclude the same for the state-wise reserves.

An example is the insurance product discussed in [Francis&Steffensen2024] with a payment stream given by

|  |  |  |
| --- | --- | --- |
|  | Bℓ,n​(d​t)=−𝟙{Xt=1}​π​d​t+𝟙{Xt=2}​b​d​t,\displaystyle B^{\ell,n}(\mathrm{d}t)=-\mathds{1}\_{\{X\_{t}=1\}}\pi\,\mathrm{d}t+\mathds{1}\_{\{X\_{t}=2\}}b\,\mathrm{d}t, |  |

where π,b>0\pi,b>0 are constants. As long as the individual is susceptible they pay a premium and if they are infected they recieve a benefit until they recover or die. Clearly Assumption [6](https://arxiv.org/html/2511.04198v1#Thmassumption6 "Assumption 6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") is satisfied. Thus assuming that the initial distribution is chaotic, we can conclude that the mean-field model and mean-field reserves discussed in [Francis&Steffensen2024] indeed can be interpreted as approximations of the nn-individual model discussed here since both the cohort-wide and state-wise reserves of the nn-individual model converge to their mean-field counterparts.

## Acknowledgements

The author has carried out this research in association with the project frame InterAct. The author would also like to thank Christian Furrer for many fruitful discussions and his helpful comments on earlier versions of the manuscript.

## Appendix A Proof of Theorems [2.2](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and [2.7](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")

Before starting with the proofs, we will introduce some notation.

Let πt:D​([τ,T],E)→E\pi\_{t}:\amsmathbb{D}([\tau,T],E)\rightarrow E be the projection πt​(ω)=ωt\pi\_{t}(\omega)=\omega\_{t}. In the following we will work on the canoncial space (D​([τ,T],E),ℬ​(D​([τ,T],E)),F)(\amsmathbb{D}([\tau,T],E),\mathcal{B}(\amsmathbb{D}([\tau,T],E)),\amsmathbb{F}), where ℬ​(D​([τ,T],E))\mathcal{B}(\amsmathbb{D}([\tau,T],E)) is the Borel σ\sigma-algebra associated with dJ1d^{J\_{1}} and the filtration F=(ℱt)t∈[τ,T]\amsmathbb{F}=(\mathcal{F}\_{t})\_{t\in[\tau,T]} is the one generated by the projections πt\pi\_{t}. Let X∘X^{\circ} denote the canoncical process.

### A.1. Proof of Theorem [2.2](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")

Associated to equation ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) is the so-called ζ\zeta-martingale problem:

###### Definition A.1.

Let ζ∈𝒫1​(E)\zeta\in\mathcal{P}^{1}(E). The measure Q∈𝒫​(D​([τ,T],E))\amsmathbb{Q}\in\mathcal{P}(\amsmathbb{D}([\tau,T],E)) solves the ζ\zeta-martingale problem starting at ζ\zeta if πτ​(Q)=ζ\pi\_{\tau}(\amsmathbb{Q})=\zeta and for any f∈C1​(E)f\in C^{1}(E)

|  |  |  |
| --- | --- | --- |
|  | Mtf=f​(Xt∘)−f​(X0∘)−∫τt∫A(f​(Xs−∘+z)−f​(Xs−∘))​μs​(Xs−∘,d​z)​ds\displaystyle M\_{t}^{f}=f(X^{\circ}\_{t})-f(X^{\circ}\_{0})-\int\_{\tau}^{t}\int\_{A}(f(X\_{s-}^{\circ}+z)-f(X^{\circ}\_{s-}))\mu\_{s}(X\_{s-}^{\circ},\mathrm{d}z)\mathrm{d}s |  |

is a local martingale wrt. Q\amsmathbb{Q} and ℱt=σ​(πs|τ≤s≤t)\mathcal{F}\_{t}=\sigma(\pi\_{s}|\tau\leq s\leq t).

Similary equation ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) has associated the so-called xx-martingale problem to it:

###### Definition A.2.

Let x∈Ex\in E. The measure Q∈𝒫​(D​([τ,T],E))\amsmathbb{Q}\in\mathcal{P}(\amsmathbb{D}([\tau,T],E)) solves the xx-martingale problem starting at xx if Qτ=δ{x}\amsmathbb{Q}\_{\tau}=\delta\_{\{x\}} and for any f∈C1​(E)f\in C^{1}(E)

|  |  |  |
| --- | --- | --- |
|  | Mtf=f​(Xt∘)−f​(X0∘)−∫τt∫A(f​(Xs−∘+z)−f​(Xs−∘))​μs​(Xs−∘,d​z)​ds\displaystyle M\_{t}^{f}=f(X^{\circ}\_{t})-f(X^{\circ}\_{0})-\int\_{\tau}^{t}\int\_{A}(f(X^{\circ}\_{s-}+z)-f(X^{\circ}\_{s-}))\mu\_{s}(X\_{s-}^{\circ},\mathrm{d}z)\mathrm{d}s |  |

is a local martingale wrt. Q\amsmathbb{Q} and ℱt=σ​(πs|τ≤s≤t)\mathcal{F}\_{t}=\sigma(\pi\_{s}|\tau\leq s\leq t).

The martingale problems and the SDEs are connected as follows:

###### Lemma A.3.

There exists a unique weak solution to ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) if and only if there exists a unique solution to the ζ\zeta-martingale problem. There exists a unique weak solution to ([2.2](https://arxiv.org/html/2511.04198v1#S2.E2 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) if and only if there exists a unique solution to the xx-martingale problem.

###### Proof.

See [Kurtz2010] Theorem 2.3 and Corollary 2.5
∎

The next result relates the solutions of the two martingale problems with each other.

###### Lemma A.4.

The following holds:

1. (1)

   Let Q\amsmathbb{Q} be a solution to the ζ\zeta-martingale problem and let (Qx)x∈E(\amsmathbb{Q}\_{x})\_{x\in E} be a regular conditional probability for Q\amsmathbb{Q} given YY. Then for ζ\zeta-a.a. x∈Ex\in E, Qx\amsmathbb{Q}\_{x} is a solution of the xx-martingale problem.
2. (2)

   If (Qx)x∈E(\amsmathbb{Q}\_{x})\_{x\in E} are solutions for the xx-martingale problem for ζ\zeta-a.a. x∈Ex\in E, then the measure

   |  |  |  |
   | --- | --- | --- |
   |  | Q​(d​ω):=∫EQx​(d​ω)​ζ​((d)​x)\displaystyle\amsmathbb{Q}(\mathrm{d}\omega):=\int\_{E}\amsmathbb{Q}\_{x}(\mathrm{d}\omega)\zeta(\mathrm{(}d)x) |  |

   is a solution for the ζ\zeta-martingale problem.

###### Proof.

Let MtfM\_{t}^{f} be a Q\amsmathbb{Q}-martingale and let s>t≥0s>t\geq 0. Then due to disintegration and the martingale property we have for all B∈ℱtB\in\mathcal{F}\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫E∫Ω1B​(ω)​Msf​(ω)\displaystyle\int\_{E}\int\_{\Omega}1\_{B}(\omega)M\_{s}^{f}(\omega) | Qx​(d​ω)​ζ​(d​x)=∫Ω1B​(ω)​Msf​(ω)​Q​(d​ω)\displaystyle\amsmathbb{Q}\_{x}(\mathrm{d}\omega)\zeta(\mathrm{d}x)=\int\_{\Omega}1\_{B}(\omega)M\_{s}^{f}(\omega)\amsmathbb{Q}(\mathrm{d}\omega) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Ω1B​(ω)​Mtf​(ω)​Q​(d​ω)=∫E∫Ω1B​(ω)​Mtf​(ω)​Qx​(d​ω)​ζ​(d​x).\displaystyle=\int\_{\Omega}1\_{B}(\omega)M\_{t}^{f}(\omega)\amsmathbb{Q}(\mathrm{d}\omega)=\int\_{E}\int\_{\Omega}1\_{B}(\omega)M\_{t}^{f}(\omega)\amsmathbb{Q}\_{x}(\mathrm{d}\omega)\zeta(\mathrm{d}x). |  |

Due to the martingale property, we have equality between the two rows above, yielding the first claim.

On the other hand, if MtfM\_{t}^{f} is a Qx\amsmathbb{Q}\_{x}-martingale for ζ\zeta-a.a. x∈Ex\in E, we have due to the definition of Q\amsmathbb{Q}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ω1B​(ω)​Msf​(ω)​Q​(d​ω)\displaystyle\int\_{\Omega}1\_{B}(\omega)M\_{s}^{f}(\omega)\amsmathbb{Q}(\mathrm{d}\omega) | =∫E∫Ω1B​(ω)​Msf​(ω)​Qx​(d​ω)​ζ​(d​x)=\displaystyle=\int\_{E}\int\_{\Omega}1\_{B}(\omega)M\_{s}^{f}(\omega)\amsmathbb{Q}\_{x}(\mathrm{d}\omega)\zeta(\mathrm{d}x)= |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫E∫Ω1B​(ω)​Mtf​(ω)​Qx​(d​ω)​ζ​(d​x)=∫Ω1B​(ω)​Mtf​(ω)​Q​(d​ω).\displaystyle=\int\_{E}\int\_{\Omega}1\_{B}(\omega)M\_{t}^{f}(\omega)\amsmathbb{Q}\_{x}(\mathrm{d}\omega)\zeta(\mathrm{d}x)=\int\_{\Omega}1\_{B}(\omega)M\_{t}^{f}(\omega)\amsmathbb{Q}(\mathrm{d}\omega). |  |

∎

Under the assumptions of Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") both ([2.1](https://arxiv.org/html/2511.04198v1#S2.E1 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) and ([2.2](https://arxiv.org/html/2511.04198v1#S2.E2 "In 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) have unique weak solutions. Thus by Lemma [A.3](https://arxiv.org/html/2511.04198v1#A1.Thmtheorem3 "Lemma A.3. ‣ A.1. Proof of Theorem 2.2 ‣ Appendix A Proof of Theorems 2.2 and 2.7 ‣ Mean-field approximations in insurance"), the ζ\zeta-martingale problem has a unique solution and the xx-martingale problem has a unique solution for all xx. By Lemma [A.4](https://arxiv.org/html/2511.04198v1#A1.Thmtheorem4 "Lemma A.4. ‣ A.1. Proof of Theorem 2.2 ‣ Appendix A Proof of Theorems 2.2 and 2.7 ‣ Mean-field approximations in insurance") it follows that

|  |  |  |
| --- | --- | --- |
|  | Qτ,ζ​(d​ω)=∫EQτ,x​(d​ω)​ζ​(d​x)\displaystyle\amsmathbb{Q}\_{\tau,\zeta}(\mathrm{d}\omega)=\int\_{E}\amsmathbb{Q}\_{\tau,x}(\mathrm{d}\omega)\zeta(\mathrm{d}x) |  |

and thus (Qτ,x)x∈E(\amsmathbb{Q}\_{\tau,x})\_{x\in E} constitutes a regular conditional probability of Qτ,ζ\amsmathbb{Q}\_{\tau,\zeta}.

### A.2. Proof of Theorem [2.7](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")

Associated to the distribution dependent SDE ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) we have the non-linear ζ\zeta-martingale problem

###### Definition A.5.

Let ζ∈𝒫1​(E)\zeta\in\mathcal{P}^{1}(E). The measure Q¯∈𝒫​(D​([τ,T],E))\bar{\amsmathbb{Q}}\in\mathcal{P}(\amsmathbb{D}([\tau,T],E)) solves the non-linear ζ\zeta-martingale problem starting at ζ\zeta if πτ​(Q¯)=ζ\pi\_{\tau}(\bar{\amsmathbb{Q}})=\zeta and for any f∈C1​(E)f\in C^{1}(E)

|  |  |  |
| --- | --- | --- |
|  | Mtf=f​(Xt∘)−f​(X0∘)−∫τt∫A(f​(Xs−∘+z)−f​(Xs−∘))​μs​(Xs−∘,πt​(Q¯)​d​z)​ds\displaystyle M\_{t}^{f}=f(X^{\circ}\_{t})-f(X^{\circ}\_{0})-\int\_{\tau}^{t}\int\_{A}(f(X^{\circ}\_{s-}+z)-f(X^{\circ}\_{s-}))\mu\_{s}(X\_{s-}^{\circ},\pi\_{t}(\bar{\amsmathbb{Q}})\mathrm{d}z)\mathrm{d}s |  |

is a local martingale wrt. Q¯\bar{\amsmathbb{Q}} and ℱt=σ​(πs|τ≤s≤t)\mathcal{F}\_{t}=\sigma(\pi\_{s}|\tau\leq s\leq t).

Associated to the linearised SDE ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) and the non-linear ζ\zeta-martingale problem, we have the linearised xx-martingale problem:

###### Definition A.6.

Let x∈Ex\in E. Given Q¯\bar{\amsmathbb{Q}}, the measure Q∈𝒫​(D​([τ,T],E))\amsmathbb{Q}\in\mathcal{P}(\amsmathbb{D}([\tau,T],E)) solves the linearised ζ\zeta-martingale problem starting at xx if Q¯τ=ζ\bar{\amsmathbb{Q}}\_{\tau}=\zeta and for any f∈C1​(E)f\in C^{1}(E)

|  |  |  |
| --- | --- | --- |
|  | Mtf=f​(Xt∘)−f​(X0∘)−∫τt∫A(f​(Xs−∘+z)−f​(Xs−∘))​μs​(Xs−∘,πt​(Q¯)​d​z)​ds\displaystyle M\_{t}^{f}=f(X^{\circ}\_{t})-f(X^{\circ}\_{0})-\int\_{\tau}^{t}\int\_{A}(f(X^{\circ}\_{s-}+z)-f(X^{\circ}\_{s-}))\mu\_{s}(X\_{s-}^{\circ},\pi\_{t}(\bar{\amsmathbb{Q}})\mathrm{d}z)\mathrm{d}s |  |

is a local martingale wrt. Q\amsmathbb{Q} and ℱt=σ​(πs|τ≤s≤t)\mathcal{F}\_{t}=\sigma(\pi\_{s}|\tau\leq s\leq t).

Lemma [A.3](https://arxiv.org/html/2511.04198v1#A1.Thmtheorem3 "Lemma A.3. ‣ A.1. Proof of Theorem 2.2 ‣ Appendix A Proof of Theorems 2.2 and 2.7 ‣ Mean-field approximations in insurance") still applies for the link between the linearised xx-martingale problem and the linearised SDE ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), as the measure Q¯\bar{\amsmathbb{Q}} is given and fixed. For the link between the non-linear ζ\zeta-martingale problem and the distribution dependent SDE ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) we need a different result:

###### Lemma A.7.

It holds that

1. (1)

   Existence of a weak solution to ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) implies existence of a solution to the non-linear ζ\zeta-martingale problem.
2. (2)

   Under the Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") the solution of the non-linear ζ\zeta-martingale problem is unique.

###### Proof.

The first statement is a direct consequence of Ito’s formula. The second statement follows by a similar argument as in the proof of Theorem 2.1 of [Graham1992].
∎

Assuming that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") is satisfied, Theorem [2.6](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") yields existence and uniqueness of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), while Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") yields existence and uniqueness of ([2.5](https://arxiv.org/html/2511.04198v1#S2.E5 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). Thus by Lemma [A.7](https://arxiv.org/html/2511.04198v1#A1.Thmtheorem7 "Lemma A.7. ‣ A.2. Proof of Theorem 2.7 ‣ Appendix A Proof of Theorems 2.2 and 2.7 ‣ Mean-field approximations in insurance"), the non-linear ζ\zeta-martingale problem has a unique solution and the linearised xx-martingale problem has a unique solution for all xx. By Lemma [A.4](https://arxiv.org/html/2511.04198v1#A1.Thmtheorem4 "Lemma A.4. ‣ A.1. Proof of Theorem 2.2 ‣ Appendix A Proof of Theorems 2.2 and 2.7 ‣ Mean-field approximations in insurance") it follows that

|  |  |  |
| --- | --- | --- |
|  | Q¯τ,ζ​(d​ω)=∫EQ~τ,ζx​(d​ω)​ζ​(d​x)\displaystyle\bar{\amsmathbb{Q}}\_{\tau,\zeta}(\mathrm{d}\omega)=\int\_{E}\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}(\mathrm{d}\omega)\zeta(\mathrm{d}x) |  |

and thus (Q~τ,ζx)x∈E(\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x})\_{x\in E} constitutes a regular conditional probability of Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta}.

## Appendix B Proof of Theorem [2.6](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")

We start by proving the following lemma, which proves non-explosiveness.

###### Lemma B.1.

Assume that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1) holds for some q≥1q\geq 1 and that ζ∈𝒫q​(E)\zeta\in\mathcal{P}^{q}(E). Then it holds that

|  |  |  |
| --- | --- | --- |
|  | E​[supt∈[τ,T]‖X¯t‖q]≤2q−1​(E​[‖Y‖q]+Cr​E​[MTq])<∞,\displaystyle\amsmathbb{E}\bigg[\sup\_{t\in[\tau,T]}\|\bar{X}\_{t}\|^{q}\bigg]\leq 2^{q-1}(\amsmathbb{E}[\|Y\|^{q}]+C\_{r}\amsmathbb{E}[M\_{T}^{q}])<\infty, |  |

where MM is a Poisson process with constant intensity CλC\_{\lambda} and it holds that Q¯τ,ζ∈𝒫q​(D​([τ,T],E))\bar{\amsmathbb{Q}}\_{\tau,\zeta}\in\mathcal{P}^{q}(\amsmathbb{D}([\tau,T],E)) and η¯tτ,ζ∈𝒫q​(E)\bar{\eta}\_{t}^{\tau,\zeta}\in\mathcal{P}^{q}(E) for all t∈[τ,T]t\in[\tau,T].

###### Proof.

By the triangle inequality and Lemma [E.3](https://arxiv.org/html/2511.04198v1#A5.Thmtheorem3 "Lemma E.3. ‣ Appendix E Auxiliary results ‣ Mean-field approximations in insurance") we have that

|  |  |  |
| --- | --- | --- |
|  | ‖X¯t‖q≤2q−1​‖Y‖q+2q−1​N¯tq−1​∑i=1N¯t‖Z¯i‖q.\displaystyle\|\bar{X}\_{t}\|^{q}\leq 2^{q-1}\|Y\|^{q}+2^{q-1}\bar{N}\_{t}^{q-1}\sum\_{i=1}^{\bar{N}\_{t}}\|\bar{Z}\_{i}\|^{q}. |  |

As the right-hand side is increasing in tt and by the tower property we get

|  |  |  |
| --- | --- | --- |
|  | E​[supt∈[τ,T]‖X¯t‖q]≤2q−1​E​[‖Y‖q]+2q−1​E​[(N¯T)q−1​∑i=1N¯TE​[‖Z¯i‖q|N¯T]].\displaystyle\amsmathbb{E}\bigg[\sup\_{t\in[\tau,T]}\|\bar{X}\_{t}\|^{q}\bigg]\leq 2^{q-1}\amsmathbb{E}[\|Y\|^{q}]+2^{q-1}\amsmathbb{E}\bigg[(\bar{N}\_{T})^{q-1}\sum\_{i=1}^{\bar{N}\_{T}}\amsmathbb{E}[\|\bar{Z}\_{i}\|^{q}|\bar{N}\_{T}]\bigg]. |  |

The first term is finite by assumption. For the second term, using the tower property again and utilising that Z¯i\bar{Z}\_{i} is independent of N¯T\bar{N}\_{T}, given (Ti,X¯Ti−)(T\_{i},\bar{X}\_{T\_{i}-}) we obtain due to Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[‖Z¯i‖q|N¯T]\displaystyle\amsmathbb{E}[\|\bar{Z}\_{i}\|^{q}|\bar{N}\_{T}] | =E​[E​[‖Z¯i‖q|Ti,X¯Ti−]|N¯T]\displaystyle=\amsmathbb{E}[\amsmathbb{E}[\|\bar{Z}\_{i}\|^{q}|T\_{i},\bar{X}\_{T\_{i}-}]|\bar{N}\_{T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[∫A‖z‖q​rTi​(X¯Ti−,η¯Tiτ,ζ,d​z)|N¯T]≤Cr\displaystyle=\amsmathbb{E}\bigg[\int\_{A}\|z\|^{q}\,r\_{T\_{i}}(\bar{X}\_{T\_{i}-},\bar{\eta}\_{T\_{i}}^{\tau,\zeta},\mathrm{d}z)\bigg|\bar{N}\_{T}\bigg]\leq C\_{r} |  |

Thus we obtain

|  |  |  |
| --- | --- | --- |
|  | E​[supt∈[τ,T]‖X¯t‖q]≤2q−1​(E​[‖Y‖q]+Cr​E​[N¯Tq]).\displaystyle\amsmathbb{E}\bigg[\sup\_{t\in[\tau,T]}\|\bar{X}\_{t}\|^{q}\bigg]\leq 2^{q-1}(\amsmathbb{E}[\|Y\|^{q}]+C\_{r}\amsmathbb{E}[\bar{N}\_{T}^{q}]). |  |

Finally we have that N¯T\bar{N}\_{T} is dominated by a homogeneous Poisson process MM with intensity CλC\_{\lambda} in the sense of first order stochastic dominance and thus we have that

|  |  |  |
| --- | --- | --- |
|  | E​[supt∈[τ,T]‖X¯t‖q]≤2q−1​(E​[‖Y‖q]+Cr​E​[MTq])<∞,\displaystyle\amsmathbb{E}\bigg[\sup\_{t\in[\tau,T]}\|\bar{X}\_{t}\|^{q}\bigg]\leq 2^{q-1}(\amsmathbb{E}[\|Y\|^{q}]+C\_{r}\amsmathbb{E}[M\_{T}^{q}])<\infty, |  |

since a Poisson random variable has moments of all orders. The other assertions follow.
∎

This result shows that if the initial distribution has moments of order q≥1q\geq 1 and the jump size distributions have moments of order qq, then the jump process will have moments of order qq. In particular this ensures, that (η¯tτ,ζ)t∈[τ,T]⊂𝒫1​(E)(\bar{\eta}\_{t}^{\tau,\zeta})\_{t\in[\tau,T]}\subset\mathcal{P}^{1}(E). We continue by proving uniqueness.

###### Lemma B.2.

Assume that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") is satified. If there exists a weak solution of the DDSDE ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), then it is unique.

###### Proof.

Let Q¯1\bar{\amsmathbb{Q}}^{1} and Q¯2\bar{\amsmathbb{Q}}^{2} be two weak solutions of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")) and let NtN\_{t} be a Poisson process with constant intensity CλC\_{\lambda} and jump times (Ti)i∈N(T\_{i})\_{i\in\amsmathbb{N}}. Based on this Poisson process, we can construct the two Poisson random measures 𝒩1\mathcal{N}^{1} and 𝒩2\mathcal{N}^{2} given by

|  |  |  |
| --- | --- | --- |
|  | 𝒩j​(B):=∑i∈N𝟙B​(Ti,Zij),B∈ℬ​([τ,∞))⊗ℬ​(A),j=1,2\displaystyle\mathcal{N}^{j}(B):=\sum\_{i\in\amsmathbb{N}}\mathds{1}\_{B}(T\_{i},Z\_{i}^{j}),\quad B\in\mathcal{B}([\tau,\infty))\otimes\mathcal{B}(A),\quad j=1,2 |  |

where, given Ti=tT\_{i}=t and X¯t−j=x\bar{X}\_{t-}^{j}=x, the ZijZ\_{i}^{j} are chosen according to the distribution

|  |  |  |
| --- | --- | --- |
|  | κt​(x,η¯tj,d​z)=λt​(x,η¯tj)Cλ​rt​(x,η¯tj,d​z)+(1−λt​(x,η¯tj)Cλ)​δ{0}​(d​z).\displaystyle\kappa\_{t}(x,\bar{\eta}\_{t}^{j},\mathrm{d}z)=\frac{\lambda\_{t}(x,\bar{\eta}\_{t}^{j})}{C\_{\lambda}}r\_{t}(x,\bar{\eta}\_{t}^{j},\mathrm{d}z)+\bigg(1-\frac{\lambda\_{t}(x,\bar{\eta}\_{t}^{j})}{C\_{\lambda}}\bigg)\delta\_{\{0\}}(\mathrm{d}z). |  |

Moreover, we can let the joint distribution of Zi1Z\_{i}^{1} and Zi2Z\_{i}^{2} given (Ti,X¯Ti−1,X¯Ti−2)=(t,x1,x2)(T\_{i},\bar{X}\_{T\_{i}-}^{1},\bar{X}\_{T\_{i}-}^{2})=(t,x\_{1},x\_{2}) be given by the optimal coupling of κt​(x1,η¯t1,d​z)\kappa\_{t}(x\_{1},\bar{\eta}\_{t}^{1},\mathrm{d}z) and κt​(x2,η¯t2,d​z)\kappa\_{t}(x\_{2},\bar{\eta}\_{t}^{2},\mathrm{d}z). Thus it holds that

|  |  |  |
| --- | --- | --- |
|  | dW​(κTi​(Zi−11,η¯t1,d​y),κTi​(Zi−12,η¯t2,d​y))=E​[‖Zi1−Zi2‖|Ti,Zi−11,Zi−12]\displaystyle d\_{W}(\kappa\_{T\_{i}}(Z\_{i-1}^{1},\bar{\eta}\_{t}^{1},\mathrm{d}y),\kappa\_{T\_{i}}(Z\_{i-1}^{2},\bar{\eta}\_{t}^{2},\mathrm{d}y))=\amsmathbb{E}[\|Z\_{i}^{1}-Z\_{i}^{2}\||T\_{i},Z\_{i-1}^{1},Z\_{i-1}^{2}] |  |

We can now write

|  |  |  |  |
| --- | --- | --- | --- |
|  | X¯tj\displaystyle\bar{X}\_{t}^{j} | =Y+∫(τ,t]∫Az​𝒩j​(d​s,d​z),\displaystyle=Y+\int\_{(\tau,t]}\int\_{A}z\,\mathcal{N}^{j}(ds,dz), |  |

with

|  |  |  |
| --- | --- | --- |
|  | L¯j​(d​t,d​z)=Cλ​κt​(X¯t−j,η¯tj,d​z)​d​t.\displaystyle\bar{L}^{j}(\mathrm{d}t,\mathrm{d}z)=C\_{\lambda}\kappa\_{t}(\bar{X}^{j}\_{t-},\bar{\eta}\_{t}^{j},\mathrm{d}z)\mathrm{d}t. |  |

As Q¯j\bar{\amsmathbb{Q}}^{j} are assumed to exist, we can take them as given and by Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") X¯j​(P)\bar{X}^{j}(\amsmathbb{P}) exist and are unique. Furthermore due to Proposition [2.5](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") and since Qj\amsmathbb{Q}^{j} is a solution of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")), we have that X¯j​(P)=Qj\bar{X}^{j}(\amsmathbb{P})=\amsmathbb{Q}^{j}. Since the jump times of X¯1\bar{X}^{1} and X¯2\bar{X}^{2} are the same (given by (Ti)i∈N(T\_{i})\_{i\in\amsmathbb{N}}) we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | supτ≤t≤T‖X¯t1−X¯t2‖\displaystyle\sup\_{\tau\leq t\leq T}\|\bar{X}\_{t}^{1}-\bar{X}\_{t}^{2}\| | ≤∑i=1NT‖Zi1−Zi2‖\displaystyle\leq\sum\_{i=1}^{N\_{T}}\|Z\_{i}^{1}-Z\_{i}^{2}\| |  |

Taking the expectation and conditioning on NTN\_{T} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖X¯t1−X¯t2‖]≤E​[∑i=1NT‖Zi1−Zi2‖]\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|\bar{X}\_{t}^{1}-\bar{X}\_{t}^{2}\|\bigg]\leq\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}}\|Z^{1}\_{i}-Z^{2}\_{i}\|\bigg] | =E​[∑i=1NTE​[‖Zi1−Zi2‖|NT]].\displaystyle=\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}}\amsmathbb{E}[\|Z^{1}\_{i}-Z^{2}\_{i}\||N\_{T}]\bigg]. |  |

Due to Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(2) and from the definition of κ\kappa we get

|  |  |  |
| --- | --- | --- |
|  | dK​R0​(κt​(x1,ρ1,d​y),κt​(x2,ρ2,d​y))≤CL​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle d\_{KR}^{0}(\kappa\_{t}(x\_{1},\rho\_{1},\mathrm{d}y),\kappa\_{t}(x\_{2},\rho\_{2},\mathrm{d}y))\leq C\_{L}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

for x1,x2∈Ex\_{1},x\_{2}\in E and ρ1,ρ2∈𝒫q​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{q}(E), where CL=CμCλC\_{L}=\frac{C\_{\mu}}{C\_{\lambda}}.
Using this and the existence of an optimal coupling we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[‖Zi1−Zi2‖|NT]\displaystyle\amsmathbb{E}\big[\|Z^{1}\_{i}-Z^{2}\_{i}\|\big|N\_{T}\big] | =E​[E​[‖Zi1−Zi2‖|NT,Ti,X¯Ti−1,X¯Ti−2]|NT]\displaystyle=\amsmathbb{E}[\amsmathbb{E}\big[\|Z^{1}\_{i}-Z^{2}\_{i}\|\big|N\_{T},T\_{i},\bar{X}\_{T\_{i}-}^{1},\bar{X}\_{T\_{i}-}^{2}]\big|N\_{T}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E​[dK​R0​(κTi​(X¯Ti−1,η¯Ti1,d​y),κTi​(X¯Ti−2,η¯Ti2,d​y))|NT]\displaystyle=\amsmathbb{E}\big[d\_{KR}^{0}(\kappa\_{T\_{i}}(\bar{X}\_{T\_{i}-}^{1},\bar{\eta}\_{T\_{i}}^{1},\mathrm{d}y),\kappa\_{T\_{i}}(\bar{X}\_{T\_{i}-}^{2},\bar{\eta}\_{T\_{i}}^{2},\mathrm{d}y))\big|N\_{T}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E​[CL​‖X¯Ti−1−X¯Ti−2‖+CL​dW​(η¯Ti1,η¯Ti2)|NT].\displaystyle\leq\amsmathbb{E}\big[C\_{L}\|\bar{X}\_{T\_{i}-}^{1}-\bar{X}\_{T\_{i}-}^{2}\|+C\_{L}d\_{W}(\bar{\eta}\_{T\_{i}}^{1},\bar{\eta}^{2}\_{T\_{i}})\big|N\_{T}\big]. |  |

The second equality follows, since (Zi1,Zi2)(Z\_{i}^{1},Z\_{i}^{2}) are independent of NTN\_{T}, given
  
(Ti,X¯Ti−1,X¯Ti−2)(T\_{i},\bar{X}\_{T\_{i}-}^{1},\bar{X}\_{T\_{i}-}^{2}). Thus we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[∑i=1NT‖Zi1−Zi2‖]\displaystyle\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}}\|Z^{1}\_{i}-Z^{2}\_{i}\|\bigg] | ≤CL​E​[∫(τ,T]‖X¯t−1−X¯t−2‖+dW​(η¯t1,η¯t2)​N​(d​t)]\displaystyle\leq C\_{L}\amsmathbb{E}\bigg[\int\_{(\tau,T]}\|\bar{X}\_{t-}^{1}-\bar{X}\_{t-}^{2}\|+d\_{W}(\bar{\eta}\_{t}^{1},\bar{\eta}^{2}\_{t})N(\mathrm{d}t)\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Cλ​CL​∫τTE​[‖X¯t−1−X¯t−2‖]+dW​(η¯t1,η¯t2)​d​t\displaystyle=C\_{\lambda}C\_{L}\int\_{\tau}^{T}\amsmathbb{E}[\|\bar{X}\_{t-}^{1}-\bar{X}\_{t-}^{2}\|]+d\_{W}(\bar{\eta}\_{t}^{1},\bar{\eta}^{2}\_{t})\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​Cμ​∫τTE​[supτ≤s≤t‖X¯s1−X¯s2‖]​dt.\displaystyle\leq 2C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|\bar{X}\_{s}^{1}-\bar{X}\_{s}^{2}\|\bigg]\mathrm{d}t. |  |

Putting everything together yields

|  |  |  |
| --- | --- | --- |
|  | E​[supτ≤t≤T‖X¯t1−X¯t2‖]≤Cλ​2​Cμ​∫τTE​[supτ≤s≤t‖X¯s1−X¯s2‖]​dt,\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|\bar{X}\_{t}^{1}-\bar{X}\_{t}^{2}\|\bigg]\leq C\_{\lambda}2C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|\bar{X}\_{s}^{1}-\bar{X}\_{s}^{2}\|\bigg]\mathrm{d}t, |  |

which by Gronwall’s inequality yields

|  |  |  |
| --- | --- | --- |
|  | dWU​(Q¯1,Q¯2)≤E​[supτ≤t≤T‖X¯t1−X¯t2‖]=0.\displaystyle d\_{W}^{U}(\bar{\amsmathbb{Q}}^{1},\bar{\amsmathbb{Q}}^{2})\leq\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|\bar{X}\_{t}^{1}-\bar{X}\_{t}^{2}\|\bigg]=0. |  |

Thus uniqueness follows.
∎

###### Proof of Theorem [2.6](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance").

The proof of existence is based on a classical Picard-iteration scheme. Throughout the proof we fix τ\tau and ζ\zeta and we suppress the dependence on τ\tau and ζ\zeta.

Existence is proven by identifying the path-law of [2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance") as the limit of the sequence of path-laws Qn=Xn​(P)\amsmathbb{Q}^{n}=X^{n}(\amsmathbb{P}), where XnX^{n} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt0\displaystyle X\_{t}^{0} | =Y\displaystyle=Y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtn\displaystyle X\_{t}^{n} | =Y+∫(τ,t]∫Az​Qn​(d​s,d​z),n∈N,\displaystyle=Y+\int\_{(\tau,t]}\int\_{A}z\,Q^{n}(\mathrm{d}s,\mathrm{d}z),\quad n\in\amsmathbb{N}, |  |

and where

|  |  |  |
| --- | --- | --- |
|  | LQn​(d​t,d​z)=μt​(Xt−n,ηtn−1,d​z)​d​t\displaystyle L^{Q^{n}}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(X\_{t-}^{n},\eta\_{t}^{n-1},\mathrm{d}z)\mathrm{d}t |  |

Here ηtn−1:=Xtn−1​(P)\eta\_{t}^{n-1}:=X^{n-1}\_{t}(\amsmathbb{P}) and YY is random variable with distribution ζ\zeta. Note that by Lemma [B.1](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance") the measure dependence is well-defined and by Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") the corresponding path-laws Qn=Xn​(P)\amsmathbb{Q}^{n}=X^{n}(\amsmathbb{P}) exist and are unique for each n∈Nn\in\amsmathbb{N}.

Similar to the proof of Lemma [B.2](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance"), we construct a representation using Poisson random measures with the same jump times. For this let NtN\_{t} be a Poisson process with constant intensity CλC\_{\lambda} and jump times (Ti)i∈N(T\_{i})\_{i\in\amsmathbb{N}}. For each n∈Nn\in\amsmathbb{N} let 𝒩n\mathcal{N}^{n} be defined by

|  |  |  |
| --- | --- | --- |
|  | 𝒩n​(B):=∑i∈N𝟙B​(Ti,Zin),B∈ℬ​([τ,T])⊗ℬ​(A),\displaystyle\mathcal{N}^{n}(B):=\sum\_{i\in\amsmathbb{N}}\mathds{1}\_{B}(T\_{i},Z\_{i}^{n}),\quad B\in\mathcal{B}([\tau,T])\otimes\mathcal{B}(A), |  |

where ZinZ\_{i}^{n} given (Ti,XTi−n)=(t,x)(T\_{i},X\_{T\_{i}-}^{n})=(t,x) are chosen according to

|  |  |  |
| --- | --- | --- |
|  | κtn​(x,ηtn−1,d​z)=λt​(x,ηtn−1)Cλ1​rt​(x,ηtn−1,d​z)+(1−λt​(x,ηtn−1)Cλ1)​δ{0}​(d​z).\displaystyle\kappa^{n}\_{t}(x,\eta\_{t}^{n-1},\mathrm{d}z)=\frac{\lambda\_{t}(x,\eta\_{t}^{n-1})}{C\_{\lambda}^{1}}r\_{t}(x,\eta\_{t}^{n-1},\mathrm{d}z)+\bigg(1-\frac{\lambda\_{t}(x,\eta\_{t}^{n-1})}{C\_{\lambda}^{1}}\bigg)\delta\_{\{0\}}(\mathrm{d}z). |  |

The compensating measure of the 𝒩n\mathcal{N}^{n} are given by

|  |  |  |
| --- | --- | --- |
|  | L𝒩n​(d​t,d​y)=Cλ​κt​(d​z,Xt−n,ηtn−1)​d​t.\displaystyle L^{\mathcal{N}^{n}}(\mathrm{d}t,\mathrm{d}y)=C\_{\lambda}\kappa\_{t}(\mathrm{d}z,X\_{t-}^{n},\eta\_{t}^{n-1})\mathrm{d}t. |  |

Then by Proposition [2.5](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") XnX^{n} can be represented as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt0\displaystyle X\_{t}^{0} | =Y\displaystyle=Y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtn\displaystyle X\_{t}^{n} | =Y+∫(τ,t]∫Az​𝒩n​(d​s,d​z),n∈N.\displaystyle=Y+\int\_{(\tau,t]}\int\_{A}z\,\mathcal{N}^{n}(\mathrm{d}s,\mathrm{d}z),\quad n\in\amsmathbb{N}. |  |

We now show, that the sequence (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} has a limit Q∞∈𝒫1​(D​([τ,T],E))\amsmathbb{Q}^{\infty}\in\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],E)). First we show by induction, that

|  |  |  |
| --- | --- | --- |
|  | dWU​(Qn,Qn−1)≤E​[supτ≤t≤T‖Xtn−Xtn−1‖]≤Cλ​Cr​Kn​(T−τ)nn!,∀n∈N,\displaystyle d\_{W}^{U}(\amsmathbb{Q}^{n},\amsmathbb{Q}^{n-1})\leq\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{n}-X\_{t}^{n-1}\|\bigg]\leq C\_{\lambda}C\_{r}K^{n}\frac{(T-\tau)^{n}}{n!},\quad\forall n\in\amsmathbb{N}, |  |

for any fixed T≥τT\geq\tau, where K=Cμ​eCμ​(T−τ)K=C\_{\mu}e^{C\_{\mu}(T-\tau)}. By using Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖Xt1−Xt0‖]\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{1}-X\_{t}^{0}\|\bigg] | ≤Cλ​Cr​(T−τ).\displaystyle\leq C\_{\lambda}C\_{r}(T-\tau). |  |

Note that this bound holds for any fixed T≥τT\geq\tau.
Now assume that the result holds for some n>1n>1. As in the proof of Lemma [B.2](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance"), we can utilise that the jump times of the processes are the same, to arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | E[supτ≤t≤T∥Xtn+1\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{n+1} | −Xtn∥]≤E[∑i=1NT∥Zin+1−Zin∥].\displaystyle-X\_{t}^{n}\|\bigg]\leq\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}}\|Z^{n+1}\_{i}-Z^{n}\_{i}\|\bigg]. |  |

Due to Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(2) and from the definition of κ\kappa we get

|  |  |  |
| --- | --- | --- |
|  | dK​R0​(κt​(x1,ρ1,d​z),κt​(x2,ρ2,d​z))≤CL​(‖x1−x2‖+dW​(ρ1,ρ2))\displaystyle d\_{KR}^{0}(\kappa\_{t}(x\_{1},\rho\_{1},\mathrm{d}z),\kappa\_{t}(x\_{2},\rho\_{2},\mathrm{d}z))\leq C\_{L}(\|x\_{1}-x\_{2}\|+d\_{W}(\rho\_{1},\rho\_{2})) |  |

for x1,x2∈Ex\_{1},x\_{2}\in E and ρ1,ρ2∈𝒫1​(E)\rho\_{1},\rho\_{2}\in\mathcal{P}^{1}(E), where CL=CμCλC\_{L}=\frac{C\_{\mu}}{C\_{\lambda}}.
Again using this and the fact that the marks may be chosen in accordance with an optimal coupling, similar calculations as in the proof of Lemma [B.2](https://arxiv.org/html/2511.04198v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Proof of Theorem 2.6 ‣ Mean-field approximations in insurance") yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | E[∑i=1NT∥Zin+1\displaystyle\amsmathbb{E}\bigg[\sum\_{i=1}^{N\_{T}}\|Z^{n+1}\_{i} | −Zin∥]\displaystyle-Z^{n}\_{i}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cμ​∫τTE​[supτ≤s≤t‖Xsn+1−Xsn‖]+E​[supτ≤s≤t‖Xsn−Xsn−1‖]​d​t.\displaystyle\leq C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{n+1}-X\_{s}^{n}\|\bigg]+\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{n}-X\_{s}^{n-1}\|\bigg]\mathrm{d}t. |  |

Now using the induction assumption yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[supτ≤t≤T‖Xtn+1−Xtn‖]≤\displaystyle\amsmathbb{E}\bigg[\sup\_{\tau\leq t\leq T}\|X\_{t}^{n+1}-X\_{t}^{n}\|\bigg]\leq | Cμ​∫τTE​[supτ≤s≤t‖Xsn+1−Xsn‖]\displaystyle C\_{\mu}\int\_{\tau}^{T}\amsmathbb{E}\bigg[\sup\_{\tau\leq s\leq t}\|X\_{s}^{n+1}-X\_{s}^{n}\|\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Cμ​Kn−1​(T−τ)n+1(n+1)!\displaystyle+C\_{\mu}K^{n-1}\frac{(T-\tau)^{n+1}}{(n+1)!} |  |

An application of Gronwall’s inequality yields the desired result. Let m∈Nm\in\amsmathbb{N}. Using this result, we can conclude that

|  |  |  |
| --- | --- | --- |
|  | dWU​(Qn+m,Qn)≤m​Cλ​Cr​Kn​(T−τ)nn!,\displaystyle d\_{W}^{U}(\amsmathbb{Q}^{n+m},\amsmathbb{Q}^{n})\leq mC\_{\lambda}C\_{r}K^{n}\frac{(T-\tau)^{n}}{n!}, |  |

which can become arbitrarily small for nn large. Thus (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} is a Cauchy sequence in the space (𝒫1​(D​([τ,T],E)),dWU)(\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],E)),d\_{W}^{U}). As the space (D​([τ,T],E),dU)(\amsmathbb{D}([\tau,T],E),d^{U}) is complete, but not separable we cannot conclude that (𝒫1​(D​([τ,T],E)),dWU)(\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],E)),d\_{W}^{U}) is complete as well and hence we cannot directly conclude that (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} has a limit in (𝒫1​(D​([τ,T],E)),dWU)(\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],E)),d\_{W}^{U}). Luckily the space (𝒫1​(D​([τ,T],E)),dWJ1)(\mathcal{P}^{1}(\amsmathbb{D}([\tau,T],E)),d\_{W}^{J\_{1}}) is complete and since the metric dWUd\_{W}^{U} is stronger than dWJ1d\_{W}^{J\_{1}}, the sequence (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} is Cauchy for dWJ1d\_{W}^{J\_{1}} as well. Thus (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} converges towards a limit Q∞\amsmathbb{Q}^{\infty}, when using dJ1d^{J\_{1}}.

It remains to show that Q∞\amsmathbb{Q}^{\infty} is actually a path-law of ([2.4](https://arxiv.org/html/2511.04198v1#S2.E4 "In 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")). For this we construct the process

|  |  |  |
| --- | --- | --- |
|  | Xt∞=Y+∫(τ,T)×Az​Q∞​(d​t,d​z),\displaystyle X\_{t}^{\infty}=Y+\int\_{(\tau,T)\times A}z\,Q^{\infty}(\mathrm{d}t,\mathrm{d}z), |  |

with

|  |  |  |
| --- | --- | --- |
|  | LQ∞​(d​t,d​z)=μt​(Xt−∞,Qt∞,d​z)​d​t.\displaystyle L^{Q^{\infty}}(\mathrm{d}t,\mathrm{d}z)=\mu\_{t}(X\_{t-}^{\infty},\amsmathbb{Q}^{\infty}\_{t},\mathrm{d}z)\mathrm{d}t. |  |

This process exists by Theorem [2.1](https://arxiv.org/html/2511.04198v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1. Jump processes ‣ 2. Jump processes ‣ Mean-field approximations in insurance") as for all the XnX^{n} we can find a Poisson representation with the same jump times (Ti)i∈N(T\_{i})\_{i\in\amsmathbb{N}}. By a similar induction argument, it can then be shown that

|  |  |  |
| --- | --- | --- |
|  | dWU​(Qn,X∞​(P))≤Cλ​Cr​T​(Cμ​T​eCμ​T)n.\displaystyle d\_{W}^{U}(\amsmathbb{Q}^{n},X^{\infty}(\amsmathbb{P}))\leq C\_{\lambda}C\_{r}T(C\_{\mu}Te^{C\_{\mu}T})^{n}. |  |

For T∗T^{\*} such that Cμ​T​eCμ​T<1C\_{\mu}Te^{C\_{\mu}T}<1 we obtain

|  |  |  |
| --- | --- | --- |
|  | limn→∞dWU​(Qn,X∞​(P))≤limn→∞Cλ​Cr​T∗​(Cμ​T∗​eCμ​T∗)n=0.\displaystyle\lim\_{n\rightarrow\infty}d\_{W}^{U}(\amsmathbb{Q}^{n},X^{\infty}(\amsmathbb{P}))\leq\lim\_{n\rightarrow\infty}C\_{\lambda}C\_{r}T^{\*}(C\_{\mu}T^{\*}e^{C\_{\mu}T^{\*}})^{n}=0. |  |

Thus on [0,T∗][0,T^{\*}] we have that X∞​(P)X^{\infty}(\amsmathbb{P}) is a limit of the sequence (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}}, which means that X∞​(P)=Q∞X^{\infty}(\amsmathbb{P})=\amsmathbb{Q}^{\infty}. As there are no point masses in the distribution of jump times, we can take XT∗∞​(P)X\_{T^{\*}}^{\infty}(\amsmathbb{P}) as initial distribution at time τ=T∗\tau=T^{\*}. Repeating the argument yields then X∞​(P)=Q∞X^{\infty}(\amsmathbb{P})=\amsmathbb{Q}^{\infty} for [T∗,2​T∗][T^{\*},2T^{\*}]. The procedure can be repeated and thus yields existence on all of [0,T][0,T].
∎

## Appendix C LLN and CLT for chaotic random variables

Let (S,ds)(S,d\_{s}) be a Polish space and let (Ω,ℱ,P)(\Omega,\mathcal{F},\amsmathbb{P}) be a probability space. Consider the triangular array ((X1,n,…,Xn,n))n∈N((X^{1,n},\ldots,X^{n,n}))\_{n\in\amsmathbb{N}} of random variables Xℓ,n:Ω→SX^{\ell,n}:\Omega\rightarrow S, where each row Xn=(X1,n,…,Xn,n)X^{n}=(X^{1,n},\ldots,X^{n,n}) has distribution Xn​(P)=Qn∈𝒫​(S)X^{n}(\amsmathbb{P})=\amsmathbb{Q}^{n}\in\mathcal{P}(S). Furthermore let X:Ω→SX:\Omega\rightarrow S be a random variable with X​(P)=Q∈𝒫​(S)X(\amsmathbb{P})=\amsmathbb{Q}\in\mathcal{P}(S).

###### Proposition C.1.

Assume that (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} is Q\amsmathbb{Q}-chaotic and that f:S→Rf:S\rightarrow\amsmathbb{R} is Q\amsmathbb{Q}-a.s. continuous. Then

|  |  |  |
| --- | --- | --- |
|  | f​(Xℓ,n)​(P)→wk.f​(X)​(P)​ for ​n→∞.\displaystyle f(X^{\ell,n})(\amsmathbb{P})\stackrel{{\scriptstyle wk.}}{{\rightarrow}}f(X)(\amsmathbb{P})\text{ for }n\rightarrow\infty. |  |

If furthermore the sequence (f​(X1,n))n∈N(f(X^{1,n}))\_{n\in\amsmathbb{N}} is uniformly integrable, then we have that

|  |  |  |
| --- | --- | --- |
|  | E​[f​(Xℓ,n)]→E​[f​(X)]​ for ​n→∞.\displaystyle\amsmathbb{E}[f(X^{\ell,n})]\rightarrow\amsmathbb{E}[f(X)]\text{ for }n\rightarrow\infty. |  |

###### Proof.

Due to chaosticity we have that Xℓ,n​(P)=Qn,1→wk.Q=X​(P)X^{\ell,n}(\amsmathbb{P})=\amsmathbb{Q}^{n,1}\stackrel{{\scriptstyle wk.}}{{\rightarrow}}\amsmathbb{Q}=X(\amsmathbb{P}). The first result follows directly from 3.8 on p.348 in [Jacod&Shiryaev2003], while the second result follows from Theorem 3.5 in [Billingsley1999].
∎

The next result is a law of large numbers:

###### Proposition C.2.

Assume that (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} is Q\amsmathbb{Q}-chaotic and let f:S→Rf:S\rightarrow\amsmathbb{R} be Q\amsmathbb{Q}-a.s. continuous with

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[|f​(X1,n)|2+ε]<∞,for some ​ε>0\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[|f(X^{1,n})|^{2+\varepsilon}]<\infty,\quad\text{for some }\varepsilon>0 |  |

Then it holds that

|  |  |  |
| --- | --- | --- |
|  | limn→∞E​[(1n​∑ℓ=1nf​(Xℓ,n)−E​[f​(X)])2]=0.\displaystyle\lim\_{n\rightarrow\infty}\amsmathbb{E}\bigg[\bigg(\frac{1}{n}\sum\_{\ell=1}^{n}f(X^{\ell,n})-\amsmathbb{E}[f(X)]\bigg)^{2}\bigg]=0. |  |

###### Proof.

The proof is based on part of the proof of Theorem 3.2 in [Gottlieb1998]. Set μ:=E​[f​(X)]\mu:=\amsmathbb{E}[f(X)].

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(1n​∑ℓ=1nf​(Xℓ,n)−μ)2]\displaystyle\amsmathbb{E}\bigg[\bigg(\frac{1}{n}\sum\_{\ell=1}^{n}f(X^{\ell,n})-\mu\bigg)^{2}\bigg] | =1n2​∑i,j=1nE​[(f​(Xi,n)−μ)​(f​(Xj,n)−μ)]\displaystyle=\frac{1}{n^{2}}\sum\_{i,j=1}^{n}\amsmathbb{E}[(f(X^{i,n})-\mu)(f(X^{j,n})-\mu)] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n​E​[(f​(X1,n)−μ)2]\displaystyle=\frac{1}{n}\amsmathbb{E}[(f(X^{1,n})-\mu)^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +n−1n​E​[(f​(X1,n)−μ)​(f​(X2,n)−μ)],\displaystyle+\frac{n-1}{n}\amsmathbb{E}[(f(X^{1,n})-\mu)(f(X^{2,n})-\mu)], |  |

The last equality is due the fact that all individuals are identically distributed. Our assumptions, Lemma [E.3](https://arxiv.org/html/2511.04198v1#A5.Thmtheorem3 "Lemma E.3. ‣ Appendix E Auxiliary results ‣ Mean-field approximations in insurance") and (3.18) on p. 31 of [Billingsley1999] imply that (f​(X1,n)−μ)2(f(X^{1,n})-\mu)^{2} and (f​(X1,n)−μ)​(f​(X2,n)−μ)(f(X^{1,n})-\mu)(f(X^{2,n})-\mu) are uniformly integrable sequences. Thus by Definition [3.1](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") and Theorem 3.5 of [Billingsley1999], it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞1n​E​[(f​(X1,n)−μ)2]\displaystyle\lim\_{n\rightarrow\infty}\frac{1}{n}\amsmathbb{E}[(f(X^{1,n})-\mu)^{2}] | =(limn→∞1n)(limn→∞E[(f(X1,n)−μ)2]\displaystyle=\bigg(\lim\_{n\rightarrow\infty}\frac{1}{n}\bigg)\bigg(\lim\_{n\rightarrow\infty}\amsmathbb{E}[(f(X^{1,n})-\mu)^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =0⋅E​[(f​(X)−μ)2]=0\displaystyle=0\cdot\amsmathbb{E}[(f(X)-\mu)^{2}]=0 |  |

and

|  |  |  |
| --- | --- | --- |
|  | limn→∞E​[(f​(X1,n)−μ)​(f​(X2,n)−μ)]=2​(E​[f​(X)]−μ)=0.\displaystyle\lim\_{n\rightarrow\infty}\amsmathbb{E}[(f(X^{1,n})-\mu)(f(X^{2,n})-\mu)]=2(\amsmathbb{E}[f(X)]-\mu)=0. |  |

The result follows.
∎

Now set μn:=E[f(X1,n]\mu\_{n}:=\amsmathbb{E}[f(X^{1,n}] and σn2:=E​[(f​(X1,n)−μ)2]\sigma^{2}\_{n}:=\amsmathbb{E}[(f(X^{1,n})-\mu)^{2}] and similarly set μ:=E​[f​(X)]\mu:=\amsmathbb{E}[f(X)] and σ2:=E​[(f​(X)−μ)2]\sigma^{2}:=\amsmathbb{E}[(f(X)-\mu)^{2}]. It is also possible (under additional assumptions) to derive a central limit theorem.

###### Proposition C.3.

Assume that (Qn)n∈N(\amsmathbb{Q}^{n})\_{n\in\amsmathbb{N}} is Q\amsmathbb{Q}-chaotic and that

|  |  |  |
| --- | --- | --- |
|  | limn→∞n​E​[(f​(X1,n)−μn)​(f​(X2,n)−μn)]=0.\displaystyle\lim\_{n\rightarrow\infty}n\amsmathbb{E}[(f(X^{1,n})-\mu\_{n})(f(X^{2,n})-\mu\_{n})]=0. |  |

Let f:S→Rf:S\rightarrow\amsmathbb{R} be Q\amsmathbb{Q}-a.s. continuous with

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[|f​(X1,n)|4+ε]<∞,for some ​ε>0\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[|f(X^{1,n})|^{4+\varepsilon}]<\infty,\quad\text{for some }\varepsilon>0 |  |

Then

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1nf​(Xi,n)−μnσn→DN​(0,1).\displaystyle\frac{1}{\sqrt{n}}\sum\_{i=1}^{n}\frac{f(X^{i,n})-\mu\_{n}}{\sigma\_{n}}\stackrel{{\scriptstyle D}}{{\rightarrow}}N\big(0,1\big). |  |

If furthermore limn→∞n​(μn−μ)=0\lim\_{n\rightarrow\infty}\sqrt{n}(\mu\_{n}-\mu)=0, then

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1nf​(Xi,n)−μσ→DN​(0,1).\displaystyle\frac{1}{\sqrt{n}}\sum\_{i=1}^{n}\frac{f(X^{i,n})-\mu}{\sigma}\stackrel{{\scriptstyle D}}{{\rightarrow}}N(0,1). |  |

###### Proof.

Since {Xℓ,n;ℓ=1,2,…}n∈N\{X^{\ell,n};\ell=1,2,\ldots\}\_{n\in\amsmathbb{N}} are exchangeable and so is {f(Xℓ,n);ℓ=1,2,…}n∈N\{f(X^{\ell,n});\ell=1,2,\ldots\}\_{n\in\amsmathbb{N}}. Therefore we would like to apply a CLT for exchangeable processes (see Theorem 2 in [BlumEtAl1958]).

The first step is now to prove the following three equalities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞μn\displaystyle\lim\_{n\rightarrow\infty}\mu\_{n} | =limn→∞E[f(X1,n)]=E[f(X)]=:μ\displaystyle=\lim\_{n\rightarrow\infty}\amsmathbb{E}[f(X^{1,n})]=\amsmathbb{E}[f(X)]=:\mu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞σn\displaystyle\lim\_{n\rightarrow\infty}\sigma\_{n} | =limn→∞E[(f(X1,n)−μn)2]=E[(f(X)−μ)2]=:σ\displaystyle=\lim\_{n\rightarrow\infty}\amsmathbb{E}[(f(X^{1,n})-\mu\_{n})^{2}]=\amsmathbb{E}[(f(X)-\mu)^{2}]=:\sigma |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞ρn\displaystyle\lim\_{n\rightarrow\infty}\rho\_{n} | =limn→∞E​[f​(X1,n)​f​(X2,n)]=E​[f​(X)]2=μ2.\displaystyle=\lim\_{n\rightarrow\infty}\amsmathbb{E}[f(X^{1,n})f(X^{2,n})]=\amsmathbb{E}[f(X)]^{2}=\mu^{2}. |  |

Due to our Assumptions, Lemma [E.3](https://arxiv.org/html/2511.04198v1#A5.Thmtheorem3 "Lemma E.3. ‣ Appendix E Auxiliary results ‣ Mean-field approximations in insurance") and (3.18) on p. 31 of [Billingsley1999] all involved sequences are uniformly integrable. Thus all three identities are implied by chaosticity and Theorem 3.5 of [Billingsley1999].
Using the same argument and the three identities it follows that

|  |  |  |
| --- | --- | --- |
|  | limn→∞E​[(f​(X1,n)−μnσn)2​(f​(X2,n)−μnσn)2]=1σ4​E​[(f​(X)−μ)2]2=1.\displaystyle\lim\_{n\rightarrow\infty}\amsmathbb{E}\bigg[\bigg(\frac{f(X^{1,n})-\mu\_{n}}{\sigma\_{n}}\bigg)^{2}\bigg(\frac{f(X^{2,n})-\mu\_{n}}{\sigma\_{n}}\bigg)^{2}\bigg]=\frac{1}{\sigma^{4}}\amsmathbb{E}[(f(X)-\mu)^{2}]^{2}=1. |  |

So condition (2) of Theorem 2 in [BlumEtAl1958] is satisfied.

A similar argument yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞E​[|f​(X1,n)−μnσn|3]\displaystyle\lim\_{n\rightarrow\infty}\amsmathbb{E}\bigg[\bigg|\frac{f(X^{1,n})-\mu\_{n}}{\sigma\_{n}}\bigg|^{3}\bigg] | =1σ3​E​[(f​(X)−μ)3]<∞,\displaystyle=\frac{1}{\sigma^{3}}\amsmathbb{E}[(f(X)-\mu)^{3}]<\infty, |  |

and therefore condition (3) of Theorem 2 in [BlumEtAl1958] is satisfied. Finally we have that

|  |  |  |
| --- | --- | --- |
|  | limn→∞E​[(f​(X1,n)−μnσn)​(f​(X2,n)−μnσn)]=1σ2​(E​[(f​(X)−μ)])2=0.\displaystyle\lim\_{n\rightarrow\infty}\amsmathbb{E}\bigg[\bigg(\frac{f(X^{1,n})-\mu\_{n}}{\sigma\_{n}}\bigg)\bigg(\frac{f(X^{2,n})-\mu\_{n}}{\sigma\_{n}}\bigg)\bigg]=\frac{1}{\sigma^{2}}\big(\amsmathbb{E}[(f(X)-\mu)]\big)^{2}=0. |  |

This shows that we have the right convergence, which is required for condition (1) of Theorem 2 in [BlumEtAl1958], but not necessarily the required convergence speed. Therefore we had to assume this in addition to the chaosticity assumption. Now all conditions of Theorem 2 in [BlumEtAl1958] are satisfied and thus we obtain

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1nf​(Xℓ,n)−μnσn→DN​(0,1).\displaystyle\frac{1}{\sqrt{n}}\sum\_{\ell=1}^{n}\frac{f(X^{\ell,n})-\mu\_{n}}{\sigma\_{n}}\stackrel{{\scriptstyle D}}{{\rightarrow}}N\big(0,1\big). |  |

Furthermore as limn→∞μn=μ\lim\_{n\rightarrow\infty}\mu\_{n}=\mu and limn→∞σn=σ\lim\_{n\rightarrow\infty}\sigma\_{n}=\sigma and since we have assumed that limn→∞n​(μn−μ)=0\lim\_{n\rightarrow\infty}\sqrt{n}(\mu\_{n}-\mu)=0, an application of Slutsky’s Lemma yields

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1nf​(Xℓ,n)−μσ=σnσ​(∑ℓ=1nf​(Xℓ,n)−μnσn)+n​(μn−μ)σ→DN​(0,1).\displaystyle\frac{1}{\sqrt{n}}\sum\_{\ell=1}^{n}\frac{f(X^{\ell,n})-\mu}{\sigma}=\frac{\sigma\_{n}}{\sigma}\bigg(\sum\_{\ell=1}^{n}\frac{f(X^{\ell,n})-\mu\_{n}}{\sigma\_{n}}\bigg)+\frac{\sqrt{n}(\mu\_{n}-\mu)}{\sigma}\stackrel{{\scriptstyle D}}{{\rightarrow}}N(0,1). |  |

∎

## Appendix D Proof of Propositions [6.3](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem3 "Proposition 6.3. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance"), [6.4](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem4 "Proposition 6.4. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") and [6.5](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem5 "Proposition 6.5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance")

Let H​([τ,T],E)⊂D​([τ,T],E)\amsmathbb{H}([\tau,T],E)\subset\amsmathbb{D}([\tau,T],E) be the space of all jump process paths the form

|  |  |  |
| --- | --- | --- |
|  | ωt:=y+∑i=1mzi​𝟙[ti,T]​(t),\displaystyle\omega\_{t}:=y+\sum\_{i=1}^{m}z\_{i}\mathds{1}\_{[t\_{i},T]}(t), |  |

where yy is the initial value, τ<t1<…<tm<T\tau<t\_{1}<\ldots<t\_{m}<T for m∈N∪{0}m\in\amsmathbb{N}\cup\{0\} are the jump times and (zi)i=1,…,m⊂E(z\_{i})\_{i=1,\ldots,m}\subset E are the jump sizes. Let J​(ω):={t1,…,tm}J(\omega):=\{t\_{1},\ldots,t\_{m}\} denote the set of jump times with m=0m=0 meaning J​(ω)=∅J(\omega)=\emptyset.

In order to prove the results, it is convenient to view the present value of discounted future payments as a function of a jump process path into the real numbers. That is P​V1,n=f​(X1,n)PV^{1,n}=f(X^{1,n}), where f:H​([τ,T],E)→Rf:\amsmathbb{H}([\tau,T],E)\rightarrow\amsmathbb{R} is given by

|  |  |  |
| --- | --- | --- |
|  | f​(ω)=∫τTb​(t,ωt)​dt+∑t∈J​(ω)bωt​(t,ωt−,Δ​ωt).\displaystyle f(\omega)=\int\_{\tau}^{T}b(t,\omega\_{t})\mathrm{d}t+\sum\_{t\in J(\omega)}b^{\omega\_{t}}(t,\omega\_{t-},\Delta\omega\_{t}). |  |

Using this, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | V1,n​(τ)=∫D​([τ,T],E)f​(ω)​Qτ,ζn,1​(d​ω)\displaystyle V^{1,n}(\tau)=\int\_{\amsmathbb{D}([\tau,T],E)}f(\omega)\amsmathbb{Q}^{n,1}\_{\tau,\zeta}(\mathrm{d}\omega) | ,V¯(τ)=∫D​([τ,T],E)f(ω)Q¯τ,ζ(dω),\displaystyle,\quad\bar{V}(\tau)=\int\_{\amsmathbb{D}([\tau,T],E)}f(\omega)\bar{\amsmathbb{Q}}\_{\tau,\zeta}(\mathrm{d}\omega), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V1,n​(τ,x)=∫D​([τ,T],E)f​(ω)​Qτ,ρ​(x)n,1​(d​ω)\displaystyle V^{1,n}(\tau,x)=\int\_{\amsmathbb{D}([\tau,T],E)}f(\omega)\amsmathbb{Q}^{n,1}\_{\tau,\rho(x)}(\mathrm{d}\omega) | ,V¯(τ,x)=∫D​([τ,T],E)f(ω)Q~τ,ζx(dω)\displaystyle,\quad\bar{V}(\tau,x)=\int\_{\amsmathbb{D}([\tau,T],E)}f(\omega)\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}(\mathrm{d}\omega) |  |

and the results then follow from Proposition [C.1](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") and Proposition [C.2](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem2 "Proposition C.2. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") if ff is Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta} (or Q~τ,ζx\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x})-a.s. continuous. As we have Q¯τ,ζ​(H​([τ,T],E))=Q~τ,ζx​(H​([τ,T],E))=1\bar{\amsmathbb{Q}}\_{\tau,\zeta}(\amsmathbb{H}([\tau,T],E))=\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}(\amsmathbb{H}([\tau,T],E))=1, we only have to prove continuity of ff on H​([τ,T],E)\amsmathbb{H}([\tau,T],E). We do this in two parts.

###### Lemma D.1.

Let f:H​([τ,T],E)→Rf:\amsmathbb{H}([\tau,T],E)\rightarrow\amsmathbb{R} be given by

|  |  |  |
| --- | --- | --- |
|  | f​(ω)=∫τTb​(t,ωt)​𝑑t,\displaystyle f(\omega)=\int\_{\tau}^{T}b(t,\omega\_{t})dt, |  |

where b:[τ,T]×E→Rb:[\tau,T]\times\amsmathbb{E}\rightarrow\amsmathbb{R} is bounded and t↦b​(t,y)t\mapsto b(t,y) has a countable number of discontinuity points for each fixed y∈Ey\in E. Then ff is bounded and continuous.

###### Proof.

Let ω∈H​([τ,T],E)\omega\in\amsmathbb{H}([\tau,T],E) and let (ωn)n∈N⊂H​([τ,T],E)(\omega^{n})\_{n\in\amsmathbb{N}}\subset\amsmathbb{H}([\tau,T],E) be sequence such that limn→∞dJ1​(ωn,ω)=0\lim\_{n\rightarrow\infty}d^{J\_{1}}(\omega^{n},\omega)=0. The goal is to show

|  |  |  |
| --- | --- | --- |
|  | limn→∞∫[τ,T]b​(t,ωtn)​dt=∫[τ,T]b​(t,ωt)​dt.\displaystyle\lim\_{n\rightarrow\infty}\int\_{[\tau,T]}b(t,\omega^{n}\_{t})\mathrm{d}t=\int\_{[\tau,T]}b(t,\omega\_{t})\mathrm{d}t. |  |

The Skorokhod convergence implies ωtn→ωt\omega^{n}\_{t}\rightarrow\omega\_{t} for all continuity points t∈[τ,T]∖J​(ω)t\in[\tau,T]\setminus J(\omega) of ω\omega, where J​(ω)J(\omega) denotes the points of discontinuity. Furthermore, the set of discontinuity points of the function t↦b​(t,y)t\mapsto b(t,y), denoted by Jy​(b)J\_{y}(b), is assumed to be countable for any y∈Ey\in E, and thus of Lebesgue measure zero. Set now

|  |  |  |
| --- | --- | --- |
|  | A:=J​(ω)∪⋃t∈J​(ω)Jωt​(b).\displaystyle A:=J(\omega)\cup\bigcup\_{t\in J(\omega)}J\_{\omega\_{t}}(b). |  |

As AA is a finite union of Lebesgue null sets, it is a Lebesgue null set itself. Thus all points, where the necessary convergence can go wrong, can be excluded from the integral. By dominated convergence, we thus get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞f​(ωn)\displaystyle\lim\_{n\rightarrow\infty}f(\omega^{n}) | =limn→∞∫[τ,T]∖Ab​(t,ωtn)​dt=∫[τ,T]∖Alimn→∞b​(t,ωtn)​d​t\displaystyle=\lim\_{n\rightarrow\infty}\int\_{[\tau,T]\setminus A}b(t,\omega^{n}\_{t})\mathrm{d}t=\int\_{[\tau,T]\setminus A}\lim\_{n\rightarrow\infty}b(t,\omega^{n}\_{t})\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫[τ,T]∖Ab​(t,ωt)​dt=∫[τ,T]b​(t,ωt)​dt=f​(ω).\displaystyle=\int\_{[\tau,T]\setminus A}b(t,\omega\_{t})\mathrm{d}t=\int\_{[\tau,T]}b(t,\omega\_{t})\mathrm{d}t=f(\omega). |  |

This proves the desired result.
∎

For any ω∈H​([τ,T],E)\omega\in\amsmathbb{H}([\tau,T],E) the set of absolute jump sizes is given by U​(ω)={‖z1‖,…,‖zm‖}U(\omega)=\{\|z\_{1}\|,\ldots,\|z\_{m}\|\}. Now for any ε>0\varepsilon>0 and ε∉U​(ω)\varepsilon\notin U(\omega) one can define the following sequence of jump times

|  |  |  |  |
| --- | --- | --- | --- |
|  | t0ε​(ω)\displaystyle t\_{0}^{\varepsilon}(\omega) | :=0\displaystyle:=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | tiε​(ω)\displaystyle t\_{i}^{\varepsilon}(\omega) | :=inf{t>ti−1ε​(ω):‖Δ​ωt‖>ε},\displaystyle:=\inf\{t>t\_{i-1}^{\varepsilon}(\omega):\|\Delta\omega\_{t}\|>\varepsilon\}, |  |

with convention inf∅=∞\inf\emptyset=\infty. Set Jε​(ω):={tiε​(ω):tiε​(ω)<∞}J^{\varepsilon}(\omega):=\{t\_{i}^{\varepsilon}(\omega):t\_{i}^{\varepsilon}(\omega)<\infty\}. Note that Jε​(ω)⊆J​(ω)J^{\varepsilon}(\omega)\subseteq J(\omega), where J​(ω)={t1,…,tm}J(\omega)=\{t\_{1},\ldots,t\_{m}\} is finite.

###### Lemma D.2.

Let fε:H​([τ,T],E)→Rf^{\varepsilon}:\amsmathbb{H}([\tau,T],E)\rightarrow\amsmathbb{R} be given by

|  |  |  |
| --- | --- | --- |
|  | fε​(ω)=∑t∈Jε​(ω)bωt​(t,ωt−,Δ​ωt),\displaystyle f^{\varepsilon}(\omega)=\sum\_{t\in J^{\varepsilon(\omega)}}b^{\omega\_{t}}(t,\omega\_{t-},\Delta\omega\_{t}), |  |

and let f:H​([τ,T],E)→Rf:\amsmathbb{H}([\tau,T],E)\rightarrow\amsmathbb{R} be given by

|  |  |  |
| --- | --- | --- |
|  | f​(ω)=∑t∈J​(ω)bωt​(t,ωt−,Δ​ωt).\displaystyle f(\omega)=\sum\_{t\in J(\omega)}b^{\omega\_{t}}(t,\omega\_{t-},\Delta\omega\_{t}). |  |

where b:[τ,T]×E3→Rb:[\tau,T]\times E^{3}\rightarrow\amsmathbb{R} is bounded and continuous. Then fεf^{\varepsilon} is continuous on H​([τ,T],E)\amsmathbb{H}([\tau,T],E), while ff is continuous on the set

|  |  |  |
| --- | --- | --- |
|  | {ω∈H​([τ,T],E)|‖Δ​ωt‖>ε,∀t∈[τ,T]}.\displaystyle\{\omega\in\amsmathbb{H}([\tau,T],E)|\|\Delta\omega\_{t}\|>\varepsilon,\,\forall t\in[\tau,T]\}. |  |

for any ε>0\varepsilon>0.

###### Proof.

By Proposition 2.7 on p.339 in [Jacod&Shiryaev2003] the mappings ω↦tiε​(ω)\omega\mapsto t^{\varepsilon}\_{i}(\omega), ω↦ωtiε​(ω)\omega\mapsto\omega\_{t^{\varepsilon}\_{i}(\omega)}, ω↦ωtiε​(ω)−\omega\mapsto\omega\_{t^{\varepsilon}\_{i}(\omega)-} and ω↦Δ​ωtiε​(ω)\omega\mapsto\Delta\omega\_{t^{\varepsilon}\_{i}(\omega)} are continuous. Thus if bb is continuous then ω↦bωtiε​(ω)​(tiε​(ω),ωtiε​(ω)−,Δ​ωtiε​(ω))\omega\mapsto b^{\omega\_{t^{\varepsilon}\_{i}(\omega)}}(t^{\varepsilon}\_{i}(\omega),\omega\_{t^{\varepsilon}\_{i}(\omega)-},\Delta\omega\_{t^{\varepsilon}\_{i}(\omega)}) is continuous. As Jε​(ω)J^{\varepsilon}(\omega) is finite, fεf^{\varepsilon} is a finite sum of such functions, which imlies that fεf^{\varepsilon} is continuous.

If ω∈{ω∈H​([τ,T],E)|‖Δ​ωt‖>ε,∀t∈[τ,T]}\omega\in\{\omega\in\amsmathbb{H}([\tau,T],E)|\|\Delta\omega\_{t}\|>\varepsilon,\,\forall t\in[\tau,T]\}, then ti​(ω)=tiε​(ω)t\_{i}(\omega)=t\_{i}^{\varepsilon}(\omega) for all i∈{0,…,m}i\in\{0,\ldots,m\} and thus

|  |  |  |
| --- | --- | --- |
|  | f​(ω)=∑t∈J​(ω)bωt​(t,ωt−)=∑t∈Jε​(ω)bωt​(t,ωt−)=fε​(ω),\displaystyle f(\omega)=\sum\_{t\in J(\omega)}b^{\omega\_{t}}(t,\omega\_{t-})=\sum\_{t\in J^{\varepsilon}(\omega)}b^{\omega\_{t}}(t,\omega\_{t-})=f^{\varepsilon}(\omega), |  |

which is continuous.
∎

###### Remark D.3.

Lemma [D.2](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem2 "Lemma D.2. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") holds true on all of H​([τ,T],E)\amsmathbb{H}([\tau,T],E), if there exists an ε>0\varepsilon>0, such that by​(t,x,y−x)=0b^{y}(t,x,y-x)=0 for ‖x−y‖≤ε\|x-y\|\leq\varepsilon.

Next we observe that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1) implies Assumption [5](https://arxiv.org/html/2511.04198v1#Thmassumption5 "Assumption 5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance")(2).

###### Lemma D.4.

Assume that Assumption [1](https://arxiv.org/html/2511.04198v1#Thmassumption1 "Assumption 1. ‣ 2.2. Distribution dependent jump process ‣ 2. Jump processes ‣ Mean-field approximations in insurance")(1) is satisfied. Then it holds that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[(Q1,n​([τ,T]×E))p]<∞\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}\big[\big(Q^{1,n}([\tau,T]\times E)\big)^{p}\big]<\infty |  |

for all p>1p>1.

###### Proof.

Note that X1,nX^{1,n} by construction only jumps, when Q1,nQ^{1,n} jumps. Therefore let Ntℓ,nN^{\ell,n}\_{t} be the counting process t↦Q1,n​([τ,t]×E)t\mapsto Q^{1,n}([\tau,t]\times E) which has intensity process

|  |  |  |
| --- | --- | --- |
|  | t↦∫τt∫Eμs​(x,ρ,d​y)​ds≤Cλ​(t−τ),\displaystyle t\mapsto\int\_{\tau}^{t}\int\_{E}\mu\_{s}(x,\rho,\mathrm{d}y)\mathrm{d}s\leq C\_{\lambda}(t-\tau), |  |

which is bounded, without the bound depending on nn. Thus it follows that all Nt1,nN^{1,n}\_{t} are dominated by a time-homogeneous Poisson process MM with rate Cμ1​(t−τ)C\_{\mu}^{1}(t-\tau) in the sense of first order stochastic dominance. This implies that E​[(NT1,n)p]≤E​MTp<∞\amsmathbb{E}[(N^{1,n}\_{T})^{p}]\leq\amsmathbb{E}{M\_{T}^{p}}<\infty for all n∈Nn\in\amsmathbb{N} and p>1p>1. The desired result follows.
∎

Before proving Proposition [6.3](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem3 "Proposition 6.3. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") we need one final result:

###### Lemma D.5.

Let E⊂RdE\subset\amsmathbb{R}^{d} be countable and that there exists ε>0\varepsilon>0 such that dE​(x,y)>εd\_{E}(x,y)>\varepsilon for all x≠yx\neq y, x,y∈Ex,y\in E. If g:H​([τ,T],E)→Rg:\amsmathbb{H}([\tau,T],E)\rightarrow\amsmathbb{R} is continuous, then so is

|  |  |  |
| --- | --- | --- |
|  | f​(ω):=𝟙{x}​(ωτ)​g​(ω)\displaystyle f(\omega):=\mathds{1}\_{\{x\}}(\omega\_{\tau})g(\omega) |  |

for all x∈Ex\in E.

###### Proof.

Note that t=τt=\tau is a continuity point for every ω∈H​([τ,T],E)\omega\in\amsmathbb{H}([\tau,T],E), since no jump can occur at the initial time. Therefore ω↦ωτ\omega\mapsto\omega\_{\tau} is continuous. Lemma [E.4](https://arxiv.org/html/2511.04198v1#A5.Thmtheorem4 "Lemma E.4. ‣ Appendix E Auxiliary results ‣ Mean-field approximations in insurance") yields that y↦𝟙{x}​(y)y\mapsto\mathds{1}\_{\{x\}}(y) is continuous for every x∈Ex\in E. Thus ω↦𝟙{x}​(ωτ)\omega\mapsto\mathds{1}\_{\{x\}}(\omega\_{\tau}) is continuous and hence also ff.
∎

We now arrive at the proof of Proposition [6.3](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem3 "Proposition 6.3. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance").

###### Proof of Proposition [6.3](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem3 "Proposition 6.3. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance").

By Assumptions [5](https://arxiv.org/html/2511.04198v1#Thmassumption5 "Assumption 5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") and [6](https://arxiv.org/html/2511.04198v1#Thmassumption6 "Assumption 6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") we can use Lemmas [D.1](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem1 "Lemma D.1. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") and [D.2](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem2 "Lemma D.2. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") to conclude that ff is Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta}-a.s. and Q~τ,ζx\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}-a.s. continuous. Due to the weak convergence proved in Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") and Theorem [4.3](https://arxiv.org/html/2511.04198v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4. Mean-field approximation of the conditional distribution ‣ Mean-field approximations in insurance") we may apply Proposition [C.1](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") in order to get the desired result. A sufficient condition for Proposition [C.1](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") to hold is

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[|f​(X1,n)|p]<∞∀p>1.\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[|f(X^{1,n})|^{p}]<\infty\quad\forall p>1. |  |

Due the boundedness of bb and (by)y∈E(b^{y})\_{y\in E} we have that

|  |  |  |
| --- | --- | --- |
|  | E​[|f​(X1,n)|p]≤2p−1​Cbp​(1+E​[(Q1,n​((τ,T]×E))p]).\displaystyle\amsmathbb{E}[|f(X^{1,n})|^{p}]\leq 2^{p-1}C\_{b}^{p}(1+\amsmathbb{E}\big[\big(Q^{1,n}((\tau,T]\times E)\big)^{p}\big]). |  |

Thus it follows by Lemma [D.4](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem4 "Lemma D.4. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") that

|  |  |  |
| --- | --- | --- |
|  | supn∈NE​[|f​(X1,n)|p]≤2p−1​Cbp​(1+supn∈NE​[(Q1,n​((τ,T]×E))p])<∞.\displaystyle\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}[|f(X^{1,n})|^{p}]\leq 2^{p-1}C\_{b}^{p}\Big(1+\sup\_{n\in\amsmathbb{N}}\amsmathbb{E}\big[\big(Q^{1,n}((\tau,T]\times E)\big)^{p}\big]\Big)<\infty. |  |

We may thus apply Proposition [C.1](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") to arrive at the desired result.

Finally if EE is countable and infx≠y‖x−y‖>0\inf\_{x\neq y}\|x-y\|>0, we can use Lemma [D.5](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem5 "Lemma D.5. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") to conclude that ω↦𝟙{x}​(ωτ)​f​(ω)\omega\mapsto\mathds{1}\_{\{x\}}(\omega\_{\tau})f(\omega) and ω↦𝟙{x}​(ωτ)\omega\mapsto\mathds{1}\_{\{x\}}(\omega\_{\tau}) are continuous. As 𝟙{x}​(ωτ)​f​(ω)≤f​(ω)\mathds{1}\_{\{x\}}(\omega\_{\tau})f(\omega)\leq f(\omega) we use Proposition [C.1](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") to conclude that

|  |  |  |
| --- | --- | --- |
|  | limn→∞E​[𝟙{x}​(Xτ1,n)​P​V1,n​(τ)]=E​[𝟙{x}​(X¯τ)​P​V¯​(τ)]\displaystyle\lim\_{n\rightarrow\infty}\amsmathbb{E}[\mathds{1}\_{\{x\}}(X\_{\tau}^{1,n})PV^{1,n}(\tau)]=\amsmathbb{E}[\mathds{1}\_{\{x\}}(\bar{X}\_{\tau})\widebar{PV}(\tau)] |  |

and

|  |  |  |
| --- | --- | --- |
|  | limn→∞E​[𝟙{x}​(Xτ1,n)]=E​[𝟙{x}​(X¯τ)]=ζ​(x).\displaystyle\lim\_{n\rightarrow\infty}\amsmathbb{E}[\mathds{1}\_{\{x\}}(X\_{\tau}^{1,n})]=\amsmathbb{E}[\mathds{1}\_{\{x\}}(\bar{X}\_{\tau})]=\zeta(x). |  |

Thus if ζ​(x)>0\zeta(x)>0, we have that

|  |  |  |
| --- | --- | --- |
|  | limn→∞V1,n​(τ,x)=limn→∞E​[𝟙{x}​(Xτ1,n)​P​V1,n​(τ)]E​[𝟙{x}​(Xτ1,n)]=E​[𝟙{x}​(X¯τ)​P​V¯​(τ)]ζ​(x)=V¯​(τ,x).\displaystyle\lim\_{n\rightarrow\infty}V^{1,n}(\tau,x)=\lim\_{n\rightarrow\infty}\frac{\amsmathbb{E}[\mathds{1}\_{\{x\}}(X\_{\tau}^{1,n})PV^{1,n}(\tau)]}{\amsmathbb{E}[\mathds{1}\_{\{x\}}(X\_{\tau}^{1,n})]}=\frac{\amsmathbb{E}[\mathds{1}\_{\{x\}}(\bar{X}\_{\tau})\widebar{PV}(\tau)]}{\zeta(x)}=\bar{V}(\tau,x). |  |

∎

We continue with the proof of Proposition [6.4](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem4 "Proposition 6.4. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance").

###### Proof of Proposition [6.4](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem4 "Proposition 6.4. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance").

By Assumptions [5](https://arxiv.org/html/2511.04198v1#Thmassumption5 "Assumption 5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") and [6](https://arxiv.org/html/2511.04198v1#Thmassumption6 "Assumption 6. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") we can use Lemmas [D.1](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem1 "Lemma D.1. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") and [D.2](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem2 "Lemma D.2. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") to conclude that ff is Q¯τ,ζ\bar{\amsmathbb{Q}}\_{\tau,\zeta}-a.s. and Q~τ,ζx\widetilde{\amsmathbb{Q}}\_{\tau,\zeta}^{x}-a.s. continuous.

The first result follows from the weak convergence proved in Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") and a similar argument as in the proof of Proposition [6.3](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem3 "Proposition 6.3. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") shows that we may apply Proposition [C.2](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem2 "Proposition C.2. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") to arrive at the desired result.

For the second result we use Lemma [D.5](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem5 "Lemma D.5. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") to conclude that ω↦𝟙{x}​(ωτ)​f​(ω)\omega\mapsto\mathds{1}\_{\{x\}}(\omega\_{\tau})f(\omega) and ω↦𝟙{x}​(ωτ)\omega\mapsto\mathds{1}\_{\{x\}}(\omega\_{\tau}) are continuous. As 𝟙{x}​(ωτ)​f​(ω)≤f​(ω)\mathds{1}\_{\{x\}}(\omega\_{\tau})f(\omega)\leq f(\omega) we use Proposition [C.2](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem2 "Proposition C.2. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance") to conclude that

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1n𝟙{Xτℓ,n=x}​P​Vℓ,n​(τ)→L2E​[𝟙{X¯τ=x}​P​V¯​(τ)]\displaystyle\frac{1}{n}\sum\_{\ell=1}^{n}\mathds{1}\_{\{X\_{\tau}^{\ell,n}=x\}}PV^{\ell,n}(\tau)\stackrel{{\scriptstyle L^{2}}}{{\rightarrow}}\amsmathbb{E}[\mathds{1}\_{\{\bar{X}\_{\tau}=x\}}\widebar{PV}(\tau)] |  |

and

|  |  |  |
| --- | --- | --- |
|  | 1n​∑ℓ=1n𝟙{Xτℓ,n=x}→L2P​(X¯τ=x)=ζ​(x).\displaystyle\frac{1}{n}\sum\_{\ell=1}^{n}\mathds{1}\_{\{X\_{\tau}^{\ell,n}=x\}}\stackrel{{\scriptstyle L^{2}}}{{\rightarrow}}\amsmathbb{P}(\bar{X}\_{\tau}=x)=\zeta(x). |  |

Both convergences also hold in probability and as ζ​(x)>0\zeta(x)>0, we may apply the continuous mapping Theorem for convergence in probability to arrive at the desired result.
∎

###### Proof of Proposition [6.5](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem5 "Proposition 6.5. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance").

The goal is to apply Proposition [C.3](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem3 "Proposition C.3. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance"). By Theorem [3.5](https://arxiv.org/html/2511.04198v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3. Mean-field approximation ‣ Mean-field approximations in insurance") we have the necessary chaosticity property, by Lemmas [D.1](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem1 "Lemma D.1. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") and [D.2](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem2 "Lemma D.2. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") the function ff is almost surely continuous and by Lemma [D.4](https://arxiv.org/html/2511.04198v1#A4.Thmtheorem4 "Lemma D.4. ‣ Appendix D Proof of Propositions 6.3, 6.4 and 6.5 ‣ Mean-field approximations in insurance") and an argument as in the proof of Proposition [6.3](https://arxiv.org/html/2511.04198v1#S6.Thmtheorem3 "Proposition 6.3. ‣ 6. Life insurance applications ‣ Mean-field approximations in insurance") the necessary moment conditions are satisfied. Thus the result follows from Proposition [C.3](https://arxiv.org/html/2511.04198v1#A3.Thmtheorem3 "Proposition C.3. ‣ Appendix C LLN and CLT for chaotic random variables ‣ Mean-field approximations in insurance").
∎

## Appendix E Auxiliary results

###### Lemma E.1.

Let Q1,Q2∈𝒫​(D​([τ,T],E))\amsmathbb{Q}\_{1},\amsmathbb{Q}\_{2}\in\mathcal{P}(\amsmathbb{D}([\tau,T],E)) and let πt:D​([τ,T],E)→E\pi\_{t}:\amsmathbb{D}([\tau,T],E)\rightarrow E be the time-marginal projection. Then dW​(πt​(Q1),πt​(Q2))≤dWU​(Q1,Q2)d\_{W}(\pi\_{t}(\amsmathbb{Q}\_{1}),\pi\_{t}(\amsmathbb{Q}\_{2}))\leq d\_{W}^{U}(\amsmathbb{Q}\_{1},\amsmathbb{Q}\_{2}).

###### Proof.

Let 𝒟\mathcal{D} be the set of couplings between Q1\amsmathbb{Q}\_{1} and Q2\amsmathbb{Q}\_{2} and let 𝒦t\mathcal{K}\_{t} be the set of couplings between πt​(Q1)\pi\_{t}(\amsmathbb{Q}\_{1}) and πt​(Q2)\pi\_{t}(\amsmathbb{Q}\_{2}).

Take any P∈𝒟\amsmathbb{P}\in\mathcal{D}. Then we have that πt(P(∙×D([τ,T],E)))=πt(Q1)\pi\_{t}(\amsmathbb{P}(\bullet\times\amsmathbb{D}([\tau,T],E)))=\pi\_{t}(\amsmathbb{Q}\_{1}) and πt(P(D([τ,T],E)×∙))=πt(Q2)\pi\_{t}(\amsmathbb{P}(\amsmathbb{D}([\tau,T],E)\times\bullet))=\pi\_{t}(\amsmathbb{Q}\_{2}). Thus we have that πt​(𝒟)⊂𝒦t\pi\_{t}(\mathcal{D})\subset\mathcal{K}\_{t}. Hence we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | dWU​(Q1,Q2)\displaystyle d\_{W}^{U}(\amsmathbb{Q}\_{1},\amsmathbb{Q}\_{2}) | =infP∈𝒟∫D​([τ,T],E)2supt∈[τ,T]‖πt​(ω1)−πt​(ω2)‖​P​(d​ω1,d​ω2)\displaystyle=\inf\_{\amsmathbb{P}\in\mathcal{D}}\int\_{\amsmathbb{D}([\tau,T],E)^{2}}\sup\_{t\in[\tau,T]}\|\pi\_{t}(\omega\_{1})-\pi\_{t}(\omega\_{2})\|\amsmathbb{P}(\mathrm{d}\omega\_{1},\mathrm{d}\omega\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥infP∈𝒟∫E2‖x−y‖​πt​(P)​(d​x,d​y)\displaystyle\geq\inf\_{\amsmathbb{P}\in\mathcal{D}}\int\_{E^{2}}\|x-y\|\pi\_{t}(\amsmathbb{P})(\mathrm{d}x,\mathrm{d}y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥infρ∈𝒦t∫E2‖x−y‖​ρ​(d​x,d​y)=dW​(πt​(Q1),πt​(Q2)).\displaystyle\geq\inf\_{\rho\in\mathcal{K}\_{t}}\int\_{E^{2}}\|x-y\|\rho(\mathrm{d}x,\mathrm{d}y)=d\_{W}(\pi\_{t}(\amsmathbb{Q}\_{1}),\pi\_{t}(\amsmathbb{Q}\_{2})). |  |

∎

###### Lemma E.2 (Gronwall’s inequality).

Let uu, vv be non-negative real functions on the interval [τ,T][\tau,T], with vv integrable and uu bounded and measurable. Let c≥0c\geq 0 and assume that

|  |  |  |
| --- | --- | --- |
|  | u​(t)≤c+∫τtv​(s)​u​(s)​ds.\displaystyle u(t)\leq c+\int\_{\tau}^{t}v(s)u(s)\mathrm{d}s. |  |

Then it holds that

|  |  |  |
| --- | --- | --- |
|  | u​(t)≤c​e∫τtv​(s)​ds.\displaystyle u(t)\leq ce^{\int\_{\tau}^{t}v(s)\mathrm{d}s}. |  |

###### Lemma E.3.

Let (xi)i=1,…,n⊂R(x\_{i})\_{i=1,\ldots,n}\subset\amsmathbb{R} and let p>1p>1. Then

|  |  |  |
| --- | --- | --- |
|  | |∑i=1nxi|p≤np−1​∑i=1n|xi|p\displaystyle\bigg|\sum\_{i=1}^{n}x\_{i}\bigg|^{p}\leq n^{p-1}\sum\_{i=1}^{n}|x\_{i}|^{p} |  |

###### Lemma E.4.

Let (E,dE)(E,d\_{E}) be a metric space and assume that there exists ε>0\varepsilon>0 such that dE​(x,y)>εd\_{E}(x,y)>\varepsilon for all x≠yx\neq y, x,y∈Ex,y\in E. Let f:E→(S,dS)f:E\rightarrow(S,d\_{S}), where (S,dS)(S,d\_{S}) is a metric space. Assume that K:=supx,y∈EdS​(f​(x),f​(y))<∞K:=\sup\_{x,y\in E}d\_{S}(f(x),f(y))<\infty. Then ff is Lipschitz continuous with Cf=KεC\_{f}=\frac{K}{\varepsilon}.

###### Proof.

Let x1,x2∈Ex\_{1},x\_{2}\in E. Then dE​(x,y)<εd\_{E}(x,y)<\varepsilon if and only if x1=x2x\_{1}=x\_{2}. Thus we have that

|  |  |  |
| --- | --- | --- |
|  | dS​(f​(x1),f​(x2))≤K≤Kε​|x1−x2|.\displaystyle d\_{S}(f(x\_{1}),f(x\_{2}))\leq K\leq\frac{K}{\varepsilon}|x\_{1}-x\_{2}|. |  |

∎