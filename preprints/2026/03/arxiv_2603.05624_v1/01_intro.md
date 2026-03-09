---
authors:
- Ulrich Horst
- Takashi Sato
doc_id: arxiv:2603.05624v1
family_id: arxiv:2603.05624
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global
  Solutions'
url_abs: http://arxiv.org/abs/2603.05624v1
url_html: https://arxiv.org/html/2603.05624v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ulrich Horst
Department of Mathematics and School of Business and Economics, Humboldt-Universität zu Berlin, Unter den Linden 6, 10099 Berlin, Germany
[horst@math.hu-berlin.de](2603.05624v1/mailto:horst@math.hu-berlin.de)
 and 
Takashi Sato
Department of Mathematics, Humboldt-Universität zu Berlin, Unter den Linden 6, 10099 Berlin, Germany
[sato.takashi@hu-berlin.de](2603.05624v1/mailto:sato.takashi@hu-berlin.de)

###### Abstract.

We establish an existence of equilibrium result for a class of non-Markovian mean-field games with unbounded control space in weak formulation. Our result is based on new existence and stability results for quadratic-growth generalized McKean-Vlasov BSDEs. Unlike earlier approaches, our approach does not require boundedness assumptions on the model parameters or time horizons and allows for running costs that are quadratic in the control variable.

Horst gratefully acknowledges financial support from DFG CRC/TRR 388 “Rough
Analysis, Stochastic Dynamics and Related Fields”- Project ID 516748464. Sato gratefully acknowledges financial support with a scholarship from the German Academic Exchange Service (DAAD). We thank Huilin Zhang for many valuable comments and discussions.

Keywords Mean field games, McKean-Vlasov BSDE, BMO norm, weak formulation

MSC (2020)
91A16, 93E20, 60H20,

## 1. Introduction

