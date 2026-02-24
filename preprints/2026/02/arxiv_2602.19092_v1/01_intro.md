---
authors:
- Neda Bagheri Renani
- Daniel Sevcovic
doc_id: arxiv:2602.19092v1
family_id: arxiv:2602.19092
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing
  Under Stochastic Volatility and Jumps
url_abs: http://arxiv.org/abs/2602.19092v1
url_html: https://arxiv.org/html/2602.19092v1
venue: arXiv q-fin
version: 1
year: 2026
---


Neda Bagheri Renani
  
Daniel Ševčovič
11221122

###### Abstract

We propose a fourth–order compact finite–difference (HOC–FD) scheme
for the transformed Bates partial integro–differential equation (PIDE).
The method employs an implicit–explicit (IMEX) Crank–Nicolson framework
for local terms and Simpson quadrature for the jump integral. Benchmarks
against second–order finite differences (FD) and quadratic finite elements
(FEM, p=2p=2) confirm near–fourth–order spatial accuracy for HOC–FD,
near–second–order for FEM, and second–order temporal convergence for
all time integrators. Efficiency tests show that HOC–FD achieves similar
accuracy at up to two orders of magnitude lower runtime than FEM,
establishing it as a practical baseline for option pricing under stochastic
volatility jump–diffusion models.

###### keywords:

Bates model; option pricing; partial integro–differential equation (PIDE); high order compact finite difference; finite element method

## 1 Introduction

