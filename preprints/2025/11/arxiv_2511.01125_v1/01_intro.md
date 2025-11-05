---
authors:
- Takashi Furuya
- Anastasis Kratsios
- Dylan Possamaï
- Bogdan Raonić
doc_id: arxiv:2511.01125v1
family_id: arxiv:2511.01125
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'One model to solve them all: 2BSDE families via neural operators'
url_abs: http://arxiv.org/abs/2511.01125v1
url_html: https://arxiv.org/html/2511.01125v1
venue: arXiv q-fin
version: 1
year: 2025
---


Takashi Furuya 111Department of Biomedical Engineering, Doshisha University, Kyōto, Japan, takashi.furuya0101@gmail.com.
  
Anastasis Kratsios 222Department of Mathematics, McMaster University, McMaster University, Hamilton, Canada, kratsiosa@mcmaster.ca.
  
Dylan Possamaï 333ETH Zürich, Department of Mathematics, Zürich, Switzerland, dylan.possamai@math.ethz.ch.
  
Bogdan Raonić 444ETH Zürich, Seminar for Applied Mathematics and ETH AI Center, Zürich, Switzerland, braonic@ethz.ch.

(November 2, 2025)

###### Abstract

We introduce a mild generative variant of the classical neural operator model, which leverages Kolmogorov–Arnold networks to solve infinite families of second-order backward stochastic differential equations (22BSDEs) on regular bounded Euclidean domains with random terminal time. Our first main result shows that the solution operator associated with a broad range of 22BSDE families is approximable by appropriate neural operator models. We then identify a structured subclass of (infinite) families of 22BSDEs whose neural operator approximation requires only a polynomial number of parameters in the reciprocal approximation rate, as opposed to the exponential requirement in general worst-case neural operator guarantees.

Key words: Neural operators, solution operators, backward stochastic differential equations, exponential approximation rates.

## 1 Introduction

Fix a positive integer d∈ℕ⋆d\in\mathbb{N}^{\star}. We work on a filtered probability space (Ω,ℱ,𝔽≔(ℱt)t∈[0,∞),ℙ)\big(\Omega,{\cal F},\mathbb{F}\coloneqq({\cal F}\_{t})\_{t\in[0,\infty)},\mathbb{P}\big) carrying a dd-dimensional (𝔽,ℙ)(\mathbb{F},\mathbb{P})–Brownian motion WW. Fix a sufficiently regular bounded open domain 𝒟⊂ℝd\mathcal{D}\subset\mathbb{R}^{d}, as well as maps μ:ℝd⟶ℝd\mu:\mathbb{R}^{d}\longrightarrow\mathbb{R}^{d}, Σ:ℝd⟶ℝd×d\Sigma:\mathbb{R}^{d}\longrightarrow\mathbb{R}^{d\times d}, and f:ℝd×ℝ×ℝd×ℝd×d⟶ℝf:\mathbb{R}^{d}\times\mathbb{R}\times\mathbb{R}^{d}\times\mathbb{R}^{d\times d}\longrightarrow\mathbb{R}, as well as an initial point x∈𝒟x\in\mathcal{D}.
We are interested in simultaneously approximately solving each 2BSDE in the (non-empty) compact infinite family ℬ⊆(X⋅,Y⋅g,f0,Z⋅g,f0,Υg,f0,Ag,f0)}(g,f0)∈𝔚\mathcal{B}\subseteq(X\_{\cdot},Y\_{\cdot}^{g,f\_{\text{$0$}}},Z\_{\cdot}^{g,f\_{\text{$0$}}},\Upsilon^{g,f\_{\text{$0$}}},A^{g,f\_{\text{$0$}}})\}\_{(g,f\_{\text{$0$}})\in\mathfrak{W}} where 𝔚\mathfrak{W} is a suitable subset of the Sobolev spaces W1,p​(∂𝒟)×W1,p​(𝒟)W^{1,p}(\partial\mathcal{D})\times W^{1,p}(\mathcal{D}). These 2BSDEs are defined through the system

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xt\displaystyle X\_{t} | =x+∫0tβ​(Xs)​ds+∫0tΣ​(Xs)​dWs,t≥0,ℙ​–a.s.,τ≔inf{t≥0:Xt∉𝒟},\displaystyle=x+\int\_{0}^{t}\beta(X\_{s})\mathrm{d}s+\int\_{0}^{t}\,\Sigma(X\_{s})\mathrm{d}W\_{s},\;t\geq 0,\;\mathbb{P}\text{\rm--a.s.},\;\tau\coloneqq\inf\big\{t\geq 0:X\_{t}\notin{\cal D}\big\}, |  | (SDE) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ytg,f0\displaystyle Y\_{t}^{g,f\_{\text{$0$}}} | =g​(Xτ)⏟Perturbation+∫t∧ττ(f​(Xs,Ysg,f0,Zsg,f0,Υsg,f0)⏟Reference generator+f0​(Xs)⏟Perturbation−12​Tr​[Σ​(Xs)​Σ⊤​(Xs)​Υsg,f0])​ds\displaystyle=\underbrace{g(X\_{\tau})}\_{\text{\tiny Perturbation}}+\int\_{t\wedge\tau}^{\tau}\bigg(\underbrace{f\big(X\_{s},Y\_{s}^{g,f\_{\text{$0$}}},Z\_{s}^{g,f\_{\text{$0$}}},\Upsilon\_{s}^{g,f\_{\text{$0$}}}\big)}\_{\text{\tiny Reference generator}}+\underbrace{f\_{0}(X\_{s})}\_{\text{\tiny Perturbation}}-\frac{1}{2}\mathrm{Tr}\big[\Sigma(X\_{s})\Sigma^{\top}(X\_{s})\Upsilon\_{s}^{g,f\_{\text{$0$}}}\big]\bigg)\mathrm{d}s |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫t∧ττZsg,f0⋅dXs,t∈[0,τ),ℙ​–a.s.,\displaystyle\quad-\int\_{t\wedge\tau}^{\tau}Z\_{s}^{g,f\_{\text{$0$}}}\cdot\mathrm{d}X\_{s},\;t\in[0,\tau),\;\mathbb{P}\text{\rm--a.s.}, |  | (FBSDE) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ztg,f0\displaystyle Z\_{t}^{g,f\_{\text{$0$}}} | =z0+∫0tAsg,f0​ds+∫0tΥsg,f0​dXs,t∈[0,τ),ℙ​–a.s..\displaystyle=z\_{0}+\int\_{0}^{t}A\_{s}^{g,f\_{\text{$0$}}}\mathrm{d}s+\int\_{0}^{t}\Upsilon\_{s}^{g,f\_{\text{$0$}}}\mathrm{d}X\_{s},\;t\in[0,\tau),\;\mathbb{P}\text{\rm--a.s.}. |  | (2BSDE) |

