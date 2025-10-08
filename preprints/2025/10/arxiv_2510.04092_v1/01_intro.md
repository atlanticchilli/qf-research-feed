---
authors:
- Emmanuel Coffie
doc_id: arxiv:2510.04092v1
family_id: arxiv:2510.04092
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Convergence in probability of numerical solutions of a highly non-linear delayed
  stochastic interest rate model
url_abs: http://arxiv.org/abs/2510.04092v1
url_html: https://arxiv.org/html/2510.04092v1
venue: arXiv q-fin
version: 1
year: 2025
---


Emmanuel Coffie 111Corresponding author, Email: emmanuel.coffie@liverpool.ac.uk
  
Institute for Financial and Actuarial Mathematics,
  
University of Liverpool, Liverpool L69 7ZL, UK

###### Abstract

We examine a delayed stochastic interest rate model with super-linearly growing coefficients and develop several new mathematical tools to establish the properties of its true and truncated EM solutions. Moreover, we show that the true solution converges to the truncated EM solutions in probability as the step size tends to zero. Further, we support the convergence result with some illustrative numerical examples and justify the convergence result for the Monte Carlo evaluation of some financial quantities.

Keywords: Stochastic interest rate model, delay, truncated EM method, Monte Carlo method, bond, option contract.

Mathematics Subject Classification: 65C05, 65C30, 91G30, 91G60

## 1 Introduction

