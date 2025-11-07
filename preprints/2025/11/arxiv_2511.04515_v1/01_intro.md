---
authors:
- Mathieu Laurière
- Ariel Neufeld
- Kyunghyun Park
doc_id: arxiv:2511.04515v1
family_id: arxiv:2511.04515
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Robust mean-field control under common noise uncertainty
url_abs: http://arxiv.org/abs/2511.04515v1
url_html: https://arxiv.org/html/2511.04515v1
venue: arXiv q-fin
version: 1
year: 2025
---


Mathieu Laurière
Shanghai Frontiers Science Center of Artificial Intelligence and Deep Learning, and NYU-ECNU Institute of Mathematical Sciences, NYU Shanghai
[mathieu.lauriere@nyu.edu](mailto:mathieu.lauriere@nyu.edu)
, 
Ariel Neufeld
Division of Mathematical Sciences, Nanyang Technological University
[ariel.neufeld@ntu.edu.sg](mailto:ariel.neufeld@ntu.edu.sg)
 and 
Kyunghyun Park
Division of Mathematical Sciences, Nanyang Technological University
[kyunghyun.park@ntu.edu.sg](mailto:kyunghyun.park@ntu.edu.sg)

(Date: November 6, 2025.)

###### Abstract.

We propose and analyze a framework for discrete-time robust mean-field control problems under common noise uncertainty. In this framework, the mean-field interaction describes the collective behavior of infinitely many cooperative agents’ state and action, while the common noise—a random disturbance affecting all agents’ state dynamics—is uncertain. A social planner optimizes over open-loop controls on an infinite horizon to maximize the representative agent’s worst-case expected reward, where worst-case corresponds to the most adverse probability measure among all candidates inducing the unknown true law of the common noise process. We refer to this optimization as a robust mean-field control problem under common noise uncertainty. We first show that this problem arises as the asymptotic limit of a cooperative NN-agent robust optimization problem, commonly known as propagation of chaos. We then prove the existence of an optimal open-loop control by linking the robust mean field control problem to a lifted robust Markov decision problem on the space of probability measures and by establishing the dynamic programming principle and Bellman–Isaac fixed point theorem for the lifted robust Markov decision problem. Finally, we complement our theoretical results with numerical experiments motivated by distribution planning and systemic risk in finance, highlighting the advantages of accounting for common noise uncertainty.

Key words: mean-field control, common noise uncertainty, robust optimization, propagation of chaos, Markov decision process, dynamic programming.

Funding:
M. Laurière acknowledges the support of the grant “AI-driven Initiative to Promote Research Paradigm Reform and Empower Discipline Advancement.” Computing resources were provided by NYU Shanghai HPC. A. Neufeld acknowledges the support of
the MOE AcRF Tier 2 Grant MOE-T2EP20222-0013.
K. Park acknowledges the support of the National Research
Foundation of Korea (grant DOI: RS-2025-02633175).

## 1. Introduction

Mean-field control problems [bensoussan2013mean, carmona2018probabilistic], also known as optimal control of McKean–Vlasov dynamics, have emerged as a fundamental framework for optimizing the behavior of large populations of cooperative agents. By considering a social planner or central controller managing an infinite (or very large) number of homogeneous agents, mean-field control problems capture a wide range of scenarios including in economics and finance (e.g., [fischer2016continuous, fu2024mean, carmona2021deep, carmona2020applications]), and robotics (e.g., [lerman2004review, elamvazhuthi2019mean, khamis2015multi, cui2023scalable].

One significant extension of the mean-field control paradigm is the inclusion of common noise—a random disturbance affecting the dynamics of all agents (e.g., [carmona2023model, motte2022mean, djete2022extended, djete2022mckean, pham2017dynamic, motte2023quantitative]). This feature has become prominent because it captures systemic, correlated randomness (such as macroeconomic shocks or environmental disturbances) that affects the entire population simultaneously. In particular, accounting for common noise enhances the realism of mean-field control problems’ applications in financial engineering, including portfolio optimization, optimal liquidation, or systemic risk (e.g., [MR3325083, balata2019class, pham2016linear]), as well as in economics, including contract theory or the production of exhaustible resources (e.g., [elie2021mean, graber2016linear, basei2019weak]).

However, mean-field control problems with common noise inevitably face a key challenge: model uncertainty. When a social planner implements a mean-field control problem with common noise, it is likely that there is a margin for potential inaccuracies in the model parameters or distributions governing the common noise process. Crucially, because the common noise process affects all agents simultaneously, even small modeling errors in the common noise process can have widespread impact across our prediction of the system’s evolution or our computation of the optimal control. This motivates the need for a robust framework—also known as the worst-case or Knightian approach (e.g., [chen2002ambiguity, dow1992uncertainty, gilboa1989maxmin, garlappi2007portfolio])—in which the social planner seeks an optimal policy that performs robustly under uncertain dynamics of the common noise.

In this article, we aim to propose and analyze a discrete-time robust mean-field control problem under *common noise uncertainty*. The starting point for our problem is based on the two recent works by Carmona et al.[carmona2023model] and Motte and Pham [motte2022mean], where infinite time-horizon discounted mean-field control problems with common noise are considered. Both two works establish the correspondence between the conditional Mckean–Vlasov dynamics for the representative agent’s state (that typically appear in mean-field control problems with common noise) and the lifted Markov decision process on the space of probability measures on the state space. This correspondence enables to articulate dynamic programming Bellman fixed point equations, leading to derive optimal open-loop (and closed-loop Markov) policies for mean-field control problems. Furthermore, [motte2022mean] establishes the propagation of chaos result which connects the mean-field control problem to a social planner’s optimization problem with a large but finite number of cooperative agents. This ensures that the optimal open-loop policy for the mean-field control problem can be a useful approximation of the optimal policy for such large but finite cooperative agents problems.

Building on [carmona2023model, motte2022mean], we introduce a probabilistic framework for robust mean-field control problems under common noise uncertainty. This framework is designed to encompass both the finite cooperative NN-agent system and the conditional McKean–Vlasov dynamics when the common noise distribution is unknown (see Sectionă[2.2](https://arxiv.org/html/2511.04515v1#S2.SS2 "2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). In contrast with the fixed probability measure setting in [carmona2023model, motte2022mean] which induces a single law for the common noise, we construct a set of probability measures, allowing the common noise to have multiple laws within a prescribed uncertainty measures set (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).
This extension is inspired by the robust Markov decision framework ofă[neufeld2023markov, neufeld2024robust, langner2024markov], which enables to specify a wide range of different uncertainty sets of probability measures and associated transition kernels.

Using this framework, we establish three main results. First, we prove a propagation of chaos result linking the finite NN-agent robust control problem to its mean-field (infinite-agent) counterpart under common noise uncertainty. Under mild regularity conditions on the system and reward functions, we show that the NN-agent robust control problem converges to the robust mean-field control problem as N→∞N\to\infty (see Theoremă[2.9](https://arxiv.org/html/2511.04515v1#S2.Thmthm9 "Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). This implies that the optimal open-loop policy obtained from the robust mean-field control problem serves as an approximately optimal policy for the finitely many NN-agent robust control problem. The proof is based on the Wasserstein convergence rates for empirical measures [fournier2015rate, boissard2014mean]. In this regard, our propagation of chaos result can be viewed as a robust analog of the results in [motte2022mean, motte2023quantitative].

Second, we establish a dynamic programming principle for the robust mean-field control problem by lifting it to the space of probability measures on the state space. To that end, we show that the conditional McKean–Vlasov state dynamics under common noise uncertainty corresponds to a lifted robust Markov decision process on the space of probability measures (see Propositionă[2.12](https://arxiv.org/html/2511.04515v1#S2.Thmthm12 "Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). This correspondence allows us to derive the Bellman–Isaacs fixed-point equations for the value function in the lifted space of distributions. The proof relies on Berge’s maximum theorem to construct local (i.e., one time-step) optimal control and worst-case common noise measure (see Propositionă[2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), and the Banach fixed-point theorem to establish the existence and uniqueness of a fixed point for the Bellman–Isaacs operator (see Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). We then construct an optimal open-loop policy for the robust mean-field control problem by aggregating the local optimizers (see Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). A crucial toolkit in this construction is the use of an extrinsic randomization source with an atomless distribution (see Assumption [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), which also appears in [carmona2023model]. This randomization not only facilitates the implementation of randomized policies in a decentralized manner but also ensures that each agent’s distribution of controls aligns with the law of optimal policy prescribed by the social planner. While the existence of a randomization source is not explicitly assumed in [motte2022mean], a randomization hypothesis on the initial information is imposed therein, which in turn induces a structure from which a randomization source naturally exists; see Remark 3.1 therein.

Third, we introduce a closed-loop Markov policy formulation of the robust mean-field control problem. We establish the equivalence between open-loop and closed-loop formulations (Corollary [2.28](https://arxiv.org/html/2511.04515v1#S2.Thmthm28 "Corollary 2.28. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and obtain an
optimal closed-loop Markov policy. This result can be considered as a robust analog of the main results in [carmona2023model].

Finally, in order to illustrate all our theoretical results, we provide two numerical examples (see Section [3](https://arxiv.org/html/2511.04515v1#S3 "3. Numerical examples ‣ Robust mean-field control under common noise uncertainty")). In the first example, inspired by Example 1 of [carmona2023model], the central planner’s goal is to steer the population distribution towards a target distribution. In the second example, inspired by the systemic risk model of [MR3325083], the central planner’s goal is to stabilize a financial system and avoid that too many institutions default. In both examples, we underscore the importance and benefits of incorporating common noise uncertainty into mean-field control frameworks.

Related literature. Classic mean-field control problems have been described predominantly in continuous time (see, e.g., [pham2017dynamic, lauriere2016dynamic, fischer2016continuous, fu2024mean, djete2022mckeanAOP, bayraktar2018randomized, soner2024viscosity, burzoni2020viscosity, bensoussan2024control, cosso2019zero, wang2017social, sanjari2020optimal]). Several works [djete2022extended, djete2022mckean, lacker2017limit, fornasier2019mean] have rigorously established the connection between mean-field control and large systems of controlled processes in continuous time settings.

Notably, robust mean-field control problems in continuous-time settings, involving uncertainty in the drift or volatility of the common noise, have been investigated in [huang2021social, wang2020social, wang2017socialjump]. The conceptual structure of the arguments in [huang2021social] bears certain similarities to ours: in the paper, a centralized control problem under volatility uncertainty of the common noise (analogous to our lifted robust Markov decision problem) is tackled, and then decentralized strategies for the population of agents (analogous to our construction of optimal open-loop policies for the robust mean-field control problem) are obtained.
Nevertheless, there are key differences. In particular, the continuous-time works rely on the theory of forward-backward stochastic differential equations, which are not suitable in the discrete-time setting we consider. Instead, our analysis requires a measure-theoretic construction of optimal controls and a derivation of the dynamic programming principle on the space of probability measures. Most notably, while the aforementioned works do not establish a propagation of chaos result, our article provides the first such result under common noise uncertainty.

Several works on mean-field game and control problems have introduced robustness via min–max formulations (e.g., [huang2017robust, liang2022robust, carmona2020policy, carmona2021linear, zaman2024robust]). However, these models do not consider common noise but idiosyncratic noise which is uncertain.
In contrast, our framework explicitly accounts for common noise uncertainty, which introduces fundamentally different technical and conceptual challenges. While extending the model to include both idiosyncratic and common noise uncertainty is of clear interest, such an extension leads to significant technical obstacles that invalidate key arguments used in establishing the propagation of chaos result and the lifted dynamic programming principle. This is beyond the scope of the present paper, and we leave it for future work.

Moving away from the above continuous time settings to discrete time settings, some works [pham2016discrete, gu2023dynamic, gu2021mean, gu2025mean, lauriere2016dynamic] have explored dynamic progarmming principles for discrete time mean-field control problems, but without considering common noise. More relevant to our setting, recent works—including those we benchmark against [motte2022mean, carmona2023model] and others such as [bauerle2023mean, motte2023quantitative, bayraktar2024infinite]—have investigated discrete-time mean-field control problems with common noise.
Notably, a recent work [langner2024markov] by two of the authors of the present article proposes a framework for discrete time mean-field Markov games under model uncertainty. In contrast, we focus on a cooperative control setting (as opposed to a game-theoretic equilibrium) and consider the model uncertainty in the law of the common noise process. This leads to a different optimization structure and our lifted dynamic programming formulation on the space of measures is specifically tailored to this social control setting. Furthermore, our propagation of chaos result has no analogue in [langner2024markov], whose results concern approximate Nash equilibria rather than centralized performance guarantees.

Finally, for completeness, we note that a substantial body of work has focused on robust Markov decision processes under model uncertainty, which also underpin our lifted dynamic programming result on the space of probability measures (see, e.g., [bauerle2022distributionally, bayraktar2023nonparametric, el2005robust, liu2022distributionally, neufeld2024robust, neufeld2023markov, neufeld2024non, wiesemann2013robust, xu2012distributionally, yang2017convex, li2023policy, lu2025distributionally] in the optimal control literature, and [hansen2008robustness] in the economics literature).

## 2. Main results

### 2.1. Notation and preliminaries

Throughout this article, we work with Polish spaces. If XX is such a space with corresponding metric dXd\_{X}, we denote by BX{\mathcal{}B}\_{X} its Borel σ\sigma-algebra and by P​(X){\mathcal{}P}(X) the set of all Borel probability measures on XX. Let Cb​(X;ℝ)C\_{b}(X;\mathbb{R}) be the set of all bounded and continuous functions f:X→ℝf:X\to\mathbb{R}, endowed with the supremum norm ‖f‖∞:=supx∈X|f​(x)|\|f\|\_{\infty}:=\sup\_{x\in X}|f(x)| where |⋅||\cdot| denotes the Euclidean norm. For any L≥0L\geq 0, we denote by Lipb,L⁡(X;ℝ)⊂Cb​(X;ℝ)\operatorname{Lip}\_{b,L}(X;\mathbb{R})\subset C\_{b}(X;\mathbb{R}) the set of all LL-Lipschitz continuous functions.

We equip P​(X){\mathcal{}P}({X}) with the topology induced by weak convergence, i.e., for any μ∈P​(X)\mu\in{\mathcal{}P}({X}) and any (μn)n∈ℕ⊆P​(X)(\mu^{n})\_{n\in\mathbb{N}}\subseteq{\mathcal{}P}({X}), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | μn⇀μ​as n→∞⇔limn→∞∫Xf​(x)​μn​(d​x)=∫Xf​(x)​μ​(d​x)​for any f∈Cb​(X;ℝ).\displaystyle\mu^{n}\rightharpoonup\mu\;\;\mbox{as $n\rightarrow\infty$}\;\Leftrightarrow\;\;\lim\_{n\rightarrow\infty}\int\_{X}f(x)\mu^{n}(dx)=\int\_{X}f(x)\mu(dx)\;\;\mbox{for any $f\in C\_{b}(X;\mathbb{R})$}. |  |

If XX is compact, then the weak topology given in ([2.1](https://arxiv.org/html/2511.04515v1#S2.E1 "In 2.1. Notation and preliminaries ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) is equivalent to the topology induced by the 1-Wasserstein distance WP​(X)​(⋅,⋅){\mathcal{}W}\_{{\mathcal{}P}(X)}(\cdot,\cdot) which we recall to be the following: For any μ,μ^∈P​(X)\mu,\hat{\mu}\in{\mathcal{}P}(X), denote by CplX×X⁡(μ,μ^)⊂P​(X×X)\operatorname{Cpl}\_{X\times X}(\mu,\hat{\mu})\subset{\mathcal{}P}(X\times X) the subset of all couplings with marginals μ,μ^\mu,\hat{\mu}. Then the 1-Wasserstein distance between μ\mu and μ^\hat{\mu} is defined by

|  |  |  |
| --- | --- | --- |
|  | WP​(X)​(μ,μ^):=infΓ∈CplX×X⁡(μ,μ^)∫X×XdX​(x,y)​Γ​(d​x,d​y).{\mathcal{}W}\_{{\mathcal{}P}(X)}(\mu,\hat{\mu}):=\inf\_{\Gamma\in\operatorname{Cpl}\_{X\times X}(\mu,\hat{\mu})}\int\_{X\times X}d\_{X}(x,y)\Gamma(dx,dy). |  |

For each t∈ℕt\in\mathbb{N}, we use the abbreviation Xt:=X×⋯×XX^{t}:=X\times\cdots\times X for the tt-times Cartesian product of the set XX. Given a sequence (x0,…,xt)∈Xt+1(x\_{0},\dots,x\_{t})\in X^{t+1} and 0≤s≤t0\leq s\leq t, we use the following abbreviation xs:t:=(xs,…,xt)x\_{s:t}:=(x\_{s},\dots,x\_{t}). Then we endow Xt+1X^{t+1} with the corresponding product topology induced by the following metric: for every x0:t,x~0:t∈Xt+1x\_{0:t},\tilde{x}\_{0:t}\in X^{t+1},

|  |  |  |
| --- | --- | --- |
|  | dXt+1​(x0:t,x~0:t):=∑i=0tdX​(xi,x~i).d\_{X^{t+1}}(x\_{0:t},\tilde{x}\_{0:t}):=\sum\_{i=0}^{t}d\_{X}(x\_{i},\tilde{x}\_{i}). |  |

The same convention applies to a finite Cartesian product of (possibly different) Polish spaces.

For two Polish spaces XX and YY, the term ‘kernel’ refers to a Borel measurable map λ:X∋x↦λ​(d​y|x)∈P​(Y)\lambda:X\ni x\mapsto\lambda(dy|x)\in{\mathcal{}P}(Y). For every μ∈P​(X)\mu\in{\mathcal{}P}(X) and kernel λ\lambda, we write μ⊗^λ∈P​(X×Y)\mu\mathbin{\hat{\otimes}}\lambda\in{\mathcal{}P}(X\times Y) for the measure given by: for every B∈BX×YB\in{\mathcal{}B}\_{X\times Y}, μ⊗^λ​(B):=∫X×Y𝟏{(x,y)∈B}​λ​(d​y|x)​μ​(d​x)\mu\mathbin{\hat{\otimes}}\lambda(B):=\int\_{X\times Y}{\bf 1}\_{\{(x,y)\in B\}}\lambda(dy|x)\mu(dx). Moreover for every ν∈P​(Y)\nu\in{\mathcal{}P}(Y), we write μ⊗ν∈P​(X×Y)\mu\otimes\nu\in{\mathcal{}P}(X\times Y) for the product measure.

Finally, given μ∈P​(X)\mu\in{\mathcal{}P}(X) we use the notation ℒμ​(Z)\mathscr{L}\_{\mu}({\mathcal{}Z}) for the law of a random variable Z{\mathcal{}Z} under μ{\mu} and use ℒμ​(Z|Y)\mathscr{L}\_{\mu}({\mathcal{}Z}|{\mathcal{}Y}) for the conditional law of Z{\mathcal{}Z} given a random variable Y{\mathcal{}Y} under μ{\mu}. The same convention applies to a σ\sigma-field. We denote by δx∈P​(X)\delta\_{x}\in{\mathcal{}P}(X) the Dirac measure at the point x∈Xx\in X.

### 2.2. Propagation of chaos under common noise uncertainty

In this section, we specify what we mean by the discrete-time NN-agent model and mean-field control (MFC) model under common noise uncertainty. We then establish the convergence of the NN-agent model to the MFC model as the number of agents NN goes to infinity.

To that end, we begin by defining a canonical space for the mean-field models with infinitely many indistinguishable agents.

Denote by GG the initial information space and by Θ\Theta the randomization source space. Moreover denote by EE and E0E^{0} idiosyncratic and common noise spaces, respectively.
On the space defined by

|  |  |  |
| --- | --- | --- |
|  | Ω:={ω:=((gi)i∈ℕ,(θti)t≥0,i∈ℕ,(eti)t≥1,i∈ℕ,(et0)t≥1):(gi,θti)∈G×Θ,for t≥0,i∈ℕ;(eti,et0)∈E×E0,for​t≥1,i∈ℕ},\displaystyle\Omega:=\left\{\omega:=\big((g^{i})\_{i\in\mathbb{N}},(\theta\_{t}^{i})\_{t\geq 0,i\in\mathbb{N}},(e\_{t}^{i})\_{t\geq 1,i\in\mathbb{N}},(e^{0}\_{t})\_{t\geq 1}\big)\;:\begin{aligned} &\;(g^{i},\theta^{i}\_{t})\in G\times\Theta,\;\;\mbox{for $t\geq 0$},\;i\in\mathbb{N};\\ &\;(e^{i}\_{t},e^{0}\_{t})\in E\times E^{0},\;\;\mbox{for}\;t\geq 1,\;i\in\mathbb{N}\end{aligned}\right\}, |  |

we denote, for every ω∈Ω\omega\in\Omega,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | (γi​(ω),ϑ0i​(ω)):=(gi,θ0i)∈G×Θi∈ℕ,(ϑti​(ω),εti​(ω)):=(θti,eti)∈Θ×Et≥1,i∈ℕ,εt0​(ω):=et0∈E0t≥1,\displaystyle\begin{aligned} \big(\gamma^{i}(\omega),\vartheta\_{0}^{i}(\omega)\big)&:=(g^{i},\theta^{i}\_{0})\in G\times\Theta\quad&&i\in\mathbb{N},\\ \big(\vartheta\_{t}^{i}(\omega),\varepsilon^{i}\_{t}(\omega)\big)&:=(\theta^{i}\_{t},e\_{t}^{i})\in\Theta\times E\quad&&t\geq 1,\;\;i\in\mathbb{N},\\ \varepsilon\_{t}^{0}(\omega)&:=e\_{t}^{0}\in E^{0}\quad&&t\geq 1,\end{aligned} |  |

so that γi\gamma^{i} and (ϑti)t≥0(\vartheta\_{t}^{i})\_{t\geq 0} represent the initial state information of agent i∈ℕi\in\mathbb{N} and her randomization source process, respectively. Moreover, (εti)t≥1(\varepsilon\_{t}^{i})\_{t\geq 1} represents her idiosyncratic noise process and (εt0)t≥1(\varepsilon\_{t}^{0})\_{t\geq 1} represents the common noise process for all agents.

In what follows, we describe a set of probability measures on the space Ω\Omega, which captures model uncertainty in the common noise process.

###### Definition 2.1 (Filtrations).

Consider the following filtrations: for each i∈ℕi\in\mathbb{N}

* ⋅\cdot

  𝔽0:=(Ft0)t≥0\mathbb{F}^{0}:=({\mathcal{}F}^{0}\_{t})\_{t\geq 0} is given by Ft0:=σ​(ε1:t0){\mathcal{}F}^{0}\_{t}:=\sigma(\varepsilon\_{1:t}^{0}) for all t≥1t\geq 1 with F00={∅,Ω}{\mathcal{}F}\_{0}^{0}=\{\emptyset,\Omega\}.
* ⋅\cdot

  𝔽i:=(Fti)t≥0\mathbb{F}^{i}:=({\mathcal{}F}^{i}\_{t})\_{t\geq 0} is given by F0i:=σ​(γi){\mathcal{}F}\_{0}^{i}:=\sigma(\gamma^{i}) and Fti:=σ​(γi,ϑ0:t−1i,ε1:ti,ε1:t0){\mathcal{}F}^{i}\_{t}:=\sigma(\gamma^{i},\vartheta\_{0:t-1}^{i},\varepsilon\_{1:t}^{i},\varepsilon\_{1:t}^{0}) for all t≥1t\geq 1.
* ⋅\cdot

  𝔾i:=(Gti)t≥0\mathbb{G}^{i}:=({\mathcal{}G}^{i}\_{t})\_{t\geq 0} is given by
  Gti:=Fti∨σ​(ϑti){\mathcal{}G}\_{t}^{i}:={\mathcal{}F}\_{t}^{i}\vee\sigma(\vartheta\_{t}^{i}) for all t≥0t\geq 0 so that 𝔽i⊆𝔾i\mathbb{F}^{i}\subseteq\mathbb{G}^{i}.

Here Ft0{\mathcal{}F}\_{t}^{0} represents the common noise information shared by all agents at time tt. Both Fti{\mathcal{}F}\_{t}^{i} and Gti{\mathcal{}G}\_{t}^{i} represent the information of agent ii at time tt, where Gti{\mathcal{}G}\_{t}^{i} includes the current randomization source ϑti\vartheta\_{t}^{i}, while Fti{\mathcal{}F}\_{t}^{i} does not.

###### Definition 2.2 (Measures).

Fix λγ∈P​(G)\lambda\_{\gamma}\in{\mathcal{}P}(G), λϑ∈P​(Θ),\lambda\_{\vartheta}\in{\mathcal{}P}(\Theta), and λε∈P​(E)\lambda\_{\varepsilon}\in{\mathcal{}P}(E).

* (i)

  Let 𝔓0⊆P​(E0)\mathfrak{P}^{0}\subseteq{\mathcal{}P}({E}^{0})
  be a non-empty subset of Borel probability measures on E0E^{0}. Then denote by 𝒦0\mathcal{K}^{0} the set of all (pt)t≥1(p\_{t})\_{t\geq 1} consisting of a measure and sequence of kernels such that

  |  |  |  |
  | --- | --- | --- |
  |  | p1∈𝔓0;pt:(E0)t−1∋e1:t−10↦pt(det0|e1:t−10)∈𝔓0for all t≥2,\displaystyle\hskip 30.00005ptp\_{1}\in\mathfrak{P}^{0};\qquad p\_{t}:(E^{0})^{t-1}\ni e\_{1:t-1}^{0}\mapsto p\_{t}(de\_{t}^{0}|e\_{1:t-1}^{0})\in\mathfrak{P}^{0}\quad\mbox{for all $t\geq 2$}, |  |

  inducing model uncertainty in the law of the common noise process (εt0)t≥1(\varepsilon\_{t}^{0})\_{t\geq 1}.
* (ii)

  Denote by Q⊆P​(Ω){\mathcal{}Q}\subseteq{\mathcal{}P}(\Omega) the subset of all Borel probability measures ℙ\mathbb{P} on Ω\Omega induced by some (pt)t≥1∈𝒦0(p\_{t})\_{t\geq 1}\in\mathcal{K}^{0} in the sense that for every B0∈⋁i∈ℕ𝒢0iB\_{0}\in\bigvee\_{i\in\mathbb{N}}\mathcal{G}\_{0}^{i} and B1∈⋁i∈ℕG1iB\_{1}\in\bigvee\_{i\in\mathbb{N}}{\mathcal{}G}\_{1}^{i}

  |  |  |  |
  | --- | --- | --- |
  |  | ℙ​{(γi,ϑ0i)i∈ℕ∈B0}=Q^0​(B0),ℙ​{((γi,ϑ0:1i,ε1i)i∈ℕ,ε10)∈B1}=(Q^0⊗Q^p1)​(B1),\displaystyle\hskip 40.00006pt\begin{aligned} &\mathbb{P}\big\{(\gamma^{i},\vartheta\_{0}^{i})\_{i\in\mathbb{N}}\in B\_{0}\big\}=\hat{Q}\_{0}(B\_{0}),\quad\mathbb{P}\big\{((\gamma^{i},\vartheta\_{0:1}^{i},\varepsilon\_{1}^{i})\_{i\in\mathbb{N}},\varepsilon\_{1}^{0})\in B\_{1}\big\}=(\hat{Q}\_{0}\otimes\hat{Q}^{p\_{1}})(B\_{1}),\end{aligned} |  |

  where

  |  |  |  |
  | --- | --- | --- |
  |  | Q^0​((d​gi,d​θ0i)i∈ℕ):=⊗i∈ℕ{(λγ⊗λϑ)​(d​gi,d​θ0i)}∈P​((G×Θ)ℕ)Q^p1​((d​θ1i,d​e1i)i∈ℕ,d​e10):=⊗i∈ℕ{(λϑ⊗λε)​(d​θ1i,d​e1i)}​p1​(d​e10)∈P​((Θ×E)ℕ×E0),\displaystyle\hskip 40.00006pt\begin{aligned} \hat{Q}\_{0}\big((dg^{i},d\theta\_{0}^{i})\_{i\in\mathbb{N}}\big)&:=\mathop{\otimes}\limits\_{i\in\mathbb{N}}\big\{(\lambda\_{\gamma}\otimes\lambda\_{\vartheta})(dg^{i},d\theta^{i}\_{0})\big\}\in{\mathcal{}P}\big((G\times\Theta)^{\mathbb{N}}\big)\\ \hat{Q}^{p\_{1}}\big((d\theta^{i}\_{1},de^{i}\_{1})\_{i\in\mathbb{N}},de^{0}\_{1}\big)&:=\mathop{\otimes}\limits\_{i\in\mathbb{N}}\big\{(\lambda\_{\vartheta}\otimes\lambda\_{\varepsilon})(d\theta^{i}\_{1},de\_{1}^{i})\big\}p\_{1}(de^{0}\_{1})\in{\mathcal{}P}\big((\Theta\times E)^{\mathbb{N}}\times E^{0}\big),\end{aligned} |  |

  whereas for every t≥2t\geq 2 and Bt∈⋁i∈ℕGtiB\_{t}\in\bigvee\_{i\in\mathbb{N}}{\mathcal{}G}\_{t}^{i}

  |  |  |  |
  | --- | --- | --- |
  |  | ℙ​{((γi,ϑ0:ti,ε1:ti)i∈ℕ,ε1:t0)∈Bt}=(Q^0⊗Q^p1⊗^Q^p2⊗^⋯⊗^Q^pt)​(Bt),\displaystyle\hskip 30.00005pt\mathbb{P}\big\{\big((\gamma^{i},\vartheta^{i}\_{0:t},\varepsilon\_{1:t}^{i})\_{i\in\mathbb{N}},\varepsilon\_{1:t}^{0}\big)\in B\_{t}\big\}=(\hat{Q}\_{0}\otimes\hat{Q}^{p\_{1}}\mathbin{\hat{\otimes}}\hat{Q}^{p\_{2}}\mathbin{\hat{\otimes}}\cdots\mathbin{\hat{\otimes}}\hat{Q}^{p\_{t}})(B\_{t}), |  |

  where Q^pt:(E0)t−1∋e1:t−10↦Q^pt​((d​θti,d​eti)i∈ℕ,d​et0|e1:t−10)∈P​((Θ×E)ℕ×E0)\hat{Q}^{p\_{t}}:(E^{0})^{t-1}\ni e\_{1:t-1}^{0}\mapsto\hat{Q}^{p\_{t}}((d\theta\_{t}^{i},de\_{t}^{i})\_{i\in\mathbb{N}},de\_{t}^{0}|e\_{1:t-1}^{0})\in{\mathcal{}P}((\Theta\times E)^{\mathbb{N}}\times E^{0}) is defined by

  |  |  |  |
  | --- | --- | --- |
  |  | Q^pt​((d​θti,d​eti)i∈ℕ,d​et0|e1:t−10):=⊗i∈ℕ{(λϑ⊗λε)​(d​θti,d​eti)}​pt​(d​et0|e1:t−10).\displaystyle\hskip 30.00005pt\hat{Q}^{p\_{t}}\big((d\theta\_{t}^{i},de\_{t}^{i})\_{i\in\mathbb{N}},de\_{t}^{0}|e\_{1:t-1}^{0}\big):=\mathop{\otimes}\limits\_{i\in\mathbb{N}}\big\{(\lambda\_{\vartheta}\otimes\lambda\_{\varepsilon})(d\theta^{i}\_{t},de\_{t}^{i})\big\}p\_{t}(de\_{t}^{0}|e\_{1:t-1}^{0}). |  |

###### Remark 2.3.

By Ionescu–Tulcea’s theorem (see, e.g., [kallenberg2002foundations, Theorem 6.17]), the set Q{\mathcal{}Q} given in Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") is well-defined and the following hold: for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q} w.r.t. some (pt)t≥1∈𝒦0(p\_{t})\_{t\geq 1}\in\mathcal{K}^{0}

* (i)

  (γi)i∈ℕ(\gamma^{i})\_{i\in\mathbb{N}}, (ϑti)t≥0,i∈ℕ(\vartheta\_{t}^{i})\_{t\geq 0,i\in\mathbb{N}}, (εti)t≥1,i∈ℕ(\varepsilon\_{t}^{i})\_{t\geq 1,i\in\mathbb{N}}, and (εt0)t≥1(\varepsilon\_{t}^{0})\_{t\geq 1} are mutually independent.
* (ii)

  (γi)i∈ℕ(\gamma^{i})\_{i\in\mathbb{N}} is independent and identically distributed (i.i.d.) with law λγ\lambda\_{\gamma}. Moreover, (ϑti)t≥0,i∈ℕ(\vartheta\_{t}^{i})\_{t\geq 0,i\in\mathbb{N}} is i.i.d. with law λϑ\lambda\_{\vartheta}, and (εti)t≥1,i∈ℕ(\varepsilon\_{t}^{i})\_{t\geq 1,i\in\mathbb{N}} is i.i.d. with law λε\lambda\_{\varepsilon}.
* (iii)

  ε10\varepsilon\_{1}^{0} is independent of ⋁i∈ℕG0i\bigvee\_{i\in\mathbb{N}}{\mathcal{}G}\_{0}^{i} with law p1p\_{1}, whereas for every t≥2t\geq 2 εt0\varepsilon\_{t}^{0} is conditionally independent of ⋁i∈ℕGt−1i\bigvee\_{i\in\mathbb{N}}{\mathcal{}G}\_{t-1}^{i} given Ft−10{\mathcal{}F}\_{t-1}^{0} (see [kallenberg2002foundations, Lemma 6.9]),
  satisfying

  |  |  |  |
  | --- | --- | --- |
  |  | ℒℙ(εt0|Ft−10)=pt(⋅|ε1:t−10)ℙ-a.s.\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{t}^{0}|{\mathcal{}F}\_{t-1}^{0})=p\_{t}(\,\cdot\,|\varepsilon\_{1:t-1}^{0})\quad\mbox{$\mathbb{P}$-a.s.} |  |

We note that when 𝔓0\mathfrak{P}^{0} is a singleton (i.e., without uncertainty), the resulting probabilistic framework
coincides with the setting in [carmona2023model, Section 2.1.2] and is also similar to the one in [motte2022mean, Section 2].

We introduce a dynamical system of mean-field models with indistinguishable NN-agents under common noise uncertainty and define the corresponding robust optimization problem. To this end, let us introduce the following elementary components:

###### Definition 2.4.

Let SS and AA be nonempty compact Polish spaces, representing the state and action spaces, respectively.

* (i)

  F:S×A×P​(S×A)×E×E0→S\operatorname{F}:S\times A\times{\mathcal{}P}(S\times A)\times E\times E^{0}\to S is a Borel measurable transition function describing the dynamics of each of the NN-agents as well as the mean-field model.
* (ii)

  r:S×A×P​(S×A)→ℝr:S\times A\times{\mathcal{}P}(S\times A)\to\mathbb{R} is a Borel measurable one-step reward function.
* (iii)

  β∈[0,1)\beta\in[0,1) is a discount factor.

###### Definition 2.5 (NN-agent model).

Recall that for each i∈ℕi\in\mathbb{N}, F0i=σ​(γi){\mathcal{}F}\_{0}^{i}=\sigma(\gamma^{i}) (see Definition [2.1](https://arxiv.org/html/2511.04515v1#S2.Thmthm1 "Definition 2.1 (Filtrations). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Denote for every i∈ℕi\in\mathbb{N} by LF0i0​(S)L^{0}\_{{\mathcal{}F}\_{0}^{i}}(S) the set of all F0i{\mathcal{}F}\_{0}^{i} measurable random variables with values in SS.

1. (i)

   Denote by Π\Pi the set of all open-loop policies (πt)t≥0(\pi\_{t})\_{t\geq 0} in the sense that πt:G×Θt+1×Et×(E0)t→A\pi\_{t}:G\times\Theta^{t+1}\times E^{t}\times(E^{0})^{t}\to A is a Borel measurable function for all t≥0t\geq 0. Given (πt)∈Π(\pi\_{t})\in\Pi, the action process of agent i∈ℕi\in\mathbb{N} is given by the open-loop control

   |  |  |  |
   | --- | --- | --- |
   |  | ati,π:=πt​(γi,ϑ0:ti,ε1:ti,ε1:t0)t≥1,with​a0i,π:=π0​(γi,ϑ0i).\hskip 10.00002pta\_{t}^{i,\pi}:=\pi\_{t}(\gamma^{i},\vartheta\_{0:t}^{i},\varepsilon\_{1:t}^{i},\varepsilon\_{1:t}^{0})\quad t\geq 1,\quad\mbox{with}\;\;a\_{0}^{i,\pi}:=\pi\_{0}(\gamma^{i},\vartheta\_{0}^{i}). |  |

   In other words, (ati,π)t≥0(a\_{t}^{i,\pi})\_{t\geq 0} is a 𝔾i\mathbb{G}^{i} adapted process (see Definition [2.1](https://arxiv.org/html/2511.04515v1#S2.Thmthm1 "Definition 2.1 (Filtrations). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).
2. (ii)

   Fix the initial state ξi∈LF0i0​(S)\xi^{i}\in L^{0}\_{{\mathcal{}F}\_{0}^{i}}(S) of agent ii. Given N∈ℕN\in\mathbb{N} and (πt)t≥0∈Π(\pi\_{t})\_{t\geq 0}\in\Pi, the state and action processes of agent i=1,…,Ni=1,\dots,N in the NN-agent model under ℙ∈Q\mathbb{P}\in{\mathcal{}Q} are given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (2.3) |  | {s0i,N,π:=ξi,st+1i,N,π:=F⁡(sti,N,π,ati,π,1N​∑j=1Nδ(stj,N,π,atj,π),εt+1i,εt+10)t≥0.\displaystyle\hskip 10.00002pt\left\{\begin{aligned} &s\_{0}^{i,N,\pi}:=\xi^{i},\\ &s\_{t+1}^{i,N,\pi}:=\operatorname{F}(s^{i,N,\pi}\_{t},a^{i,\pi}\_{t},\mbox{$\frac{1}{N}\sum\_{j=1}^{N}\delta\_{(s^{j,N,\pi}\_{t},a^{j,\pi}\_{t})}$},\varepsilon\_{t+1}^{i},\varepsilon\_{t+1}^{0})\quad t\geq 0.\end{aligned}\right. |  |

   Here we observe that both the law of the initial state and action (s0i,N,π,a0i,π)(s\_{0}^{i,N,\pi},a\_{0}^{i,\pi}) and the law of the idiosyncratic noise process (εti)t≥0(\varepsilon\_{t}^{i})\_{t\geq 0} do not depend the choice of ℙ∈Q\mathbb{P}\in{\mathcal{}Q} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)). In contrast, the law of (sti,N,π,ati,π)(s\_{t}^{i,N,\pi},a\_{t}^{i,\pi}) for t≥1t\geq 1 depends on this choice, due to the model uncertainty in (εt0)t≥1(\varepsilon\_{t}^{0})\_{t\geq 1}.
3. (iii)

   The contribution of agent ii to the social planner’s gain over an infinite horizon under ℙ∈Q\mathbb{P}\in{\mathcal{}Q} is defined by

   |  |  |  |
   | --- | --- | --- |
   |  | Ri,N,π:=∑t=0∞βt​r​(sti,N,π,ati,π,1N​∑j=1Nδ(stj,N,π,atj,π))i=1,…,N.\quad R^{i,N,\pi}:=\sum\_{t=0}^{\infty}\beta^{t}r(s\_{t}^{i,N,\pi},a\_{t}^{i,\pi},\mbox{$\frac{1}{N}\sum\_{j=1}^{N}\delta\_{(s^{j,N,\pi}\_{t},a^{j,\pi}\_{t})}$})\quad i=1,\dots,N. |  |

   Then the social planner’s worst-case expected gain under the common noise uncertainty is

   |  |  |  |
   | --- | --- | --- |
   |  | JN,π:=infℙ∈Q𝔼ℙ​[RN,π]where​RN,π:=1N​∑i=1NRi,N,π,{\mathcal{}J}^{N,\pi}:=\inf\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}[R^{N,\pi}]\quad\mbox{where}\;\;R^{N,\pi}:=\frac{1}{N}\sum\_{i=1}^{N}R^{i,N,\pi}, |  |

   and the resulting NN-agent optimization problem is given by
   VN:=supπ∈ΠJN,π.V^{N}:=\sup\_{\pi\in\Pi}{\mathcal{}J}^{N,\pi}. This problem is a robust analog of the classical NN-agent optimization problem of [carmona2023model, motte2022mean].

In light of the propagation of chaos argument, we expect and aim to show that the asymptotic version of the NN-agent problem in Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), as N→∞N\to\infty, is given by the following:

###### Definition 2.6 (MFC model).

For each i∈ℕi\in\mathbb{N}, let ξi∈LF0i0​(S)\xi^{i}\in L\_{{\mathcal{}F}\_{0}^{i}}^{0}(S) be the fixed initial state of agent ii; see Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii).

1. (i)

   Given (πt)t≥0∈Π(\pi\_{t})\_{t\geq 0}\in\Pi, the state process of agent i∈ℕi\in\mathbb{N} in the infinite population model under ℙ∈Q\mathbb{P}\in{\mathcal{}Q} is governed by the conditional McKean–Vlasov dynamics:

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (2.4) |  | {s0i,π,ℙ:=ξi,st+1i,π,ℙ:=F⁡(sti,π,ℙ,ati,π,ℙ(sti,π,ℙ,ati,π)0,εt+1i,εt+10)t≥0,\displaystyle\hskip 10.00002pt\left\{\begin{aligned} s\_{0}^{i,\pi,\mathbb{P}}&:=\xi^{i},\\ s\_{t+1}^{i,\pi,\mathbb{P}}&:=\operatorname{F}(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t},\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})},\varepsilon\_{t+1}^{i},\varepsilon\_{t+1}^{0})\quad t\geq 0,\end{aligned}\right. |  |

   where (ati,π)t≥0(a^{i,\pi}\_{t})\_{t\geq 0} is the open-loop control of agent ii as defined in Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i), and ℙ(sti,π,ℙ,ati,π)0\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})} is the conditional joint law of (sti,π,ℙ,ati,π)(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t}) under ℙ\mathbb{P} given the common noise trajectory ε1:t0\varepsilon\_{1:t}^{0}, i.e.,

   |  |  |  |
   | --- | --- | --- |
   |  | ℙ(sti,π,ℙ,ati,π)0:=ℒℙ​((sti,π,ℙ,ati,π)|ε1:t0)t≥1\hskip 10.00002pt\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})}:=\mathscr{L}\_{\mathbb{P}}\big((s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})|\varepsilon\_{1:t}^{0}\big)\quad t\geq 1 |  |

   with the convention that ℙ(s0i,π,ℙ,a0i,π)0:=ℒℙ​((s0i,π,ℙ,a0i,π))\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{0},a^{i,\pi}\_{0})}:=\mathscr{L}\_{\mathbb{P}}((s^{i,\pi,\mathbb{P}}\_{0},a^{i,\pi}\_{0})). Analogously, for every t≥1t\geq 1 let ℙsti,π,ℙ0\mathbb{P}^{0}\_{s^{i,\pi,\mathbb{P}}\_{t}} be the conditional law of sti,π,ℙs^{i,\pi,\mathbb{P}}\_{t} under ℙ\mathbb{P} given the common noise trajectory ε1:t0\varepsilon\_{1:t}^{0} with the convention that ℙs0i,π,ℙ0:=ℒℙ​(s0i,π,ℙ)\mathbb{P}^{0}\_{s^{i,\pi,\mathbb{P}}\_{0}}:=\mathscr{L}\_{\mathbb{P}}(s^{i,\pi,\mathbb{P}}\_{0}).
2. (ii)

   The contribution of agent ii to the social planner’s gain under ℙ∈Q\mathbb{P}\in{\mathcal{}Q} is defined by

   |  |  |  |
   | --- | --- | --- |
   |  | Ri,π,ℙ:=∑t=0∞βt​r​(sti,π,ℙ,ati,π,ℙ(sti,π,ℙ,ati,π)0)i∈ℕ.\quad R^{i,\pi,\mathbb{P}}:=\sum\_{t=0}^{\infty}\beta^{t}r(s\_{t}^{i,\pi,\mathbb{P}},a\_{t}^{i,\pi},\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})})\quad i\in\mathbb{N}. |  |

   Then the social planner’s worst-case expected gain under the common noise uncertainty is

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (2.5) |  | Jπ:=infℙ∈Q𝔼ℙ​[Rπ,ℙ],where​Rπ,ℙ:=𝔼ℙ0​[Ri,π,ℙ]=𝔼ℙ0​[R1,π,ℙ]i∈ℕ,\displaystyle\qquad{\mathcal{}J}^{\pi}:=\inf\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}[R^{\pi,\mathbb{P}}],\qquad\mbox{where}\;\;R^{\pi,\mathbb{P}}:=\mathbb{E}^{\mathbb{P}^{0}}[R^{i,\pi,\mathbb{P}}]=\mathbb{E}^{\mathbb{P}^{0}}[R^{1,\pi,\mathbb{P}}]\quad i\in\mathbb{N}, |  |

   where 𝔼ℙ0​[⋅]\mathbb{E}^{\mathbb{P}^{0}}[\cdot] denotes the conditional expectation under ℙ\mathbb{P} given (εt0)t≥0(\varepsilon^{0}\_{t})\_{t\geq 0} and the quantity Rπ,ℙR^{\pi,\mathbb{P}} is independent of the choice of ii due to the indistinguishability of agents. The resulting robust MFC problem is then defined as
   V:=supπ∈ΠJπ.V:=\sup\_{\pi\in\Pi}{\mathcal{}J}^{\pi}.

The main goal of this section is to rigorously connect the NN-agent model in Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") with the MFC model in Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

We impose the following conditions on the basic components given in Definition [2.4](https://arxiv.org/html/2511.04515v1#S2.Thmthm4 "Definition 2.4. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

###### Assumption 2.7.

The following conditions hold:

* (i)

  There exists some CF>0C\_{{\operatorname{F}}}>0 such that for every s,s~∈Ss,\tilde{s}\in S, a∈Aa\in A, Λ,Λ~∈P​(S×A)\Lambda,\tilde{\Lambda}\in{\mathcal{}P}(S\times A), and e0∈E0e^{0}\in E^{0}

  |  |  |  |
  | --- | --- | --- |
  |  | ∫EdS​(F⁡(s,a,Λ,e,e0),F⁡(s~,a,Λ~,e,e0))​λε​(d​e)≤CF​(dS​(s,s~)+𝒲P​(S×A)​(Λ,Λ~)),\displaystyle\hskip 30.00005pt\int\_{E}d\_{S}\big(\operatorname{F}(s,a,\Lambda,e,e^{0}),\operatorname{F}(\tilde{s},a,\tilde{\Lambda},e,e^{0})\big)\lambda\_{\varepsilon}(de)\leq C\_{{\operatorname{F}}}\big(d\_{S}(s,\tilde{s})+\mathcal{W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})\big), |  |

  where λε\lambda\_{\varepsilon} is given in Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i).
* (ii)

  There exists Cr>0C\_{{r}}>0 such that for every s,s~∈Ss,\tilde{s}\in S, a∈Aa\in A, and Λ,Λ~∈P​(S×A)\Lambda,\tilde{\Lambda}\in{\mathcal{}P}(S\times A)

  |  |  |  |
  | --- | --- | --- |
  |  | |r​(s,a,Λ)|≤Cr,|r​(s,a,Λ)−r​(s~,a,Λ~)|≤Cr​(dS​(s,s~)+𝒲P​(S×A)​(Λ,Λ~)).\hskip 30.00005pt|r(s,a,\Lambda)|\leq C\_{{r}},\qquad|r(s,a,\Lambda)-r(\tilde{s},a,\tilde{\Lambda})|\leq C\_{{r}}\big(d\_{S}(s,\tilde{s})+\mathcal{W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})\big). |  |
* (iii)

  β\beta is in [0,1∧(2​CF)−1)[0,1\wedge(2C\_{{\operatorname{F}}})^{-1}).

For every N∈ℕN\in\mathbb{N}, we define the following quantity

|  |  |  |  |
| --- | --- | --- | --- |
| (2.6) |  | MN:=supt≥0supπ∈Πsupℙ∈Q𝔼ℙ​[WP​(S×A)​(1N​∑i=1Nδ(sti,π,ℙ,ati,π),ℙ(st1,π,ℙ,at1,π)0)],\displaystyle M\_{N}:=\sup\_{t\geq 0}\sup\_{\pi\in\Pi}\sup\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\bigg[{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}\Big(\frac{1}{N}\sum\_{i=1}^{N}\delta\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})},\,\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})}\Big)\bigg], |  |

where for each j=1,⋯,Nj=1,\cdots,N, (stj,π,ℙ,atj,π)t≥0(s^{j,\pi,\mathbb{P}}\_{t},a^{j,\pi}\_{t})\_{t\geq 0} are the state and action processes of agent jj under ℙ\mathbb{P} in the MFC model, and for each t≥0t\geq 0 ℙ(st1,π,ℙ,at1,π)0\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})} is the conditional joint law of (st1,π,ℙ,at1,π)(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t}) under ℙ\mathbb{P} given the common noise ε1:t0\varepsilon\_{1:t}^{0} (see Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). By the indistinguishability of the NN agents, ℙ(st1,π,ℙ,at1,π)0\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})} can equivalently be replaced by ℙ(stj,π,ℙ,atj,π)0\mathbb{P}^{0}\_{(s^{j,\pi,\mathbb{P}}\_{t},a^{j,\pi}\_{t})} for any j∈ℕj\in\mathbb{N}.

The following estimates on the sequence (MN)N∈ℕ(M\_{N})\_{N\in\mathbb{N}}, as defined in ([2.6](https://arxiv.org/html/2511.04515v1#S2.E6 "In 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), follow from standard applications of the non asymptotic bounds for the convergence rate of empirical measures in Wasserstein distance (see [fournier2015rate, Theorem 1], [boissard2014mean, Corollary 1.2]).

###### Lemma 2.8.

Denote by ΔS×A∈[0,∞)\Delta\_{S\times A}\in[0,\infty) the diameter of S×AS\times A.
Then the following hold:

* (i)

  If S×A⊂ℝdS\times A\subset\mathbb{R}^{d} for some d∈ℕd\in\mathbb{N}, then for any q>2q>2 there exists some constant C>0C>0 (that depends only on dd and qq) such that for every N∈ℕN\in\mathbb{N},

  |  |  |  |
  | --- | --- | --- |
  |  | MN≤C​ΔS×A⋅α​(N)<∞,\displaystyle M\_{N}\leq C\Delta\_{S\times A}\cdot\alpha(N)<\infty, |  |

  where α:ℕ∋N↦α​(N)∈(0,∞)\alpha:\mathbb{N}\ni N\mapsto\alpha(N)\in(0,\infty) is given as follows: α​(N):=N−1/2\alpha(N):=N^{-1/2} for d=1d=1; α​(N):=N−1/2​log⁡(1+N)\alpha(N):=N^{-1/2}\log(1+N) for d=2d=2; α​(N):=N−1/d​log⁡(1+N)\alpha(N):=N^{-1/d}\log(1+N) for d≥3d\geq 3.
* (ii)

  If for every δ>0\delta>0 there exist some constants kS×A>0k\_{S\times A}>0 and q>2q>2 such that the minimal number of balls with radius δ\delta covering S×AS\times A, denoted by n¯​(S×A,δ)∈ℕ\underline{n}(S\times A,\delta)\in\mathbb{N}, satisfies n¯​(S×A,δ)≤kS×A​(ΔS×A⋅δ−1)q\underline{n}(S\times A,\delta)\leq k\_{S\times A}\big({\Delta\_{S\times A}}\cdot{\delta}^{-1}\big)^{q}, then there exists some C>0C>0 (that depends only on kS×Ak\_{S\times A} and qq) such that for every N∈ℕN\in\mathbb{N},

  |  |  |  |
  | --- | --- | --- |
  |  | MN≤C​ΔS×A⋅N−1q<∞.M\_{N}\leq C\Delta\_{S\times A}\cdot N^{-\frac{1}{q}}<\infty. |  |

By using Lemma [2.8](https://arxiv.org/html/2511.04515v1#S2.Thmthm8 "Lemma 2.8. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), we can obtain a rate of convergence when approximating the NN-agent model by the MFC model under model uncertainty in the common noise process.

###### Theorem 2.9.

Suppose that Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") holds. Moreover, we assume that ΔS×A\Delta\_{S\times A} satisfies one of the two settings imposed in Lemma [2.8](https://arxiv.org/html/2511.04515v1#S2.Thmthm8 "Lemma 2.8. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Then it holds that for every N∈ℕN\in\mathbb{N}, i=1,…,Ni=1,\dots,N, and t≥0t\geq 0

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | supπ∈Πsupℙ∈Q𝔼ℙ​[dS​(sti,N,π,sti,π,ℙ)]=O​(MN),\displaystyle\sup\_{\pi\in\Pi}\sup\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\big[d\_{S}(s^{i,N,\pi}\_{t},s^{i,\pi,\mathbb{P}}\_{t})\big]=O(M\_{N}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | supπ∈Πsupℙ∈Q𝔼ℙ​[WP​(S×A)​(1N​∑j=1Nδ(stj,N,π,atj,π),ℙ(sti,π,ℙ,ati,π)0)]=O​(MN),\displaystyle\sup\_{\pi\in\Pi}\sup\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\bigg[{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}\bigg(\frac{1}{N}\sum\_{j=1}^{N}\delta\_{(s^{j,N,\pi}\_{t},a^{j,\pi}\_{t})},\,\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})}\bigg)\bigg]=O(M\_{N}), |  |

where O​(⋅)O(\cdot) is the Landau symbol. Moreover, there exists some constant C>0C>0 (that depends only on CF,CrC\_{\operatorname{F}},C\_{r} and β\beta) such that for N∈ℕN\in\mathbb{N} sufficiently large

|  |  |  |  |
| --- | --- | --- | --- |
| (2.9) |  | supπ∈Π|JN,π−Jπ|≤C​MN,\displaystyle\sup\_{\pi\in\Pi}|{\mathcal{}J}^{N,\pi}-{\mathcal{}J}^{\pi}|\leq CM\_{N}, |  |

which ensures that |VN−V|=O​(MN)|V^{N}-V|=O(M\_{N}). Consequently, any ε\varepsilon-optimal policy for the robust MFC problem VV (see Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) is O​(ε)O(\varepsilon)-optimal for the NN-agent robust optimization problem VNV^{N} (see Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) if NN is sufficiently large such that MN=O​(ε)M\_{N}=O(\varepsilon). Conversely, any ε\varepsilon-optimal policy for VNV^{N} is O​(ε)O(\varepsilon)-optimal for VV if N∈ℕN\in\mathbb{N} is sufficiently large such that MN=O​(ε)M\_{N}=O(\varepsilon).

The proofs of Lemma [2.8](https://arxiv.org/html/2511.04515v1#S2.Thmthm8 "Lemma 2.8. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and Theorem [2.9](https://arxiv.org/html/2511.04515v1#S2.Thmthm9 "Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") can be found in Section [4](https://arxiv.org/html/2511.04515v1#S4 "4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty").

###### Remark 2.10.

Theorem [2.9](https://arxiv.org/html/2511.04515v1#S2.Thmthm9 "Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") can be viewed as a robust analog of [motte2022mean, Theorem 2.1]. The overall proof roadmap follows the arguments in the reference, where the convergence rate of the empirical measure (see Lemma [2.8](https://arxiv.org/html/2511.04515v1#S2.Thmthm8 "Lemma 2.8. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) plays a key role. Moreover, the Lipschitz conditions on the one-step reward and system functions in Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i), (ii) (denoted as 𝐇𝐟𝐥𝐢𝐩{\bf\operatorname{\bf Hf}\_{\operatorname{\bf lip}}} and 𝐇𝐅𝐥𝐢𝐩{\bf\operatorname{\bf HF}\_{\operatorname{\bf lip}}} therein), together with a certain condition on the discount factor (similar to Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)), are imposed. While our setting is more rigid due to the uncertainty measures set Q{\mathcal{}Q}, we are able to obtain the propagation of chaos result by establishing the convergence rate of the empirical measure uniformly over all probability measures ℙ∈Q\mathbb{P}\in{\mathcal{}Q}.

### 2.3. Lifted robust Markov decision processes on the space of probability measures

Theorem [2.9](https://arxiv.org/html/2511.04515v1#S2.Thmthm9 "Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") shows that the robust MFC model in Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") serves as a macroscopic approximation of the robust NN-agent optimization model in Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").
By definition of the conditional McKean-Vlasov dynamics ([2.4](https://arxiv.org/html/2511.04515v1#S2.E4 "In item (i) ‣ Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and the social planner’s worst-case expected gain ([2.5](https://arxiv.org/html/2511.04515v1#S2.E5 "In item (ii) ‣ Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), we can without loss of generality consider only one representative agent.

Accordingly, we suppress the index i∈ℕi\in\mathbb{N} representing individual agents, and denote the representative agent’s components as follows: the initial information is given by γ\gamma, the randomization source process by (ϑt)t≥0(\vartheta\_{t})\_{t\geq 0}, the idiosyncratic noise by (εt)t≥1(\varepsilon\_{t})\_{t\geq 1}, and the information processes by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.10) |  | 𝔽:=(Ft)t≥0with F0:=σ​(γ) and Ft:=σ​(γ,ϑ0:t−1,ε1:t,ε1:t0) for all t≥1;𝔾:=(Gt)t≥0with Gt:=Ft∨σ​(ϑt) for all t≥0 so that 𝔽⊆𝔾,\displaystyle\begin{aligned} \mathbb{F}&:=({\mathcal{}F}\_{t})\_{t\geq 0}\quad\mbox{with ${\mathcal{}F}\_{0}:=\sigma(\gamma)$ and ${\mathcal{}F}\_{t}:=\sigma(\gamma,\vartheta\_{0:t-1},\varepsilon\_{1:t},\varepsilon\_{1:t}^{0})$ for all $t\geq 1$;}\\ \mathbb{G}&:=({\mathcal{}G}\_{t})\_{t\geq 0}\quad\mbox{with ${\mathcal{}G}\_{t}:={\mathcal{}F}\_{t}\vee\sigma(\vartheta\_{t})$ for all $t\geq 0$ so that $\mathbb{F}\subseteq\mathbb{G}$},\end{aligned} |  |

see Definition [2.1](https://arxiv.org/html/2511.04515v1#S2.Thmthm1 "Definition 2.1 (Filtrations). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). The initial state is then given by ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S).

Moreover, we define by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.11) |  | A:={a:=(at)t≥0:a is 𝔾 adapted and satisfies at=πt​(γ,ϑ0:t,ε1:t,ε1:t0) for t≥1and a0=π0​(γ,ϑ0) w.r.t. some π∈Π},\displaystyle{\mathcal{}A}:=\left\{a:=(a\_{t})\_{t\geq 0}:\begin{aligned} &\,\mbox{$a$ is $\mathbb{G}$ adapted and satisfies $a\_{t}=\pi\_{t}(\gamma,\vartheta\_{0:t},\varepsilon\_{1:t},\varepsilon^{0}\_{1:t})$ for $t\geq 1$}\\ &\,\mbox{and $a\_{0}=\pi\_{0}(\gamma,\vartheta\_{0})$ w.r.t.\;some $\pi\in\Pi$}\end{aligned}\right\}, |  |

the set of open-loop controls of the representative agent (see Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i) for the notation Π\Pi).

Given a∈Aa\in{\mathcal{}A}, the state process of the representative agent in the infinite population model under ℙ∈Q\mathbb{P}\in{\mathcal{}Q} evolves according to the conditional McKean-Vlasov dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.12) |  | st+1ξ,a,ℙ:=F⁡(stξ,a,ℙ,at,ℙ(stξ,a,ℙ,at)0,εt+1,εt+10)for t≥0,with s0ξ,a,ℙ:=ξ,\displaystyle\hskip 10.00002pts\_{t+1}^{\xi,a,\mathbb{P}}:=\operatorname{F}(s^{\xi,a,\mathbb{P}}\_{t},a\_{t},\mathbb{P}^{0}\_{(s^{\xi,a,\mathbb{P}}\_{t},a\_{t})},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0})\quad\mbox{for $t\geq 0$},\;\;\mbox{with $\;\;s\_{0}^{\xi,a,\mathbb{P}}:=\xi,$} |  |

where ℙ(stξ,a,ℙ,at)0\mathbb{P}^{0}\_{(s^{\xi,a,\mathbb{P}}\_{t},a\_{t})} is the conditional joint law of (stξ,a,ℙ,at)(s^{\xi,a,\mathbb{P}}\_{t},a\_{t}) under ℙ\mathbb{P} given ε1:t0\varepsilon^{0}\_{1:t} for t≥1t\geq 1, with the convention that ℙ(s0ξ,a,ℙ,a0)0:=ℒℙ​((s0ξ,a,ℙ,a0))\mathbb{P}^{0}\_{(s^{\xi,a,\mathbb{P}}\_{0},a\_{0})}:=\mathscr{L}\_{\mathbb{P}}((s^{\xi,a,\mathbb{P}}\_{0},a\_{0})). Here we note that (stξ,a,ℙ)t≥0(s\_{t}^{\xi,a,\mathbb{P}})\_{t\geq 0} is 𝔽\mathbb{F} adapted and (ℙ(stξ,a,ℙ,at)0)t≥0(\mathbb{P}^{0}\_{(s^{\xi,a,\mathbb{P}}\_{t},a\_{t})})\_{t\geq 0} is 𝔽0\mathbb{F}^{0} adapted (see Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty") (ii)).

Then the social planner’s worst-case expected gain under the common noise uncertainty is

|  |  |  |  |
| --- | --- | --- | --- |
| (2.13) |  | Ja​(ξ):=infℙ∈Q𝔼ℙ​[Ra,ℙ​(ξ)],where​Ra,ℙ​(ξ):=𝔼ℙ0​[∑t=0∞βt​r​(stξ,a,ℙ,at,ℙ(stξ,a,ℙ,at)0)].\displaystyle\;\;{\mathcal{}J}^{a}(\xi):=\inf\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}[R^{a,\mathbb{P}}(\xi)],\quad\mbox{where}\;\;R^{a,\mathbb{P}}(\xi):=\mathbb{E}^{\mathbb{P}^{0}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}r(s\_{t}^{\xi,a,\mathbb{P}},a\_{t},\mathbb{P}^{0}\_{(s^{\xi,a,\mathbb{P}}\_{t},a\_{t})})\bigg]. |  |

Accordingly, the robust MFC problem of the social planner is defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.14) |  | V​(ξ):=supa∈AJa​(ξ),ξ∈LF00​(S).\displaystyle V(\xi):=\sup\_{a\in{\mathcal{}A}}{\mathcal{}J}^{a}(\xi),\quad\;\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S). |  |

This formulation coincides with Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (by suppressing the agent index ii).

We now show how the robust MFC problem given in ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) can be lifted to a robust Markov decision process (MDP) under model uncertainty in the space of probability measures. Given ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S), a∈Aa\in{\mathcal{}A}, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, we define the following 𝔽0\mathbb{F}^{0} adapted processes:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.15) |  | (μtξ,a,ℙ)t≥0:=(ℙstξ,a,ℙ0)t≥0⊆P​(S),\displaystyle(\mu\_{t}^{\xi,a,\mathbb{P}})\_{t\geq 0}:=(\mathbb{P}^{0}\_{s\_{t}^{\xi,a,\mathbb{P}}})\_{t\geq 0}\subseteq{\mathcal{}P}(S), |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (2.16) |  | (Λtξ,a,ℙ)t≥0:=(ℙ(stξ,a,ℙ,at)0)t≥0⊆P​(S×A).\displaystyle(\Lambda\_{t}^{\xi,a,\mathbb{P}})\_{t\geq 0}:=(\mathbb{P}^{0}\_{(s\_{t}^{\xi,a,\mathbb{P}},a\_{t})})\_{t\geq 0}\subseteq{\mathcal{}P}(S\times A). |  |

We refer to ([2.15](https://arxiv.org/html/2511.04515v1#S2.E15 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.16](https://arxiv.org/html/2511.04515v1#S2.E16 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) as the lifted state and lifted action processes, respectively. Note that the lifted processes satisfy the following marginal constraint: ℙ\mathbb{P}-a.s.,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.17) |  | pjS⁡(Λtξ,a,ℙ)=μtξ,a,ℙfor all t≥0,\displaystyle\operatorname{pj}\_{S}(\Lambda\_{t}^{\xi,a,\mathbb{P}})=\mu\_{t}^{\xi,a,\mathbb{P}}\quad\mbox{for all $t\geq 0$,} |  |

where pjS:P(S×A)∋Λ↦pjS(Λ):=Λ(⋅×A)∈P(S)\operatorname{pj}\_{S}:{\mathcal{}P}(S\times A)\ni\Lambda\mapsto\operatorname{pj}\_{S}(\Lambda):=\Lambda(\cdot\times A)\in{\mathcal{}P}(S) denotes the projection function that maps Λ\Lambda onto its marginal on SS.

Based on this observation, we first characterize the dynamics of the lifted state processes.
To that end, let us introduce some notation and functions defined on the spaces of probability measure, P​(S){\mathcal{}P}(S) and P​(S×A){\mathcal{}P}(S\times A) (we refer to them as the ‘lifted’ spaces), which is convenient to characterize the dynamics and then to obtain the lifted dynamic programming principle.

###### Definition 2.11.

Let λε∈P​(E)\lambda\_{\varepsilon}\in{\mathcal{}P}(E) be given in Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Moreover, let F\operatorname{F}
and rr be the transition function and one-step reward function, respectively, as defined in Definition [2.4](https://arxiv.org/html/2511.04515v1#S2.Thmthm4 "Definition 2.4. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i).

1. (i)

   Denote by

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔘:P​(S)∋μ↠𝔘​(μ):={Λ∈P​(S×A):pjS⁡(Λ)=μ}⊆P​(S×A)\displaystyle\hskip 20.00003pt\mathfrak{U}:{\mathcal{}P}(S)\ni\mu\twoheadrightarrow\mathfrak{U}(\mu):=\{\Lambda\in{\mathcal{}P}(S\times A):\operatorname{pj}\_{S}(\Lambda)=\mu\}\subseteq{\mathcal{}P}(S\times A) |  |

   the correspondence (i.e., a set-valued map) inducing the marginal constraint on SS. Moreover, denote by gr⁡(𝔘)\operatorname{gr}(\mathfrak{U}) the graph of 𝔘\mathfrak{U}, i.e., gr⁡(𝔘):={(μ,Λ)∈P​(S)×P​(S×A):Λ∈𝔘​(μ)}.\operatorname{gr}(\mathfrak{U}):=\{(\mu,\Lambda)\in{\mathcal{}P}(S)\times{\mathcal{}P}(S\times A):\Lambda\in\mathfrak{U}(\mu)\}.
2. (ii)

   Denote by F¯:gr⁡(𝔘)×E0∋(μ,Λ,e0)↦F¯​(μ,Λ,e0)∈P​(S)\overline{\mathrm{F}}:\operatorname{gr}(\mathfrak{U})\times E^{0}\ni(\mu,\Lambda,e^{0})\mapsto\overline{\mathrm{F}}(\mu,\Lambda,e^{0})\in{\mathcal{}P}(S) the lifted transition function given by

   |  |  |  |
   | --- | --- | --- |
   |  | F¯(μ,Λ,e0)(ds′):=((Λ⊗λε)∘F(⋅,⋅,Λ,⋅,e0)−1)(ds′),\displaystyle\hskip 10.00002pt\overline{\mathrm{F}}(\mu,\Lambda,e^{0})(ds^{\prime}):=\big((\Lambda\otimes\lambda\_{\varepsilon})\circ\operatorname{F}(\cdot,\cdot,\Lambda,\cdot,e^{0})^{-1}\big)(ds^{\prime}), |  |

   i.e., the push-forward of Λ⊗λε∈P​(S×A×E)\Lambda\otimes\lambda\_{\varepsilon}\in{\mathcal{}P}(S\times A\times E) by F⁡(⋅,⋅,Λ,⋅,e0):S×A×E→S\operatorname{F}(\cdot,\cdot,\Lambda,\cdot,e^{0}):S\times A\times E\to S.
3. (iii)

   Let p¯:gr⁡(𝔘)×P​(E0)∋(μ,Λ,p)↦p¯​(d​μ′|μ,Λ,p)∈P​(P​(S))\overline{p}:\operatorname{gr}(\mathfrak{U})\times{\mathcal{}P}(E^{0})\ni(\mu,\Lambda,p)\mapsto\overline{p}(d\mu^{\prime}|\mu,\Lambda,p)\in{\mathcal{}P}({\mathcal{}P}(S)) be a kernel defined by

   |  |  |  |
   | --- | --- | --- |
   |  | p¯​(d​μ′|μ,Λ,p):=(p∘F¯​(μ,Λ,⋅)−1)​(d​μ′),\displaystyle\overline{p}(d\mu^{\prime}|\mu,\Lambda,p):=\big(p\circ\overline{\mathrm{F}}(\mu,\Lambda,\cdot)^{-1}\big)(d\mu^{\prime}), |  |

   i.e., the push-forward of p∈P​(E0){p}\in{\mathcal{}P}(E^{0}) by F¯​(μ,Λ,⋅):E0→P​(S)\overline{\mathrm{F}}(\mu,\Lambda,\cdot):E^{0}\to{\mathcal{}P}(S).
4. (iv)

   Denote by r¯:gr⁡(𝔘)∋(μ,Λ)↦r¯​(μ,Λ)∈ℝ\overline{r}:\operatorname{gr}(\mathfrak{U})\ni(\mu,\Lambda)\mapsto\overline{r}(\mu,\Lambda)\in\mathbb{R} the lifted reward function defined by

   |  |  |  |
   | --- | --- | --- |
   |  | r¯​(μ,Λ):=∫S×Ar​(s,a,Λ)​Λ​(d​s,d​a).\overline{r}(\mu,\Lambda):=\int\_{S\times A}r(s,a,\Lambda)\Lambda(ds,da). |  |

The following lemma shows that indeed (μtξ,a,ℙ)t≥0(\mu^{\xi,a,\mathbb{P}}\_{t})\_{t\geq 0} given in ([2.15](https://arxiv.org/html/2511.04515v1#S2.E15 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) can be seen as an MDP on the space of probability measures.

###### Proposition 2.12.

Let F¯\overline{\operatorname{F}} and p¯\overline{p} be given in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Let ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S), a∈A,a\in{\mathcal{}A}, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q} be given where ℙ\mathbb{P} is induced by some couple (pt)t≥1∈𝒦0(p\_{t})\_{t\geq 1}\in\mathcal{K}^{0} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Then the lifted state and action processes (μtξ,a,ℙ)t≥0(\mu\_{t}^{\xi,a,\mathbb{P}})\_{t\geq 0} and (Λtξ,a,ℙ)t≥0(\Lambda\_{t}^{\xi,a,\mathbb{P}})\_{t\geq 0} (see ([2.15](https://arxiv.org/html/2511.04515v1#S2.E15 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), ([2.16](https://arxiv.org/html/2511.04515v1#S2.E16 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))) satisfy for every t≥0t\geq 0, ℙ\mathbb{P}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.18) |  | μt+1ξ,a,ℙ=F¯​(pjS⁡(Λtξ,a,ℙ),Λtξ,a,ℙ,εt+10),\displaystyle\mu\_{t+1}^{\xi,a,\mathbb{P}}=\overline{\mathrm{F}}(\operatorname{pj}\_{S}(\Lambda\_{t}^{\xi,a,\mathbb{P}}),\,\Lambda\_{t}^{\xi,a,\mathbb{P}},\,\varepsilon\_{t+1}^{0}), |  |

which implies that ℙ\mathbb{P}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.19) |  | ℒℙ​(μ1ξ,a,ℙ)=p¯(⋅|pjS(Λ0ξ,a,ℙ),Λ0ξ,a,ℙ,p1(⋅)),ℒℙ​(μt+1ξ,a,ℙ)=p¯(⋅|pjS(Λtξ,a,ℙ),Λtξ,a,ℙ,pt+1(⋅|ε1:t0))for all t≥1.\displaystyle\begin{aligned} \mathscr{L}\_{\mathbb{P}}(\mu\_{1}^{\xi,a,\mathbb{P}})&=\overline{p}(\,\cdot\,|\operatorname{pj}\_{S}(\Lambda\_{0}^{\xi,a,\mathbb{P}}),\Lambda\_{0}^{\xi,a,\mathbb{P}},p\_{1}(\cdot)),\\ \mathscr{L}\_{\mathbb{P}}(\mu\_{t+1}^{\xi,a,\mathbb{P}})&=\overline{p}(\,\cdot\,|\operatorname{pj}\_{S}(\Lambda\_{t}^{\xi,a,\mathbb{P}}),\Lambda\_{t}^{\xi,a,\mathbb{P}},p\_{t+1}(\,\cdot\,|\varepsilon^{0}\_{1:t}))\quad\mbox{for all $t\geq 1$}.\end{aligned} |  |

The proof of Proposition [2.12](https://arxiv.org/html/2511.04515v1#S2.Thmthm12 "Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") can be found in Section [5](https://arxiv.org/html/2511.04515v1#S5 "5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty").

###### Remark 2.13.

Let ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S), a∈Aa\in{\mathcal{}A}, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q} be given.
Note that for every t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.20) |  | 𝔼ℙ​[r​(stξ,a,ℙ,at,Λtξ,a,ℙ)]=𝔼ℙ​[𝔼ℙ​[∫S×Ar​(s~,a~,Λtξ,a,ℙ)​Λtξ,a,ℙ​(d​s~,d​a~)|Ft0]]=𝔼ℙ​[r¯​(pjS⁡(Λtξ,a,ℙ),Λtξ,a,ℙ)]=𝔼ℙ​[r¯​(μtξ,a,ℙ,Λtξ,a,ℙ)],\displaystyle\begin{aligned} \mathbb{E}^{\mathbb{P}}\big[{r}(s\_{t}^{\xi,a,{\mathbb{P}}},a\_{t},{\Lambda}\_{t}^{\xi,a,\mathbb{P}})\big]&=\mathbb{E}^{\mathbb{P}}\bigg[\mathbb{E}^{\mathbb{P}}\bigg[\int\_{S\times A}{r}(\tilde{s},\tilde{a},{\Lambda}\_{t}^{\xi,a,\mathbb{P}}){\Lambda}\_{t}^{\xi,a,\mathbb{P}}(d\tilde{s},d\tilde{a})\,\bigg|\,{\mathcal{}F}\_{t}^{0}\bigg]\bigg]\\ &=\mathbb{E}^{\mathbb{P}}\big[\overline{r}(\operatorname{pj}\_{S}({\Lambda}\_{t}^{\xi,a,\mathbb{P}}),{\Lambda}\_{t}^{\xi,a,\mathbb{P}})\big]=\mathbb{E}^{\mathbb{P}}\big[\overline{r}(\mu\_{t}^{\xi,a,\mathbb{P}},{\Lambda}\_{t}^{\xi,a,\mathbb{P}})\big],\end{aligned} |  |

where the first equality holds by Ft0{\mathcal{}F}\_{t}^{0}-measurability of Λtξ,a,ℙ{\Lambda}\_{t}^{\xi,a,\mathbb{P}} (see Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty") (ii)), the second equality follows from the definition of r¯\overline{r} (see Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iv)), and the third equality follows from the marginal constraint ([2.17](https://arxiv.org/html/2511.04515v1#S2.E17 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).111Since (μtξ,a,ℙ,Λtξ,a,ℙ)∈gr⁡(𝔘)(\mu\_{t}^{\xi,a,\mathbb{P}}\,,\,{\Lambda}\_{t}^{\xi,a,\mathbb{P}})\in\operatorname{gr}(\mathfrak{U}), ℙ\mathbb{P}-a.s., for all t≥0t\geq 0, the term r¯​(μtξ,a,ℙ,Λtξ,a,ℙ)\overline{r}(\mu\_{t}^{\xi,a,\mathbb{P}}\,,\,{\Lambda}\_{t}^{\xi,a,\mathbb{P}}) is well-defined in the ℙ\mathbb{P}-a.s. sense.

Moreover, since rr is bounded and β<1\beta<1 (see Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), by the dominated convergence theorem we can rewrite Ja​(ξ){\mathcal{}J}^{a}(\xi) (given in ([2.13](https://arxiv.org/html/2511.04515v1#S2.E13 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))) by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.21) |  | Ja​(ξ)=infℙ∈Q𝔼ℙ​[∑t=0∞βt​r¯​(μtξ,a,ℙ,Λtξ,a,ℙ)].\displaystyle{\mathcal{}J}^{a}(\xi)=\inf\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}\overline{r}(\mu\_{t}^{\xi,a,\mathbb{P}}\,,\,{\Lambda}\_{t}^{\xi,a,\mathbb{P}})\bigg]. |  |

Using Proposition [2.12](https://arxiv.org/html/2511.04515v1#S2.Thmthm12 "Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")–particularly the MDP given in ([2.19](https://arxiv.org/html/2511.04515v1#S2.E19 "In Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and the representations ([2.20](https://arxiv.org/html/2511.04515v1#S2.E20 "In Remark 2.13. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.21](https://arxiv.org/html/2511.04515v1#S2.E21 "In Remark 2.13. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Remark [2.13](https://arxiv.org/html/2511.04515v1#S2.Thmthm13 "Remark 2.13. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")–we can view the robust MFC problem ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) as a robust MDP with state and action processes (μtξ,a,ℙ,Λtξ,a,ℙ)t≥0(\mu\_{t}^{\xi,a,\mathbb{P}},\Lambda\_{t}^{\xi,a,\mathbb{P}})\_{t\geq 0} given in ([2.15](https://arxiv.org/html/2511.04515v1#S2.E15 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.16](https://arxiv.org/html/2511.04515v1#S2.E16 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). This leads us to consider the following Bellman-Isaacs operator T\mathcal{}T defined on Cb​(P​(S);ℝ)C\_{b}({\mathcal{}P}({S});\mathbb{R}): for every V¯∈Cb​(P​(S);ℝ)\overline{V}\in C\_{b}({\mathcal{}P}({S});\mathbb{R})

|  |  |  |  |
| --- | --- | --- | --- |
| (2.22) |  | T​V¯​(μ):=supΛ∈𝔘​(μ){r¯​(μ,Λ)+β​infp∈𝔓0∫P​(S)V¯​(μ′)​p¯​(d​μ′|μ,Λ,p)}μ∈P​(S),\displaystyle{\mathcal{}T}\overline{V}(\mu):=\sup\_{\Lambda\in\mathfrak{U}(\mu)}\bigg\{\overline{r}(\mu,\Lambda)+\beta\inf\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\mu,\Lambda,p)\bigg\}\quad\;\mu\in{\mathcal{}P}(S), |  |

where 𝔓0\mathfrak{P}^{0} is given in Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i), and 𝔘\mathfrak{U}, r¯\overline{r} and p¯\overline{p} are given in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

Following the framework of the ‘local to global paradigm’ for robust MDP problems (see, e.g., [neufeld2023markov, neufeld2024non, langner2024markov]), we first aim to characterize the local (i.e., one time-step) optimizers of the Bellman–Isaacs operator T{\mathcal{}T}, and subsequently establish the fixed point theorem. This will then enable us to construct the global optimizers of the robust MFC problem ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

To that end, we impose the following conditions on the basic components given in Definition [2.4](https://arxiv.org/html/2511.04515v1#S2.Thmthm4 "Definition 2.4. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). These conditions are (slightly) stronger than those in Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), as they contain certain regularity on the arguments in AA and E0E^{0} along with others on the arguments in SS and P​(S×A){\mathcal{}P}(S\times A). However, they allow us to have some useful properties on the lifted functions and mappings given in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), which are similar to and appear in a framework for robust MDP problems under model uncertainty (see, e.g., [neufeld2023markov, neufeld2024non, langner2024markov]).

###### Assumption 2.14.

The following conditions hold:

* (i)

  The subset 𝔓0\mathfrak{P}^{0} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)) is compact.
* (ii)

  There is some C¯F>0\overline{C}\_{\operatorname{F}}>0 such that222As noted in Section [2.1](https://arxiv.org/html/2511.04515v1#S2.SS1 "2.1. Notation and preliminaries ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), the product space S×A×P​(S×A)×E0S\times A\times{\mathcal{}P}(S\times A)\times E^{0} is endowed with the corresponding product topology induced by the following metric: for every (s,a,Λ,e0),(s~,a~,Λ~,e~0)∈S×A×P​(S×A)×E0(s,a,\Lambda,e^{0}),(\tilde{s},\tilde{a},\tilde{\Lambda},\tilde{e}^{0})\in S\times A\times{\mathcal{}P}(S\times A)\times E^{0},

  dS×A×P​(S×A)×E0​((s,a,Λ,e0),(s~,a~,Λ~,e~0)):=dS​(s,s~)+dA​(a,a~)+WP​(S×A)​(Λ,Λ~)+dE0​(e0,e~0).\displaystyle d\_{S\times A\times{\mathcal{}P}(S\times A)\times E^{0}}((s,a,\Lambda,e^{0}),(\tilde{s},\tilde{a},\tilde{\Lambda},\tilde{e}^{0})):=d\_{S}(s,\tilde{s})+d\_{A}(a,\tilde{a})+{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})+d\_{E^{0}}(e^{0},\tilde{e}^{0}).
  The same convention applies to S×A×P​(S×A)S\times A\times{\mathcal{}P}(S\times A) appearing in (iii).
   for every (s,a,Λ,e0),(s~,a~,Λ~,e~0)∈S×A×P​(S×A)×E0(s,a,\Lambda,e^{0}),(\tilde{s},\tilde{a},\tilde{\Lambda},\tilde{e}^{0})\in S\times A\times{\mathcal{}P}(S\times A)\times E^{0}

  |  |  |  |
  | --- | --- | --- |
  |  | ∫EdS​(F⁡(s,a,Λ,e,e0),F⁡(s~,a~,Λ~,e,e~0))​λε​(d​e)≤C¯F​dS×A×P​(S×A)×E0​((s,a,Λ,e0),(s~,a~,Λ~,e~0)).\displaystyle\hskip 15.00002pt\int\_{E}d\_{S}\big(\operatorname{F}(s,a,\Lambda,e,e^{0}),\operatorname{F}(\tilde{s},\tilde{a},\tilde{\Lambda},e,\tilde{e}^{0})\big)\lambda\_{\varepsilon}(de)\leq\overline{C}\_{{\operatorname{F}}}d\_{S\times A\times{\mathcal{}P}(S\times A)\times E^{0}}\big((s,a,\Lambda,e^{0}),(\tilde{s},\tilde{a},\tilde{\Lambda},\tilde{e}^{0})\big). |  |
* (iii)

  The reward function rr is Lipschitz continuous, in the sense that there is some C¯r>0\overline{C}\_{{r}}>0 such that for every (s,a,Λ),(s~,a~,Λ~)∈S×A×P​(S×A)(s,a,\Lambda),(\tilde{s},\tilde{a},\tilde{\Lambda})\in S\times A\times{\mathcal{}P}({S\times A})

  |  |  |  |
  | --- | --- | --- |
  |  | |r​(s,a,Λ)−r​(s~,a~,Λ~)|≤C¯r​dS×A×P​(S×A)​((s,a,Λ),(s~,a~,Λ~)).\hskip 30.00005pt|r(s,a,\Lambda)-r(\tilde{s},\tilde{a},\tilde{\Lambda})|\leq\overline{C}\_{{r}}d\_{S\times A\times{\mathcal{}P}(S\times A)}\big((s,a,\Lambda),(\tilde{s},\tilde{a},\tilde{\Lambda})\big). |  |
* (iv)

  β\beta is in [0,1∧(2​C¯F)−1)[0,1\wedge(2\overline{C}\_{{\operatorname{F}}})^{-1}).

In the following proposition, we characterize the local optimizers of the Bellman-Isaacs operator T{\mathcal{}T} given in ([2.22](https://arxiv.org/html/2511.04515v1#S2.E22 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). To that end, we recall that given L≥0L\geq 0, Lipb,L⁡(P​(S);ℝ)⊂Cb​(P​(S);ℝ)\operatorname{Lip}\_{b,L}({\mathcal{}P}(S);\mathbb{R})\subset C\_{b}({\mathcal{}P}(S);\mathbb{R}) is the set of all LL-Lipschitz continuous functions defined on P​(S){\mathcal{}P}(S).

###### Proposition 2.15.

Suppose that Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)–(iii) are satisfied. Then the following holds: For every L≥0L\geq 0 and every V¯∈Lipb,L⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,L}({\mathcal{}P}(S);\mathbb{R}),

* (i)

  (Local minimizer) There exists a measurable selector p¯∗:P​(S×A)∋Λ↦p¯∗​(Λ)∈𝔓0\overline{p}^{\*}:{\mathcal{}P}(S\times A)\ni\Lambda\mapsto\overline{p}^{\*}(\Lambda)\in\mathfrak{P}^{0} such that for every Λ∈P​(S×A)\Lambda\in{\mathcal{}P}(S\times A)

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.23) |  | ∫P​(S)V¯​(μ′)​p¯​(d​μ′|pjS⁡(Λ),Λ,p¯∗​(Λ))=infp∈𝔓0∫P​(S)V¯​(μ′)​p¯​(d​μ′|pjS⁡(Λ),Λ,p).\displaystyle\hskip 10.00002pt\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\operatorname{pj}\_{S}(\Lambda),\Lambda,\overline{p}^{\*}(\Lambda))=\inf\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\operatorname{pj}\_{S}(\Lambda),\Lambda,p). |  |
* (ii)

  (Local maximizer) There exists a measurable selector π¯∗:P​(S)∋μ↦π¯∗​(μ)∈𝔘​(μ)\overline{\pi}^{\*}:{\mathcal{}P}(S)\ni\mu\mapsto\overline{\pi}^{\*}(\mu)\in\mathfrak{U}(\mu) satisfying that for every μ∈P​(S)\mu\in{\mathcal{}P}(S)

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.24) |  | r¯​(μ,π¯∗​(μ))+β​infp∈𝔓0∫P​(S)V¯​(μ′)​p¯​(d​μ′|μ,π¯∗​(μ),p)=T​V¯​(μ).\displaystyle\hskip 10.00002pt\overline{r}(\mu,\overline{\pi}^{\*}(\mu))+\beta\inf\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\mu,\overline{\pi}^{\*}(\mu),p)={\mathcal{}T}\overline{V}(\mu). |  |

We now apply the Banach fixed-point theorem (see, e.g., [bauerle2011markov, Theorem A 3.5]) for the Bellman-Isaacs operator T{\mathcal{}T} given in ([2.22](https://arxiv.org/html/2511.04515v1#S2.E22 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

###### Proposition 2.16.

Suppose that Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") is satisfied, and let L¯≥2​C¯r/(1−2​β​C¯F)\overline{L}\geq 2\overline{C}\_{r}/(1-2\beta\overline{C}\_{{\operatorname{F}}}). Then it holds that T​(Lipb,L¯⁡(P​(S);ℝ))⊆Lipb,L¯⁡(P​(S);ℝ){\mathcal{}T}(\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}))\subseteq\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}), and for every V¯1,V¯2∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}^{1},\overline{V}^{2}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R})

|  |  |  |  |
| --- | --- | --- | --- |
| (2.25) |  | ‖T​V¯1−T​V¯2‖∞≤β​‖V¯1−V¯2‖∞.\displaystyle\|{\mathcal{}T}\overline{V}^{1}-{\mathcal{}T}\overline{V}^{2}\|\_{\infty}\leq\beta\|\overline{V}^{1}-\overline{V}^{2}\|\_{\infty}. |  |

In particular, there exists a unique V¯∗∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}^{\*}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}) satisfying that T​V¯∗=V¯∗{\mathcal{}T}\overline{V}^{\*}=\overline{V}^{\*}. Moreover, it holds for every V¯∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}) that V¯∗=limn→∞Tn​V¯\overline{V}^{\*}=\lim\_{n\to\infty}{\mathcal{}T}^{n}\overline{V}.

The proofs of Propositions [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") can be found in Section [5](https://arxiv.org/html/2511.04515v1#S5 "5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty").

### 2.4. Verification theorem

This section aims to establish that the fixed point V¯∗\overline{V}^{\*} of the Bellman-Isaacs operator T{\mathcal{}T} (see Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) coincides with the robust MFC problem VV of the representative agent (see ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))) in the sense that333By construction of the set Q{\mathcal{}Q} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)), the law of ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S) is invariant w.r.t. the choice of supporting probability measure ℙ∈Q\mathbb{P}\in{\mathcal{}Q}. Therefore, we can and do write ℒ​(ξ):=ℒℙ​(ξ)∈P​(S)\mathscr{L}(\xi):=\mathscr{L}\_{\mathbb{P}}(\xi)\in{\mathcal{}P}(S) for any ℙ∈Q\mathbb{P}\in{\mathcal{}Q}. V​(ξ)=V¯​(ℒ​(ξ))V(\xi)=\overline{V}(\mathscr{L}(\xi)) for all ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S).

To that end, we first construct a measure in Q{\mathcal{}Q} for each open-loop control in A{\mathcal{}A} (see ([2.11](https://arxiv.org/html/2511.04515v1#S2.E11 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))), using the local minimizer from Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i). This will later be used in the verification theorem to derive a worst-case measure in Q{\mathcal{}Q} by suitably choosing an optimal control in A{\mathcal{}A}.

###### Lemma 2.17.

Suppose that Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") is satisfied.
Let ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S) be the initial state of the representative agent. Then for every a∈Aa\in{\mathcal{}A}, there exists ℙ¯ξ,a∈Q\underline{\mathbb{P}}^{\xi,a}\in{\mathcal{}Q} induced by some (p¯tξ,a)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,a})\_{t\geq 1}\in\mathcal{K}^{0} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))
such that ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.26) |  | ℒℙ¯ξ,a​(ε10)=p¯1ξ,a=p¯∗​(Λ¯0ξ,a),ℒℙ¯ξ,a(εt+10|Ft0)=p¯t+1ξ,a(⋅|ε1:t0)=p¯∗(Λ¯tξ,a)for all t≥1,\displaystyle\begin{aligned} \hskip 30.00005pt&\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\varepsilon\_{1}^{0})=\underline{p}\_{1}^{\xi,a}=\overline{p}^{\*}(\underline{\Lambda}\_{0}^{\xi,a}),\\ &\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\varepsilon\_{t+1}^{0}\,|{\mathcal{}F}\_{t}^{0})=\underline{p}\_{t+1}^{\xi,a}(\,\cdot\,|\varepsilon\_{1:t}^{0})=\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,a})\quad\mbox{for all $t\geq 1$},\end{aligned} |  |

where p¯∗\overline{p}^{\*} is the local minimizer given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i), Λ¯0ξ,a\underline{\Lambda}\_{0}^{\xi,a} is the joint law of (s0ξ,a,ℙ¯ξ,a,a0)(s\_{0}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}},a\_{0}) under ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}, and for t≥1t\geq 1 Λ¯tξ,a\underline{\Lambda}\_{t}^{\xi,a} is the conditional joint law of (stξ,a,ℙ¯ξ,a,at)(s\_{t}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}},a\_{t}) under ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a} given ε1:t0\varepsilon^{0}\_{1:t}. Consequently, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.27) |  | ℒℙ¯ξ,a(μ¯t+1ξ,a)=p¯(⋅|pjS(Λ¯tξ,a),Λ¯tξ,a,p¯∗(Λ¯tξ,a)),ℙ¯ξ,a-a.s.,for all t≥0,\displaystyle\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\underline{\mu}\_{t+1}^{\xi,a})=\overline{p}(\,\cdot\,\big|\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a},\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,a})),\quad\mbox{$\underline{\mathbb{P}}^{\xi,a}$-a.s.,}\quad\mbox{for all $t\geq 0$}, |  |

where p¯\overline{p} is given in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), and μ¯t+1ξ,a\underline{\mu}\_{t+1}^{\xi,a} is the conditional law of st+1ξ,a,ℙ¯ξ,as\_{t+1}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}} under ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a} given ε1:t+10\varepsilon^{0}\_{1:t+1}.

We now construct an open-loop control in A{\mathcal{}A}, using the local maximizer from Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii). Then we will verify that this open-loop control is indeed a maximizer of the robust MFC problem given in ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

We impose the following condition.

###### Assumption 2.18.

λϑ∈P​(Θ)\lambda\_{\vartheta}\in{\mathcal{}P}(\Theta) given in Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") is atomless.

###### Remark 2.19.

Assumption [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") also appears in [carmona2023model] (see Section 2.1.2). Moreover, [motte2022mean] incorporates this assumption by assuming the existence of a uniform random variable that is independent of the given initial state (see Section 3 therein). This assumption is crucial for constructing an optimal control/policy from the lifted dynamic programming results presented in both references—and consequently in this article as well. In particular, we often use the following properties.

Since ℒℙ​(ϑ)=λϑ\mathscr{L}\_{\mathbb{P}}(\vartheta)=\lambda\_{\vartheta} for all ℙ∈Q\mathbb{P}\in{\mathcal{}Q} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)), Assumption [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") implies the existence of a sequence (ht)t≥0(h\_{t})\_{t\geq 0} of Borel measurable functions ht:Θ→[0,1]h\_{t}:\Theta\to[0,1] such that under any ℙ∈Q\mathbb{P}\in{\mathcal{}Q},

|  |  |  |
| --- | --- | --- |
|  | (ht​(ϑt))t≥0​is i.i.d. with law U[0,1], (h\_{t}(\vartheta\_{t}))\_{t\geq 0}\;\;\mbox{is i.i.d.\;with law ${\mathcal{}U}\_{[0,1]}$, } |  |

i.e., uniform distribution on [0,1][0,1]; see [bogachev2007constructions, Theorem 9.2.2]. Since all the agents are indistinguishable, such a sequence exists for each agent i∈ℕi\in\mathbb{N}, and we denote it by (hti)t≥0(h^{i}\_{t})\_{t\geq 0}.

###### Lemma 2.20.

Suppose that Assumptions [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") are satisfied. Let ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S) be the initial state of the representative agent. Then there exists a∗∈Aa^{\*}\in{\mathcal{}A} such that for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q},

|  |  |  |  |
| --- | --- | --- | --- |
| (2.28) |  | Λtξ,a∗,ℙ=π¯∗​(μtξ,a∗,ℙ), ℙ-a.s., for all t≥0,\displaystyle{\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}}=\overline{\pi}^{\*}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}),\quad\mbox{ $\mathbb{P}$-a.s., for all $t\geq 0$,} |  |

where π¯∗\overline{\pi}^{\*} is the local maximizer given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii), and (μtξ,a∗,ℙ)t≥0({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}})\_{t\geq 0} and (Λtξ,a∗,ℙ)t≥0({\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}})\_{t\geq 0} are given in ([2.15](https://arxiv.org/html/2511.04515v1#S2.E15 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.16](https://arxiv.org/html/2511.04515v1#S2.E16 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), respectively, under (a∗,ℙ)(a^{\*},\mathbb{P}).

We are now ready to state the verification theorem for the constructed open-loop control and probability measure in the preceding two lemmas.The proofs of the theorem and preceding lemmas are provided in Section [6](https://arxiv.org/html/2511.04515v1#S6 "6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty").

###### Theorem 2.21.

Suppose that Assumptions [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") are satisfied. Let L¯≥2​Cr/(1−2​β​CF)\overline{L}\geq 2C\_{r}/(1-2\beta C\_{{\operatorname{F}}}) be given, and let V¯∗∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}^{\*}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}) be such that T​V¯∗=V¯∗{\mathcal{}T}\overline{V}^{\*}=\overline{V}^{\*} (see Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Moreover, let a∗∈Aa^{\*}\in{\mathcal{}A} be such that
([2.28](https://arxiv.org/html/2511.04515v1#S2.E28 "In Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q} (see Lemma [2.20](https://arxiv.org/html/2511.04515v1#S2.Thmthm20 "Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).
Moreover, let Ja∗{\mathcal{}J}^{a^{\*}} and VV be given in ([2.13](https://arxiv.org/html/2511.04515v1#S2.E13 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), respectively. Then, for every ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S) the following hold:

* (i)

  V¯∗​(ℒ​(ξ))=V​(ξ)\overline{V}^{\*}(\mathscr{L}(\xi))=V(\xi), where ℒ​(ξ)∈P​(S)\mathscr{L}(\xi)\in{\mathcal{}P}(S) is the law of ξ\xi (see Footnote [3](https://arxiv.org/html/2511.04515v1#footnote3 "footnote 3 ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).
* (ii)

  a∗∈Aa^{\*}\in{\mathcal{}A} and ℙ¯ξ,a∗∈Q\underline{\mathbb{P}}^{\xi,a^{\*}}\in{\mathcal{}Q} induced by (p¯tξ,a∗)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,a^{\*}})\_{t\geq 1}\in\mathcal{K}^{0} satisfying ([2.26](https://arxiv.org/html/2511.04515v1#S2.E26 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), ([2.27](https://arxiv.org/html/2511.04515v1#S2.E27 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) (see Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) are optimal in the sense that

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.29) |  | V​(ξ)=Ja∗​(ξ)=𝔼ℙ¯ξ,a∗​[Ra∗,ℙ¯ξ,a∗​(ξ)].\displaystyle{V}(\xi)={\mathcal{}J}^{a^{\*}}(\xi)=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,a^{\*}}}\big[R^{a^{\*},\underline{\mathbb{P}}^{\xi,a^{\*}}}(\xi)\big]. |  |

###### Remark 2.22.

As a consequence of Theorems [2.9](https://arxiv.org/html/2511.04515v1#S2.Thmthm9 "Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), under Assumptions [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") the optimal open-loop policy π∗∈Π\pi^{\*}\in\Pi of the robust MFC problem VV (see Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))—which can be obtained from the optimal open-loop control a∗∈Aa^{\*}\in{\mathcal{}A} in Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") of the representative robust MFC problem V​(ξ)V(\xi) in ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))—serves as an approximate of the NN-agent optimization problem VNV^{N} (see Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) when N∈ℕN\in\mathbb{N} is sufficiently large.

Lastly, we note that computing the local optimizers from the lifted dynamic programming principle (given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) is crucial for deriving the optimal open-loop control of the robust MFC problem. In particular, this step involves implementation of QQ-learning (or policy iteration) algorithms for the lifted dynamic programming principle and analyzing their convergence, together with the discretization error arising from of the lifted state and action spaces. While we defer these aspects to future research, in Section [3](https://arxiv.org/html/2511.04515v1#S3 "3. Numerical examples ‣ Robust mean-field control under common noise uncertainty") we present some numerical examples based on a value iteration type scheme to implement the lifted dynamic programming principle.

### 2.5. Connection with a closed-loop Markov policy framework

In this section, we introduce the notion of a closed-loop Markov policy for the robust MFC problem. In particular, following [carmona2023model, Definition 10], we consider a relaxed version of the robust MFC problem in Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), in which individual agents are allowed to sample their actions randomly according to a policy specified by the social planner.

As in Sections [2.3](https://arxiv.org/html/2511.04515v1#S2.SS3 "2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.4](https://arxiv.org/html/2511.04515v1#S2.SS4 "2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), we suppress the index i∈ℕi\in\mathbb{N} representing individual agents and consider the following representation agent’s robust MFC problem with closed-loop Markov policies.

###### Definition 2.23.

Let Q{\mathcal{}Q} be the uncertainty measures set given in Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Moreover, let 𝔽,𝔾\mathbb{F},\mathbb{G} be the filtrations given in ([2.10](https://arxiv.org/html/2511.04515v1#S2.E10 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), and let 𝔽0\mathbb{F}^{0} be the filtration generated by the common noise.

* (i)

  Denote by Πc\Pi^{c} the set of all closed-loop Markov policies πc:=(πtc)t≥0\pi^{c}:=(\pi\_{t}^{{c}})\_{t\geq 0} such that for every t≥0t\geq 0 the kernel

  |  |  |  |
  | --- | --- | --- |
  |  | πtc:S×P​(S)∋(s,μ)↦πtc​(d​a|s,μ)∈P​(A)\pi^{c}\_{t}:S\times{\mathcal{}P}(S)\ni(s,\mu)\mapsto\pi^{c}\_{t}(da|s,\mu)\in{\mathcal{}P}(A) |  |

  induces a randomized action given a couple of a state and a probability measure on SS.
* (ii)

  Let ξ∈LF00​(S)\xi\in L^{0}\_{{\mathcal{}F}\_{0}}(S) be the fixed initial state. Assume that for any (πc,ℙ)∈Πc×Q(\pi^{c},\mathbb{P})\in\Pi^{c}\times{\mathcal{}Q}, the state and action processes (stξ,πc,ℙ,atπc,ℙ)t≥0(s\_{t}^{\xi,\pi^{c},\mathbb{P}},a\_{t}^{\pi^{c},\mathbb{P}})\_{t\geq 0} for the representative agent in the inifinite population model satisfy that444We refer to Remark [2.24](https://arxiv.org/html/2511.04515v1#S2.Thmthm24 "Remark 2.24. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") for the well-posedness of (stξ,πc,ℙ,atπc,ℙ)t≥0(s\_{t}^{\xi,\pi^{c},\mathbb{P}},a\_{t}^{\pi^{c},\mathbb{P}})\_{t\geq 0} defined as in Definition [2.23](https://arxiv.org/html/2511.04515v1#S2.Thmthm23 "Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii). (stξ,πc,ℙ)t≥0(s\_{t}^{\xi,\pi^{c},\mathbb{P}})\_{t\geq 0} is 𝔽\mathbb{F}-adapted, (atπc,ℙ)t≥0(a^{\pi^{c},\mathbb{P}}\_{t})\_{t\geq 0} is 𝔾\mathbb{G}-adapted, and they satisfy

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.30) |  | st+1ξ,πc,ℙ:=F⁡(stξ,πc,ℙ,atπc,ℙ,ℙ(stξ,πc,ℙ,atπc,ℙ)0,εt+1,εt+10)for t≥0,with s0ξ,πc,ℙ:=ξ,ℒℙ(atπc,ℙ|Ft)=πtc(⋅|stξ,πc,ℙ,ℙstξ,πc,ℙ0)ℙ-a.s. for t≥0,\displaystyle\begin{aligned} \hskip 10.00002pt&s\_{t+1}^{\xi,\pi^{c},\mathbb{P}}:=\operatorname{F}(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}},\mathbb{P}^{0}\_{(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}})},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0})\quad\mbox{for $t\geq 0$},\;\;\mbox{with $\;\;s\_{0}^{\xi,\pi^{c},\mathbb{P}}:=\xi,$}\\ &\mathscr{L}\_{\mathbb{P}}(a^{\pi^{c},\mathbb{P}}\_{t}|{\mathcal{}F}\_{t})=\pi^{c}\_{t}(\,\cdot\,|s^{\xi,\pi^{c},\mathbb{P}}\_{t},\mathbb{P}\_{s^{\xi,\pi^{c},\mathbb{P}}\_{t}}^{0})\quad\mbox{$\mathbb{P}$-a.s.\quad for $t\geq 0$},\end{aligned} |  |

  where ℙ(stξ,πc,ℙ,atπc,ℙ)0\mathbb{P}^{0}\_{(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}})} is the conditional joint law of (stξ,πc,ℙ,atπc,ℙ)(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}}) under ℙ\mathbb{P} given ε1:t0\varepsilon^{0}\_{1:t} for t≥1t\geq 1, with the convention that ℙ(s0ξ,πc,ℙ,a0πc,ℙ)0:=ℒℙ​((s0ξ,πc,ℙ,a0πc,ℙ))\mathbb{P}^{0}\_{(s^{\xi,\pi^{c},\mathbb{P}}\_{0},a\_{0}^{\pi^{c},\mathbb{P}})}:=\mathscr{L}\_{\mathbb{P}}((s^{\xi,\pi^{c},\mathbb{P}}\_{0},a\_{0}^{\pi^{c},\mathbb{P}})). In analogy, ℙstξ,πc,ℙ0\mathbb{P}^{0}\_{s^{\xi,\pi^{c},\mathbb{P}}\_{t}} is the conditional law of stξ,πc,ℙs^{\xi,\pi^{c},\mathbb{P}}\_{t} under ℙ\mathbb{P} given ε1:t0\varepsilon^{0}\_{1:t} for t≥1t\geq 1 with ℙs0ξ,πc,ℙ0:=ℒℙ​(s0ξ,πc,ℙ)\mathbb{P}^{0}\_{s^{\xi,\pi^{c},\mathbb{P}}\_{0}}:=\mathscr{L}\_{\mathbb{P}}(s^{\xi,\pi^{c},\mathbb{P}}\_{0}).
* (iii)

  Accordingly, the robust MFC problem under closed-loop Markov policies is

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.31) |  | Vc​(ξ):=supπc∈ΠcJπc​(ξ),ξ∈LF00​(S),\displaystyle V^{c}(\xi):=\sup\_{\pi^{c}\in\Pi^{c}}{\mathcal{}J}^{\pi^{c}}(\xi),\quad\;\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S), |  |

  where Jπc​(ξ){\mathcal{}J}^{\pi^{c}}(\xi) is defined as Jπc​(ξ):=infℙ∈Q𝔼ℙ​[Rπc,ℙ​(ξ)]{\mathcal{}J}^{\pi^{c}}(\xi):=\inf\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}[R^{\pi^{c},\mathbb{P}}(\xi)] with

  |  |  |  |
  | --- | --- | --- |
  |  | Rπc,ℙ​(ξ):=𝔼ℙ0​[∑t=0∞βt​r​(stξ,πc,ℙ,atπc,ℙ,ℙ(stξ,πc,ℙ,atπc,ℙ)0)].\displaystyle R^{\pi^{c},\mathbb{P}}(\xi):=\mathbb{E}^{\mathbb{P}^{0}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}r(s\_{t}^{\xi,\pi^{c},\mathbb{P}},a^{\pi^{c},\mathbb{P}}\_{t},\mathbb{P}^{0}\_{(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a^{\pi^{c},\mathbb{P}}\_{t})})\bigg]. |  |

###### Remark 2.24.

Under Assumption [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), the conditional McKean-Vlasov dynamics with closed-loop Markov policies, as given in Definition [2.23](https://arxiv.org/html/2511.04515v1#S2.Thmthm23 "Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii), are well-defined. Indeed, by using the random variable ht​(ϑt)∼U[0,1]h\_{t}(\vartheta\_{t})\sim{\mathcal{}U}\_{[0,1]} (see Remark [2.19](https://arxiv.org/html/2511.04515v1#S2.Thmthm19 "Remark 2.19. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and the Blackwell–Dubins function ρA:P​(A)×[0,1]→A\rho\_{A}:{\mathcal{}P}(A)\times[0,1]\to A (see Lemma [A.2](https://arxiv.org/html/2511.04515v1#A1.Thmthm2 "Lemma A.2 (Blackwell and Dubins [blackwell1983extension]). ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty")), we can define, for any πc∈Πc\pi^{c}\in\Pi^{c} and ℙ∈Q\mathbb{P}\in{\mathcal{}Q},

|  |  |  |
| --- | --- | --- |
|  | atπc,ℙ:=ρA(πtc(⋅|stξ,πc,ℙ,ℙstξ,πc,ℙ0),ht(ϑt))t≥0.a\_{t}^{\pi^{c},\mathbb{P}}:=\rho\_{A}\big(\pi\_{t}^{c}(\,\cdot\,|\,s\_{t}^{\xi,\pi^{c},\mathbb{P}},\mathbb{P}^{0}\_{s\_{t}^{\xi,\pi^{c},\mathbb{P}}}),h\_{t}(\vartheta\_{t})\big)\quad t\geq 0. |  |

By the same arguments presented for the proof of Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty") (ii), we note that stξ,πc,ℙs\_{t}^{\xi,\pi^{c},\mathbb{P}} is Ft{\mathcal{}F}\_{t} measurable and ℙstξ,πc,ℙ0\mathbb{P}^{0}\_{s\_{t}^{\xi,\pi^{c},\mathbb{P}}} is Ft0{\mathcal{}F}\_{t}^{0} measurable. Consequently, atπc,ℙa\_{t}^{\pi^{c},\mathbb{P}} is Gt{\mathcal{}G}\_{t} measurable by the construction above. Furthermore, since Ft{\mathcal{}F}\_{t} is independent of ϑt\vartheta\_{t}, the property of ρA\rho\_{A} ensures that atπc,ℙa\_{t}^{\pi^{c},\mathbb{P}} satisfies the distributional constraint given in ([2.30](https://arxiv.org/html/2511.04515v1#S2.E30 "In item (ii) ‣ Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

We aim to show that the robust MFC problem VcV^{c} given in ([2.31](https://arxiv.org/html/2511.04515v1#S2.E31 "In item (iii) ‣ Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) coincides with the open-loop robust MFC problem VV given in ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). This equivalence will be established by demonstrating that Vc​(ξ)=V¯∗​(ℒ​(ξ))V^{c}(\xi)=\overline{V}^{\*}(\mathscr{L}(\xi))
for all ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S), where V¯∗\overline{V}^{\*} is the fixed point of the Bellman–Isaacs operator 𝒯\mathcal{T} given in Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), and ℒ​(ξ)∈P​(S)\mathscr{L}(\xi)\in{\mathcal{}P}(S) is the law of ξ\xi (see Footnote [3](https://arxiv.org/html/2511.04515v1#footnote3 "footnote 3 ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

To this end, and following the approach in Section [2.3](https://arxiv.org/html/2511.04515v1#S2.SS3 "2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), we begin by examining the dynamics of the lifted state and action processes, defined as follows: for every πc∈Πc\pi^{c}\in\Pi^{c} and ℙ∈Q\mathbb{P}\in{\mathcal{}Q},

|  |  |  |  |
| --- | --- | --- | --- |
| (2.32) |  | (μtξ,πc,ℙ)t≥0:=(ℙstξ,πc,ℙ0)t≥0⊆P​(S),(Λtξ,πc,ℙ)t≥0:=(ℙ(stξ,πc,ℙ,atπc,ℙ)0)t≥0⊆P​(S×A).\displaystyle\begin{aligned} (\mu\_{t}^{\xi,\pi^{c},\mathbb{P}})\_{t\geq 0}&:=(\mathbb{P}^{0}\_{s\_{t}^{\xi,\pi^{c},\mathbb{P}}})\_{t\geq 0}\subseteq{\mathcal{}P}(S),\\ (\Lambda\_{t}^{\xi,\pi^{c},\mathbb{P}})\_{t\geq 0}&:=(\mathbb{P}^{0}\_{(s\_{t}^{\xi,\pi^{c},\mathbb{P}},a\_{t}^{\pi^{c},\mathbb{P}})})\_{t\geq 0}\subseteq{\mathcal{}P}(S\times A).\end{aligned} |  |

Here we note that both processes are 𝔽0\mathbb{F}^{0} adapted (see Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")).

###### Lemma 2.25.

Suppose that Assumptions [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") are satisfied. Let πc∈Πc\pi^{c}\in\Pi^{c} be given and let ℙ∈Q\mathbb{P}\in{\mathcal{}Q} be induced by some (pt)t≥1∈𝒦0(p\_{t})\_{t\geq 1}\in\mathcal{K}^{0} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Then,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.33) |  | Λtξ,πc,ℙ=μtξ,πc,ℙ⊗^πtc(⋅|⋅,μtξ,πc,ℙ)ℙ-a.s. for all t≥0.\displaystyle\Lambda\_{t}^{\xi,\pi^{c},\mathbb{P}}=\mu\_{t}^{\xi,\pi^{c},\mathbb{P}}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\,\cdot\,|\,\cdot,\mu\_{t}^{\xi,\pi^{c},\mathbb{P}})\quad\mbox{$\mathbb{P}$-a.s. for all $t\geq 0$}. |  |

Consequently, it holds that ℙ\mathbb{P}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.34) |  | ℒℙ​(μ1ξ,πc,ℙ)=p¯(⋅|μ0ξ,πc,ℙ,μ0ξ,πc,ℙ⊗^π0c(⋅|⋅,μ0ξ,πc,ℙ),p1(⋅)),ℒℙ​(μt+1ξ,πc,ℙ)=p¯(⋅|μtξ,πc,ℙ,μtξ,πc,ℙ⊗^πtc(⋅|⋅,μtξ,πc,ℙ),pt+1(⋅|ε1:t0))for all t≥1.\displaystyle\begin{aligned} \mathscr{L}\_{\mathbb{P}}(\mu\_{1}^{\xi,\pi^{c},\mathbb{P}})&=\overline{p}(\,\cdot\,|\,\mu\_{0}^{\xi,\pi^{c},\mathbb{P}},\,\,\mu\_{0}^{\xi,\pi^{c},\mathbb{P}}\mathbin{\hat{\otimes}}\pi\_{0}^{c}(\,\cdot\,|\,\cdot,\mu\_{0}^{\xi,\pi^{c},\mathbb{P}}),\,p\_{1}(\cdot)),\\ \mathscr{L}\_{\mathbb{P}}(\mu\_{t+1}^{\xi,\pi^{c},\mathbb{P}})&=\overline{p}(\,\cdot\,|\,\mu\_{t}^{\xi,\pi^{c},\mathbb{P}},\,\,\mu\_{t}^{\xi,\pi^{c},\mathbb{P}}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\,\cdot\,|\,\cdot,\mu\_{t}^{\xi,\pi^{c},\mathbb{P}}),\,p\_{t+1}(\,\cdot\,|\varepsilon^{0}\_{1:t}))\quad\mbox{for all $t\geq 1$}.\end{aligned} |  |

Then, as in Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), we construct a measure in Q{\mathcal{}Q} for each closed-loop policy in Πc\Pi^{c} (see Definition [2.23](https://arxiv.org/html/2511.04515v1#S2.Thmthm23 "Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), using the local minimizer from Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i).

###### Lemma 2.26.

Suppose that Assumptions [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") are satisfied.
For every πc∈Πc\pi^{c}\in\Pi^{c}, there exists ℙ¯ξ,πc∈Q\underline{\mathbb{P}}^{\xi,\pi^{c}}\in{\mathcal{}Q} induced by some (p¯tξ,πc)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,\pi^{c}})\_{t\geq 1}\in\mathcal{K}^{0} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))
such that ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.35) |  | ℒℙ¯ξ,πc​(ε10)=p¯1ξ,πc=p¯∗​(Λ¯0ξ,πc),ℒℙ¯ξ,πc(εt+10|Ft0)=p¯t+1ξ,πc(⋅|ε1:t0)=p¯∗(Λ¯tξ,πc)for all t≥1,\displaystyle\begin{aligned} \hskip 30.00005pt&\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\varepsilon\_{1}^{0})=\underline{p}\_{1}^{\xi,\pi^{c}}=\overline{p}^{\*}(\underline{\Lambda}\_{0}^{\xi,\pi^{c}}),\\ &\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\varepsilon\_{t+1}^{0}\,|\,{\mathcal{}F}\_{t}^{0})=\underline{p}\_{t+1}^{\xi,\pi^{c}}(\cdot\,|\,\varepsilon\_{1:t}^{0})=\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,\pi^{c}})\quad\mbox{for all $t\geq 1$},\end{aligned} |  |

where p¯∗\overline{p}^{\*} is the local minimizer in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i),
Λ¯0ξ,πc\underline{\Lambda}\_{0}^{\xi,\pi^{c}} is the joint law of (s0ξ,πc,ℙ¯ξ,πc,a0πc,ℙ¯ξ,πc)(s\_{0}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}},a^{\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}}\_{0}) under ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}, and for t≥1t\geq 1 Λ¯tξ,πc\underline{\Lambda}\_{t}^{\xi,\pi^{c}} is the conditional joint law of (stξ,πc,ℙ¯ξ,πc,atπc,ℙ¯ξ,πc)(s\_{t}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}},a^{\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}}\_{t}) under ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}} given ε1:t0\varepsilon^{0}\_{1:t}. Consequently, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.36) |  | ℒℙ¯ξ,πc(μ¯t+1ξ,πc)=p¯(⋅|pjS(Λ¯tξ,πc),Λ¯tξ,πc,p¯∗(Λ¯tξ,πc)), ℙ¯ξ,πc-a.s., for all t≥0,\displaystyle\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\underline{\mu}\_{t+1}^{\xi,\pi^{c}})=\overline{p}(\,\cdot\,|\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,\pi^{c}}),\underline{\Lambda}\_{t}^{\xi,\pi^{c}},\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,\pi^{c}})),\quad\mbox{ $\underline{\mathbb{P}}^{\xi,\pi^{c}}$-a.s., for all $t\geq 0$,} |  |

where p¯\overline{p} is given in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), and μ¯t+1ξ,πc\underline{\mu}\_{t+1}^{\xi,\pi^{c}} is the conditional law of st+1ξ,πc,ℙ¯ξ,πcs\_{t+1}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}} given ε1:t+10\varepsilon^{0}\_{1:t+1}.

The proofs of Lemma [2.25](https://arxiv.org/html/2511.04515v1#S2.Thmthm25 "Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.26](https://arxiv.org/html/2511.04515v1#S2.Thmthm26 "Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") are presented in Section [7](https://arxiv.org/html/2511.04515v1#S7 "7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty").

###### Remark 2.27.

While the construction of (p¯tξ,πc)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,\pi^{c}})\_{t\geq 1}\in\mathcal{K}^{0} given in Lemma [2.26](https://arxiv.org/html/2511.04515v1#S2.Thmthm26 "Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") proceeds inductively (as in the proof of Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), the arguments differ from those used therein. This is due to the fact that a closed-loop Markov policy πc∈Πc\pi^{c}\in\Pi^{c} does not determine a fixed action process, but a randomly sampled one. For this, we rely on the Blackwell-Dubins function given in Lemma [A.2](https://arxiv.org/html/2511.04515v1#A1.Thmthm2 "Lemma A.2 (Blackwell and Dubins [blackwell1983extension]). ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty") together with Remark [2.19](https://arxiv.org/html/2511.04515v1#S2.Thmthm19 "Remark 2.19. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and some measure-theoretic arguments.

Finally, we conclude that the robust MFC problem under the closed-loop Markov policy framework coincides with the fixed point V¯\overline{V}, and hence with the robust MFC problem under the open-loop policy framework.

###### Corollary 2.28.

Suppose that Assumptions [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.18](https://arxiv.org/html/2511.04515v1#S2.Thmthm18 "Assumption 2.18. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") are satisfied. Let L¯≥2​Cr/(1−2​β​CF)\overline{L}\geq 2C\_{r}/(1-2\beta C\_{{\operatorname{F}}}) be given, and let V¯∗∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}^{\*}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}) be such that T​V¯∗=V¯∗{\mathcal{}T}\overline{V}^{\*}=\overline{V}^{\*} (see Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Define

|  |  |  |  |
| --- | --- | --- | --- |
| (2.37) |  | πlocc,∗:S×P(S)∋(s,μ)↦πlocc,∗(⋅|s,μ):=KS×A(⋅|s,π¯∗(μ),μ)∈P(A),\displaystyle{\pi}\_{\operatorname{loc}}^{c,\*}:S\times{\mathcal{}P}(S)\ni(s,\mu)\mapsto{\pi}\_{\operatorname{loc}}^{c,\*}(\,\cdot\,|s,\mu):={\mathcal{}K}\_{S\times A}(\,\cdot\,|s,\overline{\pi}^{\*}(\mu),\mu)\in{\mathcal{}P}(A), |  |

i.e., the universal disintegration kernel of π¯∗​(μ)\overline{\pi}^{\*}(\mu) w.r.t. pjS⁡(π¯∗​(μ))=μ\operatorname{pj}\_{S}(\overline{\pi}^{\*}(\mu))=\mu (see Lemma [A.3](https://arxiv.org/html/2511.04515v1#A1.Thmthm3 "Lemma A.3 (Universal disintegration; see, e.g., [kallenberg2017random, Corollarly 1.26]). ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty")) so that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.38) |  | π¯∗(μ)=μ⊗^πlocc,∗(⋅|⋅,μ).\displaystyle\overline{\pi}^{\*}(\mu)=\mu\mathbin{\hat{\otimes}}{\pi}\_{\operatorname{loc}}^{c,\*}(\,\cdot\,|\,\cdot,\mu). |  |

Define πc,∗:=(πtc,∗)t≥0∈Πc\pi^{c,\*}:=(\pi\_{t}^{c,\*})\_{t\geq 0}\in\Pi^{c} by πtc,∗:=πlocc,∗\pi\_{t}^{c,\*}:=\pi\_{\operatorname{loc}}^{c,\*} for every t≥0t\geq 0 (i.e., stationary closed-loop Markov policy). Moreover, let VcV^{c} and Jπc,∗{\mathcal{}J}^{\pi^{c,\*}} be given in ([2.31](https://arxiv.org/html/2511.04515v1#S2.E31 "In item (iii) ‣ Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), and let VV be given in ([2.14](https://arxiv.org/html/2511.04515v1#S2.E14 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Then, for every ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S) the following hold:

* (i)

  V¯∗​(ℒ​(ξ))=Vc​(ξ)=V​(ξ)\overline{V}^{\*}(\mathscr{L}(\xi))=V^{c}(\xi)=V(\xi), where ℒ​(ξ)∈P​(S)\mathscr{L}(\xi)\in{\mathcal{}P}(S) is the law of ξ\xi (see Footnote [3](https://arxiv.org/html/2511.04515v1#footnote3 "footnote 3 ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).
* (ii)

  πc,∗∈Πc\pi^{c,\*}\in\Pi^{c} and ℙ¯ξ,πc,∗\underline{\mathbb{P}}^{\xi,\pi^{c,\*}} induced by (p¯tξ,πc,∗)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,\pi^{c,\*}})\_{t\geq 1}\in\mathcal{K}^{0} satisfying ([2.35](https://arxiv.org/html/2511.04515v1#S2.E35 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), ([2.36](https://arxiv.org/html/2511.04515v1#S2.E36 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) (see Lemma [2.26](https://arxiv.org/html/2511.04515v1#S2.Thmthm26 "Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) are optimal in the sense that

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (2.39) |  | Vc​(ξ)=Jπc,∗​(ξ)=𝔼ℙ¯ξ,πc,∗​[Rπc,∗,ℙ¯ξ,πc,∗​(ξ)].\displaystyle{V}^{c}(\xi)={\mathcal{}J}^{\pi^{c,\*}}(\xi)=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c,\*}}}\big[R^{\pi^{c,\*},\underline{\mathbb{P}}^{\xi,\pi^{c,\*}}}(\xi)\big]. |  |

## 3. Numerical examples

In this section, we apply our robust MFC framework under common noise uncertainty to illustrative examples in distribution matching and financial systemic risk, thereby emphasizing the critical role of incorporating common noise uncertainty into the analysis.
In both examples, the algorithm implementing the lifted dynamic programming principle in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") together with the verification theorem in Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (or Corollary [2.28](https://arxiv.org/html/2511.04515v1#S2.Thmthm28 "Corollary 2.28. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) builds upon the value iteration algorithm for the robust MDP framework of [neufeld2023markov, Section 4.4.1].

### 3.1. Example 1: Distribution matching

We first consider an example inspired by Example 1 in [carmona2023model], in which the goal for the central planner is to make the population distribution match a given target distribution. Common noise makes the task harder because it may randomly shift the distribution.

To be specific, consider the following basic elements (recall Definition [2.4](https://arxiv.org/html/2511.04515v1#S2.Thmthm4 "Definition 2.4. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")):555The code is provided for the sake of completeness at <https://github.com/mlauriere/RobustMFMDP>.

* •

  S={1,2,…,|S|}S=\{1,2,\dots,|S|\} representing a one-dimensional grid world with |S||S| states; in the experiments, we use |S|=7|S|=7 states.
* •

  A={−1,0,1}A=\{-1,0,1\}, where the actions are interpreted respectively as moving to the left, staying or moving to the right.
* •

  E={0}E=\{0\}, which means that there is no idiosyncratic noise.
* •

  E0={−1,0,1}E^{0}=\{-1,0,1\}, where the common noise values are interpreted as the actions but they affect the whole population.
* •

  F:S×A×P​(S×A)×E×E0→S\operatorname{F}:S\times A\times{\mathcal{}P}(S\times A)\times E\times E^{0}\to S is given by

  |  |  |  |
  | --- | --- | --- |
  |  | F⁡(s,a,Λ,e,e0)=max⁡(1,min⁡(|S|,s+a+e0)),\operatorname{F}(s,a,\Lambda,e,e^{0})=\max(1,\min(|S|,s+a+e^{0})), |  |

  which represents the fact that the agent’s movement is determined by her action and the common noise, and the agent remains at 11 (resp. 77) if she tries to move to the left (resp. right) of this state.
* •

  r:S×A×P​(S×A)→ℝr:S\times A\times{\mathcal{}P}(S\times A)\to\mathbb{R} is given by

  |  |  |  |
  | --- | --- | --- |
  |  | r​(s,a,Λ)=‖pjS⁡(Λ)−μ∗‖22=∑s∈S|pjS⁡(Λ)​(s)−μ∗​(s)|2,r(s,a,\Lambda)=\|\operatorname{pj}\_{S}(\Lambda)-\mu^{\*}\|\_{2}^{2}=\sum\_{s\in S}|\operatorname{pj}\_{S}(\Lambda)(s)-\mu^{\*}(s)|^{2}, |  |

  where μ∗∈P​(S)\mu^{\*}\in{\mathcal{}P}(S) is a fixed target distribution which is part of the model’s definition.
* •

  β=0.4\beta=0.4 is the discount factor so that Assumptions [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii) and [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iv) are satisfied.

For the common noise probability measure, we consider the following situation:

* •

  The true common noise distribution ptrue∈P​(E0)p\_{\textrm{true}}\in{\mathcal{}P}(E^{0}) is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.1) |  | ptrue:=vtrue,1​δ{ε0=−1}+vtrue,2​δ{ε0=0}+vtrue,3​δ{ε0=1},\displaystyle p\_{\textrm{true}}:=v\_{{\textrm{true}},1}\delta\_{\{\varepsilon^{0}=-1\}}+v\_{{\textrm{true}},2}\delta\_{\{\varepsilon^{0}=0\}}+v\_{{\textrm{true}},3}\delta\_{\{\varepsilon^{0}=1\}}, |  |

  with some probability vector vtrue:=(vtrue,1,vtrue,2,vtrue,3)∈[0,1]3v\_{{\textrm{true}}}:=(v\_{{\textrm{true}},1},v\_{{\textrm{true}},2},v\_{{\textrm{true}},3})\in[0,1]^{3}, i.e., a simplex.
* •

  However, we consider that the central planner does not know this true distribution; she has estimated the common noise distribution to be approximately equal to a reference probability measure pref∈P​(E0)p\_{\textrm{ref}}\in{\mathcal{}P}(E^{0}) with the corresponding probability vector vref∈[0,1]3v\_{\textrm{ref}}\in[0,1]^{3}.

As a baseline, the central planner can learn a policy πref\pi\_{\textrm{ref}} which is optimal for the MFC model with common noise distribution prefp\_{\textrm{ref}}. Alternatively, she can solve the robust MFC problem and learn a policy πrobust\pi\_{\textrm{robust}} which may be suboptimal for the model with prefp\_{\textrm{ref}} but which performs better than πref\pi\_{\textrm{ref}} in the true model with common noise distribution ptruep\_{\textrm{true}}.

We consider the uncertainty set 𝔓0\mathfrak{P}^{0} which consists of all perturbed measures p∈P​(E0)p\in{\mathcal{}P}(E^{0}) of the reference measure prefp\_{\textrm{ref}}, whose corresponding probability vector v∈[0,1]3v\in[0,1]^{3} is

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | v:=renorm​(max⁡(0,vref+vperturb)),\displaystyle v:=\mathrm{renorm}(\max(0,v\_{\textrm{ref}}+v\_{\textrm{perturb}})), |  |

where vperturb∈ℝ3v\_{\textrm{perturb}}\in\mathbb{R}^{3} is a perturbation vector constructed as follows: each coordinate is sampled uniformly from [−δperturb,δperturb][-\delta\_{\textrm{perturb}},\delta\_{\textrm{perturb}}], with a small δperturb>0\delta\_{\textrm{perturb}}>0 representing the uncertainty level. The average of the 33 coordinates is then subtracted to each coordinate to ensure that the average of vperturbv\_{\textrm{perturb}} over coordinates is 0. Under this construction, Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i) is satisfied.

![Refer to caption](x1.png)


Figure 1. Values achieved under ptruep\_{\textrm{true}} when using the optimal policy for the MFC under prefp\_{\textrm{ref}} (red dashed line) or the robust MFC under the uncertainty level δperturb∈{0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2}\delta\_{\textrm{perturb}}\in\{0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2\} (blue curve) in Example 1. Shaded areas represents ±\pm standard deviation over 8 independent runs.

We implement the above model with: vtrue=(0.2,0.7,0.1)v\_{\textrm{true}}=(0.2,0.7,0.1), vref=(0,1,0)v\_{\textrm{ref}}=(0,1,0) and δperturb\delta\_{\textrm{perturb}} varying between 0.00.0 and 0.80.8. Figure [1](https://arxiv.org/html/2511.04515v1#S3.F1 "Figure 1 ‣ 3.1. Example 1: Distribution matching ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty") shows that for moderately small δperturb\delta\_{\textrm{perturb}}, the robust policy performs better than the non-robust policy. For large values of δperturb\delta\_{\textrm{perturb}} however, the robust policy yields a smaller value: being robust against a large set of possible common noise distributions prevents the policy from performing well on the true distribution. The results are averaged over 8 different runs and the plots shows the mean value and its standard deviation.

Figure [2](https://arxiv.org/html/2511.04515v1#S3.F2 "Figure 2 ‣ 3.1. Example 1: Distribution matching ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty") shows three realizations of trajectories, starting from random initial distributions. We display a few time steps between 0 and 2020. We observe that the learnt policy uses the actions with varying proportions depending on the individual state and also depending on the current population distribution. Overall, it uses mostly action 11 (resp. −1-1) when the state is below (resp. above) the middle state because the target distribution is centered around the middle state.

![Refer to caption](x2.png)


Figure 2. Three sample trajectories of the population distribution and
corresponding action distribution for each state in Example 1. The target
distribution to be matched is shown by dashed red lines.

![Refer to caption](x3.png)


Figure 3. The three trajectories of common noise associated with Figure [2](https://arxiv.org/html/2511.04515v1#S3.F2 "Figure 2 ‣ 3.1. Example 1: Distribution matching ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty")

The fact that the target distribution is not perfectly matched is due to the impact of the common noise, whose trajectories are displayed in Figure [3](https://arxiv.org/html/2511.04515v1#S3.F3 "Figure 3 ‣ 3.1. Example 1: Distribution matching ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty"). Notice that for the second simulation, the common noise takes several positive values on time steps 17, 18 and 19, leaving little time for the population distribution to adapt and shift back to the target distribution (recall that the possible actions are {−1,0,1}\{-1,0,1\}, just as the possible common noise values).

### 3.2. Financial systemic risk

We now consider an example inspired by the systemic risk model proposed by [MR3325083]. In this model, the agents are financial institutions, represented by a state which is their log-reserve. They interact by borrowing and lending to each other, or to a central bank. Their evolution is impacted by a common noise which can be interpreted as macroscopic events affecting the whole economy. If a financial institution touches a given threshold, it defaults.
There are two main differences between the model we present below and the original model one: first, the model of [MR3325083] was a mean field game (corresponding to non-cooperative players) while we consider a mean field control problem (corresponding to cooperative players); furthermore, the original model was written in continuous space and time whereas we consider a discrete space and time model for the sake of numerical experiments. However, the main ideas underpinning the model are similar. The central planner is to make the population distribution match a given target distribution.

![Refer to caption](x4.png)


Figure 4. Value achieved under ptruep\_{\textrm{true}} when using the optimal policy for the MFC with prefp\_{\textrm{ref}} (red dashed line) or the optimal policy for the robust MFC with δperturb∈{0.0,0.1,0.2,0.3,0.4,0.5,0.6}\delta\_{\textrm{perturb}}\in\{0.0,0.1,0.2,0.3,0.4,0.5,0.6\} (blue curve) in Example 2. Shaded areas represents ±\pm standard deviation over 8 independent runs.

To be specific, consider the following basic elements (recall Definition [2.4](https://arxiv.org/html/2511.04515v1#S2.Thmthm4 "Definition 2.4. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")):

* •

  S={smin,smin+1,…,smax}S=\{s\_{\operatorname{min}},s\_{\operatorname{min}}+1,\dots,s\_{\operatorname{max}}\}, which represents a one-dimensional grid world with |S|=smax−smin+1|S|=s\_{\operatorname{max}}-s\_{\operatorname{min}}+1 states; in the experiments, we use smin=−1s\_{\operatorname{min}}=-1, smax=4s\_{\operatorname{max}}=4, |S|=5|S|=5 states.
* •

  A={−1,0,1}A=\{-1,0,1\}, which corresponds to lending (if negative) or borrowing (if positive) units.
* •

  E={−1,0,1}E=\{-1,0,1\}, which corresponds to idiosyncratic noise. Moreover, the probaility vector of its law λε∈P​(E)\lambda\_{\varepsilon}\in{\mathcal{}P}(E) is given by (0.05,0.9,0.05)(0.05,0.9,0.05).
* •

  E0={−2,−1,0,1,2}E^{0}=\{-2,-1,0,1,2\}, which corresponds to common noise affecting the whole population.
* •

  F:S×A×P​(S×A)×E×E0→S\operatorname{F}:S\times A\times{\mathcal{}P}(S\times A)\times E\times E^{0}\to S is given by

  |  |  |  |
  | --- | --- | --- |
  |  | F⁡(s,a,Λ,e,e0)=max⁡(smin,min⁡(smax,s+a+e+e0))if s>smin,\operatorname{F}(s,a,\Lambda,e,e^{0})=\max(s\_{\operatorname{min}},\min(s\_{\operatorname{max}},s+a+e+e^{0}))\quad\mbox{if $s>s\_{\operatorname{min}}$}, |  |

  and F⁡(smin,a,Λ,e,e0)=smin\operatorname{F}(s\_{\operatorname{min}},a,\Lambda,e,e^{0})=s\_{\operatorname{min}}, which represents the fact that the agent’s log-reserve evolution is determined by her action, the individual noise and the common noise, the agent remains at 11 (resp. 77) if she tries to move to the left (resp. right) of this state, and the agent remains stuck at s=1s=1 if she ever reaches this state.
* •

  r:S×A×P​(S×A)→ℝr:S\times A\times{\mathcal{}P}(S\times A)\to\mathbb{R} is given by

  |  |  |  |
  | --- | --- | --- |
  |  | r​(s,a,Λ)=−a2+q​a​(m​(Λ)−s)2−0.5​ϵ​(m​(Λ)−s)2+(m​(Λ)−starget)2,r(s,a,\Lambda)=-a^{2}+qa(m({\Lambda})-s)^{2}-0.5\epsilon(m({\Lambda})-s)^{2}+(m({\Lambda})-s\_{\mathrm{target}})^{2}, |  |

  where m​(Λ)m({\Lambda}) is given by m​(Λ):=∫Ss′​pjS⁡(Λ)​(d​s′)m({\Lambda}):=\int\_{S}s^{\prime}\operatorname{pj}\_{S}(\Lambda)(ds^{\prime}) (i.e., the first moment of the state), the constants q,ϵq,\epsilon are non-positive and satisfy q2≤ϵq^{2}\leq\epsilon, and stargets\_{\mathrm{target}} is a target state taken equal to 22 in the experiments. The first term is a cost of borrowing / lending, the second and third terms have a mean-reverting effect, and the last term means that the regulator has a target level for the mean of the log-reserves. Here, qq represents the incentive to borrowing or lending. We refer to [MR3325083] for more details.
* •

  β=0.15\beta=0.15 is the discount factor so that Assumptions [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii) and [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iv) are satisfied.

![Refer to caption](x5.png)


Figure 5. Three sample trajectories of the population distribution and corresponding action distribution for each state in Example 2.

![Refer to caption](x6.png)


Figure 6. Three sample trajectories of common noise, associated to the three distribution trajectories presented in Figure [5](https://arxiv.org/html/2511.04515v1#S3.F5 "Figure 5 ‣ 3.2. Financial systemic risk ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty").

For the common noise probability measure, we proceed as in the previous example of Section [3.1](https://arxiv.org/html/2511.04515v1#S3.SS1 "3.1. Example 1: Distribution matching ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty"). The true common noise measure is denoted by ptrue∈P​(E0)p\_{\textrm{true}}\in{\mathcal{}P}(E^{0}) (as in ([3.1](https://arxiv.org/html/2511.04515v1#S3.E1 "In 1st item ‣ 3.1. Example 1: Distribution matching ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty")), but now represented by a 5-dimensional probability vetor vtrue∈[0,1]5v\_{\textrm{true}}\in[0,1]^{5}). The central planner does not know this true measure and instead relies on a reference probability measure pref∈P​(E0)p\_{\textrm{ref}}\in{\mathcal{}P}(E^{0}) with corresponding probability vector vref∈[0,1]5v\_{\textrm{ref}}\in[0,1]^{5}. We then compare, in the true model with ptruep\_{\textrm{true}}, the performance of πref\pi\_{\textrm{ref}} (an optimal policy for the model with common noise distribution prefp\_{\textrm{ref}}) and the performance of πrobust\pi\_{\textrm{robust}} (a robust policy for prefp\_{\textrm{ref}}). The uncertainty set 𝔓0\mathfrak{P}^{0} is defined as in ([3.2](https://arxiv.org/html/2511.04515v1#S3.E2 "In 3.1. Example 1: Distribution matching ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty")), but adapted to the 5-dimensional setting so that Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i) also holds.

We implement the above model with: vtrue=(0.1,0.2,0.4,0.2,0.1)v\_{\textrm{true}}=(0.1,0.2,0.4,0.2,0.1), vref=(0,0,1,0,0)v\_{\textrm{ref}}=(0,0,1,0,0) and δperturb\delta\_{\textrm{perturb}} varying between 0.00.0 and 0.60.6. Figure [4](https://arxiv.org/html/2511.04515v1#S3.F4 "Figure 4 ‣ 3.2. Financial systemic risk ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty") shows that for moderately small δperturb\delta\_{\textrm{perturb}}, the robust policy performs better than the non-robust policy. For large values of δperturb\delta\_{\textrm{perturb}} however, the robust policy yields a smaller value: being robust against a large set of possible common noise distributions prevents the policy from performing well on the true distribution. The results are averaged over 15 different runs and the plots shows the mean value and its standard deviation. Figure [5](https://arxiv.org/html/2511.04515v1#S3.F5 "Figure 5 ‣ 3.2. Financial systemic risk ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty") shows three realizations of trajectories, starting from random initial distributions. We display a few time steps between 0 and 2020. We observe that the learnt policy is pure at the agent level, meaning that in each state, the agent uses one action with probability 11. In fact, the agent uses actions that tend to make the state move towards state 22 or 33. The distribution concentrates (but not completely due to the idiosyncratic noise which tends to make the agent spread). Moreover, the peak is not always at state 22 or 33 due to the impact of the common noise, whose trajectories are displayed in Figure [6](https://arxiv.org/html/2511.04515v1#S3.F6 "Figure 6 ‣ 3.2. Financial systemic risk ‣ 3. Numerical examples ‣ Robust mean-field control under common noise uncertainty").

## 4. Proof of results in Section [2.2](https://arxiv.org/html/2511.04515v1#S2.SS2 "2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We begin by verifying the measurability of the state dynamics appearing in both models. We recall the filtrations given in Definition [2.1](https://arxiv.org/html/2511.04515v1#S2.Thmthm1 "Definition 2.1 (Filtrations). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

###### Lemma 4.1.

For any π∈Π\pi\in\Pi and ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, the following statements hold:

* (i)

  For every N∈ℕN\in\mathbb{N}, i=1,…,Ni=1,\dots,N, and t≥0t\geq 0, sti,N,πs\_{t}^{i,N,\pi} given in ([2.3](https://arxiv.org/html/2511.04515v1#S2.E3 "In item (ii) ‣ Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) is (⋁j=1NFtj)\big(\bigvee\_{j=1}^{N}{\mathcal{}F}\_{t}^{j}\big) measurable.
* (ii)

  For every i∈ℕi\in\mathbb{N} and t≥0t\geq 0, sti,π,ℙs\_{t}^{i,\pi,\mathbb{P}} in ([2.4](https://arxiv.org/html/2511.04515v1#S2.E4 "In item (i) ‣ Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) is Fti{\mathcal{}F}^{i}\_{t} measurable, and both ℙ(sti,π,ℙ,ati,π)0\mathbb{P}^{0}\_{(s\_{t}^{i,\pi,\mathbb{P}},a\_{t}^{i,\pi})} and ℙsti,π,ℙ0\mathbb{P}\_{s\_{t}^{i,\pi,\mathbb{P}}}^{0} are Ft0{\mathcal{}F}\_{t}^{0} measurable.

###### Proof.

We start proving (i). Let N∈ℕN\in\mathbb{N} and i=1,…,Ni=1,\dots,N be given. The statement is shown via an induction over t≥0t\geq 0: Since s0i,N,π=ξi∈LF0i0​(S)s\_{0}^{i,N,\pi}=\xi^{i}\in L^{0}\_{{\mathcal{}F}\_{0}^{i}}(S) (see Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), the claim for t=0t=0 holds.

Now assume that the induction claim holds for some t≥0t\geq 0. Note that st+1i,N,πs\_{t+1}^{i,N,\pi} satisfies

|  |  |  |
| --- | --- | --- |
|  | st+1i,N,π=F⁡(sti,N,π,ati,π,1N​∑j=1Nδ(stj,N,π,atj,π),εt+1i,εt+10)s\_{t+1}^{i,N,\pi}=\operatorname{F}(s^{i,N,\pi}\_{t},a^{i,\pi}\_{t},\mbox{$\frac{1}{N}\sum\_{j=1}^{N}\delta\_{(s^{j,N,\pi}\_{t},a^{j,\pi}\_{t})}$},\varepsilon\_{t+1}^{i},\varepsilon\_{t+1}^{0}) |  |

where the first three terms are (⋁j=1NGtj)(\bigvee\_{j=1}^{N}{\mathcal{}G}\_{t}^{j}) measurable because of the induction assumption and
the definition of the open-loop control αti,π\alpha\_{t}^{i,\pi} in Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i), and the fact that ⋁j=1NFtj⊂⋁j=1NGtj\bigvee\_{j=1}^{N}{\mathcal{}F}\_{t}^{j}\subset\bigvee\_{j=1}^{N}{\mathcal{}G}\_{t}^{j}. Hence by the Borel measurability of F\operatorname{F}, st+1i,N,πs\_{t+1}^{i,N,\pi} is (⋁j=1NFt+1j)(\bigvee\_{j=1}^{N}{\mathcal{}F}\_{t+1}^{j}) measurable (see Definition [2.1](https://arxiv.org/html/2511.04515v1#S2.Thmthm1 "Definition 2.1 (Filtrations). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

By the induction hypothesis, the statement in (i) holds for all t≥0t\geq 0.

The part (ii) is also shown via an induction over tt given any i∈ℕi\in\mathbb{N}. Since s0i,π,ℙ=ξi∈LF0i0​(S)s\_{0}^{i,\pi,\mathbb{P}}=\xi^{i}\in L\_{{\mathcal{}F}\_{0}^{i}}^{0}(S) (see Definition [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), s0i,π,ℙs\_{0}^{i,\pi,\mathbb{P}} is F0i{\mathcal{}F}\_{0}^{i} measurable. Moreover, since F00{\mathcal{}F}\_{0}^{0} is trivial, both ℙ(s0i,π,ℙ,a0i,π)0\mathbb{P}^{0}\_{(s\_{0}^{i,\pi,\mathbb{P}},a\_{0}^{i,\pi})} and ℙs0i,π,ℙ0\mathbb{P}\_{s\_{0}^{i,\pi,\mathbb{P}}}^{0} are Ft0{\mathcal{}F}\_{t}^{0} measurable obviously.

We assume that the claim holds for some t≥0t\geq 0. Note that st+1i,π,ℙs\_{t+1}^{i,\pi,\mathbb{P}} satisfies

|  |  |  |
| --- | --- | --- |
|  | st+1i,π,ℙ=F⁡(sti,π,ℙ,ati,π,ℙ(sti,π,ℙ,ati,π)0,εt+1i,εt+10),s\_{t+1}^{i,\pi,\mathbb{P}}=\operatorname{F}(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t},\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})},\varepsilon\_{t+1}^{i},\varepsilon\_{t+1}^{0}), |  |

where the first three terms are Gti{\mathcal{}G}\_{t}^{i} measurable because of the induction assumption and the fact that Ft0⊂Gti{\mathcal{}F}\_{t}^{0}\subset{\mathcal{}G}\_{t}^{i}. Hence by the Borel measurability of F\operatorname{F}, st+1i,π,ℙs\_{t+1}^{i,\pi,\mathbb{P}} is Ft+1i{\mathcal{}F}\_{t+1}^{i} measurable (see Definition [2.1](https://arxiv.org/html/2511.04515v1#S2.Thmthm1 "Definition 2.1 (Filtrations). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

Moreover, since at+1i,πa^{i,\pi}\_{t+1} is Gt+1i{\mathcal{}G}\_{t+1}^{i} measurable and
(γi,ϑ0:t+1i,ε1:t+1i)(\gamma^{i},\vartheta\_{0:t+1}^{i},\varepsilon^{i}\_{1:t+1}) is independent of ε1:t+10\varepsilon^{0}\_{1:t+1} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)), we apply Lemma [A.1](https://arxiv.org/html/2511.04515v1#A1.Thmthm1 "Lemma A.1. ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty") (ii) to have that both ℙ(st+1i,π,ℙ,at+1i,π)0\mathbb{P}^{0}\_{(s\_{t+1}^{i,\pi,\mathbb{P}},a\_{t+1}^{i,\pi})} and ℙst+1i,π,ℙ0\mathbb{P}\_{s\_{t+1}^{i,\pi,\mathbb{P}}}^{0} are Ft+10{\mathcal{}F}\_{t+1}^{0} measurable. By the induction hypothesis, the statement in (ii) holds.
∎

### 4.1. Proof of Lemma [2.8](https://arxiv.org/html/2511.04515v1#S2.Thmthm8 "Lemma 2.8. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We start proving (i). Let q>2q>2 be given. Note that by Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty") (ii), the definition of open-loop controls (see Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)), and recalling that 𝔽i⊂𝔾i\mathbb{F}^{i}\subset\mathbb{G}^{i} for any i∈ℕi\in\mathbb{N} (sti,π,ℙ,ati,π)(s\_{t}^{i,\pi,\mathbb{P}},a\_{t}^{i,\pi}) is Gti{\mathcal{}G}\_{t}^{i} measurable.

Moreover, since the private components (γi)i∈ℕ(\gamma^{i})\_{i\in\mathbb{N}}, (ϑti)t≥0,i∈ℕ(\vartheta\_{t}^{i})\_{t\geq 0,i\in\mathbb{N}}, and (εti)t≥1,i∈ℕ(\varepsilon\_{t}^{i})\_{t\geq 1,i\in\mathbb{N}} are mutually independent (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)) and all agents are indistinguishable, it holds for every t≥0t\geq 0, π∈Π\pi\in\Pi, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q} that (sti,π,ℙ,ati,π)i∈ℕ(s\_{t}^{i,\pi,\mathbb{P}},a\_{t}^{i,\pi})\_{i\in\mathbb{N}} is (conditionally) i.i.d. given the common noise information Ft0{\mathcal{}F}^{0}\_{t} with law ℙ(st1,π,ℙ,at1,π)0\mathbb{P}^{0}\_{(s\_{t}^{1,\pi,\mathbb{P}},a\_{t}^{1,\pi})}. Therefore, it follows from [fournier2015rate, Theorem 1] that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ0​[WP​(S×A)​(1N​∑i=1Nδ(sti,π,ℙ,ati,π),ℙ(st1,π,ℙ,at1,π)0)]≤C​(Kq​(ℙ(st1,π,ℙ,at1,π)0))1/q​α​(N),\mathbb{E}^{\mathbb{P}^{0}}\Big[{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}\big(\mbox{$\frac{1}{N}\sum\_{i=1}^{N}\delta\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})}$},\,\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})}\big)\Big]\leq C\big(K\_{q}(\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})})\big)^{1/q}\alpha(N), |  |

where C>0C>0 does not depends on ℙ0\mathbb{P}^{0} and NN but on dd and qq, α​(⋅)\alpha(\cdot) is defined as in the statment, and Kq​(ℙ(st1,π,ℙ,at1,π)0)K\_{q}(\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})}) is given by

|  |  |  |
| --- | --- | --- |
|  | Kq​(ℙ(st1,π,ℙ,at1,π)0):=∫S×A|(s,a)|q​ℙ(st1,π,ℙ,at1,π)0​(d​s,d​a).K\_{q}(\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})}):=\int\_{S\times A}|(s,a)|^{q}\;\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})}(ds,da). |  |

Since S×AS\times A is a compact subset of ℝd\mathbb{R}^{d}, the above quantitiy is uniformly bounded by (ΔS×A)q(\Delta\_{S\times A})^{q} for every t≥0t\geq 0, π∈Π\pi\in\Pi, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q}. Hence the estimate in part (i) holds.

Last, we prove (ii). Let q>2q>2 be given. In part (i), we have verified that for every t≥0t\geq 0, π∈Π\pi\in\Pi, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, (sti,π,ℙ,ati,π)i∈ℕ(s\_{t}^{i,\pi,\mathbb{P}},a\_{t}^{i,\pi})\_{i\in\mathbb{N}} is (conditionally) i.i.d. given Ft0{\mathcal{}F}^{0}\_{t} with law ℙ(st1,π,ℙ,at1,π)0\mathbb{P}^{0}\_{(s\_{t}^{1,\pi,\mathbb{P}},a\_{t}^{1,\pi})}.

Hence, we can apply [boissard2014mean, Corollary 1.2] to obtain that for every t≥0t\geq 0, π∈Π\pi\in\Pi, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q}

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ0​[WP​(S×A)​(1N​∑i=1Nδ(sti,π,ℙ,ati,π),ℙ(st1,π,ℙ,at1,π)0)]≤c​(2q−2)2q​(kS×A)1q​ΔS×A​N−1q,\mathbb{E}^{\mathbb{P}^{0}}\Big[{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}\big(\mbox{$\frac{1}{N}\sum\_{i=1}^{N}\delta\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})}$},\,\mathbb{P}^{0}\_{(s^{1,\pi,\mathbb{P}}\_{t},a^{1,\pi}\_{t})}\big)\Big]\leq c\Big(\frac{2}{q-2}\Big)^{\frac{2}{q}}(k\_{S\times A})^{\frac{1}{q}}\Delta\_{S\times A}N^{-\frac{1}{q}}, |  |

with some c≤64/3c\leq 64/3. Therefore, we can obtain the estimate in part (ii), as claimed. ∎

### 4.2. Proof of Theorem [2.9](https://arxiv.org/html/2511.04515v1#S2.Thmthm9 "Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

For notational simplicity, throuhgout this proof, denote for every N∈ℕN\in\mathbb{N}, i=1,…,Ni=1,\dots,N, t≥0t\geq 0, π∈Π\pi\in\Pi, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q} by

|  |  |  |
| --- | --- | --- |
|  | ΛtN,π:=1N​∑j=1Nδ(stj,N,π,atj,π),ΛtN,∞,π,ℙ:=1N​∑j=1Nδ(stj,π,ℙ,atj,π),Λ~ti,π,ℙ:=ℙ(sti,π,ℙ,ati,π)0.\displaystyle\begin{aligned} &\Lambda\_{t}^{N,\pi}:=\mbox{$\frac{1}{N}\sum\_{j=1}^{N}\delta\_{(s^{j,N,\pi}\_{t},a^{j,\pi}\_{t})}$},\qquad\Lambda\_{t}^{N,\infty,\pi,\mathbb{P}}:=\mbox{$\frac{1}{N}\sum\_{j=1}^{N}\delta\_{(s^{j,\pi,\mathbb{P}}\_{t},a^{j,\pi}\_{t})}$},\\ &\tilde{\Lambda}\_{t}^{i,\pi,\mathbb{P}}:=\mathbb{P}^{0}\_{(s^{i,\pi,\mathbb{P}}\_{t},a^{i,\pi}\_{t})}.\end{aligned} |  |

Let N∈ℕN\in\mathbb{N} and i=1,…,Ni=1,\dots,N be given. We first prove ([2.7](https://arxiv.org/html/2511.04515v1#S2.E7 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.8](https://arxiv.org/html/2511.04515v1#S2.E8 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). The proof uses an induction over t≥0t\geq 0: Since s0i,N,π=s0i,π,ℙs^{i,N,\pi}\_{0}=s\_{0}^{i,\pi,\mathbb{P}} for every π∈Π\pi\in\Pi, and ℙ∈Q\mathbb{P}\in{\mathcal{}Q} (see Definitions [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.6](https://arxiv.org/html/2511.04515v1#S2.Thmthm6 "Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), the claim for t=0t=0 holds.

Now assume that the induction claim holds true for some t≥1t\geq 1. Let π∈Π\pi\in\Pi and ℙ∈Q\mathbb{P}\in{\mathcal{}Q} be given.
Since ⋁j=1NFtj⊂⋁j=1NGtj\bigvee\_{j=1}^{N}{\mathcal{}F}\_{t}^{j}\subset\bigvee\_{j=1}^{N}{\mathcal{}G}\_{t}^{j} (see Definition [2.1](https://arxiv.org/html/2511.04515v1#S2.Thmthm1 "Definition 2.1 (Filtrations). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), both sti,N,πs\_{t}^{i,N,\pi} given in ([2.3](https://arxiv.org/html/2511.04515v1#S2.E3 "In item (ii) ‣ Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and sti,π,ℙs\_{t}^{i,\pi,\mathbb{P}} given in ([2.4](https://arxiv.org/html/2511.04515v1#S2.E4 "In item (i) ‣ Definition 2.6 (MFC model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) are (⋁j=1NGtj)(\bigvee\_{j=1}^{N}{\mathcal{}G}\_{t}^{j}) measurable
(see Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")).
Moreover, ati,πa\_{t}^{i,\pi} is Gti{\mathcal{}G}\_{t}^{i} measurable (see Definition [2.5](https://arxiv.org/html/2511.04515v1#S2.Thmthm5 "Definition 2.5 (𝑁-agent model). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)).

Since εt+1i\varepsilon\_{t+1}^{i} is independent of ⋁j=1NGtj\bigvee\_{j=1}^{N}{\mathcal{}G}\_{t}^{j} and εt+10\varepsilon\_{t+1}^{0} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i), (ii)), we can have the following conditioning

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | 𝔼ℙ​[dS​(st+1i,N,π,st+1i,π,ℙ)]=𝔼ℙ​[Di,ℙ⁡(sti,N,π,sti,π,ℙ,ati,π,ℙ,ΛtN,π,Λ~ti,π,ℙ,e0)],\displaystyle\mathbb{E}^{\mathbb{P}}[d\_{S}(s^{i,N,\pi}\_{t+1},s^{i,\pi,\mathbb{P}}\_{t+1})]=\mathbb{E}^{\mathbb{P}}[\operatorname{D}^{i,\mathbb{P}}(s^{i,N,\pi}\_{t},s^{i,\pi,\mathbb{P}}\_{t},a\_{t}^{i,\pi,\mathbb{P}},\Lambda\_{t}^{N,\pi},\tilde{\Lambda}\_{t}^{i,\pi,\mathbb{P}},e^{0})], |  |

where for every (s,s~)∈S(s,\tilde{s})\in S, a∈Aa\in A, Λ,Λ~∈P​(S×A)\Lambda,\tilde{\Lambda}\in{\mathcal{}P}(S\times A), and e0∈E0e^{0}\in E^{0}

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | Di,ℙ⁡(s,s~,a,Λ,Λ~,e0):=∫EdS​(F⁡(s,a,Λ,e,e0),F⁡(s~,a,Λ~,e,e0))​λε​(d​e)≤CF​(dS​(s,s~)+𝒲P​(S×A)​(Λ,Λ~)),\displaystyle\begin{aligned} \operatorname{D}^{i,\mathbb{P}}(s,\tilde{s},a,\Lambda,\tilde{\Lambda},e^{0}):=&\int\_{E}d\_{S}\big(\operatorname{F}(s,a,\Lambda,e,e^{0}),\operatorname{F}(\tilde{s},a,\tilde{\Lambda},e,e^{0})\big)\lambda\_{\varepsilon}(de)\\ \leq&C\_{\operatorname{F}}\big(d\_{S}(s,\tilde{s})+\mathcal{W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})\big),\end{aligned} |  |

where the inequality follows from Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i).

On the other hand, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[𝒲P​(S×A)​(ΛtN,π,Λ~ti,π,ℙ)]\displaystyle\mathbb{E}^{\mathbb{P}}[\mathcal{W}\_{{\mathcal{}P}(S\times A)}(\Lambda\_{t}^{N,\pi},\tilde{\Lambda}\_{t}^{i,\pi,\mathbb{P}})] | ≤𝔼ℙ​[𝒲P​(S×A)​(ΛtN,π,ΛtN,∞,π,ℙ)]+𝔼ℙ​[𝒲P​(S×A)​(ΛtN,∞,π,ℙ,Λ~ti,π,ℙ)]\displaystyle\leq\mathbb{E}^{\mathbb{P}}[\mathcal{W}\_{{\mathcal{}P}(S\times A)}(\Lambda\_{t}^{N,\pi},\Lambda\_{t}^{N,\infty,\pi,\mathbb{P}})]+\mathbb{E}^{\mathbb{P}}[\mathcal{W}\_{{\mathcal{}P}(S\times A)}(\Lambda\_{t}^{N,\infty,\pi,\mathbb{P}},\tilde{\Lambda}\_{t}^{i,\pi,\mathbb{P}})] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.3) |  |  | ≤𝔼ℙ​[dS​(sti,N,π,sti,π,ℙ)]+MN,\displaystyle\leq\mathbb{E}^{\mathbb{P}}[d\_{S}(s^{i,N,\pi}\_{t},s^{i,\pi,\mathbb{P}}\_{t})]+M\_{N}, |  |

where the second inequality follows from the definition of MNM\_{N} given in ([2.6](https://arxiv.org/html/2511.04515v1#S2.E6 "In 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and the fact that 𝒲P​(S×A)​(ΛtN,π,ΛtN,∞,π,ℙ)≤1N​∑j=1NdS​(stj,N,π,stj,π,ℙ)\mathcal{W}\_{{\mathcal{}P}(S\times A)}(\Lambda\_{t}^{N,\pi},\Lambda\_{t}^{N,\infty,\pi,\mathbb{P}})\leq\frac{1}{N}\sum\_{j=1}^{N}d\_{S}(s^{j,N,\pi}\_{t},s^{j,\pi,\mathbb{P}}\_{t}) together with the indistinguishability.

Combining ([4.1](https://arxiv.org/html/2511.04515v1#S4.E1 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")) with ([4.2](https://arxiv.org/html/2511.04515v1#S4.E2 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")) and ([4.3](https://arxiv.org/html/2511.04515v1#S4.E3 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")), we have that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | 𝔼ℙ​[dS​(st+1i,N,π,st+1i,π,ℙ)]≤CF​(2​𝔼ℙ​[dS​(sti,N,π,sti,π,ℙ)]+MN).\displaystyle\mathbb{E}^{\mathbb{P}}[d\_{S}(s^{i,N,\pi}\_{t+1},s^{i,\pi,\mathbb{P}}\_{t+1})]\leq C\_{\operatorname{F}}\big(2\mathbb{E}^{\mathbb{P}}[d\_{S}(s^{i,N,\pi}\_{t},s^{i,\pi,\mathbb{P}}\_{t})]+M\_{N}\big). |  |

Since the estimate ([4.4](https://arxiv.org/html/2511.04515v1#S4.E4 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")) holds for any π∈Π\pi\in\Pi and ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, by the induction hypothesis we have that the estimate ([2.7](https://arxiv.org/html/2511.04515v1#S2.E7 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds for all t≥0t\geq 0, as claimed.

Moreover, since the estimate ([4.3](https://arxiv.org/html/2511.04515v1#S4.E3 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")) holds for any π∈Π\pi\in\Pi and ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, by using ([2.7](https://arxiv.org/html/2511.04515v1#S2.E7 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) we have that the other estimate ([2.8](https://arxiv.org/html/2511.04515v1#S2.E8 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds for all t≥0t\geq 0, as claimed. As N∈ℕN\in\mathbb{N} and i=1,…,Ni=1,\dots,N are given arbitrary, we can conclude that ([2.7](https://arxiv.org/html/2511.04515v1#S2.E7 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.8](https://arxiv.org/html/2511.04515v1#S2.E8 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) hold for all N∈ℕN\in\mathbb{N}, i=1,…,Ni=1,\dots,N, and t≥0t\geq 0.

We now prove ([2.9](https://arxiv.org/html/2511.04515v1#S2.E9 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Note that for every N∈ℕN\in\mathbb{N} and π∈Π\pi\in\Pi

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | |JN,π−Jπ|=|infℙ∈Q𝔼ℙ​[1N​∑i=1NRi,N,π]−infℙ∈Q𝔼ℙ​[1N​∑i=1NRi,π,ℙ]|≤supℙ∈Q1N​∑i=1N𝔼ℙ​[|Ri,N,π−Ri,π,ℙ|]=supℙ∈Q𝔼ℙ​[|R1,N,π−R1,π,ℙ|]≤∑t=0∞βtsupℙ∈Q𝔼ℙ[|r(st1,N,π,at1,π,,ΛtN,π)−r(st1,π,ℙ,at1,π,Λ~t1,π,ℙ)|]=:IN,π,\displaystyle\begin{aligned} &\big|{\mathcal{}J}^{N,\pi}-{\mathcal{}J}^{\pi}\big|=\bigg|\inf\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\bigg[\frac{1}{N}\sum\_{i=1}^{N}R^{i,N,\pi}\bigg]-\inf\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\bigg[\frac{1}{N}\sum\_{i=1}^{N}R^{i,\pi,\mathbb{P}}\bigg]\bigg|\\ &\qquad\leq\sup\_{\mathbb{P}\in{\mathcal{}Q}}\frac{1}{N}\sum\_{i=1}^{N}\mathbb{E}^{\mathbb{P}}\Big[|R^{i,N,\pi}-R^{i,\pi,\mathbb{P}}|\Big]=\sup\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\Big[|R^{1,N,\pi}-R^{1,\pi,\mathbb{P}}|\Big]\\ &\qquad\leq\sum\_{t=0}^{\infty}\beta^{t}\sup\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\Big[\big|r(s\_{t}^{1,N,\pi},a\_{t}^{1,\pi,},\Lambda\_{t}^{N,\pi})-r(s\_{t}^{1,\pi,\mathbb{P}},a\_{t}^{1,\pi},\tilde{\Lambda}\_{t}^{1,\pi,\mathbb{P}})\big|\Big]=:\operatorname{I}^{N,\pi},\end{aligned} |  |

where the equalities follow from the indistinguishability and the last inequality holds because rr is bounded (see Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)).

Moreover, by the Lipschitz continuity of r​(⋅,a,⋅):S×P​(S×A)→ℝr(\cdot,a,\cdot):S\times{\mathcal{}P}(S\times A)\to\mathbb{R} for any a∈Aa\in A (see Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)), for every N∈ℕN\in\mathbb{N} and π∈Π\pi\in\Pi

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | IN,π≤Cr​∑t=0∞βt​supℙ∈Q𝔼ℙ​[dS​(st1,N,π,st1,π,ℙ)+WP​(S×A)​(ΛtN,π,Λ~t1,π,ℙ)]≤Cr​(2​∑t=0∞βt​δtN+MN1−β),\displaystyle\begin{aligned} \operatorname{I}^{N,\pi}&\leq C\_{r}\sum\_{t=0}^{\infty}\beta^{t}\sup\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}\Big[d\_{S}(s^{1,N,\pi}\_{t},s^{1,\pi,\mathbb{P}}\_{t})+{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda\_{t}^{N,\pi},\tilde{\Lambda}\_{t}^{1,\pi,\mathbb{P}})\Big]\\ &\leq C\_{r}\bigg(2\sum\_{t=0}^{\infty}\beta^{t}\delta\_{t}^{N}+\frac{M\_{N}}{1-\beta}\bigg),\end{aligned} |  |

where δtN:=supπ∈Πsupℙ∈Q𝔼ℙ​[dS​(st1,N,π,st1,π,ℙ)]\delta\_{t}^{N}:=\sup\_{\pi\in\Pi}\sup\_{\mathbb{P}\in{\mathcal{}Q}}\mathbb{E}^{\mathbb{P}}[d\_{S}\big(s^{1,N,\pi}\_{t},s^{1,\pi,\mathbb{P}}\_{t}\big)] for t≥0t\geq 0.

Since the estimate given in ([4.5](https://arxiv.org/html/2511.04515v1#S4.E5 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")) coincides with that of [motte2022mean, Theorem 2.1]—specifically Eq. (2.17) therein—and Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii) ensures that 2​β​Cr<12\beta C\_{r}<1, we can follow the same calculations as in the proof of [motte2022mean, Theorem 2.1] (replacing KFK\_{F} with CrC\_{r}). This yields that ∑t=0∞βt​δtN≤C​MN\sum\_{t=0}^{\infty}\beta^{t}\delta\_{t}^{N}\leq CM\_{N} for some constant C>0C>0 (that do not depend on NN and π\pi); see also [motte2022mean, Remark 2.4].

Combining this with ([4.5](https://arxiv.org/html/2511.04515v1#S4.E5 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")) and ([4.6](https://arxiv.org/html/2511.04515v1#S4.E6 "In 4.2. Proof of Theorem 2.9 ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty")) establishes the estimate in ([2.9](https://arxiv.org/html/2511.04515v1#S2.E9 "In Theorem 2.9. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). ∎

## 5. Proof of results in Section [2.3](https://arxiv.org/html/2511.04515v1#S2.SS3 "2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

### 5.1. Proof of Proposition [2.12](https://arxiv.org/html/2511.04515v1#S2.Thmthm12 "Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We first prove ([2.18](https://arxiv.org/html/2511.04515v1#S2.E18 "In Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). For simplicity, denote for every t≥0t\geq 0 by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | μt:=μtξ,a,ℙ,Λt:=Λtξ,a,ℙ,νt+1:=ℒℙ​(εt+10|Ft0).\displaystyle\mu\_{t}:=\mu\_{t}^{\xi,a,\mathbb{P}},\qquad\Lambda\_{t}:=\Lambda\_{t}^{\xi,a,\mathbb{P}},\qquad\nu\_{t+1}:=\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{t+1}^{0}|{\mathcal{}F}\_{t}^{0}). |  |

Since μt+1\mu\_{t+1} is Ft+10{\mathcal{}F}\_{t+1}^{0} measurable, it is sufficient to show that for any bounded Borel measurable functions g^:(E0)t+1→ℝ\hat{g}:(E^{0})^{t+1}\to\mathbb{R} and f^:S→ℝ\hat{f}:S\to\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
| (5.2) |  | 𝔼ℙ​[g^​(ε1:t+10)​f^​(st+1ξ,a,ℙ)]=𝔼ℙ​[g^​(ε1:t+10)​∫Sf^​(s′)​F¯​(pjS⁡(Λt),Λt,εt+10)​(d​s′)],\displaystyle\mathbb{E}^{\mathbb{P}}[\hat{g}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,a,\mathbb{P}})]=\mathbb{E}^{\mathbb{P}}\bigg[\hat{g}(\varepsilon^{0}\_{1:t+1})\int\_{S}\hat{f}(s^{\prime})\overline{\mathrm{F}}(\operatorname{pj}\_{S}(\Lambda\_{t}),\Lambda\_{t},\varepsilon\_{t+1}^{0})(ds^{\prime})\bigg], |  |

where we note that (pjS⁡(Λt),Λt)∈gr⁡(𝔘)(\operatorname{pj}\_{S}(\Lambda\_{t}),\Lambda\_{t})\in\operatorname{gr}(\mathfrak{U}) (see Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)).

Note that by Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i) and (ii), εt+1\varepsilon\_{t+1} is independent of ε1:t+10,st,at,ℙ(st,at)0\varepsilon\_{1:t+1}^{0},s\_{t},a\_{t},\mathbb{P}\_{(s\_{t},a\_{t})}^{0} (since they are all Gt∨σ​(εt+10){\mathcal{}G}\_{t}\vee\sigma(\varepsilon\_{t+1}^{0}) measurable) with ℒℙ​(εt+1)=λε\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{t+1})=\lambda\_{\varepsilon}. Moreover, by ([2.12](https://arxiv.org/html/2511.04515v1#S2.E12 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and Fubini’s theorem (noting that g^\hat{g} and f^\hat{f} are both bounded)

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[g^​(ε1:t+10)​f^​(st+1ξ,a,ℙ)]\displaystyle\mathbb{E}^{\mathbb{P}}[\hat{g}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,a,\mathbb{P}})] | =𝔼ℙ​[𝔼ℙ​[g^​(ε1:t+10)​f^​(F⁡(stξ,a,ℙ,at,Λt,εt+1,εt+10))|e=εt+1]]\displaystyle=\mathbb{E}^{\mathbb{P}}\bigg[\mathbb{E}^{\mathbb{P}}\Big[\hat{g}(\varepsilon\_{1:t+1}^{0})\hat{f}(\operatorname{F}(s^{\xi,a,\mathbb{P}}\_{t},a\_{t},\Lambda\_{t},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0}))\Big|\,e=\varepsilon\_{t+1}\Big]\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫E𝔼ℙ[g^(ε1:t+10)f^(F(stξ,a,ℙ,at,Λt,e,εt+10))]λε(de)=:I.\displaystyle=\int\_{E}\mathbb{E}^{\mathbb{P}}\bigg[\hat{g}(\varepsilon\_{1:t+1}^{0})\hat{f}(\operatorname{F}(s^{\xi,a,\mathbb{P}}\_{t},a\_{t},\Lambda\_{t},e,\varepsilon\_{t+1}^{0}))\bigg]\lambda\_{\varepsilon}(de)=:\operatorname{I}. |  |

Note that ε1:t0,stξ,a,ℙ,at,\varepsilon\_{1:t}^{0},s^{\xi,a,\mathbb{P}}\_{t},a\_{t}, and Λt\Lambda\_{t} are all Gt{\mathcal{}G}\_{t} measurable. Since εt+10\varepsilon\_{t+1}^{0} is conditionally independent of Gt{\mathcal{}G}\_{t} given Ft0{\mathcal{}F}\_{t}^{0} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)), by definition of νt+1\nu\_{t+1} (see ([5.1](https://arxiv.org/html/2511.04515v1#S5.E1 "In 5.1. Proof of Proposition 2.12 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")))

|  |  |  |
| --- | --- | --- |
|  | I=∫E𝔼ℙ​[𝔼ℙ​[∫E0g^​(ε1:t0,e0)​f^​(F⁡(stξ,a,ℙ,at,Λt,e,e0))​νt+1​(d​e0)|Ft0]]​λε​(d​e)=∫E𝔼ℙ[∫E0g^(ε1:t0,e0)𝔼ℙ[f^(F(stξ,a,ℙ,at,Λt,e,e0))|Ft0]νt+1(de0)]λε(de)=:II.\displaystyle\begin{aligned} \operatorname{I}&=\int\_{E}\mathbb{E}^{\mathbb{P}}\bigg[\mathbb{E}^{\mathbb{P}}\bigg[\int\_{E^{0}}\hat{g}(\varepsilon\_{1:t}^{0},e^{0})\hat{f}\big(\operatorname{F}(s^{\xi,a,\mathbb{P}}\_{t},a\_{t},\Lambda\_{t},e,e^{0})\big)\nu\_{t+1}(de^{0})\bigg|{\mathcal{}F}\_{t}^{0}\bigg]\bigg]\lambda\_{\varepsilon}(de)\\ &=\int\_{E}\mathbb{E}^{\mathbb{P}}\bigg[\int\_{E^{0}}\hat{g}(\varepsilon\_{1:t}^{0},e^{0})\mathbb{E}^{\mathbb{P}}\Big[\hat{f}(\operatorname{F}(s^{\xi,a,\mathbb{P}}\_{t},a\_{t},\Lambda\_{t},e,e^{0}))\Big|{\mathcal{}F}\_{t}^{0}\Big]\nu\_{t+1}(de^{0})\bigg]\lambda\_{\varepsilon}(de)=:\operatorname{II}.\end{aligned} |  |

Moreover by definition of Λt\Lambda\_{t} (see ([5.1](https://arxiv.org/html/2511.04515v1#S5.E1 "In 5.1. Proof of Proposition 2.12 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty"))) and Fubini’s theorem

|  |  |  |  |
| --- | --- | --- | --- |
|  | II\displaystyle\operatorname{II} | =∫E𝔼ℙ​[∫E0g^​(ε1:t0,e0)​∫S×Af^​(F⁡(s,a,Λt,e,e0))​Λt​(d​s,d​a)​νt+1​(d​e)]​λε​(d​e)\displaystyle=\int\_{E}\mathbb{E}^{\mathbb{P}}\bigg[\int\_{E^{0}}\hat{g}(\varepsilon\_{1:t}^{0},e^{0})\int\_{S\times A}\hat{f}({\operatorname{F}}(s,a,\Lambda\_{t},e,e^{0}))\Lambda\_{t}(ds,da)\nu\_{t+1}(de)\bigg]\lambda\_{\varepsilon}(de) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ​[g^​(ε1:t+10)​∫S×A×Ef^​(F⁡(s,a,Λt,e,εt+10))​Λt​(d​s,d​a)​λε​(d​e)].\displaystyle=\mathbb{E}^{\mathbb{P}}\bigg[\hat{g}(\varepsilon\_{1:t+1}^{0})\int\_{S\times A\times E}\hat{f}({\operatorname{F}}(s,a,\Lambda\_{t},e,\varepsilon\_{t+1}^{0}))\Lambda\_{t}(ds,da)\lambda\_{\varepsilon}(de)\bigg]. |  |

By definition of F¯\overline{\mathrm{F}} (see Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)), the last term above is equal to the second term given in ([5.2](https://arxiv.org/html/2511.04515v1#S5.E2 "In 5.1. Proof of Proposition 2.12 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), as claimed.

We now prove ([2.19](https://arxiv.org/html/2511.04515v1#S2.E19 "In Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Note that by Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii) (νt)t≥0(\nu\_{t})\_{t\geq 0} given in ([5.1](https://arxiv.org/html/2511.04515v1#S5.E1 "In 5.1. Proof of Proposition 2.12 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) satisfies ℙ\mathbb{P}-a.s.

|  |  |  |
| --- | --- | --- |
|  | ν1=p1,νt=pt(⋅|ε1:t−10)for all t≥2,\nu\_{1}=p\_{1},\quad\nu\_{t}=p\_{t}(\cdot|\varepsilon\_{1:t-1}^{0})\quad\mbox{for all $t\geq 2$}, |  |

where (pt)t≥1∈𝒦0(p\_{t})\_{t\geq 1}\in\mathcal{K}^{0} induces the measure ℙ∈Q\mathbb{P}\in{\mathcal{}Q}.

Let t≥1t\geq 1. It is sufficient to show that for any bounded Borel measurable function f~:P​(S)→ℝ\tilde{f}:{\mathcal{}P}(S)\to\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
| (5.3) |  | 𝔼ℙ​[f~​(μt+1)]=𝔼ℙ​[∫P​(S)f~​(μ′)​p¯​(d​μ′|pjS⁡(Λt),Λt,νt+1)].\displaystyle\mathbb{E}^{\mathbb{P}}[\tilde{f}(\mu\_{t+1})]=\mathbb{E}^{\mathbb{P}}\bigg[\int\_{{\mathcal{}P}(S)}\tilde{f}(\mu^{\prime})\overline{p}\big(d\mu^{\prime}|\operatorname{pj}\_{S}(\Lambda\_{t}),\Lambda\_{t},\nu\_{t+1}\big)\bigg]. |  |

By ([2.18](https://arxiv.org/html/2511.04515v1#S2.E18 "In Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), we have μt+1=F¯​(pjS⁡(Λt),Λt,εt+10)\mu\_{t+1}=\overline{\mathrm{F}}(\operatorname{pj}\_{S}(\Lambda\_{t}),\Lambda\_{t},\varepsilon\_{t+1}^{0}) ℙ\mathbb{P}-a.s.. Moreover, since εt+10\varepsilon\_{t+1}^{0} is conditionally independent of (pjS⁡(Λt),Λt)(\operatorname{pj}\_{S}(\Lambda\_{t}),\Lambda\_{t}) given Ft0{\mathcal{}F}\_{t}^{0} (as Λt\Lambda\_{t} is Gt{\mathcal{}G}\_{t} measurable) with ℒℙ​(εt+10|Ft0)=νt+1\mathscr{L}\_{\mathbb{P}}(\varepsilon^{0}\_{t+1}|{\mathcal{}F}\_{t}^{0})=\nu\_{t+1}, it follows that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ​[f~​(μt+1)]=𝔼ℙ​[𝔼ℙ​[f​(F¯​(pjS⁡(Λt),Λt,εt+10))|Ft0]]=𝔼ℙ​[∫E0f​(F¯​(pjS⁡(Λt),Λt,e0))​νt+1​(d​e0)].\displaystyle\mathbb{E}^{\mathbb{P}}[\tilde{f}(\mu\_{t+1})]=\mathbb{E}^{\mathbb{P}}\Big[\mathbb{E}^{\mathbb{P}}\big[f\big(\overline{\mathrm{F}}\big(\operatorname{pj}\_{S}(\Lambda\_{t}),\Lambda\_{t},\varepsilon\_{t+1}^{0}\big)\big)\big|{\mathcal{}F}\_{t}^{0}\big]\Big]=\mathbb{E}^{\mathbb{P}}\bigg[\int\_{E^{0}}f\big(\overline{\mathrm{F}}\big(\operatorname{pj}\_{S}(\Lambda\_{t}),\Lambda\_{t},e^{0}\big)\big)\nu\_{t+1}(de^{0})\bigg]. |  |

By definition of p¯\overline{p} (see Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)),
the claim ([5.3](https://arxiv.org/html/2511.04515v1#S5.E3 "In 5.1. Proof of Proposition 2.12 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) holds.

For the case t=0t=0, note that ℒℙ​(ε10)=p1\mathscr{L}\_{\mathbb{P}}(\varepsilon^{0}\_{1})=p\_{1} and Λ0∈P​(S×A)\Lambda\_{0}\in{\mathcal{}P}(S\times A) is deterministic. Thus, it is straightforward to verify that ([2.19](https://arxiv.org/html/2511.04515v1#S2.E19 "In Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds also for t=0t=0.

This completes the proof. ∎

### 5.2. Proof of Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

In what follows, we often make use of the following coupling result along with the continuity of the projection map pjS:P​(S×A)→P​(S)\operatorname{pj}\_{S}:{\mathcal{}P}(S\times A)\to{\mathcal{}P}(S).

###### Lemma 5.1.

The following properties hold:

1. (i)

   For every (μ,ζ),(μ~,ζ~)∈P​(S)×P​(A)(\mu,\zeta),(\tilde{\mu},\tilde{\zeta})\in{\mathcal{}P}(S)\times{\mathcal{}P}(A) and every Λ∈CplS×A⁡(μ,ζ)\Lambda\in\operatorname{Cpl}\_{S\times A}(\mu,\zeta), there exists a coupling Λ~∗∈CplS×A⁡(μ~,ζ~)\tilde{\Lambda}^{\*}\in\operatorname{Cpl}\_{S\times A}(\tilde{\mu},\tilde{\zeta}) such that

   |  |  |  |
   | --- | --- | --- |
   |  | WP​(S×A)​(Λ,Λ~∗)≤WP​(S)​(μ,μ~)+WP​(A)​(ζ,ζ~).{\mathcal{}W}\_{{\mathcal{}P}({S\times A})}(\Lambda,\tilde{\Lambda}^{\*})\leq{\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu,\tilde{\mu})+{\mathcal{}W}\_{{\mathcal{}P}(A)}(\zeta,\tilde{\zeta}). |  |
2. (ii)

   For every Λ,Λ~∈P​(S×A)\Lambda,\tilde{\Lambda}\in{\mathcal{}P}(S\times A), it holds that

   |  |  |  |
   | --- | --- | --- |
   |  | WP​(S)​(pjS⁡(Λ),pjS⁡(Λ~))≤WP​(S×A)​(Λ,Λ~).{\mathcal{}W}\_{{\mathcal{}P}(S)}(\operatorname{pj}\_{S}(\Lambda),\operatorname{pj}\_{S}(\tilde{\Lambda}))\leq{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda}). |  |

   Thus pjS:P​(S×A)→P​(S)\operatorname{pj}\_{S}:{\mathcal{}P}(S\times A)\to{\mathcal{}P}(S) is continuous.

###### Proof.

We start by proving (i).
Let (μ,ζ),(μ~,ζ~)∈P​(S)×P​(A)(\mu,\zeta),(\tilde{\mu},\tilde{\zeta})\in{\mathcal{}P}(S)\times{\mathcal{}P}(A) and Λ∈CplS×A⁡(μ,ζ)\Lambda\in\operatorname{Cpl}\_{S\times A}(\mu,\zeta). Denote by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.4) |  | Γ∈CplS×S⁡(μ,μ~),Υ∈CplA×A⁡(ζ,ζ~)\displaystyle\Gamma\in\operatorname{Cpl}\_{S\times S}(\mu,\tilde{\mu}),\qquad\Upsilon\in\operatorname{Cpl}\_{A\times A}(\zeta,\tilde{\zeta}) |  |

the optimal couplings for WP​(S)​(μ,μ~){\mathcal{}W}\_{{\mathcal{}P}({S})}(\mu,\tilde{\mu}) and WP​(A)​(ζ,ζ~){\mathcal{}W}\_{{\mathcal{}P}({A})}(\zeta,\tilde{\zeta}), respectively (whose existence is ensured by [villani2008optimal, Theorem 4.1]).
Then we define Ξ∈P​((S×A)2)\Xi\in{\mathcal{}P}((S\times A)^{2}) by

|  |  |  |
| --- | --- | --- |
|  | Ξ​(d​s,d​a,d​s~,d​a~):=Υζ​(d​a~|a)​Λμ​(d​a|s)​Γ​(d​s,d​s~),\displaystyle\Xi(ds,da,d\tilde{s},d\tilde{a}):=\Upsilon\_{\zeta}(d\tilde{a}|a)\Lambda\_{\mu}(da|s)\Gamma(ds,d\tilde{s}), |  |

where Λμ:S∋s↦Λμ​(d​a|s)∈P​(A)\Lambda\_{\mu}:S\ni s\mapsto\Lambda\_{\mu}(da|s)\in{\mathcal{}P}(A) denotes a disintegrating kernel of Λ\Lambda with respect to its marginal μ=pjS⁡(Λ)\mu=\operatorname{pj}\_{S}(\Lambda), i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.5) |  | Λ​(d​s,d​a)=Λμ​(d​a|s)​μ​(d​s).\displaystyle\Lambda(ds,da)=\Lambda\_{\mu}(da|s)\mu(ds). |  |

In a similar manner, Υζ:A∋a↦Υζ​(d​a~|a)∈P​(A)\Upsilon\_{\zeta}:A\ni a\mapsto\Upsilon\_{\zeta}(d\tilde{a}|a)\in{\mathcal{}P}(A) denotes a disintegrating kernel of Υ\Upsilon with respect to its marginal ζ=pjA⁡(Υ)\zeta=\operatorname{pj}\_{A}(\Upsilon).

Then, by ([5.4](https://arxiv.org/html/2511.04515v1#S5.E4 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) and ([5.5](https://arxiv.org/html/2511.04515v1#S5.E5 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), it holds that ∫(s~,a~)∈S×AΞ​(d​s,d​a,d​s~,d​a~)=Λ​(d​s,d​a).\int\_{(\tilde{s},\tilde{a})\in S\times A}\Xi(ds,da,d\tilde{s},d\tilde{a})=\Lambda(ds,da). Moreover by setting Λ~⋄​(d​s~,d​a~):=∫(s,a)∈S×AΞ​(d​s,d​a,d​s~,d​a~)\tilde{\Lambda}^{\diamond}(d\tilde{s},d\tilde{a}):=\int\_{(s,a)\in S\times A}\Xi(ds,da,d\tilde{s},d\tilde{a}), we have that

|  |  |  |
| --- | --- | --- |
|  | Λ~⋄∈CplS×A⁡(μ~,ζ~),Ξ∈Cpl(S×A)2⁡(Λ,Λ~⋄).\displaystyle\tilde{\Lambda}^{\diamond}\in\operatorname{Cpl}\_{S\times A}(\tilde{\mu},\tilde{\zeta}),\qquad\Xi\in\operatorname{Cpl}\_{(S\times A)^{2}}(\Lambda,\tilde{\Lambda}^{\diamond}). |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | infΛ~∈CplS×A⁡(μ~,ζ~)WP​(S×A)​(Λ,Λ~)≤WP​(S×A)​(Λ,Λ~⋄)≤∫(S×A)2dS×A​((s,a),(s~,a~))​Ξ​(d​s,d​a,d​s~,d​a~)=∫S×SdS​(s,s~)​Γ​(d​s,d​s~)+∫A×AdA​(a,a~)​Υ​(d​a,d​a~)=WP​(S)​(μ,μ~)+WP​(A)​(ζ,ζ~),\displaystyle\begin{aligned} \inf\_{\tilde{\Lambda}\in\operatorname{Cpl}\_{S\times A}(\tilde{\mu},\tilde{\zeta})}{\mathcal{}W}\_{{\mathcal{}P}({S\times A})}(\Lambda,\tilde{\Lambda})\leq{\mathcal{}W}\_{{\mathcal{}P}({S\times A})}(\Lambda,\tilde{\Lambda}^{\diamond})&\leq\int\_{(S\times A)^{2}}d\_{S\times A}((s,a),(\tilde{s},\tilde{a}))\Xi(ds,da,d\tilde{s},d\tilde{a})\\ =&\int\_{S\times S}d\_{S}(s,\tilde{s})\Gamma(ds,d\tilde{s})+\int\_{A\times A}d\_{A}(a,\tilde{a})\Upsilon(da,d\tilde{a})\\ =&{\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu,\tilde{\mu})+{\mathcal{}W}\_{{\mathcal{}P}(A)}(\zeta,\tilde{\zeta}),\end{aligned} |  |

where the last equality follows from the optimality of Γ\Gamma and Υ\Upsilon (see ([5.4](https://arxiv.org/html/2511.04515v1#S5.E4 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty"))).

Combining this with the compactness of CplS×A⁡(μ~,ζ~)\operatorname{Cpl}\_{S\times A}(\tilde{\mu},\tilde{\zeta}) (see [villani2008optimal, Theorem 4.1 & Lemma 4.4]), one can choose Λ~∗∈CplS×A⁡(μ~,ζ~)\tilde{\Lambda}^{\*}\in\operatorname{Cpl}\_{S\times A}(\tilde{\mu},\tilde{\zeta}) so that

|  |  |  |
| --- | --- | --- |
|  | WP​(S×A)​(Λ,Λ~∗)=infΛ~∈CplS×A⁡(μ~,ζ~)WP​(S×A)​(Λ,Λ~)≤WP​(S)​(μ,μ~)+WP​(A)​(ζ,ζ~),{\mathcal{}W}\_{{\mathcal{}P}({S\times A})}(\Lambda,\tilde{\Lambda}^{\*})=\inf\_{\tilde{\Lambda}\in\operatorname{Cpl}\_{S\times A}(\tilde{\mu},\tilde{\zeta})}{\mathcal{}W}\_{{\mathcal{}P}({S\times A})}(\Lambda,\tilde{\Lambda})\leq{\mathcal{}W}\_{{\mathcal{}P}({S})}(\mu,\tilde{\mu})+{\mathcal{}W}\_{{\mathcal{}P}({A})}(\zeta,\tilde{\zeta}), |  |

as claimed.

Next we prove the part (ii). Let Λ,Λ~∈P​(S×A)\Lambda,\tilde{\Lambda}\in{\mathcal{}P}(S\times A). Denote by Ξ∗∈Cpl(S×A)2⁡(Λ,Λ~)\Xi^{\*}\in\operatorname{Cpl}\_{(S\times A)^{2}}(\Lambda,\tilde{\Lambda}) the optimal coupling for WP​(S×A)​(Λ,Λ~){\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda}). By setting h​(s,a):=sh(s,a):=s for every (s,a)∈S×A(s,a)\in S\times A (i.e., a projection map onto SS), denote by

|  |  |  |
| --- | --- | --- |
|  | Ξ⋄:=(Ξ∗∘(h×h)−1)∈P​(S×S)\Xi^{\diamond}:=\big(\Xi^{\*}\circ(h\times h)^{-1}\big)\in{\mathcal{}P}(S\times S) |  |

the push-forward of Ξ∗\Xi^{\*} by the map (h×h):(S×A)2→S2(h\times h):(S\times A)^{2}\to S^{2}.

Clearly Ξ⋄\Xi^{\diamond} is in CplS×S⁡(pjS⁡(Λ),pjS⁡(Λ~))\operatorname{Cpl}\_{S\times S}(\operatorname{pj}\_{S}(\Lambda),\operatorname{pj}\_{S}(\tilde{\Lambda})). Thus,

|  |  |  |
| --- | --- | --- |
|  | WP​(S)​(pjS⁡(Λ),pjS⁡(Λ~))≤∫S×SdS​(s,s~)​Ξ⋄​(d​s,d​s~)=∫(S×A)2dS​(h​(s,a),h​(s~,a~))​Ξ∗​(d​s,d​a,d​s~,d​a~).\displaystyle{\mathcal{}W}\_{{\mathcal{}P}(S)}(\operatorname{pj}\_{S}(\Lambda),\operatorname{pj}\_{S}(\tilde{\Lambda}))\leq\int\_{S\times S}d\_{S}(s,\tilde{s})\Xi^{\diamond}(ds,d\tilde{s})=\int\_{(S\times A)^{2}}d\_{S}(h(s,a),h(\tilde{s},\tilde{a}))\Xi^{\*}(ds,da,d\tilde{s},d\tilde{a}). |  |

Moreover, since dS​(h​(s,a),h​(s~,a~))=dS​(s,s~)≤dS×A​((s,a),(s~,a~))d\_{S}(h(s,a),h(\tilde{s},\tilde{a}))=d\_{S}(s,\tilde{s})\leq d\_{S\times A}((s,a),(\tilde{s},\tilde{a})) for every (s,a),(s~,a~)∈S×A(s,a),(\tilde{s},\tilde{a})\in S\times A, by the optimality of Ξ∗∈Cpl(S×A)2⁡(Λ,Λ~)\Xi^{\*}\in\operatorname{Cpl}\_{(S\times A)^{2}}(\Lambda,\tilde{\Lambda}), the assertion for the part (ii) holds, as claimed.
∎

The following lemma provides useful properties of the lifted functions defined in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

###### Lemma 5.2.

Suppose that Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii), (iii) are satisfied. Let 𝔘\mathfrak{U}, F¯\overline{\operatorname{F}}, r¯\overline{r} be given in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Then the following hold:

* (i)

  𝔘\mathfrak{U} is non-empty, compact-valued and continuous.666A correspondence between topological spaces is continuous if it is both lower- and upper-hemicontinuous (see,
  e.g., [CharalambosKim2006infinite, Definition 17.2, p. 558]).
* (ii)

  F¯\overline{\operatorname{F}} satisfies that for every (μ,Λ,e0),(μ~,Λ~,e~0)∈gr⁡(𝔘)×E0(\mu,\Lambda,e^{0}),(\tilde{\mu},\tilde{\Lambda},\tilde{e}^{0})\in\operatorname{gr}(\mathfrak{U})\times E^{0},

  |  |  |  |
  | --- | --- | --- |
  |  | WP​(S)​(F¯​(μ,Λ,e0),F¯​(μ~,Λ~,e~0))≤C¯F​(2​WP​(S×A)​(Λ,Λ~)+dE0​(e0,e~0)).\hskip 30.00005pt{\mathcal{}W}\_{{\mathcal{}P}(S)}\big(\overline{\operatorname{F}}(\mu,\Lambda,e^{0}),\overline{\operatorname{F}}(\tilde{\mu},\tilde{\Lambda},\tilde{e}^{0})\big)\leq\overline{C}\_{{\operatorname{F}}}\big(2{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})+d\_{E^{0}}(e^{0},\tilde{e}^{0})\big). |  |
* (iii)

  r¯\overline{r} is bounded. Furthermore, for every (μ,Λ),(μ~,Λ~)∈gr⁡(𝔘)(\mu,\Lambda),(\tilde{\mu},\tilde{\Lambda})\in\operatorname{gr}(\mathfrak{U})

  |  |  |  |
  | --- | --- | --- |
  |  | |r¯​(μ,Λ)−r¯​(μ~,Λ~)|≤2​C¯r​WP​(S×A)​(Λ,Λ~).|\overline{r}(\mu,\Lambda)-\overline{r}(\tilde{\mu},\tilde{\Lambda})|\leq 2\overline{C}\_{r}{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda}). |  |

###### Proof.

We start by proving (i). Both the non-emptyness and the compact-valuedness of 𝔘\mathfrak{U} are clear. Indeed, for every μ∈P​(S)\mu\in{\mathcal{}P}(S) one can consider the Dirac measure δa^​(d​a)∈P​(A)\delta\_{\hat{a}}(da)\in{\mathcal{}P}(A) at some a~∈A\tilde{a}\in A to obtain that δa~​(d​a)​μ​(d​s)∈𝔘​(μ).\delta\_{\tilde{a}}(da)\mu(ds)\in\mathfrak{U}(\mu). Therefore 𝔘​(μ)\mathfrak{U}(\mu) is non-empty.

Moreover, since pjS:P​(S×A)→P​(S)\operatorname{pj}\_{S}:{\mathcal{}P}(S\times A)\to{\mathcal{}P}(S) is continuous (see Lemma [5.1](https://arxiv.org/html/2511.04515v1#S5.Thmthm1 "Lemma 5.1. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (ii)) and P​(S×A){\mathcal{}P}(S\times A) is compact (as S×AS\times A is compact), 𝔘​(μ)⊆P​(S×A)\mathfrak{U}(\mu)\subseteq{\mathcal{}P}(S\times A) is compact for every μ∈P​(S)\mu\in{\mathcal{}P}(S), as claimed.

We now claim that 𝔘\mathfrak{U} is both upper and lower hemicontinuous. Let μ∈P​(S)\mu\in{\mathcal{}P}(S) be given.

Recalling that gr⁡(𝔘)={(μ,Λ)∈P​(S)×P​(S×A)|Λ∈𝔘​(μ)}\operatorname{gr}(\mathfrak{U})=\{(\mu,\Lambda)\in{\mathcal{}P}(S)\times{\mathcal{}P}(S\times A)\;|\;\Lambda\in\mathfrak{U}(\mu)\}, let us consider a sequence (μ(n),Λ(n))n∈ℕ∈gr⁡(𝔘)(\mu^{(n)},\Lambda^{(n)})\_{n\in\mathbb{N}}\in\operatorname{gr}(\mathfrak{U}) such that μ(n)⇀μ\mu^{(n)}\rightharpoonup\mu as n→∞n\to\infty. Since the subset gr⁡(𝔘)⊆P​(S)×P​(S×A)\operatorname{gr}(\mathfrak{U})\subseteq{\mathcal{}P}(S)\times{\mathcal{}P}(S\times A) is compact (by the continuity of pjS:P​(S×A)→P​(S)\operatorname{pj}\_{S}:{\mathcal{}P}(S\times A)\to{\mathcal{}P}(S) and the compactness of P​(S)×P​(S×A){\mathcal{}P}(S)\times{\mathcal{}P}(S\times A)), there exists a subsequence

|  |  |  |
| --- | --- | --- |
|  | (μ(nk),Λ(nk))k∈ℕ⊆(μ(n),Λ(n))n∈ℕs.t. (μ(nk),Λ(nk))⇀(μ⋆,Λ⋆) as k→∞(\mu^{(n\_{k})},\Lambda^{(n\_{k})})\_{k\in\mathbb{N}}\subseteq(\mu^{(n)},\Lambda^{(n)})\_{n\in\mathbb{N}}\quad\mbox{s.t. $(\mu^{(n\_{k})},\Lambda^{(n\_{k})})\rightharpoonup(\mu^{\star},\Lambda^{\star})$ as $k\to\infty$} |  |

with some (μ⋆,Λ⋆)∈Gr⁡(𝔘)(\mu^{\star},\Lambda^{\star})\in\operatorname{Gr}(\mathfrak{U}). Combined with the limit μ(n)⇀μ=μ⋆\mu^{(n)}\rightharpoonup\mu=\mu^{\star}, this ensures that (Λ(n))n∈ℕ(\Lambda^{(n)})\_{n\in\mathbb{N}} has a limit point Λ⋆∈𝔘​(μ)=𝔘​(μ⋆)\Lambda^{\star}\in\mathfrak{U}(\mu)=\mathfrak{U}(\mu^{\star}). Thus, by [CharalambosKim2006infinite, Theorem 17.20], 𝔘\mathfrak{U} is upper hemicontinuous.

It remains to show the lower hemicontinuity of 𝔘\mathfrak{U}. First note that for every μ∈P​(S)\mu\in{\mathcal{}P}(S) the set 𝔘​(μ)⊆P​(S×A)\mathfrak{U}(\mu)\subseteq{\mathcal{}P}(S\times A) can be represented by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.6) |  | 𝔘​(μ)=⋃ζ∈P​(A)CplS×A⁡(μ,ζ).\displaystyle\mathfrak{U}(\mu)=\bigcup\_{\zeta\in{\mathcal{}P}(A)}\operatorname{Cpl}\_{S\times A}(\mu,\zeta). |  |

Then we claim that CplS×A:P​(S)×P​(A)∋(μ,ζ)↠CplS×A⁡(μ,ζ)⊆P​(S×A)\operatorname{Cpl}\_{S\times A}:{\mathcal{}P}(S)\times{\mathcal{}P}(A)\ni(\mu,\zeta)\twoheadrightarrow\operatorname{Cpl}\_{S\times A}(\mu,\zeta)\subseteq{\mathcal{}P}(S\times A) is lower-hemicontinuous. To that end, let (μ,ζ)∈P​(S)×P​(A)(\mu,\zeta)\in{\mathcal{}P}(S)\times{\mathcal{}P}(A) and Λ∈CplS×A⁡(μ,ζ)\Lambda\in\operatorname{Cpl}\_{S\times A}(\mu,\zeta) be given, and consider a sequence (μ(n),ζ(n))n∈ℕ⊆P​(S)×P​(A)(\mu^{(n)},\zeta^{(n)})\_{n\in\mathbb{N}}\subseteq{\mathcal{}P}(S)\times{\mathcal{}P}(A) such that (μ(n),ζ(n))⇀(μ,ζ)(\mu^{(n)},\zeta^{(n)})\rightharpoonup(\mu,\zeta) as n→∞n\to\infty.

By Lemma [5.1](https://arxiv.org/html/2511.04515v1#S5.Thmthm1 "Lemma 5.1. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty"), for every n∈ℕn\in\mathbb{N} there exists Λ(n),∗∈CplS×A⁡(μ(n),ζ(n))\Lambda^{(n),\*}\in\operatorname{Cpl}\_{S\times A}(\mu^{(n)},\zeta^{(n)}) such that

|  |  |  |
| --- | --- | --- |
|  | WP​(S×A)​(Λ,Λ(n),∗)≤WP​(S)​(μ,μ(n))+WP​(A)​(ζ,ζ(n)).{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\Lambda^{(n),\*})\leq{\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu,\mu^{(n)})+{\mathcal{}W}\_{{\mathcal{}P}(A)}(\zeta,\zeta^{(n)}). |  |

Combined with the limit (μ(n),ζ(n))⇀(μ,ζ)(\mu^{(n)},\zeta^{(n)})\rightharpoonup(\mu,\zeta), this ensures that Λ(n),∗⇀Λ\Lambda^{(n),\*}\rightharpoonup\Lambda as n→∞n\rightarrow\infty. Thus, by [CharalambosKim2006infinite, Theorem 17.21], CplS×A\operatorname{Cpl}\_{S\times A} is lower hemicontinuous.

Moreover, by the lower hemicontinuity of CplS×A\operatorname{Cpl}\_{S\times A} and the representation given in ([5.6](https://arxiv.org/html/2511.04515v1#S5.E6 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), [CharalambosKim2006infinite, Theorem 17.27] asserts that 𝔘\mathfrak{U} is lower hemicontinuous. Therefore, 𝔘\mathfrak{U} is continuous, as claimed.

Now we prove the part (ii). Let (μ,Λ,e0),(μ~,Λ~,e~0)∈gr⁡(𝔘)×P​(E)×E0(\mu,\Lambda,e^{0}),(\tilde{\mu},\tilde{\Lambda},\tilde{e}^{0})\in\operatorname{gr}(\mathfrak{U})\times{\mathcal{}P}(E)\times E^{0}. For simplicity, let

|  |  |  |  |
| --- | --- | --- | --- |
| (5.7) |  | μ′:=F¯​(μ,Λ,e0),μ~′:=F¯​(μ~,Λ~,e~0).\displaystyle\begin{aligned} \mu^{\prime}:=\overline{\operatorname{F}}(\mu,\Lambda,e^{0}),\qquad\tilde{\mu}^{\prime}:=\overline{\operatorname{F}}(\tilde{\mu},\tilde{\Lambda},\tilde{e}^{0}).\end{aligned} |  |

Then, set idE:E∋e↦idE⁡(e):=(e,e)∈E2\operatorname{id}\_{E}:E\ni e\mapsto\operatorname{id}\_{E}(e):=(e,e)\in E^{2}. Then we denote the diagonal coupling of λε\lambda\_{\varepsilon} by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.8) |  | Ξ1:=λε∘(idE⁡(⋅))−1∈CplE×E⁡(λε,λε)\displaystyle\Xi\_{1}:=\lambda\_{\varepsilon}\circ(\operatorname{id}\_{E}(\cdot))^{-1}\in\operatorname{Cpl}\_{E\times E}(\lambda\_{\varepsilon},\lambda\_{\varepsilon}) |  |

so that WP​(E)​(λε,λε)=∫E×EdE​(e,e~)​Ξ1​(d​e,d​e~)=0{\mathcal{}W}\_{{\mathcal{}P}(E)}(\lambda\_{\varepsilon},\lambda\_{\varepsilon})=\int\_{E\times E}d\_{E}(e,\tilde{e})\Xi\_{1}(de,d\tilde{e})=0.

Furthermore, we denote the optimal coupling for WP​(S×A)​(Λ,Λ~){\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda}) (see [villani2008optimal, Theorem 4.1]) by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.9) |  | Ξ2∈Cpl(S×A)2⁡(Λ,Λ~).\displaystyle\Xi\_{2}\in\operatorname{Cpl}\_{(S\times A)^{2}}(\Lambda,\tilde{\Lambda}). |  |

Using the couplings Ξ1\Xi\_{1} and Ξ2\Xi\_{2}, we define a coupling Ξ3∈Cpl(S×A×E)2⁡(Λ⊗λε,Λ~⊗λε)\Xi\_{3}\in\operatorname{Cpl}\_{(S\times A\times E)^{2}}(\Lambda\otimes\lambda\_{\varepsilon},\tilde{\Lambda}\otimes\lambda\_{\varepsilon}) by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.10) |  | Ξ3​(d​s,d​a,d​e,d​s~,d​a~,d​e~):=Ξ1​(d​e,d​e~)​Ξ2​(d​s,d​a,d​s~,d​a~).\displaystyle\Xi\_{3}(ds,da,de,d\tilde{s},d\tilde{a},d\tilde{e}):=\Xi\_{1}(de,d\tilde{e})\Xi\_{2}(ds,da,d\tilde{s},d\tilde{a}). |  |

By the definition of F¯\overline{\operatorname{F}} (see Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)) and the setting ([5.7](https://arxiv.org/html/2511.04515v1#S5.E7 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), it holds that

|  |  |  |
| --- | --- | --- |
|  | Ξ3∘(F⁡(⋅,⋅,Λ,⋅,e0)×F⁡(⋅,⋅,Λ~,⋅,e~0))−1∈CplS×S⁡(μ′,μ~′),\Xi\_{3}\circ\big(\operatorname{F}(\cdot,\cdot,\Lambda,\cdot,e^{0})\times\operatorname{F}(\cdot,\cdot,\tilde{\Lambda},\cdot,\tilde{e}^{0})\big)^{-1}\in\operatorname{Cpl}\_{S\times S}(\mu^{\prime},\tilde{\mu}^{\prime}), |  |

i.e., the push-forward of Ξ3\Xi\_{3} by F⁡(⋅,⋅,Λ,⋅,e0)×F⁡(⋅,⋅,Λ~,⋅,e~0):(S,A,E)2→S2\operatorname{F}(\cdot,\cdot,\Lambda,\cdot,e^{0})\times\operatorname{F}(\cdot,\cdot,\tilde{\Lambda},\cdot,\tilde{e}^{0}):(S,A,E)^{2}\to S^{2}.

Then it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | WP​(S)​(μ′,μ~′)\displaystyle{\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu^{\prime},\tilde{\mu}^{\prime}) | ≤∫S×SdS​(s,s′)​(Ξ3∘(F⁡(⋅,⋅,Λ,⋅,e0)×F⁡(⋅,⋅,Λ~,⋅,e~0))−1)​(d​s,d​s′)\displaystyle\leq\int\_{S\times S}d\_{S}(s,s^{\prime})\big(\Xi\_{3}\circ(\operatorname{F}(\cdot,\cdot,\Lambda,\cdot,e^{0})\times\operatorname{F}(\cdot,\cdot,\tilde{\Lambda},\cdot,\tilde{e}^{0})\big)^{-1}\big)(ds,ds^{\prime}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.11) |  |  | =∫(S×A×E)2dS​(F⁡(s,a,Λ,e,e0),F⁡(s~,a~,Λ~,e~,e~0))​Ξ3​(d​s,d​a,d​e,d​s~,d​a~,d​e~)\displaystyle=\int\_{(S\times A\times E)^{2}}d\_{S}(\operatorname{F}(s,a,\Lambda,e,e^{0}),\operatorname{F}(\tilde{s},\tilde{a},\tilde{\Lambda},\tilde{e},\tilde{e}^{0}))\Xi\_{3}(ds,da,de,d\tilde{s},d\tilde{a},d\tilde{e}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(S×A)2∫EdS(F(s,a,Λ,e,e0),F(s~,a~,Λ~,e,e~0))λε(de)Ξ2(ds,da,ds~,da~)=:I,\displaystyle=\int\_{(S\times A)^{2}}\int\_{E}d\_{S}(\operatorname{F}(s,a,\Lambda,e,e^{0}),\operatorname{F}(\tilde{s},\tilde{a},\tilde{\Lambda},e,\tilde{e}^{0}))\lambda\_{\varepsilon}(de)\Xi\_{2}(ds,da,d\tilde{s},d\tilde{a})=:\operatorname{I}, |  |

where the last line follows from the definition of Ξ1\Xi\_{1} and Ξ3\Xi\_{3} (see ([5.8](https://arxiv.org/html/2511.04515v1#S5.E8 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), ([5.10](https://arxiv.org/html/2511.04515v1#S5.E10 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty"))) and by applying Fubini’s theorem (noting that F\operatorname{F} maps into the compact space SS).

By Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii) and the triangle inequality,

|  |  |  |
| --- | --- | --- |
|  | I≤C¯F​(∫(S×A)2dS×A​((s,a),(s~,a~))​Ξ2​(d​s,d​a,d​s~,d​a~)+WP​(S×A)​(Λ,Λ~)+dE0​(e0,e~0))=C¯F​(2​WP​(S×A)​(Λ,Λ~)+dE0​(e0,e~0)),\displaystyle\begin{aligned} \operatorname{I}\leq&\overline{C}\_{\operatorname{F}}\bigg(\int\_{(S\times A)^{2}}d\_{S\times A}\big((s,a),(\tilde{s},\tilde{a})\big)\Xi\_{2}(ds,da,d\tilde{s},d\tilde{a})+{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})+d\_{E^{0}}(e^{0},\tilde{e}^{0})\bigg)\\ =&\overline{C}\_{\operatorname{F}}\big(2{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})+d\_{E^{0}}(e^{0},\tilde{e}^{0})\big),\end{aligned} |  |

where the last equality follows from the optimality of Ξ2\Xi\_{2} (see ([5.9](https://arxiv.org/html/2511.04515v1#S5.E9 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty"))).

Combined with ([5.11](https://arxiv.org/html/2511.04515v1#S5.E11 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), this ensures the estimates for F¯\overline{\operatorname{F}} to hold.

We next prove the part (iii). Since SS, AA, and P​(S×A){\mathcal{}P}(S\times A) are all compact and rr is continuous (by Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i) and Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)), r¯\overline{r} is bounded. We prove its 2​C¯r2\overline{C}\_{r}-Lipschitz continuity. Let (μ,Λ),(μ~,Λ~)∈gr⁡(𝔘)(\mu,\Lambda),(\tilde{\mu},\tilde{\Lambda})\in\operatorname{gr}(\mathfrak{U}) be given. Then it follows from Assumption [2.14](https://arxiv.org/html/2511.04515v1#S2.Thmthm14 "Assumption 2.14. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii) and the triangle inequality that for every Ξ∈CplS×A⁡(Λ,Λ~)\Xi\in\operatorname{Cpl}\_{S\times A}(\Lambda,\tilde{\Lambda})

|  |  |  |
| --- | --- | --- |
|  | |r¯​(μ,Λ)−r¯​(μ~,Λ~)|=|∫(S×A)2(r​(s,a,Λ)−r​(s~,a~,Λ~))​Ξ​(d​s,d​a,d​s~,d​a~)|≤C¯r​(∫S×AdS×A​((s,a),(s~,a~))​Ξ​(d​s,d​a,d​s~,d​a~)+WP​(S×A)​(Λ,Λ~)).\displaystyle\begin{aligned} |\overline{r}(\mu,\Lambda)-\overline{r}(\tilde{\mu},\tilde{\Lambda})|&=\bigg|\int\_{(S\times A)^{2}}\big(r(s,a,\Lambda)-r(\tilde{s},\tilde{a},\tilde{\Lambda})\big)\Xi(ds,da,d\tilde{s},d\tilde{a})\bigg|\\ &\leq\overline{C}\_{r}\bigg(\int\_{S\times A}d\_{S\times A}\big((s,a),(\tilde{s},\tilde{a})\big)\Xi(ds,da,d\tilde{s},d\tilde{a})+{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda,\tilde{\Lambda})\bigg).\end{aligned} |  |

By taking inifimum over all Ξ∈CplS×A⁡(Λ,Λ~)\Xi\in\operatorname{Cpl}\_{S\times A}(\Lambda,\tilde{\Lambda}) into the above, we can obtain the estimate for r¯\overline{r}.

This completes the proof.
∎

Using the two preceding lemmas, we now proceed to prove Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

###### Proof of Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

We start by proving (i). Let L≥0L\geq 0 and V¯∈Lipb,L⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,L}({\mathcal{}P}(S);\mathbb{R}) be given. Set
S:=P​(S×A)×𝔓0.{\mathcal{}S}:={\mathcal{}P}(S\times A)\times\mathfrak{P}^{0}.
Recalling the definition of p¯\overline{p} (see Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)), define G:S∋(Λ,p)↦G​(Λ,p)∈ℝG:{\mathcal{}S}\ni(\Lambda,p)\mapsto G(\Lambda,p)\in\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.12) |  | G​(Λ,p):=∫P​(S)V¯​(μ′)​p¯​(d​μ′|pjS⁡(Λ),Λ,p)=∫E0V¯​(F¯​(pjS⁡(Λ),Λ,e0))​p​(d​e0).\displaystyle G(\Lambda,p):=\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\operatorname{pj}\_{S}(\Lambda),\Lambda,p)=\int\_{E^{0}}\overline{V}(\overline{\operatorname{F}}(\operatorname{pj}\_{S}(\Lambda),\Lambda,e^{0}))p(de^{0}). |  |

We claim that GG is continuous. Consider a sequence (Λ(n),p(n))n∈ℕ⊆S(\Lambda^{(n)},p^{(n)})\_{n\in\mathbb{N}}\subseteq{\mathcal{}S} such that (Λ(n),p(n))⇀(Λ⋆,p⋆)(\Lambda^{(n)},p^{(n)})\rightharpoonup(\Lambda^{\star},p^{\star}) as n→∞n\to\infty, with some (Λ⋆,p⋆)∈S(\Lambda^{\star},p^{\star})\in{\mathcal{}S}.

By the triangle inequality, for every n∈ℕn\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |G​(Λ(n),p(n))−G​(Λ⋆,p⋆)|\displaystyle\big|G(\Lambda^{(n)},p^{(n)})-G(\Lambda^{\star},p^{\star})\big| | ≤|G​(Λ⋆,p(n))−G​(Λ⋆,p⋆)|+|G​(Λ(n),p(n))−G​(Λ⋆,p(n))|\displaystyle\leq\big|G(\Lambda^{\star},p^{(n)})-G(\Lambda^{\star},p^{\star})\big|+\big|G(\Lambda^{(n)},p^{(n)})-G(\Lambda^{\star},p^{(n)})\big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:I(n)+II(n).\displaystyle=:\operatorname{I}^{(n)}+\operatorname{II}^{(n)}. |  |

We will show that I(n)\operatorname{I}^{(n)}and II(n)\operatorname{II}^{(n)} vanish as n→∞n\rightarrow\infty.

Since V¯∈Lipb,L⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,L}({\mathcal{}P}(S);\mathbb{R}) and F¯\overline{\operatorname{F}} is continuous (see Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (ii)), it holds that
g⋆​(⋅):=V¯​(F¯​(pjS⁡(Λ⋆),Λ⋆,⋅))∈Cb​(E0;ℝ)g^{\star}(\cdot):=\overline{V}(\overline{\operatorname{F}}(\operatorname{pj}\_{S}(\Lambda^{\star}),\Lambda^{\star},\cdot))\in C\_{b}(E\_{0};\mathbb{R}). Combined with the limit p(n)⇀p⋆p^{(n)}\rightharpoonup p^{\star}, this ensures that

|  |  |  |
| --- | --- | --- |
|  | limn→∞I(n)=limn→∞|∫E0g⋆​(e0)​p(n)​(d​e0)−∫E0g⋆​(e~0)​p⋆​(d​e~0)|=0.\displaystyle\lim\_{n\to\infty}\operatorname{I}^{(n)}=\lim\_{n\to\infty}\bigg|\int\_{E^{0}}g^{\star}(e^{0})p^{(n)}(de^{0})-\int\_{E^{0}}g^{\star}(\tilde{e}^{0})p^{\star}(d\tilde{e}^{0})\bigg|=0. |  |

It remains to show the limit of II(n)\operatorname{II}^{(n)}. We use the LL-Lipschitz continuity of V¯\overline{V}, the estimate of F¯\overline{\operatorname{F}} given in Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (ii), and the limits Λ(n)⇀Λ⋆\Lambda^{(n)}\rightharpoonup\Lambda^{\star} and p(n)⇀p⋆p^{(n)}\rightharpoonup p^{\star} to obtain

|  |  |  |
| --- | --- | --- |
|  | limn→∞II(n)≤limn→∞∫E0|V¯​(F¯​(pjS⁡(Λ(n)),Λ(n),e0))−V¯​(F¯​(pjS⁡(Λ⋆),Λ⋆,e0))|​p(n)​(d​e0)≤2​L​C¯F​limn→∞WP​(S×A)​(Λ(n),Λ⋆)=0.\displaystyle\begin{aligned} \lim\_{n\rightarrow\infty}\operatorname{II}^{(n)}&\leq\lim\_{n\rightarrow\infty}\int\_{E^{0}}\Big|\overline{V}\big(\overline{\operatorname{F}}(\operatorname{pj}\_{S}(\Lambda^{(n)}),\Lambda^{(n)},e^{0})\big)-\overline{V}\big(\overline{\operatorname{F}}(\operatorname{pj}\_{S}(\Lambda^{\star}),\Lambda^{\star},e^{0})\big)\Big|p^{(n)}(de^{0})\\ &\leq 2L\overline{C}\_{{\operatorname{F}}}\lim\_{n\rightarrow\infty}{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda^{(n)},\Lambda^{\star})=0.\end{aligned} |  |

Therefore GG given in ([5.12](https://arxiv.org/html/2511.04515v1#S5.E12 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) is continuous, as claimed.

Since 𝔓0\mathfrak{P}^{0} is compact (see Assumption [2.7](https://arxiv.org/html/2511.04515v1#S2.Thmthm7 "Assumption 2.7. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)) and GG is continuous, an application of Berge’s maximum theorem (see, e.g., [CharalambosKim2006infinite, Theorem 17.31]) ensures the continuity of the map J¯:P​(S×A)∋Λ↦J¯​(Λ)∈ℝ\overline{J}:{\mathcal{}P}(S\times A)\ni\Lambda\mapsto\overline{J}(\Lambda)\in\mathbb{R} given by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.13) |  | J¯​(Λ):=infp∈𝔓0∫P​(S)V¯​(μ′)​p¯​(d​μ′|pjS⁡(Λ),Λ,p),\displaystyle\overline{J}(\Lambda):=\inf\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\operatorname{pj}\_{S}(\Lambda),\Lambda,p), |  |

and the existence of the measurable selector p¯∗:P​(S×A)∋Λ↦p¯∗​(Λ)∈𝔓0\overline{p}^{\*}:{\mathcal{}P}(S\times A)\ni\Lambda\mapsto\overline{p}^{\*}(\Lambda)\in\mathfrak{P}^{0} satisfying ([2.23](https://arxiv.org/html/2511.04515v1#S2.E23 "In item (i) ‣ Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

We now prove the part (ii). In analogy to the part (i), the key idea is to apply Berge’s maximum theorem. To that end, we first show that a map H:gr⁡(𝔘)∈(μ,Λ)↦H​(μ,Λ)∈ℝH:\operatorname{gr}(\mathfrak{U})\in(\mu,\Lambda)\mapsto H(\mu,\Lambda)\in\mathbb{R} defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.14) |  | H​(μ,Λ):=r¯​(μ,Λ)+β⋅J¯​(Λ),\displaystyle H(\mu,\Lambda):=\overline{r}(\mu,\Lambda)+\beta\cdot\overline{J}(\Lambda), |  |

with J¯:P​(S×A)→ℝ\overline{J}:{\mathcal{}P}(S\times A)\to\mathbb{R} defined in ([5.13](https://arxiv.org/html/2511.04515v1#S5.E13 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) is continuous. That will be achieved in two steps.

Consider a sequence (μ(n),Λ(n))n∈ℕ⊆gr⁡(𝔘)(\mu^{(n)},\Lambda^{(n)})\_{n\in\mathbb{N}}\subseteq\operatorname{gr}(\mathfrak{U}) such that (μ(n),Λ(n))⇀(μ⋆,Λ⋆)(\mu^{(n)},\Lambda^{(n)})\rightharpoonup(\mu^{\star},\Lambda^{\star}) as n→∞n\to\infty, with some (μ⋆,Λ⋆)∈gr⁡(𝔘)(\mu^{\star},\Lambda^{\star})\in\operatorname{gr}(\mathfrak{U}). By the triangle inequality, it holds that for every n∈ℕn\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |H​(μ(n),Λ(n))−H​(μ⋆,Λ⋆)|\displaystyle|H(\mu^{(n)},\Lambda^{(n)})-H(\mu^{\star},\Lambda^{\star})| | ≤|r¯​(μ(n),Λ(n))−r¯​(μ⋆,Λ⋆)|+β⋅|J¯​(Λ(n))−J¯​(Λ⋆)|\displaystyle\leq|\overline{r}(\mu^{(n)},\Lambda^{(n)})-\overline{r}(\mu^{\star},\Lambda^{\star})|+\beta\cdot|\overline{J}(\Lambda^{(n)})-\overline{J}(\Lambda^{\star})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:III(n)+β⋅|IV(n)|.\displaystyle=:\operatorname{III}^{(n)}+\beta\cdot|\operatorname{IV}^{(n)}|. |  |

The limit of III(n)\operatorname{III}^{(n)} is straightforward. Indeed, by Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (iii) and the limit Λ(n)⇀Λ⋆\Lambda^{(n)}\rightharpoonup\Lambda^{\star},

|  |  |  |
| --- | --- | --- |
|  | limn→∞III(n)≤2​C¯r​limn→∞WP​(S×A)​(Λ(n),Λ⋆)=0.\displaystyle\lim\_{n\to\infty}\operatorname{III}^{(n)}\leq 2\overline{C}\_{r}\lim\_{n\to\infty}{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda^{(n)},\Lambda^{\star})=0. |  |

It remains to show the limit of |IV(n)||\operatorname{IV}^{(n)}|. Recalling the measuarable selector p¯∗\overline{p}^{\*} defined as in the part (i), denote by p⋆:=p¯∗​(Λ⋆)∈𝔓0p^{\star}:=\overline{p}^{\*}(\Lambda^{\star})\in\mathfrak{P}^{0}. Then it holds that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.15) |  | J¯​(Λ⋆)=∫P​(S)V¯​(μ′)​p¯​(d​μ′|pjS⁡(Λ⋆),Λ⋆,p⋆)=∫E0V¯​(F¯​(μ⋆,Λ⋆,e0))​p⋆​(d​e0),\displaystyle\overline{J}(\Lambda^{\star})=\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\operatorname{pj}\_{S}(\Lambda^{\star}),\Lambda^{\star},p^{\star})=\int\_{E^{0}}\overline{V}(\overline{\operatorname{F}}(\mu^{\star},\Lambda^{\star},e^{0}))p^{\star}(de^{0}), |  |

noting that pjS⁡(Λ⋆)=μ⋆\operatorname{pj}\_{S}(\Lambda^{\star})=\mu^{\star} as (μ⋆,Λ⋆)∈gr⁡(𝔘)(\mu^{\star},\Lambda^{\star})\in\operatorname{gr}(\mathfrak{U}).

On the other hand, as p⋆∈𝔓0p^{\star}\in\mathfrak{P}^{0} does not necessarily optimize J¯​(Λ(n))\overline{J}(\Lambda^{(n)}), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.16) |  | J¯​(Λ(n))≤∫P​(S)V¯​(μ′)​p¯​(d​μ′|pjS⁡(Λ(n)),Λ(n),p⋆)=∫E0V¯​(F¯​(μ(n),Λ(n),e0))​p⋆​(d​e0),\displaystyle\overline{J}(\Lambda^{(n)})\leq\int\_{{\mathcal{}P}(S)}\overline{V}(\mu^{\prime})\overline{p}(d\mu^{\prime}|\operatorname{pj}\_{S}(\Lambda^{(n)}),\Lambda^{(n)},p^{\star})=\int\_{E^{0}}\overline{V}(\overline{\operatorname{F}}(\mu^{(n)},\Lambda^{(n)},e^{0}))p^{\star}(de^{0}), |  |

with pjS⁡(Λ(n))=μ(n)\operatorname{pj}\_{S}(\Lambda^{(n)})=\mu^{(n)}.

By ([5.15](https://arxiv.org/html/2511.04515v1#S5.E15 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) and ([5.16](https://arxiv.org/html/2511.04515v1#S5.E16 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), it holds that for every n∈ℕn\in\mathbb{N} and every Γ∈CplE0×E0⁡(p⋆,p⋆)\Gamma\in\operatorname{Cpl}\_{E^{0}\times E^{0}}(p^{\star},p^{\star}),

|  |  |  |  |
| --- | --- | --- | --- |
| (5.17) |  | IV(n)≤∫E0V¯​(F¯​(μ(n),Λ(n),e0))​p⋆​(d​e0)−∫E0V¯​(F¯​(μ⋆,Λ⋆,e0))​p⋆​(d​e0)=∫E0×E0(V¯​(F¯​(μ(n),Λ(n),e0))−V¯​(F¯​(μ⋆,Λ⋆,e~0)))​Γ​(d​e0,d​e~0)≤2​L​C¯F⋅(WP​(S×A)​(Λ(n),Λ⋆)+∫E0×E0dE0​(e0,e~0)​Γ​(d​e0,d​e~0)),\displaystyle\begin{aligned} \operatorname{IV}^{(n)}&\leq\int\_{E^{0}}\overline{V}(\overline{\operatorname{F}}(\mu^{(n)},\Lambda^{(n)},e^{0}))p^{\star}(de^{0})-\int\_{E^{0}}\overline{V}(\overline{\operatorname{F}}(\mu^{\star},\Lambda^{\star},e^{0}))p^{\star}(de^{0})\\ &=\int\_{E^{0}\times E^{0}}\Big(\overline{V}(\overline{\operatorname{F}}(\mu^{(n)},\Lambda^{(n)},e^{0}))-\overline{V}(\overline{\operatorname{F}}(\mu^{\star},\Lambda^{\star},\tilde{e}^{0}))\Big)\Gamma(de^{0},d\tilde{e}^{0})\\ &\leq 2L\overline{C}\_{{\operatorname{F}}}\cdot\bigg({\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda^{(n)},\Lambda^{\star})+\int\_{E^{0}\times E^{0}}d\_{E^{0}}(e^{0},\tilde{e}^{0})\Gamma(de^{0},d\tilde{e}^{0})\bigg),\end{aligned} |  |

where the last inequality follows from the LL-Lipschitz continuity of V¯\overline{V} and the estimate of F¯\overline{\operatorname{F}} given in Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (ii).

By taking infimum over Γ∈CplE0×E0⁡(p⋆,p⋆)\Gamma\in\operatorname{Cpl}\_{E^{0}\times E^{0}}(p^{\star},p^{\star}) in the last equation of ([5.17](https://arxiv.org/html/2511.04515v1#S5.E17 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (5.18) |  | IV(n)≤2​L​C¯F​WP​(S×A)​(Λ(n),Λ⋆).\displaystyle\operatorname{IV}^{(n)}\leq 2L\overline{C}\_{{\operatorname{F}}}{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda^{(n)},\Lambda^{\star}). |  |

Using the same arguments as presented for ([5.18](https://arxiv.org/html/2511.04515v1#S5.E18 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), one can have the lower bound with the same constant, i.e., IV(n)≥−2​L​C¯F​WP​(S×A)​(Λ(n),Λ⋆).\operatorname{IV}^{(n)}\geq-2L\overline{C}\_{{\operatorname{F}}}{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\Lambda^{(n)},\Lambda^{\star}).

Combined with the limit Λ(n)⇀Λ⋆\Lambda^{(n)}\rightharpoonup\Lambda^{\star}, this ensures that |IV(n)||\operatorname{IV}^{(n)}| vanishes as n→∞n\to\infty. Therefore HH given in ([5.14](https://arxiv.org/html/2511.04515v1#S5.E14 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) is continuous as claimed.

Since 𝔘\mathfrak{U} is is non-empty, compact-valued, and continuous (see Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (ii)) and HH is continuous, an application of Berge’s maximum theorem ensures the continuity of T​V¯{\mathcal{}T}\overline{V} (see ([2.22](https://arxiv.org/html/2511.04515v1#S2.E22 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))) and the existence of the measurable selector π¯∗:P​(S)∋μ↦π¯∗​(μ)∈𝔘​(μ)\overline{\pi}^{\*}:{\mathcal{}P}(S)\ni\mu\mapsto\overline{\pi}^{\*}(\mu)\in\mathfrak{U}(\mu) satisfying ([2.24](https://arxiv.org/html/2511.04515v1#S2.E24 "In item (ii) ‣ Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). This completes the proof.
∎

### 5.3. Proof of Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

Let V¯∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}). We claim that T​V¯∈Lipb,L¯⁡(P​(S);ℝ){\mathcal{}T}\overline{V}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}).
From Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (iii) and the fact that V¯∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}), the boundedness of T​V¯{\mathcal{}T}\overline{V} is straightforward. To verify the L¯\overline{L}-Lipschitz continuity of T​V¯{\mathcal{}T}\overline{V}, let μ,μ~∈P​(S)\mu,\tilde{\mu}\in{\mathcal{}P}(S) and denote by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.19) |  | D⁡(μ,μ~):=T​V¯​(μ)−T​V¯​(μ~).\displaystyle\operatorname{D}(\mu,\tilde{\mu}):={\mathcal{}T}\overline{V}(\mu)-{\mathcal{}T}\overline{V}(\tilde{\mu}). |  |

Then let π¯∗​(μ)∈𝔘​(μ)\overline{\pi}^{\*}(\mu)\in\mathfrak{U}(\mu) be the local maximizer of T​V¯​(μ){\mathcal{}T}\overline{V}(\mu) (see Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)). Then, denote by ζ⋄:=pjA⁡(π¯∗​(μ))∈P​(A)\zeta^{\diamond}:=\operatorname{pj}\_{A}(\overline{\pi}^{\*}(\mu))\in{\mathcal{}P}(A) the marginal of π¯∗​(μ)∈𝔘​(μ)⊂P​(S×A)\overline{\pi}^{\*}(\mu)\in\mathfrak{U}(\mu)\subset{\mathcal{}P}(S\times A) on AA. Since π¯∗​(μ)∈CplS×A⁡(μ,ζ⋄)\overline{\pi}^{\*}(\mu)\in\operatorname{Cpl}\_{S\times A}(\mu,\zeta^{\diamond}), by Lemma [5.1](https://arxiv.org/html/2511.04515v1#S5.Thmthm1 "Lemma 5.1. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (i) there exists a coupling Λ~⋄∈CplS×A⁡(μ~,ζ⋄)\tilde{\Lambda}^{\diamond}\in\operatorname{Cpl}\_{S\times A}(\tilde{\mu},\zeta^{\diamond}) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.20) |  | WP​(S×A)​(π¯∗​(μ),Λ~⋄)≤WP​(S)​(μ,μ~).\displaystyle{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\overline{\pi}^{\*}(\mu),\tilde{\Lambda}^{\diamond})\leq{\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu,\tilde{\mu}). |  |

Then since Λ~⋄∈𝔘​(μ~)\tilde{\Lambda}^{\diamond}\in\mathfrak{U}(\tilde{\mu}) (which does not necessarily maximize T​V¯​(μ~){\mathcal{}T}\overline{V}(\tilde{\mu})), it holds that

|  |  |  |
| --- | --- | --- |
|  | D(μ,μ~)≤r¯(μ,π¯∗(μ))−r¯(μ~,Λ~⋄)+β⋅J¯(π¯∗(μ))−β⋅J¯(Λ~⋄)=:D1(μ,μ~),\displaystyle\operatorname{D}(\mu,\tilde{\mu})\leq\overline{r}(\mu,\overline{\pi}^{\*}(\mu))-\overline{r}(\tilde{\mu},\tilde{\Lambda}^{\diamond})+\beta\cdot\overline{J}(\overline{\pi}^{\*}(\mu))-\beta\cdot\overline{J}(\tilde{\Lambda}^{\diamond})=:\operatorname{D}^{1}(\mu,\tilde{\mu}), |  |

recalling J¯:P​(S×A)→ℝ\overline{J}:{\mathcal{}P}(S\times A)\to\mathbb{R} defined in ([5.13](https://arxiv.org/html/2511.04515v1#S5.E13 "In 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) (with noting that pjS⁡(π¯∗​(μ))=μ\operatorname{pj}\_{S}(\overline{\pi}^{\*}(\mu))=\mu and pjS⁡(Λ~⋄)=μ~\operatorname{pj}\_{S}(\tilde{\Lambda}^{\diamond})=\tilde{\mu}).

Let p¯∗​(Λ~⋄)∈𝔓0\overline{p}^{\*}(\tilde{\Lambda}^{\diamond})\in\mathfrak{P}^{0} be the local minimizers of J¯​(Λ~⋄)\overline{J}(\tilde{\Lambda}^{\diamond}) (see Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)). Since they do not necessarily minimize J¯​(π¯∗​(μ))\overline{J}(\overline{\pi}^{\*}(\mu)), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.21) |  | D1⁡(μ,μ~)≤r¯​(μ,π¯∗​(μ))−r¯​(μ~,Λ~⋄)+β​∫E0V¯​(F¯​(μ,π¯∗​(μ),e0))​p¯∗​(Λ~⋄)​(d​e0)−β∫P​(S)V¯(F¯(μ~,Λ~⋄,e~0))p¯∗(Λ~⋄)(de~0)=:D2(μ,μ~),\displaystyle\begin{aligned} \operatorname{D}^{1}(\mu,\tilde{\mu})&\leq\overline{r}(\mu,\overline{\pi}^{\*}(\mu))-\overline{r}(\tilde{\mu},\tilde{\Lambda}^{\diamond})+\beta\int\_{E^{0}}\overline{V}(\overline{\operatorname{F}}(\mu,\overline{\pi}^{\*}(\mu),e^{0}))\overline{p}^{\*}(\tilde{\Lambda}^{\diamond})(de^{0})\\ &\quad-\beta\int\_{{\mathcal{}P}(S)}\overline{V}(\overline{\operatorname{F}}(\tilde{\mu},\tilde{\Lambda}^{\diamond},\tilde{e}^{0}))\overline{p}^{\*}(\tilde{\Lambda}^{\diamond})(d\tilde{e}^{0})=:\operatorname{D}^{2}(\mu,\tilde{\mu}),\end{aligned} |  |

recalling the definition of p¯\overline{p} given in Definition [2.11](https://arxiv.org/html/2511.04515v1#S2.Thmthm11 "Definition 2.11. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii).

Let Γ∈CplE0×E0⁡(p¯∗​(Λ~⋄),p¯∗​(Λ~⋄))\Gamma\in\operatorname{Cpl}\_{E^{0}\times E^{0}}(\overline{p}^{\*}(\tilde{\Lambda}^{\diamond}),\overline{p}^{\*}(\tilde{\Lambda}^{\diamond})) be some arbitrary. Then, by the estimates for r¯\overline{r} and F¯\overline{\operatorname{F}} (given in Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (ii), (iii)) and V¯∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | D2⁡(μ,μ~)\displaystyle\operatorname{D}^{2}(\mu,\tilde{\mu}) | ≤|r¯​(μ,π¯∗​(μ))−r¯​(μ~,Λ~⋄)|+β​∫E0×E0|V¯​(F¯​(μ,π¯∗​(μ),e0))−V¯​(F¯​(μ~,Λ~⋄,e~0))|​Γ​(d​e0,d​e~0)\displaystyle\leq\big|\overline{r}(\mu,\overline{\pi}^{\*}(\mu))-\overline{r}(\tilde{\mu},\tilde{\Lambda}^{\diamond})\big|+\beta\int\_{E^{0}\times E^{0}}\big|\overline{V}(\overline{\operatorname{F}}(\mu,\overline{\pi}^{\*}(\mu),e^{0}))-\overline{V}(\overline{\operatorname{F}}(\tilde{\mu},\tilde{\Lambda}^{\diamond},\tilde{e}^{0}))\big|\Gamma(de^{0},d\tilde{e}^{0}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.22) |  |  | ≤2​C¯r​WP​(S×A)​(π¯∗​(μ),Λ~⋄)\displaystyle\leq 2\overline{C}\_{r}{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\overline{\pi}^{\*}(\mu),\tilde{\Lambda}^{\diamond}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C¯F​L¯​β​(2​WP​(S×A)​(π¯∗​(μ),Λ~⋄)+∫E0×E0dE0​(e0,e~0)​Γ​(d​e0,d​e~0)).\displaystyle\quad+\overline{C}\_{{\operatorname{F}}}\overline{L}\beta\bigg(2{\mathcal{}W}\_{{\mathcal{}P}(S\times A)}(\overline{\pi}^{\*}(\mu),\tilde{\Lambda}^{\diamond})+\int\_{E^{0}\times E^{0}}d\_{E^{0}}(e^{0},\tilde{e}^{0})\Gamma(de^{0},d\tilde{e}^{0})\bigg). |  |

For the last line of ([5.22](https://arxiv.org/html/2511.04515v1#S5.E22 "In 5.3. Proof of Proposition 2.16 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), we take infimum over all Γ∈CplE0×E0⁡(p¯∗​(Λ~⋄),p¯∗​(Λ~⋄))\Gamma\in\operatorname{Cpl}\_{E^{0}\times E^{0}}(\overline{p}^{\*}(\tilde{\Lambda}^{\diamond}),\overline{p}^{\*}(\tilde{\Lambda}^{\diamond})) and then use the estimate given in ([5.20](https://arxiv.org/html/2511.04515v1#S5.E20 "In 5.3. Proof of Proposition 2.16 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) to obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (5.23) |  | D2⁡(μ,μ~)≤(2​C¯r+2​C¯F​L¯​β)​WP​(S)​(μ,μ~)≤L¯​WP​(S)​(μ,μ~),\displaystyle\operatorname{D}^{2}(\mu,\tilde{\mu})\leq\big(2\overline{C}\_{r}+2\overline{C}\_{{\operatorname{F}}}\overline{L}\beta\big){\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu,\tilde{\mu})\leq\overline{L}{\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu,\tilde{\mu}), |  |

where the last inequality holds by the inequality L¯≥2​C¯r/(1−2​C¯F​β)\overline{L}\geq 2\overline{C}\_{r}/(1-2\overline{C}\_{{\operatorname{F}}}\beta) with 2​C¯F​β<12\overline{C}\_{\operatorname{F}}\beta<1.

By ([5.19](https://arxiv.org/html/2511.04515v1#S5.E19 "In 5.3. Proof of Proposition 2.16 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), ([5.21](https://arxiv.org/html/2511.04515v1#S5.E21 "In 5.3. Proof of Proposition 2.16 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) and ([5.23](https://arxiv.org/html/2511.04515v1#S5.E23 "In 5.3. Proof of Proposition 2.16 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")), we have that

|  |  |  |
| --- | --- | --- |
|  | T​V¯​(μ)−T​V¯​(μ~)=D⁡(μ,μ~)≤D1⁡(μ,μ~)≤D2⁡(μ,μ~)≤L¯​WP​(S)​(μ,μ~).{\mathcal{}T}\overline{V}(\mu)-{\mathcal{}T}\overline{V}(\tilde{\mu})=\operatorname{D}(\mu,\tilde{\mu})\leq\operatorname{D}^{1}(\mu,\tilde{\mu})\leq\operatorname{D}^{2}(\mu,\tilde{\mu})\leq\overline{L}{\mathcal{}W}\_{{\mathcal{}P}(S)}(\mu,\tilde{\mu}). |  |

Since μ,μ~∈P​(S)\mu,\tilde{\mu}\in{\mathcal{}P}(S) are chosen arbitrary, one can have that T​V¯​(⋅){\mathcal{}T}\overline{V}(\cdot) is L¯\overline{L}-Lipschitz continuous. Hence, we conclude that T​V¯∈Lipb,L¯⁡(P​(S);ℝ){\mathcal{}T}\overline{V}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}).

To verify ([2.25](https://arxiv.org/html/2511.04515v1#S2.E25 "In Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), let V¯,W¯∈Lipb,L¯⁡(P​(S);ℝ)\overline{V},\overline{W}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}). By Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii), for every μ∈P​(S)\mu\in{\mathcal{}P}(S)

|  |  |  |
| --- | --- | --- |
|  | |T​V¯​(μ)−T​W¯​(μ)|≤β​supp∈𝔓0∫P​(S)|V¯​(μ′)−W¯​(μ′)|​p¯​(d​μ′|μ,π¯∗​(μ),p)≤β​‖V¯−W¯‖∞,\displaystyle|{\mathcal{}T}\overline{V}(\mu)-{\mathcal{}T}\overline{W}(\mu)|\leq\beta\sup\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}|\overline{V}(\mu^{\prime})-\overline{W}(\mu^{\prime})|\overline{p}(d\mu^{\prime}|\mu,\overline{\pi}^{\*}(\mu),p)\leq\beta\|\overline{V}-\overline{W}\|\_{\infty}, |  |

which ensures ([2.25](https://arxiv.org/html/2511.04515v1#S2.E25 "In Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) to hold.

Since β<1\beta<1 and T​(Lipb,L¯⁡(P​(S);ℝ))⊆Lipb,L¯⁡(P​(S);ℝ){\mathcal{}T}(\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}))\subseteq\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}), T{\mathcal{}T} is a contraction on Lipb,L¯⁡(P​(S);ℝ)\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}). Hence, an application of the Banach’s fixed point theorem ensures the existence and uniqueness of V¯∗∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}^{\*}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}) such that for every V¯∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R}), V¯∗=T​V¯∗=limn→∞Tn​V¯\overline{V}^{\*}={\mathcal{}T}\overline{V}^{\*}=\lim\_{n\to\infty}{\mathcal{}T}^{n}\overline{V}. This completes the proof. ∎

## 6. Proof of results in Section [2.4](https://arxiv.org/html/2511.04515v1#S2.SS4 "2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We begin by presenting an observation that plays a key role in the proof of Lemmas [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and [2.20](https://arxiv.org/html/2511.04515v1#S2.Thmthm20 "Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Recall the set Q{\mathcal{}Q} given in Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and the filtration 𝔾=(Gt)t≥0\mathbb{G}=({\mathcal{}G}\_{t})\_{t\geq 0} given in ([2.10](https://arxiv.org/html/2511.04515v1#S2.E10 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

###### Lemma 6.1.

Denote for every t≥0t\geq 0 by LGt0​(Z)L^{0}\_{{\mathcal{}G}\_{t}}(Z) the set of all Gt{\mathcal{}G}\_{t} measurable random variables ζt\zeta\_{t} with values in a compact Polish space ZZ. Then for every ζ0∈LG00​(Z)\zeta\_{0}\in L^{0}\_{{\mathcal{}G}\_{0}}(Z) and ℙ,ℙ~∈Q\mathbb{P},\widetilde{\mathbb{P}}\in{\mathcal{}Q}, it holds that ℒℙ​(ζ0)=ℒℙ~​(ζ0)\mathscr{L}\_{\mathbb{P}}(\zeta\_{0})=\mathscr{L}\_{\widetilde{\mathbb{P}}}(\zeta\_{0}). Furthermore, for every t≥1t\geq 1, ζt∈LGt0​(Z)\zeta\_{t}\in L^{0}\_{{\mathcal{}G}\_{t}}(Z), and ℙ,ℙ~∈Q\mathbb{P},\widetilde{\mathbb{P}}\in{\mathcal{}Q}, it holds that ℒℙ​(ζt|ε1:t0)=ℒℙ~​(ζt|ε1:t0)\mathscr{L}\_{\mathbb{P}}(\zeta\_{t}\,|\,\varepsilon^{0}\_{1:t})=\mathscr{L}\_{\widetilde{\mathbb{P}}}(\zeta\_{t}\,|\,\varepsilon^{0}\_{1:t}), ℙ\mathbb{P}-a.s..

###### Proof.

Without loss of generality, we consider the case t≥1t\geq 1, as the case t=0t=0 can be subsumed into it. Then, let ζt∈LGt0​(Z)\zeta\_{t}\in L^{0}\_{{\mathcal{}G}\_{t}}(Z) and ℙ,ℙ~∈Q\mathbb{P},\widetilde{\mathbb{P}}\in{\mathcal{}Q} be given.

By the same arguments presented for the proof of Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty") (ii), ℒℙ​(ζt|ε1:t0)\mathscr{L}\_{\mathbb{P}}(\zeta\_{t}\,|\,\varepsilon^{0}\_{1:t}) and ℒℙ~​(ζt|ε1:t0)\mathscr{L}\_{\widetilde{\mathbb{P}}}(\zeta\_{t}\,|\,\varepsilon^{0}\_{1:t}) are Ft0{\mathcal{}F}\_{t}^{0} measurable. Hence it suffices to show that for any bounded Borel measurable functions g^t:(E0)t→ℝ\hat{g}\_{t}:(E^{0})^{t}\to\mathbb{R} and f^:Z→ℝ\hat{f}:Z\to\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ​[g^t​(ε1:t0)​f^​(ζt)]=𝔼ℙ​[g^t​(ε1:t0)​∫Zf^​(z~)​ℒℙ~​(ζt|ε1:t0)​(d​z~)].\displaystyle\mathbb{E}^{\mathbb{P}}[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\hat{f}(\zeta\_{t})]=\mathbb{E}^{\mathbb{P}}\bigg[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\int\_{Z}\hat{f}(\tilde{z})\mathscr{L}\_{\widetilde{\mathbb{P}}}(\zeta\_{t}\,|\,\varepsilon^{0}\_{1:t})(d\tilde{z})\bigg]. |  |

Note that since ζt\zeta\_{t} is Gt{\mathcal{}G}\_{t} measurable, there exists a Borel measurable function l^:G×Θt+1×Et×(E0)t→Z\hat{l}:G\times\Theta^{t+1}\times E^{t}\times(E^{0})^{t}\to Z such that ζ=l^​(γ,ϑ0:t,ε1:t,ε1:t0).\zeta=\hat{l}(\gamma,\vartheta\_{0:t},\varepsilon\_{1:t},\varepsilon\_{1:t}^{0}).

Moreover, since ε1:t0\varepsilon\_{1:t}^{0} is independent of γ,ϑ0:t,ε1:t\gamma,\vartheta\_{0:t},\varepsilon\_{1:t} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[g^t​(ε1:t0)​f^​(ζt)]\displaystyle\mathbb{E}^{\mathbb{P}}[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\hat{f}(\zeta\_{t})] | =𝔼ℙ​[g^t​(ε1:t0)​f^​(l^​(γ,ϑ0:t,ε1:t,ε1:t0))]\displaystyle=\mathbb{E}^{\mathbb{P}}\big[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\hat{f}\big(\hat{l}(\gamma,\vartheta\_{0:t},\varepsilon\_{1:t},\varepsilon\_{1:t}^{0})\big)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(E0)tg^t​(e1:t0)​𝔼ℙ​[f^​(l^​(γ,ϑ0:t,ε1:t,e1:t0))]​ℒℙ​(ε1:t0)​(d​e1:t0)\displaystyle=\int\_{(E^{0})^{t}}\hat{g}\_{t}(e^{0}\_{1:t})\mathbb{E}^{\mathbb{P}}\big[\hat{f}\big(\hat{l}(\gamma,\vartheta\_{0:t},\varepsilon\_{1:t},e^{0}\_{1:t})\big)\big]\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{1:t}^{0})(de^{0}\_{1:t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(E0)tg^t(e1:t0)𝔼ℙ~[f^(l^(γ,ϑ0:t,ε1:t,e1:t0))]ℒℙ(ε1:t0)(de1:t0)=:It,\displaystyle=\int\_{(E^{0})^{t}}\hat{g}\_{t}(e^{0}\_{1:t})\mathbb{E}^{\widetilde{\mathbb{P}}}\big[\hat{f}\big(\hat{l}(\gamma,\vartheta\_{0:t},\varepsilon\_{1:t},e^{0}\_{1:t})\big)\big]\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{1:t}^{0})(de^{0}\_{1:t})=:\operatorname{I}\_{t}, |  |

where the second equality holds by Fubini’s theorem and the last equality follows from the fact that ℒℙ​(γ,ϑ0:t,ε1:t)=ℒℙ~​(γ,ϑ0:t,ε1:t)\mathscr{L}\_{\mathbb{P}}(\gamma,\vartheta\_{0:t},\varepsilon\_{1:t})=\mathscr{L}\_{\widetilde{\mathbb{P}}}(\gamma,\vartheta\_{0:t},\varepsilon\_{1:t}) (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)).

Therefore, by definition of ℒℙ~​(ζt|ε1:t0)\mathscr{L}\_{\widetilde{\mathbb{P}}}(\zeta\_{t}\,|\,\varepsilon^{0}\_{1:t}) and ℒℙ​(ε1:t0)\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{1:t}^{0}),

|  |  |  |
| --- | --- | --- |
|  | It=∫(E0)tg^t​(e1:t0)​𝔼ℙ~​[𝔼ℙ~​[f^​(ζ)|ε1:t0=e1:t0]]​ℒℙ​(ε1:t0)​(d​e1:t0)=∫(E0)tg^t​(e1:t0)​(∫Zf^​(z)​ℒℙ~​(ζ|ε1:t0=e1:t)​(d​z))​ℒℙ​(ε1:t0)​(d​e1:t0)=𝔼ℙ​[g^t​(ε1:t0)​∫Zf^​(z~)​ℒℙ~​(ζt|ε1:t0)​(d​z~)],\displaystyle\begin{aligned} \operatorname{I}\_{t}&=\int\_{(E^{0})^{t}}\hat{g}\_{t}(e^{0}\_{1:t})\mathbb{E}^{\widetilde{\mathbb{P}}}\big[\mathbb{E}^{\widetilde{\mathbb{P}}}[\hat{f}(\zeta)|\varepsilon\_{1:t}^{0}=e^{0}\_{1:t}]\big]\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{1:t}^{0})(de^{0}\_{1:t})\\ &=\int\_{(E^{0})^{t}}\hat{g}\_{t}(e^{0}\_{1:t})\bigg(\int\_{Z}\hat{f}(z)\mathscr{L}\_{\widetilde{\mathbb{P}}}(\zeta|\varepsilon\_{1:t}^{0}=e\_{1:t})(dz)\bigg)\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{1:t}^{0})(de^{0}\_{1:t})\\ &=\mathbb{E}^{\mathbb{P}}\bigg[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\int\_{Z}\hat{f}(\tilde{z})\mathscr{L}\_{\widetilde{\mathbb{P}}}(\zeta\_{t}\,|\,\varepsilon^{0}\_{1:t})(d\tilde{z})\bigg],\end{aligned} |  |

as claimed.
∎

### 6.1. Proof of Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We first prove ([2.26](https://arxiv.org/html/2511.04515v1#S2.E26 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Let a∈Aa\in{\mathcal{}A} be given.
We will construct p¯1ξ,a∈𝔓0\underline{p}\_{1}^{\xi,a}\in\mathfrak{P}^{0} and the sequence of kernels p¯tξ,a:(E0)t−1∋e1:t−10↦p¯tξ,a​(et0|e1:t−10)∈𝔓0\underline{p}\_{t}^{\xi,a}:(E^{0})^{t-1}\ni e\_{1:t-1}^{0}\mapsto\underline{p}\_{t}^{\xi,a}(e\_{t}^{0}|e\_{1:t-1}^{0})\in\mathfrak{P}^{0} for t≥2t\geq 2 to define ℙ¯ξ,a∈Q\underline{\mathbb{P}}^{\xi,a}\in{\mathcal{}Q} induced by (p¯tξ,a)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,a})\_{t\geq 1}\in\mathcal{K}^{0}.

Step 1: Let ℙ~∈Q\widetilde{\mathbb{P}}\in{\mathcal{}Q} be some arbitrary. Then set

|  |  |  |  |
| --- | --- | --- | --- |
| (6.1) |  | s~0:=ξ,Λ~0:=ℒℙ~​((s~0,a0)),\displaystyle\begin{aligned} \tilde{s}\_{0}:=\xi,\quad\tilde{\Lambda}\_{0}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}((\tilde{s}\_{0},a\_{0})),\end{aligned} |  |

and define by

|  |  |  |  |
| --- | --- | --- | --- |
| (6.2) |  | p¯1ξ,a:=p¯∗​(Λ~0)∈𝔓0,\displaystyle\underline{p}\_{1}^{\xi,a}:=\overline{p}^{\*}(\tilde{\Lambda}\_{0})\in\mathfrak{P}^{0}, |  |

where p¯∗\overline{p}^{\*} is given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i).

Next set

|  |  |  |  |
| --- | --- | --- | --- |
| (6.3) |  | s~1:=F⁡(s~0,a0,Λ~0,ε1,ε10),Λ~1:=ℒℙ~​((s~1,a1)|ε10),\displaystyle\tilde{s}\_{1}:=\operatorname{F}\big(\tilde{s}\_{0},a\_{0},\tilde{\Lambda}\_{0},\varepsilon\_{1},\varepsilon\_{1}^{0}\big),\quad\tilde{\Lambda}\_{1}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}((\tilde{s}\_{1},a\_{1})\,|\,\varepsilon\_{1}^{0}), |  |

where (s~0,Λ~0)(\tilde{s}\_{0},\tilde{\Lambda}\_{0}) are given in ([6.1](https://arxiv.org/html/2511.04515v1#S6.E1 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")). We see that (s~1,a1)(\tilde{s}\_{1},a\_{1}) are G1{\mathcal{}G}\_{1} measurable (because s~0∈LF00​(S)\tilde{s}\_{0}\in L\_{{\mathcal{}F}\_{0}}^{0}(S), a0=π0​(γ,ϑ0)a\_{0}=\pi\_{0}(\gamma,\vartheta\_{0}), a1=π1​(γ,ϑ0:1,ε1,ε10)a\_{1}=\pi\_{1}(\gamma,\vartheta\_{0:1},\varepsilon\_{1},\varepsilon\_{1}^{0})) and ε10\varepsilon\_{1}^{0} is independent of (γ,ϑ0:1,ε1)(\gamma,\vartheta\_{0:1},\varepsilon\_{1}) (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)).

Moreover, an application of Lemma [A.1](https://arxiv.org/html/2511.04515v1#A1.Thmthm1 "Lemma A.1. ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty") (ii) implies that Λ~1\tilde{\Lambda}\_{1} is F10{\mathcal{}F}\_{1}^{0} measurable, which ensures the existence of a Borel measurable function l1:E0→P​(S×A)l\_{1}:E^{0}\to{\mathcal{}P}(S\times A) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.4) |  | l1​(ε10)=Λ~1.\displaystyle l\_{1}(\varepsilon\_{1}^{0})=\tilde{\Lambda}\_{1}. |  |

From this, define p¯2ξ,a:E0∋e10↦p¯2ξ,a(⋅|e10)∈P(E0)\underline{p}\_{2}^{\xi,a}:E^{0}\ni e\_{1}^{0}\mapsto\underline{p}\_{2}^{\xi,a}(\cdot\,|\,e\_{1}^{0})\in{\mathcal{}P}(E^{0}) by

|  |  |  |  |
| --- | --- | --- | --- |
| (6.5) |  | p¯2ξ,a(⋅|e10):=p¯∗(l1(e10))∈𝔓0.\displaystyle\underline{p}\_{2}^{\xi,a}(\,\cdot\,|\,e\_{1}^{0}):=\overline{p}^{\*}\big(l\_{1}(e\_{1}^{0})\big)\in\mathfrak{P}^{0}. |  |

Using the same arguments presented for ([6.3](https://arxiv.org/html/2511.04515v1#S6.E3 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty"))–([6.5](https://arxiv.org/html/2511.04515v1#S6.E5 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), for every t≥1t\geq 1 we inductively set

|  |  |  |  |
| --- | --- | --- | --- |
| (6.6) |  | s~t:=F⁡(s~t−1,at−1,Λ~t−1,εt,εt0),Λ~t:=ℒℙ~​((s~t,at)|ε1:t0),\displaystyle\tilde{s}\_{t}:=\operatorname{F}(\tilde{s}\_{t-1},a\_{t-1},\tilde{\Lambda}\_{t-1},\varepsilon\_{t},\varepsilon\_{t}^{0}),\quad\tilde{\Lambda}\_{t}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}((\tilde{s}\_{t},a\_{t})\,|\,\varepsilon\_{1:t}^{0}), |  |

where (s~t,at)(\tilde{s}\_{t},a\_{t}) are Gt{\mathcal{}G}\_{t} measurable, and Λ~t\tilde{\Lambda}\_{t} is Ft0{\mathcal{}F}\_{t}^{0} measurable.

Hence, there exists a Borel measurable function lt:(E0)t→P​(S×A)l\_{t}:(E^{0})^{t}\to{\mathcal{}P}(S\times A) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.7) |  | lt​(ε1:t0)=Λ~t.\displaystyle l\_{t}(\varepsilon\_{1:t}^{0})=\tilde{\Lambda}\_{t}. |  |

From this, define p¯t+1ξ,a:(E0)t∋e1:t0↦p¯t+1ξ,a(⋅|e1:t0)∈P(E0)\underline{p}\_{t+1}^{\xi,a}:(E^{0})^{t}\ni e\_{1:t}^{0}\mapsto\underline{p}\_{t+1}^{\xi,a}(\cdot\,|\,e\_{1:t}^{0})\in{\mathcal{}P}(E^{0}) by

|  |  |  |  |
| --- | --- | --- | --- |
| (6.8) |  | p¯t+1ξ,a(⋅|e1:t0):=p¯∗(lt(e1:t0))∈𝔓0.\displaystyle\underline{p}\_{t+1}^{\xi,a}(\,\cdot\,|\,e\_{1:t}^{0}):=\overline{p}^{\*}\big(l\_{t}(e\_{1:t}^{0})\big)\in\mathfrak{P}^{0}. |  |

Using (p¯tξ,a)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,a})\_{t\geq 1}\in\mathcal{K}^{0}, constructed via ([6.2](https://arxiv.org/html/2511.04515v1#S6.E2 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), ([6.5](https://arxiv.org/html/2511.04515v1#S6.E5 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), and ([6.8](https://arxiv.org/html/2511.04515v1#S6.E8 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), we define the measure ℙ¯ξ,a∈Q\underline{\mathbb{P}}^{\xi,a}\in{\mathcal{}Q} induced by this sequence. We underline that the existence of such a measure is ensured by Ionescu–Tulcea’s theorem (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), and that the above inductive construction is invariant and can be carried out under any ℙ~∈Q\widetilde{\mathbb{P}}\in{\mathcal{}Q}.

Step 2: Recall for every t≥0t\geq 0, Λ~t\tilde{\Lambda}\_{t} is the conditional joint law of (s~t,at)(\tilde{s}\_{t},a\_{t}) given ε1:t0\varepsilon\_{1:t}^{0} under ℙ~\widetilde{\mathbb{P}}, as given in ([6.1](https://arxiv.org/html/2511.04515v1#S6.E1 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), ([6.3](https://arxiv.org/html/2511.04515v1#S6.E3 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), and ([6.6](https://arxiv.org/html/2511.04515v1#S6.E6 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")). We claim that for every t≥0t\geq 0, ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (6.9) |  | stξ,a,ℙ¯ξ,a=s~t,Λ¯tξ,a=Λ~t,\displaystyle s\_{t}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}}=\tilde{s}\_{t},\qquad\underline{\Lambda}\_{t}^{\xi,a}=\tilde{\Lambda}\_{t}, |  |

where Λ¯tξ,a\underline{\Lambda}\_{t}^{\xi,a} is the conditional joint law of (stξ,a,ℙ¯ξ,a,at)(s\_{t}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}},a\_{t}) given ε1:t0\varepsilon^{0}\_{1:t} under ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}.

The proof uses an induction over t≥0t\geq 0: For t=0t=0, clearly s0ξ,a,ℙ¯ξ,a=s~0=ξ∈LF00​(S)s\_{0}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}}=\tilde{s}\_{0}=\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S). Moreover, since a0a\_{0} is G0{\mathcal{}G}\_{0} measurable (noting that G0=σ​(γ,ϑ0){\mathcal{}G}\_{0}=\sigma(\gamma,\vartheta\_{0})) and ℒℙ¯ξ,a​(γ,ϑ0)=ℒℙ~​(γ,ϑ0)\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\gamma,\vartheta\_{0})=\mathscr{L}\_{\tilde{\mathbb{P}}}(\gamma,\vartheta\_{0}) (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)), it holds that Λ¯0ξ,a=Λ~0\underline{\Lambda}\_{0}^{\xi,a}=\tilde{\Lambda}\_{0}.

Assume that the induction claim holds true for some t≥0t\geq 0. For the case t+1t+1, by the conditional McKean-Vlasov dynamics given in ([2.12](https://arxiv.org/html/2511.04515v1#S2.E12 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and the induction hypothesis for tt, it holds that ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.,

|  |  |  |  |
| --- | --- | --- | --- |
| (6.10) |  | st+1ξ,a,ℙ¯ξ,a=F⁡(stξ,a,ℙ¯ξ,a,at,Λ¯tξ,a,εt+1,εt+10)=F⁡(s~t,at,Λ~t,εt+1,εt+10)=s~t+1,\displaystyle\begin{aligned} s\_{t+1}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}}&=\operatorname{F}(s\_{t}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}},a\_{t},\underline{\Lambda}\_{t}^{\xi,a},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0})\\ &=\operatorname{F}(\tilde{s}\_{t},a\_{t},\tilde{\Lambda}\_{t},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0})=\tilde{s}\_{t+1},\end{aligned} |  |

where the second equality holds by the Borel measurability of F\operatorname{F} (see Definition [2.4](https://arxiv.org/html/2511.04515v1#S2.Thmthm4 "Definition 2.4. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)), and the last equality holds by definition ([6.6](https://arxiv.org/html/2511.04515v1#S6.E6 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), as claimed.

We now show that Λ¯t+1ξ,a=Λ~t+1\underline{\Lambda}\_{t+1}^{\xi,a}=\tilde{\Lambda}\_{t+1}, ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.. By Ft+10{\mathcal{}F}\_{t+1}^{0}-measurability of (Λt+1ξ,a,Λ~t+1)(\Lambda\_{t+1}^{\xi,a},\tilde{\Lambda}\_{t+1}), it suffices to show that for any bounded Borel measurable functions g^t+1:(E0)t+1→ℝ\hat{g}\_{t+1}:(E^{0})^{t+1}\to\mathbb{R} and f^:S×A→ℝ\hat{f}:S\times A\to\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
| (6.11) |  | 𝔼ℙ¯ξ,a​[g^t+1​(ε1:t+10)​f^​(st+1ξ,a,ℙ¯ξ,a,at+1)]=𝔼ℙ¯ξ,a​[g^t+1​(ε1:t+10)​∫S×Af​(s~,a~)​Λ~t+1​(d​s~,d​a~)].\displaystyle\mathbb{E}^{\underline{\mathbb{P}}^{\xi,a}}[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}},a\_{t+1})]=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,a}}\bigg[\hat{g}\_{t+1}(\varepsilon^{0}\_{1:t+1})\int\_{S\times A}f(\tilde{s},\tilde{a})\tilde{\Lambda}\_{t+1}(d\tilde{s},d\tilde{a})\bigg]. |  |

Indeed, by ([6.10](https://arxiv.org/html/2511.04515v1#S6.E10 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")),

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ¯ξ,a[g^t+1(ε1:t+10)f^(st+1ξ,a,ℙ¯ξ,a,at+1)]=𝔼ℙ¯ξ,a[g^t+1(ε1:t+10)f^(s~t+1,at+1)]=:It+1.\displaystyle\mathbb{E}^{\underline{\mathbb{P}}^{\xi,a}}[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}},a\_{t+1})]=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,a}}[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(\tilde{s}\_{t+1},a\_{t+1})]=:\operatorname{I}^{t+1}. |  |

Moreove, since (s~t+1,at+1)(\tilde{s}\_{t+1},a\_{t+1}) are Gt+1{\mathcal{}G}\_{t+1} measurable (with Gt+1=σ​(γ,ϑ0:t+1,ε1:t+1,ε1:t+10){\mathcal{}G}\_{t+1}=\sigma(\gamma,\vartheta\_{0:t+1},\varepsilon\_{1:t+1},\varepsilon\_{1:t+1}^{0})), an application of Lemma [6.1](https://arxiv.org/html/2511.04515v1#S6.Thmthm1 "Lemma 6.1. ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty") ensures that
ℙ¯ξ,a\underline{\mathbb{P}}{}^{\xi,a}-a.s.,

|  |  |  |
| --- | --- | --- |
|  | ℒℙ¯ξ,a​((s~t+1,at+1)|ε1:t+10)=ℒℙ~​((s~t+1,at+1)|ε1:t+10)=Λ~t+1,\mathscr{L}\_{\underline{\mathbb{P}}{}^{\xi,a}}\big((\tilde{s}\_{t+1},a\_{t+1})\,|\,\varepsilon^{0}\_{1:t+1}\big)=\mathscr{L}\_{\widetilde{\mathbb{P}}}\big((\tilde{s}\_{t+1},a\_{t+1})\,|\,\varepsilon^{0}\_{1:t+1}\big)=\tilde{\Lambda}\_{t+1}, |  |

which implies that It+1\operatorname{I}^{t+1} equals the second term given in ([6.11](https://arxiv.org/html/2511.04515v1#S6.E11 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), as claimed.

By induction hypothesis, the claim ([6.9](https://arxiv.org/html/2511.04515v1#S6.E9 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) holds for all t≥0t\geq 0.

Step 3: Recall that ℙ¯ξ,a∈Q\underline{\mathbb{P}}^{\xi,a}\in{\mathcal{}Q} is the measure induced by (p¯tξ,a)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,a})\_{t\geq 1}\in\mathcal{K}^{0} given in ([6.2](https://arxiv.org/html/2511.04515v1#S6.E2 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), ([6.5](https://arxiv.org/html/2511.04515v1#S6.E5 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), and ([6.8](https://arxiv.org/html/2511.04515v1#S6.E8 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) (see Step 1). Then from Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii), it holds that ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (6.12) |  | ℒℙ¯ξ,a​(ε10)=p¯1ξ,a∈𝔓0,ℒℙ¯ξ,a(εt0|Ft−10)=p¯tξ,a(⋅|ε1:t−10)∈𝔓0for all t≥2.\displaystyle\begin{aligned} &\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\varepsilon\_{1}^{0})=\underline{p}\_{1}^{\xi,a}\in\mathfrak{P}^{0},\\ \;\;&\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\varepsilon\_{t}^{0}|{\mathcal{}F}\_{t-1}^{0})=\underline{p}\_{t}^{\xi,a}(\cdot|\varepsilon\_{1:t-1}^{0})\in\mathfrak{P}^{0}\;\;\mbox{for all $t\geq 2$}.\end{aligned} |  |

Moreover, since Λ¯tξ,a=Λ~t\underline{\Lambda}\_{t}^{\xi,a}=\tilde{\Lambda}\_{t} ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s. for all t≥0t\geq 0 (see ([6.9](https://arxiv.org/html/2511.04515v1#S6.E9 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) in Step 2), it holds that ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (6.13) |  | p¯1ξ,a=p¯∗(Λ¯0ξ,a),p¯tξ,a(⋅|ε1:t−10)=p¯∗(Λ¯t−1ξ,a)for all t≥2,\displaystyle\underline{p}\_{1}^{\xi,a}=\overline{p}^{\*}(\underline{\Lambda}\_{0}^{\xi,a}),\qquad\underline{p}\_{t}^{\xi,a}(\cdot|\varepsilon\_{1:t-1}^{0})=\overline{p}^{\*}\big(\underline{\Lambda}\_{t-1}^{\xi,a}\big)\quad\mbox{for all $t\geq 2$}, |  |

which ensures ([2.26](https://arxiv.org/html/2511.04515v1#S2.E26 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) to hold, as claimed.

The proof for ([2.27](https://arxiv.org/html/2511.04515v1#S2.E27 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) is straightforward. Indeed, by ([2.19](https://arxiv.org/html/2511.04515v1#S2.E19 "In Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Proposition [2.12](https://arxiv.org/html/2511.04515v1#S2.Thmthm12 "Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") it holds that ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒℙ¯ξ,a​(μ¯1ξ,a)\displaystyle\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\underline{\mu}\_{1}^{\xi,a}) | =p¯(⋅|pjS(Λ¯0ξ,a),Λ¯0ξ,a,p¯1ξ,a(⋅))\displaystyle=\overline{p}(\,\cdot\,|\,\operatorname{pj}\_{S}(\underline{\Lambda}\_{0}^{\xi,a}),\,\underline{\Lambda}\_{0}^{\xi,a},\,\underline{p}\_{1}^{\xi,a}(\cdot)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒℙ¯ξ,a​(μ¯t+1ξ,a)\displaystyle\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,a}}(\underline{\mu}\_{t+1}^{\xi,a}) | =p¯(⋅|pjS(Λ¯tξ,a),Λ¯tξ,a,p¯tξ,a(⋅|ε1:t−10))for all t≥1.\displaystyle=\overline{p}(\,\cdot\,|\,\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\,\underline{\Lambda}\_{t}^{\xi,a},\,\underline{p}\_{t}^{\xi,a}(\,\cdot\,|\varepsilon\_{1:t-1}^{0}))\quad\mbox{for all $t\geq 1$}. |  |

Combined with ([6.13](https://arxiv.org/html/2511.04515v1#S6.E13 "In 6.1. Proof of Lemma 2.17 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), this ensures ([2.27](https://arxiv.org/html/2511.04515v1#S2.E27 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) to hold, as claimed. This completes the proof. ∎

### 6.2. Proof of Lemma [2.20](https://arxiv.org/html/2511.04515v1#S2.Thmthm20 "Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We first introduce some kernels used for constructing a∗∈Aa^{\*}\in{\mathcal{}A}. We denote by

|  |  |  |  |
| --- | --- | --- | --- |
| (6.14) |  | KS×A:S×P(S×A)×P(S)∋(s,Λ,μ)↦KS×A(⋅|s,Λ,μ)∈P(A)\displaystyle{\mathcal{}K}\_{S\times A}:S\times{\mathcal{}P}(S\times A)\times{\mathcal{}P}(S)\ni(s,\Lambda,\mu)\mapsto{\mathcal{}K}\_{S\times A}(\,\cdot\,|\,s,\Lambda,\mu)\in{\mathcal{}P}(A) |  |

the universal disintegration kernel (see Lemma [A.3](https://arxiv.org/html/2511.04515v1#A1.Thmthm3 "Lemma A.3 (Universal disintegration; see, e.g., [kallenberg2017random, Corollarly 1.26]). ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty")). Then, we define a kernel

|  |  |  |  |
| --- | --- | --- | --- |
| (6.15) |  | ψ∗:S×P(S)∋(s,μ)↦ψ∗(⋅|s,μ):=KS×A(⋅|s,π¯∗(μ),μ)∈P(A),\displaystyle\psi^{\*}:S\times{\mathcal{}P}(S)\ni(s,\mu)\mapsto\psi^{\*}(\,\cdot\,|s,\mu):={\mathcal{}K}\_{S\times A}(\,\cdot\,|\,s,\overline{\pi}^{\*}(\mu),\mu)\in{\mathcal{}P}(A), |  |

where π¯∗\overline{\pi}^{\*} is the local maximizer given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii).

Moreover, denote by

|  |  |  |  |
| --- | --- | --- | --- |
| (6.16) |  | ρA:P​(A)×[0,1]∋(η,u)↦ρA​(η,u)∈A\displaystyle\rho\_{A}:{\mathcal{}P}(A)\times[0,1]\ni(\eta,u)\mapsto\rho\_{A}(\eta,u)\in A |  |

the Blackwell–Dubins function of the action space AA (see Lemma [A.2](https://arxiv.org/html/2511.04515v1#A1.Thmthm2 "Lemma A.2 (Blackwell and Dubins [blackwell1983extension]). ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty")).

Step 1. Let ℙ~∈Q\widetilde{\mathbb{P}}\in{\mathcal{}Q} be some arbitrary. We will inductively construct a∗∈Aa^{\*}\in{\mathcal{}A} over time t≥0t\geq 0.
Let

|  |  |  |  |
| --- | --- | --- | --- |
| (6.17) |  | s~0:=ξ,μ~0:=ℒℙ~​(s~0),a0∗:=ρA(ψ∗(⋅|s~0,μ~0),h0(ϑ0)),Λ~0:=ℒℙ~​((s~0,a0∗)),\displaystyle\begin{aligned} \tilde{s}\_{0}&:=\xi,\quad&&\tilde{\mu}\_{0}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}(\tilde{s}\_{0}),\\ a^{\*}\_{0}&:=\rho\_{A}\big(\psi^{\*}(\cdot\,|\,\tilde{s}\_{0},\tilde{\mu}\_{0}),h\_{0}(\vartheta\_{0})\big),\quad&&\tilde{\Lambda}\_{0}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}((\tilde{s}\_{0},a\_{0}^{\*})),\end{aligned} |  |

where h0:Θ→[0,1]h\_{0}:\Theta\to[0,1] is given in Remark [2.19](https://arxiv.org/html/2511.04515v1#S2.Thmthm19 "Remark 2.19. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (so that h0​(ϑ0)∼U[0,1]h\_{0}(\vartheta\_{0})\sim{\mathcal{}U}\_{[0,1]}). In particular, since ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S), s~0\tilde{s}\_{0} is F0{\mathcal{}F}\_{0} measurable, and a0∗a\_{0}^{\*} is G0{\mathcal{}G}\_{0} measurable.

For every t≥1t\geq 1 we inductively define

|  |  |  |  |
| --- | --- | --- | --- |
| (6.18) |  | s~t:=F⁡(s~t−1,at−1∗,Λ~t−1,εt,εt0),μ~t:=ℒℙ~​(s~t|ε1:t0),at∗:=ρA(ψ∗(⋅|s~t,μ~t),ht(ϑt)),Λ~t:=ℒℙ~​((s~t,at∗)|ε1:t0),\displaystyle\begin{aligned} \tilde{s}\_{t}&:=\operatorname{F}(\tilde{s}\_{t-1},a\_{t-1}^{\*},\tilde{\Lambda}\_{t-1},\varepsilon\_{t},\varepsilon\_{t}^{0}),\quad&&\tilde{\mu}\_{t}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}(\tilde{s}\_{t}\,|\,\varepsilon\_{1:t}^{0}),\\ a^{\*}\_{t}&:=\rho\_{A}\big(\psi^{\*}(\,\cdot\,|\,\tilde{s}\_{t},\tilde{\mu}\_{t}),h\_{t}(\vartheta\_{t})\big),\quad&&\tilde{\Lambda}\_{t}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}((\tilde{s}\_{t},a\_{t}^{\*})\,|\,\varepsilon\_{1:t}^{0}),\end{aligned} |  |

where ht:Θ→[0,1]h\_{t}:\Theta\to[0,1] is given in Remark [2.19](https://arxiv.org/html/2511.04515v1#S2.Thmthm19 "Remark 2.19. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii) (so that (hu​(ϑu))0≤u≤t(h\_{u}(\vartheta\_{u}))\_{0\leq u\leq t} is i.i.d. with law U[0,1]{\mathcal{}U}\_{[0,1]}). Moreover, by the same arguments presented for the proof of Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty"), s~t\tilde{s}\_{t} is Ft{\mathcal{}F}\_{t} measurable, while at∗a\_{t}^{\*} is Gt{\mathcal{}G}\_{t} measurable. Moreover, (μ~t,Λ~t)(\tilde{\mu}\_{t},\tilde{\Lambda}\_{t}) are Ft0{\mathcal{}F}\_{t}^{0} measurable.

Since a∗=(at∗)t≥0a^{\*}=(a\_{t}^{\*})\_{t\geq 0} constructed via ([6.17](https://arxiv.org/html/2511.04515v1#S6.E17 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) and ([6.18](https://arxiv.org/html/2511.04515v1#S6.E18 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) is 𝔾\mathbb{G} adapted, it is in A{\mathcal{}A}. We underline that the above inductive construction is invariant and can be carried out under any ℙ~∈Q\widetilde{\mathbb{P}}\in{\mathcal{}Q}.

Step 2. We claim that for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q},

|  |  |  |  |
| --- | --- | --- | --- |
| (6.19) |  | stξ,a∗,ℙ=s~t,μtξ,a∗,ℙ=μ~t,Λtξ,a∗,ℙ=Λ~t,ℙ-a.s.,for all t≥0,\displaystyle s\_{t}^{\xi,a^{\*},{\mathbb{P}}}=\tilde{s}\_{t},\quad\mu\_{t}^{\xi,a^{\*},\mathbb{P}}=\tilde{\mu}\_{t},\quad\Lambda\_{t}^{\xi,a^{\*},\mathbb{P}}=\tilde{\Lambda}\_{t},\quad\mbox{$\mathbb{P}$-a.s.},\quad\mbox{for all $t\geq 0$}, |  |

where stξ,a∗,ℙs\_{t}^{\xi,a^{\*},{\mathbb{P}}}, μtξ,a∗,ℙ{\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}, and Λtξ,a∗,ℙ\Lambda\_{t}^{\xi,a^{\*},\mathbb{P}} are given in ([2.12](https://arxiv.org/html/2511.04515v1#S2.E12 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), ([2.15](https://arxiv.org/html/2511.04515v1#S2.E15 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.16](https://arxiv.org/html/2511.04515v1#S2.E16 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), respectively, under (a∗,ℙ)(a^{\*},\mathbb{P}).

Let ℙ∈Q\mathbb{P}\in{\mathcal{}Q} be given. The proof uses an induction over t≥0t\geq 0: For t=0t=0, clearly s0ξ,a,ℙ=s~0=ξ∈LF00​(S)s\_{0}^{\xi,a,{\mathbb{P}}}=\tilde{s}\_{0}=\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S). Moreover, since a0∗a\_{0}^{\*} is G0{\mathcal{}G}\_{0} measurable (noting that G0=σ​(γ,ϑ0){\mathcal{}G}\_{0}=\sigma(\gamma,\vartheta\_{0})) and ℒℙ​(γ,ϑ0)=ℒℙ~​(γ,ϑ0)\mathscr{L}\_{{\mathbb{P}}}(\gamma,\vartheta\_{0})=\mathscr{L}\_{\tilde{\mathbb{P}}}(\gamma,\vartheta\_{0}) (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)), it holds that μ0ξ,a∗,ℙ=μ~0\mu\_{0}^{\xi,a^{\*},\mathbb{P}}=\tilde{\mu}\_{0} and Λ0ξ,a∗,ℙ=Λ~0\Lambda\_{0}^{\xi,a^{\*},\mathbb{P}}=\tilde{\Lambda}\_{0}.

Assume that the induction claim holds true for some t≥0t\geq 0. For the case t+1t+1, by the conditional McKean-Vlasov dynamics given in ([2.12](https://arxiv.org/html/2511.04515v1#S2.E12 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and the induction hypothesis for tt, it holds that ℙ\mathbb{P}-a.s.,

|  |  |  |  |
| --- | --- | --- | --- |
| (6.20) |  | st+1ξ,a∗,ℙ=F⁡(stξ,a∗,ℙ,at∗,Λtξ,a∗,ℙ,εt+1,εt+10)=F⁡(s~t,at∗,Λ~t,εt+1,εt+10)=s~t+1,\displaystyle\begin{aligned} s\_{t+1}^{\xi,a^{\*},{\mathbb{P}}}&=\operatorname{F}(s\_{t}^{\xi,a^{\*},{\mathbb{P}}},a^{\*}\_{t},\Lambda\_{t}^{\xi,a^{\*},\mathbb{P}},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0})\\ &=\operatorname{F}(\tilde{s}\_{t},a^{\*}\_{t},\tilde{\Lambda}\_{t},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0})=\tilde{s}\_{t+1},\end{aligned} |  |

where the second equality holds by the Borel measurability of F\operatorname{F} (see Definition [2.4](https://arxiv.org/html/2511.04515v1#S2.Thmthm4 "Definition 2.4. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)), and the last equality holds by definition ([6.18](https://arxiv.org/html/2511.04515v1#S6.E18 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")).

We now show that Λt+1ξ,a∗,ℙ=Λ~t+1\Lambda\_{t+1}^{\xi,a^{\*},\mathbb{P}}=\tilde{\Lambda}\_{t+1}, ℙ{\mathbb{P}}-a.s.. By Ft+10{\mathcal{}F}\_{t+1}^{0}-measurability of (Λt+1ξ,a∗,ℙ,Λ~t+1)(\Lambda\_{t+1}^{\xi,a^{\*},\mathbb{P}},\tilde{\Lambda}\_{t+1}), it suffices to show that for any bounded Borel measurable functions g^t+1:(E0)t+1→ℝ\hat{g}\_{t+1}:(E^{0})^{t+1}\to\mathbb{R} and f^:S×A→ℝ\hat{f}:S\times A\to\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
| (6.21) |  | 𝔼ℙ​[g^t+1​(ε1:t+10)​f^​(st+1ξ,a∗,ℙ,at+1∗)]=𝔼ℙ​[g^t+1​(ε1:t+10)​∫S×Af​(s~,a~)​Λ~t+1​(d​s~,d​a~)].\displaystyle\mathbb{E}^{{\mathbb{P}}}[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,a^{\*},\mathbb{P}},a^{\*}\_{t+1})]=\mathbb{E}^{{\mathbb{P}}}\bigg[\hat{g}\_{t+1}(\varepsilon^{0}\_{1:t+1})\int\_{S\times A}f(\tilde{s},\tilde{a})\tilde{\Lambda}\_{t+1}(d\tilde{s},d\tilde{a})\bigg]. |  |

Indeed, by ([6.20](https://arxiv.org/html/2511.04515v1#S6.E20 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")),

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ[g^t+1(ε1:t+10)f^(st+1ξ,a∗,ℙ,at+1∗)]=𝔼ℙ[g^t+1(ε1:t+10)f^(s~t+1,at+1∗)]=:It+1.\displaystyle\mathbb{E}^{{\mathbb{P}}}[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,a^{\*},\mathbb{P}},a^{\*}\_{t+1})]=\mathbb{E}^{{\mathbb{P}}}[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(\tilde{s}\_{t+1},a^{\*}\_{t+1})]=:\operatorname{I}^{t+1}. |  |

Moreover, as (s~t+1,at+1∗)(\tilde{s}\_{t+1},a^{\*}\_{t+1}) is Gt+1{\mathcal{}G}\_{t+1} measurable, an application of Lemma [6.1](https://arxiv.org/html/2511.04515v1#S6.Thmthm1 "Lemma 6.1. ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty") ensures that ℙ{\mathbb{P}}-a.s.

|  |  |  |
| --- | --- | --- |
|  | ℒℙ​((s~t+1,at+1∗)|ε1:t+10)=ℒℙ~​((s~t+1,at+1∗)|ε1:t+10)=Λ~t+1,\mathscr{L}\_{\mathbb{P}}\big((\tilde{s}\_{t+1},a^{\*}\_{t+1})|\varepsilon^{0}\_{1:t+1}\big)=\mathscr{L}\_{\widetilde{\mathbb{P}}}\big((\tilde{s}\_{t+1},a^{\*}\_{t+1})|\varepsilon^{0}\_{1:t+1}\big)=\tilde{\Lambda}\_{t+1}, |  |

which implies that It+1\operatorname{I}^{t+1} equals the second term in ([6.21](https://arxiv.org/html/2511.04515v1#S6.E21 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), as claimed.

Using the same arguments presented for ([6.21](https://arxiv.org/html/2511.04515v1#S6.E21 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), we have that μt+1ξ,a∗,ℙ=μ~t+1\mu\_{t+1}^{\xi,a^{\*},\mathbb{P}}=\tilde{\mu}\_{t+1} ℙ\mathbb{P}-a.s.. Hence, by induction hypothesis, the claim ([6.19](https://arxiv.org/html/2511.04515v1#S6.E19 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) holds.

Step 3. Let ℙ∈Q\mathbb{P}\in{\mathcal{}Q} be some arbitrary. Then we claim that ([2.28](https://arxiv.org/html/2511.04515v1#S2.E28 "In Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds. Without loss of generality, we consider the case t≥1t\geq 1, as the case t=0t=0 can be subsumed into it.

By the Ft0{\mathcal{}F}\_{t}^{0}-measurability of (Λtξ,a∗,ℙ,μtξ,a∗,ℙ)({\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}},{\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}), it suffices to show that for any bounded Borel measurable functions g^t:(E0)t→ℝ\hat{g}\_{t}:(E^{0})^{t}\to\mathbb{R} and f^:S×A→ℝ\hat{f}:S\times A\to\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
| (6.22) |  | 𝔼ℙ​[g^t​(ε1:t0)​f^​(stξ,a∗,ℙ,at∗)]=𝔼ℙ​[g^t​(ε1:t0)​∫S×Af​(s~,a~)​π¯∗​(μtξ,a∗,ℙ)​(d​s~,d​a~)],\displaystyle\mathbb{E}^{{\mathbb{P}}}[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\hat{f}(s\_{t}^{\xi,a^{\*},{\mathbb{P}}},a^{\*}\_{t})]=\mathbb{E}^{{\mathbb{P}}}\bigg[\hat{g}\_{t}(\varepsilon^{0}\_{1:t})\int\_{S\times A}f(\tilde{s},\tilde{a})\overline{\pi}^{\*}\big({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}\big)(d\tilde{s},d\tilde{a})\bigg], |  |

where π¯∗\overline{\pi}^{\*} is the local maximizer given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii).

Since g^​(ε1:t0)\hat{g}(\varepsilon\_{1:t}^{0}) is Ft0{\mathcal{}F}\_{t}^{0} measurable and it holds that stξ,a∗,ℙ=s~ts\_{t}^{\xi,a^{\*},{\mathbb{P}}}=\tilde{s}\_{t}, ℙ{\mathbb{P}}-a.s. (see ([6.19](https://arxiv.org/html/2511.04515v1#S6.E19 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) in Step 2),

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ​[g^t​(ε1:t0)​f^​(stξ,a∗,ℙ,at∗)]=𝔼ℙ​[g^t​(ε1:t0)​f^​(s~t,at∗)]=𝔼ℙ[g^t(ε1:t0)𝔼ℙ[𝔼ℙ[f^(s~t,at∗)|Ft]|Ft0]]=:It,\displaystyle\begin{aligned} \mathbb{E}^{{\mathbb{P}}}[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\hat{f}(s\_{t}^{\xi,a^{\*},{\mathbb{P}}},a^{\*}\_{t})]&=\mathbb{E}^{{\mathbb{P}}}[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\hat{f}\big(\tilde{s}\_{t},a^{\*}\_{t}\big)]\\ &=\mathbb{E}^{{\mathbb{P}}}\Big[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\mathbb{E}^{{\mathbb{P}}}\big[\mathbb{E}^{{\mathbb{P}}}[\hat{f}(\tilde{s}\_{t},a^{\*}\_{t})|{\mathcal{}F}\_{t}]\big|{\mathcal{}F}\_{t}^{0}\big]\Big]=:\operatorname{I}\_{t},\end{aligned} |  |

where the last equality follows from the tower property with fact that Ft0⊂Ft{\mathcal{}F}\_{t}^{0}\subset{\mathcal{}F}\_{t}.

Since s~t\tilde{s}\_{t} is Ft{\mathcal{}F}\_{t} measurable and ht​(ϑt)∼U[0,1]h\_{t}(\vartheta\_{t})\sim{\mathcal{}U}\_{[0,1]} is independent of Ft{\mathcal{}F}\_{t} (noting that Ft{\mathcal{}F}\_{t} does not contain the current randomization source ϑt\vartheta\_{t}),

|  |  |  |  |
| --- | --- | --- | --- |
| (6.23) |  | It=𝔼ℙ​[g^t​(ε1:t0)​𝔼ℙ​[𝔼ℙ​[∫Af^​(s~t,a~)​ψ∗​(d​a~|s~t,μ~t)|Ft]|Ft0]]=𝔼ℙ​[g^t​(ε1:t0)​𝔼ℙ​[∫S×Af^​(s~,a~)​KS×A​(d​a~|s~,π¯∗​(μ~t),μ~t)​μ~t​(d​s~)|Ft0]]=𝔼ℙ​[g^t​(ε1:t0)​∫S×Af^​(s~,a~)​π¯∗​(μ~t)​(d​s~,d​a~)],\displaystyle\begin{aligned} \operatorname{I}\_{t}&=\mathbb{E}^{{\mathbb{P}}}\bigg[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\mathbb{E}^{{\mathbb{P}}}\bigg[\mathbb{E}^{{\mathbb{P}}}\bigg[\int\_{A}\hat{f}(\tilde{s}\_{t},\tilde{a})\psi^{\*}(d\tilde{a}\,|\,\tilde{s}\_{t},\tilde{\mu}\_{t})\,\bigg|\,{\mathcal{}F}\_{t}\bigg]\bigg|\,{\mathcal{}F}\_{t}^{0}\bigg]\bigg]\\ &=\mathbb{E}^{{\mathbb{P}}}\bigg[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\mathbb{E}^{{\mathbb{P}}}\bigg[\int\_{S\times A}\hat{f}(\tilde{s},\tilde{a}){\mathcal{}K}\_{S\times A}(d\tilde{a}\,|\,\tilde{s},\overline{\pi}^{\*}(\tilde{\mu}\_{t}),\tilde{\mu}\_{t})\tilde{\mu}\_{t}(d\tilde{s})\,\Big|\,{\mathcal{}F}\_{t}^{0}\bigg]\bigg]\\ &=\mathbb{E}^{{\mathbb{P}}}\bigg[\hat{g}\_{t}(\varepsilon\_{1:t}^{0})\int\_{S\times A}\hat{f}(\tilde{s},\tilde{a})\overline{\pi}^{\*}(\tilde{\mu}\_{t})(d\tilde{s},d\tilde{a})\bigg],\end{aligned} |  |

where the first equality follows from definition of at∗a\_{t}^{\*} given in ([6.18](https://arxiv.org/html/2511.04515v1#S6.E18 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), the second equality follows from definition of ψ∗(⋅|s~t,μ~t)\psi^{\*}(\cdot|\tilde{s}\_{t},\tilde{\mu}\_{t}) (see ([6.15](https://arxiv.org/html/2511.04515v1#S6.E15 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty"))) and Ft0{\mathcal{}F}\_{t}^{0}-measurability of μ~t\tilde{\mu}\_{t}, and the last equality follows from definition of the universal differentiation kernel KS×A{\mathcal{}K}\_{S\times A} (see ([6.14](https://arxiv.org/html/2511.04515v1#S6.E14 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty"))).

Moreover, since μ~t=μtξ,a∗,ℙ\tilde{\mu}\_{t}={\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}, ℙ\mathbb{P}-a.s. (see ([6.19](https://arxiv.org/html/2511.04515v1#S6.E19 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) in Step 2), the last term in ([6.23](https://arxiv.org/html/2511.04515v1#S6.E23 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) equals the second term in ([6.22](https://arxiv.org/html/2511.04515v1#S6.E22 "In 6.2. Proof of Lemma 2.20 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), as claimed. This completes the proof. ∎

### 6.3. Proof of Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

For notational simplicity, set μ:=ℒ​(ξ)\mu:=\mathscr{L}(\xi).

Step 1: We claim that for every n∈ℕn\in\mathbb{N}

|  |  |  |  |
| --- | --- | --- | --- |
| (6.24) |  | Inξ,a∗:=infℙ∈Q𝔼ℙ​[∑t=0n−1βt​r​(stξ,a∗,ℙ,at∗,Λtξ,a∗,ℙ)+βn​V¯∗​(μnξ,a∗,ℙ)]≥V¯∗​(μ),\displaystyle{\mathcal{}I}\_{n}^{\xi,a^{\*}}:=\inf\_{{\mathbb{P}}\in{\mathcal{}Q}}\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{n-1}\beta^{t}\,{r}(s\_{t}^{\xi,a^{\*},{\mathbb{P}}},a^{\*}\_{t},{\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}})+\beta^{n}\,\overline{V}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}})\bigg]\geq\overline{V}^{\*}(\mu), |  |

where for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, let (μtξ,a∗,ℙ)t≥0({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}})\_{t\geq 0} and (Λtξ,a∗,ℙ)t≥0({\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}})\_{t\geq 0} be given by ([2.15](https://arxiv.org/html/2511.04515v1#S2.E15 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.16](https://arxiv.org/html/2511.04515v1#S2.E16 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), respectively.

We prove ([6.24](https://arxiv.org/html/2511.04515v1#S6.E24 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) via an induction over nn. Before proceeding, note that for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q} and t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
| (6.25) |  | 𝔼ℙ​[r​(stξ,a∗,ℙ,at∗,Λtξ,a∗,ℙ)]=𝔼ℙ​[r¯​(pjS⁡(Λtξ,a∗,ℙ),Λtξ,a∗,ℙ)]=𝔼ℙ​[r¯​(μtξ,a∗,ℙ,π¯∗​(μtξ,a∗,ℙ))],\displaystyle\begin{aligned} \mathbb{E}^{{\mathbb{P}}}\big[{r}(s\_{t}^{\xi,a^{\*},{\mathbb{P}}},a^{\*}\_{t},{\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}})\big]&=\mathbb{E}^{{\mathbb{P}}}\big[\overline{r}(\operatorname{pj}\_{S}({\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}})\,,\,{\Lambda}\_{t}^{\xi,a^{\*},\mathbb{P}})\big]\\ &=\mathbb{E}^{{\mathbb{P}}}\big[\overline{r}\big({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}\,,\,\overline{\pi}^{\*}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}})\big)\big],\end{aligned} |  |

where the first equality holds by ([2.20](https://arxiv.org/html/2511.04515v1#S2.E20 "In Remark 2.13. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Remark [2.13](https://arxiv.org/html/2511.04515v1#S2.Thmthm13 "Remark 2.13. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and the second equality follows from ([2.28](https://arxiv.org/html/2511.04515v1#S2.E28 "In Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Lemma [2.20](https://arxiv.org/html/2511.04515v1#S2.Thmthm20 "Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and the fact that π¯∗​(μ)∈𝔘​(μ)\overline{\pi}^{\*}(\mu)\in\mathfrak{U}(\mu) (see Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)).

Hence by the property ([6.25](https://arxiv.org/html/2511.04515v1#S6.E25 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), Inξ,a∗{\mathcal{}I}\_{n}^{\xi,a^{\*}} given in ([6.24](https://arxiv.org/html/2511.04515v1#S6.E24 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) can be represented by

|  |  |  |  |
| --- | --- | --- | --- |
| (6.26) |  | Inξ,a∗=infℙ∈Q𝔼ℙ​[∑t=0n−1βt​r¯​(μtξ,a∗,ℙ,π¯∗​(μtξ,a∗,ℙ))+βn​V¯∗​(μnξ,a∗,ℙ)].\displaystyle{\mathcal{}I}\_{n}^{\xi,a^{\*}}=\inf\_{{\mathbb{P}}\in{\mathcal{}Q}}\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{n-1}\beta^{t}\,\overline{r}\big({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}\,,\,\overline{\pi}^{\*}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}})\big)+\beta^{n}\,\overline{V}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}})\bigg]. |  |

Step 1a: For n=1n=1, let ℙ∈Q{\mathbb{P}}\in{\mathcal{}Q} be induced by some (pt)t≥1∈𝒦0(p\_{t})\_{t\geq 1}\in\mathcal{K}^{0} (see Definition [2.2](https://arxiv.org/html/2511.04515v1#S2.Thmthm2 "Definition 2.2 (Measures). ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

We first note that μ0ξ,a∗,ℙ=μ{\mu}\_{0}^{\xi,a^{\*},\mathbb{P}}=\mu with trivial F00{\mathcal{}F}\_{0}^{0} and ℒℙ​(ε10)=p1∈𝔓0\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{1}^{0})=p\_{1}\in\mathfrak{P}^{0} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)). Combined with ([2.19](https://arxiv.org/html/2511.04515v1#S2.E19 "In Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) (see Proposition [2.12](https://arxiv.org/html/2511.04515v1#S2.Thmthm12 "Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), this implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[r¯​(μ0ξ,a∗,ℙ,π¯∗​(μ0ξ,a∗,ℙ))+β​V¯∗​(μ1ξ,a∗,ℙ)]\displaystyle\mathbb{E}^{{\mathbb{P}}}\big[\overline{r}\big({\mu}\_{0}^{\xi,a^{\*},\mathbb{P}}\,,\,\overline{\pi}^{\*}({\mu}\_{0}^{\xi,a^{\*},\mathbb{P}})\big)+\beta\,\overline{V}^{\*}({\mu}\_{1}^{\xi,a^{\*},\mathbb{P}})\big] | =r¯​(μ,π¯∗​(μ))+β​∫P​(S)V¯∗​(μ′)​p¯​(d​μ′|μ,π¯∗​(μ),p1)\displaystyle=\overline{r}(\mu,\overline{\pi}^{\*}(\mu))+\beta\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\mu^{\prime})\overline{p}(d\mu^{\prime}\big|\mu,\overline{\pi}^{\*}(\mu),p\_{1}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6.27) |  |  | ≥r¯​(μ,π¯∗​(μ))+β​infp∈𝔓0∫P​(S)V¯∗​(μ′)​p¯​(d​μ′|μ,π¯∗​(μ),p)\displaystyle\geq\overline{r}(\mu,\overline{\pi}^{\*}(\mu))+\beta\inf\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\mu^{\prime})\overline{p}(d\mu^{\prime}\big|\mu,\overline{\pi}^{\*}(\mu),p) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T​V¯∗​(μ)=V¯∗​(μ),\displaystyle={\mathcal{}T}\overline{V}^{\*}(\mu)=\overline{V}^{\*}(\mu), |  |

where the last line follows from the optimality of π¯∗​(μ)∈𝔘​(μ)\overline{\pi}^{\*}(\mu)\in\mathfrak{U}(\mu) for T​V¯∗​(μ){\mathcal{}T}\overline{V}^{\*}(\mu) (see Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii) for V¯∗∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}^{\*}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R})) and the fixed point result given in Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

Since ([6.27](https://arxiv.org/html/2511.04515v1#S6.E27 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) holds for any ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, by ([6.26](https://arxiv.org/html/2511.04515v1#S6.E26 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) we have that I1ξ,a∗≥V¯∗​(μ){\mathcal{}I}\_{1}^{\xi,a^{\*}}\geq\overline{V}^{\*}(\mu).

Step 1b: Assume that ([6.24](https://arxiv.org/html/2511.04515v1#S6.E24 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) holds for some n≥1n\geq 1. Let ℙ∈Q{\mathbb{P}}\in{\mathcal{}Q} be induced by some (pt)t≥1∈𝒦0(p\_{t})\_{t\geq 1}\in\mathcal{K}^{0}.

Note that μnξ,a∗,ℙ{\mu}\_{n}^{\xi,a^{\*},\mathbb{P}} and ℒℙ​(εn+10|Fn0)\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{n+1}^{0}|{\mathcal{}F}\_{n}^{0}) are Fn0{\mathcal{}F}\_{n}^{0} measurable and ℒℙ(εn+10|Fn0)=pn+1(⋅|ε1:n0)∈𝔓0\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{n+1}^{0}|{\mathcal{}F}\_{n}^{0})=p\_{n+1}(\cdot|\varepsilon\_{1:n}^{0})\in\mathfrak{P}^{0} ℙ\mathbb{P}-a.s. (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)).

From this, we can use the same arguments presented for ([6.27](https://arxiv.org/html/2511.04515v1#S6.E27 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) to have that ℙ\mathbb{P}-a.s.

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ​[r¯​(μtξ,a∗,ℙ,π¯∗​(μnξ,a∗,ℙ))+β​V¯∗​(μn+1ξ,a∗,ℙ)|Fn0]=r¯(μnξ,a∗,ℙ,π¯∗(μnξ,a∗,ℙ))+β∫P​(S)V¯∗(μ′)p¯(dμ′|μnξ,a∗,ℙ,π¯∗(μnξ,a∗,ℙ),pn+1(⋅|ε1:n0))≥r¯​(μnξ,a∗,ℙ,π¯∗​(μnξ,a∗,ℙ))+β​infp∈𝔓0∫P​(S)V¯∗​(μ′)​p¯​(d​μ′|μnξ,a∗,ℙ,π¯∗​(μnξ,a∗,ℙ),p)=T​V¯∗​(μnξ,a∗,ℙ)=V¯∗​(μnξ,a∗,ℙ),\displaystyle\begin{aligned} &\mathbb{E}^{{\mathbb{P}}}\big[\overline{r}\big({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}})\big)+\beta\overline{V}^{\*}({\mu}\_{n+1}^{\xi,a^{\*},\mathbb{P}})\big|{\mathcal{}F}\_{n}^{0}\big]\\ &\quad=\overline{r}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}}))+\beta\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\mu^{\prime})\overline{p}(d\mu^{\prime}|{\mu}\_{n}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}}),p\_{n+1}(\cdot|\varepsilon\_{1:n}^{0}))\\ &\quad\geq\overline{r}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}}))+\beta\inf\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\mu^{\prime})\overline{p}(d\mu^{\prime}\big|{\mu}\_{n}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}}),p)\\ &\quad={\mathcal{}T}\overline{V}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}})=\overline{V}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}}),\end{aligned} |  |

which ensures that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.28) |  | 𝔼ℙ​[∑t=0nβt​r¯​(μtξ,a∗,ℙ,π¯∗​(μtξ,a∗,ℙ))+βn+1​V¯∗​(μn+1ξ,a∗,ℙ)]≥𝔼ℙ​[∑t=0n−1βt​r¯​(μtξ,a∗,ℙ,π¯∗​(μtξ,a∗,ℙ))+βn​V¯∗​(μnξ,a∗,ℙ)]≥Inξ,a∗≥V¯∗​(μ),\displaystyle\begin{aligned} &\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{n}\beta^{t}\;\overline{r}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}))+\beta^{n+1}\overline{V}^{\*}({\mu}\_{n+1}^{\xi,a^{\*},\mathbb{P}})\bigg]\\ &\quad\geq\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{n-1}\beta^{t}\;\overline{r}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}}))+\beta^{n}\overline{V}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}})\bigg]\geq{\mathcal{}I}\_{n}^{\xi,a^{\*}}\geq\overline{V}^{\*}(\mu),\end{aligned} |  |

where the second inequality follows from definition of Inξ,a∗{\mathcal{}I}\_{n}^{\xi,a^{\*}} given in ([6.26](https://arxiv.org/html/2511.04515v1#S6.E26 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) and the last inequality follows from assumption of the induction for nn (see ([6.24](https://arxiv.org/html/2511.04515v1#S6.E24 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty"))).

As ([6.28](https://arxiv.org/html/2511.04515v1#S6.E28 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) holds for any ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, we have In+1ξ,a∗≥V¯∗​(μ){\mathcal{}I}\_{n+1}^{\xi,a^{\*}}\geq\overline{V}^{\*}(\mu). Therefore, by the induction hypothesis, ([6.24](https://arxiv.org/html/2511.04515v1#S6.E24 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) holds for every n∈ℕn\in\mathbb{N}. We conclude that the claim for Step 1 holds.

Step 2: We claim that V¯∗​(μ)≤V​(ξ)\overline{V}^{\*}(\mu)\leq{V}(\xi). Since r¯\overline{r} and V¯∗\overline{V}^{\*} is bounded and β<1\beta<1 (see Lemma [5.2](https://arxiv.org/html/2511.04515v1#S5.Thmthm2 "Lemma 5.2. ‣ 5.2. Proof of Proposition 2.15 ‣ 5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty") (iii) and V¯∗∈Lipb,L¯⁡(P​(S);ℝ)\overline{V}^{\*}\in\operatorname{Lip}\_{b,\overline{L}}({\mathcal{}P}(S);\mathbb{R})), the dominated convergence theorem asserts that for every μ∈P​(S)\mu\in{\mathcal{}P}(S)

|  |  |  |
| --- | --- | --- |
|  | lim supn→∞Inξ,a∗≤infℙ∈Q{lim supn→∞𝔼ℙ​[∑t=0n−1βt​r¯​(μtξ,a∗,ℙ,π¯∗​(μtξ,a∗,ℙ))]+lim supn→∞𝔼ℙ​[βn​|V¯∗​(μnξ,a∗,ℙ)|]}=infℙ∈Q𝔼ℙ​[∑t=0∞βt​r¯​(μtξ,a∗,ℙ,π¯∗​(μtξ,a∗,ℙ))]=Ja∗​(ξ)≤V​(ξ),\displaystyle\begin{aligned} \limsup\_{n\to\infty}{\mathcal{}I}\_{n}^{\xi,a^{\*}}&\leq\inf\_{{\mathbb{P}}\in{\mathcal{}Q}}\bigg\{\limsup\_{n\to\infty}\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{n-1}\beta^{t}\;\overline{r}\big({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}})\big)\bigg]+\limsup\_{n\to\infty}\mathbb{E}^{{\mathbb{P}}}\big[\beta^{n}\big|\overline{V}^{\*}({\mu}\_{n}^{\xi,a^{\*},\mathbb{P}})\big|\big]\bigg\}\\ &=\inf\_{{\mathbb{P}}\in{\mathcal{}Q}}\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}\;\overline{r}\big({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}},\overline{\pi}^{\*}({\mu}\_{t}^{\xi,a^{\*},\mathbb{P}})\big)\bigg]={\mathcal{}J}^{a^{\*}}(\xi)\leq{V}(\xi),\end{aligned} |  |

where the second equality follows from ([6.25](https://arxiv.org/html/2511.04515v1#S6.E25 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) and the definition of Ja∗​(ξ){\mathcal{}J}^{a^{\*}}(\xi) (see ([2.13](https://arxiv.org/html/2511.04515v1#S2.E13 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))).

Combining this with ([6.24](https://arxiv.org/html/2511.04515v1#S6.E24 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) (as shown in Step 1), we conclude that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.29) |  | V¯∗​(μ)≤lim supn→∞Inξ,a∗≤Ja∗​(ξ)≤V​(ξ),\displaystyle\overline{V}^{\*}(\mu)\leq\limsup\_{n\to\infty}{\mathcal{}I}\_{n}^{\xi,a^{\*}}\leq{\mathcal{}J}^{a^{\*}}(\xi)\leq{V}(\xi), |  |

as claimed.

Step 3:
We claim that V​(ξ)≤V¯∗​(μ){V}(\xi)\leq\overline{V}^{\*}(\mu), which ensures the statement (i) to hold. For every a∈Aa\in{\mathcal{}A}, let ℙ¯∈ξ,aQ\underline{\mathbb{P}}{}^{\xi,a}\in{\mathcal{}Q} be induced by (p¯tξ,a)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,a})\_{t\geq 1}\in\mathcal{K}^{0}
such that ([2.26](https://arxiv.org/html/2511.04515v1#S2.E26 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.27](https://arxiv.org/html/2511.04515v1#S2.E27 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) given in Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") hold.

Then, define Va​(ξ){{\mathcal{}V}}^{a}(\xi) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Va​(ξ):=\displaystyle{{\mathcal{}V}}^{a}(\xi):= | 𝔼ℙ¯ξ,a​[∑t=0∞βt​r​(stξ,a,ℙ¯ξ,a,at,Λ¯tξ,a)]=𝔼ℙ¯ξ,a​[∑t=0∞βt​r¯​(pjS⁡(Λ¯tξ,a),Λ¯tξ,a)],\displaystyle\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}r(s\_{t}^{\xi,a,\underline{\mathbb{P}}{}^{\xi,a}},a\_{t},\underline{\Lambda}\_{t}^{\xi,a})\bigg]=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}\;\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a}\big)\bigg], |  |

where Λ¯0ξ,a\underline{\Lambda}\_{0}^{\xi,a} is the joint law of (s0ξ,a,ℙ¯ξ,a,a0)(s\_{0}^{\xi,a,\underline{\mathbb{P}}{}^{\xi,a}},a\_{0}) under ℙ¯ξ,a\underline{\mathbb{P}}{}^{\xi,a}, for t≥1t\geq 1 Λ¯tξ,a\underline{\Lambda}\_{t}^{\xi,a} is the conditional joint law of (stξ,a,ℙ¯ξ,a,at)(s\_{t}^{\xi,a,\underline{\mathbb{P}}{}^{\xi,a}},a\_{t}) under ℙ¯ξ,a\underline{\mathbb{P}}{}^{\xi,a} given ε1:t0\varepsilon\_{1:t}^{0}, and the last equality follows from the same arguments presented for ([6.25](https://arxiv.org/html/2511.04515v1#S6.E25 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")).

Then by definition of Ja​(ξ){\mathcal{}J}^{a}(\xi) given in ([2.13](https://arxiv.org/html/2511.04515v1#S2.E13 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))

|  |  |  |  |
| --- | --- | --- | --- |
| (6.30) |  | V​(ξ)=supa∈AJa​(ξ)≤supa∈AVa​(ξ).\displaystyle V(\xi)=\sup\_{a\in{\mathcal{}A}}{\mathcal{}J}^{a}(\xi)\leq\sup\_{a\in{\mathcal{}A}}{{\mathcal{}V}}^{a}(\xi). |  |

Moreover, since r¯\overline{r} and V¯∗\overline{V}^{\*} is bounded and β<1\beta<1, by the dominated convergence theorem to the sums ∑t=0nβt​r¯​(pjS⁡(Λ¯tξ,a),Λ¯tξ,a)\sum\_{t=0}^{n}\beta^{t}\overline{r}(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a}) n∈ℕn\in\mathbb{N}, we can have that for every a∈Aa\in{\mathcal{}A}

|  |  |  |  |
| --- | --- | --- | --- |
| (6.31) |  | Va​(ξ)=∑t=0∞βt​𝔼ℙ¯ξ,a​[r¯​(pjS⁡(Λ¯tξ,a),Λ¯tξ,a)+β​V¯∗​(μ¯t+1ξ,a)−β​V¯∗​(μ¯t+1ξ,a)].\displaystyle{{\mathcal{}V}}^{a}(\xi)=\sum\_{t=0}^{\infty}\beta^{t}\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}\big[\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a}\big)+\beta\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a})-\beta\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a})\big]. |  |

Then it follows from ([2.27](https://arxiv.org/html/2511.04515v1#S2.E27 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") that for every t≥0t\geq 0

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ¯ξ,a​[r¯​(pjS⁡(Λ¯tξ,a),Λ¯tξ,a)+β​V¯∗​(μ¯t+1ξ,a)]\displaystyle\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}\big[\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a}\big)+\beta\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a})\big] | =𝔼ℙ¯ξ,a​[𝔼ℙ¯ξ,a​[r¯​(pjS⁡(Λ¯tξ,a),Λ¯tξ,a)+β​V¯∗​(μ¯t+1ξ,a)|Ft0]],\displaystyle=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}\Big[\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}\big[\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a}\big)+\beta\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a})\;\big|\;{\mathcal{}F}\_{t}^{0}\big]\Big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:𝔼ℙ¯ξ,a[J¯(Λ¯tξ,a)]\displaystyle=:\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}[\overline{J}(\underline{\Lambda}\_{t}^{\xi,a})] |  |

where J¯​(Λ¯tξ,a)\overline{J}(\underline{\Lambda}\_{t}^{\xi,a}) is Ft0{\mathcal{}F}\_{t}^{0} measurable and satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (6.32) |  | J¯​(Λ¯tξ,a)=r¯​(pjS⁡(Λ¯tξ,a),Λ¯tξ,a)+β​∫P​(S)V¯∗​(μ~)​p¯​(d​μ~|pjS⁡(Λ¯tξ,a),Λ¯tξ,a,p¯∗​(Λ¯tξ,a))=r¯​(pjS⁡(Λ¯tξ,a),Λ¯tξ,a)+β​infp∈𝔓0∫P​(S)V¯∗​(μ~)​p¯​(d​μ~|pjS⁡(Λ¯tξ,a),Λ¯tξ,a,p)≤T​V¯∗​(pjS⁡(Λ¯tξ,a)),\displaystyle\begin{aligned} \overline{J}(\underline{\Lambda}\_{t}^{\xi,a})&=\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a}\big)+\beta\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\tilde{\mu})\,\overline{p}\big(d\tilde{\mu}\,\big|\,\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\,\underline{\Lambda}\_{t}^{\xi,a},\,\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,a})\big)\\ &=\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\underline{\Lambda}\_{t}^{\xi,a}\big)+\beta\inf\_{p\in\mathfrak{P}^{0}}\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\tilde{\mu})\,\overline{p}\big(d\tilde{\mu}\,\big|\,\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a}),\,\underline{\Lambda}\_{t}^{\xi,a},\,p\big)\\ &\leq{\mathcal{}T}\overline{V}^{\*}(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a})),\end{aligned} |  |

where the equality holds by the local optimality p¯∗​(Λ¯tξ,a)∈𝔓0\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,a})\in\mathfrak{P}^{0} (see Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)) and the inequality holds by definition of T​V¯∗​(pjS⁡(Λ¯tξ,a)){\mathcal{}T}\overline{V}^{\*}(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a})) (see ([2.22](https://arxiv.org/html/2511.04515v1#S2.E22 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")))

Combining ([6.30](https://arxiv.org/html/2511.04515v1#S6.E30 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty"))–([6.32](https://arxiv.org/html/2511.04515v1#S6.E32 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) with the marginal constraint (i.e., pjS⁡(Λ¯tξ,a)=μ¯tξ,a\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a})=\underline{\mu}\_{t}^{\xi,a} ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.; see ([2.17](https://arxiv.org/html/2511.04515v1#S2.E17 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))), and the fixed point result (i.e., T​V¯∗=V¯∗{\mathcal{}T}\overline{V}^{\*}=\overline{V}^{\*}; see Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), we conclude that

|  |  |  |
| --- | --- | --- |
|  | V​(ξ)≤supa∈A∑t=0∞(βt​𝔼ℙ¯ξ,a​[V¯∗​(μ¯tξ,a)]−βt+1​𝔼ℙ¯ξ,a​[V¯∗​(μ¯t+1ξ,a)])=V¯∗​(μ),\displaystyle V(\xi)\leq\sup\_{a\in{\mathcal{}A}}\sum\_{t=0}^{\infty}\big(\beta^{t}\,\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}[\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,a})]-\beta^{t+1}\,\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a}}[\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a})]\big)=\overline{V}^{\*}(\mu), |  |

where the last equality holds by the dominated convergence theorem and the fact that μ¯0ξ,a=μ\underline{\mu}\_{0}^{\xi,a}=\mu, as claimed.

Step 4: It remains to show that ([2.29](https://arxiv.org/html/2511.04515v1#S2.E29 "In item (ii) ‣ Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds. Recall that a∗∈Aa^{\*}\in{\mathcal{}A} is such that
([2.28](https://arxiv.org/html/2511.04515v1#S2.E28 "In Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q} (see Lemma [2.20](https://arxiv.org/html/2511.04515v1#S2.Thmthm20 "Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Moreover, let ℙ¯ξ,a∗∈Q\underline{\mathbb{P}}^{\xi,a^{\*}}\in{\mathcal{}Q} is induced by (p¯tξ,a∗)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,a^{\*}})\_{t\geq 1}\in\mathcal{K}^{0} satisfying ([2.26](https://arxiv.org/html/2511.04515v1#S2.E26 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.27](https://arxiv.org/html/2511.04515v1#S2.E27 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) (see Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

By applying the dominated convergence theorem to ∑t=0n(βt​V¯∗​(μ¯tξ,a∗)−βt+1​V¯∗​(μ¯t+1ξ,a∗))\sum\_{t=0}^{n}(\beta^{t}\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}})-\beta^{t+1}\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a^{\*}})) n∈ℕn\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
| (6.33) |  | V¯∗​(μ)=∑t=0∞(βt​𝔼ℙ¯ξ,a∗​[V¯∗​(μ¯tξ,a∗)]−βt+1​𝔼ℙ¯ξ,a∗​[V¯∗​(μ¯t+1ξ,a∗)]),\displaystyle\overline{V}^{\*}(\mu)=\sum\_{t=0}^{\infty}\big(\beta^{t}\,\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\big[\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}})\big]-\beta^{t+1}\,\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\big[\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a^{\*}})\big]\big), |  |

where μ¯tξ,a∗\underline{\mu}\_{t}^{\xi,a^{\*}} is the conditional law of stξ,a∗,ℙ¯ξ,a∗s\_{t}^{\xi,a^{\*},\underline{\mathbb{P}}{}^{\xi,a^{\*}}} given ε1:t0\varepsilon\_{1:t}^{0}.

Note that for every μ′∈P​(S)\mu^{\prime}\in{\mathcal{}P}(S)

|  |  |  |  |
| --- | --- | --- | --- |
| (6.34) |  | V¯∗​(μ′)=T​V¯∗​(μ′)=r¯​(μ′,π¯∗​(μ′))+β​∫P​(S)V¯∗​(μ~′)​p¯​(d​μ~′|μ′,π¯∗​(μ′),p¯∗​(π¯∗​(μ′))).\displaystyle\overline{V}^{\*}(\mu^{\prime})={\mathcal{}T}\overline{V}^{\*}(\mu^{\prime})=\overline{r}(\mu^{\prime},\overline{\pi}^{\*}(\mu^{\prime}))+\beta\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\tilde{\mu}^{\prime})\overline{p}\big(d\tilde{\mu}^{\prime}|\mu^{\prime},\overline{\pi}^{\*}(\mu^{\prime}),\overline{p}^{\*}(\overline{\pi}^{\*}(\mu^{\prime}))\big). |  |

where the first equality follows from Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and the second equality follows from the optimality of the local optimizers π¯∗\overline{\pi}^{\*} and p¯∗\overline{p}^{\*} given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty").

From ([6.34](https://arxiv.org/html/2511.04515v1#S6.E34 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), it holds that for every t≥0t\geq 0

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ¯ξ,a∗​[V¯∗​(μ¯tξ,a∗)]=𝔼ℙ¯ξ,a∗​[T​V¯∗​(μ¯tξ,a∗)]\displaystyle\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\big[\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}})\big]=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\big[{\mathcal{}T}\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}})\big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼ℙ¯ξ,a∗​[r¯​(μ¯tξ,a∗,π¯∗​(μ¯tξ,a∗))+β​∫P​(S)V¯∗​(μ~′)​p¯​(d​μ~′|μ¯tξ,a∗,π¯∗​(μ¯tξ,a∗),p¯∗​(π¯∗​(μ¯tξ,a∗)))]\displaystyle\hskip 20.00003pt=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\bigg[\overline{r}(\underline{\mu}\_{t}^{\xi,a^{\*}},\overline{\pi}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}}))+\beta\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\tilde{\mu}^{\prime})\overline{p}\big(d\tilde{\mu}^{\prime}|\underline{\mu}\_{t}^{\xi,a^{\*}},\overline{\pi}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}}),\overline{p}^{\*}(\overline{\pi}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}}))\big)\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼ℙ¯ξ,a∗[r¯(pjS(Λ¯tξ,a∗),Λ¯tξ,a∗)+β∫P​(S)V¯∗(μ~′)p¯(dμ~′|pjS(Λ¯tξ,a∗),Λ¯tξ,a∗,p¯∗(Λ¯tξ,a∗))]=:It,\displaystyle\hskip 20.00003pt=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\bigg[\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a^{\*}}),\underline{\Lambda}\_{t}^{\xi,a^{\*}}\big)+\beta\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\tilde{\mu}^{\prime})\overline{p}\big(d\tilde{\mu}^{\prime}|\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a^{\*}}),\underline{\Lambda}\_{t}^{\xi,a^{\*}},\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,a^{\*}})\big)\bigg]=:\operatorname{I}\_{t}, |  |

where Λ¯0ξ,a∗\underline{\Lambda}\_{0}^{\xi,a^{\*}} is the joint law of (s0ξ,a∗,ℙ¯ξ,a∗,a0∗)(s\_{0}^{\xi,a^{\*},\underline{\mathbb{P}}{}^{\xi,a^{\*}}},a^{\*}\_{0}) under ℙ¯ξ,a∗\underline{\mathbb{P}}{}^{\xi,a^{\*}}, for t≥1t\geq 1 Λ¯tξ,a∗\underline{\Lambda}\_{t}^{\xi,a^{\*}} is the conditional joint law of (stξ,a∗,ℙ¯ξ,a∗,at∗)(s\_{t}^{\xi,a^{\*},\underline{\mathbb{P}}{}^{\xi,a^{\*}}},a\_{t}^{\*}) under ℙ¯ξ,a∗\underline{\mathbb{P}}{}^{\xi,a^{\*}} given ε1:t0\varepsilon\_{1:t}^{0}, and the last equality follows from the fact that Λ¯tξ,a∗=π¯∗​(μ¯tξ,a∗)\underline{\Lambda}\_{t}^{\xi,a^{\*}}=\overline{\pi}^{\*}(\underline{\mu}\_{t}^{\xi,a^{\*}}) ℙ¯ξ,a∗\underline{\mathbb{P}}{}^{\xi,a^{\*}}-a.s.; see Lemma [2.20](https://arxiv.org/html/2511.04515v1#S2.Thmthm20 "Lemma 2.20. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), and the marginal constraint that pjS⁡(Λ¯tξ,a∗)=μ¯tξ,a∗\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a^{\*}})=\underline{\mu}\_{t}^{\xi,a^{\*}} ℙ¯ξ,a∗\underline{\mathbb{P}}^{\xi,a^{\*}}-a.s.; see ([2.17](https://arxiv.org/html/2511.04515v1#S2.E17 "In 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

Furthermore, by ([2.27](https://arxiv.org/html/2511.04515v1#S2.E27 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Lemma [2.17](https://arxiv.org/html/2511.04515v1#S2.Thmthm17 "Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") for (a∗,ℙ¯ξ,a∗)(a^{\*},\underline{\mathbb{P}}^{\xi,a^{\*}}), it holds that for every t≥0t\geq 0

|  |  |  |
| --- | --- | --- |
|  | It=𝔼ℙ¯ξ,a∗​[r¯​(pjS⁡(Λ¯tξ,a∗),Λ¯tξ,a∗)+β​V¯∗​(μ¯t+1ξ,a∗)].\displaystyle\operatorname{I}\_{t}=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\big[\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a^{\*}}),\underline{\Lambda}\_{t}^{\xi,a^{\*}}\big)+\beta\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,a^{\*}})\big]. |  |

Combined with ([6.33](https://arxiv.org/html/2511.04515v1#S6.E33 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), this ensures that

|  |  |  |
| --- | --- | --- |
|  | V¯∗​(μ)=∑t=0∞βt​𝔼ℙ¯ξ,a∗​[r¯​(pjS⁡(Λ¯tξ,a∗),Λ¯tξ,a∗)]=𝔼ℙ¯ξ,a∗​[∑t=0∞βt​r¯​(pjS⁡(Λ¯tξ,a∗),Λ¯tξ,a∗)].\overline{V}^{\*}(\mu)=\sum\_{t=0}^{\infty}\beta^{t}\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\big[\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a^{\*}}),\underline{\Lambda}\_{t}^{\xi,a^{\*}}\big)\big]=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a^{\*}}),\underline{\Lambda}\_{t}^{\xi,a^{\*}}\big)\bigg]. |  |

Therefore, by the equality V¯∗​(μ)=V​(ξ)\overline{V}^{\*}(\mu)={V}(\xi) (from Step 2 and Step 3), we conclude that

|  |  |  |
| --- | --- | --- |
|  | V¯∗​(μ)=V​(ξ)=supa∈AJa​(ξ)=𝔼ℙ¯ξ,a∗​[∑t=0∞βt​r¯​(pjS⁡(Λ¯tξ,a∗),Λ¯tξ,a∗)]=𝔼ℙ¯ξ,a∗​[∑t=0∞βt​r​(stξ,a∗,ℙ¯ξ,a∗,at∗,Λ¯tξ,a∗)]=Ja∗​(ξ),\displaystyle\begin{aligned} \overline{V}^{\*}(\mu)=V(\xi)=\sup\_{a\in{\mathcal{}A}}{\mathcal{}J}^{a}(\xi)&=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,a^{\*}}),\underline{\Lambda}\_{t}^{\xi,a^{\*}}\big)\bigg]\\ &=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,a^{\*}}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}r\big(s\_{t}^{\xi,a^{\*},\underline{\mathbb{P}}{}^{\xi,a^{\*}}},a^{\*}\_{t},\underline{\Lambda}\_{t}^{\xi,a^{\*}}\big)\bigg]={\mathcal{}J}^{a^{\*}}(\xi),\end{aligned} |  |

where the last line follows from the same arguments presented for ([6.25](https://arxiv.org/html/2511.04515v1#S6.E25 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), and the inequality ([6.29](https://arxiv.org/html/2511.04515v1#S6.E29 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) given in Step 2. This completes the proof. ∎

## 7. Proof of results in Section [2.5](https://arxiv.org/html/2511.04515v1#S2.SS5 "2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

### 7.1. Proof of Lemma [2.25](https://arxiv.org/html/2511.04515v1#S2.Thmthm25 "Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We first prove ([2.33](https://arxiv.org/html/2511.04515v1#S2.E33 "In Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). For simplicity, denote for every t≥0t\geq 0 by

|  |  |  |
| --- | --- | --- |
|  | μt:=μtξ,πc,ℙ,Λt:=Λtξ,πc,ℙ,νt+1:=ℒℙ​(εt+10|Ft0).\displaystyle\mu\_{t}:=\mu\_{t}^{\xi,\pi^{c},\mathbb{P}},\qquad\Lambda\_{t}:=\Lambda\_{t}^{\xi,\pi^{c},\mathbb{P}},\qquad\nu\_{t+1}:=\mathscr{L}\_{\mathbb{P}}(\varepsilon\_{t+1}^{0}|{\mathcal{}F}\_{t}^{0}). |  |

As the case for t=0t=0 can be subsumed into the others for t≥1t\geq 1, we consider the case t≥1t\geq 1.
Since Λt\Lambda\_{t} and μt\mu\_{t} are Ft0{\mathcal{}F}\_{t}^{0} measurable, it is sufficient to show that for any bounded Borel measurable functions g:(E0)t→ℝg:(E^{0})^{t}\to\mathbb{R} and f:S×A→ℝf:S\times A\to\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ​[g​(ε1:t0)​f​(stξ,πc,ℙ,atπc,ℙ)]=𝔼ℙ​[g​(ε1:t0)​∫S×Af​(s′,a′)​πtc​(d​a~|s~,μt)​μt​(d​s~)].\displaystyle\mathbb{E}^{\mathbb{P}}\big[g(\varepsilon\_{1:t}^{0})f\big(s\_{t}^{\xi,\pi^{c},\mathbb{P}},a\_{t}^{\pi^{c},\mathbb{P}})\big]=\mathbb{E}^{\mathbb{P}}\bigg[g(\varepsilon\_{1:t}^{0})\int\_{S\times A}f(s^{\prime},a^{\prime})\pi^{c}\_{t}\big(d\tilde{a}|\tilde{s},\mu\_{t}\big)\mu\_{t}(d\tilde{s})\bigg]. |  |

Note that g​(ε1:t0)g(\varepsilon\_{1:t}^{0}) is Ft0{\mathcal{}F}\_{t}^{0} measurable and stξ,πc,ℙs\_{t}^{\xi,\pi^{c},\mathbb{P}} is Ft{\mathcal{}F}\_{t} measurable. Hence, by the distributional constraint that ℒℙ(atπc,ℙ|Ft)=πtc(⋅|stξ,πc,ℙ,μt)\mathscr{L}\_{\mathbb{P}}(a\_{t}^{\pi^{c},\mathbb{P}}|{\mathcal{}F}\_{t})=\pi\_{t}^{c}(\cdot|s^{\xi,\pi^{c},\mathbb{P}}\_{t},\mu\_{t}) ℙ\mathbb{P}-a.s. (see ([2.30](https://arxiv.org/html/2511.04515v1#S2.E30 "In item (ii) ‣ Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"))) and the tower property,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[g​(ε1:t0)​f​(stξ,πc,ℙ,atπc,ℙ)]\displaystyle\mathbb{E}^{\mathbb{P}}\big[g(\varepsilon\_{1:t}^{0})f(s\_{t}^{\xi,\pi^{c},\mathbb{P}},a\_{t}^{\pi^{c},\mathbb{P}})\big] | =𝔼ℙ​[g​(ε1:t0)​𝔼ℙ​[𝔼ℙ​[f​(stξ,πc,ℙ,atπc,ℙ)|Ftc]|Ft0]]\displaystyle=\mathbb{E}^{\mathbb{P}}\Big[g(\varepsilon\_{1:t}^{0})\mathbb{E}^{\mathbb{P}}\big[\mathbb{E}^{\mathbb{P}}[f(s\_{t}^{\xi,\pi^{c},\mathbb{P}},a\_{t}^{\pi^{c},\mathbb{P}})\,|\,{\mathcal{}F}\_{t}^{c}]\big|\,{\mathcal{}F}\_{t}^{0}\big]\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ[g(ε1:t0)∫Af(stξ,πc,ℙ,a~)πtc(da′|stξ,πc,ℙ,μt)]=:It.\displaystyle=\mathbb{E}^{\mathbb{P}}\bigg[g(\varepsilon\_{1:t}^{0})\int\_{A}f(s\_{t}^{\xi,\pi^{c},\mathbb{P}},\tilde{a})\pi^{c}\_{t}(da^{\prime}|s\_{t}^{\xi,\pi^{c},\mathbb{P}},\mu\_{t})\bigg]=:\operatorname{I}\_{t}. |  |

Moreover by the definition of μt\mu\_{t} and its Ft0{\mathcal{}F}\_{t}^{0}-measurability,

|  |  |  |  |
| --- | --- | --- | --- |
|  | It\displaystyle\operatorname{I}\_{t} | =𝔼ℙ​[g​(ε1:t0)​𝔼ℙ​[∫Af​(stξ,πc,ℙ,a~)​πtc​(d​a′|stξ,πc,ℙ,μt)|Ft0]]\displaystyle=\mathbb{E}^{\mathbb{P}}\bigg[g(\varepsilon\_{1:t}^{0})\mathbb{E}^{\mathbb{P}}\bigg[\int\_{A}f(s\_{t}^{\xi,\pi^{c},\mathbb{P}},\tilde{a})\pi^{c}\_{t}(da^{\prime}|s\_{t}^{\xi,\pi^{c},\mathbb{P}},\mu\_{t})\,\Big|\,{\mathcal{}F}\_{t}^{0}\bigg]\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ​[g​(ε1:t0)​∫S×Af​(s′,a′)​πtc​(d​a~|s~,μt)​μt​(d​s~)],\displaystyle=\mathbb{E}^{\mathbb{P}}\bigg[g(\varepsilon\_{1:t}^{0})\int\_{S\times A}f(s^{\prime},a^{\prime})\pi^{c}\_{t}\big(d\tilde{a}|\tilde{s},\mu\_{t}\big)\mu\_{t}(d\tilde{s})\bigg], |  |

as claimed.

Moreover, since pjS(μtξ,πc,ℙ⊗^πtc(⋅|⋅,μtξ,πc,ℙ))=μtξ,πc,ℙ\operatorname{pj}\_{S}(\mu\_{t}^{\xi,\pi^{c},\mathbb{P}}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\mu\_{t}^{\xi,\pi^{c},\mathbb{P}}))=\mu\_{t}^{\xi,\pi^{c},\mathbb{P}}, we can the same arguments as in the proof of Proposition [2.12](https://arxiv.org/html/2511.04515v1#S2.Thmthm12 "Proposition 2.12. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (we refer to Section [5](https://arxiv.org/html/2511.04515v1#S5 "5. Proof of results in Section 2.3 ‣ Robust mean-field control under common noise uncertainty")) to get that ([2.34](https://arxiv.org/html/2511.04515v1#S2.E34 "In Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds ℙ\mathbb{P}-a.s..∎

### 7.2. Proof of Lemma [2.26](https://arxiv.org/html/2511.04515v1#S2.Thmthm26 "Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

We first prove ([2.35](https://arxiv.org/html/2511.04515v1#S2.E35 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Step 1: Let πc∈Πc\pi^{c}\in\Pi^{c} be given, and let ℙ~∈Q\widetilde{\mathbb{P}}\in{\mathcal{}Q} be some arbitrary. Then set

|  |  |  |  |
| --- | --- | --- | --- |
| (7.1) |  | s~0:=ξ,μ~0:=ℒℙ~​(s~0),a~0:=ρA(π0c(⋅|s~0,μ~0),h0(ϑ0)),\displaystyle\begin{aligned} &\tilde{s}\_{0}:=\xi,\quad\quad&&\tilde{\mu}\_{0}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}(\tilde{s}\_{0}),\\ &\tilde{a}\_{0}:=\rho\_{A}\big(\pi\_{0}^{c}(\cdot\,|\,\tilde{s}\_{0},\tilde{\mu}\_{0}),h\_{0}(\vartheta\_{0})\big),\quad\end{aligned} |  |

where ρA\rho\_{A} is the Blackwell-Dubins function on AA (see Lemma [A.2](https://arxiv.org/html/2511.04515v1#A1.Thmthm2 "Lemma A.2 (Blackwell and Dubins [blackwell1983extension]). ‣ Appendix A Supplementary statements ‣ Robust mean-field control under common noise uncertainty")) and h0h\_{0} is given in Remark [2.19](https://arxiv.org/html/2511.04515v1#S2.Thmthm19 "Remark 2.19. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Here we note that s~0\tilde{s}\_{0} is F0{\mathcal{}F}\_{0} measurable (as ξ∈LF00​(S)\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S)) and a~0\tilde{a}\_{0} is G0{\mathcal{}G}\_{0} measurable.

Then we define by

|  |  |  |  |
| --- | --- | --- | --- |
| (7.2) |  | p¯1ξ,πc:=p¯∗(μ~0⊗^π0c(⋅|⋅,μ~0))∈𝔓0,\displaystyle\underline{p}\_{1}^{\xi,\pi^{c}}:=\overline{p}^{\*}\big(\tilde{\mu}\_{0}\mathbin{\hat{\otimes}}\pi\_{0}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{0})\big)\in\mathfrak{P}^{0}, |  |

where p¯∗\overline{p}^{\*} is given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i).

Next, for every t≥1t\geq 1 we inductively set

|  |  |  |  |
| --- | --- | --- | --- |
| (7.3) |  | s~t:=F(s~t−1,a~t−1,μ~t−1⊗^πt−1c(⋅|⋅,μ~t−1),εt,εt0),μ~t:=ℒℙ~​(s~t|ε1:t0),a~t:=ρA(πtc(⋅|s~t,μ~t),ht(ϑt)),\displaystyle\begin{aligned} &\tilde{s}\_{t}:=\operatorname{F}\big(\tilde{s}\_{t-1},\tilde{a}\_{t-1},\tilde{\mu}\_{t-1}\mathbin{\hat{\otimes}}\pi\_{t-1}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t-1}),\varepsilon\_{t},\varepsilon\_{t}^{0}\big),\quad&&\tilde{\mu}\_{t}:=\mathscr{L}\_{\widetilde{\mathbb{P}}}(\tilde{s}\_{t}\,|\,\varepsilon\_{1:t}^{0}),\\ &\tilde{a}\_{t}:=\rho\_{A}\big(\pi\_{t}^{c}(\cdot\,|\,\tilde{s}\_{t},\tilde{\mu}\_{t}),h\_{t}(\vartheta\_{t})\big),\quad\end{aligned} |  |

Here, by using the same arguments presented for the proof of Lemma [4.1](https://arxiv.org/html/2511.04515v1#S4.Thmthm1 "Lemma 4.1. ‣ 4. Proof of results in Section 2.2 ‣ Robust mean-field control under common noise uncertainty") (ii), we can deduce that s~t\tilde{s}\_{t} is Ft{\mathcal{}F}\_{t} measurable and a~t\tilde{a}\_{t} is Gt{\mathcal{}G}\_{t} measurable. Moreover, (μ~t,Λ~t)(\tilde{\mu}\_{t},\tilde{\Lambda}\_{t}) are Ft0{\mathcal{}F}\_{t}^{0} measurable.

From this, we can consider a Borel measurable function lt:(E0)t→P​(S×A)l\_{t}:(E^{0})^{t}\to{\mathcal{}P}(S\times A) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (7.4) |  | lt(ε1:t0)=μ~t⊗^πtc(⋅|⋅,μ~t).\displaystyle l\_{t}(\varepsilon\_{1:t}^{0})=\tilde{\mu}\_{t}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t}). |  |

Then, define p¯t+1ξ,πc:(E0)t∋e1:t0↦p¯t+1ξ,πc(⋅|e1:t0)∈P(E0)\underline{p}\_{t+1}^{\xi,\pi^{c}}:(E^{0})^{t}\ni e\_{1:t}^{0}\mapsto\underline{p}\_{t+1}^{\xi,\pi^{c}}(\cdot\,|\,e\_{1:t}^{0})\in{\mathcal{}P}(E^{0}) by

|  |  |  |  |
| --- | --- | --- | --- |
| (7.5) |  | p¯t+1ξ,πc(⋅|e1:t0):=p¯∗(lt(e1:t0))∈𝔓0.\displaystyle\underline{p}\_{t+1}^{\xi,\pi^{c}}(\,\cdot\,|\,e\_{1:t}^{0}):=\overline{p}^{\*}\big(l\_{t}(e\_{1:t}^{0})\big)\in\mathfrak{P}^{0}. |  |

Therefore we can define by ℙ¯ξ,πc∈Q\underline{\mathbb{P}}^{\xi,\pi^{c}}\in{\mathcal{}Q} the measure induced by (p¯tξ,πc)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,\pi^{c}})\_{t\geq 1}\in\mathcal{K}^{0} given in ([7.2](https://arxiv.org/html/2511.04515v1#S7.E2 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) and ([7.5](https://arxiv.org/html/2511.04515v1#S7.E5 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")).

Step 2: Recall (μ~t)t≥0(\tilde{\mu}\_{t})\_{t\geq 0} given in ([7.1](https://arxiv.org/html/2511.04515v1#S7.E1 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) and ([7.3](https://arxiv.org/html/2511.04515v1#S7.E3 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")). We claim that ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (7.6) |  | μ¯tξ,πc=μ~t,for all t≥0,\displaystyle\underline{\mu}\_{t}^{\xi,\pi^{c}}=\tilde{\mu}\_{t},\quad\mbox{for all $t\geq 0$,} |  |

where μ¯0ξ,a\underline{\mu}\_{0}^{\xi,a} is the law of s0ξ,a,ℙ¯ξ,as\_{0}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}} under ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}, and for t≥1t\geq 1 μ¯tξ,a\underline{\mu}\_{t}^{\xi,a} is the conditional law of stξ,a,ℙ¯ξ,as\_{t}^{\xi,a,\underline{\mathbb{P}}^{\xi,a}} under ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a} given ε1:t0\varepsilon^{0}\_{1:t}.

The proof uses an induction over t≥0t\geq 0: For t=0t=0, clearly s0ξ,πc,ℙ¯ξ,a=s~0=ξ∈LF00​(S)s\_{0}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,a}}=\tilde{s}\_{0}=\xi\in L\_{{\mathcal{}F}\_{0}}^{0}(S). Moreover, since ℒℙ¯ξ,πc​(γ)=ℒℙ~​(γ)\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\gamma)=\mathscr{L}\_{\tilde{\mathbb{P}}}(\gamma) (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii)), it holds that μ¯0ξ,πc=μ~0\underline{\mu}\_{0}^{\xi,\pi^{c}}=\tilde{\mu}\_{0}.

Assume that the induction claim holds for some t≥0t\geq 0. By Ft+10{\mathcal{}F}\_{t+1}^{0}-measurability of (μt+1ξ,πc,μ~t+1)(\mu\_{t+1}^{\xi,\pi^{c}},\tilde{\mu}\_{t+1}), it suffices to show that for any bounded Borel measurable functions g^t+1:(E0)t+1→ℝ\hat{g}\_{t+1}:(E^{0})^{t+1}\to\mathbb{R} and f^:S→ℝ\hat{f}:S\to\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
| (7.7) |  | 𝔼ℙ¯ξ,πc​[g^t+1​(ε1:t+10)​f^​(st+1ξ,πc,ℙ¯ξ,πc)]=𝔼ℙ¯ξ,πc​[g^t+1​(ε1:t+10)​∫S×Af​(s~)​μ~t+1​(d​s~)].\displaystyle\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\big[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}})\big]=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\bigg[\hat{g}\_{t+1}(\varepsilon^{0}\_{1:t+1})\int\_{S\times A}f(\tilde{s})\tilde{\mu}\_{t+1}(d\tilde{s})\bigg]. |  |

Indeed, by the conditional McKean-Vlasov dynamics given in ([2.30](https://arxiv.org/html/2511.04515v1#S2.E30 "In item (ii) ‣ Definition 2.23. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and Fubini’s theorem

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ¯ξ,πc[\displaystyle\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\big[ | g^t+1(ε1:t+10)f^(st+1ξ,πc,ℙ¯ξ,πc)]=𝔼ℙ¯ξ,πc[g^t+1(ε1:t+10)f^(F(stξ,πc,ℙ,atπc,ℙ,Λ¯tξ,πc,εt+1,εt+10))]\displaystyle\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}})\big]=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\Big[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}\big(\operatorname{F}(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}},\underline{\Lambda}\_{t}^{\xi,\pi^{c}},\varepsilon\_{t+1},\varepsilon\_{t+1}^{0})\big)\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (7.8) |  |  | =∫E𝔼ℙ¯ξ,πc[g^t+1(ε1:t+10)f^(F(stξ,πc,ℙ,atπc,ℙ,Λ¯tξ,πc,e,εt+10))]λε(de)=:It,\displaystyle\hskip 10.00002pt=\int\_{E}\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\Big[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}\big(\operatorname{F}(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}},\underline{\Lambda}\_{t}^{\xi,\pi^{c}},e,\varepsilon\_{t+1}^{0})\big)\Big]\lambda\_{\varepsilon}(de)=:\operatorname{I}\_{t}, |  |

where the second equality holds since εt+1\varepsilon\_{t+1} is independent of Gt∨σ​(εt+10){\mathcal{}G}\_{t}\vee\sigma(\varepsilon\_{t+1}^{0}) with ℒℙ¯ξ,πc​(εt+1)=λε\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\varepsilon\_{t+1})=\lambda\_{\varepsilon} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i), (ii)).

Moreover, since εt+10\varepsilon\_{t+1}^{0} is conditionally independent of Gt{\mathcal{}G}\_{t} given Ft0{\mathcal{}F}\_{t}^{0} (see Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii)) with ℒℙ¯ξ,πc​(εt+10|Ft0)=p¯t+1ξ,πc​(d​e0|ε1:t0)\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\varepsilon\_{t+1}^{0}|{\mathcal{}F}\_{t}^{0})=\underline{p}\_{t+1}^{\xi,\pi^{c}}(de^{0}\,|\,\varepsilon\_{1:t}^{0}) (by definition of ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}), and stξ,πc,ℙ,atπc,ℙs^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}}, and Λ¯tξ,πc\underline{\Lambda}\_{t}^{\xi,\pi^{c}} are all Gt{\mathcal{}G}\_{t} measurable, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (7.9) |  | It=∫E𝔼ℙ¯ξ,πc​[∫E0(g^t+1​(ε1:t0,e0)​DFt0⁡(e,e0))​p¯t+1ξ,πc​(d​e0|ε1:t0)]​λε​(d​e)\displaystyle\operatorname{I}\_{t}=\int\_{E}\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\bigg[\int\_{E^{0}}\Big(\hat{g}\_{t+1}(\varepsilon\_{1:t}^{0},e^{0})\operatorname{D}\_{{\mathcal{}F}\_{t}^{0}}(e,e^{0})\Big)\underline{p}\_{t+1}^{\xi,\pi^{c}}(de^{0}\,|\,\varepsilon\_{1:t}^{0})\bigg]\lambda\_{\varepsilon}(de) |  |

where for every (e,e0)∈E×E0(e,e^{0})\in E\times E^{0}

|  |  |  |  |
| --- | --- | --- | --- |
|  | DFt0⁡(e,e0):=\displaystyle\operatorname{D}\_{{\mathcal{}F}\_{t}^{0}}(e,e^{0}):= | 𝔼ℙ¯ξ,πc​[f^​(F⁡(stξ,πc,ℙ,atπc,ℙ,Λ¯tξ,πc,e,e0))|Ft0]\displaystyle\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\Big[\hat{f}\big(\operatorname{F}(s^{\xi,\pi^{c},\mathbb{P}}\_{t},a\_{t}^{\pi^{c},\mathbb{P}},\underline{\Lambda}\_{t}^{\xi,\pi^{c}},e,e^{0})\big)\,\Big|\,{\mathcal{}F}\_{t}^{0}\Big]\, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫S×Af^​(F⁡(s,a,Λ¯tξ,πc,e,e0))​Λ¯tξ,πc​(d​s,d​a).\displaystyle\int\_{S\times A}\hat{f}\big(\operatorname{F}(s,a,\underline{\Lambda}\_{t}^{\xi,\pi^{c}},e,e^{0})\big)\underline{\Lambda}\_{t}^{\xi,\pi^{c}}(ds,da). |  |

Moreover, from ([2.33](https://arxiv.org/html/2511.04515v1#S2.E33 "In Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Lemma [2.25](https://arxiv.org/html/2511.04515v1#S2.Thmthm25 "Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") it holds for every (e,e0)∈E×E0(e,e^{0})\in E\times E^{0} that ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}-a.s.,

|  |  |  |
| --- | --- | --- |
|  | DFt0⁡(e,e0)=∫S×Af^(F(s,a,(μ¯tξ,πc⊗^πtc(⋅|⋅,μ¯tξ,πc)),e,e0))(μ¯tξ,πc⊗^πtc(⋅|⋅,μ¯tξ,πc))(ds,da)=∫S×Af^(F(s,a,(μ~t⊗^πtc(⋅|⋅,μ~t)),e,e0))(μ~t⊗^πtc(⋅|⋅,μ~t))(ds,da)\displaystyle\begin{aligned} \operatorname{D}\_{{\mathcal{}F}\_{t}^{0}}(e,e^{0})&=\int\_{S\times A}\hat{f}\Big(\operatorname{F}\big(s,a,\big(\underline{\mu}\_{t}^{\xi,\pi^{c}}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\underline{\mu}\_{t}^{\xi,\pi^{c}})\big),e,e^{0}\big)\Big)\big(\underline{\mu}\_{t}^{\xi,\pi^{c}}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\underline{\mu}\_{t}^{\xi,\pi^{c}})\big)(ds,da)\\ &=\int\_{S\times A}\hat{f}\Big(\operatorname{F}\big(s,a,\big(\tilde{\mu}\_{t}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t})\big),e,e^{0}\big)\Big)\big(\tilde{\mu}\_{t}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t})\big)(ds,da)\end{aligned} |  |

where the second inequality follows from the induction assumption at tt.

Furthermore, since s~t\tilde{s}\_{t} is Gt{\mathcal{}G}\_{t} measurable (noting that Ft⊂Gt{\mathcal{}F}\_{t}\subset{\mathcal{}G}\_{t}), an application of Lemma [6.1](https://arxiv.org/html/2511.04515v1#S6.Thmthm1 "Lemma 6.1. ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty") ensures that μ~t=ℒℙ¯ξ,πc​(s~t|Ft0)\tilde{\mu}\_{t}=\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\tilde{s}\_{t}|{\mathcal{}F}\_{t}^{0}) ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}-a.s.. This implies that ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
|  | DFt0⁡(e,e0)\displaystyle\operatorname{D}\_{{\mathcal{}F}\_{t}^{0}}(e,e^{0}) | =∫S×Af^(F(s,a,(μ~t⊗^πtc(⋅|⋅,μ~t)),e,e0))(ℒℙ¯ξ,πc(s~t|Ft0)⊗^πtc(⋅|⋅,μ~t))(ds,da)\displaystyle=\int\_{S\times A}\hat{f}\Big(\operatorname{F}\big(s,a,\big(\tilde{\mu}\_{t}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t})\big),e,e^{0}\big)\Big)\big(\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\tilde{s}\_{t}|{\mathcal{}F}\_{t}^{0})\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t})\big)(ds,da) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (7.10) |  |  | =𝔼ℙ¯ξ,πc[∫Af^(F(s~t,a,(μ~t⊗^πtc(⋅|⋅,μ~t)),e,e0))πtc(da|s~t,μ~t)|Ft0]\displaystyle=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\bigg[\int\_{A}\hat{f}\Big(\operatorname{F}\big(\tilde{s}\_{t},a,\big(\tilde{\mu}\_{t}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t})\big),e,e^{0}\big)\Big)\pi\_{t}^{c}(da\,|\,\tilde{s}\_{t},\tilde{\mu}\_{t})\,\Big|{\mathcal{}F}\_{t}^{0}\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ¯ξ,πc[f^(F(s~t,a~t,(μ~t⊗^πtc(⋅|⋅,μ~t)),e,e0))|Ft0],\displaystyle=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\Big[\hat{f}\Big(\operatorname{F}\big(\tilde{s}\_{t},\tilde{a}\_{t},\big(\tilde{\mu}\_{t}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t})\big),e,e^{0}\big)\Big)\,\Big|{\mathcal{}F}\_{t}^{0}\Big], |  |

where the last equality holds by definition of a~t\tilde{a}\_{t} given in ([7.3](https://arxiv.org/html/2511.04515v1#S7.E3 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) (which follows from the property of the Blackwell-Dubins function and the fact that ℒℙ¯ξ,πc​(ht​(ϑt))=U[0,1]\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(h\_{t}(\vartheta\_{t}))={\mathcal{}U}\_{[0,1]}; see Remark [2.19](https://arxiv.org/html/2511.04515v1#S2.Thmthm19 "Remark 2.19. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

Combining ([7.9](https://arxiv.org/html/2511.04515v1#S7.E9 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) with ([7.9](https://arxiv.org/html/2511.04515v1#S7.E9 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) and ([7.8](https://arxiv.org/html/2511.04515v1#S7.E8 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")), we hence have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ¯ξ,πc​[g^t+1​(ε1:t+10)​f^​(st+1ξ,πc,ℙ¯ξ,πc)]\displaystyle\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\big[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(s\_{t+1}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}})\big] | =𝔼ℙ¯ξ,πc[g^t+1(ε1:t+10)f^(F(s~t,a~t,(μ~t⊗^πtc(⋅|⋅,μ~t)),εt+1,εt+10))]\displaystyle=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\Big[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}\Big(\operatorname{F}\big(\tilde{s}\_{t},\tilde{a}\_{t},\big(\tilde{\mu}\_{t}\mathbin{\hat{\otimes}}\pi\_{t}^{c}(\cdot\,|\,\cdot,\tilde{\mu}\_{t})\big),\varepsilon\_{t+1},\varepsilon\_{t+1}^{0}\big)\Big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ¯ξ,πc​[g^t+1​(ε1:t+10)​f^​(s~t+1)]\displaystyle=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\big[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\hat{f}(\tilde{s}\_{t+1})\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ¯ξ,πc​[g^t+1​(ε1:t+10)​∫Sf^​(s)​ℒℙ¯ξ,πc​(s~t+1|ε1:t+10)​(d​s)],\displaystyle=\mathbb{E}^{\underline{\mathbb{P}}^{\xi,\pi^{c}}}\bigg[\hat{g}\_{t+1}(\varepsilon\_{1:t+1}^{0})\int\_{S}\hat{f}(s)\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\tilde{s}\_{t+1}|\varepsilon^{0}\_{1:t+1})(ds)\bigg], |  |

where the last line holds by definition of s~t+1\tilde{s}\_{t+1} given in ([7.3](https://arxiv.org/html/2511.04515v1#S7.E3 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")).

Moreover, since s~t+1\tilde{s}\_{t+1} is Gt+1{\mathcal{}G}\_{t+1} measurable, another application of Lemma [6.1](https://arxiv.org/html/2511.04515v1#S6.Thmthm1 "Lemma 6.1. ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty") ensures that

|  |  |  |
| --- | --- | --- |
|  | ℒℙ¯ξ,πc​(s~t+1|ε1:t+10)=μ~t+1,ℙ¯ξ,πc-a.s.,\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\tilde{s}\_{t+1}|\varepsilon^{0}\_{1:t+1})=\tilde{\mu}\_{t+1},\quad\mbox{$\underline{\mathbb{P}}^{\xi,\pi^{c}}$-a.s.}, |  |

which ensures ([7.7](https://arxiv.org/html/2511.04515v1#S7.E7 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) to hold, as claimed.

By the induction hypothesis, ([7.6](https://arxiv.org/html/2511.04515v1#S7.E6 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) holds for all t≥0t\geq 0.

Step 3: Recall that ℙ¯ξ,πc∈Q\underline{\mathbb{P}}^{\xi,\pi^{c}}\in{\mathcal{}Q} is the measure induced by (p¯tξ,πc)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,\pi^{c}})\_{t\geq 1}\in\mathcal{K}^{0} given in ([7.2](https://arxiv.org/html/2511.04515v1#S7.E2 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) and ([7.5](https://arxiv.org/html/2511.04515v1#S7.E5 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) (see Step 1). Then from Remark [2.3](https://arxiv.org/html/2511.04515v1#S2.Thmthm3 "Remark 2.3. ‣ 2.2. Propagation of chaos under common noise uncertainty ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (iii), it holds that ℙ¯ξ,a\underline{\mathbb{P}}^{\xi,a}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (7.11) |  | ℒℙ¯ξ,πc​(ε10)=p¯1ξ,πc∈𝔓0,ℒℙ¯ξ,πc(εt0|Ft−10)=p¯tξ,πc(⋅|ε1:t−10)∈𝔓0for all t≥2.\displaystyle\begin{aligned} &\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\varepsilon\_{1}^{0})=\underline{p}\_{1}^{\xi,\pi^{c}}\in\mathfrak{P}^{0},\\ \;\;&\mathscr{L}\_{\underline{\mathbb{P}}^{\xi,\pi^{c}}}(\varepsilon\_{t}^{0}|{\mathcal{}F}\_{t-1}^{0})=\underline{p}\_{t}^{\xi,\pi^{c}}(\cdot|\varepsilon\_{1:t-1}^{0})\in\mathfrak{P}^{0}\;\;\mbox{for all $t\geq 2$}.\end{aligned} |  |

Moreover, by ([7.6](https://arxiv.org/html/2511.04515v1#S7.E6 "In 7.2. Proof of Lemma 2.26 ‣ 7. Proof of results in Section 2.5 ‣ Robust mean-field control under common noise uncertainty")) in Step 2 and ([2.33](https://arxiv.org/html/2511.04515v1#S2.E33 "In Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Lemma [2.25](https://arxiv.org/html/2511.04515v1#S2.Thmthm25 "Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), it holds that ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (7.12) |  | p¯1ξ,πc=p¯∗(Λ¯0ξ,πc),p¯tξ,πc(⋅|ε1:t−10)=p¯∗(Λ¯t−1ξ,πc)for all t≥2,\displaystyle\underline{p}\_{1}^{\xi,\pi^{c}}=\overline{p}^{\*}(\underline{\Lambda}\_{0}^{\xi,\pi^{c}}),\qquad\underline{p}\_{t}^{\xi,\pi^{c}}(\cdot|\varepsilon\_{1:t-1}^{0})=\overline{p}^{\*}\big(\underline{\Lambda}\_{t-1}^{\xi,\pi^{c}}\big)\quad\mbox{for all $t\geq 2$}, |  |

which ensures ([2.35](https://arxiv.org/html/2511.04515v1#S2.E35 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) to hold, as claimed.

A direct consequence of ([2.34](https://arxiv.org/html/2511.04515v1#S2.E34 "In Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) ensures ([2.36](https://arxiv.org/html/2511.04515v1#S2.E36 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) to hold, as claimed. This completes the proof. ∎

### 7.3. Proof of Corollary [2.28](https://arxiv.org/html/2511.04515v1#S2.Thmthm28 "Corollary 2.28. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")

As the essential arguments of the proof closely follow those of Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), we provide the outline of the proof and omit some details here.

Step 1. For notational simplicity, set μ:=ℒ​(ξ)\mu:=\mathscr{L}(\xi). We first consider for every n∈ℕn\in\mathbb{N}

|  |  |  |
| --- | --- | --- |
|  | Inξ,πc,∗:=infℙ∈Q𝔼ℙ​[∑t=0n−1βt​r​(stξ,πc,∗,ℙ,atπc,∗,ℙ,Λtξ,πc,∗,ℙ)+βn​V¯∗​(μnξ,πc,∗,ℙ)],\displaystyle{\mathcal{}I}\_{n}^{\xi,\pi^{c,\*}}:=\inf\_{{\mathbb{P}}\in{\mathcal{}Q}}\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{n-1}\beta^{t}\,{r}(s\_{t}^{\xi,\pi^{c,\*},{\mathbb{P}}},a^{\pi^{c,\*},\mathbb{P}}\_{t},{\Lambda}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}})+\beta^{n}\,\overline{V}^{\*}({\mu}\_{n}^{\xi,\pi^{c,\*},\mathbb{P}})\bigg], |  |

where for each ℙ∈Q\mathbb{P}\in{\mathcal{}Q}, (μtξ,πc,∗,ℙ)t≥0({\mu}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}})\_{t\geq 0} and (Λtξ,πc,∗,ℙ)t≥0({\Lambda}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}})\_{t\geq 0} are given in ([2.32](https://arxiv.org/html/2511.04515v1#S2.E32 "In 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")).

Note that by ([2.33](https://arxiv.org/html/2511.04515v1#S2.E33 "In Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) in Lemma [2.25](https://arxiv.org/html/2511.04515v1#S2.Thmthm25 "Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") and definition of πtc,∗=πlocc,∗\pi^{c,\*}\_{t}=\pi\_{\operatorname{loc}}^{c,\*} given in ([2.37](https://arxiv.org/html/2511.04515v1#S2.E37 "In Corollary 2.28. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) together with the property ([2.38](https://arxiv.org/html/2511.04515v1#S2.E38 "In Corollary 2.28. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), it holds for every ℙ∈Q\mathbb{P}\in{\mathcal{}Q} that ℙ\mathbb{P}-a.s.,

|  |  |  |
| --- | --- | --- |
|  | π¯∗​(μtξ,πc,∗,ℙ)=Λtξ,πc,∗,ℙfor all t≥0.\overline{\pi}^{\*}({\mu}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}})={\Lambda}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}}\quad\mbox{for all $t\geq 0$.} |  |

From this, using the same arguments presented for ([6.25](https://arxiv.org/html/2511.04515v1#S6.E25 "In 6.3. Proof of Theorem 2.21 ‣ 6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")), we have that for every n∈ℕn\in\mathbb{N}

|  |  |  |
| --- | --- | --- |
|  | Inξ,πc,∗=infℙ∈Q𝔼ℙ​[∑t=0n−1βt​r¯​(μtξ,πc,∗,ℙ,Λtξ,πc,∗,ℙ)+βn​V¯∗​(μnξ,πc,∗,ℙ)].\displaystyle{\mathcal{}I}\_{n}^{\xi,\pi^{c,\*}}=\inf\_{{\mathbb{P}}\in{\mathcal{}Q}}\mathbb{E}^{{\mathbb{P}}}\bigg[\sum\_{t=0}^{n-1}\beta^{t}\,\overline{r}({\mu}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}}\,,\,{\Lambda}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}})+\beta^{n}\,\overline{V}^{\*}({\mu}\_{n}^{\xi,\pi^{c,\*},\mathbb{P}})\bigg]. |  |

Hence, from the representation of the Markov decision process of the lifted state process in ([2.34](https://arxiv.org/html/2511.04515v1#S2.E34 "In Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) (see Lemma [2.25](https://arxiv.org/html/2511.04515v1#S2.Thmthm25 "Lemma 2.25. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), we can use the same arguments presented for Steps 1 and 2 in the proof of Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (that relies on the local optimality of π¯∗​(μtξ,πc,∗,ℙ)\overline{\pi}^{\*}({\mu}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}}) to T​V¯∗​(μtξ,πc,∗,ℙ){\mathcal{}T}\overline{V}^{\*}({\mu}\_{t}^{\xi,\pi^{c,\*},\mathbb{P}}) in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (ii) and the fixed point theorem in Proposition [2.16](https://arxiv.org/html/2511.04515v1#S2.Thmthm16 "Proposition 2.16. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"); see Section [6](https://arxiv.org/html/2511.04515v1#S6 "6. Proof of results in Section 2.4 ‣ Robust mean-field control under common noise uncertainty")) to have

|  |  |  |
| --- | --- | --- |
|  | V¯∗​(μ)≤lim supn→∞Inξ,πc,∗≤Jπc,∗​(ξ)≤Vc​(ξ).\displaystyle\overline{V}^{\*}(\mu)\leq\limsup\_{n\to\infty}{\mathcal{}I}\_{n}^{\xi,\pi^{c,\*}}\leq{\mathcal{}J}^{\pi^{c,\*}}(\xi)\leq{V}^{c}(\xi). |  |

Step 2. For every πc∈Πc\pi^{c}\in\Pi^{c}, let ℙ¯ξ,πc∈Q\underline{\mathbb{P}}^{\xi,\pi^{c}}\in{\mathcal{}Q} be induced by some (p¯tξ,πc)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,\pi^{c}})\_{t\geq 1}\in\mathcal{K}^{0} satisfying ([2.26](https://arxiv.org/html/2511.04515v1#S2.E26 "In Lemma 2.17. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.35](https://arxiv.org/html/2511.04515v1#S2.E35 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) (see Lemma [2.26](https://arxiv.org/html/2511.04515v1#S2.Thmthm26 "Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Then define Vπc​(ξ){\mathcal{}V}^{\pi^{c}}(\xi) by

|  |  |  |
| --- | --- | --- |
|  | Vπc​(ξ):=𝔼ℙ¯ξ,πc​[∑t=0∞βt​r​(stξ,πc,ℙ¯ξ,πc,atπc,ℙ¯ξ,πc,Λ¯tξ,πc)]=𝔼ℙ¯ξ,πc​[∑t=0∞βt​r¯​(pjS⁡(Λ¯tξ,πc),Λ¯tξ,πc)],\displaystyle{{\mathcal{}V}}^{\pi^{c}}(\xi):=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,\pi^{c}}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}r(s\_{t}^{\xi,\pi^{c},\underline{\mathbb{P}}{}^{\xi,\pi^{c}}},a^{\pi^{c},\underline{\mathbb{P}}{}^{\xi,\pi^{c}}}\_{t},\underline{\Lambda}\_{t}^{\xi,\pi^{c}})\bigg]=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,\pi^{c}}}\bigg[\sum\_{t=0}^{\infty}\beta^{t}\;\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,\pi^{c}}),\underline{\Lambda}\_{t}^{\xi,\pi^{c}}\big)\bigg], |  |

where Λ¯tξ,πc\underline{\Lambda}\_{t}^{\xi,\pi^{c}} is the conditional joint law of (stξ,πc,ℙ¯ξ,πc,atπc,ℙ)(s\_{t}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}},a^{\pi^{c},\mathbb{P}}\_{t}) under ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}} given ε1:t0\varepsilon^{0}\_{1:t}.

By the local optimality of p¯∗​(Λ¯tξ,πc)\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,\pi^{c}}) to T​V¯∗​(pjS⁡(Λ¯tξ,πc)){\mathcal{}T}\overline{V}^{\*}(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,\pi^{c}})) (see Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") (i)), we can use the same arguments presented for Step 3 in the proof of Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty") to have

|  |  |  |
| --- | --- | --- |
|  | Vc​(ξ)≤supπc∈ΠcVπc​(ξ)≤supπc∈Πc∑t=0∞(βt​𝔼ℙ¯ξ,πc​[V¯∗​(μ¯tξ,πc)]−βt+1​𝔼ℙ¯ξ,πc​[V¯∗​(μ¯t+1ξ,πc)])=V¯∗​(μ),V^{c}(\xi)\leq\sup\_{\pi^{c}\in\Pi^{c}}{\mathcal{}V}^{\pi^{c}}(\xi)\leq\sup\_{\pi^{c}\in\Pi^{c}}\sum\_{t=0}^{\infty}\Big(\beta^{t}\,\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,\pi^{c}}}[\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,\pi^{c}})]-\beta^{t+1}\,\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,\pi^{c}}}[\overline{V}^{\*}(\underline{\mu}\_{t+1}^{\xi,\pi^{c}})]\Big)=\overline{V}^{\*}(\mu), |  |

where μ¯tξ,πc\underline{\mu}\_{t}^{\xi,\pi^{c}} is the conditional law of stξ,πc,ℙ¯ξ,πcs\_{t}^{\xi,\pi^{c},\underline{\mathbb{P}}^{\xi,\pi^{c}}} under ℙ¯ξ,πc\underline{\mathbb{P}}^{\xi,\pi^{c}} given ε1:t0\varepsilon^{0}\_{1:t}.

Therefore, we have obtained that V¯∗​(μ)=Vc​(ξ)\overline{V}^{\*}(\mu)=V^{c}(\xi), as claimed. In fact, V¯∗​(μ)=V​(ξ)\overline{V}^{\*}(\mu)=V(\xi) follows from Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"). Hence the statement (i) holds.

Step 3. Lastly, we consider ℙ¯ξ,πc,∗∈Q\underline{\mathbb{P}}^{\xi,\pi^{c,\*}}\in{\mathcal{}Q} which is induced by (p¯tξ,πc,∗)t≥1∈𝒦0(\underline{p}\_{t}^{\xi,\pi^{c,\*}})\_{t\geq 1}\in\mathcal{K}^{0} satisfying ([2.35](https://arxiv.org/html/2511.04515v1#S2.E35 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) and ([2.36](https://arxiv.org/html/2511.04515v1#S2.E36 "In Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) (see Lemma [2.26](https://arxiv.org/html/2511.04515v1#S2.Thmthm26 "Lemma 2.26. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")). Then
by definition of πc,∗\pi^{c,\*} and of ℙ¯ξ,πc,∗\underline{\mathbb{P}}^{\xi,\pi^{c,\*}} (noting that both satisfy the local optimality given in Proposition [2.15](https://arxiv.org/html/2511.04515v1#S2.Thmthm15 "Proposition 2.15. ‣ 2.3. Lifted robust Markov decision processes on the space of probability measures ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")), it holds that for every t≥0t\geq 0

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ¯ξ,πc,∗​[V¯∗​(μ¯tξ,πc,∗)]=𝔼ℙ¯ξ,πc,∗​[T​V¯∗​(μ¯tξ,πc,∗)]\displaystyle\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,\pi^{c,\*}}}[\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,\pi^{c,\*}})]=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,\pi^{c,\*}}}[{\mathcal{}T}\overline{V}^{\*}(\underline{\mu}\_{t}^{\xi,\pi^{c,\*}})] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼ℙ¯ξ,πc,∗​[r¯​(pjS⁡(Λ¯tξ,πc,∗),Λ¯tξ,πc,∗)+β​∫P​(S)V¯∗​(μ~′)​p¯​(d​μ~′|pjS⁡(Λ¯tξ,πc,∗),Λ¯tξ,πc,∗,p¯∗​(Λ¯tξ,πc,∗))].\displaystyle\hskip 20.00003pt=\mathbb{E}^{\underline{\mathbb{P}}{}^{\xi,\pi^{c,\*}}}\bigg[\overline{r}\big(\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,\pi^{c,\*}}),\underline{\Lambda}\_{t}^{\xi,\pi^{c,\*}}\big)+\beta\int\_{{\mathcal{}P}(S)}\overline{V}^{\*}(\tilde{\mu}^{\prime})\overline{p}\big(d\tilde{\mu}^{\prime}|\operatorname{pj}\_{S}(\underline{\Lambda}\_{t}^{\xi,\pi^{c,\*}}),\underline{\Lambda}\_{t}^{\xi,\pi^{c,\*}},\overline{p}^{\*}(\underline{\Lambda}\_{t}^{\xi,\pi^{c,\*}})\big)\bigg]. |  |

Hence by using the same arguments presented for Step 4 of the proof of Theorem [2.21](https://arxiv.org/html/2511.04515v1#S2.Thmthm21 "Theorem 2.21. ‣ 2.4. Verification theorem ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty"), we deduce that ([2.39](https://arxiv.org/html/2511.04515v1#S2.E39 "In item (ii) ‣ Corollary 2.28. ‣ 2.5. Connection with a closed-loop Markov policy framework ‣ 2. Main results ‣ Robust mean-field control under common noise uncertainty")) holds. This completes the proof. ∎

## Appendix A Supplementary statements

Let us provide some elementary observations on conditional laws.

###### Lemma A.1.

Fix a probability space (Ω~,F~,ℙ~)(\tilde{\Omega},\tilde{\mathcal{}F},\tilde{\mathbb{P}}). Let XX be Borel space and YY be measurable space. For every random elements X{\mathcal{}X} and Y{\mathcal{}Y} with values in XX and YY, respectively, the following hold:

1. (i)

   There exists a kernel kX|Y:Y∋y↦kX|Y​(d​x|y)∈P​(X)k^{{\mathcal{}X}|{\mathcal{}Y}}:Y\ni y\mapsto k^{{\mathcal{}X}|{\mathcal{}Y}}(dx|y)\in{\mathcal{}P}(X) such that for every B∈B​(X)B\in{\mathcal{}B}(X), ℙ~​(X∈B|Y)=kX|Y​(B|Y)\tilde{\mathbb{P}}({\mathcal{}X}\in B|{\mathcal{}Y})=k^{{\mathcal{}X}|{\mathcal{}Y}}(B|{\mathcal{}Y}) ℙ~\tilde{\mathbb{P}}-a.s., and kX|Yk^{{\mathcal{}X}|{\mathcal{}Y}} is unique ℒℙ~​(Y)\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}Y})-a.e.. As a consequence, kX|Y(⋅|Y)k^{{\mathcal{}X}|{\mathcal{}Y}}(\cdot\,|\,{\mathcal{}Y}) is σ​(Y)\sigma({\mathcal{}Y}) measurable and we denote for every ω~∈Ω~\tilde{\omega}\in\tilde{\Omega}

   |  |  |  |
   | --- | --- | --- |
   |  | ℒℙ~(X|Y)(ω~):=kX|Y(⋅|Y)(ω~),\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}X}|{\mathcal{}Y})(\tilde{\omega}):=k^{{\mathcal{}X}|{\mathcal{}Y}}(\cdot|{\mathcal{}Y})(\tilde{\omega}), |  |

   i.e., a conditional law of X{\mathcal{}X} given Y{\mathcal{}Y}; see, e.g., [kallenberg2002foundations, Section 6, p.106–107].
2. (ii)

   If X{\mathcal{}X} is given by X=φ​(Y,Z){\mathcal{}X}=\varphi({\mathcal{}Y},{\mathcal{}Z}), where φ:Y×Z→X\varphi:Y\times Z\to X is a measurable function and Z{\mathcal{}Z} is a random element in ZZ and independent of Y{\mathcal{}Y}, then ℒℙ~​(X|Y)=ℒℙ~​(φ​(y,Z))|y=Y\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}X}|{\mathcal{}Y})=\mathscr{L}\_{\tilde{\mathbb{P}}}(\varphi(y,{\mathcal{}Z}))|\_{y={\mathcal{}Y}} and ℒℙ~​(X|Y)\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}X}|{\mathcal{}Y}) is σ​(Y)\sigma({\mathcal{}Y}) measurable.

###### Proof.

Part (i) is shown in [kallenberg2002foundations, Theorem 6.3]. We proceed to prove (ii), which is a consequence of (i) with an application of Fubini’s theorem. Clearly, it is sufficient to show that for any bounded measurable function g:Y→ℝg:Y\to\mathbb{R} and bounded Borel measurable function f:X→ℝf:X\to\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ~​[g​(Y)​∫Xf​(x′)​ℒℙ~​(X|Y)​(d​x′)]=𝔼ℙ~​[g​(Y)​∫Xf​(x′)​ℒℙ~​(φ​(y,Z))|y=Y​(d​x′)].\displaystyle\mathbb{E}^{\tilde{\mathbb{P}}}\bigg[g({\mathcal{}Y})\int\_{X}f(x^{\prime})\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}X}|{\mathcal{}Y})(dx^{\prime})\bigg]=\mathbb{E}^{\tilde{\mathbb{P}}}\bigg[g({\mathcal{}Y})\int\_{X}f(x^{\prime})\mathscr{L}\_{\tilde{\mathbb{P}}}(\varphi(y,{\mathcal{}Z}))|\_{y={\mathcal{}Y}}(dx^{\prime})\bigg]. |  |

Indeed, by definition of the conditional law ℒℙ~​(X|Y)\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}X}|{\mathcal{}Y}) (given in (i)) it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ~[g(Y)∫Xf(x′)ℒℙ~(X|Y)(dx′)]=𝔼ℙ~[g(Y)𝔼ℙ~[f(X)|Y]]=𝔼ℙ~[g(Y)f(X)]=:I,\mathbb{E}^{\tilde{\mathbb{P}}}\bigg[g({\mathcal{}Y})\int\_{X}f(x^{\prime})\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}X}|{\mathcal{}Y})(dx^{\prime})\bigg]=\mathbb{E}^{\tilde{\mathbb{P}}}\big[g({\mathcal{}Y})\mathbb{E}^{\tilde{\mathbb{P}}}[f({\mathcal{}X})|{\mathcal{}Y}]\big]=\mathbb{E}^{\tilde{\mathbb{P}}}[g({\mathcal{}Y})f({\mathcal{}X})]=:\operatorname{I}, |  |

where the second equality follows from the σ​(Y)\sigma({\mathcal{}Y})-measurability of g​(Y)g({\mathcal{}Y}) and the tower property.

Moreover since X=φ​(Y,Z){\mathcal{}X}=\varphi({\mathcal{}Y},{\mathcal{}Z}), and Y{\mathcal{}Y} and Z{\mathcal{}Z} are independent,

|  |  |  |  |
| --- | --- | --- | --- |
|  | I=𝔼ℙ~​[g​(Y)​𝔼ℙ~​[f​(φ​(Y,Z))|Y]]\displaystyle\operatorname{I}=\mathbb{E}^{\tilde{\mathbb{P}}}\Big[g({\mathcal{}Y})\mathbb{E}^{\tilde{\mathbb{P}}}\big[f(\varphi({\mathcal{}Y},{\mathcal{}Z}))|{\mathcal{}Y}\big]\Big] | =∫Yg​(y)​𝔼ℙ~​[f​(φ​(y,Z))]​ℒℙ~​(Y)​(d​y)\displaystyle=\int\_{Y}g(y)\mathbb{E}^{\tilde{\mathbb{P}}}\Big[f(\varphi(y,{\mathcal{}Z}))\Big]\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}Y})(dy) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Yg​(y)​𝔼ℙ~​[∫Xf​(x′)​ℒℙ~​(φ​(y,Z))​(d​x′)]​ℒℙ~​(Y)​(d​y)\displaystyle=\int\_{Y}g(y)\mathbb{E}^{\tilde{\mathbb{P}}}\bigg[\int\_{X}f(x^{\prime})\mathscr{L}\_{\tilde{\mathbb{P}}}(\varphi(y,{\mathcal{}Z}))(dx^{\prime})\bigg]\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}Y})(dy) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ~​[g​(Y)​∫Xf​(x′)​ℒℙ~​(φ​(y,Z))|y=Y​(d​x′)],\displaystyle=\mathbb{E}^{\tilde{\mathbb{P}}}\bigg[g({\mathcal{}Y})\int\_{X}f(x^{\prime})\mathscr{L}\_{\tilde{\mathbb{P}}}(\varphi(y,{\mathcal{}Z}))|\_{y={\mathcal{}Y}}(dx^{\prime})\bigg], |  |

where the second equality follows from definition of ℒℙ~​(φ​(y,Z))\mathscr{L}\_{\tilde{\mathbb{P}}}(\varphi(y,{\mathcal{}Z})) and the last one follows from Fubini’s theorem (since both ff and gg are bounded). The σ​(Y)\sigma({\mathcal{}Y})-measurability of ℒℙ~​(X|Y)\mathscr{L}\_{\tilde{\mathbb{P}}}({\mathcal{}X}|{\mathcal{}Y}) follows from (i). This concludes the proof.
∎

###### Lemma A.2 (Blackwell and Dubins [blackwell1983extension]).

For any Polish space XX, there exists a Borel measurable function ρX:P​(X)×[0,1]→X\rho\_{X}:{\mathcal{}P}(X)\times[0,1]\to X satisfying the following conditions:

* (i)

  for every λ∈P​(X)\lambda\in{\mathcal{}P}(X) and every uniform random variable U∼U[0,1]U\sim{\mathcal{}U}\_{[0,1]}, ρX​(λ,U)\rho\_{X}(\lambda,U) is distributed according to λ\lambda;
* (ii)

  for almost every uu, the map λ↦ρX​(λ,u)\lambda\mapsto\rho\_{X}(\lambda,u) is continuous w.r.t. the weak topology of P​(X){\mathcal{}P}(X).

We call ρX\rho\_{X} the Blackwell–Dubins function of the space XX.

###### Lemma A.3 (Universal disintegration; see, e.g., [kallenberg2017random, Corollarly 1.26]).

For any Borel spaces XX and YY, there exists a kernel KX×Y:X×P(X×Y)×P(X)∋(x,λ,η)↦KX×Y(⋅|x,λ,η)∈P(Y){\mathcal{}K}\_{X\times Y}:X\times{\mathcal{}P}(X\times Y)\times{\mathcal{}P}(X)\ni(x,\lambda,\eta)\mapsto{\mathcal{}K}\_{X\times Y}(\cdot|x,\lambda,\eta)\in{\mathcal{}P}(Y)
such that for every λ∈P​(X×Y)\lambda\in{\mathcal{}P}(X\times Y) and η∈P​(X)\eta\in{\mathcal{}P}(X) satisfying pjX⁡(λ)≪η\operatorname{pj}\_{X}(\lambda)\ll\eta, it holds that

|  |  |  |
| --- | --- | --- |
|  | λ=η⊗^KX×Y(⋅|⋅,λ,η),\lambda=\eta\mathbin{\hat{\otimes}}{\mathcal{}K}\_{X\times Y}(\,\cdot\,|\,\cdot,\lambda,\eta), |  |

Moreover, KX×Y(⋅|,⋅,λ,η){\mathcal{}K}\_{X\times Y}(\,\cdot\,|,\cdot,\lambda,\eta) is unique η\eta-a.e. for fixed λ\lambda and η\eta.