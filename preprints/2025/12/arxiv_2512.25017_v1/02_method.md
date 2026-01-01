---
authors:
- Chenguang Liu
- Antonis Papapantoleon
- Jasper Rou
doc_id: arxiv:2512.25017v1
family_id: arxiv:2512.25017
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Convergence of the generalization error for Deep Gradient Flow Methods for
  PDEs
url_abs: http://arxiv.org/abs/2512.25017v1
url_html: https://arxiv.org/html/2512.25017v1
venue: arXiv q-fin
version: 1
year: 2025
---


Chenguang Liu
, 
Antonis Papapantoleon
 and 
Jasper Rou
Delft Institute of Applied Mathematics, EEMCS, TU Delft, 2628 Delft, The Netherlands.
[C.Liu-13@tudelft.nl](mailto:C.Liu-13@tudelft.nl)
Delft Institute of Applied Mathematics, EEMCS, TU Delft, 2628 Delft, The Netherlands & Institute of Applied and Computational Mathematics, FORTH, 70013 Heraklion, Greece
[a.papapantoleon@tudelft.nl](mailto:a.papapantoleon@tudelft.nl)
Delft Institute of Applied Mathematics, EEMCS, TU Delft, 2628 Delft, The Netherlands
[J.G.Rou@tudelft.nl](mailto:J.G.Rou@tudelft.nl)

###### Abstract.

The aim of this article is to provide a firm mathematical foundation for the application of deep gradient flow methods (DGFMs) for the solution of (high-dimensional) partial differential equations (PDEs).
We decompose the generalization error of DGFMs into an approximation and a training error.
We first show that the solution of PDEs that satisfy reasonable and verifiable assumptions can be approximated by neural networks, thus the approximation error tends to zero as the number of neurons tends to infinity.
Then, we derive the gradient flow that the training process follows in the “wide network limit” and analyze the limit of this flow as the training time tends to infinity. These results combined show that the generalization error of DGFMs tends to zero as the number of neurons and the training time tend to infinity.

###### Key words and phrases:

Partial differential equations, deep learning, neural networks, gradient flows, generalization error, training error, approximation error, convergence

###### 2020 Mathematics Subject Classification:

68T07, 65M12

## 1. Introduction