Stochastic modelling of interest rates is important for calibrating and valuing financial products such as option contracts. There are various stochastic interest rate models proposed by some authors in the existing literature to describe the evolution of interest rates. One of the well-known stochastic interest rate models, also known as the CIR model, was proposed by Cox, Ingersoll, and Ross in [[5](https://arxiv.org/html/2510.04092v1#bib.bib5)]. This model is described by the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=α​(μ−x​(t))​d​t+σ​x​(t)​d​B​(t).\displaystyle dx(t)=\alpha(\mu-x(t))dt+\sigma\sqrt{x(t)}dB(t). |  | (1) |

Here, x=(x​(t),t≥0)x=(x(t),t\geq 0) denotes the interest rate with initial value x​(0)=x0x(0)=x\_{0}, α,μ,σ>0\alpha,\mu,\sigma>0, and B=(B​(t),t≥0)B=(B(t),t\geq 0) is a scalar Brownian motion. The CIR model is mean-reverting, and due to its square root diffusion factor, it can also avoid possible negative rates.

We observe in SDE ([1](https://arxiv.org/html/2510.04092v1#S1.E1 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) that the volatility term σ\sigma is assumed constant. However, as supported by empirical studies, volatility is not constant but exhibits empirical features widely known as volatility skews and smiles that are prevalent in option markets (see, e.g., [[7](https://arxiv.org/html/2510.04092v1#bib.bib7), [6](https://arxiv.org/html/2510.04092v1#bib.bib6)]). In order to capture the evolution of volatility skews and smiles, some authors proposed to model volatility as a function of a delay variable. For instance, Arriojas et al. in [[1](https://arxiv.org/html/2510.04092v1#bib.bib1)] proposed the delayed Black-Scholes model where both drift and diffusion terms are functions of a delay variable. This model is described by the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=μ​x​(t−a)​x​(t)​d​t+g​(x​(t−b))​x​(t)​d​B​(t)dx(t)=\mu x(t-a)x(t)dt+g(x(t-b))x(t)dB(t) |  | (2) |

on t∈[0,T]t\in[0,T] with the initial value ξ​(t)∈[−τ,0]\xi(t)\in[-\tau,0], where ξ:Ω→C([−τ,0]:ℝ)\xi:\Omega\rightarrow C([-\tau,0]:\mathbb{R}), μ,a,b>0\mu,a,b>0, τ=max⁡(a,b)\tau=\max(a,b), x​(t−a)x(t-a) and x​(t−b)x(t-b) denote delays in x​(t)x(t), g:ℝ→ℝg:\mathbb{R}\rightarrow\mathbb{R} is a continuous function, and B=(B​(t),t≥0)B=(B(t),t\geq 0) is a scalar Brownian motion. The authors showed that the delayed Black-Scholes model maintains the no-arbitrage property and the completeness of the market with the correct volatility skews and smiles. Furthermore, Mao and Sabanis in [[13](https://arxiv.org/html/2510.04092v1#bib.bib13)] introduced the delay geometric Brownian motion described by the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=r​x​(t)​d​t+v​(x​(t−τ))​x​(t)​B​(t)dx(t)=rx(t)dt+v(x(t-\tau))x(t)B(t) |  | (3) |

on t≥0t\geq 0 with the initial value ξ​(t)\xi(t) on t∈[−τ,0]t\in[-\tau,0], where τ,r>0\tau,r>0, ξ:Ω→C([−τ,0]:ℝ)\xi:\Omega\rightarrow C([-\tau,0]:\mathbb{R}), B=(B​(t),t≥0)B=(B(t),t\geq 0) is a scalar Brownian motion, the volatility function vv depends on x​(t−τ)x(t-\tau), and x​(t−τ)x(t-\tau) denotes delay in x​(t)x(t). The authors studied the quantitative properties of this model where vv is locally Lipschitz continuous and bounded. The authors provided numerical evidence to justify that the system of type ([3](https://arxiv.org/html/2510.04092v1#S1.E3 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) is a rich alternative model for an asset price process in a complete market characterised by volatility skews and smiles. The reader may also consult (e.g., [[16](https://arxiv.org/html/2510.04092v1#bib.bib16), [9](https://arxiv.org/html/2510.04092v1#bib.bib9)]) for financial models with features of past dependency.

In recent years, more empirical studies have shown that the most successful continuous-time models for interest rates are those models that allow the volatility of interest changes to be highly sensitive to the level of the rates (see, e.g., [[3](https://arxiv.org/html/2510.04092v1#bib.bib3), [14](https://arxiv.org/html/2510.04092v1#bib.bib14)]). This motivated Wu et al. in [[15](https://arxiv.org/html/2510.04092v1#bib.bib15)] to extend SDE ([1](https://arxiv.org/html/2510.04092v1#S1.E1 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) to include a super-linear diffusion term described by the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=α​(μ−x​(t))​d​t+σ​x​(t)θ​d​B​(t)\displaystyle dx(t)=\alpha(\mu-x(t))dt+\sigma x(t)^{\theta}dB(t) |  | (4) |

on t≥0t\geq 0, where θ>1\theta>1. One notable unique feature of SDE ([4](https://arxiv.org/html/2510.04092v1#S1.E4 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) is that the solution x​(t)x(t) is a highly sensitive mean-reverting process. The authors established the convergence in probability of the EM solutions to the true solution. They justified the convergence result within Monte Carlo simulations to value the expected payoff of a bond and a barrier option. To further capture volatility skews and smiles and high non-linearities in the rate, the authors in [[4](https://arxiv.org/html/2510.04092v1#bib.bib4)] extended the generalised Ait-Sahalia interest rate model to include a volatility as a function of a delay variable described by the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=(α−1​x​(t)−1−α0+α1​x​(t)−α2​x​(t)γ)​d​t+v​(x​(t−τ))​x​(t)θ​d​B​(t)dx(t)=(\alpha\_{-1}x(t)^{-1}-\alpha\_{0}+\alpha\_{1}x(t)-\alpha\_{2}x(t)^{\gamma})dt+v(x(t-\tau))x(t)^{\theta}dB(t) |  | (5) |

on t≥0t\geq 0 with the initial value ξ​(t)\xi(t) on t∈[−τ,0]t\in[-\tau,0], where α−1,α0,α1,α2,τ>0\alpha\_{-1},\alpha\_{0},\alpha\_{1},\alpha\_{2},\tau>0, ξ:Ω→C([−τ,0]:ℝ)\xi:\Omega\rightarrow C([-\tau,0]:\mathbb{R}), γ,θ>1\gamma,\theta>1 and B=(B​(t),t≥0)B=(B(t),t\geq 0) is a scalar Brownian motion, vv is a function of x​(t−τ)x(t-\tau) and x​(t−τ)x(t-\tau) denotes delay in x​(t)x(t). Under a monotone condition and the assumption that vv is locally Lipschitz continuous and bounded, the authors proved the strong convergence of the truncated EM solutions to the true solution of SDDE ([5](https://arxiv.org/html/2510.04092v1#S1.E5 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and justified that the convergence result can be applied to value a bond and a barrier option.

Therefore, in order to account for high non-linearities in the rates as well as the evolution of volatility skews and smiles, we consider it necessary to reformulate SDE ([4](https://arxiv.org/html/2510.04092v1#S1.E4 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) as SDDE with super-linearly growing drift and diffusion coefficients described by the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=α​(μ−x​(t)γ)​d​t+σ​x​(t−τ)r​x​(t)θ​d​B​(t),dx(t)=\alpha(\mu-x(t)^{\gamma})dt+\sigma x(t-\tau)^{r}x(t)^{\theta}dB(t), |  | (6) |

on t≥0t\geq 0 with the initial value ξ​(t)\xi(t) on t∈[−τ,0]t\in[-\tau,0], where τ>0\tau>0, ξ:Ω→C([−τ,0]:ℝ)\xi:\Omega\rightarrow C([-\tau,0]:\mathbb{R}), θ,r>0\theta,r>0, and γ>1\gamma>1. We observe that both the drift factor xγx^{\gamma} and the diffusion factor xθ​yrx^{\theta}y^{r} of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) are growing super-linearly and thus violate the global Lipschitz and linear growth conditions. This is further complicated by the presence of the unbounded delay variable yy. Therefore, it can be very challenging to obtain the solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) by an analytical closed-form formula. To the best of our knowledge, there exists no relevant literature for the numerical analysis of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) either in the strong sense or weak sense. In this case, we recognise the need to examine the feasibility of the system of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) from a viewpoint of financial applications. Therefore, we need an efficient numerical method with fast computational performance to estimate the solution. However, in most real-world applications, the explicit EM method is preferred to the implicit type due to its simple algebraic structure, cheap computational cost, and acceptable convergence rate. It is well-known in [[8](https://arxiv.org/html/2510.04092v1#bib.bib8)] that the explicit EM scheme diverges in the strong mean-square sense at a finite point for SDEs with super-linearly growing coefficient terms. In this work, we aim to construct a variant of the truncated EM method developed in [[11](https://arxiv.org/html/2510.04092v1#bib.bib11)] to estimate the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and show that the truncated EM solutions converge to the true solution in probability when the step size is sufficiently small. The remainder of the paper is organised as follows: We explore mathematical notations in Section [2](https://arxiv.org/html/2510.04092v1#S2 "2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"). In Section [3](https://arxiv.org/html/2510.04092v1#S3 "3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we study properties of the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")). We construct the truncated EM techniques to approximate SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and study properties of the truncated EM solutions in Section [4](https://arxiv.org/html/2510.04092v1#S4 "4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"). In Section [5](https://arxiv.org/html/2510.04092v1#S5 "5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we show that the truncated EM solutions converge to the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) in probability. We also provide illustrative numerical examples to support the convergence result and justify the result via the efficient use of the Monte Carlo method to value a bond and a lookback put option in this section.

## 2 Mathematical preliminaries

Throughout this paper, unless specified otherwise, we employ the following notation. Let {Ω,ℱ,ℙ}\{\Omega,\mathcal{F},\mathbb{P}\} be a complete probability space with filtration {ℱt}t≥0\{\mathcal{F}\_{t}\}\_{t\geq 0} satisfying the usual conditions (i.e., it is increasing and right continuous while ℱ0\mathcal{F}\_{0} contains all ℙ\mathbb{P} null sets), and let 𝔼\mathbb{E} denote the expectation corresponding to ℙ\mathbb{P}. Let B=(B​(t),t≥0)B=(B(t),t\geq 0), be a scalar Brownian motion defined on the above probability space. If a,ba,b are real numbers, then a∨ba\vee b denotes the maximum of aa and bb, and a∧ba\wedge b denotes the minimum of aa and bb. Let ℝ=(−∞,∞)\mathbb{R}=(-\infty,\infty) and ℝ+=(0,∞)\mathbb{R}\_{+}=(0,\infty). If x∈ℝx\in\mathbb{R}, then |x||x| is the Euclidean norm. For τ>0\tau>0, let C​([−τ,0];ℝ+)C([-\tau,0];\mathbb{R}\_{+}) denote the space of all continuous functions ξ:[−τ,0]→ℝ+\xi:[-\tau,0]\rightarrow\mathbb{R}\_{+} with the norm ‖ξ‖=sup−τ≤t≤0ξ​(t)\|\xi\|=\sup\_{-\tau\leq t\leq 0}\xi(t). For an empty set ∅\emptyset, we set inf ​∅=∞\text{inf }\emptyset=\infty. For a set AA, we denote its indication function by 1A1\_{A}. Let the following scalar dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=f​(x​(t))​d​t+g​(x​(t),x​(t−τ))​d​B​(t)dx(t)=f(x(t))dt+g(x(t),x(t-\tau))dB(t) |  | (7) |

with initial value x(t)=ξ(t)∈C([−τ,0]:ℝ+)x(t)=\xi(t)\in C([-\tau,0]:\mathbb{R}\_{+}) denote equation of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) such that f​(x)=α​(μ−xγ)f(x)=\alpha(\mu-x^{\gamma}) and g​(x,y)=σ​xθ​yrg(x,y)=\sigma x^{\theta}y^{r}, for all x,y∈ℝ+x,y\in\mathbb{R}\_{+}. Let C2,1​(ℝ×ℝ+;ℝ)C^{2,1}(\mathbb{R}\times\mathbb{R}\_{+};\mathbb{R}) be the family of all real-valued functions V​(x,t)V(x,t) defined on ℝ×ℝ+\mathbb{R}\times\mathbb{R}\_{+} such that V​(x,t)V(x,t) is twice continuously differentiable in xx and once in tt. For each V∈C2,1​(ℝ×ℝ+;ℝ)V\in C^{2,1}(\mathbb{R}\times\mathbb{R}\_{+};\mathbb{R}), define the operator L​V:ℝ×ℝ×ℝ+→ℝLV:\mathbb{R}\times\mathbb{R}\times\mathbb{R}\_{+}\rightarrow\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​V​(x,y,t)=Vt​(x,t)+Vx​(x,t)​f​(x)+12​Vx​x​(x,t)​g​(x,y)2LV(x,y,t)=V\_{t}(x,t)+V\_{x}(x,t)f(x)+\frac{1}{2}V\_{xx}(x,t)g(x,y)^{2} |  | (8) |

for SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) associated with the function VV, where Vt​(x,t)V\_{t}(x,t) and Vx​(x,t)V\_{x}(x,t) are first-order partial derivatives with respect to tt and xx respectively, and Vx​x​(x,t)V\_{xx}(x,t), a second-order partial derivative with respect to xx. With the operator L​VLV defined, then the Itô formula yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​V​(x​(t),t)=L​V​(x​(t),x​(t−τ),t)​d​t+Vx​(x​(t),t)​g​(x​(t),x​(t−τ))​d​B​(t)\displaystyle dV(x(t),t)=LV(x(t),x(t-\tau),t)dt+V\_{x}(x(t),t)g(x(t),x(t-\tau))dB(t) |  | (9) |

almost surely. We should emphasise that L​VLV is defined on ℝ×ℝ×ℝ+\mathbb{R}\times\mathbb{R}\times\mathbb{R}\_{+} while VV is defined on ℝ×ℝ+\mathbb{R}\times\mathbb{R}\_{+}. Moreover, we impose the following standing hypotheses.

###### Assumption 2.1.

The parameters of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1+γ>2​(r+θ),1+\gamma>2(r+\theta), |  | (10) |

where θ,r>0\theta,r>0 and γ>1\gamma>1.

###### Assumption 2.2.

There exist constants D>0D>0 and ℓ∈(0,1]\ell\in(0,1] such that for all −τ≤s≤t≤0-\tau\leq s\leq t\leq 0, the initial value ξ\xi satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ξ​(t)−ξ​(s)|≤D​|t−s|ℓ.|\xi(t)-\xi(s)|\leq D|t-s|^{\ell}. |  | (11) |

We introduce the following important lemma for later use.

###### Lemma 2.3.

Let Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") hold. For any R>0R>0, there exists a positive constant GRG\_{R} such that the coefficients of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) fulfil

|  |  |  |  |
| --- | --- | --- | --- |
|  | |f​(x)−f​(x¯)|+|g​(x,y)−g​(x¯,y¯)|≤GR​(|x−x¯|+|y−y¯|)\displaystyle|f(x)-f(\bar{x})|+|g(x,y)-g(\bar{x},\bar{y})|\leq G\_{R}(|x-\bar{x}|+|y-\bar{y}|) |  | (12) |

for all x,y,x¯,y¯∈ℝx,y,\bar{x},\bar{y}\in\mathbb{R} with |x|∨|x¯|∨|y|∨|y¯|≤R|x|\vee|\bar{x}|\vee|y|\vee|\bar{y}|\leq R.

###### Proof.

If we assume that x<x¯x<\bar{x} and y<y¯y<\bar{y}, then

|  |  |  |
| --- | --- | --- |
|  | (f​(x)−f​(x¯))+(g​(x,y)−g​(x¯,y¯))≤(α​(μ−xγ)−α​(μ−x¯γ))+(σ​xθ​yr−σ​x¯θ​y¯r).\displaystyle(f(x)-f(\bar{x}))+(g(x,y)-g(\bar{x},\bar{y}))\leq(\alpha(\mu-x^{\gamma})-\alpha(\mu-\bar{x}^{\gamma}))+(\sigma x^{\theta}y^{r}-\sigma\bar{x}^{\theta}\bar{y}^{r}). |  |

However, we note from the Young inequality that

|  |  |  |
| --- | --- | --- |
|  | xθ​yr≤x2​θ+y2​r​ and ​x¯θ​y¯r≤x¯2​θ+y¯2​r.x^{\theta}y^{r}\leq x^{2\theta}+y^{2r}\text{ and }\bar{x}^{\theta}\bar{y}^{r}\leq\bar{x}^{2\theta}+\bar{y}^{2r}. |  |

It then follows that

|  |  |  |
| --- | --- | --- |
|  | (f​(x)−f​(x¯))+(g​(x,y)−g​(x¯,y¯))≤−α​(xγ−x¯γ)+σ​(x2​θ−x¯2​θ)+σ​(y2​r−y¯2​r).\displaystyle(f(x)-f(\bar{x}))+(g(x,y)-g(\bar{x},\bar{y}))\leq-\alpha(x^{\gamma}-\bar{x}^{\gamma})+\sigma(x^{2\theta}-\bar{x}^{2\theta})+\sigma(y^{2r}-\bar{y}^{2r}). |  |

So by the mean-value theorem, we now get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |f​(x)−f​(x¯)|+|g​(x,y)−g​(x¯,y¯)|≤\displaystyle|f(x)-f(\bar{x})|+|g(x,y)-g(\bar{x},\bar{y})|\leq | −α​γ​(|xγ−1|+|x¯γ−1|)​|x−x¯|\displaystyle-\alpha\gamma(|x^{\gamma-1}|+|\bar{x}^{\gamma-1}|)|x-\bar{x}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​θ​σ​(|x2​θ−1|+|x¯2​θ−1|)​|x−x¯|\displaystyle+2\theta\sigma(|x^{2\theta-1}|+|\bar{x}^{2\theta-1}|)|x-\bar{x}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​r​σ​(|y2​r−1|+|y¯2​r−1|)​|y−y¯|.\displaystyle+2r\sigma(|y^{2r-1}|+|\bar{y}^{2r-1}|)|y-\bar{y}|. |  |

Noting that

|  |  |  |
| --- | --- | --- |
|  | γ−1>2​r+2​θ−2⇒γ+1>2​(r+θ),\displaystyle\gamma-1>2r+2\theta-2\Rightarrow\gamma+1>2(r+\theta), |  |

we can apply Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") to obtain

|  |  |  |
| --- | --- | --- |
|  | |f​(x)−f​(x¯)|+|g​(x,y)−g​(x¯,y¯)|≤GR​(|x−x¯|+|y−y¯|),\displaystyle|f(x)-f(\bar{x})|+|g(x,y)-g(\bar{x},\bar{y})|\leq G\_{R}(|x-\bar{x}|+|y-\bar{y}|), |  |

where GR≥−αγ(|xγ−1|+|x¯γ−1|)+2θσ(|x2​θ−1|+|x¯2​θ−1|))+2rσ(|y2​r−1|+|y¯2​r−1|)G\_{R}\geq-\alpha\gamma(|x^{\gamma-1}|+|\bar{x}^{\gamma-1}|)+2\theta\sigma(|x^{2\theta-1}|+|\bar{x}^{2\theta-1}|))+2r\sigma(|y^{2r-1}|+|\bar{y}^{2r-1}|).
∎

## 3 Properties of true solution

In this section, we study properties of the true solution to SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")). Since SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) is a financial model, it is a natural requirement to show that the solution is always positive.

### 3.1 Existence of positive solution

The following theorem shows that the solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) is positive almost surely.

###### Theorem 3.1.

Let Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") hold. Then for any given initial value

|  |  |  |  |
| --- | --- | --- | --- |
|  | {x(t):−τ≤t≤0}=ξ(t)∈C([−τ,0]:ℝ+),\{x(t):-\tau\leq t\leq 0\}=\xi(t)\in C([-\tau,0]:\mathbb{R}\_{+}), |  | (13) |

there exists a unique solution x​(t)x(t) to SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and x​(t)>0x(t)>0 almost surely.

###### Proof.

Since the coefficients of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) satisfy local Lipschitz condition in [−τ,∞)[-\tau,\infty), one can show by the standard truncation method that there exists a unique maximal local solution x​(t)x(t) on [−τ,ηe)[-\tau,\eta\_{e}) for any given initial value ([13](https://arxiv.org/html/2510.04092v1#S3.E13 "In Theorem 3.1. ‣ 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), where ηe\eta\_{e} is the explosion time (see [[12](https://arxiv.org/html/2510.04092v1#bib.bib12)]). Let k0>0k\_{0}>0 be sufficiently large such that

|  |  |  |
| --- | --- | --- |
|  | 1k0<min−τ≤t≤0​|ξ​(t)|≤max−τ≤t≤0​|ξ​(t)|<k0.\frac{1}{k\_{0}}<\underset{-\tau\leq t\leq 0}{\min}|\xi(t)|\leq\underset{-\tau\leq t\leq 0}{\max}|\xi(t)|<k\_{0}. |  |

For each integer k≥k0k\geq k\_{0}, we define the stopping time by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηk=inf{t∈[0,ηe):x​(t)∉[1/k,k]}.\eta\_{k}=\inf\{t\in[0,\eta\_{e}):x(t)\not\in[1/k,k]\}. |  | (14) |

We observe that ηk\eta\_{k} is increasing as k→∞k\rightarrow\infty. We set η∞=limk→∞​ηk\eta\_{\infty}=\underset{k\rightarrow\infty}{\lim}\eta\_{k}, whence η∞≤ηe\eta\_{\infty}\leq\eta\_{e} almost surely. In other words, we need to show that η∞=∞\eta\_{\infty}=\infty almost surely to complete the proof. We define a C2C^{2}-function V:ℝ+→ℝ+V:\mathbb{R\_{+}}\rightarrow\mathbb{R\_{+}} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)=xβ−1−β​log⁡(x),V(x)=x^{\beta}-1-\beta\log(x), |  | (15) |

where β∈(0,1)\beta\in(0,1). By applying the operator defined in ([8](https://arxiv.org/html/2510.04092v1#S2.E8 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) to ([15](https://arxiv.org/html/2510.04092v1#S3.E15 "In 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​V​(x,y)\displaystyle LV(x,y) | =β​(xβ−1−x−1)​α​(μ−xγ)+σ22​(β​(β−1)​xβ−2+β​x−2)​x2​θ​y2​r\displaystyle=\beta(x^{\beta-1}-x^{-1})\alpha(\mu-x^{\gamma})+\frac{\sigma^{2}}{2}(\beta(\beta-1)x^{\beta-2}+\beta x^{-2})x^{2\theta}y^{2r} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =α​μ​β​xβ−1−α​μ​β​x−1−α​β​xγ+β−1+α​β​xγ−1\displaystyle=\alpha\mu\beta x^{\beta-1}-\alpha\mu\beta x^{-1}-\alpha\beta x^{\gamma+\beta-1}+\alpha\beta x^{\gamma-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ22​β​(β−1)​x2​θ+β−2​y2​r+σ22​β​x2​θ−2​y2​r.\displaystyle+\frac{\sigma^{2}}{2}\beta(\beta-1)x^{2\theta+\beta-2}y^{2r}+\frac{\sigma^{2}}{2}\beta x^{2\theta-2}y^{2r}. |  |

We note that for β∈(0,1)\beta\in(0,1), γ+β−1>2​θ+2​r+β−2⇒γ+1>2​(r+θ)\gamma+\beta-1>2\theta+2r+\beta-2\Rightarrow\gamma+1>2(r+\theta). So by Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") and for β∈(0,1)\beta\in(0,1), −α​β​xγ+β−1-\alpha\beta x^{\gamma+\beta-1} leads and tends to −∞-\infty for large xx. However, for small xx, −α​μ​β​x−1-\alpha\mu\beta x^{-1} leads and also tends to −∞-\infty. Hence, we can find a constant K0K\_{0} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​V​(x,y)≤K0.LV(x,y)\leq K\_{0}. |  | (16) |

For any t1∈[0,τ]t\_{1}\in[0,\tau], the Itô formula yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(V​(x​(ηk∧t1)))\displaystyle\mathbb{E}(V(x(\eta\_{k}\wedge t\_{1}))) | ≤V​(ξ​(0))+𝔼​∫0ηk∧t1K0​𝑑s\displaystyle\leq V(\xi(0))+\mathbb{E}\int\_{0}^{\eta\_{k}\wedge t\_{1}}K\_{0}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤V​(ξ​(0))+K0​τ,\displaystyle\leq V(\xi(0))+K\_{0}\tau, |  |

for all k≥k0k\geq k\_{0}. Noting that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ηk≤τ)≤𝔼​[V​(x​(ηk∧t1))]V​(k)∧V​(1/k),\displaystyle\mathbb{P}(\eta\_{k}\leq\tau)\leq\frac{\mathbb{E}[V(x(\eta\_{k}\wedge t\_{1}))]}{V(k)\wedge V(1/k)}, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ηk≤τ)≤V​(ξ​(0))+K0​τV​(k)∧V​(1/k).\mathbb{P}(\eta\_{k}\leq\tau)\leq\frac{V(\xi(0))+K\_{0}\tau}{V(k)\wedge V(1/k)}. |  |

As k→∞k\rightarrow\infty, ℙ​(ηk≤τ)→0\mathbb{P}(\eta\_{k}\leq\tau)\rightarrow 0 and hence, η∞>τ\eta\_{\infty}>\tau almost surely. For t1∈[0,2​τ]t\_{1}\in[0,2\tau], the Itô formula gives us

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(V​(x​(ηk∧t1)))\displaystyle\mathbb{E}(V(x(\eta\_{k}\wedge t\_{1}))) | ≤V​(ξ​(0))+𝔼​∫0ηk∧t1K0​𝑑s\displaystyle\leq V(\xi(0))+\mathbb{E}\int\_{0}^{\eta\_{k}\wedge t\_{1}}K\_{0}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤V​(ξ​(0))+2​K0​τ,\displaystyle\leq V(\xi(0))+2K\_{0}\tau, |  |

for all k≥k0k\geq k\_{0}. This also means that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ηk≤2​τ)≤V​(ξ​(0))+2​K0​τV​(k)∧V​(1/k).\mathbb{P}(\eta\_{k}\leq 2\tau)\leq\frac{V(\xi(0))+2K\_{0}\tau}{V(k)\wedge V(1/k)}. |  |

As k→∞k\rightarrow\infty, we get η∞>2​τ\eta\_{\infty}>2\tau almost surely. Meanwhile, for t1∈[0,T]t\_{1}\in[0,T], we also derive from the Itô formula that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(V​(x​(ηk∧t1)))\displaystyle\mathbb{E}(V(x(\eta\_{k}\wedge t\_{1}))) | ≤V​(ξ​(0))+𝔼​∫0ηk∧t1K0​𝑑s\displaystyle\leq V(\xi(0))+\mathbb{E}\int\_{0}^{\eta\_{k}\wedge t\_{1}}K\_{0}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤V​(ξ​(0))+K0​T,\displaystyle\leq V(\xi(0))+K\_{0}T, |  |

for all k≥k0k\geq k\_{0}. This also means that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ηk≤T)≤V​(ξ​(0))+K0​TV​(k)∧V​(1/k).\mathbb{P}(\eta\_{k}\leq T)\leq\frac{V(\xi(0))+K\_{0}T}{V(k)\wedge V(1/k)}. |  | (17) |

As k→∞k\rightarrow\infty, we have η∞>T\eta\_{\infty}>T almost surely. Repeating this procedure for t1∈[0,∞)t\_{1}\in[0,\infty), it is easy to see that ℙ​(η∞≤∞)→0\mathbb{P}(\eta\_{\infty}\leq\infty)\rightarrow 0 as k→∞k\rightarrow\infty. This implies that η∞=∞\eta\_{\infty}=\infty almost surely and hence we must have ηe=∞\eta\_{e}=\infty almost surely as the required assertion.
∎

### 3.2 Boundedness

We also present the following useful result that is required to establish uniform boundedness of the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")).

###### Lemma 3.2.

Let Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") hold and β∈(0,1)\beta\in(0,1). Then for any initial value ξ​(0)\xi(0), the solution x​(t)x(t) of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) fulfils

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[x​(t)β−1−β​log⁡(x​(t))]≤ξ​(0)β−1−β​log⁡(ξ​(0))+K¯0\mathbb{E}\Big[x(t)^{\beta}-1-\beta\log(x(t))\Big]\leq\xi(0)^{\beta}-1-\beta\log(\xi(0))+\bar{K}\_{0} |  |

for all t≥0t\geq 0 and

|  |  |  |
| --- | --- | --- |
|  | lim supt→∞​𝔼​[x​(t)β−1−β​log⁡(x​(t))]≤K¯0\underset{t\rightarrow\infty}{\limsup}\mathbb{E}\Big[x(t)^{\beta}-1-\beta\log(x(t))\Big]\leq\bar{K}\_{0} |  |

where K¯0\bar{K}\_{0} is a positive constant that does not depend on the initial value ξ​(0)\xi(0).

###### Proof.

We define V1∈C2,1​(ℝ+×ℝ+;ℝ+)V\_{1}\in C^{2,1}(\mathbb{R}\_{+}\times\mathbb{R}\_{+};\mathbb{R}\_{+}) by V1​(x,t)=et​V​(x)V\_{1}(x,t)=e^{t}V(x), where V​(x)V(x) is the same as ([15](https://arxiv.org/html/2510.04092v1#S3.E15 "In 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")). We compute from the diffusion operator in ([8](https://arxiv.org/html/2510.04092v1#S2.E8 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​V1​(x,y,t)\displaystyle LV\_{1}(x,y,t) | =et[xβ−1−βlog(x)+αμβxβ−1−αμβx−1−αβxγ+β−1+αβxγ−1\displaystyle=e^{t}\Big[x^{\beta}-1-\beta\log(x)+\alpha\mu\beta x^{\beta-1}-\alpha\mu\beta x^{-1}-\alpha\beta x^{\gamma+\beta-1}+\alpha\beta x^{\gamma-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ22β(β−1)x2​θ+β−2y2​r+σ22βx2​θ−2y2​r]\displaystyle+\frac{\sigma^{2}}{2}\beta(\beta-1)x^{2\theta+\beta-2}y^{2r}+\frac{\sigma^{2}}{2}\beta x^{2\theta-2}y^{2r}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =et[xβ−1−βlog(x)]+et[αμβxβ−1−αμβx−1−αβxγ+β−1+αβxγ−1\displaystyle=e^{t}\Big[x^{\beta}-1-\beta\log(x)\Big]+e^{t}\Big[\alpha\mu\beta x^{\beta-1}-\alpha\mu\beta x^{-1}-\alpha\beta x^{\gamma+\beta-1}+\alpha\beta x^{\gamma-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ22β(β−1)x2​θ+β−2y2​r+σ22βx2​θ−2y2​r].\displaystyle+\frac{\sigma^{2}}{2}\beta(\beta-1)x^{2\theta+\beta-2}y^{2r}+\frac{\sigma^{2}}{2}\beta x^{2\theta-2}y^{2r}\Big]. |  |

Hence, by ([16](https://arxiv.org/html/2510.04092v1#S3.E16 "In 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), there exists a constant such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​V1​(x,y,t)\displaystyle LV\_{1}(x,y,t) | ≤et​(V​(x)+L​V​(x,y))\displaystyle\leq e^{t}(V(x)+LV(x,y)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤et​K¯0.\displaystyle\leq e^{t}\bar{K}\_{0}. |  |

Using the same stopping time as defined in ([14](https://arxiv.org/html/2510.04092v1#S3.E14 "In 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we derive from the Itô formula that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​V1​(x​(t∧τk),t∧τk)≤V1​(ξ​(0),0)+∫0t∧τkL​V1​(x​(s),x​(t−τ),s)​𝑑s.\displaystyle\mathbb{E}V\_{1}(x(t\wedge\tau\_{k}),t\wedge\tau\_{k})\leq V\_{1}(\xi(0),0)+\int\_{0}^{t\wedge\tau\_{k}}LV\_{1}(x(s),x(t-\tau),s)ds. |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | et∧τk​V​(x​(t∧τk))≤V​(ξ​(0))+∫0t∧τkes​(V​(x​(s))+L​V​(x​(s),x​(t−τ)))​𝑑s.\displaystyle e^{t\wedge\tau\_{k}}V(x(t\wedge\tau\_{k}))\leq V(\xi(0))+\int\_{0}^{t\wedge\tau\_{k}}e^{s}(V(x(s))+LV(x(s),x(t-\tau)))ds. |  |

By applying the Fatou lemma and setting k→∞k\rightarrow\infty, we now have

|  |  |  |
| --- | --- | --- |
|  | et​V​(x​(t))≤V​(ξ​(0))+et​K¯0.\displaystyle e^{t}V(x(t))\leq V(\xi(0))+e^{t}\bar{K}\_{0}. |  |

This also implies that

|  |  |  |
| --- | --- | --- |
|  | x​(t)β−1−β​log⁡(x​(t))≤V​(ξ​(0))et+K¯0,\displaystyle x(t)^{\beta}-1-\beta\log(x(t))\leq\frac{V(\xi(0))}{e^{t}}+\bar{K}\_{0}, |  |

which gives both assertions as required.
∎

The following result reveals that the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) will stay in a compact support with large probability.

###### Theorem 3.3.

Let Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") hold and β∈(0,1)\beta\in(0,1). Then for any initial value ξ​(0)\xi(0) and k>k0k>k\_{0}, there exists a constant K¯0\bar{K}\_{0} such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(1/k<x​(t)<k)≥1−ϵ\displaystyle\mathbb{P}(1/k<x(t)<k)\geq 1-\epsilon |  |

for all t≥0t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ϵ=[ξ​(0)β−1−β​log⁡(ξ​(0))+K¯0]​[1(1/k)β−1+β​log⁡(k)+1kβ−1−β​log⁡(k)].\displaystyle\epsilon=\Big[\xi(0)^{\beta}-1-\beta\log(\xi(0))+\bar{K}\_{0}\Big]\Big[\frac{1}{(1/k)^{\beta}-1+\beta\log(k)}+\frac{1}{k^{\beta}-1-\beta\log(k)}\Big]. |  |

###### Proof.

We compute from Lemma [3.2](https://arxiv.org/html/2510.04092v1#S3.Thmdefinition2 "Lemma 3.2. ‣ 3.2 Boundedness ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") that for any t≥0t\geq 0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ(x(t)\displaystyle\mathbb{P}(x(t) | ≤1/k)≤𝔼[1{x​(t)≤1/k}x​(t)β−1−β​log⁡(x​(t))(1/k)β−1+β​log⁡(k)]\displaystyle\leq 1/k)\leq\mathbb{E}\Big[1\_{\{x(t)\leq 1/k\}}\frac{x(t)^{\beta}-1-\beta\log(x(t))}{(1/k)^{\beta}-1+\beta\log(k)}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ξ​(0)β−1−β​log⁡(ξ​(0))+K¯0(1/k)β−1+β​log⁡(k).\displaystyle\leq\frac{\xi(0)^{\beta}-1-\beta\log(\xi(0))+\bar{K}\_{0}}{(1/k)^{\beta}-1+\beta\log(k)}. |  |

Similarly, we also obtain from Lemma [3.2](https://arxiv.org/html/2510.04092v1#S3.Thmdefinition2 "Lemma 3.2. ‣ 3.2 Boundedness ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") that for any t≥0t\geq 0

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ(x(t)\displaystyle\mathbb{P}(x(t) | ≥k)≤𝔼[1{x​(t)≥k}x​(t)β−1−β​log⁡(x​(t))kβ−1−β​log⁡(k)]\displaystyle\geq k)\leq\mathbb{E}\Big[1\_{\{x(t)\geq k\}}\frac{x(t)^{\beta}-1-\beta\log(x(t))}{k^{\beta}-1-\beta\log(k)}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ξ​(0)β−1−β​log⁡(ξ​(0))+K¯0kβ−1−β​log⁡(k).\displaystyle\leq\frac{\xi(0)^{\beta}-1-\beta\log(\xi(0))+\bar{K}\_{0}}{k^{\beta}-1-\beta\log(k)}. |  |

This implies that,

|  |  |  |
| --- | --- | --- |
|  | ℙ(/1k<x(t)<k)<1−[ξ(0)β−1−βlog(ξ(0))+K¯0][1(1/k)β−1+β​log⁡(k)+1kβ−1−β​log⁡(k)],\displaystyle\mathbb{P}(/1k<x(t)<k)<1-\Big[\xi(0)^{\beta}-1-\beta\log(\xi(0))+\bar{K}\_{0}\Big]\Big[\frac{1}{(1/k)^{\beta}-1+\beta\log(k)}+\frac{1}{k^{\beta}-1-\beta\log(k)}\Big], |  |

as required.
∎

## 4 Numerical method

In this section, we develop truncated EM techniques to estimate the solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")). Moreover, we establish some properties of the numerical solutions.

### 4.1 The truncated EM method

Before we construct the numerical method, we need to extend the domain of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) from ℝ+\mathbb{R}\_{+} to ℝ\mathbb{R}. We should mention that this extension does not affect previous results in anyway. To define the truncated EM method, we choose a strictly increasing continuous function z:ℝ+→ℝ+z:\mathbb{R}\_{+}\rightarrow\mathbb{R}\_{+} such that z​(u)→∞z(u)\rightarrow\infty as u→∞u\rightarrow\infty and

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup|x|∨|y|≤u(|f​(x)|∨g​(x,y))≤z​(u),\sup\_{|x|\vee|y|\leq u}\Big(|f(x)|\vee g(x,y)\Big)\leq z(u), |  | (18) |

for all u≥0u\geq 0. Denote by z−1z^{-1} the inverse function of zz and we see that z−1z^{-1} is strictly increasing continuous function from [z​(0),∞)[z(0),\infty) to ℝ+\mathbb{R}\_{+}. We also choose a number Δ∗∈(0,1]\Delta^{\*}\in(0,1] and a strictly decreasing function
ψ:(0,Δ∗]→ℝ+\psi:(0,\Delta^{\*}]\rightarrow\mathbb{R}\_{+} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(Δ∗)≥z​(1),limΔ→0ψ​(Δ)=∞​ and ​Δ1/4​ψ​(Δ)≤1,∀Δ∈(0,1).\quad\psi(\Delta^{\*})\geq z(1),\lim\_{\Delta\rightarrow 0}\psi(\Delta)=\infty\text{ and }\Delta^{1/4}\psi(\Delta)\leq 1,\quad\forall\Delta\in(0,1). |  | (19) |

For a given step size Δ∈(0,Δ∗)\Delta\in(0,\Delta^{\*}), we then define the truncated functions by

|  |  |  |  |
| --- | --- | --- | --- |
|  | fΔ​(x)\displaystyle f\_{\Delta}(x) | ={f​(x∧z−1​(ψ​(Δ))),if x≥0 α​μ,if x<0,\displaystyle=\begin{cases}f\Big(x\wedge z^{-1}(\psi(\Delta))\Big),&\mbox{if $x\geq 0$ }\\ \alpha\mu,&\mbox{if $x<0$},\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | gΔ​(x,y)\displaystyle g\_{\Delta}(x,y) | ={g​(x∧z−1​(ψ​(Δ)),y∧z−1​(ψ​(Δ))),if x,y≥0 0,if x,y<0,\displaystyle=\begin{cases}g\Big(x\wedge z^{-1}(\psi(\Delta)),y\wedge z^{-1}(\psi(\Delta))\Big),&\mbox{if $x,y\geq 0$ }\\ 0,&\mbox{if $x,y<0$},\end{cases} |  |

for all x,y∈ℝx,y\in\mathbb{R}. So for x,y∈[0,z−1​(ψ​(Δ))]x,y\in[0,z^{-1}(\psi(\Delta))], we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |fΔ​(x)|∨gΔ​(x,y)≤z​(z−1​(ψ​(Δ)))=ψ​(Δ),\displaystyle|f\_{\Delta}(x)|\vee g\_{\Delta}(x,y)\leq z(z^{-1}(\psi(\Delta)))=\psi(\Delta), |  | (20) |

for all x,y∈ℝx,y\in\mathbb{R}. That is, fΔf\_{\Delta} and gΔg\_{\Delta} are bounded by ψ​(Δ)\psi(\Delta) although ff and gg are unbounded. From now on, we let T>0T>0 be arbitrarily fixed. We also let the step size Δ∈(0,Δ∗]\Delta\in(0,\Delta^{\*}] be a fraction of τ\tau, that is, Δ=τM\Delta=\frac{\tau}{M} for some integer M>τM>\tau. We construct the discrete-time truncated EM approximation of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) by defining tk=k​Δt\_{k}=k\Delta for −M≤k≤∞-M\leq k\leq\infty, setting XΔ​(tk)=ξ​(tk)X\_{\Delta}(t\_{k})=\xi(t\_{k}) for −M≤k≤0-M\leq k\leq 0 and computing

|  |  |  |  |
| --- | --- | --- | --- |
|  | XΔ​(tk+1)=XΔ​(tk)+fΔ​(XΔ​(tk))​Δ+gΔ​(XΔ​(tk),XΔ​(tk−M))​Δ​BkX\_{\Delta}(t\_{k+1})=X\_{\Delta}(t\_{k})+f\_{\Delta}(X\_{\Delta}(t\_{k}))\Delta+g\_{\Delta}(X\_{\Delta}(t\_{k}),X\_{\Delta}(t\_{k-M}))\Delta B\_{k} |  | (21) |

for k≥0k\geq 0, where Δ​Bk=B​(tk+1)−B​(tk)\Delta B\_{k}=B(t\_{k+1})-B(t\_{k}) is an increment of the Brownian motion. For t∈[−τ,∞)t\in[-\tau,\infty), we define the continuous-time truncated EM step process by

|  |  |  |  |
| --- | --- | --- | --- |
|  | x¯Δ​(t)=∑k=−M∞XΔ​(tk)​1[tk,tk+1)​(t)\bar{x}\_{\Delta}(t)=\sum\_{k=-M}^{\infty}X\_{\Delta}(t\_{k})1\_{[t\_{k},t\_{k+1})}(t) |  | (22) |

where 1[tk,tk+1)1\_{[t\_{k},t\_{k+1})} is the indicator function on [tk,tk+1)[t\_{k},t\_{k+1}). The continuous-time continuous truncated EM process is defined by setting xΔ​(t)=ξ​(t)x\_{\Delta}(t)=\xi(t) for t∈[−τ,0]t\in[-\tau,0] while for t≥0t\geq 0, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | xΔ​(t)=ξ​(0)+∫0tfΔ​(x¯Δ​(s))​𝑑s+∫0tgΔ​(x¯Δ​(s),x¯Δ​(s−τ))​𝑑B​(s).x\_{\Delta}(t)=\xi(0)+\int\_{0}^{t}f\_{\Delta}(\bar{x}\_{\Delta}(s))ds+\int\_{0}^{t}g\_{\Delta}(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))dB(s). |  | (23) |

We observe that xΔ​(t)x\_{\Delta}(t) is an Itô process on t≥0t\geq 0 satisfying Itô differential

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xΔ​(t)=fΔ​(x¯Δ​(t))​d​t+gΔ​(x¯Δ​(t),x¯Δ​(t−τ))​d​B​(t).dx\_{\Delta}(t)=f\_{\Delta}(\bar{x}\_{\Delta}(t))dt+g\_{\Delta}(\bar{x}\_{\Delta}(t),\bar{x}\_{\Delta}(t-\tau))dB(t). |  | (24) |

It is important to note that xΔ​(tk)=x¯Δ​(tk)=XΔ​(tk)x\_{\Delta}(t\_{k})=\bar{x}\_{\Delta}(t\_{k})=X\_{\Delta}(t\_{k}) for k≥−Mk\geq-M.

### 4.2 Properties of numerical solution

The following lemma shows that the discrete-time process x¯Δ​(t)\bar{x}\_{\Delta}(t) and the continuous-time process xΔ​(t)x\_{\Delta}(t) are close to each other in the strong sense.

###### Lemma 4.1.

For any fixed Δ∈(0,Δ∗]\Delta\in(0,\Delta^{\*}] and p≥2p\geq 2, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​|xΔ​(t)−x¯Δ​(t)|p≤cp​Δp/2​(ψ​(Δ))p,\mathbb{E}|x\_{\Delta}(t)-\bar{x}\_{\Delta}(t)|^{p}\leq c\_{p}\Delta^{p/2}(\psi(\Delta))^{p}, |  | (25) |

for all t≥0t\geq 0, where cpc\_{p} is a generic constant that is dependent only on pp.

###### Proof.

Fix any Δ∈(0,Δ∗]\Delta\in(0,\Delta^{\*}] and t≥0t\geq 0. Then there is a unique integer k≥0k\geq 0 such that tk≤t≤tk+1t\_{k}\leq t\leq t\_{k+1}. By elementary inequality and ([20](https://arxiv.org/html/2510.04092v1#S4.E20 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|xΔ​(t)−x¯Δ​(t)|p=𝔼​|xΔ​(t)−x¯Δ​(tk)|p\displaystyle\mathbb{E}|x\_{\Delta}(t)-\bar{x}\_{\Delta}(t)|^{p}=\mathbb{E}|x\_{\Delta}(t)-\bar{x}\_{\Delta}(t\_{k})|^{p} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​(𝔼​|∫tktfΔ​(x¯Δ​(s))​𝑑s|p+𝔼​|∫tktgΔ​(x¯Δ​(s),x¯Δ​(s−τ))​𝑑B​(s)|p)\displaystyle\leq C\_{p}\Big(\mathbb{E}\big|\int\_{t\_{k}}^{t}f\_{\Delta}(\bar{x}\_{\Delta}(s))ds\big|^{p}+\mathbb{E}\big|\int\_{t\_{k}}^{t}g\_{\Delta}(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))dB(s)\big|^{p}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​(Δp−1​𝔼​∫tkt|fΔ​(x¯Δ​(s))|p​𝑑s+Δ(p−2)/2​𝔼​∫tkt|gΔ​(x¯Δ​(s),x¯Δ​(s−τ))|p​𝑑s)\displaystyle\leq C\_{p}\Big(\Delta^{p-1}\mathbb{E}\int\_{t\_{k}}^{t}|f\_{\Delta}(\bar{x}\_{\Delta}(s))|^{p}ds+\Delta^{(p-2)/2}\mathbb{E}\int\_{t\_{k}}^{t}|g\_{\Delta}(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))|^{p}ds\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​(Δp−1​(ψ​(Δ))p​Δ+Δ(p−2)/2​(ψ​(Δ))p​Δ)\displaystyle\leq C\_{p}\Big(\Delta^{p-1}(\psi(\Delta))^{p}\Delta+\Delta^{(p-2)/2}(\psi(\Delta))^{p}\Delta\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​(Δp​(ψ​(Δ))p+Δp/2​(ψ​(Δ))p)≤cp​Δp/2​(ψ​(Δ))p,\displaystyle\leq C\_{p}\Big(\Delta^{p}(\psi(\Delta))^{p}+\Delta^{p/2}(\psi(\Delta))^{p}\Big)\leq c\_{p}\Delta^{p/2}(\psi(\Delta))^{p}, |  |

where cp=Cp∨1c\_{p}=C\_{p}\vee 1 and from ([19](https://arxiv.org/html/2510.04092v1#S4.E19 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we obtain Δp/2​(ψ​(Δ))p≤Δp/4\Delta^{p/2}(\psi(\Delta))^{p}\leq\Delta^{p/4}.
∎

The following lemma reveals the probability that the truncated EM solutions do not explode in finite time.

###### Lemma 4.2.

Let Assumptions [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") and [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") hold and T>0T>0 be fixed. For any sufficiently large integer k>0k>0, define the stopping time by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηΔ=inf{t∈[0,T]:xΔ​(t)∉[1/k,k]}.\eta\_{\Delta}=\inf\{t\in[0,T]:x\_{\Delta}(t)\notin[1/k,k]\}. |  | (26) |

Then for any fixed Δ∈(0,Δ∗]\Delta\in(0,\Delta^{\*}], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ηΔ≤T)≤V​(ξ​(0))+K1​T+K3​D​Δℓ+cp​(K2+K3)​Δ1/2​ψ​(Δ)​TV​(1/k)∧V​(k),\mathbb{P}(\eta\_{\Delta}\leq T)\leq\frac{V(\xi(0))+K\_{1}T+K\_{3}D\Delta^{\ell}+c\_{p}(K\_{2}+K\_{3})\Delta^{1/2}\psi(\Delta)T}{V(1/k)\wedge V(k)}, |  | (27) |

where K1K\_{1}, K2K\_{2} and K3K\_{3} are generic constants and VV is defined in ([15](https://arxiv.org/html/2510.04092v1#S3.E15 "In 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")).

###### Proof.

For t1∈[0,T]t\_{1}\in[0,T], we apply the Itô formula to ([24](https://arxiv.org/html/2510.04092v1#S4.E24 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) to compute

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(V​(xΔ​(t∧ηΔ)))−V​(ξ​(0))\displaystyle\mathbb{E}(V(x\_{\Delta}(t\wedge\eta\_{\Delta})))-V(\xi(0)) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​∫0t1∧ηΔ(Vx​(xΔ​(s))​fΔ​(x¯Δ​(s))+12​Vx​x​(xΔ​(s))​gΔ​(x¯Δ​(s),x¯Δ​(s−τ))2)​𝑑s\displaystyle=\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta\_{\Delta}}\Big(V\_{x}(x\_{\Delta}(s))f\_{\Delta}(\bar{x}\_{\Delta}(s))+\frac{1}{2}V\_{xx}(x\_{\Delta}(s))g\_{\Delta}(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))^{2}\Big)ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼​∫0ηΔ∧t1(Vx​(xΔ​(s))​fΔ​(xΔ​(s))+12​Vx​x​(xΔ​(s))​gΔ​(xΔ​(s),xΔ​(s−τ))2)​𝑑s\displaystyle\leq\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}\Big(V\_{x}(x\_{\Delta}(s))f\_{\Delta}(x\_{\Delta}(s))+\frac{1}{2}V\_{xx}(x\_{\Delta}(s))g\_{\Delta}(x\_{\Delta}(s),x\_{\Delta}(s-\tau))^{2}\Big)ds |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼​∫0ηΔ∧t1Vx​(xΔ​(s))​(fΔ​(x¯Δ​(s))−fΔ​(xΔ​(s)))​𝑑s\displaystyle+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}V\_{x}(x\_{\Delta}(s))\Big(f\_{\Delta}(\bar{x}\_{\Delta}(s))-f\_{\Delta}(x\_{\Delta}(s))\Big)ds |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼​∫0ηΔ∧t112​Vx​x​(xΔ​(s))​(gΔ​(x¯Δ​(s),x¯Δ​(s−τ))2−gΔ​(xΔ​(s),xΔ​(s−τ))2)​𝑑s.\displaystyle+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}\frac{1}{2}V\_{xx}(x\_{\Delta}(s))\Big(g\_{\Delta}(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))^{2}-g\_{\Delta}(x\_{\Delta}(s),x\_{\Delta}(s-\tau))^{2}\Big)ds. |  |

By recalling the definition of the truncated functions in ([18](https://arxiv.org/html/2510.04092v1#S4.E18 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | fΔ​(⋅)=f​(⋅)​ and ​gΔ​(⋅,⋅)=g​(⋅,⋅).f\_{\Delta}(\cdot)=f(\cdot)\text{ and }g\_{\Delta}(\cdot,\cdot)=g(\cdot,\cdot). |  | (28) |

Also, for s∈[0,ηΔ∧t1]s\in[0,\eta\_{\Delta}\wedge t\_{1}] with xΔ​(s),x¯Δ​(s),xΔ​(s−τ),x¯Δ​(s−τ)∈[1/k,k]x\_{\Delta}(s),\bar{x}\_{\Delta}(s),x\_{\Delta}(s-\tau),\bar{x}\_{\Delta}(s-\tau)\in[1/k,k], we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x¯Δ​(s),x¯Δ​(s−τ))∨g​(xΔ​(s),xΔ​(s−τ))≤z​(k).g(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))\vee g(x\_{\Delta}(s),x\_{\Delta}(s-\tau))\leq z(k). |  | (29) |

By Assumption [2.2](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition2 "Assumption 2.2. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(V​(xΔ​(t∧ηΔ)))−V​(ξ​(0))≤K1​T+𝔼​∫0ηΔ∧t1Vx​(xΔ​(s))​|f​(x¯Δ​(s))−f​(xΔ​(s))|​𝑑s\displaystyle\mathbb{E}(V(x\_{\Delta}(t\wedge\eta\_{\Delta})))-V(\xi(0))\leq K\_{1}T+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}V\_{x}(x\_{\Delta}(s))|f(\bar{x}\_{\Delta}(s))-f(x\_{\Delta}(s))|ds |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼​∫0ηΔ∧t112​Vx​x​(xΔ​(s))​(g​(x¯Δ​(s),x¯Δ​(s−τ))2−g​(xΔ​(s),xΔ​(s−τ))2)​𝑑s,\displaystyle+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}\frac{1}{2}V\_{xx}(x\_{\Delta}(s))\Big(g(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))^{2}-g(x\_{\Delta}(s),x\_{\Delta}(s-\tau))^{2}\Big)ds, |  |

where L​V​(xΔ​(s),xΔ​(s−τ))≤K1LV(x\_{\Delta}(s),x\_{\Delta}(s-\tau))\leq K\_{1} for s∈[0,t∧ηΔ]s\in[0,t\wedge\eta\_{\Delta}]. By an elementary inequality, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(V​(xΔ​(t∧ηΔ)))−V​(ξ​(0))≤K1​T+𝔼​∫0ηΔ∧t1Vx​(xΔ​(s))​|f​(x¯Δ​(s))−f​(xΔ​(s))|​𝑑s\displaystyle\mathbb{E}(V(x\_{\Delta}(t\wedge\eta\_{\Delta})))-V(\xi(0))\leq K\_{1}T+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}V\_{x}(x\_{\Delta}(s))|f(\bar{x}\_{\Delta}(s))-f(x\_{\Delta}(s))|ds |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼∫0ηΔ∧t112Vx​x(xΔ(s))(|g(x¯Δ(s),x¯Δ(s−τ))−g(xΔ(s),xΔ(s−τ))|\displaystyle+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}\frac{1}{2}V\_{xx}(x\_{\Delta}(s))\Big(|g(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))-g(x\_{\Delta}(s),x\_{\Delta}(s-\tau))| |  |
|  |  |  |
| --- | --- | --- |
|  | ×|g(x¯Δ(s),x¯Δ(s−τ))+g(xΔ(s),xΔ(s−τ))|)ds.\displaystyle\times|g(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))+g(x\_{\Delta}(s),x\_{\Delta}(s-\tau))|\Big)ds. |  |

By ([20](https://arxiv.org/html/2510.04092v1#S4.E20 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), ([28](https://arxiv.org/html/2510.04092v1#S4.E28 "In 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), ([29](https://arxiv.org/html/2510.04092v1#S4.E29 "In 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and Lemma [2.3](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition3 "Lemma 2.3. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we now have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(V​(xΔ​(t∧ηΔ)))\displaystyle\mathbb{E}(V(x\_{\Delta}(t\wedge\eta\_{\Delta}))) | ≤V​(ξ​(0))+K1​T+𝔼​∫0t1∧ηΔGk​Vx​(xΔ​(s))​|x¯Δ​(s)−xΔ​(s)|​𝑑s\displaystyle\leq V(\xi(0))+K\_{1}T+\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta\_{\Delta}}G\_{k}V\_{x}(x\_{\Delta}(s))|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​∫0ηΔ∧t1(z​(k))2​Gk​Vx​x​(xΔ​(s))​|x¯Δ​(s)−xΔ​(s)|​𝑑s\displaystyle+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}(z(k))^{2}G\_{k}V\_{xx}(x\_{\Delta}(s))|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​∫0ηΔ∧t1(z​(k))2​Gk​Vx​x​(xΔ​(s))​|x¯Δ​(s−τ)−xΔ​(s−τ)|​𝑑s\displaystyle+\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}(z(k))^{2}G\_{k}V\_{xx}(x\_{\Delta}(s))|\bar{x}\_{\Delta}(s-\tau)-x\_{\Delta}(s-\tau)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤V​(ξ​(0))+K1​T+K2​𝔼​∫0ηΔ∧t1|x¯Δ​(s)−xΔ​(s)|​𝑑s\displaystyle\leq V(\xi(0))+K\_{1}T+K\_{2}\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +K3​𝔼​∫0ηΔ∧t1|x¯Δ​(s−τ)−xΔ​(s−τ)|​𝑑s,\displaystyle+K\_{3}\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}|\bar{x}\_{\Delta}(s-\tau)-x\_{\Delta}(s-\tau)|ds, |  |

where

|  |  |  |
| --- | --- | --- |
|  | K2=max1/k≤x≤k⁡(Gk​Vx​(x)+(z​(k))2​Gk​Vx​x​(x))K\_{2}=\max\_{1/k\leq x\leq k}\Big(G\_{k}V\_{x}(x)+(z(k))^{2}G\_{k}V\_{xx}(x)\Big) |  |

and

|  |  |  |
| --- | --- | --- |
|  | K3=max1/k≤x≤k⁡((z​(k))2​Gk​Vx​x​(x)).K\_{3}=\max\_{1/k\leq x\leq k}\Big((z(k))^{2}G\_{k}V\_{xx}(x)\Big). |  |

So by Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") and Lemma [4.1](https://arxiv.org/html/2510.04092v1#S4.Thmdefinition1 "Lemma 4.1. ‣ 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(V​(xΔ​(t∧ηΔ)))\displaystyle\mathbb{E}(V(x\_{\Delta}(t\wedge\eta\_{\Delta}))) | ≤V​(ξ​(0))+K1​T+K2​𝔼​∫0ηΔ∧t1|x¯Δ​(s)−xΔ​(s)|​𝑑s\displaystyle\leq V(\xi(0))+K\_{1}T+K\_{2}\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +K3​𝔼​∫−τηΔ∧t1|x¯Δ​(s)−xΔ​(s)|​𝑑s\displaystyle+K\_{3}\mathbb{E}\int\_{-\tau}^{\eta\_{\Delta}\wedge t\_{1}}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤V​(ξ​(0))+K1​T+K2​𝔼​∫0ηΔ∧t1|x¯Δ​(s)−xΔ​(s)|​𝑑s\displaystyle\leq V(\xi(0))+K\_{1}T+K\_{2}\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +K3​𝔼​∫−τ0|ξ​([s/Δ]​Δ)−ξ​(s)|​𝑑s+K3​𝔼​∫0ηΔ∧t1|x¯Δ​(s)−xΔ​(s)|​𝑑s\displaystyle+K\_{3}\mathbb{E}\int\_{-\tau}^{0}|\xi([s/\Delta]\Delta)-\xi(s)|ds+K\_{3}\mathbb{E}\int\_{0}^{\eta\_{\Delta}\wedge t\_{1}}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤V​(ξ​(0))+K1​T+K3​∫−τ0𝔼​|ξ​([s/Δ]​Δ)−ξ​(s)|​𝑑s\displaystyle\leq V(\xi(0))+K\_{1}T+K\_{3}\int\_{-\tau}^{0}\mathbb{E}|\xi([s/\Delta]\Delta)-\xi(s)|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(K2+K3)​∫0T(𝔼​|x¯Δ​(s)−xΔ​(s)|p)1/p​𝑑s\displaystyle+(K\_{2}+K\_{3})\int\_{0}^{T}(\mathbb{E}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p})^{1/p}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤V​(ξ​(0))+K1​T+K3​D​Δℓ+cp​(K2+K3)​Δ1/2​ψ​(Δ)​T.\displaystyle\leq V(\xi(0))+K\_{1}T+K\_{3}D\Delta^{\ell}+c\_{p}(K\_{2}+K\_{3})\Delta^{1/2}\psi(\Delta)T. |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ηΔ≤T)≤V​(ξ​(0))+K1​T+K3​D​Δℓ+cp​(K2+K3)​Δ1/2​ψ​(Δ)​TV​(1/k)∧V​(k),\mathbb{P}(\eta\_{\Delta}\leq T)\leq\frac{V(\xi(0))+K\_{1}T+K\_{3}D\Delta^{\ell}+c\_{p}(K\_{2}+K\_{3})\Delta^{1/2}\psi(\Delta)T}{V(1/k)\wedge V(k)}, |  |

as required.
∎

## 5 Convergence analysis

In this section, we study the finite-time convergence of the truncated EM solutions to the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")). Further, we show that the truncated EM solutions converge to the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) in probability. We perform simulation examples to support the convergence result and justify the convergence result to evaluate some option contracts.

### 5.1 Finite-time error bound

The following lemma shows that the truncated EM solutions converge to the true solution of SDDE ([6](https://arxiv.org/html/2510.04092v1#S1.E6 "In 1 Introduction ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) in finite time.

###### Lemma 5.1.

Let Assumptions [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") and [2.2](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition2 "Assumption 2.2. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") hold. Then for any p≥2p\geq 2, fixed T>0T>0, sufficiently large k>0k>0 and Δ∈(0,Δ∗]\Delta\in(0,\Delta^{\*}], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(sup0≤t≤T|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)≤K8​(Δℓ∨Δp/2​(ψ​(Δ))p),\mathbb{E}\Big(\sup\_{0\leq t\leq T}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)\leq K\_{8}(\Delta^{\ell}\vee\Delta^{p/2}(\psi(\Delta))^{p}), |  | (30) |

where K8K\_{8} is a generic constant that depends on kk but is independent of Δ\Delta and ηkΔ=ηk∧ηΔ\eta^{\Delta}\_{k}=\eta\_{k}\wedge\eta\_{\Delta}, where ηk\eta\_{k} and ηΔ\eta\_{\Delta} are defined in ([14](https://arxiv.org/html/2510.04092v1#S3.E14 "In 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([26](https://arxiv.org/html/2510.04092v1#S4.E26 "In Lemma 4.2. ‣ 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) respectively. Consequently, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limΔ→0𝔼​(sup0≤t≤T|x¯Δ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)=0.\lim\_{\Delta\rightarrow 0}\mathbb{E}\Big(\sup\_{0\leq t\leq T}|\bar{x}\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)=0. |  | (31) |

###### Proof.

It follows from ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([24](https://arxiv.org/html/2510.04092v1#S4.E24 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) that for t∈[0,t1]t\in[0,t\_{1}], we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(sup0≤t≤t1|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)≤K4+K5,\displaystyle\mathbb{E}\Big(\sup\_{0\leq t\leq t\_{1}}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)\leq K\_{4}+K\_{5}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | K4\displaystyle K\_{4} | =2p−1​(𝔼​|∫0t1∧ηkΔ(fΔ​(x¯Δ​(s))−f​(x​(s)))​𝑑s|p)\displaystyle=2^{p-1}\Big(\mathbb{E}\Big|\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}(f\_{\Delta}(\bar{x}\_{\Delta}(s))-f(x(s)))ds\Big|^{p}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K5\displaystyle K\_{5} | =2p−1​(𝔼​(sup0≤t≤t1|∫0t1∧ηkΔ)(gΔ​(x¯Δ​(s),x¯Δ​(s−τ))−g​(x​(s),x​(s−τ)))​𝑑B​(s)|p)).\displaystyle=2^{p-1}\Big(\mathbb{E}(\sup\_{0\leq t\leq t\_{1}}\Big|\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k})}(g\_{\Delta}(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))-g(x(s),x(s-\tau)))dB(s)\Big|^{p})\Big). |  |

By the Hölder inequality and ([28](https://arxiv.org/html/2510.04092v1#S4.E28 "In 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | K4\displaystyle K\_{4} | ≤2p−1​Tp−1​(𝔼​∫0t1∧ηkΔ|fΔ​(x¯Δ​(s))−f​(x​(s))|p​𝑑s)\displaystyle\leq 2^{p-1}T^{p-1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|f\_{\Delta}(\bar{x}\_{\Delta}(s))-f(x(s))|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2p−1​Tp−1​(𝔼​∫0t1∧ηkΔ|f​(x¯Δ​(s))−f​(x​(s))|p​𝑑s)\displaystyle\leq 2^{p-1}T^{p-1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|f(\bar{x}\_{\Delta}(s))-f(x(s))|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2p−1​Tp−1​Gkp​𝔼​∫0t1∧ηkΔ|x¯Δ​(s)−x​(s)|p​𝑑s.\displaystyle\leq 2^{p-1}T^{p-1}G\_{k}^{p}\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|\bar{x}\_{\Delta}(s)-x(s)|^{p}ds. |  |

Moreover, by the elementary inequality, we now have

|  |  |  |  |
| --- | --- | --- | --- |
|  | K4\displaystyle K\_{4} | ≤c0​𝔼​∫0t1∧ηkΔ|x¯Δ​(s)−xΔ​(s)|p​𝑑s+c0​𝔼​∫0t1∧ηkΔ|xΔ​(s)−x​(s)|p​𝑑s\displaystyle\leq c\_{0}\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p}ds+c\_{0}\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|x\_{\Delta}(s)-x(s)|^{p}ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤c0​∫0T𝔼​|x¯Δ​(s)−xΔ​(s)|p​𝑑s+c0​∫0t1𝔼​(sup0≤t≤s|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)​𝑑s,\displaystyle\leq c\_{0}\int\_{0}^{T}\mathbb{E}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p}ds+c\_{0}\int\_{0}^{t\_{1}}\mathbb{E}\Big(\sup\_{0\leq t\leq s}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)ds, |  | (32) |

where c0=22​(p−1)​Tp−1​Gkpc\_{0}=2^{2(p-1)}T^{p-1}G\_{k}^{p}. By the Burkholder-Davis-Gundy inequality, Lemma [2.3](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition3 "Lemma 2.3. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") and ([28](https://arxiv.org/html/2510.04092v1#S4.E28 "In 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we also have

|  |  |  |  |
| --- | --- | --- | --- |
|  | K5\displaystyle K\_{5} | ≤2p−1​Tp−22​c¯p​(𝔼​∫0t1∧ηkΔ|gΔ​(x¯Δ​(s),x¯Δ​(s−τ))−g​(x​(s),x​(s−τ))|p​𝑑s)\displaystyle\leq 2^{p-1}T^{\frac{p-2}{2}}\bar{c}\_{p}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|g\_{\Delta}(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))-g(x(s),x(s-\tau))|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2p−1​Tp−22​c¯p​(𝔼​∫0t1∧ηkΔ|g​(x¯Δ​(s),x¯Δ​(s−τ))−g​(x​(s),x​(s−τ))|p​𝑑s)\displaystyle\leq 2^{p-1}T^{\frac{p-2}{2}}\bar{c}\_{p}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|g(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))-g(x(s),x(s-\tau))|^{p}ds\Big) |  |

where c¯p\bar{c}\_{p} is a positive constant. By the elementary inequality and Lemma [2.3](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition3 "Lemma 2.3. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | K5\displaystyle K\_{5} | ≤22​(p−1)​Tp−22​c¯p​(𝔼​∫0t1∧ηkΔ|g​(x¯Δ​(s),x¯Δ​(s−τ))−g​(xΔ​(s),xΔ​(s−τ))|p​𝑑s)\displaystyle\leq 2^{2(p-1)}T^{\frac{p-2}{2}}\bar{c}\_{p}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|g(\bar{x}\_{\Delta}(s),\bar{x}\_{\Delta}(s-\tau))-g(x\_{\Delta}(s),x\_{\Delta}(s-\tau))|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +22​(p−1)​Tp−22​c¯p​(𝔼​∫0t1∧ηkΔ|g​(xΔ​(s),xΔ​(s−τ))−g​(x​(s),x​(s−τ))|p​𝑑s)\displaystyle+2^{2(p-1)}T^{\frac{p-2}{2}}\bar{c}\_{p}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|g(x\_{\Delta}(s),x\_{\Delta}(s-\tau))-g(x(s),x(s-\tau))|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤c1​(𝔼​∫0t1∧ηkΔ|x¯Δ​(s)−xΔ​(s)|p​𝑑s)+c1​(𝔼​∫0t1∧ηkΔ|x¯Δ​(s−τ)−xΔ​(s−τ)|p​𝑑s)\displaystyle\leq c\_{1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p}ds\Big)+c\_{1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|\bar{x}\_{\Delta}(s-\tau)-x\_{\Delta}(s-\tau)|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +c1​(𝔼​∫0t1∧ηkΔ|xΔ​(s)−x​(s)|p​𝑑s)+c1​(𝔼​∫0t1∧ηkΔ|xΔ​(s−τ)−x​(s−τ)|p​𝑑s),\displaystyle+c\_{1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|x\_{\Delta}(s)-x(s)|^{p}ds\Big)+c\_{1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|x\_{\Delta}(s-\tau)-x(s-\tau)|^{p}ds\Big), |  |

where c1=23​(p−1)​Tp−22​c¯p​Gkpc\_{1}=2^{3(p-1)}T^{\frac{p-2}{2}}\bar{c}\_{p}G^{p}\_{k}. This also means that

|  |  |  |  |
| --- | --- | --- | --- |
|  | K5\displaystyle K\_{5} | ≤c1​∫0T𝔼​|x¯Δ​(s)−xΔ​(s)|p​𝑑s+c1​∫−τ0𝔼​|ξ​([s/Δ]​Δ)−ξ​(s)|p​𝑑s\displaystyle\leq c\_{1}\int\_{0}^{T}\mathbb{E}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p}ds+c\_{1}\int\_{-\tau}^{0}\mathbb{E}|\xi([s/\Delta]\Delta)-\xi(s)|^{p}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +c1​∫0T𝔼​|x¯Δ​(s)−xΔ​(s)|p​𝑑s+c1​(𝔼​∫0t1∧ηkΔ|xΔ​(s)−x​(s)|p​𝑑s)\displaystyle+c\_{1}\int\_{0}^{T}\mathbb{E}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p}ds+c\_{1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|x\_{\Delta}(s)-x(s)|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +c1​∫−τ0𝔼​|ξ​([s/Δ]​Δ)−ξ​(s)|​𝑑s+c1​(𝔼​∫0t1∧ηkΔ|xΔ​(s)−x​(s)|p​𝑑s)\displaystyle+c\_{1}\int\_{-\tau}^{0}\mathbb{E}|\xi([s/\Delta]\Delta)-\xi(s)|ds+c\_{1}\Big(\mathbb{E}\int\_{0}^{t\_{1}\wedge\eta^{\Delta}\_{k}}|x\_{\Delta}(s)-x(s)|^{p}ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​c1​∫−τ0𝔼​|ξ​([s/Δ]​Δ)−ξ​(s)|p​𝑑s+2​c1​∫0T𝔼​|x¯Δ​(s)−xΔ​(s)|p​𝑑s\displaystyle\leq 2c\_{1}\int\_{-\tau}^{0}\mathbb{E}|\xi([s/\Delta]\Delta)-\xi(s)|^{p}ds+2c\_{1}\int\_{0}^{T}\mathbb{E}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p}ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2​c1​∫0t1𝔼​(sup0≤t≤s|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)​𝑑s.\displaystyle+2c\_{1}\int\_{0}^{t\_{1}}\mathbb{E}\Big(\sup\_{0\leq t\leq s}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)ds. |  | (33) |

By combining K4K\_{4} and K5K\_{5}, that is ([5.1](https://arxiv.org/html/2510.04092v1#S5.Ex79 "5.1 Finite-time error bound ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([5.1](https://arxiv.org/html/2510.04092v1#S5.Ex86 "5.1 Finite-time error bound ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we now have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(sup0≤t≤T|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)≤2​c1​∫−τ0𝔼​|ξ​([s/Δ]​Δ)−ξ​(s)|p​𝑑s\displaystyle\mathbb{E}\Big(\sup\_{0\leq t\leq T}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)\leq 2c\_{1}\int\_{-\tau}^{0}\mathbb{E}|\xi([s/\Delta]\Delta)-\xi(s)|^{p}ds |  |
|  |  |  |
| --- | --- | --- |
|  | +(c0+2​c1)​∫0T𝔼​|x¯Δ​(s)−xΔ​(s)|p​𝑑s+(c0+2​c1)​∫0t1𝔼​(sup0≤t≤s|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)​𝑑s.\displaystyle+(c\_{0}+2c\_{1})\int\_{0}^{T}\mathbb{E}|\bar{x}\_{\Delta}(s)-x\_{\Delta}(s)|^{p}ds+(c\_{0}+2c\_{1})\int\_{0}^{t\_{1}}\mathbb{E}\Big(\sup\_{0\leq t\leq s}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)ds. |  |

So by Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), Lemma [4.1](https://arxiv.org/html/2510.04092v1#S4.Thmdefinition1 "Lemma 4.1. ‣ 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") and the Gronwall inequality, we obtain the required assertion as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(sup0≤t≤T|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)\displaystyle\mathbb{E}\Big(\sup\_{0\leq t\leq T}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K6​(Δℓ∨Δp/2​(ψ​(Δ))p)+K7​∫0t1𝔼​(sup0≤t≤s|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p)​𝑑s\displaystyle\leq K\_{6}(\Delta^{\ell}\vee\Delta^{p/2}(\psi(\Delta))^{p})+K\_{7}\int\_{0}^{t\_{1}}\mathbb{E}\Big(\sup\_{0\leq t\leq s}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big)ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K8​(Δℓ∨Δp/2​(ψ​(Δ))p),\displaystyle\leq K\_{8}(\Delta^{\ell}\vee\Delta^{p/2}(\psi(\Delta))^{p}), |  |

where K6=2​c1​D+cp​(c0+2​c1)K\_{6}=2c\_{1}D+c\_{p}(c\_{0}+2c\_{1}), K7=c0+2​c1K\_{7}=c\_{0}+2c\_{1} and K8=K6​eK7K\_{8}=K\_{6}e^{K\_{7}}. Moreover, by Lemma [4.1](https://arxiv.org/html/2510.04092v1#S4.Thmdefinition1 "Lemma 4.1. ‣ 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we also get ([31](https://arxiv.org/html/2510.04092v1#S5.E31 "In Lemma 5.1. ‣ 5.1 Finite-time error bound ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) by letting Δ→0\Delta\rightarrow 0.
∎

### 5.2 Convergence in probability

The following theorem shows that the truncated EM solutions converge to the true solution of SDDE ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) in probability.

###### Theorem 5.2.

Let x​(t)x(t) and xΔ​(t)x\_{\Delta}(t) be the true solution and the truncated EM solution of ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([24](https://arxiv.org/html/2510.04092v1#S4.E24 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) respectively. Then for any fixed T>0T>0, Δ∈(0,Δ∗]\Delta\in(0,\Delta^{\*}] and p≥2p\geq 2, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limΔ→0(sup0≤t≤T|xΔ​(t)−x​(t)|p)=0​ in probability.\lim\_{\Delta\rightarrow 0}\Big(\sup\_{0\leq t\leq T}|x\_{\Delta}(t)-x(t)|^{p}\Big)=0\text{ in probability}. |  | (34) |

and consequently

|  |  |  |  |
| --- | --- | --- | --- |
|  | limΔ→0(sup0≤t≤T|x¯Δ​(t)−x​(t)|p)=0​ in probability,\lim\_{\Delta\rightarrow 0}\Big(\sup\_{0\leq t\leq T}|\bar{x}\_{\Delta}(t)-x(t)|^{p}\Big)=0\text{ in probability}, |  | (35) |

where x¯Δ​(t)\bar{x}\_{\Delta}(t) is defined in ([22](https://arxiv.org/html/2510.04092v1#S4.E22 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")).

###### Proof.

For arbitrarily small constants ϵ\epsilon and λ\lambda, set

|  |  |  |
| --- | --- | --- |
|  | Ω¯={ω:sup0≤t≤T|xΔ​(t)−x​(t)|p≥λ}.\bar{\Omega}=\Big\{\omega:\sup\_{0\leq t\leq T}|x\_{\Delta}(t)-x(t)|^{p}\geq\lambda\Big\}. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​ℙ​(Ω¯∩(ηkΔ≥T))\displaystyle\lambda\mathbb{P}(\bar{\Omega}\cap(\eta^{\Delta}\_{k}\geq T)) | =λ​𝔼​(1(ηkΔ≥T)​1Ω¯)\displaystyle=\lambda\mathbb{E}\Big(1\_{(\eta^{\Delta}\_{k}\geq T)}1\_{\bar{\Omega}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​(1(ηkΔ≥T)​sup0≤t≤T|xΔ​(t)−x​(t)|p)\displaystyle\leq\mathbb{E}\Big(1\_{(\eta^{\Delta}\_{k}\geq T)}\sup\_{0\leq t\leq T}|x\_{\Delta}(t)-x(t)|^{p}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​(sup0≤t≤T∧ηkΔ|xΔ​(t)−x​(t)|p)\displaystyle\leq\mathbb{E}\Big(\sup\_{0\leq t\leq T\wedge\eta^{\Delta}\_{k}}|x\_{\Delta}(t)-x(t)|^{p}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​(sup0≤t≤T|xΔ​(t∧ηkΔ)−x​(t∧ηkΔ)|p).\displaystyle\leq\mathbb{E}\Big(\sup\_{0\leq t\leq T}|x\_{\Delta}(t\wedge\eta^{\Delta}\_{k})-x(t\wedge\eta^{\Delta}\_{k})|^{p}\Big). |  |

By Lemma [5.1](https://arxiv.org/html/2510.04092v1#S5.Thmdefinition1 "Lemma 5.1. ‣ 5.1 Finite-time error bound ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Ω¯∩(ηkΔ≥T))≤K8​(Δℓ∨Δp/2​(ψ​(Δ))p)λ.\displaystyle\mathbb{P}(\bar{\Omega}\cap(\eta^{\Delta}\_{k}\geq T))\leq\frac{K\_{8}(\Delta^{\ell}\vee\Delta^{p/2}(\psi(\Delta))^{p})}{\lambda}. |  | (36) |

Furthermore, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Ω¯)\displaystyle\mathbb{P}(\bar{\Omega}) | ≤ℙ​(Ω¯∩(ηkΔ≥T))+ℙ​(ηkΔ≤T)\displaystyle\leq\mathbb{P}(\bar{\Omega}\cap(\eta^{\Delta}\_{k}\geq T))+\mathbb{P}(\eta^{\Delta}\_{k}\leq T) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤ℙ​(Ω¯∩(ηkΔ≥T))+ℙ​(ηk≤T)+ℙ​(ηΔ≤T).\displaystyle\leq\mathbb{P}(\bar{\Omega}\cap(\eta^{\Delta}\_{k}\geq T))+\mathbb{P}(\eta\_{k}\leq T)+\mathbb{P}(\eta\_{\Delta}\leq T). |  | (37) |

So, by substituting ([17](https://arxiv.org/html/2510.04092v1#S3.E17 "In 3.1 Existence of positive solution ‣ 3 Properties of true solution ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), ([27](https://arxiv.org/html/2510.04092v1#S4.E27 "In Lemma 4.2. ‣ 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([36](https://arxiv.org/html/2510.04092v1#S5.E36 "In 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) into ([5.2](https://arxiv.org/html/2510.04092v1#S5.Ex100 "5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Ω¯)\displaystyle\mathbb{P}(\bar{\Omega}) | ≤V​(ξ​(0))+K0​TV​(k)∧V​(1/k)+K8​(Δℓ∨Δp/2​(ψ​(Δ))p)λ\displaystyle\leq\frac{V(\xi(0))+K\_{0}T}{V(k)\wedge V(1/k)}+\frac{K\_{8}(\Delta^{\ell}\vee\Delta^{p/2}(\psi(\Delta))^{p})}{\lambda} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +V​(ξ​(0))+K1​T+K3​D​Δℓ+cp​(K2+K3)​Δ1/2​ψ​(Δ)​TV​(1/k)∧V​(k).\displaystyle+\frac{V(\xi(0))+K\_{1}T+K\_{3}D\Delta^{\ell}+c\_{p}(K\_{2}+K\_{3})\Delta^{1/2}\psi(\Delta)T}{V(1/k)\wedge V(k)}. |  | (38) |

Therefore, we can select kk sufficiently large such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​V​(ξ​(0))+K0​T+K1​TV​(k)∧V​(1/k)<ϵ2\frac{2V(\xi(0))+K\_{0}T+K\_{1}T}{V(k)\wedge V(1/k)}<\frac{\epsilon}{2} |  | (39) |

and select Δ\Delta so small such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | K3​D​Δℓ+cp​(K2+K3)​Δ1/2​ψ​(Δ)​TV​(1/k)∧V​(k)+K8​(Δℓ∨Δp/2​(ψ​(Δ))p)λ<ϵ2.\displaystyle\frac{K\_{3}D\Delta^{\ell}+c\_{p}(K\_{2}+K\_{3})\Delta^{1/2}\psi(\Delta)T}{V(1/k)\wedge V(k)}+\frac{K\_{8}(\Delta^{\ell}\vee\Delta^{p/2}(\psi(\Delta))^{p})}{\lambda}<\frac{\epsilon}{2}. |  | (40) |

So by combining ([39](https://arxiv.org/html/2510.04092v1#S5.E39 "In 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([40](https://arxiv.org/html/2510.04092v1#S5.E40 "In 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")), we now have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(sup0≤t≤T|xΔ​(t)−x​(t)|p≥λ)<ϵ,\mathbb{P}\Big(\sup\_{0\leq t\leq T}|x\_{\Delta}(t)-x(t)|^{p}\geq\lambda\Big)<\epsilon, |  | (41) |

as desired. However, by Lemma [4.1](https://arxiv.org/html/2510.04092v1#S4.Thmdefinition1 "Lemma 4.1. ‣ 4.2 Properties of numerical solution ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we also obtain ([35](https://arxiv.org/html/2510.04092v1#S5.E35 "In Theorem 5.2. ‣ 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) by setting Δ→0\Delta\rightarrow 0.
∎

### 5.3 Numerical simulation

In this illustrative simulation example, we compare the performance of the truncated EM method (TEM) constructed for SDDE ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) with the backward EM method (BEM). We should clarify that, to the best of our knowledge, there exist no relevant literature for the numerical treatment of SDDE ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) based on the backward EM method. This illustration is just for the purpose of comparison. For the sake of simplicity, let us consider the following form of SDDE ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=4​(2−x​(t)2)​d​t+0.5​x​(t−2)2/3​x​(t)3/5​d​B​(t),dx(t)=4(2-x(t)^{2})dt+0.5x(t-2)^{2/3}x(t)^{3/5}dB(t), |  | (42) |

with the initial data ξ​(0)=0.2\xi(0)=0.2, where τ=2\tau=2, γ=2\gamma=2, r=2/3r=2/3 and θ=3/5\theta=3/5. Clearly, we see that Assumption [2.1](https://arxiv.org/html/2510.04092v1#S2.Thmdefinition1 "Assumption 2.1. ‣ 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") is satisfied. Moreover, we note that

|  |  |  |
| --- | --- | --- |
|  | sup|x|∨|y|≤u(|f​(x)|∨g​(x,y))≤6.5​u2\sup\_{|x|\vee|y|\leq u}\Big(|f(x)|\vee g(x,y)\Big)\leq 6.5u^{2} |  |

for all u≥1u\geq 1. This means that we have z​(u)=6.5​u2z(u)=6.5u^{2} with inverse z−1​(u)=(u/6.5)1/2z^{-1}(u)=(u/6.5)^{1/2}. If we choose ψ​(Δ)=Δ−2/3\psi(\Delta)=\Delta^{-2/3}, then z−1​(ψ​(Δ))=(Δ−2/3/6.5)1/2z^{-1}(\psi(\Delta))=(\Delta^{-2/3}/6.5)^{1/2}. Table [1](https://arxiv.org/html/2510.04092v1#S5.T1 "Table 1 ‣ 5.3 Numerical simulation ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") and Figure [1](https://arxiv.org/html/2510.04092v1#S5.F1 "Figure 1 ‣ 5.3 Numerical simulation ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") show empirical distributions of the TEM and BEM solutions using Δ=10−2\Delta=10^{-2}. The plot of convergence of the TEM and BEM solutions is depicted in Figure [2](https://arxiv.org/html/2510.04092v1#S5.F2 "Figure 2 ‣ 5.3 Numerical simulation ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model") using the same step size. From the plots, we see that the solution paths of both methods are almost the same. By using the step sizes 10−210^{-2}, 10−310^{-3}, 10−410^{-4} and 10−510^{-5}, we have the errors between the TEM and BEM solutions with a reference line of order 1 in Figure [3](https://arxiv.org/html/2510.04092v1#S5.F3 "Figure 3 ‣ 5.3 Numerical simulation ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model").

| Numerical method | min | mean | sd | kurt | skew | max |
| --- | --- | --- | --- | --- | --- | --- |
| TEM | 0.0000 | 1.3720 | 0.1880 | 14.5202 | -1.7707 | 1.9380 |
| BEM | 0.0000 | 1.3720 | 0.1825 | 12.9464 | -2.0372 | 1.9010 |

Table 1: Empirical distribution of the TEM and BEM solutions



![Refer to caption](box.png)

Figure 1: Plot of the empirical distribution of the TEM and BEM solutions



![Refer to caption](converge.png)

Figure 2: Convergence of the TEM and BEM solutions



![Refer to caption](error.png)

Figure 3: Errors between the TEM and BEM solutions

### 5.4 Financial application

We justify the convergence result for valuation of a bond and a lookback put option via efficient use of the Monte Carlo method.

###### Lemma 5.3.

Let x​(t)x(t) and x¯Δ​(t)\bar{x}\_{\Delta}(t) be the true solution and the truncated EM step solution of ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([24](https://arxiv.org/html/2510.04092v1#S4.E24 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) respectively. If a bond price B​(T)B(T) at maturity time TT is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(T)=𝔼​[exp⁡(−∫0Tx​(t)​𝑑t)],B(T)=\mathbb{E}\Big[\exp\Big(-\int\_{0}^{T}x(t)dt\Big)\Big], |  | (43) |

then an approximation of B​(T)B(T) is computed by

|  |  |  |
| --- | --- | --- |
|  | BΔ​(T)=𝔼​[exp⁡(−∫0Tx¯Δ​(t)​𝑑t)].B\_{\Delta}(T)=\mathbb{E}\Big[\exp\Big(-\int\_{0}^{T}\bar{x}\_{\Delta}(t)dt\Big)\Big]. |  |

So, by the Theorem [5.2](https://arxiv.org/html/2510.04092v1#S5.Thmdefinition2 "Theorem 5.2. ‣ 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we get

|  |  |  |
| --- | --- | --- |
|  | limΔ→0|BΔ​(T)−B​(T)|=0.\lim\_{\Delta\rightarrow 0}|B\_{\Delta}(T)-B(T)|=0. |  |

###### Proof.

Let ϵ,δ∈(0,1)\epsilon,\delta\in(0,1) be arbitrarily small. It is sufficient to prove that

|  |  |  |
| --- | --- | --- |
|  | ℙ​[|exp⁡(−∫0Tx​(t)​𝑑t)−exp⁡(−∫0Tx¯Δ​(t)​𝑑t)|≥δ]<ϵ.\displaystyle\mathbb{P}\Big[\Big|\exp\Big(-\int\_{0}^{T}x(t)dt\Big)-\exp\Big(-\int\_{0}^{T}\bar{x}\_{\Delta}(t)dt\Big)\Big|\geq\delta\Big]<\epsilon. |  |

Using the inequality exp⁡(−|x|)−exp⁡(−|y|)≤|x−y|\exp(-|x|)-\exp(-|y|)\leq|x-y|, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |exp⁡(−∫0Tx​(t)​𝑑t)−exp⁡(−∫0Tx¯Δ​(t)​𝑑t)|\displaystyle\Big|\exp\Big(-\int\_{0}^{T}x(t)dt\Big)-\exp\Big(-\int\_{0}^{T}\bar{x}\_{\Delta}(t)dt\Big)\Big| | ≤|∫0T[x​(t)−x¯Δ​(t)]​𝑑t|\displaystyle\leq\Big|\int\_{0}^{T}[x(t)-\bar{x}\_{\Delta}(t)]dt\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T​sup0≤t≤T|x​(t)−x¯Δ​(t)|.\displaystyle\leq T\sup\_{0\leq t\leq T}|x(t)-\bar{x}\_{\Delta}(t)|. |  |

By applying Theorem [5.2](https://arxiv.org/html/2510.04092v1#S5.Thmdefinition2 "Theorem 5.2. ‣ 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we obtain the desired assertion.
∎

###### Lemma 5.4.

Let x​(t)x(t) and x¯Δ​(t)\bar{x}\_{\Delta}(t) be the true solution and the truncated EM step solution of ([7](https://arxiv.org/html/2510.04092v1#S2.E7 "In 2 Mathematical preliminaries ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([24](https://arxiv.org/html/2510.04092v1#S4.E24 "In 4.1 The truncated EM method ‣ 4 Numerical method ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) respectively. If the expected payoff of the fixed strike lookback put option with strike KK is defined by

|  |  |  |
| --- | --- | --- |
|  | P=𝔼​[(K−inf0≤t≤T​x​(t))+],P=\mathbb{E}\big[(K-\underset{0\leq t\leq T}{\inf}x(t))^{+}\big], |  |

then the approximate expected payoff based on x¯Δ​(t)\bar{x}\_{\Delta}(t) is

|  |  |  |
| --- | --- | --- |
|  | PΔ=𝔼​[(K−inf0≤t≤T​x¯Δ​(t))+].P\_{\Delta}=\mathbb{E}\big[(K-\underset{0\leq t\leq T}{\inf}\bar{x}\_{\Delta}(t))^{+}\big]. |  |

So, by the Theorem [5.2](https://arxiv.org/html/2510.04092v1#S5.Thmdefinition2 "Theorem 5.2. ‣ 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we have

|  |  |  |
| --- | --- | --- |
|  | limΔ→0​|P−PΔ|=0.\underset{\Delta\rightarrow 0}{\lim}|P-P\_{\Delta}|=0. |  |

###### Proof.

In other words, we need to prove that

|  |  |  |
| --- | --- | --- |
|  | limΔ→0|(K−inf0≤t≤Tx​(t))+−(K−inf0≤t≤T|x¯Δ​(t)|)+|=0in probability.\displaystyle\lim\_{\Delta\rightarrow 0}|(K-\inf\_{0\leq t\leq T}x(t))^{+}-(K-\inf\_{0\leq t\leq T}|\bar{x}\_{\Delta}(t)|)^{+}|=0\quad\text{in probability}. |  |

This also means that the theorem holds as long as we can establish that for any small constants ϵ>0\epsilon>0 and δ∈(0,1)\delta\in(0,1)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|(K−inf0≤t≤Tx​(t))+−(K−inf0≤t≤T|x¯Δ​(t)|)+|≥δ)<ϵ\displaystyle\mathbb{P}(|(K-\inf\_{0\leq t\leq T}x(t))^{+}-(K-\inf\_{0\leq t\leq T}|\bar{x}\_{\Delta}(t)|)^{+}|\geq\delta)<\epsilon |  | (44) |

holds for all sufficiently small Δ\Delta. We observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |(K−inf0≤t≤Tx​(t))+−(K−inf0≤t≤T|x¯Δ​(t)|)+|\displaystyle|(K-\inf\_{0\leq t\leq T}x(t))^{+}-(K-\inf\_{0\leq t\leq T}|\bar{x}\_{\Delta}(t)|)^{+}| | ≤|inf0≤t≤Tx​(t)−inf0≤t≤T|x¯Δ​(t)||\displaystyle\leq|\inf\_{0\leq t\leq T}x(t)-\inf\_{0\leq t\leq T}|\bar{x}\_{\Delta}(t)|| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤sup0≤t≤T|x​(t)−|x¯Δ​(t)||\displaystyle\leq\sup\_{0\leq t\leq T}|x(t)-|\bar{x}\_{\Delta}(t)|| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤sup0≤t≤T|x​(t)−x¯Δ​(t)|.\displaystyle\leq\sup\_{0\leq t\leq T}|x(t)-\bar{x}\_{\Delta}(t)|. |  | (45) |

Then, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|(K−inf0≤t≤Tx​(t))+−(K−inf0≤t≤T|x¯Δ​(t)|)+|≥δ)≤ℙ​(sup0≤t≤T|x​(t)−x¯Δ​(t)|≥δ).\displaystyle\mathbb{P}(|(K-\inf\_{0\leq t\leq T}x(t))^{+}-(K-\inf\_{0\leq t\leq T}|\bar{x}\_{\Delta}(t)|)^{+}|\geq\delta)\leq\mathbb{P}(\sup\_{0\leq t\leq T}|x(t)-\bar{x}\_{\Delta}(t)|\geq\delta). |  | (46) |

So, by Theorem [5.2](https://arxiv.org/html/2510.04092v1#S5.Thmdefinition2 "Theorem 5.2. ‣ 5.2 Convergence in probability ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model"), we now have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(sup0≤t≤T|x​(t)−x¯Δ​(t)|≥δ)<ϵ\displaystyle\mathbb{P}(\sup\_{0\leq t\leq T}|x(t)-\bar{x}\_{\Delta}(t)|\geq\delta)<\epsilon |  | (47) |

for all sufficiently small Δ\Delta. So by combining ([46](https://arxiv.org/html/2510.04092v1#S5.E46 "In 5.4 Financial application ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) and ([47](https://arxiv.org/html/2510.04092v1#S5.E47 "In 5.4 Financial application ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")) gives us ([44](https://arxiv.org/html/2510.04092v1#S5.E44 "In 5.4 Financial application ‣ 5 Convergence analysis ‣ Convergence in probability of numerical solutions of a highly non-linear delayed stochastic interest rate model")).
∎

## Acknowledgement

The author would like to acknowledge the financial support from the Heilbronn Institute for Mathematical Research (HIMR) and the UKRI/EPSRC Additional Funding Programme for Mathematical Sciences.

## Declarations

Conflict of interest: The author declares that he has no conflict of interest.

## References

* [1]

  Arriojas, M., Hu, Y., Mohammed, S.E. and Pap, G.: A delayed Black and Scholes formula. Stochastic Analysis and Applications, 25(2), pp.471-492 (2007).
* [2]

  Baduraliya, C.H. and Mao, X.: The Euler–Maruyama approximation for the asset price in the mean-reverting-theta stochastic volatility model. Computers & Mathematics with Applications, 64(7), pp.2209-2223 (2012)
* [3]

  Chan, K.C., Karolyi, G.A., Longstaff, F.A. and Sanders, A.B.: An empirical comparison of alternative models of the short-term interest rate. The Journal of Finance, 47(3), pp.1209-1227 (1992)
* [4]

  Coffie, E. and Mao, X.: Truncated EM numerical method for generalised Ait-Sahalia-type interest rate model with delay. Journal of Computational and Applied Mathematics, 383 (2021)
* [5]

  Cox, J.C., Ingersoll Jr, J.E. and Ross, S.A.: A theory of the term structure of interest rates. In Theory of valuation, pp. 129-164 (2005)
* [6]

  Gatheral, J.: The volatility surface: a practitioner’s guide. John Wiley & Sons (2011)
* [7]

  Heston, S.L.: A closed-form solution for options with stochastic volatility with applications to bond and currency options. The Review of Financial Studies, 6(2), pp.327-343 (1993)
* [8]

  Hutzenthaler, M., Jentzen, A. and Kloeden, P.E.: Strong and weak divergence in finite time of Euler’s method for stochastic differential equations with non-globally Lipschitz continuous coefficients. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 467(2130), pp.1563-1576 (2011)
* [9]

  Kind, P., Liptser, R.S. and Runggaldier, W.J.: Diffusion approximation in past dependent models and applications to option pricing. The Annals of Applied Probability, pp.379-405 (1991)
* [10]

  Mao, X.: Stochastic differential equations and applications. Elsevier (2007)
* [11]

  Mao, X.: The truncated Euler–Maruyama method for stochastic differential equations. Journal of Computational and Applied Mathematics, 290, pp.370-384 (2015)
* [12]

  Mao, X. and Rassias, M.J.: Khasminskii-type theorems for stochastic differential delay equations. Stochastic Analysis and Applications, 23(5), pp.1045-1069 (2005)
* [13]

  Mao, X. and Sabanis, S.: Delay geometric Brownian motion in financial option valuation. International Journal of Probability and Stochastic Processes, 85(2), pp.295-320 , (2013)
* [14]

  Nowman, K.B.: Gaussian estimation of single-factor continuous time models of the term structure of interest rates. The Journal of Finance, 52(4), pp.1695-1706 (1997)
* [15]

  Wu, F., Mao, X. and Chen, K.: A highly sensitive mean-reverting process in finance and the Euler–Maruyama approximations. Journal of Mathematical Analysis and Applications, 348(1), pp.540-554 (2008)
* [16]

  Wu, F., Mao, X. and Chen, K.: The Cox–Ingersoll–Ross model with delay and strong convergence of its Euler–Maruyama approximate solutions. Applied Numerical Mathematics, 59(10), pp.2641-2658 (2009)