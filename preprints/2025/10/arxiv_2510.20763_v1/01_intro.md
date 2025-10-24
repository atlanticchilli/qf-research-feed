---
authors:
- David Itkin
doc_id: arxiv:2510.20763v1
family_id: arxiv:2510.20763
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Consumption-Investment Problem in Rank-Based Models
url_abs: http://arxiv.org/abs/2510.20763v1
url_html: https://arxiv.org/html/2510.20763v1
venue: arXiv q-fin
version: 1
year: 2025
---


David Itkin111Department of Statistics, London School of Economics and Political Science, [d.itkin@lse.ac.uk](mailto:d.itkin@lse.ac.uk).

###### Abstract

We study a consumption-investment problem in a multi-asset market where the returns follow a generic rank-based model.
Our main result derives an HJB equation with Neumann boundary conditions for the value function and proves a corresponding verification theorem. The control problem is nonstandard due to the discontinuous nature of the coefficients in rank-based models, requiring a bespoke approach of independent mathematical interest. The special case of first-order models, prescribing constant drift and diffusion coefficients for the ranked returns, admits explicit solutions when the investor is either (a) unconstrained, (b) abides by open market constraints or (c) is fully invested in the market. The explicit optimal strategies in all cases are related to the celebrated solution to Merton’s problem, despite the intractability of constraint (b) in that setting.

#### Keywords:

Optimal portfolio choice, Merton’s problem, rank-based model, reflected stochastic differential equation, Hamilton–Jacobi–Bellman equation, Neumann boundary conditions, open markets.

#### MSC 2020 Classification:

60G44, 91G10, 93E20,

## 1 Introduction

We study a consumption-investment problem in a large dimensional equity market with a risk-free asset and dd equities X=(X1,…,Xd)X=(X\_{1},\dots,X\_{d}) available for investment. The problem is characterized by the value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,x,w)=sup(π,c)∈𝒜T∘​(t,x,w)𝔼t,x​[∫tTe−β​s​U1​(c​(s))​𝑑s+U2​(Vπ,cw​(T))],v(t,x,w)=\sup\_{(\pi,c)\in{\mathcal{A}}\_{T}^{\circ}(t,x,w)}\mathbb{E}\_{t,x}\bigg[\int\_{t}^{T}e^{-\beta s}U\_{1}(c(s))ds+U\_{2}(V^{w}\_{\pi,c}(T))\bigg], |  | (1.1) |

