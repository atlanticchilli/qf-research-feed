---
authors:
- Massimiliano Moda
- Karel J. in 't Hout
- Michèle Vanmaele
- Fred Espen Benth
doc_id: arxiv:2511.02700v1
family_id: arxiv:2511.02700
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Numerical valuation of European options under two-asset infinite-activity exponential
  Lévy models
url_abs: http://arxiv.org/abs/2511.02700v1
url_html: https://arxiv.org/html/2511.02700v1
venue: arXiv q-fin
version: 1
year: 2025
---


Massimiliano Moda, 
Karel J. in ’t Hout, 
Michèle Vanmaele, 
Fred Espen Benth
Department of Mathematics, University of Antwerp, Middelheimlaan 1, 2020 Antwerp, Belgium. Email: massimiliano.moda@uantwerpen.beDepartment of Mathematics, University of Antwerp, Middelheimlaan 1, 2020 Antwerp, Belgium. Email: karel.inthout@uantwerpen.beDepartment of Mathematics, Computer Science and Statistics, Ghent University, 9000 Ghent, Belgium. Email: michele.vanmaele@ugent.beDepartment of Data Science and Analytics, BI Norwegian Business School, N-0484 Oslo, Norway. Email: fred.e.benth@bi.no

###### Abstract

We propose a numerical method for the valuation of European-style options under two-asset infinite-activity exponential Lévy models. Our method extends
the effective approach developed by Wang et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib24)) for the 1-dimensional case to the 2-dimensional setting and is applicable for general Lévy measures under mild assumptions. A tailored discretization of the non-local integral term is developed, which can be efficiently evaluated by means of the fast Fourier transform. For the temporal discretization, the semi-Lagrangian θ\theta-method is employed in a convenient splitting fashion, where the diffusion term is treated implicitly and the integral term is handled explicitly by a fixed-point iteration. Numerical experiments for put-on-the-average options under Normal Tempered Stable dynamics reveal favourable second-order convergence of our method whenever the exponential Lévy process has finite-variation.

## 1 Introduction