Using a variant (see [Section˜3.1](https://arxiv.org/html/2511.01125v1#S3.SS1 "3.1 Elliptic PDE representation of the 2BSDE system ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") below for the proof) of the results of [Cheridito, Soner, Touzi, and Victoir](https://arxiv.org/html/2511.01125v1#bib.bib16) [[16](https://arxiv.org/html/2511.01125v1#bib.bib16)] for 2BSDEs with random terminal time τ\tau, as above, for each pair (g,f0)∈𝔚(g,f\_{0})\in\mathfrak{W}, if the following elliptic PDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x,u​(x),∇u​(x),∇2u​(x))=−f0​(x),x∈𝒟​u​(x)=g​(x),x∈∂𝒟,\displaystyle f\big(x,u(x),\nabla u(x),\nabla^{2}u(x)\big)=-f\_{0}(x),\;x\in\mathcal{D}\;u(x)=g(x),\;x\in\partial\mathcal{D}, |  | (1.1) |

admits a smooth enough solution, then the 2BSDE system ([SDE](https://arxiv.org/html/2511.01125v1#S1.Ex1 "Equation SDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")), ([FBSDE](https://arxiv.org/html/2511.01125v1#S1.Ex3 "Equation FBSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")), ([2BSDE](https://arxiv.org/html/2511.01125v1#S1.Ex4 "Equation 2BSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) admits a solution of the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ytg,f0\displaystyle Y\_{t}^{g,f\_{\text{$0$}}} | =u​(Xt),Ztg,f0=∇u​(Xt),Υtg,f0=∇2u​(Xt),Atg,f0=ℒ​∇u​(Xt),t∈[0,τ),ℙ​–a.s.,\displaystyle=u(X\_{t}),\;Z\_{t}^{g,f\_{\text{$0$}}}=\nabla u(X\_{t}),\;\Upsilon\_{t}^{g,f\_{\text{$0$}}}=\nabla^{2}u(X\_{t}),\;A\_{t}^{g,f\_{\text{$0$}}}=\mathcal{L}\nabla u(X\_{t}),\;t\in[0,\tau),\;\mathbb{P}\text{\rm--a.s.}, |  | (1.2) |

where ℒ\mathcal{L} denotes the generator associated to the forward process XX (without the drift term), defined for any continuous bounded test function ff on ℝd\mathbb{R}^{d} by

|  |  |  |
| --- | --- | --- |
|  | ℒ​(f)≔12​Tr​[Σ​(x)​Σ​(x)⊤​∇2f​(x)],x∈ℝd,\mathcal{L}(f)\coloneqq\frac{1}{2}\mathrm{Tr}\big[\Sigma(x)\Sigma(x)^{\top}\nabla^{2}f(x)\big],\;x\in\mathbb{R}^{d}, |  |

see [[16](https://arxiv.org/html/2511.01125v1#bib.bib16), Equations (2.9) and (2.11)] for a similar result in the parabolic case.

Our first main result, [Theorem˜3.7](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem7 "Theorem 3.7 (Approximability of the perturbation-to-solution map). ‣ 3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), guarantees that the following solution map is approximable by a neural operator

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Γ+:W1,∞​(𝒟;ℝ)×W1,∞​(𝒟;ℝ)\displaystyle{\Gamma^{\text{$+$}}}:W^{1,\infty}(\mathcal{D};\mathbb{R})\times W^{1,\infty}(\mathcal{D};\mathbb{R}) | ⟶W1,∞​(𝒟;ℝ)\displaystyle\longrightarrow W^{1,\infty}(\mathcal{D};\mathbb{R}) |  | (1.3) |
|  | (f0,g)\displaystyle(f\_{0},g) | ⟼u\displaystyle\longmapsto u |  |

where f0f\_{0} and gg are the source and boundary data of the PDE in ([1.1](https://arxiv.org/html/2511.01125v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")), respectively; which equivalently perturb the generator and the terminal condition of the associated 2BSDEs with random terminal time τ\tau in ([FBSDE](https://arxiv.org/html/2511.01125v1#S1.Ex3 "Equation FBSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")).

Consequently, the solution map associated to the family of second-order BSDEs is approximable by our stochastic neural operator model (which extends the neural operator model of [Furuya and Kratsios](https://arxiv.org/html/2511.01125v1#bib.bib31) in [[31](https://arxiv.org/html/2511.01125v1#bib.bib31), Definition 4] from the classical BSDE setting to 22BSDEs). This result thus provides a 22BSDE analogue of neural operator approximability results, which typically follow a two-step strategy: first, establish a quantitative universal approximation theorem for general Hölder-continuous functions with the same source and target as the solution map (see *e.g.* [Lu, Jin, Pang, Zhang, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib64) [[64](https://arxiv.org/html/2511.01125v1#bib.bib64)], [Korolev](https://arxiv.org/html/2511.01125v1#bib.bib46) [[46](https://arxiv.org/html/2511.01125v1#bib.bib46)], [Galimberti, Kratsios, and Livieri](https://arxiv.org/html/2511.01125v1#bib.bib33) [[33](https://arxiv.org/html/2511.01125v1#bib.bib33)], [Yu, Becquey, Halikias, Mallory, and Townsend](https://arxiv.org/html/2511.01125v1#bib.bib96) [[96](https://arxiv.org/html/2511.01125v1#bib.bib96)], [Lanthaler, Mishra, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib56) [[56](https://arxiv.org/html/2511.01125v1#bib.bib56)], [Lu, Jin, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib63) [[63](https://arxiv.org/html/2511.01125v1#bib.bib63)], [Lanthaler, Li, and Stuart](https://arxiv.org/html/2511.01125v1#bib.bib57) [[57](https://arxiv.org/html/2511.01125v1#bib.bib57)], [Kratsios, Furuya, Benitez, Lassas, and de Hoop](https://arxiv.org/html/2511.01125v1#bib.bib50) [[50](https://arxiv.org/html/2511.01125v1#bib.bib50)], [Schwab, Stein, and Zech](https://arxiv.org/html/2511.01125v1#bib.bib85) [[85](https://arxiv.org/html/2511.01125v1#bib.bib85)] [Gödeke and Fernsel](https://arxiv.org/html/2511.01125v1#bib.bib38) [[38](https://arxiv.org/html/2511.01125v1#bib.bib38)], [Furuya, Taniguchi, and Okuda](https://arxiv.org/html/2511.01125v1#bib.bib32) [[32](https://arxiv.org/html/2511.01125v1#bib.bib32)], and [Adcock, Brugiapaglia, Dexter, and Moraga](https://arxiv.org/html/2511.01125v1#bib.bib4) [[4](https://arxiv.org/html/2511.01125v1#bib.bib4)]); second, show that the solution map is sufficiently continuous, for instance Hölder-continuous, often via a perturbation analysis, verifying in turn it is in the scope of the main theorem, see [Alvarez, Ekren, Kratsios, and Yang](https://arxiv.org/html/2511.01125v1#bib.bib5) [[5](https://arxiv.org/html/2511.01125v1#bib.bib5)], [Horvath, Kratsios, Limmer, and Yang](https://arxiv.org/html/2511.01125v1#bib.bib43) [[43](https://arxiv.org/html/2511.01125v1#bib.bib43)], [Lanthaler and Stuart](https://arxiv.org/html/2511.01125v1#bib.bib55) [[55](https://arxiv.org/html/2511.01125v1#bib.bib55)] or [Firouzi, Yang, and Kratsios](https://arxiv.org/html/2511.01125v1#bib.bib30) [[30](https://arxiv.org/html/2511.01125v1#bib.bib30)].

One may ask if favourable approximation rates are achievable if the reference generator ff is simple enough, while still of course having a meaningful structure for several applications in optimal control and mathematical finance. Indeed, in
[Theorem˜3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")
we show that this is the case when the reference generator is of the simplified form

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x,y,z,w):=−Tr​[γ​(x)​w]−div​(γ)​(x)⋅z+μ​(x)⋅z+λ​(x)​y+f~​(x,y)f(x,y,z,w):=-\mathrm{Tr}\big[\gamma(x)w\big]-\mathrm{div}(\gamma)(x)\cdot z+\mu(x)\cdot z+\lambda(x)y+\tilde{f}(x,y) |  | (1.4) |

for some smooth enough maps λ:ℝd⟶ℝ\lambda:\mathbb{R}^{d}\longrightarrow\mathbb{R}, γ:ℝd⟶ℝd×d\gamma:\mathbb{R}^{d}\longrightarrow\mathbb{R}^{d\times d}, and μ:ℝd⟶ℝd\mu:\mathbb{R}^{d}\longrightarrow\mathbb{R}^{d} and where f~:ℝd×ℝ⟶ℝ\tilde{f}:\mathbb{R}^{d}\times\mathbb{R}\longrightarrow\mathbb{R} is still sufficiently smooth. In this setting, we reduce the general fully non-linear elliptic PDE in ([1.1](https://arxiv.org/html/2511.01125v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) to the following semi-linear form

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∇⋅γ​∇u​(x)+μ​(x)⋅∇u​(x)+λ​(x)​u​(x)+f~​(x,u)=−f0​(x)⏟Perturbation,x∈𝒟,u​(x)=g​(x)⏟Perturbation,x∈∂𝒟.\displaystyle-\nabla\cdot\gamma\nabla u(x)+\mu(x)\cdot\nabla u(x)+\lambda(x)u(x)+\tilde{f}(x,u)=\underbrace{-f\_{0}(x)}\_{\text{\tiny Perturbation}},\;x\in\mathcal{D},\;u(x)=\underbrace{g(x)}\_{\text{\tiny Perturbation}},\;x\in\partial\mathcal{D}. |  | (1.5) |

[Theorem˜3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") both extends [[31](https://arxiv.org/html/2511.01125v1#bib.bib31), Theorem 1] by allowing μ\mu and λ\lambda to be non-zero and Σ\Sigma to be non-constant and positive-definite, while no longer requiring any *a priori* knowledge of the PDE itself to be hard-coded into our design of the NO.
This is because the latter authors use explicit knowledge of Green’s function associated with the PDE
−∇⋅γ​∇u​(x)+μ​(x)⋅∇u​(x)+λ​(x)​u​(x)-\nabla\cdot\gamma\nabla u(x)+\mu(x)\cdot\nabla u(x)+\lambda(x)u(x)
to show that it admits a decomposition
Φ​(x−y)+Ψ​(x,y)\Phi(x-y)+\Psi(x,y),
where Φ\Phi is a ‘difficult to approximate’ singular part and Ψ\Psi is an ‘easily approximated’ smooth part.
The convolution with the singular component Φ\Phi is then hard-coded into each of their NO architectures by leveraging the explicit closed form for Φ\Phi obtained in [[11](https://arxiv.org/html/2511.01125v1#bib.bib11)].
In contrast, in our approach no such closed-form nor *a priori* knowledge of the PDE is required in our NO build. As should be expected, these extensions also come at the cost of devising an entirely different proof strategy.

The PDE in ([1.5](https://arxiv.org/html/2511.01125v1#S1.E5 "Equation 1.5 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) can be connected back to the 22BSDE ([FBSDE](https://arxiv.org/html/2511.01125v1#S1.Ex3 "Equation FBSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) either when the divergence of γ\gamma is absorbed into μ\mu, or
in the special case where γ\gamma is divergence-free, *i.e.* div​(γ)⊤=0\mathrm{div}(\gamma)^{\top}=0, implying that ∇⋅γ∇u=Tr[γ∇u)\nabla\cdot\gamma\nabla u=\mathrm{Tr}[\gamma\nabla u). In addition, when γ\gamma is valued in the set of semi-definite matrices, and we take for Σ\Sigma any matrix square root of e​2​γe2\gamma (that is to say Σ​Σ⊤=2​γ\Sigma\Sigma^{\top}=2\gamma), then ([1.5](https://arxiv.org/html/2511.01125v1#S1.E5 "Equation 1.5 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) reduces to the more standard Hamilton–Jacobi–Bellman–type semilinear equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | f~​(x,u)+λ​(x)​u​(x)+μ​(x)⋅∇u​(x)−12​Tr​[Σ​(x)​Σ​(x)⊤​∇2u​(x)]=−f0​(x),x∈𝒟.\tilde{f}(x,u)+\lambda(x)u(x)+\mu(x)\cdot\nabla u(x)-\frac{1}{2}\,\mathrm{Tr}\big[\Sigma(x)\Sigma(x)^{\top}\nabla^{2}u(x)\big]=-f\_{0}(x),\;x\in\mathcal{D}. |  | (1.6) |

In dimension d≥2d\geq 2, there is a whole zoology of divergence-free γ\gamma; thus this special case completely subsumes the case where γ\gamma is constant, as considered in [[31](https://arxiv.org/html/2511.01125v1#bib.bib31)]. For example, when d=2d=2, if γ\gamma is positive-definite–valued then there exist a twice continuously differentiable potential φγ:ℝ2⟶ℝ\varphi\_{\gamma}:\mathbb{R}^{2}\longrightarrow\mathbb{R} (this is the so-called Airy potential) such that
γ​(x)=R⊤​(∇2φγ​(x))​R\gamma(x)=R^{\top}\big(\nabla^{2}\varphi\_{\gamma}(x)\big)R
for the symplectic matrix R≔e1​e2⊤−e2​e1⊤R\coloneqq e\_{1}e\_{2}^{\top}-e\_{2}e\_{1}^{\top} (where (e1,e2(e\_{1},e\_{2} is the canonical basis of ℝ2\mathbb{R}^{2}). A simple non-constant example of such an Airy potential φγ\varphi\_{\gamma} which additionally yields a positive-definite γ\gamma is φγ​(x,y)≔(x2+y2)2\varphi\_{\gamma}(x,y)\coloneqq(x^{2}+y^{2})^{2}.

Our first objective is, therefore, to simultaneously approximate the solution operator to general families of fully non-linear elliptic problems ([1.1](https://arxiv.org/html/2511.01125v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) and to obtain favourable rates for semi-linear special cases of the form ([1.5](https://arxiv.org/html/2511.01125v1#S1.E5 "Equation 1.5 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")). Our strategy will be to construct a neural operator (NO) model which directly approximates ([Theorem˜3.7](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem7 "Theorem 3.7 (Approximability of the perturbation-to-solution map). ‣ 3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") resp. [Theorem˜3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")) the coefficient-to-solution operator mapping any (g,f0)∈𝔚(g,f\_{0})\in\mathfrak{W} to the elliptic PDE it defines via ([1.1](https://arxiv.org/html/2511.01125v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) (resp. ([1.5](https://arxiv.org/html/2511.01125v1#S1.E5 "Equation 1.5 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators"))).
Then, using the connections between elliptic PDEs and 2BSDEs with random terminal time in ([1.2](https://arxiv.org/html/2511.01125v1#S1.E2 "Equation 1.2 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) formalised by our non-linear Feynman–Kac formula in [Section˜3.1](https://arxiv.org/html/2511.01125v1#S3.SS1 "3.1 Elliptic PDE representation of the 2BSDE system ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), we construct an adapter transforming the functions output for our NO to tuples of stochastic processes approximating the solution to the family of associated 2BSDEs, see [Theorem˜3.13](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem13 "Theorem 3.13. ‣ 3.3.2 Solutions to the family of second-order BSDEs ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators").

### 1.1 Related literature

There is a mature numerical literature on second–order BSDEs (2BSDEs), including weak approximation and time–discretisation schemes by [Possamaï and Tan](https://arxiv.org/html/2511.01125v1#bib.bib80) [[80](https://arxiv.org/html/2511.01125v1#bib.bib80)], [Ren and Tan](https://arxiv.org/html/2511.01125v1#bib.bib82) [[82](https://arxiv.org/html/2511.01125v1#bib.bib82)], [Yang, Zhao, and Zhou](https://arxiv.org/html/2511.01125v1#bib.bib94) [[94](https://arxiv.org/html/2511.01125v1#bib.bib94)], and the recent non-equidistant scheme of [Pak, Hwang, and Kim](https://arxiv.org/html/2511.01125v1#bib.bib75) [[75](https://arxiv.org/html/2511.01125v1#bib.bib75)].
Learning–based approaches have also appeared (*e.g.*, [Beck, E, and Jentzen](https://arxiv.org/html/2511.01125v1#bib.bib7) [[7](https://arxiv.org/html/2511.01125v1#bib.bib7)], [Pereira, Wang, Chen, Reed, and Theodorou](https://arxiv.org/html/2511.01125v1#bib.bib77) [[77](https://arxiv.org/html/2511.01125v1#bib.bib77)], [Duong](https://arxiv.org/html/2511.01125v1#bib.bib24) [[24](https://arxiv.org/html/2511.01125v1#bib.bib24)], [Xiao, Qiu, and Nikan](https://arxiv.org/html/2511.01125v1#bib.bib93) [[93](https://arxiv.org/html/2511.01125v1#bib.bib93)]),
but these methods are essentially *per–instance*: they must be re–run (or re–trained) whenever coefficients or boundary data change.
By contrast, we learn a *solution operator* that acts on the entire compact family of problems indexed by (g,f0)(g,f\_{0}), so a single trained model simultaneously solves all members of the family, both at the PDE and at the 2BSDE level via the PDE–(2)BSDE correspondence ([Cheridito, Soner, Touzi, and Victoir](https://arxiv.org/html/2511.01125v1#bib.bib16) [[16](https://arxiv.org/html/2511.01125v1#bib.bib16)]; see also [Pardoux](https://arxiv.org/html/2511.01125v1#bib.bib76) [[76](https://arxiv.org/html/2511.01125v1#bib.bib76)], [Soner, Touzi, and Zhang](https://arxiv.org/html/2511.01125v1#bib.bib87) [[87](https://arxiv.org/html/2511.01125v1#bib.bib87)]).

When it comes to finite–dimensional ML for non-linear PDEs, a large body of work trains a finite–dimensional network for each target PDE separately (*e.g.*,
[Nüsken and Richter](https://arxiv.org/html/2511.01125v1#bib.bib74) [[74](https://arxiv.org/html/2511.01125v1#bib.bib74)],
[Pham, Warin, and Germain](https://arxiv.org/html/2511.01125v1#bib.bib78) [[78](https://arxiv.org/html/2511.01125v1#bib.bib78)],
[Germain, Laurière, Pham, and Warin](https://arxiv.org/html/2511.01125v1#bib.bib34), [Germain, Pham, and Warin](https://arxiv.org/html/2511.01125v1#bib.bib35), [Germain, Pham, and Warin](https://arxiv.org/html/2511.01125v1#bib.bib36) [[34](https://arxiv.org/html/2511.01125v1#bib.bib34), [35](https://arxiv.org/html/2511.01125v1#bib.bib35), [36](https://arxiv.org/html/2511.01125v1#bib.bib36)],
[Lefebvre, Loeper, and Pham](https://arxiv.org/html/2511.01125v1#bib.bib58) [[58](https://arxiv.org/html/2511.01125v1#bib.bib58)],
[Zhou, Han, and Lu](https://arxiv.org/html/2511.01125v1#bib.bib97) [[97](https://arxiv.org/html/2511.01125v1#bib.bib97)],
[Hu and Laurière](https://arxiv.org/html/2511.01125v1#bib.bib44) [[44](https://arxiv.org/html/2511.01125v1#bib.bib44)],
[Nguwi, Penent, and Privault](https://arxiv.org/html/2511.01125v1#bib.bib73) [[73](https://arxiv.org/html/2511.01125v1#bib.bib73)]).
Provable *exponential* behaviour in this setting typically requires strong structure:
either linear second–order elliptic operators ([Marcati and Schwab](https://arxiv.org/html/2511.01125v1#bib.bib66) [[66](https://arxiv.org/html/2511.01125v1#bib.bib66), [67](https://arxiv.org/html/2511.01125v1#bib.bib67)]) or analyticity of the *single* target solution, so that one may invoke classical exponential approximation of analytic functions by neural networks ([Mhaskar and Micchelli](https://arxiv.org/html/2511.01125v1#bib.bib69) [[69](https://arxiv.org/html/2511.01125v1#bib.bib69)], [Mhaskar](https://arxiv.org/html/2511.01125v1#bib.bib68) [[68](https://arxiv.org/html/2511.01125v1#bib.bib68)], [E and Wang](https://arxiv.org/html/2511.01125v1#bib.bib25) [[25](https://arxiv.org/html/2511.01125v1#bib.bib25)]).

On the other hand, neural operators (NOs) learn the infinite–dimensional coefficient–to–solution map and hence *simultaneously* solve all PDEs in a parametric class with a single model; see the early universality observation of [Chen and Chen](https://arxiv.org/html/2511.01125v1#bib.bib15) [[15](https://arxiv.org/html/2511.01125v1#bib.bib15)], the DeepONet/FNO line ([Lu, Jin, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib63) [[63](https://arxiv.org/html/2511.01125v1#bib.bib63)], [Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, and Anandkumar](https://arxiv.org/html/2511.01125v1#bib.bib47) [[47](https://arxiv.org/html/2511.01125v1#bib.bib47)]), the CNO universality [Raonić, Molinaro, de Ryck, Rohner, Bartolucci, Alaifari, Mishra, and de Bézenac](https://arxiv.org/html/2511.01125v1#bib.bib81) [[81](https://arxiv.org/html/2511.01125v1#bib.bib81)], and a large set of abstract guarantees in Banach/Besov/Sobolev and non–linear metric settings
([Yu, Becquey, Halikias, Mallory, and Townsend](https://arxiv.org/html/2511.01125v1#bib.bib96) [[96](https://arxiv.org/html/2511.01125v1#bib.bib96)],
[Lu, Jin, Pang, Zhang, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib64) [[64](https://arxiv.org/html/2511.01125v1#bib.bib64)],
[Lanthaler, Mishra, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib56) [[56](https://arxiv.org/html/2511.01125v1#bib.bib56)],
[Adcock, Brugiapaglia, Dexter, and Moraga](https://arxiv.org/html/2511.01125v1#bib.bib2) [[2](https://arxiv.org/html/2511.01125v1#bib.bib2)],
[Korolev](https://arxiv.org/html/2511.01125v1#bib.bib46) [[46](https://arxiv.org/html/2511.01125v1#bib.bib46)],
[Cuchiero, Schmocker, and Teichmann](https://arxiv.org/html/2511.01125v1#bib.bib17) [[17](https://arxiv.org/html/2511.01125v1#bib.bib17)],
[Neufeld and Schmocker](https://arxiv.org/html/2511.01125v1#bib.bib72) [[72](https://arxiv.org/html/2511.01125v1#bib.bib72)],
[Kratsios, Furuya, Benitez, Lassas, and de Hoop](https://arxiv.org/html/2511.01125v1#bib.bib50) [[50](https://arxiv.org/html/2511.01125v1#bib.bib50)],
[Adcock, Brugiapaglia, Dexter, and Moraga](https://arxiv.org/html/2511.01125v1#bib.bib4) [[4](https://arxiv.org/html/2511.01125v1#bib.bib4)],
[Gödeke and Fernsel](https://arxiv.org/html/2511.01125v1#bib.bib38) [[38](https://arxiv.org/html/2511.01125v1#bib.bib38)],
[Lanthaler and Stuart](https://arxiv.org/html/2511.01125v1#bib.bib55) [[55](https://arxiv.org/html/2511.01125v1#bib.bib55)],
[Schwab, Stein, and Zech](https://arxiv.org/html/2511.01125v1#bib.bib85) [[85](https://arxiv.org/html/2511.01125v1#bib.bib85)],
[de Hoop, Lassas, and Wong](https://arxiv.org/html/2511.01125v1#bib.bib20) [[20](https://arxiv.org/html/2511.01125v1#bib.bib20)],
[Furuya, Taniguchi, and Okuda](https://arxiv.org/html/2511.01125v1#bib.bib32) [[32](https://arxiv.org/html/2511.01125v1#bib.bib32)],
[Kratsios, Schmocker, and Zimmermann](https://arxiv.org/html/2511.01125v1#bib.bib52) [[52](https://arxiv.org/html/2511.01125v1#bib.bib52)],
[Acciaio, Kratsios, and Pammer](https://arxiv.org/html/2511.01125v1#bib.bib1) [[1](https://arxiv.org/html/2511.01125v1#bib.bib1)],
[Kratsios, Liu, Lassas, de Hoop, and Dokmanic](https://arxiv.org/html/2511.01125v1#bib.bib49) [[49](https://arxiv.org/html/2511.01125v1#bib.bib49)]).
Within this line, *exponential* (sometimes ‘exponential–in–depth’) expression rates are known for holomorphic operator classes ([Adcock, Dexter, and Moraga Scheuermann](https://arxiv.org/html/2511.01125v1#bib.bib3) [[3](https://arxiv.org/html/2511.01125v1#bib.bib3)]), for certain linear elliptic PDEs (including polytopal domains) ([Marcati and Schwab](https://arxiv.org/html/2511.01125v1#bib.bib66) [[66](https://arxiv.org/html/2511.01125v1#bib.bib66), [67](https://arxiv.org/html/2511.01125v1#bib.bib67)]), and for specific semilinear elliptic equations on smooth domains ([Furuya and Kratsios](https://arxiv.org/html/2511.01125v1#bib.bib31) [[31](https://arxiv.org/html/2511.01125v1#bib.bib31)]).
Other exponential statements rely either on super–expressive activations with effectively infinite pseudo–dimension ([Shen, Yang, and Zhang](https://arxiv.org/html/2511.01125v1#bib.bib86) [[86](https://arxiv.org/html/2511.01125v1#bib.bib86)], [Pollard](https://arxiv.org/html/2511.01125v1#bib.bib79) [[79](https://arxiv.org/html/2511.01125v1#bib.bib79)], [Alvarez, Ekren, Kratsios, and Yang](https://arxiv.org/html/2511.01125v1#bib.bib5) [[5](https://arxiv.org/html/2511.01125v1#bib.bib5)]) or on implicit/equilibrium–layer constructions exploiting convex variational structure ([Kratsios, Neufeld, and Schmocker](https://arxiv.org/html/2511.01125v1#bib.bib51) [[51](https://arxiv.org/html/2511.01125v1#bib.bib51)]).

Our contribution in this landscape is that we design a NO that *simultaneously* (i)(i) approximates the solution operator of a broad class of second–order elliptic PDEs/2BSDEs and (i​i)(ii) retains *exponential–in–depth* rates in a substantially more general semi-linear regime than in the closest prior work.
Concretely

1. (i)(i)

   *family–level learning.*
   We approximate the coefficient–to–solution map Γ+\Gamma^{\text{$+$}} on a compact infinite family indexed by (f0,g)(f\_{0},g), hence a single training phase serves the whole family (PDEs and the associated 2BSDEs).
   For fully non–linear elliptic equations we obtain general operator–level approximability (algebraic rates) by combining quantitative NO universality on Besov/Sobolev scales ([Yu, Becquey, Halikias, Mallory, and Townsend](https://arxiv.org/html/2511.01125v1#bib.bib96) [[96](https://arxiv.org/html/2511.01125v1#bib.bib96)], [Lu, Jin, Pang, Zhang, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib64) [[64](https://arxiv.org/html/2511.01125v1#bib.bib64)], [Lanthaler, Mishra, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib56) [[56](https://arxiv.org/html/2511.01125v1#bib.bib56)], [Adcock, Brugiapaglia, Dexter, and Moraga](https://arxiv.org/html/2511.01125v1#bib.bib2) [[2](https://arxiv.org/html/2511.01125v1#bib.bib2)], [Korolev](https://arxiv.org/html/2511.01125v1#bib.bib46) [[46](https://arxiv.org/html/2511.01125v1#bib.bib46)], [Galimberti, Kratsios, and Livieri](https://arxiv.org/html/2511.01125v1#bib.bib33) [[33](https://arxiv.org/html/2511.01125v1#bib.bib33)]) with stability of the solution map (Krylov–type assumptions; cf. [Krylov](https://arxiv.org/html/2511.01125v1#bib.bib54) [[54](https://arxiv.org/html/2511.01125v1#bib.bib54)]).
2. (i​i)(ii)

   *Exponential rates for semi-linear equations under *general* forward dynamics.*
   In the semi-linear case

   |  |  |  |
   | --- | --- | --- |
   |  | −∇⋅γ​(x)​∇u+μ​(x)⋅∇u+λ​(x)​u+f~​(x,u)=−f0​(x),u|∂𝒟=g,-\nabla\!\cdot\!\gamma(x)\nabla u+\mu(x)\!\cdot\!\nabla u+\lambda(x)u+\tilde{f}(x,u)=-f\_{0}(x),\;u|\_{\partial{\cal D}}=g, |  |

   with smooth, uniformly elliptic γ\gamma and smooth μ\mu, λ\lambda, we implement the classical fixed–point map by a non-local NO layer built from (approximated) Green kernels; existence/regularity of Green functions for variable–coefficient operators is standard ([Kim and Sakellaris](https://arxiv.org/html/2511.01125v1#bib.bib45) [[45](https://arxiv.org/html/2511.01125v1#bib.bib45)]).
   This yields accuracy ε\varepsilon with *logarithmic* depth L=O​(log⁡(1/ε))L=O(\log(1/\varepsilon)), *constant* width, and a finite non-local rank that scales polynomially in 1/ε1/\varepsilon.
   Compared to [Furuya and Kratsios](https://arxiv.org/html/2511.01125v1#bib.bib31) [[31](https://arxiv.org/html/2511.01125v1#bib.bib31)], which hard–codes the singular part of the Green’s kernel and effectively assumes a driftless, constant–diffusion forward (so that the singular Φ\Phi is known in closed form), our construction does *not* require a closed–form kernel split and therefore covers far more general, state–dependent Itô diffusions in the forward process and variable–coefficient elliptic operators, while preserving exponential depth–rates.
3. (i​i​i)(iii)

   *From PDE to (2)(2)BSDE at the operator level.*
   Because each 2BSDE in the family admits the PDE representation, our NO for the elliptic map transfers directly to a NO for the (Y,Z,Υ,A)(Y,Z,\Upsilon,A)–processes associated with the *entire* 2BSDE family.

Building upon the finite-dimensional lower bounds of [Yarotsky](https://arxiv.org/html/2511.01125v1#bib.bib95) [[95](https://arxiv.org/html/2511.01125v1#bib.bib95)] , it was recently shown in [Lanthaler and Stuart](https://arxiv.org/html/2511.01125v1#bib.bib55) [[55](https://arxiv.org/html/2511.01125v1#bib.bib55)] that arbitrary continuous—or even several times continuously Fréchet differentiable—non-linear operators between Sobolev spaces cannot be uniformly approximated on compact sets by NOs without requiring an exponential number of trainable parameters in the reciprocal approximation error.
Consequently, without additional structure beyond simple smoothness, there are insurmountable obstructions to operator learning. Thus, even if one could establish Hölder-continuity of the coefficient-to-solution operator in the fully non-linear setting (*e.g.* using results of [Taylor](https://arxiv.org/html/2511.01125v1#bib.bib88) [[88](https://arxiv.org/html/2511.01125v1#bib.bib88)], which we do show in [Section˜A.4](https://arxiv.org/html/2511.01125v1#A1.SS4 "A.4 Stability estimate of general solution operator ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) the solution operator would still not be regular enough to permit meaningful approximation rates. In such cases, any quantitative result is practically no more meaningful than an existential statement on the approximability of the coefficient-to-solution operator (see [Theorem˜3.7](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem7 "Theorem 3.7 (Approximability of the perturbation-to-solution map). ‣ 3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")), akin to the qualitative (rate-free) universal abstract approximation results of [Chen and Chen](https://arxiv.org/html/2511.01125v1#bib.bib14) [[14](https://arxiv.org/html/2511.01125v1#bib.bib14)], [Benth, Detering, and Galimberti](https://arxiv.org/html/2511.01125v1#bib.bib8) [[8](https://arxiv.org/html/2511.01125v1#bib.bib8)], or [Bilokopytov and Xanthos](https://arxiv.org/html/2511.01125v1#bib.bib9) [[9](https://arxiv.org/html/2511.01125v1#bib.bib9)] for other NO architectures.

When it comes to the closest exponential–rate results available in the literature, relative to linear/holomorphic NO rates ([Marcati and Schwab](https://arxiv.org/html/2511.01125v1#bib.bib66) [[66](https://arxiv.org/html/2511.01125v1#bib.bib66), [67](https://arxiv.org/html/2511.01125v1#bib.bib67)], [Adcock, Dexter, and Moraga Scheuermann](https://arxiv.org/html/2511.01125v1#bib.bib3) [[3](https://arxiv.org/html/2511.01125v1#bib.bib3)]), we require neither analyticity nor specialised domains; and unlike exponential claims relying on super–expressive activations or implicit/equilibrium layers ([Shen, Yang, and Zhang](https://arxiv.org/html/2511.01125v1#bib.bib86) [[86](https://arxiv.org/html/2511.01125v1#bib.bib86)], [Pollard](https://arxiv.org/html/2511.01125v1#bib.bib79) [[79](https://arxiv.org/html/2511.01125v1#bib.bib79)], [Alvarez, Ekren, Kratsios, and Yang](https://arxiv.org/html/2511.01125v1#bib.bib5) [[5](https://arxiv.org/html/2511.01125v1#bib.bib5)], [Kratsios, Neufeld, and Schmocker](https://arxiv.org/html/2511.01125v1#bib.bib51) [[51](https://arxiv.org/html/2511.01125v1#bib.bib51)]), our architecture maintains finite capacity per layer with explicit depth/width/rank scaling.
Crucially, compared to [Furuya and Kratsios](https://arxiv.org/html/2511.01125v1#bib.bib31) [[31](https://arxiv.org/html/2511.01125v1#bib.bib31)], our exponential regime permits markedly *more general* forward dynamics and variable–coefficient elliptic operators, because the Green–kernel is learned/approximated rather than injected in closed form.

## 2 Preliminaries

### 2.1 Notation

Let p∈(1,∞)p\in(1,\infty).
We denote by p′∈(1,∞)p^{\prime}\in(1,\infty) the conjugate of pp such that 1/p+1/p′=11/p+1/p^{\prime}=1. We let ℕ\mathbb{N} be set of non-negative integers, ℕ⋆\mathbb{N}^{\star} the set of positive integers, and ℤ\mathbb{Z} the set of all negative and non-negative integers. We henceforth fix an ambient dimension555In [[31](https://arxiv.org/html/2511.01125v1#bib.bib31)] an explicit expression for the singular part of the Green’s function associated to the stopped forward process’s induced elliptic PDE was required, which additionally constrained d≥3d\geq 3 there, but not herein. d∈ℕ⋆d\in\mathbb{N}^{\star}; and let 𝕊d+\mathbb{S}\_{d}^{\text{$+$}} denote the set of d×dd\times d (real) positive-definite matrices. Recall that, every symmetric positive definite matrix A∈𝕊d+A\in\mathbb{S}\_{d}^{+} has a unique well-defined square-root given by A≔log⁡(exp⁡(A)/2)\sqrt{A}\coloneqq\log(\exp(A)/2) where exp\exp is the matrix exponential and log\log is its (unique) inverse on 𝕊d+\mathbb{S}\_{d}^{\text{$+$}}, see *e.g*. [Arabpour, Armstrong, Galimberti, Kratsios, and Livieri](https://arxiv.org/html/2511.01125v1#bib.bib6) [[6](https://arxiv.org/html/2511.01125v1#bib.bib6), Lemma C.5]. For any d∈ℕ⋆d\in\mathbb{N}^{\star} denote the Fröbenius norm of any d×dd\times d matrix AA by ‖A‖F\|A\|\_{\text{$F$}}. Given any metric space (𝒳,ρ)(\mathcal{X},\rho), any x∈𝒳x\in\mathcal{X}, and any radius r≥0r\geq 0, we define the open ball B(𝒳,ρ)​(x,r)≔{u∈𝒳:ρ​(x,u)<r}B\_{(\mathcal{X},\rho)}(x,r)\coloneqq\{u\in\mathcal{X}:\rho(x,u)<r\}. Given any two vector spaces VV and WW, and any x∈Vx\in V and y∈Wy\in W, we write x⊕y≔(x,y)=V×Wx\oplus y\coloneqq(x,y)=V\times W.

For any p≥1p\geq 1, we let ℓp​(ℤ)\ell^{p}(\mathbb{Z}) be the set of real-valued sequences (un)n∈ℤ(u\_{n})\_{n\in\mathbb{Z}} indexed by ℤ\mathbb{Z} such that

|  |  |  |
| --- | --- | --- |
|  | ∑n∈ℤ|un|p<∞.\sum\_{n\in\mathbb{Z}}|u\_{n}|^{p}<\infty. |  |

We also let 𝕃p​(ℝ)\mathbb{L}^{p}(\mathbb{R}) be the set of pp-integrable Lebesgue-measurable functions on ℝ\mathbb{R}.

For any I∈ℕI\in\mathbb{N}, we use CI​(ℝ)C^{I}(\mathbb{R}) to denote the vector space of real-valued at-least II-times continuously differentiable functions on ℝ\mathbb{R}, and CcI​(ℝ)C\_{c}^{I}(\mathbb{R}) for the subset thereof consisting of those compactly supported functions therein.
For any (s,d,D)∈(ℕ⋆)3(s,d,D)\in(\mathbb{N}^{\star})^{3}, we write Cs​(𝒟,ℝD)C^{s}(\mathcal{D},\mathbb{R}^{D}) (resp. C∞​(𝒟,ℝD)C^{\infty}(\mathcal{D},\mathbb{R}^{D})) for set of functions from ℝd\mathbb{R}^{d} to ℝD\mathbb{R}^{D} which are at-least ss-times (resp. smooth) continuously differentiable when restricted to 𝒟\mathcal{D}. We refer the reader to Appendix [A.2.3](https://arxiv.org/html/2511.01125v1#A1.SS2.SSS3 "A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") for wavelet-centric definitions of Besov, and thus Sobolev, spaces.

Throughout this paper, (Ω,ℱ,𝔽≔(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},\mathbb{F}\coloneqq(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) will denote a filtered probability space satisfying the usual conditions.
For any T>0T>0 we use ℋT2\mathcal{H}\_{T}^{2} to denote the class of square-integrable predictable processes X:[0,T]×Ω⟶ℝX:[0,T]\times\Omega\longrightarrow\mathbb{R}.

### 2.2 Deep learning

Neural operators (NOs) extend deep learning from finite-dimensional vector spaces to infinite-dimensional Banach spaces, with standard NOs specialising in function-to-function mappings. Broadly speaking, there are three types of NO builds between function spaces: the Fourier neural operator–type builds (FNO), which iteratively use finitely parametrised integral-kernel affine transformations between their non-linearities; DeepONet-type architectures (see [Lu, Jin, and Karniadakis](https://arxiv.org/html/2511.01125v1#bib.bib63) [[63](https://arxiv.org/html/2511.01125v1#bib.bib63)]) which learn to adaptively regress against learnable bases; and encoder–-processor–-decoder-type models, such as PCA–Net (see [Chan, Jia, Gao, Lu, Zeng, and Ma](https://arxiv.org/html/2511.01125v1#bib.bib12) [[12](https://arxiv.org/html/2511.01125v1#bib.bib12)]) which project infinite-dimensional data using a Schauder basis before processing it via a standard finite-dimensional neural network, and then reassembles finite-dimensional basis functions using the network’s outputs as coefficients.

The first and last of these models tend to be more numerically stable, the middle construction can exhibit advantageous approximation rates, and the third model is more readily generalisable to non–-function space settings (see *e.g.* [Galimberti, Kratsios, and Livieri](https://arxiv.org/html/2511.01125v1#bib.bib33) [[33](https://arxiv.org/html/2511.01125v1#bib.bib33)])
by directly lifting the approximation guarantees for classical neural networks (see e.g. [Yarotsky](https://arxiv.org/html/2511.01125v1#bib.bib95), [Bolcskei, Grohs, Kutyniok, and Petersen](https://arxiv.org/html/2511.01125v1#bib.bib10), [DeVore, Hanin, and Petrova](https://arxiv.org/html/2511.01125v1#bib.bib23), [Gribonval, Kutyniok, Nielsen, and Voigtlaender](https://arxiv.org/html/2511.01125v1#bib.bib39), [Kratsios and Zamanlooy](https://arxiv.org/html/2511.01125v1#bib.bib53), [Shen, Yang, and Zhang](https://arxiv.org/html/2511.01125v1#bib.bib86), [Hong and Kratsios](https://arxiv.org/html/2511.01125v1#bib.bib41), [Schneider, Ullrich, and Vybiral](https://arxiv.org/html/2511.01125v1#bib.bib84)) to infinite dimensions. Our neural-operator build combines the best of the first two models using a two-branch structure: the top branch of an FNO-type, the bottom branch inspired by DeepONets, with coefficients shared between layers. Moreover, we map into non–-function space targets when applying our deep-learning model in the 2BSDE setting by transforming its function space–valued outputs into processes via a ‘Feynman–-Kac adapter’, that is to say a custom non-trainable readout layer encoding our nonlinear Feynman-–Kac representation ([Section˜3.1](https://arxiv.org/html/2511.01125v1#S3.SS1 "3.1 Elliptic PDE representation of the 2BSDE system ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")). Finally, we allow the non-linearities injecting structure at each layer of our NO to be adaptive rather than fixed, as in classical NO builds, thereby maximizing their flexibility, for instance granting them the ability to exactly perform multiplication, a property not shared by classical piecewise-linear ReLU activation functions.

#### 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs)

The key idea behind Kolmogorov–Arnold networks (KANs) is to make the activation function itself trainable. In KANs, one typically focuses on the spline part of the following definition [Liu, Wang, Vaidya, Ruehle, Halverson, Soljacic, Hou, and Tegmark](https://arxiv.org/html/2511.01125v1#bib.bib62) [[62](https://arxiv.org/html/2511.01125v1#bib.bib62)], with the role of the remaining part of the activation function being an afterthought, normally taken to some standard non-linearity such as the Swish or Sigmoid functions. In this paper, we explicitly exploit both parts of KANs activation functions, and as such, we add some basic structural requirements to the ‘non-spline’ part of the activation function (below in ([2.1](https://arxiv.org/html/2511.01125v1#S2.E1 "Equation 2.1 ‣ 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"))) which serves a pointed role in our approximation theory in connection with the multi-resolution analysis (MRA); see *e.g*. [Mallat](https://arxiv.org/html/2511.01125v1#bib.bib65) [[65](https://arxiv.org/html/2511.01125v1#bib.bib65)].

Specifically, the activation σβ:I:ℝ⟶ℝ\sigma\_{\beta:\text{$I$}}:\mathbb{R}\longrightarrow\mathbb{R} maps any x∈ℝx\in\mathbb{R} to a mixture of spline basis functions of varying degrees

|  |  |  |  |
| --- | --- | --- | --- |
|  | σβ:I​(x)≔β−1​σS​(x)+β0​σW​(x)⏟Spectral structure+∑i=1Iβi​𝒩i​(x)⏟Local structure\sigma\_{\beta:\text{$I$}}(x)\coloneqq\underbrace{\beta\_{\text{$-$}1}\sigma\_{\text{$S$}}(x)+\beta\_{0}\sigma\_{\text{$W$}}(x)}\_{\text{\tiny Spectral structure}}+\underbrace{\sum\_{i=1}^{\text{$I$}}\beta\_{i}\mathcal{N}\_{i}(x)}\_{\text{\tiny Local structure}} |  | (2.1) |

where I∈ℕI\in\mathbb{N}, β=(β−1,β0,⋅,βI)⊤∈ℝI+2\beta=(\beta\_{\text{$-$}1},\beta\_{0},\cdot,\beta\_{\text{$I$}})^{\top}\in\mathbb{R}^{\text{$I$}+2} is a trainable vector of coefficients, and where for i∈{1,…,I}i\in\{1,\dots,I\}, 𝒩i:ℝ⟶ℝ\mathcal{N}\_{i}:\mathbb{R}\longrightarrow\mathbb{R} are the cardinal B-splines which, following [Mhaskar and Micchelli](https://arxiv.org/html/2511.01125v1#bib.bib70) [[70](https://arxiv.org/html/2511.01125v1#bib.bib70), Equation (4.28)], can be defined by 𝒩0​(x)≔𝟏[0,1)\mathcal{N}\_{0}(x)\coloneqq\mathbf{1}\_{[0,1)} and for any i∈ℕ⋆i\in\mathbb{N}^{\star}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒩I​(x)≔∑j=0I+​1(−1)j​(I+1j)I!​ReLU​(x−j)I,x∈ℝ.\mathcal{N}\_{I}(x)\coloneqq\sum\_{j=0}^{\text{$I$}\text{$+$}1}\frac{(-1)^{j}\binom{I+1}{j}}{I!}\mathrm{ReLU}(x-j)^{I},\;x\in\mathbb{R}. |  | (2.2) |

Furthermore, σS:ℝ⟶ℝ\sigma\_{\text{$S$}}:\mathbb{R}\longrightarrow\mathbb{R} as well as σW:ℝ⟶ℝ\sigma\_{\text{$W$}}:\mathbb{R}\longrightarrow\mathbb{R} and satisfy the spectral properties in [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators") below. However, before turning to the properties, we elucidate the first few wavelets in [Figure˜1](https://arxiv.org/html/2511.01125v1#S2.F1 "In 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators").

![Refer to caption](x1.png)


Figure 1: The cardinal BB-splines of orders I=0,1I=0,1, and 22.

###### Assumption 2.1 (Daubechies properties of order II).

Fix I∈ℕI\in\mathbb{N}. The respective ‘`scale’ and ‘`wavelet’ activation function σS\sigma\_{\text{$S$}}
and σW{\sigma\_{\text{$W$}}} both belong to CcI​(ℝ)C^{I}\_{c}(\mathbb{R}) if I>0I>0 ((resp. L2​(ℝ)L^{2}(\mathbb{R}) when I=0I=0 with compact essential support)) and satisfy the refinement equation of [Daubechies](https://arxiv.org/html/2511.01125v1#bib.bib18) [[18](https://arxiv.org/html/2511.01125v1#bib.bib18), Equation (3.47)], that is to say that there is a sequence of *low-pass filters* (hk)k∈ℤ∈ℓ2​(ℤ)(h\_{k})\_{k\in\mathbb{Z}}\in\ell^{2}(\mathbb{Z}) summing to 2\sqrt{2}, satisfying the *orthogonality condition*666See [[18](https://arxiv.org/html/2511.01125v1#bib.bib18), Equation (3.18)]

|  |  |  |
| --- | --- | --- |
|  | ∑k∈ℤhk−2​i​hk−2​j=𝟏{i=j},∀(i,j)∈ℤ2,\sum\_{k\in\mathbb{Z}}h\_{k\text{$-$}2i}h\_{k\text{$-$}2j}=\mathbf{1}\_{\{i=j\}},\;\forall(i,j)\in\mathbb{Z}^{2}, |  |

and such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σS​(x)\displaystyle\sigma\_{\text{$S$}}(x) | =2​∑k∈ℤhk​σS​(2​x−k),x∈ℝ,\displaystyle=\sqrt{2}\sum\_{k\in\mathbb{Z}}h\_{k}\sigma\_{\text{$S$}}(2x-k),\;x\in\mathbb{R}, |  | (2.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σW​(x)\displaystyle\sigma\_{\text{$W$}}(x) | =2​∑k∈ℤ(−1)k​h1−k​σS​(2​x−k),x∈ℝ.\displaystyle=\sqrt{2}\sum\_{k\in\mathbb{Z}}(-1)^{k}h\_{1\text{$-$}k}\sigma\_{\text{$S$}}(2x-k),\;x\in\mathbb{R}. |  | (2.4) |

The existence of such activation functions (called Daubechies father and mother wavelets respectively), for arbitrary II, is guaranteed by [Triebel](https://arxiv.org/html/2511.01125v1#bib.bib89) [[89](https://arxiv.org/html/2511.01125v1#bib.bib89), Theorem 1.61.(i​i)(ii)], while algorithmic constructions can be found in [Daubechies](https://arxiv.org/html/2511.01125v1#bib.bib19) [[19](https://arxiv.org/html/2511.01125v1#bib.bib19), Chapter 6.4], and are standard in modern signal processing. Nevertheless, in the very low regularity regime where I=0I=0, the Haar system and the indicator function is a transparent example where [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators") holds.

###### Example 2.2 (Haar wavelets and indicator function for discontinuous regularity).

If I=0I=0 then, the indicator function of the unit interval σS≔𝟏[0,1)\sigma\_{\text{$S$}}\coloneqq\mathbf{1}\_{[0,1)} and the Haar wavelet σM≔𝟏[0,1/2)−𝟏[1/2,1)\sigma\_{M}\coloneqq\mathbf{1}\_{[0,1/2)}-\mathbf{1}\_{[1/2,1)} satisfy [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators") with h0=h1=12h\_{0}=h\_{1}=\frac{1}{\sqrt{2}} and hk=0h\_{k}=0 whenever |k|≥2|k|\geq 2. Thus, σM\sigma\_{M} and σS\sigma\_{S} belong to L2​(ℝ)L^{2}(\mathbb{R}) as expected since I=0I=0.

In a KAN, this activation operates component-wise, with parameters tailored to each neuron. That is, for any integer kk, any x∈ℝkx\in\mathbb{R}^{k}, and β≔(β1,…,βk)∈ℝ(I+2)×k\mathbf{\beta}\coloneqq(\beta\_{1},\dots,\beta\_{k})\in\mathbb{R}^{(I+2)\times k}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | σβ:I∙:ℝk\displaystyle\sigma\_{\mathbf{\beta}:\text{$I$}}\bullet:\mathbb{R}^{k} | ⟶ℝk\displaystyle\longrightarrow\mathbb{R}^{k} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x=(x1,…,xk)⊤\displaystyle x=(x\_{1},\dots,x\_{k})^{\top} | ⟼(σβ1:I​(x1),…,σβk:I​(xk))⊤.\displaystyle\longmapsto\big(\sigma\_{\beta\_{\text{$1$}}:\text{$I$}}(x\_{1}),\dots,\sigma\_{\beta\_{\text{$k$}}:\text{$I$}}(x\_{k})\big)^{\top}. |  | (2.5) |

We now introduce the core idea of *residual* KAN networks. These networks incorporate an additional *residual connection*, ensuring that signal is preserved during activation. Residual connections, standard in modern deep learning architectures, help stabilise training by preserving gradient flow and regularising the loss landscape, see [Riedi, Balestriero, and Baraniuk](https://arxiv.org/html/2511.01125v1#bib.bib83) [[83](https://arxiv.org/html/2511.01125v1#bib.bib83)]. They also mitigate vanishing gradients that can be caused by normalisation layers. Following [Acciaio, Kratsios, and Pammer](https://arxiv.org/html/2511.01125v1#bib.bib1) [[1](https://arxiv.org/html/2511.01125v1#bib.bib1)], we allow for flexible use of these residual paths, potentially modulated by a trainable gating mechanism.

More precisely, we fix positive integers doutd\_{\mathrm{out}} and dind\_{\mathrm{in}}, matrices (A,G)∈ℝdout×din×ℝdout×din(A,G)\in\mathbb{R}^{d\_{\text{$\rm out$}}\times d\_{\text{$\rm in$}}}\times\mathbb{R}^{d\_{\text{$\rm out$}}\times d\_{\text{$\rm in$}}}, with GG being diagonal (*i.e.* Gi,j=0G\_{i,j}=0 for (i,j)∈{1,…,dout}×{1,…,din}(i,j)\in\{1,\dots,d\_{\rm out}\}\times\{1,\dots,d\_{\rm in}\} with i≠ji\neq j), as well as b∈ℝdoutb\in\mathbb{R}^{d\_{\text{$\mathrm{out}$}}}, and β∈ℝ(I+2)×dout\beta\in\mathbb{R}^{({I}\text{$+$}2)\times d\_{\text{$\mathrm{out}$}}}, a matrix of trainable coefficients. We then define for x∈ℝdinx\in\mathbb{R}^{d\_{\text{$\rm in$}}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ(x|A,b,β,G:I)≔σβ:I∙(A​x+b)⏟KAN layer+G​x⏟Residual connection\mathcal{L}(x|A,b,\beta,G:I)\coloneqq\underbrace{\sigma\_{\mathbf{\beta}:\text{$I$}}\bullet(Ax+b)}\_{\text{\tiny KAN layer}}+\underbrace{Gx}\_{\text{\tiny Residual connection}} |  | (2.6) |

Although compositions of such KAN layers define valid functions, these may lack higher-order smoothness—an issue for applications such as PDE solving that require high regularity. There are two ways to address this: (1) enforce that βi=0\beta\_{i}=0 for small ii, or (2) apply a smoothing layer at the output. We adopt the first strategy to ensure that the functions realised by our *smoothed residual KANs* are infinitely differentiable.

###### Definition 2.3 (Residual KANs (Res–KANs)).

Let DD and II be positive integers, and let α>0\alpha>0. A residual Kolmogorov–Arnold network ((Res–KAN)) is a function f^:ℝd⟶ℝD\widehat{f}:\mathbb{R}^{d}\longrightarrow\mathbb{R}^{D} with
representation, for some L∈ℕ⋆L\in\mathbb{N}^{\star}

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^=A(L)​f(L)+b(L),\widehat{f}=A^{(L)}f^{(L)}+b^{(L)}, |  | (2.7) |

with

|  |  |  |
| --- | --- | --- |
|  | f(0)(x)=x,x∈ℝd,f(ℓ)=ℒ(f(ℓ−1)|A(ℓ),b(ℓ),β(ℓ),G(ℓ):I),ℓ∈{1,…,L},f^{(0)}(x)=x,\;x\in\mathbb{R}^{d},\;f^{(\ell)}=\mathcal{L}\big(f^{(\ell-1)}|A^{(\ell)},b^{(\ell)},\beta^{(\ell)},G^{(\ell)}:I\big),\;\ell\in\{1,\dots,L\}, |  |

where, for ℓ∈{1,…,L}\ell\in\{1,\dots,L\}, A(ℓ)A^{(\ell)} and G(ℓ)G^{(\ell)} are dℓ+1×dℓd\_{\ell+1}\times d\_{\ell} matrices with G(ℓ)G^{(\ell)} diagonal, β(ℓ)\beta^{(\ell)} is a (I+2)×dℓ+1(I+2)\times d\_{{\ell}{+}{1}} matrix, b∈ℝdℓ+1b\in\mathbb{R}^{d\_{\text{$\ell$}\text{$+$}\text{$1$}}}, for given positive integers (d0,…,dL+1)(d\_{0},\dots,d\_{L+1}) satisfying d0=dd\_{0}=d and dL+1=Dd\_{L+1}=D. In addition, for any ℓ∈{1,…,L}\ell\in\{1,\dots,L\}, β(ℓ)\beta^{(\ell)} satisfies the *sparsity* pattern ensuring smoothness777The ⌈α⌉\lceil\alpha\rceil-time continuous differentiability of f^\hat{f} follows from that of B-splines (see [DeVore and Sharpley](https://arxiv.org/html/2511.01125v1#bib.bib22) [[22](https://arxiv.org/html/2511.01125v1#bib.bib22)]), and the chain rule.

|  |  |  |  |
| --- | --- | --- | --- |
|  | βi,j(ℓ)=0,i<⌈α⌉​and,j∈{1,…,dℓ+1}.\beta^{(\ell)}\_{i,j}=0,\;i<\lceil\alpha\rceil{\;\mbox{\rm and},\;j\in\{1,\dots,d\_{\ell+1}\}}. |  | (2.8) |

We denote the class of all Res–KANs with LL hidden layers, width W≔maxℓ∈{1,…,L+1}⁡dℓW\coloneqq\max\_{\ell\in\{1,\dots,L+1\}}d\_{\ell}, adaptivity parameter II, and smoothness parameter α\alpha, by Res−−KANL,WI,α⁡(ℝd,ℝD)\operatorname{Res--KAN}\_{\text{$L$},\text{$W$}}^{\text{$I$},\alpha}(\mathbb{R}^{d},\mathbb{R}^{D}).

#### 2.2.2 Neural operator architectures

We recall that we have fixed a constant 1<p<∞1<p<\infty and 𝒟⊂ℝd\mathcal{D}\subset\mathbb{R}^{d}, a bounded open domain. The classical neural operators are defined in, *e.g.*, [Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, and Anandkumar](https://arxiv.org/html/2511.01125v1#bib.bib47) [[47](https://arxiv.org/html/2511.01125v1#bib.bib47)] or [Lanthaler, Li, and Stuart](https://arxiv.org/html/2511.01125v1#bib.bib57) [[57](https://arxiv.org/html/2511.01125v1#bib.bib57)].

Importantly, our NO architecture (see [Figure˜2](https://arxiv.org/html/2511.01125v1#S2.F2 "In 2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")) contains both encoder–processor–decoder (EPD) type and Fourier neural operator (FNO)-type ‘branches’ at each layer, whereby spectral features and physical features are iteratively processed in parallel, and then combined together using the adaptively activated neurons spearheaded by the KAN paradigm [[48](https://arxiv.org/html/2511.01125v1#bib.bib48)], rather than the static activation strategy of classical MLPs. The resulting architecture thus exhibits beneficial properties both of FNO-type models and EPD-type models.

![Refer to caption](x2.png)


Figure 2: The KANO ([Section˜2.2.2](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS2 "2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")) pipeline.

What is illustrated in [Figure˜2](https://arxiv.org/html/2511.01125v1#S2.F2 "In 2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators") is as follows.

* 0)0)

  First boundary data (g)(g) and the PDE structure (G0)(G\_{0}) are concatenated into an input v0v\_{0}.
* 1)1)

  Learnable spectral features akin to FNOs are then extracted from v0v\_{0} and concatenated thereto.
* 2)2)

  At each processing iteration, the top NO branch applies a finite rank (R) integral operator, then all features are mixed and adaptively activated.
* 3)3)

  Finally the predictions are decoded via two branches: one applying another finite rank integral operator together as with to the FNO and the other leveraging a (trainable) spectral feature decoding akin to EPD, before both branches are mixed together to obtain the final prediction Γ^\hat{\Gamma}.

In the 2FBNO variant ([Section˜2.2.2](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS2 "2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")): Γ^​(v0)\hat{\Gamma}(v\_{0}) is passed through the Feynman–Kac adapter (see [Section˜3.1](https://arxiv.org/html/2511.01125v1#S3.SS1 "3.1 Elliptic PDE representation of the 2BSDE system ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")).

This being said, we can now proceed with the definition. In the remainder of the paper din=2d\_{\mathrm{in}}=2, any tuple vout∈W1,∞​(𝒟;ℝ)dinv\_{\mathrm{out}}\in W^{1,\infty}(\mathcal{D};\mathbb{R})^{d\_{\text{$\mathrm{in}$}}} will correspond to a pair of boundary and source data (g,f0)(g,f\_{0}), and dout=1d\_{\mathrm{out}}=1. However, since many of these result can be use in more general approximation theory of solutions operators to other PDEs, we keep the definition of our KANO model general enough to accomodate other applications.

###### Definition 2.4 (Kolmogorov–Arnold neural operator (KANO)).

Fix positive integers dind\_{\mathrm{in}}, doutd\_{\mathrm{out}}, LL, WW, L^\widehat{L}, W^\widehat{W}, DadaD\_{\mathrm{ada}}, WadaW\_{\mathrm{ada}}, as well as smoothness parameters α>0\alpha>0 and I∈ℕ⋆I\in\mathbb{N}^{\star} with 3≤α≤I3\leq\alpha\leq I.
We define a *Kolmogorov–Arnold neural operator (KANO)* Γ^:W1,∞​(𝒟;ℝ)din⟶W1,∞​(𝒟;ℝ)dout\widehat{\Gamma}:W^{1,\infty}(\mathcal{D};\mathbb{R})^{d\_{\text{$\mathrm{in}$}}}\longrightarrow W^{1,\infty}(\mathcal{D};\mathbb{R})^{d\_{\text{$\mathrm{out}$}}} to be any map sending any vin∈W1,∞​(𝒟,ℝ)dinv\_{\mathrm{in}}\in W^{1,\infty}(\mathcal{D},\mathbb{R})^{d\_{\text{$\mathrm{in}$}}} to some vL+1∈W1,∞​(𝒟;ℝ)doutv\_{L+1}\in W^{1,\infty}(\mathcal{D};\mathbb{R})^{d\_{\text{$\mathrm{out}$}}} where vL+1v\_{L+1} is defined iteratively by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v0​(x)\displaystyle v\_{0}(x) | ≔(v0crs​(x)v0ada​(x))≔(vin​(x)∫ℝdvin​(y)⊤​Ψ^1:in​(y)​dy⋮∫ℝdvin​(y)⊤​Ψ^K:in​(y)​dy),x∈𝒟,\displaystyle\coloneqq\begin{pmatrix}v\_{0}^{\mathrm{crs}}(x)\\[5.0pt] v\_{0}^{\mathrm{ada}}(x)\end{pmatrix}\coloneqq\begin{pmatrix}v\_{\mathrm{in}}(x)\\ \displaystyle\int\_{\mathbb{R}^{\text{$d$}}}v\_{\mathrm{in}}(y)^{\top}\widehat{\Psi}\_{1:\mathrm{in}}(y)\mathrm{d}y\\ \vdots\\ \displaystyle\int\_{\mathbb{R}^{\text{$d$}}}v\_{\mathrm{in}}(y)^{\top}\widehat{\Psi}\_{\text{$K$}:\mathrm{in}}(y)\mathrm{d}y\end{pmatrix},\;x\in{\cal D}, |  | (2.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vℓ+1​(x)\displaystyle v\_{\ell\text{$+$}1}(x) | ≔(vℓ+1crs​(x)vℓ+1ada​(x))≔σβℓ:I∙(Wℓ​(vℓcrs​(x)+(K(ℓ)​vℓ)​(x)vℓada​(x))+bℓ​(x)),ℓ∈{0,…,L−1},x∈𝒟,\displaystyle\coloneqq\begin{pmatrix}v\_{\ell+1}^{\mathrm{crs}}(x)\\[5.0pt] v\_{\ell+1}^{\mathrm{ada}}(x)\end{pmatrix}\coloneqq\sigma\_{\mathbf{\beta\_{\ell}}:I}\bullet\Bigg(W^{\ell}\begin{pmatrix}v\_{\ell}^{\mathrm{crs}}(x)+\big(K^{(\ell)}v\_{\ell}\big)(x)\\[5.0pt] v\_{\ell}^{\mathrm{ada}}(x)\end{pmatrix}+b^{\ell}(x)\Bigg),\;\ell\in\{0,\dots,L-1\},\;x\in{\cal D}, |  | (2.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vL+​1​(x)\displaystyle v\_{\text{$L$}\text{$+$}1}(x) | ≔W(L)​(vLcrs​(x)+(K(L)​vL)​(x)(vLada)⊤​(x)​(Ψ^1:out​(x)⋮Ψ^K:out​(x)))+b(L)​(x),x∈𝒟,\displaystyle\coloneqq W^{(\text{$L$})}\begin{pmatrix}v\_{\text{$L$}}^{\mathrm{crs}}(x)+\big(K^{({L})}v\_{\text{$L$}}\big)(x)\\[5.0pt] \big(v\_{\text{$L$}}^{\mathrm{ada}}\big)^{\top}(x)\begin{pmatrix}\widehat{\Psi}\_{1:\mathrm{out}}(x)\\ \vdots\\ \widehat{\Psi}\_{\text{$K$}:\mathrm{out}}(x)\end{pmatrix}\end{pmatrix}+b^{({L})}(x),\;x\in{\cal D}, |  | (2.11) |

where σβ:I\sigma\_{\mathbf{\beta}:I} is as in [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.Ex3 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators") and acts as in ([2.1](https://arxiv.org/html/2511.01125v1#S2.E1 "Equation 2.1 ‣ 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")). In particular, βℓ∈ℝ(I+2)×dℓ+1\beta\_{\ell}\in\mathbb{R}^{(I+2)\times d\_{\ell+1}}, each (Ψ^k:in)k∈{1,…,K}\big(\widehat{\Psi}\_{k:\mathrm{in}}\big)\_{k\in\{1,\dots,K\}} and (Ψ^k:out)k∈{1,…,K}\big(\widehat{\Psi}\_{k:\mathrm{out}}\big)\_{k\in\{1,\dots,K\}} are Res–KANs of depth DadaD\_{\mathrm{ada}} and width WadaW\_{\mathrm{ada}}, and for any ℓ∈{0,…,L+1}\ell\in\{0,\dots,L+1\}, we have W(ℓ)∈ℝdℓ+1×dℓW^{(\ell)}\in\mathbb{R}^{d\_{\text{$\ell$}\text{$+$}\text{$1$}}\times d\_{\text{$\ell$}}}

|  |  |  |
| --- | --- | --- |
|  | (K(ℓ)​v)​(x)≔∫𝒟kNN(ℓ)​(x,y)​v​(y)​dy,x∈𝒟,v∈Lp​(𝒟;ℝ)dℓ,b(ℓ)​(x)≔bNN(ℓ)​(x),x∈𝒟,\displaystyle\big(K^{(\ell)}v\big)(x)\coloneqq\int\_{\mathcal{D}}k\_{\text{$N$}\text{$N$}}^{(\ell)}(x,y)v(y)\mathrm{d}y,\;x\in\mathcal{D},\;v\in L^{p}(\mathcal{D};\mathbb{R})^{d\_{\text{$\ell$}}},\;b^{(\ell)}(x)\coloneqq b\_{\text{$N$}\text{$N$}}^{(\ell)}(x),\;x\in{\cal D}, |  |

where kNN(ℓ)∈Res–KANL^,W^I,α​(ℝd×d,ℝdℓ+1×dℓ)k\_{\text{$N$}\text{$N$}}^{(\ell)}\in\text{\rm Res--KAN}\_{\hat{\text{$L$}},\hat{\text{$W$}}}^{\text{$I$},\alpha}(\mathbb{R}^{d\times d},\mathbb{R}^{d\_{\text{$\ell$}\text{$+$}\text{$1$}}\times d\_{\text{$\ell$}}}) and bNN(ℓ)∈Res–KANL^,W^I,α​(ℝd,ℝdℓ)b\_{\text{$N$}\text{$N$}}^{(\ell)}\in\text{\rm Res--KAN}\_{\hat{\text{$L$}},\hat{\text{$W$}}}^{\text{$I$},\alpha}(\mathbb{R}^{d},\mathbb{R}^{d\_{\text{$\ell$}}}) are Res–KANs of depth L^\widehat{L} and width W^\widehat{W}.
We denote the above class of KANOs by

|  |  |  |
| --- | --- | --- |
|  | 𝒩​𝒪L^,W^L,W,I,α​(W1,∞​(𝒟;ℝ)din,W1,∞​(𝒟;ℝ)dout),\mathcal{NO}^{\text{$L$},\text{$W$},\text{$I$},\alpha}\_{\hat{\text{$L$}},\hat{\text{$W$}}}\big(W^{1,\infty}(\mathcal{D};\mathbb{R})^{d\_{\text{$\rm in$}}},W^{1,\infty}(\mathcal{D};\mathbb{R})^{d\_{\text{${\rm out}$}}}\big), |  |

which we abbreviate to 𝒩​𝒪L^,W^L,W,I,α\mathcal{NO}^{\text{$L$},\text{$W$},\text{$I$},\alpha}\_{\hat{\text{$L$}},\hat{\text{$W$}}} when the dimensions and domains are contextually evident.

For I≔⌈s⌉I\coloneqq\lceil s\rceil, we henceforth abbreviate

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒩​𝒪I,α≔⋃(L,L^,W,W^,α)∈(ℕ⋆)4×(0,1)𝒩​𝒪L^,W^L,W,I,α,\mathcal{NO}\_{\text{$I$},\alpha}\coloneqq\bigcup\_{(\text{$L$},\hat{\text{$L$}},\text{$W$},\hat{\text{$W$}},\alpha)\in(\mathbb{N}^{\text{$\star$}})^{\text{$4$}}\times(0,1)}\mathcal{NO}^{\text{$L$},\text{$W$},\text{$I$},\alpha}\_{\hat{\text{$L$}},\hat{\text{$W$}}}, |  | (2.12) |

Motivated by the PDE representation of the solutions to each member of our family of second-order BSDEs, given in ([1.2](https://arxiv.org/html/2511.01125v1#S1.E2 "Equation 1.2 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")), and due to [[16](https://arxiv.org/html/2511.01125v1#bib.bib16)], we extend the (semi-)classical class of neural operators above to the following stochastic model as follows.

###### Definition 2.5 (22Generative neural operators (2FBNO)).

Fix dimensions dd, and dind\_{\rm in}, as well as smoothness parameters 3≤α≤I3\leq\alpha\leq I, with I∈ℕ⋆I\in\mathbb{N}^{\star}, and fix depths L∈ℕ⋆L\in\mathbb{N}^{\star}, L^∈ℕ⋆\widehat{L}\in\mathbb{N}^{\star}, and widths W∈ℕ⋆W\in\mathbb{N}^{\star}, W^∈ℕ⋆\widehat{W}\in\mathbb{N}^{\star}. The class of forward–backward KANOs (2(2FBNOs)) ℱ​ℬL^,W^,XL,W,I,α\mathcal{FB}^{\text{$L$},\text{$W$},\text{$I$},\alpha}\_{\hat{\text{$L$}},\hat{\text{$W$}},X} consists of all

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ^:W1,∞​(𝒟,ℝ)din\displaystyle\widehat{\Gamma}:W^{1,\infty}(\mathcal{D},\mathbb{R})^{d\_{\text{$\rm in$}}} | ⟶(ℋT2)4≔∏i=14ℋT2\displaystyle\longrightarrow(\mathcal{H}\_{T}^{2})^{4}\coloneqq\prod\_{i=1}^{4}\,\mathcal{H}\_{T}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | f≔(f1,…,fdin)\displaystyle f\coloneqq(f\_{1},\dots,f\_{d\_{\rm in}}) | ⟼(Y^f,Z^f,Υ^f,A^f),\displaystyle\longmapsto(\widehat{Y}^{f},\widehat{Z}^{f},\widehat{\Upsilon}^{f},\widehat{A}^{f}), |  |

for which there is a Γ∈𝒩​𝒪L^,W^L,W,I,α​(W1,∞​(𝒟;ℝ)din,W1,∞​(𝒟;ℝ))\Gamma\in\mathcal{NO}^{\text{$L$},\text{$W$},\text{$I$},\alpha}\_{\hat{\text{$L$}},\hat{\text{$W$}}}(W^{1,\infty}(\mathcal{D};\mathbb{R})^{d\_{\text{$\rm in$}}},W^{1,\infty}(\mathcal{D};\mathbb{R})) satisfying the representation

|  |  |  |
| --- | --- | --- |
|  | Ytf=Γ​(f)​(Xt),Ztf=(∇Γ​(f))​(Xt),Υtf=(∇2Γ​(f))​(Xt),and​Atf=(ℒ​∇Γ​(f))​(Xt),\displaystyle Y\_{t}^{f}=\Gamma(f)(X\_{t}),\;Z\_{t}^{f}=\big(\nabla\Gamma(f)\big)(X\_{t}),\;\Upsilon\_{t}^{f}=\big(\nabla^{2}\Gamma(f)\big)(X\_{t}),\;\mbox{\rm and}\;A\_{t}^{f}=\big(\mathcal{L}\nabla\Gamma(f)\big)(X\_{t}), |  |

where, as before, ℒ\mathcal{L} denotes the generator of XX, without the drift.

## 3 Main results

### 3.1 Elliptic PDE representation of the 2BSDE system

For the reader’s convenience, we repeat the PDE in ([1.1](https://arxiv.org/html/2511.01125v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x,u​(x),∇u​(x),∇2u​(x))=−f0​(x),x∈𝒟,u​(x)=g​(x),x∈∂𝒟,f\big(x,u(x),\nabla u(x),\nabla^{2}u(x)\big)=-f\_{0}(x),\;x\in\mathcal{D},\;u(x)=g(x),\;x\in\partial\mathcal{D}, |  | (3.1) |

###### Proposition 3.1 (Non-linear Feynman–Kac’s formula).

Let uu be a classical solution to the PDE ([1.1](https://arxiv.org/html/2511.01125v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")), such that all the quantities below are defined and continuous in time

|  |  |  |
| --- | --- | --- |
|  | Yt=u​(Xt),Zt=∇u​(Xt),Υt=∇2u​(Xt),At=ℒ​∇u​(Xt),t∈[0,τ),ℙ​–a.s.,Y\_{t}=u(X\_{t}),\;Z\_{t}=\nabla u(X\_{t}),\;\Upsilon\_{t}=\nabla^{2}u(X\_{t}),\;A\_{t}=\mathcal{L}\nabla u(X\_{t}),\;t\in[0,\tau),\;\mathbb{P}\text{\rm--a.s.}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | Xt=x+∫0tβ​(Xs)​ds+∫0tγ​(Xs)​dWs,t≥0,ℙ​–a.s.,τ≔inf{t≥0:Xt∉𝒟}.X\_{t}=x+\int\_{0}^{t}\beta(X\_{s})\mathrm{d}s+\int\_{0}^{t}\gamma(X\_{s})\mathrm{d}W\_{s},\;t\geq 0,\;\mathbb{P}\text{\rm--a.s.},\;\tau\coloneqq\inf\big\{t\geq 0:X\_{t}\notin{\cal D}\big\}. |  |

Then (Y,Z,Υ,A)(Y,Z,\Upsilon,A) is a solution to ([FBSDE](https://arxiv.org/html/2511.01125v1#S1.Ex3 "Equation FBSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators"))–([2BSDE](https://arxiv.org/html/2511.01125v1#S1.Ex4 "Equation 2BSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")).

###### Proof.

Since uu is smooth enough, we can apply Itô’s formula to obtain for any t∈[0,τ)t\in[0,\tau)

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(Xt)\displaystyle u(X\_{t}) | =u​(Xτ)−∫tτ12​Tr​[γ​(Xs)​γ⊤​(Xs)​∇2u​(Xs)]​ds−∫tτ∇u​(Xs)⋅dXs,\displaystyle=u(X\_{\tau})-\int\_{t}^{\tau}\frac{1}{2}\mathrm{Tr}\big[\gamma(X\_{s})\gamma^{\top}(X\_{s})\nabla^{2}u(X\_{s})\big]\mathrm{d}s-\int\_{t}^{\tau}\nabla u(X\_{s})\cdot\mathrm{d}X\_{s}, |  |

as well as

|  |  |  |
| --- | --- | --- |
|  | ∇u​(Xt)=∇u​(x)+∫0t∇2u​(Xs)​dXs+∫0tℒ​∇u​(Xs)​ds=∇u​(x)+∫0tΥs​dXs+∫0tAs​ds.\displaystyle\nabla u(X\_{t})=\nabla u(x)+\int\_{0}^{t}\nabla^{2}u(X\_{s})\mathrm{d}X\_{s}+\int\_{0}^{t}{\cal L}\nabla u(X\_{s})\mathrm{d}s=\nabla u(x)+\int\_{0}^{t}\Upsilon\_{s}\mathrm{d}X\_{s}+\int\_{0}^{t}A\_{s}\mathrm{d}s. |  |

it follows by the PDE satisfied by uu that

|  |  |  |
| --- | --- | --- |
|  | u​(Xt)=g​(Xτ)+∫tτ(f​(Xs,Ys,Zs,Υs)+f0​(Xs)−12​Tr​[γ​(Xs)​γ⊤​(Xs)​Υs])​ds−∫tτZs⊤​dXs,u(X\_{t})=g(X\_{\tau})+\int\_{t}^{\tau}\bigg(f(X\_{s},Y\_{s},Z\_{s},\Upsilon\_{s})+f\_{0}(X\_{s})-\frac{1}{2}\mathrm{Tr}\big[\gamma(X\_{s})\gamma^{\top}(X\_{s})\Upsilon\_{s}\big]\bigg)\mathrm{d}s-\int\_{t}^{\tau}Z\_{s}^{\top}\mathrm{d}X\_{s}, |  |

as desired.
∎

### 3.2 General approximability guarantee

Let 0<δ≤10<\delta\leq 1 and let 𝕊dδ\mathbb{S}\_{d}^{\delta} denote the subset of 𝕊d+\mathbb{S}^{\text{$+$}}\_{d} consisting of matrices satisfying the following near–norm preserving property: for every x∈ℝdx\in\mathbb{R}^{d}

|  |  |  |
| --- | --- | --- |
|  | δ​‖x‖2≤x​A⊤​x≤1δ​‖x‖2.\delta\|x\|^{2}\leq xA^{\top}x\leq\frac{1}{\delta}\|x\|^{2}. |  |

We write generically u′{\textrm{u}^{\prime}} for (x0,…,xd)∈ℝ1+d(x\_{0},\dots,x\_{d})\in\mathbb{R}^{1+d}, u′′{\textrm{u}^{\prime\prime}} for any element of 𝕊dδ\mathbb{S}\_{d}^{\delta}, and u≔(u′,u′′){\textrm{u}}\coloneqq({\textrm{u}^{\prime}},{\textrm{u}^{\prime\prime}}).

###### Setting 3.2.

and let G¯:ℝd⟶[0,∞)\bar{G}:\mathbb{R}^{d}\longrightarrow[0,\infty) be Borel measurable.
Fix constants K0,KF≥0K\_{0},K\_{F}\geq 0,
LF,Cg≥0L\_{F},C\_{g}\geq 0,
and 0<δ≤10<\delta\leq 1. We require the following of the domain 𝒟\mathcal{D}.

###### Assumption 3.3 (Domain Regularity).

The domain 𝒟⊆ℝd\mathcal{D}\subseteq\mathbb{R}^{d} is a non-empty bounded domain with C1,1C^{1,1}-boundary
satisfying the exterior ball condition.

Our general approximability result, for which favourable rates cannot generally be guaranteed, considers families of fully non-linear elliptic PDEs

|  |  |  |
| --- | --- | --- |
|  | f​(x,u​(x),∇u​(x),∇2u​(x))=0,x∈𝒟,u​(x)=g​(x),x∈∂𝒟,f\big(x,u(x),\nabla u(x),\nabla^{2}u(x)\big)=0,\;x\in\mathcal{D},\;u(x)=g(x),\;x\in\partial\mathcal{D}, |  |

where the boundary data g∈Wk,p​(∂𝒟)g\in W^{k,p}(\partial\mathcal{D}) is assumed to be sufficiently smooth, *i.e.* k≥2k\geq 2.

Following [Krylov](https://arxiv.org/html/2511.01125v1#bib.bib54) [[54](https://arxiv.org/html/2511.01125v1#bib.bib54), Chapter 14], our PDEs will have sufficiently regular solutions under the following conditions.

###### Assumption 3.4.

Assume that p>dp>d, and fix constants (c1,c2,R0)∈(0,1]3(c\_{1},c\_{2},R\_{0})\in(0,1]^{3}, LF≥0L\_{\text{$F$}}\geq 0, a function ωF:[0,∞)⟶[0,∞)\omega\_{\text{$F$}}:[0,\infty)\longrightarrow[0,\infty) with ωF​(0)=0\omega\_{\text{$F$}}(0)=0, a Borel measurable function G¯:ℝd⟶[0,∞)\bar{G}:\mathbb{R}^{d}\longrightarrow[0,\infty), and Borel measurable functions FF and GG of the variables (u0,u′,x)(u\_{0},{\textrm{u}^{\prime}},x) and (u,x)(u,x) respectively. We have

* (i)(i)

  f=F+Gf=F+G, and for all u′′∈𝕊d+{\textrm{u}^{\prime\prime}}\in\mathbb{S}\_{d}^{\text{$+$}}, u′∈ℝ1+d{\textrm{u}^{\prime}}\in\mathbb{R}^{1\text{$+$}d}, and x∈ℝdx\in\mathbb{R}^{d}, we have

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |G​(u,x)|≤c1​‖u′′‖F+c2​‖u′‖+G¯​(x),F​(0,x)=0;\big|G({\textrm{u}},x)\big|\leq c\_{1}\|{\textrm{u}^{\prime\prime}}\|\_{\text{$F$}}+c\_{2}\|{\textrm{u}^{\prime}}\|+\bar{G}(x),\;F(0,x)=0; |  | (3.2) |
* (i​i)(ii)

  FF is LFL\_{F}–Lipschitz continuous with respect to u′′;{\textrm{u}^{\prime\prime}};
* (i​i​i)(iii)

  for any v∈ℝv\in\mathbb{R}, 0<r≤R00<r\leq R\_{0}, and x∈𝒟x\in\mathcal{D}, there exists a convex function F¯:𝕊d⟶[0,∞)\bar{F}:\mathbb{S}\_{d}\longrightarrow[0,\infty) such that

  1. (a)(a)

     F¯​(0,x)=0\bar{F}(0,x)=0, and ∇u′′F¯\nabla\_{u^{\text{$\prime$}\text{$\prime$}}}\bar{F} has range in 𝕊dδ\mathbb{S}\_{d}^{\delta} at every point of twice differentiability of F¯;\bar{F};
  2. (b)(b)

     for every u′′∈𝕊d+{\textrm{u}^{\prime\prime}}\in\mathbb{S}\_{d}^{\text{$+$}} with ‖u′′‖F=1\|{\textrm{u}^{\prime\prime}}\|\_{F}=1, we have

     |  |  |  |  |
     | --- | --- | --- | --- |
     |  | infB​(r,x)∩𝒟supr¯>0|F¯​(u′0,r​u′′,u)−F¯​(τ​u′′)|r≤c2​Vol​(𝒟∩B​(r,x)),\inf\_{B(r,x)\cap\mathcal{D}}\sup\_{\bar{r}>0}\frac{\big|\bar{F}({\textrm{u}^{\prime}}\_{0},r{\textrm{u}^{\prime\prime}},u)-\bar{F}(\tau{\textrm{u}^{\prime\prime}})\big|}{r}\leq c\_{2}\mathrm{Vol}\big(\mathcal{D}\cap B(r,x)\big), |  | (3.3) |

     where Vol​(A)\mathrm{Vol}(A) denotes the dd-dimensional Lebesgue measure of a Lebesgue-measurable set A⊆ℝd;A\subseteq\mathbb{R}^{d};
  3. (c)(c)

     for any (u,v)∈ℝ2(u,v)\in\mathbb{R}^{2}, x∈𝒟x\in\mathcal{D}, and u′∈𝕊d+{\textrm{u}^{\prime}}\in\mathbb{S}\_{d}^{\text{$+$}}, we have

     |  |  |  |  |
     | --- | --- | --- | --- |
     |  | |F​(u,u′′,x)−F​(v,u′′,x)|≤ωF​(|u−v|)​‖u′′‖F.\big|F(u,{\textrm{u}^{\prime\prime}},x)-F(v,{\textrm{u}^{\prime\prime}},x)\big|\leq\omega\_{\text{$F$}}(|u-v|)\|{\textrm{u}^{\prime\prime}}\|\_{\text{$F$}}. |  | (3.4) |

The next definition introduces appropriate perturbations of the original PDE we consider, and uses notations from [Section˜3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators").

###### Definition 3.5 (PDE perturbation space 𝒳k​(r)\mathcal{X}\_{k}(r)).

Fix r>0r>0, k∈ℕ⋆k\in\mathbb{N}^{\star} and let 𝒳k​(r)\mathcal{X}\_{k}(r) consist of all pairs (G¯0,g)∈W2,p​(𝒟)×Wk,p​(𝒟)(\bar{G}\_{0},g)\in W^{2,p}(\mathcal{D})\times W^{k,p}(\mathcal{D}) with ‖g‖Wk,p​(𝒟)≤r\|g\|\_{W^{\text{$k$}\text{$,$}\text{$p$}}(\mathcal{D})}\leq r.
Define G0≔G+G¯0G\_{0}\coloneqq G+\bar{G}\_{0} and, for every pair (G0,g)∈𝒳k​(r)(G\_{0},g)\in\mathcal{X}\_{k}(r) denote the solution to the following associated fully non-linear elliptic PDE by uG¯0,gu\_{\bar{G}\_{\text{$0$}},g}

|  |  |  |  |
| --- | --- | --- | --- |
|  | (F+G⏟Structure +G¯0⏟Perturbation)​(x,u​(x),∇u​(x),∇2u​(x))=0,∀x∈𝒟,u​(x)=g​(x)⏟Perturbation,∀x∈∂𝒟.\displaystyle\bigg(\underbrace{F+G}\_{\mbox{\tiny\rm Structure \normalsize}}+\underbrace{\bar{G}\_{0}}\_{\mbox{\tiny\rm Perturbation}}\bigg)\big(x,u(x),\nabla u(x),\nabla^{2}u(x)\big)=0,\;\forall x\in\mathcal{D},\;u(x)=\underbrace{g(x)}\_{\mbox{\tiny\rm Perturbation}},\;\forall x\in\partial\mathcal{D}. |  | (3.5) |

###### Example 3.6 (Source perturbations only).

We can, of course, restrict ourselves to perturbations of the source condition itself only, in which case we may restrict our attention to G¯0\bar{G}\_{0} which are constant in their first argument; *i.e.* G¯0​(u,x)=f0​(x)\bar{G}\_{0}(u,x)=f\_{0}(x) for some f0∈Wk,p​(𝒟)f\_{0}\in W^{k,p}(\mathcal{D}), similarly to the special case in ([1.5](https://arxiv.org/html/2511.01125v1#S1.E5 "Equation 1.5 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")).

###### Theorem 3.7 (Approximability of the perturbation-to-solution map).

Fix q∈[1,+∞)q\in[1,+\infty), let 𝒟\mathcal{D} be a bounded exterior-thick domain in ℝd\mathbb{R}^{d} with C1,1C^{1,1}-boundary, let r>0r>0, k>1+max⁡{1,dp}k>1+\max\big\{1,\tfrac{d}{p}\big\}, and 𝒳⊆𝒳k​(r)\mathcal{X}\subseteq\mathcal{X}\_{k}(r) be compact.

Suppose [Sections˜3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") and [3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") hold
and that both σS\sigma\_{\text{$S$}} and σW\sigma\_{\text{$W$}} satisfy [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators").
Then, for every approximation error ε>0\varepsilon>0, there exists some neural operator Γ^∈𝒩​𝒪⌈k⌉,1\hat{\Gamma}\in\mathcal{NO}\_{\lceil k\rceil,1}, cf. ([2.12](https://arxiv.org/html/2511.01125v1#S2.E12 "Equation 2.12 ‣ 2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")), satisfying the uniform estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(G¯0,g)∈𝒳‖uG¯0,g−Γ^​(G¯0,g)‖W2,p​(𝒟)<ε.\sup\_{(\bar{G}\_{\text{$0$}},g)\in\mathcal{X}}\,\big\|u\_{\bar{G}\_{\text{$0$}},g}-\hat{\Gamma}(\bar{G}\_{0},g)\big\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}<\varepsilon. |  | (3.6) |

The proof of [Theorem˜3.7](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem7 "Theorem 3.7 (Approximability of the perturbation-to-solution map). ‣ 3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") is based on two ingredients. First, we establish the local–Lipschitz regularity of the coefficient-to-solution map associated to our family of fully non-linear elliptic PDEs ([Section˜A.4](https://arxiv.org/html/2511.01125v1#A1.SS4 "A.4 Stability estimate of general solution operator ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) verifying the only necessary condition for approximability by continuous models classes; such as our NO, namely continuity—a property which need not be immediate for arbitrary coefficient-to-solution maps.
Next, we rely on [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") which establishes a general universal approximation theorem for operators between Besov spaces.

In this sense, [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") for our NO architecture which, among other things, can be regarded as a generalisation of [Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, and Anandkumar](https://arxiv.org/html/2511.01125v1#bib.bib47) [[47](https://arxiv.org/html/2511.01125v1#bib.bib47), Theorem 11], which does not cover Besov spaces Bq,rs​(𝒟)B\_{q,r}^{s}(\mathcal{D}) for finite values of qq and rr ( recall that Ws,p​(𝒟)=Bq,rs​(𝒟)W^{s,p}(\mathcal{D})=B\_{q,r}^{s}(\mathcal{D}) [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Remark 1.2]). We emphasise that here, the case of finite qq (and rr) is necessary since Ws,∞​(𝒟)W^{s,\infty}(\mathcal{D})-spaces are automatically excluded from both [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") and [[47](https://arxiv.org/html/2511.01125v1#bib.bib47), Theorem 11], as well as any encoder-decoder-type model using basis expansions (*e.g.* [[33](https://arxiv.org/html/2511.01125v1#bib.bib33)]), since Ws,∞W^{s,\infty} is not separable and thus cannot admit a Schauder basis. Additionally, since this space is non-separable and any realistic NO model must be parameterised by finitely many parameters and depend continuously on them, any realistic NO model defines a separable space, As such, it cannot be dense/universal in spaces of continuous functions between non-separable spaces—again by elementary topological considerations.

We now consider the approximation of a specialized family of elliptic PDEs, whose solution operator exhibits enough structure so that it (not all continuous functions) can be approximated on non-separable space W1,∞​(𝒟)W^{1,\infty}(\mathcal{D}).

### 3.3 Feasible rates

#### 3.3.1 Semi-linear elliptic PDE

In what follows, we will make use of the map Sγ,μ,λ:W(d+3)/2,2​(∂𝒟;ℝ)⟶W1,∞​(𝒟;ℝ)S\_{\gamma,\mu,\lambda}:W^{(d+3)/2,2}(\partial\mathcal{D};\mathbb{R})\longrightarrow W^{1,\infty}(\mathcal{D};\mathbb{R}) sending boundary data to domain data, and defined for each g∈W(d+3)/2,2​(∂𝒟;ℝ)g\in W^{(d+3)/2,2}(\partial\mathcal{D};\mathbb{R}) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sγ,μ,λ​(g)≔wg,S\_{\gamma,\mu,\lambda}(g)\coloneqq w\_{g}, |  | (3.7) |

where wg∈W(d+4)/2,2​(𝒟;ℝ)⊂W1,∞​(𝒟;ℝ)w\_{g}\in W^{(d+4)/2,2}(\mathcal{D};\mathbb{R})\subset W^{1,\infty}(\mathcal{D};\mathbb{R}).
is the unique solution of

|  |  |  |
| --- | --- | --- |
|  | −∇⋅γ​∇wg+μ⋅∇wg+λ​wg=0​in​𝒟,wg=g​on​∂𝒟.-\nabla\cdot\gamma\nabla w\_{g}+\mu\cdot\nabla w\_{g}+\lambda w\_{g}=0\ \mathrm{in}\ \mathcal{D},\;w\_{g}=g\ \mathrm{on}\ \partial\mathcal{D}. |  |

We assume the following on the maps γ\gamma, μ\mu and λ\lambda.

###### Assumption 3.8.

The maps γ:𝒟⟶ℝd×d\gamma:\mathcal{D}\longrightarrow\mathbb{R}^{d\times d}, μ:𝒟⟶ℝd\mu:\mathcal{D}\longrightarrow\mathbb{R}^{d}, and λ:𝒟⟶ℝ\lambda:\mathcal{D}\longrightarrow\mathbb{R} satisfy the following conditions

* (i)(i)

  γ∈C∞​(𝒟¯;ℝd×d)\gamma\in C^{\infty}(\bar{\mathcal{D}};\mathbb{R}^{d\times d}), μ∈C∞​(𝒟¯;ℝd)\mu\in C^{\infty}(\bar{\mathcal{D}};\mathbb{R}^{d}), and λ∈C∞​(𝒟¯;ℝ)\lambda\in C^{\infty}(\bar{\mathcal{D}};\mathbb{R}) where C∞​(𝒟¯;ℝd)C^{\infty}(\bar{\mathcal{D}};\mathbb{R}^{d}) and C∞​(𝒟¯;ℝd×d)C^{\infty}(\bar{\mathcal{D}};\mathbb{R}^{d\times d}) denote the spaces of all dd-dimensional vector-valued and d×dd\times d matrix-valued functions that are infinitely differentiable on 𝒟\mathcal{D} and whose derivatives admit continuous extensions to the closure 𝒟¯\bar{\mathcal{D}};
* (i​i)(ii)

  γ\gamma is uniformly elliptic and bounded in the sense that there are positive constants γ0\gamma\_{0} and γ1\gamma\_{1} such that

  |  |  |  |
  | --- | --- | --- |
  |  | γ0​‖ξ‖2≤ξ⊤​γ​(x)​ξ≤γ1​‖ξ‖2,∀(x,ξ)∈𝒟×ℝd;\gamma\_{0}\|\xi\|^{2}\leq\xi^{\top}\gamma(x)\xi\leq\gamma\_{1}\|\xi\|^{2},\;\forall(x,\xi)\in\mathcal{D}\times\mathbb{R}^{d}; |  |
* (i​i​i)(iii)

  μ\mu and λ\lambda are such that

  |  |  |  |
  | --- | --- | --- |
  |  | λ≥0,and​λ≥∇⋅μ​∑i=1d∂xiμ.\lambda\geq 0,\;\text{\rm and}\;\lambda\geq\nabla\cdot\mu\sum\_{i=1}^{d}\partial\_{x\_{i}}\mu. |  |

Next, we summaries our main assumptions on f~\tilde{f}.

###### Assumption 3.9.

The map f~:𝒟×ℝ⟶ℝ\tilde{f}:\mathcal{D}\times\mathbb{R}\longrightarrow\mathbb{R} satisfies

* (i)(i)

  there exists δ0>0\delta\_{0}>0 and H∈ℕ⋆∖{1,2}H\in\mathbb{N}^{\star}\setminus\{1,2\} such that

  |  |  |  |
  | --- | --- | --- |
  |  | f~​(x,z)=∑h=0H∂zhf~​(x,0)h!​zh,for​‖z‖<δ0,and​x∈𝒟;\tilde{f}(x,z)=\sum\_{h=0}^{H}\frac{\partial\_{z}^{h}\tilde{f}(x,0)}{h!}z^{h},\;\text{\rm for}\;\|z\|<\delta\_{0},\;\text{\rm and}\;x\in\mathcal{D}; |  |
* (i​i)(ii)

  f~​(⋅,0)=∂z1f~​(⋅,0)=0;\tilde{f}(\cdot,0)=\partial\_{z}^{1}\tilde{f}(\cdot,0)=0;
* (i​i​i)(iii)

  ∂zhf~​(⋅,0)∈C∞​(𝒟¯;ℝ)\partial\_{z}^{h}\tilde{f}(\cdot,0)\in C^{\infty}(\bar{\mathcal{D}};\mathbb{R}) for all h∈{2,…,H}h\in\{2,\dots,H\}.

Assumption (i) posits that f~​(x,z)\tilde{f}(x,z) is analytic at z=0z=0 and represented by a finite power series truncated at order HH. Assumption (ii) removes the zeroth- and first-order terms, which are already captured by f0​(x)f\_{0}(x) and λ​(x)​u​(x)\lambda(x)u(x) in ([1.5](https://arxiv.org/html/2511.01125v1#S1.E5 "Equation 1.5 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")). Assumption (iii) requires all coefficient functions to be smooth, ensuring a well-posed setting for the subsequent analysis.

Finally, we formulate a smallness assumption.

###### Assumption 3.10.

We take 0<δ<δ00<\delta<\delta\_{0} ((where δ0\delta\_{0} comes from [Section˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators").(i)(i))) so that

|  |  |  |
| --- | --- | --- |
|  | C1​δ<1,ρ≔C2​δ<1,C3​δ<1,\displaystyle C\_{1}\delta<1,\;\rho\coloneqq C\_{2}\delta<1,\;C\_{3}\delta<1, |  |

where the positive constants C1C\_{1}, C2C\_{2}, C3C\_{3} will appear in ([A.6](https://arxiv.org/html/2511.01125v1#A1.E6 "Equation A.6 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), ([A.7](https://arxiv.org/html/2511.01125v1#A1.E7 "Equation A.7 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), and ([A.13](https://arxiv.org/html/2511.01125v1#A1.E13 "Equation A.13 ‣ A.1.2 Proof of Theorem 3.11 ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), and depend only pp, dd, 𝒟\mathcal{D}, f~\tilde{f}, γ\gamma, and μ\mu.

Under the above assumptions, we have the following approximation guarantee for the solution operator of the PDE associated with our randomly stopped second-order BSDE system ([SDE](https://arxiv.org/html/2511.01125v1#S1.Ex1 "Equation SDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")), ([FBSDE](https://arxiv.org/html/2511.01125v1#S1.Ex3 "Equation FBSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")), ([2BSDE](https://arxiv.org/html/2511.01125v1#S1.Ex4 "Equation 2BSDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")).

###### Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem).

Let888This is need as our proof relies on the approximation results of [[45](https://arxiv.org/html/2511.01125v1#bib.bib45)] for the relevant Green’s function associated to our PDEs. d≥3d\geq 3.
Let [Sections˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), [3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") and [3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") hold.
Suppose that 𝒟\mathcal{D} is a bounded open set with Lipschitz boundary in ℝd\mathbb{R}^{d}.
Let 1<s<21<s<2 and 1≤p<dd−11\leq p<\frac{d}{d-1}.
Then, for any 0<ε<10<\varepsilon<1, there are positive integers LL, WW, L^\widehat{L}, W^\widehat{W}, and Γ∈𝒩​𝒪L^,W^L,W,I,α​(W1,∞​(𝒟;ℝ)2,W1,∞​(𝒟;ℝ))\Gamma\in{\mathcal{NO}^{\text{$L$},\text{$W$},\text{$I$},\alpha}\_{\hat{\text{$L$}},\hat{\text{$W$}}}}(W^{1,\infty}(\mathcal{D};\mathbb{R})^{2},W^{1,\infty}(\mathcal{D};\mathbb{R})) such that

|  |  |  |
| --- | --- | --- |
|  | sup(f0,g)∈ℬ‖Γ+​(f0,g)−Γ​(f0,Sγ,μ,λ​(g))‖W1,∞​(𝒟;ℝ)≤ε.\sup\_{(f\_{0},g)\in{\cal B}}\big\|\Gamma^{\text{$+$}}(f\_{0},g)-\Gamma(f\_{0},S\_{\gamma,\mu,\lambda}(g))\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq\varepsilon. |  |

where the supremum is taken over the set

|  |  |  |
| --- | --- | --- |
|  | ℬ≔BW1,∞​(𝒟;ℝ)​(0,δ2)×BW(d+3)/2,2​(∂𝒟;ℝ)​(0,δ2).{\cal B}\coloneqq B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}(0,\delta^{2})\times B\_{W^{\text{$($}\text{$d$}\text{$+$}\text{$3$}\text{$)$}\text{$/$}\text{$2$},2}(\partial\mathcal{D};\mathbb{R})}(0,\delta^{2}). |  |

Moreover, we have the following estimates for parameters L=L​(Γ)L=L(\Gamma), W=W​(Γ)W=W(\Gamma), L^=L^​(Γ)\widehat{L}=\widehat{L}(\Gamma), and W^=W^​(Γ)\widehat{W}=\widehat{W}(\Gamma),

|  |  |  |
| --- | --- | --- |
|  | L≤C​log⁡(ε−1),W≤C,L^≤C,W^≤C​ε−1(s−1)​p,L\leq C\log(\varepsilon^{-1}),\;W\leq C,\;\widehat{L}\leq C,\;\widehat{W}\leq C\varepsilon^{\text{$-$}\frac{1}{(s-1)p}}, |  |

where C>0C>0 depends only on ss, pp, dd, 𝒟\mathcal{D}, f~\tilde{f}, γ\gamma, and μ\mu.

Our quantitative approximation rates are available because the family of elliptic PDEs considered here is well structured. In the fully general setting, however, since our NOs are continuous, one should not expect rates, as the solution operator should not even be expected to be continuous (let alone locally–Lipschitz continuous) which is necessary for approximability by the elementary uniform limit theorem from point-set topology, see [Munkres](https://arxiv.org/html/2511.01125v1#bib.bib71) [[71](https://arxiv.org/html/2511.01125v1#bib.bib71), Theorem 21.6].
In that case—even if the solution operator is only continuous for general fully non-linear families—the best achievable rates are no better than worst-case bounds for approximating non-linear locally–Lipschitz continuous operators, see [[55](https://arxiv.org/html/2511.01125v1#bib.bib55)], which require an exponential increase in trainable neurons to achieve a linear decrease in error. Thus, even when approximability holds, any such ‘rate’ would be scarcely more informative than a simple existence statement.

Consequently, the principal obstacle is approximability, which is twofold:

(i)(i) the relevant solution operator in the fully non-linear elliptic case must be regular enough to be approximable by some universal deep-learning class;

(i​i)(ii) our models must be universal on the specific function spaces on which this solution map acts.

(i)(i) requires a stability analysis of our PDE family under coefficient perturbations, while (i​i)(ii) calls for a universal approximation theorem for our architecture, proved via basis-expansion techniques as in [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"), akin in spirit to [[47](https://arxiv.org/html/2511.01125v1#bib.bib47), Theorem 11], that holds on more general Besov spaces over regular Euclidean domains. This two-step scheme was introduced for deep learning in stochastic filtering [[42](https://arxiv.org/html/2511.01125v1#bib.bib42)] and refined for differential games in [[5](https://arxiv.org/html/2511.01125v1#bib.bib5), [29](https://arxiv.org/html/2511.01125v1#bib.bib29)].

#### 3.3.2 Solutions to the family of second-order BSDEs

We now derive the stochastic version of the above (deterministic) approximation theorem.
We additionally require the following regularity conditions.

###### Assumption 3.12 (Regularity of forward process).

There is some x0∈𝒟x\_{0}\in\mathcal{D} such that for each R>0R>0

1. (i)(i)

   ((local smoothness)): (β,γ)∈Cb∞​(Bℝd​(x0,5​R);ℝd×𝕊d+)2(\beta,\gamma)\in C\_{b}^{\infty}(B\_{\mathbb{R}^{d}}(x\_{0},5R);\mathbb{R}^{d}\times\mathbb{S}\_{d}^{+})^{2};
2. (i​i)(ii)

   ((local ellipticity)): γ​(x)​γ​(x)⊤≥cx0,R​Id\gamma(x)\gamma(x)^{\top}\geq c\_{x\_{0},R}\mathrm{I}\_{d}, for every x∈Bℝd​(x0,3​R)x\in B\_{\mathbb{R}^{d}}(x\_{0},3R), for some 0<cx0,R<1;0<c\_{x\_{0},R}<1;
3. (i​i​i)(iii)

   there exists a unique strong solution to ([SDE](https://arxiv.org/html/2511.01125v1#S1.Ex1 "Equation SDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")).

###### Theorem 3.13.

Let [Sections˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), [3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), [3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") and [3.3.2](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS2 "3.3.2 Solutions to the family of second-order BSDEs ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") hold, then, for any 0<ε<10<\varepsilon<1 and any time-window 0<T−<T+0<T\_{\text{$-$}}<T\_{\text{$+$}}, there are integers LL, WW, Δ\Delta, HH, and Γ^∈ℱ​ℬL^,W^,σ^L,W,ReQU\widehat{\Gamma}\in\mathcal{FB}\_{\hat{\text{$L$}},\hat{\text{$W$}},\hat{\text{$\sigma$}}}^{\text{$L$},\text{$W$},\text{$\rm ReQU$}} satisfying

|  |  |  |
| --- | --- | --- |
|  | sup(f,g)∈ℬ𝔼ℙ​[supτ∧T−≤t≤T+∧τ|Γ^​(f,g)t−(Ytx,Ztx)|]≲ε,\sup\_{(f,g)\in{\cal B}}\,\mathbb{E}^{\mathbb{P}}\biggl[\sup\_{\tau\wedge T\_{\text{$-$}}\leq t\leq T\_{\text{$+$}}\wedge\tau}\,\Big|\widehat{\Gamma}(f,g)\_{t}-(Y^{x}\_{t},Z^{x}\_{t})\Big|\biggr]\lesssim\varepsilon, |  |

where the supremum is taken over the set

|  |  |  |
| --- | --- | --- |
|  | ℬ≔BW01,∞​(𝒟;ℝ)​(0,δ2)×BH1+(d+1)/2​(∂𝒟;ℝ)​(0,δ2).{\cal B}\coloneqq B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}\_{\text{$0$}}(\mathcal{D};\mathbb{R})}(0,\delta^{2})\times B\_{H^{\text{$1$}\text{$+$}\text{$($}\text{$d$}\text{$+$}\text{$1$}\text{$)$}\text{$/$}\text{$2$}}(\partial\mathcal{D};\mathbb{R})}(0,\delta^{2}). |  |

We have the same estimates for the parameters L=L​(Γ)L=L(\Gamma), W=W​(Γ)W=W(\Gamma), L^=L^​(Γ)\widehat{L}=\widehat{L}(\Gamma), and W^=W^​(Γ)\widehat{W}=\widehat{W}(\Gamma) as in [Theorem˜3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators").

## 4 Experimental results

In this section, we empirically validate our theoretical findings on two canonical benchmarks in the 2BSDE literature: the periodic semi-linear example of [Chassagneux, Chen, Frikha, and Zhou](https://arxiv.org/html/2511.01125v1#bib.bib13) [[13](https://arxiv.org/html/2511.01125v1#bib.bib13)] and the linear–quadratic control example of [Pham, Warin, and Germain](https://arxiv.org/html/2511.01125v1#bib.bib78) [[78](https://arxiv.org/html/2511.01125v1#bib.bib78)]. We deploy the KANO architecture with a slight modification in the kernel layer (see [C.3](https://arxiv.org/html/2511.01125v1#A3.SS3 "C.3 Architectural details ‣ Appendix C Experimental details ‣ One model to solve them all: 2BSDE families via neural operators") for details). Specifically, rather than jointly learning both the kernel basis and its coefficients, we fix the basis to a Fourier system, obtained via uniform discretisation of the spatial domain, while retaining trainable, Res–KAN–parametrised coefficients. Furthermore, skip connections parametrised by additional Res–KAN layers are introduced on top of the learnable Fourier kernel coefficients. The resulting spectral layer follows the kernel introduced in [Li, Kovachki, Azizzadenesheli, Liu, Bhattacharya, Stuart, and Anandkumar](https://arxiv.org/html/2511.01125v1#bib.bib60) [[60](https://arxiv.org/html/2511.01125v1#bib.bib60)].

### 4.1 Periodic semi-linear case

In this experiment, we study the periodic semi-linear benchmark of [[13](https://arxiv.org/html/2511.01125v1#bib.bib13)] in dimension d=5d=5. This benchmark consists of trigonometric drift–diffusion and has a closed-form solution u​(t,x)u(t,x) depending on ∑i=15xi\sum\_{i=1}^{5}x\_{i}. This enables exact supervision of u,∇u,∇2uu,\nabla u,\nabla^{2}u and pathwise validation under periodic boundary conditions. The forward–-backward SDE system and its closed-form solution are detailed in [Section˜C.1](https://arxiv.org/html/2511.01125v1#A3.SS1 "C.1 Periodic semi-linear case ‣ Appendix C Experimental details ‣ One model to solve them all: 2BSDE families via neural operators").

A KANO model is trained on 40964096 samples drawn according to the procedure in [Section˜C.4](https://arxiv.org/html/2511.01125v1#A3.SS4 "C.4 Training pipeline ‣ Appendix C Experimental details ‣ One model to solve them all: 2BSDE families via neural operators"), and subsequently evaluated along independently generated trajectories using the Euler-–Maruyama sampler described in [Section˜C.5](https://arxiv.org/html/2511.01125v1#A3.SS5 "C.5 Inference pipeline ‣ Appendix C Experimental details ‣ One model to solve them all: 2BSDE families via neural operators"). [Figures˜3](https://arxiv.org/html/2511.01125v1#S4.F3 "In 4.2 Linear–quadratic case ‣ 4 Experimental results ‣ One model to solve them all: 2BSDE families via neural operators") and [4](https://arxiv.org/html/2511.01125v1#S4.F4 "Figure 4 ‣ 4.2 Linear–quadratic case ‣ 4 Experimental results ‣ One model to solve them all: 2BSDE families via neural operators") display the projections of two randomly selected trajectories onto the (x1,x2)(x\_{1},x\_{2})-plane, together with the corresponding ground-truth solutions uu, first and second partial derivatives ∂u/∂x1\partial u/\partial x\_{1} and ∂2u/∂x12\partial^{2}u/\partial x\_{1}^{2}, and the respective predictions produced by the trained model along these trajectories. We observe that the model is generally able to accurately capture the solution, as well as the first and second partial derivatives along the entire trajectories, with only minor discrepancies in the second derivatives.

### 4.2 Linear–quadratic case

We next consider the LQ/Hamilton–Jacobi=-Bellman benchmark proposed in [[78](https://arxiv.org/html/2511.01125v1#bib.bib78)] in d=5d=5 (see [Section˜C.2](https://arxiv.org/html/2511.01125v1#A3.SS2 "C.2 Linear–quadratic (LQ) case ‣ Appendix C Experimental details ‣ One model to solve them all: 2BSDE families via neural operators") for details). It represents a HJB-type problem with quadratic cost, whose value function remains quadratic u​(t,x)=x⊤​K​(t)​xu(t,x)=x^{\top}K(t)x, and where K​(t)K(t) satisfies a Riccati ODE. It offers analytic targets for u,∇u,∇2uu,\nabla u,\nabla^{2}u and a clean test of learning constant-in-space Hessians and optimal-feedback structure.

The same training and inference pipeline as described in the semi-linear case is used, with a KANO network trained on 40964096 samples. [Figure˜5](https://arxiv.org/html/2511.01125v1#S4.F5 "In 4.2 Linear–quadratic case ‣ 4 Experimental results ‣ One model to solve them all: 2BSDE families via neural operators") presents two random trajectories projected onto the (x1,x2)(x\_{1},x\_{2})-plane. The figure also compares the analytic solution uu, its gradient components ∂u/∂x1\partial u/\partial x\_{1}, and the diagonal Hessian entries ∂2u/∂x12\partial^{2}u/\partial x\_{1}^{2} with the corresponding model predictions along these paths. The predicted values of uu closely follow the analytical solution. The derivatives are recovered with satisfactory accuracy, and the Hessian, which is expected to remain constant in space, is also well captured. Although the estimated derivatives show some deviations from the smooth exact values, their overall accuracy remains high. In summary, the network effectively learns and reproduces the solution uu and its derivatives along the generated trajectories.

![Refer to caption](x3.png)


(a) Random paths

![Refer to caption](x4.png)


(b) Solutions

![Refer to caption](x5.png)


(c) First derivatives

![Refer to caption](x6.png)


(d) Second derivatives

Figure 3: Ground-truth and KANO-predicted solutions for the first randomly selected trajectory of the periodic semilinear example from [[13](https://arxiv.org/html/2511.01125v1#bib.bib13)]. Each panel shows the projection onto the (x1,x2)(x\_{1},x\_{2})-plane with uu, ∂u/∂x1\partial u/\partial x\_{1}, and ∂2u/∂x12\partial^{2}u/\partial x\_{1}^{2} along this path.



![Refer to caption](x7.png)


(a) Random paths

![Refer to caption](x8.png)


(b) Solutions

![Refer to caption](x9.png)


(c) First derivatives

![Refer to caption](x10.png)


(d) Second derivatives

Figure 4: Continuation of [Figure˜3](https://arxiv.org/html/2511.01125v1#S4.F3 "In 4.2 Linear–quadratic case ‣ 4 Experimental results ‣ One model to solve them all: 2BSDE families via neural operators"), showing the second randomly selected trajectory for the same semi-linear example.



![Refer to caption](x11.png)

![Refer to caption](x12.png)

![Refer to caption](x13.png)

![Refer to caption](x14.png)

![Refer to caption](x15.png)


(a) Random paths

![Refer to caption](x16.png)


(b) Solutions

![Refer to caption](x17.png)


(c) First derivatives

![Refer to caption](x18.png)


(d) Second derivatives

Figure 5: Comparison between the ground-truth and KANO-predicted solutions for the periodic linear–quadratic example of [[78](https://arxiv.org/html/2511.01125v1#bib.bib78)]. The figure shows two randomly selected trajectories projected onto the (x1,x2)(x\_{1},x\_{2})-plane, together with the corresponding values of uu, ∂u/∂x1\partial u/\partial x\_{1}, and ∂2u/∂x12\partial^{2}u/\partial x\_{1}^{2} along these paths.

#### 4.2.1 Ablation on the sample size

We next train a model using eight times fewer training samples than before *i.e.*, 512 samples) and evaluate it following the same procedure as in previous experiments. The resulting quantities of interest are shown in [Figure˜6](https://arxiv.org/html/2511.01125v1#S4.F6 "In 4.2.1 Ablation on the sample size ‣ 4.2 Linear–quadratic case ‣ 4 Experimental results ‣ One model to solve them all: 2BSDE families via neural operators"). We observe that in the vicinity of t=0t=0, the solution uu is not well approximated, which in turn affects the accuracy of its first- and second-order partial derivatives. This behaviour is consistent with the theoretical discussion presented earlier: a sufficient number of training samples is required in the high-dimensional space ℝd\mathbb{R}^{d} for the model to accurately capture the solution near t=0t=0.

![Refer to caption](x19.png)


(a) Random path

![Refer to caption](x20.png)


(b) Solution

![Refer to caption](x21.png)


(c) First derivative

![Refer to caption](x22.png)


(d) Second derivative

Figure 6: Comparison between the ground-truth and KANO-predicted solutions for the periodic linear–quadratic example of [[78](https://arxiv.org/html/2511.01125v1#bib.bib78)] in *low training data regime*. The figure shows two randomly selected trajectories projected onto the (x1,x2)(x\_{1},x\_{2})-plane, together with the corresponding values of uu, ∂u/∂x1\partial u/\partial x\_{1}, and ∂2u/∂x12\partial^{2}u/\partial x\_{1}^{2} along these paths.

## Acknowledgements

Takashi Furuya was supported by JSPS KAKENHI Grant Number JP24K16949, 25H01453, JST CREST JPMJCR24Q5, JST ASPIRE JPMJAP2329.
Anastasis Kratsios acknowledges financial support from an NSERC Discovery Grant No. RGPIN-2023-04482 and No. DGECR-2023-00230, and they acknowledge that resources used in preparing this research were provided, in part, by the Province of Ontario, the Government of Canada through CIFAR, and companies sponsoring the Vector Institute999<https://vectorinstitute.ai/partnerships/current-partners/>; they would also like to thank Behnoosh Zamanlooy for her support.
Dylan Possamaï gratefully acknowledges partial support by the SNF project MINT 205121-219818.

## Appendix A Proof of PDE results

### A.1 Proof of Theorem [3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")

This appendix contains the proofs of our paper’s main theoretical guarantees.

#### A.1.1 Well-posedness

Let Gγ,μ,λ​(x,y)G\_{\gamma,\mu,\lambda}(x,y) be a (real-valued) Green’s function for −∇⋅γ​∇+μ⋅∇+λ-\nabla\cdot\gamma\nabla+\mu\cdot\nabla+\lambda with a Dirichlet boundary condition, i.e., for y∈𝒟y\in\mathcal{D},

|  |  |  |
| --- | --- | --- |
|  | −∇⋅γ∇Gγ,μ,λ(⋅,y)+μ⋅∇Gγ,μ,λ(⋅,y)+λGγ,μ,λ(⋅,y)=−δ(⋅−y)in𝒟,-\nabla\cdot\gamma\nabla G\_{\gamma,\mu,\lambda}(\cdot,y)+\mu\cdot\nabla G\_{\gamma,\mu,\lambda}(\cdot,y)+\lambda G\_{\gamma,\mu,\lambda}(\cdot,y)=-\delta(\cdot-y)\ \mathrm{in}\ \mathcal{D}, |  |

|  |  |  |
| --- | --- | --- |
|  | Gγ,μ,λ​(⋅,y)=0​on​∂𝒟.G\_{\gamma,\mu,\lambda}(\cdot,y)=0\ \mathrm{on}\ \partial\mathcal{D}. |  |

###### Lemma A.1.

Let [Section˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") hold.
Then, we have

|  |  |  |
| --- | --- | --- |
|  | Gγ,μ,λ∈Ws,p​(𝒟×𝒟;ℝ).G\_{\gamma,\mu,\lambda}\in W^{s,p}(\mathcal{D}\times\mathcal{D};\mathbb{R}). |  |

where 1≤p<dd−11\leq p<\frac{d}{d-1} and 1≤s<21\leq s<2.

###### Proof.

From [[45](https://arxiv.org/html/2511.01125v1#bib.bib45), Theorem 8.1]101010Note that our setting is that γ\gamma and μ\mu are smooth. Thus, they are uniformly Dini continuous, which implies that they are of Dini mean oscillation., the Green function Gγ,μ,λ​(x,y)G\_{\gamma,\mu,\lambda}(x,y) for the operator L​u≔−∇⋅γ​∇u+μ⋅∇u+λ​uLu\coloneqq-\nabla\cdot\gamma\nabla u+\mu\cdot\nabla u+\lambda u can be estimated as for β∈ℕ0d\beta\in\mathbb{N}^{d}\_{0} with |β|≤1|\beta|\leq 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∂xβGγ,μ,λ​(x,y)‖≤C0​‖x−y‖1−d,\big\|\partial\_{x}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|\leq C\_{0}\|x-y\|^{1-d}, |  | (A.1) |

where C0>0C\_{0}>0 is a constant depending on 𝒟\mathcal{D}, dd, β\beta, γ\gamma, μ\mu, and λ\lambda.
Also, applying [[45](https://arxiv.org/html/2511.01125v1#bib.bib45), Theorem 8.1] to the Green function gγ,μ,λ​(y,x)g\_{\gamma,\mu,\lambda}(y,x) for the adjoint operator L⊤​u=−∇⋅(γ⊤​∇u+μ​u)+λL^{\top}u=-\nabla\cdot(\gamma^{\top}\nabla u+\mu u)+\lambda, the Green function gγ,μ,λ​(y,x)g\_{\gamma,\mu,\lambda}(y,x) can be estimated, for β∈(ℕ⋆)d\beta\in(\mathbb{N}^{\star})^{d} with ‖β‖≤1\|\beta\|\leq 1 by

|  |  |  |
| --- | --- | --- |
|  | ‖∂yβgγ,μ,λ​(y,x)‖≤C0​‖y−x‖1−d.\big\|\partial\_{y}^{\beta}g\_{\gamma,\mu,\lambda}(y,x)\big\|\leq C\_{0}\|y-x\|^{1-d}. |  |

With [[45](https://arxiv.org/html/2511.01125v1#bib.bib45), Proposition 6.13] and [Section˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators").(i​i​i)(iii), we see that G​(x,y)=g​(y,x)G(x,y)=g(y,x) (x≠yx\neq y), which implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∂yβGγ,μ,λ​(x,y)‖≤C0​‖x−y‖1−d.\big\|\partial\_{y}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|\leq C\_{0}\|x-y\|^{1-d}. |  | (A.2) |

We now choose R>0R>0 such that 𝒟⊂Bℝd​(0,R)\mathcal{D}\subset B\_{\mathbb{R}^{\text{$d$}}}(0,R).
Using ([A.2](https://arxiv.org/html/2511.01125v1#A1.E2 "Equation A.2 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), we estimate that for x∈𝒟x\in\mathcal{D} and β∈(ℕ⋆)d\beta\in(\mathbb{N}^{\star})^{d} with ‖β‖≤1\|\beta\|\leq 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫𝒟‖∂xβGγ,μ,λ​(x,y)‖p​dy≲∫𝒟‖x−y‖(1−d)​p​dy=∫x−𝒟‖z‖(1−d)​p​dz\displaystyle\int\_{\mathcal{D}}\big\|\partial\_{x}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|^{p}\mathrm{d}y\lesssim\int\_{\mathcal{D}}\|x-y\|^{(1-d)p}\mathrm{d}y=\int\_{x\text{$-$}\mathcal{D}}\|z\|^{(1-d)p}\mathrm{d}z | ≤∫Bℝd​(0,2​R)‖z‖(1−d)​p​dz\displaystyle\leq\int\_{B\_{\text{$\mathbb{R}$}^{\text{$d$}}}(0,2R)}\|z\|^{(1-d)p}\mathrm{d}z |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲∫02​Rr(1−d)​p​rd−1​dr=∫02​Rr(d−1)​(1−p)​dr≲1,\displaystyle\lesssim\int\_{0}^{2R}r^{(1-d)p}r^{d-1}\mathrm{d}r=\int\_{0}^{2R}r^{(d-1)(1-p)}\mathrm{d}r\lesssim 1, |  | (A.3) |

where we have used that 1<p<dd−11<p<\frac{d}{d-1}.
We can obtain the estimate for the derivative with respect to yy similarly, using now ([A.2](https://arxiv.org/html/2511.01125v1#A1.E2 "Equation A.2 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")).
Note that we use the symbol ≲\lesssim to omit a multiplicative constant that is independent of xx on the left-hand side.
∎

Using the Green function Gγ,μ,λ​(x,y)G\_{\gamma,\mu,\lambda}(x,y), we define an integral operator encoding ([1.5](https://arxiv.org/html/2511.01125v1#S1.E5 "Equation 1.5 ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(x)≔∫𝒟Gγ,μ,λ​(x,y)​(f~​(y,u​(y))−f​(y))​dy+wg​(x),x∈𝒟,u(x)\coloneqq\int\_{\mathcal{D}}G\_{\gamma,\mu,\lambda}(x,y)\big(\tilde{f}(y,u(y))-f(y)\big)\mathrm{d}y+w\_{g}(x),\;x\in\mathcal{D}, |  | (A.4) |

where f0∈W1,∞​(𝒟;ℝ)f\_{0}\in W^{1,\infty}(\mathcal{D};\mathbb{R}) and wg​(x)∈Wd+42,2​(𝒟;ℝ)w\_{g}(x)\in W^{\frac{d+4}{2},2}(\mathcal{D};\mathbb{R}) is the unique solution of

|  |  |  |
| --- | --- | --- |
|  | −∇⋅γ​∇wg+μ⋅∇wg+λ​wg=0,on​D,wg=g,on​∂D.-\nabla\cdot\gamma\nabla w\_{g}+\mu\cdot\nabla w\_{g}+\lambda w\_{g}=0,\;\mathrm{on}\;D,\;w\_{g}=g,\;\mathrm{on}\;\partial D. |  |

where g∈Wd+32,2​(∂𝒟)g\in W^{\frac{d+3}{2},2}(\partial\mathcal{D}).
Note that, it is well known that a linear elliptic equation has the unique solution wgw\_{g} (see, e.g., [[37](https://arxiv.org/html/2511.01125v1#bib.bib37)]).
By the Sobolev embedding theorem (see, *e.g.*, [Evans](https://arxiv.org/html/2511.01125v1#bib.bib26) [[26](https://arxiv.org/html/2511.01125v1#bib.bib26), Section 5.6.3]) we have

|  |  |  |
| --- | --- | --- |
|  | W(d+4)/2,2​(𝒟)⊂C(d+4)/2−d/2−1,ξ0​(𝒟¯)⊂W1,∞​(𝒟),W^{(d+4)/2,2}(\mathcal{D})\subset C^{(d+4)/2-d/2-1,\xi\_{0}}(\overline{\mathcal{D}})\subset W^{1,\infty}(\mathcal{D}), |  |

where 0<ξ0<10<\xi\_{0}<1 is a constant. Hence, wg∈W1,∞​(𝒟)w\_{g}\in W^{1,\infty}(\mathcal{D}).
We define next the mapping TT by

|  |  |  |
| --- | --- | --- |
|  | T​(u)​(x)≔∫𝒟Gγ,μ,λ​(x,y)​(f~​(y,u​(y))−f0​(y))​dy+wg​(x),x∈𝒟,T(u)(x)\coloneqq\int\_{\mathcal{D}}G\_{\gamma,\mu,\lambda}(x,y)\big(\tilde{f}(y,u(y))-f\_{0}(y)\big)\mathrm{d}y+w\_{g}(x),\;x\in\mathcal{D}, |  |

We set

|  |  |  |
| --- | --- | --- |
|  | BW1,∞​(0,δ)≔{u∈W1,∞​(𝒟;ℝ):‖u‖W1,∞​(𝒟;ℝ)≤δ},B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta)\coloneqq\big\{u\in W^{1,\infty}(\mathcal{D};\mathbb{R}):\|u\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq\delta\big\}, |  |

|  |  |  |
| --- | --- | --- |
|  | BW(d+3)/2,2​(0,δ)≔{g∈W(d+3)/2,2​(∂𝒟;ℝ):‖g‖Wd+3)/2,2​(∂𝒟;ℝ)≤δ}.B\_{W^{\text{$(d+3)/2$}\text{$,$}\text{$2$}}}(0,\delta)\coloneqq\big\{g\in W^{(d+3)/2,2}(\partial\mathcal{D};\mathbb{R}):\|g\|\_{W^{\text{$d+3)/2$}\text{$,$}\text{$2$}}(\partial\mathcal{D};\mathbb{R})}\leq\delta\big\}. |  |

Then, BW1,∞​(0,δ)B\_{W^{1,\infty}}(0,\delta) is a closed subset in W1,∞​(𝒟;ℝ)W^{1,\infty}(\mathcal{D};\mathbb{R}).

###### Lemma A.2.

Let [Sections˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), [3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") and [3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") hold.
Let f∈BW1,∞​(𝒟;ℝ)​(0,δ2)f\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}(0,\delta^{2}) and g∈BW(d+3)/2,2​(∂𝒟;ℝ)​(0,δ2)g\in B\_{W^{\text{$($}\text{$d$}\text{$+$}\text{$3$}\text{$)$}\text{$/$}\text{$2$},\text{$2$}}(\partial\mathcal{D};\mathbb{R})}(0,\delta^{2}). Then, the map T:BW1,∞​(0,δ)⟶BW1,∞​(0,δ)T:B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta)\longrightarrow B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta) is a ρ\rho-contraction where ρ∈(0,1)\rho\in(0,1) is defined in [Section˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators").
In particular, there exists a unique solution of ([A.4](https://arxiv.org/html/2511.01125v1#A1.E4 "Equation A.4 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) in BW1,∞​(0,δ)B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).

###### Proof.

We see that for x∈𝒟x\in\mathcal{D}

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(w)​(x)\displaystyle T(w)(x) | ≔∫𝒟Gγ,μ,λ​(x,y)​[f~​(y,w​(y))−f0​(y)]​dy+wg​(x)\displaystyle\coloneqq\int\_{\mathcal{D}}G\_{\gamma,\mu,\lambda}(x,y)\big[\tilde{f}(y,w(y))-f\_{0}(y)\big]\mathrm{d}y+w\_{g}(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫𝒟Gγ,μ,λ​(x,y)​(∑h=2H∂zhf~​(y,0)h!​w​(y)h−f0​(y))​dy+wg​(x)\displaystyle=\int\_{\mathcal{D}}G\_{\gamma,\mu,\lambda}(x,y)\Bigg(\sum\_{h=2}^{H}\frac{\partial^{h}\_{z}\tilde{f}(y,0)}{h!}w(y)^{h}-f\_{0}(y)\Bigg)\mathrm{d}y+w\_{g}(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑h=2H1h!​∫𝒟Gγ,μ,λ​(x,y)​∂zhf~​(y,0)​w​(y)h​d​y−∫𝒟Gγ,μ,λ​(x,y)​f0​(y)​dy+wg​(x).\displaystyle=\sum\_{h=2}^{H}\frac{1}{h!}\int\_{\mathcal{D}}G\_{\gamma,\mu,\lambda}(x,y)\partial^{h}\_{z}\tilde{f}(y,0)w(y)^{h}\mathrm{d}y-\int\_{\mathcal{D}}G\_{\gamma,\mu,\lambda}(x,y)f\_{0}(y)\mathrm{d}y+w\_{g}(x). |  |

First, we will show that T:BW1,∞​(0,δ)⟶BW1,∞​(0,δ)T:B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta)\longrightarrow B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).
Let w∈BW1,∞​(0,δ)w\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).
Using this, that f0f\_{0}, and wgw\_{g} are both in BW1,∞​(0,δ2)B\_{W^{1,\text{$\infty$}}}(0,\delta^{2}), and [Section˜A.1.1](https://arxiv.org/html/2511.01125v1#A1.SS1.SSS1 "A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"), we see that for any β∈(ℕ⋆)d\beta\in(\mathbb{N}^{\star})^{d} with ‖β‖≤1\|\beta\|\leq 1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∂xβT​(w)​(x)‖\displaystyle\big\|\partial\_{x}^{\beta}T(w)(x)\big\| | ≲∫𝒟‖∂xβGγ,μ,λ​(x,y)‖​(∑h=2H1h!​|w​(y)|h+|f0​(y)|)​dy+‖∂xβwg​(x)‖\displaystyle\lesssim\int\_{\mathcal{D}}\big\|\partial\_{x}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|\Bigg(\sum\_{h=2}^{H}\frac{1}{h!}|w(y)|^{h}+|f\_{0}(y)|\Bigg)\mathrm{d}y+\big\|\partial\_{x}^{\beta}w\_{g}(x)\big\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲δ2​∫𝒟‖∂xβGγ,μ,λ​(x,y)‖​dy+δ2≲δ2.\displaystyle\lesssim\delta^{2}\int\_{\mathcal{D}}\big\|\partial\_{x}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|\mathrm{d}y+\delta^{2}\lesssim\delta^{2}. |  | (A.5) |

This means that T​(w)∈W1,∞​(𝒟;ℝ)T(w)\in W^{1,\infty}(\mathcal{D};\mathbb{R}).
We also see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖T​(w)‖W1,∞​(𝒟;ℝ)≤C1​δ2,\|T(w)\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq C\_{1}\delta^{2}, |  | (A.6) |

where C1>0C\_{1}>0 is a constant depending on pp, dd, 𝒟\mathcal{D}, f~\tilde{f}, γ\gamma, and μ\mu.
By choosing δ>0\delta>0 in [Section˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), we have T​w∈BW1,∞​(0,δ)Tw\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).

Next, we will show that T:BW1,∞​(0,δ)⟶BW1,∞​(0,δ)T:B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta)\longrightarrow B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta) is a contraction mapping.
Let (w1,w2)∈BW1,∞​(0,δ)×BW1,∞​(0,δ)(w\_{1},w\_{2})\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta)\times B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).
Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | w1​(y)h−w2​(y)h\displaystyle w\_{1}(y)^{h}-w\_{2}(y)^{h} | =(∑i=0h−1w1​(y)h−1−i​w2​(y)i)​(w1​(y)−w2​(y)),\displaystyle=\Bigg(\sum\_{i=0}^{h-1}w\_{1}(y)^{h-1-i}w\_{2}(y)^{i}\Bigg)\big(w\_{1}(y)-w\_{2}(y)\big), |  |

we deduce that for any β∈(ℕ⋆)d\beta\in(\mathbb{N}^{\star})^{d} with ‖β‖≤1\|\beta\|\leq 1,
by Hölder’s inequality and [Section˜A.1.1](https://arxiv.org/html/2511.01125v1#A1.SS1.SSS1 "A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∂xβT​(w1)​(x)−∂xβT​(w2)​(x)‖\displaystyle\big\|\partial\_{x}^{\beta}T(w\_{1})(x)-\partial\_{x}^{\beta}T(w\_{2})(x)\big\| | ≲∑h=2H1h!​∫𝒟‖∂xβGγ,μ,λ​(x,y)‖​|w1​(y)h−w2​(y)h|​dy\displaystyle\lesssim\sum\_{h=2}^{H}\frac{1}{h!}\int\_{\mathcal{D}}\big\|\partial\_{x}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|\big|w\_{1}(y)^{h}-w\_{2}(y)^{h}\big|\mathrm{d}y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑h=2H1h!​∑i=0h−1∫𝒟‖∂xβGγ,μ,λ​(x,y)‖​|w1​(y)h−1−i​w2​(y)i|​|w1​(y)−w2​(y)|​dy\displaystyle\leq\sum\_{h=2}^{H}\frac{1}{h!}\sum\_{i=0}^{h-1}\int\_{\mathcal{D}}\big\|\partial\_{x}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|\big|w\_{1}(y)^{h-1-i}w\_{2}(y)^{i}\big|\big|w\_{1}(y)-w\_{2}(y)\big|\mathrm{d}y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑h=2Hhh!​δh−1​∫𝒟‖∂xβGγ,μ,λ​(x,y)‖≲δ​‖w1−w2‖W1,∞​(𝒟;ℝ).\displaystyle\leq\sum\_{h=2}^{H}\frac{h}{h!}\delta^{h-1}\int\_{\mathcal{D}}\big\|\partial\_{x}^{\beta}G\_{\gamma,\mu,\lambda}(x,y)\big\|\lesssim\delta\big\|w\_{1}-w\_{2}\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}. |  |

Then, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖T​(w1)−T​(w2)‖W1,∞​(𝒟;ℝ)≤C2​δ​‖w1−w2‖W1,∞​(𝒟;ℝ)=ρ​‖w1−w2‖W1,∞​(𝒟;ℝ),\big\|T(w\_{1})-T(w\_{2})\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq C\_{2}\delta\|w\_{1}-w\_{2}\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}=\rho\|w\_{1}-w\_{2}\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}, |  | (A.7) |

where C2>0C\_{2}>0 is a constant depending on pp, dd, 𝒟\mathcal{D}, f~\tilde{f}, γ\gamma, and μ\mu. By choosing δ>0\delta>0 as in [Section˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), we have that TT is ρ\rho-contraction mapping in BW1,∞​(0,δ)B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).
∎

Given the previous result, and using Banach’s fixed-point theorem, the following solution operator is well-defined

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ+:BW1,∞​(0,δ2)×BW(d+3)/2,2​(0,δ2)\displaystyle\Gamma^{\text{$+$}}:B\_{W^{\text{$1$},\text{$\infty$}}}(0,\delta^{2})\times B\_{W^{\text{$($}\text{$d$}\text{$+$}\text{$3$}\text{$)$}\text{$/$}\text{$2$},\text{$2$}}}(0,\delta^{2}) | ⟶BW1,∞​(0,δ)\displaystyle\longrightarrow B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (f0,g)\displaystyle(f\_{0},g) | ⟼u,\displaystyle\longmapsto u, |  |

where, uu is the unique solution of [Equation˜A.4](https://arxiv.org/html/2511.01125v1#A1.E4 "In A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") in BW1,∞​(0,δ)B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).

#### A.1.2 Proof of Theorem [3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")

We now prove Theorem [3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") in a series of several steps. Throughout, the activation function applied component-wise to the neural operator layers in neural operator’s neurons, *i.e.* in ([2.9](https://arxiv.org/html/2511.01125v1#S2.E9 "Equation 2.9 ‣ 2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")), will always be taken to be the squared-ReLU function, that is to say β=(1,0,…,0)\beta=(1,0,\dots,0) in ([2.1](https://arxiv.org/html/2511.01125v1#S2.E1 "Equation 2.1 ‣ 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")) for the neural operator.

Let (f0,g)∈BW1,∞​(0,δ2)×BW(d+3)/2,2​(0,δ2)(f\_{0},g)\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta^{2})\times B\_{W^{\text{$($}\text{$d$}\text{$+$}\text{$3$}\text{$)$}\text{$/$}\text{$2$},2}}(0,\delta^{2}) and let u∈BW1,∞​(0,δ)u\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta) be a solution of ([A.4](https://arxiv.org/html/2511.01125v1#A1.E4 "Equation A.4 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), that is, Γ+​(f,g)=u\Gamma^{\text{$+$}}(f,g)=u.
By [[48](https://arxiv.org/html/2511.01125v1#bib.bib48), Theorem 1], for any ε>0\varepsilon>0, there exist Res–KANs, with representation as in [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), kn​nh:ℝd⟶ℝk\_{nn}^{h}:\mathbb{R}^{d}\longrightarrow\mathbb{R}, h∈{2,…,H}h\in\{2,\dots,H\}, and kn​n′:ℝd⟶ℝk^{\prime}\_{nn}:\mathbb{R}^{d}\longrightarrow\mathbb{R}
such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖kn​nh​(x,y)−1h!​Gγ,μ,λ​(x,y)​∂zhf~​(y,0)‖Wx,y1,p​(𝒟×𝒟;ℝ)≤ε,h∈{2,…,H},\bigg\|k\_{nn}^{h}(x,y)-\frac{1}{h!}G\_{\gamma,\mu,\lambda}(x,y)\partial^{h}\_{z}\tilde{f}(y,0)\bigg\|\_{W^{\text{$1$}\text{$,$}\text{$p$}}\_{\text{$x$}\text{$,$}\text{$y$}}(\mathcal{D}\times\mathcal{D};\mathbb{R})}\leq\varepsilon,\;h\in\{2,\dots,H\}, |  | (A.8) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖kn​n′​(x,y)−Gγ,μ,λ​(x,y)‖Wx,y1,p​(𝒟×𝒟;ℝ)≤ε,\big\|k^{\prime}\_{nn}(x,y)-G\_{\gamma,\mu,\lambda}(x,y)\big\|\_{W^{\text{$1$}\text{$,$}\text{$p$}}\_{\text{$x$}\text{$,$}\text{$y$}}(\mathcal{D}\times\mathcal{D};\mathbb{R})}\leq\varepsilon, |  | (A.9) |

where depths L^​(kn​nh)\widehat{L}(k\_{nn}^{h})
and L^​(kn​n′)\widehat{L}(k^{\prime}\_{nn}) are of order 𝒪​(1)\mathcal{O}(1), while the width of W^​(kn​nh)\widehat{W}(k\_{nn}^{h}) and W^​(kn​n′)\widehat{W}(k^{\prime}\_{nn}) are of order 𝒪​(ε−1(s−1)​p)\mathcal{O}(\varepsilon^{-\frac{1}{(s-1)p}}). Then, we define by

|  |  |  |
| --- | --- | --- |
|  | L^:=L^​(Γ):=max⁡{L^​(kn​n1),…,L^​(kn​nH),L^​(kn​n′)},W^:=W^​(Γ):=max⁡{W^​(kn​n1),…,W^​(kn​nH),W^​(kn​n′)},\widehat{L}:=\widehat{L}(\Gamma):=\max\{\widehat{L}(k\_{nn}^{1}),...,\widehat{L}(k\_{nn}^{H}),\widehat{L}(k^{\prime}\_{nn})\},\quad\widehat{W}:=\widehat{W}(\Gamma):=\max\{\widehat{W}(k\_{nn}^{1}),...,\widehat{W}(k\_{nn}^{H}),\widehat{W}(k^{\prime}\_{nn})\}, |  |

Then, they are estimated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {L^≤C,W^≤C​ε−1(s−1)​p,\begin{cases}\widehat{L}\leq C,\\[8.00003pt] \widehat{W}\leq C\varepsilon^{-\frac{1}{(s-1)p}},\end{cases} |  | (A.10) |

where C>0C>0 is a constant depending on dd, ss, HH, and pp.
We can then define the map TNNT\_{\text{$N$}\text{$N$}} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | TNN​(u)​(x)\displaystyle T\_{\text{$N$}\text{$N$}}(u)(x) | ≔∑h=2H∫𝒟kn​nh​(x,y)​(u​(y))h​dy−∫𝒟kn​n′​(x,y)​f​(y)​dy+wg​(x).\displaystyle\coloneqq\sum\_{h=2}^{H}\int\_{\mathcal{D}}k\_{nn}^{h}(x,y)(u(y))^{h}\mathrm{d}y-\int\_{\mathcal{D}}k^{\prime}\_{nn}(x,y)f(y)\mathrm{d}y+w\_{g}(x). |  | (A.11) |

###### Lemma A.3.

There exists a constant C4>0C\_{4}>0 depending on pp, dd, 𝒟\mathcal{D}, γ\gamma, μ\mu, and λ\lambda such that for any u∈BW1,∞​(𝒟;ℝ)​(0,δ)u\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}(0,\delta)

|  |  |  |
| --- | --- | --- |
|  | ‖T​(u)−TNN​(u)‖W1,∞​(𝒟;ℝ)≤C4​ε.\big\|T(u)-T\_{\text{$N$}\text{$N$}}(u)\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq C\_{4}\varepsilon. |  |

###### Proof.

Let u∈BW1,∞​(𝒟;ℝ)​(0,δ)u\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}(0,\delta).
We see that for β∈(ℕ⋆)d\beta\in(\mathbb{N}^{\star})^{d} with ‖β‖≤1\|\beta\|\leq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∂xβT​(u)​(x)−∂xβTNN​(u)​(x)|\displaystyle\big|\partial\_{x}^{\beta}T(u)(x)-\partial\_{x}^{\beta}T\_{\text{$N$}\text{$N$}}(u)(x)\big| | ≤∑h=2H‖kn​nh​(x,y)−1h!​Gγ,μ,λ​(x,y)​∂zhf​(y,0)‖Wx,y1,p​(𝒟;ℝ)​(∫𝒟|u​(y)h|p′​dy)1/p′\displaystyle\leq\sum\_{h=2}^{H}\bigg\|k\_{nn}^{h}(x,y)-\frac{1}{h!}G\_{\gamma,\mu,\lambda}(x,y)\partial^{h}\_{z}f(y,0)\bigg\|\_{W^{\text{$1$}\text{$,$}\text{$p$}}\_{\text{$x$}\text{$,$}\text{$y$}}(\mathcal{D};\mathbb{R})}\bigg(\int\_{\mathcal{D}}|u(y)^{h}|^{p^{\text{$\prime$}}}\mathrm{d}y\bigg)^{1/p^{\text{$\prime$}}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +‖kn​n′​(x,y)−Gγ,μ,λ​(x,y)‖Wx,y1,p​(𝒟;ℝ)​(∫𝒟|f​(y)|p′​dy)1/p′≤C4​δ2​ε<ε,\displaystyle\quad+\big\|k^{\prime}\_{nn}(x,y)-G\_{\gamma,\mu,\lambda}(x,y)\big\|\_{W^{\text{$1$}\text{$,$}\text{$p$}}\_{\text{$x$}\text{$,$}\text{$y$}}(\mathcal{D};\mathbb{R})}\bigg(\int\_{\mathcal{D}}|f(y)|^{p^{\text{$\prime$}}}\mathrm{d}y\bigg)^{1/p^{\text{$\prime$}}}\leq C\_{4}\delta^{2}\varepsilon<\varepsilon, |  | (A.12) |

which is exactly the desired result.
∎

###### Lemma A.4.

TNNT\_{\text{$N$}\text{$N$}} maps BW1,∞​(0,δ)B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta) to itself.

###### Proof.

Fix u∈BW1,∞​(𝒟;ℝ)​(0,δ)u\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}(0,\delta).
Using ([A.6](https://arxiv.org/html/2511.01125v1#A1.E6 "Equation A.6 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) and ([A.12](https://arxiv.org/html/2511.01125v1#A1.E12 "Equation A.12 ‣ A.1.2 Proof of Theorem 3.11 ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), we see that

|  |  |  |
| --- | --- | --- |
|  | ‖TNN​(u)‖W1,∞​(𝒟;ℝ)≤‖TNN​(u)‖W1,∞​(𝒟;ℝ)+‖T​(u)−TNN​(u)‖W1,∞​(𝒟;ℝ)≲δ2.\big\|T\_{\text{$N$}\text{$N$}}(u)\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq\big\|T\_{\text{$N$}\text{$N$}}(u)\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}+\big\|T(u)-T\_{\text{$N$}\text{$N$}}(u)\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\lesssim\delta^{2}. |  |

Thus, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖TNN​(u)‖W1,∞​(𝒟;ℝ)≤C3​δ2,\|T\_{\text{$N$}\text{$N$}}(u)\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq C\_{3}\delta^{2}, |  | (A.13) |

where C3>0C\_{3}>0 is a constant depending on ss, pp, dd, 𝒟\mathcal{D}, and γ\gamma. By the choice of δ\delta in [Section˜3.3.1](https://arxiv.org/html/2511.01125v1#S3.SS3.SSS1 "3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), we see that ‖TNN​(u)‖W1,∞​(𝒟;ℝ)≤δ\|T\_{\text{$N$}\text{$N$}}(u)\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq\delta.

∎

We can now define for an arbitrary positive integer JJ, the map ΓJ:BW1,∞​(0,δ2)×BW1,∞​(0,δ2)⟶W1,∞​(𝒟;ℝ)\Gamma\_{\text{$J$}}:B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta^{2})\times B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta^{2})\longrightarrow W^{1,\infty}(\mathcal{D};\mathbb{R}) by

|  |  |  |
| --- | --- | --- |
|  | ΓJ​(f0,wg)≔TN​N∘⋯∘TNN⏟J​times​(0)≕TNN[J]​(0).\Gamma\_{\text{$J$}}(f\_{0},w\_{g})\coloneqq\underbrace{T\_{NN}\circ\cdots\circ T\_{\text{$N$}\text{$N$}}}\_{J\;\text{\rm times}}(0)\eqqcolon T\_{\text{$N$}\text{$N$}}^{[\text{$J$}]}(0). |  |

###### Lemma A.5.

Let J≔⌈log⁡(1/ε)/log⁡(1/ρ)⌉∈ℕJ\coloneqq\lceil\log(1/\varepsilon)/\log(1/\rho)\rceil\in\mathbb{N}.
Then, there exists a constant C5>0C\_{5}>0 depending on pp, dd, 𝒟\mathcal{D}, γ\gamma, μ\mu, and λ\lambda such that for all (f0,g)∈BW1,∞​(0,δ2)×BW(d+3)/2,2​(0,δ2)(f\_{0},g)\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta^{2})\times B\_{W^{\text{$($}\text{$d$}\text{$+$}\text{$3$}\text{$)$}\text{$/$}\text{$2$},2}}(0,\delta^{2})

|  |  |  |
| --- | --- | --- |
|  | ‖Γ+​(f0,g)−ΓJ​(f0,wg)‖W1,∞​(𝒟)≤C5​ε.\big\|\Gamma^{\text{$+$}}(f\_{0},g)-\Gamma\_{\text{$J$}}(f\_{0},w\_{g})\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D})}\leq C\_{5}\varepsilon. |  |

###### Proof.

From [Section˜A.1.1](https://arxiv.org/html/2511.01125v1#A1.SS1.SSS1 "A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"), T:BW1,∞​(0,δ)⟶BW1,∞​(0,δ)T:B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta)\longrightarrow B\_{W^{1,\infty}}(0,\delta) is ρ\rho-contraction mapping, which implies that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖Γ+​(f0,g)−T[J]​(0)‖W1,∞​(𝒟;ℝ)=‖T[J]​(u)−T[J]​(0)‖W1,∞​(𝒟;ℝ)\displaystyle\big\|\Gamma^{\text{$+$}}(f\_{0},g)-T^{\text{$[$}\text{$J$}\text{$]$}}(0)\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}=\big\|T^{\text{$[$}\text{$J$}\text{$]$}}(u)-T^{\text{$[$}\text{$J$}\text{$]$}}(0)\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})} | ≲ρJ​‖u‖W1,∞​(𝒟;ℝ)≤ρJ​δ≲ε,\displaystyle\lesssim\rho^{J}\|u\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq\rho^{J}\delta\lesssim\varepsilon, |  | (A.14) |

where uu is the unique solution of ([A.4](https://arxiv.org/html/2511.01125v1#A1.E4 "Equation A.4 ‣ A.1.1 Well-posedness ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) in BW1,∞​(0,δ)B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta).
Next, we see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖T[J]​(0)−Γ​(f0,wg)‖W1,∞​(𝒟;ℝ)\displaystyle\big\|T^{\text{$[$}\text{$J$}\text{$]$}}(0)-\Gamma(f\_{0},w\_{g})\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})} | =‖T[J]​(0)−TNN[J]​(0)‖W1,∞​(𝒟;ℝ)\displaystyle=\big\|T^{\text{$[$}\text{$J$}\text{$]$}}(0)-T\_{\text{$N$}\text{$N$}}^{\text{$[$}\text{$J$}\text{$]$}}(0)\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑h=1J‖(T[J−h+1]∘TNN[h−1])​(0)−(T[J−h]∘TNN[h])​(0)‖W1,∞​(𝒟;ℝ)\displaystyle\leq\sum\_{h=1}^{\text{$J$}}\Big\|\big(T^{\text{$[$}\text{$J$}\text{$-$}h\text{$+$}1\text{$]$}}\circ T\_{\text{$N$}\text{$N$}}^{\text{$[$}h\text{$-$}1\text{$]$}}\big)(0)-\big(T^{\text{$[$}\text{$J$}\text{$-$}h\text{$]$}}\circ T\_{\text{$N$}\text{$N$}}^{\text{$[$}h\text{$]$}}\big)(0)\Big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑h=1JρJ−​h​‖(T∘TNN[h−1])​(0)−(TNN∘TNN[h−1])​(0)‖W1,∞​(𝒟;ℝ)\displaystyle\leq\sum\_{h=1}^{\text{$J$}}\rho^{\text{$J$}\text{$-$}h}\Big\|\big(T\circ T\_{\text{$N$}\text{$N$}}^{[h\text{$-$}1]}\big)(0)-\big(T\_{\text{$N$}\text{$N$}}\circ T\_{\text{$N$}\text{$N$}}^{[h\text{$-$}1]}\big)(0)\Big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑h=1JρJ−​h​‖T​(uh)−TNN​(uh)‖W1,∞​(𝒟;ℝ),\displaystyle=\sum\_{h=1}^{\text{$J$}}\rho^{\text{$J$}\text{$-$}h}\big\|T(u\_{h})-T\_{\text{$N$}\text{$N$}}(u\_{h})\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}, |  | (A.15) |

where, we see that, by [Section˜A.1.2](https://arxiv.org/html/2511.01125v1#A1.SS1.SSS2 "A.1.2 Proof of Theorem 3.11 ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")

|  |  |  |
| --- | --- | --- |
|  | uh≔TNN[h−1]​(0)∈BW1,∞​(0,δ).u\_{h}\coloneqq T\_{\text{$N$}\text{$N$}}^{[h\text{$-$}1]}(0)\in B\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}}(0,\delta). |  |

Note that we define TNN[0]≔IdT\_{\text{$N$}\text{$N$}}^{[0]}\coloneqq\mathrm{Id}. By [Section˜A.1.2](https://arxiv.org/html/2511.01125v1#A1.SS1.SSS2 "A.1.2 Proof of Theorem 3.11 ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"), we see that

|  |  |  |
| --- | --- | --- |
|  | ‖T​(u)−TNN​(u)‖W1,∞​(𝒟;ℝ)≤C4​ε,\displaystyle\big\|T(u)-T\_{\text{$N$}\text{$N$}}(u)\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq C\_{4}\varepsilon, |  |

which implies that with ([A.15](https://arxiv.org/html/2511.01125v1#A1.E15 "Equation A.15 ‣ A.1.2 Proof of Theorem 3.11 ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ‖T[J]​(0)−Γ​(f0,wg)‖W1,∞​(𝒟;ℝ)≤∑h=1JρJ−​h​C5​ε≤∑h=0∞ρh​C5​ε=C51−ρ​ε≲ε.\displaystyle\big\|T^{\text{$[$}\text{$J$}\text{$]$}}(0)-\Gamma(f\_{0},w\_{g})\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\leq\sum\_{h=1}^{\text{$J$}}\rho^{\text{$J$}\text{$-$}h}C\_{5}\varepsilon\leq\sum\_{h=0}^{\infty}\rho^{h}C\_{5}\varepsilon=\frac{C\_{5}}{1-\rho}\varepsilon\lesssim\varepsilon. |  | (A.16) |

Thus, by [Equations˜A.14](https://arxiv.org/html/2511.01125v1#A1.E14 "In A.1.2 Proof of Theorem 3.11 ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") and [A.16](https://arxiv.org/html/2511.01125v1#A1.E16 "Equation A.16 ‣ A.1.2 Proof of Theorem 3.11 ‣ A.1 Proof of Theorem 3.11 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"), we conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Γ+​(f0,g)−Γ​(f0,wg)‖W1,∞​(𝒟;ℝ)\displaystyle\big\|\Gamma^{\text{$+$}}(f\_{0},g)-\Gamma(f\_{0},w\_{g})\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})} | ≤‖Γ+​(f0,g)−T[J]​(0)‖W1,∞​(𝒟;ℝ)+‖T[J]​(0)−Γ​(f0,wg)‖W1,∞​(𝒟;ℝ)≲ε.\displaystyle\leq\big\|\Gamma^{\text{$+$}}(f\_{0},g)-T^{\text{$[$}\text{$J$}\text{$]$}}(0)\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}+\big\|T^{\text{$[$}\text{$J$}\text{$]$}}(0)-\Gamma(f\_{0},w\_{g})\big\|\_{W^{\text{$1$}\text{$,$}\text{$\infty$}}(\mathcal{D};\mathbb{R})}\lesssim\varepsilon. |  |

∎

Let us remind the reader that ΓJ\Gamma\_{\text{$J$}} is defined by

|  |  |  |
| --- | --- | --- |
|  | ΓJ​(f0,wg)=TNN∘⋯∘TNN⏟J​times​(0)=TNN[J]​(0).\Gamma\_{\text{$J$}}(f\_{0},w\_{g})=\underbrace{T\_{\text{$N$}\text{$N$}}\circ\cdots\circ T\_{\text{$N$}\text{$N$}}}\_{\text{$J$}\;\text{times}}(0)=T\_{\text{$N$}\text{$N$}}^{\text{$[$}\text{$J$}\text{$]$}}(0). |  |

where the operator TNNT\_{\text{$N$}\text{$N$}} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | TNN​(u)​(x)\displaystyle T\_{\text{$N$}\text{$N$}}(u)(x) | =∑h=2H∫𝒟kn​nh​(x,y)​(u​(y))h​dy−∫𝒟kn​n′​(x,y)​f0​(y)​dy+wg​(x)=∑h=2H∫𝒟kn​nh​(x,y)​(u​(y))h​dy+vf0,g​(x)\displaystyle=\sum\_{h=2}^{\text{$H$}}\int\_{\mathcal{D}}k\_{nn}^{h}(x,y)(u(y))^{h}\mathrm{d}y-\int\_{\mathcal{D}}k^{\prime}\_{nn}(x,y)f\_{0}(y)\mathrm{d}y+w\_{g}(x)=\sum\_{h=2}^{\text{$H$}}\int\_{\mathcal{D}}k\_{nn}^{h}(x,y)(u(y))^{h}\mathrm{d}y+v\_{f\_{0},g}(x) |  |

where

|  |  |  |
| --- | --- | --- |
|  | vf0,g​(x)≔−∫𝒟kn​n′​(x,y)​f0​(y)​dy+wg​(x)v\_{f\_{0},g}(x)\coloneqq-\int\_{\mathcal{D}}k^{\prime}\_{nn}(x,y)f\_{0}(y)\mathrm{d}y+w\_{g}(x) |  |

We see that ΓJ​(f0,wg)​(x)=vJ​(x)\Gamma\_{\text{$J$}}(f\_{0},w\_{g})(x)=v\_{\text{$J$}}(x)
where v0≔0v\_{0}\coloneqq 0 and

|  |  |  |
| --- | --- | --- |
|  | vj+1​(x)≔∑h=2H∫𝒟kn​nh​(x,y)​(vj​(y))h​dy+vf0,g​(x),j∈{0,…,J−1}.\displaystyle v\_{j+1}(x)\coloneqq\sum\_{h=2}^{\text{$H$}}\int\_{\mathcal{D}}k\_{nn}^{h}(x,y)(v\_{j}(y))^{h}\mathrm{d}y+v\_{f\_{0},g}(x),\;j\in\{0,\dots,J-1\}. |  |

We define

|  |  |  |
| --- | --- | --- |
|  | W(0)≔(0101)∈ℝ2×2,W^{(0)}\coloneqq\begin{pmatrix}0&1\\ 0&1\\ \end{pmatrix}\in\mathbb{R}^{2\times 2}, |  |

and let KN(0):W1,∞​(𝒟;ℝ)2⟶W1,∞​(𝒟;ℝ)2K^{(0)}\_{N}:W^{1,\infty}(\mathcal{D};\mathbb{R})^{2}\longrightarrow W^{1,\infty}(\mathcal{D};\mathbb{R})^{2} be defined by

|  |  |  |
| --- | --- | --- |
|  | (K(0)​(f0wg))​(x)≔∫𝒟kNN(0)​(x,y)​(f​(y)wg​(y))​dy,\bigg(K^{(0)}\begin{pmatrix}f\_{0}\\ w\_{g}\end{pmatrix}\bigg)(x)\coloneqq\int\_{\mathcal{D}}k^{(0)}\_{\text{$N$}\text{$N$}}(x,y)\begin{pmatrix}f(y)\\ w\_{g}(y)\end{pmatrix}\mathrm{d}y, |  |

where

|  |  |  |
| --- | --- | --- |
|  | kNN(0)​(x,y)≔(kNN′​(x,y)0kNN′​(x,y)0)∈ℝ2×2.k^{(0)}\_{\text{$N$}\text{$N$}}(x,y)\coloneqq\begin{pmatrix}k^{\prime}\_{\text{$N$}\text{$N$}}(x,y)&0\\ k^{\prime}\_{\text{$N$}\text{$N$}}(x,y)&0\\ \end{pmatrix}\in\mathbb{R}^{2\times 2}. |  |

We therefore compute

|  |  |  |
| --- | --- | --- |
|  | W(0)​(f0​(x)wg​(x))+(K(0)​(f0wg))​(x)=(vf0,g​(x)vf0,g​(x))=(vf0,g​(x)v1​(x)).W^{(0)}\begin{pmatrix}f\_{0}(x)\\ w\_{g}(x)\end{pmatrix}+\bigg(K^{(0)}\begin{pmatrix}f\_{0}\\ w\_{g}\end{pmatrix}\bigg)(x)=\begin{pmatrix}v\_{f\_{0},g}(x)\\ v\_{f\_{0},g}(x)\end{pmatrix}=\begin{pmatrix}v\_{f\_{0},g}(x)\\ v\_{1}(x)\end{pmatrix}. |  |

Next, we define FReQU:ℝ2⟶ℝHF\_{\text{${\rm ReQU}$}}:\mathbb{R}^{2}\longrightarrow\mathbb{R}^{H} by

|  |  |  |
| --- | --- | --- |
|  | FR​e​Q​U​(u)≔(u1(u2)2⋮(u2)H),u=(u1,u2)∈ℝ2,F\_{ReQU}(u)\coloneqq\begin{pmatrix}u\_{1}\\ (u\_{2})^{2}\\ \vdots\\ (u\_{2})^{H}\end{pmatrix},\quad u=(u\_{1},u\_{2})\in\mathbb{R}^{2}, |  |

which can have an exact implementation by a ReQU neural networks (see [Li, Tang, and Yu](https://arxiv.org/html/2511.01125v1#bib.bib59) [[59](https://arxiv.org/html/2511.01125v1#bib.bib59), Theorem 3.1]).

We define

|  |  |  |
| --- | --- | --- |
|  | W=(10⋯010⋯0)∈ℝ2×H,W=\begin{pmatrix}1&0&\cdots&0\\ 1&0&\cdots&0\end{pmatrix}\in\mathbb{R}^{2\times\text{$H$}}, |  |

and K:W1,∞​(𝒟;ℝ)H⟶W1,∞​(𝒟;ℝ)2K:W^{1,\infty}(\mathcal{D};\mathbb{R})^{\text{$H$}}\longrightarrow W^{1,\infty}(\mathcal{D};\mathbb{R})^{2}, for u=(u1,…,uH)∈W1,∞​(𝒟;ℝ)H+​1u=(u\_{1},...,u\_{H})\in W^{1,\infty}(\mathcal{D};\mathbb{R})^{\text{$H$}\text{$+$}1}

|  |  |  |
| --- | --- | --- |
|  | (K​u)​(x)≔∫𝒟kNN​(x,y)​u​(y)​dy=(0∑h=2H∫𝒟kn​nh​(x,y)​uh​(y)​dy),\displaystyle(Ku)(x)\coloneqq\int\_{\mathcal{D}}k\_{\text{$N$}\text{$N$}}(x,y)u(y)\mathrm{d}y=\begin{pmatrix}0\\[5.0pt] \displaystyle\sum\_{h=2}^{\text{$H$}}\int\_{\mathcal{D}}k\_{nn}^{h}(x,y)u\_{h}(y)\mathrm{d}y\end{pmatrix}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | kN​N​(x,y)≔(00⋯00kn​n2​(x,y)⋯kn​nH​(x,y))∈ℝ2×H,k\_{NN}(x,y)\coloneqq\begin{pmatrix}0&0&\cdots&0\\ 0&k\_{nn}^{2}(x,y)&\cdots&k\_{nn}^{\text{$H$}}(x,y)\end{pmatrix}\in\mathbb{R}^{2\times\text{$H$}}, |  |

Then, we have that for j∈{1,…,J−1}j\in\{1,...,J-1\}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ((W+K)∘FReQU​(vf0,gvj))​(x)=W​(vf0,g​(x)(vj​(x))2⋮(vj​(x))H)+K​(vf0,g(vj)2⋮(vj)H)​(x)\displaystyle\bigg((W+K)\circ F\_{\text{$\rm ReQU$}}\begin{pmatrix}v\_{f\_{0},g}\\ v\_{j}\end{pmatrix}\bigg)(x)=W\begin{pmatrix}v\_{f\_{0},g}(x)\\ (v\_{j}(x))^{2}\\ \vdots\\ (v\_{j}(x))^{\text{$H$}}\end{pmatrix}+K\begin{pmatrix}v\_{f\_{0},g}\\ (v\_{j})^{2}\\ \vdots\\ (v\_{j})^{\text{$H$}}\end{pmatrix}(x) | =(vf0,g​(x)∑h=2H∫𝒟kn​nh​(x,y)​(vj​(y))h​dy+vf0,g​(x))\displaystyle=\begin{pmatrix}v\_{f\_{0},g}(x)\\ \displaystyle\sum\_{h=2}^{\text{$H$}}\int\_{\mathcal{D}}k\_{nn}^{h}(x,y)(v\_{j}(y))^{h}\mathrm{d}y+v\_{f\_{0},g}(x)\end{pmatrix} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(vf0,g​(x)vj+1​(x)).\displaystyle=\begin{pmatrix}v\_{f\_{0},g}(x)\\ v\_{j+1}(x)\end{pmatrix}. |  |

Denoting W′≔(0,1)∈ℝ1×2W^{\prime}\coloneqq(0,1)\in\mathbb{R}^{1\times 2}, we finally obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΓJ​(f,wg)\displaystyle\Gamma\_{\text{$J$}}(f,w\_{g}) | =W′∘((W+K)∘FReQU∘⋯∘(W+K)∘FReQU⏟J−​1​times)∘(W(0)+K(0))​(fwg).\displaystyle=W^{\prime}\circ\Big(\underbrace{(W+K)\circ F\_{\text{$\rm ReQU$}}\circ\cdots\circ(W+K)\circ F\_{\text{$\rm ReQU$}}}\_{\text{$J$}\text{$-$}1\;\text{times}}\Big)\circ\big(W^{(0)}+K^{(0)}\big)\begin{pmatrix}f\\ w\_{g}\end{pmatrix}. |  |

Since the ReQU network can be represented by the KANs network [[92](https://arxiv.org/html/2511.01125v1#bib.bib92), Theorem 3.2], we have, by the above construction,

|  |  |  |
| --- | --- | --- |
|  | Γ∈𝒩​𝒪L^,W^L,W,I,α​(W1,∞​(𝒟;ℝ)2,W1,∞​(𝒟;ℝ)).\Gamma\in\mathcal{NO}^{\text{$L$},\text{$W$},\text{$I$},\alpha}\_{\hat{\text{$L$}},\hat{\text{$W$}}}(W^{1,\infty}(\mathcal{D};\mathbb{R})^{2},W^{1,\infty}(\mathcal{D};\mathbb{R})). |  |

Moreover, the depth L=L​(Γ)L=L(\Gamma) and width W=W​(Γ)W=W(\Gamma) of the neural operator Γ\Gamma can be estimated via

|  |  |  |
| --- | --- | --- |
|  | L​(Γ)≲J≤C​log⁡(ε−1),W​(Γ)≲H≤C.\displaystyle L(\Gamma)\lesssim J\leq C\log(\varepsilon^{-1}),\;W(\Gamma)\lesssim H\leq C. |  |

This concludes our proof of Theorem [3.11](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem11 "Theorem 3.11 (Exponential approximation rates: solution operator to the elliptic problem). ‣ 3.3.1 Semi-linear elliptic PDE ‣ 3.3 Feasible rates ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"); where, again, α=s\alpha=s and I≔⌈α⌉I\coloneqq\lceil\alpha\rceil.

### A.2 Proof of Theorem [3.7](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem7 "Theorem 3.7 (Approximability of the perturbation-to-solution map). ‣ 3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")

The proof of our second main result relies on some tools from multi-resolution analysis and the wavelet theory of Besov spaces. We, therefore, now overview the necessary material.

#### A.2.1 Additional background

In what follows, we use S​(ℝd)S(\mathbb{R}^{d}) to denote the Schwartz space on ℝd\mathbb{R}^{d} and consider the space of distributions defined as the topological dual D​(𝒟)′D(\mathcal{D})^{\prime}. We define the restriction operator sending any distribution g∈S​(ℝd)g\in S(\mathbb{R}^{d}) to g|𝒟∈D​(𝒟)′g|\_{\mathcal{D}}\in D(\mathcal{D})^{\prime} defined by restriction of its action to test functions φ∈D​(𝒟)\varphi\in D(\mathcal{D}) *i.e.*

|  |  |  |
| --- | --- | --- |
|  | g|𝒟​(φ)≔g​(φ).g|\_{\mathcal{D}}(\varphi)\coloneqq g(\varphi). |  |

#### A.2.2 From wavelet para-bases to Besov spaces on Euclidean spaces

Fix u∈ℕu\in\mathbb{N} and (σS,σW)∈Cu​(ℝ)×Cu​(ℝ)(\sigma\_{\text{$S$}},\sigma\_{\text{$W$}})\in C^{u}(\mathbb{R})\times C^{u}(\mathbb{\mathbb{R}})
satisfy [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"); that is to say that σS\sigma\_{\text{$S$}} and σW\sigma\_{\text{$W$}} are Daubechies father (also known as scaling function) and mother wavelets (also known as wavelet function) respectively, in the sense of [[18](https://arxiv.org/html/2511.01125v1#bib.bib18)].
For each j∈ℕj\in\mathbb{N} define the sets

|  |  |  |
| --- | --- | --- |
|  | Gj≔{{S,W}d, if ​j=0,{S,W}d⁣⋆≔{S,W}d∖{(S,…,S)}, if ​j>0.G^{j}\coloneqq\begin{cases}\{S,W\}^{d},\mbox{ if }j=0,\\ \{S,W\}^{d\star}\coloneqq\{S,W\}^{d}\setminus\{(S,\dots,S)\},\mbox{ if }j>0.\end{cases} |  |

Now, for each ‘scale’ j∈ℕj\in\mathbb{N}, location m∈ℤdm\in\mathbb{Z}^{d}, and each G∈GjG\in G^{j}, define the tensorised Daubechies wavelet by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ~G,mj​(x)≔2j​d/2​∏i=1dσGi​(2j​xi−mi),x∈ℝd,\widetilde{\Psi}\_{G,m}^{j}(x)\coloneqq 2^{jd/2}\prod\_{i=1}^{d}\sigma\_{\text{$G$}\_{\text{$i$}}}\big(2^{j}x\_{i}-m\_{i}\big),\;x\in\mathbb{R}^{d}, |  | (A.17) |

where G≔(G1,…,Gd)G\coloneqq(G\_{1},\dots,G\_{d}).
Let 𝒪≔{(j,G,m):j∈ℕ,G∈Gj,m∈ℤd}\mathcal{O}\coloneqq\{(j,G,m):j\in\mathbb{N},\;G\in G^{j},\;m\in\mathbb{Z}^{d}\} and for each (j,G,m)∈𝒪(j,G,m)\in\mathcal{O} let

|  |  |  |
| --- | --- | --- |
|  | 1(βG,mj)2≔∫ℝd(Ψ~G,mj​(x))2​dx,and​ΨG,mj≔1βG,mj​Ψ~G,mj​(x),x∈ℝd.\frac{1}{(\beta\_{\text{$G$},m}^{j})^{2}}\coloneqq\int\_{\mathbb{R}^{\text{$d$}}}\,\big(\tilde{\Psi}\_{\text{$G$},m}^{j}(x)\big)^{2}\mathrm{d}x,\mbox{\rm and}\;\Psi\_{\text{$G$},m}^{j}\coloneqq\frac{1}{\beta\_{\text{$G$},m}^{j}}\tilde{\Psi}\_{\text{$G$},m}^{j}(x),\;x\in\mathbb{R}^{d}. |  |

Then, as discussed on [Triebel](https://arxiv.org/html/2511.01125v1#bib.bib90) [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), page 13], for any u∈ℕu\in\mathbb{N} we have that (ΨG,mj)(j,G,m)∈𝒪(\Psi\_{\text{$G$},m}^{j})\_{(j,\text{$G$},m)\in\mathcal{O}} is an orthonormal basis of L2​(ℝd)L^{2}(\mathbb{R}^{d}), and for every f∈L2​(ℝd)f\in L^{2}(\mathbb{R}^{d})

|  |  |  |  |
| --- | --- | --- | --- |
|  | f=∑j∈ℕ∑G∈Gj∑m∈ℤdλG,mj​2−j​d/2​ΨG,mj,where​λG,mj≔2j​d/2​∫ℝdf​(x)​ΨG,mj​(x)​dx,f=\sum\_{j\in\mathbb{N}}\sum\_{G\in G^{\text{$j$}}}\sum\_{m\in\mathbb{Z}^{\text{$d$}}}\,\lambda\_{\text{$G$},m}^{j}2^{\text{$-$}jd/2}\Psi\_{\text{$G$},m}^{j},\;\mbox{\rm where}\;\lambda\_{\text{$G$},m}^{j}\coloneqq 2^{jd/2}\int\_{\mathbb{R}^{\text{$d$}}}\,f(x)\Psi\_{\text{$G$},m}^{j}(x)\mathrm{d}x, |  | (A.18) |

where the series converge in L2​(ℝd)L^{2}(\mathbb{R}^{d}).

A key properties of Besov spaces, from the approximation theoretic lense, is that they are entirely determined by the decay/convergence rates of the sequences (λG,mj)(j,G,m)∈𝒪(\lambda\_{\text{$G$},m}^{j})\_{(j,\text{$G$},m)\in\mathcal{O}}, defined in ([A.18](https://arxiv.org/html/2511.01125v1#A1.E18 "Equation A.18 ‣ A.2.2 From wavelet para-bases to Besov spaces on Euclidean spaces ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")). Indeed, for (q,r)∈(0,+∞]2(q,r)\in(0,+\infty]^{2} and s∈ℝs\in\mathbb{R}, if

|  |  |  |  |
| --- | --- | --- | --- |
|  | u>max⁡{s,σq−s},where​σq≔d​max⁡{0,1q−1},u>\max\{s,\sigma\_{q}-s\},\;\mbox{where}\;\sigma\_{q}\coloneqq d\max\bigg\{0,\frac{1}{q}-1\bigg\}, |  | (A.19) |

as shown in [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Theorem 1.20], f∈S​(ℝd)′f\in S(\mathbb{R}^{d})^{\prime} belongs to the Besov space B¯q,rs​(ℝd)\overline{B}\_{q,r}^{s}(\mathbb{R}^{d}) if and only if the sequence λ⋅≔(λG,mj)(j,G,m)∈𝒪\lambda\_{\cdot}\coloneqq(\lambda\_{\text{$G$},m}^{j})\_{(j,\text{$G$},m)\in\mathcal{O}}, defined by([A.18](https://arxiv.org/html/2511.01125v1#A1.E18 "Equation A.18 ‣ A.2.2 From wavelet para-bases to Besov spaces on Euclidean spaces ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖λ⋅‖bq,rsr≔∑j=0∞2j​r​(s−d/q)​∑G∈Gj(∑m∈ℤd|λG,mj|q)r/q<∞,\|\lambda\_{\cdot}\|\_{b\_{\text{$q$}\text{$,$}\text{$r$}}^{\text{$s$}}}^{r}\coloneqq\sum\_{j=0}^{\infty}2^{jr(s-d/q)}\sum\_{G\in G^{\text{$j$}}}\,\Bigg(\sum\_{m\in\mathbb{Z}^{\text{$d$}}}|\lambda\_{\text{$G$},m}^{j}|^{q}\Bigg)^{r/q}<\infty, |  | (A.20) |

with the usual modifications to the left-hand side of ([A.20](https://arxiv.org/html/2511.01125v1#A1.E20 "Equation A.20 ‣ A.2.2 From wavelet para-bases to Besov spaces on Euclidean spaces ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) if qq or rr are infinite. Additionally, the map f⟼(2j​d/2​⟨f,ΨG,mj⟩L2​(ℝd))(j,G,m)∈𝒪f\longmapsto(2^{jd/2}\langle f,\Psi\_{\text{$G$},m}^{j}\rangle\_{L^{\text{$2$}}(\mathbb{R}^{\text{$d$}})})\_{(j,\text{$G$},m)\in\mathcal{O}} is a bi-Lipschitz linear isomorphism between Bq,rs​(ℝd)B\_{q,r}^{s}(\mathbb{R}^{d}) and the (quasi–)Banach space bq,rsb\_{q,r}^{s} of all sequences for which the (quasi-)norm ∥⋅∥bq,rs\|\cdot\|\_{b\_{\text{$q$}\text{$,$}\text{$r$}}^{\text{$s$}}} is finite.

#### A.2.3 Besov spaces on domains

We begin with the definition of Besov spaces on any domain (proper open set with non-empty interior) O⊂ℝdO\subset\mathbb{R}^{d}, with closure O¯\overline{O}. We write 𝒟​(O)\mathcal{D}(O) for the space of complex-valued compactly supported smooth (test) functions on OO, topologized with the canonical (Limit of Fréchet) LF–topology. Its dual space D′​(O)D^{\prime}(O) is the space of distributions on OO, and a distribution f∈D′​(O)f\in D^{\prime}(O) is said to be supported on a set A⊆OA\subseteq O if f​(φ)=0f(\varphi)=0 for every φ∈𝒟​(O)\varphi\in\mathcal{D}(O) such that φ​(x)=0\varphi(x)=0 for all x∉Ax\not\in A; the support supp​(f)\mathrm{supp}(f) is the smallest closed set KK with this property. For instance, if x∈Ox\in O then the Dirac distribution δx​(φ)≔φ​(x)\delta\_{x}(\varphi)\coloneqq\varphi(x) has support supp​(δx)={x}\mathrm{supp}(\delta\_{x})=\{x\}, see [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Chapter 2, page 28] for further details and notation.
We now define the Besov (quasi-Banach) spaces on 𝒟\mathcal{D}.

###### Definition A.6 (Besov spaces on domains).

Let 𝒟\mathcal{D} be a domain, (q,r)∈(0,+∞]2(q,r)\in(0,+\infty]^{2}, and s∈ℝs\in\mathbb{R}. The Besov space B~q,rs​(𝒟¯)\widetilde{B}\_{q,r}^{s}(\overline{\mathcal{D}}) consists of all f∈Bq,rs​(ℝd)f\in B\_{q,r}^{s}(\mathbb{R}^{d}) supported in the closure 𝒟¯\overline{\mathcal{D}} and B~q,rs​(𝒟)\widetilde{B}\_{q,r}^{s}(\mathcal{D}) consists of all distributions f∈D​(𝒟)′f\in D(\mathcal{D})^{\prime} for which there exists some g∈Bq,rs​(𝒟¯)g\in B\_{q,r}^{s}(\overline{\mathcal{D}}) such that f=g|𝒟f=g|\_{\mathcal{D}}.
In either case, 𝔇∈{𝒟,𝒟¯}\mathfrak{D}\in\{\mathcal{D},\bar{\mathcal{D}}\}, we equip B~q,rs​(𝔇)\widetilde{B}\_{q,r}^{s}(\mathfrak{D}) with the interpolation norm

|  |  |  |
| --- | --- | --- |
|  | ∥f∥B~q,rs​(𝔇)≔inf{∥g∥Bq,rs​(ℝd):g∈B~q,rs(𝒟¯),f=g|𝔇}.\|f\|\_{\tilde{B}\_{\text{$q$}\text{$,$}\text{$r$}}^{\text{$s$}}(\mathfrak{D})}\coloneqq\inf\Big\{\|g\|\_{B\_{\text{$q$}\text{$,$}\text{$r$}}^{\text{$s$}}(\mathbb{R}^{\text{$d$}})}:g\in\widetilde{B}\_{q,r}^{s}(\overline{\mathcal{D}}),\;f=g|\_{{\mathfrak{D}}}\Big\}. |  |

We define the Besov spaces B¯q,rs​(𝒟)\overline{B}\_{q,r}^{s}(\mathcal{D}) as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | B¯q,rs​(𝒟)≔{B~q,rs​(𝒟),if​ 0<q≤∞, 0<r≤∞,s>σq,Bq,r0​(𝒟),if​ 1<q<∞, 0<r≤∞,s=0,Bq,rs​(𝒟),if​ 0<q≤∞, 0<r≤∞,s<0.\overline{B}^{s}\_{q,r}(\mathcal{D})\coloneqq\begin{cases}\widetilde{B}^{s}\_{q,r}(\mathcal{D}),\;\text{\rm if}\;0<q\leq\infty,\;0<r\leq\infty,\;s>\sigma\_{q},\\[5.0pt] B^{0}\_{q,r}(\mathcal{D}),\;\text{\rm if}\;1<q<\infty,\;0<r\leq\infty,\;s=0,\\[5.0pt] B^{s}\_{q,r}(\mathcal{D}),\;\text{\rm if}\;0<q\leq\infty,\;0<r\leq\infty,\;s<0.\end{cases} |  | (A.21) |

Following [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Section 3], we now construct wavelet systems on arbitrary domains (open subsets Ω⊂ℝn\Omega\subset\mathbb{R}^{n}) using Whitney decompositions; an object which acts almost as a leitmotif in analysis from our PDE problems to fundamental result in the geometry of functions spaces [[27](https://arxiv.org/html/2511.01125v1#bib.bib27), [28](https://arxiv.org/html/2511.01125v1#bib.bib28)].
The idea is to partition Ω\Omega into dyadic cubes whose sizes adapt to the distance from the boundary, and then build localized wavelet bases on these cubes—maintaining the regularity and cancellation properties of classical ℝn\mathbb{R}^{n} wavelets while conforming to the geometry of Ω\Omega.

These spaces can themselves be characterized in a similar way using compactly supported Daubechies wavelets. We fix a so-called approximate lattice ℤ𝒟⊂𝒟\mathbb{Z}\_{\mathcal{D}}\subset\mathcal{D} consisting of points ℤ𝒟=(xrj)(j,k)∈ℕ×{1,…,Nj}\mathbb{Z}\_{\mathcal{D}}=(x\_{r}^{j})\_{(j,k)\in\mathbb{N}\times\{1,\dots,N\_{\text{$j$}}\}} where, for each j∈ℕj\in\mathbb{N}, Nj∈ℕ¯≔ℕ∪{∞}N\_{j}\in\overline{\mathbb{N}}\coloneqq\mathbb{N}\cup\{\infty\} for which there exist positive constants c1c\_{1}, c2c\_{2}, c3c\_{3} satisfying the approximate ‘lattice separation condition’ at any scale j∈ℕj\in\mathbb{N}

|  |  |  |  |
| --- | --- | --- | --- |
|  | |xrj−xr′j|≥c12j\big|x\_{r}^{j}-x\_{r^{\text{$\prime$}}}^{j}\big|\geq\frac{c\_{1}}{2^{j}} |  | (A.22) |

and the separation from the ‘boundary condition’ at scale j∈ℕj\in\mathbb{N}

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf{z∈ℝd:‖z−xrj‖≤c2/2j}infu∈∂𝒟‖z−u‖≥c32j.\inf\_{\{z\in\mathbb{R}^{\text{$d$}}:\|z-x\_{\text{$r$}}^{\text{$j$}}\|\leq c\_{\text{$2$}}/2^{\text{$j$}}\}}\;\inf\_{u\in\partial\mathcal{D}}\|z-u\|\geq\frac{c\_{3}}{2^{j}}. |  | (A.23) |

Clearly the constants c1c\_{1}, c2c\_{2}, and c3c\_{3} may be chosen to guarantee the existence of such a ℤ𝒟\mathbb{Z}\_{\mathcal{D}} for any domain 𝒟\mathcal{D}. Intuitively, ℤ𝒟\mathbb{Z}\_{\mathcal{D}} acts precisely as the dyadic lattices ⋃j∈ℕ2−j​ℤd\bigcup\_{j\in\mathbb{N}}2^{\text{$-$}j}\mathbb{Z}^{d} does in ℝd\mathbb{R}^{d} but is contained entirely within 𝒟\mathcal{D} and condition ([A.22](https://arxiv.org/html/2511.01125v1#A1.E22 "Equation A.22 ‣ A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) vacuously holds when 𝒟\mathcal{D} is replaced by the Euclidean space.

For any L∈ℕL\in\mathbb{N}, to be specified retroactively, we denote σSL(⋅)≔σS(2L⋅)\sigma\_{\text{$S$}}^{\text{$L$}}(\cdot)\coloneqq\sigma\_{\text{$S$}}(2^{\text{$L$}}\cdot), σWL(⋅)≔σW(2L⋅)\sigma\_{\text{$W$}}^{\text{$L$}}(\cdot)\coloneqq\sigma\_{\text{$W$}}(2^{\text{$L$}}\cdot), and ΨG,mj,L≔ΨG,mj(2L⋅)\Psi\_{\text{$G$},m}^{j,\text{$L$}}\coloneqq\Psi\_{\text{$G$},m}^{j}(2^{\text{$L$}}\cdot) for each (j,G,m)∈𝒪(j,G,m)\in\mathcal{O}. In other words, the factor LL rescales our setup and we will choose it so that our problem is properly ‘shrunk’ within our domain and aligned to the approximate lattice ℤ𝒟\mathbb{Z}\_{\mathcal{D}}.

We are now ready to define wavelet classes tailored to general domains; we follow the terminology in [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Definition 2.4], the existence of which is known (see *e.g.* [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Theorem 2.33]).

###### Definition A.7 (uu-wavelets).

Let 𝒟\mathcal{D} be an arbitrary domain in ℝn\mathbb{R}^{n} with 𝒟≠ℝn\mathcal{D}\neq\mathbb{R}^{n} and let ℤ𝒟\mathbb{Z}\_{\mathcal{D}} ads well as L∈ℕL\in\mathbb{N} and u∈ℕu\in\mathbb{N} be as above. Let K∈ℕK\in\mathbb{N}, D>0D>0 and c4>0c\_{4}>0. Then, consider a sub-family of {ΨG,mj:j∈ℕ+,G∈Gj,m∈ℤ𝒟}\{\Psi\_{G,m}^{j}:\,j\in\mathbb{N}\_{+},\,G\in G^{j},\,m\in\mathbb{Z}\_{\mathcal{D}}\}

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Φrj:j∈ℕ;r∈{1,…,Nj}},where​Nj∈ℕ¯.\big\{\Phi\_{r}^{j}:j\in\mathbb{N};r\in\{1,\ldots,N\_{j}\}\big\},\;\text{\rm where}\;N\_{j}\in\overline{\mathbb{N}}. |  | (A.24) |

satisfying: supp​(Φrj)⊂Bℝd​(xrj,c2​2−j)\mathrm{supp}(\Phi\_{r}^{j})\subset B\_{\mathbb{R}^{d}}\big(x\_{r}^{j},c\_{2}2^{-j}\big), j∈ℕj\in\mathbb{N},
is called a uu-wavelet system ((with respect to 𝒟)\mathcal{D}) if it consists of the following three possible types of functions

1. (i)(i)

   basic wavelets:
   Φr0=ΨG,m0,L\Phi\_{r}^{0}=\Psi\_{\text{$G$},m}^{0,\text{$L$}} for some G∈{S,W}dG\in\{S,W\}^{d}, and m∈ℤd;m\in\mathbb{Z}^{d};
2. (i​i)(ii)

   interior wavelets:
   Φrj=ΨG,mj,L\Phi\_{r}^{j}=\Psi\_{\text{$G$},m}^{j,\text{$L$}} for each j∈ℕj\in\mathbb{N}, and m∈ℤ𝒟m\in\mathbb{Z}\_{\mathcal{D}}
   such that dist​(xrj,𝒟¯)≥c4​2−j,\mathrm{dist}(x\_{r}^{j},\bar{\mathcal{D}})\geq c\_{4}2^{\text{$-$}j},
   for some G∈{S,W}d⁣⋆;G\in\{S,W\}^{d\star};
3. (i​i​i)(iii)

   boundary wavelets:
   Φrj=∑{m′∈ℤd:‖m−m′‖≤K}dm,m′j​ΨF~,m′j,L\Phi\_{r}^{j}=\sum\_{\{m^{\text{$\prime$}}\in\mathbb{Z}^{\text{$d$}}:\|m-m^{\text{$\prime$}}\|\leq K\}}d\_{m,m^{\text{$\prime$}}}^{j}\Psi\_{\tilde{\text{$F$}},m^{\text{$\prime$}}}^{j,\text{$L$}}, for each j∈ℕj\in\mathbb{N} for which dist​(xrj,Γ)<c4​2−j,\mathrm{dist}(x\_{r}^{j},\Gamma)<c\_{4}2^{\text{$-$}j},
   for some m≔m​(j,r)∈ℤdm\coloneqq m(j,r)\in\mathbb{Z}^{d} and dm,m′j∈ℝd\_{m,m^{\text{$\prime$}}}^{j}\in\mathbb{R} with

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∑{m′∈ℤd:‖m−m′‖≤K}|dm,m′j|≤D,and​supp​(ΨF~,m′j,L)⊂B​(xrj,c2​2−j).\sum\_{\{m^{\text{$\prime$}}\in\mathbb{Z}^{\text{$d$}}:\|m-m^{\text{$\prime$}}\|\leq K\}}|d\_{m,m^{\text{$\prime$}}}^{j}|\leq D,\;\text{\rm and}\;\mathrm{supp}\big(\Psi\_{\tilde{\text{$F$}},m^{\text{$\prime$}}}^{j,\text{$L$}}\big)\subset B(x\_{r}^{j},c\_{2}2^{\text{$-$}j}). |  | (A.25) |

We may now adapt the definition of the sequence spaces bq,rsb\_{q,r}^{s}, given in ([A.20](https://arxiv.org/html/2511.01125v1#A1.E20 "Equation A.20 ‣ A.2.2 From wavelet para-bases to Besov spaces on Euclidean spaces ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), to suit the approximate lattice ℤ𝒟\mathbb{Z}\_{\mathcal{D}}, and thus the domain 𝒟\mathcal{D}.

###### Definition A.8 (Sequence space bq,rsb\_{q,r}^{s}).

Let 𝒟\mathcal{D} be an arbitrary domain in ℝn\mathbb{R}^{n} with 𝒟≠ℝn\mathcal{D}\neq\mathbb{R}^{n}, let ℤ𝒟\mathbb{Z}\_{\mathcal{D}} be as above, s∈ℝs\in\mathbb{R}, and (q,r)∈(o,∞]2(q,r)\in(o,\infty]^{2}. Then bq,rs​(ℤ𝒟)b^{s}\_{q,r}(\mathbb{Z}\_{\mathcal{D}}) is the collection of all sequences

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ≔{λrj∈ℂ:j∈ℕ,r∈{1,…,Nj}},for some​Nj∈ℕ¯,\lambda\coloneqq\big\{\lambda\_{r}^{j}\in\mathbb{C}:j\in\mathbb{N},\;r\in\{1,\ldots,N\_{j}\}\big\},\;\text{\rm for some}\;N\_{j}\in\overline{\mathbb{N}}, |  | (A.26) |

such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖λ‖bq,rs​(ℤ𝒟)q≔∑j=0∞2j​(s−n/q)​r​(∑k=1Nj|λkj|q)r/q<∞.\|\lambda\|\_{b^{\text{$s$}}\_{\text{$q$}\text{$,$}\text{$r$}}(\mathbb{Z}\_{\text{$\mathcal{D}$}})}^{q}\coloneqq\sum\_{j=0}^{\infty}2^{j(s\text{$-$}n/q)r}\Bigg(\sum\_{k=1}^{N\_{\text{$j$}}}|\lambda\_{k}^{j}|^{q}\Bigg)^{r/q}<\infty. |  | (A.27) |

As we will see shortly, the wavelet system in ([A.24](https://arxiv.org/html/2511.01125v1#A1.E24 "Equation A.24 ‣ A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) is a Schauder basis for several Besov spaces on domains, provided these domains possess a basic level of generic ‘thickness’ and regularity of their boundaries. We begin by first noting the relationship between the Besov sequence and function spaces, with the same indices, if the domain has a regular enough boundary.

A domain 𝒟⊆ℝd\mathcal{D}\subseteq\mathbb{R}^{d} is said to be special Lipschitz if there exists a Lipschitz-continuous map β:ℝd−1⟶ℝ\beta:\mathbb{R}^{d\text{$-$}1}\longrightarrow\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | 𝒟={(x~,xd)∈ℝd−1×ℝ:β​(x)<xd}.\mathcal{D}=\big\{(\tilde{x},x\_{d})\in\mathbb{R}^{d\text{$-$}1}\times\mathbb{R}:\,\beta(x)<x\_{d}\big\}. |  |

A bounded Lipschitz domain 𝒟⊂ℝd\mathcal{D}\subset\mathbb{R}^{d} is a bounded domain 𝒟\mathcal{D} for which there exists a finite number of open balls (B1,…,BN)(B\_{1},\dots,B\_{N}), for some N∈ℕ⋆N\in\mathbb{N}^{\star}, where for n∈{1,…,N}n\in\{1,\dots,N\} we have

|  |  |  |
| --- | --- | --- |
|  | Bn≔{x∈ℝd:‖x−x(n)‖<r(n)},for some​x(n)∈∂𝒟,and some​r(n)>0,B\_{n}\coloneqq\big\{x\in\mathbb{R}^{d}:\|x-x^{(n)}\|<r^{(n)}\big\},\;\text{\rm for some}\;x^{(n)}\in\partial\mathcal{D},\;\text{\rm and some}\;r^{(n)}>0, |  |

such that (Bn)n∈{1,…,N}(B\_{n})\_{n\in\{1,\dots,N\}} is a cover of ∂𝒟\partial\mathcal{D}, and there exist rotations of special Lipschitz domains (𝒟1,…,𝒟N)⊆(ℝd)N(\mathcal{D}\_{1},\dots,\mathcal{D}\_{N})\subseteq(\mathbb{R}^{d})^{N} for which

|  |  |  |
| --- | --- | --- |
|  | Bn∩𝒟=Bn∩𝒟n,n∈{1,…,N}.B\_{n}\cap\mathcal{D}=B\_{n}\cap\mathcal{D}\_{n},\;n\in\{1,\dots,N\}. |  |

Now, given any domain with Lipschitz boundary, we may characterise the inclusion of any square-integrable function into a wide array of Besov spaces depending on its associated sequence λ\lambda belonging to the ‘little Besov’ sequence space with the same indices. The following result is [[89](https://arxiv.org/html/2511.01125v1#bib.bib89), Corollary 4.28].

###### Lemma A.9 (Wavelet para–bases in Besov and Triebel–Lizorkin spaces on bounded Lipschitz domains).

Fix (q,r)∈(1,∞)2(q,r)\in(1,\infty)^{2}. For K>0K>0 small enough, if 5​d/2<K5d/2<K and s∈(−K,K)s\in(-K,K) then f∈𝒟​(𝒟)′f\in\mathcal{D}(\mathcal{D})^{\prime} belongs to B¯q,rs​(𝒟)\overline{B}\_{q,r}^{s}(\mathcal{D}) ((resp. F¯q,rs(𝒟))\overline{F}\_{q,r}^{s}(\mathcal{D})) if and only if admits the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | f=∑(j,G,m)∈S𝒟λG,mj​2−j​d/2​ΨG,mj,f=\sum\_{(j,\text{$G$},m)\in S^{\text{$\mathcal{D}$}}}\lambda\_{\text{$G$},m}^{j}2^{\text{$-$}jd/2}\Psi\_{\text{$G$},m}^{j}, |  | (A.28) |

and the following
holds

|  |  |  |
| --- | --- | --- |
|  | ‖(2j​(s−d/q)​‖(λG,mj)(G,m)∈Sj𝒟‖ℓq)j∈ℕ‖ℓp<∞.\Big\|\big(2^{j(s\text{$-$}d/q)}\big\|(\lambda\_{\text{$G$},m}^{j})\_{(\text{$G$},m)\in S^{\text{$\mathcal{D}$}}\_{\text{$j$}}}\big\|\_{\ell^{q}}\big)\_{j\in\mathbb{N}}\Big\|\_{\ell^{p}}<\infty. |  |

In what follows, given any f∈B¯q,rsf\in\bar{B}\_{q,r}^{s} we write λ​(f)≔(λG,mj)j,G,m∈S𝒟\lambda(f)\coloneqq(\lambda\_{\text{$G$},m}^{j})\_{j,G,m\in S^{\mathcal{D}}} for the sequence defined in ([A.28](https://arxiv.org/html/2511.01125v1#A1.E28 "Equation A.28 ‣ A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")); provided that it is unique. We denote the linear map f↦λ​(f)f\mapsto\lambda(f) by II.

[Section˜A.2.3](https://arxiv.org/html/2511.01125v1#A1.SS2.SSS3 "A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") does not guarantee that the wavelet expansions themselves are uniquely determined. In general, these wavelet ‘bases’ are only frames. However, the next result shows that this is not necessarily the case for EE-thick domains.

We say that a domain is exterior thick, or EE-thick for short, if there are constants 0<cL≤cU0<c\_{\text{$L$}}\leq c\_{\text{$U$}} and j0≥0j\_{0}\geq 0 such that for every j∈ℕj\in\mathbb{N} with j≥j0,j\geq j\_{0}, there is a dd-dimensional ‘interior’ cube Q⊂𝒟Q\subset\mathcal{D} with side-length

|  |  |  |
| --- | --- | --- |
|  | cL​2−j≤max⁡{ℓ​(Q),supz∈Qiinfu∈∂𝒟‖z−u‖}≤cU​2−jc\_{\text{$L$}}2^{\text{$-$}j}\leq\max\bigg\{\ell(Q),\sup\_{z\in Q^{\text{$i$}}}\inf\_{u\in\partial\mathcal{D}}\|z-u\|\bigg\}\leq c\_{\text{$U$}}2^{\text{$-$}j} |  |

where QiQ^{i} denotes the interior of any cube QQ in the norm relative topology on 𝒟\mathcal{D} and ℓ​(Q)\ell(Q) denotes its side-length; i.e. ℓ​(Q)≔supx,y∈Q‖x−y‖∞\ell(Q)\coloneqq\sup\_{x,y\in Q}\,\|x-y\|\_{\infty}; where ∥⋅∥∞\|\cdot\|\_{\infty} denotes the ∞\infty-norm on ℝd\mathbb{R}^{d}.
In the case of a thick exterior domain, we obtain a Schauder basis using our uu-wavelet expansion, see [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Theorem 3.13 (ii)].

###### Theorem A.10 (Wavelet-based Schauder bases).

Let 𝒟\mathcal{D} be an EE-thick domain in ℝd\mathbb{R}^{d}. Define for u∈ℕ⋆u\in\mathbb{N}^{\star}

|  |  |  |
| --- | --- | --- |
|  | {Φrj:j∈ℕ,r∈{1,…,Nj}},for some​Nj∈ℕ,\big\{\Phi\_{r}^{j}:j\in\mathbb{N},\;r\in\{1,\ldots,N\_{j}\}\big\},\;\text{\rm for some}\;N\_{j}\in\mathbb{N}, |  |

an orthonormal uu-wavelet basis in L2​(𝒟)L\_{2}(\mathcal{D}). Then let B¯q,rs​(𝒟)\overline{B}^{s}\_{q,r}(\mathcal{D}) be the space in [[89](https://arxiv.org/html/2511.01125v1#bib.bib89), Equation (3.46)] and let

|  |  |  |
| --- | --- | --- |
|  | u>max⁡{s,σq,r−s},s≠0.u>\max\big\{s,\sigma\_{q,r}-s\big\},\;s\neq 0. |  |

Then f∈𝒟′​(𝒟)f\in\mathcal{D}^{\prime}(\mathcal{D}) is an element of B¯q,rs​(𝒟)\overline{B}^{s}\_{q,r}(\mathcal{D}) if and only if it can be represented as

|  |  |  |
| --- | --- | --- |
|  | f=∑j=0∞∑k=1Njλkj​2−j​d/2​Φkj,λ∈bq,rs​(ℤ𝒟),f=\sum\_{j=0}^{\infty}\sum\_{k=1}^{N\_{\text{$j$}}}\lambda\_{k}^{j}2^{\text{$-$}jd/2}\Phi\_{k}^{j},\;\lambda\in b^{s}\_{q,r}(\mathbb{Z}\_{\mathcal{D}}), |  |

with convergence holding in 𝒟′​(𝒟)\mathcal{D}^{\prime}(\mathcal{D}) and locally in any spaces B¯q,rσ​(𝒟)\overline{B}^{\sigma}\_{q,r}(\mathcal{D}) with σq,r<s\sigma\_{q,r}<s.

Furthermore, if f∈B¯q,rs​(𝒟)f\in\overline{B}^{s}\_{q,r}(\mathcal{D}) then the representation is unique with λ=λ​(f)\lambda=\lambda(f) as in ([A.28](https://arxiv.org/html/2511.01125v1#A1.E28 "Equation A.28 ‣ A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) and II the linear map in Lemma [A.2.3](https://arxiv.org/html/2511.01125v1#A1.SS2.SSS3 "A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") is an bi-Lipschitz isomorphism of Banach spaces mapping B¯q.rs​(𝒟)\overline{B}^{s}\_{q.r}(\mathcal{D}) onto bq,rs​(ℤ𝒟)b^{s}\_{q,r}(\mathbb{Z}\_{\mathcal{D}}). If, in addition, q<∞q<\infty, r<∞r<\infty, then (Φkj){(j,k)∈ℕ2:k∈{1,…,Nj}}(\Phi\_{k}^{j})\_{\{(j,k)\in\mathbb{N}^{\text{$2$}}:k\in\{1,\dots,N\_{\text{$j$}}\}\}} is an unconditional basis in B¯q,rs​(𝒟)\overline{B}^{s}\_{q,r}(\mathcal{D}).

Having covered the necessary background, we now prove our universal approximation result, see [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") below.

### A.3 Proof of universal approximation

We now express the previous result in terms of neural networks.

###### Lemma A.11 (Wavelet implementation on domains).

Let 𝒟\mathcal{D} be a bounded domain with Lipschitz boundary111111The following result holds, more general on (ϵ,δ)(\epsilon,\delta)-domains and thus on any Lipschitz domain; however, we will not need that level of generality in the remainder of our paper., let σW\sigma\_{\text{$W$}} and σS\sigma\_{\text{$S$}} satisfy [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators") and s≥2s\geq 2.
Let G∈{S,W}d⁣⋆G\in\{S,W\}^{d\star}, j∈ℕj\in\mathbb{N}, and m∈ℤ𝒟m\in\mathbb{Z}\_{\mathcal{D}}. Then there exists a Res–KAN
Ψ^G,mj:ℝd⟶ℝ\widehat{\Psi}\_{\text{$G$},m}^{j}:\mathbb{R}^{d}\longrightarrow\mathbb{R} of depth dd, width at-most 2​d+12d+1, and using at-most (5​d2+25​d+2)/2(5d^{2}+25d+2)/2 non-zero parameters satisfying

|  |  |  |
| --- | --- | --- |
|  | ΨG,mj​(x)=Ψ^G,mj,x∈ℝd.\Psi\_{\text{$G$},m}^{j}(x)=\widehat{\Psi}\_{\text{$G$},m}^{j},\;x\in\mathbb{R}^{d}. |  |

Our proof will use a recent result, [[48](https://arxiv.org/html/2511.01125v1#bib.bib48), Lemma 1], which shows that the dd-ary multiplication operator can be exactly implemented using Res–KANs, but only locally. This is in contrast to ReLU MLPs, which can only approximate it locally.

###### Lemma A.12 (Exact multiplication on arbitrarily large hypercubes).

For every d∈ℕ⋆d\in\mathbb{N}^{\star} and each M>0M>0, there exists a Res–KAN ×d2:ℝd⟶ℝ\times^{2}\_{d}:\mathbb{R}^{d}\longrightarrow\mathbb{R} satisfying for each x∈[−M,M]dx\in[-M,M]^{d}

|  |  |  |
| --- | --- | --- |
|  | ×d2(x)=∏i=1dxi.\times^{2}\_{d}(x)=\prod\_{i=1}^{d}x\_{i}. |  |

Moreover ×d2\times^{2}\_{d} has depth dd, width at-most 2​d+12d+1, and at-most (5​d2+21​d)/2(5d^{2}+21d)/2 non-zero parameters.

We can now proceed with the

###### Proof of Lemma [A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators").

Recall that [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), implies that σS\sigma\_{\text{$S$}} in ([2.1](https://arxiv.org/html/2511.01125v1#S2.E1 "Equation 2.1 ‣ 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")) is a scaling function (father wavelet) and σW\sigma\_{\text{$W$}} in ([2.1](https://arxiv.org/html/2511.01125v1#S2.E1 "Equation 2.1 ‣ 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")) is the corresponding mother wavelet. In fact, by [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), both are Daubechies wavelets and are thus are in Cu​(ℝ)C^{u}(\mathbb{R}) and compactly supported. By their continuity, they are thus bounded. Whence, there is some M>0M>0 such that σG​(ℝ)⊆[−M,M]\sigma\_{\text{$G$}}(\mathbb{R})\subseteq[-M,M] for each G∈{S,W}G\in\{S,W\}.

Consequently, for every specification G=(G1,…,Gd)∈{S,W}d⁣⋆G=(G\_{1},\dots,G\_{d})\in\{S,W\}^{d\star}, for every j∈ℤj\in\mathbb{Z}, we may represent the ((multivariate)) Daubechies wavelet ΨG,mj\Psi\_{\text{$G$},m}^{j}, defined by rescaling the associated un-normalised wavelet Ψ~G,mj\widetilde{\Psi}\_{\text{$G$},m}^{j} in ([A.17](https://arxiv.org/html/2511.01125v1#A1.E17 "Equation A.17 ‣ A.2.2 From wavelet para-bases to Besov spaces on Euclidean spaces ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΨG,mj(⋅)=∏i=1d2j​d/2βG,WjσGi(2j​d/2⋅−m)=(∏i=1d2j​d/2βG,Wj)∏i=1dσGi(W0j⋅−m)\displaystyle\Psi\_{G,m}^{j}(\cdot)=\prod\_{i=1}^{d}\frac{2^{jd/2}}{\beta^{j}\_{\text{$G$},\text{$W$}}}\sigma\_{\text{$G$}\_{\text{$i$}}}\big(2^{jd/2}\cdot-m\big)=\Bigg(\prod\_{i=1}^{d}\frac{2^{jd/2}}{\beta^{j}\_{\text{$G$},\text{$W$}}}\Bigg)\prod\_{i=1}^{d}\sigma\_{\text{$G$}\_{\text{$i$}}}\big(W\_{0}^{j}\cdot-m\big) | ≕κG,Wj∏i=1dσGi(W0j⋅−m)\displaystyle\eqqcolon\kappa\_{\text{$G$},\text{$W$}}^{j}\prod\_{i=1}^{d}\sigma\_{\text{$G$}\_{\text{$i$}}}\big(W\_{0}^{j}\cdot-m\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =κG,Mj×d2∘σGi(W0j⋅−m),\displaystyle=\kappa\_{\text{$G$},\text{$M$}}^{j}\times\_{d}^{2}\circ\sigma\_{\text{$G$}\_{\text{$i$}}}\big(W\_{0}^{j}\cdot-m\big), |  | (A.29) |

where βG,Wj≔‖ΨG,mj‖L2​(ℝ)\beta\_{G,W}^{j}\coloneqq\|\Psi\_{G,m}^{j}\|\_{L^{2}(\mathbb{R})}
where W0j≔2j​d/2​IdW\_{0}^{j}\coloneqq 2^{jd/2}\mathrm{I}\_{d}, m∈ℤdm\in\mathbb{Z}^{d} and where ([A.29](https://arxiv.org/html/2511.01125v1#A1.Ex67 "Equation A.29 ‣ A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) holds by [[48](https://arxiv.org/html/2511.01125v1#bib.bib48), Lemma 1] (having chosen MM large enough); where ×d2:ℝd⟶ℝ\times^{2}\_{d}:\mathbb{R}^{d}\longrightarrow\mathbb{R} is a Res–KAN with depth dd, width at-most 2​d+12d+1, and at-most 5​d2+21​d2\frac{5d^{2}+21d}{2} non-zero parameters.

Now, making use of the chosen structure of the ‘non-spline’ factor in our trainable activation function σβ:I\sigma\_{\beta:I} in [Equation˜2.1](https://arxiv.org/html/2511.01125v1#S2.E1 "In 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), for each i∈{1,…,d}i\in\{1,\dots,d\}, if Gi=SG\_{i}=S we set βi=(1)⊕0I+1\beta\_{i}=(1)\oplus 0\_{I+1} and if Gi=WG\_{i}=W we set βi=(0)⊕(1)⊕0I\beta\_{i}=(0)\oplus(1)\oplus 0\_{I}
Then, ([A.29](https://arxiv.org/html/2511.01125v1#A1.Ex67 "Equation A.29 ‣ A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) can be re-expressed as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΨG,mj\displaystyle\Psi\_{\text{$G$},m}^{j} | ≔κG,Wj×d2∘σGi(W0j⋅−m)\displaystyle\coloneqq\kappa\_{\text{$G$},\text{$W$}}^{j}\times\_{d}^{2}\circ\sigma\_{\text{$G$}\_{\text{$i$}}}\big(W\_{0}^{j}\cdot-m\big) |  | (A.30) |

Now by [[48](https://arxiv.org/html/2511.01125v1#bib.bib48), Lemma 1], ×d2\times\_{d}^{2} can be implemented by a ReLU MLP of depth dd, width 2​d+12d+1, and using at-most (5​d2+21​d)/2(5d^{2}+21d)/2 non-zero parameters. Consequently, ×d2\times^{2}\_{d} is representable/implementable by a ReLU MLP with depth dd, width at-most 2​d+12d+1, and using at-most (5​d2+25​d+2)/2(5d^{2}+25d+2)/2 non-zero parameters.
∎

A direct consequence of the previous result is the following.

###### Proposition A.13 (Res–KAN basis of Besov spaces).

Let 𝒟\mathcal{D} be a bounded exterior-thick domain, (q,r)∈(1,∞)2(q,r)\in(1,\infty)^{2}, and s≥2s\geq 2. Then, there is a Schauder basis

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Φ^kj:j∈ℕ,k∈{1,…,Nj}},for some​Nj∈ℕ¯,\big\{\widehat{\Phi}\_{k}^{j}:j\in\mathbb{N},\;k\in\{1,\ldots,N\_{j}\}\big\},\;\text{\rm for some}\;N\_{j}\in\overline{\mathbb{N}}, |  | (A.31) |

of B¯q,rs​(𝒟)\overline{B}\_{q,r}^{s}(\mathcal{D}) consisting of uu-wavelets. Moreover, for each such k,jk,j, Φ^kj\widehat{\Phi}\_{k}^{j} is implementable by a Res–KAN of depth dd, width at-most 2​d+12d+1, and using at-most (5​d2+25​d+2)/2(5d^{2}+25d+2)/2 non-zero parameters.

###### Proof.

This is a direct consequence of [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"), [Section˜A.2.3](https://arxiv.org/html/2511.01125v1#A1.SS2.SSS3 "A.2.3 Besov spaces on domains ‣ A.2 Proof of Theorem 3.7 ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators"), and of [[90](https://arxiv.org/html/2511.01125v1#bib.bib90), Theorem 3.13 (i​i)(ii)].
∎

We now prove the universality of our models in the class of Hölder continuous maps between Besov spaces; recall the notation ([2.12](https://arxiv.org/html/2511.01125v1#S2.E12 "Equation 2.12 ‣ 2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")).
We write Hld⁡(B¯q,rs​(𝒟),B¯q,rs​(𝒟))\operatorname{Hld}(\bar{B}^{s}\_{q,r}(\mathcal{D}),\bar{B}^{s}\_{q,r}(\mathcal{D})) for the set of all
α\alpha–Hölder continuous maps from B¯q,rs​(𝒟)\bar{B}^{s}\_{q,r}(\mathcal{D}) to itself, for some 0<α≤10<\alpha\leq 1.

###### Proposition A.14 (Universal approximation).

Let d∈ℕ+d\in\mathbb{N}\_{+}, s>0s>0, and 𝒟\mathcal{D} be a bounded exterior-thick domain in ℝd\mathbb{R}^{d}, (q,r)∈(1,∞)2(q,r)\in(1,\infty)^{2} and 2≤s2\leq s, and let I≔⌈s⌉I\coloneqq\lceil s\rceil.
If σS\sigma\_{\text{$S$}} and σW\sigma\_{\text{$W$}} satisfy [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), then 𝒩​𝒪I,α\mathcal{NO}\_{I,\alpha} is dense in Hld⁡(B¯q,rs​(𝒟),B¯q,r2​(𝒟))\operatorname{Hld}(\bar{B}^{s}\_{q,r}(\mathcal{D}),\bar{B}^{2}\_{q,r}(\mathcal{D})) for the ((relative)) topology induced by the topology of uniform convergence on compact sets.

###### Proof.

Since 𝒟\mathcal{D} is exterior-thick, s≥2s\geq 2, (q,r)∈(1,∞)2(q,r)\in(1,\infty)^{2}, σS\sigma\_{\text{$S$}} and σW\sigma\_{\text{$W$}} satisfy [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), and we set I≔⌈s⌉I\coloneqq\lceil s\rceil then, [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") guarantees that we may exhibit a Schauder basis of B¯q,rs​(𝒟)\overline{B}^{s}\_{q,r}(\mathcal{D}) consisting only of Res–KANs, as in ([A.31](https://arxiv.org/html/2511.01125v1#A1.E31 "Equation A.31 ‣ A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")).

Pick an enumeration (Ψ^kℓjℓ)ℓ∈ℕ\big(\widehat{\Psi}\_{k\_{\text{$\ell$}}}^{j\_{\text{$\ell$}}}\big)\_{\ell\in\mathbb{N}} thereof.
Now, let 𝔉\mathfrak{F} consist of all functions F^:B¯q,rs​(𝒟)⟶B¯q,r2​(𝒟)\widehat{F}:\bar{B}^{s}\_{q,r}(\mathcal{D})\longrightarrow\bar{B}^{2}\_{q,r}(\mathcal{D}) of the form in [[33](https://arxiv.org/html/2511.01125v1#bib.bib33), Equation 16] and [[33](https://arxiv.org/html/2511.01125v1#bib.bib33), Definition 6 (Neural filters)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^≔(Ψ^k1j1,…,Ψ^kKjK)⊤​f^ReLU∘(∫ℝdf​(x)​Ψ^k1j1​dx⋮∫ℝdf​(x)​Ψ^kKjK​dx)\widehat{F}\coloneqq\Big(\widehat{\Psi}^{j\_{\text{$1$}}}\_{k\_{\text{$1$}}},\dots,\widehat{\Psi}^{j\_{\text{$K$}}}\_{k\_{\text{$K$}}}\Big)^{\top}\,\widehat{f}\_{\text{$\rm ReLU$}}\circ\begin{pmatrix}\displaystyle\int\_{\mathbb{R}^{\text{$d$}}}\,f(x)\widehat{\Psi}^{j\_{\text{$1$}}}\_{k\_{\text{$1$}}}\mathrm{d}x\\ \vdots\\ \displaystyle\int\_{\mathbb{R}^{\text{$d$}}}\,f(x)\widehat{\Psi}^{j\_{\text{$K$}}}\_{k\_{\text{$K$}}}\mathrm{d}x\end{pmatrix} |  | (A.32) |

for some K∈ℕ⋆K\in\mathbb{N}^{\star}, and where f^ReLU:ℝK⟶ℝK\widehat{f}\_{\text{$\rm ReLU$}}:\mathbb{R}^{K}\longrightarrow\mathbb{R}^{K} is a ReLU feed-forward neural network defined as iteratively mapping any x∈ℝKx\in\mathbb{R}^{K} to the vector f^ReLU​(x)≔xL+1\hat{f}\_{\operatorname{ReLU}}(x)\coloneqq x\_{L+1} defined recursively by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xL+1\displaystyle x\_{L+1} | ≔WL+1​xL∈ℝdL+1≔ℝdK\displaystyle\coloneqq W\_{L+1}x\_{L}\in\mathbb{R}^{d\_{L+1}}\coloneqq\mathbb{R}^{d\_{K}} |  | (A.33) |
|  | xℓ+1\displaystyle x\_{\ell+1} | ≔ReLU​(Wℓ​xℓ+bℓ)∈ℝdℓ+1,x∈ℝK,L∈ℕ+, for ​ℓ∈{0,…,L}\displaystyle\coloneqq\mathrm{ReLU}\big(W\_{\ell}x\_{\ell}+b\_{\ell}\big)\in\mathbb{R}^{d\_{\ell+1}},\;x\in\mathbb{R}^{K},\;L\in\mathbb{N}\_{+},\,\,\mbox{ for }\ell\in\{0,\dots,L\} |  |
|  | x0\displaystyle x\_{0} | ≔x∈ℝd0≔ℝdK.\displaystyle\coloneqq x\in\mathbb{R}^{d\_{0}}\coloneqq\mathbb{R}^{d\_{K}}. |  |

where the layer widths are (d0,…,dL+​1)∈(ℕ+)L+2(d\_{0},\dots,d\_{\text{$L$}\text{$+$}1})\in(\mathbb{N}\_{+})^{L\text{$+$}2},
K=d0=dL+​1K=d\_{0}=d\_{\text{$L$}\text{$+$}1}, and for each such ℓ\ell, we have Wℓ∈ℝdℓ+1×dℓW\_{\ell}\in\mathbb{R}^{d\_{\text{$\ell$}\text{$+$}\text{$1$}}\times d\_{\text{$\ell$}}}, as well as bℓ∈ℝdℓ+1b\_{\ell}\in\mathbb{R}^{d\_{\text{$\ell$}\text{$+$}\text{$1$}}}.

Since (Ψ^kℓjℓ)ℓ∈ℕ\big(\widehat{\Psi}\_{k\_{\text{$\ell$}}}^{j\_{\text{$\ell$}}}\big)\_{\ell\in\mathbb{N}} is a Schauder basis of the Banach space B¯q,rs​(𝒟)\bar{B}^{s}\_{q,r}(\mathcal{D}) and of B¯q,r2​(𝒟)\bar{B}^{2}\_{q,r}(\mathcal{D}) then [[33](https://arxiv.org/html/2511.01125v1#bib.bib33), Theorem 1] implies that 𝔉\mathfrak{F} is dense in Hld⁡(B¯q,rs​(𝒟),B¯q,r2​(𝒟))\operatorname{Hld}(\bar{B}^{s}\_{q,r}(\mathcal{D}),\bar{B}^{2}\_{q,r}(\mathcal{D})) for the (relative) topology induced by the topology of uniform convergence on compact sets. In other words, for every compact 𝒦⊆B¯q,rs​(𝒟)\mathcal{K}\subseteq\bar{B}^{s}\_{q,r}(\mathcal{D}), every ε>0\varepsilon>0, and 0<α≤10<\alpha\leq 1, and every α\alpha–Hölder continuous map f:B¯q,rs​(𝒟)⟶B¯q,r2​(𝒟)f:\bar{B}^{s}\_{q,r}(\mathcal{D})\longrightarrow\bar{B}^{2}\_{q,r}(\mathcal{D}), there is some F^∈𝔉\widehat{F}\in\mathfrak{F} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | supu∈𝒦‖F​(u)−F^​(u)‖W2,p​(𝒟)<ε.\sup\_{u\in\mathcal{K}}\|F(u)-\widehat{F}(u)\big\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}<\varepsilon. |  | (A.34) |

To deduce our claim, we will show that 𝔉⊆𝒩​𝒪I,α\mathfrak{F}\subseteq\mathcal{NO}\_{\text{$I$},\alpha}. Let F^\widehat{F} be an arbitrary element of 𝔉\mathfrak{F}, which thus admits a representation as in ([A.32](https://arxiv.org/html/2511.01125v1#A1.E32 "Equation A.32 ‣ A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")).

Now, for every ℓ∈{0,…,L−1}\ell\in\{0,\dots,L-1\}, let bℓ​(x)≔𝟎(d+dℓ+1)×(d+dℓ+1)​x+𝟎d⊕bℓb^{\ell}(x)\coloneqq\mathbf{0}\_{(d+d\_{\text{$\ell$}\text{$+$}\text{$1$}})\times(d+d\_{\text{$\ell$}\text{$+$}\text{$1$}})}x+\mathbf{0}\_{d}\oplus b\_{\ell} be a constant Res–KAN, see [Equation˜2.7](https://arxiv.org/html/2511.01125v1#S2.E7 "In 2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), where 𝟎(d+dℓ+1)×(d+dℓ+1)​x\mathbf{0}\_{(d+d\_{\text{$\ell$}\text{$+$}\text{$1$}})\times(d+d\_{\text{$\ell$}\text{$+$}\text{$1$}})}x is the (d+dℓ+1)×(d+dℓ+1)(d+d\_{\text{$\ell$}\text{$+$}\text{$1$}})\times(d+d\_{\text{$\ell$}\text{$+$}\text{$1$}}) zero matrix and 𝟎d∈ℝd\mathbf{0}\_{d}\in\mathbb{R}^{d} is the zero vector therein. Now, for every ℓ∈{1,…,L−1}\ell\in\{1,\dots,L-1\} define the matrix Wℓ≔𝟎d×d⊗WℓW^{\ell}\coloneqq\mathbf{0}\_{d\times d}\otimes W\_{\ell}, where ⊗\otimes denotes the Kronecker product and let WL≔(0K×d|WL)W^{L}\coloneqq(0\_{K\times d}|W\_{L}) denotes the column-wise concatenation of the matrix 0K×d0\_{K\times d} with the matrix WLW\_{L}
.
Now, for each ℓ∈{1,…,L}\ell\in\{1,\dots,L\} let βℓ≔(0,0,1,0,…,0)∈ℝdℓ+1+2\beta\_{\ell}\coloneqq(0,0,1,0,\dots,0)\in\mathbb{R}^{d\_{\text{$\ell$}\text{$+$}\text{$1$}}+2}. With these specifications, we see that the KANO Γ\Gamma with representation ([2.2.2](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS2 "2.2.2 Neural operator architectures ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators")) (where din=1d\_{\rm in}=1 and dout=1d\_{\rm out}=1) is exactly equal to F^\widehat{F}. We have thus shown that 𝔉⊆𝒩​𝒪I,α\mathfrak{F}\subseteq\mathcal{NO}\_{\text{$I$},\alpha}, which concludes our proof.
∎

### A.4 Stability estimate of general solution operator

###### Lemma A.15 (Linear stability of perturbations to PDE).

Under [Sections˜3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") and [3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"),
if r>0r>0 and k>1+max⁡{1,d/p}k>1+\max\{1,d/p\} then there exists a constant L2,k,𝒟>0L\_{2,k,\text{$\mathcal{D}$}}>0 such that the non-linear operator

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΓGen:𝒳k​(r)\displaystyle\Gamma\_{\text{$\rm Gen$}}:\mathcal{X}\_{k}(r) | ⟶Wp2​(𝒟)\displaystyle\longrightarrow W^{2}\_{p}(\mathcal{D}) |  | (A.35) |
|  | (G¯0,g)\displaystyle(\bar{G}\_{0},g) | ⟼uG¯0,g,\displaystyle\longmapsto u\_{\bar{\text{$G$}}\_{\text{$0$}},g}, |  |

is L2,k,𝒟L\_{2,k,\text{$\mathcal{D}$}}–Lipschitz continuous.

###### Proof.

Under [Sections˜3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") and [3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") we may apply [[54](https://arxiv.org/html/2511.01125v1#bib.bib54), Theorem 14.1.3] to deduce that for every ((G¯0,g),(G¯0′,g′))∈𝒳×𝒳((\bar{G}\_{0},g),(\bar{G}\_{0}^{\prime},g^{\prime}))\in\mathcal{X}\times{\cal X} and the respective solutions uG¯0,g,uG¯0′,g′u\_{\bar{\text{$G$}}\_{\text{$0$}},g},u\_{\bar{\text{$G$}}\_{\text{$0$}}^{\text{$\prime$}},g^{\text{$\prime$}}} (which exist by [[54](https://arxiv.org/html/2511.01125v1#bib.bib54), Theorem 14.1.5]) to their elliptic PDE in ([3.5](https://arxiv.org/html/2511.01125v1#S3.E5 "Equation 3.5 ‣ 3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators")) with G+G¯0G+\bar{G}\_{0} and G+G¯0′G+\bar{G}\_{0}^{\prime} respectively instead of GG, we have the estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖uG¯0,g−uG¯0′,g′‖Wp2​(𝒟)≲‖G¯0−G¯0′‖Lp​(𝒟)+‖g−g′‖W2,p​(𝒟)+‖uG¯0,g−uG¯0′,g′‖C​(𝒟),\|u\_{\text{$\bar{G}$}\_{\text{$0$}},g}-u\_{\text{$\bar{G}$}\_{\text{$0$}}^{\text{$\prime$}},g^{\text{$\prime$}}}\|\_{W\_{\text{$p$}}^{\text{$2$}}(\mathcal{D})}\lesssim\|\bar{G}\_{0}-\bar{G}\_{0}^{\prime}\|\_{L^{\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|u\_{\text{$\bar{G}$}\_{\text{$0$}},g}-u\_{\text{$\bar{G}$}\_{\text{$0$}}^{\text{$\prime$}},g^{\text{$\prime$}}}\|\_{C(\mathcal{D})}, |  | (A.36) |

where ≲\lesssim suppress a multiplicative constant depending only on c1c\_{1}, c2c\_{2}, R0R\_{0}, δ\delta, LFL\_{F}, ωF\omega\_{F}, and on the domain 𝒟\mathcal{D}. Next, applying [[54](https://arxiv.org/html/2511.01125v1#bib.bib54), Lemma 6.6.10] we deduce that there is an absolute constant C>0C>0 such that ‖uG¯0,g−uG¯0′,g′‖C​(𝒟)≤C​supx∈∂𝒟|g​(x)−g′​(x)|=‖g−g′‖C​(∂𝒟)\|u\_{\text{$\bar{G}$}\_{\text{$0$}},g}-u\_{\text{$\bar{G}$}\_{\text{$0$}}^{\text{$\prime$}},g^{\text{$\prime$}}}\|\_{C(\mathcal{D})}\leq C\sup\_{x\in\partial\mathcal{D}}|g(x)-{g}^{\prime}(x)|=\|g-g^{\prime}\|\_{C(\partial\mathcal{D})}. Consequently, ([A.36](https://arxiv.org/html/2511.01125v1#A1.E36 "Equation A.36 ‣ A.4 Stability estimate of general solution operator ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")) may be bounded above by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖uG¯0,g−uG¯0′,g′‖Wp2​(𝒟)\displaystyle\|u\_{\text{$\bar{G}$}\_{\text{$0$}},g}-u\_{\text{$\bar{G}$}\_{\text{$0$}}^{\text{$\prime$}},g^{\text{$\prime$}}}\|\_{W\_{\text{$p$}}^{\text{$2$}}(\mathcal{D})} | ≲‖G¯0−G¯0′‖Lp​(𝒟)+‖g−g′‖W2,p​(𝒟)+‖g−g′‖C​(∂𝒟)\displaystyle\lesssim\|\bar{G}\_{0}-\bar{G}\_{0}^{\prime}\|\_{L^{\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{C(\partial\mathcal{D})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖G¯0−G¯0′‖W2,p​(𝒟)+‖g−g′‖W2,p​(𝒟)+‖g−g′‖C​(∂𝒟)\displaystyle\leq\|\bar{G}\_{0}-\bar{G}\_{0}^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{C(\partial\mathcal{D})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖G¯0−G¯0′‖W2,p​(𝒟)+‖g−g′‖W2,p​(𝒟)+‖g−g′‖C​(𝒟)\displaystyle\leq\|\bar{G}\_{0}-\bar{G}\_{0}^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{C(\mathcal{D})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖G¯0−G¯0′‖W2,p​(𝒟)+‖g−g′‖W2,p​(𝒟)+‖g−g′‖Wk,p​(𝒟)\displaystyle\leq\|\bar{G}\_{0}-\bar{G}\_{0}^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$k$}\text{$,$}\text{$p$}}(\mathcal{D})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C~2,k,𝒟​‖G¯0−G¯0′‖Wk,p​(𝒟)+C~2,k,𝒟​‖g−g′‖Wk,p​(𝒟)+‖g−g′‖Wk,p​(𝒟)\displaystyle\leq\widetilde{C}\_{2,k,\text{$\mathcal{D}$}}\,\|\bar{G}\_{0}-\bar{G}\_{0}^{\prime}\|\_{W^{\text{$k$}\text{$,$}\text{$p$}}(\mathcal{D})}+\widetilde{C}\_{2,k,\text{$\mathcal{D}$}}\,\|g-g^{\prime}\|\_{W^{\text{$k$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$k$}\text{$,$}\text{$p$}}(\mathcal{D})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L2,k,𝒟​(‖G¯0−G¯0′‖Wk,p​(𝒟)+‖g−g′‖Wk,p​(𝒟)),\displaystyle\leq L\_{2,k,\text{$\mathcal{D}$}}\,\Big(\|\bar{G}\_{0}-\bar{G}\_{0}^{\prime}\|\_{W^{\text{$k$}\text{$,$}\text{$p$}}(\mathcal{D})}+\|g-g^{\prime}\|\_{W^{\text{$k$}\text{$,$}\text{$p$}}(\mathcal{D})}\Big), |  |

where we used in the fourth line the Sobolev embedding Theorem [[26](https://arxiv.org/html/2511.01125v1#bib.bib26), Section 5.6.3], which holds provided that k≤1+⌈dp⌉k\leq 1+\lceil\tfrac{d}{p}\rceil, where the existence of the constant C~2,k,𝒟>0\widetilde{C}\_{2,k,\text{$\mathcal{D}$}}>0 (which only depends on 22, kk, and on 𝒟\mathcal{D}) as well as the validity of the fifth line are ensured since we have assumed that 2<k2<k so that the Rellich–-Kondrachov Theorem [[88](https://arxiv.org/html/2511.01125v1#bib.bib88), Proposition 4.4] implies that W2,p​(𝒟)W^{2,p}(\mathcal{D}) is compactly embedded in Wk,p​(𝒟)W^{k,p}(\mathcal{D}), and C:=2​C~2,k,𝒟+1>1C:=2\widetilde{C}\_{2,k,\text{$\mathcal{D}$}}+1>1.
∎

We are now ready to establish our approximability result for the solution operator corresponding to the more general class of fully non-linear elliptic PDEs.

###### Proof of Theorem [3.7](https://arxiv.org/html/2511.01125v1#S3.Thmtheorem7 "Theorem 3.7 (Approximability of the perturbation-to-solution map). ‣ 3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators").

Under [Sections˜3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators") and [3.2](https://arxiv.org/html/2511.01125v1#S3.SS2 "3.2 General approximability guarantee ‣ 3 Main results ‣ One model to solve them all: 2BSDE families via neural operators"), [Section˜A.4](https://arxiv.org/html/2511.01125v1#A1.SS4 "A.4 Stability estimate of general solution operator ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") applies and guarantees that the non-linear operator ΓGen\Gamma\_{\text{$\rm Gen$}}, defined in ([A.35](https://arxiv.org/html/2511.01125v1#A1.E35 "Equation A.35 ‣ A.4 Stability estimate of general solution operator ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators")), is L2,k,𝒟L\_{2,k,\text{$\mathcal{D}$}}–Lipschitz continuous on 𝒳k​(r)\mathcal{X}\_{k}(r). Now, since 2<k<∞2<k<\infty and σS\sigma\_{\text{$S$}} and σW\sigma\_{\text{$W$}} satisfy [Section˜2.2.1](https://arxiv.org/html/2511.01125v1#S2.SS2.SSS1 "2.2.1 Residual Kolmogorov–Arnold networks (Res–KANs) ‣ 2.2 Deep learning ‣ 2 Preliminaries ‣ One model to solve them all: 2BSDE families via neural operators"), we may apply [Section˜A.3](https://arxiv.org/html/2511.01125v1#A1.SS3 "A.3 Proof of universal approximation ‣ Appendix A Proof of PDE results ‣ One model to solve them all: 2BSDE families via neural operators") to deduce that for every ε>0\varepsilon>0 and every non-empty compact subset 𝒳⊆𝒳k​(r)\mathcal{X}\subseteq\mathcal{X}\_{k}(r)(in the relative topology induced by inclusion in W2,p(𝒟)×Wk,p(𝒟))W^{2,p}(\mathcal{D})\times W^{k,p}(\mathcal{D})) equipped with the norm topology) there exists Γ^∈𝒩​𝒪⌈k⌉,1\hat{\Gamma}\in\mathcal{NO}\_{\lceil k\rceil,1} satisfying the uniform estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(G¯0,g)∈𝒳‖ΓGen​(G¯0,g)−Γ^​(G¯0,g)‖W2,p​(𝒟)<ε.\sup\_{(\bar{\text{$G$}}\_{\text{$0$}},g)\in\mathcal{X}}\,\big\|\Gamma\_{\text{$\rm Gen$}}(\bar{G}\_{0},g)-\hat{\Gamma}(\bar{G}\_{0},g)\big\|\_{W^{\text{$2$}\text{$,$}\text{$p$}}(\mathcal{D})}<\varepsilon. |  | (A.37) |

Noting that, by definition, uG¯0,g=ΓGen​(G¯0,g)u\_{\text{$\bar{G}$}\_{\text{$0$}},g}=\Gamma\_{\text{$\rm Gen$}}(\bar{G}\_{0},g) for each (G¯0,g)∈𝒳(\bar{G}\_{0},g)\in\mathcal{X} concludes the proof.
∎

## Appendix B Proof of stochastic results

To derive the stochastic counterparts of our results, we emphasise that our approach does not rely on any unconventional lifting channels—such as those introduced in [[31](https://arxiv.org/html/2511.01125v1#bib.bib31)]—which are non-standard within the operator learning literature and were originally proposed to enforce additional smoothness.
Instead, we are able to combine the Bernstein and Sobolev inequalities with Itô-type formulas in a compatible manner, without imposing excessive smoothness assumptions on the PDE solutions. This is achieved through the following transfer principle, which requires conditions we borrow from [de Marco](https://arxiv.org/html/2511.01125v1#bib.bib21) [[21](https://arxiv.org/html/2511.01125v1#bib.bib21)].

###### Assumption B.1 (Regularity of the forward process).

1. (i)(i)

   there is η≥0\eta\geq 0 such that μ\mu and γ\gamma in ([SDE](https://arxiv.org/html/2511.01125v1#S1.Ex1 "Equation SDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) are of class C∞C^{\infty} on ℝd∖Bℝd​(0,η)¯\mathbb{R}^{d}\setminus\overline{B\_{\mathbb{R}^{d}}(0,\eta)}.
   Moreover, for every R>0R>0 and x0∈ℝdx\_{0}\in\mathbb{R}^{d}, μ\mu and γ\gamma are smooth on Bℝd​(x0,3​R)⊂ℝd∖Bℝd​(0,η)¯;B\_{\mathbb{R}^{d}}(x\_{0},3R)\subset\mathbb{R}^{d}\setminus\overline{B\_{\mathbb{R}^{d}}(0,\eta)};
2. (i​i)(ii)

   there exist positive exponents qq and q¯>0\bar{q}>0, as well as constants
   0<C0<10<C\_{0}<1, Ck>0C\_{k}>0 (for every multi–index α\alpha with |α|=k≥1|\alpha|=k\geq 1) such that

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | |∂αμi​(x)|+|∂αγi,j​(x)|\displaystyle|\partial\_{\alpha}\mu^{i}(x)|+|\partial\_{\alpha}\gamma^{i,j}(x)| | ≤Ck​(1+‖x‖q),x∈ℝd,(i,j)∈{1,…,d}2,\displaystyle\leq C\_{k}(1+\|x\|^{q}),\;x\in\mathbb{R}^{d},\;(i,j)\in\{1,\dots,d\}^{2}, |  | (B.1) |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | C0​‖x‖−q¯​Id\displaystyle C\_{0}\|x\|^{-\bar{q}}\mathrm{I}\_{d} | ≤γ​(x)​γ​(x)⊤,‖x‖>η;\displaystyle\leq\gamma(x)\gamma(x)^{\top},\;\|x\|>\eta; |  | (B.2) |
3. (i​i​i)(iii)

   for every p>0p>0, sup0≤s≤t𝔼ℙ​[‖Xs‖p]<∞;\sup\_{0\leq s\leq t}\mathbb{E}^{\mathbb{P}}[\|X\_{s}\|^{p}]<\infty;
4. (i​v)(iv)

   ([SDE](https://arxiv.org/html/2511.01125v1#S1.Ex1 "Equation SDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) admits a strong solution.

Under these conditions, the process XX admits for every t∈(0,T]t\in(0,T]
a smooth density satisfying some
Gaussian-type decay and derivative bounds, as shown in [[21](https://arxiv.org/html/2511.01125v1#bib.bib21), Theorem 2.2].
In what follows, if it exists, for any time t≥0t\geq 0, we denote the density of the law XtX\_{t} with respect to the Lebesgue measure on BR​(y0)B\_{\text{$R$}}(y\_{0}), for any y0∈𝒟y\_{0}\in\mathcal{D} and R>0R>0, by ρt,y0∈L1​(BR​(y0);[0,∞))\rho\_{t,y\_{\text{$0$}}}\in L^{1}(B\_{\text{$R$}}(y\_{0});[0,\infty)), where

|  |  |  |
| --- | --- | --- |
|  | L1​(BR​(y0);[0,∞))≔{u∈L1​(BR​(y0)):u​(x)≥0,Lebesgue–a.e.}.L^{1}(B\_{\text{$R$}}(y\_{0});[0,\infty))\coloneqq\big\{u\in L^{1}(B\_{\text{$R$}}(y\_{0})):u(x)\geq 0,\;\text{\rm Lebesgue--a.e.}\}. |  |

###### Lemma B.2 (Transfer trick).

Let 1≤s<∞1\leq s<\infty, 1≤r≤∞1\leq r\leq\infty, x0∈𝒟x\_{0}\in\mathcal{D} be such that 𝒟⊆BR​(x0)\mathcal{D}\subseteq B\_{R}(x\_{0}) be a compact domain, and (u,u^)∈Ws,r​(𝒟)×Ws,r​(𝒟)(u,\hat{u})\in W^{s,r}(\mathcal{D})\times W^{s,r}(\mathcal{D}) be such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖u−u^‖Ws,r​(𝒟)≤ε.\|u-\hat{u}\|\_{W^{\text{$s$}\text{$,$}\text{$r$}}(\mathcal{D})}\leq\varepsilon. |  | (B.3) |

Suppose that XX satisfies ([SDE](https://arxiv.org/html/2511.01125v1#S1.Ex1 "Equation SDE ‣ 1 Introduction ‣ One model to solve them all: 2BSDE families via neural operators")) and [Appendix˜B](https://arxiv.org/html/2511.01125v1#A2 "Appendix B Proof of stochastic results ‣ One model to solve them all: 2BSDE families via neural operators") and τ\tau is the first exit time of XX from 𝒟{\cal D}.
If rr is finite, then additionally assume that there is some 0<δ𝒟0<\delta\_{\text{$\mathcal{D}$}} such that d​(0,𝒟)≔infx∈𝒟‖x‖2≥δ𝒟d(0,\mathcal{D})\coloneqq\inf\_{x\in\mathcal{D}}\|x\|\_{2}\geq\delta\_{\text{$\mathcal{D}$}} and fix a time-window 0<T−<T+0<T\_{\text{$-$}}<T\_{\text{$+$}}.
Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℙ​[∫T−T+∑|β|≤s‖Dβ​u​(Xt)−Dβ​u^​(Xt)‖​d​t]\displaystyle\mathbb{E}^{\mathbb{P}}\Bigg[\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\sum\_{|\beta|\leq s}\big\|D^{\beta}u(X\_{t})-D^{\beta}\hat{u}(X\_{t})\big\|\mathrm{d}t\Bigg] | ≲r,T+,𝒟ε​(CT++1T−3​d/2−1),if​ 1≤r<∞,\displaystyle\lesssim\_{r,\text{$T$}\_{\text{$+$}},\text{$\mathcal{D}$}}\varepsilon\bigg(C\_{\text{$T$}\_{\text{$+$}}}+\frac{1}{T\_{\text{$-$}}^{3d/2-1}}\bigg),\;\mbox{\rm if}1\leq r<\infty, |  | (B.4) |
|  | essupℙ​{sup0≤t≤τ‖Dβ​u​(Xt​(ω))−Dβ​u^​(Xt​(ω))‖}\displaystyle\mathrm{essup}^{\mathbb{P}}\bigg\{\sup\_{0\leq t\leq\tau}\big\|D^{\beta}u(X\_{t}(\omega))-D^{\beta}\,\hat{u}(X\_{t}(\omega))\big\|\bigg\} | ≤ε,if​r=∞,\displaystyle\leq\varepsilon,\;\mbox{\rm if}\;r=\infty, |  |

where CT+>0C\_{\text{$T$}\_{\text{$+$}}}>0 is a constant depending only on T+T\_{\text{$+$}}.

###### Proof.

For the case where r=∞r=\infty, simply note that Xt∨τ∈𝒟X\_{t\vee\tau}\in\mathcal{D}. ℙ\mathbb{P}–a.s. Thus, for ℙ\mathbb{P}–almost every ω∈Ω\omega\in\Omega we have that

|  |  |  |
| --- | --- | --- |
|  | ∑|β|≤s‖Dβ​u​(Xt​(ω))−Dβ​u^​(Xt​(ω))‖≤supx∈𝒟‖Dβ​(u−u^)​(x)‖=‖u−u^‖Ws,r​(𝒟)≤ε,\sum\_{|\beta|\leq s}\big\|D^{\beta}u(X\_{t}(\omega))-D^{\beta}\hat{u}(X\_{t}(\omega))\big\|\leq\sup\_{x\in\mathcal{D}}\big\|D^{\beta}(u-\hat{u})(x)\big\|=\|u-\hat{u}\|\_{W^{\text{$s$}\text{$,$}\text{$r$}}(\mathcal{D})}\leq\varepsilon, |  |

where the last inequality holds since s≥1s\geq 1. Consequently, ([B.4](https://arxiv.org/html/2511.01125v1#A2.E4 "Equation B.4 ‣ Appendix B Proof of stochastic results ‣ One model to solve them all: 2BSDE families via neural operators")) holds.

We now turn our attention to the case where 1≤r<∞1\leq r<\infty. Define τ⋆≔T+∧(τ∨T−)\tau^{\star}\coloneqq T\_{\text{$+$}}\wedge(\tau\vee T\_{\text{$-$}}). Note that, if t∈[T−,T+]t\in[T\_{\text{$-$}},T\_{\text{$+$}}] then Xt∧τ⋆∈𝒟¯X\_{t\wedge\tau^{\text{$\star$}}}\in\bar{\mathcal{D}}, ℙ\mathbb{P}–a.s.
In particular, since 𝒟\mathcal{D} is bounded, then for any t≥0t\geq 0, Xt∧τ⋆∈L∞​([0,T+]×Ω,ℝd)X\_{t\wedge\tau^{\text{$\star$}}}\in L^{\infty}([0,T\_{\text{$+$}}]\times\Omega,\mathbb{R}^{d}); whence, we may apply the Fubini–Tonelli theorem to deduce that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℙ​[∫T−T+∑|β|≤s‖Dβ​u​(Xt)−Dβ​u^​(Xt)‖​d​t]\displaystyle\mathbb{E}^{\mathbb{P}}\Bigg[\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\sum\_{|\beta|\leq s}\big\|D^{\beta}u(X\_{t})-D^{\beta}\hat{u}(X\_{t})\big\|\mathrm{d}t\Bigg] | =∫T−T+𝔼ℙ​[∑|β|≤s‖Dβ​u​(Xt)−Dβ​u^​(Xt)‖]​dt.\displaystyle=\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\mathbb{E}^{\mathbb{P}}\Bigg[\sum\_{|\beta|\leq s}\big\|D^{\beta}u(X\_{t})-D^{\beta}\hat{u}(X\_{t})\big\|\Bigg]\mathrm{d}t. |  | (B.5) |

Now, since we are operating under [Appendix˜B](https://arxiv.org/html/2511.01125v1#A2 "Appendix B Proof of stochastic results ‣ One model to solve them all: 2BSDE families via neural operators"), we may apply [[21](https://arxiv.org/html/2511.01125v1#bib.bib21), Theorem 2.2] to show that ρt,x0∈L+1​(BR​(x0))\rho\_{t,x\_{\text{$0$}}}\in L^{1}\_{\text{$+$}}(B\_{R}(x\_{0})) exists and there is a constant Cr,T+>0C\_{r,T\_{\text{$+$}}}>0, depending only on rr and T+T\_{\text{$+$}}, such that for every x∈BR​(x0)x\in B\_{R}(x\_{0}) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ρt,x0​(x)|≤Cr,T+​(1+1t3​d/2)​‖x‖−r.|\rho\_{t,x\_{\text{$0$}}}(x)|\leq C\_{r,T\_{\text{$+$}}}\bigg(1+\frac{1}{t^{3d/2}}\bigg)\|x\|^{\text{$-$}r}. |  | (B.6) |

In particular, since 𝒟⊆BR​(x0)\mathcal{D}\subseteq B\_{R}(x\_{0}) then ([B.6](https://arxiv.org/html/2511.01125v1#A2.E6 "Equation B.6 ‣ Appendix B Proof of stochastic results ‣ One model to solve them all: 2BSDE families via neural operators")) holds for every x∈𝒟x\in\mathcal{D}. Consequently, ([B.5](https://arxiv.org/html/2511.01125v1#A2.E5 "Equation B.5 ‣ Appendix B Proof of stochastic results ‣ One model to solve them all: 2BSDE families via neural operators")) and ([B.6](https://arxiv.org/html/2511.01125v1#A2.E6 "Equation B.6 ‣ Appendix B Proof of stochastic results ‣ One model to solve them all: 2BSDE families via neural operators")) imply that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[∫T−T+∑|β|≤s‖Dβ​u​(Xt)−Dβ​u^​(Xt)‖​d​t]\displaystyle\mathbb{E}^{\mathbb{P}}\Bigg[\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\sum\_{|\beta|\leq s}\big\|D^{\beta}u(X\_{t})-D^{\beta}\hat{u}(X\_{t})\big\|\mathrm{d}t\Bigg] | =∫T−T+∫𝒟pt,x0​(x)​∑|β|≤s‖Dβ​u​(x)−Dβ​u^​(x)‖​d​x​d​t\displaystyle=\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\int\_{\mathcal{D}}p\_{t,x\_{\text{$0$}}}(x)\sum\_{|\beta|\leq s}\big\|D^{\beta}u(x)-D^{\beta}\hat{u}(x)\big\|\mathrm{d}x\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫T−T+(∫𝒟pt,x0​(x)r′​dx)1/r′\displaystyle\leq\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\bigg(\int\_{\mathcal{D}}p\_{t,x\_{\text{$0$}}}(x)^{r^{\text{$\prime$}}}\mathrm{d}x\bigg)^{1/r^{\text{$\prime$}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(∫𝒟∑|β|≤s‖Dβ​u​(x)−Dβ​u^​(x)‖r​d​x)1/r​d​t\displaystyle\quad\times\Bigg(\int\_{\mathcal{D}}\sum\_{|\beta|\leq s}\big\|D^{\beta}u(x)-D^{\beta}\hat{u}(x)\big\|^{r}\mathrm{d}x\Bigg)^{1/r}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫T−T+(∫𝒟Cr,T+r′​(1+1t3​d/2)r′​‖x‖−(r​r′)​dx)1/r′\displaystyle\leq\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\bigg(\int\_{\mathcal{D}}C\_{r,\text{$T$}\_{\text{$+$}}}^{r^{\text{$\prime$}}}\bigg(1+\frac{1}{t^{3d/2}}\bigg)^{r^{\text{$\prime$}}}\|x\|^{\text{$-$}(rr^{\text{$\prime$}})}\mathrm{d}x\bigg)^{1/r^{\text{$\prime$}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(∫𝒟∑|β|≤s‖Dβ​u​(x)−Dβ​u^​(x)‖r​d​x)1/r​d​t,\displaystyle\quad\times\Bigg(\int\_{\mathcal{D}}\sum\_{|\beta|\leq s}\big\|D^{\beta}u(x)-D^{\beta}\hat{u}(x)\big\|^{r}\mathrm{d}x\Bigg)^{1/r}\mathrm{d}t, |  |

where the second line follows by Hölder’s inequality with 1r+1r′=1\tfrac{1}{r}+\tfrac{1}{r^{\prime}}=1 (since 1<r<∞1<r<\infty).
Now, the term

|  |  |  |
| --- | --- | --- |
|  | (∫𝒟∑|β|≤s‖Dβ​u​(x)−Dβ​u^​(x)‖r​d​x)1/r,\Bigg(\int\_{\mathcal{D}}\sum\_{|\beta|\leq s}\big\|D^{\beta}u(x)-D^{\beta}\hat{u}(x)\big\|^{r}\mathrm{d}x\Bigg)^{1/r}, |  |

is precisely the W⌊s⌋,r​(𝒟)W^{\lfloor s\rfloor,r}(\mathcal{D}) norm of (u−u^)(u-\hat{u}), which is bounded above by the Ws,r​(𝒟)W^{s,r}(\mathcal{D})-norm, which in turn is bounded above by ε\varepsilon, recall ([B.3](https://arxiv.org/html/2511.01125v1#A2.E3 "Equation B.3 ‣ Appendix B Proof of stochastic results ‣ One model to solve them all: 2BSDE families via neural operators")). Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[∫T−T+∑|β|≤s‖Dβ​u​(Xt)−Dβ​u^​(Xt)‖​d​t]\displaystyle\mathbb{E}^{\mathbb{P}}\Bigg[\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\sum\_{|\beta|\leq s}\big\|D^{\beta}u(X\_{t})-D^{\beta}\hat{u}(X\_{t})\big\|\mathrm{d}t\Bigg] | ≤ε​∫T−T+(∫𝒟Cr,T+r′​(1+1t3​d/2)r′​‖x‖−(r​r′)​dx)1/r′​dt\displaystyle\leq\varepsilon\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\bigg(\int\_{\mathcal{D}}C\_{r,T\_{\text{$+$}}}^{r^{\text{$\prime$}}}\bigg(1+\frac{1}{t^{3d/2}}\bigg)^{r^{\text{$\prime$}}}\,\|x\|^{\text{$-$}(rr^{\text{$\prime$}})}\mathrm{d}x\bigg)^{1/r^{\text{$\prime$}}}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cr,T+​ε​Vol​(𝒟)1/r′δ𝒟r​∫T−T+(1+1t3​d/2)​dt\displaystyle\leq C\_{r,T\_{\text{$+$}}}\varepsilon\frac{\mathrm{Vol}(\mathcal{D})^{1/r^{\text{$\prime$}}}}{\delta\_{\text{$\mathcal{D}$}}^{r}}\int\_{T\_{\text{$-$}}}^{T\_{\text{$+$}}}\bigg(1+\frac{1}{t^{3d/2}}\bigg)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cr,T+​ε​Vol​(𝒟)1/r′δ𝒟r​(T+−T−+T−1−3​d/2−T+1−3​d/23​d/2−1)\displaystyle\leq C\_{r,T\_{\text{$+$}}}\varepsilon\frac{\mathrm{Vol}(\mathcal{D})^{1/r^{\text{$\prime$}}}}{\delta\_{\text{$\mathcal{D}$}}^{r}}\bigg(T\_{\text{$+$}}-T\_{\text{$-$}}+\frac{T\_{\text{$-$}}^{1-3d/2}-T\_{\text{$+$}}^{1-3d/2}}{3d/2-1}\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ε​Cp,T+,𝒟​(CT++1T−3​d/2−1)\displaystyle\leq\varepsilon{C}\_{p,T\_{\text{$+$}},\mathcal{D}}\bigg(C\_{T\_{\text{$+$}}}+\frac{1}{T\_{\text{$-$}}^{3d/2-1}}\bigg) |  |

where we used the assumption that d​(𝒟,0)≥δ𝒟>0d(\mathcal{D},0)\geq\delta\_{\text{$\mathcal{D}$}}>0 and a simple supremum-bound, and where we defined

|  |  |  |
| --- | --- | --- |
|  | Cp,T+,𝒟≔Cp,T+​2​V​o​l​(𝒟)1/r′(3​d−2)​δ𝒟r,and​CT+≔(3​d2−1)​T+.{C}\_{p,T\_{\text{$+$}},\mathcal{D}}\coloneqq C\_{p,T\_{\text{$+$}}}\frac{2\mathrm{Vol}(\mathcal{D})^{1/r^{\text{$\prime$}}}}{(3d-2)\delta\_{\text{$\mathcal{D}$}}^{r}},\;\text{\rm and}\;C\_{T\_{\text{$+$}}}\coloneqq\bigg(\frac{3d}{2}-1\bigg)T\_{\text{$+$}}. |  |

∎

## Appendix C Experimental details

### C.1 Periodic semi-linear case

We consider a periodic example from [[13](https://arxiv.org/html/2511.01125v1#bib.bib13)] in d=5d=5 dimension, with T=1T=1, in which the forward SDE is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt(i)\displaystyle\mathrm{d}X\_{t}^{(i)} | =bi​(Xt(i))​d​t+σi,i​(Xt(i))​d​Wt(i),i∈{1,…,d},\displaystyle=b\_{i}\!\big(X\_{t}^{(i)}\big)\,\mathrm{d}t+\sigma\_{i,i}\!\big(X\_{t}^{(i)}\big)\,\mathrm{d}W\_{t}^{(i)},\;i\in\{1,\dots,d\}, |  |

and the coefficients of the SDE are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​(x)\displaystyle b\_{i}(x) | ≔0.2​sin⁡(2​π​xi),σi,j​(x)≔1d​π​(0.25+0.1​cos⁡(2​π​xi))​ 1{i=j},(i,j)∈{1,…,d}2.\displaystyle\coloneqq 0.2\,\sin(2\pi x\_{i}),\;\sigma\_{i,j}(x)\coloneqq\frac{1}{\sqrt{d}\,\pi}\Big(0.25+0.1\cos(2\pi x\_{i})\Big)\,\mathbf{1}\_{\{i=j\}},\;(i,j)\in\{1,\dots,d\}^{2}. |  |

The coefficients of the backward SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =−f​(t,Xt,Yt,Zt)​d​t+Zt⋅d​Wt,YT=g​(XT),\displaystyle=-\,f\!\big(t,X\_{t},Y\_{t},Z\_{t}\big)\,\mathrm{d}t\;+\;Z\_{t}\cdot\mathrm{d}W\_{t},\;Y\_{T}=g\!\big(X\_{T}\big), |  |

are given by

|  |  |  |
| --- | --- | --- |
|  | g​(x)≔1π​(sin⁡(2​π​∑i=1dxi)+cos⁡(2​π​∑i=1dxi)),\displaystyle g(x)\coloneqq\frac{1}{\pi}\Bigg(\sin\bigg(2\pi\sum\_{i=1}^{d}x\_{i}\bigg)+\cos\bigg(2\pi\sum\_{i=1}^{d}x\_{i}\bigg)\Bigg), |  |
|  |  |  |
| --- | --- | --- |
|  | f​(t,x,y,z)≔2​π2​y​∑i=1dσi,i​(x)2−∑i=1dbi​(x)σi,i​(x)​zi+h​(t,x),\displaystyle f(t,x,y,z)\coloneqq 2\pi^{2}y\sum\_{i=1}^{d}\sigma\_{i,i}(x)^{2}-\sum\_{i=1}^{d}\frac{b\_{i}(x)}{\sigma\_{i,i}(x)}z\_{i}+h(t,x), |  |

where

|  |  |  |
| --- | --- | --- |
|  | h​(t,x)≔2​(cos⁡(2​π​∑i=1dxi+2​π​(T−t))−sin⁡(2​π​∑i=1dxi+2​π​(T−t))).h(t,x)\coloneqq 2\Bigg(\cos\bigg(2\pi\sum\_{i=1}^{d}x\_{i}+2\pi(T-t)\bigg)-\sin\bigg(2\pi\sum\_{i=1}^{d}x\_{i}+2\pi(T-t)\bigg)\Bigg). |  |

The explicit solution uu is given by

|  |  |  |
| --- | --- | --- |
|  | u​(t,x)=1π​(sin⁡(θ​(t,x))+cos⁡(θ​(t,x))),u(t,x)=\frac{1}{\pi}\big(\sin(\theta(t,x))+\cos(\theta(t,x))\big), |  |

where

|  |  |  |
| --- | --- | --- |
|  | θ​(t,x)≔2​π​(∑i=1dxi+(T−t)).\theta(t,x)\coloneqq 2\pi\Bigg(\sum\_{i=1}^{d}x\_{i}+(T-t)\Bigg). |  |

The spatial derivatives of uu are given by

|  |  |  |
| --- | --- | --- |
|  | ∂u∂xi​(t,x)=2​(cos⁡(θ​(t,x))−sin⁡(θ​(t,x))),i∈{1,…,d},\frac{\partial u}{\partial x\_{i}}(t,x)=2\big(\cos(\theta(t,x))-\sin(\theta(t,x))\big),\;i\in\{1,\dots,d\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∂2u∂xi​∂xj​(t,x)=−4​π​(sin⁡(θ​(t,x))+cos⁡(θ​(t,x))),(i,j)∈{1,…,d}2.\frac{\partial^{2}u}{\partial x\_{i}\partial x\_{j}}(t,x)=-4\pi\big(\sin(\theta(t,x))+\cos(\theta(t,x))\big),\;(i,j)\in\{1,\dots,d\}^{2}. |  |

### C.2 Linear–quadratic (LQ) case

We consider a linear–quadratic case from [[78](https://arxiv.org/html/2511.01125v1#bib.bib78)] in d=5d=5 dimension, with T=1T=1. The forward SDE is a controlled process XtX\_{t} in ℝd\mathbb{R}^{d}, defined by

|  |  |  |
| --- | --- | --- |
|  | d​Xt=(A​Xt+B​αt)​d​t+D​αt​d​Wt,\mathrm{d}X\_{t}=(AX\_{t}+B\alpha\_{t})\mathrm{d}t+D\alpha\_{t}\mathrm{d}W\_{t}, |  |

where αt\alpha\_{t} is a control process in ℝ\mathbb{R}, (B,D)∈ℝd×ℝd(B,D)\in\mathbb{R}^{d}\times\mathbb{R}^{d} and A∈ℝd×dA\in\mathbb{R}^{d\times d}. The quadratic cost that is minimised is

|  |  |  |
| --- | --- | --- |
|  | J​(α)≔𝔼​b​i​g​g​[∫0T(Xt⊤​Q​Xt+αt2​N)​dt+XT⊤​P​XT],J(\alpha)\coloneqq\mathbb{E}\\ bigg[\int\_{0}^{T}\big(X\_{t}^{\top}QX\_{t}+\alpha\_{t}^{2}N\big)\mathrm{d}t+X\_{T}^{\top}PX\_{T}\bigg], |  |

where PP and QQ are non-negative, symmetric d×dd\times d matrices and N>0N>0.

The Bellman PDE associated with this process admits an explicit solution given by a quadratic form

|  |  |  |
| --- | --- | --- |
|  | u​(t,x)=xT​K​(t)​x,u(t,x)=x^{T}K(t)x, |  |

where K​(t)K(t) solves the Ricatti equation

|  |  |  |
| --- | --- | --- |
|  | K˙+A⊤​K+K​A+Q−K​B​B⊤​KN+D⊤​K​D=0,K​(T)=P.\dot{K}+A^{\top}K+KA+Q-\frac{KBB^{\top}K}{N+D^{\top}KD}=0,\;K(T)=P. |  |

In all the simulations, we set

|  |  |  |
| --- | --- | --- |
|  | A=Id,B=D=Id,Q=P=1d​Id,N=d.A=\mathrm{I}\_{d},\;B=D=\mathrm{I}\_{d},\;Q=P=\frac{1}{d}\mathrm{I}\_{d},\;N=d. |  |

The stochastic coefficients associated to the controlled process are set to

|  |  |  |
| --- | --- | --- |
|  | σ=1d​Id,and​μ​(t,x)=x.\sigma=\frac{1}{\sqrt{d}}\mathrm{I}\_{d},\;\textnormal{and}\;\mu(t,x)=x. |  |

In our isotropic setup, the Riccati matrix remains proportional to the identity, *i.e.*

|  |  |  |
| --- | --- | --- |
|  | K​(t)=k​(t)​Id.K(t)=k(t)\mathrm{I}\_{d}. |  |

Then, the explicit forms of the spatial derivatives of uu are given by

|  |  |  |
| --- | --- | --- |
|  | ∇xu​(t,x)=2​K​(t)​x=2​k​(t)​x,Dx2​u​(t,x)=2​K​(t)=2​k​(t)​Id.\nabla\_{x}u(t,x)=2K(t)x=2k(t)x,\;D\_{x}^{2}u(t,x)=2K(t)=2k(t)\mathrm{I}\_{d}. |  |

To compute the solution uu and its derivatives, we employ a fourth-order Runge-–Kutta (RK4) scheme to numerically approximate K​(t)K(t) (the solution of the Riccati equation).

### C.3 Architectural details

The KANO architecture follows a lift-–process–=project design. The input features are first lifted to a higher-dimensional latent space using a feed-forward network, producing an initial latent representation v(0)v^{(0)}.

After lifting, a composition of several KANO blocks is applied to iteratively refine this latent field:

|  |  |  |
| --- | --- | --- |
|  | v(ℓ+1)=Φ(ℓ)​(v(ℓ),x),ℓ∈{0,…,L−1},v^{(\ell+1)}=\Phi^{(\ell)}(v^{(\ell)},x),\;\ell\in\{0,\dots,L-1\}, |  |

where each block Φ(ℓ)\Phi^{(\ell)} performs a structured operator update combining coordinate encoding, spectral convolution, and residual connection. Each KANO block consists of three main components

1. 1.

   a positional encoder maps the spatial coordinates through a Res–KAN network, producing coordinate-dependent features

   |  |  |  |
   | --- | --- | --- |
   |  | vpos=b​(x);v\_{\mathrm{pos}}=b(x); |  |
2. 2.

   a spectral kernel path performs a spectral convolution in the frequency domain, analogous to the Fourier neural operator (FNO) [[60](https://arxiv.org/html/2511.01125v1#bib.bib60)]. Specifically, the feature field is transformed via a two-dimensional fast Fourier transform (FFT), filtered by learnable complex-valued multipliers, and then mapped back to the spatial domain

   |  |  |  |
   | --- | --- | --- |
   |  | vkf​(x)=ℱ−1​(W^​(k)​ℱ​[vin]​(k)),v\_{\mathrm{kf}}(x)=\mathcal{F}^{-1}\big(\hat{W}(k)\mathcal{F}[v\_{\mathrm{in}}](k)\big), |  |

   where ℱ\mathcal{F} and ℱ−1\mathcal{F}^{-1} denote the forward and inverse Fourier transforms, and W^​(k)\hat{W}(k) are learnable complex weights restricted to a finite number of Fourier modes and parametrised as Res–KANs;
3. 3.

   a residual path applies a Res–KAN transformation on the tensor obtained by concatenating (vpos,vkf,vin)\big(v\_{\mathrm{pos}},v\_{\mathrm{kf}},v\_{\mathrm{in}}\big).

After stacking LL such KANO blocks, the resulting field v(L)v^{(L)} is projected back to the target dimension through a final projection layer. This composition enables multiscale feature extraction, efficient global coupling through spectral convolution, and local adaptivity through Res–KAN-based non-linear transformations.

We restrict our training to a 22D uniform grid that spans the first two coordinates of the dd-dimensional space, while conditioning the model pointwise on the remaining d−2d-2 coordinates. The procedure for generating random training samples is described in detail in [Section˜C.4](https://arxiv.org/html/2511.01125v1#A3.SS4 "C.4 Training pipeline ‣ Appendix C Experimental details ‣ One model to solve them all: 2BSDE families via neural operators"). Our model is trained to approximate 2D slices of the solution along the (x1,x2)(x\_{1},x\_{2})-coordinates in ℝ+×ℝd\mathbb{R\_{+}}\times\mathbb{R}^{d}. Once trained, the model can be evaluated at any point in time and space by approximating the solution over these 2D slices and querying the corresponding (x1,x2)(x\_{1},x\_{2}) values (see [Section˜C.5](https://arxiv.org/html/2511.01125v1#A3.SS5 "C.5 Inference pipeline ‣ Appendix C Experimental details ‣ One model to solve them all: 2BSDE families via neural operators") for details). This type of restricted operator learning is efficient due to the following reasons.

* •

  Uniform grids enable efficient kernels. During training, the coordinates (x1,x2)(x\_{1},x\_{2}) are placed on a uniform grid, enabling convolution-like kernel layers to be computed efficiently via FFTs. This reduces the per-layer complexity from dense O​(s4)O(s^{4}) to O​(s2​log⁡s)O(s^{2}\log s), making spectral kernels both computationally efficient and numerically stable.
* •

  Learning high-dimensional maps through 2D evaluations.
  The operator is evaluated over the full s2s^{2} grid simultaneously, while the remaining coordinates (x3,…,xd)(x\_{3},\dots,x\_{d}) and time tt are provided as additional input channels. This setup allows the network to capture intrinsic symmetries in the problem and to perform restricted operator learning, approximating u​(t,x)u(t,x) across ℝd\mathbb{R}^{d} by predicting values at multiple 22D locations in parallel.
* •

  2D offers the optimal balance; 3D becomes costly.
  Extending the FFT-based grid to three dimensions increases computational and memory demands to O​(s3​log⁡s)O(s^{3}\log s) per pass and substantially raises activation and storage costs. In practice, 22D grids strike the best balance between expressivity (capturing many spatial query points per sample) and efficiency, while still encoding dd-dimensional dependencies through the auxiliary input channels.

Note that spectral convolution on uniform grids is employed to improve the training efficiency of the model. In operator learning settings, various efficient kernel architectures exist, see [Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, and Anandkumar](https://arxiv.org/html/2511.01125v1#bib.bib47) [[47](https://arxiv.org/html/2511.01125v1#bib.bib47)], including convolution-based kernels, see [Raonić, Molinaro, de Ryck, Rohner, Bartolucci, Alaifari, Mishra, and de Bézenac](https://arxiv.org/html/2511.01125v1#bib.bib81) [[81](https://arxiv.org/html/2511.01125v1#bib.bib81)], wavelet-based kernels, see [Tripura and Chakraborty](https://arxiv.org/html/2511.01125v1#bib.bib91) [[91](https://arxiv.org/html/2511.01125v1#bib.bib91)], and transformer-based kernels, see [Herde, Raonić, Rohner, Käppeli, Molinaro, de Bézenac, and Mishra](https://arxiv.org/html/2511.01125v1#bib.bib40) [[40](https://arxiv.org/html/2511.01125v1#bib.bib40)] or [Li, Meidani, and Farimani](https://arxiv.org/html/2511.01125v1#bib.bib61) [[61](https://arxiv.org/html/2511.01125v1#bib.bib61)], among others. The choice of the spectral kernel here is made solely to demonstrate that training a neural operator in the 2BSDE setting is feasible.

### C.4 Training pipeline

In all our experiments, we draw samples from the domain uniformly. To draw a random training sample, we first draw a random time, as well as random locations for the d−2d-2 dimensions (the first 2 dimensions (x​1,x​2)(x1,x2) are already sampled on uniform grids),

|  |  |  |
| --- | --- | --- |
|  | t∈[0,T],c=(x3,…,xd)∈[0,1)d−2.t\in[0,T],\;c=(x\_{3},\dots,x\_{d})\in[0,1)^{d-2}. |  |

To get the training samples, we evaluate the model on a *uniform* s×ss\times s grid for the first two coordinates

|  |  |  |
| --- | --- | --- |
|  | 𝒢≔{(x1p,x2q):x1p=ps−1,x2q=qs−1,(p,q)∈{0,…,s−1}2},\mathcal{G}\coloneqq\bigg\{(x\_{1}^{p},x\_{2}^{q}):x\_{1}^{p}=\frac{p}{s-1},\;x\_{2}^{q}=\frac{q}{s-1},\;(p,q)\in\{0,\dots,s-1\}^{2}\bigg\}, |  |

and denote N≔s2N\coloneqq s^{2} and X≔((x1​n,x2​n))n∈{1,…,N}X\coloneqq\big((x\_{1n},x\_{2n})\big)\_{n\in\{1,\dots,N\}} the grid.

At each grid node nn, the model receives the feature vector

|  |  |  |
| --- | --- | --- |
|  | ϕn≔(t,X,x3,…,xd)∈ℝ1+2+(d−2)=ℝd+1,\phi\_{n}\coloneqq\big(t,\,X,\,x\_{3},\dots,x\_{d}\big)\in\mathbb{R}^{1+2+(d-2)}=\mathbb{R}^{d+1}, |  |

*i.e.* time and the (d−2)(d-2) extra coordinates are *channels* constant across the 2d grid. A neural operator FθF\_{\theta} maps these inputs to the ℝs×s\mathbb{R}^{s\times s} field,

|  |  |  |
| --- | --- | --- |
|  | u^θ​(t,X,x3,…,xd)=Fθ​(ϕn)∈ℝs×s.\hat{u}\_{\theta}\big(t,X,x\_{3},\dots,x\_{d}\big)=F\_{\theta}\big(\phi\_{n}\big)\in\mathbb{R}^{s\times s}. |  |

### C.5 Inference pipeline

At test time, the learned approximation u^θ\hat{u}\_{\theta} can be evaluated at any query (t,x)(t,x) in the domain by either of the following.

* •

  *Spectral/Fourier synthesis.*
  If the decoder is spectral, we evaluate the Fourier–like synthesis operator at the desired coordinates to obtain u^θ​(t,x)\hat{u}\_{\theta}(t,x) directly.
  This is naturally suited to periodic problems and preserves differentiability with respect to (t,x)(t,x), enabling gradients to be obtained by automatic differentiation.
* •

  *Grid interpolation.*
  When the model outputs values on a uniform s×ss\times s grid in (x1,x2)(x\_{1},x\_{2}) at a given time tt, we interpolate that grid to any (x1,x2)(x\_{1},x\_{2}) in the domain (*e.g.* bilinear/bicubic interpolation).
  This route is simple, fast, and it requires no change to the trained model.

To evaluate the models along random paths, we generate dd-dimensional SDE trajectories using the Euler–Maruyama scheme,

|  |  |  |
| --- | --- | --- |
|  | Xn+1(i)=Xn(i)+bi​(Xn(i))​Δ​t+σi,i​(Xn(i))​Δ​t​ξn(i),ξn(i)∼𝒩​(0,1).X\_{n+1}^{(i)}=X\_{n}^{(i)}+b\_{i}(X\_{n}^{(i)})\Delta t+\sigma\_{i,i}(X\_{n}^{(i)})\sqrt{\Delta t}\xi\_{n}^{(i)},\;\xi\_{n}^{(i)}\sim\mathcal{N}(0,1). |  |

The trained model is then evaluated along these trajectories, and its predictions are compared against the exact solution uu and its first- and second-order partial derivatives. Derivatives of the neural operator are approximated using first-order finite difference scheme. To obtain model outputs at arbitrary spatial locations, we employ bilinear interpolation over the (x1,x2)(x\_{1},x\_{2}) grid.

## References

* Acciaio et al. [2024]

  B. Acciaio, A. Kratsios, and G. Pammer.
  Designing universal causal deep learning models: the geometric (hyper) transformer.
  *Mathematical Finance*, 34(2):671–735, 2024.
* Adcock et al. [2022]

  B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga.
  On efficient algorithms for computing near-best polynomial approximations to high-dimensional, Hilbert-valued functions from limited samples.
  *ArXiv preprint arXiv:2203.13908*, 2022.
* Adcock et al. [2024]

  B. Adcock, N. Dexter, and S. Moraga Scheuermann.
  Optimal deep learning of holomorphic operators between banach spaces.
  In A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, editors, *Proceedings of the 38th conference on advances in neural information processing systems ((NeurIPS 2024)), December 10–15, 2024, Vancouver, British Columbia, Canada*, volume 37, pages 27725–27789, 2024.
* Adcock et al. [2025]

  B. Adcock, S. Brugiapaglia, N. Dexter, and S. Moraga.
  Near-optimal learning of Banach-valued, high-dimensional functions via deep neural networks.
  *Neural Networks*, 181(106761):1–25, 2025.
* Alvarez et al. [2024]

  G. Alvarez, I. Ekren, A. Kratsios, and X. Yang.
  Neural operators can play dynamic Stackelberg games.
  *ArXiv preprint arXiv:2411.09644*, 2024.
* Arabpour et al. [2024]

  R. Arabpour, J. Armstrong, L. Galimberti, A. Kratsios, and G. Livieri.
  Low-dimensional approximations of the conditional law of Volterra processes: a non-positive curvature approach.
  *ArXiv preprint arXiv:2405.20094*, 2024.
* Beck et al. [2019]

  C. Beck, W. E, and A. Jentzen.
  Machine learning approximation algorithms for high-dimensional fully nonlinear partial differential equations and second-order backward stochastic differential equations.
  *Journal of Nonlinear Science*, 29(4):1563–1619, 2019.
* Benth et al. [2023]

  F. E. Benth, N. Detering, and L. Galimberti.
  Neural networks in Fréchet spaces.
  *Annals of Mathematics and Artificial Intelligence*, 91(1):75–103, 2023.
* Bilokopytov and Xanthos [2025]

  E. Bilokopytov and F. Xanthos.
  A universal approximation theorem and its applications to vector lattice theory.
  *ArXiv preprint arXiv:2507.20219*, 2025.
* Bolcskei et al. [2019]

  Helmut Bolcskei, Philipp Grohs, Gitta Kutyniok, and Philipp Petersen.
  Optimal approximation with sparsely connected deep neural networks.
  *SIAM Journal on Mathematics of Data Science*, 1(1):8–45, 2019.
* Cao and Wan [2022]

  D. Cao and J. Wan.
  Expansion of Green’s function and regularity of Robin’s function for elliptic operators in divergence form.
  *Annali della Scuola Normale Superiore di Pisa - Classe di Scienze*, to appear, 2022.
* Chan et al. [2015]

  T.-H. Chan, K. Jia, S. Gao, J. Lu, Z. Zeng, and Y. Ma.
  PCANet: simple deep learning baseline for image classification?
  *IEEE Transactions on Image Processing*, 24(12):5017–5032, 2015.
* Chassagneux et al. [2023]

  J.-F. Chassagneux, J. Chen, N. Frikha, and C. Zhou.
  A learning scheme by sparse grids and Picard approximations for semilinear parabolic pdes.
  *IMA Journal of Numerical Analysis*, 43(5):3109–3168, 2023.
* Chen and Chen [1993]

  T. Chen and H. Chen.
  Approximations of continuous functionals by neural networks with application to dynamic systems.
  *IEEE Transactions on Neural Networks*, 4(6):910–918, 1993.
* Chen and Chen [1995]

  T. Chen and H. Chen.
  Universal approximation to nonlinear operators by neural networks with arbitrary activation functions and its application to dynamical systems.
  *IEEE Transactions on Neural Networks*, 6(4):911–917, 1995.
* Cheridito et al. [2007]

  P. Cheridito, H. M. Soner, N. Touzi, and N. Victoir.
  Second-order backward stochastic differential equations and fully nonlinear parabolic PDEs.
  *Communications on Pure and Applied Mathematics*, 60(7):1081–1110, 2007.
* Cuchiero et al. [2023]

  C. Cuchiero, P. Schmocker, and J. Teichmann.
  Global universal approximation of functional input maps on weighted spaces.
  *ArXiv preprint arXiv:2306.03303*, 2023.
* Daubechies [1988]

  I. Daubechies.
  Orthonormal bases of compactly supported wavelets.
  *Communications on Pure and Applied Mathematics*, 41(7):909–996, 1988.
* Daubechies [1992]

  I. Daubechies.
  *Ten lectures on wavelets*, volume 61 of *CBMS–NSF regional conference series in applied mathematics*.
  Society for Industrial and Applied Mathematics, Philadelphia, Pennsylvania, 1992.
* de Hoop et al. [2022]

  M. V. de Hoop, M. Lassas, and C. A. Wong.
  Deep learning architectures for nonlinear operator functions and nonlinear inverse problems.
  *Mathematical Statistics and Learning*, 4(1):1–86, 2022.
* de Marco [2011]

  S. de Marco.
  Smoothness and asymptotic estimates of densities for SDEs with locally smooth coefficients and applications to square root–type diffusions.
  *The Annals of Applied Probability*, 21(4):1282–1321, 2011.
* DeVore and Sharpley [1993]

  R. A. DeVore and R. C. Sharpley.
  Besov spaces on domains in ℝ𝕕\mathbb{{R}^{d}}.
  *Transactions of the American Mathematical Society*, 335(2):843–864, 1993.
* DeVore et al. [2021]

  Ronald DeVore, Boris Hanin, and Guergana Petrova.
  Neural network approximation.
  *Acta Numerica*, 30:327–444, 2021.
* Duong [2023]

  H. Duong.
  *Solving high-dimensional fully nonlinear convex partial differential equations using deep learning*.
  PhD thesis, Florida State University, 2023.
* E and Wang [2018]

  W. E and Q. Wang.
  Exponential convergence of the deep neural network approximation for analytic functions.
  *Science China Mathematics*, 61(10):1733–1740, 2018.
* Evans [2010]

  L. C. Evans.
  *Partial differential equations*, volume 19 of *Graduate studies in mathematics*.
  American Mathematical Society, 2nd edition, 2010.
* Fefferman [2006]

  C. Fefferman.
  Whitney’s extension problem for Cm{C}^{m}.
  *Annals of Mathematics*, 164:313–359, 2006.
* Fefferman et al. [2014]

  C. Fefferman, A. Israel, and G. Luli.
  Sobolev extension by linear operators.
  *Journal of the American Mathematical Society*, 27(1):69–145, 2014.
* Firoozi et al. [2025]

  D. Firoozi, A. Kratsios, and X. Yang.
  Simultaneously solving infinitely many LQ mean field games in Hilbert spaces: the power of neural operators.
  *ArXiv preprint arXiv:2510.20017*, 2025.
* Firouzi et al. [2025]

  D. Firouzi, X. Yang, and A. Kratsios.
  Simultaneously solving infinitely many LQ mean field games in Hilbert spaces: the power of neural operators.
  *In preparation*, 2025.
* Furuya and Kratsios [2024]

  T. Furuya and A. Kratsios.
  Simultaneously solving FBSDEs with neural operators of logarithmic depth, constant width, and sub-linear rank.
  *ArXiv preprint arXiv:2410.14788*, 2024.
* Furuya et al. [2025]

  T. Furuya, K. Taniguchi, and S. Okuda.
  Quantitative approximation for neural operators in nonlinear parabolic equations.
  In *The thirteenth international conference on learning representations ((ICLR 2025)), April 24–28, 2025, Singapore*, pages 1–29, 2025.
* Galimberti et al. [2025]

  L. Galimberti, A. Kratsios, and G. Livieri.
  Designing universal causal deep learning models: the case of infinite-dimensional dynamical systems from stochastic analysis.
  *Constructive Approximation*, to appear, 2025.
* Germain et al. [2022a]

  M. Germain, M. Laurière, H. Pham, and X. Warin.
  DeepSets and their derivative networks for solving symmetric PDEs.
  *Journal of Scientific Computing*, 91(63):1–33, 2022a.
* Germain et al. [2022b]

  M. Germain, H. Pham, and X. Warin.
  Approximation error analysis of some deep backward schemes for nonlinear PDEs.
  *SIAM Journal on Scientific Computing*, 44(1):A28–A56, 2022b.
* Germain et al. [2023]

  M. Germain, H. Pham, and X. Warin.
  Neural networks–based algorithms for stochastic control and PDEs in finance.
  In A. Capponi and C.-A. Lehalle, editors, *Machine learning and data sciences for financial markets*, pages 426–452. Cambridge University Press, 2023.
* Gilbarg and Trudinger [2001]

  D. Gilbarg and N. S. Trudinger.
  *Elliptic partial differential equations of second order*, volume 224 of *Classics in mathematics*.
  Springer Berlin, Heidelberg, second edition, 2001.
* Gödeke and Fernsel [2025]

  J. Gödeke and P. Fernsel.
  New universal operator approximation theorem for encoder–decoder architectures.
  *ArXiv preprint arXiv:2503.24092*, 2025.
* Gribonval et al. [2022]

  R. Gribonval, G. Kutyniok, M. Nielsen, and F. Voigtlaender.
  Approximation spaces of deep neural networks.
  *Constructive Approximation*, 55(1):259–367, 2022.
* Herde et al. [2024]

  Maximilian Herde, B. Raonić, T. Rohner, R. Käppeli, R. Molinaro, E. de Bézenac, and S. Mishra.
  Poseidon: efficient foundation models for PDEs.
  In *Proceedings of the 38th conference on advances in neural information processing systems ((NeurIPS 2024)), December 10–15, 2024, Vancouver, British Columbia, Canada*, volume 37, pages 72525–72624, 2024.
* Hong and Kratsios [2024]

  Ruiyang Hong and Anastasis Kratsios.
  Bridging the gap between approximation and learning via optimal approximation by relu mlps of maximal regularity.
  *arXiv preprint arXiv:2409.12335*, 2024.
* Horvath et al. [2023]

  B. Horvath, A. Kratsios, Y. Limmer, and X. Yang.
  Deep Kalman filters can filter.
  *SSRN preprint 4615215*, 2023.
* Horvath et al. [2025]

  B. Horvath, A. Kratsios, Y. Limmer, and X. Yang.
  Transformers can solve non-linear and non-Markovian filtering problems in continuous time for conditionally Gaussian signals.
  *ArXiv preprint arXiv:2310.19603*, 2025.
* Hu and Laurière [2024]

  R. Hu and N. Laurière.
  Recent developments in machine learning methods for stochastic control and games.
  *Numerical Algebra, Control and Optimization*, 14(3):435–525, 2024.
* Kim and Sakellaris [2019]

  S. Kim and G. Sakellaris.
  Green’s function for second order elliptic equations with singular lower order coefficients.
  *Communications in Partial Differential Equations*, 44(3):228–270, 2019.
* Korolev [2022]

  Y. Korolev.
  Two-layer neural networks with values in a Banach space.
  *SIAM Journal on Mathematical Analysis*, 54(6):6358–6389, 2022.
* Kovachki et al. [2023]

  N. B. Kovachki, Z. Li, B. Liu, K. Azizzadenesheli, K. Bhattacharya, A. M. Stuart, and A. Anandkumar.
  Neural operator: learning maps between function spaces with applications to PDEs.
  *Journal of Machine Learning Research*, 24(89):1–97, 2023.
* Kratsios and Furuya [2025]

  A. Kratsios and T. Furuya.
  Kolmogorov–Arnold networks: approximation and learning guarantees for functions and their derivatives.
  *ArXiv preprint arXiv:2504.15110*, 2025.
* Kratsios et al. [2023]

  A. Kratsios, C. Liu, M. Lassas, M. V. de Hoop, and I. Dokmanic.
  Universal geometric deep learning via geometric attention.
  *ArXiv preprint arXiv:2304.12231*, 2023.
* Kratsios et al. [2024]

  A. Kratsios, T. Furuya, J. A. L. Benitez, M. Lassas, and M. de Hoop.
  Mixture of experts soften the curse of dimensionality in operator learning.
  *ArXiv preprint arXiv:2404.09101*, 2024.
* Kratsios et al. [2025a]

  A. Kratsios, A. Neufeld, and P. Schmocker.
  Generative neural operators of log-complexity can simultaneously solve infinitely many convex programs.
  *ArXiv preprint arXiv:2508.14995*, 2025a.
* Kratsios et al. [2025b]

  A. Kratsios, P. Schmocker, and P. Zimmermann.
  Deep inverse problem for double phase equation.
  *In preparation*, 2025b.
* Kratsios and Zamanlooy [2022]

  K. Kratsios and B. Zamanlooy.
  Do ReLU networks have an edge when approximating compactly-supported functions?
  *Transactions on Machine Learning Research*, August:1–22, 2022.
* Krylov [2018]

  N. V. Krylov.
  *Sobolev and viscosity solutions for fully nonlinear elliptic and parabolic equations*, volume 233 of *Mathematical surveys and monographs*.
  American Mathematical Society, Providence, Rhode Island, 2018.
* Lanthaler and Stuart [2025]

  S. Lanthaler and A. M. Stuart.
  The parametric complexity of operator learning.
  *IMA Journal of Numerical Analysis*, to appear, 2025.
* Lanthaler et al. [2022]

  S. Lanthaler, S. Mishra, and G. E. Karniadakis.
  Error estimates for DeepONets: a deep learning framework in infinite dimensions.
  *Transactions of Mathematics and Its Applications*, 6(1):1–141, 2022.
* Lanthaler et al. [2025]

  S. Lanthaler, Z. Li, and A. M. Stuart.
  Nonlocality and nonlinearity implies universality in operator learning.
  *Constructive Approximation*, 62:261–303, 2025.
* Lefebvre et al. [2023]

  W. Lefebvre, G. Loeper, and H. Pham.
  Differential learning methods for solving fully nonlinear PDEs.
  *Digital Finance*, 5(1):183–229, 2023.
* Li et al. [2020]

  B. Li, S. Tang, and H. Yu.
  Better approximations of high dimensional smooth functions by deep neural networks with rectified power units.
  *Communications in Computational Physics*, 27:379–411, 2020.
* Li et al. [2021]

  Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, and A. Anandkumar.
  Fourier neural operator for parametric partial differential equations.
  In *International conference on learning representations ((ICLR 2021))*, pages 1–16, 2021.
* Li et al. [2023]

  Z. Li, K. Meidani, and A. B. Farimani.
  Transformer for partial differential equations’ operator learning.
  *Transactions on Machine Learning Research*, April:1–34, 2023.
* Liu et al. [2025]

  Z. Liu, Y. Wang, S. Vaidya, F. Ruehle, J. Halverson, M. Soljacic, T. Y. Hou, and M. Tegmark.
  KAN: Kolmogorov–Arnold networks.
  In *The thirteenth international conference on learning representations ((ICLR 2025))*, pages 1–47, 2025.
* Lu et al. [2019]

  L. Lu, P. Jin, and G. E. Karniadakis.
  DeepONet: learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators.
  *ArXiv preprint arXiv:1910.03193*, 2019.
* Lu et al. [2021]

  L. Lu, P. Jin, G. Pang, Z. Zhang, and G. E. Karniadakis.
  Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators.
  *Nature Machine Intelligence*, 3:218–229, 2021.
* Mallat [1989]

  S. G. Mallat.
  Multiresolution approximations and wavelet orthonormal bases of L2​(𝕣){L}^{2}({\mathbb{r}}).
  *Transactions of the American Mathematical Society*, 315(1):69–87, 1989.
* Marcati and Schwab [2023]

  C. Marcati and C. Schwab.
  Exponential convergence of deep operator networks for elliptic partial differential equations.
  *SIAM Journal on Numerical Analysis*, 61(3):1513–1545, 2023.
* Marcati and Schwab [2025]

  C. Marcati and C. Schwab.
  Expression rates of neural operators for linear elliptic PDEs in polytopes.
  *Foundations of Computational Mathematics*, to appear, 2025.
* Mhaskar [1996]

  H. N. Mhaskar.
  Neural networks for optimal approximation of smooth and analytic functions.
  *Neural Computation*, 8(1):164–177, 1996.
* Mhaskar and Micchelli [1995]

  H. N. Mhaskar and C. A. Micchelli.
  Degree of approximation by neural and translation networks with a single hidden layer.
  *Advances in Applied Mathematics*, 16(2):151–183, 1995.
* Mhaskar and Micchelli [1992]

  H. N. Mhaskar and Charles A. Micchelli.
  Approximation by superposition of sigmoidal and radial basis functions.
  *Advances in Applied Mathematics*, 13(3):350–373, 1992.
* Munkres [2000]

  J. R. Munkres.
  *Topology*.
  Prentice Hall, Inc., Upper Saddle River, NJ, second edition, 2000.
* Neufeld and Schmocker [2023]

  A. Neufeld and P. Schmocker.
  Universal approximation property of Banach space–valued random feature models including random neural networks.
  *ArXiv preprint arXiv:2312.08410*, 2023.
* Nguwi et al. [2024]

  J. Y. Nguwi, G. Penent, and N. Privault.
  A deep branching solver for fully nonlinear partial differential equations.
  *Journal of Computational Physics*, 499:112712, 2024.
* Nüsken and Richter [2021]

  N. Nüsken and L. Richter.
  Solving high-dimensional Hamilton–Jacobi–Bellman PDEs using neural networks: perspectives from the theory of controlled diffusions and measures on path space.
  *Partial Differential Equations and Applications*, 2(48):1–48, 2021.
* Pak et al. [2025]

  C.-G. Pak, H.-J. Hwang, and M.-C. Kim.
  A nonequidistant multistep scheme for second order backward stochastic differential equations with applications to stochastic optimal control.
  *International Journal of Applied and Computational Mathematics*, 11(58):1–19, 2025.
* Pardoux [1998]

  É. Pardoux.
  Backward stochastic differential equations and viscosity solutions of systems of semilinear parabolic and elliptic PDEs of second order.
  In L. Decreusefond, B. Øksendal, J. Gjerde, and Üstünel A.S., editors, *Stochastic analysis and related topics VI. Proceedings of the sixth Oslo–Silivri workshop, Geilo, 1996*, volume 42 of *Progress in probability*, pages 79–127, 1998.
* Pereira et al. [2020]

  M. Pereira, Z. Wang, T. Chen, E. Reed, and E. Theodorou.
  Feynman–Kac neural network architectures for stochastic control using second-order FBSDE theory.
  In *Proceedings of the 2nd conference on learning for dynamics and control*, volume 120 of *Proceedings of machine learning research*, pages 728–738, 2020.
* Pham et al. [2021]

  H. Pham, X. Warin, and M. Germain.
  Neural networks-based backward scheme for fully nonlinear PDEs.
  *SN Partial Differential Equations and Applications*, 2(16):1–24, 2021.
* Pollard [1984]

  D. Pollard.
  *Convergence of stochastic processes*.
  Springer series in statistics. Springer New York, NY, 1984.
* Possamaï and Tan [2015]

  D. Possamaï and X. Tan.
  Weak approximation of second-order BSDEs.
  *The Annals of Applied Probability*, 25(5):2535–2562, 2015.
* Raonić et al. [2023]

  B. Raonić, R. Molinaro, T. de Ryck, T. Rohner, F. Bartolucci, R. Alaifari, S. Mishra, and E. de Bézenac.
  Convolutional neural operators for robust and accurate learning of PDEs.
  In *Proceedings of the 37th conference on advances in neural information processing systems ((NeurIPS 2023)), December 10–16, 2023, New Orleans, Louisiana, United States of America*, volume 36, pages 77187–77200, 2023.
* Ren and Tan [2017]

  Z. Ren and X. Tan.
  On the convergence of monotone schemes for path-dependent PDE.
  *Stochastic Processes and their Applications*, 127(6):1738–1762, 2017.
* Riedi et al. [2023]

  R. H. Riedi, R. Balestriero, and R. G. Baraniuk.
  Singular value perturbation and deep network optimization.
  *Constructive Approximation*, 57(2):807–852, 2023.
* Schneider et al. [2025]

  Cornelia Schneider, Mario Ullrich, and Jan Vybiral.
  Nonlocal techniques for the analysis of deep relu neural network approximations.
  *arXiv preprint arXiv:2504.04847*, 2025.
* Schwab et al. [2025]

  C. Schwab, A. Stein, and J. Zech.
  Deep operator network approximation rates for Lipschitz operators.
  *Analysis and Applications*, to appear, 2025.
* Shen et al. [2022]

  Z. Shen, H. Yang, and S. Zhang.
  Deep network approximation: achieving arbitrary accuracy with fixed number of neurons.
  *Journal of Machine Learning Research*, 23(276):1–60, 2022.
* Soner et al. [2012]

  H. M. Soner, N. Touzi, and J. Zhang.
  Wellposedness of second order backward SDEs.
  *Probability Theory and Related Fields*, 153(1–2):149–190, 2012.
* Taylor [2023]

  M. E. Taylor.
  *Partial differential equations I. Basic theory*, volume 115 of *Applied mathematical sciences*.
  Springer Cham, third edition, 2023.
* Triebel [2006]

  H. Triebel.
  *Theory of function spaces. III*, volume 100 of *Monographs in mathematics*.
  Birkhäuser Basel, 2006.
* Triebel [2008]

  H. Triebel.
  *Function spaces and wavelets on domains*, volume 7 of *Tracts in mathematics*.
  European Mathematical Society, Zürich, 2008.
* Tripura and Chakraborty [2022]

  T. Tripura and S. Chakraborty.
  Wavelet neural operator: a neural operator for parametric partial differential equations.
  *ArXiv preprint arXiv:2205.02191*, 2022.
* Wang et al. [2024]

  Y. Wang, J. W. Siegel, Z. Liu, and T. Y. Hou.
  On the expressiveness and spectral bias of KANs.
  *ArXiv preprint arXiv:2410.01803*, 2024.
* Xiao et al. [2024]

  X. Xiao, W. Qiu, and O. Nikan.
  Numerical approximation based on deep convolutional neural network for high-dimensional fully nonlinear merged PDEs and 2BSDEs.
  *Mathematical Methods in the Applied Sciences*, 47(7):6184–6204, 2024.
* Yang et al. [2019]

  J. Yang, W. Zhao, and T. Zhou.
  Explicit deferred correction methods for second-order forward backward stochastic differential equations.
  *Journal of Scientific Computing*, 79(3):1409–1432, 2019.
* Yarotsky [2017]

  D. Yarotsky.
  Error bounds for approximations with deep ReLU networks.
  *Neural Networks*, 94:103–114, 2017.
* Yu et al. [2021]

  A. Yu, C. Becquey, D. Halikias, M. E. Mallory, and A. Townsend.
  Arbitrary-depth universal approximation theorems for operator neural networks.
  *ArXiv preprint arXiv:2109.11354*, 2021.
* Zhou et al. [2021]

  M. Zhou, J. Han, and J. Lu.
  Actor–critic method for high dimensional static Hamilton–Jacobi–Bellman partial differential equations based on neural networks.
  *SIAM Journal on Scientific Computing*, 43(6):A4043–A4066, 2021.