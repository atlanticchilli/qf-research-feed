---
authors:
- Jou-Hua Lai
- Mykhaylo Shkolnikov
- H. Mete Soner
doc_id: arxiv:2512.17702v1
family_id: arxiv:2512.17702
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Relative arbitrage problem under eigenvalue lower bounds
url_abs: http://arxiv.org/abs/2512.17702v1
url_html: https://arxiv.org/html/2512.17702v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jou-Hua Lai, Mykhaylo Shkolnikov and H. Mete Soner
ORFE Department
  
Princeton University
  
Princeton, NJ 08544
[jhlai@princeton.edu](mailto:jhlai@princeton.edu%20) 
Department of Mathematical Sciences and Center for Nonlinear Analysis
  
Carnegie Mellon University
  
Pittsburgh, PA 15213
[mshkolni@gmail.com](mailto:mshkolni@gmail.com)
ORFE Department
  
Princeton University
  
Princeton, NJ 08544
[soner@princeton.edu](mailto:soner@princeton.edu)

(Date: December 19, 2025)

###### Abstract.

We give a new formulation of the relative arbitrage problem from stochastic portfolio theory that asks for a time horizon beyond which arbitrage relative to the market exists in all “sufficiently volatile” markets. In our formulation, “sufficiently volatile” is interpreted as a lower bound on an ordered eigenvalue of the instantaneous covariation matrix, a quantity that has been studied extensively in the empirical finance literature. Upon framing the problem in the language of stochastic optimal control, we characterize the time horizon in question through the unique upper semicontinuous viscosity solution of a fully nonlinear elliptic partial differential equation (PDE). In a special case, this PDE amounts to the arrival time formulation of the Ambrosio-Soner co-dimension mean curvature flow. Beyond the setting of stochastic portfolio theory, the stochastic optimal control problem is analyzed for arbitrary compact, possibly non-convex, domains, thanks to a boundedness assumption on the instantaneous covariation matrix.

###### Key words and phrases:

Mean curvature flow, nonlinear elliptic PDE, portfolio domination, relative arbitrage, stochastic optimal control, stochastic portfolio theory, sufficient volatility, viscosity solutions

###### 2020 Mathematics Subject Classification:

91G10, 93E20, 49L25, 53E10

M. Shkolnikov is partially supported by the National Science Foundation grant DMS-2342349. H. M. Soner is partially supported by the National Science Foundation grant DMS-2406762.

## 1. Introduction