which seeks to maximize an investor’s utility from consumption and terminal wealth (all of the ingredients in ([1.1](https://arxiv.org/html/2510.20763v1#S1.E1 "In 1 Introduction ‣ Consumption-Investment Problem in Rank-Based Models")) are precisely defined in Section [2](https://arxiv.org/html/2510.20763v1#S2 "2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")). Problems of this type have a rich history going back to Merton [[7](https://arxiv.org/html/2510.20763v1#bib.bib7)] who solved the problem explicitly with power utility and when the asset process XX is a geometric Brownian motion (GBM).

Here, we revisit this problem when the stock returns follow a *rank-based* model. These are reduced-form models where each asset’s returns at a given time depend on the rank in the market the company occupies at that time (see ([2.1](https://arxiv.org/html/2510.20763v1#S2.E1 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) below). Rank-based models have been shown to reproduce certain features of large equity markets that standard models are unable to capture, such as the empirical stability of capital distribution in the market over long periods of time [[2](https://arxiv.org/html/2510.20763v1#bib.bib2), [3](https://arxiv.org/html/2510.20763v1#bib.bib3)]. Moreover, the rank-based drift parameters can be efficiently estimated through a, so-called, collision estimator (see [[2](https://arxiv.org/html/2510.20763v1#bib.bib2), Chapter 5.4]) providing a path to drift parameter calibration, which is a notoriously difficult problem for standard name-based models. On the other hand, rank-based models inherently lead to discontinuous coefficients for the returns process leading to difficulties applying the standard stochastic optimal control machinery to characterize the value function ([1.1](https://arxiv.org/html/2510.20763v1#S1.E1 "In 1 Introduction ‣ Consumption-Investment Problem in Rank-Based Models")).

Our main result overcomes this difficulty by deriving the Hamilton–Jacobi–Bellman (HJB) equation that the value function satisfies, ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")), together with the appropriate Neumann boundary conditions, ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")), and proving a corresponding verification result, Theorem [3.2](https://arxiv.org/html/2510.20763v1#S3.Thmlem2 "Theorem 3.2 (Verification theorem). ‣ 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models"). When XX follows the *first-order model* of [[2](https://arxiv.org/html/2510.20763v1#bib.bib2), Chapter 5.5], prescribing constant drift and diffusion coefficients for the ranked returns, it turns out that an explicit solution exists. The optimal rule involves (i) the celebrated Merton fraction

|  |  |  |
| --- | --- | --- |
|  | π~∗=a~−1​(μ~−r​𝟏d),\widetilde{\pi}^{\*}=\widetilde{a}^{-1}(\widetilde{\mu}-r{\bf 1}\_{d}), |  |

where a~\widetilde{a} is the covariance matrix of the ranked returns, μ~\widetilde{\mu} is the drift of the ranked returns and rr is the risk-free rate and (ii) the same optimal feedback form consumption rule c∗c^{\*} as in Merton’s problem. The key difference is that the fraction π~∗\widetilde{\pi}^{\*} specifies the optimal proportion of wealth the investor should hold in the assets according to the rank they occupy, rather than the company name.

Additionally, in Section [4.2](https://arxiv.org/html/2510.20763v1#S4.SS2 "4.2 Open market constraints ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models"), we study *open market* constraints, which have recently gained attention in the literature [[4](https://arxiv.org/html/2510.20763v1#bib.bib4), [5](https://arxiv.org/html/2510.20763v1#bib.bib5)]. These constraints only allow investment in certain ranks and, as such, can serve as a proxy for investors who restrict their investment universe to companies of a certain size (e.g. large cap equities, mid-cap equities, etc.). Remarkably, in the case of first-order models we obtain entirely explicit optimal solutions, whereas the corresponding open market constrained problem in the standard GBM setting is intractable. Section [4.3](https://arxiv.org/html/2510.20763v1#S4.SS3 "4.3 Fully invested constraints ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models") derives further explicit optimal strategies when the investor is additionally required to be fully invested in the market.

On the mathematical side, we characterize the value function for this problem by relating it to an HJB equation with Neumann boundary conditions. Equations of this type on general domains were recently studied in [[8](https://arxiv.org/html/2510.20763v1#bib.bib8)] and shown to characterize the value function with a *reflected* diffusion, corresponding here to the ranked capitalizations X()X\_{()}, as one of the state variables. In contrast, the named capitalizations XX are state variables in ([1.1](https://arxiv.org/html/2510.20763v1#S1.E1 "In 1 Introduction ‣ Consumption-Investment Problem in Rank-Based Models")). As such, the class of admissible controls in [[8](https://arxiv.org/html/2510.20763v1#bib.bib8)] are progressively measurable with respect to the filtration generated by X()X\_{()}, while in our problem the filtration is larger incorporating information about XX. Our main result, Theorem [3.2](https://arxiv.org/html/2510.20763v1#S3.Thmlem2 "Theorem 3.2 (Verification theorem). ‣ 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models"), establishes that the value functions for these two problems coincide despite the fact that the optimal allocations π∗\pi^{\*} for the problem ([1.1](https://arxiv.org/html/2510.20763v1#S1.E1 "In 1 Introduction ‣ Consumption-Investment Problem in Rank-Based Models")) are not adapted to the filtration generated by X()X\_{()}.

The paper is organized as follows. Section [2](https://arxiv.org/html/2510.20763v1#S2 "2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") introduces the model and the consumption-investment problem. In Section [3](https://arxiv.org/html/2510.20763v1#S3 "3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models") we study the associated HJB equation. It is heuristically derived in Section [3.1](https://arxiv.org/html/2510.20763v1#S3.SS1 "3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models") and the verification theorem is established in Section [3.2](https://arxiv.org/html/2510.20763v1#S3.SS2 "3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models"). Finally in Section [4](https://arxiv.org/html/2510.20763v1#S4 "4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models") we consider first-order models with power utility preferences, explicitly solving the unconstrained problem in Section [4.1](https://arxiv.org/html/2510.20763v1#S4.SS1 "4.1 Unconstrained problem ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models"), the open market constrained problem in [4.2](https://arxiv.org/html/2510.20763v1#S4.SS2 "4.2 Open market constraints ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models") and the fully invested constrained problem in [4.3](https://arxiv.org/html/2510.20763v1#S4.SS3 "4.3 Fully invested constraints ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models").

#### Notation

For d≥2d\geq 2 and a vector x∈(0,∞)dx\in(0,\infty)^{d}, we write x()x\_{()} for its decreasing order statistics, which is the permutation of xx satisfying x(1)≥x(2)≥⋯≥x(d)x\_{(1)}\geq x\_{(2)}\geq\dots\geq x\_{(d)}. The set of all ordered vectors is defined as

|  |  |  |
| --- | --- | --- |
|  | (0,∞)≥d={y∈(0,∞)d:y1≥y2≥⋯≥yd}.(0,\infty)^{d}\_{\geq}=\{y\in(0,\infty)^{d}:y\_{1}\geq y\_{2}\geq\dots\geq y\_{d}\}. |  |

The subset of (0,∞)≥d(0,\infty)^{d}\_{\geq} consisting of all points where no coordinates are equal will be denoted by (0,∞)>d(0,\infty)^{d}\_{>} and its complement by (0,∞)=d=(0,∞)≥d∖(0,∞)>d(0,\infty)^{d}\_{=}=(0,\infty)^{d}\_{\geq}\setminus(0,\infty)^{d}\_{>}.

For every i∈{1,…,d}i\in\{1,\dots,d\}, we define the rank identifying function ℛi:(0,∞)d→{1,…,d}{\mathcal{R}}\_{i}:(0,\infty)^{d}\to\{1,\dots,d\} via ℛi​(x)=k{\mathcal{R}}\_{i}(x)=k if xi=x(k)x\_{i}=x\_{(k)}. To ensure this is well-defined we break ties using lexicographical ordering. That is, ℛi​(x)=min⁡{k∈{1,…,d}:xi=x(k)}{\mathcal{R}}\_{i}(x)=\min\{k\in\{1,\dots,d\}:x\_{i}=x\_{(k)}\} though the precise tie-breaking rule does not affect the results in this paper.

## 2 The consumption-investment problem

### 2.1 Financial market

We consider a financial market consisting of a risk-free asset d​X0​(t)=r​X0​(t)​d​tdX\_{0}(t)=rX\_{0}(t)dt
with risk-free rate rate r∈ℝr\in\mathbb{R} and dd risky assets with market capitalizations X=(X1,…,Xd)X=(X\_{1},\dots,X\_{d}). We take a rank-based model for the risky assets,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xi​(s)Xi​(s)=μi​(s,X​(s))​d​t+∑j=1dσi​j​(s,X​(s))​d​Wj​(s),Xi​(t)=xi;i=1,…,d,s≥t,\frac{dX\_{i}(s)}{X\_{i}(s)}=\mu\_{i}(s,X(s))dt+\sum\_{j=1}^{d}\sigma\_{ij}(s,X(s))dW\_{j}(s),\quad X\_{i}(t)=x\_{i};\qquad i=1,\dots,d,\quad s\geq t, |  | (2.1) |

for any initial time t≥0t\geq 0 and initial value x∈(0,∞)dx\in(0,\infty)^{d},
where

|  |  |  |
| --- | --- | --- |
|  | μi​(t,x)=∑k=1dμ~k​(t,x())​1{ℛi​(x)=k},σi​j​(t,x)=∑k,ℓ=1dσ~k​ℓ​(t,x())​1{ℛi​(x)=k,ℛj​(x)=ℓ}\mu\_{i}(t,x)=\sum\_{k=1}^{d}\widetilde{\mu}\_{k}(t,x\_{()})1\_{\{{\mathcal{R}}\_{i}(x)=k\}},\qquad\sigma\_{ij}(t,x)=\sum\_{k,\ell=1}^{d}\widetilde{\sigma}\_{k\ell}(t,x\_{()})1\_{\{{\mathcal{R}}\_{i}(x)=k,{\mathcal{R}}\_{j}(x)=\ell\}} |  |

for some functions μ~k,σ~k​ℓ:[0,∞)×(0,∞)d→ℝ\widetilde{\mu}\_{k},\widetilde{\sigma}\_{k\ell}:[0,\infty)\times(0,\infty)^{d}\to\mathbb{R}
and where WW is a standard Brownian motion. In this model an asset’s dynamics only depend on which rank that asset occupies at any time. We impose the following assumption on the inputs

###### Assumption 2.1.

μ~\widetilde{\mu} and σ~\widetilde{\sigma} are bounded and σ~\widetilde{\sigma} is uniformly elliptic. They additionally satisfy the following uniform Lipschitz condition,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖y1∘μ~​(t,y1)−y2∘μ~​(t,y2)‖+‖diag​(y1)​σ~​(t,y1)−diag​(y2)​σ~​(t,y2)‖≤L​‖y1−y2‖,\|y\_{1}\circ\widetilde{\mu}(t,y\_{1})-y\_{2}\circ\widetilde{\mu}(t,y\_{2})\|+\|\mathrm{diag}(y\_{1})\widetilde{\sigma}(t,y\_{1})-\mathrm{diag}(y\_{2})\widetilde{\sigma}(t,y\_{2})\|\leq L\|y\_{1}-y\_{2}\|, |  | (2.2) |

for some L>0L>0, all y1,y2∈(0,∞)≥dy\_{1},y\_{2}\in(0,\infty)^{d}\_{\geq} and t≥0t\geq 0. Here ∘\circ denotes elementwise product and diag​(y)\mathrm{diag}(y) is the d×dd\times d matrix with yy on the diagonal and zeros elsewhere.

Despite the high regularity of μ~\widetilde{\mu} and σ~\widetilde{\sigma}, the coefficients μ\mu and σ\sigma will typically be discontinuous and fail to be weakly differentiable. As such, we cannot expect strong solutions or uniqueness in law to ([2.1](https://arxiv.org/html/2510.20763v1#S2.E1 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")), but we will nevertheless
be able to work with weak solutions. In contrast, the coefficients of the ranked capitalizations are quite regular. Indeed, the result [[1](https://arxiv.org/html/2510.20763v1#bib.bib1), Theorem 2.5]222Note that the semimartingale decomposition in their Theorem 2.5 is applicable to the process X()X\_{()} here due to the remark preceding the statement of the theorem. ensures that the ranked process Y=X()Y=X\_{()} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yk​(s)=Yk​(s)​(μ~k​(s,Y​(s))​d​s+∑ℓ=1dσ~k​ℓ​(s,Y​(s))​d​Bℓ​(s))+d​Φk​(s),Yk​(t)=yk,dY\_{k}(s)=Y\_{k}(s)\Big(\widetilde{\mu}\_{k}(s,Y(s))ds+\sum\_{\ell=1}^{d}\widetilde{\sigma}\_{k\ell}(s,Y(s))dB\_{\ell}(s)\Big)+d\Phi\_{k}(s),\quad Y\_{k}(t)=y\_{k}, |  | (2.3) |

for k=1,…,dk=1,\dots,d, s≥ts\geq t, where yk=x(k)y\_{k}=x\_{(k)}, Bℓ​(s)=∫ts∑j=1d1{ℛj​(X​(u))=ℓ}​d​Wj​(u)B\_{\ell}(s)=\int\_{t}^{s}\sum\_{j=1}^{d}1\_{\{{\mathcal{R}}\_{j}(X(u))=\ell\}}dW\_{j}(u) and Φ\Phi is the reflection term given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φk​(s)=12​∑ℓ=k+1d∫ts1Nk​(u)​𝑑LYk−Yℓ​(u)−12​∑ℓ=1k−1∫ts1Nk​(u)​𝑑LYℓ−Yk​(u);k=1,…,d,\Phi\_{k}(s)=\frac{1}{2}\sum\_{\ell=k+1}^{d}\int\_{t}^{s}\frac{1}{N\_{k}(u)}dL\_{Y\_{k}-Y\_{\ell}}(u)-\frac{1}{2}\sum\_{\ell=1}^{k-1}\int\_{t}^{s}\frac{1}{N\_{k}(u)}dL\_{Y\_{\ell}-Y\_{k}}(u);\qquad k=1,\dots,d, |  | (2.4) |

with Nk​(u)=|{j∈{1,…,d}:Xj​(u)=X(k)​(u)}|N\_{k}(u)=|\{j\in\{1,\dots,d\}:X\_{j}(u)=X\_{(k)}(u)\}| and LYk−YℓL\_{Y\_{k}-Y\_{\ell}} being the semimartingale local time at zero of Yk−YℓY\_{k}-Y\_{\ell}. In particular, BB is a standard Brownian motion so ([2.3](https://arxiv.org/html/2510.20763v1#S2.E3 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) is a reflected stochastic differential equation (RSDE) with normal reflection on the domain (0,∞)≥d(0,\infty)^{d}\_{\geq}.

###### Proposition 2.2.

Let Assumption [2.1](https://arxiv.org/html/2510.20763v1#S2.Thmlem1 "Assumption 2.1. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") hold. Then

1. (i)

   there exists a weak solution to ([2.1](https://arxiv.org/html/2510.20763v1#S2.E1 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) for every initial t≥0t\geq 0, x∈(0,∞)dx\in(0,\infty)^{d},
2. (ii)

   there exists a pathwise unique strong solution (Y,Φ)(Y,\Phi) to ([2.3](https://arxiv.org/html/2510.20763v1#S2.E3 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) for every initial t≥0t\geq 0, y∈(0,∞)≥dy\in(0,\infty)^{d}\_{\geq}. The solution is a strong Markov process and satisfies the moment bound

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼~t,y​[supt≤s≤T‖Y​(s)‖p]≤CT,p​(1+‖y‖p)\widetilde{\mathbb{E}}\_{t,y}\bigg[\sup\_{t\leq s\leq T}\|Y(s)\|^{p}\bigg]\leq C\_{T,p}(1+\|y\|^{p}) |  | (2.5) |

   for any T≥tT\geq t, p≥1p\geq 1 and some constant CT,p>0C\_{T,p}>0. Here 𝔼~t,y​[⋅]\widetilde{\mathbb{E}}\_{t,y}[\cdot] denote expectation with respect to the law of YY when the initial value is Y​(t)=yY(t)=y.

For item [(i)](https://arxiv.org/html/2510.20763v1#S2.I1.i1 "item (i) ‣ Proposition 2.2. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") it is equivalent to establish weak existence on ℝd\mathbb{R}^{d} for Z=(log⁡X1,…​log⁡Xd)Z=(\log X\_{1},\dots\log X\_{d}), which satisfies the SDE

|  |  |  |
| --- | --- | --- |
|  | dZ(s)=((μ∘exp)(s,Z(s))+12(diag(a∘exp)(s,Z(s)))ds+(σ∘exp)(s,Z(s))dW(s),dZ(s)=\big((\mu\circ\exp)(s,Z(s))+\frac{1}{2}(\mathrm{diag}(a\circ\exp)(s,Z(s))\big)ds+(\sigma\circ\exp)(s,Z(s))dW(s), |  |

where a=σ​σ⊤a=\sigma\sigma^{\top} and exp⁡(z)=(exp⁡(z1),…,exp⁡(zd))\exp(z)=(\exp(z\_{1}),\dots,\exp(z\_{d})). By Assumption [2.1](https://arxiv.org/html/2510.20763v1#S2.Thmlem1 "Assumption 2.1. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models"), the drift and volatility coefficients of ZZ are measurable and bounded and the diffusion matrix is uniformly elliptic. Hence, [[6](https://arxiv.org/html/2510.20763v1#bib.bib6), Theorem 2.6.1] guarantees the existence of a weak solution.

The strong existence and pathwise uniqueness of the RSDE follows from Assumption [2.1](https://arxiv.org/html/2510.20763v1#S2.Thmlem1 "Assumption 2.1. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") courtesy of [[10](https://arxiv.org/html/2510.20763v1#bib.bib10), Theorem 4.1]. Both the strong Markov property and the moment bound ([2.5](https://arxiv.org/html/2510.20763v1#S2.E5 "In item (ii) ‣ Proposition 2.2. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) are standard results with the former being a consequence of uniqueness in law (see [[9](https://arxiv.org/html/2510.20763v1#bib.bib9), Section 6.2]) and the latter following from Gronwall and Burkholder–Davis–Gundy inequalities (see e.g. the proof of [[8](https://arxiv.org/html/2510.20763v1#bib.bib8), Proposition 2.1]).
∎

In view of Proposition [2.2](https://arxiv.org/html/2510.20763v1#S2.Thmlem2 "Proposition 2.2. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models"), given an initial time t≥0t\geq 0 and initial value X​(t)=xX(t)=x we can work on a filtered probability space (Ω,ℱ,(ℱs)s≥t,ℙt,x)(\Omega,{\mathcal{F}},({\mathcal{F}}\_{s})\_{s\geq t},\mathbb{P}\_{t,x}) satisfying the usual conditions and supporting a process XX satisfying ([2.1](https://arxiv.org/html/2510.20763v1#S2.E1 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")). Since X()X\_{()} solves ([2.3](https://arxiv.org/html/2510.20763v1#S2.E3 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) with y=x()y=x\_{()}, we have courtesy of the strong existence and pathwise uniqueness for the RSDE that the moment estimate ([2.5](https://arxiv.org/html/2510.20763v1#S2.E5 "In item (ii) ‣ Proposition 2.2. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) holds for X()X\_{()}. Moreover, X()X\_{()} is a strong Markov process and the law of the ranked capitalizations can be represented via the pushforward measure ℙ~t,y=x()​#​ℙt,x\widetilde{\mathbb{P}}\_{t,y}=x\_{()}\#\mathbb{P}\_{t,x}. In particular, any distinct solutions XX to ([2.1](https://arxiv.org/html/2510.20763v1#S2.E1 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")), even if on different probability spaces, give rise to the same law for the ranked capitalization process X()X\_{()}.

### 2.2 The stochastic optimal control problem

When starting with initial wealth w>0w>0, using the trading strategy π​(s)=(π1​(s),…,πd​(s))\pi(s)=(\pi\_{1}(s),\dots,\pi\_{d}(s)) and consuming at rate c​(s)≥0c(s)\geq 0 for s≥ts\geq t the investors wealth process Vπ,cwV\_{\pi,c}^{w} evolves according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vπ,cw​(s)\displaystyle dV\_{\pi,c}^{w}(s) | =(Vπ,cw​(s)​(∑i=1dπi​(s)​d​Xi​(s)Xi​(s)+π0​(s)​d​X0​(s)X0​(s))−c​(s))​d​s\displaystyle=\bigg(V\_{\pi,c}^{w}(s)\Big(\sum\_{i=1}^{d}\pi\_{i}(s)\frac{dX\_{i}(s)}{X\_{i}(s)}+\pi\_{0}(s)\frac{dX\_{0}(s)}{X\_{0}(s)}\Big)-c(s)\bigg)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Vπ,cw​(s)​(π​(s)⊤​(μ​(s,X​(s))−r​𝟏d)+r)−c​(s))​d​s+π​(s)⊤​σ​(s,X​(s))​d​W​(s),\displaystyle=\Big(V^{w}\_{\pi,c}(s)\big(\pi(s)^{\top}(\mu(s,X(s))-r{\bf 1}\_{d})+r\big)-c(s)\Big)ds+\pi(s)^{\top}\sigma(s,X(s))dW(s), |  |

where π0​(s)=1−∑i=1dπi​(s)\pi\_{0}(s)=1-\sum\_{i=1}^{d}\pi\_{i}(s) is the proportion of wealth invested in the risk-free asset and 𝟏d{\bf 1}\_{d} denotes the dd-dimensional vector of all ones. Given a time horizon T∈(0,∞)T\in(0,\infty) we restrict our attention to strictly positive wealth processes

|  |  |  |
| --- | --- | --- |
|  | 𝒜T​(t,x,w)={(π​(s),c​(s))s∈[t,T]:(π,c)​ are progressively measurable, ​c≥0 and ​Vπ,cw>0,ℙt,x​-a.s. on ​[t,T]}.{\mathcal{A}}\_{T}(t,x,w)=\bigg\{(\pi(s),c(s))\_{s\in[t,T]}:\begin{aligned} &\quad(\pi,c)\text{ are progressively measurable, }c\geq 0\\ &\quad\text{ and }V^{w}\_{\pi,c}>0,\mathbb{P}\_{t,x}\text{-a.s.\ on }[t,T]\end{aligned}\bigg\}. |  |

Our goal is to solve the investment-consumption problem characterized by the value function ([1.1](https://arxiv.org/html/2510.20763v1#S1.E1 "In 1 Introduction ‣ Consumption-Investment Problem in Rank-Based Models")) given in the introduction, where β>0\beta>0 is the patience parameter, 𝒜T∘​(t,x,w)⊂𝒜T​(t,x,w){\mathcal{A}}\_{T}^{\circ}(t,x,w)\subset{\mathcal{A}}\_{T}(t,x,w) is the set of admissible controls specified in Section [2.3](https://arxiv.org/html/2510.20763v1#S2.SS3 "2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") and U1,U2:(0,∞)→ℝU\_{1},U\_{2}:(0,\infty)\to\mathbb{R} are utility functions, which we assume are concave and increasing. Utility functions on the real line or an infinite time horizon can be handled similarly, but we do not pursue this here.

###### Remark 2.3.

Due to the potential nonuniqueness in law to ([2.1](https://arxiv.org/html/2510.20763v1#S2.E1 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) it is not apriori clear that the value function vv depends only on (t,x,w)(t,x,w) and not the particular solution to ([2.1](https://arxiv.org/html/2510.20763v1#S2.E1 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")). Part of our main result, Theorem [3.2](https://arxiv.org/html/2510.20763v1#S3.Thmlem2 "Theorem 3.2 (Verification theorem). ‣ 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models"), establishes that it is independent of the particular solution.

### 2.3 Control set

Here we define the set of controls 𝒜T∘​(t,x,w){\mathcal{A}}\_{T}^{\circ}(t,x,w) over which we optimize. We assume it is of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜T∘​(t,x,w)={(π​(s),c​(s))s∈[t,T]∈𝒜T​(t,x,w):(π​(s),c​(s))∈A​(X​(s),Vπ,cw​(s))∀s∈[t,T]}{\mathcal{A}}\_{T}^{\circ}(t,x,w)=\{(\pi(s),c(s))\_{s\in[t,T]}\in{\mathcal{A}}\_{T}(t,x,w):(\pi(s),c(s))\in A(X(s),V\_{\pi,c}^{w}(s))\quad\forall s\in[t,T]\} |  | (2.6) |

for some nonempty measurable subsets A​(x,w)⊂ℝd×[0,∞)A(x,w)\subset\mathbb{R}^{d}\times[0,\infty), which specify constraints on the controls. Next we define the rank-based constraint sets

|  |  |  |  |
| --- | --- | --- | --- |
|  | A~​(x,w)\displaystyle\widetilde{A}(x,w) | ={(π~,c)∈ℝd×[0,∞):π~k=∑i=1dπi​1{ℛi​(x)=k}∀k​ and some ​(π,c)∈A​(x,w)}.\displaystyle=\bigg\{(\widetilde{\pi},c)\in\mathbb{R}^{d}\times[0,\infty):\widetilde{\pi}\_{k}=\sum\_{i=1}^{d}\pi\_{i}1\_{\{{\mathcal{R}}\_{i}(x)=k\}}\quad\forall k\text{ and some }(\pi,c)\in A(x,w)\bigg\}. |  |

If at some point in time the investor’s portfolio weights are π∈ℝd\pi\in\mathbb{R}^{d} then π~k\widetilde{\pi}\_{k} is the proportion of wealth the investor holds in the asset currently occupying rank kk.
The main condition we will impose is permutation invariance of the rank-based constraint sets.

###### Assumption 2.4.

A~​(x,w)=A~​(x(),w)\widetilde{A}(x,w)=\widetilde{A}(x\_{()},w) for every (x,w)∈(0,∞)d+1(x,w)\in(0,\infty)^{d+1}.

We now present a few examples of common constraints that satisfy Assumption [2.4](https://arxiv.org/html/2510.20763v1#S2.Thmlem4 "Assumption 2.4. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models").

###### Example 2.5.

1. (i)

   (Unconstrained). A​(x,w)=ℝd×[0,∞)A(x,w)=\mathbb{R}^{d}\times[0,\infty),
2. (ii)

   (Long-only). A​(x,w)=[0,1]d×[0,∞)A(x,w)=[0,1]^{d}\times[0,\infty),
3. (iii)

   (Fully invested). A​(x,w)={π∈ℝd:π1+⋯+πd=1}×[0,∞)A(x,w)=\{\pi\in\mathbb{R}^{d}:\pi\_{1}+\dots+\pi\_{d}=1\}\times[0,\infty),
4. (iv)

   (Open market). A(x,w)={π∈ℝd:πi=0A(x,w)=\{\pi\in\mathbb{R}^{d}:\pi\_{i}=0 if ℛi(x)∉[n,N]}×[0,∞)\mathcal{R}\_{i}(x)\not\in[n,N]\}\times[0,\infty) for some 1≤n≤N≤d1\leq n\leq N\leq d.

That items [(i)](https://arxiv.org/html/2510.20763v1#S2.I3.i1 "item (i) ‣ Example 2.5. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")-[(iii)](https://arxiv.org/html/2510.20763v1#S2.I3.i3 "item (iii) ‣ Example 2.5. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") satisfy Assumption [2.4](https://arxiv.org/html/2510.20763v1#S2.Thmlem4 "Assumption 2.4. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") is clear, while for [(iv)](https://arxiv.org/html/2510.20763v1#S2.I3.i4 "item (iv) ‣ Example 2.5. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") we note that

|  |  |  |
| --- | --- | --- |
|  | A~={(π~,c)∈ℝd×[0,∞):π~k=0​ if ​k∉[n,N]}\widetilde{A}=\{(\widetilde{\pi},c)\in\mathbb{R}^{d}\times[0,\infty):\widetilde{\pi}\_{k}=0\text{ if }k\not\in[n,N]\} |  |

is state independent and, hence, satisfies Assumption [2.4](https://arxiv.org/html/2510.20763v1#S2.Thmlem4 "Assumption 2.4. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models"). An example of a constraint that does not satisfy Assumption [2.4](https://arxiv.org/html/2510.20763v1#S2.Thmlem4 "Assumption 2.4. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") is an asset based long-only constraint A​(x,w)=[0,∞)×ℝd−1×[0,∞)A(x,w)=[0,\infty)\times\mathbb{R}^{d-1}\times[0,\infty), which prohibits short selling in asset one, but allows it in the other assets.

## 3 Dynamic programming approach

In this section, we will work with the domains

|  |  |  |
| --- | --- | --- |
|  | D=[0,T)×(0,∞)d×(0,∞),D≥=[0,T)×(0,∞)≥d×(0,∞).D=[0,T)\times(0,\infty)^{d}\times(0,\infty),\qquad D\_{\geq}=[0,T)\times(0,\infty)^{d}\_{\geq}\times(0,\infty). |  |

We will similarly write D>D\_{>} and D=D\_{=} as in D≥D\_{\geq} with (0,∞)≥d(0,\infty)^{d}\_{\geq} replaced by (0,∞)>d(0,\infty)^{d}\_{>} and (0,∞)=d(0,\infty)^{d}\_{=} respectively. When the right endpoint {T}\{T\} is included we will append the corresponding set with a bar, such as D¯\overline{D}.
For a function v:D→ℝv:D\to\mathbb{R}, we will write ∂tv\partial\_{t}v for the derivative in the first argument, ∇v\nabla v for the (d+1)(d+1)-dimensional gradient in the last two arguments, ∇xv\nabla\_{x}v for the gradient in the second argument and ∂wv\partial\_{w}v for the derivative in the third argument. Similarly ∇2v\nabla^{2}v will denote the (d+1)×(d+1)(d+1)\times(d+1) Hessian while ∇x2v\nabla\_{x}^{2}v, ∂w∇xv\partial\_{w}\nabla\_{x}v and ∂w​wv\partial\_{ww}v will denote its respective components. For a function v~:D≥→ℝ\widetilde{v}:D\_{\geq}\to\mathbb{R} we will use an analogous convention and refer by ∇yv~\nabla\_{y}\widetilde{v} and ∇y2v~\nabla\_{y}^{2}\widetilde{v} to the derivatives in the second variable.

### 3.1 Heuristic discussion

The HJB associated to the value function ([1.1](https://arxiv.org/html/2510.20763v1#S1.E1 "In 1 Introduction ‣ Consumption-Investment Problem in Rank-Based Models")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | {0=(∂t+LX)​v​(t,x,w)+sup(π,c)∈A​(x,w)Hπ,c​(t,x,w,∇v​(t,x,w),∇2v​(t,x,w)),in ​D,v​(T,x,w)=U2​(w),in ​(0,∞)d+1,\begin{cases}\displaystyle 0=(\partial\_{t}+L^{X})v(t,x,w)+\sup\_{(\pi,c)\in A(x,w)}H\_{\pi,c}(t,x,w,\nabla v(t,x,w),\nabla^{2}v(t,x,w)),&\text{in }D,\\ v(T,x,w)=U\_{2}(w),&\text{in }(0,\infty)^{d+1},\end{cases} |  | (3.1) |

where LX​v=∑i=1dxi​μi​∂xkv+12​∑i,j=1dxi​xj​ai​j​∂xi​xjvL^{X}v=\sum\_{i=1}^{d}x\_{i}\mu\_{i}\partial\_{x\_{k}}v+\frac{1}{2}\sum\_{i,j=1}^{d}x\_{i}x\_{j}a\_{ij}\partial\_{x\_{i}x\_{j}}v and the Hamiltonian is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hπ,c​(t,x,w,ξ,M)\displaystyle H\_{\pi,c}(t,x,w,\xi,M) | =w​ξd+1​(r+π⊤​(μ​(t,x)−r​𝟏d))+w​π⊤​a​(t,x)​Md+1,1:d\displaystyle=w\xi\_{d+1}(r+\pi^{\top}(\mu(t,x)-r{\bf 1}\_{d}))+w\pi^{\top}a(t,x)M\_{d+1,1:d} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +w22​Md+1,d+1​π⊤​a​(t,x)​π−ξd+1​c+e−β​t​U1​(c)\displaystyle\qquad+\frac{w^{2}}{2}M\_{d+1,d+1}\pi^{\top}a(t,x)\pi-\xi\_{d+1}c+e^{-\beta t}U\_{1}(c) |  |

for (t,x,w,ξ,M)∈D×ℝd+1×ℝ(d+1)×(d+1)(t,x,w,\xi,M)\in D\times\mathbb{R}^{d+1}\times\mathbb{R}^{(d+1)\times(d+1)}
and where a​(t,x)=σ​(t,x)​σ​(t,x)⊤a(t,x)=\sigma(t,x)\sigma(t,x)^{\top} and Md+1,1:dM\_{d+1,1:d} denotes the first dd components in the (d+1)(d+1)st row of MM.
The HJB ([3.1](https://arxiv.org/html/2510.20763v1#S3.E1 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) is a second order nonlinear PDE where the coefficients μ\mu and aa are, in general, only measurable and bounded. Due to lack of regularity, the standard viscosity solution theory is not directly applicable.

To make progress we make the ansatz

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,x,w)=v~​(t,x(),w)v(t,x,w)=\widetilde{v}(t,x\_{()},w) |  | (3.2) |

for some function v~:D≥→ℝ\widetilde{v}:D\_{\geq}\to\mathbb{R}. For any kk the map x↦x(k)x\mapsto x\_{(k)} is Lipschitz and differentiable outside the Lebesgue null-set {x:xi=xj​ for some ​i≠j}\{x:x\_{i}=x\_{j}\text{ for some }i\neq j\} with derivative given by 1{ℛi​(x)=k}1\_{\{{\mathcal{R}}\_{i}(x)=k\}}. As such, by making this substitution into ([3.1](https://arxiv.org/html/2510.20763v1#S3.E1 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")), we formally expect v~\widetilde{v} to satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | {0=(∂t+LY)​v~​(t,y,w)+sup(π~,c)∈A~​(y,w)H~π~,c​(t,y,w,∇v~​(t,y,w),∇2v~​(t,y,w)),in ​D>,v~​(T,y,w)=U2​(w),in ​(0,∞)≥d×(0,∞),\begin{cases}\displaystyle 0=(\partial\_{t}+L^{Y})\widetilde{v}(t,y,w)+\sup\_{(\widetilde{\pi},c)\in\widetilde{A}(y,w)}\widetilde{H}\_{\widetilde{\pi},c}(t,y,w,\nabla\widetilde{v}(t,y,w),\nabla^{2}\widetilde{v}(t,y,w)),&\hfill\text{in }D\_{>},\\ \widetilde{v}(T,y,w)=U\_{2}(w),&\hskip-28.45274pt\text{in }(0,\infty)^{d}\_{\geq}\times(0,\infty),\end{cases} |  | (3.3) |

where LY​v~=∑k=1dyk​μ~k​∂ykv~+12​∑k,ℓ=1dyk​yℓ​a~k​ℓ​∂yk​yℓv~L^{Y}\widetilde{v}=\sum\_{k=1}^{d}y\_{k}\widetilde{\mu}\_{k}\partial\_{y\_{k}}\widetilde{v}+\frac{1}{2}\sum\_{k,\ell=1}^{d}y\_{k}y\_{\ell}\widetilde{a}\_{k\ell}\partial\_{y\_{k}y\_{\ell}}\widetilde{v} and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H~π~,c​(t,y,w,ξ,M)\displaystyle\widetilde{H}\_{\widetilde{\pi},c}(t,y,w,\xi,M) | =w​ξd+1​(r+π~⊤​(μ~​(t,y)−r​𝟏d))+w​π~⊤​a~​(t,y)​Md+1,1:d\displaystyle=w\xi\_{d+1}(r+\widetilde{\pi}^{\top}(\widetilde{\mu}(t,y)-r{\bf 1}\_{d}))+w\widetilde{\pi}^{\top}\widetilde{a}(t,y)M\_{d+1,1:d} |  | (3.4) |
|  |  | +w22​Md+1,d+1​π~⊤​a~​(t,y)​π~−ξd+1​c+e−β​t​U1​(c).\displaystyle\qquad+\frac{w^{2}}{2}M\_{d+1,d+1}\widetilde{\pi}^{\top}\widetilde{a}(t,y)\widetilde{\pi}-\xi\_{d+1}c+e^{-\beta t}U\_{1}(c). |  |

The diffusion matrix a~\widetilde{a} does not degenerate on the boundary D=D\_{=} so the equation ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) needs to be appended with boundary conditions. As X()X\_{()} satisfies an RSDE with normal reflection, we will impose Neumann boundary conditions on v~\widetilde{v},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇yv~​(t,y,w)⊤​𝐧​(y)=0,for ​(t,y,w)∈D=\nabla\_{y}\widetilde{v}(t,y,w)^{\top}{\bf n}(y)=0,\quad\text{for }(t,y,w)\in D\_{=} |  | (3.5) |

for any normal vector 𝐧​(y){\bf n}(y) at y∈D=y\in D\_{=}. The important role of the boundary condition ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) will become apparent in the proof of the verification theorem in the next section.

###### Remark 3.1.

For any y∈(0,∞)=dy\in(0,\infty)^{d}\_{=} with exactly two equal components yk=yk+1y\_{k}=y\_{k+1}, the unique (up to multiplicative constant) normal vector is 𝐧​(y)=ek−ek+1{\bf n}(y)=e\_{k}-e\_{k+1}. Points with three or more indices coinciding (e.g. yk+1=yk=yk−1y\_{k+1}=y\_{k}=y\_{k-1}) admit additional normal vectors. If the process Y=X()Y=X\_{()} of ([2.4](https://arxiv.org/html/2510.20763v1#S2.E4 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) is such that LYk−Yℓ=0L\_{Y\_{k}-Y\_{\ell}}=0 whenever k−ℓ>1k-\ell>1 then ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) only needs to hold for normal vectors of the type ek−ek+1e\_{k}-e\_{k+1}. A sufficient condition for these local times to vanish is if triple collisions of components of XX do not occur.

### 3.2 Verification theorem

HJB equations of the type ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) on fairly general domains with Neumann boundary conditions ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) have recently been studied in [[8](https://arxiv.org/html/2510.20763v1#bib.bib8)]. Under certain assumptions, the authors are able to establish the existence of a unique viscosity solution to ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and characterize it as the value function of a certain stochastic control problem. In our setting this value function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v~​(t,y,w)=sup(π~,c)∈𝒜~T∘​(t,y,w)𝔼~t,y​[∫tTU1​(c​(s))​𝑑s+U2​(V~π~,cw​(T))],\widetilde{v}(t,y,w)=\sup\_{(\widetilde{\pi},c)\in\widetilde{\mathcal{A}}\_{T}^{\circ}(t,y,w)}\widetilde{\mathbb{E}}\_{t,y}\bigg[\int\_{t}^{T}U\_{1}(c(s))ds+U\_{2}(\widetilde{V}^{w}\_{\widetilde{\pi},c}(T))\bigg], |  | (3.6) |

where YY is as in ([2.3](https://arxiv.org/html/2510.20763v1#S2.E3 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")), the process V~π~,cw\widetilde{V}^{w}\_{\widetilde{\pi},c} is given by

|  |  |  |
| --- | --- | --- |
|  | d​V~π~,cw​(s)=(V~π~,cw​(s)​(π~​(s)⊤​(μ~​(s,Y​(s))−r​𝟏d)+r)−c​(s))​d​s+V~π~,cw​(s)​π~​(s)⊤​σ~​(s,Y​(s))​d​B​(s),d\widetilde{V}^{w}\_{\widetilde{\pi},c}(s)=\Big(\widetilde{V}^{w}\_{\widetilde{\pi},c}(s)\big(\widetilde{\pi}(s)^{\top}(\widetilde{\mu}(s,Y(s))-r{\bf 1}\_{d})+r\big)-c(s)\Big)ds+\widetilde{V}^{w}\_{\widetilde{\pi},c}(s)\widetilde{\pi}(s)^{\top}\widetilde{\sigma}(s,Y(s))dB(s), |  |

for s≥ts\geq t with V~π,cw​(t)=w\widetilde{V}^{w}\_{\pi,c}(t)=w and 𝒜~T∘​(t,y,w)\widetilde{\mathcal{A}}\_{T}^{\circ}(t,y,w) denotes the set of admissible control processes. This set is akin to ([2.6](https://arxiv.org/html/2510.20763v1#S2.E6 "In 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) with A~​(y,w)\widetilde{A}(y,w) in place of A​(x,w)A(x,w) except additionally restricted to consisting only of processes (π~​(s),c​(s))s∈[t,T](\widetilde{\pi}(s),c(s))\_{s\in[t,T]} which are progressively measurable with respect to ℱB{\mathcal{F}}^{B}.

It is far from clear if the value function vv satisfies the relationship ([3.2](https://arxiv.org/html/2510.20763v1#S3.E2 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) with v~\widetilde{v} solving ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")). Indeed, the representation ([3.6](https://arxiv.org/html/2510.20763v1#S3.E6 "In 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) only allows for controls adapted to ℱB{\mathcal{F}}^{B}, while the original filtration ℱ=ℱX,W{\mathcal{F}}={\mathcal{F}}^{X,W} is larger. Nevertheless, we will show below that the relationship ([3.2](https://arxiv.org/html/2510.20763v1#S3.E2 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) holds where v~\widetilde{v} is a solution to ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")). For clarity of exposition, and since it is sufficient for our main example in Section [4](https://arxiv.org/html/2510.20763v1#S4 "4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models"), we will prove a verification theorem in the case of a classical solution to the HJB.

###### Theorem 3.2 (Verification theorem).

Let Assumptions [2.1](https://arxiv.org/html/2510.20763v1#S2.Thmlem1 "Assumption 2.1. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") and [2.4](https://arxiv.org/html/2510.20763v1#S2.Thmlem4 "Assumption 2.4. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") hold.
Suppose there exists a nonnegative function v~∈C1,2​(D≥)∩C​(D¯≥)\widetilde{v}\in C^{1,2}(D\_{\geq})\cap C(\overline{D}\_{\geq}) satisfying ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")), ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and the polynomial growth condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v~​(t,y,w)|≤C​(1+‖y‖p+|w|p),for all ​(t,y,w)∈D¯≥,|\widetilde{v}(t,y,w)|\leq C(1+\|y\|^{p}+|w|^{p}),\quad\text{for all }(t,y,w)\in\overline{D}\_{\geq}, |  | (3.7) |

for some C>0C>0 and p≥1p\geq 1. Suppose, further, that there exists a measurable maximizer

|  |  |  |  |
| --- | --- | --- | --- |
|  | (π~∗​(t,y,w),c~∗​(t,y,w))∈arg⁡max(π~,c)∈𝒜~​(y,w)⁡H~π~,c​(t,y,w,∇v~​(t,y,w),∇2v~​(t,y,w))(\widetilde{\pi}^{\*}(t,y,w),\widetilde{c}^{\*}(t,y,w))\in{\arg\max}\_{(\widetilde{\pi},c)\in\widetilde{\mathcal{A}}(y,w)}\widetilde{H}\_{\widetilde{\pi},c}(t,y,w,\nabla\widetilde{v}(t,y,w),\nabla^{2}\widetilde{v}(t,y,w)) |  | (3.8) |

for every (t,y,w)∈D≥(t,y,w)\in D\_{\geq}
satisfying the following uniform Lipschitz and linear growth conditions

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | ‖w1​π~∗​(t,y,w1)−w2​π~∗​(t,y,w2)‖+|c~∗​(t,y,w1)−c~∗​(t,y,w2)|\displaystyle\|w\_{1}\widetilde{\pi}^{\*}(t,y,w\_{1})-w\_{2}\widetilde{\pi}^{\*}(t,y,w\_{2})\|+|\widetilde{c}^{\*}(t,y,w\_{1})-\widetilde{c}^{\*}(t,y,w\_{2})| | ≤L​|w1−w2|,\displaystyle\leq L|w\_{1}-w\_{2}|, |  | (3.9) |
|  |  | ‖w1​π~∗​(t,y,w1)‖+|c∗​(t,y,w1)|\displaystyle\|w\_{1}\widetilde{\pi}^{\*}(t,y,w\_{1})\|+|c^{\*}(t,y,w\_{1})| | ≤C​(1+‖y‖+|w1|)\displaystyle\leq C(1+\|y\|+|w\_{1}|) |  |

for some C,L>0C,L>0 and all y∈(0,∞)≥dy\in(0,\infty)^{d}\_{\geq}, w1,w2∈(0,∞)w\_{1},w\_{2}\in(0,\infty). Then the value function ([1.1](https://arxiv.org/html/2510.20763v1#S1.E1 "In 1 Introduction ‣ Consumption-Investment Problem in Rank-Based Models")) is given by v​(t,x,w)=v~​(t,x(),w)v(t,x,w)=\widetilde{v}(t,x\_{()},w) and an optimal strategy (π∗,c∗)(\pi^{\*},c^{\*}) is given in feedback form by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | πi∗​(t,X​(t),Vπ∗,c∗w​(t))=∑k=1dπ~k∗​(t,X()​(t),Vπ∗,c∗w​(t))​1{ℛi​(X​(t))=k},\displaystyle\pi^{\*}\_{i}(t,X(t),V^{w}\_{\pi^{\*},c^{\*}}(t))=\sum\_{k=1}^{d}\widetilde{\pi}^{\*}\_{k}(t,X\_{()}(t),V^{w}\_{\pi^{\*},c^{\*}}(t))1\_{\{{\mathcal{R}}\_{i}(X(t))=k\}}, | i=1,…,d,t≥0,\displaystyle i=1,\dots,d,\quad t\geq 0, |  | (3.10) |
|  |  | c∗​(t,X​(t),Vπ∗,c∗w​(t))=c~∗​(t,X()​(t),Vπ∗,c∗w​(t)),\displaystyle c^{\*}(t,X(t),V^{w}\_{\pi^{\*},c^{\*}}(t))=\widetilde{c}^{\*}(t,X\_{()}(t),V^{w}\_{\pi^{\*},c^{\*}}(t)), | t≥0.\displaystyle t\geq 0. |  |

###### Remark 3.3.

π~∗,c~∗\widetilde{\pi}^{\*},\widetilde{c}^{\*} and c∗c^{\*} are ℱB{\mathcal{F}}^{B} measurable, but the optimal control π∗\pi^{\*} is not.

We fix initial values (t,x,w)∈D(t,x,w)\in D and
let (π,c)∈𝒜T∘​(t,x,w)(\pi,c)\in{\mathcal{A}}\_{T}^{\circ}(t,x,w) be arbitrary. In the course of this proof, to simplify the exposition, we will write Z​(t)=(X()​(t),Vπ,cw​(t))Z(t)=(X\_{()}(t),V^{w}\_{\pi,c}(t)). Applying Itô’s formula to v~​(s,Z​(s))\widetilde{v}(s,Z(s)), adding and subtracting e−β​s​U1​(c​(s))​d​se^{-\beta s}U\_{1}(c(s))ds and using the fact that X()X\_{()} satisfies ([2.3](https://arxiv.org/html/2510.20763v1#S2.E3 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​v~​(s,Z​(s))=\displaystyle d\widetilde{v}(s,Z(s))= | (∂tv~​(s,Z​(s))+H~π~​(s),c​(s)​(s,Z​(s),∇v~​(s,Z​(s)),∇2v~​(s,Z​(s)))−e−β​s​U1​(c​(s)))​d​s\displaystyle\Big(\partial\_{t}\widetilde{v}(s,Z(s))+\widetilde{H}\_{\widetilde{\pi}(s),c(s)}\big(s,Z(s),\nabla\widetilde{v}(s,Z(s)),\nabla^{2}\widetilde{v}(s,Z(s))\big)-e^{-\beta s}U\_{1}(c(s))\Big)ds |  | (3.11) |
|  |  | +d​M​(s)+∇yv~​(s,Z​(s))⊤​d​Φ​(s),\displaystyle\quad+dM(s)+\nabla\_{y}\widetilde{v}(s,Z(s))^{\top}d\Phi(s), |  |

where d​M​(s)=Vπ,cw​(s)​∂wv~​(s,Z​(s))​π​(s)⊤​σ​(s,X​(s))​d​W​(s)+∇yv~​(s,Z​(s))⊤​σ~​(s,X()​(s))​d​B​(s)dM(s)=V^{w}\_{\pi,c}(s)\partial\_{w}\widetilde{v}(s,Z(s))\pi(s)^{\top}\sigma(s,X(s))dW(s)+\nabla\_{y}\widetilde{v}(s,Z(s))^{\top}\widetilde{\sigma}(s,X\_{()}(s))dB(s) is a local martingale and π~k​(s)=∑i=1dπi​(s)​1{ℛi​(X​(t))=k}\widetilde{\pi}\_{k}(s)=\sum\_{i=1}^{d}\pi\_{i}(s)1\_{\{{\mathcal{R}}\_{i}(X(t))=k\}} for every kk. Here we used the fact that π​(s)⊤​μ​(s,Z​(s))=π~​(s)⊤​μ~​(s,Z​(s))\pi(s)^{\top}\mu(s,Z(s))=\widetilde{\pi}(s)^{\top}\widetilde{\mu}(s,Z(s))
and π​(s)⊤​a​(s,X​(s))​π​(s)=π~​(s)⊤​a~​(s,Z​(s))​π~​(s)\pi(s)^{\top}a(s,X(s))\pi(s)=\widetilde{\pi}(s)^{\top}\widetilde{a}(s,Z(s))\widetilde{\pi}(s) to rewrite the Hamiltonian in terms of (π~,c)(\widetilde{\pi},c).

By Assumption [2.4](https://arxiv.org/html/2510.20763v1#S2.Thmlem4 "Assumption 2.4. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") on the constraint set we have that (π~​(s),c​(s))∈A~​(X()​(s),Vπ,cw​(s))(\widetilde{\pi}(s),c(s))\in\widetilde{A}(X\_{()}(s),V^{w}\_{\pi,c}(s)) so we deduce from ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) that the sum of the first two terms in the d​tdt integral of the right hand side of ([3.11](https://arxiv.org/html/2510.20763v1#S3.E11 "In 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) are nonpositive. Additionally, the Neumann boundary condition ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) ensures that the reflection terms vanish. As such, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | v~​(u,Z​(u))≤v~​(t,x(),w)−∫tue−β​s​U1​(c​(s))​𝑑s+M​(u)−M​(t)\widetilde{v}(u,Z(u))\leq\widetilde{v}(t,x\_{()},w)-\int\_{t}^{u}e^{-\beta s}U\_{1}(c(s))ds+M(u)-M(t) |  | (3.12) |

for all t≤u≤Tt\leq u\leq T.
We now define the localizing sequence of stopping times τn=inf{t≥0:M​(t)≥n}\tau\_{n}=\inf\{t\geq 0:M(t)\geq n\} and note that M(⋅∧τn)M(\cdot\land\tau\_{n}) is a martingale for every nn. Evaluating ([3.12](https://arxiv.org/html/2510.20763v1#S3.E12 "In 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) at u=T∧τnu=T\land\tau\_{n} and taking expectation yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[v~​(T∧τn,Z​(T∧τn))]≤v~​(t,x(),w)−𝔼t,x​[∫tT∧τne−β​s​U1​(c​(s))​𝑑s].\mathbb{E}\_{t,x}[\widetilde{v}(T\land\tau\_{n},Z(T\land\tau\_{n}))]\leq\widetilde{v}(t,x\_{()},w)-\mathbb{E}\_{t,x}\bigg[\int\_{t}^{T\land\tau\_{n}}e^{-\beta s}U\_{1}(c(s))ds\bigg]. |  |

Sending n→∞n\to\infty we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[U2​(Vπ,cw​(T))]≤v~​(t,x(),w)−𝔼t,x​[∫tTe−β​s​U1​(c​(s))​𝑑s],\displaystyle\mathbb{E}\_{t,x}[U\_{2}(V^{w}\_{\pi,c}(T))]\leq\widetilde{v}(t,x\_{()},w)-\mathbb{E}\_{t,x}\bigg[\int\_{t}^{T}e^{-\beta s}U\_{1}(c(s))ds\bigg], |  |

where we used Fatou’s lemma and the terminal condition from ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) on the left hand side and monotone convergence on the right hand side.
This establishes that

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,x,w)=sup(π,c)∈𝒜T∘​(t,x,w)𝔼t,x​[∫tTe−β​s​U1​(c​(s))​𝑑s+U2​(Vπ,cw​(T))]≤v~​(t,x(),w).v(t,x,w)=\sup\_{(\pi,c)\in{\mathcal{A}}\_{T}^{\circ}(t,x,w)}\mathbb{E}\_{t,x}\bigg[\int\_{t}^{T}e^{-\beta s}U\_{1}(c(s))ds+U\_{2}(V^{w}\_{\pi,c}(T))\bigg]\leq\widetilde{v}(t,x\_{()},w). |  | (3.13) |

To obtain the reverse inequality we now consider the feedback control (π∗​(s),c∗​(s))s∈[t,T](\pi^{\*}(s),c^{\*}(s))\_{s\in[t,T]}. Note that for any x∈(0,∞)dx\in(0,\infty)^{d} and (π~,c)∈A~​(x(),w)(\widetilde{\pi},c)\in\widetilde{A}(x\_{()},w) we have that (π,c)∈A​(x,w)(\pi,c)\in A(x,w) where πi=∑k=1dπ~k​1{ℛi​(x)=k}\pi\_{i}=\sum\_{k=1}^{d}\widetilde{\pi}\_{k}1\_{\{\mathcal{R}\_{i}(x)=k\}} so that (π∗,c∗)(\pi^{\*},c^{\*}) is an admissible control.
Its wealth process V∗=Vπ∗,c∗wV^{\*}=V^{w}\_{\pi^{\*},c^{\*}} has dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​V∗​(s)\displaystyle dV^{\*}(s) | =(V∗(s)((r+π~∗(s,X()(s),V∗(s))⊤(μ~(s,X()(s))−r𝟏d))−c~∗(s,X()(s),V∗(s)))ds\displaystyle=\Big(V^{\*}(s)\Big((r+\widetilde{\pi}^{\*}(s,X\_{()}(s),V^{\*}(s))^{\top}(\widetilde{\mu}(s,X\_{()}(s))-r{\bf 1}\_{d})\Big)-\widetilde{c}^{\*}(s,X\_{()}(s),V^{\*}(s))\Big)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +V∗​(s)​π~∗​(s,X()​(s),V∗​(s))⊤​σ~​(s,X()​(s))​d​B​(s).\displaystyle\qquad+V^{\*}(s)\widetilde{\pi}^{\*}(s,X\_{()}(s),V^{\*}(s))^{\top}\widetilde{\sigma}(s,X\_{()}(s))dB(s). |  |

Since XX is an autonomous uncontrolled state process this SDE can be written in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​V∗​(s)=α​(V∗​(s),ω)​d​s+ν​(V∗​(s),ω)​d​B​(s),dV^{\*}(s)=\alpha(V^{\*}(s),\omega)ds+\nu(V^{\*}(s),\omega)dB(s), |  | (3.14) |

where the coefficients α\alpha and ν\nu satisfy uniform Lipschitz and linear growth conditions
courtesy of ([3.9](https://arxiv.org/html/2510.20763v1#S3.E9 "In Theorem 3.2 (Verification theorem). ‣ 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")). As such, by the standard Itô theory for SDEs there exists a pathwise unique solution V∗V^{\*} to ([3.14](https://arxiv.org/html/2510.20763v1#S3.E14 "In 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")), which satisfies the bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x​[supt≤s≤T|V∗​(s)|p]≤C​(1+|w|p)\mathbb{E}\_{t,x}\Big[\sup\_{t\leq s\leq T}|V^{\*}(s)|^{p}\Big]\leq C(1+|w|^{p}) |  | (3.15) |

for every T≥0T\geq 0, p≥1p\geq 1 and some constant C>0C>0.
Now, letting Z∗​(t)=(X()​(t),V∗​(t))Z^{\*}(t)=(X\_{()}(t),V^{\*}(t)) we proceed by Itô’s formula to see that

|  |  |  |
| --- | --- | --- |
|  | d​v~​(s,Z∗​(s))=e−β​s​U1​(c∗​(s,Z∗​(s)))​d​s+d​M∗​(s),d\widetilde{v}(s,Z^{\*}(s))=e^{-\beta s}U\_{1}(c^{\*}(s,Z^{\*}(s)))ds+dM^{\*}(s), |  |

where d​M∗​(s)=(V∗​(s)​∂wv~​(s,Z∗​(s))​π~∗​(s,Z∗​(s))+∇yv~​(s,Z∗​(s)))⊤​σ~​(s,Z∗​(s))​d​B​(s)dM^{\*}(s)=(V^{\*}(s)\partial\_{w}\widetilde{v}(s,Z^{\*}(s))\widetilde{\pi}^{\*}(s,Z^{\*}(s))+\nabla\_{y}\widetilde{v}(s,Z^{\*}(s)))^{\top}\widetilde{\sigma}(s,Z^{\*}(s))dB(s) is a local martingale, we used the optimality of (π∗,c∗)(\pi^{\*},c^{\*}) as in ([3.8](https://arxiv.org/html/2510.20763v1#S3.E8 "In Theorem 3.2 (Verification theorem). ‣ 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and the HJB ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) to handle the Hamiltonian term,
and, as before, we used the Neumann boundary condition ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) to ensure that the reflection terms vanish. Defining the stopping times τn∗=inf{s≥0:M∗​(s)≥n}\tau\_{n}^{\*}=\inf\{s\geq 0:M^{\*}(s)\geq n\} we see that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[v~​(T∧τn∗,Z∗​(T∧τn∗))]=v~​(t,x(),w)−𝔼t,x​[∫tT∧τn∗e−β​s​U1​(c∗​(s,Z∗​(s)))​𝑑s].\mathbb{E}\_{t,x}[\widetilde{v}(T\land\tau\_{n}^{\*},Z^{\*}(T\land\tau^{\*}\_{n}))]=\widetilde{v}(t,x\_{()},w)-\mathbb{E}\_{t,x}\bigg[\int\_{t}^{T\land\tau\_{n}^{\*}}e^{-\beta s}U\_{1}(c^{\*}(s,Z^{\*}(s)))ds\bigg]. |  |

By the polynomial growth condition ([3.7](https://arxiv.org/html/2510.20763v1#S3.E7 "In Theorem 3.2 (Verification theorem). ‣ 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) of v~\widetilde{v} together with the LpL^{p} bounds ([2.5](https://arxiv.org/html/2510.20763v1#S2.E5 "In item (ii) ‣ Proposition 2.2. ‣ 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) and ([3.15](https://arxiv.org/html/2510.20763v1#S3.E15 "In 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) we can send n→∞n\to\infty and use dominated convergence on the left-hand side together with the terminal condition in ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and monotone convergence on the right-hand side to obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[U2​(V∗​(T))]=v~​(t,x(),w)−𝔼t,x​[∫tTe−β​s​U1​(c∗​(s,Z∗​(s)))​𝑑s].\mathbb{E}\_{t,x}[U\_{2}(V^{\*}(T))]=\widetilde{v}(t,x\_{()},w)-\mathbb{E}\_{t,x}\bigg[\int\_{t}^{T}e^{-\beta s}U\_{1}(c^{\*}(s,Z^{\*}(s)))ds\bigg]. |  |

Since (π∗,c∗)∈𝒜T∘​(t,x,w)(\pi^{\*},c^{\*})\in{\mathcal{A}}\_{T}^{\circ}(t,x,w) we deduce that v​(t,x,w)≥v~​(t,x(),w)v(t,x,w)\geq\widetilde{v}(t,x\_{()},w), which
together with ([3.13](https://arxiv.org/html/2510.20763v1#S3.E13 "In 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) shows that v​(t,x,w)=v~​(t,x(),w)v(t,x,w)=\widetilde{v}(t,x\_{()},w) and that (π∗,c∗)(\pi^{\*},c^{\*}) is an optimal control.
∎

## 4 First-order models

Here we assume constant coefficients by setting μ~​(t,y)=μ~\widetilde{\mu}(t,y)=\widetilde{\mu} and σ~​(t,y)=σ~\widetilde{\sigma}(t,y)=\widetilde{\sigma} for some μ~∈ℝd\widetilde{\mu}\in\mathbb{R}^{d} and σ~∈𝕊++d\widetilde{\sigma}\in\mathbb{S}^{d}\_{++}, the space of symmetric positive definite d×dd\times d matrices. This model for XX is known as a *first order model* and was first proposed in [[2](https://arxiv.org/html/2510.20763v1#bib.bib2), Chapter 5.5]. As this model has constant drift and volatility coefficients it is reminiscent of the multivariate version of Merton’s problem, though first-order models prescribe constant coefficients for the ranked capitalizations rather than their named counterparts.

One criticism of Merton’s problem is the difficulty in estimating the drift parameters for the named assets. This problem is mitigated in first-order models as the rank-based drift parameters can be estimated through the collision local times appearing in the reflection term ([2.4](https://arxiv.org/html/2510.20763v1#S2.E4 "In 2.1 Financial market ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models")) (see [[2](https://arxiv.org/html/2510.20763v1#bib.bib2), Chapter 5.5] for more details). Moreover, as we will see in the following subsection, the optimal investment-consumption problem in first-order models admits an explicit solution which shares similarities to the optimal strategy in Merton’s problem. As such, the financial intuition, conclusions and tractability of Merton’s problem carry over to the present setting. Moreover, we are able to obtain an explicit solution under open market constraints, which is not a tractable constraint in the standard multivariate version of Merton’s problem. In this section we work with the family of power utility functions given for risk-aversion parameter γ∈(0,1)∪(1,∞)\gamma\in(0,1)\cup(1,\infty) and for w>0w>0 by

|  |  |  |
| --- | --- | --- |
|  | U1​(w)=U2​(w)=U​(w)=11−γ​w1−γ.U\_{1}(w)=U\_{2}(w)=U(w)=\frac{1}{1-\gamma}w^{1-\gamma}. |  |

### 4.1 Unconstrained problem

Here we let the constraint set A~​(x,w)=ℝd×[0,∞)\widetilde{A}(x,w)=\mathbb{R}^{d}\times[0,\infty). In this case the HJB ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) becomes precisely the HJB for Merton’s problem except on the smaller domain D≥D\_{\geq}, rather than DD, and with the addition of the Neumann boundary conditions ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")). It is well-known that the solution to the HJB for Merton’s problem is independent of the asset price variable. Hence, the same solution satisfies ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")). Indeed, it is straightforward to verify that

|  |  |  |
| --- | --- | --- |
|  | π~∗=1γ​a~−1​(μ~−r​𝟏d),c~∗​(t,w)=e−βγ​t​f​(t;ν)​w,v~​(t,w)=f​(t;ν)γ​w1−γ1−γ,\widetilde{\pi}^{\*}=\frac{1}{\gamma}\widetilde{a}^{-1}(\widetilde{\mu}-r{\bf 1}\_{d}),\qquad\widetilde{c}^{\*}(t,w)=e^{-\frac{\beta}{\gamma}t}f(t;\nu)w,\qquad\widetilde{v}(t,w)=f(t;\nu)^{\gamma}\frac{w^{1-\gamma}}{1-\gamma}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t;ν)=eνγ​(T−t)+γν−β​e−νγ​t​(eν−βγ​T−eν−βγ​t)​ and ​ν=(1−γ)​(r+12​γ​(μ~−r​𝟏d)⊤​a~−1​(μ~−r​𝟏d))f(t;\nu)=e^{\frac{\nu}{\gamma}(T-t)}+\frac{\gamma}{\nu-\beta}e^{-\frac{\nu}{\gamma}t}\Big(e^{\frac{\nu-\beta}{\gamma}T}-e^{\frac{\nu-\beta}{\gamma}t}\Big)\ \text{ and }\ \nu=(1-\gamma)\Big(r+\frac{1}{2\gamma}(\widetilde{\mu}-r{\bf 1}\_{d})^{\top}\widetilde{a}^{-1}(\widetilde{\mu}-r{\bf 1}\_{d})\Big) |  | (4.1) |

satisfy ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) and ([3.5](https://arxiv.org/html/2510.20763v1#S3.E5 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")).333If ν=β\nu=\beta the correct expression is obtained by taking the limit as ν→β\nu\to\beta in ([4.1](https://arxiv.org/html/2510.20763v1#S4.E1 "In 4.1 Unconstrained problem ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models")). As such, as a consequence of Theorem [3.2](https://arxiv.org/html/2510.20763v1#S3.Thmlem2 "Theorem 3.2 (Verification theorem). ‣ 3.2 Verification theorem ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models"), we obtain that the value function is given by v=v~v=\widetilde{v}, since the latter is independent of yy, and the optimal controls are of feedback form, pinned down by the functions

|  |  |  |
| --- | --- | --- |
|  | πi∗​(x)=1γ​∑k=1dπ~k∗​1{ℛi​(x)=k},c∗​(t,w)=f​(t;ν)γ​w1−γ1−γ.\pi^{\*}\_{i}(x)=\frac{1}{\gamma}\sum\_{k=1}^{d}\widetilde{\pi}^{\*}\_{k}1\_{\{\mathcal{R}\_{i}(x)=k\}},\qquad c^{\*}(t,w)=f(t;\nu)^{\gamma}\frac{w^{1-\gamma}}{1-\gamma}. |  |

Thus the value function and optimal consumption rate in the first-order models are precisely the same as in Merton’s problem when the assets have parameters μ~\widetilde{\mu} and σ~\widetilde{\sigma}. The optimal investment strategy π∗\pi^{\*} also involves the constant Merton fractions π~∗=1γ​a~−1​(μ~−r​𝟏d)\widetilde{\pi}^{\*}=\frac{1}{\gamma}\widetilde{a}^{-1}(\widetilde{\mu}-r{\bf 1}\_{d}) though, unlike in Merton’s problem, they prescribe investment in the ranked assets.

### 4.2 Open market constraints

Here we study the case when the investor is only allowed to invest in assets whose rank is in between nn and NN for some integers 1≤n≤N≤d1\leq n\leq N\leq d. Open markets allow the assets available for investment to change over time. This offers a tractable way to incorporate a changing investment universe into the analysis. Moreover, it can serve as a proxy for investors who restrict themselves to certain subsets of the available investment universe. For example taking n=1n=1 and N=500N=500 restricts investment to the largest 500 assets in the market, which can serve as a proxy for an investor who chooses to only invest in assets that make up the S&P 500.

As in pare [(iv)](https://arxiv.org/html/2510.20763v1#S2.I3.i4 "item (iv) ‣ Example 2.5. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") of Example [2.5](https://arxiv.org/html/2510.20763v1#S2.Thmlem5 "Example 2.5. ‣ 2.3 Control set ‣ 2 The consumption-investment problem ‣ Consumption-Investment Problem in Rank-Based Models") and the discussion following, the open market constraint enforces π~k=0\widetilde{\pi}\_{k}=0 whenever k∉[n,N]k\not\in[n,N]. As such, making the ansatz that v~\widetilde{v} is independent of yy again, the Hamiltonian in the HJB ([3.3](https://arxiv.org/html/2510.20763v1#S3.E3 "In 3.1 Heuristic discussion ‣ 3 Dynamic programming approach ‣ Consumption-Investment Problem in Rank-Based Models")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | supη∈ℝN−n+1{w​∂wv~​(r+η⊤​(μ~[n:N]−r​𝟏N−n+1))+w22​∂w​wv~​η⊤​a~[n:N]​η}+supc≥0{−c​∂wv~+e−β​t​U​(c)},\sup\_{\eta\in\mathbb{R}^{N-n+1}}\{w\partial\_{w}\widetilde{v}(r+\eta^{\top}(\widetilde{\mu}\_{[n:N]}-r{\bf 1}\_{N-n+1}))+\frac{w^{2}}{2}\partial\_{ww}\widetilde{v}\eta^{\top}\widetilde{a}\_{[n:N]}\eta\}+\sup\_{c\geq 0}\{-c\partial\_{w}\widetilde{v}+e^{-\beta t}U(c)\}, |  | (4.2) |

where η\eta corresponds to the non-zero entries of π~\widetilde{\pi} and μ~[n:N]\widetilde{\mu}\_{[n:N]}, a~[n:N]\widetilde{a}\_{[n:N]} are the truncated vector (μ~k)n≤k≤N(\widetilde{\mu}\_{k})\_{n\leq k\leq N} and matrix (a~k​ℓ)n≤k,ℓ≤N(\widetilde{a}\_{k\ell})\_{n\leq k,\ell\leq N} respectively. We recognize that ([4.2](https://arxiv.org/html/2510.20763v1#S4.E2 "In 4.2 Open market constraints ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models")) corresponds precisely to the Hamiltonian in Merton’s problem when there are N−n+1N-n+1 risky assets and they possess drift vector μ~[n:N]\widetilde{\mu}\_{[n:N]} and diffusion matrix a~[n:N]\widetilde{a}\_{[n:N]}. As such, in a similar fashion as to the unconstrained case, we see that the value function is given by

|  |  |  |
| --- | --- | --- |
|  | v​(t,w)=f​(t;ν[n:N])γ​w1−γ1−γv(t,w)=f(t;\nu\_{[n:N]})^{\gamma}\frac{w^{1-\gamma}}{1-\gamma} |  |

and the optimal controls are given by the feedback functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi∗​(x)\displaystyle\pi^{\*}\_{i}(x) | =∑k=nNη~k−n+1∗​1{ℛi​(x)=k},whereη~∗=1γ​(a~[n:N])−1​(μ~[n:N]−r​𝟏N−n+1),\displaystyle=\sum\_{k=n}^{N}\widetilde{\eta}^{\*}\_{k-n+1}1\_{\{\mathcal{R}\_{i}(x)=k\}},\quad\text{where}\quad\widetilde{\eta}^{\*}=\frac{1}{\gamma}(\widetilde{a}\_{[n:N]})^{-1}(\widetilde{\mu}\_{[n:N]}-r{\bf 1}\_{N-n+1}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c∗​(t,w)\displaystyle c^{\*}(t,w) | =e−βγ​t​f​(t;ν[n,N])​w,\displaystyle=e^{-\frac{\beta}{\gamma}t}f(t;\nu\_{[n,N]})w, |  |

where ff is as in ([4.1](https://arxiv.org/html/2510.20763v1#S4.E1 "In 4.1 Unconstrained problem ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models")) and

|  |  |  |
| --- | --- | --- |
|  | ν[n:N]=(1−γ)​(r+12​γ​(μ~[n:N]−r​𝟏d)⊤​(a~[n:N])−1​(μ~[n:N]−r​𝟏d))\nu\_{[n:N]}=(1-\gamma)\Big(r+\frac{1}{2\gamma}(\widetilde{\mu}\_{[n:N]}-r{\bf 1}\_{d})^{\top}(\widetilde{a}\_{[n:N]})^{-1}(\widetilde{\mu}\_{[n:N]}-r{\bf 1}\_{d})\Big) |  |

The upshot is that open market constraints, which are intractable in Merton’s problem, admit an explicit solution in first-order models.
Moreover, the rank-based Merton fraction η~∗\widetilde{\eta}^{\*} prescribes the optimal holdings. In particular the optimal strategy does not depend on μ~k\widetilde{\mu}\_{k} or a~k​ℓ\widetilde{a}\_{k\ell} for k,ℓ∉[n,N]k,\ell\not\in[n,N].

### 4.3 Fully invested constraints

Here we look at the combined open market and fully invested constraints characterized by

|  |  |  |
| --- | --- | --- |
|  | A~={π~∈ℝd:π~k=0​ if ​k∉[n,N]​ and ​π~⊤​𝟏d=0}×[0,∞).\widetilde{A}=\{\widetilde{\pi}\in\mathbb{R}^{d}:\widetilde{\pi}\_{k}=0\text{ if }k\not\in[n,N]\text{ and }\widetilde{\pi}^{\top}{\bf 1}\_{d}=0\}\times[0,\infty). |  |

Again writing η∈ℝN−n+1\eta\in\mathbb{R}^{N-n+1} for the nonzero components of π~\widetilde{\pi} we obtain the same Hamiltonian ([4.2](https://arxiv.org/html/2510.20763v1#S4.E2 "In 4.2 Open market constraints ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models")) with the additional constraint that η⊤​𝟏N−n+1=1\eta^{\top}{\bf 1}\_{N-n+1}=1. The problem for cc is as before, while the problem for η\eta is a quadratic programming problem with linear constraints and can be solved explicitly. Hence, we obtain

|  |  |  |
| --- | --- | --- |
|  | η∗=(a[n:N])−1​(−∂wv~w​∂w​wv~​μ~[n:N]+(1+∂wv~w​∂w​wv~𝟏⊤(a~[n:N])−1μ~[n:N]𝟏⊤​(a~[n:N])−1​𝟏​𝟏),c∗=e−β​t​(∂wv~)−1γ,\eta^{\*}=(a\_{[n:N]})^{-1}\bigg(-\frac{\partial\_{w}\widetilde{v}}{w\partial\_{ww}\widetilde{v}}\widetilde{\mu}\_{[n:N]}+\frac{(1+\frac{\partial\_{w}\widetilde{v}}{w\partial\_{ww}\widetilde{v}}{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}\widetilde{\mu}\_{[n:N]}}{{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}{\bf 1}}{\bf 1}\bigg),\quad c^{\*}=e^{-\beta t}(\partial\_{w}\widetilde{v})^{-\frac{1}{\gamma}}, |  |

where we write 𝟏{\bf 1} in place of 𝟏N−n+1{\bf 1}\_{N-n+1} for brevity.
Next we make the standard ansatz v~​(t,w)=u​(t)​w1−γ1−γ\widetilde{v}(t,w)=u(t)\frac{w^{1-\gamma}}{1-\gamma} for an unknown function uu, which leads to the ODE

|  |  |  |
| --- | --- | --- |
|  | 0=u′​(t)+ζ​u​(t)+γ​e−βγ​t​u​(t)1−1γ;u​(T)=1,0=u^{\prime}(t)+\zeta u(t)+\gamma e^{-\frac{\beta}{\gamma}t}u(t)^{1-\frac{1}{\gamma}};\qquad u(T)=1, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ζ=1−γ2​γ​(μ~[n:N]−γ−𝟏⊤​(a~[n:N])−1​μ~[n:N]𝟏⊤​(a~[n:N])−1​𝟏​𝟏)⊤​(a~[n:N])−1​(μ~[n;N]+γ−𝟏⊤​(a~[n:N])−1​μ~[n:N]𝟏⊤​(a~[n:N])−1​𝟏​𝟏).\zeta=\frac{1-\gamma}{2\gamma}\bigg(\widetilde{\mu}\_{[n:N]}-\frac{\gamma-{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}\widetilde{\mu}\_{[n:N]}}{{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}{\bf 1}}{\bf 1}\bigg)^{\top}(\widetilde{a}\_{[n:N]})^{-1}\bigg(\widetilde{\mu}\_{[n;N]}+\frac{\gamma-{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}\widetilde{\mu}\_{[n:N]}}{{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}{\bf 1}}{\bf 1}\bigg). |  |

This ODE has solution u​(t)=f​(t;ζ)γu(t)=f(t;\zeta)^{\gamma}, where ff is given by ([4.1](https://arxiv.org/html/2510.20763v1#S4.E1 "In 4.1 Unconstrained problem ‣ 4 First-order models ‣ Consumption-Investment Problem in Rank-Based Models")). As such, the optimal controls are given by the feedback functions

|  |  |  |
| --- | --- | --- |
|  | πi∗​(x)=∑k=nNη~k−n+1∗​1{ℛi​(x)=k}​ with ​η~∗=1γ​(a~[n:N])−1​(μ~[n:N]+γ−𝟏⊤​(a~[n:N])−1​μ~[n:N]𝟏⊤​(a~[n:N])−1​𝟏​𝟏),\displaystyle\pi^{\*}\_{i}(x)=\sum\_{k=n}^{N}\widetilde{\eta}^{\*}\_{k-n+1}1\_{\{{\mathcal{R}}\_{i}(x)=k\}}\ \text{ with }\ \widetilde{\eta}^{\*}=\frac{1}{\gamma}(\widetilde{a}\_{[n:N]})^{-1}\bigg(\widetilde{\mu}\_{[n:N]}+\frac{\gamma-{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}\widetilde{\mu}\_{[n:N]}}{{\bf 1}^{\top}(\widetilde{a}\_{[n:N]})^{-1}{\bf 1}}{\bf 1}\bigg), |  |
|  |  |  |
| --- | --- | --- |
|  | c∗​(t,w)=e−βγ​t​f​(t;ζ)​w.\displaystyle c^{\*}(t,w)=e^{-\frac{\beta}{\gamma}t}f(t;\zeta)w. |  |

## References

* [1]

  Adrian D. Banner and Raouf Ghomrasni.
  Local times of ranked continuous semimartingales.
  Stochastic Process. Appl., 118(7):1244–1253, 2008.
* [2]

  E. Robert Fernholz.
  Stochastic portfolio theory, volume 48 of Applications of
  Mathematics (New York).
  Springer-Verlag, New York, 2002.
  Stochastic Modelling and Applied Probability.
* [3]

  David Itkin and Martin Larsson.
  Calibrated rank volatility stabilized models for large equity
  markets.
  arXiv preprint arXiv:2403.04674, 2024.
* [4]

  David Itkin and Martin Larsson.
  Open markets and hybrid Jacobi processes.
  Ann. Appl. Probab., 34(3):2940–2985, 2024.
* [5]

  Ioannis Karatzas and Donghan Kim.
  Open markets.
  Math. Finance, 31(4):1111–1161, 2021.
* [6]

  N. V. Krylov.
  Controlled diffusion processes, volume 14 of Applications
  of Mathematics.
  Springer-Verlag, New York-Berlin, 1980.
  Translated from the Russian by A. B. Aries.
* [7]

  Robert C. Merton.
  Lifetime portfolio selection under uncertainty: The continuous-time
  case.
  The Review of Economics and Statistics, 51(3):247–257, 1969.
* [8]

  Jiagang Ren and Jing Wu.
  Probabilistic approach for nonlinear partial differential equations
  and stochastic partial differential equations with Neumann boundary
  conditions.
  J. Math. Anal. Appl., 477(1):1–40, 2019.
* [9]

  Daniel W. Stroock and S. R. Srinivasa Varadhan.
  Multidimensional diffusion processes, volume 233 of Grundlehren der Mathematischen Wissenschaften.
  Springer-Verlag, Berlin-New York, 1979.
* [10]

  Hiroshi Tanaka.
  Stochastic differential equations with reflecting boundary condition
  in convex regions.
  Hiroshima Math. J., 9(1):163–177, 1979.