---
authors:
- Ivan Guo
- Severin Nilsson
- Johannes Wiesel
doc_id: arxiv:2511.21287v1
family_id: arxiv:2511.21287
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Dynamic characterization of barycentric optimal transport problems and their
  martingale relaxation
url_abs: http://arxiv.org/abs/2511.21287v1
url_html: https://arxiv.org/html/2511.21287v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ivan Guo
Ivan Guo
  
   School of Mathematics
  
   Monash University
[Ivan.Guo@monash.edu](mailto:Ivan.Guo@monash.edu)
, 
Severin Nilsson
Severin Nilsson
  
   Department of Mathematics
  
   Carnegie Mellon University
[snilsson@andrew.cmu.edu](mailto:snilsson@andrew.cmu.edu)
 and 
Johannes Wiesel
Johannes Wiesel
  
   Department of Mathematics
  
   University of Copenhagen
[wiesel@math.ku.dk](mailto:wiesel@math.ku.dk)

(Date: November 26, 2025)

###### Abstract.

We extend the Benamou-Brenier formula from classical optimal transport to weak optimal transport and show that the barycentric optimal transport problem studied by Gozlan and Juillet has a dynamic analogue. We also investigate a martingale relaxation of this problem, and relate it to the martingale Benamou-Brenier formula of Backhoﬀ-Veraguas, Beiglböck, Huesmann and Källblad.

## 1. Introduction and main results

Let μ\mu and ν\nu be two probability measures on ℝd\mathbb{R}^{d} with finite second moments. The optimal transport problem with quadratic cost is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (OT) |  | 𝒯2​(μ,ν)=infπ∈Π​(μ,ν)∫|x−y|2​π​(d​x,d​y),\mathcal{T}\_{2}(\mu,\nu)=\inf\_{\pi\in\Pi(\mu,\nu)}\int|x-y|^{2}\,\pi(\mathrm{d}x,\mathrm{d}y), |  |

where Π​(μ,ν)\Pi(\mu,\nu) denotes the set of couplings between μ\mu and ν\nu, i.e.,

|  |  |  |
| --- | --- | --- |
|  | π∈Π(μ,ν)⇔π(A×ℝd)=μ(A)andπ(ℝd×A)=ν(A)∀A⊆ℝd Borel;\pi\in\Pi(\mu,\nu)\iff\pi(A\times\mathbb{R}^{d})=\mu(A)\penalty 10000\ \text{and}\penalty 10000\ \pi(\mathbb{R}^{d}\times A)=\nu(A)\quad\forall A\subseteq\mathbb{R}^{d}\text{ Borel;} |  |

