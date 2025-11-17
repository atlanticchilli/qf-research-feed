---
authors:
- Ruslan R. Boyko
doc_id: arxiv:2511.11288v1
family_id: arxiv:2511.11288
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context
  of Option Pricing in the Heston Model
url_abs: http://arxiv.org/abs/2511.11288v1
url_html: https://arxiv.org/html/2511.11288v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ruslan R. Boyko
 Mathematics and Mechanics Department, Lomonosov Moscow State University, Leninskie Gory,
Moscow, 119991,
Russian Federation
[ruslan.boiko@math.msu.ru](mailto:ruslan.boiko@math.msu.ru)

###### Abstract.

In [[1](https://arxiv.org/html/2511.11288v1#bib.bib1)] it was shown that the price of call options in the Heston model is determined in a non-unique way. In this paper, this problem is analyzed from the point of view of the existing mathematical theory of uniqueness classes for degenerate parabolic equations. For the special case of degeneracy, a new example is constructed demonstrating the accuracy of the uniqueness theorem for a solution in the class of functions of sublinear growth at infinity.

###### Key words and phrases:

option valuation problem, Heston model, degenerate parabolic equations, boundary conditions, Täcklind classes.

###### 1991 Mathematics Subject Classification:

35K65 35G16 35A02

## Introduction

In modern financial mathematics, one of the fundamental problems is finding the “fair” price of various derivative financial instruments, especially options, which are used to construct volatility surfaces necessary for standard calibration methods of various derivative pricing models. The uniqueness of the price guarantees the absence of arbitrage opportunities in financial markets. There are many probabilistic approaches to studying the question of price uniqueness in pricing models; however, a definitive and most complete solution to this important problem does not exist.

The problem of existence and uniqueness of option prices in the Heston model is related to the behavior of diffusion coefficients, which can degenerate when approaching the domain’s boundaries. This work will explain the phenomenon of non-uniqueness in the option evaluation problem for the Heston model from the perspective of the theory of boundary value problems for degenerate second-order partial differential equations. Namely, it will be shown that non-uniqueness can arise for two reasons: the absence of necessary boundary conditions, or due to the solution leaving the Tikhonov–Täcklind class.

## 1. Option price in the Heston model

The behavior of the asset in the Heston stochastic volatility model [[2](https://arxiv.org/html/2511.11288v1#bib.bib2)] is described by the system of stochastic differential equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​St=(r−q)​St​d​t+vt​St​d​Wt1d​vt=κ​(θ−vt)​d​t+σ​vt​d​Wt2,\begin{cases}dS\_{t}=(r-q)S\_{t}dt+\sqrt{v\_{t}}S\_{t}dW\_{t}^{1}\\ dv\_{t}=\kappa(\theta-v\_{t})dt+\sigma\sqrt{v\_{t}}dW\_{t}^{2},\end{cases} |  | (1) |

where the volatility process vtv\_{t} is a Cox-Ingersoll-Ross (CIR) process [[3](https://arxiv.org/html/2511.11288v1#bib.bib3)], θ>0\theta>0 is the long-term mean volatility, κ>0\kappa>0 is the rate of mean reversion, σ\sigma is the volatility of volatility, the Brownian motions Wt1,W\_{t}^{1}, Wt2W\_{t}^{2} are correlated with parameter |ρ|≤1|\rho|\leq 1, i.e., d​Wt1​d​Wt2=ρ​d​tdW\_{t}^{1}dW\_{t}^{2}=\rho dt. Additionally, it is assumed that the model is written under the equivalent risk-neutral measure with drift μ=r−q\mu=r-q, where r≥0r\geq 0 is the interest rate and q≥0q\geq 0 is the dividend yield.

The option price with payoff function Φ​(⋅)\Phi(\cdot) in the considered model can be defined as the solution to the following boundary value problem in the domain S,v≥0, and ​0≤t≤T≤∞S,v\geq 0,\text{ and }0\leq t\leq T\leq\infty with a given terminal condition [[2](https://arxiv.org/html/2511.11288v1#bib.bib2)] [[4](https://arxiv.org/html/2511.11288v1#bib.bib4)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | v​S22​VS​S+ρ​σ​v​S​VS​v+v​σ22​Vv​v+(r−q)​S​VS+(κ​(θ−v)−λ​v)​Vv−r​V+Vt=0,\displaystyle\frac{vS^{2}}{2}V\_{SS}+\rho\sigma vSV\_{Sv}+\frac{v\sigma^{2}}{2}V\_{vv}+(r-q)SV\_{S}+(\kappa(\theta-v)-\lambda v)V\_{v}-rV+V\_{t}=0, |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(S,v,T)=Φ​(S,v).\displaystyle V(S,v,T)=\Phi(S,v). |  | (3) |

### 1.1. Correct setting of boundary conditions

Equation ([2](https://arxiv.org/html/2511.11288v1#S1.E2 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) belongs to the class of parabolic equations degenerate on the boundary of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​u=∑i,j=1mai​j​(x)​uxi​xj+∑l=1mbl​(x)​uxl+c​(x)​u=f​(x),\mathcal{L}u=\sum\_{i,j=1}^{m}a\_{ij}(x)u\_{x\_{i}x\_{j}}+\sum\_{l=1}^{m}b\_{l}(x)u\_{x\_{l}}+c(x)u=f(x), |  | (4) |

defined in an open domain 𝒟⊂ℝm\mathcal{D}\subset\mathbb{R}^{m} with regular boundary ∂𝒟\partial\mathcal{D}. Assume that the matrix A​(x)={ai​j​(x)}A(x)=\big\{a\_{ij}(x)\big\} is symmetric, positive semidefinite (i.e., ⟨A​ξ,ξ⟩≥0\langle A\xi,\xi\rangle\geq 0 for any unit vector ξ\xi), and has degeneration points on the boundary ∂𝒟\partial\mathcal{D}, with the coefficient c​(x)<0c(x)<0. A general theory of weak solutions for such equations was constructed in [[5](https://arxiv.org/html/2511.11288v1#bib.bib5)] [[6](https://arxiv.org/html/2511.11288v1#bib.bib6)]. To investigate the correctness of the boundary condition formulation, we introduce the *Fichera function*

|  |  |  |
| --- | --- | --- |
|  | H​(x)=∑i=1m[bi​(x)−∑j=1m(ai​j​(x))xj]​ni,H(x)=\sum\_{i=1}^{m}\Big[b\_{i}(x)-\sum\_{j=1}^{m}\big(a\_{ij}(x)\big)\_{x\_{j}}\Big]n\_{i}, |  |

constructed for points of the set Σ0={x∈∂D∣⟨A​(x)​ν,ν⟩=0}⊂∂D\Sigma^{0}=\big\{x\in\partial D\mid\langle A(x)\nu,\nu\rangle=0\big\}\subset\partial D, where ν\nu denotes the unit normal to the boundary ∂𝒟\partial\mathcal{D} at point xx.

The Fichera function for problem ([2](https://arxiv.org/html/2511.11288v1#S1.E2 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), ([3](https://arxiv.org/html/2511.11288v1#S1.E3 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) has the form

|  |  |  |
| --- | --- | --- |
|  | H​(S,v,t)=((r−q)​S−(v​S+ρ​σ​S2))​n1+(κ​(θ−v)−λ​v−(ρ​σ​v2+σ22))​n2+n3,H(S,v,t)=\left((r-q)S-\Big(vS+\frac{\rho\sigma S}{2}\Big)\right)n\_{1}+\left(\kappa(\theta-v)-\lambda v-\Big(\frac{\rho\sigma v}{2}+\frac{\sigma^{2}}{2}\Big)\right)n\_{2}+n\_{3}, |  |

where 𝐧=(n1,n2,n3)\mathbf{n}=(n\_{1},n\_{2},n\_{3}) defines the inward normal in coordinates (S,v,t)(S,v,t) to the boundary of the domain.

Let us introduce the domains associated with the sign of the Fichera function

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Σ0\displaystyle\Sigma\_{0} | ={x∈Σ0∣H​(x)=0},\displaystyle=\big\{x\in\Sigma^{0}\mid H(x)=0\big\}, | Σ2={x∈Σ0∣H​(x)<0},\displaystyle\Sigma\_{2}=\big\{x\in\Sigma^{0}\mid H(x)<0\big\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Σ1\displaystyle\Sigma\_{1} | ={x∈Σ0∣H​(x)>0},\displaystyle=\big\{x\in\Sigma^{0}\mid H(x)>0\big\}, | Σ3={∂D−Σ0}.\displaystyle\Sigma\_{3}=\big\{\partial D-\Sigma^{0}\big\}. |  |

For ([4](https://arxiv.org/html/2511.11288v1#S1.E4 "In 1.1. Correct setting of boundary conditions ‣ 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), we pose the boundary value problem u=g​ on ​Σ2∪Σ3u=g\text{ on }\Sigma\_{2}\cup\Sigma\_{3}. In [[5](https://arxiv.org/html/2511.11288v1#bib.bib5)], a theorem on the existence of a weak solution applicable to our problem was proved. Namely, assume that for the boundary value problem

> the following conditions hold: c​(y)≤c0<0c(y)\leq c\_{0}<0 in DD, ff is a bounded measurable function on DD, gg is a bounded measurable function on Σ2∪Σ3\Sigma\_{2}\cup\Sigma\_{3}. Then there exists a weak solution to the posed boundary value problem.

Thus, for the correct formulation of the problem, it is necessary to impose a boundary condition on the domain Σ2∪Σ3\Sigma\_{2}\cup\Sigma\_{3}, i.e., at points of non-degeneracy and at points where the Fichera function is negative.

According to Fichera’s theory [[5](https://arxiv.org/html/2511.11288v1#bib.bib5)] [[7](https://arxiv.org/html/2511.11288v1#bib.bib7)], for the well-posedness of the boundary value problem it is necessary to impose a boundary condition at the terminal moment t=Tt=T. Furthermore, if the model parameters do not satisfy the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | k​θ⩾σ22,k\theta\geqslant\frac{\sigma^{2}}{2}, |  | (5) |

then a boundary condition must also be imposed on the boundary v=0v=0 (the moment the volatility trajectory reaches the zero level). This condition is commonly referred to in probability theory as the *Feller condition*.

Thus, under certain conditions on the model parameters, the non-uniqueness of the solution in problem ([2](https://arxiv.org/html/2511.11288v1#S1.E2 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), ([3](https://arxiv.org/html/2511.11288v1#S1.E3 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) occurs due to a missing boundary condition.

Studying the sign of the Fichera function shows that on the boundaries S=0S=0, S=+∞S=+\infty, and v=+∞v=+\infty, imposing a boundary condition is not required. Note that the analysis of the necessity of imposing boundary conditions for the option price equation in the Heston model was carried out in [[7](https://arxiv.org/html/2511.11288v1#bib.bib7)].

## 2. The uniqueness problem in option pricing in the Heston model under the Feller condition

In [[1](https://arxiv.org/html/2511.11288v1#bib.bib1)], an Example 3 showing that the solution to the option pricing problem may be non-unique. For this, a special case of model ([1](https://arxiv.org/html/2511.11288v1#S1.E1 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) was considered:

|  |  |  |
| --- | --- | --- |
|  | {d​St=r​St​d​t+νt​St​d​Ztℚd​νt=σ2​d​t+σ​νt​d​Ztℚ,\begin{cases}dS\_{t}=rS\_{t}dt+\sqrt{\nu\_{t}}S\_{t}dZ^{\mathbb{Q}}\_{t}\\ d\nu\_{t}=\sigma^{2}dt+\sigma\sqrt{\nu\_{t}}dZ^{\mathbb{Q}}\_{t},\end{cases} |  |

where the parameters σ>0,r≥0\sigma>0,r\geq 0 correspond to the characteristics of the volatility process and the drift of the price process, respectively, and ZtℚZ^{\mathbb{Q}}\_{t} is a Wiener process under the risk-neutral measure ℚ\mathbb{Q}.

Equation ([2](https://arxiv.org/html/2511.11288v1#S1.E2 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​S22​VS​S+σ​v​S​VS​v+v​σ22​Vv​v+r​S​VS+σ2​Vv−r​V+Vt\displaystyle\frac{vS^{2}}{2}V\_{SS}+\sigma vSV\_{Sv}+\frac{v\sigma^{2}}{2}V\_{vv}+rSV\_{S}+\sigma^{2}V\_{v}-rV+V\_{t} | =0.\displaystyle=0. |  | (6) |

Note that from the standpoint of Fichera function theory, this equation, as in the general Heston model, requires a condition to be imposed only at the terminal time t=Tt=T (the investigation reduces to examining the sign of the Fichera function on the boundaries). Here, the ”Feller condition,” which previously arose on the boundary v=0v=0, is replaced in the considered problem by the condition σ2−σ22=σ22⩾0\sigma^{2}-\frac{\sigma^{2}}{2}=\frac{\sigma^{2}}{2}\geqslant 0, i.e., imposing a condition on the boundary v=0v=0 is not required.

In [[1](https://arxiv.org/html/2511.11288v1#bib.bib1)], the differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​σ22​Πv​v+σ2​Πv+Πt−r​Π=0\frac{v\sigma^{2}}{2}\Pi\_{vv}+\sigma^{2}\Pi\_{v}+\Pi\_{t}-r\Pi=0 |  | (7) |

with final condition Π​(v,T)=0\Pi(v,T)=0 was considered to prove the non-uniqueness of the solution to problem ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), ([3](https://arxiv.org/html/2511.11288v1#S1.E3 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")). This work shows that the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(v,t)=1v​e−r​(T−t)−2​vσ2​(T−t)\Pi(v,t)=\frac{1}{v}e^{-r(T-t)-\frac{2v}{\sigma^{2}(T-t)}} |  | (8) |

provides a nontrivial solution to this problem. Consequently, if V1​(S,v,t)V\_{1}(S,v,t) denotes the “standard” solution of problem ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), ([3](https://arxiv.org/html/2511.11288v1#S1.E3 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) (e.g., [[2](https://arxiv.org/html/2511.11288v1#bib.bib2)] [[4](https://arxiv.org/html/2511.11288v1#bib.bib4)]), then V2​(S,v,t)=V1​(S,v,t)+Π​(v,t)V\_{2}(S,v,t)=V\_{1}(S,v,t)+\Pi(v,t) also solves the original problem.

Note that solution ([8](https://arxiv.org/html/2511.11288v1#S2.E8 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) is unbounded as v→0v\to 0, and it is natural to assume that to single out a unique solution, restrictions on the behavior of the solution as v→0v\to 0 must be imposed. Below it will be shown how the reason for this kind of non-uniqueness can be explained in terms of classical results of the theory of parabolic equations.

Furthermore, questions concerning the growth restriction of the solution also arise as S→0S\to 0, v→+∞v\to+\infty, S→+∞S\to+\infty. We will also obtain growth conditions for the solution that ensure uniqueness when approaching finite or infinite boundaries.

## 3. Classes of uniqueness in the problem of option valuation in the Heston model

### 3.1. Tikhonov–Täcklind classes (S→∞S\to\infty, v→∞v\to\infty).

The question of identifying uniqueness classes for the Cauchy problem for degenerate parabolic equations was first addressed by E. Holmgren in his 1924 work. The exact uniqueness class for the solution of the Cauchy problem in the context of the heat equation was obtained by A.N. Tikhonov in 1935 in [[8](https://arxiv.org/html/2511.11288v1#bib.bib8)]. It was established that the solution u​(x,t)u(x,t) of the heat equation ut=Δ​uu\_{t}=\Delta u with zero initial condition u​(x,0)=0u(x,0)=0 is unique in the class of functions

|  |  |  |
| --- | --- | --- |
|  | |u​(x,t)|≤B​exp⁡{β​|x|2},β>0,x∈ℝn,t∈[0,T],|u(x,t)|\leq B\exp\{\beta|x|^{2}\},\quad\beta>0,\,x\in\mathbb{R}^{n},\,t\in[0,T], |  |

and Tikhonov constructed an example of a nonzero solution to this Cauchy problem that belonged to a wider class. In 1936, S. Täcklind in [[9](https://arxiv.org/html/2511.11288v1#bib.bib9)] refined Tikhonov’s results by showing that the solution of the Cauchy problem is unique in the class

|  |  |  |
| --- | --- | --- |
|  | |u​(x,t)|≤B​exp⁡{|x|​h​(x)},x∈ℝ,t∈[0,T],|u(x,t)|\leq B\exp\{|x|h(x)\},\quad x\in{\mathbb{R}},\,t\in[0,T], |  |

where h​(⋅)h(\cdot) is a non-decreasing nonnegative function with a divergent integral ∫1+∞d​sh​(x)\int\_{1}^{+\infty}\frac{ds}{h(x)} (this function is commonly called the *Täcklind function*). It was also established that if the latter condition is violated, the solution ceases to be unique.

The works of Tikhonov and Täcklind were successively generalized to broader classes of equations. In particular, Kamynin and Khimchenko in [[10](https://arxiv.org/html/2511.11288v1#bib.bib10)] [[11](https://arxiv.org/html/2511.11288v1#bib.bib11)] [[12](https://arxiv.org/html/2511.11288v1#bib.bib12)] extended the theory to general second-order parabolic equations with nonnegative characteristic form and unbounded coefficients. They proposed a generalized Tikhonov–Täcklind class

|  |  |  |
| --- | --- | --- |
|  | |u​(x,t)|≤C​exp⁡{G​(|x|)​h​(G​(|x|))},G​(s)=∫0sd​xg​(x),|u(x,t)|\leq C\exp\big\{G(|x|)h(G(|x|))\big\},\quad G(s)=\int\_{0}^{s}\frac{dx}{g(x)}, |  |

where g:[0,+∞)→[1,+∞)g\colon[0,+\infty)\to[1,+\infty) is a non-decreasing function of class C1​[0,+∞)C^{1}[0,+\infty), g​(s)≡1g(s)\equiv 1 for s∈[0,1]s\in[0,1] and ∫0+∞d​sg​(s)=∞\int\_{0}^{+\infty}\frac{ds}{g(s)}=\infty.

In [[11](https://arxiv.org/html/2511.11288v1#bib.bib11)], Theorem 1 was proved, which we formulate in a special case that allows its application to our situation. Namely, assume that

> the coefficients of the differential operator
>
> |  |  |  |
> | --- | --- | --- |
> |  | ℒ=∑i,j=1mai​j​(x,t)​∂xi​xj+∑l=1mbl​(x,t)​∂xl+c​(x,t)−∂t,\mathcal{L}=\sum\_{i,j=1}^{m}a\_{ij}(x,t)\partial\_{x\_{i}x\_{j}}+\sum\_{l=1}^{m}b\_{l}(x,t)\partial\_{x\_{l}}+c(x,t)-\partial\_{t}, |  |
>
> in the strip Π​(T)={x∈ℝ, 0⩽t⩽T}\Pi(T)=\{x\in\mathbb{R},\,0\leqslant t\leqslant T\} satisfy the conditions
>
> |  |  |  |
> | --- | --- | --- |
> |  | 0≤A​(x,t;ξ)=∑i,j=1nai​j​(x,t)​ξi​ξj≤k​(|x|),∀|ξ|=1,\displaystyle 0\leq A(x,t;\xi)=\sum\_{i,j=1}^{n}a\_{ij}(x,t)\xi\_{i}\xi\_{j}\leq k(|x|),\quad\forall|\xi|=1, |  |
> |  |  |  |
> | --- | --- | --- |
> |  | 0≤a​(x,t)=(∑i=1nbi2​(x,t))1/2≤g​(|x|)​φ​(G​(|x|)),c​(x,t)≤0,\displaystyle 0\leq a(x,t)=\left(\sum\_{i=1}^{n}b\_{i}^{2}(x,t)\right)^{1/2}\leq g(|x|)\varphi(G(|x|)),\quad c(x,t)\leq 0, |  |
>
> where k​(s)=min⁡{g2​(s),s​g​(s)}k(s)=\min\{g^{2}(s),sg(s)\} for s≥1s\geq 1, and the function u​(x,t)∈C​(Π​(T))∩Cx,t2,1​(Π​(T))u(x,t)\in C(\Pi(T))\cap C\_{x,t}^{2,1}(\Pi(T)) belongs to the generalized Tikhonov–Täcklind class. Then, if ℒ​u=0\mathcal{L}u=0 and u​(x,0)=0u(x,0)=0, then u​(x,t)≡0u(x,t)\equiv 0 in the entire strip Π​(T)\Pi(T).

To find the Tikhonov–Täcklind uniqueness class for equation ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) as S→+∞S\to+\infty and v→+∞v\to+\infty, we perform the substitution x=ln⁡Sx=\ln S. Then equation ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) is rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | v2​Vx​x+σ​v​Vx​v+v​σ22​Vv​v+(r−v2)​Vx+σ2​Vv−r​V+Vt=0.\frac{v}{2}V\_{xx}+\sigma vV\_{xv}+\frac{v\sigma^{2}}{2}V\_{vv}+\left(r-\frac{v}{2}\right)V\_{x}+\sigma^{2}V\_{v}-rV+V\_{t}=0. |  | (9) |

Let us estimate the quadratic and linear coefficients:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤A​(x,v,t;ξ)\displaystyle 0\leq A(x,v,t;\xi) | =v2​ξ12+σ​v​ξ1​ξ2+v​σ22​ξ22≤C1​v,\displaystyle=\frac{v}{2}\xi\_{1}^{2}+\sigma v\xi\_{1}\xi\_{2}+\frac{v\sigma^{2}}{2}\xi\_{2}^{2}\leq C\_{1}v, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤a​(x,v,t)\displaystyle 0\leq a(x,v,t) | =((r−v2)2+(σ2)2)1/2≤C2​v,\displaystyle=\left(\left(r-\frac{v}{2}\right)^{2}+(\sigma^{2})^{2}\right)^{1/2}\leq C\_{2}v, |  |

where C1C\_{1}, C2C\_{2} are constants.
Choose

|  |  |  |
| --- | --- | --- |
|  | g​(s)={1,s∈[0,1−ε]smooth,s∈[1−ε,1+ε)s,s⩾1+εG​(s)=∫0sd​xg​(x)∼C​ln⁡(s),s→+∞,g(s)=\begin{cases}1,&s\in[0,1-\varepsilon]\\ \text{smooth},&s\in[1-\varepsilon,1+\varepsilon)\\ s,&s\geqslant 1+\varepsilon\end{cases}\qquad G(s)=\int\_{0}^{s}\frac{dx}{g(x)}\sim C\ln(s),\,s\to+\infty, |  |

which satisfy the necessary conditions given in [[10](https://arxiv.org/html/2511.11288v1#bib.bib10)] [[11](https://arxiv.org/html/2511.11288v1#bib.bib11)].
Thus, from Theorem 1 in [[10](https://arxiv.org/html/2511.11288v1#bib.bib10)] follows that the uniqueness class as S→∞S\to\infty and v→∞v\to\infty has the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |V​(S,v,t)|⩽C​exp⁡[ln⁡(ln2⁡(S)+v2)⋅h​(ln⁡(ln2⁡(S)+v2))].\displaystyle|V(S,v,t)|\leqslant C\exp\left[\ln\left(\sqrt{\ln^{2}(S)+v^{2}}\right)\cdot h\left(\ln\left(\sqrt{\ln^{2}(S)+v^{2}}\right)\right)\right]. |  | (10) |

### 3.2. Uniqueness class for ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) as S→0S\to 0.

Note that the substitution x=ln⁡Sx=\ln S also allows us to investigate the behavior of the solution as S→0S\to 0, since it reduces the problem to studying the uniqueness class for equation ([9](https://arxiv.org/html/2511.11288v1#S3.E9 "In 3.1. Tikhonov–Täcklind classes (𝑆→∞, 𝑣→∞). ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) as x→−∞x\to-\infty. This equation does not degenerate in the variable xx, so the uniqueness class coincides with the well-known uniqueness class for the heat equation.
Performing the inverse substitution, we see that condition ([10](https://arxiv.org/html/2511.11288v1#S3.E10 "In 3.1. Tikhonov–Täcklind classes (𝑆→∞, 𝑣→∞). ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) also singles out the uniqueness class for equation ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) as S→0S\to 0.

### 3.3. Uniqueness class for ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) as v→0v\to 0.

The question of uniqueness classes in this case is resolved somewhat differently. We could, of course, make the substitution w=1vw=\frac{1}{v} and study the behavior of the solutions of the resulting equation as w→∞w\to\infty, but the theory used above turns out to be inapplicable in this case. Therefore, we will proceed differently and study the behavior of the solution of equation
([7](https://arxiv.org/html/2511.11288v1#S2.E7 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) as v→0v\to 0 within the framework of the theory of degenerate partial differential equations, similar to what was done in [[17](https://arxiv.org/html/2511.11288v1#bib.bib17)].

Note that equation ([7](https://arxiv.org/html/2511.11288v1#S2.E7 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) reduces to the Feller equation [[13](https://arxiv.org/html/2511.11288v1#bib.bib13)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ut=(a​x​u)x​x−((b​x+c)​u)x,u\_{t}=(axu)\_{xx}-((bx+c)u)\_{x}, |  | (11) |

where a,b,ca,b,c are some constants. Namely, performing the substitution x=4σ2​vx=\frac{4}{\sigma^{2}}v and τ=T−t\tau=T-t (assuming r=0r=0) we obtain

|  |  |  |
| --- | --- | --- |
|  | Πτ=2​x​Πx​x+4​Πx,\Pi\_{\tau}=2x\Pi\_{xx}+4\Pi\_{x}, |  |

i.e., a=2,b=0a=2,b=0 and c=4=3−2​α1−α,α=12c=4=\frac{3-2\alpha}{1-\alpha},\alpha=\frac{1}{2}.

In turn, the substitution y=1xy=\frac{1}{x} leads us to the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πτ=2​y3​Πy​y,\Pi\_{\tau}=2y^{3}\Pi\_{yy}, |  | (12) |

with parameter α=32\alpha=\frac{3}{2}. Equation ([12](https://arxiv.org/html/2511.11288v1#S3.E12 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) belongs to the class of equations with power-law degeneracy of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πτ=a​y2​α​Πy​y,α>0,a>0,\Pi\_{\tau}=ay^{2\alpha}\Pi\_{yy},\quad\alpha>0,\,a>0, |  | (13) |

which are closely related to stochastic processes with constant elasticity (CEV) [[14](https://arxiv.org/html/2511.11288v1#bib.bib14)]. It is known that the change of variables

|  |  |  |
| --- | --- | --- |
|  | x=12​a​(1−α)2​y2​(1−α)x=\frac{1}{2a(1-\alpha)^{2}}y^{2(1-\alpha)} |  |

reduces them to the Feller equation ([11](https://arxiv.org/html/2511.11288v1#S3.E11 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) [[14](https://arxiv.org/html/2511.11288v1#bib.bib14)]. For equation ([13](https://arxiv.org/html/2511.11288v1#S3.E13 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) in the case α>1\alpha>1, there also exists a non-uniqueness problem, which was investigated in [[15](https://arxiv.org/html/2511.11288v1#bib.bib15)] from the perspective of the theory of degenerate partial differential equations. Thus, ([12](https://arxiv.org/html/2511.11288v1#S3.E12 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) is a special case of such a problem.

Let us list the results concerning the growth rate of the solution as y→∞y\to\infty that ensure its uniqueness:

1. In [[16](https://arxiv.org/html/2511.11288v1#bib.bib16)] (Theorem 4.8) it is shown that for α≥0\alpha\geq 0,

> if the initial condition Π​(x,0)=g​(x)\Pi(x,0)=g(x) in ([7](https://arxiv.org/html/2511.11288v1#S2.E7 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) has (strictly) sublinear growth at infinity, then the solution to problem ([7](https://arxiv.org/html/2511.11288v1#S2.E7 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) with this terminal condition is unique.

2. In [[15](https://arxiv.org/html/2511.11288v1#bib.bib15)] it is shown that for 0≤α≤10\leq\alpha\leq 1 the standard approach related to the construction of exact Tikhonov–Täcklind uniqueness classes [[11](https://arxiv.org/html/2511.11288v1#bib.bib11)] [[12](https://arxiv.org/html/2511.11288v1#bib.bib12)] is applicable; functions from this class can grow faster than a linear function, i.e., the necessary condition given in [[16](https://arxiv.org/html/2511.11288v1#bib.bib16)] is not sufficient.

3. For α>1\alpha>1, the theory of [[10](https://arxiv.org/html/2511.11288v1#bib.bib10)] [[11](https://arxiv.org/html/2511.11288v1#bib.bib11)] is not applicable and, apparently, it is unknown whether the sublinear growth condition is sufficient for identifying uniqueness classes. At the same time, an example of a nontrivial solution in the case of zero initial data for α=2\alpha=2 is known (see [[17](https://arxiv.org/html/2511.11288v1#bib.bib17)])

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π2​(y,t)=y​(1−2​Φ​(−1σ​y​t)),{\Pi}\_{2}(y,t)=y\left(1-2\Phi\left(-\frac{1}{\sigma y\sqrt{t}}\right)\right), |  | (14) |

where Φ​(z)=12​π​∫−∞ze−u2/2​𝑑u\Phi(z)=\displaystyle{1\over\sqrt{2\pi}}\int\_{-\infty}^{z}e^{-u^{2}/2}\,du is the Laplace function. This solution has linear growth as y→+∞y\to+\infty and serves as an example of non-uniqueness of the solution for the given parameter value. Thus, for α=2\alpha=2, Theorem 4.3 of [[16](https://arxiv.org/html/2511.11288v1#bib.bib16)] gives both a necessary and sufficient condition for the uniqueness of the solution.

Let us construct a similar example of non-uniqueness for α=3/2\alpha=3/2 based on solution ([8](https://arxiv.org/html/2511.11288v1#S2.E8 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")). For this, it suffices to note that ([8](https://arxiv.org/html/2511.11288v1#S2.E8 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) under the substitution will become

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(y,τ)=4​yσ2​e−12​y​τ,y>0,τ>0.\Pi(y,\tau)=\frac{4y}{\sigma^{2}}e^{-\frac{1}{2y\tau}},\quad y>0,\quad\tau>0. |  | (15) |

This function is a nontrivial solution of ([13](https://arxiv.org/html/2511.11288v1#S3.E13 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), vanishes at τ=0\tau=0, and grows linearly as y→+∞y\to+\infty.

Thus, the uniqueness class for solutions in problem ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), ([3](https://arxiv.org/html/2511.11288v1#S1.E3 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) as v→+0v\to+0 consists of functions having sublinear growth at infinity (after the coordinate change y=4σ2​vy=\frac{4}{\sigma^{2}v}), i.e., the solution has a singularity weaker than 1/v1/v, in particular, integrable. Outside this class, the solution of the considered equation is, generally speaking, non-unique.

### 3.4. Main theorem

Let us summarize the results obtained in Section [3](https://arxiv.org/html/2511.11288v1#S3 "3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model") on uniqueness classes for problem ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), ([3](https://arxiv.org/html/2511.11288v1#S1.E3 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")):

###### Theorem 1.

Assume that the parameters of model ([1](https://arxiv.org/html/2511.11288v1#S1.E1 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) are such that the Feller condition ([5](https://arxiv.org/html/2511.11288v1#S1.E5 "In 1.1. Correct setting of boundary conditions ‣ 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) is satisfied. Then the classical solution to problem ([6](https://arxiv.org/html/2511.11288v1#S2.E6 "In 2. The uniqueness problem in option pricing in the Heston model under the Feller condition ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), ([3](https://arxiv.org/html/2511.11288v1#S1.E3 "In 1. Option price in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) is unique in the class of functions having, as S→+∞S\to+\infty, v→+∞v\to+\infty, S→0S\to 0, growth determined by condition ([10](https://arxiv.org/html/2511.11288v1#S3.E10 "In 3.1. Tikhonov–Täcklind classes (𝑆→∞, 𝑣→∞). ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")), and belonging to the class o​(1v)o\left(\frac{1}{v}\right) as v→0v\to 0.

## 4. Conclusion and discussion

This work contains the following main results.

1. The uniqueness class in the option pricing problem in the Heston model has been found. In particular, it is shown that it consists of functions having a singularity weaker than 1/v1/v as v→+0v\to+0. This shows the reason for non-uniqueness in the example constructed in [[1](https://arxiv.org/html/2511.11288v1#bib.bib1)].

2. Example ([15](https://arxiv.org/html/2511.11288v1#S3.E15 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) is constructed, showing that the requirement of sublinear growth at infinity is not only necessary but also a sufficient condition for the uniqueness of the solution to the parabolic equation with power-law degeneracy ([13](https://arxiv.org/html/2511.11288v1#S3.E13 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) for α=3/2\alpha=3/2.
In fact, in addition to the known example ([14](https://arxiv.org/html/2511.11288v1#S3.E14 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) for α=2\alpha=2, we have constructed a second example of this kind.

A natural question arises: is it possible, by reduction to the Feller equation, to construct a similar non-uniqueness example for the remaining α>1\alpha>1 and thereby show that the sublinear growth condition at infinity is precise for identifying the uniqueness class for solutions of equations of the form ([13](https://arxiv.org/html/2511.11288v1#S3.E13 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model"))? Such a result seems quite natural, but the corresponding examples are currently unknown. A formal obstacle to transferring the result from α=3/2\alpha=3/2 to other α>1\alpha>1 is that when reducing ([12](https://arxiv.org/html/2511.11288v1#S3.E12 "In 3.3. Uniqueness class for (6) as 𝑣→0. ‣ 3. Classes of uniqueness in the problem of option valuation in the Heston model ‣ On Non-Uniqueness of Solutions to Degenerate Parabolic Equations in the Context of Option Pricing in the Heston Model")) to the Feller equation for α≠3/2\alpha\neq 3/2, additional lower-order terms appear.

## References

* [1]

  Heston S. L., Loewenstein M., Willard G. A. Options and bubbles// The Review of Financial Studies. 2007. 20. 359–390.
* [2]

  Heston S. L. A closed form solution for options with stochastic volatility with applications to bond and currency options// The Review of Financial Studies. 1993. 6. 327–344.
* [3]

  Cox J. C., Ingersoll J. E., Ross S. A. A Theory of the Term Structure of Interest Rates// Econometrica. 1985. 53. 385–407.
* [4]

  Gatheral J., Taleb N. N. The Volatility Surface: A Practitioner’s Guide. Wiley Finance. 2006.
* [5]

  Fichera G. On a unified theory of boundary value problems for elliptic-parabolic equations of second order// Matematika. 1963. 7. 99–122.
* [6]

  Oleinik O. A., Radkevich E. V. Second-order equations with nonnegative characteristic form. Itogi Nauki. Ser. Matematika. Mat. anal. 1969, VINITI, M., 1971, 7–252. (In Russian)
* [7]

  Meyer G. H. The time-discrete method of lines for options and bonds: A PDE approach. World Scientific, 2015.
* [8]

  Tikhonov A. N. Uniqueness theorems for the heat equation// Mat. Sb.. 1935. 42. No 3. 199–216. (In Russian)
* [9]

  Tacklind S. Sur les classes quasianalityques des solutions des l’equations aux derivées partielles du type paraboliques// Nord. Acta Regial Soc. Scient. Uppsaliensis. 1936, ser. 4. 10. No 3. 3–55.
* [10]

  Kamynin L. I., Khimchenko B. N. On the uniqueness of the solution of the first boundary value problem and the Cauchy problem for a parabolic equation of the 2nd order with nonnegative characteristic form// Dokl. Akad. Nauk SSSR. 1979. 248. No 2. 290–294. (In Russian)
* [11]

  Kamynin L. I., Khimchenko B. N. On the Tikhonov–Petrovsky problem for parabolic equations of the 2nd order// Sib. Mat. Zh.. 1981. 22. No 5. 78–109. (In Russian)
* [12]

  Kamynin L. I. On the uniqueness of the solution of the first boundary value problem in an unbounded domain for a parabolic equation of the second order// Zh. Vychisl. Mat. Mat. Fiz.. 1984. 24. No 9. 1331–1345. (In Russian)
* [13]

  Feller W. Two singular diffusion problems// Annals of Mathematies. 1951. 54. No 1. 173–182.
* [14]

  Hull J. C. Options, Futures, and Other Derivatives. 8th ed., Dialektika (Williams). 2019. (Russian translation)
* [15]

  Ladykova E. A., Rozanova O. S. On non-uniqueness in the option pricing problem// Moscow University Mathematics Bulletin, 2025, to appear. (arXiv:2501.18721)
* [16]

  Ekstrom E., Tysk J. Bubbles, convexity and the Black-Sholes equation// The Annals of Applied Probability. 2009. 19. No 4. 1369–1384.
* [17]

  Cox A. M. G., Hobson D. G. Local martingales, bubbles and option prices// Finance and Stochastics. 2005. 9. 477–492.