Deep learning methods for the solution of high-dimensional partial differential equations (PDEs) have gained tremendous popularity in the last few years, since they can tackle equations in dimensions that were not attainable by classical methods, such as finite difference and finite element schemes.
This ability allows the modeling of more realistic phenomena across various fields of science and technology, including engineering, biology, economics, and finance.
The seminal articles of Sirignano and Spiliopoulos [[29](https://arxiv.org/html/2512.25017v1#bib.bib29)] on the Deep Galerkin Method (DGM) and of Raissi and Karniadakis [[26](https://arxiv.org/html/2512.25017v1#bib.bib26)] and Raissi et al. [[27](https://arxiv.org/html/2512.25017v1#bib.bib27)] on physics-informed neural networks (PINNs), building on the earlier work of Lagaris et al. [[18](https://arxiv.org/html/2512.25017v1#bib.bib18)] and Lagaris et al. [[19](https://arxiv.org/html/2512.25017v1#bib.bib19)], incorporate the PDE residual and the initial and boundary conditions into the loss function of a neural network, which is then minimized by stochastic gradient descent (SGD).
These methods have laid the foundations for a variety of extensions and applications, including among many others, fractional differential equations (Pang et al. [[23](https://arxiv.org/html/2512.25017v1#bib.bib23)]), variational PINNs (Kharazmi et al. [[17](https://arxiv.org/html/2512.25017v1#bib.bib17)]), Bayesian variants (Yang et al. [[31](https://arxiv.org/html/2512.25017v1#bib.bib31)]) and mean-field games (Carmona and Zeng [[4](https://arxiv.org/html/2512.25017v1#bib.bib4)]).

On the other hand, deep gradient flow methods (DGFMs), also known as deep Ritz methods, formulate the PDE as an energy minimization problem, where the energy is derived from the differential operator, which typically leads to a loss function that is easier to compute.
Moreover, they usually discretize the equation in time and train one network for each time step, instead of using a monolithic space-time discretization; see e.g., E and Yu [[6](https://arxiv.org/html/2512.25017v1#bib.bib6)], Liao and Ming [[20](https://arxiv.org/html/2512.25017v1#bib.bib20)], Georgoulis et al. [[8](https://arxiv.org/html/2512.25017v1#bib.bib8)], Park et al. [[25](https://arxiv.org/html/2512.25017v1#bib.bib25)], Papapantoleon and Rou [[24](https://arxiv.org/html/2512.25017v1#bib.bib24)], Bruna et al. [[3](https://arxiv.org/html/2512.25017v1#bib.bib3)] for differential operators, and Georgoulis et al. [[9](https://arxiv.org/html/2512.25017v1#bib.bib9)] for an integro-differential operator.
A comprehensive review of the available methods appears in the forthcoming book of Jentzen et al. [[14](https://arxiv.org/html/2512.25017v1#bib.bib14)].

In the present article, we are interested in analyzing the error of deep gradient flow methods for the solution of PDEs.
Let us consider the PDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | ut+𝒜​u=0,(t,x)∈[0,T]×D,u​(0,x)=Φ​(x),x∈∂D,\begin{split}u\_{t}+\mathcal{A}u&=0,\quad(t,x)\in[0,T]\times D,\\ u(0,x)&=\Phi(x),\quad x\in\partial D,\end{split} |  | (1.1) |

where 𝒜\mathcal{A} is a differential operator, Φ\Phi determines the initial condition, TT is a (finite) time horizon, and D⊆ℝdD\subseteq\mathbb{R}^{d} is the domain of the PDE.
The DGFMs translate the PDE into an energy minimization problem, which is then computed using stochastic gradient descent or one of its variants (e.g. ADAM), and can be described in the following manner:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uθ,n⋆=arg​minv∈𝒞θn​∫ℓ​(v​(x))​dx,u^{\star}\_{\theta,n}=\operatorname\*{arg\,min}\_{v\in\mathcal{C}^{n}\_{\theta}}\int\ell(v(x))\mathrm{d}x, |  | (1.2) |

where 𝒞θn\mathcal{C}^{n}\_{\theta} denotes the space of neural networks with nn neurons where θ\theta is the set of trainable parameters, while ℓ\ell denotes the energy functional associated to the operator 𝒜\mathcal{A}.

Let u⋆u^{\star} denote the unique solution of ([1.1](https://arxiv.org/html/2512.25017v1#S1.E1 "Equation 1.1 ‣ 1. Introduction ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
We would like to analyze and study the difference between the true solution of ([1.1](https://arxiv.org/html/2512.25017v1#S1.E1 "Equation 1.1 ‣ 1. Introduction ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) and the solution computed by the deep gradient flow methods, *i.e.* by the outcome of the minimization problem ([1.2](https://arxiv.org/html/2512.25017v1#S1.E2 "Equation 1.2 ‣ 1. Introduction ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
This difference is known as the generalization error in the machine learning literature, *i.e.*

|  |  |  |
| --- | --- | --- |
|  | ℰgen=‖u⋆−uθ,n⋆‖.\mathcal{E}\_{\text{gen}}=\|u^{\star}-u^{\star}\_{\theta,n}\|. |  |

The generalization error ℰgen\mathcal{E}\_{\text{gen}} can be decomposed in three separate components:

* •

  the quadrature error ℰquad\mathcal{E}\_{\text{quad}}, which refers to how well the integral in ([1.2](https://arxiv.org/html/2512.25017v1#S1.E2 "Equation 1.2 ‣ 1. Introduction ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) is approximated by Monte Carlo simulations or another quadrature method;
* •

  the approximation error ℰapprox\mathcal{E}\_{\text{approx}}, which refers to how well the neural network vv can approximate the continuous function uu that solves the PDE ([1.1](https://arxiv.org/html/2512.25017v1#S1.E1 "Equation 1.1 ‣ 1. Introduction ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"));
* •

  the training error ℰtrain\mathcal{E}\_{\text{train}}, which refers to how well GD or SGD approximate the true solution of the minimization problem ([1.2](https://arxiv.org/html/2512.25017v1#S1.E2 "Equation 1.2 ‣ 1. Introduction ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).

Then, we have the error decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰgen=ℰtrain+ℰquad+ℰapprox,\displaystyle\mathcal{E}\_{\text{gen}}=\mathcal{E}\_{\text{train}}+\mathcal{E}\_{\text{quad}}+\mathcal{E}\_{\text{approx}}, |  | (1.3) |

and the aim of the present paper is to study these errors and show that, as the numbers of neurons tends to infinity and the training time also tends to infinity, then the generalization error tends to zero, and the outcome of the deep gradient flow method indeed approximates the solution of the PDE.

There are several articles available that study the generalization error of deep learning methods for PDEs, typically focusing on the popular DGM and PINN methods.
These methods rely on approximability properties of neural networks and properties of quadrature methods in order to control the generalization error, while they typically consider only a posteriori estimates for the training error.
We refer the interested reader to Mishra and Molinaro [[22](https://arxiv.org/html/2512.25017v1#bib.bib22)] and Gazoulis et al. [[7](https://arxiv.org/html/2512.25017v1#bib.bib7)] for results on PINNs, and the related while more general article of Loulakis and
Makridakis [[21](https://arxiv.org/html/2512.25017v1#bib.bib21)].
Moreover, several articles consider the approximation error of DMG and PINNs; see, for example, Sirignano and Spiliopoulos [[29](https://arxiv.org/html/2512.25017v1#bib.bib29)] and Shin et al. [[28](https://arxiv.org/html/2512.25017v1#bib.bib28)].
The recent article of Jiang et al. [[15](https://arxiv.org/html/2512.25017v1#bib.bib15)] considers the “global” convergence of DGM and PINNs, which amounts to the convergence of the training error in our notation.
Combined with other available results, this article allows to deduce the convergence of the generalization error of these methods.
Compared to the extended literature on DGM and PINNs, there are significantly fewer papers on DGFMs; let us mention here the articles of Dondl et al. [[5](https://arxiv.org/html/2512.25017v1#bib.bib5)] which focuses on the approximation error, and Jiao et al. [[16](https://arxiv.org/html/2512.25017v1#bib.bib16)] which provides a convergence rate using the Rademacher complexities.

The aim of the present article is to provide convergence results on the generalization error of DGFMs under reasonable and verifiable hypothesis on the underlying PDEs.
The first part of this work focuses on the analysis of the approximation error, i.e. we show that there exists a neural network that approximates the solution of the PDE.
This result uses ideas from PDE theory, optimization and the calculus of variations, and is inspired by the seminal paper of Sirignano and Spiliopoulos [[29](https://arxiv.org/html/2512.25017v1#bib.bib29)].
The second part of this work focuses on the analysis of the training error, and we show that as the number of neurons tend to infinity and the training time also tends to infinity, then the outcome of the deep gradient flow method tends to the true solution of the PDE.
This result is inspired by the work of Jiang et al. [[15](https://arxiv.org/html/2512.25017v1#bib.bib15)].
The quadrature error is the most well-understood error of the three, thus this work focuses on the other two errors.
Moreover, let us mention for the sake of completeness, that our method also induces a discretization error, from the time-stepping scheme.
However, as this error is also well-studied and understood, we have chosen to omit it from the discussion here.
The combination of these results, yields that the generalization error also tends to zero.

This article is organized as follows:
[2](https://arxiv.org/html/2512.25017v1#S2 "2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") provides an overview of deep gradient flow methods for the solution of PDEs.
[3](https://arxiv.org/html/2512.25017v1#S3 "3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") studies the approximation error of DGFMs, using the variational formulation of PDEs and a tailored version of the universal approximation theorem.
[4](https://arxiv.org/html/2512.25017v1#S4 "4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") studies the training error of DGFMs; we first derive a gradient flow that the training process satisfies in the “wide network limit” and then analyze the behavior of this flow as the training time tends to infinity.
Finally, the appendices contain auxilliary estimates and examples.

### 1.1. Notation

Let ℋ\mathcal{H} denote an arbitrary space, then ∥⋅∥ℋ\|\cdot\|\_{\mathcal{H}} denotes the norm, ⟨⋅,⋅⟩ℋ\langle\cdot,\cdot\rangle\_{\mathcal{H}} denotes the inner product, and wm⇀ℋww\_{m}\xrightharpoonup{\,\,\,\mathcal{H}\,\,\,}w denotes the weak convergence on this space.
We abbreviate spaces and norms as ℋ=ℋ​(ℝd)\mathcal{H}=\mathcal{H}(\mathbb{R}^{d}) and ‖f‖ℋ=‖f‖ℋ​(ℝd)\left\|f\right\|\_{\mathcal{H}}=\left\|f\right\|\_{\mathcal{H}(\mathbb{R}^{d})}.

Let 1≤p<∞1\leq p<\infty and denote by Lp​(ℝd)L^{p}(\mathbb{R}^{d}) the space of functions with finite pp-norm, where

|  |  |  |
| --- | --- | --- |
|  | ‖f‖Lp=(∫ℝd|f​(x)|p​dx)1p,\left\|f\right\|\_{L^{p}}=\left(\int\_{\mathbb{R}^{d}}\left|f(x)\right|^{p}\mathrm{d}x\right)^{\frac{1}{p}}, |  |

while LlocpL^{p}\_{\text{loc}} denotes the space of functions in LpL^{p} that are locally integrable.
Let Cck​(ℝd)C\_{c}^{k}\left(\mathbb{R}^{d}\right) denote the space of functions with compact support and continuous partial derivatives up to order kk.
Moreover, let W0k,p​(ℝd)W\_{0}^{k,p}(\mathbb{R}^{d}) denote the Sobolev space with norm

|  |  |  |
| --- | --- | --- |
|  | ‖f‖W0k,p=(∑|α|≤k∫ℝd|Dα​f​(x)|p​dx)1p<∞,\left\|f\right\|\_{W\_{0}^{k,p}}=\left(\sum\_{\left|\alpha\right|\leq k}\int\_{\mathbb{R}^{d}}\left|D^{\alpha}f(x)\right|^{p}\mathrm{d}x\right)^{\frac{1}{p}}<\infty, |  |

with Dα​fD^{\alpha}f the weak derivative of ff and α\alpha a multi-index.
Let us introduce the shorthand notation ℋ0k​(ℝd):=W0k,2​(ℝd)\mathcal{H}\_{0}^{k}(\mathbb{R}^{d}):=W\_{0}^{k,2}(\mathbb{R}^{d}) for Sobolev spaces, and let ℋ−1​(ℝd)\mathcal{H}^{-1}(\mathbb{R}^{d}) denote the dual space of ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}).

Finally, let 𝒱⊂ℋ⊂𝒱∗\mathcal{V}\subset\mathcal{H}\subset\mathcal{V}^{\*} denote a Gelfand triple, in which ℋ\mathcal{H} is a separable Hilbert space, 𝒱\mathcal{V} is a Banach space and 𝒱∗\mathcal{V}^{\*} is the topological dual of 𝒱\mathcal{V}.

###### Definition 1.1 (Self-adjoint operator).

An operator ℒ:𝒱→𝒱∗\mathcal{L}:\mathcal{V}\to\mathcal{V}^{\*} is self-adjoint if

|  |  |  |
| --- | --- | --- |
|  | ⟨ℒ​u,v⟩𝒱∗,𝒱=⟨ℒ​v,u⟩𝒱∗,𝒱for all ​u,v∈𝒱.\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{V}^{\*},\mathcal{V}}=\left\langle\mathcal{L}v,u\right\rangle\_{\mathcal{V}^{\*},\mathcal{V}}\quad\text{for all \ }u,v\in\mathcal{V}. |  |

###### Remark 1.2.

The inner product ⟨ℒ​u,v⟩𝒱∗,𝒱\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{V}^{\*},\mathcal{V}} means that ℒ​u\mathcal{L}u acts on vv as a functional.
An important example is the following: 𝒱=ℋ01​(ℝd)\mathcal{V}=\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), 𝒱∗=ℋ−1​(ℝd)\mathcal{V}^{\*}=\mathcal{H}^{-1}(\mathbb{R}^{d}), ℋ=L2​(ℝd)\mathcal{H}=L^{2}(\mathbb{R}^{d}), and ℒ=−Δ\mathcal{L}=-\Delta, where Δ\Delta denotes the Laplace operator.
Then, we define the functional ℒ​u\mathcal{L}u as follows

|  |  |  |
| --- | --- | --- |
|  | ⟨ℒ​u,v⟩ℋ−1,ℋ01=⟨−Δ​u,v⟩ℋ−1,ℋ01:=⟨∇u,∇v⟩L2.\displaystyle\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}=\left\langle-\Delta u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}:=\left\langle\nabla u,\nabla v\right\rangle\_{L^{2}}. |  |

## 2. Deep gradient flow methods for PDEs

Let us start by providing an overview of deep gradient flow methods (DGFMs) for the solution of PDEs.
These methods have gained increased popularity in the literature because they can efficiently handle high-dimensional PDEs stemming from physics, engineering, and finance; see e.g. E and Yu [[6](https://arxiv.org/html/2512.25017v1#bib.bib6)], Liao and Ming [[20](https://arxiv.org/html/2512.25017v1#bib.bib20)], Georgoulis et al. [[8](https://arxiv.org/html/2512.25017v1#bib.bib8)], Park et al. [[25](https://arxiv.org/html/2512.25017v1#bib.bib25)] and Papapantoleon and Rou [[24](https://arxiv.org/html/2512.25017v1#bib.bib24)] for differential operators, and Georgoulis et al. [[9](https://arxiv.org/html/2512.25017v1#bib.bib9)] for an integro-differential operator.
Deep gradient flow methods reformulate the PDE as an energy minimization problem, which is then approximated in a time-stepping fashion by deep artificial neural networks.
This method results in a loss function that is tailor-made to the PDE at hand, avoids the use of a second derivative, which is computationally costly, and reduces the training time compared to, for instance, the DGM of Sirignano and Spiliopoulos [[29](https://arxiv.org/html/2512.25017v1#bib.bib29)]; see e.g. Georgoulis et al. [[8](https://arxiv.org/html/2512.25017v1#bib.bib8), Sec. 5].

Let u​(t,x):[0,T]×ℝd→ℝu\left(t,x\right):\left[0,T\right]\times\mathbb{R}^{d}\to\mathbb{R} be the solution of the following partial (integro-)differential equation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ut+𝒜​u\displaystyle u\_{t}+\mathcal{A}u | =0,u​(0)=u0,\displaystyle=0,\quad u(0)=u\_{0}, |  | (2.1) |

where 𝒜\mathcal{A} is an operator from 𝒱\mathcal{V} to 𝒱∗\mathcal{V}^{\*} and u0∈ℋu\_{0}\in\mathcal{H} is the initial condition.
In order to write the PDE as an energy minimization problem, we need to split the operator in a symmetric and an (asymmetric) remainder part, *i.e.*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒜​u\displaystyle\mathcal{A}u | =ℒ​u+F​(u),\displaystyle=\mathcal{L}u+F(u), |  | (2.2) |

where ℒ\mathcal{L} is a self-adjoint, linear operator and FF is a (possibly non-linear) operator from 𝒱\mathcal{V} to 𝒱∗\mathcal{V}^{\*}.
This PDE is then discretized using, for example, the backward Euler differentiation scheme, which yields

|  |  |  |
| --- | --- | --- |
|  | Uk−Uk−1h+ℒ​Uk+F​(Uk−1)=0,U0=u0,\frac{U^{k}-U^{k-1}}{h}+\mathcal{L}U^{k}+F\Big(U^{k-1}\Big)=0,\quad U^{0}=u\_{0}, |  |

where UkU^{k} denotes the approximation to the solution of the PDE u​(tk)u(t\_{k}) at time step tkt\_{k}, on an appropriate grid.
The variational formulation of this equation yields an energy functional Ik​(v)I^{k}(v) such that UkU^{k} is a critical point of IkI^{k}, where

|  |  |  |
| --- | --- | --- |
|  | Ik​(v)=12​‖v−Uk−1‖ℋ2+h2​⟨ℒ​v,v⟩𝒱∗,𝒱+h​⟨F​(Uk−1),v⟩ℋ.I^{k}(v)=\frac{1}{2}\left\|v-U^{k-1}\right\|\_{\mathcal{H}}^{2}+\frac{h}{2}\left\langle\mathcal{L}v,v\right\rangle\_{\mathcal{V}^{\*},\mathcal{V}}+h\left\langle F\left(U^{k-1}\right),v\right\rangle\_{\mathcal{H}}. |  |

The function vv is approximated by artificial neural networks which are trained using the stochastic gradient descent (SGD) algorithm, or one of its variants, while the functional IkI^{k} provides a loss function for the SGD iterations which is tailor-made for this problem.
The aim of this paper is to show that this procedure converges to the true solution u⋆u^{\star} of the PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).

Next, we present examples of PDEs that have been treated by DGFMs, and their applications.

###### Example 2.1 (Heat equation).

The simplest example that fits this framework is the celebrated heat equation, which reads

|  |  |  |
| --- | --- | --- |
|  | ut=κ​Δ​u,κ>0,u\_{t}=\kappa\Delta u,\quad\kappa>0, |  |

subject to an initial condition.
Then 𝒜=ℒ=−κ​Δ\mathcal{A}=\mathcal{L}=-\kappa\Delta and F​(u)=0F(u)=0.

###### Example 2.2.

Georgoulis et al. [[8](https://arxiv.org/html/2512.25017v1#bib.bib8)] consider dissipative evolution PDEs of the following form

|  |  |  |
| --- | --- | --- |
|  | ut−∇⋅(A​∇u)=F,u\_{t}-\nabla\cdot(A\nabla u)=F, |  |

subject to appropriate initial and terminal conditions, where AA is a symmetric, uniformly positive definite and bounded diffusion tensor and FF is a suitable function.
Then, we have that 𝒜=ℒ=−∇⋅(A​∇u)\mathcal{A}=\mathcal{L}=-\nabla\cdot(A\nabla u).

###### Example 2.3 (Option pricing PDEs).

PDEs arising in the valuation of financial derivatives fit naturally in this setting.
In the Black and Scholes [[2](https://arxiv.org/html/2512.25017v1#bib.bib2)] model, for example, we have directly that

|  |  |  |
| --- | --- | --- |
|  | ℒ​u=−σ22​Δ​u+r​u and F​(u)=(σ22−r)​∇u.\mathcal{L}u=-\frac{\sigma^{2}}{2}\Delta u+ru\quad\text{ and }\quad F(u)=\Big(\frac{\sigma^{2}}{2}-r\Big)\nabla u. |  |

Here rr and σ\sigma are positive parameters that denote the risk-free interest rate and the asset volatility respectively.

More general and more realistic diffusion models also fit in this framework.
Let us consider the Heston [[11](https://arxiv.org/html/2512.25017v1#bib.bib11)] model as an example, where SS denotes the asset price process and VV the variance process.
The option pricing PDE in this model takes the form ([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​u=−∇⋅(A​∇u)+r​u and F​(u)=𝐛⋅∇u,\mathcal{L}u=-\nabla\cdot(A\nabla u)+ru\quad\text{ and }\quad F(u)=\mathbf{b}\cdot\nabla u, |  | (2.3) |

where

|  |  |  |
| --- | --- | --- |
|  | A=V2​[S2η​ρ​Sη​ρ​Sη2] and 𝐛=[(V−r+12​ρ​η)​Sκ​(V−θ)+12​η​ρ​V+η22].A=\frac{V}{2}\begin{bmatrix}S^{2}&\eta\rho S\\ \eta\rho S&\eta^{2}\end{bmatrix}\quad\text{ and }\quad\mathbf{b}=\begin{bmatrix}(V-r+\frac{1}{2}\rho\eta)S\\ \kappa(V-\theta)+\frac{1}{2}\eta\rho V+\frac{\eta^{2}}{2}\end{bmatrix}. |  |

Here, η\eta denotes the volatility of the volatility, ρ\rho the correlation between the Brownian motions driving the asset price and the variance process, θ\theta the long term variance and κ\kappa the reversion rate of the variance to θ\theta.

###### Example 2.4 (Option pricing PIDEs).

Certain classes of partial integro-differential equations (PIDEs) arising in the pricing of financial derivatives can also be casted in this framework, in particular when the integro-differential operator is not “symmetrized”.
Let us consider, for example, the multi-dimensional Merton model as described in Georgoulis et al. [[9](https://arxiv.org/html/2512.25017v1#bib.bib9)].
Then, the PIDE arising for the pricing of basket options can be described using ([2.3](https://arxiv.org/html/2512.25017v1#S2.E3 "Equation 2.3 ‣ Example 2.3 (Option pricing PDEs). ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), where the operator ℒ\mathcal{L} retains the same structure, while the function FF takes now the form

|  |  |  |
| --- | --- | --- |
|  | F​(u)=𝐛⋅∇u−λ​∫ℝd(u​(x​ez)−u​(x))​ν​(d​z),F(u)=\mathbf{b}\cdot\nabla u-\lambda\int\_{\mathbb{R}^{d}}\big(u\left(x\mathrm{e}^{z}\right)-u(x)\big)\nu(\mathrm{d}z), |  |

where ν\nu denotes the multivariate normal density function.

###### Example 2.5 (Allen–Cahn equation).

Park et al. [[25](https://arxiv.org/html/2512.25017v1#bib.bib25)] consider the example of the two-dimensional Allen–Cahn equation:

|  |  |  |
| --- | --- | --- |
|  | ut=Δ​u−ϵ−2​W′​(u),\displaystyle u\_{t}=\Delta u-\epsilon^{-2}W^{\prime}(u), |  |

with appropriate initial and boundary conditions, where WW is a double well potential; for instance, W​(u)=(u2−1)24W(u)=\frac{(u^{2}-1)^{2}}{4}.
Then ℒ​u=−Δ​u+ϵ−2​W′​(u)\mathcal{L}u=-\Delta u+\epsilon^{-2}W^{\prime}(u) and F​(u)=0F(u)=0.

## 3. Convergence of the approximation error

In this section, we show that the approximation error of the deep gradient flow method converges to zero, *i.e.* we consider a neural network with a single layer and prove that as the number of nodes in the network tends to infinity, there exists a neural network that converges to the solution of the PDE. This proof consists of several steps.
First, we show that the problem is well-posed in [Section 3.1](https://arxiv.org/html/2512.25017v1#S3.SS1 "3.1. Well-posedness ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Second, we prove convergence of the time-stepping scheme in [Section 3.2](https://arxiv.org/html/2512.25017v1#S3.SS2 "3.2. Time stepping ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Third, we prove the equivalence between the discretized PDE and the minimization of the variational formulation in [Section 3.3](https://arxiv.org/html/2512.25017v1#S3.SS3 "3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Fourth, we prove a version of the universal approximation theorem (UAT) in [Section 3.4](https://arxiv.org/html/2512.25017v1#S3.SS4 "3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Finally, in [Section 3.5](https://arxiv.org/html/2512.25017v1#S3.SS5 "3.5. Convergence of the minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we deduce the convergence of the neural network approximation to the solution of the minimization problem by utilizing the UAT.

In the sequel, we consider the following Gelfand triple: 𝒱=ℋ01​(ℝd)\mathcal{V}=\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), 𝒱∗=ℋ−1​(ℝd)\mathcal{V}^{\*}=\mathcal{H}^{-1}(\mathbb{R}^{d}) and ℋ=L2​(ℝd)\mathcal{H}=L^{2}(\mathbb{R}^{d}).
Let us consider the PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) and assume that the operators ℒ\mathcal{L} and FF satisfy the following conditions.

###### Assumption (CON).

Assume that the operators ℒ\mathcal{L} and FF satisfy the following inequalities, for any u,v∈ℋ01​(ℝd)u,v\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}),

|  |  |  |
| --- | --- | --- |
|  | |⟨ℒ​u,v⟩ℋ−1,ℋ01|≤M​‖u‖ℋ01​‖v‖ℋ01and‖F​(u)‖L2≤M​‖u‖ℋ01,\displaystyle\left|\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right|\leq M\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}\left\|v\right\|\_{\mathcal{H}\_{0}^{1}}\quad\text{and}\quad\left\|F(u)\right\|\_{L^{2}}\leq M\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}, |  |

where M>0M>0 is a constant.

###### Assumption (GÅ).

The operator ℒ\mathcal{L} satisfies the Gårding inequality, *i.e.* there exist constants λ1>0,λ2≥0\lambda\_{1}>0,\lambda\_{2}\geq 0 such that, for any u∈ℋ01​(ℝd),u\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), holds

|  |  |  |
| --- | --- | --- |
|  | ⟨ℒ​u,u⟩ℋ−1,ℋ01≥λ1​‖u‖ℋ012−λ2​‖u‖L22.\displaystyle\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\geq\lambda\_{1}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-\lambda\_{2}\left\|u\right\|^{2}\_{L^{2}}. |  |

###### Assumption (SA).

The operator ℒ\mathcal{L} is self-adjoint and positive definite.

###### Assumption (LIP).

The operator FF satisfies an estimate of the form

|  |  |  |
| --- | --- | --- |
|  | ‖F​(v)−F​(w)‖ℋ−1≤λ​‖v−w‖ℋ01+μ​‖v−w‖L2,\left\|F(v)-F(w)\right\|\_{\mathcal{H}^{-1}}\leq\lambda\left\|v-w\right\|\_{\mathcal{H}^{1}\_{0}}+\mu\left\|v-w\right\|\_{L^{2}}, |  |

for all v,w∈{v∈ℋ01:minx⁡‖u​(x)−v‖ℋ01≤1}v,w\in\left\{v\in\mathcal{H}\_{0}^{1}:\min\_{x}\left\|u(x)-v\right\|\_{\mathcal{H}^{1}\_{0}}\leq 1\right\}, where λ<1\lambda<1 and μ∈ℝ\mu\in\mathbb{R}.

###### Remark 3.1.

The examples of PDEs considered in the previous section typically satisfy these assumptions.
More details, focusing on the option pricing PDEs of [Examples 2.3](https://arxiv.org/html/2512.25017v1#S2.Thmtheorem3 "Example 2.3 (Option pricing PDEs). ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [2.4](https://arxiv.org/html/2512.25017v1#S2.Thmtheorem4 "Example 2.4 (Option pricing PIDEs). ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), are deferred to [Section A.3](https://arxiv.org/html/2512.25017v1#A1.SS3 "A.3. Examples ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").

### 3.1. Well-posedness

Let us first discuss the existence and uniqueness of solutions for equation ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).

###### Theorem 3.2 (Well-posedness).

Assume that the operators ℒ\mathcal{L} and FF satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), then equation ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) admits a unique weak solution u∈L2​((0,T);ℋ01​(ℝd))∩ℋ1​((0,T);ℋ−1​(ℝd))u\in L^{2}\left(\left(0,T\right);\mathcal{H}\_{0}^{1}(\mathbb{R}^{d})\right)\cap\mathcal{H}^{1}\left(\left(0,T\right);\mathcal{H}^{-1}(\mathbb{R}^{d})\right), that satisfies

|  |  |  |
| --- | --- | --- |
|  | dd​t​⟨u,v⟩L2+⟨ℒ​u,v⟩ℋ−1,ℋ01+⟨F​(u),v⟩L2=0\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}\left\langle u,v\right\rangle\_{L^{2}}+\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+\left\langle F(u),v\right\rangle\_{L^{2}}=0 |  |

for any v∈ℋ01​(ℝd)v\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) and u​(0)=u0u\left(0\right)=u\_{0}.

###### Proof.

According to Hilber et al. [[12](https://arxiv.org/html/2512.25017v1#bib.bib12), Theorem 3.2.2], we only need to verify that the bilinear form ⟨𝒜​u,v⟩ℋ−1,ℋ01\left\langle\mathcal{A}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}} is continuous and satisfies the “Gårding inequality”, where

|  |  |  |
| --- | --- | --- |
|  | ⟨𝒜​u,v⟩ℋ−1,ℋ01=⟨ℒ​u,v⟩ℋ−1,ℋ01+⟨F​(u),v⟩L2.\left\langle\mathcal{A}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}=\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+\left\langle F(u),v\right\rangle\_{L^{2}}. |  |

The continuity follows directly from [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and the Cauchy–Schwarz inequality, since

|  |  |  |  |
| --- | --- | --- | --- |
|  | |⟨𝒜​u,v⟩ℋ−1,ℋ01|\displaystyle\left|\left\langle\mathcal{A}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right| | ≤|⟨ℒ​u,v⟩ℋ−1,ℋ01|+|⟨F​(u),v⟩L2|\displaystyle\leq\left|\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right|+\left|\left\langle F(u),v\right\rangle\_{L^{2}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤M​[‖u‖ℋ01​‖v‖ℋ01+‖u‖ℋ01​‖v‖L2]≤2​M​‖u‖ℋ01​‖v‖ℋ01.\displaystyle\leq M\left[\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}\left\|v\right\|\_{\mathcal{H}\_{0}^{1}}+\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}\left\|v\right\|\_{L^{2}}\right]\leq 2M\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}\left\|v\right\|\_{\mathcal{H}\_{0}^{1}}. |  |

Let us also verify that the bilinear form satisfies the Gårding inequality, *i.e.* that there exist C1,C2>0C\_{1},C\_{2}>0, such that

|  |  |  |
| --- | --- | --- |
|  | |⟨𝒜​u,u⟩ℋ−1,ℋ01|≥C1​‖u‖ℋ012−C2​‖u‖L22.\left|\left\langle\mathcal{A}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right|\geq C\_{1}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-C\_{2}\left\|u\right\|\_{L^{2}}^{2}. |  |

We have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |⟨𝒜​u,u⟩ℋ−1,ℋ01|\displaystyle\left|\left\langle\mathcal{A}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right| | ≥|⟨ℒ​u,u⟩ℋ−1,ℋ01|−|⟨F​(u),u⟩L2|\displaystyle\geq\left|\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right|-\left|\left\langle F(u),u\right\rangle\_{L^{2}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥λ1​‖u‖ℋ012−λ2​‖u‖L22−M​‖u‖ℋ01​‖u‖L2\displaystyle\geq\lambda\_{1}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-\lambda\_{2}\left\|u\right\|^{2}\_{L^{2}}-M\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}\left\|u\right\|\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥λ1​‖u‖ℋ012−λ2​‖u‖L22−M​(λ12​M​‖u‖ℋ012+M2​λ1​‖u‖L22)\displaystyle\geq\lambda\_{1}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-\lambda\_{2}\left\|u\right\|^{2}\_{L^{2}}-M\left(\frac{\lambda\_{1}}{2M}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}+\frac{M}{2\lambda\_{1}}\left\|u\right\|\_{L^{2}}^{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ12​‖u‖ℋ012−(λ2+M22​λ1)​‖u‖L22,\displaystyle=\frac{\lambda\_{1}}{2}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-\left(\lambda\_{2}+\frac{M^{2}}{2\lambda\_{1}}\right)\left\|u\right\|^{2}\_{L^{2}}, |  |

where have used [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and the Cauchy–Schwarz inequality for the second step, and the Young inequality with ε=λ1M\varepsilon=\frac{\lambda\_{1}}{M} for the third step.
∎

### 3.2. Time stepping

The second step is to discretize the PDE in time and prove that this discretization converges to the true solution as the time step tends to zero.
Consider the PDE in formulation ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), *i.e.*

|  |  |  |
| --- | --- | --- |
|  | ut+ℒ​u+F​(u)=0,u​(0)=u0.\displaystyle u\_{t}+\mathcal{L}u+F(u)=0,\quad u(0)=u\_{0}. |  |

Let us divide [0,T][0,T] in KK intervals (tk−1,tk](t\_{k-1},t\_{k}] with step size h=tk−tk−1=1Kh=t\_{k}-t\_{k-1}=\frac{1}{K}.
Let UkU^{k} denote the approximation of u​(tk)u(t\_{k}) using the backward Euler discretization scheme, *i.e.*

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uk−Uk−1h+ℒ​Uk+F​(Uk−1)=0,U0=u0.\frac{U^{k}-U^{k-1}}{h}+\mathcal{L}U^{k}+F\left(U^{k-1}\right)=0,\quad U^{0}=u\_{0}. |  | (3.1) |

###### Theorem 3.3.

Assume that the operators ℒ\mathcal{L} and FF satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), [(SA)](https://arxiv.org/html/2512.25017v1#Thmassumption3 "Assumption (SA). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(LIP)](https://arxiv.org/html/2512.25017v1#Thmassumption4 "Assumption (LIP). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, there exists a constant CC independent of hh and kk such that, for hh sufficiently small, holds

|  |  |  |
| --- | --- | --- |
|  | max0≤k≤K⁡‖u​(tk)−Uk‖L2≤C​h.\max\_{0\leq k\leq K}\left\|u(t\_{k})-U^{k}\right\|\_{L^{2}}\leq Ch. |  |

###### Proof.

The proof follows directly from Theorem 2.1 in Akrivis et al. [[1](https://arxiv.org/html/2512.25017v1#bib.bib1)].
Indeed, using that U0=u​(0)U^{0}=u\left(0\right), we can show by direct, but tedious, calculations that the assumptions of [[1](https://arxiv.org/html/2512.25017v1#bib.bib1), p. 523] are satisfied for λ<1\lambda<1 and q=1q=1.
∎

### 3.3. Weak formulation and uniqueness of minimizer

The third step is to reformulate equation ([3.1](https://arxiv.org/html/2512.25017v1#S3.E1 "Equation 3.1 ‣ 3.2. Time stepping ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) as a variational problem and prove that its solution is equivalent to the minimization of an energy functional.
Let us first rewrite ([3.1](https://arxiv.org/html/2512.25017v1#S3.E1 "Equation 3.1 ‣ 3.2. Time stepping ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Uk−Uk−1)+h​(ℒ​Uk+F​(Uk−1))=0,U0=u0.\left(U^{k}-U^{k-1}\right)+h\left(\mathcal{L}U^{k}+F\left(U^{k-1}\right)\right)=0,\quad U^{0}=u\_{0}. |  | (3.2) |

We want to find an energy functional Ik​(u)I^{k}(u) such that UkU^{k} is a critical point of IkI^{k}.
Consider the following functional IkI^{k} on ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d})

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ik​(u)\displaystyle I^{k}(u) | =12​‖u−Uk−1‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),u⟩L2\displaystyle=\frac{1}{2}\left\|u-U^{k-1}\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),u\right\rangle\_{L^{2}} |  | (3.3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:ℳk(u)+𝒢k(u),\displaystyle=:\mathcal{M}^{k}(u)+\mathcal{G}^{k}(u), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| where | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳk​(u)\displaystyle\mathcal{M}^{k}(u) | =12​‖u‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01\displaystyle=\frac{1}{2}\left\|u\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| and | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢k​(u)\displaystyle\mathcal{G}^{k}(u) | =−⟨u,Uk−1⟩L2+12​‖Uk−1‖L22+h​⟨F​(Uk−1),u⟩L2.\displaystyle=-\left\langle u,U^{k-1}\right\rangle\_{L^{2}}+\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}+h\left\langle F\left(U^{k-1}\right),u\right\rangle\_{L^{2}}. |  |

Here, 𝒢k\mathcal{G}^{k} is a linear functional and ℳk\mathcal{M}^{k} is a nonlinear (quadratic) term.

###### Theorem 3.4.

Assume that the operators ℒ\mathcal{L} and FF satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), [(SA)](https://arxiv.org/html/2512.25017v1#Thmassumption3 "Assumption (SA). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(LIP)](https://arxiv.org/html/2512.25017v1#Thmassumption4 "Assumption (LIP). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and that 0<h<12​λ2,0<h<\frac{1}{2\lambda\_{2}}, where λ2\lambda\_{2} is the constant from [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, the minimizer of ([3.3](https://arxiv.org/html/2512.25017v1#S3.E3 "Equation 3.3 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) is the unique solution of ([3.2](https://arxiv.org/html/2512.25017v1#S3.E2 "Equation 3.2 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}).

The proof of this theorem is based on the following two preparatory results.

###### Lemma 3.5.

Consider the setting of [Theorem 3.4](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, the functional IkI^{k} is bounded from below and, for any w∗∈ℋ01​(ℝd)w\_{\*}\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) and sequence wm⇀ℋ01w∗w\_{m}\xrightharpoonup{\mathcal{H}\_{0}^{1}}w\_{\*}, we have

|  |  |  |
| --- | --- | --- |
|  | lim infm→∞Ik​(wm)≥Ik​(w∗).\displaystyle\liminf\_{m\to\infty}I^{k}\left(w\_{m}\right)\geq I^{k}\left(w\_{\*}\right). |  |

###### Proof.

Let us first prove that IkI^{k} is bounded from below.
Using the Cauchy–Schwarz inequality and the inequality α​β≤α2/4+β2\alpha\beta\leq\alpha^{2}/4+\beta^{2}, we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢k​(u)\displaystyle\mathcal{G}^{k}(u) | ≥−‖Uk−1‖L2​‖u‖L2+12​‖Uk−1‖L22−h​‖F​(Uk−1)‖L2​‖u‖L2\displaystyle\geq-\left\|U^{k-1}\right\|\_{L^{2}}\left\|u\right\|\_{L^{2}}+\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}-h\left\|F\left(U^{k-1}\right)\right\|\_{L^{2}}\left\|u\right\|\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−‖u‖L2​(‖Uk−1‖L2+h​‖F​(Uk−1)‖L2)+12​‖Uk−1‖L22\displaystyle=-\left\|u\right\|\_{L^{2}}\Big(\left\|U^{k-1}\right\|\_{L^{2}}+h\left\|F\left(U^{k-1}\right)\right\|\_{L^{2}}\Big)+\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥−14​‖u‖L22−{‖Uk−1‖L2+h​‖F​(Uk−1)‖L2}2+12​‖Uk−1‖L22.\displaystyle\geq-\frac{1}{4}\left\|u\right\|^{2}\_{L^{2}}-\left\{\left\|U^{k-1}\right\|\_{L^{2}}+h\left\|F\left(U^{k-1}\right)\right\|\_{L^{2}}\right\}^{2}+\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}. |  |

Hence, the functional IkI^{k} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ik​(u)\displaystyle I^{k}(u) | =ℳk​(u)+𝒢k​(u)\displaystyle=\mathcal{M}^{k}(u)+\mathcal{G}^{k}(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥14​‖u‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01−{‖Uk−1‖L2+h​‖F​(Uk−1)‖L2}2+12​‖Uk−1‖L22.\displaystyle\geq\frac{1}{4}\left\|u\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}-\left\{\left\|U^{k-1}\right\|\_{L^{2}}+h\left\|F\left(U^{k-1}\right)\right\|\_{L^{2}}\right\}^{2}+\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}. |  |

Using [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and the condition h<12​λ2h<\frac{1}{2\lambda\_{2}}, we have that Ik​(u)I^{k}(u) is bounded below by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ik​(u)\displaystyle I^{k}(u) | ≥14​‖u‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01−Rk(1)\displaystyle\geq\frac{1}{4}\left\|u\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}-R^{\left(1\right)}\_{k} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥(14−h​λ22)​‖u‖L22+h​λ12​‖u‖ℋ012−Rk(1),\displaystyle\geq\Big(\frac{1}{4}-\frac{h\lambda\_{2}}{2}\Big)\left\|u\right\|^{2}\_{L^{2}}+\frac{h\lambda\_{1}}{2}\left\|u\right\|^{2}\_{\mathcal{H}\_{0}^{1}}-R^{\left(1\right)}\_{k}, |  | (3.4) |

where the term Rk(1)R\_{k}^{(1)}, defined below, is independent of uu and finite

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rk(1):={‖Uk−1‖L2+h​‖F​(Uk−1)‖L2}2−12​‖Uk−1‖L22.\displaystyle R^{\left(1\right)}\_{k}:=\left\{\left\|U^{k-1}\right\|\_{L^{2}}+h\left\|F\left(U^{k-1}\right)\right\|\_{L^{2}}\right\}^{2}-\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}. |  | (3.5) |

As for the second part, consider w∗∈ℋ01​(ℝd)w\_{\*}\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) and a sequence (wm)m(w\_{m})\_{m} such that wm⇀ℋ01w∗w\_{m}\xrightharpoonup{\mathcal{H}\_{0}^{1}}w\_{\*} as m→∞m\to\infty.
Then, by the definition of weak convergence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​⟨wm,w∗⟩L2+h2​⟨ℒ​w∗,wm⟩ℋ−1,ℋ01\displaystyle\frac{1}{2}\left\langle w\_{m},w\_{\*}\right\rangle\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}w\_{\*},w\_{m}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}} | →m→∞12​‖w∗‖L22+h2​⟨ℒ​w∗,w∗⟩ℋ−1,ℋ01,\displaystyle\xrightarrow[\ m\to\infty\ ]{}\frac{1}{2}\left\|w\_{\*}\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}w\_{\*},w\_{\*}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while for the linear part we also have that | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢k​(wm)\displaystyle\mathcal{G}^{k}\left(w\_{m}\right) | →m→∞𝒢k​(w∗).\displaystyle\xrightarrow[\ m\to\infty\ ]{}\mathcal{G}^{k}\left(w\_{\*}\right). |  |

Consider now the functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ik​(wm)+Ik​(w∗)−Ik​(w∗−wm)=⟨wm,w∗⟩L2+h​⟨ℒ​w∗,wm⟩ℋ−1,ℋ01+2​𝒢k​(wm)⏟⟶ 2​Ik​(w∗),\displaystyle I^{k}\left(w\_{m}\right)+I^{k}\left(w\_{\*}\right)-I^{k}\left(w\_{\*}-w\_{m}\right)=\underbrace{\left\langle w\_{m},w\_{\*}\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}w\_{\*},w\_{m}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+2\mathcal{G}^{k}\left(w\_{m}\right)}\_{\longrightarrow\ 2I^{k}\left(w\_{\*}\right)}, |  | (3.6) |

and notice that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳk​(u)=12​‖u‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01≥(12−h​λ22)​‖u‖L22+h​λ12​‖u‖ℋ012≥0,\displaystyle\mathcal{M}^{k}(u)=\frac{1}{2}\left\|u\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\geq\Big(\frac{1}{2}-\frac{h\lambda\_{2}}{2}\Big)\left\|u\right\|^{2}\_{L^{2}}+\frac{h\lambda\_{1}}{2}\left\|u\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\geq 0, |  | (3.7) |

from [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and h<12​λ2h<\frac{1}{2\lambda\_{2}}.
Then, taking the limit as m→∞m\to\infty on both sides of ([3.6](https://arxiv.org/html/2512.25017v1#S3.E6 "Equation 3.6 ‣ Proof. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) and using ([3.7](https://arxiv.org/html/2512.25017v1#S3.E7 "Equation 3.7 ‣ Proof. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), we get that

|  |  |  |
| --- | --- | --- |
|  | lim infm→∞Ik​(wm)+Ik​(w∗)−lim infm→∞Ik​(w∗−wm)⏟≥0≥2​Ik​(w∗),\displaystyle\liminf\_{m\to\infty}I^{k}\left(w\_{m}\right)+I^{k}\left(w\_{\*}\right)-\underbrace{\liminf\_{m\to\infty}I^{k}\left(w\_{\*}-w\_{m}\right)}\_{\geq 0}\geq 2I^{k}\left(w\_{\*}\right), |  |

which implies lim infm→∞Ik​(wm)≥Ik​(w∗)\liminf\_{m\to\infty}I^{k}\left(w\_{m}\right)\geq I^{k}\left(w\_{\*}\right).
∎

###### Proposition 3.6.

Consider the setting of [Theorem 3.4](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Let Uk−1∈ℋ01​(ℝd)U^{k-1}\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), then there exists a unique minimizer in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) of the functional IkI^{k}.

###### Proof.

Let us first show the uniqueness of the minimizer of the functional IkI^{k}.
Let w1,w2∈ℋ01​(ℝd)w\_{1},w\_{2}\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) be two minimizers of IkI^{k} then, using [Assumptions (SA)](https://arxiv.org/html/2512.25017v1#Thmassumption3 "Assumption (SA). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ik​(w1)+Ik​(w2)−2​Ik​(w1+w22)\displaystyle I^{k}\left(w\_{1}\right)+I^{k}\left(w\_{2}\right)-2I^{k}\left(\frac{w\_{1}+w\_{2}}{2}\right) | =14​‖w1−w2‖L22+h4​⟨ℒ​(w1−w2),w1−w2⟩ℋ−1,ℋ01\displaystyle=\frac{1}{4}\left\|w\_{1}-w\_{2}\right\|^{2}\_{L^{2}}+\frac{h}{4}\left\langle\mathcal{L}(w\_{1}-w\_{2}),w\_{1}-w\_{2}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥(14−h​λ24)​‖w1−w2‖L22+h​λ14​‖w1−w2‖ℋ012​≥([3.7](https://arxiv.org/html/2512.25017v1#S3.E7 "Equation 3.7 ‣ Proof. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))​0,\displaystyle\geq\Big(\frac{1}{4}-\frac{h\lambda\_{2}}{4}\Big)\left\|w\_{1}-w\_{2}\right\|^{2}\_{L^{2}}+\frac{h\lambda\_{1}}{4}\left\|w\_{1}-w\_{2}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\overset{\eqref{eq:Mk-positive}}{\geq}0, |  |

which is 0 if and only if w1=w2w\_{1}=w\_{2} almost everywhere. Otherwise, Ik​(w1+w22)I^{k}\left(\frac{w\_{1}+w\_{2}}{2}\right) is smaller than Ik​(w1)I^{k}\left(w\_{1}\right), which is a contradiction.

Next, we show the existence of a minimizer for IkI^{k}.
Define the bounded set ℬk⊂ℋ01​(ℝd)\mathcal{B}^{k}\subset\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) via

|  |  |  |
| --- | --- | --- |
|  | ℬk:={f∈ℋ01​(ℝd)|(14−h​λ22)​‖f‖L22+h​λ12​‖f‖ℋ012≤Rk(1)+12​‖Uk−1‖L22},\displaystyle\mathcal{B}^{k}:=\left\{f\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d})\Big|\ \Big(\frac{1}{4}-\frac{h\lambda\_{2}}{2}\Big)\left\|f\right\|^{2}\_{L^{2}}+\frac{h\lambda\_{1}}{2}\left\|f\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\leq R^{\left(1\right)}\_{k}+\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}\right\}, |  |

where the constant Rk(1)R^{\left(1\right)}\_{k} is defined in ([3.5](https://arxiv.org/html/2512.25017v1#S3.E5 "Equation 3.5 ‣ Proof. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
Consider an f∉ℬkf\notin\mathcal{B}^{k} then, using inequality ([3.3](https://arxiv.org/html/2512.25017v1#S3.Ex24 "Proof. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), we have that Ik​(f)≥12​‖Uk−1‖L22I^{k}\left(f\right)\geq\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}.
Using that 0∈ℬk0\in\mathcal{B}^{k}, Ik​(0)=12​‖Uk−1‖L22I^{k}(0)=\frac{1}{2}\left\|U^{k-1}\right\|^{2}\_{L^{2}}, and that IkI^{k} is bounded from below, we conclude that

|  |  |  |
| --- | --- | --- |
|  | infw∈ℬkIk​(w)=infw∈ℋ01Ik​(w)>−∞.\displaystyle\inf\_{w\in\mathcal{B}^{k}}I^{k}\left(w\right)=\inf\_{w\in\mathcal{H}\_{0}^{1}}I^{k}\left(w\right)>-\infty. |  |

Let us now choose wm∈ℬkw\_{m}\in\mathcal{B}^{k} such that Ik​(wm)→infw∈ℬkIk​(w)I^{k}\left(w\_{m}\right)\to\inf\_{w\in\mathcal{B}^{k}}I^{k}\left(w\right).
Let us also define w∗w\_{\*} as the weak limit of wmw\_{m} in ℋ01\mathcal{H}\_{0}^{1}.
Then, by [Lemma 3.5](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"),

|  |  |  |
| --- | --- | --- |
|  | infw∈ℋ01Ik​(w)=infw∈ℬkIk​(w)=lim infm→∞Ik​(wm)≥Ik​(w∗).\displaystyle\inf\_{w\in\mathcal{H}\_{0}^{1}}I^{k}\left(w\right)=\inf\_{w\in\mathcal{B}^{k}}I^{k}\left(w\right)=\liminf\_{m\to\infty}I^{k}\left(w\_{m}\right)\geq I^{k}\left(w\_{\*}\right). |  |

The last inequality readily implies Ik​(w∗)=infw∈ℋ01Ik​(w)I^{k}\left(w\_{\*}\right)=\inf\_{w\in\mathcal{H}\_{0}^{1}}I^{k}\left(w\right).
∎

###### Proof of [Theorem 3.4](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").

Consider the homogeneous equation

|  |  |  |
| --- | --- | --- |
|  | wh+ℒ​w=0.\frac{w}{h}+\mathcal{L}w=0. |  |

Multiplying with ww on each side and integrating, implies 1h​‖w‖L22+⟨ℒ​w,w⟩ℋ−1,ℋ01=0\frac{1}{h}\left\|w\right\|^{2}\_{L^{2}}+\left\langle\mathcal{L}w,w\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}=0.
Using [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and h<12​λ2h<\frac{1}{2\lambda\_{2}}, yields that w=0.w=0.
Therefore the homogeneous equation only has the solution w=0w=0 in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}).
Thus, the solution of ([3.2](https://arxiv.org/html/2512.25017v1#S3.E2 "Equation 3.2 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) is unique.

Assume that UkU^{k} minimizes IkI^{k}, and let vv be a smooth function.
Consider the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | ik​(τ)=Ik​(Uk+τ​v)\displaystyle i^{k}\left(\tau\right)=I^{k}\left(U^{k}+\tau v\right) | =12​‖Uk+τ​v−Uk−1‖L22\displaystyle=\frac{1}{2}\left\|U^{k}+\tau v-U^{k-1}\right\|^{2}\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +h2​⟨ℒ​(Uk+τ​v),Uk+τ​v⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),Uk+τ​v⟩L2,\displaystyle\quad+\frac{h}{2}\left\langle\mathcal{L}(U^{k}+\tau v),U^{k}+\tau v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),U^{k}+\tau v\right\rangle\_{L^{2}}, |  |

for τ∈ℝ\tau\in\mathbb{R}.
Since UkU^{k} minimizes IkI^{k}, τ=0\tau=0 should minimize iki^{k}.
Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=(ik)′​(0)=\displaystyle 0=\left(i^{k}\right)^{\prime}\left(0\right)= | ⟨Uk−Uk−1,v⟩L2+h2​(⟨ℒ​Uk,v⟩ℋ−1,ℋ01+⟨ℒ​v,Uk⟩ℋ−1,ℋ01)+h​⟨F​(Uk−1),v⟩L2\displaystyle\left\langle U^{k}-U^{k-1},v\right\rangle\_{L^{2}}+\frac{h}{2}\Big(\left\langle\mathcal{L}U^{k},v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+\left\langle\mathcal{L}v,U^{k}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\Big)+h\left\langle F\left(U^{k-1}\right),v\right\rangle\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ⟨Uk−Uk−1,v⟩L2+h​⟨ℒ​Uk,v⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),v⟩L2,\displaystyle\left\langle U^{k}-U^{k-1},v\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}U^{k},v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),v\right\rangle\_{L^{2}}, |  |

where in the last equality we used that ℒ\mathcal{L} is self-adjoint.
This equality must hold for all vv, thus ([3.2](https://arxiv.org/html/2512.25017v1#S3.E2 "Equation 3.2 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) holds.
Finally, note that the second derivative of iki^{k} equals

|  |  |  |
| --- | --- | --- |
|  | (ik)′′​(τ)=‖v‖L22+h​⟨ℒ​v,v⟩ℋ−1,ℋ01≥(1−h​λ2)​‖v‖L22+h​λ1​‖v‖ℋ012>0,\left(i^{k}\right)^{\prime\prime}(\tau)=\left\|v\right\|\_{L^{2}}^{2}+h\left\langle\mathcal{L}v,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\geq(1-h\lambda\_{2})\left\|v\right\|\_{L^{2}}^{2}+h\lambda\_{1}\left\|v\right\|\_{\mathcal{H}\_{0}^{1}}^{2}>0, |  |

where we used [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Therefore, τ=0\tau=0 is indeed the minimizer.
∎

### 3.4. Neural network approximation and a version of the Universal Approximation Theorem

We use a neural network to approximate the solution of the PDE ([3.1](https://arxiv.org/html/2512.25017v1#S3.E1 "Equation 3.1 ‣ 3.2. Time stepping ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) or, more specifically, the solution of the optimization problem minu∈ℋ01⁡Ik​(u)\min\_{u\in\mathcal{H}^{1}\_{0}}I^{k}(u) in ([3.3](https://arxiv.org/html/2512.25017v1#S3.E3 "Equation 3.3 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
The fourth step is to consider a more general problem: show that any function v∈ℋ01​(ℝd)v\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) can be approximated by a neural network.
Hornik [[13](https://arxiv.org/html/2512.25017v1#bib.bib13)] proved that a different class of neural networks, see [Remark 3.10](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem10 "Remark 3.10. ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), is dense in ℋ01​(D)\mathcal{H}\_{0}^{1}\left(D\right), for some bounded domain D⊆ℝdD\subseteq\mathbb{R}^{d}.
However, in our case, the domain equals ℝd\mathbb{R}^{d}, therefore we need a tailor-made version of the Universal Approximation Theorem.

###### Definition 3.7 (Activation function).

An activation function is a function ψ:ℝd→ℝ\psi:\mathbb{R}^{d}\to\mathbb{R} such that ψ∈Cc∞​(ℝd)\psi\in C\_{c}^{\infty}(\mathbb{R}^{d}) and ∫ℝdψ​(x)​dx≠0\int\_{\mathbb{R}^{d}}\psi(x)\mathrm{d}x\neq 0.

###### Definition 3.8 (Neural network).

Let ψ\psi be an activation function, then we define

|  |  |  |
| --- | --- | --- |
|  | 𝒞n​(ψ)={ζ:ℝd→ℝ|ζ​(x)=∑i=1nβi​ψ​(αi​x+ci)},\mathcal{C}^{n}\left(\psi\right)=\left\{\zeta:\mathbb{R}^{d}\to\mathbb{R}\ \big|\ \zeta(x)=\sum\_{i=1}^{n}\beta\_{i}\psi(\alpha\_{i}x+c\_{i})\right\}, |  |

as the class of neural networks with a single hidden layer and nn hidden units.
The vector of weights and biases equals

|  |  |  |
| --- | --- | --- |
|  | θ=(β1,…,βn,α1,…,αn,c1,…,cn)∈ℝn×ℝn×ℝd×n,\theta=\left(\beta\_{1},\dots,\beta\_{n},\alpha\_{1},\dots,\alpha\_{n},c\_{1},\dots,c\_{n}\right)\in\mathbb{R}^{n}\times\mathbb{R}^{n}\times\mathbb{R}^{d\times n}, |  |

with αi≠0\alpha\_{i}\neq 0 for all i∈{1,…,n}i\in\{1,\dots,n\}, thus the dimension of the parameter space equals (2+d)​n\left(2+d\right)n.
Moreover, we set 𝒞​(ψ)=∪n≥1𝒞n​(ψ)\mathcal{C}\left(\psi\right)=\cup\_{n\geq 1}\mathcal{C}^{n}\left(\psi\right).

###### Remark 3.9.

In the sequel, we consider PDEs that take values in ℝd\mathbb{R}^{d}, thus choosing an activation function ψ\psi in Cc∞​(ℝd)C\_{c}^{\infty}(\mathbb{R}^{d}) is convenient.
Then, we require that αi≠0\alpha\_{i}\neq 0, otherwise ψ​(αi​x+ci)\psi\left(\alpha\_{i}x+c\_{i}\right) is a constant, which is not integrable on ℝd\mathbb{R}^{d}.

###### Remark 3.10.

Hornik [[13](https://arxiv.org/html/2512.25017v1#bib.bib13)] introduced a class of neural networks of the form ξ​(x)=∑i=1nβi​ϕ​(ai⋅x+ci)\xi\left(x\right)=\sum\_{i=1}^{n}\beta\_{i}\phi\left(a\_{i}\cdot x+c\_{i}\right) where ϕ:ℝ→ℝ\phi:\mathbb{R}\to\mathbb{R} and ai∈ℝd.a\_{i}\in\mathbb{R}^{d}.
The dimension of the parameter space in this case equals again (2+d)​n\left(2+d\right)n.
However, this kind of neural network does not belong to L2​(ℝd)L^{2}(\mathbb{R}^{d}).
In fact, it is not possible to prove that this class of neural networks is dense in ℋ01​(ℝd),\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), even if ϕ\phi has compact support.
Consider, for example, the case d=2,d=2, set n=1n=1, ϕ=𝟏[−1,1],\phi=\boldsymbol{1}\_{\left[-1,1\right]}, a1=(1,−1)a\_{1}=\left(1,-1\right).
Then ∥ϕ(α1⋅)∥L2=∫ℝ2𝟏|x−y|≤1dxdy,\left\|\phi\left(\alpha\_{1}\cdot\right)\right\|\_{L^{2}}=\int\_{\mathbb{R}^{2}}\boldsymbol{1}\_{\left|x-y\right|\leq 1}\mathrm{d}x\mathrm{d}y, which is the area of an unbounded belt, and therefore equal to +∞.+\infty.

###### Theorem 3.11.

Let ψ\psi be an activation function, then the space of neural networks 𝒞​(ψ)\mathcal{C}\left(\psi\right) is dense in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}).

The proof of this theorem builds on the proof of the next two lemmata.

###### Lemma 3.12.

Let ψ\psi be an activation function.
Let gg be a continuous function, *i.e.* g∈C​(ℝd)g\in C(\mathbb{R}^{d}).
Suppose that, for any ζ∈𝒞​(ψ)\zeta\in\mathcal{C}(\psi), holds ∫ℝdζ​(x)​g​(x)​dx=0\int\_{\mathbb{R}^{d}}\zeta(x)g(x)\mathrm{d}x=0.
Then g=0g=0.

###### Remark 3.13.

Since ψ∈Cc∞​(ℝd)\psi\in C^{\infty}\_{c}(\mathbb{R}^{d}), any function ζ\zeta in 𝒞​(ψ)\mathcal{C}\left(\psi\right) has compact support. Hence ∫ℝdζ​(x)​g​(x)​dx\int\_{\mathbb{R}^{d}}\zeta(x)g(x)\mathrm{d}x is well-defined.

###### Proof.

Let g∈C​(ℝd)g\in C(\mathbb{R}^{d}), x∈ℝdx\in\mathbb{R}^{d}, 0<ε≤10<{\varepsilon}\leq 1, and define

|  |  |  |
| --- | --- | --- |
|  | Φε​(g)​(x):=∫ℝdε−d​ψ​(x−yε)​g​(y)​dy.\Phi^{\varepsilon}\left(g\right)(x):=\int\_{\mathbb{R}^{d}}{\varepsilon}^{-d}\psi\left(\frac{x-y}{{\varepsilon}}\right)g\left(y\right)\mathrm{d}y. |  |

We would like to show that

|  |  |  |
| --- | --- | --- |
|  | limε→0Φε​(g)​(x)=c​g​(x),\lim\_{{\varepsilon}\to 0}\Phi^{\varepsilon}\left(g\right)(x)=cg(x), |  |

where c=−∫ℝdψ​(x)​dxc=-\int\_{\mathbb{R}^{d}}\psi(x)\mathrm{d}x.
Using a change of variables twice, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φε​(g)​(x)\displaystyle\Phi^{\varepsilon}\left(g\right)(x) | =∫ℝdε−d​ψ​(x−yε)​g​(y)​dy=z=x−y−∫ℝdε−d​ψ​(zε)​g​(x−z)​dz\displaystyle=\int\_{\mathbb{R}^{d}}{\varepsilon}^{-d}\psi\left(\frac{x-y}{{\varepsilon}}\right)g\left(y\right)\mathrm{d}y\stackrel{{\scriptstyle z=x-y}}{{=}}-\int\_{\mathbb{R}^{d}}{\varepsilon}^{-d}\psi\left(\frac{z}{{\varepsilon}}\right)g\left(x-z\right)\mathrm{d}z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =m=ε−1​z−∫ℝdψ​(m)​g​(x−ε​m)​dm=−∫Kψ​(m)​g​(x−ε​m)​dm,\displaystyle\stackrel{{\scriptstyle m={\varepsilon}^{-1}z}}{{=}}-\int\_{\mathbb{R}^{d}}\psi\left(m\right)g\left(x-{\varepsilon}m\right)\mathrm{d}m=-\int\_{K}\psi\left(m\right)g\left(x-{\varepsilon}m\right)\mathrm{d}m, |  |

where KK denotes the (compact) support of ψ\psi.
Notice that, since zz is a vector, we have that m=zεm=\frac{z}{{\varepsilon}} yields d​m=ε−d​d​z\mathrm{d}m={\varepsilon}^{-d}\mathrm{d}z.
Then, using the dominated convergence theorem, we get that

|  |  |  |
| --- | --- | --- |
|  | limε→0Φε​(g)​(x)=limε→0{−∫Kψ​(m)​g​(x−ε​m)​dm}=c​g​(x).\displaystyle\lim\_{{\varepsilon}\to 0}\Phi^{\varepsilon}\left(g\right)(x)=\lim\_{{\varepsilon}\to 0}\Big\{-\int\_{K}\psi\left(m\right)g\left(x-{\varepsilon}m\right)\mathrm{d}m\Big\}=cg(x). |  |

Now, consider any ζ∈𝒞​(ψ)\zeta\in\mathcal{C}\left(\psi\right) such that ∫ℝdζ​(y)​g​(y)​dy=0\int\_{\mathbb{R}^{d}}\zeta(y)g(y)\mathrm{d}y=0; then, for any x∈ℝdx\in\mathbb{R}^{d}, setting n=1n=1, β=ε−d\beta={\varepsilon}^{-d}, α=ε−1\alpha={\varepsilon}^{-1} and c=xεc=\frac{x}{{\varepsilon}} in the definition of 𝒞​(ψ)\mathcal{C}\left(\psi\right), we get that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdε−d​ψ​(x−yε)​g​(y)​dy=0.\int\_{\mathbb{R}^{d}}{\varepsilon}^{-d}\psi\left(\frac{x-y}{{\varepsilon}}\right)g\left(y\right)\mathrm{d}y=0. |  |

We conclude the proof by sending ε→0{\varepsilon}\to 0 and using that c≠0c\neq 0, by definition of an activation function.
∎

###### Lemma 3.14.

Let ww be a function on C∞​(ℝd)C^{\infty}(\mathbb{R}^{d}) with support on the unit sphere, where

|  |  |  |
| --- | --- | --- |
|  | w(x)={c​exp⁡(−11−|x|2),if |x|<1,0,if |x|≥1,w(x)=\left\{\begin{aligned} c\exp\left(\frac{-1}{1-\left|x\right|^{2}}\right),\quad&\text{if $\left|x\right|<1$},\\ 0,\quad&\text{if $\left|x\right|\geq 1$,}\end{aligned}\right. |  |

where cc is a constant such that the integral of ww equals 11.
Let f∈L*loc*1​(ℝd)f\in L^{1}\_{\emph{loc}}(\mathbb{R}^{d}), and introduce

|  |  |  |
| --- | --- | --- |
|  | Jε​f​(x)=wε∗f​(x)=∫ℝdwε​(y)​f​(x−y)​dy,J^{\varepsilon}f(x)=w\_{\varepsilon}\*f(x)=\int\_{\mathbb{R}^{d}}w\_{\varepsilon}\left(y\right)f\left(x-y\right)\mathrm{d}y, |  |

with wε=ε−d​w​(xε)w\_{\varepsilon}={\varepsilon}^{-d}w\left(\frac{x}{{\varepsilon}}\right).
Then, for any φ∈Cc∞\varphi\in C^{\infty}\_{c} and f∈L*loc*1​(ℝd)f\in L^{1}\_{\emph{loc}}(\mathbb{R}^{d}), we have that

|  |  |  |
| --- | --- | --- |
|  | limε→0⟨φ,Jε​f⟩L2=⟨φ,f⟩L2.\displaystyle\lim\_{{\varepsilon}\to 0}\left\langle\varphi,J^{\varepsilon}f\right\rangle\_{L^{2}}=\left\langle\varphi,f\right\rangle\_{L^{2}}. |  |

###### Remark 3.15.

The convolution of wεw\_{\varepsilon} with ff is convenient, because then Jε​fJ^{\varepsilon}f is infinitely differentiable.

###### Proof.

Let us first rewrite ⟨φ,Jε​f⟩L2\left\langle\varphi,J^{\varepsilon}f\right\rangle\_{L^{2}} as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨φ,Jε​f⟩L2\displaystyle\left\langle\varphi,J^{\varepsilon}f\right\rangle\_{L^{2}} | =∫ℝd∫ℝdφ​(x)​wε​(y)​f​(x−y)​dy​dx=ε−d​∫ℝd∫ℝdφ​(x)​w​(yε)​f​(x−y)​dy​dx\displaystyle=\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\varphi(x)w\_{\varepsilon}\left(y\right)f\left(x-y\right)\mathrm{d}y\mathrm{d}x={\varepsilon}^{-d}\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\varphi(x)w\left(\frac{y}{{\varepsilon}}\right)f\left(x-y\right)\mathrm{d}y\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =z=y/ε∫ℝd∫ℝdφ​(x)​w​(z)​f​(x−ε​z)​dz​dx=∫K∫Kφ​(x)​w​(z)​f​(x−ε​z)​dz​dx\displaystyle\stackrel{{\scriptstyle z=y/{\varepsilon}}}{{=}}\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\varphi(x)w\left(z\right)f\left(x-{\varepsilon}z\right)\mathrm{d}z\mathrm{d}x=\int\_{K}\int\_{K}\varphi(x)w\left(z\right)f\left(x-{\varepsilon}z\right)\mathrm{d}z\mathrm{d}x |  |

where KK is a compact set that contains the support of ww and φ\varphi.
Hence, by the dominated convergence theorem and Lusin’s theorem, letting ε→0{\varepsilon}\to 0 and using that the integral of ww equals 1, we have

|  |  |  |
| --- | --- | --- |
|  | limε→0⟨φ,Jε​f⟩L2=limε→0∫K∫Kφ​(x)​w​(z)​f​(x−ε​z)​dz​dx=⟨φ,f⟩L2.∎\lim\_{{\varepsilon}\to 0}\left\langle\varphi,J^{\varepsilon}f\right\rangle\_{L^{2}}=\lim\_{{\varepsilon}\to 0}\int\_{K}\int\_{K}\varphi(x)w\left(z\right)f\left(x-{\varepsilon}z\right)\mathrm{d}z\mathrm{d}x=\left\langle\varphi,f\right\rangle\_{L^{2}}.\qed |  |

###### Proof of [Theorem 3.11](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").

Observe that 𝒞​(ψ)⊂ℋ01​(ℝd)\mathcal{C}\left(\psi\right)\subset\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), since ψ∈Cc∞​(ℝd)\psi\in C^{\infty}\_{c}(\mathbb{R}^{d}). Assume that 𝒞​(ψ)\mathcal{C}\left(\psi\right) is not dense in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) then, as a corollary of the Hahn–Banach extension theorem, see e.g. van Neerven [[30](https://arxiv.org/html/2512.25017v1#bib.bib30), Corollary 4.12], there exists a non-zero continuous linear functional GG on ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) such that for any ζ∈𝒞​(ψ)\zeta\in\mathcal{C}\left(\psi\right),

|  |  |  |
| --- | --- | --- |
|  | G​(ζ)=0.\displaystyle G\left(\zeta\right)=0. |  |

Using the Riesz representation theorem, there exists a g≠0g\neq 0 in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), such that for any f∈ℋ01​(ℝd)f\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}),

|  |  |  |
| --- | --- | --- |
|  | ⟨f,g⟩ℋ01​(ℝd)=G​(f).\left\langle f,g\right\rangle\_{\mathcal{H}\_{0}^{1}(\mathbb{R}^{d})}=G\left(f\right). |  |

Therefore ⟨ζ,g⟩L2+⟨∇ζ,∇g⟩L2=0\left\langle\zeta,g\right\rangle\_{L^{2}}+\left\langle\nabla\zeta,\nabla g\right\rangle\_{L^{2}}=0.
Let us denote g1ε=Jε​gg^{\varepsilon}\_{1}=J^{\varepsilon}g and g2ε=Jε​∇gg^{\varepsilon}\_{2}=J^{\varepsilon}\nabla g, for convenience.
Consider the inner product of these functions with ζ\zeta, then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ζ,g1ε⟩L2\displaystyle\left\langle\zeta,g^{\varepsilon}\_{1}\right\rangle\_{L^{2}} | +⟨∇ζ,g2ε⟩L2\displaystyle+\left\langle\nabla\zeta,g^{\varepsilon}\_{2}\right\rangle\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ℝd∫ℝdζ​(x)​wε​(y)​g​(x−y)​dy​dx+∫ℝd∫ℝd∇ζ​(x)⋅[wε​(y)​∇g​(x−y)]​dy​dx\displaystyle=\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\zeta(x)w\_{\varepsilon}\left(y\right)g\left(x-y\right)\mathrm{d}y\mathrm{d}x+\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\nabla\zeta(x)\cdot\left[w\_{\varepsilon}\left(y\right)\nabla g\left(x-y\right)\right]\mathrm{d}y\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ℝd(∫ℝdζ​(x)​g​(x−y)​dx)​wε​(y)​dy+∫ℝd(∫ℝd∇ζ​(x)⋅∇g​(x−y)​dx)​wε​(y)​dy\displaystyle=\int\_{\mathbb{R}^{d}}\left(\int\_{\mathbb{R}^{d}}\zeta(x)g\left(x-y\right)\mathrm{d}x\right)w\_{\varepsilon}\left(y\right)\mathrm{d}y+\int\_{\mathbb{R}^{d}}\left(\int\_{\mathbb{R}^{d}}\nabla\zeta(x)\cdot\nabla g\left(x-y\right)\mathrm{d}x\right)w\_{\varepsilon}\left(y\right)\mathrm{d}y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x=z+y∫ℝd(∫ℝdζ​(z+y)​g​(z)​𝑑z)​wε​(y)​dy+∫ℝd(∫ℝd∇ζ​(z+y)⋅∇g​(z)​𝑑z)​wε​(y)​dy\displaystyle\stackrel{{\scriptstyle x=z+y}}{{=}}\int\_{\mathbb{R}^{d}}\left(\int\_{\mathbb{R}^{d}}\zeta\left(z+y\right)g\left(z\right)dz\right)w\_{\varepsilon}\left(y\right)\mathrm{d}y+\int\_{\mathbb{R}^{d}}\left(\int\_{\mathbb{R}^{d}}\nabla\zeta\left(z+y\right)\cdot\nabla g\left(z\right)dz\right)w\_{\varepsilon}\left(y\right)\mathrm{d}y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ℝd{⟨ζ(⋅+y),g⟩L2+⟨∇ζ(⋅+y),∇g⟩L2}wε(y)dy=0.\displaystyle=\int\_{\mathbb{R}^{d}}\Big\{\left\langle\zeta\left(\cdot+y\right),g\right\rangle\_{L^{2}}+\left\langle\nabla\zeta\left(\cdot+y\right),\nabla g\right\rangle\_{L^{2}}\Big\}\,w\_{\varepsilon}\left(y\right)\mathrm{d}y=0. |  |

Since ζ∈𝒞​(ψ)\zeta\in\mathcal{C}\left(\psi\right), it has compact support and we can apply Fubini’s theorem in the second step, while we can also use that ζ(⋅+y)∈𝒞(ψ)\zeta\left(\cdot+y\right)\in\mathcal{C}\left(\psi\right) in the last step.
Hence ⟨ζ,g1ε⟩L2+⟨∇ζ,g2ε⟩L2=0\left\langle\zeta,g^{\varepsilon}\_{1}\right\rangle\_{L^{2}}+\left\langle\nabla\zeta,g^{\varepsilon}\_{2}\right\rangle\_{L^{2}}=0.
Then, using integration by parts,

|  |  |  |
| --- | --- | --- |
|  | ⟨ζ,g1ε−∇⋅(g2ε)⟩L2=0.\displaystyle\left\langle\zeta,g^{\varepsilon}\_{1}-\nabla\cdot\left(g^{\varepsilon}\_{2}\right)\right\rangle\_{L^{2}}=0. |  |

Since g1ε−∇⋅(g2ε)g^{\varepsilon}\_{1}-\nabla\cdot\left(g^{\varepsilon}\_{2}\right) is continuous, see e.g. van Neerven [[30](https://arxiv.org/html/2512.25017v1#bib.bib30), Proposition 11.1], by [Lemma 3.12](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem12 "Lemma 3.12. ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we conclude that g1ε−∇⋅(g2ε)=0g^{\varepsilon}\_{1}-\nabla\cdot\left(g^{\varepsilon}\_{2}\right)=0.
Then, for any f∈Cc∞​(ℝd)f\in C^{\infty}\_{c}(\mathbb{R}^{d}),

|  |  |  |
| --- | --- | --- |
|  | ⟨f,g1ε⟩L2+⟨∇f,g2ε⟩L2=⟨f,g1ε−∇⋅(g2ε)⟩L2=0.\left\langle f,g^{\varepsilon}\_{1}\right\rangle\_{L^{2}}+\left\langle\nabla f,g^{\varepsilon}\_{2}\right\rangle\_{L^{2}}=\left\langle f,g^{\varepsilon}\_{1}-\nabla\cdot\left(g^{\varepsilon}\_{2}\right)\right\rangle\_{L^{2}}=0. |  |

Using [Lemma 3.14](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem14 "Lemma 3.14. ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), for any f∈Cc∞​(ℝd)f\in C^{\infty}\_{c}(\mathbb{R}^{d}), we get that

|  |  |  |
| --- | --- | --- |
|  | G​(f)=⟨f,g⟩L2+⟨∇f,∇g⟩L2=limε→0⟨f,g1ε⟩L2+⟨∇f,g2ε⟩L2=0.\displaystyle G\left(f\right)=\left\langle f,g\right\rangle\_{L^{2}}+\left\langle\nabla f,\nabla g\right\rangle\_{L^{2}}=\lim\_{{\varepsilon}\to 0}\left\langle f,g^{\varepsilon}\_{1}\right\rangle\_{L^{2}}+\left\langle\nabla f,g^{\varepsilon}\_{2}\right\rangle\_{L^{2}}=0. |  |

Since Cc∞​(ℝd)C^{\infty}\_{c}(\mathbb{R}^{d}) is dense in ℋ01\mathcal{H}\_{0}^{1} with norm ∥⋅∥ℋ01\left\|\cdot\right\|\_{\mathcal{H}\_{0}^{1}}, GG is a zero functional on ℋ01\mathcal{H}\_{0}^{1}, which is a contradiction.
∎

### 3.5. Convergence of the minimizer

The final step, is to show that the minimizer approximated by neural networks converges to the solution of the PDE, which yields that the approximation error of the method converges to zero.
[Theorem 3.4](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") yields that the minimizer of the functional IkI^{k} in ([3.3](https://arxiv.org/html/2512.25017v1#S3.E3 "Equation 3.3 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) equals the unique solution of discretized equation ([3.2](https://arxiv.org/html/2512.25017v1#S3.E2 "Equation 3.2 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
Here, we show that this minimizer can be approximated by a neural network as defined in [Definition 3.8](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem8 "Definition 3.8 (Neural network). ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
The final conclusion, *i.e.* the convergence to the true solution of PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), follows by an application of [Theorem 3.3](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.2. Time stepping ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), which shows that the time-stepping scheme converges to the PDE.

###### Theorem 3.16.

Let (wm)m∈ℕ(w\_{m})\_{m\in\mathbb{N}} be a sequence in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) and w∗w\_{\*} be the minimizer of IkI^{k}. Then

|  |  |  |
| --- | --- | --- |
|  | limm→∞‖wm−w∗‖ℋ01=0 if and only if limm→∞Ik​(wm)=Ik​(w∗).\lim\_{m\to\infty}\left\|w\_{m}-w\_{\*}\right\|\_{\mathcal{H}^{1}\_{0}}=0\quad\text{ if and only if }\quad\lim\_{m\to\infty}I^{k}\left(w\_{m}\right)=I^{k}\left(w\_{\*}\right). |  |

###### Remark 3.17.

Therefore, we can select the approximation sequence (wm)(w\_{m}) from the space of neural networks 𝒞​(ψ)\mathcal{C}\left(\psi\right).
Using that 𝒞​(ψ)\mathcal{C}\left(\psi\right) is dense in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), an approximation sequence always exists.

###### Remark 3.18.

Let us point out that for an arbitrary u∈ℋ01​(ℝd)u\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), |Ik​(um)−Ik​(u)|→0\left|I^{k}\left(u\_{m}\right)-I^{k}(u)\right|\to 0, does not imply ‖um−u‖L2→0\left\|u\_{m}-u\right\|\_{L^{2}}\to 0.
Consider, for example, F=0F=0, then IkI^{k} is quadratic and we can always choose um=−uu\_{m}=-u since Ik​(u)=Ik​(−u)I^{k}(u)=I^{k}\left(-u\right).

###### Proposition 3.19 (Continuity).

Assume that the operators ℒ\mathcal{L} and FF satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(SA)](https://arxiv.org/html/2512.25017v1#Thmassumption3 "Assumption (SA). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), then the functional IkI^{k} is continuous, *i.e.* for any f,u∈ℋ01​(ℝd)f,u\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}), holds

|  |  |  |
| --- | --- | --- |
|  | |Ik​(f)−Ik​(u)|≤(1+h​M)​‖f−u‖ℋ01​(‖f+u‖ℋ01+‖Uk−1‖ℋ01).\displaystyle\big|I^{k}\left(f\right)-I^{k}(u)\big|\leq\left(1+hM\right)\left\|f-u\right\|\_{\mathcal{H}\_{0}^{1}}\left(\left\|f+u\right\|\_{\mathcal{H}\_{0}^{1}}+\left\|U^{k-1}\right\|\_{\mathcal{H}\_{0}^{1}}\right). |  |

###### Proof.

Using the definition of the energy functional in ([3.3](https://arxiv.org/html/2512.25017v1#S3.E3 "Equation 3.3 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) and that ℒ\mathcal{L} is linear and self-adjoint, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Ik​(f)−Ik​(u)|\displaystyle\big|I^{k}\left(f\right)-I^{k}(u)\big| | =|12‖​f−Uk−1∥L22+h2​⟨ℒ​f,f⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),f⟩L2\displaystyle=\left|\frac{1}{2}\left\|f-U^{k-1}\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}f,f\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),f\right\rangle\_{L^{2}}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12∥u−Uk−1∥L22−h2⟨ℒu,u⟩ℋ−1,ℋ01−h⟨F(Uk−1),u⟩L2|\displaystyle\qquad\left.-\frac{1}{2}\left\|u-U^{k-1}\right\|^{2}\_{L^{2}}-\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}-h\left\langle F\left(U^{k-1}\right),u\right\rangle\_{L^{2}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​|‖f‖L22−‖u‖L22−2​⟨f−u,Uk−1⟩L2⏟=⟨f−u,f+u−2​Uk+1⟩|\displaystyle\leq\frac{1}{2}\Big|\underbrace{\left\|f\right\|^{2}\_{L^{2}}-\left\|u\right\|^{2}\_{L^{2}}-2\left\langle f-u,U^{k-1}\right\rangle\_{L^{2}}}\_{=\left\langle f-u,f+u-2U^{k+1}\right\rangle}\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +h2​|⟨ℒ​(f−u),f+u⟩ℋ−1,ℋ01|+h​|⟨F​(Uk−1),f−u⟩L2|\displaystyle\quad+\frac{h}{2}\left|\left\langle\mathcal{L}(f-u),f+u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right|+h\left|\left\langle F\left(U^{k-1}\right),f-u\right\rangle\_{L^{2}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤CS12​‖f−u‖L2​‖f+u−2​Uk−1‖L2+h2​|⟨ℒ​(f−u),f+u⟩ℋ−1,ℋ01|\displaystyle\stackrel{{\scriptstyle\text{CS}}}{{\leq}}\frac{1}{2}\left\|f-u\right\|\_{L^{2}}\left\|f+u-2U^{k-1}\right\|\_{L^{2}}+\frac{h}{2}\left|\left\langle\mathcal{L}(f-u),f+u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +h​|⟨F​(Uk−1),f−u⟩L2|.\displaystyle\quad+h\left|\left\langle F\left(U^{k-1}\right),f-u\right\rangle\_{L^{2}}\right|. |  | (3.8) |

Moreover, using [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and the Cauchy–Schwarz inequality again, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | h2​|⟨ℒ​(f−u),f+u⟩ℋ−1,ℋ01|\displaystyle\frac{h}{2}\left|\left\langle\mathcal{L}(f-u),f+u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right| | +h​|⟨F​(Uk−1),f−u⟩L2|\displaystyle+h\left|\left\langle F\left(U^{k-1}\right),f-u\right\rangle\_{L^{2}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h​M2​‖f−u‖ℋ01​‖f+u‖ℋ01+h​M​‖Uk−1‖ℋ01​‖f−u‖L2\displaystyle\leq\frac{hM}{2}\left\|f-u\right\|\_{\mathcal{H}\_{0}^{1}}\left\|f+u\right\|\_{\mathcal{H}\_{0}^{1}}+hM\left\|U^{k-1}\right\|\_{\mathcal{H}\_{0}^{1}}\left\|f-u\right\|\_{L^{2}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤h​M​(‖f+u‖ℋ01+‖Uk−1‖ℋ01)​‖f−u‖ℋ01,\displaystyle\leq hM\left(\left\|f+u\right\|\_{\mathcal{H}\_{0}^{1}}+\left\|U^{k-1}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\left\|f-u\right\|\_{\mathcal{H}\_{0}^{1}}, |  | (3.9) |

while from the triangle inequality, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​‖f−u‖L2​‖f+u−2​Uk−1‖L2≤‖f−u‖ℋ01​(‖f+u‖ℋ01+‖Uk−1‖ℋ01).\displaystyle\frac{1}{2}\left\|f-u\right\|\_{L^{2}}\left\|f+u-2U^{k-1}\right\|\_{L^{2}}\leq\left\|f-u\right\|\_{\mathcal{H}\_{0}^{1}}\left(\left\|f+u\right\|\_{\mathcal{H}\_{0}^{1}}+\left\|U^{k-1}\right\|\_{\mathcal{H}\_{0}^{1}}\right). |  | (3.10) |

Replacing ([3.5](https://arxiv.org/html/2512.25017v1#S3.Ex70 "Proof. ‣ 3.5. Convergence of the minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) and ([3.10](https://arxiv.org/html/2512.25017v1#S3.E10 "Equation 3.10 ‣ Proof. ‣ 3.5. Convergence of the minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) into ([3.5](https://arxiv.org/html/2512.25017v1#S3.Ex65 "Proof. ‣ 3.5. Convergence of the minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) completes the proof.
∎

###### Proof of [Theorem 3.16](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem16 "Theorem 3.16. ‣ 3.5. Convergence of the minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").

Assume that ‖wm−w∗‖ℋ01→0\left\|w\_{m}-w\_{\*}\right\|\_{\mathcal{H}\_{0}^{1}}\to 0.
Then, the sequence ‖wm−w∗‖ℋ01\left\|w\_{m}-w\_{\*}\right\|\_{\mathcal{H}\_{0}^{1}} is bounded by some constant C>0C>0.
Using [Proposition 3.19](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem19 "Proposition 3.19 (Continuity). ‣ 3.5. Convergence of the minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we get that

|  |  |  |
| --- | --- | --- |
|  | |Ik​(wm)−Ik​(w∗)|≤‖wm−w∗‖ℋ01​C​(1+‖Uk−1‖ℋ01)→0.\displaystyle\left|I^{k}\left(w\_{m}\right)-I^{k}\left(w\_{\*}\right)\right|\leq\left\|w\_{m}-w\_{\*}\right\|\_{\mathcal{H}\_{0}^{1}}C\left(1+\left\|U^{k-1}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\to 0. |  |

Thus Ik​(wm)→Ik​(w∗)I^{k}\left(w\_{m}\right)\to I^{k}\left(w\_{\*}\right).

Next, we prove that Ik​(wm)→Ik​(w∗)I^{k}\left(w\_{m}\right)\to I^{k}\left(w\_{\*}\right) implies that wm→w∗w\_{m}\to w\_{\*} in ℋ01\mathcal{H}\_{0}^{1}.
Let us first notice that wm⇀w∗w\_{m}\rightharpoonup w\_{\*}.
Otherwise, there exists a subsequence (wmi)(w\_{m\_{i}}), an ε>0{\varepsilon}>0 and a nonzero functional ff such that |f​[wmi]−f​[w∗]|≥ε\left|f\left[w\_{m\_{i}}\right]-f\left[w\_{\*}\right]\right|\geq{\varepsilon}.
Since (wmi)(w\_{m\_{i}}) is bounded in ℋ01\mathcal{H}\_{0}^{1} (otherwise Ik​(wmi)I^{k}\left(w\_{m\_{i}}\right) is unbounded), it is pre-weakly compact (which means it has a weakly convergent subsequence, see e.g. van Neerven [[30](https://arxiv.org/html/2512.25017v1#bib.bib30), Corollary 4.56]).
Let us denote one of its weak limits by w∗∗w\_{\*\*}.
Using [Lemma 3.5](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), Ik​(w∗)=limi→∞Ik​(wmi)≥Ik​(w∗∗)I^{k}\left(w\_{\*}\right)=\lim\_{i\to\infty}I^{k}\left(w\_{m\_{i}}\right)\geq I^{k}\left(w\_{\*\*}\right).
This inequality implies w∗=w∗∗w\_{\*}=w\_{\*\*} by the uniqueness of the minimizer.
Hence wm⇀w∗w\_{m}\rightharpoonup w\_{\*}, a contradiction with |f​[wmi]−f​[w∗]|≥ε\left|f\left[w\_{m\_{i}}\right]-f\left[w\_{\*}\right]\right|\geq{\varepsilon}.
Therefore, wm⇀w∗w\_{m}\rightharpoonup w\_{\*}.

Now, since Ik​(wm)→Ik​(w∗)I^{k}\left(w\_{m}\right)\to I^{k}\left(w\_{\*}\right), 𝒢n​(wm)→𝒢n​(w∗)\mathcal{G}^{n}(w\_{m})\to\mathcal{G}^{n}(w\_{\*}), and ℳk​(wm)→ℳk​(w∗)\mathcal{M}^{k}\left(w\_{m}\right)\to\mathcal{M}^{k}\left(w\_{\*}\right), we have that

|  |  |  |
| --- | --- | --- |
|  | 12​‖wm‖L22+h2​⟨ℒ​wm,wm⟩ℋ−1,ℋ01→12​‖w∗‖L22+h2​⟨ℒ​w∗,w∗⟩ℋ−1,ℋ01.\displaystyle\frac{1}{2}\left\|w\_{m}\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}w\_{m},w\_{m}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\to\frac{1}{2}\left\|w\_{\*}\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}w\_{\*},w\_{\*}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}. |  |

This convergence implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | (12−h​λ22)​‖wm−w∗‖L22\displaystyle\left(\frac{1}{2}-\frac{h\lambda\_{2}}{2}\right)\left\|w\_{m}-w\_{\*}\right\|^{2}\_{L^{2}} | +h​λ22​‖wm−w∗‖ℋ012\displaystyle+\frac{h\lambda\_{2}}{2}\left\|w\_{m}-w\_{\*}\right\|^{2}\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​‖wm−w∗‖L22+h2​⟨ℒ​(wm−w∗),wm−w∗⟩ℋ−1,ℋ01→0,\displaystyle\leq\frac{1}{2}\left\|w\_{m}-w\_{\*}\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}(w\_{m}-w\_{\*}),w\_{m}-w\_{\*}\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\to 0, |  |

since wm⇀w∗w\_{m}\rightharpoonup w\_{\*}.
Therefore, by [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we conclude ‖wm−w∗‖ℋ01→0\left\|w\_{m}-w\_{\*}\right\|\_{\mathcal{H}\_{0}^{1}}\to 0.
∎

## 4. Convergence of the training error

In this section, we show that for each fixed time step kk, the trained neural network converges to the true solution of the discretized PDE ([3.1](https://arxiv.org/html/2512.25017v1#S3.E1 "Equation 3.1 ‣ 3.2. Time stepping ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) as the number of neurons and the training time tend to infinity.
Therefore, using the convergence of the time-stepping scheme, we can conclude the convergence of the training error.

### 4.1. Convergence of the trained neural network

In this subsection, we analyze the training of the neural network for the deep gradient flow method as a function of the number of neurons nn.
In particular, we would like to study the training process of the parameters θn\theta^{n} as n→∞n\to\infty, such that the neural network introduced in [Definition 3.8](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem8 "Definition 3.8 (Neural network). ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") approximates the solution of the discretized PDE ([3.1](https://arxiv.org/html/2512.25017v1#S3.E1 "Equation 3.1 ‣ 3.2. Time stepping ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
We show that this process satisfies a gradient flow equation as the number of neurons tends to infinity, *i.e.* in the so-called “wide network limit”.

Let us denote the parameters of the neural network by θn=(βi,αi,ci)i=1n∈ℝn×ℝn×ℝd×n\theta^{n}=\left(\beta^{i},\alpha^{i},c^{i}\right)^{n}\_{i=1}\in\mathbb{R}^{n}\times\mathbb{R}^{n}\times\mathbb{R}^{d\times n}.
Moreover, for 12<δ<1\frac{1}{2}<\delta<1, let us introduce a neural network

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn​(θn;x)\displaystyle V^{n}\left(\theta^{n};x\right) | =1nδ​∑i=1nβ^i,n​ψ​(α^i,n​x+c^i,n),\displaystyle=\frac{1}{n^{\delta}}\sum\_{i=1}^{n}\hat{\beta}^{i,n}\psi\left(\hat{\alpha}^{i,n}x+\hat{c}^{i,n}\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| in accordance with [Definition 3.8](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem8 "Definition 3.8 (Neural network). ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), where the “clipped” parameters are defined as follows: | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | α^i,n\displaystyle\hat{\alpha}^{i,n} | ={(rn∧αi)∨1rn,for ​αi>0,(−1rn∧αi)∨(−rn),for ​αi<0,\displaystyle=\begin{cases}\begin{aligned} \left(r\_{n}\land\alpha^{i}\right)\lor\frac{1}{r\_{n}},\quad&\text{for }\alpha^{i}>0,\\ \left(\frac{-1}{r\_{n}}\land\alpha^{i}\right)\lor(-r\_{n}),\quad&\text{for }\alpha^{i}<0,\end{aligned}\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | β^i,n\displaystyle\hat{\beta}^{i,n} | =(rn∧βi)∨(−rn),\displaystyle=\left(r\_{n}\land\beta^{i}\right)\lor(-r\_{n}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c^i,n\displaystyle\hat{c}^{i,n} | =(rn∧ci)∨(−rn),\displaystyle=\left(r\_{n}\land c^{i}\right)\lor(-r\_{n}), |  |

for some rnr\_{n} increasing with nn. We restrict the domain of the parameters (βi,αi,ci)(\beta^{i},\alpha^{i},c^{i}) to [−rn,rn][-r\_{n},r\_{n}] which converges to ℝ\mathbb{R} as n→∞n\to\infty, and for αi\alpha^{i} we also need to subtract the ball (−1rn,1rn)\left(-\frac{1}{r\_{n}},\frac{1}{r\_{n}}\right).
Gradient clipping is in accordance with deep learning literature, see, for example, Zhang et al. [[32](https://arxiv.org/html/2512.25017v1#bib.bib32)] and Goodfellow et al. [[10](https://arxiv.org/html/2512.25017v1#bib.bib10), Ch. 10 and 11].

Next, let us introduce the gradient descent dynamics for the training process of the parameters θn\theta^{n}, where tt denotes the training time.
The neural network Vn​(θn;⋅)V^{n}(\theta^{n};\cdot) should minimize the loss functional IkI^{k} in ([3.3](https://arxiv.org/html/2512.25017v1#S3.E3 "Equation 3.3 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) of the deep gradient flow method.
Hence, the dynamic of θtn\theta\_{t}^{n} should match the gradient of Ik​(Vn;⋅)I^{k}(V^{n};\cdot), *i.e.*

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​θtnd​t=\displaystyle\frac{\mathrm{d}\theta\_{t}^{n}}{\mathrm{d}t}= | −ηn​∇θIk​(Vn​(θtn;x))\displaystyle-\eta\_{n}\nabla\_{\theta}I^{k}\left(V^{n}\left(\theta\_{t}^{n};x\right)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | −ηn​⟨𝒟​Ik​(Vtn),∇θVtn⟩ℋ01,\displaystyle-\eta\_{n}\left\langle\mathcal{D}I^{k}\left(V\_{t}^{n}\right),\nabla\_{\theta}V\_{t}^{n}\right\rangle\_{\mathcal{H}\_{0}^{1}}, |  | (4.1) |

with learning rate ηn=n2​δ−1\eta\_{n}=n^{2\delta-1}, where 𝒟\mathcal{D} denotes the Fréchet derivative; *i.e.* for any u,v∈ℋ01​(ℝd)u,v\in\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨𝒟​Ik​(v),u⟩ℋ01=\displaystyle\left\langle\mathcal{D}I^{k}\left(v\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}= | ⟨v−Uk−1,u⟩L2+h​⟨ℒ​v,u⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),u⟩L2.\displaystyle\left\langle v-U^{k-1},u\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}v,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),u\right\rangle\_{L^{2}}. |  | (4.2) |

We obtain a coordinate dynamic (θtn)t≥0=(θti,n)t≥0=(βti,n,αti,n,cti,n)t≥0{(\theta^{n}\_{t})\_{t\geq 0}}=(\theta\_{t}^{i,n})\_{t\geq 0}=\big(\beta\_{t}^{i,n},\alpha\_{t}^{i,n},c\_{t}^{i,n}\big)\_{t\geq 0}.
This dynamic depends on the number of hidden layers nn of the neural network, since the parameters that optimally approximate a function depend on the number of parameters we use.
We use a random initialization for this process, independent of nn, denoted by:

|  |  |  |
| --- | --- | --- |
|  | (β0i,n,α0i,n,c0i,n)=(β0i,α0i,c0i)=θ0i.\left(\beta\_{0}^{i,n},\alpha\_{0}^{i,n},c\_{0}^{i,n}\right)=\left(\beta\_{0}^{i},\alpha\_{0}^{i},c\_{0}^{i}\right)=\theta^{i}\_{0}. |  |

###### Assumption (NNI).

The parameters β0i,α0i,c0i\beta\_{0}^{i},\alpha\_{0}^{i},c\_{0}^{i} that initialize the neural network are i.i.d. random variables that satisfy:

* (i)

  β0i\beta\_{0}^{i} is a symmetric random variable with finite second moment: 𝔼​[|β0i|2]<+∞\mathbb{E}\left[\left|\beta\_{0}^{i}\right|^{2}\right]<+\infty;
* (ii)

  α0i≠0\alpha\_{0}^{i}\neq 0 ℙ\mathbb{P}-almost surely and 𝔼​[|α0i|d+7+|α0i|−d−2]<+∞\mathbb{E}\left[\left|\alpha\_{0}^{i}\right|^{d+7}+\left|\alpha\_{0}^{i}\right|^{-d-2}\right]<+\infty;
* (iii)

  c0ic\_{0}^{i} is an ℝd\mathbb{R}^{d}-valued random variable and 𝔼​[|c0i|d+7]<+∞\mathbb{E}\left[\left|c\_{0}^{i}\right|^{d+7}\right]<+\infty;
* (iv)

  α0i,c0i\alpha\_{0}^{i},\ c\_{0}^{i}, have full support, *i.e.* for any Borel set A⊂ℝA\subset\mathbb{R} and B⊂ℝdB\subset\mathbb{R}^{d} with positive Lebesgue measure, ℙ​(α0i∈A)\mathbb{P}\left(\alpha\_{0}^{i}\in A\right) and ℙ​(c0i∈B)\mathbb{P}\left(c\_{0}^{i}\in B\right) are positive.

Using the chain rule, the dynamic Vtn​(x)=Vn​(θtn;x)V\_{t}^{n}(x)=V^{n}\left(\theta\_{t}^{n};x\right) satisfies the following equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vtn​(x)d​t\displaystyle\frac{\mathrm{d}V\_{t}^{n}(x)}{\mathrm{d}t} | =∇θVn​(θtn;x)⋅d​θtnd​t=−ηn​∇θVn​(θtn;x)⋅∇θIk​(Vn​(θtn;x))\displaystyle=\nabla\_{\theta}V^{n}\left(\theta\_{t}^{n};x\right)\cdot\frac{\mathrm{d}\theta^{n}\_{t}}{\mathrm{d}t}=-\eta\_{n}\nabla\_{\theta}V^{n}\left(\theta\_{t}^{n};x\right)\cdot\nabla\_{\theta}I^{k}\left(V^{n}\left(\theta\_{t}^{n};x\right)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−⟨𝒟​Ik​(Vtn),Ztn​(x,⋅)⟩ℋ01,\displaystyle=-\left\langle\mathcal{D}I^{k}\left(V^{n}\_{t}\right),Z\_{t}^{n}(x,\cdot)\right\rangle\_{\mathcal{H}\_{0}^{1}}, |  | (4.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| with V0n​(x)=Vn​(θ0n;x)V\_{0}^{n}(x)=V^{n}\left(\theta\_{0}^{n};x\right) and | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ztn​(x,y)\displaystyle Z\_{t}^{n}\left(x,y\right) | =ηn​∇θVtn​(x)⋅∇θVtn​(y)\displaystyle=\eta\_{n}\nabla\_{\theta}V\_{t}^{n}(x)\cdot\nabla\_{\theta}V\_{t}^{n}\left(y\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n​∑i=1n∇θβ^ti,n​ψ​(α^ti,n​x+c^ti,n)⋅∇θβ^ti,n​ψ​(α^ti,n​y+c^ti,n).\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}\nabla\_{\theta}\hat{\beta}^{i,n}\_{t}\psi\left(\hat{\alpha}^{i,n}\_{t}x+\hat{c}^{i,n}\_{t}\right)\cdot\nabla\_{\theta}\hat{\beta}^{i,n}\_{t}\psi\left(\hat{\alpha}^{i,n}\_{t}y+\hat{c}^{i,n}\_{t}\right). |  |

We expect ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex7 "4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) to converge to the following gradient flow

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Vt​(x)d​t\displaystyle\frac{\mathrm{d}V\_{t}(x)}{\mathrm{d}t} | =−⟨𝒟​Ik​(Vt),Z​(x,⋅)⟩ℋ01,\displaystyle=-\left\langle\mathcal{D}I^{k}\left(V\_{t}\right),Z(x,\cdot)\right\rangle\_{\mathcal{H}\_{0}^{1}}, |  | (4.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| with V0=0V\_{0}=0, where | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Z​(x,y)\displaystyle Z(x,y) | =𝔼​[∇θβ01​ψ​(α01​x+c01)⋅∇θβ01​ψ​(α01​y+c01)],\displaystyle=\mathbb{E}\big[\nabla\_{\theta}\beta^{1}\_{0}\psi\left(\alpha^{1}\_{0}x+c^{1}\_{0}\right)\cdot\nabla\_{\theta}\beta^{1}\_{0}\psi\left(\alpha^{1}\_{0}y+c^{1}\_{0}\right)\big], |  |

while the inner product of the Fréchet derivative of the loss functional with another functional is defined in ([4.2](https://arxiv.org/html/2512.25017v1#S4.E2 "Equation 4.2 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
The gradient flow ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) is an infinite-dimensional ODE that governs the dynamics of the wide network limit of the neural network during the training process and, the right-hand side depends on the loss function of the gradient flow method for the solution of PDEs in ([3.3](https://arxiv.org/html/2512.25017v1#S3.E3 "Equation 3.3 ‣ 3.3. Weak formulation and uniqueness of minimizer ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).
Let us also point out that the kernel Z​(⋅,⋅)Z(\cdot,\cdot) is not the standard neural tangent kernel, as it also depends on the loss functional, which further complicates the analysis.
The right-hand side of ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), using ([4.2](https://arxiv.org/html/2512.25017v1#S4.E2 "Equation 4.2 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), takes the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯​(v)​(x)\displaystyle\mathcal{T}\left(v\right)\left(x\right) | :=⟨𝒟​Ik​(v),Z​(x,⋅)⟩ℋ01\displaystyle=\left\langle\mathcal{D}I^{k}\left(v\right),Z(x,\cdot)\right\rangle\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨v−Uk−1,Z​(x,⋅)⟩L2+h​⟨ℒ​v,Z​(x,⋅)⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),Z​(x,⋅)⟩L2.\displaystyle=\left\langle v-U^{k-1},Z(x,\cdot)\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}v,Z(x,\cdot)\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),Z(x,\cdot)\right\rangle\_{L^{2}}. |  |

The analysis of this operator plays a crucial role in the next subsection, where we study the long term behavior of this gradient flow.

Let us introduce the following shorthand notation:

|  |  |  |
| --- | --- | --- |
|  | 𝒳​(θ;x):=∇θβ​ψ​(α​x+c)and𝒳n​(θ;x):=∇θβ^​ψ​(α^​x+c^)\mathcal{X}(\theta;x):=\nabla\_{\theta}\beta\psi\left(\alpha x+c\right)\quad\text{and}\quad\mathcal{X}^{n}(\theta;x):=\nabla\_{\theta}\hat{\beta}\psi\left(\hat{\alpha}x+\hat{c}\right) |  |

for some generic parameters θ=(β,α,c)∈ℝ×ℝ×ℝd\theta=\left(\beta,\alpha,c\right)\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^{d}, where (β^,α^,c^)(\hat{\beta},\hat{\alpha},\hat{c}) denotes the clipped version of these parameters.
Moreover, in order to simplify the notation, let us set

|  |  |  |
| --- | --- | --- |
|  | X​(x):=𝒳​(θ01;x),Xn​(x):=𝒳n​(θ01;x)andXti,n​(x):=𝒳n​(θti,n;x).X(x):=\mathcal{X}\left(\theta^{1}\_{0};x\right),\quad X^{n}(x):=\mathcal{X}^{n}\left(\theta^{1}\_{0};x\right)\quad\text{and}\quad X\_{t}^{i,n}(x):=\mathcal{X}^{n}\left(\theta^{i,n}\_{t};x\right). |  |

Then, using this notation we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ztn​(x,y)\displaystyle Z\_{t}^{n}(x,y) | =1n​∑i=1nXti,n​(x)⋅Xti,n​(y),\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}X\_{t}^{i,n}\left(x\right)\cdot X\_{t}^{i,n}\left(y\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| and | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Z​(x,y)\displaystyle Z(x,y) | =𝔼​[X​(x)⋅X​(y)].\displaystyle=\mathbb{E}\left[X\left(x\right)\cdot X\left(y\right)\right]. |  |

This representation invites us to use the law of large numbers to conclude that Ztn​(x,y)→Z​(x,y)Z^{n}\_{t}(x,y)\to Z(x,y) as n→∞n\to\infty.
Intuitively, this is the connection between the gradient flow in ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex7 "4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) that the neural network follows during the training process, and the corresponding “wide network limit” in ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).

The main result of this subsection follows, which states that as the number of neurons tends to infinity during the training process, then the neural network VnV^{n} converges to the wide network limit VV, which satisfies the gradient flow ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")).

###### Theorem 4.1.

Assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), and let rnr\_{n} increase with nn, while rn≤log⁡nr\_{n}\leq\log n.
Moreover, assume that the operators of the PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, the dynamic ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex7 "4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) converges to the gradient flow ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) as n→∞n\to\infty, *i.e.* for any T>0,T>0,

|  |  |  |
| --- | --- | --- |
|  | sup0≤t≤T𝔼​[‖Vtn−Vt‖ℋ01]→n→∞0.\displaystyle\sup\_{0\leq t\leq T}\mathbb{E}\left[\big\|V^{n}\_{t}-V\_{t}\big\|\_{\mathcal{H}\_{0}^{1}}\right]\xrightarrow[n\to\infty]{}0. |  |

###### Lemma 4.2.

Assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖V0n‖ℋ01]≤C(1)​n12−δ,\displaystyle\mathbb{E}\left[\left\|V^{n}\_{0}\right\|\_{\mathcal{H}\_{0}^{1}}\right]\leq C^{\left(1\right)}n^{\frac{1}{2}-\delta}, |  |

where C(1)=𝔼​[|β0i|2]12​(𝔼​[|α0i|−d]+𝔼​[|α0i|2−d]+2)12​‖ψ‖ℋ01C^{\left(1\right)}=\mathbb{E}\left[\left|\beta\_{0}^{i}\right|^{2}\right]^{\frac{1}{2}}\left(\mathbb{E}\left[\left|\alpha\_{0}^{i}\right|^{-d}\right]+\mathbb{E}\left[\left|\alpha\_{0}^{i}\right|^{2-d}\right]+2\right)^{\frac{1}{2}}\left\|\psi\right\|\_{\mathcal{H}\_{0}^{1}}.

###### Proof.

Let us denote a neuron by Yi​(x):=β^0i​ψ​(α^0i​x+c^0i)Y^{i}(x):=\hat{\beta}\_{0}^{i}\psi\left(\hat{\alpha}\_{0}^{i}x+\hat{c}\_{0}^{i}\right), then V0n=1nδ​∑i=1nYi​(x)V\_{0}^{n}=\frac{1}{n^{\delta}}\sum\_{i=1}^{n}Y^{i}(x) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖V0n‖ℋ012]=𝔼​[∫ℝd|V0n|2+|∇xV0n|2​d​x].\mathbb{E}\left[\left\|V^{n}\_{0}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right]=\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left|V^{n}\_{0}\right|^{2}+\left|\nabla\_{x}V^{n}\_{0}\right|^{2}\mathrm{d}x\right]. |  | (4.5) |

Let us first compute the value of the cross terms, for i≠ji\neq j, which equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫ℝdYi​(x)​Yj​(x)​dx]\displaystyle\mathbb{E}\left[\int\_{\mathbb{R}^{d}}Y^{i}(x)Y^{j}(x)\mathrm{d}x\right] | =𝔼​[∫ℝdβ^0i​ψ​(α^0i​x+c^0i)​β^0j​ψ​(α^0j​x+c^0j)​dx]\displaystyle=\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\hat{\beta}\_{0}^{i}\psi\left(\hat{\alpha}\_{0}^{i}x+\hat{c}\_{0}^{i}\right)\hat{\beta}\_{0}^{j}\psi\left(\hat{\alpha}\_{0}^{j}x+\hat{c}\_{0}^{j}\right)\mathrm{d}x\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ℝd𝔼​[β^0i]​𝔼​[β^0j]​𝔼​[ψ​(α^0i​x+c^0i)​ψ​(α^0j​x+c^0j)]​dx=0;\displaystyle=\int\_{\mathbb{R}^{d}}\mathbb{E}\left[\hat{\beta}\_{0}^{i}\right]\mathbb{E}\left[\hat{\beta}\_{0}^{j}\right]\mathbb{E}\left[\psi\left(\hat{\alpha}\_{0}^{i}x+\hat{c}\_{0}^{i}\right)\psi\left(\hat{\alpha}\_{0}^{j}x+\hat{c}\_{0}^{j}\right)\right]\mathrm{d}x=0; |  |

here, we can apply Fubini’s theorem since ψ\psi has compact support and the parameters θ\theta are bounded, while the random variables β0i\beta^{i}\_{0} are symmetric, hence their expectation is zero.
Therefore, we can bound the L2L^{2}-norm of V0nV\_{0}^{n} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫ℝd|V0n|2​dx]\displaystyle\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left|V^{n}\_{0}\right|^{2}\mathrm{d}x\right] | =1n2​δ​𝔼​[∫ℝd∑i=1n|β^0i|2​|ψ​(α^0i​x+c^0i)|2​d​x]\displaystyle=\frac{1}{n^{2\delta}}\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\sum\_{i=1}^{n}\left|\hat{\beta}\_{0}^{i}\right|^{2}\left|\psi\left(\hat{\alpha}\_{0}^{i}x+\hat{c}\_{0}^{i}\right)\right|^{2}\mathrm{d}x\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n2​δ−1​𝔼​[|β^0i|2​∫ℝd|α^0i|−d​|ψ​(y)|2​dy]\displaystyle=\frac{1}{n^{2\delta-1}}\mathbb{E}\left[\left|\hat{\beta}\_{0}^{i}\right|^{2}\int\_{\mathbb{R}^{d}}\left|\hat{\alpha}\_{0}^{i}\right|^{-d}\left|\psi(y)\right|^{2}\mathrm{d}y\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤1n2​δ−1​𝔼​[|β^0i|2]​𝔼​[|α^0i|−d]​∫ℝd|ψ​(y)|2​dy.\displaystyle\leq\frac{1}{n^{2\delta-1}}\mathbb{E}\left[\left|\hat{\beta}\_{0}^{i}\right|^{2}\right]\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{-d}\right]\int\_{\mathbb{R}^{d}}\left|\psi(y)\right|^{2}\mathrm{d}y. |  | (4.6) |

The derivative of V0nV^{n}\_{0} can be expressed as

|  |  |  |
| --- | --- | --- |
|  | ∇xV0n=1nδ​∑i=1n∇xYi​(x)=1nδ​∑i=1nβ^0i​α^0i​(∇ψ)​(α^0i​x+c^0i).\nabla\_{x}V^{n}\_{0}=\frac{1}{n^{\delta}}\sum\_{i=1}^{n}\nabla\_{x}Y^{i}(x)=\frac{1}{n^{\delta}}\sum\_{i=1}^{n}\hat{\beta}\_{0}^{i}\hat{\alpha}\_{0}^{i}\left(\nabla\psi\right)\left(\hat{\alpha}\_{0}^{i}x+\hat{c}\_{0}^{i}\right). |  |

Hence, we can analogously bound the L2L^{2}-norm of the derivative of V0nV^{n}\_{0} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫ℝd|∇xV0n|2​dx]\displaystyle\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left|\nabla\_{x}V^{n}\_{0}\right|^{2}\mathrm{d}x\right] | =1n2​δ−1​𝔼​[∫ℝd|β^0i|2​|α^0i|2​|(∇ψ)​(α^0i​x+c^0i)|2​dx]\displaystyle=\frac{1}{n^{2\delta-1}}\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left|\hat{\beta}\_{0}^{i}\right|^{2}\left|\hat{\alpha}\_{0}^{i}\right|^{2}\left|\left(\nabla\psi\right)\left(\hat{\alpha}\_{0}^{i}x+\hat{c}\_{0}^{i}\right)\right|^{2}\mathrm{d}x\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤1n2​δ−1​𝔼​[|β^0i|2]​𝔼​[|α^0i|2−d]​∫ℝd|∇ψ​(x)|2​dx.\displaystyle\leq\frac{1}{n^{2\delta-1}}\mathbb{E}\left[\left|\hat{\beta}\_{0}^{i}\right|^{2}\right]\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{2-d}\right]\int\_{\mathbb{R}^{d}}\left|\nabla\psi(x)\right|^{2}\mathrm{d}x. |  | (4.7) |

Applying bounds ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex20 "Proof. ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) and ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex23 "Proof. ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) to ([4.5](https://arxiv.org/html/2512.25017v1#S4.E5 "Equation 4.5 ‣ Proof. ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), and using Jensen’s inequality and that |β^0i|≤|β0i|\left|\hat{\beta}\_{0}^{i}\right|\leq\left|\beta\_{0}^{i}\right|, yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖V0n‖ℋ01]\displaystyle\mathbb{E}\left[\left\|V^{n}\_{0}\right\|\_{\mathcal{H}\_{0}^{1}}\right] | ≤𝔼​[‖V0n‖ℋ012]\displaystyle\leq\sqrt{\mathbb{E}\left[\left\|V^{n}\_{0}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1n2​δ−1​𝔼​[|β0i|2]​𝔼​[|α^0i|−d]​∫ℝd|ψ|2​dx+1n2​δ−1​𝔼​[|β0i|2]​𝔼​[|α^0i|2−d]​∫ℝd|∇ψ|2​dx\displaystyle\leq\sqrt{\frac{1}{n^{2\delta-1}}\mathbb{E}\left[\left|\beta\_{0}^{i}\right|^{2}\right]\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{-d}\right]\int\_{\mathbb{R}^{d}}\left|\psi\right|^{2}\mathrm{d}x+\frac{1}{n^{2\delta-1}}\mathbb{E}\left[\left|\beta\_{0}^{i}\right|^{2}\right]\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{2-d}\right]\int\_{\mathbb{R}^{d}}\left|\nabla\psi\right|^{2}\mathrm{d}x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤n12−δ​𝔼​[|β0i|2]12​(𝔼​[|α^0i|−d]+𝔼​[|α^0i|2−d])12​∫ℝd|ψ|2​dx+∫ℝd|∇ψ|2​dx.\displaystyle\leq n^{\frac{1}{2}-\delta}\mathbb{E}\left[\left|\beta\_{0}^{i}\right|^{2}\right]^{\frac{1}{2}}\left(\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{-d}\right]+\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{2-d}\right]\right)^{\frac{1}{2}}\sqrt{\int\_{\mathbb{R}^{d}}\left|\psi\right|^{2}\mathrm{d}x+\int\_{\mathbb{R}^{d}}\left|\nabla\psi\right|^{2}\mathrm{d}x}. |  |

If |α|≤rn\left|\alpha\right|\leq r\_{n}, then |α^|−1≤|α|−1\left|\hat{\alpha}\right|^{-1}\leq\left|\alpha\right|^{-1} and if |α|>rn\left|\alpha\right|>r\_{n}, then |α^|−1=rn−1\left|\hat{\alpha}\right|^{-1}=r\_{n}^{-1}.
Therefore, for d=1,2d=1,2, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|α^0i|−d]+𝔼​[|α^0i|2−d]\displaystyle\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{-d}\right]+\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{2-d}\right] | ≤𝔼​[|α01|−d+(rn)−d+|α01|2−d],\displaystyle\leq\mathbb{E}\left[\left|\alpha\_{0}^{1}\right|^{-d}+\left(r\_{n}\right)^{-d}+\left|\alpha\_{0}^{1}\right|^{2-d}\right], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while for d≥3d\geq 3, we get | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|α^0i|−d]+𝔼​[|α^0i|2−d]\displaystyle\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{-d}\right]+\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{i}\right|^{2-d}\right] | ≤𝔼​[|α01|−d+(rn)−d+|α01|2−d+(rn)2−d].∎\displaystyle\leq\mathbb{E}\left[\left|\alpha\_{0}^{1}\right|^{-d}+\left(r\_{n}\right)^{-d}+\left|\alpha\_{0}^{1}\right|^{2-d}+\left(r\_{n}\right)^{2-d}\right].\qed |  |

###### Proof of [Theorem 4.1](https://arxiv.org/html/2512.25017v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").

Using ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex7 "4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) and ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), we need to estimate the following difference:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtn​(x)−Vt​(x)\displaystyle V^{n}\_{t}(x)-V\_{t}(x) | =V0n​(x)−V0​(x)+∫0t{⟨𝒟​Ik​(Vs),Z​(x,⋅)⟩ℋ01−⟨𝒟​Ik​(Vsn),Zsn​(x,⋅)⟩ℋ01}​ds\displaystyle=V^{n}\_{0}(x)-V\_{0}(x)+\int\_{0}^{t}\Big\{\left\langle\mathcal{D}I^{k}\left(V\_{s}\right),Z(x,\cdot)\right\rangle\_{\mathcal{H}\_{0}^{1}}-\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),Z\_{s}^{n}\left(x,\cdot\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}\Big\}\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =V0n​(x)−V0​(x)⏟(a​1)+∫0t{⟨𝒟​Ik​(Vs)−𝒟​Ik​(Vsn),Z​(x,⋅)⟩ℋ01⏟(a​2)\displaystyle=\underbrace{V^{n}\_{0}(x)-V\_{0}(x)}\_{\left(a1\right)}+\int\_{0}^{t}\Big\{\underbrace{\left\langle\mathcal{D}I^{k}\left(V\_{s}\right)-\mathcal{D}I^{k}\left(V^{n}\_{s}\right),Z(x,\cdot)\right\rangle\_{\mathcal{H}\_{0}^{1}}}\_{\left(a2\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +⟨𝒟​Ik​(Vsn),Z​(x,⋅)−Z0n​(x,⋅)⟩ℋ01⏟(a​3)+⟨𝒟​Ik​(Vsn),Z0n​(x,⋅)−Zsn​(x,⋅)⟩ℋ01⏟(a​4)}ds.\displaystyle\qquad+\underbrace{\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),Z(x,\cdot)-Z\_{0}^{n}\left(x,\cdot\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}}\_{\left(a3\right)}+\underbrace{\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),Z^{n}\_{0}\left(x,\cdot\right)-Z\_{s}^{n}\left(x,\cdot\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}}\_{\left(a4\right)}\Big\}\,\mathrm{d}s. |  |

The proof is now separated in several steps, corresponding to the estimation of each of the terms above.

Step (a1).
We know that V0​(x)=0V\_{0}(x)=0 by definition, hence, using [Lemma 4.2](https://arxiv.org/html/2512.25017v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we get

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖V0n​(x)−V0​(x)‖ℋ01]≤C(1)​n12−δ.\mathbb{E}\left[\left\|V^{n}\_{0}(x)-V\_{0}(x)\right\|\_{\mathcal{H}\_{0}^{1}}\right]\leq C^{\left(1\right)}n^{\frac{1}{2}-\delta}. |  |

Step (a2).
In order to separate the random terms VV and XX, we define another probability space Ω′\Omega^{\prime} and probability measure ℙ′\mathbb{P}^{\prime} such that X​(ω′)X\left(\omega^{\prime}\right) under ℙ′\mathbb{P}^{\prime} has the same distribution as XX under ℙ.\mathbb{P}.
Then, we can rewrite (a​2)(a2) as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a​2)\displaystyle(a2) | =⟨𝒟​Ik​(Vs)−𝒟​Ik​(Vsn),𝔼​[X⋅X​(x)]⟩ℋ01\displaystyle=\left\langle\mathcal{D}I^{k}\left(V\_{s}\right)-\mathcal{D}I^{k}\left(V^{n}\_{s}\right),\mathbb{E}\left[X\cdot X\left(x\right)\right]\right\rangle\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Ω′⟨𝒟​Ik​(Vs)−𝒟​Ik​(Vsn),X​(ω′)⟩ℋ01​X​(x)​(ω′)​ℙ′​(d​ω′).\displaystyle=\int\_{\Omega^{\prime}}\left\langle\mathcal{D}I^{k}\left(V\_{s}\right)-\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X\left(\omega^{\prime}\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}X\left(x\right)\left(\omega^{\prime}\right)\mathbb{P}^{\prime}\left(\mathrm{d}\omega^{\prime}\right). |  |

Hence, we can bound the ℋ01\mathcal{H}\_{0}^{1}-norm of (a2) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(a​2)‖ℋ01\displaystyle\left\|(a2)\right\|\_{\mathcal{H}\_{0}^{1}} | ≤∫Ω′‖⟨𝒟​Ik​(Vs)−𝒟​Ik​(Vsn),X​(ω′)⟩ℋ01⋅X​(x)​(ω′)‖ℋ01​ℙ​(d​ω′)\displaystyle\leq\int\_{\Omega^{\prime}}\left\|\left\langle\mathcal{D}I^{k}\left(V\_{s}\right)-\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X\left(\omega^{\prime}\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}\cdot X\left(x\right)\left(\omega^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\mathbb{P}\left(\mathrm{d}\omega^{\prime}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Ω′|⟨𝒟​Ik​(Vs)−𝒟​Ik​(Vsn),X​(ω′)⟩ℋ01|​‖X​(ω′)‖ℋ01​ℙ​(d​ω′)\displaystyle=\int\_{\Omega^{\prime}}\left|\left\langle\mathcal{D}I^{k}\left(V\_{s}\right)-\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X\left(\omega^{\prime}\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}\right|\left\|X\left(\omega^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\mathbb{P}\left(\mathrm{d}\omega^{\prime}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤[Lemma A.1](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem1 "Lemma A.1 (Continuity of the Fréchet derivative). ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")​K​‖Vs−Vsn‖ℋ01​∫Ω′‖X​(ω′)‖ℋ012​ℙ​(d​ω′)\displaystyle\hskip-13.50008pt\overset{\text{\lx@cref{creftype~refnum}{lem:con\_frechet}}}{\leq}K\left\|V\_{s}-V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\int\_{\Omega^{\prime}}\left\|X\left(\omega^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\mathbb{P}\left(\mathrm{d}\omega^{\prime}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[Lemma A.4](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem4 "Lemma A.4 (ℋ₀¹-boundedness of 𝑋). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")​K​‖Vs−Vsn‖ℋ01​𝔼​[‖X‖ℋ012]\displaystyle\hskip-13.50008pt\overset{\text{\lx@cref{creftype~refnum}{lem:bound\_XH}}}{=}K\left\|V\_{s}-V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\mathbb{E}\left[\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​‖Vs−Vsn‖ℋ01.\displaystyle\leq C\_{\psi}\left\|V\_{s}-V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}. |  |

Here, KK is the constant from [Lemma A.1](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem1 "Lemma A.1 (Continuity of the Fréchet derivative). ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and CψC\_{\psi} is another constant that depends on the activation function ψ\psi and may change from line to line.

Step (a3).
Let us rewrite the term (a​3)\left(a3\right) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a​3)\displaystyle\left(a3\right) | =1n​∑i=1n⟨𝒟​Ik​(Vsn),X0i,n⋅X0i,n​(x)−𝔼​[X0i,n⋅X0i,n​(x)]⟩ℋ01⏟(a​3.1)\displaystyle=\underbrace{\frac{1}{n}\sum\_{i=1}^{n}\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)-\mathbb{E}\left[X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)\right]\right\rangle\_{\mathcal{H}\_{0}^{1}}}\_{\left(a3.1\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +⟨𝒟​Ik​(Vsn),𝔼​[Xn⋅Xn​(x)−X⋅X​(x)]⟩ℋ01⏟(a​3.2),\displaystyle\quad+\underbrace{\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),\mathbb{E}\left[X^{n}\cdot X^{n}\left(x\right)-X\cdot X\left(x\right)\right]\right\rangle\_{\mathcal{H}\_{0}^{1}}}\_{\left(a3.2\right)}, |  |

where we can use XnX^{n} instead of X0i,nX^{i,n}\_{0} in the second term since, by [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), these two terms have the same expectation.
Then, we can further separate the term (a​3.2)\left(a3.2\right) as follows:

|  |  |  |
| --- | --- | --- |
|  | (a​3.2)=⟨𝒟​Ik​(Vsn),𝔼​[(Xn−X)⋅Xn​(x)]⟩ℋ01⏟(a​3.21)+⟨𝒟​Ik​(Vsn),𝔼​[X⋅(Xn​(x)−X​(x))]⟩ℋ01⏟(a​3.22).\displaystyle\left(a3.2\right)=\underbrace{\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),\mathbb{E}\left[\left(X^{n}-X\right)\cdot X^{n}\left(x\right)\right]\right\rangle\_{\mathcal{H}\_{0}^{1}}}\_{\left(a3.21\right)}+\underbrace{\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),\mathbb{E}\left[X\cdot\left(X^{n}\left(x\right)-X\left(x\right)\right)\right]\right\rangle\_{\mathcal{H}\_{0}^{1}}}\_{\left(a3.22\right)}. |  |

A similar computation as for the term (a​2)(a2), yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(a​3.21)‖ℋ01\displaystyle\left\|\left(a3.21\right)\right\|\_{\mathcal{H}\_{0}^{1}} | ≤∫Ω′|⟨𝒟​Ik​(Vsn),Xn​(ω′)−X​(ω′)⟩ℋ01|​‖Xn​(ω′)‖ℋ01​ℙ​(d​ω′)\displaystyle\leq\int\_{\Omega^{\prime}}\left|\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X^{n}\left(\omega^{\prime}\right)-X\left(\omega^{\prime}\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}\right|\left\|X^{n}\left(\omega^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\mathbb{P}\left(\mathrm{d}\omega^{\prime}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤[Lemma A.1](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem1 "Lemma A.1 (Continuity of the Fréchet derivative). ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")​K​(1+‖Vsn‖ℋ01)​∫Ω′‖Xn​(ω′)−X​(ω′)‖ℋ01​‖Xn​(ω′)‖ℋ01​ℙ​(d​ω′)\displaystyle\hskip-13.50008pt\overset{\text{\lx@cref{creftype~refnum}{lem:con\_frechet}}}{\leq}K\left(1+\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\int\_{\Omega^{\prime}}\left\|X^{n}\left(\omega^{\prime}\right)-X\left(\omega^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\left\|X^{n}\left(\omega^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\mathbb{P}\left(\mathrm{d}\omega^{\prime}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K​(1+‖Vsn‖ℋ01)​𝔼​[‖Xn−X‖ℋ01​‖Xn‖ℋ01].\displaystyle=K\left(1+\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}\left\|X^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\right]. |  |

Analogously, we have that

|  |  |  |
| --- | --- | --- |
|  | ‖(a​3.22)‖ℋ01≤K​(1+‖Vsn‖ℋ01)​𝔼​[‖Xn−X‖ℋ01​‖X‖ℋ01].\left\|\left(a3.22\right)\right\|\_{\mathcal{H}\_{0}^{1}}\leq K\left(1+\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}\right]. |  |

Overall, combining the two bounds and then using [Lemma A.2](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), then the Cauchy–Schwarz inequality, and finally [Lemmas A.4](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem4 "Lemma A.4 (ℋ₀¹-boundedness of 𝑋). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [A.5](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem5 "Lemma A.5. ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖(a​3.2)‖ℋ01]\displaystyle\mathbb{E}\left[\left\|\left(a3.2\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right] | ≤2​K​𝔼​[1+‖Vsn‖ℋ01]​𝔼​[‖Xn−X‖ℋ01​(‖Xn‖ℋ01+‖X‖ℋ01)]\displaystyle\leq 2K\mathbb{E}\left[1+\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\right]\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}\left(\left\|X^{n}\right\|\_{\mathcal{H}\_{0}^{1}}+\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​𝔼​[‖Xn−X‖ℋ01​(‖Xn‖ℋ01+‖X‖ℋ01)]\displaystyle\leq C\_{\psi}\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}\left(\left\|X^{n}\right\|\_{\mathcal{H}\_{0}^{1}}+\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​𝔼​[‖Xn−X‖ℋ012]12​𝔼​[‖Xn‖ℋ012+‖X‖ℋ012]12≤Cψ​εn12,\displaystyle\leq C\_{\psi}\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right]^{\frac{1}{2}}\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}+\left\|X\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]^{\frac{1}{2}}\leq C\_{\psi}\,{\varepsilon}\_{n}^{\frac{1}{2}}, |  |

where εn{\varepsilon}\_{n} is defined in [Lemma A.5](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem5 "Lemma A.5. ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and equals

|  |  |  |
| --- | --- | --- |
|  | εn=𝔼​[‖Xn−X‖ℋ012].{\varepsilon}\_{n}=\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right]. |  |

On the other hand, using [Lemma A.1](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem1 "Lemma A.1 (Continuity of the Fréchet derivative). ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") the norm of (a​3.1)\left(a3.1\right) can be bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(a​3.1)‖L2\displaystyle\left\|\left(a3.1\right)\right\|\_{L^{2}} | =1n​(∫ℝd⟨𝒟​Ik​(Vsn),∑i=1n(X0i,n⋅X0i,n​(x)−𝔼​[X0i,n⋅X0i,n​(x)])⟩ℋ012​dx)12\displaystyle=\frac{1}{n}\left(\int\_{\mathbb{R}^{d}}\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),\sum\_{i=1}^{n}\left(X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)-\mathbb{E}\left[X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)\right]\right)\right\rangle^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x\right)^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Kn​(1+‖Vsn‖ℋ01)​(∫ℝd‖∑i=1n(X0i,n⋅X0i,n​(x)−𝔼​[X0i,n⋅X0i,n​(x)])‖ℋ012​dx)12.\displaystyle\leq\frac{K}{n}\left(1+\left\|V^{n}\_{s}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\left(\int\_{\mathbb{R}^{d}}\left\|\sum\_{i=1}^{n}\left(X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)-\mathbb{E}\left[X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)\right]\right)\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x\right)^{\frac{1}{2}}. |  |

Then, using the Cauchy–Schwarz inequality and [Lemma A.2](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖(a​3.1)‖L2]\displaystyle\mathbb{E}\left[\left\|\left(a3.1\right)\right\|\_{L^{2}}\right] | ≤Kn​𝔼​[(1+‖Vsn‖ℋ01)2]12​𝔼​[∫ℝd‖∑i=1n(X0i,n⋅X0i,n​(x)−𝔼​[X0i,n⋅X0i,n​(x)])‖ℋ012​dx]12\displaystyle\leq\frac{K}{n}\mathbb{E}\left[\left(1+\left\|V^{n}\_{s}\right\|\_{\mathcal{H}\_{0}^{1}}\right)^{2}\right]^{\frac{1}{2}}\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left\|\sum\_{i=1}^{n}\left(X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)-\mathbb{E}\left[X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)\right]\right)\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x\right]^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψn​𝔼​[∫ℝd‖∑i=1n(X0i,n⋅X0i,n​(x)−𝔼​[X0i,n⋅X0i,n​(x)])‖ℋ012​dx]12\displaystyle\leq\frac{C\_{\psi}}{n}\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left\|\sum\_{i=1}^{n}\left(X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)-\mathbb{E}\left[X^{i,n}\_{0}\cdot X^{i,n}\_{0}\left(x\right)\right]\right)\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x\right]^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Cψn​𝔼​[∫ℝd‖Xn⋅Xn​(x)−𝔼​[Xn⋅Xn​(x)]‖ℋ012​dx]12,\displaystyle=\frac{C\_{\psi}}{\sqrt{n}}\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left\|X^{n}\cdot X^{n}\left(x\right)-\mathbb{E}\left[X^{n}\cdot X^{n}\left(x\right)\right]\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x\right]^{\frac{1}{2}}, |  |

where the last equality follows because XnX^{n} and X0i,nX^{i,n}\_{0} are equally distributed by [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), while Xi,n⋅Xi,n​(x)X^{i,n}\cdot X^{i,n}\left(x\right) are i.i.d. variables that satisfy

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨Xi,n⋅Xi,n​(x),Xj,n⋅Xj,n​(x)⟩ℋ01]=0,for ​i≠j.\mathbb{E}\left[\left\langle X^{i,n}\cdot X^{i,n}\left(x\right),X^{j,n}\cdot X^{j,n}\left(x\right)\right\rangle\_{\mathcal{H}\_{0}^{1}}\right]=0,\quad\text{for }i\neq j. |  |

Using the triangle inequality, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫ℝd‖Xn⋅Xn​(x)−𝔼​[Xn⋅Xn​(x)]‖ℋ012​dx]\displaystyle\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left\|X^{n}\cdot X^{n}\left(x\right)-\mathbb{E}\left[X^{n}\cdot X^{n}\left(x\right)\right]\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2​𝔼​[∫ℝd‖Xn⋅Xn​(x)‖ℋ012​dx]+2​∫ℝd‖𝔼​[Xn⋅Xn​(x)]‖ℋ012​dx\displaystyle\qquad\qquad\leq 2\mathbb{E}\left[\int\_{\mathbb{R}^{d}}\left\|X^{n}\cdot X^{n}\left(x\right)\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x\right]+2\int\_{\mathbb{R}^{d}}\left\|\mathbb{E}\left[X^{n}\cdot X^{n}\left(x\right)\right]\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}x |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2​𝔼​[‖Xn‖ℋ012​‖Xn‖L22]+2​𝔼​[‖Xn‖ℋ012]​𝔼​[‖Xn‖L22].\displaystyle\qquad\qquad\leq 2\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\left\|X^{n}\right\|^{2}\_{L^{2}}\right]+2\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]\mathbb{E}\left[\left\|X^{n}\right\|\_{L^{2}}^{2}\right]. |  |

Then, combining the last two inequalities, we arrive at

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖(a​3.1)‖L2]≤Cψn​(𝔼​[‖Xn‖ℋ012​‖Xn‖L22]12+𝔼​[‖Xn‖ℋ012]12​𝔼​[‖Xn‖L22]12).\displaystyle\mathbb{E}\left[\left\|\left(a3.1\right)\right\|\_{L^{2}}\right]\leq\frac{C\_{\psi}}{\sqrt{n}}\left(\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\left\|X^{n}\right\|^{2}\_{L^{2}}\right]^{\frac{1}{2}}+\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]^{\frac{1}{2}}\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{L^{2}}\right]^{\frac{1}{2}}\right). |  |

We can analogously estimate the term 𝔼​[‖∇x(a​3.1)‖L2]\mathbb{E}\left[\left\|\nabla\_{x}\left(a3.1\right)\right\|\_{L^{2}}\right] and deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖(a​3.1)‖ℋ01]\displaystyle\mathbb{E}\left[\left\|\left(a3.1\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right] | ≤Cψn​(𝔼​[‖Xn‖ℋ014]12+𝔼​[‖Xn‖ℋ012])≤Cψn​𝔼​[‖Xn‖ℋ014]12\displaystyle\leq\frac{C\_{\psi}}{\sqrt{n}}\left(\mathbb{E}\left[\left\|X^{n}\right\|^{4}\_{\mathcal{H}\_{0}^{1}}\right]^{\frac{1}{2}}+\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]\right)\leq\frac{C\_{\psi}}{\sqrt{n}}\mathbb{E}\left[\left\|X^{n}\right\|^{4}\_{\mathcal{H}\_{0}^{1}}\right]^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤[Lemma A.3](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem3 "Lemma A.3 (ℋ₀¹-boundedness of 𝑋^𝑛). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")​Cψ​(rn)8+dn.\displaystyle\hskip-13.50008pt\overset{\text{\lx@cref{creftype~refnum}{lem:boundXN}}}{\leq}\frac{C\_{\psi}\left(r\_{n}\right)^{8+d}}{\sqrt{n}}. |  |

Overall, we finish this step by concluding that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖(a​3)‖ℋ01]≤Cψ​((rn)8+dn+εn12).\mathbb{E}\left[\left\|\left(a3\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right]\leq C\_{\psi}\left(\frac{\left(r\_{n}\right)^{8+d}}{\sqrt{n}}+{\varepsilon}\_{n}^{\frac{1}{2}}\right). |  |

Step (a4).
Recalling the definition of Ztn,Z\_{t}^{n}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a​4)\displaystyle\left(a4\right) | =1n​∑i=1n⟨𝒟​Ik​(Vsn),X0i,n⟩ℋ01⋅X0i,n​(x)−1n​∑i=1n⟨𝒟​Ik​(Vsn),Xsi,n⟩ℋ01⋅Xsi,n​(x)\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X^{i,n}\_{0}\right\rangle\_{\mathcal{H}\_{0}^{1}}\cdot X^{i,n}\_{0}(x)-\frac{1}{n}\sum\_{i=1}^{n}\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X\_{s}^{i,n}\right\rangle\_{\mathcal{H}\_{0}^{1}}\cdot X\_{s}^{i,n}(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n​∑i=1n⟨𝒟​Ik​(Vsn),X0i,n−Xsi,n⟩ℋ01⋅X0i,n​(x)\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X^{i,n}\_{0}-X\_{s}^{i,n}\right\rangle\_{\mathcal{H}\_{0}^{1}}\cdot X^{i,n}\_{0}\left(x\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −1n​∑i=1n⟨𝒟​Ik​(Vsn),Xsi,n⟩ℋ01⋅(Xsi,n​(x)−X0i,n​(x)).\displaystyle\qquad-\frac{1}{n}\sum\_{i=1}^{n}\left\langle\mathcal{D}I^{k}\left(V^{n}\_{s}\right),X\_{s}^{i,n}\right\rangle\_{\mathcal{H}\_{0}^{1}}\cdot\left(X\_{s}^{i,n}\left(x\right)-X^{i,n}\_{0}\left(x\right)\right). |  |

Using first [Lemma A.1](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem1 "Lemma A.1 (Continuity of the Fréchet derivative). ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and then [Lemmas A.3](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem3 "Lemma A.3 (ℋ₀¹-boundedness of 𝑋^𝑛). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [A.6](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem6 "Lemma A.6 (𝜃-Lipschitz continuity). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(a​4)‖ℋ01\displaystyle\left\|\left(a4\right)\right\|\_{\mathcal{H}\_{0}^{1}} | ≤Kn​(1+‖Vsn‖ℋ01)​∑i=1n(‖Xsi,n‖ℋ01+‖Xi,n‖ℋ01)​‖Xsi,n−Xi,n‖ℋ01\displaystyle\leq\frac{K}{n}\left(1+\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\sum\_{i=1}^{n}\left(\left\|X\_{s}^{i,n}\right\|\_{\mathcal{H}\_{0}^{1}}+\left\|X^{i,n}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\left\|X\_{s}^{i,n}-X^{i,n}\right\|\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψn​(rn)8+d​(1+‖Vsn‖ℋ01)​∑i=1n|θsi,n−θ0i|12.\displaystyle\leq\frac{C\_{\psi}}{n}\left(r\_{n}\right)^{8+d}\left(1+\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\right)\sum\_{i=1}^{n}\left|\theta\_{s}^{i,n}-\theta\_{0}^{i}\right|^{\frac{1}{2}}. |  |

Hence we can bound its expectation by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖(a​4)‖ℋ01]\displaystyle\mathbb{E}\left[\left\|\left(a4\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right] | ≤Cψn​(rn)8+d​𝔼​[(‖Vsn‖ℋ01+1)2]12​𝔼​[(∑i=1n|θsi,n−θ0i|12)2]12\displaystyle\leq\frac{C\_{\psi}}{n}\left(r\_{n}\right)^{8+d}\mathbb{E}\left[\left(\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}+1\right)^{2}\right]^{\frac{1}{2}}\mathbb{E}\left[\left(\sum\_{i=1}^{n}\left|\theta\_{s}^{i,n}-\theta\_{0}^{i}\right|^{\frac{1}{2}}\right)^{2}\right]^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​n−12​(rn)8+d​𝔼​[(‖Vsn‖ℋ01+1)2]12​𝔼​[|θs1,n−θ01|]12\displaystyle\leq C\_{\psi}n^{-\frac{1}{2}}\left(r\_{n}\right)^{8+d}\mathbb{E}\left[\left(\left\|V\_{s}^{n}\right\|\_{\mathcal{H}\_{0}^{1}}+1\right)^{2}\right]^{\frac{1}{2}}\mathbb{E}\left[\left|\theta\_{s}^{1,n}-\theta\_{0}^{1}\right|\right]^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Lem. [A.2](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") & [A.7](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem7 "Lemma A.7. ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")​Cψ​t​nδ2−1​(rn)10+2​d.\displaystyle\hskip-19.49998pt\overset{\text{Lem. \ref{lem:EVtN} \& \ref{lem:thetat0}}}{\leq}C\_{\psi}\sqrt{t}n^{\frac{\delta}{2}-1}\left(r\_{n}\right)^{10+2d}. |  |

Final step.
Combining the previous steps, we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖Vtn−Vt‖ℋ01]\displaystyle\mathbb{E}\left[\left\|V^{n}\_{t}-V\_{t}\right\|\_{\mathcal{H}\_{0}^{1}}\right] | ≤𝔼​[‖(a​1)‖ℋ01]+𝔼​[‖∫0t(a​2)+(a​3)+(a​4)​d​s‖ℋ01]\displaystyle\leq\mathbb{E}\left[\left\|\left(a1\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right]+\mathbb{E}\left[\left\|\int\_{0}^{t}(a2)+\left(a3\right)+\left(a4\right)\mathrm{d}s\right\|\_{\mathcal{H}\_{0}^{1}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[‖(a​1)‖ℋ01]+∫0t𝔼​[‖(a​2)‖ℋ01]+𝔼​[‖(a​3)‖ℋ01]+𝔼​[‖(a​4)‖ℋ01]​d​s\displaystyle\leq\mathbb{E}\left[\left\|\left(a1\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right]+\int\_{0}^{t}\mathbb{E}\left[\left\|(a2)\right\|\_{\mathcal{H}\_{0}^{1}}\right]+\mathbb{E}\left[\left\|\left(a3\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right]+\mathbb{E}\left[\left\|\left(a4\right)\right\|\_{\mathcal{H}\_{0}^{1}}\right]\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤M​∫0t𝔼​[‖Vsn−Vs‖ℋ01]​ds\displaystyle\leq M\int\_{0}^{t}\mathbb{E}\left[\left\|V^{n}\_{s}-V\_{s}\right\|\_{\mathcal{H}\_{0}^{1}}\right]\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C(1)​n12−δ+T32​Cψ​((rn)8+dn+εn12+nδ2−1​(rn)10+2​d).\displaystyle\qquad+C^{\left(1\right)}n^{\frac{1}{2}-\delta}+T^{\frac{3}{2}}C\_{\psi}\left(\frac{\left(r\_{n}\right)^{8+d}}{\sqrt{n}}+{\varepsilon}\_{n}^{\frac{1}{2}}+n^{\frac{\delta}{2}-1}\left(r\_{n}\right)^{10+2d}\right). |  |

Hence, using Grönwall’s inequality, we conclude

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖Vtn−Vt‖ℋ01]\displaystyle\mathbb{E}\left[\left\|V^{n}\_{t}-V\_{t}\right\|\_{\mathcal{H}\_{0}^{1}}\right] | ≤eM​T​(C(1)​n12−δ+T32​Cψ​((rn)8+dn+εn12+nδ2−1​(rn)10+2​d))\displaystyle\leq\mathrm{e}^{MT}\left(C^{\left(1\right)}n^{\frac{1}{2}-\delta}+T^{\frac{3}{2}}C\_{\psi}\left(\frac{\left(r\_{n}\right)^{8+d}}{\sqrt{n}}+{\varepsilon}\_{n}^{\frac{1}{2}}+n^{\frac{\delta}{2}-1}\left(r\_{n}\right)^{10+2d}\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →n→∞0.∎\displaystyle\xrightarrow[n\to\infty]{}0.\qed |  |

### 4.2. Long time behavior of the gradient flow

In this subsection, we prove that the wide network limit of the trained neural network, i.e. the process VtV\_{t} defined in ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), converges to the global minimizer w∗w\_{\*} of the loss function IkI^{k} of the DGFMs, as the training time t→∞t\to\infty.
This result, combined with the convergence of the time-stepping scheme, then proves the convergence of the training error.

###### Theorem 4.3.

Assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and the coefficients of the PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, we have

|  |  |  |
| --- | --- | --- |
|  | limt→∞‖Vt−w∗‖ℋ01=0.\displaystyle\lim\_{t\to\infty}\left\|V\_{t}-w\_{\*}\right\|\_{\mathcal{H}\_{0}^{1}}=0. |  |

Let us start by rewriting the dynamics of the gradient flow VV in ([4.4](https://arxiv.org/html/2512.25017v1#S4.E4 "Equation 4.4 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(Vt−w∗)​(x)d​t=d​(Vt)​(x)d​t=−⟨𝒟​Ik​(Vt−w∗+w∗),Z​(x,⋅)⟩ℋ01=−𝒯~​(Vt−w∗)​(x),\displaystyle\frac{\mathrm{d}\left(V\_{t}-w\_{\*}\right)(x)}{\mathrm{d}t}=\frac{\mathrm{d}\left(V\_{t}\right)(x)}{\mathrm{d}t}=-\left\langle\mathcal{D}I^{k}\left(V\_{t}-w\_{\*}+w\_{\*}\right),Z(x,\cdot)\right\rangle\_{\mathcal{H}\_{0}^{1}}=-\widetilde{\mathcal{T}}\left(V\_{t}-w\_{\*}\right)\left(x\right), |  | (4.8) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯~​(v)\displaystyle\widetilde{\mathcal{T}}\left(v\right) | :=𝒯​(v+w∗)\displaystyle:=\mathcal{T}\left(v+w\_{\*}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨v+w∗−Uk−1,Z​(x,⋅)⟩L2+h​⟨ℒ​(v+w∗),Z​(x,⋅)⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),Z​(x,⋅)⟩L2\displaystyle=\left\langle v+w\_{\*}-U^{k-1},Z(x,\cdot)\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}(v+w\_{\*}),Z(x,\cdot)\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),Z(x,\cdot)\right\rangle\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨v,Z​(x,⋅)⟩L2+h​⟨ℒ​v,Z​(x,⋅)⟩ℋ−1,ℋ01+⟨w∗−Uk−1+h​(ℒ​w∗+F​(Uk−1)),Z​(x,⋅)⟩L2\displaystyle=\left\langle v,Z(x,\cdot)\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}v,Z(x,\cdot)\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+\left\langle w\_{\*}-U^{k-1}+h\left(\mathcal{L}w\_{\*}+F\left(U^{k-1}\right)\right),Z(x,\cdot)\right\rangle\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨v,Z​(x,⋅)⟩L2+h​⟨ℒ​v,Z​(x,⋅)⟩ℋ−1,ℋ01.\displaystyle=\left\langle v,Z(x,\cdot)\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}v,Z(x,\cdot)\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}. |  |

We work with 𝒯~\widetilde{\mathcal{T}} in the sequel, because 𝒯\mathcal{T} is not linear (𝒯​(0)≠0)\left(\mathcal{T}\left(0\right)\neq 0\right).
Next, let us define another inner product, such that 𝒯~\widetilde{\mathcal{T}} becomes positive semi-definite.
Indeed, for any u,v∈ℋ01​(ℝd),u,v\in\mathcal{H}\_{0}^{1}\left(\mathbb{R}^{d}\right), set

|  |  |  |
| --- | --- | --- |
|  | ⟨v,u⟩ℋ~01:=⟨v,u⟩L2+h​⟨ℒ​v,u⟩ℋ−1,ℋ01,\left\langle v,u\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}:=\left\langle v,u\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}v,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}, |  |

then, using [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have

|  |  |  |
| --- | --- | --- |
|  | ‖u‖ℋ~012=⟨u,u⟩ℋ~01=⟨u,u⟩L2+h​⟨ℒ​u,u⟩ℋ−1,ℋ01​{≤(1+h​M)​‖u‖ℋ012≥h​λ1​‖u‖ℋ012+(1−h​λ2)​‖u‖L22≥h​λ1​‖u‖ℋ012.\left\|u\right\|\_{\widetilde{\mathcal{H}}\_{0}^{1}}^{2}=\left\langle u,u\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}=\left\langle u,u\right\rangle\_{L^{2}}+h\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\begin{cases}\leq(1+hM)\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\\ \geq h\lambda\_{1}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}+(1-h\lambda\_{2})\left\|u\right\|\_{L^{2}}^{2}\geq h\lambda\_{1}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}.\end{cases} |  |

Hence, this inner product induces a norm on ℋ01​(ℝd)\mathcal{H}\_{0}^{1}\left(\mathbb{R}^{d}\right), denoted by ∥⋅∥ℋ~01\left\|\cdot\right\|\_{\widetilde{\mathcal{H}}\_{0}^{1}}, which is equivalent to ∥⋅∥ℋ01\left\|\cdot\right\|\_{\mathcal{H}\_{0}^{1}}.
In this case, we can rewrite 𝒯~​(v)​(x)=⟨v,Z​(x,⋅)⟩ℋ~01\widetilde{\mathcal{T}}\left(v\right)\left(x\right)=\left\langle v,Z(x,\cdot)\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}.

###### Proposition 4.4.

Assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and the coefficients of the PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) satisfy [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, 𝒯~\widetilde{\mathcal{T}} is a self-adjoint, positive definite, and trace class operator on ℋ01​(ℝd)\mathcal{H}^{1}\_{0}\left(\mathbb{R}^{d}\right) with inner product ⟨⋅,⋅⟩ℋ~01\left\langle\cdot,\cdot\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}} *i.e.*, for any u,v∈ℋ01​(ℝd)u,v\in\mathcal{H}\_{0}^{1}\left(\mathbb{R}^{d}\right) holds

|  |  |  |
| --- | --- | --- |
|  | ⟨𝒯~​(v),u⟩ℋ~01=⟨v,𝒯~​(u)⟩ℋ~01,⟨𝒯~​(v),v⟩ℋ~01>0​ for ​v≠0, and ∑i=1∞⟨𝒯~​(ei),ei⟩ℋ~01<+∞,\displaystyle\left\langle\widetilde{\mathcal{T}}\left(v\right),u\right\rangle\_{\widetilde{\mathcal{H}}^{1}\_{0}}=\left\langle v,\widetilde{\mathcal{T}}(u)\right\rangle\_{\widetilde{\mathcal{H}}^{1}\_{0}},\quad\left\langle\widetilde{\mathcal{T}}\left(v\right),v\right\rangle\_{\widetilde{\mathcal{H}}^{1}\_{0}}>0\ \text{ for }v\neq 0,\quad\text{ and }\quad\sum\_{i=1}^{\infty}\left\langle\widetilde{\mathcal{T}}\left(\mathrm{e}\_{i}\right),\mathrm{e}\_{i}\right\rangle\_{\widetilde{\mathcal{H}}^{1}\_{0}}<+\infty, |  |

where {ei}i=1∞\{\mathrm{e}\_{i}\}^{\infty}\_{i=1} is an orthogonal basis on ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) under the norm ⟨⋅,⋅⟩ℋ~01\left\langle\cdot,\cdot\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}.

###### Proof.

Let us first verify that 𝒯~\widetilde{\mathcal{T}} is self-adjoint and positive definite.
Using that

|  |  |  |
| --- | --- | --- |
|  | 𝒯~​(v)​(x)=⟨v,Z​(x,⋅)⟩ℋ~01=𝔼​[⟨v,X⟩ℋ~01⋅X],\widetilde{\mathcal{T}}\left(v\right)\left(x\right)=\left\langle v,Z(x,\cdot)\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}=\mathbb{E}\left[\left\langle v,X\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}\cdot X\right], |  |

taking the inner product yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝒯~​(v),u⟩ℋ~01\displaystyle\left\langle\widetilde{\mathcal{T}}\left(v\right),u\right\rangle\_{\tilde{\mathcal{H}}^{1}\_{0}} | =𝔼​[⟨v,X⟩ℋ~01⋅⟨u,X⟩ℋ~01]=⟨v,𝒯~​(u)⟩ℋ~01,\displaystyle=\mathbb{E}\left[\left\langle v,X\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}\cdot\left\langle u,X\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}\right]=\left\langle v,\widetilde{\mathcal{T}}(u)\right\rangle\_{\widetilde{\mathcal{H}}^{1}\_{0}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| and | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝒯~​(v),v⟩ℋ~01\displaystyle\left\langle\widetilde{\mathcal{T}}\left(v\right),v\right\rangle\_{\tilde{\mathcal{H}}^{1}\_{0}} | =𝔼​[|⟨v,X⟩ℋ~01|2]≥0.\displaystyle=\mathbb{E}\left[\left|\left\langle v,X\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}\right|^{2}\right]\geq 0. |  |

Next, let us verify that 𝔼​[|⟨v,X⟩ℋ~01|2]=0\mathbb{E}\left[\left|\left\langle v,X\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}\right|^{2}\right]=0 only if v=0v=0.
The first marginal of XX is ψ​(α01​x+c01)\psi\left(\alpha\_{0}^{1}x+c\_{0}^{1}\right) and we know from [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") that the random variables α01\alpha\_{0}^{1} and c01c\_{0}^{1} have full support.
Hence, 𝔼​[|⟨v,X⟩ℋ~01|2]=0\mathbb{E}\left[\left|\left\langle v,X\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}\right|^{2}\right]=0 implies ⟨v,w⟩ℋ~01=0\left\langle v,w\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}=0 for any w∈𝒞​(ψ)w\in\mathcal{C}\left(\psi\right).
Using that 𝒞​(ψ)\mathcal{C}\left(\psi\right) is dense in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}\left(\mathbb{R}^{d}\right) with the norm ∥⋅∥ℋ01\left\|\cdot\right\|\_{\mathcal{H}\_{0}^{1}}, see [Theorem 3.11](https://arxiv.org/html/2512.25017v1#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.4. Neural network approximation and a version of the Universal Approximation Theorem ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), then it is dense with the norm ∥⋅∥ℋ~01\left\|\cdot\right\|\_{\widetilde{\mathcal{H}}\_{0}^{1}} as well.
Therefore, v=0.v=0.

Finally, let us show that 𝒯~\widetilde{\mathcal{T}} is a trace class operator.
Using Parseval’s identity and [Lemma A.4](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem4 "Lemma A.4 (ℋ₀¹-boundedness of 𝑋). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have

|  |  |  |
| --- | --- | --- |
|  | ∑i=1∞⟨𝒯~​(ei),ei⟩ℋ~01=∑i=1∞𝔼​[|⟨ei,X⟩ℋ~01|2]=𝔼​[‖X‖ℋ~012]≤C​𝔼​[‖X‖ℋ012]<+∞.∎\sum\_{i=1}^{\infty}\left\langle\widetilde{\mathcal{T}}\left(\mathrm{e}\_{i}\right),\mathrm{e}\_{i}\right\rangle\_{\widetilde{\mathcal{H}}^{1}\_{0}}=\sum\_{i=1}^{\infty}\mathbb{E}\left[\left|\left\langle\mathrm{e}\_{i},X\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}\right|^{2}\right]=\mathbb{E}\left[\left\|X\right\|\_{\widetilde{\mathcal{H}}\_{0}^{1}}^{2}\right]\leq C\mathbb{E}\left[\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right]<+\infty.\qed |  |

###### Proof of [Theorem 4.3](https://arxiv.org/html/2512.25017v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2. Long time behavior of the gradient flow ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").

Using van Neerven [[30](https://arxiv.org/html/2512.25017v1#bib.bib30), Proposition 14.13], every trace class operator is compact and positive definite.
Therefore, we can do a spectral decomposition for the operator 𝒯~\widetilde{\mathcal{T}}.
There exists an orthogonal basis {e~i}i=1∞\{\tilde{\mathrm{e}}\_{i}\}^{\infty}\_{i=1}, such that

|  |  |  |
| --- | --- | --- |
|  | 𝒯~​(e~i)=γi​e~i,\displaystyle\widetilde{\mathcal{T}}\left(\tilde{\mathrm{e}}\_{i}\right)=\gamma\_{i}\tilde{\mathrm{e}}\_{i}, |  |

with γ1≥γ2≥⋯>0.\gamma\_{1}\geq\gamma\_{2}\geq\dots>0.
Set hti:=⟨Vt−w∗,e~i⟩ℋ~01h\_{t}^{i}:=\left\langle V\_{t}-w\_{\*},\tilde{\mathrm{e}}\_{i}\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}.
Then, using ([4.8](https://arxiv.org/html/2512.25017v1#S4.E8 "Equation 4.8 ‣ 4.2. Long time behavior of the gradient flow ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), we have

|  |  |  |
| --- | --- | --- |
|  | d​htid​t=⟨d​(Vt−w∗),e~i⟩ℋ~01d​t=−⟨𝒯~​(Vt−w∗),e~i⟩ℋ~01=−⟨Vt−w∗,𝒯~​e~i⟩ℋ~01=−γi​hti.\displaystyle\frac{\mathrm{d}h\_{t}^{i}}{\mathrm{d}t}=\frac{\left\langle\mathrm{d}\left(V\_{t}-w\_{\*}\right),\tilde{\mathrm{e}}\_{i}\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}}{\mathrm{d}t}=-\left\langle\widetilde{\mathcal{T}}\left(V\_{t}-w\_{\*}\right),\tilde{\mathrm{e}}\_{i}\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}=-\left\langle V\_{t}-w\_{\*},\widetilde{\mathcal{T}}\tilde{\mathrm{e}}\_{i}\right\rangle\_{\widetilde{\mathcal{H}}\_{0}^{1}}=-\gamma\_{i}h\_{t}^{i}. |  |

Therefore, hti=e−γi​t​h0ih\_{t}^{i}=\mathrm{e}^{-\gamma\_{i}t}h\_{0}^{i}.
Hence, using Parseval’s identity again, we get

|  |  |  |
| --- | --- | --- |
|  | ‖Vt−w∗‖ℋ~012=∑i=1∞(hti)2=∑i=1∞e−2​γi​t​(h0i)2,\displaystyle\left\|V\_{t}-w\_{\*}\right\|^{2}\_{\widetilde{\mathcal{H}}\_{0}^{1}}=\sum\_{i=1}^{\infty}\left(h^{i}\_{t}\right)^{2}=\sum\_{i=1}^{\infty}\mathrm{e}^{-2\gamma\_{i}t}\left(h\_{0}^{i}\right)^{2}, |  |

which converges to 0 because γi>0\gamma\_{i}>0 and ∑i=1∞(h0i)2=‖w∗‖ℋ~012<+∞.\sum\_{i=1}^{\infty}\left(h\_{0}^{i}\right)^{2}=\left\|w\_{\*}\right\|^{2}\_{\widetilde{\mathcal{H}}\_{0}^{1}}<+\infty.
Finally, since the norm ∥⋅∥ℋ~01\left\|\cdot\right\|\_{\widetilde{\mathcal{H}}\_{0}^{1}} is equivalent to ∥⋅∥ℋ01,\left\|\cdot\right\|\_{\mathcal{H}\_{0}^{1}}, we conclude

|  |  |  |
| --- | --- | --- |
|  | limt→∞‖Vt−w∗‖ℋ01=0.∎\lim\_{t\to\infty}\left\|V\_{t}-w\_{\*}\right\|\_{\mathcal{H}\_{0}^{1}}=0.\qed |  |

## Appendix A Auxiliary results

### A.1. Functional inequalities and norm estimates

In the first part of the appendix, we show that the Fréchet derivative of the loss function is continuous, and we also prove that the neural network and its wide network limit are bounded in the ℋ01\mathcal{H}\_{0}^{1}-norm.

###### Lemma A.1 (Continuity of the Fréchet derivative).

Assume that the operators of the PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) satisfy [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, the Fréchet derivative of the loss function is continuous, *i.e.* there exists a constant K>0K>0, such that for any u,v,wu,v,w in ℋ01​(ℝd)\mathcal{H}\_{0}^{1}(\mathbb{R}^{d}) holds

|  |  |  |
| --- | --- | --- |
|  | |⟨𝒟​Ik​(v),u⟩ℋ01−⟨𝒟​Ik​(w),u⟩ℋ01|≤K​‖v−w‖ℋ01​‖u‖ℋ01.\displaystyle\left|\left\langle\mathcal{D}I^{k}\left(v\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}-\left\langle\mathcal{D}I^{k}\left(w\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right|\leq K\left\|v-w\right\|\_{\mathcal{H}\_{0}^{1}}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}. |  |

In particular, by choosing w=0w=0, we have

|  |  |  |
| --- | --- | --- |
|  | |⟨𝒟​Ik​(v),u⟩ℋ01|≤K​(1+‖v‖ℋ01)​‖u‖ℋ01.\displaystyle\left|\left\langle\mathcal{D}I^{k}\left(v\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right|\leq K\left(1+\left\|v\right\|\_{\mathcal{H}\_{0}^{1}}\right)\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}. |  |

###### Proof.

Using the definition of the Fréchet derivative in ([4.2](https://arxiv.org/html/2512.25017v1#S4.E2 "Equation 4.2 ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), the triangle and Cauchy–Schwarz inequalities and [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |⟨𝒟​Ik​(v),u⟩ℋ01−⟨𝒟​Ik​(w),u⟩ℋ01|\displaystyle\left|\left\langle\mathcal{D}I^{k}\left(v\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}-\left\langle\mathcal{D}I^{k}\left(w\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right| | =|⟨v−w,u⟩L2+h2​⟨ℒ​(v−w),u⟩ℋ−1,ℋ01|\displaystyle=\left|\left\langle v-w,u\right\rangle\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}(v-w),u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖v−w‖L2​‖u‖L2+h​M2​‖v−w‖ℋ01​‖u‖ℋ01\displaystyle\leq\left\|v-w\right\|\_{L^{2}}\left\|u\right\|\_{L^{2}}+\frac{hM}{2}\left\|v-w\right\|\_{\mathcal{H}\_{0}^{1}}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​‖v−w‖ℋ01​‖u‖ℋ01.\displaystyle\leq K\left\|v-w\right\|\_{\mathcal{H}\_{0}^{1}}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}. |  |

Setting w=0w=0 and using again the Cauchy–Schwarz inequality and [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |⟨𝒟​Ik​(0),u⟩ℋ01|\displaystyle\left|\left\langle\mathcal{D}I^{k}\left(0\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right| | =|−⟨Uk−1,u⟩L2+h​⟨F​(Uk−1),u⟩L2|\displaystyle=\left|-\left\langle U^{k-1},u\right\rangle\_{L^{2}}+h\left\langle F(U^{k-1}),u\right\rangle\_{L^{2}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖Uk−1‖L2​‖u‖L2+h​‖F​(Uk−1)‖L2​‖u‖L2≤K​‖u‖ℋ01,\displaystyle\leq\left\|U^{k-1}\right\|\_{L^{2}}\left\|u\right\|\_{L^{2}}+h\left\|F(U^{k-1})\right\|\_{L^{2}}\left\|u\right\|\_{L^{2}}\leq K\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}, |  |

since Uk−1∈ℋ01U^{k-1}\in\mathcal{H}\_{0}^{1}.
Then, combining the two results and using the triangle inequality, we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | |⟨𝒟​Ik​(v),u⟩ℋ01|\displaystyle\left|\left\langle\mathcal{D}I^{k}\left(v\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right| | =|⟨𝒟​Ik​(v),u⟩ℋ01−⟨𝒟​Ik​(0),u⟩ℋ01+⟨𝒟​Ik​(0),u⟩ℋ01|\displaystyle=\left|\left\langle\mathcal{D}I^{k}\left(v\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}-\left\langle\mathcal{D}I^{k}\left(0\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}+\left\langle\mathcal{D}I^{k}\left(0\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|⟨𝒟​Ik​(v),u⟩ℋ01−⟨𝒟​Ik​(0),u⟩ℋ01|+|⟨𝒟​Ik​(0),u⟩ℋ01|\displaystyle\leq\left|\left\langle\mathcal{D}I^{k}\left(v\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}-\left\langle\mathcal{D}I^{k}\left(0\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right|+\left|\left\langle\mathcal{D}I^{k}\left(0\right),u\right\rangle\_{\mathcal{H}\_{0}^{1}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​(1+‖v‖ℋ01)​‖u‖ℋ01.∎\displaystyle\leq K\left(1+\left\|v\right\|\_{\mathcal{H}\_{0}^{1}}\right)\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}.\qed |  |

###### Lemma A.2.

Assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and the operators of the PDE ([2.1](https://arxiv.org/html/2512.25017v1#S2.E1 "Equation 2.1 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"))–([2.2](https://arxiv.org/html/2512.25017v1#S2.E2 "Equation 2.2 ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")) satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, we have the following inequalities, for all t≥0,t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖Vtn‖ℋ012]≤Cψ and ‖Vt‖ℋ012≤Cψ,\displaystyle\mathbb{E}\left[\left\|V^{n}\_{t}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right]\leq C\_{\psi}\quad\text{ and }\quad\left\|V\_{t}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\leq C\_{\psi}, |  |

where CψC\_{\psi} is a positive constant that only depends on the activation function ψ\psi.

###### Proof.

Let us first show that Ik​(Vtn)I^{k}\left(V\_{t}^{n}\right) is not increasing in tt.
According to ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex5 "4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), we have

|  |  |  |
| --- | --- | --- |
|  | d​Ik​(Vtn)d​t=∇θIk​(Vtn)⋅d​θtnd​t=−ηn​|∇θIk​(Vn​(θtn;x))|2≤0.\frac{\mathrm{d}I^{k}\left(V\_{t}^{n}\right)}{\mathrm{d}t}=\nabla\_{\theta}I^{k}\left(V\_{t}^{n}\right)\cdot\frac{\mathrm{d}\theta\_{t}^{n}}{\mathrm{d}t}=-\eta\_{n}\left|\nabla\_{\theta}I^{k}\left(V^{n}\left(\theta\_{t}^{n};x\right)\right)\right|^{2}\leq 0. |  |

This inequality readily implies Ik​(Vtn)≤Ik​(V0n)I^{k}\left(V\_{t}^{n}\right)\leq I^{k}\left(V\_{0}^{n}\right).
Using [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), the Cauchy–Schwarz inequality and a​b≤a2+b22ab\leq\frac{a^{2}+b^{2}}{2}, we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ik​(u)\displaystyle I^{k}(u) | =12​‖u−Uk−1‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01+h​⟨F​(Uk−1),u⟩L2\displaystyle=\frac{1}{2}\left\|u-U^{k-1}\right\|\_{L^{2}}^{2}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+h\left\langle F\left(U^{k-1}\right),u\right\rangle\_{L^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​‖u‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01+⟨h​F​(Uk−1)−Uk−1,u⟩L2+12​‖Uk−1‖L22\displaystyle=\frac{1}{2}\left\|u\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+\left\langle hF\left(U^{k-1}\right)-U^{k-1},u\right\rangle\_{L^{2}}+\frac{1}{2}\left\|U^{k-1}\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​‖u‖L22+h​M2​‖u‖ℋ012+‖h​F​(Uk−1)−Uk−1‖L2​‖u‖L2+12​‖Uk−1‖L22\displaystyle\leq\frac{1}{2}\left\|u\right\|^{2}\_{L^{2}}+\frac{hM}{2}\left\|u\right\|^{2}\_{\mathcal{H}\_{0}^{1}}+\left\|hF(U^{k-1})-U^{k-1}\right\|\_{L^{2}}\left\|u\right\|\_{L^{2}}+\frac{1}{2}\left\|U^{k-1}\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖u‖L22+h​M2​‖u‖ℋ012+12​‖h​F​(Uk−1)−Uk−1‖L22+12​‖Uk−1‖L22\displaystyle\leq\left\|u\right\|^{2}\_{L^{2}}+\frac{hM}{2}\left\|u\right\|^{2}\_{\mathcal{H}\_{0}^{1}}+\frac{1}{2}\left\|hF(U^{k-1})-U^{k-1}\right\|\_{L^{2}}^{2}+\frac{1}{2}\left\|U^{k-1}\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C1​‖u‖ℋ012+C2.\displaystyle=C\_{1}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}+C\_{2}. |  |

Moreover, using [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), the Cauchy–Schwarz inequality again and the inequality

|  |  |  |
| --- | --- | --- |
|  | ‖m‖L2​‖n‖L2≤λ2​‖m‖L22+12​λ​‖v‖L22​ with ​λ=h​λ12,\left\|m\right\|\_{L^{2}}\left\|n\right\|\_{L^{2}}\leq\frac{\lambda}{2}\left\|m\right\|\_{L^{2}}^{2}+\frac{1}{2\lambda}\left\|v\right\|\_{L^{2}}^{2}\text{ with }\lambda=\frac{h\lambda\_{1}}{2}, |  |

we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ik​(u)\displaystyle I^{k}(u) | =12​‖u‖L22+h2​⟨ℒ​u,u⟩ℋ−1,ℋ01+⟨h​F​(Uk−1)−Uk−1,u⟩L2+12​‖Uk−1‖L22\displaystyle=\frac{1}{2}\left\|u\right\|^{2}\_{L^{2}}+\frac{h}{2}\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}+\left\langle hF\left(U^{k-1}\right)-U^{k-1},u\right\rangle\_{L^{2}}+\frac{1}{2}\left\|U^{k-1}\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥(12−h​λ22)​‖u‖L22+h​λ12​‖u‖ℋ012−‖h​F​(Uk−1)−Uk−1‖L2​‖u‖L2−12​‖Uk−1‖L22\displaystyle\geq\left(\frac{1}{2}-\frac{h\lambda\_{2}}{2}\right)\left\|u\right\|^{2}\_{L^{2}}+\frac{h\lambda\_{1}}{2}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-\left\|hF\left(U^{k-1}\right)-U^{k-1}\right\|\_{L^{2}}\left\|u\right\|\_{L^{2}}-\frac{1}{2}\left\|U^{k-1}\right\|\_{L\_{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥(12−h​λ22)​‖u‖L22+h​λ14​‖u‖ℋ012−1h​λ1​‖h​F​(Uk−1)−Uk−1‖L22−12​‖Uk−1‖L22\displaystyle\geq\left(\frac{1}{2}-\frac{h\lambda\_{2}}{2}\right)\left\|u\right\|^{2}\_{L^{2}}+\frac{h\lambda\_{1}}{4}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-\frac{1}{h\lambda\_{1}}\left\|hF\left(U^{k-1}\right)-U^{k-1}\right\|\_{L^{2}}^{2}-\frac{1}{2}\left\|U^{k-1}\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C3​‖u‖ℋ012−C4.\displaystyle=C\_{3}\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}-C\_{4}. |  |

Therefore, since Ik​(Vtn)I^{k}\left(V\_{t}^{n}\right) is not increasing with tt and using [Lemma 4.2](https://arxiv.org/html/2512.25017v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖Vtn‖ℋ012]\displaystyle\mathbb{E}\left[\left\|V^{n}\_{t}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right] | ≤𝔼​[1C3​Ik​(Vtn)+C4C3]≤𝔼​[1C3​Ik​(V0n)+C4C3]\displaystyle\leq\mathbb{E}\left[\frac{1}{C\_{3}}I^{k}\left(V^{n}\_{t}\right)+\frac{C\_{4}}{C\_{3}}\right]\leq\mathbb{E}\left[\frac{1}{C\_{3}}I^{k}\left(V\_{0}^{n}\right)+\frac{C\_{4}}{C\_{3}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[C1C3​‖V0n‖ℋ012+C2+C4C3]≤Cψ.\displaystyle\leq\mathbb{E}\left[\frac{C\_{1}}{C\_{3}}\left\|V^{n}\_{0}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}+\frac{C\_{2}+C\_{4}}{C\_{3}}\right]\leq C\_{\psi}. |  |

Using similar arguments, we get

|  |  |  |
| --- | --- | --- |
|  | d​Ik​(Vt)d​t=⟨𝒟​Ik​(Vt),d​Vtd​t⟩ℋ01=−|⟨𝒟​Ik​(Vt),𝔼​[∇θβ0​ψ​(α0​x+c0)]⟩ℋ01|2≤0.\displaystyle\frac{\mathrm{d}I^{k}\left(V\_{t}\right)}{\mathrm{d}t}=\left\langle\mathcal{D}I^{k}\left(V\_{t}\right),\frac{\mathrm{d}V\_{t}}{\mathrm{d}t}\right\rangle\_{\mathcal{H}\_{0}^{1}}=-\left|\left\langle\mathcal{D}I^{k}\left(V\_{t}\right),\mathbb{E}\left[\nabla\_{\theta}\beta\_{0}\psi\left(\alpha\_{0}x+c\_{0}\right)\right]\right\rangle\_{\mathcal{H}\_{0}^{1}}\right|^{2}\leq 0. |  |

This inequality yields that Ik​(Vt)≤Ik​(V0)=Ik​(0)I^{k}\left(V\_{t}\right)\leq I^{k}\left(V\_{0}\right)=I^{k}\left(0\right), hence ‖Vt‖ℋ012≤Cψ.\left\|V\_{t}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\leq C\_{\psi}.
∎

### A.2. Gradient θ\theta estimates

This subsection contains several useful results concerning gradient estimates of the neurons of the neural network with respect to its parameters.
Moreover, we show that gradients of the neurons are Lipschitz continuous with respect to the parameters θ\theta of the network, that they converge to their “unclipped” analogs for large nn, and we estimate the distance between the parameters as the training progresses.

###### Lemma A.3 (ℋ01\mathcal{H}\_{0}^{1}-boundedness of XnX^{n}).

Let θ∈ℝ×ℝ×ℝd\theta\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^{d}, then XnX^{n} is bounded in ℋ01\mathcal{H}\_{0}^{1}, *i.e.* there exists a constant Cψ>0C\_{\psi}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Xn​(θ)‖ℋ012\displaystyle\left\|X^{n}(\theta)\right\|^{2}\_{\mathcal{H}\_{0}^{1}} | ≤Cψ​(rn)d+8.\displaystyle\leq C\_{\psi}\left(r\_{n}\right)^{d+8}. |  |

###### Proof.

The derivatives of a neuron with respect to its parameters equal

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂β​β^​ψ​(α^​x+c^)\displaystyle\frac{\partial}{\partial\beta}\hat{\beta}\psi\left(\hat{\alpha}x+\hat{c}\right) | =ψ​(α^​x+c^)​𝟏{|β|≤rn},\displaystyle=\psi\left(\hat{\alpha}x+\hat{c}\right)\mathbf{1}\_{\{\left|\beta\right|\leq r\_{n}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂α​β^​ψ​(α^​x+c^)\displaystyle\frac{\partial}{\partial\alpha}\hat{\beta}\psi\left(\hat{\alpha}x+\hat{c}\right) | =β^​x𝖳​(∇ψ)​(α^​x+c^)​𝟏{1rn≤|α|≤rn},\displaystyle=\hat{\beta}x^{\mathsf{T}}\left(\nabla\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\mathbf{1}\_{\{\frac{1}{r\_{n}}\leq\left|\alpha\right|\leq r\_{n}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂c​β^​ψ​(α^​x+c^)\displaystyle\frac{\partial}{\partial c}\hat{\beta}\psi\left(\hat{\alpha}x+\hat{c}\right) | =β^​(∇ψ)​(α^​x+c^)​𝟏{|c|≤rn}.\displaystyle=\hat{\beta}\left(\nabla\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\mathbf{1}\_{\{\left|c\right|\leq r\_{n}\}}. |  |

Therefore, we obtain the bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Xn​(θ)|\displaystyle\left|X^{n}(\theta)\right| | =|∂∂β​β^​ψ​(α^​x+c^)+∂∂α​β^​ψ​(α^​x+c^)+∂∂c​β^​ψ​(α^​x+c^)|\displaystyle=\left|\frac{\partial}{\partial\beta}\hat{\beta}\psi\left(\hat{\alpha}x+\hat{c}\right)+\frac{\partial}{\partial\alpha}\hat{\beta}\psi\left(\hat{\alpha}x+\hat{c}\right)+\frac{\partial}{\partial c}\hat{\beta}\psi\left(\hat{\alpha}x+\hat{c}\right)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|ψ​(α^​x+c^)​𝟏{|β|≤rn}|+|β^​x𝖳​(∇ψ)​(α^​x+c^)​𝟏{1rn≤|α|≤rn}|+|β^​(∇ψ)​(α^​x+c^)​𝟏{|c|≤rn}|\displaystyle\leq\left|\psi\left(\hat{\alpha}x+\hat{c}\right)\mathbf{1}\_{\{\left|\beta\right|\leq r\_{n}\}}\right|+\left|\hat{\beta}x^{\mathsf{T}}\left(\nabla\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\mathbf{1}\_{\{\frac{1}{r\_{n}}\leq\left|\alpha\right|\leq r\_{n}\}}\right|+\left|\hat{\beta}\left(\nabla\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\mathbf{1}\_{\{\left|c\right|\leq r\_{n}\}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|ψ​(α^​x+c^)|+rn​|x⋅∇ψ​(α^​x+c^)|+rn​|(∇ψ)​(α^​x+c^)|.\displaystyle\leq\left|\psi\left(\hat{\alpha}x+\hat{c}\right)\right|+r\_{n}\left|x\cdot\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)\right|+r\_{n}\left|\left(\nabla\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\right|. |  |

The second term above can be bounded by

|  |  |  |
| --- | --- | --- |
|  | rn​|x⋅∇ψ​(α^​x+c^)|≤rn​(α^n)−1​(|(α^n​x+c^)⋅∇ψ​(α^​x+c^)|+|c^⋅∇ψ​(α^​x+c^)|)≤Cψ​(rn)3.\displaystyle r\_{n}\left|x\cdot\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)\right|\leq r\_{n}(\hat{\alpha}\_{n})^{-1}\Big(\left|(\hat{\alpha}\_{n}x+\hat{c})\cdot\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)\right|+\left|\hat{c}\cdot\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)\right|\Big)\leq C\_{\psi}(r\_{n})^{3}. |  |

Therefore, using that |α^|≥(rn)−1\left|\hat{\alpha}\right|\geq(r\_{n})^{-1}, we have

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|Xn​(θ)|2​dx≤∫ℝd|ψ​(α^​x+c^)|2​dx+(rn)2​∫ℝd|x|2​|(∇ψ)​(α^​x+c^)|2​dx+(rn)2​∫ℝd|(∇ψ)​(α^​x+c^)|2​dx=(y=α^​x)|α^|−d​∫ℝd|ψ​(y+c^)|2​dy+(rn)2​|α^|−d−2​∫ℝd|y|2​|(∇ψ)​(y+c^)|2​dy+(rn)2​|α^|−d​∫ℝd|(∇ψ)​(y+c^)|2​dy≤(z=y+c^)(rn)d​∫ℝd|ψ​(z)|2​dz+(rn)d+4​∫ℝd|z−c^|2​|(∇ψ)​(z)|2​dz+(rn)d+2​∫ℝd|(∇ψ)​(z)|2​dz≤Cψ​(rn)d+6\int\_{\mathbb{R}^{d}}\left|X^{n}(\theta)\right|^{2}\mathrm{d}x\\ \leq\int\_{\mathbb{R}^{d}}\left|\psi\left(\hat{\alpha}x+\hat{c}\right)\right|^{2}\mathrm{d}x+(r\_{n})^{2}\int\_{\mathbb{R}^{d}}\left|x\right|^{2}\left|(\nabla\psi)\left(\hat{\alpha}x+\hat{c}\right)\right|^{2}\mathrm{d}x+(r\_{n})^{2}\int\_{\mathbb{R}^{d}}\left|\left(\nabla\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\right|^{2}\mathrm{d}x\\ \stackrel{{\scriptstyle\left(y=\hat{\alpha}x\right)}}{{=}}\left|\hat{\alpha}\right|^{-d}\int\_{\mathbb{R}^{d}}\left|\psi\left(y+\hat{c}\right)\right|^{2}\mathrm{d}y+(r\_{n})^{2}\left|\hat{\alpha}\right|^{-d-2}\int\_{\mathbb{R}^{d}}\left|y\right|^{2}\left|\left(\nabla\psi\right)\left(y+\hat{c}\right)\right|^{2}\mathrm{d}y\\ \quad+(r\_{n})^{2}\left|\hat{\alpha}\right|^{-d}\int\_{\mathbb{R}^{d}}\left|\left(\nabla\psi\right)\left(y+\hat{c}\right)\right|^{2}\mathrm{d}y\\ \stackrel{{\scriptstyle\left(z=y+\hat{c}\right)}}{{\leq}}(r\_{n})^{d}\int\_{\mathbb{R}^{d}}\left|\psi\left(z\right)\right|^{2}\mathrm{d}z+(r\_{n})^{d+4}\int\_{\mathbb{R}^{d}}\left|z-\hat{c}\right|^{2}\left|\left(\nabla\psi\right)\left(z\right)\right|^{2}\mathrm{d}z+(r\_{n})^{d+2}\int\_{\mathbb{R}^{d}}\left|\left(\nabla\psi\right)\left(z\right)\right|^{2}\mathrm{d}z\\ \leq C\_{\psi}(r\_{n})^{d+6} |  |

Analogously we can estimate the gradient, and we get that,

|  |  |  |
| --- | --- | --- |
|  | |∇xXn​(θ)|≤2​rn​|∇ψ​(α^​x+c^)|+(rn)2​|x|​|(D2​ψ)​(α^​x+c^)|+(rn)2​|(D2​ψ)​(α^​x+c^)|,\displaystyle\left|\nabla\_{x}X^{n}(\theta)\right|\leq 2r\_{n}\left|\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)\right|+\left(r\_{n}\right)^{2}\left|x\right|\left|\left(D^{2}\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\right|+(r\_{n})^{2}\left|\left(D^{2}\psi\right)\left(\hat{\alpha}x+\hat{c}\right)\right|, |  |

hence

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|∇xXn​(θ)|2​dx≤Cψ​(rn)d+8.\int\_{\mathbb{R}^{d}}\left|\nabla\_{x}X^{n}(\theta)\right|^{2}\mathrm{d}x\leq C\_{\psi}(r\_{n})^{d+8}. |  |

Finally, we arrive at

|  |  |  |
| --- | --- | --- |
|  | ‖Xn​(θ)‖ℋ012=∫ℝd|Xn​(θ)|2+|∇xXn​(θ)|2​d​x≤Cψ​(rn)d+8.∎\left\|X^{n}(\theta)\right\|^{2}\_{\mathcal{H}\_{0}^{1}}=\int\_{\mathbb{R}^{d}}\left|X^{n}(\theta)\right|^{2}+\left|\nabla\_{x}X^{n}(\theta)\right|^{2}\mathrm{d}x\leq C\_{\psi}\left(r\_{n}\right)^{d+8}.\qed |  |

###### Lemma A.4 (ℋ01\mathcal{H}\_{0}^{1}-boundedness of XX).

Let θ∈ℝ×ℝ×ℝd\theta\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^{d}, and assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, XX is bounded in ℋ01\mathcal{H}\_{0}^{1}, *i.e.* there exists a constant Cψ>0C\_{\psi}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖X​(θ)‖ℋ012≤Cψ​(1+β2)​(1+c2)​(|α|−d+|α|−d−2+|α|2−d).\displaystyle\left\|X(\theta)\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\leq C\_{\psi}\left(1+\beta^{2}\right)\left(1+c^{2}\right)\left(\left|\alpha\right|^{-d}+\left|\alpha\right|^{-d-2}+\left|\alpha\right|^{2-d}\right). |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖X‖ℋ012]<+∞ and supn≥1𝔼​[‖Xn‖ℋ012]<+∞.\displaystyle\mathbb{E}\left[\left\|X\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]<+\infty\quad\text{ and }\quad\sup\_{n\geq 1}\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]<+\infty. |  |

###### Proof.

Let us first consider the L2L^{2}-norm of X​(θ)X(\theta).
As in the proof of [Lemma A.3](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem3 "Lemma A.3 (ℋ₀¹-boundedness of 𝑋^𝑛). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖X​(θ)‖L22\displaystyle\left\|X(\theta)\right\|\_{L^{2}}^{2} | ≤∫ℝd|ψ​(α​x+c)|2​dx+β2​∫ℝd|x|2​|(∇ψ)​(α​x+c)|2​dx+β2​∫ℝd|(∇ψ)​(α​x+c)|2​dx\displaystyle\leq\int\_{\mathbb{R}^{d}}\left|\psi\left(\alpha x+c\right)\right|^{2}\mathrm{d}x+\beta^{2}\int\_{\mathbb{R}^{d}}\left|x\right|^{2}\left|\left(\nabla\psi\right)\left(\alpha x+c\right)\right|^{2}\mathrm{d}x+\beta^{2}\int\_{\mathbb{R}^{d}}\left|\left(\nabla\psi\right)\left(\alpha x+c\right)\right|^{2}\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|α|−d​∫ℝd|ψ​(z)|2​dz+β2​|α|−d−2​∫ℝd|z−c|2​|(∇ψ)​(z)|2​dz+β2​|α|−d​∫ℝd|(∇ψ)​(z)|2​dz\displaystyle=\left|\alpha\right|^{-d}\int\_{\mathbb{R}^{d}}\left|\psi\left(z\right)\right|^{2}\mathrm{d}z+\beta^{2}\left|\alpha\right|^{-d-2}\int\_{\mathbb{R}^{d}}\left|z-c\right|^{2}\left|\left(\nabla\psi\right)\left(z\right)\right|^{2}\mathrm{d}z+\beta^{2}\left|\alpha\right|^{-d}\int\_{\mathbb{R}^{d}}\left|\left(\nabla\psi\right)\left(z\right)\right|^{2}\mathrm{d}z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​(1+β2)​(1+|c|2)​(|α|−d+|α|−d−2),\displaystyle\leq C\_{\psi}\left(1+\beta^{2}\right)\left(1+\left|c\right|^{2}\right)\left(\left|\alpha\right|^{-d}+\left|\alpha\right|^{-d-2}\right), |  |

where we have used the change of variables z=α​x+cz=\alpha x+c for the equality in the second step.
Analogously, we have that

|  |  |  |
| --- | --- | --- |
|  | ‖∇X​(θ)‖L22≤Cψ​(1+β2)​(1+|c|2)​(|α|−d+|α|2−d).\left\|\nabla X(\theta)\right\|\_{L^{2}}^{2}\leq C\_{\psi}\left(1+\beta^{2}\right)\left(1+\left|c\right|^{2}\right)\left(\left|\alpha\right|^{-d}+\left|\alpha\right|^{2-d}\right). |  |

Combining these two results, we recover the ℋ01\mathcal{H}^{1}\_{0}-estimate of X​(θ)X(\theta).
Taking expectations on the ℋ01\mathcal{H}^{1}\_{0}-estimate of X​(θ)X(\theta) and using [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖X‖ℋ012]\displaystyle\mathbb{E}\left[\left\|X\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right] | ≤Cψ​𝔼​[1+|β01|2]​𝔼​[1+|c01|2]​𝔼​[|α01|−d+|α01|−d−2+|α01|2−d]<+∞,\displaystyle\leq C\_{\psi}\mathbb{E}\left[1+\left|\beta^{1}\_{0}\right|^{2}\right]\mathbb{E}\left[1+\left|c^{1}\_{0}\right|^{2}\right]\mathbb{E}\left[\left|\alpha\_{0}^{1}\right|^{-d}+\left|\alpha\_{0}^{1}\right|^{-d-2}+\left|\alpha\_{0}^{1}\right|^{2-d}\right]<+\infty, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| while using the ℋ01\mathcal{H}^{1}\_{0}-estimate of Xn​(θ)X^{n}(\theta) from the previous lemma, we arrive at | | | | |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖Xn‖ℋ012]\displaystyle\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right] | ≤Cψ​𝔼​[1+|β^01|2]​𝔼​[1+|c^01|2]​𝔼​[|α^01|−d+|α^01|−d−2+|α^01|2−d]\displaystyle\leq C\_{\psi}\mathbb{E}\left[1+\left|\hat{\beta}^{1}\_{0}\right|^{2}\right]\mathbb{E}\left[1+\left|\hat{c}^{1}\_{0}\right|^{2}\right]\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{1}\right|^{-d}+\left|\hat{\alpha}\_{0}^{1}\right|^{-d-2}+\left|\hat{\alpha}\_{0}^{1}\right|^{2-d}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​𝔼​[1+|β01|2]​𝔼​[1+|c01|2]⏟<+∞​𝔼​[|α^01|−d+|α^01|−d−2+|α^01|2−d].\displaystyle\leq C\_{\psi}\underbrace{\mathbb{E}\left[1+\left|\beta^{1}\_{0}\right|^{2}\right]\mathbb{E}\left[1+\left|c^{1}\_{0}\right|^{2}\right]}\_{<+\infty}\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{1}\right|^{-d}+\left|\hat{\alpha}\_{0}^{1}\right|^{-d-2}+\left|\hat{\alpha}\_{0}^{1}\right|^{2-d}\right]. |  |

Using a similar reasoning as in the proof of [Lemma 4.2](https://arxiv.org/html/2512.25017v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), if d=1,2d=1,2,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|α^01|−d+|α^01|−d−2+|α^01|2−d]≤𝔼​[|α01|−d+|α01|−d−2+(rn)−d+(rn)−d−2+|α01|+1]<∞,\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{1}\right|^{-d}+\left|\hat{\alpha}\_{0}^{1}\right|^{-d-2}+\left|\hat{\alpha}\_{0}^{1}\right|^{2-d}\right]\leq\mathbb{E}\left[\left|\alpha\_{0}^{1}\right|^{-d}+\left|\alpha\_{0}^{1}\right|^{-d-2}+\left(r\_{n}\right)^{-d}+\left(r\_{n}\right)^{-d-2}+\left|\alpha\_{0}^{1}\right|+1\right]<\infty, |  |

and if d≥3d\geq 3,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|α^01|−d+|α^01|−d−2+|α^01|2−d]\displaystyle\mathbb{E}\left[\left|\hat{\alpha}\_{0}^{1}\right|^{-d}+\left|\hat{\alpha}\_{0}^{1}\right|^{-d-2}+\left|\hat{\alpha}\_{0}^{1}\right|^{2-d}\right] | ≤𝔼​[|α01|−d+|α01|−d−2+(rn)−d+(rn)−d−2+|α01|2−d+(rn)2−d]\displaystyle\leq\mathbb{E}\left[\left|\alpha\_{0}^{1}\right|^{-d}+\left|\alpha\_{0}^{1}\right|^{-d-2}+\left(r\_{n}\right)^{-d}+\left(r\_{n}\right)^{-d-2}+\left|\alpha\_{0}^{1}\right|^{2-d}+\left(r\_{n}\right)^{2-d}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <∞.\displaystyle<\infty. |  |

Therefore, supn≥1𝔼​[‖Xn‖ℋ012]<+∞.\sup\_{n\geq 1}\mathbb{E}\left[\left\|X^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]<+\infty.
∎

###### Lemma A.5.

Assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then

|  |  |  |
| --- | --- | --- |
|  | εn:=𝔼​[‖Xn−X‖ℋ012]→n→∞0.\displaystyle{\varepsilon}\_{n}:=\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right]\xrightarrow[n\to\infty]{}0. |  |

###### Proof.

Let us decompose εn{\varepsilon}\_{n} as follows,

|  |  |  |
| --- | --- | --- |
|  | εn=𝔼​[‖Xn−X‖ℋ012​{𝟏|β01|≤rn,|α01|≤rn,|c01|≤rn+𝟏|β01|>rn,|α01|≤rn,|c01|≤rn+𝟏|α01|>rn,|c01|≤rn+𝟏|c01|>rn}],\displaystyle{\varepsilon}\_{n}=\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\left\{\boldsymbol{1}\_{\left|\beta\_{0}^{1}\right|\leq r\_{n},\left|\alpha\_{0}^{1}\right|\leq r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}}+\boldsymbol{1}\_{\left|\beta\_{0}^{1}\right|>r\_{n},\left|\alpha\_{0}^{1}\right|\leq r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}}+\boldsymbol{1}\_{\left|\alpha\_{0}^{1}\right|>r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}}+\boldsymbol{1}\_{\left|c\_{0}^{1}\right|>r\_{n}}\right\}\right], |  |

and then we treat each summand separately.

Term 1.
By definition ‖Xn−X‖ℋ012​𝟏{|β01|≤rn,|α01|≤rn,|c01|≤rn}=0.\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\boldsymbol{1}\_{\{\left|\beta\_{0}^{1}\right|\leq r\_{n},\left|\alpha\_{0}^{1}\right|\leq r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}\}}=0.

Term 2.
Let |β01|>rn\left|\beta\_{0}^{1}\right|>r\_{n} and |α01|≤rn\left|\alpha\_{0}^{1}\right|\leq r\_{n}, then ‖Xn‖ℋ01≤‖X‖ℋ01\left\|X^{n}\right\|\_{\mathcal{H}\_{0}^{1}}\leq\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}.
Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖Xn−X‖ℋ012​𝟏{|β01|>rn,|α01|≤rn,|c01|≤rn}]≤2​𝔼​[‖X‖ℋ012​𝟏{|β01|>rn,|α01|≤rn,|c01|≤rn}],\mathbb{E}\left[\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\boldsymbol{1}\_{\{\left|\beta\_{0}^{1}\right|>r\_{n},\left|\alpha\_{0}^{1}\right|\leq r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}\}}\right]\leq 2\mathbb{E}\left[\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\boldsymbol{1}\_{\{\left|\beta\_{0}^{1}\right|>r\_{n},\left|\alpha\_{0}^{1}\right|\leq r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}\}}\right], |  |

which converges to 0 by the dominated convergence theorem.

Terms 3 & 4.
The following inequality holds in this case

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Xn−X‖ℋ012\displaystyle\left\|X^{n}-X\right\|\_{\mathcal{H}\_{0}^{1}}^{2} | (𝟏{|α01|>rn,|c01|≤rn}+𝟏|c01|>rn)\displaystyle\Big(\boldsymbol{1}\_{\{\left|\alpha\_{0}^{1}\right|>r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}\}}+\boldsymbol{1}\_{\left|c\_{0}^{1}\right|>r\_{n}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​(‖Xn‖ℋ012+‖X‖ℋ012)​(𝟏{|α01|>rn,|c01|≤rn}+𝟏|c01|>rn).\displaystyle\leq 2\left(\left\|X^{n}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}+\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\right)\Big(\boldsymbol{1}\_{\{\left|\alpha\_{0}^{1}\right|>r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}\}}+\boldsymbol{1}\_{\left|c\_{0}^{1}\right|>r\_{n}}\Big). |  |

Using the dominated convergence theorem, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖X‖ℋ012​(𝟏{|α01|>rn,|c01|≤rn}+𝟏|c01|>rn})]→n→∞0.\displaystyle\mathbb{E}\left[\left\|X\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\Big(\boldsymbol{1}\_{\{\left|\alpha\_{0}^{1}\right|>r\_{n},\left|c\_{0}^{1}\right|\leq r\_{n}\}}+\boldsymbol{1}\_{\left|c\_{0}^{1}\right|>r\_{n}\}}\Big)\right]\xrightarrow[n\to\infty]{}0. |  |

Moreover, applying [Lemma A.3](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem3 "Lemma A.3 (ℋ₀¹-boundedness of 𝑋^𝑛). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we arrive at

|  |  |  |
| --- | --- | --- |
|  | ‖Xn‖ℋ012​(𝟏{|α01|>rn}+𝟏{|c01|>rn})≤Cψ​(rn)d+8​(𝟏{|α01|>rn}+𝟏{|c01|>rn}),\displaystyle\left\|X^{n}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\Big(\boldsymbol{1}\_{\{\left|\alpha\_{0}^{1}\right|>r\_{n}\}}+\boldsymbol{1}\_{\{\left|c\_{0}^{1}\right|>r\_{n}\}}\Big)\leq C\_{\psi}(r\_{n})^{d+8}\Big(\boldsymbol{1}\_{\{\left|\alpha\_{0}^{1}\right|>r\_{n}\}}+\boldsymbol{1}\_{\{\left|c\_{0}^{1}\right|>r\_{n}\}}\Big), |  |

which converges to 0 almost surely.
Therefore, using the dominated convergence theorem once again, we get

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖Xn‖ℋ012​(𝟏{|α01|>rn}+𝟏{|c01|>rn})]≤𝔼​[|α01|d+8​𝟏{|α01|>rn}+|c01|d+8​𝟏{|c01|>rn}]→n→∞0.∎\mathbb{E}\left[\left\|X^{n}\right\|\_{\mathcal{H}\_{0}^{1}}^{2}\Big(\boldsymbol{1}\_{\{\left|\alpha\_{0}^{1}\right|>r\_{n}\}}+\boldsymbol{1}\_{\{\left|c\_{0}^{1}\right|>r\_{n}\}}\Big)\right]\leq\mathbb{E}\Big[\left|\alpha\_{0}^{1}\right|^{d+8}\boldsymbol{1}\_{\{\left|\alpha\_{0}^{1}\right|>r\_{n}\}}+\left|c\_{0}^{1}\right|^{d+8}\boldsymbol{1}\_{\{\left|c\_{0}^{1}\right|>r\_{n}\}}\Big]\xrightarrow[n\to\infty]{}0.\qed |  |

###### Lemma A.6 (θ\theta-Lipschitz continuity).

Let θ,θ′∈ℝ×ℝ×ℝd\theta,\theta^{\prime}\in\mathbb{R}\times\mathbb{R}\times\mathbb{R}^{d}, then XnX^{n} is Lipschitz continuous in ℋ01\mathcal{H}\_{0}^{1}, *i.e.* there exists a constant Cψ>0C\_{\psi}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖Xn​(θ)−Xn​(θ′)‖ℋ01≤Cψ​(rn)4+d2​|θ−θ′|12.\displaystyle\left\|X^{n}(\theta)-X^{n}(\theta^{\prime})\right\|\_{\mathcal{H}\_{0}^{1}}\leq C\_{\psi}\left(r\_{n}\right)^{4+\frac{d}{2}}\left|\theta-\theta^{\prime}\right|^{\frac{1}{2}}. |  |

###### Proof.

As in the proof of [Lemma A.3](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem3 "Lemma A.3 (ℋ₀¹-boundedness of 𝑋^𝑛). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Xn​(θ)−Xn​(θ′)‖ℋ01\displaystyle\left\|X^{n}(\theta)-X^{n}\left(\theta^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}} | ≤∥ψ(α^⋅+c^)−ψ(α^′⋅+c^′)∥ℋ01\displaystyle\leq\left\|\psi\left(\hat{\alpha}\cdot+\hat{c}\right)-\psi\left(\hat{\alpha}^{\prime}\cdot+\hat{c}^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∥β^(⋅∇ψ)(α^⋅+c^)−β^′⋅(∇ψ)(α^′⋅+c^′)∥ℋ01\displaystyle\qquad+\left\|\hat{\beta}\left(\cdot\nabla\psi\right)\left(\hat{\alpha}\cdot+\hat{c}\right)-\hat{\beta}^{\prime}\cdot\left(\nabla\psi\right)\left(\hat{\alpha}^{\prime}\cdot+\hat{c}^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∥β^(∇ψ)(α^⋅+c^)−β^′(∇ψ)(α^′⋅+c^′)∥ℋ01.\displaystyle\qquad+\left\|\hat{\beta}\left(\nabla\psi\right)\left(\hat{\alpha}\cdot+\hat{c}\right)-\hat{\beta}^{\prime}\left(\nabla\psi\right)\left(\hat{\alpha}^{\prime}\cdot+\hat{c}^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}. |  | (A.1) |

Let us recall that |α^|,|β^|,|c^|≤rn\left|\hat{\alpha}\right|,|\hat{\beta}|,\left|\hat{c}\right|\leq r\_{n} and |α^|≥rn−1\left|\hat{\alpha}\right|\geq r\_{n}^{-1}.
Using that ψ∈Cc∞​(ℝd)\psi\in C\_{c}^{\infty}\left(\mathbb{R}^{d}\right), and therefore Lipschitz, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝd|ψ​(α^​x+c^)−ψ​(α^′​x+c^′)|2​dx\displaystyle\int\_{\mathbb{R}^{d}}\left|\psi\left(\hat{\alpha}x+\hat{c}\right)-\psi\left(\hat{\alpha}^{\prime}x+\hat{c}^{\prime}\right)\right|^{2}\mathrm{d}x | ≤∫ℝdCψ​|(α^−α^′)​x+c^−c^′|​|ψ​(α^​x+c^)−ψ​(α^′​x+c^′)|​dx\displaystyle\leq\int\_{\mathbb{R}^{d}}C\_{\psi}\left|\left(\hat{\alpha}-\hat{\alpha}^{\prime}\right)x+\hat{c}-\hat{c}^{\prime}\right|\left|\psi\left(\hat{\alpha}x+\hat{c}\right)-\psi\left(\hat{\alpha}^{\prime}x+\hat{c}^{\prime}\right)\right|\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​|θ−θ′|​∫ℝd(1+|x|)​(|ψ​(α^​x+c^)|+|ψ​(α^′​x+c^′)|)​dx.\displaystyle\leq C\_{\psi}\left|\theta-\theta^{\prime}\right|\int\_{\mathbb{R}^{d}}\left(1+\left|x\right|\right)\left(\left|\psi\left(\hat{\alpha}x+\hat{c}\right)\right|+\left|\psi\left(\hat{\alpha}^{\prime}x+\hat{c}^{\prime}\right)\right|\right)\mathrm{d}x. |  |

Using the change of variables y=α^​x+c^y=\hat{\alpha}x+\hat{c}, we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝd(1+|x|)​|ψ​(α^​x+c^)|​dx\displaystyle\int\_{\mathbb{R}^{d}}\left(1+\left|x\right|\right)\left|\psi\left(\hat{\alpha}x+\hat{c}\right)\right|\mathrm{d}x | =|α^|−d​∫ℝd|ψ​(y)|​dy+|α^|−d−1​∫ℝd|y−c^|​|ψ​(y)|​𝑑y\displaystyle=\left|\hat{\alpha}\right|^{-d}\int\_{\mathbb{R}^{d}}\left|\psi(y)\right|\mathrm{d}y+\left|\hat{\alpha}\right|^{-d-1}\int\_{\mathbb{R}^{d}}\left|y-\hat{c}\right|\left|\psi\left(y\right)\right|dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cψ​(rnd+rnd+2),\displaystyle\leq C\_{\psi}\Big(r\_{n}^{d}+r\_{n}^{d+2}\Big), |  |

and we obtain the bound

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|ψ​(α^​x+c^)−ψ​(α^′​x+c^′)|2​dx≤Cψ​|θ−θ′|​rnd+2.\int\_{\mathbb{R}^{d}}\left|\psi\left(\hat{\alpha}x+\hat{c}\right)-\psi\left(\hat{\alpha}^{\prime}x+\hat{c}^{\prime}\right)\right|^{2}\mathrm{d}x\leq C\_{\psi}\left|\theta-\theta^{\prime}\right|r\_{n}^{d+2}. |  |

Analogously, using that ∇ψ\nabla\psi is Lipschitz as well, we have that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|α^​∇ψ​(α^​x+c^)−α^′​∇ψ​(α^′​x+c^′)|2​dx≤2​∫ℝd|α^−α^′|2​|∇ψ​(α^​x+c^)|2​dx+2​∫ℝd|α^′|2​|∇ψ​(α^​x+c^)−∇ψ​(α^′​x+c^′)|2​dx≤4​rn​|θ−θ′|​∫ℝd|∇ψ​(α^​x+c^)|2​dx+2​rn2​∫ℝd|∇ψ​(α^​x+c^)−∇ψ​(α^′​x+c^′)|2​dx≤Cψ​|θ−θ′|​(rn)d+4.\int\_{\mathbb{R}^{d}}\left|\hat{\alpha}\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)-\hat{\alpha}^{\prime}\nabla\psi\left(\hat{\alpha}^{\prime}x+\hat{c}^{\prime}\right)\right|^{2}\mathrm{d}x\\ \leq 2\int\_{\mathbb{R}^{d}}\left|\hat{\alpha}-\hat{\alpha}^{\prime}\right|^{2}\left|\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)\right|^{2}\mathrm{d}x+2\int\_{\mathbb{R}^{d}}\left|\hat{\alpha}^{\prime}\right|^{2}\left|\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)-\nabla\psi\left(\hat{\alpha}^{\prime}x+\hat{c}^{\prime}\right)\right|^{2}\mathrm{d}x\\ \leq 4r\_{n}\left|\theta-\theta^{\prime}\right|\int\_{\mathbb{R}^{d}}\left|\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)\right|^{2}\mathrm{d}x+2r\_{n}^{2}\int\_{\mathbb{R}^{d}}\left|\nabla\psi\left(\hat{\alpha}x+\hat{c}\right)-\nabla\psi\left(\hat{\alpha}^{\prime}x+\hat{c}^{\prime}\right)\right|^{2}\mathrm{d}x\\ \leq C\_{\psi}\left|\theta-\theta^{\prime}\right|(r\_{n})^{d+4}. |  |

Therefore, we arrive at the following bound for the ℋ01\mathcal{H}\_{0}^{1}-norm of this term

|  |  |  |
| --- | --- | --- |
|  | ∥ψ(α^⋅+c^)−ψ(α^′⋅+c^′)∥ℋ01≤Cψ|θ−θ′|1/2(rn)d/2+2.\left\|\psi\left(\hat{\alpha}\cdot+\hat{c}\right)-\psi\left(\hat{\alpha}^{\prime}\cdot+\hat{c}^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\leq C\_{\psi}\left|\theta-\theta^{\prime}\right|^{1/2}(r\_{n})^{d/2+2}. |  |

We can similarly estimate the other two terms in ([A.2](https://arxiv.org/html/2512.25017v1#A1.Ex58 "Proof. ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), and we get that

|  |  |  |
| --- | --- | --- |
|  | ∥β^(⋅∇ψ)(α^⋅+c^)−β^′⋅(∇ψ)(α^′⋅+c^′)∥ℋ01\displaystyle\left\|\hat{\beta}\left(\cdot\nabla\psi\right)\left(\hat{\alpha}\cdot+\hat{c}\right)-\hat{\beta}^{\prime}\cdot\left(\nabla\psi\right)\left(\hat{\alpha}^{\prime}\cdot+\hat{c}^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}} |  |
|  |  |  |
| --- | --- | --- |
|  | +∥β^(∇ψ)(α^⋅+c^)−β^′(∇ψ)(α^′⋅+c^′)∥ℋ01≤Cψ|θ−θ′|1/2(rn)d/2+4\displaystyle\qquad+\left\|\hat{\beta}\left(\nabla\psi\right)\left(\hat{\alpha}\cdot+\hat{c}\right)-\hat{\beta}^{\prime}\left(\nabla\psi\right)\left(\hat{\alpha}^{\prime}\cdot+\hat{c}^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\leq C\_{\psi}\left|\theta-\theta^{\prime}\right|^{1/2}(r\_{n})^{d/2+4} |  |

Concluding, we have

|  |  |  |
| --- | --- | --- |
|  | ‖Xn​(θ)−Xn​(θ′)‖ℋ01≤Cψ​(rn)4+d2​|θ−θ′|12.∎\left\|X^{n}(\theta)-X^{n}\left(\theta^{\prime}\right)\right\|\_{\mathcal{H}\_{0}^{1}}\leq C\_{\psi}\left(r\_{n}\right)^{4+\frac{d}{2}}\left|\theta-\theta^{\prime}\right|^{\frac{1}{2}}.\qed |  |

###### Lemma A.7.

Assume that the neural network satisfies [Assumption (NNI)](https://arxiv.org/html/2512.25017v1#Thmassumption5 "Assumption (NNI). ‣ 4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Then, for t≥0t\geq 0, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|θti,n−θ0i,n|]≤Cψ​t​nδ−1​(rn)d2+4.\displaystyle\mathbb{E}\left[\left|\theta\_{t}^{i,n}-\theta\_{0}^{i,n}\right|\right]\leq C\_{\psi}tn^{\delta-1}\left(r\_{n}\right)^{\frac{d}{2}+4}. |  |

###### Remark A.8.

This lemma yields that, when nn is large, then the value θti,n\theta\_{t}^{i,n} of the evolution of the parameters of the neural network does not differ significantly from its initial value θ0i,n\theta\_{0}^{i,n}.

###### Proof.

Recalling ([4.1](https://arxiv.org/html/2512.25017v1#S4.Ex5 "4.1. Convergence of the trained neural network ‣ 4. Convergence of the training error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs")), we have

|  |  |  |
| --- | --- | --- |
|  | θti,n−θ0i,n=−ηn​∫0t⟨𝒟​Ik​(Vsn),∇θiVsn⟩ℋ01​ds,\displaystyle\theta\_{t}^{i,n}-\theta\_{0}^{i,n}=-\eta\_{n}\int\_{0}^{t}\left\langle\mathcal{D}I^{k}\left(V\_{s}^{n}\right),\nabla\_{\theta^{i}}V\_{s}^{n}\right\rangle\_{\mathcal{H}\_{0}^{1}}\mathrm{d}s, |  |

thus, their squared difference equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | |θti,n−θ0i,n|2=\displaystyle\left|\theta\_{t}^{i,n}-\theta\_{0}^{i,n}\right|^{2}= | |ηn|2​|∫0t⟨𝒟​Ik​(Vsn),∇θiVsn⟩ℋ01​ds|2≤n4​δ−2​t​∫0t⟨𝒟​Ik​(Vsn),∇θiVsn⟩ℋ012​ds.\displaystyle\left|\eta\_{n}\right|^{2}\left|\int\_{0}^{t}\left\langle\mathcal{D}I^{k}\left(V\_{s}^{n}\right),\nabla\_{\theta^{i}}V\_{s}^{n}\right\rangle\_{\mathcal{H}\_{0}^{1}}\mathrm{d}s\right|^{2}\leq n^{4\delta-2}t\int\_{0}^{t}\left\langle\mathcal{D}I^{k}\left(V\_{s}^{n}\right),\nabla\_{\theta^{i}}V\_{s}^{n}\right\rangle^{2}\_{\mathcal{H}\_{0}^{1}}\mathrm{d}s. |  |

Using LABEL:{lem:con\_frechet}, we get

|  |  |  |
| --- | --- | --- |
|  | |⟨𝒟​Ik​(Vsn),∇θiVsn⟩ℋ01|2≤K​(1+‖Vsn‖ℋ012)​‖∇θiVsn‖ℋ012.\displaystyle\left|\left\langle\mathcal{D}I^{k}\left(V\_{s}^{n}\right),\nabla\_{\theta^{i}}V\_{s}^{n}\right\rangle\_{\mathcal{H}\_{0}^{1}}\right|^{2}\leq K\left(1+\left\|V^{n}\_{s}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right)\left\|\nabla\_{\theta^{i}}V\_{s}^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}. |  |

Using that

|  |  |  |
| --- | --- | --- |
|  | |∇θiVn​(θtn;x)|=1nδ​|𝒳n​(θti,n;x)|,\left|\nabla\_{\theta^{i}}V^{n}\left(\theta^{n}\_{t};x\right)\right|=\frac{1}{n^{\delta}}\left|\mathcal{X}^{n}\left(\theta^{i,n}\_{t};x\right)\right|, |  |

and applying [Lemma A.3](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem3 "Lemma A.3 (ℋ₀¹-boundedness of 𝑋^𝑛). ‣ A.2. Gradient 𝜃 estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we get

|  |  |  |
| --- | --- | --- |
|  | ‖∇θiVtn‖ℋ012≤Cψn2​δ​(rn)d+8.\left\|\nabla\_{\theta^{i}}V\_{t}^{n}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\leq\frac{C\_{\psi}}{n^{2\delta}}\left(r\_{n}\right)^{d+8}. |  |

Moreover, from [Lemma A.2](https://arxiv.org/html/2512.25017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.1. Functional inequalities and norm estimates ‣ Appendix A Auxiliary results ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖Vtn‖ℋ012]≤Cψ.\mathbb{E}\left[\left\|V^{n}\_{t}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}\right]\leq C\_{\psi}. |  |

Hence, we can bound the norm of the square difference by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|θti,n−θ0i,n|2]≤Cψ​t​n2​(δ−1)​(rn)d+8​∫0t𝔼​[‖Vsn‖ℋ012+1]​ds≤Cψ​t2​n2​(δ−1)​(rn)d+8.\mathbb{E}\left[\left|\theta\_{t}^{i,n}-\theta\_{0}^{i,n}\right|^{2}\right]\leq C\_{\psi}tn^{2\left(\delta-1\right)}\left(r\_{n}\right)^{d+8}\int\_{0}^{t}\mathbb{E}\left[\left\|V^{n}\_{s}\right\|^{2}\_{\mathcal{H}\_{0}^{1}}+1\right]\mathrm{d}s\leq C\_{\psi}t^{2}n^{2\left(\delta-1\right)}\left(r\_{n}\right)^{d+8}. |  |

The result follows now using Jensen’s inequality.
∎

### A.3. Examples

This final appendix contains certain details in order to verify that the option pricing PDEs of [Examples 2.3](https://arxiv.org/html/2512.25017v1#S2.Thmtheorem3 "Example 2.3 (Option pricing PDEs). ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [2.4](https://arxiv.org/html/2512.25017v1#S2.Thmtheorem4 "Example 2.4 (Option pricing PIDEs). ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") indeed satisfy [Assumptions (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), [(GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), [(LIP)](https://arxiv.org/html/2512.25017v1#Thmassumption4 "Assumption (LIP). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") and [(SA)](https://arxiv.org/html/2512.25017v1#Thmassumption3 "Assumption (SA). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").

Starting from the Black–Scholes PDE of [Example 2.3](https://arxiv.org/html/2512.25017v1#S2.Thmtheorem3 "Example 2.3 (Option pricing PDEs). ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we have that

|  |  |  |
| --- | --- | --- |
|  | ℒ​u=−σ22​∂2u∂x2+r​u and F​(u)=(σ22−r)​∂u∂x,\displaystyle\mathcal{L}u=-\frac{\sigma^{2}}{2}\frac{\partial^{2}u}{\partial x^{2}}+ru\quad\text{ and }\quad F(u)=\left(\frac{\sigma^{2}}{2}-r\right)\frac{\partial u}{\partial x}, |  |

and the energy functional takes the form

|  |  |  |
| --- | --- | --- |
|  | Ik​(u)=12​‖u−Uk−1‖L22+h2​∫ℝ{σ22​(∂u∂x)2+r​u2}​dx+h​∫ℝF​(Uk−1)​u​dx.I^{k}(u)=\frac{1}{2}\left\|u-U^{k-1}\right\|^{2}\_{L^{2}}+\frac{h}{2}\int\_{\mathbb{R}}\Big\{\frac{\sigma^{2}}{2}\left(\frac{\partial u}{\partial x}\right)^{2}+ru^{2}\Big\}\mathrm{d}x+h\int\_{\mathbb{R}}F\left(U^{k-1}\right)u\mathrm{d}x. |  |

[Assumption (SA)](https://arxiv.org/html/2512.25017v1#Thmassumption3 "Assumption (SA). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") is obviously satisfied.
Using the triangle and the Cauchy–Schwarz inequalities, following some straightforward calculations, we arrive at

|  |  |  |
| --- | --- | --- |
|  | |⟨ℒ​u,v⟩ℋ−1,ℋ01|≤(|σ22|+|r|)​‖u‖ℋ01​‖v‖ℋ01 and ‖F​(u)‖L2≤|σ22−r|​‖u‖ℋ01.\displaystyle\left|\left\langle\mathcal{L}u,v\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\right|\leq\left(\left|\frac{\sigma^{2}}{2}\right|+\left|r\right|\right)\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}\left\|v\right\|\_{\mathcal{H}\_{0}^{1}}\quad\text{ and }\quad\left\|F(u)\right\|\_{L^{2}}\leq\left|\frac{\sigma^{2}}{2}-r\right|\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}. |  |

Hence, [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") is satisfied with M=|σ22|+|r|M=\left|\frac{\sigma^{2}}{2}\right|+\left|r\right|.
Moreover, we have that

|  |  |  |
| --- | --- | --- |
|  | ⟨ℒ​u,u⟩ℋ−1,ℋ01≥(σ22+r)​‖u‖ℋ012,\left\langle\mathcal{L}u,u\right\rangle\_{\mathcal{H}^{-1},\mathcal{H}\_{0}^{1}}\geq\left(\frac{\sigma^{2}}{2}+r\right)\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}, |  |

therefore [Assumption (GÅ)](https://arxiv.org/html/2512.25017v1#Thmassumption2 "Assumption (GÅ). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") is satisfied with λ1=σ22+r>0\lambda\_{1}=\frac{\sigma^{2}}{2}+r>0 and λ2=0\lambda\_{2}=0.
[Assumption (LIP)](https://arxiv.org/html/2512.25017v1#Thmassumption4 "Assumption (LIP). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs") follows by similar computations.

Turning our attention to the multi-dimensional Merton model of [Example 2.4](https://arxiv.org/html/2512.25017v1#S2.Thmtheorem4 "Example 2.4 (Option pricing PIDEs). ‣ 2. Deep gradient flow methods for PDEs ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs"), we only need to show that the function FF, which now contains the integro-differential operator stemming from the jumps of the dynamics, still satisfies [Assumption (CON)](https://arxiv.org/html/2512.25017v1#Thmassumption1 "Assumption (CON). ‣ 3. Convergence of the approximation error ‣ Convergence of the generalization error for Deep Gradient Flow Methods for PDEs").
Let us start with the integral operator, denoted by FνF\_{\nu}, then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Fν​(u)‖L22\displaystyle\left\|F\_{\nu}(u)\right\|\_{L^{2}}^{2} | ≤∫ℝd|λ​∫ℝd(u​(x​ez)−u​(x))​ν​(d​z)|2​dx\displaystyle\leq\int\_{\mathbb{R}^{d}}\left|\lambda\int\_{\mathbb{R}^{d}}\left(u\left(x\mathrm{e}^{z}\right)-u\left(x\right)\right)\nu\left(\mathrm{d}z\right)\right|^{2}\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​λ​∫ℝd∫ℝd|u​(x​ez)|2​ν​(d​z)​dx+2​λ​∫ℝd|u​(x)|2​dx\displaystyle\leq 2\lambda\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\left|u\left(x\mathrm{e}^{z}\right)\right|^{2}\nu\left(\mathrm{d}z\right)\mathrm{d}x+2\lambda\int\_{\mathbb{R}^{d}}\left|u\left(x\right)\right|^{2}\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​λ(2​π)d​∫ℝd∫ℝd|u​(x​ez)|2​e−z22​dz​dx+2​λ​‖u‖L22\displaystyle=\frac{2\lambda}{(\sqrt{2\pi})^{d}}\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\left|u\left(x\mathrm{e}^{z}\right)\right|^{2}\mathrm{e}^{-\frac{z^{2}}{2}}\mathrm{d}z\mathrm{d}x+2\lambda\left\|u\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​λ(2​π)d​∫ℝd∫ℝd|u​(x​ez)|2​e−z22​dx​dz+2​λ​‖u‖L22\displaystyle=\frac{2\lambda}{(\sqrt{2\pi})^{d}}\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\left|u\left(x\mathrm{e}^{z}\right)\right|^{2}\mathrm{e}^{-\frac{z^{2}}{2}}\mathrm{d}x\mathrm{d}z+2\lambda\left\|u\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​λ(2​π)d​∫ℝd∫ℝd|u​(y)|2​e−2​z−z22​dy​dz+2​λ​‖u‖L22\displaystyle=\frac{2\lambda}{(\sqrt{2\pi})^{d}}\int\_{\mathbb{R}^{d}}\int\_{\mathbb{R}^{d}}\left|u\left(y\right)\right|^{2}\mathrm{e}^{\frac{-2z-z^{2}}{2}}\mathrm{d}y\mathrm{d}z+2\lambda\left\|u\right\|\_{L^{2}}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​λ​(e+1)​‖u‖L22≤2​λ​(e+1)​‖u‖ℋ012,\displaystyle=2\lambda\left(\mathrm{e}+1\right)\left\|u\right\|\_{L^{2}}^{2}\leq 2\lambda\left(\mathrm{e}+1\right)\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}^{2}, |  |

where we have used the properties of the normal distribution, Fubini’s theorem for the fourth step, and the change of variables y=x​ezy=x\mathrm{e}^{z} for the fifth step.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | ‖F​(u)‖L2≤|𝒃|​‖∇u‖L2+λ​‖Fν​(u)‖L2≤2​λ​(C+e+1)​‖u‖ℋ01,\displaystyle\left\|F(u)\right\|\_{L^{2}}\leq\left|\boldsymbol{b}\right|\left\|\nabla u\right\|\_{L^{2}}+\lambda\left\|F\_{\nu}(u)\right\|\_{L^{2}}\leq 2\lambda\left(C+\mathrm{e}+1\right)\left\|u\right\|\_{\mathcal{H}\_{0}^{1}}, |  |

which implies the result.

## References

* Akrivis et al. [1999]

  G. Akrivis, M. Crouzeix, and C. Makridakis.
  Implicit-explicit multistep methods for quasilinear parabolic
  equations.
  *Numerische Mathematik*, 82:521–541, 1999.
* Black and Scholes [1973]

  F. Black and M. Scholes.
  The pricing of options and corporate liabilities.
  *Journal of Political Economy*, 81(3):637–654, 1973.
* Bruna et al. [2024]

  J. Bruna, B. Peherstorfer, and E. Vanden-Eijnden.
  Neural carmoalerkin schemes with active learning for
  high-dimensional evolution equations.
  *Journal of Computational Physics*, 496:112588, 2024.
* Carmona and Zeng [2024]

  R. A. Carmona and C. Zeng.
  Leveraging the turnpike effect for mean field games numerics.
  *IEEE Open Journal of Control Systems*, 3:389–404,
  2024.
* Dondl et al. [2022]

  P. Dondl, J. Müller, and M. Zeinhofer.
  Uniform convergence guarantees for the deep Ritz method for
  nonlinear problems.
  *Advances in Continuous and Discrete Models*, 2022(1):49, 2022.
* E and Yu [2018]

  W. E and B. Yu.
  The deep Ritz method: A deep learning-based numerical algorithm
  for solving variational problems.
  *Communications in Mathematics and Statistics*, 6:1–12, 2018.
* Gazoulis et al. [2025]

  D. Gazoulis, I. Gkanis, and C. G. Makridakis.
  On the stability and convergence of physics informed neural networks.
  *IMA Journal of Numerical Analysis*, 2025.
  (advance article).
* Georgoulis et al. [2023]

  E. Georgoulis, M. Loulakis, and A. Tsiourvas.
  Discrete gradient flow approximations of high dimensional evolution
  partial differential equations via deep neural networks.
  *Communications in Nonlinear Science and Numerical Simulation*,
  117:106893, 2023.
* Georgoulis et al. [2024]

  E. Georgoulis, A. Papapantoleon, and C. Smaragdakis.
  A deep implicit-explicit minimizing movement method for option
  pricing in jump-diffusion models.
  Preprint, arXiv:2401.06740, 2024.
* Goodfellow et al. [2016]

  I. Goodfellow, Y. Bengio, and A. Courville.
  *Deep Learning*.
  MIT Press, 2016.
* Heston [1993]

  S. L. Heston.
  A closed-form solution for options with stochastic volatility with
  applications to bond and currency options.
  *The Review of Financial Studies*, 6(2):327–343, 1993.
* Hilber et al. [2013]

  N. Hilber, O. Reichmann, C. Schwab, and C. Winter.
  *Computational Methods for Quantitative Finance: Finite Element
  Methods for Derivative Pricing*.
  Springer Science & Business Media, 2013.
* Hornik [1991]

  K. Hornik.
  Approximation capabilities of multilayer feedforward networks.
  *Neural Networks*, 4(2):251–257, 1991.
* Jentzen et al. [2025]

  A. Jentzen, B. Kuckuck, and P. von Wurstemberger.
  Mathematical Introduction to Deep Learning: Methods,
  Implementations, and Theory, 2025.
  Available at arXiv:2310.20360.
* Jiang et al. [2023]

  D. Jiang, J. Sirignano, and S. Cohen.
  Global convergence of deep Galerkin and PINNs methods for solving
  partial differential equations.
  Preprint, arXiv:2305.06000, 2023.
* Jiao et al. [2024]

  Y. Jiao, Y. Lai, Y. Lo, Y. Wang, and Y. Yang.
  Error analysis of deep Ritz methods for elliptic equations.
  *Analysis and Applications*, 22(1):57–87,
  2024.
* Kharazmi et al. [2021]

  E. Kharazmi, Z. Zhang, and G. E. Karniadakis.
  Variational physics-informed neural networks for solving partial
  differential equations.
  *Journal of Computational Physics*, 418:109629, 2021.
* Lagaris et al. [1998]

  I. E. Lagaris, A. Likas, and D. I. Fotiadis.
  Artificial neural networks for solving ordinary and partial
  differential equations.
  *IEEE Transactions on Neural Networks*, 9(5):987–1000, 1998.
* Lagaris et al. [2000]

  I. E. Lagaris, A. C. Likas, and D. G. Papageorgiou.
  Neural-network methods for boundary value problems with irregular
  boundaries.
  *IEEE Transactions on Neural Networks*, 11(5):1041–1049, 2000.
* Liao and Ming [2021]

  Y. Liao and P. Ming.
  Deep Nitsche method: deep Ritz method with essential boundary
  conditions.
  *Communications in Computational Physics*, 29(5):1365–1384, 2021.
* Loulakis and
  Makridakis [2023]

  M. Loulakis and C. G. Makridakis.
  A new approach to generalisation error of machine learning
  algorithms: Estimates and convergence, 2023.
  Preprint, arXiv:2306.13784.
* Mishra and Molinaro [2022]

  S. Mishra and R. Molinaro.
  Estimates on the generalization error of physics-informed neural
  networks for approximating PDEs.
  *IMA Journal of Numerical Analysis*, 42(2):981–1022, 2022.
* Pang et al. [2019]

  G. Pang, L. Lu, and G. E. Karniadakis.
  fPINNs: Fractional physics-informed neural networks.
  *SIAM Journal on Scientific Computing*, 41(4):A2603–A2626, 2019.
* Papapantoleon and Rou [2025]

  A. Papapantoleon and J. Rou.
  A time-stepping deep gradient flow method for option pricing in
  (rough) diffusion models.
  *Quantitative Finance*, 25:2009–2020, 2025.
* Park et al. [2023]

  M. S. Park, C. Kim, H. Son, and H. J. Hwang.
  The deep minimizing movement scheme.
  *Journal of Computational Physics*, 494:112518, 2023.
* Raissi and Karniadakis [2018]

  M. Raissi and G. E. Karniadakis.
  Hidden physics models: Machine learning of nonlinear partial
  differential equations.
  *Journal of Computational Physics*, 357:125–141,
  2018.
* Raissi et al. [2019]

  M. Raissi, P. Perdikaris, and G. E. Karniadakis.
  Physics-informed neural networks: a deep learning framework for
  solving forward and inverse problems involving nonlinear partial differential
  equations.
  *Journal of Computational Physics*, 378:686–707,
  2019.
* Shin et al. [2020]

  Y. Shin, J. Darbon, and G. E. Karniadakis.
  On the convergence of physics informed neural networks for linear
  second-order elliptic and parabolic type pdes.
  *Communications in Computational Physics*, 28(5):2042–2074, 2020.
* Sirignano and Spiliopoulos [2018]

  J. Sirignano and K. Spiliopoulos.
  DGM: A deep learning algorithm for solving partial differential
  equations.
  *Journal of Computational Physics*, 375:1339–1364,
  2018.
* van Neerven [2022]

  J. van Neerven.
  *Functional Analysis*.
  Cambridge University Press, 2022.
* Yang et al. [2021]

  L. Yang, X. Meng, and G. E. Karniadakis.
  B-pinns: Bayesian physics-informed neural networks for forward and
  inverse pde problems under uncertainty.
  *Journal of Computational Physics*, 425:109913, 2021.
* Zhang et al. [2020]

  J. Zhang, T. He, S. Sra, and A. Jadbabaie.
  Why gradient clipping accelerates training: A theoretical
  justification for adaptivity.
  In *International Conference on Learning Representations*, 2020.