In [[Fer02](https://arxiv.org/html/2512.17702v1#bib.bibx11), Section 3.3], Fernholz has introduced the concept of portfolio domination, now more commonly referred to as relative arbitrage, to rigorously capture the notion of “beating the market”. More specifically, consider a market with d≥2d\geq 2 assets whose vector μ:=(μ1,μ2,…,μd)\mu:=(\mu\_{1},\mu\_{2},\ldots,\mu\_{d}) of market weights (i.e., market capitalizations as fractions of the total market capitalization) constitutes a continuous semimartingale with respect to some stochastic basis. A predictable μ\mu-integrable process θ\theta is called a trading strategy. We refer to Vθ:=θ⊤​μ:=∑i=1dθi​μiV^{\theta}:=\theta^{\top}\mu:=\sum\_{i=1}^{d}\theta\_{i}\,\mu\_{i} as the value process of θ\theta relative to the market and only consider self-financing trading strategies, meaning:

|  |  |  |  |
| --- | --- | --- | --- |
| (1.1) |  | Vθ​(t)=Vθ​(0)+∫0tθ​(s)⊤​dμ​(s),t≥0.V^{\theta}(t)=V^{\theta}(0)+\int\_{0}^{t}\theta(s)^{\top}\,\mathrm{d}\mu(s),\quad t\geq 0. |  |

Taking the market (i.e., the trading strategy (1,1,…,1)(1,1,\ldots,1)) as the benchmark, we can state the definition of relative arbitrage from the seminal monograph by Fernholz and Karatzas ([[KF09](https://arxiv.org/html/2512.17702v1#bib.bibx19), Definition 6.1]) as follows.

###### Definition 1.1.

A trading strategy θ\theta is called a relative arbitrage over a time horizon [0,T][0,T] if its value process VθV^{\theta} relative to the market satisfies:

1. (a)

   Vθ≥0V^{\theta}\geq 0 almost surely,
2. (b)

   Vθ​(T)≥Vθ​(0)V^{\theta}(T)\geq V^{\theta}(0) almost surely,
3. (c)

   Vθ​(T)>Vθ​(0)V^{\theta}(T)>V^{\theta}(0) with positive probability.

The terms ‘trading strategy’, ‘value process’, ‘self-financing’, and ‘arbitrage’ used above
take on their customary meaning when one starts from a market without a bank account and employs the value of the portfolio continuously investing according to the market weights (‘market portfolio’) as the numéraire. The latter is emphasized by the term ‘relative (to the market)’.

A central problem of stochastic portfolio theory, going back to the foundational work [[Fer02](https://arxiv.org/html/2512.17702v1#bib.bibx11)] by Fernholz, is to identify classes of markets that admit relative arbitrages over suitable time horizons [0,T][0,T]. In particular, it is proven in [[Fer02](https://arxiv.org/html/2512.17702v1#bib.bibx11), Example 3.3.3] that every market in which the smallest eigenvalue of the underlying assets’ instantaneous covariation matrix is bounded away from 0 and the largest market weight is bounded away from 11 admits a relative arbitrage over all long enough time horizons [0,T][0,T]. Surprisingly, the existence of relative arbitrages for the same kind of markets has been shown to hold over any non-trivial time horizon in [[FKK05](https://arxiv.org/html/2512.17702v1#bib.bibx13)]. This phenomenon, now known as short-term relative arbitrage, has been demonstrated in [[FK05](https://arxiv.org/html/2512.17702v1#bib.bibx12)] also for the so-called volatility-stabilized markets. We refer further to [[KR17](https://arxiv.org/html/2512.17702v1#bib.bibx21)], [[Vov18](https://arxiv.org/html/2512.17702v1#bib.bibx32)], [[Cuc19](https://arxiv.org/html/2512.17702v1#bib.bibx9)], [[RX19](https://arxiv.org/html/2512.17702v1#bib.bibx25)], [[KK20](https://arxiv.org/html/2512.17702v1#bib.bibx20)], [[Itk25](https://arxiv.org/html/2512.17702v1#bib.bibx17)] for various extensions of these findings.

The practically important distinction between relative arbitrage over long enough time horizons and short-term relative arbitrage naturally prompted the following question (see [[BF08](https://arxiv.org/html/2512.17702v1#bib.bibx2), Section 4]). Does every sufficiently volatile market, in the sense of

|  |  |  |  |
| --- | --- | --- | --- |
| (1.2) |  | ∑i=1d1μi​(t)​d​⟨μi⟩​(t)d​t≥C>0,t≥0\sum\_{i=1}^{d}\frac{1}{\mu\_{i}(t)}\,\frac{\mathrm{d}{\langle\mu\_{i}\rangle}(t)}{\mathrm{d}t}\geq C>0,\quad t\geq 0 |  |

– a variant of the key assumption behind the construction in [[Fer02](https://arxiv.org/html/2512.17702v1#bib.bibx11), Example 3.3.3] highlighted in [[FK05](https://arxiv.org/html/2512.17702v1#bib.bibx12), Section 3]111Note that the left-hand side in ([1.2](https://arxiv.org/html/2512.17702v1#S1.E2 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is precisely the ‘excess growth rate’ in [[FK05](https://arxiv.org/html/2512.17702v1#bib.bibx12), display (3.1)]., admit a short-term relative arbitrage, and not only relative arbitrages over long enough time horizons? In another surprising twist, this question has been answered negatively in [[FKR18](https://arxiv.org/html/2512.17702v1#bib.bibx14), Section 6]. Hence, the focus has shifted to finding the smallest T∗>0T^{\*}>0 such that a relative arbitrage over the time horizon [0,T][0,T] is possible for any T>T∗T>T^{\*} in every sufficiently volatile market, usually referred to as the relative arbitrage problem.

The relative arbitrage problem appears intractable at first glance, but two remarkable insights by Larsson and Ruf (see [[LR21](https://arxiv.org/html/2512.17702v1#bib.bibx22)]) have allowed them to characterize T∗T^{\*} when the sufficient volatility condition ([1.2](https://arxiv.org/html/2512.17702v1#S1.E2 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is replaced by

|  |  |  |  |
| --- | --- | --- | --- |
| (1.3) |  | ∑i=1d⟨μi⟩​(t)≥t,t≥0\sum\_{i=1}^{d}\langle\mu\_{i}\rangle(t)\geq t,\quad t\geq 0 |  |

(a prominent variant of ([1.2](https://arxiv.org/html/2512.17702v1#S1.E2 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")), see, e.g., [[KR17](https://arxiv.org/html/2512.17702v1#bib.bibx21), Example 5.5] and apply a time change). Firstly, [[LR21](https://arxiv.org/html/2512.17702v1#bib.bibx22)] uses the Fundamental Theorem of Asset Pricing to express T∗T^{\*} through the value function of a stochastic optimal control problem. Secondly, [[LR21](https://arxiv.org/html/2512.17702v1#bib.bibx22)] identifies the Hamilton-Jacobi-Bellman equation associated with the latter as the arrival time formulation of the minimum curvature flow, a geometric flow akin to the celebrated mean curvature flow (see [[Mul56](https://arxiv.org/html/2512.17702v1#bib.bibx24)], [[Bra78](https://arxiv.org/html/2512.17702v1#bib.bibx3)], [[Hui84](https://arxiv.org/html/2512.17702v1#bib.bibx16)]), on the probability simplex. The arrival time formulation of the minimum curvature flow on the probability simplex turns out to have a unique viscosity solution that eventually characterizes T∗T^{\*} (see [[LR21](https://arxiv.org/html/2512.17702v1#bib.bibx22), Theorem 5.1]). This resolves the relative arbitrage problem under the sufficient volatility condition ([1.3](https://arxiv.org/html/2512.17702v1#S1.E3 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")).

In the setting of [[LR21](https://arxiv.org/html/2512.17702v1#bib.bibx22)], the process of market weights μ\mu
free of relative arbitrage over the time horizon [0,T∗][0,T^{\*}] is expected to have an instantaneous covariation matrix (d​⟨μi,μj⟩​(t)d​t)1≤i,j≤d\big(\frac{\mathrm{d}\langle\mu\_{i},\mu\_{j}\rangle(t)}{\mathrm{d}t}\big)\_{1\leq i,j\leq d} generically of rank 11 (cf. [[LR24](https://arxiv.org/html/2512.17702v1#bib.bibx23), discussion following Remark 1.4]). At the same time, while instantaneous covariation matrices of large asset universes are commonly estimated with factor models in the empirical finance literature (see [[JOP+23](https://arxiv.org/html/2512.17702v1#bib.bibx18), Section 8] for a concise overview) and the number of factors used – equal to the number of dominant eigenvalues reliably estimated – is indeed much smaller than dd, this number tends to be much larger than 11 (e.g., 2020 for d=238d=238 in [[JOP+23](https://arxiv.org/html/2512.17702v1#bib.bibx18), Figure 8.1]). For this reason, we amend the sufficient volatility condition ([1.3](https://arxiv.org/html/2512.17702v1#S1.E3 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) to

|  |  |  |  |
| --- | --- | --- | --- |
| (1.4) |  | λ(n−k)​(d​⟨μi,μj⟩​(t)d​t)1≤i,j≤d≥1,a.e. ​t≥0\lambda\_{(n-k)}\bigg(\frac{\mathrm{d}\langle\mu\_{i},\mu\_{j}\rangle(t)}{\mathrm{d}t}\bigg)\_{1\leq i,j\leq d}\geq 1,\quad\text{a.e. }t\geq 0 |  |

where n:=d−1n:=d-1, kk is any fixed element of {1,2,…,n−1}\{1,2,\ldots,n-1\}, and λ(n−k)\lambda\_{(n-k)} refers to the (n−k)(n-k)-largest eigenvalue. A situation such as in [[JOP+23](https://arxiv.org/html/2512.17702v1#bib.bibx18), Figure 8.1] then has n=237n=237 and k=217k=217 for example. To obtain a positive constant other than 11 on the right-hand side of ([1.4](https://arxiv.org/html/2512.17702v1#S1.E4 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")), it suffices to apply a simple time change throughout.

The “null hypothesis” ([1.4](https://arxiv.org/html/2512.17702v1#S1.E4 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is not closed with respect to the convergence in distribution of continuous processes because the lower bound of ([1.4](https://arxiv.org/html/2512.17702v1#S1.E4 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is not preserved under convex combinations of instantaneous covariation matrices. Therefore, we convexify ([1.4](https://arxiv.org/html/2512.17702v1#S1.E4 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) (cf. Lemma [2.1](https://arxiv.org/html/2512.17702v1#S2.Thmthm1 "Lemma 2.1. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds") below):

|  |  |  |  |
| --- | --- | --- | --- |
| (1.5) |  | Πm​(d​⟨μi,μj⟩​(t)d​t)1≤i,j≤d≥m−kform=k+1,k+2,…,n,a.e. ​t≥0,\Pi\_{m}\bigg(\frac{\mathrm{d}\langle\mu\_{i},\mu\_{j}\rangle(t)}{\mathrm{d}t}\bigg)\_{1\leq i,j\leq d}\geq m-k\quad\text{for}\quad m=k+1,\,k+2,\,\ldots,\,n,\quad\text{a.e. }t\geq 0, |  |

where Πm​(a):=inf{tr​(a​P):P2=P,tr​(P)=m}\Pi\_{m}(a):=\inf\{\text{tr}(aP)\!:P^{2}=P,\,\text{tr}(P)=m\} and tr stands for the trace of a square matrix. Hence, we study the relative arbitrage problem under the sufficient volatility condition ([1.5](https://arxiv.org/html/2512.17702v1#S1.E5 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) together with the technical condition
λ(1)​(d​⟨μi,μj⟩​(t)d​t)1≤i,j≤d≤L\lambda\_{(1)}\big(\frac{\mathrm{d}\langle\mu\_{i},\mu\_{j}\rangle(t)}{\mathrm{d}t}\big)\_{1\leq i,j\leq d}\leq L, a.e. ​t≥0\text{a.e. }t\geq 0 for some fixed L≥1L\geq 1. The latter may be chosen large enough to accommodate a confidence interval around an empirical estimate of λ(1)​(d​⟨μi,μj⟩d​t)1≤i,j≤d\lambda\_{(1)}\big(\frac{\mathrm{d}\langle\mu\_{i},\mu\_{j}\rangle}{\mathrm{d}t}\big)\_{1\leq i,j\leq d}. The compactness of the resulting set of instantaneous covariation matrices allows us to establish the semicontinuity of the value function and the dynamic programming principle in the ensuing stochastic optimal control problem.

To characterize T∗T^{\*}, we begin as in [[LR21](https://arxiv.org/html/2512.17702v1#bib.bibx22), Section 5]. More specifically, we apply a linear transformation UU mapping the probability simplex isometrically onto a polytope K⊂ℝnK\subset\mathbb{R}^{n}. Then, an application of the Fundamental Theorem of Asset Pricing as in [[LR21](https://arxiv.org/html/2512.17702v1#bib.bibx22), proof of Theorem 3.1] yields the representation T∗=v​(U​μ​(0))T^{\*}=v(U\mu(0)), where

|  |  |  |  |
| --- | --- | --- | --- |
| (1.6) |  | v​(x):=supP∈𝒫xP​-ess​infτK;v(x):=\sup\_{\mathrm{P}\in\mathcal{P}\_{x}}\mathrm{P}\text{-ess}\inf\tau\_{K}\,; |  |

𝒫x\mathcal{P}\_{x} is the set of probability measures on Ω:=C​([0,∞),ℝn)\Omega:=C([0,\infty),\mathbb{R}^{n}), equipped with the Borel σ\sigma-algebra for the topology of locally uniform convergence, under which the coordinate process XX is a martingale starting from xx and

|  |  |  |  |
| --- | --- | --- | --- |
| (1.7) |  | Πm​(d​⟨Xi,Xj⟩​(t)d​t)1≤i,j≤n≥m−kform=k+1,k+2,…,n,a.e. ​t≥0,λ(1)​(d​⟨Xi,Xj⟩​(t)d​t)1≤i,j≤n≤L,a.e. ​t≥0\begin{split}&\Pi\_{m}\bigg(\frac{\mathrm{d}\langle X\_{i},X\_{j}\rangle(t)}{\mathrm{d}t}\bigg)\_{1\leq i,j\leq n}\geq m-k\quad\text{for}\quad m=k+1,\,k+2,\,\ldots,\,n,\quad\text{a.e. }t\geq 0,\\ &\lambda\_{(1)}\bigg(\frac{\mathrm{d}\langle X\_{i},X\_{j}\rangle(t)}{\mathrm{d}t}\bigg)\_{1\leq i,j\leq n}\leq L,\quad\text{a.e. }t\geq 0\end{split} |  |

hold almost surely; and

|  |  |  |  |
| --- | --- | --- | --- |
| (1.8) |  | τK:=inf{t≥0:X​(t)∉K}.\tau\_{K}:=\inf\big\{t\geq 0:\,X(t)\notin K\big\}. |  |

In words: v​(x)v(x) is the largest, across all martingale laws P∈𝒫x\mathrm{P}\in\mathcal{P}\_{x}, deterministic almost sure lower bound on the exit time from KK. The following theorem characterizes vv, for any compact K⊂ℝnK\subset\mathbb{R}^{n}, and is our main result.

###### Theorem 1.1.

Let n≥2n\geq 2, k∈{1,2,…,n−1}k\in\{1,2,\ldots,n-1\}, and L≥1L\geq 1. Suppose K⊂ℝnK\subset\mathbb{R}^{n} is compact. Then, the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is an upper semicontinuous viscosity solution of the fully nonlinear elliptic partial differential equation
F​(∇v,∇2v)=1F(\nabla v,\nabla^{2}v)=1 on KK with zero boundary condition (see Definition [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmdefn1 "Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds") below) where

|  |  |  |  |
| --- | --- | --- | --- |
| (1.9) |  | F​(p,M):=inf{−12​tr​(M​a):a⪰0,a​p=0,λ(n−k)​(a)≥1,λ(1)​(a)≤L}.F(p,M):=\inf\bigg\{\!-\frac{1}{2}\mathrm{tr}(Ma):\,a\succeq 0,\,ap=0,\,\lambda\_{(n-k)}(a)\geq 1,\,\lambda\_{(1)}(a)\leq L\bigg\}. |  |

Suppose, in addition, that there are Tι:ℝn→ℝnT\_{\iota}\!:\mathbb{R}^{n}\to\mathbb{R}^{n}, ι∈(1,2]\iota\in(1,2], each given by a composition of a rotation, a dilation and a translation, and satisfying K⊂Tι​(K)∘K\subset\accentset{\circ}{T\_{\iota}(K)}, for which limι↓1Tι=I\lim\_{\iota\downarrow 1}T\_{\iota}=I. (Here, II is the identity map on ℝn\mathbb{R}^{n}.) Then, the upper semicontinuous viscosity solution of F​(∇v,∇2v)=1F(\nabla v,\nabla^{2}v)=1 on KK with zero boundary condition is unique.

###### Remark 1.1.

1. (a)

   Theorem [1.1](https://arxiv.org/html/2512.17702v1#S1.Thmthm1 "Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds") characterizes, in particular, the solution T∗T^{\*} of the described relative arbitrage problem via the representation T∗=v​(U​μ​(0))T^{\*}=v(U\mu(0)).
2. (b)

   The nonlinearity FF is ‘geometric’, as defined in [[BSS93](https://arxiv.org/html/2512.17702v1#bib.bibx4)], i.e., for any p∈ℝnp\in\mathbb{R}^{n}, symmetric n×nn\times n matrix MM, c1>0c\_{1}>0, and c2∈ℝc\_{2}\in\mathbb{R},

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (1.10) |  | F​(c1​p,c1​M+c2​p​p⊤)=c1​F​(p,M).F(c\_{1}p,c\_{1}M+c\_{2}pp^{\top})=c\_{1}F(p,M). |  |

   Parabolic equations with such nonlinearities appear in weak formulations of geometric flows, and the corresponding viscosity theory was first developed in [[CGG91](https://arxiv.org/html/2512.17702v1#bib.bibx6), [ES91](https://arxiv.org/html/2512.17702v1#bib.bibx10), [Son93](https://arxiv.org/html/2512.17702v1#bib.bibx27)] for the classical mean curvature flow, and then extended in [[BSS93](https://arxiv.org/html/2512.17702v1#bib.bibx4), [AS96](https://arxiv.org/html/2512.17702v1#bib.bibx1)].
3. (c)

   When L=1L=1, the partial differential equation F​(∇v,∇2v)=1F(\nabla v,\nabla^{2}v)=1 with zero boundary condition becomes the arrival time formulation of a co-dimension mean curvature flow from [[AS96](https://arxiv.org/html/2512.17702v1#bib.bibx1)]. For a related but different stochastic representation of these geometric flows we refer to [[ST03](https://arxiv.org/html/2512.17702v1#bib.bibx31)].
4. (d)

   In view of the right-hand side of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")), it is natural to conjecture that the value function vv does not depend on LL, at least when KK is convex. We were not able to show this and leave it as a tantalizing open problem.

The remainder of the paper is structured as follows. In Section [2](https://arxiv.org/html/2512.17702v1#S2 "2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds"), we show the upper semicontinuity of the value function vv, as well as a dynamic programming principle it satisfies. In Subsections [3.1](https://arxiv.org/html/2512.17702v1#S3.SS1 "3.1. Subsolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds") and [3.2](https://arxiv.org/html/2512.17702v1#S3.SS2 "3.2. Supersolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds") of Section [3](https://arxiv.org/html/2512.17702v1#S3 "3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"), we establish the viscosity subsolution and supersolution properties of vv, respectively. Section [4](https://arxiv.org/html/2512.17702v1#S4 "4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds") is then devoted to the uniqueness of the upper semicontinuous viscosity solution under the additional assumption in Theorem [1.1](https://arxiv.org/html/2512.17702v1#S1.Thmthm1 "Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds"), finishing the proof of the latter. Finally, Section [5](https://arxiv.org/html/2512.17702v1#S5 "5. Continuity of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds") examines the continuity of the value function vv, particularly in the case that KK is a polytope as in the setting of stochastic portfolio theory.

Acknowledgement. The authors would like to thank Martin Larsson and Johannes Ruf for many enlightening discussions on the subject of the paper.

## 2. Properties of the value function

The main result of this section (Proposition [2.4](https://arxiv.org/html/2512.17702v1#S2.Thmthm4 "Proposition 2.4. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) addresses properties of the value function vv from ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")), including the dynamic programming principle. We start with a series of lemmas pertaining to the sets 𝒫x\mathcal{P}\_{x}. Throughout we write 𝕊+n\mathbb{S}^{n}\_{+} for the set of n×nn\times n symmetric positive semidefinite matrices. The first lemma demonstrates that the set of instantaneous covariation matrices defined by ([1.5](https://arxiv.org/html/2512.17702v1#S1.E5 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is the convex hull of the one defined by ([1.4](https://arxiv.org/html/2512.17702v1#S1.E4 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")).

###### Lemma 2.1.

Let n≥2n\geq 2 and k∈{1,2,…,n−1}k\in\{1,2,\ldots,n-1\}. Then, the convex hull of the set {a∈𝕊+n:λ(n−k)​(a)≥1}\{a\in\mathbb{S}\_{+}^{n}\!:\lambda\_{(n-k)}(a)\geq 1\} is

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | {a∈𝕊+n:Πm(a)≥m−k for m=k+1,k+2,…,n}=:A.\big\{a\in\mathbb{S}^{n}\_{+}:\,\Pi\_{m}(a)\geq m-k\text{ for }m=k+1,\,k+2,\,\ldots,\,n\big\}=:A. |  |

Proof. We first observe that the “trace operator” Πm\Pi\_{m}
sums the mm smallest eigenvalues:
Πm​(a)=∑i=n−m+1nλ(i)​(a)\Pi\_{m}(a)=\sum\_{i=n-m+1}^{n}\lambda\_{(i)}(a), a∈𝕊+na\in\mathbb{S}\_{+}^{n}. Let BB be the convex hull of {a∈𝕊+n:λ(n−k)​(a)≥1}\{a\in\mathbb{S}\_{+}^{n}\!:\lambda\_{(n-k)}(a)\geq 1\}. The above formula for Πm​(a)\Pi\_{m}(a) reveals that {a∈𝕊+n:λ(n−k)​(a)≥1}⊆A\{a\in\mathbb{S}\_{+}^{n}\!:\lambda\_{(n-k)}(a)\geq 1\}\subseteq A. Moreover, for any a,a~∈Aa,\widetilde{a}\in A and c∈(0,1)c\in(0,1), the concavity of Πm\Pi\_{m} implies that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | Πm​(c​a+(1−c)​a~)≥c​Πm​(a)+(1−c)​Πm​(a~)≥m−kform=k+1,k+2,…,n.\Pi\_{m}\big(ca+(1-c)\widetilde{a}\big)\geq c\Pi\_{m}(a)+(1-c)\Pi\_{m}(\widetilde{a})\geq m-k\quad\text{for}\quad m=k+1,\,k+2,\,\ldots,\,n. |  |

Thus, AA is convex. Consequently, B⊆AB\subseteq A.

Now, suppose that B⊊AB\subsetneq A. Choose a matrix a¯∈A\overline{a}\in A such that a¯∉B\overline{a}\notin B. By the hyperplane separation theorem in the space of n×nn\times n symmetric matrices with inner product tr​(a​a~)\text{tr}(a\widetilde{a}), there exists an n×nn\times n symmetric matrix MM and c1,c2∈ℝc\_{1},c\_{2}\in\mathbb{R} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | tr​(a¯​M)<c1<c2<tr​(b​M),b∈{a∈𝕊+n:λ(n−k)​(a)≥1}.\text{tr}(\overline{a}M)<c\_{1}<c\_{2}<\text{tr}(bM),\quad b\in\{a\in\mathbb{S}\_{+}^{n}:\,\lambda\_{(n-k)}(a)\geq 1\}. |  |

Since the singleton {a¯}\{\overline{a}\} is compact and {a∈𝕊+n:λ(n−k)​(a)≥1}\{a\in\mathbb{S}\_{+}^{n}\!:\lambda\_{(n-k)}(a)\geq 1\} is closed, the inequalities can be strict. We also observe that necessarily M∈𝕊+nM\in\mathbb{S}^{n}\_{+} because tr​(b​M)\text{tr}(bM) is lower bounded over b∈{a∈𝕊+n:λ(n−k)​(a)≥1}b\in\{a\in\mathbb{S}\_{+}^{n}\!:\lambda\_{(n-k)}(a)\geq 1\}.

Let q1,q2,…,qnq\_{1},\,q\_{2},\,\ldots,\,q\_{n} be orthonormal eigenvectors of MM with eigenvalues λ1,λ2,…,λn\lambda\_{1},\,\lambda\_{2},\,\ldots,\,\lambda\_{n} and Q(1)≥Q(2)≥⋯≥Q(n)≥0Q\_{(1)}\geq Q\_{(2)}\geq\cdots\geq Q\_{(n)}\geq 0 be the ordered sequence of Qi:=tr​(a¯​qi​qi⊤)Q\_{i}:=\mathrm{tr}(\overline{a}q\_{i}q\_{i}^{\top}), i=1, 2,…,ni=1,\,2,\,\ldots,\,n. The property a¯∈A\overline{a}\in A implies that ∑i=1mQ(n−i+1)≥m−k\sum\_{i=1}^{m}Q\_{(n-i+1)}\geq m-k for m=k+1,k+2,…,nm=k+1,\,k+2,\ldots,\,n. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | c1>tr​(a¯​M)=∑i=1nλi​Qi≥∑i=1nλ(i)​Q(n−i+1)≥λ(k+1)​(∑i=1k+1Q(n−i+1))+∑i=k+2nλ(i)​Q(n−i+1)=λ(k+1)+λ(k+1)​(∑i=1k+1Q(n−i+1)−1)+λ(k+2)​Q(n−k−1)+∑i=k+3nλ(i)​Q(n−i+1)≥λ(k+1)+λ(k+2)+λ(k+2)​(∑i=1k+2Q(n−i+1)−2)+∑i=k+3nλ(i)​Q(n−i+1)≥⋯≥∑i=k+1nλ(i)>c2,\begin{split}&\,c\_{1}>\text{tr}(\overline{a}M)=\sum\_{i=1}^{n}\lambda\_{i}\,Q\_{i}\\ &\geq\sum\_{i=1}^{n}\lambda\_{(i)}\,Q\_{(n-i+1)}\\ &\geq\lambda\_{(k+1)}\,\bigg(\sum\_{i=1}^{k+1}Q\_{(n-i+1)}\bigg)+\sum\_{i=k+2}^{n}\lambda\_{(i)}\,Q\_{(n-i+1)}\\ &=\lambda\_{(k+1)}+\lambda\_{(k+1)}\,\bigg(\sum\_{i=1}^{k+1}Q\_{(n-i+1)}-1\bigg)+\lambda\_{(k+2)}\,Q\_{(n-k-1)}+\sum\_{i=k+3}^{n}\lambda\_{(i)}\,Q\_{(n-i+1)}\\ &\geq\lambda\_{(k+1)}+\lambda\_{(k+2)}+\lambda\_{(k+2)}\,\bigg(\sum\_{i=1}^{k+2}Q\_{(n-i+1)}-2\bigg)+\sum\_{i=k+3}^{n}\lambda\_{(i)}\,Q\_{(n-i+1)}\\ &\geq\cdots\geq\sum\_{i=k+1}^{n}\lambda\_{(i)}>c\_{2},\end{split} |  |

which is a contradiction. It follows that B=AB=A. □\Box

The next lemma yields the relative compactness of the sets 𝒫x\mathcal{P}\_{x}.

###### Lemma 2.2.

If S⊂𝕊+nS\subset\mathbb{S}^{n}\_{+} is bounded, then the set of continuous martingale laws under which X​(0)=x∈ℝnX(0)=x\in{\mathbb{R}}^{n} and (d​⟨Xi,Xj⟩​(t)d​t)1≤i,j≤n∈S\big(\frac{\mathrm{d}\langle X\_{i},X\_{j}\rangle(t)}{\mathrm{d}t}\big)\_{1\leq i,j\leq n}\in S, a.e. t≥0t\geq 0 almost surely is relatively compact for the topology of weak convergence. In particular, each 𝒫x\mathcal{P}\_{x} is relatively compact.

Proof. Let P\mathrm{P} be a martingale law as described and C<∞C<\infty be a constant such that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.5) |  | P​(tr​(d​⟨Xi,Xj⟩​(t)d​t)1≤i,j≤n≤C,a.e. ​t≥0)=1.\mathrm{P}\bigg(\text{tr}\bigg(\frac{\mathrm{d}\langle X\_{i},X\_{j}\rangle(t)}{\mathrm{d}t}\bigg)\_{1\leq i,j\leq n}\leq C,\;\text{a.e. }t\geq 0\bigg)=1. |  |

Set ⟨X⟩=(⟨Xi,Xj⟩)1≤i,j≤n\langle X\rangle=(\langle X\_{i},X\_{j}\rangle)\_{1\leq i,j\leq n}, fix s≥0s\geq 0, and define

|  |  |  |  |
| --- | --- | --- | --- |
| (2.6) |  | M​(t)=|X​(t)−X​(s)|2−tr​(⟨X⟩​(t))+tr​(⟨X⟩​(s)),t≥s.M(t)=|X(t)-X(s)|^{2}-\text{tr}\big(\langle X\rangle(t)\big)+\text{tr}\big(\langle X\rangle(s)\big),\quad t\geq s. |  |

Since XX is a martingale, MM is a local martingale on [s,∞)[s,\infty). Moreover, P\mathrm{P}-almost surely, ⟨M⟩​(t)≤4​C​∫st|X​(u)−X​(s)|2​du\langle M\rangle(t)\leq 4C\int\_{s}^{t}|X(u)-X(s)|^{2}\,\mathrm{d}u, t≥st\geq s by Itô’s formula and ([2.5](https://arxiv.org/html/2512.17702v1#S2.E5 "In 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")). Using the Burkholder-Davis-Gundy inequality and again ([2.5](https://arxiv.org/html/2512.17702v1#S2.E5 "In 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")), we find that for all t≥st\geq s,

|  |  |  |
| --- | --- | --- |
|  | 𝔼P​[⟨M⟩​(t)]≤4​C​∫st𝔼P​[|X​(u)−X​(s)|2]​du≤16​C​∫st𝔼P​[tr​(⟨X⟩​(u))−tr​(⟨X⟩​(s))]​du≤16​C2​∫st(u−s)​du=8​C2​(t−s)2.\begin{split}\mathbb{E}^{\mathrm{P}}[\langle M\rangle(t)]\leq 4C\int\_{s}^{t}\mathbb{E}^{\mathrm{P}}\big[|X(u)-X(s)|^{2}\big]\,\mathrm{d}u&\leq 16C\int\_{s}^{t}\mathbb{E}^{\mathrm{P}}\big[\text{tr}\big(\langle X\rangle(u)\big)-\text{tr}\big(\langle X\rangle(s)\big)\big]\,\mathrm{d}u\\ &\leq 16C^{2}\int\_{s}^{t}(u-s)\,\mathrm{d}u=8C^{2}(t-s)^{2}.\end{split} |  |

Another application of the Burkholder-Davis-Gundy inequality and ([2.5](https://arxiv.org/html/2512.17702v1#S2.E5 "In 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) yields

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | 𝔼P​[|X​(t)−X​(s)|4]=𝔼P​[(M​(t)+tr​(⟨X⟩​(t))−tr​(⟨X⟩​(s)))2]≤2​𝔼P​[M​(t)2]+2​𝔼P​[(tr​(⟨X⟩​(t))−tr​(⟨X⟩​(s)))2]≤8​𝔼P​[⟨M⟩​(t)]+2​C2​(t−s)2≤66​C2​(t−s)2,t≥s.\begin{split}\mathbb{E}^{\mathrm{P}}\big[|X(t)-X(s)|^{4}\big]&=\mathbb{E}^{\mathrm{P}}\big[\big(M(t)+\text{tr}\big(\langle X\rangle(t)\big)-\text{tr}\big(\langle X\rangle(s)\big)\big)^{2}\big]\\ &\leq 2\mathbb{E}^{\mathrm{P}}\big[M(t)^{2}\big]+2\mathbb{E}^{\mathrm{P}}\big[\big(\text{tr}\big(\langle X\rangle(t)\big)-\text{tr}\big(\langle X\rangle(s)\big)\big)^{2}\big]\\ &\leq 8\mathbb{E}^{\mathrm{P}}[\langle M\rangle(t)]+2C^{2}(t-s)^{2}\leq 66C^{2}(t-s)^{2},\quad t\geq s.\end{split} |  |

In view of the bound on 𝔼P​[|X​(t)−X​(s)|4]\mathbb{E}^{\mathrm{P}}[|X(t)-X(s)|^{4}], the Kolmogorov continuity criterion (see, e.g., [[RY99](https://arxiv.org/html/2512.17702v1#bib.bibx26), Chapter I, Theorem 2.1]) implies that for any T∈(0,∞)T\in(0,\infty) and α∈(0,14)\alpha\in\big(0,\frac{1}{4}\big), the expectation

|  |  |  |
| --- | --- | --- |
|  | 𝔼P​[(sup0≤s<t≤T|X​(t)−X​(s)||t−s|α)4]\mathbb{E}^{\mathrm{P}}\bigg[\bigg(\sup\_{0\leq s<t\leq T}\frac{|X(t)-X(s)|}{|t-s|^{\alpha}}\bigg)^{4}\bigg] |  |

is bounded uniformly over P\mathrm{P}. This ensures the desired relative compactness, by Prokhorov’s Theorem together with the relative compactness of Hölder balls in C​([0,T],ℝn)C([0,T],\mathbb{R}^{n}) due to the Arzelà–Ascoli Theorem. □\Box

We turn to the compactness of the sets 𝒫x\mathcal{P}\_{x}.

###### Lemma 2.3.

If S⊂𝕊+nS\subset\mathbb{S}^{n}\_{+} is a compact convex set, then the set of continuous martingale laws under which X​(0)=x∈ℝnX(0)=x\in{\mathbb{R}}^{n} and (d​⟨Xi,Xj⟩​(t)d​t)1≤i,j≤n∈S\big(\frac{\mathrm{d}\langle X\_{i},X\_{j}\rangle(t)}{\mathrm{d}t}\big)\_{1\leq i,j\leq n}\in S, a.e. ​t≥0\text{a.e. }t\geq 0 almost surely is compact for the topology of weak convergence. In particular, each 𝒫x\mathcal{P}\_{x} is compact.

Proof. In view of Lemma [2.2](https://arxiv.org/html/2512.17702v1#S2.Thmthm2 "Lemma 2.2. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds"), it suffices to verify that the described set of martingale laws is closed. To this end, let (Pm)m=1∞(\mathrm{P}^{m})\_{m=1}^{\infty} be a sequence of martingale laws as described converging weakly. Upon noting that ⟨X⟩\langle X\rangle is Lipschitz under Pm\mathrm{P}^{m} uniformly over mm, and thus uniformly tight, we apply Prokhorov’s Theorem followed by Skorokhod’s Representation Theorem to find a subsequence of m≥1m\geq 1 and an almost sure instance (Xm,⟨Xm⟩)→(X∞,Y∞)(X^{m},\langle X^{m}\rangle)\to(X^{\infty},Y^{\infty}) of the weakly convergent Pm∘(X,⟨X⟩)−1\mathrm{P}^{m}\circ(X,\langle X\rangle)^{-1}. Then, X∞X^{\infty} and X∞​(X∞)⊤−Y∞X^{\infty}(X^{\infty})^{\top}-Y^{\infty} are martingales thanks to Vitali’s Convergence Theorem, the moment bound ([2.7](https://arxiv.org/html/2512.17702v1#S2.E7 "In 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) and the uniform in mm Lipschitz property of ⟨Xm⟩\langle X^{m}\rangle. In particular, for all 0≤s<t0\leq s<t,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | ⟨X∞⟩​(t)−⟨X∞⟩​(s)t−s=limm→∞⟨Xm⟩​(t)−⟨Xm⟩​(s)t−s=limm→∞1t−s​∫std​⟨Xm⟩​(u)d​u​du\frac{\langle X^{\infty}\rangle(t)-\langle X^{\infty}\rangle(s)}{t-s}=\lim\_{m\to\infty}\frac{\langle X^{m}\rangle(t)-\langle X^{m}\rangle(s)}{t-s}=\lim\_{m\to\infty}\,\frac{1}{t-s}\int\_{s}^{t}\frac{\mathrm{d}\langle X^{m}\rangle(u)}{\mathrm{d}u}\,\mathrm{d}u |  |

lies in SS almost surely, since SS is convex and closed. By Lebesgue’s Fundamental Theorem of Calculus and Differentiation Theorem, d​⟨X∞⟩​(t)d​t∈S\frac{\mathrm{d}\langle X^{\infty}\rangle(t)}{\mathrm{d}t}\in S, a.e. ​t≥0\text{a.e. }t\geq 0 almost surely. □\Box

The compactness of 𝒫x\mathcal{P}\_{x} lets us conclude the subsequent properties of the value function.

###### Proposition 2.4.

Let n≥2n\geq 2, k∈{1,2,…,n−1}k\in\{1,2,\ldots,n-1\}, and L≥1L\geq 1. Suppose K⊂ℝnK\subset\mathbb{R}^{n} is compact. Then, the value function vv from ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is upper semicontinuous on ℝn\mathbb{R}^{n}. Moreover, it satisfies the following dynamic programming principle: For any x∈ℝnx\in\mathbb{R}^{n} and any stopping time θ\theta with respect to the filtration generated by the coordinate process XX,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.9) |  | v​(x)=supP∈𝒫xP​-​ess​inf(θ∧τK+v​(X​(θ))​ 1{θ≤τK}).v(x)=\sup\_{\mathrm{P}\in\mathcal{P}\_{x}}\mathrm{P}\text{-}\mathrm{ess}\inf\,\big(\theta\wedge\tau\_{K}+v(X(\theta))\,\mathbf{1}\_{\{\theta\leq\tau\_{K}\}}\big). |  |

In addition, the supremum in ([2.9](https://arxiv.org/html/2512.17702v1#S2.E9 "In Proposition 2.4. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) is attained by any optimizer P∈𝒫x\mathrm{P}\in\mathcal{P}\_{x} in ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")).

Proof. It suffices to repeat [[LR24](https://arxiv.org/html/2512.17702v1#bib.bibx23), proofs of Proposition 2.2(ii), (iii)] word by word. □\Box

###### Remark 2.1.

The above dynamic programming principle is pointwise and differs from the classical one
of stochastic optimal control which involves an expectation. This extension was first observed in [[ST00](https://arxiv.org/html/2512.17702v1#bib.bibx29)] for stochastic target problems and later used in [[ST02](https://arxiv.org/html/2512.17702v1#bib.bibx30)] for geometric flows.

## 3. Viscosity Solution Property of the Value Function

This section is devoted to verifying that the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is a viscosity solution to F​(∇v,∇2v)=1F(\nabla v,\nabla^{2}v)=1 on KK with zero boundary condition, where

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | F​(p,M):=inf{−12​tr​(M​a):a⪰0,a​p=0,λ(n−k)​(a)≥1,λ(1)​(a)≤L}.F(p,M):=\inf\bigg\{\!-\frac{1}{2}\mathrm{tr}(Ma):\,a\succeq 0,\,ap=0,\,\lambda\_{(n-k)}(a)\geq 1,\,\lambda\_{(1)}(a)\leq L\bigg\}. |  |

We start with the definition of a viscosity solution in our setting, cf. 
[[CL83](https://arxiv.org/html/2512.17702v1#bib.bibx8), [CEL84](https://arxiv.org/html/2512.17702v1#bib.bibx5), [FS06](https://arxiv.org/html/2512.17702v1#bib.bibx15)]. Hereby, we use upper and lower stars to denote the upper and lower semicontinuous envelopes (limε↓0supy:|y−x|<ε\lim\_{\varepsilon\downarrow 0}\sup\_{y:\,|y-x|<\varepsilon} and limε↓0infy:|y−x|<ε\lim\_{\varepsilon\downarrow 0}\inf\_{y:\,|y-x|<\varepsilon}) of a function, respectively. We also write K∘\accentset{\circ}{K} for the interior of KK.

###### Definition 3.1.

Let n≥2n\geq 2, k∈{1,2,…,n−1}k\in\{1,2,\ldots,n-1\}, L≥1L\geq 1, and K⊂ℝnK\subset\mathbb{R}^{n} be compact.

1. (a)

   A bounded function u:K→ℝu\!:K\to\mathbb{R} is a viscosity subsolution of F​(∇u,∇2u)=1F(\nabla u,\nabla^{2}u)=1 in K∘\accentset{\circ}{K} if for any x∈K∘x\in\accentset{\circ}{K} and φ∈C2​(ℝn)\varphi\in C^{2}(\mathbb{R}^{n}) such that (u∗−φ)​(x)=maxK⁡(u∗−φ)(u^{\ast}-\varphi)(x)=\max\_{K}(u^{\ast}-\varphi), it holds

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (3.2) |  | F∗​(∇φ​(x),∇2φ​(x))≤1.F\_{\ast}(\nabla\varphi(x),\nabla^{2}\varphi(x))\leq 1. |  |

   The function uu satisfies the zero boundary condition if for any x∈∂Kx\in\partial K with u∗​(x)>0u^{\ast}(x)>0 and φ∈C2​(ℝn)\varphi\in C^{2}(\mathbb{R}^{n}) such that (u∗−φ)​(x)=maxK⁡(u∗−φ)(u^{\ast}-\varphi)(x)=\max\_{K}(u^{\ast}-\varphi), one has the inequality ([3.2](https://arxiv.org/html/2512.17702v1#S3.E2 "In item a ‣ Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")).
2. (b)

   A bounded function u:K→ℝu\!:K\to\mathbb{R} is a viscosity supersolution of F​(∇u,∇2u)=1F(\nabla u,\nabla^{2}u)=1 in K∘\accentset{\circ}{K} if for any x∈K∘x\in\accentset{\circ}{K} and φ∈C2​(ℝn)\varphi\in C^{2}(\mathbb{R}^{n}) such that (u∗−φ)​(x)=minK⁡(u∗−φ)(u\_{\ast}-\varphi)(x)=\min\_{K}(u\_{\ast}-\varphi), it holds

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (3.3) |  | F∗​(∇φ​(x),∇2φ​(x))≥1.F^{\ast}(\nabla\varphi(x),\nabla^{2}\varphi(x))\geq 1. |  |

   The function uu satisfies the zero boundary condition if for any x∈∂Kx\in\partial K with u∗​(x)<0u\_{\ast}(x)<0 and φ∈C2​(ℝn)\varphi\in C^{2}(\mathbb{R}^{n}) such that (u∗−φ)​(x)=minK⁡(u∗−φ)(u\_{\ast}-\varphi)(x)=\min\_{K}(u\_{\ast}-\varphi), one has the inequality ([3.3](https://arxiv.org/html/2512.17702v1#S3.E3 "In item b ‣ Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")).
3. (c)

   A bounded function u:K→ℝu\!:K\to\mathbb{R} is a viscosity solution of F​(∇u,∇2u)=1F(\nabla u,\nabla^{2}u)=1 on KK with zero boundary condition if it is a viscosity subsolution in K∘\accentset{\circ}{K} satisfying the zero boundary condition and a viscosity supersolution in K∘\accentset{\circ}{K} satisfying the zero boundary condition.

In view of Definition [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmdefn1 "Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"), our first aim is to find F∗​(p,M)F\_{\*}(p,M) and F∗​(p,M)F^{\*}(p,M). To this end, let

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | Mp:={(I−p​p⊤/|p|2)​M​(I−p​p⊤/|p|2)+min⁡(λ(n)​(M),0)​p​p⊤/|p|2,if ​p≠0,M,if ​p=0,M\_{p}:=\begin{cases}\big(I-pp^{\top}/|p|^{2}\big)M\big(I-pp^{\top}/|p|^{2}\big)+\min\big(\lambda\_{(n)}(M),0\big)\,pp^{\top}/|p|^{2},\quad\text{if }\,p\neq 0,\\ M,\quad\text{if }\,p=0,\end{cases} |  |

where II is the n×nn\times n identity matrix. Observing that tr​(M​a)=tr​(Mp​a)\mathrm{tr}(Ma)=\mathrm{tr}(M\_{p}a) for all a⪰0a\succeq 0 with a​p=0ap=0 in the definition ([3.1](https://arxiv.org/html/2512.17702v1#S3.E1 "In 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) of FF, and writing the symmetric MpM\_{p} as a linear combination of outer products, we see that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | F​(p,M)=−12​∑i=1n−k(L​λ(i)​(Mp)​ 1{λ(i)​(Mp)>0}+λ(i)​(Mp)​ 1{λ(i)​(Mp)≤0})−12​∑i=n−k+1nL​λ(i)​(Mp)​ 1{λ(i)​(Mp)>0}.\begin{split}F(p,M)=&-\frac{1}{2}\sum\_{i=1}^{n-k}\big(L\lambda\_{(i)}(M\_{p})\,\mathbf{1}\_{\{\lambda\_{(i)}(M\_{p})>0\}}+\lambda\_{(i)}(M\_{p})\,\mathbf{1}\_{\{\lambda\_{(i)}(M\_{p})\leq 0\}}\big)\\ &-\frac{1}{2}\sum\_{i=n-k+1}^{n}L\lambda\_{(i)}(M\_{p})\,\mathbf{1}\_{\{\lambda\_{(i)}(M\_{p})>0\}}.\end{split} |  |

We are now ready to compute F∗F\_{\*} and F∗F^{\*}.

###### Lemma 3.1.

The nonlinearity FF satisfies F∗=F∗=FF\_{\*}=F^{\*}=F on (ℝn\{0})×𝕊n({\mathbb{R}}^{n}\backslash\{0\})\times\mathbb{S}^{n}, and F∗=FF\_{\*}=F on {0}×𝕊n\{0\}\times\mathbb{S}^{n}. Moreover, for all M∈𝕊nM\in\mathbb{S}^{n},

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | F∗​(0,M)=−12​∑i=2n−k+1(L​λ(i)​(M)​ 1{λ(i)​(M)>0}+λ(i)​(M)​ 1{λ(i)​(M)≤0})−12​∑i=n−k+2nL​λ(i)​(M)​ 1{λ(i)​(M)>0}.\begin{split}F^{\*}(0,M)=&-\frac{1}{2}\sum\_{i=2}^{n-k+1}\big(L\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)>0\}}+\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)\leq 0\}}\big)\\ &-\frac{1}{2}\sum\_{i=n-k+2}^{n}L\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)>0\}}.\end{split} |  |

Proof. The nonlinearity FF is continuous on (ℝn\{0})×𝕊n({\mathbb{R}}^{n}\backslash\{0\})\times\mathbb{S}^{n} thanks to the continuity of (p,M)↦Mp(p,M)\mapsto M\_{p}, Mp↦(λ(1)​(Mp),λ(2)​(Mp),…,λ(n)​(Mp))M\_{p}\mapsto(\lambda\_{(1)}(M\_{p}),\lambda\_{(2)}(M\_{p}),\ldots,\lambda\_{(n)}(M\_{p})), λ↦L​λ​ 1{λ>0}+λ​ 1{λ≤0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}}+\lambda\,\mathbf{1}\_{\{\lambda\leq 0\}} and λ↦L​λ​ 1{λ>0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}}. Hence, F∗=F∗=FF\_{\*}=F^{\*}=F on (ℝn\{0})×𝕊n({\mathbb{R}}^{n}\backslash\{0\})\times\mathbb{S}^{n}.

Next, given any M∈𝕊nM\in\mathbb{S}^{n}, we pick a sequence (pm,Mm)m=1∞(p^{m},M^{m})\_{m=1}^{\infty} in ℝn×𝕊n{\mathbb{R}}^{n}\times\mathbb{S}^{n} converging to (0,M)(0,M) and such that limm→∞F​(pm,Mm)=F∗​(0,M)\lim\_{m\to\infty}F(p^{m},M^{m})=F\_{\*}(0,M). Then, by the definition of FF in ([3.1](https://arxiv.org/html/2512.17702v1#S3.E1 "In 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) and the formula ([3.5](https://arxiv.org/html/2512.17702v1#S3.E5 "In 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) together with the continuity of M↦(λ(1)​(M),λ(2)​(M),…,λ(n)​(M))M\mapsto(\lambda\_{(1)}(M),\lambda\_{(2)}(M),\ldots,\lambda\_{(n)}(M)), λ↦L​λ​ 1{λ>0}+λ​ 1{λ≤0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}}+\lambda\,\mathbf{1}\_{\{\lambda\leq 0\}} and λ↦L​λ​ 1{λ>0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}},

|  |  |  |  |
| --- | --- | --- | --- |
| (3.7) |  | F∗​(0,M)=limm→∞F​(pm,Mm)≥lim supm→∞F​(0,Mm)=F​(0,M).F\_{\*}(0,M)=\lim\_{m\to\infty}F(p^{m},M^{m})\geq\limsup\_{m\to\infty}F(0,M^{m})=F(0,M). |  |

Consequently, F∗​(0,M)=F​(0,M)F\_{\*}(0,M)=F(0,M).

Finally, we compute the upper semicontinuous envelope F∗F^{\*} at (0,M)(0,M).
Let (pm,Mm)m=1∞(p^{m},M^{m})\_{m=1}^{\infty} be a sequence in ℝn×𝕊n{\mathbb{R}}^{n}\times\mathbb{S}^{n} converging to (0,M)(0,M) with limm→∞F​(pm,Mm)=F∗​(0,M)\lim\_{m\to\infty}F(p^{m},M^{m})=F^{\*}(0,M). By the Poincaré Separation Theorem, λ(i)​(Mpmm)≥λ(i+1)​(Mm)\lambda\_{(i)}(M^{m}\_{p^{m}})\geq\lambda\_{(i+1)}(M^{m}), i∈{1,2,…,n−1}i\in\{1,2,\ldots,n-1\}. Since the functions λ↦L​λ​ 1{λ>0}+λ​ 1{λ≤0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}}+\lambda\,\mathbf{1}\_{\{\lambda\leq 0\}} and λ↦L​λ​ 1{λ>0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}} are non-decreasing, applying the formula ([3.5](https://arxiv.org/html/2512.17702v1#S3.E5 "In 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) to F​(pm,Mm)F(p^{m},M^{m}) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (3.8) |  | F∗​(0,M)=limm→∞F​(pm,Mm)≤lim infm→∞(−12∑i=2n−k+1(Lλ(i)(Mm) 1{λ(i)​(Mm)>0}+λ(i)(Mm) 1{λ(i)​(Mm)≤0})−12∑i=n−k+2nLλ(i)(Mm) 1{λ(i)​(Mm)>0})=−12​∑i=2n−k+1(L​λ(i)​(M)​ 1{λ(i)​(M)>0}+λ(i)​(M)​ 1{λ(i)​(M)≤0})−12​∑i=n−k+2nL​λ(i)​(M)​ 1{λ(i)​(M)>0},\begin{split}F^{\*}(0,M)&=\lim\_{m\to\infty}F(p^{m},M^{m})\\ &\leq\liminf\_{m\to\infty}\bigg(\!-\frac{1}{2}\sum\_{i=2}^{n-k+1}\big(L\lambda\_{(i)}(M^{m})\,\mathbf{1}\_{\{\lambda\_{(i)}(M^{m})>0\}}+\lambda\_{(i)}(M^{m})\,\mathbf{1}\_{\{\lambda\_{(i)}(M^{m})\leq 0\}}\big)\\ &\qquad\qquad\;\;\;-\frac{1}{2}\sum\_{i=n-k+2}^{n}L\lambda\_{(i)}(M^{m})\,\mathbf{1}\_{\{\lambda\_{(i)}(M^{m})>0\}}\bigg)\\ &=-\frac{1}{2}\sum\_{i=2}^{n-k+1}\big(L\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)>0\}}+\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)\leq 0\}}\big)\\ &\quad-\frac{1}{2}\sum\_{i=n-k+2}^{n}L\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)>0\}},\end{split} |  |

where the last equality is due to the continuity of M↦(λ(1)​(M),λ(2)​(M),…,λ(n)​(M))M\mapsto(\lambda\_{(1)}(M),\lambda\_{(2)}(M),\ldots,\lambda\_{(n)}(M)), λ↦L​λ​ 1{λ>0}+λ​ 1{λ≤0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}}+\lambda\,\mathbf{1}\_{\{\lambda\leq 0\}} and λ↦L​λ​ 1{λ>0}\lambda\mapsto L\lambda\,\mathbf{1}\_{\{\lambda>0\}}.

To show the reversed inequality, we pick the sequence (q1m,M)m=1∞\big(\frac{q\_{1}}{m},M\big)\_{m=1}^{\infty} converging to (0,M)(0,M), where q1q\_{1} is an eigenvector of MM with the eigenvalue λ(1)​(M)\lambda\_{(1)}(M). Then, writing MM as a linear combination of outer products in the definition ([3.1](https://arxiv.org/html/2512.17702v1#S3.E1 "In 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) of F​(q1m,M)F\big(\frac{q\_{1}}{m},M\big), we infer

|  |  |  |
| --- | --- | --- |
|  | F∗​(0,M)≥lim supm→∞F​(q1m,M)=−12​∑i=2n−k+1(L​λ(i)​(M)​ 1{λ(i)​(M)>0}+λ(i)​(M)​ 1{λ(i)​(M)≤0})−12​∑i=n−k+2nL​λ(i)​(M)​ 1{λ(i)​(M)>0}.\begin{split}F^{\*}(0,M)\geq\limsup\_{m\to\infty}F\Big(\frac{q\_{1}}{m},M\Big)=&-\frac{1}{2}\sum\_{i=2}^{n-k+1}\big(L\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)>0\}}+\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)\leq 0\}}\big)\\ &-\frac{1}{2}\sum\_{i=n-k+2}^{n}L\lambda\_{(i)}(M)\,\mathbf{1}\_{\{\lambda\_{(i)}(M)>0\}}.\end{split} |  |

This concludes the proof of the lemma. □\Box

As a further preparation, we consider the following example.

###### Example 3.1.

Let K:=Br​(0)¯K:=\overline{B\_{r}(0)}, the closed ball of radius r>0r>0 around the origin in ℝn\mathbb{R}^{n}. Then, the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.9) |  | v​(x)=max⁡(r2−|x|2,0)n−k,x∈ℝn.v(x)=\frac{\max(r^{2}-|x|^{2},0)}{n-k},\quad x\in\mathbb{R}^{n}. |  |

###### Proof.

For any x∈Kx\in K and P∈𝒫x\mathrm{P}\in\mathcal{P}\_{x}, Itô’s formula and the first inequality in ([1.7](https://arxiv.org/html/2512.17702v1#S1.E7 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) with m=nm=n yield

|  |  |  |
| --- | --- | --- |
|  | |X​(t)|2=|x|2+2​∫0tX​(s)⊤​dX​(s)+tr​(⟨X⟩​(t))≥|x|2+2​∫0tX​(s)⊤​dX​(s)+(n−k)​t.|X(t)|^{2}=|x|^{2}+2\int\_{0}^{t}X(s)^{\top}\,\mathrm{d}X(s)+\text{tr}\big(\langle X\rangle(t)\big)\geq|x|^{2}+2\int\_{0}^{t}X(s)^{\top}\,\mathrm{d}X(s)+(n-k)t. |  |

Upon evaluating at τK∧t\tau\_{K}\wedge t and taking the expectation, we deduce

|  |  |  |  |
| --- | --- | --- | --- |
| (3.10) |  | P​-ess​infτK≤limt↑∞𝔼​[τK∧t]≤lim inft↑∞𝔼​[|X​(τK∧t)|2]−|x|2n−k≤r2−|x|2n−k.\mathrm{P}\text{-ess}\inf\tau\_{K}\leq\lim\_{t\uparrow\infty}\mathbb{E}[\tau\_{K}\wedge t]\leq\liminf\_{t\uparrow\infty}\frac{\mathbb{E}[|X(\tau\_{K}\wedge t)|^{2}]-|x|^{2}}{n-k}\leq\frac{r^{2}-|x|^{2}}{n-k}. |  |

For the reversed inequality, let x∈K\{0}x\in K\backslash\{0\} and n′:=n−k+1n^{\prime}:=n-k+1. Since the coordinates of xx can be relabeled, we may assume that the first n′n^{\prime} coordinates of xx, denoted by x[n′]x\_{[n^{\prime}]}, satisfy x[n′]≠0x\_{[n^{\prime}]}\neq 0. Consider P∗∈𝒫x\mathrm{P}^{\ast}\in\mathcal{P}\_{x} under which the first n′n^{\prime} coordinates of XX follow

|  |  |  |  |
| --- | --- | --- | --- |
| (3.11) |  | d​X[n′]​(t)=a​(X[n′]​(t))1/2​d​W​(t),\mathrm{d}X\_{[n^{\prime}]}(t)=a(X\_{[n^{\prime}]}(t))^{1/2}\,\mathrm{d}{W(t)}, |  |

where a​(y):=I−y​y⊤/|y|2a(y):=I-yy^{\top}/|y|^{2} when y≠0y\neq 0, a​(0):=Ia(0):=I, and WW is an n′n^{\prime}-dimensional standard Brownian motion. The remaining coordinates of XX are chosen to be constant. Then, a1/2a^{1/2} is continuous on ℝn′∖{0}{\mathbb{R}}^{n^{\prime}}\setminus\{0\}, and a​(y)1/2​y=0a(y)^{1/2}y=0. Thus, for any ε∈(0,|x[n′]|)\varepsilon\in(0,|x\_{[n^{\prime}]}|), by Itô’s formula,

|  |  |  |
| --- | --- | --- |
|  | |X[n′]​(t)|2=|x[n′]|2+(n−k)​t,t≤inf{t′≥0:|X[n′]​(t′)|≤ε}.|X\_{[n^{\prime}]}(t)|^{2}=|x\_{[n^{\prime}]}|^{2}+(n-k)t,\quad t\leq\inf\big\{t^{\prime}\geq 0:\,|X\_{[n^{\prime}]}(t^{\prime})|\leq\varepsilon\big\}. |  |

Consequently, ([3.11](https://arxiv.org/html/2512.17702v1#S3.E11 "In Proof. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) has a global weak solution satisfying |X[n′]​(t)|≥|x[n′]||X\_{[n^{\prime}]}(t)|\geq|x\_{[n^{\prime}]}|, t≥0t\geq 0. In addition, τK=(r2−|x|2)/(n−k)\tau\_{K}=(r^{2}-|x|^{2})/(n-k) almost surely under P∗\mathrm{P}^{\ast}.

For x=0x=0, consider a sequence (xm)m=1∞(x^{m})\_{m=1}^{\infty} in K\{0}K\backslash\{0\} going to xx. By the compactness of 𝒫0\mathcal{P}\_{0} (Lemma [2.3](https://arxiv.org/html/2512.17702v1#S2.Thmthm3 "Lemma 2.3. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")), the associated sequence (Pxm∗)m=1∞(\mathrm{P}^{\ast}\_{x^{m}})\_{m=1}^{\infty} has a subsequence going to a P∗∈𝒫0\mathrm{P}^{\ast}\in\mathcal{P}\_{0}. Then, it holds |X​(t)|2=(n−k)​t|X(t)|^{2}=(n-k)t, t≥0t\geq 0, thus τK=r2/(n−k)\tau\_{K}=r^{2}/(n-k), almost surely under P∗\mathrm{P}^{\ast}.
∎

### 3.1. Subsolution property of the value function

We are now ready to verify that the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) satisfies Definition [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmdefn1 "Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")(a). Since v∗=vv^{\*}=v (Proposition [2.4](https://arxiv.org/html/2512.17702v1#S2.Thmthm4 "Proposition 2.4. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) and F∗=FF\_{\*}=F (Lemma [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmthm1 "Lemma 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")), we may replace v∗v^{\*} by vv and F∗F\_{\*} by FF in Definition [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmdefn1 "Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")(a). Moreover, v​(x)>0v(x)>0 for all x∈K∘x\in\accentset{\circ}{K} by Example [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmexm1 "Example 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"). Thus, we only need to study x∈Kx\in K with v​(x)>0v(x)>0. Let φ∈C2​(ℝn)\varphi\in C^{2}(\mathbb{R}^{n}) be a test function such that φ≥v\varphi\geq v on KK and φ​(x)=v​(x)\varphi(x)=v(x). Since φ\varphi can be replaced by φ+|⋅−x|4\varphi+|\cdot-x|^{4}, we may assume that φ>v\varphi>v on K\{x}K\backslash\{x\}.

We prove the inequality ([3.2](https://arxiv.org/html/2512.17702v1#S3.E2 "In item a ‣ Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) by contradiction. Suppose that F​(∇φ​(x),∇2φ​(x))>1F(\nabla\varphi(x),\nabla^{2}\varphi(x))>1. Then, we let

|  |  |  |  |
| --- | --- | --- | --- |
| (3.12) |  | 𝒜:={a⪰0:λ(n−k)​(a)≥1,λ(1)​(a)≤L}\mathcal{A}:=\big\{a\succeq 0:\,\lambda\_{(n-k)}(a)\geq 1,\,\lambda\_{(1)}(a)\leq L\big\} |  |

and claim the existence of an ε∈(0,v​(x)​(n−k))\varepsilon\in\big(0,\sqrt{v(x)(n-k)}\big) such that for all a∈𝒜a\in\mathcal{A} and all y∈Bε​(x)∩Ky\in B\_{\varepsilon}(x)\cap K, the following implication holds:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.13) |  | 1+12​tr​(a​∇2φ​(y))>0⟹∇φ​(y)⊤​a​∇φ​(y)≥ε.1+\frac{1}{2}\text{tr}\big(a\nabla^{2}\varphi(y)\big)>0\;\;\implies\;\;\nabla\varphi(y)^{\top}a\nabla\varphi(y)\geq\varepsilon. |  |

Indeed, otherwise there would exist a sequence (am,xm)m=1∞(a^{m},x^{m})\_{m=1}^{\infty} in 𝒜×K\mathcal{A}\times K with xm→xx^{m}\to x,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.14) |  | 1+12​tr​(am​∇2φ​(xm))>0,m∈ℕ,and​∇φ​(xm)⊤​am​∇φ​(xm)→0.1+\frac{1}{2}\mathrm{tr}\big(a^{m}\nabla^{2}\varphi(x^{m})\big)>0,\;\;m\in\mathbb{N},\quad\text{and}\;\;\nabla\varphi(x^{m})^{\top}a^{m}\,\nabla\varphi(x^{m})\to 0. |  |

Since 𝒜\mathcal{A} is compact, (am)m=1∞(a^{m})\_{m=1}^{\infty} would admit a subsequence converging to some a∈𝒜a\in\mathcal{A}. Taking m→∞m\to\infty in accordance with that subsequence, we would arrive at

|  |  |  |  |
| --- | --- | --- | --- |
| (3.15) |  | 1+12​tr​(a​∇2φ​(x))≥0and∇φ​(x)⊤​a​∇φ​(x)=0.1+\frac{1}{2}\mathrm{tr}\big(a\nabla^{2}\varphi(x)\big)\geq 0\quad\text{and}\quad\nabla\varphi(x)^{\top}a\nabla\varphi(x)=0. |  |

The latter equation implies a1/2​∇φ​(x)=0a^{1/2}\nabla\varphi(x)=0, thus a​∇φ​(x)=0a\nabla\varphi(x)=0. Therefore, ([3.15](https://arxiv.org/html/2512.17702v1#S3.E15 "In 3.1. Subsolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) contradicts F​(∇φ​(x),∇2φ​(x))>1F(\nabla\varphi(x),\nabla^{2}\varphi(x))>1 (recall the definition ([3.1](https://arxiv.org/html/2512.17702v1#S3.E1 "In 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) of FF).

Next, we fix an optimizer P∈𝒫x\mathrm{P}\in\mathcal{P}\_{x} on the right-hand side of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) and let

|  |  |  |  |
| --- | --- | --- | --- |
| (3.16) |  | θ:=inf{t≥0:X​(t)∉Bε​(x)}∧v​(x).\theta:=\inf\big\{t\geq 0:\,X(t)\notin B\_{\varepsilon}(x)\big\}\wedge v(x). |  |

Thanks to Example [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmexm1 "Example 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"), τK≥v​(x)>ε2/(n−k)≥P​-ess​infτBε​(x)¯\tau\_{K}\geq v(x)>\varepsilon^{2}/(n-k)\geq\mathrm{P}\text{-ess}\inf\tau\_{\,\overline{B\_{\varepsilon}(x)}}. Hence, ∂Bε​(x)∩K≠∅\partial B\_{\varepsilon}(x)\cap K\neq\varnothing and P​(X​(θ)∈∂Bε​(x)∩K)>0\mathrm{P}(X({\theta})\in\partial B\_{\varepsilon}(x)\cap K)>0. Since θ≤τK\theta\leq\tau\_{K} under P\mathrm{P}, the dynamic programming principle (Proposition [2.4](https://arxiv.org/html/2512.17702v1#S2.Thmthm4 "Proposition 2.4. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) together with δ:=min∂Bε​(x)∩K⁡(φ−v)>0\delta:=\min\_{\partial B\_{\varepsilon}(x)\cap K}(\varphi-v)>0 imply

|  |  |  |  |
| --- | --- | --- | --- |
| (3.17) |  | φ​(x)=v​(x)≤t∧θ+v​(X​(t∧θ))≤t∧θ+φ​(X​(t∧θ))−δ​ 1[θ,∞)​(t)​ 1{X​(θ)∈∂Bε​(x)∩K}.\varphi(x)=v(x)\leq t\wedge\theta+v(X(t\wedge\theta))\leq t\wedge\theta+\varphi(X(t\wedge\theta))-\delta\,\mathbf{1}\_{[\theta,\infty)}(t)\,\mathbf{1}\_{\{X(\theta)\in\partial B\_{\varepsilon}(x)\cap K\}}. |  |

We proceed by writing a​(t)a(t), α​(t)\alpha(t), and 𝒮\mathcal{S} for d​⟨X⟩​(t)d​t\frac{\mathrm{d}\langle X\rangle(t)}{\mathrm{d}t}, 1+12​tr​(a​(t)​∇2φ​(X​(t)))1+\frac{1}{2}\text{tr}\big(a(t)\nabla^{2}\varphi(X(t))\big), and

|  |  |  |
| --- | --- | --- |
|  | {s∈[0,θ):1+12​tr​(a​(s)​∇2φ​(X​(s)))>0},\Big\{s\in[0,\theta):1+\frac{1}{2}\text{tr}\big(a(s)\nabla^{2}\varphi(X(s))\big)>0\Big\}, |  |

respectively. Starting from ([3.17](https://arxiv.org/html/2512.17702v1#S3.E17 "In 3.1. Subsolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")), applying Itô’s formula to φ​(X​(t∧θ))\varphi(X(t\wedge\theta)), introducing the auxiliary process

|  |  |  |
| --- | --- | --- |
|  | X~​(t)=X​(t)+ε−1​∫0tα​(s)​a​(s)​∇φ​(X​(s))​ 1𝒮​(s)​ds,t≥0,\widetilde{X}(t)=X(t)+\varepsilon^{-1}\int\_{0}^{t}\alpha(s)\,a(s)\,\nabla\varphi(X(s))\,\mathbf{1}\_{\mathcal{S}}(s)\,\mathrm{d}s,\quad t\geq 0, |  |

and using ([3.13](https://arxiv.org/html/2512.17702v1#S3.E13 "In 3.1. Subsolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")), we deduce

|  |  |  |
| --- | --- | --- |
|  | δ​ 1[θ,∞)​(t)​ 1{X​(θ)∈∂Bε​(x)∩K}\displaystyle\,\delta\,\mathbf{1}\_{[\theta,\infty)}(t)\,\mathbf{1}\_{\{X(\theta)\in\partial B\_{\varepsilon}(x)\cap K\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤t∧θ+φ​(X​(t∧θ))−φ​(x)\displaystyle\leq t\wedge\theta+\varphi(X(t\wedge\theta))-\varphi(x) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0t∧θ∇φ​(X​(s))⊤​dX​(s)+∫0t∧θ1+12​tr​(a​(s)​∇2φ​(X​(s)))​d​s\displaystyle=\int\_{0}^{t\wedge\theta}\nabla\varphi(X(s))^{\top}\,\mathrm{d}X(s)+\int\_{0}^{t\wedge\theta}1+\frac{1}{2}\text{tr}\big(a(s)\nabla^{2}\varphi(X(s))\big)\,\mathrm{d}{s} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫0t∧θ∇φ​(X​(s))⊤​dX​(s)+∫0t∧θα​(s)​ 1𝒮​(s)​ds\displaystyle\leq\int\_{0}^{t\wedge\theta}\nabla\varphi(X(s))^{\top}\,\mathrm{d}X(s)+\int\_{0}^{t\wedge\theta}\alpha(s)\,\mathbf{1}\_{\mathcal{S}}(s)\,\mathrm{d}{s} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0t∧θ∇φ​(X​(s))⊤​dX~​(s)+∫0t∧θα​(s)​(1−ε−1​∇φ​(X​(s))⊤​a​(s)​∇φ​(X​(s)))​ 1𝒮​(s)​ds\displaystyle=\int\_{0}^{t\wedge\theta}\nabla\varphi(X(s))^{\top}\,\mathrm{d}\widetilde{X}(s)+\int\_{0}^{t\wedge\theta}\alpha(s)\big(1-\varepsilon^{-1}\nabla\varphi(X(s))^{\top}a(s)\nabla\varphi(X(s))\big)\,\mathbf{1}\_{\mathcal{S}}(s)\,\mathrm{d}s |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫0t∧θ∇φ​(X​(s))⊤​dX~​(s).\displaystyle\leq\int\_{0}^{t\wedge\theta}\nabla\varphi(X(s))^{\top}\,\mathrm{d}\widetilde{X}(s). |  |

Finally, consider the exponential local martingale ZZ given by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.18) |  | d​Z​(t)Z​(t)=−ε−1​α​(t)​ 1𝒮​(t)​∇φ​(X​(t))⊤​d​X​(t),Z0=1.\frac{\mathrm{d}Z(t)}{Z(t)}=-\varepsilon^{-1}\alpha(t)\,\mathbf{1}\_{\mathcal{S}}(t)\,\nabla\varphi(X(t))^{\top}\,\mathrm{d}{X(t)},\quad Z\_{0}=1. |  |

Due to the boundedness of a​(⋅)a(\cdot) and the boundedness of ∇2φ\nabla^{2}\varphi, ∇φ\nabla\varphi on Bε​(x)B\_{\varepsilon}(x), the process ZZ is well-defined. Itô’s formula shows that Z​(⋅)​∫0⋅∧θ∇φ​(X​(s))⊤​dX~​(s)Z(\cdot)\int\_{0}^{\cdot\wedge\theta}\nabla\varphi(X(s))^{\top}\,\mathrm{d}\widetilde{X}(s) is a nonnegative local martingale, hence a supermartingale. Moreover, θ≤v​(x)\theta\leq v(x) renders the Optional Sampling Theorem applicable and we find via the final display of the previous paragraph:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.19) |  | 0<δ​𝔼​[Z​(θ)​ 1{X​(θ)∈∂Bε​(x)∩K}]≤𝔼​[Z​(θ)​∫0θ∇φ​(X​(s))⊤​dX~​(s)]≤0,0<\delta\mathbb{E}\left[Z(\theta)\,\mathbf{1}\_{\{X(\theta)\in\partial B\_{\varepsilon}(x)\cap K\}}\right]\leq\mathbb{E}\left[Z(\theta)\int\_{0}^{\theta}\nabla\varphi(X(s))^{\top}\,\mathrm{d}\widetilde{X}(s)\right]\leq 0, |  |

a contradiction. The proof of the subsolution property is complete. □\Box

### 3.2. Supersolution property of the value function

Since v≥0v\geq 0, it suffices to check the supersolution inequality ([3.3](https://arxiv.org/html/2512.17702v1#S3.E3 "In item b ‣ Definition 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) for x∈K∘x\in\accentset{\circ}{K}. Fix any x∈K∘x\in\accentset{\circ}{K}, and let φ∈C2​(ℝn)\varphi\in C^{2}(\mathbb{R}^{n}) satisfy φ≤v∗\varphi\leq v\_{\*} on KK and φ​(x)=v∗​(x)\varphi(x)=v\_{\*}(x). Since we can study φ−ε|⋅−x|2\varphi-\varepsilon|\cdot-x|^{2} and then pass to the limit ε↓0\varepsilon\downarrow 0, we may assume φ<v∗\varphi<v\_{\*} on K\{x}K\backslash\{x\} and that ∇2φ​(x)\nabla^{2}\varphi(x) is non-singular. We distinguish two cases: ∇φ​(x)≠0\nabla\varphi(x)\neq 0 and ∇φ​(x)=0\nabla\varphi(x)=0.

Case 1: ∇φ​(x)≠0\nabla\varphi(x)\neq 0. In this case, F∗​(∇φ​(x),∇2φ​(x))=F​(∇φ​(x),∇2φ​(x))F^{\*}(\nabla\varphi(x),\nabla^{2}\varphi(x))=F(\nabla\varphi(x),\nabla^{2}\varphi(x)). We argue by contradiction and suppose that F​(∇φ​(x),∇2φ​(x))<1F(\nabla\varphi(x),\nabla^{2}\varphi(x))<1. Then, there exists an a∈𝒜a\in{\mathcal{A}} with

|  |  |  |  |
| --- | --- | --- | --- |
| (3.20) |  | 1+12​tr​(a​∇2φ​(x))>0anda​∇φ​(x)=0.1+\frac{1}{2}\text{tr}\big(a\nabla^{2}\varphi(x)\big)>0\quad\text{and}\quad a\nabla\varphi(x)=0. |  |

By the Spectral Theorem, a=∑i=1nλ(i)​(a)​qi​qi⊤a=\sum\_{i=1}^{n}\lambda\_{(i)}(a)\,q\_{i}q\_{i}^{\top} where
q1,q2,…,qnq\_{1},\,q\_{2},\,\ldots,\,q\_{n} are orthonormal eigenvectors of aa. We can modify aa such that λ(1)​(a),λ(2)​(a),…,λ(n−k)​(a)∈(1,L)\lambda\_{(1)}(a),\,\lambda\_{(2)}(a),\,\ldots,\,\lambda\_{(n-k)}(a)\in(1,L) and ([3.20](https://arxiv.org/html/2512.17702v1#S3.E20 "In 3.2. Supersolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) remains true. In view of a​∇φ​(x)=0a\nabla\varphi(x)=0, it holds λ(i)​(a)​qi⊤​∇φ​(x)=0\lambda\_{(i)}(a)\,q\_{i}^{\top}\nabla\varphi(x)=0 for all ii. In particular, qi⊤​∇φ​(x)=0q\_{i}^{\top}\nabla\varphi(x)=0 for i=1, 2,…,n−ki=1,\,2,\,\ldots,\,n-k.

Next, we introduce the n×nn\times n matrices

|  |  |  |  |
| --- | --- | --- | --- |
| (3.21) |  | Si=λ(i)​(a)1/2|∇φ​(x)|2​(qi​∇φ​(x)⊤−∇φ​(x)​qi⊤),i=1, 2,…,n.S\_{i}=\frac{\lambda\_{(i)}(a)^{1/2}}{|\nabla\varphi(x)|^{2}}\,\big(q\_{i}\nabla\varphi(x)^{\top}-\nabla\varphi(x)q\_{i}^{\top}\big),\quad i=1,\,2,\,\ldots,\,n. |  |

Observe that Si​∇φ​(x)=λ(i)​(a)1/2​qiS\_{i}\nabla\varphi(x)=\lambda\_{(i)}(a)^{1/2}\,q\_{i}, i=1, 2,…,ni=1,\,2,\,\ldots,\,n. Now, let Σ:ℝn→ℝn×n\Sigma\!:{\mathbb{R}}^{n}\to{\mathbb{R}}^{n\times n} be such that the ii-th column of each Σ​(y)\Sigma(y) is Si​∇φ​(y)S\_{i}\nabla\varphi(y) for i=1, 2,…,ni=1,\,2,\,\ldots,\,n. Then,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.22) |  | Σ​(x)​Σ⊤​(x)=aand1+12​tr​(Σ​(x)​Σ⊤​(x)​∇2φ​(x))=1+12​tr​(a​∇2φ​(x))>0.\Sigma(x)\,\Sigma^{\top}(x)=a\quad\text{and}\quad 1+\frac{1}{2}\text{tr}\big(\Sigma(x)\,\Sigma^{\top}(x)\,\nabla^{2}\varphi(x)\big)=1+\frac{1}{2}\text{tr}\big(a\nabla^{2}\varphi(x)\big)>0. |  |

By the continuity of ∇φ\nabla\varphi, M↦(λ(1)​(M),λ(2)​(M),…,λ(n)​(M))M\mapsto(\lambda\_{(1)}(M),\lambda\_{(2)}(M),\ldots,\lambda\_{(n)}(M)) and ∇2φ\nabla^{2}\varphi, there exists an ε>0\varepsilon>0 with the properties Bε​(x)¯⊂K∘\overline{B\_{\varepsilon}(x)}\subset\accentset{\circ}{K} and that for all y∈Bε​(x)y\in B\_{\varepsilon}(x),

|  |  |  |  |
| --- | --- | --- | --- |
| (3.23) |  | λ(n−k)​(Σ​(y)​Σ⊤​(y))≥1,λ(1)​(Σ​(y)​Σ⊤​(y))≤Land1+12​tr​(Σ​(y)​Σ⊤​(y)​∇2φ​(y))≥0.\lambda\_{(n-k)}\big(\Sigma(y)\,\Sigma^{\top}(y)\big)\geq 1,\quad\lambda\_{(1)}\big(\Sigma(y)\,\Sigma^{\top}(y)\big)\leq L\quad\text{and}\quad 1+\frac{1}{2}\text{tr}\big(\Sigma(y)\,\Sigma^{\top}(y)\,\nabla^{2}\varphi(y)\big)\geq 0. |  |

Further, for y∈Bε​(x)y\in B\_{\varepsilon}(x), consider Py∈𝒫y\mathrm{P}\_{y}\in\mathcal{P}\_{y} under which the coordinate process XX follows the stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
| (3.24) |  | d​X​(t)=∑i=1n(𝟏[0,τBε​(x))​(t)​Si​∇φ​(X​(t))+𝟏[τBε​(x),∞)​(t)​ei)​d​Wi​(t)\mathrm{d}{X(t)}=\sum\_{i=1}^{n}\big(\mathbf{1}\_{[0,\tau\_{B\_{\varepsilon}(x)})}(t)\,S\_{i}\nabla\varphi(X(t))+\mathbf{1}\_{[\tau\_{B\_{\varepsilon}(x)},\infty)}(t)\,e\_{i}\big)\,\mathrm{d}W\_{i}(t) |  |

where e1,e2,…,ene\_{1},\,e\_{2},\,\ldots,\,e\_{n} is the standard basis of ℝn{\mathbb{R}}^{n} and W1,W2,…,WnW\_{1},\,W\_{2},\,\ldots,\,W\_{n} are independent one-dimensional standard Brownian motions. Since ∇φ\nabla\varphi is continuous and d​⟨X⟩​(t)d​t=(Σ​Σ⊤)​(X​(t))\frac{\mathrm{d}\langle X\rangle(t)}{\mathrm{d}t}\!=\!(\Sigma\Sigma^{\top})(X(t)), t∈[0,τBε​(x))t\in[0,\tau\_{B\_{\varepsilon}(x)}), each Py\mathrm{P}\_{y} is a well-defined element of 𝒫y\mathcal{P}\_{y}. By Example [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmexm1 "Example 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"), 𝔼y​[τBε​(x)]<∞\mathbb{E}^{y}[\tau\_{B\_{\varepsilon}(x)}]<\infty and we may apply Itô’s formula to φ​(X​(τBε​(x)))\varphi(X(\tau\_{B\_{\varepsilon}(x)})):

|  |  |  |  |
| --- | --- | --- | --- |
| (3.25) |  | τBε​(x)+φ​(X​(τBε​(x)))=φ​(y)+∑i=1n∫0τBε​(x)∇φ​(X​(t))⊤​Si​∇φ​(X​(t))​dWi​(t)+∫0τBε​(x)1+12​tr​(Σ​(X​(t))​Σ⊤​(X​(t))​∇2φ​(X​(t)))​d​t≥φ​(y),\begin{split}\tau\_{B\_{\varepsilon}(x)}+\varphi(X(\tau\_{B\_{\varepsilon}(x)}))&=\varphi(y)+\sum\_{i=1}^{n}\int\_{0}^{\tau\_{B\_{\varepsilon}(x)}}\nabla\varphi(X(t))^{\top}S\_{i}\nabla\varphi(X(t))\,\mathrm{d}W\_{i}(t)\\ &\quad+\int\_{0}^{\tau\_{B\_{\varepsilon}(x)}}1+\frac{1}{2}\text{tr}\big(\Sigma(X(t))\,\Sigma^{\top}(X(t))\,\nabla^{2}\varphi(X(t))\big)\,\mathrm{d}t\\ &\geq\varphi(y),\end{split} |  |

where we have used the skew-symmetry of the SiS\_{i}’s to conclude that the martingale term vanishes, as well as ([3.23](https://arxiv.org/html/2512.17702v1#S3.E23 "In 3.2. Supersolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")).

Lastly, with δ:=min∂Bε​(x)⁡(v−φ)>0\delta:=\min\_{\partial B\_{\varepsilon}(x)}(v-\varphi)>0, we see from the dynamic programming principle (Proposition [2.4](https://arxiv.org/html/2512.17702v1#S2.Thmthm4 "Proposition 2.4. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) and ([3.25](https://arxiv.org/html/2512.17702v1#S3.E25 "In 3.2. Supersolution property of the value function ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) that

|  |  |  |
| --- | --- | --- |
|  | v​(y)≥Py​-​ess​inf(τBε​(x)+v​(X​(τBε​(x))))≥Py​-​ess​inf(τBε​(x)+φ​(X​(τBε​(x))))+δ≥φ​(y)+δ.v(y)\geq\mathrm{P}\_{y}\text{-}\mathrm{ess}\inf\,\big(\tau\_{B\_{\varepsilon}(x)}+v(X(\tau\_{B\_{\varepsilon}(x)}))\big)\geq\mathrm{P}\_{y}\text{-}\mathrm{ess}\inf\,\big(\tau\_{B\_{\varepsilon}(x)}+\varphi(X(\tau\_{B\_{\varepsilon}(x)}))\big)+\delta\geq\varphi(y)+\delta. |  |

Taking the limit y→xy\to x along a sequence satisfying v​(y)→v∗​(x)v(y)\to v\_{\*}(x), we end up with

|  |  |  |  |
| --- | --- | --- | --- |
| (3.26) |  | φ​(x)=v∗​(x)≥φ​(x)+δ,\varphi(x)=v\_{\*}(x)\geq\varphi(x)+\delta, |  |

which is the desired contradiction.

Case 2: ∇φ​(x)=0\nabla\varphi(x)=0. We aim for a reduction to Case 1. For simplicity of notation, we assume that x=0x=0 and that ∇2φ​(0)\nabla^{2}\varphi(0) is a diagonal matrix, which can be achieved by a translation followed by a rotation. For starters, we construct a sequence (φm)m=1∞(\varphi^{m})\_{m=1}^{\infty} in C2​(ℝn)C^{2}(\mathbb{R}^{n}) such that

1. (a)

   φm​(0)=v∗​(0)\varphi^{m}(0)=v\_{\*}(0) and φm<v∗\varphi^{m}<v\_{\*} on K\{0}K\backslash\{0\}, for all m≥1m\geq 1;
2. (b)

   φm​(y)=v∗​(0)−12​y⊤​Mm​y\varphi^{m}(y)=v\_{\*}(0)-\frac{1}{2}y^{\top}M^{m}y, y∈Bεm​(0)¯y\in\overline{B\_{\varepsilon^{m}}(0)} with a non-singular diagonal MmM^{m} and an εm>0\varepsilon^{m}>0, for all m≥1m\geq 1;
3. (c)

   and limm→∞Mm=∇2φ​(0)\lim\_{m\to\infty}M^{m}=\nabla^{2}\varphi(0).

To this end, for m≥1m\geq 1, we let Mm:=∇2φ​(0)−ε0m​IM^{m}:=\nabla^{2}\varphi(0)-\frac{\varepsilon^{0}}{m}\,I and choose ε0,εm>0\varepsilon^{0},\varepsilon^{m}>0 small enough to ensure the non-singularity of MmM^{m} and φ​(0)+12​y⊤​Mm​y≤φ​(y)\varphi(0)+\frac{1}{2}y^{\top}M^{m}y\leq\varphi(y), y∈B2​εm​(0)¯⊂Ky\in\overline{B\_{2\varepsilon^{m}}(0)}\subset K. Subsequently, we pick φm∈C2​(ℝn)\varphi^{m}\in C^{2}(\mathbb{R}^{n}) satisfying φm​(y)≤φ​(0)+12​y⊤​Mm​y\varphi^{m}(y)\leq\varphi(0)+\frac{1}{2}y^{\top}M^{m}y, y∈B2​εm​(0)¯y\in\overline{B\_{2\varepsilon^{m}}(0)} with φm​(y)=φ​(0)+12​y⊤​Mm​y\varphi^{m}(y)=\varphi(0)+\frac{1}{2}y^{\top}M^{m}y, y∈Bεm​(0)¯y\in\overline{B\_{\varepsilon^{m}}(0)}, as well as φm​(y)<minK⁡v∗\varphi^{m}(y)<\min\_{K}v\_{\*} on ℝn\B2​εm​(0)¯\mathbb{R}^{n}\backslash\overline{B\_{2\varepsilon^{m}}(0)}. Then, φm​(0)=φ​(0)=v∗​(0)\varphi^{m}(0)=\varphi(0)=v\_{\*}(0), (b), and (c) hold by construction. Moreover, for m≥1m\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.27) |  | v∗​(y)−φm​(y)≥v∗​(y)−φ​(y)>0,y∈B2​εm​(0)¯\{0},\displaystyle v\_{\*}(y)-\varphi^{m}(y)\geq v\_{\*}(y)-\varphi(y)>0,\quad y\in\overline{B\_{2\varepsilon^{m}}(0)}\backslash\{0\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (3.28) |  | v∗​(y)−φm​(y)>v∗​(y)−minK⁡v∗≥0,y∈K\B2​εm​(0)¯,\displaystyle v\_{\*}(y)-\varphi^{m}(y)>v\_{\*}(y)-\min\_{K}v\_{\*}\geq 0,\quad y\in K\backslash\overline{B\_{2\varepsilon^{m}}(0)}, |  |

so that (a) also holds.

We proceed to the main line of reasoning. For the desired F∗​(0,∇2φ​(0))≥1F^{\*}(0,\nabla^{2}\varphi(0))\geq 1, it suffices to verify F∗​(0,Mm)≥1F^{\*}(0,M^{m})\geq 1 for each m≥1m\geq 1 thanks to property (c). Thus, we fix an m≥1m\geq 1 and consider auxiliary φm​(⋅;η):ℝn→ℝ\varphi^{m}(\,\cdot\,;\eta):\,\mathbb{R}^{n}\to\mathbb{R}, y↦φm​(y)−y⊤​ηy\mapsto\varphi^{m}(y)-y^{\top}\eta for η∈B1​(0)\eta\in B\_{1}(0). First, suppose that there exists a sequence (ηℓ)ℓ=1∞(\eta^{\ell})\_{\ell=1}^{\infty} such that limℓ→∞|ηℓ|=0\lim\_{\ell\to\infty}|\eta^{\ell}|=0 and ∇φm​(yℓ;ηℓ)≠0\nabla\varphi^{m}(y^{\ell};\eta^{\ell})\neq 0, ℓ≥1\ell\geq 1 where each yℓy^{\ell} is a minimizer of v∗−φm​(⋅;ηℓ)v\_{\*}-\varphi^{m}(\,\cdot\,;\eta^{\ell}) over Bεm​(0)¯\overline{B\_{\varepsilon^{m}}(0)}. Then, yℓ∈Bεm​(0)y^{\ell}\in B\_{\varepsilon^{m}}(0) for all ℓ≥1\ell\geq 1 large enough, and arguing as in Case 1 we would obtain F∗​(∇φm​(yℓ;ηℓ),Mm)≥1F^{\*}(\nabla\varphi^{m}(y^{\ell};\eta^{\ell}),M^{m})\geq 1 for those ℓ\ell. Due to property (a), limℓ→∞yℓ=0\lim\_{\ell\to\infty}y^{\ell}=0, and therefore

|  |  |  |  |
| --- | --- | --- | --- |
| (3.29) |  | limℓ→∞∇φm​(yℓ;ηℓ)=limℓ→∞(∇φm​(yℓ)−ηℓ)=limℓ→∞(Mm​yℓ−ηℓ)=0.\lim\_{\ell\to\infty}\nabla\varphi^{m}(y^{\ell};\eta^{\ell})=\lim\_{\ell\to\infty}\big(\nabla\varphi^{m}(y^{\ell})-\eta^{\ell}\big)=\lim\_{\ell\to\infty}(M^{m}y^{\ell}-\eta^{\ell})=0. |  |

Hence, F∗​(0,Mm)≥1F^{\*}(0,M^{m})\geq 1, as desired.

If a sequence (ηℓ)ℓ=1∞(\eta^{\ell})\_{\ell=1}^{\infty} as above does not exist, there is an η¯>0\overline{\eta}>0 such that for all η∈Bη¯​(0)\eta\in B\_{\overline{\eta}}(0) and all minimizers yηy^{\eta} of v∗−φm​(⋅;η)v\_{\*}-\varphi^{m}(\,\cdot\,;\eta) over Bεm​(0)¯\overline{B\_{\varepsilon^{m}}(0)}, it holds ∇φm​(yη;η)=0\nabla\varphi^{m}(y^{\eta};\eta)=0. We note that ∇φm​(yη;η)=0\nabla\varphi^{m}(y^{\eta};\eta)=0 amounts to Mm​yη=ηM^{m}y^{\eta}=\eta. Recalling that MmM^{m} is diagonal and non-singular, we conclude that {yη:η∈Bη¯​(0)}\{y^{\eta}:\,\eta\in B\_{\overline{\eta}}(0)\} contains an open ball B⊂Bεm​(0)¯B\subset\overline{B\_{\varepsilon^{m}}(0)} around 0. For all yη∈By^{\eta}\in B, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.30) |  | v∗​(yη)−φm​(yη;η)=minBεm​(0)¯⁡(v∗−φm​(⋅;η)),∇φm​(yη;η)=0,∇2φm​(yη;η)=Mm.v\_{\*}(y^{\eta})-\varphi^{m}(y^{\eta};\eta)=\min\_{\overline{B\_{\varepsilon^{m}}(0)}}\,(v\_{\*}-\varphi^{m}(\,\cdot\,;\eta)),\quad\nabla\varphi^{m}(y^{\eta};\eta)=0,\quad\nabla^{2}\varphi^{m}(y^{\eta};\eta)=M^{m}. |  |

Hence, there exists a constant C<∞C<\infty such that |v∗​(y~)−v∗​(y)|≤C​|y~−y|2|v\_{\*}(\widetilde{y})-v\_{\*}(y)|\leq C|\widetilde{y}-y|^{2}, y,y~∈By,\widetilde{y}\in B. Consequently, v∗≡cv\_{\*}\equiv c on BB for some c∈ℝc\in\mathbb{R}. But then, combining the dynamic programming principle (Proposition [2.4](https://arxiv.org/html/2512.17702v1#S2.Thmthm4 "Proposition 2.4. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")) and Example [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmexm1 "Example 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"), we find a δ>0\delta>0 such that v​(y)≥δ+cv(y)\geq\delta+c, y∈12​By\in\frac{1}{2}B. This yields c=v∗​(y)≥δ+cc=v\_{\*}(y)\geq\delta+c, y∈12​By\in\frac{1}{2}B, a contradiction, ruling out the scenario under consideration. The proof of the supersolution property is finished. □\Box

## 4. Uniqueness

In this section, we show the next proposition, which completes the proof of Theorem [1.1](https://arxiv.org/html/2512.17702v1#S1.Thmthm1 "Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds").

###### Proposition 4.1.

In the setting of Theorem [1.1](https://arxiv.org/html/2512.17702v1#S1.Thmthm1 "Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds"), suppose that there are Tι:ℝn→ℝnT\_{\iota}\!:\mathbb{R}^{n}\to\mathbb{R}^{n}, ι∈(1,2]\iota\in(1,2], each given by a composition of a rotation, a dilation and a translation, and satisfying K⊂Tι​(K)∘K\subset\accentset{\circ}{T\_{\iota}(K)}, for which limι↓1Tι=I\lim\_{\iota\downarrow 1}T\_{\iota}=I. Then, the upper semicontinuous viscosity solution of F​(∇v,∇2v)=1F(\nabla v,\nabla^{2}v)=1 on KK with zero boundary condition is unique.

###### Remark 4.1.

Mean curvature flows of any dimension are invariant under rotations, dilations, and translations (used in our assumption). This property is exploited in [[BSS93](https://arxiv.org/html/2512.17702v1#bib.bibx4), [SS93](https://arxiv.org/html/2512.17702v1#bib.bibx28)] to prove several statements about the weak flows. Also, a similar condition without a rotation is used in [[LR24](https://arxiv.org/html/2512.17702v1#bib.bibx23)]. Our assumption is satisfied, for example, by all compact convex K⊂ℝnK\subset\mathbb{R}^{n} with nonempty interior.

The proof of Proposition [4.1](https://arxiv.org/html/2512.17702v1#S4.Thmthm1 "Proposition 4.1. ‣ 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds") relies on the following two theorems of independent interest.

###### Theorem 4.2 (Maximum Principle).

In the general setting of Theorem [1.1](https://arxiv.org/html/2512.17702v1#S1.Thmthm1 "Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds"):

1. (a)

   If uu is an upper semicontinuous viscosity subsolution of F​(∇u,∇2u)=1F(\nabla u,\nabla^{2}u)=1 on KK and ww is a lower semicontinuous viscosity supersolution of F​(∇w,∇2w)=1F(\nabla w,\nabla^{2}w)=1 on KK, then there exists a point x∈∂Kx\in\partial K at which the difference u−wu-w achieves its maximum over KK.
2. (b)

   If, in addition, uu satisfies the zero boundary condition, and ww is a lower semicontinuous viscosity supersolution of F​(∇w,∇2w)=1F(\nabla w,\nabla^{2}w)=1 on some compact K′⊂ℝnK^{\prime}\subset\mathbb{R}^{n} satisfying the zero boundary condition, where K⊂K′∘K\subset\accentset{\circ}{K^{\prime}}, then u≤wu\leq w on KK.

Proof. We show both conclusions in parallel. Therein, we may replace uu by uκ:=κ​uu^{\kappa}:=\kappa u where κ∈(0,1)\kappa\in(0,1), since both (a) and (b) can be obtained by passing to the limit κ↑1\kappa\uparrow 1 at the end. (In the case of (a), any subsequential limit of xκ∈∂Kx^{\kappa}\in\partial K achieves the maximum of u−wu-w over KK thanks to the upper semicontinuity of u−wu-w.) Now, we fix a κ∈(0,1)\kappa\in(0,1), and for ε>0\varepsilon>0 consider the functions

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | Φε​(x,y):=uκ​(x)−w​(y)−ε−1​|x−y|4\Phi^{\varepsilon}(x,y):=u^{\kappa}(x)-w(y)-\varepsilon^{-1}|x-y|^{4} |  |

on K×KK\times K in the case of (a) and on K×K′K\times K^{\prime} in the case of (b). Let (xε,yε)(x^{\varepsilon},y^{\varepsilon}) be a maximizer of Φε\Phi^{\varepsilon}. By compactness, there is a sequence of (xε,yε)(x^{\varepsilon},y^{\varepsilon}) converging to a limit (x0,y0)(x^{0},y^{0}) along a sequence of ε↓0\varepsilon\downarrow 0. The inequality Φε​(xε,yε)≥uκ​(x)−w​(x)\Phi^{\varepsilon}(x^{\varepsilon},y^{\varepsilon})\geq u^{\kappa}(x)-w(x), x∈Kx\in K implies that ε−1​|xε−yε|4≤2​‖uκ‖∞+2​‖w‖∞\varepsilon^{-1}|x^{\varepsilon}-y^{\varepsilon}|^{4}\leq 2\|u^{\kappa}\|\_{\infty}+2\|w\|\_{\infty}, and thus x0=y0x^{0}=y^{0}. Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | uκ​(xε)−w​(yε)≥uκ​(xε)−w​(yε)−ε−1​|xε−yε|4≥uκ​(x)−w​(x),x∈Ku^{\kappa}(x^{\varepsilon})-w(y^{\varepsilon})\geq u^{\kappa}(x^{\varepsilon})-w(y^{\varepsilon})-\varepsilon^{-1}|x^{\varepsilon}-y^{\varepsilon}|^{4}\geq u^{\kappa}(x)-w(x),\quad x\in K |  |

together with the upper semincontinuity of uκu^{\kappa} and −w-w yield (uκ−w)​(x0)=maxK⁡(u−w)(u^{\kappa}-w)(x^{0})=\max\_{K}(u-w).

To obtain (a), it suffices to check that x0∈∂Kx^{0}\in\partial K. Suppose, on the contrary, that x0∈K∘x^{0}\in\accentset{\circ}{K}. Then, xε,yε∈K∘x^{\varepsilon},y^{\varepsilon}\in\accentset{\circ}{K} for ε>0\varepsilon>0 small enough. For such an ε\varepsilon, let ζε​(x,y):=−ε−1​|x−y|4\zeta^{\varepsilon}(x,y):=-\varepsilon^{-1}|x-y|^{4}. If xε=yεx^{\varepsilon}=y^{\varepsilon}, then ∇yζε​(xε,yε)=0\nabla\_{y}\zeta^{\varepsilon}(x^{\varepsilon},y^{\varepsilon})=0 and ∇y2ζε​(xε,yε)=0\nabla^{2}\_{y}\zeta^{\varepsilon}(x^{\varepsilon},y^{\varepsilon})=0. However, yεy^{\varepsilon} minimizes y↦w​(y)−ζε​(xε,y)y\mapsto w(y)-\zeta^{\varepsilon}(x^{\varepsilon},y) over y∈Ky\in K. By the supersolution property of ww at yεy^{\varepsilon}, it follows that 1≤F∗​(0,0)=01\leq F^{\*}(0,0)=0 (recall Lemma [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmthm1 "Lemma 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")), a contradiction. Therefore, xε≠yεx^{\varepsilon}\neq y^{\varepsilon}.

Since xε≠yεx^{\varepsilon}\neq y^{\varepsilon} belong to K∘\accentset{\circ}{K}, the Crandall-Ishii Lemma (see [[CI90](https://arxiv.org/html/2512.17702v1#bib.bibx7)]) yields Mε,Nε∈𝕊nM^{\varepsilon},N^{\varepsilon}\in\mathbb{S}^{n} with Mε⪯NεM^{\varepsilon}\preceq N^{\varepsilon}, F∗​(pε,Mε)≤κF\_{\*}(p^{\varepsilon},M^{\varepsilon})\leq\kappa and F∗​(pε,Nε)≥1F^{\*}(p^{\varepsilon},N^{\varepsilon})\geq 1 where pε:=−∇xζε​(xε,yε)≠0p^{\varepsilon}:=-\nabla\_{x}\zeta^{\varepsilon}(x^{\varepsilon},y^{\varepsilon})\neq 0. By the continuity of FF on (ℝn\{0})×𝕊n({\mathbb{R}}^{n}\backslash\{0\})\times\mathbb{S}^{n} (Lemma [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmthm1 "Lemma 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds")) and its ellipticity, we have:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | κ≥F∗​(pε,Mε)=F​(pε,Mε)≥F​(pε,Nε)=F∗​(pε,Nε)≥1,\kappa\geq F\_{\*}(p^{\varepsilon},M^{\varepsilon})=F(p^{\varepsilon},M^{\varepsilon})\geq F(p^{\varepsilon},N^{\varepsilon})=F^{\*}(p^{\varepsilon},N^{\varepsilon})\geq 1, |  |

which contradicts κ∈(0,1)\kappa\in(0,1). This contradiction proves that x0∈∂Kx^{0}\in\partial K.

To see (b), we recall that uκ​(x)−w​(x)≤Φε​(xε,yε)u^{\kappa}(x)-w(x)\leq\Phi^{\varepsilon}(x^{\varepsilon},y^{\varepsilon}), x∈Kx\in K, ε>0\varepsilon>0. Moreover, for ε>0\varepsilon>0 small enough: yε∈K′∘y^{\varepsilon}\in\accentset{\circ}{K^{\prime}} (because yε→x0∈∂K⊂K′∘y^{\varepsilon}\to x^{0}\in\partial K\subset\accentset{\circ}{K^{\prime}}); xε≠yεx^{\varepsilon}\neq y^{\varepsilon} by the same contradiction argument as above; and if uκu^{\kappa} has the subsolution property at xεx^{\varepsilon}, then the Crandall-Ishii Lemma yields the contradiction ([4.3](https://arxiv.org/html/2512.17702v1#S4.E3 "In 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds")), so xε∈∂Kx^{\varepsilon}\in\partial K and uκ​(xε)≤0u^{\kappa}(x^{\varepsilon})\leq 0. In addition, w≥0w\geq 0 on K′K^{\prime}, as a minimizer yy of ww with w​(y)<0w(y)<0 is impossible in view of the supersolution property of ww at yy (take φ≡0\varphi\equiv 0 and recall that F∗​(0,0)=0F^{\*}(0,0)=0). All in all, Φε​(xε,yε)=uκ​(xε)−w​(yε)−ε−1​|xε−yε|4≤0\Phi^{\varepsilon}(x^{\varepsilon},y^{\varepsilon})=u^{\kappa}(x^{\varepsilon})-w(y^{\varepsilon})-\varepsilon^{-1}|x^{\varepsilon}-y^{\varepsilon}|^{4}\leq 0 for ε>0\varepsilon>0 small enough. □\Box

###### Theorem 4.3 (Comparison Principle).

In the setting of Theorem [1.1](https://arxiv.org/html/2512.17702v1#S1.Thmthm1 "Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds"), suppose that there are Tι:ℝn→ℝnT\_{\iota}\!:\mathbb{R}^{n}\to\mathbb{R}^{n}, ι∈(1,2]\iota\in(1,2], each given by a composition of a rotation, a dilation and a translation, and satisfying K⊂Tι​(K)∘K\subset\accentset{\circ}{T\_{\iota}(K)}, for which limι↓1Tι=I\lim\_{\iota\downarrow 1}T\_{\iota}=I. Then, for any upper semicontinuous viscosity subsolution uu of F​(∇u,∇2u)=1F(\nabla u,\nabla^{2}u)=1 on KK satisfying the zero boundary condition and any lower semicontinuous viscosity supersolution ww of F​(∇w,∇2w)=1F(\nabla w,\nabla^{2}w)=1 on KK satisfying the zero boundary condition, it holds u≤w∗u\leq w^{\*}.

Proof. Consider wι:Tι​(K)→ℝw^{\iota}\!:T\_{\iota}(K)\to\mathbb{R}, x↦w​(Tι−1​x)x\mapsto w(T\_{\iota}^{-1}x). We aim to show that cι2​wιc\_{\iota}^{2}w^{\iota} is a lower semicontinuous viscosity supersolution of F​(∇w,∇2w)=1F(\nabla w,\nabla^{2}w)=1 on Tι​(K)T\_{\iota}(K) satisfying the zero boundary condition, where cι>0c\_{\iota}>0 is the dilation factor in TιT\_{\iota}. To this end, we claim that for any orthogonal n×nn\times n matrix OO and for all (p,M)∈ℝn×𝕊n(p,M)\in\mathbb{R}^{n}\times\mathbb{S}^{n}:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | F​(p,M)=cι2​F​(O⊤​p,cι−2​O⊤​M​O).F(p,M)=c\_{\iota}^{2}\,F(O^{\top}p,\,c\_{\iota}^{-2}O^{\top}MO). |  |

Indeed, let a¯⪰0\overline{a}\succeq 0 with a¯​O⊤​p=0\overline{a}O^{\top}p=0,
λ(n−k)​(a¯)≥1\lambda\_{(n-k)}(\overline{a})\geq 1 and λ(1)​(a¯)≤L\lambda\_{(1)}(\overline{a})\leq L. Then, a:=O​a¯​O⊤⪰0a:=O\overline{a}O^{\top}\succeq 0 satisfies a​p=0ap=0, λ(n−k)​(a)≥1\lambda\_{(n-k)}(a)\geq 1 and λ(1)​(a)≤L\lambda\_{(1)}(a)\leq L. Thus, the definition of FF in ([1.9](https://arxiv.org/html/2512.17702v1#S1.E9 "In Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) yields

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | F​(p,M)≤−12​tr​(M​a)=−cι22​tr​(cι−2​O⊤​M​O​a¯).F(p,M)\leq-\frac{1}{2}\mathrm{tr}(Ma)=-\frac{c\_{\iota}^{2}}{2}\,\mathrm{tr}(c\_{\iota}^{-2}O^{\top}MO\overline{a}). |  |

Taking the infimum over all a¯\overline{a} as described, we arrive at ([4.4](https://arxiv.org/html/2512.17702v1#S4.E4 "In 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds")) with “≤\leq”. Conversely, we can use the obtained inequality with cιc\_{\iota}, OO, and (p,M)(p,M) replaced by cι−1c\_{\iota}^{-1}, O⊤O^{\top}, and (O⊤​p,cι−2​O⊤​M​O)(O^{\top}p,\,c\_{\iota}^{-2}O^{\top}MO), respectively, to find that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | F​(O⊤​p,cι−2​O⊤​M​O)≤cι−2​F​(O​O⊤​p,cι2​O​cι−2​O⊤​M​O​O⊤)=cι−2​F​(p,M).F(O^{\top}p,\,c\_{\iota}^{-2}O^{\top}MO)\leq c\_{\iota}^{-2}\,F(OO^{\top}p,\,c\_{\iota}^{2}Oc\_{\iota}^{-2}O^{\top}MOO^{\top})=c\_{\iota}^{-2}\,F(p,M). |  |

For any test function φ∈C2​(ℝn)\varphi\in C^{2}(\mathbb{R}^{n}), the function φι:ℝn→ℝ\varphi^{\iota}\!:\mathbb{R}^{n}\to\mathbb{R}, x↦cι2​φ​(cι−1​O​x)x\mapsto c\_{\iota}^{2}\,\varphi(c\_{\iota}^{-1}Ox) belongs to C2​(ℝn)C^{2}(\mathbb{R}^{n}) and satisfies ∇φι​(x)=cι​O⊤​∇φ​(cι−1​O​x)\nabla\varphi^{\iota}(x)=c\_{\iota}O^{\top}\nabla\varphi(c\_{\iota}^{-1}Ox), ∇2φι​(x)=O⊤​∇2φ​(cι−1​O​x)​O\nabla^{2}\varphi^{\iota}(x)=O^{\top}\nabla^{2}\varphi(c\_{\iota}^{-1}Ox)O. These formulas, the definition of FF in ([1.9](https://arxiv.org/html/2512.17702v1#S1.E9 "In Theorem 1.1. ‣ 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")), and ([4.4](https://arxiv.org/html/2512.17702v1#S4.E4 "In 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds")) let us conclude that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.7) |  | F​(∇φι​(x),∇2φι​(x))=F​(cι​O⊤​∇φ​(cι−1​O​x),O⊤​∇2φ​(cι−1​O​x)​O)=cι2​F​(O⊤​∇φ​(cι−1​O​x),cι−2​O⊤​∇2φ​(cι−1​O​x)​O)=F​(∇φ​(cι−1​O​x),∇2φ​(cι−1​O​x)).\begin{split}&\;F(\nabla\varphi^{\iota}(x),\nabla^{2}\varphi^{\iota}(x))=F(c\_{\iota}O^{\top}\nabla\varphi(c\_{\iota}^{-1}Ox),\,O^{\top}\nabla^{2}\varphi(c\_{\iota}^{-1}Ox)O)\\ &=c\_{\iota}^{2}\,F(O^{\top}\nabla\varphi(c\_{\iota}^{-1}Ox),\,c\_{\iota}^{-2}O^{\top}\nabla^{2}\varphi(c\_{\iota}^{-1}Ox)O)=F(\nabla\varphi(c\_{\iota}^{-1}Ox),\nabla^{2}\varphi(c\_{\iota}^{-1}Ox)).\end{split} |  |

Since the same transformation rule then also holds for F∗F^{\*}, the lower semicontinuous cι2​wιc\_{\iota}^{2}w^{\iota} is a viscosity supersolution of F​(∇w,∇2w)=1F(\nabla w,\nabla^{2}w)=1 on Tι​(K)T\_{\iota}(K) satisfying the zero boundary condition.

Applying Theorem [4.2](https://arxiv.org/html/2512.17702v1#S4.Thmthm2 "Theorem 4.2 (Maximum Principle). ‣ 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds")(b) we obtain u≤cι2​wιu\leq c\_{\iota}^{2}w^{\iota} on KK. Finally, passing to the limit ι↓1\iota\downarrow 1 we end up with u​(x)≤lim infι↓1wι​(x)=lim infι↓1w​(Tι−1​x)≤w∗​(x)u(x)\leq\liminf\_{\iota\downarrow 1}w^{\iota}(x)=\liminf\_{\iota\downarrow 1}w(T\_{\iota}^{-1}x)\leq w^{\*}(x), x∈Kx\in K. □\Box

We are now ready for the proof of Proposition [4.1](https://arxiv.org/html/2512.17702v1#S4.Thmthm1 "Proposition 4.1. ‣ 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds").

Proof of Proposition [4.1](https://arxiv.org/html/2512.17702v1#S4.Thmthm1 "Proposition 4.1. ‣ 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds"). Let vv, v~\widetilde{v} be upper semicontinuous viscosity solutions of F​(∇v,∇2v)=1F(\nabla v,\nabla^{2}v)=1 on KK satisfying the zero boundary condition. By Theorem [4.3](https://arxiv.org/html/2512.17702v1#S4.Thmthm3 "Theorem 4.3 (Comparison Principle). ‣ 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds") with u:=vu:=v and w:=v~∗w:=\widetilde{v}\_{\*}, it holds v≤(v~∗)∗≤v~∗=v~v\leq(\widetilde{v}\_{\*})^{\*}\leq\widetilde{v}^{\*}=\widetilde{v}. For the same reason, v~≤v\widetilde{v}\leq v. □\Box

## 5. Continuity of the Value Function

In this final section, we discuss continuity properties of the value function vv from ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) assuming that the compact K⊂ℝnK\subset\mathbb{R}^{n} is convex. We start with two simple observations.

###### Proposition 5.1.

Let the compact K⊂ℝnK\subset\mathbb{R}^{n} be convex. Then, the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is continuous on K∘\accentset{\circ}{K}.

Proof. Consider an x∈K∘x\in\accentset{\circ}{K}. For ι∈(0,1)\iota\in(0,1), we define Tι:K→ℝnT\_{\iota}\!:K\to\mathbb{R}^{n}, y↦x+ι​(y−x)y\mapsto x+\iota(y-x). Since x∈K∘x\in\accentset{\circ}{K} and KK is convex, Tι​(K)⊂K∘T\_{\iota}(K)\subset\accentset{\circ}{K}. By arguing as in the proof of Theorem [4.3](https://arxiv.org/html/2512.17702v1#S4.Thmthm3 "Theorem 4.3 (Comparison Principle). ‣ 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds"), we find that vι:Tι​(K)→ℝv^{\iota}\!:T\_{\iota}(K)\to\mathbb{R}, y↦ι2​v​(Tι−1​y)y\mapsto\iota^{2}v(T\_{\iota}^{-1}y) is an upper semicontinuous viscosity solution of F​(∇v,∇2v)=1F(\nabla v,\nabla^{2}v)=1 on Tι​(K)T\_{\iota}(K) satisfying the zero boundary condition. Thus, vι≤v∗v^{\iota}\leq v\_{\*} on Tι​(K)T\_{\iota}(K) by Theorem [4.2](https://arxiv.org/html/2512.17702v1#S4.Thmthm2 "Theorem 4.2 (Maximum Principle). ‣ 4. Uniqueness ‣ Relative arbitrage problem under eigenvalue lower bounds")(b). In particular, for x=Tι​x∈Tι​(K)x=T\_{\iota}x\in T\_{\iota}(K), we have v∗​(x)≥vι​(x)=ι2​v​(x)v\_{\*}(x)\geq v^{\iota}(x)=\iota^{2}v(x). Taking the limit ι↑1\iota\uparrow 1 we arrive at v∗​(x)≥v​(x)=v∗​(x)v\_{\*}(x)\geq v(x)=v^{\*}(x). Hence, vv is continuous on K∘\accentset{\circ}{K}. □\Box

###### Proposition 5.2.

Let the compact K⊂ℝnK\subset\mathbb{R}^{n} be convex. If the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) satisfies v≡0v\equiv 0 on ∂K\partial K, then vv is continuous on KK.

Proof. Since vv is continuous on K∘\accentset{\circ}{K} by Proposition [5.1](https://arxiv.org/html/2512.17702v1#S5.Thmthm1 "Proposition 5.1. ‣ 5. Continuity of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"), it suffices to consider points x∈∂Kx\in\partial K. By the definition of vv in ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")), v≥0v\geq 0, and so v∗≥0v\_{\*}\geq 0. Together with the upper semicontinuity of vv (Proposition [2.4](https://arxiv.org/html/2512.17702v1#S2.Thmthm4 "Proposition 2.4. ‣ 2. Properties of the value function ‣ Relative arbitrage problem under eigenvalue lower bounds")), we get

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | 0=v​(x)=v∗​(x)≥v∗​(x)≥0,0=v(x)=v^{\*}(x)\geq v\_{\*}(x)\geq 0, |  |

i.e., v∗​(x)=v∗​(x)=0v^{\*}(x)=v\_{\*}(x)=0. □\Box

More generally, the boundary behavior of vv is characterized in the next lemma.

###### Lemma 5.3.

Let the compact K⊂ℝnK\subset\mathbb{R}^{n} be convex. For x∈Kx\in K, it holds v​(x)=0v(x)=0 if and only if dim​(Fx)≤n−k\text{dim}(F\_{x})\leq n-k, where FxF\_{x} is the unique face of KK whose relative interior contains xx.

Proof. For simplicity of notation, we assume that x=0x=0, which can be achieved by a translation. Define QQ as the orthogonal projection onto the orthogonal complement of F0F\_{0} and write XX for the coordinate process under an optimal P∈𝒫0\mathrm{P}\in\mathcal{P}\_{0}. Next, we distinguish three cases. If dim​(F0)<n−k\text{dim}(F\_{0})<n-k, then on the one hand, Q​d​X​(t)=0Q\,\mathrm{d}X(t)=0, t≤τF0t\leq\tau\_{F\_{0}}, and consequently 0=tr​(d​⟨Q​X⟩​(t))=tr​(Q​d​⟨X⟩​(t))0=\text{tr}(\mathrm{d}\langle QX\rangle(t))=\text{tr}(Q\,\mathrm{d}\langle X\rangle(t)), t≤τF0t\leq\tau\_{F\_{0}}. On the other hand, by the first line in ([1.7](https://arxiv.org/html/2512.17702v1#S1.E7 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")), tr​(Q​d​⟨X⟩​(t)d​t)≥n−dim​(F0)−k\text{tr}\big(Q\,\frac{\mathrm{d}\langle X\rangle(t)}{\mathrm{d}t}\big)\geq n-\text{dim}(F\_{0})-k, a.e. t≥0t\geq 0. If dim​(F0)<n−k\text{dim}(F\_{0})<n-k, we find that τF0=0\tau\_{F\_{0}}=0. Repeating [[LR24](https://arxiv.org/html/2512.17702v1#bib.bibx23), proof of Lemma 5.2] word by word we conclude that τK=τF0=0\tau\_{K}=\tau\_{F\_{0}}=0.

If dim​(F0)=n−k\text{dim}(F\_{0})=n-k, we consider an open ball Br​(0)B\_{r}(0) in the linear subspace spanned by F0F\_{0} such that F0⊂Br​(0)F\_{0}\subset B\_{r}(0). Then, for any q∈Br​(0)\{0}q\in B\_{r}(0)\backslash\{0\}, the process q⊤​X​(t)|q|\frac{q^{\top}X(t)}{|q|}, t≤τF0t\leq\tau\_{F\_{0}} is a stopped sped-up standard Brownian motion due to the first line in ([1.7](https://arxiv.org/html/2512.17702v1#S1.E7 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")). Since the exit time of the latter from [−r,r][-r,r] has an essential infimum of 0, we have 0=P​-ess​infτF0=P​-ess​infτK0=\mathrm{P}\text{-ess}\inf\tau\_{F\_{0}}=\mathrm{P}\text{-ess}\inf\tau\_{K}.

If dim​(F0)>n−k\text{dim}(F\_{0})>n-k, then there exists a non-trivial closed ball Br​(0)¯\overline{B\_{r}(0)} in the linear subspace spanned by F0F\_{0} such that Br​(0)¯⊂F0\overline{B\_{r}(0)}\subset F\_{0}. Recalling the measure P∗∈𝒫0\mathrm{P}^{\ast}\in\mathcal{P}\_{0} from Example [3.1](https://arxiv.org/html/2512.17702v1#S3.Thmexm1 "Example 3.1. ‣ 3. Viscosity Solution Property of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds"), we obtain v​(0)≥P∗​-ess​infτK=P∗​-ess​infτF0≥P∗​-ess​infτBr​(0)¯=r2/(n−k)>0v(0)\geq\mathrm{P}^{\*}\text{-ess}\inf\tau\_{K}=\mathrm{P}^{\*}\text{-ess}\inf\tau\_{F\_{0}}\geq\mathrm{P}^{\*}\text{-ess}\inf\tau\_{\overline{B\_{r}(0)}}=r^{2}/(n-k)>0. □\Box

Lastly, Lemma [5.3](https://arxiv.org/html/2512.17702v1#S5.Thmthm3 "Lemma 5.3. ‣ 5. Continuity of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds") leads to the following two propositions.

###### Proposition 5.4.

Let the compact K⊂ℝnK\subset\mathbb{R}^{n} be convex. If k=1k=1 or k=2k=2, then the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is continuous on KK.

Proof. It suffices to combine Lemma [5.3](https://arxiv.org/html/2512.17702v1#S5.Thmthm3 "Lemma 5.3. ‣ 5. Continuity of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds") with [[LR24](https://arxiv.org/html/2512.17702v1#bib.bibx23), Lemmas 5.7 and 5.6], whose proofs can be repeated word by word. □\Box

###### Proposition 5.5.

Let K⊂ℝnK\subset\mathbb{R}^{n} be a polytope. Then, the value function vv of ([1.6](https://arxiv.org/html/2512.17702v1#S1.E6 "In 1. Introduction ‣ Relative arbitrage problem under eigenvalue lower bounds")) is continuous on KK.

Proof. We can repeat [[LR24](https://arxiv.org/html/2512.17702v1#bib.bibx23), proof of Corollary 5.9(iii)] word by word, only using our Lemma [5.3](https://arxiv.org/html/2512.17702v1#S5.Thmthm3 "Lemma 5.3. ‣ 5. Continuity of the Value Function ‣ Relative arbitrage problem under eigenvalue lower bounds") instead of their Lemma 5.3. □\Box

## References

* [AS96]

  Luigi Ambrosio and H. Mete Soner, *Level set approach to mean curvature
  flow in arbitrary codimension*, Journal of Differential Geometry 43
  (1996), no. 4, 693–737.
* [BF08]

  Adrian D. Banner and Daniel Fernholz, *Short-term relative arbitrage in
  volatility-stabilized markets*, Annals of Finance 4 (2008), no. 4,
  445–454.
* [Bra78]

  Kenneth A. Brakke, *The motion of a surface by its mean curvature*,
  Mathematical Notes, vol. 20, Princeton University Press, Princeton, NJ, 1978.
  MR 485012
* [BSS93]

  Guy Barles, H. Mete Soner, and Panagiotis E. Souganidis, *Front
  propagation and phase field theory*, SIAM Journal on Control and Optimization
  31 (1993), no. 2, 439–469.
* [CEL84]

  Michael G. Crandall, Lawrence C. Evans, and Pierre-Louis Lions, *Some
  properties of viscosity solutions of Hamilton–Jacobi equations*,
  Transactions of the American Mathematical Society 282 (1984), no. 2,
  487–502.
* [CGG91]

  Yun-Gang Chen, Yoshikazu Giga, and Shun’ichi Goto, *Uniqueness and
  existence of viscosity solutions of generalized mean curvature flow
  equations*, Journal of Differential Geometry 33 (1991), 749–786.
* [CI90]

  Michael G. Crandall and Hitoshi Ishii, *The maximum principle for
  semicontinuous functions*, Differential Integral Equations 3 (1990),
  no. 6, 1001–1014.
* [CL83]

  Michael G. Crandall and Pierre-Louis Lions, *Viscosity solutions of
  Hamilton–Jacobi equations*, Transactions of the American Mathematical
  Society 277 (1983), no. 1, 1–42.
* [Cuc19]

  Christa Cuchiero, *Polynomial processes in stochastic portfolio theory*,
  Stochastic Process. Appl. 129 (2019), no. 5, 1829–1872.
  MR 3944786
* [ES91]

  L. C. Evans and J. Spruck, *Motion of level sets by mean curvature. I*,
  Journal of Differential Geometry 33 (1991), no. 3, 635–681.
* [Fer02]

  E. Robert Fernholz, *Stochastic Portfolio Theory*, Springer, New York,
  NY, 2002.
* [FK05]

  Robert Fernholz and Ioannis Karatzas, *Relative arbitrage in
  volatility-stabilized markets*, Annals of Finance 1 (2005), no. 2,
  149–177.
* [FKK05]

  Robert Fernholz, Ioannis Karatzas, and Constantinos Kardaras, *Diversity
  and relative arbitrage in equity markets*, Finance and Stochastics 9
  (2005), no. 1, 1–27.
* [FKR18]

  E. Robert Fernholz, Ioannis Karatzas, and Johannes Ruf, *Volatility and
  arbitrage*, The Annals of Applied Probability 28 (2018), no. 1,
  378–417.
* [FS06]

  Wendell H. Fleming and H. Mete Soner, *Controlled Markov processes and
  viscosity solutions*, Springer, 2006.
* [Hui84]

  Gerhard Huisken, *Flow by mean curvature of convex surfaces into spheres*,
  J. Differential Geom. 20 (1984), no. 1, 237–266. MR 772132
* [Itk25]

  David Itkin, *Stochastic portfolio theory with price impact*,
  arXiv:2506.07993 (2025).
* [JOP+23]

  Kasper Johansson, Mehmet G. Ogut, Markus Pelger, Thomas Schmelzer, and Stephen
  Boyd, *A Simple Method for Predicting Covariance Matrices of
  Financial Returns*, Foundations and Trends® in Econometrics 12
  (2023), no. 4, 324–407.
* [KF09]

  Ioannis Karatzas and Robert Fernholz, *Stochastic Portfolio Theory: an
  Overview*, Handbook of Numerical Analysis, vol. 15, Elsevier, 2009,
  pp. 89–167.
* [KK20]

  Ioannis Karatzas and Donghan Kim, *Trading strategies generated pathwise
  by functions of market weights*, Finance Stoch. 24 (2020), no. 2,
  423–463. MR 4078340
* [KR17]

  Ioannis Karatzas and Johannes Ruf, *Trading strategies generated by
  Lyapunov functions*, Finance Stoch. 21 (2017), no. 3, 753–787.
* [LR21]

  Martin Larsson and Johannes Ruf, *Relative arbitrage: sharp time horizons
  and motion by curvature*, Math. Finance 31 (2021), no. 3, 885–906.
* [LR24]

  by same author, *Minimum curvature flow and martingale exit times*, Electronic
  Journal of Probability 29 (2024), 1–32.
* [Mul56]

  W. W. Mullins, *Two-dimensional motion of idealized grain boundaries*, J.
  Appl. Phys. 27 (1956), 900–904.
* [RX19]

  Johannes Ruf and Kangjianan Xie, *Generalised Lyapunov functions and
  functionally generated trading strategies*, Appl. Math. Finance 26
  (2019), no. 4, 293–327. MR 4045804
* [RY99]

  Daniel Revuz and Marc Yor, *Continuous Martingales and Brownian
  Motion*, Grundlehren der mathematischen Wissenschaften, vol. 293,
  Springer, Berlin, Heidelberg, 1999 (en).
* [Son93]

  H. Mete Soner, *Motion of a set by the curvature of its boundary*, Journal
  of Differential Equations 101 (1993), no. 2, 313–372.
* [SS93]

  H. Mete Soner and Panagiotis E. Souganidis, *Singularities and uniqueness
  of cylindrically symmetric surfaces moving by mean curvature*, Communications
  in partial differential equations 18 (1993), no. 5-6, 859–894.
* [ST00]

  H. Mete Soner and Nizar Touzi, *Superreplication under gamma constraints*,
  SIAM Journal on Control and Optimization 39 (2000), no. 1, 73–96.
* [ST02]

  by same author, *Dynamic programming for stochastic target problems and geometric
  flows*, Journal of the European Mathematical Society 4 (2002),
  no. 3, 201–236.
* [ST03]

  by same author, *A stochastic representation for mean curvature type geometric
  flows*, Ann. Probab. 31 (2003), no. 3, 1145–1165. MR 1988466
* [Vov18]

  Vladimir Vovk, *Non-stochastic portfolio theory*, Preprint
  arXiv:1712.09108 (2018).