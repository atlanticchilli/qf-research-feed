---
authors:
- Dena Firoozi
- Anastasis Kratsios
- Xuwei Yang
doc_id: arxiv:2510.20017v1
family_id: arxiv:2510.20017
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces:
  The Power of Neural Operators'
url_abs: http://arxiv.org/abs/2510.20017v1
url_html: https://arxiv.org/html/2510.20017v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dena Firoozi

Anastasis Kratsios

Xuwei Yang111Corresponding Author.
Department of Statistical Sciences, University of Toronto (email:dena.firoozi@utoronto.ca).
Department of Mathematics and Statistics, McMaster University, and The Vector Institute (email:kratsioa@mcmaster.ca, henryyangxuwei@gmail.com).

###### Abstract

Traditional mean-field game (MFG) solvers operate on an instance-by-instance basis, which becomes infeasible when many related problems must be solved (e.g., for seeking a robust description of the solution under perturbations of the dynamics or utilities, or in settings involving continuum-parameterized agents.). We overcome this by training neural operators (NOs) to learn the rules-to-equilibrium map from the problem data (“rules”: dynamics and cost functionals) of LQ MFGs defined on separable Hilbert spaces to the corresponding equilibrium strategy. Our main result is a statistical guarantee: an NO trained on a small number of randomly sampled rules reliably solves unseen LQ MFG variants, even in infinite-dimensional settings. The number of NO parameters needed remains controlled under appropriate rule sampling during training.

Our guarantee follows from three results: (i) local-Lipschitz estimates for the highly nonlinear rules-to-equilibrium map; (ii) a universal approximation theorem using NOs with a prespecified Lipschitz regularity (unlike traditional NO results where the NO’s Lipschitz constant can diverge as the approximation error vanishes); and (iii) new sample-complexity bounds for LL-Lipschitz learners in infinite dimensions, directly applicable as the Lipschitz constants of our approximating NOs are controlled in (ii).

###### keywords:

Mean field games, operator learning, Lipschitz neural operators, PAC-Learning.

## 1 Introduction

Many phenomena across the social sciences, such as opinion formation in social networks Bauso et al. [[2016](https://arxiv.org/html/2510.20017v1#bib.bib1)] and price formation in microeconomics and finance Shrivats et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib2)], Gomes and Saúde [[2021](https://arxiv.org/html/2510.20017v1#bib.bib3)], Fujii and Takahashi [[2022](https://arxiv.org/html/2510.20017v1#bib.bib4)], as well as in engineering, epidemiology Laguzet and Turinici [[2015](https://arxiv.org/html/2510.20017v1#bib.bib5)], traffic flow in urban planning Bauso et al. [[2016](https://arxiv.org/html/2510.20017v1#bib.bib6)], ensemble Kalman filtering Del Moral et al. [[2008](https://arxiv.org/html/2510.20017v1#bib.bib7)], Carrillo et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib8)], Ertel [[2025](https://arxiv.org/html/2510.20017v1#bib.bib9)], and deep learning Mei et al. [[2019](https://arxiv.org/html/2510.20017v1#bib.bib10)], are effectively modelled as systems consisting of a large number of interacting, indistinguishable agents, each typically observing only its own state. These systems often involve continuous strategic interaction, where agents compete to optimize their individual objectives. The resulting competitive (game theoretic) equilibria, where each agent acts optimally given the aggregate behaviour of the population, is typically a highly nonlinear function of the problem data, related to the dynamics of the environment and the individual objectives of the agents. Such models fall under the framework of mean field games (MFGs), introduced in Huang et al. [[2006](https://arxiv.org/html/2510.20017v1#bib.bib11)], Lasry and Lions [[2007](https://arxiv.org/html/2510.20017v1#bib.bib12)].
One might expect that certain classes of these games are easily solvable numerically; for example, games where the agent’s behaviour and the objective function are first-order and second-order approximations of the ground truth, respectively–specifically, the linear-quadratic (LQ) MFGs. However, solutions to these games are only partially available in closed form under certain conditions. These solutions, in turn, rely on resolving multi-dimensional, high-dimensional or even infinite-dimensional coupled forward-backward ODEs, depending on the size of the state space dimension. Furthermore, these ODEs themselves depend on the rules of the MFG in a highly nonlinear manner (see e.g. Nguyen and Huang [[2012](https://arxiv.org/html/2510.20017v1#bib.bib13)], Liu and Firoozi [[2025](https://arxiv.org/html/2510.20017v1#bib.bib14)], Federico et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib15)]).

In situations involving model uncertainty, several variations of the rules of an LQ MFG problem typically need to be resolved, each variation of which quantifies a plausible alternative to the rules of the MFG and thus may admit its own plausible equilibrium state. Once each plausible variation on the rules of the game is resolved, then an explicit robust description of the MFG system is possible, typically taking the form of a worst-case or (weighted) average case.
Moreover, to more closely emulate reality, LQ MFG theory has been developed to incorporate several distinct subpopulations of agents. Within each subpopulation, agents share the same rules, which differ from those of other subpopulations. Similarly, the theory has also been extended to accommodate continuum-parametrized agents. In these respective scenarios, several or infinitely many sets of coupled forward-backward ODEs or deterministic evolution equations must be solved to characterize the equilibrium strategies (see e.g. Huang et al. [[2007](https://arxiv.org/html/2510.20017v1#bib.bib16)], Huang [[2010](https://arxiv.org/html/2510.20017v1#bib.bib17)], Nguyen and Huang [[2012](https://arxiv.org/html/2510.20017v1#bib.bib13)]). With these motivation, this paper focuses on tools capable of resolving such infinite systems of LQ MFG equations.

The critical observation is that classical solvers are not viable for resolving infinitely many MFG equations. Examples include finite-difference schemes Briceno-Arias et al. [[2019](https://arxiv.org/html/2510.20017v1#bib.bib18)], semi-Lagrangian schemes Angiuli et al. [[2019](https://arxiv.org/html/2510.20017v1#bib.bib19)], and Newton-type iterative methods Camilli and Tang [[2023](https://arxiv.org/html/2510.20017v1#bib.bib20)]. More recently, deep learning-based approaches have been proposed Fouque and Zhang [[2020](https://arxiv.org/html/2510.20017v1#bib.bib21)], Carmona and Laurière [[2021](https://arxiv.org/html/2510.20017v1#bib.bib22)], Germain et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib23)], Cao et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib24)], Soner et al. [[2025](https://arxiv.org/html/2510.20017v1#bib.bib25)]. However, all of these solvers are designed to address a single MFG instance at a time; thus, they must be re-run from scratch for each variation of the problem under consideration.

To illustrate the limitation, suppose we are solving an LQ MFG on the state space ℝd\mathbb{R}^{d}, and we wish to consider all additive perturbations to the initial condition x∈[0,1]dx\in[0,1]^{d}. This would correspond to an uncountably infinite family of games; clearly, an infeasible computational task. Even if the domain is discretized using a step size 1/S1/S for some S∈ℕ+S\in\mathbb{N}\_{+}, restricting attention to initial states on the grid {(si/S)i=1d}s1,…,sd=0S⊂[0,1]d\{(s\_{i}/S)\_{i=1}^{d}\}\_{s\_{1},\dots,s\_{d}=0}^{S}\subset[0,1]^{d}, we are still left with (S+1)d(S+1)^{d} distinct MFGs to solve. This number grows exponentially with the dimension dd, making the task intractable as SS tends to infinity.
This problem is significantly exacerbated in the setting of infinite-dimensional LQ MFGs studied in Liu and Firoozi [[2025](https://arxiv.org/html/2510.20017v1#bib.bib14)], Federico et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib15)], where the number of solver runs can easily become exponential due to lower bounds on the metric entropy of compact subsets of the space of problem variations in infinite dimensions; see [Lorentz et al., [1996](https://arxiv.org/html/2510.20017v1#bib.bib26), Chapter 15]. Such infinite-dimensional games naturally arise when considering Markovian lifts of Volterra processes on finite-dimensional state spaces with completely monotone Volterra kernels; see, e.g., Cuchiero and Teichmann [[2019](https://arxiv.org/html/2510.20017v1#bib.bib27), [2020](https://arxiv.org/html/2510.20017v1#bib.bib28)], Hamaguchi [[2024](https://arxiv.org/html/2510.20017v1#bib.bib29)]. In short, “game-by-game” solvers are poorly suited to settings involving (infinitely) many variations of the rules defining a given LQ MFG.

Our main contribution proposes a way out of this predicament, not by solving a large set of MFGs but rather by directly learning the solution operator defining the entire family. That is, we design a single solver which yields an (approximate) solution to every relevant LQ MFG simultaneously. At first glance, this may seem unlikely; however, such approaches have recently been successfully deployed in computational physics Wang et al. [[2021](https://arxiv.org/html/2510.20017v1#bib.bib30)], De Ryck and Mishra [[2022](https://arxiv.org/html/2510.20017v1#bib.bib31)], de Hoop et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib32)], Goswami et al. [[2023](https://arxiv.org/html/2510.20017v1#bib.bib33)], Benitez et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib34)], Li et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib35)], Azizzadenesheli et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib36)] and more recently for Stackelberg games Alvarez et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib37)] using infinite-dimensional deep learning models known as Neural Operators (NOs). The commonality threading each of these approaches together is that they attempt to learn a solution operator parameterizing every problem in the (possibly infinite) family of problems. In our case, we wish to learn (not only approximate) the rules-to-equilibrium operator, by which we mean the function mapping the dynamics and objective operators of each agent to their Nash equilibrium strategy, from finite data. Here, the data consists of random pairs comprising rules for the LQ MFG and the corresponding equilibrium strategy. These rules rules details how the drift coefficient, volatility, and objective of each agent are affected by the population’s aggregate behaviour, i.e. the mean field, and the individual agent’s state and control action.

While recent numerical studies provide experimental evidence that NOs offer a promising computation tool in solving MFGs Huang and Lai [[2025](https://arxiv.org/html/2510.20017v1#bib.bib38)], Chen et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib39)], there still remains no theoretical guarantee of their reliability. This work fills that gap by developing a rigorous theory; a fortiori in the infinite-dimensional setting.

##### Contributions

We therefore take a major first step in this direction by showing that a broad range of families of LQ MFGs are approximately solvable from finite training samples when using any training algorithm; that is, we demonstrate the probably approximately correct (PAC) learnability of the rules-to-equilibrium operator using NOs (Theorems [3.3](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem3 "Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and [3.4](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem4 "Theorem 3.4 (Small Empirical Risk Minimizing RNOs Exist). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). Our results additionally quantifies the required number of samples to learn the rules-to-equilibrium map, independently of the training algorithm used to optimize the deep learning model, as well as the distribution by which pairs of rules and equilibria are sampled.
It is worth noting that although our focus in this paper is on infinite-dimensional LQ MFGs, the application of the approximating NOs under study extends beyond this scope. For instance, for robustness purposes or continuum-parameterized cases, they can be effectively used to solve infinitely many finite-dimensional LQ MFGs (Huang et al. [[2007](https://arxiv.org/html/2510.20017v1#bib.bib16)]), finite-dimensional or infinite-dimensional LQ single-agent control problems (Ichikawa [[1979](https://arxiv.org/html/2510.20017v1#bib.bib40)], Tessitore [[1992](https://arxiv.org/html/2510.20017v1#bib.bib41)]), and LQ optimal control problems over large-size networks (Dunyak and Caines [[2024](https://arxiv.org/html/2510.20017v1#bib.bib42)]).

##### Technical Contributions

The derivation of our main result is an interdisciplinary combination of two new results. The first (quantitatively) establishes the stability of the perturbations of infinite-dimensional LQ MFGs; namely, we show the Lipschitz stability of the rules-to-equilibrium operator (Theorem [3.5](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). Additionally, our analysis relies on approximating the sample complexity guarantee (Theorem [3.6](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem6 "Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) when learning LL-Lipschitz (non-linear) operators using LL-Lipschitz neural operators, the analysis of which relies on techniques from optimal transport. These results are the first of their kind and extend their very recent analogues in finite dimensions Hong and Kratsios [[2024](https://arxiv.org/html/2510.20017v1#bib.bib43)], since classical NO learning and approximation guarantees do not control nor leverage the Lipschitz regularity of the NO model itself.

##### Organization of Paper

The rest of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.20017v1#S2 "2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") reviews the necessary background. Section [3](https://arxiv.org/html/2510.20017v1#S3 "3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") presents our main results along with the key technical components and proof strategy. Section [4](https://arxiv.org/html/2510.20017v1#S4 "4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and Section [5](https://arxiv.org/html/2510.20017v1#S5 "5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") contain all proofs. Additional background material is provided in the appendices [A](https://arxiv.org/html/2510.20017v1#A1 "Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and [B](https://arxiv.org/html/2510.20017v1#A2 "Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

## 2 Preliminaries

The interdisciplinary nature of our paper, which combines mean field games with the approximation theory of nonlinear operators (from a deep learning perspective) and elements of statistical learning theory, necessitates a brief overview of each of these concepts to ensure a self-contained reading of our results; which we now do.

### 2.1 Infinite-Dimensional LQ MFGs

Fix T>0T>0 and let 𝒯=def.[0,T]{\mathcal{T}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}[0,T].
We consider a class of LQ MFGs defined on Hilbert spaces over 𝒯\mathcal{T}. Such an MFG may be viewed as the limiting model for an NN-player game as N→∞N\rightarrow\infty, where the state, control, and noise processes associated with each agent take values in infinite-dimensional spaces. These models are naturally suited when an agent’s behavior is impacted by delayed state or control processes, and a Markovian lifting is employed.

Let HH, UU and VV denote separable Hilbert spaces. Moreover, let ℒ​(V,H)\mathcal{L}(V,H) denote the space of all bounded linear operators from VV to HH, which is a Banach space equipped with the norm ‖T‖ℒ​(V,H)=sup‖x‖V=1‖T​x‖H\left\|\mathrm{T}\right\|\_{\mathcal{L}(V,H)}=\sup\_{\left\|x\right\|\_{V}=1}\left\|\mathrm{T}x\right\|\_{H}. The dynamics of a representative agent in a Hilbert space-valued MFG model is governed by a stochastic evolution equation given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x​(t)=(A​x​(t)+B​u​(t)+F1​x¯​(t))​d​t+(D​x​(t)+E​u​(t)+F2​x¯​(t)+σ)​d​W​(t),x​(0)=ξ,\displaystyle\begin{aligned} &dx(t)=\left(Ax(t)+Bu(t)+F\_{1}\bar{x}(t)\right)dt+\left(Dx(t)+Eu(t)+F\_{2}\bar{x}(t)+\sigma\right)dW(t),\\ &x(0)=\xi,\end{aligned} |  | (2.1) |

where ξ∈L2​(Ω;H)\xi\in L^{2}(\Omega;H). In the above equation, x​(t)∈Hx(t)\in H denotes the state and u​(t)∈Uu(t)\in U the control action at time tt of the agent. The control process u={u​(t):t∈𝒯}u=\{u(t):t\in{\mathcal{T}}\} is assumed to be in ℳ2​(𝒯;U)\mathcal{M}^{2}({\mathcal{T}};U), which denotes the Hilbert
space of all U{U}-valued progressively measurable processes uu satisfying
‖u‖ℳ2​(𝒯;U)2=def.𝔼​∫0T‖u​(t)‖U2​𝑑t<∞\left\|u\right\|\_{\mathcal{M}^{2}({\mathcal{T}};U)}^{2}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\mathbb{E}\int\_{0}^{T}\left\|u(t)\right\|^{2}\_{U}dt<\infty. The QQ-Wiener process WW is defined on a filtered probability space (Ω,𝔉,ℱ,ℙ)\left(\Omega,{\mathfrak{F}},\mathcal{F},\mathbb{P}\right) and takes values in VV, where ℱ={ℱt:t∈𝒯}\mathcal{F}=\left\{\mathcal{F}\_{t}:t\in{\mathcal{T}}\right\} is the filtration under which the process WW is a QQ-Wiener process. The process x¯∈C​(𝒯;H)\bar{x}\in C({\mathcal{T}};H) represents the mean field, where C​(𝒯;H)C({\mathcal{T}};H) denotes the set of all continuous mappings h:𝒯→Hh:{\mathcal{T}}\rightarrow H. The mean field represents the aggregate state of the population in the limit as the number of agents N→∞N\rightarrow\infty.
The unbounded linear operator AA, with domain 𝒟​(A)\mathcal{D}(A), is the infinitesimal generator of a C0C\_{0}-semigroup S​(t)∈ℒ​(H),t∈𝒯S(t)\in\mathcal{L}(H),\,t\in{\mathcal{T}}. Moreover, there exists a constant MTM\_{T} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖S​(t)‖ℒ​(H)≤MT,∀t∈𝒯,\left\|S(t)\right\|\_{\mathcal{L}(H)}\leq M\_{T},\quad\forall t\in{\mathcal{T}}, |  | (2.2) |

where MT=def.MA​eα​TM\_{T}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}M\_{A}e^{\alpha T}, with MA≥1M\_{A}\geq 1 and α≥0\alpha\geq 0 Goldstein [[2017](https://arxiv.org/html/2510.20017v1#bib.bib44)]. The choices of MAM\_{A} and α\alpha are independent of TT. Furthermore, B∈ℒ​(U,H)B\in\mathcal{L}(U,H), D∈ℒ​(H,ℒ​(V,H))D\in\mathcal{L}(H,\mathcal{L}(V,H)), E∈ℒ​(U,ℒ​(V,H))E\in\mathcal{L}(U,\mathcal{L}(V,H)), F1∈ℒ​(H)F\_{1}\in\mathcal{L}(H), F2∈ℒ​(H;ℒ​(V;H))F\_{2}\in\mathcal{L}(H;\mathcal{L}(V;H)) and σ∈ℒ​(V;H)\sigma\in\mathcal{L}(V;H).
We focus on the mild solution of ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) which involves the C0C\_{0}-semigroup SS (cf. Liu and Firoozi [[2025](https://arxiv.org/html/2510.20017v1#bib.bib14)]).

###### Assumption 2.1.

The initial condition
ξ∈L2​(Ω;H)\xi\in L^{2}(\Omega;H) is independent of the QQ-Wiener process WW and ℱ0\mathcal{F}\_{0}-measurable. Moreover, 𝔼​[ξ]=ξ¯\mathbb{E}[\xi]=\bar{\xi}.

###### Assumption 2.2.

(Filtration & Admissible Control)
The filtration available to the representative agent is ℱ\mathcal{F}. Subsequently, the set of admissible control laws for the agent, denoted by 𝒰\mathcal{U}, is defined as the collection of ℱ\mathcal{F}-adapted control laws uu that belong to ℳ2​(𝒯;U)\mathcal{M}^{2}({\mathcal{T}};U).

A representative agent seeks a strategy uu to minimize its cost functional

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J​(u)=\displaystyle J(u)= | 𝔼​∫0T[‖M12​(x​(t)−F^1​x¯​(t))‖H2+‖u​(t)‖U2]​𝑑t+𝔼​‖G12​(x​(T)−F^2​x¯​(T))‖H2,\displaystyle\mathbb{E}\int\_{0}^{T}\Big[\big\|M^{\frac{1}{2}}\big(x(t)-\widehat{F}\_{1}\bar{x}(t)\big)\big\|^{2}\_{H}+\|u(t)\|^{2}\_{U}\Big]dt+\mathbb{E}\big\|G^{\frac{1}{2}}\big(x(T)-\widehat{F}\_{2}\bar{x}(T)\big)\big\|^{2}\_{H}, |  | (2.3) |

where MM and GG are positive operators on HH, and M,G,F^1,F^2∈ℒ​(H)M,G,\widehat{F}\_{1},\widehat{F}\_{2}\in\mathcal{L}(H).

An MFG equilibrium strategy for the representative agent is characterized by solving the following two problems.

* (i)

  A stochastic control problem obtained by fixing the mean field process at g∈C​(𝒯;H)g\in C({\mathcal{T}};H). Solving this problem yields the optimal response strategy of the representative agent, denoted by u∘u^{\circ}, to the fixed mean field. The resulting state from this strategy is denoted by x∘x^{\circ}.
* (ii)

  A mean field consistency equation requiring that the resulting mean field, 𝔼​[x∘]\mathbb{E}[x^{\circ}], match the assumed mean field gg, i.e., 𝔼​[x∘​(t)]=g​(t)\mathbb{E}[x^{\circ}(t)]=g(t) for all t∈𝒯t\in\mathcal{T}. The fixed point to this equation characterizes the mean field x¯\bar{x}.

By [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Definition 4.1], for any ℛ∈ℒ​(H)\mathcal{R}\in\mathcal{L}(H) the mappings
Δ1:ℒ​(H)→ℒ​(H;U)\Delta\_{1}:\mathcal{L}(H)\to\mathcal{L}(H;U), Δ2:ℒ​(H)→ℒ​(H)\Delta\_{2}:\mathcal{L}(H)\to\mathcal{L}(H), and
Δ3:ℒ​(H)→ℒ​(U)\Delta\_{3}:\mathcal{L}(H)\to\mathcal{L}(U)
are defined as follows using the Riesz representation theorem

|  |  |  |  |
| --- | --- | --- | --- |
|  | tr⁡((E​u)⋆​ℛ​(D​x)​Q)=⟨Δ1​(ℛ)​x,u⟩,∀x∈H,∀u∈U,tr⁡((D​x)⋆​ℛ​(D​y)​Q)=⟨Δ2​(ℛ)​x,y⟩,∀x,y∈H,tr⁡((E​u)⋆​ℛ​(E​v)​Q)=⟨Δ3​(ℛ)​u,v⟩,∀u,v∈U,\displaystyle\begin{aligned} &\operatorname{tr}((Eu)^{\star}\mathcal{R}(Dx)Q)=\langle\Delta\_{1}(\mathcal{R})x,u\rangle,\quad\forall\,x\in H,\forall\,u\in U,\\ &\operatorname{tr}((Dx)^{\star}\mathcal{R}(Dy)Q)=\langle\Delta\_{2}(\mathcal{R})x,y\rangle,\quad\forall\,x,y\in H,\\ &\operatorname{tr}((Eu)^{\star}\mathcal{R}(Ev)Q)=\langle\Delta\_{3}(\mathcal{R})u,v\rangle,\quad\forall u,v\in U,\end{aligned} |  | (2.4) |

where ∗ is used to denote associated adjoint operators. Furthermore, the mappings
Γ1:ℒ​(H)→H\Gamma\_{1}:\mathcal{L}(H)\to H and Γ2:ℒ​(H)→U\Gamma\_{2}:\mathcal{L}(H)\to U are similarly defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | tr⁡(ℛ​(D​x)​Q)=⟨Γ1​(ℛ),x⟩,∀x∈H,tr⁡(ℛ​(E​u)​Q)=⟨Γ2​(ℛ),u⟩,∀u∈U.\displaystyle\begin{aligned} &\operatorname{tr}(\mathcal{R}(Dx)Q)=\langle\Gamma\_{1}(\mathcal{R}),x\rangle,\quad\forall x\in H,\\ &\operatorname{tr}(\mathcal{R}(Eu)Q)=\langle\Gamma\_{2}(\mathcal{R}),u\rangle,\quad\forall u\in U.\end{aligned} |  | (2.5) |

As demonstrated in [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Theorem 4.9], there exists a unique equilibrium strategy to the LQ MFG ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) in a semi-closed form. Specifically, the expression of this strategy depends on the solution to a set of forward-backward deterministic evolution equations, which includes an infinite-dimensional differential Riccati equation. We recapitulate this result, which we routinely use in our stability analysis, in the supplementary material of our paper (Section [A.1](https://arxiv.org/html/2510.20017v1#A1.SS1 "A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).

#### 2.1.1 Space of Variations on Rules of LQ MFGs

We denote the set of Hilbert-Schmidt operators between two Hilbert spaces H1H\_{1} and H2H\_{2} by ℋ​𝒮​(H1,H2)\mathcal{HS}(H\_{1},H\_{2}) with inner-product ⟨,⟩ℋ​𝒮​(H1,H2)\langle,\rangle\_{\mathcal{HS}(H\_{1},H\_{2})}.

We begin by fixing a reference set of LQ MFG rules (A†,B†,F2†)(A^{\dagger},B^{\dagger},F\_{2}^{\dagger}) satisfying the assumptions of Section [2.1](https://arxiv.org/html/2510.20017v1#S2.SS1 "2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") relative to which we define our space ℋ\mathcal{H} of triples (A,B,F2)(A,B,F\_{2}) of a (possibly) unbounded linear operator A:H→HA:H\to H, and bounded linear operators B:U→HB:U\to H and F2:U→ℋ​𝒮​(V,H)F\_{2}:U\to\mathcal{HS}(V,H) for which the difference operators Δ​A=def.A−A†\Delta A\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}A-A^{\dagger}, Δ​B=def.B−B†\Delta B\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}B-B^{\dagger}, and Δ​F2=def.F2−F2†\Delta F\_{2}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}F\_{2}-F\_{2}^{\dagger} are Hilbert-Schmidt. The elements of ℋ\mathcal{H} constitute variations on rules of the LQ MFG ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). The space ℋ\mathcal{H} can be made into a Hilbert space which is isomorphic (as a Hilbert space) to the direct sum of
ℋ​𝒮​(H)⊕ℋ​𝒮​(U,H)⊕ℋ​𝒮​(U,ℋ​𝒮​(V,H))\mathcal{HS}(H)\oplus\mathcal{HS}(U,H)\oplus\mathcal{HS}\big(U,\mathcal{HS}(V,H)\big) equipped with the inner-product

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(A,B,F2),(A~,B~,F~2)⟩≤⟨Δ​A,Δ​A~⟩ℋ​𝒮​(H)+⟨Δ​B,Δ​B~⟩ℋ​𝒮​(U,H)+⟨Δ​F2,Δ​F~2⟩ℋ​𝒮​(U,ℋ​𝒮​(V,H)),\langle(A,B,F\_{2}),(\tilde{A},\tilde{B},\tilde{F}\_{2})\rangle\leq\langle\Delta A,\Delta\tilde{A}\rangle\_{\mathcal{HS}(H)}+\langle\Delta B,\Delta\tilde{B}\rangle\_{\mathcal{HS}(U,H)}+\langle\Delta F\_{2},\Delta\tilde{F}\_{2}\rangle\_{\mathcal{HS}(U,\mathcal{HS}(V,H))}, |  | (2.6) |

for all triples (A,B,F2),(A~,B~,F~2)∈ℋ(A,B,F\_{2}),(\tilde{A},\tilde{B},\tilde{F}\_{2})\in\mathcal{H}.
An explicit orthogonal basis for ℋ\mathcal{H} is constructed in Appendix [B.4](https://arxiv.org/html/2510.20017v1#A2.E4 "Equation B.4 ‣ B.2 Hilbert-Schmidt Operators Between Different Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), up to identification by the isomorphism (A,B,F2)↦(Δ​A,Δ​B,Δ​F2)(A,B,F\_{2})\mapsto(\Delta A,\Delta B,\Delta F\_{2}). We henceforth denote this orthogonal basis by (ei)i∈ℕ(e\_{i})\_{i\in\mathbb{N}}.

We note that in this paper, we present variations on only three operators (A,B,F2)(A,B,F\_{2}) related to the dynamics ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). However, the analysis may be extended to any operator appearing in the model ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) in a similar manner as the perturbation analysis for these three operators is the most challenging.

#### 2.1.2 Rules-to-Equilibrium Operator

As shown in Liu and Firoozi [[2025](https://arxiv.org/html/2510.20017v1#bib.bib14)], the equilibrium of any such LQ MFG on a Hilbert space must belong to the space ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U)
consisting of all progressively-measurable strategies uu for which the following norm is finite

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖u‖ℳ2​(𝒯,U)2=def.𝔼​[∫0T‖u​(t)‖U2​𝑑t].\|u\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}^{2}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}{\mathbb{E}\biggl[\int\_{0}^{T}\,\|u(t)\|\_{U}^{2}\,dt\biggr]}. |  | (2.7) |

This is a separable Hilbert space, for which elementary tensor product considerations show that it admits an orthogonal basis of the form
(ψn​yj)n∈ℕ,j∈J(\psi\_{n}\,y\_{j})\_{n\in\mathbb{N},\,j\in J}, where {ψn}n∈ℕ\{\psi\_{n}\}\_{n\in\mathbb{N}} enumerates an orthonormal basis of ℳ2​(𝒯,ℝ)\mathcal{M}^{2}({\mathcal{T}},\mathbb{R}); e.g. the Wiener chaos and Haar wavelet-based construction given in [Alvarez et al., [2024](https://arxiv.org/html/2510.20017v1#bib.bib37), Lemma B.6],
and (yj)j∈J(y\_{j})\_{j\in J} enumerates a fixed choice of an orthonormal basis of UU where JJ is a non-empty subset of ℕ\mathbb{N}.
We enumerate and abbreviate these basic vectors as (ηn)n∈ℕ(\eta\_{n})\_{n\in\mathbb{N}} (see Appendix [B.1](https://arxiv.org/html/2510.20017v1#A2.SS1 "B.1 Output Space: Bochner-Lebesgue Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") for further details).
Our objective is to learn the rules-to-equilibrium operator ℜ:ℋ→ℳ2​(𝒯,U)\mathfrak{R}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) from finite random noiseless training data. The rules-to-equilibrium operator thus maps a triple (A,B,F2)∈ℋ(A,B,F\_{2})\in\mathcal{H} to the equilibrium of the LQ MFG it defines; i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℜ​(A,B,F2)=def.equilibrium strategy of the LQ MFG​([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).\mathfrak{R}(A,B,F\_{2})\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\mbox{{equilibrium strategy} of the LQ MFG}~\eqref{dx\_LQ\_MFG}\mbox{-}\eqref{Jinfty}. |  | (2.8) |

Under mild conditions, we prove (Theorem [3.5](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) that this map is well-posed; that is, it not only exists, as was shown in Liu and Firoozi [[2025](https://arxiv.org/html/2510.20017v1#bib.bib14)], but it is also locally Lipschitz continuous and we estimate its local Lipschitz constant.

### 2.2 Statistics in Infinite Dimensions

The sub-Gaussian (resp. Exponential) (Orlicz) norm of a real-valued random variable Z~\tilde{Z} is defined by
‖Z~‖ψi=def.inf{c>0:𝔼​[e(Z~/c)i]≤2}\|\tilde{Z}\|\_{\psi\_{i}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\inf\big\{c>0:\,\mathbb{E}\big[e^{(\tilde{Z}/c)^{i}}\big]\leq 2\big\}, where i=2i=2 (resp. i=1i=1). Our first main technical result (Theorem [3.5](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) shows that ℜ\mathfrak{R} is well-posed; namely, that it exists and that it is LL-Lipschitz continuous on any suitable compact subsets 𝒦\mathcal{K} of ℋ\mathcal{H}; for some L≥0L\geq 0 depending on 𝒦\mathcal{K}.
Now, for any fixed non-empty compact set 𝒦⊆ℋ\mathcal{K}\subseteq\mathcal{H} we consider an LL-Lipschitz extension222An LL-Lipschitz exists by the Benyamini-Lindenstrauss theorem; see e.g. [Benyamini and Lindenstrauss, [2000](https://arxiv.org/html/2510.20017v1#bib.bib45), Theorem 1.12]. ℜ𝒦\mathfrak{R}^{\mathcal{K}}
of ℜ|𝒦\mathfrak{R}|\_{\mathcal{K}} to all of ℋ\mathcal{H}, where ℜ|𝒦\mathfrak{R}|\_{\mathcal{K}} denotes the restriction of the operator
ℜ\mathfrak{R} to the subset 𝒦\mathcal{K}. That is, ℜ𝒦\mathfrak{R}^{\mathcal{K}} is the rules-to-equilibrium operator on 𝒦\mathcal{K}, and it maintains its Lipschitz continuity globally, even outside 𝒦\mathcal{K}.
Consequently, we may meaningfully operate under the following assumptions on the training data consisting of random draws of a set of rules, e.g. Xn=(An,Bn,F2,n)X\_{n}=(A\_{n},B\_{n},F\_{2,n}), in ℋ\mathcal{H} paired with its solution Yn=ℜ𝒦​(Xn)Y\_{n}=\mathfrak{R}^{\mathcal{K}}(X\_{n}) in ℳ2​(𝒯,U)\mathcal{M}^{2}(\mathcal{T},U) to induce the LQ MFG ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).

###### Assumption 2.3 (Data Generating Distribution’s Structure).

Let ℙX\mathbb{P}\_{X} be a centred Borel probability measure on ℋ\mathcal{H}, fix a non-empty compact set 𝒦⊆ℋ\mathcal{K}\subseteq\mathcal{H}, and let ℜ𝒦\mathfrak{R}^{\mathcal{K}} be the LL-Lipschitz extension of ℜ|𝒦\mathfrak{R}|\_{\mathcal{K}} to all of ℋ\mathcal{H}; for some L≥0L\geq 0 (depending on 𝒦\mathcal{K}).
Fix a sample size N∈ℕ+N\in\mathbb{N}\_{+} and let (X1,Y1),…,(XN,YN)(X\_{1},Y\_{1}),\dots,(X\_{N},Y\_{N}) be i.i.d. random variables taking values in ℋ×ℳ2​(𝒯,U)\mathcal{H}\times\mathcal{M}^{2}(\mathcal{T},U)
defined on a probability space (Ω,𝒜,ℙ)(\Omega,\mathcal{A},\mathbb{P})
with

1. (i)

   Sampling Distribution: X1∼⋯∼XN∼ℙXX\_{1}\sim\dots\sim X\_{N}\sim\mathbb{P}\_{X},
2. (ii)

   Realizable Supervised Setting: Yn=ℜ𝒦​(Xn)Y\_{n}=\mathfrak{R}^{\mathcal{K}}(X\_{n}) for each n=1,…,Nn=1,\dots,N.
3. (iii)

   Exponential Karhunen–Loéve decomposition: If X∼ℙXX\sim\mathbb{P}\_{X}, then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | X=∑i=1∞σiZiei,⏟Karhunen–Loéve decomposition​0≤σi≲e−r​i and supj∈ℕ+∥Zj∥ψ2<∞,⏟Rapid decay\underbrace{X=\sum\_{i=1}^{\infty}\,\sigma\_{i}Z\_{i}\,e\_{i},}\_{\text{Karhunen–Lo\'{e}ve decomposition}}\,\,\underbrace{0\leq\sigma\_{i}\lesssim e^{-ri}\mbox{ and }\sup\_{j\in\mathbb{N}\_{+}}\,\|Z\_{j}\|\_{\psi\_{2}}<\infty,}\_{\text{Rapid decay}} |  | (2.9) |

   for all i∈ℕ+i\in\mathbb{N}\_{+}; and decreasing σ1≥σ2≥⋯≥0\sigma\_{1}\geq\sigma\_{2}\geq\dots\geq 0, where (Zi)i∈ℕ+(Z\_{i})\_{i\in\mathbb{N}\_{+}} are independent real-valued random variables, and (ei)i∈ℕ+(e\_{i})\_{i\in\mathbb{N}\_{+}} is the orthonormal basis for ℋ\mathcal{H} fixed in Section [2.1.1](https://arxiv.org/html/2510.20017v1#S2.SS1.SSS1 "2.1.1 Space of Variations on Rules of LQ MFGs ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

###### Example 1 (Centred Gaussian with Diagonal Covariance).

In Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") (iii), if for each i∈ℕ+i\in\mathbb{N}\_{+}, each ZiZ\_{i} is a scalar standard normal random variable, then ℙX\mathbb{P}\_{X} is a centred Gaussian measure on ℋ\mathcal{H} with diagonal covariance operator QQ, diagonalized by σ1≥σ2≥…\sigma\_{1}\geq\sigma\_{2}\geq\dots.
In this case, one may also choose (ei)i∈ℕ(e\_{i})\_{i\in\mathbb{N}} in ℋ\mathcal{H} to be the an eigenbasis of the covariance operator of ℙX\mathbb{P}\_{X}.

### 2.3 Infinite-Dimensional Deep Learning: Neural Operator

The first layer of our neural operators will compress infinite-dimensional inputs into finite-dimensional features, which can be processed by classical deep learning models. As in Galimberti et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib46)], we rely on linear projection operators, defined for each i∈Ii\in I, where II is a non-empty subset of ℕ+\mathbb{N}\_{+}, by Piℋ:ℋ→ℝiP\_{i}^{\mathcal{H}}:\mathcal{H}\to\mathbb{R}^{i} by sending

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Piℋ​(x)\displaystyle P\_{i}^{\mathcal{H}}(x) | =def.(⟨x,ek⟩)k=1i\displaystyle\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\big(\langle x,e\_{k}\rangle\big)\_{k=1}^{i} |  | (2.10) |

for each x∈𝒦x\in\mathcal{K} where ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle denotes the inner-product on ℋ\mathcal{H}
(cf. [B.2](https://arxiv.org/html/2510.20017v1#A2.E2 "Equation B.2 ‣ B.2 Hilbert-Schmidt Operators Between Different Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))
and (ei)i∈I(e\_{i})\_{i\in I} denotes
the orthonormal basis of ℋ\mathcal{H} fixed in Section [2.1.1](https://arxiv.org/html/2510.20017v1#S2.SS1.SSS1 "2.1.1 Space of Variations on Rules of LQ MFGs ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
We will also make use of the embedding operators in ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) defined using a fixed orthonormal basis thereof (ηj)j∈J(\eta\_{j})\_{j\in J} as follows: for each j∈Jj\in J let Ej:ℝj→ℳ2​(𝒯,U)E\_{j}:\mathbb{R}^{j}\to\mathcal{M}^{2}({\mathcal{T}},U) map

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ej​(β)=def.∑1≤k≤jβk​ηk.\displaystyle E\_{j}(\beta)\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\sum\_{1\leq k\leq j}\,\beta\_{k}\,\eta\_{k}. |  | (2.11) |

We consider the following class of residually guided neural operators (RNOs), which includes PCA-net Lanthaler [[2023](https://arxiv.org/html/2510.20017v1#bib.bib47)] and several other neural operator architectures.

###### Definition 2.1 (Residually-Guided Neural Operator (RNO)).

Fix a triple x†=(A,B,F2)x^{\dagger}=(A,B,F\_{2}) as in Section [2.1.1](https://arxiv.org/html/2510.20017v1#S2.SS1.SSS1 "2.1.1 Space of Variations on Rules of LQ MFGs ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), and
ordered bases (ei)i=0∞(e\_{i})\_{i=0}^{\infty} and (ηj)j=0∞(\eta\_{j})\_{j=0}^{\infty} for 𝒳\mathcal{X} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) respectively.
Fix regularity parameters 0<α≤10<\alpha\leq 1 and 0≤L0\leq L,
and a connectivity parameter C∈ℕ+C\in\mathbb{N}\_{+}.
The class of (α,L)(\alpha,L)-regular CC-connected RNOs ℛ​𝒩​𝒪Cα,L​(e⋅,η⋅)\mathcal{RNO}^{\alpha,L}\_{C}(e\_{\cdot},{\eta}\_{\cdot})
consists of all (α,L)(\alpha,L)-Hölder operators f:ℋ→ℳ2​(𝒯,U)f:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U)
with iterative representation mapping any x∈ℋx\in\mathcal{H} to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(x)\displaystyle f(x) | =def.EN2​(AΔ​xΔ+bΔ)+y†\displaystyle\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}E\_{N\_{2}}(A\_{\Delta}x\_{\Delta}+b\_{\Delta})+y^{\dagger}\allowdisplaybreaks |  | (2.12) |
|  | xl+1\displaystyle x\_{l+1} | =def.ReLU⁡(Al​xl+bl), for ​l=0,…,Δ−1\displaystyle\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\operatorname{ReLU}\big(A\_{l}x\_{l}+b\_{l}\big),\,\mbox{ for }l=0,\dots,\Delta-1\allowdisplaybreaks |  |
|  | x0\displaystyle x\_{0} | =def.PN1ℋ​(x+x†)\displaystyle\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}P\_{N\_{1}}^{\mathcal{H}}(x+x^{\dagger}) |  |

for some rank parameters N1,N2∈ℕ+N\_{1},N\_{2}\in\mathbb{N}\_{+}, a depth parameter Δ∈ℕ+\Delta\in\mathbb{N}\_{+},
a width parameter W∈ℕ+W\in\mathbb{N}\_{+}, and hidden weights Al∈ℝdl+1×dlA\_{l}\in\mathbb{R}^{d\_{l+1}\times d\_{l}} and biases
bl∈ℝdl+1b\_{l}\in\mathbb{R}^{d\_{l+1}} for l=0,…,Δl=0,\dots,\Delta; with maxl=0,…,Δ⁡dl≤W\max\_{l=0,\dots,\Delta}\,d\_{l}\leq W satisfying
∑l=0Δ‖Al‖0+‖bl‖0≤C\sum\_{l=0}^{\Delta}\,\|A\_{l}\|\_{0}+\|b\_{l}\|\_{0}\leq C, where ∥.∥0\|.\|\_{0} denotes the count of non-zero entries, EN2E\_{N\_{2}} and PN1ℋP\_{N\_{1}}^{\mathcal{H}} are defined as in ([2.11](https://arxiv.org/html/2510.20017v1#S2.E11 "Equation 2.11 ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and  ([2.10](https://arxiv.org/html/2510.20017v1#S2.E10 "Equation 2.10 ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), respectively,
and x†∈ℋx^{\dagger}\in\mathcal{H} and y†∈ℳ2​(𝒯,U)y^{\dagger}\in\mathcal{M}^{2}({\mathcal{T}},U) denote reference points.

###### Remark 1.

Since the space ℋ\mathcal{H} (cf. Section [2.1.1](https://arxiv.org/html/2510.20017v1#S2.SS1.SSS1 "2.1.1 Space of Variations on Rules of LQ MFGs ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) is defined relative to a reference set of rules x†x^{\dagger}, which by [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Theorem 4.1] corresponds to the unique equilibrium y†=ℛ​(x†)y^{\dagger}=\mathcal{R}(x^{\dagger}), the choice of orthonormal bases e⋅e\_{\cdot} and η⋅\eta\_{\cdot} in the RNO (cf. Definition [2.1](https://arxiv.org/html/2510.20017v1#S2.Thmdefinition1 "Definition 2.1 (Residually-Guided Neural Operator (RNO)). ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) implicitly fixes the reference pair (x†,y†)(x^{\dagger},y^{\dagger}).

In short, our NO architecture, described above, performs perturbations around the reference points (x†,y†)(x^{\dagger},y^{\dagger}).
We close this preliminary section by presenting a simple, fully explicit class of RNO ([2.12](https://arxiv.org/html/2510.20017v1#S2.E12 "Equation 2.12 ‣ Definition 2.1 (Residually-Guided Neural Operator (RNO)). ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) in which the reference rules x†x^{\dagger} of the MFG ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) are set such that the corresponding equilibrium strategy y†y^{\dagger} is explicitly computable.

###### Example 2.

Let aa, ss, mm, bb and gg be positive and finite real numbers, and 𝕀\mathds{I} denote the identity operator defined on the Hilbert space HH. Define A=−a​𝕀A=-a\mathds{I}, B=𝕀B=\mathds{I}, F1=a​𝕀F\_{1}=a\mathds{I}, σ=s​𝕀\sigma=s\mathds{I}, M=m​𝕀M=m\mathds{I}, F^1=b​𝕀\hat{F}\_{1}=b\,\mathds{I}, G=g​𝕀G=g\mathds{I}, F^2=b​𝕀\hat{F}\_{2}=b\,\mathds{I}, and the operators D,ED,E and F2F\_{2} to be zero operators for the MFG model ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). Then, the optimal strategy is given by u∘​(t)=Π​(t)​(x​(t)−ξ¯)u^{\circ}(t)=\Pi(t)(x(t)-\bar{\xi}), where Π​(t)=π​(t)​𝕀\Pi(t)=\pi(t)\mathds{I} with

|  |  |  |
| --- | --- | --- |
|  | πt=c1​r1​er1​t+c2​r2​er2​tc1​er1​t+c2​er2​t\displaystyle\pi\_{t}=\frac{c\_{1}r\_{1}e^{r\_{1}t}+c\_{2}r\_{2}e^{r\_{2}t}}{c\_{1}e^{r\_{1}t}+c\_{2}e^{r\_{2}t}} |  |
|  |  |  |
| --- | --- | --- |
|  | r1,r2=a±a2−m\displaystyle r\_{1},r\_{2}=a\pm\sqrt{a^{2}-m} |  |

for some real-valued constants c1c\_{1} and c2c\_{2}, and ξ¯=𝔼​[x​(0)]\bar{\xi}=\mathbb{E}[x(0)]. Here x†=def.(−a​𝕀,𝕀,0)x^{\dagger}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}(-a\mathds{I},\mathds{I},0) and y†=def.u∘y^{\dagger}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}u^{\circ}
in ([2.12](https://arxiv.org/html/2510.20017v1#S2.E12 "Equation 2.12 ‣ Definition 2.1 (Residually-Guided Neural Operator (RNO)). ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).

## 3 Main Results

Before addressing the approximability of the rules-to-equilibrium operator ℜ\mathfrak{R}, as defined in ([2.8](https://arxiv.org/html/2510.20017v1#S2.E8 "Equation 2.8 ‣ 2.1.2 Rules-to-Equilibrium Operator ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we first establish its well-posedness. Specifically, we show that ℜ\mathfrak{R} is well-defined and locally Lipschitz continuous.

In what follows we fix a priori radii ρA,ρB\rho\_{A},\rho\_{B}, ρF2>0\rho\_{F\_{2}}>0 determining the maximal allowable perturbations on the rules of the MFG, relative to a set of reference rules (A†,B†,F2†)(A^{\dagger},B^{\dagger},F\_{2}^{\dagger}). The set of all such perturbations is quantified by
the ellipsoid

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔹ℋ​(ρA,ρB,ρF2)=def.{‖Δ​A‖ℋ​𝒮​(U)≤ρA,‖Δ​B‖ℋ​𝒮​(U,H)≤ρB,‖Δ​F2‖ℋ​𝒮​(U,ℋ​𝒮​(V,H))≤ρF2}.\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}})\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\big\{\|\Delta A\|\_{\mathcal{HS}(U)}\leq\rho\_{A}\,,\|\Delta B\|\_{\mathcal{HS}(U,H)}\leq\rho\_{B},\,\|\Delta F\_{2}\|\_{\mathcal{HS}(U,\mathcal{HS}(V,H))}\leq\rho\_{F\_{2}}\big\}. |  | (3.1) |

This result follows directly from our main technical stability estimate, stated in Theorem [3.5](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") below, relative to the reference rules (A†,B†,F2†)(A^{\dagger},B^{\dagger},F\_{2}^{\dagger}) and within the ellipsoid 𝔹ℋ​(ρA,ρB,ρF2)\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}) in ℋ\mathcal{H}.

###### Proposition 3.1 (Local Well-Posedness of the Rules-to-Equilibrium Operator).

Fix a reference model (A†,B†,F2†)(A^{\dagger},B^{\dagger},F\_{2}^{\dagger}) and radii ρA,ρB,ρF2>0\rho\_{A},\rho\_{B},\rho\_{F\_{2}}>0.
There exists a time T⋆>0T^{\star}>0, depending only on the radii (ρA,ρB,ρF2)(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}) and on the C0C\_{0}-semi-group of A†A^{\dagger}, such that
the operator ℜ\mathfrak{R} is well-defined and, for every (A,B,F2),(A~,B~,F~2)(A,B,F\_{2}),(\tilde{A},\tilde{B},\tilde{F}\_{2}) in 𝔹ℋ​(ρA,ρB,ρF2)\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}), ℜ\mathfrak{R} satisfies

|  |  |  |
| --- | --- | --- |
|  | ‖ℜ​(A,B,F2)−ℜ​(A~,B~,F~2)‖ℳ2​(𝒯,U)≤L​‖(A,B,F2)−(A~,B~,F~2)‖ℋ\displaystyle\big\|\mathfrak{R}(A,B,F\_{2})-\mathfrak{R}(\tilde{A},\tilde{B},\tilde{F}\_{2})\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\,L\,\big\|(A,B,F\_{2})-(\tilde{A},\tilde{B},\tilde{F}\_{2})\big\|\_{\mathcal{H}} |  |

where the Lipschitz constant L>0L>0 depends only333An explicit dependence of LL on 𝔹ℋ​(ρA,ρB,ρF2)\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}) is given through its relationship to the constants CA,A†u,CB,B†u,1,CB,B†u,2,CF2,F2†u>0C^{u}\_{A,A^{\dagger}},C^{u,1}\_{B,B^{\dagger}},C^{u,2}\_{B,B^{\dagger}},C^{u}\_{F\_{2},F\_{2}^{\dagger}}>0 as precisely shown in the stability estimate of Theorem [3.5](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"). on the ellipsoid 𝔹ℋ​(ρA,ρB,ρF2)\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}).

Rigorously speaking, our results concern a regularized version of the rules-to-equilibrium map ([2.8](https://arxiv.org/html/2510.20017v1#S2.E8 "Equation 2.8 ‣ 2.1.2 Rules-to-Equilibrium Operator ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), whose existence and extension properties are now established.

###### Proposition 3.2 (Global Lipschitzness of the Regularized Rules-to-equilibrium Map).

In the setting of Proposition [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem1 "Proposition 3.1 (Local Well-Posedness of the Rules-to-Equilibrium Operator). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"):
For every compact subset 𝒦⊆𝔹ℋ​(ρA,ρB,ρF2)\mathcal{K}\subseteq\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}), there is an L𝒦≥0L\_{\mathcal{K}}\geq 0, depending only on 𝔹ℋ​(ρA,ρB,ρF2)\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}), and an L𝒦L\_{\mathcal{K}}-Lipschitz extension ℜ𝒦:ℋ→ℳ2​(𝒯,U)\mathfrak{R}^{\mathcal{K}}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) of ℜ|𝒦\mathfrak{R}|\_{\mathcal{K}} to all of ℋ\mathcal{H}. That is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℜ𝒦​(A,B,F2)=ℜ​(A,B,F2),for each ​(A,B,F2)∈𝒦.\mathfrak{R}^{\mathcal{K}}(A,B,F\_{2})=\mathfrak{R}(A,B,F\_{2}),\qquad\text{for each }(A,B,F\_{2})\in\mathcal{K}. |  | (3.2) |

We refer to any map ℜ𝒦\mathfrak{R}^{\mathcal{K}} given by Proposition [3.2](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem2 "Proposition 3.2 (Global Lipschitzness of the Regularized Rules-to-equilibrium Map). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") as the regularized-rules-to-equilibirum map. This map is an extension of the rules-to-equilibrium map ℜ\mathfrak{R} beyond any a-priori prescribed compact set 𝒦\mathcal{K} which has the additional property that it is globally Lipschitz, seemingly unlike the rules-to-equilibrium map; thus, ℜ𝒦\mathfrak{R}^{\mathcal{K}} effectively regularizes ℜ\mathfrak{R} using the geometry of 𝒦\mathcal{K}. Our theory is constructed relative to this extension.

###### Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs).

Fix a reference model (A†,B†,F2†)(A^{\dagger},B^{\dagger},F\_{2}^{\dagger}) and radii ρA,ρB,ρF2>0\rho\_{A},\rho\_{B},\rho\_{F\_{2}}>0 and suppose that Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") holds.
There exists a time T⋆>0T^{\star}>0, depending only on the radii (ρA,ρB,ρF2)(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}) and on the C0C\_{0}-semi-group of A†A^{\dagger}
and there is a compact subset 𝒦⊆𝔹ℋ​(ρA,ρB,ρF2)\mathcal{K}\subseteq\mathbb{B}\_{\mathcal{H}}(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}) of positive ℙX\mathbb{P}\_{X}-measure
and an r>0r>0, depending only on 𝒦\mathcal{K},
such that: For every “approximation error” ε>0\varepsilon>0, and each “failure probability” 0<δ≤10<\delta\leq 1 there is a connectivity parameter C>0C>0, depending on ε,δ\varepsilon,\delta and on 𝒦\mathcal{K}, such that if F^∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)\hat{F}\in\mathcal{RNO}^{1,L}\_{C}(e\_{\cdot},\eta\_{\cdot}) (i.e. α=1\alpha=1)
is empirical risk minimizer; i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1N​∑n=1N‖F^​(Xn)−ℜ𝒦​(Xn)‖ℳ2​(𝒯,U)=infF~∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)1N​∑n=1N‖F~​(Xn)−ℜ𝒦​(Xn)‖ℳ2​(𝒯,U)\frac{1}{N}\sum\_{n=1}^{N}\,\|\hat{F}(X\_{n})-\mathfrak{R}^{\mathcal{K}}(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}=\inf\_{\tilde{F}\in\mathcal{RNO}^{1,L}\_{C}(e\_{\cdot},\eta\_{\cdot})}\,\frac{1}{N}\sum\_{n=1}^{N}\,\|\tilde{F}(X\_{n})-\mathfrak{R}^{\mathcal{K}}(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} |  | (ERM) |

then, F^\hat{F} must satisfy the following PAC-learnability guarantee

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝔼X∼ℙX​[‖F^​(X)−ℜ𝒦​(X)‖ℳ2​(𝒯,U)]≤ε+L¯​e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N)≥𝒫X​(𝒦)N−δ\begin{aligned} {\mathbb{P}}\Biggl(\mathbb{E}\_{X\sim\mathbb{P}\_{X}}\big[\|\hat{F}(X)-\mathfrak{R}^{\mathcal{K}}(X)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\big]\leq\varepsilon+\bar{L}e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}\Biggr)\geq\mathcal{P}\_{X}(\mathcal{K})^{N}-\delta\end{aligned} |  |

where L¯=def.2​max⁡{L𝒦,1}\bar{L}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}2\max\{L\_{\mathcal{K}},1\} and 𝒦\mathcal{K} is as in Proposition [3.2](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem2 "Proposition 3.2 (Global Lipschitzness of the Regularized Rules-to-equilibrium Map). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

Theorem [3.3](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem3 "Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") establishes that regularized rules-to-equilibrium maps are PAC learnable by an RNO F^\hat{F}, provided that F^\hat{F} is an empirical risk minimizer—i.e., it satisfies condition ([ERM](https://arxiv.org/html/2510.20017v1#S3.Ex2 "Equation ERM ‣ Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). The following result extends this finding by not only guaranteeing the existence of such an RNO F^\hat{F} (i.e., that the left-hand side of ([ERM](https://arxiv.org/html/2510.20017v1#S3.Ex2 "Equation ERM ‣ Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) is realizable by some RNO F^\hat{F}), but also showing that such an F^\hat{F} can be chosen to have a surprisingly small number of non-zero (trainable) parameters.
In what follows, we use W0W\_{0} to denote the principal branch of the Lambert WW function444The principal branch W0W\_{0} of the Lambert WW function is the solution of W​eW=zWe^{W}=z that is real-valued for z≥−1/ez\geq-1/e and satisfies W0​(0)=0W\_{0}(0)=0.
.

###### Theorem 3.4 (Small Empirical Risk Minimizing RNOs Exist).

In the setting of Theorem [3.3](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem3 "Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), there exists an RNO F^\hat{F} satisfying ([ERM](https://arxiv.org/html/2510.20017v1#S3.Ex2 "Equation ERM ‣ Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) which has depth 𝒪​(1)\mathcal{O}(1) and both the width WW and the connectivity CC of F^\hat{F} are in the order of 𝒪​(log⁡(ε−1)/εcr)\mathcal{O}\big(\log(\varepsilon^{-1})/\sqrt[c\_{r}]{\varepsilon}\big); where cr=def.⌈log⁡(4​Lrrr)⌉c\_{r}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\Big\lceil\log\big(\tfrac{\sqrt[r]{4L}}{\sqrt[r]{r}}\big)\Big\rceil.

We now examine our main results by situating them within the supporting theoretical framework on which they rely. Our proofs will merge elements of dynamic game-theory, via estimates related to the stability analysis of LQ MFG with respect to its coefficients, with approximation and PAC-learning results for operator learning.

### 3.1 Explanation of Proofs via Supporting Results

The joint proofs of Theorems [3.3](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem3 "Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and [3.4](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem4 "Theorem 3.4 (Small Empirical Risk Minimizing RNOs Exist). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") will be undertaken in two overall steps. All technical details are relegated to Sections [4](https://arxiv.org/html/2510.20017v1#S4 "4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and [5](https://arxiv.org/html/2510.20017v1#S5 "5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
First, we will prove that the rules-to-equilibrium map ℜ\mathfrak{R} is well-posed by establishing the local Lipschitz dependence of the equilibrium strategy of each LQ MFG given by ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) on the rules (A,B,F2)(A,B,F\_{2}). Our stability, i.e. local-Lipschitz, estimates will allow for a more general setting than is treatable in Theorem [3.3](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem3 "Theorem 3.3 (Regularized Rules-to-Equilibria Operators are PAC-Learnable by RNOs). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and will quantify the stability in terms of the operator and supremum norms. Specifically, in this section, we consider more general operator spaces–namely, the space of bounded linear operators–and a general Lipschitz continuous function
ff, instead of the rules-to-equilibrium operator ℜ\mathfrak{R}.

In the remainder of the paper, we denote C​(𝒯;H)C({\mathcal{T}};H) as the set of all continuous mappings h:𝒯→Hh:{\mathcal{T}}\rightarrow H, a Banach space equipped with the supremum norm denoted by ∥.∥C​(𝒯;H)\|.\|\_{C(\mathcal{T};H)}. Moreover, we denote ℋ2​(𝒯;𝒳)\mathcal{H}^{2}({\mathcal{T}};\mathcal{X}) as the Hilbert
space of all 𝒳\mathcal{X}-valued progressively measurable processes xx, equipped with the norm
‖x‖ℋ2​(𝒯;𝒳)=(supt∈𝒯𝔼​‖x​(t)‖𝒳2)12\left\|x\right\|\_{\mathcal{H}^{2}({\mathcal{T}};\mathcal{X})}=\Big(\displaystyle\sup\_{t\in{\mathcal{T}}}\mathbb{E}\left\|x(t)\right\|\_{\mathcal{X}}^{2}\Big)^{\frac{1}{2}}. For brevity, we omit the index 𝒳\mathcal{X} when no confusion arises. Obviously, ℋ2​(𝒯;𝒳)⊆ℳ2​(𝒯;𝒳)\mathcal{H}^{2}({\mathcal{T}};\mathcal{X})\subseteq\mathcal{M}^{2}({\mathcal{T}};\mathcal{X}).

###### Theorem 3.5.

Consider a reference set of rules (A†,B†,F1,D,E,F2†,σ,M,F^1,G,F^2)(A^{\dagger},B^{\dagger},F\_{1},D,E,F\_{2}^{\dagger},\sigma,M,\widehat{F}\_{1},G,\widehat{F}\_{2}) for the MFG system ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))
and let (Π†,q†,x¯†,x†,u†)(\Pi^{\dagger},q^{\dagger},\bar{x}^{\dagger},x^{\dagger},u^{\dagger}) denote the solution to this MFG system given by ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). For any radii ρA,ρB,ρF2>0\rho\_{A},\rho\_{B},\rho\_{F\_{2}}>0, there exists a time T⋆>0T^{\star}>0, depending only on the radii (ρA,ρB,ρF2)(\rho\_{A},\rho\_{B},\rho\_{F\_{2}}) and on the C0C\_{0}-semi-group of A†A^{\dagger} such that:
  
For any solutions (ΠA,qA,x¯A,xA,uA)(\Pi^{A},q^{A},\bar{x}^{A},x^{A},u^{A}), (ΠB,qB,x¯B,xB,uB)(\Pi^{B},q^{B},\bar{x}^{B},x^{B},u^{B}), and (ΠF2,qF2,x¯F2,xF2,uF2)(\Pi^{F\_{2}},q^{F\_{2}},\bar{x}^{F\_{2}},x^{F\_{2}},u^{F\_{2}}) of the MFG system, corresponding to the operators A†A^{\dagger}, B†B^{\dagger}, and F2†F\_{2}^{\dagger} being perturbed to AA (provided that A−A†A-A^{\dagger} is bounded), BB, and F2F\_{2}, respectively, while other operators remain unchanged, the following stability estimates hold.

|  |  |  |
| --- | --- | --- |
|  | {supt∈𝒯‖ΠA​(t)−Π†​(t)‖ℒ​(H)≤CA,A†Π​‖A−A†‖ℒ​(H),‖x¯A−x¯†‖C​(𝒯;H)≤CA,A†x¯​‖A−A†‖ℒ​(H),‖qA−q†‖C​(𝒯;H)≤CA,A†q​‖A−A†‖ℒ​(H),‖xA−x†‖ℋ2​(𝒯;H)≤CA,A†x​‖A−A†‖ℒ​(H),‖uA−u†‖ℋ2​(𝒯;U)≤CA,A†u​‖A−A†‖ℒ​(H),\displaystyle\begin{cases}&\sup\_{t\in\mathcal{T}}\big\|\Pi^{A}(t)-\Pi^{\dagger}(t)\big\|\_{\mathcal{L}(H)}\leq C^{\Pi}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|\_{\mathcal{L}(H)},\allowdisplaybreaks\\ &\|\bar{x}^{A}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{\bar{x}}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|\_{\mathcal{L}(H)},\allowdisplaybreaks\\ &\|q^{A}-q^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{q}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|\_{\mathcal{L}(H)},\allowdisplaybreaks\\ &\|x^{A}-x^{\dagger}\|\_{\mathcal{H}^{2}({\mathcal{T}};{H})}\leq C^{x}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|\_{\mathcal{L}(H)},\allowdisplaybreaks\\ &\|u^{A}-u^{\dagger}\|\_{\mathcal{H}^{2}({\mathcal{T}};U)}\leq C^{u}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|\_{\mathcal{L}(H)},\\ \end{cases}\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | {supt∈𝒯‖ΠB​(t)−Π†​(t)‖ℒ​(H)≤CB,B†Π,1​‖B−B†‖ℒ​(U;H)+CB,B†Π,2​‖B−B†‖ℒ​(U;H)2,‖x¯B−x¯†‖C​(𝒯;H)≤CB,B†x¯,1​‖B−B†‖ℒ​(U;H)+CB,B†x¯,2​‖B−B†‖ℒ​(U;H)2,‖qB−q†‖C​(𝒯;H)≤CB,B†q,1​‖B−B†‖ℒ​(U;H)+CB,B†q,2​‖B−B†‖ℒ​(U;H)2,‖xB−x†‖ℋ2​(𝒯;H)≤CB,B†x,1​‖B−B†‖ℒ​(U;H)+CB,B†x,2​‖B−B†‖ℒ​(U;H)2,‖uB−u†‖ℋ2​(𝒯;U)≤CB,B†u,1​‖B−B†‖ℒ​(U;H)+CB,B†u,1​‖B−B†‖ℒ​(U;H)2,\displaystyle\begin{cases}&\sup\_{t\in\mathcal{T}}\big\|\Pi^{B}(t)-\Pi^{\dagger}(t)\big\|\_{\mathcal{L}(H)}\leq C^{\Pi,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}+C^{\Pi,2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}^{2},\allowdisplaybreaks\\ &\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{\bar{x},1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}+C^{\bar{x},2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}^{2},\allowdisplaybreaks\\ &\|q^{B}-q^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{q,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}+C^{q,2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}^{2},\allowdisplaybreaks\\ &\|x^{B}-x^{\dagger}\|\_{\mathcal{H}^{2}({\mathcal{T}};{H})}\leq C^{x,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}+C^{x,2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}^{2},\allowdisplaybreaks\\ &\|u^{B}-u^{\dagger}\|\_{\mathcal{H}^{2}({\mathcal{T}};{U})}\leq C^{u,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}+C^{u,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}^{2},\allowdisplaybreaks\\ \end{cases}\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | {ΠF2​(t)=Π†​(t),∀t∈𝒯,‖x¯F2−x¯†‖C​(𝒯;H)≤CF2,F2†x¯​‖F2−F2†‖ℒ​(H;ℒ​(V;H)),‖qF2−q†‖C​(𝒯;H)≤CF2,F2†q​‖F2−F2†‖ℒ​(H;ℒ​(V;H)),‖xF2−x†‖ℋ2​(𝒯;H)≤CF2,F2†x​‖F2−F2†‖ℒ​(H;ℒ​(V;H)),‖uF2−u†‖ℋ2​(𝒯;U)≤CF2,F2†u​‖F2−F2†‖ℒ​(H;ℒ​(V;H)).\displaystyle\begin{cases}&\Pi^{F\_{2}}(t)=\Pi^{\dagger}(t),\,\forall t\in\mathcal{T},\allowdisplaybreaks\\ &\|\bar{x}^{F\_{2}}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|\_{\mathcal{L}(H;\mathcal{L}(V;H))},\allowdisplaybreaks\\ &\|q^{F\_{2}}-q^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{q}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|\_{\mathcal{L}(H;\mathcal{L}(V;H))},\allowdisplaybreaks\\ &\|x^{F\_{2}}-x^{\dagger}\|\_{\mathcal{H}^{2}({\mathcal{T}};{H})}\leq C^{x}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|\_{\mathcal{L}(H;\mathcal{L}(V;H))},\allowdisplaybreaks\\ &\|u^{F\_{2}}-u^{\dagger}\|\_{\mathcal{H}^{2}({\mathcal{T}};{U})}\leq C^{u}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|\_{\mathcal{L}(H;\mathcal{L}(V;H))}.\end{cases} |  |

The constants
(CA,A†Π,CA,A†x¯,CA,A†q,CA,A†x,CA,A†u)(C^{\Pi}\_{A,A^{\dagger}},C^{\bar{x}}\_{A,A^{\dagger}},C^{q}\_{A,A^{\dagger}},C^{x}\_{A,A^{\dagger}},C^{u}\_{A,A^{\dagger}}),
(CB,B†Π,i,CB,B†x¯,i,CB,B†q,i,CB,B†x,i,CB,B†u,i)(C^{\Pi,i}\_{B,B^{\dagger}},C^{\bar{x},i}\_{B,B^{\dagger}},C^{q,i}\_{B,B^{\dagger}},C^{x,i}\_{B,B^{\dagger}},C^{u,i}\_{B,B^{\dagger}}), i=1,2i=1,2, and
  
(CF2,F2†x¯,CF2,F2†q,CF2,F2†x,CF2,F2†u)(C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}},C^{q}\_{F\_{2},F\_{2}^{\dagger}},C^{x}\_{F\_{2},F\_{2}^{\dagger}},C^{u}\_{F\_{2},F\_{2}^{\dagger}})
depend on the operators (A†,B†,F1,D,E,F2†,σ,M,F^1,G,F^2)(A^{\dagger},B^{\dagger},F\_{1},D,E,F\_{2}^{\dagger},\sigma,M,\widehat{F}\_{1},G,\widehat{F}\_{2}) and the time horizon T∗T^{\*}, as well as on the perturbed operators AA, BB, and F2F\_{2} in their respective cases.
The explicit forms of these constants are detailed in the lemmas found in Sections [4.1](https://arxiv.org/html/2510.20017v1#S4.SS1 "4.1 Stability of the equilibrium with respect to operator 𝐴 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), [4.2](https://arxiv.org/html/2510.20017v1#S4.SS2 "4.2 Stability of the equilibrium with respect to operator 𝐵 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), and [4.3](https://arxiv.org/html/2510.20017v1#S4.SS3 "4.3 Stability of the equilibrium with respect to operator 𝐹₂ ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

###### Proof.

See Sections [4.1](https://arxiv.org/html/2510.20017v1#S4.SS1 "4.1 Stability of the equilibrium with respect to operator 𝐴 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), [4.2](https://arxiv.org/html/2510.20017v1#S4.SS2 "4.2 Stability of the equilibrium with respect to operator 𝐵 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), and [4.3](https://arxiv.org/html/2510.20017v1#S4.SS3 "4.3 Stability of the equilibrium with respect to operator 𝐹₂ ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") for details.
∎

Having established that the rules-to-equilibrium operators are locally Lipschitz555We note that if Δ​B=B−B†\Delta B=B-B^{\dagger} lies in a uniformly bounded subset of ℒ​(U;H)\mathcal{L}(U;H), then quadratic terms ‖B−B†‖ℒ​(U;H)2\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}^{2} may be bounded by linear terms ‖B−B†‖ℒ​(U;H)\big\|B-B^{\dagger}\big\|\_{\mathcal{L}(U;H)}., the remaining step is to demonstrate that such operators are learnable from Gaussian samples by Lipschitz RNOs with favourable sample complexity. We show that any LL-Lipschitz map from ℋ\mathcal{H} to ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) is PAC-learnable by RNOs that preserve the same LL-Lipschitz regularity. Our sample complexity bounds are favourable precisely because RNOs can reproduce the Lipschitz continuity of the target map
666Our approximation and PAC-learning guarantees apply more generally to arbitrary separable Hilbert spaces. For clarity of exposition, however, we restrict to the spaces ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) introduced above.
.

###### Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators).

Let L≥0L\geq 0 and f:ℋ→ℳ2​(𝒯,U)f:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) be an LL-Lipschitz operator. Suppose that Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")
with Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") (ii) generalized to Yn=f​(Xn)Y\_{n}=f(X\_{n}) for n=1,…,Nn=1,\dots,N, holds.
For any compact 𝒦⊆ℋ\mathcal{K}\subseteq\mathcal{H} of measure p=def.ℙX​(𝒦)>0p\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\mathbb{P}\_{X}(\mathcal{K})>0 containing 0∈ℋ0\in\mathcal{H}, for every “approximation error” ε>0\varepsilon>0, and each “failure probability” 0<δ≤10<\delta\leq 1 there is a connectivity parameter C=def.C​(ϵ,δ,𝒦)∈ℕ+C\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}C(\epsilon,\delta,\mathcal{K})\in\mathbb{N}\_{+} such that for any empirical risk minimizer F^∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)\hat{F}\in\mathcal{RNO}^{1,L}\_{C}(e\_{\cdot},\eta\_{\cdot}); i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1N​∑n=1N‖F^​(Xn)−f​(Xn)‖ℳ2​(𝒯,U)=infF~∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)1N​∑n=1N‖F~​(Xn)−f​(Xn)‖ℳ2​(𝒯,U)\frac{1}{N}\sum\_{n=1}^{N}\,\|\hat{F}(X\_{n})-f(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}=\inf\_{\tilde{F}\in\mathcal{RNO}^{1,L}\_{C}(e\_{\cdot},\eta\_{\cdot})}\,\frac{1}{N}\sum\_{n=1}^{N}\,\|\tilde{F}(X\_{n})-f(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} |  | (ERM) |

must satisfy the following learnability guarantee

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝔼X∼ℙX​[‖F^​(X)−f​(X)‖ℳ2​(𝒯,U)]≤ε+L¯​e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N)≥pN−δ\begin{aligned} {\mathbb{P}}\Biggl(\mathbb{E}\_{X\sim\mathbb{P}\_{X}}\big[\|\hat{F}(X)-f(X)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\big]\leq\varepsilon+\bar{L}e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}\Bigg)\geq p^{N}-\delta\end{aligned} |  |

where L¯=def.2​max⁡{L,1}\bar{L}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}2\max\{L,1\} and r>0r>0 is as in Assumption ([2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) (iii). Furthermore, if C∈ℕ+C\in\mathbb{N}\_{+} is large enough, then there exists some F^∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)\hat{F}\in\mathcal{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot}) satisfying ([ERM](https://arxiv.org/html/2510.20017v1#S3.Ex19 "Equation ERM ‣ Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).

###### Proof.

See Proposition [5.5](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem5 "Proposition 5.5 (Learnability). ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") for a generalization.
∎

###### Remark 2.

If ℙN\mathbb{P}\_{N} is compactly supported on 𝒦\mathcal{K} then, the lower-bound in Theorem ([3.6](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem6 "Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) is 1−δ1-\delta.

The proof of Theorem [3.6](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem6 "Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") relies on our infinite-dimensional regular universal approximation theorem for Lipschitz RNOs. This theorem extends recent advances in Lipschitz-constrained neural network approximation Hong and Kratsios [[2024](https://arxiv.org/html/2510.20017v1#bib.bib43)], Riegler et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib48)], Murari et al. [[2025](https://arxiv.org/html/2510.20017v1#bib.bib49)] to the infinite-dimensional setting. Our analysis builds on recent developments in optimal transport techniques for establishing PAC-learning guarantees; see Amit et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib50)], Hou et al. [[2023](https://arxiv.org/html/2510.20017v1#bib.bib51)], Kratsios et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib52)], Benitez et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib34)], Detering et al. [[2025](https://arxiv.org/html/2510.20017v1#bib.bib53)].

### 3.2 Unlocking Favourable Rates

Favourable rates are obtainable when approximating a function on a suitable compact subset of the domain, called an exponentially ellipsoidal set in Alvarez et al. [[2024](https://arxiv.org/html/2510.20017v1#bib.bib37)]. In Galimberti et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib46)], it was shown that exponentially ellipsoidal subsets of Lebesgue “function” spaces on Euclidean domains correspond to infinitely smooth functions; thus, we may interpret the following as a “smoothness condition” on inputs.

###### Definition 3.1 ((ρ,r)(\rho,r)-Exponentially Ellipsoidal).

We say that 𝒦⊆ℋ\mathcal{K}\subseteq\mathcal{H} is (ρ,r¯)(\rho,\bar{r})-exponentially ellipsoidal to (ei)i∈I(e\_{i})\_{i\in I} if there exists some x†∈ℋx^{\dagger}\in\mathcal{H} and some r¯,ρ>0\bar{r},\rho>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒦⊆{x∈ℋ:x−x†=∑i∈I⟨x−x†,ei⟩​ei​ and ​|⟨x−x†,ei⟩|≤ρ​e−i​r}.\mathcal{K}\subseteq\biggl\{x\in\mathcal{H}:\,x-x^{\dagger}=\sum\_{i\in I}\,\langle x-x^{\dagger},e\_{i}\rangle e\_{i}\mbox{ and }|\langle x-x^{\dagger},e\_{i}\rangle|\leq\rho\,e^{-ir}\biggr\}. |  | (3.3) |

We say that 𝒦\mathcal{K} is centred if x†=0∈ℋx^{\dagger}=0\in\mathcal{H}; in which case 0∈𝒦0\in\mathcal{K}.
Intuitively, r¯>0\bar{r}>0 captures how “close” the “ellipsoidal set” 𝒦\mathcal{K} is aligned to the span of the basis vectors in (ei)i∈I(e\_{i})\_{i\in I} while ρ\rho captures its “radius”.

###### Proposition 3.7 (Regular Universal Approximation for Lipschitz RNOs).

Under Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), suppose that 0∈𝒦0\in\mathcal{K}, 𝒦⊂ℋ\mathcal{K}\subset\mathcal{H} is non-empty and compact, 0<α≤10<\alpha\leq 1, L>0L>0, f:𝒦→ℳ2​(𝒯,U)f:\mathcal{K}\to\mathcal{M}^{2}({\mathcal{T}},U) be an (α,L)(\alpha,L)-Hölder map, and fix an error ε>0\varepsilon>0 and a x†∈ℋx^{\dagger}\in\mathcal{H}.
There is an (α,L)(\mathbf{\alpha},{L})-Hölder RNO F^:ℋ→ℳ2​(𝒯,U)\hat{F}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) satisfying

|  |  |  |
| --- | --- | --- |
|  | supx∈𝒦‖F^​(Δ​x)−f​(x)‖ℳ2​(𝒯,U)≤ε.\sup\_{x\in\mathcal{K}}\,\big\|\hat{F}(\Delta x)-f(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\varepsilon. |  |

Furthermore, F^\hat{F} is base-point preserving; in that F^​(0)=y^†=f​(x†)\hat{F}(0)=\hat{y}^{\dagger}=f(x^{\dagger}).
  
If 𝒦\mathcal{K} is centred (r,ε)(r,\varepsilon)-exponentially ellipsoidal for some r>0r>0, then there is an F^\hat{F} of depth 𝒪​(1)\mathcal{O}(1) and whose number of non-zero parameters are 𝒪​(ε−cr,α​log⁡(ε−1))\mathcal{O}\Big(\varepsilon^{-c\_{r,\alpha}}\log(\varepsilon^{-1})\Big); where cr,α=def.1α​⌈log⁡((4​L)1r​αr1/r)⌉c\_{r,\alpha}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\frac{1}{\alpha}\Big\lceil\log\big(\tfrac{(4L)^{\frac{1}{r\alpha}}}{r^{1/r}}\big)\Big\rceil.
If, additionally, 0<L<4​eα0<L<4e^{\alpha} and r=1/W0​((4​L)−1α)r=1/W\_{0}\Big((4L)^{-\tfrac{1}{\alpha}}\Big) then, its width and connectivity are
𝒪​(ε−1​log⁡(ε−1))\mathcal{O}(\varepsilon^{-1}\log(\varepsilon^{-1})).

###### Proof.

See the more general result proved in Proposition LABEL:prop:theorem\_universality\_\_regular in Section [5.2](https://arxiv.org/html/2510.20017v1#S5.SS2 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

In situations where the user controls the sampling distribution ℙX\mathbb{P}\_{X}—used to select points on 𝒦\mathcal{K} for training the neural operator—it becomes possible to tune ℙX\mathbb{P}\_{X} so that points from 𝒦\mathcal{K} are sampled with high probability. While this is not always feasible in theory, it can often be arranged in simulations.
By coupling the radius ρ\rho of the (ρ,r)(\rho,r)-exponentially ellipsoidal set 𝒦\mathcal{K} to the approximation error, and selecting the sampling “temperature” r>0r>0 in Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") (iii) according to the failure probability δ\delta, we guarantee high-probability learnability by small neural operators. This temperature coupling is formalized in the following assumption.

###### Assumption 3.1 (Tempered Sampling).

Fix a desired sampling failure probability 0<δX≤10<\delta\_{X}\leq 1, let Δ=def.ln⁡(1/(1−δX))2+ln⁡(1/(1−δX))\Delta\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\tfrac{\ln(1/(1-\delta\_{X}))}{2+\ln(1/(1-\delta\_{X}))}, let r>0r>0 and fix an (ρ,r)(\rho,r)-ellipsoidal set 𝒦\mathcal{K} containing 0.
For simplicity, assume that: for every i∈ℕ+i\in\mathbb{N}\_{+}, and every t>0t>0 ℙ​(|Zi|≥t)≤2​e−t2/2\mathbb{P}(|Z\_{i}|\geq t)\leq 2e^{-t^{2}/2}.
  
Suppose that we pick ℙX\mathbb{P}\_{X} in Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") so that: for every i∈ℕ+i\in\mathbb{N}\_{+}

|  |  |  |
| --- | --- | --- |
|  | 0<σi≤e−r​iln⁡(2)−i​ln⁡(Δ).0<\sigma\_{i}\leq\frac{e^{-ri}}{\sqrt{\ln(2)-i\ln(\Delta)}}. |  |

In situations where the user controls the sampling distribution ℙX\mathbb{P}\_{X}—used to select points on 𝒦\mathcal{K} for training the neural operator—we obtain the following strengthened version of Theorem [3.6](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem6 "Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

###### Theorem 3.8 (Quantitative Refinement of Theorem [3.6](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem6 "Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).

In the setting of Theorem [3.6](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem6 "Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") if, additionally, there is a constant r¯>0\bar{r}>0 such that 𝒦\mathcal{K} is a centred (ε,r¯)(\varepsilon,\bar{r})-exponentially ellipsoidal777Cf. Definition [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmdefinition1 "Definition 3.1 ((𝜌,𝑟)-Exponentially Ellipsoidal). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"). setthen, there exists some F^∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)\hat{F}\in\mathcal{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot}) satisfying ([ERM](https://arxiv.org/html/2510.20017v1#S3.Ex19 "Equation ERM ‣ Theorem 3.6 (Sample Complexity of Lipschitz-RNOs When Learning Non-Linear Lipschitz Operators). ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) whose depth is 𝒪​(1)\mathcal{O}(1) and whose width and number of non-zero parameters are both 𝒪​(ε−cr¯,1​log⁡(ε−1))\mathcal{O}\big(\varepsilon^{-c\_{\bar{r},1}}\log(\varepsilon^{-1})\big); where
cr¯,1=def.⌈log⁡(4​L¯)r¯−log⁡(r¯)r¯⌉c\_{\bar{r},1}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\Big\lceil\tfrac{\log(4\bar{L})}{\bar{r}}-\tfrac{\log(\bar{r})}{\bar{r}}\Big\rceil;
satisfying

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝔼X∼ℙX​[‖F^​(X)−f​(X)‖ℳ2​(𝒯,U)]≤ε+L¯​e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N)≥e−δ−δ\begin{aligned} {\mathbb{P}}\Biggl(\mathbb{E}\_{X\sim\mathbb{P}\_{X}}\big[\|\hat{F}(X)-f(X)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\big]\leq\varepsilon+\bar{L}e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}\Bigg)\geq e^{-\delta}-\delta\end{aligned} |  |

###### Proof.

See Appendix [5.4](https://arxiv.org/html/2510.20017v1#S5.SS4 "5.4 Proof of Theorem 3.8 ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

## 4 Proofs of Stability Estimates

This section contains detailed proofs of our main results.
Consider a reference set of rules (A†,B†,F1,D,E,F2†,σ,M,F^1,G,F^2)(A^{\dagger},B^{\dagger},F\_{1},D,E,\\
F\_{2}^{\dagger},\sigma,M,\widehat{F}\_{1},G,\widehat{F}\_{2}) for the MFG system ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))
and let (Π†,q†,x¯†,x†,u†)(\Pi^{\dagger},q^{\dagger},\bar{x}^{\dagger},x^{\dagger},u^{\dagger}) denote the solution to this MFG system given by ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
In Sections [4.1](https://arxiv.org/html/2510.20017v1#S4.SS1 "4.1 Stability of the equilibrium with respect to operator 𝐴 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), [4.2](https://arxiv.org/html/2510.20017v1#S4.SS2 "4.2 Stability of the equilibrium with respect to operator 𝐵 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), and [4.3](https://arxiv.org/html/2510.20017v1#S4.SS3 "4.3 Stability of the equilibrium with respect to operator 𝐹₂ ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), we perturb the operators A†A^{\dagger}, B†B^{\dagger}, and F2†F\_{2}^{\dagger} to AA (provided that A−A†A-A^{\dagger} is bounded), BB, and F2F\_{2}, respectively, while other operators remain unchanged, and derive estimates for the resulting changes in the system.

We first present regularity results for the operators and processes associated with the reference model, i.e., (Π†,q†,x¯†,x†,u†)(\Pi^{\dagger},q^{\dagger},\bar{x}^{\dagger},x^{\dagger},u^{\dagger}). In this section, the parameters R1R\_{1}, R2R\_{2}, R3R\_{3}, R4R\_{4}, and R5R\_{5} are defined by ([A.1](https://arxiv.org/html/2510.20017v1#A1.E1 "Equation A.1 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))–([A.5](https://arxiv.org/html/2510.20017v1#A1.E5 "Equation A.5 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), respectively. Suppose S†​(t)S^{\dagger}(t) denotes the C0C\_{0}-semigroup associated with the infinitesimal generator A†A^{\dagger} such that ‖SA†​(t)‖≤MTA†\|S^{A^{\dagger}}(t)\|\leq M^{A^{\dagger}}\_{T}, for all t∈𝒯t\in\mathcal{T}. According to [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.4], the solution Π†\Pi^{\dagger} of the operator differential Riccati equation given by ([A.7](https://arxiv.org/html/2510.20017v1#A1.E7 "Equation A.7 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) for the reference set of rules satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Π†​(t)‖≤CΠ†,∀t∈𝒯,CΠ†=def.2​(MTA†)2​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))​(‖G‖+T​‖M‖).\displaystyle\begin{aligned} &\|\Pi^{\dagger}(t)\|\leq C^{\Pi^{\dagger}},\quad\forall t\in\mathcal{T},\\ &C^{\Pi^{\dagger}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}2(M\_{T}^{A^{\dagger}})^{2}\exp\big(8T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big(\|G\|+T\|M\|\big).\end{aligned} |  | (4.1) |

###### Lemma 4.1.

Suppose MTA†​(CΨ,x¯†​T+‖G‖​‖F^2‖)<1M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}^{\dagger}}T+\|G\|\|\widehat{F}\_{2}\|)<1. The mean field x¯†\bar{x}^{\dagger} and the offset term q†q^{\dagger} associated with the reference model, given by  ([A.8](https://arxiv.org/html/2510.20017v1#A1.E8 "Equation A.8 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.9](https://arxiv.org/html/2510.20017v1#A1.E9 "Equation A.9 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), respectively, satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖x¯†‖C​(𝒯;ℋ)≤Cx¯†,\displaystyle\big\|\bar{x}^{\dagger}\big\|\_{C(\mathcal{T};\mathcal{H})}\leq C^{\bar{x}^{\dagger}},\allowdisplaybreaks |  | (4.2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖q†‖C​(𝒯;ℋ)≤Cq†,\displaystyle\big\|q^{\dagger}\big\|\_{C(\mathcal{T};\mathcal{H})}\leq C^{q^{\dagger}}, |  | (4.3) |

where

|  |  |  |
| --- | --- | --- |
|  | Cx¯†=[1−MTA†(CΨ,x¯†T+∥G∥∥F^2∥)]−1[MTA†(CΦ,c,†T+|ξ¯|)exp(MTA†CΦ,x¯†T)\displaystyle C^{\bar{x}^{\dagger}}=\big[1-M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}^{\dagger}}T+\|G\|\|\widehat{F}\_{2}\|)\big]^{-1}\big[M^{A^{\dagger}}\_{T}(C^{\Phi,c,\dagger}T+|\bar{\xi}|)\exp(M^{A^{\dagger}}\_{T}C^{\Phi,\bar{x}^{\dagger}}T)\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | +MTA†CΦ,q†T(MTA†CΨ,c,†T)exp(MTA†(CΦ,x¯†+CΨ,q†)T)],\displaystyle\hskip 179.25244pt+M^{A^{\dagger}}\_{T}C^{\Phi,q^{\dagger}}T\big(M^{A^{\dagger}}\_{T}C^{\Psi,c,\dagger}T\big)\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}^{\dagger}}+C^{\Psi,q^{\dagger}})T\big)\big],\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | Cq†=MTA†​CΨ,c,†​T​exp⁡(MTA†​CΨ,q†​T)+MTA†​(CΨ,x¯†​T+‖G‖​‖F^2‖)​exp⁡(MTA†​CΨ,q†​T)​Cx¯†,\displaystyle C^{q^{\dagger}}=M^{A^{\dagger}}\_{T}C^{\Psi,c,\dagger}T\exp(M^{A^{\dagger}}\_{T}C^{\Psi,q^{\dagger}}T)+M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}^{\dagger}}T+\|G\|\|\widehat{F}\_{2}\|)\exp(M^{A^{\dagger}}\_{T}C^{\Psi,q^{\dagger}}T)C^{\bar{x}^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | CΦ,x¯†=‖B‖​(‖B‖+R3+R2​‖F2†‖)​CΠ†+‖F1‖,\displaystyle C^{\Phi,\bar{x}^{\dagger}}=\|B\|(\|B\|+R\_{3}+R\_{2}\|F\_{2}^{\dagger}\|)C^{\Pi^{\dagger}}+\|F\_{1}\|, |  |
|  |  |  |
| --- | --- | --- |
|  | CΦ,q†=‖B†‖2,CΦ,c,†=‖B†‖​R2​‖σ‖​CΠ†,\displaystyle C^{\Phi,q^{\dagger}}=\|B^{\dagger}\|^{2},\quad C^{\Phi,c,\dagger}=\|B^{\dagger}\|R\_{2}\|\sigma\|C^{\Pi^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | CΨ,q†=CΠ†​(‖B†‖+R3)​‖B†‖,\displaystyle C^{\Psi,q^{\dagger}}=C^{\Pi^{\dagger}}(\|B^{\dagger}\|+R\_{3})\big\|B^{\dagger}\big\|, |  |
|  |  |  |
| --- | --- | --- |
|  | CΨ,x¯†=[R1​CΠ†+(CΠ†)2​(‖B†‖+R3)​R2]​‖F2†‖+CΠ†​‖F1‖+‖M‖​‖F^1‖,\displaystyle C^{\Psi,\bar{x}^{\dagger}}=\big[R\_{1}C^{\Pi^{\dagger}}+(C^{\Pi^{\dagger}})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}\big]\big\|F\_{2}^{\dagger}\big\|+C^{\Pi^{\dagger}}\big\|F\_{1}\big\|+\big\|M\big\|\big\|\hat{F}\_{1}\big\|,\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | CΨ,c,†=R1​CΠ†+(CΠ†)2​(‖B†‖+R3)​R2.\displaystyle C^{\Psi,c,\dagger}=R\_{1}C^{\Pi^{\dagger}}+(C^{\Pi^{\dagger}})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}. |  |

###### Proof.

See [A.3.1](https://arxiv.org/html/2510.20017v1#A1.SS3.SSS1 "A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Lemma 4.2.

The equilibrium state x†x^{\dagger} for the reference model as given by ([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) satisfies

|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖x†​(t)‖2)12≤Cx†,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|x^{\dagger}(t)\|^{2}\big)^{\frac{1}{2}}\leq C^{x^{\dagger}}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cx†=\displaystyle C^{x^{\dagger}}= | {3(MTA†)2𝔼∥ξ∥2+3T(MTA†)2[(∥B†∥2+∥E∥2)(∥B†∥Cq†+R2(∥F2†∥Cx¯†+∥σ∥)CΠ†)]\displaystyle\big\{3(M^{A^{\dagger}}\_{T})^{2}\mathbb{E}\|\xi\|^{2}+3T(M\_{T}^{A^{\dagger}})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big(\|B^{\dagger}\|C^{q^{\dagger}}+R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}\big)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3T(MTA†)2(∥F1∥2+∥F2†∥2)(Cx¯†)2+3T(MTA†)2∥σ∥2}1/2\displaystyle\quad+3T(M^{A^{\dagger}}\_{T})^{2}(\|F\_{1}\|^{2}+\|F\_{2}^{\dagger}\|^{2})(C^{\bar{x}^{\dagger}})^{2}+3T(M^{A^{\dagger}}\_{T})^{2}\|\sigma\|^{2}\big\}^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{(MTA†)2​[(‖B†‖2+‖E‖2)​((‖B†‖+R3)​CΠ†)2+‖D‖2]​3​T/2}.\displaystyle\quad\times\exp\big\{(M^{A^{\dagger}}\_{T})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big((\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}\big)^{2}+\|D\|^{2}\big]3T/2\big\}. |  |

###### Proof.

See [A.3.2](https://arxiv.org/html/2510.20017v1#A1.SS3.SSS2 "A.3.2 Proof of Lemma 4.2 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

### 4.1 Stability of the equilibrium with respect to operator AA

In this section, we perturb the operator A†A^{\dagger} to AA and denote by (ΠA,x¯A,qA,uA,xA)(\Pi^{A},\bar{x}^{A},q^{A},u^{A},x^{A}) the solution to the MFG system, given by ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), corresponding to the set of rules (A(A, B†B^{\dagger}, DD, EE, F1F\_{1}, F2†F\_{2}^{\dagger}, σ\sigma, MM, F^1\widehat{F}\_{1}, F^2\widehat{F}\_{2}, G)G).

###### Lemma 4.3.

Suppose AA and A†A^{\dagger} are unbounded linear operators defined on the same domain, and assume that the difference operator A−A†A-A^{\dagger} is a bounded linear operator, i.e. A−A†∈ℒ​(H)A-A^{\dagger}\in\mathcal{L}(H). Furthermore, suppose that the perturbed operator AA generates a C0C\_{0}-semigroup SA​(t)∈ℒ​(H)S^{A}(t)\in\mathcal{L}(H), with ‖SA​(t)‖ℒ​(H)≤MTA\big\|S^{A}(t)\big\|\_{\mathcal{L}(H)}\leq M^{A}\_{T}, for all t∈𝒯t\in{\mathcal{T}}. Then, for all t∈𝒯t\in\mathcal{T},

|  |  |  |
| --- | --- | --- |
|  | ‖SA​(t)−SA†​(t)‖ℒ​(H)≤MTA,A†​‖A−A†‖,\displaystyle\big\|S^{A}(t)-S^{A^{\dagger}}(t)\big\|\_{\mathcal{L}(H)}\leq M^{A,A^{\dagger}}\_{T}\|A-A^{\dagger}\|, |  |

where MTA,A†=def.MTA​MTA†M^{A,A^{\dagger}}\_{T}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}M^{A}\_{T}M^{A^{\dagger}}\_{T}.

###### Proof.

See [A.4.1](https://arxiv.org/html/2510.20017v1#A1.SS4.SSS1 "A.4.1 Proof of Lemma 4.3 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Lemma 4.4.

For all t∈𝒯t\in\mathcal{T}, the solution ΠA\Pi^{A} of the operator differential Riccati equation, associated with the perturbed operator AA, satisfies

|  |  |  |
| --- | --- | --- |
|  | ‖ΠA​(t)‖≤CAΠ,\displaystyle\big\|\Pi^{A}(t)\big\|\leq C^{\Pi}\_{A},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ΠA​(t)−Π†​(t)‖≤CA,A†Π​‖A−A†‖,\displaystyle\big\|\Pi^{A}(t)-\Pi^{\dagger}(t)\big\|\leq C^{\Pi}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|, |  | (4.4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CAΠ=def.\displaystyle C^{\Pi}\_{A}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}} | 2​(MTA)2​exp⁡(8​T​(MTA)2​‖D‖2​tr​(Q))​(‖G‖+T​‖M‖),\displaystyle 2(M\_{T}^{A})^{2}\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big(\|G\|+T\|M\|\big),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Π=def.\displaystyle C^{\Pi}\_{A,A^{\dagger}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}} | {‖M‖​(T+1)+T​(‖B†‖+R3)2​CΠ†}​(1+CΠ†+CAΠ)\displaystyle\Big\{\|M\|(T+1)+T(\|B^{\dagger}\|+R\_{3})^{2}C^{\Pi^{\dagger}}\Big\}(1+C^{\Pi^{\dagger}}+C^{\Pi}\_{A})\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×2​2​[MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))+MTA​exp⁡(8​T​(MTA)2​‖D‖2​tr​(Q))]\displaystyle\times 2\sqrt{2}\big[M\_{T}^{A^{\dagger}}\exp\big(8T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)+M\_{T}^{A}\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×‖D‖​T1/2​[MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))]​exp⁡((MTA)2​‖D‖2​T)\displaystyle\times\|D\|T^{1/2}\Big[M\_{T}^{A^{\dagger}}\exp\big(8T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\Big]\exp((M\_{T}^{A})^{2}\|D\|^{2}T)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp{T(∥B†∥+R3)2(1+R5CAΠ)[CΠ2MTA†MTAexp(8T((MTA†)2+(MTA)2)∥D∥2tr(Q))\displaystyle\times\exp\Big\{T(\|B^{\dagger}\|+R\_{3})^{2}(1+R\_{5}C^{\Pi}\_{A})\Big[C^{\Pi}2M\_{T}^{A^{\dagger}}M\_{T}^{A}\exp\big(8T\big((M\_{T}^{A^{\dagger}})^{2}+(M\_{T}^{A})^{2}\big)\|D\|^{2}\mathrm{tr}(Q)\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CAΠ2(MTA)exp(8T(MTA)2∥D∥2tr(Q))]}MA,A†T.\displaystyle+C^{\Pi}\_{A}\sqrt{2}(M\_{T}^{A})\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\Big]\Big\}M^{A,A^{\dagger}}\_{T}. |  |

###### Proof.

See [A.4.2](https://arxiv.org/html/2510.20017v1#A1.SS4.SSS2 "A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Lemma 4.5.

Suppose that

|  |  |  |  |
| --- | --- | --- | --- |
|  | MTA​(CAΨ,x¯​T+‖G‖​‖F^2‖)<1,(MTA​CA,A†Ψ,x¯​T+MTA​‖G‖​‖F^2‖)​MTA​CA,A†Φ,q​T​exp⁡(MTA​(CA,A†Φ,x¯+CA,A†Ψ,q)​T)<1.\displaystyle\begin{aligned} &M^{A}\_{T}(C^{\Psi,\bar{x}}\_{A}T+\|G\|\|\widehat{F}\_{2}\|)<1,\\ &(M^{A}\_{T}C^{\Psi,\bar{x}}\_{A,A^{\dagger}}T+M^{A}\_{T}\|G\|\|\widehat{F}\_{2}\|)M^{A}\_{T}C^{\Phi,q}\_{A,A^{\dagger}}T\exp\big(M^{A}\_{T}(C^{\Phi,\bar{x}}\_{A,A^{\dagger}}+C^{\Psi,q}\_{A,A^{\dagger}})T\big)<1.\end{aligned} |  | (4.5) |

Then, the offset term qAq^{A} and the mean field x¯A\bar{x}^{A}, corresponding to the perturbed operator AA, satisfy

|  |  |  |
| --- | --- | --- |
|  | ‖x¯A‖C​(𝒯;H)≤CAx¯,\displaystyle\|\bar{x}^{A}\|\_{C(\mathcal{T};H)}\leq C^{\bar{x}}\_{A},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | ‖qA‖C​(𝒯;H)≤CAq,\displaystyle\|q^{A}\|\_{C(\mathcal{T};H)}\leq C^{q}\_{A},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | ‖x¯A−x¯†‖C​(𝒯;H)≤CA,A†x¯​‖A−A†‖,\displaystyle\|\bar{x}^{A}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{\bar{x}}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|,\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | ‖qA−q†‖C​(𝒯;H)≤CA,A†q​‖A−A†‖,\displaystyle\|q^{A}-q^{\dagger}\|\_{C(\mathcal{T};H)}\leq C^{q}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†x¯\displaystyle C^{\bar{x}}\_{A,A^{\dagger}} | =[1−(MTA​CA,A†Ψ,x¯​T+MTA​‖G‖​‖F^2‖)​MTA​CA,A†Φ,q​T​exp⁡(MTA​(CA,A†Φ,x¯+CA,A†Ψ,q)​T)]−1\displaystyle=\big[1-(M^{A}\_{T}C^{\Psi,\bar{x}}\_{A,A^{\dagger}}T+M^{A}\_{T}\|G\|\|\widehat{F}\_{2}\|)M^{A}\_{T}C^{\Phi,q}\_{A,A^{\dagger}}T\exp\big(M^{A}\_{T}(C^{\Phi,\bar{x}}\_{A,A^{\dagger}}+C^{\Psi,q}\_{A,A^{\dagger}})T\big)\big]^{-1}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×{[MTA,A†(CΦ,x¯†Cx¯†+CΦ,q†Cq†+CΦ,c,†)T+MTACA,A†Φ,ΠCA,A†ΠT+MTA,A†∥ξ¯∥]\displaystyle\times\!\Big\{\!\Big[M^{A,A^{\dagger}}\_{T}\big(C^{\Phi,\bar{x}^{\dagger}}C^{\bar{x}^{\dagger}}+C^{\Phi,q^{\dagger}}C^{q^{\dagger}}+C^{\Phi,c,\dagger}\big)T+M^{A}\_{T}C^{\Phi,\Pi}\_{A,A^{\dagger}}C^{\Pi}\_{A,A^{\dagger}}T+M\_{T}^{A,A^{\dagger}}\big\|\bar{\xi}\big\|\Big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp(MTACA,A†Φ,x¯T)+MTACA,A†Φ,qT[MTA,A†(CΨ,q†Cq†+CΨ,x¯†Cx¯†+CΨ,c,†)T\displaystyle\times\exp(M\_{T}^{A}C^{\Phi,\bar{x}}\_{A,A^{\dagger}}T)+M^{A}\_{T}C^{\Phi,q}\_{A,A^{\dagger}}T\Big[M^{A,A^{\dagger}}\_{T}\big(C^{\Psi,q^{\dagger}}C^{q^{\dagger}}+C^{\Psi,\bar{x}^{\dagger}}C^{\bar{x}^{\dagger}}+C^{\Psi,c,\dagger}\big)T\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +MTACA,A†Ψ,ΠCA,A†ΠT+MTA,A†Cx¯†∥G∥∥F^2∥]exp(MTA(CA,A†Φ,x¯+CA,A†Ψ,q)T)},\displaystyle+M^{A}\_{T}C^{\Psi,\Pi}\_{A,A^{\dagger}}C^{\Pi}\_{A,A^{\dagger}}T+M^{A,A^{\dagger}}\_{T}C^{\bar{x}^{\dagger}}\|G\|\|\widehat{F}\_{2}\|\Big]\exp\big(M^{A}\_{T}(C^{\Phi,\bar{x}}\_{A,A^{\dagger}}+C^{\Psi,q}\_{A,A^{\dagger}})T\big)\Big\},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†q=\displaystyle C^{q}\_{A,A^{\dagger}}= | [MTA,A†​(CΨ,q†​Cq†+CΨ,x¯†​Cx¯†+CΨ,c,†)​T+MTA​CA,A†Ψ,Π​CA,A†Π​T+MTA,A†​Cx¯†​‖G‖​‖F^2‖]\displaystyle\Big[M^{A,A^{\dagger}}\_{T}\big(C^{\Psi,q^{\dagger}}C^{q^{\dagger}}+C^{\Psi,\bar{x}^{\dagger}}C^{\bar{x}^{\dagger}}+C^{\Psi,c,\dagger}\big)T+M^{A}\_{T}C^{\Psi,\Pi}\_{A,A^{\dagger}}C^{\Pi}\_{A,A^{\dagger}}T+M^{A,A^{\dagger}}\_{T}C^{\bar{x}^{\dagger}}\|G\|\|\widehat{F}\_{2}\|\Big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡(MTA​CA,A†Ψ,x¯​T)+[MTA​CA,A†Ψ,x¯​T+MTA​‖G‖​‖F^2‖]​exp⁡(MTA​CA,A†Ψ,x¯​T)​CA,A†x¯,\displaystyle\times\exp\big(M^{A}\_{T}C^{\Psi,\bar{x}}\_{A,A^{\dagger}}T\big)+\Big[M^{A}\_{T}C^{\Psi,\bar{x}}\_{A,A^{\dagger}}T+M^{A}\_{T}\|G\|\|\widehat{F}\_{2}\|\Big]\exp\big(M^{A}\_{T}C^{\Psi,\bar{x}}\_{A,A^{\dagger}}T\big)C^{\bar{x}}\_{A,A^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Φ,x¯=\displaystyle C^{\Phi,\bar{x}}\_{A,A^{\dagger}}= | ‖B†‖​(‖B†‖+R3)​CAΠ+R2​CΠ†​‖B†‖​‖F2†‖+‖F1‖,\displaystyle\|B^{\dagger}\|(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}+R\_{2}C^{\Pi^{\dagger}}\|B^{\dagger}\|\|F\_{2}^{\dagger}\|+\|F\_{1}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Φ,q=\displaystyle C^{\Phi,q}\_{A,A^{\dagger}}= | ‖B†‖2,\displaystyle\|B^{\dagger}\|^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Φ,Π=\displaystyle C^{\Phi,\Pi}\_{A,A^{\dagger}}= | ‖B†‖​R5​(‖B†‖+R3)​CΠ†​Cx¯†+‖B†‖​(‖B†‖+R3)​Cx¯†+‖B†‖2​R3​Cq†\displaystyle\|B^{\dagger}\|R\_{5}(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}C^{\bar{x}^{\dagger}}+\|B^{\dagger}\|(\|B^{\dagger}\|+R\_{3})C^{\bar{x}^{\dagger}}+\|B^{\dagger}\|^{2}R\_{3}C^{q^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +‖B†‖​R5​R2​(‖F2†‖​Cx¯†+‖σ‖)​CΠ†+‖B†‖​R2​(‖F2†‖​CAx¯+‖σ‖)+‖F1‖,\displaystyle+\|B^{\dagger}\|R\_{5}R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}+\|B^{\dagger}\|R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{A}+\|\sigma\|)+\|F\_{1}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ψ,x¯=\displaystyle C^{\Psi,\bar{x}}\_{A,A^{\dagger}}= | R1​‖F2†‖​CΠ†+(‖B†‖+R3)​CAΠ​R2​‖F2†‖​CΠ†+CAΠ​‖F1‖+‖M‖​‖F^1‖,\displaystyle R\_{1}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}+(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}R\_{2}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}+C^{\Pi}\_{A}\|F\_{1}\|+\|M\|\|\widehat{F}\_{1}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ψ,q=\displaystyle C^{\Psi,q}\_{A,A^{\dagger}}= | (‖B†‖+R3)​CAΠ​‖B†‖,\displaystyle(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}\|B^{\dagger}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ψ,Π=\displaystyle C^{\Psi,\Pi}\_{A,A^{\dagger}}= | (‖B†‖+R3)​‖B†‖​Cq†+(‖B†‖+R3)​CAΠ​R5​‖B†‖​Cq†+R1​(‖F2†‖​CAx¯+‖σ‖),\displaystyle(\|B^{\dagger}\|+R\_{3})\|B^{\dagger}\|C^{q^{\dagger}}+(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}R\_{5}\|B^{\dagger}\|C^{q^{\dagger}}+R\_{1}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{A}+\|\sigma\|),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(‖B†‖+R3)​R2​(‖F2†‖​Cx¯†+‖σ‖)​CΠ†+(‖B†‖+R3)​CAΠ​R5​R2​(‖F2†‖​Cx¯†+‖σ‖)​CΠ†\displaystyle+(\|B^{\dagger}\|+R\_{3})R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}+(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}R\_{5}R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(‖B†‖+R3)​CAΠ​R2​(‖F2‖​CAx¯+‖σ‖)+‖F1‖​Cx¯†,\displaystyle+(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}R\_{2}(\|F\_{2}\|C^{\bar{x}}\_{A}+\|\sigma\|)+\|F\_{1}\|C^{\bar{x}^{\dagger}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAx¯=\displaystyle C^{\bar{x}}\_{A}= | [1−MTA​(CAΨ,x¯​T+‖G‖​‖F^2‖)]−1\displaystyle\big[1-M^{A}\_{T}(C^{\Psi,\bar{x}}\_{A}T+\|G\|\|\widehat{F}\_{2}\|)\big]^{-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[MTA​(CAΦ,c​T+‖ξ¯‖)​exp⁡(MTA​CAΦ,x¯​T)+MTA​CAΦ,q​T​(MTA​CAΨ,c​T)​exp⁡(MTA​(CAΦ,x¯+CAΨ,q)​T)],\displaystyle\times\big[M^{A}\_{T}(C^{\Phi,c}\_{A}T+\big\|\bar{\xi}\big\|)\exp(M^{A}\_{T}C^{\Phi,\bar{x}}\_{A}T)+M^{A}\_{T}C^{\Phi,q}\_{A}T\big(M^{A}\_{T}C^{\Psi,c}\_{A}T\big)\exp\big(M^{A}\_{T}(C^{\Phi,\bar{x}}\_{A}+C^{\Psi,q}\_{A})T\big)\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAq=\displaystyle C^{q}\_{A}= | MTA​CAΨ,c​T​exp⁡(MTA​CAΨ,q​T)+MTA​(CAΨ,x¯​T+‖G‖​‖F^2‖)​exp⁡(MTA​CAΨ,q​T)​CAx¯,\displaystyle M^{A}\_{T}C^{\Psi,c}\_{A}T\exp(M^{A}\_{T}C^{\Psi,q}\_{A}T)+M^{A}\_{T}(C^{\Psi,\bar{x}}\_{A}T+\|G\|\|\widehat{F}\_{2}\|)\exp(M^{A}\_{T}C^{\Psi,q}\_{A}T)C^{\bar{x}}\_{A}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAΦ,x¯=\displaystyle C^{\Phi,\bar{x}}\_{A}= | ‖B†‖​(‖B†‖+R3+R2​‖F2†‖)​CAΠ+‖F1‖,\displaystyle\|B^{\dagger}\|(\|B^{\dagger}\|+R\_{3}+R\_{2}\|F\_{2}^{\dagger}\|)C^{\Pi}\_{A}+\|F\_{1}\|, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAΦ,q=\displaystyle C^{\Phi,q}\_{A}= | ‖B†‖2,\displaystyle\|B^{\dagger}\|^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAΦ,c=\displaystyle C^{\Phi,c}\_{A}= | R2​‖B†‖​‖σ‖​CAΠ,\displaystyle R\_{2}\|B^{\dagger}\|\|\sigma\|C^{\Pi}\_{A}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAΨ,q=\displaystyle C^{\Psi,q}\_{A}= | CAΠ​(‖B†‖+R3)​‖B†‖,\displaystyle C^{\Pi}\_{A}(\|B^{\dagger}\|+R\_{3})\big\|B^{\dagger}\big\|, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAΨ,x¯=\displaystyle C^{\Psi,\bar{x}}\_{A}= | [R1​CAΠ+(CAΠ)2​(‖B†‖+R3)​R2]​‖F2†‖+CAΠ​‖F1‖+‖M‖​‖F^1‖,\displaystyle\big[R\_{1}C^{\Pi}\_{A}+(C^{\Pi}\_{A})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}\big]\big\|F\_{2}^{\dagger}\big\|+C^{\Pi}\_{A}\big\|F\_{1}\big\|+\big\|M\big\|\big\|\widehat{F}\_{1}\big\|, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CAΨ,c=\displaystyle C^{\Psi,c}\_{A}= | R1​CAΠ+(CAΠ)2​(‖B†‖+R3)​R2.\displaystyle R\_{1}C^{\Pi}\_{A}+(C^{\Pi}\_{A})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}. |  |

###### Proof.

See [A.4.3](https://arxiv.org/html/2510.20017v1#A1.SS4.SSS3 "A.4.3 Proof of Lemma 4.5 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Lemma 4.6.

The equilibrium state xAx^{A}, associated with the perturbed operator AA, satisfies

|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖xA​(t)‖2)12≤CAx,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|x^{A}(t)\|^{2}\big)^{\frac{1}{2}}\leq C^{x}\_{A}, |  |
|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖(xA−x†)​(t)‖2)12≤CA,A†x​‖A−A†‖,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|(x^{A}-x^{\dagger})(t)\|^{2}\big)^{\frac{1}{2}}\leq C^{x}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CAx=\displaystyle C^{x}\_{A}= | {3(MTA)2𝔼∥ξ∥2+3T(MTA)2[(∥B†∥2+∥E∥2)(∥B†∥CAq+R2(∥F2†∥CAx¯+∥σ∥)CAΠ)]\displaystyle\big\{3(M^{A}\_{T})^{2}\mathbb{E}\|\xi\|^{2}+3T(M\_{T}^{A})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big(\|B^{\dagger}\|C^{q}\_{A}+R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{A}+\|\sigma\|)C^{\Pi}\_{A}\big)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3T(MTA)2(∥F1∥2+∥F2†∥2)(CAx¯)2+3T(MTA)2∥σ∥2}1/2\displaystyle\hskip 113.81102pt+3T(M^{A}\_{T})^{2}(\|F\_{1}\|^{2}+\|F\_{2}^{\dagger}\|^{2})(C^{\bar{x}}\_{A})^{2}+3T(M^{A}\_{T})^{2}\|\sigma\|^{2}\big\}^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{(MTA)2​[(‖B†‖2+‖E‖2)​((‖B†‖+R3)​CAΠ)2+‖D‖2]​3​T/2},\displaystyle\times\exp\big\{(M^{A}\_{T})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big((\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}\big)^{2}+\|D\|^{2}\big]3T/2\big\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†x=\displaystyle C^{x}\_{A,A^{\dagger}}= | MTA,A†{𝔼∥ξ∥2+T(CΞ1†+CΞ2†)\displaystyle M^{A,A^{\dagger}}\_{T}\big\{\mathbb{E}\|\xi\|^{2}+T(C^{\Xi\_{1}^{\dagger}}+C^{\Xi\_{2}^{\dagger}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +T[(CA,A†Ξ1,Π+CA,A†Ξ2,Π)CA,A†Π+(CA,A†Ξ1,x¯+CA,A†Ξ2,x¯)CA,A†x¯+(CA,A†Ξ1,q+CA,A†Ξ2,q)CA,A†q]}1/2\displaystyle+T\big[(C^{\Xi\_{1},\Pi}\_{A,A^{\dagger}}+C^{\Xi\_{2},\Pi}\_{A,A^{\dagger}})C^{\Pi}\_{A,A^{\dagger}}+(C^{\Xi\_{1},\bar{x}}\_{A,A^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{A,A^{\dagger}})C^{\bar{x}}\_{A,A^{\dagger}}+(C^{\Xi\_{1},q}\_{A,A^{\dagger}}+C^{\Xi\_{2},q}\_{A,A^{\dagger}})C^{q}\_{A,A^{\dagger}}\big]\big\}^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{T​(MTA)2​(CA,A†Ξ1,x+CA,A†Ξ2,x)/2},\displaystyle\times\exp\big\{T(M^{A}\_{T})^{2}(C^{\Xi\_{1},x}\_{A,A^{\dagger}}+C^{\Xi\_{2},x}\_{A,A^{\dagger}})/2\big\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CΞ1†=\displaystyle C^{\Xi\_{1}^{\dagger}}= | 3​‖B†‖2​(‖B†‖+R3)2​(CΠ†)2​(Cx†)2+3​‖F1‖2​(Cx¯†)2\displaystyle 3\|B^{\dagger}\|^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi^{\dagger}})^{2}(C^{x^{\dagger}})^{2}+3\|F\_{1}\|^{2}(C^{\bar{x}^{\dagger}})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​‖B†‖2​[2​‖B†‖2​(Cq†)2+4​(R2)2​(‖F2†‖2​(Cx¯†)2+‖σ‖2)​(CΠ†)2],\displaystyle+3\|B^{\dagger}\|^{2}\big[2\|B^{\dagger}\|^{2}(C^{q^{\dagger}})^{2}+4(R\_{2})^{2}(\|F\_{2}^{\dagger}\|^{2}(C^{\bar{x}^{\dagger}})^{2}+\|\sigma\|^{2})(C^{\Pi^{\dagger}})^{2}\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CΞ2†=\displaystyle C^{\Xi\_{2}^{\dagger}}= | 4​[2​‖D‖2+2​‖E‖2​(‖B†‖+R3)2​(CΠ†)2]​(Cx†)2+4​‖F2†‖2​(Cx¯†)2+4​‖σ‖2\displaystyle 4\big[2\|D\|^{2}+2\|E\|^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi^{\dagger}})^{2}\big](C^{x^{\dagger}})^{2}+4\|F\_{2}^{\dagger}\|^{2}(C^{\bar{x}^{\dagger}})^{2}+4\|\sigma\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +4​‖E‖2​[2​‖B†‖2​(Cq†)2+4​(R2)2​(‖F2†‖2​(Cx¯†)2+‖σ‖2)​(CΠ†)2].\displaystyle+4\|E\|^{2}\big[2\|B^{\dagger}\|^{2}(C^{q^{\dagger}})^{2}+4(R\_{2})^{2}(\|F\_{2}^{\dagger}\|^{2}(C^{\bar{x}^{\dagger}})^{2}+\|\sigma\|^{2})(C^{\Pi^{\dagger}})^{2}\big]. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ξ1,x=\displaystyle C^{\Xi\_{1},x}\_{A,A^{\dagger}}= | 4​[‖B†‖​(‖B†‖+R3)​CΠ†]2,\displaystyle 4\big[\|B^{\dagger}\|(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}\big]^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ξ2,x=\displaystyle C^{\Xi\_{2},x}\_{A,A^{\dagger}}= | 4​[‖E‖​(‖B†‖+R3)​CΠ†]2,\displaystyle 4\big[\|E\|(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}\big]^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ξ1,Π=\displaystyle C^{\Xi\_{1},\Pi}\_{A,A^{\dagger}}= | 4​‖B†‖2​(Cx†)2​[2​(R5)2​(‖B†‖+R3)2​(CΠ†)2+2​(‖B†‖+R3)2],\displaystyle 4\|B^{\dagger}\|^{2}(C^{x^{\dagger}})^{2}\big[2(R\_{5})^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi^{\dagger}})^{2}+2(\|B^{\dagger}\|+R\_{3})^{2}\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ξ2,Π=\displaystyle C^{\Xi\_{2},\Pi}\_{A,A^{\dagger}}= | 4​‖E‖2​(Cx†)2​[2​(R5)2​(‖B†‖+R3)2​(CΠ†)2+2​(‖B†‖+R3)2],\displaystyle 4\|E\|^{2}(C^{x^{\dagger}})^{2}\big[2(R\_{5})^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi^{\dagger}})^{2}+2(\|B^{\dagger}\|+R\_{3})^{2}\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ξ1,x¯=\displaystyle C^{\Xi\_{1},\bar{x}}\_{A,A^{\dagger}}= | 4​[2​(R2)2​‖F2†‖2+2​‖F1‖2],\displaystyle 4\big[2(R\_{2})^{2}\|F\_{2}^{\dagger}\|^{2}+2\|F\_{1}\|^{2}\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ξ2,x¯=\displaystyle C^{\Xi\_{2},\bar{x}}\_{A,A^{\dagger}}= | 4​[2​(R2)2​‖F2†‖2+2​‖F2†‖2],\displaystyle 4\big[2(R\_{2})^{2}\|F\_{2}^{\dagger}\|^{2}+2\|F\_{2}^{\dagger}\|^{2}\big], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CA,A†Ξ1,q=\displaystyle C^{\Xi\_{1},q}\_{A,A^{\dagger}}= | 4​‖B†‖4,\displaystyle 4\|B^{\dagger}\|^{4}, |  | (4.6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†Ξ2,q=\displaystyle C^{\Xi\_{2},q}\_{A,A^{\dagger}}= | 4​‖E‖2​‖B†‖2.\displaystyle 4\|E\|^{2}\|B^{\dagger}\|^{2}. |  |

###### Proof.

The bound CAxC^{x}\_{A} for xAx^{A} follows from Lemma [4.2](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") with A†A^{\dagger} replaced by AA.

Denote

|  |  |  |
| --- | --- | --- |
|  | Ξ1A​(t)=B†​((KA)−1​LA)​(T−r)​xA​(r)+B†​τA​(r)−F1​x¯A​(r),\displaystyle\Xi\_{1}^{A}(t)=B^{\dagger}((K^{A})^{-1}L^{A})(T-r)x^{A}(r)+B^{\dagger}\tau^{A}(r)-F\_{1}\bar{x}^{A}(r),\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | Ξ2A​(t)=[D−E​((KA)−1​LA)​(T−t)]​xA​(r)−E​τA​(t)+F2†​x¯A​(t)+σ,\displaystyle\Xi\_{2}^{A}(t)=\big[D-E((K^{A})^{-1}L^{A})(T-t)\big]x^{A}(r)-E\tau^{A}(t)+F\_{2}^{\dagger}\bar{x}^{A}(t)+\sigma, |  |

where τA​(t)=(KA​(T−r))−1​[B⋆​qA​(T−t)+Γ2​((F2​x¯​(t)+σ)⋆​ΠA​(T−t))]\tau^{A}(t)=(K^{A}(T-r))^{-1}\big[B^{\star}q^{A}(T-t)+\Gamma\_{2}\big((F\_{2}\bar{x}(t)+\sigma)^{\star}\Pi^{A}(T-t)\big)\big]. By ([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (xA−x†)​(t)≤\displaystyle(x^{A}-x^{\dagger})(t)\leq | (SA−S†)​(t)​ξ+∫0t(SA−S†)​(t−r)​Ξ1A​(r)​𝑑r+∫0tS†​(t−r)​(Ξ1A−Ξ1†)​(r)​𝑑r\displaystyle(S^{A}-S^{\dagger})(t)\xi+\int\_{0}^{t}(S^{A}-S^{\dagger})(t-r)\Xi\_{1}^{A}(r)dr+\int\_{0}^{t}S^{\dagger}(t-r)(\Xi\_{1}^{A}-\Xi\_{1}^{\dagger})(r)dr\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t(SA−S†)​(t−r)​Ξ2A​(r)​𝑑W​(r)+∫0tS†​(t−r)​(Ξ2A−Ξ2†)​(r)​𝑑W​(r).\displaystyle+\int\_{0}^{t}(S^{A}-S^{\dagger})(t-r)\Xi\_{2}^{A}(r)dW(r)+\int\_{0}^{t}S^{\dagger}(t-r)(\Xi\_{2}^{A}-\Xi\_{2}^{\dagger})(r)dW(r). |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ξ1A−Ξ1†)​(r)=\displaystyle(\Xi\_{1}^{A}-\Xi\_{1}^{\dagger})(r)= | B†​((KA)−1​LA−(K†)−1​L†)​(T−r)​xA​(r)+B†​(K†)−1​L†​(xA−x†)​(r)\displaystyle B^{\dagger}\big((K^{A})^{-1}L^{A}-(K^{\dagger})^{-1}L^{\dagger}\big)(T-r)x^{A}(r)+B^{\dagger}(K^{\dagger})^{-1}L^{\dagger}(x^{A}-x^{\dagger})(r)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +B†​(τA−τ†)​(r)−F1​(x¯−x¯†),\displaystyle+B^{\dagger}(\tau^{A}-\tau^{\dagger})(r)-F\_{1}(\bar{x}-\bar{x}^{\dagger}),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ξ2A−Ξ2†)​(r)=\displaystyle(\Xi\_{2}^{A}-\Xi\_{2}^{\dagger})(r)= | −E​((KA)−1​LA−(K†)−1​L†)​(T−r)​xA​(r)+F2†​(x¯A−x¯†)​(r)\displaystyle-E\big((K^{A})^{-1}L^{A}-(K^{\dagger})^{-1}L^{\dagger}\big)(T-r)x^{A}(r)+F\_{2}^{\dagger}(\overline{x}^{A}-\overline{x}^{\dagger})(r)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[D−E​(K†)−1​L†​(T−r)]​(xA−x†)​(r)−E​(τA−τ†)​(r),\displaystyle+[D-E(K^{\dagger})^{-1}L^{\dagger}(T-r)](x^{A}-x^{\dagger})(r)-E(\tau^{A}-\tau^{\dagger})(r), |  |

where τ​(t)=(K​(T−r))−1​[B⋆​q​(T−t)+Γ2​((F2​x¯​(t)+σ)⋆​Π​(T−t))]\tau(t)=(K(T-r))^{-1}\big[B^{\star}q(T-t)+\Gamma\_{2}\big((F\_{2}\bar{x}(t)+\sigma)^{\star}\Pi(T-t)\big)\big], for i=1,2i=1,2, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(ΞiA−Ξi†)​(t)‖2≤\displaystyle\mathbb{E}\|(\Xi\_{i}^{A}-\Xi\_{i}^{\dagger})(t)\|^{2}\leq | CA,A†Ξi,x​𝔼​‖(xA−x†)​(t)‖2+CA,A†Ξi,Π​supr∈𝒯‖(ΠA−Π†)​(r)‖2\displaystyle C^{\Xi\_{i},x}\_{A,A^{\dagger}}\mathbb{E}\|(x^{A}-x^{\dagger})(t)\|^{2}+C^{\Xi\_{i},\Pi}\_{A,A^{\dagger}}\sup\_{r\in\mathcal{T}}\|(\Pi^{A}-\Pi^{\dagger})(r)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CA,A†Ξi,x¯​‖x¯A−x¯†‖C​(𝒯;H)2+CA,A†Ξi,q​‖qA−q†‖C​(𝒯;H)2\displaystyle+C^{\Xi\_{i},\bar{x}}\_{A,A^{\dagger}}\|\bar{x}^{A}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+C^{\Xi\_{i},q}\_{A,A^{\dagger}}\|q^{A}-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CA,A†Ξi,x​𝔼​‖(xA−x†)​(t)‖2+[CA,A†Ξi,Π​CA,A†Π+CA,A†Ξi,x¯​CA,A†x¯+CA,A†Ξi,q​CA,A†q]​‖A−A†‖2.\displaystyle C^{\Xi\_{i},x}\_{A,A^{\dagger}}\mathbb{E}\|(x^{A}-x^{\dagger})(t)\|^{2}+\big[C^{\Xi\_{i},\Pi}\_{A,A^{\dagger}}C^{\Pi}\_{A,A^{\dagger}}+C^{\Xi\_{i},\bar{x}}\_{A,A^{\dagger}}C^{\bar{x}}\_{A,A^{\dagger}}+C^{\Xi\_{i},q}\_{A,A^{\dagger}}C^{q}\_{A,A^{\dagger}}\big]\|A-A^{\dagger}\|^{2}. |  |

We also have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖Ξ1A​(r)‖2≤\displaystyle\mathbb{E}\|\Xi\_{1}^{A}(r)\|^{2}\leq | 3​‖B†​((KA)−1​LA)​(T−r)‖2​𝔼​‖xA​(r)‖2+3​‖B†‖2​‖τA​(r)‖2+3​‖F1‖2​‖x¯A​(r)‖2\displaystyle 3\|B^{\dagger}((K^{A})^{-1}L^{A})(T-r)\|^{2}\mathbb{E}\|x^{A}(r)\|^{2}+3\|B^{\dagger}\|^{2}\|\tau^{A}(r)\|^{2}+3\|F\_{1}\|^{2}\|\bar{x}^{A}(r)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 3​‖B†‖2​(‖B†‖+R3)2​(CAΠ)2​(CAx)2+3​‖F1‖2​(CAx¯)2\displaystyle 3\|B^{\dagger}\|^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi}\_{A})^{2}(C^{x}\_{A})^{2}+3\|F\_{1}\|^{2}(C^{\bar{x}}\_{A})^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​‖B†‖2​[2​‖B†‖2​(CAq)2+4​(R2)2​(‖F2†‖2​(CAx¯)2+‖σ‖2)​(CAΠ)2]\displaystyle+3\|B^{\dagger}\|^{2}\big[2\|B^{\dagger}\|^{2}(C^{q}\_{A})^{2}+4(R\_{2})^{2}(\|F\_{2}^{\dagger}\|^{2}(C^{\bar{x}}\_{A})^{2}+\|\sigma\|^{2})(C^{\Pi}\_{A})^{2}\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =def.\displaystyle\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}} | CAΞ1,\displaystyle C^{\Xi\_{1}}\_{A},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖Ξ2A​(r)‖2≤\displaystyle\mathbb{E}\|\Xi\_{2}^{A}(r)\|^{2}\leq | 4​[2​‖D‖2+2​‖E‖2​(‖B†‖+R3)2​(CAΠ)2]​(CAx)2+4​‖F2†‖2​(CAx¯)2+4​‖σ‖2\displaystyle 4\big[2\|D\|^{2}+2\|E\|^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi}\_{A})^{2}\big](C^{x}\_{A})^{2}+4\|F\_{2}^{\dagger}\|^{2}(C^{\bar{x}}\_{A})^{2}+4\|\sigma\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +4​‖E‖2​[2​‖B†‖2​(CAq)2+4​(R2)2​(‖F2†‖2​(CAx¯)2+‖σ‖2)​(CAΠ)2]\displaystyle+4\|E\|^{2}\big[2\|B^{\dagger}\|^{2}(C^{q}\_{A})^{2}+4(R\_{2})^{2}(\|F\_{2}^{\dagger}\|^{2}(C^{\bar{x}}\_{A})^{2}+\|\sigma\|^{2})(C^{\Pi}\_{A})^{2}\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =def.\displaystyle\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}} | CAΞ2.\displaystyle C^{\Xi\_{2}}\_{A}. |  |

It follows from Jensen’s inequality that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(xA−x†)​(t)‖2≤\displaystyle\mathbb{E}\big\|(x^{A}-x^{\dagger})(t)\big\|^{2}\leq | ‖SA−S†‖2​𝔼​‖ξ‖2+∫0t‖(SA−S†)​(t−r)‖2​(𝔼​‖Ξ1A​(r)‖2+𝔼​‖Ξ2A​(r)‖2)​𝑑r\displaystyle\|S^{A}-S^{\dagger}\|^{2}\mathbb{E}\|\xi\|^{2}+\int\_{0}^{t}\|(S^{A}-S^{\dagger})(t-r)\|^{2}(\mathbb{E}\|\Xi\_{1}^{A}(r)\|^{2}+\mathbb{E}\|\Xi\_{2}^{A}(r)\|^{2})dr\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t‖S†​(t−r)‖2​{𝔼​‖(Ξ1A−Ξ1†)​(r)‖2+𝔼​‖(Ξ2A−Ξ2†)​(r)‖2}​𝑑r\displaystyle+\int\_{0}^{t}\|S^{\dagger}(t-r)\|^{2}\big\{\mathbb{E}\|(\Xi\_{1}^{A}-\Xi\_{1}^{\dagger})(r)\|^{2}+\mathbb{E}\|(\Xi\_{2}^{A}-\Xi\_{2}^{\dagger})(r)\|^{2}\big\}dr\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (MTA,A†)2​‖A−A†‖2​𝔼​‖ξ‖2+T​(MTA,A†)2​‖A−A†‖2​(CAΞ1+CAΞ2)\displaystyle(M^{A,A^{\dagger}}\_{T})^{2}\|A-A^{\dagger}\|^{2}\mathbb{E}\|\xi\|^{2}+T(M^{A,A^{\dagger}}\_{T})^{2}\|A-A^{\dagger}\|^{2}(C^{\Xi\_{1}}\_{A}+C^{\Xi\_{2}}\_{A})\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(MTA†)2​∫0t(CA,A†Ξ1,x+CA,A†Ξ2,x)​𝔼​|(xA−x†)​(r)|2​𝑑r\displaystyle+(M^{A^{\dagger}}\_{T})^{2}\int\_{0}^{t}(C^{\Xi\_{1},x}\_{A,A^{\dagger}}+C^{\Xi\_{2},x}\_{A,A^{\dagger}})\mathbb{E}\big|(x^{A}-x^{\dagger})(r)\big|^{2}dr\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +T(MTA,A†)2[(CA,A†Ξ1,Π+CA,A†Ξ2,Π)CA,A†Π+(CA,A†Ξ1,x¯+CA,A†Ξ2,x¯)CA,A†x¯\displaystyle+T(M^{A,A^{\dagger}}\_{T})^{2}\big[(C^{\Xi\_{1},\Pi}\_{A,A^{\dagger}}+C^{\Xi\_{2},\Pi}\_{A,A^{\dagger}})C^{\Pi}\_{A,A^{\dagger}}+(C^{\Xi\_{1},\bar{x}}\_{A,A^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{A,A^{\dagger}})C^{\bar{x}}\_{A,A^{\dagger}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(CA,A†Ξ1,q+CA,A†Ξ2,q)CA,A†q]∥A−A†∥2.\displaystyle+(C^{\Xi\_{1},q}\_{A,A^{\dagger}}+C^{\Xi\_{2},q}\_{A,A^{\dagger}})C^{q}\_{A,A^{\dagger}}\big]\|A-A^{\dagger}\|^{2}. |  |

By the Grönwall’s inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(xA−x†)​(t)‖2≤\displaystyle\mathbb{E}\big\|(x^{A}-x^{\dagger})(t)\big\|^{2}\leq | (MTA,A†)2{𝔼∥ξ∥2+T((CAΞ1)2+(CAΞ2)2)\displaystyle(M^{A,A^{\dagger}}\_{T})^{2}\big\{\mathbb{E}\|\xi\|^{2}+T((C^{\Xi\_{1}}\_{A})^{2}+(C^{\Xi\_{2}}\_{A})^{2})\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +T[(CA,A†Ξ1,Π+CA,A†Ξ2,Π)CA,A†Π+(CA,A†Ξ1,x¯+CA,A†Ξ2,x¯)CA,A†x¯\displaystyle+T\big[(C^{\Xi\_{1},\Pi}\_{A,A^{\dagger}}+C^{\Xi\_{2},\Pi}\_{A,A^{\dagger}})C^{\Pi}\_{A,A^{\dagger}}+(C^{\Xi\_{1},\bar{x}}\_{A,A^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{A,A^{\dagger}})C^{\bar{x}}\_{A,A^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(CA,A†Ξ1,q+CA,A†Ξ2,q)CA,A†q]}∥A−A†∥2exp{T(MTA†)2(CA,A†Ξ1,x+CA,A†Ξ2,x)}.\displaystyle+(C^{\Xi\_{1},q}\_{A,A^{\dagger}}+C^{\Xi\_{2},q}\_{A,A^{\dagger}})C^{q}\_{A,A^{\dagger}}\big]\big\}\|A-A^{\dagger}\|^{2}\exp\big\{T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{A,A^{\dagger}}+C^{\Xi\_{2},x}\_{A,A^{\dagger}})\big\}. |  |

∎

###### Proposition 4.7.

The equilibrium strategy uAu^{A}, associated with the perturbed operator AA, satisfies

|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖uA​(t)−u†​(t)‖2)12≤CA,A†u​‖A−A†‖,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|u^{A}(t)-u^{\dagger}(t)\big\|^{2}\big)^{\frac{1}{2}}\leq C^{u}\_{A,A^{\dagger}}\big\|A-A^{\dagger}\big\|, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CA,A†u=\displaystyle C^{u}\_{A,A^{\dagger}}= | 5{(CA,A†Π)2[(∥B†∥+R3)2(1+R5CAΠ)2(CAx)2+(R2)2(∥F2†∥CAx¯+∥σ∥)2]\displaystyle\sqrt{5}\Big\{(C^{\Pi}\_{A,A^{\dagger}})^{2}\big[(\|B^{\dagger}\|+R\_{3})^{2}(1+R\_{5}C^{\Pi}\_{A})^{2}(C^{x}\_{A})^{2}+(R\_{2})^{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{A}+\|\sigma\|)^{2}\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(CA,A†x)2(∥B†∥+R3)2(CAΠ)2+(CA,A†x¯)2(R2)2∥F2†∥2(CAΠ)2+∥B†∥2(CA,A†q)2}12.\displaystyle+(C^{x}\_{A,A^{\dagger}})^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi}\_{A})^{2}+(C^{\bar{x}}\_{A,A^{\dagger}})^{2}(R\_{2})^{2}\|F\_{2}^{\dagger}\|^{2}(C^{\Pi}\_{A})^{2}+\|B^{\dagger}\|^{2}(C^{q}\_{A,A^{\dagger}})^{2}\Big\}^{\frac{1}{2}}. |  |

###### Proof.

By ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), the equilibrium strategy for a representative agent corresponding to AA is given by

|  |  |  |
| --- | --- | --- |
|  | uA​(t)=−(KA)−1​(T−t)​[LA​(T−t)​xA​(t)+Γ2​((F2†​x¯A​(t)+σ)⋆​ΠA​(T−t))+(B†)⋆​qA​(T−t)],\displaystyle u^{A}(t)=-(K^{A})^{-1}(T-t)\big[L^{A}(T-t)x^{A}(t)+\Gamma\_{2}\big((F\_{2}^{\dagger}\bar{x}^{A}(t)+\sigma)^{\star}\Pi^{A}(T-t)\big)+(B^{\dagger})^{\star}q^{A}(T-t)\big],\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | KA​(t)=I+Δ3​(ΠA​(t)),LA​(t)=(B†)⋆​ΠA​(t)+Δ1​(ΠA​(t)).\displaystyle K^{A}(t)=I+\Delta\_{3}(\Pi^{A}(t)),\quad L^{A}(t)=(B^{\dagger})^{\star}\Pi^{A}(t)+\Delta\_{1}(\Pi^{A}(t)). |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uA−u†)​(t)=\displaystyle(u^{A}-u^{\dagger})(t)= | ((KA)−1​LA−(K†)−1​L†)​(T−t)​xA​(t)+(K†)−1​L†​(T−t)​(xA−x†)​(t)\displaystyle((K^{A})^{-1}L^{A}-(K^{\dagger})^{-1}L^{\dagger})(T-t)x^{A}(t)+(K^{\dagger})^{-1}L^{\dagger}(T-t)(x^{A}-x^{\dagger})(t)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Γ2​(F2†​(x¯A−x¯†)​(t)​ΠA​(t)+(F2†​x¯A​(t)+σ)​(ΠA−Π†)​(t))+B†​(qA−q†)​(t),\displaystyle+\Gamma\_{2}\big(F\_{2}^{\dagger}(\bar{x}^{A}-\bar{x}^{\dagger})(t)\Pi^{A}(t)+(F\_{2}^{\dagger}\bar{x}^{A}(t)+\sigma)(\Pi^{A}-\Pi^{\dagger})(t)\big)+B^{\dagger}(q^{A}-q^{\dagger})(t), |  |

we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​‖(uA−u†)​(t)‖2\displaystyle\mathbb{E}\|(u^{A}-u^{\dagger})(t)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 5​‖((KA)−1​LA−(K†)−1​L†)​(T−t)‖2​𝔼​‖xA​(t)‖2+5​‖(K†)−1​L†​(T−t)‖2​𝔼​‖(xA−x†)​(t)‖2\displaystyle 5\|((K^{A})^{-1}L^{A}-(K^{\dagger})^{-1}L^{\dagger})(T-t)\|^{2}\mathbb{E}\|x^{A}(t)\|^{2}+5\|(K^{\dagger})^{-1}L^{\dagger}(T-t)\|^{2}\mathbb{E}\|(x^{A}-x^{\dagger})(t)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +5​(R2)2​(‖F2†‖2​‖x¯A−x¯†‖C​(𝒯;H)2​‖ΠA​(t)‖2+5​‖F2†​x¯A+σ‖2​‖(ΠA−Π†)​(t)‖2)\displaystyle+5(R\_{2})^{2}\big(\|F\_{2}^{\dagger}\|^{2}\|\bar{x}^{A}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2}\|\Pi^{A}(t)\|^{2}+5\|F\_{2}^{\dagger}\bar{x}^{A}+\sigma\|^{2}\|(\Pi^{A}-\Pi^{\dagger})(t)\|^{2}\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +5​‖B†‖2​‖qA−q†‖C​(𝒯;H)2\displaystyle+5\|B^{\dagger}\|^{2}\|q^{A}-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 5​(‖B†‖+R3)2​(1+R5​CAΠ)2​‖(ΠA−Π†)​(t)‖2​𝔼​‖xA​(t)‖2+5​(‖B†‖+R3)2​(CAΠ)2​𝔼​‖(xA−x†)​(t)‖2\displaystyle 5(\|B^{\dagger}\|+R\_{3})^{2}(1+R\_{5}C^{\Pi}\_{A})^{2}\|(\Pi^{A}-\Pi^{\dagger})(t)\|^{2}\mathbb{E}\|x^{A}(t)\|^{2}+5(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi}\_{A})^{2}\mathbb{E}\|(x^{A}-x^{\dagger})(t)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +5​(R2)2​(‖F2†‖2​‖x¯A−x¯†‖C​(𝒯;H)2​(CAΠ)2+(‖F2†‖​‖x¯A‖+‖σ‖)2​‖(ΠA−Π†)​(t)‖2)\displaystyle+5(R\_{2})^{2}\big(\|F\_{2}^{\dagger}\|^{2}\|\bar{x}^{A}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2}(C^{\Pi}\_{A})^{2}+(\|F\_{2}^{\dagger}\|\|\bar{x}^{A}\|+\|\sigma\|)^{2}\|(\Pi^{A}-\Pi^{\dagger})(t)\|^{2}\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +5​‖B†‖2​‖qA−q†‖C​(𝒯;H)2.\displaystyle+5\|B^{\dagger}\|^{2}\|q^{A}-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}.\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 5​(‖B†‖+R3)2​(1+R5​CA†Π)2​(CA,A†Π)2​‖A−A†‖2​(CAx)2+5​(‖B†‖+R3)2​(CA†Π)2​(CA,A†x)2​‖A−A†‖2\displaystyle 5(\|B^{\dagger}\|+R\_{3})^{2}(1+R\_{5}C^{\Pi}\_{A^{\dagger}})^{2}(C^{\Pi}\_{A,A^{\dagger}})^{2}\|A-A^{\dagger}\|^{2}(C^{x}\_{A})^{2}+5(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi}\_{A^{\dagger}})^{2}(C^{x}\_{A,A^{\dagger}})^{2}\|A-A^{\dagger}\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +5​(R2)2​[‖F2†‖2​(CA,A†x¯)2​(CAΠ)2+5​(‖F2†‖​‖x¯†‖+‖σ‖)2​(CA,A†Π)2]​‖A−A†‖2\displaystyle+5(R\_{2})^{2}\big[\|F\_{2}^{\dagger}\|^{2}(C^{\bar{x}}\_{A,A^{\dagger}})^{2}(C^{\Pi}\_{A})^{2}+5(\|F\_{2}^{\dagger}\|\|\bar{x}^{\dagger}\|+\|\sigma\|)^{2}(C^{\Pi}\_{A,A^{\dagger}})^{2}\big]\|A-A^{\dagger}\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +5​‖B†‖2​(CA,A†q)2​‖A−A†‖2.\displaystyle+5\|B^{\dagger}\|^{2}(C^{q}\_{A,A^{\dagger}})^{2}\|A-A^{\dagger}\|^{2}. |  |

The desired bound for (supt∈𝒯𝔼​‖uA​(t)−u†​(t)‖2)12\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|u^{A}(t)-u^{\dagger}(t)\big\|^{2}\big)^{\frac{1}{2}} then follows.
∎

### 4.2 Stability of the equilibrium with respect to operator BB

In this subsection, we perturb the parameter B†B^{\dagger} to BB and denote by (ΠB,x¯B,qB,uB,xB)(\Pi^{B},\bar{x}^{B},q^{B},u^{B},x^{B}) the solution to the MFG system, given by ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), corresponding to the set of rules (A†(A^{\dagger}, BB, DD, EE, F1F\_{1}, F2†F\_{2}^{\dagger}, σ\sigma, MM, F^1\widehat{F}\_{1}, F^2\widehat{F}\_{2}, G)G).

###### Lemma 4.8.

For all t∈𝒯t\in\mathcal{T}, the solution ΠB\Pi^{B} of the operator differential Riccati equation, associated with the perturbed operator BB, satisfies

|  |  |  |
| --- | --- | --- |
|  | ‖ΠB​(t)‖≤CBΠ,\displaystyle\big\|\Pi^{B}(t)\big\|\leq C^{\Pi}\_{B},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | ‖ΠB​(t)−Π†​(t)‖≤CB,B†Π,1​‖B−B†‖+CB,B†Π,2​‖B−B†‖2,\displaystyle\big\|\Pi^{B}(t)-\Pi^{\dagger}(t)\big\|\leq C^{\Pi,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|+C^{\Pi,2}\_{B,B^{\dagger}}\|B-B^{\dagger}\|^{2}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CBΠ=\displaystyle C^{\Pi}\_{B}= | 2​(MTA†)2​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))​(‖G‖+T​‖M‖),\displaystyle 2(M^{A^{\dagger}}\_{T})^{2}\exp\big(8T(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big(\|G\|+T\|M\|\big),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Π,1=\displaystyle C^{\Pi,1}\_{B,B^{\dagger}}= | T​exp⁡{12​(MTA†)2​(1+‖D‖2)​T}​2​MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))\displaystyle\sqrt{T}\exp\Big\{\frac{1}{2}(M^{A^{\dagger}}\_{T})^{2}(1+\|D\|^{2})T\Big\}\sqrt{2}M^{A^{\dagger}}\_{T}\exp\big(8T(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×2​(‖M‖​T+‖G‖)​exp⁡{(‖B†‖+R3+R5)​T​[2​MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))]},\displaystyle\times 2(\|M\|T+\|G\|)\exp\Big\{(\|B^{\dagger}\|+R\_{3}+R\_{5})T\big[\sqrt{2}M^{A^{\dagger}}\_{T}\exp\big(8T(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big]\Big\},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Π,2=\displaystyle C^{\Pi,2}\_{B,B^{\dagger}}= | T​exp⁡{12​(MTA†)2​(1+‖D‖2)​T}​2​MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))\displaystyle\sqrt{T}\exp\Big\{\frac{1}{2}(M^{A^{\dagger}}\_{T})^{2}(1+\|D\|^{2})T\Big\}\sqrt{2}M^{A^{\dagger}}\_{T}\exp\big(8T(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×{(‖B‖+‖B†‖+2​R3)​T​(‖B†‖+R3)​(CΠ†)3​‖B−B†‖}\displaystyle\times\Big\{(\|B\|+\|B^{\dagger}\|+2R\_{3})T(\|B^{\dagger}\|+R\_{3})(C^{\Pi^{\dagger}})^{3}\|B-B^{\dagger}\|\Big\}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{(‖B†‖+R3+R5)​T​[2​MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))]}.\displaystyle\times\exp\Big\{(\|B^{\dagger}\|+R\_{3}+R\_{5})T\big[\sqrt{2}M^{A^{\dagger}}\_{T}\exp\big(8T(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big]\Big\}. |  |

###### Proof.

See [A.5.1](https://arxiv.org/html/2510.20017v1#A1.SS5.SSS1 "A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Lemma 4.9.

Suppose that

|  |  |  |
| --- | --- | --- |
|  | MTA†​(CBΨ,x¯​T+‖G‖​‖F^2‖)<1,\displaystyle M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}}\_{B}T+\|G\|\|\widehat{F}\_{2}\|)<1,\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | (MTA†​CB,B†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​MTA†​CB,B†Φ,q​T​exp⁡(MTA†​(CB,B†Φ,x¯+CB,B†Ψ,q)​T)<1.\displaystyle(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{B,B^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|)M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{B,B^{\dagger}}T\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{B,B^{\dagger}}+C^{\Psi,q}\_{B,B^{\dagger}})T\big)<1. |  |

Then, the offset term qBq^{B} and the mean field x¯B\bar{x}^{B}, corresponding to the perturbed operator BB, satisfy

|  |  |  |
| --- | --- | --- |
|  | ‖x¯B‖C​(𝒯;ℋ)≤CBx¯,\displaystyle\big\|\bar{x}^{B}\big\|\_{C(\cal{T};\cal{H})}\leq C^{\bar{x}}\_{B},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | ‖qB‖C​(𝒯;ℋ)≤CBq,\displaystyle\big\|q^{B}\big\|\_{C(\cal{T};\cal{H})}\leq C^{q}\_{B},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | ‖x¯B−x¯†‖C​(𝒯;H)≤CB,B†x¯,1​‖B−B†‖+CB,B†x¯,2​‖B−B†‖2,\displaystyle\big\|\bar{x}^{B}-\bar{x}^{\dagger}\big\|\_{C(\mathcal{T};H)}\leq C^{\bar{x},1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|+C^{\bar{x},2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|^{2},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | ‖qB−q†‖C​(𝒯;H)≤CB,B†q,1​‖B−B†‖+CB,B†q,2​‖B−B†‖2,\displaystyle\big\|q^{B}-q^{\dagger}\big\|\_{C(\mathcal{T};H)}\leq C^{q,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|+C^{q,2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|^{2}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†x¯,1=\displaystyle C^{\bar{x},1}\_{B,B^{\dagger}}= | [1−(MTA†​CB,B†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​MTA†​CB,B†Φ,q​T​exp⁡(MTA†​(CB,B†Φ,x¯+CB,B†Ψ,q)​T)]−1\displaystyle\big[1-(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{B,B^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|)M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{B,B^{\dagger}}T\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{B,B^{\dagger}}+C^{\Psi,q}\_{B,B^{\dagger}})T\big)\big]^{-1}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[MTA†(CB,B†Φ,ΠCB,B†Π,1+CB,B†Φ,c)Texp(MTA†CB,B†Φ,x¯T)\displaystyle\times\hskip-0.85355pt\Big[M^{A^{\dagger}}\_{T}\big(C^{\Phi,\Pi}\_{B,B^{\dagger}}C^{\Pi,1}\_{B,B^{\dagger}}+C^{\Phi,c}\_{B,B^{\dagger}}\big)T\exp\big(M^{A^{\dagger}}\_{T}C^{\Phi,\bar{x}}\_{B,B^{\dagger}}T\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +MTA†CB,B†Φ,qTMTA†(CB,B†Ψ,ΠCB,B†Π,1+CB,B†Ψ,c)Texp(MTA†(CB,B†Φ,x¯+CB,B†Ψ,q)T)],\displaystyle+M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{B,B^{\dagger}}TM^{A^{\dagger}}\_{T}\big(C^{\Psi,\Pi}\_{B,B^{\dagger}}C^{\Pi,1}\_{B,B^{\dagger}}+C^{\Psi,c}\_{B,B^{\dagger}}\big)T\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{B,B^{\dagger}}+C^{\Psi,q}\_{B,B^{\dagger}})T\big)\Big],\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†x¯,2=\displaystyle C^{\bar{x},2}\_{B,B^{\dagger}}= | [1−(MTA†​CB,B†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​MTA†​CB,B†Φ,q​T​exp⁡(MTA†​(CB,B†Φ,x¯+CB,B†Ψ,q)​T)]−1\displaystyle\big[1-(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{B,B^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|)M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{B,B^{\dagger}}T\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{B,B^{\dagger}}+C^{\Psi,q}\_{B,B^{\dagger}})T\big)\big]^{-1}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[MTA†(CB,B†Φ,ΠCB,B†Π,2)Texp(MTA†CB,B†Φ,x¯T)\displaystyle\times\hskip-0.85355pt\Big[M^{A^{\dagger}}\_{T}\big(C^{\Phi,\Pi}\_{B,B^{\dagger}}C^{\Pi,2}\_{B,B^{\dagger}}\big)T\exp\big(M^{A^{\dagger}}\_{T}C^{\Phi,\bar{x}}\_{B,B^{\dagger}}T\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +MTA†CB,B†Φ,qTMTA†(CB,B†Ψ,ΠCB,B†Π,2)Texp(MTA†(CB,B†Φ,x¯+CB,B†Ψ,q)T)],\displaystyle+M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{B,B^{\dagger}}TM^{A^{\dagger}}\_{T}\big(C^{\Psi,\Pi}\_{B,B^{\dagger}}C^{\Pi,2}\_{B,B^{\dagger}}\big)T\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{B,B^{\dagger}}+C^{\Psi,q}\_{B,B^{\dagger}})T\big)\Big],\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†q,1=\displaystyle C^{q,1}\_{B,B^{\dagger}}= | MTA†​(CB,B†Ψ,Π​CB,B†Π,1+CB,B†Ψ,c)​T​exp⁡(MTA†​CB,B†Ψ,q​T)\displaystyle M^{A^{\dagger}}\_{T}\big(C^{\Psi,\Pi}\_{B,B^{\dagger}}C^{\Pi,1}\_{B,B^{\dagger}}+C^{\Psi,c}\_{B,B^{\dagger}}\big)T\exp\big(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{B,B^{\dagger}}T\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(MTA†​CB,B†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​exp⁡(MTA†​CB,B†Ψ,q​T)​CB,B†x¯,1,\displaystyle+(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{B,B^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|)\exp\big(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{B,B^{\dagger}}T\big)C^{\bar{x},1}\_{B,B^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†q,2=\displaystyle C^{q,2}\_{B,B^{\dagger}}= | MTA†​(CB,B†Ψ,Π​CB,B†Π,2)​T​exp⁡(MTA†​CB,B†Ψ,q​T)\displaystyle M^{A^{\dagger}}\_{T}\big(C^{\Psi,\Pi}\_{B,B^{\dagger}}C^{\Pi,2}\_{B,B^{\dagger}}\big)T\exp\big(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{B,B^{\dagger}}T\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(MTA†​CB,B†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​exp⁡(MTA†​CB,B†Ψ,q​T)​CB,B†x¯,2,\displaystyle+(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{B,B^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|)\exp\big(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{B,B^{\dagger}}T\big)C^{\bar{x},2}\_{B,B^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Φ,x¯=\displaystyle C^{\Phi,\bar{x}}\_{B,B^{\dagger}}= | ‖B‖​(‖B‖+R3)​CBΠ+‖B‖​R2​‖F2†‖​CΠ†+‖F1‖,\displaystyle\|B\|(\|B\|+R\_{3})C^{\Pi}\_{B}+\|B\|R\_{2}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}+\|F\_{1}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Φ,q=\displaystyle C^{\Phi,q}\_{B,B^{\dagger}}= | ‖B‖2,\displaystyle\|B\|^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Φ,Π=\displaystyle C^{\Phi,\Pi}\_{B,B^{\dagger}}= | ‖B‖​(R5+‖B‖+R3)​CBx¯+‖B‖​R2​(‖F2†‖​CBx¯+‖σ‖),\displaystyle\|B\|\big(R\_{5}+\|B\|+R\_{3}\big)C^{\bar{x}}\_{B}+\|B\|R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{B}+\|\sigma\|),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Φ,c=\displaystyle C^{\Phi,c}\_{B,B^{\dagger}}= | (‖B†‖+R3)​CΠ†​Cx¯†+‖B‖​CΠ†​Cx¯†+(‖B‖+‖B†‖)​Cq†+R2​((‖F2†‖​Cx¯†+‖σ‖)​CΠ†),\displaystyle(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}C^{\bar{x}^{\dagger}}+\|B\|C^{\Pi^{\dagger}}C^{\bar{x}^{\dagger}}+(\|B\|+\|B^{\dagger}\|)C^{q^{\dagger}}+R\_{2}\big((\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}\big),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ψ,x¯=\displaystyle C^{\Psi,\bar{x}}\_{B,B^{\dagger}}= | R1​‖F2†‖​CΠ†+(‖B‖+R3)​R2​‖F2†‖​CΠ†+(CBΠ​‖F1‖+‖M‖​‖F^1‖),\displaystyle R\_{1}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}+(\|B\|+R\_{3})R\_{2}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}+(C^{\Pi}\_{B}\|F\_{1}\|+\|M\|\|\widehat{F}\_{1}\|),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ψ,q=\displaystyle C^{\Psi,q}\_{B,B^{\dagger}}= | (‖B‖+R3)​CBΠ​‖B‖,\displaystyle(\|B\|+R\_{3})C^{\Pi}\_{B}\|B\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ψ,Π=\displaystyle C^{\Psi,\Pi}\_{B,B^{\dagger}}= | (‖B‖+R3)​‖B†‖​Cq†+(‖B‖+R3)​CBΠ​R5​‖B†‖​Cq†+R1​(‖F2†‖​Cx¯†+‖σ‖)\displaystyle(\|B\|+R\_{3})\|B^{\dagger}\|C^{q^{\dagger}}+(\|B\|+R\_{3})C^{\Pi}\_{B}R\_{5}\|B^{\dagger}\|C^{q^{\dagger}}+R\_{1}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(‖B‖+R3)​R2​(‖F2†‖​Cx¯†+‖σ‖)+(‖B‖+R3)​CBΠ​R5​R2​(‖F2†‖​Cx¯†+‖σ‖)​CΠ†\displaystyle+(\|B\|+R\_{3})R\_{2}\big(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|\big)+(\|B\|+R\_{3})C^{\Pi}\_{B}R\_{5}R\_{2}\big(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|\big)C^{\Pi^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(‖B‖+R3)​CBΠ​R2​(‖F2†‖​CBx¯+‖σ‖)+‖F1‖​Cx¯†\displaystyle+(\|B\|+R\_{3})C^{\Pi}\_{B}R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{B}+\|\sigma\|)+\|F\_{1}\|C^{\bar{x}^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ψ,c=\displaystyle C^{\Psi,c}\_{B,B^{\dagger}}= | CΠ†​‖B†‖​Cq†+(‖B‖+R3)​CΠ†​Cq†+CΠ†​R2​(‖F2†‖​Cx¯†+‖σ‖)​CΠ†,\displaystyle C^{\Pi^{\dagger}}\|B^{\dagger}\|C^{q^{\dagger}}+(\|B\|+R\_{3})C^{\Pi^{\dagger}}C^{q^{\dagger}}+C^{\Pi^{\dagger}}R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBx¯=\displaystyle C^{\bar{x}}\_{B}= | [1−MTA†​(CBΨ,x¯​T+‖G‖​‖F^2‖)]−1\displaystyle\big[1-M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}}\_{B}T+\|G\|\|\widehat{F}\_{2}\|)\big]^{-1}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[MTA†​(CBΦ,c​T+|ξ¯|)​exp⁡(MTA†​CBΦ,x¯​T)+MTA†​CBΦ,q​T​(MTA†​CBΨ,c​T)​exp⁡(MTA†​(CBΦ,x¯+CBΨ,q)​T)],\displaystyle\!\!\times\!\!\big[M^{A^{\dagger}}\_{T}(C^{\Phi,c}\_{B}T+|\bar{\xi}|)\exp(M^{A^{\dagger}}\_{T}C^{\Phi,\bar{x}}\_{B}T)+M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{B}T\big(M^{A^{\dagger}}\_{T}C^{\Psi,c}\_{B}T\big)\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{B}+C^{\Psi,q}\_{B})T\big)\big],\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBq=\displaystyle C^{q}\_{B}= | MTA†​CBΨ,c​T​exp⁡(MTA†​CBΨ,q​T)+MTA†​(CBΨ,x¯​T+‖G‖​‖F^2‖)​exp⁡(MTA†​CBΨ,q​T)​CBx¯,\displaystyle M^{A^{\dagger}}\_{T}C^{\Psi,c}\_{B}T\exp(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{B}T)+M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}}\_{B}T+\|G\|\|\widehat{F}\_{2}\|)\exp(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{B}T)C^{\bar{x}}\_{B},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBΦ,x¯=\displaystyle C^{\Phi,\bar{x}}\_{B}= | ‖B‖​(‖B‖+R3+R2​‖F2†‖)​CBΠ+‖F1‖,\displaystyle\|B\|(\|B\|+R\_{3}+R\_{2}\|F\_{2}^{\dagger}\|)C^{\Pi}\_{B}+\|F\_{1}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBΦ,q=\displaystyle C^{\Phi,q}\_{B}= | ‖B‖2,\displaystyle\|B\|^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBΦ,c=\displaystyle C^{\Phi,c}\_{B}= | R2​‖B‖​‖σ‖​CΠ†,\displaystyle R\_{2}\|B\|\|\sigma\|C^{\Pi^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBΨ,q=\displaystyle C^{\Psi,q}\_{B}= | CBΠ​(‖B‖+R3)​‖B‖,\displaystyle C^{\Pi}\_{B}(\|B\|+R\_{3})\big\|B\big\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBΨ,x¯=\displaystyle C^{\Psi,\bar{x}}\_{B}= | [R1​CBΠ+(CBΠ)2​(‖B‖+R3)​R2]​‖F2†‖+CBΠ​‖F1‖+‖M‖​‖F^1‖,\displaystyle\big[R\_{1}C^{\Pi}\_{B}+(C^{\Pi}\_{B})^{2}(\|B\|+R\_{3})R\_{2}\big]\big\|F\_{2}^{\dagger}\big\|+C^{\Pi}\_{B}\big\|F\_{1}\big\|+\big\|M\big\|\big\|\widehat{F}\_{1}\big\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CBΨ,c=\displaystyle C^{\Psi,c}\_{B}= | R1​CBΠ+(CBΠ)2​(‖B‖+R3)​R2.\displaystyle R\_{1}C^{\Pi}\_{B}+(C^{\Pi}\_{B})^{2}(\|B\|+R\_{3})R\_{2}. |  |

###### Proof.

See [A.5.2](https://arxiv.org/html/2510.20017v1#A1.SS5.SSS2 "A.5.2 Proof of Lemma 4.9 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Lemma 4.10.

The equilibrium state xBx^{B}, associated with the perturbed operator BB, satisfies

|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖xB​(t)‖2)12≤CBx,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|x^{B}(t)\|^{2}\big)^{\frac{1}{2}}\leq C^{x}\_{B},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖(xB−x†)​(t)‖2)12≤CB,B†x,1​‖B−B†‖+CB,B†x,2​‖B−B†‖2,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|(x^{B}-x^{\dagger})(t)\|^{2}\big)^{\frac{1}{2}}\leq C^{x,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|+C^{x,2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|^{2}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CBx=\displaystyle C^{x}\_{B}= | {3(MTA†)2𝔼∥ξ∥2+3T(MTA†)2\displaystyle\big\{3(M^{A^{\dagger}}\_{T})^{2}\mathbb{E}\|\xi\|^{2}+3T(M\_{T}^{A^{\dagger}})^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[(‖B‖2+‖E‖2)​(‖B‖​CBq+R2​(‖F2†‖​CBx¯+‖σ‖)​CΠ†)]\displaystyle\times\big[(\|B\|^{2}+\|E\|^{2})\big(\|B\|C^{q}\_{B}+R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{B}+\|\sigma\|)C^{\Pi^{\dagger}}\big)\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3T(MTA†)2(∥F1∥2+∥F2†∥2)(CBx¯)2+3T(MTA†)2∥σ∥2}1/2\displaystyle+3T(M^{A^{\dagger}}\_{T})^{2}(\|F\_{1}\|^{2}+\|F\_{2}^{\dagger}\|^{2})(C^{\bar{x}}\_{B})^{2}+3T(M^{A^{\dagger}}\_{T})^{2}\|\sigma\|^{2}\big\}^{1/2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{(MTA†)2​[(‖B‖2+‖E‖2)​((‖B‖+R3)​CΠ†)2+‖D‖2]​3​T/2},\displaystyle\times\exp\big\{(M^{A^{\dagger}}\_{T})^{2}\big[(\|B\|^{2}+\|E\|^{2})\big((\|B\|+R\_{3})C^{\Pi^{\dagger}}\big)^{2}+\|D\|^{2}\big]3T/2\big\},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†x,1=\displaystyle C\_{B,B^{\dagger}}^{x,1}= | T1/2MTA†3[(CB,B†Ξ1,x¯+CB,B†Ξ2,x¯)1/2CB,B†x¯,1+(CB,B†Ξ1,q+CB,B†Ξ2,q)1/2CB,B†q,1\displaystyle T^{1/2}M^{A^{\dagger}}\_{T}\sqrt{3}\Big[\big(C^{\Xi\_{1},\bar{x}}\_{B,B^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{B,B^{\dagger}}\big)^{1/2}C^{\bar{x},1}\_{B,B^{\dagger}}+\big(C^{\Xi\_{1},q}\_{B,B^{\dagger}}+C^{\Xi\_{2},q}\_{B,B^{\dagger}}\big)^{1/2}C^{q,1}\_{B,B^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(CB,B†Ξ1,c+CB,B†Ξ2,c)1/2]exp{T(MTA†)2(CB,B†Ξ1,x+CB,B†Ξ2,x)/2},\displaystyle+\big(C^{\Xi\_{1},c}\_{B,B^{\dagger}}+C^{\Xi\_{2},c}\_{B,B^{\dagger}}\big)^{1/2}\Big]\exp\Big\{T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{B,B^{\dagger}}+C^{\Xi\_{2},x}\_{B,B^{\dagger}})/2\Big\},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†x,2=\displaystyle C\_{B,B^{\dagger}}^{x,2}= | T1/2​MTA†​3​[(CB,B†Ξ1,x¯+CB,B†Ξ2,x¯)1/2​CB,B†x¯,2+(CB,B†Ξ1,q+CB,B†Ξ2,q)1/2​CB,B†q,2]\displaystyle T^{1/2}M^{A^{\dagger}}\_{T}\sqrt{3}\Big[\big(C^{\Xi\_{1},\bar{x}}\_{B,B^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{B,B^{\dagger}}\big)^{1/2}C^{\bar{x},2}\_{B,B^{\dagger}}+\big(C^{\Xi\_{1},q}\_{B,B^{\dagger}}+C^{\Xi\_{2},q}\_{B,B^{\dagger}}\big)^{1/2}C^{q,2}\_{B,B^{\dagger}}\Big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{T​(MTA†)2​(CB,B†Ξ1,x+CB,B†Ξ2,x)/2},\displaystyle\times\exp\Big\{T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{B,B^{\dagger}}+C^{\Xi\_{2},x}\_{B,B^{\dagger}})/2\Big\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ1,x=\displaystyle\allowdisplaybreaks C^{\Xi\_{1},x}\_{B,B^{\dagger}}= | 5​[(‖B‖+R3)​CΠ†]2,\displaystyle 5\big[(\|B\|+R\_{3})C^{\Pi^{\dagger}}\big]^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ1,Π=\displaystyle C^{\Xi\_{1},\Pi}\_{B,B^{\dagger}}= | 5[∥B∥R5(∥B†∥+R3)CΠ†Cx†+∥B∥(∥B∥+R3)Cx†+∥B∥R5∥B†∥Cq†\displaystyle 5\big[\|B\|R\_{5}(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}C^{x^{\dagger}}+\|B\|(\|B\|+R\_{3})C^{x^{\dagger}}+\|B\|R\_{5}\|B^{\dagger}\|C^{q^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∥B∥R2(∥F2†∥CBx¯+∥σ∥)]2,\displaystyle+\|B\|R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{B}+\|\sigma\|)\big]^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ1,x¯=\displaystyle C^{\Xi\_{1},\bar{x}}\_{B,B^{\dagger}}= | 5​[‖B‖​R2​‖F2†‖​CΠ†+‖F1‖]2,\displaystyle 5\big[\|B\|R\_{2}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}+\|F\_{1}\|\big]^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ1,q=\displaystyle C^{\Xi\_{1},q}\_{B,B^{\dagger}}= | 5​‖B‖4,\displaystyle 5\|B\|^{4},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ1,c=\displaystyle C^{\Xi\_{1},c}\_{B,B^{\dagger}}= | 5[(∥B†∥+R3)CΠ†Cx†+∥B∥R5(∥B†∥+R3)CΠ†Cx†+∥B∥2Cx†\displaystyle 5\big[(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}C^{x^{\dagger}}+\|B\|R\_{5}(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}C^{x^{\dagger}}+\|B\|^{2}C^{x^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∥B†∥Cq†+∥B∥R5∥B†∥Cq†+∥B∥Cq†+R2(∥F2†∥Cx¯†+∥σ∥)CΠ†]2,\displaystyle+\|B^{\dagger}\|C^{q^{\dagger}}+\|B\|R\_{5}\|B^{\dagger}\|C^{q^{\dagger}}+\|B\|C^{q^{\dagger}}+R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}\big]^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ2,x=\displaystyle C^{\Xi\_{2},x}\_{B,B^{\dagger}}= | 5​[‖D‖+‖E‖​(‖B†‖+R3)]2,\displaystyle 5\big[\|D\|+\|E\|(\|B^{\dagger}\|+R\_{3})\big]^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ2,Π=\displaystyle C^{\Xi\_{2},\Pi}\_{B,B^{\dagger}}= | 5[∥E∥R5(∥B†∥+R3)CΠ†Cx†+∥E∥(∥B∥+R3)Cx†\displaystyle 5\big[\|E\|R\_{5}(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}C^{x^{\dagger}}+\|E\|(\|B\|+R\_{3})C^{x^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∥E∥R5∥B†∥Cq†+∥E∥R5R2(∥F2†∥Cx¯†+∥σ∥)CΠ†+∥E∥R2(∥F2†∥Cx¯†+∥σ∥)]2,\displaystyle+\|E\|R\_{5}\|B^{\dagger}\|C^{q^{\dagger}}+\|E\|R\_{5}R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}+\|E\|R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)\big]^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ2,x¯=\displaystyle C^{\Xi\_{2},\bar{x}}\_{B,B^{\dagger}}= | 5​[‖B‖​R2​‖F2†‖​CΠ†]2,\displaystyle 5\big[\|B\|R\_{2}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}\big]^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ2,q=\displaystyle C^{\Xi\_{2},q}\_{B,B^{\dagger}}= | 5​(‖E‖​‖B‖)2,\displaystyle 5\big(\|E\|\|B\|\big)^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†Ξ2,c=\displaystyle C^{\Xi\_{2},c}\_{B,B^{\dagger}}= | 5​(‖E‖​CΠ†​Cx†+‖E‖​Cq†)2.\displaystyle 5(\|E\|C^{\Pi^{\dagger}}C^{x^{\dagger}}+\|E\|C^{q^{\dagger}})^{2}. |  |

###### Proof.

See [A.5.3](https://arxiv.org/html/2510.20017v1#A1.SS5.SSS3 "A.5.3 Proof of Lemma 4.10 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Proposition 4.11.

The equilibrium strategy uBu^{B}, associated with the perturbed operator BB, satisfies

|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖uB​(t)−u†​(t)‖2)12≤CB,B†u,1​‖B−B†‖+CB,B†u,2​‖B−B†‖2,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|u^{B}(t)-u^{\dagger}(t)\big\|^{2}\big)^{\frac{1}{2}}\leq C^{u,1}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|+C^{u,2}\_{B,B^{\dagger}}\big\|B-B^{\dagger}\big\|^{2}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†u,1=\displaystyle C^{u,1}\_{B,B^{\dagger}}= | 6​[(‖B†‖+R3)​(1+R5​CBΠ)​Cx†+6​R2​(‖F2†‖​CBx¯+‖σ‖)]​CB,B†Π,1\displaystyle 6\big[(\|B^{\dagger}\|+R\_{3})(1+R\_{5}C^{\Pi}\_{B})C^{x^{\dagger}}+6R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{B}+\|\sigma\|)\big]C^{\Pi,1}\_{B,B^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​(‖B†‖+R3)​CBΠ​CB,B†x,1+6​R2​‖F2†‖​CΠ†​CB,B†x¯,1+6​Cq†+6​‖B‖​CB,B†q,1,\displaystyle+6(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{B}C^{x,1}\_{B,B^{\dagger}}+6R\_{2}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}C^{\bar{x},1}\_{B,B^{\dagger}}+6C^{q^{\dagger}}+6\|B\|C^{q,1}\_{B,B^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CB,B†u,2=\displaystyle C^{u,2}\_{B,B^{\dagger}}= | 6​[(‖B†‖+R3)​(1+R5​CBΠ)​Cx†+R2​(‖F2†‖​CBx¯+‖σ‖)]​CB,B†Π,2\displaystyle 6\big[(\|B^{\dagger}\|+R\_{3})(1+R\_{5}C^{\Pi}\_{B})C^{x^{\dagger}}+R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{B}+\|\sigma\|)\big]C^{\Pi,2}\_{B,B^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​(‖B†‖+R3)​CBΠ​CB,B†x,2+6​R2​‖F2†‖​CΠ†​CB,B†x¯,2+6​‖B‖​CB,B†q,2.\displaystyle+6(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{B}C^{x,2}\_{B,B^{\dagger}}+6R\_{2}\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}C^{\bar{x},2}\_{B,B^{\dagger}}+6\|B\|C^{q,2}\_{B,B^{\dagger}}. |  |

###### Proof.

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uB−u†)​(t)=\displaystyle(u^{B}-u^{\dagger})(t)= | ((KB)−1​LB−(K†)−1​L†)​(T−t)​xB​(t)+(K†)−1​L†​(T−t)​(xB−x†)​(t)\displaystyle((K^{B})^{-1}L^{B}-(K^{\dagger})^{-1}L^{\dagger})(T-t)x^{B}(t)+(K^{\dagger})^{-1}L^{\dagger}(T-t)(x^{B}-x^{\dagger})(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Γ2​(F2†​(x¯B−x¯†)​(t)​Π†​(t)+(F2†​x¯†​(t)+σ)​(ΠB−Π†)​(T−t))\displaystyle+\Gamma\_{2}\big(F\_{2}^{\dagger}(\bar{x}^{B}-\bar{x}^{\dagger})(t)\Pi^{\dagger}(t)+(F\_{2}^{\dagger}\bar{x}^{\dagger}(t)+\sigma)(\Pi^{B}-\Pi^{\dagger})(T-t)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(B−B†)​q†​(T−t)+B​(q−q†)​(T−t),\displaystyle+(B-B^{\dagger})q^{\dagger}(T-t)+B(q-q^{\dagger})(T-t), |  |

we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(uB−u†)​(t)‖2≤\displaystyle\mathbb{E}\big\|(u^{B}-u^{\dagger})(t)\big\|^{2}\leq | 6​‖((KB)−1​LB−(K†)−1​L†)​(T−t)‖2​𝔼​‖xB​(t)‖2\displaystyle 6\|((K^{B})^{-1}L^{B}-(K^{\dagger})^{-1}L^{\dagger})(T-t)\|^{2}\mathbb{E}\|x^{B}(t)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​‖(K†)−1​L†​(T−t)‖2​𝔼​‖(xB−x†)​(t)‖2\displaystyle+6\|(K^{\dagger})^{-1}L^{\dagger}(T-t)\|^{2}\,\mathbb{E}\|(x^{B}-x^{\dagger})(t)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​(R2)2​(‖F2†‖2​‖x¯B−x¯†‖C​(𝒯;H)2​‖Π†​(t)‖2+‖F2†​x¯†+σ‖2​‖(ΠB−Π†)​(t)‖2)\displaystyle+6(R\_{2})^{2}\big(\|F\_{2}^{\dagger}\|^{2}\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2}\|\Pi^{\dagger}(t)\|^{2}+\|F\_{2}^{\dagger}\bar{x}^{\dagger}+\sigma\|^{2}\|(\Pi^{B}-\Pi^{\dagger})(t)\|^{2}\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​‖B−B†‖2​‖q†‖C​(𝒯;H)2+6​‖B‖2​‖q−q†‖C​(𝒯;H)2.\displaystyle+6\|B-B^{\dagger}\|^{2}\|q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+6\|B\|^{2}\|q-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}. |  |

Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (supt∈𝒯𝔼​‖(uB−u†)​(t)‖2)12≤\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|(u^{B}-u^{\dagger})(t)\big\|^{2}\big)^{\frac{1}{2}}\leq | 6​(‖B†‖+R3)​(1+R5​CBΠ)​‖(ΠB−Π†)​(t)‖​(supt∈𝒯𝔼​‖xB​(t)‖2)12\displaystyle 6(\|B^{\dagger}\|+R\_{3})(1+R\_{5}C^{\Pi}\_{B})\|(\Pi^{B}-\Pi^{\dagger})(t)\|\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|x^{B}(t)\|^{2}\big)^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​(‖B†‖+R3)​CBΠ​(supt∈𝒯𝔼​‖(xB−x†)​(t)‖2)12\displaystyle+6(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{B}\,\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|(x^{B}-x^{\dagger})(t)\|^{2}\big)^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​R2​(‖F2†‖​‖x¯B−x¯†‖C​(𝒯;H)​CΠ†+(‖F2†‖​CBx¯+‖σ‖)​‖(ΠB−Π†)​(t)‖)\displaystyle+6R\_{2}\big(\|F\_{2}^{\dagger}\|\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}C^{\Pi^{\dagger}}+(\|F\_{2}^{\dagger}\|C^{\bar{x}}\_{B}+\|\sigma\|)\|(\Pi^{B}-\Pi^{\dagger})(t)\|\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +6​‖B−B†‖​‖q†‖C​(𝒯;H)+6​‖B‖​‖qB−q†‖C​(𝒯;H).\displaystyle+6\|B-B^{\dagger}\|\|q^{\dagger}\|\_{C(\mathcal{T};H)}+6\|B\|\|q^{B}-q^{\dagger}\|\_{C(\mathcal{T};H)}. |  |

The desired estimate then follows.
∎

### 4.3 Stability of the equilibrium with respect to operator F2F\_{2}

In this subsection, we perturb the parameter F2†F\_{2}^{\dagger} to F2F\_{2} and denote by (ΠF2,x¯F2,qF2,uF2,xF2)(\Pi^{F\_{2}},\bar{x}^{F\_{2}},q^{F\_{2}},u^{F\_{2}},x^{F\_{2}}) the solution to the MFG system, given by ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), corresponding to the set of rules (A†(A^{\dagger}, B†B^{\dagger}, DD, EE, F1F\_{1}, F2F\_{2}, σ\sigma, MM, F^1\widehat{F}\_{1}, F^2\widehat{F}\_{2}, G)G).
From ([A.7](https://arxiv.org/html/2510.20017v1#A1.E7 "Equation A.7 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), the Riccati operator Π​(t)\Pi(t) is independent of F2F\_{2}. Hence, we have
ΠF2​(t)=Π†​(t),∀t∈𝒯\Pi^{F\_{2}}(t)=\Pi^{\dagger}(t),\,\forall t\in\mathcal{T}.

###### Lemma 4.12.

Suppose that

|  |  |  |
| --- | --- | --- |
|  | MTA†​(CF2Ψ,x¯​T+‖G‖​‖F^2‖)<1,\displaystyle M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}}\_{F\_{2}}T+\|G\|\|\widehat{F}\_{2}\|)<1, |  |
|  |  |  |
| --- | --- | --- |
|  | (MTA†​CF2,F2†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​MTA†​CF2,F2†Φ,q​T​exp⁡[MTA†​(CF2,F2†Φ,x¯+CF2,F2†Ψ,q)​T]<1,\displaystyle\big(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|\big)M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{F\_{2},F\_{2}^{\dagger}}T\exp\big[M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}})T\big]<1, |  |

Then, the offset term qF2q^{F\_{2}} and the mean field x¯F2\bar{x}^{F\_{2}}, associated with the perturbed operator F2F\_{2}, satisfy

|  |  |  |
| --- | --- | --- |
|  | ‖x¯F2‖C​(𝒯;ℋ)≤CF2x¯,\displaystyle\big\|\bar{x}^{F\_{2}}\big\|\_{C(\cal{T};\cal{H})}\leq C^{\bar{x}}\_{F\_{2}}, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖qF2‖C​(𝒯;ℋ)≤CF2q,\displaystyle\big\|q^{F\_{2}}\big\|\_{C(\cal{T};\cal{H})}\leq C^{q}\_{F\_{2}}, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖x¯F2−x¯†‖C​(𝒯;H)≤CF2,F2†x¯​‖F2−F2†‖,\displaystyle\big\|\bar{x}^{F\_{2}}-\bar{x}^{\dagger}\big\|\_{C(\mathcal{T};H)}\leq C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖qF2−q†‖C​(𝒯;H)≤CF2,F2†q​‖F2−F2†‖,\displaystyle\big\|q^{F\_{2}}-q^{\dagger}\big\|\_{C(\mathcal{T};H)}\leq C^{q}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†x¯=\displaystyle C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}= | [1−(MTA†​CF2,F2†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​MTA†​CF2,F2†Φ,q​T​exp⁡(MTA†​(CF2,F2†Φ,x¯+CF2,F2†Ψ,q)​T)]−1\displaystyle\big[1-(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|)M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{F\_{2},F\_{2}^{\dagger}}T\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}})T\big)\big]^{-1}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[(MTA†CF2,F2†Φ,cT)exp(MTA†CF2,F2†Ψ,qT)\displaystyle\times\big[(M^{A^{\dagger}}\_{T}C^{\Phi,c}\_{F\_{2},F\_{2}^{\dagger}}T)\exp(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}}T)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +MTA†CF2,F2†Φ,qT(MTA†CF2,F2†Ψ,cT)exp(MTA†(CF2,F2†Φ,x¯+CF2,F2†Ψ,q)T)]\displaystyle+M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{F\_{2},F\_{2}^{\dagger}}T(M^{A^{\dagger}}\_{T}C^{\Psi,c}\_{F\_{2},F\_{2}^{\dagger}}T)\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}})T\big)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†q=\displaystyle C^{q}\_{F\_{2},F\_{2}^{\dagger}}= | (MTA†​CF2,F2†Ψ,c​T)​exp⁡(MTA†​(CF2,F2†Φ,x¯+CF2,F2†Ψ,q)​T)\displaystyle(M^{A^{\dagger}}\_{T}C^{\Psi,c}\_{F\_{2},F\_{2}^{\dagger}}T)\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}})T\big)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(MTA†​CF2,F2†Ψ,x¯​T+MTA†​‖G‖​‖F^2‖)​exp⁡(MTA†​CF2,F2†Ψ,q​T)​CF2,F2†x¯\displaystyle+\big(M^{A^{\dagger}}\_{T}C^{\Psi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}T+M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|\big)\exp\big(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}}T\big)C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Φ,x¯=\displaystyle C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}= | ‖B†‖​(‖B†‖+R3)​CΠ†+‖F1‖+‖B†‖​R2​‖F2‖​CΠ†,\displaystyle\|B^{\dagger}\|(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}+\|F\_{1}\|+\|B^{\dagger}\|R\_{2}\|F\_{2}\|C^{\Pi^{\dagger}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Φ,q=\displaystyle C^{\Phi,q}\_{F\_{2},F\_{2}^{\dagger}}= | ‖B†‖,\displaystyle\|B^{\dagger}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Φ,c=\displaystyle C^{\Phi,c}\_{F\_{2},F\_{2}^{\dagger}}= | R2​‖B†‖​Cx¯†,\displaystyle R\_{2}\|B^{\dagger}\|C^{\bar{x}^{\dagger}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ψ,x¯=\displaystyle C^{\Psi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}= | R1​‖F2‖​CΠ†+(‖B†‖+R3)​CΠ†​R2​‖F2‖​CΠ†+(CΠ†​‖F1‖+‖M‖​‖F^1‖),\displaystyle R\_{1}\|F\_{2}\|C^{\Pi^{\dagger}}+(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}R\_{2}\|F\_{2}\|C^{\Pi^{\dagger}}+(C^{\Pi^{\dagger}}\|F\_{1}\|+\|M\|\|\widehat{F}\_{1}\|),\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ψ,q=\displaystyle C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}}= | (‖B†‖+R3)​CΠ†​‖B†‖,\displaystyle(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}\|B^{\dagger}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ψ,c=\displaystyle C^{\Psi,c}\_{F\_{2},F\_{2}^{\dagger}}= | (‖B†‖+R3)​CΠ†​R2​Cx¯†​CΠ†,\displaystyle(\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}R\_{2}C^{\bar{x}^{\dagger}}C^{\Pi^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2x¯=\displaystyle C^{\bar{x}}\_{F\_{2}}= | [1−MTA†(CF2Ψ,x¯T+∥G∥∥F^2∥)]−1[MTA†(CF2Φ,cT+∥ξ¯∥)exp(MTA†CF2Φ,x¯T)\displaystyle\big[1-M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}}\_{F\_{2}}T+\|G\|\|\widehat{F}\_{2}\|)\big]^{-1}\big[M^{A^{\dagger}}\_{T}(C^{\Phi,c}\_{F\_{2}}T+\|\bar{\xi}\|)\exp(M^{A^{\dagger}}\_{T}C^{\Phi,\bar{x}}\_{F\_{2}}T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +MTA†CF2Φ,qT(MTA†CF2Ψ,cT)exp(MTA†(CF2Φ,x¯+CF2Ψ,q)T)],\displaystyle+M^{A^{\dagger}}\_{T}C^{\Phi,q}\_{F\_{2}}T\big(M^{A^{\dagger}}\_{T}C^{\Psi,c}\_{F\_{2}}T\big)\exp\big(M^{A^{\dagger}}\_{T}(C^{\Phi,\bar{x}}\_{F\_{2}}+C^{\Psi,q}\_{F\_{2}})T\big)\big],\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2q=\displaystyle C^{q}\_{F\_{2}}= | MTA†​CF2Ψ,c​T​exp⁡(MTA†​CF2Ψ,q​T)+MTA†​(CF2Ψ,x¯​T+‖G‖​‖F^2‖)​exp⁡(MTA†​CF2Ψ,q​T)​CF2x¯,\displaystyle M^{A^{\dagger}}\_{T}C^{\Psi,c}\_{F\_{2}}T\exp(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{F\_{2}}T)+M^{A^{\dagger}}\_{T}(C^{\Psi,\bar{x}}\_{F\_{2}}T+\|G\|\|\widehat{F}\_{2}\|)\exp(M^{A^{\dagger}}\_{T}C^{\Psi,q}\_{F\_{2}}T)C^{\bar{x}}\_{F\_{2}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2Φ,x¯=\displaystyle C^{\Phi,\bar{x}}\_{F\_{2}}= | ‖B†‖​(‖B†‖+R3+R2​‖F2‖)​CΠ†+‖F1‖,\displaystyle\|B^{\dagger}\|(\|B^{\dagger}\|+R\_{3}+R\_{2}\|F\_{2}\|)C^{\Pi^{\dagger}}+\|F\_{1}\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2Φ,q=\displaystyle C^{\Phi,q}\_{F\_{2}}= | ‖B†‖2,\displaystyle\|B^{\dagger}\|^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2Φ,c=\displaystyle C^{\Phi,c}\_{F\_{2}}= | ‖B†‖​R2​‖σ‖​CΠ†,\displaystyle\|B^{\dagger}\|R\_{2}\|\sigma\|C^{\Pi^{\dagger}},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2Ψ,q=\displaystyle C^{\Psi,q}\_{F\_{2}}= | CΠ​(‖B†‖+R3)​‖B†‖,\displaystyle C^{\Pi}(\|B^{\dagger}\|+R\_{3})\big\|B^{\dagger}\big\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2Ψ,x¯=\displaystyle C^{\Psi,\bar{x}}\_{F\_{2}}= | [R1​CΠ†+(CΠ†)2​(‖B†‖+R3)​R2]​‖F2‖+CΠ†​‖F1‖+‖M‖​‖F^1‖,\displaystyle\big[R\_{1}C^{\Pi^{\dagger}}+(C^{\Pi^{\dagger}})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}\big]\big\|F\_{2}\big\|+C^{\Pi^{\dagger}}\big\|F\_{1}\big\|+\big\|M\big\|\big\|\widehat{F}\_{1}\big\|,\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2Ψ,c=\displaystyle C^{\Psi,c}\_{F\_{2}}= | R1​CΠ†+(CΠ†)2​(‖B†‖+R3)​R2.\displaystyle R\_{1}C^{\Pi^{\dagger}}+(C^{\Pi^{\dagger}})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}. |  |

###### Proof.

See [A.6.1](https://arxiv.org/html/2510.20017v1#A1.SS6.SSS1 "A.6.1 Proof of Lemma 4.12 ‣ A.6 Proofs of Lipschitz Stability with respect to 𝐹₂ ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Lemma 4.13.

The equilibrium state xF2x^{F\_{2}}, associated with the perturbed operator F2F\_{2}, satisfies

|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖xF2​(t)‖2)12≤CF2x,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|x^{F\_{2}}(t)\|^{2}\big)^{\frac{1}{2}}\leq C^{x}\_{F\_{2}},\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | (supt∈𝒯𝔼​‖(xF2−x†)​(t)‖2)12≤CF2,F2†x​‖F2−F2†‖,\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|(x^{F\_{2}}-x^{\dagger})(t)\|^{2}\big)^{\frac{1}{2}}\leq C^{x}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2x=\displaystyle C^{x}\_{F\_{2}}= | {3(MTA†)2𝔼∥ξ∥2+3T(MTA†)2[(∥B†∥2+∥E∥2)(∥B†∥CF2†q+R2(∥F2∥CF2x¯+∥σ∥)CΠ†)]\displaystyle\big\{3(M^{A^{\dagger}}\_{T})^{2}\mathbb{E}\|\xi\|^{2}+3T(M\_{T}^{A^{\dagger}})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big(\|B^{\dagger}\|C^{q}\_{F\_{2}^{\dagger}}+R\_{2}(\|F\_{2}\|C^{\bar{x}}\_{F\_{2}}+\|\sigma\|)C^{\Pi^{\dagger}}\big)\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3T(MTA†)2(∥F1∥2+∥F2∥2)(CF2x¯)2+3T(MTA†)2∥σ∥2}1/2\displaystyle\hskip 0.0pt+3T(M^{A^{\dagger}}\_{T})^{2}(\|F\_{1}\|^{2}+\|F\_{2}\|^{2})(C^{\bar{x}}\_{F\_{2}})^{2}+3T(M^{A^{\dagger}}\_{T})^{2}\|\sigma\|^{2}\big\}^{1/2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{(MTA†)2​[(‖B†‖2+‖E‖2)​((‖B†‖+R3)​CΠ†)2+‖D‖2]​3​T/2},\displaystyle\times\exp\big\{(M^{A^{\dagger}}\_{T})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big((\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}\big)^{2}+\|D\|^{2}\big]3T/2\big\},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†x=\displaystyle C^{x}\_{F\_{2},F\_{2}^{\dagger}}= | T1/2​MTA†​[(CF2,F2†Ξ1,q+CF2,F2†Ξ2,q)​CF2,F2†q+(CF2,F2†Ξ1,x¯+CF2,F2†Ξ2,x¯)​CF2,F2†x¯+CF2,F2†Ξ1,c+CF2,F2†Ξ2,c]1/2\displaystyle T^{1/2}M^{A^{\dagger}}\_{T}\Big[(C^{\Xi\_{1},q}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},q}\_{F\_{2},F\_{2}^{\dagger}})C^{q}\_{F\_{2},F\_{2}^{\dagger}}+(C^{\Xi\_{1},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}})C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{1},c}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},c}\_{F\_{2},F\_{2}^{\dagger}}\Big]^{1/2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡[T​(MTA†)2​(CF2,F2†Ξ1,x+CF2,F2†Ξ2,x)/2],\displaystyle\times\exp\big[T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},x}\_{F\_{2},F\_{2}^{\dagger}})/2\big],\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ1,x=\displaystyle C^{\Xi\_{1},x}\_{F\_{2},F\_{2}^{\dagger}}= | ‖B†‖2​(‖B†‖+R3)2​(CΠ†)2,\displaystyle\|B^{\dagger}\|^{2}(\|B^{\dagger}\|+R\_{3})^{2}(C^{\Pi^{\dagger}})^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ1,x¯=\displaystyle C^{\Xi\_{1},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}= | ‖B†‖2​(R2)2​‖F2‖2,\displaystyle\|B^{\dagger}\|^{2}(R\_{2})^{2}\|F\_{2}\|^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ1,q=\displaystyle C^{\Xi\_{1},q}\_{F\_{2},F\_{2}^{\dagger}}= | ‖B†‖4,\displaystyle\|B^{\dagger}\|^{4},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ1,c=\displaystyle C^{\Xi\_{1},c}\_{F\_{2},F\_{2}^{\dagger}}= | ‖B†‖2​(R2​Cx¯†​CΠ†)2,\displaystyle\|B^{\dagger}\|^{2}\big(R\_{2}C^{\bar{x}^{\dagger}}C^{\Pi^{\dagger}}\big)^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ2,x=\displaystyle C^{\Xi\_{2},x}\_{F\_{2},F\_{2}^{\dagger}}= | [‖D‖+‖E‖​(‖B†‖+R3)​(CΠ†)]2,\displaystyle\big[\|D\|+\|E\|(\|B^{\dagger}\|+R\_{3})(C^{\Pi^{\dagger}})\big]^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ2,x¯=\displaystyle C^{\Xi\_{2},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}= | ‖F2‖2+(R2​‖E‖​‖F2†‖​CΠ†)2,\displaystyle\|F\_{2}\|^{2}+\big(R\_{2}\|E\|\|F\_{2}^{\dagger}\|C^{\Pi^{\dagger}}\big)^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ2,q=\displaystyle C^{\Xi\_{2},q}\_{F\_{2},F\_{2}^{\dagger}}= | ‖E‖2​‖B†‖2,\displaystyle\|E\|^{2}\|B^{\dagger}\|^{2},\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†Ξ2,c=\displaystyle C^{\Xi\_{2},c}\_{F\_{2},F\_{2}^{\dagger}}= | ‖E‖2​(R2​Cx¯†​CΠ†)2.\displaystyle\|E\|^{2}\big(R\_{2}C^{\bar{x}^{\dagger}}C^{\Pi^{\dagger}}\big)^{2}. |  |

###### Proof.

See Section [A.6.2](https://arxiv.org/html/2510.20017v1#A1.SS6.SSS2 "A.6.2 Proof of Lemma 4.13 ‣ A.6 Proofs of Lipschitz Stability with respect to 𝐹₂ ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

###### Proposition 4.14.

The equilibrium strategy uF2u^{F\_{2}}, associated with the perturbed operator F2F\_{2}, satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖uF2​(t)−u†​(t)‖≤CF2,F2†u​‖F2−F2†‖,\mathbb{E}\|u^{F\_{2}}(t)-u^{\dagger}(t)\|\leq C^{u}\_{F\_{2},F\_{2}^{\dagger}}\big\|F\_{2}-F\_{2}^{\dagger}\big\|, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | CF2,F2†u=\displaystyle C^{u}\_{F\_{2},F\_{2}^{\dagger}}= | 6​{(‖B†‖+R3)​CF2,F2†x+R2​CΠ†​((Cx¯†)2+‖F2‖2​(CF2,F2†x¯)2)+‖B†‖​CF2,F2†q}12.\displaystyle\sqrt{6}\Big\{(\|B^{\dagger}\|+R\_{3})C^{x}\_{F\_{2},F\_{2}^{\dagger}}+R\_{2}C^{\Pi^{\dagger}}\big((C^{\bar{x}^{\dagger}})^{2}+\|F\_{2}\|^{2}(C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}})^{2}\big)+\|B^{\dagger}\|C^{q}\_{F\_{2},F\_{2}^{\dagger}}\Big\}^{\frac{1}{2}}. |  |

###### Proof.

From ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), the equilibrium strategy corresponding to the operator F2F\_{2} is given by

|  |  |  |
| --- | --- | --- |
|  | uF2​(t)=−(K†)−1​(T−t)​[L†​(T−t)​xF2​(t)+Γ2​((F2​x¯F2​(t)+σ)⋆​Π†​(T−t))+B†⋆​qF2​(T−t)],\displaystyle u^{F\_{2}}(t)=-(K^{\dagger})^{-1}(T-t)\big[L^{\dagger}(T-t)x^{F\_{2}}(t)+\Gamma\_{2}\big((F\_{2}\bar{x}^{F\_{2}}(t)+\sigma)^{\star}\Pi^{\dagger}(T-t)\big)+B^{\dagger\star}q^{F\_{2}}(T-t)\big], |  |
|  |  |  |
| --- | --- | --- |
|  | K†​(t)=I+Δ3​(Π†​(t)),L†​(t)=B†⋆​Π†​(t)+Δ1​(Π†​(t)).\displaystyle K^{\dagger}(t)=I+\Delta\_{3}(\Pi^{\dagger}(t)),\quad L^{\dagger}(t)=B^{\dagger\star}\Pi^{\dagger}(t)+\Delta\_{1}(\Pi^{\dagger}(t)). |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uF2−u†)​(t)=\displaystyle(u^{F\_{2}}-u^{\dagger})(t)= | (K†)−1​L†​(T−t)​(xF2−x†)​(t)+(K†)−1​(T−t)​Γ2​(F2​x¯F2​(t)−F2†​x¯†​(t))​Π†​(T−t)\displaystyle(K^{\dagger})^{-1}L^{\dagger}(T-t)(x^{F\_{2}}-x^{\dagger})(t)+(K^{\dagger})^{-1}(T-t)\Gamma\_{2}\big(F\_{2}\bar{x}^{F\_{2}}(t)-F\_{2}^{\dagger}\bar{x}^{\dagger}(t)\big)\Pi^{\dagger}(T-t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(K†)−1​(T−t)​B†⋆​(qF2−q†)​(T−t),\displaystyle+(K^{\dagger})^{-1}(T-t)B^{\dagger\star}(q^{F\_{2}}-q^{\dagger})(T-t), |  |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(uF2−u†)​(t)‖2\displaystyle\mathbb{E}\|(u^{F\_{2}}-u^{\dagger})(t)\|^{2} | ≤3​‖(K†)−1​L†​(T−t)‖2​𝔼​‖(xF2−x†)​(t)‖2\displaystyle\leq 3\|(K^{\dagger})^{-1}L^{\dagger}(T-t)\|^{2}\,\mathbb{E}\|(x^{F\_{2}}-x^{\dagger})(t)\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​‖(K†)−1​(T−t)‖2​‖Γ2‖2​‖F2​x¯F2​(t)−F2†​x¯†​(t)‖2​‖Π†​(T−t)‖2\displaystyle\,\,\,\,+3\|(K^{\dagger})^{-1}(T-t)\|^{2}\|\Gamma\_{2}\|^{2}\|F\_{2}\bar{x}^{F\_{2}}(t)-F\_{2}^{\dagger}\bar{x}^{\dagger}(t)\|^{2}\|\Pi^{\dagger}(T-t)\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​‖(K†)−1​(T−t)‖2​‖B†‖2​‖(qF2−q†)​(T−t)‖2\displaystyle\,\,\,\,+3\|(K^{\dagger})^{-1}(T-t)\|^{2}\|B^{\dagger}\|^{2}\|(q^{F\_{2}}-q^{\dagger})(T-t)\|^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤6(∥B†∥+R3)2(CF2,F2†x)2∥F2−F2†∥2+6(R2)2(CΠ†)2(∥F2−F2†∥2(Cx¯†)2\displaystyle\leq 6(\|B^{\dagger}\|+R\_{3})^{2}(C^{x}\_{F\_{2},F\_{2}^{\dagger}})^{2}\|F\_{2}-F\_{2}^{\dagger}\|^{2}+6(R\_{2})^{2}(C^{\Pi^{\dagger}})^{2}\big(\|F\_{2}-F\_{2}^{\dagger}\|^{2}(C^{\bar{x}^{\dagger}})^{2} |  | (4.7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∥F2∥2∥F2−F2†∥2)(CF2,F2†x¯)2+6∥B†∥2∥F2−F2†∥2(CF2,F2†q)2.\displaystyle\,\,\,+\|F\_{2}\|^{2}\|F\_{2}-F\_{2}^{\dagger}\|^{2}\big)(C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}})^{2}+6\|B^{\dagger}\|^{2}\|F\_{2}-F\_{2}^{\dagger}\|^{2}(C^{q}\_{F\_{2},F\_{2}^{\dagger}})^{2}. |  |

∎

### 4.4 Proof of Proposition [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem1 "Proposition 3.1 (Local Well-Posedness of the Rules-to-Equilibrium Operator). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

We may now deduce Proposition [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem1 "Proposition 3.1 (Local Well-Posedness of the Rules-to-Equilibrium Operator). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

###### Proof.

Direct consequence of Theorem [3.5](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), and the inequalities
([2.6](https://arxiv.org/html/2510.20017v1#S2.E6 "Equation 2.6 ‣ 2.1.1 Space of Variations on Rules of LQ MFGs ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([2.7](https://arxiv.org/html/2510.20017v1#S2.E7 "Equation 2.7 ‣ 2.1.2 Rules-to-Equilibrium Operator ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) as well as the fact that the Hilbert-Schmidt norm upper-bounds the operator norm.
∎

### 4.5 Proof of Proposition [3.2](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem2 "Proposition 3.2 (Global Lipschitzness of the Regularized Rules-to-equilibrium Map). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

By Theorem [3.5](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.1 Explanation of Proofs via Supporting Results ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), there exists a constant L~𝒦≥0\tilde{L}\_{\mathcal{K}}\geq 0, depending only on 𝒦\mathcal{K}, as given by ([3.1](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem1 "Proposition 3.1 (Local Well-Posedness of the Rules-to-Equilibrium Operator). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), such that for every (A,B,F2),(A~,B~,F~2)∈𝒦(A,B,F\_{2}),(\tilde{A},\tilde{B},\tilde{F}\_{2})\in\mathcal{K}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ℜ​(A,B,F2)t−ℜ​(A~,B~,F~2)t‖ℳ2​(𝒯,U)≤L~𝒦​(∑i=13‖A−A~‖2+‖B−B~‖2+‖F2−F~2‖2)1/2.\|\mathfrak{R}(A,B,F\_{2})\_{t}-\mathfrak{R}(\tilde{A},\tilde{B},\tilde{F}\_{2})\_{t}\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\tilde{L}\_{\mathcal{K}}\,\Big(\sum\_{i=1}^{3}\,\|A-\tilde{A}\|^{2}+\|B-\tilde{B}\|^{2}+\|F\_{2}-\tilde{F}\_{2}\|^{2}\Big)^{1/2}. |  | (4.8) |

Combining ([4.8](https://arxiv.org/html/2510.20017v1#S4.E8 "Equation 4.8 ‣ 4.5 Proof of Proposition 3.2 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) with the estimates in ([B.1](https://arxiv.org/html/2510.20017v1#A2.E1 "Equation B.1 ‣ B.1 Output Space: Bochner-Lebesgue Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))
and in ([B.3](https://arxiv.org/html/2510.20017v1#A2.E3 "Equation B.3 ‣ B.2 Hilbert-Schmidt Operators Between Different Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we deduce that ℛ:ℋ→ℳ2​(𝒯,U)\mathcal{R}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) is L𝒦=def.T​L~𝒦L\_{\mathcal{K}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}T\,\tilde{L}\_{\mathcal{K}}-Lipschitz when restricted to 𝒦\mathcal{K}. By the Benyamini-Lindenstrauss Theorem, see e.g. [Benyamini and Lindenstrauss, [2000](https://arxiv.org/html/2510.20017v1#bib.bib45), Theorem 1.12] there exists a L𝒦L\_{\mathcal{K}}-Lipschitz extension ℜ𝒦:ℋ→ℳ2​(𝒯,U)\mathfrak{R}^{\mathcal{K}}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) of the restricted rules-to-equilibrium map ℛ|𝒦:𝒦→ℳ2​(𝒯,U)\mathcal{R}|\_{\mathcal{K}}:\mathcal{K}\to\mathcal{M}^{2}({\mathcal{T}},U); i.e. ℛ𝒦\mathcal{R}^{\mathcal{K}} satisfies ([3.2](https://arxiv.org/html/2510.20017v1#S3.E2 "Equation 3.2 ‣ Proposition 3.2 (Global Lipschitzness of the Regularized Rules-to-equilibrium Map). ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and is L𝒦L\_{\mathcal{K}}-Lipschitz globally on all of ℋ\mathcal{H}.
∎

## 5 Proof of Sample-Complexity Estimates and Approximation Guarantees

In this section, we generalize ℋ\mathcal{H} (resp. ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U)) to an arbitrary infinite-dimensional separable Hilbert space ℋ\mathcal{H} (resp. ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U)), each equipped with an orthonormal basis denoted (ei)i∈I(e\_{i})\_{i\in I} (resp. (ηj)j∈J(\eta\_{j})\_{j\in J}). This generalization is justified as all results presented here remain valid in this broader setting. Accordingly, we define the projection operators ([2.10](https://arxiv.org/html/2510.20017v1#S2.E10 "Equation 2.10 ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and embedding operators ([2.11](https://arxiv.org/html/2510.20017v1#S2.E11 "Equation 2.11 ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) exactly as before, with ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) replaced by ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U), respectively. When necessary, we make the domain and codomain explicit by writing PiℋP^{\mathcal{H}}\_{i} (resp. Ejℳ2​(𝒯,U)E^{\mathcal{M}^{2}({\mathcal{T}},U)}\_{j}) instead of PiP\_{i} (resp. EjE\_{j}). Similarly, the RNO model defined previously now refers to maps from ℋ\mathcal{H} to ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U), with the only change being that the encoder and decoder maps PiP\_{i} and EjE\_{j} are now defined on ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) rather than on ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U).

### 5.1 Oracle Inequalities

We are interested in the out-of-sample performance of a neural operator model F^:ℋ→ℳ2​(𝒯,U)\hat{F}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) is measured by its ability to recover the noiseless target operator f⋆f^{\star}, as quantified by its reconstruction quality (sometimes, abusively called excess risk)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ​(F^)=def.𝔼X∼ℙX​[‖F^​(X)−f⋆​(X)⏟True Operator‖ℳ2​(𝒯,U)].\mathcal{R}(\hat{F})\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\mathbb{E}\_{X\sim\mathbb{P}\_{X}}\Big[\|\hat{F}(X)-\underbrace{f^{\star}(X)}\_{\text{True Operator}}\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\Big]. |  | (5.1) |

We denote the sample-based version of the risk, called the empirical risk, is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^𝒮​(F^)=def.1N​∑n=1N‖F^​(Xn)−Yn‖ℳ2​(𝒯,U).\hat{\mathcal{R}}\_{\mathcal{S}}(\hat{F})\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\frac{1}{N}\sum\_{n=1}^{N}\,\|\hat{F}(X\_{n})-Y\_{n}\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}. |  | (5.2) |

The next result bounds the true risk in terms of the empirical risk, under the assumption that both the target function and the hypothesis class admit the same worst-case Lipschitz constant.

###### Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality).

Let N∈ℕ+N\in\mathbb{N}\_{+}, L≥0L\geq 0, and define L¯=def.2​max⁡{L,1}\bar{L}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}2\max\{L,1\}.
Let f⋆:ℋ→ℳ2​(𝒯,U)f^{\star}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) be LL-Lipschitz and F^∈ℱ⊆Lip⁡(ℋ,ℳ2​(𝒯,U)|L)\hat{F}\in\mathcal{F}\subseteq\operatorname{Lip}(\mathcal{H},\mathcal{M}^{2}({\mathcal{T}},U)|L) be an empirical risk minimizer

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^S​(F^)=infF~∈ℱℛ^S​(F~).\hat{\mathcal{R}}^{S}(\hat{F})=\inf\_{\tilde{F}\in\mathcal{F}}\,\hat{\mathcal{R}}^{S}(\tilde{F}). |  | (5.3) |

For any compact 𝒦⊂ℋ\mathcal{K}\subset\mathcal{H} of positive ℙX\mathbb{P}\_{X}-measure, the following holds

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℛ​(F^)≤infF~∈ℱsupx∈𝒦‖F~​(x)−f⋆​(x)‖ℳ2​(𝒯,U)⏟(I):Approximation+L¯​𝒲1​(ℙX,ℙXN)⏟(II):Concentration Wasserstein)≥ℙX​(𝒦)N>0.\mathbb{P}\biggl(\mathcal{R}(\hat{F})\leq\underbrace{\inf\_{\tilde{F}\in\mathcal{F}}\,\sup\_{x\in\mathcal{K}}\|\tilde{F}(x)-f^{\star}(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}}\_{\textup{(I)}:\text{Approximation}}+\underbrace{\bar{L}\,\mathcal{W}\_{1}\big(\mathbb{P}\_{X},\mathbb{P}^{N}\_{X}\big)}\_{\textup{(II)}:\text{Concentration Wasserstein}}\biggr)\geq\mathbb{P}\_{X}(\mathcal{K})^{N}>0. |  |

###### Proof of Lemma [5.1](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

note the (random) empirical measure induced by our sample set by ℙN=def.1N​∑n=1NδXN\mathbb{P}^{N}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\frac{1}{N}\sum\_{n=1}^{N}\,\delta\_{X\_{N}}.
For every F~∈ℱ\tilde{F}\in\mathcal{F}, the map ΛF~:ℋ∋x↦‖F~​(x)−f⋆​(x)‖ℳ2​(𝒯,U)\Lambda\_{\tilde{F}}:\mathcal{H}\ni x\mapsto\|\tilde{F}(x)-f^{\star}(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} is L¯=def.2​max⁡{1,L}\bar{L}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}2\max\{1,L\}-Lipschitz since f⋆f^{\star} and F~∈ℱ\tilde{F}\in\mathcal{F} are both LL-Lipschitz and ∥⋅∥ℳ2​(𝒯,U)\|\cdot\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} is 11-Lipschitz. In particular, this is the case when taking F~=F^\tilde{F}=\hat{F}.
Therefore, the Kantorovich-Rubinstein duality implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ​(F^)=𝔼X∼ℙX​[‖F^​(X)−f⋆​(X)‖ℳ2​(𝒯,U)]≤L¯​𝒲1​(ℙ,ℙN)+𝔼X∼ℙXN​[‖F^​(X)−f⋆​(X)‖ℳ2​(𝒯,U)].\displaystyle\mathcal{R}(\hat{F})=\mathbb{E}\_{X\sim\mathbb{P}\_{X}}\big[\|\hat{F}(X)-f^{\star}(X)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\big]\leq\bar{L}\mathcal{W}\_{1}(\mathbb{P},\mathbb{P}\_{N})+\mathbb{E}\_{X\sim\mathbb{P}\_{X}^{N}}\big[\|\hat{F}(X)-f^{\star}(X)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\big]. |  | (5.4) |

Now, applying the empirical risk minimization property of F^\hat{F}, in ([5.3](https://arxiv.org/html/2510.20017v1#S5.E3 "Equation 5.3 ‣ Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we may re-express ([5.4](https://arxiv.org/html/2510.20017v1#S5.E4 "Equation 5.4 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ​(F^)≤L¯​𝒲1​(ℙ,ℙN)+infF~∈ℱ1N​∑n=1N‖F~​(Xn)−f⋆​(Xn)‖ℳ2​(𝒯,U).\displaystyle\mathcal{R}(\hat{F})\leq\bar{L}\mathcal{W}\_{1}(\mathbb{P},\mathbb{P}\_{N})+\inf\_{\tilde{F}\in\mathcal{F}}\,\frac{1}{N}\sum\_{n=1}^{N}\,\|\tilde{F}(X\_{n})-f^{\star}(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}. |  | (5.5) |

Now, since X1,…,XNX\_{1},\dots,X\_{N} are i.i.d. with law ℙ\mathbb{P} and since 𝒦\mathcal{K} has positive ℙ\mathbb{P}-measure then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(∀n=1,…,N​Xn∈𝒦)=ℙ​(X1∈𝒦)=ℙX​(𝒦)N>0.\mathbb{P}\big(\forall n=1,\dots,N\,X\_{n}\in\mathcal{K}\big)=\mathbb{P}(X\_{1}\in\mathcal{K})=\mathbb{P}\_{X}(\mathcal{K})^{N}>0. |  |

Thus, with (positive) probability at-least ℙX​(𝒦)N\mathbb{P}\_{X}(\mathcal{K})^{N}, for every F~∈ℱ\tilde{F}\in\mathcal{F} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1N​∑n=1N‖F~​(Xn)−f⋆​(Xn)‖ℳ2​(𝒯,U)≤1N​∑n=1Nsupx∈𝒦‖F~​(x)−f⋆​(x)‖ℳ2​(𝒯,U)=supx∈𝒦‖F~​(x)−f⋆​(x)‖ℳ2​(𝒯,U).\frac{1}{N}\sum\_{n=1}^{N}\|\tilde{F}(X\_{n})-f^{\star}(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\frac{1}{N}\sum\_{n=1}^{N}\sup\_{x\in\mathcal{K}}\|\tilde{F}(x)-f^{\star}(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}=\sup\_{x\in\mathcal{K}}\|\tilde{F}(x)-f^{\star}(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}. |  | (5.6) |

Taking infimal over ℱ\mathcal{F} across ([5.6](https://arxiv.org/html/2510.20017v1#S5.E6 "Equation 5.6 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | infF~∈ℱ1N​∑n=1N‖F~​(Xn)−f⋆​(Xn)‖ℳ2​(𝒯,U)≤infF~∈ℱsupx∈𝒦‖F~​(x)−f⋆​(x)‖ℳ2​(𝒯,U)\inf\_{\tilde{F}\in\mathcal{F}}\,\frac{1}{N}\sum\_{n=1}^{N}\|\tilde{F}(X\_{n})-f^{\star}(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\inf\_{\tilde{F}\in\mathcal{F}}\,\sup\_{x\in\mathcal{K}}\|\tilde{F}(x)-f^{\star}(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} |  | (5.7) |

which, again, holds with probability at-least ℙ​(𝒦)N\mathbb{P}(\mathcal{K})^{N} (on the draw of X1,…,XNX\_{1},\dots,X\_{N}).
Now, merging ([5.7](https://arxiv.org/html/2510.20017v1#S5.E7 "Equation 5.7 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) back into the right-hand side of ([5.1](https://arxiv.org/html/2510.20017v1#S5.Ex3 "5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ​(F^)\displaystyle\mathcal{R}(\hat{F}) | ≤L¯​𝒲1​(ℙ,ℙN)+infF~∈ℱ1N​∑n=1N‖F~​(Xn)−f⋆​(Xn)‖ℳ2​(𝒯,U)\displaystyle\leq\bar{L}\mathcal{W}\_{1}(\mathbb{P},\mathbb{P}\_{N})+\inf\_{\tilde{F}\in\mathcal{F}}\,\frac{1}{N}\sum\_{n=1}^{N}\,\|\tilde{F}(X\_{n})-f^{\star}(X\_{n})\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L¯​𝒲1​(ℙ,ℙN)+infF~∈ℱsupx∈𝒦‖F~​(x)−f⋆​(x)‖ℳ2​(𝒯,U)\displaystyle\leq\bar{L}\mathcal{W}\_{1}(\mathbb{P},\mathbb{P}\_{N})+\inf\_{\tilde{F}\in\mathcal{F}}\,\sup\_{x\in\mathcal{K}}\|\tilde{F}(x)-f^{\star}(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} |  |

holds with probability at-least ℙ​(𝒦)N\mathbb{P}(\mathcal{K})^{N}.
∎

###### Lemma 5.2 (Infinite-Dimensional Concentration Inequality).

Under Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), for every 0<δ≤10<\delta\leq 1, the following

|  |  |  |
| --- | --- | --- |
|  | 𝒲1​(ℙX,ℙXN)≲e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N\mathcal{W}\_{1}(\mathbb{P}\_{X},\mathbb{P}\_{X}^{N})\lesssim e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}} |  |

holds with probability at-least 1−δ1-\delta.

###### Proof of Lemma [5.2](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem2 "Lemma 5.2 (Infinite-Dimensional Concentration Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

The rapid decay condition in Assumption [2.9](https://arxiv.org/html/2510.20017v1#S2.E9 "Equation 2.9 ‣ Item (iii) ‣ Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") implies both that

|  |  |  |
| --- | --- | --- |
|  | ∑i=1∞σi2≲∑i=1∞e−r​2​i=1e2​r−1<∞.\sum\_{i=1}^{\infty}\,\sigma\_{i}^{2}\lesssim\sum\_{i=1}^{\infty}\,e^{-r2i}=\frac{1}{e^{2r}-1}<\infty. |  |

This, together with [Lei, [2020](https://arxiv.org/html/2510.20017v1#bib.bib54), Proposition 5.3], the sub-Gaussian decay condition supi∈ℕ+‖Zi‖ψ2<∞\sup\_{i\in\mathbb{N}\_{+}}\,\|Z\_{i}\|\_{\psi\_{2}}<\infty implies that XX has sub-exponential tails; i.e. ‖X‖ψ1<∞\|X\|\_{\psi\_{1}}<\infty.
As shown directly below [Lei, [2020](https://arxiv.org/html/2510.20017v1#bib.bib54), Equation (14)], the finiteness of ‖X‖ψ1\|X\|\_{\psi\_{1}} implies that condition [Lei, [2020](https://arxiv.org/html/2510.20017v1#bib.bib54), Equation (13)] is satisfied; namely, there are constant v,V>0v,V>0 satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​𝔼​[‖X‖k]≤k!​v2​Vk−22\mathbb{E}[\|X\|^{k}]\leq k!v^{2}V^{k-2} |  | (5.8) |

for all integers k≥2k\geq 2. In turn, ([5.8](https://arxiv.org/html/2510.20017v1#S5.E8 "Equation 5.8 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) implies that [Lei, [2020](https://arxiv.org/html/2510.20017v1#bib.bib54), Corollary 5.2] applies; whence, for all η>0\eta>0 we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(‖𝒲1​(ℙX,ℙXN)−𝔼​[𝒲1​(ℙX,ℙXN)]‖≥η)≤2​exp⁡(−N​η28​v2+4​V​η).\mathbb{P}\Big(\big\|\mathcal{W}\_{1}(\mathbb{P}\_{X},\mathbb{P}\_{X}^{N})-\mathbb{E}\big[\mathcal{W}\_{1}(\mathbb{P}\_{X},\mathbb{P}\_{X}^{N})\big]\big\|\geq\eta\Big)\leq 2\exp\Big(-\frac{N\eta^{2}}{8v^{2}+4V\eta}\Big). |  | (5.9) |

It remains to bound the expected Wasserstein distance 𝔼​[𝒲1​(ℙX,ℙXN)]\mathbb{E}\big[\mathcal{W}\_{1}(\mathbb{P}\_{X},\mathbb{P}\_{X}^{N})\big].
Now, the exponential decay assumption σi​e−r​i\sigma\_{i}\,e^{-ri} imply that [Lei, [2020](https://arxiv.org/html/2510.20017v1#bib.bib54), Proposition 4.4 (2)] applies; which, in turn, guarantees that [Lei, [2020](https://arxiv.org/html/2510.20017v1#bib.bib54), Theorem 4.2] applies with γ=er\gamma=e^{r}. Whence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒲1​(ℙX,ℙXN)]≲e−2​log⁡(γ)​log⁡(N)=e−log⁡(N2​r).\mathbb{E}\big[\mathcal{W}\_{1}(\mathbb{P}\_{X},\mathbb{P}\_{X}^{N})\big]\lesssim e^{-\sqrt{2\log(\gamma)\log(N)}}=e^{-\sqrt{\log(N^{2r})}}. |  | (5.10) |

Combining ([5.9](https://arxiv.org/html/2510.20017v1#S5.E9 "Equation 5.9 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) with ([5.10](https://arxiv.org/html/2510.20017v1#S5.E10 "Equation 5.10 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) implies that: for each η>0\eta>0 we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲1​(ℙX,ℙXN)≤e−log⁡(N2​r)+η\mathcal{W}\_{1}(\mathbb{P}\_{X},\mathbb{P}\_{X}^{N})\leq e^{-\sqrt{\log(N^{2r})}}+\eta |  | (5.11) |

holds with probability at-least 1−2​exp⁡(−N​η28​v2+4​V​η)1-2\exp\Big(-\frac{N\eta^{2}}{8v^{2}+4V\eta}\Big). Fix δ∈(0,1]\delta\in(0,1]. Setting δ=2​exp⁡(−N​η28​v2+4​V​η)\delta=2\exp\Big(-\frac{N\eta^{2}}{8v^{2}+4V\eta}\Big) and solving for η\eta implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​η2−4​L​V​η−8​Cδ​v2=0N\eta^{2}-4LV\eta-8C\_{\delta}v^{2}=0 |  | (5.12) |

where Cδ=def.ln⁡(2/δ)C\_{\delta}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\ln(2/\delta); which is a quadratic polynomial in η>0\eta>0. Its only positive solution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | η\displaystyle\eta | =2​V​ln⁡(2δ)​1+(1+2​N​(vV)2/ln⁡(2δ))N\displaystyle=2V\ln\Big(\frac{2}{\delta}\Big)\frac{1+\sqrt{\Big(1+2N\Big(\frac{v}{V}\Big)^{2}/\ln\big(\frac{2}{\delta}\big)\Big)}}{N} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​V​(2​ln⁡(2δ)N+v​2V​ln⁡(2δ)N)\displaystyle\leq 2V\Biggl(\frac{2\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\frac{v\sqrt{2}}{V}\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}\Biggr) |  | (5.13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​V​max⁡{2,2​vV}​(ln⁡(2δ)N+ln⁡(2δ)N)\displaystyle\leq 2V\max\Big\{2,\frac{\sqrt{2}v}{V}\Big\}\biggl(\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}\biggr) |  |

where ([5.13](https://arxiv.org/html/2510.20017v1#S5.Ex8 "Equation 5.13 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) held by the elementary inequality: a+b≤a+b\sqrt{a+b}\leq\sqrt{a}+\sqrt{b} for all a,b≥0a,b\geq 0. Substituting this upper-bound for η\eta back into the right-hand side of ([5.11](https://arxiv.org/html/2510.20017v1#S5.E11 "Equation 5.11 ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) yields the desired conclusion.
∎

To summarize the discussion to this point, we can express the results as a single transport-theoretic oracle inequality. Note that this inequality holds only under the assumption, soon to be rigorously proven below, that the hypothesis class can be taken to be Lipschitz with the same constant as the target nonlinear operator being learned.
We emphasize that the following oracle inequality fundamentally depends on us establishing the (Lipschitz) regularity of the approximating class (below).

###### Proposition 5.3 (Regularity-Based Oracle Inequality).

In the setting of Lemmata [5.1](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and [5.2](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem2 "Lemma 5.2 (Infinite-Dimensional Concentration Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"):
For any F^∈ℱ⊆Lip⁡(ℋ,ℳ2​(𝒯,U)|L)\hat{F}\in\mathcal{F}\subseteq\operatorname{Lip}(\mathcal{H},\mathcal{M}^{2}({\mathcal{T}},U)|L) which is an empirical risk minimizer, i.e. satisfies ([5.3](https://arxiv.org/html/2510.20017v1#S5.E3 "Equation 5.3 ‣ Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), any compact 𝒦⊂ℋ\mathcal{K}\subset\mathcal{H} of positive ℙX\mathbb{P}\_{X}-measure, the following

|  |  |  |
| --- | --- | --- |
|  | ℛ​(F^)≤infF~∈ℱsupx∈𝒦‖F~​(x)−f⋆​(x)‖ℳ2​(𝒯,U)⏟([5.1](https://arxiv.org/html/2510.20017v1#S5.Ex1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")):Approx. Err.+L¯​e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N⏟(III): Estimation\mathcal{R}(\hat{F})\leq\underbrace{\inf\_{\tilde{F}\in\mathcal{F}}\,\sup\_{x\in\mathcal{K}}\|\tilde{F}(x)-f^{\star}(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}}\_{\eqref{t:apprx}:\text{Approx.\ Err.}}+\bar{L}\underbrace{e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}}\_{\textup{(III)}:\text{ Estimation}} |  |

holds with probability at-least 1−(1−ℙX​(𝒦)N)−δ1-(1-\mathbb{P}\_{X}(\mathcal{K})^{N})-\delta; where L¯=def.2​max⁡{L,1}\bar{L}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}2\max\{L,1\}.

###### Proof.

Directly follows from Lemma [5.1](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and [5.2](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem2 "Lemma 5.2 (Infinite-Dimensional Concentration Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").
∎

### 5.2 Approximation Guarantees

To bound the approximation error in ([5.1](https://arxiv.org/html/2510.20017v1#S5.Ex1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we will leverage an infinite-dimensional extension of the main result in Hong and Kratsios [[2024](https://arxiv.org/html/2510.20017v1#bib.bib43)], which provides an (optimal) Lipschitz regular version of the result in Galimberti et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib46)]. The latter, in turn, is an infinite-dimensional extension of the irregular (optimal) approximation result from Shen et al. [[2022](https://arxiv.org/html/2510.20017v1#bib.bib55)]. We expand our approximation around a solution f​(x⋆)f(x^{\star}), which is available in closed-form through classical (likely non-deep learning) methods. This idea is inspired by the numerical approach of Shi et al. [[2023](https://arxiv.org/html/2510.20017v1#bib.bib56)], where a realistic hedging strategy was learned by perturbing a closed-form hedging strategy under idealized market conditions. Instead, our motivation is approximation rates, and using this idea, we can show that this residual method enables us to scale the approximation error favourably for small perturbation sets.
Fix some reference point x⋆∈Xx^{\star}\in X. For any x∈Xx\in X, we henceforth write Δ​x=def.x−x⋆\Delta x\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}x-x^{\star}.
Let W0W\_{0} be the principal branch of the Lambert WW function; which we recall is well-defined on (−1/e,∞)(-1/e,\infty) and is negative-valued on (−1/e,0)(-1/e,0).

###### Proposition 5.4 (General Version of Proposition [3.7](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem7 "Proposition 3.7 (Regular Universal Approximation for Lipschitz RNOs). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"): Quantitative Approximation).

prop:theorem\_universality\_\_regular
Under Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), suppose that 0∈𝒦0\in\mathcal{K}, 0<α≤10<\alpha\leq 1, L>0L>0, f⋆:𝒦→ℳ2​(𝒯,U)f^{\star}:\mathcal{K}\to\mathcal{M}^{2}({\mathcal{T}},U) be an (α,L)(\alpha,L)-Hölder map, and fix an error ε>0\varepsilon>0 and a x⋆∈ℋx^{\star}\in\mathcal{H}.
There is an (α,L)(\mathbf{\alpha},{L})-Hölder
RNO F^:ℋ→ℳ2​(𝒯,U)\hat{F}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) satisfying

|  |  |  |
| --- | --- | --- |
|  | supx∈𝒦‖F^​(Δ​x)−f⋆​(x)‖ℳ2​(𝒯,U)≤ε.\sup\_{x\in\mathcal{K}}\,\big\|\hat{F}(\Delta x)-f^{\star}(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\varepsilon. |  |

Furthermore, F^\hat{F} is base-point preserving; in that F^​(0)=y^⋆=f​(x⋆)\hat{F}(0)=\hat{y}^{\star}=f(x^{\star}).
  
If 𝒦\mathcal{K} is (r,ε)(r,\varepsilon)-exponentially ellipsoidal888Cf. Definition [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmdefinition1 "Definition 3.1 ((𝜌,𝑟)-Exponentially Ellipsoidal). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"). for some r>0r>0, then there is an F^\hat{F} of depth 𝒪​(1)\mathcal{O}(1) and whose width and number of non-zero parameters are F^\hat{F} are 𝒪​(ε−cr,α​log⁡(ε−1))\mathcal{O}\Big(\varepsilon^{-c\_{r,\alpha}}\log(\varepsilon^{-1})\Big); where cr,α=def.1α​⌈log⁡((4​L)1r​αr1/r)⌉c\_{r,\alpha}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\frac{1}{\alpha}\Big\lceil\log\big(\tfrac{(4L)^{\frac{1}{r\alpha}}}{r^{1/r}}\big)\Big\rceil.
If 0<L<4​eα0<L<4e^{\alpha} and999W0W\_{0} denotes the principal branch of the Lambert WW function; i.e. the inverse function of x↦x​exx\mapsto xe^{x} on [−1/e,∞)[-1/e,\infty). r=1/W0​((4​L)−1α)r=1/W\_{0}\Big((4L)^{-\tfrac{1}{\alpha}}\Big) then, its width and connectivity are
𝒪​(ε−1​log⁡(ε−1))\mathcal{O}(\varepsilon^{-1}\log(\varepsilon^{-1})).

###### Proof of Proposition LABEL:prop:theorem\_universality\_\_regular.

Step 1 - Extension:
Since ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) are both separable Hilbert spaces and ff is (α,L)(\alpha,L)-Hölder continuous then [Benyamini and Lindenstrauss, [2000](https://arxiv.org/html/2510.20017v1#bib.bib45), Theorem 1.12] applies; whence, there exists an (α,L)(\alpha,L)-Hölder continuous extension f↑:ℋ→ℳ2​(𝒯,U)f^{\uparrow}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) of ff; meaning that: for each x∈𝒦x\in\mathcal{K} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=f↑​(x)​ and ​f↑​ is (α,L)-Hölder.f(x)=f^{\uparrow}(x)\mbox{ and }f^{\uparrow}\mbox{ is $(\alpha,L)$-H\"{o}lder}. |  | (5.14) |

Since the case where ff is constant is trivial, we assume without loss of generality that ff (and hence f↑f^{\uparrow}) is non-constant; thus, L>0L>0.
Next, We define the residual target function rf:ℋ→ℳ2​(𝒯,U)r\_{f}:\mathcal{H}\to\mathcal{M}^{2}({\mathcal{T}},U) for each x∈ℋx\in\mathcal{H} by

|  |  |  |
| --- | --- | --- |
|  | rf​(x)=def.f↑​(x+x⋆)−f↑​(x⋆)=f↑​(x+x⋆)−y⋆r\_{f}(x)\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}f^{\uparrow}(x+x^{\star})-f^{\uparrow}(x^{\star})=f^{\uparrow}(x+x^{\star})-y^{\star} |  |

where y⋆=def.f↑​(x⋆)y^{\star}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}f^{\uparrow}(x^{\star}).
By construction, the following identity holds for each x∈𝒦x\in\mathcal{K}

|  |  |  |  |
| --- | --- | --- | --- |
|  | rf​(x−x⋆⏞Δ​x)+y⋆⏟Δ​y=f↑​((x−x⋆)+x⋆)−f↑​(x⋆)+y⋆=f↑​(x)=f​(x).\underbrace{r\_{f}(\overbrace{x-x^{\star}}^{\Delta x})+y^{\star}}\_{\Delta y}=f^{\uparrow}((x-x^{\star})+x^{\star})-f^{\uparrow}(x^{\star})+y^{\star}=f^{\uparrow}(x)=f(x). |  | (5.15) |

Since ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) are Banach spaces then, translation is an isometry; thus Lipα⁡(rf)≤Lipα⁡(f)\operatorname{Lip}\_{\alpha}(r\_{f})\leq\operatorname{Lip}\_{\alpha}(f).
Observe Δ​x⋆=x⋆−x⋆=0\Delta x^{\star}=x^{\star}-x^{\star}=0; therefore ([5.15](https://arxiv.org/html/2510.20017v1#S5.E15 "Equation 5.15 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) implies that rf​(0)=0r\_{f}(0)=0.
We will approximate the residual function rfr\_{f} on the following compact set of “residuals” Δ​𝒦=def.{u∈ℋ:(∃x∈𝒦)​u=x−x⋆}\Delta\mathcal{K}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\{u\in\mathcal{H}:\,(\exists x\in\mathcal{K})\,u=x-x^{\star}\}. Note that, the compactness of Δ​𝒦\Delta\mathcal{K} is due to that of 𝒦\mathcal{K} and since the map ℋ:x↦x−x⋆∈ℋ\mathcal{H}:x\mapsto x-x^{\star}\in\mathcal{H} is continuous (ℋ\mathcal{H} is a TVS).

Step 2 - Controlling the Error of Dimension Reduction:
Since ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) are both separable Hilbert spaces, then they have the metric approximation property (MAP), i.e. the 11-bounded approximation property; specifically, the projection operators {Pi𝒵}i∈I\{P\_{i}^{\mathcal{Z}}\}\_{i\in I} approximate the identity map on 𝒵∈{ℋ,ℳ2​(𝒯,U)}\mathcal{Z}\in\{\mathcal{H},\mathcal{M}^{2}({\mathcal{T}},U)\} uniformly on compact subsets thereof and each Pi𝒵P\_{i}^{\mathcal{Z}} has operator norm at-most 11.
This implies two things: first, since ℋ\mathcal{H} and ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U) are both Hilbert spaces then, the embeddings {Ii𝒵}i∈I\{I\_{i}^{\mathcal{Z}}\}\_{i\in I} are isometric embeddings; again for 𝒵∈{ℋ,ℳ2​(𝒯,U)}\mathcal{Z}\in\{\mathcal{H},\mathcal{M}^{2}({\mathcal{T}},U)\}, and therefore, for 𝒵∈{ℋ,ℳ2​(𝒯,U)}\mathcal{Z}\in\{\mathcal{H},\mathcal{M}^{2}({\mathcal{T}},U)\} and i∈Ii\in I, the maps

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai𝒵=def.Ii𝒵∘Pi𝒵:𝒵→𝒵A\_{i}^{\mathcal{Z}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}I\_{i}^{\mathcal{Z}}\circ P\_{i}^{\mathcal{Z}}:\mathcal{Z}\to\mathcal{Z} |  | (5.16) |

are all 11-Lipschitz linear operators of (finite) rank ii.
Second, since 𝒦\mathcal{K} is compact then the MAP implies that: for every “dimension reduction error” εD>0\varepsilon\_{D}>0 there exists some I∈ℕ+I\in\mathbb{N}\_{+}, depending only on εD\varepsilon\_{D} and on the compact set 𝒦\mathcal{K}, satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | supx∈𝒦‖AIℋ​(x−x⋆)−(x−x⋆)‖ℋ≤εD1/α(2​L)1/α⏟(IV):Dimension-Reduction: Domain​ and ​supy∈f​(𝒦)∪{y⋆}‖AIℳ2​(𝒯,U)​(y)−y‖ℋ≤εD2⏟(V):Dimension-Reduction: Range.\underbrace{\sup\_{x\in\mathcal{K}}\,\|A\_{I}^{\mathcal{H}}(x-x^{\star})-(x-x^{\star})\|\_{\mathcal{H}}\leq\frac{\varepsilon\_{D}^{1/\alpha}}{(2L)^{1/\alpha}}}\_{\textup{(IV)}:\,\text{Dimension-Reduction: Domain}}\mbox{ and }\underbrace{\sup\_{y\in f(\mathcal{K})\cup\{y^{\star}\}}\,\|A\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}(y)-y\|\_{\mathcal{H}}\leq\frac{\varepsilon\_{D}}{2}}\_{\textup{(V)}:\text{Dimension-Reduction: Range}}. |  | (5.17) |

In the special case where 𝒦\mathcal{K} and f​(𝒦)f(\mathcal{K}) are both (ρ,r)(\rho,r)-exponentially ellipsoidal with respect to the respective bases (ei)i∈I(e\_{i})\_{i\in I} and (ηj)j∈J(\eta\_{j})\_{j\in J} (cf. Definition ([3.3](https://arxiv.org/html/2510.20017v1#S3.E3 "Equation 3.3 ‣ Definition 3.1 ((𝜌,𝑟)-Exponentially Ellipsoidal). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))) then, we may quantify the dependence of II and on εD,r,ρ\varepsilon\_{D},r,\rho as follows: for each x∈𝒦x\in\mathcal{K}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖AIℋ​(x−x⋆)−(x−x⋆)‖ℋ\displaystyle\|A\_{I}^{\mathcal{H}}(x-x^{\star})-(x-x^{\star})\|\_{\mathcal{H}} | =‖∑i>I⟨x−x⋆,ei⟩​ei‖\displaystyle=\big\|\sum\_{i>I}\,\langle x-x^{\star},e\_{i}\rangle e\_{i}\big\| |  | (5.18) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑i>I‖⟨x−x⋆,ei⟩‖​‖ei‖\displaystyle\leq\sum\_{i>I}\,\big\|\langle x-x^{\star},e\_{i}\rangle\big\|\,\|e\_{i}\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑i>I‖⟨x−x⋆,ei⟩‖\displaystyle=\sum\_{i>I}\,\big\|\langle x-x^{\star},e\_{i}\rangle\big\| |  | (5.19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤∑i>Iρ​e−r​i\displaystyle\leq\sum\_{i>I}\,\rho\,e^{-r\,i} |  | (5.20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤ρ​∫I∞e−r​u​𝑑u=ρ​e−r​Ir,\displaystyle\leq\rho\,\int\_{I}^{\infty}e^{-r\,u}\,du=\frac{\rho\,e^{-rI}}{r}, |  | (5.21) |

where ([5.19](https://arxiv.org/html/2510.20017v1#S5.E19 "Equation 5.19 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) follows since each {ei}i∈I\{e\_{i}\}\_{i\in I} is a unit vector and ([5.20](https://arxiv.org/html/2510.20017v1#S5.E20 "Equation 5.20 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) follows from the exponentially ellipsoidal hypothesis on 𝒦\mathcal{K}. Thus, ([5.18](https://arxiv.org/html/2510.20017v1#S5.E18 "Equation 5.18 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([5.21](https://arxiv.org/html/2510.20017v1#S5.E21 "Equation 5.21 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) imply that any choice of I∈ℕ+I\in\mathbb{N}\_{+} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | I≥log⁡((2​L​ρ)1/(α​r)r1/r​εD1/(α​r))I\geq\log\biggl(\frac{(2L\rho)^{1/(\alpha r)}}{r^{1/r}\varepsilon\_{D}^{1/(\alpha r)}}\biggr) |  | (5.22) |

ensures that ([5.17](https://arxiv.org/html/2510.20017v1#S5.E17 "Equation 5.17 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) holds. A nearly identical computation shows that ([5.17](https://arxiv.org/html/2510.20017v1#S5.E17 "Equation 5.17 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) holds if II satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | I≥log⁡((ρ​2)1/r(r​εD)1/r).I\geq\log\biggl(\frac{(\rho 2)^{1/r}}{(r\varepsilon\_{D})^{1/r}}\biggr). |  | (5.23) |

In view of combining ([5.22](https://arxiv.org/html/2510.20017v1#S5.E22 "Equation 5.22 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([5.23](https://arxiv.org/html/2510.20017v1#S5.E23 "Equation 5.23 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and since 1/α≥11/\alpha\geq 1 and log\log is monotonically increasing; then, it is enough to set

|  |  |  |  |
| --- | --- | --- | --- |
|  | I=def.⌈log⁡(ρ1/(α​r)​(2​L)1/(α​r)r1/r​εD1/(α​r))⌉∈𝒪​(log⁡(ρ1/(α​r)​L1/(α​r)r1/r​εD1/(α​r)))I\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\Biggl\lceil\log\biggl(\frac{\rho^{1/(\alpha r)}(2L)^{1/(\alpha r)}}{r^{1/r}\varepsilon\_{D}^{1/(\alpha r)}}\biggr)\Biggr\rceil\in\mathcal{O}\Biggl(\log\biggl(\frac{\rho^{1/(\alpha r)}L^{1/(\alpha r)}}{r^{1/r}\varepsilon\_{D}^{1/(\alpha r)}}\biggr)\Biggr) |  | (5.24) |

in order to ensure that both conditions in ([5.17](https://arxiv.org/html/2510.20017v1#S5.E17 "Equation 5.17 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) are simultaneously satisfied.
If we couple the radius, ρ\rho, of the ellipsoidal set 𝒦\mathcal{K} to the dimension reduction error εD\varepsilon\_{D} via

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ∈𝒪​(εD)\rho\in\mathcal{O}(\varepsilon\_{D}) |  | (5.25) |

then II becomes independent of the dimension reduction error since

|  |  |  |  |
| --- | --- | --- | --- |
|  | I=⌈r​log⁡(r−1​(2​L)1/(α​r))⌉∈𝒪​(1).I=\lceil r\log(r^{-1}(2L)^{1/(\alpha r)})\rceil\in\mathcal{O}(1). |  | (5.26) |

We will return to the observation in ([5.26](https://arxiv.org/html/2510.20017v1#S5.E26 "Equation 5.26 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) at the end of the proof.

Step 3 - Approximation Error Decomposition:
For any ReLU\operatorname{ReLU} MLP f^:ℝI→ℝI\hat{f}:\mathbb{R}^{I}\to\mathbb{R}^{I}, to be specified retroactively, consider the induced residual NO (RNO) given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^​(u)=def.IIℳ2​(𝒯,U)∘f^∘PIℋ​(u)+y⋆\hat{F}(u)\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ\hat{f}\circ P\_{I}^{\mathcal{H}}(u)+y^{\star} |  | (5.27) |

where u∈ℋu\in\mathcal{H}; note we have chosen our base-points x⋆x^{\star} and y⋆y^{\star} in Definition [2.1](https://arxiv.org/html/2510.20017v1#S2.Thmdefinition1 "Definition 2.1 (Residually-Guided Neural Operator (RNO)). ‣ 2.3 Infinite-Dimensional Deep Learning: Neural Operator ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") according to ([5.15](https://arxiv.org/html/2510.20017v1#S5.E15 "Equation 5.15 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
Thus, ([5.15](https://arxiv.org/html/2510.20017v1#S5.E15 "Equation 5.15 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) implies that for all Δ​x∈Δ​𝒦\Delta x\in\Delta\mathcal{K} write x=def.Δ​x+x⋆x\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\Delta x+x^{\star}

|  |  |  |
| --- | --- | --- |
|  | (VI)=def.‖F^​(Δ​x)−f​(x)‖ℳ2​(𝒯,U)=‖IIℳ2​(𝒯,U)∘f^∘PIℋ​(x)−rf​(Δ​x)‖ℳ2​(𝒯,U).\displaystyle\textup{(VI)}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\big\|\hat{F}(\Delta x)-f(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}=\|I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ\hat{f}\circ P\_{I}^{\mathcal{H}}(x)-r\_{f}(\Delta x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}. |  |

Consequently, ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex14 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) may be bounded above, for each Δ​x∈Δ​𝒦\Delta x\in\Delta\mathcal{K} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex14 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) | =‖IIℳ2​(𝒯,U)∘f^∘PIℋ​(x)−rf​(x)‖ℳ2​(𝒯,U)\displaystyle=\big\|I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ\hat{f}\circ P\_{I}^{\mathcal{H}}(x)-r\_{f}(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖IIℳ2​(𝒯,U)∘(f^∘PIℋ​(x))−((IIℳ2​(𝒯,U)∘PIℳ2​(𝒯,U))∘rf∘(IIℋ∘PIℋ)​(x))‖ℳ2​(𝒯,U)⏟(VII)\displaystyle\leq\underbrace{\big\|I^{\mathcal{M}^{2}({\mathcal{T}},U)}\_{I}\circ\big(\hat{f}\circ P\_{I}^{\mathcal{H}}(x)\big)-\big((I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\circ r\_{f}\circ(I\_{I}^{\mathcal{H}}\circ P\_{I}^{\mathcal{H}})(x)\big)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}}\_{\textup{(VII)}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +‖((IIℳ2​(𝒯,U)∘PIℳ2​(𝒯,U))∘rf∘(IIℋ∘PIℋ)​(x))−((IIℳ2​(𝒯,U)∘PIℳ2​(𝒯,U))∘rf​(x))‖ℳ2​(𝒯,U)⏟(VIII)\displaystyle+\underbrace{\big\|\big((I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\circ r\_{f}\circ(I\_{I}^{\mathcal{H}}\circ P\_{I}^{\mathcal{H}})(x)\big)-\big((I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\circ r\_{f}(x)\big)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}}\_{\textup{(VIII)}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +‖((IIℳ2​(𝒯,U)∘PIℳ2​(𝒯,U))∘rf​(x))−rf​(x)‖ℳ2​(𝒯,U)⏟(IX)\displaystyle+\underbrace{\big\|\big((I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\circ r\_{f}(x)\big)-r\_{f}(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}}\_{\textup{(IX)}} |  |

Our objective is to bound the approximation error ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex14 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), which we will accomplish by bounding each of the individual errors ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex16 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex17 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), and ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex18 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")); which we now do.

Step 4: Bounding the Individual Errors:
First, by ([5.17](https://arxiv.org/html/2510.20017v1#S5.E17 "Equation 5.17 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex18 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) | =‖((IIℳ2​(𝒯,U)∘PIℳ2​(𝒯,U))∘rf​(x))−rf​(x)‖ℳ2​(𝒯,U)\displaystyle=\big\|\big((I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\circ r\_{f}(x)\big)-r\_{f}(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)} |  | (5.28) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤supy∈f​(𝒦)‖((IIℳ2​(𝒯,U)∘PIℳ2​(𝒯,U))​(y))−y‖ℋα≤εD2.\displaystyle\leq\sup\_{y\in f(\mathcal{K})}\big\|\big((I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})(y)\big)-y\big\|\_{\mathcal{H}}^{\alpha}\leq\frac{\varepsilon\_{D}}{2}. |  | (5.29) |

Next, using ([5.17](https://arxiv.org/html/2510.20017v1#S5.E17 "Equation 5.17 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we control ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex17 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex17 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) | ≤Lip⁡(IIℳ2​(𝒯,U))​Lip⁡(PIℳ2​(𝒯,U))​Lipα⁡(rf)​‖((IIℋ∘PIℋ)​(x))−x‖ℳ2​(𝒯,U)α\displaystyle\leq\operatorname{Lip}(I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\operatorname{Lip}(P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\operatorname{Lip}\_{\alpha}(r\_{f})\big\|\big((I\_{I}^{\mathcal{H}}\circ P\_{I}^{\mathcal{H}})(x)\big)-x\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}^{\alpha} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤Lip⁡(IIℳ2​(𝒯,U))​Lip⁡(PIℳ2​(𝒯,U))​Lipα⁡(f)​‖((IIℋ∘PIℋ)​(x))−x‖ℳ2​(𝒯,U)α\displaystyle\leq\operatorname{Lip}(I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\operatorname{Lip}(P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\operatorname{Lip}\_{\alpha}(f)\big\|\big((I\_{I}^{\mathcal{H}}\circ P\_{I}^{\mathcal{H}})(x)\big)-x\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}^{\alpha} |  | (5.30) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supx∈𝒦L​‖((IIℋ∘PIℋ)​(x))−x‖ℳ2​(𝒯,U)α\displaystyle\leq\sup\_{x\in\mathcal{K}}\,L\big\|\big((I\_{I}^{\mathcal{H}}\circ P\_{I}^{\mathcal{H}})(x)\big)-x\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}^{\alpha} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supx∈𝒦L​(εD1/α(2​L)1/α)α\displaystyle\leq\sup\_{x\in\mathcal{K}}\,L\Big(\frac{\varepsilon\_{D}^{1/\alpha}}{(2L)^{1/\alpha}}\Big)^{\alpha} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =εD2.\displaystyle=\frac{\varepsilon\_{D}}{2}. |  | (5.31) |

Consequently, all the dimension reduction errors in ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex14 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) have been bounded above leading to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex14 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) | ≤εD+Lip⁡(IIℳ2​(𝒯,U))​‖(f^∘PIℋ​(x))−(PIℳ2​(𝒯,U)∘rf∘(IIℋ∘PIℋ)​(x))‖ℝI\displaystyle\leq\varepsilon\_{D}+\operatorname{Lip}(I^{\mathcal{M}^{2}({\mathcal{T}},U)}\_{I})\big\|\big(\hat{f}\circ P\_{I}^{\mathcal{H}}(x)\big)-\big(P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ r\_{f}\circ(I\_{I}^{\mathcal{H}}\circ P\_{I}^{\mathcal{H}})(x)\big)\big\|\_{\mathbb{R}^{I}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤εD+supu∈𝒦I∥f^(u)−(PIℳ2​(𝒯,U)∘rf∘(IIℋ(u))∥ℝI⏟(X)\displaystyle\leq\varepsilon\_{D}+\underbrace{\sup\_{u\in\mathcal{K}\_{I}}\big\|\hat{f}(u)-\big(P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ r\_{f}\circ(I\_{I}^{\mathcal{H}}(u)\big)\big\|\_{\mathbb{R}^{I}}}\_{\textup{(X)}} |  | (5.32) |

where 𝒦I=def.PIℋ​(𝒦)\mathcal{K}\_{I}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}P\_{I}^{\mathcal{H}}(\mathcal{K}) is compact (by to the compactness of 𝒦\mathcal{K} and the continuity of PIℋP\_{I}^{\mathcal{H}}).
Remark that the map fI:ℝI→ℝIf\_{I}:\mathbb{R}^{I}\to\mathbb{R}^{I} given for any u∈𝒦Iu\in\mathcal{K}\_{I} by
fI(u)=def.PIℳ2​(𝒯,U)∘rf∘(IIℋ(u)f\_{I}(u)\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ r\_{f}\circ(I\_{I}^{\mathcal{H}}(u) is (L,α)(L,\alpha)-Hölder continuous since PIℳ2​(𝒯,U)P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)} and IIℋI\_{I}^{\mathcal{H}} are both 11-Lipschitz and since rfr\_{f} is (L,α)(L,\alpha)-Hölder continuous. Thus, for every C∈ℕ+C\in\mathbb{N}\_{+} (to be set retroactively), upon applying [retroactively, Corollary 5.1] pick f^\hat{f} to be a (globally) (L,α)(L,\alpha)-Hölder continuous ReLU MLP with depth ⌈log2⁡(I)⌉+5\lceil\log\_{2}(I)\rceil+5, width 8​I​(1+C)I8\,I(1+C)^{I}, with at-most 18​I​(1+C)I18\,I(1+C)^{I} non-zero (trainable) parameters such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxu∈𝒦I⁡‖f^​(u)−fI​(u)‖2≤L​(I/2​C)α.\max\_{u\in\mathcal{K}\_{I}}\,\|\hat{f}(u)-f\_{I}(u)\|\_{2}\leq L(I/2C)^{\alpha}. |  | (5.33) |

Retroactively, setting the connectivity parameter CC to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=def.⌈I2​(LεA)1/α⌉\displaystyle C\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\biggl\lceil\frac{I}{2}\biggl(\frac{L}{\varepsilon\_{A}}\biggr)^{1/\alpha}\biggr\rceil |  | (5.34) |

implies that ([5.32](https://arxiv.org/html/2510.20017v1#S5.E32 "Equation 5.32 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) is at most εA\varepsilon\_{A}. Further, this determines the ReLU MLP f^\hat{f}. Our bound on ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex14 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) is complete since the inequality in ([5.32](https://arxiv.org/html/2510.20017v1#S5.E32 "Equation 5.32 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) has further reduced to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex14 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) | ≤εD+εA.\displaystyle\leq\varepsilon\_{D}+\varepsilon\_{A}. |  |

Let ε>0\varepsilon>0 and retroactively couple εD=εA=def.ε/2\varepsilon\_{D}=\varepsilon\_{A}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\varepsilon/2.
It only remains to tally parameters.
Combining our estimate for the latent dimension II in ([5.24](https://arxiv.org/html/2510.20017v1#S5.E24 "Equation 5.24 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) with the estimate in ([5.34](https://arxiv.org/html/2510.20017v1#S5.E34 "Equation 5.34 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) yields

|  |  |  |
| --- | --- | --- |
|  | C=⌈I​L1/α​r−r​(2−1​ε)−1/α⌉∈𝒪​(log⁡((C​L)1/(α​r)​r−1/r​(2−1​ε)−1/(α​r))​L1/α​(2−1​ε)−1/α).\displaystyle\begin{aligned} C&=\big\lceil IL^{1/\alpha}r^{-r}(2^{-1}\varepsilon)^{-1/\alpha}\big\rceil\\ &\in\mathcal{O}\biggl(\log\biggl((CL)^{1/(\alpha r)}\,r^{-1/r}(2^{-1}\varepsilon)^{-1/(\alpha r)}\biggr)\,L^{1/\alpha}\,(2^{-1}\varepsilon)^{-1/\alpha}\biggr).\end{aligned} |  |

Similarly, f^\hat{f} has a depth of at-most

|  |  |  |
| --- | --- | --- |
|  | ⌈log2⁡(I)⌉+5=⌈log2⁡(⌈log⁡(ρ1/(α​r)​(2​L)1/(α​r)​r−1/r​(ε/2)−1/(α​r))⌉)⌉+5\lceil\log\_{2}(I)\rceil+5=\Biggl\lceil\log\_{2}\Biggl(\Biggl\lceil\log\biggl(\rho^{1/(\alpha r)}(2L)^{1/(\alpha r)}\,r^{-1/r}(\varepsilon/2)^{-1/(\alpha r)}\biggr)\Biggr\rceil\Biggr)\Biggr\rceil+5 |  |

and a width of the order of

|  |  |  |  |
| --- | --- | --- | --- |
|  | W=def.8​log⁡((C​L)r/α​r−r​(2−1​εA)−1/(α​r))×(1+⌈(log⁡((C​L)1/(α​r)​r−1/r​(2−1​εA)−1/(α​r)))2​(L(2−1​ε))1/α⌉)⌈log⁡(ρr/α​(2​L)1/(α​r)​r−r​(2−1​εD))⌉\begin{aligned} W\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}&8\,\log\big((CL)^{r/\alpha}\,r^{-r}(2^{-1}\varepsilon\_{A})^{-1/(\alpha r)}\big)\\ &\times\biggl(1+\biggl\lceil\frac{\big(\log\big((CL)^{1/(\alpha r)}\,r^{-1/r}(2^{-1}\varepsilon\_{A})^{-1/(\alpha r)}\big)\big)}{2}\biggl(\frac{L}{(2^{-1}\varepsilon)}\biggr)^{1/\alpha}\biggr\rceil\biggr)^{\Biggl\lceil\log\biggl(\rho^{r/\alpha}(2L)^{1/(\alpha r)}\,r^{-r}(2^{-1}\varepsilon\_{D})\biggr)\Biggr\rceil}\end{aligned} |  | (5.35) |

and the number of non-zero parameters are the same up to a (constant) multiple of WW, namely 9/49/4.

The Special Case of Exponentially Ellipsoidal Sets with Scaling Radii
  
If we scale the “ellipsoidal radius” ρ\rho of the relevant compact set by retroactively coupling
ρ=def.ε\rho\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\varepsilon, mirroring ([5.25](https://arxiv.org/html/2510.20017v1#S5.E25 "Equation 5.25 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
Then, the exponent in ([5.35](https://arxiv.org/html/2510.20017v1#S5.E35 "Equation 5.35 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) becomes

|  |  |  |
| --- | --- | --- |
|  | c~r,α=def.⌈log⁡((2​L)r/α​2r/α​r−1/r​(ρ/ε)1/(α​r))⌉=⌈log⁡((4​L)1(α​r)r1/r)⌉.\tilde{c}\_{r,\alpha}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\Biggl\lceil\log\biggl((2L)^{r/\alpha}2^{r/\alpha}\,\,r^{-1/r}\Big(\rho/\varepsilon\Big)^{1/(\alpha r)}\biggr)\Biggr\rceil=\Biggl\lceil\log\biggl(\frac{(4L)^{\frac{1}{(\alpha r)}}}{r^{1/r}}\biggr)\Biggr\rceil. |  |

Setting cr,α=def.c~r,α/αc\_{r,\alpha}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\tilde{c}\_{r,\alpha}/\alpha; then, ([5.35](https://arxiv.org/html/2510.20017v1#S5.E35 "Equation 5.35 ‣ 5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) ameliorates to

W∈𝒪​(ε−cr,α​log⁡(ε−1)).W\in\mathcal{O}\Big(\varepsilon^{-c\_{r,\alpha}}\log(\varepsilon^{-1})\Big).
Similarly, the depth Δ\Delta of f^\hat{f} ameliorates to
Δ=⌈log2⁡(⌈log⁡((4​L)r/α​r−r)⌉)⌉+5∈𝒪​(1)\Delta=\Big\lceil\log\_{2}\Big(\Big\lceil\log\big((4L)^{r/\alpha}r^{-r}\big)\Big\rceil\Big)\Big\rceil+5\in\mathcal{O}(1).

This completes the main portion of the proof. It only remains to verify the “base-point preserving property” of F^\hat{F}; i.e. that F^​(0)=y⋆\hat{F}(0)=y^{\star}.

Verifying the Pointedness of F^−y⋆\hat{F}-y^{\star}:
Since 0∈𝒦0\in\mathcal{K} and by the linearity of PIℋP\_{I}^{\mathcal{H}} we have

|  |  |  |
| --- | --- | --- |
|  | PIℋ​(0)=0∈ℝI.P\_{I}^{\mathcal{H}}(0)=0\in\mathbb{R}^{I}. |  |

Note also that, since rf​(0)r\_{f}(0) then again the linearity of II𝒵I\_{I}^{\mathcal{Z}} and PI𝒵P\_{I}^{\mathcal{Z}} for 𝒵∈{ℋ,ℳ2​(𝒯,U)}\mathcal{Z}\in\{\mathcal{H},\mathcal{M}^{2}({\mathcal{T}},U)\} implies that the finite-dimensional version of our target residual function (IIℳ2​(𝒯,U)∘PIℳ2​(𝒯,U))∘rf∘(IIℋ∘PIℋ)(x)):ℝI→ℝI(I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ P\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)})\circ r\_{f}\circ(I\_{I}^{\mathcal{H}}\circ P\_{I}^{\mathcal{H}})(x)\big):\mathbb{R}^{I}\to\mathbb{R}^{I} in ([5.2](https://arxiv.org/html/2510.20017v1#S5.Ex16 "5.2 Approximation Guarantees ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) fixes 0. Since f^\hat{f} was constructed using [Hong and Kratsios, [2024](https://arxiv.org/html/2510.20017v1#bib.bib43), Corollary 5.1]; then the “ample-interpolation” property of the ReLU MLP f^\hat{f} guaranteed by [Hong and Kratsios, [2024](https://arxiv.org/html/2510.20017v1#bib.bib43), Theorem 4.1] implies that f^​(0)=rf​(0)=0\hat{f}(0)=r\_{f}(0)=0. Again appealing to the linearity of IIℳ2​(𝒯,U)I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)} we have that

|  |  |  |
| --- | --- | --- |
|  | F^​(0)−y⋆=IIℳ2​(𝒯,U)∘f^∘PIℋ​(0)+y^⋆−y^⋆=0.\hat{F}(0)-y^{\star}=I\_{I}^{\mathcal{M}^{2}({\mathcal{T}},U)}\circ\hat{f}\circ P\_{I}^{\mathcal{H}}(0)+\hat{y}^{\star}-\hat{y}^{\star}=0. |  |

This yields the last statement and concludes our proof.
∎

### 5.3 Completing the Proof of the Main Learning Guarantee

Equipped with the regular universal approximation guarantee from Proposition LABEL:prop:theorem\_universality\_\_regular and the oracle-type inequality in Proposition [5.3](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem3 "Proposition 5.3 (Regularity-Based Oracle Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), we are now in a position to present our main abstract learning guarantee.
We first work out the general case, then specialize to the exponentially ellipsoidal case.

###### Proposition 5.5 (Learnability).

Consider the setting of Proposition LABEL:prop:theorem\_universality\_\_regular
and suppose that Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") (ii) is generalized to Yn=f​(Xn)Y\_{n}=f(X\_{n}) for n=1,…,Nn=1,\dots,N, holds.
For every approximation error ε>0\varepsilon>0, and a failure probability 0<δ≤10<\delta\leq 1.
For compact every 𝒦⊂ℋ\mathcal{K}\subset\mathcal{H} of positive ℙX\mathbb{P}\_{X}-measure containing101010I.e. ℙX​(𝒦)>0\mathbb{P}\_{X}(\mathcal{K})>0 and 0∈𝒦0\in\mathcal{K}. 0 and each LL-Lipschitz target function f:𝒦→ℳ2​(𝒯,U)f:\mathcal{K}\to\mathcal{M}^{2}({\mathcal{T}},U):
there is a connectivity parameter C=def.C​(ϵ,δ,𝒦)∈ℕ+C\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}C(\epsilon,\delta,\mathcal{K})\in\mathbb{N}\_{+} such that for any empirical risk minimizer F^∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)\hat{F}\in\mathcal{RNO}^{1,L}\_{C}(e\_{\cdot},\eta\_{\cdot}); i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^S​(F^)=infF~∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)ℛ^S​(F~).\hat{\mathcal{R}}^{S}(\hat{F})=\inf\_{\tilde{F}\in\mathcal{RNO}^{1,L}\_{C}(e\_{\cdot},\eta\_{\cdot})}\,\hat{\mathcal{R}}^{S}(\tilde{F}). |  | (5.36) |

and the following holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ℛ​(F^)≤ε+L¯​e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N)≥pN−δ,\displaystyle\mathbb{P}\biggl(\mathcal{R}(\hat{F})\leq\varepsilon+\bar{L}e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}\bigg)\geq p^{N}-\delta, |  | (5.37) |

where
p=def.ℙX​(𝒦)p\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\mathbb{P}\_{X}(\mathcal{K}) and (
L¯=def.2​max⁡{L,1}\bar{L}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}2\max\{L,1\}, where r>0r>0 is as in Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") (iii).
  
If, additionally, there exists some r¯>0\bar{r}>0 such that 𝒦\mathcal{K} is (ε,r¯)(\varepsilon,\bar{r})-exponentially ellipsoidal111111Cf. Definition [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmdefinition1 "Definition 3.1 ((𝜌,𝑟)-Exponentially Ellipsoidal). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"). then, F^\hat{F} has depth 𝒪​(1)\mathcal{O}(1) and both the width and the number of non-zero parameters of F^\hat{F} are 𝒪​(ε−cr¯,α​log⁡(ε−1))\mathcal{O}\big(\varepsilon^{-c\_{\bar{r},\alpha}}\log(\varepsilon^{-1})\big); where
cr¯,α=def.1α​⌈log⁡(4​L¯)r¯​α−log⁡(r¯)r¯⌉c\_{\bar{r},\alpha}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\frac{1}{\alpha}\Big\lceil\tfrac{\log(4\bar{L})}{\bar{r}\alpha}-\tfrac{\log(\bar{r})}{\bar{r}}\Big\rceil.

###### Proof of Proposition [5.5](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem5 "Proposition 5.5 (Learnability). ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

Suppose that 𝒦\mathcal{K} has positive ℙX\mathbb{P}\_{X} measure. Since each F~∈ℛ​𝒩​𝒪C1,L​(e⋅,η⋅)\tilde{F}\in\mathcal{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot}) and the target function ff are LL-Lipschitz, and since every element of RNOC1,L⁡(e⋅,η⋅)\operatorname{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot}) fixes the origin–i.e. maps the zero vector to the zero vector in their respective spaces–then, Proposition [5.3](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem3 "Proposition 5.3 (Regularity-Based Oracle Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") applies with ℱ=def.RNOC1,L⁡(e⋅,η⋅)\mathcal{F}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\operatorname{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot}); whence, for every empirical risk minimizer F^∈RNOC1,L⁡(e⋅,η⋅)\hat{F}\in\operatorname{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot}) (i.e. satisfying ([5.3](https://arxiv.org/html/2510.20017v1#S5.E3 "Equation 5.3 ‣ Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and thus satisfying ([5.36](https://arxiv.org/html/2510.20017v1#S5.E36 "Equation 5.36 ‣ Proposition 5.5 (Learnability). ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))) the following holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ​(F^)≤infF~∈RNOC1,L⁡(e⋅,η⋅)supx∈𝒦‖F~​(x)−F​(x)‖ℳ2​(𝒯,U)⏟([5.1](https://arxiv.org/html/2510.20017v1#S5.Ex1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))+L¯​e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N⏟([5.3](https://arxiv.org/html/2510.20017v1#S5.Ex10 "Proposition 5.3 (Regularity-Based Oracle Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))\displaystyle\mathcal{R}(\hat{F})\leq\underbrace{\inf\_{\tilde{F}\in\operatorname{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot})}\,\sup\_{x\in\mathcal{K}}\|\tilde{F}(x)-F(x)\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}}\_{\eqref{t:apprx}}+\bar{L}\underbrace{e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}}\_{\eqref{t:stat\_II}} |  | (5.38) |

with probability at-least 1−(1−ℙX​(𝒦))N−δ1-(1-\mathbb{P}\_{X}(\mathcal{K}))^{N}-\delta.

As term ([5.3](https://arxiv.org/html/2510.20017v1#S5.Ex10 "Proposition 5.3 (Regularity-Based Oracle Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) converges to 0 as the sample size NN tends to infinity, it only remains to control the approximation error–expressed by term ([5.1](https://arxiv.org/html/2510.20017v1#S5.Ex1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
Since the target function ff is LL-Lipschitz, i.e. (1,L)(1,L)-Hölder, and since 𝒦\mathcal{K} is compact then Proposition LABEL:prop:theorem\_universality\_\_regular applies upon
setting the depth, width, and connectivity parameters large enough to guarantee the existence of some
F^∈RNOC1,L⁡(e⋅,η⋅)\hat{F}\in\operatorname{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot}) satisfying ([5.36](https://arxiv.org/html/2510.20017v1#S5.E36 "Equation 5.36 ‣ Proposition 5.5 (Learnability). ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supx∈𝒦‖F^​(Δ​x)−f​(x)‖ℳ2​(𝒯,U)≤ε.\displaystyle\sup\_{x\in\mathcal{K}}\,\big\|\hat{F}(\Delta x)-f(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\varepsilon. |  | (5.39) |

If, additionally, there exists some r¯>0\bar{r}>0 such that 𝒦\mathcal{K} is (ε,r¯)(\varepsilon,\bar{r})-exponentially ellipsoidal then
there F^\hat{F} can be guaranteed to have 𝒪​(1)\mathcal{O}(1), width and number of non-zero parameters (CC) at-most 𝒪​(ε−cr¯,α​log⁡(ε−1))\mathcal{O}\big(\varepsilon^{-c\_{\bar{r},\alpha}}\log(\varepsilon^{-1})\big); where cr¯,α=def.1α​⌈log⁡((4​L¯)1r¯​αr¯1/r¯)⌉c\_{\bar{r},\alpha}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\frac{1}{\alpha}\Big\lceil\log\big(\tfrac{(4\bar{L})^{\frac{1}{\bar{r}\alpha}}}{\bar{r}^{1/\bar{r}}}\big)\Big\rceil.
Consequently, the uniform bound in ([5.39](https://arxiv.org/html/2510.20017v1#S5.E39 "Equation 5.39 ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ([5.1](https://arxiv.org/html/2510.20017v1#S5.Ex1 "Lemma 5.1 (A General Transport-Theoretic Oracle-Type Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))=infF~∈RNOC1,L⁡(e⋅,η⋅)supx∈𝒦‖F^⋆​(Δ​x)−f⋆​(x)‖ℳ2​(𝒯,U)≤supx∈𝒦‖F^⋆​(Δ​x)−f⋆​(x)‖ℳ2​(𝒯,U)≤ε.\displaystyle\eqref{t:apprx}=\inf\_{\tilde{F}\in\operatorname{RNO}\_{C}^{1,L}(e\_{\cdot},\eta\_{\cdot})}\sup\_{x\in\mathcal{K}}\,\big\|\hat{F}^{\star}(\Delta x)-f^{\star}(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\sup\_{x\in\mathcal{K}}\,\big\|\hat{F}^{\star}(\Delta x)-f^{\star}(x)\big\|\_{\mathcal{M}^{2}({\mathcal{T}},U)}\leq\varepsilon. |  | (5.40) |

Incorporating the estimate in ([5.40](https://arxiv.org/html/2510.20017v1#S5.E40 "Equation 5.40 ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) back into ([5.40](https://arxiv.org/html/2510.20017v1#S5.E40 "Equation 5.40 ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ​(F^)≤ε+L¯​e−log⁡(N2​r)+ln⁡(2δ)N+ln⁡(2δ)N⏟([5.3](https://arxiv.org/html/2510.20017v1#S5.Ex10 "Proposition 5.3 (Regularity-Based Oracle Inequality). ‣ 5.1 Oracle Inequalities ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))\displaystyle\mathcal{R}(\hat{F})\leq\varepsilon+\bar{L}\underbrace{e^{-\sqrt{\log(N^{2r})}}+\frac{\ln\big(\frac{2}{\delta}\big)}{N}+\frac{\sqrt{\ln\big(\frac{2}{\delta}\big)}}{\sqrt{N}}}\_{\eqref{t:stat\_II}} |  | (5.41) |

holds with probability at-least 1−(1−ℙX​(𝒦)N)−δ=ℙX​(𝒦)N−δ1-(1-\mathbb{P}\_{X}(\mathcal{K})^{N})-\delta=\mathbb{P}\_{X}(\mathcal{K})^{N}-\delta.
∎

### 5.4 Proof of Theorem [3.8](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem8 "Theorem 3.8 (Quantitative Refinement of Theorem 3.6). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

It remains to control the probability of obtaining all NN samples on the exponentially ellipsoidal set given in the previous proposition. Indeed, under Assumption [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmassumption1 "Assumption 3.1 (Tempered Sampling). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), we have the following guarantee.

###### Lemma 5.6.

Let ρ≥0\rho\geq 0, r>0r>0, and let 𝒦⊆ℋ\mathcal{K}\subseteq\mathcal{H} be exponentially (ρ,r)(\rho,r)-exponentially ellipsoidal and contain the origin 0∈ℋ0\in\mathcal{H}.
Fix a “sampling failure probability” 0<δX≤10<\delta\_{X}\leq 1, and assume that ℙX\mathbb{P}\_{X} further satisfies Assumption [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmassumption1 "Assumption 3.1 (Tempered Sampling). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(X1∈𝒦)≥1−δX.\mathbb{P}(X\_{1}\in\mathcal{K})\geq 1-\delta\_{X}. |  | (5.42) |

###### Proof of Lemma [5.6](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem6 "Lemma 5.6. ‣ 5.4 Proof of Theorem 3.8 ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

Since we have assumed that, for all i∈ℕ+i\in\mathbb{N}\_{+} and every t≥0t\geq 0 ℙ​(|Zi|≥t)≤2​e−t2/2\mathbb{P}(|Z\_{i}|\geq t)\leq 2e^{-t^{2}/2} then the independence of the {Zi}i=1∞\{Z\_{i}\}\_{i=1}^{\infty}, the relationship between X1∼X∼ℙXX\_{1}\sim X\sim\mathbb{P}\_{X} in ([2.9](https://arxiv.org/html/2510.20017v1#S2.E9 "Equation 2.9 ‣ Item (iii) ‣ Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), Assumption [2.3](https://arxiv.org/html/2510.20017v1#S2.Thmassumption3 "Assumption 2.3 (Data Generating Distribution’s Structure). ‣ 2.2 Statistics in Infinite Dimensions ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), and the definition of (ρ,r)(\rho,r)-exponentially ellipsoidal sets, implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(X∈𝒦)=ℙ​((∀i∈ℕ+)​|σi​Zi|≤ρ​e−r​i)=∏i=1∞ℙ​(|σi​Zi|≤ρ​e−r​i)≥∏i=1∞(1−2​e−ti2/2​σi2).\mathbb{P}(X\in\mathcal{K})=\mathbb{P}((\forall i\in\mathbb{N}\_{+})|\sigma\_{i}\,Z\_{i}|\leq\rho e^{-ri})=\prod\_{i=1}^{\infty}\,\mathbb{P}(|\sigma\_{i}\,Z\_{i}|\leq\rho e^{-ri})\geq\prod\_{i=1}^{\infty}\,\big(1-2e^{-t\_{i}^{2}/2\sigma\_{i}^{2}}\big). |  | (5.43) |

Now, the constant on σi\sigma\_{i} in Assumption [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmassumption1 "Assumption 3.1 (Tempered Sampling). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")implies that: for every i∈ℕ+i\in\mathbb{N}\_{+} we have 1−2​e−ti2/2​σi2≥1−Δi1-2e^{-t\_{i}^{2}/2\sigma\_{i}^{2}}\geq 1-\Delta^{i}. Consequently, the left-hand side of ([5.43](https://arxiv.org/html/2510.20017v1#S5.E43 "Equation 5.43 ‣ 5.4 Proof of Theorem 3.8 ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) can be bounded below by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(X∈𝒦)≥∏i=1∞(1−2​e−ti2/2​σi2)≥∏i=1∞(1−Δi)≥exp⁡(−2​∑i=1∞Δi)=exp⁡(−2​Δ1−Δ).\mathbb{P}(X\in\mathcal{K})\geq\prod\_{i=1}^{\infty}\,\big(1-2e^{-t\_{i}^{2}/2\sigma\_{i}^{2}}\big)\geq\prod\_{i=1}^{\infty}\,\big(1-\Delta^{i}\big)\geq\exp\Big(-2\sum\_{i=1}^{\infty}\,\Delta^{i}\Big)=\exp\big(\tfrac{-2\Delta}{1-\Delta}\big). |  | (5.44) |

The definition of Δ\Delta, as coupled to δX\delta\_{X}, given in Assumption [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmassumption1 "Assumption 3.1 (Tempered Sampling). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") implies that exp⁡(−2​Δ1−Δ)=1−δX\exp\big(\tfrac{-2\Delta}{1-\Delta}\big)=1-\delta\_{X} which concludes our proof.
∎

###### Proof of Theorem [3.8](https://arxiv.org/html/2510.20017v1#S3.Thmtheorem8 "Theorem 3.8 (Quantitative Refinement of Theorem 3.6). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators").

In the setting of Proposition [5.5](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem5 "Proposition 5.5 (Learnability). ‣ 5.3 Completing the Proof of the Main Learning Guarantee ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") if, additionally Assumption [3.1](https://arxiv.org/html/2510.20017v1#S3.Thmassumption1 "Assumption 3.1 (Tempered Sampling). ‣ 3.2 Unlocking Favourable Rates ‣ 3 Main Results ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") holds with δX=e−δ/N\delta\_{X}=e^{-\delta/N} then the result following upon applying Lemma [5.6](https://arxiv.org/html/2510.20017v1#S5.Thmtheorem6 "Lemma 5.6. ‣ 5.4 Proof of Theorem 3.8 ‣ 5 Proof of Sample-Complexity Estimates and Approximation Guarantees ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"), since, in this setting, p=ℙX​(𝒦)≥δN=e−δ/Np=\mathbb{P}\_{X}(\mathcal{K})\geq\delta\_{N}=e^{-\delta/N}; whence pN−δ≥e−δ−δp^{N}-\delta\geq e^{-\delta}-\delta.
∎

## Acknowledgments

A. Kratsios and X. Yang acknowledge financial support from an NSERC Discovery Grant No. RGPIN-2023-04482 and No. DGECR-2023-00230, and they acknowledge that resources used in preparing this research were provided, in part, by the Province of Ontario, the Government of Canada through CIFAR, and companies sponsoring the Vector Institute121212<https://vectorinstitute.ai/partnerships/current-partners/>.
Dena Firoozi would like to acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC), grants RGPIN-2022-05337 and DGECR-2022-00468.

## References

* Bauso et al. [2016]

  D. Bauso, H. Tembine, T. Basar,
  Opinion dynamics in social networks through mean-field games,
  SIAM Journal on Control and Optimization 54 (2016) 3225–3257.
* Shrivats et al. [2022]

  A. V. Shrivats, D. Firoozi, S. Jaimungal,
  A mean-field game approach to equilibrium pricing in solar renewable energy certificate markets,
  Mathematical Finance 32 (2022) 779–824.
* Gomes and Saúde [2021]

  D. Gomes, J. Saúde,
  A mean-field game approach to price formation in electricity markets,
  Dynamic Games and Applications 11 (2021) 29–53.
* Fujii and Takahashi [2022]

  M. Fujii, A. Takahashi,
  A mean field game approach to equilibrium pricing with market clearing condition,
  SIAM Journal on Control and Optimization 60 (2022) 259–279.
* Laguzet and Turinici [2015]

  L. Laguzet, G. Turinici,
  Individual vaccination as nash equilibrium in a sir model with application to the 2009–2010 influenza a (h1n1) epidemic in france,
  Bulletin of mathematical biology 77 (2015) 1955–1984.
* Bauso et al. [2016]

  D. Bauso, X. Zhang, A. Papachristodoulou,
  Density flow in dynamical networks via mean-field games,
  IEEE Transactions on Automatic Control 62 (2016) 1342–1355.
* Del Moral et al. [2008]

  P. Del Moral, F. Patras, S. Rubenthaler, A mean field theory of nonlinear filtering, Ph.D. thesis, INRIA, 2008.
* Carrillo et al. [2024]

  J. A. Carrillo, F. Hoffmann, A. M. Stuart, U. Vaes,
  The mean-field ensemble kalman filter: near-gaussian setting,
  SIAM Journal on Numerical Analysis 62 (2024) 2549–2587.
* Ertel [2025]

  S. W. Ertel,
  On the mean field theory of ensemble kalman filters for spdes,
  SIAM/ASA Journal on Uncertainty Quantification 13 (2025) 891–930.
* Mei et al. [2019]

  S. Mei, T. Misiakiewicz, A. Montanari,
  Mean-field theory of two-layers neural networks: dimension-free bounds and kernel limit,
  in: Conference on learning theory, PMLR, 2019, pp. 2388–2464.
* Huang et al. [2006]

  M. Huang, R. P. Malhamé, P. E. Caines,
  Large population stochastic dynamic games: closed-loop McKean-Vlasov systems and the Nash certainty equivalence principle,
  Commun. Inf. Syst. 6 (2006) 221–251. URL: <https://doi.org/10.4310/cis.2006.v6.n3.a5>. doi:[10.4310/cis.2006.v6.n3.a5](http://dx.doi.org/10.4310/cis.2006.v6.n3.a5).
* Lasry and Lions [2007]

  J.-M. Lasry, P.-L. Lions,
  Mean field games,
  Japanese journal of mathematics 2 (2007) 229–260.
* Nguyen and Huang [2012]

  S. L. Nguyen, M. Huang,
  Linear-quadratic-gaussian mixed games with continuum-parametrized minor players,
  SIAM Journal on Control and Optimization 50 (2012) 2907–2937. doi:[10.1137/110841217](http://dx.doi.org/10.1137/110841217).
* Liu and Firoozi [2025]

  H. Liu, D. Firoozi,
  Hilbert space-valued LQ mean field games: An infinite-dimensional analysis,
  SIAM Journal on Control and Optimization 63 (2025) 3297–3327.
* Federico et al. [2024]

  S. Federico, F. Gozzi, D. Ghilli, Linear-Quadratic mean field games in Hilbert spaces, arXiv:2402.14935, 2024.
* Huang et al. [2007]

  M. Huang, P. E. Caines, R. P. Malhamé,
  Large-population cost-coupled LQG problems with nonuniform agents: individual-mass behavior and decentralized ε\varepsilon-Nash equilibria,
  IEEE transactions on automatic control 52 (2007) 1560–1571.
* Huang [2010]

  M. Huang,
  Large-population LQG games involving a major player: the Nash certainty equivalence principle,
  SIAM Journal on Control and Optimization 48 (2010) 3318–3353.
* Briceno-Arias et al. [2019]

  L. Briceno-Arias, D. Kalise, Z. Kobeissi, M. Lauriere, A. M. González, F. J. Silva,
  On the implementation of a primal-dual algorithm for second order time-dependent mean field games with local couplings,
  ESAIM: Proceedings and Surveys 65 (2019) 330–348.
* Angiuli et al. [2019]

  A. Angiuli, C. V. Graves, H. Li, J.-F. Chassagneux, F. Delarue, R. Carmona,
  Cemracs 2017: numerical probabilistic approach to mfg,
  ESAIM: Proceedings and Surveys 65 (2019) 84–113.
* Camilli and Tang [2023]

  F. Camilli, Q. Tang,
  A convergence rate for the newton’s method for mean field games with non-separable hamiltonians,
  arXiv preprint arXiv:2311.05416 (2023).
* Fouque and Zhang [2020]

  J.-P. Fouque, Z. Zhang,
  Deep learning methods for mean field control problems with delay,
  Frontiers in Applied Mathematics and Statistics 6 (2020) 11.
* Carmona and Laurière [2021]

  R. Carmona, M. Laurière,
  Convergence analysis of machine learning algorithms for the numerical solution of mean field control and games i: The ergodic case,
  SIAM Journal on Numerical Analysis 59 (2021) 1455–1485.
* Germain et al. [2022]

  M. Germain, J. Mikael, X. Warin,
  Numerical resolution of mckean-vlasov fbsdes using neural networks,
  Methodology and Computing in Applied Probability 24 (2022) 2557–2586.
* Cao et al. [2024]

  H. Cao, X. Guo, M. Laurière,
  Connecting gans, mean-field games, and optimal transport,
  SIAM Journal on Applied Mathematics 84 (2024) 1255–1287.
* Soner et al. [2025]

  H. M. Soner, J. Teichmann, Q. Yan,
  Learning algorithms for mean field optimal control,
  arXiv preprint arXiv:2503.17869 (2025).
* Lorentz et al. [1996]

  G. G. Lorentz, M. v. Golitschek, Y. Makovoz, Constructive approximation: advanced problems, volume 304 of Grundlehren der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], Springer-Verlag, Berlin, 1996. URL: <https://doi.org/10.1007/978-3-642-60932-9>. doi:[10.1007/978-3-642-60932-9](http://dx.doi.org/10.1007/978-3-642-60932-9), advanced problems.
* Cuchiero and Teichmann [2019]

  C. Cuchiero, J. Teichmann,
  Markovian lifts of positive semidefinite affine volterra-type processes,
  Decisions in Economics and Finance 42 (2019) 407–448.
* Cuchiero and Teichmann [2020]

  C. Cuchiero, J. Teichmann,
  Generalized feller processes and markovian lifts of stochastic volterra processes: the affine case,
  Journal of evolution equations 20 (2020) 1301–1348.
* Hamaguchi [2024]

  Y. Hamaguchi,
  Markovian lifting and asymptotic log-harnack inequality for stochastic volterra integral equations,
  Stochastic Processes and their Applications 178 (2024) 104482.
* Wang et al. [2021]

  S. Wang, H. Wang, P. Perdikaris,
  Learning the solution operator of parametric partial differential equations with physics-informed deeponets,
  Science advances 7 (2021) eabi8605.
* De Ryck and Mishra [2022]

  T. De Ryck, S. Mishra,
  Generic bounds on the approximation error for physics-informed (and) operator learning,
  Advances in Neural Information Processing Systems 35 (2022) 10945–10958.
* de Hoop et al. [2022]

  M. V. de Hoop, M. Lassas, C. A. Wong,
  Deep learning architectures for nonlinear operator functions and nonlinear inverse problems,
  Mathematical Statistics and Learning 4 (2022) 1–86.
* Goswami et al. [2023]

  S. Goswami, A. Bora, Y. Yu, G. E. Karniadakis,
  Physics-informed deep neural operator networks,
  in: Machine learning in modeling and simulation: methods and applications, Springer, 2023, pp. 219–254.
* Benitez et al. [2024]

  J. A. L. Benitez, T. Furuya, F. Faucher, A. Kratsios, X. Tricoche, M. V. de Hoop,
  Out-of-distributional risk bounds for neural operators with applications to the Helmholtz equation,
  Journal of Computational Physics (2024) 113168.
* Li et al. [2024]

  Z. Li, H. Zheng, N. Kovachki, D. Jin, H. Chen, B. Liu, K. Azizzadenesheli, A. Anandkumar,
  Physics-informed neural operator for learning partial differential equations,
  ACM/JMS Journal of Data Science 1 (2024) 1–27.
* Azizzadenesheli et al. [2024]

  K. Azizzadenesheli, N. Kovachki, Z. Li, M. Liu-Schiaffini, J. Kossaifi, A. Anandkumar,
  Neural operators for accelerating scientific simulations and design,
  Nature Reviews Physics 6 (2024) 320–328.
* Alvarez et al. [2024]

  G. Alvarez, I. Ekren, A. Kratsios, X. Yang,
  Neural operators can play dynamic stackelberg games,
  arXiv preprint arXiv:2411.09644 (2024).
* Huang and Lai [2025]

  H. Huang, R. Lai,
  Unsupervised solution operator learning for mean-field games,
  Journal of Computational Physics 537 (2025) 114057. URL: <https://www.sciencedirect.com/science/article/pii/S0021999125003407>. doi:[https://doi.org/10.1016/j.jcp.2025.114057](http://dx.doi.org/https://doi.org/10.1016/j.jcp.2025.114057).
* Chen et al. [2024]

  X. Chen, S. Liu, X. Di,
  Physics-informed graph neural operator for mean field games on graph: A scalable learning approach,
  Games 15 (2024) 12.
* Ichikawa [1979]

  A. Ichikawa,
  Dynamic programming approach to stochastic evolution equations,
  SIAM Journal on Control and Optimization 17 (1979) 152–174.
* Tessitore [1992]

  G. Tessitore,
  Some remarks on the Riccati equation arising in an optimal control problem with state-and control-dependent noise,
  SIAM Journal on Control and Optimization 30 (1992) 717–744.
* Dunyak and Caines [2024]

  A. Dunyak, P. E. Caines,
  Quadratic optimal control of graphon q-noise linear systems,
  arXiv preprint arXiv:2407.00212 (2024).
* Hong and Kratsios [2024]

  R. Hong, A. Kratsios,
  Bridging the gap between approximation and learning via optimal approximation by relu MLPs of maximal regularity,
  arXiv preprint arXiv:2409.12335 (2024).
* Goldstein [2017]

  J. A. Goldstein, Semigroups of linear operators and applications, second ed., Dover Publications, Inc., Mineola, NY, 2017.
* Benyamini and Lindenstrauss [2000]

  Y. Benyamini, J. Lindenstrauss, Geometric nonlinear functional analysis. Vol. 1, volume 48 of American Mathematical Society Colloquium Publications, American Mathematical Society, Providence, RI, 2000. URL: <https://doi.org/10.1090/coll/048>. doi:[10.1090/coll/048](http://dx.doi.org/10.1090/coll/048).
* Galimberti et al. [2022]

  L. Galimberti, A. Kratsios, G. Livieri,
  Designing universal causal deep learning models: The case of infinite-dimensional dynamical systems from stochastic analysis,
  arXiv preprint arXiv:2210.13300 (2022).
* Lanthaler [2023]

  S. Lanthaler,
  Operator learning with pca-net: upper and lower complexity bounds,
  Journal of Machine Learning Research 24 (2023) 1–67.
* Riegler et al. [2024]

  E. Riegler, A. Bühler, Y. Pan, H. Bölcskei,
  Generating rectifiable measures through neural networks,
  arXiv preprint arXiv:2412.05109 (2024).
* Murari et al. [2025]

  D. Murari, T. Furuya, C.-B. Schönlieb,
  Approximation theory for 1-lipschitz resnets,
  arXiv preprint arXiv:2505.12003 (2025).
* Amit et al. [2022]

  R. Amit, B. Epstein, S. Moran, R. Meir,
  Integral probability metrics pac-bayes bounds,
  Advances in Neural Information Processing Systems 35 (2022) 3123–3136.
* Hou et al. [2023]

  S. Hou, P. Kassraie, A. Kratsios, A. Krause, J. Rothfuss,
  Instance-dependent generalization bounds via optimal transport,
  Journal of Machine Learning Research 24 (2023) 1–51.
* Kratsios et al. [2024]

  A. Kratsios, A. M. Neuman, G. Pammer,
  Tighter generalization bounds on digital computers via discrete optimal transport,
  arXiv preprint arXiv:2402.05576 (2024).
* Detering et al. [2025]

  N. Detering, L. Galimberti, A. Kratsios, G. Livieri, A. M. Neuman,
  Learning from one graph: Transductive learning guarantees via the geometry of small random worlds,
  arXiv preprint arXiv:2509.06894 (2025). URL: <https://arxiv.org/abs/2509.06894>.
* Lei [2020]

  J. Lei,
  Convergence and concentration of empirical measures under Wasserstein distance in unbounded functional spaces,
  Bernoulli 26 (2020) 767–798. URL: <https://doi.org/10.3150/19-BEJ1151>. doi:[10.3150/19-BEJ1151](http://dx.doi.org/10.3150/19-BEJ1151).
* Shen et al. [2022]

  Z. Shen, H. Yang, S. Zhang,
  Optimal approximation rate of relu networks in terms of width and depth,
  Journal de Mathématiques Pures et Appliquées 157 (2022) 101–135.
* Shi et al. [2023]

  X. Shi, D. Xu, Z. Zhang,
  Deep learning algorithms for hedging with frictions,
  Digital Finance 5 (2023) 113–147. URL: <https://doi.org/10.1007/s42521-023-00075-z>. doi:[10.1007/s42521-023-00075-z](http://dx.doi.org/10.1007/s42521-023-00075-z).
* Ryan [2002]

  R. A. Ryan, Introduction to tensor products of Banach spaces, Springer Monographs in Mathematics, Springer-Verlag London, Ltd., London, 2002. URL: <https://doi.org/10.1007/978-1-4471-3903-4>. doi:[10.1007/978-1-4471-3903-4](http://dx.doi.org/10.1007/978-1-4471-3903-4).
* Kadison and Ringrose [1997]

  R. V. Kadison, J. R. Ringrose, Fundamentals of the theory of operator algebras. Vol. I, volume 15 of Graduate Studies in Mathematics, American Mathematical Society, Providence, RI, 1997. URL: <https://doi.org/10.1090/gsm/015>. doi:[10.1090/gsm/015](http://dx.doi.org/10.1090/gsm/015), elementary theory, Reprint of the 1983 original.

## Appendix A Additional Background

This appendix contains additional background supporting a self-contained reading of our manuscript.

### A.1 Mean Field Game Equilibrium Strategy

By [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Theorem 4.1], the mappings given by ([2.4](https://arxiv.org/html/2510.20017v1#S2.E4 "Equation 2.4 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.5](https://arxiv.org/html/2510.20017v1#S2.E5 "Equation 2.5 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) satisfy the following bounds:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Γ1∈ℒ​(ℒ​(H);H)\displaystyle\Gamma\_{1}\in\mathcal{L}(\mathcal{L}(H);H)\quad | and‖Γ1‖≤R1withR1=tr⁡(Q)​‖D‖,\displaystyle\mbox{and}\quad\|\Gamma\_{1}\|\leq R\_{1}\quad\mbox{with}\quad R\_{1}=\operatorname{tr}(Q)\|D\|, |  | (A.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Γ2∈ℒ​(ℒ​(H);U)\displaystyle\Gamma\_{2}\in\mathcal{L}(\mathcal{L}(H);U)\quad | and‖Γ2‖≤R2withR2=tr⁡(Q)​‖E‖,\displaystyle\mbox{and}\quad\|\Gamma\_{2}\|\leq R\_{2}\quad\mbox{with}\quad R\_{2}=\operatorname{tr}(Q)\|E\|, |  | (A.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ1∈ℒ​(ℒ​(H);ℒ​(H;U))\displaystyle\Delta\_{1}\in\mathcal{L}(\mathcal{L}(H);\mathcal{L}(H;U))\quad | and‖Δ1‖≤R3withR3=tr⁡(Q)​‖D‖​‖E‖,\displaystyle\mbox{and}\quad\|\Delta\_{1}\|\leq R\_{3}\quad\mbox{with}\quad R\_{3}=\operatorname{tr}(Q)\|D\|\|E\|, |  | (A.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ2∈ℒ​(ℒ​(H);ℒ​(H))\displaystyle\Delta\_{2}\in\mathcal{L}(\mathcal{L}(H);\mathcal{L}(H))\quad | and‖Δ2‖≤R4withR4=tr⁡(Q)​‖D‖2,\displaystyle\mbox{and}\quad\|\Delta\_{2}\|\leq R\_{4}\quad\mbox{with}\quad R\_{4}=\operatorname{tr}(Q)\|D\|^{2}, |  | (A.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ3∈ℒ​(ℒ​(H);ℒ​(U))\displaystyle\Delta\_{3}\in\mathcal{L}(\mathcal{L}(H);\mathcal{L}(U))\quad | and‖Δ3‖≤R5withR5=tr⁡(Q)​‖E‖2.\displaystyle\mbox{and}\quad\|\Delta\_{3}\|\leq R\_{5}\quad\mbox{with}\quad R\_{5}=\operatorname{tr}(Q)\|E\|^{2}. |  | (A.5) |

Below, we present the equilibrium strategy associated with the set of operators (A,B,D,E,F1,F2,σ,M,F^1,F^2,G)(A,B,D,E,F\_{1},F\_{2},\sigma,\\
M,\widehat{F}\_{1},\widehat{F}\_{2},G) for the MFG system ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")). The strategy corresponding to variations in these operators–for instance, in the reference model (A†,B†,D,E,F1,F2†,σ,M,F^1,F^2,G)(A^{\dagger},B^{\dagger},D,E,F\_{1},F\_{2}^{\dagger},\sigma,M,\widehat{F}\_{1},\widehat{F}\_{2},G) or in perturbed cases–can be obtained by direct substitution into the relevant equations.

###### Theorem A.1 (MFG Equilibrium Strategy).

[Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Theorem 4.9]. Consider the Hilbert space-valued limiting system with the set of operators (AA, BB, DD, EE, F1F\_{1}, F2F\_{2}, σ\sigma, MM, F^1\widehat{F}\_{1}, F^2\widehat{F}\_{2}, GG) described by ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
Suppose the relevant Riesz mappings Δk,k=1,2,3,\Delta\_{k},k=1,2,3, Γk,k=1,2,\Gamma\_{k},k=1,2, given by ([2.4](https://arxiv.org/html/2510.20017v1#S2.E4 "Equation 2.4 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.5](https://arxiv.org/html/2510.20017v1#S2.E5 "Equation 2.5 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), respectively.
Suppose Assumptions [2.1](https://arxiv.org/html/2510.20017v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")-[2.2](https://arxiv.org/html/2510.20017v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") and the following contraction condition hold:

|  |  |  |
| --- | --- | --- |
|  | C4​exp⁡(T​MTA​‖B‖​C1​(‖B‖+R3))<1,C\_{4}\exp\big(TM^{A}\_{T}\|B\|C\_{1}(\|B\|+R\_{3})\big)<1, |  |

where

|  |  |  |
| --- | --- | --- |
|  | C4=T​MTA​[MTA​‖B‖2​(T​C2+‖G‖​‖F^2‖)​exp⁡(MTA​T​C3)+C1​R2​‖B‖​‖F2‖+‖F1‖],\displaystyle C\_{4}=TM^{A}\_{T}\Big[M^{A}\_{T}\|B\|^{2}\big(TC\_{2}+\|G\|\big\|\widehat{F}\_{2}\big\|\big)\exp(M^{A}\_{T}TC\_{3})+C\_{1}R\_{2}\|B\|\|F\_{2}\|+\|F\_{1}\|\Big], |  |
|  |  |  |
| --- | --- | --- |
|  | C2=C1​(R1​‖F2‖+C1​R6​R2​‖F2‖+‖F1‖)+‖M‖​‖F^1‖,\displaystyle C\_{2}=C\_{1}\big(R\_{1}\|F\_{2}\|+C\_{1}R\_{6}R\_{2}\|F\_{2}\|+\|F\_{1}\|\big)+\|M\|\big\|\widehat{F}\_{1}\big\|, |  |
|  |  |  |
| --- | --- | --- |
|  | C3=C1​R6​‖B‖,\displaystyle C\_{3}=C\_{1}R\_{6}\|B\|, |  |
|  |  |  |
| --- | --- | --- |
|  | C1=CΠ,\displaystyle C\_{1}=C^{\Pi}, |  |

with CΠC^{\Pi} defined in ([4.1](https://arxiv.org/html/2510.20017v1#S4.E1 "Equation 4.1 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
Then, the the MFG equilibrium strategy is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(t)=−K−1​(T−t)​[L​(T−t)​x​(t)+Γ2​((F2​x¯​(t)+σ)⋆​Π​(T−t))+B⋆​q​(T−t)],K​(t)=I+Δ3​(Π​(t)),L​(t)=B⋆​Π​(t)+Δ1​(Π​(t)),\displaystyle\begin{aligned} u(t)&=-K^{-1}(T-t)\big[L(T-t)x(t)+\Gamma\_{2}\big((F\_{2}\bar{x}(t)+\sigma)^{\star}\Pi(T-t)\big)+B^{\star}q(T-t)\big],\\ K(t)&=I+\Delta\_{3}(\Pi(t)),\quad L(t)=B^{\star}\Pi(t)+\Delta\_{1}(\Pi(t)),\end{aligned} |  | (A.6) |

where the mean field
x¯​(t)∈H\bar{x}(t)\in H, the operator Π​(t)∈ℒ​(H)\Pi(t)\in\mathcal{L}(H) and the offset term q​(t)∈Hq(t)\in H, are characterized by the unique fixed point of the following set of consistency equations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | dd​t​⟨Π​(t)​x,x⟩=2​⟨Π​(t)​x,A​x⟩−⟨L⋆​(t)​(K​(t))−1​L​(t)​x,x⟩+⟨Δ2​(Π​(t))​x,x⟩+⟨M​x,x⟩,x∈𝒟​(A),\displaystyle\frac{d}{dt}\langle\Pi(t)x,x\rangle=2\langle\Pi(t)x,Ax\rangle-\langle L^{\star}(t)(K(t))^{-1}L(t)x,x\rangle+\langle\Delta\_{2}(\Pi(t))x,x\rangle+\langle Mx,x\rangle,\,\,\,x\in\mathcal{D}(A), |  | (A.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | q˙​(t)=(A⋆−L⋆​(t)​(K​(t))−1​B⋆)​q​(t)+Γ1​((F2​x¯​(T−t)+σ)⋆​Π​(t))\displaystyle\dot{q}(t)=\big(A^{\star}-L^{\star}(t)(K(t))^{-1}B^{\star}\big)q(t)+\Gamma\_{1}\Big(\big(F\_{2}\bar{x}(T-t)+\sigma\big)^{\star}\Pi(t)\Big) |  | (A.8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −L⋆​(t)​K−1​(t)​Γ2​((F2​x¯​(T−t)+σ)⋆​Π​(t))+(Π​(t)​F1−M​F^1)​x¯​(T−t),\displaystyle\hskip 85.35826pt-L^{\star}(t)K^{-1}(t)\Gamma\_{2}\left(\big(F\_{2}\bar{x}(T-t)+\sigma\big)^{\star}\Pi(t)\right)+\big(\Pi(t)F\_{1}-M\hat{F}\_{1}\big)\bar{x}(T-t), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | x¯(t)=S(t)ξ¯−∫0tS(t−r)[B(K(T−r))−1(L(T−r)x¯(r)+B⋆q(T−r)\displaystyle\bar{x}(t)=S(t)\bar{\xi}-\int\_{0}^{t}S(t-r)\Big[B(K(T-r))^{-1}\big(L(T-r)\bar{x}(r)+B^{\star}q(T-r) |  | (A.9) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Γ2((F2x¯(r)+σ)⋆Π(T−r)))−F1x¯(r)]dr,\displaystyle\hskip 85.35826pt+\Gamma\_{2}\big((F\_{2}\bar{x}(r)+\sigma)^{\star}\Pi(T-r)\big)\big)-F\_{1}\bar{x}(r)\Big]dr, |  |

with Π​(0)=G\Pi(0)=G, q​(0)=−G​F2​x¯​(T)q(0)=-GF\_{2}\bar{x}(T).

The equilibrium state of the MFG system ([2.1](https://arxiv.org/html/2510.20017v1#S2.E1 "Equation 2.1 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))-([2.3](https://arxiv.org/html/2510.20017v1#S2.E3 "Equation 2.3 ‣ 2.1 Infinite-Dimensional LQ MFGs ‣ 2 Preliminaries ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) under the strategy ([A.6](https://arxiv.org/html/2510.20017v1#A1.E6 "Equation A.6 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(t)=S​(t)​ξ−∫0tS​(t−r)​[B​(K​(T−r))−1​L​(T−r)​x​(t)+B​τ​(r)−F1​x¯​(r)]​𝑑r+∫0tS​(t−r)​[(D−E​(K​(T−r))−1​L​(T−r))​x​(r)−E​τ​(r)+F2​x¯​(r)+σ]​𝑑W​(r),\displaystyle\begin{aligned} x(t)=&S(t)\xi-\int\_{0}^{t}S(t-r)\big[B(K(T-r))^{-1}L(T-r)x(t)+B\tau(r)-F\_{1}\bar{x}(r)\big]dr\\ &+\int\_{0}^{t}S(t-r)\Big[\big(D-E(K(T-r))^{-1}L(T-r)\big)x(r)-E\tau(r)+F\_{2}\bar{x}(r)+\sigma\Big]dW(r),\end{aligned} |  | (A.10) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ​(t)=(K​(T−r))−1​[B⋆​q​(T−t)+Γ2​((F2​x¯​(t)+σ)⋆​Π​(T−t))].\displaystyle\tau(t)=(K(T-r))^{-1}\big[B^{\star}q(T-t)+\Gamma\_{2}\big((F\_{2}\bar{x}(t)+\sigma)^{\star}\Pi(T-t)\big)\big]. |  | (A.11) |

### A.2 Estimates for continuous mappings

###### Lemma A.2.

Suppose f∈C​(𝒯;H)f\in C(\mathcal{T};H) and g∈C​(𝒯;H)g\in C(\mathcal{T};H) satisfy the following system of inequalities on 𝒯\mathcal{T}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f​(t)‖≤∫0t(af​‖f​(r)‖+bf​‖g​(T−r)‖+cf)​𝑑r+df,\displaystyle\|f(t)\|\leq\int\_{0}^{t}\big(a\_{f}\|f(r)\|+b\_{f}\|g(T-r)\|+c\_{f}\big)dr+d\_{f}, |  | (A.12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖g​(t)‖≤dg,f​‖f​(T)‖+dg+∫0t(ag​‖g​(r)‖+bg​‖f​(T−r)‖+cg)​𝑑r,\displaystyle\|g(t)\|\leq d\_{g,f}\|f(T)\|+d\_{g}+\int\_{0}^{t}\big(a\_{g}\|g(r)\|+b\_{g}\|f(T-r)\|+c\_{g}\big)dr, |  | (A.13) |

where (af,bf,cf,df)(a\_{f},b\_{f},c\_{f},d\_{f}) and (ag,bg,cg,dg,dg,f)(a\_{g},b\_{g},c\_{g},d\_{g},d\_{g,f}) are positive constants and satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | (bg​T+dg,f)​bf​T​exp⁡((af+ag)​T)<1.\displaystyle(b\_{g}T+d\_{g,f})b\_{f}T\exp((a\_{f}+a\_{g})T)<1. |  | (A.14) |

Then ff and gg have the estimates

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖f‖C​(𝒯;H)≤\displaystyle\|f\|\_{C(\mathcal{T};H)}\leq | [1−(bg​T+dg,f)​bf​T​exp⁡((af+ag)​T)]−1\displaystyle\big[1-(b\_{g}T+d\_{g,f})b\_{f}T\exp((a\_{f}+a\_{g})T)\big]^{-1} |  | (A.15) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[(cf​T+df)​exp⁡(af​T)+bf​T​(cg​T+dg)​exp⁡((af+ag)​T)],\displaystyle\times\big[(c\_{f}T+d\_{f})\exp(a\_{f}T)+b\_{f}T\big(c\_{g}T+d\_{g}\big)\exp\big((a\_{f}+a\_{g})T\big)\big], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖g‖C​(𝒯;H)≤\displaystyle\|g\|\_{C(\mathcal{T};H)}\leq | (cg​T+dg)​exp⁡(ag​T)\displaystyle(c\_{g}T+d\_{g})\exp(a\_{g}T) |  | (A.16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(bg​T+dg,f)​exp⁡(ag​T)​[1−(bg​T+dg,f)​bf​T​exp⁡((af+ag)​T)]−1\displaystyle+(b\_{g}T+d\_{g,f})\exp(a\_{g}T)\big[1-(b\_{g}T+d\_{g,f})b\_{f}T\exp((a\_{f}+a\_{g})T)\big]^{-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[(cf​T+df)​exp⁡(af​T)+bf​T​(cg​T+dg)​exp⁡((af+ag)​T)].\displaystyle\times\big[(c\_{f}T+d\_{f})\exp(a\_{f}T)+b\_{f}T\big(c\_{g}T+d\_{g}\big)\exp\big((a\_{f}+a\_{g})T\big)\big]. |  |

###### Proof.

From ([A.12](https://arxiv.org/html/2510.20017v1#A1.E12 "Equation A.12 ‣ Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.13](https://arxiv.org/html/2510.20017v1#A1.E13 "Equation A.13 ‣ Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f​(t)‖≤∫0taf​‖f​(r)‖​𝑑r+bf​t​‖g‖C​(𝒯;H)+cf​t+df,\displaystyle\|f(t)\|\leq\int\_{0}^{t}a\_{f}\|f(r)\|dr+b\_{f}t\|g\|\_{C(\mathcal{T};H)}+c\_{f}t+d\_{f}, |  | (A.17) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖g​(t)‖≤∫0tag​‖g​(r)‖​𝑑r+(bg​t+dg,f)​‖f‖C​(𝒯;H)+cg​t+dg.\displaystyle\|g(t)\|\leq\int\_{0}^{t}a\_{g}\|g(r)\|dr+(b\_{g}t+d\_{g,f})\|f\|\_{C(\mathcal{T};H)}+c\_{g}t+d\_{g}. |  | (A.18) |

With the Grönwall’s inequality applied to ([A.17](https://arxiv.org/html/2510.20017v1#A1.E17 "Equation A.17 ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.18](https://arxiv.org/html/2510.20017v1#A1.E18 "Equation A.18 ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f‖C​(𝒯;H)≤(bf​T​‖g‖C​(𝒯;H)+cf​T+df)​exp⁡(af​T),\displaystyle\|f\|\_{C(\mathcal{T};H)}\leq\big(b\_{f}T\|g\|\_{C(\mathcal{T};H)}+c\_{f}T+d\_{f}\big)\exp(a\_{f}T), |  | (A.19) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖g‖C​(𝒯;H)≤[(bg​T+dg,f)​‖f‖C​(𝒯;H)+cg​T+dg]​exp⁡(ag​T).\displaystyle\|g\|\_{C(\mathcal{T};H)}\leq\big[(b\_{g}T+d\_{g,f})\|f\|\_{C(\mathcal{T};H)}+c\_{g}T+d\_{g}\big]\exp(a\_{g}T). |  | (A.20) |

Substituting ([A.20](https://arxiv.org/html/2510.20017v1#A1.E20 "Equation A.20 ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) into ([A.19](https://arxiv.org/html/2510.20017v1#A1.E19 "Equation A.19 ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f‖C​(𝒯;H)≤\displaystyle\|f\|\_{C(\mathcal{T};H)}\leq | (cf​T+df)​exp⁡(af​T)+bf​T​[(bg​T+dg,f)​‖f‖C​(𝒯;H)+cg​T+dg]​exp⁡(ag​T)​exp⁡(af​T)\displaystyle(c\_{f}T+d\_{f})\exp(a\_{f}T)+b\_{f}T\big[(b\_{g}T+d\_{g,f})\|f\|\_{C(\mathcal{T};H)}+c\_{g}T+d\_{g}\big]\exp(a\_{g}T)\exp(a\_{f}T) |  |

and furthermore

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ‖f‖C​(𝒯;H)​[1−(bg​T+dg,f)​bf​T​exp⁡((af+ag)​T)]\displaystyle\|f\|\_{C(\mathcal{T};H)}\big[1-(b\_{g}T+d\_{g,f})b\_{f}T\exp((a\_{f}+a\_{g})T)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (cf​T+df)​exp⁡(af​T)+bf​T​(cg​T+dg)​exp⁡((af+ag)​T).\displaystyle(c\_{f}T+d\_{f})\exp(a\_{f}T)+b\_{f}T\big(c\_{g}T+d\_{g}\big)\exp\big((a\_{f}+a\_{g})T\big). |  |

Since ([A.14](https://arxiv.org/html/2510.20017v1#A1.E14 "Equation A.14 ‣ Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) is satisfied, we immediately have the upper bound ([A.15](https://arxiv.org/html/2510.20017v1#A1.E15 "Equation A.15 ‣ Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) for ff.
Substituting ([A.15](https://arxiv.org/html/2510.20017v1#A1.E15 "Equation A.15 ‣ Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) into ([A.20](https://arxiv.org/html/2510.20017v1#A1.E20 "Equation A.20 ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we obtain the estimate ([A.16](https://arxiv.org/html/2510.20017v1#A1.E16 "Equation A.16 ‣ Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) for gg.
∎

### A.3 Proof of Regularity Results for the Reference MFG Model

#### A.3.1 Proof of Lemma [4.1](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem1 "Lemma 4.1. ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

Denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ†​(r)=\displaystyle\Phi^{\dagger}(r)= | B†​(K†)−1​(T−r)​[L†​(T−r)​x¯†​(r)+(B†)⋆​q†​(T−r)+Γ2​((F2†​x¯†​(r)+σ)⋆​Π†​(T−r))]\displaystyle B^{\dagger}(K^{\dagger})^{-1}(T-r)\big[L^{\dagger}(T-r)\bar{x}^{\dagger}(r)+(B^{\dagger})^{\star}q^{\dagger}(T-r)+\Gamma\_{2}\big((F\_{2}^{\dagger}\bar{x}^{\dagger}(r)+\sigma)^{\star}\Pi^{\dagger}(T-r)\big)\big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −F1​x¯†​(r),\displaystyle-F\_{1}\bar{x}^{\dagger}(r), |  | (A.21) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ†​(r)=\displaystyle\Psi^{\dagger}(r)= | −(L†)⋆​(r)​(K†)−1​(r)​(B†)⋆​q​(r)+Γ1​((F2†​x¯†​(T−r)+σ)⋆​Π†​(r))\displaystyle-(L^{\dagger})^{\star}(r)(K^{\dagger})^{-1}(r)(B^{\dagger})^{\star}q(r)+\Gamma\_{1}\big((F\_{2}^{\dagger}\bar{x}^{\dagger}(T-r)+\sigma)^{\star}\Pi^{\dagger}(r)\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(L†)⋆​(r)​(K†)−1​(r)​Γ2​((F2†​x¯†​(T−r)+σ)⋆​Π†​(r))+(Π†​(r)​F1−M​F^1)​x¯†​(T−r).\displaystyle\quad-(L^{\dagger})^{\star}(r)(K^{\dagger})^{-1}(r)\Gamma\_{2}\big((F\_{2}^{\dagger}\bar{x}^{\dagger}(T-r)+\sigma)^{\star}\Pi^{\dagger}(r)\big)+\big(\Pi^{\dagger}(r)F\_{1}-M\widehat{F}\_{1}\big)\bar{x}^{\dagger}(T-r). |  | (A.22) |

By ([A.8](https://arxiv.org/html/2510.20017v1#A1.E8 "Equation A.8 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.9](https://arxiv.org/html/2510.20017v1#A1.E9 "Equation A.9 ‣ Theorem A.1 (MFG Equilibrium Strategy). ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), the terms q†∈ℋq^{\dagger}\in\mathcal{H} and
the limiting mean field terms x¯†∈ℋ\bar{x}^{\dagger}\in\mathcal{H} have the following integral forms

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x¯†​(t)=\displaystyle\bar{x}^{\dagger}(t)= | S†​(t)​ξ¯−∫0tS†​(t−r)​Φ†​(r)​𝑑r,\displaystyle S^{\dagger}(t)\bar{\xi}-\int\_{0}^{t}S^{\dagger}(t-r)\Phi^{\dagger}(r)dr, |  | (A.23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q†​(t)=\displaystyle q^{\dagger}(t)= | −S†​(t)​G​F^2​x¯†​(T)+∫0tS†​(t−r)​Ψ†​(r)​𝑑r.\displaystyle-S^{\dagger}(t)G\widehat{F}\_{2}\bar{x}^{\dagger}(T)+\int\_{0}^{t}S^{\dagger}(t-r)\Psi^{\dagger}(r)dr. |  | (A.24) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Φ†​(r)‖≤CΦ,x¯†​‖x¯†​(r)‖+CΦ,q†​‖q†​(T−r)‖+CΦ,c,†,\displaystyle\big\|\Phi^{\dagger}(r)\big\|\leq C^{\Phi,\bar{x}^{\dagger}}\|\bar{x}^{\dagger}(r)\|+C^{\Phi,q^{\dagger}}\|q^{\dagger}(T-r)\|+C^{\Phi,c,\dagger}, |  | (A.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Ψ†​(r)‖≤CΨ,q†​‖q†​(r)‖+CΨ,x¯†​‖x¯†​(T−r)‖+CΨ,c,†,\displaystyle\big\|\Psi^{\dagger}(r)\big\|\leq C^{\Psi,q^{\dagger}}\|q^{\dagger}(r)\|+C^{\Psi,\bar{x}^{\dagger}}\|\bar{x}^{\dagger}(T-r)\|+C^{\Psi,c,\dagger}, |  | (A.26) |

where

|  |  |  |
| --- | --- | --- |
|  | CΦ,x¯†=‖B†‖​(‖B†‖+R3+R2​‖F2†‖)​CΠ†+‖F1‖,\displaystyle C^{\Phi,\bar{x}^{\dagger}}=\|B^{\dagger}\|(\|B^{\dagger}\|+R\_{3}+R\_{2}\|F\_{2}^{\dagger}\|)C^{\Pi^{\dagger}}+\|F\_{1}\|, |  |
|  |  |  |
| --- | --- | --- |
|  | CΦ,q†=‖B†‖2,CΦ,c,†=‖B†‖​R2​‖σ‖​CΠ†,\displaystyle C^{\Phi,q^{\dagger}}=\|B^{\dagger}\|^{2},\quad C^{\Phi,c,\dagger}=\|B^{\dagger}\|R\_{2}\|\sigma\|C^{\Pi^{\dagger}}, |  |
|  |  |  |
| --- | --- | --- |
|  | CΨ,q†=CΠ†​(‖B†‖+R3)​‖B†‖,\displaystyle C^{\Psi,q^{\dagger}}=C^{\Pi^{\dagger}}(\|B^{\dagger}\|+R\_{3})\big\|B^{\dagger}\big\|, |  |
|  |  |  |
| --- | --- | --- |
|  | CΨ,x¯†=[R1​CΠ†+(CΠ†)2​(‖B†‖+R3)​R2]​‖F2†‖+CΠ†​‖F1‖+‖M‖​‖F^1‖,\displaystyle C^{\Psi,\bar{x}^{\dagger}}=\big[R\_{1}C^{\Pi^{\dagger}}+(C^{\Pi^{\dagger}})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}\big]\big\|F\_{2}^{\dagger}\big\|+C^{\Pi^{\dagger}}\big\|F\_{1}\big\|+\big\|M\big\|\big\|\hat{F}\_{1}\big\|, |  |
|  |  |  |
| --- | --- | --- |
|  | CΨ,c,†=R1​CΠ†+(CΠ†)2​(‖B†‖+R3)​R2.\displaystyle C^{\Psi,c,\dagger}=R\_{1}C^{\Pi^{\dagger}}+(C^{\Pi^{\dagger}})^{2}(\|B^{\dagger}\|+R\_{3})R\_{2}. |  |

By ([A.23](https://arxiv.org/html/2510.20017v1#A1.E23 "Equation A.23 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), ([A.24](https://arxiv.org/html/2510.20017v1#A1.E24 "Equation A.24 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), ([A.25](https://arxiv.org/html/2510.20017v1#A1.E25 "Equation A.25 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.26](https://arxiv.org/html/2510.20017v1#A1.E26 "Equation A.26 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖x¯†​(t)‖≤\displaystyle\|\bar{x}^{\dagger}(t)\|\leq | ‖S†​(t)‖​‖ξ¯‖+∫0t‖S†​(t−r)‖​‖Φ†​(r)‖​𝑑r\displaystyle\|S^{\dagger}(t)\|\|\bar{\xi}\|+\int\_{0}^{t}\|S^{\dagger}(t-r)\|\big\|\Phi^{\dagger}(r)\big\|dr\allowdisplaybreaks |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | MTA†​‖ξ¯‖+MTA†​∫0t(CΦ,x¯†​‖x¯†​(r)‖+CΦ,q†​‖q†​(T−r)‖+CΦ,c,†)​𝑑r\displaystyle M^{A^{\dagger}}\_{T}\|\bar{\xi}\|+M^{A^{\dagger}}\_{T}\int\_{0}^{t}\big(C^{\Phi,\bar{x}^{\dagger}}\|\bar{x}^{\dagger}(r)\|+C^{\Phi,q^{\dagger}}\|q^{\dagger}(T-r)\|+C^{\Phi,c,\dagger}\big)dr |  | (A.27) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖q†​(t)‖≤\displaystyle\big\|q^{\dagger}(t)\big\|\leq | ‖S†​(t)‖​‖G‖​‖F^2‖​‖x¯†​(T)‖+∫0t‖S†​(t−r)‖​‖Ψ†​(r)‖​𝑑r\displaystyle\big\|S^{\dagger}(t)\big\|\|G\|\|\widehat{F}\_{2}\|\|\bar{x}^{\dagger}(T)\|+\int\_{0}^{t}\big\|S^{\dagger}(t-r)\big\|\big\|\Psi^{\dagger}(r)\big\|dr\allowdisplaybreaks |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | MTA†​‖G‖​‖F^2‖​‖x¯†​(T)‖+MTA†​∫0tCΨ,q†​‖q†​(r)‖+CΨ,x¯†​‖x¯†​(T−r)‖+CΨ,c,†​d​r.\displaystyle M^{A^{\dagger}}\_{T}\|G\|\|\widehat{F}\_{2}\|\|\bar{x}^{\dagger}(T)\|+M^{A^{\dagger}}\_{T}\int\_{0}^{t}C^{\Psi,q^{\dagger}}\|q^{\dagger}(r)\|+C^{\Psi,\bar{x}^{\dagger}}\|\bar{x}^{\dagger}(T-r)\|+C^{\Psi,c,\dagger}dr. |  | (A.28) |

Applying Lemma [A.2](https://arxiv.org/html/2510.20017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") to ([A.27](https://arxiv.org/html/2510.20017v1#A1.E27 "Equation A.27 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.28](https://arxiv.org/html/2510.20017v1#A1.E28 "Equation A.28 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have
([4.2](https://arxiv.org/html/2510.20017v1#S4.E2 "Equation 4.2 ‣ Lemma 4.1. ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([4.3](https://arxiv.org/html/2510.20017v1#S4.E3 "Equation 4.3 ‣ Lemma 4.1. ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
∎

#### A.3.2 Proof of Lemma [4.2](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

By ([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​‖x†​(t)‖2\displaystyle\mathbb{E}\|x^{\dagger}(t)\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 3∥S†(t)∥2𝔼∥ξ∥2+3𝔼∥∫0tS†(t−r)[B†(K†)−1(T−r)L†(T−r)x†(r)\displaystyle 3\|S^{\dagger}(t)\|^{2}\mathbb{E}\|\xi\|^{2}+3\mathbb{E}\Big\|\int\_{0}^{t}S^{\dagger}(t-r)\big[B^{\dagger}(K^{\dagger})^{-1}(T-r)L^{\dagger}(T-r)x^{\dagger}(r)\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +B†τ†(r)−F1x¯†(r)]dr∥2\displaystyle\hskip 199.16928pt+B^{\dagger}\tau^{\dagger}(r)-F\_{1}\bar{x}^{\dagger}(r)\big]dr\Big\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​𝔼​‖∫0tS†​(t−r)​[(D−E​(K†)−1​(T−r)​L†​(T−r))​x†​(r)−E​τ†​(r)+F2†​x¯†​(r)+σ]​𝑑W​(r)‖2\displaystyle+3\mathbb{E}\Big\|\int\_{0}^{t}S^{\dagger}(t-r)\big[\big(D-E(K^{\dagger})^{-1}(T-r)L^{\dagger}(T-r)\big)x^{\dagger}(r)-E\tau^{\dagger}(r)+F\_{2}^{\dagger}\bar{x}^{\dagger}(r)+\sigma\big]dW(r)\Big\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 3​(MTA†)2​𝔼​‖ξ‖2+3​∫0t(MTA†)2​[‖B†‖2​‖L†​(T−r)‖2​𝔼​‖x†​(t)‖2+‖B†‖2​‖τ†​(r)‖2+‖F1‖2​‖x¯†​(r)‖2]​𝑑r\displaystyle 3(M^{A^{\dagger}}\_{T})^{2}\mathbb{E}\|\xi\|^{2}+3\int\_{0}^{t}(M^{A^{\dagger}}\_{T})^{2}\big[\|B^{\dagger}\|^{2}\|L^{\dagger}(T-r)\|^{2}\mathbb{E}\|x^{\dagger}(t)\|^{2}+\|B^{\dagger}\|^{2}\|\tau^{\dagger}(r)\|^{2}+\|F\_{1}\|^{2}\|\bar{x}^{\dagger}(r)\|^{2}\big]dr\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​∫0t(MTA†)2​[(‖D‖2+‖E‖2​‖L†​(T−r)‖2)​𝔼​‖x†​(r)‖2+‖E‖2​‖τ†​(r)‖2+‖F2†‖2​‖x¯†‖2+‖σ‖2]​𝑑r.\displaystyle+3\int\_{0}^{t}(M^{A^{\dagger}}\_{T})^{2}\big[\big(\|D\|^{2}+\|E\|^{2}\|L^{\dagger}(T-r)\|^{2}\big)\mathbb{E}\|x^{\dagger}(r)\|^{2}+\|E\|^{2}\|\tau^{\dagger}(r)\|^{2}+\|F\_{2}^{\dagger}\|^{2}\|\bar{x}^{\dagger}\|^{2}+\|\sigma\|^{2}\big]dr. |  |

By ([A.11](https://arxiv.org/html/2510.20017v1#A1.E11 "Equation A.11 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖τ​(t)‖≤\displaystyle\|\tau(t)\|\leq | ‖K−1​(T−t)‖​[‖B‖​|q​(T−t)|+‖Γ2‖​((‖F2†‖​|x¯†​(t)|+‖σ‖)​‖Π†​(T−t)‖)]\displaystyle\|K^{-1}(T-t)\|\big[\|B\||q(T-t)|+\|\Gamma\_{2}\|\big((\|F\_{2}^{\dagger}\||\bar{x}^{\dagger}(t)|+\|\sigma\|)\|\Pi^{\dagger}(T-t)\|\big)\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖B†‖​Cq†+R2​(‖F2†‖​Cx¯†+‖σ‖)​CΠ†.\displaystyle\|B^{\dagger}\|C^{q^{\dagger}}+R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}. |  |

By the Grönwall’s inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖x†​(t)‖2≤\displaystyle\mathbb{E}\|x^{\dagger}(t)\|^{2}\leq | {3(MTA†)2𝔼∥ξ∥2+3T(MTA†)2[(∥B†∥2+∥E∥2)(∥B†∥Cq†+R2(∥F2†∥Cx¯†+∥σ∥)CΠ†)]\displaystyle\big\{3(M^{A^{\dagger}}\_{T})^{2}\mathbb{E}\|\xi\|^{2}+3T(M\_{T}^{A^{\dagger}})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big(\|B^{\dagger}\|C^{q^{\dagger}}+R\_{2}(\|F\_{2}^{\dagger}\|C^{\bar{x}^{\dagger}}+\|\sigma\|)C^{\Pi^{\dagger}}\big)\big]\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3T(MTA†)2(∥F1∥2+∥F2†∥2)(Cx¯†)2+3T(MTA†)2∥σ∥2}⋅\displaystyle\hskip 142.26378pt+3T(M^{A^{\dagger}}\_{T})^{2}(\|F\_{1}\|^{2}+\|F\_{2}^{\dagger}\|^{2})(C^{\bar{x}^{\dagger}})^{2}+3T(M^{A^{\dagger}}\_{T})^{2}\|\sigma\|^{2}\big\}\cdot\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | exp⁡{3​(MTA†)2​[(‖B†‖2+‖E‖2)​((‖B†‖+R3)​CΠ†)2+‖D‖2]​T}.\displaystyle\exp\big\{3(M^{A^{\dagger}}\_{T})^{2}\big[(\|B^{\dagger}\|^{2}+\|E\|^{2})\big((\|B^{\dagger}\|+R\_{3})C^{\Pi^{\dagger}}\big)^{2}+\|D\|^{2}\big]T\big\}. |  |

The desired estimate then follows.
∎

### A.4 Proofs of Lipschitz Stability with respect to AA

#### A.4.1 Proof of Lemma [4.3](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.1 Stability of the equilibrium with respect to operator 𝐴 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

Denote K=A−A†K=A-A^{\dagger}. According to Goldstein [[2017](https://arxiv.org/html/2510.20017v1#bib.bib44)], we have

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | dd​t​SA​(t)\displaystyle\frac{d}{dt}S^{A}(t) | =A​SA​(t)=(K+A†)​SA​(t),\displaystyle=AS^{A}(t)=(K+A^{\dagger})S^{A}(t), | SA​(0)\displaystyle S^{A}(0) | =I,\displaystyle=I, |  | (A.29) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | dd​t​SA†​(t)\displaystyle\frac{d}{dt}S^{A^{\dagger}}(t) | =A†​SA†​(t),\displaystyle=A^{\dagger}S^{A^{\dagger}}(t), | SA†​(0)\displaystyle S^{A^{\dagger}}(0) | =I.\displaystyle=I. |  | (A.30) |

Then, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​(SA​(t)−SA†​(t))=A†​(SA​(t)+SA†​(t))−K​SA​(t),\frac{d}{dt}(S^{A}(t)-S^{A^{\dagger}}(t))=A^{\dagger}(S^{A}(t)+S^{A^{\dagger}}(t))-KS^{A}(t), |  | (A.31) |

which results in

|  |  |  |  |
| --- | --- | --- | --- |
|  | SA†​(t)−SA​(t)=∫0tSA†​(t−s)​K​SA​(s)​𝑑s.S^{A^{\dagger}}(t)-S^{A}(t)=\int\_{0}^{t}S^{A^{\dagger}}(t-s)KS^{A}(s)ds. |  | (A.32) |

From the above equation, we conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖SA†​(t)−SA​(t)‖≤T​MTA†​MTA​‖A−A†‖.\|S^{A^{\dagger}}(t)-S^{A}(t)\|\leq TM^{A^{\dagger}}\_{T}M^{A}\_{T}\|A-A^{\dagger}\|. |  | (A.33) |

∎

#### A.4.2 Proof of Lemma [4.4](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.1 Stability of the equilibrium with respect to operator 𝐴 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

The proof is based on [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3].
We introduce the processes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | d​yA​(t)=(A​yA​(t)+B†​u​(t))​d​t+(D​yA​(t)+E​u​(t))​d​W​(t),yA​(0)=ξ,\displaystyle dy^{A}(t)=(Ay^{A}(t)+B^{\dagger}u(t))dt+(Dy^{A}(t)+Eu(t))dW(t),\quad y^{A}(0)=\xi, |  | (A.34) |
|  |  | d​y†​(t)=(A†​y†​(t)+B†​u​(t))​d​t+(D​y†​(t)+E​u​(t))​d​W​(t),y†​(0)=ξ,\displaystyle dy^{\dagger}(t)=(A^{\dagger}y^{\dagger}(t)+B^{\dagger}u(t))dt+(Dy^{\dagger}(t)+Eu(t))dW(t),\quad y^{\dagger}(0)=\xi, |  |

and cost functionals

|  |  |  |
| --- | --- | --- |
|  | 𝔼​∫0T(‖M1/2​yA​(t)‖2+‖u​(t)‖2)​𝑑t+𝔼​‖G1/2​yA​(T)‖2,\displaystyle\mathbb{E}\int\_{0}^{T}\big(\big\|M^{1/2}y^{A}(t)\big\|^{2}+\|u(t)\|^{2}\big)dt+\mathbb{E}\big\|G^{1/2}y^{A}(T)\big\|^{2}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​∫0T(‖M1/2​y†​(t)‖2+‖u​(t)‖2)​𝑑t+𝔼​‖G1/2​y†​(T)‖2.\displaystyle\mathbb{E}\int\_{0}^{T}\big(\big\|M^{1/2}y^{\dagger}(t)\big\|^{2}+\|u(t)\|^{2}\big)dt+\mathbb{E}\big\|G^{1/2}y^{\dagger}(T)\big\|^{2}. |  |

Let S†∈ℒ​(H)S^{\dagger}\in\mathcal{L}(H) and SA∈ℒ​(H)S^{A}\in\mathcal{L}(H) be the semigroup corresponding to the infinite generator A†A^{\dagger} and AA, respectively. The mild solutions of ([A.34](https://arxiv.org/html/2510.20017v1#A1.E34 "Equation A.34 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | yA​(t)=\displaystyle y^{A}(t)= | SA​(t)​ξ+∫0tSA​(t−r)​B†​u​(r)​𝑑r+∫0tSA​(t−r)​(D​yA​(r)+E​u​(r))​𝑑W​(r),\displaystyle S^{A}(t)\xi+\int\_{0}^{t}S^{A}(t-r)B^{\dagger}u(r)dr+\int\_{0}^{t}S^{A}(t-r)(Dy^{A}(r)+Eu(r))dW(r), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y†​(t)=\displaystyle y^{\dagger}(t)= | S†​(t)​ξ+∫0tS†​(t−r)​B†​u​(r)​𝑑r+∫0tS†​(t−r)​(D​y†​(r)+E​u​(r))​𝑑W​(r),\displaystyle S^{\dagger}(t)\xi+\int\_{0}^{t}S^{\dagger}(t-r)B^{\dagger}u(r)dr+\int\_{0}^{t}S^{\dagger}(t-r)(Dy^{\dagger}(r)+Eu(r))dW(r), |  |

and satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | yA​(t)−y†​(t)=\displaystyle y^{A}(t)-y^{\dagger}(t)= | (SA−S†)​(t)​ξ+∫0t(SA−S†)​(t−r)​B†​u​(r)​𝑑r\displaystyle(S^{A}-S^{\dagger})(t)\xi+\int\_{0}^{t}(S^{A}-S^{\dagger})(t-r)B^{\dagger}u(r)dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t[(SA−S†)​(t−r)​(D​yA​(r)+E​u​(r))+S†​(t−r)​D​(yA​(r)−y†​(r))]​𝑑W​(r).\displaystyle+\int\_{0}^{t}\big[(S^{A}-S^{\dagger})(t-r)(Dy^{A}(r)+Eu(r))+S^{\dagger}(t-r)D(y^{A}(r)-y^{\dagger}(r))\big]dW(r). |  |

By the Itô’s formula and Cauchy-Schwarz inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(‖(yA−y†)​(t)‖2)=\displaystyle\mathbb{E}\big(\|(y^{A}-y^{\dagger})(t)\|^{2}\big)= | 𝔼​∫0t2​⟨(yA−y†)​(r),(SA−S†)​(t−r)​B†​u​(r)⟩​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}2\langle(y^{A}-y^{\dagger})(r),(S^{A}-S^{\dagger})(t-r)B^{\dagger}u(r)\rangle dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​∫0t‖(SA−S†)​(t−r)​(D​yA​(r)+E​u​(r))+S†​(t−r)​D​(yA−y†)​(r)‖2​𝑑r\displaystyle+\mathbb{E}\int\_{0}^{t}\big\|(S^{A}-S^{\dagger})(t-r)(Dy^{A}(r)+Eu(r))+S^{\dagger}(t-r)D(y^{A}-y^{\dagger})(r)\big\|^{2}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​∫0t2​‖(yA−y†)​(r)‖​‖(SA−S†)​(t−r)‖​‖B†‖​‖u​(r)‖​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}2\big\|(y^{A}-y^{\dagger})(r)\big\|\big\|(S^{A}-S^{\dagger})(t-r)\big\|\|B^{\dagger}\|\|u(r)\|dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​∫0t2​‖(SA−S†)​(t−r)​(D​yA​(r)+E​u​(r))‖2​𝑑r\displaystyle+\mathbb{E}\int\_{0}^{t}2\big\|(S^{A}-S^{\dagger})(t-r)(Dy^{A}(r)+Eu(r))\big\|^{2}dr |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼​∫0t2​‖S†​(t−r)​D​(yA−y†)​(r)‖2​𝑑r.\displaystyle+\mathbb{E}\int\_{0}^{t}2\big\|S^{\dagger}(t-r)D(y^{A}-y^{\dagger})(r)\big\|^{2}dr. |  | (A.35) |

As in the proof of [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3], we have the following bounds for yAy^{A} and y†y^{\dagger}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖yA​(t)‖2≤2​(MTA)2​‖ξ‖2​exp⁡(16​T​(MTA)2​‖D‖2​tr​(Q)),𝔼​‖y†​(t)‖2≤2​(MTA†)2​‖ξ‖2​exp⁡(16​T​(MTA†)2​‖D‖2​tr​(Q)).\displaystyle\begin{aligned} &\mathbb{E}\|y^{A}(t)\|^{2}\leq 2(M^{A}\_{T})^{2}\|\xi\|^{2}\exp\big(16T(M^{A}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big),\\ &\mathbb{E}\|y^{\dagger}(t)\|^{2}\leq 2(M\_{T}^{A^{\dagger}})^{2}\|\xi\|^{2}\exp\big(16T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big).\end{aligned} |  | (A.36) |

where each MTAM^{A}\_{T} and MTA†M^{A^{\dagger}}\_{T} are the upper bounds for SAS^{A} and S†S^{\dagger} such that
‖S​(t)‖≤MTA\|S(t)\|\leq M^{A}\_{T} and
‖S†​(t)‖≤MTA†\|S^{\dagger}(t)\|\leq M^{A^{\dagger}}\_{T}, for all t∈𝒯t\in\mathcal{T}.

From ([A.50](https://arxiv.org/html/2510.20017v1#A1.E50 "Equation A.50 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) with u​(t)=0u(t)=0 for all t∈𝒯t\in\mathcal{T}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​(‖(yA−y†)​(t)‖2)\displaystyle\mathbb{E}\big(\|(y^{A}-y^{\dagger})(t)\|^{2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​∫0t2​‖(SA−S†)​(t−r)​D​y​(r)‖2​𝑑r+𝔼​∫0t2​‖S†​(t−r)​D​(yA−y†)​(r)‖2​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}2\big\|(S^{A}-S^{\dagger})(t-r)Dy(r)\big\|^{2}dr+\mathbb{E}\int\_{0}^{t}2\big\|S^{\dagger}(t-r)D(y^{A}-y^{\dagger})(r)\big\|^{2}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​∫0t2​‖(SA−S†)​(t−r)‖2​‖D‖2​‖yA​(r)‖2​𝑑r+𝔼​∫0t2​‖S†​(t−r)‖2​‖D‖2​‖(yA−y†)​(r)‖2​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}2\big\|(S^{A}-S^{\dagger})(t-r)\big\|^{2}\|D\|^{2}\|y^{A}(r)\|^{2}dr+\mathbb{E}\int\_{0}^{t}2\big\|S^{\dagger}(t-r)\big\|^{2}\|D\|^{2}\|(y^{A}-y^{\dagger})(r)\|^{2}dr |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​∫0t2​‖(SA−S†)​(t−r)‖2​‖D‖2​‖yA​(r)‖2​𝑑r+𝔼​∫0t2​(MTA†)2​‖D‖2​‖(yA−y†)​(r)‖2​𝑑r.\displaystyle\mathbb{E}\int\_{0}^{t}2\big\|(S^{A}-S^{\dagger})(t-r)\big\|^{2}\|D\|^{2}\|y^{A}(r)\|^{2}dr+\mathbb{E}\int\_{0}^{t}2(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\|(y^{A}-y^{\dagger})(r)\|^{2}dr. |  | (A.37) |

By the Grönwall’s inequality and ([A.36](https://arxiv.org/html/2510.20017v1#A1.E36 "Equation A.36 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we further have that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​(‖yA​(t)−y†​(t)‖2)\displaystyle\mathbb{E}\big(\|y^{A}(t)-y^{\dagger}(t)\|^{2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​∫0t2​‖(SA−S†)​(t−r)‖2​‖D‖2​‖yA​(r)‖2​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}2\big\|(S^{A}-S^{\dagger})(t-r)\big\|^{2}\|D\|^{2}\|y^{A}(r)\|^{2}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t[𝔼​∫0s2​‖(SA−S†)​(s−r)‖2​‖D‖2​‖yA​(r)‖2​𝑑r]​2​(MTA†)2​‖D‖2​exp⁡(2​(MTA†)2​‖D‖2​(t−s))​𝑑s\displaystyle+\int\_{0}^{t}\Big[\mathbb{E}\int\_{0}^{s}2\big\|(S^{A}-S^{\dagger})(s-r)\big\|^{2}\|D\|^{2}\|y^{A}(r)\|^{2}dr\Big]2(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\exp\big(2(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}(t-s)\big)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​∫0t2​‖(SA−S†)​(t−r)‖2​‖D‖2​‖yA​(r)‖2​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}2\|(S^{A}-S^{\dagger})(t-r)\|^{2}\|D\|^{2}\|y^{A}(r)\|^{2}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −[𝔼​∫0t2​‖(SA−S†)​(t−r)‖2​‖D‖2​‖yA​(r)‖2​𝑑r]​∫0t2​(MTA†)2​‖D‖2​exp⁡(2​(MTA†)2​‖D‖2​(t−s))​𝑑s\displaystyle-\Big[\mathbb{E}\int\_{0}^{t}2\big\|(S^{A}-S^{\dagger})(t-r)\big\|^{2}\|D\|^{2}\|y^{A}(r)\|^{2}dr\Big]\int\_{0}^{t}2(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\exp\big(2(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}(t-s)\big)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | [𝔼​∫0t2​‖(SA−S†)​(t−r)‖2​‖D‖2​‖yA​(r)‖2​𝑑r]​[1−1+exp⁡(2​(MTA†)2​‖D‖2​t)]\displaystyle\Big[\mathbb{E}\int\_{0}^{t}2\|(S^{A}-S^{\dagger})(t-r)\|^{2}\|D\|^{2}\|y^{A}(r)\|^{2}dr\Big]\Big[1-1+\exp(2(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}t)\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 2​supt∈𝒯‖(SA−S†)​(t)‖2​‖D‖2​T​[2​(MTA)2​‖ξ‖2​exp⁡(16​T​(MTA)2​‖D‖2​tr​(Q))]​exp⁡(2​(MTA†)2​‖D‖2​T).\displaystyle 2\sup\_{t\in\mathcal{T}}\|(S^{A}-S^{\dagger})(t)\|^{2}\|D\|^{2}T\Big[2(M\_{T}^{A})^{2}\|\xi\|^{2}\exp\big(16T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\Big]\exp(2(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}T). |  | (A.38) |

We have from ([A.36](https://arxiv.org/html/2510.20017v1#A1.E36 "Equation A.36 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and
([A.38](https://arxiv.org/html/2510.20017v1#A1.E38 "Equation A.38 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (supt∈𝒯𝔼​‖yA​(t)‖2)1/2≤2​(MTA)​‖ξ‖​exp⁡(8​T​(MTA)2​‖D‖2​tr​(Q)),(supt∈𝒯𝔼​‖y†​(t)‖2)1/2≤2​(MTA†)​‖ξ‖​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q)),\displaystyle\begin{aligned} &\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|y^{A}(t)\big\|^{2}\big)^{1/2}\leq\sqrt{2}(M\_{T}^{A})\|\xi\|\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big),\\ &\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|y^{\dagger}(t)\big\|^{2}\big)^{1/2}\leq\sqrt{2}(M\_{T}^{A^{\dagger}})\|\xi\|\exp\big(8T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big),\end{aligned} |  | (A.39) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | (supt∈𝒯𝔼\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E} | ∥yA(t)−y†(t)∥2)1/2\displaystyle\big\|y^{A}(t)-y^{\dagger}(t)\big\|^{2}\big)^{1/2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​supt∈𝒯‖(SA−S†)​(t)‖​‖D‖​T1/2​[MTA​‖ξ‖​exp⁡(8​T​(MTA)2​‖D‖2​tr​(Q))]​exp⁡((MTA†)2​‖D‖2​T).\displaystyle\leq 2\sup\_{t\in\mathcal{T}}\|(S^{A}-S^{\dagger})(t)\|\|D\|T^{1/2}\big[M\_{T}^{A}\|\xi\|\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big]\exp((M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}T). |  | (A.40) |

By the proof of [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3], we have for any u​(t)u(t), t∈𝒯t\in\mathcal{T} that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ΠA​(t)​ξ,ξ⟩=\displaystyle\langle\Pi^{A}(t)\xi,\xi\rangle= | 𝔼​∫0t(‖M1/2​yA​(r)‖2+‖u​(r)‖2)​𝑑r+𝔼​‖G1/2​yA​(t)‖2\displaystyle\mathbb{E}\int\_{0}^{t}\big(\big\|M^{1/2}y^{A}(r)\big\|^{2}+\|u(r)\|^{2}\big)dr+\mathbb{E}\big\|G^{1/2}y^{A}(t)\big\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​∫0t‖u​(r)+(KA)−1​LA​(T−r)​yA​(r)‖2​𝑑r,\displaystyle-\mathbb{E}\int\_{0}^{t}\big\|u(r)+(K^{A})^{-1}L^{A}(T-r)y^{A}(r)\big\|^{2}dr, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Π†​(t)​ξ,ξ⟩=\displaystyle\langle\Pi^{\dagger}(t)\xi,\xi\rangle= | 𝔼​∫0t(‖M1/2​y†​(r)‖2+‖u​(r)‖2)​𝑑r+𝔼​‖G1/2​y†​(t)‖2\displaystyle\mathbb{E}\int\_{0}^{t}\big(\big\|M^{1/2}y^{\dagger}(r)\big\|^{2}+\|u(r)\|^{2}\big)dr+\mathbb{E}\big\|G^{1/2}y^{\dagger}(t)\big\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​∫0t‖u​(r)+(K†)−1​L†​(T−r)​y†​(r)‖2​𝑑r.\displaystyle-\mathbb{E}\int\_{0}^{t}\big\|u(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\|^{2}dr. |  |

It then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟨(ΠA​(t)−Π†​(t))​ξ,ξ⟩\displaystyle\langle(\Pi^{A}(t)-\Pi^{\dagger}(t))\xi,\xi\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​∫0t‖M1/2​yA​(r)‖2−‖M1/2​y†​(r)‖2​d​r+𝔼​(‖G1/2​yA​(t)‖2−‖G1/2​y†​(t)‖2)\displaystyle\mathbb{E}\int\_{0}^{t}\big\|M^{1/2}y^{A}(r)\big\|^{2}-\big\|M^{1/2}y^{\dagger}(r)\big\|^{2}dr+\mathbb{E}\big(\big\|G^{1/2}y^{A}(t)\big\|^{2}-\big\|G^{1/2}y^{\dagger}(t)\big\|^{2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​∫0t(‖u​(r)+(KA)−1​LA​(T−r)​yA​(r)‖2−‖u​(r)+(K†)−1​L†​(T−r)​y†​(r)‖2)​𝑑r\displaystyle-\mathbb{E}\int\_{0}^{t}\big(\big\|u(r)+(K^{A})^{-1}L^{A}(T-r)y^{A}(r)\big\|^{2}-\big\|u(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\|^{2}\big)dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​∫0t⟨M1/2​(yA​(r)−y†​(r)),M1/2​(yA​(r)+y†​(r))⟩​𝑑r+𝔼​⟨G1/2​(yA​(t)−y†​(t)),G1/2​(yA​(t)+y†​(t))⟩\displaystyle\mathbb{E}\int\_{0}^{t}\langle M^{1/2}(y^{A}(r)-y^{\dagger}(r)),M^{1/2}(y^{A}(r)+y^{\dagger}(r))\rangle dr+\mathbb{E}\langle G^{1/2}(y^{A}(t)-y^{\dagger}(t)),G^{1/2}(y^{A}(t)+y^{\dagger}(t))\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼∫0t⟨(KA)−1LA(T−r)yA(r)−(K†)−1L†(T−r)y†(r),\displaystyle-\mathbb{E}\int\_{0}^{t}\bigl\langle(K^{A})^{-1}L^{A}(T-r)y^{A}(r)-(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (KA)−1LA(T−r)yA(r)+(K†)−1L†(T−r)y†(r)+2u(r)⟩dr.\displaystyle\hskip 56.9055pt(K^{A})^{-1}L^{A}(T-r)y^{A}(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)+2u(r)\bigr\rangle dr. |  |

We take u​(t)=0u(t)=0, for all t∈𝒯t\in\mathcal{T}, and let yAy^{A} and y†y^{\dagger} be the states corresponding to u​(t)=0u(t)=0, t∈𝒯t\in\mathcal{T}.
It then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(ΠA(t)\displaystyle\langle(\Pi^{A}(t) | −Π†(t))ξ,ξ⟩\displaystyle-\Pi^{\dagger}(t))\xi,\xi\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​∫0t⟨M1/2​(yA​(r)−y†​(r)),M1/2​(yA​(r)+y†​(r))⟩​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}\langle M^{1/2}(y^{A}(r)-y^{\dagger}(r)),M^{1/2}(y^{A}(r)+y^{\dagger}(r))\rangle dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​⟨G1/2​(yA​(t)−y†​(t)),G1/2​(yA​(t)+y†​(t))⟩\displaystyle\hskip 28.45274pt+\mathbb{E}\langle G^{1/2}(y^{A}(t)-y^{\dagger}(t)),G^{1/2}(y^{A}(t)+y^{\dagger}(t))\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼∫0t⟨(KA)−1LA(T−r)yA(r)−(K†)−1L†(T−r)y†(r),\displaystyle\hskip 28.45274pt-\mathbb{E}\int\_{0}^{t}\bigl\langle(K^{A})^{-1}L^{A}(T-r)y^{A}(r)-(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (KA)−1LA(T−r)yA(r)+(K†)−1L†(T−r)y†(r)⟩dr\displaystyle\hskip 56.9055pt(K^{A})^{-1}L^{A}(T-r)y^{A}(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\bigr\rangle dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​∫0t‖M‖​|yA​(r)−y†​(r)|​|yA​(r)+y†​(r)|​𝑑r+𝔼​(‖G‖​|yA​(t)−y†​(t)|​|yA​(t)+y†​(t)|)\displaystyle\leq\mathbb{E}\int\_{0}^{t}\|M\||y^{A}(r)-y^{\dagger}(r)||y^{A}(r)+y^{\dagger}(r)|dr+\mathbb{E}\big(\|G\||y^{A}(t)-y^{\dagger}(t)||y^{A}(t)+y^{\dagger}(t)|\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​∫0t‖(KA)−1​LA​(T−r)​yA​(r)−(K†)−1​L†​(T−r)​y†​(r)‖\displaystyle\hskip 28.45274pt+\mathbb{E}\int\_{0}^{t}\big\|(K^{A})^{-1}L^{A}(T-r)y^{A}(r)-(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×‖(KA)−1​LA​(T−r)​yA​(r)+(K†)−1​L†​(T−r)​y†​(r)‖​d​r.\displaystyle\hskip 85.35826pt\times\big\|(K^{A})^{-1}L^{A}(T-r)y^{A}(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\|dr. |  | (A.41) |

The following estimates of ΠA\Pi^{A} and Π†\Pi^{\dagger} are given by [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ΠA​(t)‖≤CAΠ,‖Π†​(t)‖≤CΠ†∀t∈𝒯,\displaystyle\|\Pi^{A}(t)\|\leq C^{\Pi}\_{A},\quad\|\Pi^{\dagger}(t)\|\leq C^{\Pi^{\dagger}}\quad\forall t\in\mathcal{T}, |  | (A.42) |
|  |  |  |
| --- | --- | --- |
|  | CAΠ=2​(MTA)2​exp⁡(8​T​(MTA)2​‖D‖2​tr​(Q))​(‖G‖+T​‖M‖),\displaystyle C^{\Pi}\_{A}=2(M\_{T}^{A})^{2}\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big(\|G\|+T\|M\|\big), |  |
|  |  |  |
| --- | --- | --- |
|  | CΠ†=2​(MTA†)2​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))​(‖G‖+T​‖M‖).\displaystyle C^{\Pi^{\dagger}}=2(M\_{T}^{A^{\dagger}})^{2}\exp\big(8T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big(\|G\|+T\|M\|\big). |  |

By the estimates for Δ1\Delta\_{1} and Δ2\Delta\_{2} in [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Theorem 4.1], the estimate for Π\Pi in [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3], and the bounds ‖(KA)−1​(t)‖≤1\|(K^{A})^{-1}(t)\|\leq 1 and ‖(K†)−1​(t)‖≤1\|(K^{\dagger})^{-1}(t)\|\leq 1, ∀t∈𝒯\forall t\in\mathcal{T}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(KA)−1LA(t)−\displaystyle\big\|(K^{A})^{-1}L^{A}(t)- | (K†)−1L†(t)∥\displaystyle(K^{\dagger})^{-1}L^{\dagger}(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ‖(KA)−1​(LA−L†)​(t)+((KA)−1−(K†)−1)​L†​(t)‖\displaystyle\big\|(K^{A})^{-1}\big(L^{A}-L^{\dagger}\big)(t)+\big((K^{A})^{-1}-(K^{\dagger})^{-1}\big)L^{\dagger}(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖(KA)−1​(t)‖​‖(LA−L†)​(t)‖+‖(KA)−1​(t)‖​‖(K†−KA)​(t)‖​‖(K†)−1​(t)‖​‖L†​(t)‖\displaystyle\big\|(K^{A})^{-1}(t)\big\|\big\|\big(L^{A}-L^{\dagger}\big)(t)\big\|+\big\|(K^{A})^{-1}(t)\big\|\big\|(K^{\dagger}-K^{A})(t)\big\|\big\|(K^{\dagger})^{-1}(t)\big\|\big\|L^{\dagger}(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (‖B†‖+‖Δ1‖)​‖(ΠA−Π†)​(t)‖+‖Δ3‖​‖(ΠA−Π†)​(t)‖​(‖B†‖+‖Δ1‖)​CΠ†\displaystyle(\|B^{\dagger}\|+\|\Delta\_{1}\|)\|(\Pi^{A}-\Pi^{\dagger})(t)\|+\|\Delta\_{3}\|\|(\Pi^{A}-\Pi^{\dagger})(t)\|(\|B^{\dagger}\|+\|\Delta\_{1}\|)C^{\Pi^{\dagger}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (‖B†‖+R3)​(1+R5​CΠ†)​‖(ΠA−Π†)​(t)‖,\displaystyle(\|B^{\dagger}\|+R\_{3})(1+R\_{5}C^{\Pi^{\dagger}})\|(\Pi^{A}-\Pi^{\dagger})(t)\|, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(KA)−1\displaystyle\big\|(K^{A})^{-1} | LA(T−r)y(r)−(K†)−1L†(T−r)y†(r)∥\displaystyle L^{A}(T-r)y(r)-(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖(KA)−1‖​‖LA​(T−r)‖​‖yA​(r)−y†​(r)‖+‖((KA)−1​LA−(K†)−1​L†)​(t−r)‖​‖y†​(r)‖\displaystyle\big\|(K^{A})^{-1}\big\|\big\|L^{A}(T-r)\big\|\big\|y^{A}(r)-y^{\dagger}(r)\big\|+\big\|\big((K^{A})^{-1}L^{A}-(K^{\dagger})^{-1}L^{\dagger}\big)(t-r)\big\|\big\|y^{\dagger}(r)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (‖B†‖+R3)​CAΠ​‖yA​(r)−y†​(r)‖+(‖B†‖+‖Δ1‖)​(1+‖Δ3‖​CΠ†)​‖(ΠA−Π†)​(t)‖​‖y†​(r)‖\displaystyle(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}\big\|y^{A}(r)-y^{\dagger}(r)\big\|+(\|B^{\dagger}\|+\|\Delta\_{1}\|)(1+\|\Delta\_{3}\|C^{\Pi^{\dagger}})\|(\Pi^{A}-\Pi^{\dagger})(t)\|\big\|y^{\dagger}(r)\big\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (‖B†‖+R3)​CAΠ​‖yA​(r)−y†​(r)‖+(‖B†‖+R3)​(1+R5​CΠ†)​‖(ΠA−Π†)​(t)‖​‖y†​(r)‖,\displaystyle(\|B^{\dagger}\|+R\_{3})C^{\Pi}\_{A}\big\|y^{A}(r)-y^{\dagger}(r)\big\|+(\|B^{\dagger}\|+R\_{3})(1+R\_{5}C^{\Pi^{\dagger}})\|(\Pi^{A}-\Pi^{\dagger})(t)\|\big\|y^{\dagger}(r)\big\|, |  | (A.43) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(KA)−1LA(T−r)yA(r)\displaystyle\big\|(K^{A})^{-1}L^{A}(T-r)y^{A}(r) | +(K†)−1L†(T−r)y†(r)∥\displaystyle+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖(KA)−1‖​‖LA​(T−r)‖​‖yA​(r)‖+‖(K†)−1‖​‖L†​(T−r)‖​‖y†​(r)‖\displaystyle\big\|(K^{A})^{-1}\big\|\big\|L^{A}(T-r)\big\|\|y^{A}(r)\|+\big\|(K^{\dagger})^{-1}\big\|\big\|L^{\dagger}(T-r)\big\|\big\|y^{\dagger}(r)\big\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (‖B†‖+R3)​(CAΠ​‖yA​(r)‖+CΠ†​‖y†​(r)‖).\displaystyle(\|B^{\dagger}\|+R\_{3})(C^{\Pi}\_{A}\|y^{A}(r)\|+C^{\Pi^{\dagger}}\|y^{\dagger}(r)\|). |  | (A.44) |

From ([A.41](https://arxiv.org/html/2510.20017v1#A1.E41 "Equation A.41 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), ([A.43](https://arxiv.org/html/2510.20017v1#A1.E43 "Equation A.43 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators"))
and ([A.44](https://arxiv.org/html/2510.20017v1#A1.E44 "Equation A.44 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1‖ξ‖2​⟨(ΠA−Π†)​(t)​ξ,ξ⟩\displaystyle\frac{1}{\|\xi\|^{2}}\langle(\Pi^{A}-\Pi^{\dagger})(t)\xi,\xi\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1‖ξ‖2​‖M‖​(T+1)​(supr∈𝒯𝔼​‖yA​(r)−y†​(r)‖2)1/2​[(supr∈𝒯𝔼​‖yA​(r)‖2)1/2+(supr∈𝒯𝔼​‖y†​(r)‖2)1/2]\displaystyle\frac{1}{\|\xi\|^{2}}\|M\|(T+1)\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\big\|y^{A}(r)-y^{\dagger}(r)\big\|^{2}\big)^{1/2}\Big[\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{A}(r)\|^{2}\big)^{1/2}+\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1‖ξ‖2​T​(‖B†‖+R3)2​CΠ†​[CAΠ​(supr∈𝒯𝔼​‖yA​(r)‖2)1/2+CΠ†​(supr∈𝒯𝔼​‖y†​(r)‖2)1/2]\displaystyle+\frac{1}{\|\xi\|^{2}}T(\|B^{\dagger}\|+R\_{3})^{2}C^{\Pi^{\dagger}}\Big[C^{\Pi}\_{A}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{A}(r)\|^{2}\big)^{1/2}+C^{\Pi^{\dagger}}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(supt∈𝒯𝔼​‖yA​(r)−y†​(r)‖2)1/2+1‖ξ‖2​(‖B†‖+R3)2​(1+R5​CΠ†)\displaystyle\times\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|y^{A}(r)-y^{\dagger}(r)\|^{2}\big)^{1/2}+\frac{1}{\|\xi\|^{2}}(\|B^{\dagger}\|+R\_{3})^{2}(1+R\_{5}C^{\Pi^{\dagger}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[CAΠ​(supt∈𝒯𝔼​‖yA​(r)‖2)1/2​(supr∈𝒯𝔼​‖y†​(r)‖2)1/2+CΠ†​(supr∈𝒯𝔼​‖y†​(r)‖2)1/2]​∫0t‖(ΠA−Π†)​(r)‖​𝑑r.\displaystyle\times\Big[C^{\Pi}\_{A}\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|y^{A}(r)\big\|^{2}\big)^{1/2}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}+C^{\Pi^{\dagger}}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}\Big]\int\_{0}^{t}\|(\Pi^{A}-\Pi^{\dagger})(r)\|dr. |  |

Then, from Grönwall’s inequality and the estimates ([A.36](https://arxiv.org/html/2510.20017v1#A1.E36 "Equation A.36 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.38](https://arxiv.org/html/2510.20017v1#A1.E38 "Equation A.38 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(ΠA−Π†)​(t)‖≤\displaystyle\big\|(\Pi^{A}-\Pi^{\dagger})(t)\big\|\leq | 1‖ξ‖2​{‖M‖​(T+1)+T​(‖B†‖+R3)2​CAΠ}​(1+CAΠ+CΠ†)\displaystyle\frac{1}{\|\xi\|^{2}}\Big\{\|M\|(T+1)+T(\|B^{\dagger}\|+R\_{3})^{2}C^{\Pi}\_{A}\Big\}(1+C^{\Pi}\_{A}+C^{\Pi^{\dagger}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[(supr∈𝒯𝔼​‖yA​(r)‖2)1/2+(supr∈𝒯𝔼​‖y†​(r)‖2)1/2]​(supr∈𝒯𝔼​‖yA​(r)−y†​(r)‖2)1/2\displaystyle\times\Big[\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{A}(r)\|^{2}\big)^{1/2}+\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}\Big]\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{A}(r)-y^{\dagger}(r)\|^{2}\big)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp{1‖ξ‖2T(∥B†∥+R3)2(1+R5CΠ†)\displaystyle\times\exp\Big\{\frac{1}{\|\xi\|^{2}}T(\|B^{\dagger}\|+R\_{3})^{2}(1+R\_{5}C^{\Pi^{\dagger}}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×[CAΠ(supr∈𝒯𝔼∥yA(r)∥2)1/2(supr∈𝒯𝔼∥y†(r)∥2)1/2+CΠ†(supr∈𝒯𝔼∥y†(r)∥2)1/2]}.\displaystyle\hskip 31.2982pt\times\Big[C^{\Pi}\_{A}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\big\|y^{A}(r)\big\|^{2}\big)^{1/2}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}+C^{\Pi^{\dagger}}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}\Big]\Big\}. |  | (A.45) |

By ([A.39](https://arxiv.org/html/2510.20017v1#A1.E39 "Equation A.39 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.40](https://arxiv.org/html/2510.20017v1#A1.E40 "Equation A.40 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | [(supr∈𝒯𝔼​‖yA​(r)‖2)1/2+(supr∈𝒯𝔼​‖y†​(r)‖2)1/2]​(supt∈𝒯𝔼​‖yA​(r)−y†​(r)‖2)1/2\displaystyle\Big[\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{A}(r)\|^{2}\big)^{1/2}+\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}\Big]\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|y^{A}(r)-y^{\dagger}(r)\|^{2}\big)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 2​‖ξ‖​[(MTA)​exp⁡(8​T​(MTA)2​‖D‖2​tr​(Q))+(MTA†)​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))]\displaystyle\sqrt{2}\|\xi\|\big[(M\_{T}^{A})\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)+(M\_{T}^{A^{\dagger}})\exp\big(8T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×2​supt∈𝒯‖(S−S†)​(t)‖​‖D‖​T1/2​[2​MTA​‖ξ‖​exp⁡(8​T​(MTA)2​‖D‖2​tr​(Q))]​exp⁡((MTA†)2​‖D‖2​T)\displaystyle\times\sqrt{2}\sup\_{t\in\mathcal{T}}\|(S-S^{\dagger})(t)\|\|D\|T^{1/2}\Big[\sqrt{2}M\_{T}^{A}\|\xi\|\exp\big(8T(M\_{T}^{A})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\Big]\exp((M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}T) |  | (A.46) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (supt∈𝒯𝔼​‖yA​(r)‖2)1/2\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|y^{A}(r)\big\|^{2}\big)^{1/2} | (supt∈𝒯𝔼​‖y†​(r)‖2)1/2≤2​MTA​MTA†​‖ξ‖2​exp⁡[8​T​((MTA)2+(MTA†)2)​‖D‖2​tr​(Q)].\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(r)\|^{2}\big)^{1/2}\leq 2M\_{T}^{A}M\_{T}^{A^{\dagger}}\|\xi\|^{2}\exp\big[8T\big((M\_{T}^{A})^{2}+(M\_{T}^{A^{\dagger}})^{2}\big)\|D\|^{2}\mathrm{tr}(Q)\big]. |  | (A.47) |

Substituting ([A.46](https://arxiv.org/html/2510.20017v1#A1.E46 "Equation A.46 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and
([A.47](https://arxiv.org/html/2510.20017v1#A1.E47 "Equation A.47 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) into ([A.45](https://arxiv.org/html/2510.20017v1#A1.E45 "Equation A.45 ‣ A.4.2 Proof of Lemma 4.4 ‣ A.4 Proofs of Lipschitz Stability with respect to 𝐴 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")),
we obtain
([4.4](https://arxiv.org/html/2510.20017v1#S4.E4 "Equation 4.4 ‣ Lemma 4.4. ‣ 4.1 Stability of the equilibrium with respect to operator 𝐴 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
∎

#### A.4.3 Proof of Lemma [4.5](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1 Stability of the equilibrium with respect to operator 𝐴 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

From ([A.23](https://arxiv.org/html/2510.20017v1#A1.E23 "Equation A.23 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.24](https://arxiv.org/html/2510.20017v1#A1.E24 "Equation A.24 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(x¯A−x¯†)​(t)‖≤\displaystyle\big\|(\bar{x}^{A}-\bar{x}^{\dagger})(t)\big\|\leq | ‖(SA−S†)​(t)‖​‖ξ¯‖+∫0t‖(SA−S†)​(t−r)‖​‖ΦA​(r)‖​𝑑r\displaystyle\big\|(S^{A}-S^{\dagger})(t)\big\|\|\bar{\xi}\|\!+\!\!\int\_{0}^{t}\!\!\big\|(S^{A}-S^{\dagger})(t-r)\big\|\big\|\Phi^{A}(r)\big\|dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t‖S†​(t−r)‖​‖ΦA​(r)−Φ†​(r)‖​𝑑r,\displaystyle+\!\!\int\_{0}^{t}\!\!\big\|S^{\dagger}(t-r)\big\|\big\|\Phi^{A}(r)-\Phi^{\dagger}(r)\big\|dr, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(qA−q†)​(t)‖≤\displaystyle\|(q^{A}-q^{\dagger})(t)\|\leq | (∥(SA−S†)(t)∥∥x†∥+∥S†∥∥(x¯A−x¯†∥)(T))∥G∥∥F^2∥\displaystyle\big(\|(S^{A}-S^{\dagger})(t)\|\|x^{\dagger}\|+\|S^{\dagger}\|\|(\bar{x}^{A}-\bar{x}^{\dagger}\|)(T)\big)\|G\|\|\widehat{F}\_{2}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t(‖(SA−S†)​(t−r)‖​‖ΨA​(r)‖+‖S†​(t−r)‖​‖(ΨA−Ψ†)​(r)‖)​𝑑r,\displaystyle+\int\_{0}^{t}\left(\|(S^{A}-S^{\dagger})(t-r)\|\|\Psi^{A}(r)\|+\|S^{\dagger}(t-r)\|\|(\Psi^{A}-\Psi^{\dagger})(r)\|\right)dr, |  |

where Φ†\Phi^{\dagger} and Ψ†\Psi^{\dagger} are given by ([A.21](https://arxiv.org/html/2510.20017v1#A1.E21 "Equation A.21 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.22](https://arxiv.org/html/2510.20017v1#A1.E22 "Equation A.22 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), respectively, and ΦA\Phi^{A} and ΨA\Psi^{A} are defined analogously for the perturbed operator AA. Since

|  |  |  |
| --- | --- | --- |
|  | ‖ΦA​(r)−Φ†​(r)‖≤CA,A†Φ,x¯​‖(x¯A−x¯†)​(r)‖+CA,A†Φ,q​‖(qA−q†)​(T−r)‖+CA,A†Φ,Π​‖(ΠA−Π†)​(T−r)‖,\displaystyle\big\|\Phi^{A}(r)-\Phi^{\dagger}(r)\big\|\leq C^{\Phi,\bar{x}}\_{A,A^{\dagger}}\|(\bar{x}^{A}-\bar{x}^{\dagger})(r)\|+C^{\Phi,q}\_{A,A^{\dagger}}\|(q^{A}-q^{\dagger})(T-r)\|+C^{\Phi,\Pi}\_{A,A^{\dagger}}\big\|(\Pi^{A}-\Pi^{\dagger})(T-r)\big\|, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖ΨA​(r)−Ψ†​(r)‖≤CA,A†Ψ,x¯​‖(x¯A−x¯†)​(T−r)‖+CA,A†Ψ,q​‖(qA−q†)​(r)‖+CA,A†Ψ,Π​‖(ΠA−Π†)​(r)‖,\displaystyle\big\|\Psi^{A}(r)-\Psi^{\dagger}(r)\big\|\leq C^{\Psi,\bar{x}}\_{A,A^{\dagger}}\|(\bar{x}^{A}-\bar{x}^{\dagger})(T-r)\|+C^{\Psi,q}\_{A,A^{\dagger}}\|(q^{A}-q^{\dagger})(r)\|+C^{\Psi,\Pi}\_{A,A^{\dagger}}\big\|(\Pi^{A}-\Pi^{\dagger})(r)\big\|, |  |

where the constants CA,A†Φ,x¯C^{\Phi,\bar{x}}\_{A,A^{\dagger}}, CA,A†Φ,qC^{\Phi,q}\_{A,A^{\dagger}}, CA,A†Φ,ΠC^{\Phi,\Pi}\_{A,A^{\dagger}},
CA,A†Ψ,x¯C^{\Psi,\bar{x}}\_{A,A^{\dagger}}, CA,A†Ψ,qC^{\Psi,q}\_{A,A^{\dagger}}, and CA,A†Ψ,ΠC^{\Psi,\Pi}\_{A,A^{\dagger}} are defined in the statement of the lemma,
it then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(x¯A\displaystyle\big\|(\bar{x}^{A} | −x¯†)(t)∥\displaystyle-\bar{x}^{\dagger})(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | MTA,A†​‖A−A†‖​‖ξ¯‖+∫0tMTA,A†​‖A−A†‖​(CA,A†Φ,x¯​CAx¯+CA,A†Φ,q​CAq+CA,A†Φ,c)​𝑑r\displaystyle M^{A,A^{\dagger}}\_{T}\|A-A^{\dagger}\|\|\bar{\xi}\|+\int\_{0}^{t}M^{A,A^{\dagger}}\_{T}\|A-A^{\dagger}\|\big(C^{\Phi,\bar{x}}\_{A,A^{\dagger}}C^{\bar{x}}\_{A}+C^{\Phi,q}\_{A,A^{\dagger}}C^{q}\_{A}+C^{\Phi,c}\_{A,A^{\dagger}}\big)dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tMTA†​(CA,A†Φ,x¯​‖(x¯A−x¯†)​(r)‖+CA,A†Φ,q​‖(qA−q†)​(T−r)‖+CA,A†Φ,Π​CA,A†Π​‖A−A†‖)​𝑑r\displaystyle+\int\_{0}^{t}M^{A^{\dagger}}\_{T}\big(C^{\Phi,\bar{x}}\_{A,A^{\dagger}}\|(\bar{x}^{A}-\bar{x}^{\dagger})(r)\|+C^{\Phi,q}\_{A,A^{\dagger}}\|(q^{A}-q^{\dagger})(T-r)\|+C^{\Phi,\Pi}\_{A,A^{\dagger}}C^{\Pi}\_{A,A^{\dagger}}\|A-A^{\dagger}\|\big)dr |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(qA\displaystyle\big\|(q^{A} | −q†)(t)∥\displaystyle-q^{\dagger})(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (MTA,A†​‖A−A†‖​Cx¯+MTA†​‖(x¯A−x¯†)​(T)‖)​‖G‖​‖F^2‖\displaystyle\big(M^{A,A^{\dagger}}\_{T}\|A-A^{\dagger}\|C^{\bar{x}}+M^{A^{\dagger}}\_{T}\|(\bar{x}^{A}-\bar{x}^{\dagger})(T)\|\big)\|G\|\|\widehat{F}\_{2}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tMTA,A†​‖A−A†‖​(CA,A†Ψ,q​CAq+CA,A†Ψ,x¯​CAx¯+CA,A†Ψ,c)​𝑑r\displaystyle+\int\_{0}^{t}M^{A,A^{\dagger}}\_{T}\|A-A^{\dagger}\|\big(C^{\Psi,q}\_{A,A^{\dagger}}C^{q}\_{A}+C^{\Psi,\bar{x}}\_{A,A^{\dagger}}C^{\bar{x}}\_{A}+C^{\Psi,c}\_{A,A^{\dagger}}\big)dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tMTA†​(CA,A†Ψ,q​‖(qA−q†)​(r)‖+CA,A†Ψ,x¯​‖(x¯A−x¯†)​(T−r)‖+CA,A†Ψ,Π​CA,A†Π​‖A−A†‖)​𝑑r.\displaystyle+\int\_{0}^{t}M^{A^{\dagger}}\_{T}\big(C^{\Psi,q}\_{A,A^{\dagger}}\|(q^{A}-q^{\dagger})(r)\|+C^{\Psi,\bar{x}}\_{A,A^{\dagger}}\|(\bar{x}^{A}-\bar{x}^{\dagger})(T-r)\|+C^{\Psi,\Pi}\_{A,A^{\dagger}}C^{\Pi}\_{A,A^{\dagger}}\|A-A^{\dagger}\|\big)dr. |  |

Applying Lemma [A.2](https://arxiv.org/html/2510.20017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") to the above two inequalities, we obtain
the desired estimates for
‖x¯A−x¯†‖C​(𝒯;H)\|\bar{x}^{A}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}
and
‖qA−q†‖C​(𝒯;H)\|q^{A}-q^{\dagger}\|\_{C(\mathcal{T};H)}.
∎

### A.5 Proof of Lipschitz Stability with respect to BB

#### A.5.1 Proofs of Lemma [4.8](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4.2 Stability of the equilibrium with respect to operator 𝐵 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

The proof is carried out in a similar manner as in [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3].
We introduce the processes corresponding to BB and B†B^{\dagger}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | d​yB​(t)=(A†​yB​(t)+B​u​(t))​d​t+(D​yB​(t)+E​u​(t))​d​W​(t),yB​(0)=ξ,\displaystyle dy^{B}(t)=(A^{\dagger}y^{B}(t)+Bu(t))dt+(Dy^{B}(t)+Eu(t))dW(t),\quad y^{B}(0)=\xi, |  | (A.48) |
|  |  | d​y†​(t)=(A†​y†​(t)+B†​u​(t))​d​t+(D​y†​(t)+E​u​(t))​d​W​(t),y†​(0)=ξ,\displaystyle dy^{\dagger}(t)=(A^{\dagger}y^{\dagger}(t)+B^{\dagger}u(t))dt+(Dy^{\dagger}(t)+Eu(t))dW(t),\quad y^{\dagger}(0)=\xi, |  |

and the cost functionals

|  |  |  |
| --- | --- | --- |
|  | 𝔼​∫0T(‖M1/2​yB​(t)‖2+‖u​(t)‖2)​𝑑t+𝔼​‖G1/2​yB​(T)‖2,\displaystyle\mathbb{E}\int\_{0}^{T}\big(\big\|M^{1/2}y^{B}(t)\big\|^{2}+\|u(t)\|^{2}\big)dt+\mathbb{E}\big\|G^{1/2}y^{B}(T)\big\|^{2}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​∫0T(‖M1/2​y†​(t)‖2+‖u​(t)‖2)​𝑑t+𝔼​‖G1/2​y†​(T)‖2.\displaystyle\mathbb{E}\int\_{0}^{T}\big(\big\|M^{1/2}y^{\dagger}(t)\big\|^{2}+\|u(t)\|^{2}\big)dt+\mathbb{E}\big\|G^{1/2}y^{\dagger}(T)\big\|^{2}. |  |

Let S†∈ℒ​(H)S^{\dagger}\in\mathcal{L}(H) be the semigroup corresponding to the infinite generator A†A^{\dagger}. The mild solutions of ([A.48](https://arxiv.org/html/2510.20017v1#A1.E48 "Equation A.48 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) for BB and B†B^{\dagger} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | yB​(t)=S†​(t)​ξ+∫0tS†​(t−r)​B​u​(r)​𝑑r+∫0tS†​(t−r)​(D​yB​(r)+E​u​(r))​𝑑W​(r),y†​(t)=S†​(t)​ξ+∫0tS†​(t−r)​B†​u​(r)​𝑑r+∫0tS†​(t−r)​(D​y†​(r)+E​u​(r))​𝑑W​(r),\displaystyle\begin{aligned} y^{B}(t)=&S^{\dagger}(t)\xi+\int\_{0}^{t}S^{\dagger}(t-r)Bu(r)dr+\int\_{0}^{t}S^{\dagger}(t-r)(Dy^{B}(r)+Eu(r))dW(r),\\ y^{\dagger}(t)=&S^{\dagger}(t)\xi+\int\_{0}^{t}S^{\dagger}(t-r)B^{\dagger}u(r)dr+\int\_{0}^{t}S^{\dagger}(t-r)(Dy^{\dagger}(r)+Eu(r))dW(r),\end{aligned} |  | (A.49) |

and satisfy

|  |  |  |
| --- | --- | --- |
|  | yB​(t)−y†​(t)=∫0tS†​(t−r)​(B−B†)​u​(r)​𝑑r+∫0tS†​(t−r)​D​(yB​(r)−y†​(r))​𝑑W​(r).y^{B}(t)-y^{\dagger}(t)=\int\_{0}^{t}S^{\dagger}(t-r)(B-B^{\dagger})u(r)dr+\int\_{0}^{t}S^{\dagger}(t-r)D(y^{B}(r)-y^{\dagger}(r))dW(r). |  |

By the Itô’s formula and Cauchy-Schwarz inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼∥yB​(t)−\displaystyle\mathbb{E}\|y^{B}(t)- | y†(t)∥2\displaystyle y^{\dagger}(t)\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​∫0t2​⟨yB​(r)−y†​(r),S†​(t−r)​(B−B†)​u​(r)⟩​𝑑r+𝔼​∫0t‖S†​(t−r)​D​(yB​(r)−y†​(r))‖2​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}2\langle y^{B}(r)-y^{\dagger}(r),S^{\dagger}(t-r)(B-B^{\dagger})u(r)\rangle dr+\mathbb{E}\int\_{0}^{t}\big\|S^{\dagger}(t-r)D(y^{B}(r)-y^{\dagger}(r))\big\|^{2}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 4​𝔼​∫0t‖yB​(r)−y†​(r)‖2+(MTA†)2​‖B−B†‖2​‖u​(r)‖2​d​r\displaystyle 4\mathbb{E}\int\_{0}^{t}\big\|y^{B}(r)-y^{\dagger}(r)\big\|^{2}+(M^{A^{\dagger}}\_{T})^{2}\|B-B^{\dagger}\|^{2}\|u(r)\|^{2}dr |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(MTA†)2​‖D‖2​𝔼​∫0t‖yB​(r)−y†​(r)‖2​𝑑r,\displaystyle+(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathbb{E}\int\_{0}^{t}\big\|y^{B}(r)-y^{\dagger}(r)\big\|^{2}dr, |  | (A.50) |

where MTA†M^{A^{\dagger}}\_{T} is the upper bound for S†S^{\dagger} such that ‖S†​(t)‖≤MTA†\|S^{\dagger}(t)\|\leq M^{A^{\dagger}}\_{T}, for all t∈𝒯t\in\mathcal{T}.

By ([A.49](https://arxiv.org/html/2510.20017v1#A1.E49 "Equation A.49 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and the inequality ‖a+b+c‖2≤3​(‖a‖2+‖b‖2+‖c‖2)\|a+b+c\|^{2}\leq 3(\|a\|^{2}+\|b\|^{2}+\|c\|^{2}),
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​|y†​(t)|2=\displaystyle\mathbb{E}|y^{\dagger}(t)|^{2}= | 3​(MTA†)2​‖ξ‖2+3​𝔼​‖∫0tS†​(t−r)​B†​u​(r)​𝑑r‖2+3​𝔼​‖∫0tS†​(t−r)​(D​y†​(r)+E​u​(r))​𝑑W​(r)‖2\displaystyle 3(M^{A^{\dagger}}\_{T})^{2}\|\xi\|^{2}+3\mathbb{E}\Big\|\int\_{0}^{t}S^{\dagger}(t-r)B^{\dagger}u(r)dr\Big\|^{2}+3\mathbb{E}\Big\|\int\_{0}^{t}S^{\dagger}(t-r)(Dy^{\dagger}(r)+Eu(r))dW(r)\Big\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 3​(MTA†)2​‖ξ‖2+3​(MTA†)2​𝔼​∫0t‖B†‖​‖u​(r)‖​𝑑r\displaystyle 3(M^{A^{\dagger}}\_{T})^{2}\|\xi\|^{2}+3(M^{A^{\dagger}}\_{T})^{2}\mathbb{E}\int\_{0}^{t}\|B^{\dagger}\|\|u(r)\|dr |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +3​(MTA†)2​𝔼​∫0t2​(‖D‖2​‖y†​(r)‖2+‖E‖2​‖u​(r)‖2)​𝑑r.\displaystyle+3(M^{A^{\dagger}}\_{T})^{2}\mathbb{E}\int\_{0}^{t}2\big(\|D\|^{2}\|y^{\dagger}(r)\|^{2}+\|E\|^{2}\|u(r)\|^{2}\big)dr. |  | (A.51) |

From ([A.50](https://arxiv.org/html/2510.20017v1#A1.E50 "Equation A.50 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.51](https://arxiv.org/html/2510.20017v1#A1.E51 "Equation A.51 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) with ‖u​(t)‖=1\|u(t)\|=1, for all t∈𝒯t\in\mathcal{T}, we have by the Grönwall’s inequality that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖yB​(t)−y†​(t)‖2≤4​T​(MTA†)2​‖B−B†‖2​exp⁡{(4+(MTA†)2​‖D‖2)​T},\displaystyle\mathbb{E}\|y^{B}(t)-y^{\dagger}(t)\|^{2}\leq 4T(M^{A^{\dagger}}\_{T})^{2}\big\|B-B^{\dagger}\big\|^{2}\exp\big\{\big(4+(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\big)T\big\}, |  | (A.52) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖y†​(t)‖2≤3​(MTA†)2​[‖ξ‖2+(‖B†‖+2​‖E‖2)​T]​exp⁡{6​(MTA†)2​‖D‖2​T}.\displaystyle\mathbb{E}\|y^{\dagger}(t)\|^{2}\leq 3(M^{A^{\dagger}}\_{T})^{2}\big[\|\xi\|^{2}+(\|B^{\dagger}\|+2\|E\|^{2})T\big]\exp\big\{6(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}T\big\}. |  | (A.53) |

By the proof of [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3], we have for any u​(t)u(t), t∈𝒯t\in\mathcal{T}, that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Π†​(t)​ξ,ξ⟩=\displaystyle\langle\Pi^{\dagger}(t)\xi,\xi\rangle= | 𝔼​∫0t(‖M1/2​y†​(r)‖2+‖u​(r)‖2)​𝑑r+𝔼​‖G1/2​y†​(t)‖2\displaystyle\mathbb{E}\int\_{0}^{t}\big(\big\|M^{1/2}y^{\dagger}(r)\big\|^{2}+\|u(r)\|^{2}\big)dr+\mathbb{E}\big\|G^{1/2}y^{\dagger}(t)\big\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​∫0t‖u​(r)+(K†)−1​L†​(T−r)​y†​(r)‖2​𝑑r,\displaystyle-\mathbb{E}\int\_{0}^{t}\big\|u(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\|^{2}dr, |  |

and furthermore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(ΠB\displaystyle\langle(\Pi^{B} | (t)−Π†(t))ξ,ξ⟩\displaystyle(t)-\Pi^{\dagger}(t))\xi,\xi\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​∫0t‖M1/2​yB​(r)‖2−‖M1/2​y†​(r)‖2​d​r+𝔼​(‖G1/2​yB​(t)‖2−‖G1/2​y†​(t)‖2)\displaystyle\mathbb{E}\int\_{0}^{t}\big\|M^{1/2}y^{B}(r)\big\|^{2}-\big\|M^{1/2}y^{\dagger}(r)\big\|^{2}dr+\mathbb{E}\big(\big\|G^{1/2}y^{B}(t)\big\|^{2}-\big\|G^{1/2}y^{\dagger}(t)\big\|^{2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​∫0t(‖u​(r)+(KB)−1​LB​(T−r)​yB​(r)‖2−‖u​(r)+(K†)−1​L†​(T−r)​y†​(r)‖2)​𝑑r\displaystyle-\mathbb{E}\int\_{0}^{t}\big(\big\|u(r)+(K^{B})^{-1}L^{B}(T-r)y^{B}(r)\big\|^{2}-\big\|u(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\|^{2}\big)dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​∫0t⟨M1/2​(yB​(r)−y†​(r)),M1/2​(yB​(r)+y†​(r))⟩​𝑑r\displaystyle\mathbb{E}\int\_{0}^{t}\langle M^{1/2}(y^{B}(r)-y^{\dagger}(r)),M^{1/2}(y^{B}(r)+y^{\dagger}(r))\rangle dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​⟨G1/2​(yB​(t)−y†​(t)),G1/2​(yB​(t)+y†​(t))⟩\displaystyle\hskip 56.9055pt+\mathbb{E}\langle G^{1/2}(y^{B}(t)-y^{\dagger}(t)),G^{1/2}(y^{B}(t)+y^{\dagger}(t))\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼∫0t⟨(KB)−1LB(T−r)yB(r)−(K†)−1L†(T−r)y†(r),\displaystyle-\mathbb{E}\int\_{0}^{t}\bigl\langle(K^{B})^{-1}L^{B}(T-r)y^{B}(r)-(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (KB)−1LB(T−r)yB(r)+(K†)−1L†(T−r)y†(r)+2u(r)⟩dr.\displaystyle\hskip 56.9055pt(K^{B})^{-1}L^{B}(T-r)y^{B}(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)+2u(r)\bigr\rangle dr. |  | (A.54) |

We take ‖u​(t)‖=1\|u(t)\|=1, for all t∈𝒯t\in\mathcal{T},
and let yy and y†y^{\dagger} be the states corresponding to the u​(t)u(t), t∈𝒯t\in\mathcal{T}.
By the Cauchy-Schwarz inequality, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(ΠB(t)\displaystyle\langle(\Pi^{B}(t) | −Π†(t))ξ,ξ⟩\displaystyle-\Pi^{\dagger}(t))\xi,\xi\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​∫0t‖M‖​‖yB​(r)−y†​(r)‖​‖yB​(r)+y†​(r)‖​𝑑r+‖G‖​‖yB​(T)−y†​(T)‖​‖yB​(T)+y†​(T)‖\displaystyle\mathbb{E}\int\_{0}^{t}\|M\|\big\|y^{B}(r)-y^{\dagger}(r)\big\|\big\|y^{B}(r)+y^{\dagger}(r)\big\|dr+\|G\|\big\|y^{B}(T)-y^{\dagger}(T)\big\|\big\|y^{B}(T)+y^{\dagger}(T)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​∫0t‖(KB)−1​LB​(T−r)​yB​(r)−(K†)−1​L†​(T−r)​y†​(r)‖\displaystyle+\mathbb{E}\int\_{0}^{t}\big\|(K^{B})^{-1}L^{B}(T-r)y^{B}(r)-(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×(‖(KB)−1​LB​(T−r)​yB​(r)+(K†)−1​L†​(T−r)​y†​(r)‖+2)​d​r.\displaystyle\times\big(\big\|(K^{B})^{-1}L^{B}(T-r)y^{B}(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\|+2\big)dr. |  | (A.55) |

By [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3], we have the following estimate of Π†\Pi^{\dagger}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Π†​(t)‖≤CΠ†,∀t∈𝒯,\displaystyle\|\Pi^{\dagger}(t)\|\leq C^{\Pi^{\dagger}},\quad\forall t\in\mathcal{T}, |  | (A.56) |
|  |  |  |
| --- | --- | --- |
|  | CΠ†=2​(MTA†)2​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))​(‖G‖+T​‖M‖).\displaystyle C^{\Pi^{\dagger}}=2(M\_{T}^{A^{\dagger}})^{2}\exp\big(8T(M\_{T}^{A^{\dagger}})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big(\|G\|+T\|M\|\big). |  |

By the estimates for Δ1\Delta\_{1} and Δ2\Delta\_{2} in [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Theorem 4.1], the estimate for Π†\Pi^{\dagger} in [Liu and Firoozi, [2025](https://arxiv.org/html/2510.20017v1#bib.bib14), Proposition 4.3], and the bounds ‖(KB)−1​(t)‖≤1\|(K^{B})^{-1}(t)\|\leq 1 and ‖(K†)−1​(t)‖≤1\|(K^{\dagger})^{-1}(t)\|\leq 1, ∀t∈𝒯\forall t\in\mathcal{T}, we have

|  |  |  |
| --- | --- | --- |
|  | ‖L†​(t)‖=‖(B†)⋆​Π†​(t)+Δ1​(Π†​(t))‖\displaystyle\big\|L^{\dagger}(t)\big\|=\big\|(B^{\dagger})^{\star}\Pi^{\dagger}(t)+\Delta\_{1}(\Pi^{\dagger}(t))\big\| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(‖B†‖+‖Δ1‖)​‖Π†​(t)‖≤(‖B†‖+R3)​CΠ†,\displaystyle\hskip 42.67912pt\leq\big(\|B^{\dagger}\|+\|\Delta\_{1}\|\big)\big\|\Pi^{\dagger}(t)\big\|\leq\big(\|B^{\dagger}\|+R\_{3}\big)C^{\Pi^{\dagger}}, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖(K†)−1​(t)‖=‖(I+Δ3​(Π†​(t)))−1‖≤1,\displaystyle\|(K^{\dagger})^{-1}(t)\|=\big\|(I+\Delta\_{3}(\Pi^{\dagger}(t)))^{-1}\big\|\leq 1, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖LB​(t)−L†​(t)‖=‖B⋆​ΠB​(t)−(B†)⋆​Π†​(t)+Δ1​(ΠB​(t)−Π†​(t))‖\displaystyle\big\|L^{B}(t)-L^{\dagger}(t)\big\|=\big\|B^{\star}\Pi^{B}(t)-(B^{\dagger})^{\star}\Pi^{\dagger}(t)+\Delta\_{1}(\Pi^{B}(t)-\Pi^{\dagger}(t))\big\| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤CΠ†​‖B−B†‖+(‖B†‖+R3)​‖ΠB​(t)−Π†​(t)‖,\displaystyle\hskip 68.28644pt\leq C^{\Pi^{\dagger}}\|B-B^{\dagger}\|+(\|B^{\dagger}\|+R\_{3})\big\|\Pi^{B}(t)-\Pi^{\dagger}(t)\big\|, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖KB​(t)−K†​(t)‖=‖Δ3​(ΠB​(t)−Π†​(t))‖≤R5​‖ΠB​(t)−Π†​(t)‖,\displaystyle\|K^{B}(t)-K^{\dagger}(t)\|=\|\Delta\_{3}(\Pi^{B}(t)-\Pi^{\dagger}(t))\|\leq R\_{5}\big\|\Pi^{B}(t)-\Pi^{\dagger}(t)\big\|, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(KB)−1\displaystyle\big\|(K^{B})^{-1} | LB(t)−(K†)−1L†(t)∥\displaystyle L^{B}(t)-(K^{\dagger})^{-1}L^{\dagger}(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ‖(KB)−1​(LB−L†)​(t)+((KB)−1−(K†)−1)​L†​(t)‖\displaystyle\big\|(K^{B})^{-1}\big(L^{B}-L^{\dagger}\big)(t)+\big((K^{B})^{-1}-(K^{\dagger})^{-1}\big)L^{\dagger}(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖(KB)−1​(t)‖​‖(LB−L†)​(t)‖+‖(KB)−1​(t)‖​‖(K†−KB)​(t)‖​‖(K†)−1​(t)‖​‖L†​(t)‖\displaystyle\big\|(K^{B})^{-1}(t)\big\|\big\|\big(L^{B}-L^{\dagger}\big)(t)\big\|+\big\|(K^{B})^{-1}(t)\big\|\big\|(K^{\dagger}-K^{B})(t)\big\|\big\|(K^{\dagger})^{-1}(t)\big\|\big\|L^{\dagger}(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CΠ†​‖B−B†‖+(‖B†‖+R3+R5)​‖ΠB​(t)−Π†​(t)‖.\displaystyle C^{\Pi^{\dagger}}\|B-B^{\dagger}\|+(\|B^{\dagger}\|+R\_{3}+R\_{5})\big\|\Pi^{B}(t)-\Pi^{\dagger}(t)\big\|. |  |

Then we have the estimates

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(KB)−1\displaystyle\big\|(K^{B})^{-1} | LB(T−r)yB(r)−(K†)−1L†(T−r)y†(r)∥\displaystyle L^{B}(T-r)y^{B}(r)-(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖(KB)−1‖​‖LB​(T−r)‖​‖yB​(r)−y†​(r)‖+‖(KB)−1​LB​(t−r)−(K†)−1​L†​(t−r)‖​‖y†​(r)‖\displaystyle\big\|(K^{B})^{-1}\big\|\big\|L^{B}(T-r)\big\|\big\|y^{B}(r)-y^{\dagger}(r)\big\|+\big\|(K^{B})^{-1}L^{B}(t-r)-(K^{\dagger})^{-1}L^{\dagger}(t-r)\big\|\big\|y^{\dagger}(r)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (‖B‖+R3)​CΠ†​‖yB​(r)−y†​(r)‖\displaystyle(\|B\|+R\_{3})C^{\Pi^{\dagger}}\big\|y^{B}(r)-y^{\dagger}(r)\big\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +{CΠ†​‖B−B†‖+(‖B†‖+R3+R5)​‖(ΠB−Π†)​(t)‖}​‖y†​(r)‖\displaystyle+\big\{C^{\Pi^{\dagger}}\|B-B^{\dagger}\|+(\|B^{\dagger}\|+R\_{3}+R\_{5})\big\|(\Pi^{B}-\Pi^{\dagger})(t)\big\|\big\}\big\|y^{\dagger}(r)\big\| |  | (A.57) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(KB)−1\displaystyle\big\|(K^{B})^{-1} | LB(T−r)yB(r)+(K†)−1L†(T−r)y†(r)∥\displaystyle L^{B}(T-r)y^{B}(r)+(K^{\dagger})^{-1}L^{\dagger}(T-r)y^{\dagger}(r)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖(KB)−1‖​‖LB​(T−r)‖​‖yB​(r)‖+‖(K†)−1‖​‖L†​(T−r)‖​‖y†​(r)‖\displaystyle\big\|(K^{B})^{-1}\big\|\big\|L^{B}(T-r)\big\|\|y^{B}(r)\|+\big\|(K^{\dagger})^{-1}\big\|\big\|L^{\dagger}(T-r)\big\|\big\|y^{\dagger}(r)\big\| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | [‖B‖​‖yB​(r)‖+‖B†‖​‖y†​(r)‖+R3​(‖yB​(r)‖+‖y†​(r)‖)]​CΠ†.\displaystyle\big[\|B\|\|y^{B}(r)\|+\|B^{\dagger}\|\|y^{\dagger}(r)\|+R\_{3}(\|y^{B}(r)\|+\|y^{\dagger}(r)\|)\big]C^{\Pi^{\dagger}}. |  | (A.58) |

By ([A.55](https://arxiv.org/html/2510.20017v1#A1.E55 "Equation A.55 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")),
([A.57](https://arxiv.org/html/2510.20017v1#A1.E57 "Equation A.57 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")),
([A.58](https://arxiv.org/html/2510.20017v1#A1.E58 "Equation A.58 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), and the Cauchy-Schwarz inequality,
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1‖ξ‖2\displaystyle\frac{1}{\|\xi\|^{2}} | ⟨(ΠB−Π†)​(t)​ξ,ξ⟩\displaystyle\langle(\Pi^{B}-\Pi^{\dagger})(t)\xi,\xi\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1‖ξ‖2​(‖M‖​T+‖G‖)​[supr∈𝒯𝔼​‖yB​(r)−y†​(r)‖2]1/2​[supr∈𝒯𝔼​‖yB​(r)+y†​(r)‖2]1/2\displaystyle\frac{1}{\|\xi\|^{2}}(\|M\|T+\|G\|)\big[\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{B}(r)-y^{\dagger}(r)\|^{2}\big]^{1/2}\big[\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{B}(r)+y^{\dagger}(r)\|^{2}\big]^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1‖ξ‖2​[(‖B‖+‖B†‖+2​R3)​CΠ†​(supr∈𝒯𝔼​‖yB​(r)‖2)1/2+2]\displaystyle+\frac{1}{\|\xi\|^{2}}\big[(\|B\|+\|B^{\dagger}\|+2R\_{3})C^{\Pi^{\dagger}}(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{B}(r)\|^{2})^{1/2}+2\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×∫0t(∥B∥+R3)CΠ†(supr∈𝒯∥yB(r)−y†(r)∥2)1/2\displaystyle\times\int\_{0}^{t}(\|B\|+R\_{3})C^{\Pi^{\dagger}}(\sup\_{r\in\mathcal{T}}\|y^{B}(r)-y^{\dagger}(r)\|^{2})^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +{CΠ†​‖B−B†‖+(‖B†‖+R3+R5)​‖ΠB​(r)−Π†​(r)‖}​{supr∈𝒯(𝔼​‖y†​(r)‖2)1/2}​d​r.\displaystyle+\big\{C^{\Pi^{\dagger}}\|B-B^{\dagger}\|+(\|B^{\dagger}\|+R\_{3}+R\_{5})\big\|\Pi^{B}(r)-\Pi^{\dagger}(r)\big\|\big\}\big\{\sup\_{r\in\mathcal{T}}(\mathbb{E}\|y^{\dagger}(r)\|^{2})^{1/2}\big\}dr. |  |

It then follows from the Grönwall’s inequality that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥(ΠB\displaystyle\big\|(\Pi^{B} | −Π†)(t)∥\displaystyle-\Pi^{\dagger})(t)\big\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1‖ξ‖2{(∥M∥T+∥G∥)[supr∈𝒯𝔼∥yB(r)−y†(r)∥2]1/22[supr∈𝒯𝔼∥yB(r)∥2]1/2\displaystyle\frac{1}{\|\xi\|^{2}}\Big\{(\|M\|T+\|G\|)\big[\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{B}(r)-y^{\dagger}(r)\|^{2}\big]^{1/2}2\big[\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{B}(r)\|^{2}\big]^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(‖B‖+‖B†‖+2​R3)​CΠ†​(supt∈𝒯𝔼​‖y†​(t)‖2)1/2​(supt∈𝒯𝔼​‖yB​(t)−y†​(t)‖2)1/2\displaystyle+(\|B\|+\|B^{\dagger}\|+2R\_{3})C^{\Pi^{\dagger}}(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|y^{\dagger}(t)\big\|^{2})^{1/2}(\sup\_{t\in\mathcal{T}}\mathbb{E}\big\|y^{B}(t)-y^{\dagger}(t)\big\|^{2})^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×T(∥B†∥+R3)(CΠ†)2∥B−B†∥}exp{(∥B†∥+R3+R5)T(supt∈𝒯𝔼∥y†(t)∥2)1/2}\displaystyle\times T(\|B^{\dagger}\|+R\_{3})(C^{\Pi^{\dagger}})^{2}\|B-B^{\dagger}\|\Big\}\exp\Big\{(\|B^{\dagger}\|+R\_{3}+R\_{5})T(\sup\_{t\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(t)\|^{2})^{1/2}\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1‖ξ‖2(supr∈𝒯𝔼∥yB(r)−y†(r)∥2)1/2(supr∈𝒯𝔼|yB(r)|2)1/2{2(∥M∥T+∥G∥)\displaystyle\frac{1}{\|\xi\|^{2}}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}\|y^{B}(r)-y^{\dagger}(r)\|^{2}\big)^{1/2}\big(\sup\_{r\in\mathcal{T}}\mathbb{E}|y^{B}(r)|^{2}\big)^{1/2}\Big\{2(\|M\|T+\|G\|) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(∥B∥+∥B†∥+2R3)T(∥B∥+R3)(CΠ†)3∥B−B†∥}\displaystyle+(\|B\|+\|B^{\dagger}\|+2R\_{3})T(\|B\|+R\_{3})(C^{\Pi^{\dagger}})^{3}\|B-B^{\dagger}\|\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡{(‖B†‖+R3+R5)​T​(supt∈𝒯𝔼​‖y†​(t)‖2)1/2}.\displaystyle\times\exp\Big\{(\|B^{\dagger}\|+R\_{3}+R\_{5})T(\sup\_{t\in\mathcal{T}}\mathbb{E}\|y^{\dagger}(t)\|^{2})^{1/2}\Big\}. |  |

By ([A.52](https://arxiv.org/html/2510.20017v1#A1.E52 "Equation A.52 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.53](https://arxiv.org/html/2510.20017v1#A1.E53 "Equation A.53 ‣ A.5.1 Proofs of Lemma 4.8 ‣ A.5 Proof of Lipschitz Stability with respect to 𝐵 ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(ΠB−Π†)​(t)‖≤\displaystyle\big\|(\Pi^{B}-\Pi^{\dagger})(t)\big\|\leq | T​‖B−B†‖​exp⁡{12​(MTA†)2​(1+‖D‖2)​T}​2​MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))\displaystyle\sqrt{T}\big\|B-B^{\dagger}\big\|\exp\Big\{\frac{1}{2}(M\_{T}^{A^{\dagger}})^{2}(1+\|D\|^{2})T\Big\}\sqrt{2}M^{A^{\dagger}}\_{T}\exp\big(8T(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×{2​(‖M‖​T+‖G‖)+(‖B‖+‖B†‖+2​R3)​T​(‖B‖+R3)​(CΠ†)3​‖B−B†‖}\displaystyle\times\Big\{2(\|M\|T+\|G\|)+(\|B\|+\|B^{\dagger}\|+2R\_{3})T(\|B\|+R\_{3})(C^{\Pi^{\dagger}})^{3}\|B-B^{\dagger}\|\Big\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×exp⁡{(‖B†‖+R3+R5)​T​[2​MTA†​exp⁡(8​T​(MTA†)2​‖D‖2​tr​(Q))]}.\displaystyle\times\exp\Big\{(\|B^{\dagger}\|+R\_{3}+R\_{5})T\big[\sqrt{2}M^{A^{\dagger}}\_{T}\exp\big(8T(M^{A^{\dagger}}\_{T})^{2}\|D\|^{2}\mathrm{tr}(Q)\big)\big]\Big\}. |  | (A.59) |

∎

#### A.5.2 Proof of Lemma [4.9](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem9 "Lemma 4.9. ‣ 4.2 Stability of the equilibrium with respect to operator 𝐵 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

From ([A.23](https://arxiv.org/html/2510.20017v1#A1.E23 "Equation A.23 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.24](https://arxiv.org/html/2510.20017v1#A1.E24 "Equation A.24 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ‖(x¯B−x¯†)​(t)‖≤∫0t‖S†​(t−r)‖​‖ΦB​(r)−Φ†​(r)‖​𝑑r,\displaystyle\big\|(\bar{x}^{B}-\bar{x}^{\dagger})(t)\big\|\leq\int\_{0}^{t}\big\|S^{\dagger}(t-r)\big\|\big\|\Phi^{B}(r)-\Phi^{\dagger}(r)\big\|dr, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(q−q†)​(t)‖\displaystyle\|(q-q^{\dagger})(t)\| | ≤‖S​(t)‖​‖(x¯−x¯†)​(T)‖​‖G‖​‖F^2‖+∫0t‖S​(t−r)‖​‖(Ψ−Ψ†)​(r)‖​𝑑r.\displaystyle\leq\|S(t)\|\|(\bar{x}-\bar{x}^{\dagger})(T)\|\|G\|\|\widehat{F}\_{2}\|+\int\_{0}^{t}\|S(t-r)\|\|(\Psi-\Psi^{\dagger})(r)\|dr. |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ΦB​(r)−Φ†​(r)‖≤\displaystyle\big\|\Phi^{B}(r)-\Phi^{\dagger}(r)\big\|\leq | CB,B†Φ,x¯​‖(x¯B−x¯†)​(r)‖+CB,B†Φ,q​‖(qB−q†)​(T−r)‖\displaystyle C^{\Phi,\bar{x}}\_{B,B^{\dagger}}\|(\bar{x}^{B}-\bar{x}^{\dagger})(r)\|+C^{\Phi,q}\_{B,B^{\dagger}}\|(q^{B}-q^{\dagger})(T-r)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CB,B†Φ,Π​‖(ΠB−Π†)​(T−r)‖+CB,B†Φ,c​‖B−B†‖,\displaystyle+C^{\Phi,\Pi}\_{B,B^{\dagger}}\|(\Pi^{B}-\Pi^{\dagger})(T-r)\|+C^{\Phi,c}\_{B,B^{\dagger}}\|B-B^{\dagger}\|, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ΨB​(r)−Ψ†​(r)‖≤\displaystyle\big\|\Psi^{B}(r)-\Psi^{\dagger}(r)\big\|\leq | CB,B†Ψ,x¯​‖(x¯B−x¯†)​(T−r)‖+CB,B†Ψ,q​‖(qB−q†)​(r)‖\displaystyle C^{\Psi,\bar{x}}\_{B,B^{\dagger}}\|(\bar{x}^{B}-\bar{x}^{\dagger})(T-r)\|+C^{\Psi,q}\_{B,B^{\dagger}}\|(q^{B}-q^{\dagger})(r)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CB,B†Ψ,Π​‖(ΠB−Π†)​(r)‖+CB,B†Ψ,c​‖B−B†‖,\displaystyle+C^{\Psi,\Pi}\_{B,B^{\dagger}}\|(\Pi^{B}-\Pi^{\dagger})(r)\|+C^{\Psi,c}\_{B,B^{\dagger}}\|B-B^{\dagger}\|, |  |

where the constants CB,B†Φ,x¯C^{\Phi,\bar{x}}\_{B,B^{\dagger}}, CB,B†Φ,qC^{\Phi,q}\_{B,B^{\dagger}}, CB,B†Φ,ΠC^{\Phi,\Pi}\_{B,B^{\dagger}},
CB,B†Ψ,x¯C^{\Psi,\bar{x}}\_{B,B^{\dagger}}, CB,B†Ψ,qC^{\Psi,q}\_{B,B^{\dagger}}, and CB,B†Ψ,ΠC^{\Psi,\Pi}\_{B,B^{\dagger}} are defined in the statement of the lemma, it then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(x¯B−x¯†)​(t)‖≤\displaystyle\big\|(\bar{x}^{B}-\bar{x}^{\dagger})(t)\big\|\leq | ∫0tMTA†[CB,B†Φ,x¯∥(x¯B−x¯†)(r)∥+CB,B†Φ,q∥(qB−q†)(T−r)∥\displaystyle\int\_{0}^{t}M^{A^{\dagger}}\_{T}\big[C^{\Phi,\bar{x}}\_{B,B^{\dagger}}\|(\bar{x}^{B}-\bar{x}^{\dagger})(r)\|+C^{\Phi,q}\_{B,B^{\dagger}}\|(q^{B}-q^{\dagger})(T-r)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CB,B†Φ,Π∥(ΠB−Π†)(T−r)∥+CB,B†Φ,c∥B−B†∥]dr,\displaystyle\hskip 56.9055pt+C^{\Phi,\Pi}\_{B,B^{\dagger}}\|(\Pi^{B}-\Pi^{\dagger})(T-r)\|+C^{\Phi,c}\_{B,B^{\dagger}}\|B-B^{\dagger}\|\big]dr, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(qB−q†)​(t)‖≤\displaystyle\|(q^{B}-q^{\dagger})(t)\|\leq | MTA†​‖(x¯B−x¯†)​(T)‖​‖G‖​‖F^2‖\displaystyle M^{A^{\dagger}}\_{T}\|(\bar{x}^{B}-\bar{x}^{\dagger})(T)\|\|G\|\|\widehat{F}\_{2}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tMTA†[CB,B†Ψ,x¯∥(x¯B−x¯†)(T−r)∥+CB,B†Ψ,q∥(qB−q†)(r)∥\displaystyle+\int\_{0}^{t}M^{A^{\dagger}}\_{T}\big[C^{\Psi,\bar{x}}\_{B,B^{\dagger}}\|(\bar{x}^{B}-\bar{x}^{\dagger})(T-r)\|+C^{\Psi,q}\_{B,B^{\dagger}}\|(q^{B}-q^{\dagger})(r)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CB,B†Ψ,Π∥(ΠB−Π†)(r)∥+CB,B†Ψ,c∥B−B†∥]dr.\displaystyle\hskip 56.9055pt+C^{\Psi,\Pi}\_{B,B^{\dagger}}\|(\Pi^{B}-\Pi^{\dagger})(r)\|+C^{\Psi,c}\_{B,B^{\dagger}}\|B-B^{\dagger}\|\big]dr. |  |

Applying Lemma [A.2](https://arxiv.org/html/2510.20017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") to the above two inequalities, we obtain
the desired estimates for
‖x¯B−x¯†‖C​(𝒯;H)\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}
and
‖qB−q†‖C​(𝒯;H)\|q^{B}-q^{\dagger}\|\_{C(\mathcal{T};H)}.

∎

#### A.5.3 Proof of Lemma [4.10](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem10 "Lemma 4.10. ‣ 4.2 Stability of the equilibrium with respect to operator 𝐵 ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

The bound CBxC^{x}\_{B} for xBx^{B} follows from Lemma [4.2](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") with B†B^{\dagger} replaced by BB.

By ([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (xB−x†)​(t)≤\displaystyle(x^{B}-x^{\dagger})(t)\leq | ∫0tS†​(t−r)​(Ξ1B−Ξ1†)​(r)​𝑑r+∫0tS†​(t−r)​(Ξ2B−Ξ2†)​(r)​𝑑W​(r),\displaystyle\int\_{0}^{t}S^{\dagger}(t-r)(\Xi\_{1}^{B}-\Xi\_{1}^{\dagger})(r)dr+\int\_{0}^{t}S^{\dagger}(t-r)(\Xi\_{2}^{B}-\Xi\_{2}^{\dagger})(r)dW(r), |  |

where, for i=1,2i=1,2,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(ΞiB−Ξi†)​(t)‖2≤\displaystyle\mathbb{E}\|(\Xi\_{i}^{B}-\Xi\_{i}^{\dagger})(t)\|^{2}\leq | CB,B†Ξi,x​𝔼​‖(xB−x†)​(t)‖2+CB,B†Ξi,Π​‖(ΠB−Π†)​(t)‖2\displaystyle C^{\Xi\_{i},x}\_{B,B^{\dagger}}\mathbb{E}\|(x^{B}-x^{\dagger})(t)\|^{2}+C^{\Xi\_{i},\Pi}\_{B,B^{\dagger}}\|(\Pi^{B}-\Pi^{\dagger})(t)\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CB,B†Ξi,x¯​‖x¯B−x¯†‖C​(𝒯;H)2+CB,B†Ξi,q​‖qB−q†‖C​(𝒯;H)2+CB,B†Ξi,c​‖B−B†‖2.\displaystyle+C^{\Xi\_{i},\bar{x}}\_{B,B^{\dagger}}\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+C^{\Xi\_{i},q}\_{B,B^{\dagger}}\|q^{B}-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+C^{\Xi\_{i},c}\_{B,B^{\dagger}}\|B-B^{\dagger}\|^{2}. |  |

It then follows from the Cauchy-Schwarz inequality that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(xB−x†)​(t)‖2≤\displaystyle\mathbb{E}\|(x^{B}-x^{\dagger})(t)\|^{2}\leq | ∫0t‖S†​(t−r)‖2​{𝔼​‖(Ξ1B−Ξ1†)​(r)‖2+𝔼​‖(Ξ2B−Ξ2†)​(r)‖2}​𝑑r\displaystyle\int\_{0}^{t}\|S^{\dagger}(t-r)\|^{2}\big\{\mathbb{E}\|(\Xi\_{1}^{B}-\Xi\_{1}^{\dagger})(r)\|^{2}+\mathbb{E}\|(\Xi\_{2}^{B}-\Xi\_{2}^{\dagger})(r)\|^{2}\big\}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (MTA†)2​∫0t(CB,B†Ξ1,x+CB,B†Ξ2,x)​𝔼​‖(xB−x†)​(r)‖2​𝑑r\displaystyle(M^{A^{\dagger}}\_{T})^{2}\int\_{0}^{t}(C^{\Xi\_{1},x}\_{B,B^{\dagger}}+C^{\Xi\_{2},x}\_{B,B^{\dagger}})\mathbb{E}\|(x^{B}-x^{\dagger})(r)\|^{2}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +T(MTA†)2[(CB,B†Ξ1,x¯+CB,B†Ξ2,x¯)∥x¯B−x¯†∥C​(𝒯;H)2\displaystyle+T(M^{A^{\dagger}}\_{T})^{2}\Big[\big(C^{\Xi\_{1},\bar{x}}\_{B,B^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{B,B^{\dagger}}\big)\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(CB,B†Ξ1,q+CB,B†Ξ2,q)∥qB−q†∥C​(𝒯;H)2+(CB,B†Ξ1,c+CB,B†Ξ2,c)∥B−B†∥2].\displaystyle+\big(C^{\Xi\_{1},q}\_{B,B^{\dagger}}+C^{\Xi\_{2},q}\_{B,B^{\dagger}}\big)\|q^{B}-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+\big(C^{\Xi\_{1},c}\_{B,B^{\dagger}}+C^{\Xi\_{2},c}\_{B,B^{\dagger}}\big)\|B-B^{\dagger}\|^{2}\Big]. |  |

By the Grönwall’s inequality, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(xB−x†)​(t)‖2≤\displaystyle\mathbb{E}\|(x^{B}-x^{\dagger})(t)\|^{2}\leq | T(MTA†)2[(CB,B†Ξ1,x¯+CB,B†Ξ2,x¯)∥x¯B−x¯†∥C​(𝒯;H)2+(CB,B†Ξ1,q+CB,B†Ξ2,q)∥qB−q†∥C​(𝒯;H)2\displaystyle T(M^{A^{\dagger}}\_{T})^{2}\Big[\big(C^{\Xi\_{1},\bar{x}}\_{B,B^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{B,B^{\dagger}}\big)\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+\big(C^{\Xi\_{1},q}\_{B,B^{\dagger}}+C^{\Xi\_{2},q}\_{B,B^{\dagger}}\big)\|q^{B}-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(CB,B†Ξ1,c+CB,B†Ξ2,c)∥B−B†∥2]exp{T(MTA†)2(CB,B†Ξ1,x+CB,B†Ξ2,x)},\displaystyle\hskip 0.0pt+\big(C^{\Xi\_{1},c}\_{B,B^{\dagger}}+C^{\Xi\_{2},c}\_{B,B^{\dagger}}\big)\|B-B^{\dagger}\|^{2}\Big]\exp\Big\{T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{B,B^{\dagger}}+C^{\Xi\_{2},x}\_{B,B^{\dagger}})\Big\}, |  |

which further implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (supt∈𝒯𝔼∥\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\| | (xB−x†)(t)∥2)12\displaystyle(x^{B}-x^{\dagger})(t)\|^{2}\big)^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | T1/2MTA†3[(CB,B†Ξ1,x¯+CB,B†Ξ2,x¯)1/2∥x¯B−x¯†∥C​(𝒯;H)+(CB,B†Ξ1,q+CB,B†Ξ2,q)1/2∥qB−q†∥C​(𝒯;H)\displaystyle T^{1/2}M^{A^{\dagger}}\_{T}\sqrt{3}\Big[\big(C^{\Xi\_{1},\bar{x}}\_{B,B^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{B,B^{\dagger}}\big)^{1/2}\|\bar{x}^{B}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}+\big(C^{\Xi\_{1},q}\_{B,B^{\dagger}}+C^{\Xi\_{2},q}\_{B,B^{\dagger}}\big)^{1/2}\|q^{B}-q^{\dagger}\|\_{C(\mathcal{T};H)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(CB,B†Ξ1,c+CB,B†Ξ2,c)1/2∥B−B†∥]exp{T(MTA†)2(CB,B†Ξ1,x+CB,B†Ξ2,x)/2}.\displaystyle\hskip 0.0pt+\big(C^{\Xi\_{1},c}\_{B,B^{\dagger}}+C^{\Xi\_{2},c}\_{B,B^{\dagger}}\big)^{1/2}\|B-B^{\dagger}\|\Big]\exp\Big\{T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{B,B^{\dagger}}+C^{\Xi\_{2},x}\_{B,B^{\dagger}})/2\Big\}. |  |

The desired estimate then follows.
∎

### A.6 Proofs of Lipschitz Stability with respect to F2F\_{2}

#### A.6.1 Proof of Lemma [4.12](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem12 "Lemma 4.12. ‣ 4.3 Stability of the equilibrium with respect to operator 𝐹₂ ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

From ([A.23](https://arxiv.org/html/2510.20017v1#A1.E23 "Equation A.23 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and ([A.24](https://arxiv.org/html/2510.20017v1#A1.E24 "Equation A.24 ‣ A.3.1 Proof of Lemma 4.1 ‣ A.3 Proof of Regularity Results for the Reference MFG Model ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have that

|  |  |  |
| --- | --- | --- |
|  | ‖(x¯F2−x¯†)​(t)‖≤∫0t‖S†​(t−r)‖​‖ΦF2​(r)−Φ†​(r)‖​𝑑r,\displaystyle\big\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(t)\big\|\leq\int\_{0}^{t}\big\|S^{\dagger}(t-r)\big\|\big\|\Phi^{F\_{2}}(r)-\Phi^{\dagger}(r)\big\|dr, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖(qF2−q†)​(t)‖≤‖S†‖​‖(x¯F2−x¯†)​(T)‖​‖G‖​‖F^2‖+∫0t‖S†​(t−r)‖​‖(ΨF2−Ψ†)​(r)‖​𝑑r.\displaystyle\|(q^{F\_{2}}-q^{\dagger})(t)\|\leq\|S^{\dagger}\|\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(T)\|\|G\|\|\widehat{F}\_{2}\|+\int\_{0}^{t}\|S^{\dagger}(t-r)\|\|(\Psi^{F\_{2}}-\Psi^{\dagger})(r)\|dr. |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ΦF2−Φ†)​(r)=\displaystyle(\Phi^{F\_{2}}-\Phi^{\dagger})(r)= | (B†​(K†)−1​L†​(T−r)−F1)​(x¯F2−x¯†)​(r)+(B†)⋆​(qF2−q†)​(T−r)\displaystyle\big(B^{\dagger}(K^{\dagger})^{-1}L^{\dagger}(T-r)-F\_{1}\big)(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(r)+(B^{\dagger})^{\star}(q^{F\_{2}}-q^{\dagger})(T-r) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +B†​(K†)−1​(T−r)​Γ2​(((F2−F2†)​x¯F2+F2†​(x¯F2−x¯†))⋆​Π†​(T−r)),\displaystyle+B^{\dagger}(K^{\dagger})^{-1}(T-r)\Gamma\_{2}\big(((F\_{2}-F\_{2}^{\dagger})\bar{x}^{F\_{2}}+F\_{2}^{\dagger}(\bar{x}^{F\_{2}}-\bar{x}^{\dagger}))^{\star}\Pi^{\dagger}(T-r)\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (ΨF2−Ψ†)​(r)=\displaystyle(\Psi^{F\_{2}}-\Psi^{\dagger})(r)= | −(L†)⋆​(K†)−1​(r)​B⋆​(qF2−q†)​(r)\displaystyle-(L^{\dagger})^{\star}(K^{\dagger})^{-1}(r)B^{\star}(q^{F\_{2}}-q^{\dagger})(r) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Γ1​[((F2−F2†)​x¯F2+F2†​(x¯F2−x¯†))⋆​(T−r)​Π†​(r)]\displaystyle+\Gamma\_{1}\big[\big((F\_{2}-F\_{2}^{\dagger})\bar{x}^{F\_{2}}+F\_{2}^{\dagger}(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})\big)^{\star}(T-r)\Pi^{\dagger}(r)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(L†)⋆​(K†)−1​(r)​Γ2​[((F2−F2†)​x¯+F2†​(x¯F2−x¯†))⋆​(T−r)​Π†​(r)]\displaystyle-(L^{\dagger})^{\star}(K^{\dagger})^{-1}(r)\Gamma\_{2}\big[\big((F\_{2}-F\_{2}^{\dagger})\bar{x}+F\_{2}^{\dagger}(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})\big)^{\star}(T-r)\Pi^{\dagger}(r)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(Π†​(r)​F1−M​F^1)​(x¯F2−x¯†)​(T−r).\displaystyle+(\Pi^{\dagger}(r)F\_{1}-M\widehat{F}\_{1})(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(T-r). |  |

Since

|  |  |  |
| --- | --- | --- |
|  | ‖ΦF2​(r)−Φ†​(r)‖≤CF2,F2†Φ,x¯​‖(x¯F2−x¯†)​(r)‖+CF2,F2†Φ,q​‖(qF2−q†)​(T−r)‖+CF2,F2†Φ,c​‖F2−F2†‖,\displaystyle\big\|\Phi^{F\_{2}}(r)-\Phi^{\dagger}(r)\big\|\leq C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(r)\|+C^{\Phi,q}\_{F\_{2},F\_{2}^{\dagger}}\|(q^{F\_{2}}-q^{\dagger})(T-r)\|+C^{\Phi,c}\_{F\_{2},F\_{2}^{\dagger}}\|F\_{2}-F\_{2}^{\dagger}\|, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖ΨF2​(r)−Ψ†​(r)‖≤CF2,F2†Ψ,x¯​‖(x¯F2−x¯†)​(T−r)‖+CF2,F2†Ψ,q​‖(qF2−q†)​(r)‖+CF2,F2†Ψ,c​‖F2−F2†‖,\displaystyle\big\|\Psi^{F\_{2}}(r)-\Psi^{\dagger}(r)\big\|\leq C^{\Psi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(T-r)\|+C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}}\|(q^{F\_{2}}-q^{\dagger})(r)\|+C^{\Psi,c}\_{F\_{2},F\_{2}^{\dagger}}\|F\_{2}-F\_{2}^{\dagger}\|, |  |

where the constants CF2,F2†Φ,x¯C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}, CF2,F2†Φ,qC^{\Phi,q}\_{F\_{2},F\_{2}^{\dagger}}, CF2,F2†Φ,ΠC^{\Phi,\Pi}\_{F\_{2},F\_{2}^{\dagger}},
CF2,F2†Ψ,x¯C^{\Psi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}, CF2,F2†Ψ,qC^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}}, and CF2,F2†Ψ,ΠC^{\Psi,\Pi}\_{F\_{2},F\_{2}^{\dagger}} are given in the statement of the lemma, it then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(x¯F2−x¯†)​(t)‖≤\displaystyle\big\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(t)\big\|\leq | ∫0tMTA†​(CF2,F2†Φ,x¯​‖(x¯F2−x¯†)​(r)‖+CF2,F2†Φ,q​‖(qF2−q†)​(T−r)‖+CF2,F2†Φ,c​‖F2−F2†‖)​𝑑r,\displaystyle\int\_{0}^{t}\!\!M^{A^{\dagger}}\_{T}\big(C^{\Phi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(r)\|+C^{\Phi,q}\_{F\_{2},F\_{2}^{\dagger}}\|(q^{F\_{2}}-q^{\dagger})(T-r)\|+C^{\Phi,c}\_{F\_{2},F\_{2}^{\dagger}}\|F\_{2}-F\_{2}^{\dagger}\|\big)dr, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(qF2−q†)​(t)‖≤\displaystyle\big\|(q^{F\_{2}}-q^{\dagger})(t)\big\|\leq | MTA†​‖(x¯F2−x¯†)​(T)‖​‖G‖​‖F^2‖\displaystyle M^{A^{\dagger}}\_{T}\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(T)\|\|G\|\|\widehat{F}\_{2}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tMTA†​(CF2,F2†Ψ,q​‖(qF2−q†)​(r)‖+CF2,F2†Ψ,x¯​‖(x¯F2−x¯†)​(T−r)‖+CF2,F2†Ψ,c​‖F2−F2†‖)​𝑑r.\displaystyle\hskip-14.22636pt+\int\_{0}^{t}M^{A^{\dagger}}\_{T}\big(C^{\Psi,q}\_{F\_{2},F\_{2}^{\dagger}}\|(q^{F\_{2}}-q^{\dagger})(r)\|+C^{\Psi,\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\|(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(T-r)\|+C^{\Psi,c}\_{F\_{2},F\_{2}^{\dagger}}\|F\_{2}-F\_{2}^{\dagger}\|\big)dr. |  |

Applying Lemma [A.2](https://arxiv.org/html/2510.20017v1#A1.Thmtheorem2 "Lemma A.2. ‣ A.2 Estimates for continuous mappings ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") to the above two inequalities, we obtain
the desired estimates for
‖x¯F2−x¯†‖C​(𝒯;H)\|\bar{x}^{F\_{2}}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}
and
‖qF2−q†‖C​(𝒯;H)\|q^{F\_{2}}-q^{\dagger}\|\_{C(\mathcal{T};H)}.
∎

#### A.6.2 Proof of Lemma [4.13](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem13 "Lemma 4.13. ‣ 4.3 Stability of the equilibrium with respect to operator 𝐹₂ ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")

###### Proof.

The bound CF2xC^{x}\_{F\_{2}} for xF2x^{F\_{2}} follows from Lemma [4.2](https://arxiv.org/html/2510.20017v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4 Proofs of Stability Estimates ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators") with F2†F\_{2}^{\dagger} replaced by F2F\_{2}.

By ([A.10](https://arxiv.org/html/2510.20017v1#A1.E10 "Equation A.10 ‣ A.1 Mean Field Game Equilibrium Strategy ‣ Appendix A Additional Background ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), we have

|  |  |  |
| --- | --- | --- |
|  | (xF2−x†)​(t)≤∫0tS†​(t−r)​(Ξ1F2−Ξ1†)​(r)​𝑑r+∫0tS†​(t−r)​(Ξ2F2−Ξ2†)​(r)​𝑑W​(r).(x^{F\_{2}}-x^{\dagger})(t)\leq\int\_{0}^{t}S^{\dagger}(t-r)(\Xi\_{1}^{F\_{2}}-\Xi\_{1}^{\dagger})(r)dr+\int\_{0}^{t}S^{\dagger}(t-r)(\Xi\_{2}^{F\_{2}}-\Xi\_{2}^{\dagger})(r)dW(r). |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ξ1F2−Ξ1†)​(r)=\displaystyle(\Xi\_{1}^{F\_{2}}-\Xi\_{1}^{\dagger})(r)= | B†​(K†)−1​L†​(xF2−x†)​(r)+B†​(τF2−τ†)​(r)−F1​(x¯F2−x¯†),\displaystyle B^{\dagger}(K^{\dagger})^{-1}L^{\dagger}(x^{F\_{2}}-x^{\dagger})(r)+B^{\dagger}(\tau^{F\_{2}}-\tau^{\dagger})(r)-F\_{1}(\bar{x}^{F\_{2}}-\bar{x}^{\dagger}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ξ2F2−Ξ2†)​(r)=\displaystyle(\Xi\_{2}^{F\_{2}}-\Xi\_{2}^{\dagger})(r)= | F2​(x¯F2−x¯†)​(r)+[D−E​(K†)−1​L†​(T−r)]​(xF2−x†)​(r)−E​(τF2−τ†)​(r),\displaystyle F\_{2}(\bar{x}^{F\_{2}}-\bar{x}^{\dagger})(r)+[D-E(K^{\dagger})^{-1}L^{\dagger}(T-r)](x^{F\_{2}}-x^{\dagger})(r)-E(\tau^{F\_{2}}-\tau^{\dagger})(r), |  |

we have that for i=1,2i=1,2,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼∥\displaystyle\mathbb{E}\| | (ΞiF2−Ξi†)(t)∥2\displaystyle(\Xi\_{i}^{F\_{2}}-\Xi\_{i}^{\dagger})(t)\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CF2,F2†Ξi,x​𝔼​‖(xF2−x†)​(t)‖2+CF2,F2†Ξi,x¯​‖x¯F2−x¯†‖C​(𝒯;H)2+CF2,F2†Ξi,q​‖qF2−q†‖C​(𝒯;H)2+CF2,F2†Ξi,c​‖F2−F2†‖2\displaystyle C^{\Xi\_{i},x}\_{F\_{2},F\_{2}^{\dagger}}\mathbb{E}\|(x^{F\_{2}}-x^{\dagger})(t)\|^{2}+C^{\Xi\_{i},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}\|\bar{x}^{F\_{2}}-\bar{x}^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+C^{\Xi\_{i},q}\_{F\_{2},F\_{2}^{\dagger}}\|q^{F\_{2}}-q^{\dagger}\|\_{C(\mathcal{T};H)}^{2}+C^{\Xi\_{i},c}\_{F\_{2},F\_{2}^{\dagger}}\|F\_{2}-F\_{2}^{\dagger}\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CF2,F2†Ξi,x​𝔼​‖(xF2−x†)​(t)‖2+[CF2,F2†Ξi,x¯​CF2,F2†x¯+CF2,F2†Ξi,q​CF2,F2†q+CF2,F2†Ξi,c]​‖F2−F2†‖2.\displaystyle C^{\Xi\_{i},x}\_{F\_{2},F\_{2}^{\dagger}}\mathbb{E}\|(x^{F\_{2}}-x^{\dagger})(t)\|^{2}+\Big[C^{\Xi\_{i},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{i},q}\_{F\_{2},F\_{2}^{\dagger}}C^{q}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{i},c}\_{F\_{2},F\_{2}^{\dagger}}\Big]\|F\_{2}-F\_{2}^{\dagger}\|^{2}. |  |

It follows from the Cauchy-Schwartz inequality that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(xF2−x†)​(t)‖2≤\displaystyle\mathbb{E}\|(x^{F\_{2}}-x^{\dagger})(t)\|^{2}\leq | ∫0t‖S†​(t−r)‖2​{𝔼​‖(Ξ1F2−Ξ1†)​(r)‖2+𝔼​‖(Ξ2F2−Ξ2†)​(r)‖2}​𝑑r\displaystyle\int\_{0}^{t}\|S^{\dagger}(t-r)\|^{2}\big\{\mathbb{E}\|(\Xi\_{1}^{F\_{2}}-\Xi\_{1}^{\dagger})(r)\|^{2}+\mathbb{E}\|(\Xi\_{2}^{F\_{2}}-\Xi\_{2}^{\dagger})(r)\|^{2}\big\}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (MTA†)2∫0t(CF2,F2†Ξ1,x+CF2,F2†Ξ2,x)𝔼∥(x−x†)(r)∥2dr+T(MTA†)2[(CF2,F2†Ξ1,q\displaystyle(M^{A^{\dagger}}\_{T})^{2}\int\_{0}^{t}(C^{\Xi\_{1},x}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},x}\_{F\_{2},F\_{2}^{\dagger}})\mathbb{E}\|(x-x^{\dagger})(r)\|^{2}dr+T(M^{A^{\dagger}}\_{T})^{2}\Big[(C^{\Xi\_{1},q}\_{F\_{2},F\_{2}^{\dagger}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CF2,F2†Ξ2,q)CF2,F2†q+(CF2,F2†Ξ1,x¯+CF2,F2†Ξ2,x¯)CF2,F2†x¯+CF2,F2†Ξ1,c+CF2,F2†Ξ2,c]∥F2−F2†∥2.\displaystyle+C^{\Xi\_{2},q}\_{F\_{2},F\_{2}^{\dagger}})C^{q}\_{F\_{2},F\_{2}^{\dagger}}+(C^{\Xi\_{1},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}})C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{1},c}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},c}\_{F\_{2},F\_{2}^{\dagger}}\Big]\|F\_{2}-F\_{2}^{\dagger}\|^{2}. |  |

By the Grönwall’s inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖(xF2−x†)​(t)‖2≤\displaystyle\mathbb{E}\|(x^{F\_{2}}-x^{\dagger})(t)\|^{2}\leq | T(MTA†)2[(CF2,F2†Ξ1,q+CF2,F2†Ξ2,q)CF2,F2†q+(CF2,F2†Ξ1,x¯+CF2,F2†Ξ2,x¯)CF2,F2†x¯\displaystyle T(M^{A^{\dagger}}\_{T})^{2}\Big[(C^{\Xi\_{1},q}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},q}\_{F\_{2},F\_{2}^{\dagger}})C^{q}\_{F\_{2},F\_{2}^{\dagger}}+(C^{\Xi\_{1},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}})C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CF2,F2†Ξ1,c+CF2,F2†Ξ2,c]∥F2−F2†∥2exp[T(MTA†)2(CF2,F2†Ξ1,x+CF2,F2†Ξ2,x)].\displaystyle+C^{\Xi\_{1},c}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},c}\_{F\_{2},F\_{2}^{\dagger}}\Big]\|F\_{2}-F\_{2}^{\dagger}\|^{2}\exp\big[T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},x}\_{F\_{2},F\_{2}^{\dagger}})\big]. |  |

It then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (supt∈𝒯𝔼​‖(xF2−x†)​(t)‖2)12≤\displaystyle\big(\sup\_{t\in\mathcal{T}}\mathbb{E}\|(x^{F\_{2}}-x^{\dagger})(t)\|^{2}\big)^{\frac{1}{2}}\leq | TMTA†[(CF2,F2†Ξ1,q+CF2,F2†Ξ2,q)CF2,F2†q+(CF2,F2†Ξ1,x¯+CF2,F2†Ξ2,x¯)CF2,F2†x¯\displaystyle\sqrt{T}M^{A^{\dagger}}\_{T}\Big[(C^{\Xi\_{1},q}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},q}\_{F\_{2},F\_{2}^{\dagger}})C^{q}\_{F\_{2},F\_{2}^{\dagger}}+(C^{\Xi\_{1},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},\bar{x}}\_{F\_{2},F\_{2}^{\dagger}})C^{\bar{x}}\_{F\_{2},F\_{2}^{\dagger}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CF2,F2†Ξ1,c+CF2,F2†Ξ2,c]12∥F2−F2†∥exp[T(MTA†)2(CF2,F2†Ξ1,x+CF2,F2†Ξ2,x)/2].\displaystyle+C^{\Xi\_{1},c}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},c}\_{F\_{2},F\_{2}^{\dagger}}\Big]^{\frac{1}{2}}\|F\_{2}-F\_{2}^{\dagger}\|\exp\big[T(M^{A^{\dagger}}\_{T})^{2}(C^{\Xi\_{1},x}\_{F\_{2},F\_{2}^{\dagger}}+C^{\Xi\_{2},x}\_{F\_{2},F\_{2}^{\dagger}})/2\big]. |  |

∎

## Appendix B A Brief Overview of Structures over Hilbert Spaces

This section provides a brief overview of some functional analytic background to help keep our results as self-contained as possible.

### B.1 Output Space: Bochner-Lebesgue Spaces

Next, we are interested in working with the Bochner-Lebesgue space ℳ2​(𝒯,U)=L2​(Prog,U)\mathcal{M}^{2}(\mathcal{T},U)=L^{2}(\operatorname{Prog},U) of all UU-valued strongly-measurable and square-integrable functions; where Prog\operatorname{Prog} is the σ\sigma-algebra of progressively measurable processes.
The space ℳ2​(𝒯,U)\mathcal{M}^{2}(\mathcal{T},U) is a Hilbert space with inner-product defined for any f,g∈ℳ2​(𝒯,U)f,g\in\mathcal{M}^{2}(\mathcal{T},U) by
⟨f,g⟩ℳ2​(𝒯,U)=def.𝔼​[∫t=0T⟨f​(t),g​(t)⟩U​𝑑t]\langle f,g\rangle\_{\mathcal{M}^{2}(\mathcal{T},U)}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\mathbb{E}\left[\int\_{t=0}^{T}\,\langle f(t),g(t)\rangle\_{U}\,dt\right]. It is easy, but useful, to note that if f∈ℳ2​(𝒯,U)f\in\mathcal{M}^{2}({\mathcal{T}},U) is continuous and has finite supremum norm then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​‖f‖ℳ2​(𝒯,U)2=1T​𝔼​[∫0T‖f​(t)‖U2​𝑑t]≤sup0≤t≤T‖f​(t)‖U2\tfrac{1}{T}\,\|f\|\_{\mathcal{M}^{2}(\mathcal{T},U)}^{2}=\tfrac{1}{T}\,\mathbb{E}\biggl[\int\_{0}^{T}\,\|f(t)\|\_{U}^{2}\,dt\biggr]\leq\sup\_{0\leq t\leq T}\|f(t)\|\_{U}^{2} |  | (B.1) |

where ‖f‖ℳ2​(𝒯,U)\|f\|\_{\mathcal{M}^{2}(\mathcal{T},U)} is the natural norm on the Bochner-Lebesgue space ℳ2​(𝒯,U)\mathcal{M}^{2}(\mathcal{T},U).

With the obvious modifications of [Ryan, [2002](https://arxiv.org/html/2510.20017v1#bib.bib57), Example 2.19] (which treats the L1L^{1} and not L2L^{2} case as an example) the extension ℑ\mathfrak{I} of the linear map ℑ~:L2​(Prog)⊗U→ℳ2​(𝒯,U)\tilde{\mathfrak{I}}:L^{2}(\operatorname{Prog})\otimes U\to\mathcal{M}^{2}({\mathcal{T}},U) defined on elementary tensors f⊗yf\otimes y by ℑ~​(f⊗y)=def.f​(⋅)​y\tilde{\mathfrak{I}}(f\otimes y)\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}f(\cdot)y defines a (linear) isomorphism of Hilbert spaces.
As discussed in [Kadison and Ringrose, [1997](https://arxiv.org/html/2510.20017v1#bib.bib58), Chapter 2.6], an orthonormal basis for a tensor product of Hilbert spaces is given by the tensor product of the basis elements of its factors, up to normalizing constants. Consequently, when passing through ℑ\mathfrak{I} they yield an orthonormal basis of ℳ2​(𝒯,U)\mathcal{M}^{2}({\mathcal{T}},U).

### B.2 Hilbert-Schmidt Operators Between Different Spaces

Recall the square-summable sequence space ℓ2=def.{x=def.(xn)n=0∞,xn∈ℝ:⟨x,x⟩ℓ2<∞}\ell^{2}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\{x\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}(x\_{n})\_{n=0}^{\infty},\,x\_{n}\in\mathbb{R}:\,\langle x,x\rangle\_{\ell^{2}}<\infty\} where
⟨x,y⟩ℓ2=def.∑n=0∞xn​yn\langle x,y\rangle\_{\ell^{2}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\sum\_{n=0}^{\infty}\,x\_{n}y\_{n} for any x=def.(xn)n=0,y=def.(yn)n=0∈ℝℕx\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}(x\_{n})\_{n=0},y\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}(y\_{n})\_{n=0}\in\mathbb{R}^{\mathbb{N}}.
Fix separable Hilbert spaces 𝒴\mathcal{Y} and 𝒵\mathcal{Z}
which we, without loss of generality, assume are infinite-dimensional (if not, one may embed them in larger infinite-dimensional spaces and all operators become finite-rank and therefore trivially Hilbert-Schmidt).
Then, there exists isometric (linear) isomorphisms ϕ:𝒴↪ℓ2\phi:\mathcal{Y}\hookrightarrow\ell^{2} and ψ:𝒵↪ℓ2\psi:\mathcal{Z}\hookrightarrow\ell^{2}; which can, for instance, be constructed by fixing an orthonormal basis (yn)n=0∞(y\_{n})\_{n=0}^{\infty} of 𝒴\mathcal{Y} and then defining

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ:𝒴\displaystyle\phi:\mathcal{Y} | →ℓ2\displaystyle\rightarrow\ell^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y\displaystyle y | ↦(⟨y,yn⟩𝒴)n=0∞\displaystyle\mapsto(\langle y,y\_{n}\rangle\_{\mathcal{Y}})\_{n=0}^{\infty} |  |

where ⟨⋅,⋅⟩𝒴\langle\cdot,\cdot\rangle\_{\mathcal{Y}} denotes the inner-product on 𝒴\mathcal{Y}; with a similar (non-canonical) construction for ψ\psi.
We define subclass ℋ​𝒮​(𝒴,𝒵)⊆ℒ​(𝒴,𝒵)\mathcal{HS}(\mathcal{Y},\mathcal{Z})\subseteq\mathcal{L}(\mathcal{Y},\mathcal{Z}) consisting of operators that, under this identification, correspond to Hilbert-Schmidt operators; that is, A∈ℋ​𝒮​(𝒴,𝒵)A\in\mathcal{HS}(\mathcal{Y},\mathcal{Z}) if and only if the conjugated operator 𝐀=def.ψ∘A∘ϕ−1\mathbf{A}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\psi\circ A\circ\phi^{-1} is Hilbert-Schmidt; note, this definition is “canonical” in that it is independent of the choice of ϕ\phi and of ψ\psi (since all bases are chosen to be orthonormal).
We equip the (vector) space ℋ​𝒮​(𝒴,𝒵)\mathcal{HS}(\mathcal{Y},\mathcal{Z}) with the inner product

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨A,B⟩ℋ​𝒮​(𝒴,𝒵)=def.∑n=0∞⟨𝐀​λn,𝐁​λn⟩ℓ2,\langle A,B\rangle\_{\mathcal{HS}(\mathcal{Y},\mathcal{Z})}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\sum\_{n=0}^{\infty}\,\langle\mathbf{A}\lambda\_{n},\mathbf{B}\lambda\_{n}\rangle\_{\ell^{2}}, |  | (B.2) |

where {λn}n=0∞\{\lambda\_{n}\}\_{n=0}^{\infty}
and
for any n∈ℕn\in\mathbb{N}, λn=def.(λn:i)i=0∞\lambda\_{n}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}(\lambda\_{n:i})\_{i=0}^{\infty} where λi=1\lambda\_{i}=1 if i=ni=n and equals to zero otherwise.
From ([B.2](https://arxiv.org/html/2510.20017v1#A2.E2 "Equation B.2 ‣ B.2 Hilbert-Schmidt Operators Between Different Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")), it is relatively straightforward to see that the norm induced by the above inner product, called the Hilbert-Schmidt norm and denoted by ∥⋅∥ℋ​𝒮​(𝒴,𝒵)\|\cdot\|\_{\mathcal{HS}(\mathcal{Y},\mathcal{Z})}, dominates the operator norm

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖A‖o​p≤‖A‖ℋ​𝒮​(𝒴,𝒵).\|A\|\_{op}\leq\|A\|\_{\mathcal{HS}(\mathcal{Y},\mathcal{Z})}. |  | (B.3) |

The linear space ℋ​𝒮​(𝒴,𝒵)\mathcal{HS}(\mathcal{Y},\mathcal{Z}) is a Hilbert space with inner-product in ([B.2](https://arxiv.org/html/2510.20017v1#A2.E2 "Equation B.2 ‣ B.2 Hilbert-Schmidt Operators Between Different Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")) and with orthonormal basis {E(i,j)𝒴→𝒵}(i,j)∈ℕ2\{E\_{(i,j)}^{\mathcal{Y}\to\mathcal{Z}}\}\_{(i,j)\in\mathbb{N}^{2}} given by for each (i,j)∈ℕ2(i,j)\in\mathbb{N}^{2}
and every y∈𝒴y\in\mathcal{Y} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | E(i,j)𝒴→𝒵​(y)=def.⟨y,yi⟩𝒴​zjE\_{(i,j)}^{\mathcal{Y}\to\mathcal{Z}}(y)\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\langle y,y\_{i}\rangle\_{\mathcal{Y}}\,z\_{j} |  | (B.4) |

where (zj)j∈ℕ(z\_{j})\_{j\in\mathbb{N}} is choice of an orthonormal basis of 𝒵\mathcal{Z}.

###### Example 3.

Let 𝒳\mathcal{X} be an infinite-dimensional separable Hilbert space with inner-product ⟨⋅,⋅⟩𝒳\langle\cdot,\cdot\rangle\_{\mathcal{X}} and orthonormal basis (xk)k=0∞(x\_{k})\_{k=0}^{\infty}, and consider the orthonormal basis of ℋ​𝒮​(𝒴,𝒵)\mathcal{HS}(\mathcal{Y},\mathcal{Z}) defined in ([B.4](https://arxiv.org/html/2510.20017v1#A2.E4 "Equation B.4 ‣ B.2 Hilbert-Schmidt Operators Between Different Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
Then, we obtain an orthonormal basis of ℋ​𝒮​(𝒳,ℋ​𝒮​(𝒴,𝒵))\mathcal{HS}(\mathcal{X},\mathcal{HS}(\mathcal{Y},\mathcal{Z})) by iterating the construction in ([B.4](https://arxiv.org/html/2510.20017v1#A2.E4 "Equation B.4 ‣ B.2 Hilbert-Schmidt Operators Between Different Spaces ‣ Appendix B A Brief Overview of Structures over Hilbert Spaces ‣ Simultaneously Solving Infinitely Many LQ Mean Field Games In Hilbert Spaces: The Power of Neural Operators")).
Namely, let
{E(k,i,j)𝒳→ℋ​𝒮​(𝒴,𝒵)}(k,i,j)∈ℕ3\{E\_{(k,i,j)}^{\mathcal{X}\to\mathcal{HS}(\mathcal{Y},\mathcal{Z})}\}\_{(k,i,j)\in\mathbb{N}^{3}} be defined for each (k,i,j)∈ℕ3(k,i,j)\in\mathbb{N}^{3} as mapping any x∈𝒳x\in\mathcal{X} to the
Hilbert-Schmidt operator in ℋ​𝒮​(𝒴,𝒵)\mathcal{HS}(\mathcal{Y},\mathcal{Z}) given by

|  |  |  |
| --- | --- | --- |
|  | E(k,i,j)𝒳→ℋ​𝒮​(𝒴,𝒵)​(x)=def.⟨x,xk⟩𝒳​E(i,j)𝒴→𝒵.E\_{(k,i,j)}^{\mathcal{X}\to\mathcal{HS}(\mathcal{Y},\mathcal{Z})}(x)\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\langle x,x\_{k}\rangle\_{\mathcal{X}}\,E\_{(i,j)}^{\mathcal{Y}\to\mathcal{Z}}. |  |

### B.3 Direct Sums of Spaces of Hilbert Spaces

Fix an integer I≥2I\geq 2 and let 𝒳1,…,𝒳I\mathcal{X}\_{1},\dots,\mathcal{X}\_{I} be separable infinite-dimensional Hilbert spaces. For each i=1,…,Ii=1,\dots,I, let {xn(i)}n=0∞\{x^{(i)}\_{n}\}\_{n=0}^{\infty} be an orthonormal basis of 𝒳(i)\mathcal{X}^{(i)} and let ⟨⋅,⋅⟩𝒳(i)\langle\cdot,\cdot\rangle\_{\mathcal{X}^{(i)}} denote the inner-product thereon. Then, the direct sum of these Hilbert spaces, denoted by ⨁i=1I𝒳(i)\bigoplus\_{i=1}^{I}\,\mathcal{X}^{(i)} or by 𝒳(1)⊕⋯⊕𝒳(I)\mathcal{X}^{(1)}\oplus\dots\oplus\mathcal{X}^{(I)}, is the vector space whose underlying set is the Cartesian product ∏i=1I𝒳(i)\prod\_{i=1}^{I}\,\mathcal{X}^{(i)} and whose inner-product
⟨⋅,⋅⟩⨁i=1I𝒳(i)\langle\cdot,\cdot\rangle\_{\bigoplus\_{i=1}^{I}\,\mathcal{X}^{(i)}}
is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(xi)i=1I,(x~i)i=1I⟩⨁i=1I𝒳(i)=def.∑i=1I⟨xi,x~i⟩𝒳(i)\langle(x^{i})\_{i=1}^{I},(\tilde{x}^{i})\_{i=1}^{I}\rangle\_{\bigoplus\_{i=1}^{I}\,\mathcal{X}^{(i)}}\stackrel{{\scriptstyle\mbox{\tiny def.}}}{{=}}\sum\_{i=1}^{I}\,\langle x^{i},\tilde{x}^{i}\rangle\_{\mathcal{X}^{(i)}} |  | (B.5) |

for any (xi)i=1I,(x~i)i=1I∈⨁i=1I𝒳(i)(x^{i})\_{i=1}^{I},(\tilde{x}^{i})\_{i=1}^{I}\in\bigoplus\_{i=1}^{I}\,\mathcal{X}^{(i)}. Moreover, an orthonormal basis of ⨁i=1I𝒳(i)\bigoplus\_{i=1}^{I}\,\mathcal{X}^{(i)} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⋃j=1I{(δj=i​xn(i))j=1I}n=1∞.\bigcup\_{j=1}^{I}\,\big\{(\delta\_{j=i}x^{(i)}\_{n})\_{j=1}^{I}\big\}\_{n=1}^{\infty}. |  | (B.6) |