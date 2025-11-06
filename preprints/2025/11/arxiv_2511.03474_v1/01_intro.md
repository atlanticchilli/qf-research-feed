---
authors:
- Emmanuel Gnabeyeu
- Gilles Pagès
doc_id: arxiv:2511.03474v1
family_id: arxiv:2511.03474
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On a Stationarity Theory for Stochastic Volterra Integral Equations
url_abs: http://arxiv.org/abs/2511.03474v1
url_html: https://arxiv.org/html/2511.03474v1
venue: arXiv q-fin
version: 1
year: 2025
---


Emmanuel Gnabeyeu
  
Laboratoire de Probabilités


 Statistique et Modélisation (LPSM)


 UMR 8001



  
Sorbonne Université and Université Paris Cité


 Paris


 France.
  
E-mail: emmanuel.gnabeyeu\_mbiada@sorbonne-universite.fr


Gilles Pagès
  
Laboratoire de Probabilités


 Statistique et Modélisation (LPSM)


 UMR 8001



  
Sorbonne Université


 case 158


 4


 pl. Jussieu


 F-75252 Paris Cedex 5


 France.
  
E-mail: gilles.pages@sorbonne-universite.fr

(September 1, 2025)

###### Abstract

This paper provide a comprehensive analysis of the finite and long time behavior of continuous-time non-Markovian dynamical systems, with a focus on the forward Stochastic Volterra Integral Equations(SVIEs).
We investigate the properties of solutions to such equations specifically their stationarity, both over a finite horizon and in the long run. In particular, we demonstrate that such an equation does not exhibit a strong stationary regime unless the kernel is constant or in a degenerate settings. However, we show that it is possible to induce a fake stationary regime in the sense that all marginal distributions share the same expectation and variance. This effect is achieved by introducing a deterministic stabilizer ς\varsigma associated with the kernel.
We also look at the LpL^{p} -confluence (for p>0p>0) of such process as time goes to infinity(i.e. we investigate if its marginals when starting from various initial values are confluent in LpL^{p} as time goes to infinity) and finally the functional weak long-run assymptotics for some classes of diffusion coefficients. Those results are applied to the case of Exponential-Fractional Stochastic Volterra Integral Equations, with an α\alpha-gamma fractional integration kernel, where α≤1\alpha\leq 1 enters the regime of rough path whereas α>1\alpha>1 regularizes diffusion paths and invoke long-term memory, persistence or long range dependence. With this fake stationary Volterra processes, we introduce a family of stabilized volatility models.

Keywords: Stochastic Volterra Processes, Stochastic Differential Equations, Fourier-Laplace Transforms, Jordan-Cauchy Residue Theorem, Regular Variation, Tauberian Theorems, Limit theorems.

## 1 Introduction

The theory of stochastic Volterra integral equations (SVIEs) has its origins in the 1980s and has been widely developed since then. These equations which have recently attracted much attention in the mathematical finance community have
been introduced mostly with non-singular kernel for modelling in population dynamics, biology
and physics [mohammed1998](https://arxiv.org/html/2511.03474v1#bib.bib34) , in order to generalize modelling to non-Markovian stochastic systems with
some memory effect. They were also motivated particularly by the physics of heat transfer [gripenberg1990](https://arxiv.org/html/2511.03474v1#bib.bib4)  and have undergone extensive mathematical study. Early investigations can be traced back to the seminal work of Berger et al. (see [Berger1980a](https://arxiv.org/html/2511.03474v1#bib.bib5) ,[Berger1980b](https://arxiv.org/html/2511.03474v1#bib.bib6) )
who derived existence and uniqueness results for SVIEs driven by Brownian motion with Lipschitz continuous coefficients. These initial results were subsequently extended in various directions.
For instance, [Protter1985](https://arxiv.org/html/2511.03474v1#bib.bib40)  generalized the existence and uniqueness results to SVIEs driven by right-continuous semimartingales and smooth kernels. An example of such a kernel is K​(t,s)=(t−s)H−12K(t,s)=(t-s)^{H-\frac{1}{2}}, where HH is known as the Hurst coefficient. Others studies focused on extensions that incorporated anticipative integrands, utilizing Skorokhod integration and Malliavin calculus (This was explored in [Pardoux1990](https://arxiv.org/html/2511.03474v1#bib.bib38)  and [Alos1997](https://arxiv.org/html/2511.03474v1#bib.bib3) ).
[Cochran1995](https://arxiv.org/html/2511.03474v1#bib.bib12)  and [Coutin2001](https://arxiv.org/html/2511.03474v1#bib.bib14)  focused on SVIEs with singular kernels. In a more recent contribution, [Wang2008](https://arxiv.org/html/2511.03474v1#bib.bib49)  proved the existence and uniqueness of solutions to SVIEs with singular kernels and non-Lipschitz coefficients, utilizing a condition analogous to that of [Yamada1971](https://arxiv.org/html/2511.03474v1#bib.bib50)  for stochastic differential equations. Additionally, [ZhangXi2010](https://arxiv.org/html/2511.03474v1#bib.bib51)  examined SVIEs in Banach spaces with locally Lipschitz coefficients and singular kernels.

In the late 1990s, attempts were made within the financial community to incorporate long-memory effects into continuous-time stochastic volatility models. This shift was largely motivated by the need to capture persistent dependencies observed in financial markets, particularly through fractional Brownian motion (see [CoutinD2001](https://arxiv.org/html/2511.03474v1#bib.bib15) ; [ComteR1998](https://arxiv.org/html/2511.03474v1#bib.bib13) ). Earlier studies, such as those by Comte and Renault [ComteR1998](https://arxiv.org/html/2511.03474v1#bib.bib13) , found that H>1/2H>1/2 was a key parameter in capturing long memory in volatility dynamics.
In the early 2000s, research shifted to Volterra equations with singular kernels that blow up as s→ts\to t (i.e., K​(t,s)→+∞K(t,s)\to+\infty as s→ts\to t or H<1/2H<1/2), following the empirical observation in [GatheralJR2018](https://arxiv.org/html/2511.03474v1#bib.bib19)  that volatility paths exhibit low Hölder regularity (H≈0.1H\approx 0.1). As a result, there has been a resurgence of interest in SVIEs within mathematical finance, particularly with the rise of rough volatility models, as highlighted in the work of [ElEuchR2018](https://arxiv.org/html/2511.03474v1#bib.bib16) . These models, which use the above kernel, naturally capture this feature, as their paths have a Hölder continuity exponent HH. Singular kernel Volterra equations also arise as limiting dynamics in models of order books via nearly unstable Hawkes processes (see [JaissonR2016](https://arxiv.org/html/2511.03474v1#bib.bib29) ; [EGnabeyeuR2025](https://arxiv.org/html/2511.03474v1#bib.bib22) ).

In both context, such processes are used to mimic Fractional Brownian motion-driven stochastic differential equations (SDEs). More specifically, within these frameworks, Volterra equations with fractional kernels KK provide a more tractable alternative than SDEs involving stochastic integrals with respect to true HH-fractional Brownian motions, which would otherwise require the use of “high-order” rough path theory or regularity structures.
As the debate on the empirical value of the Hurst index remains controversial in the literature, we note that the setting considered in this paper covers the full range of the Hurst coefficient, namely H:=α−12∈(0,1)H:=\alpha-\tfrac{1}{2}\in(0,1).

By considering a deterministic continuous function ϕ\phi, typically normalized such that ϕ​(0)=1\phi(0)=1, a rather general form of the stochastic version of the Volterra equation on [0,T][0,T] in ℝ\mathbb{R} for any T>0T>0 takes the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Xt=X0ϕ(t)+∫0tK(t,s)b(s,Xs)ds+∫0tK(t,s)σ(s,Xs)dWs,X0⟂⟂W.X0:(Ω,ℱ,ℙ)→(ℝ,ℬ​(ℝ))​ is a given initial random variable\begin{cases}X\_{t}=X\_{0}\phi(t)+\int\_{0}^{t}K(t,s)b(s,X\_{s})\,ds+\int\_{0}^{t}K(t,s)\sigma(s,X\_{s})\,dW\_{s},\quad X\_{0}\perp\!\!\!\perp W.\\ X\_{0}:(\Omega,\mathcal{F},\mathbb{P})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))\text{ is a given initial random variable}\end{cases} |  | (1.1) |

where b,σ:[0,T]×ℝ→ℝb,\sigma:[0,T]\times\mathbb{R}\to\mathbb{R} are Lipstchiz continuous function
and K​(t,s)K(t,s) a deterministic kernel modeling the memory or hereditary structure of the system. The process (Wt)t≥0(W\_{t})\_{t\geq 0} is an ℝ\mathbb{R}-valued Brownian motion independent of X0X\_{0}, both defined on a probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) and ℱt⊃ℱt,X0,W\mathcal{F}\_{t}\supset\mathcal{F}\_{t,X\_{0},W} a filtration satisfying the usual conditions.
Such equations ([1.1](https://arxiv.org/html/2511.03474v1#S1.E1 "In 1 Introduction ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) naturally arise in the modeling of random systems with memory effects and irregular behaviour, including in mathematical finance, physics, and biology.

### 1.1 Our contribution

In this paper, we investigate a weak form of stationarity for SVIEs with affine drifts and convolutive kernels of the form ([1.1](https://arxiv.org/html/2511.03474v1#S1.E1 "In 1 Introduction ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).
Specifically, our main result follow that of [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36)  and states that, under a suitable functional equation satisfied by a stabilizing function, the process of the form ([1.1](https://arxiv.org/html/2511.03474v1#S1.E1 "In 1 Introduction ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) may exhibit a form of *fake stationarity regime*, where the solution has either constant moments up to the order 2 or the same marginal distribution at each time tt in the Gaussian case (typically pseudo-Ornstein-Uhlenbeck process, which could be called a fake stationary regime of type II).
Moreover, we establish the existence of limiting distributions. Formally, we prove that as u→∞u\to\infty, the shifted process (Xtu)t≥0(X^{u}\_{t})\_{t\geq 0}, defined by Xtu:=Xt+uX^{u}\_{t}:=X\_{t+u}, converges in law to a limiting continuous process X∞X^{\infty}. Unlike in [EGnabeyeuPR2025](https://arxiv.org/html/2511.03474v1#bib.bib21)  (see also [friesen2022volterra](https://arxiv.org/html/2511.03474v1#bib.bib18) ; [Jacquieretal2022](https://arxiv.org/html/2511.03474v1#bib.bib28) ), this convergence does not imply that the limiting process is stationary (in the sense that its finite-dimensional distributions are invariant under time shifts). However, we prove that, under *fake stationarity* regime, the limiting process is weak L2L^{2}-stationary.
Furthermore, since we do not characterize the dynamics of the limiting process, the notion of *fake stationarity* provides a tractable alternative framework for analyzing both short- and long-term behaviors in settings where classical stationarity is either unavailable or analytically intractable.

From an applied perspective, this result may have important implications for volatility models widely used in mathematical finance. In particular, it suggests the possibility of introducing stabilized versions of such models, where the dynamics driving the asset’s (typically equity) volatility exhibit constant mean and variance over time. A key advantage of the stabilized formulation lies in its ability to overcome a well-known limitation of classical and rough Heston models [Heston1993](https://arxiv.org/html/2511.03474v1#bib.bib27) ; [el2019characteristic](https://arxiv.org/html/2511.03474v1#bib.bib17)  driven by mean-reverting CIR or Volterra-CIR dynamics.
These models typically display two distinct regimes: a short-maturity regime, where the initial condition (deterministic value at the origin, often the long run mean) is prominent and the variance remains very small, and a long-term regime, which may correspond to the stationary distribution of the process.
In contrast, the stabilized model provides a unified and coherent framework that captures both short- and long-maturity behaviors within a single regime, thereby enabling robust and consistent fitting across the full term structure.

### 1.2 Plan of the paper and Notations

The remainder of the paper is organized as follows: In Section [2](https://arxiv.org/html/2511.03474v1#S2 "2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we review key properties of stochastic Volterra equations with convolutive kernels, including results on existence, moment control, and a special focus on processes with affine drift. In this setting, specific analytical tools become available, such as the *resolvent* and the solution of the *Wiener–Hopf equation*.
Section [3](https://arxiv.org/html/2511.03474v1#S3 "3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") investigates the conditions under which SVIEs ([1.1](https://arxiv.org/html/2511.03474v1#S1.E1 "In 1 Introduction ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) with affine drift admit a weak stationary regime, in the spirit of [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) , in a setting where the volatility coefficient is separable in time and state. The time-dependent (deterministic) multiplicative function, referred to as the *stabilizer*, appears in the Brownian convolution and serves to regulate or control the volatility of the process. In the *fake stationarity* regime, this stabilizing function is characterized as the solution to an intrinsic convolution equation involving the derivative of the resolvent associated with the Volterra kernel. Next, in Section [3.3](https://arxiv.org/html/2511.03474v1#S3.SS3 "3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we provide an example of a *fake stationary regime of order p=2p=2* when the state-depedndent diffusion coefficient is a trinomial function.
It follows in Section [4](https://arxiv.org/html/2511.03474v1#S4 "4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") the analysis of the confluence and long-run behavior of these time-inhomogenous processes as time tends to infinity. Specifically, we investigate, for such stabilized processes, the functional weak asymptotics of the time-shifted process (Xt+s)s≥0(X\_{t+s})\_{s\geq 0} as t→+∞t\to+\infty, which turns out to be a weakly L2L^{2}-stationary process.
Finally, in Section [5](https://arxiv.org/html/2511.03474v1#S5 "5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we apply these results to the case of SVIEs with an α\alpha-fractional integration kernel for α∈(1,32)\alpha\in\left(1,\frac{3}{2}\right) (long-term memory, persistence or long range dependence), where the case α∈(12,1)\alpha\in\left(\frac{1}{2},1\right) has been extensively studied in ([Pages2024,](https://arxiv.org/html/2511.03474v1#bib.bib36) , Section 5, Theorem 5.2). In Section [6](https://arxiv.org/html/2511.03474v1#S6 "6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we further extend the application to SVIEs with an α\alpha -exponential fractional integration kernel for α∈(12,32)\alpha\in\left(\frac{1}{2},\frac{3}{2}\right) involving both the *rough/short memory* and *long-term memory* effects inherent to Volterra equations.

Notations.

∙\bullet Denote 𝕋=[0,T]⊂ℝ+\mathbb{T}=[0,T]\subset\mathbb{R}\_{+}, Lebd{\rm Leb}\_{d} the Lebesgue measure on (ℝd,ℬ​o​r​(ℝd))(\mathbb{R}^{d},{\cal B}or(\mathbb{R}^{d})), ℍ:=ℝd,\mathbb{H}:=\mathbb{R}^{d}, etc.

∙\bullet 𝕏:=𝒞​([0,T],ℍ)​(resp.𝒞0​([0,T],ℍ))\mathbb{X}:={\cal C}([0,T],\mathbb{H})(\text{resp.}\quad{\mathcal{C}\_{0}}([0,T],\mathbb{H})) denotes the set of continuous functions(resp. null at 0) from [0,T][0,T] to ℍ\mathbb{H} and ℬ​o​r​(𝒞d){\cal B}or({\cal C}\_{d}) denotes the Borel σ\sigma-field of 𝒞d{\cal C}\_{d} induces by the sup\sup-norm topology.

∙\bullet For p∈(0,+∞)p\in(0,+\infty), Lℍp​(ℙ)L\_{\mathbb{H}}^{p}(\mathbb{P}) or simply Lp​(ℙ)L^{p}(\mathbb{P}) denote the set of ℍ\mathbb{H}-valued random vectors XX defined on a probability space (Ω,𝒜,ℙ)(\Omega,{\cal A},\mathbb{P}) such that ‖X‖p:=(𝔼​[‖X‖ℍp])1/p<+∞\|X\|\_{p}:=(\mathbb{E}[\|X\|\_{\mathbb{H}}^{p}])^{1/p}<+\infty. For f:E→ℝf:E\to\mathbb{R}, ‖f‖sup=supx∈E|f​(x)|\displaystyle\|f\|\_{\sup}=\sup\_{x\in E}|f(x)|

∙\bullet For f,g∈ℒℝ+,l​o​c1​(ℝ+,Leb1)f,g\!\in{\cal L}\_{\mathbb{R}\_{+},loc}^{1}(\mathbb{R}\_{+},{\rm Leb}\_{1}), we define their convolution by f∗g​(t)=∫0tf​(t−s)​g​(s)​𝑑sf\*g(t)=\int\_{0}^{t}f(t-s)g(s)ds, t≥0t\geq 0.

∙\bullet For f,g∈ℒℝ+,l​o​c2​(ℝ+,Leb)f,g\!\in{\cal L}\_{\mathbb{R}\_{+},loc}^{2}(\mathbb{R}\_{+},{\rm Leb}) and WW a Brownian motion, we define their stochastic convolution by

f∗Wg=∫0tf​(t−s)​g​(s)​𝑑Ws,t≥0.f\stackrel{{\scriptstyle W}}{{\*}}g=\int\_{0}^{t}f(t-s)g(s)dW\_{s},\quad t\geq 0.

∙\bullet For a random variable/vector/process XX, we denote by L​(X)L(X) or [X][X] its law or distribution.

∙\bullet X⟂⟂YX\perp\!\!\!\perp Y stands for independence of random variables, vectors or processes XX and YY.

∙\bullet Γ​(a)=∫0+∞ua−1​e−u​𝑑u,a>0,andB​(a,b)=∫01ua−1​(1−u)b−1​𝑑u,a,b>0.\Gamma(a)=\int\_{0}^{+\infty}u^{a-1}e^{-u}\,du,\;a>0,\;\text{and}\quad B(a,b)=\int\_{0}^{1}u^{a-1}(1-u)^{b-1}\,du,\quad a,b>0.
We will extensively use the classical identities:
Γ​(a+1)=a​Γ​(a)​and​B​(a,b)=Γ​(a)​Γ​(b)Γ​(a+b).\Gamma(a+1)=a\,\Gamma(a)\;\text{and}\;B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}.

## 2 Background on Stochastic Volterra equations with convolutive kernels

We will assume that, the process (Xt)t≥0(X\_{t})\_{t\geq 0} takes values in ℝ\mathbb{R}, i.e. ℍ=ℍ~=ℝ\mathbb{H}=\tilde{\mathbb{H}}=\mathbb{R} and 𝕏:=𝒞​([0,T],ℝ)\mathbb{X}:={\cal C}([0,T],\mathbb{R}).

###### Definition 2.1 (Convolutive kernel and Volterra equations).

A kernel K:{(s,t)∈ℝ+2:0≤s<t}→ℝ+K:\{(s,t)\!\in\mathbb{R}\_{+}^{2}:0\leq s<t\}\to\mathbb{R}\_{+} satisfying ∀s,t≥0,s<t,K​(s,t)=K​(0,t−s)\forall\,s,\,t\geq 0,\;s<t,\quad K(s,t)=K(0,t-s)
is called a convolutive kernel. A Volterra equation based on a convolutive kernel is called a convolutive Volterra equation.

To alleviate notations, we denote from now on K​(t):=K​(0,t)K(t):=K(0,t) so that K​(s,t)=K​(t−s)K(s,t)=K(t-s). For convenience we also extend the function K:ℝ+→ℝ+K:\mathbb{R}\_{+}\to\mathbb{R}\_{+} to the whole real line by setting K​(t)=0K(t)=0, t≤0t\leq 0.

### 2.1 Volterra processes with convolutive kernels

A significant difference between regular diffusion processes and Volterra processes from a technical viewpoint comes from the presence of the kernels which introduces some memory in the dynamics of the process, depriving us of the Markov property and usual tools of stochastic calculus.
We are interested in the convolutive stochastic Volterra equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0​ϕ​(t)+∫0tK​(t−s)​b​(s,Xs)​𝑑s+∫0tK​(t−s)​σ​(s,Xs)​𝑑Ws,t≥0.X\_{t}=X\_{0}\phi(t)+\int\_{0}^{t}K(t-s)b(s,X\_{s})ds+\int\_{0}^{t}K(t-s)\sigma(s,X\_{s})dW\_{s},\quad t\geq 0. |  | (2.2) |

where b:𝕋×ℝ→ℝb:\mathbb{T}\times\mathbb{R}\to\mathbb{R}, σ:𝕋×ℝ→ℝ\sigma:\mathbb{T}\times\mathbb{R}\to\mathbb{R} are Borel measurable, K∈ℒl​o​c,ℝ+2​(Leb1)K\!\in{\cal L}^{2}\_{loc,\mathbb{R}\_{+}}({\rm Leb}\_{1}) is a convolutive kernel and (Wt)t≥0(W\_{t})\_{t\geq 0} is a standard Brownian motion independent from the ℝ\mathbb{R}-valued random variable X0X\_{0} both defined on a probability space (Ω,𝒜,ℙ)(\Omega,{\cal A},\mathbb{P}). Let (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0} be a filtration (satisfying the usual conditions) such that X0X\_{0} is ℱ0{\cal F}\_{0}-measurable and WW is an (ℱt)({\cal F}\_{t})-Brownian motion independent of X0X\_{0}. X0​ϕX\_{0}\phi is thus a random function evolving deterministically for t>0t>0, i.e. X0​ϕX\_{0}\phi is ℱ0{\cal F}\_{0}-measurable.

###### Assumption 2.2 (On Volterra Equations with convolutive kernels).

Assume that the kernel KK satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | for every ​T>0,(𝒦T,βi​n​t)∃β>1​such that​K∈Ll​o​c2​β​(Leb1).\text{for every }\,T>0,\quad\big({\cal K}^{int}\_{T,\beta}\big)\hskip 42.67912pt\exists\,\beta>1\quad\mbox{such that}\quad K\!\in L^{2\beta}\_{loc}({\rm Leb}\_{1}). |  | (2.3) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒦T,θc​o​n​t)∃κT<+∞,∃θT>0,∀δ∈(0,T),supt∈[0,T][∫0t|K((s+δ)∧T)−K(s))|2ds]12≤κTδθT.({\cal K}^{cont}\_{T,\theta})\;\exists\,\kappa\_{{}\_{T}}<+\infty,\;\exists\,\theta\_{{}\_{T}}>0,\;\forall\,\delta\!\in(0,T),\;\sup\_{t\in[0,T]}\left[\int\_{0}^{t}|K(\big(s+\delta)\wedge T\big)-K(s))|^{2}ds\right]^{\frac{1}{2}}\leq\kappa\_{{}\_{T}}\,\delta^{\theta\_{{}\_{T}}}. |  | (2.4) |

Assume bb and σ\sigma satisfy the following Lipschitz-linear growth assumption uniform in time

|  |  |  |  |
| --- | --- | --- | --- |
|  | (i)\displaystyle(i) | ∀t∈[0,T],∀x,y∈ℝ,|b​(t,x)−b​(t,y)|+|σ​(t,x)−σ​(t,y)|≤Cb,σ,T​|x−y|,\displaystyle\;\forall t\in[0,T],\;\forall x,y\in\mathbb{R},\;|b(t,x)-b(t,y)|+|\sigma(t,x)-\sigma(t,y)|\leq C\_{b,\sigma,T}|x-y|, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (i​i)\displaystyle(ii) | supt∈[0,T](|b​(t,0)|+|σ​(t,0)|)<+∞,\displaystyle\;\sup\_{t\in[0,T]}\left(|b(t,0)|+|\sigma(t,0)|\right)<+\infty, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (i​i​i)\displaystyle(iii) | Moreover, for some ​δ>0, for any ​p>0​ and ​T>0,\displaystyle\;\text{Moreover, for some }\delta>0,\text{ for any }p>0\text{ and }T>0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​(supt∈[0,T]|X0​ϕ​(t)|p)<+∞,𝔼​|X0​ϕ​(t′)−X0​ϕ​(t)|p⩽CT,p​(1+𝔼​[supt∈[0,T]|X0​ϕ​(t)|p])​|t′−t|δ​p.\displaystyle\qquad\mathbb{E}\left(\sup\_{t\in[0,T]}|X\_{0}\phi(t)|^{p}\right)<+\infty,\qquad\mathbb{E}|X\_{0}\phi(t^{\prime})-X\_{0}\phi(t)|^{p}\leqslant C\_{T,p}\left(1+\mathbb{E}\left[\sup\_{t\in[0,T]}|X\_{0}\phi(t)|^{p}\right]\right)|t^{\prime}-t|^{\delta p}. |  |

Under Assumption ([2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), if X0∈Lp​(ℙ)X\_{0}\!\in L^{p}(\mathbb{P}) for some p>0p>0, then Equation ([2.2](https://arxiv.org/html/2511.03474v1#S2.E2 "In 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) admits a unique pathwise continuous solution on ℝ+\mathbb{R}\_{+} starting from X0X\_{0} satisfying (among other properties),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀T>0,∃CT,p>0,‖supt∈[0,T]|Xt|‖p≤CT,p​(1+supt∈[0,T]|ϕ​(t)|​‖|X0|‖p).\forall\,T>0,\;\exists\,C\_{{}\_{T,p}}>0,\quad\big\|\sup\_{t\in[0,T]}|X\_{t}|\big\|\_{p}\leq C\_{{}\_{T,p}}\left(1+\sup\_{t\in[0,T]}|\phi(t)|\big\||X\_{0}|\big\|\_{p}\right). |  | (2.5) |

This result appears as a generalization of the classical strong existence-uniqueness result of pathwise continuous solutions established in ([JouPag22,](https://arxiv.org/html/2511.03474v1#bib.bib30) , Theorem 1.1) as an improved version of ([ZhangXi2010,](https://arxiv.org/html/2511.03474v1#bib.bib51) , Theorem 3.1 and Theorem 3.3), which holds only when the starting value X0X\_{0} has finite polynomial moments of any order (the framework is more general with a function ϕ\phi in front of the starting value).

### 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel

The Laplace transform is a valuable tool, and we provide a brief overview here, as it is particularly effective for addressing the key equation ([2.2](https://arxiv.org/html/2511.03474v1#S2.E2 "In 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).

Let us first introduce the Laplace transform of a Borel function f:ℝ+→ℝ+f:\mathbb{R}\_{+}\to\mathbb{R}\_{+} by

∀t≥0,Lf​(t)=∫0+∞e−t​u​f​(u)​𝑑u∈[0,∞].\forall\,t\geq 0,\quad L\_{f}(t)=\int\_{0}^{+\infty}e^{-tu}f(u)du\!\in[0,\infty].

This Laplace transform is non-increasing and if Lf​(t0)<+∞L\_{f}(t\_{0})<+\infty for some t0≥0t\_{0}\geq 0, then Lf​(t)→0L\_{f}(t)\to 0 as t→+∞t\to+\infty by Lebesgue’s dominated convergence theorem.
One can define the Laplace transform of a Borel function f:ℝ+→ℝf:\mathbb{R}\_{+}\to\mathbb{R} on (0,+∞)(0,+\infty) as soon as L|f|​(t)<+∞L\_{|f|}(t)<+\infty for every t>0t>0 by the above formula. The Laplace transform can be extended to ℝ+\mathbb{R}\_{+} as an ℝ\mathbb{R}-valued function if f∈ℒℝ+1​(Leb1)f\!\in{\cal L}^{1}\_{\mathbb{R}\_{+}}({\rm Leb}\_{1}).
  
Throughout this work, we will adopt the below resolvent definition put forth in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) , which offers a distinct perspective compared to the functional resolvent introduced in [gripenberg1990](https://arxiv.org/html/2511.03474v1#bib.bib4)  and also discussed or presented in works such as [abi2019affine](https://arxiv.org/html/2511.03474v1#bib.bib2) .

Let KK be a convolution kernel satisfying ([2.3](https://arxiv.org/html/2511.03474v1#S2.E3 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), ([2.4](https://arxiv.org/html/2511.03474v1#S2.E4 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ∫0tK​(u)​𝑑u>0\int\_{0}^{t}K(u)du>0 for every t>0t>0.
For every λ∈ℝ\lambda\!\in\mathbb{R}, the resolvent or Solvent core RλR\_{\lambda} associated to KK and λ\lambda is defined as the unique solution – if it exists – to the deterministic Volterra equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,Rλ​(t)+λ​∫0tK​(t−s)​Rλ​(s)​𝑑s=1.\forall\,t\geq 0,\quad R\_{\lambda}(t)+\lambda\int\_{0}^{t}K(t-s)R\_{\lambda}(s)ds=1. |  | (2.6) |

or, equivalently, written in terms of convolution,
Rλ+λ​K∗Rλ=1.R\_{\lambda}+\lambda K\*R\_{\lambda}=1.
This equation is also known as resolvent equation or renewal equation. Its solution always satisfies Rλ​(0)=1R\_{\lambda}(0)=1 and admits the formal Neumann series expansion 222Recall that K1⁣∗=KK^{1\*}=K and Kk⁣∗​(t)=∫0tK​(t−s)⋅K(k−1)⁣∗​(s)​𝑑s.K^{k\*}(t)=\int\_{0}^{t}K(t-s)\cdot K^{(k-1)\*}(s)\,ds.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rλ=∑k≥0(−1)k​λk​(1∗Kk⁣∗).R\_{\lambda}=\sum\_{k\geq 0}(-1)^{k}\lambda^{k}(\mbox{\bf 1}\*K^{k\*}). |  | (2.7) |

where, Kk⁣∗K^{k\*} denotes the kk-th convolution of KK or the k-fold ∗\*
product of k with itself, with the convention in this formula, K0⁣∗=δ0K^{0\*}=\delta\_{0} (Dirac mass at 0).

From now on we will assume that the kernel KK has a finite Laplace transform LK​(t)<+∞.L\_{K}(t)<+\infty. Note that, as mentioned in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) , if the (non-negative) kernel KK satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤K​(t)≤C​eb​t​ta−1​ for some ​a,b,C>0∈ℝ+.0\leq K(t)\leq Ce^{bt}t^{a-1}\mbox{ for some }\;a,\,\;b,\;C>0\!\in\mathbb{R}\_{+}. |  | (2.8) |

then, by induction 1∗K∗n​(t)≤Cn​eb​t​Γ​(a)nΓ​(a​n+1)​ta​n,\mbox{\bf 1}\*K^{\*n}(t)\leq C^{n}e^{bt}\frac{\Gamma(a)^{n}}{\Gamma(an+1)}t^{an}, so that for such kernels, the above series ([2.7](https://arxiv.org/html/2511.03474v1#S2.E7 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) is absolutely converging for every t>0t>0 implying that the function RλR\_{\lambda} is well-defined on (0,+∞)(0,+\infty).

Remark 1. If KK is regular enough (say continuous) the resolvent RλR\_{\lambda} is differentiable and one checks that fλ=−Rλ′f\_{\lambda}=-R^{\prime}\_{\lambda} satisfies, for every t>0t>0, −fλ​(t)+λ​(Rλ​(0)​K​(t)−K∗fλ​(t))=0-f\_{\lambda}(t)+\lambda\big(R\_{\lambda}(0)K(t)-K\*f\_{\lambda}(t)\big)=0
that is fλf\_{\lambda} is solution to the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | fλ+λ​K∗fλ=λ​K.f\_{\lambda}+\lambda K\*f\_{\lambda}=\lambda K. |  | (2.9) |

2. Taking the Laplace transform from both side of the above equality ([2.9](https://arxiv.org/html/2511.03474v1#S2.E9 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we have that :
Lfλ​(t)​(1+λ​LK​(t))=λ​LK​(t)L\_{f\_{\lambda}}(t)(1+\lambda L\_{K}(t))=\lambda L\_{K}(t), t>0t>0. Consequently, Lfλ​(t)=λ​LK​(t)1+λ​LK​(t)L\_{f\_{\lambda}}(t)=\frac{\lambda L\_{K}(t)}{1+\lambda L\_{K}(t)}
so that, for λ≥0,\lambda\geq 0, Lfλ​(t)≡0L\_{f\_{\lambda}}(t)\equiv 0 if and only if
LK​(t)≡0L\_{K}(t)\equiv 0 i.e. if and only if K=0K=0 by the injectivity of Laplace transform.

3. If limt→+∞Rλ​(t)=0\displaystyle\lim\_{t\to+\infty}R\_{\lambda}(t)=0 then, one also has that ∫0+∞fλ​(t)​𝑑t=1−Rλ​(+∞)=1\int\_{0}^{+\infty}f\_{\lambda}(t)dt=1-R\_{\lambda}(+\infty)=1.Moreover, if RλR\_{\lambda} turns out to be non-increasing, then fλf\_{\lambda} is non-negative and satisfies 0≤fλ≤λ​K0\leq f\_{\lambda}\leq\lambda K, so that fλf\_{\lambda} is a probability density.

###### Example 2.3 (Laplace transform and λ−\lambda- Resolvent associated to the Exponential-fractional Kernel).

The Laplace transform associated to a kernel KK always exists and reads, for t>0t>0
LK​(t):=∫0+∞e−t​u​K​(u)​𝑑u.L\_{K}(t):=\int\_{0}^{+\infty}e^{-tu}K(u)du.
When K is the Gamma kernel Kb,α,ρ​(t):=b​e−ρ​t​tα−1Γ​(α)⋅𝟏(0,∞)​(t)K\_{b,\alpha,\rho}(t):=be^{-\rho t}\frac{t^{\alpha-1}}{\Gamma(\alpha)}\cdot\mathbf{1}\_{(0,\infty)}(t), for b>0,α>0b>0,\alpha>0 and ρ>0\rho>0, then by
introducing v=u​(t+ρ), we havev=u(t+\rho),\textit{ we have}

|  |  |  |
| --- | --- | --- |
|  | LKb,α,ρ​(t)=∫0∞b​e−(t+ρ)​u​uα−1Γ​(α)​𝑑u=b​(t+ρ)−αΓ​(α)​∫0∞e−v​vα−1​𝑑v=b​(t+ρ)−α.L\_{K\_{b,\alpha,\rho}}(t)=\int\_{0}^{\infty}be^{-(t+\rho)u}\frac{u^{\alpha-1}}{\Gamma(\alpha)}du=\frac{b(t+\rho)^{-\alpha}}{\Gamma(\alpha)}\int\_{0}^{\infty}e^{-v}v^{\alpha-1}dv=b(t+\rho)^{-\alpha}. |  |

Moreover, one checks that these kernels also satisfy ([2.3](https://arxiv.org/html/2511.03474v1#S2.E3 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([2.4](https://arxiv.org/html/2511.03474v1#S2.E4 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) for α>1/2\alpha>1/2 (with θT=(α−12)∧1\theta\_{{}\_{T}}=(\alpha-\frac{1}{2})\wedge 1) and trivially ([2.8](https://arxiv.org/html/2511.03474v1#S2.E8 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).
For simplification, assume that b=1b=1.
It follows from the easy identity Kα,ρ∗Kα′,ρ=Kα+α′,ρK\_{\alpha,\rho}\*K\_{\alpha^{\prime},\rho}=K\_{\alpha+\alpha^{\prime},\rho} and the Neumann series expansion provided in equation ([2.7](https://arxiv.org/html/2511.03474v1#S2.E7 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that the resolvent
reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rα,ρ,λ​(t)=(1∗δ0)​(t)+∑k≥1(−1)k​λk​(1∗Kα,ρ(k∗))=𝟏ℝ+​(t)+∑k≥1(−1)k​λk​∫0te−ρ​s​sk​α−1Γ​(k​α)​𝑑s.R\_{\alpha,\rho,\lambda}(t)=(1\*\delta\_{0})(t)+\sum\_{k\geq 1}(-1)^{k}\lambda^{k}(\mbox{\bf 1}\*K\_{\alpha,\rho}^{(k\*)})=\mathbf{1}\_{\mathbb{R}\_{+}}(t)+\sum\_{k\geq 1}(-1)^{k}\lambda^{k}\int\_{0}^{t}\frac{e^{-\rho s}s^{k\alpha-1}}{\Gamma(k\alpha)}\,ds. |  | (2.10) |

Hence, if λ>0\lambda>0, we define the function fα,ρ,λ:=−Rα,ρ,λf\_{\alpha,\rho,\lambda}:=-R\_{\alpha,\rho,\lambda} on (0,+∞)(0,+\infty) by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fα,ρ,λ​(t)=−dd​t​Rα,ρ,λ​(t)=−∑k≥1(−1)k​λk​e−ρ​t​tk​α−1Γ​(k​α)=λ​e−ρ​t​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1)).f\_{\alpha,\rho,\lambda}(t)=-\frac{d}{dt}R\_{\alpha,\rho,\lambda}(t)=-\sum\_{k\geq 1}(-1)^{k}\lambda^{k}\frac{e^{-\rho t}t^{k\alpha-1}}{\Gamma(k\alpha)}=\lambda e^{-\rho t}t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\lambda^{k}\frac{t^{\alpha k}}{\Gamma(\alpha(k+1))}. |  | (2.11) |

### 2.3 Application to the Wiener-Hopf equation

###### Proposition 2.4 (Wiener-Hopf and Resolvent equations).

Let g,h:ℝ+→ℝg,h:\mathbb{R}\_{+}\to\mathbb{R} be two locally bounded Borel function, let K∈Ll​o​c1​(L​e​bℝ+)K\!\in L^{1}\_{loc}(Leb\_{\mathbb{R}\_{+}}) and let λ∈ℝ\lambda\!\in\mathbb{R}. Assume that the λ\lambda-resolvent RλR\_{\lambda} of KK is differentiable on (0,+∞)(0,+\infty) with a derivative Rλ′∈Ll​o​c1​(L​e​bℝ+)R^{\prime}\_{\lambda}\!\in L^{1}\_{loc}(Leb\_{\mathbb{R}\_{+}}), that both RλR\_{\lambda} and Rλ′R^{\prime}\_{\lambda} admit a finite Laplace transform on ℝ+\mathbb{R}\_{+} and limu→+∞e−t​u​Rλ​(u)=0\displaystyle\lim\_{u\to+\infty}e^{-tu}R\_{\lambda}(u)=0 for every t>0t>0. Then,

1. (a)(a)

   The Wiener-Hopf equation
   ∀t≥0,x​(t)=g​(t)−λ​∫0tK​(t−s)​x​(s)​𝑑s\forall\,t\geq 0,\quad x(t)=g(t)-\lambda\int\_{0}^{t}K(t-s)x(s)ds
   (also reading x=g−λ​K∗xx=g-\lambda K\*x) has a solution given by:

   ∀t≥0,x​(t)=g​(t)+∫0tRλ′​(t−s)​g​(s)​𝑑sor equivalently,x=g−fλ∗g,\forall\,t\geq 0,\quad x(t)=g(t)+\int\_{0}^{t}R^{\prime}\_{\lambda}(t-s)g(s)ds\;\quad\text{or equivalently,}\quad x=g-f\_{\lambda}\*g,

   where fλ=−Rλ′f\_{\lambda}=-R^{\prime}\_{\lambda}. This solution is uniquely defined on ℝ+\mathbb{R}\_{+} up to d​tdt-a.e.a.e. equality.
2. (b)(b)

   The integral equation
   ∀t≥0,x​(t)=h​(t)−∫0tRλ′​(t−s)​x​(s)​𝑑swhereRλ′=−fλ\forall\,t\geq 0,\quad x(t)=h(t)-\int\_{0}^{t}R^{\prime}\_{\lambda}(t-s)x(s)ds\quad\text{where}\quad R^{\prime}\_{\lambda}=-f\_{\lambda}
   (also reading x=h−Rλ′∗xx=h-R^{\prime}\_{\lambda}\*x) has a solution given by:

   ∀t≥0,x​(t)=h​(t)+λ​∫0tK​(t−s)​h​(s)​𝑑sor equivalently,x=h+λ​K∗h.\forall\,t\geq 0,\quad x(t)=h(t)+\lambda\int\_{0}^{t}K(t-s)h(s)ds\;\quad\text{or equivalently,}\quad x=h+\lambda K\*h.

   This solution is uniquely defined on ℝ+\mathbb{R}\_{+} up to d​tdt-a.e. equality.

In Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we provide a proof of this classical result for the reader’s convenience.

## 3 Investigating stationarity of a scaled stochastic Volterra Integral equation

From now we focus on the special case of a scaled stochastic Volterra equation associated to a convolutive kernel K:ℝ+→ℝ+K:\mathbb{R}\_{+}\to\mathbb{R}\_{+} satisfying ([2.3](https://arxiv.org/html/2511.03474v1#S2.E3 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([2.4](https://arxiv.org/html/2511.03474v1#S2.E4 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0ϕ(t)+∫0tK(t−s)(μ(s)−λXs)ds+∫0tK(t−s)σ(s,Xs)dWs,X0⟂⟂W.X\_{t}=X\_{0}\phi(t)+\int\_{0}^{t}K(t-s)(\mu(s)-\lambda X\_{s})ds+\int\_{0}^{t}K(t-s)\sigma(s,X\_{s})dW\_{s},\quad X\_{0}\perp\!\!\!\perp W. |  | (3.12) |

where λ>0\lambda>0, μ:𝕋+→ℝ\mu:\mathbb{T}\_{+}\to\mathbb{R} is a bounded Borel function (hence having a well-defined finite Laplace transform on (0,+∞)(0,+\infty)) and σ:𝕋+×ℝ→ℝ\sigma:\mathbb{T}\_{+}\times\mathbb{R}\to\mathbb{R} is Lipschitz continuous in xx, locally uniformly in t∈𝕋+t\!\in\mathbb{T}\_{+}. Note that the drift b​(t,x)=μ​(t)−λ​xb(t,x)=\mu(t)-\lambda x is clearly Lipschitz continuous in xx, uniformly in t∈𝕋+t\!\in\mathbb{T}\_{+}.
Then, Equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has a unique solution (Xt)t≥0(X\_{t})\_{t\geq 0} adapted to ℱtX0,W\mathcal{F}^{X\_{0},W}\_{t}, starting from X0∈Lp​(ℙ),p>0X\_{0}\in L^{p}(\mathbb{P}),p>0. This follows by applying the existence Theorem of [ZhangXi2010](https://arxiv.org/html/2511.03474v1#bib.bib51) ; [JouPag22](https://arxiv.org/html/2511.03474v1#bib.bib30) to each time interval [0,T][0,T], T∈ℕT\in\mathbb{N}, and gluing the solutions together, utilizing the uniform linear growth of the drift and σ\sigma in time.

Note that under our assumptions, if p>0p>0 and 𝔼​[|X0|p]<+∞\mathbb{E}[|X\_{0}|^{p}]<+\infty, then 𝔼​[supt∈[0,T]|Xt|p]<CT​(1+‖ϕ‖Tp​𝔼​[|X0|p])<+∞\mathbb{E}[\sup\_{t\in[0,T]}|X\_{t}|^{p}]<C\_{T}(1+\|\phi\|^{p}\_{T}\mathbb{E}[|X\_{0}|^{p}])<+\infty for every T>0T>0 (see ([JouPag22,](https://arxiv.org/html/2511.03474v1#bib.bib30) , Theorem 1.1)). Combined with |σ​(t,x)|≤CT′​(1+|x|)|\sigma(t,x)|\leq C^{\prime}\_{T}(1+|x|) for t∈[0,T]t\in[0,T], this implies 𝔼​[supt∈[0,T]|σ​(t,Xt)|p]<CT′​(1+‖ϕ‖Tp​𝔼​[|X0|p])<+∞\mathbb{E}[\sup\_{t\in[0,T]}|\sigma(t,X\_{t})|^{p}]<C^{\prime}\_{T}(1+\|\phi\|^{p}\_{T}\mathbb{E}[|X\_{0}|^{p}])<+\infty for every T>0T>0, enabling the unrestricted use of both regular and stochastic 333Interchangeability of Lebesgue and stochastic integration.  Fubini’s theorems.

Sufficient conditions for interchanging the order of ordinary integration (with respect to a finite measure) and stochastic integration (with respect to a square integrable martingale) are provided in ([Kailath\_Segall,](https://arxiv.org/html/2511.03474v1#bib.bib46) , Thm. 1), and further details can be found in ([Protter,](https://arxiv.org/html/2511.03474v1#bib.bib39) , Thm. IV.65).(see also ([Walsh1986,](https://arxiv.org/html/2511.03474v1#bib.bib48) , Theorem 2.6), ([Veraar2012,](https://arxiv.org/html/2511.03474v1#bib.bib47) , Theorem 2.6))

We will always work under the following assumption.

###### Assumption 3.1 (λ\lambda-resolvent RλR\_{\lambda} of the kernel).

Throughout the paper, we assume that the λ\lambda-resolvent RλR\_{\lambda} of the kernel KK satisfies the following for every λ>0\lambda>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒦){(i)Rλ(t) is differentiable on ℝ+,Rλ(0)=1 and limt→+∞Rλ(t)=a∈[0,1[,(i​i)fλ∈ℒloc2​(ℝ+,Leb1), where we set fλ:=−Rλ′​ for ​t>0,Lfλ​(t)≠0​d​t−a.e.,(i​i​i)ϕ∈ℒℝ+1​(Leb1), is a continuous function satisfying​limt→∞ϕ​(t)=ϕ∞, with ​a​ϕ∞<1,(i​v)μ​ is a C1-function such that ​‖μ‖sup<∞​ and ​limt→+∞μ​(t)=μ∞∈ℝ.({\cal K})\quad\left\{\begin{array}[]{ll}(i)&R\_{\lambda}(t)\text{ is }\text{differentiable on }\mathbb{R}^{+},\;R\_{\lambda}(0)=1\text{ and }\lim\_{t\to+\infty}R\_{\lambda}(t)=a\in[0,1[,\\ (ii)&f\_{\lambda}\in{\cal L}\_{\text{loc}}^{2}(\mathbb{R}\_{+},\text{Leb}\_{1}),\text{ where we set }\quad f\_{\lambda}:=-R^{\prime}\_{\lambda}\text{ for }t>0,\;L\_{f\_{\lambda}}(t)\neq 0\;dt-a.e.,\\ (iii)&\phi\in{\cal L}^{1}\_{\mathbb{R}\_{+}}(\text{Leb}\_{1}),\text{ is a continuous function satisfying}\;\lim\_{t\to\infty}\phi(t)=\phi\_{\infty},\text{ with }a\phi\_{\infty}<1,\\ (iv)&\mu\text{ is a $C^{1}$-function such that }\|\mu\|\_{\sup}<\infty\text{ and }\lim\_{t\to+\infty}\mu(t)=\mu\_{\infty}\in\mathbb{R}.\end{array}\right. |  | (3.13) |

Under assumptions 𝒦\cal K (i)(i) and (i​i)(ii), fλf\_{\lambda} is a (1−a)(1-a)-sum measure, i.e., ∫0+∞fλ​(s)​𝑑s=1−a\int\_{0}^{+\infty}f\_{\lambda}(s)\,ds=1-a.
In fact,

∫0+∞fλ​(s)​𝑑s=[1−Rλ​(s)]s=0s=+∞=−lims→+∞Rλ​(s)+Rλ​(0)=1−a\int\_{0}^{+\infty}f\_{\lambda}(s)\,ds=[1-R\_{\lambda}(s)]\_{s=0}^{s=+\infty}=-\lim\_{s\to+\infty}R\_{\lambda}(s)+R\_{\lambda}(0)=1-a

###### Lemma 3.1.

Assume that assumption (𝒦)({\cal K}) (i​i)(ii) holds, then limt→+∞∫0tfλ​(t−s)​μ​(s)​𝑑s=μ∞​(1−a)\lim\_{t\to+\infty}\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds=\mu\_{\infty}(1-a) and
limt→+∞ϕ​(t)−(fλ∗ϕ)​(t)=ϕ∞​a.\lim\_{t\to+\infty}\phi(t)-(f\_{\lambda}\*\phi)(t)=\phi\_{\infty}\,a.

For clarity and conciseness, the proof of the above Lemma is postponed to Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), where the main technical results are presented.

###### Proposition 3.2 (Wiener-Hopf transform).

Let λ>0\lambda>0 and let μ:ℝ→ℝ\mu:\mathbb{R}\to\mathbb{R} be a bounded Borel function. Assume the kernel KK satisfies the above assumptions (𝒦)({\cal K}), ([2.3](https://arxiv.org/html/2511.03474v1#S2.E3 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([2.4](https://arxiv.org/html/2511.03474v1#S2.E4 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) from Assumption [2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and its λ\lambda-resolvent RλR\_{\lambda} is well-defined
on (0,+∞)(0,+\infty). Then, the solution (Xt)t≥0(X\_{t})\_{t\geq 0} of the Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) also satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0​(ϕ​(t)−∫0tfλ​(t−s)​ϕ​(s)​𝑑s)+1λ​∫0tfλ​(t−s)​μ​(s)​𝑑s+1λ​∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws.X\_{t}=X\_{0}\Big(\phi(t)-\int\_{0}^{t}f\_{\lambda}(t-s)\phi(s)\,ds\Big)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)\,ds+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})\,dW\_{s}. |  | (3.14) |

Conversely, any process satisfying ([3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) also satisfies the original Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")). Thus, the two formulations are equivalent.

Proof.
Equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) can be interpreted pathwise as a Wiener-Hopf equation with x​(t)=Xt​(ω)x(t)=X\_{t}(\omega) and

g(t)=X0(ω)ϕ(t)+(μ∗K)t+(K∗Wσ(.,X⋅(ω)))t.g(t)=X\_{0}(\omega)\phi(t)+(\mu\*K)\_{t}+\left(K\stackrel{{\scriptstyle W}}{{\*}}\sigma(.,X\_{\cdot}(\omega))\right)\_{t}.

This leads to the following expression for XtX\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt\displaystyle X\_{t} | =g(s)+∫0tRλ′(t−s)g(s)ds=X0ϕ(t)+(μ∗K)t+(K∗Wσ(.,X.))t\displaystyle=g(s)+\int\_{0}^{t}R^{\prime}\_{\lambda}(t-s)g(s)\,ds=X\_{0}\phi(t)+(\mu\*K)\_{t}+\big(K\stackrel{{\scriptstyle W}}{{\*}}\sigma(.,X\_{.})\big)\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tRλ′(t−s)[X0ϕ(s)+(μ∗K)s+(K∗Wσ(.,X.))s]ds=X0ϕ(t)+(μ∗K)t+(K∗Wσ(.,X⋅))t\displaystyle+\int\_{0}^{t}R^{\prime}\_{\lambda}(t-s)\Big[X\_{0}\phi(s)+(\mu\*K)\_{s}+\big(K\stackrel{{\scriptstyle W}}{{\*}}\sigma(.,X\_{.})\big)\_{s}\Big]ds=X\_{0}\phi(t)+(\mu\*K)\_{t}+\left(K\stackrel{{\scriptstyle W}}{{\*}}\sigma(.,X\_{\cdot})\right)\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +X0​∫0tRλ′​(t−s)​ϕ​(s)​𝑑s+∫0tRλ′​(t−s)​(μ∗K)s​𝑑s⏟(a)+∫0tRλ′(t−s)(K∗Wσ(.,X⋅))sds⏟(b).\displaystyle\quad+X\_{0}\int\_{0}^{t}R^{\prime}\_{\lambda}(t-s)\phi(s)\,ds+\underbrace{\int\_{0}^{t}R^{\prime}\_{\lambda}(t-s)(\mu\*K)\_{s}\,ds}\_{(a)}+\underbrace{\int\_{0}^{t}R^{\prime}\_{\lambda}(t-s)\left(K\stackrel{{\scriptstyle W}}{{\*}}\sigma(.,X\_{\cdot})\right)\_{s}\,ds}\_{(b)}. |  |

Using commutativity and associativity (via regular Fubini’s theorem) of convolution, we obtain for (a)(a):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a)=−fλ∗(μ∗K)t=−((fλ∗K)∗μ)t.(a)=-f\_{\lambda}\*(\mu\*K)\_{t}=-\left((f\_{\lambda}\*K)\*\mu\right)\_{t}. |  | (3.15) |

Differentiating Equation ([2.6](https://arxiv.org/html/2511.03474v1#S2.E6 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) yields the identity −fλ∗K=1λ​fλ−K,-f\_{\lambda}\*K=\frac{1}{\lambda}f\_{\lambda}-K, which, upon substitution into ([3.15](https://arxiv.org/html/2511.03474v1#S3.E15 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), leads to the following expression in ([3.16](https://arxiv.org/html/2511.03474v1#S3.E16 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) for term (a)(a).
For term (b)(b), owing to stochastic Fubini’s theorem, equation ([2.9](https://arxiv.org/html/2511.03474v1#S2.E9 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) provides the below expression in ([3.16](https://arxiv.org/html/2511.03474v1#S3.E16 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (a)\displaystyle(a) | =1λ​(fλ∗μ)t−(K∗μ)t,(b)=1λ​(fλ∗Wσ​(⋅,X⋅))t−(K∗Wσ​(⋅,X⋅))t.\displaystyle=\frac{1}{\lambda}(f\_{\lambda}\*\mu)\_{t}-(K\*\mu)\_{t},\quad(b)=\frac{1}{\lambda}\left(f\_{\lambda}\stackrel{{\scriptstyle W}}{{\*}}\sigma(\cdot,X\_{\cdot})\right)\_{t}-\left(K\stackrel{{\scriptstyle W}}{{\*}}\sigma(\cdot,X\_{\cdot})\right)\_{t}. |  | (3.16) |

Substituting ([3.16](https://arxiv.org/html/2511.03474v1#S3.E16 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) into ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), finally yields

Xt=X0​(ϕ​(t)−(fλ∗ϕ)t)+1λ​(fλ∗μ)t+1λ​(fλ∗Wσ​(⋅,X⋅))t,X\_{t}=X\_{0}(\phi(t)-(f\_{\lambda}\*\phi)\_{t})+\frac{1}{\lambda}(f\_{\lambda}\*\mu)\_{t}+\frac{1}{\lambda}\left(f\_{\lambda}\stackrel{{\scriptstyle W}}{{\*}}\sigma(\cdot,X\_{\cdot})\right)\_{t},

The controverse is obtained by solving the corresponding Wiener-Hopf equation. We convolve both sides of Equation ([3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) with the kernel KK, using regular and stochastic Fubini’s theorem. Details are left to the reader.

###### Remark 3.3.

1. Notably, in the Markovian case, the Wiener–Hopf equation amounts to applying Itô’s lemma to the transformed process eλ​t​Xte^{\lambda t}X\_{t}. In fact, if K​(t)=𝟏K(t)=\mathbf{1} in the volterra equation, then Rλ​(t)=e−λ​tR\_{\lambda}(t)=e^{-\lambda t} and fλ​(t)=λ​e−λ​t,f\_{\lambda}(t)=\lambda e^{-\lambda t},
so that the above computation corresponds to Itô’ s Lemma applied to eλ​t​Xte^{\lambda t}X\_{t}.

2. Note that if the solution (Xt)t≥0(X\_{t})\_{t\geq 0} is stationary444In the sense that the shifted processes (Xt+u)u≥0(X\_{t+u})\_{u\geq 0} and (Xu)u≥0(X\_{u})\_{u\geq 0} have the same distribution when viewed on the canonical space 𝒞​(ℝ+,ℝ)\mathcal{C}(\mathbb{R}\_{+},\mathbb{R})., and X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}), then both the mean and variance of XtX\_{t} are constant functions of tt. Furthermore, the expectations of any function of XtX\_{t} that grows at most quadratically (see see ([2.5](https://arxiv.org/html/2511.03474v1#S2.E5 "In 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))) also remain constant. Typically, such is the case of x↦xx\mapsto x, x↦x2x\mapsto x^{2}.

### 3.1 Towards stationarity of First Moments.

Before investigating the stationary regime of the “scaled” stochastic Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we first determine under which conditions this equation has a constant first moments.

#### 3.1.1 Stationarity of the Mean

We begin by identifying the conditions under which the Volterra Equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) exhibits a constant mean; that is, when 𝔼​[Xt]=𝔼​[X0]\mathbb{E}[X\_{t}]=\mathbb{E}[X\_{0}] for all t≥0t\geq 0, assuming that X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}).
We know that:

𝔼​[(∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws)2]=∫0tfλ2​(t−s)​𝔼​[|σ​(s,Xs)|2]​𝑑s≤C​(1+‖ϕ‖T2​𝔼​[|X0|2])​∫0tfλ2​(u)​𝑑u<+∞,\mathbb{E}\left[\left(\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})dW\_{s}\right)^{2}\right]=\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\mathbb{E}[|\sigma(s,X\_{s})|^{2}]\,ds\leq C(1+\|\phi\|\_{T}^{2}\mathbb{E}[|X\_{0}|^{2}])\int\_{0}^{t}f\_{\lambda}^{2}(u)\,du<+\infty,

which implies 𝔼​[∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws]=0.\mathbb{E}\left[\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})dW\_{s}\right]=0.
Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,𝔼​[Xt]=(ϕ​(t)−(fλ∗ϕ)t)​𝔼​[X0]+1λ​(fλ∗μ)t.\forall t\geq 0,\quad\mathbb{E}[X\_{t}]=(\phi(t)-(f\_{\lambda}\*\phi)\_{t})\mathbb{E}[X\_{0}]+\frac{1}{\lambda}(f\_{\lambda}\*\mu)\_{t}. |  | (3.17) |

Thus, 𝔼​[Xt]\mathbb{E}[X\_{t}] is constant if and only if the following condition holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,𝔼​[X0]​(1−ϕ​(t)+(fλ∗ϕ)t)=1λ​∫0tfλ​(t−s)​μ​(s)​𝑑s.\forall t\geq 0,\quad\mathbb{E}[X\_{0}]\Big(1-\phi(t)+(f\_{\lambda}\*\phi)\_{t}\Big)=\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\,\mu(s)\,ds. |  | (3.18) |

###### Proposition 3.4 (Stationarity of the first moment).

Let (Xt)t≥0(X\_{t})\_{t\geq 0} be a solution to the scaled Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0∈L1​(Ω,ℱ,ℙ)X\_{0}\in L^{1}(\Omega,\mathcal{F},\mathbb{P}), with λ>0\lambda>0 and μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}. Then the Volterra process (Xt)t≥0(X\_{t})\_{t\geq 0}
has constant first moment, if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[X0]=1−a1−a​ϕ∞​μ∞λ:=x∞​and​∀t≥0,ϕ​(t)=1−λ​∫0tK​(t−s)​(μ​(s)λ​x∞−1)​𝑑s.\mathbb{E}[X\_{0}]=\frac{1-a}{1-a\phi\_{\infty}}\frac{\mu\_{\infty}}{\lambda}:=x\_{\infty}\quad\text{and}\quad\forall\,t\geq 0,\quad\phi(t)=1-\lambda\int\_{0}^{t}K(t-s)\left(\frac{\mu(s)}{\lambda x\_{\infty}}-1\right)\,ds. |  | (3.19) |

so that the equation reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0−1λ​x∞​(X0−x∞)​∫0tfλ​(t−s)​μ​(s)​𝑑s+1λ​∫0tfλ​(t−s)​ς​(s)​σ​(Xs)​𝑑Ws.\displaystyle X\_{t}=X\_{0}-\frac{1}{\lambda x\_{\infty}}\Big(X\_{0}-x\_{\infty}\Big)\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\varsigma(s)\sigma(X\_{s})dW\_{s}. |  | (3.20) |

Proof.

Case 1 𝔼​[X0]=0\mathbb{E}[X\_{0}]=0: In this case, equation ([3.18](https://arxiv.org/html/2511.03474v1#S3.E18 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) reads:
(fλ∗μ)t=0.(f\_{\lambda}\*\mu)\_{t}=0. By taking the limit in both side and owing to Lemma [3.1](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem1 "Lemma 3.1. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we have μ∞=0.\mu\_{\infty}=0. Taking the Laplace transform and owing to assumption 𝒦​(i​i)\mathcal{K}(ii), we μ​(t)=0​d​t−a.e.\mu(t)=0\;dt-a.e. and since μ\mu is C1C^{1} owing to 𝒦​(i​v)\mathcal{K}(iv), we have μ≡0\mu\equiv 0. In this case, from equation ([3.17](https://arxiv.org/html/2511.03474v1#S3.E17 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we deduce that ∀t≥0,𝔼​[Xt]=𝔼​[X0]=0.\forall t\geq 0,\quad\mathbb{E}[X\_{t}]=\mathbb{E}[X\_{0}]=0.

Case 2 𝔼​[X0]≠0\mathbb{E}[X\_{0}]\neq 0: In this case, equation ([3.18](https://arxiv.org/html/2511.03474v1#S3.E18 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) reads:
ϕ​(t)−(fλ∗ϕ)​(t)=1−1λ​(fλ∗μ𝔼​[X0])t.\phi(t)-(f\_{\lambda}\*\phi)(t)=1-\frac{1}{\lambda}(f\_{\lambda}\*\frac{\mu}{\mathbb{E}[X\_{0}]})\_{t}.
We may read the above equation as a Wiener-Hopf equation with x​(t)=ϕ​(t)x(t)=\phi(t) and h​(t)=1−1λ​(fλ∗μ𝔼​[X0])t.h(t)=1-\frac{1}{\lambda}(f\_{\lambda}\*\frac{\mu}{\mathbb{E}[X\_{0}]})\_{t}.
Then, applying the claim (b) of Proposition [2.4](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem4 "Proposition 2.4 (Wiener-Hopf and Resolvent equations). ‣ 2.3 Application to the Wiener-Hopf equation ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we get: ϕ​(t)=h​(t)+λ​(K∗h)t.\phi(t)=h(t)+\lambda(K\*h)\_{t}. That is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(t)\displaystyle\phi(t) | =1−(fλ∗μλ​𝔼​[X0])t+λ​(K∗1)t−(K∗fλ∗μ𝔼​[X0])t=1−((fλ+λ​K∗fλ)∗μλ​𝔼​[X0])t+λ​(K∗1)t\displaystyle=1-(f\_{\lambda}\*\frac{\mu}{\lambda\mathbb{E}[X\_{0}]})\_{t}+\lambda(K\*1)\_{t}-(K\*f\_{\lambda}\*\frac{\mu}{\mathbb{E}[X\_{0}]})\_{t}=1-\Big(\left(f\_{\lambda}+\lambda K\*f\_{\lambda}\right)\*\frac{\mu}{\lambda\mathbb{E}[X\_{0}]}\Big)\_{t}+\lambda(K\*1)\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =([2.9](https://arxiv.org/html/2511.03474v1#S2.E9 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))​1−(K∗μ𝔼​[X0])t+λ​(K∗1)t=1−λ​∫0tK​(t−s)​(μ​(s)λ​𝔼​[X0]−1)​𝑑s.\displaystyle\overset{\eqref{eq:flambda-eq}}{=}1-(K\*\frac{\mu}{\mathbb{E}[X\_{0}]})\_{t}+\lambda(K\*1)\_{t}=1-\lambda\int\_{0}^{t}K(t-s)\left(\frac{\mu(s)}{\lambda\mathbb{E}[X\_{0}]}-1\right)\,ds. |  |

Moreover, by taking the limit in both side of the equality ([3.18](https://arxiv.org/html/2511.03474v1#S3.E18 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we have:

𝔼[X0](1−aϕ∞):=limt→+∞𝔼[X0](1−(ϕ(t)−(fλ∗ϕ)t))=limt→+∞1λ(fλ∗μ)t=:μ∞λ(1−a)\mathbb{E}[X\_{0}](1-a\phi\_{\infty}):=\lim\_{t\to+\infty}\mathbb{E}[X\_{0}]\Big(1-(\phi(t)-(f\_{\lambda}\*\phi)\_{t})\Big)=\lim\_{t\to+\infty}\frac{1}{\lambda}(f\_{\lambda}\*\mu)\_{t}=:\frac{\mu\_{\infty}}{\lambda}(1-a)\;

owing to Lemma [3.1](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem1 "Lemma 3.1. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") so that, 𝔼​[X0]=1−a1−a​ϕ∞​μ∞λ:=x∞.\mathbb{E}[X\_{0}]=\frac{1-a}{1-a\phi\_{\infty}}\frac{\mu\_{\infty}}{\lambda}:=x\_{\infty}.
Therefore, ϕ​(t)=1−λ​∫0tK​(t−s)​(μ​(s)λ​x∞−1)​𝑑s\phi(t)=1-\lambda\int\_{0}^{t}K(t-s)\left(\frac{\mu(s)}{\lambda x\_{\infty}}-1\right)\,ds and 𝔼​[X0]=x∞.\mathbb{E}[X\_{0}]=x\_{\infty}.
Conversely, as ϕ​(t)−(fλ∗ϕ)​(t)=1−1λ​(fλ∗μ𝔼​[X0])t,\;\phi(t)-(f\_{\lambda}\*\phi)(t)=1-\frac{1}{\lambda}(f\_{\lambda}\*\frac{\mu}{\mathbb{E}[X\_{0}]})\_{t}, equation ([3.17](https://arxiv.org/html/2511.03474v1#S3.E17 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) gives:

∀t≥0,𝔼​[Xt]=x∞​(ϕ​(t)−(fλ∗ϕ)t)+1λ​(fλ∗μ)t=x∞\forall t\geq 0,\quad\mathbb{E}[X\_{t}]=x\_{\infty}\Big(\phi(t)-(f\_{\lambda}\*\phi)\_{t}\Big)+\frac{1}{\lambda}(f\_{\lambda}\*\mu)\_{t}=x\_{\infty}

Thus a necessary and sufficient condition for constant mean is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[X0]=x∞,ϕ​(t)−(fλ∗ϕ)​(t)=1−(fλ∗μ)​(t)λ​x∞​i.e.​ϕ​(t)=1−λ​∫0tK​(t−s)​(μ​(s)λ​x∞−1)​𝑑s.\displaystyle\mathbb{E}[X\_{0}]=x\_{\infty},\;\phi(t)-(f\_{\lambda}\*\phi)(t)=1-\frac{(f\_{\lambda}\*\mu)(t)}{\lambda x\_{\infty}}\;\text{i.e.}\;\phi(t)=1-\lambda\int\_{0}^{t}K(t-s)\left(\frac{\mu(s)}{\lambda x\_{\infty}}-1\right)\,ds. |  | (3.21) |

Then Equation ([3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) can be rewritten as ([3.20](https://arxiv.org/html/2511.03474v1#S3.E20 "In Proposition 3.4 (Stationarity of the first moment). ‣ 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))
We can easily check that ϕ​(0)=1\phi(0)=1. However, if
ϕ​(t)≡Cste≡1,(ϕ∞=1)\phi(t)\equiv C^{\text{ste}}\equiv 1,(\phi\_{\infty}=1), then by ([3.21](https://arxiv.org/html/2511.03474v1#S3.E21 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we have ∫0tK​(t−s)​(μ​(s)λ​x∞−1)​𝑑s≡0​∀t≥0,\int\_{0}^{t}K(t-s)\left(\frac{\mu(s)}{\lambda x\_{\infty}}-1\right)\,ds\equiv 0\;\forall t\geq 0, which reduces to the Laplace transform equation LK⋅Lμ​(⋅)λ​x∞−1≡0.L\_{K}\cdot L\_{\frac{\mu(\cdot)}{\lambda x\_{\infty}}-1}\equiv 0.
Since LK​(t)>0​∀t≥0L\_{K}(t)>0\;\forall t\geq 0 as K>0K>0, we have Lμ​(⋅)λ​x∞−1≡0L\_{\frac{\mu(\cdot)}{\lambda x\_{\infty}}-1}\equiv 0 i.e. μ​(⋅)λ​x∞−1≡0\frac{\mu(\cdot)}{\lambda x\_{\infty}}-1\equiv 0 i.e. ∀t≥0,μ​(t)=Cste=μ∞.\forall t\geq 0,\mu(t)=C^{\text{ste}}=\mu\_{\infty}.
Consequently, the mean is stationary, with the following conditions:

ϕ​(t)=1almost surely,μ​(t)=μ∞almost surely,𝔼​[X0]=μ∞λ.\phi(t)=1\quad\text{almost surely},\quad\mu(t)=\mu\_{\infty}\quad\text{almost surely},\quad\mathbb{E}[X\_{0}]=\frac{\mu\_{\infty}}{\lambda}.

Conversely, these conditions guarantee that the mean of XtX\_{t} is constant over time and we recover the case studied in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) .
In the following, we will assume the more general case: ([3.21](https://arxiv.org/html/2511.03474v1#S3.E21 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) □\square

#### 3.1.2 Towards stationarity of the variance

We deduce from the beginning of the section( [3](https://arxiv.org/html/2511.03474v1#S3 "3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that, the non-negative function defined by

t⟼Ξ2​(t):=𝔼​σ2​(t,Xt),t≥0.t\longmapsto\Xi^{2}(t):=\mathbb{E}\,\sigma^{2}(t,X\_{t}),\quad t\geq 0.

is locally bounded on ℝ+\mathbb{R}\_{+} since σ\sigma has at most linear growth in space, locally uniformly in t≥0t\geq 0.
To take advantage of this formula, we need to assume that a priori Ξ∈Ll​o​c2​(ℝ+,Leb1)\Xi\!\in L^{2}\_{loc}(\mathbb{R}\_{+},{\rm Leb}\_{1}).
First noting that by assuming constant mean as in the above section, i.e. ∀t≥0,𝔼​Xt=𝔼​X0=x∞\forall\,t\geq 0,\mathbb{E}\,X\_{t}=\mathbb{E}\,X\_{0}=x\_{\infty},
equation ([3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) reads:

Xt−x∞=(X0−x∞)​(ϕ−fλ∗ϕ)​(t)+1λ​∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws.X\_{t}-x\_{\infty}=\Big(X\_{0}-x\_{\infty}\Big)(\phi-f\_{\lambda}\*\phi)(t)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})\,dW\_{s}.

By Itô’s isomorphism and Fubini’s Theorem

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws)\displaystyle{\rm Var}\Big(\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})\,dW\_{s}\Big) | =𝔼​[∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws]2=∫0tfλ​(t−s)2​Ξ2​(s)​𝑑s=(fλ2∗Ξ2)​(t).\displaystyle=\mathbb{E}\Big[\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})\,dW\_{s}\Big]^{2}=\int\_{0}^{t}f\_{\lambda}(t-s)^{2}\Xi^{2}(s)ds=(f\_{\lambda}^{2}\*\Xi^{2})(t). |  |

Then, it follows from the above equation that: ∀t≥0,\quad\forall\,t\geq 0, by setting v0=Var​(X0)v\_{0}={\rm Var}(X\_{0}), we have:

|  |  |  |
| --- | --- | --- |
|  | Var​(Xt)=𝔼​[(Xt−x∞)2]=𝔼​[(X0−x∞)2]​(ϕ−fλ∗ϕ)2​(t)+1λ2​∫0tfλ​(t−s)2​Ξ2​(s)​𝑑s=v0​(ϕ−fλ∗ϕ)2​(t)+1λ2​(fλ2∗Ξ2)​(t){\rm Var}(X\_{t})=\mathbb{E}\Big[(X\_{t}-x\_{\infty})^{2}\Big]=\mathbb{E}\Big[(X\_{0}-x\_{\infty})^{2}\Big](\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}\int\_{0}^{t}f\_{\lambda}(t-s)^{2}\Xi^{2}(s)ds=v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*\Xi^{2})(t) |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | i.e.∀t≥0,Var​(Xt)=v0​(ϕ−fλ∗ϕ)2​(t)+1λ2​(fλ2∗Ξ2)​(t).\text{i.e.}\quad\forall\,t\geq 0,\quad{\rm Var}(X\_{t})=v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*\Xi^{2})(t). |  | (3.22) |

Examples. ⊳\rhd The case of equation ([3.20](https://arxiv.org/html/2511.03474v1#S3.E20 "In Proposition 3.4 (Stationarity of the first moment). ‣ 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) reads easily owing to (ϕ−fλ∗ϕ)​(t)=1−(fλ∗μ)tλ​𝔼​[X0]=1−(fλ∗μ)tλ​x∞(\phi-f\_{\lambda}\*\phi)(t)=1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda\mathbb{E}[X\_{0}]}=1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda x\_{\infty}}

∀t≥0,Var​(Xt)=v0​(1−(fλ∗μ)tλ​x∞)2+1λ2​(fλ2∗Ξ2)​(t).\forall\,t\geq 0,\quad{\rm Var}(X\_{t})=v\_{0}\Big(1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda x\_{\infty}}\Big)^{2}+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*\Xi^{2})(t).

Now, assume a time homogenous or autonomous volatility coefficient, i.e. ∀(t,x)∈𝕋×ℝ,σ​(t,x)=σ​(x).\forall\,(t,x)\!\in\mathbb{T}\times\mathbb{R},\;\sigma(t,x)=\sigma(x).

As discussed in Remark [3.3](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem3 "Remark 3.3. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (2), if the solution (Xt)t≥0(X\_{t})\_{t\geq 0} is stationary and X0∈L2​(ℙ)X\_{0}\!\in L^{2}(\mathbb{P}) then:

∀t≥0,𝔼​Xt=cs​t​e=x∞,Var​(Xt)=cs​t​e=v0≥0 and σ¯2​(t):=𝔼​σ2​(Xt)=cs​t​e:=σ¯2≥0.\forall\,t\geq 0,\quad\mathbb{E}\,X\_{t}=\textit{c}^{ste}=x\_{\infty},\quad{\rm Var}(X\_{t})=\textit{c}^{ste}=v\_{0}\geq 0\quad\mbox{ and }\quad\bar{\sigma}^{2}(t):=\mathbb{E}\,\sigma^{2}(X\_{t})=\textit{c}^{ste}:=\bar{\sigma}^{2}\geq 0.

so that from equation ([3.22](https://arxiv.org/html/2511.03474v1#S3.E22 "In 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) together with the fact that, here Ξ2=σ¯2\Xi^{2}=\bar{\sigma}^{2}, we have:

∀t≥0,v0=Var​(Xt)=v0​(ϕ−fλ∗ϕ)2​(t)+1λ2​(fλ2∗σ¯2)​(t)=v0​(ϕ−fλ∗ϕ)2​(t)+σ¯2λ2​∫0tfλ2​(s)​𝑑s\forall\,t\geq 0,\quad v\_{0}={\rm Var}(X\_{t})=v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*\bar{\sigma}^{2})(t)=v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{\bar{\sigma}^{2}}{\lambda^{2}}\int\_{0}^{t}f\_{\lambda}^{2}(s)ds

or, equivalently

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,v0​(1−(ϕ−fλ∗ϕ)2​(t))=σ¯2λ2​∫0tfλ2​(s)​𝑑s.\forall\,t\geq 0,\quad v\_{0}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=\frac{\bar{\sigma}^{2}}{\lambda^{2}}\int\_{0}^{t}f\_{\lambda}^{2}(s)ds. |  | (3.23) |

Consequently,

* (i)(i)

  If σ¯2=0\bar{\sigma}^{2}=0, we get v0=0v\_{0}=0 since limt→+∞(ϕ−fλ∗ϕ)​(t)=a​ϕ∞<1⇒(ϕ−fλ∗ϕ)​(t)≠1\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)(t)=a\phi\_{\infty}<1\Rightarrow(\phi-f\_{\lambda}\*\phi)(t)\neq 1 (at least for tt large enough). As a consequence, Var​(Xt)=0{\rm Var}(X\_{t})=0 for every t≥0t\geq 0. But, we know that 𝔼​Xt=𝔼​X0=x∞\mathbb{E}\,X\_{t}=\mathbb{E}\,X\_{0}=x\_{\infty}, it follows that Xt=x∞X\_{t}=x\_{\infty} ℙ\mathbb{P}-a.s.a.s..
* (i​i)(ii)

  If σ¯>0\bar{\sigma}>0, using equation ([3.21](https://arxiv.org/html/2511.03474v1#S3.E21 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and differentiating this equality implies, owing to 𝒦\cal K (i​v)(iv) and Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (2):

  κλ​x∞​(1−(fλ∗μ)tλ​x∞)​(μ​(0)​fλ​(t)+(fλ∗μ′)t)=fλ2​(t)whereκ=2​λ2​v0σ¯2.\frac{\kappa}{\lambda x\_{\infty}}\left(1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda x\_{\infty}}\right)\left(\mu(0)f\_{\lambda}(t)+(f\_{\lambda}\*\mu^{\prime})\_{t}\right)=f\_{\lambda}^{2}(t)\quad\textit{where}\quad\kappa=2\frac{\lambda^{2}v\_{0}}{\bar{\sigma}^{2}}.

  Thus the kernel KK must be the function such that its Laplace transform is given (from equation ([2.6](https://arxiv.org/html/2511.03474v1#S2.E6 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))) by LK​(t)=1λ​(1t​LRλ​(t)−1)L\_{K}(t)=\frac{1}{\lambda}\Big(\frac{1}{tL\_{R\_{\lambda}}(t)}-1\Big) where fλ:=Rλ′f\_{\lambda}:=R^{\prime}\_{\lambda} is a solution (if exists any) of the above functional equation.
  However, in the particular case ϕ≡1\phi\equiv 1 i.e. ∀t≥0,μ​(t)=μ∞,a.s.\forall t\geq 0,\;\mu(t)=\mu\_{\infty},\;\text{a.s.}, as shown in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) , the kernel K is necessary constant, in which case (Xt)t≥0(X\_{t})\_{t\geq 0} is a (Markov) Brownian diffusion process with constant mean and variance, thus true Volterra equations with non constant kernels are never stationary.

From now on, we will assume that the volatility coefficient σ​(t,x)\sigma(t,x) is time-dependent or inhomogenous defined by:

|  |  |  |
| --- | --- | --- |
|  | ∀(t,x)∈𝕋+×ℝ,σ​(t,x)=ς​(t)​σ​(x)ς​(t),σ​(x)>0.\forall\,(t,x)\!\in\mathbb{T}\_{+}\times\mathbb{R},\qquad\sigma(t,x)=\varsigma(t)\sigma(x)\quad\varsigma(t),\sigma(x)>0. |  |

where ς\varsigma is a (locally) bounded Borel function to be specified later.
We assume that the kernel KK satisfies equations ([2.3](https://arxiv.org/html/2511.03474v1#S2.E3 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([2.4](https://arxiv.org/html/2511.03474v1#S2.E4 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) of Assumption [2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and σ\sigma is Lipschitz continuous. As ς\varsigma is a (locally) bounded Borel function, the scaled Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has a unique (ℱtX0,W)t>0(\mathcal{F}^{X\_{0},W}\_{t})\_{t>0}-adapted pathwise continuous solution starting from X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) independent of W (still owing to ([ZhangXi2010,](https://arxiv.org/html/2511.03474v1#bib.bib51) , Theorem 3.3.)

Still as a consequence of Remark [3.3](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem3 "Remark 3.3. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (2), if the solution (Xt)t≥0(X\_{t})\_{t\geq 0} of the Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting by X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) is stationary, then:

∀t≥0,𝔼​Xt=cs​t​e=x∞,Var​(Xt)=cs​t​e=v0≥0​ and ​σ¯2​(t):=𝔼​σ2​(Xt)=cs​t​e:=σ¯02≥0.\forall\,t\geq 0,\;\mathbb{E}\,X\_{t}=\textit{c}^{ste}=x\_{\infty},\;{\rm Var}(X\_{t})=\textit{c}^{ste}=v\_{0}\geq 0\;\mbox{ and }\;\bar{\sigma}^{2}(t):=\mathbb{E}\,\sigma^{2}(X\_{t})=\textit{c}^{ste}:=\bar{\sigma}^{2}\_{0}\geq 0.

The theorem below shows what are the consequences of these three constraints in this settings.

###### Theorem 3.5 (Time-dependent or inhomogenous diffusion coefficient σ\sigma).

Let σ​(t,x)=ς​(t)​σ​(x)\sigma(t,x)=\varsigma(t)\sigma(x) in the equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), and assume that X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) with 𝔼​[X0]=x∞\mathbb{E}[X\_{0}]=x\_{\infty}. Suppose the following conditions hold for all t≥0t\geq 0:

𝔼​[Xt]=x∞,Var​(Xt)=v0≥0,andσ¯2​(t)=𝔼​[Xt]=σ¯02≥0.\mathbb{E}[X\_{t}]=x\_{\infty},\quad\text{Var}(X\_{t})=v\_{0}\geq 0,\quad\text{and}\quad\bar{\sigma}^{2}(t)=\mathbb{E}[X\_{t}]=\bar{\sigma}^{2}\_{0}\geq 0.

Then, a necessary condition for these relations to be satisfied is that the triplet (v0,σ¯02,ς​(t))(v\_{0},\bar{\sigma}\_{0}^{2},\varsigma(t)) satisfies the following functional equation :

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Eλ,c):∀t≥0,cλ2(1−(ϕ−fλ∗ϕ)2(t))=(fλ2∗ς2)(t)wherec=v0σ¯02and thusς=ςλ,c.\textit{($E\_{\lambda,c}$)}:\quad\forall\,t\geq 0,\quad c\lambda^{2}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=(f\_{\lambda}^{2}\*\varsigma^{2})(t)\quad\textit{where}\quad c=\frac{v\_{0}}{\bar{\sigma}\_{0}^{2}}\quad\textit{and thus}\quad\varsigma=\varsigma\_{\lambda,c}. |  | (3.24) |

Remark
With equation ([3.21](https://arxiv.org/html/2511.03474v1#S3.E21 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), (Eλ,cE\_{\lambda,c}) in ([3.24](https://arxiv.org/html/2511.03474v1#S3.E24 "In Theorem 3.5 (Time-dependent or inhomogenous diffusion coefficient 𝜎). ‣ 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) can also be re-written as follows:

(Eλ,c):∀t≥0,cλ2(1−(1−(fλ∗μ)tλ​x∞)2)=(fλ2∗ς2)(t)wherec=v0σ¯02and thusς=ςλ,c.\textit{($E\_{\lambda,c}$)}:\quad\forall\,t\geq 0,\quad c\lambda^{2}\left(1-\Big(1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda x\_{\infty}}\Big)^{2}\right)=(f\_{\lambda}^{2}\*\varsigma^{2})(t)\quad\textit{where}\quad c=\frac{v\_{0}}{\bar{\sigma}\_{0}^{2}}\quad\textit{and thus}\quad\varsigma=\varsigma\_{\lambda,c}.

Proof of Theorem [3.5](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem5 "Theorem 3.5 (Time-dependent or inhomogenous diffusion coefficient 𝜎). ‣ 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
From Equation ([3.22](https://arxiv.org/html/2511.03474v1#S3.E22 "In 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) with Ξ2=ς2​σ¯2\Xi^{2}=\varsigma^{2}\bar{\sigma}^{2} and the assumption of the theorem :

∀t≥0,v0=Var​(Xt)=v0​(ϕ−fλ∗ϕ)2​(t)+1λ2​(fλ2∗σ¯2​ς2)​(t)=v0​(ϕ−fλ∗ϕ)2​(t)+σ¯2λ2​(fλ2∗ς2)​(t)\forall\,t\geq 0,\quad v\_{0}={\rm Var}(X\_{t})=v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*\bar{\sigma}^{2}\varsigma^{2})(t)=v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{\bar{\sigma}^{2}}{\lambda^{2}}(f\_{\lambda}^{2}\*\varsigma^{2})(t)

or, equivalently

∀t≥0,v0​(1−(ϕ−fλ∗ϕ)2​(t))=σ¯2λ2​(fλ2∗ς2)​(t).\forall\,t\geq 0,\quad v\_{0}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=\frac{\bar{\sigma}^{2}}{\lambda^{2}}(f\_{\lambda}^{2}\*\varsigma^{2})(t).

### 3.2 Stabilizer and Fake Stationary Regimes

###### Definition 3.6 (Stationary of Order p≥1p\geq 1 and Fake stationary regime of type I and II (see. [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) )).

.

1. 1.

   The process (Xt)t≥0(X\_{t})\_{t\geq 0} starting from X0∈Lp​(ℙ)X\_{0}\!\in L^{p}(\mathbb{P}) for p≥1p\geq 1, exhibit a stationary regime of order p if:

   ∀t≥0,∀k∈{1,…,p},𝔼​[Xtk]=cs​t​e=𝔼​[X0k].\forall\,t\geq 0,\quad\forall\,k\in\{1,...,p\},\quad\mathbb{E}\,[X\_{t}^{k}]=\textit{c}^{ste}=\mathbb{E}\,[X\_{0}^{k}].
2. 2.

   The process (Xt)t≥0(X\_{t})\_{t\geq 0} starting from X0∈L2​(ℙ)X\_{0}\!\in L^{2}(\mathbb{P}), exhibit a fake stationary regime of type I if:

   ∀t≥0,𝔼​Xt=cs​t​e=x∞,Var​(Xt)=cs​t​e=v0≥0​ and ​σ¯2​(t):=𝔼​σ2​(Xt)=cs​t​e:=σ¯2≥0.\forall\,t\geq 0,\quad\mathbb{E}\,X\_{t}=\textit{c}^{ste}=x\_{\infty},\quad{\rm Var}(X\_{t})=\textit{c}^{ste}=v\_{0}\geq 0\;\mbox{ and }\;\bar{\sigma}^{2}(t):=\mathbb{E}\,\sigma^{2}(X\_{t})=\textit{c}^{ste}:=\bar{\sigma}^{2}\geq 0.

   This is equivalent to the definition (1) above, for p=2.
   In fact,( see proposition [3.1](https://arxiv.org/html/2511.03474v1#S3.Thmprop1 "Proposition 3.1 (Equivalence). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), there is an equivalence between the abose last two equalities, assuming the first one.
3. 3.

   The process (Xt)t≥0(X\_{t})\_{t\geq 0} starting from X0X\_{0} has a fake stationary regime of type II if (Xt)t≥0(X\_{t})\_{t\geq 0} has the same marginal distribution, i.e., Xt​=𝑑​X0X\_{t}\overset{d}{=}X\_{0} for every t≥0t\geq 0. 555The distribution of X0X\_{0} is not the invariant distribution of the equation since (Xt)t≥0(X\_{t})\_{t\geq 0} is not a stationary process.

###### Definition 3.7.

We will call the stabilizer (or corrector) of the scaled stochastic Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) a bounded Borel function ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, which is a solution(if any) to the functional equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Eλ,c):∀t≥0,cλ2(1−(ϕ−fλ∗ϕ)2(t))=(fλ2∗ς2)(t)wherec=v0σ¯02and thusς=ςλ,c.\textit{($E\_{\lambda,c}$)}:\quad\forall\,t\geq 0,\quad c\lambda^{2}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=(f\_{\lambda}^{2}\*\varsigma^{2})(t)\quad\textit{where}\quad c=\frac{v\_{0}}{\bar{\sigma}^{2}\_{0}}\quad\textit{and thus}\quad\varsigma=\varsigma\_{\lambda,c}. |  | (3.25) |

Remark
Note that ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has a solution ςλ,c\varsigma\_{\lambda,c} for some c>0c>0 if and only if it has a solution ςλ,1\varsigma\_{\lambda,1} when c=1c=1, and ςλ,c=c​ςλ,1\varsigma\_{\lambda,c}=\sqrt{c}\varsigma\_{\lambda,1}. Hence, (Eλ,cE\_{\lambda,c}) can be replaced by (Eλ,1E\_{\lambda,1}) denoted (EλE\_{\lambda}) for simplicity.

###### Assumption 3.8 (On the stabilizer).

There exists a unique positive bounded Borel solution ςλ\varsigma\_{\lambda} on ]0,+∞)]0,+\infty) of the equation (Eλ):∀t>0,λ2(1−(ϕ−fλ∗ϕ)2(t))=(fλ2∗ς2)(t)\textit{($E\_{\lambda}$)}:\quad\forall\,t>0,\quad\lambda^{2}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=(f\_{\lambda}^{2}\*\varsigma^{2})(t).

###### Lemma 3.9 (On equation (Eλ,cE\_{\lambda,c}): Laplace Transform of (Eλ,cE\_{\lambda,c}), Uniqueness and Limit of ςλ,c2\varsigma^{2}\_{\lambda,c}).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1.\displaystyle 1.\qquad | ∀t>0,t​Lfλ2​(t)​Lς2​(t)=−2​c​λ2​L(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t).\displaystyle\forall\,t>0,\quad t\,L\_{f^{2}\_{\lambda}}(t)L\_{\varsigma^{2}}(t)=-2c\lambda^{2}L\_{(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t). |  | (3.26) |

2. (ϕ−fλ∗ϕ)′​(t)=−1λ​x∞​(μ​(0)​fλ​(t)+(fλ∗μ′)t)(\phi-f\_{\lambda}\*\phi)^{\prime}(t)=-\frac{1}{\lambda x\_{\infty}}\left(\mu(0)f\_{\lambda}(t)+(f\_{\lambda}\*\mu^{\prime})\_{t}\right) so that (ϕ−fλ∗ϕ)′​(t)∼0−μ​(0)λ​x∞​fλ​(t)(\phi-f\_{\lambda}\*\phi)^{\prime}(t)\stackrel{{\scriptstyle 0}}{{\sim}}-\frac{\mu(0)}{\lambda x\_{\infty}}f\_{\lambda}(t).

3. cc being fixed, the equation (Eλ,cE\_{\lambda,c}) in ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has at most one solution
ςλ,c2\varsigma^{2}\_{\lambda,c} in Lloc1​(Leb1)L^{1}\_{\text{loc}}(\text{Leb}\_{1}).

4. For fixed cc, if ςλ,c2∈Lloc1​(Leb1)\varsigma^{2}\_{\lambda,c}\in L^{1}\_{\text{loc}}(\text{Leb}\_{1})
is the unique solution of (Eλ,cE\_{\lambda,c}) in ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))
and fλ∈L2​(ℝ+,Leb1)f\_{\lambda}\in L^{2}(\mathbb{R}\_{+},\text{Leb}\_{1}), then

limt→+∞ςλ,c2​(t)=c​λ2​(1−a2​ϕ∞2)‖fλ‖L2​(Leb1)2.\lim\_{t\to+\infty}\varsigma^{2}\_{\lambda,c}(t)=\frac{c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})}{\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}}.

###### Proposition 3.1 (Equivalence).

Let λ>0\lambda>0, let μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}, and let σ:ℝ→ℝ\sigma:\mathbb{R}\to\mathbb{R} be a Lipschitz continuous function. Let X0∈L2​(Ω,𝒜,ℙ)X\_{0}\in L^{2}(\Omega,\mathcal{A},\mathbb{P}) be such that 𝔼​[X0]=x∞\mathbb{E}[X\_{0}]=x\_{\infty} and Var​(X0)=v0≥0\text{Var}(X\_{0})=v\_{0}\geq 0. Set σ¯02=𝔼​[σ2​(X0)]>0\bar{\sigma}\_{0}^{2}=\mathbb{E}[\sigma^{2}(X\_{0})]>0 and set c=v0σ¯02∈ℝ+c=\frac{v\_{0}}{\bar{\sigma}\_{0}^{2}}\in\mathbb{R}^{+}. Assume the kernel KK satisfies ([2.3](https://arxiv.org/html/2511.03474v1#S2.E3 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), ([2.4](https://arxiv.org/html/2511.03474v1#S2.E4 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), fλ2f\_{\lambda}^{2} has a finite Laplace transform on (0,+∞)(0,+\infty), and (Eλ,c)(E\_{\lambda,c}) is in force.

Then, the unique strong solution starting from X0X\_{0} of the scaled stochastic Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), where ςλ,c\varsigma\_{\lambda,c} is a solution to ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has constant mean and satisfies the following equivalence :

* (i)

  ∀t≥0,Var​(Xt)=Var​(X0)=v0\forall t\geq 0,\,\text{Var}(X\_{t})=\text{Var}(X\_{0})=v\_{0},
* (ii)

  ∀t≥0,𝔼​[σ2​(Xt)]=𝔼​[σ2​(X0)]=σ¯02\forall t\geq 0,\,\mathbb{E}[\sigma^{2}(X\_{t})]=\mathbb{E}[\sigma^{2}(X\_{0})]=\bar{\sigma}\_{0}^{2}.

For clarity and conciseness, the proofs of Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and Proposition [3.1](https://arxiv.org/html/2511.03474v1#S3.Thmprop1 "Proposition 3.1 (Equivalence). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") are deferred to Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), where the main technical results are presented.

### 3.3 Examples of fake stationary regimes of type I and II

In this section we specify a family of scaled models where b​(t,x)=μ​(t)−λ​xb(t,x)=\mu(t)-\lambda\,x and the diffusion coefficient σ\sigma (to be specified later) satisfies the usual conditions (Lipschitz continuous) and is sufficiently regular or smooth, specifically, σ∈C3​(ℝ)\sigma\in C^{3}(\mathbb{R}).

###### Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics).

Let X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} be a one-dimensional solution of the stabilized Volterra equation ([3.20](https://arxiv.org/html/2511.03474v1#S3.E20 "In Proposition 3.4 (Stationarity of the first moment). ‣ 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from any random variable X0X\_{0} defined on
(Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), with λ>0\lambda>0, μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}, and a squared diffusion coefficient σ2∈CK,Lip2​(ℝ,ℝ)\sigma^{2}\in C^{2}\_{K,\text{Lip}}(\mathbb{R},\mathbb{R}), where ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, assumed to be the unique continuous solution to Equation ([3.24](https://arxiv.org/html/2511.03474v1#S3.E24 "In Theorem 3.5 (Time-dependent or inhomogenous diffusion coefficient 𝜎). ‣ 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))
for some c∈(0,1[σ]Lip2)c\in(0,\frac{1}{[\sigma]^{2}\_{\text{Lip}}}) (so that condition (Eλ,cE\_{\lambda,c}) is satisfied).
If X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) is such that 𝔼​[X0]=x∞, given in ([3.20](https://arxiv.org/html/2511.03474v1#S3.E20 "In Proposition 3.4 (Stationarity of the first moment). ‣ 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and​Var​(X0)=v0\mathbb{E}[X\_{0}]=x\_{\infty},\;\text{ given in\penalty 10000\ \eqref{eq:ConstMean} and}\;\mathrm{Var}(X\_{0})=v\_{0}

1. 1.

   Case σ​(x)=σ\sigma(x)=\sigma is constant.
   The solution (Xt)t≥0(X\_{t})\_{t\geq 0} has a constant mean μ∞λ\frac{\mu\_{\infty}}{\lambda} and variance v0v\_{0}.

   * —

     The process exhibits a fake stationary regime of type I i.e.

     ∀t≥0,𝔼​[Xt]=x∞,Var​(Xt)=v0=c​σ2.\forall t\geq 0,\quad\mathbb{E}[X\_{t}]=x\_{\infty},\quad\text{Var}(X\_{t})=v\_{0}=c\sigma^{2}.
   * —

     Furthermore, if X0∼ν∗:=𝒩​(x∞,v0)X\_{0}\sim\nu^{\*}:=\mathcal{N}\left(x\_{\infty},v\_{0}\right), this represents a fake stationary regime of type II, since in this case, Xt∼X0X\_{t}\sim X\_{0} for all t≥0t\geq 0. ((Xt)t≥0(X\_{t})\_{t\geq 0} is a Gaussian process with a fake stationary regime of type II. anyway.). ν∗\nu^{\*} is the 1-marginal distribution.
2. 2.

   Case where σ\sigma is not constant. Assume that the mean, variance process (vt:=𝔼​[(Xt−x∞)2])t≥0(v\_{t}:=\mathbb{E}[\left(X\_{t}-x\_{\infty}\right)^{2}])\_{t\geq 0} and expected squared diffusion process (σ¯2​(t):=𝔼​[σ2​(Xt)])t≥0(\bar{\sigma}^{2}(t):=\mathbb{E}[\sigma^{2}(X\_{t})])\_{t\geq 0} are constant, i.e.

   ∀t≥0,𝔼​[Xt]=x∞,Var​(Xt)=v0=Cste,𝔼​[σ2​(Xt)]=σ¯02=Cste.\forall t\geq 0,\quad\mathbb{E}[X\_{t}]=x\_{\infty},\quad\mathrm{Var}(X\_{t})=v\_{0}=C^{\text{ste}},\quad\mathbb{E}[\sigma^{2}(X\_{t})]=\bar{\sigma}\_{0}^{2}=C^{\text{ste}}.

   Then, a necessary and sufficient condition for this Fake Stationarity Regime of Type I to hold is that there exists a function ff not depending on tt such that:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∀u∈[0,1],∀t≥0​𝔼​[(Xt−x∞)3​∂x3σ2​(x∞+(Xt−x∞)​u)]=f​(u).\forall u\in[0,1]\,,\quad\forall t\geq 0\quad\mathbb{E}\left[(X\_{t}-x\_{\infty})^{3}\partial\_{x}^{3}\sigma^{2}(x\_{\infty}+(X\_{t}-x\_{\infty})u)\right]=f(u). |  | (3.27) |

   As soon as equation ([3.27](https://arxiv.org/html/2511.03474v1#S3.E27 "In item 2 ‣ Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) holds, the solution (Xt)t≥0(X\_{t})\_{t\geq 0} to the Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0X\_{0} has a fake stationary regime of type I in the sense i.e. for all t≥0t\geq 0,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼​[Xt]=x∞,Var​(Xt)=v0=c​(σ2​(x∞)+r∞)1−c​κ,and​𝔼​[σ2​(Xt)]=σ¯02=(σ2​(x∞)+r∞)1−c​κ.\mathbb{E}[X\_{t}]=x\_{\infty},\quad\text{Var}(X\_{t})=v\_{0}=\frac{c(\sigma^{2}(x\_{\infty})+r\_{\infty})}{1-c\kappa},\quad\text{and}\quad\mathbb{E}[\sigma^{2}(X\_{t})]=\bar{\sigma}\_{0}^{2}=\frac{(\sigma^{2}(x\_{\infty})+r\_{\infty})}{1-c\kappa}. |  | (3.28) |

   where​κ:=12​∂x2σ2​(x∞)​is the curvature of ​σ2​and​r∞:=∫01(1−u)22​f​(u)​𝑑u​provided ​κ​c≠1.\text{where}\;\kappa:=\frac{1}{2}\partial\_{x}^{2}\sigma^{2}(x\_{\infty})\;\text{is the curvature of }\sigma^{2}\;\text{and}\;r\_{\infty}:=\int\_{0}^{1}\frac{(1-u)^{2}}{2}f(u)\;du\;\text{provided }\;\kappa c\neq 1.

Moreover if limt→+∞Rλ​(t)=0\lim\_{t\to+\infty}R\_{\lambda}(t)=0 (i.e. a=0a=0) or if limt→+∞ϕ​(t)=0\lim\_{t\to+\infty}\phi(t)=0 (i.e. ϕ∞=0\phi\_{\infty}=0), as a consequence of the confluence properties in Proposition[4.4](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem4 "Proposition 4.4 (𝐿^𝑝-confluence). ‣ 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), for any starting value X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}),

𝔼​[Xt]→x∞,andVar​(Xt)→v0ast→+∞.\mathbb{E}[X\_{t}]\to x\_{\infty},\quad\text{and}\quad\text{Var}(X\_{t})\to v\_{0}\quad\text{as}\quad t\to+\infty.

Remark.
If K≡1K\equiv 1, i.e. the solution (Xt)t≥0(X\_{t})\_{t\geq 0} to ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))
is a (Markov) SDE, and if it admits an invariant distribution (see e.g. [Pages2023](https://arxiv.org/html/2511.03474v1#bib.bib37) )
νσ​(d​x)=πσ​(x)​λ1​(d​x)\nu\_{\sigma}(dx)=\pi\_{\sigma}(x)\,\lambda\_{1}(dx), then starting from
X0​=𝑑​νσX\_{0}\overset{d}{=}\nu\_{\sigma} yields a fake stationary regime of type II and,
in particular, of type I. In this case, for all t≥0t\geq 0,
equation ([3.27](https://arxiv.org/html/2511.03474v1#S3.E27 "In item 2 ‣ Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) corresponds to the expectation under the invariant
distribution, i.e. 𝔼πσ​[⋅]\mathbb{E}\_{\pi\_{\sigma}}[\cdot], and thus the function
ff does not depend on tt.

Proof.
Assume there exists at least a weak solution on the whole non-negative real line of the Stochastic Voltera equation with volatility term σ​(t,x)=ςλ,c​(t)​σ​(x)\sigma(t,x)=\varsigma\_{\lambda,c}(t)\sigma(x) starting from any X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) such that 𝔼​[X0]=x∞\mathbb{E}[X\_{0}]=x\_{\infty} and V​a​r​[X0]=v0.Var[X\_{0}]=v\_{0}.
The first claim (1) is obvious once noted that (Xt)t≥0(X\_{t})\_{t\geq 0} is a Gaussian process (and [σ]Lip=0[\sigma]\_{\rm Lip}=0).
The last claim is a straightforward consequence of the confluence property in Proposition [4.4](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem4 "Proposition 4.4 (𝐿^𝑝-confluence). ‣ 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
We know that: 𝔼​Xt=𝔼​X0−1λ​x∞​(𝔼​X0−x∞)​∫0tfλ​(t−s)​μ​(s)​𝑑s.\mathbb{E}\,X\_{t}=\mathbb{E}\,X\_{0}-\frac{1}{\lambda x\_{\infty}}\Big(\mathbb{E}\,X\_{0}-x\_{\infty}\Big)\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds.

Step 1. (Conditions for Fake stationary Regime of type I.)
Using the second-Order Taylor Expansion of σ2\sigma^{2} around x∞x\_{\infty} with Integral Remainder, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(Xt)=σ2​(x∞)+∂xσ2​(x∞)​Yt+∂x2σ2​(x∞)2​Yt2+∫01(1−u)22​Yt3​∂x3σ2​(x∞+u​Yt)​d​u.\sigma^{2}(X\_{t})=\sigma^{2}(x\_{\infty})+\partial\_{x}\sigma^{2}(x\_{\infty})Y\_{t}+\frac{\partial\_{x}^{2}\sigma^{2}(x\_{\infty})}{2}Y\_{t}^{2}+\int\_{0}^{1}\frac{(1-u)^{2}}{2}\,Y\_{t}^{3}\,\partial\_{x}^{3}\sigma^{2}\left(x\_{\infty}+uY\_{t}\right)\,du. |  | (3.29) |

where Yt:=Xt−x∞Y\_{t}:=X\_{t}-x\_{\infty} for σ2∈C3​(ℝ)\sigma^{2}\in C^{3}(\mathbb{R}), and the change of variable u→u−x∞u\to u-x\_{\infty} in the integral term.

Now, taking the expectation and invoking the standard Fubini lemma, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ¯​(t)2:=𝔼​[σ2​(Xt)]=σ2​(x∞)+κ​Var​(Xt)+rt,with ​rt=∫01(1−u)22​𝔼​[Yt3​∂x3σ2​(x∞+u​Yt)]​𝑑u.\bar{\sigma}(t)^{2}:=\mathbb{E}[\sigma^{2}(X\_{t})]=\sigma^{2}\left(x\_{\infty}\right)+\kappa\,\mathrm{Var}(X\_{t})+r\_{t},\;\text{with }\;r\_{t}=\int\_{0}^{1}\frac{(1-u)^{2}}{2}\,\mathbb{E}\left[Y\_{t}^{3}\,\partial\_{x}^{3}\sigma^{2}\left(x\_{\infty}+uY\_{t}\right)\right]\,du. |  | (3.30) |

By the equivalence property, the Fake Stationarity Regime of Type I holds whenever σ¯​(t)\bar{\sigma}(t) is constant in which case Var​(Xt){\rm Var}(X\_{t}) remains constant as well (see Proposition [3.1](https://arxiv.org/html/2511.03474v1#S3.Thmprop1 "Proposition 3.1 (Equivalence). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).
It is thus necessary and sufficient that rtr\_{t} be constant (denoted r∞r\_{\infty}) or equivalently, a necessary and sufficient condition is that 𝔼​[Yt3​∂x3σ2​(x∞+Yt​u)]\mathbb{E}\left[Y\_{t}^{3}\partial\_{x}^{3}\sigma^{2}(x\_{\infty}+Y\_{t}u)\right] is independent of tt for any fixed u∈[0,1]u\in[0,1] i.e. Equation ([3.28](https://arxiv.org/html/2511.03474v1#S3.E28 "In item 2 ‣ Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) holds.

Step 2. (Fake stationary Regime of type I.
If X0∈L1​(ℙ)X\_{0}\in L^{1}(\mathbb{P}) is such that ([3.19](https://arxiv.org/html/2511.03474v1#S3.E19 "In Proposition 3.4 (Stationarity of the first moment). ‣ 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) holds,
then from equation ([3.20](https://arxiv.org/html/2511.03474v1#S3.E20 "In Proposition 3.4 (Stationarity of the first moment). ‣ 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) we have constant mean for every t≥0t\geq 0 i.e. 𝔼​Xt=x∞\mathbb{E}\,X\_{t}=x\_{\infty}

Assume that the condition c​κ≠1c\kappa\neq 1 is satisfied and as for the variance, from equation ([3.22](https://arxiv.org/html/2511.03474v1#S3.E22 "In 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we have:

∀t≥0,Var​(Xt)=Var​(X0)​(ϕ−fλ∗ϕ)2​(t)+1λ2​fλ2∗(ς2​𝔼​σ2​(X⋅))t\forall\,t\geq 0,\quad{\rm Var}(X\_{t})={\rm Var}(X\_{0})(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}f^{2}\_{\lambda}\*\big(\varsigma^{2}\,\mathbb{E}\,\sigma^{2}(X\_{\cdot})\big)\_{t}

Which become, with equation ([3.30](https://arxiv.org/html/2511.03474v1#S3.E30 "In 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) in mind:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(Xt)=Var​(X0)​(ϕ−fλ∗ϕ)2​(t)+1λ2​(fλ2∗(ς​σ¯)2)t=Var​(X0)​(ϕ−fλ∗ϕ)2​(t)+1λ2​(fλ2∗(ς2​(σ2​(x∞)+κ​Var​(X⋅)+rt)))t.{\rm Var}(X\_{t})={\rm Var}(X\_{0})(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*(\varsigma\bar{\sigma})^{2})\_{t}={\rm Var}(X\_{0})(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{1}{\lambda^{2}}(f\_{\lambda}^{2}\*(\varsigma^{2}(\sigma^{2}(x\_{\infty})+\kappa{\rm Var}(X\_{\cdot})+r\_{t})))\_{t}. |  | (3.31) |

Now, assuming constant variance, Var​(Xt)=v0for every ​t≥0,\mathrm{Var}(X\_{t})=v\_{0}\quad\text{for every }t\geq 0, equation ([3.27](https://arxiv.org/html/2511.03474v1#S3.E27 "In item 2 ‣ Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) holds and equation [3.30](https://arxiv.org/html/2511.03474v1#S3.E30 "In 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") becomes:

σ¯(t)2:=𝔼[σ2(Xt)]=σ2(x∞)+κVar(Xt)+r∞=σ2(x∞)+κv0+r∞=:σ¯02\bar{\sigma}(t)^{2}:=\mathbb{E}[\sigma^{2}(X\_{t})]=\sigma^{2}(x\_{\infty})+\kappa{\rm Var}(X\_{t})+r\_{\infty}=\sigma^{2}(x\_{\infty})+\kappa v\_{0}+r\_{\infty}=:\bar{\sigma}\_{0}^{2}.

And then, the equation ([3.31](https://arxiv.org/html/2511.03474v1#S3.E31 "In 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) above becomes ( where in the second line, we take advantage of the
identity ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) satisfied by ς=ςλ,c\varsigma=\varsigma\_{\lambda,c} so that (Eλ,cE\_{\lambda,c}) in force),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,v0=Var​(Xt)\displaystyle\forall\,t\geq 0,\quad v\_{0}={\rm Var}(X\_{t}) | =Var​(X0)​(ϕ−fλ∗ϕ)2​(t)+σ¯02λ2​(fλ2∗ς2)​(t)\displaystyle={\rm Var}(X\_{0})(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{\bar{\sigma}\_{0}^{2}}{\lambda^{2}}(f\_{\lambda}^{2}\*\varsigma^{2})(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =v0​(ϕ−fλ∗ϕ)2​(t)+(σ2​(x∞)+κ​v0+r∞)​c​(1−(ϕ−fλ∗ϕ)2​(t))\displaystyle=v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+(\sigma^{2}(x\_{\infty})+\kappa v\_{0}+r\_{\infty})c(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)) |  |

Which also reads: v0​(1−(ϕ−fλ∗ϕ)2​(t))=c​(σ2​(x∞)+κ​v0+r∞)​(1−(ϕ−fλ∗ϕ)2​(t)),t≥0v\_{0}(1-(\phi-f\_{\lambda}\*\phi)^{2}(t))=c(\sigma^{2}(x\_{\infty})+\kappa v\_{0}+r\_{\infty})(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)),\;t\geq 0
i.e. the variance becomes v0=c​(σ2​(x∞)+r∞)1−c​κ>0v\_{0}=\frac{c\left(\sigma^{2}(x\_{\infty})+r\_{\infty}\right)}{1-c\kappa}>0
which is clearly solution to the equation.

Conversely one checks that this constant value for the variance solves the above equation. Let us prove that it is the only one.
Assume that there exist two solutions to Equation ([3.31](https://arxiv.org/html/2511.03474v1#S3.E31 "In 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from a unique initial value Var​(X0)=v0{\rm Var}(X\_{0})=v\_{0}, and let x∈𝒞​(ℝ+,ℝ)x\in{\cal C}(\mathbb{R}\_{+},\mathbb{R}) represent the discrepancy over time between those solutions. By the linearity of Equation ([3.31](https://arxiv.org/html/2511.03474v1#S3.E31 "In 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), it suffices to show that the equation in x∈𝒞​(ℝ+,ℝ)x\!\in{\cal C}(\mathbb{R}\_{+},\mathbb{R})

|  |  |  |
| --- | --- | --- |
|  | x(t)=κλ2(fλ2∗(ς2.x))t,x(0)=0x(t)=\frac{\kappa}{\lambda^{2}}\big(f^{2}\_{\lambda}\*(\varsigma^{2}.\,x)\big)\_{t},\quad x(0)=0 |  |

only has the null function as solution. If xx solves the above equation, then

|  |  |  |
| --- | --- | --- |
|  | |x​(t)|≤κλ2​(fλ2∗ς2)t​sup0≤s≤t|x​(s)|=κ​c​|1−(ϕ−fλ∗ϕ)2​(t)|​sup0≤s≤t|x​(s)|≤c​κ​sup0≤s≤t|x​(s)|.|x(t)|\leq\frac{\kappa}{\lambda^{2}}(f^{2}\_{\lambda}\*\varsigma^{2})\_{t}\sup\_{0\leq s\leq t}|x(s)|\,=\kappa c|1-(\phi-f\_{\lambda}\*\phi)^{2}(t)|\sup\_{0\leq s\leq t}|x(s)|\,\leq c\kappa\sup\_{0\leq s\leq t}|x(s)|. |  |

where the last inequality comes from 𝒦​(i​i​i)\mathcal{K}(iii).
If x≡/ 0x\equiv\!\!\!\!\!/\,0, there exist ε>0\varepsilon>0 such that τε=inf{t:|x​(t)|>ε}<+∞\tau\_{\varepsilon}=\inf\{t:|x(t)|>\varepsilon\}<+\infty. By continuity of xx it is clear that τε>0\tau\_{\varepsilon}>0 and |x​(τε)|=sup0⁣:⁣≤s⁣≤t|x​(s)|=ε|x(\tau\_{\varepsilon})|=\sup\_{0:\leq s\leq t}|x(s)|=\varepsilon which is impossible since κ​c≠1\kappa c\neq 1. Consequently x≡0x\equiv 0.
We also have:

σ¯02=σ2​(x∞)+κ​v0+r∞=σ2​(x∞)+κ​c​(σ2​(x∞)+r∞)1−c​κ+r∞=σ2​(x∞)+r∞1−c​κ.\bar{\sigma}\_{0}^{2}=\sigma^{2}(x\_{\infty})+\kappa v\_{0}+r\_{\infty}=\sigma^{2}(x\_{\infty})+\kappa\frac{c\left(\sigma^{2}(x\_{\infty})+r\_{\infty}\right)}{1-c\kappa}+r\_{\infty}=\frac{\sigma^{2}(x\_{\infty})+r\_{\infty}}{1-c\kappa}.

Hence (Xt)t≥0(X\_{t})\_{t\geq 0} is a fake stationary regime of type I with the above mean and variance. □\square

###### Example 3.10 (Polynomial of degree 2).

Consider as in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36)  a squared trinomial diffusion coefficient:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(x)=κ0+κ1​x+κ2​x2 with κi≥0,i=0,2,κ12≤4​κ2​κ0.\sigma(x)=\sqrt{\kappa\_{0}+\kappa\_{1}\,x+\kappa\_{2}\,x^{2}}\quad\mbox{ with }\quad\kappa\_{i}\geq 0,\;i=0,2,\;\kappa^{2}\_{1}\leq 4\kappa\_{2}\kappa\_{0}. |  | (3.32) |

∙\bullet The above vol-vol term covers the rough Heston dynamics introduced in [el2019characteristic](https://arxiv.org/html/2511.03474v1#bib.bib17)  (the volatility process Vt=XtV\_{t}=X\_{t} has the vol-vol term as in equation ([3.32](https://arxiv.org/html/2511.03474v1#S3.E32 "In Example 3.10 (Polynomial of degree 2). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) with κ0=κ2=a=0\kappa\_{0}=\kappa\_{2}=a=0, while the volatility of the traded asset is driven by a different Brownian motion ).

∙\bullet This type of vol-vol term also appears in the quadratic rough volatility dynamic introduced in [GaJuRo2020](https://arxiv.org/html/2511.03474v1#bib.bib20)  (Vt=σ2​(Xt)V\_{t}=\sigma^{2}(X\_{t})). In that model, the asset and its volatility are driven by the same Brownian motion, aiming to jointly calibrate the the S&P 500 and VIX smile, accounting for the so-called Zumbach effect, which links the evolution of the asset (here, an index) with its volatility.

In the next proposition, we assume that when κ2=0\kappa\_{2}=0, the associated Volterra Equation has at least a weak solution (see [EGnabeyeuR2025](https://arxiv.org/html/2511.03474v1#bib.bib22) ).

###### Proposition 3.11.

Under the same assumptions as Proposition [3.2](https://arxiv.org/html/2511.03474v1#S3.Thmprop2 "Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), We have the following claims:

1. 1.

   If the diffusion coefficient σ\sigma is degenerated in the sense that σ​(x∞)=0\sigma(x\_{\infty})=0, (in particular σ¯02=0\bar{\sigma}\_{0}^{2}=0 and v0=0v\_{0}=0) then the solution Xt=x∞X\_{t}=x\_{\infty} ℙ\mathbb{P}-a.s.a.s. represents a fake stationary regime (of type I).
2. 2.

   If σ2\sigma^{2} is not constant and not degenerated given by ([3.32](https://arxiv.org/html/2511.03474v1#S3.E32 "In Example 3.10 (Polynomial of degree 2). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) i.e. σ2​(x)∈Pol2​(ℝ)\sigma^{2}(x)\in\mathrm{Pol}\_{2}(\mathbb{R}), the solution (Xt)t≥0(X\_{t})\_{t\geq 0} to the Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has a fake stationary regime of type I, in the sense that

   ∀t≥0,𝔼​[Xt]=x∞,Var​(Xt)=v0=c​σ2​(x∞)1−c​κ2,and​𝔼​[σ2​(Xt)]=σ¯02=σ2​(x∞)1−c​κ2.\forall\,t\geq 0,\quad\mathbb{E}[X\_{t}]=x\_{\infty},\;\text{Var}(X\_{t})=v\_{0}=\frac{c\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}},\;\text{and}\;\;\mathbb{E}[\sigma^{2}(X\_{t})]=\bar{\sigma}\_{0}^{2}=\frac{\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}.

   Moreover if a=0a=0 of if ϕ∞=0\phi\_{\infty}=0, for any starting value X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}),

   𝔼​[Xt]→x∞,andVar​(Xt)→c​σ2​(x∞)1−c​κ2ast→+∞.\mathbb{E}[X\_{t}]\to x\_{\infty},\quad\text{and}\quad\text{Var}(X\_{t})\to\frac{c\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}\quad\text{as}\quad t\to+\infty.

Proof. (Applicability of equation ([3.27](https://arxiv.org/html/2511.03474v1#S3.E27 "In item 2 ‣ Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))).

1. 1.

   First, in the degenerate setting σ​(x∞)=0\sigma(x\_{\infty})=0, one has σ¯02=𝔼​[σ2​(X0)]=0\bar{\sigma}\_{0}^{2}=\mathbb{E}[\sigma^{2}(X\_{0})]=0, we get v0=0v\_{0}=0 owing to equation ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) since limt→+∞(ϕ−fλ∗ϕ)​(t)=a​ϕ∞<1⇒ϕ​(t)−(fλ∗ϕ)​(t)≠1\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)(t)=a\phi\_{\infty}<1\Rightarrow\phi(t)-(f\_{\lambda}\*\phi)(t)\neq 1 (at least for tt large enough). As a consequence, Var​(Xt)=0{\rm Var}(X\_{t})=0 for every t≥0t\geq 0. But, we know that 𝔼​Xt=𝔼​X0=x∞\mathbb{E}\,X\_{t}=\mathbb{E}\,X\_{0}=x\_{\infty}, it follows that Xt=x∞X\_{t}=x\_{\infty} ℙ\mathbb{P}-a.s.a.s. and ∀t≥0,ℒ​(Yt)​(d​y)=δ0​(d​y)\forall t\geq 0,\quad\mathcal{L}(Y\_{t})(dy)=\delta\_{0}(dy) so that

   ∀t≥0,𝔼​[Yt3​∂x3σ2​(x∞+u​Yt)]=∫ℝy3​∂x3σ2​(x∞+u​y)​ℒ​(Yt)​(d​y)=0​and​r∞=0.\forall t\geq 0,\quad\mathbb{E}\left[Y\_{t}^{3}\,\partial\_{x}^{3}\sigma^{2}\left(x\_{\infty}+uY\_{t}\right)\right]=\int\_{\mathbb{R}}y^{3}\,\partial\_{x}^{3}\sigma^{2}\left(x\_{\infty}+uy\right)\,\mathcal{L}(Y\_{t})(dy)=0\;\text{and}\;r\_{\infty}=0.
2. 2.

   Secondly, if ∂x3σ2​(v)=0,∀v∈ℝ\partial\_{x}^{3}\sigma^{2}(v)=0,\;\forall v\in\mathbb{R}, then the integral reminder in ([3.29](https://arxiv.org/html/2511.03474v1#S3.E29 "In 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) necessarily vanishes.
   This corresponds to the *trinomial setting*, which has already been extensively studied in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36)  and in which case if κ2>0\kappa\_{2}>0, [σ]Lip=κ2[\sigma]\_{\rm Lip}=\sqrt{\kappa\_{2}}, the curvature κ=κ2\kappa=\kappa\_{2} and r∞=0r\_{\infty}=0 (since f≡0f\equiv 0 in ([3.27](https://arxiv.org/html/2511.03474v1#S3.E27 "In item 2 ‣ Proposition 3.2 (Fake stationary regimes (types I and II) and asymptotics). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))). □\Box

Practitioner’s corner: 1. The constraint c∈(0,1κ)c\in\left(0,\frac{1}{\kappa}\right) implies that we treat cc as a free parameter, from which we can deduce v0v\_{0} and σ¯02\bar{\sigma}\_{0}^{2}. 2. The presence of the stabilizer ςλ,c\varsigma\_{\lambda,c} allows a better control of the behaviour of the equation since it induces an L2L^{2}-confluence and a stability of first two moments if needed.
3. Note that [σ]Lip2=κ2=κ[\sigma]^{2}\_{\rm Lip}=\kappa\_{2}=\kappa so that, in practice, if we rather fix the value of v0v\_{0}, then c=v0σ2​(x∞)+v0​κc=\frac{v\_{0}}{\sigma^{2}(x\_{\infty})+v\_{0}\kappa} so that, σ\sigma being κ\sqrt{\kappa}-Lipschitz continuous, one has c​κ=v0​κσ2​(x∞)+v0​κ<1c\kappa=\frac{v\_{0}\kappa}{\sigma^{2}(x\_{\infty})+v\_{0}\kappa}<1 provided σ2​(x∞)>0\sigma^{2}(x\_{\infty})>0 which ensures the L2L^{2}-confluence of the paths of the solution (Proposition [4.4](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem4 "Proposition 4.4 (𝐿^𝑝-confluence). ‣ 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") further on).

## 4 Towards Long run behaviour: asymptotics and confluence

###### Remark 4.1.

Let μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}, by assumption ([2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) (i), one has for every x∈ℝx\in\mathbb{R},

σ2​(x)≤(σ​(x∞)+[σ]Lip​|x−x∞|)2≤κ0+κ2​|x−x∞|2\sigma^{2}(x)\leq\Big(\sigma(x\_{\infty})+[\sigma]\_{\text{Lip}}|x-x\_{\infty}|\Big)^{2}\leq\kappa\_{0}+\kappa\_{2}|x-x\_{\infty}|^{2}

where k0=k0​(ϵ):=(1+ϵ)​|σ​(x∞)|2k\_{0}=k\_{0}(\epsilon):=(1+\epsilon)|\sigma(x\_{\infty})|^{2} and k2=k2​(ϵ):=(1+1ϵ)​[σ]Lip2k\_{2}=k\_{2}(\epsilon):=(1+\frac{1}{\epsilon})[\sigma]^{2}\_{\text{Lip}}, owing to Young’s inequality
(a+b)2≤(1+ϵ)​a2+(1+1ϵ)​b2(a+b)^{2}\leq(1+\epsilon)a^{2}+(1+\frac{1}{\epsilon})b^{2}. Therefore, we can always assume that σ\sigma is sublinear i.e.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (SLσ):∃k0=k0(ϵ)∈ℝ+,k2=k2(ϵ)∈ℝ+such that∀x∈ℝ,|σ(x)|2≤κ0+κ2|x−x∞|2.(SL\_{\sigma}):\exists k\_{0}=k\_{0}(\epsilon)\in\mathbb{R}\_{+},k\_{2}=k\_{2}(\epsilon)\in\mathbb{R}\_{+}\quad\textit{such that}\quad\forall x\in\mathbb{R},|\sigma(x)|^{2}\leq\kappa\_{0}+\kappa\_{2}|x-x\_{\infty}|^{2}. |  | (4.33) |

### 4.1 Moments control.

###### Lemma 4.2 (Best constant in a BDG inequality (see Remark 2 in [carlen1991lp](https://arxiv.org/html/2511.03474v1#bib.bib11) )).

Let MM be a continuous local martingale null at t=0t=0. Then, for every p≥1p\geq 1,

1p​‖Mt‖p≤2​‖⟨M⟩t1/2‖p.\frac{1}{\sqrt{p}}\|M\_{t}\|\_{p}\leq 2\|\langle M\rangle\_{t}^{1/2}\|\_{p}.

###### Proposition 4.3 (Moment control).

Assume ([2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) (ii) and 𝒦\cal K (i​i)(ii) hold. Let σ​(t,x):=ς​(t)​σ​(x)\sigma(t,x):=\varsigma(t)\sigma(x) where ς=ςλ,c\varsigma=\varsigma\_{\lambda,c} is a non-negative, continuous and bounded solution to ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) for some fixed λ,c>0\lambda,c>0 (i.e.(EλE\_{\lambda}) is in force).
Let (Xt)t≥0(X\_{t})\_{t\geq 0} be the solutions to the Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from any random variable X0X\_{0}.

(a)(a) First two moments. Assume X0∈L2​(ℙ)X\_{0}\!\in L^{2}(\mathbb{P}) and c∈(0,1[σ]Lip2)c\!\in\big(0,\frac{1}{[\sigma]^{2}\_{\text{Lip}}}\big). Then, one has:

|  |  |  |
| --- | --- | --- |
|  | |𝔼​(Xt)−x∞|≤|ϕ​(t)−(fλ∗ϕ)​(t)|​|𝔼​(X0)−x∞|=|1−(fλ∗μλ​x∞)t|​|𝔼​(X0)−x∞|,t≥0\Big|\mathbb{E}\,\big(X\_{t}\big)-x\_{\infty}\Big|\leq|\phi(t)-(f\_{\lambda}\*\phi)(t)|\Big|\mathbb{E}\,\big(X\_{0}\big)-x\_{\infty}\Big|=\Big|1-(f\_{\lambda}\*\frac{\mu}{\lambda x\_{\infty}})\_{t}\Big|\Big|\mathbb{E}\,\big(X\_{0}\big)-x\_{\infty}\Big|,\;\;t\geq 0 |  |

|  |  |  |
| --- | --- | --- |
|  | supt≥0‖|Xt−x∞|‖2≤[c1−[σ]Lip​c​|σ​(x∞)|]∨‖|X0−x∞|‖2<+∞.\sup\_{t\geq 0}\Big\||X\_{t}-x\_{\infty}|\Big\|\_{2}\leq\left[\frac{\sqrt{c}}{1-[\sigma]\_{\text{Lip}}\sqrt{c}}|\sigma(x\_{\infty})|\right]\vee\Big\||X\_{0}-x\_{\infty}|\Big\|\_{2}<+\infty. |  |

(b)(b) LpL^{p}-moments. Let p∈(2,+∞)p\!\in(2,+\infty). If X0∈Lp​(ℙ)X\_{0}\!\in L^{p}(\mathbb{P}) and cc is such that ρp:=4​c​p​[σ]Lip2<1\rho\_{p}:=4c\,p\,[\sigma]^{2}\_{\text{Lip}}<1, then

|  |  |  |
| --- | --- | --- |
|  | supt≥0‖|Xt−x∞|‖p≤infϵ∈(0,1ρp−1)[2​p​c​(1+ϵ)1−2​[σ]Lip​p​c​(1+ϵ)​|σ​(x∞)|2]∨[(1+1/ϵ)12​‖|X0−x∞|‖p]<+∞\sup\_{t\geq 0}\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p}\leq\inf\_{\epsilon\in(0,\frac{1}{\rho\_{p}}-1)}\left[\frac{2\sqrt{pc(1+\epsilon)}}{1-2[\sigma]\_{\text{Lip}}\sqrt{pc(1+\epsilon)}}\big|\sigma(x\_{\infty})\big|^{2}\right]\vee\left[(1+1/\epsilon)^{\frac{1}{2}}\Big\||X\_{0}-x\_{\infty}|\Big\|\_{p}\right]<+\infty |  |

The proof is postponed to Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"). It relies on techniques similar to those in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) , which extend the methods developed for the Markovian framework, as discussed extensively in ([pages2018numerical,](https://arxiv.org/html/2511.03474v1#bib.bib35) , Chapter 7).

### 4.2 LpL^{p}-Confluence or Contraction Properties

Fix p>0p>0. Let (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X^{\prime}\_{t})\_{t\geq 0} be two solutions of the Volterra stochastic equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) with initial conditions X0,X0′∈Lp​(ℙ)X\_{0},X^{\prime}\_{0}\in L^{p}(\mathbb{P}). According to assumption [2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (i), ∃κ>0\exists\;\kappa>0 such that for every t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|σ​(Xs)−σ​(Xs′)|2‖p2≤κ​‖|Xs−Xs′|‖p2.\Big\||\sigma(X\_{s})-\sigma(X^{\prime}\_{s})|^{2}\Big\|\_{\frac{p}{2}}\leq\kappa\Big\||X\_{s}-X^{\prime}\_{s}|\Big\|\_{p}^{2}. |  | (4.34) |

###### Proposition 4.4 (LpL^{p}-confluence).

Assume assumption ([2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) (ii). Assume fλ∈L2​(ℝ+,Leb1)f\_{\lambda}\!\in L^{2}(\mathbb{R}\_{+},\text{Leb}\_{1}), σ​(t,x):=ς​(t)​σ​(x)\sigma(t,x):=\varsigma(t)\sigma(x) where ς=ςλ,c\varsigma=\varsigma\_{\lambda,c} is a non-negative, continuous and bounded solution to ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) for some fixed λ,c>0\lambda,c>0 (i.e. assumption [3.8](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem8 "Assumption 3.8 (On the stabilizer). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") is in force) and σ:ℝ→ℝ\sigma:\mathbb{R}\to\mathbb{R} is a Lipschitz continuous function.
Let p>0p>0, for X0,X0′∈Lp​(ℙ)X\_{0},X^{\prime}\_{0}\!\in L^{p}({\mathbb{P}}), we consider the solutions to Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) denoted (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X^{\prime}\_{t})\_{t\geq 0} starting from X0X\_{0} and X0′X^{\prime}\_{0} respectively. Let c∈(0,1κ)c\!\in\big(0,\frac{1}{\kappa}\big), where κ\kappa is defined in [4.34](https://arxiv.org/html/2511.03474v1#S4.E34 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), set ρp:=c​(CpBDG)2​κ.\rho\_{p}:=c\,(C\_{p}^{\mathrm{BDG}})^{2}\,\kappa. and assume that ρp<1−a2​ϕ∞2\rho\_{p}<1-a^{2}\phi\_{\infty}^{2}.
Then, one has:

* (a)

  There exists a continuous non-negative function φ∞,pλ,c,K,ϕ=:φ∞,p:ℝ+→[0,1(1−ρp)2]\varphi\_{\infty,p}^{\lambda,c,K,\phi}=:\varphi\_{\infty,p}:\mathbb{R}^{+}\to[0,\frac{1}{(1-\sqrt{\rho\_{p}})^{2}}], such that φ∞​(0)=11−ρp\varphi\_{\infty}(0)=\frac{1}{1-\rho\_{p}}, 0≤limt→∞φ∞,p​(t)≤a2​ϕ∞2(1−ρp​1−a2​ϕ∞2)20\leq\lim\_{t\to\infty}\varphi\_{\infty,p}(t)\leq\frac{a^{2}\phi\_{\infty}^{2}}{\big(1-\sqrt{\rho\_{p}}\sqrt{1-a^{2}\phi\_{\infty}^{2}}\big)^{2}}, only depending on λ,c,ϕ\lambda,c,\phi, and the kernel KK, such that :

  ∀t≥0,𝔼​(|Xt−Xt′|p)≤φ∞,p​(t)​𝔼​(|X0−X0′|p).\forall t\geq 0,\quad\mathbb{E}\,\Big(\Big|X\_{t}-X^{\prime}\_{t}\Big|^{p}\Big)\leq\varphi\_{\infty,p}(t)\mathbb{E}\,\Big(\Big|X\_{0}-X^{\prime}\_{0}\Big|^{p}\Big).
* (b)

  This result can be written using the pp-Wasserstein distance between marginals of XX and X′X^{\prime}:

  |  |  |  |
  | --- | --- | --- |
  |  | ∀t≥0,Wp​([Xt],[Xt′])≤φ∞,p​(t)1/2​Wp​([X0],[X0′]).\forall t\geq 0,\quad W\_{p}([X\_{t}],[X^{\prime}\_{t}])\leq\varphi\_{\infty,p}(t)^{1/2}\,W\_{p}([X\_{0}],[X^{\prime}\_{0}]). |  |
* (c)

  In particular, whenever a=0a=0 or ϕ∞=0\phi\_{\infty}=0, the limit yields φ∞,p​(t)→0\varphi\_{\infty,p}(t)\to 0 and thus the process is contracting in WpW\_{p} as t→∞t\to\infty i.e more generally finite-dimensional WpW\_{p}-convergence of marginals.

Proof.
By a Banach fixed point argument on the complete space (Cb([0,∞),ℝ),∥⋅∥∞).(C\_{b}([0,\infty),\mathbb{R}),\|\cdot\|\_{\infty}).
  
Fix p>0p>0. Let (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X^{\prime}\_{t})\_{t\geq 0} be two solutions of the same SVIE with initial conditions X0,X0′∈Lp​(ℙ)X\_{0},X^{\prime}\_{0}\in L^{p}(\mathbb{P}). Set Δt=Xt−Xt′∈Lp​(ℙ)\Delta\_{t}=X\_{t}-X^{\prime}\_{t}\in L^{p}(\mathbb{P}) for every t≥0t\geq 0. one writes owing to equation [3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt−Xt′\displaystyle X\_{t}-X^{\prime}\_{t} | =(ϕ​(t)−(fλ∗ϕ)​(t))​(X0−X0′)+1λ​∫0tfλ​(t−s)​ς​(s)​(σ​(Xs)−σ​(Xs′))​𝑑Ws\displaystyle=\big(\phi(t)-(f\_{\lambda}\*\phi)(t)\big)\big(X\_{0}-X^{\prime}\_{0}\big)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\varsigma(s)\Big(\sigma(X\_{s})-\sigma(X^{\prime}\_{s})\Big)dW\_{s} |  |

Let δ¯t=‖|Δt|‖p\bar{\delta}\_{t}=\Big\||\Delta\_{t}|\Big\|\_{p} for convenience. Under our assumptions, t↦δ¯tt\mapsto\bar{\delta}\_{t} is continuous (see [JouPag22](https://arxiv.org/html/2511.03474v1#bib.bib30)  ).
Let CpBDG>0C\_{p}^{\mathrm{BDG}}>0 denote a BDG constant in LpL^{p}. Set ρp:=c​(CpBDG)2​κ.\rho\_{p}:=c\,(C\_{p}^{\mathrm{BDG}})^{2}\,\kappa.
Owing to the triangle inequality and applying the BDG inequality to the (a priori) local martingale Mu=∫0ufλ​(t−s)​ς​(s)​σ​(Xs)​𝑑WsM\_{u}=\int\_{0}^{u}f\_{\lambda}(t-s)\varsigma(s)\sigma(X\_{s})dW\_{s}, 0≤s≤t0\leq s\leq t, (see ([RevuzYor,](https://arxiv.org/html/2511.03474v1#bib.bib41) , Proposition 4.3)) follow by the generalized Minkowski inequality, we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|Xt−Xt′|‖p\displaystyle\Big\||X\_{t}-X^{\prime}\_{t}|\Big\|\_{p} | ≤‖|X0−X0′|‖p​|ϕ​(t)−(fλ∗ϕ)​(t)​|+CpB​D​Gλ‖​(fλ2∗d​tς2​(⋅)​|σ​(Xs)−σ​(Xs′)|2)t‖p212\displaystyle\leq\Big\||X\_{0}-X^{\prime}\_{0}|\Big\|\_{p}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|+\frac{C\_{p}^{BDG}}{\lambda}\Big\|\left(f\_{\lambda}^{2}\stackrel{{\scriptstyle dt}}{{\*}}\varsigma^{2}(\cdot)|\sigma(X\_{s})-\sigma(X^{\prime}\_{s})|^{2}\right)\_{t}\Big\|\_{\frac{p}{2}}^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖|X0−X0′|‖p​|ϕ​(t)−(fλ∗ϕ)​(t)|+CpB​D​Gλ​(∫0tfλ2​(t−s)​ς2​(s)​‖|σ​(Xs)−σ​(Xs′)|2‖p2)12\displaystyle\leq\Big\||X\_{0}-X^{\prime}\_{0}|\Big\|\_{p}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|+\frac{C\_{p}^{BDG}}{\lambda}\Big(\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\big\||\sigma(X\_{s})-\sigma(X^{\prime}\_{s})|^{2}\big\|\_{\frac{p}{2}}\Big)^{\frac{1}{2}} |  |

Fix ϵ>0\epsilon>0, using the elementary inequality (a+b)2≤(1+1/ϵ)​a2+(1+ϵ)​b2(a+b)^{2}\leq(1+1/\epsilon)a^{2}+(1+\epsilon)b^{2} for ϵ∈(0,1/ρp−1)\epsilon\!\in(0,1/\rho\_{p}-1) i.e. β:=ρp​(1+ε)< 1\beta:=\rho\_{p}(1+\varepsilon)\;<\;1, it follows owing to equation ([4.34](https://arxiv.org/html/2511.03474v1#S4.E34 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|Xt−Xt′|‖p2\displaystyle\Big\||X\_{t}-X^{\prime}\_{t}|\Big\|\_{p}^{2} | ≤‖|X0−X0′|‖p2​|ϕ​(t)−(fλ∗ϕ)​(t)|2​(1+1/ϵ)+ρpc​λ2​(1+ϵ)​∫0tfλ2​(t−s)​ς2​(s)​‖|Xs−Xs′|2‖p​𝑑s\displaystyle\leq\Big\||X\_{0}-X^{\prime}\_{0}|\Big\|\_{p}^{2}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|^{2}(1+1/\epsilon)+\frac{\rho\_{p}}{c\lambda^{2}}(1+\epsilon)\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\Big\||X\_{s}-X^{\prime}\_{s}|^{2}\Big\|\_{p}ds |  |

which entails:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|Δt|‖p2≤‖|Δ0|‖p2​|ϕ​(t)−(fλ∗ϕ)​(t)|2​(1+1ϵ)+(1+ϵ)​ρpc​λ2​∫0tfλ2​(t−s)​ς2​(s)​‖|Δs|‖p2​𝑑s.\Big\||\Delta\_{t}|\Big\|\_{p}^{2}\leq\Big\||\Delta\_{0}|\Big\|\_{p}^{2}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|^{2}\left(1+\frac{1}{\epsilon}\right)+\left(1+\epsilon\right)\frac{\rho\_{p}}{c\lambda^{2}}\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\Big\||\Delta\_{s}|\Big\|\_{p}^{2}\,ds. |  | (4.35) |

i.e. we obtain, for all t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ¯t2≤δ¯02​|ϕ​(t)−(fλ∗ϕ)​(t)|2​(1+1ε)+ρp​(1+ε)​1λ2​c​∫0tfλ2​(t−s)​ς2​(s)​δ¯s2​𝑑s.\bar{\delta}\_{t}^{2}\leq\bar{\delta}\_{0}^{2}\,\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|^{2}\Big(1+\frac{1}{\varepsilon}\Big)+\rho\_{p}(1+\varepsilon)\frac{1}{\lambda^{2}c}\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\,\bar{\delta}\_{s}^{2}\,ds. |  | (4.36) |

Step 1. Non-expansivity via a deterministic stopping-time argument:
For the fixed ε>0\varepsilon>0 such that β:=ρp​(1+ε)<1\beta:=\rho\_{p}(1+\varepsilon)<1, let η>0\eta>0 such that 1+1ϵ<ρp​(1+ϵ)​(1+η)21+\frac{1}{\epsilon}<\rho\_{p}(1+\epsilon)(1+\eta)^{2} and define the stopping time

|  |  |  |
| --- | --- | --- |
|  | τη:=inf{t≥0:δ¯t>(1+η)​δ¯0}\tau\_{\eta}:=\inf\{t\geq 0:\bar{\delta}\_{t}>(1+\eta)\bar{\delta}\_{0}\} |  |

(with the convention inf∅=+∞\inf\varnothing=+\infty). If τη<∞\tau\_{\eta}<\infty, then for s≤τηs\leq\tau\_{\eta} we have δ¯s≤(1+η)​δ¯0\bar{\delta}\_{s}\leq(1+\eta)\bar{\delta}\_{0} and by continuity δ¯τη=(1+η)​δ¯0\bar{\delta}\_{\tau\_{\eta}}=(1+\eta)\bar{\delta}\_{0}. Evaluating ([4.36](https://arxiv.org/html/2511.03474v1#S4.E36 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) at t=τηt=\tau\_{\eta} and bounding δ¯s2≤(1+η)2​δ¯02\bar{\delta}\_{s}^{2}\leq(1+\eta)^{2}\bar{\delta}\_{0}^{2} in the integral combined with the identity fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}) yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ¯τη2\displaystyle\bar{\delta}\_{\tau\_{\eta}}^{2} | ≤δ¯02​[(ϕ−fλ∗ϕ)2​(τη)​(1+1ε)+(1−(ϕ−fλ∗ϕ)2​(τη))​ρp​(1+ε)​(1+η)2]\displaystyle\leq\bar{\delta}\_{0}^{2}\left[(\phi-f\_{\lambda}\*\phi)^{2}(\tau\_{\eta})(1+\frac{1}{\varepsilon})+(1-(\phi-f\_{\lambda}\*\phi)^{2}(\tau\_{\eta}))\rho\_{p}(1+\varepsilon)(1+\eta)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤δ02​[(ϕ−fλ∗ϕ)2​(τη)​(1+1ε−ρp​(1+ε)​(1+η)2)+ρp​(1+ε)​(1+η)2]\displaystyle\leq\delta\_{0}^{2}\left[(\phi-f\_{\lambda}\*\phi)^{2}(\tau\_{\eta})\left(1+\frac{1}{\varepsilon}-\rho\_{p}(1+\varepsilon)(1+\eta)^{2}\right)+\rho\_{p}(1+\varepsilon)(1+\eta)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <ρp​(1+ε)​(1+η)2​δ¯02<(1+η)2​δ¯02.\displaystyle<\rho\_{p}(1+\varepsilon)(1+\eta)^{2}\bar{\delta}\_{0}^{2}<(1+\eta)^{2}\bar{\delta}\_{0}^{2}. |  |

which leads to a contradiction. Whence τη=+∞\tau\_{\eta}=+\infty i.e., δ¯s≤(1+η)​δ¯0\bar{\delta}\_{s}\leq(1+\eta)\bar{\delta}\_{0} for all s≥0s\geq 0. This holds for every η>0\eta>0, implying the non-expansivity bound δ¯t≤δ¯0\bar{\delta}\_{t}\leq\bar{\delta}\_{0} for all t≥0t\geq 0 when letting η↓0\eta\downarrow 0.

Step 2. Iteration and the Volterra map:
Substituting this (i.e. δ¯t≤δ¯0\bar{\delta}\_{t}\leq\bar{\delta}\_{0}) into ([4.35](https://arxiv.org/html/2511.03474v1#S4.E35 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) combined with the stabilizer identity fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}) gives, for all t>0t>0,

|  |  |  |
| --- | --- | --- |
|  | δ¯t2≤δ¯02​φ1,pε​(t),whereφ1,pε​(t):=(1+1ε)​(ϕ−fλ∗ϕ)2​(t)+ρp​(1+ε)​(1−(ϕ−fλ∗ϕ)2​(t)).\bar{\delta}\_{t}^{2}\leq\bar{\delta}\_{0}^{2}\,\varphi\_{1,p}^{\varepsilon}(t),\quad\text{where}\quad\,\varphi\_{1,p}^{\varepsilon}(t):=\Big(1+\frac{1}{\varepsilon}\Big)(\phi-f\_{\lambda}\*\phi)^{2}(t)+\rho\_{p}(1+\varepsilon)(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)). |  |

Note that φ1,pε​(t)=ρp​(1+ε)+(ϕ−fλ∗ϕ)2​(t)​(1+1ε−ρp​(1+ε))\varphi\_{1,p}^{\varepsilon}(t)=\rho\_{p}(1+\varepsilon)+(\phi-f\_{\lambda}\*\phi)^{2}(t)(1+\frac{1}{\varepsilon}-\rho\_{p}(1+\varepsilon)) satisfies:

|  |  |  |
| --- | --- | --- |
|  | φ1,pε​(0)=1+1ε,φ1​ is continuous, ​M1:=‖φ1,pε‖∞≤1+1ϵ+ρp​(1+ε)\varphi\_{1,p}^{\varepsilon}(0)=1+\frac{1}{\varepsilon},\quad\varphi\_{1}\text{ is continuous, }M\_{1}:=\|\varphi\_{1,p}^{\varepsilon}\|\_{\infty}\leq 1+\frac{1}{\epsilon}+\rho\_{p}(1+\varepsilon) |  |

Substituting this upper bound for δt2\delta\_{t}^{2} (i.e. δ¯t2≤δ¯02​φ1,pε​(t)\bar{\delta}\_{t}^{2}\leq\bar{\delta}\_{0}^{2}\varphi\_{1,p}^{\varepsilon}(t)) into ([4.35](https://arxiv.org/html/2511.03474v1#S4.E35 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) yields

|  |  |  |
| --- | --- | --- |
|  | δ¯t2≤δ¯¯02​φ2,pε​(t),whereφ2,pε​(t):=(1+1ε)​(ϕ−fλ∗ϕ)2​(t)+ρp​(1+ε)​∫0tfλ2​(t−s)​ς2​(s)​φ1,pε​(s)​d​sλ2​c.\bar{\delta}\_{t}^{2}\leq\bar{\bar{\delta}}\_{0}^{2}\varphi\_{2,p}^{\varepsilon}(t),\quad\text{where}\quad\varphi\_{2,p}^{\varepsilon}(t):=\Big(1+\frac{1}{\varepsilon}\Big)(\phi-f\_{\lambda}\*\phi)^{2}(t)+\rho\_{p}(1+\varepsilon)\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\varphi\_{1,p}^{\varepsilon}(s)\frac{ds}{\lambda^{2}c}. |  |

and inductively for k≥2k\geq 2

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ¯t2≤δ¯¯02​φk,pε​(t),whereφk,pε​(t):=(ϕ−fλ∗ϕ)2​(t)​(1+1ε)+ρp​(1+ε)​1λ2​c​∫0tfλ2​(t−s)​ς2​(s)​φk−1,pε​(s)​𝑑s.\bar{\delta}\_{t}^{2}\leq\bar{\bar{\delta}}\_{0}^{2}\varphi\_{k,p}^{\varepsilon}(t),\quad\text{where}\quad\varphi\_{k,p}^{\varepsilon}(t):=(\phi-f\_{\lambda}\*\phi)^{2}(t)\Big(1+\frac{1}{\varepsilon}\Big)+\rho\_{p}(1+\varepsilon)\frac{1}{\lambda^{2}c}\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\,\varphi\_{k-1,p}^{\varepsilon}(s)\,ds. |  | (4.37) |

To obtain a uniform sup-bound, put Mk:=‖φk,pε‖∞M\_{k}:=\|\varphi\_{k,p}^{\varepsilon}\|\_{\infty}. From ([4.37](https://arxiv.org/html/2511.03474v1#S4.E37 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and (ϕ−fλ∗ϕ)​(t)≤1(\phi-f\_{\lambda}\*\phi)(t)\leq 1, 1−(ϕ−fλ∗ϕ)​(t)≤11-(\phi-f\_{\lambda}\*\phi)(t)\leq 1, we get Mk≤(1+1ε)+β​Mk−1.M\_{k}\leq\Big(1+\frac{1}{\varepsilon}\Big)+\beta M\_{k-1}.
Iterating yields (since β<1\beta<1):

Mk≤(1+1ε)​∑j=1k−1βj+βk−1​M1≤max⁡(M1,1+1ε1−β)≤max⁡(1+1ε+β,1+1ε1−β)=1+1ε1−β.M\_{k}\leq\Big(1+\frac{1}{\varepsilon}\Big)\sum\_{j=1}^{k-1}\beta^{j}+\beta^{k-1}M\_{1}\leq\max(M\_{1},\frac{1+\frac{1}{\varepsilon}}{1-\beta})\leq\max(1+\frac{1}{\varepsilon}+\beta,\frac{1+\frac{1}{\varepsilon}}{1-\beta})=\frac{1+\frac{1}{\varepsilon}}{1-\beta}.
Thus for every k≥1k\geq 1 and t≥0t\geq 0 one has the uniform bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤φk,pε​(t)≤1+1/ε1−ρp​(1+ε):=M∗ϵ.0\leq\varphi\_{k,p}^{\varepsilon}(t)\leq\frac{1+1/\varepsilon}{1-\rho\_{p}(1+\varepsilon)}:=M\_{\*}^{\epsilon}. |  | (4.38) |

Step 3. Define the operator 𝒯:Cb​([0,∞))→Cb​([0,∞))\mathcal{T}:C\_{b}([0,\infty))\to C\_{b}([0,\infty)) :

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒯​ψ)​(t):=(ϕ−fλ∗ϕ)2​(t)​(1+1ε)+ρp​(1+ε)​1λ2​c​∫0tfλ2​(t−s)​ς2​(s)​ψ​(s)​𝑑s.(\mathcal{T}\psi)(t):=(\phi-f\_{\lambda}\*\phi)^{2}(t)\Big(1+\frac{1}{\varepsilon}\Big)+\rho\_{p}(1+\varepsilon)\frac{1}{\lambda^{2}c}\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\,\psi(s)\,ds. |  | (4.39) |

and, for k≥2k\geq 2, set φk,pε=𝒯​φk−1,pε\varphi\_{k,p}^{\varepsilon}=\mathcal{T}\varphi\_{k-1,p}^{\varepsilon}.
The operator 𝒯\mathcal{T} is linear in its last term and for any ψ1,ψ2∈Cb\psi\_{1},\psi\_{2}\in C\_{b},

|  |  |  |
| --- | --- | --- |
|  | ‖𝒯​ψ1−𝒯​ψ2‖∞≤ρp​(1+ε)⋅supt≥01λ2​c​∫0tfλ2​(t−s)​ς2​(s)​𝑑s⋅‖ψ1−ψ2‖∞=ρp​(1+ε)​‖ψ1−ψ2‖∞\|\mathcal{T}\psi\_{1}-\mathcal{T}\psi\_{2}\|\_{\infty}\leq\rho\_{p}(1+\varepsilon)\cdot\sup\_{t\geq 0}\frac{1}{\lambda^{2}c}\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\,ds\;\cdot\;\|\psi\_{1}-\psi\_{2}\|\_{\infty}=\rho\_{p}(1+\varepsilon)\|\psi\_{1}-\psi\_{2}\|\_{\infty} |  |

because the convolution integral equals 1−(ϕ−fλ∗ϕ)​(t)≤11-(\phi-f\_{\lambda}\*\phi)(t)\leq 1. By assumption ρp​(1+ε)<1\rho\_{p}(1+\varepsilon)<1, so 𝒯\mathcal{T} is a strict contraction in ∥⋅∥∞\|\cdot\|\_{\infty} with Lipschitz constant ρp​(1+ε)<1\rho\_{p}(1+\varepsilon)<1 on the complete or Banach space Cb​([0,∞))C\_{b}([0,\infty)) with the sup norm. The Banach fixed point theorem therefore provides a unique fixed point φ∞,pε∈Cb​([0,∞))\varphi\_{\infty,p}^{\varepsilon}\in C\_{b}([0,\infty)) and, moreover, φk,pε=𝒯k−1​φ1,pε→k→∞∥⋅∥∞φ∞,pε.\varphi\_{k,p}^{\varepsilon}=\mathcal{T}^{k-1}\varphi\_{1,p}^{\varepsilon}\xrightarrow[k\to\infty]{\|\cdot\|\_{\infty}}\varphi\_{\infty,p}^{\varepsilon}.

In particular the convergence is uniform on [0,∞)[0,\infty) i.e. φk,pε=𝒯k−1​φ1,pε\varphi\_{k,p}^{\varepsilon}=\mathcal{T}^{k-1}\varphi\_{1,p}^{\varepsilon} converges uniformly (on [0,∞)[0,\infty)) to φ∞,pε\varphi\_{\infty,p}^{\varepsilon}. For every t≥0t\geq 0 the LpL^{p}-norm satisfies
δ¯t2≤δ¯02​φ∞,pε​(t).\bar{\delta}\_{t}^{2}\leq\bar{\delta}\_{0}^{2}\,\varphi\_{\infty,p}^{\varepsilon}(t).

Step 4. Limit equation and ε\varepsilon-dependent asymptotic bound:
Passing to the limit in ([4.37](https://arxiv.org/html/2511.03474v1#S4.E37 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) yields that φ∞,pε\varphi\_{\infty,p}^{\varepsilon} satisfies the Volterra or functional fixed-point equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ∞,pε​(t)=(ϕ−fλ∗ϕ)2​(t)​(1+1ε)+ρp​(1+ε)​1λ2​c​∫0tfλ2​(t−s)​ς2​(s)​φ∞,pε​(s)​𝑑s.\varphi\_{\infty,p}^{\varepsilon}(t)=(\phi-f\_{\lambda}\*\phi)^{2}(t)\Big(1+\frac{1}{\varepsilon}\Big)+\rho\_{p}(1+\varepsilon)\frac{1}{\lambda^{2}c}\int\_{0}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}(s)\,\varphi\_{\infty,p}^{\varepsilon}(s)\,ds. |  | (4.40) |

By the uniform bound in equation ([4.38](https://arxiv.org/html/2511.03474v1#S4.E38 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), φ∞,pε\varphi\_{\infty,p}^{\varepsilon} is bounded and nonnegative on [0,∞)[0,\infty) i.e. ∀t≥0,0≤φ∞,pε​(t)≤1+1/ε1−ρp​(1+ε).\forall t\geq 0,\quad 0\leq\varphi\_{\infty,p}^{\varepsilon}(t)\leq\frac{1+1/\varepsilon}{1-\rho\_{p}(1+\varepsilon)}.
Taking lim inft→+∞,lim supt→∞\liminf\_{t\to+\infty},\limsup\_{t\to\infty} in ([4.40](https://arxiv.org/html/2511.03474v1#S4.E40 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and using (ϕ−fλ∗ϕ)2​(t)→a2(\phi-f\_{\lambda}\*\phi)^{2}(t)\to a^{2} and the stabilizer identity we obtain ℓ¯∞,pε,ℓ∞,pε:=lim inft→+∞φ∞,pε​(t),lim supt→+∞φ∞,pε​(t)∈[0,M∗ϵ]\underline{\ell}\_{\infty,p}^{\varepsilon},\ell\_{\infty,p}^{\varepsilon}:=\liminf\_{t\to+\infty}\varphi\_{\infty,p}^{\varepsilon}(t),\limsup\_{t\to+\infty}\varphi\_{\infty,p}^{\varepsilon}(t)\in[0,M\_{\*}^{\epsilon}]. Now, ℓ¯∞,pε,ℓ∞,pε∈[0,M∗ϵ]\underline{\ell}\_{\infty,p}^{\varepsilon},\ell\_{\infty,p}^{\varepsilon}\in[0,M\_{\*}^{\epsilon}] implies that for any η>0\eta>0, there exists tη∈ℝ+t\_{\eta}\in\mathbb{R}^{+} such that for t≥tηt\geq t\_{\eta}, ℓ¯∞,pε−η≤φ∞,pε​(t)≤ℓ∞,pε+η\underline{\ell}\_{\infty,p}^{\varepsilon}-\eta\leq\varphi\_{\infty,p}^{\varepsilon}(t)\leq\ell\_{\infty,p}^{\varepsilon}+\eta. Then, we obtain on the first hand,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tfλ2​(t−s)​ς2​(s)​φ∞,pε​(s)​d​sλ2​c\displaystyle\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{\infty,p}^{\varepsilon}(s)\frac{ds}{\lambda^{2}c} | ≤1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ∞,pε+η)​𝑑s+1c​λ2​∫0tηfλ2​(t−s)​ς2​(s)​φ∞,pε​(s)​𝑑s\displaystyle\leq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\ell\_{\infty,p}^{\varepsilon}+\eta)\,ds+\frac{1}{c\lambda^{2}}\int\_{0}^{t\_{\eta}}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{\infty,p}^{\varepsilon}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ∞,pε+η)​𝑑s+1c​λ2​M∗ϵ​∫t−tηtfλ2​(u)​ς2​(t−s)​𝑑u.\displaystyle\leq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\ell\_{\infty,p}^{\varepsilon}+\eta)\,ds+\frac{1}{c\lambda^{2}}M\_{\*}^{\epsilon}\int\_{t-t\_{\eta}}^{t}f^{2}\_{\lambda}(u)\varsigma^{2}(t-s)\,du. |  |

where the second term on the right-hand side of the last inequality follows from the fact that φ∞,pε​(t−u)≤M∗ϵ\varphi\_{\infty,p}^{\varepsilon}(t-u)\leq M\_{\*}^{\epsilon} for all u≤t≤tηu\leq t\leq t\_{\eta} and vanishes as t goes to infinity.

Since fλ∈L2​(Leb1)f\_{\lambda}\in L^{2}(\text{Leb}\_{1}) and limt→+∞(ϕ−fλ∗ϕ)2​(t)=a2​ϕ∞2\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)^{2}(t)=a^{2}\phi\_{\infty}^{2} both owing to Assumption [3.1](https://arxiv.org/html/2511.03474v1#S3.Thmassumption1 "Assumption 3.1 (𝜆-resolvent 𝑅_𝜆 of the kernel). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we conclude from equation ([4.40](https://arxiv.org/html/2511.03474v1#S4.E40 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and the identity satisfied by ς\varsigma:

|  |  |  |
| --- | --- | --- |
|  | ℓ∞,pε=:lim supt→+∞φ∞,pε(t)≤(1+1ε)a2ϕ∞2+ρp(1+ε)(ℓ∞,pε+η)(1−a2ϕ∞2)⟹η→0ℓ∞,pε≤(1+1ε)​a2​ϕ∞21−ρp​(1+ε)​(1−a2​ϕ∞2)\ell\_{\infty,p}^{\varepsilon}=:\limsup\_{t\to+\infty}\varphi\_{\infty,p}^{\varepsilon}(t)\leq(1+\frac{1}{\varepsilon})\,a^{2}\phi\_{\infty}^{2}+\rho\_{p}(1+\varepsilon)(\ell\_{\infty,p}^{\varepsilon}+\eta)(1-a^{2}\phi\_{\infty}^{2})\overset{\eta\to 0}{\implies}\ell\_{\infty,p}^{\varepsilon}\leq\frac{(1+\frac{1}{\varepsilon})\,a^{2}\phi\_{\infty}^{2}}{1-\rho\_{p}(1+\varepsilon)(1-a^{2}\phi\_{\infty}^{2})} |  |

On the other hand, we also have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tfλ2​(t−s)​ς2​(s)​φ∞,pε​(s)​d​sλ2​c\displaystyle\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\varphi\_{\infty,p}^{\varepsilon}(s)\frac{ds}{\lambda^{2}c} | ≥1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ¯∞,pε−η)​𝑑s+∫t−tηtfλ2​(u)​ς2​(t−u)​φ∞,pε​(t−u)​d​uc​λ2\displaystyle\geq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\underline{\ell}\_{\infty,p}^{\varepsilon}-\eta)\,ds+\int\_{t-t\_{\eta}}^{t}f^{2}\_{\lambda}(u)\,\varsigma^{2}(t-u)\varphi\_{\infty,p}^{\varepsilon}(t-u)\,\frac{du}{c\lambda^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥1c​λ2​∫tηtfλ2​(t−s)​ς2​(s)​(ℓ¯∞,pε−η)​𝑑s.\displaystyle\geq\frac{1}{c\lambda^{2}}\int\_{t\_{\eta}}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)(\underline{\ell}\_{\infty,p}^{\varepsilon}-\eta)\,ds. |  |

Therefore, still with the fact that fλ∈L2​(Leb1)f\_{\lambda}\in L^{2}(\text{Leb}\_{1}) and limt→+∞(ϕ−fλ∗ϕ)2​(t)=a2\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)^{2}(t)=a^{2}, we obtain from equation ([4.40](https://arxiv.org/html/2511.03474v1#S4.E40 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and the identity satisfied by ς\varsigma:

|  |  |  |
| --- | --- | --- |
|  | ℓ¯∞,pε=:lim inft→+∞φ∞,pε(t)≥(1+1ε)a2ϕ∞2+ρp(1+ε)(ℓ¯∞,pε−η)(1−a2ϕ∞2)⟹η→0ℓ¯∞,pε≥(1+1ε)​a2​ϕ∞21−ρp​(1+ε)​(1−a2​ϕ∞2).\underline{\ell}\_{\infty,p}^{\varepsilon}=:\liminf\_{t\to+\infty}\varphi\_{\infty,p}^{\varepsilon}(t)\geq(1+\frac{1}{\varepsilon})\,a^{2}\phi\_{\infty}^{2}+\rho\_{p}(1+\varepsilon)(\underline{\ell}\_{\infty,p}^{\varepsilon}-\eta)(1-a^{2}\phi\_{\infty}^{2})\overset{\eta\to 0}{\implies}\underline{\ell}\_{\infty,p}^{\varepsilon}\geq\frac{(1+\frac{1}{\varepsilon})\,a^{2}\phi\_{\infty}^{2}}{1-\rho\_{p}(1+\varepsilon)(1-a^{2}\phi\_{\infty}^{2})}. |  |

Consequently, ℓ¯∞,pε=ℓ∞,pε=(1+1ε)​a2​ϕ∞21−ρp​(1+ε)​(1−a2​ϕ∞2):=L​(ϵ)\underline{\ell}\_{\infty,p}^{\varepsilon}=\ell\_{\infty,p}^{\varepsilon}=\frac{(1+\frac{1}{\varepsilon})\,a^{2}\phi\_{\infty}^{2}}{1-\rho\_{p}(1+\varepsilon)(1-a^{2}\phi\_{\infty}^{2})}:=L(\epsilon).
The minimizer of L​(ϵ)L(\epsilon) in (0,1/ρp−1)(0,1/\rho\_{p}-1) is ε∗=1ρp​(1−a2​ϕ∞2)−1,\varepsilon\_{\*}=\frac{1}{\sqrt{\rho\_{p}(1-a^{2}\phi\_{\infty}^{2})}}-1,
which is admissible iff ρp<1−a2​ϕ∞2\rho\_{p}<1-a^{2}\phi\_{\infty}^{2}. In that admissible case one obtains the optimal asymptotic value: infε∈(0,1/ρp−1)L​(ϵ)=ℓ∞,pε∗=a2​ϕ∞2(1−ρp​1−a2​ϕ∞2)2.\inf\_{\varepsilon\in(0,1/\rho\_{p}-1)}L(\epsilon)=\ell\_{\infty,p}^{\varepsilon\_{\*}}=\frac{a^{2}\phi\_{\infty}^{2}}{\big(1-\sqrt{\rho\_{p}}\sqrt{1-a^{2}\phi\_{\infty}^{2}}\big)^{2}}.

Step 5. Passage to the ε\varepsilon-Free Control: Finally, optimizing φ∞,pε\varphi\_{\infty,p}^{\varepsilon} over admissible ε\varepsilon gives the ε\varepsilon-free control i.e. passing to the infimum over admissible ε\varepsilon gives the claimed ε\varepsilon-free control with φ∞,p​(t)\varphi\_{\infty,p}(t).
δ¯t2≤δ¯02​φ∞,p​(t),φ∞,p​(t):=infε∈(0,1/ρp−1)φ∞,pε​(t).\bar{\delta}\_{t}^{2}\leq\bar{\delta}\_{0}^{2}\,\varphi\_{\infty,p}(t),\qquad\varphi\_{\infty,p}(t):=\inf\_{\varepsilon\in(0,1/\rho\_{p}-1)}\varphi\_{\infty,p}^{\varepsilon}(t).\quad
Now, note that

|  |  |  |
| --- | --- | --- |
|  | ∀t≥0,0≤φ∞,p​(t):=infε∈(0,1/ρp−1)φ∞,pε​(t)≤infε∈(0,1/ρp−1)1+1/ε1−ρp​(1+ε)=M∗ϵ=1ρp−1=1(1−ρp)2.\forall t\geq 0,\quad 0\leq\varphi\_{\infty,p}(t):=\inf\_{\varepsilon\in(0,1/\rho\_{p}-1)}\varphi\_{\infty,p}^{\varepsilon}(t)\leq\inf\_{\varepsilon\in(0,1/\rho\_{p}-1)}\frac{1+1/\varepsilon}{1-\rho\_{p}(1+\varepsilon)}=M\_{\*}^{\epsilon=\frac{1}{\sqrt{\rho\_{p}}}-1}=\frac{1}{(1-\sqrt{\rho\_{p}})^{2}}. |  |

Moreover, lim supt→∞φ∞,p​(t)=lim supt→∞infε∈(0,1/ρp−1)φ∞,pε​(t)≤lim supt→∞φ∞,pε∗​(t)=ℓ∞,pε∗\limsup\_{t\to\infty}\varphi\_{\infty,p}(t)=\limsup\_{t\to\infty}\inf\_{\varepsilon\in(0,1/\rho\_{p}-1)}\varphi\_{\infty,p}^{\varepsilon}(t)\leq\limsup\_{t\to\infty}\varphi\_{\infty,p}^{\varepsilon\_{\*}}(t)=\ell\_{\infty,p}^{\varepsilon\_{\*}}
so that
limt→∞φ∞,p​(t)≤a2​ϕ∞2(1−ρp​1−a2​ϕ∞2)2,\lim\_{t\to\infty}\varphi\_{\infty,p}(t)\leq\frac{a^{2}\phi\_{\infty}^{2}}{\big(1-\sqrt{\rho\_{p}}\sqrt{1-a^{2}\phi\_{\infty}^{2}}\big)^{2}},
with equality if the uniform convergence supε∈(0,1/ρp−1)|φ∞,pε​(t)−ℓ​(ε)|→t→∞0\sup\_{\varepsilon\in(0,1/\rho\_{p}-1)}\big|\varphi\_{\infty,p}^{\varepsilon}(t)-\ell(\varepsilon)\big|\xrightarrow[t\to\infty]{}0\; holds.
Hence ‖Xt−Xt′‖p≤φ∞,p​(t)1/2​‖X0−X0′‖p\|X\_{t}-X^{\prime}\_{t}\|\_{p}\leq\varphi\_{\infty,p}(t)^{1/2}\,\|X\_{0}-X^{\prime}\_{0}\|\_{p} for every t≥0t\geq 0,
and therefore, by coupling, for the pp-Wasserstein distance between marginals,Wp​([Xt],[Xt′])≤φ∞,p​(t)1/2​Wp​([X0],[X0′]).W\_{p}([X\_{t}],[X^{\prime}\_{t}])\leq\varphi\_{\infty,p}(t)^{1/2}\,W\_{p}([X\_{0}],[X^{\prime}\_{0}]).
In particular, if a=0a=0 the asymptotic bound above yields φ∞,p​(t)→0\varphi\_{\infty,p}(t)\to 0 and thus the process is contracting in WpW\_{p} as t→∞t\to\infty.
This completes the proof. □\square

Remark. 1. The function φ∞,p\varphi\_{\infty,p} quantifies the time decay of the LpL^{p} discrepancy between two solutions of the SVIE with different initial values. If ς\varsigma is bounded (i.e. ‖ς2‖∞<+∞\|\varsigma^{2}\|\_{\infty}<+\infty ) and both κ<λ2(CpBDG)2​(1+ε∗)​‖ς2‖∞​∫0+∞fλ2​(u)​𝑑u\kappa<\frac{\lambda^{2}}{(C\_{p}^{\mathrm{BDG}})^{2}\,(1+\varepsilon\_{\*})\,\|\varsigma^{2}\|\_{\infty}\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\,du} and (ϕ−fλ∗ϕ)∈L2​(Leb1)(\phi-f\_{\lambda}\*\phi)\in L^{2}(\text{Leb}\_{1}),
then one derives from equation ([4.40](https://arxiv.org/html/2511.03474v1#S4.E40 "In 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and using Fubini-Tonelli’s theorem that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0+∞φ∞,p​(s)​𝑑s\displaystyle\int\_{0}^{+\infty}\varphi\_{\infty,p}(s)\,ds | ≤∫0+∞φ∞,pε∗​(s)​𝑑s≤λ2​(1+1ε∗)λ2−(CpBDG)2​κ​(1+ε∗)​‖ς2‖∞​‖fλ‖L2​(Leb1)2​∫0+∞(ϕ−fλ∗ϕ)2​(t)​𝑑t<∞.\displaystyle\leq\int\_{0}^{+\infty}\varphi\_{\infty,p}^{\varepsilon\_{\*}}(s)\,ds\leq\frac{\lambda^{2}\Big(1+\frac{1}{\varepsilon\_{\*}}\Big)}{\lambda^{2}-(C\_{p}^{\mathrm{BDG}})^{2}\,\kappa(1+\varepsilon\_{\*})\|\varsigma^{2}\|\_{\infty}\|f\_{\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}}\int\_{0}^{+\infty}(\phi-f\_{\lambda}\*\phi)^{2}(t)\,dt<\infty. |  |

2. L2L^{2}-confluence: Under the assumption of Proposition [4.4](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem4 "Proposition 4.4 (𝐿^𝑝-confluence). ‣ 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") with c∈(0,1κ)c\!\in\big(0,\frac{1}{\kappa}\big), ρ:=c​κ\rho:=c\kappa and X0,X0′∈L2​(ℙ)X\_{0},X^{\prime}\_{0}\!\in L^{2}({\mathbb{P}}). By ([EGnabeyeuPR2025,](https://arxiv.org/html/2511.03474v1#bib.bib21) , Proposition 5.3) (which use Itô’s Isometry and the first Dini Lemma), one has that the solutions to Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) denoted (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X^{\prime}\_{t})\_{t\geq 0} starting from X0X\_{0} and X0′X^{\prime}\_{0} respectively satisfies:

* (a)

  There exists a continuous non-negative function φ∞λ,c,K,ϕ=:φ∞:ℝ+→[0,1]\varphi\_{\infty}^{\lambda,c,K,\phi}=:\varphi\_{\infty}:\mathbb{R}^{+}\to[0,1], such that φ∞​(0)=1\varphi\_{\infty}(0)=1, limt→+∞φ∞​(t)=a2​ϕ∞21−ρ​(1−a2​ϕ∞2)\lim\_{t\to+\infty}\varphi\_{\infty}(t)=\frac{a^{2}\phi\_{\infty}^{2}}{1-\rho(1-a^{2}\phi\_{\infty}^{2})}, only depending on λ,c,ϕ\lambda,c,\phi, and KK, such that :

  |  |  |  |
  | --- | --- | --- |
  |  | ∀t≥0,𝔼​(|Xt−Xt′|)2≤φ∞​(t)​𝔼​(|X0−X0′|)2W2​([Xt′],[Xt])≤φ∞​(t)1/2​W2​([X0′],[X0]).\forall t\geq 0,\;\mathbb{E}\,\Big(\Big|X\_{t}-X^{\prime}\_{t}\Big|\Big)^{2}\leq\varphi\_{\infty}(t)\mathbb{E}\,\Big(\Big|X\_{0}-X^{\prime}\_{0}\Big|\Big)^{2}\quad\;W\_{2}([X\_{t}^{\prime}],[X\_{t}])\leq\varphi\_{\infty}(t)^{1/2}W\_{2}([X\_{0}^{\prime}],[X\_{0}]). |  |
* (b)

  In particular, if a=0a=0 or ϕ∞=0\phi\_{\infty}=0 and XX has a fake stationary regime of type I, 𝔼​Xt′→x∞\mathbb{E}X\_{t}^{\prime}\to x\_{\infty}, Var​(Xt′)→v0\text{Var}(X\_{t}^{\prime})\to v\_{0} as t→+∞t\to+\infty.
  And more generally finite-dimensional W2W\_{2}-convergence.
  Thus, the process X′X^{\prime} mixes: as time increases, the random variable Xt′X^{\prime}\_{t} progressively forgets its initial mean and variance and converges to those of the limiting fake stationary regime.
  While, if X has a fake stationary regime of type II, its marginal distribution is unique.

### 4.3 Asymptotics: Long run functional weak behaviour:

In the following, →(C)\stackrel{{\scriptstyle(C)}}{{\rightarrow}} stands for functional weak convergence on C​(ℝ+,ℝ)C(\mathbb{R}\_{+},\mathbb{R}) equipped with the topology of uniform convergence on compact sets.
To establish relative compactness in (b) of the below theorem, in terms of functional 𝒲2{\cal W}\_{2}-compactness (quadratic Wasserstein distance), we require that ‖supt≥0|Xt|‖p<+∞\|\sup\_{t\geq 0}|X\_{t}|\|\_{p}<+\infty for some p>2p>2.

###### Assumption 4.5 (Integrability and Uniform Hölder continuity).

Let λ,c>0\lambda,c>0, and assume the kernel KK and its λ\lambda-resolvent RλR\_{\lambda} satisfy

∫0+∞fλ2​β​(u)​𝑑u<+∞for some ​β≥1,so thatfλ∈ℒ2​(L​e​b1),\int\_{0}^{+\infty}f\_{\lambda}^{2\beta}(u)\,du<+\infty\quad\text{for some }\beta\geq 1,\quad\text{so that}\quad f\_{\lambda}\in\mathcal{L}^{2}(Leb\_{1}),

and there exists ϑ∈(0,1]\vartheta\in(0,1], and a real constant C<+∞C<+\infty such that666Uniform Hölder continuity or Hölder regularity with exponent ϑ\vartheta for the function fα,λf\_{\alpha,\lambda}, ensuring controlled behavior as tt and t+δt+\delta become arbitrarily close.

maxi=1,2[∫0+∞|fλ(u+δ¯)−fλ(u)|idu]1i≤Cδ¯ϑ.\max\_{i=1,2}\left[\int\_{0}^{+\infty}|f\_{\lambda}(u+\bar{\delta})-f\_{\lambda}(u)|^{i}\,du\right]^{\frac{1}{i}}\leq C\bar{\delta}^{\vartheta}.

###### Theorem 4.6.

Let λ,c>0\lambda,c>0, let μ∞∈ℝ\mu\_{\infty}\in\mathbb{R}, and let μ:ℝ→ℝ\mu:\mathbb{R}\to\mathbb{R} a bounded bornel funtion, σ:ℝ→ℝ\sigma:\mathbb{R}\to\mathbb{R} be a Lipschitz continuous function satisfying equation ([4.33](https://arxiv.org/html/2511.03474v1#S4.E33 "In Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) (S​Lσ)(SL\_{\sigma}). Assume Assumption [4.5](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem5 "Assumption 4.5 (Integrability and Uniform Hölder continuity). ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and Assumption [3.8](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem8 "Assumption 3.8 (On the stabilizer). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") on Equation (Eλ)(E\_{\lambda}) are in force. Let (Xt)t≥0(X\_{t})\_{t\geq 0} be the solution to the scaled Stochastic Volterra Integral Equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0∈Lp​(ℙ)X\_{0}\in L^{p}(\mathbb{P}) for some suitable pp.

(a) C-tightness of time-shifted processes. Assume

|  |  |  |  |
| --- | --- | --- | --- |
|  | X0∈Lp​(ℙ)and{p=2andc<1κ2if(δ∧ϑ∧β−12​β)>12,p>1δ∧ϑ∧β−12​βandc<1(CpBDG)2​κ2if(δ∧ϑ∧β−12​β)≤12.X\_{0}\in L^{p}(\mathbb{P})\quad\text{and}\quad\begin{cases}p=2\quad\text{and}\quad c<\frac{1}{\kappa\_{2}}\quad\text{if}\quad(\delta\wedge\vartheta\wedge\frac{\beta-1}{2\beta})>\frac{1}{2},\\ p>\frac{1}{\delta\wedge\vartheta\wedge\frac{\beta-1}{2\beta}}\quad\text{and}\quad c<\frac{1}{(C\_{p}^{\text{BDG}})^{2}\kappa\_{2}}\quad\text{if}\quad(\delta\wedge\vartheta\wedge\frac{\beta-1}{2\beta})\leq\frac{1}{2}.\end{cases} |  | (4.41) |

Then, the family of shifted processes (Xt+u)u≥0(X\_{t+u})\_{u\geq 0} is C-tight, uniformly integrable, and square uniformly integrable for p>2p>2 as t→+∞t\to+\infty. For any limiting distribution PP on Ω0:=C​(ℝ+,ℝ)\Omega\_{0}:=C(\mathbb{R}\_{+},\mathbb{R}), the canonical process Yt​(ω)=ω​(t)Y\_{t}(\omega)=\omega(t) has a (δ∧ϑ∧β−12​β−1p−η)\left(\delta\wedge\vartheta\wedge\frac{\beta-1}{2\beta}-\frac{1}{p}-\eta\right)-Hölder pathwise continuous PP-modification for sufficiently small η>0\eta>0.

That is, there exists a process X∞X^{\infty} with continuous sample paths such that

(Xt+u)t≥0⇒(Xt∞)t≥0weakly in ​C​(ℝ+;ℝ)​ as ​u→∞.(X\_{t+u})\_{t\geq 0}\Rightarrow(X^{\infty}\_{t})\_{t\geq 0}\quad\text{weakly in }C(\mathbb{R}\_{+};\mathbb{R})\text{ as }u\to\infty.

Any limiting process X∞X^{\infty} satisfies ∀t≥0,Xt∞∈Lp​(ℙ)\forall t\geq 0,\quad X^{\infty}\_{t}\in L^{p}(\mathbb{P}) for each p≥2p\geq 2 and its first moment is given by
𝔼​[Xt∞]=a​ϕ∞​𝔼​[X0]+(1−a)​μ∞λ.\mathbb{E}[X^{\infty}\_{t}]=a\phi\_{\infty}\mathbb{E}[X\_{0}]+(1-a)\frac{\mu\_{\infty}}{\lambda}.

Moreover, if a=0a=0, the shifted processes of two solutions (Xt)t≥0(X\_{t})\_{t\geq 0} and (Xt′)t≥0(X\_{t}^{\prime})\_{t\geq 0} are L2L^{2}-confluent, i.e. there exists a non-increasing function φ¯∞:ℝ+→[0,1]\bar{\varphi}\_{\infty}:\mathbb{R}\_{+}\to[0,1] with limt→+∞φ¯∞​(t)=0\lim\_{t\to+\infty}\bar{\varphi}\_{\infty}(t)=0, and

W2​([(Xt+t1,…,Xt+tN)],[(Xt+t1′,…,Xt+tN′)])→0ast→+∞.W\_{2}\left(\left[(X\_{t+t\_{1}},\ldots,X\_{t+t\_{N}})\right],\left[(X^{\prime}\_{t+t\_{1}},\ldots,X^{\prime}\_{t+t\_{N}})\right]\right)\to 0\quad\text{as}\quad t\to+\infty.

Hence, the functional weak limiting distributions of [Xt+⁣⋅][X\_{t+\cdot}] and [Xt+⁣⋅′][X^{\prime}\_{t+\cdot}] coincide, meaning that if [Xtn+⁣⋅]→(C)P[X\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)}}{{\rightarrow}}P for some subsequence tn→+∞t\_{n}\to+\infty, then [Xtn+⁣⋅′]→(C)wP[X^{\prime}\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)\_{w}}}{{\rightarrow}}P and vice versa.

(b) Functional weak long-run behavior. Assume furthermore that the solution (Xt)t≥0(X\_{t})\_{t\geq 0} of the volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has a fake stationary regime of type I, starting from a random variable X0∈L2​(P)X\_{0}\in L^{2}(P) with mean μ∞λ\frac{\mu\_{\infty}}{\lambda} and variance v0v\_{0}.Then for any limiting distribution X∞X^{\infty}, 𝔼​[Xt∞]=μ∞λ\mathbb{E}[X^{\infty}\_{t}]=\frac{\mu\_{\infty}}{\lambda}
while its autocovariance function is, for t1,t2≥0t\_{1},t\_{2}\geq 0, t1≤t2t\_{1}\leq t\_{2}, given by Cov​(Xt1∞,Xt2∞)=Cfλ​(t1,t2)\text{Cov}(X\_{t\_{1}}^{\infty},X\_{t\_{2}}^{\infty})=C\_{f\_{\lambda}}(t\_{1},t\_{2})

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(Xt+t1,Xt+t2)​→t→+∞​Cfλ​(t1,t2):=a2​ϕ∞2​Var​(X0)+(1−a2​ϕ∞2)​v0∫0+∞fλ2​(s)​𝑑s​∫0+∞fλ​(t2−t1+u)​fλ​(u)​𝑑u.\text{Cov}(X\_{t+t\_{1}},X\_{t+t\_{2}})\overset{t\to+\infty}{\to}C\_{f\_{\lambda}}(t\_{1},t\_{2}):=a^{2}\phi\_{\infty}^{2}{\rm Var}(X\_{0})+\frac{(1-a^{2}\phi\_{\infty}^{2})v\_{0}}{\int\_{0}^{+\infty}f^{2}\_{\lambda}(s)ds}\int\_{0}^{+\infty}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)du. |  | (4.42) |

Thus, under any limiting distribution PP, the canonical process YY is a (weak) L2L^{2}-stationary process777Weak-stationarity in the sense of constant mean, variance and stable autocovariance function (see for example [KloedenPlaten1999](https://arxiv.org/html/2511.03474v1#bib.bib31) ) in constrat to Strong-stationarity where all finite-dimensional distributions are invariant under time shifts. with mean x∞x\_{\infty} and covariance function C¯fλ​(s,t)\bar{C}\_{f\_{\lambda}}(s,t), for s,t≥0s,t\geq 0.

(c) Stationary Gaussian Case. If σ​(x)=σ>0\sigma(x)=\sigma>0 is constant and X0X\_{0} has a Gaussian distribution, (say X0∼𝒩​(x∞,v0)X\_{0}\sim\mathcal{N}\left(x\_{\infty},v\_{0}\right)),
then (Xt)t≥0(X\_{t})\_{t\geq 0} satisfies
Xt+⁣⋅⟶(C)𝒢​𝒫​(fλ)ast→+∞,X\_{t+\cdot}\stackrel{{\scriptstyle(C)}}{{\longrightarrow}}\mathcal{GP}(f\_{\lambda})\quad\text{as}\quad t\to+\infty,
where 𝒢​𝒫​(fλ)\mathcal{GP}(f\_{\lambda}) is the stationary Gaussian process with mean x∞x\_{\infty}
and covariance function Cfλ​(⋅)C\_{f\_{\lambda}}(\cdot).

Remark: Be aware that at this stage, we do not have uniqueness of the limit distributions since they are
not characterized by their mean and covariance functions, except in Gaussian setting.

## 5 Applications to Fractional Stochastic Volterra Integral equations

Let consider the below Fractional integration kernel where α=H+12\alpha=H+\frac{1}{2}, with HH denoting the Hurst coefficient:

|  |  |  |  |
| --- | --- | --- | --- |
|  | K​(t)=Kα​(t)=uα−1Γ​(α)​1ℝ+​(t),α>0.K(t)=K\_{\alpha}(t)=\frac{u^{\alpha-1}}{\Gamma(\alpha)}\mbox{\bf 1}\_{\mathbb{R}\_{+}}(t),\quad\alpha>0. |  | (5.43) |

This family of kernels corresponds to the fractional integrations of order α>0\alpha>0 and satisfy ([2.8](https://arxiv.org/html/2511.03474v1#S2.E8 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), ([2.3](https://arxiv.org/html/2511.03474v1#S2.E3 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([2.4](https://arxiv.org/html/2511.03474v1#S2.E4 "In Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) for α>1/2\alpha>1/2 (with θT=(α−12)∧1\theta\_{{}\_{T}}=(\alpha-\frac{1}{2})\wedge 1, see [RiTaYa2020](https://arxiv.org/html/2511.03474v1#bib.bib42) ; [JouPag22](https://arxiv.org/html/2511.03474v1#bib.bib30) ) among many others.
It follows from the easy identity Kα∗Kα′=Kα+α′K\_{\alpha}\*K\_{\alpha^{\prime}}=K\_{\alpha+\alpha^{\prime}}, that Rα,λ​(t)=∑k≥0(−1)k​λk​tα​kΓ​(α​k+1)=Eα​(−λ​tα)=eα​(λ1/α​t)​t≥0,R\_{\alpha,\lambda}(t)=\sum\_{k\geq 0}(-1)^{k}\frac{\lambda^{k}t^{\alpha k}}{\Gamma(\alpha k+1)}=E\_{\alpha}(-\lambda t^{\alpha})=e\_{\alpha}(\lambda^{1/\alpha}t)\;t\geq 0,
where EαE\_{\alpha} denotes the standard Mittag-Leffler function and eαe\_{\alpha}, the alternate Mittag-Leffler function.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eα​(t)=∑k≥0tkΓ​(α​k+1),t∈ℝandeα​(t):=Eα​(−tα)=∑k≥0(−1)k​tα​kΓ​(α​k+1),t≥0.E\_{\alpha}(t)=\sum\_{k\geq 0}\frac{t^{k}}{\Gamma(\alpha k+1)},\ t\!\in\mathbb{R}\quad\textit{and}\quad e\_{\alpha}(t):=E\_{\alpha}(-t^{\alpha})=\sum\_{k\geq 0}(-1)^{k}\frac{t^{\alpha k}}{\Gamma(\alpha k+1)},\quad t\geq 0. |  | (5.44) |

In section 5 of [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36)  (see [GorMain1997](https://arxiv.org/html/2511.03474v1#bib.bib25)  further on), the author demonstrated that for such kernels KαK\_{\alpha}, with 12<α<1\frac{1}{2}<\alpha<1 (“ rough models”
),
EαE\_{\alpha} is increasing and differentiable on the real line with limt→+∞Eα​(t)=+∞\displaystyle\lim\_{t\to+\infty}E\_{\alpha}(t)=+\infty and Eα​(0)=1E\_{\alpha}(0)=1. In particular, EαE\_{\alpha} is an homeomorphism from (−∞,0](-\infty,0] to (0,1](0,1]. Consequently,
the resolvent Rα,λR\_{\alpha,\lambda} satisfies its established monotonicity condition (𝒦)({\cal K})\; for all λ>0\lambda>0. Moreover, it was shown that
if λ>0\lambda>0, the function fα,λ:=−Rα,λf\_{\alpha,\lambda}:=-R\_{\alpha,\lambda} exists and is defined on (0,+∞)(0,+\infty) by:
  
fα,λ​(t)=−Rα,λ′​(t)=α​λ​tα−1​Eα′​(−λ​tα)=λ​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1))f\_{\alpha,\lambda}(t)=-R^{\prime}\_{\alpha,\lambda}(t)=\alpha\lambda t^{\alpha-1}E^{\prime}\_{\alpha}(-\lambda t^{\alpha})=\lambda t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\lambda^{k}\frac{t^{\alpha k}}{\Gamma(\alpha(k+1))}
so that for α∈(12,1)\alpha\in(\frac{1}{2},1),
fα,λf\_{\alpha,\lambda} is a probability densitycalled Mittag-Leffler density and is square-integrable with respect to the Lebesgue measure on ℝ+\mathbb{R}\_{+}. Consequently, the results established in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) , particularly in Sections 2, 3, and 4, apply to the case σ​(t,x)=σ​(t)\sigma(t,x)=\sigma(t) (Gaussian setting) and σ​(t,x)=ς​(t)​σ​(x)\sigma(t,x)=\varsigma(t)\sigma(x).

Note that, in this paper, our Assumption (𝒦)({\cal K})\; is a slightly relaxed version of that of [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) .
The purpose of this part is to extend these results to the general case where α∈ℝ+∗\alpha\in\mathbb{R}^{\*}\_{+}. We show that for 0<α<20<\alpha<2, the resolvent Rα,λR\_{\alpha,\lambda} of KαK\_{\alpha} satisfy our relaxed monotonicity assumption (𝒦)({\cal K})\; for all λ>0\lambda>0, and that fα,λ:=−Rα,λf\_{\alpha,\lambda}:=-R\_{\alpha,\lambda} exists and is square-integrable with respect to the Lebesgue measure on ℝ+\mathbb{R}\_{+}, both for 12<α<1\frac{1}{2}<\alpha<1 (“rough models”
) and 12<α<32\frac{1}{2}<\alpha<\frac{3}{2} (“long memory volatility models”). As a result, the findings from Sections [3](https://arxiv.org/html/2511.03474v1#S3 "3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and [4](https://arxiv.org/html/2511.03474v1#S4 "4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), will be applicable in the cases where σ​(t,x)=σ​(x)\sigma(t,x)=\sigma(x) (Gaussian setting) and σ​(t,x)=ς​(t)​σ​(x)\sigma(t,x)=\varsigma(t)\sigma(x).
To this end, by a scaling property, it is enough to study Rα,1R\_{\alpha,1} (λ=1\lambda=1) given by its expansion Eα​(−tα)E\_{\alpha}(-t^{\alpha}) where EαE\_{\alpha} in the literature is known as Mittag-Leffler function.

We will leverage the conducive class of completely monotone functions. Let us recall that a function φ:(0,+∞)→[0,+∞)\varphi:(0,+\infty)\to[0,+\infty) is called a completely monotone (CM) function if it is non-negative, C∞C^{\infty} (i.e. it is infinitely differentiable on (0,+∞)(0,+\infty)), and satisfies (−1)n​φ(n)​(t)≥0(-1)^{n}\varphi^{(n)}(t)\geq 0 for all n∈ℕn\in\mathbb{N} and t>0t>0.

Crucially, “Bernstein-Widder theorem” ([Schilling2010,](https://arxiv.org/html/2511.03474v1#bib.bib44) , Theorem 1.4) (see also [Bernstein1929](https://arxiv.org/html/2511.03474v1#bib.bib7) ) provides a necessary and sufficient condition a function φ:ℝ+→ℝ\varphi:\mathbb{R}\_{+}\to\mathbb{R} to be CM. More specifically, φ\varphi is CM if it is a ( real valued) Laplace transform of a unique non-negative measure μ\mu on [0,∞)[0,\infty). Futhermore, a result by Pollard [SchillingSongVondracek2012](https://arxiv.org/html/2511.03474v1#bib.bib45)  state that a CM function can be obtained by composing a CM function with a Bernstein function888A function ψ:ℝ+→ℝ\psi:\mathbb{R}\_{+}\to\mathbb{R} is called a Bernstein function if it is of class 𝒞∞\mathcal{C}^{\infty}, is non-negative, and its derivative is CM.

### 5.1 α\alpha-fractional kernels with α>0\alpha>0

The Mittag-Leffler function Eα​(z)E\_{\alpha}(z), with α>0\alpha>0, generalizes the exponential function (attained with α=1\alpha=1). It is defined by a power series, which converges on the entire complex plane. In particular, we are interested in the alternate Mittag-Leffler function reading:

|  |  |  |
| --- | --- | --- |
|  | eα​(t):=Eα​(−tα)=∑k≥0(−1)k​tα​kΓ​(α​k+1),t≥0,Eα​(z):=∑n=0∞znΓ​(α​n+1),α>0,z∈ℂ.e\_{\alpha}(t):=E\_{\alpha}(-t^{\alpha})=\sum\_{k\geq 0}(-1)^{k}\frac{t^{\alpha k}}{\Gamma(\alpha k+1)},\quad t\geq 0,\quad E\_{\alpha}(z):=\sum\_{n=0}^{\infty}\frac{z^{n}}{\Gamma(\alpha n+1)},\quad\alpha>0,\quad z\in\mathbb{C}. |  |

In the limiting cases α=1\alpha=1 and α=2\alpha=2, eα​(t)e\_{\alpha}(t) are elementary functions, namely e1​(t)=e−tande2​(t)=cos⁡t.e\_{1}(t)=e^{-t}\quad\text{and}\quad e\_{2}(t)=\cos t.
Integral representations of the Mittag-Leffler function EαE\_{\alpha} were first established in [Pollard1948](https://arxiv.org/html/2511.03474v1#bib.bib1) , followed by further results in [GorMain2000](https://arxiv.org/html/2511.03474v1#bib.bib33) , where they were connected by the Laplace transform. For instance, (see (F.12) in [GorMain2000](https://arxiv.org/html/2511.03474v1#bib.bib33) ), the Laplace transform of Eα​(−a​tα)E\_{\alpha}(-at^{\alpha}), with a∈ℂa\in\mathbb{C}, is given by:
  
LEα​(−a​tα)​(z)=zα−1zα+a,z∈ℂ,ℜ⁡(z)>|a|1/α,α>0.L\_{E\_{\alpha}(-at^{\alpha})}(z)=\frac{z^{\alpha-1}}{z^{\alpha}+a},\quad z\in\mathbb{C},\;\Re(z)>|a|^{1/\alpha},\quad\alpha>0.
From this, we can deduce the Laplace transform of eαe\_{\alpha}, which is given by: Leα​(z)=zα−1zα+1,z∈ℂ,ℜ⁡(z)>1,α>0.L\_{e\_{\alpha}}(z)=\frac{z^{\alpha-1}}{z^{\alpha}+1},\quad z\in\mathbb{C},\;\Re(z)>1,\quad\alpha>0.
Here, we define zα:=|z|α​ei​α​arg⁡(z)z^{\alpha}:=|z|^{\alpha}e^{i\alpha\arg(z)}, where −π<arg⁡(z)<π-\pi<\arg(z)<\pi, that is in the complex
z-plane cut along the negative real axis

#### 5.1.1 α\alpha-fractional kernels for α∈ℝ+∗\alpha\!\in\mathbb{R}^{\*}\_{+}

###### Proposition 5.1.

The followings hold for the the alternate Mittag-Leffler function for any t≥0t\geq 0:

1. 1.

   If α∈ℝ+∗∖ℕ∗\alpha\!\in\mathbb{R}^{\*}\_{+}\setminus\mathbb{N}^{\*}, eα​(t)=Fα​(t)+Gα​(t)e\_{\alpha}(t)=F\_{\alpha}(t)+G\_{\alpha}(t) where
   Fα​(t):=∫0+∞e−t​u​Hα​(u)​𝑑uF\_{\alpha}(t):=\int\_{0}^{+\infty}e^{-tu}H\_{\alpha}(u)\,du with ∀u∈ℝ+,\forall\,u\!\in\mathbb{R}\_{+},\;
     
   Hα​(u)=sin⁡(α​π)π​uα−1u2​α+2​uα​cos⁡(π​α)+1H\_{\alpha}(u)=\frac{\sin(\alpha\pi)}{\pi}\frac{u^{\alpha-1}}{u^{2\alpha}+2u^{\alpha}\cos(\pi\alpha)+1} and Gα​(t):=2α​∑n=0⌊α−12⌋exp⁡[t​cos⁡((2​n+1)​πα)]​cos⁡[t​sin⁡((2​n+1)​πα)]G\_{\alpha}(t):=\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\cos\left[t\sin\left(\frac{(2n+1)\pi}{\alpha}\right)\right]
2. 2.

   If α∈ℕ∗\alpha\in\mathbb{N}^{\*}, eα​(t)=Gα​(t)=2α​∑n=0⌊α−12⌋exp⁡[t​cos⁡((2​n+1)​πα)]​cos⁡[t​sin⁡((2​n+1)​πα)]e\_{\alpha}(t)=G\_{\alpha}(t)=\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\cos\left[t\sin\left(\frac{(2n+1)\pi}{\alpha}\right)\right]

The result or representation of the above proposition [5.1](https://arxiv.org/html/2511.03474v1#S5.Thmprop1 "Proposition 5.1. ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") is an extension of the case α∈(0,2)\alpha\in(0,2) studied in [GorenfloMainardi1997](https://arxiv.org/html/2511.03474v1#bib.bib23)  to the general case α∈ℝ∖ℕ\alpha\!\in\mathbb{R}\setminus\mathbb{N}. The second claim is straigthforward as the function HαH\_{\alpha} vanishes identically if α\alpha is an integer.

Proof.
Based on the inverse Laplace transform (Bromwich-Mellin formula 999on the Bromwich path, i.e., a line Re​{z}=a\text{Re}\{z\}=a with a≥1a\geq 1, and Im​{z}\text{Im}\{z\} running from −∞-\infty to +∞+\infty.
), we have the below representation as a Laplace inverse integral: For γ\gamma larger than the real parts of all poles of the integrand,

|  |  |  |  |
| --- | --- | --- | --- |
|  | eα(t)=12​π​i∫Br​(γ,∞)ez​tzα−1zα+1dz,=12​i​π∫z=γ−i⋅∞z=γ+i⋅∞ez​tzα−1zα+1dz=12​π​ilimR→+∞∫Br​(γ,R)ez​tzα−1zα+1dz.e\_{\alpha}(t)=\frac{1}{2\pi i}\int\_{\textit{Br}(\gamma,\infty)}e^{zt}\frac{z^{\alpha-1}}{z^{\alpha}+1}\,dz,=\frac{1}{2i\pi}\int\_{z=\gamma-i\cdot\infty}^{z=\gamma+i\cdot\infty}e^{zt}\frac{z^{\alpha-1}}{z^{\alpha}+1}dz=\frac{1}{2\pi i}\lim\_{R\to+\infty}\int\_{\textit{Br}(\gamma,R)}e^{zt}\frac{z^{\alpha-1}}{z^{\alpha}+1}\,dz. |  | (5.45) |

Let Jα​(t,⋅):z→ez​t​zα−1zα+1J\_{\alpha}(t,\cdot):z\to e^{zt}\frac{z^{\alpha-1}}{z^{\alpha}+1} be the integrand of the above representaion.
The relevant poles of Jα​(t,⋅)J\_{\alpha}(t,\cdot) or rather zα−1zα+1\frac{z^{\alpha-1}}{z^{\alpha}+1} is the set 𝕊:={zn=exp⁡(i​(2​n+1)​πα),n=0,⋯,⌊α−1⌋}\mathbb{S}:=\{z\_{n}=\exp\left(i\frac{(2n+1)\pi}{\alpha}\right),n=0,\cdots,\lfloor\alpha-1\rfloor\}. Jα​(t,⋅)J\_{\alpha}(t,\cdot) is thus holomorphic/analytic on ℂ∖𝕊\mathbb{C}\setminus\mathbb{S}.
And since 0 is a brand-point of the integrand Jα​(t,⋅)J\_{\alpha}(t,\cdot), we consider Γγ,δ,R\Gamma\_{\gamma,\delta,R} the Jordan contour (see Figure [1](https://arxiv.org/html/2511.03474v1#S5.F1 "Figure 1 ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) defined as the union of the below-represented several distinct paths:

Γγ,δ,R=Br​(γ,R)∪C+∪CR+∪(−H​(δ,1R))∪CR−∪C−,\Gamma\_{\gamma,\delta,R}=\textit{Br}(\gamma,R)\cup C^{+}\cup C\_{R}^{+}\cup(-\textit{H}(\delta,\frac{1}{R}))\cup C\_{R}^{-}\cup C^{-},

* —

  H​(δ,1R)\textit{H}(\delta,\frac{1}{R}) is the Hankel Contour given by
  H​(δ,1R):=[−R+i​δ,−c+i​δ]∪C1R∪[−R−i​δ,−c−i​δ],\textit{H}(\delta,\frac{1}{R}):=[-R+i\delta,-c+i\delta]\cup C\_{\frac{1}{R}}\cup[-R-i\delta,-c-i\delta], where C1RC\_{\frac{1}{R}} is the small circular arc |s|=1R|s|=\frac{1}{R}.
* —

  Br​(γ,R)\textit{Br}(\gamma,R), the truncated Bromwich Path i.e. Br​(γ,R):=[γ−i​R,γ+i​R]\textit{Br}(\gamma,R):=[\gamma-iR,\gamma+iR], where γ≥1\gamma\geq 1 and Re​{z}=γ\text{Re}\{z\}=\gamma, with Im​{z}∈[−R,R]\text{Im}\{z\}\in[-R,R].
* —

  C+:=[γ+i​R,i​R]C^{+}:=[\gamma+iR,iR] and C−:=[−i​R,γ−i​R]C^{-}:=[-iR,\gamma-iR].
* —

  CR+C\_{R}^{+} and CR−C\_{R}^{-} denote the upper and lower semicircular arcs, respectively, of a circle of radius RR; CR+C\_{R}^{+} runs from i​RiR to −R+i​δ-R+i\delta, and CR−C\_{R}^{-} from −R−i​δ-R-i\delta to −i​R-iR.

ℜ⁡(z)\Re(z)ℑ⁡(z)\Im(z)Br​(γ,R)\textit{Br}(\gamma,R)C+C^{+}C−C^{-}CR+C\_{R}^{+}CR−C\_{R}^{-}H(δ,1R)(\delta,\tfrac{1}{R})

Figure 1: Jordan contour Γγ,δ,R\Gamma\_{\gamma,\delta,R}.

For small values of δ\delta, large values of RR, and γ≥1\gamma\geq 1, the Jordan contour Γγ,δ,R\Gamma\_{\gamma,\delta,R} encloses all poles of Jα​(t,⋅)J\_{\alpha}(t,\cdot). Therefore, by the Jordan-Cauchy Residue Theorem, we have:

|  |  |  |
| --- | --- | --- |
|  | ∑z∈ℂ∖{−1}:zα=−1Res​(Jα​(t,⋅),z)=12​π​i​∮Γγ,δ,RJα​(t,z)​𝑑z=12​π​i​∫Br​(γ,R)Jα​(t,z)​𝑑z+12​π​i​∫C+Jα​(t,z)​𝑑z\displaystyle\sum\_{z\in\mathbb{C}\setminus\{-1\}:z^{\alpha}=-1}\text{Res}(J\_{\alpha}(t,\cdot),z)=\frac{1}{2\pi i}\oint\_{\Gamma\_{\gamma,\delta,R}}J\_{\alpha}(t,z)\,dz=\frac{1}{2\pi i}\int\_{\textit{Br}(\gamma,R)}J\_{\alpha}(t,z)\,dz+\frac{1}{2\pi i}\int\_{C^{+}}J\_{\alpha}(t,z)\,dz |  |
|  |  |  |
| --- | --- | --- |
|  | +12​π​i​∫CR+Jα​(t,z)​𝑑z−12​π​i​∫H​(δ,1R)Jα​(t,z)​𝑑z+12​π​i​∫CR−Jα​(t,z)​𝑑z+12​π​i​∫C−Jα​(t,z)​𝑑z.\displaystyle\qquad\hskip 42.67912pt+\frac{1}{2\pi i}\int\_{C\_{R}^{+}}J\_{\alpha}(t,z)\,dz-\frac{1}{2\pi i}\int\_{\textit{H}(\delta,\frac{1}{R})}J\_{\alpha}(t,z)\,dz+\frac{1}{2\pi i}\int\_{C\_{R}^{-}}J\_{\alpha}(t,z)\,dz+\frac{1}{2\pi i}\int\_{C^{-}}J\_{\alpha}(t,z)\,dz. |  |

Taking the limit as R→∞R\to\infty and δ→0\delta\to 0, we may decompose ([5.45](https://arxiv.org/html/2511.03474v1#S5.E45 "In 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | eα​(t)\displaystyle e\_{\alpha}(t) | :=12​π​i​limR→+∞∫Br​(γ,R)Jα​(t,z)​𝑑z=∑z∈ℂ∖{−1}:zα=−1Res​(Jα​(t,⋅),z)+12​π​i​limR→+∞limδ→0∫H​(δ,1R)Jα​(t,z)​𝑑z\displaystyle:=\frac{1}{2\pi i}\lim\_{R\to+\infty}\int\_{\textit{Br}(\gamma,R)}J\_{\alpha}(t,z)\,dz=\sum\_{z\in\mathbb{C}\setminus\{-1\}:z^{\alpha}=-1}\text{Res}(J\_{\alpha}(t,\cdot),z)+\frac{1}{2\pi i}\lim\_{R\to+\infty}\lim\_{\delta\to 0}\int\_{\textit{H}(\delta,\frac{1}{R})}J\_{\alpha}(t,z)\,dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​π​i​(limR→+∞∫C+Jα​(t,z)​𝑑z+limR→+∞∫CR+Jα​(t,z)​𝑑z+limR→+∞∫CR−Jα​(t,z)​𝑑z+limR→+∞∫C−Jα​(t,z)​𝑑z).\displaystyle-\frac{1}{2\pi i}\left(\lim\_{R\to+\infty}\int\_{C^{+}}J\_{\alpha}(t,z)\,dz+\lim\_{R\to+\infty}\int\_{C\_{R}^{+}}J\_{\alpha}(t,z)\,dz+\lim\_{R\to+\infty}\int\_{C\_{R}^{-}}J\_{\alpha}(t,z)\,dz+\lim\_{R\to+\infty}\int\_{C^{-}}J\_{\alpha}(t,z)\,dz\right). |  |

We now examine these six terms. The contribution from the Hankel path is given by 12​π​i​∫H​(δ,1R)Jα​(t,z)​𝑑z\frac{1}{2\pi i}\int\_{\textit{H}(\delta,\frac{1}{R})}J\_{\alpha}(t,z)\,dz, whose limit coincides with the usual contour representation of the Mittag-Leffler function for α∈(0,1)\alpha\in(0,1).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​π​i∫H​(δ,1R)ez​tzα−1zα+1dz=R→+∞,δ→0∫0+∞e−t​uHα(u)du=LHα(t)=:Fα(t).\frac{1}{2\pi i}\int\_{\textit{H}(\delta,\frac{1}{R})}e^{zt}\frac{z^{\alpha-1}}{z^{\alpha}+1}\,dz\overset{R\to+\infty,\delta\to 0}{=}\int\_{0}^{+\infty}e^{-tu}H\_{\alpha}(u)\,du=L\_{H\_{\alpha}}(t)=:F\_{\alpha}(t). |  | (5.46) |

where a synthetic formula was found for HαH\_{\alpha} in [GorMain2000](https://arxiv.org/html/2511.03474v1#bib.bib33)  (see (F.22) p.31, see also [Mainardi2014](https://arxiv.org/html/2511.03474v1#bib.bib32)  in the case 0<α<10<\alpha<1).

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀u∈ℝ+,Hα​(u)=−12​π⋅2​ℑ⁡m​(zα−1zα+1)|z=uei​π=sin⁡(α​π)π​uα−1u2​α+2​uα​cos⁡(π​α)+1\forall\,u\!\in\mathbb{R}\_{+},\;H\_{\alpha}(u)=-\frac{1}{2\pi}\cdot 2\,\Im{\rm m}\Big(\frac{z^{\alpha-1}}{z^{\alpha}+1}\Big)\_{|z=ue^{i\pi}}=\frac{\sin(\alpha\pi)}{\pi}\frac{u^{\alpha-1}}{u^{2\alpha}+2u^{\alpha}\cos(\pi\alpha)+1} |  | (5.47) |

Note that this representation of FαF\_{\alpha} in term of the Laplace transform of a non-negative Lebesgue integrable function (see Equation ([5.46](https://arxiv.org/html/2511.03474v1#S5.E46 "In 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) above) was first established in [Pollard1948](https://arxiv.org/html/2511.03474v1#bib.bib1) .

Also note that the function HαH\_{\alpha} vanishes identically if α\alpha is an integer.
The limit of the other integrals vanishes. In fact:
|∫CR+Jα​(t,z)​dz|≤∫π2πR​|Jα​(t,ei​θ)|​dθ\left\lvert\penalty 10000\ \int\_{C\_{R}^{+}}J\_{\alpha}(t,z)\,\mathrm{d}z\,\right\rvert\leq\int\_{\frac{\pi}{2}}^{\pi}R\lvert J\_{\alpha}(t,e^{i\theta})\rvert\,\mathrm{d}\theta\, and |Jα​(t,ei​θ)|≤Rα−1Rα−1​et​R​cos⁡(θ)≤Rα−1Rα−1​et​R​(−2π​θ+1)\lvert J\_{\alpha}(t,e^{i\theta})\rvert\,\leq\frac{R^{\alpha-1}}{R^{\alpha}-1}e^{tR\cos(\theta)}\leq\frac{R^{\alpha-1}}{R^{\alpha}-1}e^{tR(-\frac{2}{\pi}\theta+1)} where in the last inequality, we used the trick cos⁡(θ)≤−2π​θ+1∀θ∈[π2,π]\cos(\theta)\leq-\frac{2}{\pi}\theta+1\quad\forall\theta\in[\frac{\pi}{2},\pi].
Consequently, |∫CR+Jα​(t,z)​dz|≤Rα−1Rα−1×π−2​t​R​[et​R​(−2π​θ+1)]θ=π2θ=π=π​Rα2​t​(Rα+1−R)​(1−e−t​R)⟶R→∞0\left\lvert\penalty 10000\ \int\_{C\_{R}^{+}}J\_{\alpha}(t,z)\,\mathrm{d}z\,\right\rvert\leq\frac{R^{\alpha-1}}{R^{\alpha}-1}\times\frac{\pi}{-2tR}\left[e^{tR(-\frac{2}{\pi}\theta+1)}\right]\_{\theta=\frac{\pi}{2}}^{\theta=\pi}=\frac{\pi R^{\alpha}}{2t(R^{\alpha+1}-R)}(1-e^{-tR})\stackrel{{\scriptstyle R\to\infty}}{{\longrightarrow}}0\,
Likewise limR→+∞|∫CR−Jα​(t,z)​dz|=0\lim\_{R\to+\infty}\left\lvert\penalty 10000\ \int\_{C\_{R}^{-}}J\_{\alpha}(t,z)\,\mathrm{d}z\,\right\rvert=0. Moreover:
∫C+Jα​(t,z)​𝑑z=∫γ+i​Ri​RJα​(t,z)​𝑑z=∫γ0Jα​(t,x+i​R)​𝑑x\int\_{C^{+}}J\_{\alpha}(t,z)\,dz=\int\_{\gamma+iR}^{iR}J\_{\alpha}(t,z)\,dz=\int\_{\gamma}^{0}J\_{\alpha}(t,x+iR)\,dx.
Now, observe that:
|Jα​(t,x+i​R)|≤(x2+R2)α−12(x2+R2)α2−1​et​x≤et​x​(γ2+R2)α−12Rα−1.\lvert J\_{\alpha}(t,x+iR)\rvert\,\leq\frac{(x^{2}+R^{2})^{\frac{\alpha-1}{2}}}{(x^{2}+R^{2})^{\frac{\alpha}{2}}-1}e^{tx}\leq e^{tx}\frac{(\gamma^{2}+R^{2})^{\frac{\alpha-1}{2}}}{R^{\alpha}-1}.
As a consequence, |∫C+Jα​(t,z)​dz|≤(γ2+R2)α−12Rα−1​∫γ0et​x​dx⟶R→∞0.\left\lvert\penalty 10000\ \int\_{C^{+}}J\_{\alpha}(t,z)\,\mathrm{d}z\,\right\rvert\leq\frac{(\gamma^{2}+R^{2})^{\frac{\alpha-1}{2}}}{R^{\alpha}-1}\int\_{\gamma}^{0}e^{tx}\,\mathrm{d}x\,\stackrel{{\scriptstyle R\to\infty}}{{\longrightarrow}}0.
Likewise for limR→+∞|∫C−Jα​(t,z)​dz|=0.\lim\_{R\to+\infty}\left\lvert\penalty 10000\ \int\_{C^{-}}J\_{\alpha}(t,z)\,\mathrm{d}z\,\right\rvert=0.
Finally,

|  |  |  |
| --- | --- | --- |
|  | Gα​(t):=∑z∈ℂ∖{−1}:zα=−1Res​(Jα​(t,⋅),z)=∑zn∈𝕊Res​(Jα​(t,⋅),zn)=∑n=0⌊α−1⌋ezn​t​Res​[zα−1zα+1]zn=1α​∑n=0⌊α−1⌋ezn​t,G\_{\alpha}(t):=\sum\_{z\in\mathbb{C}\setminus\{-1\}:z^{\alpha}=-1}\text{Res}(J\_{\alpha}(t,\cdot),z)=\sum\_{z\_{n}\in\mathbb{S}}\text{Res}(J\_{\alpha}(t,\cdot),z\_{n})=\sum\_{n=0}^{\lfloor\alpha-1\rfloor}e^{z\_{n}t}\,\text{Res}\left[\frac{z^{\alpha-1}}{z^{\alpha}+1}\right]\_{z\_{n}}=\frac{1}{\alpha}\sum\_{n=0}^{\lfloor\alpha-1\rfloor}e^{z\_{n}t}, |  |

Note that, ezn​t+ez¯n​t=eRe​{zn}​t​(eIm​{zn}​t+e−Im​{zn}​t)=2​eRe​{zn}​t​cos⁡(Im​{zn}​t)e^{z\_{n}t}+e^{\bar{z}\_{n}t}=e^{\text{Re}\{z\_{n}\}t}\left(e^{\text{Im}\{z\_{n}\}t}+e^{-\text{Im}\{z\_{n}\}t}\right)=2e^{\text{Re}\{z\_{n}\}t}\cos\left(\text{Im}\{z\_{n}\}t\right) and
  
∑zn∈𝕊Res​(Jα​(t,⋅),zn)=1α​∑n=0⌊α−1⌋ezn​t=1α​∑n=0⌊α−12⌋(ezn​t+ez¯n​t).\sum\_{z\_{n}\in\mathbb{S}}\text{Res}(J\_{\alpha}(t,\cdot),z\_{n})=\frac{1}{\alpha}\sum\_{n=0}^{\lfloor\alpha-1\rfloor}e^{z\_{n}t}=\frac{1}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\left(e^{z\_{n}t}+e^{\bar{z}\_{n}t}\right).
As a consequence,

|  |  |  |
| --- | --- | --- |
|  | Gα​(t):=∑z∈ℂ∖{−1}:zα=−1Res​(Jα​(t,⋅),z)=1α​∑n=0⌊α−1⌋ezn​t=2α​∑n=0⌊α−12⌋exp⁡[t​cos⁡((2​n+1)​πα)]​cos⁡[t​sin⁡((2​n+1)​πα)]G\_{\alpha}(t):=\sum\_{z\in\mathbb{C}\setminus\{-1\}:z^{\alpha}=-1}\text{Res}(J\_{\alpha}(t,\cdot),z)=\frac{1}{\alpha}\sum\_{n=0}^{\lfloor\alpha-1\rfloor}e^{z\_{n}t}=\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\cos\left[t\sin\left(\frac{(2n+1)\pi}{\alpha}\right)\right] |  |

Remark: 1. For 0<α<10<\alpha<1, there are no relevant poles since |arg⁡(zk)|>π|\arg(z\_{k})|>\pi, so Gα​(t)≡0G\_{\alpha}(t)\equiv 0, and we obtain eα​(t)=Fα​(t),for0<α<1.e\_{\alpha}(t)=F\_{\alpha}(t),\;\text{for}\quad 0<\alpha<1. For 1<α<21<\alpha<2, there are exactly two relevant poles, z0=exp⁡(i​π/α)z\_{0}=\exp(i\pi/\alpha) and z−1=exp⁡(−i​π/α)=z¯0z\_{-1}=\exp(-i\pi/\alpha)=\bar{z}\_{0}, located in the left half-plane. In this case, we have Gα​(t)=2α​et​cos⁡(πα)​cos⁡(t​sin⁡(πα))G\_{\alpha}(t)=\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\cos\left(t\sin\left(\frac{\pi}{\alpha}\right)\right) and eα​(t)=∫0+∞e−t​u​Hα​(u)​𝑑u+2α​et​cos⁡(πα)​cos⁡(t​sin⁡(πα)).e\_{\alpha}(t)=\int\_{0}^{+\infty}e^{-tu}H\_{\alpha}(u)\,du+\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\cos\left(t\sin\left(\frac{\pi}{\alpha}\right)\right).
It is clear that the function eα​(t)e\_{\alpha}(t) oscillates in an evanescent manner to 0 as t→+∞t\to+\infty.
We note that this function exhibits oscillations with circular frequency and an exponentially decaying amplitude (see Figure [3](https://arxiv.org/html/2511.03474v1#S5.F3 "Figure 3 ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).
  
Note that, the above expression of eαe\_{\alpha} is the same for 2<α<32<\alpha<3 with the only difference that the two poles are now located in the right haft plane, and so providing amplified oscillations.

2. In the case 2<α<+∞2<\alpha<+\infty ,
however, certains poles are located in the right half plane, so providing amplified
oscillations. This common instability for α>2\alpha>2 is the reason why
we will limit ourselves to consider α\alpha in the range 0<α<20<\alpha<2 as highlighted by the below proposition.

![Refer to caption](Images/courbes_e_alpha_f_alpha_2.png)


Figure 2: Curves of Rα,λ​(t)R\_{\alpha,\lambda}(t) and fα,λ​(t)f\_{\alpha,\lambda}(t) for different values of α∈[12,1)\alpha\in[\frac{1}{2},1)

![Refer to caption](Images/courbes_e_alpha_f_alpha.png)


Figure 3: Curves of Rα,λ​(t)R\_{\alpha,\lambda}(t) and fα,λ​(t)f\_{\alpha,\lambda}(t) for different values of α∈(1,2)\alpha\in(1,2)

###### Proposition 5.1.

Let λ>0\lambda>0 and let α∈ℝ+∖ℕ\alpha\!\in\mathbb{R}^{+}\setminus\mathbb{N}.

(a)(a) The function (−1)⌊α⌋​Fα(-1)^{\lfloor\alpha\rfloor}F\_{\alpha} is completely monotonic(thus convex), hence infinitely differentiable on ℝ+∗\mathbb{R}\_{+}^{\*}.

(b)(b) The λ\lambda-resolvent Rα,λR\_{\alpha,\lambda} satisfies Rα,1=eαR\_{\alpha,1}=e\_{\alpha} and Rα,λ=Rα,1(λ1/α⋅)R\_{\alpha,\lambda}=R\_{\alpha,1}(\lambda^{1/\alpha}\cdot). The function Rα,λR\_{\alpha,\lambda} is infinitely differentiable i.e. 𝒞∞\mathcal{C}^{\infty} on (0,+∞)(0,+\infty). Moreover Rα,λ​(0)=1R\_{\alpha,\lambda}(0)=1, Rα,λ∈ℒr​(Leb1)R\_{\alpha,\lambda}\!\in{\cal L}^{r}({\rm Leb}\_{1}) for every r>1αr>\frac{1}{\alpha} and α≤2\alpha\leq 2.

fα,λ​(t):=−Rα,λ′​(t)f\_{\alpha,\lambda}(t):=-R^{\prime}\_{\alpha,\lambda}(t) is infinitely differentiable and satisfy : ∀t>0,fα,λ(t)=\forall\,t>0,\quad f\_{\alpha,\lambda}(t)=

|  |  |  |
| --- | --- | --- |
|  | λ1α​(∫0+∞e−λ1α​t​u​u​Hα​(u)​𝑑u−2α​∑n=0⌊α−12⌋exp⁡[t​λ1α​cos⁡((2​n+1)​πα)]​cos⁡[t​λ1α​sin⁡((2​n+1)​πα)−(2​n+1)​πα])\lambda^{\frac{1}{\alpha}}\left(\int\_{0}^{+\infty}e^{-\lambda^{\frac{1}{\alpha}}tu}uH\_{\alpha}(u)du-\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\lambda^{\frac{1}{\alpha}}\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\cos\left[t\lambda^{\frac{1}{\alpha}}\sin\left(\frac{(2n+1)\pi}{\alpha}\right)-\frac{(2n+1)\pi}{\alpha}\right]\right) |  |

so that, Rα,λR\_{\alpha,\lambda} converges to a∈[0,1)a\in[0,1) and fα,λ∈ℒ2​β​(Leb1)f\_{\alpha,\lambda}\!\in{\cal L}^{2\beta}({\rm Leb}\_{1}) for every β>0\beta>0
provided α∈(0,2)\alpha\in(0,2).

(c)(c) if α≥2\alpha\geq 2 the ℒ2​(ℝ+){\cal L}^{2}(\mathbb{R}\_{+})-ϑ\vartheta-Hölder continuity of fα,λf\_{\alpha,\lambda} as stated in Assumption [4.5](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem5 "Assumption 4.5 (Integrability and Uniform Hölder continuity). ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") does not holds.

Furthermore, the function Rα,λR\_{\alpha,\lambda} satisfies the assumptions 𝒦\mathcal{K} (i), specifically, that Rα,λR\_{\alpha,\lambda} converges to 0, along with the function fα,λf\_{\alpha,\lambda} satisfying the assumption [4.5](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem5 "Assumption 4.5 (Integrability and Uniform Hölder continuity). ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") 101010Uniform Hölder continuity or Hölder regularity with exponent ϑ\vartheta for the function fα,λf\_{\alpha,\lambda}, ensuring controlled behavior as tt and t+δt+\delta become arbitrarily close. (for the weak functional behavior property) if and only if α∈(0,2)\alpha\in(0,2).

###### Proposition 5.2 (α\alpha-fractional kernels 1<α<21<\alpha<2).

Let λ>0\lambda>0 and let α∈(1,2)\alpha\!\in(1,2).

(a)(a) The λ\lambda-resolvent Rα,λR\_{\alpha,\lambda} satisfies Rα,1=eαR\_{\alpha,1}=e\_{\alpha} and Rα,λ=Rα,1(λ1/α⋅)R\_{\alpha,\lambda}=R\_{\alpha,1}(\lambda^{1/\alpha}\cdot). The function eαe\_{\alpha} and thus Rα,λR\_{\alpha,\lambda} are infinitely differentiable i.e. 𝒞∞\mathcal{C}^{\infty} on (0,+∞)(0,+\infty)) with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀k∈ℕ,eα(k)​(t)=Fα(k)​(t)+Gα(k)​(t)​where​Fα(k)​(t)=∫0+∞e−t​u​Hα(k)​(u)​𝑑u\forall k\in\mathbb{N},\quad e^{(k)}\_{\alpha}(t)=F^{(k)}\_{\alpha}(t)+G^{(k)}\_{\alpha}(t)\quad\text{where}\quad F^{(k)}\_{\alpha}(t)=\int\_{0}^{+\infty}e^{-tu}H^{(k)}\_{\alpha}(u)\,du\; |  | (5.48) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hα(k)​(u):=(−1)k​sin⁡(α​π)π​uα−1+ku2​α+2​uα​cos⁡(α​π)+1​and​Gα(k)​(t)=2α​et​cos⁡(πα)​cos⁡[t​sin⁡(πα)−k​πα].H^{(k)}\_{\alpha}(u):=(-1)^{k}\frac{\sin(\alpha\pi)}{\pi}\frac{u^{\alpha-1+k}}{u^{2\alpha}+2u^{\alpha}\cos(\alpha\pi)+1}\;\text{and}\;G^{(k)}\_{\alpha}(t)=\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\cos\left[t\sin\left(\frac{\pi}{\alpha}\right)-\frac{k\pi}{\alpha}\right]. |  | (5.49) |

Moreover Rα,λ​(0)=1R\_{\alpha,\lambda}(0)=1, Rα,λ​(t)≤1∀t≥0R\_{\alpha,\lambda}(t)\leq 1\quad\forall t\geq 0, Rα,λR\_{\alpha,\lambda} converges to 0.
Rα,λ∈ℒr​(Leb1)R\_{\alpha,\lambda}\!\in{\cal L}^{r}({\rm Leb}\_{1}) for every r>1αr>\frac{1}{\alpha} and
fα,λ:=−Rα,λ′f\_{\alpha,\lambda}:=-R^{\prime}\_{\alpha,\lambda} is infinitely differentiable , converges to 0 and satisfy:

|  |  |  |
| --- | --- | --- |
|  | ∀t>0,fα,λ​(t):=−Rα,λ′​(t)=λ1α​(∫0+∞e−λ1α​t​u​u​Hα​(u)​𝑑u−2α​et​λ1α​cos⁡(πα)​cos⁡[t​λ1α​sin⁡(πα)−πα]).\forall\,t>0,\quad f\_{\alpha,\lambda}(t):=-R^{\prime}\_{\alpha,\lambda}(t)=\lambda^{\frac{1}{\alpha}}\left(\int\_{0}^{+\infty}e^{-\lambda^{\frac{1}{\alpha}}tu}uH\_{\alpha}(u)du-\frac{2}{\alpha}e^{t\lambda^{\frac{1}{\alpha}}\cos\left(\frac{\pi}{\alpha}\right)}\cos\left[t\lambda^{\frac{1}{\alpha}}\sin\left(\frac{\pi}{\alpha}\right)-\frac{\pi}{\alpha}\right]\right). |  |

(b)(b) Moreover, if α∈(1,2)\alpha\!\in(1,2), fα,λ∈ℒ2​β​(Leb1)f\_{\alpha,\lambda}\!\in{\cal L}^{2\beta}({\rm Leb}\_{1}) for every β>0\beta>0 and for i∈{1,2}i\in\{1,2\}, for every ϑ∈(0,α−𝟏i=2i)\vartheta\!\in\big(0,\alpha-\frac{\mathbf{1}\_{i=2}}{i}\big), there exists a real constant Cϑ,λ>0C\_{\vartheta,\lambda}>0 such that

∀δ>0,[∫0+∞(fα,λ​(t+δ)−fα,λ​(t))i​𝑑t]1/i≤Cϑ,λ​δϑ.\forall\,\delta>0,\quad\left[\int\_{0}^{+\infty}\big(f\_{\alpha,\lambda}(t+\delta)-f\_{\alpha,\lambda}(t)\big)^{i}\,dt\right]^{1/i}\leq C\_{\vartheta,\lambda}\delta^{\vartheta}.

For clarity and conciseness, the proofs of Propositions [5.1](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem1 "Proposition 5.1. ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and [5.2](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem2 "Proposition 5.2 (𝛼-fractional kernels 1<𝛼<2). ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") are postponed to Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

###### Theorem 5.3.

Let α∈(1,32)\alpha\in\left(1,\frac{3}{2}\right) (and more generally α∈(12,32)\alpha\in\left(\frac{1}{2},\frac{3}{2}\right)), let K​(t)=Kα​(t)=tα−1Γ​(α)K(t)=K\_{\alpha}(t)=\frac{t^{\alpha-1}}{\Gamma(\alpha)}, t>0t>0 the fractional kernel, let σ​(t,x):=ς​(t)​σ​(x)\sigma(t,x):=\varsigma(t)\sigma(x) with σ\sigma a Lipschitz continuous function given by equation ([3.32](https://arxiv.org/html/2511.03474v1#S3.E32 "In Example 3.10 (Polynomial of degree 2). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), thus satisfying a relation of the type ([4.33](https://arxiv.org/html/2511.03474v1#S4.E33 "In Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) (S​Lσ)(SL\_{\sigma}) with κ:=κ2>0\kappa:=\kappa\_{2}>0, let c∈(0,1κ2)c\in\left(0,\frac{1}{\kappa\_{2}}\right) with ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, λ>0\lambda>0 and let X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) such that 𝔼​[X0]=x∞\mathbb{E}[X\_{0}]=x\_{\infty} and V​a​r​(X0)=v0=c​σ2​(x∞)1−c​κ2.Var(X\_{0})=v\_{0}=\frac{c\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}. Then,

1. 1.

   For fractional kernels KαK\_{\alpha} with 1<α<21<\alpha<2, the solution (Xt)t≥0(X\_{t})\_{t\geq 0} to the Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0X\_{0} has a fake
   stationary regime of type I in the sense that:

   ∀t≥0,𝔼​Xt=x∞,Var​(Xt)=v0=c​σ2​(x∞)1−c​κ2​ and 𝔼​σ2​(Xt)=σ¯02=σ2​(x∞)1−c​κ2.\forall\,t\geq 0,\qquad\mathbb{E}\,X\_{t}=x\_{\infty},\quad{\rm Var}(X\_{t})=v\_{0}=\frac{c\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}\mbox{ and }\quad\mathbb{E}\,\sigma^{2}(X\_{t})=\bar{\sigma}\_{0}^{2}=\frac{\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}.
2. 2.

   If a=0a=0 or ϕ∞=0\phi\_{\infty}=0, ∀X0′∈L2​(ℙ)\forall X\_{0}^{\prime}\in L^{2}(\mathbb{P}), a solution to ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0′X\_{0}^{\prime} satisfies ‖Xt′−Xt‖2​→t→∞​0\|X\_{t}^{\prime}-X\_{t}\|\_{2}\underset{t\to\infty}{\to}0
3. 3.

   The family of shifted processes Xt+⁣⋅,t≥0X\_{t+\cdot},t\geq 0, is CC-tight as t→+∞t\to+\infty and its (functional) limiting distributions are all L2L^{2}-stationary processes with covariance function C∞C\_{\infty} given by ([4.42](https://arxiv.org/html/2511.03474v1#S4.E42 "In Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).

Proof. (1), (2) are consequences of Proposition [3.11](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem11 "Proposition 3.11. ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
If 0<ϑ<α−120<\vartheta<\alpha-\frac{1}{2} and β>1\beta>1, Theorem [4.6](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem6 "Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") applies.

### 5.2 The function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} solution of the stabilizer equation when α∈(0,2)\alpha\in(0,2)

In this section we want to compute ςλ,c\varsigma\_{\lambda,c} as a power series in tk​αt^{k\alpha}. To this end we rely on the Laplace version of the equation (Eλ,cE\_{\lambda,c}) in ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) satisfied by ςλ,c2\varsigma^{2}\_{\lambda,c} : c​λ2​(1−(ϕ−fλ∗ϕ)2​(t))=(fλ2∗ς2)​(t)​∀t≥0,\,c\lambda^{2}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=(f\_{\lambda}^{2}\*\varsigma^{2})(t)\;\forall\,t\geq 0,
for which the laplace transform is given by equation ([3.26](https://arxiv.org/html/2511.03474v1#S3.E26 "In Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) in Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"):

∀t>0,t​Lfλ2​(t).Lς2​(t)=−2​c​λ2​L(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t).\forall\,t>0,\quad t\,L\_{f^{2}\_{\lambda}}(t).L\_{\varsigma^{2}}(t)=-2\,c\lambda^{2}L\_{(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t).

Given the kernel Kα​(u)=uα−1Γ​(α)K\_{\alpha}(u)=\frac{u^{\alpha-1}}{\Gamma(\alpha)} and the expansion of the resolvents Rα,λR\_{\alpha,\lambda} and it derivative −fα,λ-f\_{\alpha,\lambda}, ∀t≥0,\forall t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rα,λ​(t)=∑k≥0(−1)k​λk​tα​kΓ​(α​k+1)=Eα​(−λ​tα),fα,λ​(t)=α​λ​tα−1​Eα′​(−λ​tα)=λ​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1)).R\_{\alpha,\lambda}(t)=\sum\_{k\geq 0}(-1)^{k}\frac{\lambda^{k}t^{\alpha k}}{\Gamma(\alpha k+1)}=E\_{\alpha}(-\lambda t^{\alpha}),\;f\_{\alpha,\lambda}(t)=\alpha\lambda t^{\alpha-1}E^{\prime}\_{\alpha}(-\lambda t^{\alpha})=\lambda t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\frac{\lambda^{k}t^{\alpha k}}{\Gamma(\alpha(k+1))}. |  | (5.50) |

Since ϕ​(t)−(fλ∗ϕ)​(t)=1−(fλ∗μ)tλ​x∞\phi(t)-(f\_{\lambda}\*\phi)(t)=1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda x\_{\infty}} we have ϕ​(t)−(fλ∗ϕ)​(t)∼01\phi(t)-(f\_{\lambda}\*\phi)(t)\stackrel{{\scriptstyle 0}}{{\sim}}1 and by Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (2)
(ϕ​(t)−(fλ∗ϕ)​(t))′∼0−μ​(0)λ​x∞​fλ​(t)(\phi(t)-(f\_{\lambda}\*\phi)(t))^{\prime}\stackrel{{\scriptstyle 0}}{{\sim}}-\frac{\mu(0)}{\lambda x\_{\infty}}f\_{\lambda}(t), so that: (ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t)∼0−μ​(0)λ​x∞​λ​tα−1Γ​(α) andfλ2​(t)∼0λ2​t2​(α−1)Γ​(α)2.(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}(t)\stackrel{{\scriptstyle 0}}{{\sim}}-\frac{\mu(0)}{\lambda x\_{\infty}}\frac{\lambda t^{\alpha-1}}{\Gamma(\alpha)}\quad\mbox{ and}\quad f^{2}\_{\lambda}(t)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{\lambda^{2}t^{2(\alpha-1)}}{\Gamma(\alpha)^{2}}.
  
It follows that – at least heuristically (111111We use here heuristically a dual version of the Hardy-Littlewood Tauberian theorem for Laplace transform, namely ς2​(t)∼0C​tγ\varsigma^{2}(t)\stackrel{{\scriptstyle 0}}{{\sim}}Ct^{\gamma}, γ>−1\gamma>-1, iff Lς2​(t)∼+∞C​t−(γ+1)​Γ​(γ+1).L\_{\varsigma^{2}}(t)\stackrel{{\scriptstyle+\infty}}{{\sim}}Ct^{-(\gamma+1)}\Gamma(\gamma+1). We refer to [BiGoTe1989](https://arxiv.org/html/2511.03474v1#bib.bib8) ; [DeHaanFerreira2006](https://arxiv.org/html/2511.03474v1#bib.bib26)  for a general theory of regular variation.) –

L(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t)∼+∞−λ​μ​(0)λ​x∞​t−α andLfλ2​(t)∼+∞λ2​Γ​(2​α−1)​t−(2​α−1)Γ​(α)2.L\_{(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t)\stackrel{{\scriptstyle+\infty}}{{\sim}}-\lambda\frac{\mu(0)}{\lambda x\_{\infty}}t^{-\alpha}\quad\mbox{ and}\quad L\_{f^{2}\_{\lambda}}(t)\stackrel{{\scriptstyle+\infty}}{{\sim}}\frac{\lambda^{2}\Gamma(2\alpha-1)t^{-(2\alpha-1)}}{\Gamma(\alpha)^{2}}.

This implies that Lς2​(t)∼+∞2​λ​c​μ​(0)λ​x∞​Γ​(α)2Γ​(2​α−1)​t−(2−α)L\_{\varsigma^{2}}(t)\stackrel{{\scriptstyle+\infty}}{{\sim}}2\lambda\,c\frac{\mu(0)}{\lambda x\_{\infty}}\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)}t^{-(2-\alpha)}
owing to Equation ([3.26](https://arxiv.org/html/2511.03474v1#S3.E26 "In Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).
This in turn suggests that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ς2​(t)∼02​λ​c​Γ​(α)2Γ​(2​α−1)​Γ​(2−α)​μ​(0)λ​x∞​t1−αso that​{(i)ς​(0)=0​ if ​α<1,(i​i)limt→0+ς​(t)=+∞​ if ​α>1​ provided ​μ​(0)λ​x∞>0.\varsigma^{2}(t)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{2\lambda c\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)\Gamma(2-\alpha)}\frac{\mu(0)}{\lambda x\_{\infty}}t^{1-\alpha}\quad\text{so that}\left\{\begin{array}[]{ll}(i)&\varsigma(0)=0\text{ if }\alpha<1,\\ (ii)&\lim\_{t\to 0^{+}}\varsigma(t)=+\infty\text{ if }\alpha>1\text{ provided }\frac{\mu(0)}{\lambda x\_{\infty}}>0.\end{array}\right. |  | (5.51) |

This suggests to search ς2​(t)\varsigma^{2}(t) of the form (Power Series Ansatz):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ς2​(t)=ςα,λ,c2​(t):=2​λ​c​t1−α​∑k≥0(−1)k​ck​λk​tα​kwithc0=Γ​(α)2Γ​(2​α−1)​Γ​(2−α)​μ​(0)λ​x∞.\varsigma^{2}(t)=\varsigma\_{\alpha,\lambda,c}^{2}(t):=2\,\lambda\,c\,t^{1-\alpha}\sum\_{k\geq 0}(-1)^{k}c\_{k}\lambda^{k}t^{\alpha k}\quad\text{with}\quad c\_{0}=\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)\Gamma(2-\alpha)}\frac{\mu(0)}{\lambda x\_{\infty}}. |  | (5.52) |

Remark: 1. At this point, it is crucial to emphasize that, for a fixed value of α\alpha, all functions ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} from equation ([6.58](https://arxiv.org/html/2511.03474v1#S6.E58 "In 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) are derived or generated from a common function, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ςα,λ,c2​(t)=c​λ2−1α​ςα2​(λ1α​t)withςα2​(t):=2​t1−α​∑k≥0(−1)k​ck​tα​k.\varsigma^{2}\_{\alpha,\lambda,c}(t)=c\lambda^{2-\frac{1}{\alpha}}\varsigma\_{\alpha}^{2}\left(\lambda^{\frac{1}{\alpha}}t\right)\quad\text{with}\quad\varsigma\_{\alpha}^{2}(t):=2\,t^{1-\alpha}\sum\_{k\geq 0}(-1)^{k}c\_{k}t^{\alpha k}. |  | (5.53) |

where the coefficients ckc\_{k} depend on α\alpha. Thus, for simplicity in what follows, we will assume c=λ=1c=\lambda=1.

2. For the computation of the function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2}, we need to establish a recurrence formula satisfied by the coefficients ckc\_{k}, which involves knowing the form of the function ϕ\phi or more specificcally, the mean-reverting function μ\mu. In practice, since this function is usually taken to be constant equal to μ0\mu\_{0}, we are going in the next subsection to compute and study the function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} when μ​(t)=μ0a.e.\mu(t)=\mu\_{0}\quad\text{a.e.} and α∈(1,32)\alpha\in(1,\frac{3}{2}) bearing in mind that, the case when α∈(12,1)\alpha\in(\frac{1}{2},1) have been intensively study in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) .

#### 5.2.1 Existence and computation of the function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} solution of the stabilizer equation when α∈(1,32)\alpha\in(1,\frac{3}{2})

The recurrence formula satisfied by the coefficients ckc\_{k}, which make possible the computation of the functions ςα,λ,c\varsigma\_{\alpha,\lambda,c} are established in the same manner as in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) .
We consider the case where μ​(t)=μ0\mu(t)=\mu\_{0} a.e., so that μ∞=μ​(0)=μ0\mu\_{\infty}=\mu(0)=\mu\_{0}, and assume ϕ≡1\phi\equiv 1 as in the previous subsection. We then have the following proposition, whose proof is postponed to Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

###### Proposition 5.2 (Existence of the function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} for α∈(1,2)\alpha\in(1,2)).

Let α∈(1,2)\alpha\in(1,2):

1. 1.

   limt→0ςα,λ,c2=+∞\lim\_{t\to 0}\varsigma^{2}\_{\alpha,\lambda,c}=+\infty, and limt→+∞ςα,λ,c2​(t)=c​λ2‖fα,λ‖L2​(Leb1)2.\lim\_{t\to+\infty}\varsigma^{2}\_{\alpha,\lambda,c}(t)=\frac{c\lambda^{2}}{\|f\_{\alpha,\lambda}\|^{2}\_{L^{2}(\text{Leb}\_{1})}}.
2. 2.

   ςα,λ,c2​(t)=c​λ2−1α​ςα2​(λ1α​t)\varsigma^{2}\_{\alpha,\lambda,c}(t)=c\lambda^{2-\frac{1}{\alpha}}\varsigma\_{\alpha}^{2}(\lambda^{\frac{1}{\alpha}}t) where ςα2​(t):=2​t1−α​∑k≥0(−1)k​ck​tα​k\varsigma\_{\alpha}^{2}(t):=2\,t^{1-\alpha}\sum\_{k\geq 0}(-1)^{k}c\_{k}t^{\alpha k} and the coefficients (ck)k≥0(c\_{k})\_{k\geq 0} are defined as follows: c0=Γ​(α)2Γ​(2​α−1)​Γ​(2−α) and for everyk≥1,c\_{0}=\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)\Gamma(2-\alpha)}\quad\textit{ and for every}\quad k\geq 1,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ck=Γ​(α)2​Γ​(α​(k+1))Γ​(2​α−1)​Γ​(α​k+2−α)​[(a∗b)k−α​(k+1)​∑ℓ=1kB​(α​(ℓ+2)−1,α​(k−ℓ−1)+2)​(b∗2)ℓ​ck−ℓ].c\_{k}=\frac{\Gamma(\alpha)^{2}\Gamma(\alpha(k+1))}{\Gamma(2\alpha-1)\Gamma(\alpha k+2-\alpha)}\left[(a\*b)\_{k}-\alpha(k+1)\sum\_{\ell=1}^{k}B\big(\alpha(\ell+2)-1,\alpha(k-\ell-1)+2\big)(b^{\*2})\_{\ell}c\_{k-\ell}\right]. |  | (5.54) |

   where for two sequences of real numbers (uk)k≥0(u\_{k})\_{k\geq 0} and (vk)k≥0(v\_{k})\_{k\geq 0}, the Cauchy product is defined as (u∗v)k=∑ℓ=0kuℓ​vk−ℓ(u\*v)\_{k}=\sum\_{\ell=0}^{k}u\_{\ell}v\_{k-\ell} and B​(a,b)=∫01ua−1​(1−u)b−1​𝑑uB(a,b)=\int\_{0}^{1}u^{a-1}(1-u)^{b-1}du denoting the beta function.
3. 3.

   The convergence radius ρα=(lim infk(|ck|1/k))−1α\rho\_{\alpha}=\left(\liminf\_{k}\left(|c\_{k}|^{1/k}\right)\right)^{\frac{-1}{\alpha}} of the power series ∑k≥0ck​tα​k\sum\_{k\geq 0}c\_{k}t^{\alpha k}, defined by the coefficients ckc\_{k}, is infinite. Specifically, there exist constants K≥1K\geq 1 and A≥2α+2A\geq 2^{\alpha+2} such that for all k≥0k\geq 0, the following inequality holds: |ck|≤K​AkΓ​(α​(k−1)+2).|c\_{k}|\leq\frac{KA^{k}}{\Gamma(\alpha(k-1)+2)}.
   As a consequence, the expansion in equation [5.53](https://arxiv.org/html/2511.03474v1#S5.E53 "In 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") converges for all t∈ℝ+t\in\mathbb{R}^{+}, and in fact, for all t∈ℝt\in\mathbb{R}.

Remark.
The equation in ([5.54](https://arxiv.org/html/2511.03474v1#S5.E54 "In item 2 ‣ Proposition 5.2 (Existence of the function 𝜍_{𝛼,𝜆,𝑐}² for 𝛼∈(1,2)). ‣ 5.2.1 Existence and computation of the function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1,3/2) ‣ 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), which provides the coefficients of the expansion
for ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} when α∈(1,32)\alpha\in(1,\tfrac{3}{2}),
closely resembles that obtained for α∈(12,1)\alpha\in(\tfrac{1}{2},1) in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) ,
although the properties of the two functions differ significantly.
By the scaling property ([5.53](https://arxiv.org/html/2511.03474v1#S5.E53 "In 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we may assume now that c=λ=1c=\lambda=1.

###### Proposition 5.3 (Existence of ςα,λ,c\varsigma\_{\alpha,\lambda,c} i.e. positivity computation of the function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2} solution of the stabilizer equation for α∈(1,32)\alpha\in(1,\frac{3}{2})).

Let α∈(1,32)\alpha\in(1,\frac{3}{2}) and consider the volterra equation of the first kind,

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ​(1−Rα2​(t))=(fα2∗gα)​(t),∀t≥0,κ>0.\kappa\,\left(1-R\_{\alpha}^{2}(t)\right)=(f\_{\alpha}^{2}\*g\_{\alpha})(t),\quad\forall t\geq 0,\quad\kappa>0. |  | (5.55) |

with Rα:ℝ+→ℝR\_{\alpha}:\mathbb{R}^{+}\to\mathbb{R}, fα:=−Rα′f\_{\alpha}:=-R\_{\alpha}^{\prime} satisfy Rα​(0)=1R\_{\alpha}(0)=1, limt→+∞Rα​(t)=0\lim\_{t\to+\infty}R\_{\alpha}(t)=0, and fα​(0)=0f\_{\alpha}(0)=0, limt→+∞fα​(t)=0\lim\_{t\to+\infty}f\_{\alpha}(t)=0

1. (a)

   Then equation ([6.59](https://arxiv.org/html/2511.03474v1#S6.E59 "In item 1 ‣ Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has at most one solution in Lloc1​(Leb1)L^{1}\_{\text{loc}}(\text{Leb}\_{1}) that converges to a finite limit.
2. (b)

   If the equation ([6.59](https://arxiv.org/html/2511.03474v1#S6.E59 "In item 1 ‣ Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has a continuous solution gαg\_{\alpha} defined on I⊆(0,+∞)I\subseteq(0,+\infty) , then gα≥0g\_{\alpha}\geq 0 on I⊆ℝ+I\subseteq\mathbb{R}^{+}, so that the function gα\sqrt{g\_{\alpha}} is well-defined on I⊆ℝ+I\subseteq\mathbb{R}\_{+}.

Proof. The argument is similar to that of Proposition [6.1](https://arxiv.org/html/2511.03474v1#S6.Thmprop1 "Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and is therefore left to the reader.

### 5.3 Numerical illustration of Fake Stationarity for Fractional SVIE with α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2})

In this section we specify a family of scaled volterra equations where b​(x)=μ0−λ​xb(x)=\mu\_{0}-\lambda\,x for λ>0\lambda>0 and a diffusion coefficient σ\sigma to be specified later. Let c be such that c​[σ]L​i​p2<1c[\sigma]^{2}\_{Lip}<1.
For the numerical illustrations, we consider the case ϕ​(t)=Cste=ϕ​(0)=1almost surely,\phi(t)=C^{\text{ste}}=\phi(0)=1\quad\text{almost surely}, in which case the equation with constant mean reads :

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=μ0λ+(X0−μ0λ)​Rλ​(t)+1λ​∫0tfα,λ​(t−s)​ς​(s)​σ​(Xs)​𝑑Ws.X\_{t}=\frac{\mu\_{0}}{\lambda}+\Big(X\_{0}-\frac{\mu\_{0}}{\lambda}\Big)R\_{\lambda}(t)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\alpha,\lambda}(t-s)\varsigma(s)\sigma(X\_{s})dW\_{s}. |  | (5.56) |

The reader is invited to take a look to the Appendix [A](https://arxiv.org/html/2511.03474v1#A1 "Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE) ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") for the semi-integrated Euler scheme introduce in this setting for the above equation and to the captions of the differents figures for the numerical values of the parameters of the Stochastic Volterra equation.

#### 5.3.1 A numerical illustration of Fake Stationarity in SVIE with α\alpha-Fractional Kernels for α∈(1,32)\alpha\in(1,\frac{3}{2}) and (stabilized) quadratic Diffusion coefficient

We consider an α\alpha-fractional kernel for α∈(1,32)\alpha\in(1,\frac{3}{2}) (“Long Memory”) and a squared trinomial diffusion coefficient of the form [3.32](https://arxiv.org/html/2511.03474v1#S3.E32 "In Example 3.10 (Polynomial of degree 2). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), σ​(x)=κ0+κ1​(x−μ0λ)+κ2​(x−μ0λ)2,κi≥0,i=0,2,κ12≤4​κ2​κ0.\sigma(x)=\sqrt{\kappa\_{0}+\kappa\_{1}\,(x-\frac{\mu\_{0}}{\lambda})+\kappa\_{2}\,(x-\frac{\mu\_{0}}{\lambda})^{2}},\;\kappa\_{i}\geq 0,\;i=0,2,\;\kappa^{2}\_{1}\leq 4\kappa\_{2}\kappa\_{0}.

![Refer to caption](x1.png)


Figure 4:  Graph of the stabilizer t→ςα,λ,c​(t)t\to\varsigma\_{\alpha,\lambda,c}(t) over time interval [0, T ], T = 10 for a value of the Hurst esponent H=0.8H=0.8, λ=0.2\lambda=0.2, c = 0.3.

![Refer to caption](x2.png)


Figure 5: Confluence from a [0,30]-Uniform Distribution, T=60, H=0.8H=0.8, λ=0.2\lambda=0.2, c = 0.36.

Figure [5](https://arxiv.org/html/2511.03474v1#S5.F5 "Figure 5 ‣ 5.3.1 A numerical illustration of Fake Stationarity in SVIE with 𝛼-Fractional Kernels for 𝛼∈(1,3/2) and (stabilized) quadratic Diffusion coefficient ‣ 5.3 Numerical illustration of Fake Stationarity for Fractional SVIE with 𝛼∈(1/2,3/2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") shows L2L^{2}-confluence of the the process’s marginals for different initial values as time increases.

![Refer to caption](x3.png)


Figure 6: Graph of tk↦StdDev​(tk,M)t\_{k}\mapsto\text{StdDev}(t\_{k},M) and tk↦𝔼​[σ2​(Xtk,M)]t\_{k}\mapsto\mathbb{E}[\sigma^{2}(X\_{t\_{k}},M)] over [0,T][0,T], T=1T=1, H=0.8H=0.8, μ0=2\mu\_{0}=2, λ=0.2\lambda=0.2, v0=0.09v\_{0}=0.09, and StdDev​(X0)=0.3\text{StdDev}(X\_{0})=0.3. Number of steps: n=800n=800, Simulation size: M=100000M=100000.

#### 5.3.2 A numerical illustration of the degenerate case of Fake Stationarity in SVIE with α\alpha-Fractional Kernels for α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2}) and a (stabilized) tanh Diffusion coefficient

In this section we specify a family of scaled models where b​(x)=μ0−λ​xb(x)=\mu\_{0}-\lambda\,x and σ​(x)=tanh⁡(x−μ0λ)2,λ>0\sigma(x)=\sqrt{\frac{\tanh(x-\frac{\mu\_{0}}{\lambda})}{2}},\lambda>0.

![Refer to caption](x4.png)


Figure 7:  Graph of the stabilizer t→ςα,λ,c​(t)t\to\varsigma\_{\alpha,\lambda,c}(t) over time interval [0, T ], T = 50 for a value of the Hurst esponent H=0.4H=0.4, λ=0.2\lambda=0.2, c=0.36c=0.36.

![Refer to caption](x5.png)


Figure 8: Confluent trajectories in the degenerate case, T=50T=50, H=0.4H=0.4, λ=0.2\lambda=0.2, c=0.36c=0.36.

## 6 Applications to Exponential-Fractional Stochastic Volterra Equations

Let consider the below Gamma Fractional integration kernel or Exponential-Fractional integration kernel defined in Example [2.3](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem3 "Example 2.3 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), where α=H+12\alpha=H+\frac{1}{2}, with HH denoting the Hurst coefficient:

K​(t)=Kα,ρ​(t)=e−ρ​t​uα−1Γ​(α)​𝟏ℝ+​(t),withα,ρ>0.K(t)=K\_{\alpha,\rho}(t)=e^{-\rho t}\frac{u^{\alpha-1}}{\Gamma(\alpha)}\mathbf{1}\_{\mathbb{R}\_{+}}(t),\quad\text{with}\quad\alpha,\rho>0.

The purpose of this part is to extend the results of the preceeding section to the general case of a gamma fractional integration kernel where α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2}). Note that, this is a generalization of the exponential kernel and the fractional integration kernel.
The gamma kernel is often adopted in the Quadratic Rough Heston model (see, e.g., [BourgeyGatheral2025](https://arxiv.org/html/2511.03474v1#bib.bib9) ) due to its numerical convenience, flexibility, and the availability of a closed-form expression for its resolvent of the second kind. We show that for such kernels Kα,ρK\_{\alpha,\rho}, the resolvent Rα,ρ,λR\_{\alpha,\rho,\lambda} satisfy our standing assumption (𝒦)({\cal K})\; for all λ>0\lambda>0, and that fα,ρ,λ:=−Rα,ρ,λf\_{\alpha,\rho,\lambda}:=-R\_{\alpha,\rho,\lambda} exists and is square-integrable with respect to the Lebesgue measure on ℝ+\mathbb{R}\_{+}, both for 12<α<1\frac{1}{2}<\alpha<1 (“rough models”) and 12<α<32\frac{1}{2}<\alpha<\frac{3}{2} (“long memory volatility models”). As a result, the findings from Sections [3](https://arxiv.org/html/2511.03474v1#S3 "3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), [3.3](https://arxiv.org/html/2511.03474v1#S3.SS3 "3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and [4](https://arxiv.org/html/2511.03474v1#S4 "4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), will be applicable in the cases where σ​(t,x)=σ​(x)\sigma(t,x)=\sigma(x) (Gaussian setting) and σ​(t,x)=ς​(t)​σ​(x)\sigma(t,x)=\varsigma(t)\sigma(x).

### 6.1 α−\alpha- Exponential Fractional kernels 12<α<32\frac{1}{2}<\alpha<\frac{3}{2}

By definition, ℒ​[Rα,ρ,λ]​(s)=1s​(1+ℒ​[Kα,ρ]​(s))=1s​(1+λ​(s+ρ)−α)\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)=\frac{1}{s(1+\mathcal{L}[K\_{\alpha,\rho}](s))}=\frac{1}{s(1+\lambda(s+\rho)^{-\alpha})} (owing to Example [2.3](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem3 "Example 2.3 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))
so that, by the Tauberian Final Value Theorem 121212f:[0,∞)→ℂf:[0,\infty)\to\mathbb{C} continuous,
limt→∞f​(t)=f∞\lim\_{t\to\infty}f(t)=f\_{\infty}, the Laplace transform Lf​(s)L\_{f}(s) exists for s>0s>0 and
lims→0+s​Lf​(s)=f∞.\lim\_{s\to 0^{+}}sL\_{f}(s)=f\_{\infty}. : a:=limt→∞Rα,ρ,λ​(t)=lims→0s​ℒ​[Rα,ρ,λ]​(s)=11+λ​ρ−α∈[0,1)a:=\lim\_{t\to\infty}R\_{\alpha,\rho,\lambda}(t)=\lim\_{s\to 0}s\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)=\frac{1}{1+\lambda\rho^{-\alpha}}\in[0,1).
If λ>0\lambda>0, we define the function fα,ρ,λ:=−Rα,ρ,λf\_{\alpha,\rho,\lambda}:=-R\_{\alpha,\rho,\lambda} on (0,+∞)(0,+\infty) (see ([2.11](https://arxiv.org/html/2511.03474v1#S2.E11 "In Example 2.3 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) in Example[2.3](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem3 "Example 2.3 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) by noticing that :

|  |  |  |
| --- | --- | --- |
|  | ℒ​[fα,ρ,λ]​(s)=ℒ​[−Rα,ρ,λ′]​(s)=−s​ℒ​[Rα,ρ,λ]​(s)+Rα,ρ,λ​(0)=−ss​(1+λ​(s+ρ)−α)+1=λλ+(s+ρ)α=ℒ​[e−ρ⁣⋅​fα,λ]​(s)\mathcal{L}[f\_{\alpha,\rho,\lambda}](s)=\mathcal{L}[-R^{\prime}\_{\alpha,\rho,\lambda}](s)=-s\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)+R\_{\alpha,\rho,\lambda}(0)=\frac{-s}{s(1+\lambda(s+\rho)^{-\alpha})}+1=\frac{\lambda}{\lambda+(s+\rho)^{\alpha}}=\mathcal{L}[e^{-\rho\cdot}f\_{\alpha,\lambda}](s) |  |

i.e. by injectivity of the Laplace transform, fα,ρ,λ​(t)=e−ρ​t​fα,λ​(t)=α​λ​e−ρ​t​tα−1​Eα′​(−λ​tα).f\_{\alpha,\rho,\lambda}(t)=e^{-\rho t}f\_{\alpha,\lambda}(t)=\alpha\lambda e^{-\rho t}t^{\alpha-1}E^{\prime}\_{\alpha}(-\lambda t^{\alpha}).
Likewise, using Tauberian Final Value Theorem, limt→∞fα,ρ,λ​(t)=lims→0s​ℒ​[−Rα,ρ,λ′]​(s)\lim\_{t\to\infty}f\_{\alpha,\rho,\lambda}(t)=\lim\_{s\to 0}s\mathcal{L}[-R^{\prime}\_{\alpha,\rho,\lambda}](s), that is

limt→∞fα,ρ,λ​(t)=−lims→0s​(s​ℒ​[Rα,ρ,λ]​(s)−Rα,ρ,λ​(0))=−lims→0s(1+λ​(s+ρ)−α)−s=0\lim\_{t\to\infty}f\_{\alpha,\rho,\lambda}(t)=-\lim\_{s\to 0}s\left(s\mathcal{L}[R\_{\alpha,\rho,\lambda}](s)-R\_{\alpha,\rho,\lambda}(0)\right)=-\lim\_{s\to 0}\frac{s}{(1+\lambda(s+\rho)^{-\alpha})}-s=0

Remark: Note that we recover the exponential kernel if α=ρ=1\alpha=\rho=1.
In fact, if K​(t)=e−t​𝟏ℝ+​(t)K(t)=e^{-t}\mathbf{1}\_{\mathbb{R}\_{+}}(t), R1,1,λR\_{1,1,\lambda}
reads:

|  |  |  |
| --- | --- | --- |
|  | R1,1,λ​(t)=𝟏ℝ+​(t)+∑k≥1(−1)k​λk​∫0te−s​sk−1Γ​(k)​𝑑s=𝟏ℝ+​(t)+∫0te−s​∑k≥1(−1)k​λk​sk−1k!​d​s=1−λ​∫0te−(λ+1)​s​𝑑s\displaystyle R\_{1,1,\lambda}(t)=\mathbf{1}\_{\mathbb{R}\_{+}}(t)+\sum\_{k\geq 1}(-1)^{k}\lambda^{k}\int\_{0}^{t}\frac{e^{-s}s^{k-1}}{\Gamma(k)}\,ds=\mathbf{1}\_{\mathbb{R}\_{+}}(t)+\int\_{0}^{t}e^{-s}\sum\_{k\geq 1}(-1)^{k}\lambda^{k}\frac{s^{k-1}}{k!}\,ds=1-\lambda\int\_{0}^{t}e^{-(\lambda+1)s}\,ds |  |

So that we recover the resolvent of the exponential kernel given in [Pages2024](https://arxiv.org/html/2511.03474v1#bib.bib36) :

|  |  |  |
| --- | --- | --- |
|  | K​(t)=e−t,which are ​Rλ​(t)={t+1if ​λ=−11+λ​e−(λ+1)​tλ+1if ​λ≠−1K(t)=e^{-t},\quad\text{which are }R\_{\lambda}(t)=\begin{cases}t+1&\text{if }\lambda=-1\\ \frac{1+\lambda e^{-(\lambda+1)t}}{\lambda+1}&\text{if }\lambda\neq-1\end{cases} |  |

###### Proposition 6.1.

Let λ>0\lambda>0 and let α∈(0,2)\alpha\!\in(0,2).

(a)(a) The λ\lambda-resolvent Rα,ρ,λR\_{\alpha,\rho,\lambda} is infinitely differentiable i.e. 𝒞∞\mathcal{C}^{\infty} on (0,+∞)(0,+\infty) and completely monotonic if α<1\alpha<1.
Moreover Rα,ρ,λ​(0)=1R\_{\alpha,\rho,\lambda}(0)=1, Rα,ρ,λR\_{\alpha,\rho,\lambda} converges to a:=11+λ​ρ−α∈[0,1[a:=\frac{1}{1+\lambda\rho^{-\alpha}}\in[0,1[.
Rα,ρ,λ∈ℒr​(Leb1)R\_{\alpha,\rho,\lambda}\!\in{\cal L}^{r}({\rm Leb}\_{1}) for every r>1αr>\frac{1}{\alpha}.

(b)(b) fα,ρ,λ:=−Rα,ρ,λ′f\_{\alpha,\rho,\lambda}:=-R^{\prime}\_{\alpha,\rho,\lambda} is infinitely differentiable, converges to 0, and satisfy :

|  |  |  |
| --- | --- | --- |
|  | ∀t>0,fα,ρ,λ​(t):=e−ρ​t​fα,λ​(t)=λ1α​∫0+∞e−(ρ+λ1α)​t​u​u​Hα​(u)​𝑑u−2α​et​(λ1α​cos⁡(πα)−ρ)​cos⁡[t​λ1α​sin⁡(πα)−πα].\forall\,t>0,\quad f\_{\alpha,\rho,\lambda}(t):=e^{-\rho t}f\_{\alpha,\lambda}(t)=\lambda^{\frac{1}{\alpha}}\int\_{0}^{+\infty}e^{-(\rho+\lambda^{\frac{1}{\alpha}})tu}uH\_{\alpha}(u)du-\frac{2}{\alpha}e^{t(\lambda^{\frac{1}{\alpha}}\cos\left(\frac{\pi}{\alpha}\right)-\rho)}\cos\left[t\lambda^{\frac{1}{\alpha}}\sin\left(\frac{\pi}{\alpha}\right)-\frac{\pi}{\alpha}\right]. |  |

If α<1\alpha<1, fα,ρ,λf\_{\alpha,\rho,\lambda} is a completely monotonic function (hence convex), decreasing to 0 while 1−Rα,ρ,λ1-R\_{\alpha,\rho,\lambda} is a Bernstein function.

(c)(c) If α∈(12,32)\alpha\!\in(\frac{1}{2},\frac{3}{2}), fα,ρ,λf\_{\alpha,\rho,\lambda} is ℒ2​β{\cal L}^{2\beta}-integrable ∀β∈(0,12​(1−α))\forall\beta\in\big(0,\frac{1}{2(1-\alpha)}\big) if α<1\alpha<1 and for every β\beta if α>1\alpha>1.
  
Moreover, for i∈{1,2}i\in\{1,2\} and for every ϑ∈(0,α−𝟏i=2i)\vartheta\!\in\big(0,\alpha-\frac{\mathbf{1}\_{i=2}}{i}\big), there exists a real constant Cϑ,ρ,λ>0C\_{\vartheta,\rho,\lambda}>0 such that

∀δ>0,[∫0+∞(fα,ρ,λ​(t+δ)−fα,ρ,λ​(t))i]1/i≤Cϑ,ρ,λ​δϑ.\forall\,\delta>0,\quad\left[\int\_{0}^{+\infty}\big(f\_{\alpha,\rho,\lambda}(t+\delta)-f\_{\alpha,\rho,\lambda}(t)\big)^{i}\right]^{1/i}\leq C\_{\vartheta,\rho,\lambda}\delta^{\vartheta}.

For clarity and conciseness, the proof is postponed to Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

###### Theorem 6.2.

Let α∈(12,32)\alpha\in\left(\frac{1}{2},\frac{3}{2}\right) , ρ>0\rho>0, let K​(t)=Kα,ρ​(t)=e−ρ​t​tα−1Γ​(α)K(t)=K\_{\alpha,\rho}(t)=e^{-\rho t}\frac{t^{\alpha-1}}{\Gamma(\alpha)}, t>0t>0 the Gamma fractional kernel, let σ​(t,x):=ς​(t)​σ​(x)\sigma(t,x):=\varsigma(t)\sigma(x) with σ\sigma be a Lipschitz continuous function given by ([3.32](https://arxiv.org/html/2511.03474v1#S3.E32 "In Example 3.10 (Polynomial of degree 2). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), thus satisfying a relation of the type ([4.33](https://arxiv.org/html/2511.03474v1#S4.E33 "In Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) (S​Lσ)(SL\_{\sigma}) with κ:=κ2>0\kappa:=\kappa\_{2}>0, let c∈(0,1κ2)c\in\left(0,\frac{1}{\kappa\_{2}}\right) with ς=ςλ,c\varsigma=\varsigma\_{\lambda,c}, λ>0\lambda>0 and let X0∈L2​(ℙ)X\_{0}\in L^{2}(\mathbb{P}) such that 𝔼​[X0]=x∞\mathbb{E}[X\_{0}]=x\_{\infty} and V​a​r​(X0)=v0=c​σ2​(x∞)1−c​κ2.Var(X\_{0})=v\_{0}=\frac{c\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}.
Then,

1. 1.

   For exponential-fractional kernels Kα,ρK\_{\alpha,\rho} with 12<α<32\frac{1}{2}<\alpha<\frac{3}{2}, the solution (Xt)t≥0(X\_{t})\_{t\geq 0} to the Volterra equation ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0X\_{0} has a fake
   stationary regime of type I in the sense that:

   ∀t≥0,𝔼​Xt=x∞,Var​(Xt)=v0=c​σ2​(x∞)1−c​κ2​ and 𝔼​σ2​(Xt)=σ¯02=σ2​(x∞)1−c​κ2.\forall\,t\geq 0,\qquad\mathbb{E}\,X\_{t}=x\_{\infty},\quad{\rm Var}(X\_{t})=v\_{0}=\frac{c\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}\mbox{ and }\quad\mathbb{E}\,\sigma^{2}(X\_{t})=\bar{\sigma}\_{0}^{2}=\frac{\sigma^{2}(x\_{\infty})}{1-c\kappa\_{2}}.
2. 2.

   If ϕ∞=0\phi\_{\infty}=0, for every X0′∈L2​(ℙ)X\_{0}^{\prime}\in L^{2}(\mathbb{P}), a solution to ([3.12](https://arxiv.org/html/2511.03474v1#S3.E12 "In 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0′X\_{0}^{\prime} satisfies ‖Xt′−Xt‖2​→t→∞​0\|X\_{t}^{\prime}-X\_{t}\|\_{2}\underset{t\to\infty}{\to}0.
3. 3.

   The family of shifted processes Xt+⁣⋅,t≥0X\_{t+\cdot},t\geq 0, is CC-tight as t→+∞t\to+\infty and its (functional) limiting distributions are all L2L^{2}-stationary processes with covariance function C∞C\_{\infty} given by ([4.42](https://arxiv.org/html/2511.03474v1#S4.E42 "In Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).

Proof.
The (1) is a consequence of Proposition [3.11](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem11 "Proposition 3.11. ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
If 0<ϑ<α−120<\vartheta<\alpha-\frac{1}{2} and β>1\beta>1,
Theorem [4.6](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem6 "Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") applies.

### 6.2 Existence of ςα,ρ,λ,c\varsigma\_{\alpha,\rho,\lambda,c} i.e. positivity computation of the function ςα,ρ,λ,c2\varsigma\_{\alpha,\rho,\lambda,c}^{2} solution of the stabilizer equation when α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2})

In this section we want to compute ςλ,c\varsigma\_{\lambda,c}. To this end we rely on the Laplace version of the equation (Eλ,cE\_{\lambda,c}) in ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) satisfied by ςλ,c2\varsigma^{2}\_{\lambda,c}, namely ∀t≥0,c​λ2​(1−(ϕ−fλ∗ϕ)2​(t))=(fλ2∗ς2)​(t),\forall\,t\geq 0,\quad c\lambda^{2}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=(f\_{\lambda}^{2}\*\varsigma^{2})(t),
for which the laplace transform is given by equation ([3.26](https://arxiv.org/html/2511.03474v1#S3.E26 "In Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) in Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"):

∀t>0,t​Lfλ2​(t).Lς2​(t)=−2​c​λ2​L(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t).\forall\,t>0,\quad t\,L\_{f^{2}\_{\lambda}}(t).L\_{\varsigma^{2}}(t)=-2\,c\lambda^{2}L\_{(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t).

Given the form of the kernel Kα,ρ​(u)=e−ρ​u​uα−1Γ​(α)​𝟏ℝ​(u),α,ρ>0K\_{\alpha,\rho}(u)=e^{-\rho u}\frac{u^{\alpha-1}}{\Gamma(\alpha)}\mathbf{1}\_{\mathbb{R}}(u),\quad\alpha,\rho>0 and the expansion of the resolvents Rα,λR\_{\alpha,\lambda} and it derivative −fα,λ-f\_{\alpha,\lambda}, in Example [2.3](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem3 "Example 2.3 (Laplace transform and limit-from𝜆- Resolvent associated to the Exponential-fractional Kernel). ‣ 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")

|  |  |  |
| --- | --- | --- |
|  | Rα,ρ,λ​(t)=1+∑k≥1(−1)k​λk​∫0te−ρ​s​sk​α−1Γ​(k​α)​𝑑s,fα,ρ,λ​(t)=e−ρ​t​fα,λ​(t)=λ​e−ρ​t​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1))R\_{\alpha,\rho,\lambda}(t)=1+\sum\_{k\geq 1}(-1)^{k}\lambda^{k}\int\_{0}^{t}\frac{e^{-\rho s}s^{k\alpha-1}}{\Gamma(k\alpha)}\,ds,\quad f\_{\alpha,\rho,\lambda}(t)=e^{-\rho t}f\_{\alpha,\lambda}(t)=\lambda e^{-\rho t}t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\lambda^{k}\frac{t^{\alpha k}}{\Gamma(\alpha(k+1))} |  |

Since ϕ​(t)−(fλ∗ϕ)​(t)=1−(fλ∗μ)tλ​x∞\phi(t)-(f\_{\lambda}\*\phi)(t)=1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda x\_{\infty}} we have ϕ​(t)−(fλ∗ϕ)​(t)∼01\phi(t)-(f\_{\lambda}\*\phi)(t)\stackrel{{\scriptstyle 0}}{{\sim}}1 and by Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (2)
(ϕ​(t)−(fλ∗ϕ)​(t))′∼0−μ​(0)λ​x∞​fλ​(t)(\phi(t)-(f\_{\lambda}\*\phi)(t))^{\prime}\stackrel{{\scriptstyle 0}}{{\sim}}-\frac{\mu(0)}{\lambda x\_{\infty}}f\_{\lambda}(t), so that:

e2​ρ​t​(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t)∼0−μ​(0)λ​x∞​λ​tα−1Γ​(α) ande2​ρ​t​fλ2​(t)∼0λ2​t2​(α−1)Γ​(α)2e^{2\rho t}(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}(t)\stackrel{{\scriptstyle 0}}{{\sim}}-\frac{\mu(0)}{\lambda x\_{\infty}}\frac{\lambda t^{\alpha-1}}{\Gamma(\alpha)}\quad\mbox{ and}\quad e^{2\rho t}f^{2}\_{\lambda}(t)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{\lambda^{2}t^{2(\alpha-1)}}{\Gamma(\alpha)^{2}}

It follows that (heuristically) Le2​ρ⁣⋅​(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t)∼+∞−λ​μ​(0)λ​x∞​t−α​ and​Le2​ρ⁣⋅​fλ2​(t)∼+∞λ2​Γ​(2​α−1)​t−(2​α−1)Γ​(α)2.L\_{e^{2\rho\cdot}(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t)\stackrel{{\scriptstyle+\infty}}{{\sim}}-\lambda\frac{\mu(0)}{\lambda x\_{\infty}}t^{-\alpha}\;\mbox{ and}\;L\_{e^{2\rho\cdot}f^{2}\_{\lambda}}(t)\stackrel{{\scriptstyle+\infty}}{{\sim}}\frac{\lambda^{2}\Gamma(2\alpha-1)t^{-(2\alpha-1)}}{\Gamma(\alpha)^{2}}.
So, roughly, this implies that

Le2​ρ⁣⋅​ς2​(t)=Lς2​(t−2​ρ)=−2​c​λ2​L(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t−2​ρ)(t−2​ρ)​Le2​ρ⁣⋅​fλ2​(t−2​ρ)∼+∞2​λ​c​μ​(0)λ​x∞​Γ​(α)2Γ​(2​α−1)​t−(2−α)L\_{e^{2\rho\cdot}\varsigma^{2}}(t)=L\_{\varsigma^{2}}(t-2\rho)=\frac{-2c\lambda^{2}L\_{(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t-2\rho)}{(t-2\rho)L\_{e^{2\rho\cdot}f^{2}\_{\lambda}}(t-2\rho)}\stackrel{{\scriptstyle+\infty}}{{\sim}}2\lambda\,c\frac{\mu(0)}{\lambda x\_{\infty}}\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)}t^{-(2-\alpha)}

owing to Equation ([3.26](https://arxiv.org/html/2511.03474v1#S3.E26 "In Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) evaluated at (t−2​ρ)(t-2\rho).
This in turn suggests that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ς2​(t)∼02​λ​c​Γ​(α)2Γ​(2​α−1)​Γ​(2−α)​μ​(0)λ​x∞​e−2​ρ​t​t1−α​so that​{(i)ς​(0)=0​ if ​α<1,(i​i)limt→0+ς​(t)=+∞​ if ​α>1​ provided ​μ​(0)λ​x∞>0.\varsigma^{2}(t)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{2\lambda c\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)\Gamma(2-\alpha)}\frac{\mu(0)}{\lambda x\_{\infty}}e^{-2\rho t}t^{1-\alpha}\quad\text{so that}\left\{\begin{array}[]{ll}(i)&\varsigma(0)=0\text{ if }\alpha<1,\\ (ii)&\lim\_{t\to 0^{+}}\varsigma(t)=+\infty\text{ if }\alpha>1\text{ provided }\frac{\mu(0)}{\lambda x\_{\infty}}>0.\end{array}\right. |  | (6.57) |

This suggests to search ς2​(t)\varsigma^{2}(t) of the form (Exponential Power Series Ansatz):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ς2​(t)=ςα,ρ,λ,c2​(t):=2​λ​c​e−2​ρ​t​t1−α​∑k≥0(−1)k​ck​λk​tα​k,with​c0=Γ​(α)2Γ​(2​α−1)​Γ​(2−α)​μ​(0)λ​x∞.\varsigma^{2}(t)=\varsigma\_{\alpha,\rho,\lambda,c}^{2}(t):=2\,\lambda\,c\,e^{-2\rho t}t^{1-\alpha}\sum\_{k\geq 0}(-1)^{k}c\_{k}\lambda^{k}t^{\alpha k},\;\text{with}\;c\_{0}=\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)\Gamma(2-\alpha)}\frac{\mu(0)}{\lambda x\_{\infty}}. |  | (6.58) |

so that, there exists η\eta small enough such that ∀t∈(0,η),ςα,ρ,λ,c2​(t)≈e−2​ρ​t​ςα,λ,c2​(t).\forall t\in(0,\eta),\quad\varsigma\_{\alpha,\rho,\lambda,c}^{2}(t)\approx e^{-2\rho t}\varsigma\_{\alpha,\lambda,c}^{2}(t).

Remark: 
1. For the computation of the function ςα,λ,c2\varsigma\_{\alpha,\lambda,c}^{2}, establishing a recurrence formula satisfied by the coefficients ckc\_{k} turns out to be quite challenging. We rather solve the functional equation numerically. This involves knowing the form of the mean-reverting function μ\mu. In practice, since this function is usually taken to be constant equal to μ0\mu\_{0}, we are study ςα,ρ,λ,c2\varsigma\_{\alpha,\rho,\lambda,c}^{2} when μ​(t)=μ0a.e.\mu(t)=\mu\_{0}\quad\text{a.e.} and α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2}).
  
2. With that in mind, on a time grid tk=k​Tn,k=0,…,n.t\_{k}=k\frac{T}{n},k=0,...,n., we use the discretization

∀k≥1,c​λ2​(1−Rα,ρ,λ,c2​(tk))=(fα,ρ,λ,c2∗ςα,ρ,λ,c2)​(tk)=∑j=0k−1fα,ρ,λ,c2​(tk−tj)​ςα,ρ,λ,c2​(tj+1)​(tj+1−tj).\forall\,k\geq 1,\quad c\lambda^{2}\big(1-R^{2}\_{\alpha,\rho,\lambda,c}(t\_{k})\big)=(f\_{\alpha,\rho,\lambda,c}^{2}\*\varsigma\_{\alpha,\rho,\lambda,c}^{2})(t\_{k})=\sum\_{j=0}^{k-1}f\_{\alpha,\rho,\lambda,c}^{2}(t\_{k}-t\_{j})\varsigma\_{\alpha,\rho,\lambda,c}^{2}(t\_{j+1})(t\_{j+1}-t\_{j}).

which we can solve step by step (Lower-Triangular system) to recover the values ςα,ρ,λ,c2​(tk).\varsigma\_{\alpha,\rho,\lambda,c}^{2}(t\_{k}).

From now on, we consider the case μ​(t)=μ0a.e.\mu(t)=\mu\_{0}\quad\text{a.e.}, such that μ∞=μ​(0)=μ0\mu\_{\infty}=\mu(0)=\mu\_{0} and ϕ≡1\phi\equiv 1.

###### Proposition 6.1 (Existence and Properties of the function ςα,ρ,λ,c2\varsigma\_{\alpha,\rho,\lambda,c}^{2} for α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2})).

Let α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2}):

1. 1.

   In reference to the remark on the stabilizer, consider the following equation for c,λ>0c,\lambda>0:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | c​λ2​(1−Rα,ρ,λ2​(t))=(fα,ρ,λ2∗gα,ρ,λ)​(t),∀t≥0.c\lambda^{2}\left(1-R\_{\alpha,\rho,\lambda}^{2}(t)\right)=(f\_{\alpha,\rho,\lambda}^{2}\*g\_{\alpha,\rho,\lambda})(t),\quad\forall t\geq 0. |  | (6.59) |

   where Rα,ρ,λ:ℝ+→ℝR\_{\alpha,\rho,\lambda}:\mathbb{R}^{+}\to\mathbb{R} and fα,ρ,λ:=−Rα,ρ,λ′f\_{\alpha,\rho,\lambda}:=-R\_{\alpha,\rho,\lambda}^{\prime} satisfy Rα,ρ,λ​(0)=1R\_{\alpha,\rho,\lambda}(0)=1, limt→+∞Rα,ρ,λ​(t)=a\lim\_{t\to+\infty}R\_{\alpha,\rho,\lambda}(t)=a, and limt→+∞fα,ρ,λ​(t)=0\lim\_{t\to+\infty}f\_{\alpha,\rho,\lambda}(t)=0.

   1. (a)

      Then equation ([6.59](https://arxiv.org/html/2511.03474v1#S6.E59 "In item 1 ‣ Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has at most one solution in Lloc1​(Leb1)L^{1}\_{\text{loc}}(\text{Leb}\_{1}) that converges to a finite limit.
   2. (b)

      If the equation ([6.59](https://arxiv.org/html/2511.03474v1#S6.E59 "In item 1 ‣ Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) has a continuous solution gα,ρ,λg\_{\alpha,\rho,\lambda} defined on I⊆(0,+∞)I\subseteq(0,+\infty), then gα,ρ,λ≥0g\_{\alpha,\rho,\lambda}\geq 0 on I⊆ℝ+I\subseteq\mathbb{R}^{+}, so that the function gα,ρ,λ\sqrt{g\_{\alpha,\rho,\lambda}} is well-defined on I⊆ℝ+I\subseteq\mathbb{R}\_{+}. If α<1\alpha<1, gα,ρ,λg\_{\alpha,\rho,\lambda} is concave, non-decreasing and non-negative on [0,+∞)[0,+\infty). In particular, we have ∀t>0gα,ρ,λ​(t)>0\forall t>0\quad g\_{\alpha,\rho,\lambda}(t)>0.
2. 2.

   The stabilizer ςα,ρ,λ,c2\varsigma^{2}\_{\alpha,\rho,\lambda,c} exists as a non-negative function on I⊆(0,+∞)I\subseteq(0,+\infty) and

   limt→0ςα,ρ,λ,c={0​ if ​α≤1,+∞​ if ​α>1.andlimt→+∞ςα,ρ,λ,c​(t)=c​(1−a2​ϕ∞2)​λ‖fα,ρ,λ‖L2​(Leb1),a=11+λ​ρ−α.\lim\_{t\to 0}\varsigma\_{\alpha,\rho,\lambda,c}=\left\{\begin{array}[]{ll}&0\text{ if }\alpha\leq 1,\\
   &+\infty\text{ if }\alpha>1.\end{array}\quad\text{and}\quad\lim\_{t\to+\infty}\varsigma\_{\alpha,\rho,\lambda,c}(t)=\frac{\sqrt{c(1-a^{2}\phi\_{\infty}^{2})}\lambda}{\|f\_{\alpha,\rho,\lambda}\|\_{L^{2}(\text{Leb}\_{1})}},\quad a=\frac{1}{1+\lambda\rho^{-\alpha}}.\right.

Proof. Claim 1(a) comes from Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (3).
Claim (2)(2) follows from 1(b), equation ([6.57](https://arxiv.org/html/2511.03474v1#S6.E57 "In 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (4). The proof of 1(b) is postponed to Appendix [B](https://arxiv.org/html/2511.03474v1#A2 "Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

### 6.3 Numerical illustration of Fake Stationarity for α\alpha-Gamma Fractional SVIE With (Stabilized) Quadratic Diffusion Coefficient and α∈(12,32)\alpha\in(\frac{1}{2},\frac{3}{2})

In this section we specify a family of scaled volterra equations where b​(x)=μ0−λ​xb(x)=\mu\_{0}-\lambda\,x for some λ>0\lambda>0 and a diffusion coefficient σ\sigma given by ([6.60](https://arxiv.org/html/2511.03474v1#S6.E60 "In 6.3 Numerical illustration of Fake Stationarity for 𝛼-Gamma Fractional SVIE With (Stabilized) Quadratic Diffusion Coefficient and 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")). Let c such that c​[σ]L​i​p2<1c[\sigma]^{2}\_{Lip}<1.
For the numerical illustrations, we consider the case ϕ​(t)=Cste=ϕ​(0)=1almost surely,\phi(t)=C^{\text{ste}}=\phi(0)=1\quad\text{almost surely}, in which case the equation with constant mean reads :

Xt=μ0λ+(X0−μ0λ)​Rλ​(t)+1λ​∫0tfα,λ​(t−s)​ς​(s)​σ​(Xs)​𝑑Ws.X\_{t}=\frac{\mu\_{0}}{\lambda}+\Big(X\_{0}-\frac{\mu\_{0}}{\lambda}\Big)R\_{\lambda}(t)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\alpha,\lambda}(t-s)\varsigma(s)\sigma(X\_{s})dW\_{s}.

The reader is invited to take a look to the Appendix [A](https://arxiv.org/html/2511.03474v1#A1 "Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE) ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") for the semi-integrated Euler scheme introduce in this setting for the above equation and to the captions of the differents figures for the numerical values of the parameters of the Stochastic Volterra equation.
We consider an α\alpha-Gamma Fractional kernel for α∈(12,32)⊂(0,2)\alpha\in(\frac{1}{2},\frac{3}{2})\subset(0,2) (“Rough and Long Memory models ”) and a squared trinomial diffusion coefficient
σ\sigma of the form [3.32](https://arxiv.org/html/2511.03474v1#S3.E32 "In Example 3.10 (Polynomial of degree 2). ‣ 3.3 Examples of fake stationary regimes of type I and II ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(x)=κ0+κ1​(x−μ0λ)+κ2​(x−μ0λ)2 with κi≥0,i=0,2,κ12≤4​κ2​κ0.\sigma(x)=\sqrt{\kappa\_{0}+\kappa\_{1}\,(x-\frac{\mu\_{0}}{\lambda})+\kappa\_{2}\,(x-\frac{\mu\_{0}}{\lambda})^{2}}\quad\mbox{ with }\quad\kappa\_{i}\geq 0,\;i=0,2,\;\kappa^{2}\_{1}\leq 4\kappa\_{2}\kappa\_{0}. |  | (6.60) |

![Refer to caption](x6.png)


Figure 9:  Graph of the stabilizer t→ςα,λ,c​(t)t\to\varsigma\_{\alpha,\lambda,c}(t) over time interval [0, T ], T = 10 for a value of
  
the Hurst esponent H=0.4H=0.4, λ=0.2\lambda=0.2, ρ=1.2\rho=1.2, c = 0.36.

![Refer to caption](x7.png)


Figure 10: Graph of the stabilizer t→ςα,λ,c​(t)t\to\varsigma\_{\alpha,\lambda,c}(t) over time interval [0, T ], T = 10 for a value of the Hurst esponent H=0.8H=0.8, λ=0.2\lambda=0.2, ρ=1.2\rho=1.2, c = 0.36.

![Refer to caption](x8.png)


Figure 11: Graph of tk↦StdDev​(tk,M)t\_{k}\mapsto\text{StdDev}(t\_{k},M) and tk↦𝔼​[σ2​(Xtk,M)]t\_{k}\mapsto\mathbb{E}[\sigma^{2}(X\_{t\_{k}},M)] over the time interval [0,T][0,T], T=1T=1, H=0.8H=0.8, μ0=2\mu\_{0}=2, λ=0.2\lambda=0.2, v0=0.09v\_{0}=0.09, ρ=1.2\rho=1.2, and StdDev​(X0)=0.3\text{StdDev}(X\_{0})=0.3. Number of steps: n=800n=800, Simulation size: M=100000M=100000.

![Refer to caption](x9.png)


Figure 12: Graph of tk↦StdDev​(tk,M)t\_{k}\mapsto\text{StdDev}(t\_{k},M) and tk↦𝔼​[σ2​(Xtk,M)]t\_{k}\mapsto\mathbb{E}[\sigma^{2}(X\_{t\_{k}},M)] over the time interval [0,T][0,T], T=1T=1, H=0.4H=0.4, μ0=2\mu\_{0}=2, λ=0.2\lambda=0.2, v0=0.09v\_{0}=0.09, ρ=1.2\rho=1.2, and StdDev​(X0)=0.3\text{StdDev}(X\_{0})=0.3. Number of steps: n=800n=800, Simulation size: M=100000M=100000.

![Refer to caption](x10.png)


Figure 13: Graph of tk↦StdDev​(tk,M)t\_{k}\mapsto\text{StdDev}(t\_{k},M) and tk↦𝔼​[σ2​(Xtk,M)]t\_{k}\mapsto\mathbb{E}[\sigma^{2}(X\_{t\_{k}},M)] over the time interval [0,T][0,T], T=1T=1, H=0.1H=0.1, μ0=2\mu\_{0}=2, λ=0.2\lambda=0.2, v0=0.09v\_{0}=0.09, ρ=1.2\rho=1.2, and StdDev​(X0)=0.3\text{StdDev}(X\_{0})=0.3. Number of steps: n=800n=800, Simulation size: M=150000M=150000.

Acknowledgement: The authors thank J-F. Chassagneux and M. Rosenbaum for insightful discussions, help and comments.

## References

* [1]

  O. I. Marichev A. A. Kilbas and S. G. Samko.
  Fractional integrals and derivatives (theory and applications).
  1993.
* [2]

  E. Abi Jaber, M. Larsson, and S. Pulido.
  Affine volterra processes.
  The Annals of Applied Probability, 29:3155–3200, 2019.
* [3]

  E. Alos and D. Nualart.
  Anticipating stochastic volterra equations.
  Stochastic Process. Appl., 72(1):73–95, 1997.
* [4]

  S. Norlund B. Gripenberg and O. Saavalainen.
  Volterra Integral and Functional Equations.
  *Encyclopedia of Mathematics and its Applications*. Cambridge
  University Press, Cambridge, UK, 1990.
* [5]

  M. A. Berger and V. J. Mizel.
  Volterra equations with ito integrals i.
  J. Integral Equations, 2(3):187–245, 1980.
* [6]

  M. A. Berger and V. J. Mizel.
  Volterra equations with ito integrals ii.
  J. Integral Equations, 2(4):319–337, 1980.
* [7]

  S. Bernstein.
  Sur les fonctions absolument monotones.
  Acta Mathematica, 52:1–66, 1929.
* [8]

  N. H. Bingham, C. M. Goldie, and J. L. Teugels.
  Regular variation, volume 27 of Encyclopedia of
  Mathematics and its Applications.
  Cambridge University Press, Cambridge, 1989.
* [9]

  Florian Bourgey and Jim Gatheral.
  The ssr under quadratic rough heston.
  SSRN Electronic Journal, 2025.
  Available at SSRN: <https://ssrn.com/abstract=5239929>.
* [10]

  Giorgia Callegaro, Martino Grasselli, and Gilles Pagès.
  Fast hybrid schemes for fractional Riccati equations (rough is not
  so tough).
  Math. Oper. Res., 46(1):221–254, 2021.
* [11]

  Eric Carlen and Paul Krée.
  LpL^{p} estimates on iterated stochastic integrals.
  Annals of Probability, 19(1):354–368, 1991.
* [12]

  W. G. Cochran, J.-S. Lee, and J. Potthoff.
  Stochastic volterra equations with singular kernels.
  Stochastic Process. Appl., 56(2):337–349, 1995.
* [13]

  Fabienne Comte and Eric Renault.
  Long memory in continuous-time stochastic volatility models.
  Math. Finance, 8(4):291–323, 1998.
* [14]

  L. Coutin and L. Decreusefond.
  Stochastic volterra equations with singular kernels.
  In Stochastic analysis and mathematical physics, volume 50 of
  Progr. Probab., pages 39–50. Birkhäuser Boston, 2001.
* [15]

  L. Coutin and L. Decreusefond.
  Stochastic Volterra equations with singular kernels.
  In Stochastic analysis and mathematical physics, volume 50 of
  Progr. Probab., pages 39–50. Birkhäuser Boston, Boston, MA, 2001.
* [16]

  Omar El Euch and Mathieu Rosenbaum.
  Perfect hedging in rough Heston models.
  Ann. Appl. Probab., 28(6):3813–3856, 2018.
* [17]

  Omar El Euch and Mathieu Rosenbaum.
  The characteristic function of rough Heston models.
  Mathematical Finance, 29(1):3–38, 2019.
* [18]

  Martin Friesen and Peng Jin.
  Volterra square-root process: Stationarity and regularity of the law,
  2022.
* [19]

  Jim Gatheral, Thibault Jaisson, and Mathieu Rosenbaum.
  Volatility is rough.
  Quant. Finance, 18(6):933–949.
* [20]

  Jim Gatheral, Paul Jusselin, and Mathieu Rosenbaum.
  The quadratic rough Heston model and the joint S&P 500/VIX smile
  calibration problem.
  arXiv e-prints, page arXiv:2001.01789, January 2020.
* [21]

  E. Gnabeyeu, G. Pagès, and M. Rosenbaum.
  On stationarity of Time-inhomogeneous Affine Volterra
  process: Finite-Time, Functional Weak Asymptotics and Applications.
  2025.
  working paper.
* [22]

  E. Gnabeyeu and M. Rosenbaum.
  On the Microstructural Foundation of the
  Time-Inhomogeneous Rough Fractional Square-Root Process.
  2025.
  working paper.
* [23]

  R. Gorenflo and F. Mainardi.
  Fractional calculus: Integral and differential equations of
  fractional order.
  In A. Carpinteri and F. Mainardi, editors, Fractals and
  Fractional Calculus in Continuum Mechanics, pages 223–276. Springer Verlag,
  Wien, 1997.
  [E-print arxiv.org/abs/0805.3823].
* [24]

  Rudolf Gorenflo, Anatoly A. Kilbas, Francesco Mainardi, and Sergei V. Rogosin.
  Mittag-Leffler Functions, Related Topics and Applications.
  Springer Monographs in Mathematics. Springer, Berlin, Heidelberg,
  2020.
* [25]

  Rudolf Gorenflo and Francesco Mainardi.
  Fractional calculus: integral and differential equations of
  fractional order.
  In Fractals and fractional calculus in continuum mechanics
  (Udine, 1996), volume 378 of CISM Courses and Lect., pages 223–276.
  Springer, Vienna, 1997.
* [26]

  L. De Haan and A. Ferreira.
  *Extreme Value Theory: An Introduction*.
  Springer Science & Business Media, 2006.
* [27]

  Steven L. Heston.
  A closed-form solution for options with stochastic volatility with
  applications to bond and currency options.
  The Review of Financial Studies, 6(2):327–343, 1993.
* [28]

  Antoine Jacquier, Alexandre Pannier, and Konstantinos Spiliopoulos.
  On the ergodic behaviour of affine Volterra processes.
  arXiv e-prints, page arXiv:2204.05270, April 2022.
* [29]

  Thibault Jaisson and Mathieu Rosenbaum.
  Rough fractional diffusions as scaling limits of nearly unstable
  heavy tailed Hawkes processes.
  Ann. Appl. Probab., 26(5):2860–2882, 2016.
* [30]

  Benjamin Jourdain and Gilles Pagès.
  Convex ordering for stochastic Volterra equations and their Euler
  schemes.
  arXiv e-prints, pages arXiv:2211.10186, to appear in Fin.
  & Stoch., November 2022.
* [31]

  P. E. Kloeden and E. Platen.
  *Numerical Solution of Stochastic Differential Equations*.
  Springer, 1999.
* [32]

  Francesco Mainardi.
  On some properties of the Mittag-Leffler function
  Eα​(−tα)E\_{\alpha}(-t^{\alpha}), completely monotone for t>0t>0 with 0<α<10<\alpha<1.
  Discrete Contin. Dyn. Syst. Ser. B, 19(7):2267–2278, 2014.
* [33]

  Francesco Mainardi and Rudolf Gorenflo.
  Fractional calculus: special functions and applications.
  In Advanced special functions and applications (Melfi, 1999),
  volume 1 of Proc. Melfi Sch. Adv. Top. Math. Phys., pages 165–188.
  Aracne, Rome, 2000.
* [34]

  Salah-Eldin A. Mohammed.
  *Stochastic differential systems with memory: Theory,
  examples and applications*.
  Birkhäuser Boston, Boston, MA, 1998.
* [35]

  G. Pagès.
  Numerical Probability: An Introduction with Applications to
  Finance.
  Springer, 2018.
* [36]

  G. Pagès.
  Volterra equations with affine drift: looking for stationarity.
  application to quadratic rough heston model.
  2024.
  working paper.
* [37]

  Gilles Pagès and Fabien. Panloup.
  Unadjusted langevin algorithm with multiplicative noise: total
  variation and wasserstein bounds.
  Ann. Appl. Probab., 33(1):726–779, 2023.
* [38]

  E. Pardoux and P. Protter.
  Stochastic volterra equations with anticipating coefficients.
  Ann. Probab., 18(4):1635–1655, 1990.
* [39]

  P. E. Protter.
  Stochastic integration and differential equations.
  2005.
* [40]

  Philip Protter.
  Volterra equations driven by semimartingales.
  Ann. Probab., 13(2):519–530, 1985.
* [41]

  Daniel Revuz and Marc Yor.
  Continuous martingales and Brownian motion, volume 293 of
  Grundlehren der mathematischen Wissenschaften [Fundamental Principles of
  Mathematical Sciences].
  Springer-Verlag, 1999.
* [42]

  Alexandre Richard, Xiaolu Tan, and Fan Yang.
  Discrete-time simulation of stochastic Volterra equations.
  Stochastic Process. Appl., 141:109–138, 2021.
* [43]

  L. C. G. Rogers and David Williams.
  Diffusions, Markov processes, and martingales. Vol. 2:
  Itô calculus.
  Cambridge: Cambridge University Press, 2nd ed. edition, 2000.
* [44]

  René L. Schilling, Renming Song, and Zoran Vondracek.
  Bernstein Functions, volume 37 of De Gruyter Studies in
  Mathematics.
  Walter de Gruyter, Berlin, 2010.
* [45]

  René L. Schilling, Renming Song, and Zoran Vondraček.
  Bernstein Functions: Theory and Applications, volume 37 of De Gruyter Studies in Mathematics.
  De Gruyter, Berlin, Boston, 2nd edition, 2012.
* [46]

  A. Segall T. Kailath and M. Zakai.
  Fubini-type theorems for stochastic integrals.
  Sankhyā: The Indian Journal of Statistics, pages 138–143.,
  1978.
* [47]

  M. Veraar.
  The stochastic fubini theorem revisited.
  Stochastics, 84(4):543–551, 2012.
* [48]

  J. B. Walsh.
  An introduction to stochastic partial differential equations.
  In P. L. Hennequin, editor, École d’Été de
  Probabilités de Saint Flour XIV–1984, volume 1180 of Lecture Notes
  in Mathematics, pages 265–439. Springer, Berlin, 1986.
* [49]

  Z. Wang.
  Existence and uniqueness of solutions to stochastic volterra
  equations with singular kernels and non-lipschitz coefficients.
  Statist. Probab. Lett., 78(9):1062–1071, 2008.
* [50]

  T. Yamada and S. Watanabe.
  On the uniqueness of solutions of stochastic differential equations.
  Journal of Mathematics of Kyoto University, 11(1):155–167,
  1971.
* [51]

  Xicheng Zhang.
  Stochastic Volterra equations in Banach spaces and stochastic
  partial differential equation.
  J. Funct. Anal., 258(4):1361–1425, 2010.

## Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE)

We aim at providing numerical approximation for the equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0​(ϕ​(t)−∫0tfλ​(t−s)​ϕ​(s)​𝑑s)+1λ​∫0tfλ​(t−s)​θ​(s)​𝑑s⏟=⁣:g​(t)+1λ​∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws⏟=⁣:(b).X\_{t}=\underbrace{X\_{0}(\phi(t)-\int\_{0}^{t}f\_{\lambda}(t-s)\phi(s)\,ds)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\theta(s)ds}\_{=:g(t)}+\underbrace{\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})dW\_{s}}\_{=:(b)}. |  | (A.61) |

We want to provide a more generalized scheme for equations of the type:

Xt=g​(t)+∫0tf​(t,s)​σ​(s,Xs)​𝑑Ws.X\_{t}=g(t)+\int\_{0}^{t}f(t,s)\,\sigma(s,X\_{s})dW\_{s}.

Where g(t) can be computed using
quadrature formulae on different intervals( Gauss-Legendre, Gauss-Laguerre etc.)
We introduce the following Euler-Maruyama scheme for the above equation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X¯tk\displaystyle\overline{X}\_{t\_{k}} | =g​(tk)+∑ℓ=1k∫tℓ−1tℓf​(tk,s)​σ​(tℓ−1,X¯tℓ−1)​𝑑Ws=g​(tk)+∑ℓ=1kσ​(tℓ−1,X¯tℓ−1)​Ikn,l\displaystyle=g(t\_{k})+\sum\_{\ell=1}^{k}\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{k},s)\,\sigma(t\_{\ell-1},\overline{X}\_{t\_{\ell-1}})dW\_{s}=g(t\_{k})+\sum\_{\ell=1}^{k}\sigma(t\_{\ell-1},\overline{X}\_{t\_{\ell-1}})I^{n,l}\_{k} |  | (A.62) |

where Ikn,l=∫tℓ−1tℓf​(tk,s)​𝑑WsI^{n,l}\_{k}=\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{k},s)dW\_{s} on the time grid tk=tkn=k​Tn,k=0,…,nt\_{k}=t^{n}\_{k}=\frac{kT}{n},k=0,\dots,n.
Due to the lack of Markovianity, X¯tkn\bar{X}\_{t^{n}\_{k}} is generally not a function of (X¯tk−1n,Wtkn−Wtk−1n)(\bar{X}\_{t^{n}\_{k-1}},W\_{t^{n}\_{k}}-W\_{t^{n}\_{k-1}}). However, it can be computed uniquely from (X¯0h,…,X¯tk−1n)(\bar{X}\_{0}^{h},\dots,\bar{X}\_{t^{n}\_{k-1}}) and the Gaussian vector (∫tℓ−1tℓf​(tkn,s)​𝑑Ws)ℓ=1,…,k\left(\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t^{n}\_{k},s)dW\_{s}\right)\_{\ell=1,\dots,k}, ensuring that the Euler-Maruyama scheme is well-defined by induction.
The exact simulation of the Euler-Maruyama scheme ([A.62](https://arxiv.org/html/2511.03474v1#A1.E62 "In Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE) ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) involves simulating the independent random vectors:(∫tℓntℓ+1nK2​(tkn,s)​𝑑Ws)ℓ≤k≤n,ℓ=1,…,n.\left(\int\_{t^{n}\_{\ell}}^{t^{n}\_{\ell+1}}K\_{2}(t^{n}\_{k},s)\,dW\_{s}\right)\_{\ell\leq k\leq n},\quad\ell=1,\dots,n.
Practitioner’s corner:.
We aim at providing all the Ikn,lI^{n,l}\_{k} at once.

|  |  |  |
| --- | --- | --- |
|  | I1n,ℓI2n,ℓ…Inn,ℓG1n,ℓG2n,ℓG3n,ℓ⋮Gnn,ℓ[Δ​Wtℓ∫tℓ−1tℓf​(t1,u)​f​(t2,u)​𝑑Wu∫tℓ−1tℓf​(t1,u)​f​(t3,u)​𝑑Wu⋯∫tℓ−1tℓf​(t1,u)​f​(tn,u)​𝑑Wu0Δ​Wtℓ∫tℓ−1tℓf​(t2,u)​f​(t3,u)​𝑑Wu⋯∫tℓ−1tℓf​(t2,u)​f​(tn,u)​𝑑Wu00Δ​Wtℓ⋯∫tℓ−1tℓf​(t3,u)​f​(tn,u)​𝑑Wu⋮⋮⋮⋱⋮000⋯Δ​Wtℓ]\begin{array}[]{c@{}c}&\begin{array}[]{cccccc}I^{n,\ell}\_{1}&I^{n,\ell}\_{2}&\dots&I^{n,\ell}\_{n}\\ \\ \end{array}\\[-4.62497pt] \begin{array}[]{c}G^{n,\ell}\_{1}\\ G^{n,\ell}\_{2}\\ G^{n,\ell}\_{3}\\ \vdots\\ G^{n,\ell}\_{n}\\ \end{array}&\begin{bmatrix}\Delta W\_{t\_{\ell}}&\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{1},u)f(t\_{2},u)\,dW\_{u}&\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{1},u)f(t\_{3},u)\,dW\_{u}&\cdots&\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{1},u)f(t\_{n},u)\,dW\_{u}\\[2.77501pt] 0&\Delta W\_{t\_{\ell}}&\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{2},u)f(t\_{3},u)\,dW\_{u}&\cdots&\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{2},u)f(t\_{n},u)\,dW\_{u}\\[2.77501pt] 0&0&\Delta W\_{t\_{\ell}}&\cdots&\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{3},u)f(t\_{n},u)\,dW\_{u}\\[2.77501pt] \vdots&\vdots&\vdots&\ddots&\vdots\\[2.77501pt] 0&0&0&\cdots&\Delta W\_{t\_{\ell}}\end{bmatrix}\end{array} |  |

We will rather consider and simulate the nn independent Gaussian vectors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gn,ℓ\displaystyle G^{n,\ell} | =(Δ​Wtl,[∫tℓntℓ+1nf​(tkn,s)​𝑑Ws]k=ℓ,…,n)=(Δ​Wtl,[Ikn,l]k=ℓ,…,n),ℓ=1,…,n.\displaystyle=\left(\Delta W\_{t\_{l}},\left[\int\_{t^{n}\_{\ell}}^{t^{n}\_{\ell+1}}f(t^{n}\_{k},s)\,dW\_{s}\right]\_{k=\ell,\ldots,n}\right)=\left(\Delta W\_{t\_{l}},\left[I^{n,l}\_{k}\right]\_{k=\ell,\ldots,n}\right),\qquad\ell=1,\ldots,n. |  |

Remark:
Note that we consider the Brownian increment in the above vector because, in applications to volatility model dynamics, the dynamics of the traded asset and its volatility process can be jointly driven by the same Brownian motion (see for exemple the quadratic rough volatility dynamic introduced in [[20](https://arxiv.org/html/2511.03474v1#bib.bib20)]). This approach takes into account, among other factors, the so-called Zumbach effect, which links the evolution of the asset or an index with its volatility.

The covariance matrix of ([Ikn,l]k=ℓ,…,n)\left(\left[I^{n,l}\_{k}\right]\_{k=\ell,\ldots,n}\right) is symmetric and (n−ℓ+1)×(n−ℓ+1)(n-\ell+1)\times(n-\ell+1), given by:

|  |  |  |
| --- | --- | --- |
|  | Σn,ℓ=[C​o​v​(Iin,l,Ijn,l)]ℓ≤i,j≤n=[∫tℓ−1tℓf​(ti,u)​f​(tj,u)​𝑑u]ℓ≤i,j≤n=[∫0T/nf​(tin,tℓn+u)​f​(tjn,tℓn+u)​𝑑u]ℓ≤i,j≤n.\Sigma^{n,\ell}=\left[Cov(I^{n,l}\_{i},I^{n,l}\_{j})\right]\_{\ell\leq i,j\leq n}=\left[\int\_{t\_{\ell-1}}^{t\_{\ell}}f(t\_{i},u)f(t\_{j},u)du\right]\_{\ell\leq i,j\leq n}=\left[\int\_{0}^{T/n}f(t^{n}\_{i},t^{n}\_{\ell}+u)f(t^{n}\_{j},t^{n}\_{\ell}+u)\,du\right]\_{\ell\leq i,j\leq n}. |  |

The covariance matrix of Gn,ℓG^{n,\ell} will be symmetric and (n−ℓ+2)×(n−ℓ+2)(n-\ell+2)\times(n-\ell+2) C:=Cn+1,1C:=C^{n+1,1}, given by:

|  |  |  |
| --- | --- | --- |
|  | C=(TnC0,1tC0,1Σn,1),C0,ℓ=[C​o​v​(Δ​Wtl,Iin,l)]ℓ≤i≤n=[∫0T/nf​(tin,tℓn+u)​𝑑u]ℓ≤k,k′≤n​ℓ=1,…,n,C=\begin{pmatrix}\frac{T}{n}&\begin{array}[]{ccc}{}^{t}C^{0,1}\end{array}\\[10.0pt] \begin{array}[]{c}C^{0,1}\end{array}&\Sigma^{n,1}\end{pmatrix},\;C^{0,\ell}=\left[Cov(\Delta W\_{t\_{l}},I^{n,l}\_{i})\right]\_{\ell\leq i\leq n}=\left[\int\_{0}^{T/n}f(t^{n}\_{i},t^{n}\_{\ell}+u)\,du\right]\_{\ell\leq k,k^{\prime}\leq n}\;\ell=1,\ldots,n, |  |

At this stage, we can compute any fixed sub-matrix of CC by a cubature formula (such as Trapezoid, Midpoint, Simpson, higher-order Newton-Cote, or Gauss-Legendre integration formulas) and then perform a numerically stable extended Cholesky transform. This results in the decomposition:

[Ci​j]1≤i,j≤n+1=T(n)​D(n)​T(n)⁣∗T(n)​ lower triangular.[C\_{ij}]\_{1\leq i,j\leq n+1}=T^{(n)}D^{(n)}T^{(n)\*}\quad T^{(n)}\text{ lower triangular}.

T(n)T^{(n)} is a lower triangular matrix with diagonal entries Ti​i(n)=1T^{(n)}\_{ii}=1, and D(n)D^{(n)} is a diagonal matrix with non-negative entries.
Then, taking advantage of the telescopic feature and the structure of this Cholesky transform one has:

|  |  |  |
| --- | --- | --- |
|  | [Ci​j]1≤i,j≤n+1−ℓ=[Ti​j(n)]1≤i,j≤n+1−ℓ​[Di​j(n)]1≤i,j≤n+1−ℓ​[Ti​j(n)]1≤i,j≤n+1−ℓ∗,ℓ=1,…,n.[C\_{ij}]\_{1\leq i,j\leq n+1-\ell}=[T\_{ij}^{(n)}]\_{1\leq i,j\leq n+1-\ell}[D^{(n)}\_{ij}]\_{1\leq i,j\leq n+1-\ell}[T\_{ij}^{(n)}]^{\*}\_{1\leq i,j\leq n+1-\ell},\;\ell=1,\ldots,n. |  |

Finally, for each ℓ=1,…,n\ell=1,\ldots,n, we have: (Gn+1,ℓ)ℓ=1,…,n=d(T~(n+1−ℓ)​Z(ℓ))ℓ=1,…,n,(G^{n+1,\ell})\_{\ell=1,\dots,n}\stackrel{{\scriptstyle d}}{{=}}(\tilde{T}^{(n+1-\ell)}Z^{(\ell)})\_{\ell=1,\dots,n}, where

|  |  |  |
| --- | --- | --- |
|  | Z(ℓ)∼𝒩​(0,In−ℓ+2)andT~(n+1−ℓ)=[Ti​j(n)]1≤i,j≤n+1−ℓ​[Di​j(n)]1≤i,j≤n+1−ℓ.Z^{(\ell)}\sim\mathcal{N}(0,I\_{n-\ell+2})\quad\text{and}\quad\tilde{T}^{(n+1-\ell)}=[T\_{ij}^{(n)}]\_{1\leq i,j\leq n+1-\ell}[\sqrt{D^{(n)}\_{ij}}]\_{1\leq i,j\leq n+1-\ell}. |  |

Remark:
This Cholesky matrix is usually quite sparse (when HH is small in the case of fractional kernel for example) since, all entries beyond the fourth column are numerically 0 (in fact smaller than 10−410^{-4}). This is due to the fact that such singular kernels have essentially no memory for small HH. This feature quickly disappears when running the procedure with H>1/2H>1/2.

Application in the Fake Stationary case with ϕ​(t)=1​∀t≥0\phi(t)=1\;\forall t\geq 0.
([A.61](https://arxiv.org/html/2511.03474v1#A1.E61 "In Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE) ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) can be re-written as follow:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=μ0λ+(X0−μ0λ)​Rλ​(t)+1λ​∫0tfλ​(t−s)​σ​(s,Xs)​𝑑Ws.X\_{t}=\frac{\mu\_{0}}{\lambda}+(X\_{0}-\frac{\mu\_{0}}{\lambda})R\_{\lambda}(t)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\sigma(s,X\_{s})dW\_{s}. |  | (A.63) |

knowing that μ​(s)=μ0\mu(s)=\mu\_{0} and noting that ∫0tfλ​(s)​𝑑s=1−Rλ​(t)\int\_{0}^{t}f\_{\lambda}(s)ds=1-R\_{\lambda}(t).
Here f​(t,s)=1λ​fλ​(t−s)f(t,s)=\frac{1}{\lambda}f\_{\lambda}(t-s). The Euler-Maruyama scheme ([A.62](https://arxiv.org/html/2511.03474v1#A1.E62 "In Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE) ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) on the time grid tk=tkn=k​Tn,k=0,…,nt\_{k}=t^{n}\_{k}=\frac{kT}{n},k=0,\dots,n, write recursively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X¯tk=μ0λ+(X0−μ0λ)​Rλ​(tk)+∑ℓ=1k∫tℓ−1tℓfλ​(tk−s)​ς​(tℓ)λ​σ​(X¯tℓ−1)​𝑑Ws=g​(tk)+∑ℓ=1kς​(tℓ)λ​σ​(X¯tℓ−1)​Ikn,l\displaystyle\overline{X}\_{t\_{k}}=\frac{\mu\_{0}}{\lambda}+\big(X\_{0}-\frac{\mu\_{0}}{\lambda}\big)R\_{\lambda}(t\_{k})+\sum\_{\ell=1}^{k}\int\_{t\_{\ell-1}}^{t\_{\ell}}f\_{\lambda}(t\_{k}-s)\,\frac{\varsigma(t\_{\ell})}{\lambda}\sigma(\overline{X}\_{t\_{\ell-1}})dW\_{s}=g(t\_{k})+\sum\_{\ell=1}^{k}\frac{\varsigma(t\_{\ell})}{\lambda}\sigma(\overline{X}\_{t\_{\ell-1}})I^{n,l}\_{k} |  | (A.64) |

where the integrals (Ikn,l=∫tℓ−1tℓfλ​(tk−s)​𝑑Ws)k\left(I^{n,l}\_{k}=\int\_{t\_{\ell-1}}^{t\_{\ell}}f\_{\lambda}(t\_{k}-s)dW\_{s}\right)\_{k} can be simulated on the discrete grid (tkn)0≤k≤n(t^{n}\_{k})\_{0\leq k\leq n} by generating an independent sequence of gaussian vectors Gn,l,l=1​⋯​nG^{n,l},l=1\cdots n using the Cholesky decomposition of the covariance matrix CC of these vectors which read (setting u=Tn​(ℓ−v)u=\frac{T}{n}(\ell-v), v∈[0,1]v\!\in[0,1]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σn,ℓ\displaystyle\Sigma^{n,\ell} | =[C​o​v​(Ikn,l,Ik′n,l)]ℓ≤k,k′≤n=[∫tℓ−1tℓfλ​(tk−u)​fλ​(tk′−u)​𝑑u]ℓ≤k,k′≤n,ℓ=1,…,n,\displaystyle=\left[Cov(I^{n,l}\_{k},I^{n,l}\_{k^{\prime}})\right]\_{\ell\leq k,k^{\prime}\leq n}=\left[\int\_{t\_{\ell-1}}^{t\_{\ell}}f\_{\lambda}(t\_{k}-u)f\_{\lambda}(t\_{k^{\prime}}-u)du\right]\_{\ell\leq k,k^{\prime}\leq n},\;\ell=1,\ldots,n, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Tn)​[∫01fλ​(Tn​(k−l+v))​fλ​(Tn​(k′−l+v))​𝑑v]ℓ≤k,k′≤n=(Tn)​[Ωk−ℓ,k′−ℓn]ℓ≤k,k′≤n,\displaystyle=\left(\frac{T}{n}\right)\left[\int\_{0}^{1}f\_{\lambda}(\frac{T}{n}(k-l+v))f\_{\lambda}(\frac{T}{n}(k^{\prime}-l+v))dv\right]\_{\ell\leq k,k^{\prime}\leq n}=\left(\frac{T}{n}\right)\big[\Omega^{n}\_{k-\ell,k^{\prime}-\ell}\big]\_{\ell\leq k,k^{\prime}\leq n}, |  |

where the symmetric matrix Ωn\Omega^{n} is defined by Ωn:=[∫01fλ​(Tn​(i+v))​fλ​(Tn​(j+v))​𝑑v]i,j≥0\Omega^{n}:=\left[\int\_{0}^{1}f\_{\lambda}(\frac{T}{n}(i+v))f\_{\lambda}(\frac{T}{n}(j+v))dv\right]\_{i,j\geq 0} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ0,ℓ\displaystyle\Sigma^{0,\ell} | =[Cov​(Δtℓ,, ​Ikn,ℓ)]ℓ≤k,k′≤n=[∫tℓ−1tℓfλ​(tk−u)​du]ℓ≤k,k′≤n\displaystyle=\left[\mathrm{Cov}\left(\Delta\_{t\_{\ell}},\text{,\ }I^{n,\ell}\_{k}\right)\right]\_{\ell\leq k,k^{\prime}\leq n}=\left[\int\_{t\_{\ell-1}}^{t\_{\ell}}f\_{\lambda}(t\_{k}-u)\,\mathrm{d}u\right]\_{\ell\leq k,k^{\prime}\leq n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[Rλ​(tk−tℓ)−Rλ​(tk−tℓ−1)]ℓ≤k,k′≤n=(Tn)​[∫01fλ​(Tn​(k−ℓ+v))​dv]ℓ≤k,k′≤n\displaystyle=\left[R\_{\lambda}(t\_{k}-t\_{\ell})-R\_{\lambda}(t\_{k}-t\_{\ell-1})\right]\_{\ell\leq k,k^{\prime}\leq n}=\left(\frac{T}{n}\right)\left[\int\_{0}^{1}f\_{\lambda}\left(\frac{T}{n}(k-\ell+v)\right)\,\mathrm{d}v\right]\_{\ell\leq k,k^{\prime}\leq n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Tn)​[Ωk−ℓ,k′−ℓ0]ℓ≤k,k′≤n,ℓ=1,…,n.so that​C:=Cn+1=(Tn)​(1Ω0Ω0Ωn).\displaystyle=\left(\frac{T}{n}\right)\left[\Omega^{0}\_{k-\ell,k^{\prime}-\ell}\right]\_{\ell\leq k,k^{\prime}\leq n},\qquad\ell=1,\ldots,n.\qquad\text{so that}\qquad C:=C^{n+1}=\left(\frac{T}{n}\right)\begin{pmatrix}1&\begin{array}[]{ccc}\Omega^{0}\end{array}\\[10.0pt] \begin{array}[]{c}\Omega^{0}\end{array}&\Omega^{n}\end{pmatrix}. |  |

Remark 1.
If the fonction fλf\_{\lambda} is a monone (case where we replace it mutantis mutandis by the fractional integration kernel K​(u)=K1,α,0​(u)=uα−1Γ​(α),u∈[0,T]K(u)=K\_{1,\alpha,0}(u)=\frac{u^{\alpha-1}}{\Gamma(\alpha)},u\in[0,T], where α∈(1/2,1)\alpha\!\in(1/2,1)), we will have the fact that CnC^{n} is a certain power factor of (Tn)\left(\frac{T}{n}\right), say Ψ​(Tn)β\Psi\left(\frac{T}{n}\right)^{\beta}, times an infinite symmetric matrix (Γ¯\bar{\Gamma}) (not depending on n anyway) defined by Γ¯:=[∫01((i+v)​(j+v))(α−1)​𝑑v]i,j≥0.\bar{\Gamma}:=\left[\int\_{0}^{1}\big((i+v)(j+v)\big)^{(\alpha-1)}dv\right]\_{i,j\geq 0}.
In this case, the diagonal entries of Γ¯\bar{\Gamma} have closed form formular and the matrices of interest [Ci​j]0⁣≤,i,j≤n−1[C\_{ij}]\_{0\leq,i,j\leq n-1}, n≥1n\geq 1 are telescopic sub-matrices of Γ¯\bar{\Gamma} times the factor Ψ​(Tn)β\Psi\left(\frac{T}{n}\right)^{\beta}.

2. For comprehensive results concerning convergence rates and *a priori* error estimates related to the approximation of the stochastic Volterra process ([A.63](https://arxiv.org/html/2511.03474v1#A1.E63 "In Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE) ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) by the semi-integrated Euler–Maruyama scheme ([A.64](https://arxiv.org/html/2511.03474v1#A1.E64 "In Appendix A About the Simulation of the semi-integrated scheme for stochastic Volterra integral Equations (SVIE) ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), as well as its continuous-time (or “genuine”) extension, the reader is referred to [[30](https://arxiv.org/html/2511.03474v1#bib.bib30)].

## Appendix B Supplementary material and Proofs.

Proof of Proposition [2.4](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem4 "Proposition 2.4 (Wiener-Hopf and Resolvent equations). ‣ 2.3 Application to the Wiener-Hopf equation ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"):
Convoluting x​(t)+λ​∫0tK​(t−s)​x​(s)​𝑑sx(t)+\lambda\int\_{0}^{t}K(t-s)x(s)ds with Rλ′R^{\prime}\_{\lambda} together with the fact that λ​K∗Rλ′=−λ​K−Rλ′\lambda K\*R^{\prime}\_{\lambda}=-\lambda K-R^{\prime}\_{\lambda}(see equation [2.9](https://arxiv.org/html/2511.03474v1#S2.E9 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") ), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tg​(s)​Rλ′​(t−s)​𝑑s\displaystyle\int\_{0}^{t}g(s)R^{\prime}\_{\lambda}(t-s)ds | =∫0tx​(s)​Rλ′​(t−s)​𝑑s+λ​∫0t∫0sK​(s−u)​x​(u)​𝑑u​Rλ′​(t−s)​𝑑s\displaystyle=\int\_{0}^{t}x(s)R^{\prime}\_{\lambda}(t-s)ds+\lambda\int\_{0}^{t}\int\_{0}^{s}K(s-u)x(u)duR^{\prime}\_{\lambda}(t-s)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tx​(s)​Rλ′​(t−s)​𝑑s+λ​∫0t∫0t−uK​(t−u−s)​Rλ′​(s)​𝑑s​x​(u)​𝑑u\displaystyle=\int\_{0}^{t}x(s)R^{\prime}\_{\lambda}(t-s)ds+\lambda\int\_{0}^{t}\int\_{0}^{t-u}K(t-u-s)R^{\prime}\_{\lambda}(s)dsx(u)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tx​(s)​Rλ′​(t−s)​𝑑s+∫0t(−λ​K​(t−u)−Rλ′​(t−u))​x​(u)​𝑑u=−λ​∫0tK​(t−s)​x​(s)​𝑑s.\displaystyle=\int\_{0}^{t}x(s)R^{\prime}\_{\lambda}(t-s)ds+\int\_{0}^{t}\big(-\lambda K(t-u)-R^{\prime}\_{\lambda}(t-u)\big)x(u)du=-\lambda\int\_{0}^{t}K(t-s)x(s)ds. |  |

Inserting this in the Wiener-Hopf equation gives the results.
For the second claim, we can use the Laplace transform in the integral equation and deduced that:

Lx​(t)=Lh​(t)1+LRλ′​(t)=Lh​(t)​(1+λ​LK​(t))=Lh+λ​K∗h​(t)L\_{x}(t)=\frac{L\_{h}(t)}{1+L\_{R^{\prime}\_{\lambda}}(t)}=L\_{h}(t)\big(1+\lambda L\_{K}(t)\big)=L\_{h+\lambda K\*h}(t)

where the penultimate equality comes from applying the Laplace transform to Rλ′∗K=−K−Rλ′λR^{\prime}\_{\lambda}\*K=-K-\frac{R^{\prime}\_{\lambda}}{\lambda} (see Equation ([2.9](https://arxiv.org/html/2511.03474v1#S2.E9 "In 2.2 Fourier-Laplace transforms and Solvent core of a convolutive kernel ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))). We then conclude by the injectivity of the Laplace transform.

Proof of Lemma [3.1](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem1 "Lemma 3.1. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"). For our convenience, we will consider two cases:

Case 1 (fλf\_{\lambda} is a probability density). If fλ>0f\_{\lambda}>0 on (0,+∞)(0,+\infty) (i.e. RλR\_{\lambda} decreases), then the function fλf\_{\lambda} is a probability density.
Upon replacing μ\mu with μμ∞\frac{\mu}{\mu\_{\infty}}, we can assume that μ​(t)\mu(t) tends to 1 as t becomes large.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tfλ​(t−s)​μ​(s)​𝑑s−μ∞​(1−a)\displaystyle\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds-\mu\_{\infty}(1-a) | =∫0tfλ​(t−s)​μ​(s)​𝑑s−μ∞​∫0+∞fλ​(s)​𝑑s\displaystyle=\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds-\mu\_{\infty}\int\_{0}^{+\infty}f\_{\lambda}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tfλ​(t−s)​(μ​(s)−μ∞)​𝑑s−μ∞​∫t+∞fλ​(s)​𝑑s\displaystyle=\int\_{0}^{t}f\_{\lambda}(t-s)(\mu(s)-\mu\_{\infty})\,ds-\mu\_{\infty}\int\_{t}^{+\infty}f\_{\lambda}(s)\,ds |  |

so that, by the triangle inequality, we have:

|∫0tfλ​(t−s)​μ​(s)​𝑑s−μ∞​(1−a)|≤∫0tfλ​(t−s)​|μ​(s)−μ∞|​𝑑s+μ∞​∫t+∞fλ​(s)​𝑑s\left|\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds-\mu\_{\infty}(1-a)\right|\leq\int\_{0}^{t}f\_{\lambda}(t-s)\left|\mu(s)-\mu\_{\infty}\right|\,ds+\mu\_{\infty}\int\_{t}^{+\infty}f\_{\lambda}(s)\,ds

First note that we can split the first integral as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tfλ​(t−s)​|μ​(s)−μ∞|​𝑑s\displaystyle\int\_{0}^{t}f\_{\lambda}(t-s)\left|\mu(s)-\mu\_{\infty}\right|\,ds | =∫0t−Aϵfλ​(t−s)​|μ​(s)−μ∞|​𝑑s+∫t−Aϵtfλ​(t−s)​|μ​(s)−μ∞|​𝑑s\displaystyle=\int\_{0}^{t-A\_{\epsilon}}f\_{\lambda}(t-s)\left|\mu(s)-\mu\_{\infty}\right|\,ds+\int\_{t-A\_{\epsilon}}^{t}f\_{\lambda}(t-s)\left|\mu(s)-\mu\_{\infty}\right|\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Aϵtfλ​(s)​|μ​(t−s)−μ∞|​𝑑s+∫0Aϵfλ​(s)​|μ​(t−s)−μ∞|​𝑑s.\displaystyle=\int\_{A\_{\epsilon}}^{t}f\_{\lambda}(s)\left|\mu(t-s)-\mu\_{\infty}\right|\,ds+\int\_{0}^{A\_{\epsilon}}f\_{\lambda}(s)\left|\mu(t-s)-\mu\_{\infty}\right|\,ds. |  |

where AϵA\_{\epsilon} is chosen such that for all s≥Aϵs\geq A\_{\epsilon}, we have |μ​(s)−μ∞|≤ϵ|\mu(s)-\mu\_{\infty}|\leq\epsilon. Moreover ∀s∈]0,Aϵ[,t−s≥t−Aϵ≥Aϵ\forall s\in]0,A\_{\epsilon}[,\quad t-s\geq t-A\_{\epsilon}\geq A\_{\epsilon} for t large enough, (say t≥2​Aϵt\geq 2A\_{\epsilon}), and hence, this implies that |μ(t−s)−μ∞|≤ϵ,∀s∈]0,Aϵ[\left|\mu(t-s)-\mu\_{\infty}\right|\leq\epsilon,\quad\forall s\in]0,A\_{\epsilon}[.

We thus have: ∫0tfλ​(t−s)​|μ​(s)−μ∞|​𝑑s≤‖μ−μ∞‖sup​∫Aϵtfλ​(s)​𝑑s+ϵ​∫0Aϵfλ​(s)​𝑑s.\int\_{0}^{t}f\_{\lambda}(t-s)\left|\mu(s)-\mu\_{\infty}\right|\,ds\leq\|\mu-\mu\_{\infty}\|\_{\sup}\int\_{A\_{\epsilon}}^{t}f\_{\lambda}(s)\,ds+\epsilon\int\_{0}^{A\_{\epsilon}}f\_{\lambda}(s)\,ds.
And hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞|∫0tfλ​(t−s)​μ​(s)​𝑑s−μ∞​(1−a)|\displaystyle\lim\_{t\to\infty}\left|\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds-\mu\_{\infty}(1-a)\right| | ≤‖μ−μ∞‖∞​limt→∞∫Aϵtfλ​(s)​𝑑s+ϵ​∫0Aϵfλ​(s)​𝑑s\displaystyle\leq\|\mu-\mu\_{\infty}\|\_{\infty}\lim\_{t\to\infty}\int\_{A\_{\epsilon}}^{t}f\_{\lambda}(s)\,ds+\epsilon\int\_{0}^{A\_{\epsilon}}f\_{\lambda}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +μ∞​limt→∞∫t+∞fλ​(s)​𝑑s≤ϵ​(1−a)≤ϵ,since​∫0∞fλ​(s)​𝑑s=1−a.\displaystyle+\mu\_{\infty}\lim\_{t\to\infty}\int\_{t}^{+\infty}f\_{\lambda}(s)\,ds\leq\epsilon(1-a)\leq\epsilon,\qquad\text{since}\int\_{0}^{\infty}f\_{\lambda}(s)\,ds=1-a. |  |

Case 2 (fλf\_{\lambda} is just a 1-sum measure). If ∫0+∞fλ​(s)​𝑑s=1\int\_{0}^{+\infty}f\_{\lambda}(s)\,ds=1 , a more rigorous Approach to prove the above Lemma make used of Laplace Transforms - and Tauberian Final Value Theorem. Let’s assume the L1L^{1}-integrability of fλf\_{\lambda}, i.e., ∫0∞|fλ​(s)|​𝑑s<∞\int\_{0}^{\infty}|f\_{\lambda}(s)|ds<\infty so that L|fλ|​(t)<+∞L\_{|f\_{\lambda}|}(t)<+\infty for every t>0t>0: fλf\_{\lambda} has subsequently
a finite Laplace transform defined (at least) on ℝ+\mathbb{R}^{+}.

Since limt→+∞μ​(t)=μ∞\lim\_{t\to+\infty}\mu(t)=\mu\_{\infty}, we have by Tauberian Final Value Theorem limz→0z​Lμ​(z)=μ∞\lim\_{z\to 0}zL\_{\mu}(z)=\mu\_{\infty}. As the Laplace transform of the convolution is the product of the Laplace transforms, we have:

ℒ​(∫0tfλ​(t−s)​μ​(s)​𝑑s)​(z)=Lfλ​(z)​Lμ​(z)\mathcal{L}\left(\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds\right)(z)=L\_{f\_{\lambda}}(z)L\_{\mu}(z)

Therefore, by Tauberian Final Value Theorem if limt→+∞∫0tfλ​(t−s)​μ​(s)​𝑑s\lim\_{t\to+\infty}\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds exists, then

|  |  |  |
| --- | --- | --- |
|  | limt→+∞∫0tfλ​(t−s)​μ​(s)​𝑑s=limz→0z​ℒ​(∫0tfλ​(t−s)​μ​(s)​𝑑s)​(z)=limz→0z​Lμ​(z)​Lfλ​(z)=μ∞​limz→0Lfλ​(z)\lim\_{t\to+\infty}\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds=\lim\_{z\to 0}z\mathcal{L}\left(\int\_{0}^{t}f\_{\lambda}(t-s)\mu(s)ds\right)(z)=\lim\_{z\to 0}zL\_{\mu}(z)L\_{f\_{\lambda}}(z)=\mu\_{\infty}\lim\_{z\to 0}L\_{f\_{\lambda}}(z) |  |

However, by our assumption ∫0∞fλ​(s)​𝑑s=1−a\int\_{0}^{\infty}f\_{\lambda}(s)ds=1-a, we have limz→0Lfλ​(z)=limz→0∫0∞e−z​s​fλ​(s)​𝑑s=Lfλ​(0)=∫0∞fλ​(s)​𝑑s=1−a\lim\_{z\to 0}L\_{f\_{\lambda}}(z)=\lim\_{z\to 0}\int\_{0}^{\infty}e^{-zs}f\_{\lambda}(s)ds=L\_{f\_{\lambda}}(0)=\int\_{0}^{\infty}f\_{\lambda}(s)ds=1-a.
  
Consequently, we have
limt→+∞ϕ​(t)−(fλ∗ϕ)​(t)=ϕ∞−ϕ∞​(1−a)=ϕ∞​a.\lim\_{t\to+\infty}\phi(t)-(f\_{\lambda}\*\phi)(t)=\phi\_{\infty}-\phi\_{\infty}(1-a)=\phi\_{\infty}\,a.
This completes the proof.

Proof of Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

Step 1. 
The equation [3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") can be expressed in terms of the Laplace transform as follows:
c​λ2​L1−(ϕ−fλ∗ϕ)2=Lfλ2​Lς2.c\lambda^{2}L\_{1-(\phi-f\_{\lambda}\*\phi)^{2}}=L\_{f\_{\lambda}^{2}}L\_{\varsigma^{2}}.

In order to get rid of the Laplace transform of 1−(ϕ−fλ∗ϕ)21-(\phi-f\_{\lambda}\*\phi)^{2}, we apply integration by parts using (ϕ−fλ∗ϕ)(\phi-f\_{\lambda}\*\phi) as the integrator, treating it as a single function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L1−(ϕ−fλ∗ϕ)2​(t)\displaystyle L\_{1-(\phi-f\_{\lambda}\*\phi)^{2}}(t) | =L1​(t)−L(ϕ−fλ∗ϕ)2​(t)\displaystyle=L\_{1}(t)-L\_{(\phi-f\_{\lambda}\*\phi)^{2}}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1t−((ϕ−fλ∗ϕ)2​(0)−limu→+∞e−t​u​(ϕ−fλ∗ϕ)2​(u)t+2t​L(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t))\displaystyle=\frac{1}{t}-\left(\frac{(\phi-f\_{\lambda}\*\phi)^{2}(0)-\lim\_{u\to+\infty}e^{-tu}(\phi-f\_{\lambda}\*\phi)^{2}(u)}{t}+\frac{2}{t}L\_{(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−2t​L(ϕ−fλ∗ϕ)​(ϕ−fλ∗ϕ)′​(t).\displaystyle=-\frac{2}{t}L\_{(\phi-f\_{\lambda}\*\phi)(\phi-f\_{\lambda}\*\phi)^{\prime}}(t). |  |

Thus, the Laplace counterpart of equation ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) simplifies to equation ([3.26](https://arxiv.org/html/2511.03474v1#S3.E26 "In Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).

Step 2.  The second assertion is straightforward, noting that ϕ​(t)−(fλ∗ϕ)​(t)=1−(fλ∗μ)tλ​x∞\phi(t)-(f\_{\lambda}\*\phi)(t)=1-\frac{(f\_{\lambda}\*\mu)\_{t}}{\lambda x\_{\infty}}, and applying the Leibniz rule for differentiating an integral along with the fact that the space (L1​(ℝ),+,⋅,∗)(L^{1}(\mathbb{R}),+,\cdot,\*) is a commutative algebra:

|  |  |  |
| --- | --- | --- |
|  | dd​t​(∫0tμ​(t−s)​fλ​(s)​𝑑s)=μ​(t−t)​fλ​(t)+∫0t∂∂t​(μ​(t−s)​fλ​(s))​𝑑s=μ​(0)​fλ​(t)+∫0tμ′​(t−s)​fλ​(s)​𝑑s.\displaystyle\frac{d}{dt}\left(\int\_{0}^{t}\mu(t-s)f\_{\lambda}(s)\,ds\right)=\mu(t-t)f\_{\lambda}(t)+\int\_{0}^{t}\frac{\partial}{\partial t}\left(\mu(t-s)f\_{\lambda}(s)\right)\,ds=\mu(0)f\_{\lambda}(t)+\int\_{0}^{t}\mu^{\prime}(t-s)f\_{\lambda}(s)\,ds. |  |

One recognises hereinabove the equation given in the Lemma.

Step 3.  If ςλ,c1\varsigma\_{\lambda,c}^{1} and ςλ,c2\varsigma\_{\lambda,c}^{2} are two solutions of the equation (Eλ,cE\_{\lambda,c}) in ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), then fλ2∗δ​ςλ,c=0f\_{\lambda}^{2}\*\delta\varsigma\_{\lambda,c}=0 in Lloc1​(ℝ+)L^{1}\_{\text{loc}}(\mathbb{R}^{+}) with δ​ςλ,c=ςλ,c1−ςλ,c2\delta\varsigma\_{\lambda,c}=\varsigma\_{\lambda,c}^{1}-\varsigma\_{\lambda,c}^{2}. As Lfλ2​(t)>0L\_{f^{2}\_{\lambda}}(t)>0 for t>0t>0 (by Assumption (𝒦{\cal K})(ii)), then δ​g=0\delta g=0, which implies δ​ςλ,c=0\delta\varsigma\_{\lambda,c}=0 in Lloc1​(ℝ+)L^{1}\_{\text{loc}}(\mathbb{R}^{+}). Thus, the solution ςλ,c2\varsigma^{2}\_{\lambda,c} of Equation ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) if any, is unique.

We would also note that, cc being fixed, Lfλ2​(t)>0L\_{f^{2}\_{\lambda}}(t)>0 for t>0t>0 (by Assumption (𝒦{\cal K})(ii)). Then Lςλ,c2L\_{\varsigma^{2}\_{\lambda,c}} is uniquely determined by ([3.26](https://arxiv.org/html/2511.03474v1#S3.E26 "In Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), which in turn implies the uniqueness of ςλ,c2\varsigma^{2}\_{\lambda,c} (at least dt-a.e.).

Step 4.  ςλ,c2\varsigma^{2}\_{\lambda,c}
is non-negative and has a limit l∞∈(0,+∞]l\_{\infty}\in(0,+\infty] as t→+∞t\to+\infty. If l∞=+∞l\_{\infty}=+\infty, then for every A>0A>0, there exists tAt\_{A} such that for t≥tAt\geq t\_{A}, ςλ,c2​(t)≥A\varsigma^{2}\_{\lambda,c}(t)\geq A. Hence

(fλ2∗ςλ,c2)​(t)=∫0tAfλ2​(t−s)​ςλ,c2​(s)​𝑑s+∫tAtfλ2​(t−s)​ςλ,c2​(s)​𝑑s≥∫0tAfλ2​(t−s)​ςλ,c2​(s)​𝑑s+A​∫tAtfλ2​(t−s)​𝑑s(f\_{\lambda}^{2}\*\varsigma^{2}\_{\lambda,c})(t)=\int\_{0}^{t\_{A}}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds+\int\_{t\_{A}}^{t}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds\geq\int\_{0}^{t\_{A}}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds+A\int^{t}\_{t\_{A}}f\_{\lambda}^{2}(t-s)\,ds

i.e.

|  |  |  |
| --- | --- | --- |
|  | (fλ2∗ςλ,c2)​(t)≥∫0tAfλ2​(t−s)​ςλ,c2​(s)​𝑑s+A​∫0t−tAfλ2​(s)​𝑑s.(f\_{\lambda}^{2}\*\varsigma^{2}\_{\lambda,c})(t)\geq\int\_{0}^{t\_{A}}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds+A\int\_{0}^{t-t\_{A}}f\_{\lambda}^{2}(s)\,ds. |  |

Consequently, as (fλ2∗ςλ,c2)​(t)=c​λ2​(1−(ϕ−fλ∗ϕ)2​(t))→c​λ2​(1−a2​ϕ∞2)(f\_{\lambda}^{2}\ast\varsigma^{2}\_{\lambda,c})(t)=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}(t))\to c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2}) as t→+∞t\to+\infty owing to Lemma [3.1](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem1 "Lemma 3.1. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we have: c​λ2​(1−a2​ϕ∞2)=limt→+∞(fλ2∗ςλ,c2)​(t)≥A​∫0+∞fλ2​(u)​𝑑u.c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})=\lim\_{t\to+\infty}(f\_{\lambda}^{2}\ast\varsigma^{2}\_{\lambda,c})(t)\geq A\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\,du.
As fλ∈L2​(ℝ+,Leb1)f\_{\lambda}\in L^{2}(\mathbb{R}\_{+},\text{Leb}\_{1}), this yields a contradiction by letting A→∞A\to\infty. Hence, l∞<+∞l\_{\infty}<+\infty.
Now, still by the same arguments, limt→+∞ςλ,c2(t)=l∞∈(0,+∞[⟹∀η>0,∃tη∈ℝ+\lim\_{t\to+\infty}\varsigma^{2}\_{\lambda,c}(t)=l\_{\infty}\in(0,+\infty[\implies\forall\eta>0,\exists t\_{\eta}\in\mathbb{R}^{+} such that ∀t>tηl∞−η≤ςλ,c2​(t)≤l∞+η\forall t>t\_{\eta}\quad l\_{\infty}-\eta\leq\varsigma^{2}\_{\lambda,c}(t)\leq l\_{\infty}+\eta

On the first hand, we have:

|  |  |  |
| --- | --- | --- |
|  | (fλ2∗ςλ,c2)​(t)≥∫0tηfλ2​(t−s)​ςλ,c2​(s)​𝑑s+(l∞−η)​∫tηtfλ2​(t−s)​𝑑s=∫0tηfλ2​(t−s)​ςλ,c2​(s)​𝑑s+(l∞−η)​∫0t−tηfλ2​(s)​𝑑s.(f\_{\lambda}^{2}\*\varsigma^{2}\_{\lambda,c})(t)\geq\int\_{0}^{t\_{\eta}}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds+(l\_{\infty}-\eta)\int^{t}\_{t\_{\eta}}f\_{\lambda}^{2}(t-s)\,ds=\int\_{0}^{t\_{\eta}}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds+(l\_{\infty}-\eta)\int\_{0}^{t-t\_{\eta}}f\_{\lambda}^{2}(s)\,ds. |  |

Hence, we obtain:

c​λ2​(1−a2​ϕ∞2)=limt→+∞(fλ2∗ςλ,c2)​(t)≥(l∞−η)​∫0+∞fλ2​(u)​𝑑u⟹l∞≤c​λ2​(1−a2​ϕ∞2)∫0+∞fλ2​(s)​𝑑s​by letting​η→0.c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})=\lim\_{t\to+\infty}(f\_{\lambda}^{2}\ast\varsigma^{2}\_{\lambda,c})(t)\geq(l\_{\infty}-\eta)\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\,du\implies l\_{\infty}\leq\frac{c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})}{\int\_{0}^{+\infty}f^{2}\_{\lambda}(s)\,ds}\;\textit{by letting}\;\eta\to 0.

On the other hand, we also have:

|  |  |  |
| --- | --- | --- |
|  | (fλ2∗ςλ,c2)​(t)≤∫0tηfλ2​(t−s)​ςλ,c2​(s)​𝑑s+(l∞+η)​∫tηtfλ2​(t−s)​𝑑s=∫0tηfλ2​(t−s)​ςλ,c2​(s)​𝑑s+(l∞+η)​∫0t−tηfλ2​(s)​𝑑s.(f\_{\lambda}^{2}\*\varsigma^{2}\_{\lambda,c})(t)\leq\int\_{0}^{t\_{\eta}}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds+(l\_{\infty}+\eta)\int^{t}\_{t\_{\eta}}f\_{\lambda}^{2}(t-s)\,ds=\int\_{0}^{t\_{\eta}}f\_{\lambda}^{2}(t-s)\varsigma^{2}\_{\lambda,c}(s)\,ds+(l\_{\infty}+\eta)\int\_{0}^{t-t\_{\eta}}f\_{\lambda}^{2}(s)\,ds. |  |

Therefore, we obtain:

c​λ2​(1−a2​ϕ∞2)=limt→+∞(fλ2∗ςλ,c2)​(t)≤(l∞+η)​∫0+∞fλ2​(u)​𝑑u⟹l∞≥c​λ2​(1−a2​ϕ∞2)∫0+∞fλ2​(s)​𝑑sasη→0.c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})=\lim\_{t\to+\infty}(f\_{\lambda}^{2}\ast\varsigma^{2}\_{\lambda,c})(t)\leq(l\_{\infty}+\eta)\int\_{0}^{+\infty}f\_{\lambda}^{2}(u)\,du\implies l\_{\infty}\geq\frac{c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})}{\int\_{0}^{+\infty}f^{2}\_{\lambda}(s)\,ds}\quad\textit{as}\quad\eta\to 0.

This completes the proof and we are done. □\square

Proof of Proposition [3.1](https://arxiv.org/html/2511.03474v1#S3.Thmprop1 "Proposition 3.1 (Equivalence). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
We adapt the proof of the corresponding Proposition in [[36](https://arxiv.org/html/2511.03474v1#bib.bib36)] in order to prove the equivalence of the two statements or claims above.

(i)⇒(i​i)(i)\Rightarrow(ii) Assume Var​(Xt)=Var​(X0)=v0{\rm Var}(X\_{t})={\rm Var}(X\_{0})=v\_{0} for every t≥0t\geq 0. If v0=0v\_{0}=0, then Xt=x∞X\_{t}=x\_{\infty} a.s.a.s. for every t≥0t\geq 0. Consequently 𝔼​σ2​(Xt)=𝔼​σ2​(μ∞λ)\mathbb{E}\,\sigma^{2}(X\_{t})=\mathbb{E}\,\sigma^{2}\big(\frac{\mu\_{\infty}}{\lambda}\big) which is constant over time anyway.
Assume that v0>0v\_{0}>0. Then, since the constant cc is finite, it follows that 𝔼​[σ2​(X0)]>0\mathbb{E}[\sigma^{2}(X\_{0})]>0. Define the function

g​(t)=ςλ,c2​(𝔼​[σ2​(Xt)]𝔼​[σ2​(X0)]−1).g(t)=\varsigma^{2}\_{\lambda,c}\left(\frac{\mathbb{E}[\sigma^{2}(X\_{t})]}{\mathbb{E}[\sigma^{2}(X\_{0})]}-1\right).

We can check using equation ([3.22](https://arxiv.org/html/2511.03474v1#S3.E22 "In 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and (Eλ,c)(E\_{\lambda,c}) that this function satisfies the convolution equation fλ2∗g=0f^{2}\_{\lambda}\*g=0 with the initial condition g​(0)=0g(0)=0.
Furthermore, under the assumption that σ\sigma has linear growth, the expectation 𝔼​[σ2​(Xt)]\mathbb{E}[\sigma^{2}(X\_{t})] remains bounded due to the boundedness of 𝔼​[Xt2]\mathbb{E}[X\_{t}^{2}]. As a consequence, the function gg, along with its positive and negative parts g+g^{+} and g−g^{-}, admits a Laplace transform.

Since the Laplace transform of fλ2f^{2}\_{\lambda}, denoted Lfλ2L\_{f^{2}\_{\lambda}}, is not identically zero and is strictly positive on (0,+∞)(0,+\infty), we obtain:

Lfλ2⋅Lg+=Lfλ2⋅Lg−.L\_{f^{2}\_{\lambda}}\cdot L\_{g^{+}}=L\_{f^{2}\_{\lambda}}\cdot L\_{g^{-}}.

This implies Lg+=Lg−L\_{g^{+}}=L\_{g^{-}}, hence g+=g−g^{+}=g^{-}, and consequently g=0g=0.
(i​i)⇒(i)(ii)\Rightarrow(i) First, we have that σ¯02=σ¯t2=𝔼​σ2​(Xt)\bar{\sigma}^{2}\_{0}=\bar{\sigma}^{2}\_{t}=\mathbb{E}\,\sigma^{2}(X\_{t}), t≥0t\geq 0, so that it follows from Equation ([3.22](https://arxiv.org/html/2511.03474v1#S3.E22 "In 3.1.2 Towards stationarity of the variance ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and (Eλ,c)(E\_{\lambda,c}).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(Xt)\displaystyle{\rm Var}(X\_{t}) | =Var​(X0)​(ϕ−fλ∗ϕ)2​(t)+σ¯02λ2​(fλ2∗ςλ,c2)​(t)=Var​(X0)​(ϕ−fλ∗ϕ)2​(t)+v0c​λ2​(fλ2∗ςλ,c2)​(t)\displaystyle={\rm Var}(X\_{0})(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{\bar{\sigma}^{2}\_{0}}{\lambda^{2}}(f^{2}\_{\lambda}\*\varsigma\_{\lambda,c}^{2})(t)={\rm Var}(X\_{0})(\phi-f\_{\lambda}\*\phi)^{2}(t)+\frac{v\_{0}}{c\lambda^{2}}(f^{2}\_{\lambda}\*\varsigma\_{\lambda,c}^{2})(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Eλ,c)​v0​(ϕ−fλ∗ϕ)2​(t)+v0​(1−(ϕ−fλ∗ϕ)2​(t))=v0.\displaystyle\overset{(E\_{\lambda,c})}{\operatorname\*{=}}v\_{0}(\phi-f\_{\lambda}\*\phi)^{2}(t)+v\_{0}\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)=v\_{0}. |  |

Proof of Proposition [4.3](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem3 "Proposition 4.3 (Moment control). ‣ 4.1 Moments control. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"). Using equation ([3.2](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem2 "Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"))
and owing to ([3.21](https://arxiv.org/html/2511.03474v1#S3.E21 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we have: ∀t≥0\forall\,t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt−x∞\displaystyle X\_{t}-x\_{\infty} | =(X0−x∞)​(ϕ−fλ∗ϕ)​(t)+x∞​((ϕ−fλ∗ϕ)​(t)−1)+1λ​(fλ∗μ)t+1λ​(fλ∗Wς​(⋅)​σ​(X⋅))t\displaystyle=\Big(X\_{0}-x\_{\infty}\Big)(\phi-f\_{\lambda}\*\phi)(t)+x\_{\infty}\Big((\phi-f\_{\lambda}\*\phi)(t)-1\Big)+\frac{1}{\lambda}(f\_{\lambda}\*\mu)\_{t}+\frac{1}{\lambda}\left(f\_{\lambda}\stackrel{{\scriptstyle W}}{{\*}}\varsigma(\cdot)\sigma(X\_{\cdot})\right)\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(X0−x∞)​(ϕ−fλ∗ϕ)​(t)+1λ​∫0tfλ​(t−s)​ς​(s)​σ​(Xs)​𝑑Ws.\displaystyle=\Big(X\_{0}-x\_{\infty}\Big)(\phi-f\_{\lambda}\*\phi)(t)+\frac{1}{\lambda}\int\_{0}^{t}f\_{\lambda}(t-s)\varsigma(s)\sigma(X\_{s})\,dW\_{s}. |  |

so that in particular, |𝔼​(Xt)−x∞|≤|ϕ​(t)−(fλ∗ϕ)​(t)|​|𝔼​(X0)−x∞|=|1−(fλ∗μλ​x∞)t|​|𝔼​(X0)−x∞|\quad\Big|\mathbb{E}\,\big(X\_{t}\big)-x\_{\infty}\Big|\leq|\phi(t)-(f\_{\lambda}\*\phi)(t)|\Big|\mathbb{E}\,\big(X\_{0}\big)-x\_{\infty}\Big|=\Big|1-(f\_{\lambda}\*\frac{\mu}{\lambda x\_{\infty}})\_{t}\Big|\Big|\mathbb{E}\,\big(X\_{0}\big)-x\_{\infty}\Big|.
  
(a)(a)
Using elementary computations and Itô’s Isometry show that for every t≥0t\geq 0

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(|Xt−x∞|)2\displaystyle\mathbb{E}\,\Big(\Big|X\_{t}-x\_{\infty}\Big|\Big)^{2} | ≤𝔼​(|(X0−x∞)​(ϕ​(t)−(fλ∗ϕ)​(t))|2)+1λ2​∫0tfλ2​(t−s)​ς2​(s)​𝔼​(σ2​(Xs))​𝑑s.\displaystyle\leq\mathbb{E}\,\Big(\Big|(X\_{0}-x\_{\infty})(\phi(t)-(f\_{\lambda}\*\phi)(t))\Big|^{2}\Big)+\frac{1}{\lambda^{2}}\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\mathbb{E}\,\Big(\sigma^{2}(X\_{s})\Big)ds. |  |

Set ρ:=c​[σ]Lip2∈(0, 1)\rho:=c\,[\sigma]^{2}\_{\text{Lip}}\in(0,\,1) and let ϵ\epsilon in Remark [4.1](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem1 "Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") be equal to ϵ=ρη\epsilon=\frac{\rho}{\eta} where η∈(0, 1−ρ)\eta\in(0,\,1-\rho) is a free parameter such that ρ+η∈(0, 1)\rho+\eta\in(0,\,1).
From equation ([4.33](https://arxiv.org/html/2511.03474v1#S4.E33 "In Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")),
The real constants κi,i=0,2\kappa\_{i},\,i=0,2 depending on η\eta and given by
k0=k0​(η):=(1+ρη)​|σ​(x∞)|2k\_{0}=k\_{0}(\eta):=(1+\frac{\rho}{\eta})|\sigma(x\_{\infty})|^{2} and k2=k2​(η):=(1+ηρ)​[σ]Lip2k\_{2}=k\_{2}(\eta):=(1+\frac{\eta}{\rho})[\sigma]^{2}\_{\text{Lip}} so that c​κ2=ρ+η<1.c\,\kappa\_{2}=\rho+\eta<1.

Next, we have using equations ([4.33](https://arxiv.org/html/2511.03474v1#S4.E33 "In Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) (fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2})):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(|Xt−x∞|)2\displaystyle\mathbb{E}\,\Big(|X\_{t}-x\_{\infty}|\Big)^{2} | ≤𝔼​(|X0−x∞|)2​(ϕ−fλ∗ϕ)2​(t)+κ0​c​(1−(ϕ−fλ∗ϕ)2​(t))\displaystyle\leq\mathbb{E}\,\Big(|X\_{0}-x\_{\infty}|\Big)^{2}(\phi-f\_{\lambda}\*\phi)^{2}(t)+\kappa\_{0}c\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ2λ2​∫0tfλ2​(t−s)​ς2​(s)​𝔼​(|Xs−x∞|2)​𝑑s.\displaystyle+\frac{\kappa\_{2}}{\lambda^{2}}\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\mathbb{E}\,\Big(|X\_{s}-x\_{\infty}|^{2}\Big)ds. |  |

Now let A>A¯η:=κ0​c1−κ2​c∨𝔼​(|X0−x∞|)2A>\bar{A}\_{\eta}:=\frac{\kappa\_{0}c}{1-\kappa\_{2}c}\vee\mathbb{E}\,\Big(|X\_{0}-x\_{\infty}|\Big)^{2}, δ>0\delta>0 and
tδ=inf{t≥0:𝔼​(|Xt−x∞|)2≥A+δ}.t\_{\delta}=\inf\Big\{t\geq 0:\mathbb{E}\,\Big(|X\_{t}-x\_{\infty}|\Big)^{2}\geq A+\delta\Big\}.
As t↦𝔼​(|Xt−x∞|)2t\mapsto\mathbb{E}\,\Big(|X\_{t}-x\_{\infty}|\Big)^{2} is continuous and A>𝔼​(|X0−x∞|)2A>\mathbb{E}\,\Big(|X\_{0}-x\_{\infty}|\Big)^{2} it follows from the above inequality and the identity satisfied by ς\varsigma 131313fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}) that, if tδ<+∞t\_{\delta}<+\infty, then 𝔼​(|Xs−x∞|)2<A+δ∀s≤tδ\mathbb{E}\,\Big(|X\_{s}-x\_{\infty}|\Big)^{2}<A+\delta\quad\forall s\leq t\_{\delta} and we have:
A+δ=𝔼​(|Xtδ−μ∞λ|)2<A​(ϕ−fλ∗ϕ)2​(tδ)+(κ0​c+κ2​c​(A+δ))​(1−(ϕ−fλ∗ϕ)2​(tδ)).A+\delta=\mathbb{E}\,\Big(|X\_{t\_{\delta}}-\frac{\mu\_{\infty}}{\lambda}|\Big)^{2}<A(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})+\big(\kappa\_{0}c+\kappa\_{2}c(A+\delta)\big)\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})\big).
Now, as κ0​c+κ2​c​A<A\kappa\_{0}c+\kappa\_{2}cA<A by construction of AA, we have:

|  |  |  |
| --- | --- | --- |
|  | A+δ=𝔼(|Xtδ−x∞|)2<A(ϕ−fλ∗ϕ)2(tδ)+A(1−(ϕ−fλ∗ϕ)2(tδ))+κ2cδ((1−(ϕ−fλ∗ϕ)2(tδ))<A+δ.A+\delta=\mathbb{E}\,\Big(|X\_{t\_{\delta}}-x\_{\infty}|\Big)^{2}<A(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})+A(1-(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta}))+\kappa\_{2}c\delta\big((1-(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})\big)<A+\delta. |  |

As c is
so that c​κ2<1c\kappa\_{2}<1. This yields a contradiction. Consequently, tδ=+∞t\_{\delta}=+\infty which implies that 𝔼​(|Xt−x∞|)2≤A+δ\mathbb{E}\,\Big(|X\_{t}-x\_{\infty}|\Big)^{2}\leq A+\delta for every t≥0t\geq 0. Letting δ→0\delta\to 0 and
A→A¯ηA\to\bar{A}\_{\eta} successively, yields

supt≥0𝔼​(|Xt−x∞|)2≤A¯η=c​(1+ρη)​|σ​(x∞)|21−(1+ηρ)​c​[σ]Lip2=c​|σ​(x∞)|2​η+ρη​(1−ρ−η).\sup\_{t\geq 0}\mathbb{E}\,\Big(|X\_{t}-x\_{\infty}|\Big)^{2}\leq\bar{A}\_{\eta}=\frac{c(1+\frac{\rho}{\eta})|\sigma(x\_{\infty})|^{2}}{1-(1+\frac{\eta}{\rho})c[\sigma]^{2}\_{\text{Lip}}}=c|\sigma(x\_{\infty})|^{2}\frac{\eta+\rho}{\eta(1-\rho-\eta)}.

A straightforward computation shows that
η↦A¯η\eta\mapsto\bar{A}\_{\eta}
attains its minimum on (0, 1−ρ)(0,\,1-\rho)
at η=ρ−ρ\eta=\sqrt{\rho}-\rho. This minimum is given by c(1−ρ)2​|σ​(x∞)|2\frac{c}{(1-\sqrt{\rho})^{2}}|\sigma(x\_{\infty})|^{2} which completes the proof of the stated result.

(b)(b) Let p≥2p\geq 2. Set ρp:=c​(CpB​D​G)2​[σ]Lip2∈(0, 1)\rho\_{p}:=c\,(C\_{p}^{BDG})^{2}\,[\sigma]^{2}\_{\mathrm{Lip}}\in(0,\,1). Owing to the triangle inequality and applying the BDG inequality to the (a priori) local martingale Mu=∫0ufλ​(t−s)​ς​(s)​σ​(Xs)​𝑑WsM\_{u}=\int\_{0}^{u}f\_{\lambda}(t-s)\varsigma(s)\sigma(X\_{s})dW\_{s}, 0≤s≤t0\leq s\leq t, (see [[41](https://arxiv.org/html/2511.03474v1#bib.bib41), Proposition 4.3]) follow by the generalized Minkowski inequality, we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|Xt−x∞|‖p\displaystyle\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p} | ≤‖|X0−x∞|‖p​|ϕ​(t)−(fλ∗ϕ)​(t)​|+CpB​D​Gλ‖​(fλ2∗d​tς2​(⋅)​|σ​(X⋅)|2)t‖p212\displaystyle\leq\Big\||X\_{0}-x\_{\infty}|\Big\|\_{p}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|+\frac{C\_{p}^{BDG}}{\lambda}\Big\|\left(f\_{\lambda}^{2}\stackrel{{\scriptstyle dt}}{{\*}}\varsigma^{2}(\cdot)|\sigma(X\_{\cdot})|^{2}\right)\_{t}\Big\|\_{\frac{p}{2}}^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖|X0−x∞|‖p​|ϕ​(t)−(fλ∗ϕ)​(t)|+CpB​D​Gλ​(∫0tfλ2​(t−s)​ς2​(s)​‖|σ​(Xs)|2‖p2)12.\displaystyle\leq\Big\||X\_{0}-x\_{\infty}|\Big\|\_{p}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|+\frac{C\_{p}^{BDG}}{\lambda}\Big(\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\big\||\sigma(X\_{s})|^{2}\big\|\_{\frac{p}{2}}\Big)^{\frac{1}{2}}. |  |

Owing to the elementary inequality (a+b)2≤(1+1ϵ)​a2+(1+ϵ)​b2​∀ϵ∈(0,1/ρp−1)(a+b)^{2}\leq(1+\frac{1}{\epsilon})a^{2}+(1+\epsilon)b^{2}\;\forall\epsilon\!\in(0,1/\rho\_{p}-1), it follows that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|Xt−x∞|‖p2\displaystyle\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p}^{2} | ≤‖|X0−x∞|‖p2​|ϕ​(t)−(fλ∗ϕ)​(t)|2​(1+1/ϵ)+(CpB​D​G)2λ2​(1+ϵ)​∫0tfλ2​(t−s)​ς2​(s)​‖|σ​(Xs)|2‖p2​𝑑s\displaystyle\leq\Big\||X\_{0}-x\_{\infty}|\Big\|\_{p}^{2}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|^{2}(1+1/\epsilon)+\frac{(C^{BDG}\_{p})^{2}}{\lambda^{2}}(1+\epsilon)\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\||\sigma(X\_{s})|^{2}\|\_{\frac{p}{2}}ds |  |

Likewise, set ρ~p:=c​(CpB​D​G)2​[σ]Lip2​(1+ε)=ρp​(1+ε)∈(0, 1)\widetilde{\rho}\_{p}:=c\,(C\_{p}^{BDG})^{2}\,[\sigma]^{2}\_{\mathrm{Lip}}(1+\varepsilon)=\rho\_{p}(1+\varepsilon)\in(0,\,1) and let ϵ\epsilon in Remark [4.1](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem1 "Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") be equal to ρ~pη\frac{\widetilde{\rho}\_{p}}{\eta} where η∈(0, 1−ρ~p)\eta\in(0,\,1-\widetilde{\rho}\_{p}) is a free parameter such that ρ~p+η∈(0, 1)\widetilde{\rho}\_{p}+\eta\in(0,\,1).
From equation ([4.33](https://arxiv.org/html/2511.03474v1#S4.E33 "In Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")),
The real constants κi,i=0,2\kappa\_{i},\,i=0,2 depending on η\eta are given by
k0=k0​(η):=(1+ρ~pη)​|σ​(x∞)|2k\_{0}=k\_{0}(\eta):=(1+\frac{\widetilde{\rho}\_{p}}{\eta})|\sigma(x\_{\infty})|^{2} and k2=k2​(η):=(1+ηρ~p)​[σ]Lip2k\_{2}=k\_{2}(\eta):=(1+\frac{\eta}{\widetilde{\rho}\_{p}})[\sigma]^{2}\_{\text{Lip}} so that c​(CpB​D​G)2​(1+ε)​κ2=ρ~p+η<1.c\,(C\_{p}^{BDG})^{2}\,(1+\varepsilon)\,\kappa\_{2}=\widetilde{\rho}\_{p}+\eta<1.
As p2≥1\frac{p}{2}\geq 1, according to the remark [4.1](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem1 "Remark 4.1. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), ‖|σ​(Xs)|2‖p2≤κ0+κ2​‖|Xs−x∞|‖p2\Big\||\sigma(X\_{s})|^{2}\Big\|\_{\frac{p}{2}}\leq\kappa\_{0}+\kappa\_{2}\Big\||X\_{s}-x\_{\infty}|\Big\|^{2}\_{p}
which entails, combined with the identity fλ2∗ς2=c​λ2​(1−(ϕ−fλ∗ϕ)2)f^{2}\_{\lambda}\*\varsigma^{2}=c\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}), that, for every t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ‖|Xt−x∞|‖p2≤‖|X0−x∞|‖p2​|ϕ​(t)−(fλ∗ϕ)​(t)|2​(1+1ϵ)\displaystyle\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p}^{2}\leq\Big\||X\_{0}-x\_{\infty}|\Big\|\_{p}^{2}\Big|\phi(t)-(f\_{\lambda}\*\phi)(t)\Big|^{2}(1+\frac{1}{\epsilon}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(CpB​D​G)2​(1+ϵ)​(κ0​c​(1−(ϕ−fλ∗ϕ)2​(t))+κ2λ2​∫0tfλ2​(t−s)​ς2​(s)​‖|Xs−x∞|‖p2​𝑑s).\displaystyle\hskip 45.52458pt+(C^{BDG}\_{p})^{2}(1+\epsilon)\Big(\kappa\_{0}c\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)\big)+\frac{\kappa\_{2}}{\lambda^{2}}\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\Big\||X\_{s}-x\_{\infty}|\Big\|^{2}\_{p}ds\Big). |  | (B.65) |

Now let A>A¯η,ϵ:=κ0​c​(CpB​D​G)2​(1+ϵ)1−κ2​c​(CpB​D​G)2​(1+ϵ)∨[(1+1/ϵ)​‖|X0−x∞|‖p2]A>\bar{A}\_{\eta,\epsilon}:=\frac{\kappa\_{0}c(C^{BDG}\_{p})^{2}(1+\epsilon)}{1-\kappa\_{2}c(C^{BDG}\_{p})^{2}(1+\epsilon)}\vee\Big[(1+1/\epsilon)\Big\||X\_{0}-x\_{\infty}|\Big\|\_{p}^{2}\Big], δ>0\delta>0 and tδ=inf{t≥0:‖|Xt−x∞|‖p2≥A+δ}.t\_{\delta}=\inf\Big\{t\geq 0:\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p}^{2}\geq A+\delta\Big\}.
If tδ<+∞t\_{\delta}<+\infty, then, on the one hand, it follows from the continuity of t↦‖|Xt−x∞|‖p2t\mapsto\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p}^{2} that A+δ=‖|Xtδ−x∞|‖p2A+\delta=\Big\||X\_{t\_{\delta}}-x\_{\infty}|\Big\|\_{p}^{2} and, on the other hand, from Equation ([3.25](https://arxiv.org/html/2511.03474v1#S3.E25 "In Definition 3.7. ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) satisfied by ς\varsigma, that
∫0tfλ2​(t−s)​ς2​(s)​‖|Xs−x∞|‖p2​𝑑s≤A​c​λ2​(1−(ϕ−fλ∗ϕ)2​(t)).\int\_{0}^{t}f^{2}\_{\lambda}(t-s)\varsigma^{2}(s)\Big\||X\_{s}-x\_{\infty}|\Big\|\_{p}^{2}ds\leq Ac\lambda^{2}(1-(\phi-f\_{\lambda}\*\phi)^{2}(t)).\quad
Moreover, since A>‖X0−x∞‖p2​(1+1ϵ)A>\left\|X\_{0}-x\_{\infty}\right\|\_{p}^{2}(1+\frac{1}{\epsilon}), we deduce from ([B.65](https://arxiv.org/html/2511.03474v1#A2.E65 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) the inequalities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A+δ\displaystyle A+\delta | =‖|Xtδ−x∞|‖p2<A​(ϕ−fλ∗ϕ)2​(tδ)+(CpB​D​G)2​(1+ϵ)​(κ0​c+κ2​c​(A+δ))​(1−(ϕ−fλ∗ϕ)2​(tδ))\displaystyle=\Big\||X\_{t\_{\delta}}-x\_{\infty}|\Big\|\_{p}^{2}<A(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})+(C^{BDG}\_{p})^{2}(1+\epsilon)\big(\kappa\_{0}c+\kappa\_{2}c(A+\delta)\big)\big(1-(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <A(ϕ−fλ∗ϕ)2(tδ)+A(1−(ϕ−fλ∗ϕ)2(tδ))+(CpB​D​G)2(1+ϵ)cκ2δ((1−(ϕ−fλ∗ϕ)2(tδ))\displaystyle<A(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})+A(1-(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta}))+(C^{BDG}\_{p})^{2}(1+\epsilon)c\kappa\_{2}\delta\big((1-(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <A+δ((1−(ϕ−fλ∗ϕ)2(tδ))<A+δ.\displaystyle<A+\delta\big((1-(\phi-f\_{\lambda}\*\phi)^{2}(t\_{\delta})\big)<A+\delta. |  |

Here, the second inequality uses the bound (CpBDG)2​(1+ϵ)​c​(κ0+κ2​A)<A(C^{\mathrm{BDG}}\_{p})^{2}(1+\epsilon)\,c\,(\kappa\_{0}+\kappa\_{2}A)<A
which holds by the very definition of AA, while the penultimate inequality follows from the assumption that (CpB​D​G)2​(1+ϵ)​c​κ2<1(C^{BDG}\_{p})^{2}(1+\epsilon)c\kappa\_{2}<1. This yields a contradiction. Consequently, tδ=+∞t\_{\delta}=+\infty which implies that ‖|Xtδ−x∞|‖p2≤A+δ\Big\||X\_{t\_{\delta}}-x\_{\infty}|\Big\|\_{p}^{2}\leq A+\delta for every t≥0t\geq 0. Letting δ→0\delta\to 0 and
A→A¯η,ϵA\to\bar{A}\_{\eta,\epsilon} successively, yields

supt≥0‖|Xt−x∞|‖p≤A¯η,ϵ12=(ρ~p[σ]Lip2​|σ​(x∞)|2​η+ρ~pη​(1−ρ~p−η))12<+∞.\sup\_{t\geq 0}\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p}\leq\bar{A}^{\frac{1}{2}}\_{\eta,\epsilon}=\left(\frac{\widetilde{\rho}\_{p}}{[\sigma]^{2}\_{\text{Lip}}}|\sigma(x\_{\infty})|^{2}\frac{\eta+\widetilde{\rho}\_{p}}{\eta(1-\widetilde{\rho}\_{p}-\eta)}\right)^{\frac{1}{2}}<+\infty.

A straightforward computation shows that the mapping
η↦A¯η,η\eta\mapsto\bar{A}\_{\eta,\eta} attains its minimum on the interval
(0, 1−ρ~p)(0,\,1-\widetilde{\rho}\_{p}) at η=ρ~p−ρ~p\eta=\sqrt{\widetilde{\rho}\_{p}}-\widetilde{\rho}\_{p}, this minimum being
ρ~p[σ]Lip2​(1−ρ~p)2​|σ​(x∞)|2=c​(CpB​D​G)2​(1+ϵ)(1−[σ]Lip​c​(CpB​D​G)2​(1+ϵ))2​|σ​(x∞)|2\frac{\widetilde{\rho}\_{p}}{[\sigma]^{2}\_{\text{Lip}}(1-\sqrt{\widetilde{\rho}\_{p}})^{2}}\big|\sigma(x\_{\infty})\big|^{2}=\frac{c(C^{BDG}\_{p})^{2}(1+\epsilon)}{(1-[\sigma]\_{\text{Lip}}\sqrt{c(C^{BDG}\_{p})^{2}(1+\epsilon)})^{2}}\big|\sigma(x\_{\infty})\big|^{2},
which completes the proof.
The stated results follows by setting CpB​D​G=2​pC^{BDG}\_{p}=2\sqrt{p} owing to Lemma [4.2](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem2 "Lemma 4.2 (Best constant in a BDG inequality (see Remark 2 in carlen1991lp )). ‣ 4.1 Moments control. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"). □\square

Proof of Theorem [4.6](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem6 "Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
It follows from ([4.41](https://arxiv.org/html/2511.03474v1#S4.E41 "In Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that either p=2p=2 and c<1κ2c<\frac{1}{\kappa\_{2}}, or p>2p>2 and c<1(CpB​D​G)2​κ2c<\frac{1}{(C\_{p}^{BDG})^{2}\kappa\_{2}}. Hence, Proposition [4.3](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem3 "Proposition 4.3 (Moment control). ‣ 4.1 Moments control. ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") implies that supt≥0‖|Xt−x∞|‖p<+∞\sup\_{t\geq 0}\Big\||X\_{t}-x\_{\infty}|\Big\|\_{p}<+\infty.
As a consequence of σ\sigma having at most affine growth, we derive that supt≥0‖|σ​(Xt)|‖p<+∞\sup\_{t\geq 0}\Big\||\sigma(X\_{t})|\Big\|\_{p}<+\infty.

Step 1. (Kolmogorov criterion).
Now, we can establish C-tightness by the Kolmogorov criterion. Let pp be given by ([4.41](https://arxiv.org/html/2511.03474v1#S4.E41 "In Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")). One writes for s,t≥0s,\,t\geq 0 with s≤ts\leq t and owing to equation [3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"):

|  |  |  |
| --- | --- | --- |
|  | Xt−Xs=((ϕ−fλ∗ϕ)​(t)−(ϕ−fλ∗ϕ)​(s))​X0+1λ​(J​(t)−J​(s)+I​(t)−I​(s)).X\_{t}-X\_{s}=\big((\phi-f\_{\lambda}\*\phi)(t)-(\phi-f\_{\lambda}\*\phi)(s)\big)X\_{0}+\frac{1}{\lambda}\Big(J(t)-J(s)+I(t)-I(s)\Big). |  |

Where we set: J​(t):=∫0tfλ​(t−u)​ς​(u)​σ​(Xu)​𝑑WuJ(t):=\int\_{0}^{t}f\_{\lambda}(t-u)\varsigma(u)\sigma(X\_{u})dW\_{u} and I​(t)=∫0tfλ​(t−u)​μ​(u)​𝑑uI(t)=\int\_{0}^{t}f\_{\lambda}(t-u)\mu(u)\,du.
On the first hand,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |(fα,λ∗ϕ)​(t)−(fα,λ∗ϕ)​(s)|\displaystyle\Big|(f\_{\alpha,\lambda}\*\phi)(t)-(f\_{\alpha,\lambda}\*\phi)(s)\Big| | =|∫0s[fα,λ​(t−u)−fα,λ​(s−u)]​ϕ​(u)​𝑑u+∫stfα,λ​(t−u)​ϕ​(u)​𝑑u|\displaystyle=\Big|\int\_{0}^{s}\left[f\_{\alpha,\lambda}(t-u)-f\_{\alpha,\lambda}(s-u)\right]\phi(u)\,du+\int\_{s}^{t}f\_{\alpha,\lambda}(t-u)\phi(u)\,du\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supu≥0|ϕ​(u)|​(∫0s|(fα,λ​(t−u)−fα,λ​(s−u))|​𝑑u+∫st|fα,λ​(t−u)|​𝑑u).\displaystyle\leq\sup\_{u\geq 0}|\phi(u)|\Bigg(\int\_{0}^{s}|\left(f\_{\alpha,\lambda}(t-u)-f\_{\alpha,\lambda}(s-u)\right)|du+\int\_{s}^{t}|f\_{\alpha,\lambda}(t-u)|du\Bigg). |  |

Consequently, we obtain the following bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥\displaystyle\Big\| | |((ϕ−fλ∗ϕ)(t)−(ϕ−fλ∗ϕ)(s))X0|∥p=∥|X0|∥p|(|(fα,λ∗ϕ)(s)−(fα,λ∗ϕ)(t)|+|ϕ(t)−ϕ(s)|)\displaystyle|\big((\phi-f\_{\lambda}\*\phi)(t)-(\phi-f\_{\lambda}\*\phi)(s)\big)X\_{0}|\Big\|\_{p}=\Big\||X\_{0}|\Big\|\_{p}|\Big(|(f\_{\alpha,\lambda}\*\phi)(s)-(f\_{\alpha,\lambda}\*\phi)(t)|+|\phi(t)-\phi(s)|\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖|X0|‖p​‖ϕ‖∞​(C​|t−s|ϑ+(∫0+∞fα,λ2​β​(u)​𝑑u)12​β​|t−s|1−12​β)+Cp′​(1+‖ϕ‖∞​‖|X0|‖p)​|t−s|δ\displaystyle\leq\Big\||X\_{0}|\Big\|\_{p}\|\phi\|\_{\infty}\Bigg(C\;|t-s|^{\vartheta}+\left(\int\_{0}^{+\infty}f\_{\alpha,\lambda}^{2\beta}(u)du\right)^{\frac{1}{2\beta}}|t-s|^{1-\frac{1}{2\beta}}\Bigg)+C^{\prime}\_{p}\left(1+\|\phi\|\_{\infty}\left\||X\_{0}|\right\|\_{p}\right)|t-s|^{\delta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cp,X0,ϕ,β,fλ​|t−s|ϑ​(1−12​β)∧δ.\displaystyle\leq C\_{p,X\_{0},\phi,\beta,f\_{\lambda}}|t-s|^{\vartheta(1-\frac{1}{2\beta})\wedge\delta}. |  |

where the penultimate inequality come from assumption [2.2](https://arxiv.org/html/2511.03474v1#S2.ThmTheorem2 "Assumption 2.2 (On Volterra Equations with convolutive kernels). ‣ 2.1 Volterra processes with convolutive kernels ‣ 2 Background on Stochastic Volterra equations with convolutive kernels ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (iii).
Next, by using generalized Minkowski inequalities, one gets similarly:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖|I​(t)−I​(s)|‖p\displaystyle\Big\||I(t)-I(s)|\Big\|\_{p} | ≤‖|∫stfλ​(t−u)​μ​(u)​𝑑u|‖p+‖|∫0s(fλ​(t−u)−fλ​(s−u))​μ​(u)​𝑑u|‖p\displaystyle\leq\left\||\int\_{s}^{t}f\_{\lambda}(t-u)\mu(u)\,du|\right\|\_{p}+\left\||\int\_{0}^{s}\left(f\_{\lambda}(t-u)-f\_{\lambda}(s-u)\right)\mu(u)\,du|\right\|\_{p} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supu≥0|μ​(u)|×(∫st|fλ​(t−u)|​𝑑u+∫0s|(fλ​(t−u)−fλ​(s−u))|​𝑑u)\displaystyle\leq\sup\_{u\geq 0}|\mu(u)|\times\Bigg(\int\_{s}^{t}|f\_{\lambda}(t-u)|\,du+\int\_{0}^{s}|\left(f\_{\lambda}(t-u)-f\_{\lambda}(s-u)\right)|\,du\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖μ‖∞×((∫0+∞fλ2​β​(u)​𝑑u)12​β​(t−s)1−12​β+∫0s|fλ​(t−u)−fλ​(s−u)|​𝑑u)\displaystyle\leq\|\mu\|\_{\infty}\times\Bigg(\Big(\int\_{0}^{+\infty}f\_{\lambda}^{2\beta}(u)du\Big)^{\frac{1}{2\beta}}(t-s)^{1-\frac{1}{2\beta}}+\int\_{0}^{s}|f\_{\lambda}(t-u)-f\_{\lambda}(s-u)|\,du\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cp,μ,fλ​|t−s|(ϑ∧(1−12​β)).\displaystyle\leq C\_{p,\mu,f\_{\lambda}}|t-s|^{(\vartheta\wedge(1-\frac{1}{2\beta}))}. |  |

On the other hand, combining the LpL^{p}-BDG and the generalized Minkowski inequality, one derives from ([4.41](https://arxiv.org/html/2511.03474v1#S4.E41 "In Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that,

|  |  |  |
| --- | --- | --- |
|  | ‖|J​(t)−J​(s)|‖p≤‖|∫stfλ​(t−u)​ς​(u)​σ​(Xu)​dWu|‖p+‖|∫0s(fλ​(t−u)−fλ​(s−u))​ς​(u)​σ​(Xu)​𝑑Wu|‖p\displaystyle\ \Big\||J(t)-J(s)|\Big\|\_{p}\leq\left\||\int\_{s}^{t}f\_{\lambda}(t-u)\varsigma(u)\sigma(X\_{u})\mathrm{d}W\_{u}|\right\|\_{p}+\left\||\int\_{0}^{s}\left(f\_{\lambda}(t-u)-f\_{\lambda}(s-u)\right)\varsigma(u)\sigma(X\_{u})dW\_{u}|\right\|\_{p} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​‖ς2‖∞​[(∫stfα,λ2​(t−u)​‖|σ​(Xu)|‖p2​𝑑u)12+(∫0s(fα,λ​(t−u)−fα,λ​(s−u))2​‖|σ​(Xu)|‖p2​𝑑u)12]\displaystyle\leq C\_{p}\|\varsigma^{2}\|\_{\infty}\left[\Big(\int\_{s}^{t}f^{2}\_{\alpha,\lambda}(t-u)\big\||\sigma(X\_{u})|\big\|\_{p}^{2}du\Big)^{\frac{1}{2}}+\Big(\int\_{0}^{s}\big(f\_{\alpha,\lambda}(t-u)-f\_{\alpha,\lambda}(s-u)\big)^{2}\big\||\sigma(X\_{u})|\big\|\_{p}^{2}du\Big)^{\frac{1}{2}}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​‖ς2‖∞​supu≥0‖|σ​(Xu)|‖p​[(∫0+∞fα,λ2​β​(u)​𝑑u)12​β​|t−s|β−12​β+(∫0+∞(fα,λ​(t−s+u)−fα,λ​(u))2​𝑑u)12]\displaystyle\leq C\_{p}\|\varsigma^{2}\|\_{\infty}\sup\_{u\geq 0}\Big\||\sigma(X\_{u})|\Big\|\_{p}\left[\Big(\int\_{0}^{+\infty}f^{2\beta}\_{\alpha,\lambda}(u)du\Big)^{\frac{1}{2\beta}}|t-s|^{\frac{\beta-1}{2\beta}}+\left(\int\_{0}^{+\infty}\big(f\_{\alpha,\lambda}(t-s+u)-f\_{\alpha,\lambda}(u)\big)^{2}du\right)^{\frac{1}{2}}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp,ς,fλ⋅(1+‖ϕ‖T​‖|X0|‖p)​|t−s|ϑ∧β−12​β:=Cp,T,σ,ς,fλ,X0⋅|t−s|ϑ∧β−12​β​where​Cp≡CpB​D​G.\displaystyle\leq C\_{p,\varsigma,f\_{\lambda}}\cdot\left(1+\|\phi\|\_{T}\Big\||X\_{0}|\Big\|\_{p}\right)|t-s|^{\vartheta\wedge\frac{\beta-1}{2\beta}}:=C\_{p,T,\sigma,\varsigma,f\_{\lambda},X\_{0}}\cdot|t-s|^{\vartheta\wedge\frac{\beta-1}{2\beta}}\qquad\text{where}\qquad C\_{p}\equiv C^{BDG}\_{p}. |  |

Finally, putting all these estimates together, since β−12​β≤1−12​β\frac{\beta-1}{2\beta}\leq 1-\frac{1}{2\beta} we have the existence of a real constant Cp,X0,ϕ,β,λ,fλ>0C\_{p,X\_{0},\phi,\beta,\lambda,f\_{\lambda}}>0 such that:

𝔼​(|Xt−Xs|)p≤Cp,X0,ϕ,β,λ,fλ​|t−s|p​(δ∧ϑ∧β−12​β)\mathbb{E}\,\left(|X\_{t}-X\_{s}|\right)^{p}\leq C\_{p,X\_{0},\phi,\beta,\lambda,f\_{\lambda}}|t-s|^{p(\delta\wedge\vartheta\wedge\frac{\beta-1}{2\beta})}

Define for u≥0u\geq 0 the process XuX^{u} by Xtu=Xt+uX^{u}\_{t}=X\_{t+u}, where t≥0t\geq 0. Then XuX^{u} has continuous sample paths and satisfies

supu≥0𝔼​[|Xtu−Xsu|p]≤C​(p)​|t−s|p​(δ∧ϑ∧β−12​β)for ​0≤t−s≤1.\sup\_{u\geq 0}\mathbb{E}[|X^{u}\_{t}-X^{u}\_{s}|^{p}]\leq C(p)|t-s|^{p(\delta\wedge\vartheta\wedge\frac{\beta-1}{2\beta})}\quad\text{for }0\leq t-s\leq 1.

As p​(δ∧ϑ∧β−12​β)>1p(\delta\wedge\vartheta\wedge\frac{\beta-1}{2\beta})>1 according to equation ([4.41](https://arxiv.org/html/2511.03474v1#S4.E41 "In Theorem 4.6. ‣ 4.3 Asymptotics: Long run functional weak behaviour: ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), it follows from Kolmogorov’s CC-tightness criterion (see [[41](https://arxiv.org/html/2511.03474v1#bib.bib41), Theorem 2.1, p. 26, 3rd edition] 141414If a process XX taking values in a Polish space (S,ρ)(S,\rho) satisfies
𝔼​[ρ​(Xs,Xt)α]≤c​|s−t|β+d\mathbb{E}[\rho(X\_{s},X\_{t})^{\alpha}]\leq c|s-t|^{\beta+d} for some constants α,β,c>0\alpha,\beta,c>0 and all s,t∈ℝs,t\in\mathbb{R},
then XX admits a continuous modification whose paths are Hölder continuous of any
order γ∈(0,βα)\gamma\in(0,\tfrac{\beta}{\alpha}).
or [[43](https://arxiv.org/html/2511.03474v1#bib.bib43), Lemma 44.4, Section IV.44, p.100]), that the family of shifted processes Xt+⁣⋅X\_{t+\cdot}, t≥0t\geq 0, is CC-tight i.e. (Xu)u≥0(X^{u})\_{u\geq 0} is tight on C​(ℝ+;ℝ)C(\mathbb{R}\_{+};\mathbb{R}) (hence the existence of a weak
continuous accumulation point thanks to Prokhorov’s theorem) with limiting distributions P under which the canonical process has the announced Hölder pathwise regularity. Therefore, we conclude that along a sequence uk↑∞u\_{k}\uparrow\infty, the process XukX^{u\_{k}} converges in law to some continuous process X∞X^{\infty}.

An application of Fatou’s lemma shows that any limiting process (resp. the limit distribution) has a finite moment of any order, i.e., ∀t>0,𝔼​[|Xt∞|p]≤supu≥0𝔼​[|Xu|p]<∞.\quad\forall t>0,\quad\mathbb{E}[|X^{\infty}\_{t}|^{p}]\leq\sup\_{u\geq 0}\mathbb{E}[|X\_{u}|^{p}]<\infty.

For the first moment formula, we note using equation ([3.17](https://arxiv.org/html/2511.03474v1#S3.E17 "In 3.1.1 Stationarity of the Mean ‣ 3.1 Towards stationarity of First Moments. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and Lemma [3.1](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem1 "Lemma 3.1. ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xt]⟶a​ϕ∞​𝔼​[X0]+(1−a)​μ∞λas ​t→∞.\mathbb{E}[X\_{t}]\longrightarrow a\phi\_{\infty}\mathbb{E}[X\_{0}]+(1-a)\frac{\mu\_{\infty}}{\lambda}\quad\text{as }t\to\infty. |  |

Since supt≥0𝔼​[|Xt|2]<∞\sup\_{t\geq 0}\mathbb{E}[|X\_{t}|^{2}]<\infty, we easily conclude that limt→∞𝔼​[Xt]=𝔼​[Xt∞].\quad\lim\_{t\to\infty}\mathbb{E}[X\_{t}]=\mathbb{E}[X^{\infty}\_{t}].

Step 3. (b) Asymptotic weak stationarity. 
Now let us consider the asymptotic covariance between Xt+t1X\_{t+t\_{1}} and Xt+t2X\_{t+t\_{2}}, 0<t1<t20<t\_{1}<t\_{2} when XtX\_{t} starts for X0X\_{0} with mean μ∞λ\frac{\mu\_{\infty}}{\lambda}, variance v0v\_{0} and σ¯2=𝔼​σ​(Xt)2\bar{\sigma}^{2}=\mathbb{E}\,\sigma(X\_{t})^{2}, t≥0t\geq 0 constant over time.
Using Cov​(a​U+b,c​V+d)=a​c​Cov​(U,V)\text{Cov}(aU+b,cV+d)=ac\,\text{Cov}(U,V) and equation ([3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we have:

|  |  |  |
| --- | --- | --- |
|  | Cov​(Xt+t1,Xt+t2)=Var​(X0)​((ϕ−fλ∗ϕ)​(t+t1))​((ϕ−fλ∗ϕ)​(t+t2))\displaystyle\,{\rm Cov}(X\_{t+t\_{1}},X\_{t+t\_{2}})={\rm Var}(X\_{0})\left((\phi-f\_{\lambda}\*\phi)(t+t\_{1})\right)\left((\phi-f\_{\lambda}\*\phi)(t+t\_{2})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | +1λ2​𝔼​[∫0t+t1fλ​(t+t2−s)​fλ​(t+t1−s)​ς2​(s)​σ2​(Xs)​𝑑s]\displaystyle\hskip 199.16928pt+\frac{1}{\lambda^{2}}\mathbb{E}\left[\int\_{0}^{t+t\_{1}}f\_{\lambda}(t+t\_{2}-s)f\_{\lambda}(t+t\_{1}-s)\varsigma^{2}(s)\sigma^{2}(X\_{s})ds\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =Var​(X0)​((ϕ−fλ∗ϕ)​(t+t1))​((ϕ−fλ∗ϕ)​(t+t2))+σ¯2λ2​∫0t+t1fλ​(t2−t1+u)​fλ​(u)​ς2​(t+t1−u)​𝑑u.\displaystyle={\rm Var}(X\_{0})\left((\phi-f\_{\lambda}\*\phi)(t+t\_{1})\right)\left((\phi-f\_{\lambda}\*\phi)(t+t\_{2})\right)+\frac{\bar{\sigma}^{2}}{\lambda^{2}}\int\_{0}^{t+t\_{1}}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)\varsigma^{2}(t+t\_{1}-u)du. |  |

As fλ(t2−t1+⋅)fλ∈ℒ2(Leb1)f\_{\lambda}(t\_{2}-t\_{1}+\cdot)f\_{\lambda}\!\in{\cal L}^{2}({\rm Leb}\_{1}) since fλ∈ℒ2​(Leb1)f\_{\lambda}\!\in{\cal L}^{2}({\rm Leb}\_{1}) , 1{0≤u≤t+t1}​ς2​(t+t1−u)→c​λ2​(1−a2​ϕ∞2)∫0+∞fλ2​(s)​𝑑s\mbox{\bf 1}\_{\{0\leq u\leq t+t\_{1}\}}\varsigma^{2}(t+t\_{1}-u)\to\frac{c\lambda^{2}(1-a^{2}\phi\_{\infty}^{2})}{\int\_{0}^{+\infty}f^{2}\_{\lambda}(s)ds} for every u∈ℝ+u\!\in\mathbb{R}\_{+} as t→+∞t\to+\infty (owing to Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and limt→+∞(ϕ−fλ∗ϕ)​(t)=a​ϕ∞\lim\_{t\to+\infty}(\phi-f\_{\lambda}\*\phi)(t)=a\phi\_{\infty}, v0=c​σ¯2v\_{0}=c\bar{\sigma}^{2}, we have:

Cov(Xt+t1,Xt+t2)⟶t→+∞a2ϕ∞2Var(X0)+c​σ¯2​(1−a2​ϕ∞2)∫0+∞fλ2​(s)​𝑑s∫0+∞fλ(t2−t1+u)fλ(u)du=:Cfλ(t1,t2).{\rm Cov}(X\_{t+t\_{1}},X\_{t+t\_{2}})\stackrel{{\scriptstyle t\to+\infty}}{{\longrightarrow}}a^{2}\phi\_{\infty}^{2}{\rm Var}(X\_{0})+\frac{c\bar{\sigma}^{2}(1-a^{2}\phi\_{\infty}^{2})}{\int\_{0}^{+\infty}f^{2}\_{\lambda}(s)ds}\int\_{0}^{+\infty}f\_{\lambda}(t\_{2}-t\_{1}+u)f\_{\lambda}(u)du=:C\_{f\_{\lambda}}(t\_{1},t\_{2}).

The confluence result follows from the Remark (2) in Proposition [4.4](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem4 "Proposition 4.4 (𝐿^𝑝-confluence). ‣ 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") with φ¯∞​(t)=supu≥tφ∞​(u)\bar{\varphi}\_{\infty}(t)=\sup\_{u\geq t}\varphi\_{\infty}(u).
Let XX and X′X^{\prime} be two solutions of Equation ([3.14](https://arxiv.org/html/2511.03474v1#S3.E14 "In Proposition 3.2 (Wiener-Hopf transform). ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) starting from X0X\_{0} and X0′X^{\prime}\_{0} respectively, both square integrable. Using the Remark (2) in Proposition [4.4](https://arxiv.org/html/2511.03474v1#S4.ThmTheorem4 "Proposition 4.4 (𝐿^𝑝-confluence). ‣ 4.2 𝐿^𝑝-Confluence or Contraction Properties ‣ 4 Towards Long run behaviour: asymptotics and confluence ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), we derive that for every 0≤t1<t2<⋯<tN<+∞0\leq t\_{1}<t\_{2}<\cdots<t\_{{}\_{N}}<+\infty

𝒲2​([(Xt+t1,⋯,Xt+tN)],[(Xt+t1′,⋯,Xt+tN′)])→0​ as ​t→+∞.{\cal W}\_{2}\big([(X\_{t+t\_{1}},\cdots,X\_{t+t\_{{}\_{N}}})],[(X^{\prime}\_{t+t\_{1}},\cdots,X^{\prime}\_{t+t\_{{}\_{N}}})])\to 0\mbox{ as }t\to+\infty.

As a consequence, the weak limiting distributions of [Xt+⁣⋅][X\_{t+\cdot}] and [Xt+⁣⋅′][X^{\prime}\_{t+\cdot}] are the same in the sense that, if [Xtn+⁣⋅]⟶(C)P[X\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)}}{{\longrightarrow}}P for some subsequence tn→+∞t\_{n}\to+\infty (where PP is a probability measure on C​(ℝ+,ℝ)C(\mathbb{R}\_{+},\mathbb{R}) equipped with the Borel σ\sigma-field induced by the sup-norm topology), then [Xtn+⁣⋅′]⟶(C)wP[X^{\prime}\_{t\_{n}+\cdot}]\stackrel{{\scriptstyle(C)\_{w}}}{{\longrightarrow}}P and conversely.

Step 4. (c) Stationary Gausian case. This result stems first from the fact that (Xt)t≥0(X\_{t})\_{t\geq 0} is a Gaussian process, implying that its limiting distributions in the functional weak sense are also Gaussian. Secondly, a Gaussian process is completely characterized by its mean and covariance functions.
  
In fact, when σ​(x)=σ>0∀x∈ℝ\sigma(x)=\sigma>0\quad\forall x\in\mathbb{R} and X0X\_{0} follows a Gaussian distribution, the process XX is Gaussian, which implies (at least for finite-dimensional weak convergence, i.e., weak convergence of all marginals of any order) that,(Xt+⁣⋅)⟶(C)𝒢​𝒫​(fλ)ast→+∞,(X\_{t+\cdot})\stackrel{{\scriptstyle(C)}}{{\longrightarrow}}\mathcal{GP}(f\_{\lambda})\quad\text{as}\quad t\to+\infty,
where 𝒢​𝒫​(fλ)\mathcal{GP}(f\_{\lambda}) is a Gaussian process with mean x∞x\_{\infty} and covariance function given above. □\Box

###### Lemma B.1 (Expansions).

We have the following inequalities:

1. 1.

   0≤1−e−v≤(1−e−v)ϑ≤vϑ0\leq 1-e^{-v}\leq(1-e^{-v})^{\vartheta}\leq{v}^{\vartheta}, for every v≥0v\geq 0, and ϑ∈(0,1]\vartheta\!\in(0,1].
2. 2.

   sin⁡(v)≤vϑ\sin(v)\leq{v}^{\vartheta}, for every v≥0v\geq 0, and ϑ∈(0,1]\vartheta\!\in(0,1].

Proof. The claim (1) is straightforward since ϑ∈(0,1)\vartheta\!\in(0,1), while for the second claim, we have:

* —

  if 0≤v≤10\leq v\leq 1, then sin⁡(v)≤v≤vϑ\sin(v)\leq v\leq{v}^{\vartheta}, for every ϑ∈(0,1]\vartheta\!\in(0,1].
* —

  if v≥1v\geq 1, then vϑ≥1≥sin⁡(v){v}^{\vartheta}\geq 1\geq\sin(v), for every ϑ∈(0,1]\vartheta\!\in(0,1].

Proof of Proposition [5.1](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem1 "Proposition 5.1. ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"):

Step 1.
As ∀α∈ℝ∖ℕ\forall\alpha\!\in\mathbb{R}\setminus\mathbb{N} , (−1)⌊α⌋​sin⁡(α​π)>0(-1)^{\lfloor\alpha\rfloor}\sin(\alpha\pi)>0, we have the inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u2​α+2​uα​cos⁡(π​α)+1≥1−cos2⁡(α​π)=sin2⁡(α​π)>0​(or≥(uα−1)2>0).u^{2\alpha}+2u^{\alpha}\cos(\pi\alpha)+1\geq 1-\cos^{2}(\alpha\pi)=\sin^{2}(\alpha\pi)>0\quad(\textit{or}\quad\geq(u^{\alpha}-1)^{2}>0). |  | (B.66) |

i.e., (−1)⌊α⌋​Hα​(u)(-1)^{\lfloor\alpha\rfloor}H\_{\alpha}(u) is non-negative for all uu in the integral [5.46](https://arxiv.org/html/2511.03474v1#S5.E46 "In 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"). Therefore, (−1)⌊α⌋​Fα​(t)(-1)^{\lfloor\alpha\rfloor}F\_{\alpha}(t) is the Laplace transform of a non-negative Lebesgue integrable function (−1)⌊α⌋​Hα:ℝ+→ℝ+(-1)^{\lfloor\alpha\rfloor}H\_{\alpha}:\mathbb{R}\_{+}\to\mathbb{R}\_{+}, and, by the ”Bernstein theorem”, (−1)⌊α⌋​Fα​(t)(-1)^{\lfloor\alpha\rfloor}F\_{\alpha}(t) is completely monotone (CM) in the real line,in the sense that (−1)n​(−1)⌊α⌋​Fα(n)​(t)≥0(-1)^{n}(-1)^{\lfloor\alpha\rfloor}F^{(n)}\_{\alpha}(t)\geq 0 at every order n≥0n\geq 0.
However, the CM property of (−1)⌊α⌋​Fα​(t)(-1)^{\lfloor\alpha\rfloor}F\_{\alpha}(t) can also be seen as a consequence of the result by Pollard [[45](https://arxiv.org/html/2511.03474v1#bib.bib45)] because the transformation x=tαx=t^{\alpha} is a Bernstein function for α∈(0,1)\alpha\in(0,1).

Step 2. Moreover as HαH\_{\alpha} is continuous on (0,+∞)(0,+\infty), Hα​(u)∼0uα−1​sin⁡(π​α)π and Hα​(u)∼+∞sin⁡(π​α)π​uα+1.H\_{\alpha}(u)\stackrel{{\scriptstyle 0}}{{\sim}}u^{\alpha-1}\frac{\sin(\pi\alpha)}{\pi}\quad\mbox{ and }\quad H\_{\alpha}(u)\stackrel{{\scriptstyle+\infty}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi u^{\alpha+1}}.
  
It is clear that Hα∈ℒℝ+1​(Leb1)H\_{\alpha}\!\in{\cal L}\_{\mathbb{R}\_{+}}^{1}({\rm Leb}\_{1}) and that both functions u↦u​Hα​(u)u\mapsto uH\_{\alpha}(u) and u↦uα+1​Hα​(u)u\mapsto u^{\alpha+1}H\_{\alpha}(u) are bounded on ℝ+\mathbb{R}\_{+}.
Thus, for every t>0t>0, ∫0+∞e−t​u​u​Hα​(u)​𝑑u<+∞\int\_{0}^{+\infty}e^{-tu}uH\_{\alpha}(u)du<+\infty so that owing to a Lebesgue-type condition for differentiation under the integral sign, FαF\_{\alpha} is differentiable on (0,+∞)(0,+\infty) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fα′​(t)=−∫0+∞e−t​u​u​Hα​(u)​𝑑u,t>0.F^{\prime}\_{\alpha}(t)=-\int\_{0}^{+\infty}e^{-tu}uH\_{\alpha}(u)du,\quad t>0. |  | (B.67) |

The same rule applied kk times shows that FαF\_{\alpha} is 𝒞k\mathcal{C}^{k} for k∈ℕk\in\mathbb{N}, hence is infinitely differentiable and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fα(k)​(t)=∫0+∞e−t​u​Hα(k)​(u)​𝑑u​with​Hα(k)​(u):=(−1)k​uk​Hα​(u)=(−1)k​sin⁡(α​π)π​uα−1+ku2​α+2​uα​cos⁡(α​π)+1.F^{(k)}\_{\alpha}(t)=\int\_{0}^{+\infty}e^{-tu}H^{(k)}\_{\alpha}(u)\,du\;\text{with}\;H^{(k)}\_{\alpha}(u):=(-1)^{k}u^{k}H\_{\alpha}(u)=(-1)^{k}\frac{\sin(\alpha\pi)}{\pi}\frac{u^{\alpha-1+k}}{u^{2\alpha}+2u^{\alpha}\cos(\alpha\pi)+1}. |  | (B.68) |

Gα​(t)G\_{\alpha}(t) is infinitely differentiable(𝒞k\mathcal{C}^{k} for k∈ℕk\in\mathbb{N}) as product of such functions and by recurrence, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀k∈ℕ,Gα(k)​(t)=2α​∑n=0⌊α−12⌋exp⁡[t​cos⁡((2​n+1)​πα)]​cos⁡[t​sin⁡((2​n+1)​πα)−k​(2​n+1)​πα].\forall k\in\mathbb{N},\quad G^{(k)}\_{\alpha}(t)=\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\cos\left[t\sin\left(\frac{(2n+1)\pi}{\alpha}\right)-\frac{k(2n+1)\pi}{\alpha}\right]. |  | (B.69) |

Claim (b)(b) follows from the fact that Rα,λ=eα(λ1/α⋅)=Rα,1(λ1/α⋅)R\_{\alpha,\lambda}=e\_{\alpha}(\lambda^{1/\alpha}\cdot)=R\_{\alpha,1}(\lambda^{1/\alpha}\cdot), hence infinitely differentiable on (0,+∞)(0,+\infty) from [B.68](https://arxiv.org/html/2511.03474v1#A2.E68 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and [B.69](https://arxiv.org/html/2511.03474v1#A2.E69 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
The representation of fα,λf\_{\alpha,\lambda} follows from [B.67](https://arxiv.org/html/2511.03474v1#A2.E67 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and [B.69](https://arxiv.org/html/2511.03474v1#A2.E69 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

It follows from ([5.47](https://arxiv.org/html/2511.03474v1#S5.E47 "In 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([B.66](https://arxiv.org/html/2511.03474v1#A2.E66 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that Hα​(u)≤uα−1​sin⁡(π​α)π​sin2⁡(π​α)=uα−1π​sin⁡(π​α).H\_{\alpha}(u)\leq\frac{u^{\alpha-1}\sin(\pi\alpha)}{\pi\sin^{2}(\pi\alpha)}=\frac{u^{\alpha-1}}{\pi\sin(\pi\alpha)}.
Hence, for every t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rα,1​(t)=eα​(t)\displaystyle R\_{\alpha,1}(t)=e\_{\alpha}(t) | =Fα​(t)+Gα​(t)<1π​sin⁡(π​α)​∫0+∞e−t​u​uα−1​𝑑u+2α​∑n=0⌊α−12⌋exp⁡[t​cos⁡((2​n+1)​πα)]\displaystyle=F\_{\alpha}(t)+G\_{\alpha}(t)<\frac{1}{\pi\sin(\pi\alpha)}\int\_{0}^{+\infty}e^{-tu}u^{\alpha-1}du+\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Γ​(α)π​sin⁡(π​α)​t−α+2α​∑n=0⌊α−12⌋exp⁡[t​cos⁡((2​n+1)​πα)]≤Γ​(α)π​sin⁡(π​α)​t−α+⌊α+1⌋α​et​cos⁡(πα)\displaystyle\leq\frac{\Gamma(\alpha)}{\pi\sin(\pi\alpha)}t^{-\alpha}+\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\leq\frac{\Gamma(\alpha)}{\pi\sin(\pi\alpha)}t^{-\alpha}+\frac{\lfloor\alpha+1\rfloor}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)} |  |

where the last inequality comes from the fact that cos⁡(x)\cos(x) is non-increasing on [0,π][0,\pi]
so that Rα,1∈ℒγ​(Leb1)R\_{\alpha,1}\!\in{\cal L}^{\gamma}({\rm Leb}\_{1}) for every γ>1α\gamma>\frac{1}{\alpha} where α\alpha is such that cos⁡(πα)<0\cos\left(\frac{\pi}{\alpha}\right)<0 i.e. α∈(0,2]\alpha\in(0,2] . This extends to Rλ,αR\_{\lambda,\alpha} by scaling.
For the L2​βL^{2\beta}-integrability of fα,λf\_{\alpha,\lambda}, once noted that fα,λ=λ1/αfα,1(λ1/α⋅)f\_{\alpha,\lambda}=\lambda^{1/\alpha}f\_{\alpha,1}(\lambda^{1/\alpha}\cdot) so that ∫0+∞fα,λ2​β​(t)​𝑑t=λ2​β−1α​∫0+∞fα,12​β​(t)​𝑑t\int\_{0}^{+\infty}f\_{\alpha,\lambda}^{2\beta}(t)dt=\lambda^{\frac{2\beta-1}{\alpha}}\int\_{0}^{+\infty}f\_{\alpha,1}^{2\beta}(t)dt, it is clear that it is enough to prove that fα,1f\_{\alpha,1} is ℒ2​β{\cal L}^{2\beta}-integrable.

By the same argument as above, it follows from ([B.67](https://arxiv.org/html/2511.03474v1#A2.E67 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([B.69](https://arxiv.org/html/2511.03474v1#A2.E69 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that for every t>0t>0

|  |  |  |
| --- | --- | --- |
|  | fα,1​(t)<1π​sin⁡(π​α)​∫0+∞e−t​u​uα​𝑑u−2α​∑n=0⌊α−12⌋exp⁡[t​cos⁡((2​n+1)​πα)]≤Γ​(α+1)tα+1​π​sin⁡(π​α)−⌊α+1⌋α​et​cos⁡(πα).f\_{\alpha,1}(t)<\frac{1}{\pi\sin(\pi\alpha)}\int\_{0}^{+\infty}e^{-tu}u^{\alpha}du-\frac{2}{\alpha}\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\exp\left[t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\leq\frac{\Gamma(\alpha+1)}{t^{\alpha+1}\pi\sin(\pi\alpha)}-\frac{\lfloor\alpha+1\rfloor}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}. |  |

Thus fα,1∈ℒ2​β​([1,+∞),Leb1)∀β>0f\_{\alpha,1}\!\in{\cal L}^{2\beta}([1,+\infty),{\rm Leb}\_{1})\quad\forall\beta>0 provided that cos⁡(πα)<0\cos\left(\frac{\pi}{\alpha}\right)<0 i.e. α∈(0,2)\alpha\in(0,2).
On the other hand fα,λ​(t)=−Rα,λ′​(t)=α​λ​tα−1​Eα′​(−λ​tα)=λ​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1))f\_{\alpha,\lambda}(t)=-R^{\prime}\_{\alpha,\lambda}(t)=\alpha\lambda t^{\alpha-1}E^{\prime}\_{\alpha}(-\lambda t^{\alpha})=\lambda t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\lambda^{k}\frac{t^{\alpha k}}{\Gamma(\alpha(k+1))}
so that fα,1​(t)∼0tα−1Γ​(α).f\_{\alpha,1}(t)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{t^{\alpha-1}}{\Gamma(\alpha)}.
As t↦1t1−α∈ℒ2​β​((0,1],Leb1)t\mapsto\frac{1}{t^{1-\alpha}}\!\in{\cal L}^{2\beta}((0,1],{\rm Leb}\_{1}) for any β∈(12​(1−α),+∞)\beta\!\in\big(\frac{1}{2(1-\alpha)},+\infty\big) , we conclude that fα,1∈ℒ2​β​(Leb1)∀β>0f\_{\alpha,1}\!\in{\cal L}^{2\beta}({\rm Leb}\_{1})\quad\forall\beta>0 provided that cos⁡(πα)<0\cos\left(\frac{\pi}{\alpha}\right)<0 i.e. α∈(0,2)\alpha\in(0,2).

Step 3.
As for the ℒ2​(ℝ+){\cal L}^{2}(\mathbb{R}\_{+})-ϑ\vartheta-Hölder continuity of fα,λf\_{\alpha,\lambda}, one may again assume w.l.g. that λ=1\lambda=1. Let δ>0\delta>0. One has

|  |  |  |
| --- | --- | --- |
|  | fα,1​(t+δ)−fα,1​(t)=(Fα′​(t)−Fα′​(t+δ))+(Gα′​(t)−Gα′​(t+δ))=(Fα′​(t)−Fα′​(t+δ))+∑n=0⌊α−12⌋(Gα′⁣n​(t)−Gα′⁣n​(t+δ))f\_{\alpha,1}(t+\delta)-f\_{\alpha,1}(t)=\left(F^{\prime}\_{\alpha}(t)-F^{\prime}\_{\alpha}(t+\delta)\right)+\left(G^{\prime}\_{\alpha}(t)-G^{\prime}\_{\alpha}(t+\delta)\right)=\left(F^{\prime}\_{\alpha}(t)-F^{\prime}\_{\alpha}(t+\delta)\right)+\sum\_{n=0}^{\lfloor\frac{\alpha-1}{2}\rfloor}\left(G^{\prime n}\_{\alpha}(t)-G^{\prime n}\_{\alpha}(t+\delta)\right) |  |

However, bearing in mind that 0≤πα≤(2​n+1)​πα≤π0\leq\frac{\pi}{\alpha}\leq\frac{(2n+1)\pi}{\alpha}\leq\pi for α∈ℝ+∖ℕ\alpha\in\mathbb{R}^{+}\setminus\mathbb{N} and 0≤n≤⌊α−12⌋0\leq n\leq\lfloor\frac{\alpha-1}{2}\rfloor , we have:

|  |  |  |
| --- | --- | --- |
|  | Gα′⁣n​(t)−Gα′⁣n​(t+δ)=\displaystyle G^{\prime n}\_{\alpha}(t)-G^{\prime n}\_{\alpha}(t+\delta)= |  |
|  |  |  |
| --- | --- | --- |
|  | 2α​et​cos⁡((2​n+1)​πα)​(cos⁡[t​sin⁡((2​n+1)​πα)−(2​n+1)​πα]−eδ​cos⁡((2​n+1)​πα)​cos⁡[(t+δ)​sin⁡((2​n+1)​πα)−(2​n+1)​πα])\displaystyle\frac{2}{\alpha}e^{t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)}\left(\cos\left[t\sin\left(\frac{(2n+1)\pi}{\alpha}\right)-\frac{(2n+1)\pi}{\alpha}\right]-e^{\delta\cos\left(\frac{(2n+1)\pi}{\alpha}\right)}\cos\left[(t+\delta)\sin\left(\frac{(2n+1)\pi}{\alpha}\right)-\frac{(2n+1)\pi}{\alpha}\right]\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =2α​et​cos⁡((2​n+1)​πα)​(cos⁡[t​sin⁡((2​n+1)​πα)−(2​n+1)​πα]−cos⁡[(t+δ)​sin⁡((2​n+1)​πα)−(2​n+1)​πα])\displaystyle=\frac{2}{\alpha}e^{t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)}\Bigg(\cos\left[t\sin\left(\frac{(2n+1)\pi}{\alpha}\right)-\frac{(2n+1)\pi}{\alpha}\right]-\cos\left[(t+\delta)\sin\left(\frac{(2n+1)\pi}{\alpha}\right)-\frac{(2n+1)\pi}{\alpha}\right]\Bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | +(1−eδ​cos⁡((2​n+1)​πα))​cos⁡[(t+δ)​sin⁡((2​n+1)​πα)−(2​n+1)​πα]\displaystyle\qquad\hskip 170.71652pt+\left(1-e^{\delta\cos\left(\frac{(2n+1)\pi}{\alpha}\right)}\right)\cos\left[(t+\delta)\sin\left(\frac{(2n+1)\pi}{\alpha}\right)-\frac{(2n+1)\pi}{\alpha}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2α​et​cos⁡((2​n+1)​πα)​(2​sin⁡[δ2​sin⁡((2​n+1)​πα)]​sin⁡[−(t+δ2)​sin⁡((2​n+1)​πα)+(2​n+1)​πα]+(1−eδ​cos⁡((2​n+1)​πα)))\displaystyle\leq\frac{2}{\alpha}e^{t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)}\left(2\sin\left[\frac{\delta}{2}\sin\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\sin\left[-(t+\frac{\delta}{2})\sin\left(\frac{(2n+1)\pi}{\alpha}\right)+\frac{(2n+1)\pi}{\alpha}\right]+(1-e^{\delta\cos\left(\frac{(2n+1)\pi}{\alpha}\right)})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2α​et​cos⁡((2​n+1)​πα)​(2​sin⁡[δ2​sin⁡((2​n+1)​πα)]+(1−eδ​cos⁡((2​n+1)​πα)))\displaystyle\leq\frac{2}{\alpha}e^{t\cos\left(\frac{(2n+1)\pi}{\alpha}\right)}\left(2\sin\left[\frac{\delta}{2}\sin\left(\frac{(2n+1)\pi}{\alpha}\right)\right]+(1-e^{\delta\cos\left(\frac{(2n+1)\pi}{\alpha}\right)})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2α​et​cos⁡(πα)​(2​(δ2​π)θ+(1−e−δ))≤2α​et​cos⁡(πα)​(21−θ​πθ​δθ+δθ)=2α​et​cos⁡(πα)​(21−θ​πθ+1)​δθ.\displaystyle\leq\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2\left(\frac{\delta}{2}\pi\right)^{\theta}+(1-e^{-\delta})\right)\leq\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2^{1-\theta}\pi^{\theta}\delta^{\theta}+\delta^{\theta}\right)=\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2^{1-\theta}\pi^{\theta}+1\right)\delta^{\theta}. |  |

The penultimate inequality follows from the fact that 0≤πα≤(2​n+1)​πα≤π0\leq\frac{\pi}{\alpha}\leq\frac{(2n+1)\pi}{\alpha}\leq\pi, which leads to two key observations. On one hand, we have 1−eδ​cos⁡((2​n+1)​πα)≤1−e−δ,1-e^{\delta\cos\left(\frac{(2n+1)\pi}{\alpha}\right)}\leq 1-e^{-\delta},
and on the other hand, by applying Lemma [B.1](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem1 "Lemma B.1 (Expansions). ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (2), we obtain the following inequality:

sin⁡[δ2​sin⁡((2​n+1)​πα)]≤(δ2​sin⁡((2​n+1)​πα))θ≤(δ2​((2​n+1)​πα))θ≤(δ2​π)θ.\sin\left[\frac{\delta}{2}\sin\left(\frac{(2n+1)\pi}{\alpha}\right)\right]\leq\left(\frac{\delta}{2}\sin\left(\frac{(2n+1)\pi}{\alpha}\right)\right)^{\theta}\leq\left(\frac{\delta}{2}\left(\frac{(2n+1)\pi}{\alpha}\right)\right)^{\theta}\leq\left(\frac{\delta}{2}\pi\right)^{\theta}.

Where the final inequality follows from Lemma [B.1](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem1 "Lemma B.1 (Expansions). ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (1).
Consequently, Hölder regularity with exponent ϑ\vartheta for the function fα,λf\_{\alpha,\lambda} can be achieved provided that cos⁡(πα)<0\cos\left(\frac{\pi}{\alpha}\right)<0, i.e., α∈(0,2)\alpha\in(0,2).

Now, about the α\alpha-fractional kernels with 1<α<21<\alpha<2, it follows from Proposition[5.1](https://arxiv.org/html/2511.03474v1#S5.Thmprop1 "Proposition 5.1. ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), (see also [[23](https://arxiv.org/html/2511.03474v1#bib.bib23)]) that:

eα​(t)=Fα​(t)+Gα​(t)=∫0+∞e−t​u​Hα​(u)​𝑑u+2α​et​cos⁡(πα)​cos⁡(t​sin⁡(πα)),1<α<2,t≥0.e\_{\alpha}(t)=F\_{\alpha}(t)+G\_{\alpha}(t)=\int\_{0}^{+\infty}e^{-tu}H\_{\alpha}(u)\,du+\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\cos\left(t\sin\left(\frac{\pi}{\alpha}\right)\right),\quad 1<\alpha<2,\quad t\geq 0.

Note that, in this case (1<α<21<\alpha<2), the function Hα​(u)H\_{\alpha}(u) is negative for all u (and thus -F is completely monotone and hence infinitely differentiable on ℝ++\mathbb{R}\_{+}^{+})
since 1<α<21<\alpha<2 implies sin⁡(α​π)<0\sin(\alpha\pi)<0 and we have the following inequality: u2​α+2​uα​cos⁡(π​α)+1≥1−cos2⁡(α​π)=sin2⁡(α​π)>0​(or≥(uα−1)2>0).u^{2\alpha}+2u^{\alpha}\cos(\pi\alpha)+1\geq 1-\cos^{2}(\alpha\pi)=\sin^{2}(\alpha\pi)>0\;(\textit{or}\;\geq(u^{\alpha}-1)^{2}>0). □\square

Proof of Proposition [5.2](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem2 "Proposition 5.2 (𝛼-fractional kernels 1<𝛼<2). ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
(a)(a) follows from the first claim of Proposition [5.1](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem1 "Proposition 5.1. ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") since Rα,λ=eα(λ1/α⋅)=Rα,1(λ1/α⋅)R\_{\alpha,\lambda}=e\_{\alpha}(\lambda^{1/\alpha}\cdot)=R\_{\alpha,1}(\lambda^{1/\alpha}\cdot), hence infinitely differentiable on (0,+∞)(0,+\infty) from [B.68](https://arxiv.org/html/2511.03474v1#A2.E68 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and [B.69](https://arxiv.org/html/2511.03474v1#A2.E69 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"). All will extend to Rα,λR\_{\alpha,\lambda} by scaling.
It follows from ([5.47](https://arxiv.org/html/2511.03474v1#S5.E47 "In 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([B.66](https://arxiv.org/html/2511.03474v1#A2.E66 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that Hα​(u)≤uα−1​sin⁡(π​α)π​sin2⁡(π​α)=uα−1π​sin⁡(π​α).H\_{\alpha}(u)\leq\frac{u^{\alpha-1}\sin(\pi\alpha)}{\pi\sin^{2}(\pi\alpha)}=\frac{u^{\alpha-1}}{\pi\sin(\pi\alpha)}.
Hence, for every t≥0t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | Rα,1​(t)=eα​(t)=Fα​(t)+Gα​(t)≤1π​sin⁡(π​α)​∫0+∞e−t​u​uα−1​𝑑u+2α​et​cos⁡(πα)=Γ​(α)π​sin⁡(π​α)​t−α+2α​et​cos⁡(πα).R\_{\alpha,1}(t)=e\_{\alpha}(t)=F\_{\alpha}(t)+G\_{\alpha}(t)\leq\frac{1}{\pi\sin(\pi\alpha)}\int\_{0}^{+\infty}e^{-tu}u^{\alpha-1}du+\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}=\frac{\Gamma(\alpha)}{\pi\sin(\pi\alpha)}t^{-\alpha}+\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}. |  |

so that Rα,1∈ℒγ​(Leb1)R\_{\alpha,1}\!\in{\cal L}^{\gamma}({\rm Leb}\_{1}) for every γ>1α\gamma>\frac{1}{\alpha} as cos⁡(πα)<0,∀α∈(1,2)\cos\left(\frac{\pi}{\alpha}\right)<0,\,\forall\,\alpha\in(1,2) and in particular Rα,1​(t)≤1∀t≥0R\_{\alpha,1}(t)\leq 1\quad\forall t\geq 0 since sin⁡(π​α)≤0\sin(\pi\alpha)\leq 0 . The representation of fα,λf\_{\alpha,\lambda} in (b)(b) follows from ([B.67](https://arxiv.org/html/2511.03474v1#A2.E67 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([5.49](https://arxiv.org/html/2511.03474v1#S5.E49 "In Proposition 5.2 (𝛼-fractional kernels 1<𝛼<2). ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")).

(c)(c) Let us prove the L2​βL^{2\beta}-integrability of fα,λf\_{\alpha,\lambda}. Once noted that fα,λ=λ1/αfα,1(λ1/α⋅)f\_{\alpha,\lambda}=\lambda^{1/\alpha}f\_{\alpha,1}(\lambda^{1/\alpha}\cdot) so that ∫0+∞fα,λ2​β​(t)​𝑑t=λ2​β−1α​∫0+∞fα,12​β​(t)​𝑑t\int\_{0}^{+\infty}f\_{\alpha,\lambda}^{2\beta}(t)dt=\lambda^{\frac{2\beta-1}{\alpha}}\int\_{0}^{+\infty}f\_{\alpha,1}^{2\beta}(t)dt, it is clear that it is enough to prove that fα,1f\_{\alpha,1} is ℒ2​β{\cal L}^{2\beta}-integrable.

It follows from ([B.67](https://arxiv.org/html/2511.03474v1#A2.E67 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and ([5.49](https://arxiv.org/html/2511.03474v1#S5.E49 "In Proposition 5.2 (𝛼-fractional kernels 1<𝛼<2). ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that for every t>0t>0,

|  |  |  |
| --- | --- | --- |
|  | fα,1​(t)=−eα′​(t)=−Fα′​(t)−Gα′​(t)≤1π​sin⁡(π​α)​∫0+∞e−t​u​uα​𝑑u+2α​et​cos⁡(πα)=Γ​(α+1)tα+1​π​sin⁡(π​α)+2α​et​cos⁡(πα).f\_{\alpha,1}(t)=-e^{\prime}\_{\alpha}(t)=-F^{\prime}\_{\alpha}(t)-G^{\prime}\_{\alpha}(t)\leq\frac{1}{\pi\sin(\pi\alpha)}\int\_{0}^{+\infty}e^{-tu}u^{\alpha}du+\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}=\frac{\Gamma(\alpha+1)}{t^{\alpha+1}\pi\sin(\pi\alpha)}+\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}. |  |

Thus fα,1∈ℒ2​β​([1,+∞),Leb1)∀β>0.f\_{\alpha,1}\!\in{\cal L}^{2\beta}([1,+\infty),{\rm Leb}\_{1})\quad\forall\beta>0.
On the other hand fα,λ​(t)=λ​tα−1​∑k≥0(−1)k​λk​tα​kΓ​(α​(k+1))f\_{\alpha,\lambda}(t)=\lambda t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}\lambda^{k}\frac{t^{\alpha k}}{\Gamma(\alpha(k+1))}
so that fα,1​(t)∼0tα−1Γ​(α).f\_{\alpha,1}(t)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{t^{\alpha-1}}{\Gamma(\alpha)}.
As t↦1t1−α∈ℒ2​β​((0,1],Leb1)t\mapsto\frac{1}{t^{1-\alpha}}\!\in{\cal L}^{2\beta}((0,1],{\rm Leb}\_{1}) for any β∈(12​(1−α),+∞)∩ℝ+∗=ℝ+∗\beta\!\in\big(\frac{1}{2(1-\alpha)},+\infty\big)\cap\mathbb{R}\_{+}^{\*}=\mathbb{R}\_{+}^{\*}, we conclude that fα,1∈ℒ2​β​(Leb1)∀β>0f\_{\alpha,1}\!\in{\cal L}^{2\beta}({\rm Leb}\_{1})\quad\forall\beta>0 and in particular ∀β>1\forall\beta>1. Another consequence is that, for every t≥1t\geq 1,
Rα,1​(t)=eα​(t)=∫t+∞fα,1​(s)​𝑑s≤Cα′​t−α+Cα′′​et​cos⁡(πα),R\_{\alpha,1}(t)=e\_{\alpha}(t)=\int\_{t}^{+\infty}f\_{\alpha,1}(s)\,ds\leq C\_{\alpha}^{\prime}\,t^{-\alpha}+C\_{\alpha}^{\prime\prime}\,e^{t\cos\left(\frac{\pi}{\alpha}\right)},
so that Rα,1∈L2​(Leb1)R\_{\alpha,1}\in L^{2}(\text{Leb}\_{1}).

As for the ℒ2​(ℝ+){\cal L}^{2}(\mathbb{R}\_{+})-ϑ\vartheta-Hölder continuity of fα,λf\_{\alpha,\lambda}, one may again assume w.l.g. that λ=1\lambda=1. Let δ>0\delta>0. One has fα,1​(t+δ)−fα,1​(t)=(Fα′​(t)−Fα′​(t+δ))+(Gα′​(t)−Gα′​(t+δ))f\_{\alpha,1}(t+\delta)-f\_{\alpha,1}(t)=\left(F^{\prime}\_{\alpha}(t)-F^{\prime}\_{\alpha}(t+\delta)\right)+\left(G^{\prime}\_{\alpha}(t)-G^{\prime}\_{\alpha}(t+\delta)\right) and following the same reasoning as above while bearing in mind that cos⁡(πα)≤0\cos\left(\frac{\pi}{\alpha}\right)\leq 0, sin⁡(πα)≥0\sin\left(\frac{\pi}{\alpha}\right)\geq 0 for α∈(1,2)\alpha\in(1,2), we have:

|  |  |  |
| --- | --- | --- |
|  | Gα′​(t)−Gα′​(t+δ)=2α​et​cos⁡(πα)​(cos⁡[t​sin⁡(πα)−πα]−eδ​cos⁡(πα)​cos⁡[(t+δ)​sin⁡(πα)−πα])\displaystyle G^{\prime}\_{\alpha}(t)-G^{\prime}\_{\alpha}(t+\delta)=\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(\cos\left[t\sin\left(\frac{\pi}{\alpha}\right)-\frac{\pi}{\alpha}\right]-e^{\delta\cos\left(\frac{\pi}{\alpha}\right)}\cos\left[(t+\delta)\sin\left(\frac{\pi}{\alpha}\right)-\frac{\pi}{\alpha}\right]\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =2α​et​cos⁡(πα)​((cos⁡[t​sin⁡(πα)−πα]−cos⁡[(t+δ)​sin⁡(πα)−πα])+(1−eδ​cos⁡(πα))​cos⁡[(t+δ)​sin⁡(πα)−πα])\displaystyle=\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left((\cos\left[t\sin\left(\frac{\pi}{\alpha}\right)-\frac{\pi}{\alpha}\right]-\cos\left[(t+\delta)\sin\left(\frac{\pi}{\alpha}\right)-\frac{\pi}{\alpha}\right])+(1-e^{\delta\cos\left(\frac{\pi}{\alpha}\right)})\cos\left[(t+\delta)\sin\left(\frac{\pi}{\alpha}\right)-\frac{\pi}{\alpha}\right]\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2α​et​cos⁡(πα)​(2​sin⁡[δ2​sin⁡(πα)]​sin⁡[−(t+δ2)​sin⁡(πα)+πα]+(1−eδ​cos⁡(πα)))\displaystyle\leq\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2\sin\left[\frac{\delta}{2}\sin\left(\frac{\pi}{\alpha}\right)\right]\sin\left[-(t+\frac{\delta}{2})\sin\left(\frac{\pi}{\alpha}\right)+\frac{\pi}{\alpha}\right]+(1-e^{\delta\cos\left(\frac{\pi}{\alpha}\right)})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2α​et​cos⁡(πα)​(2​sin⁡[δ2​sin⁡(πα)]+(1−eδ​cos⁡(πα)))≤2α​et​cos⁡(πα)​(2​(δ2​πα)θ+(1−e−δ))\displaystyle\leq\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2\sin\left[\frac{\delta}{2}\sin\left(\frac{\pi}{\alpha}\right)\right]+(1-e^{\delta\cos\left(\frac{\pi}{\alpha}\right)})\right)\leq\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2\left(\frac{\delta}{2}\frac{\pi}{\alpha}\right)^{\theta}+(1-e^{-\delta})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2α​et​cos⁡(πα)​(21−θ​(πα)θ​δθ+δθ)=2α​et​cos⁡(πα)​(21−θ​(πα)θ+1)​δθ.\displaystyle\leq\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}\delta^{\theta}+\delta^{\theta}\right)=\frac{2}{\alpha}e^{t\cos\left(\frac{\pi}{\alpha}\right)}\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}+1\right)\delta^{\theta}. |  |

Where the penultimate inequality follows from the fact that π2≤πα≤π\frac{\pi}{2}\leq\frac{\pi}{\alpha}\leq\pi, so that 1−eδ​cos⁡(πα)≤1−e−δ,1-e^{\delta\cos\left(\frac{\pi}{\alpha}\right)}\leq 1-e^{-\delta},
and sin⁡[δ2​sin⁡(πα)]≤(δ2​sin⁡(πα))θ≤(δ2​(πα))θ\sin\left[\frac{\delta}{2}\sin\left(\frac{\pi}{\alpha}\right)\right]\leq\left(\frac{\delta}{2}\sin\left(\frac{\pi}{\alpha}\right)\right)^{\theta}\leq\left(\frac{\delta}{2}\left(\frac{\pi}{\alpha}\right)\right)^{\theta} owing to Lemma [B.1](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem1 "Lemma B.1 (Expansions). ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (2).
The final inequality follows from Lemma [B.1](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem1 "Lemma B.1 (Expansions). ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (1).
Moreover, for the term Fα′​(t)−Fα′​(t+δ):=∫0+∞e−t​u​(1−e−δ​u)​u​Hα​(u)​𝑑uF^{\prime}\_{\alpha}(t)-F^{\prime}\_{\alpha}(t+\delta):=\int\_{0}^{+\infty}e^{-tu}(1-e^{-\delta u})uH\_{\alpha}(u)du, we may write

Fα′​(t)−Fα′​(t+δ)≤∫0+∞e−t​u​(1−e−δ​u)ϑ​u​Hα​(u)​𝑑u≤∫0+∞e−t​u​δϑ​u1+ϑ​Hα​(u)​𝑑u.F^{\prime}\_{\alpha}(t)-F^{\prime}\_{\alpha}(t+\delta)\leq\int\_{0}^{+\infty}e^{-tu}(1-e^{-\delta u})^{\vartheta}uH\_{\alpha}(u)du\leq\int\_{0}^{+\infty}e^{-tu}\delta^{\vartheta}u^{1+\vartheta}H\_{\alpha}(u)du.

1. Owing to Fubini-Tonelli’s theorem in the first line to interwind the order of integration, we have:
∫0+∞(Fα′​(t+δ)−Fα′​(t))​𝑑t≤∫(0,+∞)u1+ϑ​Hα​(u)​∫0+∞e−t​u​𝑑t​𝑑u​δϑ=[∫(0,+∞)uϑ​Hα​(u)​𝑑u]​δϑ\int\_{0}^{+\infty}\big(F^{\prime}\_{\alpha}(t+\delta)-F^{\prime}\_{\alpha}(t)\big)dt\leq\int\_{(0,+\infty)}\!\!\!u^{1+\vartheta}H\_{\alpha}(u)\int\_{0}^{+\infty}\!\!e^{-tu}dt\,du\,\delta^{\vartheta}=\left[\int\_{(0,+\infty)}\!\!\!u^{\vartheta}H\_{\alpha}(u)\,du\,\right]\delta^{\vartheta} and

|  |  |  |
| --- | --- | --- |
|  | ∫0+∞(Gα′​(t)−Gα′​(t+δ))​𝑑t≤2α​(21−θ​(πα)θ+1)​δθ​∫0+∞et​cos⁡(πα)​𝑑t=[−2α​cos⁡(πα)​(21−θ​(πα)θ+1)]​δϑ.\int\_{0}^{+\infty}\big(G^{\prime}\_{\alpha}(t)-G^{\prime}\_{\alpha}(t+\delta)\big)dt\leq\frac{2}{\alpha}\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}+1\right)\delta^{\theta}\int\_{0}^{+\infty}\!\!e^{t\cos\left(\frac{\pi}{\alpha}\right)}dt\,=\left[\frac{-2}{\alpha\cos\left(\frac{\pi}{\alpha}\right)}\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}+1\right)\right]\delta^{\vartheta}. |  |

It follows that, ∫0+∞(fα,1​(t+δ)−fα,1​(t))​𝑑t≤[∫ℝ+uϑ​Hα​(u)​𝑑u+2α​(21−θ​(πα)θ+1)]​δϑ.\int\_{0}^{+\infty}\big(f\_{\alpha,1}(t+\delta)-f\_{\alpha,1}(t)\big)dt\leq\left[\int\_{\mathbb{R}\_{+}}\!\!\!u^{\vartheta}H\_{\alpha}(u)\,du\,+\frac{2}{\alpha}\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}+1\right)\right]\delta^{\vartheta}.

Now, we derive form ([5.47](https://arxiv.org/html/2511.03474v1#S5.E47 "In 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that: Hα​(u)∼0sin⁡(π​α)π​uα−1 and Hα​(u)∼+∞sin⁡(π​α)π​u−(α+1).H\_{\alpha}(u)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{\alpha-1}\quad\mbox{ and }\quad H\_{\alpha}(u)\stackrel{{\scriptstyle+\infty}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{-(\alpha+1)}.
Consequently

|  |  |  |
| --- | --- | --- |
|  | uϑ​Hα​(u)∼0sin⁡(π​α)π​uα−1+ϑ and uϑ​Hα​(u)∼+∞sin⁡(π​α)π​u−(1+α−ϑ),u^{\vartheta}H\_{\alpha}(u)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{\alpha-1+\vartheta}\quad\mbox{ and }\quad u^{\vartheta}H\_{\alpha}(u)\stackrel{{\scriptstyle+\infty}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{-(1+\alpha-\vartheta)}, |  |

which implies that ∫(0,+∞)uϑ​Hα​(u)​𝑑u<+∞ if and only if 2−α<ϑ<α.\int\_{(0,+\infty)}\!\!\!u^{\vartheta}H\_{\alpha}(u)\,du<+\infty\quad\mbox{ if and only if }\quad 2-\alpha<\vartheta<\alpha.

2. Secondly, as: (fα,1​(t+δ)−fα,1​(t))2≤2​((Fα′​(t)−Fα′​(t+δ)))2+2​((Gα′​(t)−Gα′​(t+δ)))2\left(f\_{\alpha,1}(t+\delta)-f\_{\alpha,1}(t)\right)^{2}\leq 2\left(\left(F^{\prime}\_{\alpha}(t)-F^{\prime}\_{\alpha}(t+\delta)\right)\right)^{2}+2\left(\left(G^{\prime}\_{\alpha}(t)-G^{\prime}\_{\alpha}(t+\delta)\right)\right)^{2}
with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0+∞(Fα′(t+δ)\displaystyle\int\_{0}^{+\infty}\big(F^{\prime}\_{\alpha}(t+\delta)\, | −Fα′(t))2dt≤∫0+∞∫0+∞e−t​uδϑu1+ϑHα(u)du∫0+∞e−t​vδϑv1+ϑHα(v)dv\displaystyle-F^{\prime}\_{\alpha}(t)\big)^{2}dt\leq\int\_{0}^{+\infty}\int\_{0}^{+\infty}e^{-tu}\delta^{\vartheta}u^{1+\vartheta}H\_{\alpha}(u)du\int\_{0}^{+\infty}e^{-tv}\delta^{\vartheta}v^{1+\vartheta}H\_{\alpha}(v)dv |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫(0,+∞)2(u​v)1+ϑ​Hα​(u)​Hα​(v)​∫0+∞e−t​(u+v)​𝑑t​𝑑u​𝑑v​δ2​ϑ=∫(0,+∞)2(u​v)1+ϑu+v​Hα​(u)​Hα​(v)​𝑑u​𝑑v​δ2​ϑ\displaystyle\leq\int\_{(0,+\infty)^{2}}\!\!\!(uv)^{1+\vartheta}H\_{\alpha}(u)H\_{\alpha}(v)\int\_{0}^{+\infty}\!\!e^{-t(u+v)}dt\,du\,dv\,\delta^{2\vartheta}=\int\_{(0,+\infty)^{2}}\!\!\!\frac{(uv)^{1+\vartheta}}{u+v}H\_{\alpha}(u)H\_{\alpha}(v)\,du\,dv\,\delta^{2\vartheta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​∫(0,+∞)2(u​v)12+ϑ​Hα​(u)​Hα​(v)​𝑑u​𝑑v​δ2​ϑ=12​[∫(0,+∞)u12+ϑ​Hα​(u)​𝑑u]​δ2​ϑ.\displaystyle\leq\tfrac{1}{2}\int\_{(0,+\infty)^{2}}\!\!\!(uv)^{\frac{1}{2}+\vartheta}H\_{\alpha}(u)H\_{\alpha}(v)\,du\,dv\,\delta^{2\vartheta}=\tfrac{1}{2}\left[\int\_{(0,+\infty)}\!\!\!u^{\frac{1}{2}+\vartheta}H\_{\alpha}(u)\,du\right]\,\delta^{2\vartheta}. |  |

where we used Fubini-Tonelli’s theorem in the first line to interwind the order of integration and the elementary inequality u​v≤12​(u+v)\sqrt{uv}\leq\frac{1}{2}(u+v) when u,v≥0u,\,v\geq 0 in the penultimate line. Furthermore,

|  |  |  |
| --- | --- | --- |
|  | ∫0+∞(Gα′​(t+δ)−Gα′​(t))2​𝑑t≤4α2​((21−θ​(πα)θ+1)​δθ)2​∫0+∞e2​t​cos⁡(πα)​𝑑t=[−2α2​cos⁡(πα)​(21−θ​(πα)θ+1)2]​δ2​ϑ.\int\_{0}^{+\infty}\big(G^{\prime}\_{\alpha}(t+\delta)-G^{\prime}\_{\alpha}(t)\big)^{2}dt\leq\frac{4}{\alpha^{2}}\left(\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}+1\right)\delta^{\theta}\right)^{2}\int\_{0}^{+\infty}\!\!e^{2t\cos\left(\frac{\pi}{\alpha}\right)}dt\,=\left[\frac{-2}{\alpha^{2}\cos\left(\frac{\pi}{\alpha}\right)}\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}+1\right)^{2}\right]\delta^{2\vartheta}. |  |

It follows that , ∫0+∞(fα,1​(t+δ)−fα,1​(t))2​𝑑t≤[∫ℝ+u12+ϑ​Hα​(u)​𝑑u+4α2​(21−θ​(πα)θ+1)2]​δ2​ϑ.\int\_{0}^{+\infty}\big(f\_{\alpha,1}(t+\delta)-f\_{\alpha,1}(t)\big)^{2}dt\leq\left[\int\_{\mathbb{R}\_{+}}\!\!\!u^{\frac{1}{2}+\vartheta}H\_{\alpha}(u)\,du+\frac{4}{\alpha^{2}}\left(2^{1-\theta}(\frac{\pi}{\alpha})^{\theta}+1\right)^{2}\right]\,\delta^{2\vartheta}.

Now, we derive form ([5.47](https://arxiv.org/html/2511.03474v1#S5.E47 "In 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) that:
Hα​(u)∼0sin⁡(π​α)π​uα−1 and Hα​(u)∼+∞sin⁡(π​α)π​u−(α+1),H\_{\alpha}(u)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{\alpha-1}\quad\mbox{ and }\quad H\_{\alpha}(u)\stackrel{{\scriptstyle+\infty}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{-(\alpha+1)},
Consequently

|  |  |  |
| --- | --- | --- |
|  | u12+ϑ​Hα​(u)∼0sin⁡(π​α)π​uα−12+ϑ and u12+ϑ​Hα​(u)∼+∞sin⁡(π​α)π​u−(−12+α−ϑ),u^{\frac{1}{2}+\vartheta}H\_{\alpha}(u)\stackrel{{\scriptstyle 0}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{\alpha-\frac{1}{2}+\vartheta}\quad\mbox{ and }\quad u^{\frac{1}{2}+\vartheta}H\_{\alpha}(u)\stackrel{{\scriptstyle+\infty}}{{\sim}}\frac{\sin(\pi\alpha)}{\pi}u^{-(-\frac{1}{2}+\alpha-\vartheta)}, |  |

which implies that ∫ℝ+u12+ϑ​Hα​(u)​𝑑u<+∞​ iff ​ϑ<α−12.\int\_{\mathbb{R}\_{+}}\!\!\!u^{\frac{1}{2}+\vartheta}H\_{\alpha}(u)\,du<+\infty\;\mbox{ iff }\;\vartheta<\alpha-\tfrac{1}{2}.
One concludes when λ>0\lambda>0 by scaling. □\Box

###### Lemma B.2.

Let α∈(1,32)\alpha\in(1,\frac{3}{2}). For every k≥1k\geq 1,

1. 1.

   ∀l≥1∀a≥1,B​(α​ℓ,α​(k−ℓ+a))≥1(α​(k+a)−1)​2α​k+2​(a−1)≥1α​(k+a)​2α​k+2​(a−1).\forall l\geq 1\quad\forall a\geq 1,\quad B(\alpha\ell,\alpha(k-\ell+a))\geq\frac{1}{(\alpha(k+a)-1)2^{\alpha k+2(a-1)}}\geq\frac{1}{\alpha(k+a)2^{\alpha k+2(a-1)}}.
2. 2.

   (a∗b)k≤2α​kΓ​(α​(k+1))​(1+(k+1)​(1+log⁡k)).(a\*b)\_{k}\leq\frac{2^{\alpha k}}{\Gamma(\alpha(k+1))}\left(1+(k+1)(1+\log k)\right).
3. 3.

   (b∗2)k≤(α​(k+2)−1)​(k+1)​2α​k+2Γ​(α​(k+2)).(b^{\*2})\_{k}\leq\frac{(\alpha(k+2)-1)(k+1)2^{\alpha k+2}}{\Gamma(\alpha(k+2))}.

Proof. 1.∀l≥1∀a≥1,\forall l\geq 1\quad\forall a\geq 1, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(α​ℓ,α​(k−ℓ+a))\displaystyle B(\alpha\ell,\alpha(k-\ell+a)) | =∫01uα​ℓ−1​(1−u)α​(k−ℓ+a)−1​𝑑u≥∫012uα​(k+a)−2​𝑑u+∫121(1−u)α​(k+a)−2​𝑑u\displaystyle=\int\_{0}^{1}u^{\alpha\ell-1}\left(1-u\right)^{\alpha(k-\ell+a)-1}\,du\geq\int\_{0}^{\frac{1}{2}}u^{\alpha(k+a)-2}\,du+\int\_{\frac{1}{2}}^{1}\left(1-u\right)^{\alpha(k+a)-2}\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​∫012uα​(k+a)−2​𝑑u≥1(α​(k+a)−1)​2α​(k+a)−2≥1(α​(k+a)−1)​2α​k+2​(a−1).\displaystyle=2\int\_{0}^{\frac{1}{2}}u^{\alpha(k+a)-2}\,du\geq\frac{1}{(\alpha(k+a)-1)2^{\alpha(k+a)-2}}\geq\frac{1}{(\alpha(k+a)-1)2^{\alpha k+2(a-1)}}. |  |

Where the last inequality comes from the fact that α<2\alpha<2.

2. Using the identity :
∀a,b>0Γ​(a+1)=a​Γ​(a),B​(a,b):=Γ​(a)​Γ​(b)Γ​(a+b)\forall a,b>0\quad\Gamma(a+1)=a\Gamma(a),\quad B(a,b):=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}, we have for every k≥1k\geq 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a∗b)k\displaystyle(a\*b)\_{k} | =∑ℓ=0k1Γ​(α​ℓ+1)​Γ​(α​(k−ℓ+1))=1Γ​(1)​Γ​(α​(k+1))+∑ℓ=1k1α​ℓ​Γ​(α​ℓ)​Γ​(α​(k−ℓ+1))\displaystyle=\sum\_{\ell=0}^{k}\frac{1}{\Gamma(\alpha\ell+1)\Gamma(\alpha(k-\ell+1))}=\frac{1}{\Gamma(1)\Gamma(\alpha(k+1))}+\sum\_{\ell=1}^{k}\frac{1}{\alpha\ell\Gamma(\alpha\ell)\Gamma(\alpha(k-\ell+1))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1Γ​(α​(k+1))​[1+1α​∑ℓ=1k1ℓ​1B​(α​ℓ,α​(k−ℓ+1))]≤2α​kΓ​(α​(k+1))​(1+(k+1)​(1+log⁡k)).\displaystyle=\frac{1}{\Gamma(\alpha(k+1))}\left[1+\frac{1}{\alpha}\sum\_{\ell=1}^{k}\frac{1}{\ell}\frac{1}{B(\alpha\ell,\alpha(k-\ell+1))}\right]\leq\frac{2^{\alpha k}}{\Gamma(\alpha(k+1))}\left(1+(k+1)(1+\log k)\right). |  |

where the last inequality comes from Lemma [B.2](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem2 "Lemma B.2. ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")(1) for a=1a=1 and the fact that 12α≤1\frac{1}{2^{\alpha}}\leq 1.
3. Likewise,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (b∗2)k\displaystyle(b^{\*2})\_{k} | =∑ℓ=0k1Γ​(α​(ℓ+1))​Γ​(α​(k−ℓ+1))=1Γ​(α​(k+2))​∑ℓ=0k1B​(α​(ℓ+1),α​(k−ℓ+1))\displaystyle=\sum\_{\ell=0}^{k}\frac{1}{\Gamma(\alpha(\ell+1))\Gamma(\alpha(k-\ell+1))}=\frac{1}{\Gamma(\alpha(k+2))}\sum\_{\ell=0}^{k}\frac{1}{B(\alpha(\ell+1),\alpha(k-\ell+1))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(α​(k+2)−1)​(k+1)Γ​(α​(k+2))​2α​k+2.\displaystyle\leq\frac{(\alpha(k+2)-1)(k+1)}{\Gamma(\alpha(k+2))}2^{\alpha k+2}. |  |

Still owing to Lemma [B.2](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem2 "Lemma B.2. ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (1), now for a=2a=2. □\Box

Proof of Proposition [5.2](https://arxiv.org/html/2511.03474v1#S5.Thmprop2 "Proposition 5.2 (Existence of the function 𝜍_{𝛼,𝜆,𝑐}² for 𝛼∈(1,2)). ‣ 5.2.1 Existence and computation of the function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1,3/2) ‣ 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

Step 1. (1) comes from equation ([5.51](https://arxiv.org/html/2511.03474v1#S5.E51 "In 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and Lemma [3.9](https://arxiv.org/html/2511.03474v1#S3.ThmTheorem9 "Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") (4).

Step 2. To establish statement (2), following the approach in [[36](https://arxiv.org/html/2511.03474v1#bib.bib36)], it is useful (though not strictly necessary) to transition to Laplace transforms. For simplicity, and as indicated in remark ([5.53](https://arxiv.org/html/2511.03474v1#S5.E53 "In 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we assume c=λ=1c=\lambda=1 and proceed by rewriting the series expansions in ([5.50](https://arxiv.org/html/2511.03474v1#S5.E50 "In 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")). We define Rα:=Rα,1R\_{\alpha}:=R\_{\alpha,1} and fα:=fα,1f\_{\alpha}:=f\_{\alpha,1}, as follows:

|  |  |  |
| --- | --- | --- |
|  | Rα​(t)=∑k≥0(−1)k​ak​tα​k,fα​(t)=tα−1​∑k≥0(−1)k​bk​tα​kwithak=1Γ​(α​k+1),bk=1Γ​(α​(k+1)),k≥0.R\_{\alpha}(t)=\sum\_{k\geq 0}(-1)^{k}a\_{k}t^{\alpha k},\;f\_{\alpha}(t)=t^{\alpha-1}\sum\_{k\geq 0}(-1)^{k}b\_{k}t^{\alpha k}\quad\text{with}\quad a\_{k}=\frac{1}{\Gamma(\alpha k+1)},\;b\_{k}=\frac{1}{\Gamma(\alpha(k+1))},\;k\geq 0. |  |

Now, using the Cauchy product of two series151515The Cauchy product of two series A​(x)=∑n=0∞an​xnA(x)=\sum\_{n=0}^{\infty}a\_{n}x^{n} and B​(x)=∑n=0∞bn​xnB(x)=\sum\_{n=0}^{\infty}b\_{n}x^{n} is given by the series C​(x)=A​(x)⋅B​(x)=∑n=0∞cn​xnC(x)=A(x)\cdot B(x)=\sum\_{n=0}^{\infty}c\_{n}x^{n}, where the coefficients cnc\_{n} are defined by cn=∑k=0nak​bn−kc\_{n}=\sum\_{k=0}^{n}a\_{k}b\_{n-k}.
and the fact that Luγ​(t)=t−(γ+1)​Γ​(γ+1)L\_{u^{\gamma}}(t)=t^{-(\gamma+1)}\Gamma(\gamma+1), we obtain the following Laplace transforms: LRα​fα​(t)=t−α​∑k≥0(−1)k​(a∗b)k​t−α​k​Γ​(α​(k+1))L\_{R\_{\alpha}f\_{\alpha}}(t)=t^{-\alpha}\sum\_{k\geq 0}(-1)^{k}(a\*b)\_{k}t^{-\alpha k}\Gamma(\alpha(k+1)) and
  
Lfα2​(t)=t−2​α+1​∑k≥0(−1)k​(b∗2)k​t−α​k​Γ​(α​(k+2)−1)L\_{f\_{\alpha}^{2}}(t)=t^{-2\alpha+1}\sum\_{k\geq 0}(-1)^{k}(b^{\*2})\_{k}t^{-\alpha k}\Gamma(\alpha(k+2)-1),
where for two sequences of real numbers (uk)k≥0(u\_{k})\_{k\geq 0} and (vk)k≥0(v\_{k})\_{k\geq 0}, the Cauchy product is defined as (u∗v)k=∑ℓ=0kuℓ​vk−ℓ(u\*v)\_{k}=\sum\_{\ell=0}^{k}u\_{\ell}v\_{k-\ell}. We define the sequences

|  |  |  |
| --- | --- | --- |
|  | b~k=(b∗2)k​Γ​(α​(k+2)−1)andc~k=ck​Γ​(α​(k−1)+2),k≥0.\widetilde{b}\_{k}=(b^{\*2})\_{k}\Gamma(\alpha(k+2)-1)\quad\text{and}\quad\widetilde{c}\_{k}=c\_{k}\Gamma(\alpha(k-1)+2),\;k\geq 0. |  |

Assuming that ςα2​(t)\varsigma\_{\alpha}^{2}(t) (for c=λ=1c=\lambda=1) takes the expected form ([5.53](https://arxiv.org/html/2511.03474v1#S5.E53 "In 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we have:

|  |  |  |
| --- | --- | --- |
|  | Lςα2​(t)=2​∑k≥0(−1)k​ck​t−(α​(k−1)+2)​Γ​(α​(k−1)+2)=2​tα−2​∑k≥0(−1)k​c~k​t−α​k.L\_{\varsigma\_{\alpha}^{2}}(t)=2\sum\_{k\geq 0}(-1)^{k}c\_{k}t^{-(\alpha(k-1)+2)}\Gamma(\alpha(k-1)+2)=2t^{\alpha-2}\sum\_{k\geq 0}(-1)^{k}\widetilde{c}\_{k}t^{-\alpha k}. |  |

Thus, by equating the coefficients from both sides of equation ([3.26](https://arxiv.org/html/2511.03474v1#S3.E26 "In Lemma 3.9 (On equation (E_{λ,c}): Laplace Transform of (𝐸_{𝜆,𝑐}), Uniqueness and Limit of 𝜍²_{𝜆,𝑐}). ‣ 3.2 Stabilizer and Fake Stationary Regimes ‣ 3 Investigating stationarity of a scaled stochastic Volterra Integral equation ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), we obtain the condition:

∀k≥0,(b~∗c~)k=(a∗b)k​Γ​(α​(k+1)).\forall k\geq 0,\quad(\widetilde{b}\*\widetilde{c})\_{k}=(a\*b)\_{k}\Gamma(\alpha(k+1)).

Simple computations yield c0=Γ​(α)2Γ​(2​α−1)​Γ​(2−α),c\_{0}=\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)\Gamma(2-\alpha)},
and for every k≥1k\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ck=Γ​(α)2Γ​(α​(k−1)+2)​Γ​(2​α−1)​[Γ​(α​(k+1))​(a∗b)k−∑ℓ=1kΓ​(α​(ℓ+2)−1)​Γ​(α​(k−ℓ−1)+2)​(b∗2)ℓ​ck−ℓ].c\_{k}=\frac{\Gamma(\alpha)^{2}}{\Gamma(\alpha(k-1)+2)\Gamma(2\alpha-1)}\left[\Gamma(\alpha(k+1))(a\*b)\_{k}-\sum\_{\ell=1}^{k}\Gamma(\alpha(\ell+2)-1)\Gamma(\alpha(k-\ell-1)+2)(b^{\*2})\_{\ell}c\_{k-\ell}\right]. |  | (B.70) |

Using standard identities such as Γ​(a)​Γ​(b)=Γ​(a+b)​B​(a,b)\Gamma(a)\Gamma(b)=\Gamma(a+b)B(a,b) for a,b>0a,b>0, where B​(a,b)=∫01ua−1​(1−u)b−1​𝑑uB(a,b)=\int\_{0}^{1}u^{a-1}(1-u)^{b-1}\,du, and Γ​(a+1)=a​Γ​(a)\Gamma(a+1)=a\Gamma(a), we arrive at the formulation of the ckc\_{k}’s provided in the proposition, which is more suitable for numerical computations.

Step 3. Using standard methods, as in [[10](https://arxiv.org/html/2511.03474v1#bib.bib10)]
or Appendix A of [[36](https://arxiv.org/html/2511.03474v1#bib.bib36)] (in the case α∈(12,1)\alpha\in(\frac{1}{2},1)), we show that the radius of convergence ρα\rho\_{\alpha} of the power series defined by the coefficients ckc\_{k} is infinite.
Firstly, let us prove by induction that there exists A>2α+2A>2^{\alpha+2} and K>1K>1 such that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀k≥0|ck|≤K​AkΓ​(α​(k−1)+2).\forall k\geq 0\quad|c\_{k}|\leq\frac{KA^{k}}{\Gamma(\alpha(k-1)+2)}. |  | (B.71) |

By the triangle inequality, we get the bound :

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ck|≤Γ​(α)2​Γ​(α​(k+1))Γ​(α​(k−1)+2)​Γ​(2​α−1)​[(a∗b)k+α​(k+1)​∑ℓ=1kB​(α​(ℓ+2)−1,α​(k−ℓ−1)+2)​(b∗2)ℓ​|ck−ℓ|].\displaystyle\left|c\_{k}\right|\leq\frac{\Gamma(\alpha)^{2}\Gamma(\alpha(k+1))}{\Gamma(\alpha(k-1)+2)\Gamma(2\alpha-1)}\left[(a\*b)\_{k}+\alpha(k+1)\sum\_{\ell=1}^{k}B\left(\alpha(\ell+2)-1,\alpha(k-\ell-1)+2\right)(b^{\*2})\_{\ell}|c\_{k-\ell}|\right]. |  | (B.72) |

Initialisation:
For k=0k=0, c0=Γ​(α)2Γ​(2−α)​Γ​(2​α−1)≤KΓ​(2−α)c\_{0}=\frac{\Gamma(\alpha)^{2}}{\Gamma(2-\alpha)\Gamma(2\alpha-1)}\leq\frac{K}{\Gamma(2-\alpha)} since K>1K>1 and by log-convexity Γ​(α)2Γ​(2​α−1)<1\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)}<1.
Heredity:
Now let k≥1k\geq 1 and assume that cℓc\_{\ell} satisfies the inequality ([B.71](https://arxiv.org/html/2511.03474v1#A2.E71 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) for every ℓ=0,…,k−1\ell=0,\dots,k-1. Then, for every ℓ=1,…,k\ell=1,\dots,k,

|  |  |  |
| --- | --- | --- |
|  | B​(α​(ℓ+2)−1,α​(k−ℓ−1)+2)​(b∗2)ℓ​|ck−ℓ|≤Γ​(α​(ℓ+2)−1)​Γ​(α​(k−ℓ−1)+2)Γ​(α​(k+1)+1)​Γ​(α​(k−ℓ−1)+2)×K​Ak−ℓ​(b∗2)ℓ\displaystyle\,B\left(\alpha(\ell+2)-1,\alpha(k-\ell-1)+2\right)(b^{\*2})\_{\ell}|c\_{k-\ell}|\leq\frac{\Gamma(\alpha(\ell+2)-1)\Gamma(\alpha(k-\ell-1)+2)}{\Gamma(\alpha(k+1)+1)\;\Gamma(\alpha(k-\ell-1)+2)}\times KA^{k-\ell}(b^{\*2})\_{\ell} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​Ak−ℓ​Γ​(α​(ℓ+2)−1)Γ​(α​(k+1)+1)​(α​(l+2)−1)​(l+1)​2α​l+2Γ​(α​(l+2))≤K​Ak−ℓΓ​(α​(k+1)+1)​(α​(l+2)−1)​(l+1)​2α​l+2(α​(ℓ+2)−1)\displaystyle\leq\frac{KA^{k-\ell}\Gamma(\alpha(\ell+2)-1)}{\Gamma(\alpha(k+1)+1)}\frac{(\alpha(l+2)-1)(l+1)2^{\alpha l+2}}{\Gamma(\alpha(l+2))}\leq\frac{KA^{k-\ell}}{\Gamma(\alpha(k+1)+1)}\frac{(\alpha(l+2)-1)(l+1)2^{\alpha l+2}}{(\alpha(\ell+2)-1)} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K(l+1)​2α​l+2​Ak−ℓα​(k+1)​Γ​(α​(k+1)).Inserting this bound into the inequality ([B.72](https://arxiv.org/html/2511.03474v1#A2.E72 "In Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) for ck gives:\displaystyle\leq K\frac{(l+1)2^{\alpha l+2}A^{k-\ell}}{\alpha(k+1)\Gamma(\alpha(k+1))}.\quad\text{Inserting this bound into the inequality\penalty 10000\ \eqref{eq:second\_inequality} for $c\_{k}$ gives:} |  |

|ck|≤Γ​(α)2Γ​(α​(k−1)+2)​Γ​(2​α−1)​[Γ​(α​(k+1))​(a∗b)k+K​Ak​1Γ​(α​(k+1))​∑ℓ=1k(ℓ+1)​ρℓ].\left|c\_{k}\right|\leq\frac{\Gamma(\alpha)^{2}}{\Gamma(\alpha(k-1)+2)\Gamma(2\alpha-1)}\left[\Gamma(\alpha(k+1))(a\*b)\_{k}+K\,A^{k}\frac{1}{\Gamma(\alpha(k+1))}\sum\_{\ell=1}^{k}(\ell+1)\rho^{\ell}\right].

where we set ρ=ρ​(A):=2α+2A\rho=\rho(A):=\frac{2^{\alpha+2}}{A}. Next, dividing the above inequality by K​AkKA^{k} and using the upper bound for (a∗b)k(a\*b)\_{k} from Lemma [B.2](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem2 "Lemma B.2. ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")(2):

|  |  |  |
| --- | --- | --- |
|  | |ck|K​Ak≤1Γ​(α​(k−1)+2)​Γ​(α)2Γ​(2​α−1)​[ρkK​(1+(k+1)​(1+log⁡k))+1(1−ρ)2].\frac{\left|c\_{k}\right|}{KA^{k}}\leq\frac{1}{\Gamma(\alpha(k-1)+2)}\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)}\left[\frac{\rho^{k}}{K}\left(1+(k+1)(1+\log k)\right)+\frac{1}{(1-\rho)^{2}}\right]. |  |

Owing to the elementary inequality: ∀ρ∈(0,1),∑l≥1l​ρl−1≤1(1−ρ)2\forall\,\rho\in(0,1),\quad\sum\_{l\geq 1}l\rho^{l-1}\leq\frac{1}{(1-\rho)^{2}}.
Let ϵ>0\epsilon>0 and let A=AϵA=A\_{\epsilon} be large enough so that
supk≥1(ρk+ρk​(k+1)​(1+log⁡k))<ϵand1(1−ρ)2<1+ϵ.\sup\_{k\geq 1}\left(\rho^{k}+\rho^{k}(k+1)(1+\log k)\right)<\epsilon\quad\text{and}\quad\frac{1}{(1-\rho)^{2}}<1+\epsilon.
Due to the log-convexity of the Gamma function, log⁡Γ​(α)≤12​log⁡Γ​(2​α−1)+log⁡Γ​(1)=12​log⁡Γ​(2​α−1)\log\Gamma(\alpha)\leq\tfrac{1}{2}\log\Gamma(2\alpha-1)+\log\Gamma(1)=\tfrac{1}{2}\log\Gamma(2\alpha-1), so that Γ​(α)2Γ​(2​α−1)<1\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)}<1. Thus, it is possible to choose ϵ\epsilon small enough and KK large enough such that:

Γ​(α)2Γ​(2​α−1)​[ρkK​(1+(k+1)​(1+log⁡k))+1(1−ρ)2]≤Γ​(α)2Γ​(2​α−1)​(ϵK+1+ϵ)<1.\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)}\left[\frac{\rho^{k}}{K}\left(1+(k+1)(1+\log k)\right)+\frac{1}{(1-\rho)^{2}}\right]\leq\frac{\Gamma(\alpha)^{2}}{\Gamma(2\alpha-1)}\left(\frac{\epsilon}{K}+1+\epsilon\right)<1.

Consequently, |ck|≤K​AkΓ​(α​(k−1)+2).|c\_{k}|\leq\frac{KA^{k}}{\Gamma(\alpha(k-1)+2)}.
And thus the Cauchy-Hadamard’s formula for the radius of convergence together with Stirling’s formula give:

lim supk→∞|ck|1k≤lim supk→∞(K​AkΓ​(α​k+2−α))1/k∼limk→∞A​K1ke−α​(α​(k−1)+2)α=0.\limsup\_{k\to\infty}|c\_{k}|^{\frac{1}{k}}\leq\limsup\_{k\to\infty}\left(\frac{K\,A^{k}}{\Gamma(\alpha k+2-\alpha)}\right)^{1/k}\sim\lim\_{k\to\infty}A\frac{K^{\frac{1}{k}}}{e^{-\alpha}(\alpha(k-1)+2)^{\alpha}}=0.

Proof of Proposition [5.3](https://arxiv.org/html/2511.03474v1#S5.Thmprop3 "Proposition 5.3 (Existence of 𝜍_{𝛼,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation for 𝛼∈(1,3/2)). ‣ 5.2.1 Existence and computation of the function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1,3/2) ‣ 5.2 The function 𝜍_{𝛼,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(0,2) ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").From equation ([6.58](https://arxiv.org/html/2511.03474v1#S6.E58 "In 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")), there exists an analytic function g~α:ℂ→ℂ\tilde{g}\_{\alpha}:\mathbb{C}\to\mathbb{C} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t≥0,gα,ρ,λ​(t)=e−2​ρ​t​t1−α​g~α​(λ​tα)andg~α​(0)=2​c​λ​c0>0.\forall t\geq 0,\quad g\_{\alpha,\rho,\lambda}(t)=e^{-2\rho t}t^{1-\alpha}\tilde{g}\_{\alpha}(\lambda\,t^{\alpha})\quad\textit{and}\quad\tilde{g}\_{\alpha}(0)=2\,c\,\lambda\,c\_{0}>0. |  | (B.73) |

Step 1. Case α≤1\alpha\leq 1:
The class of completely monotone (CM) functions is a convex cone, thus is stable under pointwise positive
summation, product, and also convolution. Differentiating both sides of equation ([6.59](https://arxiv.org/html/2511.03474v1#S6.E59 "In item 1 ‣ Proposition 6.1 (Existence and Properties of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² for 𝛼∈(1/2,3/2)). ‣ 6.2 Existence of 𝜍_{𝛼,𝜌,𝜆,𝑐} i.e. positivity computation of the function 𝜍_{𝛼,𝜌,𝜆,𝑐}² solution of the stabilizer equation when 𝛼∈(1/2,3/2) ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations")) and using the
fact that gα,ρ,λ​(0)=0g\_{\alpha,\rho,\lambda}(0)=0 yields

|  |  |  |
| --- | --- | --- |
|  | 2​c​λ2​fα,ρ,λ​(t)​Rα,ρ,λ​(t)=∫0tfα,ρ,λ2​(t−s)​gα,ρ,λ′​(s)​𝑑s,∀t≥0.2c\lambda^{2}f\_{\alpha,\rho,\lambda}(t)R\_{\alpha,\rho,\lambda}(t)=\int\_{0}^{t}f\_{\alpha,\rho,\lambda}^{2}(t-s)\,g^{\prime}\_{\alpha,\rho,\lambda}(s)\,ds,\quad\forall\,t\geq 0. |  |

Here fα,ρ,λ​(t):=e−ρ​t​fα,λ​(t)f\_{\alpha,\rho,\lambda}(t):=e^{-\rho t}f\_{\alpha,\lambda}(t), which is CM as the
product of two CM functions. Hence Rα,ρ,λR\_{\alpha,\rho,\lambda} is CM, and consequently
both 2​c​λ2​fα,ρ,λ​Rα,ρ,λ2c\lambda^{2}f\_{\alpha,\rho,\lambda}R\_{\alpha,\rho,\lambda} and
fα,ρ,λ2f\_{\alpha,\rho,\lambda}^{2} are CM functions.
Since gα,ρ,λ​(0)=0g\_{\alpha,\rho,\lambda}(0)=0, we deduce from [[4](https://arxiv.org/html/2511.03474v1#bib.bib4), Theorem 5.5.5]
that gα,ρ,λ​(t)=∫0tgα,ρ,λ′​(s)​𝑑s≥0,∀t≥0.g\_{\alpha,\rho,\lambda}(t)=\int\_{0}^{t}g^{\prime}\_{\alpha,\rho,\lambda}(s)\,ds\geq 0,\quad\forall\,t\geq 0.

For simplification, we set gα,ρ,λ≡gαg\_{\alpha,\rho,\lambda}\equiv g\_{\alpha}. One shows, as in [[36](https://arxiv.org/html/2511.03474v1#bib.bib36)], by contradiction that gα′′≤0g^{{}^{\prime\prime}}\_{\alpha}\leq 0 on (0,+∞)(0,+\infty), i.e. gαg\_{\alpha} is concave.
Using the product and chain rules, we have that
  
gα′​(t)=e−2​ρ​t​((−2​ρ​t1−α+(1−α)​t−α)​g~α​(λ​tα)+λ​α​g~α′​(λ​tα))g^{\prime}\_{\alpha}(t)=e^{-2\rho t}\left((-2\rho t^{1-\alpha}+(1-\alpha)t^{-\alpha})\tilde{g}\_{\alpha}(\lambda t^{\alpha})+\lambda\,\alpha\,\tilde{g}^{\prime}\_{\alpha}(\lambda t^{\alpha})\right).
Since α<1,limt→0+t−αt1−α=limt→0+1t=+∞\alpha<1,\quad\lim\_{t\to 0^{+}}\frac{t^{-\alpha}}{t^{1-\alpha}}=\lim\_{t\to 0^{+}}\frac{1}{t}\\
=+\infty, we have
gα′​(t)​∼t→0+​(1−α)​t−α​g~α​(0)+λ​α​g~α′​(0)g^{\prime}\_{\alpha}(t)\underset{t\to 0^{+}}{\sim}(1-\alpha)t^{-\alpha}\tilde{g}\_{\alpha}(0)+\lambda\,\alpha\tilde{g}^{\prime}\_{\alpha}(0) so that limt→0+gα′​(t)=+∞\lim\_{t\to 0^{+}}g^{\prime}\_{\alpha}(t)=+\infty.
Moreover, by Tauberian Final Value Theorem if limt→+∞g~α′​(t)\lim\_{t\to+\infty}\tilde{g}^{\prime}\_{\alpha}(t) exists, then

|  |  |  |
| --- | --- | --- |
|  | limt→+∞g~α′​(t)=limz→0z​Lg~α′​(z)​(z)=limz→0(z2​Lg~α​(z)−z​g~α​(0))=limz→0(z2​Lg~α​(0)−z​g~α​(0))=0\lim\_{t\to+\infty}\tilde{g}^{\prime}\_{\alpha}(t)=\lim\_{z\to 0}zL\_{\tilde{g}^{\prime}\_{\alpha}}(z)(z)=\lim\_{z\to 0}\left(z^{2}L\_{\tilde{g}\_{\alpha}}(z)-z\tilde{g}\_{\alpha}(0)\right)=\lim\_{z\to 0}\left(z^{2}L\_{\tilde{g}\_{\alpha}}(0)-z\tilde{g}\_{\alpha}(0)\right)=0 |  |

since g~α\tilde{g}\_{\alpha} is integrable and thus have a finite Laplace transform.
Consequently, limt→+∞gα′​(t)=0\lim\_{t\to+\infty}g^{\prime}\_{\alpha}(t)=0.
Finally, limt→0+gα′​(t)=+∞\lim\_{t\to 0^{+}}g^{\prime}\_{\alpha}(t)=+\infty , limt→+∞gα′​(t)=0\lim\_{t\to+\infty}g^{\prime}\_{\alpha}(t)=0 and gα′g^{\prime}\_{\alpha} is non-increasing on (0,+∞)(0,+\infty) (gα′′≤0g^{\prime\prime}\_{\alpha}\leq 0), it follows that gα′​(t)≥0∀t∈(0,+∞)g\_{\alpha}^{\prime}(t)\geq 0\quad\forall t\in(0,+\infty).
Hence gαg\_{\alpha} is concave, non-decreasing and non-negative on (0,+∞)(0,+\infty).

step 2.Case α>1\alpha>1:
We have limt→0+gα,ρ,λ=+∞\lim\_{t\to 0^{+}}g\_{\alpha,\rho,\lambda}=+\infty and limt→+∞gα,ρ,λ>0\lim\_{t\to+\infty}g\_{\alpha,\rho,\lambda}>0.
Hence, there exists t0,t1>0t\_{0},t\_{1}>0 such that gα,ρ,λ≥0g\_{\alpha,\rho,\lambda}\geq 0 at least on the small intervals (0,t0)∪(t1,+∞)(0,t\_{0})\cup(t\_{1},+\infty) with t0=inf{t:gα,ρ,λ​(t)<0}t\_{0}=\inf\{t\,:\,g\_{\alpha,\rho,\lambda}(t)<0\} and t1=sup{t:gα,ρ,λ​(t)<0}t\_{1}=\sup\{t\,:\,g\_{\alpha,\rho,\lambda}(t)<0\}.
By continuity of gα,ρ,λg\_{\alpha,\rho,\lambda} it is clear that gα,ρ,λ​(t0)=gα,ρ,λ​(t1)=0g\_{\alpha,\rho,\lambda}(t\_{0})=g\_{\alpha,\rho,\lambda}(t\_{1})=0 and gα,ρ,λ≥0g\_{\alpha,\rho,\lambda}\geq 0 on [0,t0]∪[t1,+∞)[0,t\_{0}]\cup[t\_{1},+\infty).
While numerical computations suggest that gα,ρ,λg\_{\alpha,\rho,\lambda} is positive on ℝ+\mathbb{R}\_{+} (i.e. t0=t1=∞t\_{0}=t\_{1}=\infty), establishing this positivity analytically turns out to be quite challenging.
We shall, however, establish that if Tα,λ,ρT^{\alpha,\lambda,\rho} is the first zero of the resolvent Rα,ρ,λR\_{\alpha,\rho,\lambda} (see [[24](https://arxiv.org/html/2511.03474v1#bib.bib24), Proposition 3.13.] for all zeros of the functions EαE\_{\alpha}), then, since Rα,ρ,λ2R\_{\alpha,\rho,\lambda}^{2} decreases strictly on (0,Tα,λ,ρ)(0,T^{\alpha,\lambda,\rho}), the function gα,ρ,λg\_{\alpha,\rho,\lambda} remains non-negative over that interval.

Let’s assume that t0∈(0,Tα,λ,ρ)t\_{0}\in(0,T^{\alpha,\lambda,\rho}) and thus gα,ρ,λ≤0g\_{\alpha,\rho,\lambda}\leq 0 on a small interval [t0,t0+η]⊂(0,Tα,λ,ρ)[t\_{0},t\_{0}+\eta]\subset(0,T^{\alpha,\lambda,\rho}) for some η>0\eta>0.
Then, for every t∈(t0,t0+η]t\in(t\_{0},t\_{0}+\eta], there exists τ>0\tau>0 such that t=t0+τt=t\_{0}+\tau.
Let δ∈(0,τ2)\delta\in(0,\frac{\tau}{2}), and set c:=−maxs∈[t0+δ,t0+τ]⁡gα,ρ,λ​(s)c:=-\max\_{s\in[t\_{0}+\delta,t\_{0}+\tau]}g\_{\alpha,\rho,\lambda}(s).
By continuity c>0c>0 and
gα,ρ,λ​(s)≤−cg\_{\alpha,\rho,\lambda}(s)\leq-c for all s∈[t0+δ,t0+τ]s\in[t\_{0}+\delta,t\_{0}+\tau].
For simplification, we set fα,ρ,λ≡fαf\_{\alpha,\rho,\lambda}\equiv f\_{\alpha} and Rα,ρ,λ≡Rα,gα,ρ,λ≡gαR\_{\alpha,\rho,\lambda}\equiv R\_{\alpha},g\_{\alpha,\rho,\lambda}\equiv g\_{\alpha}. Then, we have:

|  |  |  |
| --- | --- | --- |
|  | (fα2∗gα)​(t0+τ)−(fα2∗gα)​(t0)=∫0t0(fα2​(t0+τ−s)−fα2​(t0−s))⏟≥⁣≈0​gα​(s)⏟≥0​𝑑s+∫t0t0+δfα2​(t0+τ−s)​gα​(s)⏟≤0​𝑑s\displaystyle\,(f\_{\alpha}^{2}\*g\_{\alpha})(t\_{0}+\tau)-(f\_{\alpha}^{2}\*g\_{\alpha})(t\_{0})=\int\_{0}^{t\_{0}}\underbrace{(f\_{\alpha}^{2}(t\_{0}+\tau-s)-f\_{\alpha}^{2}(t\_{0}-s))}\_{\geq\approx 0}\,\underbrace{g\_{\alpha}(s)}\_{\geq 0}\,ds+\int\_{t\_{0}}^{t\_{0}+\delta}f\_{\alpha}^{2}(t\_{0}+\tau-s)\,\underbrace{g\_{\alpha}(s)}\_{\leq 0}\,ds |  |
|  |  |  |
| --- | --- | --- |
|  | +∫t0+δt0+τfα2​(t0+τ−s)​gα​(s)⏟≤0​𝑑s≤I1−I2−c​(∫0τ−δfα2​(u)​𝑑u).\displaystyle\hskip 18.49988pt\hskip 113.81102pt+\int\_{t\_{0}+\delta}^{t\_{0}+\tau}f\_{\alpha}^{2}(t\_{0}+\tau-s)\,\underbrace{g\_{\alpha}(s)}\_{\leq 0}\,ds\leq I\_{1}-I\_{2}-c\left(\int\_{0}^{\tau-\delta}f\_{\alpha}^{2}(u)\,du\right).\; |  |

where I2:=−∫t0t0+δfα2​(t0+τ−s)​gα​(s)​𝑑s≥0I\_{2}:=-\int\_{t\_{0}}^{t\_{0}+\delta}f\_{\alpha}^{2}(t\_{0}+\tau-s)\,g\_{\alpha}(s)\,ds\geq 0 and I1:=∫0t0(fα2​(t0+τ−s)−fα2​(t0−s))​gα​(s)​𝑑s≥0I\_{1}:=\int\_{0}^{t\_{0}}(f\_{\alpha}^{2}(t\_{0}+\tau-s)-f\_{\alpha}^{2}(t\_{0}-s))\,g\_{\alpha}(s)\,ds\geq 0

However, as I1I\_{1} is nonnegative and close to zero, for an adequate choice of δ∈(0,τ2)\delta\in(0,\frac{\tau}{2}), the upper bound above is strictly negative.
On the other hand,
(fα2∗gα)​(t0+τ)−(fα2∗gα)​(t0)=c​λ2​(Rα2​(t0)−Rα2​(t0+τ))>0(f\_{\alpha}^{2}\*g\_{\alpha})(t\_{0}+\tau)-(f\_{\alpha}^{2}\*g\_{\alpha})(t\_{0})=c\lambda^{2}(R^{2}\_{\alpha}(t\_{0})-R^{2}\_{\alpha}(t\_{0}+\tau))>0,
which yields a contradiction.
Hence, for every large enough n≥0n\geq 0, there exists
tn+∈(t0,t0+1n]t\_{n}^{+}\in(t\_{0},t\_{0}+\frac{1}{n}] such that gα​(tn+)>0g\_{\alpha}(t\_{n}^{+})>0.
On the other hand, by the very definition of t0t\_{0},
there exists a sequence tn−>t0t\_{n}^{-}>t\_{0}, n≥1n\geq 1, such that gα​(tn−)<0g\_{\alpha}(t\_{n}^{-})<0.
One then builds by induction a sequence (τn)n≥1(\tau\_{n})\_{n\geq 1} such that
gα​(τ2​n+1)<0g\_{\alpha}(\tau\_{2n+1})<0 and gα​(τ2​n)>0g\_{\alpha}(\tau\_{2n})>0, with τn→t0\tau\_{n}\to t\_{0} as n→+∞n\to+\infty, τn>t0\tau\_{n}>t\_{0}.
In turn this implies, by the intermediate value theorem,
the existence of a sequence (τ~n)n≥1(\tilde{\tau}\_{n})\_{n\geq 1} such that
g~α​(λ​τ~nα)=gα​(τ~n)=0\tilde{g}\_{\alpha}(\lambda\tilde{\tau}^{\alpha}\_{n})=g\_{\alpha}(\tilde{\tau}\_{n})=0,
λ​τ~nα>λ​t0α\lambda\tilde{\tau}\_{n}^{\alpha}>\lambda t\_{0}^{\alpha} and
λ​τ~nα→λ​t0α\lambda\tilde{\tau}\_{n}^{\alpha}\to\lambda t\_{0}^{\alpha} by the continuity of gαg\_{\alpha}.
As g~α\tilde{g}\_{\alpha} is analytic, it implies that g~α\tilde{g}\_{\alpha} is everywhere zero.
Hence a contradiction since g~α​(0)>0\tilde{g}\_{\alpha}(0)>0.

From the above steps, we have ∀t≥0gα,ρ,λ​(t)≥0\forall t\geq 0\quad g\_{\alpha,\rho,\lambda}(t)\geq 0 on an interval I⊆(0,+∞)I\subseteq(0,+\infty) so that the function gα,ρ,λ\sqrt{g\_{\alpha,\rho,\lambda}} is well-defined on II. □\square

Proof of Proposition [6.1](https://arxiv.org/html/2511.03474v1#S6.ThmTheorem1 "Proposition 6.1. ‣ 6.1 limit-from𝛼- Exponential Fractional kernels 1/2<𝛼<3/2 ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").
(a)(a) We consider the function Rα,ρ,λ​(t)=1+∑k≥1(−1)k​λkΓ​(k​α)​Ik​(t)R\_{\alpha,\rho,\lambda}(t)=1+\sum\_{k\geq 1}(-1)^{k}\frac{\lambda^{k}}{\Gamma(k\alpha)}I\_{k}(t) where Ik​(t)=∫0te−ρ​s​sk​α−1​𝑑sI\_{k}(t)=\int\_{0}^{t}e^{-\rho s}s^{k\alpha-1}\,ds. Given that for all k≥1k\geq 1, the function s↦e−ρ​s​sk​α−1s\mapsto e^{-\rho s}s^{k\alpha-1} is measurable and locally integrable on (0,t)(0,t), the map t↦∫0te−ρ​s​sk​α−1​dst\mapsto\int\_{0}^{t}e^{-\rho s}s^{k\alpha-1}\,\mathrm{d}s is differentiable. Moreover, the series of derivatives ∑k≥1(−1)k​λkΓ​(k​α)​e−ρ​t​tk​α−1\sum\_{k\geq 1}(-1)^{k}\frac{\lambda^{k}}{\Gamma(k\alpha)}e^{-\rho t}t^{k\alpha-1}
converges absolutely locally uniformly in t>0t>0. Hence, by the dominated convergence theorem (or Lebesgue’s theorem on differentiation under the integral sign), term-by-term differentiation is justified, and Rα,ρ,λ​(t)R\_{\alpha,\rho,\lambda}(t) is differentiable for t>0t>0, with its derivative given by: Rα,ρ,λ′(t)=∑k≥1(−1)kλkΓ​(k​α)e−ρ​ttk​α−1=:fα,ρ,λ(t),R^{\prime}\_{\alpha,\rho,\lambda}(t)=\sum\_{k\geq 1}(-1)^{k}\frac{\lambda^{k}}{\Gamma(k\alpha)}e^{-\rho t}t^{k\alpha-1}=:f\_{\alpha,\rho,\lambda}(t),
One could argue similarly to show that Rα,ρ,λR\_{\alpha,\rho,\lambda} is infinitely differentiable, i.e., 𝒞∞\mathcal{C}^{\infty} on (0,+∞)(0,+\infty). Alternatively, observe that for all t>0t>0, we have fα,ρ,λ​(t)=e−ρ​t​fα,λ​(t),f\_{\alpha,\rho,\lambda}(t)=e^{-\rho t}f\_{\alpha,\lambda}(t),
which is 𝒞∞\mathcal{C}^{\infty} as the product of such functions, by virtue of the first claim in Proposition [5.2](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem2 "Proposition 5.2 (𝛼-fractional kernels 1<𝛼<2). ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

(b)(b) The representation of fα,ρ,λf\_{\alpha,\rho,\lambda} follows by definition and from the claim (b)(b) of Proposition [6.1](https://arxiv.org/html/2511.03474v1#S6.ThmTheorem1 "Proposition 6.1. ‣ 6.1 limit-from𝛼- Exponential Fractional kernels 1/2<𝛼<3/2 ‣ 6 Applications to Exponential-Fractional Stochastic Volterra Equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations").

(c)(c) Let us prove the L2​βL^{2\beta}-integrability of fα,ρ,λf\_{\alpha,\rho,\lambda}. Once noted that fα,ρ,λ=e−ρ​t​fα,λf\_{\alpha,\rho,\lambda}=e^{-\rho t}f\_{\alpha,\lambda} so that

|  |  |  |
| --- | --- | --- |
|  | ∫0+∞fα,ρ,λ2​β​(t)​𝑑t=∫0+∞e−2​β​ρ​t​fα,λ2​β​(t)​𝑑t≤∫0+∞fα,λ2​β​(t)​𝑑t,\int\_{0}^{+\infty}f\_{\alpha,\rho,\lambda}^{2\beta}(t)dt=\int\_{0}^{+\infty}e^{-2\beta\rho t}f\_{\alpha,\lambda}^{2\beta}(t)dt\leq\int\_{0}^{+\infty}f\_{\alpha,\lambda}^{2\beta}(t)dt, |  |

it is clear that it is enough to have that fα,λf\_{\alpha,\lambda} is ℒ2​β{\cal L}^{2\beta}-integrable.

It follows from [[36](https://arxiv.org/html/2511.03474v1#bib.bib36), Proposition 5.1] and Proposition [5.2](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem2 "Proposition 5.2 (𝛼-fractional kernels 1<𝛼<2). ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") that fα,ρ,λf\_{\alpha,\rho,\lambda} is ℒ2​β{\cal L}^{2\beta}-integrable ∀β∈(0,12​(1−α))\forall\beta\in\big(0,\frac{1}{2(1-\alpha)}\big) if α<1\alpha<1 and ∀β∈ℝ+∗\forall\beta\in\mathbb{R}\_{+}^{\*} if α>1\alpha>1.

As for the ℒ2​(ℝ+){\cal L}^{2}(\mathbb{R}\_{+})-ϑ\vartheta-Hölder continuity of fα,ρ,λf\_{\alpha,\rho,\lambda}, let δ>0\delta>0. One has

|  |  |  |
| --- | --- | --- |
|  | fα,ρ,λ​(t+δ)−fα,ρ,λ​(t)=e−ρ​(t+δ)​(fα,λ​(t+δ)−fα,λ​(t))+fα,λ​(t)​(e−ρ​(t+δ)−e−ρ​t).f\_{\alpha,\rho,\lambda}(t+\delta)-f\_{\alpha,\rho,\lambda}(t)=e^{-\rho(t+\delta)}\left(f\_{\alpha,\lambda}(t+\delta)-f\_{\alpha,\lambda}(t)\right)+f\_{\alpha,\lambda}(t)\left(e^{-\rho(t+\delta)}-e^{-\rho t}\right). |  |

Then, for i∈{1,2}i\in\{1,2\}, we write:

|  |  |  |
| --- | --- | --- |
|  | |fα,ρ,λ​(t+δ)−fα,ρ,λ​(t)|i≤2i−1​(e−i​ρ​(t+δ)​|fα,λ​(t+δ)−fα,λ​(t)|i+e−i​ρ​t​|fα,λ​(t)|i​(1−e−i​ρ​δ)i).\left|f\_{\alpha,\rho,\lambda}(t+\delta)-f\_{\alpha,\rho,\lambda}(t)\right|^{i}\leq 2^{i-1}\left(e^{-i\rho(t+\delta)}\left|f\_{\alpha,\lambda}(t+\delta)-f\_{\alpha,\lambda}(t)\right|^{i}+e^{-i\rho t}\left|f\_{\alpha,\lambda}(t)\right|^{i}(1-e^{-i\rho\delta})^{i}\right). |  |

Integrating both side and using again Lemma [B.1](https://arxiv.org/html/2511.03474v1#A2.ThmTheorem1 "Lemma B.1 (Expansions). ‣ Appendix B Supplementary material and Proofs. ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations"), one may deduce

|  |  |  |
| --- | --- | --- |
|  | ∫0∞|fα,ρ,λ​(t+δ)−fα,ρ,λ​(t)|i​𝑑t≤2i−1​(e−i​ρ​δ​∫0∞|fα,λ​(t+δ)−fα,λ​(t)|i​𝑑t+(ρ​δ)i​ϑ​∫0∞|fα,λ​(t)|i​𝑑t).\int\_{0}^{\infty}\left|f\_{\alpha,\rho,\lambda}(t+\delta)-f\_{\alpha,\rho,\lambda}(t)\right|^{i}dt\leq 2^{i-1}\left(e^{-i\rho\delta}\int\_{0}^{\infty}\left|f\_{\alpha,\lambda}(t+\delta)-f\_{\alpha,\lambda}(t)\right|^{i}dt+(\rho\delta)^{i\vartheta}\int\_{0}^{\infty}\left|f\_{\alpha,\lambda}(t)\right|^{i}dt\right). |  |

Consequently, since fα,λ∈L2​(Leb1)f\_{\alpha,\lambda}\in L^{2}(\text{Leb}\_{1})

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∫0∞|fα,ρ,λ​(t+δ)−fα,ρ,λ​(t)|i​𝑑t)1/i\displaystyle\left(\int\_{0}^{\infty}\left|f\_{\alpha,\rho,\lambda}(t+\delta)-f\_{\alpha,\rho,\lambda}(t)\right|^{i}dt\right)^{1/i} | ≤e−ρ​δ​(∫0∞|fα,λ​(t+δ)−fα,λ​(t)|i​𝑑t)1/i+(ρ​δ)ϑ​(∫0∞|fα,λ​(t)|i​𝑑t)1i\displaystyle\leq e^{-\rho\delta}\left(\int\_{0}^{\infty}\left|f\_{\alpha,\lambda}(t+\delta)-f\_{\alpha,\lambda}(t)\right|^{i}dt\right)^{1/i}+(\rho\delta)^{\vartheta}\left(\int\_{0}^{\infty}\left|f\_{\alpha,\lambda}(t)\right|^{i}dt\right)^{\frac{1}{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤e−ρ​δ​Cϑ,λ​δϑ+Cfλ​δϑ:=Cϑ,ρ,λ​δϑ.\displaystyle\leq e^{-\rho\delta}C\_{\vartheta,\lambda}\delta^{\vartheta}+C\_{f\_{\lambda}}\delta^{\vartheta}:=C\_{\vartheta,\rho,\lambda}\delta^{\vartheta}. |  |

where the last inequality is a direct application of Proposition [5.2](https://arxiv.org/html/2511.03474v1#S5.ThmTheorem2 "Proposition 5.2 (𝛼-fractional kernels 1<𝛼<2). ‣ 5.1.1 𝛼-fractional kernels for 𝛼∈ℝ^∗₊ ‣ 5.1 𝛼-fractional kernels with 𝛼>0 ‣ 5 Applications to Fractional Stochastic Volterra Integral equations ‣ On a Stationarity Theory for Stochastic Volterra Integral Equations") and we are done. □\square