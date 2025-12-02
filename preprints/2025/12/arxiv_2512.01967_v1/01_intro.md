---
authors:
- Robert Jenkinson Alvarez
doc_id: arxiv:2512.01967v1
family_id: arxiv:2512.01967
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian
  Fog Post-Fit
url_abs: http://arxiv.org/abs/2512.01967v1
url_html: https://arxiv.org/html/2512.01967v1
venue: arXiv q-fin
version: 1
year: 2025
---

Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit
  
Robert Jenkinson Álvarez
  
December 1, 2025

###### Abstract

We study the construction of arbitrage-free option price surfaces from noisy bid-ask quotes across strike and maturity. Our starting point is a Chebyshev representation of the call price surface on a warped log-moneyness/maturity rectangle, together with linear sampling and no-arbitrage operators acting on a collocation grid. Static no-arbitrage requirements are enforced as linear inequalities, while the surface is fitted directly to prices via a coverage-seeking quadratic objective that trades off squared band misfit against spectral and transport-inspired regularisation of the Chebyshev coefficients. This yields a strictly convex quadratic program in the modal coefficients, solvable at practical scales with off-the-shelf solvers (OSQP).

On top of the global backbone, we introduce a local post-fit layer based on a discrete fog of risk-neutral densities on a three-dimensional lattice (m,τ,u)(m,\tau,u) and an associated Hamiltonian-type energy. On each patch of the (m,τ)(m,\tau) plane, the fog variables are coupled to a nodal price field obtained from the baseline surface, yielding a joint convex optimisation problem that reweights noisy quotes and applies noise-aware local corrections while preserving global static no-arbitrage and locality.

The method is designed such that for equity options panels, the combined procedure achieves high inside–spread coverage in stable regimes (in calm years, 98−99%98-99\% of quotes are priced inside the bid–ask intervals) and low rates of static no–arbitrage violations (below 1%1\%). In stressed periods, the fog layer provides a mechanism for controlled leakage outside the band: when local quotes are mutually inconsistent or unusually noisy, the optimiser allocates fog mass outside the bid–ask tube and justifies small out–of–band deviations of the post–fit surface, while preserving a globally arbitrage–free and well–regularised description of the option surface.

## 1.  Introduction

Liquid option markets require a smooth, stable and *arbitrage-free*
surface of prices or implied volatilities over strike and maturity.
Such a surface underpins marking, risk management and model calibration, and
feeds directly into trading and hedging decisions.
In practice, the raw quote grid is sparse, noisy and often inconsistent with
the static no-arbitrage conditions implied by absence of butterfly and
calendar spreads.
Production systems therefore interpolate and regularise the observed quotes
into a dense surface subject to no-arbitrage constraints.

There is substantial literature on arbitrage-free surface
construction.
Parametric approaches such as SVI and its extensions impose functional forms
on implied volatility and derive analytical sufficient conditions for absence
of static arbitrage.
Alternatively, nonparametric smoothing methods reconstruct prices or
volatilities on a grid while enforcing no-arbitrage inequalities either as
hard constraints or via penalisation.
These methods have been successfully deployed in practice, but there remains
a trade-off between fidelity to the bid-ask quotes, strict enforcement of
no-arbitrage on a dense grid, and computational cost on large universes of
names and dates.

This paper contributes a practical convex-programming formulation for option price
surfaces that aims to balance these considerations, together with a local geometric
post-fit layer that explicitly models quote noise on difficult regions of the surface.
The key ingredients are:

* •

  a global Chebyshev representation of the price surface on a warped
  log-moneyness / maturity rectangle, which provides high approximation power;
* •

  linear operators that encode static no-arbitrage constraints on a dense
  collocation grid (monotonicity in strike, convexity in strike, calendar
  monotonicity and simple bounds), so that absence of butterfly and calendar
  arbitrage is enforced directly in price space;
* •

  a coverage-seeking quadratic objective aligned to the bid–ask geometry,
  augmented by spectral and transport-inspired regularisers (ridge in the
  Chebyshev coefficients, discrete H−1H^{-1} smoothing of the density, short-end
  anchoring and frequency tapering) that stabilise the fit while preserving
  convexity;
* •

  a patch-wise post-fit in price space, built on a discrete “fog” of
  risk-neutral densities on a three-dimensional lattice (m,τ,u)(m,\tau,u) and a
  Hamiltonian-type energy on that fog, which yields a convex, noise-aware local
  correction of the baseline surface on problematic regions while preserving
  global static no-arbitrage.

The resulting baseline surface is obtained as the solution of a single medium-scale
QP with sparse structure, solvable reliably with off-the-shelf solvers, and tuned to
reach high within-band coverage and low static no-arbitrage violation rates on a
dense grid. The discrete Hamiltonian fog layer appears as a second, fully convex
post-fit stage defined on local patches in (m,τ)(m,\tau); it is implemented in this
paper in a finite-dimensional setting (Chapter [12](https://arxiv.org/html/2512.01967v1#Ch12 "12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) and used to refine the baseline surface in stressed regimes.

The rest of the paper is organised as follows. Chapter [2](https://arxiv.org/html/2512.01967v1#Ch2 "2. Market coordinates, targets, and no-arbitrage axioms ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") defines the market
coordinates, targets and static no-arbitrage axioms. Chapters [3](https://arxiv.org/html/2512.01967v1#Ch3 "3. Warped tensor Chebyshev basis and design matrices ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")-[4](https://arxiv.org/html/2512.01967v1#Ch4 "4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") build the warped
Chebyshev tensor basis and the no-arbitrage operators on a collocation grid.
Chapters [5](https://arxiv.org/html/2512.01967v1#Ch5 "5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")-[7](https://arxiv.org/html/2512.01967v1#Ch7 "7. No–arbitrage constraints and soft penalties ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") specify the coverage-seeking data term and the soft no-arbitrage
penalties, and Chapter [8](https://arxiv.org/html/2512.01967v1#Ch8 "8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") assembles the global QP and discusses convexity and
solution. Chapters [6](https://arxiv.org/html/2512.01967v1#Ch6 "6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") and [10](https://arxiv.org/html/2512.01967v1#Ch10 "10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") develop the spectral and transport-inspired quadratic
regularisers, and Chapter [11](https://arxiv.org/html/2512.01967v1#Ch11 "11. Diagnostics and Implementation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") collects structure monitors that diagnose stability.
Chapter [12](https://arxiv.org/html/2512.01967v1#Ch12 "12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") then introduces the patch-wise Hamiltonian fog post-fit in price space,
formulated as a joint convex optimisation in the nodal surface and fog variables.
Chapter [13](https://arxiv.org/html/2512.01967v1#Ch13 "13. Conclusion and outlook ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") concludes and outlines a continuum version of the fog/Hamiltonian
geometry, which is deferred to a separate theoretical follow-up paper.

## 2.  Market coordinates, targets, and no-arbitrage axioms

Let tt be a trading date and Ft​(T)F\_{t}(T) denote the discount adjusted forward for maturity time TT. Set τ=T−t>0\tau=T-t>0, the time to maturity. We work in forward discounted prices:

|  |  |  |
| --- | --- | --- |
|  | Cf​(K,τ)≔er​(τ)​τ​C​(K,τ)andm≔log⁡KFt​(τ).C\_{f}(K,\tau)\;\coloneqq\;e^{r(\tau)\tau}C(K,\tau)\quad\text{and}\quad m\;\coloneqq\;\log\!\frac{K}{F\_{t}(\tau)}. |  |

Throughout, we fit a surface Cf​(m,τ)C\_{f}(m,\tau) from quoted calls. Puts follow from put-call parity.

These are sufficient conditions for Static no-arbitrage for calls (for a.e. m,τm,\tau):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂mCf​(m,τ)\displaystyle\partial\_{m}C\_{f}(m,\tau) | ≤0,\displaystyle\leq 0, |  | (2.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂m​mCf​(m,τ)\displaystyle\partial\_{mm}C\_{f}(m,\tau) | ≥0,\displaystyle\geq 0, |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂τCf​(m,τ)|K\displaystyle\partial\_{\tau}C\_{f}(m,\tau)\big|\_{K} | ≥0.\displaystyle\geq 0. |  | (2.3) |

Bounds: 0≤Cf​(m,τ)≤Ft​(τ)0\leq C\_{f}(m,\tau)\leq F\_{t}(\tau) and Cf​(m,0+)=(Ft​(0)−K)+C\_{f}(m,0^{+})=\big(F\_{t}(0)-K\big)^{+}.

Throughout this section we tacitly assume enough regularity for the continuum
derivatives in ([2.1](https://arxiv.org/html/2512.01967v1#Ch2.E1 "Equation 2.1 ‣ 2. Market coordinates, targets, and no-arbitrage axioms ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))–([2.3](https://arxiv.org/html/2512.01967v1#Ch2.E3 "Equation 2.3 ‣ 2. Market coordinates, targets, and no-arbitrage axioms ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) to be well defined on the compact rectangle
where we approximate the surface. In particular, on the box [mmin,mmax]×[τmin,τmax][m\_{\min},m\_{\max}]\times[\tau\_{\min},\tau\_{\max}] used in Section [3](https://arxiv.org/html/2512.01967v1#Ch3 "3. Warped tensor Chebyshev basis and design matrices ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), we work under

|  |  |  |
| --- | --- | --- |
|  | Cf∈C2,1​([mmin,mmax]×[τmin,τmax]),F∈C1​([τmin,τmax]),C\_{f}\in C^{2,1}\bigl([m\_{\min},m\_{\max}]\times[\tau\_{\min},\tau\_{\max}]\bigr),\qquad F\in C^{1}\bigl([\tau\_{\min},\tau\_{\max}]\bigr), |  |

so that ∂mCf\partial\_{m}C\_{f}, ∂m​mCf\partial\_{mm}C\_{f}, (∂τCf)|K(\partial\_{\tau}C\_{f})|\_{K} and
dd​τ​log⁡F​(τ)\frac{\mathrm{d}}{\mathrm{d}\tau}\log F(\tau) all exist and are continuous. The later
discrete QP only uses linear operators on a grid, but these smoothness conditions
provide the natural continuum axioms behind ([2.1](https://arxiv.org/html/2512.01967v1#Ch2.E1 "Equation 2.1 ‣ 2. Market coordinates, targets, and no-arbitrage axioms ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))–([2.3](https://arxiv.org/html/2512.01967v1#Ch2.E3 "Equation 2.3 ‣ 2. Market coordinates, targets, and no-arbitrage axioms ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")).

###### Remark 1 (Calendar derivative at fixed strike).

Since the basis uses (m,τ)(m,\tau), the calendar derivative at fixed KK becomes
∂τCf|K=∂τCf+∂mCf⋅∂τm|K=∂τCf−∂mCf⋅(rcc​(τ)+τ​rcc′​(τ)).\partial\_{\tau}C\_{f}|\_{K}=\partial\_{\tau}C\_{f}+\partial\_{m}C\_{f}\cdot\partial\_{\tau}m\big|\_{K}=\partial\_{\tau}C\_{f}-\partial\_{m}C\_{f}\cdot\big(r\_{\text{cc}}(\tau)+\tau r^{\prime}\_{\text{cc}}(\tau)\big).
This is implemented exactly in the operators below.

### Notation

| Symbol | Meaning |
| --- | --- |
| KK | Strike |
| τ\tau | Time to maturity T−tT-t |
| Ft​(τ)F\_{t}(\tau) | Forward (discount‑adjusted) underlying for τ\tau |
| mm | Log‑moneyness log⁡(K/Ft​(τ))\log(K/F\_{t}(\tau)) |
| CfC\_{f} | Forward‑discounted call price |
| ρ\rho | Risk‑neutral density ∂K​KCf\partial\_{KK}C\_{f} |
| A,Am,Am​m,AτA,\ A\_{m},\ A\_{mm},\ A\_{\tau} | Design/derivative blocks in coefficient space |

## 3.  Warped tensor Chebyshev basis and design matrices

This chapter builds the approximation space and its derivative blocks.

### 3.1  Why normalise to [−1,1]2[-1,1]^{2} and why Chebyshev?

The problem is to approximate a continuous surface Cf​(m,τ)C\_{f}(m,\tau) on a compact rectangle
[mmin,mmax]×[τmin,τmax][m\_{\min},m\_{\max}]\times[\tau\_{\min},\tau\_{\max}].
On a compact interval, polynomials are dense (Weierstrass), and Chebyshev polynomials are numerically preferred because:

1. (i)

   they minimise Runge oscillations on [−1,1][-1,1],
2. (ii)

   they admit stable three–term recurrences and Clenshaw evaluation,
3. (iii)

   they possess explicit derivative identities useful for Greeks.

We therefore map each axis to [−1,1][-1,1] and expand in a tensor-product
Chebyshev basis.

### 3.2  Coordinate warps (endpoint preserving)

Let [mmin,mmax][m\_{\min},m\_{\max}] and [τmin,τmax][\tau\_{\min},\tau\_{\max}] be robust, date-adaptive intervals.

Define the warps

|  |  |  |
| --- | --- | --- |
|  | x=Φm​(m)∈[−1,1],y=Φτ​(τ)∈[−1,1],x=\Phi\_{m}(m)\in[-1,1],\qquad y=\Phi\_{\tau}(\tau)\in[-1,1], |  |

so that the interval endpoints map exactly to ±1\pm 1.

##### Log-moneyness warp (asinh).

Let cmc\_{m} be a centre (e.g. the liquidity-weighted median of mm),
and λm>0\lambda\_{m}>0 a tail-compression parameter. Set

|  |  |  |
| --- | --- | --- |
|  | ϕm,±≔asinh⁡(λm​(mmax/min−cm)),Wm≔ϕm,+−ϕm,−,\phi\_{m,\pm}\coloneqq\operatorname{asinh}\!\big(\lambda\_{m}(m\_{\max/\min}-c\_{m})\big),\quad W\_{m}\coloneqq\phi\_{m,+}-\phi\_{m,-}, |  |

|  |  |  |
| --- | --- | --- |
|  | Φm​(m)=2Wm​(asinh⁡(λm​(m−cm))−ϕm,−)−1.\boxed{\ \Phi\_{m}(m)=\frac{2}{W\_{m}}\Big(\operatorname{asinh}(\lambda\_{m}(m-c\_{m}))-\phi\_{m,-}\Big)-1\ }. |  |

Then Φm​(mmin)=−1\Phi\_{m}(m\_{\min})=-1, Φm​(mmax)=+1\Phi\_{m}(m\_{\max})=+1. Derivatives (by the chain rule) are

|  |  |  |
| --- | --- | --- |
|  | Φm′​(m)=2​λmWm​11+λm2​(m−cm)2,Φm′′​(m)=−2​λm3Wm​(m−cm)(1+λm2​(m−cm)2)3/2.\Phi\_{m}^{\prime}(m)=\frac{2\lambda\_{m}}{W\_{m}}\frac{1}{\sqrt{1+\lambda\_{m}^{2}(m-c\_{m})^{2}}},\qquad\Phi\_{m}^{\prime\prime}(m)=-\frac{2\lambda\_{m}^{3}}{W\_{m}}\frac{(m-c\_{m})}{\big(1+\lambda\_{m}^{2}(m-c\_{m})^{2}\big)^{3/2}}. |  |

##### Maturity warp (square-root).

Let Δτ≔τmax−τmin>0\Delta\_{\tau}\coloneqq\tau\_{\max}-\tau\_{\min}>0 and s​(τ)≔(τ−τmin)/Δτ∈[0,1]s(\tau)\coloneqq(\tau-\tau\_{\min})/\Delta\_{\tau}\in[0,1]. Set

|  |  |  |
| --- | --- | --- |
|  | Φτ​(τ)=2​s​(τ)−1,Φτ′​(τ)=1Δτ​(τ−τmin)​(finite if ​τ>τmin).\boxed{\ \Phi\_{\tau}(\tau)=2\sqrt{s(\tau)}-1\ },\qquad\Phi\_{\tau}^{\prime}(\tau)=\frac{1}{\sqrt{\Delta\_{\tau}\,(\tau-\tau\_{\min})}}\;\;(\text{finite if }\tau>\tau\_{\min}). |  |

The square-root allocates higher resolution near short maturities.
(If τmin\tau\_{\min} is very close to 0, a small positive floor avoids the
endpoint singularity in Φτ′\Phi\_{\tau}^{\prime}.)

###### Remark 2 (Why these warps).

The asinh warp allocates more resolution near m≈cmm\approx c\_{m} (ATM) while compressing
deep wings; the square-root warp concentrates basis power near short maturities
where curvature in τ\tau is largest. Both preserve endpoints and expose simple
chain-rule factors for derivatives.

### 3.3  Chebyshev polynomials on [−1,1][-1,1]

For x∈[−1,1]x\in[-1,1], the Chebyshev polynomials of the first kind are

|  |  |  |
| --- | --- | --- |
|  | Tk​(x)=cos⁡(k​arccos⁡x),T0=1,T1=x,Tk+1=2​x​Tk−Tk−1.T\_{k}(x)=\cos\big(k\arccos x\big.),\qquad T\_{0}=1,\ \ T\_{1}=x,\ \ T\_{k+1}=2x\,T\_{k}-T\_{k-1}. |  |

The derivatives needed later are available in closed form:

|  |  |  |
| --- | --- | --- |
|  | Tk′​(x)=k​Uk−1​(x),T\_{k}^{\prime}(x)=k\,U\_{k-1}(x),\qquad |  |

and, for |x|<1|x|<1,

|  |  |  |
| --- | --- | --- |
|  | (1−x2)​Tk′′​(x)−x​Tk′​(x)+k2​Tk​(x)=0⇒Tk′′​(x)=x​k​Uk−1​(x)−k2​Tk​(x)1−x2,(1-x^{2})\,T\_{k}^{\prime\prime}(x)-x\,T\_{k}^{\prime}(x)+k^{2}\,T\_{k}(x)=0\;\Rightarrow\;\boxed{\ T\_{k}^{\prime\prime}(x)=\frac{x\,k\,U\_{k-1}(x)-k^{2}T\_{k}(x)}{1-x^{2}}\ }, |  |

where UnU\_{n} are Chebyshev polynomials of the second kind, which are defined recursively
(U0​(x)=1,U1​(x)=2​x,Un+1​(x)=2​x⋅Un​(x)−Un−1​(x)U\_{0}(x)=1,\,U\_{1}(x)=2x,\,U\_{n+1}(x)=2x\cdot U\_{n}(x)-U\_{n-1}(x)).
In practice, we evaluate Tk,Uk−1T\_{k},U\_{k-1} stably via Clenshaw recurrences.

### 3.4  Tensor-product basis for the surface

Let K,L∈ℕK,L\in\mathbb{N} be polynomial degrees in mm and τ\tau, and define
the coefficient array a={ak​ℓ}k=0,…,K;ℓ=0,…,La=\{a\_{k\ell}\}\_{k=0,\dots,K;\ \ell=0,\dots,L}.
We approximate

|  |  |  |
| --- | --- | --- |
|  | Cf​(m,τ)=∑k=0K∑ℓ=0Lak​ℓ​Tk​(Φm​(m))​Tℓ​(Φτ​(τ)).\boxed{\ C\_{f}(m,\tau)\;=\;\sum\_{k=0}^{K}\sum\_{\ell=0}^{L}a\_{k\ell}\,T\_{k}\!\big(\Phi\_{m}(m)\big)\,T\_{\ell}\!\big(\Phi\_{\tau}(\tau)\big)\ }. |  |

Stacking aa into a vector in ℝP\mathbb{R}^{P} with
P=(K+1)​(L+1)P=(K{+}1)(L{+}1) yields a linear map from coefficients to prices.

### 3.5  Design matrices at arbitrary points

Given data points {(mi,τi)}i=1N\{(m\_{i},\tau\_{i})\}\_{i=1}^{N}, set xi=Φm​(mi)x\_{i}=\Phi\_{m}(m\_{i}),
yi=Φτ​(τi)y\_{i}=\Phi\_{\tau}(\tau\_{i}). Define the following row vectors

|  |  |  |
| --- | --- | --- |
|  | 𝒕​(xi)=[T0​(xi),…,TK​(xi)],\bm{t}(x\_{i})=\big[T\_{0}(x\_{i}),\dots,T\_{K}(x\_{i})\big], |  |

|  |  |  |
| --- | --- | --- |
|  | 𝒔​(yi)=[T0​(yi),…,TL​(yi)].\bm{s}(y\_{i})=\big[T\_{0}(y\_{i}),\dots,T\_{L}(y\_{i})\big]. |  |

The pair (k,ℓ)(k,\ell) defines the index of the column (where k∈{0,…,K}k\in\{0,\dots,K\} and l∈{0,…,L}l\in\{0,\dots,L\}).

###### Definition 1.

The (price) design matrix A∈ℝN×PA\in\mathbb{R}^{N\times P} is defined as

|  |  |  |
| --- | --- | --- |
|  | Ai,(k,ℓ)=Tk​(xi)​Tℓ​(yi).\boxed{\ A\_{i,(k,\ell)}=T\_{k}(x\_{i})\,T\_{\ell}(y\_{i})\ }. |  |

Equivalently, if ΦK∈ℝN×(K+1)\Phi\_{K}\in\mathbb{R}^{N\times(K+1)} stacks 𝒕​(xi)\bm{t}(x\_{i}) and
ΦL∈ℝN×(L+1)\Phi\_{L}\in\mathbb{R}^{N\times(L+1)} stacks 𝒔​(yi)\bm{s}(y\_{i}), then AA is the
row-wise Khatri–Rao product A=ΦK⊙ΦLA=\Phi\_{K}\odot\Phi\_{L}; for grid evaluations,
Kronecker structure (ΦL⊗ΦK)(\Phi\_{L}\otimes\Phi\_{K}) can be exploited.

### 3.6  Derivative design blocks via the chain rule

###### Proposition 1 (Closed-form derivative design blocks).

Fix integers K,L≥0K,L\geq 0 and let P=(K+1)​(L+1)P=(K{+}1)(L{+}1). For each data point (mi,τi)(m\_{i},\tau\_{i}) define

|  |  |  |
| --- | --- | --- |
|  | xi≔Φm​(mi),yi≔Φτ​(τi),x\_{i}\coloneqq\Phi\_{m}(m\_{i}),\qquad y\_{i}\coloneqq\Phi\_{\tau}(\tau\_{i}), |  |

where Φm∈C2\Phi\_{m}\in C^{2} and Φτ∈C1\Phi\_{\tau}\in C^{1} on their domains. Let the price design matrix
A∈ℝN×PA\in\mathbb{R}^{N\times P} be

|  |  |  |
| --- | --- | --- |
|  | Ai,(k,ℓ)=Tk​(xi)​Tℓ​(yi),0≤k≤K, 0≤ℓ≤L,A\_{i,(k,\ell)}\;=\;T\_{k}(x\_{i})\,T\_{\ell}(y\_{i}),\qquad 0\leq k\leq K,\ 0\leq\ell\leq L, |  |

with any fixed stacking (k,ℓ)↦(k,ℓ)(k,\ell)\mapsto(k,\ell)-column. Define the “inner-variable” derivative
matrices by

|  |  |  |
| --- | --- | --- |
|  | (∂xA)i,(k,ℓ)≔Tk′​(xi)​Tℓ​(yi),(∂x​xA)i,(k,ℓ)≔Tk′′​(xi)​Tℓ​(yi),(\partial\_{x}A)\_{i,(k,\ell)}\coloneqq T\_{k}^{\prime}(x\_{i})\,T\_{\ell}(y\_{i}),\qquad(\partial\_{xx}A)\_{i,(k,\ell)}\coloneqq T\_{k}^{\prime\prime}(x\_{i})\,T\_{\ell}(y\_{i}), |  |

|  |  |  |
| --- | --- | --- |
|  | (∂yA)i,(k,ℓ)≔Tk​(xi)​Tℓ′​(yi).(\partial\_{y}A)\_{i,(k,\ell)}\coloneqq T\_{k}(x\_{i})\,T\_{\ell}^{\prime}(y\_{i}). |  |

For any coefficient vector a∈ℝPa\in\mathbb{R}^{P}, consider the model values

|  |  |  |
| --- | --- | --- |
|  | C^i=(A​a)i=∑k,ℓak​ℓ​Tk​(xi)​Tℓ​(yi).\widehat{C}\_{i}=(Aa)\_{i}=\sum\_{k,\ell}a\_{k\ell}\,T\_{k}(x\_{i})T\_{\ell}(y\_{i}). |  |

Then the vectors of physical derivatives evaluated at the same points are linear images of aa:

|  |  |  |
| --- | --- | --- |
|  | (∂mC^)i=(Am​a)i,(∂m​mC^)i=(Am​m​a)i,(∂τC^)i=(Aτ​a)i,\big(\partial\_{m}\widehat{C}\big)\_{i}=(A\_{m}a)\_{i},\qquad\big(\partial\_{mm}\widehat{C}\big)\_{i}=(A\_{mm}a)\_{i},\qquad\big(\partial\_{\tau}\widehat{C}\big)\_{i}=(A\_{\tau}a)\_{i}, |  |

where the derivative design blocks are

|  |  |  |
| --- | --- | --- |
|  | Am=diag(Φm′(m))∂xA,\boxed{\ A\_{m}\;=\;\operatorname{diag}\!\big(\Phi\_{m}^{\prime}(m)\big)\,\partial\_{x}A,} |  |

|  |  |  |
| --- | --- | --- |
|  | Am​m=diag((Φm′)2)∂x​xA+diag(Φm′′(m))∂xA,\boxed{A\_{mm}\;=\;\operatorname{diag}\!\big((\Phi\_{m}^{\prime})^{2}\big)\,\partial\_{xx}A\;+\;\operatorname{diag}\!\big(\Phi\_{m}^{\prime\prime}(m)\big)\,\partial\_{x}A,} |  |

|  |  |  |
| --- | --- | --- |
|  | Aτ=diag(Φτ′(τ))∂yA.\boxed{\ A\_{\tau}\;=\;\operatorname{diag}\!\big(\Phi\_{\tau}^{\prime}(\tau)\big)\,\partial\_{y}A.} |  |

###### Proof.

All statements follow from linearity and the chain rule, applied row-wise.

##### Setup:

Write the one–dimensional warped basis functions

|  |  |  |
| --- | --- | --- |
|  | ϕk​(m)≔Tk​(Φm​(m)),ψℓ​(τ)≔Tℓ​(Φτ​(τ)).\phi\_{k}(m)\coloneqq T\_{k}(\Phi\_{m}(m)),\qquad\psi\_{\ell}(\tau)\coloneqq T\_{\ell}(\Phi\_{\tau}(\tau)). |  |

Then the model at (mi,τi)(m\_{i},\tau\_{i}) is

|  |  |  |
| --- | --- | --- |
|  | C^i=∑k=0K∑ℓ=0Lak​ℓ​ϕk​(mi)​ψℓ​(τi)=∑k,ℓak​ℓ​Tk​(xi)​Tℓ​(yi).\widehat{C}\_{i}\;=\;\sum\_{k=0}^{K}\sum\_{\ell=0}^{L}a\_{k\ell}\,\phi\_{k}(m\_{i})\,\psi\_{\ell}(\tau\_{i})\;=\;\sum\_{k,\ell}a\_{k\ell}\,T\_{k}(x\_{i})\,T\_{\ell}(y\_{i}). |  |

By construction, the ii-th row of AA consists of the basis values
{Tk​(xi)​Tℓ​(yi)}k,ℓ\{T\_{k}(x\_{i})T\_{\ell}(y\_{i})\}\_{k,\ell}, so C^=A​a\widehat{C}=Aa.

##### First derivative in mm:

Differentiating ϕk​(m)=Tk​(Φm​(m))\phi\_{k}(m)=T\_{k}(\Phi\_{m}(m)) with respect to mm, by the chain rule we obtain the following:

|  |  |  |
| --- | --- | --- |
|  | dd​m​ϕk​(m)=Tk′​(Φm​(m))​Φm′​(m).\frac{d}{dm}\phi\_{k}(m)\;=\;T\_{k}^{\prime}\!\big(\Phi\_{m}(m)\big)\,\Phi\_{m}^{\prime}(m). |  |

Fixing τ\tau , the derivative of each product is

|  |  |  |
| --- | --- | --- |
|  | ∂∂m​[ϕk​(m)​ψℓ​(τ)]=Tk′​(Φm​(m))​Φm′​(m)⋅Tℓ​(Φτ​(τ)).\frac{\partial}{\partial m}\big[\phi\_{k}(m)\psi\_{\ell}(\tau)\big]=T\_{k}^{\prime}\!\big(\Phi\_{m}(m)\big)\,\Phi\_{m}^{\prime}(m)\cdot T\_{\ell}\!\big(\Phi\_{\tau}(\tau)\big). |  |

Evaluating at (mi,τi)(m\_{i},\tau\_{i}) and summing over (k,ℓ)(k,\ell):

|  |  |  |
| --- | --- | --- |
|  | (∂mC^)i=Φm′​(mi)​∑k,ℓak​ℓ​Tk′​(xi)​Tℓ​(yi)=(Φm′​(mi)⋅(∂xA​a)i).\big(\partial\_{m}\widehat{C}\big)\_{i}=\Phi\_{m}^{\prime}(m\_{i})\sum\_{k,\ell}a\_{k\ell}\,T\_{k}^{\prime}(x\_{i})\,T\_{\ell}(y\_{i})=\big(\ \Phi\_{m}^{\prime}(m\_{i})\cdot(\partial\_{x}A\,a)\_{i}\ \big). |  |

Taking the scalar formula for each ii and writing as a vector-matrix equation yields

|  |  |  |
| --- | --- | --- |
|  | ∂mC^=diag⁡(Φm′​(m))​∂xA​a,\partial\_{m}\widehat{C}=\operatorname{diag}(\Phi\_{m}^{\prime}(m))\,\partial\_{x}A\,a, |  |

where
Am=diag⁡(Φm′​(m))​∂xAA\_{m}=\operatorname{diag}(\Phi\_{m}^{\prime}(m))\,\partial\_{x}A.

##### Second derivative in mm:

Differentiate once more, using the product rule and chain rule:

|  |  |  |
| --- | --- | --- |
|  | d2d​m2​ϕk​(m)=dd​m​(Tk′​(Φm​(m))​Φm′​(m))\frac{d^{2}}{dm^{2}}\phi\_{k}(m)=\frac{d}{dm}\Big(T\_{k}^{\prime}\!\big(\Phi\_{m}(m)\big)\,\Phi\_{m}^{\prime}(m)\Big) |  |

|  |  |  |
| --- | --- | --- |
|  | =Tk′′​(Φm​(m))​(Φm′​(m))2+Tk′​(Φm​(m))​Φm′′​(m).=T\_{k}^{\prime\prime}\!\big(\Phi\_{m}(m)\big)\,(\Phi\_{m}^{\prime}(m))^{2}+T\_{k}^{\prime}\!\big(\Phi\_{m}(m)\big)\,\Phi\_{m}^{\prime\prime}(m). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | ∂2∂m2​[ϕk​(m)​ψℓ​(τ)]=(Tk′′​(Φm​(m))​(Φm′)2+Tk′​(Φm​(m))​Φm′′)​Tℓ​(Φτ​(τ)).\frac{\partial^{2}}{\partial m^{2}}\big[\phi\_{k}(m)\psi\_{\ell}(\tau)\big]=\Big(T\_{k}^{\prime\prime}(\Phi\_{m}(m))(\Phi\_{m}^{\prime})^{2}+T\_{k}^{\prime}(\Phi\_{m}(m))\Phi\_{m}^{\prime\prime}\Big)\,T\_{\ell}(\Phi\_{\tau}(\tau)). |  |

Evaluating at (mi,τi)(m\_{i},\tau\_{i}) and summing,

|  |  |  |
| --- | --- | --- |
|  | (∂m​mC^)i=(Φm′​(mi))2​∑k,ℓak​ℓ​Tk′′​(xi)​Tℓ​(yi)+Φm′′​(mi)​∑k,ℓak​ℓ​Tk′​(xi)​Tℓ​(yi).\big(\partial\_{mm}\widehat{C}\big)\_{i}=(\Phi\_{m}^{\prime}(m\_{i}))^{2}\sum\_{k,\ell}a\_{k\ell}\,T\_{k}^{\prime\prime}(x\_{i})\,T\_{\ell}(y\_{i})+\Phi\_{m}^{\prime\prime}(m\_{i})\sum\_{k,\ell}a\_{k\ell}\,T\_{k}^{\prime}(x\_{i})\,T\_{\ell}(y\_{i}). |  |

In matrix form,

|  |  |  |
| --- | --- | --- |
|  | ∂m​mC^=diag⁡((Φm′​(m))2)​∂x​xA​a+diag⁡(Φm′′​(m))​∂xA​a,\partial\_{mm}\widehat{C}=\operatorname{diag}\!\big((\Phi\_{m}^{\prime}(m))^{2}\big)\,\partial\_{xx}A\,a\;+\;\operatorname{diag}\!\big(\Phi\_{m}^{\prime\prime}(m)\big)\,\partial\_{x}A\,a, |  |

so Am​m=diag⁡((Φm′)2)​∂x​xA+diag⁡(Φm′′)​∂xAA\_{mm}=\operatorname{diag}((\Phi\_{m}^{\prime})^{2})\partial\_{xx}A+\operatorname{diag}(\Phi\_{m}^{\prime\prime})\partial\_{x}A.

##### First derivative in τ\tau:

Analogously, with y=Φτ​(τ)y=\Phi\_{\tau}(\tau),

|  |  |  |
| --- | --- | --- |
|  | dd​τ​ψℓ​(τ)=Tℓ′​(Φτ​(τ))​Φτ′​(τ),\frac{d}{d\tau}\psi\_{\ell}(\tau)\;=\;T\_{\ell}^{\prime}\!\big(\Phi\_{\tau}(\tau)\big)\,\Phi\_{\tau}^{\prime}(\tau), |  |

Fixing mm ,

|  |  |  |
| --- | --- | --- |
|  | ∂∂τ​[ϕk​(m)​ψℓ​(τ)]=Tk​(Φm​(m))​Tℓ′​(Φτ​(τ))​Φτ′​(τ).\frac{\partial}{\partial\tau}\big[\phi\_{k}(m)\psi\_{\ell}(\tau)\big]=T\_{k}(\Phi\_{m}(m))\,T\_{\ell}^{\prime}(\Phi\_{\tau}(\tau))\,\Phi\_{\tau}^{\prime}(\tau). |  |

Evaluating at (mi,τi)(m\_{i},\tau\_{i}) and summing over (k,ℓ)(k,\ell) yields:

|  |  |  |
| --- | --- | --- |
|  | (∂τC^)i=Φτ′​(τi)​∑k,ℓak​ℓ​Tk​(xi)​Tℓ′​(yi)=(Φτ′​(τi)⋅(∂yA​a)i),\big(\partial\_{\tau}\widehat{C}\big)\_{i}=\Phi\_{\tau}^{\prime}(\tau\_{i})\sum\_{k,\ell}a\_{k\ell}\,T\_{k}(x\_{i})\,T\_{\ell}^{\prime}(y\_{i})=\big(\ \Phi\_{\tau}^{\prime}(\tau\_{i})\cdot(\partial\_{y}A\,a)\_{i}\ \big), |  |

Taking the scalar formula for each ii and writing as a vector-matrix equation yields

|  |  |  |
| --- | --- | --- |
|  | ∂τC^=diag⁡(Φτ′​(τ))​∂yA​a\partial\_{\tau}\widehat{C}=\operatorname{diag}(\Phi\_{\tau}^{\prime}(\tau))\,\partial\_{y}A\,a |  |

where
Aτ=diag⁡(Φτ′​(τ))​∂yAA\_{\tau}=\operatorname{diag}(\Phi\_{\tau}^{\prime}(\tau))\,\partial\_{y}A.

##### Conclusion.

In each case the derivative vector equals a fixed matrix (depending only on the warps and basis) times aa, establishing the stated formulas.
∎

###### Remark 3.

Precompute {Tk​(xi),Uk−1​(xi)}k≤K\{T\_{k}(x\_{i}),U\_{k-1}(x\_{i})\}\_{k\leq K} and
{Tℓ​(yi),Uℓ−1​(yi)}ℓ≤L\{T\_{\ell}(y\_{i}),U\_{\ell-1}(y\_{i})\}\_{\ell\leq L} via Clenshaw recurrences.
Then obtain Tk′​(xi)=k​Uk−1​(xi)T\_{k}^{\prime}(x\_{i})=k\,U\_{k-1}(x\_{i}) and, for interior points |xi|<1|x\_{i}|<1,
Tk′′​(xi)=(xi​k​Uk−1​(xi)−k2​Tk​(xi))/(1−xi2)T\_{k}^{\prime\prime}(x\_{i})=\big(x\_{i}\,k\,U\_{k-1}(x\_{i})-k^{2}T\_{k}(x\_{i})\big)/(1-x\_{i}^{2}).
At the Chebyshev–Lobatto endpoints x=±1x=\pm 1 the denominator 1−x21-x^{2} vanishes, but
TkT\_{k} is a polynomial so Tk′′​(x)T^{\prime\prime}\_{k}(x) exists and is finite there. In practice we define
Tk′′​(±1)T^{\prime\prime}\_{k}(\pm 1) by continuity (or via the closed forms
Tk′′​(1)=k2​(k2−1)3T^{\prime\prime}\_{k}(1)=\tfrac{k^{2}(k^{2}-1)}{3} and
Tk′′​(−1)=(−1)k​k2​(k2−1)3T^{\prime\prime}\_{k}(-1)=(-1)^{k}\tfrac{k^{2}(k^{2}-1)}{3} for k≥2k\geq 2) and use these values whenever
|1−xi2||1-x\_{i}^{2}| is numerically small. With this convention, all entries of ∂x​xA\partial\_{xx}A
are well defined and the assembly of A,∂xA,∂x​xA,∂yAA,\partial\_{x}A,\partial\_{xx}A,\partial\_{y}A uses
only closed-form expressions, with no numerical differencing.

## 4.  No-arbitrage operators on a collocation grid

From the previous chapter we have for any set of evaluation points (m,τ)(m,\tau), the
price design matrix AA and the derivative blocks Am,Am​m,AτA\_{m},A\_{mm},A\_{\tau} are defined by

|  |  |  |
| --- | --- | --- |
|  | (A​a)​(m,τ)=Cf​(m,τ),(Am​a)​(m,τ)=∂mCf,(Aa)(m,\tau)=C\_{f}(m,\tau),\quad(A\_{m}a)(m,\tau)=\partial\_{m}C\_{f},\quad |  |

|  |  |  |
| --- | --- | --- |
|  | (Am​m​a)​(m,τ)=∂m​mCf,(Aτ​a)​(m,τ)=∂τCf.(A\_{mm}a)(m,\tau)=\partial\_{mm}C\_{f},\quad(A\_{\tau}a)(m,\tau)=\partial\_{\tau}C\_{f}. |  |

All maps are linear in aa and are computed pointwise via the chain rule.

### 4.1  Collocation grid and evaluation

Let {(mg,τg)}g=1G\{(m\_{g},\tau\_{g})\}\_{g=1}^{G} be a fixed collocation grid used to test the
no-arbitrage shape conditions (Chebyshev nodes in mm, uniform in τ\tau are a robust choice).
On this grid define the forward (no-arbitrage price of receiving one unit of the underlying at time (t+τ)(t+\tau)) and strike (rearrangement from the definition of mm)

|  |  |  |
| --- | --- | --- |
|  | Fg≔Ft​(τg),Kg≔Fg​emg.F\_{g}\coloneqq F\_{t}(\tau\_{g}),\qquad K\_{g}\coloneqq F\_{g}\,e^{m\_{g}}. |  |

We evaluate the same derivative blocks on the grid (rather than on {(mi,τi)}i=1N\{(m\_{i},\tau\_{i})\}\_{i=1}^{N}, we evaluate on {(mg,τg)}g=1G\{(m\_{g},\tau\_{g})\}\_{g=1}^{G}); keeping the
symbols A,Am,Am​m,AτA,A\_{m},A\_{mm},A\_{\tau} for the G×PG\times P versions where the gg-th row corresponds
to (mg,τg)(m\_{g},\tau\_{g}).

###### Remark 4 (Why a separate grid).

Quotes can be sparse or clustered. A collocation grid decouples shape testing from where data happen to lie and gives uniform control of violations over the rectangle in (m,τ)(m,\tau).

### 4.2  Strike-space operators (monotonicity and convexity)

Static no-arb for *calls* requires ∂KCf≤0\partial\_{K}C\_{f}\leq 0 and ∂K​KCf≥0\partial\_{KK}C\_{f}\geq 0 at fixed τ\tau.
However, our derivative blocks are in the mm coordinate, where m=ln⁡(K/F​(τ))m=\ln\!\big(K/F(\tau)\big).
At fixed τ\tau,

|  |  |  |
| --- | --- | --- |
|  | ∂m∂K=1K,∂2m∂K2=−1K2.\frac{\partial m}{\partial K}=\frac{1}{K},\qquad\frac{\partial^{2}m}{\partial K^{2}}=-\frac{1}{K^{2}}. |  |

For any smooth f​(m,τ)f(m,\tau), by the chain rule

|  |  |  |
| --- | --- | --- |
|  | ∂f∂K|τ=1K​fm,∂2f∂K2|τ=1K2​(fm​m−fm).\frac{\partial f}{\partial K}\Big|\_{\tau}=\frac{1}{K}\,f\_{m},\qquad\frac{\partial^{2}f}{\partial K^{2}}\Big|\_{\tau}=\frac{1}{K^{2}}\,(f\_{mm}-f\_{m}). |  |

Apply this with f=Cff=C\_{f} row-wise on the grid, replacing fmf\_{m} and fm​mf\_{mm} by Am​aA\_{m}a and
Am​m​aA\_{mm}a.

|  |  |  |
| --- | --- | --- |
|  | ∂KCf​(Kg,τg)=1Kg​∂mCf​(mg,τg)=1Kg​(Am​a)g\partial\_{K}C\_{f}(K\_{g},\tau\_{g})=\frac{1}{K\_{g}}\partial\_{m}C\_{f}(m\_{g},\tau\_{g})=\frac{1}{K\_{g}}(A\_{m}a)\_{g} |  |

|  |  |  |
| --- | --- | --- |
|  | ∂K​KCf​(Kg,τg)=−1Kg2​∂mCf​(mg,τg)+1Kg2​∂m​mCf​(mg,τg)=(Am​m​a)g−(Am​a)gKg2\partial\_{KK}C\_{f}(K\_{g},\tau\_{g})=-\frac{1}{K\_{g}^{2}}\partial\_{m}C\_{f}(m\_{g},\tau\_{g})+\frac{1}{K\_{g}^{2}}\partial\_{mm}C\_{f}(m\_{g},\tau\_{g})=\frac{(A\_{mm}a)\_{g}-(A\_{m}a)\_{g}}{K\_{g}^{2}} |  |

This yields the *linear operators* that map coefficients aa to strike derivatives:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Monotonicity in strike: | AK=diag(Kg)−1Am,\displaystyle A\_{K}\;=\;\operatorname{diag}(K\_{g})^{-1}\,A\_{m}, |  | (4.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Convexity in strike: | AK​K=diag(Kg)−2(Am​m−Am).\displaystyle A\_{KK}\;=\;\operatorname{diag}(K\_{g})^{-2}\,\big(A\_{mm}-A\_{m}\big). |  | (4.2) |

Thus, (AK​a)g=∂KCf​(Kg,τg)(A\_{K}a)\_{g}=\partial\_{K}C\_{f}(K\_{g},\tau\_{g}) and (AK​K​a)g=∂K​KCf​(Kg,τg)(A\_{KK}a)\_{g}=\partial\_{KK}C\_{f}(K\_{g},\tau\_{g}).

### 4.3  Calendar derivative at fixed strike

Calendar no-arbitrage requires ∂τCf|K≥0\partial\_{\tau}C\_{f}\big|\_{K}\geq 0.
The block AτA\_{\tau} computes ∂τCf\partial\_{\tau}C\_{f} at fixed mm; to switch to fixed KK use the following relation

|  |  |  |
| --- | --- | --- |
|  | (∂τCf)K=(∂τCf)m+(∂mCf)​(∂τm)K.\Big(\partial\_{\tau}C\_{f}\Big)\_{\!K}=\Big(\partial\_{\tau}C\_{f}\Big)\_{\!m}+\Big(\partial\_{m}C\_{f}\Big)\Big(\partial\_{\tau}m\Big)\_{\!K}. |  |

With m=log⁡(K/F​(τ))m=\log\big(K/F(\tau)\big.) and KK fixed,

|  |  |  |
| --- | --- | --- |
|  | (∂τm)K=−dd​τ​log⁡F​(τ).\Big(\partial\_{\tau}m\Big)\_{\!K}=-\,\frac{d}{d\tau}\log F(\tau). |  |

Two equivalent parameterisations of FF give:

*(i) General form.* Let ρ​(τ)≔dd​τ​log⁡F​(τ)\rho(\tau)\coloneqq\tfrac{d}{d\tau}\log F(\tau).
Then

|  |  |  |
| --- | --- | --- |
|  | Aτ|K=Aτ−diag⁡(ρ​(τg))​Am.A\_{\tau|K}\;=\;A\_{\tau}\;-\;\operatorname{diag}\!\big(\rho(\tau\_{g})\big)\,A\_{m}. |  |

*(ii) Report convention.* If log⁡F​(τ)=τ​rcc​(τ)\log F(\tau)=\tau\,r\_{\mathrm{cc}}(\tau) (net continuously
compounded carry), then
ρ​(τ)=rcc​(τ)+τ​rcc′​(τ)\rho(\tau)=r\_{\mathrm{cc}}(\tau)+\tau\,r^{\prime}\_{\mathrm{cc}}(\tau) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aτ|K=Aτ+diag⁡(−rcc​(τg)−τg​rcc′​(τg))​Am.A\_{\tau|K}\;=\;A\_{\tau}\;+\;\operatorname{diag}\!\big(-r\_{\mathrm{cc}}(\tau\_{g})-\tau\_{g}r^{\prime}\_{\mathrm{cc}}(\tau\_{g})\big)\,A\_{m}. |  | (4.3) |

###### Remark 5 (Sanity checks).

If FF is flat (zero carry), then ρ≡0\rho\equiv 0 and Aτ|K=AτA\_{\tau|K}=A\_{\tau}.
If carry is constant rr, then ρ≡r\rho\equiv r and Aτ|K=Aτ−r​AmA\_{\tau|K}=A\_{\tau}-r\,A\_{m}.

### 4.4  Price map and bound operators

Price non-negativity and upper bounds by the forward read on the grid as

|  |  |  |
| --- | --- | --- |
|  | 0≤(A​a)g≤Fg,g=1,…,G.0\ \leq\ (Aa)\_{g}\ \leq\ F\_{g},\qquad g=1,\dots,G. |  |

Simply write Aprice=AA\_{\text{price}}=A and use the known vector F=(Fg)gF=(F\_{g})\_{g} when
imposing hard constraints or soft penalties for violations.

### 4.5  Row scaling and a single no-arb weight

The three no-arbitrage defect maps have different natural magnitudes and units:

|  |  |  |
| --- | --- | --- |
|  | AK​a(“price per strike”),−AK​K​a(“price per strike2​”),A\_{K}a\quad(\text{``price per strike''}),\qquad-A\_{KK}a\quad(\text{``price per strike}^{2}\text{''}), |  |

|  |  |  |
| --- | --- | --- |
|  | −Aτ|K​a(“price per time”).-A\_{\tau|K}a\quad(\text{``price per time''}). |  |

If a single penalty weight λNA\lambda\_{\mathrm{NA}} is applied to all three without normalisation, the largest magnitude block dominates and the others become numerically inert. Therefore, normalise each block by a positive scalar so that a single λNA\lambda\_{\mathrm{NA}} can control them comparably.

##### Blocks to be normalised:

On the collocation grid (size G×PG\times P), set

|  |  |  |
| --- | --- | --- |
|  | B1≔AK,B2≔−AK​K,B3≔−Aτ|K.B\_{1}\coloneqq A\_{K},\qquad B\_{2}\coloneqq-\,A\_{KK},\qquad B\_{3}\coloneqq-\,A\_{\tau|K}. |  |

##### Robust block scales:

For each j∈{1,2,3}j\in\{1,2,3\}, compute Euclidean row ℓ2\ell\_{2} norms

|  |  |  |
| --- | --- | --- |
|  | rg(j)≔‖(Bj)g,:‖2=∑p=1P(Bj)g​p2,g=1,…,Gr^{(j)}\_{g}\coloneqq\|(B\_{j})\_{g,:}\|\_{2}=\sqrt{\sum\_{p=1}^{P}(B\_{j})^{2}\_{gp}},\qquad g=1,\dots,G |  |

Sorting the list in ascending order, pick the value sjs\_{j} below which 95%95\% of the rg(j)r^{(j)}\_{g} fall.

###### Definition 2.

The robust scale is defined as

|  |  |  |
| --- | --- | --- |
|  | sj≔q0.95​({rg(j):g=1,…,G}),s\_{j}\;\coloneqq\;\mathrm{q}\_{0.95}\!\big(\{\,r^{(j)}\_{g}\,:\,g=1,\dots,G\}\big), |  |

(Other robust choices are possible; q0.95q\_{0.95} balances outliers vs. typical rows.)

##### Scaled blocks and unified weight:

Define the scaled operators

|  |  |  |
| --- | --- | --- |
|  | B~j≔1sj​Bj,j=1,2,3.\widetilde{B}\_{j}\;\coloneqq\;\frac{1}{s\_{j}}\,B\_{j},\qquad j=1,2,3. |  |

Using a single λNA\lambda\_{\mathrm{NA}} for all three terms, the soft no–arbitrage penalty becomes

|  |  |  |
| --- | --- | --- |
|  | λNA2​∑j=13‖(B~j​a)+‖22=12​∑j=13(λNAsj2)⏟effective weight for block j​‖(Bj​a)+‖22,\frac{\lambda\_{\mathrm{NA}}}{2}\sum\_{j=1}^{3}\big\|(\widetilde{B}\_{j}a)\_{+}\big\|\_{2}^{2}\;=\;\frac{1}{2}\sum\_{j=1}^{3}\underbrace{\Big(\frac{\lambda\_{\mathrm{NA}}}{s\_{j}^{2}}\Big)}\_{\text{effective weight for block $j$}}\;\big\|(B\_{j}a)\_{+}\big\|\_{2}^{2}, |  |

so that the typical (p95) row magnitude of each block is ≈1\approx 1 and one knob λNA\lambda\_{\mathrm{NA}} moves all three violation shares on a comparable scale.

###### Proposition 2 (Invariance of hard constraints under positive scaling).

Let DD be any positive diagonal matrix (in particular D=α​ID=\alpha I with α>0\alpha>0). Then, for any B∈ℝG×PB\in\mathbb{R}^{G\times P} and any a∈ℝPa\in\mathbb{R}^{P},

|  |  |  |
| --- | --- | --- |
|  | B​a≤0⟺(D​B)​a≤0.Ba\leq 0\;\Longleftrightarrow\;(DB)a\leq 0. |  |

Hence replacing BjB\_{j} by B~j=1sj​Bj\widetilde{B}\_{j}=\frac{1}{s\_{j}}B\_{j} leaves the hard no–arbitrage feasible set unchanged; only numerical conditioning and relative penalty weights are affected.

###### Proof.

All inequalities are understood componentwise.

Let D=diag⁡(d1,…,dG)D=\operatorname{diag}(d\_{1},\dots,d\_{G}) with di>0d\_{i}>0 for all ii. For any
a∈ℝPa\in\mathbb{R}^{P} we have

|  |  |  |
| --- | --- | --- |
|  | (D​B)​a=D​(B​a),(DB)a=D(Ba), |  |

so on the ii-th component

|  |  |  |
| --- | --- | --- |
|  | ((D​B)​a)i=di​(B​a)i.\bigl((DB)a\bigr)\_{i}=d\_{i}\,(Ba)\_{i}. |  |

(⇒\Rightarrow) Suppose B​a≤0Ba\leq 0. Then for every ii,

|  |  |  |
| --- | --- | --- |
|  | (B​a)i≤0⟹di​(B​a)i≤0(Ba)\_{i}\leq 0\quad\Longrightarrow\quad d\_{i}(Ba)\_{i}\leq 0 |  |

because di>0d\_{i}>0. Hence (D​B)​a=D​(B​a)≤0(DB)a=D(Ba)\leq 0.

(⇐\Leftarrow) Conversely, suppose (D​B)​a≤0(DB)a\leq 0. Then for every ii,

|  |  |  |
| --- | --- | --- |
|  | di​(B​a)i=((D​B)​a)i≤0.d\_{i}(Ba)\_{i}=\bigl((DB)a\bigr)\_{i}\leq 0. |  |

Since di>0d\_{i}>0, dividing by did\_{i} preserves the inequality sign and yields

|  |  |  |
| --- | --- | --- |
|  | (B​a)i≤0for all ​i,(Ba)\_{i}\leq 0\quad\text{for all }i, |  |

i.e. B​a≤0Ba\leq 0.

Thus {a:B​a≤0}={a:(D​B)​a≤0}\{a:Ba\leq 0\}=\{a:(DB)a\leq 0\}, proving the equivalence
B​a≤0⟺(D​B)​a≤0Ba\leq 0\;\Longleftrightarrow\;(DB)a\leq 0.

For the final claim, take D=1sj​ID=\frac{1}{s\_{j}}I with sj>0s\_{j}>0 and BB replaced
by a given block BjB\_{j}. Then

|  |  |  |
| --- | --- | --- |
|  | Bj​a≤0⟺(1sj​I​Bj)​a≤0⟺B~j​a≤0,B\_{j}a\leq 0\;\Longleftrightarrow\;\Bigl(\frac{1}{s\_{j}}I\,B\_{j}\Bigr)a\leq 0\;\Longleftrightarrow\;\widetilde{B}\_{j}a\leq 0, |  |

so replacing BjB\_{j} by B~j=1sj​Bj\widetilde{B}\_{j}=\frac{1}{s\_{j}}B\_{j} leaves the hard
no–arbitrage feasible set {a:Bj​a≤0}\{a:B\_{j}a\leq 0\} (and hence the intersection over
all blocks jj) unchanged. Only the numerical conditioning of the operators and
the effective relative weights in any soft penalties involving BjB\_{j} are affected.
∎

###### Remark 6 (Exact recipe used in this paper).

1. 1.

   *Where scaling is applied.* We first apply any coefficient reparameterisation UU (price–invariant transform), i.e. replace each block by A∙​UA\_{\bullet}U. Scaling is computed and applied to these *post-UU* blocks.
2. 2.

   *Which blocks.* We scale B1=AKB\_{1}=A\_{K}, B2=−AK​KB\_{2}=-A\_{KK}, B3=−Aτ|KB\_{3}=-A\_{\tau|K} by *one scalar per block*: sK,sK​K,sτs\_{K},s\_{KK},s\_{\tau} given by the p95 of row ℓ2\ell\_{2} norms on the collocation grid.
3. 3.

   *How it enters the objective.* The no–arb penalty uses the scaled operators B~j=Bj/sj\widetilde{B}\_{j}=B\_{j}/s\_{j} with a *single* weight λNA\lambda\_{\mathrm{NA}}:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝒫NA​(a)=λNA2​(‖(A~K​a)+‖22+‖(−A~K​K​a)+‖22+‖(−A~τ|K​a)+‖22).\mathcal{P}\_{\mathrm{NA}}(a)=\frac{\lambda\_{\mathrm{NA}}}{2}\!\left(\big\|(\widetilde{A}\_{K}a)\_{+}\big\|\_{2}^{2}+\big\|(-\widetilde{A}\_{KK}a)\_{+}\big\|\_{2}^{2}+\big\|(-\widetilde{A}\_{\tau|K}a)\_{+}\big\|\_{2}^{2}\right). |  |
4. 4.

   *Bounds kept separate.* Price bounds 0≤A​a≤F0\leq Aa\leq F are handled with a separate weight λB\lambda\_{B}; we do not include AA in the no–arb scaling group.
5. 5.

   *Reporting.* Diagnostics/violation shares are computed from the unscaled physical operators AK,AK​K,Aτ|KA\_{K},A\_{KK},A\_{\tau|K}.

###### Remark 7 (Alternative (not used): row–by–row equalisation).

One may also scale *each row* to equalise row influence by taking Dj=diag⁡(dg(j))D\_{j}=\operatorname{diag}(d^{(j)}\_{g}) with dg(j)=1/max⁡(‖(Bj)g,:‖2,ε)d^{(j)}\_{g}=1/\max(\|(B\_{j})\_{g,:}\|\_{2},\varepsilon) and using Dj​BjD\_{j}B\_{j}. This preserves feasibility for hard constraints (Prop. [2](https://arxiv.org/html/2512.01967v1#Thmprop2 "Proposition 2 (Invariance of hard constraints under positive scaling). ‣ Scaled blocks and unified weight: ‣ 4.5 Row scaling and a single no-arb weight ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) but reweights the grid non–uniformly. We *do not* use this in our main results; we use the block–scalar scheme of Remark [6](https://arxiv.org/html/2512.01967v1#Thmremark6 "Remark 6 (Exact recipe used in this paper). ‣ Scaled blocks and unified weight: ‣ 4.5 Row scaling and a single no-arb weight ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

### 4.6  Summary (operators used in the optimiser)

On the collocation grid, the no-arbitrage conditions become linear maps of aa:

|  |  |  |
| --- | --- | --- |
|  | strike monotonicity:AK​a≤ 0,strike convexity:−AK​K​a≤ 0,calendar at fixed K:−Aτ|K​a≤ 0,bounds:0≤A​a≤F.\begin{array}[]{ll}\text{strike monotonicity:}&A\_{K}a\ \leq\ 0,\\[2.0pt] \text{strike convexity:}&-\,A\_{KK}a\ \leq\ 0,\\[2.0pt] \text{calendar at fixed $K$:}&-\,A\_{\tau|K}a\ \leq\ 0,\\[2.0pt] \text{bounds:}&0\ \leq\ Aa\ \leq\ F.\end{array} |  |

Enforce these either as hard linear inequalities or as convex quadratic penalties on the positive parts, all while keeping the problem a single QP.

## 5.  Coverage-seeking data term with bid-ask geometry

On date tt, let {(mi,τi)}i=1N\{(m\_{i},\tau\_{i})\}\_{i=1}^{N} be the quote locations, and let

|  |  |  |
| --- | --- | --- |
|  | bi≔bidi,ai≔aski,yi≔12​(bidi+aski),b\_{i}\coloneqq\text{bid}\_{i},\qquad a\_{i}\coloneqq\text{ask}\_{i},\qquad y\_{i}\coloneqq\tfrac{1}{2}(\text{bid}\_{i}+\text{ask}\_{i}), |  |

be the forward–discounted band endpoints and mids (0≤bi≤ai0\leq b\_{i}\leq a\_{i} after standard cleaning).
Let A∈ℝN×PA\in\mathbb{R}^{N\times P} be the price design matrix so that y^​(a)≔A​a\widehat{y}(a)\coloneqq Aa are model
prices at the quote points. Set heteroscedastic residual weights

|  |  |  |
| --- | --- | --- |
|  | wi=liqimax(ai−bi,ε)2,W≔diag⁡(w1,…,wN),w\_{i}\;=\;\frac{\mathrm{liq}\_{i}}{\max(a\_{i}-b\_{i},\varepsilon)^{2}},\qquad W\coloneqq\operatorname{diag}(w\_{1},\dots,w\_{N}), |  |

where liqi=1+volumei+0.1​open​\_​interesti\mathrm{liq}\_{i}=1+\sqrt{\mathrm{volume}\_{i}}+0.1\sqrt{\mathrm{open\\_interest}\_{i}} and with a small floor ε>0\varepsilon>0.

### 5.1  Loss components and their roles

Use two convex terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒfit​(a)=12​‖W1/2​(A​a−y)‖22⏟within-band centre anchor+μ​∑i=1Nℓband​((A​a)i;bi,ai)⏟coverage/Slack pricing,\mathcal{L}\_{\text{fit}}(a)\;=\;\underbrace{\frac{1}{2}\,\|W^{1/2}(Aa-y)\|\_{2}^{2}}\_{\text{within-band centre anchor}}\;+\;\underbrace{\mu\sum\_{i=1}^{N}\ell\_{\text{band}}\big((Aa)\_{i};b\_{i},a\_{i}\big)}\_{\text{coverage/Slack pricing}}, |  | (5.1) |

where the *quadratic band hinge* for a scalar y^\hat{y} and interval [b,a][b,a] is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓband(y^;b,a)=12(max{b−y^,0}2+max{y^−a,0}2)=12dist(y^,[b,a])2.\ell\_{\text{band}}(\hat{y};b,a)\;=\;\frac{1}{2}\big(\max\{b-\hat{y},0\}^{2}+\max\{\hat{y}-a,0\}^{2}\big)\;=\;\frac{1}{2}\,\mathrm{dist}\!\big(\hat{y},[b,a]\big)^{2}. |  | (5.2) |

This means that ℓband​(y^;b,a)=0\ell\_{\text{band}}(\hat{y};b,a)=0 iff y^∈[b,a]\hat{y}\in[b,a], and otherwise equals one–half the
squared Euclidean distance to the band. The first term in ([5.1](https://arxiv.org/html/2512.01967v1#Ch5.E1 "Equation 5.1 ‣ 5.1 Loss components and their roles ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) selects a point
*inside* the band (preferentially near yy defined as the mid) whenever that is compatible with the other constraints;
the second term is a convex surrogate that drives *coverage* by penalizing exactly the squared
violation outside the band.

###### Lemma 1 (Convexity of band loss and fit objective).

Fix b≤ab\leq a and define ℓband\ell\_{\mathrm{band}} as in ([5.2](https://arxiv.org/html/2512.01967v1#Ch5.E2 "Equation 5.2 ‣ 5.1 Loss components and their roles ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")).
Then y^↦ℓband​(y^;b,a)\hat{y}\mapsto\ell\_{\mathrm{band}}(\hat{y};b,a) is a convex function on ℝ\mathbb{R}.
Consequently, for any μ≥0\mu\geq 0, any weight matrix W⪰0W\succeq 0, design matrix
A∈ℝN×PA\in\mathbb{R}^{N\times P} and vector y∈ℝNy\in\mathbb{R}^{N}, the loss

|  |  |  |
| --- | --- | --- |
|  | ℒfit​(a)=12​‖W1/2​(A​a−y)‖22+μ​∑i=1Nℓband​((A​a)i;bi,ai)\mathcal{L}\_{\mathrm{fit}}(a)=\frac{1}{2}\big\|W^{1/2}(Aa-y)\big\|\_{2}^{2}+\mu\sum\_{i=1}^{N}\ell\_{\mathrm{band}}\big((Aa)\_{i};b\_{i},a\_{i}\big) |  |

is convex in a∈ℝPa\in\mathbb{R}^{P}.

###### Proof.

Write

|  |  |  |
| --- | --- | --- |
|  | ℓband(y^;b,a)=12(max{b−y^,0}2+max{y^−a,0}2).\ell\_{\mathrm{band}}(\hat{y};b,a)=\frac{1}{2}\Big(\max\{b-\hat{y},0\}^{2}+\max\{\hat{y}-a,0\}^{2}\Big). |  |

Each map y^↦b−y^\hat{y}\mapsto b-\hat{y} and y^↦y^−a\hat{y}\mapsto\hat{y}-a is affine, hence convex.
The hinge map t↦max⁡{t,0}t\mapsto\max\{t,0\} is convex as a pointwise maximum of two affine
functions (tt and 0). Therefore

|  |  |  |
| --- | --- | --- |
|  | y^↦max⁡{b−y^,0},y^↦max⁡{y^−a,0}\hat{y}\mapsto\max\{b-\hat{y},0\},\qquad\hat{y}\mapsto\max\{\hat{y}-a,0\} |  |

are convex functions. Moreover, both are nonnegative.

The square map s↦s2s\mapsto s^{2} is convex and nondecreasing on [0,∞)[0,\infty).
The composition of a convex, nondecreasing function with a convex, nonnegative
function is convex. Hence

|  |  |  |
| --- | --- | --- |
|  | y^↦max{b−y^,0}2,y^↦max{y^−a,0}2\hat{y}\mapsto\max\{b-\hat{y},0\}^{2},\qquad\hat{y}\mapsto\max\{\hat{y}-a,0\}^{2} |  |

are convex, and so is their sum. Multiplication by 12>0\tfrac{1}{2}>0 preserves convexity,
therefore ℓband​(⋅;b,a)\ell\_{\mathrm{band}}(\cdot;b,a) is convex.

For the second claim, the map a↦A​a−ya\mapsto Aa-y is affine, W1/2W^{1/2} is linear, and
f​(z)=12​‖z‖22f(z)=\tfrac{1}{2}\|z\|\_{2}^{2} is convex; the composition a↦f​(W1/2​(A​a−y))a\mapsto f\big(W^{1/2}(Aa-y)\big)
is therefore convex. We also have just shown that y^↦ℓband​(y^;bi,ai)\hat{y}\mapsto\ell\_{\mathrm{band}}(\hat{y};b\_{i},a\_{i})
is convex for each ii. Composition with the affine map a↦(A​a)ia\mapsto(Aa)\_{i} preserves
convexity, so a↦ℓband​((A​a)i;bi,ai)a\mapsto\ell\_{\mathrm{band}}\big((Aa)\_{i};b\_{i},a\_{i}\big) is convex for all ii.
Summation over ii and scaling by μ≥0\mu\geq 0 preserve convexity. Adding the two convex
terms yields that ℒfit\mathcal{L}\_{\mathrm{fit}} is convex in aa.
∎

###### Remark 8 (Optional dead–zone/margin).

To avoid hugging the band edges, one may widen the interior by a margin δi≥0\delta\_{i}\geq 0 and
replace [bi,ai][b\_{i},a\_{i}] with [bi+δi,ai−δi][b\_{i}+\delta\_{i},a\_{i}-\delta\_{i}] in ([5.2](https://arxiv.org/html/2512.01967v1#Ch5.E2 "Equation 5.2 ‣ 5.1 Loss components and their roles ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). All results below are unchanged.

### 5.2  Quadratic–program form via auxiliary slacks

While ([5.1](https://arxiv.org/html/2512.01967v1#Ch5.E1 "Equation 5.1 ‣ 5.1 Loss components and their roles ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) is already convex in aa, it is possible to cast it as a QP with *only* a quadratic
objective and linear constraints. Introduce non negative slacks (ui,vi)(u\_{i},v\_{i}) per quote:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓband​(y^;b,a)=minu,v≥0⁡12​(u2+v2)s.t.u≥b−y^,v≥y^−a.\ell\_{\text{band}}(\hat{y};b,a)\;=\;\min\_{u,v\geq 0}\ \frac{1}{2}(u^{2}+v^{2})\quad\text{s.t.}\quad u\geq b-\hat{y},\ \ v\geq\hat{y}-a. |  | (5.3) |

###### Lemma 2 (Exact equivalence of ([5.2](https://arxiv.org/html/2512.01967v1#Ch5.E2 "Equation 5.2 ‣ 5.1 Loss components and their roles ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) and ([5.3](https://arxiv.org/html/2512.01967v1#Ch5.E3 "Equation 5.3 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))).

For any b≤ab\leq a and any y^∈ℝ\hat{y}\in\mathbb{R}, the optimal slacks in ([5.3](https://arxiv.org/html/2512.01967v1#Ch5.E3 "Equation 5.3 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) are
u⋆=(b−y^)+u^{\star}=(b-\hat{y})\_{+} and v⋆=(y^−a)+v^{\star}=(\hat{y}-a)\_{+}, and the optimal value equals
12​[(b−y^)+2+(y^−a)+2]=ℓband​(y^;b,a)\tfrac{1}{2}[(b-\hat{y})\_{+}^{2}+(\hat{y}-a)\_{+}^{2}]=\ell\_{\text{band}}(\hat{y};b,a).

###### Proof.

If y^∈[b,a]\hat{y}\in[b,a], feasibility with u=v=0u=v=0 gives value 0; nonnegativity enforces u=v=0u=v=0 at optimum.
If y^<b\hat{y}<b, the constraints reduce to u≥b−y^>0u\geq b-\hat{y}>0 and v≥0v\geq 0, so the quadratic objective
is minimised at (u⋆,v⋆)=(b−y^,0)(u^{\star},v^{\star})=(b-\hat{y},0). The case y^>a\hat{y}>a is symmetric.
∎

Stacking ([5.3](https://arxiv.org/html/2512.01967v1#Ch5.E3 "Equation 5.3 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) over quotes yields the QP

|  |  |  |  |
| --- | --- | --- | --- |
|  | mina,u,v⁡12​‖W1/2​(A​a−y)‖22+μ2​(‖u‖22+‖v‖22)s.t.{u≥b−A​a,u≥0,v≥A​a−a,v≥0,\min\_{a,u,v}\ \frac{1}{2}\|W^{1/2}(Aa-y)\|\_{2}^{2}+\frac{\mu}{2}\big(\|u\|\_{2}^{2}+\|v\|\_{2}^{2}\big)\quad\text{s.t.}\quad\begin{cases}u\geq b-Aa,\ \ u\geq 0,\\ v\geq Aa-a,\ \ v\geq 0,\end{cases} |  | (5.4) |

where all inequalities are coordinate-wise.

###### Remark 9 (KKT and projection viewpoint).

At the solution of ([5.3](https://arxiv.org/html/2512.01967v1#Ch5.E3 "Equation 5.3 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) for a fixed y^\hat{y}, (u⋆,v⋆)(u^{\star},v^{\star}) is precisely the
vector of signed violations projected onto the nonnegative orthant; equivalently,
2​ℓband​(y^;b,a)=dist​(y^,[b,a])\sqrt{2\,\ell\_{\text{band}}(\hat{y};b,a)}=\mathrm{dist}(\hat{y},[b,a]).
Thus the second term in ([5.1](https://arxiv.org/html/2512.01967v1#Ch5.E1 "Equation 5.1 ‣ 5.1 Loss components and their roles ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) is μ2​‖dist​(A​a,[b,a])‖22\tfrac{\mu}{2}\|\mathrm{dist}(Aa,[b,a])\|\_{2}^{2} (coordinatewise distance).

#### Strict convexity and uniqueness of the data QP

###### Definition 3 (Positive definiteness on the span of AA).

We say that the quadratic form Q​(a)=12​a⊤​A⊤​W​A​aQ(a)=\tfrac{1}{2}\,a^{\top}A^{\top}WA\,a is *positive definite on the span of AA* if

|  |  |  |
| --- | --- | --- |
|  | a≠0​ and ​A​a≠0⟹a⊤​A⊤​W​A​a=(A​a)⊤​W​(A​a)>0.a\neq 0\ \text{ and }\ Aa\neq 0\quad\Longrightarrow\quad a^{\top}A^{\top}WA\,a=(Aa)^{\top}W(Aa)>0. |  |

In particular, QQ is strictly convex in the prediction variable p:=A​ap:=Aa, and in coefficient space its only flat directions are those in ker⁡(A)\ker(A): for each fixed pp the restriction of QQ to the affine fibre {a:A​a=p}\{a:\ Aa=p\} is constant.

###### Proposition 3 (Strict convexity ⇒\Rightarrow uniqueness).

Assume W≻0W\succ 0 (symmetric positive definite, ie xT​W​x>0x^{T}Wx>0 for every non-zero vector xx) and μ>0\mu>0. If A⊤​W​AA^{\top}WA is positive definite on the span of AA (in particular, if AA has full column rank), then the objective of ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) is strictly convex in (a,u,v)(a,u,v), and hence ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) has a unique optimiser (a⋆,u⋆,v⋆)(a^{\star},u^{\star},v^{\star}) whenever the feasible set is nonempty. Here and throughout, uniqueness is understood modulo the nullspace of AA: if AA is rank-deficient and (a1,u1,v1)(a\_{1},u\_{1},v\_{1}) and (a2,u2,v2)(a\_{2},u\_{2},v\_{2}) are both optimal solutions of ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), then A​a1=A​a2Aa\_{1}=Aa\_{2}, u1=u2u\_{1}=u\_{2}, v1=v2v\_{1}=v\_{2}, and a2−a1∈ker⁡(A)a\_{2}-a\_{1}\in\ker(A). Moreover, if a ridge term λ2​‖a‖22\tfrac{\lambda}{2}\|a\|\_{2}^{2} with λ>0\lambda>0 is added, the objective is strictly convex *unconditionally* (regardless of rank​(A)\mathrm{rank}(A)), yielding uniqueness of the optimiser.

###### Proof.

The slack QP has decision variables z=(a,u,v)z=(a,u,v) and objective

|  |  |  |
| --- | --- | --- |
|  | F​(a,u,v)=mina,u,v⁡12​‖W1/2​(A​a−y)‖22+μ2​(‖u‖22+‖v‖22)F(a,u,v)=\min\_{a,u,v}\ \frac{1}{2}\|W^{1/2}(Aa-y)\|\_{2}^{2}+\frac{\mu}{2}\big(\|u\|\_{2}^{2}+\|v\|\_{2}^{2}\big) |  |

Expanding the first term

|  |  |  |
| --- | --- | --- |
|  | 12​(A​a−y)⊤​W​(A​a−y)=12​a⊤​A⊤​W​A​a−y⊤​W​A​a+12​y⊤​W​y\frac{1}{2}(Aa-y)^{\top}W(Aa-y)=\frac{1}{2}a^{\top}A^{\top}WAa-y^{\top}WAa+\frac{1}{2}y^{\top}Wy |  |

Firstly we can see that 12​yT​W​y\frac{1}{2}y^{T}Wy does not depend on the decision variable, so it is a constant. A quadratic function can be written as:

|  |  |  |
| --- | --- | --- |
|  | q​(z)=12​z⊤​H​z+c⊤​z+c​o​n​s​t​a​n​tq(z)=\frac{1}{2}z^{\top}Hz+c^{\top}z+constant |  |

with HH symmetric. We can see from the expansion that F​(a,u,v)F(a,u,v) is a quadratic function of (a,u,v)(a,u,v) with Hessian

|  |  |  |
| --- | --- | --- |
|  | H=[A⊤​W​A000μ​I000μ​I].H\;=\;\begin{bmatrix}A^{\top}WA&0&0\\[2.0pt] 0&\mu I&0\\[2.0pt] 0&0&\mu I\end{bmatrix}. |  |

Also note that from the equation, the constant is 12​yT​W​y\frac{1}{2}y^{T}Wy and

|  |  |  |
| --- | --- | --- |
|  | C=[−A⊤​W​y00].C\;=\;\begin{bmatrix}-A^{\top}Wy\\[2.0pt] 0\\[2.0pt] 0\end{bmatrix}. |  |

Since μ>0\mu>0, the uu- and vv-blocks are positive definite (namely μ​I≻0\mu I\succ 0).

For the aa-block, take any direction δ​a∈ℝP\delta a\in\mathbb{R}^{P}, and define the prediction perturbation

|  |  |  |
| --- | --- | --- |
|  | δ​p=A​δ​a∈ℝN\delta p=A\delta a\in\mathbb{R}^{N} |  |

Then

|  |  |  |
| --- | --- | --- |
|  | δ​a⊤​A⊤​W​A​δ​a=(A​δ​a)⊤​W​(A​δ​a)=(δ​p)⊤​W​(δ​p)=‖δ​p‖W2,\delta a^{\top}A^{\top}WA\,\delta a=(A\delta a)^{\top}W(A\delta a)=(\delta p)^{\top}W(\delta p)=\|\delta p\|\_{W}^{2}, |  |

where ‖z‖W2:=z⊤​W​z\|z\|\_{W}^{2}:=z^{\top}Wz is the weighted Euclidean norm (since W≻0W\succ 0 it is in fact a norm. The interpretation is that curvature in the aa-block aling δ​a\delta a equals the weighted squared change in predictions produced by that δ​a\delta a:

* •

  If A​δ​a≠0A\delta a\neq 0, predictions move and the term is >0>0
* •

  If A​δ​a=0A\delta a=0, predictions don’t move and the term is =0=0

The set k​e​r​(A)={δ​a:A​δ​a=0}ker(A)=\{\delta a:A\delta a=0\} is the nullspace (directions in coefficient space that leave predictions unchanged).

By the assumption “positive definite on the span of AA”, ‖A​δ​a‖W2>0\|A\delta a\|\_{W}^{2}>0 for every δ​a\delta a with A​δ​a≠0A\delta a\neq 0; hence along any nonzero direction (δ​a,δ​u,δ​v)(\delta a,\delta u,\delta v) with (δ​u,δ​v)≠0(\delta u,\delta v)\neq 0 or A​δ​a≠0A\delta a\neq 0 we have

|  |  |  |
| --- | --- | --- |
|  | (δ​a,δ​u,δ​v)⊤​H​(δ​a,δ​u,δ​v)=‖A​δ​a‖W2+μ​‖δ​u‖22+μ​‖δ​v‖22> 0.(\delta a,\delta u,\delta v)^{\top}H\,(\delta a,\delta u,\delta v)=\|A\delta a\|\_{W}^{2}+\mu\|\delta u\|\_{2}^{2}+\mu\|\delta v\|\_{2}^{2}\;>\;0. |  |

Thus the objective is strictly convex on ℝP×ℝN×ℝN\mathbb{R}^{P}\times\mathbb{R}^{N}\times\mathbb{R}^{N} modulo the trivial flat directions δ​a∈ker⁡(A)\delta a\in\ker(A) with δ​u=δ​v=0\delta u=\delta v=0. If AA has full column rank, ker⁡(A)={0}\ker(A)=\{0\} and H≻0H\succ 0, so the objective is strictly convex in (a,u,v)(a,u,v). A strictly convex objective over a convex (polyhedral) feasible set admits at most one minimiser; feasibility of ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) then yields uniqueness.

If a ridge term λ2​‖a‖22\tfrac{\lambda}{2}\|a\|\_{2}^{2} with λ>0\lambda>0 is added, the Hessian becomes

|  |  |  |
| --- | --- | --- |
|  | Hλ=[A⊤​W​A+λ​I000μ​I000μ​I]≻ 0,H\_{\lambda}\;=\;\begin{bmatrix}A^{\top}WA+\lambda I&0&0\\[2.0pt] 0&\mu I&0\\[2.0pt] 0&0&\mu I\end{bmatrix}\ \succ\ 0, |  |

which is positive definite regardless of rank​(A)\mathrm{rank}(A), hence the objective is strictly convex in (a,u,v)(a,u,v) and the minimiser is unique.
∎

###### Remark 10 (What is unique when AA is rank-deficient).

If AA is rank-deficient and no ridge is used, the objective is strictly convex in the *predictions* p:=A​ap:=Aa and in (u,v)(u,v), but flat along ker⁡(A)\ker(A). Consequently, the optimiser’s predictions p⋆=A​a⋆p^{\star}=Aa^{\star} and slacks (u⋆,v⋆)(u^{\star},v^{\star}) are unique, while a⋆a^{\star} is unique only up to additions by vectors in ker⁡(A)\ker(A). Adding a small ridge fixes a⋆a^{\star} uniquely.

### 5.3  Weights, units, and invariance

The choice wi∝(ai−bi)−2w\_{i}\propto(a\_{i}-b\_{i})^{-2} makes the mid–squared error scale–free with respect to the
local band width; and the multiplicative factor liqi\mathrm{liq}\_{i} up-weights more reliable quotes. The hinge
term already measures squared band distance, so μ\mu is dimensionless. If one rescales all prices by a
factor c>0c>0, then A←c​AA\!\leftarrow cA, y←c​yy\!\leftarrow cy, b←c​bb\!\leftarrow cb, a←c​aa\!\leftarrow ca; the minimiser of ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))
is unchanged after dividing μ\mu by c2c^{2} and multiplying WW by c−2c^{-2}—this is the standard
homogeneity of quadratic objectives.

### 5.4  Binned variant (optional)

To stabilise sparse regions, let G∈{0,1}B×NG\in\{0,1\}^{B\times N} be a selector that sums quotes in (m,τ)(m,\tau) bins.
Replacing per–quote hinge terms by binned terms yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1Nℓband​((A​a)i;bi,ai)↝∑b=1Bℓband​((G​A​a)b;(G​b)b,(G​a)b),\sum\_{i=1}^{N}\ell\_{\text{band}}\big((Aa)\_{i};b\_{i},a\_{i}\big)\;\leadsto\;\sum\_{b=1}^{B}\ell\_{\text{band}}\Big((GAa)\_{b};\ (Gb)\_{b},\ (Ga)\_{b}\Big), |  | (5.5) |

which is still a QP by Lemma [2](https://arxiv.org/html/2512.01967v1#Thmlemma2 "Lemma 2 (Exact equivalence of (5.2) and (5.3)). ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), with slacks now attached to bins. The binned form
penalises average violations in each cell and reduces sensitivity to isolated outliers.

### 5.5  Feasibility and the role of μ\mu

Let 𝒮band={a∈ℝP:b≤A​a≤a}\mathcal{S}\_{\text{band}}=\{a\in\mathbb{R}^{P}:\ b\leq Aa\leq a\} be the band–feasible set (coordinate-wise).

* •

  If 𝒮band≠∅\mathcal{S}\_{\text{band}}\neq\emptyset and other constraints (no–arb penalties or hard
  inequalities) admit a feasible intersection, then taking μ→∞\mu\to\infty in ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))
  forces A​aAa into the band while the WLS term selects the point closest to yy among the band–feasible reconstructions.
* •

  If the intersection is empty, ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) finds the unique pair (a,u,v)(a,u,v) that minimises the
  ℓ2\ell\_{2}–distance of A​aAa to the rectangle [b,a][b,a] while trading off the mid anchor through WW.

###### Remark 11 (Targeting coverage).

Define coverage(a)=1N​∑i𝟏​{bi≤(A​a)i≤ai}(a)=\frac{1}{N}\sum\_{i}\mathbf{1}\{b\_{i}\leq(Aa)\_{i}\leq a\_{i}\}. Increasing μ\mu reduces hinge violations and typically (empirically) increases coverage; we adjust μ\mu with a short controller to hit a target coverage level. Formal monotonicity in μ\mu is not required for the optimiser or the QP structure.

### 5.6  What is used in this paper (precise choices)

1. 1.

   Forward–discounted bands and mids: (bi,ai,yi)(b\_{i},a\_{i},y\_{i}) constructed at each quote and robustly cleaned so 0≤bi≤ai0\leq b\_{i}\leq a\_{i}.
2. 2.

   Weights: wi=liqi/max(ai−bi,ε)2w\_{i}=\mathrm{liq}\_{i}/\max(a\_{i}-b\_{i},\varepsilon)^{2} with ε\varepsilon a small fixed floor; W=diag⁡(w)W=\operatorname{diag}(w).
3. 3.

   Band hinge: quadratic ℓband\ell\_{\text{band}} as in ([5.2](https://arxiv.org/html/2512.01967v1#Ch5.E2 "Equation 5.2 ‣ 5.1 Loss components and their roles ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")); no interior margin unless stated (set δi=0\delta\_{i}=0 by default).
4. 4.

   QP form: auxiliary slacks (u,v)≥0(u,v)\geq 0 with linear constraints ([5.4](https://arxiv.org/html/2512.01967v1#Ch5.E4 "Equation 5.4 ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), solved jointly with the rest of the QP (ridge, no–arb penalties, etc.).
5. 5.

   Optional binning: GG–aggregation in ([5.5](https://arxiv.org/html/2512.01967v1#Ch5.E5 "Equation 5.5 ‣ 5.4 Binned variant (optional) ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) enabled on sparse books; otherwise per–quote hinge.
6. 6.

   Controller for μ\mu: simple scheduler that increases μ\mu until the observed coverage reaches the target (with caps); WLS weight WW is held fixed across the schedule.

## 6.  Ridge, spectral geometry, and transport regularisation

This chapter specifies the quadratic regularisers added to the objective, and the
price invariant reparameterisation used to improve conditioning. Every term below is a
fixed quadratic form in the coefficient vector a∈ℝPa\in\mathbb{R}^{P} (or in a linear reparameterisation
a~\tilde{a}), so the overall problem remains a convex QP.

### 6.1  Spectral ridge (modal energy control)

Let the tensor index be (k,ℓ)(k,\ell) with k=0,…,Kk=0,\dots,K (log–moneyness) and ℓ=0,…,L\ell=0,\dots,L
(maturity). Define a diagonal weight

|  |  |  |
| --- | --- | --- |
|  | Λ(k,ℓ),(k,ℓ)=(1+α​k2+β​ℓ2)s,α,β>0,s>0,\Lambda\_{(k,\ell),(k,\ell)}\;=\;\big(1+\alpha\,k^{2}+\beta\,\ell^{2}\big)^{\,s},\qquad\alpha,\beta>0,\ s>0, |  |

and set Λ=diag⁡(Λ(k,ℓ),(k,ℓ))∈ℝP×P\Lambda=\operatorname{diag}(\Lambda\_{(k,\ell),(k,\ell)})\in\mathbb{R}^{P\times P} with P=(K+1)​(L+1)P=(K{+}1)(L{+}1).
The spectral ridge is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛridge​(a)=λridge2​‖Λ1/2​a‖22=λridge2​a⊤​Λ​a=λridge2​∑k=0K∑l=0L(1+α​k2+β​ℓ2)s​ak​l2.\mathcal{R}\_{\mathrm{ridge}}(a)\;=\;\frac{\lambda\_{\mathrm{ridge}}}{2}\,\|\Lambda^{1/2}a\|\_{2}^{2}\;=\;\frac{\lambda\_{\mathrm{ridge}}}{2}\,a^{\top}\Lambda a\;=\;\frac{\lambda\_{\mathrm{ridge}}}{2}\sum\_{k=0}^{K}\sum\_{l=0}^{L}(1+\alpha\,k^{2}+\beta\,\ell^{2}\big)^{\,s}a\_{kl}^{2}. |  | (6.1) |

##### Interpretation:

Each coefficient is penalised by a weight that grows with its modal index. Low modes (small kk and ll) get weight ≈1\approx 1; higher (k,ℓ)(k,\ell) modes carry larger weights (are expensive). α,β\alpha,\beta tune the relative penalisation across mm vs. τ\tau, and ss controls the growth rate (asymptotically the weights grow like (α​k2+β​ℓ2)s(\alpha k^{2}+\beta\ell^{2})^{s}, so s=1s=1 gives quadratic growth in the indices and s=2s=2 gives quartic growth). This damps high–frequency oscillations while leaving low modes essentially unchanged. In spectral methods, smooth functions have rapidly decaying coefficients and non-smooth noisy features push energy into high indices. Penalising ak​l2a\_{kl}^{2} with a weight increasing in k,lk,l is the discrete analogue of a Sobolev HsH^{s} seminorm, suppressing high frequency components components while leaving low modes mostly alone. The wraps Φm\Phi\_{m} and Φτ\Phi\_{\tau} mean smoothness is enforced in the wrapped coordinates where the basis is well-conditioned (ATM focus and short-τ\tau density).

Unless otherwise stated, we fix α=β=1\alpha=\beta=1 and s=2s=2. The scalar
λridge\lambda\_{\mathrm{ridge}} is chosen once per date by a small-subsample generalised
cross–validation (GCV) pass on the *linear* WLS subproblem. Build AsubA\_{\mathrm{sub}} and WsubW\_{\mathrm{sub}} on a random 8%8\% subset of quotes. Namely As​u​b∈ℝNs​u​b×PA\_{sub}\in\mathbb{R}^{N\_{sub}\times P}, Ws​u​b=d​i​a​g​(ws​u​b)≻0W\_{sub}=diag(w\_{sub})\succ 0 and ys​u​b∈ℝNs​u​by\_{sub}\in\mathbb{R}^{N\_{sub}}. For any λ>0\lambda>0, solve the ridge-regularised weighted least squares:

|  |  |  |
| --- | --- | --- |
|  | mina⁡12​‖Wsub1/2​(Asub​a−ysub)‖22+λ2​‖Λ1/2​a‖22,\min\_{a}\;\frac{1}{2}\|W\_{\mathrm{sub}}^{1/2}(A\_{\mathrm{sub}}a-y\_{\mathrm{sub}})\|\_{2}^{2}+\frac{\lambda}{2}\|\Lambda^{1/2}a\|\_{2}^{2}, |  |

This has the closed form

|  |  |  |
| --- | --- | --- |
|  | a​(λ)=(Asub⊤​Wsub​Asub+λ​Λ)−1​Asub⊤​Wsub​ysuba(\lambda)=(A\_{\mathrm{sub}}^{\top}W\_{\mathrm{sub}}A\_{\mathrm{sub}}+\lambda\Lambda)^{-1}A\_{\mathrm{sub}}^{\top}W\_{\mathrm{sub}}y\_{\mathrm{sub}} |  |

Define the weighted residual and the hat matrix

|  |  |  |
| --- | --- | --- |
|  | r​(λ)=Wsub1/2​(Asub​a​(λ)−ysub);H​(λ)=Wsub1/2​Asub​(Asub⊤​Wsub​Asub+λ​Λ)−1​Asub⊤​Wsub1/2.r(\lambda)=W\_{\mathrm{sub}}^{1/2}(A\_{\mathrm{sub}}a(\lambda)-y\_{\mathrm{sub}});\quad H(\lambda)=W\_{\mathrm{sub}}^{1/2}A\_{\mathrm{sub}}(A\_{\mathrm{sub}}^{\top}W\_{\mathrm{sub}}A\_{\mathrm{sub}}+\lambda\Lambda)^{-1}A\_{\mathrm{sub}}^{\top}W\_{\mathrm{sub}}^{1/2}. |  |

###### Remark 12.

A useful identity for computation is

|  |  |  |
| --- | --- | --- |
|  | t​r​(H​(λ))=t​r​(S​G​(λ)−1),S=(Asub⊤​Wsub​Asub),G​(λ)=S+λ​Λ.tr(H(\lambda))=tr\left(SG(\lambda)^{-1}\right),\quad S=(A\_{\mathrm{sub}}^{\top}W\_{\mathrm{sub}}A\_{\mathrm{sub}}),\quad G(\lambda)=S+\lambda\Lambda. |  |

We compute the GCV (Generalised cross-validation) score

|  |  |  |
| --- | --- | --- |
|  | GCV​(λ)=‖r​(λ)‖22(Nsub−tr​H​(λ))2.\mathrm{GCV}(\lambda)=\frac{\|r(\lambda)\|\_{2}^{2}}{\big(N\_{\mathrm{sub}}-\mathrm{tr}\,H(\lambda)\big)^{2}}. |  |

Choose
λridge=arg⁡minλ⁡GCV​(λ)\lambda\_{\mathrm{ridge}}=\arg\min\_{\lambda}\mathrm{GCV}(\lambda) and use it in the full QP.

###### Lemma 3 (Spectral ridge is a fixed quadratic form).

Fix the tensor grid (k,ℓ)(k,\ell) with k=0,…,Kk=0,\dots,K, ℓ=0,…,L\ell=0,\dots,L, and
hyperparameters α,β>0\alpha,\beta>0, s>0s>0. Let Λ∈ℝP×P\Lambda\in\mathbb{R}^{P\times P},
P=(K+1)​(L+1)P=(K{+}1)(L{+}1), be the diagonal matrix defined above and let
λridge≥0\lambda\_{\mathrm{ridge}}\geq 0 be fixed. Then for every a∈ℝPa\in\mathbb{R}^{P},
the spectral ridge ([6.1](https://arxiv.org/html/2512.01967v1#Ch6.E1 "Equation 6.1 ‣ 6.1 Spectral ridge (modal energy control) ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) can be written as

|  |  |  |
| --- | --- | --- |
|  | ℛridge​(a)=12​a⊤​Qridge​a,Qridge:=λridge​Λ,\mathcal{R}\_{\mathrm{ridge}}(a)\;=\;\frac{1}{2}\,a^{\top}Q\_{\mathrm{ridge}}a,\qquad Q\_{\mathrm{ridge}}:=\lambda\_{\mathrm{ridge}}\,\Lambda, |  |

with QridgeQ\_{\mathrm{ridge}} symmetric positive semidefinite and independent of aa.
In particular, ℛridge\mathcal{R}\_{\mathrm{ridge}} is a convex quadratic function of
the coefficient vector aa, and enters any optimisation problem as a fixed
quadratic form (for given (α,β,s)(\alpha,\beta,s) and λridge\lambda\_{\mathrm{ridge}}).

###### Proof.

By definition,

|  |  |  |
| --- | --- | --- |
|  | Λ(k,ℓ),(k,ℓ)=(1+α​k2+β​ℓ2)s>0for all ​0≤k≤K, 0≤ℓ≤L,\Lambda\_{(k,\ell),(k,\ell)}=\bigl(1+\alpha k^{2}+\beta\ell^{2}\bigr)^{s}>0\quad\text{for all }0\leq k\leq K,\ 0\leq\ell\leq L, |  |

so Λ\Lambda is diagonal with strictly positive diagonal entries and hence
Λ⪰0\Lambda\succeq 0 (indeed Λ≻0\Lambda\succ 0). For any a∈ℝPa\in\mathbb{R}^{P},

|  |  |  |
| --- | --- | --- |
|  | ‖Λ1/2​a‖22=a⊤​Λ1/2​Λ1/2​a=a⊤​Λ​a.\|\Lambda^{1/2}a\|\_{2}^{2}=a^{\top}\Lambda^{1/2}\Lambda^{1/2}a=a^{\top}\Lambda a. |  |

Thus ([6.1](https://arxiv.org/html/2512.01967v1#Ch6.E1 "Equation 6.1 ‣ 6.1 Spectral ridge (modal energy control) ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | ℛridge​(a)=λridge2​a⊤​Λ​a=12​a⊤​Qridge​a,Qridge:=λridge​Λ.\mathcal{R}\_{\mathrm{ridge}}(a)=\frac{\lambda\_{\mathrm{ridge}}}{2}\,a^{\top}\Lambda a=\frac{1}{2}\,a^{\top}Q\_{\mathrm{ridge}}a,\qquad Q\_{\mathrm{ridge}}:=\lambda\_{\mathrm{ridge}}\Lambda. |  |

The matrix QridgeQ\_{\mathrm{ridge}} is symmetric. Since λridge≥0\lambda\_{\mathrm{ridge}}\geq 0
and Λ⪰0\Lambda\succeq 0, we have Qridge⪰0Q\_{\mathrm{ridge}}\succeq 0, so the map
a↦12​a⊤​Qridge​aa\mapsto\tfrac{1}{2}a^{\top}Q\_{\mathrm{ridge}}a is a convex quadratic function.
For fixed hyperparameters (α,β,s)(\alpha,\beta,s), grid sizes (K,L)(K,L), and a chosen
value of λridge\lambda\_{\mathrm{ridge}}, the matrix QridgeQ\_{\mathrm{ridge}} is completely
determined and does not depend on aa. Hence ℛridge\mathcal{R}\_{\mathrm{ridge}} is a
fixed quadratic form in the coefficient vector.
∎

### 6.2  Λ\Lambda–module: price–invariant reparameterisation

Now propose a change of coordinates in the coefficient space to make the optimisation numerically well-behaved. Since the variables and matrices are changed in a consistent way, all prices and constraint values stay identical, and the conditioning of the problem improves.

Let U∈ℝP×PU\in\mathbb{R}^{P\times P} be a fixed, invertible linear map. Define new coefficients
a~:=U−1​a\tilde{a}:=U^{-1}a and replace every block by post–multiplication with UU:

|  |  |  |
| --- | --- | --- |
|  | A←A​U,Am←Am​U,Am​m←Am​m​U,Aτ←Aτ​U,etc.A\leftarrow AU,\quad A\_{m}\leftarrow A\_{m}U,\quad A\_{mm}\leftarrow A\_{mm}U,\quad A\_{\tau}\leftarrow A\_{\tau}U,\quad\text{etc.} |  |

Predictions are unchanged: (A​U)​a~=A​(U​a~)=A​a(AU)\tilde{a}=A(U\tilde{a})=Aa. The ridge becomes

|  |  |  |
| --- | --- | --- |
|  | ℛridge​(a)=λridge2​‖Λ1/2​U​a~‖22=λridge2​a~⊤​U⊤​Λ​U⏟Λ~​a~,\mathcal{R}\_{\mathrm{ridge}}(a)=\frac{\lambda\_{\mathrm{ridge}}}{2}\,\|\Lambda^{1/2}U\tilde{a}\|\_{2}^{2}=\frac{\lambda\_{\mathrm{ridge}}}{2}\,\tilde{a}^{\top}\underbrace{U^{\top}\Lambda U}\_{\widetilde{\Lambda}}\,\tilde{a}, |  |

i.e. the same quadratic form in a~\tilde{a} with Λ~=U⊤​Λ​U\widetilde{\Lambda}=U^{\top}\Lambda U.

##### Blockwise whitening and why it is safe:

Firstly, partition columns by maturity slice ℓ\ell (all mm–modes for that ℓ\ell) and define the sets {𝒢ℓ}\{\mathcal{G}\_{\ell}\}.
Then for each block form the *weighted* thin QR

|  |  |  |
| --- | --- | --- |
|  | W1/2​A[:,𝒢ℓ]=Qℓ​Rℓ,Qℓ⊤​Qℓ=I,Rℓ​ invertible upper–triangular,W^{1/2}A\_{[:,\mathcal{G}\_{\ell}]}\;=\;Q\_{\ell}R\_{\ell},\qquad Q\_{\ell}^{\top}Q\_{\ell}=I,\ R\_{\ell}\text{ invertible upper–triangular}, |  |

and assemble a block–diagonal UU with U𝒢ℓ,𝒢ℓ:=Rℓ−1U\_{\mathcal{G}\_{\ell},\mathcal{G}\_{\ell}}:=R\_{\ell}^{-1} (zeros off–block). Optionally, right–scale
columns so ‖W1/2​(A​U)[:,j]‖2=1\|W^{1/2}(AU)\_{[:,j]}\|\_{2}=1 by replacing U←U​D−1U\leftarrow UD^{-1} with D=diag⁡(dj)D=\operatorname{diag}(d\_{j}), dj=‖W1/2​(A​U)[:,j]‖2d\_{j}=\|W^{1/2}(AU)\_{[:,j]}\|\_{2}.

We implicitly require that each slice A​[:,Gℓ]A[:,G\_{\ell}] have full column rank under the
WW–inner product, so that the thin QR factorisation with a square, invertible
RℓR\_{\ell} exists. This condition is satisfied for the Chebyshev grids used in our
experiments; in degenerate cases one can replace Rℓ−1R\_{\ell}^{-1} by a pseudo–inverse
obtained from a rank–revealing QR or SVD, at the price of a slightly lower–dimensional
reparameterisation.

###### Proposition 4 (W–orthonormality within slices).

With UU defined above,

|  |  |  |
| --- | --- | --- |
|  | (A​U)[:,𝒢ℓ]=W−1/2​Qℓ⟹(A​U)[:,𝒢ℓ]⊤​W​(A​U)[:,𝒢ℓ]=I|𝒢ℓ|.(AU)\_{[:,\mathcal{G}\_{\ell}]}\;=\;W^{-1/2}Q\_{\ell}\quad\Longrightarrow\quad(AU)\_{[:,\mathcal{G}\_{\ell}]}^{\top}W\,(AU)\_{[:,\mathcal{G}\_{\ell}]}\;=\;I\_{|\mathcal{G}\_{\ell}|}. |  |

In particular, the WLS normal matrix becomes block–identity within each slice (collinearity removed).

###### Proof.

A[:,𝒢ℓ]=W−1/2​Qℓ​RℓA\_{[:,\mathcal{G}\_{\ell}]}=W^{-1/2}Q\_{\ell}R\_{\ell} and U𝒢ℓ,𝒢ℓ=Rℓ−1U\_{\mathcal{G}\_{\ell},\mathcal{G}\_{\ell}}=R\_{\ell}^{-1} give
(A​U)[:,𝒢ℓ]=W−1/2​Qℓ(AU)\_{[:,\mathcal{G}\_{\ell}]}=W^{-1/2}Q\_{\ell}.

Hence (A​U)[:,𝒢ℓ]⊤​W​(A​U)[:,𝒢ℓ]=Qℓ⊤​Qℓ=I(AU)\_{[:,\mathcal{G}\_{\ell}]}^{\top}W(AU)\_{[:,\mathcal{G}\_{\ell}]}=Q\_{\ell}^{\top}Q\_{\ell}=I.
∎

###### Proposition 5 (Price/constraint invariance).

Let a~=U−1​a\tilde{a}=U^{-1}a, A′:=A​UA^{\prime}:=AU, and for any block A∙A\_{\bullet} set A∙′:=A∙​UA\_{\bullet}^{\prime}:=A\_{\bullet}U. Then

|  |  |  |
| --- | --- | --- |
|  | A′​a~=A​a,A∙′​a~=A∙​a.A^{\prime}\tilde{a}=Aa,\qquad A\_{\bullet}^{\prime}\tilde{a}=A\_{\bullet}a. |  |

Consequently, hard inequalities A∙​a≤0A\_{\bullet}a\leq 0 are equivalent to (A∙​U)​a~≤0(A\_{\bullet}U)\tilde{a}\leq 0, and soft penalties that depend on A∙​aA\_{\bullet}a take the same values when written in a~\tilde{a}.

###### Proof.

We see by definition of A′A^{\prime} and a~\tilde{a}, A′​a~=A​U​U−1​a=A​aA^{\prime}\tilde{a}=AUU^{-1}a=Aa as required.
∎

###### Proposition 6 (Ridge congruence).

For any symmetric Q⪰0Q\succeq 0,

|  |  |  |
| --- | --- | --- |
|  | 12​a⊤​Q​a=12​a~⊤​(U⊤​Q​U)​a~.\frac{1}{2}\,a^{\top}Qa\;=\;\frac{1}{2}\,\tilde{a}^{\top}(U^{\top}QU)\,\tilde{a}. |  |

In particular, the spectral ridge becomes λridge2​a~⊤​Λ~​a~\frac{\lambda\_{\mathrm{ridge}}}{2}\,\tilde{a}^{\top}\widetilde{\Lambda}\,\tilde{a}
with Λ~:=U⊤​Λ​U⪰0\widetilde{\Lambda}:=U^{\top}\Lambda U\succeq 0.

###### Proof.

Substitute a=U​a~a=U\tilde{a} and regroup; congruence preserves positive semidefiniteness.
∎

###### Remark 13 (Global whitening as a special case).

If one QR–factorises W1/2​A=Q​RW^{1/2}A=QR once and sets U=R−1U=R^{-1}, then (A​U)⊤​W​(A​U)=IP(AU)^{\top}W(AU)=I\_{P} (full whitening); the blockwise construction above is its per–slice counterpart.

### 6.3  DW–module: discrete transport (H−1H^{-1}) smoothing of density

This section penalises oscillations of the risk-neutral density ρ\rho along mm by measuring how much potential ϕ\phi is needed so its discrete derivative matches ρ\rho. High frequency wiggles are expensive and slowly varying shapes cost little.

Let ρ=∂K​KCf\rho=\partial\_{KK}C\_{f} denote the risk–neutral density. On each maturity slice
τ=τg\tau=\tau\_{g}, we discretise the mm–axis on the collocation nodes mjm\_{j} and build:

* •

  a diagonal mass matrix Mm=diag⁡(w(m))M\_{m}=\operatorname{diag}(w^{(m)}) with Gauss–Lobatto (Chebyshev) quadrature weights.
* •

  a first–difference matrix Dm∈ℝ(Mm−1)×MmD\_{m}\in\mathbb{R}^{(M\_{m}-1)\times M\_{m}} (forward differences with
  homogeneous Neumann boundary, i.e. zero–flux ends) with (Dm​ϕ)i=ϕi+1−ϕi(D\_{m}\phi)\_{i}=\phi\_{i+1}-\phi\_{i} for i=1,…,Mm−1i=1,...,M\_{m}-1.

Define the discrete Neumann Laplacian in mm by

|  |  |  |
| --- | --- | --- |
|  | Lm:=Dm⊤​Mm−1​Dm∈ℝMm×Mm.L\_{m}\;:=\;D\_{m}^{\top}M\_{m}^{-1}D\_{m}\;\in\;\mathbb{R}^{M\_{m}\times M\_{m}}. |  |

LmL\_{m} is symmetric positive semidefinite and its nullspace is the span of the constant vector
(along each slice). For a discrete function f∈ℝMmf\in\mathbb{R}^{M\_{m}}, the discrete H−1​(m)H^{-1}(m)
seminorm is defined by

|  |  |  |
| --- | --- | --- |
|  | ‖f‖H−1​(m)2:=f⊤​Lm+⏟Moore–Penrose pseudoinverse of ​Lm​f,\|f\|\_{H^{-1}(m)}^{2}\;:=\;f^{\top}\underbrace{L\_{m}^{+}}\_{\text{Moore--Penrose pseudoinverse of }L\_{m}}f, |  |

where + is the Moore–Penrose pseudoinverse on the range.
This is the standard discrete Neumann H−1H^{-1} seminorm: Lm+L\_{m}^{+} plays the role of
the inverse Laplacian, so only the mean–zero component of ff is penalised and the
constant/mean mode lies in the nullspace.

Assemble the full grid operator
L+=blkdiag​(Lm+,…,Lm+)L^{+}=\mathrm{blkdiag}(L\_{m}^{+},\dots,L\_{m}^{+}) across slices and the sampling matrix
S:ℝG→ℝMm​(Mτ+1)S:\mathbb{R}^{G}\to\mathbb{R}^{M\_{m}(M\_{\tau}{+}1)} that reshapes grid values into slice stacks. With
E:=S​AK​K∈ℝMm​(Mτ+1)×PE:=S\,A\_{KK}\in\mathbb{R}^{M\_{m}(M\_{\tau}{+}1)\times P} (density map in slice–stacked order), the DW penalty is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛDW​(a)=λDW2​‖ρ​(a)‖H−12=λDW2​a⊤​E⊤​L+​E​a,\mathcal{R}\_{\mathrm{DW}}(a)\;=\;\frac{\lambda\_{\mathrm{DW}}}{2}\,\|\rho(a)\|\_{H^{-1}}^{2}\;=\;\frac{\lambda\_{\mathrm{DW}}}{2}\,a^{\top}E^{\top}L^{+}E\,a, |  | (6.2) |

a fixed quadratic form once L+L^{+} is precomputed (e.g. Cholesky on each LmL\_{m} on the
mean–zero subspace, plus a rank–1 fix for the constant nullspace).

In Fourier language, ‖f‖H−1​(m)2∼∑k|fk|2/k2\|f\|\_{H^{-1}(m)}^{2}\sim\sum\_{k}|f\_{k}|^{2}/k^{2}. The high kk content is amplified, so the optimiser prefers smooth densities. The constant/mean component sits in the nullspace and is not penalised. The constraint set continues to control positivity/monotonicity and DW just damps ripples that those constraints do not eliminate.

We apply ([6.2](https://arxiv.org/html/2512.01967v1#Ch6.E2 "Equation 6.2 ‣ 6.3 DW–module: discrete transport (𝐻⁻¹) smoothing of density ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) *along mm only* on each slice, with Neumann
boundaries and Chebyshev–Lobatto weights. The difference operator DmD\_{m} only takes
interior forward differences,

|  |  |  |
| --- | --- | --- |
|  | (Dm​ϕ)i=ϕi+1−ϕii=1,…,Mm−1,(D\_{m}\phi)\_{i}=\phi\_{i+1}-\phi\_{i}\qquad i=1,\dots,M\_{m}-1, |  |

so the associated Laplacian Lm=Dm⊤​Mm−1​DmL\_{m}=D\_{m}^{\top}M\_{m}^{-1}D\_{m} has the constant vector in
its nullspace: adding a constant to ϕ\phi does not change Dm​ϕD\_{m}\phi or the quadratic
form. In the H−1H^{-1} penalty, this means the mean component of ρ\rho is left
unpenalised and only fluctuations around the mean contribute to ‖ρ‖H−1\|\rho\|\_{H^{-1}};
this is the discrete zero–flux (Neumann) condition at the ends.

Equivalently, on each slice we can view ρ\rho as a one–dimensional “charge
distribution” along mm. The matrix LmL\_{m} is a discrete Neumann Laplacian on
the nodes, and Lm+L\_{m}^{+} acts as its inverse on mean–zero densities. For any
profile f∈ℝMmf\in\mathbb{R}^{M\_{m}} with zero MmM\_{m}–mean there exists a potential
ϕ\phi (unique up to an additive constant) solving the discrete Poisson problem

|  |  |  |
| --- | --- | --- |
|  | Lm​ϕ=f(Neumann in m).L\_{m}\phi=f\qquad\text{(Neumann in $m$)}. |  |

Among all such potentials, the one with the smallest discrete Dirichlet energy
ϕ⊤​Lm​ϕ\phi^{\top}L\_{m}\phi satisfies

|  |  |  |
| --- | --- | --- |
|  | ϕ⊤​Lm​ϕ=f⊤​Lm+​f=‖f‖H−1​(m)2.\phi^{\top}L\_{m}\phi\;=\;f^{\top}L\_{m}^{+}f\;=\;\|f\|\_{H^{-1}(m)}^{2}. |  |

So ‖f‖H−1​(m)2\|f\|\_{H^{-1}(m)}^{2} measures how much “bending” of the potential ϕ\phi
is needed to support the density: sharply oscillating ff requires a highly
curved potential and incurs a large penalty, while slowly varying ff can be
supported by a gentle potential and is cheap. The constant component of ff
generates no potential at all and is left unpenalised.

Chebyshev-Lobatto nodes cluster near the endpoints, and without quadrature weights, any discrete L2L^{2} inner product would outweigh the ends and underweight the middle. Mm=d​i​a​g​(w(m))M\_{m}=diag(w^{(m)}) fixes that. For a smooth function gg,

|  |  |  |
| --- | --- | --- |
|  | ∑j=1Mmwj(m)​g​(mj)≈∫mm​i​nmm​a​xg​(m)​𝑑m.\sum\_{j=1}^{M\_{m}}w\_{j}^{(m)}g(m\_{j})\approx\int\_{m\_{min}}^{m\_{max}}g(m)dm. |  |

So ϕ⊤​Mm​ϕ\phi^{\top}M\_{m}\phi is a proper discretisation of ∫ϕ​(m)2​𝑑m\int\phi(m)^{2}dm, independent of how densely sampled near the ends.
The weights are obtained using standard Clenshaw-Curtis (Gauss-Lobatto) quadrature on the Chebyshev-Lobatto nodes in the reference variable n∈[−1,1]n\in[-1,1] and then rescaled to m∈[mm​i​n,mm​a​x]m\in[m\_{min},m\_{max}].

If m=mm​a​x−mm​i​n2​n+mm​a​x+mm​i​n2m=\frac{m\_{max}-m\_{min}}{2}n+\frac{m\_{max}+m\_{min}}{2}, the Jacobian is constant and

|  |  |  |
| --- | --- | --- |
|  | wj(m)=mm​a​x−mm​i​n2​wj(n).w\_{j}^{(m)}=\frac{m\_{max}-m\_{min}}{2}w\_{j}^{(n)}. |  |

The weight is tapered in maturity:
λDW​(τg)=λDW(0)⋅min⁡{1,τ⋆/τg}\lambda\_{\mathrm{DW}}(\tau\_{g})=\lambda\_{\mathrm{DW}}^{(0)}\cdot\min\{1,\tau\_{\star}/\tau\_{g}\} to
dampen short maturity ripples; defaults τ⋆=5\tau\_{\star}=5 trading days. For τg≤τ∗\tau\_{g}\leq\tau\_{\*}, we use the full DW smoothing strength λDW(0)\lambda\_{\mathrm{DW}}^{(0)} and for τg>τ∗\tau\_{g}>\tau\_{\*} the smoothing weight decays like 1/τg1/\tau\_{g} so that the long end is not over-smoothed.

###### Lemma 4 (DW penalty as a fixed quadratic form).

Fix the grid operators

|  |  |  |
| --- | --- | --- |
|  | L+∈ℝMm​(Mτ+1)×Mm​(Mτ+1),E:=S​AK​K∈ℝMm​(Mτ+1)×P,L^{+}\in\mathbb{R}^{M\_{m}(M\_{\tau}+1)\times M\_{m}(M\_{\tau}+1)},\qquad E:=SA\_{KK}\in\mathbb{R}^{M\_{m}(M\_{\tau}+1)\times P}, |  |

as above, and let
λDW≥0\lambda\_{\mathrm{DW}}\geq 0 be given. Then for every a∈ℝPa\in\mathbb{R}^{P}, let

|  |  |  |
| --- | --- | --- |
|  | ℛDW​(a)=λDW2​‖ρ​(a)‖H−12=12​a⊤​QDW​a,QDW:=λDW​E⊤​L+​E,\mathcal{R}\_{\mathrm{DW}}(a)\;=\;\frac{\lambda\_{\mathrm{DW}}}{2}\,\|\rho(a)\|\_{H^{-1}}^{2}\;=\;\frac{1}{2}\,a^{\top}Q\_{\mathrm{DW}}a,\qquad Q\_{\mathrm{DW}}:=\lambda\_{\mathrm{DW}}\,E^{\top}L^{+}E, |  |

with QDWQ\_{\mathrm{DW}} symmetric positive semidefinite and independent of aa.
Then ℛDW\mathcal{R}\_{\mathrm{DW}} is a convex quadratic function of the
coefficient vector aa and enters the global problem as a fixed quadratic term,
so the formulation remains a convex QP.

###### Proof.

By construction, ρ​(a)\rho(a) is linear in aa: on the slice-stacked grid,
ρ​(a)=E​a\rho(a)=Ea with E=S​AK​KE=SA\_{KK} independent of aa. The discrete
H−1H^{-1} seminorm is

|  |  |  |
| --- | --- | --- |
|  | ‖ρ​(a)‖H−12=ρ​(a)⊤​L+​ρ​(a)=(E​a)⊤​L+​(E​a)=a⊤​E⊤​L+​E​a.\|\rho(a)\|\_{H^{-1}}^{2}=\rho(a)^{\top}L^{+}\rho(a)=(Ea)^{\top}L^{+}(Ea)=a^{\top}E^{\top}L^{+}Ea. |  |

Thus

|  |  |  |
| --- | --- | --- |
|  | ℛDW​(a)=λDW2​a⊤​E⊤​L+​E​a=12​a⊤​QDW​a\mathcal{R}\_{\mathrm{DW}}(a)=\frac{\lambda\_{\mathrm{DW}}}{2}\,a^{\top}E^{\top}L^{+}Ea=\frac{1}{2}\,a^{\top}Q\_{\mathrm{DW}}a |  |

with QDW:=λDW​E⊤​L+​EQ\_{\mathrm{DW}}:=\lambda\_{\mathrm{DW}}E^{\top}L^{+}E. The operator L+L^{+} is symmetric positive semidefinite by construction, as the
Moore–Penrose pseudoinverse of the symmetric positive semidefinite block–diagonal
matrix whose blocks are Lm=Dm⊤​Mm−1​DmL\_{m}=D\_{m}^{\top}M\_{m}^{-1}D\_{m}. Hence for any zz,
z⊤​L+​z≥0z^{\top}L^{+}z\geq 0 (by definition of symmetric positive semidefinite), and in particular

|  |  |  |
| --- | --- | --- |
|  | a⊤​QDW​a=λDW​(E​a)⊤​L+​(E​a)≥ 0a^{\top}Q\_{\mathrm{DW}}a=\lambda\_{\mathrm{DW}}(Ea)^{\top}L^{+}(Ea)\;\geq\;0 |  |

for all aa, so QDW⪰0Q\_{\mathrm{DW}}\succeq 0 whenever λDW≥0\lambda\_{\mathrm{DW}}\geq 0.
All ingredients (E,L+,λDW)(E,L^{+},\lambda\_{\mathrm{DW}}) are fixed once the grid,
quadrature, and smoothing weight are chosen, so QDWQ\_{\mathrm{DW}} does not
depend on aa. Therefore ℛDW\mathcal{R}\_{\mathrm{DW}} is a fixed convex
quadratic function of the coefficients.
∎

###### Remark 14 (Maturity taper).

If the smoothing weight is tapered in maturity, with slice weights
λDW​(τg)≥0\lambda\_{\mathrm{DW}}(\tau\_{g})\geq 0 as above, one can collect them in a
diagonal matrix ΛDW\Lambda\_{\mathrm{DW}} acting on the slice–stacked density,
and write

|  |  |  |
| --- | --- | --- |
|  | ℛDW​(a)=12​(E​a)⊤​ΛDW​L+​(E​a)=12​a⊤​QDW​a\mathcal{R}\_{\mathrm{DW}}(a)=\frac{1}{2}(Ea)^{\top}\Lambda\_{\mathrm{DW}}L^{+}(Ea)=\frac{1}{2}\,a^{\top}Q\_{\mathrm{DW}}a |  |

with QDW:=E⊤​ΛDW​L+​EQ\_{\mathrm{DW}}:=E^{\top}\Lambda\_{\mathrm{DW}}L^{+}E (or
QDW:=E⊤​ΛDW1/2​L+​ΛDW1/2​EQ\_{\mathrm{DW}}:=E^{\top}\Lambda\_{\mathrm{DW}}^{1/2}L^{+}\Lambda\_{\mathrm{DW}}^{1/2}E).
This is again symmetric positive semidefinite and independent of aa, so the
DW term remains a fixed quadratic form under tapering.

### 6.4  RN–module: near–maturity residual and calendar flattening

The objective here is on very short maturities to pull the forward-discounted call surface towards its τ↓0\tau\downarrow 0 limit and suppress calendar wiggles at fixed strike. Both are quadratic, so the overall QP stays convex.

On Γ0+={(mg,τg):τg≤τ⋆}\Gamma\_{0^{+}}=\{(m\_{g},\tau\_{g}):\tau\_{g}\leq\tau\_{\star}\}, anchor the price to the intrinsic
limit and penalise calendar drift at fixed strike:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛRN​(a)=λRN2​‖A​a−C0+‖2,Γ0+2+ηRN2​‖Aτ|K​a‖2,Γ0+2,\mathcal{R}\_{\mathrm{RN}}(a)\;=\;\frac{\lambda\_{\mathrm{RN}}}{2}\,\|Aa-C\_{0^{+}}\|\_{2,\Gamma\_{0^{+}}}^{2}\;+\;\frac{\eta\_{\mathrm{RN}}}{2}\,\|A\_{\tau|K}a\|\_{2,\Gamma\_{0^{+}}}^{2}, |  | (6.3) |

where C0+​(m)=F0​(1−em)+C\_{0^{+}}(m)=F\_{0}(1-e^{m})\_{+} and ∥⋅∥2,Γ0+\|\cdot\|\_{2,\Gamma\_{0^{+}}} is the ℓ2\ell\_{2} norm restricted
to indices in Γ0+\Gamma\_{0^{+}}. The terms mean the following:

1. 1.

   Near-maturity anchor: C0+​(m)C\_{0^{+}}(m) is the intrinsic value of a forward-discounted call. As τ↓0\tau\downarrow 0, no-arb implies that Cf​(m,τ)→C0+​(m)C\_{f}(m,\tau)\rightarrow C\_{0^{+}}(m). The term ‖A​a−C0+‖2,Γ0+2\|Aa-C\_{0^{+}}\|\_{2,\Gamma\_{0^{+}}}^{2} enforces this only on the short-end grid Γ0+\Gamma\_{0^{+}}.
2. 2.

   Calendar flattening at fixed strike: ‖Aτ|K​a‖2,Γ0+2\|A\_{\tau|K}a\|\_{2,\Gamma\_{0^{+}}}^{2} penalises the τ\tau-slope at fixed KK near τ=0\tau=0. This damps spurious day-to-day oscillations that data sparsity and noise can introduce at the short end.

We must derive Aτ|KA\_{\tau|K}, which was done in [4.3](https://arxiv.org/html/2512.01967v1#Ch4.S3 "4.3 Calendar derivative at fixed strike ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"). Since the operator is linear in aa, then it is a quadratic penalty.

To suppress odd–in–mm artifacts at τ↓0\tau\downarrow 0 we optionally project coefficients onto the even subspace along mm: let PevenP\_{\mathrm{even}} be the
diagonal projector with (Peven)(k,ℓ),(k,ℓ)=1(P\_{\mathrm{even}})\_{(k,\ell),(k,\ell)}=1 for even kk and 0 for odd kk;
replace aa by Peven​aP\_{\mathrm{even}}a when evaluating the first term in ([6.3](https://arxiv.org/html/2512.01967v1#Ch6.E3 "Equation 6.3 ‣ 6.4 RN–module: near–maturity residual and calendar flattening ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). This is linear
and preserves QP structure.

We set τ⋆∈[5,10]\tau\_{\star}\in[5,10] trading days. Default weights:
λRN\lambda\_{\mathrm{RN}} chosen so that the first term’s RMS on Γ0+\Gamma\_{0^{+}} matches the median
band width there; ηRN\eta\_{\mathrm{RN}} is set to achieve ≤0.5%\leq 0.5\% calendar violations on the
shortest two slices once combined with the no–arb penalties. Parity projection is off by default
(Peven=IP\_{\mathrm{even}}=I) unless short–end butterflies appear.

###### Lemma 5 (RN penalty as a fixed quadratic in the coefficients).

Let Γ0+\Gamma\_{0^{+}} be the short-maturity index set and let
Π0+∈ℝN×N\Pi\_{0^{+}}\in\mathbb{R}^{N\times N} be the diagonal selector with
(Π0+)i​i=1(\Pi\_{0^{+}})\_{ii}=1 if i∈Γ0+i\in\Gamma\_{0^{+}} and 0 otherwise. Then for
any a∈ℝPa\in\mathbb{R}^{P} the RN penalty ([6.3](https://arxiv.org/html/2512.01967v1#Ch6.E3 "Equation 6.3 ‣ 6.4 RN–module: near–maturity residual and calendar flattening ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) can be written as

|  |  |  |
| --- | --- | --- |
|  | ℛRN​(a)=12​a⊤​QRN​a+cRN⊤​a+const,\mathcal{R}\_{\mathrm{RN}}(a)\;=\;\frac{1}{2}\,a^{\top}Q\_{\mathrm{RN}}a+c\_{\mathrm{RN}}^{\top}a+\text{const}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | QRN:=λRN​A⊤​Π0+​A+ηRN​Aτ|K⊤​Π0+​Aτ|K⪰0,cRN:=−λRN​A⊤​Π0+​C0+.Q\_{\mathrm{RN}}:=\lambda\_{\mathrm{RN}}\,A^{\top}\Pi\_{0^{+}}A+\eta\_{\mathrm{RN}}\,A\_{\tau|K}^{\top}\Pi\_{0^{+}}A\_{\tau|K}\succeq 0,\qquad c\_{\mathrm{RN}}:=-\,\lambda\_{\mathrm{RN}}\,A^{\top}\Pi\_{0^{+}}C\_{0^{+}}. |  |

In particular, ℛRN\mathcal{R}\_{\mathrm{RN}} is a convex quadratic function of
the coefficient vector aa with fixed Hessian QRNQ\_{\mathrm{RN}}, so adding
ℛRN\mathcal{R}\_{\mathrm{RN}} to the objective preserves the convex QP structure.

###### Proof.

By definition of the restricted norm, there exists a diagonal selector
Π0+\Pi\_{0^{+}} such that for any x∈ℝNx\in\mathbb{R}^{N},

|  |  |  |
| --- | --- | --- |
|  | ‖x‖2,Γ0+2=‖Π0+​x‖22=x⊤​Π0+​x.\|x\|\_{2,\Gamma\_{0^{+}}}^{2}=\|\Pi\_{0^{+}}x\|\_{2}^{2}=x^{\top}\Pi\_{0^{+}}x. |  |

Therefore the two terms in ([6.3](https://arxiv.org/html/2512.01967v1#Ch6.E3 "Equation 6.3 ‣ 6.4 RN–module: near–maturity residual and calendar flattening ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) can be written as

|  |  |  |
| --- | --- | --- |
|  | ‖A​a−C0+‖2,Γ0+2=(A​a−C0+)⊤​Π0+​(A​a−C0+),\|Aa-C\_{0^{+}}\|\_{2,\Gamma\_{0^{+}}}^{2}=(Aa-C\_{0^{+}})^{\top}\Pi\_{0^{+}}(Aa-C\_{0^{+}}), |  |

|  |  |  |
| --- | --- | --- |
|  | ‖Aτ|K​a‖2,Γ0+2=(Aτ|K​a)⊤​Π0+​(Aτ|K​a).\|A\_{\tau|K}a\|\_{2,\Gamma\_{0^{+}}}^{2}=(A\_{\tau|K}a)^{\top}\Pi\_{0^{+}}(A\_{\tau|K}a). |  |

Expanding the first term gives

|  |  |  |
| --- | --- | --- |
|  | (A​a−C0+)⊤​Π0+​(A​a−C0+)=a⊤​A⊤​Π0+​A​a−2​C0+⊤​Π0+​A​a+C0+⊤​Π0+​C0+,(Aa-C\_{0^{+}})^{\top}\Pi\_{0^{+}}(Aa-C\_{0^{+}})=a^{\top}A^{\top}\Pi\_{0^{+}}Aa-2\,C\_{0^{+}}^{\top}\Pi\_{0^{+}}Aa+C\_{0^{+}}^{\top}\Pi\_{0^{+}}C\_{0^{+}}, |  |

while the second term is already of the form

|  |  |  |
| --- | --- | --- |
|  | (Aτ|K​a)⊤​Π0+​(Aτ|K​a)=a⊤​Aτ|K⊤​Π0+​Aτ|K​a.(A\_{\tau|K}a)^{\top}\Pi\_{0^{+}}(A\_{\tau|K}a)=a^{\top}A\_{\tau|K}^{\top}\Pi\_{0^{+}}A\_{\tau|K}a. |  |

Plugging into ([6.3](https://arxiv.org/html/2512.01967v1#Ch6.E3 "Equation 6.3 ‣ 6.4 RN–module: near–maturity residual and calendar flattening ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) yields

|  |  |  |
| --- | --- | --- |
|  | ℛRN​(a)=12​a⊤​QRN​a+cRN⊤​a+const,\mathcal{R}\_{\mathrm{RN}}(a)=\frac{1}{2}\,a^{\top}Q\_{\mathrm{RN}}a+c\_{\mathrm{RN}}^{\top}a+\text{const}, |  |

with QRNQ\_{\mathrm{RN}} and cRNc\_{\mathrm{RN}} as claimed, and a constant term
λRN2​C0+⊤​Π0+​C0+\frac{\lambda\_{\mathrm{RN}}}{2}\,C\_{0^{+}}^{\top}\Pi\_{0^{+}}C\_{0^{+}} which does
not depend on aa.

For any a∈ℝPa\in\mathbb{R}^{P},

|  |  |  |
| --- | --- | --- |
|  | a⊤​QRN​a=λRN​‖A​a‖2,Γ0+2+ηRN​‖Aτ|K​a‖2,Γ0+2≥ 0a^{\top}Q\_{\mathrm{RN}}a=\lambda\_{\mathrm{RN}}\,\|Aa\|\_{2,\Gamma\_{0^{+}}}^{2}+\eta\_{\mathrm{RN}}\,\|A\_{\tau|K}a\|\_{2,\Gamma\_{0^{+}}}^{2}\;\geq\;0 |  |

whenever λRN,ηRN≥0\lambda\_{\mathrm{RN}},\eta\_{\mathrm{RN}}\geq 0, so
QRN⪰0Q\_{\mathrm{RN}}\succeq 0 and the Hessian of
ℛRN\mathcal{R}\_{\mathrm{RN}} is positive semidefinite. All matrices
A,Aτ|K,Π0+A,A\_{\tau|K},\Pi\_{0^{+}} and the vector C0+C\_{0^{+}} are fixed once the
grid, short-maturity set Γ0+\Gamma\_{0^{+}}, and weights
λRN,ηRN\lambda\_{\mathrm{RN}},\eta\_{\mathrm{RN}} are chosen; hence
QRNQ\_{\mathrm{RN}} and cRNc\_{\mathrm{RN}} are independent of aa and
ℛRN\mathcal{R}\_{\mathrm{RN}} is a fixed convex quadratic function of the
coefficients.
∎

### 6.5  Ω\Omega–module: high–frequency taper and commutator hook

Let Uω∈ℝP×PU\_{\omega}\in\mathbb{R}^{P\times P} be a fixed orthogonal change of basis to a frequency chart
(separable 2D DCT aligned with the (k,ℓ)(k,\ell) grid). Denote a^=Uω​a\widehat{a}=U\_{\omega}a and
let MωM\_{\omega} be a diagonal mask selecting high–frequency indices. The taper is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛΩ​(a)=λΩ2​‖Mω​a^‖22=λΩ2​a⊤​Uω⊤​Mω⊤​Mω​Uω​a.\mathcal{R}\_{\Omega}(a)\;=\;\frac{\lambda\_{\Omega}}{2}\,\|M\_{\omega}\widehat{a}\|\_{2}^{2}\;=\;\frac{\lambda\_{\Omega}}{2}\,a^{\top}U\_{\omega}^{\top}M\_{\omega}^{\top}M\_{\omega}U\_{\omega}a. |  | (6.4) |

We use a maturity–dependent mask: on slices with τg≤τ⋆\tau\_{g}\leq\tau\_{\star} only the top third of
mm–frequencies are penalised; for τg>2​τ⋆\tau\_{g}>2\tau\_{\star} the mask is zero.

##### Liouville hook (commutator residual).

Let ℒ\mathcal{L} denote the forward–flow generator at fixed strike,
ℒ​Cf:=(∂τCf)|K\mathcal{L}C\_{f}:=(\partial\_{\tau}C\_{f})\big|\_{K}, and let ∂K\partial\_{K} be the
strike derivative. At the continuum level, mixed derivatives commute and we
can write the commutator

|  |  |  |
| --- | --- | --- |
|  | [ℒ,∂K]​Cf:=ℒ​(∂KCf)−∂K(ℒ​Cf),[\mathcal{L},\partial\_{K}]C\_{f}\;:=\;\mathcal{L}(\partial\_{K}C\_{f})\;-\;\partial\_{K}(\mathcal{L}C\_{f}), |  |

which vanishes for smooth CfC\_{f}.

On the collocation grid we work with nodal price vectors u∈ℝGu\in\mathbb{R}^{G} and
linear operators

|  |  |  |
| --- | --- | --- |
|  | A~K,A~τ|K∈ℝG×G\widetilde{A}\_{K},\;\widetilde{A}\_{\tau|K}\in\mathbb{R}^{G\times G} |  |

acting on uu and approximating, respectively, ∂KCf\partial\_{K}C\_{f} and
(∂τCf)|K(\partial\_{\tau}C\_{f})\big|\_{K} at the grid nodes. They are chosen consistently
with the coefficient–space design blocks AK,Aτ|K∈ℝG×PA\_{K},A\_{\tau|K}\in\mathbb{R}^{G\times P}
in the sense that for all coefficient vectors a∈ℝPa\in\mathbb{R}^{P},

|  |  |  |
| --- | --- | --- |
|  | A~K​(A​a)≈AK​a,A~τ|K​(A​a)≈Aτ|K​a,\widetilde{A}\_{K}(Aa)\approx A\_{K}a,\qquad\widetilde{A}\_{\tau|K}(Aa)\approx A\_{\tau|K}a, |  |

where u​(a):=A​au(a):=Aa denotes the nodal surface implied by aa.

Define the discrete commutator on nodal prices by

|  |  |  |
| --- | --- | --- |
|  | [A~τ|K,A~K]​u:=A~τ|K​(A~K​u)−A~K​(A~τ|K​u),[\widetilde{A}\_{\tau|K},\widetilde{A}\_{K}]\,u:=\widetilde{A}\_{\tau|K}(\widetilde{A}\_{K}u)-\widetilde{A}\_{K}(\widetilde{A}\_{\tau|K}u), |  |

and set

|  |  |  |
| --- | --- | --- |
|  | C:=A~τ|K​A~K−A~K​A~τ|K∈ℝG×G.C:=\widetilde{A}\_{\tau|K}\,\widetilde{A}\_{K}-\widetilde{A}\_{K}\,\widetilde{A}\_{\tau|K}\;\in\mathbb{R}^{G\times G}. |  |

Evaluated at the model surface u​(a)=A​au(a)=Aa, this yields the GG–vector
commutator defect

|  |  |  |
| --- | --- | --- |
|  | c​(a):=[A~τ|K,A~K]​u​(a)=C​(A​a).c(a):=[\widetilde{A}\_{\tau|K},\widetilde{A}\_{K}]\,u(a)=C(Aa). |  |

We penalise the hook residual via

|  |  |  |
| --- | --- | --- |
|  | ℛhook​(a):=λhook2​‖c​(a)‖22=λhook2​‖C​(A​a)‖22,\mathcal{R}\_{\mathrm{hook}}(a):=\frac{\lambda\_{\mathrm{hook}}}{2}\,\|c(a)\|\_{2}^{2}=\frac{\lambda\_{\mathrm{hook}}}{2}\,\|C(Aa)\|\_{2}^{2}, |  |

with a small stabilising weight λhook≪λNA\lambda\_{\mathrm{hook}}\ll\lambda\_{\mathrm{NA}}.

UωU\_{\omega} is the separable 2D DCT on (k,ℓ)(k,\ell); MωM\_{\omega} masks the
top 33%33\% highest mm–frequencies for τ≤τ⋆\tau\leq\tau\_{\star} and is zero otherwise; default
λΩ\lambda\_{\Omega} is picked so that the high–frequency modal energy share
ℰhi≤5%\mathcal{E}\_{\mathrm{hi}}\leq 5\%; λhook\lambda\_{\mathrm{hook}} is set to a small fraction
(10−310^{-3}–10−210^{-2}) of λNA\lambda\_{\mathrm{NA}}.

###### Lemma 6 (Ω\Omega taper and hook as fixed quadratics in the coefficients).

Let Uω∈ℝP×PU\_{\omega}\in\mathbb{R}^{P\times P} be an orthogonal matrix
(Uω⊤​Uω=IU\_{\omega}^{\top}U\_{\omega}=I), let Mω∈ℝP×PM\_{\omega}\in\mathbb{R}^{P\times P} be a fixed
diagonal mask, and define a^=Uω​a\widehat{a}=U\_{\omega}a. Let

|  |  |  |
| --- | --- | --- |
|  | ℛΩ​(a):=λΩ2​‖Mω​a^‖22\mathcal{R}\_{\Omega}(a):=\frac{\lambda\_{\Omega}}{2}\,\|M\_{\omega}\widehat{a}\|\_{2}^{2} |  |

and, with C:=A~τ|K​A~K−A~K​A~τ|K∈ℝG×GC:=\widetilde{A}\_{\tau|K}\widetilde{A}\_{K}-\widetilde{A}\_{K}\widetilde{A}\_{\tau|K}\in\mathbb{R}^{G\times G} as above,

|  |  |  |
| --- | --- | --- |
|  | c​(a):=C​(A​a),ℛhook​(a):=λhook2​‖c​(a)‖22=λhook2​‖C​(A​a)‖22.c(a):=C(Aa),\qquad\mathcal{R}\_{\mathrm{hook}}(a):=\frac{\lambda\_{\mathrm{hook}}}{2}\,\|c(a)\|\_{2}^{2}=\frac{\lambda\_{\mathrm{hook}}}{2}\,\|C(Aa)\|\_{2}^{2}. |  |

Then both penalties are fixed convex quadratic functions of the coefficient
vector aa:

|  |  |  |
| --- | --- | --- |
|  | ℛΩ​(a)=12​a⊤​QΩ​a,ℛhook​(a)=12​a⊤​Qhook​a,\mathcal{R}\_{\Omega}(a)=\frac{1}{2}\,a^{\top}Q\_{\Omega}a,\qquad\mathcal{R}\_{\mathrm{hook}}(a)=\frac{1}{2}\,a^{\top}Q\_{\mathrm{hook}}a, |  |

with

|  |  |  |
| --- | --- | --- |
|  | QΩ:=λΩ​Uω⊤​Mω⊤​Mω​Uω⪰0,Qhook:=λhook​A⊤​C⊤​C​A⪰0.Q\_{\Omega}:=\lambda\_{\Omega}\,U\_{\omega}^{\top}M\_{\omega}^{\top}M\_{\omega}U\_{\omega}\succeq 0,\qquad Q\_{\mathrm{hook}}:=\lambda\_{\mathrm{hook}}\,A^{\top}C^{\top}CA\succeq 0. |  |

All matrices Uω,Mω,A,A~K,A~τ|KU\_{\omega},M\_{\omega},A,\widetilde{A}\_{K},\widetilde{A}\_{\tau|K}, and thus
QΩ,QhookQ\_{\Omega},Q\_{\mathrm{hook}}, are independent of aa. In particular, adding
ℛΩ\mathcal{R}\_{\Omega} and ℛhook\mathcal{R}\_{\mathrm{hook}} to the objective preserves the convex
QP structure.

###### Proof.

For the taper, write

|  |  |  |
| --- | --- | --- |
|  | ℛΩ​(a)=λΩ2​‖Mω​Uω​a‖22=λΩ2​(Uω​a)⊤​Mω⊤​Mω​(Uω​a).\mathcal{R}\_{\Omega}(a)=\frac{\lambda\_{\Omega}}{2}\,\|M\_{\omega}U\_{\omega}a\|\_{2}^{2}=\frac{\lambda\_{\Omega}}{2}\,(U\_{\omega}a)^{\top}M\_{\omega}^{\top}M\_{\omega}(U\_{\omega}a). |  |

Set QΩ:=λΩ​Uω⊤​Mω⊤​Mω​UωQ\_{\Omega}:=\lambda\_{\Omega}\,U\_{\omega}^{\top}M\_{\omega}^{\top}M\_{\omega}U\_{\omega}.
Then

|  |  |  |
| --- | --- | --- |
|  | ℛΩ​(a)=12​a⊤​QΩ​a.\mathcal{R}\_{\Omega}(a)=\frac{1}{2}\,a^{\top}Q\_{\Omega}a. |  |

For any aa,

|  |  |  |
| --- | --- | --- |
|  | a⊤​QΩ​a=λΩ​‖Mω​Uω​a‖22≥ 0a^{\top}Q\_{\Omega}a=\lambda\_{\Omega}\,\|M\_{\omega}U\_{\omega}a\|\_{2}^{2}\;\geq\;0 |  |

whenever λΩ≥0\lambda\_{\Omega}\geq 0, so QΩ⪰0Q\_{\Omega}\succeq 0. Once the grid,
frequency chart, and maturity–dependent mask are chosen, both UωU\_{\omega}
and MωM\_{\omega} are fixed, and therefore QΩQ\_{\Omega} is fixed (independent
of aa).

For the hook, note that AA is a fixed linear map from coefficients to nodal
prices and CC is a fixed linear operator on grid space, so the commutator
residual is linear in aa:

|  |  |  |
| --- | --- | --- |
|  | c​(a)=C​(A​a)=(C​A)​a.c(a)=C(Aa)=(CA)\,a. |  |

Let B:=C​A∈ℝG×PB:=CA\in\mathbb{R}^{G\times P}. Then

|  |  |  |
| --- | --- | --- |
|  | ℛhook​(a)=λhook2​‖B​a‖22=λhook2​a⊤​B⊤​B​a.\mathcal{R}\_{\mathrm{hook}}(a)=\frac{\lambda\_{\mathrm{hook}}}{2}\,\|Ba\|\_{2}^{2}=\frac{\lambda\_{\mathrm{hook}}}{2}\,a^{\top}B^{\top}Ba. |  |

Setting Qhook:=λhook​A⊤​C⊤​C​A=λhook​B⊤​BQ\_{\mathrm{hook}}:=\lambda\_{\mathrm{hook}}\,A^{\top}C^{\top}CA=\lambda\_{\mathrm{hook}}\,B^{\top}B gives

|  |  |  |
| --- | --- | --- |
|  | ℛhook​(a)=12​a⊤​Qhook​a.\mathcal{R}\_{\mathrm{hook}}(a)=\frac{1}{2}\,a^{\top}Q\_{\mathrm{hook}}a. |  |

For any aa,

|  |  |  |
| --- | --- | --- |
|  | a⊤​Qhook​a=λhook​‖B​a‖22≥ 0a^{\top}Q\_{\mathrm{hook}}a=\lambda\_{\mathrm{hook}}\,\|Ba\|\_{2}^{2}\;\geq\;0 |  |

whenever λhook≥0\lambda\_{\mathrm{hook}}\geq 0, so Qhook⪰0Q\_{\mathrm{hook}}\succeq 0.
All ingredients are fixed once AA, A~K\widetilde{A}\_{K}, A~τ|K\widetilde{A}\_{\tau|K} and
λhook\lambda\_{\mathrm{hook}} are chosen, so QhookQ\_{\mathrm{hook}} is independent
of aa.

Thus both ℛΩ\mathcal{R}\_{\Omega} and ℛhook\mathcal{R}\_{\mathrm{hook}} are fixed convex quadratic
functions of the coefficients.
∎

### 6.6  Summary of fixed choices used

* •

  Ridge: α=β=1\alpha=\beta=1, s=2s=2; λridge\lambda\_{\mathrm{ridge}} by GCV on an 8%8\%
  WLS subsample (no hinge, no penalties); fixed per date, reused in the full QP.
* •

  𝚲\bm{\Lambda} reparameterisation: UU built by blockwise (per–τ\tau) QR/Gram–Schmidt
  and column rescaling on (A​U)(AU) over the quotes; all blocks post–multiplied by UU; ridge uses
  Λ~=U⊤​Λ​U\widetilde{\Lambda}=U^{\top}\Lambda U.
* •

  DW: H−1H^{-1} along mm per slice with Neumann ends; Chebyshev–Lobatto MmM\_{m};
  λDW​(τ)=λDW(0)​min⁡{1,τ⋆/τ}\lambda\_{\mathrm{DW}}(\tau)=\lambda\_{\mathrm{DW}}^{(0)}\min\{1,\tau\_{\star}/\tau\},
  τ⋆∈[5,10]\tau\_{\star}\in[5,10] trading days.
* •

  RN: window Γ0+={τ≤τ⋆}\Gamma\_{0^{+}}=\{\tau\leq\tau\_{\star}\}; weights (λRN,ηRN)(\lambda\_{\mathrm{RN}},\eta\_{\mathrm{RN}}) calibrated to short–end RMS and calendar share; Peven=IP\_{\mathrm{even}}=I by default.
* •

  𝛀\bm{\Omega}: separable 2D DCT, mask top 33%33\% mm–frequencies for τ≤τ⋆\tau\leq\tau\_{\star}, off beyond 2​τ⋆2\tau\_{\star}; λΩ\lambda\_{\Omega} chosen to cap high–frequency energy at ≤5%\leq 5\%.
* •

  Hook: commutator penalty λhook2​‖C​(A​a)‖22\frac{\lambda\_{\mathrm{hook}}}{2}\,\|C(Aa)\|\_{2}^{2} with
  C:=A~τ|K​A~K−A~K​A~τ|K∈ℝG×GC:=\widetilde{A}\_{\tau|K}\widetilde{A}\_{K}-\widetilde{A}\_{K}\widetilde{A}\_{\tau|K}\in\mathbb{R}^{G\times G} and
  λhook∈[10−3,10−2]​λNA\lambda\_{\mathrm{hook}}\in[10^{-3},10^{-2}]\,\lambda\_{\mathrm{NA}}.

All terms above are quadratic in aa (or a~\tilde{a}) and are entered additively into the QP objective.
They stabilise the global fit, suppress short–maturity artifacts, and improve conditioning while
preserving convexity and the solver class.

## 7.  No–arbitrage constraints and soft penalties

We impose the three shape conditions (monotone in KK, convex in KK, and calendar nonnegativity at fixed KK) as soft penalties evaluated on the collocation grid, using the linear operators defined previously:

|  |  |  |
| --- | --- | --- |
|  | AK,AK​K,Aτ|K∈ℝG×P,and the price block ​A∈ℝG×P.A\_{K},\quad A\_{KK},\quad A\_{\tau|K}\in\mathbb{R}^{G\times P},\qquad\text{and the price block }A\in\mathbb{R}^{G\times P}. |  |

All vectors below are understood componentwise and (x)+=max⁡{x,0}(x)\_{+}=\max\{x,0\}.

### 7.1  Penalty definitions (soft versions of the shape constraints)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒫mono​(a)\displaystyle\mathcal{P}\_{\text{mono}}(a) | =λNA2​‖(AK​a)+‖22\displaystyle=\frac{\lambda\_{\text{NA}}}{2}\,\big\|(A\_{K}a)\_{+}\big\|\_{2}^{2} | (targets ∂KCf≤0),\displaystyle\text{(targets $\partial\_{K}C\_{f}\leq 0$)}, |  | (7.1) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒫conv​(a)\displaystyle\mathcal{P}\_{\text{conv}}(a) | =λNA2​‖(−AK​K​a)+‖22\displaystyle=\frac{\lambda\_{\text{NA}}}{2}\,\big\|(-A\_{KK}a)\_{+}\big\|\_{2}^{2} | (targets ∂K​KCf≥0),\displaystyle\text{(targets $\partial\_{KK}C\_{f}\geq 0$)}, |  | (7.2) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒫cal​(a)\displaystyle\mathcal{P}\_{\text{cal}}(a) | =λNA2​‖(−Aτ|K​a)+‖22\displaystyle=\frac{\lambda\_{\text{NA}}}{2}\,\big\|(-A\_{\tau|K}a)\_{+}\big\|\_{2}^{2} | (targets (∂τCf)|K≥0),\displaystyle\text{(targets $(\partial\_{\tau}C\_{f})|\_{K}\geq 0$)}, |  | (7.3) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒫bnd​(a)\displaystyle\mathcal{P}\_{\text{bnd}}(a) | =λB2​(‖(−A​a)+‖22+‖(A​a−F)+‖22)\displaystyle=\frac{\lambda\_{\text{B}}}{2}\left(\big\|(-Aa)\_{+}\big\|\_{2}^{2}+\big\|(Aa-F)\_{+}\big\|\_{2}^{2}\right) | (targets 0≤Cf≤F).\displaystyle\text{(targets $0\leq C\_{f}\leq F$)}. |  | (7.4) |

These are sums of squares of convex functions of an affine map of aa, hence convex and QP–compatible.

##### QP form (auxiliary slacks).

Exactly as in the band–hinge reformulation, each penalty admits a slack representation. For example,

|  |  |  |
| --- | --- | --- |
|  | 12​‖(AK​a)+‖22=minu∈ℝG⁡12​‖u‖22s.t.u≥AK​a,u≥0,\frac{1}{2}\big\|(A\_{K}a)\_{+}\big\|\_{2}^{2}=\min\_{u\in\mathbb{R}^{G}}\ \frac{1}{2}\|u\|\_{2}^{2}\quad\text{s.t.}\quad u\geq A\_{K}a,\ \ u\geq 0, |  |

and similarly

|  |  |  |
| --- | --- | --- |
|  | 12​‖(−AK​K​a)+‖22=minv≥0,v≥−AK​K​a⁡12​‖v‖22,12​‖(−Aτ|K​a)+‖22=minw≥0,w≥−Aτ|K​a⁡12​‖w‖22,\frac{1}{2}\big\|(-A\_{KK}a)\_{+}\big\|\_{2}^{2}=\min\_{v\geq 0,\ v\geq-A\_{KK}a}\ \frac{1}{2}\|v\|\_{2}^{2},\quad\frac{1}{2}\big\|(-A\_{\tau|K}a)\_{+}\big\|\_{2}^{2}=\min\_{w\geq 0,\ w\geq-A\_{\tau|K}a}\ \frac{1}{2}\|w\|\_{2}^{2}, |  |

and for bounds

|  |  |  |
| --- | --- | --- |
|  | 12​‖(−A​a)+‖2+12​‖(A​a−F)+‖2=mins,t≥0,s≥−A​a,t≥A​a−F⁡12​(‖s‖2+‖t‖2).\frac{1}{2}\big\|(-Aa)\_{+}\big\|^{2}+\frac{1}{2}\big\|(Aa-F)\_{+}\big\|^{2}=\min\_{s,t\geq 0,\ s\geq-Aa,\ t\geq Aa-F}\ \frac{1}{2}\big(\|s\|^{2}+\|t\|^{2}\big). |  |

###### Lemma 7.

For any x∈ℝGx\in\mathbb{R}^{G},

|  |  |  |
| --- | --- | --- |
|  | 12​‖(x)+‖22=minu∈ℝG⁡{12​‖(u)+‖22:u≥x,u≥0}\frac{1}{2}\|(x)\_{+}\|^{2}\_{2}=\min\_{u\in\mathbb{R}^{G}}\{\frac{1}{2}\|(u)\_{+}\|^{2}\_{2}:u\geq x,u\geq 0\} |  |

and the unique minimiser is u∗=(x)+u^{\*}=(x)\_{+}.

###### Proof.

The problem separates across coordinates. For scalar u∈ℝu\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | minu∈ℝ⁡12​u2stu≥x,u≥0\min\_{u\in\mathbb{R}}\frac{1}{2}u^{2}\quad\text{st}\quad u\geq x,\;u\geq 0 |  |

has feasible set u≥m​a​x​{x, 0}u\geq max\{x,\;0\}. The objective 12​u2\frac{1}{2}u^{2} is strictly increasing on [0,∞)[0,\infty), so the minimum is attained at the smallest feasible point:

|  |  |  |
| --- | --- | --- |
|  | u∗=max⁡{x,0}=x+,u^{\*}=\max\{x,0\}=x\_{+}, |  |

with value 12​(x+)2\frac{1}{2}(x\_{+})^{2}. Summing over coordinates gives the vector result, and strict convexity yields uniqueness.
∎

### 7.2  Row scaling and invariance

As in §[9](https://arxiv.org/html/2512.01967v1#Ch9 "9. Scaling, schedules, and the 𝜇-controller ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), we scale each block (after any UU–reparameterisation) by a positive scalar so typical row norms are comparable:

|  |  |  |
| --- | --- | --- |
|  | A~K=1sK​AK,A~K​K=1sK​K​AK​K,A~τ|K=1sτ​Aτ|K,\widetilde{A}\_{K}=\frac{1}{s\_{K}}A\_{K},\quad\widetilde{A}\_{KK}=\frac{1}{s\_{KK}}A\_{KK},\quad\widetilde{A}\_{\tau|K}=\frac{1}{s\_{\tau}}A\_{\tau|K}, |  |

with s∙s\_{\bullet} the empirical p95 of row ℓ2\ell\_{2} norms ([4.5](https://arxiv.org/html/2512.01967v1#Ch4.S5 "4.5 Row scaling and a single no-arb weight ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). Hard constraints are invariant under positive row/ block scaling, and with soft penalties this makes a single λNA\lambda\_{\text{NA}} control all three terms on a comparable numeric scale.

### 7.3  Compatibility with the Λ\Lambda–module

Under the price–invariant reparameterisation a=U​a~a=U\tilde{a} (see the Λ\Lambda–module), all operators post–multiply by UU:

|  |  |  |
| --- | --- | --- |
|  | A∙←A∙U,∙∈{,K,KK,τ|K}.A\_{\bullet}\leftarrow A\_{\bullet}U,\qquad\bullet\in\{\,,K,KK,\tau|K\,\}. |  |

By construction, A∙​U​a~=A∙​aA\_{\bullet}U\,\tilde{a}=A\_{\bullet}a, so the penalty values are unchanged and convexity is preserved. The spectral ridge is updated by congruence Λ↦Λ~=U⊤​Λ​U\Lambda\mapsto\widetilde{\Lambda}=U^{\top}\Lambda U as already stated.

### 7.4  Binned variant (optional)

To stabilise very sparse regions, aggregate quotes by a selector G∈{0,1}B×NG\in\{0,1\}^{B\times N} (bins in (m,τ)(m,\tau)) and replace the per–quote band–hinge term ∑iℓband​((A​a)i;bi,ai)\sum\_{i}\ell\_{\text{band}}((Aa)\_{i};b\_{i},a\_{i}) by

|  |  |  |
| --- | --- | --- |
|  | ∑b=1Bℓband​((G​A​a)b;(G​b)b,(G​a)b);\sum\_{b=1}^{B}\ell\_{\text{band}}((GAa)\_{b};(Gb)\_{b},(Ga)\_{b}); |  |

the slack QP form carries over verbatim.

After scaling, we use a single λNA\lambda\_{\text{NA}} for (A~K,A~K​K,A~τ|K)(\widetilde{A}\_{K},\widetilde{A}\_{KK},\widetilde{A}\_{\tau|K}) and select it (once per date) to reach ≤1%\leq 1\% violations on the evaluation grid; λB\lambda\_{\text{B}} is kept separate for price bounds.

## 8.  The convex program

We collect all terms and write the problem as a single quadratic program (QP). When the
Λ\Lambda–module is active ([6.2](https://arxiv.org/html/2512.01967v1#Ch6.S2 "6.2 Λ–module: price–invariant reparameterisation ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), we solve in a~=U−1​a\tilde{a}=U^{-1}a with all
blocks post–multiplied by UU and Λ\Lambda replaced by Λ~=U⊤​Λ​U\widetilde{\Lambda}=U^{\top}\Lambda U; to
avoid clutter we keep the symbol aa below (read as a~\tilde{a} in that case).

### 8.1  Slack QP (standard form)

Let u,v∈ℝNu,v\in\mathbb{R}^{N} be the band slacks from §[5.2](https://arxiv.org/html/2512.01967v1#Ch5.S2 "5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), and let
uK,vK​K,wτ∈ℝGu\_{K},v\_{KK},w\_{\tau}\in\mathbb{R}^{G} and slo,shi∈ℝGs\_{\mathrm{lo}},s\_{\mathrm{hi}}\in\mathbb{R}^{G} be nonnegative grid slacks
for the three shape operators and price bounds, respectively (all inequalities
componentwise):

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | u\displaystyle u | ≥b−A​a,\displaystyle\geq b-Aa, | u\displaystyle u | ≥0,\displaystyle\geq 0, | v\displaystyle v | ≥A​a−a,\displaystyle\geq Aa-a, | v\displaystyle v | ≥0,\displaystyle\geq 0, |  |
|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | uK\displaystyle u\_{K} | ≥AK​a,\displaystyle\geq A\_{K}a, | uK\displaystyle u\_{K} | ≥0,\displaystyle\geq 0, | vK​K\displaystyle v\_{KK} | ≥−AK​K​a,\displaystyle\geq-A\_{KK}a, | vK​K\displaystyle v\_{KK} | ≥0,\displaystyle\geq 0, |  |
|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | wτ\displaystyle w\_{\tau} | ≥−Aτ|K​a,\displaystyle\geq-A\_{\tau|K}a, | wτ\displaystyle w\_{\tau} | ≥0,\displaystyle\geq 0, |  | | | | |
|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | slo\displaystyle s\_{\mathrm{lo}} | ≥−A​a,\displaystyle\geq-Aa, | slo\displaystyle s\_{\mathrm{lo}} | ≥0,\displaystyle\geq 0, | shi\displaystyle s\_{\mathrm{hi}} | ≥A​a−F,\displaystyle\geq Aa-F, | shi\displaystyle s\_{\mathrm{hi}} | ≥0.\displaystyle\geq 0. |  |

With these slacks, the objective collects the data term (§[5](https://arxiv.org/html/2512.01967v1#Ch5 "5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), the
quadratic regularisers (§[6](https://arxiv.org/html/2512.01967v1#Ch6 "6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), and the soft no–arb penalties
(§[7.1](https://arxiv.org/html/2512.01967v1#Ch7.S1 "7.1 Penalty definitions (soft versions of the shape constraints) ‣ 7. No–arbitrage constraints and soft penalties ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | mina,u,v,uK,vK​K,wτ,slo,shi\displaystyle\min\_{a,u,v,u\_{K},v\_{KK},w\_{\tau},s\_{\mathrm{lo}},s\_{\mathrm{hi}}} | 12​‖W1/2​(A​a−y)‖22+μ2​(‖u‖22+‖v‖22)\displaystyle\frac{1}{2}\|W^{1/2}(Aa-y)\|\_{2}^{2}+\frac{\mu}{2}\big(\|u\|\_{2}^{2}+\|v\|\_{2}^{2}\big) |  | (8.1) |
|  |  | +λridge2​a⊤​Λ​a+λDW2​a⊤​E⊤​L+​E​a+ηRN2​‖Aτ|K​a‖2,Γ0+2\displaystyle\ +\frac{\lambda\_{\mathrm{ridge}}}{2}\,a^{\top}\Lambda a+\frac{\lambda\_{\mathrm{DW}}}{2}\,a^{\top}E^{\top}L^{+}Ea+\frac{\eta\_{\mathrm{RN}}}{2}\,\|A\_{\tau|K}a\|\_{2,\Gamma\_{0^{+}}}^{2} |  |
|  |  | +λΩ2​a⊤​Uω⊤​Mω⊤​Mω​Uω​a+λhook2​‖C​(A​a)‖22\displaystyle\ +\frac{\lambda\_{\Omega}}{2}\,a^{\top}U\_{\omega}^{\top}M\_{\omega}^{\top}M\_{\omega}U\_{\omega}a+\frac{\lambda\_{\mathrm{hook}}}{2}\,\|C(Aa)\|\_{2}^{2} |  |
|  |  | +λRN2​‖A​a−C0+‖2,Γ0+2\displaystyle\ +\frac{\lambda\_{\mathrm{RN}}}{2}\,\|Aa-C\_{0^{+}}\|\_{2,\Gamma\_{0^{+}}}^{2} |  |
|  |  | +λNA2​(‖uK‖22+‖vK​K‖22+‖wτ‖22)+λB2​(‖slo‖22+‖shi‖22).\displaystyle\ +\frac{\lambda\_{\mathrm{NA}}}{2}\big(\|u\_{K}\|\_{2}^{2}+\|v\_{KK}\|\_{2}^{2}+\|w\_{\tau}\|\_{2}^{2}\big)+\frac{\lambda\_{\mathrm{B}}}{2}\big(\|s\_{\mathrm{lo}}\|\_{2}^{2}+\|s\_{\mathrm{hi}}\|\_{2}^{2}\big). |  |

All matrices (AA, AKA\_{K}, AK​KA\_{KK}, Aτ|KA\_{\tau|K}, EE, UωU\_{\omega}, MωM\_{\omega}, L+L^{+}, CC)
are fixed from earlier sections; ∥⋅∥2,Γ0+\|\cdot\|\_{2,\Gamma\_{0^{+}}} denotes restriction to the short–maturity
index set. Row–scaled operators (§[9](https://arxiv.org/html/2512.01967v1#Ch9 "9. Scaling, schedules, and the 𝜇-controller ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) may be used in place of unscaled ones.

##### Why ([8.1](https://arxiv.org/html/2512.01967v1#Ch8.E1 "Equation 8.1 ‣ 8.1 Slack QP (standard form) ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) is a QP:

Every term in the objective is a convex quadratic form in aa or a sum of squared slacks; all
constraints are linear inequalities.

### 8.2  Convexity, existence, and uniqueness

###### Proposition 7 (Convexity and global optimality).

The program ([8.1](https://arxiv.org/html/2512.01967v1#Ch8.E1 "Equation 8.1 ‣ 8.1 Slack QP (standard form) ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) is convex. If a convex QP solver returns a feasible
primal–dual point satisfying KKT, then the associated a⋆a^{\star} is a *global* minimiser.

###### Proof.

The feasible set is a polyhedron (linear inequalities), hence convex and closed. The objective
is a sum of convex quadratics, hence convex and lower semicontinuous. KKT conditions are
necessary and sufficient for convex QPs; any feasible KKT point is globally optimal.
∎

###### Proposition 8 (Strict convexity conditions and uniqueness).

Define C:=A~τ|K​A~K−A~K​A~τ|K∈ℝG×GC:=\widetilde{A}\_{\tau|K}\widetilde{A}\_{K}-\widetilde{A}\_{K}\widetilde{A}\_{\tau|K}\in\mathbb{R}^{G\times G}. and ΠΓ0+\Pi\_{\Gamma\_{0^{+}}} selects the short maturity grid.If the quadratic form in aa,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q=A⊤​W​A+λridge​Λ+λDW​E⊤​L+​E+λΩ​Uω⊤​Mω⊤​Mω​Uω\displaystyle Q\;=\;A^{\top}WA+\lambda\_{\mathrm{ridge}}\Lambda+\lambda\_{\mathrm{DW}}E^{\top}L^{+}E+\lambda\_{\Omega}U\_{\omega}^{\top}M\_{\omega}^{\top}M\_{\omega}U\_{\omega} |  | (8.2) |
|  | +λhook​A⊤​C⊤​C​A+λRN​A⊤​Π0+​A+ηRN​Aτ|K⊤​Π0+​Aτ|K,\displaystyle+\lambda\_{\mathrm{hook}}A^{\top}C^{\top}CA+\lambda\_{\mathrm{RN}}\,A^{\top}\Pi\_{0^{+}}A+\eta\_{\mathrm{RN}}\,A\_{\tau|K}^{\top}\Pi\_{0^{+}}A\_{\tau|K}, |  |

is positive definite, then the objective is strictly convex in (a,u,v,…)(a,u,v,\dots) and the minimiser is unique.
In particular, it suffices that A⊤​W​AA^{\top}WA be positive definite on ℛ​(A)\mathcal{R}(A) and
λridge>0\lambda\_{\mathrm{ridge}}>0 (cf. §[5.2](https://arxiv.org/html/2512.01967v1#Ch5.S2.SSx1 "Strict convexity and uniqueness of the data QP ‣ 5.2 Quadratic–program form via auxiliary slacks ‣ 5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")).

###### Proof.

Block Hessian is blkdiag⁡(Q,μ​I,μ​I,λNA​I,…)\operatorname{blkdiag}(Q,\mu I,\mu I,\lambda\_{\mathrm{NA}}I,\dots); if Q≻0Q\succ 0 and
μ,λNA,λB>0\mu,\lambda\_{\mathrm{NA}},\lambda\_{\mathrm{B}}>0, the whole Hessian is positive definite.
∎

###### Definition 4 (Global coefficient-space metric).

Define the symmetric positive *semidefinite* matrix

|  |  |  |
| --- | --- | --- |
|  | Mh:=A⊤​W​A+λridge​Λ+λDW​E⊤​L+​E+λΩ​Uω⊤​Mω⊤​Mω​Uω\displaystyle M\_{h}\;:=\;A^{\top}WA\;+\;\lambda\_{\mathrm{ridge}}\Lambda\;+\;\lambda\_{\mathrm{DW}}E^{\top}L\_{+}E\;+\;\lambda\_{\Omega}U\_{\omega}^{\top}M\_{\omega}^{\top}M\_{\omega}U\_{\omega} |  |
|  |  |  |
| --- | --- | --- |
|  | +λhook​A⊤​C⊤​C​A+λRN​A⊤​Π0+​A+ηRN​Aτ|K⊤​Π0+​Aτ|K.\displaystyle\;+\;\lambda\_{\mathrm{hook}}A^{\top}C^{\top}CA\;+\;\lambda\_{\mathrm{RN}}A^{\top}\Pi\_{0^{+}}A\;+\;\eta\_{\mathrm{RN}}\,A\_{\tau|K}^{\top}\Pi\_{0^{+}}A\_{\tau|K}. |  |

###### Assumption 1 (Strictly positive ridge shape).

The ridge shape matrix Λ\Lambda is symmetric positive definite
(e.g. diagonal with strictly positive entries).

###### Proposition 9 (When MhM\_{h} is positive definite).

Suppose Assumption [1](https://arxiv.org/html/2512.01967v1#Thmassump1 "Assumption 1 (Strictly positive ridge shape). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") holds and
λridge>0\lambda\_{\mathrm{ridge}}>0.
Then the matrix MhM\_{h} from Definition [4](https://arxiv.org/html/2512.01967v1#Thmdefinition4 "Definition 4 (Global coefficient-space metric). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") is symmetric
positive definite. In particular, MhM\_{h} is invertible and induces
a norm ‖a‖Mh2:=a⊤​Mh​a\|a\|\_{M\_{h}}^{2}:=a^{\top}M\_{h}a on ℝP\mathbb{R}^{P}.

###### Proof.

Each term in the definition of MhM\_{h} is symmetric and positive
semidefinite. Under Assumption [1](https://arxiv.org/html/2512.01967v1#Thmassump1 "Assumption 1 (Strictly positive ridge shape). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), Λ≻0\Lambda\succ 0,
so for any a≠0a\neq 0 we have

|  |  |  |
| --- | --- | --- |
|  | a⊤​(λridge​Λ)​a=λridge​a⊤​Λ​a>0a^{\top}\bigl(\lambda\_{\mathrm{ridge}}\Lambda\bigr)a=\lambda\_{\mathrm{ridge}}\,a^{\top}\Lambda a>0 |  |

whenever λridge>0\lambda\_{\mathrm{ridge}}>0.
All the remaining terms in MhM\_{h} are positive semidefinite, so

|  |  |  |
| --- | --- | --- |
|  | a⊤​Mh​a=a⊤​(λridge​Λ)​a+a⊤​(psd terms)​a≥λridge​a⊤​Λ​a>0a^{\top}M\_{h}a=a^{\top}\bigl(\lambda\_{\mathrm{ridge}}\Lambda\bigr)a+a^{\top}(\text{psd terms})a\geq\lambda\_{\mathrm{ridge}}\,a^{\top}\Lambda a>0 |  |

for all a≠0a\neq 0. Hence Mh≻0M\_{h}\succ 0.
∎

###### Proposition 10 (Metric projection form of the global solution).

Let 𝒞h⊂ℝP\mathcal{C}\_{h}\subset\mathbb{R}^{P} be the polyhedron defined by the hard
constraints (if any) in aa (no–arbitrage, bounds, etc.). Consider the strictly
convex quadratic problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | mina∈𝒞h⁡12​a⊤​Mh​a−b⊤​a,\min\_{a\in\mathcal{C}\_{h}}\;\frac{1}{2}\,a^{\top}M\_{h}a\;-\;b^{\top}a, |  | (8.3) |

where MhM\_{h} is the matrix from Definition [4](https://arxiv.org/html/2512.01967v1#Thmdefinition4 "Definition 4 (Global coefficient-space metric). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") and

|  |  |  |  |
| --- | --- | --- | --- |
|  | b:=A⊤​W​y−cRN,b:=A^{\top}Wy-c\_{\mathrm{RN}}, |  | (8.4) |

with cRNc\_{\mathrm{RN}} the linear coefficient from Lemma [5](https://arxiv.org/html/2512.01967v1#Thmlemma5 "Lemma 5 (RN penalty as a fixed quadratic in the coefficients). ‣ 6.4 RN–module: near–maturity residual and calendar flattening ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

Set

|  |  |  |  |
| --- | --- | --- | --- |
|  | a^:=Mh−1​b.\hat{a}\;:=\;M\_{h}^{-1}b. |  | (8.5) |

Then the unique minimiser a⋆a^{\star} of ([8.3](https://arxiv.org/html/2512.01967v1#Ch8.E3 "Equation 8.3 ‣ Proposition 10 (Metric projection form of the global solution). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) can be
written as the metric projection of a^\hat{a} onto 𝒞h\mathcal{C}\_{h} in the MhM\_{h}–inner
product:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a⋆=arg⁡mina∈𝒞h⁡12​‖a−a^‖Mh2,‖z‖Mh2:=z⊤​Mh​z.a^{\star}\;=\;\arg\min\_{a\in\mathcal{C}\_{h}}\frac{1}{2}\,\|a-\hat{a}\|\_{M\_{h}}^{2},\qquad\|z\|\_{M\_{h}}^{2}:=z^{\top}M\_{h}z. |  | (8.6) |

###### Proof.

Write the objective in ([8.3](https://arxiv.org/html/2512.01967v1#Ch8.E3 "Equation 8.3 ‣ Proposition 10 (Metric projection form of the global solution). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) as

|  |  |  |
| --- | --- | --- |
|  | J​(a):=12​a⊤​Mh​a−b⊤​a,a∈𝒞h.J(a):=\frac{1}{2}\,a^{\top}M\_{h}a-b^{\top}a,\qquad a\in\mathcal{C}\_{h}. |  |

By Definition [4](https://arxiv.org/html/2512.01967v1#Thmdefinition4 "Definition 4 (Global coefficient-space metric). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") the matrix MhM\_{h} is symmetric and positive semidefinite.
Under the assumptions of Proposition [8](https://arxiv.org/html/2512.01967v1#Thmprop8 "Proposition 8 (Strict convexity conditions and uniqueness). ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") (in particular,
A⊤​W​AA^{\top}WA positive definite on the span of AA and λridge>0\lambda\_{\mathrm{ridge}}>0),
the quadratic form a↦a⊤​Mh​aa\mapsto a^{\top}M\_{h}a is positive definite, and hence MhM\_{h}
is symmetric positive definite. In particular, MhM\_{h} is invertible, so a^\hat{a} is
well defined by

|  |  |  |
| --- | --- | --- |
|  | a^:=Mh−1​b⟺Mh​a^=b.\hat{a}:=M\_{h}^{-1}b\quad\Longleftrightarrow\quad M\_{h}\hat{a}=b. |  |

We first rewrite JJ in terms of (a−a^)(a-\hat{a}). Using b=Mh​a^b=M\_{h}\hat{a} and the
symmetry of MhM\_{h}, for any a∈ℝPa\in\mathbb{R}^{P},

|  |  |  |
| --- | --- | --- |
|  | J​(a)=12​a⊤​Mh​a−b⊤​a=12​a⊤​Mh​a−(Mh​a^)⊤​a=12​a⊤​Mh​a−a^⊤​Mh​a.J(a)=\frac{1}{2}\,a^{\top}M\_{h}a-b^{\top}a=\frac{1}{2}\,a^{\top}M\_{h}a-(M\_{h}\hat{a})^{\top}a=\frac{1}{2}\,a^{\top}M\_{h}a-\hat{a}^{\top}M\_{h}a. |  |

On the other hand,

|  |  |  |
| --- | --- | --- |
|  | (a−a^)⊤​Mh​(a−a^)=a⊤​Mh​a−2​a^⊤​Mh​a+a^⊤​Mh​a^,(a-\hat{a})^{\top}M\_{h}(a-\hat{a})=a^{\top}M\_{h}a-2\,\hat{a}^{\top}M\_{h}a+\hat{a}^{\top}M\_{h}\hat{a}, |  |

again by symmetry of MhM\_{h}. Hence,

|  |  |  |
| --- | --- | --- |
|  | 12​(a−a^)⊤​Mh​(a−a^)−12​a^⊤​Mh​a^=12​a⊤​Mh​a−a^⊤​Mh​a=J​(a).\frac{1}{2}\,(a-\hat{a})^{\top}M\_{h}(a-\hat{a})-\frac{1}{2}\,\hat{a}^{\top}M\_{h}\hat{a}=\frac{1}{2}\,a^{\top}M\_{h}a-\hat{a}^{\top}M\_{h}a=J(a). |  |

Thus, for all a∈ℝPa\in\mathbb{R}^{P},

|  |  |  |
| --- | --- | --- |
|  | J​(a)=12​(a−a^)⊤​Mh​(a−a^)−12​a^⊤​Mh​a^.J(a)=\frac{1}{2}\,(a-\hat{a})^{\top}M\_{h}(a-\hat{a})-\frac{1}{2}\,\hat{a}^{\top}M\_{h}\hat{a}. |  |

The second term on the right-hand side does not depend on aa. Therefore,
minimising JJ over a∈𝒞ha\in\mathcal{C}\_{h} is equivalent to minimising

|  |  |  |
| --- | --- | --- |
|  | a⟼12​(a−a^)⊤​Mh​(a−a^)=12​‖a−a^‖Mh2a\;\longmapsto\;\frac{1}{2}\,(a-\hat{a})^{\top}M\_{h}(a-\hat{a})=\frac{1}{2}\,\|a-\hat{a}\|\_{M\_{h}}^{2} |  |

over a∈𝒞ha\in\mathcal{C}\_{h}. Since MhM\_{h} is positive definite, this functional is
strictly convex in aa, so it has a unique minimiser in the closed convex set
𝒞h\mathcal{C}\_{h}; by definition, this minimiser is the metric projection of
a^\hat{a} onto 𝒞h\mathcal{C}\_{h} in the MhM\_{h}–inner product. This is exactly the
claim.
∎

When discussing the hard–constraint limit it will be convenient to make the global
feasibility assumption explicit. Namely, we assume that the static no–arbitrage and
bound inequalities admit at least one coefficient vector, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞NA:={a∈ℝP:AK​a≤0,−AK​K​a≤0,−Aτ|K​a≤0, 0≤A​a≤F}≠∅.\mathcal{C}\_{\mathrm{NA}}:=\bigl\{a\in\mathbb{R}^{P}:A\_{K}a\leq 0,\;-A\_{KK}a\leq 0,\;-A\_{\tau|K}a\leq 0,\;0\leq Aa\leq F\bigr\}\neq\varnothing. |  | (8.7) |

This is a modelling condition stating that the chosen Chebyshev approximation space
contains at least one globally static no–arbitrage surface.

##### Hard–constraint limits.

Hard–constraint limits. Under ([8.7](https://arxiv.org/html/2512.01967v1#Ch8.E7 "Equation 8.7 ‣ 8.2 Convexity, existence, and uniqueness ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), letting
λNA,λB→∞\lambda\_{\mathrm{NA}},\lambda\_{B}\to\infty drives the corresponding slacks to 0 and
recovers the constrained solution of the remaining strictly convex quadratic objective. If the
intersection is empty, the finite–λ\lambda problem yields the minimum–violation compromise
(§[7.1](https://arxiv.org/html/2512.01967v1#Ch7.S1 "7.1 Penalty definitions (soft versions of the shape constraints) ‣ 7. No–arbitrage constraints and soft penalties ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")).

### 8.3  Invariance and scaling

If the Λ\Lambda–module is used (§[6.2](https://arxiv.org/html/2512.01967v1#Ch6.S2 "6.2 Λ–module: price–invariant reparameterisation ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), replace every block by its
multiplied version and Λ\Lambda by Λ~=U⊤​Λ​U\widetilde{\Lambda}=U^{\top}\Lambda U; the feasible set and all
objective values are unchanged (Proposition [5](https://arxiv.org/html/2512.01967v1#Thmprop5 "Proposition 5 (Price/constraint invariance). ‣ Blockwise whitening and why it is safe: ‣ 6.2 Λ–module: price–invariant reparameterisation ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). Row–scaling the no–arb blocks
(§[9](https://arxiv.org/html/2512.01967v1#Ch9 "9. Scaling, schedules, and the 𝜇-controller ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) multiplies them by positive scalars and only equilibrates numeric weights; it
does not alter feasibility.

### 8.4  Solution procedure (used)

Solve ([8.1](https://arxiv.org/html/2512.01967v1#Ch8.E1 "Equation 8.1 ‣ 8.1 Slack QP (standard form) ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) with OSQP (warm starts). The no–arb weight
λNA\lambda\_{\mathrm{NA}} is set after row scaling to hit ≤1%\leq 1\% grid violations
(§[9](https://arxiv.org/html/2512.01967v1#Ch9 "9. Scaling, schedules, and the 𝜇-controller ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")); λridge\lambda\_{\mathrm{ridge}} is fixed by GCV on a small WLS subsample
(§[6.1](https://arxiv.org/html/2512.01967v1#Ch6.S1 "6.1 Spectral ridge (modal energy control) ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")); μ\mu is increased by a short controller until target coverage is reached
(§[5](https://arxiv.org/html/2512.01967v1#Ch5 "5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). All other quadratic weights follow §[6](https://arxiv.org/html/2512.01967v1#Ch6 "6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

###### Remark 15 (Why the 99/199/1 target is attainable).

The data term prices *into* the bid–ask bands (hinge), while AK,AK​K,Aτ|KA\_{K},A\_{KK},A\_{\tau|K} are
enforced densely on the grid with p95 row scaling, so a single λNA\lambda\_{\mathrm{NA}} controls the
violation budget. Short–maturity defects are suppressed by the RN anchoring and the DW/Ω\Omega
terms, which remove the usual butterfly/aliasing artifacts.

## 9.  Scaling, schedules, and the μ\mu-controller

### 9.1  Row scaling (summary)

We use the p95 block-scalar normalisation of §[4.5](https://arxiv.org/html/2512.01967v1#Ch4.S5 "4.5 Row scaling and a single no-arb weight ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"): on the grid,
set A~K=AK/sK\widetilde{A}\_{K}=A\_{K}/s\_{K}, A~K​K=AK​K/sK​K\widetilde{A}\_{KK}=A\_{KK}/s\_{KK},
A~τ|K=Aτ|K/sτ\widetilde{A}\_{\tau|K}=A\_{\tau|K}/s\_{\tau} with s∙=q0.95s\_{\bullet}=\mathrm{q}\_{0.95} of row ℓ2\ell\_{2} norms,
computed *after* the Λ\Lambda–module transform. This preserves hard feasibility and allows a
single λNA\lambda\_{\mathrm{NA}} to control all three terms on a comparable scale.

### 9.2  Short schedule for λNA\lambda\_{\mathrm{NA}}

We select λNA\lambda\_{\mathrm{NA}} on a thinned setup to save time while preserving the target
violation share.

##### Thinned probe:

Build a reduced grid (every other Chebyshev node in mm and a
coarser subset in τ\tau) and a tiny quote subset (55-10%10\% uniformly across (m,τ)(m,\tau)).
Fix a moderate μ\mu (the previous day’s value) and all other weights.

##### Grid search:

For a short geometric ladder
Λtrial={1,2,4,8,16,32,64,128,256}\Lambda\_{\mathrm{trial}}=\{1,2,4,8,16,32,64,128,256\} solve the QP on the thinned setup and
measure the violation rate:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | viol​(λ)\displaystyle\mathrm{viol}(\lambda) | =13​G∑g=1G(𝟏{(AKa(λ))g>τK}\displaystyle=\frac{1}{3G}\sum\_{g=1}^{G}\Big(\mathbf{1}\{(A\_{K}a(\lambda))\_{g}>\tau\_{K}\} |  | (9.1) |
|  |  | +𝟏{(−AK​Ka(λ))g>τK​K}+𝟏{(−Aτ∣Ka(λ))g>ττ}).\displaystyle\quad+\mathbf{1}\{(-A\_{KK}a(\lambda))\_{g}>\tau\_{KK}\}+\mathbf{1}\{(-A\_{\tau\mid K}a(\lambda))\_{g}>\tau\_{\tau}\}\Big). |  |

with small numerical tolerances τ∙\tau\_{\bullet} (in scaled units). Pick the smallest
λ∈Λtrial\lambda\in\Lambda\_{\mathrm{trial}} such that viol​(λ)≤1%\mathrm{viol}(\lambda)\leq 1\%, and *fix*
that λNA\lambda\_{\mathrm{NA}} for the full grid and book.

##### Explanation:

Solve the QP ([8.1](https://arxiv.org/html/2512.01967v1#Ch8.E1 "Equation 8.1 ‣ 8.1 Slack QP (standard form) ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) repeatedly, but with λNA←λ\lambda\_{\mathrm{NA}}\leftarrow\lambda for each λ∈Λtrial\lambda\in\Lambda\_{\mathrm{trial}} and all other weights fixed. Each solve returns a different a​(λ)a(\lambda) and then using this a​(λ)a(\lambda), compute the violation rate viol​(λ)\mathrm{viol}(\lambda). From the violation rates pick the smallest λ\lambda achieving ≤1%\leq 1\%, and use that as λNA\lambda\_{\mathrm{NA}} for the full problem.

###### Remark 16 (Invariance to scaling).

Because each block was divided by sBs\_{B}, the selected λNA\lambda\_{\mathrm{NA}} is stable
day-to-day and across underliers; without scaling, the same ladder would over/under–penalise
whichever block happens to have the largest raw norms.

### 9.3  The μ\mu–controller (coverage target)

Recall the coverage–seeking data term (§[5](https://arxiv.org/html/2512.01967v1#Ch5 "5. Coverage-seeking data term with bid-ask geometry ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")): the mid–squared error plus
μ\mu times the quadratic band–hinge. Let

|  |  |  |
| --- | --- | --- |
|  | Hinge​(a):=∑i=1Nℓband​((A​a)i;bi,ai)=12​‖dist​(A​a,[b,a])‖22,\mathrm{Hinge}(a)\;:=\;\sum\_{i=1}^{N}\ell\_{\mathrm{band}}\big((Aa)\_{i};b\_{i},a\_{i}\big)=\tfrac{1}{2}\big\|\mathrm{dist}(Aa,\,[b,a])\big\|\_{2}^{2}, |  |

|  |  |  |
| --- | --- | --- |
|  | Cov​(a):=1N​∑i=1N𝟏​{bi≤(A​a)i≤ai}.\mathrm{Cov}(a)\;:=\;\frac{1}{N}\sum\_{i=1}^{N}\mathbf{1}\{b\_{i}\leq(Aa)\_{i}\leq a\_{i}\}. |  |

We adjust μ\mu (similar to [9.2](https://arxiv.org/html/2512.01967v1#Ch9.S2 "9.2 Short schedule for 𝜆_NA ‣ 9. Scaling, schedules, and the 𝜇-controller ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) so that Cov​(a⋆​(μ))\mathrm{Cov}(a^{\star}(\mu)) reaches a target (99%99\%).
Although coverage is a discrete functional (hence may have plateaus), the hinge at the
optimiser is nonincreasing in μ\mu:

###### Lemma 8 (Monotonicity of optimal hinge).

Let g​(a)g(a) denote the full objective without the hinge weight (all terms in ([8.1](https://arxiv.org/html/2512.01967v1#Ch8.E1 "Equation 8.1 ‣ 8.1 Slack QP (standard form) ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))
except μ​Hinge​(a)\mu\,\mathrm{Hinge}(a)). For μ1<μ2\mu\_{1}<\mu\_{2}, let
aj∈arg⁡mina⁡{g​(a)+μj​Hinge​(a)}a\_{j}\in\arg\min\_{a}\{g(a)+\mu\_{j}\,\mathrm{Hinge}(a)\} for j=1, 2j=1,\;2. Then
Hinge​(a2)≤Hinge​(a1)\mathrm{Hinge}(a\_{2})\leq\mathrm{Hinge}(a\_{1}).

###### Proof.

By definition of the minimisers, for all x,yx,\;y we have the following:

|  |  |  |
| --- | --- | --- |
|  | g​(a1)+μ1​H​(a1)≤g​(x)+μ1​H​(x);g(a\_{1})+\mu\_{1}H(a\_{1})\leq g(x)+\mu\_{1}H(x); |  |

|  |  |  |
| --- | --- | --- |
|  | g​(a2)+μ2​H​(a2)≤g​(y)+μ2​H​(y).g(a\_{2})+\mu\_{2}H(a\_{2})\leq g(y)+\mu\_{2}H(y). |  |

Taking x=a2x=a\_{2} and y=a1y=a\_{1} yields the following:

|  |  |  |
| --- | --- | --- |
|  | g​(a1)+μ1​H​(a1)≤g​(a2)+μ1​H​(a2)g(a\_{1})+\mu\_{1}H(a\_{1})\leq g(a\_{2})+\mu\_{1}H(a\_{2}) |  |

|  |  |  |
| --- | --- | --- |
|  | g​(a2)+μ2​H​(a2)≤g​(a1)+μ2​H​(a1)g(a\_{2})+\mu\_{2}H(a\_{2})\leq g(a\_{1})+\mu\_{2}H(a\_{1}) |  |

Summing and dividing by μ2−μ1>0\mu\_{2}-\mu\_{1}>0 yields H​(a2)≤H​(a1)H(a\_{2})\leq H(a\_{1}).
∎

##### Controller (bracket & bisection).

1. 1.

   *Bracket.* Start from (μmin,μmax)(\mu\_{\min},\mu\_{\max}) (reusing prior-day values when
   available). If coverage at μmax\mu\_{\max} is below target, expand μmax←c​μmax\mu\_{\max}\leftarrow c\,\mu\_{\max}
   (e.g. c=4c=4) until Cov​(a⋆​(μmax))\mathrm{Cov}(a^{\star}(\mu\_{\max})) crosses the target or a cap is reached.
2. 2.

   *Bisection.* While μmax−μmin\mu\_{\max}-\mu\_{\min} is above tolerance and coverage not yet at
   target, set μ←μmin​μmax\mu\leftarrow\sqrt{\mu\_{\min}\mu\_{\max}} (geometric bisection), solve once, and
   update the endpoint whose coverage is on the wrong side of the target.

##### What is held fixed:

All other weights (λridge,λNA,λDW,λΩ,λRN,λB\lambda\_{\mathrm{ridge}},\lambda\_{\mathrm{NA}},\lambda\_{\mathrm{DW}},\lambda\_{\Omega},\lambda\_{\mathrm{RN}},\lambda\_{\mathrm{B}}) and the scaled operators are held
fixed while μ\mu is adjusted.

### 9.4  Practical notes

* •

  *Warm starts.* Reuse a⋆a^{\star} when moving along the λNA\lambda\_{\mathrm{NA}} ladder
  and the μ\mu bracket; OSQP converges in a few iterations from a nearby point.
* •

  *Tolerances.* Use small positive tolerances τ∙\tau\_{\bullet} when counting violations to
  avoid flagging solver noise; report violations in unscaled operator units.
* •

  *Stability.* If coverage oscillates near the target, accept the smallest μ\mu in the
  final bracket that achieves the target.

## 10.  Short-maturity remedy

Recall the calendar operator at fixed strike from §[4](https://arxiv.org/html/2512.01967v1#Ch4 "4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") (see ([4.3](https://arxiv.org/html/2512.01967v1#Ch4.E3 "Equation 4.3 ‣ 4.3 Calendar derivative at fixed strike ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))):

|  |  |  |
| --- | --- | --- |
|  | Aτ|K=Aτ+diag⁡(−ρ​(τg))​Am,ρ​(τ)≡dd​τ​log⁡F​(τ).A\_{\tau|K}\;=\;A\_{\tau}\;+\;\operatorname{diag}\!\big(-\rho(\tau\_{g})\big)\,A\_{m},\quad\rho(\tau)\equiv\tfrac{d}{d\tau}\log F(\tau). |  |

When τ\tau is very small, noise in ∂mCf\partial\_{m}C\_{f} is fed into
(∂τCf)|K(\partial\_{\tau}C\_{f})|\_{K} through the ρ​(τ)\rho(\tau) term, so small ripples in mm can flip
the calendar sign. Counter this with three convex, model–agnostic devices that act only
near the boundary and vanish smoothly as maturity grows.

### 10.1  Boundary anchoring and calendar flattening on Γ0+\Gamma\_{0^{+}}

Let Γ0+={g:τg≤τ⋆}\Gamma\_{0^{+}}=\{g:\tau\_{g}\leq\tau\_{\star}\} be the short–maturity window (usually
τ⋆=5\tau\_{\star}=5–1010 trading days). Define the intrinsic forward–discounted limit

|  |  |  |
| --- | --- | --- |
|  | C0+​(m)=F0​(1−em)+=(F0−K)+,m=log⁡(K/F0).C\_{0^{+}}(m)\;=\;F\_{0}\,(1-e^{m})\_{+}\;=\;\big(F\_{0}-K\big)^{+},\qquad m=\log(K/F\_{0}). |  |

We use the convex quadratic (see [6.3](https://arxiv.org/html/2512.01967v1#Ch6.E3 "Equation 6.3 ‣ 6.4 RN–module: near–maturity residual and calendar flattening ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛRN​(a)=λRN2​‖A​a−C0+‖2,Γ0+2+ηRN2​‖Aτ|K​a‖2,Γ0+2.\mathcal{R}\_{\mathrm{RN}}(a)\;=\;\frac{\lambda\_{\mathrm{RN}}}{2}\,\|Aa-C\_{0^{+}}\|\_{2,\Gamma\_{0^{+}}}^{2}\;+\;\frac{\eta\_{\mathrm{RN}}}{2}\,\|A\_{\tau|K}a\|\_{2,\Gamma\_{0^{+}}}^{2}. |  | (10.1) |

###### Lemma 9 (Consistency with the short–time limit).

Assume that for fixed K≠F0K\neq F\_{0}, Cf​(K,τ)→(F0−K)+C\_{f}(K,\tau)\to(F\_{0}-K)^{+} and
∂τCf​(K,τ)|K→0\partial\_{\tau}C\_{f}(K,\tau)\big|\_{K}\to 0 as τ↓0\tau\downarrow 0.
Let Γ0+={g:τg≤τ⋆}\Gamma\_{0^{+}}=\{g:\tau\_{g}\leq\tau\_{\star}\} and write

|  |  |  |
| --- | --- | --- |
|  | R1​(a):=‖A​a−C0+‖2,Γ0+2,R2​(a):=‖Aτ|K​a‖2,Γ0+2,R\_{1}(a):=\|Aa-C\_{0^{+}}\|\_{2,\Gamma\_{0^{+}}}^{2},\qquad R\_{2}(a):=\|A\_{\tau|K}a\|\_{2,\Gamma\_{0^{+}}}^{2}, |  |

so that the RN penalty in ([10.1](https://arxiv.org/html/2512.01967v1#Ch10.E1 "Equation 10.1 ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) is λRN2​R1​(a)+ηRN2​R2​(a)\tfrac{\lambda\_{\mathrm{RN}}}{2}R\_{1}(a)+\tfrac{\eta\_{\mathrm{RN}}}{2}R\_{2}(a).
Let ℱ⊂ℝP\mathcal{F}\subset\mathbb{R}^{P} be a closed convex feasible set and let g:ℱ→ℝg:\mathcal{F}\to\mathbb{R}
collect all other (convex) terms of the objective in ([8.1](https://arxiv.org/html/2512.01967v1#Ch8.E1 "Equation 8.1 ‣ 8.1 Slack QP (standard form) ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")).
Assume the boundary conditions are attainable on Γ0+\Gamma\_{0^{+}}, i.e.

|  |  |  |
| --- | --- | --- |
|  | 𝒞:={a∈ℱ:R1​(a)=0,R2​(a)=0}≠∅.\mathcal{C}:=\{a\in\mathcal{F}:\ R\_{1}(a)=0,\ R\_{2}(a)=0\}\neq\varnothing. |  |

For λ,η>0\lambda,\eta>0 define

|  |  |  |
| --- | --- | --- |
|  | Jλ,η​(a):=g​(a)+λ2​R1​(a)+η2​R2​(a),aλ,η∈arg⁡mina∈ℱ⁡Jλ,η​(a).J\_{\lambda,\eta}(a):=g(a)+\frac{\lambda}{2}R\_{1}(a)+\frac{\eta}{2}R\_{2}(a),\quad a\_{\lambda,\eta}\in\arg\min\_{a\in\mathcal{F}}J\_{\lambda,\eta}(a). |  |

Then, as min⁡{λ,η}→∞\min\{\lambda,\eta\}\to\infty,

|  |  |  |
| --- | --- | --- |
|  | R1​(aλ,η)→0andR2​(aλ,η)→0,R\_{1}(a\_{\lambda,\eta})\to 0\qquad\text{and}\qquad R\_{2}(a\_{\lambda,\eta})\to 0, |  |

so A​aλ,η→C0+Aa\_{\lambda,\eta}\to C\_{0^{+}} and Aτ|K​aλ,η→0A\_{\tau|K}a\_{\lambda,\eta}\to 0 on Γ0+\Gamma\_{0^{+}}.
Moreover, every cluster point a⋆a^{\star} of {aλ,η}\{a\_{\lambda,\eta}\} solves the equality–constrained problem

|  |  |  |
| --- | --- | --- |
|  | min⁡{g​(a):a∈𝒞}.\min\{\,g(a):\ a\in\mathcal{C}\,\}. |  |

###### Proof.

Step 1 (residuals vanish).
Pick a0∈𝒞a^{0}\in\mathcal{C} (exists by assumption, discussed later), so R1​(a0)=R2​(a0)=0R\_{1}(a^{0})=R\_{2}(a^{0})=0.
By optimality of aλ,ηa\_{\lambda,\eta},

|  |  |  |
| --- | --- | --- |
|  | Jλ,η​(aλ,η)≤Jλ,η​(a0)=g​(a0).J\_{\lambda,\eta}(a\_{\lambda,\eta})\;\leq\;J\_{\lambda,\eta}(a^{0})\;=\;g(a^{0}). |  |

Hence, for all λ,η>0\lambda,\eta>0,

|  |  |  |
| --- | --- | --- |
|  | g​(aλ,η)+λ2​R1​(aλ,η)+η2​R2​(aλ,η)≤g​(a0).g(a\_{\lambda,\eta})+\frac{\lambda}{2}R\_{1}(a\_{\lambda,\eta})+\frac{\eta}{2}R\_{2}(a\_{\lambda,\eta})\;\leq\;g(a^{0}). |  |

Since gg is bounded below on ℱ\mathcal{F} (true in our QP, e.g. by the ridge term; (Remark [18](https://arxiv.org/html/2512.01967v1#Thmremark18 "Remark 18 (Lower bound for 𝑔). ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))), there exists m>−∞m>-\infty
with g​(a)≥mg(a)\geq m for all a∈ℱa\in\mathcal{F}. Therefore

|  |  |  |
| --- | --- | --- |
|  | λ2R1(aλ,η)+η2R2(aλ,η)≤g(a0)−g(aλ,η)≤g(a0)−m=:C<∞.\frac{\lambda}{2}R\_{1}(a\_{\lambda,\eta})+\frac{\eta}{2}R\_{2}(a\_{\lambda,\eta})\;\leq\;g(a^{0})-g(a\_{\lambda,\eta})\;\leq\;g(a^{0})-m\;=:\;C<\infty. |  |

Let min⁡{λ,η}→∞\min\{\lambda,\eta\}\to\infty. The left-hand side is a sum of nonnegative terms with coefficients
diverging to +∞+\infty, so necessarily

|  |  |  |
| --- | --- | --- |
|  | R1​(aλ,η)→0andR2​(aλ,η)→0.R\_{1}(a\_{\lambda,\eta})\to 0\quad\text{and}\quad R\_{2}(a\_{\lambda,\eta})\to 0. |  |

By linearity of AA and Aτ|KA\_{\tau|K}, this yields A​aλ,η→C0+Aa\_{\lambda,\eta}\to C\_{0^{+}} and
Aτ|K​aλ,η→0A\_{\tau|K}a\_{\lambda,\eta}\to 0 on Γ0+\Gamma\_{0^{+}}.

Step 2 (limit points solve the constrained problem).
Because gg is convex and (by the ridge) coercive on ℱ\mathcal{F}, the sequence {aλ,η}\{a\_{\lambda,\eta}\} is bounded; thus it has cluster points. Let aλ,η→a⋆a\_{\lambda,\eta}\to a^{\star} along some subsequence. From Step 1 and continuity of the linear maps, a⋆∈𝒞a^{\star}\in\mathcal{C}.

For any a∈𝒞a\in\mathcal{C}, we have Jλ,η​(a)=g​(a)J\_{\lambda,\eta}(a)=g(a), hence

|  |  |  |
| --- | --- | --- |
|  | Jλ,η​(aλ,η)≤Jλ,η​(a)=g​(a)⇒g​(aλ,η)≤g​(a)∀λ,η.J\_{\lambda,\eta}(a\_{\lambda,\eta})\leq J\_{\lambda,\eta}(a)=g(a)\quad\Rightarrow\quad g(a\_{\lambda,\eta})\leq g(a)\qquad\forall\,\lambda,\eta. |  |

Taking lim sup\limsup and using lower semicontinuity of gg,

|  |  |  |
| --- | --- | --- |
|  | g​(a⋆)≤lim infg​(aλ,η)≤lim supg​(aλ,η)≤g​(a)∀a∈𝒞,g(a^{\star})\ \leq\ \liminf g(a\_{\lambda,\eta})\ \leq\ \limsup g(a\_{\lambda,\eta})\ \leq\ g(a)\quad\forall\,a\in\mathcal{C}, |  |

so g​(a⋆)=minx∈𝒞⁡g​(x)g(a^{\star})=\min\_{x\in\mathcal{C}}g(x). This completes the proof.
∎

###### Remark 17.

If exact feasibility on Γ0+\Gamma\_{0^{+}} is relaxed (e.g. excluding an ATM tube |m|≤c​τ|m|\leq c\sqrt{\tau}),
interpret R1,R2R\_{1},R\_{2} with that restriction; the same argument applies. If 𝒞=∅\mathcal{C}=\varnothing, then
R1​(aλ,η)R\_{1}(a\_{\lambda,\eta}) and R2​(aλ,η)R\_{2}(a\_{\lambda,\eta}) converge to their joint infimum and aλ,ηa\_{\lambda,\eta}
approaches the minimum–violation compromise.

###### Remark 18 (Lower bound for gg).

In ([8.1](https://arxiv.org/html/2512.01967v1#Ch8.E1 "Equation 8.1 ‣ 8.1 Slack QP (standard form) ‣ 8. The convex program ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) the function g​(a)g(a) (all terms except the RN penalty) is a sum of
positive–semidefinite quadratics and squared norms with positive weights:
12​‖W1/2​(A​a−y)‖22\tfrac{1}{2}\|W^{1/2}(Aa-y)\|\_{2}^{2}, λridge2​a⊤​Λ​a\tfrac{\lambda\_{\mathrm{ridge}}}{2}a^{\top}\Lambda a,
λDW2​a⊤​E⊤​L+​E​a\tfrac{\lambda\_{\mathrm{DW}}}{2}a^{\top}E^{\top}L^{+}Ea,
λΩ2​a⊤​Uω⊤​Mω⊤​Mω​Uω​a\tfrac{\lambda\_{\Omega}}{2}a^{\top}U\_{\omega}^{\top}M\_{\omega}^{\top}M\_{\omega}U\_{\omega}a, etc.
After dropping the constant 12​y⊤​W​y\tfrac{1}{2}y^{\top}Wy from the LS term, we have g​(a)≥0g(a)\geq 0
for all a∈ℱa\in\mathcal{F}. Hence m:=infa∈ℱg​(a)≥0m:=\inf\_{a\in\mathcal{F}}g(a)\geq 0 is finite, which is the bound
used in the proof of Lemma [9](https://arxiv.org/html/2512.01967v1#Thmlemma9 "Lemma 9 (Consistency with the short–time limit). ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

###### Remark 19 (Attainability is an assumption).

Lemma [9](https://arxiv.org/html/2512.01967v1#Thmlemma9 "Lemma 9 (Consistency with the short–time limit). ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") assumes the boundary conditions are attainable on Γ0+\Gamma\_{0^{+}},
i.e. 𝒞:={a∈ℱ:R1​(a)=0,R2​(a)=0}≠∅\mathcal{C}:=\{a\in\mathcal{F}:\ R\_{1}(a)=0,\ R\_{2}(a)=0\}\neq\varnothing.
This is not automatic; it depends on the basis and the feasible set ℱ\mathcal{F}.

###### Proposition 11 (Sufficient discrete condition for attainability).

Let AΓ∈ℝG0×PA\_{\Gamma}\in\mathbb{R}^{G\_{0}\times P} and Aτ|K,Γ∈ℝG0×PA\_{\tau|K,\Gamma}\in\mathbb{R}^{G\_{0}\times P} denote
AA and Aτ|KA\_{\tau|K} restricted to the rows g∈Γ0+g\in\Gamma\_{0^{+}} (with G0:=|Γ0+|G\_{0}:=|\Gamma\_{0^{+}}|).
Stack the constraints into

|  |  |  |
| --- | --- | --- |
|  | S:=[AΓAτ|K,Γ]∈ℝ(2​G0)×P,c:=[C0+0]∈ℝ2​G0.S\;:=\;\begin{bmatrix}A\_{\Gamma}\\[2.0pt] A\_{\tau|K,\Gamma}\end{bmatrix}\in\mathbb{R}^{(2G\_{0})\times P},\qquad c\;:=\;\begin{bmatrix}C\_{0^{+}}\\[2.0pt] 0\end{bmatrix}\in\mathbb{R}^{2G\_{0}}. |  |

If rank​(S)=2​G0\mathrm{rank}(S)=2G\_{0} (full row rank) and ℱ=ℝP\mathcal{F}=\mathbb{R}^{P} (or ℱ\mathcal{F} is any convex set
that contains a solution of S​a=cSa=c), then 𝒞≠∅\mathcal{C}\neq\varnothing.
In particular, when P≥2​G0P\geq 2G\_{0} and SS has full row rank, the system S​a=cSa=c is solvable and any solution aa
satisfies R1​(a)=R2​(a)=0R\_{1}(a)=R\_{2}(a)=0.

###### Proof.

If rank​(S)=2​G0≤P\mathrm{rank}(S)=2G\_{0}\leq P, then Range​(S)=ℝ2​G0\mathrm{Range}(S)=\mathbb{R}^{2G\_{0}}, so for any right-hand side cc
there exists a∈ℝPa\in\mathbb{R}^{P} with S​a=cSa=c. Such an aa obeys AΓ​a=C0+A\_{\Gamma}a=C\_{0^{+}} and
Aτ|K,Γ​a=0A\_{\tau|K,\Gamma}a=0, hence R1​(a)=R2​(a)=0R\_{1}(a)=R\_{2}(a)=0; if ℱ\mathcal{F} contains one such aa, then a∈𝒞a\in\mathcal{C}.
∎

###### Corollary 1 (Practical sufficient conditions).

Attainability holds if (i) the coefficient space is rich enough so that P≥2​G0P\geq 2G\_{0}
and the slice-restricted design matrices have independent rows (so SS has full row rank), and
(ii) the feasible set ℱ\mathcal{F} does not exclude these solutions.
For Chebyshev tensor bases in (m,τ)(m,\tau), increasing degrees (K,L)(K,L) makes SS generically full row rank
on a fixed grid Γ0+\Gamma\_{0^{+}}; moreover, the boundary value C0+∈[0,F0]C\_{0^{+}}\in[0,F\_{0}] and the condition
Aτ|K,Γ​a=0A\_{\tau|K,\Gamma}a=0 are compatible with usual hard constraints (monotonicity/convexity and bounds).

###### Remark 20 (If attainability fails).

If 𝒞=∅\mathcal{C}=\varnothing (e.g. degrees too low, or additional constraints forbid exact matching),
then the conclusions of Lemma [9](https://arxiv.org/html/2512.01967v1#Thmlemma9 "Lemma 9 (Consistency with the short–time limit). ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") hold in the approximate sense:
R1​(aλ,η)→R1⋆R\_{1}(a\_{\lambda,\eta})\to R\_{1}^{\star} and R2​(aλ,η)→R2⋆R\_{2}(a\_{\lambda,\eta})\to R\_{2}^{\star} where
R1⋆+R2⋆=infa∈ℱ{R1​(a)+R2​(a)}R\_{1}^{\star}+R\_{2}^{\star}=\inf\_{a\in\mathcal{F}}\{R\_{1}(a)+R\_{2}(a)\}; the minimisers converge to the
minimum-violation compromise on Γ0+\Gamma\_{0^{+}}.

##### ATM tube (optional).

To avoid over–penalizing the thin region where the O​(τ)O(\sqrt{\tau}) time value concentrates,
one may exclude |m|≤c​τ|m|\leq c\sqrt{\tau} from Γ0+\Gamma\_{0^{+}} (small cc) or down–weight those rows.

##### Parity projection (optional).

As a linear preprocessing that preserves QP structure, set a←Peven​aa\leftarrow P\_{\mathrm{even}}a with
(Peven)(k,ℓ),(k,ℓ)=1(P\_{\mathrm{even}})\_{(k,\ell),(k,\ell)}=1 for even kk and 0 for odd kk when evaluating the
first term in ([10.1](https://arxiv.org/html/2512.01967v1#Ch10.E1 "Equation 10.1 ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")); this removes odd–in–mm glitches near τ↓0\tau\downarrow 0.

### 10.2  Frequency truncation: Ω\Omega taper near the boundary

Use the spectral mask from §[6.5](https://arxiv.org/html/2512.01967v1#Ch6.S5 "6.5 Ω–module: high–frequency taper and commutator hook ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), but only on short maturities. Let
UωU\_{\omega} be the fixed frequency chart (e.g. separable 2D DCT) and define a maturity–dependent
mask Mω​(τg)M\_{\omega}(\tau\_{g}) that zeros the highest mm–frequencies on slices with
τg≤τ⋆\tau\_{g}\leq\tau\_{\star} and ramps to 0 by 2​τ⋆2\tau\_{\star}:

|  |  |  |
| --- | --- | --- |
|  | ℛΩ​(a)=12​∑g:τg​gridλΩ​(τg)​‖Mω​(τg)​Uω​a‖22,\mathcal{R}\_{\Omega}(a)\;=\;\frac{1}{2}\sum\_{g:\,\tau\_{g}\ \text{grid}}\lambda\_{\Omega}(\tau\_{g})\,\|M\_{\omega}(\tau\_{g})\,U\_{\omega}a\|\_{2}^{2}, |  |

|  |  |  |
| --- | --- | --- |
|  | λΩ​(τ)=λΩ(0)×{1,τ≤τ⋆,2−τ/τ⋆,τ⋆<τ≤2​τ⋆,0,τ>2​τ⋆.\lambda\_{\Omega}(\tau)\!=\!\lambda\_{\Omega}^{(0)}\!\times\!\begin{cases}1,&\tau\leq\tau\_{\star},\\ 2-\tau/\tau\_{\star},&\tau\_{\star}<\tau\leq 2\tau\_{\star},\\ 0,&\tau>2\tau\_{\star}.\end{cases} |  |

This convex quadratic suppresses only the high–kk content where butterfly ripples originate;
low modes (ATM/term structure) are left intact by construction.

### 10.3  Transport damping: H−1H^{-1} smoothing of density at short maturities

Let ρ=∂K​KCf\rho=\partial\_{KK}C\_{f} and recall the discrete H−1H^{-1} seminorm from §[6.3](https://arxiv.org/html/2512.01967v1#Ch6.S3 "6.3 DW–module: discrete transport (𝐻⁻¹) smoothing of density ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"):
‖f‖H−12=f⊤​L+​f\|f\|\_{H^{-1}}^{2}=f^{\top}L^{+}f with L+⪰0L^{+}\succeq 0 fixed. We weight it more at short τ\tau:

|  |  |  |
| --- | --- | --- |
|  | ℛDW​(a)=12​∑g:τg​gridλDW​(τg)​‖(E​a)g‖H−12,λDW​(τ)=λDW(0)​min⁡{1,τ⋆/τ},\mathcal{R}\_{\mathrm{DW}}(a)\;=\;\frac{1}{2}\sum\_{g:\,\tau\_{g}\ \text{grid}}\lambda\_{\mathrm{DW}}(\tau\_{g})\,\|(Ea)\_{g}\|\_{H^{-1}}^{2},\qquad\lambda\_{\mathrm{DW}}(\tau)=\lambda\_{\mathrm{DW}}^{(0)}\min\{1,\tau\_{\star}/\tau\}, |  |

where E​aEa stacks AK​K​aA\_{KK}a slice–wise. This biases the optimiser toward *spreading* density
rather than oscillating it in short strips, eliminating spurious negative lobes.

### 10.4  Convexity and invariance

Each addend in this chapter is a sum of squares of affine functions of aa (or a congruence of a
fixed SPD quadratic), hence convex and QP–compatible. Under the Λ\Lambda–module
(§[6.2](https://arxiv.org/html/2512.01967v1#Ch6.S2 "6.2 Λ–module: price–invariant reparameterisation ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), post–multiply all blocks by UU and replace Λ\Lambda by
Λ~=U⊤​Λ​U\widetilde{\Lambda}=U^{\top}\Lambda U; penalty values on (A​a,Aτ|K​a,AK​K​a)(Aa,A\_{\tau|K}a,A\_{KK}a) are unchanged.

### 10.5  Practical choices and interaction with scaling

* •

  Window: τ⋆=5\tau\_{\star}=5–1010 trading days. Apply ([10.1](https://arxiv.org/html/2512.01967v1#Ch10.E1 "Equation 10.1 ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) only on
  Γ0+\Gamma\_{0^{+}}; optionally exclude an ATM tube |m|≤c​τ|m|\leq c\sqrt{\tau}.
* •

  Weights: Choose λRN\lambda\_{\mathrm{RN}} so that the RMS of A​a−C0+Aa-C\_{0^{+}} on
  Γ0+\Gamma\_{0^{+}} matches the median band width there; choose ηRN\eta\_{\mathrm{RN}} to bring short–end
  calendar violations under the global 1%1\% budget when combined with the scaled
  no–arb penalties (§[9](https://arxiv.org/html/2512.01967v1#Ch9 "9. Scaling, schedules, and the 𝜇-controller ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). Use the short–maturity ramps
  λΩ​(τ)\lambda\_{\Omega}(\tau) and λDW​(τ)\lambda\_{\mathrm{DW}}(\tau) above.
* •

  Row scaling: Apply the same p95 row scaling (§[9](https://arxiv.org/html/2512.01967v1#Ch9 "9. Scaling, schedules, and the 𝜇-controller ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) to
  Aτ|KA\_{\tau|K} when used inside ([10.1](https://arxiv.org/html/2512.01967v1#Ch10.E1 "Equation 10.1 ‣ 10.1 Boundary anchoring and calendar flattening on Γ_0⁺ ‣ 10. Short-maturity remedy ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")); this keeps the knob ηRN\eta\_{\mathrm{RN}}
  comparable to λNA\lambda\_{\mathrm{NA}}.

## 11.  Diagnostics and Implementation

### 11.1  Structure monitors

We carry a set of diagnostics that do not enter the optimisation but certify stability.

##### MON1 (symplectic/volume/reversibility).

If an auxiliary Hamiltonian stepper is used (e.g. to generate UU or kicks),
we compute the discrete symplectic defect and the map‐determinant on random probes.
Both are monitor scalars and must remain below pre‐set tolerances.

##### MON2 (RN residual/commuting defect).

Report *RN residual*
‖A​a−C0+‖Γ0+\norm{Aa-C\_{0^{+}}}\_{\Gamma\_{0^{+}}},
and *calendar commutator*
‖C​(A​a)‖2\norm{C(Aa)}\_{2} on the grid, where
C:=A~τ|K​A~K−A~K​A~τ|K∈ℝG×GC:=\widetilde{A}\_{\tau|K}\widetilde{A}\_{K}-\widetilde{A}\_{K}\widetilde{A}\_{\tau|K}\in\mathbb{R}^{G\times G} is the grid-space commutator from
Section [6.5](https://arxiv.org/html/2512.01967v1#Ch6.S5 "6.5 Ω–module: high–frequency taper and commutator hook ‣ 6. Ridge, spectral geometry, and transport regularisation ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

##### MON3 (aliasing).

Let ℰhi\mathcal{E}\_{\text{hi}} be the share of modal energy in the upper third of
(k,ℓ)(k,\ell) indices. Large values predict convexity noise; the Ω\Omega penalty is tuned to
cap ℰhi\mathcal{E}\_{\text{hi}}.

##### Q (Egorov bridge).

Under short‐time linearisation, classical transport of observables commutes with
quantum propagation up to 𝒪​(τ)\mathcal{O}(\tau) (Egorov’s theorem).
We monitor the deviation of CfC\_{f} pushed through the (linearised) forward drift
versus the surface rebuilt at τ+δ​τ\tau+\delta\tau; the resulting defect is reported
as absolute/relative scalars. (Purely diagnostic; no constraints are added.)

### 11.2  Implementation notes

* •

  Basis sizes: K∈[28,40]K\!\in[28,40], L∈[22,32]L\!\in[22,32]; grid G≈(2​K)×(2​L)G\!\approx\!(2K){\times}(2L).
* •

  Scaling: row p95 to 1; convexity block optionally scaled by a small boost (×2\times 2–55).
* •

  Penalties: λNA\lambda\_{\text{NA}} via short probe; λridge\lambda\_{\text{ridge}} by GCV on a random 8% subsample.
* •

  Short–maturity: set τ⋆≈\tau\_{\star}\approx 5–10 trading days; ramp λRN,λΩ,λDW\lambda\_{\text{RN}},\lambda\_{\Omega},\lambda\_{\text{DW}} to zero after 2​τ⋆2\tau\_{\star}.
* •

  Solver: OSQP with εabs=εrel=4.5×10−7\varepsilon\_{\text{abs}}=\varepsilon\_{\text{rel}}=4.5\times 10^{-7}, adaptive ρ\rho (default 0.10.1), polishing enabled, and a 900-second time cap; other options stay at their defaults.

## 12.  Hamiltonian Fog Post-Fit in Price Space

The global Chebyshev–QP fit constructed in the previous Chapters already enforces
static no–arbitrage on a dense collocation grid and is tuned to achieve
approximately 99%99\% within–band coverage with at most 1%1\% grid violations.
However, some trading dates and regions of the (m,τ)(m,\tau)–plane
remain unsatisfactory even after the main fit and
the short–maturity remedy.

The main QP already delivers a strong baseline surface on most dates. For *calm* years such as 2019 and 2022-23, a single choice of μ\mu and λN​A\lambda\_{NA} is enough to reach the target.
In these regimes, the badness field ω\omega is close to zero everywhere, so any local post-fit is minimal.

However, in 2020-21 quotes are noisier, and cross-sectional inconsistencies between strikes and maturities are more common. On these stressed dates, the baseline QP is forced into local compromises (either coverage or no-arbitrage deteriorates). Empirically, the misfit is concentrated in small regions.

In this chapter, we describe a second *local* post-fit layer that takes, for
each trading date tt, a forward-discounted option baseline surface
Cf0​(m,τ)C\_{f}^{0}(m,\tau) and returns a corrected nodal surface ut⋆u\_{t}^{\star} on a
structured (m,τ)(m,\tau)-grid. The post-fit acts only on regions where the baseline
fit is locally problematic (poor band coverage and/or fragile static
no-arbitrage).

### 12.1  Baseline grid surface and quotes

Fix a trading date tt and let

|  |  |  |
| --- | --- | --- |
|  | 𝒢:={(mi,τj):i=1,…,nm,j=1,…,nτ}\mathcal{G}:=\{(m\_{i},\tau\_{j}):i=1,\dots,n\_{m},\ j=1,\dots,n\_{\tau}\} |  |

be a structured working grid in log-moneyness mm and maturity τ\tau. Denote its
cardinality by

|  |  |  |
| --- | --- | --- |
|  | G:=|𝒢|=nm​nτ,G:=|\mathcal{G}|=n\_{m}n\_{\tau}, |  |

fixing any one-to-one enumeration of 𝒢\mathcal{G} by indices
g∈{1,…,G}↔(i​(g),j​(g))∈𝒢g\in\{1,\dots,G\}\leftrightarrow(i(g),j(g))\in\mathcal{G}.

Let Cf0​(m,τ)C\_{f}^{0}(m,\tau) be the baseline forward-discounted call surface obtained from
the main QP fit on date tt. The corresponding nodal values on 𝒢\mathcal{G} are given by

|  |  |  |
| --- | --- | --- |
|  | ui,j0:=Cf0​(mi,τj),(i,j)∈𝒢.u^{0}\_{i,j}:=C\_{f}^{0}(m\_{i},\tau\_{j}),\qquad(i,j)\in\mathcal{G}. |  |

Collecting them into a vector, we obtain u0∈ℝGu^{0}\in\mathbb{R}^{G}.

For the same date tt, consider a set of cleaned forward-discounted quote bands

|  |  |  |
| --- | --- | --- |
|  | {(mq,τq,bq,aq)}q=1Q,0≤bq≤aq,\{(m\_{q},\tau\_{q},b\_{q},a\_{q})\}\_{q=1}^{Q},\qquad 0\leq b\_{q}\leq a\_{q}, |  |

where (mq,τq)(m\_{q},\tau\_{q}) denotes the quote location in (m,τ)(m,\tau) and
[bq,aq][b\_{q},a\_{q}] is the corresponding bid–ask interval in forward-discounted units.

Let S∈ℝQ×GS\in\mathbb{R}^{Q\times G} be the (fixed) bilinear interpolation operator
that maps nodal values on 𝒢\mathcal{G} to model prices at the quote locations.
For any nodal field u∈ℝGu\in\mathbb{R}^{G} we write

|  |  |  |
| --- | --- | --- |
|  | Cq​(u):=(S​u)q,q=1,…,Q,C\_{q}(u):=(Su)\_{q},\qquad q=1,\dots,Q, |  |

so Cq​(u)C\_{q}(u) is the model forward-discounted call price at (mq,τq)(m\_{q},\tau\_{q}) implied
by the nodal surface uu.

### 12.2  Badness map and patch decomposition

We now detect where the baseline surface is locally problematic.

###### Definition 5 (Baseline band misfit).

For each quote q∈{1,…,Q}q\in\{1,\dots,Q\}, the baseline band violation is defined as

|  |  |  |
| --- | --- | --- |
|  | dq​(u0):=dist⁡((S​u0)q,[bq,aq])=max⁡{bq−(S​u0)q, 0,(S​u0)q−aq}≥0.d\_{q}(u^{0}):=\operatorname{dist}\big((Su^{0})\_{q},\ [b\_{q},a\_{q}]\big)=\max\{b\_{q}-(Su^{0})\_{q},\ 0,\ (Su^{0})\_{q}-a\_{q}\}\geq 0. |  |

Collecting all quote-wise misfits into a vector

|  |  |  |
| --- | --- | --- |
|  | d​(u0):=(dq​(u0))q=1Q∈ℝ≥0Q,d(u^{0}):=\big(d\_{q}(u^{0})\big)\_{q=1}^{Q}\in\mathbb{R}^{Q}\_{\geq 0}, |  |

regard d​(u0)d(u^{0}) as the baseline distance-to-band profile at the true quote locations.

We transport these quote-level misfits to the working grid 𝒢\mathcal{G} via a fixed
linear operator

|  |  |  |
| --- | --- | --- |
|  | Rband∈ℝG×Q,R^{\mathrm{band}}\in\mathbb{R}^{G\times Q}, |  |

(for example by locally averaging nearby quotes around each grid node). The purpose is to observe these violations at the grid nodes rather than at the quote locations. We write

|  |  |  |
| --- | --- | --- |
|  | wband:=Rband​d​(u0)∈ℝG,wi,jband≥0,(i,j)∈𝒢.w^{\mathrm{band}}:=R^{\mathrm{band}}d(u^{0})\in\mathbb{R}^{G},\qquad w^{\mathrm{band}}\_{i,j}\geq 0,\ (i,j)\in\mathcal{G}. |  |

In practice the entries of RbandR^{\mathrm{band}} are chosen nonnegative and supported
only on quotes (mq,τq)(m\_{q},\tau\_{q}) lying in a small neighbourhood of (mi,τj)(m\_{i},\tau\_{j}), so
that wi,jbandw^{\mathrm{band}}\_{i,j} is a local aggregated band-misfit around that node.

Next, build a single scalar at each grid node to see how badly the baseline surface u0u^{0} violates static no-arbitrage at that grid node. Let wnoarb∈ℝ≥0Gw^{\mathrm{noarb}}\in\mathbb{R}^{G}\_{\geq 0} be any nonnegative
*static no-arbitrage defect field* obtained by aggregating local violations of
discrete bounds, strike monotonicity, strike convexity, and calendar monotonicity
on the grid when evaluated at u0u^{0}. Concretely, one may define at each node
(i,j)(i,j):

###### Definition 6 (Bound violation vi,jbndv^{\mathrm{bnd}}\_{i,j}).

Bounds are 0≤ui,j0≤Fi,j0\leq u^{0}\_{i,j}\leq F\_{i,j}. At each node, define the distance to the interval [0,Fi,j][0,F\_{i,j}]

|  |  |  |
| --- | --- | --- |
|  | vi,jbnd=max⁡{−ui,j0, 0,ui,j0−Fi,j}.v^{\mathrm{bnd}}\_{i,j}=\max\big\{-u^{0}\_{i,j},\;0,\;u^{0}\_{i,j}-F\_{i,j}\big\}. |  |

Therefore,

* •

  If ui,j0∈[0,Fi,j]u^{0}\_{i,j}\in[0,F\_{i,j}], then vi,jbnd=0v^{\mathrm{bnd}}\_{i,j}=0.
* •

  If ui,j0<0u^{0}\_{i,j}<0, then vi,jbnd=−ui,j0v^{\mathrm{bnd}}\_{i,j}=-u^{0}\_{i,j}.
* •

  If ui,j0>Fi,ju^{0}\_{i,j}>F\_{i,j}, then vi,jbnd=ui,j0−Fi,jv^{\mathrm{bnd}}\_{i,j}=u^{0}\_{i,j}-F\_{i,j}.

###### Definition 7 (Strike monotonicity violation vi,jmonov^{\mathrm{mono}}\_{i,j}).

Static no-arbitrage requires call prices to be non-increasing in strike at fixed maturity. On the grid,
this means that along each maturity slice jj we should have

|  |  |  |
| --- | --- | --- |
|  | ui+1,j0−ui,j0≤0,i=1,…,nm−1.u^{0}\_{i+1,j}-u^{0}\_{i,j}\leq 0,\qquad i=1,\dots,n\_{m}-1. |  |

Define the forward slope in mm between nodes ii and i+1i+1 by

|  |  |  |
| --- | --- | --- |
|  | Δi+12,jmono:=ui+1,j0−ui,j0,i=1,…,nm−1.\Delta^{\mathrm{mono}}\_{i+\frac{1}{2},j}:=u^{0}\_{i+1,j}-u^{0}\_{i,j},\qquad i=1,\dots,n\_{m}-1. |  |

If Δi+12,jmono≤0\Delta^{\mathrm{mono}}\_{i+\frac{1}{2},j}\leq 0, there is no monotonicity issue on that edge; if
Δi+12,jmono>0\Delta^{\mathrm{mono}}\_{i+\frac{1}{2},j}>0, the price goes up in strike there (violation).
Define the edge violation

|  |  |  |
| --- | --- | --- |
|  | di+12,jmono:=max⁡{Δi+12,jmono, 0}.d^{\mathrm{mono}}\_{i+\frac{1}{2},j}:=\max\big\{\Delta^{\mathrm{mono}}\_{i+\frac{1}{2},j},\,0\big\}. |  |

We then attach a node-based violation by aggregating the incident edges. For interior nodes
2≤i≤nm−12\leq i\leq n\_{m}-1,

|  |  |  |
| --- | --- | --- |
|  | vi,jmono:=max⁡{di−12,jmono,di+12,jmono},v^{\mathrm{mono}}\_{i,j}:=\max\big\{d^{\mathrm{mono}}\_{i-\frac{1}{2},j},d^{\mathrm{mono}}\_{i+\frac{1}{2},j}\big\}, |  |

and at the boundaries we use the single available edge,

|  |  |  |
| --- | --- | --- |
|  | v1,jmono:=d1+12,jmono,vnm,jmono:=dnm−12,jmono.v^{\mathrm{mono}}\_{1,j}:=d^{\mathrm{mono}}\_{1+\frac{1}{2},j},\qquad v^{\mathrm{mono}}\_{n\_{m},j}:=d^{\mathrm{mono}}\_{n\_{m}-\frac{1}{2},j}. |  |

Thus,

* •

  If all nearby slopes around (i,j)(i,j) are non-positive, then vi,jmono=0v^{\mathrm{mono}}\_{i,j}=0.
* •

  If some local slope is upward, vi,jmonov^{\mathrm{mono}}\_{i,j} records the largest upward jump
  touching that node.

###### Definition 8 (Strike convexity violation vi,jconvv^{\mathrm{conv}}\_{i,j}).

Static no-arbitrage also requires convexity in strike. On a uniform mm-grid, this is encoded by
non-negative second differences

|  |  |  |
| --- | --- | --- |
|  | Δi,j2:=ui+1,j0−2​ui,j0+ui−1,j0≥0,i=2,…,nm−1.\Delta^{2}\_{i,j}:=u^{0}\_{i+1,j}-2u^{0}\_{i,j}+u^{0}\_{i-1,j}\geq 0,\qquad i=2,\dots,n\_{m}-1. |  |

Define the convexity defect at the central node by

|  |  |  |
| --- | --- | --- |
|  | vi,jconv:={max⁡{−Δi,j2, 0},2≤i≤nm−1,0,i=1​ or ​i=nm​ (no centred stencil).v^{\mathrm{conv}}\_{i,j}:=\begin{cases}\max\big\{-\Delta^{2}\_{i,j},\,0\big\},&2\leq i\leq n\_{m}-1,\\[3.0pt] 0,&i=1\text{ or }i=n\_{m}\text{ (no centred stencil).}\end{cases} |  |

Therefore,

* •

  If Δi,j2≥0\Delta^{2}\_{i,j}\geq 0, there is no convexity issue and vi,jconv=0v^{\mathrm{conv}}\_{i,j}=0.
* •

  If Δi,j2<0\Delta^{2}\_{i,j}<0, the profile is locally concave in strike (violation) and
  vi,jconv=−Δi,j2v^{\mathrm{conv}}\_{i,j}=-\Delta^{2}\_{i,j} measures how badly convexity is violated.

On a non-uniform mm-grid one can replace Δi,j2\Delta^{2}\_{i,j} by the standard three-point
second-derivative formula with unequal spacings; for the purposes of constructing a badness
indicator wnoarbw^{\mathrm{noarb}} the simple second difference is typically sufficient.

###### Definition 9 (Calendar violation vi,jcalv^{\mathrm{cal}}\_{i,j} via Aτ|KA\_{\tau|K}).

Let a⋆a^{\star} be the baseline coefficient vector and let Aτ|KA\_{\tau|K} be the
calendar operator at fixed strike.
Evaluate

|  |  |  |
| --- | --- | --- |
|  | h:=Aτ|K​a⋆∈ℝG,h:=A\_{\tau|K}a^{\star}\in\mathbb{R}^{G}, |  |

and reshape hh on the grid as hi,jh\_{i,j}.
Define the node-wise calendar defect by

|  |  |  |
| --- | --- | --- |
|  | vi,jcal:=max⁡{−hi,j, 0}.v^{\mathrm{cal}}\_{i,j}:=\max\{-h\_{i,j},\,0\}. |  |

Then vi,jcal=0v^{\mathrm{cal}}\_{i,j}=0 whenever (∂τCf)​(K,τ)|K≥0(\partial\_{\tau}C\_{f})(K,\tau)\big|\_{K}\geq 0
at (mi,τj)(m\_{i},\tau\_{j}), and vi,jcalv^{\mathrm{cal}}\_{i,j} measures the local size of negative
calendar slopes at fixed strike.

With the bound violation vi,jbndv^{\mathrm{bnd}}\_{i,j}, strike monotonicity violation vi,jmonov^{\mathrm{mono}}\_{i,j}, strike convexity violation vi,jconvv^{\mathrm{conv}}\_{i,j} and calendar violation vi,jcalv^{\mathrm{cal}}\_{i,j} define the static no-arbitrage defect field wnoarbw^{\mathrm{noarb}}.

###### Definition 10 (Static no-arbitrage defect field wnoarbw^{\mathrm{noarb}}).

Given the node-wise violations

|  |  |  |
| --- | --- | --- |
|  | vi,jbnd,vi,jmono,vi,jconv,vi,jcal≥0,v^{\mathrm{bnd}}\_{i,j},\quad v^{\mathrm{mono}}\_{i,j},\quad v^{\mathrm{conv}}\_{i,j},\quad v^{\mathrm{cal}}\_{i,j}\ \geq 0, |  |

defined respectively for bounds, strike monotonicity, strike convexity, and calendar
constraints at (mi,τj)(m\_{i},\tau\_{j}), the *static no-arbitrage defect field* is

|  |  |  |
| --- | --- | --- |
|  | wi,jnoarb:=max⁡{vi,jbnd,vi,jmono,vi,jconv,vi,jcal},(i,j)∈𝒢.w^{\mathrm{noarb}}\_{i,j}:=\max\big\{v^{\mathrm{bnd}}\_{i,j},v^{\mathrm{mono}}\_{i,j},v^{\mathrm{conv}}\_{i,j},v^{\mathrm{cal}}\_{i,j}\big\},\qquad(i,j)\in\mathcal{G}. |  |

Thus wi,jnoarb≥0w^{\mathrm{noarb}}\_{i,j}\geq 0 for all (i,j)(i,j), and
wi,jnoarb=0w^{\mathrm{noarb}}\_{i,j}=0 whenever all discrete no-arbitrage inequalities
(bounds, strike monotonicity, strike convexity, and calendar monotonicity) hold
without violation in a neighbourhood of (mi,τj)(m\_{i},\tau\_{j}).

Any alternative construction of a field wnoarb∈ℝ≥0Gw^{\mathrm{noarb}}\in\mathbb{R}^{G}\_{\geq 0}
with the same qualitative properties

* •

  wi,jnoarb≥0w^{\mathrm{noarb}}\_{i,j}\geq 0 for all (i,j)(i,j), and
* •

  wi,jnoarb=0w^{\mathrm{noarb}}\_{i,j}=0 whenever all discrete no-arbitrage
  inequalities are satisfied (with margin) near (mi,τj)(m\_{i},\tau\_{j}),

is equally admissible for the purposes of the badness map construction below.

The band-misfit field wbandw^{\mathrm{band}} and the static no-arbitrage defect field
wnoarbw^{\mathrm{noarb}} provide two complementary scalar diagnostics on the grid
𝒢\mathcal{G}: the former reflects how hard it is for the baseline surface to
respect the bid-ask bands, while the latter reflects how fragile the static
shape constraints are in a neighborhood of each node. For the purposes of
patch detection we now compress these two pieces of information into a single
scalar badness field on 𝒢\mathcal{G}, allowing for a tunable trade-off
between band fit and no-arbitrage robustness.

###### Definition 11 (Raw and smoothed badness field).

Fix positive scalars αband,αnoarb>0\alpha\_{\mathrm{band}},\alpha\_{\mathrm{noarb}}>0. The
*raw badness field* on 𝒢\mathcal{G} is

|  |  |  |
| --- | --- | --- |
|  | w~i,j:=αbandwi,jband+αnoarbwi,jnoarb,(i,j)∈𝒢.\tilde{w}\_{i,j}:=\alpha\_{\mathrm{band}}\,w^{\mathrm{band}}\_{i,j}+\alpha\_{\mathrm{noarb}}\,w^{\mathrm{noarb}}\_{i,j},\qquad(i,j)\in\mathcal{G}. |  |

Let KσK\_{\sigma} be a fixed separable Gaussian kernel on the grid,
Kσ​(i,j)=kσ(m)​(i)​kσ(τ)​(j)K\_{\sigma}(i,j)=k\_{\sigma}^{(m)}(i)\,k\_{\sigma}^{(\tau)}(j), and let
∗\* denote discrete convolution on 𝒢\mathcal{G}:

|  |  |  |
| --- | --- | --- |
|  | (Kσ∗w~)i,j:=∑(i′,j′)∈𝒢Kσ​(i−i′,j−j′)​w~i′,j′.(K\_{\sigma}\*\tilde{w})\_{i,j}:=\sum\_{(i^{\prime},j^{\prime})\in\mathcal{G}}K\_{\sigma}(i-i^{\prime},j-j^{\prime})\,\tilde{w}\_{i^{\prime},j^{\prime}}. |  |

Define the (componentwise) clipping operator

|  |  |  |
| --- | --- | --- |
|  | Clip[0,1](x)i,j:=min{1,max{0,xi,j}}.\operatorname{Clip}\_{[0,1]}(x)\_{i,j}:=\min\{1,\max\{0,x\_{i,j}\}\}. |  |

The *smoothed badness field* is then

|  |  |  |
| --- | --- | --- |
|  | w:=Clip[0,1]⁡(Kσ∗w~)∈[0,1]G.w:=\operatorname{Clip}\_{[0,1]}(K\_{\sigma}\*\tilde{w})\ \in\ [0,1]^{G}. |  |

The fixed separable Gaussian kernel on the grid KσK\_{\sigma} is a bell-shaped weight function centered at 0 and decaying as you move away. Separable means that it can factor into a product of a 1D kernel in mm and a 1D kernel inn τ\tau.
The convolution (Kσ∗w~)i,j(K\_{\sigma}\*\tilde{w})\_{i,j} is a weighted average of the raw badness w~i,j\tilde{w}\_{i,j} in a neighborhood of (i,j)(i,j) with weights given by the Gaussian kernel evaluated at offsets (i−i′,j−j′)(i-i^{\prime},j-j^{\prime}).

###### Example 12 (Single Spike).

Consider a 1D grid with indices i=1,…,7i=1,\dots,7 and a raw badness vector

|  |  |  |
| --- | --- | --- |
|  | w~=(0, 0, 0, 1, 0, 0, 0),\tilde{w}=(0,\ 0,\ 0,\ 1,\ 0,\ 0,\ 0), |  |

so there is a single spike of badness at i=4i=4. Take a simple discrete kernel

|  |  |  |
| --- | --- | --- |
|  | K=(14,12,14),K=\Big(\tfrac{1}{4},\ \tfrac{1}{2},\ \tfrac{1}{4}\Big), |  |

interpreted as K​(−1)=14K(-1)=\tfrac{1}{4}, K​(0)=12K(0)=\tfrac{1}{2}, K​(1)=14K(1)=\tfrac{1}{4}, and K​(k)=0K(k)=0
for |k|>1|k|>1. The convolution (K∗w~)i(K\*\tilde{w})\_{i} with zero-padding at the
boundaries is

|  |  |  |
| --- | --- | --- |
|  | (K∗w~)i=14​w~i−1+12​w~i+14​w~i+1,i=1,…,7.(K\*\tilde{w})\_{i}=\tfrac{1}{4}\,\tilde{w}\_{i-1}+\tfrac{1}{2}\,\tilde{w}\_{i}+\tfrac{1}{4}\,\tilde{w}\_{i+1},\qquad i=1,\dots,7. |  |

A direct computation gives

|  |  |  |
| --- | --- | --- |
|  | (K∗w~)=(0, 0, 0.25, 0.5, 0.25, 0, 0).(K\*\tilde{w})=(0,\ 0,\ 0.25,\ 0.5,\ 0.25,\ 0,\ 0). |  |

Thus the original spike of height 11 at i=4i=4 is smoothed into a smaller peak
of height 0.50.5 at i=4i=4 with nonzero neighbours of height 0.250.25 at i=3i=3 and
i=5i=5: the mass has been spread out and diluted.

###### Example 13 (Cluster).

Now consider a cluster of three bad nodes

|  |  |  |
| --- | --- | --- |
|  | w~=(0, 0, 1, 1, 1, 0, 0),\tilde{w}=(0,\ 0,\ 1,\ 1,\ 1,\ 0,\ 0), |  |

again on indices i=1,…,7i=1,\dots,7, with the same kernel

|  |  |  |
| --- | --- | --- |
|  | K=(14,12,14).K=\Big(\tfrac{1}{4},\ \tfrac{1}{2},\ \tfrac{1}{4}\Big). |  |

Using the same convolution formula

|  |  |  |
| --- | --- | --- |
|  | (K∗w~)i=14​w~i−1+12​w~i+14​w~i+1,i=1,…,7,(K\*\tilde{w})\_{i}=\tfrac{1}{4}\,\tilde{w}\_{i-1}+\tfrac{1}{2}\,\tilde{w}\_{i}+\tfrac{1}{4}\,\tilde{w}\_{i+1},\qquad i=1,\dots,7, |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | (K∗w~)2\displaystyle(K\*\tilde{w})\_{2} | =14⋅0+12⋅0+14⋅1=0.25,\displaystyle=\tfrac{1}{4}\cdot 0+\tfrac{1}{2}\cdot 0+\tfrac{1}{4}\cdot 1=25, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (K∗w~)3\displaystyle(K\*\tilde{w})\_{3} | =14⋅0+12⋅1+14⋅1=0.75,\displaystyle=\tfrac{1}{4}\cdot 0+\tfrac{1}{2}\cdot 1+\tfrac{1}{4}\cdot 1=75, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (K∗w~)4\displaystyle(K\*\tilde{w})\_{4} | =14⋅1+12⋅1+14⋅1=1.00,\displaystyle=\tfrac{1}{4}\cdot 1+\tfrac{1}{2}\cdot 1+\tfrac{1}{4}\cdot 1=00, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (K∗w~)5\displaystyle(K\*\tilde{w})\_{5} | =14⋅1+12⋅1+14⋅0=0.75,\displaystyle=\tfrac{1}{4}\cdot 1+\tfrac{1}{2}\cdot 1+\tfrac{1}{4}\cdot 0=75, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (K∗w~)6\displaystyle(K\*\tilde{w})\_{6} | =14⋅1+12⋅0+14⋅0=0.25,\displaystyle=\tfrac{1}{4}\cdot 1+\tfrac{1}{2}\cdot 0+\tfrac{1}{4}\cdot 0=25, |  |

and (K∗w~)1=(K∗w~)7=0(K\*\tilde{w})\_{1}=(K\*\tilde{w})\_{7}=0. Hence

|  |  |  |
| --- | --- | --- |
|  | (K∗w~)=(0, 0.25, 0.75, 1.0, 0.75, 0.25, 0).(K\*\tilde{w})=(0,\ 0.25,\ 0.75,\ 1.0,\ 0.75,\ 0.25,\ 0). |  |

In this case a contiguous cluster of bad nodes remains a single coherent bump:
the central node retains height 11 and its neighbours are only slightly
reduced to 0.750.75, while a halo of smaller values 0.250.25 appears around the
cluster. This illustrates how Gaussian smoothing preserves genuine regions of
badness while softening their edges and suppressing isolated spikes.

Therefore, a single noisy spike in w~\tilde{w} will spread out to neighbors, clusters of large w~\tilde{w} will be smoothed into a broader hot region rather than an isolated piece and a smooth, spatially coherent badness image is created.

The clipping operator is applied to obtain a dimensionless, bounded heatmap which is comparable across dates and assets. One can therefore chose a threshold θ∈(0,1)\theta\in(0,1) and obtain patches from the connected components of {ωi,j>θ}\{\omega\_{i,j}>\theta\}. Moreover, the smoothing step ensures that patches correspond to regions rather than isolated single nodes.

Graphically, ww can be viewed as a heatmap on the (m,τ)(m,\tau)-plane:
nodes with wi,j≈0w\_{i,j}\approx 0 are locally well-behaved (good band coverage and
robust static no-arbitrage), while nodes with wi,jw\_{i,j} close to 11 lie in fragile or hard-to-fit regions.

mmτ\tauΩp\Omega\_{p}darker = larger wi,jw\_{i,j}lighter = smaller wi,jw\_{i,j}


Figure 12.1: Schematic badness map wi,jw\_{i,j} on the (m,τ)(m,\tau) grid 𝒢\mathcal{G}.
Darker cells indicate regions where the smoothed badness field is large; a
connected high-badness region is shown as a patch Ωp\Omega\_{p}.

We now threshold ww and decompose the high-badness region into connected
components.

###### Definition 14 (Active set and patches).

Fix a threshold θ∈(0,1)\theta\in(0,1). The *active set* is

|  |  |  |
| --- | --- | --- |
|  | A:={(i,j)∈𝒢:wi,j>θ}.A:=\{(i,j)\in\mathcal{G}:w\_{i,j}>\theta\}. |  |

Equip 𝒢\mathcal{G} with a nearest-neighbour graph structure, either
*4-neighbour* (edges between (i,j)(i,j) and (i±1,j)(i\pm 1,j), (i,j±1)(i,j\pm 1)) or
*8-neighbour* (4-neighbour plus diagonals (i±1,j±1)(i\pm 1,j\pm 1)). Two nodes of
AA are said to be connected if they are joined by a path of neighbours in this
graph. The connected components of AA are then

|  |  |  |
| --- | --- | --- |
|  | A=⨆p∈𝒫Ωp,A=\bigsqcup\_{p\in\mathcal{P}}\Omega\_{p}, |  |

where each Ωp⊂𝒢\Omega\_{p}\subset\mathcal{G} is a maximal connected subset of AA
(with respect to the chosen neighbourhood) and is called a *patch*.

Nodes in ⋃pΩp\bigcup\_{p}\Omega\_{p} belong to locally difficult regions and are candidates
for post-fit adjustment; nodes in
𝒢∖⋃pΩp\mathcal{G}\setminus\bigcup\_{p}\Omega\_{p} are left unchanged by the post-fit. The
construction is entirely local and depends only on the baseline misfit and static
defect fields at the given date, not on the calendar regime; both calm and stressed
dates are treated identically.

From now on we fix a single patch Ω⊂𝒢\Omega\subset\mathcal{G} and describe the
patch-level post-fit problem.

### 12.3  Discrete 3D fog on (m,τ,u)(m,\tau,u)

On a fixed patch Ω⊂𝒢\Omega\subset\mathcal{G} we will represent local pricing
uncertainty and potential quote noise by a discretised probability density over
the three-dimensional space (m,τ,u)(m,\tau,u), where uu denotes forward-discounted
call price.

#### 12.3.1 3D lattice and fog variables

###### Definition 15 (3D fog lattice).

Let Ω⊂𝒢\Omega\subset\mathcal{G} be a patch with cardinality NΩ:=|Ω|N\_{\Omega}:=|\Omega|.
Fix a finite, strictly increasing sequence of price levels

|  |  |  |
| --- | --- | --- |
|  | U:={uk}k=1nu⊂ℝ,u1<u2<⋯<unu,U:=\{u\_{k}\}\_{k=1}^{n\_{u}}\subset\mathbb{R},\qquad u\_{1}<u\_{2}<\dots<u\_{n\_{u}}, |  |

spanning a relevant price range (for example from 0 up to a suitable multiple
of the local forward). The associated three-dimensional lattice of
(m,τ,u)(m,\tau,u)-nodes on Ω\Omega is

|  |  |  |
| --- | --- | --- |
|  | ℒΩ:={(i,j,k):(i,j)∈Ω,k=1,…,nu}.\mathcal{L}\_{\Omega}:=\{(i,j,k):(i,j)\in\Omega,\ k=1,\dots,n\_{u}\}. |  |

###### Definition 16 (Fog variables and normalisation).

For each (i,j,k)∈ℒΩ(i,j,k)\in\mathcal{L}\_{\Omega} introduce a nonnegative *fog
variable* πi,j,k≥0\pi\_{i,j,k}\geq 0. Collecting all such variables into a single vector

|  |  |  |
| --- | --- | --- |
|  | π:=(πi,j,k)(i,j,k)∈ℒΩ∈ℝNΩ​nu,\pi:=(\pi\_{i,j,k})\_{(i,j,k)\in\mathcal{L}\_{\Omega}}\in\mathbb{R}^{N\_{\Omega}n\_{u}}, |  |

we impose the global normalisation

|  |  |  |
| --- | --- | --- |
|  | ∑(i,j)∈Ω∑k=1nuπi,j,k=1.\sum\_{(i,j)\in\Omega}\sum\_{k=1}^{n\_{u}}\pi\_{i,j,k}=1. |  |

The associated feasible set of fog configurations on Ω\Omega is the simplex

|  |  |  |
| --- | --- | --- |
|  | 𝒞π​(Ω):={π∈ℝ≥0NΩ​nu:∑(i,j)∈Ω∑k=1nuπi,j,k=1}.\mathcal{C}\_{\pi}(\Omega):=\Big\{\pi\in\mathbb{R}^{N\_{\Omega}n\_{u}}\_{\geq 0}:\sum\_{(i,j)\in\Omega}\sum\_{k=1}^{n\_{u}}\pi\_{i,j,k}=1\Big\}. |  |

Thus π\pi is a discrete probability measure on the finite set ℒΩ\mathcal{L}\_{\Omega}:
each πi,j,k\pi\_{i,j,k} is the probability mass (or fog mass) attached to the node
(mi,τj,uk)(m\_{i},\tau\_{j},u\_{k}), and 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) is a standard (NΩ​nu−1)(N\_{\Omega}n\_{u}-1)-dimensional
simplex.

At fixed (i,j)∈Ω(i,j)\in\Omega, the vertical profile

|  |  |  |
| --- | --- | --- |
|  | {πi,j,k}k=1nu\{\pi\_{i,j,k}\}\_{k=1}^{n\_{u}} |  |

describes the distribution of fog across price levels {uk}\{u\_{k}\} at that grid
location. In particular, we may interpret:

* •

  πi,j,k\pi\_{i,j,k} large for some kk as assigning high plausibility to local
  prices near uku\_{k} at (mi,τj)(m\_{i},\tau\_{j});
* •

  a spread-out vertical profile as expressing substantial local uncertainty
  over uu;
* •

  a concentrated profile as expressing locally precise information.

#### 12.3.2 2D noise marginal on the patch

###### Definition 17 (2D marginal noise density).

Given π∈𝒞π​(Ω)\pi\in\mathcal{C}\_{\pi}(\Omega), define the *2D marginal* of the fog
on Ω\Omega by

|  |  |  |
| --- | --- | --- |
|  | ni,j:=∑k=1nuπi,j,k,(i,j)∈Ω.n\_{i,j}:=\sum\_{k=1}^{n\_{u}}\pi\_{i,j,k},\qquad(i,j)\in\Omega. |  |

The marginal n:=(ni,j)(i,j)∈Ωn:=(n\_{i,j})\_{(i,j)\in\Omega} satisfies

|  |  |  |
| --- | --- | --- |
|  | ni,j≥0,∑(i,j)∈Ωni,j=1,n\_{i,j}\geq 0,\qquad\sum\_{(i,j)\in\Omega}n\_{i,j}=1, |  |

and can be interpreted as a probability distribution on Ω\Omega:

|  |  |  |
| --- | --- | --- |
|  | ni,j=ℙ​{(m,τ)​ lies at node ​(mi,τj)}.n\_{i,j}=\mathbb{P}\{(m,\tau)\text{ lies at node }(m\_{i},\tau\_{j})\}. |  |

Equivalently, ni,jn\_{i,j} is the *total fog mass* sitting above (mi,τj)(m\_{i},\tau\_{j})
when one integrates out the price dimension uu.

Where ni,jn\_{i,j} is relatively large, the fog is thick in the (m,τ)(m,\tau)-plane
and the local order book in that region is regarded as noisy or unreliable;
where ni,jn\_{i,j} is small, very little fog mass resides and the local book is
regarded as comparatively clean.

When ni,j>0n\_{i,j}>0, it is often convenient to speak of the *conditional
vertical distribution* at (i,j)(i,j),

|  |  |  |
| --- | --- | --- |
|  | pi,j,k:=πi,j,kni,j,k=1,…,nu,p\_{i,j,k}:=\frac{\pi\_{i,j,k}}{n\_{i,j}},\qquad k=1,\dots,n\_{u}, |  |

which is a discrete probability distribution on {uk}\{u\_{k}\} satisfying
∑k=1nupi,j,k=1\sum\_{k=1}^{n\_{u}}p\_{i,j,k}=1. In terms of this factorisation,

|  |  |  |
| --- | --- | --- |
|  | πi,j,k=ni,j​pi,j,k,\pi\_{i,j,k}=n\_{i,j}\,p\_{i,j,k}, |  |

so that nn encodes where fog mass is located on the patch, and pp encodes
how that fog is distributed vertically in price at each node.

#### 12.3.3 Schematic geometry

The geometry of the fog on a patch can be visualised as a stack of vertical
columns above the (m,τ)(m,\tau) nodes in Ω\Omega, each column sampled at levels
{uk}\{u\_{k}\}:

mmτ\tauuuΩ\Omega


Figure 12.2: Schematic 3D fog on a patch Ω\Omega. The (m,τ)(m,\tau)-plane is spanned
by the horizontal mm-axis and the in-plane τ\tau-axis; the uu-axis is vertical.
Each node (mi,τj)∈Ω(m\_{i},\tau\_{j})\in\Omega carries a vertical column of fog mass discretised
at price levels {uk}\{u\_{k}\}. The variables πi,j,k\pi\_{i,j,k} encode the mass at
(mi,τj,uk)(m\_{i},\tau\_{j},u\_{k}); their 2D marginal ni,jn\_{i,j} is the total mass in the column
above (mi,τj)(m\_{i},\tau\_{j}).

In the optimisation below, the fog configuration π∈𝒞π​(Ω)\pi\in\mathcal{C}\_{\pi}(\Omega)
will be coupled to the nodal price field on Ω\Omega via band-based potentials
and a Hamiltonian energy, with ni,jn\_{i,j} controlling how strongly local
bid-ask information is enforced at each node.

### 12.4  Patch-level price field and static no-arbitrage

Fix a patch Ω⊂𝒢\Omega\subset\mathcal{G} with cardinality NΩ:=|Ω|N\_{\Omega}:=|\Omega| and
baseline nodal surface u0∈ℝGu^{0}\in\mathbb{R}^{G} as in Section [12.1](https://arxiv.org/html/2512.01967v1#Ch12.S1 "12.1 Baseline grid surface and quotes ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").
On Ω\Omega we will allow nodal prices to move, while all off-patch values are
kept fixed at their baseline levels. Static no-arbitrage is imposed on the
*assembled* full-grid surface.

#### 12.4.1 Interior price variables and assembly map

###### Definition 18 (Interior price variables and assembled surface).

Choose any one-to-one enumeration of the patch

|  |  |  |
| --- | --- | --- |
|  | Ω={(iℓ,jℓ)}ℓ=1NΩ⊂𝒢.\Omega=\{(i\_{\ell},j\_{\ell})\}\_{\ell=1}^{N\_{\Omega}}\subset\mathcal{G}. |  |

The *interior price vector* (unknown) on Ω\Omega is

|  |  |  |
| --- | --- | --- |
|  | uI:=(uiℓ,jℓ)ℓ=1NΩ∈ℝNΩ,u\_{I}:=(u\_{i\_{\ell},j\_{\ell}})\_{\ell=1}^{N\_{\Omega}}\in\mathbb{R}^{N\_{\Omega}}, |  |

whose entries correspond to the nodal prices on Ω\Omega. Define the *assembly map*

|  |  |  |
| --- | --- | --- |
|  | 𝒜Ω:ℝNΩ→ℝG,uI↦u​(uI),\mathcal{A}\_{\Omega}:\mathbb{R}^{N\_{\Omega}}\to\mathbb{R}^{G},\qquad u\_{I}\mapsto u(u\_{I}), |  |

by

|  |  |  |
| --- | --- | --- |
|  | u​(uI)i,j:={ui,j,(i,j)∈Ω,ui,j0,(i,j)∉Ω.u(u\_{I})\_{i,j}:=\begin{cases}u\_{i,j},&(i,j)\in\Omega,\\[3.0pt] u^{0}\_{i,j},&(i,j)\notin\Omega.\end{cases} |  |

Equivalently, if we write u∈ℝGu\in\mathbb{R}^{G} in the same enumeration as 𝒢\mathcal{G}
and let PΩ∈ℝG×NΩP\_{\Omega}\in\mathbb{R}^{G\times N\_{\Omega}} be the binary matrix that injects
uIu\_{I} into the coordinates corresponding to Ω\Omega (and zeros elsewhere), then
the assembly map can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(uI)=PΩ​uI+u0,off,u(u\_{I})=P\_{\Omega}u\_{I}+u^{0,\mathrm{off}}, |  | (12.1) |

where u0,off∈ℝGu^{0,\mathrm{off}}\in\mathbb{R}^{G} coincides with u0u^{0} on
𝒢∖Ω\mathcal{G}\setminus\Omega and is zero on Ω\Omega. Thus 𝒜Ω\mathcal{A}\_{\Omega} is an
affine map, with linear part PΩP\_{\Omega}.

#### 12.4.2 Global discrete static no-arbitrage on the grid

We recall that in Chapters [4](https://arxiv.org/html/2512.01967v1#Ch4 "4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")–[7](https://arxiv.org/html/2512.01967v1#Ch7 "7. No–arbitrage constraints and soft penalties ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") the
discrete static no-arbitrage conditions on the nodal grid 𝒢\mathcal{G} were encoded
as a finite system of linear inequalities in the full nodal vector
u∈ℝGu\in\mathbb{R}^{G}. Concretely, there exists an index set
ℐ=ℐbnd∪ℐmono∪ℐconv∪ℐcal\mathcal{I}=\mathcal{I}\_{\mathrm{bnd}}\cup\mathcal{I}\_{\mathrm{mono}}\cup\mathcal{I}\_{\mathrm{conv}}\cup\mathcal{I}\_{\mathrm{cal}} and, for each
α∈ℐ\alpha\in\mathcal{I}, a row vector ℓα⊤∈ℝ1×G\ell\_{\alpha}^{\top}\in\mathbb{R}^{1\times G}
and a scalar rα∈ℝr\_{\alpha}\in\mathbb{R} such that:

* •

  for α∈ℐbnd\alpha\in\mathcal{I}\_{\mathrm{bnd}}, the inequality
  ℓα⊤​u≤rα\ell\_{\alpha}^{\top}u\leq r\_{\alpha} encodes a bound constraint
  0≤ui,j≤Fi,j0\leq u\_{i,j}\leq F\_{i,j} at some node (i,j)∈𝒢(i,j)\in\mathcal{G};
* •

  for α∈ℐmono\alpha\in\mathcal{I}\_{\mathrm{mono}}, the inequality encodes a
  discrete strike-monotonicity condition ∂Ku≤0\partial\_{K}u\leq 0 on a maturity
  slice (e.g. ui+1,j−ui,j≤0u\_{i+1,j}-u\_{i,j}\leq 0);
* •

  for α∈ℐconv\alpha\in\mathcal{I}\_{\mathrm{conv}}, the inequality encodes a
  discrete strike-convexity condition ∂K​Ku≥0\partial\_{KK}u\geq 0 on a slice
  (e.g. a local second-difference inequality);
* •

  for α∈ℐcal\alpha\in\mathcal{I}\_{\mathrm{cal}}, the inequality encodes a
  discrete calendar condition (∂τu)|K≥0(\partial\_{\tau}u)|\_{K}\geq 0 at fixed strike,
  implemented via the fixed-strike calendar operator Aτ|KA\_{\tau|K} from
  Section [4.3](https://arxiv.org/html/2512.01967v1#Ch4.S3 "4.3 Calendar derivative at fixed strike ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

Collecting these, the global static no-arbitrage feasible set on the full grid is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞glob:={u∈ℝG:ℓα⊤​u≤rα,∀α∈ℐ}.\mathcal{C}\_{\mathrm{glob}}:=\Big\{u\in\mathbb{R}^{G}:\ell\_{\alpha}^{\top}u\leq r\_{\alpha},\quad\forall\alpha\in\mathcal{I}\Big\}. |  | (12.2) |

This is precisely the intersection of finitely many closed half-spaces in
ℝG\mathbb{R}^{G}.

###### Definition 19 (Global no-arbitrage operators).

Let 𝒢={(i​(g),j​(g)):g=1,…,G}\mathcal{G}=\{(i(g),j(g)):g=1,\dots,G\} be an enumeration of the nodal
grid and let e(g)∈ℝGe^{(g)}\in\mathbb{R}^{G} denote the gg-th standard basis vector.
Write g​(i,j)g(i,j) for the index such that (i​(g​(i,j)),j​(g​(i,j)))=(i,j)(i(g(i,j)),j(g(i,j)))=(i,j).

We define index sets and pairs (ℓα,rα)(\ell\_{\alpha},r\_{\alpha}) as follows, where e(g)e^{(g)} is the gg-th standard basis vector in ℝG\mathbb{R}^{G} (vector with 11 in position gg and 0 elsewhere):

* •

  *(Bounds)*
  For each (i,j)∈𝒢(i,j)\in\mathcal{G} with g=g​(i,j)g=g(i,j) define lower and upper indices
  α=(i,j,lo)\alpha=(i,j,\mathrm{lo}), α′=(i,j,up)\alpha^{\prime}=(i,j,\mathrm{up}) and

  |  |  |  |
  | --- | --- | --- |
  |  | ℓ(i,j,lo)⊤:=−(e(g))⊤,r(i,j,lo):=0,ℓ(i,j,up)⊤:=(e(g))⊤,r(i,j,up):=Fi,j.\ell\_{(i,j,\mathrm{lo})}^{\top}:=-(e^{(g)})^{\top},\quad r\_{(i,j,\mathrm{lo})}:=0,\qquad\ell\_{(i,j,\mathrm{up})}^{\top}:=(e^{(g)})^{\top},\quad r\_{(i,j,\mathrm{up})}:=F\_{i,j}. |  |

  Collect all such indices into ℐbnd\mathcal{I}\_{\mathrm{bnd}}.
* •

  *(Monotonicity)*
  For each maturity jj and i=1,…,nm−1i=1,\dots,n\_{m}-1, with
  g1=g​(i,j)g\_{1}=g(i,j), g2=g​(i+1,j)g\_{2}=g(i+1,j), define α=(i,j)∈ℐmono\alpha=(i,j)\in\mathcal{I}\_{\mathrm{mono}} and

  |  |  |  |
  | --- | --- | --- |
  |  | ℓ(i,j)⊤:=(e(g2)−e(g1))⊤,r(i,j):=0.\ell\_{(i,j)}^{\top}:=(e^{(g\_{2})}-e^{(g\_{1})})^{\top},\qquad r\_{(i,j)}:=0. |  |
* •

  *(Convexity)*
  For each maturity jj and i=2,…,nm−1i=2,\dots,n\_{m}-1, with
  g−=g​(i−1,j)g\_{-}=g(i-1,j), g0=g​(i,j)g\_{0}=g(i,j), g+=g​(i+1,j)g\_{+}=g(i+1,j), define α=(i,j)∈ℐconv\alpha=(i,j)\in\mathcal{I}\_{\mathrm{conv}} and

  |  |  |  |
  | --- | --- | --- |
  |  | ℓ(i,j)⊤:=(−e(g+)+2​e(g0)−e(g−))⊤,r(i,j):=0.\ell\_{(i,j)}^{\top}:=(-e^{(g\_{+})}+2e^{(g\_{0})}-e^{(g\_{-})})^{\top},\qquad r\_{(i,j)}:=0. |  |
* •

  *(Calendar)*
  Let Aτ|K∈ℝG×GA\_{\tau|K}\in\mathbb{R}^{G\times G} be the fixed-strike calendar operator.
  For each g∈{1,…,G}g\in\{1,\dots,G\} define α=g∈ℐcal\alpha=g\in\mathcal{I}\_{\mathrm{cal}} and

  |  |  |  |
  | --- | --- | --- |
  |  | ℓg⊤:=−(Aτ|K)g,⋅,rg:=0.\ell\_{g}^{\top}:=-(A\_{\tau|K})\_{g,\cdot},\qquad r\_{g}:=0. |  |

Set ℐ:=ℐbnd∪ℐmono∪ℐconv∪ℐcal\mathcal{I}:=\mathcal{I}\_{\mathrm{bnd}}\cup\mathcal{I}\_{\mathrm{mono}}\cup\mathcal{I}\_{\mathrm{conv}}\cup\mathcal{I}\_{\mathrm{cal}}.

This definition can be seen as follows:

##### Bounds.

We first explain how to encode the pointwise bounds

|  |  |  |
| --- | --- | --- |
|  | 0≤ui,j≤Fi,j,(i,j)∈𝒢,0\leq u\_{i,j}\leq F\_{i,j},\qquad(i,j)\in\mathcal{G}, |  |

as linear inequalities of the form ℓα⊤​u≤rα\ell\_{\alpha}^{\top}u\leq r\_{\alpha}.

Fix a node (i,j)∈𝒢(i,j)\in\mathcal{G} and let g=g​(i,j)g=g(i,j) be its index in the flattened
nodal vector u∈ℝGu\in\mathbb{R}^{G}, so that ug=ui,ju\_{g}=u\_{i,j}. For this node we introduce
*two* constraint indices:

|  |  |  |
| --- | --- | --- |
|  | α=(i,j,lo),α′=(i,j,up).\alpha=(i,j,\mathrm{lo}),\qquad\alpha^{\prime}=(i,j,\mathrm{up}). |  |

*Lower bound.* For α=(i,j,lo)\alpha=(i,j,\mathrm{lo}) we define

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,lo)⊤:=−(e(g))⊤,r(i,j,lo):=0,\ell\_{(i,j,\mathrm{lo})}^{\top}:=-(e^{(g)})^{\top},\qquad r\_{(i,j,\mathrm{lo})}:=0, |  |

where e(g)∈ℝGe^{(g)}\in\mathbb{R}^{G} is the gg-th standard basis vector. Then

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,lo)⊤​u=−e(g)⊤​u=−ug=−ui,j,\ell\_{(i,j,\mathrm{lo})}^{\top}u=-e^{(g)\top}u=-u\_{g}=-u\_{i,j}, |  |

so the inequality ℓ(i,j,lo)⊤​u≤r(i,j,lo)\ell\_{(i,j,\mathrm{lo})}^{\top}u\leq r\_{(i,j,\mathrm{lo})} reads

|  |  |  |
| --- | --- | --- |
|  | −ui,j≤0⟺ui,j≥0.-u\_{i,j}\leq 0\quad\Longleftrightarrow\quad u\_{i,j}\geq 0. |  |

*Upper bound.* For α′=(i,j,up)\alpha^{\prime}=(i,j,\mathrm{up}) we set

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,up)⊤:=(e(g))⊤,r(i,j,up):=Fi,j.\ell\_{(i,j,\mathrm{up})}^{\top}:=(e^{(g)})^{\top},\qquad r\_{(i,j,\mathrm{up})}:=F\_{i,j}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,up)⊤​u=e(g)⊤​u=ug=ui,j,\ell\_{(i,j,\mathrm{up})}^{\top}u=e^{(g)\top}u=u\_{g}=u\_{i,j}, |  |

so ℓ(i,j,up)⊤​u≤r(i,j,up)\ell\_{(i,j,\mathrm{up})}^{\top}u\leq r\_{(i,j,\mathrm{up})} is exactly

|  |  |  |
| --- | --- | --- |
|  | ui,j≤Fi,j.u\_{i,j}\leq F\_{i,j}. |  |

Thus for each node (i,j)(i,j) we obtain the two bounds 0≤ui,j≤Fi,j0\leq u\_{i,j}\leq F\_{i,j} as the
pair of inequalities

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,lo)⊤​u≤r(i,j,lo),ℓ(i,j,up)⊤​u≤r(i,j,up).\ell\_{(i,j,\mathrm{lo})}^{\top}u\leq r\_{(i,j,\mathrm{lo})},\qquad\ell\_{(i,j,\mathrm{up})}^{\top}u\leq r\_{(i,j,\mathrm{up})}. |  |

All such indices (i,j,lo)(i,j,\mathrm{lo}) and (i,j,up)(i,j,\mathrm{up}) are collected in
ℐbnd\mathcal{I}\_{\mathrm{bnd}}.

##### Monotonicity.

We now encode discrete strike monotonicity, namely

|  |  |  |
| --- | --- | --- |
|  | ui+1,j−ui,j≤0,i=1,…,nm−1,j=1,…,nτ.u\_{i+1,j}-u\_{i,j}\leq 0,\qquad i=1,\dots,n\_{m}-1,\quad j=1,\dots,n\_{\tau}. |  |

Fix a maturity jj and i∈{1,…,nm−1}i\in\{1,\dots,n\_{m}-1\}. Let

|  |  |  |
| --- | --- | --- |
|  | g1:=g​(i,j),g2:=g​(i+1,j)g\_{1}:=g(i,j),\qquad g\_{2}:=g(i+1,j) |  |

be the indices of the adjacent nodes (i,j)(i,j) and (i+1,j)(i+1,j) in the flattened
vector uu. We introduce a single index α=(i,j)∈ℐmono\alpha=(i,j)\in\mathcal{I}\_{\mathrm{mono}}
and define

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤:=(e(g2)−e(g1))⊤,r(i,j):=0.\ell\_{(i,j)}^{\top}:=(e^{(g\_{2})}-e^{(g\_{1})})^{\top},\qquad r\_{(i,j)}:=0. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤​u=e(g2)⊤​u−e(g1)⊤​u=ug2−ug1=ui+1,j−ui,j.\ell\_{(i,j)}^{\top}u=e^{(g\_{2})\top}u-e^{(g\_{1})\top}u=u\_{g\_{2}}-u\_{g\_{1}}=u\_{i+1,j}-u\_{i,j}. |  |

Thus the inequality ℓ(i,j)⊤​u≤r(i,j)\ell\_{(i,j)}^{\top}u\leq r\_{(i,j)} is precisely

|  |  |  |
| --- | --- | --- |
|  | ui+1,j−ui,j≤0,u\_{i+1,j}-u\_{i,j}\leq 0, |  |

the desired monotonicity condition. Each adjacent pair of strikes at fixed jj
contributes one such index (i,j)(i,j) to ℐmono\mathcal{I}\_{\mathrm{mono}}.

##### Convexity.

Discrete strike convexity requires

|  |  |  |
| --- | --- | --- |
|  | ui+1,j−2​ui,j+ui−1,j≥0,i=2,…,nm−1,j=1,…,nτ.u\_{i+1,j}-2u\_{i,j}+u\_{i-1,j}\geq 0,\qquad i=2,\dots,n\_{m}-1,\quad j=1,\dots,n\_{\tau}. |  |

Equivalently,

|  |  |  |
| --- | --- | --- |
|  | −ui+1,j+2​ui,j−ui−1,j≤0.-u\_{i+1,j}+2u\_{i,j}-u\_{i-1,j}\leq 0. |  |

Fix a maturity jj and an interior strike index i∈{2,…,nm−1}i\in\{2,\dots,n\_{m}-1\}. Let

|  |  |  |
| --- | --- | --- |
|  | g−:=g​(i−1,j),g0:=g​(i,j),g+:=g​(i+1,j).g\_{-}:=g(i-1,j),\qquad g\_{0}:=g(i,j),\qquad g\_{+}:=g(i+1,j). |  |

We introduce an index α=(i,j)∈ℐconv\alpha=(i,j)\in\mathcal{I}\_{\mathrm{conv}} and set

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤:=(−e(g+)+2​e(g0)−e(g−))⊤,r(i,j):=0.\ell\_{(i,j)}^{\top}:=(-e^{(g\_{+})}+2e^{(g\_{0})}-e^{(g\_{-})})^{\top},\qquad r\_{(i,j)}:=0. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤​u=−ug++2​ug0−ug−=−ui+1,j+2​ui,j−ui−1,j,\ell\_{(i,j)}^{\top}u=-u\_{g\_{+}}+2u\_{g\_{0}}-u\_{g\_{-}}=-u\_{i+1,j}+2u\_{i,j}-u\_{i-1,j}, |  |

so the inequality ℓ(i,j)⊤​u≤r(i,j)\ell\_{(i,j)}^{\top}u\leq r\_{(i,j)} is exactly

|  |  |  |
| --- | --- | --- |
|  | −ui+1,j+2​ui,j−ui−1,j≤0⟺ui+1,j−2​ui,j+ui−1,j≥0.-u\_{i+1,j}+2u\_{i,j}-u\_{i-1,j}\leq 0\quad\Longleftrightarrow\quad u\_{i+1,j}-2u\_{i,j}+u\_{i-1,j}\geq 0. |  |

All such indices (i,j)(i,j) form the convexity index set ℐconv\mathcal{I}\_{\mathrm{conv}}.

##### Calendar (fixed strike).

Finally, we encode the discrete calendar condition at fixed strike via the operator
Aτ|K∈ℝG×GA\_{\tau|K}\in\mathbb{R}^{G\times G}. By construction, (Aτ|K​u)g(A\_{\tau|K}u)\_{g} is the
discrete approximation of (∂τCf)​(K,τ)|K(\partial\_{\tau}C\_{f})(K,\tau)|\_{K} at the grid node
indexed by gg. The condition

|  |  |  |
| --- | --- | --- |
|  | (Aτ|K​u)g≥0,g=1,…,G,(A\_{\tau|K}u)\_{g}\geq 0,\qquad g=1,\dots,G, |  |

can be written as

|  |  |  |
| --- | --- | --- |
|  | −(Aτ|K​u)g≤0.-(A\_{\tau|K}u)\_{g}\leq 0. |  |

For each grid index g∈{1,…,G}g\in\{1,\dots,G\} we take α=g∈ℐcal\alpha=g\in\mathcal{I}\_{\mathrm{cal}}
and define

|  |  |  |
| --- | --- | --- |
|  | ℓg⊤:=−(Aτ|K)g,⋅,rg:=0,\ell\_{g}^{\top}:=-(A\_{\tau|K})\_{g,\cdot},\qquad r\_{g}:=0, |  |

i.e. ℓg⊤\ell\_{g}^{\top} is the negative of the gg-th row of Aτ|KA\_{\tau|K}. Then

|  |  |  |
| --- | --- | --- |
|  | ℓg⊤​u=−(Aτ|K​u)g,\ell\_{g}^{\top}u=-(A\_{\tau|K}u)\_{g}, |  |

so the inequality ℓg⊤​u≤rg\ell\_{g}^{\top}u\leq r\_{g} is precisely

|  |  |  |
| --- | --- | --- |
|  | −(Aτ|K​u)g≤0⟺(Aτ|K​u)g≥0.-(A\_{\tau|K}u)\_{g}\leq 0\quad\Longleftrightarrow\quad(A\_{\tau|K}u)\_{g}\geq 0. |  |

Thus each row gg of Aτ|KA\_{\tau|K} generates one calendar inequality, and all these
indices gg belong to ℐcal\mathcal{I}\_{\mathrm{cal}}.

###### Definition 20 (Primitive discrete static no-arbitrage on 𝒢\mathcal{G}).

A nodal surface

|  |  |  |
| --- | --- | --- |
|  | u=(ui,j)(i,j)∈𝒢∈ℝGu=(u\_{i,j})\_{(i,j)\in\mathcal{G}}\in\mathbb{R}^{G} |  |

is said to satisfy *primitive discrete static no-arbitrage* on 𝒢\mathcal{G} if:

* •

  *(BND)* (Bounds) For all (i,j)∈𝒢(i,j)\in\mathcal{G},

  |  |  |  |
  | --- | --- | --- |
  |  | 0≤ui,j≤Fi,j.0\leq u\_{i,j}\leq F\_{i,j}. |  |
* •

  *(MONO)* (Strike monotonicity) For each maturity jj and each
  i=1,…,nm−1i=1,\dots,n\_{m}-1,

  |  |  |  |
  | --- | --- | --- |
  |  | ui+1,j−ui,j≤0.u\_{i+1,j}-u\_{i,j}\leq 0. |  |
* •

  *(CONV)* (Strike convexity) For each maturity jj and
  i=2,…,nm−1i=2,\dots,n\_{m}-1,

  |  |  |  |
  | --- | --- | --- |
  |  | ui+1,j−2​ui,j+ui−1,j≥0.u\_{i+1,j}-2u\_{i,j}+u\_{i-1,j}\geq 0. |  |
* •

  *(CAL)* (Calendar at fixed strike) Let Aτ|K∈ℝG×GA\_{\tau|K}\in\mathbb{R}^{G\times G}
  be the fixed-strike calendar operator from
  Section [4.3](https://arxiv.org/html/2512.01967v1#Ch4.S3 "4.3 Calendar derivative at fixed strike ‣ 4. No-arbitrage operators on a collocation grid ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"). Then

  |  |  |  |
  | --- | --- | --- |
  |  | (Aτ|K​u)g≥0for all grid indices ​g=1,…,G.(A\_{\tau|K}u)\_{g}\geq 0\qquad\text{for all grid indices }g=1,\dots,G. |  |

###### Proposition 12 (Equivalence of operator encoding and primitive no-arbitrage).

Let (ℓα,rα)α∈ℐ(\ell\_{\alpha},r\_{\alpha})\_{\alpha\in\mathcal{I}} be defined as in
Definition [19](https://arxiv.org/html/2512.01967v1#Thmdefinition19 "Definition 19 (Global no-arbitrage operators). ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), with index sets
ℐbnd\mathcal{I}\_{\mathrm{bnd}}, ℐmono\mathcal{I}\_{\mathrm{mono}},
ℐconv\mathcal{I}\_{\mathrm{conv}}, ℐcal\mathcal{I}\_{\mathrm{cal}} corresponding to
bounds, strike monotonicity, strike convexity, and calendar constraints respectively,
and ℐ=ℐbnd∪ℐmono∪ℐconv∪ℐcal\mathcal{I}=\mathcal{I}\_{\mathrm{bnd}}\cup\mathcal{I}\_{\mathrm{mono}}\cup\mathcal{I}\_{\mathrm{conv}}\cup\mathcal{I}\_{\mathrm{cal}}.

For u∈ℝGu\in\mathbb{R}^{G}, the following are equivalent:

1. (i)

   uu satisfies all linear inequalities

   |  |  |  |
   | --- | --- | --- |
   |  | ℓα⊤​u≤rα,∀α∈ℐ.\ell\_{\alpha}^{\top}u\leq r\_{\alpha},\qquad\forall\alpha\in\mathcal{I}. |  |
2. (ii)

   uu satisfies primitive discrete static no-arbitrage on 𝒢\mathcal{G} in the
   sense of Definition [20](https://arxiv.org/html/2512.01967v1#Thmdefinition20 "Definition 20 (Primitive discrete static no-arbitrage on 𝒢). ‣ Calendar (fixed strike). ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

In particular, the global static no-arbitrage feasible set

|  |  |  |
| --- | --- | --- |
|  | 𝒞glob={u∈ℝG:ℓα⊤​u≤rα​∀α∈ℐ}\mathcal{C}\_{\mathrm{glob}}=\big\{u\in\mathbb{R}^{G}:\ell\_{\alpha}^{\top}u\leq r\_{\alpha}\ \forall\alpha\in\mathcal{I}\big\} |  |

coincides with the set of all nodal surfaces that satisfy the primitive discrete
no-arbitrage conditions (BND), (MONO), (CONV) and (CAL).

###### Proof.

We prove (i)⇔(i​i)(i)\Leftrightarrow(ii) by decomposing ℐ\mathcal{I} into its four
subsets.

*(ii) ⇒\Rightarrow (i).* Suppose uu satisfies the primitive
conditions (BND), (MONO), (CONV), (CAL).

*Bounds.* Fix (i,j)∈𝒢(i,j)\in\mathcal{G} and let g=g​(i,j)g=g(i,j) be its index. By
Definition [19](https://arxiv.org/html/2512.01967v1#Thmdefinition19 "Definition 19 (Global no-arbitrage operators). ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), the two bound indices
α=(i,j,lo)\alpha=(i,j,\mathrm{lo}), α′=(i,j,up)\alpha^{\prime}=(i,j,\mathrm{up}) satisfy

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,lo)⊤=−(e(g))⊤,r(i,j,lo)=0,ℓ(i,j,up)⊤=(e(g))⊤,r(i,j,up)=Fi,j,\ell\_{(i,j,\mathrm{lo})}^{\top}=-(e^{(g)})^{\top},\quad r\_{(i,j,\mathrm{lo})}=0,\qquad\ell\_{(i,j,\mathrm{up})}^{\top}=(e^{(g)})^{\top},\quad r\_{(i,j,\mathrm{up})}=F\_{i,j}, |  |

where e(g)e^{(g)} is the gg-th standard basis vector in ℝG\mathbb{R}^{G}.
Then

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,lo)⊤​u=−ui,j,ℓ(i,j,up)⊤​u=ui,j.\ell\_{(i,j,\mathrm{lo})}^{\top}u=-u\_{i,j},\qquad\ell\_{(i,j,\mathrm{up})}^{\top}u=u\_{i,j}. |  |

The bound condition 0≤ui,j≤Fi,j0\leq u\_{i,j}\leq F\_{i,j} implies

|  |  |  |
| --- | --- | --- |
|  | −ui,j≤0=r(i,j,lo),ui,j≤Fi,j=r(i,j,up),-u\_{i,j}\leq 0=r\_{(i,j,\mathrm{lo})},\qquad u\_{i,j}\leq F\_{i,j}=r\_{(i,j,\mathrm{up})}, |  |

hence ℓα⊤​u≤rα\ell\_{\alpha}^{\top}u\leq r\_{\alpha} for all
α∈ℐbnd\alpha\in\mathcal{I}\_{\mathrm{bnd}}.

*Strike monotonicity.* Fix a maturity jj and i=1,…,nm−1i=1,\dots,n\_{m}-1, and let
g1=g​(i,j)g\_{1}=g(i,j), g2=g​(i+1,j)g\_{2}=g(i+1,j). By
Definition [19](https://arxiv.org/html/2512.01967v1#Thmdefinition19 "Definition 19 (Global no-arbitrage operators). ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), for α=(i,j)∈ℐmono\alpha=(i,j)\in\mathcal{I}\_{\mathrm{mono}}
we have

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤:=(e(g2)−e(g1))⊤,r(i,j):=0,\ell\_{(i,j)}^{\top}:=(e^{(g\_{2})}-e^{(g\_{1})})^{\top},\qquad r\_{(i,j)}:=0, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤​u=ui+1,j−ui,j.\ell\_{(i,j)}^{\top}u=u\_{i+1,j}-u\_{i,j}. |  |

The primitive monotonicity condition (MONO) states that ui+1,j−ui,j≤0u\_{i+1,j}-u\_{i,j}\leq 0,
hence ℓ(i,j)⊤​u≤r(i,j)\ell\_{(i,j)}^{\top}u\leq r\_{(i,j)} for all (i,j)(i,j), i.e. for all
α∈ℐmono\alpha\in\mathcal{I}\_{\mathrm{mono}}.

*Strike convexity.* Fix a maturity jj and i=2,…,nm−1i=2,\dots,n\_{m}-1, and let
g−=g​(i−1,j)g\_{-}=g(i-1,j), g0=g​(i,j)g\_{0}=g(i,j), g+=g​(i+1,j)g\_{+}=g(i+1,j). For α=(i,j)∈ℐconv\alpha=(i,j)\in\mathcal{I}\_{\mathrm{conv}},
Definition [19](https://arxiv.org/html/2512.01967v1#Thmdefinition19 "Definition 19 (Global no-arbitrage operators). ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") gives

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤:=(−e(g+)+2​e(g0)−e(g−))⊤,r(i,j):=0.\ell\_{(i,j)}^{\top}:=(-e^{(g\_{+})}+2e^{(g\_{0})}-e^{(g\_{-})})^{\top},\qquad r\_{(i,j)}:=0. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤​u=−ui+1,j+2​ui,j−ui−1,j.\ell\_{(i,j)}^{\top}u=-u\_{i+1,j}+2u\_{i,j}-u\_{i-1,j}. |  |

The primitive convexity condition (CONV) is
ui+1,j−2​ui,j+ui−1,j≥0u\_{i+1,j}-2u\_{i,j}+u\_{i-1,j}\geq 0, or equivalently
−ui+1,j+2​ui,j−ui−1,j≤0-u\_{i+1,j}+2u\_{i,j}-u\_{i-1,j}\leq 0, hence ℓ(i,j)⊤​u≤r(i,j)\ell\_{(i,j)}^{\top}u\leq r\_{(i,j)}
for all (i,j)(i,j), i.e. all α∈ℐconv\alpha\in\mathcal{I}\_{\mathrm{conv}}.

*Calendar.* Let Aτ|K∈ℝG×GA\_{\tau|K}\in\mathbb{R}^{G\times G} be the fixed-strike
calendar operator. For each grid index g∈{1,…,G}g\in\{1,\dots,G\}, the calendar index
α=g∈ℐcal\alpha=g\in\mathcal{I}\_{\mathrm{cal}} is defined by

|  |  |  |
| --- | --- | --- |
|  | ℓg⊤:=−(Aτ|K)g,⋅,rg:=0,\ell\_{g}^{\top}:=-(A\_{\tau|K})\_{g,\cdot},\qquad r\_{g}:=0, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | ℓg⊤​u=−(Aτ|K​u)g.\ell\_{g}^{\top}u=-(A\_{\tau|K}u)\_{g}. |  |

The primitive calendar condition (CAL) states (Aτ|K​u)g≥0(A\_{\tau|K}u)\_{g}\geq 0 for all
gg, which is equivalent to −(Aτ|K​u)g≤0=rg-(A\_{\tau|K}u)\_{g}\leq 0=r\_{g}, hence
ℓg⊤​u≤rg\ell\_{g}^{\top}u\leq r\_{g} for all α∈ℐcal\alpha\in\mathcal{I}\_{\mathrm{cal}}.

Combining the four families, we see that (ii) implies ℓα⊤​u≤rα\ell\_{\alpha}^{\top}u\leq r\_{\alpha}
for all α∈ℐ\alpha\in\mathcal{I}, i.e. (i) holds.

*(i) ⇒\Rightarrow (ii).* Conversely, suppose uu satisfies
ℓα⊤​u≤rα\ell\_{\alpha}^{\top}u\leq r\_{\alpha} for all α∈ℐ\alpha\in\mathcal{I}. We show that the
primitive conditions (BND), (MONO), (CONV), (CAL) hold.

*Bounds.* Fix (i,j)∈𝒢(i,j)\in\mathcal{G} and g=g​(i,j)g=g(i,j). For α=(i,j,lo)\alpha=(i,j,\mathrm{lo})
and α′=(i,j,up)\alpha^{\prime}=(i,j,\mathrm{up}) we have, by definition,

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j,lo)⊤​u=−ui,j≤r(i,j,lo)=0,ℓ(i,j,up)⊤​u=ui,j≤r(i,j,up)=Fi,j.\ell\_{(i,j,\mathrm{lo})}^{\top}u=-u\_{i,j}\leq r\_{(i,j,\mathrm{lo})}=0,\qquad\ell\_{(i,j,\mathrm{up})}^{\top}u=u\_{i,j}\leq r\_{(i,j,\mathrm{up})}=F\_{i,j}. |  |

Thus −ui,j≤0-u\_{i,j}\leq 0 and ui,j≤Fi,ju\_{i,j}\leq F\_{i,j}, i.e. 0≤ui,j≤Fi,j0\leq u\_{i,j}\leq F\_{i,j}
for all (i,j)(i,j), which is (BND).

*Strike monotonicity.* For each jj and i=1,…,nm−1i=1,\dots,n\_{m}-1, the inequality
for α=(i,j)∈ℐmono\alpha=(i,j)\in\mathcal{I}\_{\mathrm{mono}} reads

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤​u=ui+1,j−ui,j≤0,\ell\_{(i,j)}^{\top}u=u\_{i+1,j}-u\_{i,j}\leq 0, |  |

which is exactly the discrete monotonicity condition ui+1,j−ui,j≤0u\_{i+1,j}-u\_{i,j}\leq 0
for all such (i,j)(i,j); this is (MONO).

*Strike convexity.* For each jj and i=2,…,nm−1i=2,\dots,n\_{m}-1, the inequality
for α=(i,j)∈ℐconv\alpha=(i,j)\in\mathcal{I}\_{\mathrm{conv}} is

|  |  |  |
| --- | --- | --- |
|  | ℓ(i,j)⊤​u=−ui+1,j+2​ui,j−ui−1,j≤0.\ell\_{(i,j)}^{\top}u=-u\_{i+1,j}+2u\_{i,j}-u\_{i-1,j}\leq 0. |  |

Rearranging gives ui+1,j−2​ui,j+ui−1,j≥0u\_{i+1,j}-2u\_{i,j}+u\_{i-1,j}\geq 0, which is (CONV).

*Calendar.* Finally, for each grid index g∈{1,…,G}g\in\{1,\dots,G\} we have

|  |  |  |
| --- | --- | --- |
|  | ℓg⊤​u=−(Aτ|K​u)g≤0,\ell\_{g}^{\top}u=-(A\_{\tau|K}u)\_{g}\leq 0, |  |

or equivalently (Aτ|K​u)g≥0(A\_{\tau|K}u)\_{g}\geq 0. Thus (CAL) holds at every grid index.

Therefore all four primitive conditions (BND), (MONO), (CONV), (CAL) hold, and
uu satisfies primitive discrete static no-arbitrage. This proves (ii).

We have shown (i​i)⇒(i)(ii)\Rightarrow(i) and (i)⇒(i​i)(i)\Rightarrow(ii), so the two statements
are equivalent. The characterisation of 𝒞glob\mathcal{C}\_{\mathrm{glob}} as the set
of all primitively no-arbitrage nodal surfaces follows immediately from the
definition of 𝒞glob\mathcal{C}\_{\mathrm{glob}}.
∎

#### 12.4.3 Patch-level feasible set and its geometry

We now enforce global static no-arbitrage on the *assembled* surface u​(uI)u(u\_{I})
obtained from a patch interior vector uIu\_{I}.

###### Definition 21 (No-arbitrage feasible set on a patch).

The *patch-level no-arbitrage feasible set* is

|  |  |  |
| --- | --- | --- |
|  | 𝒞u​(Ω):={uI∈ℝNΩ:u​(uI)∈𝒞glob}.\mathcal{C}\_{u}(\Omega):=\big\{u\_{I}\in\mathbb{R}^{N\_{\Omega}}:u(u\_{I})\in\mathcal{C}\_{\mathrm{glob}}\big\}. |  |

Equivalently, using ([12.2](https://arxiv.org/html/2512.01967v1#Ch12.E2 "Equation 12.2 ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) and the assembly map
([12.1](https://arxiv.org/html/2512.01967v1#Ch12.E1 "Equation 12.1 ‣ 12.4.1 Interior price variables and assembly map ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")),

|  |  |  |
| --- | --- | --- |
|  | 𝒞u​(Ω)={uI∈ℝNΩ:ℓα⊤​u​(uI)≤rα,∀α∈ℐ}.\mathcal{C}\_{u}(\Omega)=\Big\{u\_{I}\in\mathbb{R}^{N\_{\Omega}}:\ell\_{\alpha}^{\top}u(u\_{I})\leq r\_{\alpha},\quad\forall\alpha\in\mathcal{I}\Big\}. |  |

We now characterise 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega) as a polyhedron and prove its
basic geometric properties.

###### Proposition 13 (Polyhedral structure of 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega)).

The set 𝒞u​(Ω)⊂ℝNΩ\mathcal{C}\_{u}(\Omega)\subset\mathbb{R}^{N\_{\Omega}} can be written as the
finite intersection of affine half-spaces

|  |  |  |
| --- | --- | --- |
|  | 𝒞u​(Ω)=⋂α∈ℐHα,\mathcal{C}\_{u}(\Omega)=\bigcap\_{\alpha\in\mathcal{I}}H\_{\alpha}, |  |

where each HαH\_{\alpha} is of the form

|  |  |  |
| --- | --- | --- |
|  | Hα:={uI∈ℝNΩ:aα⊤​uI≤bα}H\_{\alpha}:=\{u\_{I}\in\mathbb{R}^{N\_{\Omega}}:a\_{\alpha}^{\top}u\_{I}\leq b\_{\alpha}\} |  |

for some aα∈ℝNΩa\_{\alpha}\in\mathbb{R}^{N\_{\Omega}} and bα∈ℝb\_{\alpha}\in\mathbb{R}. In particular,
𝒞u​(Ω)\mathcal{C}\_{u}(\Omega) is a (possibly empty) closed convex polyhedron in
ℝNΩ\mathbb{R}^{N\_{\Omega}}.

###### Proof.

Fix α∈ℐ\alpha\in\mathcal{I}. For uI∈ℝNΩu\_{I}\in\mathbb{R}^{N\_{\Omega}}, the corresponding
assembled surface is u​(uI)=PΩ​uI+u0,offu(u\_{I})=P\_{\Omega}u\_{I}+u^{0,\mathrm{off}} by
([12.1](https://arxiv.org/html/2512.01967v1#Ch12.E1 "Equation 12.1 ‣ 12.4.1 Interior price variables and assembly map ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). The α\alpha-th global no-arbitrage inequality reads

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​u​(uI)≤rα.\ell\_{\alpha}^{\top}u(u\_{I})\leq r\_{\alpha}. |  |

Substituting the affine expression for u​(uI)u(u\_{I}), we obtain

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​(PΩ​uI+u0,off)≤rα,\ell\_{\alpha}^{\top}(P\_{\Omega}u\_{I}+u^{0,\mathrm{off}})\leq r\_{\alpha}, |  |

which can be rearranged as

|  |  |  |
| --- | --- | --- |
|  | (ℓα⊤​PΩ)​uI≤rα−ℓα⊤​u0,off.(\ell\_{\alpha}^{\top}P\_{\Omega})\,u\_{I}\leq r\_{\alpha}-\ell\_{\alpha}^{\top}u^{0,\mathrm{off}}. |  |

Now, define

|  |  |  |
| --- | --- | --- |
|  | aα:=PΩ⊤​ℓα∈ℝNΩ,bα:=rα−ℓα⊤​u0,off∈ℝ.a\_{\alpha}:=P\_{\Omega}^{\top}\ell\_{\alpha}\in\mathbb{R}^{N\_{\Omega}},\qquad b\_{\alpha}:=r\_{\alpha}-\ell\_{\alpha}^{\top}u^{0,\mathrm{off}}\in\mathbb{R}. |  |

Note that ℓα⊤​PΩ=aα⊤\ell\_{\alpha}^{\top}P\_{\Omega}=a\_{\alpha}^{\top} by construction. Then the
α\alpha-th constraint is equivalent to

|  |  |  |
| --- | --- | --- |
|  | aα⊤​uI≤bα.a\_{\alpha}^{\top}u\_{I}\leq b\_{\alpha}. |  |

Therefore, the set of uIu\_{I} satisfying the α\alpha-th global no-arbitrage inequality
is the half-space

|  |  |  |
| --- | --- | --- |
|  | Hα:={uI∈ℝNΩ:aα⊤​uI≤bα}.H\_{\alpha}:=\{u\_{I}\in\mathbb{R}^{N\_{\Omega}}:a\_{\alpha}^{\top}u\_{I}\leq b\_{\alpha}\}. |  |

Because this construction holds for every α∈ℐ\alpha\in\mathcal{I} (namely; to be patch-feasible uIu\_{I} has to satisfy every constraint, so belong to every HαH\_{\alpha}), we have

|  |  |  |
| --- | --- | --- |
|  | 𝒞u​(Ω)={uI∈ℝNΩ:aα⊤​uI≤bα​∀α∈ℐ}=⋂α∈ℐHα.\mathcal{C}\_{u}(\Omega)=\{u\_{I}\in\mathbb{R}^{N\_{\Omega}}:a\_{\alpha}^{\top}u\_{I}\leq b\_{\alpha}\ \forall\alpha\in\mathcal{I}\}=\bigcap\_{\alpha\in\mathcal{I}}H\_{\alpha}. |  |

Recall that a half-space in ℝn\mathbb{R}^{n} is any set that can be written as {x∈ℝn:a⊤​x≤b}\{x\in\mathbb{R}^{n}:a^{\top}x\leq b\} or {x∈ℝn:a⊤​x≥b}\{x\in\mathbb{R}^{n}:a^{\top}x\geq b\} for some fixed nonzero vector aa and scalar bb. Therefore; by definition, each HαH\_{\alpha} is a half-space in ℝNΩ\mathbb{R}^{N\_{\Omega}}.

A set CC is convex if for all x,y∈Cx,y\in C and λ∈[0,1]\lambda\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | λ​x+(1−λ)​y∈C.\lambda x+(1-\lambda)y\in C. |  |

Now, take Hα:={uI∈ℝNΩ:aα⊤​uI≤bα}H\_{\alpha}:=\{u\_{I}\in\mathbb{R}^{N\_{\Omega}}:a\_{\alpha}^{\top}u\_{I}\leq b\_{\alpha}\} and let uI(1),uI(2)∈Hαu\_{I}^{(1)},u\_{I}^{(2)}\in H\_{\alpha}. We therefore have by definition of HαH\_{\alpha} that aα⊤​uI(1)≤bαa\_{\alpha}^{\top}u\_{I}^{(1)}\leq b\_{\alpha} and aα⊤​uI(2)≤bαa\_{\alpha}^{\top}u\_{I}^{(2)}\leq b\_{\alpha}. Let λ∈[0,1]\lambda\in[0,1] and consider uI(λ):=λ​uI(1)+(1−λ)​uI(2)u\_{I}^{(\lambda)}:=\lambda u\_{I}^{(1)}+(1-\lambda)u\_{I}^{(2)}. Computing:

|  |  |  |
| --- | --- | --- |
|  | aα⊤​uI(λ)=aα⊤​(λ​uI(1)+(1−λ)​uI(2))=aα⊤​λ​uI(1)+aα⊤​(1−λ)​uI(2).a\_{\alpha}^{\top}u\_{I}^{(\lambda)}=a\_{\alpha}^{\top}(\lambda u\_{I}^{(1)}+(1-\lambda)u\_{I}^{(2)})=a\_{\alpha}^{\top}\lambda u\_{I}^{(1)}+a\_{\alpha}^{\top}(1-\lambda)u\_{I}^{(2)}. |  |

Since aα⊤​uI(1)≤bαa\_{\alpha}^{\top}u\_{I}^{(1)}\leq b\_{\alpha} and aα⊤​uI(2)≤bαa\_{\alpha}^{\top}u\_{I}^{(2)}\leq b\_{\alpha}, we have

|  |  |  |
| --- | --- | --- |
|  | aα⊤​λ​uI(1)+aα⊤​(1−λ)​uI(2)≤λ​bα+(1−λ)​bα=bα.a\_{\alpha}^{\top}\lambda u\_{I}^{(1)}+a\_{\alpha}^{\top}(1-\lambda)u\_{I}^{(2)}\leq\lambda b\_{\alpha}+(1-\lambda)b\_{\alpha}=b\_{\alpha}. |  |

Therefore, aα⊤​uI(λ)≤bαa\_{\alpha}^{\top}u\_{I}^{(\lambda)}\leq b\_{\alpha}. By definition, uI(λ)∈Hαu\_{I}^{(\lambda)}\in H\_{\alpha}; which is the exact definition of convexity and thus HαH\_{\alpha} is convex.

We can see that each HαH\_{\alpha} is closed is via sequences.
Let (uI(n))n∈ℕ(u\_{I}^{(n)})\_{n\in\mathbb{N}} be a sequence in HαH\_{\alpha} converging to
some uI⋆∈ℝNΩu\_{I}^{\star}\in\mathbb{R}^{N\_{\Omega}}. By definition of HαH\_{\alpha} we have

|  |  |  |
| --- | --- | --- |
|  | aα⊤​uI(n)≤bα,∀n∈ℕ.a\_{\alpha}^{\top}u\_{I}^{(n)}\leq b\_{\alpha},\qquad\forall n\in\mathbb{N}. |  |

The map uI↦aα⊤​uIu\_{I}\mapsto a\_{\alpha}^{\top}u\_{I} is linear and hence continuous on
ℝNΩ\mathbb{R}^{N\_{\Omega}}, so passing to the limit n→∞n\to\infty yields

|  |  |  |
| --- | --- | --- |
|  | aα⊤​uI⋆=limn→∞aα⊤​uI(n)≤bα.a\_{\alpha}^{\top}u\_{I}^{\star}=\lim\_{n\to\infty}a\_{\alpha}^{\top}u\_{I}^{(n)}\leq b\_{\alpha}. |  |

Thus uI⋆u\_{I}^{\star} also satisfies aα⊤​uI⋆≤bαa\_{\alpha}^{\top}u\_{I}^{\star}\leq b\_{\alpha}, i.e. uI⋆∈Hαu\_{I}^{\star}\in H\_{\alpha}. Therefore HαH\_{\alpha} contains the limit of every
convergent sequence of its elements, and is closed.

Hence, each HαH\_{\alpha} is a closed half-space in ℝNΩ\mathbb{R}^{N\_{\Omega}} and is convex.
The intersection of any family of convex sets is convex, and the intersection of
any family of closed sets is closed. Since ℐ\mathcal{I} is finite, this intersection
defines a closed convex polyhedron. The polyhedron may be empty or nonempty,
depending on the data; we analyse feasibility separately.
∎

###### Definition 22 (Patch feasibility).

A patch Ω⊂𝒢\Omega\subset\mathcal{G} is said to be *feasible* if
𝒞u​(Ω)≠∅\mathcal{C}\_{u}(\Omega)\neq\emptyset.

The assumption that all patches used in the post-fit are feasible is mild and
consistent with the construction of Ω\Omega from the baseline surface. Indeed,
if the baseline nodal surface u0u^{0} is globally statically no-arbitrage on
𝒢\mathcal{G}, then u0∈𝒞globu^{0}\in\mathcal{C}\_{\mathrm{glob}}. If, in addition, the
patch decomposition is chosen so that every static no-arbitrage stencil that
intersects the interior of Ω\Omega is either fully contained in Ω\Omega or
fully contained in 𝒢∖Ω\mathcal{G}\setminus\Omega, then the restriction of u0u^{0}
to Ω\Omega defines an interior vector uI0,Ωu\_{I}^{0,\Omega} satisfying all
constraints aα⊤​uI≤bαa\_{\alpha}^{\top}u\_{I}\leq b\_{\alpha} and hence
uI0,Ω∈𝒞u​(Ω)u\_{I}^{0,\Omega}\in\mathcal{C}\_{u}(\Omega). In practice, feasibility can be
verified numerically by solving a simple linear feasibility problem for each
patch; in the theoretical development of this chapter we take it as an explicit
assumption that patches are chosen so that 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega) is nonempty.

### 12.5  Hamiltonian energy on the fog

We now endow the discrete fog π\pi on the lattice ℒΩ\mathcal{L}\_{\Omega} with a
quadratic Hamiltonian energy. The Hamiltonian has two components:
a *kinetic* (Dirichlet) term that penalises roughness of π\pi across
neighboring lattice sites in (m,τ,u)(m,\tau,u), and a *potential* term that
penalises fog mass lying far outside local bid–ask tubes or basic price ranges.

Throughout this section we fix a patch Ω⊂𝒢\Omega\subset\mathcal{G} with
NΩ=|Ω|N\_{\Omega}=|\Omega| and a set of price levels {uk}k=1nu\{u\_{k}\}\_{k=1}^{n\_{u}}, and we
work on the lattice

|  |  |  |
| --- | --- | --- |
|  | ℒΩ:={(i,j,k):(i,j)∈Ω,k=1,…,nu},\mathcal{L}\_{\Omega}:=\{(i,j,k):(i,j)\in\Omega,\ k=1,\dots,n\_{u}\}, |  |

as in Section [12.3](https://arxiv.org/html/2512.01967v1#Ch12.S3 "12.3 Discrete 3D fog on (𝑚,𝜏,𝑢) ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

#### 12.5.1 Discrete 3D graph and difference operators

We begin by making the discrete graph structure of ℒΩ\mathcal{L}\_{\Omega} explicit
and constructing the associated difference operators.

###### Definition 23 (Adjacency graph on ℒΩ\mathcal{L}\_{\Omega}).

Let ℒΩ\mathcal{L}\_{\Omega} be the 3D lattice of nodes (i,j,k)(i,j,k) with
(i,j)∈Ω(i,j)\in\Omega and k∈{1,…,nu}k\in\{1,\dots,n\_{u}\}. We define three families of
undirected edges:

* •

  *mm-edges* EmE\_{m}: for every (i,j,k)∈ℒΩ(i,j,k)\in\mathcal{L}\_{\Omega} such that
  (i+1,j)∈Ω(i+1,j)\in\Omega, we introduce an edge between (i,j,k)(i,j,k) and
  (i+1,j,k)(i+1,j,k);
* •

  *τ\tau-edges* EτE\_{\tau}: for every (i,j,k)∈ℒΩ(i,j,k)\in\mathcal{L}\_{\Omega}
  such that (i,j+1)∈Ω(i,j+1)\in\Omega, we introduce an edge between (i,j,k)(i,j,k)
  and (i,j+1,k)(i,j+1,k);
* •

  *uu-edges* EuE\_{u}: for every (i,j,k)∈ℒΩ(i,j,k)\in\mathcal{L}\_{\Omega} such that
  k+1≤nuk+1\leq n\_{u}, we introduce an edge between (i,j,k)(i,j,k) and (i,j,k+1)(i,j,k+1).

The full edge set is

|  |  |  |
| --- | --- | --- |
|  | E:=Em∪Eτ∪Eu.E:=E\_{m}\cup E\_{\tau}\cup E\_{u}. |  |

Thus EmE\_{m} connects nearest neighbours in the mm-direction (at fixed
(τ,u)(\tau,u)), EτE\_{\tau} connects nearest neighbours in the τ\tau-direction (at
fixed (m,u)(m,u)), and EuE\_{u} connects nearest neighbours in the uu-direction (at
fixed (m,τ)(m,\tau)). Since edges are only drawn between nodes that both belong to
ℒΩ\mathcal{L}\_{\Omega}, this corresponds to homogeneous Neumann boundary
conditions at the boundary of the patch.

For each edge family we now define a discrete gradient operator as the signed
incidence matrix of the corresponding graph.

###### Definition 24 (Discrete gradients along m,τ,um,\tau,u).

Fix an arbitrary but fixed orientation of each edge in Em,Eτ,EuE\_{m},E\_{\tau},E\_{u}:
for each edge e={p,q}∈Eme=\{p,q\}\in E\_{m}, choose an ordering (p→q)(p\to q) (e.g. increasing
in ii); similarly for EτE\_{\tau} (increasing in jj) and EuE\_{u} (increasing in kk).

Let NL:=|ℒΩ|=NΩ​nuN\_{L}:=|\mathcal{L}\_{\Omega}|=N\_{\Omega}n\_{u} be the number of lattice nodes,
and enumerate ℒΩ\mathcal{L}\_{\Omega} as

|  |  |  |
| --- | --- | --- |
|  | ℒΩ={ξℓ}ℓ=1NL,ξℓ=(iℓ,jℓ,kℓ).\mathcal{L}\_{\Omega}=\{\xi\_{\ell}\}\_{\ell=1}^{N\_{L}},\qquad\xi\_{\ell}=(i\_{\ell},j\_{\ell},k\_{\ell}). |  |

We identify fog configurations π\pi with vectors in ℝNL\mathbb{R}^{N\_{L}} via
πℓ:=πiℓ,jℓ,kℓ\pi\_{\ell}:=\pi\_{i\_{\ell},j\_{\ell},k\_{\ell}}.

* •

  The *mm-gradient* Dm:ℝNL→ℝ|Em|D\_{m}:\mathbb{R}^{N\_{L}}\to\mathbb{R}^{|E\_{m}|} is
  defined as follows: index Em={er}r=1|Em|E\_{m}=\{e\_{r}\}\_{r=1}^{|E\_{m}|} and for each
  edge er=(p→q)e\_{r}=(p\to q), set

  |  |  |  |
  | --- | --- | --- |
  |  | (Dm​π)r:=πq−πp.(D\_{m}\pi)\_{r}:=\pi\_{q}-\pi\_{p}. |  |

  In matrix form, DmD\_{m} is the |Em|×NL|E\_{m}|\times N\_{L} matrix whose rr-th row
  has entry −1-1 in the column corresponding to node pp, entry +1+1 in
  the column corresponding to node qq, and zeros elsewhere.
* •

  The *τ\tau-gradient* Dτ:ℝNL→ℝ|Eτ|D\_{\tau}:\mathbb{R}^{N\_{L}}\to\mathbb{R}^{|E\_{\tau}|}
  is defined analogously, with one row per edge in EτE\_{\tau}, oriented in
  increasing jj.
* •

  The *uu-gradient* Du:ℝNL→ℝ|Eu|D\_{u}:\mathbb{R}^{N\_{L}}\to\mathbb{R}^{|E\_{u}|} is
  defined analogously, with one row per edge in EuE\_{u}, oriented in
  increasing kk.

Thus Dm​πD\_{m}\pi collects all forward differences of π\pi along mm-edges, and similarly
for DτD\_{\tau} and DuD\_{u}. We now weight these differences by nonnegative edge
weights.

###### Definition 25 (Edge-weight matrices).

Let wrm≥0w^{m}\_{r}\geq 0 be a nonnegative weight associated with the rr-th mm-edge in
EmE\_{m}, and define the diagonal matrix

|  |  |  |
| --- | --- | --- |
|  | Wm:=diag​(w1m,…,w|Em|m)∈ℝ|Em|×|Em|.W\_{m}:=\mathrm{diag}(w^{m}\_{1},\dots,w^{m}\_{|E\_{m}|})\in\mathbb{R}^{|E\_{m}|\times|E\_{m}|}. |  |

Similarly, let wrτ≥0w^{\tau}\_{r}\geq 0 and wru≥0w^{u}\_{r}\geq 0 be edge weights on EτE\_{\tau} and
EuE\_{u}, and define diagonal matrices
Wτ∈ℝ|Eτ|×|Eτ|W\_{\tau}\in\mathbb{R}^{|E\_{\tau}|\times|E\_{\tau}|} and
Wu∈ℝ|Eu|×|Eu|W\_{u}\in\mathbb{R}^{|E\_{u}|\times|E\_{u}|} with these weights on the diagonal.

Typical choices include wrm,wrτ,wru≡1w^{m}\_{r},w^{\tau}\_{r},w^{u}\_{r}\equiv 1 (unweighted differences), or
weights that depend on grid spacings and/or the 2D marginal ni,jn\_{i,j}; the only
property needed here is nonnegativity.

For any such diagonal matrix W⪰0W\succeq 0 and vector xx, we write

|  |  |  |
| --- | --- | --- |
|  | ‖x‖W2:=x⊤​W​x\|x\|\_{W}^{2}:=x^{\top}Wx |  |

for the weighted squared norm.

#### 12.5.2 Kinetic energy and graph Laplacian

We now define the Dirichlet kinetic energy of the fog in terms of these
discrete gradients.

###### Definition 26 (Kinetic energy of the fog).

Let κm,κτ,κu≥0\kappa\_{m},\kappa\_{\tau},\kappa\_{u}\geq 0 be fixed nonnegative parameters. The
*kinetic energy* (Dirichlet energy) of a fog configuration
π∈ℝNL\pi\in\mathbb{R}^{N\_{L}} is

|  |  |  |
| --- | --- | --- |
|  | ℰkin​(π):=κm2​‖Dm​π‖Wm2+κτ2​‖Dτ​π‖Wτ2+κu2​‖Du​π‖Wu2.\mathcal{E}\_{\mathrm{kin}}(\pi):=\frac{\kappa\_{m}}{2}\,\|D\_{m}\pi\|\_{W\_{m}}^{2}+\frac{\kappa\_{\tau}}{2}\,\|D\_{\tau}\pi\|\_{W\_{\tau}}^{2}+\frac{\kappa\_{u}}{2}\,\|D\_{u}\pi\|\_{W\_{u}}^{2}. |  |

Explicitly,

|  |  |  |
| --- | --- | --- |
|  | ℰkin​(π)=κm2​(Dm​π)⊤​Wm​(Dm​π)+κτ2​(Dτ​π)⊤​Wτ​(Dτ​π)+κu2​(Du​π)⊤​Wu​(Du​π).\mathcal{E}\_{\mathrm{kin}}(\pi)=\frac{\kappa\_{m}}{2}\,(D\_{m}\pi)^{\top}W\_{m}(D\_{m}\pi)+\frac{\kappa\_{\tau}}{2}\,(D\_{\tau}\pi)^{\top}W\_{\tau}(D\_{\tau}\pi)+\frac{\kappa\_{u}}{2}\,(D\_{u}\pi)^{\top}W\_{u}(D\_{u}\pi). |  |

The Dirichlet energy is a nonnegative quadratic form in π\pi, and it can be
written in the standard graph-Laplacian form.

###### Proposition 14 (Matrix form and positive semidefiniteness of LπL\_{\pi}).

Define

|  |  |  |
| --- | --- | --- |
|  | Lm:=Dm⊤​Wm​Dm,Lτ:=Dτ⊤​Wτ​Dτ,Lu:=Du⊤​Wu​DuL\_{m}:=D\_{m}^{\top}W\_{m}D\_{m},\qquad L\_{\tau}:=D\_{\tau}^{\top}W\_{\tau}D\_{\tau},\qquad L\_{u}:=D\_{u}^{\top}W\_{u}D\_{u} |  |

and

|  |  |  |
| --- | --- | --- |
|  | Lπ:=κm​Lm+κτ​Lτ+κu​Lu.L\_{\pi}:=\kappa\_{m}L\_{m}+\kappa\_{\tau}L\_{\tau}+\kappa\_{u}L\_{u}. |  |

Then:

1. (i)

   Lm,Lτ,LuL\_{m},L\_{\tau},L\_{u} and LπL\_{\pi} are symmetric positive semidefinite matrices
   in ℝNL×NL\mathbb{R}^{N\_{L}\times N\_{L}};
2. (ii)

   for all π∈ℝNL\pi\in\mathbb{R}^{N\_{L}},

   |  |  |  |
   | --- | --- | --- |
   |  | ℰkin​(π)=12​π⊤​Lπ​π.\mathcal{E}\_{\mathrm{kin}}(\pi)=\frac{1}{2}\,\pi^{\top}L\_{\pi}\pi. |  |

###### Proof.

(i) For any matrix DD and diagonal matrix W⪰0W\succeq 0, the matrix
L:=D⊤​W​DL:=D^{\top}WD is symmetric and positive semidefinite:

|  |  |  |
| --- | --- | --- |
|  | L⊤=(D⊤​W​D)⊤=D⊤​W⊤​D=D⊤​W​D=L,L^{\top}=(D^{\top}WD)^{\top}=D^{\top}W^{\top}D=D^{\top}WD=L, |  |

and for any xx,

|  |  |  |
| --- | --- | --- |
|  | x⊤​L​x=x⊤​D⊤​W​D​x=(D​x)⊤​W​(D​x)≥0,x^{\top}Lx=x^{\top}D^{\top}WDx=(Dx)^{\top}W(Dx)\geq 0, |  |

since WW has nonnegative diagonal entries. Applying this with
(D,W)=(Dm,Wm)(D,W)=(D\_{m},W\_{m}), (Dτ,Wτ)(D\_{\tau},W\_{\tau}) and (Du,Wu)(D\_{u},W\_{u}) yields the claimed properties
for Lm,Lτ,LuL\_{m},L\_{\tau},L\_{u}. A nonnegative linear combination of symmetric positive
semidefinite matrices is again symmetric positive semidefinite, so LπL\_{\pi} is
symmetric positive semidefinite.

(ii) By definition of Lm,Lτ,LuL\_{m},L\_{\tau},L\_{u},

|  |  |  |
| --- | --- | --- |
|  | (Dm​π)⊤​Wm​(Dm​π)=π⊤​Lm​π,(Dτ​π)⊤​Wτ​(Dτ​π)=π⊤​Lτ​π,(D\_{m}\pi)^{\top}W\_{m}(D\_{m}\pi)=\pi^{\top}L\_{m}\pi,\quad(D\_{\tau}\pi)^{\top}W\_{\tau}(D\_{\tau}\pi)=\pi^{\top}L\_{\tau}\pi, |  |

|  |  |  |
| --- | --- | --- |
|  | (Du​π)⊤​Wu​(Du​π)=π⊤​Lu​π.(D\_{u}\pi)^{\top}W\_{u}(D\_{u}\pi)=\pi^{\top}L\_{u}\pi. |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | ℰkin​(π)=12​(κm​π⊤​Lm​π+κτ​π⊤​Lτ​π+κu​π⊤​Lu​π)=12​π⊤​Lπ​π,\mathcal{E}\_{\mathrm{kin}}(\pi)=\frac{1}{2}\bigl(\kappa\_{m}\,\pi^{\top}L\_{m}\pi+\kappa\_{\tau}\,\pi^{\top}L\_{\tau}\pi+\kappa\_{u}\,\pi^{\top}L\_{u}\pi\bigr)=\frac{1}{2}\,\pi^{\top}L\_{\pi}\pi, |  |

which proves the claim.
∎

Consequently, ℰkin\mathcal{E}\_{\mathrm{kin}} is a convex quadratic functional on
ℝNL\mathbb{R}^{N\_{L}}, with flat directions corresponding to fog configurations that
are constant along connected components of the underlying graph (if all
κm,κτ,κu>0\kappa\_{m},\kappa\_{\tau},\kappa\_{u}>0 and the graph is connected with Neumann
boundary, the constant vector lies in the kernel of LπL\_{\pi}).

#### 12.5.3 Potential energy and band-aware penalisation

We now introduce a nonnegative potential field VV on ℒΩ\mathcal{L}\_{\Omega} that
penalises fog mass far from the local bid-ask tubes and from basic price bounds.

###### Definition 27 (Band and range potential).

For each quote qq lying on the patch, let (mq,τq)(m\_{q},\tau\_{q}) be its location and
[bq,aq][b\_{q},a\_{q}] its cleaned forward-discounted bid–ask band, and choose a
representative grid node (iq,jq)∈Ω(i\_{q},j\_{q})\in\Omega (e.g. the nearest neighbour in
Ω\Omega).

Fix parameters αband≥0\alpha\_{\mathrm{band}}\geq 0 and αrange≥0\alpha\_{\mathrm{range}}\geq 0.
Define the *band potential* as

|  |  |  |
| --- | --- | --- |
|  | Vi,j,kband:={αbanddist(uk,[bq,aq])2,if ​(i,j)=(iq,jq)​ for some quote ​q,0,otherwise,V^{\mathrm{band}}\_{i,j,k}:=\begin{cases}\alpha\_{\mathrm{band}}\,\operatorname{dist}(u\_{k},[b\_{q},a\_{q}])^{2},&\text{if }(i,j)=(i\_{q},j\_{q})\text{ for some quote }q,\\[3.0pt] 0,&\text{otherwise},\end{cases} |  |

for all (i,j,k)∈ℒΩ(i,j,k)\in\mathcal{L}\_{\Omega}, where
dist⁡(u,[b,a]):=max⁡{b−u,0,u−a}\operatorname{dist}(u,[b,a]):=\max\{b-u,0,u-a\} is the Euclidean distance
from uu to the interval [b,a][b,a].

Define the *range potential* by

|  |  |  |
| --- | --- | --- |
|  | Vi,j,krange:=αrange​(𝟏{uk<0}+𝟏{uk>Fi,j}),V^{\mathrm{range}}\_{i,j,k}:=\alpha\_{\mathrm{range}}\Bigl(\mathbf{1}\_{\{u\_{k}<0\}}+\mathbf{1}\_{\{u\_{k}>F\_{i,j}\}}\Bigr), |  |

where Fi,jF\_{i,j} is the forward at node (i,j)(i,j) and 𝟏A\mathbf{1}\_{A} is the
indicator of the event AA.

Finally, set

|  |  |  |
| --- | --- | --- |
|  | Vi,j,k:=Vi,j,kband+Vi,j,krange,(i,j,k)∈ℒΩ.V\_{i,j,k}:=V^{\mathrm{band}}\_{i,j,k}+V^{\mathrm{range}}\_{i,j,k},\qquad(i,j,k)\in\mathcal{L}\_{\Omega}. |  |

By construction, Vi,j,k≥0V\_{i,j,k}\geq 0 for all (i,j,k)(i,j,k). The band potential is small
when uku\_{k} lies inside the bid–ask interval associated with the quote at
(iq,jq)(i\_{q},j\_{q}), and grows quadratically as uku\_{k} moves away from that interval; it
is zero at grid nodes that are not directly associated with quotes. The range
potential imposes a hard penalty αrange\alpha\_{\mathrm{range}} whenever uku\_{k} lies
below zero or above the local forward Fi,jF\_{i,j}, discouraging fog from sitting
at obviously unreasonable price levels.

It is convenient to collect the potential values into a vector V∈ℝNLV\in\mathbb{R}^{N\_{L}}
by setting Vℓ:=Viℓ,jℓ,kℓV\_{\ell}:=V\_{i\_{\ell},j\_{\ell},k\_{\ell}} for each lattice index
ℓ=1,…,NL\ell=1,\dots,N\_{L}, and to define the diagonal matrix
diag​(V)∈ℝNL×NL\mathrm{diag}(V)\in\mathbb{R}^{N\_{L}\times N\_{L}} with entries
(diag​(V))ℓ​ℓ=Vℓ(\mathrm{diag}(V))\_{\ell\ell}=V\_{\ell}.

###### Definition 28 (Potential energy of the fog).

The *potential energy* of a fog configuration π∈ℝNL\pi\in\mathbb{R}^{N\_{L}} is

|  |  |  |
| --- | --- | --- |
|  | ℰpot​(π):=12​∑(i,j)∈Ω∑k=1nuVi,j,k​πi,j,k2.\mathcal{E}\_{\mathrm{pot}}(\pi):=\frac{1}{2}\sum\_{(i,j)\in\Omega}\sum\_{k=1}^{n\_{u}}V\_{i,j,k}\,\pi\_{i,j,k}^{2}. |  |

Equivalently, in vector notation,

|  |  |  |
| --- | --- | --- |
|  | ℰpot​(π)=12​π⊤​diag​(V)​π.\mathcal{E}\_{\mathrm{pot}}(\pi)=\frac{1}{2}\,\pi^{\top}\mathrm{diag}(V)\,\pi. |  |

Because Vi,j,k≥0V\_{i,j,k}\geq 0 for all (i,j,k)(i,j,k), the matrix diag​(V)\mathrm{diag}(V) is
symmetric positive semidefinite, and ℰpot\mathcal{E}\_{\mathrm{pot}} is a convex
quadratic functional. Note that ℰpot​(π)\mathcal{E}\_{\mathrm{pot}}(\pi) penalises
large values of πi,j,k\pi\_{i,j,k} at lattice sites where Vi,j,kV\_{i,j,k} is large, i.e. far outside the band tube or the basic price range; it is indifferent to the
sign of πi,j,k\pi\_{i,j,k} as a quadratic form, but in our optimisation the fog
variables are constrained to be nonnegative and to lie on the simplex
𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega).

#### 12.5.4 Hamiltonian energy and basic properties

We now combine kinetic and potential contributions into a single Hamiltonian
energy.

###### Definition 29 (Hamiltonian matrix and energy).

Define the *Hamiltonian matrix* by

|  |  |  |
| --- | --- | --- |
|  | Hπ:=Lπ+diag​(V)∈ℝNL×NL,H\_{\pi}:=L\_{\pi}+\mathrm{diag}(V)\in\mathbb{R}^{N\_{L}\times N\_{L}}, |  |

where LπL\_{\pi} is as in Proposition [14](https://arxiv.org/html/2512.01967v1#Thmprop14 "Proposition 14 (Matrix form and positive semidefiniteness of 𝐿_𝜋). ‣ 12.5.2 Kinetic energy and graph Laplacian ‣ 12.5 Hamiltonian energy on the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") and VV is from
Definition [27](https://arxiv.org/html/2512.01967v1#Thmdefinition27 "Definition 27 (Band and range potential). ‣ 12.5.3 Potential energy and band-aware penalisation ‣ 12.5 Hamiltonian energy on the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"). The *Hamiltonian energy* of a
fog configuration π∈ℝNL\pi\in\mathbb{R}^{N\_{L}} is the quadratic functional

|  |  |  |
| --- | --- | --- |
|  | ℰHam​(π):=12​π⊤​Hπ​π.\mathcal{E}\_{\mathrm{Ham}}(\pi):=\frac{1}{2}\,\pi^{\top}H\_{\pi}\pi. |  |

By construction,

|  |  |  |
| --- | --- | --- |
|  | ℰHam​(π)=ℰkin​(π)+ℰpot​(π).\mathcal{E}\_{\mathrm{Ham}}(\pi)=\mathcal{E}\_{\mathrm{kin}}(\pi)+\mathcal{E}\_{\mathrm{pot}}(\pi). |  |

###### Proposition 15 (Symmetry, positive semidefiniteness, and convexity).

The Hamiltonian matrix HπH\_{\pi} is symmetric positive semidefinite. Consequently,
ℰHam:ℝNL→ℝ+\mathcal{E}\_{\mathrm{Ham}}:\mathbb{R}^{N\_{L}}\to\mathbb{R}\_{+} is a convex quadratic
functional. Moreover, if at least one of the following holds:

* •

  the graph underlying LπL\_{\pi} is connected and
  κm+κτ+κu>0\kappa\_{m}+\kappa\_{\tau}+\kappa\_{u}>0, and
  Vi,j,k>0V\_{i,j,k}>0 at least at one lattice site; or
* •

  more generally, HπH\_{\pi} is positive definite on the affine subspace
  {π∈ℝNL:∑ℓπℓ=1}\{\pi\in\mathbb{R}^{N\_{L}}:\sum\_{\ell}\pi\_{\ell}=1\},

then ℰHam\mathcal{E}\_{\mathrm{Ham}} is strictly convex on the simplex
𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega), and has a unique minimiser on 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega).

###### Proof.

By Proposition [14](https://arxiv.org/html/2512.01967v1#Thmprop14 "Proposition 14 (Matrix form and positive semidefiniteness of 𝐿_𝜋). ‣ 12.5.2 Kinetic energy and graph Laplacian ‣ 12.5 Hamiltonian energy on the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), LπL\_{\pi} is symmetric positive semidefinite.
The matrix diag​(V)\mathrm{diag}(V) is diagonal with nonnegative entries and hence
symmetric positive semidefinite. Therefore their sum Hπ=Lπ+diag​(V)H\_{\pi}=L\_{\pi}+\mathrm{diag}(V) is symmetric positive semidefinite. For any
π∈ℝNL\pi\in\mathbb{R}^{N\_{L}},

|  |  |  |
| --- | --- | --- |
|  | ℰHam​(π)=12​π⊤​Hπ​π≥0.\mathcal{E}\_{\mathrm{Ham}}(\pi)=\frac{1}{2}\,\pi^{\top}H\_{\pi}\pi\geq 0. |  |

A quadratic form with positive semidefinite matrix is convex, so
ℰHam\mathcal{E}\_{\mathrm{Ham}} is convex.

If HπH\_{\pi} is positive definite on a subspace S⊂ℝNLS\subset\mathbb{R}^{N\_{L}} (in
particular, on the subspace tangent to the simplex), then the restriction of
ℰHam\mathcal{E}\_{\mathrm{Ham}} to SS is strictly convex. The simplex
𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) lies in the affine hyperplane
{π:∑ℓπℓ=1}\{\pi:\sum\_{\ell}\pi\_{\ell}=1\}, and the tangent space at any point of the
simplex is the subspace
{δ​π:∑ℓδ​πℓ=0}\{\delta\pi:\sum\_{\ell}\delta\pi\_{\ell}=0\}. If HπH\_{\pi} is positive definite
on this subspace, then ℰHam\mathcal{E}\_{\mathrm{Ham}} is strictly convex on
𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega), and a strictly convex continuous function on a compact
convex set has a unique minimiser. The sufficient condition stated in the
proposition ensures this property in typical settings. The detailed proof of
positive definiteness on the tangent space depends on the connectivity of the
graph and the support of VV and is standard in the theory of weighted graph
Laplacians plus diagonal potentials.
∎

To justify the strict convexity statement in the “moreover” part, we record the
standard argument that under the connectivity and positivity assumptions in the
first bullet HπH\_{\pi} is positive definite on the simplex tangent

|  |  |  |
| --- | --- | --- |
|  | T:={δ​π∈ℝNL:𝟏⊤​δ​π=0}.T:=\{\delta\pi\in\mathbb{R}^{N\_{L}}:\mathbf{1}^{\top}\delta\pi=0\}. |  |

Assume that the underlying graph on LΩL\_{\Omega} is connected and that
κm+κτ+κu>0\kappa\_{m}+\kappa\_{\tau}+\kappa\_{u}>0, so that LπL\_{\pi} is a weighted graph
Laplacian with ker⁡Lπ=span​{𝟏}\ker L\_{\pi}=\mathrm{span}\{\mathbf{1}\}. Suppose in addition
that there exists at least one lattice site ℓ⋆\ell^{\star} with Vℓ⋆>0V\_{\ell^{\star}}>0.
If Hπ​δ​π=0H\_{\pi}\delta\pi=0, then

|  |  |  |
| --- | --- | --- |
|  | 0=δ​π⊤​Hπ​δ​π=δ​π⊤​Lπ​δ​π+δ​π⊤​diag​(V)​δ​π,0=\delta\pi^{\top}H\_{\pi}\delta\pi=\delta\pi^{\top}L\_{\pi}\delta\pi+\delta\pi^{\top}\mathrm{diag}(V)\,\delta\pi, |  |

and both terms on the right-hand side are nonnegative. Hence
δ​π∈ker⁡Lπ∩ker⁡diag​(V)\delta\pi\in\ker L\_{\pi}\cap\ker\mathrm{diag}(V). The first condition implies
δ​π=c​ 1\delta\pi=c\,\mathbf{1} for some c∈ℝc\in\mathbb{R}, while the second forces
δ​πℓ⋆=0\delta\pi\_{\ell^{\star}}=0 and therefore c=0c=0. Thus δ​π=0\delta\pi=0 is the only
vector with δ​π⊤​Hπ​δ​π=0\delta\pi^{\top}H\_{\pi}\delta\pi=0, so HπH\_{\pi} has trivial kernel and is
positive definite. In particular there is no nonzero δ​π∈T\delta\pi\in T with
δ​π⊤​Hπ​δ​π=0\delta\pi^{\top}H\_{\pi}\delta\pi=0, and EHamE\_{\mathrm{Ham}} is strictly convex on
Cπ​(Ω)C\_{\pi}(\Omega) and on its tangent space.

###### Remark 21 (Interpretation of the Hamiltonian energy).

The kinetic energy ℰkin​(π)\mathcal{E}\_{\mathrm{kin}}(\pi) penalises large discrete
gradients of the fog in the (m,τ,u)(m,\tau,u) directions: it is large when π\pi
varies rapidly across neighbouring lattice sites and small when π\pi is
smooth. The potential energy ℰpot​(π)\mathcal{E}\_{\mathrm{pot}}(\pi) penalises fog
mass located at lattice sites with large Vi,j,kV\_{i,j,k}, i.e. far outside
bid–ask tubes or basic price ranges.

On a calm patch with tight bands and reasonable baseline fit, the minimum-energy
fog tends to concentrate its mass at price levels uku\_{k} inside the local bands
and within [0,Fi,j][0,F\_{i,j}], while remaining smooth across neighbouring nodes. On
a stressed patch with conflicting quotes or strong local misfit, a portion of
the fog may be forced to reside outside the bands; in that case
ℰHam\mathcal{E}\_{\mathrm{Ham}} balances the cost of leaking mass out of the band
against the cost of introducing sharp gradients in (m,τ,u)(m,\tau,u).

### 12.6  Noise-aware band term via the fog

We now couple the 3D fog π\pi on ℒΩ\mathcal{L}\_{\Omega} with the nodal surface
u​(uI)u(u\_{I}) at each quote on the patch. The aim is to obtain, for each quote qq,
a band penalty whose effective strength is modulated by the local fog mass
outside the corresponding bid-ask band.

Throughout this section we fix a patch Ω⊂𝒢\Omega\subset\mathcal{G}, an interior
price vector uI∈ℝNΩu\_{I}\in\mathbb{R}^{N\_{\Omega}} with associated full nodal surface
u​(uI)∈ℝGu(u\_{I})\in\mathbb{R}^{G}, and a fog configuration
π=(πi,j,k)(i,j,k)∈ℒΩ∈ℝNΩ​nu\pi=(\pi\_{i,j,k})\_{(i,j,k)\in\mathcal{L}\_{\Omega}}\in\mathbb{R}^{N\_{\Omega}n\_{u}}.

#### 12.6.1 Fog mass outside the band at a quote

We first define, for each quote qq, the fraction of fog mass that lies on
price levels outside the corresponding bid–ask interval.

###### Definition 30 (Index set of out-of-band levels at a quote).

Let qq be a quote associated with location (mq,τq)(m\_{q},\tau\_{q}) and cleaned
forward-discounted band [bq,aq][b\_{q},a\_{q}]. Let (iq,jq)∈Ω(i\_{q},j\_{q})\in\Omega be a fixed
representative of (mq,τq)(m\_{q},\tau\_{q}) on the patch grid. Recall that
{uk}k=1nu\{u\_{k}\}\_{k=1}^{n\_{u}} are the discrete price levels. The *out-of-band index
set* at quote qq is

|  |  |  |
| --- | --- | --- |
|  | 𝒦qout:={k∈{1,…,nu}:uk​<bq​or​uk>​aq}.\mathcal{K}^{\mathrm{out}}\_{q}:=\{k\in\{1,\dots,n\_{u}\}:u\_{k}<b\_{q}\ \text{or}\ u\_{k}>a\_{q}\}. |  |

Thus 𝒦qout\mathcal{K}^{\mathrm{out}}\_{q} collects exactly those vertical levels
uku\_{k} which lie strictly below the bid or strictly above the ask at quote qq.

###### Definition 31 (Local fog mass outside the band at a quote).

For a fog configuration π\pi, the *fog mass outside the band at quote qq*
is defined by

|  |  |  |
| --- | --- | --- |
|  | Mq​(π):=∑k∈𝒦qoutπiq,jq,k.M\_{q}(\pi):=\sum\_{k\in\mathcal{K}^{\mathrm{out}}\_{q}}\pi\_{i\_{q},j\_{q},k}. |  |

By construction πi,j,k≥0\pi\_{i,j,k}\geq 0 for all (i,j,k)∈ℒΩ(i,j,k)\in\mathcal{L}\_{\Omega} on the
feasible set 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega), hence Mq​(π)≥0M\_{q}(\pi)\geq 0 for
all quotes qq. The quantity Mq​(π)M\_{q}(\pi) should be interpreted as the local
probability mass (or “fog thickness”) allocated by π\pi to out-of-band price
levels at quote qq.

###### Remark 22 (Linearity of MqM\_{q}).

For each fixed qq, the map π↦Mq​(π)\pi\mapsto M\_{q}(\pi) is linear: there exists a
vector cq∈ℝNΩ​nuc\_{q}\in\mathbb{R}^{N\_{\Omega}n\_{u}} with entries

|  |  |  |
| --- | --- | --- |
|  | (cq)i,j,k={1,if ​(i,j)=(iq,jq)​and​k∈𝒦qout,0,otherwise,(c\_{q})\_{i,j,k}=\begin{cases}1,&\text{if }(i,j)=(i\_{q},j\_{q})\ \text{and}\ k\in\mathcal{K}\_{q}^{\mathrm{out}},\\[2.0pt] 0,&\text{otherwise},\end{cases} |  |

such that Mq​(π)=cq⊤​πM\_{q}(\pi)=c\_{q}^{\top}\pi for all π\pi. In particular, MqM\_{q} is both
linear and continuous.

#### 12.6.2 Band misfit and noise-aware penalty

We now recall the band misfit at a quote and introduce the noise-aware band
penalty, whose strength is modulated by the local fog mass outside the band.

###### Definition 32 (Band misfit at a quote).

Let S∈ℝQ×GS\in\mathbb{R}^{Q\times G} be the fixed sampling operator mapping nodal
values u∈ℝGu\in\mathbb{R}^{G} to model prices at quote locations. For a given
nodal surface u​(uI)u(u\_{I}), the model price at quote qq is

|  |  |  |
| --- | --- | --- |
|  | Cq​(u):=(S​u)q.C\_{q}(u):=(Su)\_{q}. |  |

The corresponding *band violation* is

|  |  |  |
| --- | --- | --- |
|  | dq​(u):=dist⁡(Cq​(u),[bq,aq])=max⁡{bq−Cq​(u), 0,Cq​(u)−aq}≥0.d\_{q}(u):=\operatorname{dist}\big(C\_{q}(u),[b\_{q},a\_{q}]\big)=\max\{b\_{q}-C\_{q}(u),\ 0,\ C\_{q}(u)-a\_{q}\}\geq 0. |  |

Since u↦Cq​(u)u\mapsto C\_{q}(u) is affine and dist⁡(⋅,[bq,aq])\operatorname{dist}(\cdot,[b\_{q},a\_{q}]) is
the pointwise maximum of three affine functions (see
Definition [5](https://arxiv.org/html/2512.01967v1#Thmdefinition5 "Definition 5 (Baseline band misfit). ‣ 12.2 Badness map and patch decomposition ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), the composition u↦dq​(u)u\mapsto d\_{q}(u)
is a convex function on ℝG\mathbb{R}^{G}. Therefore uI↦dq​(u​(uI))u\_{I}\mapsto d\_{q}(u(u\_{I})) is
also convex on ℝNΩ\mathbb{R}^{N\_{\Omega}} because u​(uI)u(u\_{I}) depends affinely on
uIu\_{I}.

We now define the noise-aware band penalty, which couples the misfit dq​(u)d\_{q}(u)
and the fog mass outside the band Mq​(π)M\_{q}(\pi).

###### Definition 33 (Fog simplex on a patch).

The fog feasible set on Ω\Omega is the probability simplex

|  |  |  |
| --- | --- | --- |
|  | 𝒞π​(Ω):={π∈ℝNΩ​nu:πi,j,k≥0​∀(i,j,k)∈ℒΩ,∑(i,j)∈Ω∑k=1nuπi,j,k=1}.\mathcal{C}\_{\pi}(\Omega):=\left\{\pi\in\mathbb{R}^{N\_{\Omega}n\_{u}}:\pi\_{i,j,k}\geq 0\ \forall(i,j,k)\in\mathcal{L}\_{\Omega},\quad\sum\_{(i,j)\in\Omega}\sum\_{k=1}^{n\_{u}}\pi\_{i,j,k}=1\right\}. |  |

On 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega), the quantity Mq​(π)M\_{q}(\pi) defined in
Definition [31](https://arxiv.org/html/2512.01967v1#Thmdefinition31 "Definition 31 (Local fog mass outside the band at a quote). ‣ 12.6.1 Fog mass outside the band at a quote ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") satisfies 0≤Mq​(π)≤10\leq M\_{q}(\pi)\leq 1 for each qq.

###### Definition 34 (Noise-aware band penalty at a quote).

Fix parameters λnoise≥0\lambda\_{\mathrm{noise}}\geq 0 and ε>0\varepsilon>0. For a given
fog π\pi and quote qq, define

|  |  |  |
| --- | --- | --- |
|  | νq​(π):=ε+Mq​(π)=ε+∑k∈𝒦qoutπiq,jq,k.\nu\_{q}(\pi):=\varepsilon+M\_{q}(\pi)=\varepsilon+\sum\_{k\in\mathcal{K}\_{q}^{\mathrm{out}}}\pi\_{i\_{q},j\_{q},k}. |  |

Then νq​(π)∈[ε,1+ε]\nu\_{q}(\pi)\in[\varepsilon,1+\varepsilon] for all π∈𝒞π​(Ω)\pi\in\mathcal{C}\_{\pi}(\Omega).
Given an interior price vector uI∈ℝNΩu\_{I}\in\mathbb{R}^{N\_{\Omega}}, with associated
nodal surface u=u​(uI)u=u(u\_{I}) and band violation dq​(u)d\_{q}(u), the *noise-aware
band penalty* at quote qq is

|  |  |  |
| --- | --- | --- |
|  | ϕq​(uI,π):=dq​(u)2νq​(π)+λnoise​νq​(π).\phi\_{q}(u\_{I},\pi):=\frac{d\_{q}(u)^{2}}{\nu\_{q}(\pi)}+\lambda\_{\mathrm{noise}}\,\nu\_{q}(\pi). |  |

Intuitively, νq​(π)\nu\_{q}(\pi) is a local “noise scale” at quote qq:
if the fog is almost entirely inside the band, then Mq​(π)M\_{q}(\pi) is small and
νq​(π)≈ε\nu\_{q}(\pi)\approx\varepsilon, so any nonzero violation dq​(u)>0d\_{q}(u)>0 is heavily
penalised by the term dq​(u)2/νq​(π)d\_{q}(u)^{2}/\nu\_{q}(\pi). Conversely, if a significant
fraction of the local fog mass lies outside the band, then Mq​(π)M\_{q}(\pi) and hence
νq​(π)\nu\_{q}(\pi) are larger, making violations dq​(u)>0d\_{q}(u)>0 cheaper; however, large
νq​(π)\nu\_{q}(\pi) is itself penalised linearly through
λnoise​νq​(π)\lambda\_{\mathrm{noise}}\nu\_{q}(\pi).

#### 12.6.3 Convexity of the noise-aware band term

We now establish joint convexity of the noise-aware band term in its two
arguments (uI,π)(u\_{I},\pi), which is crucial for the global convexity of the patch
objective.

The key tool is the *perspective* of a convex function.

###### Definition 35 (Perspective of a convex function).

Let g:ℝ→ℝg:\mathbb{R}\to\mathbb{R} be a convex function with g​(x)≥0g(x)\geq 0 for all
x∈ℝx\in\mathbb{R}. The *perspective* of gg is the function
g~:ℝ×(0,∞)→ℝ\tilde{g}:\mathbb{R}\times(0,\infty)\to\mathbb{R} defined by

|  |  |  |
| --- | --- | --- |
|  | g~​(d,ν):=ν​g​(dν),ν>0.\tilde{g}(d,\nu):=\nu\,g\!\left(\frac{d}{\nu}\right),\qquad\nu>0. |  |

###### Lemma 10 (Convexity of the perspective).

Let g:ℝ→[0,∞)g:\mathbb{R}\to[0,\infty) be convex. Then its perspective
g~​(d,ν)=ν​g​(d/ν)\tilde{g}(d,\nu)=\nu g(d/\nu) is convex on ℝ×(0,∞)\mathbb{R}\times(0,\infty).

###### Proof.

This is a standard result in convex analysis; we recall the argument for
completeness. Let (d1,ν1)(d\_{1},\nu\_{1}) and (d2,ν2)(d\_{2},\nu\_{2}) be in
ℝ×(0,∞)\mathbb{R}\times(0,\infty) and let θ∈[0,1]\theta\in[0,1]. Set

|  |  |  |
| --- | --- | --- |
|  | (d,ν):=θ​(d1,ν1)+(1−θ)​(d2,ν2)=(θ​d1+(1−θ)​d2,θ​ν1+(1−θ)​ν2),(d,\nu):=\theta(d\_{1},\nu\_{1})+(1-\theta)(d\_{2},\nu\_{2})=(\theta d\_{1}+(1-\theta)d\_{2},\ \theta\nu\_{1}+(1-\theta)\nu\_{2}), |  |

with ν>0\nu>0 by convexity of (0,∞)(0,\infty). Then

|  |  |  |
| --- | --- | --- |
|  | dν=θ​ν1ν​d1ν1+(1−θ)​ν2ν​d2ν2,\frac{d}{\nu}=\frac{\theta\nu\_{1}}{\nu}\,\frac{d\_{1}}{\nu\_{1}}+\frac{(1-\theta)\nu\_{2}}{\nu}\,\frac{d\_{2}}{\nu\_{2}}, |  |

where the coefficients

|  |  |  |
| --- | --- | --- |
|  | α1:=θ​ν1ν,α2:=(1−θ)​ν2ν\alpha\_{1}:=\frac{\theta\nu\_{1}}{\nu},\qquad\alpha\_{2}:=\frac{(1-\theta)\nu\_{2}}{\nu} |  |

are nonnegative and satisfy α1+α2=1\alpha\_{1}+\alpha\_{2}=1. By convexity of gg,

|  |  |  |
| --- | --- | --- |
|  | g​(dν)≤α1​g​(d1ν1)+α2​g​(d2ν2).g\!\left(\frac{d}{\nu}\right)\leq\alpha\_{1}g\!\left(\frac{d\_{1}}{\nu\_{1}}\right)+\alpha\_{2}g\!\left(\frac{d\_{2}}{\nu\_{2}}\right). |  |

Multiplying both sides by ν>0\nu>0 yields

|  |  |  |
| --- | --- | --- |
|  | g~​(d,ν)=ν​g​(dν)≤θ​ν1​g​(d1ν1)+(1−θ)​ν2​g​(d2ν2)=θ​g~​(d1,ν1)+(1−θ)​g~​(d2,ν2).\tilde{g}(d,\nu)=\nu g\!\left(\frac{d}{\nu}\right)\leq\theta\nu\_{1}g\!\left(\frac{d\_{1}}{\nu\_{1}}\right)+(1-\theta)\nu\_{2}g\!\left(\frac{d\_{2}}{\nu\_{2}}\right)=\theta\tilde{g}(d\_{1},\nu\_{1})+(1-\theta)\tilde{g}(d\_{2},\nu\_{2}). |  |

Thus g~\tilde{g} is convex on ℝ×(0,∞)\mathbb{R}\times(0,\infty).
∎

We now apply this lemma with g​(x)=x2g(x)=x^{2}.

###### Proposition 16 (Convexity of the noise-aware band term).

Let qq be a quote on the patch. The map

|  |  |  |
| --- | --- | --- |
|  | (uI,π)↦ϕq​(uI,π)(u\_{I},\pi)\mapsto\phi\_{q}(u\_{I},\pi) |  |

defined in Definition [34](https://arxiv.org/html/2512.01967v1#Thmdefinition34 "Definition 34 (Noise-aware band penalty at a quote). ‣ 12.6.2 Band misfit and noise-aware penalty ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") is jointly convex on
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega), where
𝒞u​(Ω)\mathcal{C}\_{u}(\Omega) and 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) are as in
Definitions [21](https://arxiv.org/html/2512.01967v1#Thmdefinition21 "Definition 21 (No-arbitrage feasible set on a patch). ‣ 12.4.3 Patch-level feasible set and its geometry ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") and [33](https://arxiv.org/html/2512.01967v1#Thmdefinition33 "Definition 33 (Fog simplex on a patch). ‣ 12.6.2 Band misfit and noise-aware penalty ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

###### Proof.

We proceed in steps.

*(1) Convexity of dq​(uI)d\_{q}(u\_{I}) in uIu\_{I}.*
The map uI↦u​(uI)u\_{I}\mapsto u(u\_{I}) is affine by construction of the assembly map
(equation ([12.1](https://arxiv.org/html/2512.01967v1#Ch12.E1 "Equation 12.1 ‣ 12.4.1 Interior price variables and assembly map ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"))). The band misfit
dq​(u)=dist⁡(Cq​(u),[bq,aq])d\_{q}(u)=\operatorname{dist}(C\_{q}(u),[b\_{q},a\_{q}]) can be written as

|  |  |  |
| --- | --- | --- |
|  | dq​(u)=max⁡{bq−Cq​(u), 0,Cq​(u)−aq},d\_{q}(u)=\max\{b\_{q}-C\_{q}(u),\ 0,\ C\_{q}(u)-a\_{q}\}, |  |

where u↦Cq​(u)u\mapsto C\_{q}(u) is affine. A pointwise maximum of finitely many affine
functions is convex, hence u↦dq​(u)u\mapsto d\_{q}(u) is convex on ℝG\mathbb{R}^{G}.
Composing with the affine map u​(uI)u(u\_{I}), we obtain that

|  |  |  |
| --- | --- | --- |
|  | uI↦dq​(u​(uI))u\_{I}\mapsto d\_{q}(u(u\_{I})) |  |

is convex on ℝNΩ\mathbb{R}^{N\_{\Omega}} and, in particular, on 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega).

*(2) Affinity and positivity of νq​(π)\nu\_{q}(\pi) in π\pi.*
By Remark [22](https://arxiv.org/html/2512.01967v1#Thmremark22 "Remark 22 (Linearity of 𝑀_𝑞). ‣ 12.6.1 Fog mass outside the band at a quote ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), Mq​(π)M\_{q}(\pi) is a linear functional of π\pi and
is therefore affine. Adding the constant ε>0\varepsilon>0, we obtain

|  |  |  |
| --- | --- | --- |
|  | νq​(π)=ε+Mq​(π),\nu\_{q}(\pi)=\varepsilon+M\_{q}(\pi), |  |

which is an affine function of π\pi. On the simplex 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega)
we have Mq​(π)≥0M\_{q}(\pi)\geq 0, hence

|  |  |  |
| --- | --- | --- |
|  | νq​(π)≥ε>0\nu\_{q}(\pi)\geq\varepsilon>0 |  |

for all π∈𝒞π​(Ω)\pi\in\mathcal{C}\_{\pi}(\Omega). Thus the pair
(dq​(uI),νq​(π))(d\_{q}(u\_{I}),\nu\_{q}(\pi)) always lies in ℝ×(0,∞)\mathbb{R}\times(0,\infty) on the
feasible domain.

*(3) Convexity of (d,ν)↦d2ν(d,\nu)\mapsto\frac{d^{2}}{\nu}.*
Consider the function g:ℝ→[0,∞)g:\mathbb{R}\to[0,\infty) defined by g​(x)=x2g(x)=x^{2}.
It is convex and nonnegative. Its perspective is

|  |  |  |
| --- | --- | --- |
|  | g~​(d,ν):=ν​g​(d/ν)=d2ν,ν>0.\tilde{g}(d,\nu):=\nu g(d/\nu)=\frac{d^{2}}{\nu},\qquad\nu>0. |  |

By Lemma [10](https://arxiv.org/html/2512.01967v1#Thmlemma10 "Lemma 10 (Convexity of the perspective). ‣ 12.6.3 Convexity of the noise-aware band term ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), g~\tilde{g} is convex on
ℝ×(0,∞)\mathbb{R}\times(0,\infty). Hence the map

|  |  |  |
| --- | --- | --- |
|  | (d,ν)↦d2ν(d,\nu)\mapsto\frac{d^{2}}{\nu} |  |

is convex on ℝ×(0,∞)\mathbb{R}\times(0,\infty).

(4) Convexity of (d,ν)↦d2ν+λnoise​ν(d,\nu)\mapsto\frac{d^{2}}{\nu}+\lambda\_{\mathrm{noise}}\nu. The function

|  |  |  |
| --- | --- | --- |
|  | (d,ν)↦λnoise​ν(d,\nu)\mapsto\lambda\_{\mathrm{noise}}\nu |  |

is affine (hence convex) on ℝ×(0,∞)\mathbb{R}\times(0,\infty). The sum of a convex function and an affine
function is convex, so the map

|  |  |  |
| --- | --- | --- |
|  | h​(d,ν):=d2ν+λnoise​νh(d,\nu):=\frac{d^{2}}{\nu}+\lambda\_{\mathrm{noise}}\nu |  |

is convex on ℝ×(0,∞)\mathbb{R}\times(0,\infty). Moreover, for each fixed ν>0\nu>0, the function
d↦h​(d,ν)d\mapsto h(d,\nu) is nondecreasing on [0,∞)[0,\infty), since

|  |  |  |
| --- | --- | --- |
|  | ∂∂d​h​(d,ν)=2​dν≥0for all ​d≥0.\frac{\partial}{\partial d}\,h(d,\nu)=\frac{2d}{\nu}\geq 0\quad\text{for all }d\geq 0. |  |

(5) Joint convexity of φq​(uI,π)\varphi\_{q}(u\_{I},\pi). Let (uI1,π1)(u\_{I}^{1},\pi^{1}) and (uI2,π2)(u\_{I}^{2},\pi^{2}) be arbitrary
points in 𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega) and let θ∈[0,1]\theta\in[0,1]. Define

|  |  |  |
| --- | --- | --- |
|  | (uIθ,πθ):=θ​(uI1,π1)+(1−θ)​(uI2,π2)∈𝒞u​(Ω)×𝒞π​(Ω).(u\_{I}^{\theta},\pi^{\theta}):=\theta(u\_{I}^{1},\pi^{1})+(1-\theta)(u\_{I}^{2},\pi^{2})\in\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega). |  |

For i=1,2i=1,2 set

|  |  |  |
| --- | --- | --- |
|  | di:=dq​(u​(uIi)),νi:=νq​(πi),d\_{i}:=d\_{q}(u(u\_{I}^{i})),\qquad\nu\_{i}:=\nu\_{q}(\pi^{i}), |  |

and similarly

|  |  |  |
| --- | --- | --- |
|  | dθ:=dq​(u​(uIθ)),νθ:=νq​(πθ).d\_{\theta}:=d\_{q}(u(u\_{I}^{\theta})),\qquad\nu\_{\theta}:=\nu\_{q}(\pi^{\theta}). |  |

By construction dq​(⋅)d\_{q}(\cdot) is a distance to the interval [bq,aq][b\_{q},a\_{q}], hence dq​(u)≥0d\_{q}(u)\geq 0 for all
uu, and therefore di,dθ≥0d\_{i},d\_{\theta}\geq 0. From (1), the map uI↦dq​(u​(uI))u\_{I}\mapsto d\_{q}(u(u\_{I})) is convex, so

|  |  |  |
| --- | --- | --- |
|  | dθ=dq​(u​(uIθ))≤θ​dq​(u​(uI1))+(1−θ)​dq​(u​(uI2))=θ​d1+(1−θ)​d2.d\_{\theta}=d\_{q}\bigl(u(u\_{I}^{\theta})\bigr)\leq\theta\,d\_{q}\bigl(u(u\_{I}^{1})\bigr)+(1-\theta)\,d\_{q}\bigl(u(u\_{I}^{2})\bigr)=\theta d\_{1}+(1-\theta)d\_{2}. |  |

From (2), νq​(π)\nu\_{q}(\pi) is affine in π\pi, hence

|  |  |  |
| --- | --- | --- |
|  | νθ=νq​(πθ)=θ​νq​(π1)+(1−θ)​νq​(π2)=θ​ν1+(1−θ)​ν2.\nu\_{\theta}=\nu\_{q}(\pi^{\theta})=\theta\nu\_{q}(\pi^{1})+(1-\theta)\nu\_{q}(\pi^{2})=\theta\nu\_{1}+(1-\theta)\nu\_{2}. |  |

Recall that φq​(uI,π)=h​(dq​(u​(uI)),νq​(π))\varphi\_{q}(u\_{I},\pi)=h(d\_{q}(u(u\_{I})),\nu\_{q}(\pi)) with hh convex on
ℝ×(0,∞)\mathbb{R}\times(0,\infty) by (4), and that for each ν>0\nu>0 the map d↦h​(d,ν)d\mapsto h(d,\nu) is
nondecreasing on [0,∞)[0,\infty). Using dθ≥0d\_{\theta}\geq 0 and dθ≤θ​d1+(1−θ)​d2d\_{\theta}\leq\theta d\_{1}+(1-\theta)d\_{2},
monotonicity in the first argument yields

|  |  |  |
| --- | --- | --- |
|  | h​(dθ,νθ)≤h​(θ​d1+(1−θ)​d2,νθ)=h​(θ​d1+(1−θ)​d2,θ​ν1+(1−θ)​ν2).h(d\_{\theta},\nu\_{\theta})\leq h\bigl(\theta d\_{1}+(1-\theta)d\_{2},\;\nu\_{\theta}\bigr)=h\bigl(\theta d\_{1}+(1-\theta)d\_{2},\;\theta\nu\_{1}+(1-\theta)\nu\_{2}\bigr). |  |

The pair on the right-hand side is exactly the convex combination

|  |  |  |
| --- | --- | --- |
|  | (θ​d1+(1−θ)​d2,θ​ν1+(1−θ)​ν2)=θ​(d1,ν1)+(1−θ)​(d2,ν2).\bigl(\theta d\_{1}+(1-\theta)d\_{2},\;\theta\nu\_{1}+(1-\theta)\nu\_{2}\bigr)=\theta(d\_{1},\nu\_{1})+(1-\theta)(d\_{2},\nu\_{2}). |  |

By convexity of hh we therefore have

|  |  |  |
| --- | --- | --- |
|  | h​(θ​d1+(1−θ)​d2,θ​ν1+(1−θ)​ν2)≤θ​h​(d1,ν1)+(1−θ)​h​(d2,ν2).h\bigl(\theta d\_{1}+(1-\theta)d\_{2},\;\theta\nu\_{1}+(1-\theta)\nu\_{2}\bigr)\leq\theta h(d\_{1},\nu\_{1})+(1-\theta)h(d\_{2},\nu\_{2}). |  |

Combining the two inequalities gives

|  |  |  |
| --- | --- | --- |
|  | h​(dθ,νθ)≤θ​h​(d1,ν1)+(1−θ)​h​(d2,ν2).h(d\_{\theta},\nu\_{\theta})\leq\theta h(d\_{1},\nu\_{1})+(1-\theta)h(d\_{2},\nu\_{2}). |  |

Rewriting in terms of φq\varphi\_{q},

|  |  |  |
| --- | --- | --- |
|  | φq​(uIθ,πθ)=h​(dθ,νθ)≤θ​h​(d1,ν1)+(1−θ)​h​(d2,ν2)=θ​φq​(uI1,π1)+(1−θ)​φq​(uI2,π2).\varphi\_{q}(u\_{I}^{\theta},\pi^{\theta})=h(d\_{\theta},\nu\_{\theta})\leq\theta h(d\_{1},\nu\_{1})+(1-\theta)h(d\_{2},\nu\_{2})=\theta\varphi\_{q}(u\_{I}^{1},\pi^{1})+(1-\theta)\varphi\_{q}(u\_{I}^{2},\pi^{2}). |  |

This is exactly the defining inequality for joint convexity of
(uI,π)↦φq​(uI,π)(u\_{I},\pi)\mapsto\varphi\_{q}(u\_{I},\pi) on 𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega).
∎

###### Remark 23 (Interpretation of the noise-aware band penalty).

The penalty ϕq​(uI,π)\phi\_{q}(u\_{I},\pi) can be seen as an adaptive band penalty whose
effective stiffness is controlled by the fog. When the local fog mass outside
the band is small (Mq​(π)≈0M\_{q}(\pi)\approx 0, thus νq​(π)≈ε\nu\_{q}(\pi)\approx\varepsilon),
any nonzero violation dq​(u)d\_{q}(u) incurs a large cost dq​(u)2/νq​(π)d\_{q}(u)^{2}/\nu\_{q}(\pi),
forcing the surface uu to stay tightly inside the band. When the fog assigns
significant mass to out-of-band price levels (Mq​(π)M\_{q}(\pi) large), violations
become cheaper but increase the “noise budget” λnoise​νq​(π)\lambda\_{\mathrm{noise}}\nu\_{q}(\pi). The optimiser can therefore treat a subset of quotes as noisy
(outliers) by allowing the fog to populate out-of-band regions, but must pay a
linear cost for doing so, while still operating within a globally convex
framework.

### 12.7  Surface energy and closeness to the baseline

On each patch Ω\Omega we regularise the surface in two complementary ways:

1. (i)

   by penalising roughness of the implied risk-neutral density in a patch-level influence region,
2. (ii)

   by penalising deviations from the baseline nodal values on Ω\Omega.

Both terms are quadratic in the interior vector uIu\_{I} and yield convex contributions to the patch objective.

#### 12.7.1 Discrete density operator and patch restriction

Recall that the (continuum) risk-neutral density associated with the forward-
discounted call surface Cf​(K,τ)C\_{f}(K,\tau) is

|  |  |  |
| --- | --- | --- |
|  | ρ​(K,τ):=∂K​KCf​(K,τ).\rho(K,\tau):=\partial\_{KK}C\_{f}(K,\tau). |  |

On the nodal grid 𝒢\mathcal{G}, and on any additional grid used to represent
densities (for instance a collocation grid in (K,τ)(K,\tau)), the Breeden-Litzenberger
relation is implemented by a fixed linear operator that maps nodal prices to
discretised densities.

###### Assumption 2 (Global discrete density operator).

There exists a finite set of density evaluation points

|  |  |  |
| --- | --- | --- |
|  | 𝒢ρ={(Kr,τr)}r=1Nρ,\mathcal{G}\_{\rho}=\{(K\_{r},\tau\_{r})\}\_{r=1}^{N\_{\rho}}, |  |

and a matrix Dρ∈ℝNρ×GD\_{\rho}\in\mathbb{R}^{N\_{\rho}\times G} such that, for every
nodal vector u∈ℝGu\in\mathbb{R}^{G}, the vector

|  |  |  |
| --- | --- | --- |
|  | ρ​(u):=Dρ​u∈ℝNρ\rho(u):=D\_{\rho}u\in\mathbb{R}^{N\_{\rho}} |  |

represents the discrete risk-neutral density evaluated at the points in
𝒢ρ\mathcal{G}\_{\rho}.

We are interested only in those density points that are influenced by the patch
Ω\Omega, namely points whose density values depend (possibly together with
off-patch values) on at least one interior node in Ω\Omega.

###### Definition 36 (Patch influence region in density space).

Let PΩ∈ℝG×NΩP\_{\Omega}\in\mathbb{R}^{G\times N\_{\Omega}} be the patch assembly matrix
from ([12.1](https://arxiv.org/html/2512.01967v1#Ch12.E1 "Equation 12.1 ‣ 12.4.1 Interior price variables and assembly map ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), which injects an interior vector
uI∈ℝNΩu\_{I}\in\mathbb{R}^{N\_{\Omega}} into the full nodal vector. We write the full
surface as

|  |  |  |
| --- | --- | --- |
|  | u​(uI)=PΩ​uI+u0,off,u(u\_{I})=P\_{\Omega}u\_{I}+u^{0,\mathrm{off}}, |  |

where u0,off∈ℝGu^{0,\mathrm{off}}\in\mathbb{R}^{G} is the off-patch baseline contribution
(ui,j0,off=0u^{0,\mathrm{off}}\_{i,j}=0 for (i,j)∈Ω(i,j)\in\Omega and
ui,j0,off=ui,j0u^{0,\mathrm{off}}\_{i,j}=u^{0}\_{i,j} otherwise).

Define the *patch influence index set* in density space by

|  |  |  |
| --- | --- | --- |
|  | ℐρ​(Ω):={r∈{1,…,Nρ}:(Dρ​PΩ)r,⋅≠0},\mathcal{I}\_{\rho}(\Omega):=\Big\{r\in\{1,\dots,N\_{\rho}\}:\bigl(D\_{\rho}P\_{\Omega}\bigr)\_{r,\cdot}\neq 0\Big\}, |  |

namely those density rows whose value depends on at least one interior node in
Ω\Omega. Let Nρ,Ω:=|ℐρ​(Ω)|N\_{\rho,\Omega}:=|\mathcal{I}\_{\rho}(\Omega)|, and define the
restriction operator RΩ∈ℝNρ,Ω×NρR\_{\Omega}\in\mathbb{R}^{N\_{\rho,\Omega}\times N\_{\rho}} that
extracts the components with indices in ℐρ​(Ω)\mathcal{I}\_{\rho}(\Omega).

Thus, given uIu\_{I}, the vector RΩ​ρ​(u​(uI))R\_{\Omega}\rho(u(u\_{I})) collects precisely those
density values that are affected by the patch Ω\Omega.

###### Definition 37 (Patch-level density map).

With DρD\_{\rho} and RΩR\_{\Omega} as above, define

|  |  |  |
| --- | --- | --- |
|  | ρΩ​(uI):=RΩ​ρ​(u​(uI))=RΩ​Dρ​(PΩ​uI+u0,off).\rho\_{\Omega}(u\_{I}):=R\_{\Omega}\rho(u(u\_{I}))=R\_{\Omega}D\_{\rho}(P\_{\Omega}u\_{I}+u^{0,\mathrm{off}}). |  |

We write this as an affine map

|  |  |  |
| --- | --- | --- |
|  | ρΩ​(uI)=BΩ​uI+ρoff,\rho\_{\Omega}(u\_{I})=B\_{\Omega}u\_{I}+\rho\_{\mathrm{off}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | BΩ:=RΩ​Dρ​PΩ∈ℝNρ,Ω×NΩ,ρoff:=RΩ​Dρ​u0,off∈ℝNρ,Ω.B\_{\Omega}:=R\_{\Omega}D\_{\rho}P\_{\Omega}\in\mathbb{R}^{N\_{\rho,\Omega}\times N\_{\Omega}},\qquad\rho\_{\mathrm{off}}:=R\_{\Omega}D\_{\rho}u^{0,\mathrm{off}}\in\mathbb{R}^{N\_{\rho,\Omega}}. |  |

By construction, ρΩ​(uI)\rho\_{\Omega}(u\_{I}) collects exactly the density values on the
patch influence region, and depends affinely on the interior vector uIu\_{I}.

#### 12.7.2 Surface density energy

We now penalise rough or irregular density configurations on the patch influence
region via a quadratic form in ρΩ​(uI)\rho\_{\Omega}(u\_{I}).

###### Definition 38 (Surface density energy).

Let Hρ∈ℝNρ,Ω×Nρ,ΩH\_{\rho}\in\mathbb{R}^{N\_{\rho,\Omega}\times N\_{\rho,\Omega}} be a fixed
symmetric positive semidefinite matrix, Hρ⪰0H\_{\rho}\succeq 0. For example, HρH\_{\rho}
may encode a discrete H−1H^{-1}-type smoothing operator or a weighted graph
Laplacian on 𝒢ρ\mathcal{G}\_{\rho} restricted to ℐρ​(Ω)\mathcal{I}\_{\rho}(\Omega). The
*surface density energy* associated with an interior vector uIu\_{I} is

|  |  |  |
| --- | --- | --- |
|  | Esurf​(uI):=12​ρΩ​(uI)⊤​Hρ​ρΩ​(uI).E\_{\mathrm{surf}}(u\_{I}):=\frac{1}{2}\,\rho\_{\Omega}(u\_{I})^{\top}H\_{\rho}\,\rho\_{\Omega}(u\_{I}). |  |

Because ρΩ​(uI)=BΩ​uI+ρoff\rho\_{\Omega}(u\_{I})=B\_{\Omega}u\_{I}+\rho\_{\mathrm{off}} is affine in
uIu\_{I}, EsurfE\_{\mathrm{surf}} is a quadratic functional of uIu\_{I}. We make this
explicit.

###### Proposition 17 (Quadratic form and convexity of EsurfE\_{\mathrm{surf}}).

The surface density energy can be written as

|  |  |  |
| --- | --- | --- |
|  | Esurf​(uI)=12​uI⊤​Qρ​uI+cρ⊤​uI+c0,E\_{\mathrm{surf}}(u\_{I})=\frac{1}{2}\,u\_{I}^{\top}Q\_{\rho}u\_{I}+c\_{\rho}^{\top}u\_{I}+c\_{0}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | Qρ:=BΩ⊤​Hρ​BΩ⪰0,cρ:=BΩ⊤​Hρ​ρoff,c0:=12​ρoff⊤​Hρ​ρoff.Q\_{\rho}:=B\_{\Omega}^{\top}H\_{\rho}B\_{\Omega}\succeq 0,\qquad c\_{\rho}:=B\_{\Omega}^{\top}H\_{\rho}\rho\_{\mathrm{off}},\qquad c\_{0}:=\frac{1}{2}\,\rho\_{\mathrm{off}}^{\top}H\_{\rho}\rho\_{\mathrm{off}}. |  |

In particular, EsurfE\_{\mathrm{surf}} is a convex quadratic function of uIu\_{I} with
Hessian QρQ\_{\rho}.

###### Proof.

Substituting the affine form ρΩ​(uI)=BΩ​uI+ρoff\rho\_{\Omega}(u\_{I})=B\_{\Omega}u\_{I}+\rho\_{\mathrm{off}}
into Definition [38](https://arxiv.org/html/2512.01967v1#Thmdefinition38 "Definition 38 (Surface density energy). ‣ 12.7.2 Surface density energy ‣ 12.7 Surface energy and closeness to the baseline ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), we obtain

|  |  |  |
| --- | --- | --- |
|  | Esurf​(uI)=12​(BΩ​uI+ρoff)⊤​Hρ​(BΩ​uI+ρoff).E\_{\mathrm{surf}}(u\_{I})=\frac{1}{2}\,(B\_{\Omega}u\_{I}+\rho\_{\mathrm{off}})^{\top}H\_{\rho}\,(B\_{\Omega}u\_{I}+\rho\_{\mathrm{off}}). |  |

Expanding the quadratic form yields

|  |  |  |
| --- | --- | --- |
|  | Esurf​(uI)=12​uI⊤​BΩ⊤​Hρ​BΩ​uI+uI⊤​BΩ⊤​Hρ​ρoff+12​ρoff⊤​Hρ​ρoff.E\_{\mathrm{surf}}(u\_{I})=\frac{1}{2}\,u\_{I}^{\top}B\_{\Omega}^{\top}H\_{\rho}B\_{\Omega}u\_{I}+u\_{I}^{\top}B\_{\Omega}^{\top}H\_{\rho}\rho\_{\mathrm{off}}+\frac{1}{2}\,\rho\_{\mathrm{off}}^{\top}H\_{\rho}\rho\_{\mathrm{off}}. |  |

Identifying

|  |  |  |
| --- | --- | --- |
|  | Qρ:=BΩ⊤​Hρ​BΩ,cρ:=BΩ⊤​Hρ​ρoff,c0:=12​ρoff⊤​Hρ​ρoff,Q\_{\rho}:=B\_{\Omega}^{\top}H\_{\rho}B\_{\Omega},\quad c\_{\rho}:=B\_{\Omega}^{\top}H\_{\rho}\rho\_{\mathrm{off}},\quad c\_{0}:=\frac{1}{2}\,\rho\_{\mathrm{off}}^{\top}H\_{\rho}\rho\_{\mathrm{off}}, |  |

we obtain the claimed quadratic representation. Since Hρ⪰0H\_{\rho}\succeq 0, we have
for any x∈ℝNΩx\in\mathbb{R}^{N\_{\Omega}},

|  |  |  |
| --- | --- | --- |
|  | x⊤​Qρ​x=x⊤​BΩ⊤​Hρ​BΩ​x=(BΩ​x)⊤​Hρ​(BΩ​x)≥0.x^{\top}Q\_{\rho}x=x^{\top}B\_{\Omega}^{\top}H\_{\rho}B\_{\Omega}x=(B\_{\Omega}x)^{\top}H\_{\rho}(B\_{\Omega}x)\geq 0. |  |

Thus Qρ⪰0Q\_{\rho}\succeq 0, and the Hessian of EsurfE\_{\mathrm{surf}} with respect to
uIu\_{I} is positive semidefinite. A quadratic function with positive semidefinite
Hessian is convex, hence EsurfE\_{\mathrm{surf}} is convex in uIu\_{I}.
∎

In particular, EsurfE\_{\mathrm{surf}} penalises interior configurations uIu\_{I} that
produce “rough” or oscillatory risk-neutral densities in the patch influence
region, with the exact notion of roughness encoded by HρH\_{\rho}.

#### 12.7.3 Closeness to the baseline

We also penalise departures of the patch interior from the baseline nodal
values, in order to avoid gratuitous changes that are not required by the data
and no-arbitrage constraints.

###### Definition 39 (Closeness to the baseline).

Let uI0∈ℝNΩu\_{I}^{0}\in\mathbb{R}^{N\_{\Omega}} be the vector of baseline nodal values on
Ω\Omega, extracted from u0u^{0}, and fix a parameter λcl>0\lambda\_{\mathrm{cl}}>0.
The *closeness* (or Tikhonov) term on Ω\Omega is

|  |  |  |
| --- | --- | --- |
|  | Ecl(uI):=λcl2∥uI−uI0∥22=λcl2(uI−uI0)⊤(uI−uI0).E\_{\mathrm{cl}}(u\_{I}):=\frac{\lambda\_{\mathrm{cl}}}{2}\,\|u\_{I}-u\_{I}^{0}\|\_{2}^{2}=\frac{\lambda\_{\mathrm{cl}}}{2}\,(u\_{I}-u\_{I}^{0})^{\top}(u\_{I}-u\_{I}^{0}). |  |

This is a standard ℓ2\ell^{2}-type regulariser that penalises deviations from the
baseline. Its convexity and strict positive definiteness are immediate.

###### Proposition 18 (Strict convexity of EclE\_{\mathrm{cl}}).

The functional Ecl:ℝNΩ→ℝ+E\_{\mathrm{cl}}:\mathbb{R}^{N\_{\Omega}}\to\mathbb{R}\_{+} is a
strictly convex quadratic function of uIu\_{I} with Hessian
λcl​INΩ≻0\lambda\_{\mathrm{cl}}I\_{N\_{\Omega}}\succ 0.

###### Proof.

Expanding the square, we have

|  |  |  |
| --- | --- | --- |
|  | Ecl​(uI)=λcl2​(uI⊤​uI−2​uI⊤​uI0+uI0⊤​uI0),E\_{\mathrm{cl}}(u\_{I})=\frac{\lambda\_{\mathrm{cl}}}{2}\,(u\_{I}^{\top}u\_{I}-2u\_{I}^{\top}u\_{I}^{0}+u\_{I}^{0\top}u\_{I}^{0}), |  |

so

|  |  |  |
| --- | --- | --- |
|  | Ecl​(uI)=λcl2​uI⊤​uI−λcl​uI0⊤​uI+λcl2​uI0⊤​uI0.E\_{\mathrm{cl}}(u\_{I})=\frac{\lambda\_{\mathrm{cl}}}{2}\,u\_{I}^{\top}u\_{I}-\lambda\_{\mathrm{cl}}\,u\_{I}^{0\top}u\_{I}+\frac{\lambda\_{\mathrm{cl}}}{2}\,u\_{I}^{0\top}u\_{I}^{0}. |  |

The Hessian with respect to uIu\_{I} is λcl​INΩ\lambda\_{\mathrm{cl}}I\_{N\_{\Omega}},
which is positive definite since λcl>0\lambda\_{\mathrm{cl}}>0. A quadratic
functional with positive definite Hessian is strictly convex, so
EclE\_{\mathrm{cl}} is strictly convex on ℝNΩ\mathbb{R}^{N\_{\Omega}}.
∎

###### Remark 24 (Combined surface regularisation).

Both EsurfE\_{\mathrm{surf}} and EclE\_{\mathrm{cl}} are convex quadratic functionals
of uIu\_{I}. The combined surface regulariser

|  |  |  |
| --- | --- | --- |
|  | uI↦Ecl​(uI)+λsurf​Esurf​(uI),λsurf≥0,u\_{I}\mapsto E\_{\mathrm{cl}}(u\_{I})+\lambda\_{\mathrm{surf}}E\_{\mathrm{surf}}(u\_{I}),\qquad\lambda\_{\mathrm{surf}}\geq 0, |  |

is therefore convex. If either λcl>0\lambda\_{\mathrm{cl}}>0 or the matrix
Qρ=BΩ⊤​Hρ​BΩQ\_{\rho}=B\_{\Omega}^{\top}H\_{\rho}B\_{\Omega} is positive definite on the relevant
subspace, the combined regulariser is strictly convex, which contributes to
uniqueness of the patch-level minimiser.

### 12.8  Patch-level post-fit optimisation problem

We now assemble the various ingredients introduced above into a single
patch-level objective and formulate the post-fit optimisation problem on a
patch Ω⊂𝒢\Omega\subset\mathcal{G}.

#### 12.8.1 Fog feasible set and quote index set

Recall that on Ω\Omega the fog variables are

|  |  |  |
| --- | --- | --- |
|  | π=(πi,j,k)(i,j,k)∈ℒΩ∈ℝNΩ​nu,\pi=(\pi\_{i,j,k})\_{(i,j,k)\in\mathcal{L}\_{\Omega}}\in\mathbb{R}^{N\_{\Omega}n\_{u}}, |  |

where πi,j,k\pi\_{i,j,k} represents the fog mass at (mi,τj,uk)(m\_{i},\tau\_{j},u\_{k}) and
ℒΩ={(i,j,k):(i,j)∈Ω,k=1,…,nu}\mathcal{L}\_{\Omega}=\{(i,j,k):(i,j)\in\Omega,\ k=1,\dots,n\_{u}\}.

###### Definition 40 (Fog feasible set on a patch).

The *fog feasible set* on Ω\Omega is the probability simplex

|  |  |  |
| --- | --- | --- |
|  | 𝒞π​(Ω):={π∈ℝNΩ​nu:πi,j,k≥0​∀(i,j,k)∈ℒΩ,∑(i,j)∈Ω∑k=1nuπi,j,k=1}.\mathcal{C}\_{\pi}(\Omega):=\left\{\pi\in\mathbb{R}^{N\_{\Omega}n\_{u}}:\pi\_{i,j,k}\geq 0\ \forall(i,j,k)\in\mathcal{L}\_{\Omega},\quad\sum\_{(i,j)\in\Omega}\sum\_{k=1}^{n\_{u}}\pi\_{i,j,k}=1\right\}. |  |

###### Lemma 11 (Geometry of 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega)).

The set 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) is a nonempty, compact, convex polytope in
ℝNΩ​nu\mathbb{R}^{N\_{\Omega}n\_{u}}.

###### Proof.

Nonemptiness is obvious, for example the uniform vector
πi,j,k=1/(NΩ​nu)\pi\_{i,j,k}=1/(N\_{\Omega}n\_{u}) belongs to 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega). The
constraints defining 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) consist of finitely many linear
equalities and inequalities:

|  |  |  |
| --- | --- | --- |
|  | πi,j,k≥0,∑(i,j)∈Ω∑k=1nuπi,j,k=1.\pi\_{i,j,k}\geq 0,\quad\sum\_{(i,j)\in\Omega}\sum\_{k=1}^{n\_{u}}\pi\_{i,j,k}=1. |  |

Thus 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) is the intersection of a finite number of closed
half-spaces (one per inequality) and a hyperplane (the equality constraint), so
it is a closed convex polyhedron. The additional equality fixing the total mass
to 11 implies boundedness: all coordinates are nonnegative and sum to 11, so
0≤πi,j,k≤10\leq\pi\_{i,j,k}\leq 1 for every (i,j,k)(i,j,k). A closed and bounded subset of
ℝNΩ​nu\mathbb{R}^{N\_{\Omega}n\_{u}} is compact. Being a bounded polyhedron, it is in
fact a polytope.
∎

We also need to know which quotes interact with a given patch.

###### Definition 41 (Quote index set attached to a patch).

Let S∈ℝQ×GS\in\mathbb{R}^{Q\times G} be the sampling operator mapping nodal prices
to quote locations, so that Cq​(u)=(S​u)qC\_{q}(u)=(Su)\_{q} for q=1,…,Qq=1,\dots,Q. Each row of
SS has finite support (the interpolation stencil of that quote). We define

|  |  |  |
| --- | --- | --- |
|  | QΩ:={q∈{1,…,Q}:the stencil of row q of S intersects ​Ω}.Q\_{\Omega}:=\Bigl\{q\in\{1,\dots,Q\}:\text{the stencil of row $q$ of $S$ intersects }\Omega\Bigr\}. |  |

Equivalently, q∈QΩq\in Q\_{\Omega} if and only if there exists (i,j)∈Ω(i,j)\in\Omega such
that the nodal value ui,ju\_{i,j} enters (S​u)q(Su)\_{q} with nonzero weight.

Thus QΩQ\_{\Omega} collects exactly those quotes whose model prices depend on at
least one interior node of Ω\Omega; the remaining quotes are insensitive to
changes on Ω\Omega and need not appear in the patch objective.

#### 12.8.2 Patch energy functional

We now define the patch-level energy as a sum of four components:
noise-aware band penalties, closeness-to-baseline, density regularisation, and
Hamiltonian energy of the fog.

Recall:

* •

  ϕq​(uI,π)\phi\_{q}(u\_{I},\pi) is the noise-aware band penalty at quote qq, defined
  in Definition [34](https://arxiv.org/html/2512.01967v1#Thmdefinition34 "Definition 34 (Noise-aware band penalty at a quote). ‣ 12.6.2 Band misfit and noise-aware penalty ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), with u=u​(uI)u=u(u\_{I}) assembled from uIu\_{I};
* •

  Ecl​(uI)E\_{\mathrm{cl}}(u\_{I}) is the closeness energy from
  Definition [39](https://arxiv.org/html/2512.01967v1#Thmdefinition39 "Definition 39 (Closeness to the baseline). ‣ 12.7.3 Closeness to the baseline ‣ 12.7 Surface energy and closeness to the baseline ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit");
* •

  Esurf​(uI)E\_{\mathrm{surf}}(u\_{I}) is the surface density energy from
  Definition [38](https://arxiv.org/html/2512.01967v1#Thmdefinition38 "Definition 38 (Surface density energy). ‣ 12.7.2 Surface density energy ‣ 12.7 Surface energy and closeness to the baseline ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit");
* •

  ℰHam​(π)\mathcal{E}\_{\mathrm{Ham}}(\pi) is the Hamiltonian energy of the fog
  from Definition [29](https://arxiv.org/html/2512.01967v1#Thmdefinition29 "Definition 29 (Hamiltonian matrix and energy). ‣ 12.5.4 Hamiltonian energy and basic properties ‣ 12.5 Hamiltonian energy on the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").

###### Definition 42 (Patch energy functional).

Fix nonnegative weights

|  |  |  |
| --- | --- | --- |
|  | λnoise,λsurf,λπ≥0,\lambda\_{\mathrm{noise}},\ \lambda\_{\mathrm{surf}},\ \lambda\_{\pi}\ \geq 0, |  |

and recall that λcl>0\lambda\_{\mathrm{cl}}>0 is part of the definition of
EclE\_{\mathrm{cl}}. For an interior vector uI∈𝒞u​(Ω)u\_{I}\in\mathcal{C}\_{u}(\Omega) and a fog
π∈𝒞π​(Ω)\pi\in\mathcal{C}\_{\pi}(\Omega), the *patch energy* is the functional
JΩ:𝒞u​(Ω)×𝒞π​(Ω)→ℝJ\_{\Omega}:\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega)\to\mathbb{R} defined
by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | JΩ​(uI,π)\displaystyle J\_{\Omega}(u\_{I},\pi) | :=∑q∈QΩϕq​(uI,π)+Ecl​(uI)+λsurf​Esurf​(uI)+λπ​ℰHam​(π)\displaystyle=\sum\_{q\in Q\_{\Omega}}\phi\_{q}(u\_{I},\pi)+E\_{\mathrm{cl}}(u\_{I})+\lambda\_{\mathrm{surf}}\,E\_{\mathrm{surf}}(u\_{I})+\lambda\_{\pi}\,\mathcal{E}\_{\mathrm{Ham}}(\pi) |  | (12.3) |
|  |  | =∑q∈QΩ(dq​(u)2ε+Mq​(π)+λnoise​(ε+Mq​(π)))\displaystyle=\sum\_{q\in Q\_{\Omega}}\left(\frac{d\_{q}(u)^{2}}{\varepsilon+M\_{q}(\pi)}+\lambda\_{\mathrm{noise}}\bigl(\varepsilon+M\_{q}(\pi)\bigr)\right) |  |
|  |  | +λcl2​‖uI−uI0‖22+λsurf2​ρΩ​(uI)⊤​Hρ​ρΩ​(uI)+λπ2​π⊤​Hπ​π,\displaystyle\quad+\frac{\lambda\_{\mathrm{cl}}}{2}\,\|u\_{I}-u\_{I}^{0}\|\_{2}^{2}+\frac{\lambda\_{\mathrm{surf}}}{2}\,\rho\_{\Omega}(u\_{I})^{\top}H\_{\rho}\,\rho\_{\Omega}(u\_{I})+\frac{\lambda\_{\pi}}{2}\,\pi^{\top}H\_{\pi}\,\pi, |  |

where u=u​(uI)u=u(u\_{I}), dq​(u)d\_{q}(u) is the band violation at quote qq
(Definition [32](https://arxiv.org/html/2512.01967v1#Thmdefinition32 "Definition 32 (Band misfit at a quote). ‣ 12.6.2 Band misfit and noise-aware penalty ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) and Mq​(π)M\_{q}(\pi) is the fog mass outside the band at
quote qq (Definition [31](https://arxiv.org/html/2512.01967v1#Thmdefinition31 "Definition 31 (Local fog mass outside the band at a quote). ‣ 12.6.1 Fog mass outside the band at a quote ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")).

###### Remark 25 (Well-definedness and continuity of JΩJ\_{\Omega}).

Since π∈𝒞π​(Ω)\pi\in\mathcal{C}\_{\pi}(\Omega) implies Mq​(π)≥0M\_{q}(\pi)\geq 0 and ε>0\varepsilon>0
by construction, the denominators ε+Mq​(π)\varepsilon+M\_{q}(\pi) are bounded away from
zero and all terms in ([12.3](https://arxiv.org/html/2512.01967v1#Ch12.E3 "Equation 12.3 ‣ Definition 42 (Patch energy functional). ‣ 12.8.2 Patch energy functional ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) are finite. Each component
ϕq​(uI,π)\phi\_{q}(u\_{I},\pi), Ecl​(uI)E\_{\mathrm{cl}}(u\_{I}), Esurf​(uI)E\_{\mathrm{surf}}(u\_{I}), and
ℰHam​(π)\mathcal{E}\_{\mathrm{Ham}}(\pi) is continuous in its arguments. Therefore
JΩJ\_{\Omega} is a continuous real-valued function on
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega).

We now establish the basic convexity property of JΩJ\_{\Omega}.

###### Proposition 19 (Convexity of the patch energy).

For any feasible patch Ω\Omega (i.e. 𝒞u​(Ω)≠∅\mathcal{C}\_{u}(\Omega)\neq\emptyset), the
patch energy functional JΩJ\_{\Omega} is jointly convex in (uI,π)(u\_{I},\pi) on
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega).

###### Proof.

By Proposition [16](https://arxiv.org/html/2512.01967v1#Thmprop16 "Proposition 16 (Convexity of the noise-aware band term). ‣ 12.6.3 Convexity of the noise-aware band term ‣ 12.6 Noise-aware band term via the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), each individual noise-aware band term
ϕq​(uI,π)\phi\_{q}(u\_{I},\pi) is jointly convex in (uI,π)(u\_{I},\pi) on
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega). By
Proposition [17](https://arxiv.org/html/2512.01967v1#Thmprop17 "Proposition 17 (Quadratic form and convexity of 𝐸_surf). ‣ 12.7.2 Surface density energy ‣ 12.7 Surface energy and closeness to the baseline ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), Esurf​(uI)E\_{\mathrm{surf}}(u\_{I}) is a convex
quadratic functional of uIu\_{I}. By Proposition [18](https://arxiv.org/html/2512.01967v1#Thmprop18 "Proposition 18 (Strict convexity of 𝐸_cl). ‣ 12.7.3 Closeness to the baseline ‣ 12.7 Surface energy and closeness to the baseline ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"),
Ecl​(uI)E\_{\mathrm{cl}}(u\_{I}) is a strictly convex quadratic functional of uIu\_{I}
(hence convex). By Proposition [15](https://arxiv.org/html/2512.01967v1#Thmprop15 "Proposition 15 (Symmetry, positive semidefiniteness, and convexity). ‣ 12.5.4 Hamiltonian energy and basic properties ‣ 12.5 Hamiltonian energy on the fog ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), ℰHam​(π)\mathcal{E}\_{\mathrm{Ham}}(\pi)
is a convex quadratic functional of π\pi.

Multiplying convex functionals by nonnegative scalars preserves convexity, and
summing finitely many convex functionals yields a convex functional. Therefore,
for each (uI,π)(u\_{I},\pi) in the convex set
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega), the map

|  |  |  |
| --- | --- | --- |
|  | (uI,π)↦JΩ​(uI,π)(u\_{I},\pi)\mapsto J\_{\Omega}(u\_{I},\pi) |  |

is convex. This proves the claim.
∎

#### 12.8.3 Patch-level post-fit problem: existence and uniqueness

We can now formulate the patch-level convex optimisation problem.

###### Definition 43 (Patch-level post-fit problem).

Let Ω⊂𝒢\Omega\subset\mathcal{G} be a feasible patch (i.e. 𝒞u​(Ω)≠∅\mathcal{C}\_{u}(\Omega)\neq\emptyset). The *patch-level post-fit problem*
is the constrained optimisation problem

|  |  |  |
| --- | --- | --- |
|  | min⁡{JΩ​(uI,π):uI∈𝒞u​(Ω),π∈𝒞π​(Ω)}.\min\bigl\{J\_{\Omega}(u\_{I},\pi):u\_{I}\in\mathcal{C}\_{u}(\Omega),\ \pi\in\mathcal{C}\_{\pi}(\Omega)\bigr\}. |  |

Any pair (uI⋆,π⋆)∈𝒞u​(Ω)×𝒞π​(Ω)(u\_{I}^{\star},\pi^{\star})\in\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega)
achieving this minimum is called a *patch minimiser*.

We now show that at least one minimiser exists under our standing assumptions.

###### Proposition 20 (Existence of patch-level minimisers).

Assume that 𝒞u​(Ω)≠∅\mathcal{C}\_{u}(\Omega)\neq\emptyset and that λcl>0\lambda\_{\mathrm{cl}}>0
(as in Definition [39](https://arxiv.org/html/2512.01967v1#Thmdefinition39 "Definition 39 (Closeness to the baseline). ‣ 12.7.3 Closeness to the baseline ‣ 12.7 Surface energy and closeness to the baseline ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). Then the patch problem admits at least one
minimiser (uI⋆,π⋆)(u\_{I}^{\star},\pi^{\star}).

###### Proof.

The feasible set

|  |  |  |
| --- | --- | --- |
|  | ℱΩ:=𝒞u​(Ω)×𝒞π​(Ω)⊂ℝNΩ×ℝNΩ​nu\mathcal{F}\_{\Omega}:=\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega)\subset\mathbb{R}^{N\_{\Omega}}\times\mathbb{R}^{N\_{\Omega}n\_{u}} |  |

is nonempty by assumption on 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega) and Lemma [11](https://arxiv.org/html/2512.01967v1#Thmlemma11 "Lemma 11 (Geometry of 𝒞_𝜋⁢(Ω)). ‣ 12.8.1 Fog feasible set and quote index set ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit").
By Proposition [13](https://arxiv.org/html/2512.01967v1#Thmprop13 "Proposition 13 (Polyhedral structure of 𝒞_𝑢⁢(Ω)). ‣ 12.4.3 Patch-level feasible set and its geometry ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega) is a closed
convex polyhedron in ℝNΩ\mathbb{R}^{N\_{\Omega}} and may be unbounded. By
Lemma [11](https://arxiv.org/html/2512.01967v1#Thmlemma11 "Lemma 11 (Geometry of 𝒞_𝜋⁢(Ω)). ‣ 12.8.1 Fog feasible set and quote index set ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) is a compact convex
polytope in ℝNΩ​nu\mathbb{R}^{N\_{\Omega}n\_{u}}. Hence ℱΩ\mathcal{F}\_{\Omega} is closed,
convex, and nonempty, but not necessarily bounded.

To apply the Weierstrass theorem, we consider sublevel sets of JΩJ\_{\Omega}.
From ([12.3](https://arxiv.org/html/2512.01967v1#Ch12.E3 "Equation 12.3 ‣ Definition 42 (Patch energy functional). ‣ 12.8.2 Patch energy functional ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), using Ecl​(uI)=λcl2​‖uI−uI0‖22E\_{\mathrm{cl}}(u\_{I})=\frac{\lambda\_{\mathrm{cl}}}{2}\|u\_{I}-u\_{I}^{0}\|\_{2}^{2} and nonnegativity of all other terms, we have

|  |  |  |
| --- | --- | --- |
|  | JΩ​(uI,π)≥Ecl​(uI)=λcl2​‖uI−uI0‖22.J\_{\Omega}(u\_{I},\pi)\;\geq\;E\_{\mathrm{cl}}(u\_{I})=\frac{\lambda\_{\mathrm{cl}}}{2}\,\|u\_{I}-u\_{I}^{0}\|\_{2}^{2}. |  |

Let m:=infℱΩJΩm:=\inf\_{\mathcal{F}\_{\Omega}}J\_{\Omega} denote the infimum of JΩJ\_{\Omega}
on the feasible set, which is finite because JΩ≥0J\_{\Omega}\geq 0 and the baseline
pair (uI0,πref)(u\_{I}^{0},\pi^{\text{ref}}) (with any fixed πref∈𝒞π​(Ω)\pi^{\text{ref}}\in\mathcal{C}\_{\pi}(\Omega))
belongs to ℱΩ\mathcal{F}\_{\Omega}. For any α>m\alpha>m, consider the sublevel set

|  |  |  |
| --- | --- | --- |
|  | ℱΩ​(α):={(uI,π)∈ℱΩ:JΩ​(uI,π)≤α}.\mathcal{F}\_{\Omega}(\alpha):=\bigl\{(u\_{I},\pi)\in\mathcal{F}\_{\Omega}:J\_{\Omega}(u\_{I},\pi)\leq\alpha\bigr\}. |  |

By the inequality above,

|  |  |  |
| --- | --- | --- |
|  | λcl2​‖uI−uI0‖22≤JΩ​(uI,π)≤α⟹‖uI−uI0‖22≤2​αλcl.\frac{\lambda\_{\mathrm{cl}}}{2}\,\|u\_{I}-u\_{I}^{0}\|\_{2}^{2}\leq J\_{\Omega}(u\_{I},\pi)\leq\alpha\quad\Longrightarrow\quad\|u\_{I}-u\_{I}^{0}\|\_{2}^{2}\leq\frac{2\alpha}{\lambda\_{\mathrm{cl}}}. |  |

Thus, for any (uI,π)∈ℱΩ​(α)(u\_{I},\pi)\in\mathcal{F}\_{\Omega}(\alpha), the interior vector
uIu\_{I} lies in the closed Euclidean ball of radius
2​α/λcl\sqrt{2\alpha/\lambda\_{\mathrm{cl}}} centred at uI0u\_{I}^{0}. The fog variable
π\pi always lies in the compact set 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega) by definition
of ℱΩ\mathcal{F}\_{\Omega}. It follows that ℱΩ​(α)\mathcal{F}\_{\Omega}(\alpha) is
bounded.

Moreover, ℱΩ​(α)\mathcal{F}\_{\Omega}(\alpha) is closed: it is the intersection of the
closed set ℱΩ\mathcal{F}\_{\Omega} with the closed inverse image
{(uI,π):JΩ​(uI,π)≤α}\{(u\_{I},\pi):J\_{\Omega}(u\_{I},\pi)\leq\alpha\} of (−∞,α](-\infty,\alpha] under the
continuous map (uI,π)↦JΩ​(uI,π)(u\_{I},\pi)\mapsto J\_{\Omega}(u\_{I},\pi). Hence
ℱΩ​(α)\mathcal{F}\_{\Omega}(\alpha) is compact.

By construction mm is the infimum of JΩJ\_{\Omega} over ℱΩ\mathcal{F}\_{\Omega}, so
there exists a sequence (uI(n),π(n))(u\_{I}^{(n)},\pi^{(n)}) in ℱΩ\mathcal{F}\_{\Omega} such
that JΩ​(uI(n),π(n))↓mJ\_{\Omega}(u\_{I}^{(n)},\pi^{(n)})\downarrow m as n→∞n\to\infty. All but
finitely many of these points lie in ℱΩ​(α)\mathcal{F}\_{\Omega}(\alpha) for any
fixed α>m\alpha>m. By compactness of ℱΩ​(α)\mathcal{F}\_{\Omega}(\alpha), the sequence
has a convergent subsequence (uI(nk),π(nk))(u\_{I}^{(n\_{k})},\pi^{(n\_{k})}) with limit
(uI⋆,π⋆)∈ℱΩ​(α)⊂ℱΩ(u\_{I}^{\star},\pi^{\star})\in\mathcal{F}\_{\Omega}(\alpha)\subset\mathcal{F}\_{\Omega}.
Continuity of JΩJ\_{\Omega} implies

|  |  |  |
| --- | --- | --- |
|  | JΩ​(uI⋆,π⋆)=limk→∞JΩ​(uI(nk),π(nk))=m.J\_{\Omega}(u\_{I}^{\star},\pi^{\star})=\lim\_{k\to\infty}J\_{\Omega}(u\_{I}^{(n\_{k})},\pi^{(n\_{k})})=m. |  |

Thus (uI⋆,π⋆)(u\_{I}^{\star},\pi^{\star}) attains the infimum and is a minimiser of
JΩJ\_{\Omega} on ℱΩ\mathcal{F}\_{\Omega}.
∎

We now provide sufficient conditions for uniqueness of the patch minimiser.

###### Proposition 21 (Uniqueness under strict convexity).

Suppose, in addition to the assumptions of Proposition [20](https://arxiv.org/html/2512.01967v1#Thmprop20 "Proposition 20 (Existence of patch-level minimisers). ‣ 12.8.3 Patch-level post-fit problem: existence and uniqueness ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), that:

1. 1.

   The quadratic form in uIu\_{I} given by

   |  |  |  |
   | --- | --- | --- |
   |  | uI↦Ecl​(uI)+λsurf​Esurf​(uI)u\_{I}\mapsto E\_{\mathrm{cl}}(u\_{I})+\lambda\_{\mathrm{surf}}E\_{\mathrm{surf}}(u\_{I}) |  |

   is strictly convex on the affine hull of 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega); equivalently,
   its Hessian λcl​INΩ+λsurf​QΩ\lambda\_{\mathrm{cl}}I\_{N\_{\Omega}}+\lambda\_{\mathrm{surf}}Q\_{\Omega}
   is positive definite on the tangent cone of 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega).
2. 2.

   λπ>0\lambda\_{\pi}>0 and the Hamiltonian matrix HπH\_{\pi} is positive definite
   on the affine hull of 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega); equivalently, the quadratic
   form π↦π⊤​Hπ​π\pi\mapsto\pi^{\top}H\_{\pi}\pi is strictly convex on 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega).

Then the minimiser (uI⋆,π⋆)(u\_{I}^{\star},\pi^{\star}) of JΩJ\_{\Omega} on
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega) is unique.

###### Proof.

By assumption (1), the map

|  |  |  |
| --- | --- | --- |
|  | uI↦Ecl​(uI)+λsurf​Esurf​(uI)u\_{I}\mapsto E\_{\mathrm{cl}}(u\_{I})+\lambda\_{\mathrm{surf}}E\_{\mathrm{surf}}(u\_{I}) |  |

is strictly convex on 𝒞u​(Ω)\mathcal{C}\_{u}(\Omega). By assumption (2), the map

|  |  |  |
| --- | --- | --- |
|  | π↦λπ​ℰHam​(π)=λπ2​π⊤​Hπ​π\pi\mapsto\lambda\_{\pi}\,\mathcal{E}\_{\mathrm{Ham}}(\pi)=\frac{\lambda\_{\pi}}{2}\,\pi^{\top}H\_{\pi}\pi |  |

is strictly convex on 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega). The remaining contribution to
JΩJ\_{\Omega} is the sum of noise-aware band terms

|  |  |  |
| --- | --- | --- |
|  | (uI,π)↦∑q∈QΩϕq​(uI,π),(u\_{I},\pi)\mapsto\sum\_{q\in Q\_{\Omega}}\phi\_{q}(u\_{I},\pi), |  |

which is convex by Proposition [19](https://arxiv.org/html/2512.01967v1#Thmprop19 "Proposition 19 (Convexity of the patch energy). ‣ 12.8.2 Patch energy functional ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") (and does not affect
strict convexity, since adding a convex function to a strictly convex one
preserves strict convexity).

To see that JΩJ\_{\Omega} is strictly convex on the product set
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega), let
(uI(1),π(1))(u\_{I}^{(1)},\pi^{(1)}) and (uI(2),π(2))(u\_{I}^{(2)},\pi^{(2)}) be two distinct feasible
points, and let θ∈(0,1)\theta\in(0,1). Then at least one of the components uI(1)u\_{I}^{(1)}
and uI(2)u\_{I}^{(2)} differs, or π(1)\pi^{(1)} and π(2)\pi^{(2)} differ. If
uI(1)≠uI(2)u\_{I}^{(1)}\neq u\_{I}^{(2)}, strict convexity of the uIu\_{I}-quadratic implies

|  |  |  |
| --- | --- | --- |
|  | Ecl​(θ​uI(1)+(1−θ)​uI(2))+λsurf​Esurf​(θ​uI(1)+(1−θ)​uI(2))E\_{\mathrm{cl}}(\theta u\_{I}^{(1)}+(1-\theta)u\_{I}^{(2)})+\lambda\_{\mathrm{surf}}E\_{\mathrm{surf}}(\theta u\_{I}^{(1)}+(1-\theta)u\_{I}^{(2)}) |  |

|  |  |  |
| --- | --- | --- |
|  | <θ​(Ecl​(uI(1))+λsurf​Esurf​(uI(1)))+(1−θ)​(Ecl​(uI(2))+λsurf​Esurf​(uI(2))).<\theta\bigl(E\_{\mathrm{cl}}(u\_{I}^{(1)})+\lambda\_{\mathrm{surf}}E\_{\mathrm{surf}}(u\_{I}^{(1)})\bigr)+(1-\theta)\bigl(E\_{\mathrm{cl}}(u\_{I}^{(2)})+\lambda\_{\mathrm{surf}}E\_{\mathrm{surf}}(u\_{I}^{(2)})\bigr). |  |

If instead uI(1)=uI(2)u\_{I}^{(1)}=u\_{I}^{(2)} but π(1)≠π(2)\pi^{(1)}\neq\pi^{(2)}, strict
convexity of λπ​ℰHam\lambda\_{\pi}\mathcal{E}\_{\mathrm{Ham}} on 𝒞π​(Ω)\mathcal{C}\_{\pi}(\Omega)
implies a strict inequality in the π\pi-component. In either case, adding the
convex sum of band terms preserves strict inequality:

|  |  |  |
| --- | --- | --- |
|  | JΩ​(θ​uI(1)+(1−θ)​uI(2),θ​π(1)+(1−θ)​π(2))J\_{\Omega}\bigl(\theta u\_{I}^{(1)}+(1-\theta)u\_{I}^{(2)},\ \theta\pi^{(1)}+(1-\theta)\pi^{(2)}\bigr) |  |

|  |  |  |
| --- | --- | --- |
|  | <θ​JΩ​(uI(1),π(1))+(1−θ)​JΩ​(uI(2),π(2)).<\theta J\_{\Omega}(u\_{I}^{(1)},\pi^{(1)})+(1-\theta)J\_{\Omega}(u\_{I}^{(2)},\pi^{(2)}). |  |

Thus JΩJ\_{\Omega} is strictly convex on the convex feasible set
𝒞u​(Ω)×𝒞π​(Ω)\mathcal{C}\_{u}(\Omega)\times\mathcal{C}\_{\pi}(\Omega). A strictly convex function
on a convex set has at most one minimiser. Combined with existence
(Proposition [20](https://arxiv.org/html/2512.01967v1#Thmprop20 "Proposition 20 (Existence of patch-level minimisers). ‣ 12.8.3 Patch-level post-fit problem: existence and uniqueness ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), this implies that the minimiser of JΩJ\_{\Omega}
is unique.
∎

###### Remark 26 (Non-quadratic but convex structure).

The patch energy JΩJ\_{\Omega} is convex but not quadratic in the joint variables
(uI,π)(u\_{I},\pi). The non-quadratic structure arises from the perspective-type terms
dq​(u)2/(ε+Mq​(π))d\_{q}(u)^{2}/(\varepsilon+M\_{q}(\pi)) in the noise-aware band penalties ϕq\phi\_{q},
which couple the surface misfit and the fog mass in a nonlinear way. Introducing
additional slack variables to eliminate the perspective structure would break
the natural probabilistic interpretation of π\pi and νq​(π)\nu\_{q}(\pi), and is not
pursued here. Consequently, the patch-level post-fit is formulated and solved
as a general convex optimisation problem, rather than as a quadratic program.

### 12.9  Global post-fit across patches and dates

We now describe how the patch-level post-fit is assembled into a global
arbitrage-free surface on each date, and state conditions under which global
static no-arbitrage is preserved.

Throughout this section we fix a calendar date tt and suppress explicit tt-dependence
in the notation when no ambiguity arises. All objects (quotes, bands, forwards,
baseline u0u^{0}, operators ℓα,rα\ell\_{\alpha},r\_{\alpha}, etc.) are understood to be
associated with this fixed date.

#### 12.9.1 Patch decomposition and compatibility with no-arbitrage stencils

Recall that the global discrete static no-arbitrage constraints on the nodal
grid 𝒢\mathcal{G} are encoded by the index set ℐ\mathcal{I} and linear
inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓα⊤​u≤rα,α∈ℐ,\ell\_{\alpha}^{\top}u\leq r\_{\alpha},\qquad\alpha\in\mathcal{I}, |  | (12.4) |

as in Definition [19](https://arxiv.org/html/2512.01967v1#Thmdefinition19 "Definition 19 (Global no-arbitrage operators). ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") and
equation ([12.2](https://arxiv.org/html/2512.01967v1#Ch12.E2 "Equation 12.2 ‣ 12.4.2 Global discrete static no-arbitrage on the grid ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")). For each α∈ℐ\alpha\in\mathcal{I}, the *support*
of the stencil is

|  |  |  |
| --- | --- | --- |
|  | supp​(ℓα):={g∈{1,…,G}:(ℓα)g≠0}.\mathrm{supp}(\ell\_{\alpha}):=\bigl\{g\in\{1,\dots,G\}:(\ell\_{\alpha})\_{g}\neq 0\bigr\}. |  |

Equivalently, supp​(ℓα)\mathrm{supp}(\ell\_{\alpha}) is the set of nodal indices at which
uu enters the α\alpha-th constraint with nonzero coefficient.

Let {Ωp}p∈𝒫\{\Omega\_{p}\}\_{p\in\mathcal{P}} be a finite family of pairwise disjoint
patches in 𝒢\mathcal{G}, i.e.

|  |  |  |
| --- | --- | --- |
|  | Ωp⊂𝒢,Ωp∩Ωp′=∅​for ​p≠p′.\Omega\_{p}\subset\mathcal{G},\quad\Omega\_{p}\cap\Omega\_{p^{\prime}}=\emptyset\ \text{for }p\neq p^{\prime}. |  |

Define their union and complement by

|  |  |  |
| --- | --- | --- |
|  | Ωall:=⋃p∈𝒫Ωp,Ωoff:=𝒢∖Ωall.\Omega\_{\mathrm{all}}:=\bigcup\_{p\in\mathcal{P}}\Omega\_{p},\qquad\Omega\_{\mathrm{off}}:=\mathcal{G}\setminus\Omega\_{\mathrm{all}}. |  |

We explicitly assume that the patch decomposition is compatible with the global
no-arbitrage stencils in the following sense.

###### Assumption 3 (Stencil compatibility of the patch decomposition).

For every α∈ℐ\alpha\in\mathcal{I}, the support of ℓα\ell\_{\alpha} is either
contained entirely in one patch or entirely outside all patches; that is, for
each α∈ℐ\alpha\in\mathcal{I} there exists either:

* •

  a patch index p∈𝒫p\in\mathcal{P} such that
  supp​(ℓα)⊂Ωp\mathrm{supp}(\ell\_{\alpha})\subset\Omega\_{p}, or
* •

  no patch index with this property, in which case
  supp​(ℓα)⊂Ωoff\mathrm{supp}(\ell\_{\alpha})\subset\Omega\_{\mathrm{off}}.

Equivalently, there is no α∈ℐ\alpha\in\mathcal{I} such that
supp​(ℓα)\mathrm{supp}(\ell\_{\alpha}) intersects both Ωp\Omega\_{p} and
𝒢∖Ωp\mathcal{G}\setminus\Omega\_{p} for some pp.

In words, no-arbitrage stencils do not “straddle” patch boundaries: each
discrete bound, monotonicity, convexity, or calendar constraint is supported
either entirely on a single patch, or entirely outside the union of patches.
This is a slightly stronger version of the patch feasibility condition discussed
after Definition [22](https://arxiv.org/html/2512.01967v1#Thmdefinition22 "Definition 22 (Patch feasibility). ‣ 12.4.3 Patch-level feasible set and its geometry ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), and is natural in view of the local
construction of patches from the badness field.

#### 12.9.2 Global post-fit surface on a fixed date

For a fixed date tt, the patch-level post-fit yields, for each patch
Ωp\Omega\_{p}, a pair (uI,p⋆,πp⋆)(u\_{I,p}^{\star},\pi\_{p}^{\star}) solving the patch problem
(Definition [43](https://arxiv.org/html/2512.01967v1#Thmdefinition43 "Definition 43 (Patch-level post-fit problem). ‣ 12.8.3 Patch-level post-fit problem: existence and uniqueness ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) on that patch, i.e.

|  |  |  |
| --- | --- | --- |
|  | (uI,p⋆,πp⋆)∈arg⁡min⁡{JΩp​(uI,π):uI∈𝒞u​(Ωp),π∈𝒞π​(Ωp)}.(u\_{I,p}^{\star},\pi\_{p}^{\star})\in\arg\min\bigl\{J\_{\Omega\_{p}}(u\_{I},\pi):u\_{I}\in\mathcal{C}\_{u}(\Omega\_{p}),\ \pi\in\mathcal{C}\_{\pi}(\Omega\_{p})\bigr\}. |  |

By construction, uI,p⋆∈𝒞u​(Ωp)u\_{I,p}^{\star}\in\mathcal{C}\_{u}(\Omega\_{p}), so the assembled
surface u(p):=u​(uI,p⋆)u^{(p)}:=u(u\_{I,p}^{\star}) (defined as in
Section [12.4](https://arxiv.org/html/2512.01967v1#Ch12.S4 "12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) satisfies all global no-arbitrage inequalities
([12.4](https://arxiv.org/html/2512.01967v1#Ch12.E4 "Equation 12.4 ‣ 12.9.1 Patch decomposition and compatibility with no-arbitrage stencils ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) with off-patch nodes fixed to their baseline
values.

We now combine all patch-level interior solutions into a single global nodal
surface u⋆u^{\star} for date tt.

###### Definition 44 (Global post-fit surface on a date).

Let u0∈ℝGu^{0}\in\mathbb{R}^{G} be the baseline nodal surface for date tt, and let
{Ωp}p∈𝒫\{\Omega\_{p}\}\_{p\in\mathcal{P}} be a stencil-compatible patch decomposition
(Assumption [3](https://arxiv.org/html/2512.01967v1#Thmassump3 "Assumption 3 (Stencil compatibility of the patch decomposition). ‣ 12.9.1 Patch decomposition and compatibility with no-arbitrage stencils ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) with corresponding interior
solutions {uI,p⋆}p∈𝒫\{u\_{I,p}^{\star}\}\_{p\in\mathcal{P}}. The *global post-fit
nodal surface* u⋆∈ℝGu^{\star}\in\mathbb{R}^{G} for date tt is defined componentwise
by

|  |  |  |
| --- | --- | --- |
|  | ui,j⋆:={(uI,p⋆)i,j,if ​(i,j)∈Ωp​for some ​p∈𝒫,ui,j0,if ​(i,j)∈Ωoff.u^{\star}\_{i,j}:=\begin{cases}(u\_{I,p}^{\star})\_{i,j},&\text{if }(i,j)\in\Omega\_{p}\ \text{for some }p\in\mathcal{P},\\[3.0pt] u^{0}\_{i,j},&\text{if }(i,j)\in\Omega\_{\mathrm{off}}.\end{cases} |  |

Equivalently, u⋆u^{\star} coincides with the patch-level interior solutions on
each Ωp\Omega\_{p} and with the baseline on all nodes outside the union of
patches.

We emphasise that the fog fields πp⋆\pi\_{p}^{\star} remain patch-local; they are not
assembled into a single global fog, since only u⋆u^{\star} is used in further
pricing and calibration.

#### 12.9.3 Global static no-arbitrage and locality

We now show that under Assumption [3](https://arxiv.org/html/2512.01967v1#Thmassump3 "Assumption 3 (Stencil compatibility of the patch decomposition). ‣ 12.9.1 Patch decomposition and compatibility with no-arbitrage stencils ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), the global
post-fit surface u⋆u^{\star} is statically no-arbitrage on 𝒢\mathcal{G}, and that
nodes outside the patches are unchanged.

###### Proposition 22 (Global static no-arbitrage and locality).

Fix a date tt and suppose:

1. (i)

   the patch decomposition {Ωp}p∈𝒫\{\Omega\_{p}\}\_{p\in\mathcal{P}} satisfies
   Assumption [3](https://arxiv.org/html/2512.01967v1#Thmassump3 "Assumption 3 (Stencil compatibility of the patch decomposition). ‣ 12.9.1 Patch decomposition and compatibility with no-arbitrage stencils ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit");
2. (ii)

   each patch Ωp\Omega\_{p} is feasible in the sense of
   Definition [22](https://arxiv.org/html/2512.01967v1#Thmdefinition22 "Definition 22 (Patch feasibility). ‣ 12.4.3 Patch-level feasible set and its geometry ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") and admits a patch-level solution
   (uI,p⋆,πp⋆)(u\_{I,p}^{\star},\pi\_{p}^{\star}) as in Definition [43](https://arxiv.org/html/2512.01967v1#Thmdefinition43 "Definition 43 (Patch-level post-fit problem). ‣ 12.8.3 Patch-level post-fit problem: existence and uniqueness ‣ 12.8 Patch-level post-fit optimisation problem ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit");
3. (iii)

   the baseline nodal surface u0u^{0} is globally statically
   no-arbitrage, i.e. u0∈𝒞globu^{0}\in\mathcal{C}\_{\mathrm{glob}}.

Let u⋆u^{\star} be the global post-fit surface defined in
Definition [44](https://arxiv.org/html/2512.01967v1#Thmdefinition44 "Definition 44 (Global post-fit surface on a date). ‣ 12.9.2 Global post-fit surface on a fixed date ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"). Then:

1. 1.

   u⋆u^{\star} is statically no-arbitrage on 𝒢\mathcal{G}, i.e. u⋆∈𝒞globu^{\star}\in\mathcal{C}\_{\mathrm{glob}}; and
2. 2.

   locality holds: ui,j⋆=ui,j0u^{\star}\_{i,j}=u^{0}\_{i,j} for all
   (i,j)∈Ωoff(i,j)\in\Omega\_{\mathrm{off}}.

###### Proof.

Part (b) (locality) is immediate from the definition of u⋆u^{\star}: by
Definition [44](https://arxiv.org/html/2512.01967v1#Thmdefinition44 "Definition 44 (Global post-fit surface on a date). ‣ 12.9.2 Global post-fit surface on a fixed date ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"), for (i,j)∈Ωoff(i,j)\in\Omega\_{\mathrm{off}} we set
ui,j⋆:=ui,j0u^{\star}\_{i,j}:=u^{0}\_{i,j}. Hence u⋆u^{\star} agrees with the baseline on all
off-patch nodes.

We now prove (a). It suffices to show that all global no-arbitrage inequalities
([12.4](https://arxiv.org/html/2512.01967v1#Ch12.E4 "Equation 12.4 ‣ 12.9.1 Patch decomposition and compatibility with no-arbitrage stencils ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")) hold for u⋆u^{\star}; that is, we must verify

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​u⋆≤rα,∀α∈ℐ.\ell\_{\alpha}^{\top}u^{\star}\leq r\_{\alpha},\qquad\forall\alpha\in\mathcal{I}. |  |

Fix α∈ℐ\alpha\in\mathcal{I} and consider the support
supp​(ℓα)\mathrm{supp}(\ell\_{\alpha}). By Assumption [3](https://arxiv.org/html/2512.01967v1#Thmassump3 "Assumption 3 (Stencil compatibility of the patch decomposition). ‣ 12.9.1 Patch decomposition and compatibility with no-arbitrage stencils ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit"),
there are two mutually exclusive cases:

*Case 1:* supp​(ℓα)⊂Ωoff\mathrm{supp}(\ell\_{\alpha})\subset\Omega\_{\mathrm{off}}.

In this case, the α\alpha-th inequality involves only off-patch nodes. On
Ωoff\Omega\_{\mathrm{off}}, we have ui,j⋆=ui,j0u^{\star}\_{i,j}=u^{0}\_{i,j}, so the α\alpha-th
constraint evaluated at u⋆u^{\star} is identical to that evaluated at u0u^{0}:

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​u⋆=ℓα⊤​u0.\ell\_{\alpha}^{\top}u^{\star}=\ell\_{\alpha}^{\top}u^{0}. |  |

By assumption (iii), u0∈𝒞globu^{0}\in\mathcal{C}\_{\mathrm{glob}}, so
ℓα⊤​u0≤rα\ell\_{\alpha}^{\top}u^{0}\leq r\_{\alpha}. Hence
ℓα⊤​u⋆≤rα\ell\_{\alpha}^{\top}u^{\star}\leq r\_{\alpha} in Case 1.

*Case 2:* There exists p∈𝒫p\in\mathcal{P} such that
supp​(ℓα)⊂Ωp\mathrm{supp}(\ell\_{\alpha})\subset\Omega\_{p}.

In this case, the α\alpha-th constraint involves only nodes inside the single
patch Ωp\Omega\_{p}. Let u(p)u^{(p)} denote the full nodal surface corresponding to
the patch-level interior solution uI,p⋆u\_{I,p}^{\star}, i.e. the assembled surface
obtained by replacing u0u^{0} by uI,p⋆u\_{I,p}^{\star} on Ωp\Omega\_{p} and keeping all
other nodes at their baseline values. By definition of 𝒞u​(Ωp)\mathcal{C}\_{u}(\Omega\_{p})
(Definition [21](https://arxiv.org/html/2512.01967v1#Thmdefinition21 "Definition 21 (No-arbitrage feasible set on a patch). ‣ 12.4.3 Patch-level feasible set and its geometry ‣ 12.4 Patch-level price field and static no-arbitrage ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit")), we have uI,p⋆∈𝒞u​(Ωp)u\_{I,p}^{\star}\in\mathcal{C}\_{u}(\Omega\_{p}),
hence

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​u(p)≤rα,∀α∈ℐ.\ell\_{\alpha}^{\top}u^{(p)}\leq r\_{\alpha},\qquad\forall\alpha\in\mathcal{I}. |  |

In particular, for the specific index α\alpha under consideration,

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​u(p)≤rα.\ell\_{\alpha}^{\top}u^{(p)}\leq r\_{\alpha}. |  |

We now compare u(p)u^{(p)} and u⋆u^{\star} on the support of ℓα\ell\_{\alpha}. On
Ωp\Omega\_{p}, both u(p)u^{(p)} and u⋆u^{\star} take the same nodal values, namely
(uI,p⋆)i,j(u\_{I,p}^{\star})\_{i,j}; on 𝒢∖Ωp\mathcal{G}\setminus\Omega\_{p}, the α\alpha-th
constraint has zero coefficients (since
supp​(ℓα)⊂Ωp\mathrm{supp}(\ell\_{\alpha})\subset\Omega\_{p}). Therefore

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​u⋆=ℓα⊤​u(p).\ell\_{\alpha}^{\top}u^{\star}=\ell\_{\alpha}^{\top}u^{(p)}. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | ℓα⊤​u⋆=ℓα⊤​u(p)≤rα.\ell\_{\alpha}^{\top}u^{\star}=\ell\_{\alpha}^{\top}u^{(p)}\leq r\_{\alpha}. |  |

In both cases we have shown ℓα⊤​u⋆≤rα\ell\_{\alpha}^{\top}u^{\star}\leq r\_{\alpha}. Since
α∈ℐ\alpha\in\mathcal{I} was arbitrary, it follows that
ℓα⊤​u⋆≤rα\ell\_{\alpha}^{\top}u^{\star}\leq r\_{\alpha} for all α∈ℐ\alpha\in\mathcal{I}, i.e.
u⋆∈𝒞globu^{\star}\in\mathcal{C}\_{\mathrm{glob}}. This proves (a).
∎

###### Remark 27 (Independence across dates).

The above argument is purely cross-sectional and is applied separately on each
date tt. There is no coupling in the static no-arbitrage constraints between
different dates, so the global post-fit surfaces {ut⋆}t\{u\_{t}^{\star}\}\_{t} across all
dates are obtained by applying the per-date patch decomposition and assembly
independently. Provided that the assumptions of
Proposition [22](https://arxiv.org/html/2512.01967v1#Thmprop22 "Proposition 22 (Global static no-arbitrage and locality). ‣ 12.9.3 Global static no-arbitrage and locality ‣ 12.9 Global post-fit across patches and dates ‣ 12. Hamiltonian Fog Post-Fit in Price Space ‣ Arbitrage-Free Option Price Surfaces via Chebyshev Tensor Bases and a Hamiltonian Fog Post-Fit") hold for each date, the family
{ut⋆}t\{u\_{t}^{\star}\}\_{t} is statically no-arbitrage on every date, and coincides with
the baseline surfaces outside the union of patches on each date.

## 13.  Conclusion and outlook

We have presented a convex-programming framework for constructing arbitrage-free
option price surfaces based on a global Chebyshev representation on a warped
log-moneyness domain. By encoding static no-arbitrage inequalities as
linear constraints on a dense collocation grid, and fitting directly to prices via
a coverage-seeking quadratic objective, the method yields a surface that is
both smooth and internally consistent.

On the empirical side, our implementation attains high inside-spread coverage and
low rates of static no-arbitrage violations across a multi-year panel of equity
options. These results suggest that Chebyshev/QP formulations, combined with spectral-geometry
and transport-type regularisers, are a viable and competitive alternative to more
widely used parametric and spline-based approaches, particularly when tight control
over arbitrage metrics is required.

Beyond the global QP backbone, we have formulated a local post-fit layer in which
a discrete fog of risk-neutral densities on (m,τ,u)(m,\tau,u) is endowed with a
Hamiltonian-type energy. On each problematic patch of the (m,τ)(m,\tau)-plane, this
fog is coupled convexly to a nodal price field that remains globally
arbitrage-free. The resulting patch problems are jointly convex in the surface
and fog variables and yield noise-aware corrections that improve local band
coverage in stressed regions while preserving static no-arbitrage and locality.

Several limitations and directions for further work remain. First, our study
focuses on a particular choice of warping, regularisation and grid design; different
markets or underlyings may benefit from alternative configurations, and a more
systematic comparison against SVI-type and deep-learning-based surfaces would be
informative. This will be tackled in a separate paper. Second, we have evaluated performance primarily through static
diagnostics (spread coverage, violation rates, smoothness) and local band metrics
on patches. A natural next step is to examine the impact on hedging performance
and risk measures, for example via delta-hedging backtests or scenario analysis of
risk-neutral densities, both for the baseline QP and for the fog-corrected surface.

Finally, the Hamiltonian fog layer is implemented here in a finite-dimensional,
patch-wise discretisation. From a mathematical standpoint, it suggests a continuous
framework in which a fog density π​(m,τ,u)\pi(m,\tau,u) on a three-dimensional manifold
evolves under a Hamiltonian or transport-type metric, with the option surface
appearing as a constrained “sheet” inside this geometry. Developing this
continuous theory-including PDE and variational formulations, existence and
uniqueness questions, and connections to optimal transport on the space of
risk-neutral measures is beyond the scope of the present paper and will be
pursued in separate work. We view the discrete constructions in this article as a practical, convex
realisation of that program: the global Chebyshev/QP fit provides a transparent
arbitrage-free backbone, and the patch-wise Hamiltonian fog post-fit offers a
local, noise-aware refinement that remains compatible with production-style
constraints and solvers.

### Acknowledgments

The author made limited use of an AI language model (ChatGPT by OpenAI) as a writing and brainstorming aid; all models, proofs and numerical results presented are the author’s own work and have been independently verified.