The accurate valuation of derivative securities in modern financial
markets requires modeling techniques capable of capturing empirical
irregularities in asset price dynamics. Classical models based on
Brownian motion, such as the Black–Scholes model, rely on continuous-path
diffusion and fail to reflect important stylized facts, such as heavy
tails and skewness in log-returns. This has motivated the use of Lévy
processes in the last decades, which naturally offers a richer class
of models for asset dynamics. Among various Lévy models, the Normal
Inverse Gaussian (NIG) process has emerged as a parsimonious and effective
choice to capture such characteristics. Among others, Rydberg ([1997](https://arxiv.org/html/2511.02700v1#bib.bib20))
shows how the NIG model provides a significantly better statistical
fit to equity return data compared to classical Gaussian-based models. Lévy
models allow for a more realistic representation of market risk and
are therefore natural candidates for use in option pricing models.

In this paper, we propose a numerical method for pricing European-style financial
derivatives written on two underlying assets, whose dynamics are driven
by a 2-dimensional Lévy process, with particular focus on infinite
activity processes. Financial pricing under jump-diffusion models
can be approached through various methodologies, such as Monte Carlo
simulation, Fourier-based methods, and partial integro-differential
equations (PIDEs). Monte Carlo methods are flexible and easy to implement,
but they suffer from slow convergence. Fourier-based methods, such as
in Jackson et al. ([2008](https://arxiv.org/html/2511.02700v1#bib.bib12)) and Ruijter & Oosterlee ([2012](https://arxiv.org/html/2511.02700v1#bib.bib19)), can be applied when
the characteristic exponent of the process is known, and they can achieve
exponential convergence. Numerical methods for PIDEs, such as in Cont & Voltchkova ([2005](https://arxiv.org/html/2511.02700v1#bib.bib6)),
d’Halluin et al. ([2005](https://arxiv.org/html/2511.02700v1#bib.bib7)), Wang et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib24)), Clift & Forsyth ([2008](https://arxiv.org/html/2511.02700v1#bib.bib5)), Salmi et al. ([2014](https://arxiv.org/html/2511.02700v1#bib.bib21)),
Kaushansky et al. ([2018](https://arxiv.org/html/2511.02700v1#bib.bib13)), Boen & in ’t Hout ([2021](https://arxiv.org/html/2511.02700v1#bib.bib4)) and in ’t Hout & Lamotte ([2023](https://arxiv.org/html/2511.02700v1#bib.bib11)),
can instead be applied when the Lévy measure is known, and do not
require knowledge of the characteristic exponent.
They are applicable to a wide variety of financial derivatives.

The numerical method derived in this paper focuses on the case where the underlying
2-dimensional Lévy process exhibits infinite-activity, meaning that
an infinite number of jumps occur over any finite time horizon. In
this setting, particular care must be taken in the discretization
of the non-local 2-dimensional integral term in the PIDE near
the origin, where the Lévy measure becomes singular. Indeed, classical
quadrature formulae fail to yield the desired second-order convergence.

The main contribution of this paper is an extension of the effective numerical
solution approach of Wang et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib24)) from the 1-dimensional to the 2-dimensional
setting.
Here a key idea, originally introduced in Asmussen & Rosiński ([2001](https://arxiv.org/html/2511.02700v1#bib.bib2)) and Cont & Voltchkova ([2005](https://arxiv.org/html/2511.02700v1#bib.bib6)),
is to replace the small jumps with an artificial diffusion term. This substitution
enables the development of a tailored quadrature scheme, which restores the desired
order of convergence of the entire numerical scheme.
For the efficient evaluation of the discretized integral operator, a fast Fourier
transform (FFT) algorithm is constructed.
For the temporal discretization, the semi-Lagrangian θ\theta-method is considered.
Here operator splitting is applied, where the diffusion term is treated implicitly
and the integral term is handled explicitly by a fixed-point iteration.
For the large linear system in each time step, the BiCGSTAB iterative solver is used.

An outline of this paper is as follows. In Section [2](https://arxiv.org/html/2511.02700v1#S2 "2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"),
we introduce the market model and the PIDE for the derivative pricing.
In Section [3](https://arxiv.org/html/2511.02700v1#S3 "3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models") the proposed numerical scheme is derived.
Numerical experiments are discussed in Section [4](https://arxiv.org/html/2511.02700v1#S4 "4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").
The final Section [5](https://arxiv.org/html/2511.02700v1#S5 "5 Conclusions ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models") contains our conclusions.

## 2 Model framework

### 2.1 Market model

Let (Ω,ℱ,(ℱt)t∈[0,T],ℙ)\left(\Omega,\mathcal{F},\left(\mathcal{F}\_{t}\right)\_{t\in\left[0,T\right]},\mathbb{P}\right)
be a filtered probability space, for some given T>0T>0. We consider
an arbitrage free market characterized by a constant (instantaneous)
risk-free interest rate rr and an equivalent martingale measure
ℚ∼ℙ\mathbb{Q}\sim\mathbb{P}. We assume that there exist two risky
assets, whose prices are modeled by the 2-dimensional stochastic process
X=(X(1),X(2))X=\left(X^{\left(1\right)},X^{\left(2\right)}\right) that solves
the following stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)=μ​(X​(t))​d​t+Σ​(X​(t))​d​W​(t)+∫ℝ∗2γ​(z,X​(t−))​Π~​(d​t,d​z)(t∈(0,T])dX\left(t\right)=\mu\left(X\left(t\right)\right)dt+\Sigma\left(X\left(t\right)\right)dW\left(t\right)+\int\_{\mathbb{R}\_{\*}^{2}}\gamma\left(z,X\left(t\_{-}\right)\right)\tilde{\Pi}\left(dt,dz\right)\qquad\left(t\in\left(0,T\right]\right) |  | (2.1) |

for some non-negative initial value X​(0)X\left(0\right). In ([2.1](https://arxiv.org/html/2511.02700v1#S2.E1 "In 2.1 Market model ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
WW denotes a standard 2-dimensional Wiener process and Π~\tilde{\Pi} is
a compensated Poisson random measure with Lévy measure ℓ\ell over
ℝ∗2=ℝ2∖{0}\mathbb{R}\_{\*}^{2}=\mathbb{R}^{2}\setminus\left\{0\right\}. Both
are directly defined under ℚ\mathbb{Q} and are mutually independent.

The functions μ:ℝ≥02→ℝ2\mu:\mathbb{R}\_{\geq 0}^{2}\rightarrow\mathbb{R}^{2},
Σ:ℝ≥02→ℝ2×2\Sigma:\mathbb{R}\_{\geq 0}^{2}\rightarrow\mathbb{R}^{2\times 2} and
γ:ℝ2×ℝ≥02→ℝ2\gamma:\mathbb{R}^{2}\times\mathbb{R}\_{\geq 0}^{2}\rightarrow\mathbb{R}^{2}
are called drift, diffusion and jump function (or term) respectively,
where ℝ≥02={x∈ℝ2:x(i)≥0​ for ​i=1,2}\mathbb{R}\_{\geq 0}^{2}=\left\{x\in\mathbb{R}^{2}:x^{\left(i\right)}\geq 0\text{ for }i=1,2\right\}.
In this paper, we consider the case of the well-known exponential
Lévy process, i.e. where the coordinates of the coefficient functions
are defined as follows

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ(i)​(x)\displaystyle\mu^{\left(i\right)}\left(x\right) | =x(i)​r\displaystyle=x^{\left(i\right)}r |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Σ​Σ⊤)(i,j)​(x)\displaystyle\left(\Sigma\Sigma^{\top}\right)^{\left(i,j\right)}\left(x\right) | =x(i)​x(j)​(σ​σ⊤)(i,j)\displaystyle=x^{\left(i\right)}x^{\left(j\right)}\left(\sigma\sigma^{\top}\right)^{\left(i,j\right)} |  | (2.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ(i)​(z,x)\displaystyle\gamma^{\left(i\right)}\left(z,x\right) | =x(i)​(ez(i)−1),\displaystyle=x^{\left(i\right)}\left(e^{z^{\left(i\right)}}-1\right), |  | (2.4) |

where σ​σ⊤\sigma\sigma^{\top} is a constant positive
definite symmetric 2×22\times 2 matrix and σ\sigma denotes the volatility matrix.
Here, Σ​Σ⊤​(x)\Sigma\Sigma^{\top}\left(x\right) is a shorthand notation
for the matrix product Σ​(x)​Σ⊤​(x)\Sigma\left(x\right)\Sigma^{\top}\left(x\right).

Let ∥⋅∥\left\|\cdot\right\| be any given norm on ℝ2\mathbb{R}^{2}.
In this paper we assume that ℓ\ell is absolutely continuous, has finite variance, i.e.

|  |  |  |
| --- | --- | --- |
|  | ∫ℝz2​ℓ​(d​z)<∞\int\_{\mathbb{R}}z^{2}\ell\left(dz\right)<\infty |  |

and there exist constants Aℓ<2A\_{\ell}<2, Bℓ>2B\_{\ell}>2 such that for any given h>0h>0 there is Cℓ​(h)>0C\_{\ell}\left(h\right)>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ℓ​(z)≤Cℓ​(h)​‖z‖−Aℓ−2for any ​z​ such that ​‖z‖∈(0,h]ℓ​(z)=O​(e−Bℓ​‖z‖)as ​‖z‖→∞.\begin{cases}\ell\left(z\right)\leq C\_{\ell}\left(h\right)\left\|z\right\|^{-A\_{\ell}-2}&\text{for any }z\text{ such that }\left\|z\right\|\in\left(0,h\right]\\ \ell\left(z\right)=O\left(e^{-B\_{\ell}\left\|z\right\|}\right)&\text{as }\left\|z\right\|\rightarrow\infty.\end{cases} |  | (2.5) |

The number AℓA\_{\ell} governs the activity and variation of the
process: XX is of finite-activity if Aℓ<0A\_{\ell}<0, since ∫ℝ2ℓ​(d​z)<∞\int\_{\mathbb{R}^{2}}\ell\left(dz\right)<\infty;
it is of finite-variation if Aℓ<1A\_{\ell}<1, since ∫‖z‖<ϵ‖z‖​ℓ​(d​z)<∞\int\_{\left\|z\right\|<\epsilon}\left\|z\right\|\ell\left(dz\right)<\infty
for any ϵ>0\epsilon>0. The number BℓB\_{\ell} characterizes the exponential decay of ℓ\ell at infinity. Since the process XX has finite moments of all orders up to k∈ℕk\in\mathbb{N} if and only if ∫‖z‖>ϵek​‖z‖​ℓ​(d​z)<∞\int\_{\left\|z\right\|>\epsilon}e^{k\left\|z\right\|}\ell\left(dz\right)<\infty for any ϵ>0\epsilon>0, then k<Bℓk<B\_{\ell} provides a necessary condition of it. Following Applebaum ([2004](https://arxiv.org/html/2511.02700v1#bib.bib1), Chapter 6), the stronger condition Bℓ≥2B\_{\ell}\geq 2 is necessary to guarantee the
existence of a unique solution with finite variance to the stochastic
differential equation ([2.1](https://arxiv.org/html/2511.02700v1#S2.E1 "In 2.1 Market model ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).
Most of the common Lévy processes in finance satisfy the conditions
([2.5](https://arxiv.org/html/2511.02700v1#S2.E5 "In 2.1 Market model ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")), such as
the Kou, Carr-Geman-Madan-Yor (CGMY), Variance Gamma (VG) and Normal
Inverse Gaussian (NIG) models.

In this work, we focus on the case of 2-dimensional Normal Tempered
Stable (NTS) processes. These are obtained by subordinating a 2-dimensional
arithmetic Brownian motion with a Tempered Stable subordinator. A
detailed construction of the NTS process together with its main properties
is provided in Appendix [A](https://arxiv.org/html/2511.02700v1#A1 "Appendix A 𝑑-dimensional Normal Tempered Stable process ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").
The choice of this class of processes is motivated by two reasons.
First, bivariate VG and NIG processes arise as particular cases. Second,
the associated Lévy measure satisfies the conditions ([2.5](https://arxiv.org/html/2511.02700v1#S2.E5 "In 2.1 Market model ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
with constant Aℓ=2​αA\_{\ell}=2\alpha, where α\alpha is the key model
parameter. The NTS framework provides a convenient and flexible setting
for the purposes of this paper.

### 2.2 Initial boundary value problem for derivatives pricing

By the fundamental theorem of asset-pricing, the value at time t∈[0,T]t\in\left[0,T\right]
of an European-style111Means a financial derivative with no intermediate cash flows.
financial derivative of XX with maturity TT is represented by
the stochastic process PP such that

|  |  |  |
| --- | --- | --- |
|  | P​(t)=𝔼ℚ​[ϕ​(X​(T))​e−r​(T−t)∣ℱt]P\left(t\right)=\mathbb{E}^{\mathbb{Q}}\left[\phi\left(X\left(T\right)\right)e^{-r\left(T-t\right)}\mid\mathcal{F}\_{t}\right] |  |

where ϕ:ℝ2→ℝ\phi:\mathbb{R}^{2}\rightarrow\mathbb{R} denotes the pay-off
function and 𝔼ℚ[⋅∣ℱt]\mathbb{E}^{\mathbb{Q}}\left[\cdot\mid\mathcal{F}\_{t}\right]
is the ℱt\mathcal{F}\_{t}-conditional expected value (i.e. knowing
the history of the asset prices up to tt) under ℚ\mathbb{Q}.

Let 𝒜\mathcal{A} be the infinitesimal generator of XX (see Applebaum ([2004](https://arxiv.org/html/2511.02700v1#bib.bib1)),
Garroni & Menaldi ([1992](https://arxiv.org/html/2511.02700v1#bib.bib8)) and Øksendal & Sulem ([2019](https://arxiv.org/html/2511.02700v1#bib.bib15))), defined in matrix
notation as222By expanding the term, we obtain the common notation used for 𝒜\mathcal{A},
which is

𝒜​u​(x,t)=\displaystyle\mathcal{A}u\left(x,t\right)=
∑i=12μ(i)​(x)​∂u∂x(i)​(x,t)+12​∑i,j=12(Σ​Σ⊤)(i,j)​(x)​∂2u∂x(i)​∂x(j)​(x,t)\displaystyle\sum\_{i=1}^{2}\mu^{\left(i\right)}\left(x\right)\frac{\partial u}{\partial x^{\left(i\right)}}\left(x,t\right)+\frac{1}{2}\sum\_{i,j=1}^{2}\left(\Sigma\Sigma^{\top}\right)^{\left(i,j\right)}\left(x\right)\frac{\partial^{2}u}{\partial x^{\left(i\right)}\partial x^{\left(j\right)}}\left(x,t\right)



+∫ℝ∗2(u​(x+γ​(z,x),t)−u​(x,t)−∑i=12γ(i)​(z,x)​∂u∂x(i)​(x,t))​ℓ​(d​z).\displaystyle+\int\_{\mathbb{R}\_{\*}^{2}}\left(u\left(x+\gamma\left(z,x\right),t\right)-u\left(x,t\right)-\sum\_{i=1}^{2}\gamma^{\left(i\right)}\left(z,x\right)\frac{\partial u}{\partial x^{\left(i\right)}}\left(x,t\right)\right)\ell\left(dz\right).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜​u​(x,t)=μ​(x)⊤​ux​(x,t)+12​𝟏⊤​(ux​x​(x,t)∘Σ​Σ⊤​(x))​𝟏+∫ℝ∗2f​(z,x,t)​ℓ​(d​z)\mathcal{A}u\left(x,t\right)=\mu\left(x\right)^{\top}u\_{x}\left(x,t\right)+\frac{1}{2}\mathbf{1}^{\top}\left(u\_{xx}\left(x,t\right)\circ\Sigma\Sigma^{\top}\left(x\right)\right)\mathbf{1}+\int\_{\mathbb{R}\_{\*}^{2}}f\left(z,x,t\right)\ell\left(dz\right) |  | (2.6) |

where 𝟏=[1,1]⊤\mathbf{1}=\left[1,1\right]^{\top}, the symbol ∘\circ denotes
the Hadamard (element-wise) product333In this paper, we use the convention A​B∘C​D=(A​B)∘(C​D)AB\circ CD=\left(AB\right)\circ\left(CD\right),
for any suitable matrices A,B,C,DA,B,C,D. and

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(z,x,t)=u​(x+γ​(z,x),t)−u​(x,t)−γ​(z,x)⊤​ux​(x,t).f\left(z,x,t\right)=u\left(x+\gamma\left(z,x\right),t\right)-u\left(x,t\right)-\gamma\left(z,x\right)^{\top}u\_{x}\left(x,t\right). |  | (2.7) |

If there exists a function u:ℝ≥02×[0,T]→ℝu:\mathbb{R}\_{\geq 0}^{2}\times\left[0,T\right]\rightarrow\mathbb{R}
that solves the following initial value problem for a partial integro-differential
equation (PIDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ut​(x,t)=𝒜​u​(x,t)−r​u​(x,t)for any ​(x,t)∈ℝ≥02×(0,T]u​(x,0)=ϕ​(x)\begin{cases}u\_{t}\left(x,t\right)=\mathcal{A}u\left(x,t\right)-ru\left(x,t\right)&\text{for any }\left(x,t\right)\in\mathbb{R}\_{\geq 0}^{2}\times\left(0,T\right]\\ u\left(x,0\right)=\phi\left(x\right)\end{cases} |  | (2.8) |

then the value of the financial derivative is given by

|  |  |  |
| --- | --- | --- |
|  | P​(t)=u​(X​(t),T−t).P\left(t\right)=u\left(X\left(t\right),T-t\right). |  |

Note that uu also satisfies the PIDE at the boundary of the xx-domain,
as in the case of option pricing with the Black–Scholes model.

## 3 Numerical scheme

In this section, we derive the numerical scheme proposed for problem
([2.8](https://arxiv.org/html/2511.02700v1#S2.E8 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).

The method consists of three main steps: integral discretization,
spatial discretization, and temporal discretization. By discretization,
we mean that the pertinent integro/differential operators are approximated
on a given finite set of grid points. The adjectives indicate the
variable being discretized: integral for zz, spatial for xx, and
temporal for tt.

The integral discretization yields an approximation to the integral
term in ([2.8](https://arxiv.org/html/2511.02700v1#S2.E8 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) for any given pair (x,t)∈ℝ≥02×[0,T]\left(x,t\right)\in\mathbb{R}\_{\geq 0}^{2}\times\left[0,T\right].
The quadrature formula that we derive is inspired by the ideas in
Wang et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib24)) and Cont & Voltchkova ([2005](https://arxiv.org/html/2511.02700v1#bib.bib6)), where the singular part of
the integral near the origin z=0z=0 is approximated by a diffusion
(second-order spatial derivative). The integral discretization leads
to the approximate problem ([3.8](https://arxiv.org/html/2511.02700v1#S3.E8 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) where
the integral in ([2.8](https://arxiv.org/html/2511.02700v1#S2.E8 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) has been replaced by
a summation term.

The spatial discretization concerns the diffusion and summation terms
in ([3.8](https://arxiv.org/html/2511.02700v1#S3.E8 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")). For the diffusion term, a
standard second-order central finite difference scheme is applied
on a suitable nonuniform spatial grid. For the summation term, a direct
valuation on the spatial grid is computationally too expensive. For
the efficient treatment of this term, we shall extend the FFT-based
approach by Wang et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib24)).

The temporal discretization is done by the semi-Lagrangian θ\theta-method.
The semi-Lagrangian approach is chosen to take into account that problem
([3.8](https://arxiv.org/html/2511.02700v1#S3.E8 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) can be convection-dominated.
In each time step of the semi-Lagrangian θ\theta-method, the summation
term appears in an implicit manner. To effectively handle this term,
a fixed-point iteration is employed.

### 3.1 Integral discretization

When the Lévy measure is singular, it is not possible to apply classical
quadrature formulae, such as the midpoint or the trapezoidal rule.
In fact, in this case the error will blow up as the number of quadrature
points increases. To address this problem, we develop in this subsection
a different quadrature formula.

First, it is useful to investigate the behaviour of ff, defined
in ([2.7](https://arxiv.org/html/2511.02700v1#S2.E7 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")), around the origin with
respect to zz. For any given point (x,t)∈ℝ≥02×[0,T]\left(x,t\right)\in\mathbb{R}\_{\geq 0}^{2}\times\left[0,T\right],
the Taylor approximation of the function z↦f​(z,x,t)z\mapsto f\left(z,x,t\right)
at z=0z=0 is given by

|  |  |  |
| --- | --- | --- |
|  | f​(z,x,t)=f​(0,x,t)+z⊤​fz​(0,x,t)+12​z⊤​fz​z​(0,x,t)​z+ε​(z,x,t)as ​‖z‖→0+,f\left(z,x,t\right)=f\left(0,x,t\right)+z^{\top}f\_{z}\left(0,x,t\right)+\frac{1}{2}z^{\top}f\_{zz}\left(0,x,t\right)z+\varepsilon\left(z,x,t\right)\qquad\text{as }\left\|z\right\|\rightarrow 0^{+}, |  |

where fzf\_{z} and fz​zf\_{zz} are the gradient and the Hessian of ff
with respect to zz. Here, ε\varepsilon denotes the remainder and
is such that ε​(z,x,t)=O​(‖z‖3)\varepsilon\left(z,x,t\right)=O\left(\left\|z\right\|^{3}\right).
Invoking ([2.7](https://arxiv.org/html/2511.02700v1#S2.E7 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) and noting that f​(0,x,t)=0f\left(0,x,t\right)=0
and fz​(0,x,t)=0f\_{z}\left(0,x,t\right)=0, we can rewrite the previous equation,
after some straightforward computations, as

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(z,x,t)=12​𝟏⊤​(ux​x​(x,t)∘Ix​z​z⊤​Ix)​𝟏+ε​(z,x,t)as ​‖z‖→0+,f\left(z,x,t\right)=\frac{1}{2}\mathbf{1}^{\top}\left(u\_{xx}\left(x,t\right)\circ I\_{x}zz^{\top}I\_{x}\right)\mathbf{1}+\varepsilon\left(z,x,t\right)\qquad\text{as }\left\|z\right\|\rightarrow 0^{+}, |  | (3.1) |

where ux​xu\_{xx} is the Hessian of uu with respect to xx and Ix=diag​(x(1),x(2))I\_{x}=\text{diag}\left(x^{\left(1\right)},x^{\left(2\right)}\right).

Next, let Rz𝐈R\_{z}^{\mathbf{I}}, Rz𝐈𝐈R\_{z}^{\mathbf{II}} and Rz𝐈𝐈𝐈R\_{z}^{\mathbf{III}}
be three sets defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rz𝐈\displaystyle R\_{z}^{\mathbf{I}} | ={z∈ℝ2:‖z‖∞≤zmax𝐈},\displaystyle=\left\{z\in\mathbb{R}^{2}:\left\|z\right\|\_{\infty}\leq z\_{\max}^{\mathbf{I}}\right\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rz𝐈𝐈\displaystyle R\_{z}^{\mathbf{II}} | ={z∈ℝ2:zmax𝐈<‖z‖∞≤zmax𝐈𝐈},\displaystyle=\left\{z\in\mathbb{R}^{2}:z\_{\max}^{\mathbf{I}}<\left\|z\right\|\_{\infty}\leq z\_{\max}^{\mathbf{II}}\right\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rz𝐈𝐈𝐈\displaystyle R\_{z}^{\mathbf{III}} | ={z∈ℝ2:zmax𝐈𝐈<‖z‖∞≤zmax𝐈𝐈𝐈},\displaystyle=\left\{z\in\mathbb{R}^{2}:z\_{\max}^{\mathbf{II}}<\left\|z\right\|\_{\infty}\leq z\_{\max}^{\mathbf{III}}\right\}, |  |

where ‖z‖∞=maxj=1,2⁡|z(j)|\left\|z\right\|\_{\infty}=\max\_{j=1,2}\left|z^{\left(j\right)}\right|
and 0<zmax𝐈<zmax𝐈𝐈<zmax𝐈𝐈𝐈0<z\_{\max}^{\mathbf{I}}<z\_{\max}^{\mathbf{II}}<z\_{\max}^{\mathbf{III}}
are given numbers, which will be specified in Section [4](https://arxiv.org/html/2511.02700v1#S4 "4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").
The above three sets represent a partition of Rz={z∈ℝ2:‖z‖∞≤zmax𝐈𝐈𝐈}R\_{z}=\left\{z\in\mathbb{R}^{2}:\left\|z\right\|\_{\infty}\leq z\_{\max}^{\mathbf{III}}\right\}, which is a square centered
at the origin, as shown in Figure [1](https://arxiv.org/html/2511.02700v1#S3.F1 "Figure 1 ‣ 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").

Figure 1: Partition
of the integration domain RzR\_{z}

![Refer to caption](x1.png)

For any given Nz∈ℕN\_{z}\in\mathbb{N}, define a set of points 𝐳\mathbf{z}
whose elements are

|  |  |  |
| --- | --- | --- |
|  | zl1​l2=((l1+12)hz,(l2+12)hz)(l1,l2=−Nz,−Nz+1,…,Nz−2,Nz−1),z\_{l\_{1}l\_{2}}=\left(\left(l\_{1}+\frac{1}{2}\right)h\_{z},\left(l\_{2}+\frac{1}{2}\right)h\_{z}\right)\qquad\left(l\_{1},l\_{2}=-N\_{z},-N\_{z}+1,\ldots,N\_{z}-2,N\_{z}-1\right), |  |

where hz=zmax𝐈𝐈𝐈/Nzh\_{z}=z\_{\max}^{\mathbf{III}}/N\_{z} denotes the mesh-width.
Note that the point zl1​l2z\_{l\_{1}l\_{2}} is the center of the cell

|  |  |  |
| --- | --- | --- |
|  | Rl1​l2=[l1​hz,(l1+1)​hz]×[l2​hz,(l2+1)​hz].R\_{l\_{1}l\_{2}}=\left[l\_{1}h\_{z},\left(l\_{1}+1\right)h\_{z}\right]\times\left[l\_{2}h\_{z},\left(l\_{2}+1\right)h\_{z}\right]. |  |

We then consider the approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝ∗2f​(z,x,t)​ℓ​(d​z)≃∫Rz𝐈f​(z,x,t)​ℓ​(d​z)+∫Rz𝐈𝐈f​(z,x,t)​ℓ​(d​z)+∫Rz𝐈𝐈𝐈f​(z,x,t)​ℓ​(d​z),\int\_{\mathbb{R}\_{\*}^{2}}f\left(z,x,t\right)\ell\left(dz\right)\simeq\int\_{R\_{z}^{\mathbf{I}}}f\left(z,x,t\right)\ell\left(dz\right)+\int\_{R\_{z}^{\mathbf{II}}}f\left(z,x,t\right)\ell\left(dz\right)+\int\_{R\_{z}^{\mathbf{III}}}f\left(z,x,t\right)\ell\left(dz\right), |  | (3.2) |

where the individual terms on the right-hand side will be approximated
in different ways: the first one will be transformed into a diffusion
term by replacing the integrand function with its Taylor expansion;
for the second one, a particular quadrature formula is used that takes
into account the limiting singular behaviour of the Lévy measure as
‖z‖→0+\left\|z\right\|\rightarrow 0^{+}; for the third one, a
generic method is used.

By substituting ([3.1](https://arxiv.org/html/2511.02700v1#S3.E1 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
in the first integral in ([3.2](https://arxiv.org/html/2511.02700v1#S3.E2 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Rz𝐈f​(z,x,t)​ℓ​(d​z)≃12​𝟏⊤​(ux​x​(x,t)∘Ix​(∫Rz𝐈z​z⊤​ℓ​(d​z))​Ix)​𝟏.\int\_{R\_{z}^{\mathbf{I}}}f\left(z,x,t\right)\ell\left(dz\right)\simeq\frac{1}{2}\mathbf{1}^{\top}\left(u\_{xx}\left(x,t\right)\circ I\_{x}\left(\int\_{R\_{z}^{\mathbf{I}}}zz^{\top}\ell\left(dz\right)\right)I\_{x}\right)\mathbf{1}. |  | (3.3) |

Here, the entries of the matrix ∫Rz𝐈z​z⊤​ℓ​(d​z)\int\_{R\_{z}^{\mathbf{I}}}zz^{\top}\ell\left(dz\right)
can be accurately approximated using a common numerical integrator.

Moving on to the second and third terms in ([3.2](https://arxiv.org/html/2511.02700v1#S3.E2 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
we consider a quadrature formula of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Rz𝐈𝐈∪Rz𝐈𝐈𝐈f​(z,x,t)​ℓ​(d​z)≃∑l1,l2=−NzNz−1ωl1​l2​f​(zl1​l2,x,t).\int\_{R\_{z}^{\mathbf{II}}\cup R\_{z}^{\mathbf{III}}}f\left(z,x,t\right)\ell\left(dz\right)\simeq\sum\_{l\_{1},l\_{2}=-N\_{z}}^{N\_{z}-1}\omega\_{l\_{1}l\_{2}}f\left(z\_{l\_{1}l\_{2}},x,t\right). |  | (3.4) |

Defining the coefficients

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωl1​l2={0if ​l1,l2:zl1​l2∈Rz𝐈,‖zl1​l2‖−2​∫Rl1​l2‖z‖2​ℓ​(d​z)if ​l1,l2:zl1​l2∈Rz𝐈𝐈,ℓ​(zl1​l2)​hz2if ​l1,l2:zl1​l2∈Rz𝐈𝐈𝐈,\omega\_{l\_{1}l\_{2}}=\begin{cases}0&\text{if }l\_{1},l\_{2}:z\_{l\_{1}l\_{2}}\in R\_{z}^{\mathbf{I}},\\ \left\|z\_{l\_{1}l\_{2}}\right\|^{-2}\int\_{R\_{l\_{1}l\_{2}}}\left\|z\right\|^{2}\ell\left(dz\right)&\text{if }l\_{1},l\_{2}:z\_{l\_{1}l\_{2}}\in R\_{z}^{\mathbf{II}},\\ \ell\left(z\_{l\_{1}l\_{2}}\right)h\_{z}^{2}&\text{if }l\_{1},l\_{2}:z\_{l\_{1}l\_{2}}\in R\_{z}^{\mathbf{III}},\end{cases} |  | (3.5) |

a high level of accuracy is achieved, despite the integrand being
singular at the origin. Clearly, the quadrature weights used in Rz𝐈𝐈R\_{z}^{\mathbf{II}}
are constructed as integrals of the Lévy measure, which turns out
to be beneficial for the convergence behaviour (as Nz→∞N\_{z}\rightarrow\infty).
Analogously to the entries of the matrix ∫Rz𝐈z​z⊤​ℓ​(d​z)\int\_{R\_{z}^{\mathbf{I}}}zz^{\top}\ell\left(dz\right)
in ([3.3](https://arxiv.org/html/2511.02700v1#S3.E3 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
the integrals ∫Rl1​l2‖z‖2​ℓ​(d​z)\int\_{R\_{l\_{1}l\_{2}}}\left\|z\right\|^{2}\ell\left(dz\right)
can be precomputed using a common numerical integrator. Regarding
Rz𝐈𝐈𝐈R\_{z}^{\mathbf{III}}, the coefficients are obtained by applying
the classical midpoint rule, see for example Quarteroni et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib17)).
Finally, note that the weights ωl1​l2\omega\_{l\_{1}l\_{2}} are null over
Rz𝐈R\_{z}^{\mathbf{I}}, as the first integral in ([3.2](https://arxiv.org/html/2511.02700v1#S3.E2 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
has already been approximated through ([3.3](https://arxiv.org/html/2511.02700v1#S3.E3 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).

Using ([3.3](https://arxiv.org/html/2511.02700v1#S3.E3 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) and substituting ([2.7](https://arxiv.org/html/2511.02700v1#S2.E7 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) into ([3.4](https://arxiv.org/html/2511.02700v1#S3.E4 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
we can define an approximating operator 𝒜ω\mathcal{A}\_{\omega} and
a number rωr\_{\omega} such that

|  |  |  |
| --- | --- | --- |
|  | 𝒜​u​(x,t)−r​u​(x,t)≃𝒜ω​u​(x,t)−rω​u​(x,t)for any ​(x,t)∈ℝ≥02×(0,T],\mathcal{A}u\left(x,t\right)-ru\left(x,t\right)\simeq\mathcal{A}\_{\omega}u\left(x,t\right)-r\_{\omega}u\left(x,t\right)\qquad\text{for any }\left(x,t\right)\in\mathbb{R}\_{\geq 0}^{2}\times\left(0,T\right], |  |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒜ω​u​(x,t)\displaystyle\mathcal{A}\_{\omega}u\left(x,t\right) | =μω​(x)⊤​ux​(x,t)+12​𝟏⊤​(ux​x​(x,t)∘Σω​Σω⊤​(x))​𝟏+(ℬω​u)​(x,t)\displaystyle=\mu\_{\omega}\left(x\right)^{\top}u\_{x}\left(x,t\right)+\frac{1}{2}\mathbf{1}^{\top}\left(u\_{xx}\left(x,t\right)\circ\Sigma\_{\omega}\Sigma\_{\omega}^{\top}\left(x\right)\right)\mathbf{1}+\left(\mathcal{B}\_{\omega}u\right)\left(x,t\right) |  | (3.6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | rω\displaystyle r\_{\omega} | =r+∑l1,l2=−NzNz−1ωl1​l2\displaystyle=r+\sum\_{l\_{1},l\_{2}=-N\_{z}}^{N\_{z}-1}\omega\_{l\_{1}l\_{2}} |  |

where, for i,j=1,2i,j=1,2,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μω(i)​(x)\displaystyle\mu\_{\omega}^{\left(i\right)}\left(x\right) | =x(i)​κω(i)\displaystyle=x^{\left(i\right)}\kappa\_{\omega}^{\left(i\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | κω(i)\displaystyle\kappa\_{\omega}^{\left(i\right)} | =r−∑l1,l2=−NzNz−1ωl1​l2​(ezl1​l2(i)−1)\displaystyle=r-\sum\_{l\_{1},l\_{2}=-N\_{z}}^{N\_{z}-1}\omega\_{l\_{1}l\_{2}}\left(e^{z\_{l\_{1}l\_{2}}^{\left(i\right)}}-1\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (Σω​Σω⊤)(i,j)​(x)\displaystyle\left(\Sigma\_{\omega}\Sigma\_{\omega}^{\top}\right)^{\left(i,j\right)}\left(x\right) | =x(i)​x(j)​(σω​σω⊤)(i,j)\displaystyle=x^{\left(i\right)}x^{\left(j\right)}\left(\sigma\_{\omega}\sigma\_{\omega}^{\top}\right)^{\left(i,j\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σω​σω⊤\displaystyle\sigma\_{\omega}\sigma\_{\omega}^{\top} | =σ​σ⊤+∫Rz𝐈z​z⊤​ℓ​(d​z)\displaystyle=\sigma\sigma^{\top}+\int\_{R\_{z}^{\mathbf{I}}}zz^{\top}\ell\left(dz\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (ℬω​u)​(x,t)\displaystyle\left(\mathcal{B}\_{\omega}u\right)\left(x,t\right) | =∑l1,l2=−NzNz−1ωl1​l2​u​(x+γ​(zl1​l2,x),t).\displaystyle=\sum\_{l\_{1},l\_{2}=-N\_{z}}^{N\_{z}-1}\omega\_{l\_{1}l\_{2}}u\left(x+\gamma\left(z\_{l\_{1}l\_{2}},x\right),t\right). |  | (3.7) |

Then, we approximate the solution uu of ([2.8](https://arxiv.org/html/2511.02700v1#S2.E8 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
by the function v:ℝ≥02×[0,T]→ℝv:\mathbb{R}\_{\geq 0}^{2}\times\left[0,T\right]\rightarrow\mathbb{R}
which solves the following problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | {vt​(x,t)=𝒜ω​v​(x,t)−rω​v​(x,t)for any ​(x,t)∈ℝ≥02×(0,T]v​(x,0)=ϕ​(x).\begin{cases}v\_{t}\left(x,t\right)=\mathcal{A}\_{\omega}v\left(x,t\right)-r\_{\omega}v\left(x,t\right)&\text{for any }\left(x,t\right)\in\mathbb{R}\_{\geq 0}^{2}\times\left(0,T\right]\\ v\left(x,0\right)=\phi\left(x\right).\end{cases} |  | (3.8) |

### 3.2 Spatial discretization

In this section, we successively consider the spatial discretization
of the diffusion and summation terms in the operator 𝒜ω\mathcal{A}\_{\omega}.
The convection term will be discussed in Section [3.3](https://arxiv.org/html/2511.02700v1#S3.SS3 "3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").

Let Rx=[0,xmax]×[0,xmax]R\_{x}=\left[0,x\_{\max}\right]\times\left[0,x\_{\max}\right]
be the truncated xx-domain over which the solution to ([3.8](https://arxiv.org/html/2511.02700v1#S3.E8 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
is approximated and Nx∈ℕN\_{x}\in\mathbb{N} be a given number of spatial
grid points. Here, xmaxx\_{\max} is heuristically chosen in such a way
that the localization error is negligible. We construct a spatial
grid 𝐱\mathbf{x} in RxR\_{x} by applying, in each dimension, a strictly
increasing and smooth transformation φ\varphi to an artificial uniform
grid. Let

|  |  |  |
| --- | --- | --- |
|  | xm=φ​(φ−1​(0)+φ−1​(xmax)−φ−1​(0)Nx​m)(m=0,1,…,Nx)x\_{m}=\varphi\left(\varphi^{-1}\left(0\right)+\frac{\varphi^{-1}\left(x\_{\max}\right)-\varphi^{-1}\left(0\right)}{N\_{x}}m\right)\qquad\left(m=0,1,\ldots,N\_{x}\right) |  |

with hx,m=xm−xm−1h\_{x,m}=x\_{m}-x\_{m-1}. The elements of 𝐱\mathbf{x} are defined
by

|  |  |  |
| --- | --- | --- |
|  | xm1​m2=(xm1,xm2)(m1,m2=0,1,…,Nx).x\_{m\_{1}m\_{2}}=\left(x\_{m\_{1}},x\_{m\_{2}}\right)\qquad\left(m\_{1},m\_{2}=0,1,\ldots,N\_{x}\right). |  |

The function φ\varphi will be chosen in such a way that relatively
many points are placed in a region of financial and numerical interest.

In what follows, we denote the values over 𝐱\mathbf{x} of any given
function g:Rx×[0,T]→ℝg:R\_{x}\times\left[0,T\right]\rightarrow\mathbb{R} by
the vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(𝐱,t)=[g​(x00,t),g​(x10,t),…,g​(xNx−1,Nx,t),g​(xNx​Nx,t)]⊤.g\left(\mathbf{x},t\right)=\left[g\left(x\_{00},t\right),g\left(x\_{10},t\right),\ldots,g\left(x\_{N\_{x}-1,N\_{x}},t\right),g\left(x\_{N\_{x}N\_{x}},t\right)\right]^{\top}. |  | (3.9) |

#### 3.2.1 Diffusion term

In this subsection, we construct a semi-discrete diffusion matrix
DD such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​v​(𝐱,t)≃[12​𝟏⊤​(vx​x​(xm1​m2,t)∘Σω​Σω⊤​(xm1​m2))​𝟏]m1,m2=0,1,…,Nx,Dv\left(\mathbf{x},t\right)\simeq\left[\frac{1}{2}\mathbf{1}^{\top}\left(v\_{xx}\left(x\_{m\_{1}m\_{2}},t\right)\circ\Sigma\_{\omega}\Sigma\_{\omega}^{\top}\left(x\_{m\_{1}m\_{2}}\right)\right)\mathbf{1}\right]\_{m\_{1},m\_{2}=0,1,\ldots,N\_{x}}, |  | (3.10) |

where the right-hand side is a vector, whose elements are ordered
according to ([3.9](https://arxiv.org/html/2511.02700v1#S3.E9 "In 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).

To this purpose, in each spatial dimension, we approximate the first-
and second-order derivatives of a given smooth function g:ℝ→ℝg:\mathbb{R}\rightarrow\mathbb{R}
by the following second-order central finite difference schemes

|  |  |  |  |
| --- | --- | --- | --- |
|  | g′​(xm)\displaystyle g^{\prime}\left(x\_{m}\right) | ≃αm(−1)​g​(xm−1)+αm(0)​g​(xm)+αm(1)​g​(xm+1)\displaystyle\simeq\alpha\_{m}^{\left(-1\right)}g\left(x\_{m-1}\right)+\alpha\_{m}^{\left(0\right)}g\left(x\_{m}\right)+\alpha\_{m}^{\left(1\right)}g\left(x\_{m+1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g′′​(xm)\displaystyle g^{\prime\prime}\left(x\_{m}\right) | ≃βm(−1)​g​(xm−1)+βm(0)​g​(xm)+βm(1)​g​(xm+1)\displaystyle\simeq\beta\_{m}^{\left(-1\right)}g\left(x\_{m-1}\right)+\beta\_{m}^{\left(0\right)}g\left(x\_{m}\right)+\beta\_{m}^{\left(1\right)}g\left(x\_{m+1}\right) |  |

with coefficients

|  |  |  |
| --- | --- | --- |
|  | αm(−1)=−hx,m+1hx,m​(hx,m+hx,m+1),αm(0)=hx,m+1−hx,mhx,m​hx,m+1,αm(1)=hx,mhx,m+1​(hx,m+hx,m+1),\alpha\_{m}^{\left(-1\right)}=\frac{-h\_{x,m+1}}{h\_{x,m}\left(h\_{x,m}+h\_{x,m+1}\right)},\qquad\alpha\_{m}^{\left(0\right)}=\frac{h\_{x,m+1}-h\_{x,m}}{h\_{x,m}h\_{x,m+1}},\qquad\alpha\_{m}^{\left(1\right)}=\frac{h\_{x,m}}{h\_{x,m+1}\left(h\_{x,m}+h\_{x,m+1}\right)}, |  |

|  |  |  |
| --- | --- | --- |
|  | βm(−1)=2hx,m​(hx,m+hx,m+1),βm(0)=−2hx,m​hx,m+1,βm(1)=2hx,m+1​(hx,m+hx,m+1).\beta\_{m}^{\left(-1\right)}=\frac{2}{h\_{x,m}\left(h\_{x,m}+h\_{x,m+1}\right)},\qquad\beta\_{m}^{\left(0\right)}=\frac{-2}{h\_{x,m}h\_{x,m+1}},\qquad\beta\_{m}^{\left(1\right)}=\frac{2}{h\_{x,m+1}\left(h\_{x,m}+h\_{x,m+1}\right)}. |  |

Concerning the boundary of the truncated spatial domain, we modify
the previous formulae in the following way. At the lower boundary
x0=0x\_{0}=0, the first- and second-order derivative terms in ([3.8](https://arxiv.org/html/2511.02700v1#S3.E8 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
vanish. Hence, it is natural to choose α0(j)=0\alpha\_{0}^{\left(j\right)}=0
and β0(j)=0\beta\_{0}^{\left(j\right)}=0 for any j={−1,0,1}j=\left\{-1,0,1\right\}.
At the upper boundary xNx=xmaxx\_{N\_{x}}=x\_{\max}, we make the natural assumption
that the solution vv behaves linearly in xx, thus we choose βNx(j)=0\beta\_{N\_{x}}^{\left(j\right)}=0
for any j={−1,0,1}j=\left\{-1,0,1\right\}, and we approximate the first-order
derivative by the first-order backward finite difference scheme.

Noting that 𝐱\mathbf{x} is the Cartesian product of two identical
1-dimensional grids, by employing the 1-directional finite difference
formulae in both the spatial dimensions, it leads to the matrix DD
defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | D=12​(σω​σω⊤)(1,1)​I⊗I𝐱2​D2+(σω​σω⊤)(1,2)​I𝐱​D1⊗I𝐱​D1+12​(σω​σω⊤)(2,2)​I𝐱2​D2⊗I.D=\frac{1}{2}\left(\sigma\_{\omega}\sigma\_{\omega}^{\top}\right)^{\left(1,1\right)}I\otimes I\_{\mathbf{x}}^{2}D\_{2}+\left(\sigma\_{\omega}\sigma\_{\omega}^{\top}\right)^{\left(1,2\right)}I\_{\mathbf{x}}D\_{1}\otimes I\_{\mathbf{x}}D\_{1}+\frac{1}{2}\left(\sigma\_{\omega}\sigma\_{\omega}^{\top}\right)^{\left(2,2\right)}I\_{\mathbf{x}}^{2}D\_{2}\otimes I. |  | (3.11) |

Here, I∈ℝ(Nx+1)×(Nx+1)I\in\mathbb{R}^{\left(N\_{x}+1\right)\times\left(N\_{x}+1\right)}
is the identity matrix, I𝐱=diag​(x0(i),…,xNx(i))I\_{\mathbf{x}}=\text{diag}\left(x\_{0}^{\left(i\right)},\ldots,x\_{N\_{x}}^{\left(i\right)}\right)
and ⊗\otimes denotes the Kronecker product.444In this paper, we use the convention A​B⊗C​D=(A​B)⊗(C​D)AB\otimes CD=\left(AB\right)\otimes\left(CD\right),
for any suitable matrices A,B,C,DA,B,C,D. The matrices D1,D2∈ℝ(Nx+1)×(Nx+1)D\_{1},D\_{2}\in\mathbb{R}^{\left(N\_{x}+1\right)\times\left(N\_{x}+1\right)}
are the matrices representing numerical differentiation of first-
and second-order by the relevant finite difference formulae above.
The mixed derivative has been approximated by applying the finite
difference formula for the first-order derivative subsequently in
the two spatial dimensions.

#### 3.2.2 Summation term

In this section, we derive an efficient method to approximate the
summation term (ℬω​v)​(𝐱,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right)
given the values of v​(𝐱,t)v\left(\mathbf{x},t\right). Unlike the differential
component of 𝒜ω\mathcal{A}\_{\omega}, we do not construct a matrix
BωB\_{\omega} such that (ℬω​v)​(𝐱,t)≃Bω​v​(𝐱,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right)\simeq B\_{\omega}v\left(\mathbf{x},t\right),
as this matrix would be large and dense.

Assuming that the values of vv are known for all (x,t)∈Rx×[0,T]\left(x,t\right)\in R\_{x}\times\left[0,T\right],
using formula ([3.7](https://arxiv.org/html/2511.02700v1#S3.E7 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
to directly evaluate (ℬω​v)​(𝐱,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right)
would require O​(Nx2​Nz2)O\left(N\_{x}^{2}N\_{z}^{2}\right) elementary operations,
which is computationally too expensive. For this reason, a particularly
efficient method combining interpolation and FFT is considered, which
extends the approach by Wang et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib24)).

Let Ny−,Ny+∈ℕN\_{y}^{-},N\_{y}^{+}\in\mathbb{N} be any given natural numbers
and let 𝐲out\mathbf{y}^{\text{out}} and 𝐲in\mathbf{y}^{\text{in}} be
two grids of points defined by555The superscripts stand for “input” and “output”.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ym1​m2out\displaystyle y\_{m\_{1}m\_{2}}^{\text{out}} | =(em1​hz,em2​hz)(m1,m2=−Ny−,−Ny−+1,…,Ny+−1,Ny+),\displaystyle=\left(e^{m\_{1}h\_{z}},e^{m\_{2}h\_{z}}\right)\qquad\left(m\_{1},m\_{2}=-N\_{y}^{-},-N\_{y}^{-}+1,\ldots,N\_{y}^{+}-1,N\_{y}^{+}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ym1​m2in\displaystyle y\_{m\_{1}m\_{2}}^{\text{in}} | =(e(m1+12)​hz,e(m2+12)​hz)(m1,m2=−Nz−Ny−,−Nz−Ny−+1,…,Nz+Ny+−2,Nz+Ny+−1),\displaystyle=\left(e^{\left(m\_{1}+\frac{1}{2}\right)h\_{z}},e^{\left(m\_{2}+\frac{1}{2}\right)h\_{z}}\right)\qquad\left(m\_{1},m\_{2}=-N\_{z}-N\_{y}^{-},-N\_{z}-N\_{y}^{-}+1,\ldots,N\_{z}+N\_{y}^{+}-2,N\_{z}+N\_{y}^{+}-1\right), |  |

then it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℬωv)(ym1​m2out,t)=∑l1,l2=−NzNz−1ωl1​l2v(yl1+m1,l2+m2in,t)(m1,m2=−Ny−,−Ny−+1,…,Ny+−1,Ny+).\left(\mathcal{B}\_{\omega}v\right)\left(y\_{m\_{1}m\_{2}}^{\text{out}},t\right)=\sum\_{l\_{1},l\_{2}=-N\_{z}}^{N\_{z}-1}\omega\_{l\_{1}l\_{2}}v\left(y\_{l\_{1}+m\_{1},l\_{2}+m\_{2}}^{\text{in}},t\right)\qquad\left(m\_{1},m\_{2}=-N\_{y}^{-},-N\_{y}^{-}+1,\ldots,N\_{y}^{+}-1,N\_{y}^{+}\right). |  | (3.12) |

Clearly, the summation term ([3.12](https://arxiv.org/html/2511.02700v1#S3.E12 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) can be viewed as a discrete 2-dimensional cross-correlation. It is well known, see for instance Plonka et al. ([2018](https://arxiv.org/html/2511.02700v1#bib.bib16), Chapter 3), that it can be written in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℬω​v)​(𝐲out,t)=I~​C​v​(𝐲in,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{y}^{\text{out}},t\right)=\tilde{I}Cv\left(\mathbf{y}^{\text{in}},t\right) |  | (3.13) |

where:

* ∙\bullet

  C∈ℝ(♯​in)2×(♯​in)2C\in\mathbb{R}^{\left(\sharp\text{in}\right)^{2}\times\left(\sharp\text{in}\right)^{2}}
  is a circulant matrix whose first row is given by C1,⋅⊤C\_{1,\cdot}^{\top}
  with

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | C1,⋅=vec​([Ω0♯​𝐳×(♯​in−♯​𝐳)0(♯​in−♯​𝐳)×♯​𝐳0(♯​in−♯​𝐳)×(♯​in−♯​𝐳)]).C\_{1,\cdot}=\text{vec}\left(\left[\begin{array}[]{cc}\Omega&0\_{\sharp\mathbf{z}\times\left(\sharp\text{in}-\sharp\mathbf{z}\right)}\\ 0\_{\left(\sharp\text{in}-\sharp\mathbf{z}\right)\times\sharp\mathbf{z}}&0\_{\left(\sharp\text{in}-\sharp\mathbf{z}\right)\times\left(\sharp\text{in}-\sharp\mathbf{z}\right)}\end{array}\right]\right). |  | (3.14) |

  Here, 0P×Q0\_{P\times Q} denotes the null matrix of dimensions P×QP\times Q,
  vec​(⋅)\text{vec}\left(\cdot\right) denotes the vectorization of a matrix,
  ♯\sharp indicates the number of points of a given grid in one direction
  and Ω∈ℝ♯​𝐳×♯​𝐳\Omega\in\mathbb{R}^{\sharp\mathbf{z}\times\sharp\mathbf{z}}
  is the matrix whose entries are the coefficients ωl1​l2\omega\_{l\_{1}l\_{2}}
  defined by ([3.5](https://arxiv.org/html/2511.02700v1#S3.E5 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")). For an example of a matrix CC, we refer to Appendix [B](https://arxiv.org/html/2511.02700v1#A2 "Appendix B Summation operator as a circulant matrix-vector multiplication ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").

  The matrix-vector
  multiplication C​aCa, for any given vector a∈ℝ(♯​in)2×1a\in\mathbb{R}^{\left(\sharp\text{in}\right)^{2}\times 1},
  can be obtained by two (1-dimensional) FFTs and one (1-dimensional)
  inverse FFT, requiring just O​((♯​in)2⋅log⁡♯​in)O\left(\left(\sharp\text{in}\right)^{2}\cdot\log\sharp\text{in}\right)
  elementary operations. The pertinent formula is

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | C​a=ifft​(fft​(C1,⋅)H∘fft​(a)),Ca=\text{ifft}\left(\text{fft}\left(C\_{1,\cdot}\right)^{H}\circ\text{fft}\left(a\right)\right), |  | (3.15) |

  where H denotes the complex conjugate.
* ∙\bullet

  I~∈ℝ(♯​out)2×(♯​in)2\tilde{I}\in\mathbb{R}^{\left(\sharp\text{out}\right)^{2}\times\left(\sharp\text{in}\right)^{2}}
  is obtained from the identity matrix I∈ℝ(♯​in)2×(♯​in)2I\in\mathbb{R}^{\left(\sharp\text{in}\right)^{2}\times\left(\sharp\text{in}\right)^{2}}
  by removing the rows corresponding to the zeros in the following vector

  |  |  |  |
  | --- | --- | --- |
  |  | vec​([1♯​out×♯​out0♯​out×(♯​in−♯​out)0(♯​in−♯​out)×♯​out0(♯​in−♯​out)×(♯​in−♯​out)]).\text{vec}\left(\left[\begin{array}[]{cc}1\_{\sharp\text{out}\times\sharp\text{out}}&0\_{\sharp\text{out}\times\left(\sharp\text{in}-\sharp\text{out}\right)}\\ 0\_{\left(\sharp\text{in}-\sharp\text{out}\right)\times\sharp\text{out}}&0\_{\left(\sharp\text{in}-\sharp\text{out}\right)\times\left(\sharp\text{in}-\sharp\text{out}\right)}\end{array}\right]\right). |  |

  Here, 1P×P1\_{P\times P} denotes a P×PP\times P matrix whose elements
  are all equal to 1. We note that the matrix-vector multiplication
  C​v​(𝐲in,t)Cv\left(\mathbf{y}^{\text{in}},t\right) in ([3.13](https://arxiv.org/html/2511.02700v1#S3.E13 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
  returns a value also for grid points that can be discarded. The purpose
  of I~\tilde{I} is precisely to extract only those entries that correspond
  to (ℬω​v)​(𝐲out,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{y}^{\text{out}},t\right).

In order to obtain an approximation to (ℬω​v)​(𝐱,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right)
using ([3.13](https://arxiv.org/html/2511.02700v1#S3.E13 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
we need to interpolate both the input and the output value in ([3.13](https://arxiv.org/html/2511.02700v1#S3.E13 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
since 𝐲in\mathbf{y}^{\text{in}} and 𝐲out\mathbf{y}^{\text{out}} are
generally different from 𝐱\mathbf{x}. Let Tin∈ℝ(♯​in)2×(Nx+1)2T^{\text{in}}\in\mathbb{R}^{\left(\sharp\text{in}\right)^{2}\times\left(N\_{x}+1\right)^{2}}
be a matrix representing an interpolation procedure from the 𝐱\mathbf{x}
grid to the 𝐲in\mathbf{y}^{\text{in}} grid and let Tout∈ℝ(Nx+1)2×(♯​in)2T^{\text{out}}\in\mathbb{R}^{\left(N\_{x}+1\right)^{2}\times\left(\sharp\text{in}\right)^{2}}
be a matrix representing an interpolation procedure from the 𝐲out\mathbf{y}^{\text{out}}
grid to the 𝐱\mathbf{x} grid. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(𝐲in,t)\displaystyle v\left(\mathbf{y}^{\text{in}},t\right) | ≃Tin​v​(𝐱,t),\displaystyle\simeq T^{\text{in}}v\left(\mathbf{x},t\right), |  | (3.16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (ℬω​v)​(𝐱,t)\displaystyle\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right) | ≃Tout​(ℬω​v)​(𝐲out,t).\displaystyle\simeq T^{\text{out}}\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{y}^{\text{out}},t\right). |  | (3.17) |

Note that, by using Lagrange interpolation, the interpolation matrices
are sparse and have at most P+1P+1 nonzero entries per row, where
PP is the polynomial degree. Let MM be the number of rows, it
follows that the corresponding matrix–vector multiplications require
a number of operations of order O​(M​P)O\left(MP\right), and are therefore
negligible compared with multiplication performed via FFT.

From ([3.13](https://arxiv.org/html/2511.02700v1#S3.E13 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
([3.16](https://arxiv.org/html/2511.02700v1#S3.E16 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) and ([3.17](https://arxiv.org/html/2511.02700v1#S3.E17 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
we arrive at the approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℬω​v)​(𝐱,t)≃Bω​v​(𝐱,t),\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right)\simeq B\_{\omega}v\left(\mathbf{x},t\right), |  | (3.18) |

where Bω∈ℝ(Nx+1)2×(Nx+1)2B\_{\omega}\in\mathbb{R}^{\left(N\_{x}+1\right)^{2}\times\left(N\_{x}+1\right)^{2}}
is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bω=Tout​I~​C​Tin.B\_{\omega}=T^{\text{out}}\tilde{I}CT^{\text{in}}. |  | (3.19) |

We emphasize that BωB\_{\omega} is only used for notational purposes
and never explicitly computed. To compute the right-hand side of ([3.18](https://arxiv.org/html/2511.02700v1#S3.E18 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
we always use

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bω​V=Tout​I~​ifft​(fft​(C1,⋅)H∘fft​(Tin​V)),B\_{\omega}V=T^{\text{out}}\tilde{I}\,\text{ifft}\left(\text{fft}\left(C\_{1,\cdot}\right)^{H}\circ\text{fft}\left(T^{\text{in}}V\right)\right), |  | (3.20) |

for any vector V∈ℝ(Nx+1)2×1V\in\mathbb{R}^{\left(N\_{x}+1\right)^{2}\times 1}.
Figure

Figure 2: Diagram
of the scheme used to approximate (ℬω​v)​(𝐱,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| \begin{array}[]{c}\\ \\ \end{array} | v​(𝐱,t)v\left(\mathbf{x},t\right) |  | (ℬω​v)​(𝐱,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{x},t\right) |  |
| interpolationfrom 𝐱 to ​𝐲in\begin{array}[]{c}\text{interpolation}\\ \text{from $\mathbf{x}$ to }\mathbf{y}^{\text{in}}\end{array} | ↓\downarrow |  | ↑\uparrow | interpolationfrom 𝐲out to ​𝐱\begin{array}[]{c}\text{interpolation}\\ \text{from $\mathbf{y}^{\text{out}}$ to }\mathbf{x}\end{array} |
| \begin{array}[]{c}\\ \\ \end{array} | v​(𝐲in,t)v\left(\mathbf{y}^{\text{in}},t\right) | → \xrightarrow{\text{\hskip 85.35826pt}} | (ℬω​v)​(𝐲out,t)\left(\mathcal{B}\_{\omega}v\right)\left(\mathbf{y}^{\text{out}},t\right) |  |
|  |  | matrix-vectormultiplication by FFT\begin{array}[]{c}\text{matrix-vector}\\ \text{multiplication by FFT}\end{array} |  |  |

[2](https://arxiv.org/html/2511.02700v1#S3.F2 "Figure 2 ‣ 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")
provides a schematic illustration of how FFT and interpolation are
combined to evaluate ([3.20](https://arxiv.org/html/2511.02700v1#S3.E20 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).

#### 3.2.3 Cell averaging

We conclude the spatial discretization with a technique for handling
the non-smoothness of the initial function ϕ\phi of ([2.8](https://arxiv.org/html/2511.02700v1#S2.E8 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).
As it turns out, pointwise valuation of ϕ\phi over the spatial
grid can lead to deteriorated (spatial) convergence behaviour, which
can be alleviated by applying cell averaging.

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | xm+12\displaystyle x\_{m+\frac{1}{2}} | =12​(xm+xm+1)(m=0,1,…,Nx−1)\displaystyle=\frac{1}{2}\left(x\_{m}+x\_{m+1}\right)\qquad\left(m=0,1,\ldots,N\_{x}-1\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | hx,m+12\displaystyle h\_{x,m+\frac{1}{2}} | =xm+12−xm−12(m=0,1,…,Nx)\displaystyle=x\_{m+\frac{1}{2}}-x\_{m-\frac{1}{2}}\qquad\left(m=0,1,\ldots,N\_{x}\right) |  |

with x−12=−x12x\_{-\frac{1}{2}}=-x\_{\frac{1}{2}} and xNx+12=2​xmax−xNx−12x\_{N\_{x}+\frac{1}{2}}=2x\_{\max}-x\_{N\_{x}-\frac{1}{2}}.
Then, we use the approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(xm1​m2,0)≃1hx,m1+12​hx,m2+12​∫xm1−12xm1+12∫xm2−12xm2+12ϕ​(x1,x2)​𝑑x2​𝑑x1,v\left(x\_{m\_{1}m\_{2}},0\right)\simeq\frac{1}{h\_{x,m\_{1}+\frac{1}{2}}h\_{x,m\_{2}+\frac{1}{2}}}\int\_{x\_{m\_{1}-\frac{1}{2}}}^{x\_{m\_{1}+\frac{1}{2}}}\int\_{x\_{m\_{2}-\frac{1}{2}}}^{x\_{m\_{2}+\frac{1}{2}}}\phi\left(x\_{1},x\_{2}\right)dx\_{2}dx\_{1}, |  | (3.21) |

whenever the cell [xm1−12,xm1+12)×[xm2−12,xm2+12)\left[x\_{m\_{1}-\frac{1}{2}},x\_{m\_{1}+\frac{1}{2}}\right)\times\left[x\_{m\_{2}-\frac{1}{2}},x\_{m\_{2}+\frac{1}{2}}\right)
has a nonempty intersection with the set of non-smoothness of ϕ\phi.

### 3.3 Temporal discretization: the semi-Lagrangian θ\theta-method

The problem ([3.8](https://arxiv.org/html/2511.02700v1#S3.E8 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) can be convection-dominated.
To account for this, we shall consider temporal discretization using
the θ\theta-method combined with the semi-Lagrangian approach, as
described by Spiegelman & Katz ([2006](https://arxiv.org/html/2511.02700v1#bib.bib23)). The semi-Lagrangian method follows,
in each time step, the characteristics backwards in time to determine
the departure points of the spatial grid points.

Let x:[0,T]→ℝ≥02x:\left[0,T\right]\rightarrow\mathbb{R}\_{\geq 0}^{2} and v∗:[0,T]→ℝv^{\*}:\left[0,T\right]\rightarrow\mathbb{R}
such that v∗​(t)=v​(x​(t),t)v^{\*}\left(t\right)=v\left(x\left(t\right),t\right).
The derivative of v∗v^{\*} is given by

|  |  |  |
| --- | --- | --- |
|  | vt∗​(t)=vt​(x​(t),t)+xt​(t)⊤​vx​(x​(t),t).v\_{t}^{\*}\left(t\right)=v\_{t}\left(x\left(t\right),t\right)+x\_{t}\left(t\right)^{\top}v\_{x}\left(x\left(t\right),t\right). |  |

Assume xx satisfies the following (linear) ODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt​(t)=−μω​(x​(t))(0<t≤T).x\_{t}\left(t\right)=-\mu\_{\omega}\left(x\left(t\right)\right)\qquad\left(0<t\leq T\right). |  | (3.22) |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt∗​(t)=(𝒜ωSL−rω)​v​(x​(t),t)(0<t≤T),v\_{t}^{\*}\left(t\right)=\left(\mathcal{A}\_{\omega}^{\text{SL}}-r\_{\omega}\right)v\left(x\left(t\right),t\right)\qquad\left(0<t\leq T\right), |  | (3.23) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝒜ωSL​v​(x,t)=12​𝟏⊤​(vx​x​(x,t)∘Σω​Σω⊤​(x))​𝟏+(ℬω​v)​(x,t).\mathcal{A}\_{\omega}^{\text{SL}}v\left(x,t\right)=\frac{1}{2}\mathbf{1}^{\top}\left(v\_{xx}\left(x,t\right)\circ\Sigma\_{\omega}\Sigma\_{\omega}^{\top}\left(x\right)\right)\mathbf{1}+\left(\mathcal{B}\_{\omega}v\right)\left(x,t\right). |  |

Clearly, 𝒜ωSL\mathcal{A}\_{\omega}^{\text{SL}} is obtained from 𝒜ω\mathcal{A}\_{\omega}
by omitting the convection term.

Let parameter θ∈[0,1]\theta\in\left[0,1\right]. Let 𝐭=(tn)n=0Nt\mathbf{t}=\left(t\_{n}\right)\_{n=0}^{N\_{t}}
be any given uniform grid with step size ht=TNth\_{t}=\frac{T}{N\_{t}}.
For any given n=1,2,…,Ntn=1,2,\ldots,N\_{t}, approximating ([3.23](https://arxiv.org/html/2511.02700v1#S3.E23 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
using the θ\theta-method and substituting the definition of v∗v^{\*},
we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(x​(tn),tn)−v​(x​(tn−1),tn−1)ht≃θ​(𝒜ωSL−rω)​v​(x​(tn),tn)+(1−θ)​(𝒜ωSL−rω)​v​(x​(tn−1),tn−1).\frac{v\left(x\left(t\_{n}\right),t\_{n}\right)-v\left(x\left(t\_{n-1}\right),t\_{n-1}\right)}{h\_{t}}\simeq\theta\left(\mathcal{A}\_{\omega}^{\text{SL}}-r\_{\omega}\right)v\left(x\left(t\_{n}\right),t\_{n}\right)+\left(1-\theta\right)\left(\mathcal{A}\_{\omega}^{\text{SL}}-r\_{\omega}\right)v\left(x\left(t\_{n-1}\right),t\_{n-1}\right). |  | (3.24) |

The approximation ([3.24](https://arxiv.org/html/2511.02700v1#S3.E24 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) holds along
any trajectory satisfying ([3.22](https://arxiv.org/html/2511.02700v1#S3.E22 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).
In each given time step from tn−1t\_{n-1} to tnt\_{n}, the semi-Lagrangian
approach involves selecting the set of trajectories that intersect
the points (𝐱,tn)\left(\mathbf{x},t\_{n}\right), ensuring that an approximation
is defined on the fixed grid 𝐱\mathbf{x}. Let 𝐱SL\mathbf{x}^{\text{SL}}
denote the grid corresponding to tn−1t\_{n-1} along this set of trajectories.
Its elements are given by xm1​m2SL=(xm1SL,xm2SL)x\_{m\_{1}m\_{2}}^{\text{SL}}=\left(x\_{m\_{1}}^{\text{SL}},x\_{m\_{2}}^{\text{SL}}\right)
where xmiSLx\_{m\_{i}}^{\text{SL}} is obtained by ([3.22](https://arxiv.org/html/2511.02700v1#S3.E22 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
as

|  |  |  |
| --- | --- | --- |
|  | xmiSL=xmi​eκω(i)​ht(mi=0,1,…,Nx).x\_{m\_{i}}^{\text{SL}}=x\_{m\_{i}}e^{\kappa\_{\omega}^{\left(i\right)}h\_{t}}\qquad\left(m\_{i}=0,1,\ldots,N\_{x}\right). |  |

Then ([3.24](https://arxiv.org/html/2511.02700v1#S3.E24 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) becomes

|  |  |  |
| --- | --- | --- |
|  | v​(𝐱,tn)−v​(𝐱SL,tn−1)ht≃θ​(𝒜ωSL−rω)​v​(𝐱,tn)+(1−θ)​(𝒜ωSL−rω)​v​(𝐱SL,tn−1).\frac{v\left(\mathbf{x},t\_{n}\right)-v\left(\mathbf{x}^{\text{SL}},t\_{n-1}\right)}{h\_{t}}\simeq\theta\left(\mathcal{A}\_{\omega}^{\text{SL}}-r\_{\omega}\right)v\left(\mathbf{x},t\_{n}\right)+\left(1-\theta\right)\left(\mathcal{A}\_{\omega}^{\text{SL}}-r\_{\omega}\right)v\left(\mathbf{x}^{\text{SL}},t\_{n-1}\right). |  |

Interpolation is employed to acquire approximations at the grid 𝐱SL\mathbf{x}^{\text{SL}}.
Let TSL∈ℝ(Nx+1)2×(Nx+1)2T^{\text{SL}}\in\mathbb{R}^{\left(N\_{x}+1\right)^{2}\times\left(N\_{x}+1\right)^{2}}
be a matrix representing an interpolation procedure from the 𝐱\mathbf{x}
grid to the 𝐱SL\mathbf{x}^{\text{SL}} grid. Together with the approximation
of the diffusion and summation terms, discussed in Section [3.2](https://arxiv.org/html/2511.02700v1#S3.SS2 "3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"),
we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(𝐱SL,tn−1)\displaystyle v\left(\mathbf{x}^{\text{SL}},t\_{n-1}\right) | ≃TSL​v​(𝐱,tn−1),\displaystyle\simeq T^{\text{SL}}v\left(\mathbf{x},t\_{n-1}\right), |  | (3.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒜ωSL−rω)​v​(𝐱,tn)\displaystyle\left(\mathcal{A}\_{\omega}^{\text{SL}}-r\_{\omega}\right)v\left(\mathbf{x},t\_{n}\right) | ≃(D+Bω−rω​I)​v​(𝐱,tn),\displaystyle\simeq\left(D+B\_{\omega}-r\_{\omega}I\right)v\left(\mathbf{x},t\_{n}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒜ωSL−rω)​v​(𝐱SL,tn−1)\displaystyle\left(\mathcal{A}\_{\omega}^{\text{SL}}-r\_{\omega}\right)v\left(\mathbf{x}^{\text{SL}},t\_{n-1}\right) | ≃TSL​(D+Bω−rω​I)​v​(𝐱,tn−1).\displaystyle\simeq T^{\text{SL}}\left(D+B\_{\omega}-r\_{\omega}I\right)v\left(\mathbf{x},t\_{n-1}\right). |  |

This leads to the following natural definition of the approximation
VnV^{n} to the exact solution vector v​(𝐱,tn)v\left(\mathbf{x},t\_{n}\right):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−ht​θ​(D+Bω−rω​I))​Vn=TSL​(I+ht​(1−θ)​(D+Bω−rω​I))​Vn−1\left(I-h\_{t}\theta\left(D+B\_{\omega}-r\_{\omega}I\right)\right)V^{n}=T^{\text{SL}}\left(I+h\_{t}\left(1-\theta\right)\left(D+B\_{\omega}-r\_{\omega}I\right)\right)V^{n-1} |  | (3.26) |

for n=1,2,…,Ntn=1,2,\ldots,N\_{t}. The initial vector V0V^{0} is defined
by pointwise valuation on the spatial grid 𝐱\mathbf{x} of the pay-off
function ϕ\phi, except near the set of non-smoothness, where cell
averaging is employed (see Section [3.2.3](https://arxiv.org/html/2511.02700v1#S3.SS2.SSS3 "3.2.3 Cell averaging ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")).
The time-stepping scheme ([3.26](https://arxiv.org/html/2511.02700v1#S3.E26 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) is called
the semi-Lagrangian θ\theta-method. We shall apply ([3.26](https://arxiv.org/html/2511.02700v1#S3.E26 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
with θ=12\theta=\frac{1}{2}, which is also called the semi-Lagrangian
Crank–Nicolson method. Here, to account for the non-smoothness of
ϕ\phi, a damping procedure is used where the first time step (i.e.
n=1n=1) is replaced by four time steps of size equal to 14​ht\frac{1}{4}h\_{t}
of ([3.26](https://arxiv.org/html/2511.02700v1#S3.E26 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) with θ=1\theta=1.

It remains to consider the treatment of the discretized integral term
in ([3.26](https://arxiv.org/html/2511.02700v1#S3.E26 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")), represented formally by the
matrix BωB\_{\omega}. Recall from Section [3.2.2](https://arxiv.org/html/2511.02700v1#S3.SS2.SSS2 "3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")
that BωB\_{\omega} is never actually computed. To effectively handle
this term, we shall employ fixed-point iteration:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−ht​θ​(D−rω​I))​Yn,k=ht​θ​Bω​Yn,k−1+TSL​(I+ht​(1−θ)​(D−rω​I))​Vn−1+ht​(1−θ)​TSL​Bω​Vn−1\left(I-h\_{t}\theta\left(D-r\_{\omega}I\right)\right)Y^{n,k}=h\_{t}\theta B\_{\omega}Y^{n,k-1}+T^{\text{SL}}\left(I+h\_{t}\left(1-\theta\right)\left(D-r\_{\omega}I\right)\right)V^{n-1}+h\_{t}\left(1-\theta\right)T^{\text{SL}}B\_{\omega}V^{n-1} |  | (3.27) |

for k=1,2,…k=1,2,\ldots. Here matrix-vector multiplications involving
BωB\_{\omega} are always computed by the efficient FFT algorithm of
Section [3.2.2](https://arxiv.org/html/2511.02700v1#S3.SS2.SSS2 "3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"). For a given
tolerance t​o​l>0tol>0 sufficiently small, we use the following stopping
criterion

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxm1,m2⁡|Ym1​m2n,k−Ym1​m2n,k−1|max⁡{1,|Ym1​m2n,k|}<t​o​l\max\_{m\_{1},m\_{2}}\frac{\left|Y\_{m\_{1}m\_{2}}^{n,k}-Y\_{m\_{1}m\_{2}}^{n,k-1}\right|}{\max\left\{1,\left|Y\_{m\_{1}m\_{2}}^{n,k}\right|\right\}}<tol |  | (3.28) |

and define Vn=Yn,kV^{n}=Y^{n,k}.

The starting vector Yn,0Y^{n,0} for the fixed-point iteration is commonly
chosen in the literature as Yn,0=Vn−1Y^{n,0}=V^{n-1}. Here, we shall consider
a more accurate starting vector, defined by higher-order extrapolation
from known approximations at previous temporal grid points:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yn,0={Vn−1n=1,2​Vn−1−Vn−2n=2,3​Vn−1−3​Vn−2+Vn−3n=3,4​Vn−1−6​Vn−2+4​Vn−3−Vn−4n≥4.Y^{n,0}=\begin{cases}V^{n-1}&n=1,\\ 2V^{n-1}-V^{n-2}&n=2,\\ 3V^{n-1}-3V^{n-2}+V^{n-3}&n=3,\\ 4V^{n-1}-6V^{n-2}+4V^{n-3}-V^{n-4}&n\geq 4.\end{cases} |  | (3.29) |

This yields a significant reduction in the number of fixed-point iterations
compared to the common choice.

Finally, for the linear system in ([3.27](https://arxiv.org/html/2511.02700v1#S3.E27 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
we apply the BiCGSTAB iterative solver using an ILU preconditioner.

Our complete algorithm for the numerical solution of problem ([2.8](https://arxiv.org/html/2511.02700v1#S2.E8 "In 2.2 Initial boundary value problem for derivatives pricing ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
is outlined in Algorithm [1](https://arxiv.org/html/2511.02700v1#algorithm1 "Algorithm 1 ‣ 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").

Algorithm 1  Outline of the algorithm

precomputations:

∙\bullet
:   define the grids 𝐳\mathbf{z}, 𝐱\mathbf{x}, 𝐲in\mathbf{y}^{\text{in}},
    𝐲out\mathbf{y}^{\text{out}}, 𝐭\mathbf{t} and 𝐱SL\mathbf{x}^{\text{SL}}

∙\bullet
:   define the matrix DD given by ([3.11](https://arxiv.org/html/2511.02700v1#S3.E11 "In 3.2.1 Diffusion term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
    and compute the ILU factorization of I−ht​θ​(D−rω​I)I-h\_{t}\theta\left(D-r\_{\omega}I\right)

∙\bullet
:   define the vector C1,⋅C\_{1,\cdot} given by ([3.14](https://arxiv.org/html/2511.02700v1#S3.E14 "In 1st item ‣ 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
    and compute fft​(C1,⋅)\text{fft}\left(C\_{1,\cdot}\right)

∙\bullet
:   define the matrices TinT^{\text{in}}, ToutT^{\text{out}}
    and TSLT^{\text{SL}} given by ([3.16](https://arxiv.org/html/2511.02700v1#S3.E16 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")),
    ([3.17](https://arxiv.org/html/2511.02700v1#S3.E17 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) and ([3.25](https://arxiv.org/html/2511.02700v1#S3.E25 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))

∙\bullet
:   choose θ=12\theta=\frac{1}{2}

time-stepping:

:   compute V0=ϕ​(𝐱)V^{0}=\phi\left(\mathbf{x}\right)
    and apply cell averaging ([3.21](https://arxiv.org/html/2511.02700v1#S3.E21 "In 3.2.3 Cell averaging ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
:   for n=1,2,…,Ntn=1,2,\ldots,N\_{t}

    1.
    :   compute Bω​Vn−1B\_{\omega}V^{n-1} using ([3.20](https://arxiv.org/html/2511.02700v1#S3.E20 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))

    2.
    :   compute Wn−1=TSL​(I+ht​(1−θ)​(D−rω​I))​Vn−1+ht​(1−θ)​TSL​Bω​Vn−1W^{n-1}=T^{\text{SL}}\left(I+h\_{t}\left(1-\theta\right)\left(D-r\_{\omega}I\right)\right)V^{n-1}+h\_{t}\left(1-\theta\right)T^{\text{SL}}B\_{\omega}V^{n-1}

    3.
    :   compute Yn,0Y^{n,0} given by ([3.29](https://arxiv.org/html/2511.02700v1#S3.E29 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))

    4.
    :   for k=1,2,…k=1,2,\ldots

        i.
        :   compute Bω​Yn,k−1B\_{\omega}Y^{n,k-1} using ([3.20](https://arxiv.org/html/2511.02700v1#S3.E20 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))

        ii.
        :   solve (I−ht​θ​(D−rω​I))​Yn,k=ht​θ​Bω​Yn,k−1+Wn−1\left(I-h\_{t}\theta\left(D-r\_{\omega}I\right)\right)Y^{n,k}=h\_{t}\theta B\_{\omega}Y^{n,k-1}+W^{n-1}
            using BiCGSTAB

    5.
    :   end for if Yn,kY^{n,k} satisfies ([3.28](https://arxiv.org/html/2511.02700v1#S3.E28 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))

    6.
    :   let Vn=Yn,kV^{n}=Y^{n,k}
:   end for

## 4 Numerical experiments

We consider an European put-on-the-average option, which has the pay-off
function

|  |  |  |
| --- | --- | --- |
|  | ϕ​(x)=max⁡(K−12​(x(1)+x(2)),0)\phi\left(x\right)=\max\left(K-\frac{1}{2}\left(x^{\left(1\right)}+x^{\left(2\right)}\right),0\right) |  |

with fixed strike price K>0K>0. Clearly, ϕ\phi is non-smooth over
the set {x∈ℝ≥02:x(1)+x(2)=2​K}\left\{x\in\mathbb{R}\_{\geq 0}^{2}:x^{\left(1\right)}+x^{\left(2\right)}=2K\right\}.
To define the non-uniform grid 𝐱\mathbf{x}, we use the same transformation φ\varphi as in in ’t Hout & Lamotte ([2023](https://arxiv.org/html/2511.02700v1#bib.bib11)). Let cc, xintx\_{\rm int} be two given positive numbers. We choose the function φ\varphi in Section [3.2](https://arxiv.org/html/2511.02700v1#S3.SS2 "3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models") as

|  |  |  |
| --- | --- | --- |
|  | φ​(ξ)={c​ξ0≤ξ≤ξint,xint+c​sinh⁡(ξ−ξint)ξint<ξ≤ξmax,\varphi\left(\xi\right)=\begin{cases}c\xi&0\leq\xi\leq\xi\_{\rm int},\\ x\_{\rm int}+c\sinh\left(\xi-\xi\_{\rm int}\right)&\xi\_{\rm int}<\xi\leq\xi\_{\rm max},\end{cases} |  |

with

|  |  |  |
| --- | --- | --- |
|  | ξint=xintc,ξmax=ξint+sinh−1⁡(xmax−xintc).\xi\_{\rm int}=\frac{x\_{\rm int}}{c},\quad\xi\_{\rm max}=\xi\_{\rm int}+\sinh^{-1}\left(\frac{x\_{\rm max}-x\_{\rm int}}{c}\right). |  |

In this way, the resulting spatial grid in each direction is uniform over [0,xint]\left[0,x\_{\rm int}\right], whereas in [xint,xmax]\left[x\_{\rm int},x\_{\rm max}\right] the distance between consecutive grid points gradually increases as one moves away from xintx\_{\rm int}. The limit of the fraction of spatial grid points within the interval [0,xint]\left[0,x\_{\rm int}\right]
as Nx→∞N\_{x}\rightarrow\infty, denoted by FF, is given
by

|  |  |  |
| --- | --- | --- |
|  | F=ξintξmax=(1+cxint​sinh−1⁡(xmax−xintc))−1.F=\frac{\xi\_{\rm int}}{\xi\_{\rm max}}=\left(1+\frac{c}{x\_{\rm int}}\sinh^{-1}\left(\frac{x\_{\rm max}-x\_{\rm int}}{c}\right)\right)^{-1}. |  |

Note that F→xintxmaxF\rightarrow\frac{x\_{\rm int}}{x\_{\rm max}}
as c→∞c\rightarrow\infty, which corresponds to the uniform
case.

Moving on to the Lévy measure, we model the jump component in ([2.1](https://arxiv.org/html/2511.02700v1#S2.E1 "In 2.1 Market model ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
by a pure-jump 2-dimensional Normal Tempered Stable process. It is
characterized by the parameters 0≤α<10\leq\alpha<1, δ>0\delta>0, λ>0\lambda>0,
η∈ℝ2×1\eta\in\mathbb{R}^{2\times 1} and a positive definite symmetric
matrix ρ∈ℝ2×2\rho\in\mathbb{R}^{2\times 2}. The case where α=0\alpha=0 is known as Variance Gamma, while the case where α=12\alpha=\frac{1}{2} is known as Normal Inverse Gaussian. Both are commonly used to model financial dynamics. The Lévy measure is given
by

|  |  |  |
| --- | --- | --- |
|  | ℓ​(z)=δπ​(‖η‖ρ2+2​λ)1+αdet[ρ]​K1+α​(‖η‖ρ2+2​λ​‖z‖ρ)​‖z‖ρ−1−α​e⟨η,z⟩ρ\ell\left(z\right)=\frac{\delta}{\pi}\sqrt{\frac{\left(\left\|\eta\right\|\_{\rho}^{2}+2\lambda\right)^{1+\alpha}}{\det\left[\rho\right]}}K\_{1+\alpha}\left(\sqrt{\left\|\eta\right\|\_{\rho}^{2}+2\lambda}\left\|z\right\|\_{\rho}\right)\left\|z\right\|\_{\rho}^{-1-\alpha}e^{\left\langle\eta,z\right\rangle\_{\rho}} |  |

where Kν​(τ)=12​∫0∞yν−1​e−12​τ​(y+y−1)​𝑑yK\_{\nu}\left(\tau\right)=\frac{1}{2}\int\_{0}^{\infty}y^{\nu-1}e^{-\frac{1}{2}\tau\left(y+y^{-1}\right)}dy, for τ>0\tau>0,
denotes the modified Bessel function of the second kind,666See Schoutens ([2003](https://arxiv.org/html/2511.02700v1#bib.bib22), Appendix A).
⟨x,y⟩ρ=x⊤​ρ−1​y\left\langle x,y\right\rangle\_{\rho}=x^{\top}\rho^{-1}y and ‖x‖ρ=⟨x,x⟩ρ\left\|x\right\|\_{\rho}=\sqrt{\left\langle x,x\right\rangle\_{\rho}}
is its induced norm. The constants Aℓ,BℓA\_{\ell},B\_{\ell} and CℓC\_{\ell}
in ([2.5](https://arxiv.org/html/2511.02700v1#S2.E5 "In 2.1 Market model ‣ 2 Model framework ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) are
defined, with respect to ∥⋅∥ρ\left\|\cdot\right\|\_{\rho}, as

|  |  |  |
| --- | --- | --- |
|  | (Aℓ,Bℓ,Cℓ​(h))=(2​α,‖η‖ρ2+2​λ−‖η‖ρ,2α​δ​Γ​(1+α)π​det[ρ]​eh​‖η‖ρ).\left(A\_{\ell},B\_{\ell},C\_{\ell}\left(h\right)\right)=\left(2\alpha,\sqrt{\left\|\eta\right\|\_{\rho}^{2}+2\lambda}-\left\|\eta\right\|\_{\rho},\frac{2^{\alpha}\delta\Gamma\left(1+\alpha\right)}{\pi\sqrt{\det\left[\rho\right]}}e^{h\left\|\eta\right\|\_{\rho}}\right). |  |

The variance of the random variable L​(t)=∫0t∫ℝ∗2z​Π~​(d​t,d​z)L\left(t\right)=\int\_{0}^{t}\int\_{\mathbb{R}\_{\*}^{2}}z\tilde{\Pi}\left(dt,dz\right), for t∈[0,T]t\in\left[0,T\right],
is given by

|  |  |  |
| --- | --- | --- |
|  | 𝕍​[L​(t)]=t⋅δ​Γ​(2−α)λ2−α​(ρ​λ1−α+η​η⊤).\mathbb{V}\left[L\left(t\right)\right]=t\cdot\delta\frac{\Gamma\left(2-\alpha\right)}{\lambda^{2-\alpha}}\left(\rho\lambda^{1-\alpha}+\eta\eta^{\top}\right). |  |

We refer to Appendix [A](https://arxiv.org/html/2511.02700v1#A1 "Appendix A 𝑑-dimensional Normal Tempered Stable process ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models") for
further details.

Table [1](https://arxiv.org/html/2511.02700v1#S4.T1 "Table 1 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")

Table 1: Parameter
sets

| Parameters | VG0 | VG1 | NIG0 | NIG1 |
| --- | --- | --- | --- | --- |
| α\alpha | 0 | 0 | 12\frac{1}{2} | 12\frac{1}{2} |
| λ\lambda | 1 | 6 | 20766.4 | 57.1108 |
| δ\delta | 1 | 6 | 0.77576 | 4.26367 |
| η(1)\eta^{\left(1\right)} | -0.1 | -0.1 | -37.688 | -0.295846 |
| η(2)\eta^{\left(2\right)} | -0.2 | -0.2 | -2.224 | -0.292984 |
| ρ(1,1)\rho^{\left(1,1\right)} | 0.09 | 0.01 | 3.984 | 0.037021 |
| ρ(1,2)\rho^{\left(1,2\right)} | 0.06 | 0 | 3.160 | 0.026574 |
| ρ(2,2)\rho^{\left(2,2\right)} | 0.16 | 0.0225 | 3.512 | 0.054613 |
| rr | 0.05 | 0 | 0 | 0 |
| TT | 1 | 12\frac{1}{2} | 12\frac{1}{2} | 12\frac{1}{2} |
| KK | 100 | 100 | 100 | 100 |

lists four sets of representative parameter values where we always take the diffusion matrix σ\sigma equal to zero. Table [2](https://arxiv.org/html/2511.02700v1#S4.T2 "Table 2 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")

Table 2: Standard deviation and correlation coefficient

|  | VG0 | VG1 | NIG0 | NIG1 |
| --- | --- | --- | --- | --- |
| 𝕍​[L(1)​(1)]\sqrt{\mathbb{V}\left[L^{\left(1\right)}\left(1\right)\right]} | 0.3162 | 0.1080 | 0.1958 | 0.1943 |
| 𝕍​[L(2)​(1)]\sqrt{\mathbb{V}\left[L^{\left(2\right)}\left(1\right)\right]} | 0.4472 | 0.1707 | 0.1830 | 0.2352 |
| cov​[L(1)​(1),L(2)​(1)]𝕍​[L(1)​(1)]​𝕍​[L(2)​(1)]\frac{\textrm{cov}\left[L^{\left(1\right)}\left(1\right),L^{\left(2\right)}\left(1\right)\right]}{\sqrt{\mathbb{V}\left[L^{\left(1\right)}\left(1\right)\right]\mathbb{V}\left[L^{\left(2\right)}\left(1\right)\right]}} | 0.5656 | 0.1807 | 0.8417 | 0.5975 |

contains the corresponding standard deviations and correlation coefficients.
The sets VG0 and NIG0 are taken from Hilber et al. ([2013](https://arxiv.org/html/2511.02700v1#bib.bib10), page 208)
and Rydberg ([1997](https://arxiv.org/html/2511.02700v1#bib.bib20), Figure 8), respectively. The VG1 set was
designed by us based on VG0. Finally, the NIG1 set was obtained via
standard maximum likelihood estimation777The density function for the case where α∈{0,12}\alpha\in\left\{0,\frac{1}{2}\right\}
can be found in Appendix [A](https://arxiv.org/html/2511.02700v1#A1 "Appendix A 𝑑-dimensional Normal Tempered Stable process ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"). using the close price data of S&P500 (^GSPC) and
EUROSTOXX50 (^STOXX50E), retrieved from Yahoo Finance,
covering the period from 01/01/2014 to 31/12/2024. In particular,
we apply the methodology used by Hainaut & Le Courtois ([2014](https://arxiv.org/html/2511.02700v1#bib.bib9)) to the logarithmic
return of the price, i.e. d​ln⁡Xd\ln X.

The following list specifies all choices for the values of the parameters of our numerical scheme:

* ∙\bullet

  Nz=2​NxN\_{z}=2N\_{x} and Nt=round​[12​Nx]N\_{t}=\text{round}\left[\frac{1}{2}N\_{x}\right].
  Clearly, with this choice, the three mesh widths are directly proportional
  to each other.
* ∙\bullet

  zmax𝐈=2​hzz\_{\max}^{\mathbf{I}}=2h\_{z}. This choice is motivated by the fact
  that the artificial diffusion acts over a small region around the
  origin.
* ∙\bullet

  zmax𝐈𝐈=0.1​zmax𝐈𝐈𝐈z\_{\max}^{\mathbf{II}}=\sqrt{0.1}z\_{\max}^{\mathbf{III}}. In this
  way, the size of Rz𝐈𝐈R\_{z}^{\mathbf{II}} is about 10% of the full integration domain RzR\_{z}.
* ∙\bullet

  zmax𝐈𝐈𝐈=max⁡{‖z‖∞:z∈ℝ2,ℓ​(z)=10−8}z\_{\max}^{\mathbf{III}}=\max\left\{\left\|z\right\|\_{\infty}:z\in\mathbb{R}^{2},\ell\left(z\right)=10^{-8}\right\}.
  Since the Lévy measure decays at least exponentially as ‖z‖→∞\left\|z\right\|\rightarrow\infty,
  we ensure that ℓ​(z)<10−8\ell\left(z\right)<10^{-8} for all z∈ℝ2z\in\mathbb{R}^{2}
  such that ‖z‖∞>zmax𝐈𝐈𝐈\left\|z\right\|\_{\infty}>z\_{\max}^{\mathbf{III}}.
* ∙\bullet

  xint=52​Kx\_{\rm int}=\frac{5}{2}K. The non-smoothness set of ϕ\phi
  is contained in the portion of RxR\_{x} where the grid 𝐱\mathbf{x} is uniform.
* ∙\bullet

  xmaxx\_{\rm max} was heuristically chosen as 57​K57K
  for VG0, 5​K5K for VG1, 6​K6K for NIG0, and 7​K7K
  for NIG1.
* ∙\bullet

  cc is chosen such that F=max⁡(65%,xintxmax)F=\max\left(65\%,\frac{x\_{\rm int}}{x\_{\rm max}}\right).
  In this way, approximately at least 65% of the spatial grid points in each given direction are in the interval [0,xint]\left[0,x\_{\rm int}\right].
* ∙\bullet

  Ny−=ceil​[−1hz​ln⁡(x1)]+Ny∗N\_{y}^{-}=\text{ceil}\left[-\frac{1}{h\_{z}}\ln\left(x\_{1}\right)\right]+N\_{y}^{\*}
  and Ny+=ceil​[1hz​ln⁡(xmax)]+Ny∗N\_{y}^{+}=\text{ceil}\left[\frac{1}{h\_{z}}\ln\left(x\_{\rm max}\right)\right]+N\_{y}^{\*}
  for some given Ny∗∈ℕ0N\_{y}^{\*}\in\mathbb{N}\_{0}. This choice minimises the need for extrapolation in
  ([3.17](https://arxiv.org/html/2511.02700v1#S3.E17 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"))
  as it is necessary to extrapolate just to the grid points xm1​m2x\_{m\_{1}m\_{2}} with either m1=0m\_{1}=0 or m2=0m\_{2}=0.
  This is done in a linear fashion.
  In ([3.16](https://arxiv.org/html/2511.02700v1#S3.E16 "In 3.2.2 Summation term ‣ 3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")), we set v​(x,t)=0v\left(x,t\right)=0 whenever x∉Rxx\notin R\_{x}.
* ∙\bullet

  Ny∗N\_{y}^{\*} is taken as the minimal n∈ℕ0n\in\mathbb{N}\_{0} such that
  the maximal prime factor of ♯​in=Ny−+Ny++2​Nz\sharp\textrm{in}=N\_{y}^{-}+N\_{y}^{+}+2N\_{z} is at most 7. This is beneficial for the efficiency of the FFT.
* ∙\bullet

  The tolerances used for the fixed-point iteration and BiCGSTAB are
  set to 10−710^{-7} and 10−1410^{-14}, respectively.
* ∙\bullet

  Interpolation is performed by cubic Lagrange polynomials.

Figure [3](https://arxiv.org/html/2511.02700v1#S4.F3 "Figure 3 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")

Figure 3: European put-on-the-average option
price and the Greeks Delta and Gamma for the parameter set NIG0

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

displays the graphs of the option price function and its Greeks Delta and Gamma for the parameter set NIG0
from Table [1](https://arxiv.org/html/2511.02700v1#S4.T1 "Table 1 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models"), where we have taken Nx=400N\_{x}=400. The Greeks have been approximated (at negligible computational cost) by applying the second-order central finite difference schemes described in Section [3.2](https://arxiv.org/html/2511.02700v1#S3.SS2 "3.2 Spatial discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").
Table [3](https://arxiv.org/html/2511.02700v1#S4.T3 "Table 3 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")

Table 3: Numerical option prices for points xx near (K,K)\left(K,K\right)

| (x(1),x(2))\left(x^{\left(1\right)},x^{\left(2\right)}\right) | VG0 | VG1 | NIG0 | NIG1 |
| --- | --- | --- | --- | --- |
| (90,90)\left(90,90\right) | 12.6534 | 10.1080 | 11.4067 | 11.5830 |
| (90,100)\left(90,100\right) | 10.6121 | 5.8462 | 7.8724 | 8.1529 |
| (90,110)\left(90,110\right) | 9.0136 | 3.0178 | 5.1023 | 5.4657 |
| (100,90)\left(100,90\right) | 10.4061 | 5.7637 | 7.8897 | 8.0910 |
| (100,100)\left(100,100\right) | 8.8015 | 2.9037 | 5.1186 | 5.3953 |
| (100,110)\left(100,110\right) | 7.5309 | 1.3893 | 3.1156 | 3.4311 |
| (110,90)\left(110,90\right) | 8.6181 | 2.8070 | 5.1393 | 5.3381 |
| (110,100)\left(110,100\right) | 7.3464 | 1.3062 | 3.1326 | 3.3735 |
| (110,110)\left(110,110\right) | 6.3290 | 0.6014 | 1.7937 | 2.0397 |

provides the numerical option prices for various points xx around (K,K)\left(K,K\right) and all four parameter sets from Table [1](https://arxiv.org/html/2511.02700v1#S4.T1 "Table 1 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").

We next investigate the convergence behaviour of the numerical scheme.
Let 𝐱N\mathbf{x}\_{N} denote the set of spatial grid points if Nx=NN\_{x}=N. For x∈Rxx\in R\_{x}, let u~​(x;N)\tilde{u}(x;N) denote the approximation of the exact solution value u​(x,T)u(x,T) obtained by the numerical scheme if Nx=NN\_{x}=N. More precisely, the vector VNtV^{N\_{t}} generated by ([3.27](https://arxiv.org/html/2511.02700v1#S3.E27 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")), ([3.28](https://arxiv.org/html/2511.02700v1#S3.E28 "In 3.3 Temporal discretization: the semi-Lagrangian 𝜃-method ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")) yields the approximation on the spatial grid 𝐱N\mathbf{x}\_{N} and cubic interpolation is employed whenever x∉𝐱Nx\notin\mathbf{x}\_{N}.
We consider u~​(x;N)\tilde{u}(x;N) with N=400N=400 as the reference solution and study for 50≤N≤20050\leq N\leq 200 the total error defined by

|  |  |  |
| --- | --- | --- |
|  | E​(N)=max⁡{|u~​(x;N)−u~​(x;400)|:x∈𝐱N​ and ​x∈[0,3​K]×[0,3​K]}.E\left(N\right)=\max\left\{|\tilde{u}(x;N)-\tilde{u}(x;400)|:x\in\mathbf{x}\_{N}\textrm{\penalty 10000\ and\penalty 10000\ }x\in\left[0,3K\right]\times\left[0,3K\right]\right\}. |  |

Figure [4](https://arxiv.org/html/2511.02700v1#S4.F4 "Figure 4 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")

Figure 4: Total error in [0,3​K]×[0,3​K]\left[0,3K\right]\times\left[0,3K\right]

![Refer to caption](x8.png)

displays the total errors for all four parameter sets from Table [1](https://arxiv.org/html/2511.02700v1#S4.T1 "Table 1 ‣ 4 Numerical experiments ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models").
The quantity pp in the legend denotes the numerical order of convergence, which is computed by linear regression.
Clearly, the favourable result is found that the numerical scheme achieves second-order convergence for each set of parameters.

## 5 Conclusions

In this paper, we have developed an effective numerical method for the valuation of European options under two-asset exponential Lévy models with particular attention to the infinite-activity case.
Our method is based upon the ideas in Wang et al. ([2007](https://arxiv.org/html/2511.02700v1#bib.bib24)) for the one-asset case.
A key part of our method is the tailored discretization of the non-local integral term, designed to handle singular measures under mild assumptions. The discretized integral term can subsequently be efficiently evaluated by FFT.
For the discretization in time, the semi-Lagrangian Crank–Nicolson method is employed with a fixed-point iteration on the integral part.
Numerical experiments for put-on-the-average options under Normal Tempered Stable processes indicate that our method achieves favourable second-order convergence whenever the exponential Lévy model has finite-variation.

A main topic for future research will be extending the proposed methodology to the valuation of American-style two-asset options under exponential Lévy models with infinite-activity, where the combination of the early-exercise feature and the non-local integral term poses additional challenges.

## 6 Acknowledgements

The authors acknowledge the support of the Research Foundation - Flanders
(FWO) under grant G0B5623N and the FWO Scientific Research Network
ModSimFIE (FWO WOG W001021N). The third author also acknowledges the financial support of the Research Foundation - Flanders (FWO) through FWO SAB K803124.

## Appendix A dd-dimensional Normal Tempered Stable process

The term dd-dimensional Normal Tempered Stable process refers to a
dd-dimensional pure-jump compensated Lévy process LL with Lévy
measure generated by subordinating a dd-dimensional Brownian motion
BB with a tempered stable subordinator GG, i.e., a pure-jump process
with almost surely non-decreasing trajectories. Such a process is defined
by the following equation

|  |  |  |
| --- | --- | --- |
|  | L​(t)=B​(G​(t))−𝔼​[B​(G​(t))]with ​L​(0)=0.L\left(t\right)=B\left(G\left(t\right)\right)-\mathbb{E}\left[B\left(G\left(t\right)\right)\right]\qquad\text{with }L\left(0\right)=0. |  |

In our context, we will use this process to define the jump component
of the logarithmic return in asset prices, i.e. we choose

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ∗2z​Π~​(d​t,d​z)=d​L​(t).\int\_{\mathbb{R}\_{\*}^{2}}z\tilde{\Pi}\left(dt,dz\right)=dL\left(t\right). |  |

### A.1 Tempered Stable subordinator

A tempered stable subordinator is a non-compensated 1-sided tempered
stable process GG, which is characterized by the parameters δ,λ>0\delta,\lambda>0 and α∈[0,1)\alpha\in\left[0,1\right). For more details see Küchler & Tappe ([2013](https://arxiv.org/html/2511.02700v1#bib.bib14)). Table [4](https://arxiv.org/html/2511.02700v1#A1.T4 "Table 4 ‣ A.1 Tempered Stable subordinator ‣ Appendix A 𝑑-dimensional Normal Tempered Stable process ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")

Table 4: Main quantities of the Tempered Stable subordinator

| Quantity | Formula |
| --- | --- |
| Lévy measure | ℓG​(x)=𝕀x>0​δ​e−λ​x​x−1−α\ell\_{G}\left(x\right)=\mathbb{I}\_{x>0}\delta e^{-\lambda x}x^{-1-\alpha} |
| Characteristic exponent | ψG​(x)={−δ​ln⁡(1−i​x​λ−1)if ​α=0δ​Γ​(−α)​((λ−i​x)α−λα)if ​α∈(0,1)\psi\_{G}\left(x\right)=\begin{cases}-\delta\ln\left(1-ix\lambda^{-1}\right)&\text{if }\alpha=0\\ \delta\Gamma\left(-\alpha\right)\left(\left(\lambda-ix\right)^{\alpha}-\lambda^{\alpha}\right)&\text{if }\alpha\in\left(0,1\right)\end{cases} |
| Expected value | 𝔼​[G​(1)]=δ​Γ​(1−α)λ1−α\mathbb{E}\left[G\left(1\right)\right]=\delta\frac{\Gamma\left(1-\alpha\right)}{\lambda^{1-\alpha}} |
| Variance | 𝕍​[G​(1)]=δ​Γ​(2−α)λ2−α\mathbb{V}\left[G\left(1\right)\right]=\delta\frac{\Gamma\left(2-\alpha\right)}{\lambda^{2-\alpha}} |
| Density function | fG​(x)={𝕀x>0​λδΓ​(δ)​xδ−1​e−λ​xif ​α=0𝕀x>0​δ​x−32​e−(λ​x−δ​π)2​x−1if ​α=12not known analyticallyelsef\_{G}\left(x\right)=\begin{cases}\mathbb{I}\_{x>0}\frac{\lambda^{\delta}}{\Gamma\left(\delta\right)}x^{\delta-1}e^{-\lambda x}&\text{if }\alpha=0\\ \mathbb{I}\_{x>0}\delta x^{-\frac{3}{2}}e^{-\left(\sqrt{\lambda}x-\delta\sqrt{\pi}\right)^{2}x^{-1}}&\text{if }\alpha=\frac{1}{2}\\ \text{not known analytically}&\text{else}\end{cases} |

shows the main quantities for such a process. Note that GG corresponds to the Gamma process for α=0\alpha=0 and to the Inverse Gaussian process for α=12\alpha=\frac{1}{2}.

### A.2 Normal Tempered Stable process

Consider B​(t)=η​t+ρ​W​(t)B\left(t\right)=\eta t+\sqrt{\rho}\,W\left(t\right), where WW is a standard dd-dimensional Wiener process, η∈ℝd\eta\in\mathbb{R}^{d} and ρ\sqrt{\rho} is the Cholesky decomposition of a given positive semi-definite symmetric matrix ρ\rho, i.e., ρ=ρ⋅ρ⊤\rho=\sqrt{\rho}\cdot\sqrt{\rho}^{\top}. Adapting the results presented in Barndorff-Nielsen
et al. ([2001](https://arxiv.org/html/2511.02700v1#bib.bib3)) and Rocha-Arteaga & Sato ([2019](https://arxiv.org/html/2511.02700v1#bib.bib18), Chapter 4)888The authors consider the more general case where the characteristic
exponent of LL is defined as ψL​(τ)=∫ℝd(ei​τ⊤​z−1−i​τ⊤​z​𝕀‖z‖<1)​ℓL​(d​z)\psi\_{L}\left(\tau\right)=\int\_{\mathbb{R}^{d}}\left(e^{i\tau^{\top}z}-1-i\tau^{\top}z\mathbb{I}\_{\left\|z\right\|<1}\right)\ell\_{L}\left(dz\right),
while we consider the case where ψL​(τ)=∫ℝd(ei​τ⊤​z−1−i​τ⊤​z)​ℓL​(d​z)\psi\_{L}\left(\tau\right)=\int\_{\mathbb{R}^{d}}\left(e^{i\tau^{\top}z}-1-i\tau^{\top}z\right)\ell\_{L}\left(dz\right)., we define a dd-dimensional Normal Tempered Stable process as

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(t)=B​(G​(t))−c​t,L\left(t\right)=B\left(G\left(t\right)\right)-ct, |  | (A.1) |

where GG is a Tempered Stable subordinator and c=𝔼​[B​(G​(t))]=δ​Γ​(1−α)λ1−α​ηc=\mathbb{E}\left[B\left(G\left(t\right)\right)\right]=\delta\frac{\Gamma\left(1-\alpha\right)}{\lambda^{1-\alpha}}\eta.

Table [5](https://arxiv.org/html/2511.02700v1#A1.T5 "Table 5 ‣ A.2 Normal Tempered Stable process ‣ Appendix A 𝑑-dimensional Normal Tempered Stable process ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")

Table 5: Main quantities of the Normal Tempered Stable process

| Quantity | Formula |
| --- | --- |
| Lévy measure | ℓL​(x)=δ​Φ​(x∣α,0)\ell\_{L}\left(x\right)=\delta\Phi\left(x\mid\alpha,0\right) |
| Characteristic exponent | ψL​(x)={−δ​ln⁡(λ−i​x⊤​η+12​x⊤​ρ​xλ)−i​x⊤​cif ​α=0δ​Γ​(−α)​((λ−i​x⊤​η+12​x⊤​ρ​x)α−λα)−i​x⊤​cif ​α∈(0,1)\psi\_{L}\left(x\right)=\begin{cases}-\delta\ln\left(\frac{\lambda-ix^{\top}\eta+\frac{1}{2}x^{\top}\rho x}{\lambda}\right)-ix^{\top}c&\text{if }\alpha=0\\ \delta\Gamma\left(-\alpha\right)\left(\left(\lambda-ix^{\top}\eta+\frac{1}{2}x^{\top}\rho x\right)^{\alpha}-\lambda^{\alpha}\right)-ix^{\top}c&\text{if }\alpha\in\left(0,1\right)\end{cases} |
| Expected value | 𝔼​[L​(1)]=0\mathbb{E}\left[L\left(1\right)\right]=0 |
| Variance | 𝕍​[L​(1)]=δ​Γ​(2−α)λ2−α​(ρ​λ1−α+η​η⊤)\mathbb{V}\left[L\left(1\right)\right]=\delta\frac{\Gamma\left(2-\alpha\right)}{\lambda^{2-\alpha}}\left(\rho\frac{\lambda}{1-\alpha}+\eta\eta^{\top}\right) |
| Density function | fL​(x)={λδΓ​(δ)​Φ​(x+c∣−δ,0)if ​α=0δ​e2​δ​λ​π​Φ​(x+c∣12,δ2​π)if ​α=12not known analyticallyelsef\_{L}\left(x\right)=\begin{cases}\frac{\lambda^{\delta}}{\Gamma\left(\delta\right)}\Phi\left(x+c\mid-\delta,0\right)&\text{if }\alpha=0\\ \delta e^{2\delta\sqrt{\lambda\pi}}\Phi\left(x+c\mid\frac{1}{2},\delta^{2}\pi\right)&\text{if }\alpha=\frac{1}{2}\\ \text{not known analytically}&\text{else}\end{cases} |

shows the main quantities for such a process. Most of the formulae
are expressed in terms of the function Φ\Phi which is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(x∣a,b)=2​(‖η‖ρ2+2​λ)a+d2(2​π)d​det[ρ]​Ka+d2​((‖η‖ρ2+2​λ)​(‖x‖ρ2+2​b))(‖x‖ρ2+2​b)a+d2​e⟨η,x⟩ρ\Phi\left(x\mid a,b\right)=2\sqrt{\frac{\left(\left\|\eta\right\|\_{\rho}^{2}+2\lambda\right)^{a+\frac{d}{2}}}{\left(2\pi\right)^{d}\det\left[\rho\right]}}\frac{K\_{a+\frac{d}{2}}\left(\sqrt{\left(\left\|\eta\right\|\_{\rho}^{2}+2\lambda\right)\left(\left\|x\right\|\_{\rho}^{2}+2b\right)}\right)}{\left(\sqrt{\left\|x\right\|\_{\rho}^{2}+2b}\right)^{a+\frac{d}{2}}}e^{\left\langle\eta,x\right\rangle\_{\rho}} |  | (A.2) |

where Kν​(τ)=12​∫0∞yν−1​e−12​τ​(y+y−1)​𝑑yK\_{\nu}\left(\tau\right)=\frac{1}{2}\int\_{0}^{\infty}y^{\nu-1}e^{-\frac{1}{2}\tau\left(y+y^{-1}\right)}dy, for τ>0\tau>0,
denotes the modified Bessel function of the second kind (see Schoutens ([2003](https://arxiv.org/html/2511.02700v1#bib.bib22), Appendix A)),
⟨x,y⟩ρ=x⊤​ρ−1​y\left\langle x,y\right\rangle\_{\rho}=x^{\top}\rho^{-1}y and ‖x‖ρ=⟨x,x⟩\left\|x\right\|\_{\rho}=\sqrt{\left\langle x,x\right\rangle} is its induced norm. We conclude this appendix with the following proposition.

###### Proposition A.1.

Consider a Lévy measure ℓ\ell over ℝ∗d=ℝd∖{0}\mathbb{R}^{d}\_{\*}=\mathbb{R}^{d}\setminus\{0\}. Assume that there exist constants
AℓA\_{\ell} and BℓB\_{\ell}, and for any given h>0h>0 a constant Cℓ​(h)C\_{\ell}(h) such that

|  |  |  |
| --- | --- | --- |
|  | {ℓ​(z)≤Cℓ​(h)​‖z‖ρ−Aℓ−dfor any ​z∈ℝ∗d​ such that ​‖z‖ρ∈(0,h]ℓ​(z)=O​(e−Bℓ​‖z‖ρ)as ​‖z‖ρ→∞.\begin{cases}\ell\left(z\right)\leq C\_{\ell}\left(h\right)\left\|z\right\|\_{\rho}^{-A\_{\ell}-d}&\text{for any }z\in\mathbb{R}^{d}\_{\*}\text{ such that }\left\|z\right\|\_{\rho}\in\left(0,h\right]\\ \ell\left(z\right)=O\left(e^{-B\_{\ell}\left\|z\right\|\_{\rho}}\right)&\text{as }\left\|z\right\|\_{\rho}\rightarrow\infty.\end{cases} |  |

Then, for a Normal Tempered Stable process these constants are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aℓ\displaystyle A\_{\ell} | =2​α\displaystyle=2\alpha |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Bℓ\displaystyle B\_{\ell} | =‖η‖ρ2+2​λ−‖η‖ρ\displaystyle=\sqrt{\left\|\eta\right\|\_{\rho}^{2}+2\lambda}-\left\|\eta\right\|\_{\rho} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Cℓ​(h)\displaystyle C\_{\ell}\left(h\right) | =2α​δ​Γ​(α+d2)πd​det[ρ]​eh​‖η‖ρ.\displaystyle=\frac{2^{\alpha}\delta\Gamma\left(\alpha+\frac{d}{2}\right)}{\sqrt{\pi^{d}\det\left[\rho\right]}}e^{h\left\|\eta\right\|\_{\rho}}. |  |

###### Proof.

Denote c1=‖η‖ρ2+2​λc\_{1}=\sqrt{\left\|\eta\right\|\_{\rho}^{2}+2\lambda} and c2=2​δ​c1α+d2​(2​π)−d2​det[ρ]−12c\_{2}=2\delta c\_{1}^{\alpha+\frac{d}{2}}\left(2\pi\right)^{-\frac{d}{2}}\det\left[\rho\right]^{-\frac{1}{2}}. The function ℓ¯:ℝ>0→ℝ\overline{\ell}:\mathbb{R}\_{>0}\rightarrow\mathbb{R},
defined by

|  |  |  |
| --- | --- | --- |
|  | ℓ¯​(τ)=c2​τ−α−d2​Kα+d2​(c1​τ)​eτ​‖η‖ρ,\overline{\ell}\left(\tau\right)=c\_{2}\tau^{-\alpha-\frac{d}{2}}K\_{\alpha+\frac{d}{2}}\left(c\_{1}\tau\right)e^{\tau\left\|\eta\right\|\_{\rho}}, |  |

represents a radial upper bound for ℓ\ell, since by the Cauchy-Schwarz inequality ℓ​(z)≤ℓ¯​(‖z‖ρ)\ell\left(z\right)\leq\overline{\ell}\left(\left\|z\right\|\_{\rho}\right) for any z∈ℝ∗dz\in\mathbb{R}^{d}\_{\*}.
Applying the following well known inequality for the modified Bessel function of the second kind

|  |  |  |
| --- | --- | --- |
|  | τν​Kν​(τ)≤Γ​(ν)​2ν−1for any ​τ,ν>0,\tau^{\nu}K\_{\nu}\left(\tau\right)\leq\Gamma\left(\nu\right)2^{\nu-1}\qquad\text{for any }\tau,\nu>0, |  |

we readily get

|  |  |  |
| --- | --- | --- |
|  | ℓ¯​(τ)≤c2​c1−α−d2​2α+d2−1​eτ​‖η‖ρ​Γ​(α+d2)​τ−2​α−d.\overline{\ell}\left(\tau\right)\leq c\_{2}c\_{1}^{-\alpha-\frac{d}{2}}2^{\alpha+\frac{d}{2}-1}e^{\tau\left\|\eta\right\|\_{\rho}}\Gamma\left(\alpha+\frac{d}{2}\right)\tau^{-2\alpha-d}. |  |

For τ=‖z‖ρ\tau=\left\|z\right\|\_{\rho} with ‖z‖ρ∈(0,h]\left\|z\right\|\_{\rho}\in\left(0,h\right] we easily deduce the stated expressions for AℓA\_{\ell} and Cℓ​(h)C\_{\ell}(h).
Invoking the following asymptotic behaviour of the modified Bessel function of the second kind

|  |  |  |
| --- | --- | --- |
|  | Kν​(τ)=O​(τ−12​e−τ)as ​τ→∞,K\_{\nu}\left(\tau\right)=O\left(\tau^{-\frac{1}{2}}e^{-\tau}\right)\qquad\text{as }\tau\rightarrow\infty, |  |

it follows that

|  |  |  |
| --- | --- | --- |
|  | ℓ¯​(τ)=O​(τ−α−d2−12​e−τ​(c1−‖η‖ρ)).\overline{\ell}\left(\tau\right)=O\left(\tau^{-\alpha-\frac{d}{2}-\frac{1}{2}}e^{-\tau\left(c\_{1}-\left\|\eta\right\|\_{\rho}\right)}\right). |  |

Since τ−α−d2−12=O​(1)\tau^{-\alpha-\frac{d}{2}-\frac{1}{2}}=O\left(1\right) as τ→∞\tau\rightarrow\infty, we obtain the expression for BℓB\_{\ell}.
∎

## Appendix B Summation operator as a circulant matrix-vector multiplication

Let Nz=1N\_{z}=1, Ny−=0N\_{y}^{-}=0 and Ny+=1N\_{y}^{+}=1. Then ♯​out=Ny++Ny−+1=2\sharp\text{out}=N\_{y}^{+}+N\_{y}^{-}+1=2 and ♯​in=2​Nz+Ny++Ny−=3\sharp\text{in}=2N\_{z}+N\_{y}^{+}+N\_{y}^{-}=3. The quadrature matrix Ω\Omega, whose entries are the coefficients ω\omega defined in ([3.5](https://arxiv.org/html/2511.02700v1#S3.E5 "In 3.1 Integral discretization ‣ 3 Numerical scheme ‣ Numerical valuation of European options under two-asset infinite-activity exponential Lévy models")), is given by

|  |  |  |
| --- | --- | --- |
|  | Ω=[ω−1,−1ω−1,0ω0,−1ω0,0]∈ℝ2​Nz×2​Nz.\Omega=\left[\begin{array}[]{cc}\omega\_{-1,-1}&\omega\_{-1,0}\\ \omega\_{0,-1}&\omega\_{0,0}\end{array}\right]\in\mathbb{R}^{2N\_{z}\times 2N\_{z}}. |  |

The first row of the circulant matrix CC is defined according to

|  |  |  |
| --- | --- | --- |
|  | C1,⋅=vec​([ω−1,−1ω−1,00ω0,−1ω0,00000])∈ℝ(♯​in)2×1,C\_{1,\cdot}=\text{vec}\left(\left[\begin{array}[]{ccc}\omega\_{-1,-1}&\omega\_{-1,0}&0\\ \omega\_{0,-1}&\omega\_{0,0}&0\\ 0&0&0\end{array}\right]\right)\in\mathbb{R}^{\left(\sharp\text{in}\right)^{2}\times 1}, |  |

while the entire matrix is

|  |  |  |
| --- | --- | --- |
|  | C=[ω−1,−1ω0,−10ω−1,0ω0,000000ω−1,−1ω0,−10ω−1,0ω0,000000ω−1,−1ω0,−10ω−1,0ω0,000000ω−1,−1ω0,−10ω−1,0ω0,000000ω−1,−1ω0,−10ω−1,0ω0,0ω0,00000ω−1,−1ω0,−10ω−1,0ω−1,0ω0,00000ω−1,−1ω0,−100ω−1,0ω0,00000ω−1,−1ω0,−1ω0,−10ω−1,0ω0,00000ω−1,−1]∈ℝ(♯​in)2×(♯​in)2.C=\left[\begin{array}[]{ccccccccc}{\color[rgb]{1,0,0}\omega\_{-1,-1}}&{\color[rgb]{1,0,0}\omega\_{0,-1}}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}\omega\_{-1,0}}&{\color[rgb]{1,0,0}\omega\_{0,0}}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}\\ {\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}\omega\_{-1,-1}}&{\color[rgb]{1,0,0}\omega\_{0,-1}}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}\omega\_{-1,0}}&{\color[rgb]{1,0,0}\omega\_{0,0}}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}\\ 0&0&\omega\_{-1,-1}&\omega\_{0,-1}&0&\omega\_{-1,0}&\omega\_{0,0}&0&0\\ {\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}\omega\_{-1,-1}}&{\color[rgb]{1,0,0}\omega\_{0,-1}}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}\omega\_{-1,0}}&{\color[rgb]{1,0,0}\omega\_{0,0}}&{\color[rgb]{1,0,0}0}\\ {\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}\omega\_{-1,-1}}&{\color[rgb]{1,0,0}\omega\_{0,-1}}&{\color[rgb]{1,0,0}0}&{\color[rgb]{1,0,0}\omega\_{-1,0}}&{\color[rgb]{1,0,0}\omega\_{0,0}}\\ \omega\_{0,0}&0&0&0&0&\omega\_{-1,-1}&\omega\_{0,-1}&0&\omega\_{-1,0}\\ \omega\_{-1,0}&\omega\_{0,0}&0&0&0&0&\omega\_{-1,-1}&\omega\_{0,-1}&0\\ 0&\omega\_{-1,0}&\omega\_{0,0}&0&0&0&0&\omega\_{-1,-1}&\omega\_{0,-1}\\ \omega\_{0,-1}&0&\omega\_{-1,0}&\omega\_{0,0}&0&0&0&0&\omega\_{-1,-1}\end{array}\right]\in\mathbb{R}^{\left(\sharp\text{in}\right)^{2}\times\left(\sharp\text{in}\right)^{2}}. |  |

The entries in the first, second, fourth, and fifth rows (highlighted in red) correspond to the matrix I~​C∈ℝ(♯​out)2×(♯​in)2\tilde{I}C\in\mathbb{R}^{\left(\sharp\text{out}\right)^{2}\times\left(\sharp\text{in}\right)^{2}}.

## References

* Applebaum (2004)

  Applebaum, D. (2004) Lévy Processes and Stochastic Calculus.
  Cambridge University Press, Cambridge, UK.
* Asmussen & Rosiński (2001)

  Asmussen, S. & Rosiński, J. (2001) Approximations of small jumps of
  Lévy processes with a view towards simulation.
  Journal of Applied Probability, 38(02), 482–493.
* Barndorff-Nielsen
  et al. (2001)

  Barndorff-Nielsen, O.E., Pedersen, J., & Sato, K.I. (2001) Multivariate
  subordination, self-decomposability and stability.
  Advances in Applied Probability, 33(1), 160–187.
* Boen & in ’t Hout (2021)

  Boen, L. & in ’t Hout, K.J. (2021) Operator splitting schemes for the
  two-asset Merton jump-diffusion model.
  Journal of Computational and Applied Mathematics, 387, 112309.
* Clift & Forsyth (2008)

  Clift, S.S. & Forsyth, P.A. (2008) Numerical solution of two asset jump
  diffusion models for option valuation.
  Applied Numerical Mathematics, 58, 743–782.
* Cont & Voltchkova (2005)

  Cont, R. & Voltchkova, E. (2005) A finite difference scheme for option pricing
  in jump diffusion and exponential Lévy models.
  SIAM Journal on Numerical Analysis, 43(4), 1596–1626.
* d’Halluin et al. (2005)

  d’Halluin, Y., Forsyth, P.A., & Vetzal, K.R. (2005) Robust numerical methods
  for contingent claims under jump diffusion processes.
  IMA Journal of Numerical Analysis, 25(1), 87–112.
* Garroni & Menaldi (1992)

  Garroni, M.G. & Menaldi, J.L. (1992) Green Functions for Second Order
  Parabolic Integro-Differential Problems.
  Longman, Harlow, UK.
* Hainaut & Le Courtois (2014)

  Hainaut, D. & Le Courtois, O. (2014) An intensity model for credit risk with
  switching Lévy processes.
  Quantitative Finance, 14(8), 1453–1465.
* Hilber et al. (2013)

  Hilber, N., Reichmann, O., Schwab, C., & Winter, C. (2013) Computational
  Methods for Quantitative Finance: Finite Element Methods for
  Derivative Pricing.
  Springer, Heidelberg.
* in ’t Hout & Lamotte (2023)

  in ’t Hout, K.J. & Lamotte, P. (2023) Efficient numerical valuation of
  European options under the two-asset Kou jump-diffusion model.
  Journal of Computational Finance, 26(4), 101–137.
* Jackson et al. (2008)

  Jackson, K.R., Jaimungal, S., & Surkov, V. (2008) Fourier space time-stepping
  for option pricing with Lévy models.
  Journal of Computational Finance, 12(2), 1–29.
* Kaushansky et al. (2018)

  Kaushansky, V., Lipton, A., & Reisinger, C. (2018) Numerical analysis of an
  extended structural default model with mutual liabilities and jump risk.
  Journal of Computational Science, 24, 218–231.
* Küchler & Tappe (2013)

  Küchler, U. & Tappe, S. (2013) Tempered stable distributions and
  processes.
  Stochastic Processes and their Applications, 123(12),
  4256–4293.
* Øksendal & Sulem (2019)

  Øksendal, B. & Sulem, A. (2019) Applied Stochastic Control of
  Jump Diffusions.
  Springer, Cham, Switzerland.
* Plonka et al. (2018)

  Plonka, G., Potts, D., Steidl, G., & Tasche, M. (2018) Numerical
  Fourier Analysis.
  Springer, Cham, Switzerland.
* Quarteroni et al. (2007)

  Quarteroni, A., Sacco, R., & Saleri, F. (2007) Numerical Mathematics.
  Springer, Berlin.
* Rocha-Arteaga & Sato (2019)

  Rocha-Arteaga, A. & Sato, K.I. (2019) Topics in Infinitely Divisible
  Distributions and Lévy Processes, Revised Edition.
  Springer, Cham, Switzerland.
* Ruijter & Oosterlee (2012)

  Ruijter, M.J. & Oosterlee, C.W. (2012) Two-dimensional Fourier cosine
  series expansion method for pricing financial options.
  SIAM Journal on Scientific Computing, 34(5), B642–B671.
* Rydberg (1997)

  Rydberg, T.H. (1997) The normal inverse Gaussian Lévy process:
  simulation and approximation.
  Communications in Statistics. Stochastic Models, 13(4),
  887–910.
* Salmi et al. (2014)

  Salmi, S., Toivanen, J., & von Sydow, L. (2014) An IMEX-scheme for pricing
  options under stochastic volatility models with jumps.
  SIAM Journal on Scientific Computing, 36, B817–B834.
* Schoutens (2003)

  Schoutens, W. (2003) Lévy Processes in Finance: Pricing
  Financial Derivatives.
  Wiley, Chichester, UK.
* Spiegelman & Katz (2006)

  Spiegelman, M. & Katz, R.F. (2006) A semi-Lagrangian Crank-Nicolson
  algorithm for the numerical solution of advection-diffusion problems.
  Geochemistry, Geophysics, Geosystems, 7(4).
* Wang et al. (2007)

  Wang, I.R., Wan, J.W.L., & Forsyth, P.A. (2007) Robust numerical valuation of
  European and American options under the CGMY process.
  Journal of Computational Finance, 10(4), 31–69.