Mean field games (MFGs) provide a powerful mathematical framework for analyzing strategic interactions in large populations of agents. Introduced independently by Lasry and Lions [[undefak](#bib.bibx38), [undefal](#bib.bibx39)] and by Huang, Caines, and Malhamé [[undefac](#bib.bibx30), [undefad](#bib.bibx31)], MFGs describe the asymptotic behavior of Nash equilibria in stochastic differential games as the number of players tends to infinity. In this limit, each individual agent has a negligible influence on the overall system but interacts with the population through the empirical distribution of states and/or controls.

Formally, for a given measure-flow μ\mu, a representative agent in an MFG selects an admissible control α\alpha to maximize a cost functional of the form

|  |  |  |
| --- | --- | --- |
|  | J​(α):=𝔼​[∫0Tf​(t,Xt,μt,αt)​𝑑t+g​(XT,μT)]J(\alpha):=\mathbb{E}\left[\int\_{0}^{T}f(t,X\_{t},\mu\_{t},\alpha\_{t})\,dt+g(X\_{T},\mu\_{T})\right] |  |

subject to the state dynamics

|  |  |  |
| --- | --- | --- |
|  | d​Xt=b​(t,Xt,μt,αt)​d​t+σ​(t,Xt,μt,αt)​d​Wt,X0=x0,dX\_{t}=b(t,X\_{t},{\mu}\_{t},\alpha\_{t})\,dt+\sigma(t,X\_{t},{\mu}\_{t},\alpha\_{t})\,dW\_{t},\quad X\_{0}=x\_{0}, |  |

together with the equilibrium condition that μ\mu coincides with the law of the optimally controlled state process.

Several approaches have been developed to solve such problems. In their original formulation [[undefak](#bib.bibx38), [undefal](#bib.bibx39)], Lasry and Lions adopted an analytic perspective and characterized equilibria through a coupled system of nonlinear partial differential equations: a backward Hamilton–Jacobi–Bellman (HJB) equation for the representative agent’s value function and a forward Fokker–Planck (Kolmogorov) equation describing the evolution of the population distribution.

The probabilistic approach to MFG theory was pioneered by Carmona and Delarue in [[undefi](#bib.bibx10)]. Using a Pontryagin-type stochastic maximum principle, they showed that MFG equilibria can be characterized in terms of a McKean–Vlasov forward–backward SDE (MV-FBSDE).

A relaxed solution concept for MFGs was introduced by Lacker in [[undefah](#bib.bibx35)] and later extended to MFGs with common noise by Carmona et al. [[undefk](#bib.bibx12)], and to MFGs with singular controls by Fu and Horst [[undefu](#bib.bibx22)]. In the spirit of traditional game theory the key idea when working with relaxed controls is to first establish upper hemicontinuity of the agent’s best-response correspondence with respect to a given measure-flow, and then to apply a fixed-point argument.

Since their introduction, MFGs have found numerous applications in engineering, finance, economics, and operations research. These range from decentralized control of robotic swarms, communication networks, and automated vehicles [[undef](#bib.bibx1), [undefb](#bib.bibx3), [undefad](#bib.bibx31), [undefac](#bib.bibx30)], to portfolio choice problems under performance concerns [[undefh](#bib.bibx9), [undefv](#bib.bibx23), [undefaj](#bib.bibx37)], to optimal trade execution under market impact [[undeff](#bib.bibx7), [undefg](#bib.bibx8), [undefr](#bib.bibx19), [undefs](#bib.bibx20), [undeft](#bib.bibx21)], as well as to the optimal exploitation of exhaustible resources and models of optimal energy transition [[undefo](#bib.bibx16), [undefp](#bib.bibx17), [undefw](#bib.bibx24), [undefx](#bib.bibx25)].

### 1.1. Our contribution

We consider a class of non-Markovian mean-field games of control in weak formulation with possibly non-compact action sets. The weak formulation, first introduced by Carmona and Lacker [[undefl](#bib.bibx13)] and further developed in [[undefm](#bib.bibx14), [undefai](#bib.bibx36), [undefan](#bib.bibx41), [undefao](#bib.bibx42)], avoids the direct use of MV-FBSDEs. In this setting, the FBSDE system arising in the probabilistic formulation reduces to a generalized McKean–Vlasov BSDE of the form

|  |  |  |  |
| --- | --- | --- | --- |
| (1.1) |  | {d​Xt=σt​(X)​d​Wt,X0=x0,d​Yt=−Ht​(X,Zt,ℒ¯​(X,Zt))​d​t+Zt​d​Wt,YT=G​(X,ℒ¯​(X)),d​ℙ¯d​ℙ=ℰ​(B⋅​(X,Z⋅,ℒ¯​(X))⋅W)T,ℒ¯​(⋅):=ℙ¯∘(⋅)−1.\left\{\begin{split}\mathrm{d}X\_{t}&=\sigma\_{t}(X)\mathrm{d}W\_{t},\quad X\_{0}=x\_{0},\\ \mathrm{d}Y\_{t}&=-H\_{t}(X,Z\_{t},\bar{\mathcal{L}}(X,Z\_{t}))\mathrm{d}t+Z\_{t}\mathrm{d}W\_{t},\quad Y\_{T}=G(X,\bar{\mathcal{L}}(X)),\\ \frac{\mathrm{d}\bar{\mathbb{P}}}{\mathrm{d}\mathbb{P}}&=\mathcal{E}\left(B\_{\cdot}(X,Z\_{\cdot},\bar{\mathcal{L}}(X))\cdot W\right)\_{T},\quad\bar{\mathcal{L}}(\cdot):=\bar{\mathbb{P}}\circ(\cdot)^{-1}.\end{split}\right. |  |

We establish novel existence results for equations of this type under quadratic growth conditions on the driver. While MV-(F)BSDEs with quadratic drivers in a strong formulation have been extensively studied in the literature [[undefe](#bib.bibx6), [undefy](#bib.bibx26), [undefaa](#bib.bibx28), [undefab](#bib.bibx29), [undefaf](#bib.bibx33)], to the best of our knowledge this is the first work to consider generalized MV-BSDEs of the form ([1.1](#S1.E1 "In 1.1. Our contribution ‣ 1. Introduction ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with quadratic drivers.

Our results enable us to prove the existence of equilibria in MFGs with path-dependent and possibly discontinuous (in the state variable) running cost functions that may exhibit quadratic growth in the control variable. Wang and Zhang [[undefaq](#bib.bibx44)] showed that optimal controls, and hence MFG equilibria, may fail to exist in strong formulation when the running cost is path-dependent and discontinuous in the state variable.

Compactness of the control space is frequently assumed in the literature, but this excludes games with purely quadratic running costs. Lacker [[undefai](#bib.bibx36)] is among the few works that relax the compactness assumption on the control space; however, mean-field interaction through the control variable is not permitted in his framework. Our setting is also more flexible than that of Carmona and Lacker [[undefl](#bib.bibx13)], as we do not require the drift BB to be bounded. This allows, for example, for a geometric Brownian motion with an unbounded controlled drift as the state dynamics. These generalizations come at the expense of additional boundedness assumptions on the state variable, as our analysis relies heavily on existence results for quadratic BSDEs.

Our work is strongly inspired by Possamaï and Tangpi [[undefao](#bib.bibx42)]. To our knowledge, they were the first to characterize MFG equilibria in weak formulation via generalized MV-BSDEs of the form ([1.1](#S1.E1 "In 1.1. Our contribution ‣ 1. Introduction ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). They established existence and uniqueness of equilibria, together with non-asymptotic convergence rates for finite-player games, under boundedness assumptions on the action sets and suitable Lipschitz continuity conditions, as well as differentiability assumptions on the model parameters or smallness conditions on the terminal payoff. In contrast, we do not consider finite-player games and instead focus on the existence of equilibria in MFGs with possibly non-compact action sets and quadratic drivers.

Our approach consists in replacing the law arguments in the generalized MV-BSDE with generic parameters and defining a solution mapping that associates these parameters with the laws of the corresponding BSDE solutions. Existence then reduces to proving continuity of this mapping and identifying a compact, convex subset that is mapped into itself. A key novelty of our approach lies in the use of uniform boundedness of the ZZ-components of solutions to quadratic BSDEs in the BMO norm, without requiring smallness conditions on the model parameters or compactness of the control space. This distinguishes our work from existing approaches. In [[undefl](#bib.bibx13)], the solution mapping is set-valued and involves maximized Hamiltonians, and equilibrium existence is obtained via a Measurable Maximum Theorem [[undefa](#bib.bibx2), Theorem 18.19], which typically requires compact action spaces. In [[undefao](#bib.bibx42)], this issue is avoided by fixing a measurable maximizer of the Hamiltonian in advance and incorporating it into their MV-BSDE. Regardless of the specific approach, in both papers compactness of the action space is required to guarantee Lipschitz continuity of BSDE drivers as both papers rely on stability results for BSDEs with Lipschitz drivers. We use stability results for quadratic BSDEs.

Since the ZZ-component of a BSDE solution need not be continuous, compactness in the space of probability measures is difficult to establish directly. To address this difficulty, we lift the solution mapping to the space of integrable Young measures. The use of Young measures in the context of MV-BSDEs was pioneered in [[undefl](#bib.bibx13)]; we extend this methodology to quadratic settings, which raises several technical challenges.111Since the space of all Young measures is too large in our setting, due to the relaxed boundedness assumptions on the mean-field terms, we actually need to work with integrable Young measures. First, continuity of the solution mapping with respect to the stable topology on integrable Young measures must be established. We address this by proving a new stability result for quadratic BSDEs, which is of independent interest as a stability result with respect to the driver. Second, one must identify a compact set of measures that is invariant under the solution mapping. When the model parameters are bounded in the mean-field terms, such a set can be characterized using a uniform BMO bound for solutions of quadratic BSDEs. When the model parameters are unbounded in the mean-field terms, more delicate arguments are required. In this case, uniform BMO bounds are not available to the best of our knowledge. However, by exploiting the equivalence between generalized MV-BSDEs and MV-FBSDEs, and by adapting an a priori estimate due to Hao et al. [[undefy](#bib.bibx26)], we derive an upper bound for the BMO norm of the ZZ-component of any solution to our generalized MV-BSDE, which allows us to establish existence via a truncation argument.

### 1.2. Organization of the paper

The remainder of the paper is organized as follows. Section [2](#S2 "2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") introduces the model, key assumptions, and main results. Rather than stating all assumptions at once, we deliberately develop the theory progressively (as there are many subtleties), which is more transparent, beginning with a general characterization of MFG equilibria in terms of an abstract generalized MV-BSDE. We then specify conditions on the model parameters and admissible control sets under which the BSDE admits a comparison principle. Existence of solutions is established under standard separability conditions on the running cost, and—when model parameters are unbounded—under an additional strong quadratic growth condition on the driver. Section [3](#S3 "3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") proves continuity of the solution mapping in the stable topology. Section [4](#S4 "4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") establishes a compactness result for integrable Young measures and identifies a compact, convex invariant set. Finally, Section [5](#S5 "5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") proves the existence of equilibria in weak formulation within our framework.

### 1.3. Notation.

We set ℕ∗:=ℕ∪{∞}\mathbb{N}^{\ast}:=\mathbb{N}\cup\{\infty\} and write 𝒫​(E)\mathcal{P}(E) for the set of probability measures on a measurable space (E,ℰ)(E,\mathcal{E}). Expectations w.r.t. a measure μ\mu are denoted 𝔼μ\mathbb{E}^{\mu} or simply 𝔼\mathbb{E}. The pp-th moment of μ\mu is denoted Mp​(μ)M\_{p}(\mu), and 𝒫p​(E):={μ∈𝒫​(E):Mp​(μ)<∞}.\mathcal{P}\_{p}(E):=\{\mu\in\mathcal{P}(E):M\_{p}(\mu)<\infty\}. For two measures μ,μ′∈𝒫p​(E)\mu,\mu^{\prime}\in\mathcal{P}\_{p}(E), we denote by 𝒲p​(μ,μ′)\mathcal{W}\_{p}(\mu,\mu^{\prime}) their Wasserstein distance induced by a metric on EE.
Unless otherwise specified, 𝒫p​(E)\mathcal{P}\_{p}(E) is endowed with the 𝒲p\mathcal{W}\_{p}-topology.
𝕃p​(ℝl;ℚ)\mathbb{L}^{p}(\mathbb{R}^{l};\mathbb{Q}) denotes the usual space of ℝl\mathbb{R}^{l}-valued measurable functions with finite LpL^{p}-norm under ℚ\mathbb{Q} and ℍp​(ℝl;ℚ)\mathbb{H}^{p}(\mathbb{R}^{l};\mathbb{Q}) denotes the space of ℝl\mathbb{R}^{l}-valued predictable processes HH on [0,T][0,T] with ‖(∫0T|Hs|2​ds)12‖𝕃p​(ℝ;ℚ)<∞\|(\int\_{0}^{T}\left|H\_{s}\right|^{2}\mathrm{d}s)^{\frac{1}{2}}\|\_{\mathbb{L}^{p}(\mathbb{R};\mathbb{Q})}<\infty.
For progressively measurable processes HH we set ‖H‖SSp​(ℝl;ℚ):=‖supt∈[0,T]|Ht|‖𝕃p​(ℝ;ℙ)\left\|H\right\|\_{\SS^{p}(\mathbb{R}^{l};\mathbb{Q})}:=\|\sup\_{t\in[0,T]}\left|H\_{t}\right|\|\_{\mathbb{L}^{p}(\mathbb{R};\mathbb{P})} and ‖H‖ℍBMO2​(ℝl;ℚ)\left\|H\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{R}^{l};\mathbb{Q})} denotes the usual BMO-norm.
SSp​(ℝl;ℚ)\SS^{p}(\mathbb{R}^{l};\mathbb{Q}) denotes the space of ℝl\mathbb{R}^{l}-valued adapted continuous processes on [0,T][0,T] with finite ∥⋅∥SSp​(ℝl;ℚ)\left\|\cdot\right\|\_{\SS^{p}(\mathbb{R}^{l};\mathbb{Q})}-norm, and ℍBMO2​(ℝl;ℚ)\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{R}^{l};\mathbb{Q}) is the space of ℝl\mathbb{R}^{l}-valued predictable processes on [0,T][0,T] with finite ∥⋅∥ℍBMO2​(ℝl;ℚ)\left\|\cdot\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{R}^{l};\mathbb{Q})}-norm.
When no confusion arises, we write Lp​(ℚ),ℍp​(ℚ),SSp​(ℚ)L^{p}(\mathbb{Q}),\mathbb{H}^{p}(\mathbb{Q}),\SS^{p}(\mathbb{Q}), and ℍBMO2​(ℚ)\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{Q}) for short.

## 2. Setup and main results

Throughout this paper, all randomness is described by a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) that carries a dd-dimensional Brownian WW. We denote by 𝔽={ℱt}\mathbb{F}=\{\mathcal{F}\_{t}\} the natural filtration generated by WW augmented by the ℙ\mathbb{P}-null sets. Stochastic integrals of progressively measurable process HH w.r.t. WW are denoted H⋅WH\cdot W. We fix a time horizon T<∞T<\infty, denote by 𝒞d\mathcal{C}\_{d} the set of ℝd\mathbb{R}^{d}-valued continuous functions on [0,T][0,T] equipped with the supremum norm ∥⋅∥∞\left\|\cdot\right\|\_{\infty}.

### 2.1. Mean-field game in weak formulation

To introduce our non-Markovian MFG in weak formulation, we fix measurable diffusion coefficients222We implicitly assume that the space 𝒞d×ℝd\mathcal{C}\_{d}\times\mathbb{R}^{d} is endowed with the norm ∥(⋅,⋅)∥:=∥⋅∥∞+|⋅|\left\|(\cdot,\cdot)\right\|:=\left\|\cdot\right\|\_{\infty}+\left|\cdot\right|.

|  |  |  |
| --- | --- | --- |
|  | b:[0,T]×𝒞d×𝒫​(𝒞d×A)×A→ℝd,σ:[0,T]×𝒞d→ℝd×d.b:[0,T]\times\mathcal{C}\_{d}\times\mathcal{P}(\mathcal{C}\_{d}\times A)\times A\to\mathbb{R}^{d},\quad\sigma:[0,T]\times\mathcal{C}\_{d}\to\mathbb{R}^{d\times d}. |  |

For x∈𝒞dx\in\mathcal{C}\_{d}, we set [x]t:=(xs)0≤s≤t[x]\_{t}:=(x\_{s})\_{0\leq s\leq t} and assume throughout that

|  |  |  |
| --- | --- | --- |
|  | bt​(x,q,a)=bt​([x]t,q∘πt−1,a),σt​(x)=σt​([x]t),whereπt​(x,a):=([x]t,a).b\_{t}(x,q,a)=b\_{t}({[x]\_{t},q\circ\pi\_{t}^{-1},a),\quad\sigma\_{t}(x)=\sigma\_{t}([x]\_{t}}),\quad\text{where}\quad\pi\_{t}(x,a):=([x]\_{t},a). |  |

For an initial state x0∈ℝx\_{0}\in\mathbb{R}, we consider the ℝd\mathbb{R}^{d}-valued state process XX on [0,T][0,T] with dynamics

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | d​Xt=σt​(X)​d​Wt,X0=x0.\mathrm{d}X\_{t}=\sigma\_{t}(X)\mathrm{d}W\_{t},\quad X\_{0}=x\_{0}. |  |

We assume that the volatility process satisfies the following conditions under which our SDE admits a unique strong solution X∈⋂p<∞SSp​(ℙ)X\in\bigcap\_{p<\infty}\SS^{p}(\mathbb{P}) for any initial state.

###### Assumption 2.1.

The volatility process σ\sigma satisfies the following conditions:

1. (1)

   σ⋅​(0)∈L2​([0,T];ℝd)\sigma\_{\cdot}(0)\in L^{2}([0,T];\mathbb{R}^{d}) and |σt​(x)−σt​(x¯)|≤Kσ​‖x−x¯‖∞\left|\sigma\_{t}(x)-\sigma\_{t}(\bar{x})\right|\leq K\_{\sigma}\left\|x-\bar{x}\right\|\_{\infty}
2. (2)

   the d×dd\times d-diffusion matrix σt​(X)\sigma\_{t}(X) is invertible ℙ\mathbb{P}-almost surely.

In what follows, we denote by ℳ1\mathcal{M}\_{1} the class of Borel measurable measure-flows

|  |  |  |
| --- | --- | --- |
|  | m:[0,T]→𝒫1​(𝒞d×ℝd)with∫0TM1​(mt)​dt<∞.m:[0,T]\to\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})\quad\mbox{with}\quad\int\_{0}^{T}M\_{1}(m\_{t})\mathrm{d}t<\infty. |  |

We frequently write m=(mx,ma)m=(m^{x},m^{a}) to indicate the marginal distributions on the path-space and control set. We fix a (possibly unbounded) set of admissible actions A⊂ℝkA\subset\mathbb{R}^{k} and denote by 𝔄\mathfrak{A} a class of predictable control processes α:[0,T]×Ω→A\alpha:[0,T]\times\Omega\to A that may take values in an unbounded set. The precise definition of admissibility is given below. For now, we only assume that for any m∈ℳ1m\in\mathcal{M}\_{1} and α∈𝔄\alpha\in\mathfrak{A} the measure ℙα,m\mathbb{P}^{\alpha,m} with density

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | d​ℙα,md​ℙ=ℰ​((σ−1​b)⋅​(X,m⋅,α⋅)⋅W)T\frac{\mathrm{d}\mathbb{P}^{\alpha,m}}{\mathrm{d}\mathbb{P}}=\mathcal{E}\left((\sigma^{-1}b)\_{\cdot}\big(X,m\_{\cdot},\alpha\_{\cdot}\big)\cdot W\right)\_{T} |  |

on ℱT\mathcal{F}\_{T} is well defined, where ℰ​(M):=exp⁡{M−12​⟨M⟩}\mathcal{E}(M):=\exp\{M-\frac{1}{2}\langle M\rangle\} denotes the stochastic exponential of a continuous local martingale MM.

###### Remark 2.2.

Under the measure ℙα,m\mathbb{P}^{\alpha,m} the process

|  |  |  |
| --- | --- | --- |
|  | Wtα,m:=Wt−∫0t(σ−1​b)s​(X,ms,αs)​dsW\_{t}^{\alpha,m}:=W\_{t}-\int\_{0}^{t}(\sigma^{-1}b)\_{s}(X,m\_{s},\alpha\_{s})\mathrm{d}s |  |

is a Brownian motion and the state process XX satisfies the SDE

|  |  |  |
| --- | --- | --- |
|  | d​Xt=bt​(X,mt,αt)​d​t+σt​(X)​d​Wtα,m.\mathrm{d}X\_{t}=b\_{t}(X,m\_{t},\alpha\_{t})\mathrm{d}t+\sigma\_{t}(X)\mathrm{d}W\_{t}^{\alpha,m}. |  |

This justifies working with martingale state processes.

To define the objective function, we fix the running and terminal payoff functions

|  |  |  |
| --- | --- | --- |
|  | f:[0,T]×𝒞d×𝒫​(𝒞d×A)×A→ℝ,andg:𝒞d×𝒫​(𝒞d)→ℝ.f:[0,T]\times\mathcal{C}\_{d}\times\mathcal{P}(\mathcal{C}\_{d}\times A)\times A\to\mathbb{R},\quad\mbox{and}\quad g:\mathcal{C}\_{d}\times\mathcal{P}(\mathcal{C}\_{d})\to\mathbb{R}. |  |

Analogously to the diffusion coefficients, we assume that

|  |  |  |
| --- | --- | --- |
|  | ft​(x,q,a)=ft​([x]t,q∘πt−1,a).f\_{t}(x,q,a)=f\_{t}([x]\_{t},q\circ\pi\_{t}^{-1},a). |  |

For any measure-flow m=(mx,ma)∈ℳ1m=(m^{x},m^{a})\in\mathcal{M}\_{1} the representative player chooses a control to maximize the expected payoff

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | JW​(α,m):=𝔼ℙα,m​[∫0Tfs​(X,ms,αs)​ds+g​(X,mTx)],J\_{W}(\alpha,m):=\mathbb{E}^{\mathbb{P}^{\alpha,m}}\left[\int\_{0}^{T}f\_{s}(X,m\_{s},\alpha\_{s})\mathrm{d}s+g(X,m\_{T}^{x})\right], |  |

over the class of admissible controls 𝔄\mathfrak{A}. This implicitly assumes that the payoff function JW​(α,m)J\_{W}(\alpha,m) is well defined. We hence employ the following definition of admissibility.

###### Definition 2.3.

An ℝd\mathbb{R}^{d}-valued, 𝔽\mathbb{F}-predictable control α\alpha is called admissible if the measure change ([2.2](#S2.E2 "In 2.1. Mean-field game in weak formulation ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and the payoff functional ([2.3](#S2.E3 "In 2.1. Mean-field game in weak formulation ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) are well defined for all m∈ℳ1m\in\mathcal{M}\_{1}.

Our goal is to establish the existence of an equilibrium in our mean-field game in weak formulation in the sense of the following definition.

###### Definition 2.4 (Mean-field equilibrium).

Let 𝔄¯⊆𝔄\bar{\mathfrak{A}}\subseteq\mathfrak{A} be a subset of admissible controls. A control α^∈𝔄¯\hat{\alpha}\in\bar{\mathfrak{A}} is a mean-field equilibrium in weak formulation if there exists a measure-flow m^∈ℳ1\hat{m}\in\mathcal{M}\_{1} such that

|  |  |  |
| --- | --- | --- |
|  | JW​(α^,m^)≥JW​(α,m^)for allα∈𝔄¯\displaystyle J\_{W}(\hat{\alpha},\hat{m})\geq J\_{W}(\alpha,\hat{m})\quad\mbox{for all}\quad\alpha\in\bar{\mathfrak{A}} |  |

and the following fixed-point condition holds:

|  |  |  |
| --- | --- | --- |
|  | m^t=ℙα^,m^∘(X,α^t)−1for a.e. ​t∈[0,T].\hat{m}\_{t}=\mathbb{P}^{\hat{\alpha},\hat{m}}\circ(X,\hat{\alpha}\_{t})^{-1}\quad\text{for a.e. }t\in[0,T]. |  |

### 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria

In this section, we derive a characterization of equilibria in weak formulation in terms of a generalized MV-BSDE. This section is strongly inspired by the work of Possamaï and Tangpi [[undefao](#bib.bibx42)]. However, there are important (and sometimes subtle) differences. Since our model parameters may be unbounded or exhibit quadratic growth, the set of admissible controls is different and so is the proof of the well-posedness of the MFG. The verification of the comparison principle is also different as we work with stochastic Lipschitz drivers.

#### 2.2.1. A sufficient maximum principle for MFGs

We first introduce the following abstract result that establishes a link between equilibria in weak formulation and solutions to generalized MV-BSDEs. It can be viewed as a sufficient maximum principle for MFGs in weak formulation.

###### Theorem 2.5.

([[undefao](#bib.bibx42), Proposition 2.8])
Let (t,x,z,m)↦Λt​(x,z,m)(t,x,z,m)\mapsto\Lambda\_{t}(x,z,m) be a measurable maximizer of the (reduced) Hamiltonian

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | ht​(x,z,m,a):=ft​(x,m,a)+(σ−1​b)t​(x,m,a)⋅z.h\_{t}(x,z,m,a):=f\_{t}(x,m,a)+(\sigma^{-1}b)\_{t}(x,m,a)\cdot z. |  |

Let α^∈𝔄¯\hat{\alpha}\in\bar{\mathfrak{A}} be an admissible control, let ℙ^∈𝒫​(Ω)\hat{\mathbb{P}}\in\mathcal{P}(\Omega) be a probability measure that is absolutely continuous w.r.t. ℙ\mathbb{P}, and let

|  |  |  |
| --- | --- | --- |
|  | (X,Y,Z)∈SS2​(ℙ)×SS2​(ℙ)×ℍ2​(ℙ)(X,Y,Z)\in\SS^{2}(\mathbb{P})\times\SS^{2}(\mathbb{P})\times\mathbb{H}^{2}(\mathbb{P}) |  |

be a triple of processes that satisfy the (generalized) MV-BSDE

|  |  |  |  |
| --- | --- | --- | --- |
| (2.5) |  | d​Xt=σt​(X)​d​Wt,X0=x0,d​Yt=−ht​(X,Zt,ℒ^​(X,α^t),α^t)​d​t+Zt​d​Wt,YT=g​(X,ℒ^​(X)),\begin{split}\mathrm{d}X\_{t}&=\sigma\_{t}(X)\mathrm{d}W\_{t},\quad X\_{0}=x\_{0},\\ \mathrm{d}Y\_{t}&=-h\_{t}(X,Z\_{t},\hat{\mathcal{L}}(X,\hat{\alpha}\_{t}),\hat{\alpha}\_{t})\mathrm{d}t+Z\_{t}\mathrm{d}W\_{t},\quad Y\_{T}=g(X,\hat{\mathcal{L}}(X)),\end{split} |  |

where ℒ^​(⋅):=ℙ^∘(⋅)−1\hat{\mathcal{L}}(\cdot):=\hat{\mathbb{P}}\circ(\cdot)^{-1} denotes the law of a random variable under ℙ^\hat{\mathbb{P}}. If ℒ^​(X,α^⋅)∈ℳ1\hat{\mathcal{L}}(X,\hat{\alpha}\_{\cdot})\in\mathcal{M}\_{1} and ℙ^\hat{\mathbb{P}} is absolutely continuous with density

|  |  |  |  |
| --- | --- | --- | --- |
| (2.6) |  | d​ℙ^d​ℙ=ℰ​((σ−1​b)⋅​(X,ℒ^​(X,α^⋅),α^⋅)⋅W)T,\frac{\mathrm{d}\hat{\mathbb{P}}}{\mathrm{d}\mathbb{P}}=\mathcal{E}\left((\sigma^{-1}b)\_{\cdot}\big(X,\hat{\mathcal{L}}(X,\hat{\alpha}\_{\cdot}),\hat{\alpha}\_{\cdot}\big)\cdot W\right)\_{T}, |  |

on ℱT\mathcal{F}\_{T} and if the control α^\hat{\alpha} satisfies the fixed-point condition

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | α^t=Λt​(X,Zt,ℒ^​(X,α^t))\hat{\alpha}\_{t}=\Lambda\_{t}(X,Z\_{t},\hat{\mathcal{L}}(X,\hat{\alpha}\_{t})) |  |

and if the BSDEs with drivers

|  |  |  |
| --- | --- | --- |
|  | Htα​(z):=ht​(X,z,ℒ^​(X,α^t),αt)(α∈𝔄¯)H^{\alpha}\_{t}(z):=h\_{t}(X,z,\hat{\mathcal{L}}(X,\hat{\alpha}\_{t}),\alpha\_{t})\quad(\alpha\in\bar{\mathfrak{A}}) |  |

and terminal condition

|  |  |  |
| --- | --- | --- |
|  | g​(X,ℒ^​(X))g(X,\hat{\mathcal{L}}(X)) |  |

admit unique solutions and satisfy a comparison principle, then α^\hat{\alpha} is an equilibrium with payoff

|  |  |  |
| --- | --- | --- |
|  | Y0=JW​(α^,ℒ^​(X,α^⋅)).Y\_{0}=J\_{W}(\hat{\alpha},\hat{\mathcal{L}}(X,\hat{\alpha}\_{\cdot})). |  |

#### 2.2.2. Comparison

The driver HαH^{\alpha} is Lipschitz continuous in the zz-variable with stochastic Lipschitz constants

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | K⋅:=(σ−1​b)⋅​(X,m^⋅,α⋅).K\_{\cdot}:=(\sigma^{-1}b)\_{\cdot}(X,\hat{m}\_{\cdot},\alpha\_{\cdot}). |  |

Existence and uniqueness of solutions to BSDEs with stochastic Lipschitz constants has been established by Briand and Confortola [[undefc](#bib.bibx4)] under the assumption that K∈ℍBMO2​(ℙ)K\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}).
This motivates the following assumption.

###### Assumption 2.6.

For any measure-flow m∈ℳ1m\in\mathcal{M}\_{1} and any admissible control α∈𝔄\alpha\in\mathfrak{A} we have

|  |  |  |
| --- | --- | --- |
|  | (σ−1​b)⋅​(X,m⋅,α⋅)∈ℍBMO2​(ℙ).(\sigma^{-1}b)\_{\cdot}(X,m\_{\cdot},\alpha\_{\cdot})\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}). |  |

Furthermore,

|  |  |  |
| --- | --- | --- |
|  | g​(X,mTx)+∫0T|fs​(X,ms,αs)|​ds∈𝕃p​(ℙ)for any p∈[1,∞).g(X,m\_{T}^{x})+\int\_{0}^{T}\left|f\_{s}(X,m\_{s},\alpha\_{s})\right|\mathrm{d}s\in\mathbb{L}^{p}(\mathbb{P})\quad\mbox{for any $p\in[1,\infty)$}. |  |

The next result follows from Proposition [A.2](#A1.Thmtheorem2 "Proposition A.2. ‣ Appendix A BSDEs with stochastic Lipschitz drivers ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") along with the energy inequality (Proposition [B.3](#A2.Thmtheorem3 "Proposition B.3 (Energy inequality). ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and our assumptions on gg and ff.

###### Proposition 2.7.

Under the above assumption, for any m∈ℳ1m\in\mathcal{M}\_{1} the BSDEs

|  |  |  |  |
| --- | --- | --- | --- |
| (2.9) |  | Ytα=g​(X,mTx)+∫tThs​(X,Zsα,ms,αs)​ds−∫tTZsα​dWs\begin{split}Y\_{t}^{\alpha}&=g(X,m\_{T}^{x})+\int\_{t}^{T}h\_{s}(X,Z^{\alpha}\_{s},m\_{s},\alpha\_{s})\mathrm{d}s-\int\_{t}^{T}Z\_{s}^{\alpha}\mathrm{d}W\_{s}\end{split} |  |

defined in terms of the admissible controls α∈𝔄\alpha\in\mathfrak{A} admit unique solutions

|  |  |  |
| --- | --- | --- |
|  | (yα,zα)∈⋂p<∞(SSp​(ℙ)×ℍp​(ℙ))(y^{\alpha},z^{\alpha})\in\bigcap\_{p<\infty}(\SS^{p}(\mathbb{P})\times\mathbb{H}^{p}(\mathbb{P})) |  |

and satisfy a comparison principle.

#### 2.2.3. Admissibility

It turns out that Assumption [2.6](#S2.Thmtheorem6 "Assumption 2.6. ‣ 2.2.2. Comparison ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") is satisfied if we impose a suitable growth condition on the model parameters and take 𝔄:=ℍBMO2​(ℙ)\mathfrak{A}:=\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}) as our set of admissible controls.

###### Assumption 2.8.

The functions σ−1​b\sigma^{-1}b, ff, and Λ\Lambda satisfy the following conditions for any (t,a,z,m)∈[0,T]×A×ℝd×𝒫1​(𝒞d×A)(t,a,z,m)\in[0,T]\times A\times\mathbb{R}^{d}\times\mathcal{P}\_{1}(\mathcal{C}\_{d}\times A).

1. (1)

   For any p∈[1,∞)p\in[1,\infty),

   |  |  |  |
   | --- | --- | --- |
   |  | g​(X,δ0)+∫0T|fs​(X,δ0,0)|​ds∈Lp​(ℙ).g(X,\delta\_{0})+\int\_{0}^{T}\left|f\_{s}(X,\delta\_{0},0)\right|\mathrm{d}s\in L^{p}(\mathbb{P}). |  |
2. (2)

   It holds

   |  |  |  |
   | --- | --- | --- |
   |  | (σ−1​b)⋅​(X,δ0,0)∈ℍBMO2​(ℙ),Λ⋅​(X,0,δ0)∈ℍBMO2​(ℙ).\displaystyle(\sigma^{-1}b)\_{\cdot}(X,\delta\_{0},0)\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}),\quad\Lambda\_{\cdot}(X,0,\delta\_{0})\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}). |  |
3. (3)

   There exist constant γ>0\gamma>0 s.t. the following growth conditions hold a.s.

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |g​(X,mx)|\displaystyle\left|g(X,m^{x})\right| | ≤|g​(X,δ0)|+γ​M1​(mx),\displaystyle\leq\left|g(X,\delta\_{0})\right|+\gamma M\_{1}(m^{x}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |(σ−1​b)t​(X,m,a)|\displaystyle\left|(\sigma^{-1}b)\_{t}(X,m,a)\right| | ≤|(σ−1​b)t​(X,δ0,0)|+γ​(|a|+M1​(m)),\displaystyle\leq\left|(\sigma^{-1}b)\_{t}(X,\delta\_{0},0)\right|+\gamma(\left|a\right|+M\_{1}(m)), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |ft​(X,m,a)|\displaystyle\left|f\_{t}(X,m,a)\right| | ≤|ft​(X,δ0,0)|+γ​(|a|2+M1​(m)),\displaystyle\leq\left|f\_{t}(X,\delta\_{0},0)\right|+\gamma(\left|a\right|^{2}+M\_{1}(m)), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |Λt​(X,z,m)|\displaystyle\left|\Lambda\_{t}(X,z,m)\right| | ≤|Λt​(X,0,δ0)|+γ​(1+|z|).\displaystyle\leq\left|\Lambda\_{t}(X,0,\delta\_{0})\right|+\gamma(1+\left|z\right|). |  |

###### Proposition 2.9.

Under Assumption [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the following holds.

1. (i)

   Any control α∈ℍBMO2​(ℙ)\alpha\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}) is admissible.
2. (ii)

   If there exist an 𝔽\mathbb{F}-predictable AA-valued process α^\hat{\alpha} and a solution

   |  |  |  |
   | --- | --- | --- |
   |  | (X,Y,Z,ℙ^)∈SS2​(ℙ)×SS∞​(ℙ)×ℍBMO2​(ℙ)×𝒫​(Ω)(X,Y,Z,\hat{\mathbb{P}})\in\SS^{2}(\mathbb{P})\times\SS^{\infty}(\mathbb{P})\times\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})\times\mathcal{P}(\Omega) |  |

   to the generalized BSDE ([2.5](#S2.E5 "In Theorem 2.5. ‣ 2.2.1. A sufficient maximum principle for MFGs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"))-([2.7](#S2.E7 "In Theorem 2.5. ‣ 2.2.1. A sufficient maximum principle for MFGs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with ℒ^​(X,α^⋅)∈ℳ1\hat{\mathcal{L}}(X,\hat{\alpha}\_{\cdot})\in\mathcal{M}\_{1}, then

   |  |  |  |
   | --- | --- | --- |
   |  | α^∈ℍBMO2​(ℙ),\hat{\alpha}\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}), |  |

   and the BSDEs ([2.9](#S2.E9 "In Proposition 2.7. ‣ 2.2.2. Comparison ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with m⋅=ℒ^​(X,α^⋅)m\_{\cdot}=\hat{\mathcal{L}}(X,\hat{\alpha}\_{\cdot}) admit unique solutions and satisfy a comparison principle. In particular, α^\hat{\alpha} forms a mean-field equilibrium in weak formulation.

Proof.

1. (i)

   Under Assumption [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") the density d​ℙα,md​ℙ\mathrm{d}\mathbb{P}^{\alpha,m}\over\mathrm{d}\mathbb{P} in ([2.2](#S2.E2 "In 2.1. Mean-field game in weak formulation ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is well defined for any α∈ℍBMO2​(ℙ)\alpha\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}). To see that the cost function JW​(α,m)J\_{W}(\alpha,m) in ([2.3](#S2.E3 "In 2.1. Mean-field game in weak formulation ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is well defined, it is enough to verify

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼α,m​[∫0T|fs​(X,δ0,0)|​ds]+𝔼α,m​[∫0T|αs|2​ds]+𝔼α,m​[|g​(X,mT)|]<∞.\mathbb{E}^{\alpha,m}\left[\int\_{0}^{T}\left|f\_{s}(X,\delta\_{0},0)\right|\mathrm{d}s\right]+\mathbb{E}^{\alpha,m}\left[\int\_{0}^{T}\left|\alpha\_{s}\right|^{2}\mathrm{d}s\right]+\mathbb{E}^{\alpha,m}\left[\left|g(X,m\_{T})\right|\right]<\infty. |  |

   Proposition [B.2](#A2.Thmtheorem2 "Proposition B.2. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") implies that α∈ℍBMO2​(ℙα,m)\alpha\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}^{\alpha,m}); hence the second term is integrable.
   The reverse Hölder inequality (Proposition [B.4](#A2.Thmtheorem4 "Proposition B.4. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) yileds q>1q>1 such that 𝔼​[|d​ℙα,md​ℙ|q]<∞\mathbb{E}\left[\left|\frac{\mathrm{d}\mathbb{P}^{\alpha,m}}{\mathrm{d}\mathbb{P}}\right|^{q}\right]<\infty. Thus, by Hölder’s inequality

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼ℙα,m​[∫0T|fs​(X,δ0,0)|​ds]≤𝔼​[|d​ℙα,md​ℙ|q]​𝔼​[(∫0T|fs​(X,δ0,0)|​ds)p]<∞,\mathbb{E}^{\mathbb{P}^{\alpha,m}}\left[\int\_{0}^{T}\left|f\_{s}(X,\delta\_{0},0)\right|\mathrm{d}s\right]\leq~\mathbb{E}\left[\left|\frac{\mathrm{d}\mathbb{P}^{\alpha,m}}{\mathrm{d}\mathbb{P}}\right|^{q}\right]\mathbb{E}\left[\left(\int\_{0}^{T}\left|f\_{s}(X,\delta\_{0},0)\right|\mathrm{d}s\right)^{p}\right]<\infty, |  |

   where p>1p>1 is the conjugate of qq. Similarly, 𝔼ℙα,m​[|g​(X,mT)|]<∞\mathbb{E}^{\mathbb{P}^{\alpha,m}}[\left|g(X,m\_{T})\right|]<\infty.
2. (ii)

   The fact that α^∈ℍBMO2​(ℙ)\hat{\alpha}\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}) follows from Assumption [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") (3).
   Since Assumption [2.6](#S2.Thmtheorem6 "Assumption 2.6. ‣ 2.2.2. Comparison ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") is satisfied under Assumption [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the assertion follow from Proposition [2.7](#S2.Thmtheorem7 "Proposition 2.7. ‣ 2.2.2. Comparison ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"). The equilibrium property follows from Theorem [2.5](#S2.Thmtheorem5 "Theorem 2.5. ‣ 2.2.1. A sufficient maximum principle for MFGs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").

□\Box

In view of the preceding result,
we assume from now on that the set of admissible controls is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔄:=ℍBMO2​(ℙ).\mathfrak{A}:=\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}). |  |

#### 2.2.4. Existence of solutions

We establish the existence of an equilibrium under the usual separability conditions on the drift and running cost function.

###### Assumption 2.10.

The drift bb is independent of the law of the control. That is,

|  |  |  |
| --- | --- | --- |
|  | bt​(x,m,a)=bt​(x,mx,a).b\_{t}(x,m,a)=b\_{t}(x,m^{x},a). |  |

Moreover, the running cost function ff satisfies the separability condition

|  |  |  |
| --- | --- | --- |
|  | ft​(x,m,a)=ft1​(x,mx,a)+ft2​(x,m),f\_{t}(x,m,a)=f\_{t}^{1}(x,m^{x},a)+f\_{t}^{2}(x,m), |  |

for measurable functions f1f^{1} and f2f^{2}.

Under Assumption [2.10](#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the fixed-point condition reduces to the purely functional relation

|  |  |  |  |
| --- | --- | --- | --- |
| (2.10) |  | α^t=Λt​(X,Zt,ℒ^​(X)),\hat{\alpha}\_{t}=\Lambda\_{t}\big(X,Z\_{t},\hat{\mathcal{L}}(X)\big), |  |

that we inserted into the driver of the BSDE ([2.5](#S2.E5 "In Theorem 2.5. ‣ 2.2.1. A sufficient maximum principle for MFGs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). Moreover, the density ([2.6](#S2.E6 "In Theorem 2.5. ‣ 2.2.1. A sufficient maximum principle for MFGs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
| (2.11) |  | d​ℙ^d​ℙ=ℰ​((σ−1​b)⋅​(X,ℒ^​(X),α^⋅)⋅W)T.\frac{\mathrm{d}\hat{\mathbb{P}}}{\mathrm{d}\mathbb{P}}=\mathcal{E}\left((\sigma^{-1}b)\_{\cdot}\big(X,\hat{\mathcal{L}}(X),\hat{\alpha}\_{\cdot}\big)\cdot W\right)\_{T}. |  |

In what follows q=(qx,qz)∈𝒫1​(𝒞d×ℝd)q=(q^{x},q^{z})\in\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}) is a generic variable for the joint law of the process (X,Z)(X,Z) and

|  |  |  |
| --- | --- | --- |
|  | θtq​(x,z):=(x,Λt​(x,qx,z)).\theta\_{t}^{q}(x,z):=\big(x,\Lambda\_{t}(x,q^{x},z)\big). |  |

Finding a MFG equilibrium in weak formulation then reduces to first solving the generalized MV-BSDE

|  |  |  |  |
| --- | --- | --- | --- |
| (2.12) |  | d​Xt=σt​(X)​d​Wt,X0=x0,d​Yt=−Ht​(X,Zt,ℒ¯​(X,Zt))​d​t+Zt​d​Wt,YT=G​(X,ℒ¯​(X)),d​ℙ¯d​ℙ=ℰ​(B⋅​(X,Z⋅,ℒ¯​(X))⋅W)T,ℒ¯​(⋅):=ℙ¯∘(⋅)−1,\begin{split}\mathrm{d}X\_{t}&=\sigma\_{t}(X)\mathrm{d}W\_{t},\quad X\_{0}=x\_{0},\\ \mathrm{d}Y\_{t}&=-H\_{t}(X,Z\_{t},\bar{\mathcal{L}}(X,Z\_{t}))\mathrm{d}t+Z\_{t}\mathrm{d}W\_{t},\quad Y\_{T}=G(X,\bar{\mathcal{L}}(X)),\\ \frac{\mathrm{d}\bar{\mathbb{P}}}{\mathrm{d}\mathbb{P}}&=\mathcal{E}\left(B\_{\cdot}(X,Z\_{\cdot},\bar{\mathcal{L}}(X))\cdot W\right)\_{T},\quad\bar{\mathcal{L}}(\cdot):=\bar{\mathbb{P}}\circ(\cdot)^{-1},\end{split} |  |

with terminal condition G​(x,qx):=g​(x,qx)G(x,q^{x}):=g(x,q^{x}) and driver/maximized Hamiltonian

|  |  |  |
| --- | --- | --- |
|  | Ht​(x,z,q):=Ft​(x,z,q)+z⋅Bt​(x,z,qx)H\_{t}(x,z,q):=F\_{t}(x,z,q)+z\cdot B\_{t}(x,z,q^{x}) |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft​(x,z,q)\displaystyle F\_{t}(x,z,q) | :=ft​(x,q∘(θtq)−1,Λt​(x,z,qx)),\displaystyle:=f\_{t}\big(x,q\circ(\theta\_{t}^{q})^{-1},\Lambda\_{t}(x,z,q^{x})\big), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bt​(x,z,qx)\displaystyle B\_{t}(x,z,q^{x}) | :=(σ−1​b)t​(x,qx,Λt​(x,z,qx)),\displaystyle:=(\sigma^{-1}b)\_{t}\big(x,q^{x},\Lambda\_{t}(x,z,q^{x})\big), |  |

and then verifying the integrability condition

|  |  |  |
| --- | --- | --- |
|  | ℒ¯​(X,α^⋅)∈ℳ1.\bar{\mathcal{L}}(X,\hat{\alpha}\_{\cdot})\in\mathcal{M}\_{1}. |  |

###### Remark 2.11.

Under Assumptions [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and [2.10](#S2.Thmtheorem10 "Assumption 2.10. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") the above integrability condition is guaranteed if ℒ¯​(X,Z⋅)∈ℳ1\bar{\mathcal{L}}(X,Z\_{\cdot})\in\mathcal{M}\_{1}. In fact, since α^t=Λt​(X,Zt,ℒ^​(X))\hat{\alpha}\_{t}=\Lambda\_{t}\big(X,Z\_{t},\hat{\mathcal{L}}(X)\big) condition ([3](#S2.I2.i3 "item 3 ‣ Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) in Assumption [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") yields a constant C<∞C<\infty such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T\displaystyle\int\_{0}^{T} | M1​(ℒ^​(X,α^s))​d​s≤C+𝔼ℙ¯​[∫0T|Λs​(X,0,δ0)|​ds]+γΛ​𝔼ℙ¯​[∫0T|Zs|​ds].\displaystyle M\_{1}\big(\hat{\mathcal{L}}(X,\hat{\alpha}\_{s})\big)\mathrm{d}s\leq C+\mathbb{E}^{\bar{\mathbb{P}}}\left[\int\_{0}^{T}\left|\Lambda\_{s}(X,0,\delta\_{0})\right|\mathrm{d}s\right]+\gamma\_{\Lambda}\mathbb{E}^{\bar{\mathbb{P}}}\left[\int\_{0}^{T}\left|Z\_{s}\right|\mathrm{d}s\right]. |  |

The integrability ℒ^​(X,α^⋅)∈ℳ1\hat{\mathcal{L}}(X,\hat{\alpha}\_{\cdot})\in\mathcal{M}\_{1} follows from condition ([2](#S2.I2.i2 "item 2 ‣ Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) in Assumption [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").

The preceding remark motivates the following definition.

###### Definition 2.12.

We call a quadruple

|  |  |  |
| --- | --- | --- |
|  | (X,Y,Z,ℙ¯)∈SS2​(ℙ)×SS2​(ℙ)×ℍBMO2​(ℙ)×𝒫​(Ω)(X,Y,Z,\bar{\mathbb{P}})\in\SS^{2}(\mathbb{P})\times\SS^{2}(\mathbb{P})\times\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})\times\mathcal{P}(\Omega) |  |

a solution to the generalized MV-BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) if ℙ¯≪ℙ\bar{\mathbb{P}}\ll\mathbb{P}, the measure-flow ℒ¯​(X,Z⋅)\bar{\mathcal{L}}(X,Z\_{\cdot}) belongs to ℳ1\mathcal{M}\_{1}, and the process (X,Y,Z)(X,Y,Z) satisfies the generalized MV-BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).

It turns out that our MV-BSDE admits a solution under standard assumptions on model parameters if the parameters are bounded in the mean field term.

###### Assumption 2.13.

The model parameters satisfy the following assumptions for any (t,x)∈[0,T]×𝒞d(t,x)\in[0,T]\times\mathcal{C}\_{d} and (z,q),(z¯,q¯)∈ℝd×𝒫1​(𝒞d×ℝd)(z,q),(\bar{z},\bar{q})\in\mathbb{R}^{d}\times\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}).

1. (1)

   The functions BB, GG, and FF are bounded in x∈𝒞dx\in\mathcal{C}\_{d} and of linear growth in q∈𝒫1​(𝒞d×ℝd)q\in\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}); for some L>0L>0,

   |  |  |  |
   | --- | --- | --- |
   |  | |G​(x,qx)|+|Bt​(x,0,qx)|+|Ft​(x,0,q)|≤L​(1+M1​(q)).\left|G(x,q^{x})\right|+\left|B\_{t}(x,0,q^{x})\right|+\left|F\_{t}(x,0,q)\right|\leq L(1+M\_{1}(q)). |  |
2. (2)

   The functions
   BB and FF are (locally) Lipschitz continuous in z∈ℝdz\in\mathbb{R}^{d}; for some K>0K>0,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |Bt​(x,z,qx)−Bt​(x,z¯,qx)|\displaystyle\left|B\_{t}(x,z,q^{x})-B\_{t}(x,\bar{z},q^{x})\right| | ≤K​|z−z¯|,\displaystyle\leq K\left|z-\bar{z}\right|, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |Ft​(x,z,q)−Ft​(x,z¯,q)|\displaystyle\left|F\_{t}(x,z,q)-F\_{t}(x,\bar{z},q)\right| | ≤K​(1+|z|+|z¯|)​(|z−z¯|).\displaystyle\leq K(1+\left|z\right|+\left|\bar{z}\right|)(\left|z-\bar{z}\right|). |  |
3. (3)

   The mappings

   |  |  |  |
   | --- | --- | --- |
   |  | qx↦Bt​(x,z,qx),qx↦G​(x,qx),q↦Ft​(x,z,q)q^{x}\mapsto B\_{t}(x,z,q^{x}),\quad q^{x}\mapsto G(x,q^{x}),\quad q\mapsto F\_{t}(x,z,q) |  |

   are continuous w.r.t. the 𝒲1\mathcal{W}\_{1}-topology.

We now state the first main result of this paper. The proof is given in Section 5.

###### Theorem 2.14.

Under Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), if the model parameters are bounded in the mean-field term in the sense that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.13) |  | |G​(x,qx)|+|Bt​(x,0,qx)|+|Ft​(x,0,q)|≤L\left|G(x,q^{x})\right|+\left|B\_{t}(x,0,q^{x})\right|+\left|F\_{t}(x,0,q)\right|\leq L\\ |  |

for some L>0L>0, then the generalized MV-BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) admits a solution.

If the model parameters are unbounded in the mean-field terms, more refined conditions are required. In particular, additional growth and boundedness conditions on the drift function are required if the running costs are unbounded in the law of the state-control process.

###### Assumption 2.15.

The functions BB and FF satisfy the following conditions for any (t,x,z,q)∈[0,T]×𝒞d×ℝd×𝒫1​(𝒞d×ℝd)(t,x,z,q)\in[0,T]\times\mathcal{C}\_{d}\times\mathbb{R}^{d}\times\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}).

1. (1)

   Either of the following conditions holds for some γ>0\gamma>0:

   1. (a)

      The function FF is bounded in the law of state;

      |  |  |  |
      | --- | --- | --- |
      |  | |Ft​(x,0,q)|≤γ​(1+M1​(qz)).\left|F\_{t}(x,0,q)\right|\leq\gamma(1+M\_{1}(q^{z})). |  |
   2. (b)

      The functions BB and FF satisfy the linear growth conditions;

      |  |  |  |
      | --- | --- | --- |
      |  | |(σ​B)t​(x,z,qx)|≤γ​(1+|z|+M1​(qx)),|Ft​(x,0,q)|≤γ​(1+M1​(q)).\displaystyle\left|(\sigma B)\_{t}(x,z,q^{x})\right|\leq\gamma(1+\left|z\right|+M\_{1}(q^{x})),\quad\left|F\_{t}(x,0,q)\right|\leq\gamma(1+M\_{1}(q)). |  |
2. (2)

   The function FF satisfies the strictly quadratic growth condition; for some γ~>0\tilde{\gamma}>0 either

   |  |  |  |
   | --- | --- | --- |
   |  | Ft​(x,z,q)≤−γ~2​|z|2+Ft​(x,0,q)orFt​(x,z,q)≥γ~2​|z|2−Ft​(x,0,q).\displaystyle F\_{t}(x,z,q)\leq-\frac{\tilde{\gamma}}{2}\left|z\right|^{2}+F\_{t}(x,0,q)\quad\mbox{or}\quad F\_{t}(x,z,q)\geq\frac{\tilde{\gamma}}{2}\left|z\right|^{2}-F\_{t}(x,0,q). |  |

The following is the main result of this paper. The proof is again given in Section 5.

###### Theorem 2.16.

Under Assumptions [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the generalized MV-BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) admits a solution

|  |  |  |
| --- | --- | --- |
|  | (X,Y,Z,ℙ¯)∈SS2​(ℙ)×SS∞​(ℙ)×ℍBMO2​(ℙ)×𝒫​(Ω).(X,Y,Z,\bar{\mathbb{P}})\in\SS^{2}(\mathbb{P})\times\SS^{\infty}(\mathbb{P})\times\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P})\times\mathcal{P}(\Omega). |  |

#### 2.2.5. Generalized MV-BSDEs and MV-FBSDEs

We proceed with an equivalence result between generalized MV-BSDEs and MV-FBSDEs that will be important for our subsequent analysis. The equivalence is intuitive and is often implicitly assumed in the literature. However, there is an important subtlety on which we now elaborate. The MV-BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) under ℙ\mathbb{P} can be rewritten into the following MV-FBSDE:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.14) |  | d​Xt=(σ​B)t​(X,Zt,ℒ¯​(X))​d​t+σt​(X)​d​W¯t,X0=x0,d​Yt=−Ft​(X,Yt,Zt,ℒ¯​(X,Zt))​d​t+Zt​d​W¯t,YT=G​(X,ℒ¯​(X)).\begin{split}\mathrm{d}X\_{t}&=(\sigma B)\_{t}(X,Z\_{t},\bar{\mathcal{L}}(X))\mathrm{d}t+\sigma\_{t}(X)\mathrm{d}\bar{W}\_{t},\quad X\_{0}=x\_{0},\\ \mathrm{d}Y\_{t}&=-F\_{t}(X,Y\_{t},Z\_{t},\bar{\mathcal{L}}(X,Z\_{t}))\mathrm{d}t+Z\_{t}\mathrm{d}\bar{W}\_{t},\quad Y\_{T}=G(X,\bar{\mathcal{L}}(X)).\end{split} |  |

where

|  |  |  |
| --- | --- | --- |
|  | W¯t:=Wt−∫0tBs​(X,Zs,ℒ¯​(X))​ds.\bar{W}\_{t}:=W\_{t}-\int\_{0}^{t}B\_{s}(X,Z\_{s},\bar{\mathcal{L}}(X))\mathrm{d}s. |  |

If the stochastic exponential in ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is ℙ\mathbb{P}-martingale, then W¯\bar{W} is a ℙ¯\bar{\mathbb{P}}-Brownian motion and ([2.14](#S2.E14 "In 2.2.5. Generalized MV-BSDEs and MV-FBSDEs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) yields a MV-FBSDE under ℙ¯\bar{\mathbb{P}}. This suggests that solving the generalized MV-BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is equivalent to solving the MV-FBSDE ([2.14](#S2.E14 "In 2.2.5. Generalized MV-BSDEs and MV-FBSDEs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). The subtle issue is the different solution spaces; solving the generalized MV-BSDE under ℙ\mathbb{P} requires integrability conditions under ℙ\mathbb{P} while solving the associated MV-FBSDE requires integrability w.r.t. ℙ¯\bar{\mathbb{P}}. The next proposition shows that the two equations are indeed equivalent under the assumptions made in this section.

###### Proposition 2.17.

For any measure ℙ¯∈𝒫​(Ω)\bar{\mathbb{P}}\in\mathcal{P}(\Omega) and any triple (X,Y,Z)(X,Y,Z) of 𝔽\mathbb{F}-adapted processes, the following conditions are equivalent under Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"):

1. (1)

   the quadruple (X,Y,Z,ℙ¯)(X,Y,Z,\bar{\mathbb{P}}) solves the McKean-Vlasov BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and satisfies

   |  |  |  |
   | --- | --- | --- |
   |  | (X,Y,Z)∈SS2​(ℙ)×SS∞​(ℙ)×ℍBMO2​(ℙ),(X,Y,Z)\in\SS^{2}(\mathbb{P})\times\SS^{\infty}(\mathbb{P})\times\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}), |  |
2. (2)

   the quadruple (X,Y,Z,ℙ¯)(X,Y,Z,\bar{\mathbb{P}}) solves the McKean-Vlasov FBSDE ([2.14](#S2.E14 "In 2.2.5. Generalized MV-BSDEs and MV-FBSDEs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and satisfies

   |  |  |  |
   | --- | --- | --- |
   |  | (X,Y,Z)∈SS2​(ℙ¯)×SS∞​(ℙ¯)×ℍBMO2​(ℙ¯),(X,Y,Z)\in\SS^{2}(\bar{\mathbb{P}})\times\SS^{\infty}(\bar{\mathbb{P}})\times\mathbb{H}^{2}\_{\operatorname{BMO}}(\bar{\mathbb{P}}), |  |

If a quadruple (X,Y,Z,ℙ¯)(X,Y,Z,\bar{\mathbb{P}}) satisfies condition (1) or (2), then any constants L,L¯>0L,\bar{L}>0 there exist positive constants γℙ,γℙ¯>0\gamma\_{\mathbb{P}},\gamma\_{\bar{\mathbb{P}}}>0 such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.15) |  | ‖Z‖ℍBMO2​(ℙ)≤L\displaystyle\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})}\leq L | ⇒‖Z‖ℍBMO2​(ℙ¯)≤γℙ​‖Z‖ℍBMO2​(ℙ),\displaystyle\quad\Rightarrow\quad\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\bar{\mathbb{P}})}\leq\gamma\_{\mathbb{P}}\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})}, |  |
|  | ‖Z‖ℍBMO2​(ℙ¯)≤L¯\displaystyle\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\bar{\mathbb{P}})}\leq\bar{L} | ⇒‖Z‖ℍBMO2​(ℙ)≤γℙ¯​‖Z‖ℍBMO2​(ℙ¯).\displaystyle\quad\Rightarrow\quad\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})}\leq\gamma\_{\bar{\mathbb{P}}}\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\bar{\mathbb{P}})}. |  |

