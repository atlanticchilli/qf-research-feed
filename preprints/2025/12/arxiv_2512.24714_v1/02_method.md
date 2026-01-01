---
authors:
- Xiang Gao
- Cody Hyndman
doc_id: arxiv:2512.24714v1
family_id: arxiv:2512.24714
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Boundary error control for numerical solution of BSDEs by the convolution-FFT
  method
url_abs: http://arxiv.org/abs/2512.24714v1
url_html: https://arxiv.org/html/2512.24714v1
venue: arXiv q-fin
version: 1
year: 2025
---


Xiang Gao111Department of Mathematics and Statistics,
Concordia University,
1455 Boulevard de Maisonneuve Ouest,
Montréal, Québec,
Canada H3G 1M8.
and
Cody Hyndman11footnotemark: 1   222Corresponding Author: cody.hyndman@concordia.ca

(November 3, 2025)

###### Abstract

We first review the convolution fast-Fourier-transform (CFFT) approach for the numerical solution of backward stochastic differential equations (BSDEs) introduced in (Hyndman and
Oyono Ngou, [2017](https://arxiv.org/html/2512.24714v1#bib.bib10)). We then propose a method for improving the boundary errors obtained when valuing options using this approach. We modify the damping and shifting schemes used in the original formulation, which transforms the target function into a bounded periodic function so that Fourier transforms can be applied successfully. Time-dependent shifting reduces boundary error significantly. We present numerical results for our implementation and provide a detailed error analysis showing the improved accuracy and convergence of the modified convolution method.

Keywords:
Backward stochastic differential equations; numerical method; error control; fast Fourier transform; convolution method; option pricing

Mathematics Subject Classification (2020):
Primary: 65T50, 60H35; Secondary: 91G60, 60H30,

## 1 Introduction

In this paper we study a convolution-based numerical method for solving backward stochastic differential equations (BSDEs) that arise in option valuation. Specifically, we consider the coupled forward–backward system

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xt\displaystyle X\_{t} | =x+∫0tη​(s,Xs)​𝑑s+∫0tσ​(s,Xs)​𝑑Ws,\displaystyle=x+\int\_{0}^{t}\eta(s,X\_{s})\,ds+\int\_{0}^{t}\sigma(s,X\_{s})\,dW\_{s}, |  | (1.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Yt\displaystyle Y\_{t} | =g​(XT)+∫tTf​(s,Xs,Ys,Zs)​𝑑s−∫tTZs⊤​𝑑Ws,\displaystyle=g(X\_{T})+\int\_{t}^{T}f(s,X\_{s},Y\_{s},Z\_{s})\,ds-\int\_{t}^{T}Z\_{s}^{\top}\,dW\_{s}, |  | (1.2) |

on a filtered probability space (Ω,ℱ,{ℱt}t∈[0,T],ℙ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{P}), where WW is an nn-dimensional Brownian motion and {ℱt}\{\mathcal{F}\_{t}\} is its augmented natural filtration. Given the coefficient functions η\eta, σ\sigma, ff, and terminal condition gg, the unknown adapted processes are (Xt,Yt,Zt)(X\_{t},Y\_{t},Z\_{t}).

Pardoux and
Peng ([1990](https://arxiv.org/html/2512.24714v1#bib.bib16)) first introduced nonlinear BSDEs and established foundational existence and uniqueness results. Subsequent work developed the theory in several directions, including forward–backward SDEs (FBSDEs) Antonelli ([1993](https://arxiv.org/html/2512.24714v1#bib.bib1)), solvability and well-posedness results Yong ([1997](https://arxiv.org/html/2512.24714v1#bib.bib19)), and extensions beyond the globally Lipschitz setting, including quadratic-growth drivers Kobylanski ([2000](https://arxiv.org/html/2512.24714v1#bib.bib11)).

BSDEs have many applications in mathematical finance, including pricing, hedging, and nonlinear valuation problems. As a result, numerical methods for BSDEs have been studied extensively. Common approaches include simulation-based schemes Bouchard and
Touzi ([2004](https://arxiv.org/html/2512.24714v1#bib.bib4)), PDE-based discretizations Douglas
et al. ([1996](https://arxiv.org/html/2512.24714v1#bib.bib6)), Picard iteration Bender and
Denk ([2007](https://arxiv.org/html/2512.24714v1#bib.bib2)), and regression-based methods Lemor
et al. ([2006](https://arxiv.org/html/2512.24714v1#bib.bib12)). Spatial discretization methods for Markovian BSDEs can be found, for example, in Huijskens
et al. ([2016](https://arxiv.org/html/2512.24714v1#bib.bib9)) and in Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)).

The convolution method for numerical solution of BSDEs introduced in Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)) is fast and accurate, and was further studied in Oyono Ngou and
Hyndman ([2022](https://arxiv.org/html/2512.24714v1#bib.bib15)) through alternative spatial approximation schemes aimed at reducing extrapolation error. However, in the original formulation, numerical errors can grow rapidly as the initial value of the forward process approaches the truncation boundaries. This paper is complementary to our convolution–FFT methods for option pricing based on characteristic functions under the Heston model Gao and
Hyndman ([2025](https://arxiv.org/html/2512.24714v1#bib.bib8)). While the Heston model convolution–FFT approach focuses on Fourier inversion of terminal payoffs, the present paper develops a convolution-based time-stepping scheme for general BSDEs. Throughout, the convolution representation is understood as a short-time approximation consistent with the underlying time discretization of the BSDE.

The paper is organized as follows. In Section [2](https://arxiv.org/html/2512.24714v1#S2 "2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), we review the convolution method with an implicit Euler time discretization scheme for BSDEs. In Section [3](https://arxiv.org/html/2512.24714v1#S3 "3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), we introduce the proposed boundary-error control method and provide an error analysis describing how local errors vary with respect to the initial value. In Section [4](https://arxiv.org/html/2512.24714v1#S4 "4 Numerical result of option pricing ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), we present numerical results for option valuation and compare the performance of the modified method with the original scheme of Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)). Section [5](https://arxiv.org/html/2512.24714v1#S5 "5 Conclusion ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") concludes and an appendix contains proofs of technical results.

## 2 Assumptions and the convolution method

In this section, we will review the convolution approach to the numerical solution of BSDEs introduced in Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)). To ensure the existence and uniqueness of an adapted solution to ([1.1](https://arxiv.org/html/2512.24714v1#S1.E1 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"))-([1.2](https://arxiv.org/html/2512.24714v1#S1.E2 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), we require the following conditions (see e.g. Ma
et al. ([1999](https://arxiv.org/html/2512.24714v1#bib.bib14))) to be satisfied.

###### Assumption 2.1.

For η:[0,T]×ℝ→ℝ\eta:[0,T]\times\mathbb{R}\rightarrow\mathbb{R}, σ:[0,T]×ℝ→ℝ\sigma:[0,T]\times\mathbb{R}\rightarrow\mathbb{R}, f:[0,T]×ℝ×ℝ×ℝ→ℝf:[0,T]\times\mathbb{R}\times\mathbb{R}\times\mathbb{R}\rightarrow\mathbb{R} and g:ℝ→ℝg:\mathbb{R}\rightarrow\mathbb{R} assume:

* (i)

  The functions η\eta, σ\sigma, ff, and gg are uniformly Lipschitz continuous with bounded first order derivatives in the space variables, for all t∈[0,T]t\in[0,T]:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |η​(t,u)−η​(t,v)|≤\displaystyle|\eta(t,u)-\eta(t,v)|\leq | K​(|u−v|),\displaystyle K(|u-v|), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |σ​(t,u)−σ​(t,v)|≤\displaystyle|\sigma(t,u)-\sigma(t,v)|\leq | K​(|u−v|),\displaystyle K(|u-v|), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |g​(u)−g​(v)|≤\displaystyle|g(u)-g(v)|\leq | K​(|u−v|),\displaystyle K(|u-v|), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |f​(t,ξ)−f​(t,ζ)|≤\displaystyle|f(t,\xi)-f(t,\zeta)|\leq | K​(‖ξ−ζ‖∞),\displaystyle K(\|\xi-\zeta\|\_{\infty}), |  |

  for some constant KK independent of u,v∈ℝu,v\in\mathbb{R} and ξ,ζ∈ℝ×ℝ×ℝ\xi,\zeta\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}.
* (ii)

  The volatility Σ​(t,x)=σ​(t,x)​σ⊤​(t,x)\Sigma(t,x)={\sigma(t,x)}{\sigma}^{\top}(t,x) is continuous and L2L^{2}-bounded
  ‖Σ‖2≤C,\|\Sigma\|\_{2}\leq C,
  for some positive constant CC.

Using a uniform time discretization with step size Δ​t=ti+1−ti\Delta t=t\_{i+1}-t\_{i} we write
Xi=XtiX\_{i}=X\_{t\_{i}}, Yi=YtiY\_{i}=Y\_{t\_{i}}, Zi=ZtiZ\_{i}=Z\_{t\_{i}}, and Δ​Wi=(Wti+1−Wi)\Delta W\_{i}=(W\_{t\_{i+1}}-W\_{i}). Applying a first-order Euler scheme we have

|  |  |  |
| --- | --- | --- |
|  | Xi+1=Xi+η​(ti,Xi)​Δ​t+σ​(ti,Xi)​Δ​Wi;X0=x;i=0,…,N−1X\_{i+1}=X\_{i}+\eta(t\_{i},X\_{i})\Delta t+\sigma(t\_{i},X\_{i})\Delta W\_{i};\qquad X\_{0}=x;\qquad i=0,\ldots,N-1 |  |

for the approximation of the forward SDE ([1.1](https://arxiv.org/html/2512.24714v1#S1.E1 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) and

|  |  |  |
| --- | --- | --- |
|  | Yi=Yi+1+f​(i,Xi,Yi,Zi)​Δ​t−Zi​Δ​Wi;YN=g​(XN),ZN=0i=N−1,…,0Y\_{{i}}=Y\_{{i+1}}+f(i,X\_{i},Y\_{i},Z\_{i})\Delta t-Z\_{i}\Delta W\_{i};\qquad Y\_{N}=g(X\_{N}),\qquad Z\_{N}=0\qquad i=N-1,\ldots,0 |  |

for the implicit approximation of the backward SDE ([1.2](https://arxiv.org/html/2512.24714v1#S1.E2 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")).
By taking the conditional expectation of YiY\_{i} and Yi​Δ​WiY\_{i}\Delta W\_{i} given XiX\_{i} we obtain
the standard explicit scheme

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Yi\displaystyle Y\_{i} | =Y.⁡i+Δ​t​f​(ti,Xi,𝔼​[Yi+1∣Xi],Zi),\displaystyle=\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{i}+\Delta t\,f\!\left(t\_{i},X\_{i},\mathbb{E}[Y\_{i+1}\mid X\_{i}],Z\_{i}\right), |  | (2.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Zi\displaystyle Z\_{i} | =1Δ​t𝔼[Yi+1ΔWi|Xti],\displaystyle=\frac{1}{\Delta t}\,\mathbb{E}\!\left[\,{Y}\_{i+1}\Delta W\_{i}\,\middle|\,X\_{t\_{i}}\,\right], |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Y.⁡i\displaystyle\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{i} | =𝔼[Yi+1|Xi].\displaystyle=\mathbb{E}\!\left[Y\_{i+1}\middle|\,X\_{i}\,\right]. |  | (2.3) |

Provided the conditional expectations can be calculated, at least approximately, we have a recursive numerical method for solving ([1.1](https://arxiv.org/html/2512.24714v1#S1.E1 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"))-([1.2](https://arxiv.org/html/2512.24714v1#S1.E2 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")). The ZZ-component is approximated consistently with the spatial discretization underlying the convolution scheme.

Under standard regularity assumptions on the coefficients of the forward SDE and the driver of the BSDE, the solution admits a Markovian representation. In particular, there exists a deterministic function u:[0,T]×ℝ→ℝu:[0,T]\times\mathbb{R}\to\mathbb{R} such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Yt\displaystyle Y\_{t} | =u​(t,Xt),\displaystyle=u(t,X\_{t}), |  | (2.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Zt\displaystyle Z\_{t} | =σ​(t,Xt)⊤​∇xu​(t,Xt)\displaystyle=\sigma(t,X\_{t})^{\top}\nabla\_{x}u(t,X\_{t}) |  | (2.5) |

t∈[0,T]t\in[0,T], almost surely. The representation ([2.4](https://arxiv.org/html/2512.24714v1#S2.E4 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"))-([2.5](https://arxiv.org/html/2512.24714v1#S2.E5 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) follows from the nonlinear Feynman–Kac formula, see Pardoux and
Peng ([1990](https://arxiv.org/html/2512.24714v1#bib.bib16)), and allows the backward component of the BSDE to be expressed as a function of time and the current value of the forward process.

Conditioning on Xti=xX\_{t\_{i}}=x and denoting Δ​t=ti+1−ti\Delta t=t\_{i+1}-t\_{i}, the conditional expectations appearing in the time–discretized BSDE may be written in integral form as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y.⁡i​(x)=𝔼​[Yti+1∣Xti=x]=∫ℝu​(ti+1,x′)​ϕ​(x′∣ti,x)​𝑑x′,\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{i}(x)=\mathbb{E}\!\left[Y\_{t\_{i+1}}\mid X\_{t\_{i}}=x\right]=\int\_{\mathbb{R}}u(t\_{i+1},x^{\prime})\,\phi(x^{\prime}\mid t\_{i},x)\,dx^{\prime}, |  | (2.6) |

where ϕ(⋅∣ti,x)\phi(\cdot\mid t\_{i},x) denotes the transition density of the forward process Xti+1X\_{t\_{i+1}} conditional on Xti=xX\_{t\_{i}}=x.

For small time increments Δ​t\Delta t, the transition density admits a short–time approximation consistent with the local behavior of the forward diffusion. In particular, conditional on Xti=xX\_{t\_{i}}=x, the density ϕ​(x′∣ti,x)\phi(x^{\prime}\mid t\_{i},x) may be approximated by a Gaussian density of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(x′∣ti,x)≈ϕ​(x′−x∣ti,x)=12​π​σ2​(tn,x)​Δ​t​exp⁡(−(x′−x−η​(ti,x)​Δ​t)22​σ2​(ti,x)​Δ​t),\phi(x^{\prime}\mid t\_{i},x)\approx\phi(x^{\prime}-x\mid t\_{i},x)=\frac{1}{\sqrt{2\pi\sigma^{2}(t\_{n},x)\Delta t}}\exp\!\left(-\frac{\big(x^{\prime}-x-\eta(t\_{i},x)\Delta t\big)^{2}}{2\sigma^{2}(t\_{i},x)\Delta t}\right), |  | (2.7) |

where η​(t,x)\eta(t,x) and σ​(t,x)\sigma(t,x) are the drift and diffusion coefficients of the forward SDE.
Such short–time Gaussian approximations of the transition density are standard for diffusion processes and are consistent with Euler–Maruyama discretization; see, for example, Risken ([1996](https://arxiv.org/html/2512.24714v1#bib.bib17)) or classical results on transition densities of SDEs.

Substituting ([2.7](https://arxiv.org/html/2512.24714v1#S2.E7 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) into ([2.6](https://arxiv.org/html/2512.24714v1#S2.E6 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), the conditional expectation can be written in convolution form,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y.⁡i(x)=𝔼[Yti+1∣Xti=x]≈∫ℝu(ti+1,x′)ϕ(x′−x∣ti,x)dx′=(u(ti+1,⋅)∗ϕ(⋅∣ti,x))(x),\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{i}(x)=\mathbb{E}\!\left[Y\_{t\_{i+1}}\mid X\_{t\_{i}}=x\right]\approx\int\_{\mathbb{R}}u(t\_{i+1},x^{\prime})\,\phi(x^{\prime}-x\mid t\_{i},x)\,dx^{\prime}=\big(u(t\_{i+1},\cdot)\*\phi(\cdot\mid t\_{i},x)\big)(x), |  | (2.8) |

where ∗\* denotes convolution with respect to the spatial variable.

This short–time convolution representation provides the basis for the numerical scheme developed below. In practice, the convolution integral is evaluated on a truncated spatial domain and discretized using FFT-based techniques, leading to an efficient approximation of the conditional expectations appearing in the BSDE time–stepping scheme.

A similar integral representation is available for the conditional expectation appearing in the standard discrete approximation of the ZZ–component. In particular, for the Euler-type scheme

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi(x)=1Δ​t𝔼[Yi+1ΔWi|Xti=x],Z\_{i}(x)=\frac{1}{\Delta t}\,\mathbb{E}\!\left[\,Y\_{i+1}\Delta W\_{i}\,\middle|\,X\_{t\_{i}}=x\,\right], |  | (2.9) |

we may write, conditioning on Xti=xX\_{t\_{i}}=x and using the Markovian representation Yi+1=u​(ti+1,Xti+1)Y\_{i+1}=u(t\_{i+1},X\_{t\_{i+1}}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[Yi+1ΔWi|Xti=x]=∫ℝu(ti+1,x′)𝔼[ΔWi|Xti+1=x′,Xti=x]ϕ(x′∣ti,x)dx′,\mathbb{E}\!\left[\,Y\_{i+1}\Delta W\_{i}\,\middle|\,X\_{t\_{i}}=x\,\right]=\int\_{\mathbb{R}}u(t\_{i+1},x^{\prime})\,\mathbb{E}\!\left[\,\Delta W\_{i}\,\middle|\,X\_{t\_{i+1}}=x^{\prime},\,X\_{t\_{i}}=x\,\right]\,\phi(x^{\prime}\mid t\_{i},x)\,dx^{\prime}, |  | (2.10) |

where ϕ(⋅∣ti,x)\phi(\cdot\mid t\_{i},x) denotes the transition density of Xti+1X\_{t\_{i+1}} conditional on Xti=xX\_{t\_{i}}=x.

Under the short–time Euler approximation of the forward diffusion,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xti+1≈x+η​(ti,x)​Δ​t+σ​(ti,x)​Δ​Wi,X\_{t\_{i+1}}\approx x+\eta(t\_{i},x)\Delta t+\sigma(t\_{i},x)\Delta W\_{i}, |  | (2.11) |

we have the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Wi≈Xti+1−x−η​(ti,x)​Δ​tσ​(ti,x).\Delta W\_{i}\approx\frac{X\_{t\_{i+1}}-x-\eta(t\_{i},x)\Delta t}{\sigma(t\_{i},x)}. |  | (2.12) |

Substituting ([2.12](https://arxiv.org/html/2512.24714v1#S2.E12 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) into ([2.10](https://arxiv.org/html/2512.24714v1#S2.E10 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) and using the corresponding short–time approximation ϕ​(x′∣ti,x)≈ϕ​(x′−x∣ti,x)\phi(x^{\prime}\mid t\_{i},x)\approx\phi(x^{\prime}-x\mid t\_{i},x) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[Yi+1ΔWi|Xti=x]≈1σ​(ti,x)∫ℝu(ti+1,x′)(x′−x−η(ti,x)Δt)ϕ(x′−x∣ti,x)dx′.\mathbb{E}\!\left[\,Y\_{i+1}\Delta W\_{i}\,\middle|\,X\_{t\_{i}}=x\,\right]\approx\frac{1}{\sigma(t\_{i},x)}\int\_{\mathbb{R}}u(t\_{i+1},x^{\prime})\,\big(x^{\prime}-x-\eta(t\_{i},x)\Delta t\big)\,\phi(x^{\prime}-x\mid t\_{i},x)\,dx^{\prime}. |  | (2.13) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi​(x)≈1Δ​t​σ​(ti,x)​∫ℝu​(ti+1,x′)​(x′−x−η​(ti,x)​Δ​t)​ϕ​(x′−x∣ti,x)​𝑑x′.Z\_{i}(x)\approx\frac{1}{\Delta t\,\sigma(t\_{i},x)}\int\_{\mathbb{R}}u(t\_{i+1},x^{\prime})\,\big(x^{\prime}-x-\eta(t\_{i},x)\Delta t\big)\,\phi(x^{\prime}-x\mid t\_{i},x)\,dx^{\prime}. |  | (2.14) |

Defining the kernel

|  |  |  |
| --- | --- | --- |
|  | κi​(z;x):=z−η​(ti,x)​Δ​tΔ​t​σ​(ti,x)​ϕ​(z∣ti,x),z∈ℝ,\kappa\_{i}(z;x):=\frac{z-\eta(t\_{i},x)\Delta t}{\Delta t\,\sigma(t\_{i},x)}\,\phi(z\mid t\_{i},x),\qquad z\in\mathbb{R}, |  |

the approximation ([2.14](https://arxiv.org/html/2512.24714v1#S2.E14 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) can be written compactly as the convolution

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi​(x)≈(u​(ti+1,⋅)∗κi​(z;⋅))​(x),Z\_{i}(x)\approx\big(u(t\_{i+1},\cdot)\*\kappa\_{i}(z;\cdot)\big)(x), |  | (2.15) |

where ∗\* denotes convolution with respect to the spatial variable.

The convolution representations derived above provide a convenient framework for numerical approximation. In particular, convolution integrals can be evaluated efficiently in the Fourier domain using the convolution theorem, which transforms convolutions in physical space into pointwise products in frequency space. At the continuous level, this amounts to applying the Fourier transform to the convolution kernels and the functions being convolved, followed by inversion of the transform to recover the approximations in physical space. Further details can be found in Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)) and Oyono Ngou and
Hyndman ([2022](https://arxiv.org/html/2512.24714v1#bib.bib15)).

In practice, the spatial domain must be truncated and the resulting integrals discretized. The numerical evaluation of these Fourier-domain expressions is carried out using discrete Fourier transforms and fast Fourier transform (FFT) algorithms. Since truncation, discretization, and boundary effects play a crucial role in the stability and accuracy of the method, we defer the detailed discussion of Fourier discretization, damping and shifting techniques, and FFT-based implementation to the next section.

## 3 Boundary control schemes

This section develops boundary-control modifications for the convolution-based FBSDE scheme. We first motivate damping and shifting transformations that reduce truncation and periodic-extension artifacts, then derive the corresponding Fourier-domain representations and present an FFT-based implementation together with error estimates.

### 3.1 Boundary effects and damping–shifting strategy

In practice, the Fourier transform is applied on a truncated spatial domain. While truncation allows the transform to be computed numerically, it also introduces boundary effects due to the implicit periodic extension associated with Fourier-based methods. If not properly controlled, these boundary effects can lead to large numerical errors and instability in the resulting approximations.

Convergence results for Euler discretizations of BSDEs are available under suitable regularity conditions. For example, Zhang ([2004](https://arxiv.org/html/2512.24714v1#bib.bib20)) show that, for a partition scheme Δ\Delta, the approximation error satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|Y​(X)−Y​(XΔ)|2≤C​(1+|x|2)​|Δ|,\mathbb{E}\left|Y(X)-Y(X^{\Delta})\right|^{2}\leq C\left(1+\left|x\right|^{2}\right)\left|\Delta\right|, |  |

provided the target function satisfies an appropriate Lipschitz condition. However, in option pricing problems, terminal payoff functions are typically non-Lipschitz and unbounded, and additional modifications are required to ensure numerical stability.

To address the lack of integrability, Carr and
Madan ([1999](https://arxiv.org/html/2512.24714v1#bib.bib5)) introduced an exponential damping factor to enforce decay of the target function prior to applying the Fourier transform. Related damping ideas have been adopted in Lord and
Kahl ([2006](https://arxiv.org/html/2512.24714v1#bib.bib13)) and Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)), where negative damping parameters are used to improve stability. While damping ensures integrability, truncation alone does not eliminate boundary artifacts. In particular, the implicit periodic extension induced by the Fourier transform may still generate significant errors near the boundaries of the computational domain.

To mitigate these effects, Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)) proposed a linear shifting function to enforce periodicity of the target function prior to applying the Fourier transform. However, linear shifting may itself introduce large boundary errors when applied to option payoff functions. This motivates the use of a shifting function adapted to the structure of the terminal condition.

In this work, we combine exponential damping with an exponential shifting function tailored to option pricing payoffs. Specifically, we introduce a modified target function

|  |  |  |  |
| --- | --- | --- | --- |
|  | u~​(x)=eα​x​(u​(x)−h​(x)),\tilde{u}(x)=e^{\alpha x}\big(u(x)-h(x)\big), |  | (3.1) |

where α<0\alpha<0 is a damping parameter and h​(x)=A​ex+Bh(x)=Ae^{x}+B is chosen so that the modified function u~\tilde{u} satisfies the periodicity conditions

|  |  |  |
| --- | --- | --- |
|  | u~​(x0)=u~​(xN),d​u~d​x​(x0)=d​u~d​x​(xN),\tilde{u}(x\_{0})=\tilde{u}(x\_{N}),\qquad\frac{d\tilde{u}}{dx}(x\_{0})=\frac{d\tilde{u}}{dx}(x\_{N}), |  |

on the truncated spatial interval [x0,xN][x\_{0},x\_{N}]. This construction significantly reduces boundary-induced errors and improves numerical stability.

With this damped and shifted formulation, the convolution representations derived in Section 2 can be evaluated efficiently in the Fourier domain using the convolution theorem. At the continuous level, this leads to Fourier-domain expressions for the approximations of the YY- and ZZ-components, which can subsequently be inverted to recover the solutions in physical space. The precise Fourier transform definitions, damping and shifting in frequency space, and discrete FFT-based implementation are presented in the following subsections.

### 3.2 Fourier-domain representation of the damped–shifted scheme

With the damped and shifted formulation introduced in Section [3.1](https://arxiv.org/html/2512.24714v1#S3.SS1 "3.1 Boundary effects and damping–shifting strategy ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), the convolution updates for the backward components can be expressed conveniently in the Fourier domain. At the continuous level, convolution in physical space corresponds to pointwise multiplication in frequency space, and the original target functions can be recovered by applying the inverse Fourier transform.

Under the short-time Gaussian approximation over a single step Δ​t\Delta t, the forward increment satisfies

|  |  |  |
| --- | --- | --- |
|  | Xt+Δ​t−Xt≈η​Δ​t+σ​Δ​Wt,X\_{t+\Delta t}-X\_{t}\approx\eta\,\Delta t+\sigma\,\Delta W\_{t}, |  |

so its characteristic function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(v):=𝔼​[ei​v​(Xt+Δ​t−Xt)∣Xt]=exp⁡(Δ​t​(η​i​v−12​σ2​v2)),\psi(v):=\mathbb{E}\!\left[e^{\mathrm{i}\mkern 1.0muv(X\_{t+\Delta t}-X\_{t})}\mid X\_{t}\right]=\exp\!\left(\Delta t\left(\eta\,\mathrm{i}\mkern 1.0muv-\tfrac{1}{2}\sigma^{2}v^{2}\right)\right), |  | (3.2) |

with derivative ψ′​(v)=Δ​t​(η​i−σ2​v)​ψ​(v)\psi^{\prime}(v)=\Delta t(\eta\,\mathrm{i}\mkern 1.0mu-\sigma^{2}v)\psi(v).
In the damped formulation ([3.1](https://arxiv.org/html/2512.24714v1#S3.E1 "In 3.1 Boundary effects and damping–shifting strategy ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), the Fourier multipliers corresponding to the YY- and ZZ-updates are evaluated at complex-shifted frequencies.

We first consider the update for the YY–component. Applyin the damping and shifting transformation ([3.1](https://arxiv.org/html/2512.24714v1#S3.E1 "In 3.1 Boundary effects and damping–shifting strategy ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) to ([2.8](https://arxiv.org/html/2512.24714v1#S2.E8 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), taking the Fourier transform, applying the convolution theorem, inverting the Fourier transform, then inverting the damping and shifting gives that the approximation Y.⁡t\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{t} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y.⁡t​(x)=\displaystyle\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{t}(x)={} | 𝔉−1​[𝔉​[Yt+1]​(v)​Ψy​(v)]​(x)\displaystyle\mathfrak{F}^{-1}\!\left[\mathfrak{F}\!\left[Y\_{t+1}\right](v)\,\Psi\_{y}(v)\right](x) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle={} | e−α​x​𝔉−1​[𝔉​[Y~t+1(α)]​(v)​Ψy​(v)]​(x)+A​𝔼​[eXt+1∣Xt=x]+B\displaystyle e^{-\alpha x}\,\mathfrak{F}^{-1}\!\left[\mathfrak{F}\!\left[\tilde{Y}\_{t+1}^{(\alpha)}\right](v)\,\Psi\_{y}(v)\right](x)+A\,\mathbb{E}\!\left[e^{X\_{t+1}}\mid X\_{t}=x\right]+B |  | (3.3) |

where we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψy​(v):=ψ​(v+α​i),\Psi\_{y}(v):=\psi(v+\alpha\mathrm{i}\mkern 1.0mu), |  | (3.4) |

for the fixed damping parameter α<0\alpha<0.
Under the short–time Gaussian approximation of the forward process ([2.11](https://arxiv.org/html/2512.24714v1#S2.E11 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), the conditional expectation in ([3.3](https://arxiv.org/html/2512.24714v1#S3.E3 "In 3.2 Fourier-domain representation of the damped–shifted scheme ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) can be evaluated explicitly, yielding

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y.⁡t​(x)=e−α​x​𝔉−1​[𝔉​[Y~t+1(α)]​(v)​Ψy​(v)]​(x)+A​ex​ψ​(−i)+B.\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{t}(x)=e^{-\alpha x}\,\mathfrak{F}^{-1}\!\left[\mathfrak{F}\!\left[\tilde{Y}\_{t+1}^{(\alpha)}\right](v)\,\Psi\_{y}(v)\right](x)+Ae^{x}\psi(-\mathrm{i}\mkern 1.0mu)+B. |  | (3.5) |

The explicit recovery terms associated with the exponential shift h​(x)=A​ex+Bh(x)=Ae^{x}+B are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y..⁡​(x):=ex​ψ​(−i),Z..⁡​(x):=−η​Δ​t​ex​ψ​(−i)+i​ex​ψ′​(−i)σ​Δ​t.\overset{\,{}\_{\mbox{\Large..}}}{Y}(x):=e^{x}\psi(-\mathrm{i}\mkern 1.0mu),\qquad\overset{\,{}\_{\mbox{\Large..}}}{Z}(x):=-\,\frac{\eta\,\Delta t\,e^{x}\psi(-\mathrm{i}\mkern 1.0mu)+\mathrm{i}\mkern 1.0mu\,e^{x}\psi^{\prime}(-\mathrm{i}\mkern 1.0mu)}{\sigma\,\Delta t}. |  | (3.6) |

These recovery terms can be precomputed on the spatial grid.

A similar representation holds for the ZZ–component. Applying the damping and shifting transformation ([3.1](https://arxiv.org/html/2512.24714v1#S3.E1 "In 3.1 Boundary effects and damping–shifting strategy ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) to the approximation ([2.15](https://arxiv.org/html/2512.24714v1#S2.E15 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) for ZtZ\_{t}, taking the Fourier transform, applying the convolution theorem, inverting the Fourier transform and inverting the damping and shifting, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt​(x)=\displaystyle Z\_{t}(x)={} | 𝔉−1​[𝔉​[Yt+1]​(v)​Ψz​(v)]​(x)\displaystyle\mathfrak{F}^{-1}\!\left[\mathfrak{F}\!\left[Y\_{t+1}\right](v)\,\Psi\_{z}(v)\right](x) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle={} | e−α​x​𝔉−1​[𝔉​[Y~t+1(α)]​(v)​Ψz​(v)]​(x)+AΔ​t​𝔼​[eXt+1​Δ​Wt∣Xt=x]\displaystyle e^{-\alpha x}\,\mathfrak{F}^{-1}\!\left[\mathfrak{F}\!\left[\tilde{Y}\_{t+1}^{(\alpha)}\right](v)\,\Psi\_{z}(v)\right](x)+\frac{A}{\Delta t}\,\mathbb{E}\!\left[e^{X\_{t+1}}\Delta W\_{t}\mid X\_{t}=x\right] |  | (3.7) |

where we define

|  |  |  |
| --- | --- | --- |
|  | Ψz​(v):=σ​(i​v−α)​ψ​(v+α​i).\Psi\_{z}(v):=\sigma(\mathrm{i}\mkern 1.0muv-\alpha)\,\psi(v+\alpha\mathrm{i}\mkern 1.0mu). |  |

Evaluating the conditional expectation using the short–time approximation of the forward increment ([2.11](https://arxiv.org/html/2512.24714v1#S2.E11 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt​(x)=e−α​x​𝔉−1​[𝔉​[Y~t+1(α)]​(v)​Ψz​(v)]​(x)−A​(η​Δ​t​ex​ψ​(−i)+i​ex​ψ′​(−i)σ​Δ​t).Z\_{t}(x)=e^{-\alpha x}\,\mathfrak{F}^{-1}\!\left[\mathfrak{F}\!\left[\tilde{Y}\_{t+1}^{(\alpha)}\right](v)\,\Psi\_{z}(v)\right](x)-A\,\left(\frac{\eta\,\Delta t\,e^{x}\psi(-\mathrm{i}\mkern 1.0mu)+\mathrm{i}\mkern 1.0mu\,e^{x}\psi^{\prime}(-\mathrm{i}\mkern 1.0mu)}{\sigma\,\Delta t}\right). |  | (3.8) |

Here,

|  |  |  |
| --- | --- | --- |
|  | ψ​(v)=exp⁡(Δ​t​(η​i​v−12​σ2​v2))\psi(v)=\exp\!\left(\Delta t\left(\eta\,\mathrm{i}\mkern 1.0muv-\tfrac{1}{2}\sigma^{2}v^{2}\right)\right) |  |

denotes the characteristic function associated with the short–time Gaussian approximation of the forward increment, and

|  |  |  |
| --- | --- | --- |
|  | ψ′​(v)=Δ​t​(η​i−σ2​v)​ψ​(v)\psi^{\prime}(v)=\Delta t\left(\eta\,\mathrm{i}\mkern 1.0mu-\sigma^{2}v\right)\psi(v) |  |

is its first derivative with respect to vv.

### 3.3 Discrete Fourier implementation

We now describe the discrete Fourier implementation of the damped–shifted convolution scheme. All Fourier-domain formulas in Section [3.2](https://arxiv.org/html/2512.24714v1#S3.SS2 "3.2 Fourier-domain representation of the damped–shifted scheme ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") are evaluated numerically on a truncated spatial grid and the corresponding frequency grid. Let the truncation interval be [x0,xN][x\_{0},x\_{N}] with length L=xN−x0L=x\_{N}-x\_{0}, and define the uniform spatial grid

|  |  |  |
| --- | --- | --- |
|  | xn=x0+n​Δ​x,n=0,1,…,N−1,Δ​x=LN.x\_{n}=x\_{0}+n\Delta x,\qquad n=0,1,\dots,N-1,\qquad\Delta x=\frac{L}{N}. |  |

The associated frequency grid is

|  |  |  |
| --- | --- | --- |
|  | vk=(k−N2)​Δ​v,k=0,1,…,N−1,Δ​v=2​πL,v\_{k}=\left(k-\frac{N}{2}\right)\Delta v,\qquad k=0,1,\dots,N-1,\qquad\Delta v=\frac{2\pi}{L}, |  |

so that the Nyquist relation Δ​x​Δ​v=2​π/N\Delta x\,\Delta v=2\pi/N holds.

For a grid function {fn}n=0N−1\{f\_{n}\}\_{n=0}^{N-1}, we write 𝔇​[f]​(vk)\mathfrak{D}[f](v\_{k}) for its discrete Fourier transform and 𝔇−1\mathfrak{D}^{-1} for the inverse transform, defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔇​[f]​(vk)\displaystyle\mathfrak{D}[f](v\_{k}) | :=∑n=0N−1fn​e−i​vk​xn,\displaystyle:=\sum\_{n=0}^{N-1}f\_{n}\,e^{-\mathrm{i}\mkern 1.0muv\_{k}x\_{n}}, |  | (3.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔇−1​[F]​(xn)\displaystyle\mathfrak{D}^{-1}[F](x\_{n}) | :=1N​∑k=0N−1F​(vk)​ei​vk​xn.\displaystyle:=\frac{1}{N}\sum\_{k=0}^{N-1}F(v\_{k})\,e^{\mathrm{i}\mkern 1.0muv\_{k}x\_{n}}. |  | (3.10) |

In order to work with a frequency grid centered at zero, we use the standard phase-shift identity

|  |  |  |
| --- | --- | --- |
|  | e±i​vk​xn=(−1)n+k​e±i​(k​Δ​v)​(n​Δ​x),e^{\pm\mathrm{i}\mkern 1.0muv\_{k}x\_{n}}=(-1)^{n+k}\,e^{\pm\mathrm{i}\mkern 1.0mu(k\Delta v)(n\Delta x)}, |  |

which results in the (−1)n(-1)^{n} factors appearing in the FFT-ready formulas below. In practice, this centering is implemented by multiplying the input and output grid vectors componentwise by (−1)n(-1)^{n}.

We summarize the resulting FFT-based backward iteration with boundary control in Algorithm [1](https://arxiv.org/html/2512.24714v1#alg1 "Algorithm 1 ‣ 3.3 Discrete Fourier implementation ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"). The shifting parameters (A,B)(A,B) are updated at each time step to enforce periodicity of the modified function u~\tilde{u}, while the damping parameter α\alpha is fixed throughout. This choice reduces computational overhead and avoids the stability issues that can arise when α\alpha is updated adaptively.

Algorithm 1  Convolution–FFT scheme for the FBSDE system with damping and shifting

Truncation length LL, grid size NN, time grid {tk}k=0n\{t\_{k}\}\_{k=0}^{n} with Δ​t=T/n\Delta t=T/n, damping parameter α<0\alpha<0 (fixed),
payoff/terminal function gg, driver ff, model parameters (η,σ)(\eta,\sigma).

2:Approximations {\mathaccentV​b​a​r​0​\symboldoperators​16​YkΔ​(xi),\mathaccentV​b​a​r​0​\symboldoperators​16​ZkΔ​(xi)}\{\mathaccentV{bar}0\symboldoperators 16Y\_{k}^{\Delta}(x\_{i}),\mathaccentV{bar}0\symboldoperators 16Z\_{k}^{\Delta}(x\_{i})\} on the spatial grid.

Set Δ​x←L/N\Delta x\leftarrow L/N, Δ​v←2​π/L\Delta v\leftarrow 2\pi/L

4:Define spatial grid xi←x0+i​Δ​xx\_{i}\leftarrow x\_{0}+i\Delta x, i=0,…,N−1i=0,\dots,N-1

Define frequency grid vj←(j−N2)​Δ​vv\_{j}\leftarrow(j-\frac{N}{2})\Delta v, j=0,…,N−1j=0,\dots,N-1

6:Initialize terminal values: Yn,iΔ←g​(xi)Y\_{n,i}^{\Delta}\leftarrow g(x\_{i}) for i=0,…,N−1i=0,\dots,N-1

Initialize Zn,iΔZ\_{n,i}^{\Delta} (e.g. regression/finite-difference/analytic if available) for i=0,…,N−1i=0,\dots,N-1

8:Precompute Fourier multipliers for all j=0,…,N−1j=0,\dots,N-1:

|  |  |  |
| --- | --- | --- |
|  | Ψy​(vj)←ψ​(vj+α​i),Ψz​(vj)←σ​(i​vj−α)​ψ​(vj+α​i)\Psi\_{y}(v\_{j})\leftarrow\psi(v\_{j}+\alpha\mathrm{i}\mkern 1.0mu),\qquad\Psi\_{z}(v\_{j})\leftarrow\sigma(\mathrm{i}\mkern 1.0muv\_{j}-\alpha)\psi(v\_{j}+\alpha\mathrm{i}\mkern 1.0mu) |  |

Precompute recovery terms on the grid:

|  |  |  |
| --- | --- | --- |
|  | Y..⁡​(xi)←exi​ψ​(−i),Z..⁡​(xi)←−η​Δ​t​exi​ψ​(−i)+i​exi​ψ′​(−i)σ​Δ​t\overset{\,{}\_{\mbox{\Large..}}}{Y}(x\_{i})\leftarrow e^{x\_{i}}\psi(-\mathrm{i}\mkern 1.0mu),\qquad\overset{\,{}\_{\mbox{\Large..}}}{Z}(x\_{i})\leftarrow-\frac{\eta\Delta t\,e^{x\_{i}}\psi(-\mathrm{i}\mkern 1.0mu)+\mathrm{i}\mkern 1.0mue^{x\_{i}}\psi^{\prime}(-\mathrm{i}\mkern 1.0mu)}{\sigma\Delta t} |  |

10:for k←n−1,n−2,…,0k\leftarrow n-1,n-2,\dots,0 do

(Shift) Compute boundary slopes (one-sided differences):

|  |  |  |
| --- | --- | --- |
|  | y0′←−3​Yk+1,0Δ+4​Yk+1,1Δ−Yk+1,2Δ2​Δ​x,yN−1′←3​Yk+1,N−1Δ−4​Yk+1,N−2Δ+Yk+1,N−3Δ2​Δ​xy^{\prime}\_{0}\leftarrow\frac{-3Y\_{k+1,0}^{\Delta}+4Y\_{k+1,1}^{\Delta}-Y\_{k+1,2}^{\Delta}}{2\Delta x},\quad y^{\prime}\_{N-1}\leftarrow\frac{3Y\_{k+1,N-1}^{\Delta}-4Y\_{k+1,N-2}^{\Delta}+Y\_{k+1,N-3}^{\Delta}}{2\Delta x} |  |

12:  Solve for shifting parameters A,BA,B (enforcing periodicity of u~\tilde{u} and u~′\tilde{u}^{\prime} on [x0,xN−1][x\_{0},x\_{N-1}])

Form the damped–shifted vector on the grid:

|  |  |  |
| --- | --- | --- |
|  | Y~k+1,i(α)←eα​xi​(Yk+1,iΔ−(A​exi+B)),i=0,…,N−1\tilde{Y}\_{k+1,i}^{(\alpha)}\leftarrow e^{\alpha x\_{i}}\bigl(Y\_{k+1,i}^{\Delta}-(Ae^{x\_{i}}+B)\bigr),\quad i=0,\dots,N-1 |  |

14:  (FFT step) Compute centered DFT/IDFT using the phase factors (−1)i(-1)^{i}:

Y~^←𝔇​(((−1)i​Y~k+1,i(α))i=0N−1)\widehat{\tilde{Y}}\leftarrow\mathfrak{D}\bigl(((-1)^{i}\tilde{Y}\_{k+1,i}^{(\alpha)})\_{i=0}^{N-1}\bigr)

16:   Y.⁡^←Y~^⊙Ψy\widehat{\overset{\,{}\_{\mbox{\Large.}}}{Y}}\leftarrow\widehat{\tilde{Y}}\odot\Psi\_{y} ⊳\triangleright pointwise product

Z.⁡^←Y~^⊙Ψz\widehat{\overset{\,{}\_{\mbox{\Large.}}}{Z}}\leftarrow\widehat{\tilde{Y}}\odot\Psi\_{z}

18:   Y.⁡kΔ←((−1)i​𝔇−1​(Y.⁡^))i=0N−1\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{k}^{\Delta}\leftarrow((-1)^{i}\,\mathfrak{D}^{-1}(\widehat{\overset{\,{}\_{\mbox{\Large.}}}{Y}}))\_{i=0}^{N-1}

Z.⁡kΔ←((−1)i​𝔇−1​(Z.⁡^))i=0N−1\overset{\,{}\_{\mbox{\Large.}}}{Z}\_{k}^{\Delta}\leftarrow((-1)^{i}\,\mathfrak{D}^{-1}(\widehat{\overset{\,{}\_{\mbox{\Large.}}}{Z}}))\_{i=0}^{N-1}

20:  (Undamp/unshift) Recover (Y^kΔ,\mathaccentV​b​a​r​0​\symboldoperators​16​ZkΔ)(\hat{Y}\_{k}^{\Delta},\mathaccentV{bar}0\symboldoperators 16Z\_{k}^{\Delta}) on the grid:

|  |  |  |
| --- | --- | --- |
|  | Y^k,iΔ←e−α​xi​Y.⁡k,iΔ+A​Y..⁡​(xi)+B,\mathaccentV​b​a​r​0​\symboldoperators​16​Zk,iΔ←e−α​xi​Z.⁡k,iΔ+A​Z..⁡​(xi)\hat{Y}\_{k,i}^{\Delta}\leftarrow e^{-\alpha x\_{i}}\overset{\,{}\_{\mbox{\Large.}}}{Y}\_{k,i}^{\Delta}+A\,\overset{\,{}\_{\mbox{\Large..}}}{Y}(x\_{i})+B,\qquad\mathaccentV{bar}0\symboldoperators 16Z\_{k,i}^{\Delta}\leftarrow e^{-\alpha x\_{i}}\overset{\,{}\_{\mbox{\Large.}}}{Z}\_{k,i}^{\Delta}+A\,\overset{\,{}\_{\mbox{\Large..}}}{Z}(x\_{i}) |  |

(Driver update) Explicit Euler step for YY:

|  |  |  |
| --- | --- | --- |
|  | \mathaccentV​b​a​r​0​\symboldoperators​16​Yk,iΔ←Y^k,iΔ+f​(Xk,iΔ,Y^k,iΔ,\mathaccentV​b​a​r​0​\symboldoperators​16​Zk,iΔ)​Δ​t\mathaccentV{bar}0\symboldoperators 16Y\_{k,i}^{\Delta}\leftarrow\hat{Y}\_{k,i}^{\Delta}+f(X\_{k,i}^{\Delta},\hat{Y}\_{k,i}^{\Delta},\mathaccentV{bar}0\symboldoperators 16Z\_{k,i}^{\Delta})\Delta t |  |

22:  Optional constraint (e.g. call payoff): \mathaccentV​b​a​r​0​\symboldoperators​16​Yk,iΔ←max⁡(\mathaccentV​b​a​r​0​\symboldoperators​16​Yk,iΔ,0)\mathaccentV{bar}0\symboldoperators 16Y\_{k,i}^{\Delta}\leftarrow\max(\mathaccentV{bar}0\symboldoperators 16Y\_{k,i}^{\Delta},0)

Set Yk,iΔ←\mathaccentV​b​a​r​0​\symboldoperators​16​Yk,iΔY\_{k,i}^{\Delta}\leftarrow\mathaccentV{bar}0\symboldoperators 16Y\_{k,i}^{\Delta}, Zk,iΔ←\mathaccentV​b​a​r​0​\symboldoperators​16​Zk,iΔZ\_{k,i}^{\Delta}\leftarrow\mathaccentV{bar}0\symboldoperators 16Z\_{k,i}^{\Delta} for all ii

24:end for

return {\mathaccentV​b​a​r​0​\symboldoperators​16​YkΔ​(xi),\mathaccentV​b​a​r​0​\symboldoperators​16​ZkΔ​(xi)}\{\mathaccentV{bar}0\symboldoperators 16Y\_{k}^{\Delta}(x\_{i}),\mathaccentV{bar}0\symboldoperators 16Z\_{k}^{\Delta}(x\_{i})\}

In Algorithm [1](https://arxiv.org/html/2512.24714v1#alg1 "Algorithm 1 ‣ 3.3 Discrete Fourier implementation ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), we fix the damping parameter and only update the shifting parameter at every time step which gives fast and efficient calculation. Comparing the results to those obtained using the convolution algorithm given by Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)), where both the shifting and the damping parameters are adaptively updated at every time step, we find that the changes embodied in Algorithm [1](https://arxiv.org/html/2512.24714v1#alg1 "Algorithm 1 ‣ 3.3 Discrete Fourier implementation ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") increase stability.

### 3.4 Error analysis

We denote the convolution estimation for u​(xn)=𝔼​[Y|Xtn=xn]u(x\_{n})=\mathbb{E}\left[Y\left|X\_{t\_{n}}=x\_{n}\right.\right]

|  |  |  |
| --- | --- | --- |
|  | \mathaccentV​b​a​r​0​\symboldoperators​16​u​(xn)≔(−1)n​𝔇−1​[{𝔇​[{wn​(−1)n​YiΔ}i=0N−1]​(vj)​Ψ​(vj)}j=0N−1]n.\mathaccentV{bar}0\symboldoperators 16u(x\_{n})\coloneqq(-1)^{n}\mathfrak{D}^{-1}\left[\left\{\mathfrak{D}\left[\left\{w\_{n}(-1)^{n}Y^{\Delta}\_{i}\right\}\_{i=0}^{N-1}\right](v\_{j})\Psi\left(v\_{j}\right)\right\}\_{j=0}^{N-1}\right]\_{n}. |  |

Following Proposition 2.1 of Gao and
Hyndman ([2025](https://arxiv.org/html/2512.24714v1#bib.bib8)) and the fact that the characteristic function of Gaussian density decays as exp⁡(−12​Σ​x2)\exp\left(-\frac{1}{2}\Sigma x^{2}\right), we obtain the following lemma.

###### Lemma 3.1 (Error of the convolution method).

Assuming the integrable function f​(x)f(x) is bounded by \mathaccentV​b​a​r​0​\symboldoperators​16​f\mathaccentV{bar}0\symboldoperators 16f on [−L2,L2][-\frac{L}{2},\frac{L}{2}] and admits the Fourier expansion

|  |  |  |
| --- | --- | --- |
|  | f​(x)=∑j=−∞∞Fj​e−i​j​2​π​xL,f(x)=\sum\_{j=-\infty}^{\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}, |  |

with coefficients defined by

|  |  |  |
| --- | --- | --- |
|  | Fj=1L​∫−L2L2f​(x)​ei​j​2​π​xL​𝑑x.F\_{j}=\frac{1}{L}\int\_{-\frac{L}{2}}^{\frac{L}{2}}f(x)e^{\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}dx. |  |

Suppose the discrete Fourier coefficient

|  |  |  |
| --- | --- | --- |
|  | \mathaccentV​b​a​r​0​\symboldoperators​16​Fj=Δ​xL​∑k=0N−1f​(xk)​ei​j​2​π​xkL,\mathaccentV{bar}0\symboldoperators 16{F}\_{j}=\frac{\Delta x}{L}\sum\_{k=0}^{N-1}f(x\_{k})e^{\mathrm{i}\mkern 1.0muj\frac{2\pi x\_{k}}{L}}, |  |

has bounded error |Fj−\mathaccentV​b​a​r​0​\symboldoperators​16​Fj|≤ϵL​N−m\left|F\_{j}-\mathaccentV{bar}0\symboldoperators 16F\_{j}\right|\leq\epsilon\_{L}N^{-m} for m≥2m\geq 2 and some constant ϵL>0\epsilon\_{L}>0. Then the convolution method has an estimation error bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ey|≔|u−\mathaccentV​b​a​r​0​\symboldoperators​16​u|≤CL​(\mathaccentV​b​a​r​0​\symboldoperators​16​f​(1−erf​(σ​(N−2)​πL​Δ​t2))+ϵ​L​N−m),\left|e\_{y}\right|\coloneqq\left|u-\mathaccentV{bar}0\symboldoperators 16u\right|\leq C\_{L}\left(\mathaccentV{bar}0\symboldoperators 16f\left(1-\mathrm{erf}\left(\frac{\sigma\left(N-2\right)\pi}{L}\sqrt{\frac{\Delta t}{2}}\right)\right)+\epsilon LN^{-m}\right), |  | (3.11) |

for some constant ϵ>0\epsilon>0 depending on LL and CL=Lσ​2​π​Δ​tC\_{L}=\frac{L}{\sigma\sqrt{2\pi\Delta t}} on the truncation regions [−L2,L2][-\frac{L}{2},\frac{L}{2}] with discretization Δ=(Δ​t,Δ​x,Δ​v)\Delta=(\Delta t,\Delta x,\Delta v). The error function erf​(x)\mathrm{erf}(x) is defined as

|  |  |  |
| --- | --- | --- |
|  | erf​(x)≔2π​∫0xe−u2​𝑑u.\mathrm{erf}(x)\coloneqq\frac{2}{\sqrt{\pi}}\int\_{0}^{x}e^{-u^{2}}du. |  |

###### Remark 3.1 (Boundary problem).

In Lemma [3.1](https://arxiv.org/html/2512.24714v1#S3.Thmlemma1 "Lemma 3.1 (Error of the convolution method). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), we use the bound \mathaccentV​b​a​r​0​\symboldoperators​16​f\mathaccentV{bar}0\symboldoperators 16f to estimate the Fourier coefficients as the target function may be unbounded with increasing derivatives. The terminal function used in option pricing is a such function that is not in the Schwartz space of all functions whose derivatives are rapidly decreasing. The rapidly increasing derivatives of the log-underlying makes its Fourier coefficient |Fj|\left|F\_{j}\right| increase as x→∞x\rightarrow\infty. To analyze the Fourier transform of such target function, the bound \mathaccentV​b​a​r​0​\symboldoperators​16​f\mathaccentV{bar}0\symboldoperators 16f could heavily influence the local error in addition to the truncation factor LL and the discretization factor Δ\Delta. Similar to Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)) we will prove local and global error estimates, stability and convergence criteria, and illustrate boundary problem numerically in the application section.

Lemma [3.1](https://arxiv.org/html/2512.24714v1#S3.Thmlemma1 "Lemma 3.1 (Error of the convolution method). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") provides a general error estimate for the convolution method, and as we can see from ([3.11](https://arxiv.org/html/2512.24714v1#S3.E11 "In Lemma 3.1 (Error of the convolution method). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) that if the target function is unbounded at one side, the value of \mathaccentV​b​a​r​0​\symboldoperators​16​f\mathaccentV{bar}0\symboldoperators 16f can be large and the convolution method yields poor approximation results at boundaries. This result can be viewed from the numerical results provided by Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)). In the convolution method proposed by Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)), a linear function was applied to modify the target function, which provides reliable accuracy in the center area of the truncation region but does not improve performance on boundaries. That is, the error on the boundaries are becoming unbounded since the target function itself is an exponential-type function and the linear function is not compatible to shift it as a bounded function. Considering that the shifted function yields smoothly connected boundaries, we could find a smaller f^<\mathaccentV​b​a​r​0​\symboldoperators​16​f\hat{f}<\mathaccentV{bar}0\symboldoperators 16f to bound the shifted function f~\tilde{f}. Following Lemma [3.1](https://arxiv.org/html/2512.24714v1#S3.Thmlemma1 "Lemma 3.1 (Error of the convolution method). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") and consider the Fourier transform with damping and shifting schemes, the error estimate is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | |e~y|≤Cα,L​e−α​x​(f^​(1−e​r​f​(σ​(N−2)​πL​Δ​t2))+ϵ​L​N−m),\left|\tilde{e}\_{y}\right|\leq C\_{\alpha,L}e^{-\alpha x}\left(\hat{f}\left(1-erf\left(\frac{\sigma\left(N-2\right)\pi}{L}\sqrt{\frac{\Delta t}{2}}\right)\right)+\epsilon LN^{-m}\right), |  | (3.12) |

for the constant Cα,L=L​e−α​Δ​t​(η−12​σ2​α)σ​2​π​Δ​tC\_{\alpha,L}=\frac{Le^{-\alpha\Delta t\left(\eta-\frac{1}{2}\sigma^{2}\alpha\right)}}{\sigma\sqrt{2\pi\Delta t}} and some value f^≥|f~​(x)|\hat{f}\geq\left|\tilde{f}(x)\right| for all xx. Then, the error for ZZ is bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | |e~z|≤Cα,L​σ​e−α​x|α|​(f^​(1−e​r​f​(σ​(N−2)​πL​Δ​t2))+1σ​|α|​2​π​Δ​t)+𝒪​(e−K​N2L2​Δ​t),\left|\tilde{e}\_{z}\right|\leq C\_{\alpha,L}\frac{\sigma e^{-\alpha x}}{|\alpha|}\left(\hat{f}\left(1-erf\left(\frac{\sigma\left(N-2\right)\pi}{L}\sqrt{\frac{\Delta t}{2}}\right)\right)+\frac{1}{\sigma|\alpha|\sqrt{2\pi\Delta t}}\right)+\mathcal{O}\left(e^{-K\frac{N^{2}}{L^{2}}\Delta t}\right), |  | (3.13) |

for the constant K=σ2​π22K=\frac{\sigma^{2}\pi^{2}}{2}.

###### Remark 3.2 (Error transfer with damping parameter).

From ([3.12](https://arxiv.org/html/2512.24714v1#S3.E12 "In 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) and ([3.13](https://arxiv.org/html/2512.24714v1#S3.E13 "In 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) we observe that the shifting term reduces the truncation error given that f^<\mathaccentV​b​a​r​0​\symboldoperators​16​f\hat{f}<\mathaccentV{bar}0\symboldoperators 16f while the damping term e−α​xe^{-\alpha x} has a side effect which makes the error increase as xx approaches to the right boundary for α<0\alpha<0. The proper shifting function h​(x)h(x) is chosen to be similar to the terminal condition g​(x)g(x) of Yt​(x)Y\_{t}(x). The shifting result gives us a periodic function which yields smaller error estimates than using f^\hat{f} to bound the Fourier coefficients, see Theorem 4.4 of Vretblad ([2003](https://arxiv.org/html/2512.24714v1#bib.bib18)), where the convolution error is of order 𝒪​(N−1)\mathcal{O}\left(N^{-1}\right). We can rewrite ([3.12](https://arxiv.org/html/2512.24714v1#S3.E12 "In 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) and ([3.13](https://arxiv.org/html/2512.24714v1#S3.E13 "In 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |e~y|≤\displaystyle\left|\tilde{e}\_{y}\right|\leq | 𝒪​(N−1),\displaystyle\mathcal{O}\left(N^{-1}\right), |  | (3.14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |e~z|≤\displaystyle\left|\tilde{e}\_{z}\right|\leq | 𝒪​(Δ​t−1)+𝒪​(N−1)+𝒪​(e−K​N2L2​Δ​t).\displaystyle\mathcal{O}\left(\Delta t^{-1}\right)+\mathcal{O}\left(N^{-1}\right)+\mathcal{O}\left(e^{-K\frac{N^{2}}{L^{2}}\Delta t}\right). |  | (3.15) |

By Lemma [3.1](https://arxiv.org/html/2512.24714v1#S3.Thmlemma1 "Lemma 3.1 (Error of the convolution method). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") and the Lipschitz condition of ff, we obtain the local error estimation for the convolution method with the damping and shifting scheme.

###### Lemma 3.2 (Local error of the convolution method with damping and shifting).

Suppose Assumption [2.1](https://arxiv.org/html/2512.24714v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") is satisfied, the damping and the shifting schemes admits the following error estimation on the discretized region Δ=(Δ​t,Δ​x,Δ​v)\Delta=\left(\Delta t,\Delta x,\Delta v\right)

|  |  |  |
| --- | --- | --- |
|  | |Y​(x)−\mathaccentV​b​a​r​0​\symboldoperators​16​YΔ​(x)|≤Cα​e−α​x​(Δ​x+Δ​t),\left|Y(x)-\mathaccentV{bar}0\symboldoperators 16Y^{\Delta}(x)\right|\leq C\_{\alpha}e^{-\alpha x}\left(\Delta x+\sqrt{\Delta t}\right), |  |

for some constant Cα>0C\_{\alpha}>0 depending only on α\alpha.

Let σ​(N−2)​πL​Δ​t2\frac{\sigma\left(N-2\right)\pi}{L}\sqrt{\frac{\Delta t}{2}} be large enough and e​r​f​(σ​(N−2)​πL​Δ​t2)→1erf\left(\frac{\sigma\left(N-2\right)\pi}{L}\sqrt{\frac{\Delta t}{2}}\right)\rightarrow 1 such that the truncation error converges in ([3.11](https://arxiv.org/html/2512.24714v1#S3.E11 "In Lemma 3.1 (Error of the convolution method). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), which yields the following convergence condition.

###### Proposition 3.1 (Stability and convergence).

If the discretization NN and the truncation LL satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | N≥Lσ​2Δ​t,N\geq\frac{L}{\sigma}\sqrt{\frac{2}{\Delta t}}, |  | (3.16) |

then the convolution method is stable and convergent.

Next, we investigate the global error estimation and summarize it by the following Theorem.

###### Theorem 3.1 (Global error bounds).

Suppose f∈ℂ1,2,2,2→ℝf\in\mathbb{C}^{1,2,2,2}\rightarrow\mathbb{R} satisfies Assumption [2.1](https://arxiv.org/html/2512.24714v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") and ([3.16](https://arxiv.org/html/2512.24714v1#S3.E16 "In Proposition 3.1 (Stability and convergence). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) holds Then, the error of the convolution-FFT numerical solution of ([1.1](https://arxiv.org/html/2512.24714v1#S1.E1 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"))-([1.2](https://arxiv.org/html/2512.24714v1#S1.E2 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) on the discretized region Δ=(Δ​t,Δ​x,Δ​v)\Delta=\left(\Delta t,\Delta x,\Delta v\right) is of the form

|  |  |  |
| --- | --- | --- |
|  | err​(Δ)≔max0≤i≤n⁡𝔼​[supti≤t≤ti+1|Yt−\mathaccentV​b​a​r​0​\symboldoperators​16​YtiΔ|]≤𝒪​(Δ​t12)+𝒪​(Δ​t)+𝒪​(Δ​t​Δ​x)+𝒪​(Δ​t​e−K​Δ​tΔ​x2),\mathrm{err}(\Delta)\coloneqq\max\_{0\leq i\leq n}\mathbb{E}\left[\sup\_{t\_{i}\leq t\leq t\_{i+1}}\left|Y\_{t}-\mathaccentV{bar}0\symboldoperators 16Y^{\Delta}\_{t\_{i}}\right|\right]\leq\mathcal{O}\left(\Delta t^{\frac{1}{2}}\right)+\mathcal{O}\left(\Delta t\right)+\mathcal{O}\left(\Delta t\Delta x\right)+\mathcal{O}\left(\Delta te^{-K\frac{\Delta t}{\Delta x^{2}}}\right), |  |

for the constant K=σ2​π22K=\frac{\sigma^{2}\pi^{2}}{2}.

Proof: see Appendix [A.1](https://arxiv.org/html/2512.24714v1#A1.SS1 "A.1 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method").

Theorem [3.1](https://arxiv.org/html/2512.24714v1#S3.Thmtheorem1 "Theorem 3.1 (Global error bounds). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") decomposes the global error into three contributions: time-discretization error of order 𝒪​(Δ​t1/2)+𝒪​(Δ​t)\mathcal{O}(\Delta t^{1/2})+\mathcal{O}(\Delta t), spatial discretization error of order 𝒪​(Δ​t​Δ​x)\mathcal{O}(\Delta t\,\Delta x), and a truncation term of order 𝒪​(Δ​t​exp⁡(−K​Δ​t/Δ​x2))\mathcal{O}\!\left(\Delta t\,\exp{(-K\Delta t/\Delta x^{2})}\right). The boundary-control strategy developed in Section [3.1](https://arxiv.org/html/2512.24714v1#S3.SS1 "3.1 Boundary effects and damping–shifting strategy ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") is designed to prevent the truncation and periodic-extension effects from dominating the numerical solution when the target functions are non-periodic and unbounded on the full line.

Compared with the adaptive damping and shifting strategy in Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)), we fix the damping parameter and update only the shifting parameters at each time step. This avoids step-to-step variation in the damping exponent, which can amplify boundary artifacts in practice. Moreover, the truncation term in Theorem [3.1](https://arxiv.org/html/2512.24714v1#S3.Thmtheorem1 "Theorem 3.1 (Global error bounds). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") decays rapidly as the spatial mesh is refined under the stability condition ([3.16](https://arxiv.org/html/2512.24714v1#S3.E16 "In Proposition 3.1 (Stability and convergence). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), and the numerical experiments in the next section confirm that the resulting scheme achieves improved accuracy on comparable grids.

## 4 Numerical result of option pricing

Suppose the underlying asset StS\_{t} pays constant dividend with constant μ\mu, dd, σ\sigma which is defined as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​exp⁡{(μ−d−12​tr​(σ​σ′))​t+σ​Wt}.{S}\_{t}={S}\_{0}\exp\left\{\left(\mu-d-\frac{1}{2}\text{tr}\left(\sigma\sigma^{\prime}\right)\right)t+\sigma W\_{t}\right\}. |  | (4.1) |

The corresponding logarithm of the stock prices Xt=ln⁡StX\_{t}=\ln S\_{t} is defined in ([1.1](https://arxiv.org/html/2512.24714v1#S1.E1 "In 1 Introduction ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) with ηt=μ−d−12​tr​(σ​σ′)\eta\_{t}=\mu-d-\frac{1}{2}\text{tr}\left(\sigma\sigma^{\prime}\right) and X0=ln⁡S0X\_{0}=\ln S\_{0}. In the market with borrowing rate RtR\_{t}, the driver for the American call option price is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t,x,y,z)=−rt​y−(μt−dt−r)​σt−1​z+(Rt−rt)​(y−tr​(σt−1​z))−.f(t,{x},y,{z})=-r\_{t}y-\left(\mu\_{t}-d\_{t}-r\right){\sigma\_{t}}^{-1}{z}+\left(R\_{t}-r\_{t}\right)\left(y-\text{tr}\left(\sigma\_{t}^{-1}{z}\right)\right)^{-}. |  | (4.2) |

The terminal condition of options in European or American type is

|  |  |  |
| --- | --- | --- |
|  | g​(x)=(ex−K)+.g(x)=\left(e^{x}-K\right)^{+}. |  |

We choose that S0=100S\_{0}=100, K=100K=100, d=0d=0, r=R=0.01r=R=0.01, μ=0.05\mu=0.05, σ=0.2\sigma=0.2, and T=1T=1. In Figure [1](https://arxiv.org/html/2512.24714v1#S4.F1 "Figure 1 ‣ 4 Numerical result of option pricing ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), we replicate the result and the method provided by Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)). We construct the mesh of the spatial variable XX with NN discretized values on X0+[−L2,L2]X\_{0}+[-\frac{L}{2},\frac{L}{2}] and the backward iterations over the time with nn steps for Δ​t=Tn\Delta t=\frac{T}{n}. Since d=0d=0 and R=rR=r, our numerical results specialize to the Black-Scholes European call option price.

Figure 1: Call option price and delta errors - convolution method of Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10))

![Refer to caption](x1.png)



Figure 2: Call option price and delta errors - convolution method with boundary error control.

![Refer to caption](x2.png)

As we can see from Figure [1](https://arxiv.org/html/2512.24714v1#S4.F1 "Figure 1 ‣ 4 Numerical result of option pricing ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") and Figure [2](https://arxiv.org/html/2512.24714v1#S4.F2 "Figure 2 ‣ 4 Numerical result of option pricing ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"), the CFFT–BSDE method with boundary control substantially decreases errors at the boundaries, effectively eliminating boundary error for deeply out-of-the-money (OTM) options. The CFFT–BSDE method with boundary control also provides more stable results compared to Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)) method which has wide range of damped oscillation shown in Figure [1](https://arxiv.org/html/2512.24714v1#S4.F1 "Figure 1 ‣ 4 Numerical result of option pricing ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method"). Table [1](https://arxiv.org/html/2512.24714v1#S4.T1 "Table 1 ‣ 4 Numerical result of option pricing ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") examines the impacts of different parameters on the hedging ratio. We calculate the hedge ratios using Δ=Z/(σ​S)\Delta=Z/(\sigma S) based on ([2.5](https://arxiv.org/html/2512.24714v1#S2.E5 "In 2 Assumptions and the convolution method ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) and using finite differences derived from the CFFT-BSDE approximation of YtY\_{t}.

Figure 3: Call option delta surface - convolution method with boundary error control

![Refer to caption](x3.png)

The delta surface provided in Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)) does not show the full picture on the truncation region since the value of delta explodes at boundary as well. Figure [3](https://arxiv.org/html/2512.24714v1#S4.F3 "Figure 3 ‣ 4 Numerical result of option pricing ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method") demonstrates that our method displays the entire delta surface which is smooth and very accurate at the boundaries.

Table 1: ATM Delta errors for the CFFT/BSDE method (via ZZ and finite differences) against Black–Scholes.
S0=100S\_{0}=100, K=100K=100, r=0.01r=0.01, σ=0.2\sigma=0.2, T=1T=1.

| nn | LL | NN | ΔBS\Delta\_{\mathrm{BS}} | ΔZ\Delta\_{Z} | |ΔZ−ΔBS||\Delta\_{Z}-\Delta\_{\mathrm{BS}}| | |ΔZ−ΔBS||ΔBS|\frac{|\Delta\_{Z}-\Delta\_{\mathrm{BS}}|}{|\Delta\_{\mathrm{BS}}|} | ΔFD\Delta\_{\mathrm{FD}} | |ΔFD−ΔBS||\Delta\_{\mathrm{FD}}-\Delta\_{\mathrm{BS}}| | |ΔFD−ΔBS||ΔBS|\frac{|\Delta\_{\mathrm{FD}}-\Delta\_{\mathrm{BS}}|}{|\Delta\_{\mathrm{BS}}|} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1000 | 10.000000 | 2102^{10} | 0.559618 | 0.559619 | 1.153e-06 | 2.061e-06 | 0.559613 | 4.418e-06 | 7.894e-06 |
| 1000 | 10.000000 | 2112^{11} | 0.559618 | 0.559622 | 4.616e-06 | 8.249e-06 | 0.559617 | 9.785e-07 | 1.749e-06 |
| 1000 | 10.000000 | 2122^{12} | 0.559618 | 0.559623 | 5.351e-06 | 9.562e-06 | 0.559617 | 2.448e-07 | 4.375e-07 |
| 1000 | 12.000000 | 2102^{10} | 0.559618 | 0.559616 | 1.266e-06 | 2.263e-06 | 0.559611 | 6.810e-06 | 1.217e-05 |
| 1000 | 12.000000 | 2112^{11} | 0.559618 | 0.559622 | 4.178e-06 | 7.466e-06 | 0.559616 | 1.415e-06 | 2.528e-06 |
| 1000 | 12.000000 | 2122^{12} | 0.559618 | 0.559623 | 5.244e-06 | 9.370e-06 | 0.559617 | 3.525e-07 | 6.299e-07 |
| 1000 | 14.000000 | 2102^{10} | 0.559618 | 0.559613 | 4.369e-06 | 7.807e-06 | 0.559608 | 9.868e-06 | 1.763e-05 |
| 1000 | 14.000000 | 2112^{11} | 0.559618 | 0.559621 | 3.634e-06 | 6.494e-06 | 0.559616 | 1.956e-06 | 3.495e-06 |
| 1000 | 14.000000 | 2122^{12} | 0.559618 | 0.559623 | 5.116e-06 | 9.142e-06 | 0.559617 | 4.797e-07 | 8.571e-07 |
| 2000 | 10.000000 | 2102^{10} | 0.559618 | 0.559616 | 1.925e-06 | 3.441e-06 | 0.559613 | 4.698e-06 | 8.396e-06 |
| 2000 | 10.000000 | 2112^{11} | 0.559618 | 0.559619 | 1.801e-06 | 3.218e-06 | 0.559617 | 9.958e-07 | 1.779e-06 |
| 2000 | 10.000000 | 2122^{12} | 0.559618 | 0.559620 | 2.553e-06 | 4.562e-06 | 0.559617 | 2.448e-07 | 4.375e-07 |
| 2000 | 12.000000 | 2102^{10} | 0.559618 | 0.559613 | 4.467e-06 | 7.982e-06 | 0.559610 | 7.213e-06 | 1.289e-05 |
| 2000 | 12.000000 | 2112^{11} | 0.559618 | 0.559619 | 1.310e-06 | 2.341e-06 | 0.559616 | 1.485e-06 | 2.653e-06 |
| 2000 | 12.000000 | 2122^{12} | 0.559618 | 0.559620 | 2.445e-06 | 4.370e-06 | 0.559617 | 3.525e-07 | 6.299e-07 |
| 2000 | 14.000000 | 2102^{10} | 0.559618 | 0.559610 | 7.639e-06 | 1.365e-05 | 0.559607 | 1.034e-05 | 1.848e-05 |
| 2000 | 14.000000 | 2112^{11} | 0.559618 | 0.559618 | 6.851e-07 | 1.224e-06 | 0.559616 | 2.107e-06 | 3.765e-06 |
| 2000 | 14.000000 | 2122^{12} | 0.559618 | 0.559620 | 2.318e-06 | 4.142e-06 | 0.559617 | 4.798e-07 | 8.574e-07 |
| 5000 | 10.000000 | 2102^{10} | 0.559618 | 0.559614 | 3.791e-06 | 6.775e-06 | 0.559613 | 4.885e-06 | 8.730e-06 |
| 5000 | 10.000000 | 2112^{11} | 0.559618 | 0.559618 | 7.899e-08 | 1.412e-07 | 0.559617 | 1.039e-06 | 1.856e-06 |
| 5000 | 10.000000 | 2122^{12} | 0.559618 | 0.559619 | 8.740e-07 | 1.562e-06 | 0.559617 | 2.451e-07 | 4.380e-07 |
| 5000 | 12.000000 | 2102^{10} | 0.559618 | 0.559611 | 6.346e-06 | 1.134e-05 | 0.559610 | 7.413e-06 | 1.325e-05 |
| 5000 | 12.000000 | 2112^{11} | 0.559618 | 0.559617 | 4.101e-07 | 7.328e-07 | 0.559616 | 1.526e-06 | 2.727e-06 |
| 5000 | 12.000000 | 2122^{12} | 0.559618 | 0.559618 | 7.638e-07 | 1.365e-06 | 0.559617 | 3.553e-07 | 6.348e-07 |
| 5000 | 14.000000 | 2102^{10} | 0.559618 | 0.559608 | 9.524e-06 | 1.702e-05 | 0.559607 | 1.055e-05 | 1.885e-05 |
| 5000 | 14.000000 | 2112^{11} | 0.559618 | 0.559617 | 1.062e-06 | 1.898e-06 | 0.559616 | 2.175e-06 | 3.887e-06 |
| 5000 | 14.000000 | 2122^{12} | 0.559618 | 0.559618 | 6.281e-07 | 1.122e-06 | 0.559617 | 4.908e-07 | 8.770e-07 |

## 5 Conclusion

In this paper, we propose a numerical method that improves the performance using convolution method in solving BSDEs and demonstrate that the boundary error is significantly reduced by our method. This numerical method provides a new approach to improve the accuracy of convolution method with the fast Fourier transform. Our motivation is focused on the transformation of the target function using a shifting function which is similar to the terminal of the BSDEs and is able to map the target function as a bounded periodic function. We have studied the application of the convolution method in valuing options through the framework of BSDEs and provided detailed error analysis including three parts from extrapolation, truncation to discretization. The numerical result shows that our method has better accuracy than the original method given by Hyndman and
Oyono Ngou ([2017](https://arxiv.org/html/2512.24714v1#bib.bib10)). Both the theoretical analysis and numerical result show us that the boundary error still increases with respect to the truncation domain, however, the boundary error is well controlled by using our method in the Fourier transform for the unbounded and non-periodic problem. Therefore, our method is feasible to apply on more general BSDEs problems. Future work will investigate extensions of this approach to more general BSDEs and to higher dimensional problems.

## References

* Antonelli (1993)

  Antonelli, F. (1993).
  Backward forward stochastic differential equations.
  Ph. D. thesis, Purdue University.
* Bender and
  Denk (2007)

  Bender, C. and R. Denk (2007).
  A forward scheme for backward sdes.
  Stochastic processes and their applications 117(12),
  1793–1812.
* Bouchard
  et al. (2009)

  Bouchard, B., R. Elie, and N. Touzi (2009).
  Discrete-time approximation of bsdes and probabilistic schemes for
  fully nonlinear pdes.
  In H. Albrecher, W. J. Runggaldier, and W. Schachermayer (Eds.), Advanced Financial Modelling, pp. 91–124. De Gruyter.
* Bouchard and
  Touzi (2004)

  Bouchard, B. and N. Touzi (2004).
  Discrete-time approximation and monte-carlo simulation of backward
  stochastic differential equations.
  Stochastic Processes and Their Applications 111(2),
  175–206.
* Carr and
  Madan (1999)

  Carr, P. and D. Madan (1999).
  Option valuation using the fast Fourier transform.
  Journal of Computational Finance 2(4), 61–73.
* Douglas
  et al. (1996)

  Douglas, J., J. Ma, and P. Protter (1996).
  Numerical methods for forward-backward stochastic differential
  equations.
  Annals of Applied Probability 6(3), 940–968.
* Gao (2021)

  Gao, X. (2021, March).
  Stochastic control, numerical methods, and machine learning in
  finance and insurance.
  Ph. D. thesis, Concordia University.
* Gao and
  Hyndman (2025)

  Gao, X. and C. B. Hyndman (2025).
  Convolution-FFT for option pricing in the Heston model.
  arXiv preprint.
  2512.05326.
* Huijskens
  et al. (2016)

  Huijskens, T., M. J. Ruijter, and C. W. Oosterlee (2016).
  Efficient numerical Fourier methods for coupled forward–backward
  SDEs.
  Journal of Computational and Applied Mathematics 296,
  593–612.
* Hyndman and
  Oyono Ngou (2017)

  Hyndman, C. B. and P. Oyono Ngou (2017).
  A convolution method for numerical solution of backward stochastic
  differential equations.
  Methodology and Computing in Applied Probability 19(1), 1–29.
* Kobylanski (2000)

  Kobylanski, M. (2000).
  Backward stochastic differential equations and partial differential
  equations with quadratic growth.
  Annals of Probability 28(2), 558–602.
* Lemor
  et al. (2006)

  Lemor, J.-P., E. Gobet, and X. Warin (2006).
  Rate of convergence of an empirical regression method for solving
  generalized backward stochastic differential equations.
  Bernoulli 12(5), 889–916.
* Lord and
  Kahl (2006)

  Lord, R. and C. Kahl (2006, 01).
  Optimal Fourier inversion in semi-analytical option pricing.
  Tinbergen Institute, Tinbergen Institute Discussion
  Papers 10, 1–23.
* Ma
  et al. (1999)

  Ma, J., J.-M. Morel, and J. Yong (1999).
  Forward-backward stochastic differential equations and their
  applications.
  Number 1702 in Lecture Notes in Mathematics. Berlin Heidelberg:
  Springer Verlag.
* Oyono Ngou and
  Hyndman (2022)

  Oyono Ngou, P. and C. B. Hyndman (2022).
  A Fourier interpolation method for numerical solution of FBSDEs:
  Global convergence, stability, and higher order discretizations.
  Journal of Risk and Financial Management 15(9), 388.
* Pardoux and
  Peng (1990)

  Pardoux, E. and S. Peng (1990).
  Adapted solution of a backward stochastic differential equation.
  Systems & Control Letters 14(1), 55–61.
* Risken (1996)

  Risken, H. (1996).
  The Fokker-Planck Equation (2nd ed.).
  Berlin Heidelberg: Springer.
* Vretblad (2003)

  Vretblad, A. (2003).
  Fourier Analysis and its Applications, Volume 223.
  New York: Springer.
* Yong (1997)

  Yong, J. (1997).
  Finding adapted solutions of forward-backward stochastic differential
  equations: method of continuation.
  Probability Theory and Related Fields 107(4),
  537–572.
* Zhang (2004)

  Zhang, J. (2004).
  A numerical scheme for BSDEs.
  Annals of Applied Probability 14(1), 459–488.

## Appendix A Appendix

We provide the technical results for the proofs.

### A.1 Proof of Theorem [3.1](https://arxiv.org/html/2512.24714v1#S3.Thmtheorem1 "Theorem 3.1 (Global error bounds). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")

###### Proof.

According to Bouchard
et al. ([2009](https://arxiv.org/html/2512.24714v1#bib.bib3)), the explicit Euler scheme

|  |  |  |
| --- | --- | --- |
|  | {Zti=1Δ​t​𝔼​[Yi+1​Δ​Wti],Yti=𝔼​[Yti+1]+Δ​t​f​(ti,Xti,𝔼​[Yti+1],Zti),\left\{\begin{aligned} Z\_{t\_{i}}=&\frac{1}{\Delta t}\mathbb{E}\left[Y\_{i+1}\Delta{W}\_{t\_{i}}\right],\\ Y\_{t\_{i}}=&\mathbb{E}\left[Y\_{t\_{i+1}}\right]+\Delta tf\left({t\_{i}},X\_{t\_{i}},\mathbb{E}\left[Y\_{t\_{i+1}}\right],{Z}\_{t\_{i}}\right),\end{aligned}\right. |  |

admits an error in order 𝒪​(Δ​t12)\mathcal{O}\left(\Delta t^{\frac{1}{2}}\right) for any t∈[ti,ti+1]t\in[t\_{i},t\_{i+1}]

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[supti≤t≤ti+1|Yt−Yti|]≤C​(Δ​t12).\mathbb{E}\left[\sup\_{t\_{i}\leq t\leq t\_{i+1}}\Big|Y\_{t}-Y\_{t\_{i}}\Big|\right]\leq C\left(\Delta t^{\frac{1}{2}}\right). |  | (A.1) |

Since ff is Lipschitz continuous, we obtain that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Yti−YtiΔ|≤\displaystyle\left|Y\_{t\_{i}}-Y^{\Delta}\_{t\_{i}}\right|\leq | C​Δ​t​(|𝔼​[Yti+1]−𝔼.⁡​[Yti+1]|+|Zti+1−Zti+1Δ|).\displaystyle C\Delta t\left(\left|\mathbb{E}\left[Y\_{t\_{i+1}}\right]-\overset{\,{}\_{\mbox{\Large.}}}{\mathbb{E}}\left[Y\_{t\_{i+1}}\right]\right|+\left|Z\_{t\_{i+1}}-Z^{\Delta}\_{t\_{i+1}}\right|\right). |  | (A.2) |

According to ([3.14](https://arxiv.org/html/2512.24714v1#S3.E14 "In Remark 3.2 (Error transfer with damping parameter). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) and ([3.15](https://arxiv.org/html/2512.24714v1#S3.E15 "In Remark 3.2 (Error transfer with damping parameter). ‣ 3.4 Error analysis ‣ 3 Boundary control schemes ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), we can rewrite ([A.2](https://arxiv.org/html/2512.24714v1#A1.E2 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Yti−YtiΔ|≤\displaystyle\left|Y\_{t\_{i}}-Y^{\Delta}\_{t\_{i}}\right|\leq | C​Δ​t​(N−1+|α|+1σ​2​π​Δ​t+e−K​N2L2​Δ​t)\displaystyle C\Delta t\left(N^{-1}+|\alpha|+\frac{1}{\sigma\sqrt{2\pi\Delta t}}+e^{-K\frac{N^{2}}{L^{2}}\Delta t}\right) |  | (A.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​(Δ​t12+Δ​t+Δ​t​N−1+Δ​t​e−K​N2L2​Δ​t).\displaystyle C\left(\Delta t^{\frac{1}{2}}+\Delta t+\Delta tN^{-1}+\Delta te^{-K\frac{N^{2}}{L^{2}}\Delta t}\right). |  | (A.4) |

Combining ([A.1](https://arxiv.org/html/2512.24714v1#A1.E1 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")) and ([A.3](https://arxiv.org/html/2512.24714v1#A1.E3 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Boundary error control for numerical solution of BSDEs by the convolution-FFT method")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | e​r​r​(Δ)≔\displaystyle err(\Delta)\coloneqq | max0≤i≤n⁡𝔼​[supti≤t≤ti+1|Yt−YtiΔ|]\displaystyle\max\_{0\leq i\leq n}\mathbb{E}\left[\sup\_{t\_{i}\leq t\leq t\_{i+1}}\left|Y\_{t}-Y^{\Delta}\_{t\_{i}}\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | max0≤i≤n⁡𝔼​[supti≤t≤ti+1|Yt−Yti|+|Yti−YtiΔ|]\displaystyle\max\_{0\leq i\leq n}\mathbb{E}\left[\sup\_{t\_{i}\leq t\leq t\_{i+1}}\Big|Y\_{t}-Y\_{t\_{i}}\Big|+\left|Y\_{t\_{i}}-Y^{\Delta}\_{t\_{i}}\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝒪​(Δ​t12)+𝒪​(Δ​t)+𝒪​(Δ​t​N−1)+𝒪​(Δ​t​e−K​N2L2​Δ​t)\displaystyle\mathcal{O}\left(\Delta t^{\frac{1}{2}}\right)+\mathcal{O}\left(\Delta t\right)+\mathcal{O}\left(\Delta tN^{-1}\right)+\mathcal{O}\left(\Delta te^{-K\frac{N^{2}}{L^{2}}\Delta t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝒪​(Δ​t12)+𝒪​(Δ​t)+𝒪​(Δ​t​Δ​x)+𝒪​(Δ​t​e−K​Δ​tΔ​x2).\displaystyle\mathcal{O}\left(\Delta t^{\frac{1}{2}}\right)+\mathcal{O}\left(\Delta t\right)+\mathcal{O}\left(\Delta t\Delta x\right)+\mathcal{O}\left(\Delta te^{-K\frac{\Delta t}{\Delta x^{2}}}\right). |  |

∎