see [[Vil21](https://arxiv.org/html/2511.21287v1#bib.bibx31), [San15](https://arxiv.org/html/2511.21287v1#bib.bibx24)] for an overview.
In the seminal work [[BB00](https://arxiv.org/html/2511.21287v1#bib.bibx3)] it is shown that solving 𝒯2​(μ,ν)\mathcal{T}\_{2}(\mu,\nu) is equivalent to minimizing the total energy along absolutely continuous curves (μt)t∈[0,1](\mu\_{t})\_{t\in[0,1]} from μ\mu to ν\nu; to be precise,

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | 𝒯2​(μ,ν)=inf(μt,vt)∫01∫ℝd|vt|2​dμt​dt,\mathcal{T}\_{2}(\mu,\nu)=\inf\_{(\mu\_{t},v\_{t})}\int\_{0}^{1}\int\_{\mathbb{R}^{d}}\left|v\_{t}\right|^{2}\mathrm{d}\mu\_{t}\mathrm{d}t, |  |

where the infimum is taken over all (μt,vt)(\mu\_{t},v\_{t}) such that μ0=μ,μ1=ν\mu\_{0}=\mu,\mu\_{1}=\nu, and (μt,vt)(\mu\_{t},v\_{t}) solves

|  |  |  |
| --- | --- | --- |
|  | ∂tμt+div​(vt​μt)=0\partial\_{t}\mu\_{t}+\textup{div}\left(v\_{t}\mu\_{t}\right)=0 |  |

in the sense of distributions. Problem ([1](https://arxiv.org/html/2511.21287v1#S1.E1 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) is known as the dynamic formulation of optimal transport, or the Benamou-Brenier formula. It has the probabilistic representation

|  |  |  |  |
| --- | --- | --- | --- |
| (DOT) |  | 𝒯2(μ,ν)=inf{𝔼[∫01|vt|2dt]:dXt=vtdtwhereX0∼μ,X1∼ν}.\displaystyle\mathcal{T}\_{2}(\mu,\nu)=\inf\left\{\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\mathrm{d}t\right]:\,\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t\penalty 10000\ \text{where}\penalty 10000\ X\_{0}\sim\mu,X\_{1}\sim\nu\right\}. |  |

In this note we extend the Benamou-Brenier formula to the so-called barycentric weak optimal transport problem. Introduced in the series of papers [[GRST17](https://arxiv.org/html/2511.21287v1#bib.bibx19), [GRS+18](https://arxiv.org/html/2511.21287v1#bib.bibx18)], this problem is defined as

|  |  |  |  |
| --- | --- | --- | --- |
| (WOT) |  | 𝒯¯2​(μ,ν):=infπ∈Π​(μ,ν)∫|mean​(πx)−x|2​μ​(d​x),\overline{\mathcal{T}}\_{2}(\mu,\nu):=\inf\_{\pi\in\Pi(\mu,\nu)}\int\left|\mathrm{mean}(\pi\_{x})-x\right|^{2}\,\mu(\mathrm{d}x), |  |

where the map (πx)x∈ℝd(\pi\_{x})\_{x\in\mathbb{R}^{d}} is the disintegration of π\pi with respect to μ\mu and
mean​(ρ):=∫y​ρ​(d​y)\mathrm{mean}(\rho):=\int y\,\rho(\mathrm{d}y) for any integrable probability measure ρ\rho. Weak optimal transport covers the settings of martingale optimal transport [[BHLP13](https://arxiv.org/html/2511.21287v1#bib.bibx6), [BJ16](https://arxiv.org/html/2511.21287v1#bib.bibx7)], entropic optimal transport [[Con19](https://arxiv.org/html/2511.21287v1#bib.bibx13), [Nut21](https://arxiv.org/html/2511.21287v1#bib.bibx22)] and semi-martingale optimal transport [[TT14](https://arxiv.org/html/2511.21287v1#bib.bibx30), [GL21](https://arxiv.org/html/2511.21287v1#bib.bibx17), [BCH+24](https://arxiv.org/html/2511.21287v1#bib.bibx4)], among others; see also the related works [[Mar96a](https://arxiv.org/html/2511.21287v1#bib.bibx20), [Mar96b](https://arxiv.org/html/2511.21287v1#bib.bibx21), [Tal95](https://arxiv.org/html/2511.21287v1#bib.bibx28), [Tal96](https://arxiv.org/html/2511.21287v1#bib.bibx29), [FS18](https://arxiv.org/html/2511.21287v1#bib.bibx15), [ABC19](https://arxiv.org/html/2511.21287v1#bib.bibx1), [BG18](https://arxiv.org/html/2511.21287v1#bib.bibx5), [FS18](https://arxiv.org/html/2511.21287v1#bib.bibx15), [Shu20](https://arxiv.org/html/2511.21287v1#bib.bibx26)] It has recently proved to be an extremely versatile tool in OT.
Intuitively, 𝒯¯2​(μ,ν)\overline{\mathcal{T}}\_{2}(\mu,\nu) measures how far μ\mu and ν\nu are away from being the marginals of a one-step martingale. [[GJ20](https://arxiv.org/html/2511.21287v1#bib.bibx16)] show that

|  |  |  |
| --- | --- | --- |
|  | 𝒯¯2​(μ,ν)=infη⪯cν𝒯2​(μ,η),\displaystyle\overline{\mathcal{T}}\_{2}(\mu,\nu)=\inf\_{\eta\preceq\_{c}\nu}\mathcal{T}\_{2}(\mu,\eta), |  |

where ⪯c\preceq\_{c} denotes convex order, i.e. η⪯cν\eta\preceq\_{c}\nu if ∫f​dη≤∫f​dν\int f\mathrm{d}\eta\leq\int f\mathrm{d}\nu for all convex functions f:ℝd→ℝ.f:\mathbb{R}^{d}\to\mathbb{R}.
Our first main result is the following dynamic characterization of
𝒯¯2\overline{\mathcal{T}}\_{2}:

###### Theorem 1.

We have

|  |  |  |
| --- | --- | --- |
|  | 𝒯¯2(μ,ν)=inf{𝔼[∫01|vt|2]:dXt=vtdt+σtdBt,X0∼μ,X1∼ν},\displaystyle\overline{\mathcal{T}}\_{2}(\mu,\nu)=\inf\left\{\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\right]:\,\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t},\penalty 10000\ X\_{0}\sim\mu,X\_{1}\sim\nu\right\}, |  |

where the infimum is taken over predictable processes vv and σ\sigma.

Compared to ([DOT](https://arxiv.org/html/2511.21287v1#S1.Ex4 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")), the dynamic formulation in Theorem [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") allows for a costless martingale transport via the diffusion term σt​d​Bt\sigma\_{t}\mathrm{d}B\_{t}; on the flip side 𝒯¯2​(μ,ν)\overline{\mathcal{T}}\_{2}(\mu,\nu) penalizes only the deviation of x↦mean​(πx)x\mapsto\mathrm{mean}(\pi\_{x}) from the identity.

We note that the dynamic formulation in Theorem [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") is different from the entropic projection problem, also known as the Schrödinger bridge,

|  |  |  |
| --- | --- | --- |
|  | inf{𝔼[∫01|vt|2]dt:dXt=vtdt+dBtwhereX0∼μ,X1∼ν},\displaystyle\inf\left\{\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\right]\,\mathrm{d}t:\,\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t+\mathrm{d}B\_{t}\penalty 10000\ \text{where}\penalty 10000\ X\_{0}\sim\mu,X\_{1}\sim\nu\right\}, |  |

see [[Sch32](https://arxiv.org/html/2511.21287v1#bib.bibx25), [Föl06](https://arxiv.org/html/2511.21287v1#bib.bibx14)],
where the infimum is taken over the drift vv only and σ\sigma is identically equal to the identity matrix. The Schrödinger bridge minimizes the Kullback-Leibler divergence of the law of XX with respect to the Wiener measure, rather than a cost function on the marginals.

As mentioned above, 𝒯¯2​(μ,ν)\overline{\mathcal{T}}\_{2}(\mu,\nu) essentially allows for arbitrary martingale transports, as σ\sigma does not influence the cost 𝔼​[∫01|vt|2​𝑑t]\mathbb{E}[\int\_{0}^{1}\left|v\_{t}\right|^{2}dt]. It is thus natural to extend our analysis to the functional

|  |  |  |
| --- | --- | --- |
|  | 𝒯¯α,β​(μ,ν):=infπ∈Π​(μ,ν)∫α​|mean​(πx)−x|2−β​MCov​(πx,γ1d)​μ​(d​x)\overline{\mathcal{T}}^{\alpha,\beta}(\mu,\nu):=\inf\_{\pi\in\Pi(\mu,\nu)}\int\alpha\left|\mathrm{mean}(\pi\_{x})-x\right|^{2}-\beta\mathrm{MCov}(\pi\_{x},\gamma\_{1}^{d})\,\mu(\mathrm{d}x) |  |

for α,β>0\alpha,\beta>0, see [[BPRS25](https://arxiv.org/html/2511.21287v1#bib.bibx8), Section 1.1.6] . In the above, the maximal covariance

|  |  |  |
| --- | --- | --- |
|  | MCov​(ρ,ϱ):=supπ∈Π​(ρ,ϱ)∫⟨y,z⟩​π​(d​y,d​z),ρ,ϱ∈𝒫2​(ℝd),\displaystyle\mathrm{MCov}(\rho,\varrho):=\sup\_{\pi\in\Pi(\rho,\varrho)}\int\langle y,z\rangle\,\pi(\mathrm{d}y,\mathrm{d}z),\quad\rho,\varrho\in\mathcal{P}\_{2}(\mathbb{R}^{d}), |  |

measures the 22-Wasserstein distance of the disintegration πx\pi\_{x} from the dd-dimensional standard normal distribution γ1d\gamma\_{1}^{d}, up to terms that do not depend on the coupling π\pi.
  
One of the main results of [[BVBHK19](https://arxiv.org/html/2511.21287v1#bib.bibx11)] is the representation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2) |  | supπ∈ΠM​(μ,ν)∫MCov​(πx,γ1d)​μ​(d​x)=sup{𝔼​[∫01Tr​(σt)​dt]:d​Xt=σt​d​Bt,X0∼μ,X1∼ν},\displaystyle\begin{split}&\sup\_{\pi\in\Pi\_{M}(\mu,\nu)}\int\mathrm{MCov}(\pi\_{x},\gamma\_{1}^{d})\,\mu(\mathrm{d}x)\\ &\qquad=\sup\left\{\mathbb{E}\left[\int\_{0}^{1}\mathrm{Tr}\left(\sigma\_{t}\right)\mathrm{d}t\right]:\mathrm{d}X\_{t}=\sigma\_{t}\mathrm{d}B\_{t},\penalty 10000\ X\_{0}\sim\mu,X\_{1}\sim\nu\right\},\end{split} | |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | ΠM​(μ,ν)={π∈Π​(μ,ν):mean​(πx)=x∀x∈ℝd}\displaystyle\Pi\_{M}(\mu,\nu)=\left\{\pi\in\Pi(\mu,\nu):\mathrm{mean}(\pi\_{x})=x\quad\forall x\in\mathbb{R}^{d}\right\} |  |

is the set of martingale measures with marginals μ\mu and ν\nu and we recall that ΠM​(μ,ν)≠∅\Pi\_{M}(\mu,\nu)\neq\emptyset if and only if μ⪯cν\mu\preceq\_{c}\nu; see [[Str65](https://arxiv.org/html/2511.21287v1#bib.bibx27)]. The solution of ([2](https://arxiv.org/html/2511.21287v1#S1.E2 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) is given by a so-called stretched Brownian motion.
Equation ([2](https://arxiv.org/html/2511.21287v1#S1.E2 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) corresponds to 𝒯¯0,1\overline{\mathcal{T}}^{0,1} in our notation above. Our second main result result gives a similar representation of 𝒯¯α,β\overline{\mathcal{T}}^{\alpha,\beta} for the intermediate case α,β>0\alpha,\beta>0.

###### Theorem 2.

For α,β>0\alpha,\beta>0 and μ,ν∈𝒫2​(ℝd)\mu,\nu\in\mathcal{P}\_{2}(\mathbb{R}^{d}) we have

|  |  |  |
| --- | --- | --- |
|  | 𝒯¯α,β​(μ,ν)\displaystyle\overline{\mathcal{T}}^{\alpha,\beta}(\mu,\nu) |  |
|  |  |  |
| --- | --- | --- |
|  | =inf{𝔼[∫01α|vt|2−β(⟨Bt,vt⟩+Tr(σt))dt]:dXt=vtdt+σdBt,X0∼μ,X1∼ν},\displaystyle\quad=\inf\left\{\mathbb{E}\left[\int\_{0}^{1}\alpha\left|v\_{t}\right|^{2}-\beta\left(\langle B\_{t},v\_{t}\rangle+\mathrm{Tr}\left(\sigma\_{t}\right)\right)\mathrm{d}t\right]:\,\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t+\sigma\mathrm{d}B\_{t},\penalty 10000\ X\_{0}\sim\mu,X\_{1}\sim\nu\right\}, |  |

where the infimum is taken over all predictable processes vv and σ.\sigma. The right hand side is attained by the process

|  |  |  |
| --- | --- | --- |
|  | d​Xt=(∇φ​(X0)−X0)​d​t+σt​d​BtwithX0∼μ,\mathrm{d}X\_{t}=(\nabla\varphi(X\_{0})-X\_{0})\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t}\quad\text{with}\quad X\_{0}\sim\mu, |  |

where the 11-Lipschitz map ∇φ\nabla\varphi is given in Proposition [4](https://arxiv.org/html/2511.21287v1#Thmthm4 "Proposition 4 ([GJ20, Theorem 1.2]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") and σ\sigma is given in Proposition [5](https://arxiv.org/html/2511.21287v1#Thmthm5 "Proposition 5 ([BPRS25, Theorem 5.4]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") below.

Note that Theorem [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") can be formally obtained from Theorem [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") by taking α=1,β→0\alpha=1,\beta\to 0; similarly ([2](https://arxiv.org/html/2511.21287v1#S1.E2 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) can be obtained by setting α→∞,β=1\alpha\to\infty,\beta=1. Let us also remark that one can actually restrict the minimization in Theorem [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") to drifts vv that are independent of BB, leading to 𝔼​[⟨Bt,vt⟩]=0\mathbb{E}[\langle B\_{t},v\_{t}\rangle]=0. This follows from the proof of Theorem [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") below. The dynamic formulation in Theorem [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") can also be seen as a version of the semimartingale optimal transport problem.

## 2. Notation

We write 𝒫2​(ℝd)\mathcal{P}\_{2}(\mathbb{R}^{d}) for the set of (Borel) probability measures with finite second moments. We let ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle denote the standard inner product on ℝd\mathbb{R}^{d} and for x∈ℝdx\in\mathbb{R}^{d} we write |x|2=⟨x,x⟩\left|x\right|^{2}=\langle x,x\rangle. For a probability measure μ\mu on ℝd\mathbb{R}^{d} and a function κ:ℝd→𝒫​(ℝd)\kappa:\mathbb{R}^{d}\to\mathcal{P}(\mathbb{R}^{d}) we define (μ⊗κx)​(A×B):=∫Aκx​(B)​μ​(d​x)(\mu\otimes\kappa\_{x})(A\times B):=\int\_{A}\kappa\_{x}(B)\,\mu(\mathrm{d}x) for all Borel sets A,B⊆ℝdA,B\subseteq\mathbb{R}^{d}. Next, we write (πx)x∈ℝd(\pi\_{x})\_{x\in\mathbb{R}^{d}} for the disintegration of π∈Π​(μ,ν)\pi\in\Pi(\mu,\nu) wrt. μ\mu, i.e. x↦πx​(A)x\mapsto\pi\_{x}(A) is Borel measurable for all Borel sets A⊆ℝdA\subseteq\mathbb{R}^{d} and satisfies μ⊗πx=π.\mu\otimes\pi\_{x}=\pi. Lastly we define the push-forward measure of a function f:ℝd→ℝkf:\mathbb{R}^{d}\to\mathbb{R}^{k} under μ\mu as f#​μ​(A):=μ​({x∈ℝd:f​(x)∈A})f\_{\#}\mu(A):=\mu(\{x\in\mathbb{R}^{d}:\,f(x)\in A\}) for all Borel sets A⊆ℝkA\subseteq\mathbb{R}^{k}, k∈ℕ.k\in\mathbb{N}.

We say that a process XX is an admissible diffusion process if there exists a filtered probability space (Ω,ℱ,(ℱt)t∈[0,1],ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\in[0,1]},\mathbb{P}) which supports a standard Brownian motion (Bt)t∈[0,1](B\_{t})\_{t\in[0,1]} with X0⟂⟂(Bt)t∈[0,1]X\_{0}\perp\!\!\!\!\perp(B\_{t})\_{t\in[0,1]} and predictable processes v∈L2​(ℙ⊗d​t;ℝd)v\in L^{2}(\mathbb{P}\otimes\mathrm{d}t;\mathbb{R}^{d}) and σ∈L2​(ℙ⊗d​t;ℝd×d)\sigma\in L^{2}(\mathbb{P}\otimes\mathrm{d}t;\mathbb{R}^{d\times d}) such that

|  |  |  |
| --- | --- | --- |
|  | d​Xt=vt​d​t+σt​d​Bt.\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t}. |  |

For μ,ν∈𝒫2​(ℝd)\mu,\nu\in\mathcal{P}\_{2}(\mathbb{R}^{d}), we denote by 𝒟​(μ,ν)\mathcal{D}(\mu,\nu) the set of all admissible diffusion processes XX with X0∼μX\_{0}\sim\mu and X1∼νX\_{1}\sim\nu. We set γtd:=Law​(Bt)\gamma\_{t}^{d}:=\text{Law}\left(B\_{t}\right).
We also define

|  |  |  |
| --- | --- | --- |
|  | ℬ​ℬα,β​(μ,ν):=infX∈𝒟​(μ,ν)𝔼​[∫01α​|vt|2−β​(⟨Bt,vt⟩+Tr​(σt))​d​t].\mathcal{BB}^{\alpha,\beta}(\mu,\nu):=\inf\_{X\in\mathcal{D}(\mu,\nu)}\mathbb{E}\left[\int\_{0}^{1}\alpha\left|v\_{t}\right|^{2}-\beta\left(\langle B\_{t},v\_{t}\rangle+\mathrm{Tr}\left(\sigma\_{t}\right)\right)\mathrm{d}t\right]. |  |

Using this more compact notation, Theorem [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") reads
𝒯¯2=ℬ​ℬ1,0,\overline{\mathcal{T}}\_{2}=\mathcal{BB}^{1,0},
while Theorem [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") reads
𝒯¯α,β=ℬ​ℬα,β\overline{\mathcal{T}}^{\alpha,\beta}=\mathcal{BB}^{\alpha,\beta}
for α,β>0\alpha,\beta>0.

## 3. Preliminary results

Before we turn to the proofs of Theorems [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") and [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation"), we need to investigate the relation between two results, which were mentioned in the introduction.

###### Proposition 3 ([[BVBHK19](https://arxiv.org/html/2511.21287v1#bib.bibx11), Theorem 2.2.]).

Let μ,ν∈𝒫2​(ℝd)\mu,\nu\in\mathcal{P}\_{2}(\mathbb{R}^{d}) with μ⪯cν\mu\preceq\_{c}\nu. Then
([2](https://arxiv.org/html/2511.21287v1#S1.E2 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) holds and the problem

|  |  |  |
| --- | --- | --- |
|  | sup{𝔼​[∫01Tr​(σt)​dt]:d​Xt=σt​d​Bt,X0∼μ,X1∼ν}.\sup\left\{\mathbb{E}\left[\int\_{0}^{1}\mathrm{Tr}\left(\sigma\_{t}\right)\mathrm{d}t\right]:\mathrm{d}X\_{t}=\sigma\_{t}\mathrm{d}B\_{t},X\_{0}\sim\mu,X\_{1}\sim\nu\right\}. |  |

admits a unique (in law) maximizer M^\widehat{M}.

The authors call the maximizer M^\widehat{M} a *stretched Brownian motion*; M^\widehat{M} is the martingale MM whose trajectories are as close as possible to Brownian motion in the adapted Wasserstein distance, while satisfying the marginal conditions M0∼μM\_{0}\sim\mu and M1∼νM\_{1}\sim\nu (see [[BVBHK19](https://arxiv.org/html/2511.21287v1#bib.bibx11), Section 6]).

In the follow-up paper [[BVBST25](https://arxiv.org/html/2511.21287v1#bib.bibx12)] it is shown that under an irreducibility condition111Two measures μ\mu and ν\nu are irreducible if for any martingale MM with M0∼μM\_{0}\sim\mu and M1∼νM\_{1}\sim\nu we have the implication μ​(A),ν​(B)>0⟹ℙ​(M0∈A,M1∈B)>0\mu(A),\nu(B)>0\implies\mathbb{P}(M\_{0}\in A,M\_{1}\in B)>0 for any A,B⊆ℝdA,B\subseteq\mathbb{R}^{d} Borel. on μ\mu and ν\nu, M^\widehat{M} is a *Bass martingale* between μ\mu and ν\nu. Bass martingales, which go back to [[Bas83](https://arxiv.org/html/2511.21287v1#bib.bibx2)] as a solution to the Skorokhod embedding problem, are martingales MM of the form

|  |  |  |
| --- | --- | --- |
|  | Mt=𝔼​[∇ϕ​(W1)|Wt],M\_{t}=\mathbb{E}\left[\nabla\phi(W\_{1})|W\_{t}\right], |  |

where the Brownian motion WW is started at some W0∼αW\_{0}\sim\alpha, ϕ:ℝd→ℝ\phi:\mathbb{R}^{d}\to\mathbb{R} is a convex function and ∇ϕ​(W1)\nabla\phi(W\_{1}) is square integrable.
Bass’ construction can be viewed as a natural analogue of Brenier’s Theorem [[Bre91](https://arxiv.org/html/2511.21287v1#bib.bibx9)], which states that for regular enough measures μ\mu and ν\nu, the minimizing vector field vtv\_{t} appearing in the dynamic formulation on 𝒯2​(μ,ν)\mathcal{T}\_{2}(\mu,\nu) is of the form vt=∇ϕ−Idv\_{t}=\nabla\phi-\text{Id} for some convex function ϕ\phi.

Next we recall the following result of [[GJ20](https://arxiv.org/html/2511.21287v1#bib.bibx16)], which was later refined in [[BPRS25](https://arxiv.org/html/2511.21287v1#bib.bibx8)] and [[BVBST25](https://arxiv.org/html/2511.21287v1#bib.bibx12)].

###### Proposition 4 ([[GJ20](https://arxiv.org/html/2511.21287v1#bib.bibx16), Theorem 1.2]).

There exists a unique μ¯⪯cν\bar{\mu}\preceq\_{c}\nu such

|  |  |  |
| --- | --- | --- |
|  | 𝒯¯2​(μ,ν)=𝒯2​(μ,μ¯)=infη⪯cν𝒯2​(μ,η).\overline{\mathcal{T}}\_{2}(\mu,\nu)=\mathcal{T}\_{2}(\mu,\bar{\mu})=\inf\_{\eta\preceq\_{c}\nu}\mathcal{T}\_{2}(\mu,\eta). |  |

In particular, μ¯\bar{\mu} is given by

|  |  |  |
| --- | --- | --- |
|  | μ¯=∇φ#​μ\bar{\mu}=\nabla\varphi\_{\#}\mu |  |

where φ:ℝd→ℝ\varphi:\mathbb{R}^{d}\to\mathbb{R} is a convex C1​(ℝd)C^{1}(\mathbb{R}^{d})-function and ∇φ\nabla\varphi is 11-Lipschitz. Furthermore, the optimizers of 𝒯¯2​(μ,ν)\overline{\mathcal{T}}\_{2}(\mu,\nu) and 𝒯2​(μ,μ¯)\mathcal{T}\_{2}(\mu,\bar{\mu}) are connected via the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | π∈Π​(μ,ν) is optimal for 𝒯¯2​(μ,ν)⇔πx=κ∇φ​(x)​ μ-a.e for some ​κ∈ΠM​(∇φ#​μ,ν),\displaystyle\begin{split}\pi\in\Pi(\mu,\nu)&\text{ is optimal for $\overline{\mathcal{T}}\_{2}(\mu,\nu)$}\\ &\iff\pi\_{x}=\kappa\_{\nabla\varphi(x)}\text{ $\mu$-a.e for some }\kappa\in\Pi\_{M}(\nabla\varphi\_{\#}\mu,\nu),\end{split} | |  |

where ΠM\Pi\_{M} was defined in ([3](https://arxiv.org/html/2511.21287v1#S1.E3 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")).

We can now make a connection between Propositions [3](https://arxiv.org/html/2511.21287v1#Thmthm3 "Proposition 3 ([BVBHK19, Theorem 2.2.]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") and [4](https://arxiv.org/html/2511.21287v1#Thmthm4 "Proposition 4 ([GJ20, Theorem 1.2]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation"): indeed, an admissible choice in Proposition [4](https://arxiv.org/html/2511.21287v1#Thmthm4 "Proposition 4 ([GJ20, Theorem 1.2]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") is κ=Law​(M0^,M^1)\kappa=\text{Law}(\widehat{M\_{0}},\widehat{M}\_{1}) where M^\widehat{M} is a stretched Brownian motion between ∇φ#​μ\nabla\varphi\_{\#}\mu and ν\nu from Proposition [3](https://arxiv.org/html/2511.21287v1#Thmthm3 "Proposition 3 ([BVBHK19, Theorem 2.2.]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation"). In fact, the following holds:

###### Proposition 5 ([[BPRS25](https://arxiv.org/html/2511.21287v1#bib.bibx8), Theorem 5.4]).

Let φ:ℝd→ℝ\varphi:\mathbb{R}^{d}\to\mathbb{R} be as in Proposition [4](https://arxiv.org/html/2511.21287v1#Thmthm4 "Proposition 4 ([GJ20, Theorem 1.2]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") and let κ=Law​(M^0,M^1)\kappa=\text{Law}(\widehat{M}\_{0},\widehat{M}\_{1}), where M^\widehat{M} is a stretched Brownian motion between ∇φ#​μ\nabla\varphi\_{\#}\mu and ν\nu. Then the coupling π=μ⊗κ∇φ​(x)∈Π​(μ,ν)\pi=\mu\otimes\kappa\_{\nabla\varphi(x)}\in\Pi(\mu,\nu) is optimal for 𝒯¯α,β​(μ,ν)\overline{\mathcal{T}}^{\alpha,\beta}(\mu,\nu), for all α,β>0\alpha,\beta>0.

## 4. Proofs

We start with the following lemma.

###### Lemma 6.

We have

|  |  |  |
| --- | --- | --- |
|  | ℬ​ℬ1,0​(μ,ν)=infη⪯cν𝒯2​(μ,η).\mathcal{BB}^{1,0}(\mu,\nu)=\inf\_{\eta\preceq\_{c}\nu}\mathcal{T}\_{2}(\mu,\eta). |  |

###### Proof.

We begin by proving the inequality 𝒯2​(μ,η)≥ℬ​ℬ1,0​(μ,ν)\mathcal{T}\_{2}(\mu,\eta)\geq\mathcal{BB}^{1,0}(\mu,\nu) for any η⪯cν\eta\preceq\_{c}\nu. Take any vector field v∈L2​(ℙ⊗d​t;ℝd)v\in L^{2}(\mathbb{P}\otimes\mathrm{d}t;\mathbb{R}^{d}) that pushes μ\mu onto η\eta, i.e.

|  |  |  |
| --- | --- | --- |
|  | d​Xt=vt​d​twithX0∼μ,X1∼η.\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t\quad\text{with}\quad X\_{0}\sim\mu,X\_{1}\sim\eta. |  |

Since η⪯cν\eta\preceq\_{c}\nu, by the martingale representation theorem there exists σ∈L2(ℙ⊗dt;ℝd×d),M0⟂⟂(Bt)t∈[0,1]\sigma\in L^{2}(\mathbb{P}\otimes\mathrm{d}t;\mathbb{R}^{d\times d}),M\_{0}\perp\!\!\!\!\perp(B\_{t})\_{t\in[0,1]} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | d​Mt=σt​d​BtwithM0∼η,M1∼ν.\displaystyle\mathrm{d}M\_{t}=\sigma\_{t}\mathrm{d}B\_{t}\quad\text{with}\quad M\_{0}\sim\eta,M\_{1}\sim\nu. |  |

For any ε∈(0,1)\varepsilon\in(0,1) define the process XεX^{\varepsilon} via

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | d​Xtε=vt1−ε1−ε​1{0≤t≤1−ε}​d​t+σt+ε−1εε​1{1−ε<t≤1}​d​BtwithX0ε=X0.\displaystyle\mathrm{d}X\_{t}^{\varepsilon}=\frac{v\_{\frac{t}{1-\varepsilon}}}{1-\varepsilon}\textbf{1}\_{\left\{0\leq t\leq 1-\varepsilon\right\}}\mathrm{d}t+\frac{\sigma\_{\frac{t+\varepsilon-1}{\varepsilon}}}{\sqrt{\varepsilon}}\textbf{1}\_{\left\{1-\varepsilon<t\leq 1\right\}}\mathrm{d}B\_{t}\quad\text{with}\quad X\_{0}^{\varepsilon}=X\_{0}. |  |

Then XεX^{\varepsilon} is an element of 𝒟​(μ,ν)\mathcal{D}(\mu,\nu) and we have

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | ℬ​ℬ1,0​(μ,ν)≤1(1−ε)2​𝔼​[∫01|vt1−ε|2​1{0≤t≤1−ε}​dt]=11−ε​𝔼​[∫01|vt|2​dt].\displaystyle\mathcal{BB}^{1,0}(\mu,\nu)\leq\frac{1}{(1-\varepsilon)^{2}}\mathbb{E}\left[\int\_{0}^{1}\big|v\_{\frac{t}{1-\varepsilon}}\big|^{2}\textbf{1}\_{\left\{0\leq t\leq 1-\varepsilon\right\}}\mathrm{d}t\right]=\frac{1}{1-\varepsilon}\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\mathrm{d}t\right]. |  |

Minimizing over all such vector fields vv, appealing to the Benamou-Brenier formula ([DOT](https://arxiv.org/html/2511.21287v1#S1.Ex4 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")), and taking ε↓0\varepsilon\downarrow 0, we get the desired inequality ℬ​ℬ1,0​(μ,ν)≤𝒯2​(μ,η)\mathcal{BB}^{1,0}(\mu,\nu)\leq\mathcal{T}\_{2}(\mu,\eta).

We now turn to proving the inequality infη⪯cν𝒯2​(μ,ν)≤ℬ​ℬ1,0​(μ,ν)\inf\_{\eta\preceq\_{c}\nu}\mathcal{T}\_{2}(\mu,\nu)\leq\mathcal{BB}^{1,0}(\mu,\nu). Suppose that X∈𝒟​(μ,ν)X\in\mathcal{D}(\mu,\nu), i.e.

|  |  |  |
| --- | --- | --- |
|  | d​Xt=vt​d​t+σt​d​BtwithX0∼μ,X1∼ν.\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t}\quad\text{with}\quad X\_{0}\sim\mu,X\_{1}\sim\nu. |  |

Let YY be given by

|  |  |  |
| --- | --- | --- |
|  | d​Yt=𝔼​[vt|X0]​d​twithY0=X0\mathrm{d}Y\_{t}=\mathbb{E}[v\_{t}|X\_{0}]\penalty 10000\ \mathrm{d}t\quad\text{with}\quad Y\_{0}=X\_{0} |  |

and set μ^:=Law​(Y1)\widehat{\mu}:=\text{Law}\left(Y\_{1}\right). Then μ^⪯cν\widehat{\mu}\preceq\_{c}\nu as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y1\displaystyle Y\_{1} | =X0+∫01𝔼​[vt|X0]​dt=𝔼​[X0+∫01vt​dt|X0]\displaystyle=X\_{0}+\int\_{0}^{1}\mathbb{E}[v\_{t}|X\_{0}]\mathrm{d}t=\mathbb{E}\left[X\_{0}+\int\_{0}^{1}v\_{t}\mathrm{d}t\bigg|X\_{0}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[X0+∫01vt​dt+∫01σt​dBt|X0]=𝔼​[X1|X0].\displaystyle=\mathbb{E}\left[X\_{0}+\int\_{0}^{1}v\_{t}\mathrm{d}t+\int\_{0}^{1}\sigma\_{t}\mathrm{d}B\_{t}\penalty 10000\ \bigg|X\_{0}\right]=\mathbb{E}[X\_{1}|X\_{0}]. |  |

Thus, ([DOT](https://arxiv.org/html/2511.21287v1#S1.Ex4 "In 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")), Jensen’s inequality and Tonelli’s theorem yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | infη⪯cν𝒯2​(μ,η)≤𝒯2​(μ,μ^)\displaystyle\inf\_{\eta\preceq\_{c}\nu}\mathcal{T}\_{2}(\mu,\eta)\leq\mathcal{T}\_{2}(\mu,\widehat{\mu}) | ≤𝔼[∫01|𝔼[vt|X0]|2dt]\displaystyle\leq\mathbb{E}\left[\int\_{0}^{1}\left|\mathbb{E}[v\_{t}|X\_{0}]\right|^{2}\mathrm{d}t\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[∫01𝔼​[|vt|2|X0]​dt]=𝔼​[∫01|vt|2​dt].\displaystyle\leq\mathbb{E}\left[\int\_{0}^{1}\mathbb{E}[\left|v\_{t}\right|^{2}|X\_{0}]\mathrm{d}t\right]=\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\mathrm{d}t\right]. |  |

As X∈𝒟​(μ,ν)X\in\mathcal{D}(\mu,\nu) was arbitrary, this concludes the proof.
∎

We now give the proof of Theorem [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation").

###### Proof of Theorem [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation").

We first show 𝒯¯2​(μ,ν)≤ℬ​ℬ1,0​(μ,ν)\overline{\mathcal{T}}\_{2}(\mu,\nu)\leq\mathcal{BB}^{1,0}(\mu,\nu).
Take a process X∈𝒟​(μ,ν)X\in\mathcal{D}(\mu,\nu), i.e.

|  |  |  |
| --- | --- | --- |
|  | d​Xt=vt​d​t+σt​d​BtwithX0∼μ,X1∼ν.\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t}\quad\text{with}\quad X\_{0}\sim\mu,X\_{1}\sim\nu. |  |

By definition, Law​(X0,X1)∈Π​(μ,ν)\text{Law}(X\_{0},X\_{1})\in\Pi(\mu,\nu). Applying Jensen’s inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝒯¯2(μ,ν)≤𝔼[|𝔼[X1|X0]−X0|2]=𝔼[|𝔼[∫01vtdt|X0]|2]≤𝔼[∫01|vt|2dt].\overline{\mathcal{T}}\_{2}(\mu,\nu)\leq\mathbb{E}\big[\left|\mathbb{E}[X\_{1}|X\_{0}]-X\_{0}\right|^{2}\big]=\mathbb{E}\left[\left|\mathbb{E}\left[\int\_{0}^{1}v\_{t}\mathrm{d}t\bigg|X\_{0}\right]\right|^{2}\right]\leq\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\mathrm{d}t\right]. |  |

Minimizing over XX yields the inequality 𝒯¯2​(μ,ν)≤ℬ​ℬ1,0​(μ,ν)\overline{\mathcal{T}}\_{2}(\mu,\nu)\leq\mathcal{BB}^{1,0}(\mu,\nu).

For the opposite inequality, let (X0,Y)∼π∈Π​(μ,ν)(X\_{0},Y)\sim\pi\in\Pi(\mu,\nu). We set vt:=𝔼​[Y|X0]−X0v\_{t}:=\mathbb{E}[Y|X\_{0}]-X\_{0} and let XX solve d​Xt=vt​d​t\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t. Note that here vtv\_{t} only depends on X0X\_{0} and is constant in tt. Then

|  |  |  |
| --- | --- | --- |
|  | η:=Law​(X1)=Law​(𝔼​[Y|X0])⪯cLaw​(Y)=ν.\eta:=\text{Law}(X\_{1})=\text{Law}(\mathbb{E}[Y|X\_{0}])\preceq\_{c}\text{Law}(Y)=\nu. |  |

We now define ([4](https://arxiv.org/html/2511.21287v1#S4.E4 "In Lemma 6. ‣ 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) and ([5](https://arxiv.org/html/2511.21287v1#S4.E5 "In Lemma 6. ‣ 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) as in the proof of Lemma [6](https://arxiv.org/html/2511.21287v1#Thmthm6 "Lemma 6. ‣ 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") above to obtain

|  |  |  |
| --- | --- | --- |
|  | ℬℬ1,0(μ,ν)≤𝔼[∫01|vt|2dt]=𝔼[|𝔼[Y|X0]−X0|2]\mathcal{BB}^{1,0}(\mu,\nu)\leq\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\mathrm{d}t\right]=\mathbb{E}\left[\left|\mathbb{E}[Y|X\_{0}]-X\_{0}\right|^{2}\right] |  |

as in ([6](https://arxiv.org/html/2511.21287v1#S4.E6 "In Lemma 6. ‣ 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")).
Minimizing over (X0,Y)∼π∈Π​(μ,ν)(X\_{0},Y)\sim\pi\in\Pi(\mu,\nu) concludes the proof.
∎

Combining Lemma [6](https://arxiv.org/html/2511.21287v1#Thmthm6 "Lemma 6. ‣ 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") and the proof of Theorem [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") actually gives an independent proof of Proposition [4](https://arxiv.org/html/2511.21287v1#Thmthm4 "Proposition 4 ([GJ20, Theorem 1.2]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation").

###### Corollary 7.

We have

|  |  |  |
| --- | --- | --- |
|  | 𝒯¯2​(μ,ν)=ℬ​ℬ1,0​(μ,ν)=infη⪯cν𝒯2​(μ,η).\displaystyle\overline{\mathcal{T}}\_{2}(\mu,\nu)=\mathcal{BB}^{1,0}(\mu,\nu)=\inf\_{\eta\preceq\_{c}\nu}\mathcal{T}\_{2}(\mu,\eta). |  |

We now turn to the proof of Theorem [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation").

###### Proof of Theorem [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation").

Suppose that X∈𝒟​(μ,ν)X\in\mathcal{D}(\mu,\nu), i.e.

|  |  |  |
| --- | --- | --- |
|  | d​Xt=vt​d​t+σt​d​BtwithX0∼μ,X1∼ν,\mathrm{d}X\_{t}=v\_{t}\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t}\quad\text{with}\quad X\_{0}\sim\mu,X\_{1}\sim\nu, |  |

and define π:=Law​(X0,X1)∈Π​(μ,ν)\pi:=\text{Law}\left(X\_{0},X\_{1}\right)\in\Pi(\mu,\nu). Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (7) |  | ∫|mean​(πx)−x|2​μ​(d​x)=𝔼[|𝔼[X1|X0]−X0|2]=𝔼[|𝔼[∫01vtdt+∫01σtdBt|X0]|2]=𝔼[|𝔼[∫01vtdt|X0]|2]≤𝔼[∫01|vt|2dt],\displaystyle\begin{split}\int\left|\mathrm{mean}(\pi\_{x})-x\right|^{2}\,\mu(\mathrm{d}x)&=\mathbb{E}\left[\left|\mathbb{E}\left[X\_{1}|X\_{0}\right]-X\_{0}\right|^{2}\right]\\ &=\mathbb{E}\left[\left|\mathbb{E}\left[\int\_{0}^{1}v\_{t}\mathrm{d}t+\int\_{0}^{1}\sigma\_{t}\mathrm{d}B\_{t}\bigg|X\_{0}\right]\right|^{2}\right]\\ &=\mathbb{E}\left[\left|\mathbb{E}\left[\int\_{0}^{1}v\_{t}\mathrm{d}t\bigg|X\_{0}\right]\right|^{2}\right]\leq\mathbb{E}\left[\int\_{0}^{1}\left|v\_{t}\right|^{2}\mathrm{d}t\right],\end{split} | |  |

where the last inequality follows by two applications of Jensen’s inequality. Similarly, recalling that X0⟂⟂(Bt)t∈[0,1]X\_{0}\perp\!\!\!\!\perp(B\_{t})\_{t\in[0,1]} and taking the possibly sub-optimal candidate ϱx:=Law​(X1,B1|X0=x)∈Π​(πx,γ1d)\varrho\_{x}:=\text{Law}\left(X\_{1},B\_{1}|X\_{0}=x\right)\in\Pi(\pi\_{x},\gamma\_{1}^{d}) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (8) |  | ∫ℝdMCov​(πx,γ1d)​μ​(d​x)≥𝔼​[𝔼​[⟨X1,B1⟩|X0]]=𝔼​[⟨X1,B1⟩]=𝔼​[∫01⟨vt,Bt⟩+Tr​(σt)​d​t].\displaystyle\begin{split}\int\_{\mathbb{R}^{d}}\mathrm{MCov}(\pi\_{x},\gamma\_{1}^{d})\mu(\mathrm{d}x)&\geq\mathbb{E}\left[\mathbb{E}[\langle X\_{1},B\_{1}\rangle|X\_{0}]\right]\\ &=\mathbb{E}\left[\langle X\_{1},B\_{1}\rangle\right]=\mathbb{E}\left[\int\_{0}^{1}\langle v\_{t},B\_{t}\rangle+\mathrm{Tr}\left(\sigma\_{t}\right)\mathrm{d}t\right].\end{split} | |  |

Combining ([7](https://arxiv.org/html/2511.21287v1#S4.E7 "In 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) and ([8](https://arxiv.org/html/2511.21287v1#S4.E8 "In 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) we deduce the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝdα​|mean​(πx)−x|−\displaystyle\int\_{\mathbb{R}^{d}}\alpha\left|\mathrm{mean}(\pi\_{x})-x\right|- | β​MCov​(πx,γ1d)​μ​(d​x)\displaystyle\beta\mathrm{MCov}(\pi\_{x},\gamma\_{1}^{d})\mu(\mathrm{d}x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[∫01α​|vt|2−β​(⟨vt,Bt⟩+Tr​(σt))​d​t],\displaystyle\leq\mathbb{E}\left[\int\_{0}^{1}\alpha\left|v\_{t}\right|^{2}-\beta\left(\langle v\_{t},B\_{t}\rangle+\mathrm{Tr}\left(\sigma\_{t}\right)\right)\mathrm{d}t\right], |  |

showing 𝒯¯α,β​(μ,ν)≤ℬ​ℬα,β​(μ,ν)\overline{\mathcal{T}}^{\alpha,\beta}(\mu,\nu)\leq\mathcal{BB}^{\alpha,\beta}(\mu,\nu).

For the inequality 𝒯¯α,β​(μ,ν)≥ℬ​ℬα,β​(μ,ν)\overline{\mathcal{T}}^{\alpha,\beta}(\mu,\nu)\geq\mathcal{BB}^{\alpha,\beta}(\mu,\nu), let κ\kappa and ∇φ\nabla\varphi be as in Proposition [3](https://arxiv.org/html/2511.21287v1#Thmthm3 "Proposition 3 ([BVBHK19, Theorem 2.2.]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") and [4](https://arxiv.org/html/2511.21287v1#Thmthm4 "Proposition 4 ([GJ20, Theorem 1.2]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation"), i.e. κ=Law​(M^0,M^1)\kappa=\text{Law}(\widehat{M}\_{0},\widehat{M}\_{1}) where M^\widehat{M} denotes the stretched Brownian motion from ∇φ#​μ\nabla\varphi\_{\#}\mu to ν\nu. Let us take X0∼μX\_{0}\sim\mu and apply the martingale representation theorem to write

|  |  |  |
| --- | --- | --- |
|  | M^t=∇φ​(X0)+∫0tσs​dBs\widehat{M}\_{t}=\nabla\varphi(X\_{0})+\int\_{0}^{t}\sigma\_{s}\mathrm{d}B\_{s} |  |

for some σ∈L2​(ℙ⊗d​t;ℝd×d)\sigma\in L^{2}(\mathbb{P}\otimes\mathrm{d}t;\mathbb{R}^{d\times d}) and X0⟂⟂(Bt)t∈[0,1]X\_{0}\perp\!\!\!\!\perp(B\_{t})\_{t\in[0,1]}.
Next, we set vt=∇φ​(X0)−X0v\_{t}=\nabla\varphi(X\_{0})-X\_{0} and define the process XX via

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt\displaystyle\mathrm{d}X\_{t} | =vt​d​t+σt​d​Bt.\displaystyle=v\_{t}\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t}. |  |

By definition, π:=Law​(X0,X1)\pi:=\text{Law}\left(X\_{0},X\_{1}\right) is an element of Π​(μ,ν)\Pi(\mu,\nu) and πx=κ∇φ​(x)\pi\_{x}=\kappa\_{\nabla\varphi(x)}. By Proposition [5](https://arxiv.org/html/2511.21287v1#Thmthm5 "Proposition 5 ([BPRS25, Theorem 5.4]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") we conclude that π\pi is the minimizer of 𝒯¯α,β​(μ,ν)\overline{\mathcal{T}}^{\alpha,\beta}(\mu,\nu). Furthermore,

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | 𝔼​[∫01|vt|2​dt]=𝔼​[|∇φ​(X0)−X0|2]=∫|mean​(κ∇φ​(x))−x|2​μ​(d​x).\displaystyle\mathbb{E}\left[\int\_{0}^{1}|v\_{t}|^{2}\mathrm{d}t\right]=\mathbb{E}\left[\left|\nabla\varphi(X\_{0})-X\_{0}\right|^{2}\right]=\int\left|\mathrm{mean}(\kappa\_{\nabla\varphi(x)})-x\right|^{2}\,\mu(\mathrm{d}x). |  |

Next we observe that by Proposition [3](https://arxiv.org/html/2511.21287v1#Thmthm3 "Proposition 3 ([BVBHK19, Theorem 2.2.]). ‣ 3. Preliminary results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation"),

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | ∫MCov​(κ∇φ​(x),γ1d)​μ​(d​x)=∫MCov​(πx,γ1d)​μ​(d​x)=𝔼​[∫01Tr​(σt)​dt].\displaystyle\int\mathrm{MCov}(\kappa\_{\nabla\varphi(x)},\gamma\_{1}^{d})\,\mu(\mathrm{d}x)=\int\mathrm{MCov}(\pi\_{x},\gamma\_{1}^{d})\,\mu(\mathrm{d}x)=\mathbb{E}\left[\int\_{0}^{1}\mathrm{Tr}\left(\sigma\_{t}\right)\mathrm{d}t\right]. |  |

Lastly, by Fubini’s theorem and X0⟂⟂(Bt)t∈[0,1]X\_{0}\perp\!\!\!\!\perp(B\_{t})\_{t\in[0,1]}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (11) |  | 𝔼​[∫01⟨vt,Bt⟩​dt]=∫01𝔼​[⟨∇φ​(X0)−X0,Bt⟩]​dt=∫01⟨𝔼​[∇φ​(X0)−X0],𝔼​[Bt]⟩​dt=0.\displaystyle\begin{split}\mathbb{E}\left[\int\_{0}^{1}\langle v\_{t},B\_{t}\rangle\mathrm{d}t\right]&=\int\_{0}^{1}\mathbb{E}\left[\langle\nabla\varphi(X\_{0})-X\_{0},B\_{t}\rangle\right]\mathrm{d}t\\ &=\int\_{0}^{1}\langle\mathbb{E}\left[\nabla\varphi(X\_{0})-X\_{0}\right],\mathbb{E}[B\_{t}]\rangle\mathrm{d}t=0.\end{split} | |  |

Combining ([9](https://arxiv.org/html/2511.21287v1#S4.E9 "In 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation"))-([11](https://arxiv.org/html/2511.21287v1#S4.E11 "In 4. Proofs ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation")) and using optimality of π\pi we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯¯α,β​(μ,ν)\displaystyle\overline{\mathcal{T}}^{\alpha,\beta}(\mu,\nu) | =∫ℝdα​|x−mean​(κ∇φ​(x))|−β​MCov​(κ∇φ​(x),γ1d)​μ​(d​x)\displaystyle=\int\_{\mathbb{R}^{d}}\alpha\big|x-\mathrm{mean}(\kappa\_{\nabla\varphi(x)})|-\beta\mathrm{MCov}(\kappa\_{\nabla\varphi(x)},\gamma\_{1}^{d})\,\mu(\mathrm{d}x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫01α​|vt|2−β​(⟨vt,Bt⟩+Tr​(σt))​d​t]≥ℬ​ℬα,β​(μ,ν).\displaystyle=\mathbb{E}\left[\int\_{0}^{1}\alpha\left|v\_{t}\right|^{2}-\beta\left(\langle v\_{t},B\_{t}\rangle+\mathrm{Tr}\left(\sigma\_{t}\right)\right)\mathrm{d}t\right]\geq\mathcal{BB}^{\alpha,\beta}(\mu,\nu). |  |

This concludes the proof.
∎

###### Remark 8.

In Theorems [1](https://arxiv.org/html/2511.21287v1#Thmthm1 "Theorem 1. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation") and [2](https://arxiv.org/html/2511.21287v1#Thmthm2 "Theorem 2. ‣ 1. Introduction and main results ‣ Dynamic characterization of barycentric optimal transport problems and their martingale relaxation"), the quadratic cost function can be generalized to any convex cost function using the same argument, noting that [[BPRS25](https://arxiv.org/html/2511.21287v1#bib.bibx8), Theorem 5.4] also holds for general convex cost functions. This is analogous to the extension of the Benamou-Brenier formula to convex cost functions [[Bre04](https://arxiv.org/html/2511.21287v1#bib.bibx10), [PS25](https://arxiv.org/html/2511.21287v1#bib.bibx23)].

## References

* [ABC19]

  J-J Alibert, Guy Bouchitté, and Thierry Champion, *A new class of costs for optimal transport planning*, European Journal of Applied Mathematics 30 (2019), no. 6, 1229–1263.
* [Bas83]

  Richard F Bass, *Skorokhod imbedding via stochastic integrals*, Séminaire de Probabilités 17 (1983), 221–224.
* [BB00]

  Jean-David Benamou and Yann Brenier, *A computational fluid mechanics solution to the Monge-Kantorovich mass transfer problem*, Numer. Math. (Heidelb.) 84 (2000), no. 3, 375–393.
* [BCH+24]

  Jean-David Benamou, Guillaume Chazareix, Marc Hoffmann, Gregoire Loeper, and François-Xavier Vialard, *Entropic semi-martingale optimal transport*, arXiv preprint arXiv:2408.09361 (2024).
* [BG18]

  Malcolm Bowles and Nassif Ghoussoub, *A theory of transfers: Duality and convolution*, arXiv preprint arXiv:1804.08563 (2018).
* [BHLP13]

  Mathias Beiglböck, Pierre Henry-Labordere, and Friedrich Penkner, *Model-independent bounds for option prices—a mass transport approach*, Finance and Stochastics 17 (2013), no. 3, 477–501.
* [BJ16]

  Mathias Beiglböck and Nicolas Juillet, *On a problem of optimal transport under marginal martingale constraints*.
* [BPRS25]

  Mathias Beiglböck, Gudmund Pammer, Lorenz Riess, and Stefan Schrott, *The fundamental theorem of weak optimal transport*, 2025.
* [Bre91]

  Yann Brenier, *Polar factorization and monotone rearrangement of vector-valued functions*, Communications on pure and applied mathematics 44 (1991), no. 4, 375–417.
* [Bre04]

  by same author, *Extended monge-kantorovich theory*, Optimal Transportation and Applications: Lectures given at the CIME Summer School, held in Martina Franca, Italy, September 2-8, 2001, Springer, 2004, pp. 91–121.
* [BVBHK19]

  Julio Backhoff-Veraguas, Mathias Beiglböck, Martin Huesmann, and Sigrid Källblad, *Martingale benamou–brenier: a probabilistic perspective*, 2019.
* [BVBST25]

  Julio Backhoff-Veraguas, Mathias Beiglböck, Walter Schachermayer, and Bertram Tschiderer, *Existence of bass martingales and the martingale benamou−-brenier problem in ℝd\mathbb{R}^{d}*, 2025.
* [Con19]

  Giovanni Conforti, *A second order equation for schrödinger bridges with applications to the hot gas experiment and entropic transportation cost*, Probability Theory and Related Fields 174 (2019), no. 1, 1–47.
* [Föl06]

  Hans Föllmer, *Random fields and diffusion processes*, École d’Été de Probabilités de Saint-Flour XV–XVII, 1985–87, Springer, 2006, pp. 101–203.
* [FS18]

  Max Fathi and Yan Shu, *Curvature and transport inequalities for markov chains in discrete spaces*.
* [GJ20]

  Nathael Gozlan and Nicolas Juillet, *On a mixture of brenier and strassen theorems*, Proceedings of the London Mathematical Society 120 (2020), no. 3, 434–463.
* [GL21]

  Ivan Guo and Grégoire Loeper, *Path dependent optimal transport and model calibration on exotic derivatives*, The Annals of Applied Probability 31 (2021), no. 3, 1232–1263.
* [GRS+18]

  Nathael Gozlan, Cyril Roberto, Paul-Marie Samson, Yan Shu, and Prasad Tetali, *Characterization of a class of weak transport-entropy inequalities on the line*, Ann. Inst. Henri Poincare Probab. Stat. 54 (2018), no. 3, 1667–1693.
* [GRST17]

  Nathael Gozlan, Cyril Roberto, Paul-Marie Samson, and Prasad Tetali, *Kantorovich duality for general transport costs and applications*, J. Funct. Anal. 273 (2017), no. 11, 3327–3405 (en).
* [Mar96a]

  Katalin Marton, *Bounding d¯\bar{d}-distance by informational divergence: a method to prove measure concentration*, The Annals of Probability 24 (1996), no. 2, 857–866.
* [Mar96b]

  by same author, *A measure concentration inequality for contracting markov chains*, Geometric & Functional Analysis GAFA 6 (1996), no. 3, 556–571.
* [Nut21]

  Marcel Nutz, *Introduction to entropic optimal transport*, Lecture notes, Columbia University (2021).
* [PS25]

  Brendan Pass and Yair Shenfeld, *A dynamical formulation of multi-marginal optimal transport*, arXiv preprint arXiv:2509.22494 (2025).
* [San15]

  Filippo Santambrogio, *Optimal transport for applied mathematicians*.
* [Sch32]

  Erwin Schrödinger, *Sur la théorie relativiste de l’électron et l’interprétation de la mécanique quantique*, Annales de l’institut Henri Poincaré, vol. 2, 1932, pp. 269–310.
* [Shu20]

  Yan Shu, *From hopf–lax formula to optimal weak transfer plan*, SIAM Journal on Mathematical Analysis 52 (2020), no. 3, 3052–3072.
* [Str65]

  Volker Strassen, *The existence of probability measures with given marginals*, The Annals of Mathematical Statistics 36 (1965), no. 2, 423–439.
* [Tal95]

  Michel Talagrand, *Concentration of measure and isoperimetric inequalities in product spaces*, Publications Mathématiques de l’Institut des Hautes Etudes Scientifiques 81 (1995), no. 1, 73–205.
* [Tal96]

  by same author, *New concentration inequalities in product spaces*, Inventiones mathematicae 126 (1996), no. 3, 505–563.
* [TT14]

  Xiaolu Tan and Nizar Touzi, *Optimal transportation under controlled stochastic dynamics*, Annals of Probability 41 (2014), no. 5, 3201–3240.
* [Vil21]

  Cédric Villani, *Topics in optimal transportation*, vol. 58, American Mathematical Soc., 2021.