Proof.  Since ℙ∼ℙ¯\mathbb{P}\sim\bar{\mathbb{P}} we only need to verify that the pair (X,Z)(X,Z) belongs to the right spaces.

(1) ⇒\Rightarrow (2)
Since X∈SSp​(ℙ)X\in\SS^{p}(\mathbb{P}) for any p∈[2,∞)p\in[2,\infty), the reverse Hölder inequality yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯​[supt∈[0,T]|Xt|2]≤𝔼​[|d​ℙ¯d​ℙ|q]​𝔼​[supt∈[0,T]|Xt|2​p]<∞\bar{\mathbb{E}}\left[\sup\_{t\in[0,T]}\left|X\_{t}\right|^{2}\right]\leq\mathbb{E}\left[\left|\mathrm{d}\bar{\mathbb{P}}\over\mathrm{d}\mathbb{P}\right|^{q}\right]\mathbb{E}\left[\sup\_{t\in[0,T]}\left|X\_{t}\right|^{2p}\right]<\infty |  |

for some Hölder conjugates p,q>1p,q>1. By Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"),

|  |  |  |
| --- | --- | --- |
|  | |Bt​(X,Zt,ℒ¯​(X))|≤|Bt​(X,0,δ0)|+K​(|Zt|+𝔼¯​[|Xt∗|])≤C​(1+|Zt|)\left|B\_{t}(X,Z\_{t},\bar{\mathcal{L}}(X))\right|\leq\left|B\_{t}(X,0,\delta\_{0})\right|+K(\left|Z\_{t}\right|+\bar{\mathbb{E}}\left[\left|X\_{t}^{\ast}\right|\right])\leq C(1+\left|Z\_{t}\right|) |  |

for some constant C>0C>0 and so the process B⋅​(X,Z⋅,ℒ¯​(X))B\_{\cdot}(X,Z\_{\cdot},\bar{\mathcal{L}}(X)) belongs to ℍBMO2​(ℙ)\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}).
Therefore, by Proposition [B.2](#A2.Thmtheorem2 "Proposition B.2. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), there exists a constant γℙ\gamma\_{\mathbb{P}} that depends only on ‖Z‖ℍBMO2​(ℙ)\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})} such that

|  |  |  |
| --- | --- | --- |
|  | ‖Z‖ℍBMO2​(ℙ¯)≤γℙ​‖Z‖ℍBMO2​(ℙ).\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\bar{\mathbb{P}})}\leq\gamma\_{\mathbb{P}}\left\|Z\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})}. |  |

(2) ⇒\Rightarrow (1)
To prove the other direction, we use that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙd​ℙ¯\displaystyle\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\bar{\mathbb{P}}} | =ℰ​(−B⋅​(X,Z⋅,ℒ¯​(X))⋅W¯)T.\displaystyle=\mathcal{E}\left(-B\_{\cdot}(X,Z\_{\cdot},\bar{\mathcal{L}}(X))\cdot\bar{W}\right)\_{T}. |  |

From Hölder’s inequality, for some Hölder conjugates p,q>1p,q>1,

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯​[supt∈[0,T]|Xt|r]≤𝔼​[|d​ℙ¯d​ℙ|q]​[supt∈[0,T]|Xt|r​p]<∞for all​r∈[2,∞).\bar{\mathbb{E}}\left[\sup\_{t\in[0,T]}\left|X\_{t}\right|^{r}\right]\leq\mathbb{E}\left[\left|\mathrm{d}\bar{\mathbb{P}}\over\mathrm{d}\mathbb{P}\right|^{q}\right]\left[\sup\_{t\in[0,T]}\left|X\_{t}\right|^{rp}\right]<\infty\quad\text{for all}~r\in[2,\infty). |  |

We can now use the same arguments as above to show that X∈SS2​(ℙ)X\in\SS^{2}(\mathbb{P}) and Z∈ℍBMO2​(ℙ)Z\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}).
□\Box

### 2.3. Our approach

To prove the existence of mean-field equilibria it would be natural to consider, for any measure q∈ℳ1q\in\mathcal{M}\_{1}, the BSDEs

|  |  |  |  |
| --- | --- | --- | --- |
| (2.16) |  | d​Ytq=−Ht​(X,Ztq,qt)​d​t+Ztq​d​Wt,YTq=G​(X,qTx),\mathrm{d}Y\_{t}^{q}=-H\_{t}(X,Z\_{t}^{q},q\_{t})\mathrm{d}t+Z\_{t}^{q}\mathrm{d}W\_{t},\quad Y\_{T}^{q}=G(X,q^{x}\_{T}), |  |

establish the existence and uniqueness of solutions (Yq,Zq)∈SS2​(ℙ)×ℍBMO2​(ℙ)(Y^{q},Z^{q})\in\SS^{2}(\mathbb{P})\times\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}), consider the probability measures ℙq\mathbb{P}^{q} defined in terms of the processes ZqZ^{q} by

|  |  |  |
| --- | --- | --- |
|  | d​ℙqd​ℙ=ℰ​(B⋅​(X,Z⋅q,q⋅x)⋅W),\frac{\mathrm{d}\mathbb{P}^{q}}{\mathrm{d}\mathbb{P}}=\mathcal{E}\left(B\_{\cdot}(X,Z^{q}\_{\cdot},q^{x}\_{\cdot})\cdot W\right), |  |

and to prove that the following solution mapping has a fixed-point:

|  |  |  |
| --- | --- | --- |
|  | q↦ϕ​(q):=ℒq​(X,Z⋅q),whereℒq​(⋅):=ℙq∘(⋅)−1.q\mapsto{\phi}(q):=\mathcal{L}^{q}(X,Z\_{\cdot}^{q}),\quad\text{where}\quad\mathcal{L}^{q}(\cdot):=\mathbb{P}^{q}\circ(\cdot)^{-1}. |  |

This would require ϕ\phi to map a suitable compact, convex set into itself. Since we cannot expect the processes ZqZ^{q} to be continuous (c.f. [[undefae](#bib.bibx32), Section 5]), verifying compactness in ℳ1\mathcal{M}\_{1} would be difficult. To bypass this problem, we lift the solution map to the space

|  |  |  |
| --- | --- | --- |
|  | 𝒫1(𝒞d)×𝒴1([0,T]×𝒫1(𝒞d×ℝd))=:𝒫1×𝒴1\mathcal{P}\_{1}(\mathcal{C}\_{d})\times\mathcal{Y}\_{1}\big([0,T]\times\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})\big)=:\mathcal{P}\_{1}\times\mathcal{Y}\_{1} |  |

where 𝒴1​([0,T]×𝒫1​(𝒞d×ℝd))\mathcal{Y}\_{1}([0,T]\times\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})) denotes the space of integrable Young measures on [0,T]×𝒫1​(𝒞d×ℝd)[0,T]\times\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}), equipped with the stable topology.333Basic properties of (integrable) Young measures are reviewed in Appendix [C](#A3 "Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").

A subtle issue is that in our setting the mapping z⋅Bt​(x,z,qx)z\cdot B\_{t}(x,z,q^{x}) is not necessarily of linear growth in qxq^{x} due to a cross term of zz and qxq^{x}, while Ft​(x,z,q)F\_{t}(x,z,q) is always of linear growth in qq. This difference turns out to be important when lifting the solution map. To be able to treat the laws in the drift and cost term differently, we introduce the modified Hamiltonian

|  |  |  |
| --- | --- | --- |
|  | H¯t​(x,z,μ,q):=Ft​(x,z,q)+z⋅Bt​(x,z,μ)\bar{H}\_{t}(x,z,\mu,q):=F\_{t}(x,z,q)+z\cdot B\_{t}(x,z,\mu) |  |

where μ∈𝒫1​(𝒞d)\mu\in\mathcal{P}\_{1}(\mathcal{C}\_{d}) and q∈𝒫1​(𝒞d×ℝd)q\in\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}). If the driver of the original MV-BSDE satisfies Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"),
we can then consider, for any law μ∈𝒫1\mu\in\mathcal{P}\_{1} and Young measure 𝝂​(d​t,d​q)=νt​(d​q)​d​t∈𝒴1\bm{\nu}(\mathrm{d}t,\mathrm{d}q)=\nu\_{t}(\mathrm{d}q)\mathrm{d}t\in\mathcal{Y}\_{1},
the quadratic BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.17) |  | Ytμ,𝝂\displaystyle Y\_{t}^{\mu,\bm{\nu}} | =G​(X,μ)+∫tT∫𝒫1​(𝒞d×ℝd)H¯s​(X,Zsμ,𝝂,μ,q)​νs​(d​q)​ds−∫tTZsμ,𝝂​dWs.\displaystyle=G(X,\mu)+\int\_{t}^{T}\int\_{\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})}\bar{H}\_{s}(X,Z\_{s}^{\mu,\bm{\nu}},\mu,q)\nu\_{s}(\mathrm{d}q)\mathrm{d}s-\int\_{t}^{T}Z\_{s}^{\mu,\bm{\nu}}\mathrm{d}W\_{s}. |  |

The lifted BSDE is well defined because

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫𝒫1​(𝒞d×ℝd)|H¯s​(X,0,δ0,q)|​νs​(d​q)​ds≤C​(1+∫0T∫𝒫1​(𝒞d×ℝd)M1​(q)​𝝂​(d​q,d​t))<∞\int\_{0}^{T}\int\_{\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})}\left|\bar{H}\_{s}(X,0,\delta\_{0},q)\right|\nu\_{s}(\mathrm{d}q)\mathrm{d}s\leq C\left(1+\int\_{0}^{T}\int\_{\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})}M\_{1}(q)\bm{\nu}(\mathrm{d}q,\mathrm{d}t)\right)<\infty |  |

for some constant C>0C>0. If the density

|  |  |  |  |
| --- | --- | --- | --- |
| (2.18) |  | d​ℙμ,𝝂d​ℙ=ℰ​(B⋅​(X,Z⋅μ,𝝂,μ)⋅W)T\frac{\mathrm{d}\mathbb{P}^{\mu,\bm{\nu}}}{\mathrm{d}\mathbb{P}}=\mathcal{E}(B\_{\cdot}(X,Z^{\mu,\bm{\nu}}\_{\cdot},\mu)\cdot W)\_{T} |  |

is well defined, then we can define the solution map Φ\Phi on 𝒫1×𝒴1\mathcal{P}\_{1}\times\mathcal{Y}\_{1} by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.19) |  | Φ​(μ,𝝂):=(ℒμ,𝝂​(X),δℒμ,𝝂​(X,Ztμ,𝝂)​(d​q)​d​t),whereℒμ,𝝂​(⋅):=ℙμ,𝝂∘(⋅)−1.\Phi(\mu,\bm{\nu}):=\big(\mathcal{L}^{\mu,\bm{\nu}}(X),\delta\_{\mathcal{L}^{\mu,\bm{\nu}}(X,Z\_{t}^{\mu,\bm{\nu}})}(\mathrm{d}q)\mathrm{d}t\big),\quad\text{where}\quad\mathcal{L}^{\mu,\bm{\nu}}(\cdot):=\mathbb{P}^{\mu,\bm{\nu}}\circ(\cdot)^{-1}. |  |

If that mapping admits a fixed-point (μ∗,𝝂∗)∈𝒫1×𝒴1(\mu^{\*},\bm{\nu}^{\*})\in\mathcal{P}\_{1}\times\mathcal{Y}\_{1} then our MV-BSDE admits a solution and hence our MFG admits an equilibrium in weak formulation.

###### Remark 2.18.

We emphasize that the use of integrable Young measures is important to account for the integrability condition ℒμ∗,𝛎∗​(X,α^)∈ℳ1\mathcal{L}^{\mu^{\*},\bm{\nu}^{\*}}(X,\hat{\alpha})\in\mathcal{M}\_{1} of the equilibrium control α^\hat{\alpha}.

The following proposition shows that the mapping Φ\Phi is well defined in our setting; the proof follows essentially from [[undefd](#bib.bibx5), Proposition 3]. It also provides a uniform BMO-bound if the coefficients are bounded in the mean-field terms, which will be key to our subsequent analysis.

###### Proposition 2.19.

Under Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the BSDEs ([2.17](#S2.E17 "In 2.3. Our approach ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) admit a unique solution

|  |  |  |
| --- | --- | --- |
|  | (Yμ,𝝂,Zμ,𝝂)∈SS∞​(ℙ)×ℍBMO2​(ℙ)(Y^{\mu,\bm{\nu}},Z^{\mu,\bm{\nu}})\in\SS^{\infty}(\mathbb{P})\times\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}) |  |

for each (μ,𝛎)∈𝒫1×𝒴1(\mu,\bm{\nu})\in\mathcal{P}\_{1}\times\mathcal{Y}\_{1}. The solutions satisfy

|  |  |  |
| --- | --- | --- |
|  | ‖Zμ,𝝂‖ℍBMO2​(ℙ)≤ϕ​(M1​(μ),∫0T∫𝒫1​(𝒞d×ℝd)M1​(q)​𝝂​(d​q,d​t))\left\|Z^{\mu,\bm{\nu}}\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})}\leq\phi\left(M\_{1}(\mu),\int\_{0}^{T}\int\_{\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})}M\_{1}(q)\bm{\nu}(\mathrm{d}q,\mathrm{d}t)\right) |  |

for some positive function ϕ\phi.
If the boundedness condition ([2.13](#S2.E13 "In Theorem 2.14. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) holds, then the processes Zμ,𝛎Z^{\mu,\bm{\nu}} are uniformly bounded in BMO-norm:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.20) |  | CBMO:=supμ∈𝒫1,𝝂∈𝒴1‖Zμ,𝝂‖ℍBMO2​(ℙ)<∞.C\_{\operatorname{BMO}}:=\sup\_{\mu\in\mathcal{P}\_{1},\bm{\nu}\in\mathcal{Y}\_{1}}\left\|Z^{\mu,\bm{\nu}}\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P})}<\infty. |  |

If our model parameters are bounded in mean-field terms, the uniform BMO bound on the processes Zμ,𝝂Z^{\mu,\bm{\nu}} allows us to identify a convex set that the solution map maps onto itself. In fact, for any measure q=(qx,qz)q=(q^{x},q^{z}) in the range of Φ\Phi,

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫ℝd|w|2​dqtz​(w)​dt≤CBMO.\int\_{0}^{T}\int\_{\mathbb{R}^{d}}|w|^{2}\mathrm{d}q\_{t}^{z}(w)\mathrm{d}t\leq C\_{\operatorname{BMO}}. |  |

Furthermore, by construction qx≪μX:=ℙ∘X−1q^{x}\ll\mu\_{X}:=\mathbb{P}\circ X^{-1}, and by Proposition [B.4](#A2.Thmtheorem4 "Proposition B.4. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") there exists a constant δRH>0\delta\_{\operatorname{RH}}>0 such that

|  |  |  |
| --- | --- | --- |
|  | CRH:=supμ∈𝒫​(𝒞d),𝝂∈𝒴𝔼​[ℰ​(B⋅​(X,Z⋅μ,𝝂,μ)⋅W)T1+δRH]<∞.C\_{\operatorname{RH}}:=\sup\_{\mu\in\mathcal{P}(\mathcal{C}\_{d}),\bm{\nu}\in\mathcal{Y}}\mathbb{E}\left[\mathcal{E}\left(B\_{\cdot}(X,Z\_{\cdot}^{\mu,\bm{\nu}},\mu)\cdot W\right)\_{T}^{1+\delta\_{\operatorname{RH}}}\right]<\infty. |  |

In terms of these bounds, we now introduce the sets

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.21) |  | 𝒬∗\displaystyle\mathcal{Q}^{\*} | :={μ∈𝒫1​(𝒞d)|μ≪μX,∫𝒞d|d​μd​μX|1+δRH​dμX≤CRH},\displaystyle=\left\{\mu\in\mathcal{P}\_{1}(\mathcal{C}\_{d})~\middle|~\mu\ll\mu\_{X},~\int\_{\mathcal{C}\_{d}}\left|\frac{\mathrm{d}\mu}{\mathrm{d}\mu\_{X}}\right|^{1+\delta\_{\operatorname{RH}}}\mathrm{d}\mu\_{X}\leq C\_{\operatorname{RH}}\right\}, |  |
|  | 𝒦o\displaystyle\mathcal{K}^{o} | :={q∈ℳ1|qtx∈𝒬∗​for all ​t∈[0,T],∫0T∫ℝd|w|2​dqtz​(w)​dt≤CBMO}.\displaystyle=\left\{q\in\mathcal{M}\_{1}~\middle|~q\_{t}^{x}\in\mathcal{Q}^{\ast}~\mbox{for all }t\in[0,T],~\int\_{0}^{T}\int\_{\mathbb{R}^{d}}\left|w\right|^{2}\mathrm{d}q\_{t}^{z}(w)\mathrm{d}t\leq C\_{\operatorname{BMO}}\right\}. |  |

The set 𝒬∗\mathcal{Q}^{\*} is a convex subset of 𝒫1​(𝒞d)\mathcal{P}\_{1}(\mathcal{C}\_{d}) and 𝒦o\mathcal{K}^{o} is a convex subset of ℳ1\mathcal{M}\_{1}. When embedded into the set 𝒴1\mathcal{Y}\_{1}, the set 𝒦o\mathcal{K}^{o} may not be convex, but the following set is:

|  |  |  |
| --- | --- | --- |
|  | 𝒦∗:=conv⁡{δqt​(d​q)​d​t∈𝒴1∣q∈𝒦o}¯𝒮1​(𝒫1​(𝒞d×ℝd)).\mathcal{K}^{\*}:=\overline{\operatorname{conv}\{\delta\_{q\_{t}}(\mathrm{d}q)\mathrm{d}t\in\mathcal{Y}\_{1}\mid q\in\mathcal{K}^{o}\}}^{\mathcal{S}\_{1}(\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}))}. |  |

###### Corollary 2.20.

