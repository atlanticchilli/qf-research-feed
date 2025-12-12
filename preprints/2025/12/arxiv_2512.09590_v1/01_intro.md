---
authors:
- Emmanuel Gnabeyeu
- Gilles Pagès
- Mathieu Rosenbaum
doc_id: arxiv:2512.09590v1
family_id: arxiv:2512.09590
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'On Inhomogeneous Affine Volterra Processes: Stationarity and Applications
  to the Volterra Heston Model.'
url_abs: http://arxiv.org/abs/2512.09590v1
url_html: https://arxiv.org/html/2512.09590v1
venue: arXiv q-fin
version: 1
year: 2025
---


Emmanuel Gnabeyeu
  
LPSM


 Sorbonne Université and Université Paris Cité


 Paris


 France.
  
E-mail: emmanuel.gnabeyeu\_mbiada@sorbonne-universite.fr


Gilles Pagès
  
LPSM


 Sorbonne Université


 case 158


 4


 pl. Jussieu


 F-75252 Paris Cedex 5


 France.
  
E-mail: gilles.pages@sorbonne-universite.fr


Mathieu Rosenbaum
  
CMAP


 École Polytechnique


 Paris


 France.
  
E-mail: mathieu.rosenbaum@polytechnique.edu

(November 1, 2025)

###### Abstract

True Volterra equations are inherently non stationary and therefore do not admit genuine stationary regimes over finite horizons. This motivates the
study of the finite-time behavior of the solutions to scaled inhomogeneous affine Stochastic Volterra equations through the lens of
a weaker notion of stationarity referred to as fake stationary regime in the sense that all marginal
distributions share the same expectation and variance.
As a first application, we introduce the Fake stationary Volterra Heston model and derive a closed-form expression for its characteristic function.
Having established this finite-time proxy for stationarity, we then investigate the asymptotic (long-time) behavior to assess whether genuine stationary regimes emerge in the limit.
Using an extension of the exponential-affine transformation formula for those processes, we establish in the long run the existence of limiting distributions, which (unlike in the case of classical affine diffusion processes) may depend on the initial state of the process, unless the Volterra kernel coincides with the α\alpha-fractional integration kernel, for which the dependence on the initial state vanishes.
We then proceed to the construction of stationary processes associated with these limiting distributions. However, the dynamics in this long-term regime are analytically intractable, and the process itself is not guaranteed to be stationary in the classical sense over finite horizons.
This highlights the relevance of finite-time analysis through the lens of the aforementioned fake stationarity, which offers a tractable approximation to stationary behavior in genuinely non-stationary Volterra systems.

Keywords: Affine Volterra Processes, Stochastic Differential Equations, Fractional Calculus, Functional Integral Equation, Fourier-Laplace Transforms, Dini Theorem, Limit Theorems.

Mathematics Subject Classification (2020):  45D05, 60G10, 60H10,60G22, 91B24, 91B70, 91G80

## 1 Introduction

### 1.1 Literature review

We consider the class of inhomogeneous affine Volterra stochastic integral equations which naturally arises in the modeling of systems with memory, (including) in mathematical finance, physics, and biology:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Xt=X0​ϕ​(t)+∫0tK​(t,s)​b​(s,Xs)​𝑑s+∫0tK​(t,s)​σ​(s,Xs)​𝑑Ws,X0:(Ω,ℱ,ℙ)→(ℝ,ℬ(ℝ))X0⟂⟂W.\begin{cases}X\_{t}=X\_{0}\phi(t)+\int\_{0}^{t}K(t,s)b(s,X\_{s})\,ds+\int\_{0}^{t}K(t,s)\sigma(s,X\_{s})\,dW\_{s},\\ X\_{0}:(\Omega,\mathcal{F},\mathbb{P})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))\quad X\_{0}\perp\!\!\!\perp W.\end{cases} |  | (1.1) |

where ϕ\phi is a deterministic continuous function, K​(t,s)K(t,s) a deterministic kernel modeling the memory or hereditary structure of the system and the process (Wt)t≥0(W\_{t})\_{t\geq 0}, an ℝ\mathbb{R}-valued Brownian motion independent of X0X\_{0}, both defined on a probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) with ℱt⊃ℱt,X0,W\mathcal{F}\_{t}\supset\mathcal{F}\_{t,X\_{0},W} a filtration satisfying the usual conditions. The drift bb and the diffusion coefficient σ\sigma
are time inhomogeneous and affine in the state variable in the sense that the functions bb and a:=σ​σ⊤a:=\sigma\sigma^{\top} belong to Pol1​(ℝ)\mathrm{Pol}\_{1}(\mathbb{R}), where Poln​(ℝ)\mathrm{Pol}\_{n}(\mathbb{R}) denote the subspace of the ring Pol​(ℝ)\mathrm{Pol}(\mathbb{R}) of all polynomials on ℝ\mathbb{R}, consisting of polynomials of degree at most nn.

Special cases of affine processes have long been instrumental in various domains of stochastic analysis, particularly in mathematical finance and biological modeling. Seminal contributions include the foundational works of [[17](https://arxiv.org/html/2512.09590v1#bib.bib17)], [[33](https://arxiv.org/html/2512.09590v1#bib.bib33)], and [[8](https://arxiv.org/html/2512.09590v1#bib.bib8)]. The theoretical framework of affine processes was further advanced through significant milestones achieved by [[12](https://arxiv.org/html/2512.09590v1#bib.bib12)], as well as [[20](https://arxiv.org/html/2512.09590v1#bib.bib20)].

More recently, the study of affine processes within the context of Volterra equations has attracted considerable attention [[31](https://arxiv.org/html/2512.09590v1#bib.bib31), [13](https://arxiv.org/html/2512.09590v1#bib.bib13), [2](https://arxiv.org/html/2512.09590v1#bib.bib2), [3](https://arxiv.org/html/2512.09590v1#bib.bib3)]. In this setting, the dynamics depend not only on the current time ss but also on the terminal time tt via the kernel KK appearing in equation ([1.1](https://arxiv.org/html/2512.09590v1#S1.E1 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). This dependence introduces memory effects, thereby violating the Markov property. The aim is to mimic the behavior of affine stochastic differential equations (SDEs) driven by fractional Brownian motion (W⋅HW^{H}\_{\cdot}), while avoiding the technical challenges associated with their analysis, particularly those arising from “high-order” rough path theory or regularity structures, which become especially intricate as the Hurst parameter HH playing a crucial role in the path’s regularity, approaches zero. This type of dynamics has gained significant attraction in the financial community over the past decade, particularly because it enables consistent modeling of financial markets across multiple time scales from order book dynamics to the pricing of derivative products despite its non-Markovian nature.
The idea of introducing a fractional Brownian motion in the volatility noise is not new. To the best of our knowledge, it dates back to [[10](https://arxiv.org/html/2512.09590v1#bib.bib10), [11](https://arxiv.org/html/2512.09590v1#bib.bib11)], where the authors extended classical models to incorporate long-memory effects with a Hurst index HH greater than 0.50.5. This extension aimed to capture the empirically observed persistence in the stochastic behavior of Black–Scholes implied volatilities as time to maturity increases. More recently, the roughness phenomenon in the behavior of high-frequency volatility data has come under the spotlight. Empirical studies suggest that the log-volatility is well modeled by a fractional Brownian motion with a Hurst parameter less than 0.50.5; see for instance,
[[21](https://arxiv.org/html/2512.09590v1#bib.bib21)] where the fractional versions of affine models
are able to reproduce the slope of short-term skew observed in option markets.

In this work, we consider the class of convolutive kernels, i.e. kernels K:{(s,t)∈ℝ+2:0≤s<t}→ℝ+K:\{(s,t)\!\in\mathbb{R}\_{+}^{2}:0\leq s<t\}\to\mathbb{R}\_{+} satisfying ∀s,t≥0,s<t,K​(s,t)=K​(0,t−s)\forall\,s,\,t\geq 0,\;s<t,\quad K(s,t)=K(0,t-s) and we are chiefly interested in inhomogeneous stochastic Volterra equations of convolution type of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0ϕ(t)+∫0tK(t−s)(θ(s)−λXs)ds+∫0tK(t−s)ς(s)κ0+κ1​XsdWs,X0⟂⟂W,X\_{t}=X\_{0}\phi(t)+\int\_{0}^{t}K(t-s)(\theta(s)-\lambda X\_{s})ds+\int\_{0}^{t}K(t-s)\varsigma(s)\sqrt{\kappa\_{0}+\kappa\_{1}X\_{s}}\,dW\_{s},\quad X\_{0}\perp\!\!\!\perp W, |  | (1.2) |

which provides the most general example of a continuous-time inhomogeneous affine Volterra process on ℝ+\mathbb{R}\_{+} with ς\varsigma a deterministic borel (locally) bounded function.
Our aim is to investigate their stationarity over a finite horizon, analyze their limiting distributions, and construct the associated stationary process when applicable.
Building upon results developed in [[30](https://arxiv.org/html/2512.09590v1#bib.bib30), [13](https://arxiv.org/html/2512.09590v1#bib.bib13)], the recent and insightful contribution of [[24](https://arxiv.org/html/2512.09590v1#bib.bib24)] establishes that equation ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) when κ0=0\kappa\_{0}=0 admits at least a weak positive solution, as the joint time-and-space scaling limit of the intensity process of a nearly unstable Hawkes process. More generally, building on the approach in [[1](https://arxiv.org/html/2512.09590v1#bib.bib1)], which introduced a local martingale problem for convolutional-type SVEs to extend the theory of weak solutions from ODEs to SVEs, [[37](https://arxiv.org/html/2512.09590v1#bib.bib37)] establishes a generalized local martingale problem for stochastic Volterra equations and shows that its solvability is equivalent to the existence of a weak solution, thereby proving weak existence results for SVEs with time-inhomogeneous coefficients. This weak solution X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} is defined on some stochastic basis (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) supporting a one-dimensional Brownian motion (Wt)t≥0(W\_{t})\_{t\geq 0}. Moreover, XX admits a modification with well-defined Hölder continuous sample paths and satisfies
supt∈[0,T]𝔼​[|Xt|p]<∞\sup\_{t\in[0,T]}\mathbb{E}[|X\_{t}|^{p}]<\infty
for each p≥0p\geq 0 and T>0T>0.

### 1.2 Our contribution

First, using the measure-extended affine transformation formula allowing for explicit control over the finite-dimensional distributions of the process, we establish the existence of limiting distributions, which are shown to correspond to stationary processes.
Furthermore, we provide a complete characterization of all such limiting distributions, which (unlike in the case of classical affine diffusion processes) may depend on the initial state of the process, unless the Volterra kernel is the α\alpha-fractional integration kernel or the initial condition goes to 0 at infinity, and we show that each one gives rise to a stationary process. For these stationary processes, we explicitly derive the characteristic function of their finite-dimensional distributions.
However, we do not provide information on the dynamics of the limiting processes. This remain an open question as well as the uniqueness and the characterization of the dynamics of the corresponding stationary processes. It is for this reason that we develop the notion of fake stationarity regimes in the sense of [[35](https://arxiv.org/html/2512.09590v1#bib.bib35)] 111In this framework, the solution of the SVIE only has constant mean and variance at every time t under appropriate functional equation satisfied by the stabilizer, which offer a tractable alternative framework to study short and long-term behaviors in settings where classical stationarity is either unavailable or analytically intractable.
A “fake stationarity regime” for affine SVIEs, insofar as it exists, will ipso facto lead to a tractable weak stationarity theory in the finite horizon and at least to the classical weak L2L^{2}-stationarity based on the covariance structure in the long run.
We next introduce and analyse the characteristic function of the fake stationary Volterra Heston model, a natural extension of the rough Heston model by [[16](https://arxiv.org/html/2512.09590v1#bib.bib16), [15](https://arxiv.org/html/2512.09590v1#bib.bib15)] widely used in mathematical finance. That new model, emerges
as the continuous-time limit of a suitably rescaled non-Markovian Linear Hawkes model for high frequency assets prices, as proposed in the influential work [[24](https://arxiv.org/html/2512.09590v1#bib.bib24)]. In this setting, the time-modulated function ς\varsigma appearing in the diffusion coefficient solves a functional equation that ensures the process has constant mean and variance over time. What is more, the characteristic function of the asset price admits a semi-closed-form representation associated with the solution of a fractional Riccati ordinary differential equation (quadratic ODE) whose efficient numerical computation in the spirit of [[7](https://arxiv.org/html/2512.09590v1#bib.bib7)] can be performed, so that the fake stationary rough Heston model turns out to be highly
tractable insofar option pricing as well as volatility fitting can be carried out efficiently via Fourier methods.
A key advantage of this fake stationary formulation is that it overcomes a known drawback of classical [[25](https://arxiv.org/html/2512.09590v1#bib.bib25)] or rough Heston [[16](https://arxiv.org/html/2512.09590v1#bib.bib16)] models driven by mean-reverting classical or Volterra-CIR dynamics, which typically exhibit two distinct regimes: a short-maturity regime, where the initial condition (deterministic value at the origin, often the long run mean) is prominent and the variance remains very small, and a long-term regime, which may correspond to the stationary distribution of the process.
By construction, the fake stationary model offers a unified and consistent framework for capturing both short- and long-maturity behaviors, improving robust fitting across the entire term structure.

### 1.3 Structure of the paper and Notations

Organization of the Work.
This work is organized as follows.
In Section [2](https://arxiv.org/html/2512.09590v1#S2 "2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we present the main assumptions and collect some preliminaries needed for the study of affine Volterra integral equations, including the Fourier-Laplace transforms, the so-called resolvent of the convolutive kernel and the forward process.
In Section [3](https://arxiv.org/html/2512.09590v1#S3 "3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we establish that the conditional Laplace functional of time-inhomogeneous Volterra integral equations can
be represented via an exponential-affine form by a solution of an inhomogeneous Riccati-Volterra integral equation. We further analyze this equation and establish regularity results for its solution.
Section [4](https://arxiv.org/html/2512.09590v1#S4 "4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") is devoted to establishing weaker notions of stationarity for these equations in finite time; we show that, under appropriate functional equations satisfied by a stabilizing function, all marginal distributions share the same mean and variance. We then introduce the Fake stationary Volterra Heston model, a natural extension of the rough Heston model introduced by [[16](https://arxiv.org/html/2512.09590v1#bib.bib16)], studied in [[15](https://arxiv.org/html/2512.09590v1#bib.bib15), [2](https://arxiv.org/html/2512.09590v1#bib.bib2)], and widely used in mathematical finance. We also provide its characteristic function, namely its Fourier-Laplace exponential-affine representation.
Building on the Laplace transform representation developed in section [3](https://arxiv.org/html/2512.09590v1#S3 "3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), Section [5](https://arxiv.org/html/2512.09590v1#S5 "5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") establishes the weak convergence of the law of XtX\_{t} towards a limiting distribution πx¯0\pi\_{\bar{x}\_{0}} as t→∞t\to\infty. We also construct the stationary process and characterize when the limit πx¯0\pi\_{\bar{x}\_{0}} actually depends on the initial condition or distribution. We then analyse the functional long-run asymptotics in the fake stationarity regime.
Finally, in Section [6](https://arxiv.org/html/2512.09590v1#S6 "6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we provide a broad class of applications, including a numerical display of the finite-time fake stationary fractional CIR process, the volatility smiles in the Fake stationary rough Heston model and the long-run finite-dimensional distribution of the fake stationary exponential-fractional CIR process.

Notations.

∙\bullet Denote 𝕋=[0,T]⊂ℝ+\mathbb{T}=[0,T]\subset\mathbb{R}\_{+}, Lebd{\rm Leb}\_{d} the Lebesgue measure on (ℝd,ℬ​o​r​(ℝd))(\mathbb{R}^{d},{\cal B}or(\mathbb{R}^{d})), ℍ:=ℝd,\mathbb{H}:=\mathbb{R}^{d}, etc.

∙\bullet 𝕏:=𝒞​([0,T],ℍ)​(resp.𝒞0​([0,T],ℍ))\mathbb{X}:={\cal C}([0,T],\mathbb{H})(\text{resp.}\quad{\mathcal{C}\_{0}}([0,T],\mathbb{H})) denotes the set of continuous functions(resp. null at 0) from [0,T][0,T] to ℍ\mathbb{H} and ℬ​o​r​(𝒞d){\cal B}or({\cal C}\_{d}) denotes the Borel σ\sigma-field of 𝒞d{\cal C}\_{d} induces by the sup\sup-norm topology.

∙\bullet For p∈(0,+∞)p\in(0,+\infty), Lℍp​(ℙ)L\_{\mathbb{H}}^{p}(\mathbb{P}) or simply Lp​(ℙ)L^{p}(\mathbb{P}) denote the set of ℍ\mathbb{H}-valued random vectors XX defined on a probability space (Ω,𝒜,ℙ)(\Omega,{\cal A},\mathbb{P}) such that ‖X‖p:=(𝔼​[‖X‖ℍp])1/p<+∞\|X\|\_{p}:=(\mathbb{E}[\|X\|\_{\mathbb{H}}^{p}])^{1/p}<+\infty.

∙\bullet Let ℳ\mathcal{M} denote the space of all (ℝ+,ℬ​o​r​(ℝ))(\mathbb{R}\_{+},{\cal B}or(\mathbb{R}))-measurable functions μ\mu on ℝ+\mathbb{R}\_{+} such that the restriction μ|[0,T]\mu|\_{[0,T]}, for any T>0T>0, is a ℝ\mathbb{R}-valued finite measure (i.e. the restriction μ|[0,T]\mu|\_{[0,T]} with T>0T>0 is well-defined). For μ∈ℳ\mu\in\mathcal{M} and a compact set E⊂ℝ+E\subset\mathbb{R}\_{+}, we define the total variation of μ\mu on EE by:

|μ|(E):=sup{∑j=1N|μ(Ej)|:{Ej}j=1N is a finite measurable partition of E}.|\mu|(E):=\sup\left\{\sum\_{j=1}^{N}|\mu(E\_{j})|:\{E\_{j}\}\_{j=1}^{N}\text{ is a finite measurable partition of }E\right\}.

∙\bullet For f,g∈ℒℝ+,l​o​c1​(ℝ+,Leb1)f,g\!\in{\cal L}\_{\mathbb{R}\_{+},loc}^{1}(\mathbb{R}\_{+},{\rm Leb}\_{1}), we define their convolution by (f∗g)t=(f∗g)​(t)=∫0tf​(t−s)​g​(s)​𝑑s(f\*g)\_{t}=(f\*g)(t)=\int\_{0}^{t}f(t-s)g(s)ds, t≥0t\geq 0. We will frequently use Young’s convolution inequality
which states that for any T>0T>0, f∈Lp​([0,T])f\in L^{p}([0,T]), g∈Lq​([0,T])g\in L^{q}([0,T]), and 1≤p,r,q≤∞1\leq p,r,q\leq\infty such that 1p+1q=1+1r\frac{1}{p}+\frac{1}{q}=1+\frac{1}{r}, the convolution f∗gf\*g belongs to Lr​([0,T])L^{r}([0,T]), and Young’s inequality writes: ‖f∗g‖Lr​([0,T])≤‖f‖Lp​([0,T])⋅‖g‖Lq​([0,T]).\quad\|f\*g\|\_{L^{r}([0,T])}\leq\|f\|\_{L^{p}([0,T])}\cdot\|g\|\_{L^{q}([0,T])}.

∙\bullet Convolution between a function and a measure. Let f:(0,T]→ℝf:(0,T]\to\mathbb{R} be a function and μ∈ℳ\mu\in\mathcal{M}. Their convolution (whenever the integral is well-defined) is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (f∗μ)​(t)=∫[0,t)f​(t−s)​𝑑μ​(s)=∫[0,t)f​(t−s)​μ​(d​s)=(f∗μ𝟏)t,t∈(0,T].(f\*\mu)(t)=\int\_{[0,t)}f(t-s)\,d\mu(s)=\int\_{[0,t)}f(t-s)\,\mu(ds)=(f\stackrel{{\scriptstyle\mu}}{{\*}}\mathbf{1})\_{t},\quad t\in(0,T]. |  | (1.3) |

∙\bullet For a random variable/vector/process XX, we denote by ℒ​(X)\mathcal{L}(X) or [X][X] its law or distribution.

∙\bullet X⟂⟂YX\perp\!\!\!\perp Y stands for independence of random variables, vectors or processes XX and YY.

∙\bullet For a measurable function φ:ℝ+→ℝ\varphi:\mathbb{R}^{+}\to\mathbb{R}, we denote:

∀p≥1,‖φ‖Lp​([0,T])p:=∫0T|φ​(u)|p​𝑑uand‖φ‖∞=‖φ‖sup:=supu∈ℝ+|φ​(u)|.\forall p\geq 1,\quad\|\varphi\|^{p}\_{L^{p}([0,T])}:=\int\_{0}^{T}|\varphi(u)|^{p}\,du\quad\text{and}\quad\displaystyle\|\varphi\|\_{\infty}=\|\varphi\|\_{\sup}:=\sup\_{u\in\mathbb{R}^{+}}|\varphi(u)|.

∙\bullet Given p≥1p\geq 1 and η∈(0,1)\eta\in(0,1) let Wη,p​([0,T])W^{\eta,p}([0,T]) be the Banach space of equivalence classes of measurable functions f:[0,T]⟶ℝf:[0,T]\longrightarrow\mathbb{R} with finite norm (Sobolev–Slobodeckij norm) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f‖Wη,p​([0,T]):=(∫0T|f​(t)|p​𝑑t+∫0T∫0T|f​(t)−f​(s)|p|t−s|1+η​p​𝑑s​𝑑t)1/p.\|f\|\_{W^{\eta,p}([0,T])}:=\left(\int\_{0}^{T}|f(t)|^{p}\,dt+\int\_{0}^{T}\int\_{0}^{T}\frac{|f(t)-f(s)|^{p}}{|t-s|^{1+\eta p}}\,ds\,dt\right)^{1/p}. |  | (1.4) |

Finally, define for a kernel KK, the quantity [K]η,p,T=(∫0Tt−η​p​|K​(t)|p​𝑑t+∫0T∫0T|K​(t)−K​(s)|p|t−s|1+η​p​𝑑s​𝑑t)1/p.[K]\_{\eta,p,T}=\left(\int\_{0}^{T}t^{-\eta p}|K(t)|^{p}dt+\int\_{0}^{T}\int\_{0}^{T}\frac{|K(t)-K(s)|^{p}}{|t-s|^{1+\eta p}}dsdt\right)^{1/p}.

∙\bullet Γ​(a)=∫0+∞ua−1​e−u​𝑑u,a>0,andB​(a,b)=∫01ua−1​(1−u)b−1​𝑑u,a,b>0.\Gamma(a)=\int\_{0}^{+\infty}u^{a-1}e^{-u}\,du,\quad a>0,\quad\text{and}\quad B(a,b)=\int\_{0}^{1}u^{a-1}(1-u)^{b-1}\,du,\quad a,b>0.
We recall the classical identities:
Γ​(a+1)=a​Γ​(a)andB​(a,b)=Γ​(a)​Γ​(b)Γ​(a+b)\Gamma(a+1)=a\,\Gamma(a)\quad\text{and}\quad B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}
and we set ℝ+=[0,+∞)\mathbb{R}\_{+}=[0,+\infty), ℝ−=(−∞,0]\mathbb{R}\_{-}=(-\infty,0].

The results of this paper are developed in a one-dimensional setting to keep the presentation fairly short without cumbersome notation. They are expected to extend to a multi-dimensional setting or more general Hilbert spaces in a straightforward manner.

## 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations.

From now we focus on the special case of a  scaled stochastic Volterra equation ([1.1](https://arxiv.org/html/2512.09590v1#S1.E1 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) associated to a convolutive kernel K:ℝ+→ℝ+K:\mathbb{R}\_{+}\to\mathbb{R}\_{+} satisfying ([2.6](https://arxiv.org/html/2512.09590v1#S2.E6 "In 1st item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([2.7](https://arxiv.org/html/2512.09590v1#S2.E7 "In 2nd item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0ϕ(t)+∫0tK(t−s)(μ(s)−λXs)ds+∫0tK(t−s)ς(s)σ(Xs)dWs,X0⟂⟂W.X\_{t}=X\_{0}\phi(t)+\int\_{0}^{t}K(t-s)(\mu(s)-\lambda X\_{s})ds+\int\_{0}^{t}K(t-s)\varsigma(s)\sigma(X\_{s})dW\_{s},\quad X\_{0}\perp\!\!\!\perp W. |  | (2.5) |

where λ>0\lambda>0, μ:𝕋+→ℝ\mu:\mathbb{T}\_{+}\to\mathbb{R} is a bounded Borel function (hence having a well-defined finite Laplace transform on (0,+∞)(0,+\infty)) and σ:𝕋+×ℝ→ℝ\sigma:\mathbb{T}\_{+}\times\mathbb{R}\to\mathbb{R} is γ−\gamma- Hölder continuous in xx, locally uniformly in t∈𝕋+t\!\in\mathbb{T}\_{+}. Note that the drift b​(t,x)=μ​(t)−λ​xb(t,x)=\mu(t)-\lambda x is clearly Lipschitz continuous in xx, uniformly in t∈𝕋+t\!\in\mathbb{T}\_{+}.
We always work under the assumption below, which applies to the inhomogeneous Volterra equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

###### Assumption 2.1 (On Volterra Equations with convolutive kernels).

1. (i)

   Assume that the kernels KK, satisfy for every T>0T>0 :

   * —

     The integrability assumption: The following is satisfied for some θ^∈(0,1]\widehat{\theta}\in(0,1].

     |  |  |  |  |
     | --- | --- | --- | --- |
     |  | (𝒦^θ^c​o​n​t)​∃κ^<+∞,∀δ¯∈(0,T],η^​(δ):=supt∈[0,T][∫(t−δ¯)+tK​(t−u)2​𝑑u]12≤κ^​δ¯θ^.(\widehat{\cal K}^{cont}\_{\widehat{\theta}})\;\;\exists\,\widehat{\kappa}<+\infty,\;\forall\bar{\delta}\!\in(0,T],\;\widehat{\eta}(\delta):=\sup\_{t\in[0,T]}\left[\int\_{(t-\bar{\delta})^{+}}^{t}\thinspace K\big(t-u\big)^{2}du\right]^{\frac{1}{2}}\leq\widehat{\kappa}\,\bar{\delta}^{\,\widehat{\theta}}. |  | (2.6) |
   * —

     The continuity assumption: (𝒦θc​o​n​t)​∃κ<+∞,∃θ∈(0,1]​such that​∀δ¯∈(0,T)({\cal K}^{cont}\_{\theta})\;\;\exists\,\kappa<+\infty,\;\exists\;\theta\in(0,1]\;\text{such that}\;\forall\,\bar{\delta}{\in(0,T)}

     |  |  |  |  |
     | --- | --- | --- | --- |
     |  | (𝒦T,θc​o​n​t)​∀δ¯∈(0,T),η​(δ¯):=supt∈[0,T][∫0t|K​((s+δ)∧T)−K​(s)|2​𝑑s]12≤κ​δ¯θ.({\cal K}^{cont}\_{T,\theta})\;\forall\,\bar{\delta}{\,\in(0,T)},\;\eta(\bar{\delta}):=\sup\_{t\in[0,T]}\left[\int\_{0}^{t}|K(\big(s+\delta)\wedge T\big)-K(s)|^{2}ds\right]^{\frac{1}{2}}\leq\kappa\,\bar{\delta}^{\theta}. |  | (2.7) |
2. (ii)

   Assume that the drift term bb and the diffusion coefficient σ\sigma are of linear growth, i.e. there is a constant Cb,σ>0C\_{b,\sigma}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | |b​(t,x)|+|σ​(t,x)|≤Cb,σ​(1+|x|),for all ​t∈[0,T]​ and ​x∈ℝ.|b(t,x)|+|\sigma(t,x)|\leq C\_{b,\sigma}(1+|x|),\quad\text{for all }t\in[0,T]\text{ and }x\in\mathbb{R}. |  |
3. (iii)

   Assume that the function ℝ∋x↦b​(t,x)\mathbb{R}\ni x\mapsto b(t,x) is Lipschitz continuous and ℝ∋x↦σ​(t,x)\mathbb{R}\ni x\mapsto\sigma(t,x) is Hölder continuous in the space variable uniformly
   in time of order γ\gamma for some γ∈[12,1]\gamma\in[\tfrac{1}{2},1].
   Hence, there are constants Cb,Cσ>0C\_{b},C\_{\sigma}>0 such that
   222In particular bb is of linear growth, i.e. ∃C>0\exists\,C>0 such that |b​(t,x)|≤C​(1+|x|)​and​supt∈[0,T](|b​(t,0)|+|σ​(t,0)|)<+∞|b(t,x)|\leq C(1+|x|)\;\textit{and}\;\sup\_{t\in[0,T]}\left(|b(t,0)|+|\sigma(t,0)|\right)<+\infty

   |  |  |  |
   | --- | --- | --- |
   |  | |μ​(t,x)−μ​(t,y)|≤Cb​|x−y|​and​|σ​(t,x)−σ​(t,y)|≤Cσ​|x−y|γ​hold for all ​t∈[0,T]​ and ​x,y∈ℝ.|\mu(t,x)-\mu(t,y)|\leq C\_{b}|x-y|\;\text{and}\;|\sigma(t,x)-\sigma(t,y)|\leq C\_{\sigma}|x-y|^{\gamma}\;\text{hold for all }t\in[0,T]\text{ and }x,y\in\mathbb{R}. |  |
4. (iv)

   Finally, assume that X0∈Lp​(ℙ)X\_{0}\in L^{p}(\mathbb{P}) for some suitable p∈(0,+∞)p\in(0,+\infty), such that
   the process t→x0​(t)=X0​ϕ​(t)t\to x\_{0}(t)=X\_{0}\phi(t) is absolutely continuous and (ℱt)(\mathcal{F}\_{t})-adapted.

   Moreover, for some δ>0\delta>0, for any p>0p>0 and T>0T>0,

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​(supt∈[0,T]|x0​(t)|p)<+∞,𝔼​[|x0​(t′)−x0​(t)|p]≤CT,p​(1+𝔼​[supt∈[0,T]|x0​(t)|p])​|t′−t|δ​p.\mathbb{E}\,\!\Big(\sup\_{t\in[0,T]}|x\_{0}(t)|^{p}\Big)<+\infty,\quad\mathbb{E}\!\big[\,|x\_{0}(t^{\prime})-x\_{0}(t)|^{p}\,\big]\leq C\_{T,p}\Big(1+\mathbb{E}\,\big[\sup\_{t\in[0,T]}|x\_{0}(t)|^{p}\big]\Big)|t^{\prime}-t|^{\delta p}. |  |

Under Assumption ([2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), if γ=1\gamma=1, then, Equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) has a unique strong solution (Xt)t≥0(X\_{t})\_{t\geq 0} adapted to ℱtX0,W\mathcal{F}^{X\_{0},W}\_{t}, starting from X0∈Lp​(ℙ),p>0X\_{0}\in L^{p}(\mathbb{P}),p>0. This follows by applying the existence Theorem of [[45](https://arxiv.org/html/2512.09590v1#bib.bib45), [28](https://arxiv.org/html/2512.09590v1#bib.bib28)]
to each time interval [0,T][0,T], T∈ℕT\in\mathbb{N}, and gluing the solutions together, utilizing the uniform linear growth of the drift and σ\sigma in time. However, if γ<1\gamma<1, such an equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits at least one weak solution (see [[37](https://arxiv.org/html/2512.09590v1#bib.bib37)], which establishes this result via a Volterra local martingale problem, or [[24](https://arxiv.org/html/2512.09590v1#bib.bib24)], which, in addition, proves positivity and uniqueness in law in the case of inhomogeneous α−\alpha- fractional square root process (corresponding to κ0=0\kappa\_{0}=0 in equation ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and K=K0,α,0K=K\_{0,\alpha,0} in Example [2.1](https://arxiv.org/html/2512.09590v1#S2.ThmTheorem1 "Example 2.1 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") below with α∈[12,1)\alpha\in[\frac{1}{2},1)), using a scaling limit of a sequence of Hawkes process.

Moreover, if X0∈Lp​(ℙ)X\_{0}\!\in L^{p}(\mathbb{P}) for some p>0p>0, then, a pathwise continuous solution on ℝ+\mathbb{R}\_{+} to Equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), starting from X0X\_{0} satisfying (among other properties),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀T>0,∃CT,p>0,‖supt∈[0,T]|Xt|‖p≤CT,p​(1+supt∈[0,T]|ϕ​(t)|​‖|X0|‖p).\forall\,T>0,\;\exists\,C\_{{}\_{T,p}}>0,\quad\big\|\sup\_{t\in[0,T]}|X\_{t}|\big\|\_{p}\leq C\_{{}\_{T,p}}\left(1+\sup\_{t\in[0,T]}|\phi(t)|\big\||X\_{0}|\big\|\_{p}\right). |  | (2.8) |

Note that under our assumptions, if p>0p>0 and 𝔼​[|X0|p]<+∞\mathbb{E}[|X\_{0}|^{p}]<+\infty, then by ([2.8](https://arxiv.org/html/2512.09590v1#S2.E8 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), 𝔼​[supt∈[0,T]|Xt|p]<CT​(1+‖ϕ‖Tp​𝔼​[|X0|p])<+∞\mathbb{E}[\sup\_{t\in[0,T]}|X\_{t}|^{p}]<C\_{T}(1+\|\phi\|^{p}\_{T}\mathbb{E}[|X\_{0}|^{p}])<+\infty for every T>0T>0. Combined with the linear growth in Assumption [2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")(ii) |σ​(t,x)|≤CT′​(1+|x|)|\sigma(t,x)|\leq C^{\prime}\_{T}(1+|x|) for t∈[0,T]t\in[0,T], this implies 𝔼​[supt∈[0,T]|σ​(t,Xt)|p]<CT′​(1+‖ϕ‖Tp​𝔼​[|X0|p])<+∞\mathbb{E}[\sup\_{t\in[0,T]}|\sigma(t,X\_{t})|^{p}]<C^{\prime}\_{T}(1+\|\phi\|^{p}\_{T}\mathbb{E}[|X\_{0}|^{p}])<+\infty for every T>0T>0, enabling the unrestricted use of both regular and stochastic Fubini’s theorems.
Sufficient conditions for interchanging the order of ordinary integration (with respect to a finite measure) and stochastic integration (with respect to a square integrable martingale) are provided in [[42](https://arxiv.org/html/2512.09590v1#bib.bib42), Thm.1], and further details can be found in [[36](https://arxiv.org/html/2512.09590v1#bib.bib36), Thm. IV.65], [[44](https://arxiv.org/html/2512.09590v1#bib.bib44), Theorem 2.6], [[43](https://arxiv.org/html/2512.09590v1#bib.bib43), Theorem 2.6].

We next introduce key tools including (functional) Fourier-Laplace transforms and a series asymptotic results on resolvents of a borel function that will be important to our analysis.

### 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels

The Laplace transform is a powerful tool commonly used to solve differential equations, including the key equation ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). It transforms a Borel function f:ℝ+→ℝ+f:\mathbb{R}\_{+}\to\mathbb{R}\_{+} to LfL\_{f} defined as

∀t≥0,Lf​(t)=∫0+∞e−t​u​f​(u)​𝑑u∈[0,∞].\forall\,t\geq 0,\quad L\_{f}(t)=\int\_{0}^{+\infty}e^{-tu}f(u)du\!\in[0,\infty].

This Laplace transform is non-increasing and if Lf​(t0)<+∞L\_{f}(t\_{0})<+\infty for some t0≥0t\_{0}\geq 0, then Lf​(t)→0L\_{f}(t)\to 0 as t→+∞t\to+\infty by Lebesgue’s dominated convergence theorem.
One can define the Laplace transform of a Borel function f:ℝ+→ℝf:\mathbb{R}\_{+}\to\mathbb{R} on (0,+∞)(0,+\infty) as soon as L|f|​(t)<+∞L\_{|f|}(t)<+\infty for every t>0t>0 by the above formula. The Laplace transform can be extended to ℝ+\mathbb{R}\_{+} as an ℝ\mathbb{R}-valued function if f∈ℒℝ+1​(Leb1)f\!\in{\cal L}^{1}\_{\mathbb{R}\_{+}}({\rm Leb}\_{1}).
  
Throughout this work, we will adopt the below resolvent definition put forth in [[35](https://arxiv.org/html/2512.09590v1#bib.bib35)], which offers a distinct perspective compared to the functional resolvent introduced in [[4](https://arxiv.org/html/2512.09590v1#bib.bib4)] and also discussed or presented in works such as [[2](https://arxiv.org/html/2512.09590v1#bib.bib2)].
Let KK be a convolution kernel satisfying ([2.6](https://arxiv.org/html/2512.09590v1#S2.E6 "In 1st item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), ([2.7](https://arxiv.org/html/2512.09590v1#S2.E7 "In 2nd item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ∫0tK​(u)​𝑑u>0\int\_{0}^{t}K(u)du>0 for every t>0t>0.
For every λ∈ℝ\lambda\!\in\mathbb{R}, the  resolvent or Solvent core RλR\_{\lambda} associated to KK and λ\lambda, known as the  λ\lambda-resolvent of KK is defined as the unique solution – if it exists – to the deterministic Volterra equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,Rλ​(t)+λ​∫0tK​(t−s)​Rλ​(s)​𝑑s=1.\forall\,t\geq 0,\quad R\_{\lambda}(t)+\lambda\int\_{0}^{t}K(t-s)R\_{\lambda}(s)ds=1. |  | (2.9) |

or, equivalently, written in terms of convolution,
Rλ+λ​K∗Rλ=1.R\_{\lambda}+\lambda K\*R\_{\lambda}=1.
This equation is also known as resolvent equation or renewal equation. Its solution always satisfies Rλ​(0)=1R\_{\lambda}(0)=1 and admits the formal Neumann series expansion (Recall that K1⁣∗=KK^{1\*}=K and Kk⁣∗​(t)=∫0tK​(t−s)⋅K(k−1)⁣∗​(s)​𝑑sK^{k\*}(t)=\int\_{0}^{t}K(t-s)\cdot K^{(k-1)\*}(s)\,ds):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rλ=1∗(∑k≥0(−1)k​λk​Kk⁣∗).R\_{\lambda}=\mbox{\bf 1}\*\big(\sum\_{k\geq 0}(-1)^{k}\lambda^{k}K^{k\*}\big). |  | (2.10) |

where, Kk⁣∗K^{k\*} denotes the kk-th convolution of KK or the k-fold ∗\*
product of KK with itself, with the convention, K0⁣∗=δ0K^{0\*}=\delta\_{0} (Dirac mass at 0).

From now on we will assume that the kernel KK has a finite Laplace transform LK​(t)<+∞.L\_{K}(t)<+\infty. Note that, as mentioned in [[35](https://arxiv.org/html/2512.09590v1#bib.bib35)] (see also [[23](https://arxiv.org/html/2512.09590v1#bib.bib23)]), if the (non-negative) kernel KK satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤K​(t)≤C​eb​t​ta−1​ for some ​a,b,C>0∈ℝ+.0\leq K(t)\leq Ce^{bt}t^{a-1}\mbox{ for some }\;a,\,\;b,\;C>0\!\in\mathbb{R}\_{+}. |  | (2.11) |

then, by induction 1∗K∗n​(t)≤Cn​eb​t​Γ​(a)nΓ​(a​n+1)​ta​n,\mbox{\bf 1}\*K^{\*n}(t)\leq C^{n}e^{bt}\frac{\Gamma(a)^{n}}{\Gamma(an+1)}t^{an}, so that for such kernels, the above series ([2.10](https://arxiv.org/html/2512.09590v1#S2.E10 "In 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is absolutely converging for every t>0t>0 implying that the function RλR\_{\lambda} is well-defined on (0,+∞)(0,+\infty).

Remark 1. If KK is regular enough (say continuous) the resolvent RλR\_{\lambda} is differentiable and one checks that fλ=−Rλ′f\_{\lambda}=-R^{\prime}\_{\lambda} satisfies, for every t>0t>0, −fλ​(t)+λ​(Rλ​(0)​K​(t)−K∗fλ​(t))=0-f\_{\lambda}(t)+\lambda\big(R\_{\lambda}(0)K(t)-K\*f\_{\lambda}(t)\big)=0
that is fλf\_{\lambda} is solution to the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | fλ+λ​K∗fλ=λ​Kand readsfλ=∑k≥1(−1)k​λk​Kk⁣∗.f\_{\lambda}+\lambda K\*f\_{\lambda}=\lambda K\quad\text{and reads}\quad f\_{\lambda}=\sum\_{k\geq 1}(-1)^{k}\lambda^{k}K^{k\*}. |  | (2.12) |

2. Taking the Laplace transform from both side of the above equality ([2.12](https://arxiv.org/html/2512.09590v1#S2.E12 "In 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), we have that :
Lfλ​(t)​(1+λ​LK​(t))=λ​LK​(t)L\_{f\_{\lambda}}(t)(1+\lambda L\_{K}(t))=\lambda L\_{K}(t), t>0t>0. Consequently, Lfλ​(t)=λ​LK​(t)1+λ​LK​(t)L\_{f\_{\lambda}}(t)=\frac{\lambda L\_{K}(t)}{1+\lambda L\_{K}(t)}
so that, for λ≥0,\lambda\geq 0, Lfλ​(t)≡0L\_{f\_{\lambda}}(t)\equiv 0 if and only if
LK​(t)≡0L\_{K}(t)\equiv 0 i.e. if and only if K=0K=0 by the injectivity of Laplace transform.

∙\bullet Moreover, taking Laplace transforms of both sides of equation ([2.9](https://arxiv.org/html/2512.09590v1#S2.E9 "In 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and then using that L1​(t)=1tL\_{1}(t)=\frac{1}{t}, yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LRλ​(t)=1t​(1+λ​LK​(t)).L\_{R\_{\lambda}}(t)=\frac{1}{t(1+\lambda L\_{K}(t))}. |  | (2.13) |

3. In particular, if λ>0\lambda>0 and RλR\_{\lambda} turns out to be non-increasing, then fλf\_{\lambda} is non-negative and satisfies 0≤fλ≤λ​K0\leq f\_{\lambda}\leq\lambda K. In that case one also has that ∫0+∞fλ​(t)​𝑑t=1−Rλ​(+∞)\int\_{0}^{+\infty}f\_{\lambda}(t)dt=1-R\_{\lambda}(+\infty), so that fλf\_{\lambda}  is a probability density if and only if limt→+∞Rλ​(t)=0\displaystyle\lim\_{t\to+\infty}R\_{\lambda}(t)=0.

###### Example 2.1 (Laplace transform and λ−\lambda- Resolvent associated to the Exponential-fractional Kernel).

The Laplace transform associated to a kernel KK always exists and reads, for t>0t>0
LK​(t):=∫0+∞e−t​u​K​(u)​𝑑u.L\_{K}(t):=\int\_{0}^{+\infty}e^{-tu}K(u)du.
When K is the Gamma kernel Kb,α,ρ​(t):=b​e−ρ​t​tα−1Γ​(α)⋅𝟏(0,∞)​(t)K\_{b,\alpha,\rho}(t):=be^{-\rho t}\frac{t^{\alpha-1}}{\Gamma(\alpha)}\cdot\mathbf{1}\_{(0,\infty)}(t), for b>0,α>0b>0,\alpha>0 and ρ>0\rho>0, then by
introducing v=u​(t+ρ), we havev=u(t+\rho),\textit{ we have}

|  |  |  |
| --- | --- | --- |
|  | LKb,α,ρ​(t)=∫0∞b​e−(t+ρ)​u​uα−1Γ​(α)​𝑑u=b​(t+ρ)−αΓ​(α)​∫0∞e−v​vα−1​𝑑v=b​(t+ρ)−α.L\_{K\_{b,\alpha,\rho}}(t)=\int\_{0}^{\infty}be^{-(t+\rho)u}\frac{u^{\alpha-1}}{\Gamma(\alpha)}du=\frac{b(t+\rho)^{-\alpha}}{\Gamma(\alpha)}\int\_{0}^{\infty}e^{-v}v^{\alpha-1}dv=b(t+\rho)^{-\alpha}. |  |

Moreover, one checks that these kernels also satisfy ([2.6](https://arxiv.org/html/2512.09590v1#S2.E6 "In 1st item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([2.7](https://arxiv.org/html/2512.09590v1#S2.E7 "In 2nd item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) for α>1/2\alpha>1/2 (with θT=(α−12)∧1\theta\_{{}\_{T}}=(\alpha-\frac{1}{2})\wedge 1) and trivially ([2.11](https://arxiv.org/html/2512.09590v1#S2.E11 "In 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
For simplification, assume that b=1b=1.
It follows from the easy identity Kα,ρ∗Kα′,ρ=Kα+α′,ρK\_{\alpha,\rho}\*K\_{\alpha^{\prime},\rho}=K\_{\alpha+\alpha^{\prime},\rho} and the Neumann series expansion provided in equation ([2.10](https://arxiv.org/html/2512.09590v1#S2.E10 "In 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) that the resolvent
reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rα,ρ,λ​(t)=(1∗δ0)​(t)+∑k≥1(−1)k​λk​(1∗Kα,ρ(k∗))=𝟏ℝ+​(t)+∑k≥1(−1)k​λk​∫0te−ρ​s​sk​α−1Γ​(k​α)​𝑑s.R\_{\alpha,\rho,\lambda}(t)=(1\*\delta\_{0})(t)+\sum\_{k\geq 1}(-1)^{k}\lambda^{k}(\mbox{\bf 1}\*K\_{\alpha,\rho}^{(k\*)})=\mathbf{1}\_{\mathbb{R}\_{+}}(t)+\sum\_{k\geq 1}(-1)^{k}\lambda^{k}\int\_{0}^{t}\frac{e^{-\rho s}s^{k\alpha-1}}{\Gamma(k\alpha)}\,ds. |  | (2.14) |

Hence, if λ>0\lambda>0, we define the function fα,ρ,λ:=−Rα,ρ,λf\_{\alpha,\rho,\lambda}:=-R\_{\alpha,\rho,\lambda} on (0,+∞)(0,+\infty) by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fα,ρ,λ​(t)=−dd​t​Rα,ρ,λ​(t)=−∑k≥1(−1)k​λk​e−ρ​t​tk​α−1Γ​(k​α)=λ​e−ρ​t​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1)).f\_{\alpha,\rho,\lambda}(t)=-\frac{d}{dt}R\_{\alpha,\rho,\lambda}(t)=-\sum\_{k\geq 1}(-1)^{k}\lambda^{k}\frac{e^{-\rho t}t^{k\alpha-1}}{\Gamma(k\alpha)}=\lambda e^{-\rho t}t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\lambda^{k}\frac{t^{\alpha k}}{\Gamma(\alpha(k+1))}. |  | (2.15) |

### 2.2 Wiener-Hopf equations and Forward Process

We will always work under the following assumption.

###### Assumption 2.2 (λ\lambda-resolvent RλR\_{\lambda} of the kernel).

Throughout the paper, we assume that the λ\lambda-resolvent RλR\_{\lambda} of the kernel KK satisfies the following for every λ>0\lambda>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒦){(i)Rλ(t) is differentiable on ℝ+,Rλ(0)=1 and limt→+∞Rλ(t)=a∈[0,1[,(i​i)fλ∈ℒlocp(ℝ+,Leb1),forp≥1, for t>0,Lfλ(t)≠0dt−a.e., where fλ:=−Rλ′,(i​i​i)ϕ∈ℒℝ+1​(Leb1), is a continuous function satisfying​limt→∞ϕ​(t)=ϕ∞, with ​a​ϕ∞<1,(i​v)θ​ is a C1-function such that ​‖θ‖sup<∞​ and ​limt→+∞θ​(t)=μ∞∈ℝ.({\cal K})\quad\left\{\begin{array}[]{ll}(i)&R\_{\lambda}(t)\text{ is }\text{differentiable on }\mathbb{R}^{+},\;R\_{\lambda}(0)=1\text{ and }\lim\_{t\to+\infty}R\_{\lambda}(t)=a\in[0,1[,\\ (ii)&f\_{\lambda}\in{\cal L}\_{\text{loc}}^{p}(\mathbb{R}\_{+},\text{Leb}\_{1}),\;\text{for}\;p\geq 1\;,\text{ for }\;t>0,\;L\_{f\_{\lambda}}(t)\neq 0\;dt-a.e.,\text{ where }f\_{\lambda}:=-R^{\prime}\_{\lambda},\\ (iii)&\phi\in{\cal L}^{1}\_{\mathbb{R}\_{+}}(\text{Leb}\_{1}),\text{ is a continuous function satisfying}\;\lim\_{t\to\infty}\phi(t)=\phi\_{\infty},\text{ with }a\phi\_{\infty}<1,\\ (iv)&\theta\text{ is a $C^{1}$-function such that }\|\theta\|\_{\sup}<\infty\text{ and }\lim\_{t\to+\infty}\theta(t)=\mu\_{\infty}\in\mathbb{R}.\end{array}\right. |  | (2.16) |

Remark:
Under the assumption (𝒦)({\cal K}), fλf\_{\lambda} is a (1−a)(1-a)-sum measure, i.e., ∫0+∞fλ​(s)​𝑑s=1−a\int\_{0}^{+\infty}f\_{\lambda}(s)\,ds=1-a. Furthermore, limt→+∞∫0tfλ​(t−s)​θ​(s)​𝑑s=μ∞\lim\_{t\to+\infty}\int\_{0}^{t}f\_{\lambda}(t-s)\theta(s)ds=\mu\_{\infty} and limt→+∞ϕ​(t)−(fλ∗ϕ)​(t)=ϕ∞​a.\lim\_{t\to+\infty}\phi(t)-(f\_{\lambda}\*\phi)(t)=\phi\_{\infty}\,a.. (see [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Lemma 3.1]).
Finally, if fλ=−Rλ′>0​ for ​t>0f\_{\lambda}=-R^{\prime}\_{\lambda}>0\text{ for }t>0, then fλf\_{\lambda} is a probability density in which case, RλR\_{\lambda} is non-increasing.
This is in particular the case for the Mittag-Leffler density function fα,λf\_{\alpha,\lambda} for α∈(12,1)\alpha\in(\frac{1}{2},1).

We now come to the main result of these preliminaries.

###### Proposition 2.2 (Wiener-Hopf transform and Forward Process).

For all s,t∈[0,T]s,t\in[0,T], we call ξt​(s):=𝔼​[Xs∣ℱt]\xi\_{t}(s):=\mathbb{E}[X\_{s}\mid\mathcal{F}\_{t}] the Forward process of XX.
Assume that assumptions ([2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) are satisfied and that X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} is a continuous weak solution of ([1.1](https://arxiv.org/html/2512.09590v1#S1.E1 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
(Xt)t≥0(X\_{t})\_{t\geq 0} is solution of equation ([1.1](https://arxiv.org/html/2512.09590v1#S1.E1 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) if and only if it is the solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0​(ϕ​(t)−∫0tfλ​(t−s)​ϕ​(s)​𝑑s)+1λ​∫0tfλ​(t−s)​θ​(s)​𝑑s+1λ​∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws.X\_{t}=X\_{0}\big(\phi(t)-\int\_{0}^{t}f\_{\lambda}(t-s)\phi(s)ds\big)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\theta(s)ds+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})\,dW\_{s}. |  | (2.17) |

Then ξt​(s)\xi\_{t}(s) is an ℱt\mathcal{F}\_{t} -martingale, and for all s,t∈[0,T]s,t\in[0,T] such that t≤st\leq s, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xs∣ℱt]=X0​ϕ​(s)+∫0sK​(s−r)​(θ​(r)−λ​𝔼​[Xr∣ℱt])​dr+∫0tK​(s−r)​σ​(r,Xr)​dWr.\mathbb{E}[X\_{s}\mid\mathcal{F}\_{t}]=X\_{0}\phi(s)+\int\_{0}^{s}K(s-r)\left(\theta(r)-\lambda\mathbb{E}[X\_{r}\mid\mathcal{F}\_{t}]\right)\,\mathrm{d}r+\int\_{0}^{t}K(s-r)\sigma(r,X\_{r})\,\mathrm{d}W\_{r}. |  | (2.18) |

Equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xs∣ℱt]=X0​(ϕ​(s)−∫0sfλ​(s−r)​ϕ​(r)​𝑑r)+1λ​∫0sfλ​(s−r)​θ​(r)​dr+1λ​∫0tfλ​(s−r)​σ​(r,Xr)​dWr.\mathbb{E}[X\_{s}\mid\mathcal{F}\_{t}]=X\_{0}(\phi(s)-\int\_{0}^{s}f\_{\lambda}(s-r)\phi(r)\,dr)+\frac{1}{\lambda}\int\_{0}^{s}f\_{\lambda}(s-r)\theta(r)\,\mathrm{d}r+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(s-r)\sigma(r,X\_{r})\,\mathrm{d}W\_{r}. |  | (2.19) |

Moreover, the forward process ξt​(s)\xi\_{t}(s)
satisfies the stochastic differential equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ξt​(s)=1λ​fλ​(s−t)​σ​(t,Xt)​d​Wt,ξ0​(s)=X0​(ϕ​(s)−∫0sfλ​(s−r)​ϕ​(r)​𝑑r)+1λ​∫0sfλ​(s−r)​θ​(r)​dr.\mathrm{d}\xi\_{t}(s)=\frac{1}{\lambda}f\_{\lambda}(s-t)\,\sigma(t,X\_{t})\,\mathrm{d}W\_{t},\;\xi\_{0}(s)=X\_{0}(\phi(s)-\int\_{0}^{s}f\_{\lambda}(s-r)\phi(r)\,dr)+\frac{1}{\lambda}\int\_{0}^{s}f\_{\lambda}(s-r)\theta(r)\,\mathrm{d}r. |  | (2.20) |

where ξ0​(s):=𝔼​[Xs∣ℱ0]\xi\_{0}(s):=\mathbb{E}[X\_{s}\mid\mathcal{F}\_{0}] is the initial condition (the expected process at future time s).

Remark:
It is easy to see that the initial forward process curve t↦ξ0​(t)=𝔼​[Xt∣ℱ0]t\mapsto\xi\_{0}(t)=\mathbb{E}[X\_{t}\mid\mathcal{F}\_{0}] is the solution to the Volterra equation

ξ0​(t)=X0​ϕ​(t)+∫0tK​(t−s)​(θ​(s)−λ​ξ0​(s))​𝑑s,\xi\_{0}(t)=X\_{0}\phi(t)+\int\_{0}^{t}K(t-s)(\theta(s)-\lambda\xi\_{0}(s))\,ds,

or equivalently, if the kernel KK is the α\alpha-fractional kernels K​(t)=Kα​(t)=uα−1Γ​(α)​𝟏ℝ​(t)K(t)=K\_{\alpha}(t)=\frac{u^{\alpha-1}}{\Gamma(\alpha)}\mathbf{1}\_{\mathbb{R}}(t), α∈(12,1)\alpha\in(\frac{1}{2},1), the initial forward process is the solution to the fractional equation

|  |  |  |
| --- | --- | --- |
|  | ξ0​(t)−X0​ϕ​(t)+λ​Iα​(ξ0)​(t)=Iα​(θ)​(t),\xi\_{0}(t)-X\_{0}\phi(t)+\lambda\,I^{\alpha}(\xi\_{0})(t)=I^{\alpha}(\theta)(t), |  |

where IrI^{r} denotes the fractional integral of order r∈(0,1]r\in(0,1].333Recall that the fractional integral of order r∈(0,1]r\in(0,1] of a function ff is Ir​f​(t)=1Γ​(r)​∫0t(t−s)r−1​f​(s)​𝑑s,I^{r}f(t)=\frac{1}{\Gamma(r)}\int\_{0}^{t}(t-s)^{r-1}f(s)\,ds,
while the fractional derivative of order r∈[0,1)r\in[0,1) is defined asDr​f​(t)=1Γ​(1−r)​dd​t​∫0t(t−s)−r​f​(s)​𝑑s,D^{r}f(t)=\frac{1}{\Gamma(1-r)}\frac{d}{dt}\int\_{0}^{t}(t-s)^{-r}f(s)\,ds,
whenever the integrals exist. As a result, setting θ​(t)=Dα​(ξ0​(t)−X0​ϕ​(t))+ξ0​(t)\theta(t)=D^{\alpha}(\xi\_{0}(t)-X\_{0}\phi(t))+\xi\_{0}(t)
ensures that the model is consistent with any given initial forward process curve ξ0​(u)=𝔼​[Xu]\xi\_{0}(u)=\mathbb{E}[X\_{u}]. Here, DrD^{r} denotes the fractional derivative of order r∈[0,1)r\in[0,1). (see also Proposition 3.1 and Remark 3.2 in [[15](https://arxiv.org/html/2512.09590v1#bib.bib15)])

## 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process

In this section, we establish the representation result for the conditional Laplace functional of the time-inhomogeneous affine Volterra equation and prove that it is exponential-affine in the past path.
More generally, we consider the time-inhomogeneous affine Volterra equation where the diffusion coefficient is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(t,x)=ς​(t)​σ​(x)withσ​(x):=κ0+κ1​x,κ1>0,κ0>0.\sigma(t,x)=\varsigma(t)\,\sigma(x)\quad\text{with}\quad\sigma(x):=\sqrt{\kappa\_{0}+\kappa\_{1}\,x}\,,\quad\kappa\_{1}>0\,,\kappa\_{0}>0. |  | (3.21) |

and we assume that such resulting equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
has (at least) one non-negative weak solution X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} defined on some stochastic basis (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}), e.g. as the CC-weak limit of Hawkes processes as illustrated in the influential contribution [[24](https://arxiv.org/html/2512.09590v1#bib.bib24)]. We denote by ℙx\mathbb{P}\_{x},
the probability measure on Ω\Omega representing the law of the Volterra process (Xt)t>0(X\_{t})\_{t>0} started at xx, i.e., it holds that X0=xX\_{0}=x, ℙx\mathbb{P}\_{x}-almost surely. Here, 𝔼x\mathbb{E}\_{x} denotes the expectation with respect to ℙx\mathbb{P}\_{x}.

From now on, we set x0​(⋅)≡x¯0​ϕ​(⋅)x\_{0}(\cdot)\equiv\bar{x}\_{0}\phi(\cdot) and aim at analysing the measure-extended conditional Laplace functional for any measure μ∈ℳ−⊂ℳ\mu\in\mathcal{M}^{-}\subset\mathcal{M}, the subset of ℝ−\mathbb{R}\_{-}-valued set functions μ∈ℳ\mu\in\mathcal{M} negative on ℝ+\mathbb{R}\_{+}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∫0TXT−s​μ​(d​s))|ℱt],t∈[0,T].\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\big(\int\_{0}^{T}X\_{T-s}\,\mu(\mathrm{d}s)\big)\,\Big|\,\mathcal{F}\_{t}\Bigg],\quad t\in[0,T]. |  | (3.22) |

Remarkably, the functional in equation ([3.22](https://arxiv.org/html/2512.09590v1#S3.E22 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a representation that can be expressed in terms of the solution of an associated time-inhomogeneous measure-extended Riccati-type Volterra equation.
This type of representation has been investigated in the convolution setting by [[2](https://arxiv.org/html/2512.09590v1#bib.bib2), Theorem 4.3] and, in the non-convolution case with more general Volterra time-inhomogeneous diffusions, by [[3](https://arxiv.org/html/2512.09590v1#bib.bib3), Theorem 2.1]. These results extend the classical exponential-affine transform for standard affine diffusions (see, e.g., [[12](https://arxiv.org/html/2512.09590v1#bib.bib12)]) to the Volterra framework.
In our context, however, the structure differs significantly: the initial condition is not deterministic but instead given by a random function x0∈Lloc1​(ℝ+;ℝ+)x\_{0}\in L^{1}\_{\text{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{+}) which evolves deterministically for t>0t>0. Concretely, for t>0t>0, the value x0​(t)x\_{0}(t) is ℱ0\mathcal{F}\_{0}-measurable, where ℱ0\mathcal{F}\_{0} encodes the information up to time t=0t=0. Moreover, we consider a measure-extended version i.e. we extend the affine transform formula in the spirit of [[12](https://arxiv.org/html/2512.09590v1#bib.bib12), [2](https://arxiv.org/html/2512.09590v1#bib.bib2), [3](https://arxiv.org/html/2512.09590v1#bib.bib3)] from f∈Lloc1​(ℝ+;ℝ)f\in L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}) to μ∈ℳ\mu\in\mathcal{M}.
This provides the key tool to characterize the finite-dimensional distributions of the stationary process via a measure-extended Riccati–Volterra equation.
To state the main formula in a synthetic form, let us define and then consider for a measure μ∈ℳ\mu\in\mathcal{M}, the following measure-extended Riccati–Volterra equation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∀μ∈ℳ,ψ​(t)\displaystyle\forall\,\mu\in\mathcal{M},\quad\psi(t) | =∫[0,t)K​(t−s)​μ​(d​s)+∫0tK​(t−s)​F​(T−s,ψ​(s))​ds,t≥0\displaystyle=\int\_{[0,t)}K(t-s)\,\mu(\,\mathrm{d}s)+\int\_{0}^{t}K(t-s)\,F(T-s,\psi(s))\,\,\mathrm{d}s,\quad t\geq 0 |  | (3.23) |
|  | F​(s,ψ)\displaystyle F(s,\psi) | =−λ​ψ+κ12​ς2​(s)​ψ2(t,ψ)∈ℝ+×ℝ.\displaystyle=-\lambda\psi+\frac{\kappa\_{1}}{2}\varsigma^{2}(s)\psi^{2}\quad(t,\psi)\in\mathbb{R}\_{+}\times\mathbb{R}. |  |

where λ∈ℝ\lambda\in\mathbb{R}, and ς:ℝ+→ℝ\varsigma:\mathbb{R}\_{+}\to\mathbb{R} is a given continuous function.

Remark:
Equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is written in a forward form. An equivalent expression in backward form is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(T−t)=∫tTK​(s−t)​𝑑μ​(T−s)+∫tTF​(s,ψ​(T−s))​K​(s−t)​ds.\psi(T-t)=\int\_{t}^{T}K(s-t)\,d\mu(T-s)+\int\_{t}^{T}F(s,\psi(T-s))K(s-t)\,\,\mathrm{d}s. |  | (3.24) |

This formulation ([3.24](https://arxiv.org/html/2512.09590v1#S3.E24 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is essential in problems where the system’s behavior is determined by a known final state, allowing for the determination of the system’s evolution by integrating backwards in time.

###### Lemma 3.1.

The inhomogeneous measure-extended Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(t)=1λ​∫[0,t)fλ​(t−s)​μ​(d​s)+1λ​κ12​∫0tς2​(T−s)​ψ2​(s)​fλ​(t−s)​ds.\psi(t)=\frac{1}{\lambda}\int\_{[0,t)}f\_{\lambda}(t-s)\,\,\mu(\mathrm{d}s)+\frac{1}{\lambda}\frac{\kappa\_{1}}{2}\int\_{0}^{t}\varsigma^{2}(T-s)\psi^{2}(s)f\_{\lambda}(t-s)\,\mathrm{d}s. |  | (3.25) |

where fλ:=−Rλ′​ for ​t>0,f\_{\lambda}:=-R^{\prime}\_{\lambda}\text{ for }t>0, is solution to the equation fλ+λ​K∗fλ=λ​K.f\_{\lambda}+\lambda K\*f\_{\lambda}=\lambda K.

Proof: Equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) can be interpreted as a Wiener-Hopf equation with x​(t)=ψ​(t)x(t)=\psi(t) and

|  |  |  |
| --- | --- | --- |
|  | g(t)=∫[0,t)K(t−s)μ(ds)+κ12∫0tK(t−s)ς2(T−s)ψ2(s)ds=((μ+κ12ς2(T−⋅)ψ2)∗K)(t).g(t)=\int\_{[0,t)}K(t-s)\,\mu(\,\mathrm{d}s)+\frac{\kappa\_{1}}{2}\int\_{0}^{t}K(t-s)\,\varsigma^{2}(T-s)\,\psi^{2}(s)\,\,\mathrm{d}s=\Big(\big(\mu+\frac{\kappa\_{1}}{2}\varsigma^{2}(T-\cdot)\,\psi^{2}\big)\*K\Big)(t). |  |

From [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 2.4 (a)], it follows that the expression for ψ\psi is given for all t≥0t\geq 0 by:

|  |  |  |
| --- | --- | --- |
|  | ψ(t)=g(t)−∫0tfλ(t−s)g(s)ds=((μ+κ12ς2(T−⋅)ψ2)∗K)(t)\displaystyle\,\psi(t)=g(t)-\int\_{0}^{t}f\_{\lambda}(t-s)g(s)\,\,\mathrm{d}s=\Big(\big(\mu+\frac{\kappa\_{1}}{2}\varsigma^{2}(T-\cdot)\,\psi^{2}\big)\*K\Big)(t) |  |
|  |  |  |
| --- | --- | --- |
|  | −∫0tfλ(t−s)[((μ+κ12ς2(T−⋅)ψ2)∗K)(s)]ds=(μ∗K)(t)+κ12((ς2(T−⋅)ψ2)∗K)(t)\displaystyle-\int\_{0}^{t}f\_{\lambda}(t-s)\Big[\Big(\big(\mu+\frac{\kappa\_{1}}{2}\varsigma^{2}(T-\cdot)\,\psi^{2}\big)\*K\Big)(s)\Big]\,\mathrm{d}s=\big(\mu\*K\big)(t)+\frac{\kappa\_{1}}{2}\Big(\big(\varsigma^{2}(T-\cdot)\,\psi^{2}\big)\*K\Big)(t) |  |
|  |  |  |
| --- | --- | --- |
|  | −∫0tfλ(t−s)(μ∗K)(s)ds−κ12∫0tfλ(t−s)(K∗(ς2(T−⋅)ψ2))(s)ds\displaystyle\quad-\int\_{0}^{t}f\_{\lambda}(t-s)(\mu\*K)(s)\,\,\mathrm{d}s-\frac{\kappa\_{1}}{2}\int\_{0}^{t}f\_{\lambda}(t-s)\left(K\*\big(\varsigma^{2}(T-\cdot)\,\psi^{2}\big)\right)(s)\,\,\mathrm{d}s |  |
|  |  |  |
| --- | --- | --- |
|  | =(μ∗(K−fλ∗K))(t)+κ12((ς2(T−⋅)ψ2)∗(K−fλ∗K))(t)=1λ(μ∗fλ+κ12(ς2(T−⋅)ψ2)∗fλ)(t)\displaystyle=\big(\mu\*(K-f\_{\lambda}\*K)\big)(t)+\frac{\kappa\_{1}}{2}\big((\varsigma^{2}(T-\cdot)\,\psi^{2})\*(K-f\_{\lambda}\*K)\big)(t)=\frac{1}{\lambda}\Big(\mu\*f\_{\lambda}+\frac{\kappa\_{1}}{2}\big(\varsigma^{2}(T-\cdot)\,\psi^{2}\big)\*f\_{\lambda}\Big)(t) |  |

where we used commutativity and associativity (via regular Fubini’s theorem) of convolution, and the
last equality coming from the definition ([2.12](https://arxiv.org/html/2512.09590v1#S2.E12 "In 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) of fλf\_{\lambda} namely fλ+λ​K∗fλ=λ​K.f\_{\lambda}+\lambda K\*f\_{\lambda}=\lambda K.
The converse is true by convoluting equation ([3.25](https://arxiv.org/html/2512.09590v1#S3.E25 "In Lemma 3.1. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) by KK and arguing similarly or by using the equivalence in the Wiener-Hopf equation since the solution is uniquely defined on ℝ+\mathbb{R}\_{+} up to d​t\text{d}t-almost sure equality.

In this section, we will work under the following assumptions:

###### Assumption 3.2.

Assume that the kernel KK is such that for every λ>0\lambda>0, its λ\lambda-resolvent RλR\_{\lambda} exists and fλ:=−Rλ′f\_{\lambda}:=-R^{\prime}\_{\lambda}, together with KK are nonnegative, not identically zero, and continuous on (0,∞)(0,\infty). Assume furthermore that the kernel K∈Llocp​(ℝ+)K\in L^{p}\_{\text{loc}}(\mathbb{R}\_{+}), satisfies equations ([2.6](https://arxiv.org/html/2512.09590v1#S2.E6 "In 1st item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([2.7](https://arxiv.org/html/2512.09590v1#S2.E7 "In 2nd item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) of Assumption [2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and the Sobolev-Slobodeckij-type condition [K]η,p,T<∞[K]\_{\eta,p,T}<\infty
for some p≥2p\geq 2, η∈(0,1)\eta\in(0,1), and for T>0T>0.

Finally assume that the function ς:ℝ+→ℝ\varsigma:\mathbb{R}\_{+}\to\mathbb{R} is continuous and bounded on (0,∞)(0,\infty), i.e. ‖ς‖∞<∞\|\varsigma\|\_{\infty}<\infty.

###### Example 3.3.

A sufficient condition for a kernel KK to satisfy the assumption [3.2](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") is
that it satisfies ([2.11](https://arxiv.org/html/2512.09590v1#S2.E11 "In 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and K,fλK,f\_{\lambda} are completely monotone (or 1−Rλ1-R\_{\lambda} is
a Bernstein function) and not identically zero.
This covers in particular the gamma kernel K​(t)=tα−1Γ​(α)​e−ρ​t​𝟏ℝ+K(t)=\frac{t^{\alpha-1}}{\Gamma(\alpha)}e^{-\rho t}\mathbf{1}\_{\mathbb{R}\_{+}} with α∈(12,1]\alpha\in\left(\tfrac{1}{2},1\right] and ρ≥0\rho\geq 0 ( see e.g. [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Propositions 6.1 and 6.3]).
We have by [[1](https://arxiv.org/html/2512.09590v1#bib.bib1)] [K]η,p,T<∞[K]\_{\eta,p,T}<\infty for each T>0T>0, p=2p=2, and η∈(0,H)\eta\in(0,H).

The results of this section will play a central role in
section [5](https://arxiv.org/html/2512.09590v1#S5 "5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), where we characterize the
distributional properties of the limiting and stationary process
associated with inhomogeneous affine Volterra equations.

### 3.1 Analysis of the Measure-extended Riccati–Volterra Equation

We derive the existence of a solution to the Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
First note that, for any T>0T>0, from the definition of the convolution of a measure μ∈ℳ\mu\in\mathcal{M} and a function f:(0,T]→ℝf:(0,T]\to\mathbb{R} in equation ([1.3](https://arxiv.org/html/2512.09590v1#S1.E3 "In 1.3 Structure of the paper and Notations ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), it is straightforward to check that for each p∈[1,∞]p\in[1,\infty],
‖f∗μ‖Lp​([0,T])≤‖f‖Lp​([0,T])​|μ|​([0,T]).\|f\*\mu\|\_{L^{p}([0,T])}\leq\|f\|\_{L^{p}([0,T])}\,|\mu|([0,T]).
Furthermore, if ff is continuous on [0,T][0,T], then the convolution f∗μf\*\mu is also continuous on [0,T][0,T].

###### Theorem 3.4 (Existence of solution to the Riccati–Volterra Equation).

Under Assumption [3.2](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."),

(a) For each μ∈ℳ−\mu\in\mathcal{M}^{-}, the measure-extended Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a unique global solution ψ=ψ​(⋅,μ)∈Lloc2​(ℝ+;ℝ−)\psi=\psi(\cdot,\mu)\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}), i.e., ψ​(t)≤0\psi(t)\leq 0 for all t∈[0,T]t\in[0,T].

(b) (LpL^{p}-bounds and Sobolev-Slobodeckij regularity): ‖ψ​(⋅,μ)‖Lq​([0,T])≤1λ​|μ|​([0,T])​‖fλ‖Lq​([0,T])\|\psi(\cdot,\mu)\|\_{L^{q}([0,T])}\leq\frac{1}{\lambda}|\mu|([0,T])\,\|f\_{\lambda}\|\_{L^{q}([0,T])} for each q∈[1,p]q\in[1,p].
Moreover, The unique solution ψ\psi
of ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) belongs to the fractional Sobolev
space Wη,p​([0,T])W^{\eta,p}([0,T]), and satisfies the Sobolev-Slobodeckij a priori estimate for a constant C:=Cp,λ,κ1,ς,T>0C:=C\_{p,\lambda,\kappa\_{1},\varsigma,T}>0

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ψ​(⋅,μ)‖Wη,p​([0,T])≤‖ψ​(⋅,μ)‖Lp​([0,T])+C​(1+[K]η,p,Tp)​(1+|μ|​([0,T])+‖ψ​(⋅,μ)‖L2​([0,T])2).\|\psi(\cdot,\mu)\|\_{W^{\eta,p}([0,T])}\leq\|\psi(\cdot,\mu)\|\_{L^{p}([0,T])}+C\,(1+[K]\_{\eta,p,T}^{p})\,\left(1+|\mu|([0,T])+\|\psi(\cdot,\mu)\|\_{L^{2}([0,T])}^{2}\right). |  | (3.26) |

(c) (Continuity): The function ψ​(⋅,μ)\psi(\cdot,\mu) is continuous at each t0≥0t\_{0}\geq 0 for which the convolution (K∗μ)(⋅):=∫[0,⋅)K(⋅−s)μ(ds)(K\*\mu)(\cdot):=\int\_{[0,\cdot)}K(\cdot-s)\,\mu(\,\mathrm{d}s) is continuous at t0t\_{0}.

For clarity and conciseness, the proof of the above Theorem is postponed to Appendix [A](https://arxiv.org/html/2512.09590v1#A1 "Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), where the main technical results are presented. The bounds in (b) are provided here as a straightforward consequence of how the existence result is established (see Appendix [A](https://arxiv.org/html/2512.09590v1#A1 "Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") for further details).
It is worth noting that
Theorem [3.4](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem4 "Theorem 3.4 (Existence of solution to the Riccati–Volterra Equation). ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") applied for T=∞T=\infty still provides the desired integrability as sketched below.

###### Corollary 3.5.

Let’s consider a measure μ∈ℳ−\mu\in\mathcal{M}^{-} with |μ|​(ℝ+)<∞|\mu|(\mathbb{R}\_{+})<\infty. Then, under the same assumptions as in Theorem [3.4](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem4 "Theorem 3.4 (Existence of solution to the Riccati–Volterra Equation). ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), ψ∈L1​(ℝ+;ℝ−)∩L2​(ℝ+;ℝ−)\psi\in L^{1}(\mathbb{R}\_{+};\mathbb{R}\_{-})\cap L^{2}(\mathbb{R}\_{+};\mathbb{R}\_{-}), i.e. ∫0∞(|ψ​(t,μ)|+|ψ​(t,μ)|2)​𝑑t<∞;\int\_{0}^{\infty}\left(|\psi(t,\mu)|+|\psi(t,\mu)|^{2}\right)dt<\infty; where ψ=ψ​(⋅,μ)\psi=\psi(\cdot,\mu) is the solution to the below measure-extended Riccati–Volterra equation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ​(t,μ)\displaystyle\psi(t,\mu) | =∫[0,t)K​(t−s)​μ​(d​s)+∫0tK​(t−s)​F∞​(ψ​(s,μ))​ds,t≥0\displaystyle=\int\_{[0,t)}K(t-s)\,\mu(\,\mathrm{d}s)+\int\_{0}^{t}K(t-s)\,F\_{\infty}(\psi(s,\mu))\,\,\mathrm{d}s,\quad t\geq 0 |  | (3.27) |
|  | F∞​(ψ)\displaystyle F\_{\infty}(\psi) | :=−λ​ψ+κ12​ς∞2​ψ2andς∞2:=limt→+∞ς2​(t).\displaystyle=-\lambda\psi+\frac{\kappa\_{1}}{2}\varsigma^{2}\_{\infty}\psi^{2}\quad\text{and}\quad\varsigma^{2}\_{\infty}=\lim\_{t\to+\infty}\varsigma^{2}(t). |  |

Proof: Note that 1{0≤t≤T}​ς2​(T−t)→limT→+∞ς2​(T):=ς∞2\mbox{\bf 1}\_{\{0\leq t\leq T\}}\varsigma^{2}(T-t)\to\lim\_{T\to+\infty}\varsigma^{2}(T):=\varsigma^{2}\_{\infty} for every t∈ℝ+t\!\in\mathbb{R}\_{+} as T→+∞T\to+\infty.

### 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes

Similarly to the classical square-root process, there is a semi-explicit form for the
Laplace transform of the inhomogeneous affine Volterra process, i.e., it is an affine process
on ℝ+\mathbb{R}\_{+}.
The following theorem establishes the weak existence and uniqueness of ℝ+−\mathbb{R}\_{+}- solutions to ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), together with an expression for their Laplace transform ([3.22](https://arxiv.org/html/2512.09590v1#S3.E22 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
in terms of the Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

###### Theorem 3.6.

Fix T>0T>0 and suppose that Assumption [3.2](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") holds.
Consider a measure μ∈ℳ−\mu\in\mathcal{M}^{-}
such that (K∗μ)(K\*\mu) is continuous on [0,T][0,T]. Then, the measure-extended Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a unique global solution ψ=ψ​(⋅,μ)∈Lloc2​(ℝ+;ℝ−)∩𝒞​([0,T],ℝ−)\psi=\psi(\cdot,\mu)\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-})\cap\mathcal{C}([0,T],\mathbb{R}\_{-}), i.e., ψ​(t)≤0\psi(t)\leq 0 for all t∈[0,T]t\in[0,T].

1. Furthermore, the following exponential-affine transform formula holds for the measure-extended Laplace transform of XTX\_{T}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∫0TXT−s​μ​(d​s))|ℱt]=exp⁡(∫0Tξt​(T−s)​μ​(d​s)+12​∫tTς2​(s)​σ2​(ξt​(s))​ψ2​(T−s)​ds).\displaystyle\mathbb{E}\_{\bar{x}\_{0}}\left[\exp\left(\int\_{0}^{T}X\_{T-s}\,\,\mu(\mathrm{d}s)\right)\Big|\mathcal{F}\_{t}\right]=\exp\left(\int\_{0}^{T}\xi\_{t}(T-s)\,\mu(\mathrm{d}s)+\frac{1}{2}\int\_{t}^{T}\varsigma^{2}(s)\sigma^{2}(\xi\_{t}(s))\,\psi^{2}(T-s)\,\mathrm{d}s\right). |  | (3.28) |

where the process ξt​(s)\xi\_{t}(s) is given by: ξt​(s)=ξ0​(s)+1λ​∫0tfλ​(s−r)​σ​(r,Xr)​dWr,for ​t∈[0,s],\xi\_{t}(s)=\xi\_{0}(s)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(s-r)\,\sigma(r,X\_{r})\,\mathrm{d}W\_{r},\quad\text{for }t\in[0,s], and

|  |  |  |
| --- | --- | --- |
|  | ξ0​(s)=x0​(s)−∫0sfλ​(s−r)​x0​(r)​𝑑r+1λ​∫0sfλ​(s−r)​θ​(r)​dr.\xi\_{0}(s)=x\_{0}(s)-\int\_{0}^{s}f\_{\lambda}(s-r)x\_{0}(r)\,dr+\frac{1}{\lambda}\int\_{0}^{s}f\_{\lambda}(s-r)\theta(r)\,\mathrm{d}r. |  |

2. The inhomogeneous affine Volterra
process ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) satisfies the exponential-affine transformation formula for the Laplace
transform:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∫0TXT−s​μ​(d​s))]=exp⁡(∫0T𝔼x¯0​[XT−s]​μ​(d​s)+12​∫0Tς2​(s)​σ2​(𝔼x¯0​[Xs])​ψ2​(T−s,μ)​ds)\displaystyle\ \mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\int\_{0}^{T}X\_{T-s}\,\mu(\,\mathrm{d}s)\Bigg)\Bigg]=\exp\Bigg(\int\_{0}^{T}\mathbb{E}\_{\bar{x}\_{0}}[X\_{T-s}]\,\mu(\,\mathrm{d}s)+\frac{1}{2}\int\_{0}^{T}\varsigma^{2}(s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{s}])\,\psi^{2}(T-s,\mu)\,\,\mathrm{d}s\Bigg) |  | (3.29) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =exp⁡((x0∗μ)​(T)+(θ∗ψ​(⋅,μ))​(T)+∫0TF​(s,ψ​(T−s,μ))​x0​(s)​ds+κ02​∫0Tς2​(s)​ψ2​(T−s,μ)​ds).\displaystyle=\exp\Bigg((x\_{0}\*\mu)(T)+(\theta\*\psi(\cdot,\mu))(T)+\int\_{0}^{T}F(s,\psi(T-s,\mu))\,x\_{0}(s)\,\,\mathrm{d}s+\frac{\kappa\_{0}}{2}\int\_{0}^{T}\varsigma^{2}(s)\psi^{2}(T-s,\mu)\,\,\mathrm{d}s\Bigg). |  | (3.30) |

The main steps of the proof are sketched in Appendix [A](https://arxiv.org/html/2512.09590v1#A1 "Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), as the underlying strategy closely follows the approach developed in [[2](https://arxiv.org/html/2512.09590v1#bib.bib2), Theorem 4.3] for the convolution case and in [[3](https://arxiv.org/html/2512.09590v1#bib.bib3), Theorem 2.1] for the non-convolution and more general time-inhomogeneous setting.

###### Remark 3.7.

Note that the results of this section can be extended to any measure μ∈ℳ\mu\in\mathcal{M} (or μ∈ℳc\mu\in\mathcal{M}\_{c}, the subset of ℂ\mathbb{C}-valued locally finite measures) for which the associated measure-extended Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a unique global solution ψ=ψ​(⋅,μ)∈Lloc2​(ℝ+;ℝ)∩𝒞​([0,T],ℝ)\psi=\psi(\cdot,\mu)\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R})\cap\mathcal{C}([0,T],\mathbb{R}) (or ψ=ψ​(⋅,μ)∈Lloc2​(ℝ+;ℂ)∩𝒞​([0,T],ℂ)\psi=\psi(\cdot,\mu)\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{C})\cap\mathcal{C}([0,T],\mathbb{C})) for any T>0T>0, and for which the exponential affine representation ([3.29](https://arxiv.org/html/2512.09590v1#S3.E29 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([3.30](https://arxiv.org/html/2512.09590v1#S3.E30 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) hold.

Building upon the preceding results, we will established in section [5](https://arxiv.org/html/2512.09590v1#S5 "5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") that the time-shifted process (Xt+u)t≥0(X\_{t+u})\_{t\geq 0} converges in finite-dimensional distributions to a stationary444Stationary in the sense that its finite-dimensional distributions are invariant under time shifts. process as u→∞u\to\infty.
However, this limiting behavior does not imply that the original process XX is itself stationary, nor does it yield information about the dynamics of the limiting and stationary process, an aspect that remains an open and challenging problem. To address this gap, we now introduce a weaker yet analytically tractable framework: fake stationarity in the sense of [[35](https://arxiv.org/html/2512.09590v1#bib.bib35), [23](https://arxiv.org/html/2512.09590v1#bib.bib23)]. This notion allows us to capture key features of both the short- and long-term behavior of XX, despite the absence of full stationarity or explicit dynamical characterization of the limit. Note also that, this framework covers a wide range of kernels including
α−\alpha-gamma fractional integration kernel, with α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2}), where α≤1\alpha\leq 1 enters the regime of rough path whereas α>1\alpha>1 regularizes diffusion paths and invoke long-term memory, persistence or long range dependence (see. e.g. [[23](https://arxiv.org/html/2512.09590v1#bib.bib23)]).

## 4 Fake Stationarity Regimes of Affine Volterra Processes.

We consider the stochastic affine volterra integral equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) with the diffusion coefficient given in equation ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
As shown in [[35](https://arxiv.org/html/2512.09590v1#bib.bib35)] (and [[23](https://arxiv.org/html/2512.09590v1#bib.bib23)]), true Volterra equations with affine drift are never strongly stationary (i.e. in the classical sense, where the finite-dimensional distribution of the process is invariant under time shifts (see [[29](https://arxiv.org/html/2512.09590v1#bib.bib29)])). Alternative fake stationarity regimes are defined by the author, characterized through a functional equation satisfied by the stabilizing term (or corrector) ς=ςλ,c,λ,c>0\varsigma=\varsigma\_{\lambda,c},\;\lambda,c>0, which adjusts the volatility structure accordingly.

### 4.1 Stabilizer and Fake Stationarity Regimes.

###### Definition 4.1 (Fake Stationarity Regimes).

Let (Xt)t≥0(X\_{t})\_{t\geq 0} be a solution to the scaled Volterra equation in its form ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) starting from any X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}). Let σ​(t,x)=ς​(t)​σ​(x)\sigma(t,x)=\varsigma(t)\sigma(x) given in equation ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), where ς\varsigma is a (locally) bounded Borel function.

1. 1.

   The process (Xt)t≥0(X\_{t})\_{t\geq 0} exhibit a fake stationary regime of type I if it has constant mean, variance, and expected diffusion coefficient over time i.e.:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∀t≥0,𝔼​[Xt]=cste,Var​(Xt)=cste=v0≥0​and​σ¯2​(t):=𝔼​[σ2​(Xt)]=cste:=σ¯02≥0.\forall\,t\geq 0,\quad\mathbb{E}[X\_{t}]=\textit{c}^{\text{ste}},\quad\text{Var}(X\_{t})=\textit{c}^{\text{ste}}=v\_{0}\geq 0\quad\mbox{and}\quad\bar{\sigma}^{2}(t):=\mathbb{E}[\sigma^{2}(X\_{t})]=\textit{c}^{\text{ste}}:=\bar{\sigma}^{2}\_{0}\geq 0. |  | (4.31) |
2. 2.

   The process (Xt)t≥0(X\_{t})\_{t\geq 0} exhibit a fake stationary regime of type II if (Xt)t≥0(X\_{t})\_{t\geq 0} has the same marginal distribution, i.e., Xt​=𝑑​X0X\_{t}\overset{d}{=}X\_{0} for every t≥0t\geq 0.

The Proposition below shows what are the consequences of the three constraints in equation ([4.31](https://arxiv.org/html/2512.09590v1#S4.E31 "In item 1 ‣ Definition 4.1 (Fake Stationarity Regimes). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

###### Proposition 4.2 (Time-Dependent Volatility Coefficient.).

Let (Xt)t≥0(X\_{t})\_{t\geq 0} be a solution to the scaled Volterra equation in its form ([2.17](https://arxiv.org/html/2512.09590v1#S2.E17 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) starting from any random variable X0∈L2​(Ω,ℱ,ℙ)X\_{0}\in L^{2}(\Omega,\mathcal{F},\mathbb{P}), with λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}.
Then, a necessary and sufficient condition for the relations ([4.31](https://arxiv.org/html/2512.09590v1#S4.E31 "In item 1 ‣ Definition 4.1 (Fake Stationarity Regimes). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) to be satisfied is that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[X0]=1−a1−a​ϕ∞​μ∞λ:=x∞​and​∀t≥0,ϕ​(t)=1−λ​∫0tK​(t−s)​(θ​(s)λ​x∞−1)​ds.\displaystyle\ \mathbb{E}[X\_{0}]=\frac{1-a}{1-a\phi\_{\infty}}\frac{\mu\_{\infty}}{\lambda}:=x\_{\infty}\qquad\text{and}\qquad\forall\,t\geq 0,\qquad\phi(t)=1-\lambda\int\_{0}^{t}K(t-s)\left(\frac{\theta(s)}{\lambda x\_{\infty}}-1\right)\,\,\mathrm{d}s. |  | (4.32) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | so that ([2.17](https://arxiv.org/html/2512.09590v1#S2.E17 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) reads:​Xt=X0−1λ​x∞​(X0−x∞)​∫0tfλ​(t−s)​θ​(s)​ds+1λ​∫0tfλ​(t−s)​ς​(s)​σ​(Xs)​𝑑Ws.\displaystyle\text{so that\penalty 10000\ \eqref{eq:Volterrameanrevert2} reads:}\;X\_{t}=X\_{0}-\frac{1}{\lambda x\_{\infty}}\Big(X\_{0}-x\_{\infty}\Big)\int\_{0}^{t}f\_{\lambda}(t-s)\theta(s)\,\mathrm{d}s+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\varsigma(s)\sigma(X\_{s})dW\_{s}. |  | (4.33) |

and the triplet (v0,σ¯02,ς​(t))(v\_{0},\bar{\sigma}\_{0}^{2},\varsigma(t)), where v0=Var​(X0)v\_{0}=\text{Var}(X\_{0}) and σ¯02=𝔼​[σ2​(X0)]\bar{\sigma}\_{0}^{2}=\mathbb{E}[\sigma^{2}(X\_{0})], must satisfy the equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Eλ,c):∀t≥0,c​λ2​(1−(ϕ​(t)−(fλ∗ϕ)t)2)=(fλ2∗ς2)​(t)wherec=v0σ¯2and thusς=ςλ,c.\textit{($E\_{\lambda,c}$)}:\;\forall\,t\geq 0,\;c\lambda^{2}\big(1-(\phi(t)-(f\_{\lambda}\*\phi)\_{t})^{2}\big)=(f\_{\lambda}^{2}\*\varsigma^{2})(t)\quad\textit{where}\quad c=\frac{v\_{0}}{\bar{\sigma}^{2}}\quad\textit{and thus}\quad\varsigma=\varsigma\_{\lambda,c}. |  | (4.34) |

Proof : This follows from [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 3.4 and Theorem 3.5],
Remark that in this case, setting σ¯​(t):=𝔼​[σ2​(Xt)]\bar{\sigma}(t):=\mathbb{E}[\sigma^{2}(X\_{t})], the variance reads ∀t≥0\forall\,t\geq 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(Xt)=v0​(ϕ​(t)−(fλ∗ϕ)t)2+1λ2​(fλ2∗(ς​σ¯)2)​(t)=v0​(1−(fλ∗θ)tμ∞)2+1λ2​(fλ2∗(ς​σ¯)2)​(t).{\rm Var}(X\_{t})=v\_{0}\big(\phi(t)-(f\_{\lambda}\*\phi)\_{t}\big)^{2}+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*(\varsigma\bar{\sigma})^{2})(t)=v\_{0}\Big(1-\frac{(f\_{\lambda}\*\theta)\_{t}}{\mu\_{\infty}}\Big)^{2}+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*(\varsigma\bar{\sigma})^{2})(t). |  | (4.35) |

###### Definition 4.3.

We will call the stabilizer (or corrector) of the scaled stochastic Volterra equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) a (locally) bounded Borel function ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, which is a solution(if any) to the functional equation (Eλ,cE\_{\lambda,c}).

Remark on (Eλ,cE\_{\lambda,c}): If we introduce an antiderivative of −fλ2-f\_{\lambda}^{2}, namely R¯λ​(t)=∫t+∞fλ2​(s)​ds\bar{R}\_{\lambda}(t)=\int\_{t}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s
which goes to 0 as t→+∞t\to+\infty.
Then one derives by a straightforward integration by parts that Lfλ2​(t)=∫0+∞fλ2​(s)​ds−t​LR¯λ​(t)L\_{f^{2}\_{\lambda}}(t)=\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s-tL\_{\bar{R}\_{\lambda}}(t) so that

|  |  |  |
| --- | --- | --- |
|  | Lς2​(t)=c​λ2​L1−(ϕ−fλ∗ϕ)2​(t)∫0+∞fλ2​(s)​ds−t​LR¯λ​(t)=c​λ2∫0+∞fλ2​(s)​ds​L1−(ϕ−fλ∗ϕ)2⋅∑k≥0(t∫0+∞fλ2​(s)​ds)k​LR¯λk​(t).L\_{\varsigma^{2}}(t)=c\lambda^{2}\frac{L\_{1-(\phi-f\_{\lambda}\*\phi)^{2}}(t)}{\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s-tL\_{\bar{R}\_{\lambda}}(t)}=\frac{c\lambda^{2}}{\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s}L\_{1-(\phi-f\_{\lambda}\*\phi)^{2}}\cdot\sum\_{k\geq 0}\left(\frac{t}{\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s}\right)^{k}L\_{\bar{R}\_{\lambda}}^{k}(t). |  |

where the last equality comes from the fact that,
by definition,

|  |  |  |
| --- | --- | --- |
|  | LR¯λ​(t)=∫0+∞e−t​s​(∫s+∞fλ2​(u)​𝑑u)​ds=∫0+∞fλ2​(u)​(∫0ue−t​s​ds)​𝑑u=∫0+∞fλ2​(u)​1−e−t​ut​𝑑u.L\_{\bar{R}\_{\lambda}}(t)=\int\_{0}^{+\infty}e^{-ts}\left(\int\_{s}^{+\infty}f\_{\lambda}^{2}(u)\,du\right)\,\mathrm{d}s=\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\left(\int\_{0}^{u}e^{-ts}\,\,\mathrm{d}s\right)du=\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\,\frac{1-e^{-tu}}{t}\,du. |  |

owing to Fubini–Tonelli theorem, since the integrand is nonnegative, so that:

t​LR¯λ​(t)=∫0+∞fλ2​(s)​(1−e−t​s)​ds<∫0+∞fλ2​(s)​ds.t\,L\_{\bar{R}\_{\lambda}}(t)=\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,(1-e^{-ts})\,\,\mathrm{d}s<\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s.

Consequently, the function ς​(t)\varsigma(t) is entirely determined by that equation: it writes formally

|  |  |  |  |
| --- | --- | --- | --- |
|  | ς2​(t)=c​λ2∫0+∞fλ2​(s)​ds​(1−(ϕ−fλ∗ϕ)2)∗∑k≥0(−1)k​(fλ2∫0+∞fλ2​(s)​ds−δ0)∗k​(t).\varsigma^{2}(t)=\frac{c\lambda^{2}}{\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s}(1-(\phi-f\_{\lambda}\*\phi)^{2})\*\sum\_{k\geq 0}(-1)^{k}\left(\frac{f\_{\lambda}^{2}}{\int\_{0}^{+\infty}f\_{\lambda}^{2}(s)\,\,\mathrm{d}s}-\delta\_{0}\right)^{\*k}(t). |  | (4.36) |

without presuming the convergence of the serie in the right hand side, nor its sign.
However, for numerical purposes, we will use the expansion defines recursively in Proposition [6.1](https://arxiv.org/html/2512.09590v1#S6.ThmTheorem1 "Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.1 A Numerical illustration: The Fake Stationary Fractional-CIR Process. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (2).

From now on, we will assume that there exists a unique positive bounded Borel solution ς=ςλ,c\varsigma=\varsigma\_{\lambda,c} on (0,+∞)(0,+\infty) of the equation (Eλ,c)(E\_{\lambda,c}) above, so that, the corresponding time-inhomogeneous affine Volterra equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is refered to as a Stabilized affine Volterra equation or
as a Fake stationary affine Volterra equation if, in addition, equation ([4.32](https://arxiv.org/html/2512.09590v1#S4.E32 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) holds.

### 4.2 Fake stationary regimes of affine Volterra process and first asymptotics

We now come to the main result of this section.

###### Proposition 4.4 ((Fake stationary regimes (types I and II) and first asymptotics) ).

Let X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} be a one-dimensional solution of the stabilized Volterra equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) starting from any random variable X0X\_{0} defined on
(Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), with λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}, and a diffusion coefficient given by equation ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), where ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, assumed to be the unique continuous solution to Equation ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
for some c>0c>0 (so that condition (Eλ,cE\_{\lambda,c}) is satisfied).
If X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) is such that 𝔼​[X0]=x∞, given in ([4.33](https://arxiv.org/html/2512.09590v1#S4.E33 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and​Var​(X0)=v0\mathbb{E}[X\_{0}]=x\_{\infty},\;\text{ given in\penalty 10000\ \eqref{eq:ConstMean} and}\;\mathrm{Var}(X\_{0})=v\_{0}. Then, the resulting Volterra equation is such that:

1. 1.

   If the diffusion coefficient σ\sigma is degenerated in the sense that σ​(x∞)=0\sigma(x\_{\infty})=0, (in particular σ¯02=0\bar{\sigma}\_{0}^{2}=0 and v0=0v\_{0}=0) then the solution Xt=x∞X\_{t}=x\_{\infty} ℙ\mathbb{P}-a.s.a.s. represents a fake stationary regime (of type I).
2. 2.

   If σ2\sigma^{2} is constant (i.e. κ1=0\kappa\_{1}=0 or Volterra Ornstein-Uhlenbeck process with σ​(x)=κ0\sigma(x)=\sqrt{\kappa\_{0}}), then the solution (Xt)t≥0(X\_{t})\_{t\geq 0} has a constant mean x∞x\_{\infty} and variance v0v\_{0}. Consequently:

   * —

     The process exhibits a fake stationary regime of type I i.e.

     ∀t≥0,𝔼​[Xt]=x∞,Var​(Xt)=v0=c​κ0.\forall t\geq 0,\quad\mathbb{E}[X\_{t}]=x\_{\infty},\quad\text{Var}(X\_{t})=v\_{0}=c\kappa\_{0}.
   * —

     Furthermore, if X0∼ν∗:=𝒩​(x∞,v0)X\_{0}\sim\nu^{\*}:=\mathcal{N}\left(x\_{\infty},v\_{0}\right), this represents a fake stationary regime of type II, since in this case, Xt∼X0X\_{t}\sim X\_{0} for all t≥0t\geq 0. ((Xt)t≥0(X\_{t})\_{t\geq 0} is a Gaussian process with a fake stationary regime of type II. anyway.). ν∗\nu^{\*} is the 1-marginal distribution.
3. 3.

   If σ2\sigma^{2} is not constant and not degenerated, the solution (Xt)t≥0(X\_{t})\_{t\geq 0} to the Volterra equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) has a fake stationary regime of type I, in the sense that

   ∀t≥0,𝔼​[Xt]=x∞,Var​(Xt)=v0=c​σ2​(x∞),and​𝔼​[σ2​(Xt)]=σ¯02=σ2​(x∞).\forall\,t\geq 0,\quad\mathbb{E}[X\_{t}]=x\_{\infty},\;\text{Var}(X\_{t})=v\_{0}=c\sigma^{2}(x\_{\infty}),\;\text{and}\;\;\mathbb{E}[\sigma^{2}(X\_{t})]=\bar{\sigma}\_{0}^{2}=\sigma^{2}(x\_{\infty}).

Moreover if a=0a=0 or if ϕ∞=0\phi\_{\infty}=0, whenever a fake stationarity regime of type I is present, for any starting value X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) such that the ”right continuous left limits” (aka càdlàg)
solution XX of equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) satisfies equation ([5.48](https://arxiv.org/html/2512.09590v1#S5.E48 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), the following holds true :

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∃κ>0​such that ​∀c∈(0,1κ),𝔼​[Xt]→x∞,and​Var​(Xt)→v0=c​σ2​(x∞)​as​t→+∞.\exists\kappa>0\;\text{such that }\;\forall\,c\in(0,\frac{1}{\kappa}),\;\mathbb{E}[X\_{t}]\to x\_{\infty},\;\text{and}\;\text{Var}(X\_{t})\to v\_{0}=c\sigma^{2}(x\_{\infty})\;\text{as}\;t\to+\infty. |  | (4.37) |

Thus, the process X mixes: as time increases, the
random variable XtX\_{t} gradually loses memory of its initial its initial mean and variance, and approaches a limit of a Fake stationarity regime.

Remark On Inhomogeneous Volterra
square-root process:
In particular, if κ0=0\kappa\_{0}=0 , then σ​(x)=ν​x\sigma(x)=\nu\sqrt{x}, where ν=κ1\nu=\sqrt{\kappa\_{1}}.
The resulting Volterra equation has a fake stationary regime of type I, in the sense that

∀t≥0,𝔼​[Xt]=x∞,Var​(Xt)=v0=c​σ2​(x∞)=c​ν2​x∞,and​𝔼​[σ2​(Xt)]=σ¯02=σ2​(x∞)=ν2​x∞.\forall\,t\geq 0,\quad\mathbb{E}[X\_{t}]=x\_{\infty},\;\text{Var}(X\_{t})=v\_{0}=c\sigma^{2}(x\_{\infty})=c\nu^{2}x\_{\infty},\;\text{and}\;\;\mathbb{E}[\sigma^{2}(X\_{t})]=\bar{\sigma}\_{0}^{2}=\sigma^{2}(x\_{\infty})=\nu^{2}x\_{\infty}.

Proof of Proposition [4.4](https://arxiv.org/html/2512.09590v1#S4.ThmTheorem4 "Proposition 4.4 ((Fake stationary regimes (types I and II) and first asymptotics) ). ‣ 4.2 Fake stationary regimes of affine Volterra process and first asymptotics ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
Assuming that there exists at least a weak solution on the whole non-negative real line of Stochastic Voltera equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) with volatility term σ​(t,x)=ςλ,c​(t)​σ​(x)\sigma(t,x)=\varsigma\_{\lambda,c}(t)\sigma(x) given in ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) starting from any X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) such that 𝔼​[X0]=x∞\mathbb{E}[X\_{0}]=x\_{\infty} and V​a​r​[X0]=v0Var[X\_{0}]=v\_{0}, the results follows from [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 3.11 and Proposition 3.13]. Now, for equation ([4.37](https://arxiv.org/html/2512.09590v1#S4.E37 "In Proposition 4.4 ((Fake stationary regimes (types I and II) and first asymptotics) ). ‣ 4.2 Fake stationary regimes of affine Volterra process and first asymptotics ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), by assumption, any càdlàg
solution XX of equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) satisfies ℙ​(σ​(Xt)>0,∀t≥0)=1\mathbb{P}(\sigma(X\_{t})>0,\forall t\geq 0)=1 so that ∃κ¯>0\exists\bar{\kappa}>0 such that σ​(Xt)>κ¯∀t≥0\sigma(X\_{t})>\bar{\kappa}\quad\forall t\geq 0, and thus equation ([5.48](https://arxiv.org/html/2512.09590v1#S5.E48 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) holds with κ=κ124​κ¯2\kappa=\frac{\kappa\_{1}^{2}}{4\bar{\kappa}^{2}}. The claim follows directly from the Remark on Lipschitz L2L^{2}-Confluence in section [5.1](https://arxiv.org/html/2512.09590v1#S5.SS1 "5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). □\Box

### 4.3 The Fake stationary Volterra Heston model and its characteristic functions.

Without loss of generality, we work on ℂ\mathbb{C} and set: ℂ−={u∈ℂ:Re⁡(u)≤0}.\mathbb{C}\_{-}=\{u\in\mathbb{C}:\operatorname{Re}(u)\leq 0\}. Here we denote by ℳc−⊂ℳc\mathcal{M}^{-}\_{c}\subset\mathcal{M}\_{c} the subset of ℂ\mathbb{C}-valued locally finite measures μ∈ℳc\mu\in\mathcal{M}\_{c} such that Re⁡(μ)≤0\operatorname{Re}(\mu)\leq 0 and consider the equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) ∀μ∈ℳc\forall\,\mu\in\mathcal{M}\_{c}.

We now examine an affine Volterra process with state space ℝ×ℝ+\mathbb{R}\times\mathbb{R}\_{+}, which can be interpreted as an extension of the Volterra Heston [[2](https://arxiv.org/html/2512.09590v1#bib.bib2)] and the classical Heston [[25](https://arxiv.org/html/2512.09590v1#bib.bib25)] stochastic volatility model widely used in financial mathematics. It represents a special case of the more general inhomogeneous Volterra-Heston model introduced in [[3](https://arxiv.org/html/2512.09590v1#bib.bib3)], where the diffusion coefficient is time-dependent and separable in the state variable and time. Moreover, the time-dependent function ς\varsigma satisfies a functional equation ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
for some c>0c>0 (so that condition (Eλ,cE\_{\lambda,c}) is satisfied). We refer to this as the Fake stationary Volterra Heston model. In this setting, we define the process X=(log⁡S,V)X=(\log S,V), where SS denotes the asset price and VV its variance process, governed by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | d​StSt=Vt​(1−ρ2​d​Wt(1)+ρ​d​Wt(2)),S0∈(0,∞),\displaystyle\qquad\qquad\qquad\frac{dS\_{t}}{S\_{t}}=\sqrt{V\_{t}}\,(\sqrt{1-\rho^{2}}\,dW^{(1)}\_{t}+\rho\,dW^{(2)}\_{t}),\qquad S\_{0}\in(0,\infty), |  | (4.38) |
|  |  | Vt=V0ϕ(t)+∫0tKα(t−s)((θ(s)−λVs)ds+νς(s)VsdWs(2)),V0⟂⟂W,ς=ςλ,c.\displaystyle V\_{t}=V\_{0}\phi(t)+\int\_{0}^{t}K\_{\alpha}(t-s)\left((\theta(s)-\lambda V\_{s})ds+\nu\varsigma(s)\sqrt{V\_{s}}\,dW^{(2)}\_{s}\right),V\_{0}\perp\!\!\!\perp W,\qquad\varsigma=\varsigma\_{\lambda,c}. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,ϕ​(t)=1−λ​∫0tKα​(t−s)​(θ​(s)λ​x∞−1)​ds,c​λ2​(1−(ϕ​(t)−(fα,λ∗ϕ)t)2)=(fα,λ2∗ςα,λ,c2)​(t).\forall\,t\geq 0,\,\phi(t)=1-\lambda\int\_{0}^{t}K\_{\alpha}(t-s)\left(\frac{\theta(s)}{\lambda x\_{\infty}}-1\right)\,\,\mathrm{d}s,\;\;c\lambda^{2}\big(1-(\phi(t)-(f\_{\alpha,\lambda}\*\phi)\_{t})^{2}\big)=(f\_{\alpha,\lambda}^{2}\*\varsigma\_{\alpha,\lambda,c}^{2})(t). |  | (4.39) |

where the kernel KαK\_{\alpha} lies in Lloc2​(ℝ+,ℝ)L^{2}\_{\rm loc}(\mathbb{R}\_{+},\mathbb{R}), W=(W1,W2)W=(W\_{1},W\_{2}) is a two-dimensional standard Brownian motion with correlation ρ∈[−1,1]\rho\in[-1,1], and the θ\theta a deterministic function, λ,ν∈ℝ+\lambda,\nu\in\mathbb{R}\_{+} such that VV is at least a weak solution to the Volterra equation ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). More precisely, the process VV in ([4.38](https://arxiv.org/html/2512.09590v1#S4.E38 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) can be rewritten:

|  |  |  |
| --- | --- | --- |
|  | Vt=V0−1λ​x∞(V0−x∞)∫0tfα,λ(t−s)θ(s)ds+1λ∫0tfα,λ(t−s)ςα,λ,c(s)VsdWs(2),λ,ςα,λ,c(t),≥0.V\_{t}=V\_{0}-\frac{1}{\lambda x\_{\infty}}\Big(V\_{0}-x\_{\infty}\Big)\int\_{0}^{t}f\_{\alpha,\lambda}(t-s)\theta(s)\,\mathrm{d}s+\frac{1}{\lambda}\int\_{0}^{t}f\_{\alpha,\lambda}(t-s)\varsigma\_{\alpha,\lambda,c}(s)\,\sqrt{V\_{s}}dW^{(2)}\_{s},\quad\lambda\;,\varsigma\_{\alpha,\lambda,c}(t),\geq 0. |  |

Note that the joint dynamics in equation ([4.38](https://arxiv.org/html/2512.09590v1#S4.E38 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) for the asset’s price process
SS (e.g., the SPX) and its spot variance are expressed in this form (risk-neutral prices) because
volatility models are typically formulated in terms of the so-called forward prices, that is,
the process Ft=e(r−q)​t​StF\_{t}=e^{(r-q)t}S\_{t}.

Once VV is determined, the asset price process SS follows accordingly. Moreover by applying Itô’s formula, one can verify that for every t∈[0,T]t\in[0,T], the log-price process satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(St)=log⁡(S0)+∫0tVs​(1−ρ2​d​Ws(1)+ρ​d​Ws(2))−∫0tVs2​ds.\log(S\_{t})=\log(S\_{0})+\int\_{0}^{t}\sqrt{V\_{s}}\left(\sqrt{1-\rho^{2}}dW^{(1)}\_{s}+\rho dW^{(2)}\_{s}\right)-\int\_{0}^{t}\frac{V\_{s}}{2}\,\mathrm{d}s. |  | (4.40) |

Hence, X=(log⁡S,V)X=(\log S,V) constitutes an affine Volterra process which evolves according to the system

|  |  |  |  |
| --- | --- | --- | --- |
|  | (log⁡(St)Vt)=(log⁡(S0)V0​ϕ​(t))+∫0t(100Kα​(t−u))​[(0θ​(u))+(00)​log⁡(Su)+(−12−λ)​Vu]​𝑑u+∫0t(100Kα​(t−u))​(1−ρ2ρ0ν​ς​(u))​Vu​𝑑Wu,t∈[0,T],ς=ςλ,c.\begin{split}\begin{pmatrix}\log(S\_{t})\\ V\_{t}\end{pmatrix}&=\begin{pmatrix}\log(S\_{0})\\ V\_{0}\phi(t)\end{pmatrix}+\int\_{0}^{t}\begin{pmatrix}1&0\\ 0&K\_{\alpha}(t-u)\end{pmatrix}\left[\begin{pmatrix}0\\ \theta(u)\end{pmatrix}+\begin{pmatrix}0\\ 0\end{pmatrix}\log(S\_{u})+\begin{pmatrix}-\frac{1}{2}\\ -\lambda\end{pmatrix}V\_{u}\right]du\\ &\quad+\int\_{0}^{t}\begin{pmatrix}1&0\\ 0&K\_{\alpha}(t-u)\end{pmatrix}\begin{pmatrix}\sqrt{1-\rho^{2}}&\rho\\ 0&\nu\varsigma(u)\end{pmatrix}\sqrt{V\_{u}}\,dW\_{u},\quad t\in[0,T],\,\quad\varsigma=\varsigma\_{\lambda,c}.\end{split} |  | (4.41) |

We thus obtain that for the fake stationary Volterra-Heston model the Riccati-Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) with μ∈ℳc\mu\in\mathcal{M}\_{c} given by μ​(d​s)=u​δ0​(d​s)+f​(s)​λ1​(d​s)\mu(\,\mathrm{d}s)=u\,\delta\_{0}(\,\mathrm{d}s)+f(s)\lambda\_{1}(\,\mathrm{d}s)555λ1\lambda\_{1} denotes the Lebesgue measure on (ℝ,ℬ​o​r​(ℝ))(\mathbb{R},{\cal B}or(\mathbb{R})), in dimension 2, for any u∈(ℂ2)∗u\in(\mathbb{C}^{2})^{\*} and f∈L1​([0,T],(ℂ2)∗)f\in L^{1}\left([0,T],(\mathbb{C}^{2})^{\*}\right) (see also [[3](https://arxiv.org/html/2512.09590v1#bib.bib3), Equation 12]) takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ1​(t)=u1+∫0tf1​(s)​ds,ψ2​(t)=u2Kα(t)+∫0tKα(t−s)(f2(s)+12(ψ12(s)−ψ1(s))+(ρνς(T−s)ψ1(s)−λ)ψ2(s)+ν22ς2(T−s)ψ22(s))ds,t∈[0,T],ς=ςλ,c.\begin{split}\psi\_{1}(t)&=u\_{1}+\int\_{0}^{t}f\_{1}(s)\,\mathrm{d}s,\\ \psi\_{2}(t)&=u\_{2}K\_{\alpha}(t)+\int\_{0}^{t}K\_{\alpha}(t-s)\;\Big(f\_{2}(s)+\frac{1}{2}(\psi^{2}\_{1}(s)-\psi\_{1}(s))\\ &\quad+\left(\rho\nu\varsigma(T-s)\psi\_{1}(s)-\lambda\right)\psi\_{2}(s)+\frac{\nu^{2}}{2}\varsigma^{2}(T-s)\psi\_{2}^{2}(s)\Big)\,\mathrm{d}s,\quad t\in[0,T],\,\quad\varsigma=\varsigma\_{\lambda,c}.\end{split} |  | (4.42) |

###### Proposition 4.5.

Suppose that KαK\_{\alpha} satisfies condition ([2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))(i).
Consider a fake stationary Volterra Equation with λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}, where ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, assumed to be the unique continuous solution to Equation ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
for some c>0c>0 (so that condition (Eλ,cE\_{\lambda,c}) is satisfied).

1. 1.

   The stochastic Volterra system ([4.38](https://arxiv.org/html/2512.09590v1#S4.E38 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a [0,+∞)−[0,+\infty)-valued unique in law
   continuous weak solution (log⁡S,V)(\log S,V) with values in ℝ×ℝ+\mathbb{R}\times\mathbb{R}\_{+}, for any initial state (log⁡S0,V¯0)∈ℝ×ℝ+(\log S\_{0},\bar{V}\_{0})\in\mathbb{R}\times\mathbb{R}\_{+}. Moreover, the sample paths of VV are (δ∧ϑ∧θ^−1p−η)\left(\delta\wedge\vartheta\wedge\widehat{\theta}-\frac{1}{p}-\eta\right)-Hölder pathwise continuous (modulo PP-indistinguability) for sufficiently small η>0\eta>0.
2. 2.

   Let u∈(ℂ2)∗u\in(\mathbb{C}^{2})^{\*} and f∈Lloc1​(ℝ+,(ℂ2)∗)f\in L^{1}\_{\rm loc}(\mathbb{R}\_{+},(\mathbb{C}^{2})^{\*}) such that Re​ψ1∈[0,1]{\rm Re\,}\psi\_{1}\in[0,1], Re​u2≤0{\rm Re\,}u\_{2}\leq 0, and Re​f2≤0{\rm Re\,}f\_{2}\leq 0.
   where ψ1\psi\_{1} solves the first relation in ([4.42](https://arxiv.org/html/2512.09590v1#S4.E42 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). Then the second equation of the Riccati–Volterra equation ([4.42](https://arxiv.org/html/2512.09590v1#S4.E42 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a unique global solution ψ2∈Lloc2​(ℝ+,ℂ∗)\psi\_{2}\in L^{2}\_{\rm loc}(\mathbb{R}\_{+},\mathbb{C}^{\*}) with Re​ψ2≤0{\rm Re\,}\psi\_{2}\leq 0. Furthermore, the exponential-affine representation ([3.30](https://arxiv.org/html/2512.09590v1#S3.E30 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is valid for (log⁡S,V)(\log S,V) for any initial state (log⁡S0,V¯0)∈ℝ×ℝ+(\log S\_{0},\bar{V}\_{0})\in\mathbb{R}\times\mathbb{R}\_{+} with ℳc∋μ​(d​s):=u​δ0​(d​s)+f​(s)​λ1​(d​s)\mathcal{M}\_{c}\ni\mu(\,\mathrm{d}s):=u\,\delta\_{0}(\,\mathrm{d}s)+f(s)\lambda\_{1}(\,\mathrm{d}s).
3. 3.

   The process SS solution of the first equation in ([4.38](https://arxiv.org/html/2512.09590v1#S4.E38 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is a true martingale and can be written:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | St=S0​exp⁡(−∫0tVs2​ds+∫0tVs​(1−ρ2​d​Ws(1)+ρ​d​Ws(2))),t∈[0,T].S\_{t}=S\_{0}\exp\left(-\int\_{0}^{t}\frac{V\_{s}}{2}\,\mathrm{d}s+\int\_{0}^{t}\sqrt{V\_{s}}\left(\sqrt{1-\rho^{2}}dW^{(1)}\_{s}+\rho dW^{(2)}\_{s}\right)\right),\quad t\in[0,T]. |  | (4.43) |

The preceding results allow us to derive the Fourier–Laplace transform at time zero for the Fake stationary Volterra-Heston model with fractional integration kernel.
Such kernels are particularly relevant in capturing either the short or the long-term memory of volatility phenomena, as seen for instance in the rough Heston model ([[31](https://arxiv.org/html/2512.09590v1#bib.bib31)], [[13](https://arxiv.org/html/2512.09590v1#bib.bib13)] and [[14](https://arxiv.org/html/2512.09590v1#bib.bib14)]). The next result extends those of [[16](https://arxiv.org/html/2512.09590v1#bib.bib16)], [[15](https://arxiv.org/html/2512.09590v1#bib.bib15)] and [[2](https://arxiv.org/html/2512.09590v1#bib.bib2), Example 7.2] by incorporating time-dependent drift θ​(⋅)\theta(\cdot) and diffusion coefficient ς​(⋅)​σ​(⋅)\varsigma(\cdot)\sigma(\cdot).
Consider (log⁡S0,V¯0)∈ℝ×ℝ+(\log S\_{0},\bar{V}\_{0})\in\mathbb{R}\times\mathbb{R}\_{+}, any initial state of the Volterra system ([4.38](https://arxiv.org/html/2512.09590v1#S4.E38 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

###### Corollary 4.6 (Fake stationary Rough Heston model).

Let α∈(12,1)\alpha\in(\frac{1}{2},1), and consider the α−\alpha- fractional integration kernel Kα​(t)=tα−1Γ​(α)K\_{\alpha}(t)=\frac{t^{\alpha-1}}{\Gamma(\alpha)} for t∈(0,T]t\in(0,T].
Suppose u∈(ℂ2)∗u\in(\mathbb{C}^{2})^{\*} and f∈L1​([0,T],(ℂ2)∗)f\in L^{1}\left([0,T],(\mathbb{C}^{2})^{\*}\right) satisfy the conditions ℜ⁡ψ1∈[0,1]\Re\psi\_{1}\in[0,1], ℜ⁡u2≤0\Re u\_{2}\leq 0, and ℜ⁡f2≤0\Re f\_{2}\leq 0, where ψ1=u1+∫0⋅f1​(s)​ds\psi\_{1}=u\_{1}+\int\_{0}^{\cdot}f\_{1}(s)\,\,\mathrm{d}s. Then there exists a unique function ψ2∈L2​([0,T],ℂ)\psi\_{2}\in L^{2}([0,T],\mathbb{C}) solving the fractional Riccati equation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (Dα​ψ2)​(t)=f2​(t)+12​(u12−u1+2​u1​∫0tf1​(s)​ds+(∫0tf1​(s)​ds)2)+ν22​ς2​(T−t)​ψ22​(t)\displaystyle\ (D^{\alpha}\psi\_{2})(t)=f\_{2}(t)+\frac{1}{2}\left(u\_{1}^{2}-u\_{1}+2u\_{1}\int\_{0}^{t}f\_{1}(s)\,\,\mathrm{d}s+\left(\int\_{0}^{t}f\_{1}(s)\,\,\mathrm{d}s\right)^{2}\right)+\frac{\nu^{2}}{2}\varsigma^{2}(T-t)\,\psi\_{2}^{2}(t) |  | (4.44) |
|  |  | +(ρ​ν​ς​(T−t)​(u1+∫0tf1​(s)​ds)−λ)​ψ2​(t),t∈[0,T],ς=ςλ,c,(I1−α​ψ2)​(0)=u2.\displaystyle\qquad+\left(\rho\nu\varsigma(T-t)\left(u\_{1}+\int\_{0}^{t}f\_{1}(s)\,\,\mathrm{d}s\right)-\lambda\right)\psi\_{2}(t),\quad t\in[0,T],\;\varsigma=\varsigma\_{\lambda,c},\;(I^{1-\alpha}\psi\_{2})(0)=u\_{2}. |  |

leading to the full Fourier–Laplace representation for the integrated log-price and variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼(log⁡(S0),V¯0)​[exp⁡(u1​log⁡(ST)+u2​VT+∫0Tf1​(T−u)​log⁡(Su)​𝑑u+∫0Tf2​(T−u)​Vu​𝑑u)]=exp⁡(φ​(T)+(u1+∫0Tf1​(s)​ds)​log⁡(S0)+((I1−α​ψ2)​(T)−λ​∫0T(θ​(u)λ​x∞−1)​ψ2​(T−u)​𝑑u)​V¯0).\begin{split}&\mathbb{E}\_{(\log(S\_{0}),\bar{V}\_{0})}\left[\exp\left(u\_{1}\log(S\_{T})+u\_{2}V\_{T}+\int\_{0}^{T}f\_{1}(T-u)\log(S\_{u})\,du+\int\_{0}^{T}f\_{2}(T-u)V\_{u}\,du\right)\right]\\ &=\exp\left(\varphi(T)+\left(u\_{1}+\int\_{0}^{T}f\_{1}(s)\,\,\mathrm{d}s\right)\log(S\_{0})+\left((I^{1-\alpha}\psi\_{2})(T)-\lambda\int\_{0}^{T}\Big(\frac{\theta(u)}{\lambda x\_{\infty}}-1\Big)\psi\_{2}(T-u)\,du\right)\bar{V}\_{0}\right).\end{split} |  | (4.45) |

with φ\varphi defined as ,∀t∈[0,T],φ(t)=∫0tθ(s)ψ2(t−s)ds,\forall\,t\in[0,T],\;\varphi(t)=\int\_{0}^{t}\theta(s)\psi\_{2}(t-s)\,\,\mathrm{d}s, φ​(0)=0\varphi(0)=0 and Dα=dd​t​I1−αD^{\alpha}=\frac{d}{dt}I^{1-\alpha} where DαD^{\alpha} and I1−αI^{1-\alpha} denote, respectively, the Riemann–Liouville fractional derivative of order α\alpha, and the Riemann–Liouville fractional integral of order 1−α1-\alpha (see [[41](https://arxiv.org/html/2512.09590v1#bib.bib41), Chapter 2]).
In the particular case where θ​(t)=θ0=λ​x∞​∀t≥0\theta(t)=\theta\_{0}=\lambda x\_{\infty}\;\forall t\geq 0 (so that ϕ≡1\phi\equiv 1), 666As a necessary and sufficient condition for the process to have a constant mean (see Section [4.1](https://arxiv.org/html/2512.09590v1#S4.SS1 "4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")),
the above Fourier–Laplace representation simplifies to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼(log⁡(S0),V¯0)​[exp⁡(u1​log⁡(ST)+u2​VT+∫0Tf1​(T−u)​log⁡(Su)​𝑑u+∫0Tf2​(T−u)​Vu​𝑑u)]=exp⁡(φ​(T)+(u1+∫0Tf1​(s)​ds)​log⁡(S0)+(I1−α​ψ2)​(T)​V¯0).\begin{split}&\mathbb{E}\_{(\log(S\_{0}),\bar{V}\_{0})}\left[\exp\left(u\_{1}\log(S\_{T})+u\_{2}V\_{T}+\int\_{0}^{T}f\_{1}(T-u)\log(S\_{u})\,du+\int\_{0}^{T}f\_{2}(T-u)V\_{u}\,du\right)\right]\\ &=\exp\left(\varphi(T)+\left(u\_{1}+\int\_{0}^{T}f\_{1}(s)\,\,\mathrm{d}s\right)\log(S\_{0})+(I^{1-\alpha}\psi\_{2})(T)\bar{V}\_{0}\right).\end{split} |  | (4.46) |

Practitionner corner: On numerical Approximation of the the so-called inhomogeneous Riccati equations.
It is worth noting that the characteristic function of the fake stationary rough Heston model introduced above can be computed by solving ordinary differential or integral equations, specifically the so-called Riccati equations.
See, for instance, the pioneering work [[7](https://arxiv.org/html/2512.09590v1#bib.bib7)], which develops fast hybrid schemes for the numerical approximation of such equations. This methodology can be adapted to the inhomogeneous setting, by introducing the stabilizer ςα,λ,c\varsigma\_{\alpha,\lambda,c} mutatis mutandis.
Plug the numerical solution of the riccati equation, into ([4.46](https://arxiv.org/html/2512.09590v1#S4.E46 "In Corollary 4.6 (Fake stationary Rough Heston model). ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), to obtain the characteristic function. Then, classical methods can be applied to compute call (resp. put) option prices
C​(St,K,T)=exp⁡(−r​(T−t))​𝔼ℚ​[(ST−K)+|ℱt]C(S\_{t},K,T)=\exp(-r(T-t))\mathbb{E}^{\mathbb{Q}}[(S\_{T}-K)^{+}|\mathcal{F}\_{t}] (resp. P​(St,K,T)=exp⁡(−r​(T−t))​𝔼ℚ​[(K−ST)+|ℱt]P(S\_{t},K,T)=\exp(-r(T-t))\mathbb{E}^{\mathbb{Q}}[(K-S\_{T})^{+}|\mathcal{F}\_{t}]); see [[9](https://arxiv.org/html/2512.09590v1#bib.bib9), [34](https://arxiv.org/html/2512.09590v1#bib.bib34), [26](https://arxiv.org/html/2512.09590v1#bib.bib26)] and the survey [[40](https://arxiv.org/html/2512.09590v1#bib.bib40)].

Proof of Corollary [4.6](https://arxiv.org/html/2512.09590v1#S4.ThmTheorem6 "Corollary 4.6 (Fake stationary Rough Heston model). ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
Indeed, the fake stationary rough Heston model arises as a specific instance of the inhomogeneous Volterra-Heston framework analyzed in [[3](https://arxiv.org/html/2512.09590v1#bib.bib3), Corollary 4.5.] when the volatility coefficient is constant, i.e., η​(t)≡1\eta(t)\equiv 1, the parameters θ\theta, and σ​(⋅,⋅)\sigma(\cdot,\cdot) are time-dependent, and the kernel is chosen to be fractional.
Consider ℳc∋μ​(d​s):=u​δ0​(d​s)+f​(s)​λ1​(d​s)\mathcal{M}\_{c}\ni\mu(\,\mathrm{d}s):=u\,\delta\_{0}(\,\mathrm{d}s)+f(s)\lambda\_{1}(\,\mathrm{d}s), the existence follows from the second claim of Proposition [4.5](https://arxiv.org/html/2512.09590v1#S4.ThmTheorem5 "Proposition 4.5. ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
Consequently, formula in equation ([3.30](https://arxiv.org/html/2512.09590v1#S3.E30 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) of Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (b) applies for (log⁡S,V)(\log S,V) (see Remark [3.7](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem7 "Remark 3.7. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and yields the expression in ([4.45](https://arxiv.org/html/2512.09590v1#S4.E45 "In Corollary 4.6 (Fake stationary Rough Heston model). ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) since on the first hand:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0TF​(s,ψ​(T−s))​[log⁡(S0)V¯0​ϕ​(s)]​ds\displaystyle\int\_{0}^{T}F(s,\psi(T-s))\,\begin{bmatrix}\log(S\_{0})\\ \bar{V}\_{0}\phi(s)\end{bmatrix}\,\,\mathrm{d}s | =∫0T[log⁡(S0)V0​ϕ​(T−s)]​(ψ​(s)​[0−120−λ]+12​[0ψ​(s)​A​A⊤​ψ⊤​(s)])​ds\displaystyle=\int\_{0}^{T}\begin{bmatrix}\log(S\_{0})&V\_{0}\phi(T-s)\end{bmatrix}\left(\psi(s)\begin{bmatrix}0&-\frac{1}{2}\\ 0&-\lambda\end{bmatrix}+\frac{1}{2}\begin{bmatrix}0\\ \psi(s)AA^{\top}\psi^{\top}(s)\end{bmatrix}\right)\,\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =χ​(T)​V¯0\displaystyle=\chi(T)\bar{V}\_{0} |  |

where A=A​(T−s)=(1−ρ2ρ0ν​ς​(T−s))A=A(T-s)=\begin{pmatrix}\sqrt{1-\rho^{2}}&\rho\\
0&\nu\varsigma(T-s)\end{pmatrix}, so that on the second hand, the full Fourier–Laplace representation for the integrated log-price and variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼(log⁡(S0),V¯0)​[exp⁡(u1​log⁡(ST)+u2​VT+∫0Tf1​(T−u)​log⁡(Su)​𝑑u+∫0Tf2​(T−u)​Vu​𝑑u)]=exp⁡(φ​(T)+(u1+∫0Tf1​(s)​ds)​log⁡(S0)+(u2​ϕ​(T)+∫0Tf2​(T−s)​ϕ​(s)​ds+χ​(T))​V¯0).\displaystyle\begin{split}&\mathbb{E}\_{(\log(S\_{0}),\bar{V}\_{0})}\left[\exp\left(u\_{1}\log(S\_{T})+u\_{2}V\_{T}+\int\_{0}^{T}f\_{1}(T-u)\log(S\_{u})\,du+\int\_{0}^{T}f\_{2}(T-u)V\_{u}\,du\right)\right]\\ &=\exp\left(\varphi(T)+\left(u\_{1}+\int\_{0}^{T}f\_{1}(s)\,\,\mathrm{d}s\right)\log(S\_{0})+\left(u\_{2}\,\phi(T)+\int\_{0}^{T}f\_{2}(T-s)\,\phi(s)\,\,\mathrm{d}s+\chi(T)\right)\bar{V}\_{0}\right).\end{split} | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∀t∈[0,T],χ​(t)=∫0tϕ​(t−s)​(12​(ψ12​(s)−ψ1​(s))+(ρ​ν​ς​(t−s)​ψ1​(s)−λ)​ψ2​(s)+ν22​ς2​(t−s)​ψ22​(s))​ds,\displaystyle\ \forall\,t\in[0,T],\;\chi(t)=\int\_{0}^{t}\phi(t-s)\;\Big(\frac{1}{2}(\psi^{2}\_{1}(s)-\psi\_{1}(s))+\left(\rho\nu\varsigma(t-s)\psi\_{1}(s)-\lambda\right)\psi\_{2}(s)+\frac{\nu^{2}}{2}\varsigma^{2}(t-s)\psi\_{2}^{2}(s)\Big)\,\mathrm{d}s, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t(12(ψ12(s)−ψ1(s))+(ρνς(t−s)ψ1(s)−λ)ψ2(s)+ν22ς2(t−s)ψ22(s))ds−λ[∫0t(θ​(u)λ​x∞−1)\displaystyle\quad\quad=\int\_{0}^{t}\Big(\frac{1}{2}(\psi^{2}\_{1}(s)-\psi\_{1}(s))+\left(\rho\nu\varsigma(t-s)\psi\_{1}(s)-\lambda\right)\psi\_{2}(s)+\frac{\nu^{2}}{2}\varsigma^{2}(t-s)\psi\_{2}^{2}(s)\Big)\,\mathrm{d}s-\lambda\Bigg[\int\_{0}^{t}\Big(\frac{\theta(u)}{\lambda x\_{\infty}}-1\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(∫0t−uKα(t−u−s)(12(ψ12(s)−ψ1(s))+(ρνς(t−s)ψ1(s)−λ)ψ2(s)+ν22ς2(t−s)ψ22(s))ds)du].\displaystyle\quad\times\Bigg(\int\_{0}^{t-u}K\_{\alpha}(t-u-s)\Big(\frac{1}{2}(\psi\_{1}^{2}(s)-\psi\_{1}(s))+(\rho\nu\varsigma(t-s)\psi\_{1}(s)-\lambda)\psi\_{2}(s)+\frac{\nu^{2}}{2}\varsigma^{2}(t-s)\psi\_{2}^{2}(s)\Big)\,\mathrm{d}s\Bigg)du\Bigg]. |  |

where we used the fact that ϕ​(t)=1−λ​∫0tKα​(t−s)​(θ​(s)λ​x∞−1)​ds,\phi(t)=1-\lambda\int\_{0}^{t}K\_{\alpha}(t-s)\left(\frac{\theta(s)}{\lambda x\_{\infty}}-1\right)\,\,\mathrm{d}s,\;
together with Fubini-Tonelli’s theorem and a change of variables, so that we have

|  |  |  |
| --- | --- | --- |
|  | u2​ϕ​(t)+∫0tf2​(t−s)​ϕ​(s)​ds+χ​(t)=(I1−α​ψ2)​(t)\displaystyle\,u\_{2}\,\phi(t)+\int\_{0}^{t}f\_{2}(t-s)\,\phi(s)\,\,\mathrm{d}s+\chi(t)=(I^{1-\alpha}\psi\_{2})(t) |  |
|  |  |  |
| --- | --- | --- |
|  | −λ[∫0t(θ​(u)λ​x∞−1)(u2Kα(t−u)+∫0t−uKα(t−u−s)f2(s)ϕ(s)ds\displaystyle\qquad\qquad\qquad-\lambda\Bigg[\int\_{0}^{t}\Big(\frac{\theta(u)}{\lambda x\_{\infty}}-1\Big)\Bigg(u\_{2}\,K\_{\alpha}(t-u)+\int\_{0}^{t-u}K\_{\alpha}(t-u-s)f\_{2}(s)\,\phi(s)\,\,\mathrm{d}s |  |
|  |  |  |
| --- | --- | --- |
|  | +∫0t−uKα(t−u−s)(12(ψ12(s)−ψ1(s))+(ρνς(t−s)ψ1(s)−λ)ψ2(s)+ν22ς2(t−s)ψ22(s))ds)du]\displaystyle\quad+\int\_{0}^{t-u}K\_{\alpha}(t-u-s)\Big(\frac{1}{2}(\psi\_{1}^{2}(s)-\psi\_{1}(s))+(\rho\nu\varsigma(t-s)\psi\_{1}(s)-\lambda)\psi\_{2}(s)+\frac{\nu^{2}}{2}\varsigma^{2}(t-s)\psi\_{2}^{2}(s)\Big)\,\mathrm{d}s\Bigg)du\Bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =(I1−α​ψ2)​(t)−λ​∫0t(θ​(u)λ​x∞−1)​ψ2​(t−u)​𝑑u.\displaystyle\qquad\qquad\qquad=(I^{1-\alpha}\psi\_{2})(t)-\lambda\int\_{0}^{t}\Big(\frac{\theta(u)}{\lambda x\_{\infty}}-1\Big)\psi\_{2}(t-u)\,du. |  |

still owing to Fubini-Tonelli’s theorem.
The expression in ([4.46](https://arxiv.org/html/2512.09590v1#S4.E46 "In Corollary 4.6 (Fake stationary Rough Heston model). ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) follows directly from standard results in fractional calculus, in conjunction with equation ([4.42](https://arxiv.org/html/2512.09590v1#S4.E42 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
□\square

## 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics

### 5.1 γ\gamma-Hölder L2L^{2}-Contraction

Let (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X^{\prime}\_{t})\_{t\geq 0} be two solutions of the Volterra stochastic equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) with initial conditions X0,X0′∈L2​(ℙ)X\_{0},X^{\prime}\_{0}\in L^{2}(\mathbb{P}).
Owing to assumption [2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (iii) and the concavity of x→xγx\to x^{\gamma} for all γ∈[0,1]\gamma\in[0,1], ∃[σ]Höl2>0\exists\;[\sigma]^{2}\_{\text{H\"{o}l}}>0 such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|σ​(Xs)−σ​(Xs′)|2]≤[σ]Höl2​𝔼​[|Xs−Xs′|2]γ.\mathbb{E}\left[|\sigma(X\_{s})-\sigma(X^{\prime}\_{s})|^{2}\right]\leq[\sigma]^{2}\_{\text{H\"{o}l}}\mathbb{E}\left[|X\_{s}-X^{\prime}\_{s}|^{2}\right]^{\gamma}. |  | (5.47) |

###### Proposition 5.1 (γ\gamma-Hölder L2L^{2}-Contraction).

Assume assumption ([2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) (ii) so that equation ([5.47](https://arxiv.org/html/2512.09590v1#S5.E47 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) holds. Assume fλ∈L2​(ℝ+,Leb1)f\_{\lambda}\!\in L^{2}(\mathbb{R}\_{+},\text{Leb}\_{1}), σ​(t,x):=ς​(t)​σ​(x)\sigma(t,x):=\varsigma(t)\sigma(x) where ς=ςλ,c\varsigma=\varsigma\_{\lambda,c} is a non-negative, continuous and (locally) bounded solution to ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) for some fixed λ,c>0\lambda,c>0 (i.e. Eλ,cE\_{\lambda,c} is in force).
For X0,X0′∈L2​(ℙ)X\_{0},X^{\prime}\_{0}\!\in L^{2}({\mathbb{P}}), we consider the solutions to the time-inhomogeneous affine Volterra equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) denoted (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X^{\prime}\_{t})\_{t\geq 0} starting from X0X\_{0} and X0′X^{\prime}\_{0} respectively.
For c∈(0,1[σ]Höl2)c\!\in\big(0,\frac{1}{[\sigma]^{2}\_{\text{H\"{o}l}}}\big), set ρ:=c​[σ]Höl2\rho:=c[\sigma]^{2}\_{\text{H\"{o}l}}. Then, one has:

* (a)

  (γ\gamma-Hölder L2L^{2}-Contraction): There exists a continuous non-negative function φ∞:ℝ+→[0,1]\varphi\_{\infty}:\mathbb{R}^{+}\to[0,1],
  such that φ∞​(0)=1\varphi\_{\infty}(0)=1, limt→+∞φ∞​(t)={ℓ∞∗:=a2​ϕ∞21−ρ​(1−a2​ϕ∞2)​ if ​γ=1ℓ∞∈]ℓ∞∗,(ρ​(1−a2​ϕ∞2)+ρ2​(1−a2​ϕ∞2)+4​a2​ϕ∞2)24] if γ∈[12,1[.\lim\_{t\to+\infty}\varphi\_{\infty}(t)=\left\{\begin{array}[]{ll}&\ell\_{\infty}^{\*}:=\frac{a^{2}\phi\_{\infty}^{2}}{1-\rho(1-a^{2}\phi\_{\infty}^{2})}\text{ if }\gamma=1\\
  &\ell\_{\infty}\in]\ell\_{\infty}^{\*},\frac{\left(\rho(1-a^{2}\phi\_{\infty}^{2})+\sqrt{\rho^{2}(1-a^{2}\phi\_{\infty}^{2})+4a^{2}\phi\_{\infty}^{2}}\right)^{2}}{4}]\text{ if }\gamma\in[\frac{1}{2},1[\end{array}.\right.

  only depending on λ,c,ϕ\lambda,c,\phi, and the kernel KK.

  |  |  |  |
  | --- | --- | --- |
  |  | ∀t≥0,𝔼​(|Xt−Xt′|)2≤φ∞​(t)​Ψ​(𝔼​[|X0−X0′|2]),where​Ψ:x→{x​ if ​γ=11∨x if γ∈[12,1[.\forall t\geq 0,\;\mathbb{E}\,\Big(\Big|X\_{t}-X^{\prime}\_{t}\Big|\Big)^{2}\leq\varphi\_{\infty}(t)\Psi\left(\mathbb{E}\,\Big[\big|X\_{0}-X^{\prime}\_{0}\big|^{2}\Big]\right),\;\text{where}\,\Psi:x\to\left\{\begin{array}[]{ll}&x\text{ if }\gamma=1\\ &1\vee x\text{ if }\gamma\in[\frac{1}{2},1[\end{array}.\right. |  |

  In particular, if a=0a=0 or ϕ∞=0\phi\_{\infty}=0, then limt→+∞φ∞​(t)={ρ11−γ if γ∈[12,1[0​ if ​γ=1.\lim\_{t\to+\infty}\varphi\_{\infty}(t)=\left\{\begin{array}[]{ll}&\rho^{\frac{1}{1-\gamma}}\text{ if }\gamma\in[\frac{1}{2},1[\\
  &0\text{ if }\gamma=1\end{array}.\right.
* (b)

  This result can be written using the 2-Wasserstein distance between XX and X′X^{\prime}:

  |  |  |  |
  | --- | --- | --- |
  |  | ∀t≥0,W2​([Xt′],[Xt])≤φ∞​(t)1/2​Ψ​(W2​([X0′],[X0])).\forall t\geq 0,\;W\_{2}([X\_{t}^{\prime}],[X\_{t}])\leq\varphi\_{\infty}(t)^{1/2}\Psi\Big(W\_{2}([X\_{0}^{\prime}],[X\_{0}])\Big). |  |
* (c)

  (Lipschitz L2L^{2}-Confluence): In the setting γ=1\gamma=1, in particular, if a=0a=0 or ϕ∞=0\phi\_{\infty}=0, we have:

  + —

    if XX has a fake stationary regime of type I, 𝔼​Xt′→x∞\mathbb{E}X\_{t}^{\prime}\to x\_{\infty}, Var​(Xt′)→v0\text{Var}(X\_{t}^{\prime})\to v\_{0} as t→+∞t\to+\infty.

    And more generally finite-dimensional W2W\_{2}-convergence.
    Thus, the process X′X^{\prime} mixes: as time increases, the
    random variable Xt′X^{\prime}\_{t} progressively forgets its initial initial mean and variance, and approaches a limit of a Fake stationarity regime.
  + —

    In case if X has a fake stationary regime of type II, its marginal distribution is unique.

Remark on Lipschitz L2L^{2}-Confluence:
At this stage, we do not have confluence, unless a=0a=0 or ϕ∞=0\phi\_{\infty}=0 and γ=1\gamma=1 (Lipschitzianity).
However, assume that the diffusion coefficient σ2\sigma^{2} given in ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is non-negative and uniformly elliptic i.e.
∃σ¯0>0,such that​∀x∈ℝ,σ2​(x)≥σ¯02\exists\,\bar{\sigma}\_{0}>0,\;\text{such that}\;\ \forall x\in\mathbb{R},\ \sigma^{2}(x)\geq\bar{\sigma}\_{0}^{2}, then σ\sigma is Lispchitz in I:=]−κ0κ1,+∞[I:=]-\frac{\kappa\_{0}}{\kappa\_{1}},+\infty[ since

∀x,y∈I,|σ​(x)−σ​(y)|=|κ1|​|x−y|σ​(x)+σ​(y)≤|κ1|2​σ¯0​|x−y|.\forall x,y\in I,|\sigma(x)-\sigma(y)|=\frac{|\kappa\_{1}||x-y|}{\sigma(x)+\sigma(y)}\leq\frac{|\kappa\_{1}|}{2\bar{\sigma}\_{0}}|x-y|.

Consequently, if κ0+κ1​X0>0\kappa\_{0}+\kappa\_{1}\;X\_{0}>0 and θ,λ,κ0,κ1\theta,\lambda,\kappa\_{0},\kappa\_{1} are such that κ0+κ1​Xt>0\kappa\_{0}+\kappa\_{1}\;X\_{t}>0 for all tt i.e. any càdlàg solution XX of equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) satisfies ℙ​(σ2​(Xt)>0,∀t≥0)=1,ℙ−a.s\mathbb{P}(\sigma^{2}(X\_{t})>0,\forall t\geq 0)=1,\;\mathbb{P}-a.s , then by setting κ:=(κ12​σ¯0)2>0\kappa:=\left(\frac{\kappa\_{1}}{2\bar{\sigma}\_{0}}\right)^{2}>0, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0𝔼​[|σ​(Xt)−σ​(Xt′)|2]≤κ​𝔼​[|Xt−Xt′|2].\forall t\geq 0\quad\mathbb{E}\left[|\sigma(X\_{t})-\sigma(X^{\prime}\_{t})|^{2}\right]\leq\kappa\mathbb{E}\left[|X\_{t}-X^{\prime}\_{t}|^{2}\right]. |  | (5.48) |

So that if c is taken such that c∈(0,1κ)c\in(0,\frac{1}{\kappa}), the Proposition [5.1](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem1 "Proposition 5.1 (𝛾-Hölder 𝐿²-Contraction). ‣ 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") above applies as if γ=1\gamma=1, in which case, there exists a continuous non-negative function φ∞λ,c,K,ϕ=:φ∞:ℝ+→[0,1]\varphi\_{\infty}^{\lambda,c,K,\phi}=:\varphi\_{\infty}:\mathbb{R}^{+}\to[0,1], satisfying φ∞​(0)=1\varphi\_{\infty}(0)=1, limt→+∞φ∞​(t)=a2​ϕ∞21−ρ​(1−a2​ϕ∞2)\lim\_{t\to+\infty}\varphi\_{\infty}(t)=\frac{a^{2}\phi\_{\infty}^{2}}{1-\rho(1-a^{2}\phi\_{\infty}^{2})}, only depending on λ,c,ϕ\lambda,c,\phi, and KK, such that :

|  |  |  |
| --- | --- | --- |
|  | ∀t≥0,𝔼​(|Xt−Xt′|)2≤φ∞​(t)​𝔼​(|X0−X0′|)2​or​W2​([Xt′],[Xt])≤φ∞​(t)1/2​W2​([X0′],[X0]).\forall t\geq 0,\;\mathbb{E}\,\Big(\Big|X\_{t}-X^{\prime}\_{t}\Big|\Big)^{2}\leq\varphi\_{\infty}(t)\mathbb{E}\,\Big(\Big|X\_{0}-X^{\prime}\_{0}\Big|\Big)^{2}\;\text{or}\;W\_{2}([X\_{t}^{\prime}],[X\_{t}])\leq\varphi\_{\infty}(t)^{1/2}W\_{2}([X\_{0}^{\prime}],[X\_{0}]). |  |

Consequently, whenever a=0a=0 or ϕ∞=0\phi\_{\infty}=0, we have limt→+∞φ∞​(t)=0\lim\_{t\to+\infty}\varphi\_{\infty}(t)=0 so that the confluence in Proposition [5.1](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem1 "Proposition 5.1 (𝛾-Hölder 𝐿²-Contraction). ‣ 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (c) holds, that is 𝔼​Xt′→x∞\mathbb{E}X\_{t}^{\prime}\to x\_{\infty}, Var​(Xt′)→v0\text{Var}(X\_{t}^{\prime})\to v\_{0} as t→+∞t\to+\infty and if X has a fake stationary regime of type II, its marginal distribution is unique.

Proof of Proposition [5.1](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem1 "Proposition 5.1 (𝛾-Hölder 𝐿²-Contraction). ‣ 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). (b) and (c) are straightforward consequences of (a).
Set Δt=Xt−Xt′∈L2​(ℙ)\Delta\_{t}=X\_{t}-X^{\prime}\_{t}\in L^{2}(\mathbb{P}) for every t≥0t\geq 0. One writes owing to the reduced form [2.17](https://arxiv.org/html/2512.09590v1#S2.E17 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt−Xt′\displaystyle X\_{t}-X^{\prime}\_{t} | =(ϕ​(t)−(fλ∗ϕ)​(t))​(X0−X0′)+1λ​∫0tfλ​(t−s)​ς​(s)​(σ​(Xs)−σ​(Xs′))​𝑑Ws\displaystyle=\big(\phi(t)-(f\_{\lambda}\*\phi)(t)\big)\big(X\_{0}-X^{\prime}\_{0}\big)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\varsigma(s)\Big(\sigma(X\_{s})-\sigma(X^{\prime}\_{s})\Big)dW\_{s} |  |

Let δ¯t=‖|Δt|‖2\bar{\delta}\_{t}=\Big\||\Delta\_{t}|\Big\|\_{2} for convenience. One checks that, under our assumptions, t↦δ¯tt\mapsto\bar{\delta}\_{t} is continuous (see [[28](https://arxiv.org/html/2512.09590v1#bib.bib28)]).
Set ρ=c​[σ]Höl2∈(0,1)\rho=c[\sigma]^{2}\_{\text{H\"{o}l}}\in(0,1). Using elementary computations and Itô’s Isometry show that for every t≥0t\geq 0

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(|Xt−Xt′|)2\displaystyle\mathbb{E}\,\Big(\Big|X\_{t}-X^{\prime}\_{t}\Big|\Big)^{2} | =|ϕ​(t)−(fλ∗ϕ)​(t)|2​𝔼​(|X0−X0′|)2+1λ2​∫0tfλ2​(t−s)​ς2​(s)​𝔼​(|σ​(Xs)−σ​(Xs′)|)2​𝑑s.\displaystyle=\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|^{2}\mathbb{E}\,\Big(\Big|X\_{0}-X^{\prime}\_{0}\Big|\Big)^{2}+\frac{1}{\lambda^{2}}\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\mathbb{E}\,\Big(|\sigma(X\_{s})-\sigma(X^{\prime}\_{s})|\Big)^{2}ds. |  |

which entails owing to equation ([5.47](https://arxiv.org/html/2512.09590v1#S5.E47 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) :

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|Δt|‖22≤‖|Δ0|‖22​|ϕ​(t)−(fλ∗ϕ)​(t)|2+[σ]Höl2λ2​∫0tfλ2​(t−s)​ς2​(s)​‖|Δs|‖22​γ​𝑑s.\Big\||\Delta\_{t}|\Big\|\_{2}^{2}\leq\Big\||\Delta\_{0}|\Big\|\_{2}^{2}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|^{2}+\frac{[\sigma]^{2}\_{\text{H\"{o}l}}}{\lambda^{2}}\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\Big\||\Delta\_{s}|\Big\|\_{2}^{2\gamma}\,ds. |  | (5.49) |

From now on, we define Ψ:x→{x​ if ​γ=11∨x if γ∈[12,1[.\Psi:x\to\left\{\begin{array}[]{ll}&x\text{ if }\gamma=1\\
&1\vee x\text{ if }\gamma\in[\frac{1}{2},1[\end{array}.\right.
One checks that, ∀α,x∈ℝ+,Ψα​(x)=Ψ​(xα)\forall\;\alpha,x\in\mathbb{R}\_{+},\;\Psi^{\alpha}(x)=\Psi(x^{\alpha}), Ψ​(x)≥x\Psi(x)\geq x and Ψ2​γ​(x)≤Ψ2​(x)=Ψ​(x2).\Psi^{2\gamma}(x)\leq\Psi^{2}(x)=\Psi(x^{2}). (Note that (1∨δ¯0)≥1\left(1\vee\bar{\delta}\_{0}\right)\geq 1 so that (1∨δ¯0)2​γ≤(1∨δ¯0)2\left(1\vee\bar{\delta}\_{0}\right)^{2\gamma}\leq\left(1\vee\bar{\delta}\_{0}\right)^{2} as γ≤1\gamma\leq 1)

Step 1  Non-expansivity via a stopping-time argument: Let η>0\eta>0 such that ρ​(1+η)2>1\rho(1+\eta)^{2}>1. We define τη:=inf{t≥0:δ¯t>(1+η)​Ψ​(δ¯0)}\tau\_{\eta}:=\inf\{t\geq 0:\bar{\delta}\_{t}>(1+\eta)\Psi(\bar{\delta}\_{0})\}.
If τη<+∞\tau\_{\eta}<+\infty, we have δ¯s≤(1+η)​Ψ​(δ¯0)\bar{\delta}\_{s}\leq(1+\eta)\Psi(\bar{\delta}\_{0}) for s∈(0,τη)s\in(0,\tau\_{\eta}) and by continuity, δ¯τη2=(1+η)2​Ψ​(δ¯02)\bar{\delta}\_{\tau\_{\eta}}^{2}=(1+\eta)^{2}\Psi(\bar{\delta}\_{0}^{2}). Plugging this into equation ([5.49](https://arxiv.org/html/2512.09590v1#S5.E49 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), the inequality at time τη\tau\_{\eta} combined with the identity fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}) yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ¯τη2\displaystyle\bar{\delta}\_{\tau\_{\eta}}^{2} | ≤Ψ​(δ¯02)​[(ϕ−fλ∗ϕ)2​(τη)+(1−(ϕ−fλ∗ϕ)2​(τη))​ρ​(1+η)2​γ]\displaystyle\leq\Psi(\bar{\delta}\_{0}^{2})\left[(\phi-f\_{\lambda}\*\phi)^{2}(\tau\_{\eta})+(1-(\phi-f\_{\lambda}\*\phi)^{2}(\tau\_{\eta}))\rho(1+\eta)^{2\gamma}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Ψ​(δ¯02)​[(ϕ−fλ∗ϕ)2​(τη)−(ϕ−fλ∗ϕ)2​(τη)​ρ​(1+η)2+ρ​(1+η)2]<ρ​(1+η)2​Ψ​(δ¯02),\displaystyle\leq\Psi(\bar{\delta}\_{0}^{2})\left[(\phi-f\_{\lambda}\*\phi)^{2}(\tau\_{\eta})-(\phi-f\_{\lambda}\*\phi)^{2}(\tau\_{\eta})\rho(1+\eta)^{2}+\rho(1+\eta)^{2}\right]<\rho(1+\eta)^{2}\Psi(\bar{\delta}\_{0}^{2}), |  |

which leads to a contradiction. Therefore τη=+∞\tau\_{\eta}=+\infty i.e., δ¯s≤(1+η)​Ψ​(δ¯0)\bar{\delta}\_{s}\leq(1+\eta)\Psi(\bar{\delta}\_{0}) for all s≥0s\geq 0. This holds for every η>0\eta>0, implying the non-expansive bound δ¯t≤Ψ​(δ¯0)\bar{\delta}\_{t}\leq\Psi(\bar{\delta}\_{0}) for all t≥0t\geq 0 when throwing η\eta to 0.

Step 2 Iteration and the Volterra map: Substituting this (i.e. δ¯t≤Ψ​(δ¯0)\bar{\delta}\_{t}\leq\Psi(\bar{\delta}\_{0})) into ([5.49](https://arxiv.org/html/2512.09590v1#S5.E49 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) combined with the identity fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}) gives, for all t>0t>0,

|  |  |  |
| --- | --- | --- |
|  | δ¯t2≤Ψ​(δ¯02)​φ1​(t),whereφ1​(t):=(ϕ−fλ∗ϕ)2​(t)+(1−(ϕ−fλ∗ϕ)2​(t))​ρ,limt→∞φ1​(t)=a2+(1−a2)​ρ.\bar{\delta}\_{t}^{2}\leq\Psi(\bar{\delta}\_{0}^{2})\varphi\_{1}(t),\quad\text{where}\quad\varphi\_{1}(t):=(\phi-f\_{\lambda}\*\phi)^{2}(t)+(1-(\phi-f\_{\lambda}\*\phi)^{2}(t))\rho,\;\quad\lim\_{t\to\infty}\varphi\_{1}(t)=a^{2}+(1-a^{2})\rho. |  |

Note that φ1​(t)=ρ+(ϕ−fλ∗ϕ)2​(t)​(1−ρ)\varphi\_{1}(t)=\rho+(\phi-f\_{\lambda}\*\phi)^{2}(t)(1-\rho) satisfies:
φ1​(0)=1,φ1​(t)∈(0,1)​∀t>0,φ1​ is continuous.\varphi\_{1}(0)=1,\;\varphi\_{1}(t)\in(0,1)\,\forall\,t>0,\;\varphi\_{1}\text{ is continuous.}
Substituting this upper bound (i.e. δ¯t2≤Ψ​(δ¯02)​φ1​(t)\bar{\delta}\_{t}^{2}\leq\Psi(\bar{\delta}\_{0}^{2})\varphi\_{1}(t)) into ([5.49](https://arxiv.org/html/2512.09590v1#S5.E49 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) yields

|  |  |  |
| --- | --- | --- |
|  | δ¯t2≤Ψ​(δ¯02)​φ2​(t),whereφ2​(t):=(ϕ−fλ∗ϕ)2​(t)+ρ​∫0tfλ2​(t−s)​ς2​(s)​φ1γ​(s)​d​sλ2​c.\bar{\delta}\_{t}^{2}\leq\Psi(\bar{\delta}\_{0}^{2})\varphi\_{2}(t),\quad\text{where}\quad\varphi\_{2}(t):=(\phi-f\_{\lambda}\*\phi)^{2}(t)+\rho\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\varphi\_{1}^{\gamma}(s)\frac{ds}{\lambda^{2}c}. |  |

Using the identity ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) satisfied by ς2\varsigma^{2} (fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2})) and the definition of φ1\varphi\_{1}, we get

|  |  |  |
| --- | --- | --- |
|  | φ2​(t):=φ1​(t)−ρ​∫0tfλ2​(t−s)​ς2​(s)​(1−φ1γ​(s))​d​sλ2​c.\varphi\_{2}(t):=\varphi\_{1}(t)-\rho\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\left(1-\varphi\_{1}^{\gamma}(s)\right)\frac{ds}{\lambda^{2}c}. |  |

Thus, 0≤φ2<φ1<10\leq\varphi\_{2}<\varphi\_{1}<1 on (0,+∞)(0,+\infty). By induction, we show that δ¯t2≤Ψ​(δ¯02)​φk​(t)\bar{\delta}^{2}\_{t}\leq\Psi(\bar{\delta}\_{0}^{2})\varphi\_{k}(t)
with

|  |  |  |
| --- | --- | --- |
|  | φk​(t)=(ϕ−fλ∗ϕ)2​(t)+ρ​∫0tfλ2​(t−s)​ς2​(s)​φk−1γ​(s)​d​sλ2​c=φ1​(t)−ρ​∫0tfλ2​(t−s)​ς2​(s)​(1−φk−1γ​(s))​d​sλ2​c.\varphi\_{k}(t)=(\phi-f\_{\lambda}\*\phi)^{2}(t)+\rho\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{k-1}^{\gamma}(s)\frac{ds}{\lambda^{2}c}=\varphi\_{1}(t)-\rho\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\left(1-\varphi\_{k-1}^{\gamma}(s)\right)\frac{ds}{\lambda^{2}c}. |  |

where we used again the identity ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) satisfied by ς2\varsigma^{2} and the definition of φ1\varphi\_{1}.

Step 3  Monotonicity and Limit equation: Consequently, starting from 0≤φ2<φ1<10\leq\varphi\_{2}<\varphi\_{1}<1 on (0,+∞)(0,+\infty), induction shows that 0≤φk<φk−1<10\leq\varphi\_{k}<\varphi\_{k-1}<1 on (0,+∞)(0,+\infty) for every k≥2k\geq 2. Furthermore, we verify by induction that φk\varphi\_{k} is continuous, as by change of variable,

|  |  |  |
| --- | --- | --- |
|  | φk​(t)=φ1​(t)−ρ​∫0tfλ2​(s)​ς2​(t−s)​(1−φk−1γ​(t−s))​d​sλ2​c,\varphi\_{k}(t)=\varphi\_{1}(t)-\rho\int\_{0}^{t}f^{2}\_{\lambda}(s)\varsigma^{2}(t-s)\left(1-\varphi\_{k-1}^{\gamma}(t-s)\right)\frac{ds}{\lambda^{2}c}, |  |

where ς2\varsigma^{2} is continuous and bounded in ℝ+∗\mathbb{R}\_{+}^{\*} by assumption.

By the first Dini Lemma, we have φk↓φ∞∈𝒞​(ℝ+,ℝ)\varphi\_{k}\downarrow\varphi\_{\infty}\in\mathcal{C}(\mathbb{R}\_{+},\mathbb{R}) uniformly on compact intervals with φ∞​(0)=1\varphi\_{\infty}(0)=1. In particular, φ∞\varphi\_{\infty} satisfies the functional equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ∞​(t)=(ϕ−fλ∗ϕ)2​(t)+ρ​∫0tfλ2​(t−s)​ς2​(s)​φ∞γ​(s)​d​sλ2​c.\varphi\_{\infty}(t)=(\phi-f\_{\lambda}\*\phi)^{2}(t)+\rho\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{\infty}^{\gamma}(s)\frac{ds}{\lambda^{2}c}. |  | (5.50) |

Step 4  Limit and asymptotic bound: Let ℓ∞:=limt→+∞φ∞​(t)∈[0,1]\ell\_{\infty}:=\lim\_{t\to+\infty}\varphi\_{\infty}(t)\in[0,1]. Now, ℓ∞∈[0,1]\ell\_{\infty}\in[0,1] implies that for any η>0\eta>0, there exists tη∈ℝ+t\_{\eta}\in\mathbb{R}^{+} such that for t≥tηt\geq t\_{\eta}, l∞−η≤φ∞​(t)≤l∞+ηl\_{\infty}-\eta\leq\varphi\_{\infty}(t)\leq l\_{\infty}+\eta.
On the first hand,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tfλ2​(t−s)​ς2​(s)​φ∞​(s)​d​sλ2​c\displaystyle\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{\infty}(s)\frac{ds}{\lambda^{2}c} | ≤1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ∞+η)γ​𝑑s+1c​λ2​∫0tηfλ2​(t−s)​ς2​(s)​φ∞γ​(s)​𝑑s\displaystyle\leq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\ell\_{\infty}+\eta)^{\gamma}\,ds+\frac{1}{c\lambda^{2}}\int\_{0}^{t\_{\eta}}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{\infty}^{\gamma}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ∞+η)γ​𝑑s+1c​λ2​∫t−tηtfλ2​(u)​ς2​(t−u)​𝑑u.\displaystyle\leq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\ell\_{\infty}+\eta)^{\gamma}\,ds+\frac{1}{c\lambda^{2}}\int\_{t-t\_{\eta}}^{t}f^{2}\_{\lambda}(u)\varsigma^{2}(t-u)\,du. |  |

where the second term on the right-hand side of the last inequality follows from the fact that φ∞​(t−u)≤1\varphi\_{\infty}(t-u)\leq 1 for all u≤t≤tηu\leq t\leq t\_{\eta} and vanishes as t goes to infinity. Since fλ∈L2​(Leb1)f\_{\lambda}\in L^{2}(\text{Leb}\_{1}) and limt→+∞(ϕ−fλ∗ϕ)2​(t)=a2​ϕ∞2\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)^{2}(t)=a^{2}\phi^{2}\_{\infty} both owing to Assumption [2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we conclude from equation ([5.50](https://arxiv.org/html/2512.09590v1#S5.E50 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and the identity satisfied by ς\varsigma:

|  |  |  |
| --- | --- | --- |
|  | ℓ∞=:limt→+∞φ∞(t)≤a2ϕ∞2+ρ(ℓ∞+η)γ(1−a2ϕ∞2),\ell\_{\infty}=:\lim\_{t\to+\infty}\varphi\_{\infty}(t)\leq a^{2}\phi^{2}\_{\infty}+\rho(\ell\_{\infty}+\eta)^{\gamma}(1-a^{2}\phi^{2}\_{\infty}), |  |

which implies ℓ∞≤a2​ϕ∞2+ρ​(1−a2​ϕ∞2)​ℓ∞γby lettingη→0.\ell\_{\infty}\leq a^{2}\phi^{2}\_{\infty}+\rho(1-a^{2}\phi^{2}\_{\infty})\ell\_{\infty}^{\gamma}\quad\textit{by letting}\quad\eta\to 0.
On the other hand, we also have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tfλ2​(t−s)​ς2​(s)​φ∞​(s)​d​sλ2​c\displaystyle\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{\infty}(s)\frac{ds}{\lambda^{2}c} | ≥1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ∞−η)γ​𝑑s+1c​λ2​∫t−tηtfλ2​(u)​ς2​(t−u)​φ∞γ​(t−u)​𝑑u\displaystyle\geq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\ell\_{\infty}-\eta)^{\gamma}\,ds+\frac{1}{c\lambda^{2}}\int\_{t-t\_{\eta}}^{t}f^{2}\_{\lambda}(u)\,\varsigma^{2}(t-u)\varphi\_{\infty}^{\gamma}(t-u)\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ∞−η)γ​𝑑s.\displaystyle\geq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\ell\_{\infty}-\eta)^{\gamma}\,ds. |  |

Therefore, still with the fact that fλ∈L2​(Leb1)f\_{\lambda}\in L^{2}(\text{Leb}\_{1}) and limt→+∞(ϕ−fλ∗ϕ)2​(t)=a2​ϕ∞2\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)^{2}(t)=a^{2}\phi^{2}\_{\infty}, we obtain from equation ([5.50](https://arxiv.org/html/2512.09590v1#S5.E50 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and the identity satisfied by ς\varsigma:

|  |  |  |
| --- | --- | --- |
|  | ℓ∞=:limt→+∞φ∞(t)≥a2ϕ∞2+ρ(ℓ∞−η)γ(1−a2ϕ∞2)⟹l∞≥a2ϕ∞2+ρ(1−a2ϕ∞2)ℓ∞γasη→0.\ell\_{\infty}=:\lim\_{t\to+\infty}\varphi\_{\infty}(t)\geq a^{2}\phi^{2}\_{\infty}+\rho(\ell\_{\infty}-\eta)^{\gamma}(1-a^{2}\phi^{2}\_{\infty})\quad\implies l\_{\infty}\geq a^{2}\phi^{2}\_{\infty}+\rho(1-a^{2}\phi^{2}\_{\infty})\ell\_{\infty}^{\gamma}\quad\textit{as}\quad\eta\to 0. |  |

Thus, ℓ∞\ell\_{\infty} must solves the equation l∞=a2​ϕ∞2+ρ​(1−a2​ϕ∞2)​ℓ∞γl\_{\infty}=a^{2}\phi^{2}\_{\infty}+\rho(1-a^{2}\phi^{2}\_{\infty})\ell\_{\infty}^{\gamma}. Now, note that,
if γ=1,\gamma=1, then ℓ∞=ℓ¯∞=ℓ¯∞=a2​ϕ∞21−ρ​(1−a2​ϕ∞2)\ell\_{\infty}=\underline{\ell}\_{\infty}=\overline{\ell}\_{\infty}=\frac{a^{2}\phi^{2}\_{\infty}}{1-\rho(1-a^{2}\phi^{2}\_{\infty})}
and if γ∈[12,1[\gamma\in[\frac{1}{2},1[, as ℓ∞∈(0,1)\ell\_{\infty}\in(0,1), we have ℓ∞≤ℓ∞γ≤ℓ∞\ell\_{\infty}\leq\ell\_{\infty}^{\gamma}\leq\sqrt{\ell\_{\infty}}.

Step 5 (Case a=0a=0 or ϕ∞=0\phi\_{\infty}=0). When a=0a=0 or ϕ∞=0\phi\_{\infty}=0, ℓ∞\ell\_{\infty} is a fixed point of the function x→ρ​xγx\to\rho x^{\gamma} i.e. ℓ∞\ell\_{\infty} is either 0 or ρ11−γ\rho^{\frac{1}{1-\gamma}}. Note that, the only fixed point is 0 when γ=1\gamma=1. If γ∈[12,1[\gamma\in[\frac{1}{2},1[, as the sequence (φk)k≥1(\varphi\_{k})\_{k\geq 1} is non-incresasing and limt→∞φ1​(t)=ρ≥ρ2≥ρ11−γ\lim\_{t\to\infty}\varphi\_{1}(t)=\rho\geq\rho^{2}\geq\rho^{\frac{1}{1-\gamma}}, we may have that ρ11−γ\rho^{\frac{1}{1-\gamma}} is an attractive/stable fixed point. Owing to the monotone convergence theorem, we deduce that ℓ∞=ρ11−γ\ell\_{\infty}=\rho^{\frac{1}{1-\gamma}}

This completes the proof and we are done. □\square

Remark: The function φ∞\varphi\_{\infty} quantifies the decay over time of the expected squared difference between two solutions of the SVIE with different initial values.
If ς\varsigma is bounded (i.e. ‖ς‖∞<∞\|\varsigma\|\_{\infty}<\infty ) and both κ<λ2‖ς2‖∞​∫0+∞fλ2​(u)​𝑑u\kappa<\frac{\lambda^{2}}{\|\varsigma^{2}\|\_{\infty}\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\,du} and (ϕ−fλ∗ϕ)∈L2​(Leb1)(\phi-f\_{\lambda}\*\phi)\in L^{2}(\text{Leb}\_{1}),
then one derives from equation ([5.50](https://arxiv.org/html/2512.09590v1#S5.E50 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and using Fubini-Tonelli’s theorem that:

∫0+∞φ∞​(s)​𝑑s≤λ2λ2−κ​‖ς2‖∞​∫0+∞fλ2​(u)​𝑑u​∫0+∞(ϕ−fλ∗ϕ)2​(t)​𝑑t<+∞.\int\_{0}^{+\infty}\varphi\_{\infty}(s)\,ds\leq\frac{\lambda^{2}}{\lambda^{2}-\kappa\|\varsigma^{2}\|\_{\infty}\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\,du}\int\_{0}^{+\infty}(\phi-f\_{\lambda}\*\phi)^{2}(t)\,dt<+\infty.

### 5.2 Existence of limiting distributions

To establish the existence of limiting distributions for the inhomogeneous affine Volterra process, it is sufficient to prove the convergence of its Laplace transform, i.e. to show that the limit as t→∞t\to\infty in ([3.29](https://arxiv.org/html/2512.09590v1#S3.E29 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([3.30](https://arxiv.org/html/2512.09590v1#S3.E30 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) of Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (b) exists.
Then, one can apply Lévy’s continuity theorem, as done in [[27](https://arxiv.org/html/2512.09590v1#bib.bib27)]. This requires that the function ψ\psi obtained from ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is globally integrable in time; for example, it suffices that ψ∈L1​(ℝ+;ℝ)∩L2​(ℝ+;ℝ)\psi\in L^{1}(\mathbb{R}\_{+};\mathbb{R})\cap L^{2}(\mathbb{R}\_{+};\mathbb{R}), a condition that has been established in Theorem [A.1](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem1 "Proposition A.1 (Existence for the time-inhomogeneous Riccati-Volterra equation). ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). As a first step, we have the convergence of the Laplace transform given below.

###### Proposition 5.2.

Let XX be the time-inhomogeneous affine Volterra Equation with the diffusion coefficient σ\sigma given by ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and let λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}. Let X0∈L2​(P)X\_{0}\in L^{2}(P) be the initial random variable. Suppose that the Riccati-Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) has a unique global solution ψ=ψ​(⋅,μ)∈𝒞​([0,T],ℝ−)\psi=\psi(\cdot,\mu)\in\mathcal{C}([0,T],\mathbb{R}\_{-}) for each T>0T>0.
Then ψ∈L1​(ℝ+;ℝ−)∩L2​(ℝ+;ℝ−)\psi\in L^{1}(\mathbb{R}\_{+};\mathbb{R}\_{-})\cap L^{2}(\mathbb{R}\_{+};\mathbb{R}\_{-}), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞𝔼x¯0​[exp⁡(∫0tXt−s​μ​(d​s))]=exp⁡[ξ¯0​μ​(ℝ+)+ς∞22​σ2​(ξ¯0)​∫0∞ψ​(s,μ)2​𝑑s]\displaystyle\ \lim\_{t\to\infty}\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\int\_{0}^{t}X\_{t-s}\,\mu(ds)\Bigg)\Bigg]=\exp\left[\bar{\xi}\_{0}\;\mu(\mathbb{R}\_{+})+\frac{\varsigma^{2}\_{\infty}}{2}\sigma^{2}\left(\bar{\xi}\_{0}\right)\int\_{0}^{\infty}\psi(s,\mu)^{2}ds\right] |  | (5.51) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =exp⁡[(μ​(ℝ+)+∫0∞F∞​(ψ​(s,μ))​𝑑s)​ϕ∞​x¯0+(∫0∞ψ​(s,μ)​𝑑s)​μ∞+κ02​ς∞2​∫0∞ψ2​(s,μ)​𝑑s]\displaystyle\hskip 2.84544pt=\exp\left[\Big(\mu(\mathbb{R}\_{+})+\int\_{0}^{\infty}F\_{\infty}(\psi(s,\mu))\,ds\Big)\,\phi\_{\infty}\bar{x}\_{0}+\Big(\int\_{0}^{\infty}\psi(s,\mu)\,ds\Big)\mu\_{\infty}+\frac{\kappa\_{0}}{2}\varsigma^{2}\_{\infty}\int\_{0}^{\infty}\psi^{2}(s,\mu)\,ds\right] |  | (5.52) |

where F∞F\_{\infty} is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F∞​(ψ):=−λ​ψ+κ12​ς∞2​ψ2andς∞2:=limt→+∞ς2​(t)andξ¯0=a​ϕ∞​x¯0+(1−a)​μ∞λ.\displaystyle F\_{\infty}(\psi):=-\lambda\psi+\frac{\kappa\_{1}}{2}\varsigma^{2}\_{\infty}\psi^{2}\quad\text{and}\quad\varsigma^{2}\_{\infty}:=\lim\_{t\to+\infty}\varsigma^{2}(t)\quad\text{and}\quad\bar{\xi}\_{0}=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}. |  | (5.53) |

For clarity and conciseness, the proof of the above proposition is deferred to Appendix [A](https://arxiv.org/html/2512.09590v1#A1 "Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), where the main technical results are presented.

From the convergence of the Laplace transform we can now deduce convergence towards limiting distributions.
The following is our main result on limiting distributions for the time-inhomogeneous affine Volterra process, which generalizes results in [[19](https://arxiv.org/html/2512.09590v1#bib.bib19)]. In contrast to the classical case, the limiting distribution now also involves the initial state of the process.

###### Theorem 5.3 (Limiting Distribution).

Let XX be the time-inhomogeneous affine Volterra Equation with the diffusion coefficient σ\sigma given by ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and let λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}. Let also x¯0\bar{x}\_{0} be the initial state.
Then the law of the random variable XtX\_{t} converges for t→∞t\to\infty weakly to a limiting distribution πx¯0\pi\_{\bar{x}\_{0}}, whose Laplace transform is for u∈ℝ−u\in\mathbb{R}\_{-} given by

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ+exp⁡(u​x)​πx¯0​(d​x)=exp⁡[u​ξ¯0+ς∞22​σ2​(ξ¯0)​∫0∞ψ2​(s,u​δ0)​𝑑s]\displaystyle\ \int\_{\mathbb{R}\_{+}}\exp\left(u\,x\right)\pi\_{\bar{x}\_{0}}(dx)=\exp\left[u\,\bar{\xi}\_{0}+\frac{\varsigma^{2}\_{\infty}}{2}\sigma^{2}\left(\bar{\xi}\_{0}\right)\int\_{0}^{\infty}\psi^{2}(s,u\,\delta\_{0})ds\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =exp⁡[u​ϕ∞​x¯0+(∫0∞F∞​(ψ​(s,u​δ0))​𝑑s)​ϕ∞​x¯0+(∫0∞ψ​(s,u​δ0)​𝑑s)​μ∞+κ02​ς∞2​∫0∞ψ2​(s,u​δ0)​𝑑s].\displaystyle\ =\exp\left[u\phi\_{\infty}\bar{x}\_{0}+\left(\int\_{0}^{\infty}F\_{\infty}(\psi(s,u\,\delta\_{0}))\,ds\right)\,\phi\_{\infty}\bar{x}\_{0}+\left(\int\_{0}^{\infty}\psi(s,u\,\delta\_{0})\,ds\right)\mu\_{\infty}+\frac{\kappa\_{0}}{2}\varsigma^{2}\_{\infty}\int\_{0}^{\infty}\psi^{2}(s,u\,\delta\_{0})\,ds\right]. |  |

where F∞F\_{\infty} is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F∞​(ψ):=−λ​ψ+κ12​ς∞2​ψ2andς∞2:=limt→+∞ς2​(t)andξ¯0=a​ϕ∞​x¯0+(1−a)​μ∞λ.\displaystyle F\_{\infty}(\psi):=-\lambda\psi+\frac{\kappa\_{1}}{2}\varsigma^{2}\_{\infty}\psi^{2}\quad\text{and}\quad\varsigma^{2}\_{\infty}:=\lim\_{t\to+\infty}\varsigma^{2}(t)\quad\text{and}\quad\bar{\xi}\_{0}=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}. |  | (5.54) |

Moreover, πx¯0\pi\_{\bar{x}\_{0}} has finite first moment.

Proof of Theorem [5.3](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem3 "Theorem 5.3 (Limiting Distribution). ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").

Consider u∈ℝ−u\in\mathbb{R}\_{-}. According to Proposition [5.2](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem2 "Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), if we take μ​(d​s)=u​δ0​(d​s),\mu(ds)=u\,\delta\_{0}(ds), it holds that
(Or just, this is a direct consequence of Proposition [5.2](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem2 "Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), if we take μ​(d​s)=u​δ0​(d​s),\mu(ds)=u\,\delta\_{0}(ds), which gives the pointwise
convergence of the corresponding characteristic functions).

|  |  |  |
| --- | --- | --- |
|  | limt→∞𝔼x¯0​[exp⁡(u​Xt)]=exp⁡[u​(a​ϕ∞​x¯0+(1−a)​μ∞λ)+ς∞22​σ2​(a​ϕ∞​x¯0+(1−a)​μ∞λ)​∫0∞ψ​(s,u​δ0)2​𝑑s]\displaystyle\ \lim\_{t\to\infty}\mathbb{E}\_{\bar{x}\_{0}}\left[\exp\left(uX\_{t}\right)\right]=\exp\left[u\left(a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)+\frac{\varsigma^{2}\_{\infty}}{2}\sigma^{2}\left(a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)\int\_{0}^{\infty}\psi(s,u\,\delta\_{0})^{2}ds\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =exp⁡[u​ϕ∞​x¯0+(∫0∞F∞​(ψ​(s,u​δ0))​𝑑s)​ϕ∞​x¯0+(∫0∞ψ​(s,u​δ0)​𝑑s)​μ∞+κ02​ς∞2​∫0∞ψ2​(s,u​δ0)​𝑑s].\displaystyle=\exp\left[u\phi\_{\infty}\bar{x}\_{0}+\left(\int\_{0}^{\infty}F\_{\infty}(\psi(s,u\,\delta\_{0}))\,ds\right)\,\phi\_{\infty}\bar{x}\_{0}+\left(\int\_{0}^{\infty}\psi(s,u\,\delta\_{0})\,ds\right)\mu\_{\infty}+\frac{\kappa\_{0}}{2}\varsigma^{2}\_{\infty}\int\_{0}^{\infty}\psi^{2}(s,u\,\delta\_{0})\,ds\right]. |  |

Moreover, the estimate ([A.83](https://arxiv.org/html/2512.09590v1#A1.E83 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([A.82](https://arxiv.org/html/2512.09590v1#A1.E82 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) (in the proof of the proposition [5.2](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem2 "Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") above) hold with |μ|​(ℝ+)=|u||\mu|(\mathbb{R}\_{+})=|u|, showing that the right-hand side is continuous at u=0u=0. Hence, by Lévy’s continuity theorem for Laplace transforms, we conclude that XtX\_{t} converges weakly to some limiting distribution, we
denote it by πx¯0\pi\_{\bar{x}\_{0}}, and that the claimed formula for the Laplace transform ( characteristic function) of πx¯0\pi\_{\bar{x}\_{0}} holds.
An application of Fatou’s lemma shows that the limiting distribution πx¯0\pi\_{\bar{x}\_{0}} has a finite first moment, i.e., ∫ℝ+|x|​πx¯0​(d​x)≤supt≥0𝔼x¯0​[|Xt|]<∞.\int\_{\mathbb{R}\_{+}}|x|\,\pi\_{\bar{x}\_{0}}(dx)\leq\sup\_{t\geq 0}\mathbb{E}\_{\bar{x}\_{0}}[|X\_{t}|]<\infty.
This completes the proof. □\square

Remark:
In the classical (Markovian) setting, one would deduce using Feller semigroup theory that πx¯0\pi\_{\bar{x}\_{0}} is indeed a stationary distribution for the process XX.
In this setting, stationarity is typically verified by assuming that the initial state X0X\_{0} is distributed according to πx¯0\pi\_{\bar{x}\_{0}}, and then showing that, for any u∈ℝu\in\mathbb{R}, the following identity holds:

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ𝔼x​[exp⁡(u​Xt)]​πx¯0​(d​x):=𝔼πx¯0​[exp⁡(u​Xt)]=∫ℝexp⁡(u​x)​πx¯0​(d​x).\int\_{\mathbb{R}}\mathbb{E}\_{x}\left[\exp\left(uX\_{t}\right)\right]\,\pi\_{\bar{x}\_{0}}(dx):=\mathbb{E}\_{\pi\_{\bar{x}\_{0}}}\left[\exp\left(uX\_{t}\right)\right]=\int\_{\mathbb{R}}\exp\left(ux\right)\,\pi\_{\bar{x}\_{0}}(dx). |  |

This confirms that the law of XtX\_{t} remains invariant under πx¯0\pi\_{\bar{x}\_{0}}; that is, X0∼πx¯0⟹∀t≥0,Xt∼πx¯0,X\_{0}\sim\pi\_{\bar{x}\_{0}}\quad\Longrightarrow\quad\forall\,t\geq 0,\;X\_{t}\sim\pi\_{\bar{x}\_{0}},
implying that πx¯0\pi\_{\bar{x}\_{0}} is stationary for the process.
However, in our setting, the process XX does not possess the Markov property. Therefore, we follow the framework used in [[19](https://arxiv.org/html/2512.09590v1#bib.bib19)], which is specifically designed for non-Markovian (e.g., Volterra-type) dynamics.

### 5.3 Asymptotics: Long run functional weak behaviour and Stationary process

In the next step, we construct the associated stationary process.
To this end, we recall that for a real-valued stochastic process XX on [0,T][0,T], the Kolmogorov continuity theorem states that if for some constants p,a,C>0p,a,C>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|Xt−Xs|p]≤C⋅|t−s|1+a,\mathbb{E}\left[\left|X\_{t}-X\_{s}\right|^{p}\right]\leq C\cdot|t-s|^{1+a}, |  | (5.55) |

uniformly in 0≤s,t≤T0\leq s,t\leq T, then the process has a θ\theta-Hölder continuous modification for all 0<θ<a/p0<\theta<a/p.

To prove the existence of a stationary process associated with a limiting distribution, we cannot rely, as is typically done in the classical literature, on Feller semigroup theory or standard Markovian arguments. Instead, we adopt the alternative approach developed in [[19](https://arxiv.org/html/2512.09590v1#bib.bib19)], which is based on the extension of the exponential-affine transform formula presented in Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
Thanks to that extension, we obtain explicit control over the process’s finite-dimensional distributions.

Consequently, we prove in this section that, as u→∞u\to\infty, the shifted process (Xtu)t≥0(X^{u}\_{t})\_{t\geq 0} defined by Xtu:=Xt+uX^{u}\_{t}:=X\_{t+u} converges in law to a continuous process X∞X^{\infty}.
From Theorem [5.3](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem3 "Theorem 5.3 (Limiting Distribution). ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), it follows that for any t≥0t\geq 0, Xt⟶πx¯0X\_{t}\longrightarrow\pi\_{\bar{x}\_{0}} weakly as t→∞t\to\infty. Thus, Xt∞X\_{t}^{\infty} has distribution πx¯0\pi\_{\bar{x}\_{0}} for each t≥0t\geq 0, which is therefore the desired stationary solution.

###### Assumption 5.4 (Integrability and Uniform Hölder Continuity).

Let λ,c>0\lambda,c>0. Assume the kernel KαK\_{\alpha} is such that its λ\lambda-resolvent Rα,λR\_{\alpha,\lambda} and its derivative −fα,λ-f\_{\alpha,\lambda} satisfy:

1. (i)

   Integrability: We assume that the condition below is satisfied for some θ^∈(0,1]\widehat{\theta}\in(0,1]

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (𝒦^θ^c​o​n​t)​∃κ^<+∞,∀δ¯∈(0,T],η^​(δ):=maxi=1,2​supt∈[0,T][∫(t−δ¯)+t|fλ​(t−u)|i​𝑑u]1/i≤κ^​δ¯θ^.(\widehat{\cal K}^{cont}\_{\widehat{\theta}})\;\;\exists\,\widehat{\kappa}<+\infty,\;\forall\bar{\delta}\!\in(0,T],\;\widehat{\eta}(\delta):=\max\_{i=1,2}\sup\_{t\in[0,T]}\left[\int\_{(t-\bar{\delta})^{+}}^{t}\thinspace|f\_{\lambda}\big(t-u\big)|^{i}du\right]^{1/i}\leq\widehat{\kappa}\,\bar{\delta}^{\,\widehat{\theta}}. |  | (5.56) |
2. (ii)

   Hölder Continuity: There exists ϑ∈(0,1]\vartheta\in(0,1], C<+∞C<+\infty such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | maxi=1,2[∫0+∞|fλ(u+δ¯)−fλ(u)|idu]1i≤Cδ¯ϑ.\max\_{i=1,2}\left[\int\_{0}^{+\infty}|f\_{\lambda}(u+\bar{\delta})-f\_{\lambda}(u)|^{i}\,du\right]^{\frac{1}{i}}\leq C\bar{\delta}^{\vartheta}. |  | (5.57) |

Remark on the regularity:
According to [[35](https://arxiv.org/html/2512.09590v1#bib.bib35), Proposition 5.1] (see also [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 5.3] ), for the α\alpha-fractional integration kernel, ϑ∈(0,α−12)\vartheta\in(0,\alpha-\frac{1}{2}) and hence owing to the above theorem, the process XX is almost surely Hölder continuous of any order strictly less than δ∧α−12∧ϑ\delta\wedge\alpha-\frac{1}{2}\wedge\vartheta. Also note, that, according to the same results, fα,λ∈Lp​[0,T]f\_{\alpha,\lambda}\in L^{p}[0,T] for p∈[1,2]p\in[1,2] and T>0T>0

###### Theorem 5.5 (Long run theorem: Functional weak asymptotics and Stationary Process).

Let XX be the inhomogeneous affine Volterra equation with the diffusion coefficient σ\sigma given by ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and let λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}. Let also the initial state be X0∈Lp​(ℙ)X\_{0}\in L^{p}(\mathbb{P}) for some suitable p.
Suppose
that
condition (𝒦)(\mathcal{K}) holds, as well as assumption [3.2](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). Then the following assertions hold:

(a) Then, the family of shifted processes (Xt+u)u≥0(X\_{t+u})\_{u\geq 0} is C-tight, uniformly integrable, and square uniformly integrable for p>2p>2 as t→+∞t\to+\infty. For any limiting distribution PP on Ω0:=𝒞​(ℝ+,ℝ)\Omega\_{0}:=\mathcal{C}(\mathbb{R}\_{+},\mathbb{R}), the canonical process Yt​(ω)=ω​(t)Y\_{t}(\omega)=\omega(t) has a (δ∧ϑ∧θ^−1p−η)\left(\delta\wedge\vartheta\wedge\widehat{\theta}-\frac{1}{p}-\eta\right)-Hölder pathwise continuous PP-modification for sufficiently small η>0\eta>0.
There exists a stationary process X∞X^{\infty} with continuous sample paths such that

|  |  |  |
| --- | --- | --- |
|  | (Xt+u)t≥0⇒(Xt∞)t≥0weakly in ​𝒞​(ℝ+;ℝ)​ as ​u→∞.(X\_{t+u})\_{t\geq 0}\Rightarrow(X^{\infty}\_{t})\_{t\geq 0}\quad\text{weakly in }\mathcal{C}(\mathbb{R}\_{+};\mathbb{R})\text{ as }u\to\infty. |  |

Moreover, if ([5.48](https://arxiv.org/html/2512.09590v1#S5.E48 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) holds, in the setting ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, assumed to be the unique continuous solution to Equation ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
for some c∈(0,1κ)c\in(0,\frac{1}{\kappa}) (so that condition (Eλ,cE\_{\lambda,c}) is satisfied),
if a=0a=0 or ϕ∞=0\phi\_{\infty}=0, the shifted processes of two solutions (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X\_{t}^{\prime})\_{t\geq 0} are L2L^{2}-confluent, i.e. there exists a non-increasing function φ¯∞:ℝ+→[0,1]\bar{\varphi}\_{\infty}:\mathbb{R}\_{+}\to[0,1] with limt→+∞φ¯∞​(t)=0\lim\_{t\to+\infty}\bar{\varphi}\_{\infty}(t)=0, and

|  |  |  |
| --- | --- | --- |
|  | W2​([(Xt+t1,…,Xt+tN)],[(Xt+t1′,…,Xt+tN′)])→0ast→+∞.W\_{2}\left(\left[(X\_{t+t\_{1}},\ldots,X\_{t+t\_{N}})\right],\left[(X^{\prime}\_{t+t\_{1}},\ldots,X^{\prime}\_{t+t\_{N}})\right]\right)\to 0\quad\text{as}\quad t\to+\infty. |  |

Hence, the functional weak limiting distributions of [Xt+⁣⋅][X\_{t+\cdot}] and [Xt+⁣⋅′][X^{\prime}\_{t+\cdot}] coincide, meaning that if [Xtn+⁣⋅]→(C)P[X\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)}}{{\rightarrow}}P for some subsequence tn→+∞t\_{n}\to+\infty, then [Xtn+⁣⋅′]→(C)wP[X^{\prime}\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)\_{w}}}{{\rightarrow}}P and vice versa.

(b) The stationary process X∞X^{\infty} satisfies 𝔼​[|Xt∞|p]=∫ℝ+|x|p​πx¯0​(d​x)<∞\mathbb{E}[|X\_{t}^{\infty}|^{p}]=\int\_{\mathbb{R}\_{+}}|x|^{p}\pi\_{\bar{x}\_{0}}(dx)<\infty for each p>0p>0. Moreover, its first moment is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xt∞]=a​ϕ∞​𝔼​[X0]+(1−a)​μ∞λ,\mathbb{E}[X\_{t}^{\infty}]=a\phi\_{\infty}\mathbb{E}[X\_{0}]+(1-a)\frac{\mu\_{\infty}}{\lambda}, |  |

while its autocovariance function is Cov​(Xt1∞,Xt2∞):=Cfλ​(t1,t2)\text{Cov}(X\_{t\_{1}}^{\infty},X\_{t\_{2}}^{\infty}):=C\_{f\_{\lambda}}(t\_{1},t\_{2}), for 0≤t1≤t20\leq t\_{1}\leq t\_{2}, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | cov​(Xt2∞,Xt1∞)=a2​ϕ∞2​Var​(X0)+ς∞2λ2​σ2​(a​ϕ∞​𝔼​[X0]+(1−a)​μ∞λ)​∫0+∞fλ​(t2−t1+u)​fλ​(u)​𝑑u.\mathrm{cov}(X\_{t\_{2}}^{\infty},X\_{t\_{1}}^{\infty})=a^{2}\phi^{2}\_{\infty}{\rm Var}(X\_{0})+\frac{\varsigma^{2}\_{\infty}}{\lambda^{2}}\sigma^{2}\left(a\phi\_{\infty}\mathbb{E}[X\_{0}]+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)\int\_{0}^{+\infty}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)du. |  | (5.58) |

so that the process (Xt∞)t≥0(X^{\infty}\_{t})\_{t\geq 0} is at least a weak L2L^{2}-stationary process (see for example [[32](https://arxiv.org/html/2512.09590v1#bib.bib32)] for the definition of weak stationarity.) with mean x∞x\_{\infty} and covariance function Cfλ​(s,t)C\_{f\_{\lambda}}(s,t), for s,t≥0s,t\geq 0.

(c) The finite dimensional distributions of X∞X^{\infty} are determined by (here, ξ¯0:=a​ϕ∞​x¯0+(1−a)​μ∞λ\bar{\xi}\_{0}:=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda})

|  |  |  |
| --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∑i=1nui​Xti∞)]=exp⁡[∑i=1nξ¯0​ui+ς∞22​σ2​(ξ¯0)​∫0∞ψ​(s)2​𝑑s].\displaystyle\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\sum\_{i=1}^{n}u\_{i}X\_{t\_{i}}^{\infty}\Bigg)\Bigg]=\exp\left[\sum\_{i=1}^{n}\bar{\xi}\_{0}\,u\_{i}+\frac{\varsigma^{2}\_{\infty}}{2}\sigma^{2}\left(\bar{\xi}\_{0}\right)\int\_{0}^{\infty}\psi(s)^{2}ds\right]. |  |

where ς∞2:=limt→+∞ς2​(t)\varsigma^{2}\_{\infty}:=\lim\_{t\to+\infty}\varsigma^{2}(t) and
ψ​(⋅)=ψ​(⋅,μt1,…,tn)\psi(\cdot)=\psi(\cdot,\mu\_{t\_{1},\dots,t\_{n}}) denotes the unique solution of ([3.27](https://arxiv.org/html/2512.09590v1#S3.E27 "In Corollary 3.5. ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) in ℝ+\mathbb{R}\_{+} with μt1,…,tn​(d​s)=∑j=1nuj​δtn−tj​(d​s)\mu\_{t\_{1},\dots,t\_{n}}(ds)=\sum\_{j=1}^{n}u\_{j}\delta\_{t\_{n}-t\_{j}}(ds), n∈ℕn\in\mathbb{N}, u1,…,un∈ℝ−u\_{1},\dots,u\_{n}\in\mathbb{R}\_{-} and 0≤t1<⋯<tn0\leq t\_{1}<\dots<t\_{n}.

Proof of Theorem [5.5](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem5 "Theorem 5.5 (Long run theorem: Functional weak asymptotics and Stationary Process). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").

Step 1  (C-tightness of time-shifted processes and weak convergence ).
We can argue as in the proof of [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), Theorem 4.10] to show that under assumption [5.4](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem4 "Assumption 5.4 (Integrability and Uniform Hölder Continuity). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and assumption[2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (iv), for any p⩾pe​u:=1δ∨1ϑ∨1θ^p\geqslant p\_{eu}:=\frac{1}{\delta}\vee\frac{1}{\vartheta}\vee\frac{1}{\widehat{\theta}}, the solution XX satisfies (up to a ℙ\mathbb{P}-indistinguishability or a path-continuous version X~\tilde{X} ):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(|Xt−Xs|)p≤Cp,t0,ς,β,fα⋅(1+‖ϕ‖t0p​𝔼​[|X0|p])​|t−s|p​(δ∧ϑ∧θ^).\mathbb{E}\,\big(|X\_{t}-X\_{s}|\big)^{p}\leq C\_{p,t\_{0},\varsigma,\beta,f\_{\alpha}}\cdot\Big(1+\|\phi\|\_{t\_{0}}^{p}\mathbb{E}[|X\_{0}|^{p}]\Big)|t-s|^{p(\delta\wedge\vartheta\wedge\widehat{\theta})}. |  | (5.59) |

And thus, t↦Xtt\mapsto X\_{t} admits a Hölder continuous modification (still denoted XX in lieu of X~\tilde{X} up to a ℙ\mathbb{P}-indistinguishability), so that the process has the announced Hölder pathwise regularity, i.e. t↦Xtt\mapsto X\_{t} has a (δ∧ϑ∧θ^−η)\big(\delta\wedge\vartheta\wedge\widehat{\theta}-\eta\big)-Hölder pathwise continuous ℙ\mathbb{P}-modification for sufficiently small η>0\eta>0.

Define for u≥0u\geq 0 the process XuX^{u} by Xtu=Xt+uX^{u}\_{t}=X\_{t+u}, where t≥0t\geq 0. Then XuX^{u} has continuous sample paths and satisfies for some constant C​(p)>0C(p)>0 (This follows from equation ([5.59](https://arxiv.org/html/2512.09590v1#S5.E59 "In 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) or similarly to [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), Theorem 2.8]):

|  |  |  |
| --- | --- | --- |
|  | supu≥0𝔼​[|Xtu−Xsu|p]≤C​(p)​|t−s|p​(δ∧ϑ∧θ^)for allt,s≥0with ​0≤t−s≤1.\sup\_{u\geq 0}\mathbb{E}[|X^{u}\_{t}-X^{u}\_{s}|^{p}]\leq C(p)|t-s|^{p(\delta\wedge\vartheta\wedge\widehat{\theta})}\quad\text{for all}\quad t,s\geq 0\quad\text{with }0\leq t-s\leq 1. |  |

Now, choose p≥2p\geq 2 sufficiently large so that p​(δ∧ϑ∧θ^)>1p(\delta\wedge\vartheta\wedge\widehat{\theta})>1, it follows from Kolmogorov’s CC-tightness criterion (see [[39](https://arxiv.org/html/2512.09590v1#bib.bib39), Theorem 2.1, p. 26, 3rd edition] 777If a process XX taking values in a Polish space (S,ρ)(S,\rho) satisfies
𝔼​[ρ​(Xs,Xt)α]≤c​|s−t|β+d\mathbb{E}[\rho(X\_{s},X\_{t})^{\alpha}]\leq c|s-t|^{\beta+d} for some constants α,β,c>0\alpha,\beta,c>0 and all s,t∈ℝs,t\in\mathbb{R},
then XX admits a continuous modification whose paths are Hölder continuous of any
order γ∈(0,βα)\gamma\in(0,\tfrac{\beta}{\alpha}). or [[38](https://arxiv.org/html/2512.09590v1#bib.bib38), Lemma 44.4, Section IV.44, p.100]), that the family of shifted processes Xt+⁣⋅X\_{t+\cdot}, t≥0t\geq 0, is CC-tight i.e. (Xu)u≥0(X^{u})\_{u\geq 0} is tight on 𝒞​(ℝ+;ℝ)\mathcal{C}(\mathbb{R}\_{+};\mathbb{R}) (hence the existence of a weak
continuous accumulation point thanks to Prokhorov’s theorem) with limiting distributions P under which the canonical process has the announced Hölder pathwise regularity.
Consequently, we conclude that along a sequence uk↑∞u\_{k}\uparrow\infty, the process XukX^{u\_{k}} converges in law to some continuous process X∞X^{\infty}.

The confluence result follows from Proposition [5.1](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem1 "Proposition 5.1 (𝛾-Hölder 𝐿²-Contraction). ‣ 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") with φ¯∞​(t)=supu≥tφ∞​(u)\bar{\varphi}\_{\infty}(t)=\sup\_{u\geq t}\varphi\_{\infty}(u).
Let XX and X′X^{\prime} be two solutions of Equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) starting from X0X\_{0} and X0′X^{\prime}\_{0} respectively, both square integrable. Using the Remark in Proposition [5.1](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem1 "Proposition 5.1 (𝛾-Hölder 𝐿²-Contraction). ‣ 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") on Lipschitz L2L^{2}-Confluence, we derive that for every 0≤t1<t2<⋯<tN<+∞0\leq t\_{1}<t\_{2}<\cdots<t\_{{}\_{N}}<+\infty

|  |  |  |
| --- | --- | --- |
|  | 𝒲2​([(Xt+t1,⋯,Xt+tN)],[(Xt+t1′,⋯,Xt+tN′)])→0​ as ​t→+∞.{\cal W}\_{2}\big([(X\_{t+t\_{1}},\cdots,X\_{t+t\_{{}\_{N}}})],[(X^{\prime}\_{t+t\_{1}},\cdots,X^{\prime}\_{t+t\_{{}\_{N}}})])\to 0\mbox{ as }t\to+\infty. |  |

As a consequence, the weak limiting distributions of [Xt+⁣⋅][X\_{t+\cdot}] and [Xt+⁣⋅′][X^{\prime}\_{t+\cdot}] are the same in the sense that, if [Xtn+⁣⋅]⟶(C)P[X\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)}}{{\longrightarrow}}P for some subsequence tn→+∞t\_{n}\to+\infty (where PP is a probability measure on 𝒞​(ℝ+,ℝ)\mathcal{C}(\mathbb{R}\_{+},\mathbb{R}) equipped with the Borel σ\sigma-field induced by the sup-norm topology), then [Xtn+⁣⋅′]⟶(C)wP[X^{\prime}\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)\_{w}}}{{\longrightarrow}}P and conversely.

Step 2 (Moment and autocovariance function ).
Thanks to [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), Theorem 4.8], supt≥0𝔼​[|Xt|p]<∞\sup\_{t\geq 0}\mathbb{E}[|X\_{t}|^{p}]<\infty holds for each p>0p>0 and Xt⟶πx¯0X\_{t}\longrightarrow\pi\_{\bar{x}\_{0}} weakly, the Lemma of Fatou implies that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ+|x|p​πx¯0​(d​x)≤supt≥0𝔼​[|Xt|p]<∞.\int\_{\mathbb{R}\_{+}}|x|^{p}\,\pi\_{\bar{x}\_{0}}(dx)\leq\sup\_{t\geq 0}\mathbb{E}[|X\_{t}|^{p}]<\infty. |  |

And thus πx¯0\pi\_{\bar{x}\_{0}} has all finite moments. Since X∞X^{\infty} is stationary, we conclude the first assertion.

For the first moment formula, we note using equation ([2.19](https://arxiv.org/html/2512.09590v1#S2.E19 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and the remark on assumption [2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (or rather [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Lemma 3.1]) that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xt]=𝔼​[X0]​(ϕ​(t)−∫0tfλ​(t−r)​ϕ​(r)​𝑑r)+1λ​∫0tfλ​(t−r)​θ​(r)​dr⟶a​ϕ∞​𝔼​[X0]+(1−a)​μ∞λas ​t→∞.\mathbb{E}[X\_{t}]=\mathbb{E}[X\_{0}](\phi(t)-\int\_{0}^{t}f\_{\lambda}(t-r)\phi(r)\,dr)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-r)\theta(r)\,\mathrm{d}r\longrightarrow a\phi\_{\infty}\mathbb{E}[X\_{0}]+(1-a)\frac{\mu\_{\infty}}{\lambda}\quad\text{as }t\to\infty. |  |

Since supt≥0𝔼​[|Xt|2]<∞\sup\_{t\geq 0}\mathbb{E}[|X\_{t}|^{2}]<\infty, we easily conclude that limt→∞𝔼​[Xt]=∫ℝ+x​πx¯0​(d​x)=𝔼​[Xt∞].\quad\lim\_{t\to\infty}\mathbb{E}[X\_{t}]=\int\_{\mathbb{R\_{+}}}x\,\pi\_{\bar{x}\_{0}}(dx)=\mathbb{E}[X^{\infty}\_{t}].
This proves the desired first moment formula for the assymptotic (stationary) process.

(a) Now let us consider the asymptotic covariance between Xt+t1X\_{t+t\_{1}} and Xt+t2X\_{t+t\_{2}}, 0<t1<t20<t\_{1}<t\_{2} when XtX\_{t} starts for X0X\_{0}, t≥0t\geq 0 with v0:=Var​(X0)v\_{0}:={\rm Var}(X\_{0}).
Noting from equation ([2.17](https://arxiv.org/html/2512.09590v1#S2.E17 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) that (where we set Ξ​(t):=(ϕ−fλ∗ϕ)​(t)\Xi(t):=(\phi-f\_{\lambda}\*\phi)(t)):

|  |  |  |
| --- | --- | --- |
|  | Xt2−𝔼​[Xt2]=(X0−𝔼​[X0])​Ξ​(t2)+1λ​(∫0t1fλ​(t2−s)​ς​(s)​σ​(Xs)​𝑑Ws+∫t1t2fλ​(t2−s)​ς​(s)​σ​(Xs)​𝑑Ws),\displaystyle\;X\_{t\_{2}}-\mathbb{E}[X\_{t\_{2}}]=(X\_{0}-\mathbb{E}[X\_{0}])\Xi(t\_{2})+\frac{1}{\lambda}\left(\int\_{0}^{t\_{1}}f\_{\lambda}(t\_{2}-s)\varsigma(s)\sigma(X\_{s})\,dW\_{s}+\int\_{t\_{1}}^{t\_{2}}f\_{\lambda}(t\_{2}-s)\varsigma(s)\sigma(X\_{s})\,dW\_{s}\right), |  |
|  |  |  |
| --- | --- | --- |
|  | andXt1−𝔼​[Xt1]=(X0−𝔼​[X0])​Ξ​(t1)+1λ​∫0t1fλ​(t1−s)​ς​(s)​σ​(Xs)​𝑑Ws.\displaystyle\;\text{and}\;\qquad X\_{t\_{1}}-\mathbb{E}[X\_{t\_{1}}]=(X\_{0}-\mathbb{E}[X\_{0}])\Xi(t\_{1})+\frac{1}{\lambda}\int\_{0}^{t\_{1}}f\_{\lambda}(t\_{1}-s)\varsigma(s)\sigma(X\_{s})\,dW\_{s}. |  |

Using Cov​(a​U+b,c​V+d)=a​c​Cov​(U,V)\text{Cov}(aU+b,cV+d)=ac\,\text{Cov}(U,V), we find that the autocovariance function for XX is given by:

|  |  |  |
| --- | --- | --- |
|  | Cov​(Xt1,Xt2)=v0​Ξ​(t1)​Ξ​(t2)+1λ2​𝔼​[(∫0t1fλ​(t1−s)​ς​(s)​σ​(Xs)​𝑑Ws)​(∫0t1fλ​(t2−s)​ς​(s)​σ​(Xs)​𝑑Ws)]\displaystyle{\rm Cov}(X\_{t\_{1}},X\_{t\_{2}})=v\_{0}\;\Xi(t\_{1})\Xi(t\_{2})+\frac{1}{\lambda^{2}}\mathbb{E}\left[\left(\int\_{0}^{t\_{1}}f\_{\lambda}(t\_{1}-s)\varsigma(s)\sigma(X\_{s})dW\_{s}\right)\left(\int\_{0}^{t\_{1}}f\_{\lambda}(t\_{2}-s)\varsigma(s)\sigma(X\_{s})dW\_{s}\right)\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =Var​(X0)​((ϕ−fλ∗ϕ)​(t1))​((ϕ−fλ∗ϕ)​(t2))+1λ2​𝔼​[∫0t1fλ​(t2−s)​fλ​(t1−s)​ς2​(s)​σ2​(Xs)​𝑑s]\displaystyle\hskip 1.42271pt={\rm Var}(X\_{0})\left((\phi-f\_{\lambda}\*\phi)(t\_{1})\right)\left((\phi-f\_{\lambda}\*\phi)(t\_{2})\right)+\frac{1}{\lambda^{2}}\mathbb{E}\left[\int\_{0}^{t\_{1}}f\_{\lambda}(t\_{2}-s)f\_{\lambda}(t\_{1}-s)\varsigma^{2}(s)\sigma^{2}(X\_{s})ds\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =Var​(X0)​((ϕ−fλ∗ϕ)​(t1))​((ϕ−fλ∗ϕ)​(t2))+1λ2​∫0t1fλ​(t2−t1+u)​fλ​(u)​ς2​(t1−u)​𝔼​[σ2​(Xt1−u)]​𝑑u\displaystyle\hskip 0.56917pt={\rm Var}(X\_{0})\left((\phi-f\_{\lambda}\*\phi)(t\_{1})\right)\left((\phi-f\_{\lambda}\*\phi)(t\_{2})\right)+\frac{1}{\lambda^{2}}\int\_{0}^{t\_{1}}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)\varsigma^{2}(t\_{1}-u)\mathbb{E}\left[\sigma^{2}(X\_{t\_{1}-u})\right]du |  |
|  |  |  |
| --- | --- | --- |
|  | =Var​(X0)​((ϕ−fλ∗ϕ)​(t1))​((ϕ−fλ∗ϕ)​(t2))+1λ2​∫0t1fλ​(t2−t1+u)​fλ​(u)​ς2​(t1−u)​σ2​(𝔼​[Xt1−u])​𝑑u.\displaystyle\hskip 1.42271pt={\rm Var}(X\_{0})\left((\phi-f\_{\lambda}\*\phi)(t\_{1})\right)\left((\phi-f\_{\lambda}\*\phi)(t\_{2})\right)+\frac{1}{\lambda^{2}}\int\_{0}^{t\_{1}}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)\varsigma^{2}(t\_{1}-u)\sigma^{2}(\mathbb{E}\left[X\_{t\_{1}-u}\right])du. |  |

where in the last equality, we have used the particular affine form of σ2​(x)\sigma^{2}(x).
Consequently, the autocovariance function of the the assymptotic (stationary) process is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | cov​(Xt2∞,Xt1∞)\displaystyle\mathrm{cov}(X\_{t\_{2}}^{\infty},X\_{t\_{1}}^{\infty}) | =limt→∞Cov​(Xt+t1,Xt+t2)=Var​(X0)​limt→∞((ϕ−fλ∗ϕ)​(t+t1))​((ϕ−fλ∗ϕ)​(t+t2))\displaystyle=\lim\_{t\to\infty}{\rm Cov}(X\_{t+t\_{1}},X\_{t+t\_{2}})={\rm Var}(X\_{0})\lim\_{t\to\infty}\left((\phi-f\_{\lambda}\*\phi)(t+t\_{1})\right)\left((\phi-f\_{\lambda}\*\phi)(t+t\_{2})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1λ2​limt→∞∫0t+t1fλ​(t2−t1+u)​fλ​(u)​ς2​(t+t1−u)​σ2​(𝔼​[Xt+t1−u])​𝑑u\displaystyle\hskip 56.9055pt+\frac{1}{\lambda^{2}}\lim\_{t\to\infty}\int\_{0}^{t+t\_{1}}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)\varsigma^{2}(t+t\_{1}-u)\sigma^{2}(\mathbb{E}\left[X\_{t+t\_{1}-u}\right])du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a2​ϕ∞2​Var​(X0)+1λ2​ς∞2​σ2​(a​ϕ∞​𝔼​[X0]+(1−a)​μ∞λ)​∫0+∞fλ​(t2−t1+u)​fλ​(u)​𝑑u.\displaystyle=a^{2}\phi^{2}\_{\infty}{\rm Var}(X\_{0})+\frac{1}{\lambda^{2}}\varsigma^{2}\_{\infty}\;\sigma^{2}\left(a\phi\_{\infty}\mathbb{E}[X\_{0}]+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)\int\_{0}^{+\infty}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)du. |  |

where the last equality follows from the fact that fλ(t2−t1+⋅)fλ∈ℒ2(Leb1)f\_{\lambda}(t\_{2}-t\_{1}+\cdot)f\_{\lambda}\!\in{\cal L}^{2}({\rm Leb}\_{1}) since fλ∈ℒ2​(Leb1)f\_{\lambda}\!\in{\cal L}^{2}({\rm Leb}\_{1}) (assumption (𝒦)​(i​i)(\mathcal{K})(ii)), 1{0≤u≤t+t1}ς2(t+t1−u)→limt→+∞ς2(t)=:ς∞2\mbox{\bf 1}\_{\{0\leq u\leq t+t\_{1}\}}\varsigma^{2}(t+t\_{1}-u)\to\lim\_{t\to+\infty}\varsigma^{2}(t)=:\varsigma^{2}\_{\infty} for every u∈ℝ+u\!\in\mathbb{R}\_{+} as t→+∞t\to+\infty (owing to [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Lemma 3.9]) and limt→+∞(ϕ−fλ∗ϕ)​(t)=a​ϕ∞\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)(t)=a\phi\_{\infty} (owing to assumption (𝒦)​(i​i​i)(\mathcal{K})(iii) in [2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

Step 3
Take n∈ℕn\in\mathbb{N} and let 0≤t1<⋯<tn0\leq t\_{1}<\dots<t\_{n}. Applying Proposition
[5.2](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem2 "Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") for the particular choice μt1,…,tn​(d​s)=∑i=1nui​δtn−ti​(d​s)\mu\_{t\_{1},\dots,t\_{n}}(ds)=\sum\_{i=1}^{n}u\_{i}\delta\_{t\_{n}-t\_{i}}(ds),
where u1,…,un∈ℝ−u\_{1},\dots,u\_{n}\in\mathbb{R}\_{-},
we find owing to μt1,…,tn​(ℝ+)=∑i=1nui\mu\_{t\_{1},\dots,t\_{n}}(\mathbb{R}\_{+})=\sum\_{i=1}^{n}u\_{i}, that for all h≥0h\geq 0,

|  |  |  |
| --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∑i=1nui​Xti+h∞)]=limk→∞𝔼x¯0​[exp⁡(∑i=1nui​Xti+hhk)]=limk→∞𝔼x¯0​[exp⁡(∑i=1nui​Xhk+h+ti)]\displaystyle\ \mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\sum\_{i=1}^{n}u\_{i}X\_{t\_{i}+h}^{\infty}\Bigg)\Bigg]=\lim\_{k\to\infty}\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\sum\_{i=1}^{n}u\_{i}X\_{t\_{i}+h}^{h\_{k}}\Bigg)\Bigg]=\lim\_{k\to\infty}\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\sum\_{i=1}^{n}u\_{i}X\_{h\_{k}+h+t\_{i}}\Bigg)\Bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =limk→∞𝔼x¯0​[exp⁡(∫[0,hk+h+tn]Xhk+h+tn−s​μt1,…,tn​(d​s))]\displaystyle\hskip 128.0374pt=\lim\_{k\to\infty}\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\int\_{[0,\,h\_{k}+h+t\_{n}]}X\_{h\_{k}+h+t\_{n}-s}\,\mu\_{t\_{1},\dots,t\_{n}}(ds)\Bigg)\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =exp⁡[(a​ϕ∞​x¯0+(1−a)​μ∞λ)​∑i=1nui+ς∞22​σ2​(a​ϕ∞​x¯0+(1−a)​μ∞λ)​∫0∞ψ2​(s,μt1,…,tn)​𝑑s].\displaystyle\hskip 8.5359pt=\exp\left[\left(a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)\sum\_{i=1}^{n}u\_{i}+\frac{\varsigma^{2}\_{\infty}}{2}\sigma^{2}\left(a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)\int\_{0}^{\infty}\psi^{2}(s,\mu\_{t\_{1},\dots,t\_{n}})ds\right]. |  | (5.60) |

Since {hk}\{h\_{k}\} is arbitrary and ([5.60](https://arxiv.org/html/2512.09590v1#S5.E60 "In 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is independent of {hk}\{h\_{k}\}, it is standard to verify the weak convergence in (b).
This proves the assertion and we are done. □\square

The particular form of the Laplace transform for the limiting distribution in Theorem [5.3](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem3 "Theorem 5.3 (Limiting Distribution). ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and the stationary process X∞X^{\infty} in Theorem [5.5](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem5 "Theorem 5.5 (Long run theorem: Functional weak asymptotics and Stationary Process). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") give the following characterization for the independence on the initial condition X0∈Lp​(ℙ)X\_{0}\in L^{p}(\mathbb{P}) for some suitable p>0p>0.

###### Corollary 5.6.

Let XX be the time-inhomogeneous affine Volterra Equation with the diffusion coefficient σ\sigma given by ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and let λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}. Let also the initial state be X0∈Lp​(ℙ)X\_{0}\in L^{p}(\mathbb{P}) for some suitable p>0p>0 and x¯0\bar{x}\_{0} a realization of X0X\_{0}. Suppose that assumption [2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") holds,then the following are equivalent:

1. (i)

   The stationary process X∞X^{\infty} is independent of x¯0\bar{x}\_{0};
2. (ii)

   The limiting distribution πx¯0\pi\_{\bar{x}\_{0}} is independent of x¯0\bar{x}\_{0};
3. (iii)

   The function x¯0⟼∫ℝ+x​πx¯0​(d​x)\bar{x}\_{0}\longmapsto\int\_{\mathbb{R}\_{+}}x\pi\_{\bar{x}\_{0}}(dx) is constant;
4. (iv)

   a:=limt→+∞Rλ​(t)=0a:=\lim\_{t\to+\infty}R\_{\lambda}(t)=0 or ϕ∞:=limt→+∞ϕ​(t)=0\phi\_{\infty}:=\lim\_{t\to+\infty}\phi(t)=0.

So that in case the particular case ϕ∞=0\phi\_{\infty}=0, ς∞2\varsigma^{2}\_{\infty} being defined by equation ([5.53](https://arxiv.org/html/2512.09590v1#S5.E53 "In Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞𝔼​[exp⁡(∫0tXt−s​μ​(d​s))]\displaystyle\lim\_{t\to\infty}\mathbb{E}\Bigg[\exp\Bigg(\int\_{0}^{t}X\_{t-s}\,\mu(ds)\Bigg)\Bigg] | =exp⁡[(1−a)​μ∞λ​μ​(ℝ+)+ς∞22​σ2​((1−a)​μ∞λ)​∫0∞ψ​(s,μ)2​𝑑s]\displaystyle=\exp\left[(1-a)\frac{\mu\_{\infty}}{\lambda}\;\mu(\mathbb{R}\_{+})+\frac{\varsigma^{2}\_{\infty}}{2}\sigma^{2}\left((1-a)\frac{\mu\_{\infty}}{\lambda}\right)\int\_{0}^{\infty}\psi(s,\mu)^{2}ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡[(∫0∞ψ​(s,μ)​𝑑s)​μ∞+κ02​ς∞2​∫0∞ψ2​(s,μ)​𝑑s].\displaystyle=\exp\left[\Big(\int\_{0}^{\infty}\psi(s,\mu)\,ds\Big)\mu\_{\infty}+\frac{\kappa\_{0}}{2}\varsigma^{2}\_{\infty}\int\_{0}^{\infty}\psi^{2}(s,\mu)\,ds\right]. |  |

Proof of Corollary [5.6](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem6 "Corollary 5.6. ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").

Since πx¯0\pi\_{\bar{x}\_{0}} is the law of Xt∞X\_{t}^{\infty}, clearly (i) implies (ii), and (ii) implies (iii). Suppose that (iii) holds. Using the first moment for the stationary process, we have ∫ℝ+y​πx¯0​(d​y)=𝔼x¯0​[Xt∞]:=ξ¯0=a​ϕ∞​x¯0+(1−a)​μ∞λ\int\_{\mathbb{R}\_{+}}y\pi\_{\bar{x}\_{0}}(dy)=\mathbb{E}\_{\bar{x}\_{0}}[X\_{t}^{\infty}]:=\bar{\xi}\_{0}=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}, which depends of x¯0\bar{x}\_{0} unless a=0a=0 or ϕ∞=0\phi\_{\infty}=0 in which case ∫ℝ+x​πx¯0​(d​x)\int\_{\mathbb{R}\_{+}}x\pi\_{\bar{x}\_{0}}(dx) reduces to (1−a)​μ∞λ(1-a)\frac{\mu\_{\infty}}{\lambda}, thus readily yields (iv). Finally, suppose that (iv) is satisfied. Then, the Laplace transform for the stationary process implies that X∞X^{\infty} is independent of x¯0\bar{x}\_{0}, i.e., (i) holds, then
no matter what the initial condition is, the limiting behaviour does not depend on that initial condition. □\square

###### Theorem 5.7 (Functional asymptotics in the Fake Stationarity Regime.).

Consider a fake stationary affine Volterra equation with λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}, where ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, assumed to be the unique continuous solution to Equation ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
for some c>0c>0 (so that condition (Eλ,cE\_{\lambda,c}) is satisfied).

Under the same conditions as in Theorem [5.5](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem5 "Theorem 5.5 (Long run theorem: Functional weak asymptotics and Stationary Process). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."),
if the solution (Xt)t≥0(X\_{t})\_{t\geq 0} of the volterra equation ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) has a fake stationary regime of type I, starting from a random variable X0X\_{0} with mean x∞:=1−a1−a​ϕ∞​μ∞λx\_{\infty}:=\frac{1-a}{1-a\phi\_{\infty}}\frac{\mu\_{\infty}}{\lambda} and variance v0v\_{0} i.e. X0∈ℳ2​(x∞,v0)X\_{0}\in\mathcal{M}\_{2}\!\left(x\_{\infty},\,v\_{0}\right). Then,

(a) The identities ([5.51](https://arxiv.org/html/2512.09590v1#S5.E51 "In Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([5.52](https://arxiv.org/html/2512.09590v1#S5.E52 "In Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) become (where ξ¯0=a​ϕ∞​x¯0+(1−a)​μ∞λ\bar{\xi}\_{0}=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞𝔼x¯0​[exp⁡(∫0tXt−s​μ​(d​s))]=exp⁡[ξ¯0​μ​(ℝ+)+12​c​λ2​(1−a2​ϕ∞2)‖fλ‖L2​(Leb1)2​σ2​(ξ¯0)​∫0∞ψ2​(s,μ)​𝑑s]\displaystyle\ \lim\_{t\to\infty}\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\int\_{0}^{t}X\_{t-s}\,\mu(ds)\Bigg)\Bigg]=\exp\left[\bar{\xi}\_{0}\mu(\mathbb{R}\_{+})+\frac{1}{2}\frac{c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})}{\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}}\sigma^{2}\left(\bar{\xi}\_{0}\right)\int\_{0}^{\infty}\psi^{2}(s,\mu)ds\right] |  | (5.61) |
|  |  |  |
| --- | --- | --- |
|  | =exp⁡[(μ​(ℝ+)+∫0∞F∞​(ψ​(s,μ))​𝑑s)​ϕ∞​x¯0+(∫0∞ψ​(s,μ)​𝑑s)​μ∞+κ02​c​λ2​(1−a2​ϕ∞2)‖fλ‖L2​(Leb1)2​∫0∞ψ2​(s,μ)​𝑑s].\displaystyle=\exp\left[\Big(\mu(\mathbb{R}\_{+})+\int\_{0}^{\infty}F\_{\infty}(\psi(s,\mu))\,ds\Big)\,\phi\_{\infty}\bar{x}\_{0}+\Big(\int\_{0}^{\infty}\psi(s,\mu)\,ds\Big)\mu\_{\infty}+\frac{\kappa\_{0}}{2}\frac{c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})}{\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}}\int\_{0}^{\infty}\psi^{2}(s,\mu)\,ds\right]. |  |

In particular, the final distribution in the fake stationary regime does not depend on the initial distribution whenever a=0a=0 or ϕ∞=0\phi\_{\infty}=0, even if they have the same mean and variance.

(b) The family of shifted processes Xt+⁣⋅,t≥0X\_{t+\cdot},t\geq 0, is CC-tight as t→+∞t\to+\infty and its (functional) limiting distributions are all at least weak L2L^{2}-stationary888see for example [[32](https://arxiv.org/html/2512.09590v1#bib.bib32)] for the definition of weak stationarity. processes with mean limt→∞𝔼​[Xt]:=𝔼​[Xt∞]=x∞\lim\_{t\to\infty}\mathbb{E}[X\_{t}]:=\mathbb{E}[X\_{t}^{\infty}]=x\_{\infty} and covariance function C∞C\_{\infty} given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t1,t2≥0​with​t1≤t2​C∞​(t1,t2)=a2​ϕ∞2​v0+c​(1−a2​ϕ∞2)λ2​‖fλ‖L2​(Leb1)2​σ2​(x∞)​∫0∞fλ​(t2−t1+u)​fλ​(u)​𝑑u.\forall t\_{1},t\_{2}\geq 0\quad\text{with}\quad t\_{1}\leq t\_{2}\quad C\_{\infty}(t\_{1},t\_{2})=a^{2}\phi^{2}\_{\infty}v\_{0}+\frac{c(1-a^{2}\phi^{2}\_{\infty})}{\lambda^{2}\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}}\sigma^{2}\left(x\_{\infty}\right)\int\_{0}^{\infty}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)\,du. |  | (5.62) |

(c) The finite dimensional distributions of X∞X^{\infty} are determined by (n∈ℕ,u1,…,un∈ℝ−n\in\mathbb{N},\;u\_{1},\dots,u\_{n}\in\mathbb{R}\_{-} and 0≤t1<⋯<tn0\leq t\_{1}<\dots<t\_{n}) (where ξ¯0=a​ϕ∞​x¯0+(1−a)​μ∞λ\bar{\xi}\_{0}=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda} and x¯0​ a realization of ​X0∈ℳ2​(x∞,v0)\bar{x}\_{0}\text{ a realization of }X\_{0}\in\mathcal{M}\_{2}\!\left(x\_{\infty},\,v\_{0}\right)):

|  |  |  |
| --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∑i=1nui​Xti∞)]=exp⁡[ξ¯0​∑i=1nui+c​λ2​(1−a2​ϕ∞2)2​‖fλ‖L2​(Leb1)2​σ2​(ξ¯0)​∫0∞ψ​(s)2​𝑑s].\ \mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\sum\_{i=1}^{n}u\_{i}X\_{t\_{i}}^{\infty}\Bigg)\Bigg]=\exp\left[\bar{\xi}\_{0}\sum\_{i=1}^{n}u\_{i}+\frac{c\lambda^{2}(1-a^{2}\phi^{2}\_{\infty})}{2\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}}\sigma^{2}\left(\bar{\xi}\_{0}\right)\int\_{0}^{\infty}\psi(s)^{2}ds\right]. |  |

where
ψ​(⋅)=ψ​(⋅,μt1,…,tn)\psi(\cdot)=\psi(\cdot,\mu\_{t\_{1},\dots,t\_{n}}) denotes the unique solution of ([3.27](https://arxiv.org/html/2512.09590v1#S3.E27 "In Corollary 3.5. ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) in ℝ+\mathbb{R}\_{+} with μt1,…,tn​(d​s)=∑j=1nuj​δtn−tj​(d​s).\mu\_{t\_{1},\dots,t\_{n}}(ds)\;=\;\sum\_{j=1}^{n}u\_{j}\,\delta\_{\,t\_{n}-t\_{j}}(ds).

Proof of Theorem [5.7](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem7 "Theorem 5.7 (Functional asymptotics in the Fake Stationarity Regime.). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
The claims (a) and (c) are straightforward consequences of Theorem [5.5](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem5 "Theorem 5.5 (Long run theorem: Functional weak asymptotics and Stationary Process). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), and equation ([5.62](https://arxiv.org/html/2512.09590v1#S5.E62 "In Theorem 5.7 (Functional asymptotics in the Fake Stationarity Regime.). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) in (b) follows by noticing that in the Fake stationarity regime, 𝔼​[X0]=x∞\mathbb{E}[X\_{0}]=x\_{\infty} and ς∞2:=limt→+∞ς2​(t)=c​λ2​(1−a2​ϕ∞2)‖fλ‖L2​(Leb1)2\varsigma^{2}\_{\infty}:=\lim\_{t\to+\infty}\varsigma^{2}(t)=\frac{c\lambda^{2}(1-a^{2}\phi^{2}\_{\infty})}{\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}} owing to [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Lemma 3.9 ]. □\square

## 6 Applications: The case of Fake Stationary Volterra CIR process.

In this section, we provide a broad class of applications, starting from the fake stationary fractional-CIR Process to the long run behaviour of fake stationary Volterra-CIR process with an exponentially damped fractional integration kernel .

### 6.1 A Numerical illustration: The Fake Stationary Fractional-CIR Process.

For the numerical illustration, we consider α\alpha-fractional kernels with α∈(12,1)\alpha\in\left(\frac{1}{2},1\right) (corresponding to “rough models”) and α∈(1,32)\alpha\in\left(1,\frac{3}{2}\right) (corresponding to “long memory models”), within the setting where
ϕ​(t)=ϕ​(0)=1for all ​t≥0almost surely.\phi(t)=\phi(0)=1\quad\text{for all }t\geq 0\quad\text{almost surely}.
In this case, the equation simplifies in the so-called fake stationarity regime (i.e., θ​(t)=θ0\theta(t)=\theta\_{0} and σ​(x)=ν​x\sigma(x)=\nu\sqrt{x}) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=θ0λ+(X0−θ0λ)​Rλ​(t)+νλ​∫0tfα,λ​(t−s)​ς​(s)​Xs​𝑑Ws.X\_{t}=\frac{\theta\_{0}}{\lambda}+\Big(X\_{0}-\frac{\theta\_{0}}{\lambda}\Big)R\_{\lambda}(t)+\frac{\nu}{\lambda}\int\_{0}^{t}f\_{\alpha,\lambda}(t-s)\varsigma(s)\sqrt{X\_{s}}dW\_{s}. |  | (6.63) |

We now focus on α−\alpha- fractional kernels K​(t)=Kα,0​(t)=Kα​(t)=tα−1Γ​(α)​𝟏ℝ+​(t),α>0K(t)=K\_{\alpha,0}(t)=K\_{\alpha}(t)=\frac{t^{\alpha-1}}{\Gamma(\alpha)}\mathbf{1}\_{\mathbb{R}\_{+}}(t),\;\alpha>0 for which we have the following (Recall also from Example [2.1](https://arxiv.org/html/2512.09590v1#S2.ThmTheorem1 "Example 2.1 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") with ρ=0\rho=0):

(1). The identity Kα∗Kα′=Kα+α′K\_{\alpha}\*K\_{\alpha^{\prime}}=K\_{\alpha+\alpha^{\prime}} holds for t≥0t\geq 0 so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rα,λ​(t)=∑k≥0(−1)k​λk​tα​kΓ​(α​k+1)=Eα​(−λ​tα),and ​fα,λ​(t)=−Rα,λ′​(t)=λ​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1)).R\_{\alpha,\lambda}(t)=\sum\_{k\geq 0}(-1)^{k}\frac{\lambda^{k}t^{\alpha k}}{\Gamma(\alpha k+1)}=E\_{\alpha}(-\lambda t^{\alpha}),\;\text{and }\;f\_{\alpha,\lambda}(t)=-R^{\prime}\_{\alpha,\lambda}(t)=\lambda t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\lambda^{k}\frac{t^{\alpha k}}{\Gamma(\alpha(k+1))}. |  | (6.64) |

(2). Here, EαE\_{\alpha} denotes the standard Mittag-Leffler function and a:=limt→∞Rα,λ​(t)=0a:=\lim\_{t\to\infty}R\_{\alpha,\lambda}(t)=0 by a Tauberian Final Value argument (see also section [6.3](https://arxiv.org/html/2512.09590v1#S6.SS3 "6.3 Long-run behaviour of the Fake Stationary Volterra-CIR with a Gamma Kernel ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") below).

We have the below proposition, which is the main takeaway from [[35](https://arxiv.org/html/2512.09590v1#bib.bib35), Sections 5.1 and 5.2 ] and [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 5.5 and Proposition 5.6].

###### Proposition 6.1 (Existence and Properties of the function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} for α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2})).

Let α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2}) and c>0c>0. Set ak=1Γ​(α​k+1),bk=1Γ​(α​(k+1)),k≥0a\_{k}=\frac{1}{\Gamma(\alpha k+1)},b\_{k}=\frac{1}{\Gamma(\alpha(k+1))},\;k\geq 0.

The stabilizer ς=ζα,λ,c\varsigma=\zeta\_{\alpha,\lambda,c} exists as a non-negative function, on (0,+∞)(0,+\infty), such that:

1. limt→0ζα,λ,c={0​ if ​α≤1,+∞​ if ​α>1,andlimt→+∞ζα,λ,c​(t)=c​λ‖fα,λ‖L2​(Leb1).\lim\_{t\to 0}\zeta\_{\alpha,\lambda,c}=\left\{\begin{array}[]{ll}&0\text{ if }\alpha\leq 1,\\
&+\infty\text{ if }\alpha>1,\end{array}\quad\text{and}\quad\lim\_{t\to+\infty}\zeta\_{\alpha,\lambda,c}(t)=\frac{\sqrt{c}\lambda}{\|f\_{\alpha,\lambda}\|\_{L^{2}(\text{Leb}\_{1})}}.\right.

2.
ςα,λ,c2​(t)=c​λ2−1α​ςα2​(λ1α​t)\varsigma^{2}\_{\alpha,\lambda,c}(t)=c\lambda^{2-\frac{1}{\alpha}}\varsigma\_{\alpha}^{2}(\lambda^{\frac{1}{\alpha}}t) where ςα2​(t):=2​t1−α​∑k≥0(−1)k​ck​tα​k\varsigma\_{\alpha}^{2}(t):=2\,t^{1-\alpha}\sum\_{k\geq 0}(-1)^{k}c\_{k}t^{\alpha k} and the coefficients (ck)k≥0(c\_{k})\_{k\geq 0} are defined by the following recurrence formula:

|  |  |  |
| --- | --- | --- |
|  | c0=Γ​(α)2Γ​(2​α−1)​Γ​(2−α) and for everyk≥1,c\_{0}=\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)\Gamma(2-\alpha)}\quad\textit{ and for every}\quad k\geq 1, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ck=Γ​(α)2​Γ​(α​(k+1))Γ​(2​α−1)​Γ​(α​k+2−α)​[(a∗b)k−α​(k+1)​∑ℓ=1kB​(α​(ℓ+2)−1,α​(k−ℓ−1)+2)​(b∗2)ℓ​ck−ℓ].c\_{k}=\frac{\Gamma(\alpha)^{2}\Gamma(\alpha(k+1))}{\Gamma(2\alpha-1)\Gamma(\alpha k+2-\alpha)}\left[(a\*b)\_{k}-\alpha(k+1)\sum\_{\ell=1}^{k}B\big(\alpha(\ell+2)-1,\alpha(k-\ell-1)+2\big)(b^{\*2})\_{\ell}c\_{k-\ell}\right]. |  | (6.65) |

where for two sequences of real numbers (uk)k≥0(u\_{k})\_{k\geq 0} and (vk)k≥0(v\_{k})\_{k\geq 0}, the Cauchy product is defined as (u∗v)k=∑ℓ=0kuℓ​vk−ℓ(u\*v)\_{k}=\sum\_{\ell=0}^{k}u\_{\ell}v\_{k-\ell} and B​(a,b)=∫01ua−1​(1−u)b−1​𝑑uB(a,b)=\int\_{0}^{1}u^{a-1}(1-u)^{b-1}du denoting the beta function.

3. The convergence radius ρα=(lim infk(|ck|1/k))−1/α\rho\_{\alpha}=\left(\liminf\_{k}\left(|c\_{k}|^{1/k}\right)\right)^{-1/\alpha} of the fractional power series ∑k≥0ck​tα​k\sum\_{k\geq 0}c\_{k}t^{\alpha k}, defined by the coefficients ckc\_{k}, is infinite.
As a consequence, the expansion which define ζα,λ,c2\zeta\_{\alpha,\lambda,c}^{2} converges for all t∈ℝ+t\in\mathbb{R}^{+}, and in fact, for all t∈ℝt\in\mathbb{R}. Thus ζα,λ,c\zeta\_{\alpha,\lambda,c}
is positive on (0,+∞)(0,+\infty) so that ςα,λ,c\varsigma\_{\alpha,\lambda,c} is
well-defined.

Remark:
Note that in the expansion of ςα,λ,c2\varsigma^{2}\_{\alpha,\lambda,c} defines in Proposition [6.1](https://arxiv.org/html/2512.09590v1#S6.ThmTheorem1 "Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.1 A Numerical illustration: The Fake Stationary Fractional-CIR Process. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (2), the coefficients (ck)k≥0(c\_{k})\_{k\geq 0} are determined recursively via identification with those of the expansion of Rα,λR\_{\alpha,\lambda} in ([6.64](https://arxiv.org/html/2512.09590v1#S6.E64 "In 6.1 A Numerical illustration: The Fake Stationary Fractional-CIR Process. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
Moreover, if α<1\alpha<1, the non-negativity of the above series hold on the whole positive real line ℝ+\mathbb{R}\_{+} and consequently the finiteness
of ςα,λ,c​(t)\varsigma\_{\alpha,\lambda,c}(t) in [0,+∞)[0,+\infty). Also, ςα,λ,c​(t)\varsigma\_{\alpha,\lambda,c}(t) in this case is a nonnegative, non-increasing concave function (See [[35](https://arxiv.org/html/2512.09590v1#bib.bib35)] or [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Propostion 6.3]).

![Refer to caption](x1.png)


Figure 1:  Graph of the stabilizer t→ςα,λ,c​(t)t\to\varsigma\_{\alpha,\lambda,c}(t) over time interval [0, T ], T = 100 for a value of the Hurst esponent H=0.4H=0.4, λ=0.2\lambda=0.2, c = 0.3.

![Refer to caption](x2.png)


Figure 2:  Graph of the stabilizer t→ςα,λ,c​(t)t\to\varsigma\_{\alpha,\lambda,c}(t) over time interval [0, T ], T = 50 for a value of the Hurst esponent H=0.8H=0.8, λ=0.2\lambda=0.2, c = 0.36.

We introduce an Euler-Maruyama scheme below on the time grid tk=tkn=k​Tn,k=0,…,nt\_{k}=t^{n}\_{k}=\frac{kT}{n},k=0,\dots,n, for the semi-integrated form ([6.63](https://arxiv.org/html/2512.09590v1#S6.E63 "In 6.1 A Numerical illustration: The Fake Stationary Fractional-CIR Process. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), which write recursively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X¯tk\displaystyle\overline{X}\_{t\_{k}} | =θ0λ+(X0−θ0λ)​Rλ​(tk)+∑ℓ=1kνλ​∫tℓ−1tℓfλ​(tk−s)​ς​(tℓ)​X¯tℓ−1​𝑑Ws=g​(tk)+νλ​∑ℓ=1kς​(tℓ)​X¯tℓ−1​Ikn,l.\displaystyle=\frac{\theta\_{0}}{\lambda}+\big(X\_{0}-\frac{\theta\_{0}}{\lambda}\big)R\_{\lambda}(t\_{k})+\sum\_{\ell=1}^{k}\frac{\nu}{\lambda}\int\_{t\_{\ell-1}}^{t\_{\ell}}f\_{\lambda}(t\_{k}-s)\,\varsigma(t\_{\ell})\sqrt{\overline{X}\_{t\_{\ell-1}}}dW\_{s}=g(t\_{k})+\frac{\nu}{\lambda}\sum\_{\ell=1}^{k}\varsigma(t\_{\ell})\sqrt{\overline{X}\_{t\_{\ell-1}}}I^{n,l}\_{k}. |  |

where the integrals (Ikn,l=∫tℓ−1tℓfλ​(tk−s)​𝑑Ws)k\left(I^{n,l}\_{k}=\int\_{t\_{\ell-1}}^{t\_{\ell}}f\_{\lambda}(t\_{k}-s)dW\_{s}\right)\_{k} can be simulated on the discrete grid (tkn)0≤k≤n(t^{n}\_{k})\_{0\leq k\leq n} by generating an independent sequence of gaussian vectors Gn,l,l=1​⋯​nG^{n,l},l=1\cdots n using the Cholesky decomposition of a well-defined covariance matrix CC.
The reader is referred to Appendix A of [[23](https://arxiv.org/html/2512.09590v1#bib.bib23)] for further details on the semi-integrated Euler scheme introduced in this context for the above equation.
The reader is also invited to consult the captions of the various figures for the numerical values of the parameters used in the simulation of the Volterra CIR equation.

![Refer to caption](x3.png)


Figure 3: Graph of tk↦StdDev​(tk,M)t\_{k}\mapsto\text{StdDev}(t\_{k},M) and tk↦𝔼​[σ2​(Xtk,M)]t\_{k}\mapsto\mathbb{E}[\sigma^{2}(X\_{t\_{k}},M)] over the time interval [0,T][0,T], T=1T=1, H=0.8H=0.8, θ0=2\theta\_{0}=2, λ=0.2\lambda=0.2, v0=0.09v\_{0}=0.09, and StdDev​(X0)=0.3\text{StdDev}(X\_{0})=0.3, ν=1\nu=1. Number of steps: n=800n=800, Simulation size: M=150000M=150000.

![Refer to caption](x4.png)


Figure 4: Graph of tk↦StdDev​(tk,M)t\_{k}\mapsto\text{StdDev}(t\_{k},M) and tk↦𝔼​[σ2​(Xtk,M)]t\_{k}\mapsto\mathbb{E}[\sigma^{2}(X\_{t\_{k}},M)] over the time interval [0,T][0,T], T=1T=1, H=0.4H=0.4, θ0=2\theta\_{0}=2, λ=0.2\lambda=0.2, v0=0.09v\_{0}=0.09, and StdDev​(X0)=0.3\text{StdDev}(X\_{0})=0.3, ν=1\nu=1, n=800n=800, M=100000M=100000.

![Refer to caption](x5.png)


Figure 5: Graph of tk↦StdDev​(tk,M)t\_{k}\mapsto\text{StdDev}(t\_{k},M) and tk↦𝔼​[σ2​(Xtk,M)]t\_{k}\mapsto\mathbb{E}[\sigma^{2}(X\_{t\_{k}},M)] over the time interval [0,T][0,T], T=1T=1, H=0.1H=0.1, θ0=2\theta\_{0}=2, λ=0.2\lambda=0.2, v0=0.09v\_{0}=0.09, and StdDev​(X0)=0.3\text{StdDev}(X\_{0})=0.3, ν=1\nu=1, n=800n=800, M=100000M=100000.

### 6.2 An illustration of the Fake Stationary Rough Heston Model.

![Refer to caption](Images/Curve_meanSigma_VarianceS.png)


Figure 6: Graph of tk↦Var​(Vtk,M)t\_{k}\mapsto\text{Var}(V\_{t\_{k}},M) over the time interval [0,1][0,1], H=0.1H=0.1, θ0=2\theta\_{0}=2, λ=0.2\lambda=0.2, Var​(V0)=v0=0.09\text{Var}(V\_{0})=v\_{0}=0.09, and ν=0.05\nu=0.05. Number of steps: n=600n=600, Simulation size: M=100000M=100000.

![Refer to caption](x6.png)


Figure 7: Graph of one sample of tk↦Stkt\_{k}\mapsto S\_{t\_{k}} and tk↦σ​(Vtk)t\_{k}\mapsto\sigma(V\_{t\_{k}}) over time interval [0,1][0,1], H=0.1H=0.1, θ0=2\theta\_{0}=2, λ=0.2\lambda=0.2, Var​(V0)=v0=0.09\text{Var}(V\_{0})=v\_{0}=0.09, ρ=−0.5\rho=-0.5 and ν=0.05\nu=0.05. Number of steps: n=600n=600.

Many methods are used in the industry to encode implied-volatility information,
including non-parametric grids of implied volatilities with spline interpolation,
direct modelling of the asset’s implied density, surface-level parametrizations followed by AI-driven fitting as in [[22](https://arxiv.org/html/2512.09590v1#bib.bib22)] and
diffusion-based models such as (L)SV models, to which the Fake Stationary Volterra–Heston model belongs (Figures [7](https://arxiv.org/html/2512.09590v1#S6.F7 "Figure 7 ‣ 6.2 An illustration of the Fake Stationary Rough Heston Model. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and [7](https://arxiv.org/html/2512.09590v1#S6.F7 "Figure 7 ‣ 6.2 An illustration of the Fake Stationary Rough Heston Model. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
The model has a few set of parameter κ=(α,λ,ρ,c,ν,θ0)\kappa=(\alpha,\lambda,\rho,c,\nu,\theta\_{0}) and then we deduce from Proposition [4.4](https://arxiv.org/html/2512.09590v1#S4.ThmTheorem4 "Proposition 4.4 ((Fake stationary regimes (types I and II) and first asymptotics) ). ‣ 4.2 Fake stationary regimes of affine Volterra process and first asymptotics ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") that v0=c​ν2​θ0λv\_{0}=c\nu^{2}\frac{\theta\_{0}}{\lambda}.
The parameter sets in Table ([1](https://arxiv.org/html/2512.09590v1#S6.T1 "Table 1 ‣ 6.2 An illustration of the Fake Stationary Rough Heston Model. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) are, up to rounding and disregarding cc,λ\lambda and θ0\theta\_{0} taken from [[14](https://arxiv.org/html/2512.09590v1#bib.bib14)], where they are obtained by calibration to SPX options. They therefore represent realistic test cases.

| κ\kappa | α=H+12\alpha=H+\frac{1}{2} | λ\lambda | ρ\rho | cc | ν\nu | θ0\theta\_{0} |
| --- | --- | --- | --- | --- | --- | --- |
| Fake Stationary Rough Heston | 0.12+12\frac{1}{2} | 5.05.0 | −0.6714-0.6714 | 0.560.56 | 0.29100.2910 | 0.20 |

Table 1: Parameters for the Fake Stationary Rough Heston Model.

The implied volatility σivModel​(κ,K,T)\sigma\_{\textsc{iv}}^{\mathrm{Model}}(\kappa,K,T) denote the Black–Scholes volatility σ\sigma that matches the European option price given by the Fake Stationary Rough Heston model with the set of parameters κ\kappa obtained for example and amongst others by Fourier techniques using the characteristic function or by Monte-Carlo simulations with antithetic sampling, i.e., simulating two paths VV and V(2)V^{(2)} driven by WW and −W-W respectively.

In the following figure [8](https://arxiv.org/html/2512.09590v1#S6.F8 "Figure 8 ‣ 6.2 An illustration of the Fake Stationary Rough Heston Model. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we represent the term structure of volatility as a function of the strike KK for two expiries, where the strike is expressed relative to the spot S0S\_{0} (moneyness).

![Refer to caption](Images/iv_smile_20ds.png)

![Refer to caption](Images/iv_smile_40ds.png)

Figure 8: Implied volatilities for 2020 (left) and 4040 (right) days expiry options(S0=5489.83S\_{0}=5489.83 and r=q=0.0r=q=0.0). Number of steps: n=600n=600, Simulation size: M=300000M=300000.

It is clear in Figure [8](https://arxiv.org/html/2512.09590v1#S6.F8 "Figure 8 ‣ 6.2 An illustration of the Fake Stationary Rough Heston Model. ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") that the Fake Stationary Rough Heston Model succeeds at producing or generating the desired smile for different maturities.

### 6.3 Long-run behaviour of the Fake Stationary Volterra-CIR with a Gamma Kernel

In this section we briefly state our results when applied to the Volterra Cox-Ingersoll-Ross process with a Gamma or Exponential-fractional integration kernel obtained up to the existence of a weak solution (see [[37](https://arxiv.org/html/2512.09590v1#bib.bib37)]) from

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xt\displaystyle X\_{t} | =x0(t)+∫0tK(t−s)(θ(s)−λXs)ds+ν∫0tK(t−s)ςλ,c(s)XsdWs,X0⟂⟂W.\displaystyle=x\_{0}(t)+\int\_{0}^{t}K(t-s)(\theta(s)-\lambda X\_{s})ds+\nu\int\_{0}^{t}K(t-s)\varsigma\_{\lambda,c}(s)\sqrt{X\_{s}}dW\_{s},\quad X\_{0}\perp\!\!\!\perp W. |  | (6.66) |

where K​(t)=Kα,ρ​(t)=e−ρ​t​tα−1Γ​(α)​𝟏ℝ​(t)K(t)=K\_{\alpha,\rho}(t)=e^{-\rho t}\frac{t^{\alpha-1}}{\Gamma(\alpha)}\mathbf{1}\_{\mathbb{R}}(t),
α∈(12,1)\alpha\in(\frac{1}{2},1),x0=X0​ϕx\_{0}=X\_{0}\phi, λ,σ,b,X0≥0\lambda,\sigma,b,X\_{0}\geq 0, β∈ℝ\beta\in\mathbb{R}, and (Wt)t≥0(W\_{t})\_{t\geq 0} is a one-dimensional Brownian motion and ςλ,c\varsigma\_{\lambda,c} is the solution of (Eλ,cE\_{\lambda,c}) in equation ([4.34](https://arxiv.org/html/2512.09590v1#S4.E34 "In Proposition 4.2 (Time-Dependent Volatility Coefficient.). ‣ 4.1 Stabilizer and Fake Stationarity Regimes. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), i.e. ς∞2:=limt→+∞ςλ,c2​(t)=c​λ2​(1−a2​ϕ∞2)‖fλ‖L2​(Leb1)2\varsigma^{2}\_{\infty}:=\lim\_{t\to+\infty}\varsigma\_{\lambda,c}^{2}(t)=\frac{c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})}{\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}} owing to [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Lemma 3.9 ].
Recalling from Example [2.1](https://arxiv.org/html/2512.09590v1#S2.ThmTheorem1 "Example 2.1 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") the Exponential-fractional kernels K​(t)=Kα,ρ​(t)=e−ρ​t​tα−1Γ​(α)​𝟏ℝ+​(t),α,ρ>0K(t)=K\_{\alpha,\rho}(t)=e^{-\rho t}\frac{t^{\alpha-1}}{\Gamma(\alpha)}\mathbf{1}\_{\mathbb{R}\_{+}}(t),\;\alpha,\rho>0.

(1). By definition, ℒ​[Rα,ρ,λ]​(s)=1s​(1+ℒ​[Kα,ρ]​(s))=1s​(1+λ​(s+ρ)−α)\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)=\frac{1}{s(1+\mathcal{L}[K\_{\alpha,\rho}](s))}=\frac{1}{s(1+\lambda(s+\rho)^{-\alpha})} (owing to Example [2.1](https://arxiv.org/html/2512.09590v1#S2.ThmTheorem1 "Example 2.1 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))
so that, by the Tauberian Final Value Theorem 999f:[0,∞)→ℂf:[0,\infty)\to\mathbb{C} continuous,
limt→∞f​(t)=f∞\lim\_{t\to\infty}f(t)=f\_{\infty}, the Laplace transform Lf​(s)L\_{f}(s) exists for s>0s>0 and
lims→0+s​Lf​(s)=f∞.\lim\_{s\to 0^{+}}sL\_{f}(s)=f\_{\infty}. (see. for e.g. [[5](https://arxiv.org/html/2512.09590v1#bib.bib5)]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | a:=limt→∞Rα,ρ,λ​(t)=lims→0s​ℒ​[Rα,ρ,λ]​(s)=11+λ​ρ−α∈[0,1).a:=\lim\_{t\to\infty}R\_{\alpha,\rho,\lambda}(t)=\lim\_{s\to 0}s\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)=\frac{1}{1+\lambda\rho^{-\alpha}}\in[0,1). |  | (6.67) |

(2). If λ>0\lambda>0, we define the function fα,ρ,λ:=−Rα,ρ,λf\_{\alpha,\rho,\lambda}:=-R\_{\alpha,\rho,\lambda} on (0,+∞)(0,+\infty) (see ([2.15](https://arxiv.org/html/2512.09590v1#S2.E15 "In Example 2.1 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) in Example[2.1](https://arxiv.org/html/2512.09590v1#S2.ThmTheorem1 "Example 2.1 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.1 Fourier-Laplace Transforms and Resolvent of Convolutive Kernels ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) by noticing that :

|  |  |  |
| --- | --- | --- |
|  | ℒ​[fα,ρ,λ]​(s)=ℒ​[−Rα,ρ,λ′]​(s)=−s​ℒ​[Rα,ρ,λ]​(s)+Rα,ρ,λ​(0)=−ss​(1+λ​(s+ρ)−α)+1=λλ+(s+ρ)α=ℒ​[e−ρ⁣⋅​fα,λ]​(s)\mathcal{L}[f\_{\alpha,\rho,\lambda}](s)=\mathcal{L}[-R^{\prime}\_{\alpha,\rho,\lambda}](s)=-s\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)+R\_{\alpha,\rho,\lambda}(0)=\frac{-s}{s(1+\lambda(s+\rho)^{-\alpha})}+1=\frac{\lambda}{\lambda+(s+\rho)^{\alpha}}=\mathcal{L}[e^{-\rho\cdot}f\_{\alpha,\lambda}](s) |  |

i.e. by injectivity of the Laplace transform, fα,ρ,λ​(t)=e−ρ​t​fα,λ​(t)=α​λ​e−ρ​t​tα−1​Eα′​(−λ​tα).f\_{\alpha,\rho,\lambda}(t)=e^{-\rho t}f\_{\alpha,\lambda}(t)=\alpha\lambda e^{-\rho t}t^{\alpha-1}E^{\prime}\_{\alpha}(-\lambda t^{\alpha}).
Likewise, using Tauberian Final Value Theorem, limt→∞fα,ρ,λ​(t)=lims→0s​ℒ​[−Rα,ρ,λ′]​(s)\lim\_{t\to\infty}f\_{\alpha,\rho,\lambda}(t)=\lim\_{s\to 0}s\mathcal{L}[-R^{\prime}\_{\alpha,\rho,\lambda}](s), that is

|  |  |  |
| --- | --- | --- |
|  | limt→∞fα,ρ,λ​(t)=−lims→0s​(s​ℒ​[Rα,ρ,λ]​(s)−Rα,ρ,λ​(0))=−lims→0s(1+λ​(s+ρ)−α)−s=0.\lim\_{t\to\infty}f\_{\alpha,\rho,\lambda}(t)=-\lim\_{s\to 0}s\left(s\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)-R\_{\alpha,\rho,\lambda}(0)\right)=-\lim\_{s\to 0}\frac{s}{(1+\lambda(s+\rho)^{-\alpha})}-s=0. |  |

Note that, by [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 6.1], the function fα,ρ,λf\_{\alpha,\rho,\lambda} satisfy the assumption [5.4](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem4 "Assumption 5.4 (Integrability and Uniform Hölder Continuity). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and the kernel K​(t)=Kα,ρ​(t)K(t)=K\_{\alpha,\rho}(t) with α∈(12,1)\alpha\in(\frac{1}{2},1) and ρ≥0\rho\geq 0 satisfies [K]η,p,T<∞[K]\_{\eta,p,T}<\infty for each T>0T>0, p=2p=2, and η∈(0,α−12)\eta\in(0,\alpha-\frac{1}{2}), see [[1](https://arxiv.org/html/2512.09590v1#bib.bib1)].

The following is our main result on limiting distributions and stationarity of the process.

###### Theorem 6.2.

Let XX be a weak solution of the stabilized Volterra Equation given by ([6.66](https://arxiv.org/html/2512.09590v1#S6.E66 "In 6.3 Long-run behaviour of the Fake Stationary Volterra-CIR with a Gamma Kernel ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). We have the following claims:

(1). XtX\_{t} converges weakly to some limiting distribution πx¯0\pi\_{\bar{x}\_{0}} when t→∞t\to\infty, and that its characteristic function is given by the expression in Theorem [5.3](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem3 "Theorem 5.3 (Limiting Distribution). ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and ψ\psi being determined from the ricatti-volterra equation ([3.27](https://arxiv.org/html/2512.09590v1#S3.E27 "In Corollary 3.5. ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) with μ​(d​s)=u​δ0​(d​s),\mu(ds)=u\,\delta\_{0}(ds),.

(2). Moreover, the process (Xt+u)t≥0(X\_{t+u})\_{t\geq 0} converges in law to a continuous stationary process (Xt∞)t≥0(X\_{t}^{\infty})\_{t\geq 0} when u→∞u\to\infty. Moreover, the finite dimensional distributions of X∞X^{\infty} have the characteristic function

|  |  |  |
| --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∑i=1nui​Xti∞)]=exp⁡[ρα​ϕ∞​x¯0+μ∞ρα+λ​(∑i=1nui+ς∞22​ν2​∫0∞ψ​(s)2​𝑑s)],where\displaystyle\mathbb{E}\_{\bar{x}\_{0}}\Bigg[\exp\Bigg(\sum\_{i=1}^{n}u\_{i}X\_{t\_{i}}^{\infty}\Bigg)\Bigg]=\exp\left[\frac{\rho^{\alpha}\phi\_{\infty}\bar{x}\_{0}+\mu\_{\infty}}{\rho^{\alpha}+\lambda}\left(\sum\_{i=1}^{n}u\_{i}+\frac{\varsigma^{2}\_{\infty}}{2}\nu^{2}\int\_{0}^{\infty}\psi(s)^{2}ds\right)\right],\quad\text{where} |  |

ς∞2:=c​λ2‖fα,ρ,λ‖L2​(Leb1)2​ρ2​α​(1−ϕ∞2)+λ​(2​ρα+λ)(ρα+λ)2\varsigma^{2}\_{\infty}:=\frac{c\lambda^{2}}{\|f\_{\alpha,\rho,\lambda}\|^{2}\_{L^{2}(\mathrm{Leb}\_{1})}}\frac{\rho^{2\alpha}\left(1-\phi\_{\infty}^{2}\right)+\lambda\left(2\rho^{\alpha}+\lambda\right)}{\left(\rho^{\alpha}+\lambda\right)^{2}}, 0≤t1<⋯<tn0\leq t\_{1}<\dots<t\_{n}, u1,…,un∈ℝ−u\_{1},\dots,u\_{n}\in\mathbb{R}\_{-}, and ψ\psi unique solution of

ψ​(t)=∑j=1n𝟏{t>tn−tj}​Kα,ρ​(t−(tn−tj))​uj+∫0tKα,ρ​(t−s)​(−λ​ψ​(s)+ς∞2​ν22​ψ​(s)2)​𝑑s.\psi(t)=\sum\_{j=1}^{n}\mathbf{1}\_{\{t>t\_{n}-t\_{j}\}}\,K\_{\alpha,\rho}(t-(t\_{n}-t\_{j}))u\_{j}+\int\_{0}^{t}K\_{\alpha,\rho}(t-s)\left(-\lambda\psi(s)+\varsigma^{2}\_{\infty}\frac{\nu^{2}}{2}\psi(s)^{2}\right)ds.

Moreover, the first moment and the autocovariance function of the stationary process satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[Xt∞]=ρα​ϕ∞​𝔼​[X0]+μ∞ρα+λ=μ∞λ+ρα​(1−ϕ∞),and for​t1,t2≥0,t1≤t2,\displaystyle\ \hskip 85.35826pt\mathbb{E}[X\_{t}^{\infty}]=\frac{\rho^{\alpha}\phi\_{\infty}\mathbb{E}[X\_{0}]+\mu\_{\infty}}{\rho^{\alpha}+\lambda}=\frac{\mu\_{\infty}}{\lambda+\rho^{\alpha}(1-\phi\_{\infty})},\;\text{and for}\;t\_{1},t\_{2}\geq 0,t\_{1}\leq t\_{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Cov(Xt2∞,Xt1∞)=ρ2​α(ρα+λ)2ϕ∞2Var(X0)+cν2⋅μ∞​(ρ2​α​(1−ϕ∞2)+λ​(2​ρα+λ))(ρα+λ)2​(λ+ρα​(1−ϕ∞))​‖fα,ρ,λ‖L2​(Leb1)2⋅\displaystyle\mathrm{Cov}(X\_{t\_{2}}^{\infty},X\_{t\_{1}}^{\infty})=\frac{\rho^{2\alpha}}{(\rho^{\alpha}+\lambda)^{2}}\phi\_{\infty}^{2}\,\mathrm{Var}(X\_{0})+c\nu^{2}\cdot\frac{\mu\_{\infty}\left(\rho^{2\alpha}(1-\phi\_{\infty}^{2})+\lambda(2\rho^{\alpha}+\lambda)\right)}{(\rho^{\alpha}+\lambda)^{2}(\lambda+\rho^{\alpha}(1-\phi\_{\infty}))\|f\_{\alpha,\rho,\lambda}\|^{2}\_{L^{2}(\mathrm{Leb}\_{1})}}\cdot |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×e−ρ​(t2−t1)​∫0+∞e−2​ρ​u​fα,λ​(t2−t1+u)​fα,λ​(u)​𝑑u.\displaystyle\hskip 142.26378pt\times e^{-\rho(t\_{2}-t\_{1})}\int\_{0}^{+\infty}e^{-2\rho u}f\_{\alpha,\lambda}(t\_{2}-t\_{1}+u)f\_{\alpha,\lambda}(u)\,du. |  | (6.68) |

As a consequence of that result, we see that the stationary process X∞X^{\infty} is independent of the initial distribution of X0X\_{0} or initial state x¯0\bar{x}\_{0} if and only if ρ=0\rho=0. Its boils down that a=0a=0 in equation ([6.67](https://arxiv.org/html/2512.09590v1#S6.E67 "In 6.3 Long-run behaviour of the Fake Stationary Volterra-CIR with a Gamma Kernel ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) as demonstrated in Corollary [5.6](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem6 "Corollary 5.6. ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). This is the specific case of Stochastic Volterra Equations with α−\alpha-fractional integration kernel.
Moreover, for α=1\alpha=1 the autocovariance function satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | cov​(Xt2∞,Xt1∞)=c​ν2​μ∞λ​e−λ​(t2−t1).\mathrm{cov}(X\_{t\_{2}}^{\infty},X\_{t\_{1}}^{\infty})=c\nu^{2}\frac{\mu\_{\infty}}{\lambda}e^{-\lambda(t\_{2}-t\_{1})}. |  | (6.69) |

which is that of the Markovian square root process with constant stabilizer. In fact,
If K=1K=1 in the volterra equation and c>0c>0 given, then Rλ​(t)=e−λ​tandfλ​(t)=λ​e−λ​t,so that ςλ,c=2​λ​cR\_{\lambda}(t)=e^{-\lambda t}\quad\text{and}\quad f\_{\lambda}(t)=\lambda e^{-\lambda t},\quad\text{so that }\quad\varsigma\_{\lambda,c}=\sqrt{2\lambda c}
and XX satisfy the following stochastic differential equation:

d​Xt=(θ​(t)−λ​Xt)​d​t+ςλ,c​ν​Xt​d​Wt,t≥0.dX\_{t}=(\theta(t)-\lambda X\_{t})\,dt+\varsigma\_{\lambda,c}\nu\sqrt{X\_{t}}\,dW\_{t},\quad t\geq 0.

where WW is a 11-dimensional Brownian motion on some filtered probability space (Ω,ℱ,{ℱt}t≥0,ℙ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\geq 0},\mathbb{P}).

Long-Run Confluence of the Stabilized Fractional CIR Process: Here, we consider ρ=0\rho=0 (fractional kernel).
The Remark in Proposition [5.1](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem1 "Proposition 5.1 (𝛾-Hölder 𝐿²-Contraction). ‣ 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") on Lipschitz L2L^{2}-confluence applies, since a=0a=0 and as X0>0X\_{0}>0, the solution of the Volterra equation ([2.5](https://arxiv.org/html/2512.09590v1#S2.E5 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is strictly non-negative (as noted in [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), Remark on Theorem 4.1]), so that its diffusion coefficient is Lipschitz on ℝ+∗\mathbb{R}\_{+}^{\*} i.e. equation ([5.48](https://arxiv.org/html/2512.09590v1#S5.E48 "In 5.1 𝛾-Hölder 𝐿²-Contraction ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) holds.
This is closely linked with the existence of strong solutions since the diffusion coefficient
x↦xx\mapsto\sqrt{x} is smooth on (0,∞)(0,\infty), and the Lipschitz
continuity is only violated at x=0x=0.

![Refer to caption](x7.png)


Figure 9: Confluence or Contraction from a ]0,30]-Uniform Distribution: over time interval [0,T], T = 100 for a value of the Hurst esponent H=0.4H=0.4, λ=0.2\lambda=0.2, c = 0.3.

![Refer to caption](x8.png)


Figure 10: Confluence or Contraction from a ]0,30]-Uniform Distribution:over time interval [0,T], T = 50 for a value of the Hurst esponent H=0.8H=0.8, λ=0.2\lambda=0.2, c = 0.36.

Figures ([10](https://arxiv.org/html/2512.09590v1#S6.F10 "Figure 10 ‣ 6.3 Long-run behaviour of the Fake Stationary Volterra-CIR with a Gamma Kernel ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([10](https://arxiv.org/html/2512.09590v1#S6.F10 "Figure 10 ‣ 6.3 Long-run behaviour of the Fake Stationary Volterra-CIR with a Gamma Kernel ‣ 6 Applications: The case of Fake Stationary Volterra CIR process. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) show that the marginals of such a process when
starting with various initial values are confluent in L2L^{2} as time goes to infinity.
Note that, as confirmed in the figure, Theorem [5.7](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem7 "Theorem 5.7 (Functional asymptotics in the Fake Stationarity Regime.). ‣ 5.3 Asymptotics: Long run functional weak behaviour and Stationary process ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (b) indicates that the mean of the limiting distribution remains constant.

Acknowledgement: The authors thank J-F. Chassagneux for insightful discussions, help and comments.

## References

* AJCLP [21]

  E. Abi Jaber, C. Cuchiero, M. Larsson, and S. Pulido.
  A weak solution theory for stochastic volterra equations of
  convolution type.
  Annals of Applied Probability, 31(6):2924–2952, 2021.
* AJLP [19]

  E. Abi Jaber, M. Larsson, and S. Pulido.
  Affine volterra processes.
  The Annals of Applied Probability, 29(5):3155–3200, 2019.
* AKO [22]

  J. Ackermann, T. Kruse, and L. Overbeck.
  Inhomogeneous affine volterra processes.
  Stochastic Processes and their Applications, 150:250–279,
  2022.
* BGS [90]

  S. Norlund B. Gripenberg and O. Saavalainen.
  Volterra Integral and Functional Equations.
  *Encyclopedia of Mathematics and its Applications*. Cambridge
  University Press, Cambridge, UK, 1990.
* BGT [89]

  N. H. Bingham, C. M. Goldie, and J. L. Teugels.
  Regular variation, volume 27 of Encyclopedia of
  Mathematics and its Applications.
  Cambridge University Press, Cambridge, 1989.
* Bre [10]

  Haim Brezis.
  Functional Analysis, Sobolev Spaces and Partial Differential
  Equations.
  Springer Science & Business Media, 2010.
* CGP [20]

  Giorgia Callegaro, Martino Grasselli, and Gilles Pagès.
  Fast hybrid schemes for fractional riccati equations (rough is not so
  tough).
  Mathematics of Operations Research, 46(1):221–254, 2020.
* CIR [85]

  J. C. Cox, J. E. Ingersoll, and S. A. Ross.
  A theory of the term structure of interest rates.
  Econometrica, 53(2):385–407, 1985.
* CM [99]

  Peter Carr and Dilip Madan.
  Option valuation using the fast fourier transform.
  Journal of Computational Finance, 2(4):61–73, 1999.
* CR [96]

  F. Comte and E. Renault.
  Long memory continuous time models.
  J. Econometrics, 73(1):101–149, 1996.
* CR [98]

  Fabienne Comte and Eric Renault.
  Long memory in continuous-time stochastic volatility models.
  Math. Finance, 8(4):291–323, 1998.
* DFS [03]

  D. Duffie, D. Filipović, and W. Schachermayer.
  Affine processes and applications in finance.
  The Annals of Applied Probability, 13(3):984–1053, 2003.
* EEFR [18]

  O. El Euch, M. Fukasawa, and M. Rosenbaum.
  The microstructural foundations of leverage effect and rough
  volatility.
  Finance Stoch., 22(2):241–280, 2018.
* EEGR [19]

  Omar El Euch, Jim Gatheral, and Mathieu Rosenbaum.
  Roughening heston.
  Risk, pages 84–89, 2019.
* EER [18]

  Omar El Euch and Mathieu Rosenbaum.
  Perfect hedging in rough Heston models.
  Ann. Appl. Probab., 28(6):3813–3856, 2018.
* EER [19]

  Omar El Euch and Mathieu Rosenbaum.
  The characteristic function of rough Heston models.
  Mathematical Finance, 29(1):3–38, 2019.
* Fel [51]

  W. Feller.
  Diffusion processes in genetics.
  In Proceedings of the Second Berkeley Symposium on Mathematical
  Statistics and Probability, pages 227–246, Berkeley and Los Angeles, 1951.
  University of California Press.
* FG [95]

  Franco Flandoli and Dariusz Gatarek.
  Martingale and stationary solutions for stochastic navier-stokes
  equations.
  Probability Theory and Related Fields, 102(3):367–391, 1995.
* FJ [22]

  Martin Friesen and Peng Jin.
  Volterra square-root process: Stationarity and regularity of the law.
  Stochastic Processes and their Applications, 2022.
* FM [09]

  D. Filipović and E. Mayerhofer.
  Affine diffusion processes: theory and applications.
  In Advanced Financial Modelling, volume 8, pages 1–40. 2009.
* GJR [18]

  Jim Gatheral, Thibault Jaisson, and Mathieu Rosenbaum.
  Volatility is rough.
  Quant. Finance, 18(6):933–949, 2018.
* GKI [24]

  Emmanuel Gnabeyeu, Omar Karkar, and Imad Idboufous.
  Solving the dynamic volatility fitting problem: A deep reinforcement
  learning approach.
  <https://doi.org/10.48550/arXiv.2410.11789>, 2024.
* GP [25]

  Emmanuel Gnabeyeu and Gilles Pagès.
  On a stationarity theory for stochastic volterra integral equations.
  <https://doi.org/10.48550/arXiv.2511.03474>, 2025.
* GR [25]

  E. Gnabeyeu and M. Rosenbaum.
  On the Microstructural Foundation of Inhomogeneous Rough
  Fractional Square-Root Process.
  2025.
  working paper.
* Hes [93]

  Steven L. Heston.
  A closed-form solution for options with stochastic volatility with
  applications to bond and currency options.
  The Review of Financial Studies, 6(2):327–343, 1993.
* Itk [05]

  Andrey Itkin.
  Pricing options with vg model using fft.
  arXiv preprint physics/0503137, 2005.
* JKR [20]

  Peng Jin, Jonas Kremer, and Barbara Rüdiger.
  Existence of limiting distribution for affine processes.
  Journal of Mathematical Analysis and Applications,
  486(2):123912, 2020.
* JP [22]

  Benjamin Jourdain and Gilles Pagès.
  Convex ordering for stochastic Volterra equations and their Euler
  schemes.
  arXiv e-prints, pages arXiv:2211.10186, to appear in Fin.
  & Stoch., November 2022.
* JPS [22]

  Antoine Jacquier, Alexandre Pannier, and Konstantinos Spiliopoulos.
  On the ergodic behaviour of affine Volterra processes.
  arXiv e-prints, page arXiv:2204.05270, April 2022.
* JR [15]

  T. Jaisson and M. Rosenbaum.
  Limit theorems for nearly unstable hawkes processes.
  Ann. Appl. Probab., 25(2):600–631, 2015.
* JR [16]

  Thibault Jaisson and Mathieu Rosenbaum.
  Rough fractional diffusions as scaling limits of nearly unstable
  heavy tailed Hawkes processes.
  Ann. Appl. Probab., 26(5):2860–2882, 2016.
* KP [99]

  P. E. Kloeden and E. Platen.
  Numerical Solution of Stochastic Differential Equations.
  Springer, 1999.
* KW [71]

  K. Kawazu and S. Watanabe.
  Branching processes with immigration and related limit theorems.
  Teoriya Veroyatnostei i ee Primeneniya, 16:34–51, 1971.
* Lew [01]

  Alan L. Lewis.
  A simple option formula for general jump-diffusion and other
  exponential lévy processes.
  Available at SSRN: <https://ssrn.com/abstract=282110>, 2001.
* Pag [24]

  G. Pagès.
  Volterra equations with affine drift: looking for stationarity.
  application to quadratic rough heston model.
  2024.
  working paper.
* Pro [05]

  P. E. Protter.
  Stochastic integration and differential equations.
  2005.
* PS [23]

  David J. Prömel and David Scheffels.
  On the existence of weak solutions to stochastic volterra equations.
  Electronic Communications in Probability, 28(52):1–12, 2023.
* RW [00]

  L. C. G. Rogers and David Williams.
  Diffusions, Markov processes, and martingales. Vol. 2:
  Itô calculus.
  Cambridge: Cambridge University Press, 2nd ed. edition, 2000.
* RY [99]

  Daniel Revuz and Marc Yor.
  Continuous martingales and Brownian motion, volume 293 of
  Grundlehren der mathematischen Wissenschaften [Fundamental Principles of
  Mathematical Sciences].
  Springer-Verlag, Berlin, third edition, 1999.
* Sch [10]

  Michael Schmelzle.
  Option pricing formulae using fourier transform: Theory and
  application.
  <http://pfadintegral.com>, 2010.
  Preprint.
* SGSM [93]

  A. A. Kilbas S. G. Samko and O. I. Marichev.
  Fractional integrals and derivatives.
  Gordon and Breach Science Publishers, Yverdon-les-Bains, Switzerland,
  1993.
* TKZ [78]

  A. Segall T. Kailath and M. Zakai.
  Fubini-type theorems for stochastic integrals.
  Sankhyā: The Indian Journal of Statistics, pages 138–143.,
  1978.
* Ver [12]

  M. Veraar.
  The stochastic fubini theorem revisited.
  Stochastics, 84(4):543–551, 2012.
* Wal [86]

  J. B. Walsh.
  An introduction to stochastic partial differential equations.
  In P. L. Hennequin, editor, École d’Été de
  Probabilités de Saint Flour XIV–1984, volume 1180 of Lecture Notes
  in Mathematics, pages 265–439. Springer, Berlin, 1986.
* Zha [10]

  Xicheng Zhang.
  Stochastic Volterra equations in Banach spaces and stochastic
  partial differential equation.
  J. Funct. Anal., 258(4):1361–1425, 2010.

## Appendix A Supplementary material and Proofs.

Proof of Proposition [2.2](https://arxiv.org/html/2512.09590v1#S2.ThmTheorem2 "Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."):
The first claim is a straigtforward consequence of [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), Equivalence Wiener-Hopf transform, Proposition 2.8] (Equation ([2.8](https://arxiv.org/html/2512.09590v1#S2.E8 "In 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."))), under assumption ([2.16](https://arxiv.org/html/2512.09590v1#S2.E16 "In Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) (𝒦)({\cal K}).

For every s∈[0,T]s\in[0,T], define the process Ms=(Mts)t∈[0,T]M^{s}=(M^{s}\_{t})\_{t\in[0,T]} by
Mts=∫0t∧sK​(s−r)​σ​(r,Xr)​dWr,t∈[0,T]M^{s}\_{t}=\int\_{0}^{t\wedge s}K(s-r)\sigma(r,X\_{r})\,\mathrm{d}W\_{r},\quad t\in[0,T]. By the linear growth in Assumption [2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")(ii) and [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), equation 4.58, Theorem 4.10], we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨Ms⟩T]=∫0T∧s|K​(s−r)|2​𝔼​[|σ​(r,Xr)|2]​dr≤C​(1+‖ϕ‖T2​𝔼​[|X0|2])​(∫0sK​(s−r)2​dr)<∞.\mathbb{E}[\langle M^{s}\rangle\_{T}]=\int\_{0}^{T\wedge s}|K(s-r)|^{2}\mathbb{E}\left[|\sigma(r,X\_{r})|^{2}\right]\,\mathrm{d}r\leq C(1+\|\phi\|\_{T}^{2}\mathbb{E}[|X\_{0}|^{2}])\left(\int\_{0}^{s}K(s-r)^{2}\,\mathrm{d}r\right)<\infty. |  |

Hence, ∀s∈[0,T]\forall\,s\in[0,T], the process MsM^{s} is a martingale. Therefore, in the case s≥ts\geq t, it holds by ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xs∣ℱt]\displaystyle\mathbb{E}[X\_{s}\mid\mathcal{F}\_{t}] | =x0​(s)+𝔼​[∫0sK​(s−r)​(θ​(r)−λ​Xr)​dr|ℱt]+𝔼​[∫0sK​(s−r)​σ​(r,Xr)​dWr|ℱt]\displaystyle=x\_{0}(s)+\mathbb{E}\left[\int\_{0}^{s}K(s-r)\left(\theta(r)-\lambda X\_{r}\right)\,\mathrm{d}r\,\Big|\,\mathcal{F}\_{t}\right]+\mathbb{E}\left[\int\_{0}^{s}K(s-r)\sigma(r,X\_{r})\,\mathrm{d}W\_{r}\,\Big|\,\mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =X0​ϕ​(s)+∫0sK​(s−r)​(θ​(r)−λ​𝔼​[Xr∣ℱt])​dr+∫0tK​(s−r)​σ​(r,Xr)​dWr.\displaystyle=X\_{0}\phi(s)+\int\_{0}^{s}K(s-r)\left(\theta(r)-\lambda\mathbb{E}[X\_{r}\mid\mathcal{F}\_{t}]\right)\,\mathrm{d}r+\int\_{0}^{t}K(s-r)\sigma(r,X\_{r})\,\mathrm{d}W\_{r}. |  |

The third equation in ([2.19](https://arxiv.org/html/2512.09590v1#S2.E19 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) follows as a direct consequence of the Wiener-Hopf equation ([2.17](https://arxiv.org/html/2512.09590v1#S2.E17 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). Alternatively, using the representation ([2.17](https://arxiv.org/html/2512.09590v1#S2.E17 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), one may derive this equation by considering the process Mt:=∫0tfλ​(T−s)​σ​(s,Xs)​dWs,t∈[0,T],M\_{t}:=\int\_{0}^{t}f\_{\lambda}(T-s)\,\sigma(s,X\_{s})\,\mathrm{d}W\_{s},\quad t\in[0,T],
which is a local martingale. Its quadratic variation satisfies the estimate

𝔼​[⟨M⟩T]≤∫0T|fλ​(T−s)|2​𝔼​[|σ​(s,Xs)|2]​ds≤C​‖fλ‖L2​(0,T)2​(1+‖ϕ‖T2​𝔼​[|X0|2]).\mathbb{E}\left[\langle M\rangle\_{T}\right]\leq\int\_{0}^{T}|f\_{\lambda}(T-s)|^{2}\,\mathbb{E}[|\sigma(s,X\_{s})|^{2}]\,\mathrm{d}s\leq C\,\|f\_{\lambda}\|\_{L^{2}(0,T)}^{2}\,\left(1+\|\phi\|\_{T}^{2}\,\mathbb{E}[|X\_{0}|^{2}]\right).

which is finite under Assumption (𝒦)​(i​i)(\mathcal{K})(ii) in [2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") together with the moment bound in [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), Theorem 4.2]. Therefore, MM is a true martingale, and taking ℱt\mathcal{F}\_{t}-conditional expectations concludes the proof and we are done. □\square

Proof of Theorem [3.4](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem4 "Theorem 3.4 (Existence of solution to the Riccati–Volterra Equation). ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
To prove the existence results for the measure-extended Riccati–Volterra equation in Theorem [3.4](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem4 "Theorem 3.4 (Existence of solution to the Riccati–Volterra Equation). ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we begin by deriving the existence of a solution to the Riccati–Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) below with f∈Lloc1​(ℝ+;ℝ−)f\in L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}), and then extend the result to μ∈ℳ−\mu\in\mathcal{M}^{-} by means of a suitable approximation procedure provided by Lemma [A.2](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem2 "Lemma A.2. ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). Let us consider for f∈Lloc1​(ℝ+;ℝ−)f\in L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}), the following Riccati–Volterra equation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ​(t)\displaystyle\psi(t) | =∫0tf​(s)​K​(t−s)​ds+∫0tF​(T−s,ψ​(s))​K​(t−s)​ds,\displaystyle=\int\_{0}^{t}f(s)K(t-s)\,\mathrm{d}s+\int\_{0}^{t}F(T-s,\psi(s))K(t-s)\,\mathrm{d}s, |  | (A.70) |
|  | F​(s,ψ)\displaystyle F(s,\psi) | =−λ​ψ+κ12​ς2​(s)​ψ2(t,ψ)∈ℝ+×ℝ.\displaystyle=-\lambda\psi+\frac{\kappa\_{1}}{2}\varsigma^{2}(s)\psi^{2}\quad(t,\psi)\in\mathbb{R}\_{+}\times\mathbb{R}. |  |

where λ∈ℝ\lambda\in\mathbb{R}, and ς:ℝ+→ℝ\varsigma:\mathbb{R}\_{+}\to\mathbb{R} is a given continuous function.
We are now in place to derive the existence of a solution to the Riccati–Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

###### Proposition A.1 (Existence for the time-inhomogeneous Riccati-Volterra equation).

Assume that [3.2](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") holds.
For any function f∈𝒞​([0,T],ℝ−)∩Lloc1​(ℝ+;ℝ−)f\in\mathcal{C}([0,T],\mathbb{R}\_{-})\cap L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}), the time-inhomogeneous Riccati–Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a unique global solution ψ=ψ​(⋅,f)∈𝒞​([0,T],ℝ−)∩Lloc2​(ℝ+;ℝ−)\psi=\psi(\cdot,f)\in\mathcal{C}([0,T],\mathbb{R}\_{-})\cap L^{2}\_{\text{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}), i.e., ψ​(t)≤0\psi(t)\leq 0 for all t∈[0,T]t\in[0,T]. Moreover, the following hold:

1. Let p∈[1,∞]p\in[1,\infty], If fλ∈Llocp​(ℝ+;ℝ)f\_{\lambda}\in L^{p}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}), then for each T>0T>0,

|  |  |  |
| --- | --- | --- |
|  | ‖ψ​(⋅,f)‖Lp​([0,T])≤1λ​‖f‖L1​([0,T])​‖fλ‖Lp​([0,T]).\|\psi(\cdot,f)\|\_{L^{p}([0,T])}\leq\frac{1}{\lambda}\|f\|\_{L^{1}([0,T])}\,\|f\_{\lambda}\|\_{L^{p}([0,T])}. |  |

2. Sobolev-Slobodeckij regularity of ψ\psi: The unique solution ψ\psi of ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) belongs to the fractional Sobolev space Wη,p​([0,T])W^{\eta,p}([0,T]), and satisfies the Sobolev-Slobodeckij a priori estimate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ψ​(⋅,f)‖Wη,p​([0,T])≤‖ψ​(⋅,f)‖Lp​([0,T])+C​(1+[K]η,p,T)​(1+‖f‖L1​([0,T])+‖ψ​(⋅,f)‖L2​([0,T])2).\|\psi(\cdot,f)\|\_{W^{\eta,p}([0,T])}\leq\|\psi(\cdot,f)\|\_{L^{p}([0,T])}+C\,(1+[K]\_{\eta,p,T})\,\left(1+\|f\|\_{L^{1}([0,T])}+\|\psi(\cdot,f)\|\_{L^{2}([0,T])}^{2}\right). |  | (A.71) |

where the constant C:=Cp,λ,κ1,ς,T>0C:=C\_{p,\lambda,\kappa\_{1},\varsigma,T}>0 depends only on T,p,λ,κ1T,p,\lambda,\kappa\_{1}, and the L∞−L^{\infty}-norm of ς\varsigma.

Proof of [A.1](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem1 "Proposition A.1 (Existence for the time-inhomogeneous Riccati-Volterra equation). ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
The existence of a nonpositive solution to the Riccati-Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is obtained in the first two steps below.

Step 1 (Existence of local solutions to deterministic Volterra equations.)
Since the kernel KK satisfies ([2.6](https://arxiv.org/html/2512.09590v1#S2.E6 "In 1st item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and ([2.7](https://arxiv.org/html/2512.09590v1#S2.E7 "In 2nd item ‣ item (i) ‣ Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) of Assumption [2.1](https://arxiv.org/html/2512.09590v1#S2.Thmassumption1 "Assumption 2.1 (On Volterra Equations with convolutive kernels). ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we deduce from [[4](https://arxiv.org/html/2512.09590v1#bib.bib4), Theorem 12.2.6] that if f∈𝒞​([0,T],ℝ−)f\in\mathcal{C}([0,T],\mathbb{R}\_{-}) the deterministic Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a unique non-continuable solution ψ∈𝒞​([0,Tm​a​x),ℝ)\psi\in\mathcal{C}([0,T\_{max}),\mathbb{R}) in the sense that ψ\psi satisfies ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) on [0,Tm​a​x)[0,T\_{max}) with Tm​a​x∈(0,∞]T\_{max}\in(0,\infty] and supt<Tm​a​x|ψ​(t)|=+∞\sup\_{t<T\_{max}}|\psi(t)|=+\infty, if Tm​a​x<∞T\_{max}<\infty. If K∈Lloc2​(ℝ+)K\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+}) and if f∈Lloc1​(ℝ+;ℝ−)f\in L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}), then by Young’s convolution inequality, this solution ψ=ψ​(⋅,f)∈L2​([0,Tmax))\psi=\psi(\cdot,f)\in L^{2}([0,T\_{\rm max})).
101010More generally, if f∈𝒞​([0,T],ℝ)f\in\mathcal{C}([0,T],\mathbb{R}) (resp. f∈Lloc1​(ℝ+;ℝ)f\in L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}) ), a non-continuable solution of ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) is a pair (ψ,Tmax)(\psi,T\_{\max}) with Tmax∈(0,∞]T\_{\max}\in(0,\infty] and ψ∈𝒞​([0,Tm​a​x),ℝ)\psi\in\mathcal{C}([0,T\_{max}),\mathbb{R})
(resp. ψ∈Lloc2([0,Tmax));ℝ)\psi\in L^{2}\_{\mathrm{loc}}([0,T\_{\max}));\mathbb{R}), such that ψ\psi satisfies ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) on
[0,Tmax)[0,T\_{\max}) and supt<Tm​a​x|ψ​(t)|=+∞\sup\_{t<T\_{max}}|\psi(t)|=+\infty (resp. ‖ψ‖L2​(0,Tmax)=∞\|\psi\|\_{L^{2}(0,T\_{\max})}=\infty ) whenever Tmax<∞T\_{\max}<\infty.
If Tmax=∞T\_{\max}=\infty, we call ψ\psi a global solution of ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

Step 2 (Non-positivity statement for the solution of the Riccati–Volterra equation.)
We now deal with the non-positivity of solutions to the deterministic Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
For this, we first observe that,
on the interval [0,Tmax)[0,T\_{\rm max}), the function χ:=−ψ\chi:=-\psi satisfies the linear equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | χ​(t)=∫0tK​(t−s)​(−f​(s)+(−λ+κ12​ς2​(T−s)​ψ​(s))​χ​(s))​𝑑s.\chi(t)=\int\_{0}^{t}K(t-s)\left(-f(s)+\big(-\lambda+\frac{\kappa\_{1}}{2}\varsigma^{2}(T-s)\psi(s)\big)\chi(s)\right)d\,s. |  | (A.72) |

which has by [[2](https://arxiv.org/html/2512.09590v1#bib.bib2), Theorem C.2] a unique solution χ∈Lloc2​(ℝ+;ℝ)\chi\in L^{2}\_{\text{loc}}(\mathbb{R}\_{+};\mathbb{R}) with χ≥0\chi\geq 0, owing to assumption [3.2](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") on KK and the fact that −f≥0-f\geq 0, i.e. there exists an ℝ+\mathbb{R}\_{+}-valued continuous solution χ\chi to ([A.72](https://arxiv.org/html/2512.09590v1#A1.E72 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
Then, the function ψ∈𝒞​([0,T],ℝ−)\psi\in\mathcal{C}([0,T],\mathbb{R}\_{-}) solves the Riccati–Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

Step 3 Global existence Tmax=∞T\_{\max}=\infty: We are now going to show that any local solution can be extended
to a local solution on a larger interval.
Our aim is to prove that Tmax≥TT\_{\rm max}\geq T for every T>0T>0 by showing that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt<Tmax|ψ​(t)|<∞.\sup\_{t<T\_{\rm max}}|\psi(t)|<\infty. |  | (A.73) |

Let h∈𝒞​([0,T],ℝ)h\in\mathcal{C}([0,T],\mathbb{R}) be the solution of the linear deterministic Wiener-Hopf equation
h​(t)=∫0tK​(t−s)​(f​(s)−λ​h​(s))​dsh(t)=\int\_{0}^{t}K(t-s)\left(f(s)-\lambda h(s)\right)\,\mathrm{d}s,
whose unique solution given by [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 2.4] reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(t)=((K−fλ∗K)∗f)​(t)=1λ​(fλ∗f)​(t)=1λ​∫0tfλ​(t−s)​f​(s)​ds.h(t)=((K-f\_{\lambda}\*K)\*f)(t)=\frac{1}{\lambda}(f\_{\lambda}\*f)(t)=\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)f(s)\,\mathrm{d}s. |  | (A.74) |

Observing that the function χ:=ψ−h\chi:=\psi-h satisfies the Wiener-Hopf equation

|  |  |  |
| --- | --- | --- |
|  | χ​(t)=∫0tK​(t−s)​(−λ​χ​(s)+κ12​ς2​(T−s)​ψ2​(s))​ds,\chi(t)=\int\_{0}^{t}K(t-s)\left(-\lambda\chi(s)+\frac{\kappa\_{1}}{2}\varsigma^{2}(T-s)\psi^{2}(s)\right)\,\mathrm{d}s, |  |

on [0,Tmax)[0,T\_{\rm max}) whose unique solution given by [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Proposition 2.4] reads:

|  |  |  |
| --- | --- | --- |
|  | χ(t)=((K−fλ∗K)∗κ12ς2(T−⋅)ψ2)(t)=1λ(fλ∗κ12ς2(T−⋅)ψ2)(t)=1λκ12∫0tfλ(t−s)ς2(T−s)ψ2(s)ds,\chi(t)=((K-f\_{\lambda}\*K)\*\frac{\kappa\_{1}}{2}\varsigma^{2}(T-\cdot)\psi^{2})(t)=\frac{1}{\lambda}(f\_{\lambda}\*\frac{\kappa\_{1}}{2}\varsigma^{2}(T-\cdot)\psi^{2})(t)=\frac{1}{\lambda}\frac{\kappa\_{1}}{2}\int\_{0}^{t}f\_{\lambda}(t-s)\varsigma^{2}(T-s)\psi^{2}(s)\,\mathrm{d}s, |  |

so that ψ−h:=χ≥0\psi-h:=\chi\geq 0 on [0,Tmax)[0,T\_{\mathrm{max}}), since by assumption [3.2](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), fλf\_{\lambda} is non-negative on [0,Tmax)[0,T\_{\mathrm{max}}).

In summary, we have shown that h≤ψ≤0h\leq\psi\leq 0 on [0,Tmax)[0,T\_{\rm max}).
Since hh is a global solution and thus have finite norm on any bounded interval, this implies ([A.73](https://arxiv.org/html/2512.09590v1#A1.E73 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) so that Tmax≥TT\_{\rm max}\geq T as needed. This being true for every T>0T>0, we conclude that Tmax=+∞T\_{\rm max}=+\infty.

Step 4 (LpL^{p}-bounds).
We obtain from the third step above that
‖ψ​(⋅,f)‖Lp​([0,T])≤‖h‖Lp​([0,T]).\|\psi(\cdot,f)\|\_{L^{p}([0,T])}\leq\|h\|\_{L^{p}([0,T])}. Now, applying Young’s inequality to equation ([A.74](https://arxiv.org/html/2512.09590v1#A1.E74 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), we have ‖h‖Lp​([0,T])≤1λ​‖f‖L1​([0,T])​‖fλ‖Lp​([0,T]).\|h\|\_{L^{p}([0,T])}\leq\frac{1}{\lambda}\|f\|\_{L^{1}([0,T])}\,\|f\_{\lambda}\|\_{L^{p}([0,T])}.

Step 5 ( Sobolev-Slobodeckij a priori estimate). By assumption, K∈Lloc2​(ℝ+)K\in L^{2}\_{\text{loc}}(\mathbb{R}\_{+}) satisfies the Sobolev-Slobodeckij-type condition [K]η,p,T<∞[K]\_{\eta,p,T}<\infty
for some p≥2p\geq 2, η∈(0,1)\eta\in(0,1), and each T>0T>0. Let us denote:

|  |  |  |
| --- | --- | --- |
|  | ψ​(t)=I1​(t)+I2​(t)withI1​(t):=∫0tf​(s)​K​(t−s)​dsandI2​(t):=∫0tF​(T−s,ψ​(s))​K​(t−s)​ds.\psi(t)=I\_{1}(t)+I\_{2}(t)\quad\text{with}\quad I\_{1}(t):=\int\_{0}^{t}f(s)K(t-s)\,\,\mathrm{d}s\quad\text{and}\quad I\_{2}(t):=\int\_{0}^{t}F(T-s,\psi(s))K(t-s)\,\,\mathrm{d}s. |  |

We estimate the increment |ψ​(t)−ψ​(s)||\psi(t)-\psi(s)| via the elementary inequality:

|  |  |  |
| --- | --- | --- |
|  | |ψ​(t)−ψ​(s)|p≤2p−1​(|I1​(t)−I1​(s)|p+|I2​(t)−I2​(s)|p).|\psi(t)-\psi(s)|^{p}\leq 2^{p-1}\left(|I\_{1}(t)-I\_{1}(s)|^{p}+|I\_{2}(t)-I\_{2}(s)|^{p}\right). |  |

For the nonlinear contribution I2I\_{2}, using the structure of F​(s,ψ)=−λ​ψ+κ12​ς2​(s)​ψ2F(s,\psi)=-\lambda\psi+\frac{\kappa\_{1}}{2}\varsigma^{2}(s)\psi^{2}, and the fact that ς\varsigma is bounded in (0,+∞)(0,+\infty), we have: |F​(s,ψ)|≤C′′​(|ψ|+|ψ|2)≤C′′​(1+|ψ|2)|F(s,\psi)|\leq C^{\prime\prime}(|\psi|+|\psi|^{2})\leq C^{\prime\prime}(1+|\psi|^{2}) for some positive constant C′′:=λ∨κ12​‖ς2‖∞C^{\prime\prime}:=\lambda\vee\frac{\kappa\_{1}}{2}\|\varsigma^{2}\|\_{\infty}.
Set g​(u):=|F​(T−u,ψ​(u))|g(u):=|F(T-u,\psi(u))|, which satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0Tg​(u)​𝑑u≤C​(1+‖ψ‖L2​([0,T])2)withC′:=C′′​(1∨T).\int\_{0}^{T}g(u)\,du\leq C\left(1+\|\psi\|\_{L^{2}([0,T])}^{2}\right)\quad\text{with}\quad C^{\prime}:=C^{\prime\prime}\,(1\vee T). |  | (A.75) |

Then, we estimate the increment:

|  |  |  |
| --- | --- | --- |
|  | |I2​(t)−I2​(s)|p≤2p−1​(∫st|K​(t−u)|​g​(u)​𝑑u)p+2p−1​(∫0s|K​(t−u)−K​(s−u)|​g​(u)​𝑑u)p\displaystyle|I\_{2}(t)-I\_{2}(s)|^{p}\leq 2^{p-1}\left(\int\_{s}^{t}|K(t-u)|g(u)\,du\right)^{p}+2^{p-1}\left(\int\_{0}^{s}|K(t-u)-K(s-u)|g(u)\,du\right)^{p} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1​(∫stg​(u)​𝑑u)p−1​∫st|K​(t−u)|p​g​(u)​𝑑u+2p−1​(∫0sg​(u)​𝑑u)p−1​∫0s|K​(t−u)−K​(s−u)|p​g​(u)​𝑑u.\displaystyle\hskip 14.22636pt\leq 2^{p-1}\left(\int\_{s}^{t}g(u)\,du\right)^{p-1}\int\_{s}^{t}|K(t-u)|^{p}g(u)\,du+2^{p-1}\left(\int\_{0}^{s}g(u)\,du\right)^{p-1}\int\_{0}^{s}|K(t-u)-K(s-u)|^{p}g(u)\,du. |  |

where we used estimate ([A.75](https://arxiv.org/html/2512.09590v1#A1.E75 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and Jensen’s inequality
111111For two measurable real-valued functions ff, gg, and p≥1p\geq 1 and 0≤a<b0\leq a<b, it holds:

|∫abf​(s)​g​(s)​ds|p\displaystyle\left|\int\_{a}^{b}f(s)g(s)\,\,\mathrm{d}s\right|^{p}
≤|∫ab|f​(s)|1−1p⋅|f​(s)|1p​g​(s)​ds|p≤(∫ab|f​(s)|​ds)p−1⋅∫ab|f​(s)|​|g​(s)|p​ds.\displaystyle\leq\left|\int\_{a}^{b}|f(s)|^{1-\frac{1}{p}}\cdot|f(s)|^{\frac{1}{p}}g(s)\,\,\mathrm{d}s\right|^{p}\leq\left(\int\_{a}^{b}|f(s)|\,\,\mathrm{d}s\right)^{p-1}\cdot\int\_{a}^{b}|f(s)||g(s)|^{p}\,\,\mathrm{d}s.
.
It follows that:

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫0T|I2​(t)−I2​(s)|p|t−s|1+η​p​𝑑s​𝑑t\displaystyle\ \int\_{0}^{T}\int\_{0}^{T}\frac{|I\_{2}(t)-I\_{2}(s)|^{p}}{|t-s|^{1+\eta p}}\,ds\,dt |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1​(∫0Tg​(u)​𝑑u)p−1​(∫0T∫0T∫st|K​(t−u)|p|t−s|1+η​p​g​(u)​𝑑u​𝑑s​𝑑t+∫0T∫0T∫0s|K​(t−u)−K​(s−u)|p|t−s|1+η​p​g​(u)​𝑑u​𝑑s​𝑑t)\displaystyle\leq 2^{p-1}\left(\int\_{0}^{T}g(u)\,du\right)^{p-1}\left(\int\_{0}^{T}\int\_{0}^{T}\int\_{s}^{t}\frac{|K(t-u)|^{p}}{|t-s|^{1+\eta p}}g(u)\,du\,ds\,dt+\int\_{0}^{T}\int\_{0}^{T}\int\_{0}^{s}\frac{|K(t-u)-K(s-u)|^{p}}{|t-s|^{1+\eta p}}g(u)\,du\,ds\,dt\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1​(∫0Tg​(u)​𝑑u)p−1​(∫0T∫uT∫0u|K​(t−u)|p|t−s|1+η​p​g​(u)​𝑑s​𝑑t​𝑑u+∫0T∫uT∫0u|K​(t−u)−K​(s−u)|p|t−s|1+η​p​g​(u)​𝑑s​𝑑t​𝑑u)\displaystyle\leq 2^{p-1}\left(\int\_{0}^{T}g(u)\,du\right)^{p-1}\left(\int\_{0}^{T}\int\_{u}^{T}\int\_{0}^{u}\frac{|K(t-u)|^{p}}{|t-s|^{1+\eta p}}g(u)\,ds\,dt\,du+\int\_{0}^{T}\int\_{u}^{T}\int\_{0}^{u}\frac{|K(t-u)-K(s-u)|^{p}}{|t-s|^{1+\eta p}}g(u)\,ds\,dt\,du\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1​(∫0Tg​(u)​𝑑u)p−1​(1η​p​∫0T∫uT|K​(t−u)|p|t−u|η​p​g​(u)​𝑑t​𝑑u+∫0T∫uT∫0u|K​(t−u)−K​(s−u)|p|t−s|1+η​p​g​(u)​𝑑s​𝑑t​𝑑u)\displaystyle\leq 2^{p-1}\left(\int\_{0}^{T}g(u)\,du\right)^{p-1}\left(\frac{1}{\eta p}\int\_{0}^{T}\int\_{u}^{T}\frac{|K(t-u)|^{p}}{|t-u|^{\eta p}}g(u)\,dt\,du+\int\_{0}^{T}\int\_{u}^{T}\int\_{0}^{u}\frac{|K(t-u)-K(s-u)|^{p}}{|t-s|^{1+\eta p}}g(u)\,ds\,dt\,du\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1​(∫0Tg​(u)​𝑑u)p​[K]η,p,Tp≤C​(1+[K]η,p,Tp)​(1+‖ψ‖L2​([0,T])2​p), C:=(2p−1​C′)p=2p2−p​(λp∨κ1p2p​‖ς2‖∞p).\displaystyle\leq 2^{p-1}\left(\int\_{0}^{T}g(u)\,du\right)^{p}[K]^{p}\_{\eta,p,T}\leq C\,(1+[K]\_{\eta,p,T}^{p})\,\left(1+\|\psi\|\_{L^{2}([0,T])}^{2p}\right),\;\text{ $C:=(2^{p-1}C^{\prime})^{p}=2^{p^{2}-p}\,(\lambda^{p}\vee\frac{\kappa\_{1}^{p}}{2^{p}}\|\varsigma^{2}\|^{p}\_{\infty})$}. |  |

where in the second inequality, we applied Fubini’s theorem twice to interchange the order of integration.

Repeating the above arguments for I1I\_{1}, with now, g​(u):=|f​(u)|g(u):=|f(u)|, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T∫0T|I1​(t)−I1​(s)|p|t−s|1+η​p​𝑑s​𝑑t≤2p−1​[K]η,p,Tp​‖f‖L1​([0,T])p≤2p−1​(1+[K]η,p,Tp)​‖f‖L1​([0,T])p.\displaystyle\int\_{0}^{T}\int\_{0}^{T}\frac{|I\_{1}(t)-I\_{1}(s)|^{p}}{|t-s|^{1+\eta p}}ds\,dt\leq 2^{p-1}\,[K]\_{\eta,p,T}^{p}\|f\|\_{L^{1}([0,T])}^{p}\leq 2^{p-1}\,(1+[K]\_{\eta,p,T}^{p})\|f\|\_{L^{1}([0,T])}^{p}. |  | (A.76) |

Summarizing the above first estimate with ([A.76](https://arxiv.org/html/2512.09590v1#A1.E76 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), we obtain there exists a constant K:=Kp,T,ς,λ,κ1K:=K\_{p,T,\varsigma,\lambda,\kappa\_{1}}

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫0T|ψ​(t,f)−ψ​(s,f)|p|t−s|1+η​p​𝑑s​𝑑t≤K​(1+[K]η,p,Tp)​(1+‖f‖L1​([0,T])p+‖ψ‖L2​([0,T])2​p).\displaystyle\int\_{0}^{T}\int\_{0}^{T}\frac{|\psi(t,f)-\psi(s,f)|^{p}}{|t-s|^{1+\eta p}}dsdt\leq K(1+[K]\_{\eta,p,T}^{p})\left(1+\|f\|\_{L^{1}([0,T])}^{p}+\|\psi\|\_{L^{2}([0,T])}^{2p}\right). |  |

In view of equation ([1.4](https://arxiv.org/html/2512.09590v1#S1.E4 "In 1.3 Structure of the paper and Notations ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), the assertion is proved.
This completes the proof of the proposition [A.1](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem1 "Proposition A.1 (Existence for the time-inhomogeneous Riccati-Volterra equation). ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). □\square

Main Proof of Theorem [3.4](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem4 "Theorem 3.4 (Existence of solution to the Riccati–Volterra Equation). ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
We recall the following result (see also [[19](https://arxiv.org/html/2512.09590v1#bib.bib19), Lemma 3.6]), stated here in the setting of (0,+∞)(0,+\infty).

###### Lemma A.2.

For each μ∈ℳ−\mu\in\mathcal{M}^{-} there exists a sequence (fn)n≥1⊂Lloc1​(ℝ+;ℝ−)(f\_{n})\_{n\geq 1}\subset L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}) such that:

1. (i)

   ‖fn‖L1​([0,T])≤|μ|​([0,T])\|f\_{n}\|\_{L^{1}([0,T])}\leq|\mu|([0,T]) for all T>0T>0;
2. (ii)

   For each T>0T>0, p≥1p\geq 1, and g∈Lp​([0,T];ℝ)g\in L^{p}([0,T];\mathbb{R}) one has g∗fn→g∗μinLp​([0,T]);g\*f\_{n}\to g\*\mu\quad\text{in}\quad L^{p}([0,T]);
3. (iii)

   For each T>0T>0 and each g∈𝒞​([0,T];ℝ)g\in\mathcal{C}([0,T];\mathbb{R}) with g​(0)=0g(0)=0 one has

   |  |  |  |
   | --- | --- | --- |
   |  | limn→∞∫0tg​(t−s)​fn​(s)​𝑑s=∫0tg​(t−s)​μ​(d​s),∀t∈[0,T].\lim\_{n\to\infty}\int\_{0}^{t}g(t-s)f\_{n}(s)ds=\int\_{0}^{t}g(t-s)\,\mu(ds),\quad\forall t\in[0,T]. |  |

Step 1
Let μ∈ℳ−\mu\in\mathcal{M}^{-} and (fn)n≥1⊂Lloc1​(ℝ+;ℝ−)(f\_{n})\_{n\geq 1}\subset L^{1}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-}) be a sequence of functions as given in Lemma [A.2](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem2 "Lemma A.2. ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), and let ψn:=ψ​(⋅,fn)\psi\_{n}:=\psi(\cdot,f\_{n}) denote the corresponding sequence of unique solutions to the standard Riccati equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) with input fnf\_{n}. Fix T>0T>0 and q∈[1,p]q\in[1,p]. By Proposition [A.1](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem1 "Proposition A.1 (Existence for the time-inhomogeneous Riccati-Volterra equation). ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (1) and Lemma [A.2](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem2 "Lemma A.2. ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (i):

|  |  |  |
| --- | --- | --- |
|  | ‖ψ​(⋅,fn)‖Lq​([0,T])≤1λ​|μ|​([0,T])​‖fλ‖Lq​([0,T]).\|\psi(\cdot,f\_{n})\|\_{L^{q}([0,T])}\leq\frac{1}{\lambda}|\mu|([0,T])\,\|f\_{\lambda}\|\_{L^{q}([0,T])}. |  |

Likewise by Proposition [A.1](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem1 "Proposition A.1 (Existence for the time-inhomogeneous Riccati-Volterra equation). ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (1) and Lemma [A.2](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem2 "Lemma A.2. ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (i):

|  |  |  |
| --- | --- | --- |
|  | ‖ψ​(⋅,fn)‖Wη,p​([0,T])≤‖ψ​(⋅,fn)‖Lp​([0,T])+C​(1+[K]η,p,T)​(1+|μ|​([0,T])+‖ψ​(⋅,fn)‖L2​([0,T])2).\|\psi(\cdot,f\_{n})\|\_{W^{\eta,p}([0,T])}\leq\|\psi(\cdot,f\_{n})\|\_{L^{p}([0,T])}+C\,(1+[K]\_{\eta,p,T})\big(1+|\mu|([0,T])+\|\psi(\cdot,f\_{n})\|\_{L^{2}([0,T])}^{2}\big). |  |

Owing to the LqL^{q}-estimates above, the right-hand side remains uniformly bounded in nn.
By the relative compactness121212Relative compactness in LpL^{p} spaces is classically characterized by the Kolmogorov–Riesz–Fréchet theorem; see, for instance, [[6](https://arxiv.org/html/2512.09590v1#bib.bib6), Theorem 4.26].The relationship between the Sobolev–Slobodeckij norm and the LpL^{p} topology is similar to that between Hölder norms and spaces of continuous functions: in particular, bounded sets in Wη,p​(0,T)W^{\eta,p}(0,T) are relatively compact in Lp​(0,T)L^{p}(0,T); see, e.g., [[18](https://arxiv.org/html/2512.09590v1#bib.bib18), Theorem 2.1]. of the ball {h∈Lp​([0,T];ℝ):‖h‖Wη,p​([0,T])≤R}\{h\in L^{p}([0,T];\mathbb{R}):\|h\|\_{W^{\eta,p}([0,T])}\leq R\} in Lp​([0,T];ℝ)L^{p}([0,T];\mathbb{R}) for any R>0R>0 (see [[18](https://arxiv.org/html/2512.09590v1#bib.bib18), Theorem 2.1]), we extract a subsequence (fnk)k≥1(f\_{n\_{k}})\_{k\geq 1} such that ψ​(⋅,fnk)→ψin ​Lp​([0,T];ℝ).\psi(\cdot,f\_{n\_{k}})\to\psi\quad\text{in }L^{p}([0,T];\mathbb{R}).
Furthermore, by passing to a further subsequence (still denoted by (fnk)k≥1(f\_{n\_{k}})\_{k\geq 1}), we may assume that
ψ​(⋅,fnk)→ψa.e. on ​[0,T].\psi(\cdot,f\_{n\_{k}})\to\psi\quad\text{a.e.\ on }[0,T].
Taking the limit k→∞k\to\infty and applying Fatou’s lemma yields the desired bounds in part (b).

Step 2 We now show that ψ=ψ​(⋅,μ)\psi=\psi(\cdot,\mu) solves the extended Riccati equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) on [0,T][0,T].
Since ψnk→ψandK∗fnk→K∗μin ​Lp​([0,T];ℝ),by Lemma [A.2](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem2 "Lemma A.2. ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (ii)\psi\_{n\_{k}}\to\psi\quad\text{and}\quad K\ast f\_{n\_{k}}\to K\ast\mu\quad\text{in }L^{p}([0,T];\mathbb{R}),\;\text{by Lemma\penalty 10000\ \ref{lemma:admissible-mu-approx}\penalty 10000\ (ii)}
it suffices to show that K∗F(T−⋅,ψnk)→K∗F(T−⋅,ψ)in Lp([0,T];ℝ).K\ast F(T-\cdot,\psi\_{n\_{k}})\to K\ast F(T-\cdot,\psi)\quad\text{in }L^{p}([0,T];\mathbb{R}).
To this end, we use the Lipschitz-type estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F(T−⋅,ψ)−F(T−⋅,ψ~)|≤C(1+|ψ|+|ψ~|)|ψ−ψ~|.|F(T-\cdot,\psi)-F(T-\cdot,\tilde{\psi})|\leq C(1+|\psi|+|\tilde{\psi}|)|\psi-\tilde{\psi}|. |  | (A.77) |

and apply Young’s inequality
to obtain with K′:=C​‖K‖Lp​([0,T])K^{\prime}:=C\|K\|\_{L^{p}([0,T])}

|  |  |  |
| --- | --- | --- |
|  | ∥K∗F(T−⋅,ψnk)−K∗F(T−⋅,ψ)∥Lp​([0,T])≤K′∫0T(1+|ψnk(s)|+|ψ(s)|)|ψnk(s)−ψ(s)|ds\displaystyle\ \|K\ast F(T-\cdot,\psi\_{n\_{k}})-K\ast F(T-\cdot,\psi)\|\_{L^{p}([0,T])}\leq K^{\prime}\int\_{0}^{T}(1+|\psi\_{n\_{k}}(s)|+|\psi(s)|)|\psi\_{n\_{k}}(s)-\psi(s)|\,ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​‖K‖Lp​([0,T])​(1+‖ψnk‖L2​([0,T])+‖ψ‖L2​([0,T]))​‖ψnk−ψ‖L2​([0,T]).\displaystyle\hskip 156.49014pt\leq C\|K\|\_{L^{p}([0,T])}\left(1+\|\psi\_{n\_{k}}\|\_{L^{2}([0,T])}+\|\psi\|\_{L^{2}([0,T])}\right)\|\psi\_{n\_{k}}-\psi\|\_{L^{2}([0,T])}. |  |

where the last inequality comes form Cauchy-Schwarz inequality.
Since the right-hand side tends to zero, it follows that ψ\psi solves ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) on [0,T][0,T]. As the set (−∞,0](-\infty,0] is closed, we have that ψ\psi lies in (−∞,0](-\infty,0].

Finally, note that ([A.77](https://arxiv.org/html/2512.09590v1#A1.E77 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) holds globally and that K∗μ∈Lloc2​(ℝ+;ℝ)K\ast\mu\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}). Then by [[2](https://arxiv.org/html/2512.09590v1#bib.bib2), Theorem B.1], the equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) admits a unique maximal solution. Since ψ\psi is a global solution, it must coincide with the unique maximal solution on ℝ+\mathbb{R}\_{+}. This completes the proof of part (a).

Step 3
To prove part (c), in view of ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), it suffices to show that K∗F(T−⋅,ψ)K\*F(T-\cdot,\psi) is continuous on ℝ+\mathbb{R}\_{+}. The latter is true if for example K∈Lloc2K\in L^{2}\_{\mathrm{loc}} and F(T−⋅,ψ(⋅))∈Lloc2F(T-\cdot,\psi(\cdot))\in L^{2}\_{\mathrm{loc}} as given by Young’s inequality, which holds true due to |F​(s,ψ)|≤(λ∨κ12​‖ς2‖∞)​(1+|ψ|2)|F(s,\psi)|\leq(\lambda\vee\frac{\kappa\_{1}}{2}\|\varsigma^{2}\|\_{\infty})(1+|\psi|^{2})) and ψ∈Lloc2\psi\in L^{2}\_{\mathrm{loc}}. This proves part (c).
□\square

Proof of Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").

Step 1 (The conditional Laplace of XTX\_{T} ). Let T>0T>0 and consider a measure μ∈ℳ−\mu\in\mathcal{M}^{-}, by Theorem [3.4](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem4 "Theorem 3.4 (Existence of solution to the Riccati–Volterra Equation). ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") there exists a unique solution ψ=ψ​(⋅,μ)∈Lloc2​(ℝ+;ℝ−)∩𝒞​([0,T],ℝ−)\psi=\psi(\cdot,\mu)\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+};\mathbb{R}\_{-})\cap\mathcal{C}([0,T],\mathbb{R}\_{-}) to the measure-extended Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ut\displaystyle U\_{t} | =𝔼x¯0​[∫0TXT−s​μ​(d​s)+12​∫tTσ2​(s,Xs)​ψ2​(T−s)​𝑑s|ℱt]=∫0T𝔼x¯0​[XT−s∣ℱt]​μ​(d​s)\displaystyle=\mathbb{E}\_{\bar{x}\_{0}}\left[\int\_{0}^{T}X\_{T-s}\,\mu(ds)+\frac{1}{2}\int\_{t}^{T}\sigma^{2}(s,X\_{s})\psi^{2}(T-s)\,ds\Big|\mathcal{F}\_{t}\right]=\int\_{0}^{T}\mathbb{E}\_{\bar{x}\_{0}}[X\_{T-s}\mid\mathcal{F}\_{t}]\,\mu(ds) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​∫tTσ2​(s,𝔼x¯0​[Xs∣ℱt])​ψ2​(T−s)​ds=∫0Tξt​(T−s)​μ​(d​s)+12​∫tTσ2​(s,ξt​(s))​ψ2​(T−s)​ds.\displaystyle+\frac{1}{2}\int\_{t}^{T}\sigma^{2}(s,\,\mathbb{E}\_{\bar{x}\_{0}}[X\_{s}\mid\mathcal{F}\_{t}])\,\psi^{2}(T-s)\,\mathrm{d}s=\int\_{0}^{T}\xi\_{t}(T-s)\,\mu(\mathrm{d}s)+\frac{1}{2}\int\_{t}^{T}\sigma^{2}(s,\xi\_{t}(s))\,\psi^{2}(T-s)\,\mathrm{d}s. |  |

where the last equality comes from the affine nature of XX.
Moreover, set M=exp⁡(U)M=\exp(U).

Let XX be a solution of equation ([1.2](https://arxiv.org/html/2512.09590v1#S1.E2 "In 1.1 Literature review ‣ 1 Introduction ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), with σ​(x)\sigma(x) as in equation ([3.21](https://arxiv.org/html/2512.09590v1#S3.E21 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), and assume K∈Lloc2​(ℝ+)K\in L^{2}\_{\mathrm{loc}}(\mathbb{R}\_{+}). Then the process (Mt)t∈[0,T](M\_{t})\_{t\in[0,T]} is a
local martingale on [0,T][0,T], and satisfies d​MtMt=ψ​(T−t)​σ​(t,Xt)​d​Wt.\frac{\mathrm{d}M\_{t}}{M\_{t}}=\psi(T-t)\,\sigma(t,X\_{t})\,\mathrm{d}W\_{t}.
In fact, by computing its dynamics using Itó’s formula, we can write:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​MtMt=d​Ut+12​d​⟨U⟩t.\displaystyle\frac{dM\_{t}}{M\_{t}}=dU\_{t}+\frac{1}{2}d\langle U\rangle\_{t}. |  | (A.78) |

The dynamics of UU can be obtained by recalling ξt​(s)\xi\_{t}(s) from ([2.20](https://arxiv.org/html/2512.09590v1#S2.E20 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) and noting that for fixed ss, the dynamics of t↦ξt​(s)t\mapsto\xi\_{t}(s) are given by d​ξt​(s)=1λ​fλ​(s−t)​σ​(t,Xt)​d​Wt,for ​t≤s.\mathrm{d}\xi\_{t}(s)=\frac{1}{\lambda}f\_{\lambda}(s-t)\,\sigma(t,X\_{t})\,\mathrm{d}W\_{t},\quad\text{for }t\leq s.
Since ξt​(t)=Xt\xi\_{t}(t)=X\_{t}, it follows that:

|  |  |  |
| --- | --- | --- |
|  | d​Ut=∫0T−t𝑑ξt​(T−s)​μ​(d​s)−12​σ2​(t,Xt)​ψ2​(T−t)​d​t+12​∫tT∂xσ2​(s,ξt​(s))​ψ2​(T−s)​d​ξt​(s)​d​s\displaystyle\,dU\_{t}=\int\_{0}^{T-t}d\xi\_{t}(T-s)\,\mu(\mathrm{d}s)-\frac{1}{2}\sigma^{2}(t,X\_{t})\,\psi^{2}(T-t)\,dt+\frac{1}{2}\int\_{t}^{T}\partial\_{x}\sigma^{2}(s,\xi\_{t}(s))\,\psi^{2}(T-s)\,d\xi\_{t}(s)\,ds |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0T−tfλ​(T−s−t)​μ​(d​s)​σ​(t,Xt)λ​𝑑Wt−σ2​(t,Xt)2​ψ2​(T−t)​d​t+∫tTk1​ς2​(s)​ψ2​(T−s)​fλ​(s−t)​𝑑s​σ​(t,Xt)2​λ​𝑑Wt\displaystyle=\int\_{0}^{T-t}f\_{\lambda}(T-s-t)\,\mu(\mathrm{d}s)\,\frac{\sigma(t,X\_{t})}{\lambda}\,dW\_{t}-\frac{\sigma^{2}(t,X\_{t})}{2}\,\psi^{2}(T-t)\,dt+\int\_{t}^{T}k\_{1}\,\varsigma^{2}(s)\,\psi^{2}(T-s)\,f\_{\lambda}(s-t)\,ds\frac{\sigma(t,X\_{t})}{2\,\lambda}\,dW\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =−12​σ2​(t,Xt)​ψ2​(T−t)​d​t+(∫0T−tfλ​(T−t−s)​μ​(d​s)+12​∫tTk1​ς2​(s)​ψ2​(T−s)​fλ​(s−t)​𝑑s)​σ​(t,Xt)λ​d​Wt\displaystyle=-\frac{1}{2}\sigma^{2}(t,X\_{t})\,\psi^{2}(T-t)\,dt+\Bigg(\int\_{0}^{T-t}f\_{\lambda}(T-t-s)\,\mu(\mathrm{d}s)+\frac{1}{2}\int\_{t}^{T}k\_{1}\,\varsigma^{2}(s)\,\psi^{2}(T-s)\,f\_{\lambda}(s-t)\,ds\Bigg)\frac{\sigma(t,X\_{t})}{\lambda}\,dW\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =−12​σ2​(t,Xt)​ψ2​(T−t)​d​t+ψ​(T−t)​σ​(t,Xt)​d​Wt.\displaystyle=-\frac{1}{2}\sigma^{2}(t,X\_{t})\,\psi^{2}(T-t)\,dt+\psi(T-t)\,\sigma(t,X\_{t})\,\mathrm{d}W\_{t}. |  |

where the last equality follows after a change of variable from the measure-extended Riccati–Volterra equation ([3.25](https://arxiv.org/html/2512.09590v1#S3.E25 "In Lemma 3.1. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) in Lemma [3.1](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem1 "Lemma 3.1. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."). Thus, d​⟨U⟩t=ψ2​(T−t)​σ2​(t,Xt)​d​t.d\langle U\rangle\_{t}=\psi^{2}(T-t)\,\sigma^{2}(t,X\_{t})\,dt.
Injecting the dynamics of d​UtdU\_{t} and d​⟨U⟩td\langle U\rangle\_{t} into ([A.78](https://arxiv.org/html/2512.09590v1#A1.E78 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), we get d​MtMt=ψ​(T−t)​σ​(t,Xt)​d​Wt.\frac{dM\_{t}}{M\_{t}}=\psi(T-t)\,\sigma(t,X\_{t})\,\mathrm{d}W\_{t}.
This shows that MM is an exponential local martingale of the form

|  |  |  |
| --- | --- | --- |
|  | Mt=M0​exp⁡(∫0tψ​(T−s)​σ​(s,Xs)​𝑑Ws−12​∫0tψ2​(T−s)​σ2​(s,Xs)​𝑑s).M\_{t}=M\_{0}\exp\left(\int\_{0}^{t}\psi(T-s)\,\sigma(s,X\_{s})\,dW\_{s}-\frac{1}{2}\int\_{0}^{t}\psi^{2}(T-s)\,\sigma^{2}(s,X\_{s})\,ds\right). |  |

To obtain ([3.28](https://arxiv.org/html/2512.09590v1#S3.E28 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), it suffices to prove that MM is a martingale. Indeed, if this is the case then, the martingale property yields using that UT=∫0TXT−s​μ​(d​s)U\_{T}=\int\_{0}^{T}X\_{T-s}\,\mu(\mathrm{d}s)

|  |  |  |
| --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∫0TXT−s​μ​(d​s))|ℱt]=𝔼x¯0​[MT|ℱt]=Mt\displaystyle\ \mathbb{E}\_{\bar{x}\_{0}}\left[\exp\left(\int\_{0}^{T}X\_{T-s}\,\mu(\mathrm{d}s)\right)\Big|\mathcal{F}\_{t}\right]=\mathbb{E}\_{\bar{x}\_{0}}\left[M\_{T}\Big|\mathcal{F}\_{t}\right]=M\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =exp⁡(∫0T𝔼x¯0​[XT−s∣ℱt]​μ​(d​s)+12​∫tTς2​(s)​σ2​(𝔼x¯0​[Xs∣ℱt])​ψ​(T−s)2​ds).\displaystyle\hskip 135.15059pt=\exp\left(\int\_{0}^{T}\mathbb{E}\_{\bar{x}\_{0}}[X\_{T-s}\mid\mathcal{F}\_{t}]\,\mu(\mathrm{d}s)+\frac{1}{2}\int\_{t}^{T}\varsigma^{2}(s)\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{s}\mid\mathcal{F}\_{t}])\,\psi(T-s)^{2}\,\mathrm{d}s\right). |  |

That is, if MM is a true martingale, then the measure-extended Laplace transform of XTX\_{T} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(∫0TXT−s​μ​(d​s))|ℱt]=exp⁡(∫0Tξt​(T−s)​μ​(d​s)+12​∫tTς2​(s)​σ2​(ξt​(s))​ψ​(T−s)2​ds).\displaystyle\mathbb{E}\_{\bar{x}\_{0}}\left[\exp\left(\int\_{0}^{T}X\_{T-s}\,\mu(\mathrm{d}s)\right)\Big|\mathcal{F}\_{t}\right]=\exp\left(\int\_{0}^{T}\xi\_{t}(T-s)\,\mu(\mathrm{d}s)+\frac{1}{2}\int\_{t}^{T}\varsigma^{2}(s)\sigma^{2}(\xi\_{t}(s))\,\psi(T-s)^{2}\,\mathrm{d}s\right). |  | (A.79) |

which yields ([3.28](https://arxiv.org/html/2512.09590v1#S3.E28 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
We now argue martingality of MM: Recall that Mt=exp⁡(Ut−12​⟨U⟩t)M\_{t}=\exp(U\_{t}-\tfrac{1}{2}\langle U\rangle\_{t}). Since MM is a nonnegative local martingale, it follows from Fatou’s lemma that MM is a supermartingale. Therefore, to conclude that MM is a true martingale, it suffices to show that 𝔼x¯0​[MT]≥1\mathbb{E}\_{\bar{x}\_{0}}[M\_{T}]\geq 1 for all T∈ℝ+T\in\mathbb{R}\_{+}.
To this end, we adapt the argument of [[2](https://arxiv.org/html/2512.09590v1#bib.bib2), Lemma 7.3] to our setting since ψ\psi is real-valued
and continuous and hence bounded on [0,T][0,T]. Namely, let us define the sequence of stopping
times τn=inf{t≥0:Xt≥n}\tau\_{n}=\inf\{t\geq 0:X\_{t}\geq n\}. Then MτnM^{\tau\_{n}} is a uniformly integrable martingale for each nn by Novikov’s condition, and we may define a measure change d​ℚnd​ℙ=Mτn∧T\frac{d\mathbb{Q}^{n}}{d\mathbb{P}}=M\_{\tau\_{n}\wedge T}. By Girsanov’s theorem, the process,
d​Wtn=d​Wt−𝟏[0,τn]​(t)​ψ​(T−t)​σ​(t,Xt)​d​tdW^{n}\_{t}=dW\_{t}-\mathbf{1}\_{[0,\tau\_{n}]}(t)\psi(T-t)\,\sigma(t,X\_{t})\,dt
is a Brownian motion under ℚn\mathbb{Q}^{n}, and we have

|  |  |  |
| --- | --- | --- |
|  | Xt=x0​(t)+∫0tK​(t−s)​(θ​(s)−λ​Xs+𝟏[0,τn]​(s)​ψ​(T−s)​σ2​(s,Xs))​𝑑s+∫0tK​(t−s)​σ​(s,Xs)​𝑑Wsn.X\_{t}=x\_{0}(t)+\int\_{0}^{t}K(t-s)(\theta(s)-\lambda X\_{s}+\mathbf{1}\_{[0,\tau\_{n}]}(s)\psi(T-s)\,\sigma^{2}(s,X\_{s})\,)ds+\int\_{0}^{t}K(t-s)\sigma(s,X\_{s})dW^{n}\_{s}. |  |

Since ψ\psi is bounded and both the drift and σ\sigma are deterministic and sufficiently regular, we conclude similarly to proof of [[24](https://arxiv.org/html/2512.09590v1#bib.bib24), Theorem 4.2] that 𝔼x¯0ℚn​(supt∈[0,T]|Xt|2)≤C​(1+‖x0‖T2)\mathbb{E}\_{\bar{x}\_{0}}^{\mathbb{Q}^{n}}\left(\sup\_{t\in[0,T]}|X\_{t}|^{2}\right)\leq C\left(1+\|x\_{0}\|\_{T}^{2}\right) for a constant CC independent of nn and where ‖x0‖T:=supt∈[0,T]|x0​(t)|<+∞\|x\_{0}\|\_{T}:=\sup\_{t\in[0,T]}|x\_{0}(t)|<+\infty. Hence, by Markow’s inequality

|  |  |  |
| --- | --- | --- |
|  | ℚn​(τn<T)=ℚn​(supt∈[0,T]Xt≥n)≤1n2​𝔼x¯0ℚn​(supt∈[0,T]|Xt|2)≤Cn2​(1+‖x0‖T2),so that\displaystyle\,\mathbb{Q}^{n}(\tau\_{n}<T)=\mathbb{Q}^{n}\left(\sup\_{t\in[0,T]}X\_{t}\geq n\right)\leq\frac{1}{n^{2}}\mathbb{E}\_{\bar{x}\_{0}}^{\mathbb{Q}^{n}}\left(\sup\_{t\in[0,T]}|X\_{t}|^{2}\right)\leq\frac{C}{n^{2}}\left(1+\|x\_{0}\|\_{T}^{2}\right),\;\text{so that}\; |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼x¯0ℙ​[MT]≥𝔼x¯0ℙ​[MT​𝟏{τn≥T}]=ℚn​(τn≥T)→1as ​n→∞.\displaystyle\mathbb{E}\_{\bar{x}\_{0}}^{\mathbb{P}}[M\_{T}]\geq\mathbb{E}\_{\bar{x}\_{0}}^{\mathbb{P}}[M\_{T}\mathbf{1}\_{\{\tau\_{n}\geq T\}}]=\mathbb{Q}^{n}(\tau\_{n}\geq T)\to 1\quad\text{as }n\to\infty. |  |

We conclude that MM is a martingale.

Step 2 (The Fourier-Laplace of XTX\_{T} ).
For any function g∈Lloc1​(ℝ;ℝ)g\in L^{1}\_{\text{loc}}(\mathbb{R};\mathbb{R}), by regular Fubini’s theorem and the measure-extended Riccati–Volterra equation ([3.25](https://arxiv.org/html/2512.09590v1#S3.E25 "In Lemma 3.1. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) in Lemma [3.1](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem1 "Lemma 3.1. ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we have that for all T>0T>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T∫0T−sfλ​(T−s−r)​g​(r)​dr​μ​(d​s)+∫0Tκ12​ς2​(s)​∫0sfλ​(s−r)​g​(r)​dr​ψ​(T−s)​ds=∫0Tλ​ψ​(T−r)​g​(r)​dr.\int\_{0}^{T}\int\_{0}^{T-s}f\_{\lambda}(T-s-r)\,g(r)\,\mathrm{d}r\,\mu(\mathrm{d}s)+\int\_{0}^{T}\frac{\kappa\_{1}}{2}\varsigma^{2}(s)\,\int\_{0}^{s}f\_{\lambda}(s-r)\,g(r)\,\mathrm{d}r\,\psi(T-s)\,\mathrm{d}s=\int\_{0}^{T}\lambda\psi(T-r)\,g(r)\,\mathrm{d}r. |  | (A.80) |

Evaluating the equation ([A.79](https://arxiv.org/html/2512.09590v1#A1.E79 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) at t = 0, and using equation ([2.20](https://arxiv.org/html/2512.09590v1#S2.E20 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) for ξ0​(s)​∀s≤T\xi\_{0}(s)\;\forall\,s\leq T, we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | U0\displaystyle U\_{0} | =∫0Tξ0​(T−s)​μ​(d​s)+12​∫0Tς2​(s)​σ2​(ξ0​(s))​ψ2​(T−s)​ds\displaystyle=\int\_{0}^{T}\xi\_{0}(T-s)\,\mu(\mathrm{d}s)+\frac{1}{2}\int\_{0}^{T}\varsigma^{2}(s)\sigma^{2}(\xi\_{0}(s))\,\psi^{2}(T-s)\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0Tx0​(T−s)​μ​(d​s)+∫0TF​(s,ψ​(T−s))​x0​(s)​𝑑s+∫0Tθ​(s)​ψ​(T−s)​𝑑s+κ02​∫0Tς2​(s)​ψ2​(T−s)​𝑑s.\displaystyle=\int\_{0}^{T}x\_{0}(T-s)\,\mu(\mathrm{d}s)+\int\_{0}^{T}F(s,\psi(T-s))\,x\_{0}(s)\,ds+\int\_{0}^{T}\theta(s)\psi(T-s)\,ds+\frac{\kappa\_{0}}{2}\int\_{0}^{T}\varsigma^{2}(s)\psi^{2}(T-s)\,ds. |  |

where in the second line, we used the relation ([A.80](https://arxiv.org/html/2512.09590v1#A1.E80 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) for both x0x\_{0} and θ\theta and the measure-extended Riccati–Volterra equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). Note that, the first equality in the claim follows directly by the fact that ∀s≥0,ξ0​(s)=𝔼x¯0​[Xs]=𝔼​[Xs|X0=x¯0]\forall s\geq 0\,,\quad\xi\_{0}(s)=\mathbb{E}\_{\bar{x}\_{0}}\left[X\_{s}\right]=\mathbb{E}\left[X\_{s}|X\_{0}=\bar{x}\_{0}\right].
This provides the result. □\square

###### Lemma A.3.

The expected process at future time satisfied in the long run:

|  |  |  |
| --- | --- | --- |
|  | limt→+∞𝔼x¯0​[Xt]=limt→+∞ξ0​(t)=a​ϕ∞​𝔼x¯0​[X0]+(1−a)​μ∞λ=a​ϕ∞​x¯0+(1−a)​μ∞λ:=ξ¯0.\displaystyle\lim\_{t\to+\infty}\mathbb{E}\_{\bar{x}\_{0}}[X\_{t}]=\lim\_{t\to+\infty}\xi\_{0}(t)=a\phi\_{\infty}\mathbb{E}\_{\bar{x}\_{0}}[X\_{0}]+(1-a)\frac{\mu\_{\infty}}{\lambda}=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}:=\bar{\xi}\_{0}. |  |

Proof:
Note that fλf\_{\lambda} is integrable, hence we can pass to the limit t→∞t\to\infty in ([2.20](https://arxiv.org/html/2512.09590v1#S2.E20 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→+∞𝔼x¯0​[Xt]=limt→+∞ξ0​(t)\displaystyle\lim\_{t\to+\infty}\mathbb{E}\_{\bar{x}\_{0}}[X\_{t}]=\lim\_{t\to+\infty}\xi\_{0}(t) | =limt→+∞x0​(t)−limt→+∞∫0tfλ​(t−r)​x0​(r)​𝑑r+limt→+∞1λ​∫0tfλ​(t−r)​θ​(r)​dr\displaystyle=\lim\_{t\to+\infty}x\_{0}(t)-\lim\_{t\to+\infty}\int\_{0}^{t}f\_{\lambda}(t-r)x\_{0}(r)\,dr+\lim\_{t\to+\infty}\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-r)\theta(r)\,\mathrm{d}r |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a​ϕ∞​x¯0+(1−a)​μ∞λ,where we used the Remark on assumption [2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").\displaystyle=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda},\;\text{where we used the Remark on assumption \ref{ass:resolvent}.} |  |

This proves the desired convergence of the first moment. □\square

Proof of Proposition [4.5](https://arxiv.org/html/2512.09590v1#S4.ThmTheorem5 "Proposition 4.5. ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
The first claim [1](https://arxiv.org/html/2512.09590v1#S4.I3.i1 "item 1 ‣ Proposition 4.5. ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") of the proposition is a direct consequence of [[24](https://arxiv.org/html/2512.09590v1#bib.bib24)] combined with the fact that SS is fully determined by VV. The uniqueness in law comes from the existence of a solution to the Riccati Volterra equation. 131313In fact, the law of X is determined by the Laplace
transforms 𝔼​[exp⁡(∑i=1nui​Xti)]\mathbb{E}\big[\exp\left(\sum\_{i=1}^{n}u\_{i}\;X\_{t\_{i}}\right)\big] where 0≤t1<⋯<tn0\leq t\_{1}<\dots<t\_{n}, u1,…,un∈ℝ−u\_{1},\dots,u\_{n}\in\mathbb{R}\_{-}, and n∈ℕn\in\mathbb{N}. Uniqueness thus follows by applying Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (b) for the particular choice μt1,…,tn​(d​s)=∑i=1nui​δtn−ti​(d​s)\mu\_{t\_{1},\dots,t\_{n}}(ds)=\sum\_{i=1}^{n}u\_{i}\delta\_{t\_{n}-t\_{i}}(ds)
Consider μ∈ℳc\mu\in\mathcal{M}\_{c}, where μ​(d​s):=u​δ0​(d​s)+f​(s)​λ1​(d​s)\mu(ds):=u\,\delta\_{0}(ds)+f(s)\lambda\_{1}(ds), in equation ([3.23](https://arxiv.org/html/2512.09590v1#S3.E23 "In 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), in order to recover the Riccati–Volterra equation ([4.42](https://arxiv.org/html/2512.09590v1#S4.E42 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")). The claims in part [2](https://arxiv.org/html/2512.09590v1#S4.I3.i2 "item 2 ‣ Proposition 4.5. ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") regarding existence, uniqueness of (ψ1,ψ2)(\psi\_{1},\psi\_{2}) in ([4.42](https://arxiv.org/html/2512.09590v1#S4.E42 "In 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), and non-positivity of Re​ψ2{\rm Re\,}\psi\_{2} follow from [[3](https://arxiv.org/html/2512.09590v1#bib.bib3), Proposition 4.2]. Remark [3.7](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem7 "Remark 3.7. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") (b) confirm the validity of the exponential-affine transform formula. Alternatively, we can invoke [[3](https://arxiv.org/html/2512.09590v1#bib.bib3), Proposition 4.3], and mirror its proof (the same reasoning ) in order to get the exponential-affine transform formula ([3.29](https://arxiv.org/html/2512.09590v1#S3.E29 "In Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) with μ\mu.

The martingale property stated in part [3](https://arxiv.org/html/2512.09590v1#S4.I3.i3 "item 3 ‣ Proposition 4.5. ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), as well as the validity of equation ([4.43](https://arxiv.org/html/2512.09590v1#S4.E43 "In item 3 ‣ Proposition 4.5. ‣ 4.3 The Fake stationary Volterra Heston model and its characteristic functions. ‣ 4 Fake Stationarity Regimes of Affine Volterra Processes. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), follows directly from [[3](https://arxiv.org/html/2512.09590v1#bib.bib3), Proposition 4.1] in the case where the volatility coefficient η\eta is constant, i.e., η​(t)≡1\eta(t)\equiv 1. □\square

Proof of Proposition [5.2](https://arxiv.org/html/2512.09590v1#S5.ThmTheorem2 "Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").
(b) is a straightforward consequences of (a).
  
(a) Assuming that ψ:=ψ​(⋅,μ)\psi:=\psi(\cdot,\mu) satisfies the Riccati-Volterra equation ([A.70](https://arxiv.org/html/2512.09590v1#A1.E70 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")),
we set
F∞​(ψ):=limt→+∞F​(t,ψ)F\_{\infty}(\psi):=\lim\_{t\to+\infty}F(t,\psi).
As fλ∈ℒ2​(Leb1)f\_{\lambda}\!\in{\cal L}^{2}({\rm Leb}\_{1}) , 1{0≤s≤t}​ς2​(t−s)→limt→+∞ς2​(t):=ς∞2\mbox{\bf 1}\_{\{0\leq s\leq t\}}\varsigma^{2}(t-s)\to\lim\_{t\to+\infty}\varsigma^{2}(t):=\varsigma^{2}\_{\infty} for every s∈ℝ+s\!\in\mathbb{R}\_{+} as t→+∞t\to+\infty (owing to [[23](https://arxiv.org/html/2512.09590v1#bib.bib23), Lemma 3.9 ]) and likewise limt→+∞(ϕ−fλ∗ϕ)​(t)=a​ϕ∞\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)(t)=a\phi\_{\infty}, we have F∞​(ψ):=−λ​ψ+κ12​ς∞2​ψ2F\_{\infty}(\psi):=-\lambda\psi+\frac{\kappa\_{1}}{2}\varsigma^{2}\_{\infty}\psi^{2}.
Evaluating the equation ([A.79](https://arxiv.org/html/2512.09590v1#A1.E79 "In Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) at t = 0, and using equation ([2.20](https://arxiv.org/html/2512.09590v1#S2.E20 "In Proposition 2.2 (Wiener-Hopf transform and Forward Process). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")) for ξ0​(s)∀s≤T\xi\_{0}(s)\quad\forall s\leq T, we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x¯0​[exp⁡(u​Xt)]=exp⁡(ξ0​(t)+12​∫0tς2​(t−s)​σ2​(ξt​(t−s))​ψ​(s)2​ds).\displaystyle\mathbb{E}\_{\bar{x}\_{0}}\left[\exp\left(uX\_{t}\right)\right]=\exp\left(\xi\_{0}(t)+\frac{1}{2}\int\_{0}^{t}\varsigma^{2}(t-s)\sigma^{2}(\xi\_{t}(t-s))\,\psi(s)^{2}\,\mathrm{d}s\right). |  | (A.81) |

and likewise, noticing from the affine nature of σ2\sigma^{2} that 1{0≤s≤t}​σ2​(ξt​(t−s))→σ2​(limt→+∞ξ0​(t))\mbox{\bf 1}\_{\{0\leq s\leq t\}}\sigma^{2}(\xi\_{t}(t-s))\to\sigma^{2}(\lim\_{t\to+\infty}\xi\_{0}(t)) for every s∈ℝ+s\!\in\mathbb{R}\_{+} as t→+∞t\to+\infty by the continuity of σ\sigma
where the quantity limt→+∞ξ0​(t)=a​ϕ∞​x¯0+(1−a)​μ∞λ\lim\_{t\to+\infty}\xi\_{0}(t)=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda} as given by Lemma [A.3](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem3 "Lemma A.3. ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.").

To establish the first equality in ([5.51](https://arxiv.org/html/2512.09590v1#S5.E51 "In Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")), we appeal to the first identity from Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") and pass to the limit as t→∞t\to\infty, leveraging the continuity of the map x↦exp⁡(x)x\mapsto\exp(x). It therefore suffices to show that:

1. (i)

   limt→∞∫0t𝔼x¯0​[Xt−s]​μ​(d​s)=(a​ϕ∞​x¯0+(1−a)​μ∞λ)​μ​(ℝ+).\lim\_{t\to\infty}\int\_{0}^{t}\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]\,\mu(ds)=\left(a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)\mu(\mathbb{R}\_{+}).
2. (ii)

   limt→∞∫0tς2​(s)​σ2​(𝔼x¯0​[Xs])​ψ​(t−s)2​𝑑s=ς∞2​σ2​(a​ϕ∞​x¯0+(1−a)​μ∞λ)​∫0∞ψ​(s)2​𝑑s\lim\_{t\to\infty}\int\_{0}^{t}\varsigma^{2}(s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{s}])\,\psi(t-s)^{2}\,ds=\varsigma^{2}\_{\infty}\sigma^{2}\left(a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}\right)\int\_{0}^{\infty}\psi(s)^{2}ds.

Set x¯:=a​ϕ∞​x¯0+(1−a)​μ∞λ\bar{x}:=a\phi\_{\infty}\bar{x}\_{0}+(1-a)\frac{\mu\_{\infty}}{\lambda}.
Since x¯=limt→∞𝔼x¯0​[Xt]\bar{x}=\lim\_{t\to\infty}\mathbb{E}\_{\bar{x}\_{0}}[X\_{t}] by Lemma [A.3](https://arxiv.org/html/2512.09590v1#A1.ThmTheorem3 "Lemma A.3. ‣ Appendix A Supplementary material and Proofs. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), we have

|  |  |  |
| --- | --- | --- |
|  | ∫0t𝔼x¯0​[Xt−s]​μ​(d​s)−x¯​μ​(ℝ+)=∫0t(𝔼x¯0​[Xt−s]−x¯)​μ​(d​s)−x¯​∫t+∞μ​(d​s).\displaystyle\int\_{0}^{t}\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]\,\mu(ds)-\bar{x}\mu(\mathbb{R}\_{+})=\int\_{0}^{t}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]-\bar{x})\,\mu(ds)-\bar{x}\int\_{t}^{+\infty}\mu(ds). |  |

so that, by the triangle inequality,
|∫0t𝔼x¯0​[Xt−s]​μ​(d​s)−x¯​μ​(ℝ+)|≤|∫0t(𝔼x¯0​[Xt−s]−x¯)​μ​(d​s)|+x¯​|μ|​((t,∞))\left|\int\_{0}^{t}\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]\,\mu(ds)-\bar{x}\mu(\mathbb{R}\_{+})\right|\leq\left|\int\_{0}^{t}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]-\bar{x})\,\mu(ds)\right|+\bar{x}|\mu|((t,\infty))
First note that we can split the first integral as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∫0t(𝔼x¯0​[Xt−s]−x¯)​μ​(d​s)|\displaystyle\left|\int\_{0}^{t}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]-\bar{x})\,\mu(ds)\right| | =|∫0t−Aϵ(𝔼x¯0​[Xt−s]−x¯)​μ​(d​s)|+|∫t−Aϵt(𝔼x¯0​[Xt−s]−x¯)​μ​(d​s)|\displaystyle=\left|\int\_{0}^{t-A\_{\epsilon}}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]-\bar{x})\,\mu(ds)\right|+\left|\int\_{t-A\_{\epsilon}}^{t}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]-\bar{x})\,\mu(ds)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϵ​|μ|​(ℝ+)+(sups≥0𝔼x¯0​[|Xs|]+x¯)​|μ|​((t−Aϵ,t]).\displaystyle\leq\epsilon|\mu|(\mathbb{R}\_{+})+\left(\sup\_{s\geq 0}\mathbb{E}\_{\bar{x}\_{0}}[|X\_{s}|]+\bar{x}\right)|\mu|((t-A\_{\epsilon},t]). |  |

where AϵA\_{\epsilon} is chosen such that ∀s≥Aϵ\forall\,s\geq A\_{\epsilon}, we have |𝔼x¯0​[Xs]−x¯|≤ϵ|\mathbb{E}\_{\bar{x}\_{0}}[X\_{s}]-\bar{x}|\leq\epsilon. Moreover, ∀s​s∈(0,t−Aϵ)\forall\,ss\in(0,t-A\_{\epsilon}), we have t−s≥Aϵt-s\geq A\_{\epsilon} for tt large enough (say t≥2​Aϵt\geq 2A\_{\epsilon}), and hence this implies that |𝔼x¯0​[Xt−s]−x¯|≤ϵ,∀s∈(0,t−Aϵ).\left|\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]-\bar{x}\right|\leq\epsilon,\quad\forall s\in(0,t-A\_{\epsilon}).
We thus have:

|  |  |  |
| --- | --- | --- |
|  | |∫0t𝔼x¯0​[Xt−s]​μ​(d​s)−x¯​μ​(ℝ+)|≤ϵ​|μ|​(ℝ+)+(sups≥0𝔼x¯0​[|Xs|])​|μ|​((t−Aϵ,t])+2​x¯​|μ|​((t−Aϵ,∞)).\left|\int\_{0}^{t}\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}]\,\mu(ds)-\bar{x}\mu(\mathbb{R}\_{+})\right|\leq\epsilon|\mu|(\mathbb{R}\_{+})+\left(\sup\_{s\geq 0}\mathbb{E}\_{\bar{x}\_{0}}[|X\_{s}|]\right)|\mu|((t-A\_{\epsilon},t])+2\bar{x}|\mu|((t-A\_{\epsilon},\infty)). |  |

Since |μ|​(ℝ+)<∞|\mu|(\mathbb{R}\_{+})<\infty, we have |μ|​((t−Aϵ,t])→0|\mu|((t-A\_{\epsilon},t])\to 0 and |μ|​((t−Aϵ,∞))→0|\mu|((t-A\_{\epsilon},\infty))\to 0 as t→∞t\to\infty, which proves (i).

Likewise for (ii) we
have,

|  |  |  |
| --- | --- | --- |
|  | |∫0tς2​(s)​σ2​(𝔼x¯0​[Xs])​ψ​(t−s)2​𝑑s−ς∞2​σ2​(x¯)​∫0∞ψ​(s)2​𝑑s|\displaystyle\ \left|\int\_{0}^{t}\varsigma^{2}(s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{s}])\,\psi(t-s)^{2}\,ds-\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\int\_{0}^{\infty}\psi(s)^{2}ds\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫0t|ς2​(t−s)​σ2​(𝔼x¯0​[Xt−s])−ς∞2​σ2​(x¯)|​ψ2​(s)​𝑑s+ς∞2​σ2​(x¯)​∫t∞ψ​(s)2​𝑑s.\displaystyle\leq\int\_{0}^{t}\left|\varsigma^{2}(t-s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}])\,-\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right|\psi^{2}(s)ds+\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\int\_{t}^{\infty}\psi(s)^{2}ds. |  |

The second term tends to zero since ψ∈L2​(ℝ+;ℝ)\psi\in L^{2}(\mathbb{R}\_{+};\mathbb{R}). For the first term, choose AϵA\_{\epsilon} such that for all s≥Aϵs\geq A\_{\epsilon}, we have |ς2​(s)​σ2​(𝔼x¯0​[Xs])−ς∞2​σ2​(x¯)|≤ϵ\left|\varsigma^{2}(s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{s}])\,-\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right|\leq\epsilon. Moreover, for all s∈(0,t−Aϵ)s\in(0,t-A\_{\epsilon}), we have t−s≥Aϵt-s\geq A\_{\epsilon} for tt large enough (say t≥2​Aϵt\geq 2A\_{\epsilon}), and hence this implies that

|  |  |  |
| --- | --- | --- |
|  | |ς2​(t−s)​σ2​(𝔼x¯0​[Xt−s])−ς∞2​σ2​(x¯)|≤ϵ,∀s∈(0,t−Aϵ).\left|\varsigma^{2}(t-s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}])\,-\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right|\leq\epsilon,\;\forall s\in(0,t-A\_{\epsilon}). |  |

|  |  |  |
| --- | --- | --- |
|  | ∫0t|ς2​(t−s)​σ2​(𝔼x¯0​[Xt−s])−ς∞2​σ2​(x¯)|​ψ2​(s)​𝑑s=∫0t−Aϵ|ς2​(t−s)​σ2​(𝔼x¯0​[Xt−s])−ς∞2​σ2​(x¯)|​ψ2​(s)​𝑑s\displaystyle\ \int\_{0}^{t}\left|\varsigma^{2}(t-s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}])\,-\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right|\psi^{2}(s)ds=\int\_{0}^{t-A\_{\epsilon}}\left|\varsigma^{2}(t-s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}])\,-\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right|\psi^{2}(s)ds |  |
|  |  |  |
| --- | --- | --- |
|  | +∫t−Aϵt|ς2​(t−s)​σ2​(𝔼x¯0​[Xt−s])−ς∞2​σ2​(x¯)|​ψ2​(s)​𝑑s\displaystyle\hskip 142.26378pt+\int\_{t-A\_{\epsilon}}^{t}\left|\varsigma^{2}(t-s)\,\sigma^{2}(\mathbb{E}\_{\bar{x}\_{0}}[X\_{t-s}])\,-\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right|\psi^{2}(s)ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤ϵ​∫0+∞ψ2​(s)​𝑑s+∫0∞𝟏[t−Aϵ,t]​(s)​(σ2​(sups≥0𝔼x¯0​[|Xs|])​ς2​(t−s)+ς∞2​σ2​(x¯))​ψ2​(s)​ds\displaystyle\hskip 45.52458pt\leq\epsilon\int\_{0}^{+\infty}\psi^{2}(s)\,ds+\int\_{0}^{\infty}\mathbf{1}\_{[t-A\_{\epsilon},\,t]}(s)\,\left(\sigma^{2}\big(\sup\_{s\geq 0}\mathbb{E}\_{\bar{x}\_{0}}[|X\_{s}|]\big)\,\varsigma^{2}(t-s)+\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right)\,\psi^{2}(s)\,\mathrm{d}s |  |
|  |  |  |
| --- | --- | --- |
|  | ≤ϵ​∫0+∞ψ2​(s)​𝑑s+(‖ς2‖∞​σ2​(sups≥0𝔼x¯0​[|Xs|])+ς∞2​σ2​(x¯))​∫0∞𝟏[t−Aϵ,t]​(s)​ψ2​(s)​ds.\displaystyle\hskip 45.52458pt\leq\epsilon\int\_{0}^{+\infty}\psi^{2}(s)\,ds+\left(\|\varsigma^{2}\|\_{\infty}\sigma^{2}\big(\sup\_{s\geq 0}\mathbb{E}\_{\bar{x}\_{0}}[|X\_{s}|]\big)+\varsigma^{2}\_{\infty}\sigma^{2}\left(\bar{x}\right)\right)\int\_{0}^{\infty}\mathbf{1}\_{[t-A\_{\epsilon},\,t]}(s)\,\psi^{2}(s)\,\mathrm{d}s. |  |

By the dominated convergence theorem, the second term vanishes as t→∞t\to\infty. Since ϵ\epsilon was arbitrary, this establishes (ii) and thereby completes the proof of the first claim.
  
For the second identity in part (a), use the second identity from Theorem [3.6](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem6 "Theorem 3.6. ‣ 3.2 Conditional Laplace functional of inhomogeneous affine Volterra processes ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") to pass to the limit t→∞t\to\infty, i.e., we show that:
1. limt→∞∫0tx0​(t−s)​μ​(d​s)=ϕ∞​x¯0​μ​(ℝ+)\lim\_{t\to\infty}\int\_{0}^{t}x\_{0}(t-s)\,\mu(ds)=\phi\_{\infty}\bar{x}\_{0}\mu(\mathbb{R}\_{+});
 
  
2. limt→∞∫0tF​(s,ψ​(t−s))​x0​(s)​𝑑s=(∫0∞F∞​(ψ​(s))​𝑑s)​ϕ∞​x¯0\lim\_{t\to\infty}\int\_{0}^{t}F(s,\psi(t-s))\,x\_{0}(s)\,ds=\Big(\int\_{0}^{\infty}F\_{\infty}(\psi(s))\,ds\Big)\phi\_{\infty}\bar{x}\_{0};
  
3. limt→∞∫0tθ​(s)​ψ​(t−s)​𝑑s=(∫0∞ψ​(s)​𝑑s)​μ∞\lim\_{t\to\infty}\int\_{0}^{t}\theta(s)\,\psi(t-s)\,ds=\Big(\int\_{0}^{\infty}\psi(s)\,ds\Big)\mu\_{\infty};  4. limt→∞κ02​∫0tς2​(s)​ψ2​(t−s)​𝑑s=κ02​ς∞2​∫0∞ψ2​(s)​𝑑s\lim\_{t\to\infty}\frac{\kappa\_{0}}{2}\int\_{0}^{t}\varsigma^{2}(s)\,\psi^{2}(t-s)\,ds=\frac{\kappa\_{0}}{2}\varsigma^{2}\_{\infty}\int\_{0}^{\infty}\psi^{2}(s)\,ds.
Assertions 3. and 4. follow directly from the arguments presented above for the first identity, as the proofs are analogous by definition. Moreover, Corollary [3.5](https://arxiv.org/html/2512.09590v1#S3.ThmTheorem5 "Corollary 3.5. ‣ 3.1 Analysis of the Measure-extended Riccati–Volterra Equation ‣ 3 Measure-extended Laplace Functional for Inhomogeneous Affine Volterra Process ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.") ensures that the desired integrability still holds for T=∞T=\infty, namely ∫0∞(|ψ​(t)|+|ψ​(t)|2)​𝑑t<∞.\int\_{0}^{\infty}\left(|\psi(t)|+|\psi(t)|^{2}\right)dt<\infty.
Once again, we leverage Assumption (𝒦)​(i​i​i)(\mathcal{K})(iii) in [2.2](https://arxiv.org/html/2512.09590v1#S2.Thmassumption2 "Assumption 2.2 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 2.2 Wiener-Hopf equations and Forward Process ‣ 2 Preliminaries on Volterra processes with convolutive kernels and Some useful Tools: Resolvents and Wiener-Hopf equations. ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model."), to obtain the claim 1., which follows directly. Similarly, the claim in 2. follows from the same assumption after an appropriate change of variables.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∫0t|x0​(t−s)​μ​(d​s)|\displaystyle\int\_{0}^{t}|x\_{0}(t-s)\,\mu(ds)| | ≤supt≥0|x0​(t)|​∫0t|μ​(d​s)|≤|μ|​(ℝ+)​‖x0‖∞<∞.\displaystyle\leq\sup\_{t\geq 0}|x\_{0}(t)|\int\_{0}^{t}|\mu(ds)|\leq|\mu|(\mathbb{R}\_{+})\|x\_{0}\|\_{\infty}<\infty. |  | (A.82) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0t|F​(s,ψ​(t−s))​x0​(s)|​𝑑s\displaystyle\int\_{0}^{t}\left|F(s,\psi(t-s))\,x\_{0}(s)\right|\,ds | ≤(λ​∫0t|ψ​(t−s)|​𝑑s+κ12​∫0tς2​(s)​|ψ​(t−s)|2​𝑑s)​‖x0‖∞\displaystyle\leq\left(\lambda\int\_{0}^{t}|\psi(t-s)|\,ds+\frac{\kappa\_{1}}{2}\int\_{0}^{t}\varsigma^{2}(s)|\psi(t-s)|^{2}\,ds\right)\|x\_{0}\|\_{\infty} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤(λ​∫0t|ψ​(s)|​𝑑s+κ12​‖ς2‖∞​∫0t|ψ​(s)|2​𝑑s)​‖x0‖∞<∞.\displaystyle\leq\left(\lambda\int\_{0}^{t}|\psi(s)|\,ds+\frac{\kappa\_{1}}{2}\|\varsigma^{2}\|\_{\infty}\int\_{0}^{t}|\psi(s)|^{2}\,ds\right)\|x\_{0}\|\_{\infty}<\infty. |  | (A.83) |

Taken together, the foregoing discussion and these estimates establish the convergence in ([5.52](https://arxiv.org/html/2512.09590v1#S5.E52 "In Proposition 5.2. ‣ 5.2 Existence of limiting distributions ‣ 5 Towards Long run behaviour: Confluence, Limiting distributions and Asymptotics ‣ On Inhomogeneous Affine Volterra Processes: Stationarity and Applications to the Volterra Heston Model.")).
This completes the proof and we are done. □\square