Stochastic volatility models with jumps, such as the Bates model, lead to
partial integro–differential equations (PIDEs) central to option pricing.
Their complexity motivates efficient high–order numerical solvers
[[9](https://arxiv.org/html/2602.19092v1#bib.bib1 "Option pricing in illiquid markets with jumps"), [8](https://arxiv.org/html/2602.19092v1#bib.bib2 "On solutions of a partial integro-differential equation in bessel potential spaces with applications in option pricing models")]. Compact high–order finite difference
schemes have been successfully applied to liquidity shock models
[[13](https://arxiv.org/html/2602.19092v1#bib.bib23 "Fourth-order compact schemes for a parabolic-ordinary system of european option pricing liquidity shocks model")], nonlinear PDEs [[14](https://arxiv.org/html/2602.19092v1#bib.bib24 "A kernel-based algorithm for numerical solution of nonlinear pdes in finance")], fractional
extensions [[10](https://arxiv.org/html/2602.19092v1#bib.bib25 "High order finite difference schemes on non-uniform meshes for the time-fractional black–scholes equation")], and uncertain correlation problems
[[15](https://arxiv.org/html/2602.19092v1#bib.bib26 "A positive flux limited difference scheme for option pricing 2d fully non-linear parabolic equation with uncertain correlation")], confirming their advantages for accuracy and stability.

We develop a fourth–order compact finite–difference (HOC–FD) scheme for the
transformed Bates PIDE, combining an IMEX–Crank–Nicolson split for local terms
with Simpson quadrature for the jump integral. Benchmarks against second–order
finite differences and quadratic FEM demonstrate near fourth–order spatial
accuracy, second–order temporal accuracy, and substantial efficiency gains,
establishing HOC–FD as a competitive baseline for option pricing under
stochastic volatility jump–diffusion models.

## 2 Stochastic Differential Equations of the Bates Model

The Bates model augments the Heston stochastic–volatility framework with a jump component in the asset price, combining continuous variance dynamics with discontinuous returns to better reproduce market skew, fat tails, and smile effects ([[2](https://arxiv.org/html/2602.19092v1#bib.bib12 "A comparison study of adi and lod methods on option pricing models"), [23](https://arxiv.org/html/2602.19092v1#bib.bib15 "Galerkin finite element methods for parabolic problems"), [6](https://arxiv.org/html/2602.19092v1#bib.bib4 "The pricing of options and corporate liabilities")] see also [[9](https://arxiv.org/html/2602.19092v1#bib.bib1 "Option pricing in illiquid markets with jumps")]).

#### Risk–neutral dynamics.

Let S​(t)S(t) denote the price of the asset and v​(t)v(t) the variance. Under the risk–neutral measure with correlation ρ\rho between Brownian drivers,

|  |  |  |
| --- | --- | --- |
|  | d​S​(t)=μ​S​(t)​d​t+v​(t)​S​(t)​d​WS​(t)+S​(t)​d​J​(t),dS(t)=\mu S(t)dt+\sqrt{v(t)}S(t)dW\_{S}(t)+S(t)dJ(t),\\ |  |

|  |  |  |
| --- | --- | --- |
|  | d​v​(t)=κ​(θ−v​(t))​d​t+σ​v​(t)​d​Wv​(t),dv(t)=\kappa(\theta-v(t))dt+\sigma\sqrt{v(t)}dW\_{v}(t), |  |

where κ>0\kappa>0 (mean–reversion speed), θ>0\theta>0 (long–run variance), and σ>0\sigma>0 (volatility of variance). The jump process J​(t)J(t) is Poisson with intensity λ\lambda; logarithmic jump sizes YY are often modeled Gaussian with mean μJ\mu\_{J} and variance σJ2\sigma\_{J}^{2}, yielding multiplicative price jumps S↦S​eYS\mapsto Se^{Y} [[11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [19](https://arxiv.org/html/2602.19092v1#bib.bib6 "Option pricing when underlying stock returns are discontinuous")].

#### Option–pricing PIDE.

For an option value V​(S,v,t)V(S,v,t) with a risk-free rate rr, the price satisfies the partial integro–differential equation:

|  |  |  |
| --- | --- | --- |
|  | ∂V∂t+12​S2​v​∂2V∂S2+ρ​σ​v​S​∂2V∂S​∂v+12​σ2​v​∂2V∂v2+(r−λ)​S​∂V∂S+κ​(θ−v)​∂V∂v\displaystyle\frac{\partial V}{\partial t}+\frac{1}{2}S^{2}v\frac{\partial^{2}V}{\partial S^{2}}+\rho\sigma vS\frac{\partial^{2}V}{\partial S\partial v}+\frac{1}{2}\sigma^{2}v\frac{\partial^{2}V}{\partial v^{2}}+(r-\lambda)S\frac{\partial V}{\partial S}+\kappa(\theta-v)\frac{\partial V}{\partial v} |  |
|  |  |  |
| --- | --- | --- |
|  | −(r+λ)​V=λ​∫ℝ[V​(S​ez,v,t)−V​(S,v,t)−(ez−1)​S​∂V∂S​(S,v,t)]​f​(z)​𝑑z.\displaystyle-(r+\lambda)V=\lambda\int\_{\mathbb{R}}\left[V(Se^{z},v,t)-V(S,v,t)-\left(e^{z}-1\right)S\frac{\partial V}{\partial S}(S,v,t)\right]f(z)\,dz. |  |

where f​(z)f(z) is the density of the log–jump size zz (e.g., Gaussian with mean μJ\mu\_{J} and variance σJ2\sigma\_{J}^{2}).
where f​(z)f(z) denotes the density of the log jump size zz (typically z∼𝒩​(μJ,σJ2)z\sim\mathcal{N}(\mu\_{J},\sigma\_{J}^{2})) [[5](https://arxiv.org/html/2602.19092v1#bib.bib5 "Jumps and stochastic volatility: exchange rate processes implicit in deutsche mark options"), [4](https://arxiv.org/html/2602.19092v1#bib.bib20 "The evaluation of american options in a stochastic volatility model with jumps: an efficient finite element approach")].

### 2.1 Transformed Bates Model PIDE

To obtain a numerically convenient form, we introduce the backward time and normalized variables.

|  |  |  |
| --- | --- | --- |
|  | τ=T−tx=ln⁡SKy=σvu​(x,y,τ)=1K​e(r+λ)​τ​V​(S,v,t).\tau=T-t\qquad x=\ln\frac{S}{K}\qquad y=\frac{\sigma}{v}\qquad u(x,y,\tau)=\frac{1}{K}\,e^{(r+\lambda)\tau}\,V(S,v,t). |  |

Here, KK is the strike, rr the risk–free rate, and the parameter λ>0\lambda>0 measures the intensity of jumps. Let f​(z)f(z) denote the
probability density of the logarithmic jump size [[20](https://arxiv.org/html/2602.19092v1#bib.bib22 "Nonlinear profit maximization with account changing of prices"), [11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models")].
With these variables and using differentiation rules, we have:

|  |  |  |
| --- | --- | --- |
|  | S​∂∂S=∂∂x,v​∂∂v=−y​∂∂y,S2​∂2∂S2=∂2∂x2−∂∂x,v​∂∂v=−y​∂∂y,S\frac{\partial}{\partial S}=\frac{\partial}{\partial x},\ v\frac{\partial}{\partial v}=-y\frac{\partial}{\partial y},\ S^{2}\frac{\partial^{2}}{\partial S^{2}}=\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x},\ v\frac{\partial}{\partial v}=-y\frac{\partial}{\partial y}, |  |

|  |  |  |
| --- | --- | --- |
|  | v​∂2∂v2=y3σ​∂2∂y2+2​y2σ​∂∂y,v​S​∂2∂S​∂v=−y​∂2∂x​∂y,v\frac{\partial^{2}}{\partial v^{2}}=\frac{y^{3}}{\sigma}\frac{\partial^{2}}{\partial y^{2}}+2\frac{y^{2}}{\sigma}\frac{\partial}{\partial y},\ vS\frac{\partial^{2}}{\partial S\partial v}=-y\frac{\partial^{2}}{\partial x\partial y},\ |  |

|  |  |  |
| --- | --- | --- |
|  | ∂V∂t−(r+λ)​V=−K​e−(r+λ)​τ​∂u∂τ,V​(S​ez,v,t)=K​e−(r+λ)​τ​u​(x+z,y,τ).\frac{\partial V}{\partial t}-(r+\lambda)V=-K\,e^{-(r+\lambda)\tau}\,\frac{\partial u}{\partial\tau},\ \ V(Se^{z},v,t)=K\,e^{-(r+\lambda)\tau}u(x+z,y,\tau). |  |

Thus, the transformed PIDE reads as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∂u∂τ+σ2​y​(∂2u∂x2−∂u∂x)−ρ​σ​y​∂2u∂x​∂y+σ2​(y3​∂2u∂y2+2​y2​∂u∂y)\displaystyle-\frac{\partial u}{\partial\tau}+\frac{\sigma}{2y}\left(\frac{\partial^{2}u}{\partial x^{2}}-\frac{\partial u}{\partial x}\right)-\rho\sigma y\frac{\partial^{2}u}{\partial x\partial y}+\frac{\sigma}{2}\left(y^{3}\frac{\partial^{2}u}{\partial y^{2}}+2y^{2}\frac{\partial u}{\partial y}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(r−λ)​∂u∂x−κ​(θ−σy)​y2σ​∂u∂y\displaystyle+(r-\lambda)\frac{\partial u}{\partial x}-\kappa\left(\theta-\frac{\sigma}{y}\right)\frac{y^{2}}{\sigma}\frac{\partial u}{\partial y} |  | (1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​∫ℝ[u​(x+z,y,τ)−u​(x,y,τ)−(ez−1)​∂u∂x​(x,y,τ)]​f​(z)​𝑑z=0.\displaystyle+\lambda\int\_{\mathbb{R}}\left[u(x+z,y,\tau)-u(x,y,\tau)-\left(e^{z}-1\right)\frac{\partial u}{\partial x}(x,y,\tau)\right]f(z)\,dz=0. |  |

## 3 Spatial Discretization and IMEX–Crank–Nicolson

We consider a uniform tensor product grid
{(xi,yj):i=0,…,Nx,j=0,…,Ny}\{(x\_{i},y\_{j}):\ i=0,\dots,N\_{x},\ j=0,\dots,N\_{y}\},
xi=xmin+i​hx,yj=ymin+j​hyx\_{i}=x\_{\min}+i\,h\_{x},\quad y\_{j}=y\_{\min}+j\,h\_{y},
with spatial discretization steps hx,hy>0h\_{x},h\_{y}>0. Let ui,jnu\_{i,j}^{n} denote the approximation to u​(xi,yj,τn)u(x\_{i},y\_{j},\tau\_{n})
at time levels τn=n​k\tau\_{n}=nk, where k=T/Nτk=T/N\_{\tau}. The center difference operators
Dx,Dy,Dx​x,Dy​y,Dx​yD\_{x},D\_{y},D\_{xx},D\_{yy},D\_{xy} will be used for the spatial derivatives (their
concrete stencils are given in Sections [3.1](https://arxiv.org/html/2602.19092v1#S3.SS1 "3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")–[3.2](https://arxiv.org/html/2602.19092v1#S3.SS2 "3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")).
The local (differential) part of ([2.1](https://arxiv.org/html/2602.19092v1#S2.Ex9 "2.1 Transformed Bates Model PIDE ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")) reads as:

|  |  |  |
| --- | --- | --- |
|  | L​[u]=σ2​y​ux​x+σ2​y3​uy​y−ρ​σ​y​ux​y+(r−λ−σ2​y)​ux+(σ​y2+κ​y−κ​θ​y2σ)​uy.L[u]=\frac{\sigma}{2y}\,u\_{xx}+\frac{\sigma}{2}y^{3}\,u\_{yy}-\rho\sigma y\,u\_{xy}+\left(r-\lambda-\frac{\sigma}{2y}\right)u\_{x}+\left(\sigma y^{2}+\kappa y-\kappa\theta\frac{y^{2}}{\sigma}\right)u\_{y}. |  |

Its discrete counterpart at (xi,yj)(x\_{i},y\_{j}) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lh​[u]i,j=σ2​yj​Dx​x​u+σ2​yj3​Dy​y​u\displaystyle L\_{h}[u]\_{i,j}=\frac{\sigma}{2y\_{j}}\,D\_{xx}u+\frac{\sigma}{2}y\_{j}^{3}\,D\_{yy}u | −ρ​σ​yj​Dx​y​u+(r−λ−σ2​yj)​Dx​u\displaystyle-\rho\sigma y\_{j}\,D\_{xy}u+\left(r-\lambda-\frac{\sigma}{2y\_{j}}\right)D\_{x}u |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +(σ​yj2+κ​yj−κ​θ​yj2σ)​Dy​u.\displaystyle+\left(\sigma y\_{j}^{2}+\kappa y\_{j}-\kappa\theta\frac{y\_{j}^{2}}{\sigma}\right)D\_{y}u. |  | |

The nonlocal (jump) term in ([2.1](https://arxiv.org/html/2602.19092v1#S2.Ex9 "2.1 Transformed Bates Model PIDE ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")) is treated explicitly. Its discrete approximation Ih​[u]i,jI\_{h}[u]\_{i,j} is designed to match the integral part in ([2.1](https://arxiv.org/html/2602.19092v1#S2.Ex9 "2.1 Transformed Bates Model PIDE ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")):

|  |  |  |
| --- | --- | --- |
|  | Ih​[u]i,j=λ​∫ℝ(u​(xi+z,yj,τ)−u​(xi,yj,τ)−(ez−1)​ux​(xi,yj,τ))​f​(z)​𝑑z.I\_{h}[u]\_{i,j}=\lambda\int\_{\mathbb{R}}\big(u(x\_{i}+z,y\_{j},\tau)-u(x\_{i},y\_{j},\tau)-(e^{z}-1)\,u\_{x}(x\_{i},y\_{j},\tau)\big)f(z)\,dz. |  |

With these definitions, the semi–discrete system has the form

|  |  |  |
| --- | --- | --- |
|  | d​ud​τ​u=Lh​[u]+Ih​[u].\frac{du}{d\tau}u=L\_{h}[u]+I\_{h}[u]. |  |

For time stepping, we use an IMEX–Crank–Nicolson scheme: the local operator LhL\_{h} is
treated implicitly, and the jump operator IhI\_{h} explicitly. Writing UnU^{n} for the vector
of all grid values at time τn\tau\_{n}, one step from nn to n+1n+1 is given by

|  |  |  |
| --- | --- | --- |
|  | Un+1−Unk=12​Lh​[Un+1+Un]+Ih​[Un].\frac{U^{n+1}-U^{n}}{k}=\frac{1}{2}\,L\_{h}[U^{n+1}+U^{n}]+I\_{h}[U^{n}]. |  |

Sections [3.1](https://arxiv.org/html/2602.19092v1#S3.SS1 "3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps") and [3.2](https://arxiv.org/html/2602.19092v1#S3.SS2 "3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps") provide the compact spatial
stencils for LhL\_{h} and the quadrature/convolution realization of IhI\_{h}, respectively (cf. [[4](https://arxiv.org/html/2602.19092v1#bib.bib20 "The evaluation of american options in a stochastic volatility model with jumps: an efficient finite element approach"), [11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [23](https://arxiv.org/html/2602.19092v1#bib.bib15 "Galerkin finite element methods for parabolic problems")]).

### 3.1 Fourth-Order Compact Discretization of the Local Operator

We denote ui,j≈u​(xi,yj,τ)u\_{i,j}\approx u(x\_{i},y\_{j},\tau) and adopt fourth–order compact
relations to approximate first-, second-, and mixed derivatives on a 3×33\times 3
stencil. Such compact schemes are well established for elliptic and parabolic
PDEs with variable coefficients and are known for their spectral-like resolution
[[17](https://arxiv.org/html/2602.19092v1#bib.bib16 "Compact finite difference schemes with spectral-like resolution"), [22](https://arxiv.org/html/2602.19092v1#bib.bib17 "A high-order compact formulation for the 3d poisson equation"), [11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [21](https://arxiv.org/html/2602.19092v1#bib.bib3 "High-order compact finite difference schemes for option pricing in stochastic volatility jump-diffusion models")].

#### Compact line relations (1D, fourth order).

For fixed jj (differentiation in xx),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 14​ux,i−1,j+ux,i,j+14​ux,i+1,j\displaystyle\tfrac{1}{4}u\_{x,i-1,j}+u\_{x,i,j}+\tfrac{1}{4}u\_{x,i+1,j} | =ui+1,j−ui−1,j2​hx,\displaystyle=\frac{u\_{i+1,j}-u\_{i-1,j}}{2h\_{x}}, |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 112​ux​x,i−1,j+1012​ux​x,i,j+112​ux​x,i+1,j\displaystyle\tfrac{1}{12}u\_{xx,i-1,j}+\tfrac{10}{12}u\_{xx,i,j}+\tfrac{1}{12}u\_{xx,i+1,j} | =ui−1,j−2​ui,j+ui+1,jhx2.\displaystyle=\frac{u\_{i-1,j}-2u\_{i,j}+u\_{i+1,j}}{h\_{x}^{2}}. |  | (3) |

For fixed ii (differentiation in yy),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 14​uy,i,j−1+uy,i,j+14​uy,i,j+1\displaystyle\tfrac{1}{4}u\_{y,i,j-1}+u\_{y,i,j}+\tfrac{1}{4}u\_{y,i,j+1} | =ui,j+1−ui,j−12​hy,\displaystyle=\frac{u\_{i,j+1}-u\_{i,j-1}}{2h\_{y}}, |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 112​uy​y,i,j−1+1012​uy​y,i,j+112​uy​y,i,j+1\displaystyle\tfrac{1}{12}u\_{yy,i,j-1}+\tfrac{10}{12}u\_{yy,i,j}+\tfrac{1}{12}u\_{yy,i,j+1} | =ui,j−1−2​ui,j+ui,j+1hy2.\displaystyle=\frac{u\_{i,j-1}-2u\_{i,j}+u\_{i,j+1}}{h\_{y}^{2}}. |  | (5) |

#### Mixed derivative via sequential compact differentiation.

Let Mx=tridiag​(14,1,14)M\_{x}=\mathrm{tridiag}(\tfrac{1}{4},1,\tfrac{1}{4}) and DxD\_{x} the centered difference
line operator in xx, with My,DyM\_{y},D\_{y} defined analogously.
The mixed derivative is evaluated by

|  |  |  |
| --- | --- | --- |
|  | Ux​y=Mx−1​Dx​(My−1​Dy​U)=My−1​Dy​(Mx−1​Dx​U).U\_{xy}=M\_{x}^{-1}D\_{x}\big(M\_{y}^{-1}D\_{y}U\big)=M\_{y}^{-1}D\_{y}\big(M\_{x}^{-1}D\_{x}U\big). |  |

#### Compact local operator (nodewise form).

With coefficients taken directly from the transformed Bates operator
([2.1](https://arxiv.org/html/2602.19092v1#S2.Ex9 "2.1 Transformed Bates Model PIDE ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Lh​[U])i,j=ai,j​Ux​x+bi,j​Uy​y+ci,j​Ux​y+di,j​Ux+ei,j​Uy+fi,j​Ui,j,(L\_{h}[U])\_{i,j}=a\_{i,j}U\_{xx}+b\_{i,j}U\_{yy}+c\_{i,j}U\_{xy}+d\_{i,j}U\_{x}+e\_{i,j}U\_{y}+f\_{i,j}U\_{i,j}, |  | (6) |

where

|  |  |  |
| --- | --- | --- |
|  | ai,j=12​σyj,bi,j=12​σ​yj3,ci,j=−ρ​σ​yj,di,j=(r−λ)−12​σyj,\displaystyle a\_{i,j}=\frac{1}{2}\frac{\sigma}{y\_{j}},\quad b\_{i,j}=\frac{1}{2}\sigma y\_{j}^{3},\quad c\_{i,j}=-\rho\sigma y\_{j},\quad d\_{i,j}=(r-\lambda)-\frac{1}{2}\frac{\sigma}{y\_{j}},\quad |  |
|  |  |  |
| --- | --- | --- |
|  | ei,j=σ​yj2+κ​yj−κ​θ​yj2σ,fi,j=0.\displaystyle e\_{i,j}=\sigma y\_{j}^{2}+\kappa y\_{j}-\kappa\theta\frac{y\_{j}^{2}}{\sigma},\quad f\_{i,j}=0. |  |

Here Ux,Uy,Ux​x,Uy​y,Ux​yU\_{x},U\_{y},U\_{xx},U\_{yy},U\_{xy} are supplied by the compact
relations ([2](https://arxiv.org/html/2602.19092v1#S3.E2 "In Compact line relations (1D, fourth order). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"))–([5](https://arxiv.org/html/2602.19092v1#S3.E5 "In Compact line relations (1D, fourth order). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")) and the mixed
construction above. The interior accuracy satisfies

|  |  |  |
| --- | --- | --- |
|  | Lh​[u]−L​[u]=O​(hx4+hy4).L\_{h}[u]-L[u]=O(h\_{x}^{4}+h\_{y}^{4}). |  |

#### Nine-point compact balance (assembled stencil).

Eliminating auxiliary derivatives from
([2](https://arxiv.org/html/2602.19092v1#S3.E2 "In Compact line relations (1D, fourth order). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"))–([5](https://arxiv.org/html/2602.19092v1#S3.E5 "In Compact line relations (1D, fourth order). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")) within
([6](https://arxiv.org/html/2602.19092v1#S3.E6 "In Compact local operator (nodewise form). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps")) yields a 3×33\times 3 balance

|  |  |  |
| --- | --- | --- |
|  | ∑ℓ=08αℓ​uℓ=∑ℓ=08γℓ​fℓ,\sum\_{\ell=0}^{8}\alpha\_{\ell}u\_{\ell}=\sum\_{\ell=0}^{8}\gamma\_{\ell}f\_{\ell}, |  |

with {uℓ}\{u\_{\ell}\} the stencil values centered at (i,j)(i,j) and {fℓ}\{f\_{\ell}\}
the right-hand side samples (arising from PDE insertion at (i,j)(i,j)).
The weights αℓ,γℓ\alpha\_{\ell},\gamma\_{\ell} depend only on the local coefficients
and (hx,hy)(h\_{x},h\_{y}).

#### Verification template (constant coefficients).

For a=b=1a=b=1, c=d=e=0c=d=e=0, hx=hy=hh\_{x}=h\_{y}=h, the scheme reduces to the
classical fourth-order nine-point Laplacian
[[1](https://arxiv.org/html/2602.19092v1#bib.bib10 "A partial differential equation connected to option pricing with stochastic volatility: regularity results and discretization"), [7](https://arxiv.org/html/2602.19092v1#bib.bib14 "A finite difference scheme for option pricing in jump diffusion and exponential lévy models")]

|  |  |  |
| --- | --- | --- |
|  | −ui−1,j−1+16​ui,j−1−ui+1,j−1+16​ui−1,j−60​ui,j+16​ui+1,j12​h2\displaystyle\frac{-u\_{i-1,j-1}+16u\_{i,j-1}-u\_{i+1,j-1}+16u\_{i-1,j}-60u\_{i,j}+16u\_{i+1,j}}{12h^{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | +−ui−1,j+1+16​ui,j+1−ui+1,j+112​h2=fi,j+h212​Δ​fi,j.\displaystyle+\;\frac{-u\_{i-1,j+1}+16u\_{i,j+1}-u\_{i+1,j+1}}{12h^{2}}=f\_{i,j}+\tfrac{h^{2}}{12}\,\Delta f\_{i,j}. |  |

providing a convenient code check in line with established compact
formulations for financial PIDEs [[11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [12](https://arxiv.org/html/2602.19092v1#bib.bib8 "Efficient hedging in bates model using high-order compact finite differences"), [18](https://arxiv.org/html/2602.19092v1#bib.bib9 "A variable step-size extrapolated crank–nicolson method for option pricing under stochastic volatility model with jump"), [2](https://arxiv.org/html/2602.19092v1#bib.bib12 "A comparison study of adi and lod methods on option pricing models"), [3](https://arxiv.org/html/2602.19092v1#bib.bib18 "Reduced order models for pricing european and american options under stochastic volatility and jump-diffusion models")].

### 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching

The nonlocal jump part of (1) is

|  |  |  |
| --- | --- | --- |
|  | λ​∫ℝ[u​(x+z,y,τ)−u​(x,y,τ)−(ez−1)​ux​(x,y,τ)]​f​(z)​𝑑z,\lambda\int\_{\mathbb{R}}\big[u(x+z,y,\tau)-u(x,y,\tau)-(e^{z}-1)u\_{x}(x,y,\tau)\big]f(z)\,dz, |  |

with log-normal jump density f​(z)f(z)
[[19](https://arxiv.org/html/2602.19092v1#bib.bib6 "Option pricing when underlying stock returns are discontinuous"), [5](https://arxiv.org/html/2602.19092v1#bib.bib5 "Jumps and stochastic volatility: exchange rate processes implicit in deutsche mark options"), [7](https://arxiv.org/html/2602.19092v1#bib.bib14 "A finite difference scheme for option pricing in jump diffusion and exponential lévy models")]. The compensator
(ez−1)​ux(e^{z}-1)u\_{x} guarantees integrability and preserves the martingale
condition.

#### Discrete jump operator.

On the grid, we approximate

|  |  |  |
| --- | --- | --- |
|  | (Ih​[u])i,j=λ​∑m=−MMωm​[u​(xi+zm,yj,τ)−u​(xi,yj,τ)−(ezm−1)​Dx​u​(xi,yj,τ)],(I\_{h}[u])\_{i,j}=\lambda\sum\_{m=-M}^{M}\omega\_{m}\big[u(x\_{i}+z\_{m},y\_{j},\tau)-u(x\_{i},y\_{j},\tau)-(e^{z\_{m}}-1)D\_{x}u(x\_{i},y\_{j},\tau)\big], |  |

using quadrature nodes {zm}\{z\_{m}\} and weights {ωm}\{\omega\_{m}\}, with
interpolation for off-grid values
[[7](https://arxiv.org/html/2602.19092v1#bib.bib14 "A finite difference scheme for option pricing in jump diffusion and exponential lévy models"), [11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [18](https://arxiv.org/html/2602.19092v1#bib.bib9 "A variable step-size extrapolated crank–nicolson method for option pricing under stochastic volatility model with jump")].

#### IMEX–CN scheme.

The semi-discrete system

|  |  |  |
| --- | --- | --- |
|  | dd​τ​U=Lh​[U]+Ih​[U]\frac{d}{d\tau}U=L\_{h}[U]+I\_{h}[U] |  |

is advanced in time by the IMEX–Crank–Nicolson method
[[16](https://arxiv.org/html/2602.19092v1#bib.bib11 "Initial boundary value problems for hyperbolic systems"), [2](https://arxiv.org/html/2602.19092v1#bib.bib12 "A comparison study of adi and lod methods on option pricing models")]:

|  |  |  |
| --- | --- | --- |
|  | Un+1−Unk=12​Lh​[Un+1+Un]+Ih​[Un],\frac{U^{n+1}-U^{n}}{k}=\frac{1}{2}L\_{h}[U^{n+1}+U^{n}]+I\_{h}[U^{n}], |  |

treating LhL\_{h} implicitly and IhI\_{h} explicitly. This combination
retains unconditional stability for the stiff diffusion operator while
avoiding costly implicit treatment of the integral. The scheme fits
naturally into high-order compact PIDE solvers
[[11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [12](https://arxiv.org/html/2602.19092v1#bib.bib8 "Efficient hedging in bates model using high-order compact finite differences"), [21](https://arxiv.org/html/2602.19092v1#bib.bib3 "High-order compact finite difference schemes for option pricing in stochastic volatility jump-diffusion models")].

## 4 Initial and Boundary Conditions

For the transformed Bates PIDE we prescribe the payoff as the initial
condition at τ=0\tau=0:

|  |  |  |
| --- | --- | --- |
|  | u​(x,y,0)=max⁡(1−ex,0).u(x,y,0)=\max(1-e^{x},0). |  |

At the far left boundary xminx\_{\min}, the option value approaches the
discounted intrinsic value. Thus we impose

|  |  |  |
| --- | --- | --- |
|  | u​(xmin,y,τ)=e(r+λ)​τ​(1−exmin).u(x\_{\min},y,\tau)=e^{(r+\lambda)\tau}\,\big(1-e^{x\_{\min}}\big). |  |

At the far right boundary xmaxx\_{\max}, the put option value decays, so we
set:

|  |  |  |
| --- | --- | --- |
|  | u​(xmax,y,τ)=0.u(x\_{\max},y,\tau)=0. |  |

In the variance direction, we impose homogeneous Neumann conditions:

|  |  |  |
| --- | --- | --- |
|  | ∂yu​(x,ymin,τ)=0,∂yu​(x,ymax,τ)=0.\partial\_{y}u(x,y\_{\min},\tau)=0,\qquad\partial\_{y}u(x,y\_{\max},\tau)=0. |  |

These conditions ensure consistency with the no-arbitrage bounds for
European puts under stochastic volatility jump–diffusion dynamics.

## 5 Benchmarking via the Finite Element Method

We benchmark the compact finite-difference scheme against a conforming finite
element method (FEM) applied to the transformed Bates PIDE under identical
payoff and boundary conditions. The comparison highlights accuracy, stability,
and computational cost.

#### Weak formulation.

Writing the local operator in divergence form, we enforce economic Dirichlet
conditions on vertical boundaries and homogeneous Neumann conditions on
horizontal ones, consistent with the FD setup. The weak form reads

|  |  |  |
| --- | --- | --- |
|  | (un+1−unΔ​τ,ψ)+a​(un+1+un2,ψ)=(32​LI​[un]−12​LI​[un−1],ψ),∀ψ∈V,\Big(\tfrac{u^{n+1}-u^{n}}{\Delta\tau},\psi\Big)+a\!\left(\tfrac{u^{n+1}+u^{n}}{2},\psi\right)=\Big(\tfrac{3}{2}L\_{I}[u^{n}]-\tfrac{1}{2}L\_{I}[u^{n-1}],\psi\Big),\quad\forall\psi\in V, |  |

with V={ψ∈H1​(Ω):ψ|ΓD=0}V=\{\psi\in H^{1}(\Omega):\psi|\_{\Gamma\_{D}}=0\} and bilinear form

|  |  |  |
| --- | --- | --- |
|  | a​(u,ψ)=∫ΩA​∇u⋅∇ψ​d​x​d​y+∫Ω(b⋅∇u)​ψ​𝑑x​𝑑y.a(u,\psi)=\int\_{\Omega}A\nabla u\cdot\nabla\psi\,dxdy+\int\_{\Omega}(b\cdot\nabla u)\psi\,dxdy. |  |

#### Spatial discretization.

In a regular shape mesh we use Vh⊂VV\_{h}\subset V with continuous quadratic
elements (P2/Q2). The Gaussian quadrature yields the mass MM, stiffness KK, and
convection CC matrices. For coefficient vector UnU^{n},

|  |  |  |
| --- | --- | --- |
|  | Ah​Un+1=Bh​Un+Δ​τ​(32​Fn−12​Fn−1),A\_{h}U^{n+1}=B\_{h}U^{n}+\Delta\tau\Big(\tfrac{3}{2}F^{n}-\tfrac{1}{2}F^{n-1}\Big), |  |

with Ah=M+Δ​τ2​(K+C)A\_{h}=M+\tfrac{\Delta\tau}{2}(K+C), Bh=M−Δ​τ2​(K+C)B\_{h}=M-\tfrac{\Delta\tau}{2}(K+C),
and Fn=(LI​[uhn],ϕi)F^{n}=(L\_{I}[u\_{h}^{n}],\phi\_{i}).
  
For time-independent coefficients, a sparse
factorization of AhA\_{h} is reused.

#### Jump treatment.

The nonlocal operator is evaluated explicitly by Simpson quadrature on a
truncated log-jump interval, with FEM interpolation at off-grid xx-values.
This keeps the implicit system confined to local terms.

#### Takeaway.

FEM achieves near second-order spatial convergence for quadratic elements
[[23](https://arxiv.org/html/2602.19092v1#bib.bib15 "Galerkin finite element methods for parabolic problems"), [4](https://arxiv.org/html/2602.19092v1#bib.bib20 "The evaluation of american options in a stochastic volatility model with jumps: an efficient finite element approach"), [24](https://arxiv.org/html/2602.19092v1#bib.bib19 "Pricing european and american options under heston model using discontinuous galerkin finite elements")], but in
structured domains HOC–FD attains comparable accuracy with significantly
lower runtime and memory [[11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [21](https://arxiv.org/html/2602.19092v1#bib.bib3 "High-order compact finite difference schemes for option pricing in stochastic volatility jump-diffusion models")].

## 6 Numerical Experiments

We evaluate the (HOC–FD) scheme for the transformed Bates PIDE against second–order finite differences and FEM
with Lagrange bases of degree p=1,2p=1,2. All solvers employ identical payoff
and boundary conditions, the IMEX–CN scheme for local terms,
and explicit Simpson quadrature on a truncated interval for the jump
integral. Accuracy is measured by discrete L2L^{2} error and RMSE relative to
a high–resolution reference, while efficiency is assessed in terms of
degrees of freedom, CPU time, memory usage, and a cost–accuracy ratio.

Table 1: Simulation parameters used in Bates model experiments

| Parameter | Value | Parameter | Value | Parameter | Value |
| --- | --- | --- | --- | --- | --- |
| KK | 110 | TT (years) | 1.0 | rr | 0.03 |
| κ\kappa | 1.8 | θ\theta | 0.02 | ρ\rho | −0.4-0.4 |
| σ\sigma | 0.15 | λ\lambda | 0.25 | Jump law | Lognormal |
| μJ\mu\_{J} | set per exp. | σJ\sigma\_{J} | set per exp. | – | – |



‘ ![Refer to caption](x1.png)

Figure 1: European put price V​(S,t)V(S,t) under the Bates model for
S∈[70,130]S\in[70,130]. The intrinsic payoff max⁡(K−S,0)\max(K-S,0) and the
no-arbitrage lower bound max⁡{K​e−r​T−S,0}\max\{Ke^{-rT}-S,0\} are shown as
reference curves

### 6.1 Numerical Convergence

We measure numerical accuracy using three error norms:

|  |  |  |
| --- | --- | --- |
|  | ‖uh−ur​e​f‖L2=(hx​hy​∑i=1Nx∑j=1Ny(ui,jh−ui,jr​e​f)2)1/2,\|u^{h}-u^{ref}\|\_{L^{2}}=\left(h\_{x}h\_{y}\sum\_{i=1}^{N\_{x}}\sum\_{j=1}^{N\_{y}}(u^{h}\_{i,j}-u^{ref}\_{i,j})^{2}\right)^{1/2}, |  |

the discrete L2L^{2} error norm, which approximates the continuous integral norm;

|  |  |  |
| --- | --- | --- |
|  | RMSE=(1Nx​Ny​∑i=1Nx∑j=1Ny(ui,jh−ui,jr​e​f)2)1/2,\text{RMSE}=\left(\frac{1}{N\_{x}N\_{y}}\sum\_{i=1}^{N\_{x}}\sum\_{j=1}^{N\_{y}}(u^{h}\_{i,j}-u^{ref}\_{i,j})^{2}\right)^{1/2}, |  |

the root-mean-square error, representing average nodal error; and

|  |  |  |
| --- | --- | --- |
|  | ‖uh−ur​e​f‖L∞=max1≤i≤Nx, 1≤j≤Ny⁡|ui,jh−ui,jr​e​f|,\|u^{h}-u^{ref}\|\_{L^{\infty}}=\max\_{1\leq i\leq N\_{x},\,1\leq j\leq N\_{y}}|u^{h}\_{i,j}-u^{ref}\_{i,j}|, |  |

the maximum pointwise error.

Thus, L2L^{2} reflects global accuracy, RMSE captures average nodal error, and L∞L^{\infty} highlights the worst-case deviation [[23](https://arxiv.org/html/2602.19092v1#bib.bib15 "Galerkin finite element methods for parabolic problems"), [2](https://arxiv.org/html/2602.19092v1#bib.bib12 "A comparison study of adi and lod methods on option pricing models"), [16](https://arxiv.org/html/2602.19092v1#bib.bib11 "Initial boundary value problems for hyperbolic systems")].

Table 2: Observed convergence orders in space and time, comparing HOC–FD
with second–order finite differences [[7](https://arxiv.org/html/2602.19092v1#bib.bib14 "A finite difference scheme for option pricing in jump diffusion and exponential lévy models"), [2](https://arxiv.org/html/2602.19092v1#bib.bib12 "A comparison study of adi and lod methods on option pricing models")]
and FEM(P2) [[23](https://arxiv.org/html/2602.19092v1#bib.bib15 "Galerkin finite element methods for parabolic problems"), [4](https://arxiv.org/html/2602.19092v1#bib.bib20 "The evaluation of american options in a stochastic volatility model with jumps: an efficient finite element approach"), [24](https://arxiv.org/html/2602.19092v1#bib.bib19 "Pricing european and american options under heston model using discontinuous galerkin finite elements")].
Spatial studies fix Δ​τ/h2\Delta\tau/h^{2}; temporal studies fix hh

| Method | Spatial order psp\_{s} | Temporal order ptp\_{t} |
| --- | --- | --- |
| FEM (P2) | ≈2.0\approx 2.0 (both L2L^{2}, L∞L^{\infty}) | ≈2.0\approx 2.0 (CN, BDF2, MP) |
| HOC–FD (compact) | ≈4.0\approx 4.0 (both L2L^{2}, L∞L^{\infty}) | ≈2.0\approx 2.0 (IMEX–CN) |

### 6.2 Computational Efficiency Comparison

Efficiency was assessed using the cost–accuracy ratio

|  |  |  |
| --- | --- | --- |
|  | ηA/B=εA2​tAεB2​tB,ε∈{∥⋅∥L2,RMSE},\eta\_{A/B}=\frac{\varepsilon\_{A}^{2}\,t\_{A}}{\varepsilon\_{B}^{2}\,t\_{B}},\qquad\varepsilon\in\{\|\cdot\|\_{L^{2}},\mathrm{RMSE}\}, |  |

reported relative to the HOC–FD baseline (η=1\eta=1). Here tt denotes CPU time.

Table 3 shows that, at matched settings, the compact HOC–FD scheme attains
comparable accuracy at substantially lower runtime on structured grids.
Relative to HOC–FD, FEM(P2) is roughly two orders of magnitude more costly,
while second–order FD variants are within single–digit multiples of the
baseline. These results confirm earlier findings that compact FD schemes
achieve significant efficiency gains over FEM in structured domains
[[11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [4](https://arxiv.org/html/2602.19092v1#bib.bib20 "The evaluation of american options in a stochastic volatility model with jumps: an efficient finite element approach"), [24](https://arxiv.org/html/2602.19092v1#bib.bib19 "Pricing european and american options under heston model using discontinuous galerkin finite elements")].

Table 3: Efficiency snapshot at h=0.1h=0.1 relative to HOC–FD baseline
[[11](https://arxiv.org/html/2602.19092v1#bib.bib7 "High-order compact finite difference scheme for option pricing in stochastic volatility jump models"), [21](https://arxiv.org/html/2602.19092v1#bib.bib3 "High-order compact finite difference schemes for option pricing in stochastic volatility jump-diffusion models")]. Comparisons include second–order
finite differences [[7](https://arxiv.org/html/2602.19092v1#bib.bib14 "A finite difference scheme for option pricing in jump diffusion and exponential lévy models"), [2](https://arxiv.org/html/2602.19092v1#bib.bib12 "A comparison study of adi and lod methods on option pricing models")] and FEM(P2)
[[23](https://arxiv.org/html/2602.19092v1#bib.bib15 "Galerkin finite element methods for parabolic problems"), [4](https://arxiv.org/html/2602.19092v1#bib.bib20 "The evaluation of american options in a stochastic volatility model with jumps: an efficient finite element approach"), [24](https://arxiv.org/html/2602.19092v1#bib.bib19 "Pricing european and american options under heston model using discontinuous galerkin finite elements")]. Errors
measured against a high–resolution reference; η\eta uses L2L^{2} error and runtime

| Method | DOF | Time (s) | 𝑳𝟐L^{2} | RMSE | 𝜼\eta |
| --- | --- | --- | --- | --- | --- |
| HOC–FD (IMEX–CN) | 1,681 | 1.106 | 0.0230 | 0.0095 | 1.00 |
| FEM (P2P\_{2}) | 6,561 | 23.426 | 0.1522 | 0.0475 | ≈1.40×102\approx 1.40\times 10^{2} |
| CN (2nd–order FD) | 1,681 | 2.230 | 0.0341 | 0.0148 | ≈2.99\approx 2.99 |
| BDF2 (2nd–order FD) | 1,681 | 2.904 | 0.0417 | 0.0181 | ≈4.76\approx 4.76 |
| Midpoint (FD) | 1,681 | 3.117 | 0.0425 | 0.0185 | ≈5.21\approx 5.21 |

## 7 Conclusion

We developed a fourth–order compact finite–difference scheme for the transformed
Bates PIDE, combining an IMEX–Crank–Nicolson split for local terms with explicit
Simpson quadrature for the jump integral. Benchmarks against second–order finite
differences and quadratic FEM confirmed near–fourth–order spatial accuracy for the
compact scheme and near–second–order for FEM, with all time integrators exhibiting
second–order accuracy. Efficiency tests on structured grids showed that the compact
scheme achieves substantially lower runtimes—up to two orders of magnitude faster
than FEM—while maintaining comparable pricing accuracy. This establishes the
scheme as a competitive baseline for structured–domain option pricing. Future work
will extend the method to American and path–dependent payoffs, adaptive meshes,
broader jump specifications, and accelerated integral solvers.

## 8 Acknowledgements

The first author was supported by Comenius University grant UK/1024/2025. The second author received support from the Slovak VEGA 1-0493-24 agency.

## References

* [1]
  Y. Achdou, B. Franchi, and N. Tchou (2005)
  A partial differential equation connected to option pricing with stochastic volatility: regularity results and discretization.
  Mathematics of Computation 74 (251),  pp. 1291–1322.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.SSS0.Px5.p1.3 "Verification template (constant coefficients). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [2]
  N. Bagheri and H. K. Haghighi (2017)
  A comparison study of adi and lod methods on option pricing models.
  Journal of Mathematical Finance 7 (2),  pp. 275–290.
  External Links: ISSN 2162-2442
  Cited by: [§2](https://arxiv.org/html/2602.19092v1#S2.p1.1 "2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.SSS0.Px5.p1.4 "Verification template (constant coefficients). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px2.p1.4 "IMEX–CN scheme. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§6.1](https://arxiv.org/html/2602.19092v1#S6.SS1.p8.2 "6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 2](https://arxiv.org/html/2602.19092v1#S6.T2 "In 6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 3](https://arxiv.org/html/2602.19092v1#S6.T3 "In 6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [3]
  M. Balajewicz and J. Toivanen (2017)
  Reduced order models for pricing european and american options under stochastic volatility and jump-diffusion models.
  Journal of Computational Science 20,  pp. 198–204.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.SSS0.Px5.p1.4 "Verification template (constant coefficients). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [4]
  L. V. Ballestra and C. Sgarra (2010)
  The evaluation of american options in a stochastic volatility model with jumps: an efficient finite element approach.
  Computers & Mathematics with Applications 60 (6),  pp. 1571–1590.
  Cited by: [§2](https://arxiv.org/html/2602.19092v1#S2.SS0.SSS0.Px2.p1.9 "Option–pricing PIDE. ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3](https://arxiv.org/html/2602.19092v1#S3.p1.18 "3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§5](https://arxiv.org/html/2602.19092v1#S5.SS0.SSS0.Px4.p1.1 "Takeaway. ‣ 5 Benchmarking via the Finite Element Method ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§6.2](https://arxiv.org/html/2602.19092v1#S6.SS2.p2.1 "6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 2](https://arxiv.org/html/2602.19092v1#S6.T2 "In 6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 3](https://arxiv.org/html/2602.19092v1#S6.T3 "In 6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [5]
  D. S. Bates (1996)
  Jumps and stochastic volatility: exchange rate processes implicit in deutsche mark options.
  The Review of Financial Studies 9 (1),  pp. 69–107.
  Cited by: [§2](https://arxiv.org/html/2602.19092v1#S2.SS0.SSS0.Px2.p1.9 "Option–pricing PIDE. ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.p1.2 "3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [6]
  F. Black and M. Scholes (1973)
  The pricing of options and corporate liabilities.
  Journal of Political Economy 81 (3),  pp. 637–654.
  Cited by: [§2](https://arxiv.org/html/2602.19092v1#S2.p1.1 "2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [7]
  R. Cont and E. Voltchkova (2005)
  A finite difference scheme for option pricing in jump diffusion and exponential lévy models.
  SIAM Journal on Numerical Analysis 43 (4),  pp. 1596–1626.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.SSS0.Px5.p1.3 "Verification template (constant coefficients). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px1.p1.2 "Discrete jump operator. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.p1.2 "3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 2](https://arxiv.org/html/2602.19092v1#S6.T2 "In 6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 3](https://arxiv.org/html/2602.19092v1#S6.T3 "In 6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [8]
  J. M. T. S. Cruz and D. Ševčovič (2020)
  On solutions of a partial integro-differential equation in bessel potential spaces with applications in option pricing models.
  Japan Journal of Industrial and Applied Mathematics 37 (3),  pp. 697–721.
  Cited by: [§1](https://arxiv.org/html/2602.19092v1#S1.p1.1 "1 Introduction ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [9]
  J. M. Cruz and D. Ševčovič (2018)
  Option pricing in illiquid markets with jumps.
  Applied Mathematical Finance 25 (4),  pp. 395–415.
  Cited by: [§1](https://arxiv.org/html/2602.19092v1#S1.p1.1 "1 Introduction ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§2](https://arxiv.org/html/2602.19092v1#S2.p1.1 "2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [10]
  D. Dimitrov and L. Vulkov (2016)
  High order finite difference schemes on non-uniform meshes for the time-fractional black–scholes equation.
  Applied Numerical Mathematics 111,  pp. 251–266.
  Cited by: [§1](https://arxiv.org/html/2602.19092v1#S1.p1.1 "1 Introduction ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [11]
  B. Düring and A. Pitkin (2019)
  High-order compact finite difference scheme for option pricing in stochastic volatility jump models.
  Journal of Computational and Applied Mathematics 355,  pp. 201–217.
  Cited by: [§2](https://arxiv.org/html/2602.19092v1#S2.SS0.SSS0.Px1.p1.12 "Risk–neutral dynamics. ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§2.1](https://arxiv.org/html/2602.19092v1#S2.SS1.p1.4 "2.1 Transformed Bates Model PIDE ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.SSS0.Px5.p1.4 "Verification template (constant coefficients). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.p1.2 "3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px1.p1.2 "Discrete jump operator. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px2.p1.2 "IMEX–CN scheme. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3](https://arxiv.org/html/2602.19092v1#S3.p1.18 "3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§5](https://arxiv.org/html/2602.19092v1#S5.SS0.SSS0.Px4.p1.1 "Takeaway. ‣ 5 Benchmarking via the Finite Element Method ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§6.2](https://arxiv.org/html/2602.19092v1#S6.SS2.p2.1 "6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 3](https://arxiv.org/html/2602.19092v1#S6.T3 "In 6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [12]
  B. Düring and A. Pitkin (2024)
  Efficient hedging in bates model using high-order compact finite differences.
  arXiv preprint arXiv:1710.05542.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.SSS0.Px5.p1.4 "Verification template (constant coefficients). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px2.p1.2 "IMEX–CN scheme. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [13]
  M. N. Koleva, L. G. Vulkov, and T. Mudzimbabwe (2017)
  Fourth-order compact schemes for a parabolic-ordinary system of european option pricing liquidity shocks model.
  Numerical Algorithms 74,  pp. 1075–1098.
  Cited by: [§1](https://arxiv.org/html/2602.19092v1#S1.p1.1 "1 Introduction ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [14]
  M. N. Koleva and L. G. Vulkov (2013)
  A kernel-based algorithm for numerical solution of nonlinear pdes in finance.
  In Numerical Analysis and Its Applications (NAA 2012),
  Lecture Notes in Computer Science, Vol. 8236,  pp. 520–527.
  Cited by: [§1](https://arxiv.org/html/2602.19092v1#S1.p1.1 "1 Introduction ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [15]
  M. N. Koleva and L. G. Vulkov (2014)
  A positive flux limited difference scheme for option pricing 2d fully non-linear parabolic equation with uncertain correlation.
  Journal of Computational and Applied Mathematics 271,  pp. 368–382.
  Cited by: [§1](https://arxiv.org/html/2602.19092v1#S1.p1.1 "1 Introduction ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [16]
  H. Kreiss (1970)
  Initial boundary value problems for hyperbolic systems.
  Communications on Pure and Applied Mathematics 23 (3),  pp. 277–298.
  Cited by: [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px2.p1.4 "IMEX–CN scheme. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§6.1](https://arxiv.org/html/2602.19092v1#S6.SS1.p8.2 "6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [17]
  S. K. Lele (1992)
  Compact finite difference schemes with spectral-like resolution.
  Journal of Computational Physics 103 (1),  pp. 16–42.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.p1.2 "3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [18]
  M. Mao, H. Tian, and W. Wang (2024)
  A variable step-size extrapolated crank–nicolson method for option pricing under stochastic volatility model with jump.
  Mathematical Methods in the Applied Sciences 47 (2),  pp. 762–781.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.SSS0.Px5.p1.4 "Verification template (constant coefficients). ‣ 3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px1.p1.2 "Discrete jump operator. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [19]
  R. C. Merton (1976)
  Option pricing when underlying stock returns are discontinuous.
  Journal of Financial Economics 3 (1-2),  pp. 125–144.
  Cited by: [§2](https://arxiv.org/html/2602.19092v1#S2.SS0.SSS0.Px1.p1.12 "Risk–neutral dynamics. ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.p1.2 "3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [20]
  E. Pankratov (2018)
  Nonlinear profit maximization with account changing of prices.
  International journal of modeling, simulation and applications 2 (2),  pp. 9–17.
  Cited by: [§2.1](https://arxiv.org/html/2602.19092v1#S2.SS1.p1.4 "2.1 Transformed Bates Model PIDE ‣ 2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [21]
  A. Pitkin (2020)
  High-order compact finite difference schemes for option pricing in stochastic volatility jump-diffusion models.
  Ph.D. Thesis, University of Sussex.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.p1.2 "3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3.2](https://arxiv.org/html/2602.19092v1#S3.SS2.SSS0.Px2.p1.2 "IMEX–CN scheme. ‣ 3.2 Nonlocal Jump Operator and IMEX–CN Time Marching ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§5](https://arxiv.org/html/2602.19092v1#S5.SS0.SSS0.Px4.p1.1 "Takeaway. ‣ 5 Benchmarking via the Finite Element Method ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 3](https://arxiv.org/html/2602.19092v1#S6.T3 "In 6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [22]
  W. F. Spotz and G. F. Carey (1996)
  A high-order compact formulation for the 3d poisson equation.
  Numerical Methods for Partial Differential Equations: An International Journal 12 (2),  pp. 235–243.
  Cited by: [§3.1](https://arxiv.org/html/2602.19092v1#S3.SS1.p1.2 "3.1 Fourth-Order Compact Discretization of the Local Operator ‣ 3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [23]
  V. Thomée (2007)
  Galerkin finite element methods for parabolic problems.
  Vol. 25, Springer Science & Business Media.
  Cited by: [§2](https://arxiv.org/html/2602.19092v1#S2.p1.1 "2 Stochastic Differential Equations of the Bates Model ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§3](https://arxiv.org/html/2602.19092v1#S3.p1.18 "3 Spatial Discretization and IMEX–Crank–Nicolson ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§5](https://arxiv.org/html/2602.19092v1#S5.SS0.SSS0.Px4.p1.1 "Takeaway. ‣ 5 Benchmarking via the Finite Element Method ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§6.1](https://arxiv.org/html/2602.19092v1#S6.SS1.p8.2 "6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 2](https://arxiv.org/html/2602.19092v1#S6.T2 "In 6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 3](https://arxiv.org/html/2602.19092v1#S6.T3 "In 6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").
* [24]
  M. Uzunca et al. (2020)
  Pricing european and american options under heston model using discontinuous galerkin finite elements.
  Technical report
   arXiv.org.
  Cited by: [§5](https://arxiv.org/html/2602.19092v1#S5.SS0.SSS0.Px4.p1.1 "Takeaway. ‣ 5 Benchmarking via the Finite Element Method ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [§6.2](https://arxiv.org/html/2602.19092v1#S6.SS2.p2.1 "6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 2](https://arxiv.org/html/2602.19092v1#S6.T2 "In 6.1 Numerical Convergence ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps"),
  [Table 3](https://arxiv.org/html/2602.19092v1#S6.T3 "In 6.2 Computational Efficiency Comparison ‣ 6 Numerical Experiments ‣ Finite Element Solution of the Two-Dimensional Bates Model for Option Pricing Under Stochastic Volatility and Jumps").