Under Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and the boundedness condition ([2.13](#S2.E13 "In Theorem 2.14. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) the solution mapping Φ\Phi can be viewed as a mapping

|  |  |  |
| --- | --- | --- |
|  | Φ:𝒫1×𝒴1→𝒬∗×𝒦∗.\Phi:\mathcal{P}\_{1}\times\mathcal{Y}\_{1}\to\mathcal{Q}^{\ast}\times\mathcal{K}^{\*}. |  |

In particular, it maps the closed convex set 𝒬∗×𝒦∗\mathcal{Q}^{\ast}\times\mathcal{K}^{\*} to itself.

In Section 3 we prove that the solution mapping is continuous and in Section 4 that 𝒬∗×𝒦∗\mathcal{Q}^{\*}\times\mathcal{K}^{\*} is compact. As a result, the solution mapping has a fixed point (μ∗,𝝂∗)∈𝒫1×𝒴1(\mu^{\*},\bm{\nu}^{\*})\in\mathcal{P}\_{1}\times\mathcal{Y}\_{1} and hence a MFG equilibrium in weak formulation exists when the model parameters are bounded in mean-field terms. The case of unbounded coefficients will be solved by approximation.

### 2.4. Examples

We close this section with a discussion of two toy models that are covered by our framework but not by existing ones. For simplicity, we consider only the case of one-dimensional state dynamics and control processes. The below examples easily extend to multi-dimensional settings and time-delayed models where xtx\_{t} is replaced by xt−δx\_{t-\delta} for some δ>0\delta>0.

###### Example 2.21 (State process governed by Geometric Brownian motion).

Let

|  |  |  |
| --- | --- | --- |
|  | x0>0,σt​(x):=xt,bt​(x,mx,a):=xt​{a+∫𝒞1x¯t​mx​(d​x¯)},g​(x,mx):=∫𝒞1x¯T​mx​(d​x¯)\displaystyle x\_{0}>0,\quad\sigma\_{t}(x):=x\_{t},\quad b\_{t}(x,m^{x},a):=x\_{t}\left\{a+\int\_{\mathcal{C}\_{1}}\bar{x}\_{t}m^{x}(\mathrm{d}\bar{x})\right\},\quad g(x,m^{x}):=\int\_{\mathcal{C}\_{1}}\bar{x}\_{T}m^{x}(\mathrm{d}\bar{x}) |  |

and

|  |  |  |
| --- | --- | --- |
|  | ft​(x,m,a):={−12​a+ϕt​(∫𝒞1x¯t​mx​(d​x¯))}⋅a+f¯​(xt)​∫ℝa¯​ma​(d​a¯),f\_{t}(x,m,a):=\left\{-\frac{1}{2}a+\phi\_{t}\left(\int\_{\mathcal{C}\_{1}}\bar{x}\_{t}m^{x}(\mathrm{d}\bar{x})\right)\right\}\cdot a+\bar{f}(x\_{t})\int\_{\mathbb{R}}\bar{a}m^{a}(\mathrm{d}\bar{a}), |  |

where ϕ:ℝ→ℝ\phi:\mathbb{R}\to\mathbb{R} is bounded and continuous, and f¯:ℝ→ℝ\bar{f}:\mathbb{R}\to\mathbb{R} is measurable and bounded. In this case XX is geometric Brownian motion. Hence σt​(X)\sigma\_{t}(X) is a.s. invertible and

|  |  |  |
| --- | --- | --- |
|  | (σ−1​b)t​(X,mx,a)=a+∫𝒞1x¯t​mx​(d​x¯).(\sigma^{-1}b)\_{t}(X,m^{x},a)=a+\int\_{\mathcal{C}\_{1}}\bar{x}\_{t}m^{x}(\mathrm{d}\bar{x}). |  |

Moreover, the maximizer Λ\Lambda of the reduced Hamiltonian ([2.4](#S2.E4 "In Theorem 2.5. ‣ 2.2.1. A sufficient maximum principle for MFGs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.22) |  | Λt​(X,m,z)=z+ϕ​(∫𝒞1x¯t​mx​(d​x¯)).\Lambda\_{t}(X,m,z)=z+\phi\left(\int\_{\mathcal{C}\_{1}}\bar{x}\_{t}m^{x}(\mathrm{d}\bar{x})\right). |  |

Since the growth condition ([2](#S2.I2.i2 "item 2 ‣ Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) of Assumption [2.8](#S2.Thmtheorem8 "Assumption 2.8. ‣ 2.2.3. Admissibility ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") is assumed on σ−1​b\sigma^{-1}b, not separately on σ−1\sigma^{-1} and bb, our framework accommodates geometric Brownian motion as state process. This point has already been emphasized in [[undefh](#bib.bibx9), Example 5.7 ]. However, their result does not cover this case as they require σ−1​b\sigma^{-1}b to be bounded, in which case their maximizer Λt\Lambda\_{t} is also bounded.
If Λ\Lambda is bounded, then the Hamiltonian is Lipschitz continuous in zz, a case that has already been addressed in, e.g.  [[undefao](#bib.bibx42)].
Furthermore, our drift function bb depends on the product of the state and control variables. Control problems involving such product term are often challenging. To the best of our knowledge, there are very few universal results for these problems.

###### Example 2.22 (Cost function unbounded in the law of state and control).

Let

|  |  |  |
| --- | --- | --- |
|  | x0>0,σt​(x):=1,bt​(x,mx,a):=a+∫𝒞1x¯t​mx​(d​x¯),g​(x,mx):=∫𝒞1x¯T​mx​(d​x¯),\displaystyle x\_{0}>0,\quad\sigma\_{t}(x):=1,\quad b\_{t}(x,m^{x},a):=a+\int\_{\mathcal{C}\_{1}}\bar{x}\_{t}m^{x}(\mathrm{d}\bar{x}),\quad g(x,m^{x}):=\int\_{\mathcal{C}\_{1}}\bar{x}\_{T}m^{x}(\mathrm{d}\bar{x}), |  |

and

|  |  |  |
| --- | --- | --- |
|  | ft​(x,m,a):={−12​a+ϕ​(∫𝒞1x¯t​mx​(d​x¯))}⋅a+f¯​(xt)​∫𝒞1×ℝ(x¯t+a¯)​m​(d​x¯,d​a¯),f\_{t}(x,m,a):=\left\{-\frac{1}{2}a+\phi\left(\int\_{\mathcal{C}\_{1}}\bar{x}\_{t}m^{x}(\mathrm{d}\bar{x})\right)\right\}\cdot a+\bar{f}(x\_{t})\int\_{\mathcal{C}\_{1}\times\mathbb{R}}(\bar{x}\_{t}+\bar{a})m(\mathrm{d}\bar{x},\mathrm{d}\bar{a}), |  |

where
ϕ\phi and f¯\bar{f} are as in Example [2.21](#S2.Thmtheorem21 "Example 2.21 (State process governed by Geometric Brownian motion). ‣ 2.4. Examples ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").
We see that the maximizer Λ\Lambda of the reduced Hamiltonian is given by ([2.22](#S2.E22 "In Example 2.21 (State process governed by Geometric Brownian motion). ‣ 2.4. Examples ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). Unlike in Example [2.21](#S2.Thmtheorem21 "Example 2.21 (State process governed by Geometric Brownian motion). ‣ 2.4. Examples ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") the running cost function is unbounded in the law of the state. This comes at the expense of dropping the multiplicative term x⋅ax\cdot a from the drift function. The drift term in Example [2.21](#S2.Thmtheorem21 "Example 2.21 (State process governed by Geometric Brownian motion). ‣ 2.4. Examples ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") does not meet the condition ([1b](#S2.I6.i1.I1.i2 "item 1b ‣ item 1 ‣ Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) of Assumption [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").

## 3. The solution mapping

In this section, we prove the continuity of the solution mapping Φ:𝒫1×𝒴1→𝒫1×𝒴1\Phi:\mathcal{P}\_{1}\times\mathcal{Y}\_{1}\to\mathcal{P}\_{1}\times\mathcal{Y}\_{1}. Our continuity result is based on a novel stability result for quadratic MV-BSDEs.

### 3.1. Stability of quadratic MV-BSDEs

The proof of the stability result requires a series of auxiliary results that we now present. In what follows (E,∥⋅∥E)(E,\left\|\cdot\right\|\_{E}) is a Banach space, and for an indexed measure ℙi∈𝒫​(Ω)\mathbb{P}^{i}\in\mathcal{P}(\Omega) we set 𝔼i​[⋅]:=𝔼ℙi​[⋅]\mathbb{E}^{i}[\cdot]:=\mathbb{E}^{\mathbb{P}^{i}}[\cdot] and ℒi​(⋅):=ℙi∘(⋅)−1\mathcal{L}^{i}(\cdot):=\mathbb{P}^{i}\circ(\cdot)^{-1}.

###### Proposition 3.1.

Let ℙn∈𝒫​(Ω)\mathbb{P}^{n}\in\mathcal{P}(\Omega) and Xn∈ℍ2​(E;ℙn)∩ℍ2​(E;ℙ∞)X^{n}\in\mathbb{H}^{2}(E;\mathbb{P}^{n})\cap\mathbb{H}^{2}(E;\mathbb{P}^{\infty}) for any n∈ℕ∗n\in\mathbb{N}^{\ast}, satisfy

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | supn∈ℕ{‖Xn‖ℍ2​(E;ℙn)+‖Xn‖ℍ2​(E;ℙ∞)}<∞.\textstyle\sup\_{n\in\mathbb{N}}\big\{\left\|X^{n}\right\|\_{\mathbb{H}^{2}(E;\mathbb{P}^{n})}+\left\|X^{n}\right\|\_{\mathbb{H}^{2}(E;\mathbb{P}^{\infty})}\big\}<\infty. |  |

If

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | ‖ℙn−ℙ∞‖TV→0\left\|\mathbb{P}^{n}-\mathbb{P}^{\infty}\right\|\_{\operatorname{TV}}\to 0 |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | 𝔼∞​[∫0T‖Xsn−Xs∞‖E2​ds]→0,\mathbb{E}^{\infty}\left[\int\_{0}^{T}\left\|X\_{s}^{n}-X\_{s}^{\infty}\right\|\_{E}^{2}\mathrm{d}s\right]\to 0, |  |

then

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | δℒn​(Xtn)​(d​q)​d​t→δℒ∞​(Xt∞)​(d​q)​d​tin𝒮1​(𝒫1​(E)).\delta\_{\mathcal{L}^{n}(X\_{t}^{n})}(\mathrm{d}q)\mathrm{d}t\to\delta\_{\mathcal{L}^{\infty}(X\_{t}^{\infty})}(\mathrm{d}q)\mathrm{d}t\quad\text{in}\quad\mathcal{S}\_{1}(\mathcal{P}\_{1}(E)). |  |

Proof.  In view of Proposition [C.10](#A3.Thmtheorem10 "Proposition C.10. ‣ C.2. Integrable Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), it suffices to prove that

|  |  |  |
| --- | --- | --- |
|  | ∫0T𝒲1​(ℒn​(Xtn),ℒ∞​(Xtn))​dt→0,and∫0T𝒲1​(ℒ∞​(Xtn),ℒ∞​(Xt∞))​dt→0.\int\_{0}^{T}\mathcal{W}\_{1}(\mathcal{L}^{n}(X\_{t}^{n}),\mathcal{L}^{\infty}(X\_{t}^{n}))\mathrm{d}t\to 0,\quad\mbox{and}\quad\int\_{0}^{T}\mathcal{W}\_{1}(\mathcal{L}^{\infty}(X\_{t}^{n}),\mathcal{L}^{\infty}(X\_{t}^{\infty}))\mathrm{d}t\to 0. |  |

The second convergence follows directly from ([3.3](#S3.E3 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). To establish the first, we set

|  |  |  |
| --- | --- | --- |
|  | Ytn,R:=Xtn​𝟏{‖Xtn‖E≤R}forR>0,n∈ℕ∗.Y\_{t}^{n,R}:=X\_{t}^{n}\bm{1}\_{\{\left\|X\_{t}^{n}\right\|\_{E}\leq R\}}\quad\mbox{for}\quad R>0,~n\in\mathbb{N}^{\ast}. |  |

Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲1\displaystyle\mathcal{W}\_{1} | (ℒn​(Xtn),ℒ∞​(Xtn))\displaystyle(\mathcal{L}^{n}(X\_{t}^{n}),\mathcal{L}^{\infty}(X\_{t}^{n})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝒲1​(ℒn​(Ytn,R),ℒ∞​(Ytn,R))﹈=⁣:Dt1​(n,R)+𝒲1​(ℒn​(Xtn),ℒn​(Ytn,R))+𝒲1​(ℒ∞​(Xtn),ℒ∞​(Ytn,R))﹈=⁣:Dt2​(n,R).\displaystyle\leq\underbracket{\mathcal{W}\_{1}\big(\mathcal{L}^{n}(Y\_{t}^{n,R}),\mathcal{L}^{\infty}(Y\_{t}^{n,R})\big)}\_{=:D\_{t}^{1}(n,R)}+\underbracket{\mathcal{W}\_{1}\big(\mathcal{L}^{n}(X\_{t}^{n}),\mathcal{L}^{n}(Y\_{t}^{n,R})\big)+\mathcal{W}\_{1}\big(\mathcal{L}^{\infty}(X\_{t}^{n}),\mathcal{L}^{\infty}(Y\_{t}^{n,R})\big)}\_{=:D\_{t}^{2}(n,R)}. |  |

The term Dt1​(n,R)D\_{t}^{1}(n,R) satisfies Dt1​(n,R)≤2​R​‖ℙn−ℙ∞‖TVD\_{t}^{1}(n,R)\leq 2R\left\|\mathbb{P}^{n}-\mathbb{P}^{\infty}\right\|\_{\operatorname{TV}},
and the term Dt2​(n,R)D\_{t}^{2}(n,R) satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.5) |  | Dt2​(n,R)\displaystyle D\_{t}^{2}(n,R) | ≤𝔼n​[‖Xtn‖E​𝟏{‖Xtn‖E>R}]+𝔼∞​[‖Xtn‖E​𝟏{‖Xtn‖E>R}]\displaystyle\leq\mathbb{E}^{n}\left[\left\|X\_{t}^{n}\right\|\_{E}\bm{1}\_{\{\left\|X\_{t}^{n}\right\|\_{E}>R\}}\right]+\mathbb{E}^{\infty}\left[\left\|X\_{t}^{n}\right\|\_{E}\bm{1}\_{\{\left\|X\_{t}^{n}\right\|\_{E}>R\}}\right] |  |
|  |  | ≤1R​(𝔼n​[‖Xtn‖E2]+𝔼∞​[‖Xtn‖E2]).\displaystyle\leq\frac{1}{R}\Big(\mathbb{E}^{n}\left[\left\|X\_{t}^{n}\right\|\_{E}^{2}]+\mathbb{E}^{\infty}[\left\|X\_{t}^{n}\right\|\_{E}^{2}\right]\Big). |  |

Combining the two estimates, we obtain the following:

|  |  |  |
| --- | --- | --- |
|  | ∫0T𝒲1​(ℒn​(Xtn),ℒ∞​(Xtn))​dt≤2​R​T​‖ℙn−ℙ∞‖TV+CR,\int\_{0}^{T}\mathcal{W}\_{1}(\mathcal{L}^{n}(X\_{t}^{n}),\mathcal{L}^{\infty}(X\_{t}^{n}))\mathrm{d}t\leq 2RT\left\|\mathbb{P}^{n}-\mathbb{P}^{\infty}\right\|\_{\operatorname{TV}}+\frac{C}{R}, |  |

for any R>0R>0 and n∈ℕn\in\mathbb{N}, where C:=supn∈ℕ(‖Xn‖ℍ2​(E;ℙn)2+‖Xn‖ℍ2​(E;ℙ∞)2)<∞C:=\sup\_{n\in\mathbb{N}}\big(\left\|X^{n}\right\|\_{\mathbb{H}^{2}(E;\mathbb{P}^{n})}^{2}+\left\|X^{n}\right\|\_{\mathbb{H}^{2}(E;\mathbb{P}^{\infty})}^{2}\big)<\infty by assumption ([3.1](#S3.E1 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). Taking R=‖ℙn−ℙ∞‖TV−1/2R=\left\|\mathbb{P}^{n}-\mathbb{P}^{\infty}\right\|\_{\operatorname{TV}}^{-1/2} yields

|  |  |  |
| --- | --- | --- |
|  | ∫0T𝒲1​(ℒn​(Xtn),ℒ∞​(Xtn))​dt≤(2​T+C)​‖ℙn−ℙ∞‖TV.\int\_{0}^{T}\mathcal{W}\_{1}(\mathcal{L}^{n}(X\_{t}^{n}),\mathcal{L}^{\infty}(X\_{t}^{n}))\mathrm{d}t\leq(2T+C)\sqrt{\left\|\mathbb{P}^{n}-\mathbb{P}^{\infty}\right\|\_{\operatorname{TV}}}. |  |

□\Box

When we later apply Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") to our stability result (Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")), the probability measures ℙn\mathbb{P}^{n} in Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") will have densities d​ℙnd​ℙ\frac{\mathrm{d}\mathbb{P}^{n}}{\mathrm{d}\mathbb{P}} w.r.t.  ℙ\mathbb{P} that are determined by stochastic exponentials.
The next proposition shows that, under this condition, the L2L^{2}-convergence ([3.3](#S3.E3 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) implies the convergence in total variation norm ([3.2](#S3.E2 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). A related result has previously been obtained by
Carmona and Lacker [[undefl](#bib.bibx13)] using the Pinsker inequality. We prepare the proposition with the following basic lemma that will be used repeatedly throughout the rest of the paper.

###### Lemma 3.2.

Let X:Ω→EX:\Omega\to E be a random variable and II be an index set. For any i∈Ii\in I let Zi∈ℍBMO2​(ℝd;ℙ)Z^{i}\in\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{R}^{d};\mathbb{P}), let θi:[0,T]×Ω×ℝd→ℝd\theta^{i}:[0,T]\times\Omega\times\mathbb{R}^{d}\to\mathbb{R}^{d} be a measurable function that satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | |θti​(z)−θti​(z¯)|≤Kθ​|z−z¯|,Kθ<∞,\left|\theta\_{t}^{i}(z)-\theta\_{t}^{i}(\bar{z})\right|\leq K\_{\theta}|z-\bar{z}|,\quad K\_{\theta}<\infty, |  |

and let ℙi∈𝒫​(Ω)\mathbb{P}^{i}\in\mathcal{P}(\Omega) be a probability measure with density d​ℙid​ℙ=ℰ​(θi​(Zi)⋅W)T.\frac{\mathrm{d}\mathbb{P}^{i}}{\mathrm{d}\mathbb{P}}=\mathcal{E}\left(\theta^{i}(Z^{i})\cdot W\right)\_{T}.
If

|  |  |  |  |
| --- | --- | --- | --- |
| (3.7) |  | X∈⋂p<∞𝕃p​(E;ℙ)andsupi∈I‖Zi‖ℍBMO2​(ℙ)+supi∈I‖θi​(0)‖ℍBMO2​(ℙ)<∞,X\in\bigcap\_{p<\infty}\mathbb{L}^{p}(E;\mathbb{P})\quad\mbox{and}\quad\sup\_{i\in I}\left\|Z^{i}\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P})}+\sup\_{i\in I}\left\|\theta^{i}(0)\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P})}<\infty, |  |

then

|  |  |  |  |
| --- | --- | --- | --- |
| (3.8) |  | supi∈I∫E|d​(ℙi∘X−1)d​(ℙ∘X−1)|1+δ​d​(ℙ∘X−1)<∞\sup\_{i\in I}\int\_{E}\left|\frac{\mathrm{d}(\mathbb{P}^{i}\circ X^{-1})}{\mathrm{d}(\mathbb{P}\circ X^{-1})}\right|^{1+\delta}\mathrm{d}(\mathbb{P}\circ X^{-1})<\infty |  |

for some δ>0\delta>0.
Furthermore,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.9) |  | supi∈I‖X‖𝕃2​(E;ℙi)<∞\sup\_{i\in I}\left\|X\right\|\_{\mathbb{L}^{2}(E;\mathbb{P}^{i})}<\infty |  |

and for any i0∈Ii\_{0}\in I,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.10) |  | supi∈I{‖Zi‖ℍBMO2​(ℙi)+‖Zi‖ℍBMO2​(ℙi0)}<∞.\sup\_{i\in I}\Big\{\left\|Z^{i}\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}^{i})}+\left\|Z^{i}\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}^{i\_{0}})}\Big\}<\infty. |  |

Proof.  By [[undefh](#bib.bibx9), Lemma 7.6] and the Jensen inequality, it holds for any δ>0\delta>0 that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫E|d​(ℙi∘X−1)d​(ℙ∘X−1)|1+δ​d​(ℙ∘X−1)\displaystyle\int\_{E}\left|\frac{\mathrm{d}(\mathbb{P}^{i}\circ X^{-1})}{\mathrm{d}(\mathbb{P}\circ X^{-1})}\right|^{1+\delta}\mathrm{d}(\mathbb{P}\circ X^{-1}) | =𝔼[|d​(ℙi∘X−1)d​(ℙ∘X−1)∘X|1+δ]=𝔼[𝔼[d​ℙid​ℙ|X]1+δ]\displaystyle=\mathbb{E}\left[\left|\frac{\mathrm{d}(\mathbb{P}^{i}\circ X^{-1})}{\mathrm{d}(\mathbb{P}\circ X^{-1})}\circ X\right|^{1+\delta}\right]=\mathbb{E}\left[\mathbb{E}\left[\frac{\mathrm{d}\mathbb{P}^{i}}{\mathrm{d}\mathbb{P}}\,\middle|\,X\right]^{1+\delta}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[ℰ​(θi​(Zi)⋅W)T1+δ].\displaystyle\leq\mathbb{E}\left[\mathcal{E}\big(\theta^{i}(Z^{i})\cdot W\big)\_{T}^{1+\delta}\right]. |  |

Assumptions ([3.6](#S3.E6 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and ([3.7](#S3.E7 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) imply supi∈I‖θi​(Zi)‖ℍBMO2​(ℙ)<∞\sup\_{i\in I}\left\|\theta^{i}(Z^{i})\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P})}<\infty and so ([3.8](#S3.E8 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from the reverse Hölder inequality. The inequality ([3.10](#S3.E10 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from the uniform BMO-bound on θi​(Zi)\theta^{i}(Z^{i}) along with Proposition [B.2](#A2.Thmtheorem2 "Proposition B.2. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") which yield a positive constant CC that does not dependent on i∈Ii\in I such that

|  |  |  |
| --- | --- | --- |
|  | ‖Zi‖ℍBMO2​(ℙi)+‖Zi‖ℍBMO2​(ℙi0)≤C​‖Zi‖ℍBMO2​(ℙ).\displaystyle\left\|Z^{i}\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}^{i})}+\left\|Z^{i}\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}^{i\_{0}})}\leq C\left\|Z^{i}\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P})}. |  |

Finally, ([3.9](#S3.E9 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from the fact that for some q>1q>1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼i​[‖X‖E2]\displaystyle\mathbb{E}^{i}[\left\|X\right\|\_{E}^{2}] | ≤∫E‖x‖E​|d​(ℙi∘X−1)d​(ℙ∘X−1)|​(ℙ∘X−1)​(d​x)\displaystyle\leq\int\_{E}\left\|x\right\|\_{E}\left|\frac{\mathrm{d}(\mathbb{P}^{i}\circ X^{-1})}{\mathrm{d}(\mathbb{P}\circ X^{-1})}\right|(\mathbb{P}\circ X^{-1})(\mathrm{d}x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[‖X‖Eq]1q​∫E|d​(ℙi∘X−1)d​(ℙ∘X−1)|1+δ​d​(ℙ∘X−1).\displaystyle\leq\mathbb{E}[{\left\|X\right\|\_{E}^{q}}]^{\frac{1}{q}}\int\_{E}\left|\frac{\mathrm{d}(\mathbb{P}^{i}\circ X^{-1})}{\mathrm{d}(\mathbb{P}\circ X^{-1})}\right|^{1+\delta}\mathrm{d}(\mathbb{P}\circ X^{-1}). |  |

□\Box

###### Proposition 3.3.

Under the assumptions of Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") with I=ℕ∗I=\mathbb{N}^{\ast} if

|  |  |  |  |
| --- | --- | --- | --- |
| (3.11) |  | 𝔼​[(∫0T|(θsn−θs∞)​(Zs∞)|2​ds)p]→0for any​p∈[1,∞),\mathbb{E}\left[\left(\int\_{0}^{T}\left|(\theta^{n}\_{s}-\theta^{\infty}\_{s})(Z\_{s}^{\infty})\right|^{2}\mathrm{d}s\right)^{p}\right]\to 0\quad\text{for any}~p\in[1,\infty), |  |

then ([3.3](#S3.E3 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) implies ([3.2](#S3.E2 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with Xn=(X,Zn)X^{n}=(X,Z^{n}). In particular, the convergence ([3.3](#S3.E3 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) implies ([3.4](#S3.E4 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).

Proof.  Assumption ([3.1](#S3.E1 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is satisfied, due to Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").
In view of the Pinsker inequality, the convergence ([3.2](#S3.E2 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows if

|  |  |  |  |
| --- | --- | --- | --- |
| (3.12) |  | H​(ℙ∞∣ℙn)=−𝔼∞​[log⁡d​ℙnd​ℙ∞]→0(n→∞),H(\mathbb{P}^{\infty}\mid\mathbb{P}^{n})=-\mathbb{E}^{\infty}\left[\log\frac{\mathrm{d}\mathbb{P}^{n}}{\mathrm{d}\mathbb{P}^{\infty}}\right]\to 0\quad(n\to\infty), |  |

where HH is the Kullback information. To see the convergence, let Θtn:=θtn​(Ztn)\Theta\_{t}^{n}:=\theta\_{t}^{n}(Z\_{t}^{n}). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(ℙ∞∣ℙn)\displaystyle H(\mathbb{P}^{\infty}\mid\mathbb{P}^{n}) | =12​𝔼∞​[∫0T|Θsn−Θs∞|2​ds]\displaystyle=\frac{1}{2}\mathbb{E}^{\infty}\left[\int\_{0}^{T}\left|\Theta\_{s}^{n}-\Theta\_{s}^{\infty}\right|^{2}\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Kθ2​𝔼∞​[∫0T|Zsn−Zs∞|2​ds]+𝔼∞​[∫0T|(θsn−θs∞)​(Zs∞)|2​ds].\displaystyle\leq K\_{\theta}^{2}\mathbb{E}^{\infty}\left[\int\_{0}^{T}\left|Z\_{s}^{n}-Z\_{s}^{\infty}\right|^{2}\mathrm{d}s\right]+\mathbb{E}^{\infty}\left[\int\_{0}^{T}\left|(\theta\_{s}^{n}-\theta\_{s}^{\infty})(Z\_{s}^{\infty})\right|^{2}\mathrm{d}s\right]. |  |

By the reverse Hölder inequality there exist p∈(1,∞)p\in(1,\infty) and Cp>0C\_{p}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼∞​[∫0T|(θsn−θs∞)​(Zs∞)|2​ds]≤Cp​𝔼∞​[(∫0T|(θsn−θs∞)​(Zs∞)|2​ds)p].\mathbb{E}^{\infty}\left[\int\_{0}^{T}\left|(\theta\_{s}^{n}-\theta\_{s}^{\infty})(Z\_{s}^{\infty})\right|^{2}\mathrm{d}s\right]\leq C\_{p}\mathbb{E}^{\infty}\left[\left(\int\_{0}^{T}\left|(\theta\_{s}^{n}-\theta\_{s}^{\infty})(Z\_{s}^{\infty})\right|^{2}\mathrm{d}s\right)^{p}\right]. |  |

Thus, the convergence ([3.3](#S3.E3 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) implies ([3.2](#S3.E2 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")), due to the assumption ([3.11](#S3.E11 "In Proposition 3.3. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).
□\Box

In view of the preceding proposition, our stability result for quadratic BSDEs reduces to verifying the condition ([3.3](#S3.E3 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). For this, the following lemma will be useful.

###### Lemma 3.4.

A sequence {Xn}n∈ℕ\{X^{n}\}\_{n\in\mathbb{N}} of EE-valued random variables on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) converges to a random variable X∞X^{\infty} in probability if there exists a BMO-bounded sequence of stochastic processes {Ψn}n∈ℕ⊂ℍBMO2​(ℙ)\{\Psi^{n}\}\_{n\in\mathbb{N}}\subset\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.13) |  | 𝔼Ψn​[‖Xn−X∞‖E]→0whered​ℙΨn:=ℰ​(Ψn⋅W)T​d​ℙ.\mathbb{E}^{\Psi^{n}}\big[\left\|X^{n}-X^{\infty}\right\|\_{E}\big]\to 0\quad\mbox{where}\quad\mathrm{d}\mathbb{P}^{\Psi^{n}}:=\mathcal{E}(\Psi^{n}\cdot W)\_{T}\mathrm{d}\mathbb{P}. |  |

Proof.  Using the Hölder inequality, we have for any p∈(1,∞)p\in(1,\infty) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖Xn−X∞‖E1p]\displaystyle\mathbb{E}\left[\left\|X^{n}-X^{\infty}\right\|\_{E}^{\frac{1}{p}}\right] | =𝔼​[ℰ​(Ψn⋅W)T1p​‖Xn−X∞‖E1p​ℰ​(Ψn⋅W)T−1p]\displaystyle=\mathbb{E}\left[\mathcal{E}(\Psi^{n}\cdot W)\_{T}^{\frac{1}{p}}\left\|X^{n}-X^{\infty}\right\|\_{E}^{\frac{1}{p}}\mathcal{E}(\Psi^{n}\cdot W)\_{T}^{-\frac{1}{p}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼Ψn​[‖Xn−X∞‖E]1p​𝔼​[(1ℰ​(Ψn⋅W)T)1q−1]1q,\displaystyle\leq\mathbb{E}^{\Psi^{n}}\left[\left\|X^{n}-X^{\infty}\right\|\_{E}\right]^{\frac{1}{p}}\mathbb{E}\left[\left(\frac{1}{\mathcal{E}(\Psi^{n}\cdot W)\_{T}}\right)^{\frac{1}{q-1}}\right]^{\frac{1}{q}}, |  |

where qq is the Hölder conjugate of pp.
Since the assumption ([3.13](#S3.E13 "In Lemma 3.4. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) implies the uniform boundedness of Ψn\Psi^{n} in ℍBMO2​(ℙ)\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}), Proposition [B.4](#A2.Thmtheorem4 "Proposition B.4. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") ensures the existence of q2∈(1,∞)q\_{2}\in(1,\infty) such that

|  |  |  |
| --- | --- | --- |
|  | supn∈ℕ𝔼​[(1ℰ​(Ψn⋅W)T)1q2−1]<∞.\sup\_{n\in\mathbb{N}}\mathbb{E}\left[\left(\frac{1}{\mathcal{E}(\Psi^{n}\cdot W)\_{T}}\right)^{\frac{1}{q\_{2}-1}}\right]<\infty. |  |

Therefore, there exists a constant C>0C>0 that does not dependent on n∈ℕn\in\mathbb{N} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖Xn−X∞‖E1p2]≤C​𝔼Ψn​[‖Xn−X∞‖E]1p2,\mathbb{E}\left[\left\|X^{n}-X^{\infty}\right\|\_{E}^{\frac{1}{p\_{2}}}\right]\leq C\mathbb{E}^{\Psi^{n}}\big[\left\|X^{n}-X^{\infty}\right\|\_{E}\big]^{\frac{1}{p\_{2}}}, |  |

where p2p\_{2} is the conjugate of q2q\_{2}.
The desired convergence therefore follows from ([3.13](#S3.E13 "In Lemma 3.4. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).
□\Box

We are now ready to state our stability result for quadratic BSDEs.

###### Theorem 3.5.

For any n∈ℕ∗n\in\mathbb{N}^{\ast} let ξn:Ω→ℝ\xi^{n}:\Omega\to\mathbb{R} be a random variable and

|  |  |  |
| --- | --- | --- |
|  | Hn:[0,T]×Ω×ℝ×ℝd→ℝH^{n}:[0,T]\times\Omega\times\mathbb{R}\times\mathbb{R}^{d}\to\mathbb{R} |  |

be a measurable function such that H⋅n​(⋅,y,z)H^{n}\_{\cdot}(\cdot,y,z) is 𝔽\mathbb{F}-progressively measurable for any (y,z)(y,z), and
the (local) Lipschitz continuity condition

|  |  |  |  |
| --- | --- | --- | --- |
| (3.14) |  | |Htn​(y,z)−Htn​(y¯,z¯)|≤KH​{|y−y¯|+(1+|z|+|z¯|)​|z−z¯|},\left|H\_{t}^{n}(y,z)-H\_{t}^{n}(\bar{y},\bar{z})\right|\leq K\_{H}\{\left|y-\bar{y}\right|+(1+\left|z\right|+\left|\bar{z}\right|)\left|z-\bar{z}\right|\}, |  |

holds for some KH>0K\_{H}>0. Assume that the BSDEs

|  |  |  |  |
| --- | --- | --- | --- |
| (3.15) |  | Ytn=ξn+∫tTHsn​(Ysn,Zsn)​ds−∫tTZsn​dWs(n∈ℕ∗)Y\_{t}^{n}=\xi^{n}+\int\_{t}^{T}H\_{s}^{n}(Y\_{s}^{n},Z\_{s}^{n})\mathrm{d}s-\int\_{t}^{T}Z\_{s}^{n}\mathrm{d}W\_{s}\quad(n\in\mathbb{N}^{\ast}) |  |

admit solutions

|  |  |  |
| --- | --- | --- |
|  | (Yn,Zn)∈⋂p<∞SSp​(ℙ)×ℍBMO2​(ℙ),(Y^{n},Z^{n})\in\bigcap\_{p<\infty}\SS^{p}(\mathbb{P})\times\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}), |  |

and let the family of functions θn\theta^{n} and probability measures ℙn∈𝒫​(Ω)\mathbb{P}^{n}\in\mathcal{P}(\Omega) be as in Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") with I=ℕ∗I=\mathbb{N}^{\ast}.
If the integrability conditions ([3.7](#S3.E7 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) hold for (θn,Zn)(\theta^{n},Z^{n}), if

|  |  |  |  |
| --- | --- | --- | --- |
| (3.16) |  | ξn∈⋂p<∞Lp​(Ω),supn∈ℕ𝔼​[|∫0T|​Hsn​(0,0)​|d​s|p]<∞for all​p∈[0,∞),\begin{split}\xi^{n}\in\bigcap\_{p<\infty}L^{p}(\Omega),\quad\sup\_{n\in\mathbb{N}}\mathbb{E}\left[\left|\int\_{0}^{T}\left|H\_{s}^{n}(0,0)\right|\mathrm{d}s\right|^{p}\right]<\infty\quad\text{for all}~p\in[0,\infty),\end{split} |  |

and if for all p∈[1,∞)p\in[1,\infty) and t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
| (3.17) |  | 𝔼​[|ξn−ξ∞|p+(∫0T|(θsn−θs∞)​(Zs∞)|2​ds)p]→0,∫tT(Hsn−Hs∞)​(Ys∞,Zs∞)​ds→0ℙ​-a.s.\begin{split}&\mathbb{E}\left[\left|\xi^{n}-\xi^{\infty}\right|^{p}+\left(\int\_{0}^{T}\left|(\theta^{n}\_{s}-\theta^{\infty}\_{s})(Z\_{s}^{\infty})\right|^{2}\mathrm{d}s\right)^{p}\right]\to 0,\\ &\int\_{t}^{T}(H\_{s}^{n}-H\_{s}^{\infty})(Y\_{s}^{\infty},Z\_{s}^{\infty})\mathrm{d}s\to 0\quad\mathbb{P}\text{-a.s.}\end{split} |  |

as n→∞n\to\infty, then the convergence ([3.4](#S3.E4 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) holds with Xn=(X,Zn)X^{n}=(X,Z^{n}) for any X∈⋂p<∞𝕃p​(E;ℙ)X\in\bigcap\_{p<\infty}\mathbb{L}^{p}(E;\mathbb{P}).

Proof.  Let X∈⋂p<∞𝕃p​(E;ℙ)X\in\bigcap\_{p<\infty}\mathbb{L}^{p}(E;\mathbb{P}) and set Xn:=(X,Zn)X^{n}:=(X,Z^{n}).
Since θn\theta^{n} and ZnZ^{n} satisfy the assumptions in Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), it follows from Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") that the convergence ([3.4](#S3.E4 "In Proposition 3.1. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) holds if 444A stronger convergence result for (Zn)(Z^{n}) has been obtained in [[undefar](#bib.bibx45), Theorem 7.3.4] under a uniform boundedness on the sequence (Yn)(Y^{n}) in the SS∞\SS^{\infty}-norm. We do not require this condition for ([3.18](#S3.E18 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).

|  |  |  |  |
| --- | --- | --- | --- |
| (3.18) |  | 𝔼∞​[∫0T|Zsn−Zs∞|2​ds]→0.\mathbb{E}^{\infty}\left[\int\_{0}^{T}\left|Z\_{s}^{n}-Z\_{s}^{\infty}\right|^{2}\mathrm{d}s\right]\to 0. |  |

Step 1. The convergence ([3.18](#S3.E18 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from Vitali’s convergence theorem if

|  |  |  |  |
| --- | --- | --- | --- |
| (3.19) |  | {∫0T|Δ​Zsn|2​ds}n∈ℕ​is uniformly integrable w.r.t. ​ℙ∞,\left\{\int\_{0}^{T}\left|\Delta Z\_{s}^{n}\right|^{2}\mathrm{d}s\right\}\_{n\in\mathbb{N}}~\text{is uniformly integrable w.r.t.~}~\mathbb{P}^{\infty}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (3.20) |  | ∫0T|Δ​Zsn|2​ds→0in probability under​ℙ∞.\int\_{0}^{T}\left|\Delta Z\_{s}^{n}\right|^{2}\mathrm{d}s\to 0\quad\text{in probability under}~\mathbb{P}^{\infty}. |  |

By the energy inequality (Proposition [B.3](#A2.Thmtheorem3 "Proposition B.3 (Energy inequality). ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and the equivalency of the BMO norms (Proposition [B.2](#A2.Thmtheorem2 "Proposition B.2. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")), it follows from our assumptions that

|  |  |  |
| --- | --- | --- |
|  | supn∈ℕ𝔼∞​[(∫0T|Δ​Zsn|2​ds)2]≤2​supn∈ℕ‖Δ​Zn‖ℍBMO2​(ℙ∞)4<∞.\sup\_{n\in\mathbb{N}}\mathbb{E}^{\infty}\left[\left(\int\_{0}^{T}\left|\Delta Z\_{s}^{n}\right|^{2}\mathrm{d}s\right)^{2}\right]\leq 2\sup\_{n\in\mathbb{N}}\left\|\Delta Z^{n}\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}^{\infty})}^{4}<\infty. |  |

This implies the uniform integrability ([3.19](#S3.E19 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).
To prove the convergence ([3.20](#S3.E20 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")), it suffices to prove the corresponding convergence in probability under ℙ\mathbb{P} since ℙ∞≪ℙ\mathbb{P}^{\infty}\ll\mathbb{P}.555Absolute continuity of ℙ∞\mathbb{P}^{\infty} w.r.t. ℙ\mathbb{P} is equivalent to the following condition:

limδ↓0(sup{ℙ∞​(A)∣A∈ℱ,ℙ​(A)≤δ})=0.\lim\_{\delta\downarrow 0}(\sup\{\mathbb{P}^{\infty}(A)\mid A\in\mathcal{F},~\mathbb{P}(A)\leq\delta\})=0.

Step 2. By Lemma [3.4](#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the convergence ([3.20](#S3.E20 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) under ℙ\mathbb{P} follows if we find a BMO-bounded sequence {Ψn}n∈ℕ⊂ℍBMO2​(ℙ)\{\Psi^{n}\}\_{n\in\mathbb{N}}\subset\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}) that satisfies condition ([3.13](#S3.E13 "In Lemma 3.4. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with

|  |  |  |
| --- | --- | --- |
|  | Xn:=∫0T|Zsn−Zs∞|2​ds,X∞:=0.X^{n}:=\int\_{0}^{T}\left|Z\_{s}^{n}-Z\_{s}^{\infty}\right|^{2}\mathrm{d}s,\quad X^{\infty}:=0. |  |

For this, we use the BSDEs ([3.15](#S3.E15 "In Theorem 3.5. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). Setting Δ​ξn:=ξn−ξ∞\Delta\xi^{n}:=\xi^{n}-\xi^{\infty}, Δ​Yn:=Yn−Y∞\Delta Y^{n}:=Y^{n}-Y^{\infty} and Δ​Zn:=Zn−Z∞\Delta Z^{n}:=Z^{n}-Z^{\infty} we see that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.21) |  | Δ​Ytn\displaystyle\Delta Y\_{t}^{n} | =Δ​ξn+∫tT{δy​Hsn​Δ​Ysn+Δn​Hs​(Ys∞,Zs∞)}​ds−∫tTΔ​Zsn​dW¯sn,\displaystyle=\Delta\xi^{n}+\int\_{t}^{T}\{\delta\_{y}H\_{s}^{n}\Delta Y\_{s}^{n}+\Delta\_{n}H\_{s}(Y\_{s}^{\infty},Z\_{s}^{\infty})\}\mathrm{d}s-\int\_{t}^{T}\Delta Z\_{s}^{n}\mathrm{d}\bar{W}\_{s}^{n}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | W¯tn:=Wt−∫0tδz​Hsn​ds,Δn​Ht​(y,z):=Htn​(y,z)−Ht∞​(y,z),\displaystyle\bar{W}\_{t}^{n}:=W\_{t}-\int\_{0}^{t}\delta\_{z}H\_{s}^{n}\mathrm{d}s,\quad\Delta\_{n}H\_{t}(y,z):=H\_{t}^{n}(y,z)-H\_{t}^{\infty}(y,z), |  |
|  |  |  |
| --- | --- | --- |
|  | δy​Htn:=Htn​(Ytn,Ztn)−Htn​(Yt∞,Ztn)Δ​Ytn​𝟏{Δ​Ytn≠0},\displaystyle\delta\_{y}H\_{t}^{n}:=\frac{H\_{t}^{n}(Y\_{t}^{n},Z\_{t}^{n})-H\_{t}^{n}(Y\_{t}^{\infty},Z\_{t}^{n})}{\Delta Y\_{t}^{n}}\mathbf{1}\_{\{\Delta Y\_{t}^{n}\neq 0\}}, |  |
|  |  |  |
| --- | --- | --- |
|  | δz​Htn:=Htn​(Yt∞,Ztn)−Htn​(Yt∞,Zt∞)|Δ​Ztn|2⋅Δ​Ztn​𝟏{|Δ​Ztn|≠0}.\displaystyle\delta\_{z}H\_{t}^{n}:=\frac{H\_{t}^{n}(Y\_{t}^{\infty},Z\_{t}^{n})-H\_{t}^{n}(Y\_{t}^{\infty},Z\_{t}^{\infty})}{\left|\Delta Z\_{t}^{n}\right|^{2}}\cdot\Delta Z\_{t}^{n}\mathbf{1}\_{\{\left|\Delta Z\_{t}^{n}\right|\neq 0\}}. |  |

In particular, W¯n\bar{W}^{n} is a Brownian motion under the probability measure ℙ¯n\bar{\mathbb{P}}^{n} with density d​ℙ¯nd​ℙ=ℰ​(δz​Hn⋅W)T;\frac{\mathrm{d}\bar{\mathbb{P}}^{n}}{\mathrm{d}\mathbb{P}}=\mathcal{E}(\delta\_{z}H^{n}\cdot W)\_{T}; the density is well defined since δz​Hn∈ℍBMO2​(ℙ)\delta\_{z}H^{n}\in\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}) by assumption. In the next step, we show that condition ([3.13](#S3.E13 "In Lemma 3.4. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) holds with Ψn:=δz​Hn\Psi^{n}:=\delta\_{z}H^{n}.

Step 3.
The required uniform BMO bound follows from the assumption ([3.7](#S3.E7 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). It remains to prove that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.22) |  | 𝔼¯n​[∫0T|Δ​Zsn|2​ds]→0(n→∞).\bar{\mathbb{E}}^{n}\left[\int\_{0}^{T}\left|\Delta Z\_{s}^{n}\right|^{2}\mathrm{d}s\right]\to 0\quad(n\to\infty). |  |

The above expected values are well defined since Δ​Zn∈ℍBMO2​(ℙ)\Delta Z^{n}\in\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}) and δz​Hn∈ℍBMO2​(ℙ)\delta\_{z}H^{n}\in\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}) and so Proposition [B.2](#A2.Thmtheorem2 "Proposition B.2. ‣ Appendix B BMO martingales ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") implies Δ​Zn∈ℍBMO2​(ℙ¯n)\Delta Z^{n}\in\mathbb{H}\_{\operatorname{BMO}}^{2}(\bar{\mathbb{P}}^{n}). By moving the stochastic integral to the left hand side in the equation ([3.21](#S3.E21 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and then taking expectations under ℙ¯n\bar{\mathbb{P}}^{n}, we see that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.23) |  | 𝔼¯n​[|Δ​Ytn|2]\displaystyle\bar{\mathbb{E}}^{n}[\left|\Delta Y\_{t}^{n}\right|^{2}] | +𝔼¯n​[∫tT|Δ​Zsn|2​ds]\displaystyle+\bar{\mathbb{E}}^{n}\left[\int\_{t}^{T}\left|\Delta Z\_{s}^{n}\right|^{2}\mathrm{d}s\right] |  |
|  |  | =𝔼¯n​[|Δ​ξn+∫tT{δy​Hsn​Δ​Ysn+Δn​Hs​(Ys∞,Zs∞)}​ds|2]\displaystyle=\bar{\mathbb{E}}^{n}\left[\left|\Delta\xi^{n}+\int\_{t}^{T}\{\delta\_{y}H\_{s}^{n}\Delta Y\_{s}^{n}+\Delta\_{n}H\_{s}(Y\_{s}^{\infty},Z\_{s}^{\infty})\}\mathrm{d}s\right|^{2}\right] |  |
|  |  | ≤3​{T​|KH|2​∫tT𝔼¯n​[|Δ​Ysn|2]​ds+𝔼¯n​[|Δ​ξn|2+|∫tTΔn​Hs​(Ys∞,Zs∞)|2]}.\displaystyle\leq 3\left\{T\left|K\_{H}\right|^{2}\int\_{t}^{T}\bar{\mathbb{E}}^{n}[\left|\Delta Y\_{s}^{n}\right|^{2}]\mathrm{d}s+\bar{\mathbb{E}}^{n}\left[\left|\Delta\xi^{n}\right|^{2}+\left|\int\_{t}^{T}\Delta\_{n}H\_{s}(Y\_{s}^{\infty},Z\_{s}^{\infty})\right|^{2}\right]\right\}. |  |

From Gronwall’s inequality it then follows that

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯n​[|Δ​Ytn|2]≤C​(𝔼¯n​[|Δ​ξn|2]+αtn+∫tTαsn​ds)\bar{\mathbb{E}}^{n}[\left|\Delta Y\_{t}^{n}\right|^{2}]\leq C\left(\bar{\mathbb{E}}^{n}[\left|\Delta\xi^{n}\right|^{2}]+\alpha\_{t}^{n}+\int\_{t}^{T}\alpha\_{s}^{n}\mathrm{d}s\right) |  |

for some C>0C>0, where

|  |  |  |
| --- | --- | --- |
|  | αtn:=𝔼¯n​[|∫tTΔn​Hs​(Ys∞,Zs∞)​ds|2].\alpha\_{t}^{n}:=\bar{\mathbb{E}}^{n}\left[\left|\int\_{t}^{T}\Delta\_{n}H\_{s}(Y\_{s}^{\infty},Z\_{s}^{\infty})\mathrm{d}s\right|^{2}\right]. |  |

Plugging this result into the inequality ([3.23](#S3.E23 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) yields for some C~>0\tilde{C}>0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.24) |  | 𝔼¯n​[∫0T|Δ​Zsn|2​ds]\displaystyle\bar{\mathbb{E}}^{n}\left[\int\_{0}^{T}\left|\Delta Z\_{s}^{n}\right|^{2}\mathrm{d}s\right] | ≤C~​(𝔼¯n​[|Δ​ξn|2]+α0n+∫0Tαtn​dt).\displaystyle\leq\tilde{C}\left(\bar{\mathbb{E}}^{n}[\left|\Delta\xi^{n}\right|^{2}]+\alpha\_{0}^{n}+\int\_{0}^{T}\alpha\_{t}^{n}\mathrm{d}t\right). |  |

Since supn∈ℕ‖δz​Hn‖ℍBMO2​(ℙ)<∞\sup\_{n\in\mathbb{N}}\left\|\delta\_{z}H^{n}\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P})}<\infty, the reverse Hölder inequality yields p1∈(1,∞)p\_{1}\in(1,\infty) s.t.

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯n​[|Δ​ξn|2]≤𝔼​[ℰ​(δz​Hn⋅W)Tp1]1p1​𝔼​[|Δ​ξn|2​q1]1q1≤Cp1​𝔼​[|Δ​ξn|2​q1]1q1,\bar{\mathbb{E}}^{n}[\left|\Delta\xi^{n}\right|^{2}]\leq\mathbb{E}[\mathcal{E}(\delta\_{z}H^{n}\cdot W)\_{T}^{p\_{1}}]^{\frac{1}{p\_{1}}}\mathbb{E}[\left|\Delta\xi^{n}\right|^{2q\_{1}}]^{\frac{1}{q\_{1}}}\leq C\_{p\_{1}}\mathbb{E}[\left|\Delta\xi^{n}\right|^{2q\_{1}}]^{\frac{1}{q\_{1}}}, |  |

where q1q\_{1} is the Hölder conjugate of p1p\_{1} and Cp1C\_{p\_{1}} depends only on p1p\_{1}.
Thus, by assumption

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯n​[|Δ​ξn|2]→0(n→∞).\bar{\mathbb{E}}^{n}[\left|\Delta\xi^{n}\right|^{2}]\to 0\quad(n\to\infty). |  |

Analogously, we can apply the reverse Hölder inequality to obtain

|  |  |  |
| --- | --- | --- |
|  | αtn≤Cp1​𝔼​[|∫tTΔn​Hs​(Ys∞,Zs∞)​ds|2​q1]1q1.\alpha\_{t}^{n}\leq C\_{p\_{1}}\mathbb{E}\left[\left|\int\_{t}^{T}\Delta\_{n}H\_{s}(Y\_{s}^{\infty},Z\_{s}^{\infty})\mathrm{d}s\right|^{2q\_{1}}\right]^{\frac{1}{q\_{1}}}. |  |

Therefore, we have pointwise convergence αtn→0\alpha\_{t}^{n}\to 0 for all t∈[0,T]t\in[0,T]. Since supn∈ℕ∫0T|αtn|q1​dt<∞\sup\_{n\in\mathbb{N}}\int\_{0}^{T}\left|\alpha\_{t}^{n}\right|^{q\_{1}}\mathrm{d}t<\infty the functions are uniformly integrable and so

|  |  |  |
| --- | --- | --- |
|  | ∫0Tαtn​dt→0.\int\_{0}^{T}\alpha\_{t}^{n}\mathrm{d}t\to 0. |  |

Thus, the second term also converges to zero and ([3.22](#S3.E22 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from ([3.24](#S3.E24 "In 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).
□\Box

### 3.2. Continuity of the solution mapping

Since the space 𝒞d×ℝd\mathcal{C}\_{d}\times\mathbb{R}^{d} is Banach space, the set 𝒫1​(𝒞d×ℝd)\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}) is a Polish space under the Wasserstein-1 distance. Thus, by Proposition [C.4](#A3.Thmtheorem4 "Proposition C.4. ‣ C.1. Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") the stable topology 𝒮​(𝒫1​(𝒞d×ℝd))\mathcal{S}(\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})) on the set of Young measures on 𝒫1​(𝒞d×ℝd)\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}) is metrizable.

Since this topology is weaker than the 𝒮1​(𝒫1​(𝒞d×ℝd))\mathcal{S}\_{1}(\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d}))-topology when restricted to the set of integrable Young measures, any compact set 𝒦⊂𝒴1\mathcal{K}\subset\mathcal{Y}\_{1} is metrizable. This allows us to prove that the solution mapping Φ\Phi is sequentially continuous and continuous on any compact set.666We used the following facts. (i) If f:X→Yf:X\to Y is a continuous bijection and if XX is compact and YY is Hausdorff, then ff is homeomorphism. In particular, any two compact topologies τ0⊂τ1\tau\_{0}\subset\tau\_{1} on the common set XX coincide if τ0\tau\_{0} is Hausdorff; c.f. [[undefam](#bib.bibx40), Theorem 26.6] and [[undefap](#bib.bibx43), p.62]. (ii) A function on a metric space is continuous iff it is sequentially continuous.

###### Corollary 3.6.

Under Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the solution mapping Φ:𝒫1×𝒴1→𝒫1×𝒴1\Phi:\mathcal{P}\_{1}\times\mathcal{Y}\_{1}\to\mathcal{P}\_{1}\times\mathcal{Y}\_{1} is sequentially continuous and continuous on any compact subset of 𝒫1×𝒴1\mathcal{P}\_{1}\times\mathcal{Y}\_{1}.

Proof.  In view of the preceding discussion, we only need to establish sequential continuity. Let

|  |  |  |
| --- | --- | --- |
|  | {(μn,𝝂n)}n∈ℕ⊂𝒫1×𝒴1\{(\mu^{n},\bm{\nu}^{n})\}\_{n\in\mathbb{N}}\subset\mathcal{P}\_{1}\times\mathcal{Y}\_{1} |  |

be a sequence that converges to (μ∞,𝝂∞)∈𝒫1×𝒴1(\mu^{\infty},\bm{\nu}^{\infty})\in\mathcal{P}\_{1}\times\mathcal{Y}\_{1}, and let ν⋅n\nu\_{\cdot}^{n} be the unique disintegration of the Young measure 𝝂n\bm{\nu}^{n}. For each n∈ℕ∗n\in\mathbb{N}^{\ast}, let

|  |  |  |  |
| --- | --- | --- | --- |
| (3.25) |  | ξn:=G​(X,μn),θtn​(z):=Bt​(X,z,μn),ℙn:=ℙμn,𝝂n,Htn​(z):=∫𝒫1​(𝒞d×ℝd)H¯t​(X,z,μn,q)​νt​(d​q),(Yn,Zn):=(Yμn,𝝂n,Zμn,𝝂n).\begin{gathered}\xi^{n}:=G(X,\mu^{n}),\quad\theta\_{t}^{n}(z):=B\_{t}(X,z,\mu^{n}),\quad\mathbb{P}^{n}:=\mathbb{P}^{\mu^{n},\bm{\nu}^{n}},\\ H\_{t}^{n}(z):=\int\_{\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})}\bar{H}\_{t}(X,z,\mu^{n},q)\nu\_{t}(\mathrm{d}q),\quad(Y^{n},Z^{n}):=(Y^{\mu^{n},\bm{\nu}^{n}},Z^{\mu^{n},\bm{\nu}^{n}}).\end{gathered} |  |

We need to verify the assumptions of Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").
The assumptions on the state process XX and the functions θn\theta^{n} are clear.
Since the sequence {(μn,𝝂n)}n∈ℕ\{(\mu^{n},\bm{\nu}^{n})\}\_{n\in\mathbb{N}} converges in 𝒫1×𝒴1\mathcal{P}\_{1}\times\mathcal{Y}\_{1} and hence

|  |  |  |
| --- | --- | --- |
|  | supn∈ℕM1​(μn)<∞,supn∈ℕ∫0T∫𝒫1​(𝒞d×ℝd)𝒲1​(δ0,q)​𝝂n​(d​q,d​t)<∞,\sup\_{n\in\mathbb{N}}M\_{1}(\mu^{n})<\infty,\quad\sup\_{n\in\mathbb{N}}\int\_{0}^{T}\int\_{\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})}\mathcal{W}\_{1}(\delta\_{0},q)\bm{\nu}^{n}(\mathrm{d}q,\mathrm{d}t)<\infty, |  |

the integrability condition ([3.16](#S3.E16 "In Theorem 3.5. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from Assumption [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"). The uniform BMO-bound ([3.7](#S3.E7 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from Proposition [2.19](#S2.Thmtheorem19 "Proposition 2.19. ‣ 2.3. Our approach ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").
It remains to verify the convergence ([3.17](#S3.E17 "In Theorem 3.5. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")). The convergences

|  |  |  |  |
| --- | --- | --- | --- |
| (3.26) |  | 𝔼​[|ξn−ξ∞|p]→0,𝔼​[(∫0T|(θsn−θs∞)​(Zs∞)|2​ds)p]→0for all​p∈[1,∞),\mathbb{E}[\left|\xi^{n}-\xi^{\infty}\right|^{p}]\to 0,\quad\mathbb{E}\left[\left(\int\_{0}^{T}\left|(\theta\_{s}^{n}-\theta\_{s}^{\infty})(Z\_{s}^{\infty})\right|^{2}\mathrm{d}s\right)^{p}\right]\to 0\quad\text{for all}~p\in[1,\infty), |  |

follow from the dominated convergence theorem.
In addition, for any t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tT(Hsn−Hs∞)​(Zs∞)​ds\displaystyle\int\_{t}^{T}(H\_{s}^{n}-H\_{s}^{\infty})(Z\_{s}^{\infty})\mathrm{d}s | =∫tT∫𝒫1​(𝒞d×ℝd)Fs​(X,Zs∞,q)​(νsn−νs∞)​(d​q)​ds\displaystyle=\int\_{t}^{T}\int\_{\mathcal{P}\_{1}(\mathcal{C}\_{d}\times\mathbb{R}^{d})}F\_{s}(X,Z\_{s}^{\infty},q)(\nu\_{s}^{n}-\nu\_{s}^{\infty})(\mathrm{d}q)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫tTZs∞⋅{Bs​(X,Zs∞,μn)−Bs​(X,Zs∞,μ∞)}​ds\displaystyle\hskip 50.00008pt+\int\_{t}^{T}Z\_{s}^{\infty}\cdot\big\{B\_{s}(X,Z\_{s}^{\infty},\mu^{n})-B\_{s}(X,Z\_{s}^{\infty},\mu^{\infty})\big\}\mathrm{d}s |  |

where, by assumption,

|  |  |  |
| --- | --- | --- |
|  | |Ft​(X,Zt∞,q)|≤C​(1+|Zt∞|2+𝒲1​(δ0,q))ℙ​-a.s.\left|F\_{t}(X,Z\_{t}^{\infty},q)\right|\leq C(1+\left|Z\_{t}^{\infty}\right|^{2}+\mathcal{W}\_{1}(\delta\_{0},q))\quad\mathbb{P}\text{-a.s.} |  |

Hence it follows from Proposition [C.10](#A3.Thmtheorem10 "Proposition C.10. ‣ C.2. Integrable Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and the dominated convergence theorem that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.27) |  | ∫tT(Hsn−Hs∞)​(Zs∞)​ds→0ℙ​-a.s. for any​t∈[0,T].\int\_{t}^{T}(H\_{s}^{n}-H\_{s}^{\infty})(Z\_{s}^{\infty})\mathrm{d}s\to 0\quad\mathbb{P}\text{-a.s.\ for any}~t\in[0,T]. |  |

□\Box

In view of the above corollary, to establish the existence of a fixed point it remains to identify a compact, convex subset of 𝒫1×𝒴1\mathcal{P}\_{1}\times\mathcal{Y}\_{1} that the solution mapping maps to itself. In the following section, we establish sufficient conditions for compactness in the space 𝒴1\mathcal{Y}\_{1}. In particular, the range 𝒬∗×𝒦∗\mathcal{Q}^{\*}\times\mathcal{K}^{\*} of our solution mapping introduced in Corollary [2.20](#S2.Thmtheorem20 "Corollary 2.20. ‣ 2.3. Our approach ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") turns out to be compact.

## 4. Compactness in the space of integrable Young measures

We start with the following basic lemma. The proof follows from the fact that weak relative compactness together with uniform integrability implies relative compactness in the 𝒲1\mathcal{W}\_{1}-topology (c.f. [[undefj](#bib.bibx11), Corollary 5.6]).

###### Lemma 4.1.

Let 𝒬⊂𝒫1​(E)\mathcal{Q}\subset\mathcal{P}\_{1}(E) and 𝔎⊂𝒫1​(ℝd)\mathfrak{K}\subset\mathcal{P}\_{1}(\mathbb{R}^{d}) be relatively compact subsets of probability measures. Then, the set

|  |  |  |
| --- | --- | --- |
|  | 𝔎¯:={q∈𝒫1​(E×ℝd)∣qx∈𝒬,qz∈𝔎}\bar{\mathfrak{K}}:=\{q\in\mathcal{P}\_{1}(E\times\mathbb{R}^{d})\mid q^{x}\in\mathcal{Q},~q^{z}\in\mathfrak{K}\} |  |

is relatively compact in 𝒫1​(E×ℝd)\mathcal{P}\_{1}(E\times\mathbb{R}^{d}).

The next lemma is essentially a corollary of Proposition 7.8 in [[undefl](#bib.bibx13)].

###### Lemma 4.2.

For any reference measure 𝔮x∈⋂p<∞𝒫p​(E)\mathfrak{q}^{x}\in\bigcap\_{p<\infty}\mathcal{P}\_{p}(E), and any δ,C>0\delta,C>0, the set

|  |  |  |
| --- | --- | --- |
|  | 𝒬:={qx∈𝒫1​(E)|qx≪𝔮x,∫E|d​qxd​𝔮x|1+δ​d𝔮x≤C}⊂𝒫1​(E).\mathcal{Q}:=\left\{q^{x}\in\mathcal{P}\_{1}(E)~\middle|~q^{x}\ll\mathfrak{q}^{x},~\int\_{E}\left|\frac{\mathrm{d}q^{x}}{\mathrm{d}\mathfrak{q}^{x}}\right|^{1+\delta}\mathrm{d}\mathfrak{q}^{x}\leq C\right\}\subset\mathcal{P}\_{1}(E). |  |

Proof.  By Proposition 7.8 in [[undefl](#bib.bibx13)], the set 𝒬\mathcal{Q} is weakly compact in 𝒫​(E)\mathcal{P}(E).
Since for some q>1q>1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supqx∈𝒬∫E‖x‖E2​dqx​(x)\displaystyle\sup\_{q^{x}\in\mathcal{Q}}\int\_{E}\left\|x\right\|\_{E}^{2}\mathrm{d}q^{x}(x) | ≤(∫E‖x‖E2​q​d𝔮x​(x))1q​supqx∈𝒬(∫E|d​qxd​𝔮x|1+δ​d𝔮x)11+δ\displaystyle\leq\left(\int\_{E}\left\|x\right\|\_{E}^{2q}\mathrm{d}\mathfrak{q}^{x}(x)\right)^{\frac{1}{q}}\sup\_{q^{x}\in\mathcal{Q}}\left(\int\_{E}\left|\frac{\mathrm{d}q^{x}}{\mathrm{d}\mathfrak{q}^{x}}\right|^{1+\delta}\mathrm{d}\mathfrak{q}^{x}\right)^{\frac{1}{1+\delta}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C11+δ​M2​q​(𝔮x)1q,\displaystyle\leq C^{\frac{1}{1+\delta}}M\_{2q}(\mathfrak{q}^{x})^{\frac{1}{q}}, |  |

the set is uniformly integrable and thus 𝒲1\mathcal{W}\_{1}-relatively compact.
Since 𝒲1\mathcal{W}\_{1}-convergence implies weak convergence and since 𝒬\mathcal{Q} is weakly closed, it is also 𝒲1\mathcal{W}\_{1}-closed and hence 𝒲1\mathcal{W}\_{1}-compact.
□\Box

The next theorem proves a compactness condition for integrable Young measures.

###### Theorem 4.3.

Let II be an index set and assume that the family of integrable measure-flows {qi}i∈I⊂ℳ1\{q^{i}\}\_{i\in I}\subset\mathcal{M}\_{1} satisfies the following conditions:

1. (1)

   There exists δ1,C1>0\delta\_{1},C\_{1}>0 and a reference measure 𝔮x∈⋂p<∞𝒫p​(E)\mathfrak{q}^{x}\in\bigcap\_{p<\infty}\mathcal{P}\_{p}(E) such that

   |  |  |  |
   | --- | --- | --- |
   |  | qti,x≪𝔮xfor all​i∈I,t∈[0,T],q\_{t}^{i,x}\ll\mathfrak{q}^{x}\quad\text{for all}~i\in I,~t\in[0,T], |  |

   and

   |  |  |  |
   | --- | --- | --- |
   |  | supi∈I∫E|d​qti,xd​𝔮x|1+δ1​d𝔮x≤C1.\sup\_{i\in I}\int\_{E}\left|\frac{\mathrm{d}q\_{t}^{i,x}}{\mathrm{d}\mathfrak{q}^{x}}\right|^{1+\delta\_{1}}\mathrm{d}\mathfrak{q}^{x}\leq C\_{1}. |  |
2. (2)

   There exists δ2,C2>0\delta\_{2},C\_{2}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | supi∈I∫0T∫ℝd|w|1+δ2​qti,z​(d​w)​dt≤C2.\sup\_{i\in I}\int\_{0}^{T}\int\_{\mathbb{R}^{d}}\left|w\right|^{1+\delta\_{2}}q\_{t}^{i,z}(\mathrm{d}w)\mathrm{d}t\leq C\_{2}. |  |

Then, the family of integrable Young measures {𝛎i}i∈I:={δqti​(d​q)​d​t}i∈I\{\bm{\nu}^{i}\}\_{i\in I}:=\{\delta\_{q\_{t}^{i}}(\mathrm{d}q)\mathrm{d}t\}\_{i\in I} is relatively compact w.r.t. 𝒮1​(𝒫1​(E×ℝd))\mathcal{S}\_{1}(\mathcal{P}\_{1}(E\times\mathbb{R}^{d})) and so is their convex hull.

Proof.  According to Proposition [C.6](#A3.Thmtheorem6 "Proposition C.6. ‣ C.1. Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the family of Young measures {𝝂i}i∈I\{\bm{\nu}^{i}\}\_{i\in I} is tight in the sense of Definition [C.5](#A3.Thmtheorem5 "Definition C.5 (Tightness). ‣ C.1. Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") if there exists a compact set 𝔎¯ϵ⊂𝒫1​(E×ℝd)\bar{\mathfrak{K}}\_{\epsilon}\subset\mathcal{P}\_{1}(E\times\mathbb{R}^{d}) for every ϵ>0\epsilon>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | supi∈Iλ​({t∈[0,T]∣qti∈𝒫1​(E×ℝd)∖𝔎¯ϵ})≤ϵ.\sup\_{i\in I}\lambda(\{t\in[0,T]\mid q\_{t}^{i}\in\mathcal{P}\_{1}(E\times\mathbb{R}^{d})\setminus\bar{\mathfrak{K}}\_{\epsilon}\})\leq\epsilon. |  |

Furthermore, by Proposition [C.7](#A3.Thmtheorem7 "Proposition C.7. ‣ C.1. Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") tightness implies relative compactness w.r.t. 𝒮​(𝒫1​(E×ℝd))\mathcal{S}(\mathcal{P}\_{1}(E\times\mathbb{R}^{d})).

To find a compact set 𝔎¯ϵ\bar{\mathfrak{K}}\_{\epsilon} that satisfies condition ([4.1](#S4.E1 "In 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")), we define a subset 𝒬⊂𝒫1​(E)\mathcal{Q}\subset\mathcal{P}\_{1}(E) and parametrized subsets 𝔎​(D)⊂𝒫1​(ℝd)\mathfrak{K}(D)\subset\mathcal{P}\_{1}(\mathbb{R}^{d}) for each D>0D>0 by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒬\displaystyle\mathcal{Q} | :={qx∈𝒫1​(E)|qx≪𝔮x,∫E|d​qxd​𝔮x|1+δ1​d𝔮x≤C1}\displaystyle:=\left\{q^{x}\in\mathcal{P}\_{1}(E)~\middle|~q^{x}\ll\mathfrak{q}^{x},~\int\_{E}\left|\frac{\mathrm{d}q^{x}}{\mathrm{d}\mathfrak{q}^{x}}\right|^{1+\delta\_{1}}\mathrm{d}\mathfrak{q}^{x}\leq C\_{1}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔎​(D)\displaystyle\mathfrak{K}(D) | :={qz∈𝒫1​(ℝd)|∫ℝd|w|​𝟏{|w|>K}​dqz​(w)≤DKδ2​for all​K>0},\displaystyle:=\left\{q^{z}\in\mathcal{P}\_{1}(\mathbb{R}^{d})~\middle|~\int\_{\mathbb{R}^{d}}\left|w\right|\mathbf{1}\_{\{\left|w\right|>K\}}\mathrm{d}q^{z}(w)\leq\frac{D}{K^{\delta\_{2}}}~\text{for all}~K>0\right\}, |  |

and let

|  |  |  |
| --- | --- | --- |
|  | 𝔎¯​(D):={q∈𝒫1​(E×ℝd)∣qx∈𝒬,qz∈𝔎​(D)}.\bar{\mathfrak{K}}(D):=\{q\in\mathcal{P}\_{1}(E\times\mathbb{R}^{d})\mid q^{x}\in\mathcal{Q},~q^{z}\in\mathfrak{K}(D)\}. |  |

Step 1. We first prove that 𝔎¯​(D)⊂𝒫1​(E×ℝd)\bar{\mathfrak{K}}(D)\subset\mathcal{P}\_{1}(E\times\mathbb{R}^{d}) is compact.
Relative compactness follows from Lemma [4.1](#S4.Thmtheorem1 "Lemma 4.1. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") if we can prove that 𝒬\mathcal{Q} and 𝔎​(D)\mathfrak{K}(D) are relatively compact. By Lemma [4.2](#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the set 𝒬\mathcal{Q} is relatively 𝒲1\mathcal{W}\_{1}-compact. Moreover, by definition, the set 𝔎​(D)\mathfrak{K}(D) is tight and uniformly integrable, and hence also relatively 𝒲1\mathcal{W}\_{1}-compact. To see that 𝔎¯​(D)\bar{\mathfrak{K}}(D) is closed, let us take a sequence (qn)n=1∞⊂𝔎¯​(D)(q\_{n})\_{n=1}^{\infty}\subset\bar{\mathfrak{K}}(D) that converges to q∞∈𝒫1​(E×ℝd)q\_{\infty}\in\mathcal{P}\_{1}(E\times\mathbb{R}^{d}). The compactness of 𝒬\mathcal{Q} implies q∞x∈𝒬q\_{\infty}^{x}\in\mathcal{Q} since qnx→q∞xq\_{n}^{x}\to q\_{\infty}^{x} in 𝒫1​(E)\mathcal{P}\_{1}(E). Moreover, by the Portmanteu theorem

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|w|​𝟏{|w|>K}​q∞z​(d​w)≤lim infn→∞∫ℝd|w|​𝟏{|w|>K}​qnz​(d​w)≤DK,\int\_{\mathbb{R}^{d}}\left|w\right|\mathbf{1}\_{\{\left|w\right|>K\}}q\_{\infty}^{z}(\mathrm{d}w)\leq\liminf\_{n\to\infty}\int\_{\mathbb{R}^{d}}\left|w\right|\mathbf{1}\_{\{\left|w\right|>K\}}q\_{n}^{z}(\mathrm{d}w)\leq\frac{D}{\sqrt{K}}, |  |

because the indicator function 𝟏{|w|>K}\mathbf{1}\_{\{\left|w\right|>K\}} is lower semicontinuous. Thus, q∞q\_{\infty} belongs to 𝔎¯​(D)\bar{\mathfrak{K}}(D).

Step 2. Now we prove the tightness of {𝝂i}i∈I\{\bm{\nu}^{i}\}\_{i\in I}. To this end, we fix ϵ>0\epsilon>0 and find a constant Dϵ>0D\_{\epsilon}>0 that satisfies the inequality ([4.1](#S4.E1 "In 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with 𝔎¯ϵ=𝔎¯​(Dϵ)\bar{\mathfrak{K}}\_{\epsilon}=\bar{\mathfrak{K}}(D\_{\epsilon}). For this, we introduce the measurable subsets

|  |  |  |
| --- | --- | --- |
|  | Ei,D:={t∈[0,T]∣qti∉𝔎¯​(D)}⊂[0,T]E\_{i,D}:=\{t\in[0,T]\mid q^{i}\_{t}\notin\bar{\mathfrak{K}}(D)\}\subset[0,T] |  |

in terms of which the inequality ([4.1](#S4.E1 "In 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | supi∈Iλ​(Ei,D)<ϵ.\sup\_{i\in I}\lambda(E\_{i,D})<\epsilon. |  |

If q∈𝒫1​(ℝd)q\in\mathcal{P}\_{1}(\mathbb{R}^{d}) does not belong to 𝔎​(D)\mathfrak{K}(D), then there exists a constant K>0K>0 such that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|w|1+δ2​dq​(w)≥Kδ2​∫ℝd|w|​𝟏{|w|>K}​dq​(w)>D\displaystyle\int\_{\mathbb{R}^{d}}\left|w\right|^{1+\delta\_{2}}\mathrm{d}q(w)\geq K^{\delta\_{2}}\int\_{\mathbb{R}^{d}}\left|w\right|\mathbf{1}\_{\{\left|w\right|>K\}}\mathrm{d}q(w)>D |  |

and so

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | ∫ℝd|w|1+δ2​dqti,z​(w)>Dfor all​t∈Ei,D.\int\_{\mathbb{R}^{d}}\left|w\right|^{1+\delta\_{2}}\mathrm{d}q\_{t}^{i,z}(w)>D\quad\text{for all}~t\in E\_{i,D}. |  |

If for any D>0D>0 there would exist i​(D)∈Ii(D)\in I such that λ​(Ei​(D),D)>ϵ\lambda(E\_{{i(D)},D})>\epsilon, then for any D>0D>0

|  |  |  |  |
| --- | --- | --- | --- |
|  | C2\displaystyle C\_{2} | ≥∫0T∫ℝd|w|1+δ2​qti​(D),z​(d​w)​dt≥∫Ei​(D),D∫ℝd|w|1+δ2​qti​(D),z​(d​w)​dt>ϵ​D,\displaystyle\geq\int\_{0}^{T}\int\_{\mathbb{R}^{d}}\left|w\right|^{1+\delta\_{2}}q\_{t}^{i(D),z}(\mathrm{d}w)\mathrm{d}t\geq\int\_{E\_{{i(D)},D}}\int\_{\mathbb{R}^{d}}\left|w\right|^{1+\delta\_{2}}q\_{t}^{i(D),z}(\mathrm{d}w)\mathrm{d}t>\epsilon D, |  |

which is impossible. Thus, there exists Dϵ>0D\_{\epsilon}>0 for any ϵ>0\epsilon>0 that satisfies ([4.1](#S4.E1 "In 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with 𝔎¯ϵ=𝔎¯​(Dϵ)\bar{\mathfrak{K}}\_{\epsilon}=\bar{\mathfrak{K}}(D\_{\epsilon}).

Step 3.
By Proposition [C.11](#A3.Thmtheorem11 "Proposition C.11. ‣ C.2. Integrable Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), it remains to verify uniform integrability of the set {𝝂i}i∈I\{\bm{\nu}^{i}\}\_{i\in I} i.e.

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | supi∈I∫0T𝒲1​(δ0,qti)​𝟏{𝒲1​(δ0,qti)>K}​dt→0asK→∞.\sup\_{i\in I}\int\_{0}^{T}\mathcal{W}\_{1}(\delta\_{0},q^{i}\_{t})\mathbf{1}\_{\{\mathcal{W}\_{1}(\delta\_{0},q^{i}\_{t})>K\}}\mathrm{d}t\to 0\quad\mbox{as}\quad K\to\infty. |  |

For some constant C>0C>0 that may vary from line to line we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T𝒲1​(δ0,qti)\displaystyle\int\_{0}^{T}\mathcal{W}\_{1}(\delta\_{0},q^{i}\_{t}) | 𝟏{𝒲1​(δ0,qti)>K}​d​t\displaystyle\mathbf{1}\_{\{\mathcal{W}\_{1}(\delta\_{0},q^{i}\_{t})>K\}}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1Kδ2​∫0T𝒲1​(δ0,qti)1+δ2​dt\displaystyle\leq\frac{1}{K^{\delta\_{2}}}\int\_{0}^{T}\mathcal{W}\_{1}(\delta\_{0},q\_{t}^{i})^{1+\delta\_{2}}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤CKδ2​[∫0T∫E‖x‖E1+δ2​qti,x​(d​x)​dt+∫0T∫ℝd|w|1+δ2​qti,z​(d​w)​dt]\displaystyle\leq\frac{C}{K^{\delta\_{2}}}\left[\int\_{0}^{T}\int\_{E}\left\|x\right\|\_{E}^{1+\delta\_{2}}q\_{t}^{i,x}(\mathrm{d}x)\mathrm{d}t+\int\_{0}^{T}\int\_{\mathbb{R}^{d}}\left|w\right|^{1+\delta\_{2}}q\_{t}^{i,z}(\mathrm{d}w)\mathrm{d}t\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤CKδ2​[T​(∫E‖x‖Ep1​(1+δ2)​d𝔮x​(d​x))1p1​(∫E|d​qti,xd​𝔮x|1+δ1​d𝔮x)11+δ1+C2]\displaystyle\leq\frac{C}{K^{\delta\_{2}}}\left[T\left(\int\_{E}\left\|x\right\|\_{E}^{p\_{1}(1+\delta\_{2})}\mathrm{d}\mathfrak{q}^{x}(\mathrm{d}x)\right)^{\frac{1}{p\_{1}}}\left(\int\_{E}\left|\frac{\mathrm{d}q\_{t}^{i,x}}{\mathrm{d}\mathfrak{q}^{x}}\right|^{1+\delta\_{1}}\mathrm{d}\mathfrak{q}^{x}\right)^{\frac{1}{1+\delta\_{1}}}+C\_{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤CKδ2​[T​Mp1​(1+δ2)​(𝔮x)1+δ2​C111+δ1+C2],\displaystyle\leq\frac{C}{K^{\delta\_{2}}}\left[TM\_{p\_{1}(1+\delta\_{2})}(\mathfrak{q}^{x})^{1+\delta\_{2}}C\_{1}^{\frac{1}{1+\delta\_{1}}}+C\_{2}\right], |  |

from which uniform integrability follows. Relative compactness of the convex hull is clear.
□\Box

The following corollary considers the important special case where our integrable Young measures are defined in terms of probability measures with BMO-bounded densities.

###### Corollary 4.4.

Suppose we are given a random variable XX, processes Zn∈ℍBMO2​(ℙ)Z^{n}\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}), measurable functions θn\theta^{n}, and probability measure ℙi∈𝒫​(Ω)\mathbb{P}^{i}\in\mathcal{P}(\Omega) satisfying the assumptions of Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").
Then, the families of probability laws and integrable Young measures,

|  |  |  |
| --- | --- | --- |
|  | {ℒi​(X)}i∈I,{δℒi​(X,Zti)​(d​q)​d​t}i∈Iwhereℒi​(⋅):=ℙi∘(⋅)−1,\{\mathcal{L}^{i}(X)\}\_{i\in I},\quad\big\{\delta\_{\mathcal{L}^{i}(X,Z\_{t}^{i})}(\mathrm{d}q)\mathrm{d}t\big\}\_{i\in I}\quad\text{where}\quad\mathcal{L}^{i}(\cdot):=\mathbb{P}^{i}\circ(\cdot)^{-1}, |  |

are relatively compact w.r.t. the 𝒲1\mathcal{W}\_{1}-topology and 𝒮1​(𝒫1​(E×ℝd))\mathcal{S}\_{1}(\mathcal{P}\_{1}(E\times\mathbb{R}^{d})), respectively.

Proof.  The result follows from Lemma [4.2](#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and Theorem [4.3](#S4.Thmtheorem3 "Theorem 4.3. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") applied to

|  |  |  |
| --- | --- | --- |
|  | 𝔮x:=ℙ∘X−1,qti,x:≡ℙi∘X−1,qti,z:=ℙi∘Zt−1.\mathfrak{q}^{x}:=\mathbb{P}\circ X^{-1},\quad q\_{t}^{i,x}:\equiv\mathbb{P}^{i}\circ X^{-1},\quad q\_{t}^{i,z}:=\mathbb{P}^{i}\circ Z\_{t}^{-1}. |  |

In fact, qti,x≪𝔮xq\_{t}^{i,x}\ll\mathfrak{q}^{x} because ℙi≪ℙ\mathbb{P}^{i}\ll\mathbb{P}.
Moreover, the assumptions of Theorem [4.3](#S4.Thmtheorem3 "Theorem 4.3. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") are satisfied by ([3.8](#S3.E8 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and ([3.10](#S3.E10 "In Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) in Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Stability of quadratic MV-BSDEs ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").
□\Box

## 5. Existence of solutions to generalized MV-BSDE

In this section, we prove our main results, Theorem [2.14](#S2.Thmtheorem14 "Theorem 2.14. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and Theorem [2.16](#S2.Thmtheorem16 "Theorem 2.16. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), and hence the existence of MFG equilibria in weak formulation.

### 5.1. MV-BSDEs with bounded parameters

We first consider the benchmark case where the model parameters are bounded in mean-field terms. To prove Theorem [2.14](#S2.Thmtheorem14 "Theorem 2.14. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") it is enough to show that the solution map ([2.19](#S2.E19 "In 2.3. Our approach ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) has a fixed-point.

Proof of Theorem [2.14](#S2.Thmtheorem14 "Theorem 2.14. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").  
By Corollary [2.20](#S2.Thmtheorem20 "Corollary 2.20. ‣ 2.3. Our approach ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the solution mapping Φ\Phi maps the convex, closed set 𝒬∗×𝒦∗\mathcal{Q}^{\ast}\times\mathcal{K}^{\ast} to itself.
In view of Lemma [4.2](#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), the convex set 𝒬∗⊂𝒫1\mathcal{Q}^{\ast}\subset\mathcal{P}\_{1} is compact. Corollary [4.4](#S4.Thmtheorem4 "Corollary 4.4. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") implies that the convex set 𝒦∗⊂𝒴1\mathcal{K}^{\ast}\subset\mathcal{Y}\_{1} is also compact. It follows from Corollary [3.6](#S3.Thmtheorem6 "Corollary 3.6. ‣ 3.2. Continuity of the solution mapping ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") that Φ\Phi is continuous on 𝒬∗×𝒦∗\mathcal{Q}^{\ast}\times\mathcal{K}^{\ast}. Moreover, as shown in Appendix [C.3](#A3.SS3 "C.3. Embedding the space of integrable Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") the space 𝒫1×𝒴1\mathcal{P}\_{1}\times\mathcal{Y}\_{1} can be embedded into a locally convex Hausdorff topological space. Therefore, Schauder’s fixed-point theorem is applicable to the solution mapping and yields a fixed point

|  |  |  |
| --- | --- | --- |
|  | (μ,𝝂)=(ℒμ,𝝂​(X),δℒμ,𝝂​(X,Ztμ,𝝂)​(d​q)​d​t)∈𝒫1×𝒴1.(\mu,\bm{\nu})=(\mathcal{L}^{\mu,\bm{\nu}}(X),\delta\_{\mathcal{L}^{\mu,\bm{\nu}}(X,Z\_{t}^{\mu,\bm{\nu}})}(\mathrm{d}q)\mathrm{d}t)\in\mathcal{P}\_{1}\times\mathcal{Y}\_{1}. |  |

In particular, ℒμ,𝝂​(X,Z⋅μ,𝝂)∈ℳ1\mathcal{L}^{\mu,\bm{\nu}}(X,Z\_{\cdot}^{\mu,\bm{\nu}})\in\mathcal{M}\_{1}. Since the disintegration ν\nu of 𝝂\bm{\nu} is unique,

|  |  |  |
| --- | --- | --- |
|  | νt=δℒμ,𝝂​(X,Ztμ,𝝂)for a.e. t∈[0,T]\nu\_{t}=\delta\_{\mathcal{L}^{\mu,\bm{\nu}}(X,Z\_{t}^{\mu,\bm{\nu}})}\quad\mbox{for a.e. $t\in[0,T]$} |  |

and the BSDE ([2.17](#S2.E17 "In 2.3. Our approach ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) turns into

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ytμ,𝝂\displaystyle\mathrm{d}Y\_{t}^{\mu,\bm{\nu}} | =−Ht​(X,Ztμ,𝝂,ℒμ,𝝂​(X,Zsμ,𝝂))​d​t+Ztμ,𝝂​d​Wt,YTμ,𝝂=G​(X,ℒμ,𝝂​(X)),\displaystyle=-H\_{t}(X,Z\_{t}^{\mu,\bm{\nu}},\mathcal{L}^{\mu,\bm{\nu}}(X,Z\_{s}^{\mu,\bm{\nu}}))\mathrm{d}t+Z\_{t}^{\mu,\bm{\nu}}\mathrm{d}W\_{t},\quad Y\_{T}^{\mu,\bm{\nu}}=G(X,\mathcal{L}^{\mu,\bm{\nu}}(X)), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙμ,𝝂d​ℙ\displaystyle\frac{\mathrm{d}\mathbb{P}^{\mu,\bm{\nu}}}{\mathrm{d}\mathbb{P}} | =ℰ​(B⋅​(X,Z⋅μ,𝝂,ℒμ,𝝂​(X))⋅W)T.\displaystyle=\mathcal{E}\left(B\_{\cdot}(X,Z\_{\cdot}^{\mu,\bm{\nu}},\mathcal{L}^{\mu,\bm{\nu}}(X))\cdot W\right)\_{T}. |  |

Hence, (X,Yμ,𝝂,Zμ,𝝂,ℙμ,𝝂)(X,Y^{\mu,\bm{\nu}},Z^{\mu,\bm{\nu}},\mathbb{P}^{\mu,\bm{\nu}}) is a solution to the generalized MV-BSDE ([2.12](#S2.E12 "In 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).
□\Box

### 5.2. MV-BSDEs with unbounded parameters

We now extend the previous result to the case of unbounded parameters. We start with a uniform a priori bound on the solutions of our MV-BSDEs. The result is a modification of Theorem 3.8 in Hao et al. [[undefy](#bib.bibx26)].

###### Proposition 5.1.

Under Assumption [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") any solution (X,Y,Z,ℙ¯)∈SS2​(ℙ¯)×SS∞​(ℙ¯)×ℍBMO2​(ℙ¯)×𝒫​(Ω)(X,Y,Z,\bar{\mathbb{P}})\in\SS^{2}(\bar{\mathbb{P}})\times\SS^{\infty}(\bar{\mathbb{P}})\times\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\bar{\mathbb{P}})\times\mathcal{P}(\Omega) to the generalized McKean-Vlasov FBSDE ([2.14](#S2.E14 "In 2.2.5. Generalized MV-BSDEs and MV-FBSDEs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is bounded:

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | ‖X‖SS2​(ℙ¯)≤L¯x,‖Y‖SS∞​(ℙ¯)≤L¯y,‖Z‖ℍBMO2​(ℙ¯)≤L¯z\left\|X\right\|\_{\SS^{2}(\bar{\mathbb{P}})}\leq\bar{L}\_{x},\quad\left\|Y\right\|\_{\SS^{\infty}(\bar{\mathbb{P}})}\leq\bar{L}\_{y},\quad\left\|Z\right\|\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\bar{\mathbb{P}})}\leq\bar{L}\_{z} |  |

for some constants L¯x,L¯y,L¯z\bar{L}\_{x},\bar{L}\_{y},\bar{L}\_{z} that depend only on the constants L,Kσ,K,γ,γ~L,K\_{\sigma},K,\gamma,\tilde{\gamma} given in Assumptions [2.13](#S2.Thmtheorem13 "Assumption 2.13. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").

Proof.  If condition (1a) of Assumption [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") is satisfied, the result follows from Theorem 3.8 in [[undefy](#bib.bibx26)]. In what follows we outline the key arguments under condition (1b).

Step 1.
The dynamics of XX under the probability measure ℙ¯\bar{\mathbb{P}} is given by

|  |  |  |
| --- | --- | --- |
|  | d​Xt=σt​(X)​Bt​(X,Zt,ℒ¯​(X))​d​t+σt​(X)​d​W¯t.\mathrm{d}X\_{t}=\sigma\_{t}(X)B\_{t}(X,Z\_{t},\bar{\mathcal{L}}(X))\mathrm{d}t+\sigma\_{t}(X)\mathrm{d}\bar{W}\_{t}. |  |

We set Xt∗:=sups∈[0,t]|Xs|X\_{t}^{\ast}:=\sup\_{s\in[0,t]}\left|X\_{s}\right|.
From condition (1b) of Assumption [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"), a standard argument using the BDG inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼¯​[|Xs∗|2]\displaystyle\bar{\mathbb{E}}[\left|X\_{s}^{\ast}\right|^{2}] | ≤3​[|x0|2+3​T​γ2​∫0t(1+𝔼¯​[|Xs∗|2]+𝔼¯​[|Zs|2])​ds+4​𝔼¯​[∫0t|σs​(X)|2​ds]]\displaystyle\leq 3\left[\left|x\_{0}\right|^{2}+3T\gamma^{2}\int\_{0}^{t}\left(1+\bar{\mathbb{E}}[\left|X\_{s}^{\ast}\right|^{2}]+\bar{\mathbb{E}}[\left|Z\_{s}\right|^{2}]\right)\mathrm{d}s+4\bar{\mathbb{E}}\left[\int\_{0}^{t}\left|\sigma\_{s}(X)\right|^{2}\mathrm{d}s\right]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(1+∫0t𝔼¯​[|Xs∗|2]​ds+𝔼¯​[∫0t|Zs|2​ds])\displaystyle\leq C\left(1+\int\_{0}^{t}\bar{\mathbb{E}}[\left|X\_{s}^{\ast}\right|^{2}]\mathrm{d}s+\bar{\mathbb{E}}\left[\int\_{0}^{t}\left|Z\_{s}\right|^{2}\mathrm{d}s\right]\right) |  |

for some C>0C>0, and an application of Gronwall’s inequality yields for some L1>0L\_{1}>0

|  |  |  |  |
| --- | --- | --- | --- |
| (5.2) |  | 𝔼¯​[|XT∗|2]≤L1​(1+𝔼¯​[∫0T|Zs|2​ds]).\bar{\mathbb{E}}[\left|X\_{T}^{\ast}\right|^{2}]\leq L\_{1}\left(1+\bar{\mathbb{E}}\left[\int\_{0}^{T}\left|Z\_{s}\right|^{2}\mathrm{d}s\right]\right). |  |

Step 2.
Analogously to the proof of Theorem 3.8 in [[undefy](#bib.bibx26)], we prove that the norms of the solutions are controlled by the expectation of XX as

|  |  |  |  |
| --- | --- | --- | --- |
| (5.3) |  | ‖Y‖SS[t,T]∞​(ℙ¯)≤L2​(1+𝔼¯​[|XT∗|]),𝔼¯​[∫0T|Zs|2​ds]≤L2​(1+𝔼¯​[|XT∗|]),\displaystyle\left\|Y\right\|\_{\SS^{\infty}\_{[t,T]}(\bar{\mathbb{P}})}\leq L\_{2}\left(1+\bar{\mathbb{E}}\left[\left|X\_{T}^{\ast}\right|\right]\right),\quad\bar{\mathbb{E}}\left[\int\_{0}^{T}\left|Z\_{s}\right|^{2}\mathrm{d}s\right]\leq L\_{2}\left(1+\bar{\mathbb{E}}\left[\left|X\_{T}^{\ast}\right|\right]\right), |  |

for some positive constants L2L\_{2}. Let

|  |  |  |
| --- | --- | --- |
|  | Ψt(y):=exp{4Ky+4K∫0t(2K+γ(1+𝔼¯[|Xs∗|]+𝔼¯[|Zs|]))ds}.\Psi\_{t}(y):=\exp\left\{4Ky+4K\int\_{0}^{t}\left(2K+\gamma\left(1+\bar{\mathbb{E}}\left[\left|X\_{s}^{\ast}\right|\right]+\bar{\mathbb{E}}[\left|Z\_{s}\right|]\right)\right)\mathrm{d}s\right\}. |  |

An application of the Itô-Tanaka formula to Ψt​(|Y|t)\Psi\_{t}(\left|Y\right|\_{t}) yields for some C>0C>0 777We refer to [[undefy](#bib.bibx26)] for the detailed computation.

|  |  |  |  |
| --- | --- | --- | --- |
| (5.4) |  | ‖Y‖SS[t,T]∞​(ℙ¯)≤C​(1+𝔼¯​[|XT∗|])+γ​∫tT𝔼¯​[|Zs|]​ds.\begin{split}\left\|Y\right\|\_{\SS^{\infty}\_{[t,T]}(\bar{\mathbb{P}})}\leq C\left(1+\bar{\mathbb{E}}\left[\left|X\_{T}^{\ast}\right|\right]\right)+\gamma\int\_{t}^{T}\bar{\mathbb{E}}[\left|Z\_{s}\right|]\mathrm{d}s.\end{split} |  |

The strictly quadratic growth condition allows us to eliminate the integral of the ZZ-process from the above equation. In fact, by condition ([2](#S2.I6.i2 "item 2 ‣ Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) in Assumption [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"),

|  |  |  |  |
| --- | --- | --- | --- |
| (5.5) |  | γ~∫tT|Zs|2​ds≤YT−Yt+∫tTγ​(1+𝔼¯​[|Xs∗|]+𝔼¯​[|Zs|])​ds−∫tTZs​dW¯s.\begin{split}\tilde{\gamma}&\int\_{t}^{T}\left|Z\_{s}\right|^{2}\mathrm{d}s\leq Y\_{T}-Y\_{t}+\int\_{t}^{T}\gamma\left(1+\bar{\mathbb{E}}\left[\left|X\_{s}^{\ast}\right|\right]+\bar{\mathbb{E}}[\left|Z\_{s}\right|]\right)\mathrm{d}s-\int\_{t}^{T}Z\_{s}\mathrm{d}\bar{W}\_{s}.\end{split} |  |

By Young’s inequality,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.6) |  | γ​∫tT𝔼¯​[|Zs|]​ds≤ϵ​γ~2​∫tT𝔼¯​[|Zs|2]​ds+T​γ22​ϵ​γ~\gamma\int\_{t}^{T}\bar{\mathbb{E}}[\left|Z\_{s}\right|]\mathrm{d}s\leq\frac{\epsilon\tilde{\gamma}}{2}\int\_{t}^{T}\bar{\mathbb{E}}[\left|Z\_{s}\right|^{2}]\mathrm{d}s+\frac{T\gamma^{2}}{2\epsilon\tilde{\gamma}} |  |

for any ϵ>0\epsilon>0. Taking expectations in ([5.5](#S5.E5 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and applying the above inequality with ϵ=1\epsilon=1 yields

|  |  |  |  |
| --- | --- | --- | --- |
| (5.7) |  | γ~2​𝔼¯​[∫tT|Zs|2​ds]≤2​‖Y‖SS[t,T]∞​(ℙ¯)+T​γ22​γ~+T​γ​(1+𝔼¯​[|XT∗|]).\begin{split}\frac{\tilde{\gamma}}{2}\bar{\mathbb{E}}\left[\int\_{t}^{T}\left|Z\_{s}\right|^{2}\mathrm{d}s\right]&\leq 2\left\|Y\right\|\_{\SS^{\infty}\_{[t,T]}(\bar{\mathbb{P}})}+\frac{T\gamma^{2}}{2\tilde{\gamma}}+T\gamma\left(1+\bar{\mathbb{E}}\left[\left|X\_{T}^{\ast}\right|\right]\right).\end{split} |  |

Therefore, the first estimate in ([5.3](#S5.E3 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows by plugging ([5.7](#S5.E7 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) into ([5.6](#S5.E6 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) and then ([5.6](#S5.E6 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) into ([5.4](#S5.E4 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) with sufficiently small ϵ\epsilon.
The second inequality follows from the first one and ([5.7](#S5.E7 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).

Step 3. We are ready to prove the existence of the desired bounds on (X,Y,Z)(X,Y,Z).
Plugging ([5.3](#S5.E3 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) into ([5.2](#S5.E2 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼¯​[|XT∗|2]\displaystyle\bar{\mathbb{E}}[\left|X\_{T}^{\*}\right|^{2}] | ≤L1​(1+L2​(1+𝔼¯​[|XT∗|]))≤C+12​𝔼¯​[|XT∗|2]\displaystyle\leq L\_{1}\big(1+L\_{2}(1+\bar{\mathbb{E}}[\left|X\_{T}^{\ast}\right|])\big)\leq C+\frac{1}{2}\bar{\mathbb{E}}[\left|X\_{T}^{\*}\right|^{2}] |  |

for some C>0C>0.
This result yields the a priori bound for XX in ([5.1](#S5.E1 "In Proposition 5.1. ‣ 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).
The estimate for YY in ([5.1](#S5.E1 "In Proposition 5.1. ‣ 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) follows from that for XX and ([5.3](#S5.E3 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")).
Taking the conditional expectation of ([5.5](#S5.E5 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ~\displaystyle\tilde{\gamma} | 𝔼¯[∫τT|Zs|2ds|ℱτ]≤2∥Y∥SS[t,T]∞​(ℙ¯)+T​γ22​γ~+Tγ(1+𝔼¯[|XT∗|])+γ~2∫0T𝔼¯[|Zs|2]ds\displaystyle\bar{\mathbb{E}}\left[\int\_{\tau}^{T}\left|Z\_{s}\right|^{2}\mathrm{d}s~\middle|~\mathcal{F}\_{\tau}\right]\leq 2\left\|Y\right\|\_{\SS^{\infty}\_{[t,T]}(\bar{\mathbb{P}})}+\frac{T\gamma^{2}}{2\tilde{\gamma}}+T\gamma\left(1+\bar{\mathbb{E}}\left[\left|X\_{T}^{\ast}\right|\right]\right)+\frac{\tilde{\gamma}}{2}\int\_{0}^{T}\bar{\mathbb{E}}[\left|Z\_{s}\right|^{2}]\mathrm{d}s |  |

for any 𝔽\mathbb{F}-stopping time τ≥0\tau\geq 0.
Plugging ([5.3](#S5.E3 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) into the above inequality, we conclude that

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯[∫τT|Zs|2ds|ℱτ]≤C(1+L¯x+L¯y)\displaystyle\bar{\mathbb{E}}\left[\int\_{\tau}^{T}\left|Z\_{s}\right|^{2}\mathrm{d}s~\middle|~\mathcal{F}\_{\tau}\right]\leq C(1+\bar{L}\_{x}+\bar{L}\_{y}) |  |

for some C>0C>0, which yields the desired a priori bound for ZZ.
□\Box

The preceding result allows us to establish the desired existence result using a truncation argument. To this end, we choose continuous cut-off functions cN=(cNx,cNz)c\_{N}=(c\_{N}^{x},c\_{N}^{z}) that satisfy

|  |  |  |  |
| --- | --- | --- | --- |
| (5.8) |  | ‖cN​(x,z)−(x,z)‖≤‖(x,z)‖​𝟏{‖(x,z)‖≥N}and‖cN​(x,z)‖≤N∧‖(x,z)‖,\left\|c\_{N}(x,z)-(x,z)\right\|\leq\left\|(x,z)\right\|\bm{1}\_{\{\left\|(x,z)\right\|\geq N\}}\quad\mbox{and}\quad\left\|c\_{N}(x,z)\right\|\leq N\wedge\left\|(x,z)\right\|, |  |

and define the corresponding truncated functions GN,BN,FNG^{N},B^{N},F^{N}, and HNH^{N} by

|  |  |  |
| --- | --- | --- |
|  | GN​(x,qx):=G​(x,qx∘(cNx)−1),BtN​(x,z,qx):=Bt​(x,z,qx∘(cNx)−1),FtN​(x,z,q):=Ft​(x,z,q∘cN−1),HtN​(x,y,z,q):=FtN​(x,y,z,q)+BtN​(x,z,qx)⋅z\begin{split}G^{N}(x,q^{x})&:=G(x,q^{x}\circ(c\_{N}^{x})^{-1}),\quad B\_{t}^{N}(x,z,q^{x}):=B\_{t}(x,z,q^{x}\circ(c\_{N}^{x})^{-1}),\\ F\_{t}^{N}(x,z,q)&:=F\_{t}(x,z,q\circ c\_{N}^{-1}),\quad H\_{t}^{N}(x,y,z,q):=F\_{t}^{N}(x,y,z,q)+B\_{t}^{N}(x,z,q^{x})\cdot z\end{split} |  |

By Theorem [2.14](#S2.Thmtheorem14 "Theorem 2.14. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") the respective MV-BSDEs admit solutions

|  |  |  |  |
| --- | --- | --- | --- |
| (5.9) |  | (X,YN,ZN,ℙN)∈SS2​(ℙ)×SS∞​(ℙ)×ℍBMO2​(ℙ)×𝒫​(Ω).(X,Y^{N},Z^{N},\mathbb{P}^{N})\in\SS^{2}(\mathbb{P})\times\SS^{\infty}(\mathbb{P})\times\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P})\times\mathcal{P}(\Omega). |  |

The next lemma provides an auxiliary convergence result for the cut-off functions from which we subsequently conclude that the solutions to the “truncated” MV-BSDEs converge to a solution of the original quadratic MV-BSDE.

###### Lemma 5.2.

Let t↦qtNt\mapsto q\_{t}^{N} be 𝒫2​(𝒞d×ℝd)\mathcal{P}\_{2}(\mathcal{C}\_{d}\times\mathbb{R}^{d})-valued Borel measurable maps on [0,T][0,T]. If

|  |  |  |
| --- | --- | --- |
|  | supN∈ℕ∫0T∫𝒞d×ℝd‖(x,z)‖2​dqtN​(x,z)​dt<∞,\sup\_{N\in\mathbb{N}}\int\_{0}^{T}\int\_{\mathcal{C}\_{d}\times\mathbb{R}^{d}}\left\|(x,z)\right\|^{2}\mathrm{d}q\_{t}^{N}(x,z)\mathrm{d}t<\infty, |  |

then any continuous cut-off function cN:𝒞d×ℝd→𝒞d×ℝdc\_{N}:\mathcal{C}\_{d}\times\mathbb{R}^{d}\to\mathcal{C}\_{d}\times\mathbb{R}^{d} that satisfies ([5.8](#S5.E8 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) also satisfies

|  |  |  |
| --- | --- | --- |
|  | ∫0T𝒲1​(qtN∘cN−1,qtN)​dt→0.\int\_{0}^{T}\mathcal{W}\_{1}\big(q\_{t}^{N}\circ c\_{N}^{-1},q\_{t}^{N}\big)\mathrm{d}t\to 0. |  |

Proof.  The assertion follows from ([5.8](#S5.E8 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲1​(qtN∘cN−1,qtN)\displaystyle\mathcal{W}\_{1}(q\_{t}^{N}\circ c\_{N}^{-1},q\_{t}^{N}) | ≤∫𝒞d×ℝd‖cN​(x,z)−(x,z)‖​dqtN​(x,z)≤1N​∫𝒞d×ℝd‖(x,z)‖2​dqtN​(x,z).\displaystyle\leq\int\_{\mathcal{C}\_{d}\times\mathbb{R}^{d}}\left\|c\_{N}(x,z)-(x,z)\right\|\mathrm{d}q\_{t}^{N}(x,z)\leq\frac{1}{N}\int\_{\mathcal{C}\_{d}\times\mathbb{R}^{d}}\left\|(x,z)\right\|^{2}\mathrm{d}q\_{t}^{N}(x,z). |  |

□\Box

Proof of Theorem [2.16](#S2.Thmtheorem16 "Theorem 2.16. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions").
If the original parameters G,BG,B and FF satisfy Assumption [2.15](#S2.Thmtheorem15 "Assumption 2.15. ‣ 2.2.4. Existence of solutions ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") for some constants γ,γF,γ~F\gamma,\gamma\_{F},\tilde{\gamma}\_{F}, then so do GN,BNG^{N},B^{N} and FNF^{N}. As a result, Proposition [5.1](#S5.Thmtheorem1 "Proposition 5.1. ‣ 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") yields uniform bounds L¯x,L¯z>0\bar{L}\_{x},\bar{L}\_{z}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.10) |  | supN∈ℕ‖X‖SS2​(ℙN)≤L¯x,supN∈ℕ‖ZN‖ℍBMO2​(ℙN)≤L¯z\sup\_{N\in\mathbb{N}}\left\|X\right\|\_{\SS^{2}(\mathbb{P}^{N})}\leq\bar{L}\_{x},\quad\sup\_{N\in\mathbb{N}}\left\|Z^{N}\right\|\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P}^{N})}\leq\bar{L}\_{z} |  |

and hence

|  |  |  |  |
| --- | --- | --- | --- |
| (5.11) |  | supN∈ℕ|B⋅N​(X,0,ℒN​(X))|2≤C​(1+L¯x)<∞.\sup\_{N\in\mathbb{N}}\left|B\_{\cdot}^{N}(X,0,\mathcal{L}^{N}(X))\right|^{2}\leq C(1+\bar{L}\_{x})<\infty. |  |

In particular, supN∈ℕ‖B⋅N​(X,Z⋅N,ℒN​(X))‖ℍBMO2​(ℙN)<∞\sup\_{N\in\mathbb{N}}\left\|B\_{\cdot}^{N}(X,Z\_{\cdot}^{N},\mathcal{L}^{N}(X))\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P}^{N})}<\infty. Thus, by Proposition [2.17](#S2.Thmtheorem17 "Proposition 2.17. ‣ 2.2.5. Generalized MV-BSDEs and MV-FBSDEs ‣ 2.2. Generalized McKean-Vlasov BSDEs and MFG Equilibria ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions"),

|  |  |  |
| --- | --- | --- |
|  | supN∈ℕ‖ZN‖ℍBMO2​(ℙ)<∞.\displaystyle\sup\_{N\in\mathbb{N}}\left\|Z^{N}\right\|\_{\mathbb{H}\_{\operatorname{BMO}}^{2}(\mathbb{P})}<\infty. |  |

We now use these a priori estimates to prove the convergence of the solutions to the truncated MV-BSDEs to a solution to the original MV-BSDE along a subsequence. For this, we set

|  |  |  |
| --- | --- | --- |
|  | μN:=ℒN​(X),qtN:=ℒN​(X,ZtN),𝝂N​(d​q,d​t):=δqtN​(d​q)​d​t.\mu^{N}:=\mathcal{L}^{N}(X),\quad q^{N}\_{t}:=\mathcal{L}^{N}(X,Z\_{t}^{N}),\quad\bm{\nu}^{N}(\mathrm{d}q,\mathrm{d}t):=\delta\_{q\_{t}^{N}}(\mathrm{d}q)\mathrm{d}t. |  |

By Corollary [4.4](#S4.Thmtheorem4 "Corollary 4.4. ‣ 4. Compactness in the space of integrable Young measures ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") we may without loss of generality assume that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.12) |  | μN→μ∗∈𝒫1and𝝂N→𝝂∗∈𝒴1.\mu^{N}\to\mu^{\*}\in\mathcal{P}\_{1}\quad\mbox{and}\quad\bm{\nu}^{N}\to\bm{\nu}^{\*}\in\mathcal{Y}\_{1}. |  |

Furthermore, setting q¯tN:=qtN∘cN−1\bar{q}\_{t}^{N}:=q\_{t}^{N}\circ c\_{N}^{-1} Lemma [5.2](#S5.Thmtheorem2 "Lemma 5.2. ‣ 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") yields

|  |  |  |
| --- | --- | --- |
|  | μ¯N:=μN∘(cNx)−1→μ∗and𝝂¯N​(d​q,d​t):=δq¯tN​(d​q)​d​t→𝝂∗.\bar{\mu}^{N}:=\mu^{N}\circ(c\_{N}^{x})^{-1}\to\mu^{\*}\quad\mbox{and}\quad\bar{\bm{\nu}}^{N}(\mathrm{d}q,\mathrm{d}t):=\delta\_{\bar{q}\_{t}^{N}}(\mathrm{d}q)\mathrm{d}t\to\bm{\nu}^{\ast}. |  |

From the definition ([2.19](#S2.E19 "In 2.3. Our approach ‣ 2. Setup and main results ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) of the solution map, we obtain

|  |  |  |
| --- | --- | --- |
|  | Φ​(μ¯N,𝝂¯N)=(μN,𝝂N)→(μ∗,𝝂∗)in𝒫1×𝒴1\Phi(\bar{\mu}^{N},\bar{\bm{\nu}}^{N})=(\mu^{N},\bm{\nu}^{N})\to(\mu^{\ast},\bm{\nu}^{\ast})\quad\text{in}\quad\mathcal{P}\_{1}\times\mathcal{Y}\_{1} |  |

and from Corollary [3.6](#S3.Thmtheorem6 "Corollary 3.6. ‣ 3.2. Continuity of the solution mapping ‣ 3. The solution mapping ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") and ([5.12](#S5.E12 "In 5.2. MV-BSDEs with unbounded parameters ‣ 5. Existence of solutions to generalized MV-BSDE ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) we obtain

|  |  |  |
| --- | --- | --- |
|  | Φ​(μ¯N,𝝂¯N)→Φ​(μ∗,𝝂∗)in𝒫1×𝒴1.\Phi(\bar{\mu}^{N},\bar{\bm{\nu}}^{N})\to\Phi(\mu^{\ast},\bm{\nu}^{\ast})\quad\text{in}\quad\mathcal{P}\_{1}\times\mathcal{Y}\_{1}. |  |

Combining the above two convergences, we conclude that Φ​(μ∗,𝝂∗)=(μ∗,𝝂∗)\Phi(\mu^{\ast},\bm{\nu}^{\ast})=(\mu^{\ast},\bm{\nu}^{\ast}). □\Box

## Appendix A BSDEs with stochastic Lipschitz drivers

In this appendix, we recall/establish an auxiliary comparison principle for a family of BSDEs with stochastic Lipschitz drivers. The result is essentially a corollary [[undefc](#bib.bibx4), Theorem 10]. Specifically, for some index set II and any i∈Ii\in I we consider the BSDEs

|  |  |  |
| --- | --- | --- |
|  | d​Yti=Hti​(ω,Yti,Zti)​d​t+Zti​d​Wt,YTi=ξidY^{i}\_{t}=H^{i}\_{t}(\omega,Y^{i}\_{t},Z^{i}\_{t})dt+Z^{i}\_{t}dW\_{t},\quad Y^{i}\_{T}=\xi^{i} |  |

defined on (Ω,ℱ,(ℱt),ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t}),\mathbb{P}). We assume that the drivers Hti​(ω,y,z)H\_{t}^{i}(\omega,y,z) are 𝔽\mathbb{F}-progressively measurable for all (y,z)∈ℝ×ℝd(y,z)\in\mathbb{R}\times\mathbb{R}^{d} and that the terminal conditions gig^{i} are ℱT\mathcal{F}\_{T}-measurable.

###### Definition A.1 (Comparison principle).

We say that the above family of BSDEs satisfies a comparison principle if, for any two indices i,j∈Ii,j\in I with

|  |  |  |
| --- | --- | --- |
|  | ξi≥ξjℙ​-a.s.andHti​(y,z)≥Htj​(y,z)d​t×d​ℙ​-a.s. for all​(y,z)∈ℝ×ℝd\displaystyle\xi^{i}\geq\xi^{j}\quad\mathbb{P}\text{-a.s.}\quad\mbox{and}\quad H\_{t}^{i}(y,z)\geq H\_{t}^{j}(y,z)\quad\mathrm{d}t\times\mathrm{d}\mathbb{P}\text{-a.s. for all}~(y,z)\in\mathbb{R}\times\mathbb{R}^{d} |  |

the corresponding solutions (Yi,Zi),(Yj,Zj)∈SS2​(ℝ;ℙ)×ℍ2​(ℝd;ℙ)(Y^{i},Z^{i}),(Y^{j},Z^{j})\in\SS^{2}(\mathbb{R};\mathbb{P})\times\mathbb{H}^{2}(\mathbb{R}^{d};\mathbb{P}) satisfy

|  |  |  |
| --- | --- | --- |
|  | Yti≥Ytjfor all​t∈[0,T],ℙ​-a.s.\displaystyle Y\_{t}^{i}\geq Y\_{t}^{j}\quad\text{for all}~t\in[0,T],~\mathbb{P}\text{-a.s.} |  |

###### Proposition A.2.

Suppose that ξi\xi^{i} and HiH^{i} satisfy the following additional conditions ℙ\mathbb{P}-a.s. for any i∈Ii\in I:

1. (1)

   For some α∈(0,1)\alpha\in(0,1) and K∈ℍBMO2​(ℙ)K\in\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{P}) such that K≥1K\geq 1 and 𝔼​[ℰ​(K⋅W)Tq∗]<∞\mathbb{E}\left[\mathcal{E}\left(K\cdot W\right)\_{T}^{q\_{\ast}}\right]<\infty for some q∗>1q\_{\ast}>1, the driver HiH^{i} satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (y−y¯)​(Hti​(y,z)−Hti​(y¯,z))\displaystyle(y-\bar{y})(H\_{t}^{i}(y,z)-H\_{t}^{i}(\bar{y},z)) | ≤Kt2​α​|y−y¯|2,\displaystyle\leq K\_{t}^{2\alpha}\left|y-\bar{y}\right|^{2}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |Hti​(y,z)−Hti​(y,z¯)|\displaystyle\left|H\_{t}^{i}(y,z)-H\_{t}^{i}(y,\bar{z})\right| | ≤Kt​|z−z¯|,for all​y,y¯∈ℝ,z,z¯∈ℝd.\displaystyle\leq K\_{t}\left|z-\bar{z}\right|,\quad\text{for all}~y,\bar{y}\in\mathbb{R},\,z,\bar{z}\in\mathbb{R}^{d}. |  |
2. (2)

   The following integrability condition holds for some constants (that may depend on i∈Ii\in I) p∗>p∗p^{\ast}>p\_{\ast} where p∗>1p\_{\ast}>1 is the Hölder conjugate of q∗q\_{\ast}:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[|ξi|p∗+(∫0T|fs​(X,ms,αs)|​ds)p∗]<∞\mathbb{E}\left[\left|\xi^{i}\right|^{p^{\ast}}+\left(\int\_{0}^{T}\left|f\_{s}(X,m\_{s},\alpha\_{s})\right|\mathrm{d}s\right)^{p^{\ast}}\right]<\infty |  |

Then, the BSDEs with drivers HiH^{i} and terminal conditions gig^{i} admit unique solutions

|  |  |  |
| --- | --- | --- |
|  | (Yi,Zi)∈⋂p<p∗(SSp​(ℙ)×ℍp​(ℙ))(Y^{i},Z^{i})\in\bigcap\_{p<p^{\ast}}(\SS^{p}(\mathbb{P})\times\mathbb{H}^{p}(\mathbb{P})) |  |

and satisfy the comparison principle.

Proof.  The existence and uniqueness of solutions follows from Theorem 10 in [[undefc](#bib.bibx4)]. The comparison principle is standard. Let i,j∈Ii,j\in I with

|  |  |  |
| --- | --- | --- |
|  | ξi≥ξjℙ​-a.s.Hti​(y,z)≥Htj​(y,z)d​t×d​ℙ​-a.s. for all​(y,z)∈ℝ×ℝd.\xi^{i}\geq\xi^{j}\quad\mathbb{P}\text{-a.s.}\quad H\_{t}^{i}(y,z)\geq H\_{t}^{j}(y,z)\quad\mathrm{d}t\times\mathrm{d}\mathbb{P}\text{-a.s. for all}~(y,z)\in\mathbb{R}\times\mathbb{R}^{d}. |  |

Let

|  |  |  |
| --- | --- | --- |
|  | Δ​Yt=Yti−Ytj,Δ​Zt=Zti−Ztj,Δ​Ht​(y,z)=Hti​(y,z)−Htj​(y,z)\Delta Y\_{t}=Y\_{t}^{i}-Y\_{t}^{j},\quad\Delta Z\_{t}=Z\_{t}^{i}-Z\_{t}^{j},\quad\Delta H\_{t}(y,z)=H\_{t}^{i}(y,z)-H\_{t}^{j}(y,z) |  |

and set

|  |  |  |  |
| --- | --- | --- | --- |
|  | δz​Hti\displaystyle\delta\_{z}H\_{t}^{i} | :=Hti​(Yti,Zti)−Hti​(Ytj,Ztj)|Δ​Yt|​𝟏{|Δ​Yt|≠0},\displaystyle:=\frac{H\_{t}^{i}(Y\_{t}^{i},Z\_{t}^{i})-H\_{t}^{i}(Y\_{t}^{j},Z\_{t}^{j})}{\left|\Delta Y\_{t}\right|}\mathbf{1}\_{\{\left|\Delta Y\_{t}\right|\neq 0\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δz​Hti\displaystyle\delta\_{z}H\_{t}^{i} | :=Hti​(Ytj,Zti)−Hti​(Ytj,Ztj)|Δ​Zt|2​𝟏{|Δ​Zt|≠0}​Δ​Zt.\displaystyle:=\frac{H\_{t}^{i}(Y\_{t}^{j},Z\_{t}^{i})-H\_{t}^{i}(Y\_{t}^{j},Z\_{t}^{j})}{\left|\Delta Z\_{t}\right|^{2}}\mathbf{1}\_{\{\left|\Delta Z\_{t}\right|\neq 0\}}\Delta Z\_{t}. |  |

Then, (Δ​Y,Δ​Z)∈SSp​(ℙ)×ℍp​(ℙ)(\Delta Y,\Delta Z)\in\SS^{p}(\mathbb{P})\times\mathbb{H}^{p}(\mathbb{P}) satisfies the linear BSDE

|  |  |  |
| --- | --- | --- |
|  | Δ​Yt=∫tT(δy​Hsi​Δ​Ys+δz​Hsi​Δ​Zs+Δ​Hs​(Ysj,Zsj))​ds+∫tTΔ​Zs​dWs.\Delta Y\_{t}=\int\_{t}^{T}(\delta\_{y}H\_{s}^{i}\Delta Y\_{s}+\delta\_{z}H\_{s}^{i}\Delta Z\_{s}+\Delta H\_{s}(Y\_{s}^{j},Z\_{s}^{j}))\mathrm{d}s+\int\_{t}^{T}\Delta Z\_{s}\mathrm{d}W\_{s}. |  |

Following a similar argument as in the proof of [[undefc](#bib.bibx4), Lemma 7], we obtain that

|  |  |  |
| --- | --- | --- |
|  | etΔYt=𝔼ℙ∗[eTΔξ+∫tTesΔHs(Ysj,Zsj)ds|ℱt],e\_{t}\Delta Y\_{t}=\mathbb{E}^{\mathbb{P}^{\ast}}\left[e\_{T}\Delta\xi+\int\_{t}^{T}e\_{s}\Delta H\_{s}(Y\_{s}^{j},Z\_{s}^{j})\mathrm{d}s~\middle|~\mathcal{F}\_{t}\right], |  |

where et:=exp⁡{∫0tδy​Hsi​ds}e\_{t}:=\exp\big\{\int\_{0}^{t}\delta\_{y}H\_{s}^{i}\mathrm{d}s\big\} and ℙ∗\mathbb{P}^{\ast} is equivalent to ℙ\mathbb{P} with density

|  |  |  |
| --- | --- | --- |
|  | d​ℙ∗d​ℙ=ℰ​(δz​Hi⋅W)T.\frac{\mathrm{d}\mathbb{P}^{\ast}}{\mathrm{d}\mathbb{P}}=\mathcal{E}\left(\delta\_{z}H^{i}\cdot W\right)\_{T}. |  |

The assertion now follows from standard arguments.
□\Box

## Appendix B BMO martingales

This appendix recalls key properties of BMO martingales.888The reader is referred to [[undefag](#bib.bibx34)] for a detailed discussion of BMO martingales. We continue working on our probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) and denote by 𝒯\mathcal{T} the set of all [0,T][0,T]-valued 𝔽\mathbb{F}-stopping times.

###### Definition B.1.

The BMO norm ‖H‖ℍBMO2​(ℝd;ℙ)\left\|H\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{R}^{d};\mathbb{P})} of a process H∈ℍ2​(ℝd;ℙ)H\in\mathbb{H}^{2}(\mathbb{R}^{d};\mathbb{P}) is defined by

|  |  |  |
| --- | --- | --- |
|  | ∥H∥ℍBMO2​(ℝd;ℙ):=supτ∈𝒯∥𝔼ℙ[∫τT|Hs|2ds|ℱτ]∥L∞​(Ω;ℝ;ℙ).\left\|H\right\|\_{\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{R}^{d};\mathbb{P})}:=\sup\_{\tau\in\mathcal{T}}\left\|\mathbb{E}^{\mathbb{P}}\left[\int\_{\tau}^{T}\left|H\_{s}\right|^{2}\mathrm{d}s\;\middle|\;\mathcal{F}\_{\tau}\right]\right\|\_{L^{\infty}(\Omega;\mathbb{R};\mathbb{P})}. |  |

We write ℍBMO2​(ℝd;ℙ)\mathbb{H}^{2}\_{\operatorname{BMO}}(\mathbb{R}^{d};\mathbb{P}) for the set of all processes with finite BMO norm under ℙ\mathbb{P}.

###### Proposition B.2.

([[undefag](#bib.bibx34), Theorem 3.3 and 3.6])
For any M>0M>0, there exist two constants γ1,γ2\gamma\_{1},\gamma\_{2} that only depend on MM such that, for any two processes θ,H∈ℍBMO2​(ℙ)\theta,H\in\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P}) such that ‖θ‖ℍBMO2​(ℙ)≤M\|\theta\|\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P})}\leq M the process HH belongs to ℍBMO2​(ℙθ)\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P}^{\theta}) as well and satisfies

|  |  |  |
| --- | --- | --- |
|  | γ1​‖H‖ℍBMO2​(ℙ)≤‖H‖ℍBMO2​(ℙθ)≤γ2​‖H‖ℍBMO2​(ℙ)whered​ℙθd​ℙ:=ℰ​(θ⋅W)T.\gamma\_{1}\|H\|\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P})}\leq\|H\|\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P}^{\theta})}\leq\gamma\_{2}\|H\|\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P})}\quad\mbox{where}\quad\frac{\mathrm{d}\mathbb{P}^{\theta}}{\mathrm{d}\mathbb{P}}:=\mathcal{E}(\theta\cdot W)\_{T}. |  |

###### Proposition B.3 (Energy inequality).

Every H∈ℍBMO2​(ℙ)H\in\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P}) satisfies the following inequality:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(∫0T|Hs|2​ds)n]≤n!​‖H‖ℍBMO2​(ℙ)2​nfor all​n∈ℕ.\mathbb{E}\left[\left(\int\_{0}^{T}\left|H\_{s}\right|^{2}\mathrm{d}s\right)^{n}\right]\leq n!\|H\|^{2n}\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P})}\quad\text{for all}~n\in\mathbb{N}. |  |

###### Proposition B.4.

([[undefz](#bib.bibx27), Lemma A.2] and [[undefag](#bib.bibx34), Theorem 3.1])
For any M>0M>0, there exist some p∈(1,∞)p\in(1,\infty) and Cp>0C\_{p}>0 that only depends on pp such that every process H∈ℍBMO2​(ℙ)H\in\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P}) with ‖H‖ℍBMO2​(ℙ)≤M\left\|H\right\|\_{\mathbb{H}^{2}\_{{\operatorname{BMO}}}(\mathbb{P})}\leq M satisfies the following for all τ∈𝒯\tau\in\mathcal{T}:

1. (1)

   The following inequality holds:

   |  |  |  |
   | --- | --- | --- |
   |  | ‖𝔼τ​[(ℰ​(H⋅W)τℰ​(H⋅W)T)1p−1]‖L∞​(ℙ)≤Cp,\left\|\mathbb{E}\_{\tau}\left[\left(\frac{\mathcal{E}(H\cdot W)\_{\tau}}{\mathcal{E}(H\cdot W)\_{T}}\right)^{\frac{1}{p-1}}\right]\right\|\_{L^{\infty}(\mathbb{P})}\leq C\_{p}, |  |
2. (2)

   The reverse Hölder inequality holds:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼τℙ​[ℰ​(H⋅W)Tp]≤Cp​ℰ​(H⋅W)τp.\mathbb{E}\_{\tau}^{\mathbb{P}}[\mathcal{E}(H\cdot W)\_{T}^{p}]\leq C\_{p}\mathcal{E}(H\cdot W)\_{\tau}^{p}. |  |

## Appendix C Young measures and stable topologies

This appendix recalls key properties of (integrable) Young measures and the stable topology that we utilize. A detailed discussion of Young measures can be found in [[undefn](#bib.bibx15), [undefq](#bib.bibx18)].

### C.1. Young measures

Throughout, (Ω,𝒜,μ)(\Omega,\mathcal{A},\mu) is a positive measure space, (E,τE)(E,\tau\_{E}) is a Polish space with metic dd, and EE and 𝒫​(E)\mathcal{P}(E) are equipped with their respective Borel σ\sigma-algebra.

###### Definition C.1 (Young measures).

If a positive measure 𝛎\bm{\nu} on Ω×E\Omega\times E satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝝂​(A×E)=μ​(A)for all​A∈𝒜,\bm{\nu}(A\times E)=\mu(A)\quad\text{for all}~A\in\mathcal{A}, |  |

then 𝛎\bm{\nu} is called a Young measure on Ω×E\Omega\times E.
We denote by 𝒴​(Ω×E)\mathcal{Y}(\Omega\times E), or 𝒴​(E)\mathcal{Y}(E) in short, the space of Young measures on Ω×E\Omega\times E.

###### Proposition C.2.

([[undefq](#bib.bibx18), Theorem 3.2 and Remark 3.3] or [[undefn](#bib.bibx15), p.19-20])
For every Young measure 𝛎∈𝒴​(Ω×E)\bm{\nu}\in\mathcal{Y}(\Omega\times E), there exists a measurable map ν⋅:Ω→𝒫​(E)\nu\_{\cdot}:\Omega\to\mathcal{P}(E) such that

|  |  |  |
| --- | --- | --- |
|  | 𝝂​(A×B)=∫Aνω​(B)​dμ​(ω)=∫Ω∫𝒫​(E)𝟏A×B​(ω,q)​νω​(d​q)​μ​(d​ω)\bm{\nu}(A\times B)=\int\_{A}\nu\_{\omega}(B)\mathrm{d}\mu(\omega)=\int\_{\Omega}\int\_{\mathcal{P}(E)}\mathbf{1}\_{A\times B}(\omega,q)\nu\_{\omega}(\mathrm{d}q)\mu(\mathrm{d}\omega) |  |

for any measurable set A⊂ΩA\subset\Omega and B⊂𝒫​(E)B\subset\mathcal{P}(E).
The mapping ν⋅\nu\_{\cdot} is called *disintegration* of the measure 𝛎\bm{\nu} w.r.t. μ\mu. The disintegration is unique in the sense that any two disintegrations ν⋅,ν⋅′\nu\_{\cdot},\nu^{\prime}\_{\cdot} of 𝛎\bm{\nu}, satisfy ν⋅=ν⋅′\nu\_{\cdot}=\nu^{\prime}\_{\cdot} μ\mu-almost everywhere.

###### Definition C.3 (Stable topology).

The stable topology on 𝒴​(E)\mathcal{Y}(E) is the weakest topology for which the map

|  |  |  |  |
| --- | --- | --- | --- |
| (C.1) |  | {𝒴→ℝ,𝝂↦∫Ω×E𝟏A​(ω)​f​(q)​d𝝂​(ω,q)\begin{cases}\mathcal{Y}&\to\mathbb{R},\\ \bm{\nu}&\mapsto\int\_{\Omega\times E}\mathbf{1}\_{A}(\omega)f(q)\mathrm{d}\bm{\nu}(\omega,q)\end{cases} |  |

is continuous for any A∈𝒜A\in\mathcal{A} and any bounded, Lipschitz continuous function f:E→ℝf:E\to\mathbb{R}.999This definition can be justified by Proposition 3.22 in [[undefq](#bib.bibx18)]. The stable topology on 𝒴​(E)\mathcal{Y}(E) is denoted by 𝒮​(E)\mathcal{S}(E).

###### Proposition C.4.

([[undefq](#bib.bibx18), Proposition 3.25])
If 𝒜\mathcal{A} is countably generated, then the topology 𝒮​(E)\mathcal{S}(E) is metrizable.

###### Definition C.5 (Tightness).

A subset 𝒦⊂𝒴​(E)\mathcal{K}\subset\mathcal{Y}(E) is called *tight* if, for any positive value ϵ>0\epsilon>0, there exists a compact set K⊂SK\subset S such that

|  |  |  |
| --- | --- | --- |
|  | sup𝝂∈𝒦𝝂​(Ω×(S∖K))<ϵ.\sup\_{\bm{\nu}\in\mathcal{K}}\bm{\nu}(\Omega\times(S\setminus K))<\epsilon. |  |

###### Proposition C.6.

([[undefq](#bib.bibx18), Proposition 3.54])
Let 𝒰\mathcal{U} be a family of measurable mappings u:Ω→Eu:\Omega\to E, and let

|  |  |  |
| --- | --- | --- |
|  | 𝝂u​(d​ω,d​q):=δuω​(d​q)​μ​(d​ω)foru∈𝒰.\bm{\nu}^{u}(\mathrm{d}\omega,\mathrm{d}q):=\delta\_{u\_{\omega}}(\mathrm{d}q)\mu(\mathrm{d}\omega)\quad\mbox{for}\quad u\in\mathcal{U}. |  |

Then, the family of Young measures (𝛎u)u∈H(\bm{\nu}^{u})\_{u\in H} is tight if and only if, for any ϵ>0\epsilon>0, there exists a compact subset K⊂EK\subset E such that

|  |  |  |
| --- | --- | --- |
|  | supu∈Hμ​(u−1​(E∖K))<ϵ.\sup\_{u\in H}\mu(u^{-1}(E\setminus K))<\epsilon. |  |

###### Proposition C.7.

(The Prokhorov theorem; [[undefq](#bib.bibx18), Theorem 3.59])
A subset ℋ⊂𝒴​(E)\mathcal{H}\subset\mathcal{Y}(E) is relatively compact w.r.t. the stable topology 𝒮​(E)\mathcal{S}(E) if and only if ℋ\mathcal{H} is tight in 𝒴​(E)\mathcal{Y}(E).

### C.2. Integrable Young measures

###### Definition C.8 (Integrable Young measures).

An element 𝛎∈𝒴​(Ω×E)\bm{\nu}\in\mathcal{Y}(\Omega\times E) is called an integrable Young measure if for some q0∈Eq\_{0}\in E

|  |  |  |
| --- | --- | --- |
|  | ∫Ω×Ed​(q0,q)​d𝝂​(ω,q)<∞.\int\_{\Omega\times E}d(q\_{0},q)\mathrm{d}\bm{\nu}(\omega,q)<\infty. |  |

We denote the class of integrable Young measures on Ω×E\Omega\times E by 𝒴1​(Ω×E)\mathcal{Y}\_{1}(\Omega\times E), or 𝒴1​(E)\mathcal{Y}\_{1}(E) for short.

###### Definition C.9 (Stable topology on 𝒴1​(E)\mathcal{Y}\_{1}(E)).

The stable topology 𝒮1​(E)\mathcal{S}\_{1}(E) on 𝒴1​(E)\mathcal{Y}\_{1}(E) is the weakest topology for which the mapping ([C.1](#A3.E1 "In Definition C.3 (Stable topology). ‣ C.1. Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) is continuous for any A∈𝒜A\in\mathcal{A} and any Lipschitz continuous function f:E→ℝf:E\to\mathbb{R}.101010This definition can be justified by Proposition 2.4.1 in [[undefn](#bib.bibx15)].

###### Proposition C.10.

([[undefn](#bib.bibx15), Proposition 2.4.1])
Let {𝛎i}i∈I\{\bm{\nu}^{i}\}\_{i\in I} be a net in 𝒴1​(E)\mathcal{Y}\_{1}(E) and 𝛎∞∈𝒴1​(E)\bm{\nu}^{\infty}\in\mathcal{Y}\_{1}(E). The following conditions are equivalent:

1. (i)

   𝝂i→𝝂∞\bm{\nu}^{i}\to\bm{\nu}^{\infty} in 𝒮1​(E)\mathcal{S}\_{1}(E),
2. (ii)

   𝝂i→𝝂∞\bm{\nu}^{i}\to\bm{\nu}^{\infty} in 𝒮​(E)\mathcal{S}(E) and ∫Ω×Ed​(q0,q)​d𝝂i​(ω,q)→∫Ω×Ed​(q0,q)​d𝝂∞​(ω,q)\int\_{\Omega\times E}d(q\_{0},q)\mathrm{d}\bm{\nu}^{i}(\omega,q)\to\int\_{\Omega\times E}d(q\_{0},q)\mathrm{d}\bm{\nu}^{\infty}(\omega,q) for some q0∈Sq\_{0}\in S,
3. (iii)

   ∫Ω×Eϕ​d𝝂i→∫Ω×Eϕ​d𝝂∞\int\_{\Omega\times E}\phi\mathrm{d}\bm{\nu}^{i}\to\int\_{\Omega\times E}\phi\mathrm{d}\bm{\nu}^{\infty} for any measurable function ϕ:Ω×E→ℝ\phi:\Omega\times E\to\mathbb{R} such that ϕ​(ω,⋅)\phi(\omega,\cdot) is Lipschitz continuous for each ω∈Ω\omega\in\Omega and for some η∈𝕃1​(Ω)\eta\in\mathbb{L}^{1}(\Omega) and q0∈Sq\_{0}\in S,

   |  |  |  |
   | --- | --- | --- |
   |  | |ϕ​(ω,q)|≤K​(η​(ω)+d​(q0,q))ω∈Ω,q∈S.\left|\phi(\omega,q)\right|\leq K(\eta(\omega)+d(q\_{0},q))\quad\omega\in\Omega,q\in S. |  |

###### Proposition C.11.

([[undefn](#bib.bibx15), Proposition 4.1.2])
Let 𝔎⊂𝒴1​(E)\mathfrak{K}\subset\mathcal{Y}\_{1}(E). The following is equivalent:

1. (i)

   the set 𝔎\mathfrak{K} is relatively compact in 𝒮1​(E)\mathcal{S}\_{1}(E),
2. (ii)

   the set 𝔎\mathfrak{K} is relatively compact in 𝒮​(E)\mathcal{S}(E) and uniformly integrable in the sense that

   |  |  |  |
   | --- | --- | --- |
   |  | limK→∞sup𝝂∈𝔎∫Ω×Ed​(q0,q)​𝟏{d​(q0,q)>K}​d𝝂​(ω,q)=0.\lim\_{K\to\infty}\sup\_{\bm{\nu}\in\mathfrak{K}}\int\_{\Omega\times E}d(q\_{0},q)\mathbf{1}\_{\{d(q\_{0},q)>K\}}\mathrm{d}\bm{\nu}(\omega,q)=0. |  |

### C.3. Embedding the space of integrable Young measures

To apply Schauder’s fixed-point theorem ([[undefa](#bib.bibx2), Corollary 17.56]), we need to embed the set 𝒫1×𝒴1\mathcal{P}\_{1}\times\mathcal{Y}\_{1} into a locally convex Hausdorff topological vector space.111111This subtlety has already been highlighted in Carmona and Lacker [[undefl](#bib.bibx13)] in the proof of their Theorem 3.5.
We address the embedding of the set of 𝒴1​([0,T]×E)\mathcal{Y}\_{1}([0,T]\times E) integrable measures equipped with the 𝒮1​(E)\mathcal{S}\_{1}(E)-topology for a general Polish space EE. Our arguments below resemble [[undefa](#bib.bibx2), p.507]. Similar arguments apply to 𝒫1\mathcal{P}\_{1}. Let ℱ\mathcal{F} be the collection of functions

|  |  |  |
| --- | --- | --- |
|  | (t,q)↦𝟏A​(t)​ϕ​(q)(t,q)\mapsto\mathbf{1}\_{A}(t)\phi(q) |  |

for Borel measurable sets A⊂[0,T]A\subset[0,T] and Lipschitz continuous functions ϕ:E→ℝ\phi:E\to\mathbb{R}.
The product space ℝℱ\mathbb{R}^{\mathcal{F}} is the collection of all mappings from ℱ\mathcal{F} to ℝ\mathbb{R}, endowed with the product topology, i.e. the topology of point-wise convergence on ℱ\mathcal{F}. It is well known that ℝℱ\mathbb{R}^{\mathcal{F}} is a locally convex Hausdorff space (c.f. Lemma 5.74 in [[undefa](#bib.bibx2)]).
We now define a linear map ι:𝒴1→ℝℱ\iota:\mathcal{Y}\_{1}\to\mathbb{R}^{\mathcal{F}} by

|  |  |  |
| --- | --- | --- |
|  | ι​(𝝂)​(ϕ¯):=∫0T∫Eϕ¯​d𝝂for each​𝝂∈𝒴1​and​ϕ¯∈ℱ.\iota(\bm{\nu})(\bar{\phi}):=\int\_{0}^{T}\int\_{E}\bar{\phi}\mathrm{d}\bm{\nu}\quad\text{for each}~\bm{\nu}\in\mathcal{Y}\_{1}~\text{and}~\bar{\phi}\in\mathcal{F}. |  |

If we can prove that the above mapping is injective, then the mapping ι:𝒴1→ι​(𝒴1)\iota:\mathcal{Y}\_{1}\to\iota(\mathcal{Y}\_{1}) is homeomorphism
which shows that 𝒴1\mathcal{Y}\_{1} can be embedded into a locally convex Hausdorff space.

To prove that ι\iota is injective we recall the following result on the characterization of weak convergence of probability measures.

###### Lemma C.12.

([[undefn](#bib.bibx15), p.15])
Let EE be a Polish space and let Lip⁡(E)\operatorname{Lip}(E) be the class of real-valued Lipschitz continuous functions on EE. There exists a countable family {ϕn}n∈ℕ⊂Lip⁡(S)\{\phi^{n}\}\_{n\in\mathbb{N}}\subset\operatorname{Lip}(S) of test functions that determines the weak topology on 𝒫​(E)\mathcal{P}(E), that is νi→ν\nu^{i}\to\nu weakly in 𝒫​(S)\mathcal{P}(S) if and only if ∫Sϕn​dνi→∫Sϕn​dν\int\_{S}\phi^{n}\mathrm{d}\nu^{i}\to\int\_{S}\phi^{n}\mathrm{d}\nu for all n∈ℕn\in\mathbb{N}.

Let us take any two Young measures 𝝂,𝝂¯∈𝒴1\bm{\nu},\bar{\bm{\nu}}\in\mathcal{Y}\_{1} with respective disintegrations ν⋅,ν¯⋅\nu\_{\cdot},\bar{\nu}\_{\cdot} such that ι​(𝝂)=ι​(𝝂¯)\iota(\bm{\nu})=\iota(\bar{\bm{\nu}}). Then, for any measurable set A⊂[0,T]A\subset[0,T] and any ϕ∈Lip⁡(E)\phi\in\operatorname{Lip}(E) we have that

|  |  |  |
| --- | --- | --- |
|  | ∫A∫Eϕ​(q)​(νt−ν¯t)​(d​q)​dt=0.\int\_{A}\int\_{E}\phi(q)(\nu\_{t}-\bar{\nu}\_{t})(\mathrm{d}q)\mathrm{d}t=0. |  |

Thus, for each ϕ∈Lip⁡(E)\phi\in\operatorname{Lip}(E) there exists a null set Nϕ⊂[0,T]N\_{\phi}\subset[0,T] such that

|  |  |  |  |
| --- | --- | --- | --- |
| (C.2) |  | ∫Eϕ​dνt=∫Eϕ​dν¯tfor all​t∈Nϕc.\int\_{E}\phi\mathrm{d}\nu\_{t}=\int\_{E}\phi\mathrm{d}\bar{\nu}\_{t}\quad\text{for all}~t\in N\_{\phi}^{c}. |  |

In view of Lemma [C.12](#A3.Thmtheorem12 "Lemma C.12. ‣ C.3. Embedding the space of integrable Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions") this shows that there exists a null set N⊂[0,T]N\subset[0,T] such that

|  |  |  |
| --- | --- | --- |
|  | νt=ν¯tfor allt∉N.\nu\_{t}=\bar{\nu}\_{t}\quad\mbox{for all}\quad t\notin N. |  |

Since the disinteration uniquely determines the Young measures (cf. Proposition [C.2](#A3.Thmtheorem2 "Proposition C.2. ‣ C.1. Young measures ‣ Appendix C Young measures and stable topologies ‣ Mean-Field Games with Unbounded Controls: A Weak Formulation Approach to Global Solutions")) this shows that
𝝂=𝝂¯\bm{\nu}=\bar{\bm{\nu}}
and hence that ι\iota is indeed injective.

## References

* [undef]
  Y. Achdou, F. Camilli and I. Capuzzo-Dolcetta
  “Mean field games: numerical methods”
  In *SIAM Journal on Numerical Analysis* 48, 2010, pp. 1136–1162
* [undefa]
  Charalambos D. Aliprantis and Kim C. Border
  “Infinite dimensional analysis: a hitchhiker’s guide”
  Springer, 2006
* [undefb]
  A. Bensoussan, J. Frehse and P. Yam
  “Mean field games and mean field type control theory”
  Springer, 2013
* [undefc]
  Philippe Briand and Fulvia Confortola
  “BSDEs with stochastic Lipschitz condition and quadratic PDEs in Hilbert spaces”
  In *Stochastic Processes and their Applications* 118.5
  Elsevier, 2008, pp. 818–838
* [undefd]
  Philippe Briand and Ying Hu
  “Quadratic BSDEs with convex generators and unbounded terminal conditions”
  In *Probability Theory and Related Fields* 141
  Springer, 2008, pp. 543–567
* [undefe]
  Rainer Buckdahn, Juan Li, Yanwei Li and Yi Wang
  “A global stochastic maximum principle for mean-field forward-backward stochastic control systems with quadratic generators”
  In *The Annals of Applied Probability* 36.1
  Institute of Mathematical Statistics, 2026, pp. 275–318
* [undeff]
  P. Cardaliaguet and C.-A. Lehalle
  “Mean field game of controls and an application to trade crowding”
  In *Mathematics and Financial Economics* 12, 2018, pp. 335–363
* [undefg]
  P. Cardaliaguet, C.-A. Lehalle and X. Xu
  “Price impact and mean field games of control”
  In *SIAM Journal on Financial Mathematics* 10, 2019, pp. 459–496
* [undefh]
  R. Carmona, J.-P. Fouque and L.-H. Sun
  “Mean field games and systemic risk”
  In *Communications in Mathematical Sciences* 13, 2015, pp. 911–933
* [undefi]
  René Carmona and François Delarue
  “Probabilistic analysis of mean-field games”
  In *SIAM Journal on Control and Optimization* 51.4
  SIAM, 2013, pp. 2705–2734
* [undefj]
  René Carmona and François Delarue
  “Probabilistic theory of mean field games with applications I”
  Springer International Publishing, 2018
* [undefk]
  René Carmona, François Delarue and Daniel Lacker
  “Mean field games with common noise”
  In *The Annals of Probability* 44.6
  Institute of Mathematical Statistics, 2016, pp. 3740–3803
* [undefl]
  René Carmona and Daniel Lacker
  “A probabilistic weak formulation of mean field games and applications”
  In *The Annals of Applied Probability* 25.3, 2015, pp. 1189–1231
* [undefm]
  René Carmona and Peiqi Wang
  “A probabilistic approach to extended finite state mean field games”
  In *Mathematics of Operations Research* 46.2, 2021, pp. 471–502
* [undefn]
  Charles Castaing, Paul Raynaud De Fitte and Michel Valadier
  “Young measures on topological spaces: with applications in control theory and probability theory”
  Springer Science & Business Media, 2004
* [undefo]
  P. Chan and R. Sircar
  “Fracking, renewables, and mean field games”
  In *SIAM Review* 59.3
  SIAM, 2017, pp. 588–615
* [undefp]
  Roxana Dumitrescu, Marcos Leutscher and Peter Tankov
  “Energy transition under scenario uncertainty: a mean-field game of stopping with common noise”
  In *Mathematics and Financial Economics* 18.4, 2024, pp. 233–274
  DOI: [10.1007/s11579-023-00352-w](https://dx.doi.org/10.1007/s11579-023-00352-w)
* [undefq]
  Liviu C Florescu and Christiane Godet-Thobie
  “Young measures and compactness in measure spaces”
  Walter de Gruyter, 2012
* [undefr]
  G. Fu, P. Hager and U. Horst
  “Mean-field liquidation games with market drop-out”
  In *Mathematical Finance* 49.4, 2024, pp. 2356–2384
* [undefs]
  G. Fu, U. Horst and X. Xia
  “Portfolio liquidation games with self exciting order flow”
  In *Mathematical Finance* 30.4, 2022, pp. 1020–1065
* [undeft]
  G. Fu, P. Graewe, U. Horst and A. Popier
  “A mean field game of optimal portfolio liquidation”
  In *Mathematics of Operations Research* 46.4, 2021, pp. 1251–1281
* [undefu]
  Guanxing Fu and Ulrich Horst
  “Mean field games with singular controls”
  In *SIAM Journal on Control and Optimization* 55.6, 2017, pp. 3831–3868
* [undefv]
  Guanxing Fu and Chao Zhou
  “Mean field portfolio games”
  In *Finance and Stochastics* 27.1, 2023, pp. 189–231
  DOI: [10.1007/s00780-022-00492-9](https://dx.doi.org/10.1007/s00780-022-00492-9)
* [undefw]
  P. Graewe, U. Horst and R. Sircar
  “A maximum principle approach to a deterministic mean field game of control with absorption”
  In *SIAM Journal on Control and Optimization* 60.5, 2022, pp. 3173–3190
* [undefx]
  O. Guéant, J.-M. Lasry and P.-L. Lions
  “Mean field games and applications”
  In *Paris–Princeton Lectures on Mathematical Finance 2010*
  Springer, 2011
* [undefy]
  Tao Hao, Ying Hu, Shanjian Tang and Jiaqiang Wen
  “Mean-field backward stochastic differential equations and nonlocal PDEs with quadratic growth”
  In *The Annals of Applied Probability* 35.3
  Institute of Mathematical Statistics, 2025, pp. 2128–2174
* [undefz]
  Martin Herdegen, Johannes Muhle-Karbe and Dylan Possamaı
  “Equilibrium asset pricing with transaction costs”
  In *Finance and Stochastics* 25
  Springer, 2021, pp. 231–275
* [undefaa]
  Hélène Hibon, Ying Hu and Shanjian Tang
  “Mean-field type quadratic BSDEs”
  In *Numerical Algebra, Control and Optimization* 13.3-4, 2023, pp. 392–412
* [undefab]
  Ying Hu, Remi Moreau and Falei Wang
  “Quadratic mean-field reflected BSDEs”
  In *Probability, Uncertainty and Quantitative Risk* 7.3
  Probability, UncertaintyQuantitative Risk, 2022, pp. 169–194
* [undefac]
  M. Huang, P.. Caines and R.. Malhamé
  “Large population LQG problems”
  In *IEEE Transactions on Automatic Control* 52, 2007, pp. 1560–1571
* [undefad]
  Minyi Huang, Roland P. Malhamé and Peter E. Caines
  “Large population stochastic dynamic games: closed-loop McKean-Vlasov systems and the Nash certainty equivalence principle”
  In *Communications in Information & Systems* 6.3
  International Press of Boston, 2006, pp. 221–252
* [undefae]
  Peter Imkeller and Gonçalo Dos Reis
  “Path regularity and explicit convergence rate for BSDE with truncated quadratic growth”
  In *Stochastic Processes and their Applications* 120.3
  Elsevier, 2010, pp. 348–379
* [undefaf]
  Weimin Jiang, Juan Li and Qingmeng Wei
  “General mean-field BSDEs with diagonally quadratic generator in multi-dimension”
  In *Discrete and Continuous Dynamical Systems* 44.10
  DiscreteContinuous Dynamical Systems, 2024, pp. 2957–2984
* [undefag]
  Norihiko Kazamaki
  “Continuous exponential martingales and BMO”
  Springer, 2006
* [undefah]
  Daniel Lacker
  “Mean field games via controlled martingale problems: existence of Markovian equilibria”
  In *Stochastic Processes and their Applications* 125.7, 2015, pp. 2856–2894
* [undefai]
  Daniel Lacker
  “Mean field games via controlled martingale problems: existence of Markovian equilibria”
  In *Stochastic Processes and their Applications* 125.7
  Elsevier, 2015, pp. 2856–2894
* [undefaj]
  Daniel Lacker and Thaleia Zariphopoulou
  “Mean field and N-player games for optimal investment under relative performance criteria”
  In *Mathematical Finance* 29.3, 2019, pp. 1003–1038
* [undefak]
  J.-M. Lasry and P.-L. Lions
  “Jeux à champ moyen I–II”
  In *Comptes Rendus de l’Académie des Sciences de Paris* 343, 2006, pp. 619–625\bibrangessep679–684
* [undefal]
  Jean-Michel Lasry and Pierre-Louis Lions
  “Mean field games”
  In *Japanese Journal of Mathematics* 2.1
  Springer ScienceBusiness Media LLC, 2007, pp. 229–260
  DOI: [10.1007/s11537-007-0657-8](https://dx.doi.org/10.1007/s11537-007-0657-8)
* [undefam]
  James R. Munkres
  “Topology”
  Prentice Hall, 2000
* [undefan]
  Dylan Possamaï and Nizar Talbi
  “Mean-field games of optimal stopping: master equation and weak equilibria”
  In *arXiv preprint*, 2023
  arXiv:[2307.09278 [math.PR]](https://arxiv.org/abs/2307.09278)
* [undefao]
  Dylan Possamaï and Ludovic Tangpi
  “Non-asymptotic convergence rates for mean-field games: weak formulation and McKean-Vlasov BSDEs”
  In *Applied Mathematics & Optimization* 91.3
  Springer, 2025, pp. 58
* [undefap]
  Walter Rudin
  “Functional analysis”
  New York: McGraw-Hill, 1991
* [undefaq]
  Haiyang Wang and Jianfeng Zhang
  “Forward backward SDEs in weak formulation”
  In *Mathematical Control and Related Fields* 8.3&4, 2018, pp. 1021–1049
* [undefar]
  Jianfeng Zhang
  “Backward Stochastic Differential Equations: From Linear to Fully Nonlinear Theory” 86, Probability Theory and Stochastic Modelling
  Springer New York, 2017
  DOI: [10.1007/978-1-4939-7256-2](https://dx.doi.org/10.1007/978-1-4939-7256-2)

BETA