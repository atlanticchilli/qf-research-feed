---
authors:
- Hanqing Jin
- Renyuan Xu
- Yanzhao Yang
doc_id: arxiv:2512.14991v1
family_id: arxiv:2512.14991
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes
url_abs: http://arxiv.org/abs/2512.14991v1
url_html: https://arxiv.org/html/2512.14991v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hanqing Jin
Mathematical Institute, University of Oxford. Email: hanqing.jin@spc.ox.ac.uk and yanzhao.yang@merton.ox.ac.uk .
  
Renyuan Xu
Department of Management Science and Engineering, Stanford University. R.X. is supported in part by the NSF CAREER Award DMS-2524465 and a gift fund from Point72. Email: renyuanxu@stanford.edu
  
Yanzhao Yang 11footnotemark: 1

(December 17, 2025)

###### Abstract

We study reinforcement learning for controlled diffusion processes with unbounded continuous state spaces, bounded continuous actions, and polynomially growing rewards—settings that arise naturally in finance, economics, and operations research. To overcome the challenges of continuous and high-dimensional domains, we introduce a model-based algorithm that adaptively partitions the joint state–action space. The algorithm maintains estimators of drift, volatility, and rewards within each partition, refining the discretization whenever estimation bias exceeds statistical confidence. This adaptive scheme balances exploration and approximation, enabling efficient learning in unbounded domains. Our analysis establishes regret bounds that depend on the problem horizon, state dimension, reward growth order, and a newly defined notion of zooming dimension tailored to unbounded diffusion processes. The bounds recover existing results for bounded settings as a special case, while extending theoretical guarantees to a broader class of diffusion-type problems. Finally, we validate the effectiveness of our approach through numerical experiments, including applications to high-dimensional problems such as multi-asset mean-variance portfolio selection.

## 1 Introduction

Data-driven decision-making has emerged as a foundational paradigm in modern scientific and engineering disciplines, enabling systems to adapt and optimize behavior in complex, uncertain environments by learning from empirical evidence. In particular, reinforcement learning (RL) formalizes sequential decision-making under uncertainty as a mathematical framework involving agents interacting with unknown environments to maximize long-term cumulative reward. Applications range from robotics (Kober et al., [2013](https://arxiv.org/html/2512.14991v1#bib.bib42); Zhao et al., [2020](https://arxiv.org/html/2512.14991v1#bib.bib66)) and autonomous systems (Kiran et al., [2021](https://arxiv.org/html/2512.14991v1#bib.bib39); Shalev-Shwartz et al., [2016](https://arxiv.org/html/2512.14991v1#bib.bib52)) to finance (Hambly et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib27)) and healthcare (Yu et al., [2021](https://arxiv.org/html/2512.14991v1#bib.bib64)), especially in settings where traditional model-based methods may fail due to restrictive structural assumptions or limited flexibility.

The literature on RL theory has progressed through a structured hierarchy of assumptions on state–action spaces, beginning with finite (tabular) settings and extending toward infinite states/actions or continuous domains. Earlier seminal works focused on tabular MDPs with finite state-action spaces, where convergence and sample efficiency of model-free algorithms, such as Q-learning, are studied under exact representations (Auer et al., [2008](https://arxiv.org/html/2512.14991v1#bib.bib2); Dayan and Watkins, [1992](https://arxiv.org/html/2512.14991v1#bib.bib16); Jaakkola et al., [1993](https://arxiv.org/html/2512.14991v1#bib.bib32); Kakade, [2003](https://arxiv.org/html/2512.14991v1#bib.bib36)). These settings allow for strong performance guarantees using regret and PAC frameworks (Azar et al., [2017](https://arxiv.org/html/2512.14991v1#bib.bib3); Dann et al., [2017](https://arxiv.org/html/2512.14991v1#bib.bib15)). As attention shifted to large or continuous state spaces, linear function approximation has been introduced, preserving tractability while enabling generalization (Tsitsiklis and Van Roy, [1996](https://arxiv.org/html/2512.14991v1#bib.bib57); Bertsekas and Tsitsiklis, [1996](https://arxiv.org/html/2512.14991v1#bib.bib6); Lazaric et al., [2012](https://arxiv.org/html/2512.14991v1#bib.bib43)). These frameworks often retain finite action spaces and require bounded features or realizability assumptions. More recent work explores continuous or unbounded state spaces using either nonparametric techniques (e.g., nearest-neighbor methods (Jin et al., [2020](https://arxiv.org/html/2512.14991v1#bib.bib35))) or neural network approximations (Fan et al., [2020](https://arxiv.org/html/2512.14991v1#bib.bib21); Fu et al., [2020](https://arxiv.org/html/2512.14991v1#bib.bib23); Wang et al., [2019](https://arxiv.org/html/2512.14991v1#bib.bib61)), though theoretical guarantees remain limited in the latter (in terms of the choice of network architectures). Finite action spaces remain the standard setting in theoretical RL studies, largely due to the combinatorial challenges posed by continuous action spaces, namely the interrelated difficulties in optimization, exploration, and representation. Only a few exceptions exist, such as studies focusing on problems with special structure (e.g., linear-quadratic regulators (Fazel et al., [2018](https://arxiv.org/html/2512.14991v1#bib.bib22); Hambly et al., [2021](https://arxiv.org/html/2512.14991v1#bib.bib26); Guo et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib25))) or those exploring discretization-based nonparametric methods, which include both uniform partitioning (Bayraktar and Kara, [2023](https://arxiv.org/html/2512.14991v1#bib.bib4); Kara and Yuksel, [2023](https://arxiv.org/html/2512.14991v1#bib.bib38)) and adaptive partitioning approaches (Dong et al., [2019](https://arxiv.org/html/2512.14991v1#bib.bib18); Pazis and Parr, [2013](https://arxiv.org/html/2512.14991v1#bib.bib49); Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)). This progression of the theoretical RL literature reflects a trade-off between tractability and expressive power: tabular and linearly parameterized settings are more tractable for analysis, whereas generic continuous state–action spaces, though more general and practically important, remain less understood and less theoretically developed due to their complexity.

Many critical decision-making problems in finance, economics, and operations research involve unbounded, continuous state spaces, as well as continuous (often high-dimensional) action spaces, and unbounded reward functions. A central class of such problems arises in portfolio optimization, where agents take continuous actions by dynamically adjusting their wealth allocations across risky assets in response to evolving market conditions. These problems typically involve an unbounded and continuous state space, representing asset prices and wealth levels, and often feature unbounded reward (utility functions) subject to suitable growth conditions (Black and Litterman, [1992](https://arxiv.org/html/2512.14991v1#bib.bib9); Zhou and Li, [2000](https://arxiv.org/html/2512.14991v1#bib.bib67); He et al., [2015](https://arxiv.org/html/2512.14991v1#bib.bib29)). Optimal execution and intraday trading problems are often formulated within a continuous state-action framework, as traders must balance market impact, adverse selection risk, and order flow dynamics in a tractable manner (Almgren and Chriss, [2001](https://arxiv.org/html/2512.14991v1#bib.bib1); Cartea et al., [2015](https://arxiv.org/html/2512.14991v1#bib.bib13)). In dynamic hedging, particularly in incomplete markets or under stochastic volatility, agents must continuously adjust their positions to manage risk exposure (Carr et al., [2001](https://arxiv.org/html/2512.14991v1#bib.bib12); Duffie et al., [1997](https://arxiv.org/html/2512.14991v1#bib.bib20)). Credit risk and asset-liability management problems faced by banks, insurers, and pension funds also fall within this framework, as they involve dynamic decision-making under uncertainty, often with evolving and potentially unbounded risk profiles (Tektas et al., [2005](https://arxiv.org/html/2512.14991v1#bib.bib56)). At a broader scale, macro-financial decisions (such as sovereign debt issuance and monetary policy under uncertainty) rely on models with unbounded, continuous spaces to capture long-term dynamics and structural risks (Blommestein and Turner, [2012](https://arxiv.org/html/2512.14991v1#bib.bib10); Du et al., [2020](https://arxiv.org/html/2512.14991v1#bib.bib19)).
Despite their importance, such settings remain less understood in the RL literature, particularly regarding algorithmic development and theoretical guarantees.

Motivated by these challenges, this work seeks to address the following open question:

* Can we design an adaptive partition scheme tailored to (unknown) high-dimensional diffusion processes and simultaneously learn the optimal policy efficiently within the RL framework?

### 1.1 Our work and contributions

We investigate the above-mentioned open question in a setting governed by diffusion-type dynamics over a finite time horizon, with an unbounded state space and a continuous action space. To facilitate learning, we consider a discrete-time Markov decision process (MDP) with Gaussian increments, serving as an approximation of continuous-time diffusion processes. Crucially, we allow the expected reward to exhibit polynomial growth, going beyond the standard bounded reward assumptions, which enables our framework to capture a broader class of real-world applications.

To address the challenges of unbounded state space, we localize the state space by restricting the learning to a bounded ball, whose radius is carefully chosen to control the ultimate regret. The learning algorithm operates in an episodic setting. Throughout the learning process, we maintain representative estimators of both the drift and volatility within each partition of the joint state-action space. These partitions are refined adaptively: when the estimated bias exceeds the statistical confidence of the representative estimators, the partition is subdivided. Using the estimated drift and volatility, we construct a Q-function and select actions based on the upper confidence bound of this function. Mathematically, we show that the proposed algorithm achieves a regret of order 𝒪~​(H​K1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4))\tilde{\mathcal{O}}({H}K^{1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}}), with HH the horizon of the problem, KK the number of episodes, pp the highest bounded moments for the initial state distribution, m+1m+1 the order of reward polynomial growth, d𝒮d\_{\mathcal{S}} the dimension of state space and zmax,cz\_{\max,c} the worst-case zooming dimension over the entire horizon. Here, the zooming dimension quantifies problem benignness, with zmax,cz\_{\max,c} often much smaller than the joint state-action space dimension d𝒜+d𝒮d\_{\mathcal{A}}+d\_{\mathcal{S}} for benign instances (Kleinberg et al., [2019](https://arxiv.org/html/2512.14991v1#bib.bib41)).
The idea of adaptive partitioning is largely inspired by (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)), which considers a markedly different setting—namely, an MDP with a bounded state space and bounded rewards. Nevertheless, as pp tends to infinity, our regret order asymptotically approaches 𝒪~​(H​Kzmax,c+1zmax,c+2)\tilde{\mathcal{O}}({H}K^{\frac{z\_{\max,c}+1}{z\_{\max,c}+2}}), which is consistent with the order established in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) in terms of the episodes number KK, despite the substantial differences in both the problem setting and the underlying technical analysis.

From a technical perspective, a key challenge lies in defining an appropriate notion of zooming dimension which affects the algorithm design and hyperparameter set-up. Unlike the classical zooming dimension defined for bounded state-action spaces, our setting requires a new formulation suited to unbounded state spaces, one that can be meaningfully linked to the regret analysis (see Definition [5.15](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem15 "Definition 5.15 (Zooming dimension and maximum zooming dimension). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and the proof of Lemma [5.17](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem17 "Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). Furthermore, as we aim to analyze regret in diffusion-type settings, our approach differs from that of (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)), which characterizes the concentration of Markov transition kernels. Instead, we fully leverage the structure of the dynamics and derive concentration inequalities for the drift and volatility terms (see the proof of Theorem [4.4](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). In particular, deriving concentration inequalities for covariance matrices under only Lipschitz regularity of the volatility is challenging. To address this, we introduce and carefully analyze two intermediate terms (see ([4.2](https://arxiv.org/html/2512.14991v1#S4.E2 "In 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))). Moreover, to accommodate practical applications, we allow general reward functions with polynomial growth. This introduces additional challenges in estimator construction when the domain is unbounded (see ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))–([5.14](https://arxiv.org/html/2512.14991v1#S5.E14 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the proof of Theorem [5.3](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem3 "Theorem 5.3. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). Finally, our regret analysis must also accommodate martingale difference terms that are unbounded, requiring concentration tools more sophisticated than the standard Azuma–Hoeffding inequality (see the proof of Theorem [5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

### 1.2 Closely related literature

##### Uniform partition and adaptive partition.

Uniform partitioning or discretization is a straightforward nonparametric approach for continuous-state problems (Bayraktar and Kara, [2023](https://arxiv.org/html/2512.14991v1#bib.bib4); Kara and Yuksel, [2023](https://arxiv.org/html/2512.14991v1#bib.bib38)). However, these methods may suffer from the curse of dimensionality: fine grids are computationally intensive, whereas coarse grids produce inaccurate results and numerical instability (Zhang and Suen, [2025](https://arxiv.org/html/2512.14991v1#bib.bib65)), limiting their effectiveness in higher dimensions. For example, value iteration has a per-iteration complexity of 𝒪​(|𝒮|2​|𝒜|)\mathcal{O}(|\mathcal{S}|^{2}|\mathcal{A}|), and policy iteration requires 𝒪​(|𝒮|3+|𝒮|2​|𝒜|)\mathcal{O}(|\mathcal{S}|^{3}+|\mathcal{S}|^{2}|\mathcal{A}|) per iteration (Puterman, [2014](https://arxiv.org/html/2512.14991v1#bib.bib50)), with |𝒮||\mathcal{S}| and |𝒜||\mathcal{A}| denoting the size of discretized state and action spaces respectively. Moreover, uniform schemes are often suboptimal due to heterogeneous state visit frequencies—leading to wasted resolution on rarely visited states and insufficient resolution where it matters most. The challenge intensifies in unbounded state spaces, such as those arising in diffusion processes with applications in finance, physics, and engineering. In these settings, discretization typically requires domain truncation, which introduces bias, while extending grids to the full space is computationally prohibitive. Scalable and principled methods for such domains remain largely unresolved.

Adaptive partition in RL addresses the inefficiency of uniform grids by refining the state-action spaces only where needed. Early methods, such as U-Tree (McCallum, [1996](https://arxiv.org/html/2512.14991v1#bib.bib44)) and variable-resolution discretization (Munos and Moore, [2002](https://arxiv.org/html/2512.14991v1#bib.bib45)), focused on adaptively partitioning the state space based on visitation frequency or value approximation error. Subsequent works incorporated function approximation and confidence bounds to guide refinement more systematically (Strehl and Littman, [2006](https://arxiv.org/html/2512.14991v1#bib.bib55); Munos and Szepesvári, [2008](https://arxiv.org/html/2512.14991v1#bib.bib46); Ortner et al., [2014](https://arxiv.org/html/2512.14991v1#bib.bib48)). While some algorithms extend adaptivity to continuous action spaces under smoothness assumptions (Pazis and Parr, [2013](https://arxiv.org/html/2512.14991v1#bib.bib49); Dong et al., [2019](https://arxiv.org/html/2512.14991v1#bib.bib18)), jointly handling continuous, high-dimensional state-action spaces, especially under complex dynamics, remains a major challenge. A notable recent exception is (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)), which proposes an adaptive partitioning method for MDPs with bounded, continuous state-action spaces.

##### Zooming algorithms.

The use of zooming algorithms for adaptive partitioning was initially developed in the contextual multi-armed bandits (MAB) literature, particularly for problems with Lipschitz structure. (Kleinberg et al., [2008](https://arxiv.org/html/2512.14991v1#bib.bib40)) introduced a zooming algorithm for adaptive exploration and defined the zooming dimension to quantify the complexity of such problems. Building on this, (Slivkins, [2011](https://arxiv.org/html/2512.14991v1#bib.bib54)) extended the approach to contextual bandits, proposing a zooming algorithm for adaptive partitioning of the context-action space and analyzing its regret.

These ideas were later generalized to RL by (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)), who studied adaptive partition in finite-horizon RL with bounded state-action spaces, assuming a bounded reward function. They proposed both model-free and model-based algorithms and provided unified regret bounds. The model-free variant achieves a regret of order 𝒪~​(H52​Kzmax,c′+1zmax,c′+2)\tilde{\mathcal{O}}\Big(H^{\frac{5}{2}}K^{\frac{{z^{\prime}\_{\max,c}}+1}{{z^{\prime}\_{\max,c}}+2}}\Big), while the model-based variant achieves 𝒪~​(H52​Kzmax,c′+d𝒮−1zmax,c′+d𝒮)\tilde{\mathcal{O}}\Big(H^{\frac{5}{2}}K^{\frac{{z^{\prime}\_{\max,c}}+d\_{\mathcal{S}}-1}{{z^{\prime}\_{\max,c}}+d\_{\mathcal{S}}}}\Big) when d𝒮>2d\_{\mathcal{S}}>2 and 𝒪~​(H52​Kzmax,c′+1zmax,c′+2)\tilde{\mathcal{O}}\Big(H^{\frac{5}{2}}K^{\frac{{z^{\prime}\_{\max,c}}+1}{{z^{\prime}\_{\max,c}}+2}}\Big) when d𝒮≤2d\_{\mathcal{S}}\leq 2, where zmax,c′z^{\prime}\_{\max,c} denotes the worst-case zooming dimension under bounded state assumptions. These algorithms inspire the design of our framework, though our setting departs from theirs in several important ways.
More recently, (Kar and Singh, [2024](https://arxiv.org/html/2512.14991v1#bib.bib37)) proposed adaptive partitioning algorithms for non-episodic RL with infinite time horizons, under an ergodicity assumption. Their model-based algorithm attains a regret bound of order 𝒪~​(T1−12​d𝒮+z+3)\tilde{\mathcal{O}}\left(T^{1-\frac{1}{2d\_{\mathcal{S}}+z+3}}\right), where TT denotes the total number of decision steps, d𝒮d\_{\mathcal{S}} is the dimension of the state space, and zz is the zooming dimension tailored to their setting.

##### Continuous-time RL under diffusion processes.

As our study concerns diffusion-type dynamics in discrete time, it naturally relates to the literature on RL with system dynamics governed by continuous-time diffusion processes. Recent contributions in this area, such as (Wang et al., [2020](https://arxiv.org/html/2512.14991v1#bib.bib60); Jia and Zhou, [2023](https://arxiv.org/html/2512.14991v1#bib.bib34); Dai et al., [2025](https://arxiv.org/html/2512.14991v1#bib.bib14); Jia and Zhou, [2022](https://arxiv.org/html/2512.14991v1#bib.bib33); Huang et al., [2025](https://arxiv.org/html/2512.14991v1#bib.bib31); Han et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib28)), provide elegant mathematical frameworks and demonstrate substantial algorithmic progress. At the same time, aspects such as sample complexity or regret guarantees at the implementation level—particularly in terms of the number of observations collected from the environment—are typically not the primary focus of these works. In addition, theoretical treatments of unbounded state–action spaces and of implementable sampling schemes for general (non-Gaussian) policies over such spaces remain relatively limited. Addressing these issues constitutes one of the main focuses of our work.

This paper is organized as follows. Section [2](https://arxiv.org/html/2512.14991v1#S2 "2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") introduces the mathematical formulation of the problem, and Section [3](https://arxiv.org/html/2512.14991v1#S3 "3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") presents the design of our algorithm. We then turn to the technical developments: Section [4](https://arxiv.org/html/2512.14991v1#S4 "4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") establishes concentration inequalities for the estimators used in the algorithm, while Section [5](https://arxiv.org/html/2512.14991v1#S5 "5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") provides the regret analysis. Finally, Section [6](https://arxiv.org/html/2512.14991v1#S6 "6 Numerical experiments ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") evaluates the algorithm’s performance through some numerical experiments.

## 2 Mathematical set-up

To facilitate learning and implementation, we consider a discrete-time Markov decision process (MDP) with Gaussian increments fully characterized by (ℝd𝒮,𝒜,H,μ,σ)(\mathbb{R}^{d\_{\mathcal{S}}},\mathcal{A},H,\mu,\sigma), serving as an approximation of continuous-time diffusion processes. Here HH is the number of timestamps indexed in each episode, with [H]={1,2,⋯,H}[H]=\{1,2,\cdots,H\}. In addition, ℝd𝒮\mathbb{R}^{d\_{\mathcal{S}}} denotes the state space with dimension d𝒮∈ℕ+d\_{\mathcal{S}}\in\mathbb{N}\_{+}, equipped with metric 𝒟𝒮\mathcal{D}\_{\mathcal{S}}. 𝒜\mathcal{A} is the action/control space equipped with metric 𝒟𝒜\mathcal{D}\_{\mathcal{A}}. For analytical convenience, we assume that 𝒜\mathcal{A} is a closed hypercube in ℝd𝒜\mathbb{R}^{d\_{\mathcal{A}}} whose center is 0 and diam​(𝒜)=2​a¯>0{\rm diam}(\mathcal{A})=2\bar{a}>0. For the joint state-action space ℝd𝒮×𝒜\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}, we define the metric
𝒟​((x,a),(x′,a′))=(𝒟𝒮​(x,x′))2+(𝒟𝒜​(a,a′))2\mathcal{D}((x,a),(x^{\prime},a^{\prime}))=\sqrt{(\mathcal{D}\_{\mathcal{S}}(x,x^{\prime}))^{2}+(\mathcal{D}\_{\mathcal{A}}(a,a^{\prime}))^{2}} for (x,a),(x′,a′)∈ℝd𝒮×𝒜(x,a),(x^{\prime},a^{\prime})\in\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}. To ease the notation, we denote by ∥.∥\|.\| the ℓ2\ell\_{2} norm, unless specified otherwise.

The state transition are governed by a collection of drift and volatility terms μ:={μh​(x,a)}h∈[H−1]{\mu}:=\{\mu\_{h}(x,a)\}\_{h\in[H-1]} and σ:={σh​(x,a)}h∈[H−1]\sigma:=\{\sigma\_{h}(x,a)\}\_{h\in[H-1]}, with μh:ℝd𝒮×𝒜↦ℝd𝒮\mu\_{h}:\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}\mapsto\mathbb{R}^{d\_{\mathcal{S}}} and σh:ℝd𝒮×𝒜↦ℝd𝒮×d𝒮\sigma\_{h}:\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}\mapsto\mathbb{R}^{d\_{\mathcal{S}}\times d\_{\mathcal{S}}}. Mathematically, for h∈[H−1]h\in[H-1], the state process follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Xh+1−Xh\displaystyle X\_{h+1}-X\_{h} | =\displaystyle= | μh​(Xh,Ah)​Δ+σh​(Xh,Ah)​Bh​Δ,\displaystyle\mu\_{h}(X\_{h},A\_{h})\Delta+\sigma\_{h}(X\_{h},A\_{h})B\_{h}\sqrt{\Delta}, |  | (2.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X1\displaystyle X\_{1} | =\displaystyle= | ξ,\displaystyle\xi, |  |

where Δ>0\Delta>0 is the time-increment between two consecutive time stamps, BhB\_{h} are i.i.d. samples from the multi-variate Gaussian distribution 𝒩​(0,Id𝒮)\mathcal{N}(0,I\_{d\_{\mathcal{S}}}) and ξ\xi is independently sampled from an initial distribution Ξ\Xi. Note that ([2.1](https://arxiv.org/html/2512.14991v1#S2.E1 "In 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) can be viewed as a controlled diffusion process discretized in time.
We further denote the transition kernel of the dynamics as Th(⋅|x,a)∈𝒫(ℝd𝒮)T\_{h}(\cdot|x,a)\in\mathcal{P}(\mathbb{R}^{d\_{\mathcal{S}}}) conditioned on Xh=x,Ah=aX\_{h}=x,A\_{h}=a. Clearly, for non-degenerate σh​(x,a)\sigma\_{h}(x,a), we have Th(⋅|x,a)=𝒩(μh(x,a)Δ,Σh(x,a)Δ)T\_{h}(\cdot|x,a)=\mathcal{N}\Big(\mu\_{h}(x,a)\Delta,\Sigma\_{h}(x,a)\Delta\Big), where Σh​(x,a)=σh​(x,a)​σh⊤​(x,a)\Sigma\_{h}(x,a)=\sigma\_{h}(x,a)\sigma\_{h}^{\top}(x,a).

At timestamp hh, given state Xh=xX\_{h}=x and after taking an action Ah=aA\_{h}=a, the agent receives an instantaneous stochastic reward rh​(x,a)r\_{h}(x,a), which is drawn from a distribution Rh:ℝd𝒮×𝒜↦𝒫​(ℝ)R\_{h}:\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}\mapsto{\mathcal{P}(\mathbb{R})}. We let R={Rh}h∈[H]R=\{R\_{h}\}\_{h\in[H]} denote the collection of reward distributions and let R¯h​(x,a)=𝔼rh∼Rh​(x,a)​[rh]\bar{R}\_{h}(x,a)=\mathbb{E}\_{r\_{h}\sim R\_{h}(x,a)}[r\_{h}] be the mean-reward at timestamp hh under the state-action pair (x,a)(x,a).

The agent interacts with the environment (ℝd𝒮,𝒜,H,μ,σ,R)(\mathbb{R}^{d\_{\mathcal{S}}},\mathcal{A},H,\mu,\sigma,R) by taking actions according to a (randomized) control policy π\pi. Such a policy is specified by a collection of distributions π={πh}h∈[H]\pi=\{\pi\_{h}\}\_{h\in[H]}, where each timestamp-hh component πh:ℝd𝒮↦𝒫​(𝒜)\pi\_{h}:\mathbb{R}^{d\_{\mathcal{S}}}\mapsto\mathcal{P}(\mathcal{A}) maps a given state x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}}
to a distribution over the action space 𝒜\mathcal{A}. In the control literature, this is also referred to as a mixed control strategy (Yong and Zhou, [1999](https://arxiv.org/html/2512.14991v1#bib.bib63)).

### 2.1 Value function, Bellman equations and evaluation criterion

##### Bellman equation for generic policy.

For any policy π\pi, we define the policy value function under a given policy π\pi as

|  |  |  |
| --- | --- | --- |
|  | Vhπ​(x):=𝔼​[∑h′=hHrh′|Xh=x]​ subject to ​rh′∼Rh′​(Xh′,Ah′π)​ and ​Ah′π∼πh′​(Xh′).\displaystyle V\_{h}^{\pi}(x):=\mathbb{E}\Bigg[\sum\_{h^{\prime}=h}^{H}r\_{h^{\prime}}\Bigg|X\_{h}=x\Bigg]\mbox{ subject to }r\_{h^{\prime}}\sim R\_{h^{\prime}}(X\_{h^{\prime}},A\_{h^{\prime}}^{\pi})\mbox{ and }A^{\pi}\_{h^{\prime}}\sim\pi\_{h^{\prime}}(X\_{h^{\prime}}). |  |

Similarly, we define the state-action value function (or Q-function) Qhπ:ℝd𝒮×𝒜↦ℝQ\_{h}^{\pi}:\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}\mapsto\mathbb{R} as

|  |  |  |
| --- | --- | --- |
|  | Qhπ(x,a):=R¯h(x,a)+𝔼[∑h′=h+1Hrh′|Xh+1∼Th(⋅|x,a)],\displaystyle Q\_{h}^{\pi}(x,a):=\bar{R}\_{h}(x,a)+\mathbb{E}\left[\sum\_{h^{\prime}=h+1}^{H}r\_{h^{\prime}}\,\Bigg|\,X\_{h+1}\sim T\_{h}(\cdot|x,a)\right], |  |

subject to rh′∼Rh′​(Xh′,Ah′π)r\_{h^{\prime}}\sim R\_{h^{\prime}}(X\_{h^{\prime}},A\_{h^{\prime}}^{\pi}) and Ah′π∼πh′​(Xh′)A^{\pi}\_{h^{\prime}}\sim\pi\_{h^{\prime}}(X\_{h^{\prime}}). Intuitively, Qhπ​(x,a)Q\_{h}^{\pi}(x,a) is the value of taking action aa in state xx at timestamp hh and playing according to policy π\pi thereafter.

For a generic randomized policy π={πh}h∈[H]\pi=\{\pi\_{h}\}\_{h\in[H]}, the associated action-value function QπQ^{\pi} and value function VπV^{\pi} satisfy the Bellman equations (Puterman, [2014](https://arxiv.org/html/2512.14991v1#bib.bib50)). Specifically, for any x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}} and 𝒜\mathcal{A},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vhπ​(x)\displaystyle V\_{h}^{\pi}(x) | =\displaystyle= | 𝔼a∼πh​(x)​[Qhπ​(x,a)],\displaystyle\mathbb{E}\_{a\sim\pi\_{h}(x)}\Big[Q\_{h}^{\pi}(x,a)\Big], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qhπ​(x,a)\displaystyle Q\_{h}^{\pi}(x,a) | =\displaystyle= | R¯h​(x,a)+𝔼Xh+1∼Th(⋅|x,a),a′∼πh+1(Xh+1)​[Qh+1π​(Xh+1,a′)],\displaystyle\bar{R}\_{h}(x,a)+\mathbb{E}\_{X\_{h+1}\sim T\_{h}(\cdot|x,a),a^{\prime}\sim\pi\_{h+1}(X\_{h+1})}\Big[Q\_{h+1}^{\pi}(X\_{h+1},a^{\prime})\Big], |  |

with terminal condition VH+1π​(x)=0V\_{H+1}^{\pi}(x)=0 and QH+1π​(x,a)=0Q\_{H+1}^{\pi}(x,a)=0. As a consequence, we have for h∈[H]h\in[H] and x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vhπ​(x)\displaystyle V\_{h}^{\pi}(x) | =𝔼a∼πh​(x)​[R¯h​(x,a)]+𝔼Xh+1∼Th(⋅|x,a),a∼πh(x)​[Vh+1π​(Xh+1)].\displaystyle=\mathbb{E}\_{a\sim\pi\_{h}(x)}\Big[\bar{R}\_{h}(x,a)\Big]+\mathbb{E}\_{X\_{h+1}\sim T\_{h}(\cdot|x,a),a\sim\pi\_{h}(x)}\Big[V\_{h+1}^{\pi}(X\_{h+1})\Big]. |  |  |

##### Bellman equation for optimal policy.

The optimal value function is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vh∗​(x)=supπVhπ​(x).\displaystyle V\_{h}^{\*}(x)=\sup\_{\pi}V\_{h}^{\pi}(x). |  | (2.2) |

The corresponding Bellman equation for the optimal value function is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vh∗​(x)=supa∈𝒜{R¯h​(x,a)+𝔼X′∼Th(⋅|x,a)​[Vh+1∗​(X′)]},\displaystyle V\_{h}^{\*}(x)=\sup\_{a\in\mathcal{A}}\Big\{\bar{R}\_{h}(x,a)+\mathbb{E}\_{X^{\prime}\sim T\_{h}(\cdot|x,a)}\Big[V\_{h+1}^{\*}(X^{\prime})\Big]\Big\}, |  | (2.3) |

with terminal condition VH+1∗​(x)=0V^{\*}\_{H+1}(x)=0. We write the value function as

|  |  |  |
| --- | --- | --- |
|  | Vh∗​(x)=supa∈𝒜Qh∗​(x,a)\displaystyle V\_{h}^{\*}(x)=\sup\_{a\in\mathcal{A}}Q\_{h}^{\*}(x,a) |  |

where the Qh∗Q^{\*}\_{h} function is defined to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qh∗​(x,a)=R¯h​(x,a)+𝔼X′∼Th(⋅|x,a)​[Vh+1∗​(X′)].\displaystyle Q^{\*}\_{h}(x,a)=\bar{R}\_{h}(x,a)+\mathbb{E}\_{X^{\prime}\sim T\_{h}(\cdot|x,a)}\Big[V\_{h+1}^{\*}(X^{\prime})\Big]. |  | (2.4) |

There is also a Bellman equation for the Q∗Q^{\*}-function given by

|  |  |  |
| --- | --- | --- |
|  | Qh∗​(x,a)=R¯h​(x,a)+𝔼X′∼Th(⋅|x,a)​[supa′∈𝒜Qh+1∗​(X′,a′)].\displaystyle Q^{\*}\_{h}(x,a)=\bar{R}\_{h}(x,a)+\mathbb{E}\_{X^{\prime}\sim T\_{h}(\cdot|x,a)}\Big[\sup\_{a^{\prime}\in\mathcal{A}}Q\_{h+1}^{\*}(X^{\prime},a^{\prime})\Big]. |  |

##### Objective and evaluation criterion.

It is well known in the literature that for the MDP problem ([2.2](https://arxiv.org/html/2512.14991v1#S2.E2 "In Bellman equation for optimal policy. ‣ 2.1 Value function, Bellman equations and evaluation criterion ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) with a closed and bounded action space, there always exists an optimal policy that is deterministic (Puterman, [2014](https://arxiv.org/html/2512.14991v1#bib.bib50)). Specifically, π∗={πh∗}h∈[H]\pi^{\*}=\{\pi\_{h}^{\*}\}\_{h\in[H]}, where each πh∗​(x)=δah∗​(x)​(⋅)\pi\_{h}^{\*}(x)=\delta\_{a^{\*}\_{h}(x)}(\cdot) is a Dirac measure concentrated on some action ah∗​(x)∈𝒜a\_{h}^{\*}(x)\in\mathcal{A}. In this case, when no ambiguity arises, we simply write πh∗​(x)=ah∗​(x)\pi\_{h}^{\*}(x)=a^{\*}\_{h}(x) and refer to {ah∗​(x)}h∈[H]\{a^{\*}\_{h}(x)\}\_{h\in[H]} as the optimal deterministic policy (which may not be unique). Throughout the remainder of the paper, the term optimal policy will always refer to the optimal deterministic policy.

The goal is to design an algorithm that generates a sequence of randomized policies through interaction with the environment. The objective is that, as the episodes progress, the output policies improve in the sense that their corresponding value functions approach the optimal value function. To quantify the performance of such an algorithm, we introduce the notion of regret, defined as follows.

###### Definition 2.1.

For an algorithm deploying a sequence of policies {πk}k∈[K]\{\pi\_{k}\}\_{k\in[K]} with a given sequences of initial states {X1k}k∈[K]\{X\_{1}^{k}\}\_{k\in[K]}, define the regret as

|  |  |  |
| --- | --- | --- |
|  | Regret​(K):=∑k=1K(V1∗​(X1k)−V1πk​(X1k)).\displaystyle{\rm Regret}(K):=\sum\_{k=1}^{K}\Big(V\_{1}^{\*}(X\_{1}^{k})-V\_{1}^{\pi\_{k}}(X\_{1}^{k})\Big). |  |

### 2.2 Outstanding assumptions

In this subsection, we list the outstanding assumptions used throughout the paper. Specifially, we assume that μh\mu\_{h}, σh\sigma\_{h}, and R¯h\bar{R}\_{h} satisfy (local) Lipschitz continuity, and that the distribution Rh​(x,a)R\_{h}(x,a) exhibits sub-Gaussian tail decay, which are standard assumptions in the control and RL literature (see (Yong and Zhou, [1999](https://arxiv.org/html/2512.14991v1#bib.bib63)) and (Bubeck et al., [2011](https://arxiv.org/html/2512.14991v1#bib.bib11)) for example).

###### Assumption 2.1 (Regularity of the dynamics).

Assume there exists constants ℓμ,ℓσ>0\ell\_{\mu},\ell\_{\sigma}>0, m∈ℕm\in\mathbb{N} and L0>0L\_{0}>0 such that for all h∈[H−1]h\in[H-1], x1,x2∈ℝd𝒮x\_{1},x\_{2}\in\mathbb{R}^{d\_{\mathcal{S}}}, and a1,a2∈𝒜a\_{1},a\_{2}\in\mathcal{A}, it holds that:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖μh​(x1,a1)−μh​(x2,a2)‖\displaystyle\|\mu\_{h}(x\_{1},a\_{1})-\mu\_{h}(x\_{2},a\_{2})\| | ≤\displaystyle\leq | ℓμ​(‖x1−x2‖+‖a1−a2‖),\displaystyle\ell\_{\mu}\Big(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|\Big), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖σh​(x1,a1)−σh​(x1,a2)‖\displaystyle\|\sigma\_{h}(x\_{1},a\_{1})-\sigma\_{h}(x\_{1},a\_{2})\| | ≤\displaystyle\leq | ℓσ​(‖x1−x2‖+‖a1−a2‖),\displaystyle\ell\_{\sigma}\Big(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|\Big), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxh∈[H−1]⁡{‖μh​(0,0)‖,‖σh​(0,0)‖}\displaystyle\max\_{h\in[H-1]}\{\|\mu\_{h}(0,0)\|,\|\sigma\_{h}(0,0)\|\} | ≤\displaystyle\leq | L0.\displaystyle L\_{0}. |  |

In addition, assume the following elliptic condition, i.e., there exists a constant λ>0\lambda>0 such that ∀x∈ℝd𝒮,a∈𝒜,\forall x\in\mathbb{R}^{d\_{\mathcal{S}}},a\in\mathcal{A}, and h∈[H−1]h\in[H-1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σh​(x,a)​σh​(x,a)⊤≻λ​Id𝒮.\displaystyle\sigma\_{h}(x,a)\sigma\_{h}(x,a)^{\top}\succ\lambda I\_{d\_{\mathcal{S}}}. |  | (2.5) |

###### Assumption 2.2 (Regularity of the reward).

Assume the expected reward is local Lipschitz, namely, there exists constants ℓr>0\ell\_{r}>0, m∈ℕm\in\mathbb{N} and L0>0L\_{0}>0 such that for all h∈[H]h\in[H], x1,x2∈ℝd𝒮x\_{1},x\_{2}\in\mathbb{R}^{d\_{\mathcal{S}}}, and a1,a2∈𝒜a\_{1},a\_{2}\in\mathcal{A}, it holds that:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |R¯h​(x1,a1)−R¯h​(x2,a2)|\displaystyle|\bar{R}\_{h}(x\_{1},a\_{1})-\bar{R}\_{h}(x\_{2},a\_{2})| | ≤\displaystyle\leq | ℓr​(‖x1‖m+‖x2‖m+1)​(‖x1−x2‖+‖a1−a2‖),\displaystyle{\ell\_{r}\Big(\|x\_{1}\|^{m}+\|x\_{2}\|^{m}{+1}\Big)\,\Big(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|\Big)}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxh∈[H]⁡|R¯h​(0,0)|\displaystyle\max\_{h\in[H]}|\bar{R}\_{h}(0,0)| | ≤\displaystyle\leq | L0.\displaystyle L\_{0}. |  |

In addition, assume that the reward distribution has sub-Gaussian tail decay, i.e., there exists a known constant θ>0\theta>0 such that ∀x∈ℝd𝒮,a∈𝒜,λ1∈ℝ\forall x\in\mathbb{R}^{d\_{\mathcal{S}}},a\in\mathcal{A},\lambda\_{1}\in\mathbb{R}, and h∈[H]h\in[H]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼rh∼Rh​(x,a)​[exp⁡(λ1​(rh−R¯h​(x,a)))]≤eθ​λ122.\displaystyle\mathbb{E}\_{{}\_{r\_{h}\sim R\_{h}(x,a)}}\Big[\exp\Big(\lambda\_{1}(r\_{h}-\bar{R}\_{h}(x,a))\Big)\Big]\leq e^{\frac{\theta\lambda\_{1}^{2}}{2}}. |  | (2.6) |

###### Assumption 2.3 (Regularity of the initial distribution).

Assume that there exists p∈ℕp\in\mathbb{N} with p2>(m+1)2​(d𝒮+d𝒜+2)+(m+1)​(2​d𝒮+2​m+4)p^{2}>(m+1)^{2}(d\_{\mathcal{S}}+d\_{\mathcal{A}}+2)+(m+1)(2d\_{\mathcal{S}}+2m+4), such that the initial state X1=ξX\_{1}=\xi of the diffusion process in ([2.1](https://arxiv.org/html/2512.14991v1#S2.E1 "In 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) satisfies:

|  |  |  |
| --- | --- | --- |
|  | 𝔼ξ∼Ξ​[‖ξ‖p]<+∞,\displaystyle\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]<+\infty, |  |

The assumption that p2>(m+1)2​(d𝒮+d𝒜+2)+(m+1)​(2​d𝒮+2​m+4)p^{2}>(m+1)^{2}(d\_{\mathcal{S}}+d\_{\mathcal{A}}+2)+(m+1)(2d\_{\mathcal{S}}+2m+4) ensures that the initial distribution is well behaved. This requirement is not restrictive; for example, Gaussian and, more generally, sub-Gaussian distributions satisfy it. This condition is useful for the regret analysis.

### 2.3 Properties of the dynamics and value functions

Under the assumptions outlined in Section [2.2](https://arxiv.org/html/2512.14991v1#S2.SS2 "2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we establish several useful properties of the dynamics and the associated value functions, which will play a central role in the subsequent analysis.

###### Proposition 2.2.

Given Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), there exists a constant MM such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[suph∈[H]‖Xh‖p]≤M​(1+𝔼ξ∼Ξ​[‖ξ‖p]),\displaystyle\mathbb{E}\left[\sup\_{h\in[H]}\|X\_{h}\|^{p}\right]\leq M\Big(1+\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]\Big), |  |

where MM depends only on H,ℓμ,ℓσ,p,a¯,L0H,\ell\_{\mu},\ell\_{\sigma},p,\bar{a},L\_{0} and Δ\Delta.

The proof of Proposition [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [A.1](https://arxiv.org/html/2512.14991v1#A1.SS1 "A.1 Proof of Proposition 2.2 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). Proposition [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") immediately implies the following result.

###### Corollary 2.3.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"),[2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. For any given ρ>0\rho>0, there exists a constant MpM\_{p} independent of ρ\rho such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(suph∈[H]‖Xh‖≥ρ)≤Mpρp.\displaystyle\mathbb{P}\left(\sup\_{h\in[H]}\|X\_{h}\|\geq\rho\right)\leq\frac{M\_{p}}{\rho^{p}}. |  |

Corollary [2.3](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") suggests that, with probability at least 1−Mpρp1-\frac{M\_{p}}{\rho^{p}}, the entire state trajectory collected in one episode is within the radius ρ\rho.

Next, we establish the local Lipschitz continuity of the optimal value function and a growth condition for the value function under any generic policy π\pi. Both results are essential for algorithm design and regret analysis.

###### Proposition 2.4 (Local Lipschitz property of the value function).

Suppose Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. Then for each h∈[H]h\in[H], it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Vh∗​(x1)−Vh∗​(x2)|≤C¯h​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖,\displaystyle|V\_{h}^{\*}(x\_{1})-V\_{h}^{\*}(x\_{2})|\leq\overline{C}\_{h}\Big(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m}\Big)\|x\_{1}-x\_{2}\|, |  | (2.7) |

with C¯h:=C¯h​(C¯h+1,L0,ℓμ,ℓσ,ℓr,Δ,m)\overline{C}\_{h}:=\overline{C}\_{h}(\overline{C}\_{h+1},L\_{0},\ell\_{\mu},\ell\_{\sigma},\ell\_{r},\Delta,m).

The proof of Proposition [2.4](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem4 "Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [A.2](https://arxiv.org/html/2512.14991v1#A1.SS2 "A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

When the expected reward function is locally Lipschtiz with order mm (see Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the value function of any admissible policy π\pi has a polynomial growth of order m+1m+1.

###### Proposition 2.5.

Suppose Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. Then for all h∈[H]h\in[H] and any policy π\pi, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Vhπ​(x)|≤C~h​(‖x‖m+1+1),\displaystyle|V\_{h}^{\pi}(x)|\leq\widetilde{C}\_{h}(\|x\|^{m+1}+1), |  | (2.8) |

with constant C~h:=C~h​(C~h+1,L0,ℓμ,ℓσ,ℓr,a¯,H,h,Δ,m)\widetilde{C}\_{h}:=\widetilde{C}\_{h}(\widetilde{C}\_{h+1},L\_{0},\ell\_{\mu},\ell\_{\sigma},\ell\_{r},\bar{a},H,h,\Delta,m).

The proof of Proposition [2.5](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [A.3](https://arxiv.org/html/2512.14991v1#A1.SS3 "A.3 Proof of Proposition 2.5 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

## 3 Algorithm design

This section provides an overview of the algorithm design and its key ingredients, with the technical details and theoretical guarantees deferred to Sections [4](https://arxiv.org/html/2512.14991v1#S4 "4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [5](https://arxiv.org/html/2512.14991v1#S5 "5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). We develop a value-based algorithm that maintains estimators for both the Q-function and the value function over each partition of the joint state–action space. Based on these estimators, the algorithm implements a greedy policy by selecting the action that maximizes the estimated Q-function. The adaptive partitioning of the state–action space is guided by a bias–variance trade-off, following the approach introduced by Sinclair et al. (2023), which was originally developed for bounded state–action spaces.

##### Initial state partition.

Since the state space is unbounded, we restrict our learning and optimization to a subset of the full space, defined as

|  |  |  |
| --- | --- | --- |
|  | 𝒮1:={x∈ℝd𝒮|‖x‖≤ρ},\mathcal{S}\_{1}:=\Big\{x\in\mathbb{R}^{d\_{\mathcal{S}}}\,\,\Big|\,\,\|x\|\leq\rho\Big\}, |  |

where ρ>0\rho>0 is a radius to be specified in the regret analysis (see Section [5](https://arxiv.org/html/2512.14991v1#S5 "5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) such that the state process remains within 𝒮1\mathcal{S}\_{1} with high probability. For states outside this subset, we will apply some coarse estimations that do not affect the leading-order term in the regret bound.

Due to the unbounded nature of the state space, our initial partition of the state-action space differs from that in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)). We first partition the entire state-action space ℝd𝒮×𝒜\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A} into (closed) hypercubes of fixed diameter D>0D>0. 111The constant DD can be chosen arbitrarily, provided that 2​a¯​d𝒮+d𝒜D​d𝒜\frac{2\bar{a}\sqrt{d\_{\mathcal{S}}+d\_{\mathcal{A}}}}{D\sqrt{d\_{\mathcal{A}}}} is a positive integer. This ensures that the state-action space can be partitioned into those hypercubes. Denote by 𝒵D\mathcal{Z}\_{D} the collection of these hypercubes, and we construct the initial partition of our subset of state-action space by

|  |  |  |
| --- | --- | --- |
|  | ℬD:={B|B∈𝒵D,B∩(𝒮1×𝒜)≠∅},\displaystyle\mathcal{B}\_{D}:=\left\{B\,\Big|\,B\in\mathcal{Z}\_{D},B\cap(\mathcal{S}\_{1}\times\mathcal{A})\neq\emptyset\right\}, |  |

with |ℬD|<∞|\mathcal{B}\_{D}|<\infty. The adaptive partition procedure will be carried out only for B∈ℬDB\in\mathcal{B}\_{D} (not 𝒵D\mathcal{Z}\_{D}). For further use, define the partition space as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z¯:=∪B∈ℬDB.\displaystyle\bar{Z}:=\cup\_{B\in\mathcal{B}\_{D}}B. |  | (3.1) |

As a consequence, 𝒮1×𝒜⊆Z¯\mathcal{S}\_{1}\times\mathcal{A}\subseteq\bar{Z}.

The main algorithm, especially the key mechanism behind adaptive partition, is inspired by (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)).
In a nutshell, the proposed Adaptive Partition and Learning for Diffusions (APL-Diffusion) Algorithm (see Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) consists of the following key steps:

* •

  Construct the estimators Q¯hk(.),V¯hk(.)\overline{Q}\_{h}^{k}(.),\overline{V}\_{h}^{k}(.) for the QQ-function and the value function;
* •

  Select block BhkB\_{h}^{k} according to the estimated QQ-function;
* •

  Construct the confidence level CONFhk​(Bhk){\rm CONF}\_{h}^{k}(B\_{h}^{k}) for each visited block BhkB\_{h}^{k};
* •

  If CONFhk​(Bhk)≤diam​(Bhk){\rm CONF}\_{h}^{k}(B\_{h}^{k})\leq{\rm diam}(B\_{h}^{k}), split the block BhkB\_{h}^{k}

  + –

    Each side of the block is divided evenly into two parts along every dimension,
  + –

    As a result, BkhB\_{k}^{h} is split into smaller (closed) hypercubes with half the diameter of the original block.

Note that our estimation of the Q-functions and value functions, as well as the construction of the confidence measure, differs from (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) due to the different problem setting.

Algorithm 1  Adaptive Partition and Learning for Diffusions (APL-Diffusion)

1:Initialize:
Initialize the partition 𝒫h0=ℬD\mathcal{P}\_{h}^{0}=\mathcal{B}\_{D} for h∈[H]h\in[H] and the counting with
nh0​(B)=0n\_{h}^{0}(B)=0 for B∈𝒫h0B\in\mathcal{P}\_{h}^{0}.
Also, initialize the function estimators
Q¯h0,V¯h0\overline{Q}\_{h}^{0},\overline{V}\_{h}^{0} according to ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and Q¯hk​(Z¯∁)\overline{Q}\_{h}^{k}(\bar{Z}^{\complement}) according to ([5.5](https://arxiv.org/html/2512.14991v1#S5.E5 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) for k∈[K]∪{0}k\in[K]\cup\{0\}

2:for each episode k=1,2,⋯,Kk=1,2,\cdots,K do

3:  for each step h=1,2,⋯,Hh=1,2,\cdots,H do

4:   Observe XhkX\_{h}^{k}

5:    Select BhkB\_{h}^{k} by BLOCK SELECTION(Xhk)(X\_{h}^{k})

6:    Take action: AhkA\_{h}^{k} uniformly sampled from the action set Γ𝒜​(Bhk)\Gamma\_{\mathcal{A}}(B\_{h}^{k})

7:   Receive rhkr\_{h}^{k} and transition to Xh+1kX\_{h+1}^{k}

8:  end for

9:  for each step h=H,H−1,⋯,1h=H,H-1,\cdots,1 do

10:   UPDATE COUNTS (Bhk)(B\_{h}^{k})

11:   SPLITTING (Bhk)(B\_{h}^{k})

12:   UPDATE ESTIMATE (Xhk,Ahk,Xh+1k,rhk,Bhk)(X\_{h}^{k},A\_{h}^{k},X\_{h+1}^{k},r\_{h}^{k},B\_{h}^{k})

13:  end for

14:end for

Projection operators (line [6](https://arxiv.org/html/2512.14991v1#alg1.l6 "In Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") in Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and line [1](https://arxiv.org/html/2512.14991v1#alg2.l1 "In Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") in Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
For a block B⊂ℝd𝒮×𝒜B\subset\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}, we denote Γ𝒮​(B)\Gamma\_{\mathcal{S}}(B) and Γ𝒜​(B)\Gamma\_{\mathcal{A}}(B) as the projections of BB into ℝd𝒮\mathbb{R}^{d\_{\mathcal{S}}} and 𝒜\mathcal{A}, respectively.

The three primary components (sub-algorithms) of Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), BLOCK SELECTION(Xhk)(X\_{h}^{k}), UPDATE ESTIMATE (Xhk,Ahk,Xh+1k,rhk,Bhk)(X\_{h}^{k},A\_{h}^{k},X\_{h+1}^{k},r\_{h}^{k},B\_{h}^{k}) and SPLITTING(Bhk)(B\_{h}^{k}), are presented below.

Algorithm 2  BLOCK SELECTION(Xhk)(X\_{h}^{k})

1:
Determine RELEVANThk​(Xhk)={B∈𝒫hk−1∪{Z¯∁}|Xhk∈Γ𝒮​(B)}{\rm RELEVANT}\_{h}^{k}(X\_{h}^{k})=\{B\in\mathcal{P}\_{h}^{k-1}\cup\{\bar{Z}^{\complement}\}|X\_{h}^{k}\in\Gamma\_{\mathcal{S}}(B)\}

2:
Greedy selection rule: select Bhk∈arg⁡maxB∈RELEVANThk​(Xhk)⁡Q¯hk−1​(B)B\_{h}^{k}\in\arg\max\_{B\in{\rm RELEVANT}\_{h}^{k}(X\_{h}^{k})}\overline{Q}\_{h}^{k-1}(B)

For a given state XhkX\_{h}^{k}, Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") determines all B∈𝒫hk−1∪{Z¯∁}B\in\mathcal{P}\_{h}^{k-1}\cup\{\bar{Z}^{\complement}\} that XhkX\_{h}^{k} lies in and chooses the one that maximizes the current estimate of the Q function Q¯hk−1\overline{Q}\_{h}^{k-1}.

Algorithm 3  UPDATE COUNTS(Bhk)(B\_{h}^{k})

1:for B∈𝒫hk−1B\in\mathcal{P}\_{h}^{k-1} do

2:  
Update nhk​(B)n\_{h}^{k}(B) via ([3.2](https://arxiv.org/html/2512.14991v1#S3.E2 "In Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))

3:end for

Counts updates (line [2](https://arxiv.org/html/2512.14991v1#alg3.l2 "In Algorithm 3 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") in Algorithm [3](https://arxiv.org/html/2512.14991v1#alg3 "Algorithm 3 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
Note that nhk​(B)n\_{h}^{k}(B) is the number of times the block BB or its ancestors have been visited up to (and including) episode kk. It is updated for the visited block BhkB\_{h}^{k} if Bhk∈𝒫hk−1B\_{h}^{k}\in\mathcal{P}\_{h}^{k-1} and remained the same for other blocks B∈𝒫hk−1∖{Bhk}B\in\mathcal{P}\_{h}^{k-1}\setminus\{B\_{h}^{k}\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | nhk​(Bhk)=nhk−1​(Bhk)+1,nhk​(B)=nhk−1​(B).\displaystyle n\_{h}^{k}(B\_{h}^{k})=n\_{h}^{k-1}(B\_{h}^{k})+1,\quad n\_{h}^{k}(B)=n\_{h}^{k-1}(B). |  | (3.2) |

Algorithm 4  SPLITTING(Bhk)(B\_{h}^{k})

1: If Bhk∈𝒫hk−1B\_{h}^{k}\in\mathcal{P}\_{h}^{k-1}, CONFhk​(Bhk)≤diam​(Bhk){\rm CONF}\_{h}^{k}(B\_{h}^{k})\leq{\rm{\rm diam}}(B\_{h}^{k})
then:

2:   Construct 𝒫​(Bhk)={B1,⋯,B2d𝒮+d𝒜}\mathcal{P}(B\_{h}^{k})=\{B\_{1},\cdots,B\_{2^{d\_{\mathcal{S}}+d\_{\mathcal{A}}}}\} as the partition of BhkB\_{h}^{k} such that each BiB\_{i} is a (closed) hypercube with diam​(Bi)=diam​(B)2{\rm diam}(B\_{i})=\frac{{\rm diam}(B)}{2} such that ∪i=12d𝒮+d𝒜Bi=Bhk\cup\_{i=1}^{2^{d\_{\mathcal{S}}+d\_{\mathcal{A}}}}B\_{i}=B\_{h}^{k}

3:   Update 𝒫hk=𝒫hk−1∪𝒫​(Bhk)∖Bhk\mathcal{P}\_{h}^{k}=\mathcal{P}\_{h}^{k-1}\cup\mathcal{P}(B\_{h}^{k})\setminus B\_{h}^{k}

4:for B1,⋯,B2d𝒮+d𝒜B\_{1},\cdots,B\_{2^{d\_{\mathcal{S}}+d\_{\mathcal{A}}}} do

5:  Initialize nhk​(Bi)=nhk​(Bhk)n\_{h}^{k}(B\_{i})=n\_{h}^{k}(B\_{h}^{k})

6:end for

7:Else Bhk∈𝒫hk−1B\_{h}^{k}\in\mathcal{P}\_{h}^{k-1} with CONFhk​(Bhk)>diam​(Bhk){\rm CONF}\_{h}^{k}(B\_{h}^{k})>{\rm{\rm diam}}(B\_{h}^{k}) or Bhk=Z¯∁B\_{h}^{k}=\bar{Z}^{\complement}
then:

8:   Update 𝒫hk=𝒫hk−1\mathcal{P}\_{h}^{k}=\mathcal{P}\_{h}^{k-1}

Splitting rule (line [1](https://arxiv.org/html/2512.14991v1#alg4.l1 "In Algorithm 4 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") in Algorithm [4](https://arxiv.org/html/2512.14991v1#alg4 "Algorithm 4 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
To refine the partition over episodes, in episode kk and step hh, we split the visited block BhkB\_{h}^{k} if

|  |  |  |  |
| --- | --- | --- | --- |
|  | CONFhk​(Bhk)≤diam​(Bhk),\displaystyle{\rm CONF}\_{h}^{k}(B\_{h}^{k})\leq{\rm diam}(B\_{h}^{k}), |  | (3.3) |

where CONFhk{\rm CONF}\_{h}^{k} is formally defined in ([4.20](https://arxiv.org/html/2512.14991v1#S4.E20 "In 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), which represents the confidence of a block in its estimators. In a nutshell, ([3.3](https://arxiv.org/html/2512.14991v1#S3.E3 "In Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) compares the confidence of the estimators for the visited block, quantified by CONFhk​(Bhk){\rm CONF}\_{h}^{k}(B\_{h}^{k}), and the bias of the block, which is proportional to the diameter of the block. If the bias associated with a block, in representing all the points it contains, exceeds the confidence level of its estimators, the block should be further partitioned.

Algorithm 5  UPDATE ESTIMATE (Xhk,Ahk,Xh+1k,rhk,Bhk)(X\_{h}^{k},A\_{h}^{k},X\_{h+1}^{k},r\_{h}^{k},B\_{h}^{k})

1:for B∈𝒫hkB\in\mathcal{P}\_{h}^{k} do

2:  
Update the following quantities:

* •

  μ^hk​(B)\widehat{\mu}\_{h}^{k}(B), Σ^hk​(B)\widehat{\Sigma}\_{h}^{k}(B) and T¯hk(⋅|B)\bar{T}\_{h}^{k}(\cdot|B) via ([4.1](https://arxiv.org/html/2512.14991v1#S4.E1 "In 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))
* •

  R^hk​(B)\hat{R}\_{h}^{k}(B) via ([4.3](https://arxiv.org/html/2512.14991v1#S4.Ex21 "4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))

3:  Update Q¯hk\overline{Q}\_{h}^{k} and V¯hk\overline{V}\_{h}^{k} via ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))-([5.14](https://arxiv.org/html/2512.14991v1#S5.E14 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))

4:end for

Estimators (line [2](https://arxiv.org/html/2512.14991v1#alg5.l2 "In Algorithm 5 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") in Algorithm [5](https://arxiv.org/html/2512.14991v1#alg5 "Algorithm 5 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
For B∈𝒫hkB\in\mathcal{P}\_{h}^{k}, R^hk​(B)\hat{R}\_{h}^{k}(B), μ^hk​(B)\widehat{\mu}\_{h}^{k}(B), Σ^hk​(B)\widehat{\Sigma}\_{h}^{k}(B) and T¯hk(⋅|B)\bar{T}\_{h}^{k}(\cdot|\,B) are the estimators of R¯h​(x,a)\bar{R}\_{h}(x,a), μh​(x,a)\mu\_{h}(x,a), Σh​(x,a)\Sigma\_{h}(x,a) and Th(⋅|x,a)T\_{h}(\cdot|\,x,a), for the state-action pairs (x,a)∈B(x,a)\in B. In addition, Q¯hk​(B)\overline{Q}\_{h}^{k}(B) is the estimate of Qh∗​(x,a)Q\_{h}^{\*}(x,a) for (x,a)∈B(x,a)\in B and V¯hk​(x)\overline{V}\_{h}^{k}(x) is the estimate of Vh∗​(x)V\_{h}^{\*}(x) for x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}}.

For further use, we define the APL-Diffusion policy as the sequences of policies described in line [5](https://arxiv.org/html/2512.14991v1#alg1.l5 "In Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [6](https://arxiv.org/html/2512.14991v1#alg1.l6 "In Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") in Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and denote it by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π~k}k∈[K].\displaystyle\{\tilde{\pi}^{k}\}\_{k\in[K]}. |  | (3.4) |

Demonstration of the algorithm. Given the complexity of the algorithm and sophistication of the design,
below we provide a demonstration example with visualization, which is inspired by Figure 1 from Sinclair et al. ([2023](https://arxiv.org/html/2512.14991v1#bib.bib53)).

![Refer to caption](Adaptive_Partition_Heat.png)


(a) Illustration of the adaptive partition. The right panel zooms
  
into the current partition 𝒫hk−1\mathcal{P}\_{h}^{k-1}.

![Refer to caption](Adaptive_Partition_Tree.png)


(b) History partitions {𝒫hj}j=0k−1\{\mathcal{P}\_{h}^{j}\}\_{j=0}^{k-1} .

Figure 1: Partitioning scheme for ℝ×𝒜=(−∞,+∞)×[−3,3]\mathbb{R}\times\mathcal{A}=(-\infty,+\infty)\times[-3,3].

In Figure [1](https://arxiv.org/html/2512.14991v1#S3.F1 "Figure 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") (a)-left, the color indicates the true value of Qh∗Q\_{h}^{\*}, with the darker corresponding to larger values. Note that the partition is more refined in areas which have higher Qh∗Q\_{h}^{\*}.
In Figure [1](https://arxiv.org/html/2512.14991v1#S3.F1 "Figure 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") (a)-right, we zoom in the current partition 𝒫hk−1\mathcal{P}\_{h}^{k-1}. In Figure [1](https://arxiv.org/html/2512.14991v1#S3.F1 "Figure 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") (b), the history partitions {𝒫hj}j=0k−1\{\mathcal{P}\_{h}^{j}\}\_{j=0}^{k-1} are depicted by a tree diagram.

## 4 Concentration inequalities of the estimators

This section is devoted to the development of concentration inequalities of the estimators associated with the transition kernel. Different from (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)), we fully utilize the property of diffusion process and construct estimators for the drift and volatility. Note that establishing concentration inequalities for covariance matrices under merely Lipschitz conditions on the volatility is challenging. To address this, we introduce and carefully analyze two intermediate terms (see ([4.2](https://arxiv.org/html/2512.14991v1#S4.E2 "In 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))).

Here, we denote k1≤,⋯,≤knhk​(B)k\_{1}\leq,\cdots,\leq k\_{n\_{h}^{k}(B)} the episode indices such that BB or its ancestors have been visited by the algorithm up to episode kk. It is clear that knhk​(B)≤kk\_{n\_{h}^{k}(B)}\leq k.

For each block B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with (h,k)∈[H−1]×[K](h,k)\in[H-1]\times[K], when nhk​(B)>0n^{k}\_{h}(B)>0 we construct the estimators μ^hk​(B)\widehat{\mu}\_{h}^{k}(B) and Σ^hk​(B)\widehat{\Sigma}\_{h}^{k}(B) by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ^hk​(B)\displaystyle\widehat{\mu}\_{h}^{k}(B) | =\displaystyle= | ∑i(Xh+1ki−Xhki)nhk​(B)​Δ,\displaystyle\frac{\sum\_{i}(X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}})}{n\_{h}^{k}(B)\Delta}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Σ^hk​(B)\displaystyle\widehat{\Sigma}\_{h}^{k}(B) | =\displaystyle= | ∑i((Xh+1ki−Xhki)−μ^hk​(B)​Δ)​((Xh+1ki−Xhki)−μ^hk​(B)​Δ)⊤nhk​(B)​Δ.\displaystyle\frac{\sum\_{i}\Big((X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}})-\widehat{\mu}\_{h}^{k}(B)\Delta\Big)\Big((X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}})-\widehat{\mu}\_{h}^{k}(B)\Delta\Big)^{\top}}{n\_{h}^{k}(B)\Delta}. |  | (4.1) |

When nhk​(B)=0n^{k}\_{h}(B)=0, we simply take
μ^hk​(B)=0​ and ​Σ^hk​(B)=0.\widehat{\mu}\_{h}^{k}(B)=0\mbox{ and }\widehat{\Sigma}\_{h}^{k}(B)=0.

As a result, the transition kernel can be estimated by

|  |  |  |
| --- | --- | --- |
|  | T¯hk(⋅|B):=𝒩(μ^hk(B)Δ,Σ^hk(B)Δ).\displaystyle\bar{T}\_{h}^{k}(\cdot|B):=\mathcal{N}\Big(\widehat{\mu}\_{h}^{k}(B)\Delta,\widehat{\Sigma}\_{h}^{k}(B)\Delta\Big). |  |

Since the analysis heavily relies on conditioning arguments, we also introduce the following notations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼¯​[⋅]\displaystyle\overline{\mathbb{E}}\Big[\cdot\Big] | :=\displaystyle:= | 𝔼[⋅|Xhk1,Ahk1,…,Xhknhk​(B),Ahknhk​(B)],\displaystyle\mathbb{E}\Big[\,\,\cdot\,\,\Big|X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...,X\_{h}^{k\_{n\_{h}^{k}(B)}},A\_{h}^{k\_{n\_{h}^{k}(B)}}\Big], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝕍¯​[⋅]\displaystyle\overline{\mathbb{V}}\Big[\cdot\Big] | :=\displaystyle:= | 𝕍[⋅|Xhk1,Ahk1,…,Xhknhk​(B),Ahknhk​(B)],\displaystyle\mathbb{\mathbb{V}}\Big[\,\,\cdot\,\,\Big|X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...,X\_{h}^{k\_{n\_{h}^{k}(B)}},A\_{h}^{k\_{n\_{h}^{k}(B)}}\Big], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒲¯2​(⋅)\displaystyle\overline{\mathcal{W}}\_{2}\Big(\cdot\Big) | :=\displaystyle:= | 𝒲2(⋅|Xhk1,Ahk1,…,Xhknhk​(B),Ahknhk​(B)).\displaystyle\mathcal{W}\_{2}\Big(\,\,\cdot\,\,\Big|X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...,X\_{h}^{k\_{n\_{h}^{k}(B)}},A\_{h}^{k\_{n\_{h}^{k}(B)}}\Big). |  |

Note that Xh+1k1−Xhk1,…,Xh+1knhk​(B)−Xhknhk​(B)X\_{h+1}^{k\_{1}}-X\_{h}^{k\_{1}},...,X\_{h+1}^{k\_{n\_{h}^{k}(B)}}-X\_{h}^{k\_{n\_{h}^{k}(B)}} are conditionally independent given Xhk1,Ahk1,…,Xhknhk​(B)X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...,X\_{h}^{k\_{n\_{h}^{k}(B)}}, and Ahknhk​(B)A\_{h}^{k\_{n\_{h}^{k}(B)}}. Hence it is straightforward to derive concentration inequality for μ^hk​(B)\widehat{\mu}\_{h}^{k}(B). However, the expectation and variance of the estimator Σ^hk​(B)\widehat{\Sigma}\_{h}^{k}(B) are challenging to analyze as Xh+1k1−Xhk1−μ^hk​(B)​ΔX\_{h+1}^{k\_{1}}-X\_{h}^{k\_{1}}-\widehat{\mu}\_{h}^{k}(B)\Delta ,⋯\cdots,Xh+1knhk​(B)−Xhknhk​(B)−μ^hk​(B)​ΔX\_{h+1}^{k\_{n\_{h}^{k}(B)}}-X\_{h}^{k\_{n\_{h}^{k}(B)}}-\widehat{\mu}\_{h}^{k}(B)\Delta are dependent.
Hence, we consider the following intermediate quantity and decomposition to proceed:

|  |  |  |
| --- | --- | --- |
|  | Σ~hk​(B):=∑i((Xh+1ki−Xhki)−Δ​𝔼¯​[μ^hk​(B)])​((Xh+1ki−Xhki)−Δ​𝔼¯​[μ^hk​(B)])⊤nhk​(B)​Δ,\displaystyle\widetilde{\Sigma}\_{h}^{k}(B):=\frac{\sum\_{i}\Big((X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}})-\Delta\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big)\Big((X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}})-\Delta\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big)^{\top}}{n\_{h}^{k}(B)\Delta}, |  |

and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ‖Σ^hk​(B)−Σh​(x,a)‖F\displaystyle\|\widehat{\Sigma}\_{h}^{k}(B)-\Sigma\_{h}(x,a)\|\_{F} |  | (4.2) |
|  |  | ≤\displaystyle\leq | ‖Σ^hk​(B)−Σ~hk​(B)‖F⏟(I)+‖Σ~hk​(B)−𝔼¯​[Σ~hk​(B)]‖F⏟(I​I)+‖𝔼¯​[Σ~hk​(B)]−Σh​(x,a)‖F⏟(I​I​I).\displaystyle\underbrace{\Big\|\widehat{\Sigma}\_{h}^{k}(B)-\widetilde{\Sigma}\_{h}^{k}(B)\Big\|\_{F}}\_{(I)}+\underbrace{\Big\|\widetilde{\Sigma}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Big\|\_{F}}\_{(II)}+\underbrace{\Big\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]-\Sigma\_{h}(x,a)\Big\|\_{F}}\_{(III)}. |  |

We analyze (I)-(III) in the next subsection. As a heads-up,

* •

  Term (II) on the RHS is straightforward to bound as Xh+1k1−Xhk1−𝔼¯​[μ^hk​(B)]​Δ,⋯,Xh+1knhk​(B)−Xhknhk​(B)−𝔼¯​[μ^hk​(B)]​ΔX\_{h+1}^{k\_{1}}-X\_{h}^{k\_{1}}-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Delta,\cdots,X\_{h+1}^{k\_{n\_{h}^{k}(B)}}-X\_{h}^{k\_{n\_{h}^{k}(B)}}-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Delta are conditionally independent. We handle this term by Lemma [B.2](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.2 Lemma B.2 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Proposition [4.2](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").
* •

  To bound term (I), let Pi:=(Xh+1ki−Xhki)−μ^hk​(B)​ΔP\_{i}:=(X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}})-\widehat{\mu}\_{h}^{k}(B)\Delta and Qi:=(Xh+1ki−Xhki)−Δ​𝔼¯​[μ^hk​(B)]Q\_{i}:=(X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}})-\Delta\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]. Then we have

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | ‖Σ^hk​(B)−Σ~hk​(B)‖\displaystyle\|\widehat{\Sigma}\_{h}^{k}(B)-\widetilde{\Sigma}\_{h}^{k}(B)\| | =\displaystyle= | ‖∑iPi​Pi⊤nhk​(B)​Δ−∑iQi​Qi⊤nhk​(B)​Δ‖\displaystyle\Bigg\|\frac{\sum\_{i}P\_{i}P\_{i}^{\top}}{n\_{h}^{k}(B)\Delta}-\frac{\sum\_{i}Q\_{i}Q\_{i}^{\top}}{n\_{h}^{k}(B)\Delta}\Bigg\| |  | (4.3) |
  |  |  | =\displaystyle= | ‖∑iPi​(Pi⊤−Qi⊤)nhk​(B)​Δ+∑i(Pi−Qi)​Qi⊤nhk​(B)​Δ‖\displaystyle\Bigg\|\frac{\sum\_{i}P\_{i}(P\_{i}^{\top}-Q\_{i}^{\top})}{n\_{h}^{k}(B)\Delta}+\frac{\sum\_{i}(P\_{i}-Q\_{i})Q\_{i}^{\top}}{n\_{h}^{k}(B)\Delta}\Bigg\| |  |
  |  |  | =\displaystyle= | ‖(μ^hk​(B)−𝔼¯​[μ^hk​(B)])​(μ^hk​(B)−𝔼¯​[μ^hk​(B)])⊤​Δ‖,\displaystyle\Bigg\|\Big(\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big)\Big(\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big)^{\top}\Delta\Bigg\|, |  |

  which will be handled by Lemma [B.1](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1 Lemma B.1 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Proposition [4.1](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").
* •

  As for term (III), we provide an upper bound in Theorem [4.7](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem7 "Theorem 4.7. ‣ 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

### 4.1 Concentration of the estimators for drift and volatility

In this section, we provide concentration inequalities for the drift and volatility estimators.

For convinience, denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | L:=max⁡{ℓμ,ℓσ},\displaystyle L:=\max\{\ell\_{\mu},\ell\_{\sigma}\}, |  | (4.4) |

where ℓμ,ℓσ\ell\_{\mu},\ell\_{\sigma} are the Lipschitz constants defined in Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").
For any h∈[H],k∈[K]∪{0}h\in[H],k\in[K]\cup\{0\}, B∈𝒫hkB\in\mathcal{P}\_{h}^{k}, denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~​(B),a~​(B)\tilde{x}(B),\tilde{a}(B) as centers of Γ𝒮​(B),Γ𝒜​(B)\Gamma\_{\mathcal{S}}(B),\Gamma\_{\mathcal{A}}(B) respectively. |  | (4.5) |

In addition, denote Bo{}^{o}B as the block in the original partition that contains a given block BB, i.e., Bo{}^{o}B is the unique set satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | B⊂oB​ such that o​B∈ℬD.\displaystyle B\subset\,^{o}B\mbox{ such that }^{o}B\in\mathcal{B}\_{D}. |  | (4.6) |

With these notations, we have, for any (x,a)∈B(x,a)\in B and f=μh,σhf=\mu\_{h},\sigma\_{h},

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖f​(x,a)‖\displaystyle\|f(x,a)\| | ≤\displaystyle\leq | ∥f(x~(oB),a~(oB))∥+∥f(x,a)−f(x~(oB),a~(oB))∥\displaystyle\Big\|f(\tilde{x}(^{o}B),\tilde{a}(^{o}B))\Big\|+\Big\|f(x,a)-f(\tilde{x}(^{o}B),\tilde{a}(^{o}B))\Big\| |  | (4.7) |
|  |  | ≤\displaystyle\leq | L0+L(∥x~(oB)∥+a¯)+2LD:=η(∥x~(oB)∥),\displaystyle L\_{0}+L(\|\tilde{x}(^{o}B)\|+\bar{a})+2LD:=\eta(\|\tilde{x}(^{o}B)\|), |  |

in which we defined η:ℝ+∪{0}↦ℝ+\eta:\mathbb{R}\_{+}\cup\{0\}\mapsto\mathbb{R}\_{+}.

Next, we establish concentration inequalities for the estimators of the drift and volatility terms, as presented in Propositions [4.1](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [4.2](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Proposition 4.1.

Suppose Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") holds, then we have the following result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(∥μ^hk(B)−𝔼¯[μ^hk(B)]∥≤κμ(δ,∥x~(oB)∥,nhk(B)),∀h∈[H−1],k∈[K],B∈𝒫hk​ with​nhk​(B)>0)≥1−δ,\displaystyle\mathbb{P}\begin{pmatrix}&\left\|\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\right\|\leq\kappa\_{\mu}\big(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B)\big),\\ &\forall h\in[H-1],k\in[K],B\in\mathcal{P}\_{h}^{k}\,\,\mbox{ with}\,\,n\_{h}^{k}(B)>0\end{pmatrix}\geq 1-\delta, |  | (4.8) |

where κμ:(0,1]×(ℝ+∪{0})×ℕ+↦ℝ+\kappa\_{\mu}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\times\mathbb{N}\_{+}\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |
| --- | --- | --- |
|  | κμ​(δ,y,n):=η​(y)Δ​(d𝒮n+2​log⁡(H​K2δ)n).\displaystyle\kappa\_{\mu}(\delta,y,n):=\frac{\eta(y)}{\sqrt{\Delta}}\Big(\sqrt{\frac{d\_{\mathcal{S}}}{n}}+\sqrt{\frac{2\log(\frac{HK^{2}}{\delta})}{n}}\Big). |  |

The proof of Proposition [4.1](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is largely inspired by the proof of Lemma 5 in (Nguyen et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib47)), which is deferred to Appendix [B.3](https://arxiv.org/html/2512.14991v1#A2.SS3 "B.3 Proof of Proposition 4.1 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Proposition 4.2.

Suppose Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") holds. Then there exist universal constants D1>0,D2>1,D3>0D\_{1}>0,D\_{2}>1,D\_{3}>0 (independent of ρ\rho) such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(∥Σ~hk(B)−𝔼¯[Σ~hk(B)]∥≤κΣ(δ,∥x~(oB)∥,nhk(B)),∀h∈[H−1],k∈[K],B∈𝒫hk​ with​nhk​(B)>0)≥1−δ,\displaystyle\mathbb{P}\begin{pmatrix}\Big\|\widetilde{\Sigma}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Big\|\leq\kappa\_{\Sigma}\big(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B)\big),\\ \forall h\in[H-1],k\in[K],B\in\mathcal{P}\_{h}^{k}\,\,\mbox{ with}\,\,n\_{h}^{k}(B)>0\end{pmatrix}\geq 1-\delta, |  | (4.9) |

where κΣ:(0,1]×(ℝ+∪{0})×ℕ+↦ℝ+\kappa\_{\Sigma}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\times\mathbb{N}\_{+}\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |
| --- | --- | --- |
|  | κΣ​(δ,y,n):=η​(y)2​(D1​(d𝒮n+d𝒮n)+(log⁡(D2d𝒮)D3​n+log⁡(D2​H​K2δ)D3​n)).\displaystyle\kappa\_{\Sigma}(\delta,y,n):=\eta(y)^{2}\Bigg(D\_{1}\Big(\sqrt{\frac{d\_{\mathcal{S}}}{n}}+\frac{d\_{\mathcal{S}}}{\sqrt{n}}\Big)+\Bigg(\sqrt{\frac{\log(\frac{D\_{2}}{d\_{\mathcal{S}}})}{D\_{3}n}}+\frac{\log(\frac{D\_{2}HK^{2}}{\delta})}{D\_{3}\sqrt{n}}\Bigg)\Bigg). |  |

The proof of Proposition [4.2](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is essentially based on Theorem 6.5 in (Wainwright, [2019](https://arxiv.org/html/2512.14991v1#bib.bib59)) and Lemma 6 in (Nguyen et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib47)), which is deferred to Appendix [B.4](https://arxiv.org/html/2512.14991v1#A2.SS4 "B.4 Proof of Proposition 4.2 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

### 4.2 Concentration inequalities for transition kernel estimators

Building upon Propositions [4.1](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [4.2](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we have the following result bounding the Wasserstein distance between the true transition kernel and the estimated transition kernel. The detailed proof is deferred to Appendix [B.5](https://arxiv.org/html/2512.14991v1#A2.SS5 "B.5 Proof of Theorem 4.3 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Theorem 4.3.

Given Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), it holds with probability at least 1−2​δ1-2\delta that, for any (h,k)∈[H−1]×[K](h,k)\in[H-1]\times[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and any (x,a)∈B(x,a)\in B,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲¯2​(𝒩​(μ^hk​(B)​Δ,Σ^hk​(B)​Δ),𝒩​(μh​(x,a)​Δ,Σh​(x,a)​Δ))\displaystyle\overline{\mathcal{W}}\_{2}\Big(\mathcal{N}(\widehat{\mu}\_{h}^{k}(B)\Delta,\widehat{\Sigma}\_{h}^{k}(B)\Delta),\mathcal{N}(\mu\_{h}(x,a)\Delta,\Sigma\_{h}(x,a)\Delta)\Big) |  | (4.10) |
|  |  | ≤\displaystyle\leq | Δκμ(δ,∥x~(oB)∥,nhk(B))+Δ32λκμ(δ,∥x~(oB)∥,nhk(B))2+d𝒮​Δ12λκΣ(δ,∥x~(oB)∥,nhk(B))\displaystyle\Delta\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))+\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{2}+\frac{\sqrt{d\_{\mathcal{S}}}\Delta^{\frac{1}{2}}}{\sqrt{\lambda}}\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B)) |  |
|  |  |  | +‖𝔼¯​[μ^hk​(B)]−μh​(x,a)‖​Δ+‖𝔼¯​[Σ~hk​(B)]−Σh​(x,a)‖​Δλ.\displaystyle+\Big\|\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]-\mu\_{h}(x,a)\Big\|\Delta+\Big\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]-\Sigma\_{h}(x,a)\Big\|\frac{\sqrt{\Delta}}{\sqrt{\lambda}}. |  |

With the above inequality, we quantify the following difference:

|  |  |  |
| --- | --- | --- |
|  | |𝔼X∼T¯hk(⋅|B)​[Vh+1∗​(X)]−𝔼Y∼Th(⋅|x,a)​[Vh+1∗​(Y)]|.\displaystyle\left|\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[V\_{h+1}^{\*}(X)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(Y)]\right|. |  |

To do so, we characterize the concentration inequality of the transition kernels, for which we define the following function T-UCBhk​(B)\mbox{\rm T-UCB}\_{h}^{k}(B) to represent the uncertainty in the transition kernel. Specifically, for all (h,k)∈[H]×[K],B∈𝒫hk(h,k)\in[H]\times[K],B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | T-UCBhk​(B)\displaystyle\mbox{\rm T-UCB}\_{h}^{k}(B) | :=\displaystyle:= | LV(δ,∥x~(oB)∥)×(κμ(δ,∥x~(oB)∥,nhk(B))Δ+Δ32λκμ(δ,∥x~(oB)∥,nhk(B))2\displaystyle L\_{V}(\delta,\|\tilde{x}(^{o}B)\|)\times\Bigg(\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\Delta+\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{2} |  |
|  |  |  | +d𝒮​Δ12λκΣ(δ,∥x~(oB)∥,nhk(B))),h<H,\displaystyle+\frac{\sqrt{d\_{\mathcal{S}}}\Delta^{\frac{1}{2}}}{\sqrt{\lambda}}\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\Bigg),\quad h<H, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | T-UCBHk​(B)\displaystyle\mbox{\rm T-UCB}\_{H}^{k}(B) | :=\displaystyle:= | 0,\displaystyle 0, |  | (4.11) |

where the function LV:(0,1]×(ℝ+∪{0})↦ℝ+L\_{V}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | LV​(δ,y)\displaystyle L\_{V}(\delta,y) | :=\displaystyle:= | 3C¯max(1+C~(m,d𝒮)(2m((nκμ(δ,y,n))m+η(y)m)Δm\displaystyle\sqrt{3}\,\overline{C}\_{\max}\Bigg(1+{\widetilde{C}(m,d\_{\mathcal{S}})}\Bigg(2^{m}\Big((\sqrt{n}\,\,\kappa\_{\mu}(\delta,y,n))^{m}+\eta(y)^{m}\Big)\Delta^{m} |  | (4.12) |
|  |  |  | +3m2​((n​κμ​(δ,y,n))m​Δm2+(n​κΣ​(δ,y,n))m2+(η​(y)2+L2​D2​Δ)m2)​Δm2\displaystyle\quad+3^{\frac{m}{2}}\Big((\sqrt{n}\,\,\kappa\_{\mu}(\delta,y,n))^{m}\Delta^{\frac{m}{2}}+(\sqrt{n}\,\,\kappa\_{\Sigma}(\delta,y,n))^{\frac{m}{2}}+\Big(\eta(y)^{2}+L^{2}D^{2}\Delta\Big)^{\frac{m}{2}}\Big)\Delta^{\frac{m}{2}} |  |
|  |  |  | +η(y)mΔm+η(y)mΔm2))\displaystyle\quad+\eta(y)^{m}\Delta^{m}+\eta(y)^{m}\Delta^{\frac{m}{2}}\Bigg)\Bigg) |  |

with the constant C¯m​a​x\overline{C}\_{max} and C~​(m,d𝒮)\widetilde{C}(m,d\_{\mathcal{S}}) defined by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | C¯max\displaystyle\overline{C}\_{\max} | :=\displaystyle:= | maxh∈[H]⁡C¯h,\displaystyle\max\_{h\in[H]}\overline{C}\_{h}, |  | (4.13) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | C~​(m,d𝒮)\displaystyle\widetilde{C}(m,d\_{\mathcal{S}}) | :=\displaystyle:= | d𝒮34​m+1​23​m−12​Γ​(m+12)12π14.\displaystyle d\_{\mathcal{S}}^{\frac{3}{4}m+1}2^{\frac{3m-1}{2}}\frac{\Gamma(m+\frac{1}{2})^{\frac{1}{2}}}{\pi^{\frac{1}{4}}}. |  | (4.14) |

Hence, we can bound the difference of expected value functions using the T-UCB function.

###### Theorem 4.4.

Assume Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")
holds. With probability at least 1−2​δ1-2\delta, we have that, for any (h,k)∈[H−1]×[K](h,k)\in[H-1]\times[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and (x,a)∈B(x,a)\in B:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |𝔼X∼T¯hk(⋅|B)​[Vh+1∗​(X)]−𝔼Y∼Th(⋅|x,a)​[Vh+1∗​(Y)]|\displaystyle\left|\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[V\_{h+1}^{\*}(X)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(Y)]\right| |  |
|  |  | ≤\displaystyle\leq | T-UCBhk(B)+LV(δ,∥x~(oB)∥)(∥𝔼¯[μ^hk(B)]−μh(x,a)∥Δ+∥𝔼¯[Σ~hk(B)]−Σh(x,a)∥Δλ).\displaystyle\mbox{\rm T-UCB}\_{h}^{k}(B)+L\_{V}(\delta,\|\tilde{x}(^{o}B)\|)\,\,\Big(\Big\|\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]-\mu\_{h}(x,a)\Big\|\Delta+\Big\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]-\Sigma\_{h}(x,a)\Big\|\frac{\sqrt{\Delta}}{\sqrt{\lambda}}\Big). |  |

The proof of Theorem [4.4](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [B.6](https://arxiv.org/html/2512.14991v1#A2.SS6 "B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

### 4.3 Concentration on reward estimators and properties of adaptive partition

We construct the estimator of the reward for any (h,k)∈[H]×[K](h,k)\in[H]\times[K] and B∈𝒫hkB\in\mathcal{P}\_{h}^{k}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | R^hk​(B)\displaystyle\widehat{R}\_{h}^{k}(B) | =\displaystyle= | ∑i=1nhk​(B)rhkinhk​(B),if​nhk​(B)>0,\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}r\_{h}^{k\_{i}}}{n\_{h}^{k}(B)},\quad\mbox{if}\,\,n\_{h}^{k}(B)>0, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | R^hk​(B)\displaystyle\widehat{R}\_{h}^{k}(B) | =\displaystyle= | 0,if​nhk​(B)=0,\displaystyle 0,\quad\mbox{if}\,\,n\_{h}^{k}(B)=0, |  | (4.16) |

where rhkir\_{h}^{k\_{i}} are the corresponding instantaneous rewards received in episode kik\_{i} at step hh.

We then characterize the concentration inequality for reward estimation, introducing R-UCBhk​(B)\mbox{\rm R-UCB}\_{h}^{k}(B) to quantify the associated uncertainty. Specifically, for all (h,k)∈[H]×[K](h,k)\in[H]\times[K] and all B∈𝒫hkB\in\mathcal{P}\_{h}^{k}, we define R-UCBhk​(B)\mbox{\rm R-UCB}\_{h}^{k}(B) as follows when nhk​(B)>0n\_{h}^{k}(B)>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R-UCBhk​(B):=log⁡(2​H​K2δ)​θnhk​(B),\displaystyle\mbox{\rm R-UCB}\_{h}^{k}(B):=\sqrt{\frac{\log(\frac{2HK^{2}}{\delta})\,\theta}{n\_{h}^{k}(B)}}, |  | (4.17) |

with θ\theta defined in ([2.6](https://arxiv.org/html/2512.14991v1#S2.E6 "In Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Theorem 4.5.

Under Assumption [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), It holds with probability at least 1−δ1-\delta that, for any (h,k)∈[H]×[K],B∈𝒫hk(h,k)\in[H]\times[K],B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and any (x,a)∈B(x,a)\in B,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |R^hk​(B)−R¯h​(x,a)|≤R-UCBhk​(B)+|∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)−R¯h​(x,a)|.\displaystyle|\widehat{R}\_{h}^{k}(B)-\bar{R}\_{h}(x,a)|\leq\mbox{\rm R-UCB}\_{h}^{k}(B)+\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\bar{R}\_{h}(x,a)\right|. |  | (4.18) |

###### Proof.

For fixed h,kh,k and B∈𝒫hkB\in\mathcal{P}\_{h}^{k} such that nhk​(B)>0n\_{h}^{k}(B)>0, by sub-Gaussian assumption of expected reward in ([2.6](https://arxiv.org/html/2512.14991v1#S2.E6 "In Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |
| --- | --- | --- |
|  | ℙ¯​(|∑i=1nhk​(B)rhkinhk​(B)−∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)|≥R-UCBhk​(B))≤δH​K2.\displaystyle\overline{\mathbb{P}}\Bigg(\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}r\_{h}^{k\_{i}}}{n\_{h}^{k}(B)}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\right|\geq\mbox{\rm R-UCB}\_{h}^{k}(B)\Bigg)\leq\frac{\delta}{HK^{2}}. |  |

Taking expectations we get:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|∑i=1nhk​(B)rhkinhk​(B)−∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)|≥R-UCBhk​(B))≤δH​K2.\displaystyle\mathbb{P}\Bigg(\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}r\_{h}^{k\_{i}}}{n\_{h}^{k}(B)}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\right|\geq\mbox{\rm R-UCB}\_{h}^{k}(B)\Bigg)\leq\frac{\delta}{HK^{2}}. |  |

Then we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ℙ(∩h=1H∩k=1K∩B∈𝒫hk,nhk​(B)>0{|∑i=1nhk​(B)rhkinhk​(B)−∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)|≤R-UCBhk(B)})\displaystyle\mathbb{P}\Bigg(\cap\_{h=1}^{H}\cap\_{k=1}^{K}\cap\_{B\in\mathcal{P}\_{h}^{k},n\_{h}^{k}(B)>0}\Bigg\{\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}r\_{h}^{k\_{i}}}{n\_{h}^{k}(B)}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\right|\leq\mbox{\rm R-UCB}\_{h}^{k}(B)\Bigg\}\Bigg) |  | (4.19) |
|  |  | =\displaystyle= | ℙ(∩h=1H∩k=1K∩nhk​(Bhk)=1K{|∑i=1nhk​(Bhk)rhkinhk​(Bhk)−∑i=1nhk​(Bhk)R¯h​(Xhki,Ahki)nhk​(Bhk)|≤log⁡(2​H​K2δ)​θnhk​(Bhk)})\displaystyle\mathbb{P}\Bigg(\cap\_{h=1}^{H}\cap\_{k=1}^{K}\cap\_{n\_{h}^{k}(B\_{h}^{k})=1}^{K}\Bigg\{\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B\_{h}^{k})}r\_{h}^{k\_{i}}}{n\_{h}^{k}(B\_{h}^{k})}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B\_{h}^{k})}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B\_{h}^{k})}\right|\leq\sqrt{\frac{\log(\frac{2HK^{2}}{\delta})\,\theta}{n\_{h}^{k}(B\_{h}^{k})}}\Bigg\}\Bigg) |  |
|  |  | ≥\displaystyle\geq | 1−∑h=1H∑k=1K∑nhk​(Bhk)=1Kℙ​(|∑i=1nhk​(Bhk)rhkinhk​(Bhk)−∑i=1nhk​(Bhk)R¯h​(Xhki,Ahki)nhk​(Bhk)|≥log⁡(2​H​K2δ)​θnhk​(Bhk))\displaystyle 1-\sum\_{h=1}^{H}\sum\_{k=1}^{K}\sum\_{n\_{h}^{k}(B\_{h}^{k})=1}^{K}\mathbb{P}\Bigg(\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B\_{h}^{k})}r\_{h}^{k\_{i}}}{n\_{h}^{k}(B\_{h}^{k})}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B\_{h}^{k})}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B\_{h}^{k})}\right|\geq\sqrt{\frac{\log(\frac{2HK^{2}}{\delta})\,\theta}{n\_{h}^{k}(B\_{h}^{k})}}\Bigg) |  |
|  |  | ≥\displaystyle\geq | 1−δ,\displaystyle 1-\delta, |  |

where BhkB\_{h}^{k} is selected according to Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). The first equality holds since only the estimate of selected block BhkB\_{h}^{k} is updated for each (h,k)(h,k) pair. The first inequality holds since for a countable sets of events {Ei}\{E\_{i}\} we have ℙ​(∩iEi)≥1−∑iℙ​(Ei∁)\mathbb{P}(\cap\_{i}E\_{i})\geq 1-\sum\_{i}\mathbb{P}(E\_{i}^{\complement}).

Furthermore, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |R^hk​(B)−R¯h​(x,a)|\displaystyle|\widehat{R}\_{h}^{k}(B)-\bar{R}\_{h}(x,a)| |  |
|  |  | ≤\displaystyle\leq | |∑i=1nhk​(B)rhkinhk​(B)−∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)|+|∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)−R¯h​(x,a)|.\displaystyle\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}r\_{h}^{k\_{i}}}{n\_{h}^{k}(B)}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\right|+\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\bar{R}\_{h}(x,a)\right|. |  |

Combine ([4.19](https://arxiv.org/html/2512.14991v1#S4.E19 "In 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([4.3](https://arxiv.org/html/2512.14991v1#S4.Ex28 "4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we verify that the desirable result in ([4.18](https://arxiv.org/html/2512.14991v1#S4.E18 "In Theorem 4.5. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds.
∎

To upper bound R-UCBhk​(B)+T-UCBhk​(B)\mbox{\rm R-UCB}\_{h}^{k}(B)+\mbox{\rm T-UCB}\_{h}^{k}(B), we construct the confidence of a block by

|  |  |  |  |
| --- | --- | --- | --- |
|  | CONFhk​(B)=g1(δ,∥x~(oB)∥)nhk​(B),\displaystyle{\rm CONF}\_{h}^{k}(B)=\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|)}{\sqrt{n\_{h}^{k}(B)}}, |  | (4.20) |

for all (h,k)∈[H]×[K],B∈𝒫hk(h,k)\in[H]\times[K],B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0. Here
g1:(0,1]×(ℝ+∪{0})↦ℝ+g\_{1}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g1(δ,y):=n(LV(δ,y)(κμ(δ,y,n)Δ+nΔ32λκμ(δ,y,n)2+d𝒮​Δ12λκΣ(δ,y,n))+log⁡(2​H​K2δ)​θn).g\_{1}(\delta,y):=\sqrt{n}\Big(L\_{V}(\delta,y)\,\,\Big(\kappa\_{\mu}(\delta,y,n)\Delta+\sqrt{n}\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}\kappa\_{\mu}(\delta,y,n)^{2}+\frac{\sqrt{d\_{\mathcal{S}}}\Delta^{\frac{1}{2}}}{\sqrt{\lambda}}\kappa\_{\Sigma}(\delta,y,n)\Big)+\sqrt{\frac{\log(\frac{2HK^{2}}{\delta})\,\theta}{n}}\Big). |  | (4.21) |

Next, we provide upper bounds for ∑i=1nhk​(B)diam​(Bhki)nhk​(B)\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)} and ∑i=1nhk​(B)diam​(Bhki)2nhk​(B)\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})^{2}}{n\_{h}^{k}(B)} with respect to diam​(B){\rm diam}(B). Note that the proof of Lemma [4.6](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") relies on the CONFhk​(B){\rm CONF}\_{h}^{k}(B) specified in ([4.20](https://arxiv.org/html/2512.14991v1#S4.E20 "In 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). We defer the full proof to Appendix [B.7](https://arxiv.org/html/2512.14991v1#A2.SS7 "B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Lemma 4.6.

For all (h,k)∈[H]×[K](h,k)\in[H]\times[K] and B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nhk​(B)diam​(Bhki)nhk​(B)≤4​diam​(B)​ and ​∑i=1nhk​(B)diam​(Bhki)2nhk​(B)≤4​D​diam​(B),\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\leq 4\,{\rm diam}(B)\,\,\mbox{ and }\,\,\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})^{2}}{n\_{h}^{k}(B)}\leq 4D\,{\rm diam}(B), |  | (4.22) |

where k1≤,⋯,≤knhk​(B)k\_{1}\leq,\cdots,\leq k\_{n\_{h}^{k}(B)} are the corresponding episode indices such that BB or its ancestors have been visited by Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

### 4.4 Bias of the estimators

Next, we provide upper bounds for ‖𝔼¯​[μ^hk​(B)]−μh​(x,a)‖​Δ+‖𝔼¯​[Σ~hk​(B)]−Σh​(x,a)‖​Δλ\Big\|\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]-\mu\_{h}(x,a)\Big\|\Delta+\Big\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]-\Sigma\_{h}(x,a)\Big\|\frac{\sqrt{\Delta}}{\sqrt{\lambda}}, for which we introduce T-BIAS​(B)\mbox{\rm T-BIAS}(B) to represent the block-wise bias in estimating the transition kernel

|  |  |  |
| --- | --- | --- |
|  | T-BIAS(B)=(8LΔ+16Lη(∥x~(oB)∥)Δλ+32L2DΔ32λ+128L2DΔ32λ)diam(B).\displaystyle\mbox{\rm T-BIAS}(B)=\Bigg(8L\Delta+16L\,\,\eta(\|\tilde{x}(^{o}B)\|)\frac{\sqrt{\Delta}}{\sqrt{\lambda}}+32L^{2}D\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}+128L^{2}D\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}\Bigg){\rm diam}(B). |  |

###### Theorem 4.7.

With the same assumptions as in Theorem [4.3](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), the following inequality holds for all h∈[H−1],k∈[K]h\in[H-1],k\in[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and any (x,a)∈B(x,a)\in B:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝔼¯​[μ^hk​(B)]−μh​(x,a)‖​Δ+‖𝔼¯​[Σ~hk​(B)]−Σh​(x,a)‖​Δλ≤T-BIAS​(B).\displaystyle\Big\|\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]-\mu\_{h}(x,a)\Big\|\Delta+\Big\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]-\Sigma\_{h}(x,a)\Big\|\frac{\sqrt{\Delta}}{\sqrt{\lambda}}\leq\mbox{\rm T-BIAS}(B). |  | (4.23) |

###### Proof.

Recall from Lemma [B.1](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1 Lemma B.1 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Lemma [B.2](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.2 Lemma B.2 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") that,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼¯​[μ^hk​(B)]\displaystyle\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)] | =\displaystyle= | ∑i=1nhk​(B)μh​(Xhki,Ahki)nhk​(B),\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼¯​[Σ~hk​(B)]\displaystyle\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)] | =\displaystyle= | ∑i=1nhk​(B)(Σh​(Xhki,Ahki)+(μh​(Xhki,Ahki)−𝔼¯​[μ^hk​(B)])​(μh​(Xhki,Ahki)−𝔼¯​[μ^hk​(B)])⊤​Δ)nhk​(B).\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Big(\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})+\big(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\big)\big(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\big)^{\top}\Delta\Big)}{n\_{h}^{k}(B)}. |  |

Then we have,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ‖𝔼¯​[μ^hk​(B)]−μh​(x,a)‖​Δ+‖𝔼¯​[Σ~hk​(B)]−Σh​(x,a)‖​Δλ\displaystyle\Big\|\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]-\mu\_{h}(x,a)\Big\|\Delta+\Big\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]-\Sigma\_{h}(x,a)\Big\|\frac{\sqrt{\Delta}}{\sqrt{\lambda}} |  | (4.24) |
|  |  | ≤\displaystyle\leq | ‖∑i=1nhk​(B)μh​(Xhki,Ahki)nhk​(B)−μh​(x,a)‖​Δ+‖∑i=1nhk​(B)Σh​(Xhki,Ahki)nhk​(B)−Σh​(x,a)‖​Δλ\displaystyle\,\,\Big\|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\mu\_{h}(x,a)\Big\|\Delta+\Big\|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\Sigma\_{h}(x,a)\Big\|\frac{\sqrt{\Delta}}{\sqrt{\lambda}} |  |
|  |  |  | +∑i=1nhk​(B)‖(μh​(Xhki,Ahki)−μh​(x,a)+μh​(x,a)−∑inhk​(B)μh​(Xhki,Ahki)nhk​(B))‖2nhk​(B)​Δ32λ\displaystyle\qquad+\sum\_{i=1}^{n\_{h}^{k}(B)}\frac{\Big\|(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\mu\_{h}(x,a)+\mu\_{h}(x,a)-\frac{\sum\_{i}^{n\_{h}^{k}(B)}\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)})\Big\|^{2}}{n\_{h}^{k}(B)}\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}} |  |
|  |  | ≤\displaystyle\leq | F0​Δ+(F1+2​F2+2​F3)​Δλ,\displaystyle F\_{0}\Delta+(F\_{1}+2F\_{2}+2F\_{3})\frac{\sqrt{\Delta}}{\sqrt{\lambda}}, |  |

in which

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | F0\displaystyle F\_{0} | =\displaystyle= | ‖∑i=1nhk​(B)μh​(Xhki,Ahki)nhk​(B)−μh​(x,a)‖,F1=‖∑i=1nhk​(B)Σh​(Xhki,Ahki)nhk​(B)−Σh​(x,a)‖,\displaystyle\Big\|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\mu\_{h}(x,a)\Big\|,\quad F\_{1}=\Big\|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\Sigma\_{h}(x,a)\Big\|, |  | (4.25) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F2\displaystyle F\_{2} | =\displaystyle= | ∑i=1nhk​(B)‖(μh​(Xhki,Ahki)−μh​(x,a))‖2nhk​(B)​Δ,F3=∑i=1nhk​(B)‖(μh​(x,a)−∑inhk​(B)μh​(Xhki,Ahki)nhk​(B))‖2nhk​(B)​Δ.\displaystyle\sum\_{i=1}^{n\_{h}^{k}(B)}\frac{\Big\|(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\mu\_{h}(x,a))\Big\|^{2}}{n\_{h}^{k}(B)}\Delta,\quad F\_{3}=\sum\_{i=1}^{n\_{h}^{k}(B)}\frac{\Big\|(\mu\_{h}(x,a)-\frac{\sum\_{i}^{n\_{h}^{k}(B)}\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)})\Big\|^{2}}{n\_{h}^{k}(B)}\Delta. |  |

For F0F\_{0} in ([4.25](https://arxiv.org/html/2512.14991v1#S4.E25 "In 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")),
since (x,a)(x,a) and (Xhki,Ahki)(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}}) lie in BhkiB\_{h}^{k\_{i}}, we have ‖μh​(Xhki,Ahki)−μh​(x,a)‖≤L​diam​(Bhki)\Big\|\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\mu\_{h}(x,a)\Big\|\leq L\,{\rm diam}(B\_{h}^{k\_{i}}). Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F0≤∑i=1nhk​(B)‖μh​(Xhki,Ahki)−μh​(x,a)‖nhk​(B)≤2​L​∑i=1nhk​(B)diam​(Bhki)nhk​(B).\displaystyle F\_{0}\leq\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Big\|\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\mu\_{h}(x,a)\Big\|}{n\_{h}^{k}(B)}\leq\frac{2L\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}. |  | (4.26) |

For F1F\_{1},
we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | F1\displaystyle F\_{1} | ≤\displaystyle\leq | ∑i=1nhk​(B)‖Σh​(Xhki,Ahki)−Σh​(x,a)‖nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Big\|\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\Sigma\_{h}(x,a)\Big\|}{n\_{h}^{k}(B)} |  | (4.27) |
|  |  | ≤\displaystyle\leq | ∑i=1nhk​(B)(‖σh​(Xhki,Ahki)‖+‖σh​(x,a)‖)​‖σh​(Xhki,Ahki)−σh​(x,a)‖nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Big(\Big\|\sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})\Big\|+\Big\|\sigma\_{h}(x,a)\Big\|\Big)\Big\|\sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\sigma\_{h}(x,a)\Big\|}{n\_{h}^{k}(B)} |  |
|  |  | ≤\displaystyle\leq | ∑i=1nhk​(B)2η(∥x~(oB)∥)∥σh(Xhki,Ahki)−σh(x,a)∥nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}2\eta(\|\tilde{x}(^{o}B)\|)\Big\|\sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\sigma\_{h}(x,a)\Big\|}{n\_{h}^{k}(B)} |  |
|  |  | ≤\displaystyle\leq | 4Lη(∥x~(oB)∥)∑i=1nhk​(B)diam​(Bhki)nhk​(B),\displaystyle 4L\,\,\eta(\|\tilde{x}(^{o}B)\|)\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}, |  |

where we used ([4.7](https://arxiv.org/html/2512.14991v1#S4.E7 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) in getting the third inequality of ([4.27](https://arxiv.org/html/2512.14991v1#S4.E27 "In 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

For F2F\_{2} and F3F\_{3}
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | F2≤4​L2​∑i=1nhk​(B)diam​(Bhki)2nhk​(B),F3≤(2​L​∑i=1nhk​(B)diam​(Bhki)nhk​(B))2,\displaystyle F\_{2}\leq\frac{4L^{2}\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})^{2}}{n\_{h}^{k}(B)},\quad F\_{3}\leq\left(2L\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\right)^{2}, |  | (4.28) |

Combining ([4.24](https://arxiv.org/html/2512.14991v1#S4.E24 "In 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([4.26](https://arxiv.org/html/2512.14991v1#S4.E26 "In 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([4.27](https://arxiv.org/html/2512.14991v1#S4.E27 "In 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([4.28](https://arxiv.org/html/2512.14991v1#S4.E28 "In 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([4.22](https://arxiv.org/html/2512.14991v1#S4.E22 "In Lemma 4.6. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")),
we get ([4.23](https://arxiv.org/html/2512.14991v1#S4.E23 "In Theorem 4.7. ‣ 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
∎

Then we derive upper bounds for |∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)−R¯h​(x,a)|\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\bar{R}\_{h}(x,a)\right|, for which we define R-BIAS​(B)\mbox{\rm R-BIAS}(B) to represent the block-wise bias in reward estimator

|  |  |  |
| --- | --- | --- |
|  | R-BIAS(B)=4Lm(∥x~(oB)∥)diam(B),\displaystyle\mbox{\rm R-BIAS}(B)=4L\_{m}(\|\tilde{x}(^{o}B)\|){\rm diam}(B), |  |

with Lm:ℝ+∪{0}↦ℝ+L\_{m}:\mathbb{R}\_{+}\cup\{0\}\mapsto\mathbb{R}\_{+} defined by

|  |  |  |
| --- | --- | --- |
|  | Lm​(y):=4​L​(1+2​(y+D)m).\displaystyle L\_{m}(y):=4L\Big(1+2(y+D)^{m}\Big). |  |

In Proposition [C.1](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem1 "Proposition C.1. ‣ C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") of Appendix [C.3](https://arxiv.org/html/2512.14991v1#A3.SS3 "C.3 Proof of Theorem 5.5 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we show that |∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)−R¯h​(x,a)|≤R-BIAS​(B)\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\bar{R}\_{h}(x,a)\right|\leq\mbox{\rm R-BIAS}(B) holds almost surely.

## 5 Regret analysis

In this section, we provide the regret analysis of the proposed adaptive partition framework.

### 5.1 Construction of value estimators

In this subsection, we construct estimators of the value functions.

To proceed, we first introduce a few notations. Define the block-wise bias consisting both the bias of transition estimator and the bias of reward estimator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | BIAS(B):=R-BIAS(B)+LV(δ,∥x~(oB)∥)T-BIAS(B):=g2(δ,∥x~(oB)∥)diam(B),\displaystyle{\rm BIAS}(B):=\mbox{\rm R-BIAS}(B)+L\_{V}(\delta,\|\tilde{x}(^{o}B)\|)\mbox{\rm T-BIAS}(B):=g\_{2}(\delta,\|\tilde{x}(^{o}B)\|){\rm diam}(B), |  | (5.1) |

with g2:(0,1]×(ℝ+∪{0})↦ℝg\_{2}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\mapsto\mathbb{R} defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g2​(δ,y):=(4​Lm​(y)+LV​(δ,y)​(8​L​Δ+16​L​η​(y)​Δλ+32​L2​D​Δ32λ+128​L2​D​Δ32λ)).\displaystyle g\_{2}(\delta,y):=\Bigg(4L\_{m}(y)+L\_{V}(\delta,y)\Big(8L\Delta+16L\,\eta(y)\frac{\sqrt{\Delta}}{\sqrt{\lambda}}+32L^{2}D\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}+128L^{2}D\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}\Big)\Bigg). |  | (5.2) |

Here η\eta is defined in ([4.7](https://arxiv.org/html/2512.14991v1#S4.E7 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), x~\tilde{x} is defined in ([4.5](https://arxiv.org/html/2512.14991v1#S4.E5 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), Bo{}^{o}B is defined in ([4.6](https://arxiv.org/html/2512.14991v1#S4.E6 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and LVL\_{V} is defined in ([4.12](https://arxiv.org/html/2512.14991v1#S4.E12 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

In addition, ∀(h,k)∈[H]×[K]\forall(h,k)\in[H]\times[K], let

|  |  |  |
| --- | --- | --- |
|  | Γ𝒮​(𝒫hk):=∪{B∈𝒫hk​s.t.∄​B′∈𝒫hk,Γ𝒮​(B′)⊊Γ𝒮​(B)}{Γ𝒮​(B)}\displaystyle\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k}):=\cup\_{\{B\in\mathcal{P}\_{h}^{k}\,\,{\rm s.t.}\,\,\nexists B^{\prime}\in\mathcal{P}\_{h}^{k},\Gamma\_{\mathcal{S}}(B^{\prime})\subsetneq\Gamma\_{\mathcal{S}}(B)\}}\{\Gamma\_{\mathcal{S}}(B)\} |  |

be the state partition induced by the current state-action partition 𝒫hk\mathcal{P}\_{h}^{k}.
For S∈Γ𝒮​(𝒫hk)S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k}), we overload the notation defined in ([4.5](https://arxiv.org/html/2512.14991v1#S4.E5 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), i.e., denote x~​(S)\tilde{x}(S) as the center of SS.

Finally, we set the local Lipschitz constant as follows, which will be used below in the construction of value function estimators

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ch:=max⁡{C¯h,2m+1​C~h},∀h∈[H],\displaystyle C\_{h}:=\max\Big\{\overline{C}\_{h},2^{m+1}\widetilde{C}\_{h}\Big\},\quad\forall h\in[H], |  | (5.3) |

where C¯h\overline{C}\_{h} is defined in ([2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and C~h\widetilde{C}\_{h} is defined in ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). It is worth emphasizing that such choice of local Lipschitz constant is necessary to guarantee the local Lipschitz property of V¯hk\overline{V}\_{h}^{k} which is formally stated in Theorem [5.3](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem3 "Theorem 5.3. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

##### Design of value estimators.

For k=0,h∈[H],B∈𝒫h0,S=Γ𝒮​(B)k=0,h\in[H],B\in\mathcal{P}\_{h}^{0},S=\Gamma\_{\mathcal{S}}(B), and x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}}, the function estimators are initialized with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Q¯h0​(B)\displaystyle\overline{Q}\_{h}^{0}(B) | :=\displaystyle:= | C~h(1+(∥x~(oB)∥+D)m+1),\displaystyle\widetilde{C}\_{h}(1+(\|\tilde{x}(^{o}B)\|+D)^{m+1}), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V~h0​(S)\displaystyle\widetilde{V}\_{h}^{0}(S) | :=\displaystyle:= | C~h​(1+(‖x~​(S)‖+D)m+1),\displaystyle\widetilde{C}\_{h}(1+(\|\tilde{x}(S)\|+D)^{m+1}), |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | V¯h0​(x)\displaystyle\overline{V}\_{h}^{0}(x) | :=\displaystyle:= | C~h​(1+‖x‖m+1).\displaystyle\widetilde{C}\_{h}(1+\|x\|^{m+1}). |  | (5.4) |

In addition, for (h,k)∈[H]×([K]∪{0})(h,k)\in[H]\times([K]\cup\{0\}), we set Q¯hk​(Z¯∁)\overline{Q}\_{h}^{k}(\bar{Z}^{\complement}) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q¯hk​(Z¯∁):=−C~h​(1+ρm+1).\displaystyle\overline{Q}\_{h}^{k}(\bar{Z}^{\complement}):=-\widetilde{C}\_{h}(1+\rho^{m+1}). |  | (5.5) |

Now we specify the following recursive definition with respect to k≥1k\geq 1. Specifically, at the terminal timestamp HH, for B∈𝒫HkB\in\mathcal{P}\_{H}^{k}, S∈Γ𝒮​(𝒫Hk)S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{H}^{k}), x∈𝒮1x\in\mathcal{S}\_{1}, we define

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Q¯Hk​(B)\displaystyle\overline{Q}\_{H}^{k}(B) | :=\displaystyle:= | {R^Hk​(B)+R-UCBHk​(B)+R-BIAS​(B) if ​nHk​(B)>0Q¯H0​(B) if ​nHk​(B)=0,\displaystyle\left\{\begin{array}[]{lll}\widehat{R}\_{H}^{k}(B)+\mbox{\rm R-UCB}\_{H}^{k}(B)+\mbox{\rm R-BIAS}(B)&&\mbox{ if }n\_{H}^{k}(B)>0\\ \overline{Q}\_{H}^{0}(B)&&\mbox{ if }n\_{H}^{k}(B)=0,\end{array}\right. |  | (5.8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V~Hk​(S)\displaystyle\widetilde{V}\_{H}^{k}(S) | :=\displaystyle:= | min⁡{V~Hk−1​(S),maxB∈𝒫Hk,S⊂Γ𝒮​(B)⁡Q¯Hk​(B)},\displaystyle\min\Big\{\widetilde{V}\_{H}^{k-1}(S),\max\_{B\in\mathcal{P}\_{H}^{k},S\subset\Gamma\_{\mathcal{S}}(B)}\overline{Q}\_{H}^{k}(B)\Big\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VH,klocal​(x,S)\displaystyle V\_{H,k}^{\rm local}(x,S) | :=\displaystyle:= | V~Hk​(S)+CH​(1+‖x‖m+‖x~​(S)‖m)​‖x−x~​(S)‖,\displaystyle\widetilde{V}\_{H}^{k}(S)+C\_{H}\Big(1+\|x\|^{m}+\|\tilde{x}(S)\|^{m}\Big)\|x-\tilde{x}(S)\|, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | V¯Hk​(x)\displaystyle\overline{V}\_{H}^{k}(x) | :=\displaystyle:= | minS∈Γ𝒮​(𝒫Hk)⁡VH,klocal​(x,S).\displaystyle\min\_{S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{H}^{k})}V\_{H,k}^{\rm local}(x,S). |  | (5.9) |

For x∈ℝd𝒮∖𝒮1x\in\mathbb{R}^{d\_{\mathcal{S}}}\setminus\mathcal{S}\_{1}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯Hk​(x):=V¯Hk​(ρ‖x‖​x)+CH​(1+‖x‖m+ρm)​‖(1−ρ‖x‖)​x‖.\displaystyle\overline{V}\_{H}^{k}(x):=\overline{V}\_{H}^{k}\left(\frac{\rho}{\|x\|}x\right)+C\_{H}(1+\|x\|^{m}+\rho^{m})\left\|\left(1-\frac{\rho}{\|x\|}\right)x\right\|. |  | (5.10) |

Note that this extrapolation ensures the continuity of V¯Hk\overline{V}\_{H}^{k} on the entire state space.

Similarly, we define the values for h<Hh<H. For B∈𝒫hkB\in\mathcal{P}\_{h}^{k},S∈Γ𝒮​(𝒫hk)S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k}), x∈𝒮1x\in\mathcal{S}\_{1} we define

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Q¯hk​(B)\displaystyle\overline{Q}\_{h}^{k}(B) | :=\displaystyle:= | {R^hk​(B)+R-UCBhk​(B)+𝔼X∼T¯hk(⋅|B)​[V¯h+1k​(X)]+T-UCBhk​(B)+BIAS​(B)if ​nhk​(B)>0Q¯h0​(B)if ​nhk​(B)=0,\displaystyle\left\{\begin{array}[]{lll}\widehat{R}\_{h}^{k}(B)+\mbox{\rm R-UCB}\_{h}^{k}(B)+\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\overline{V}\_{h+1}^{k}(X)]\\ +\mbox{\rm T-UCB}\_{h}^{k}(B)+{\rm BIAS}(B)&&\mbox{if }n\_{h}^{k}(B)>0\\ \overline{Q}\_{h}^{0}(B)&&\mbox{if }n\_{h}^{k}(B)=0,\end{array}\right. |  | (5.12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V~hk​(S)\displaystyle\widetilde{V}\_{h}^{k}(S) | :=\displaystyle:= | min⁡{V~hk−1​(S),maxB∈𝒫hk,S⊂Γ𝒮​(B)⁡Q¯hk​(B)},\displaystyle\min\Big\{\widetilde{V}\_{h}^{k-1}(S),\max\_{B\in\mathcal{P}\_{h}^{k},S\subset\Gamma\_{\mathcal{S}}(B)}\overline{Q}\_{h}^{k}(B)\Big\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vh,klocal​(x,S)\displaystyle V\_{h,k}^{\rm local}(x,S) | :=\displaystyle:= | V~hk​(S)+Ch​(1+‖x‖m+‖x~​(S)‖m)​‖x−x~​(S)‖,\displaystyle\widetilde{V}\_{h}^{k}(S)+C\_{h}\Big(1+\|x\|^{m}+\|\tilde{x}(S)\|^{m}\Big)\|x-\tilde{x}(S)\|, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | V¯hk​(x)\displaystyle\overline{V}\_{h}^{k}(x) | :=\displaystyle:= | minS∈Γ𝒮​(𝒫hk)⁡Vh,klocal​(x,S).\displaystyle\min\_{S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k})}V\_{h,k}^{\rm local}(x,S). |  | (5.13) |

Finally, for x∈ℝd𝒮∖𝒮1x\in\mathbb{R}^{d\_{\mathcal{S}}}\setminus\mathcal{S}\_{1}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯hk​(x):=V¯hk​(ρ‖x‖​x)+Ch​(1+‖x‖m+ρm)​‖(1−ρ‖x‖)​x‖.\displaystyle\overline{V}\_{h}^{k}(x):=\overline{V}\_{h}^{k}\left(\frac{\rho}{\|x\|}x\right)+C\_{h}(1+\|x\|^{m}+\rho^{m})\left\|\left(1-\frac{\rho}{\|x\|}\right)x\right\|. |  | (5.14) |

###### Remark 5.1 (Role of Vh,klocalV^{\rm local}\_{h,k}).

We design
Vh,klocal(.,S)V^{\rm local}\_{h,k}(.,S) as a locally Lipschitz extension of the estimate for SS across the entire state space. The local Lipschitz property plays a key role in establishing concentration bounds associated with V¯hk\overline{V}\_{h}^{k}. This is formalized in Corollary [5.4](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem4 "Corollary 5.4. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

The update formulas ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))-([5.14](https://arxiv.org/html/2512.14991v1#S5.E14 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) correspond to a value iteration step, where the true rewards and transition kernels in the Bellman equation ([2.1](https://arxiv.org/html/2512.14991v1#S2.Ex5 "Bellman equation for generic policy. ‣ 2.1 Value function, Bellman equations and evaluation criterion ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) are replaced by their respective estimators. The terms R-UCBhk​(B)\mbox{\rm R-UCB}\_{h}^{k}(B), T-UCBhk​(B)\mbox{\rm T-UCB}\_{h}^{k}(B), and BIAS​(B){\rm BIAS}(B) serve as bonus terms that account for uncertainty in reward estimation, uncertainty in transition kernel estimation, and partition biases, respectively.

Below we show that the value estimators Q¯hk\overline{Q}\_{h}^{k}, V~hk\widetilde{V}\_{h}^{k}, and V¯hk\overline{V}\_{h}^{k} defined in ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))-([5.14](https://arxiv.org/html/2512.14991v1#S5.E14 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) serve as upper bounds of the true value functions.

###### Theorem 5.2.

Under Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), with probability at least 1−3​δ1-3\delta, it holds that for all (h,k)∈[H]×[K](h,k)\in[H]\times[K],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Q¯hk​(B)\displaystyle\overline{Q}\_{h}^{k}(B) | ≥\displaystyle\geq | Qh∗​(x,a),for all B∈𝒫hk and (x,a)∈B,\displaystyle Q\_{h}^{\*}(x,a),\,\,\mbox{for all $B\in\mathcal{P}\_{h}^{k}$ and $(x,a)\in B$}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V~hk​(S)\displaystyle\widetilde{V}\_{h}^{k}(S) | ≥\displaystyle\geq | Vh∗​(x),for all S∈Γ𝒮​(𝒫hk) and x∈S,\displaystyle V\_{h}^{\*}(x),\,\,\mbox{for all $S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k})$ and $x\in S$}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | V¯hk​(x)\displaystyle\overline{V}\_{h}^{k}(x) | ≥\displaystyle\geq | Vh∗​(x),for all x∈ℝd𝒮.\displaystyle V\_{h}^{\*}(x),\,\,\mbox{for all $x\in\mathbb{R}^{d\_{\mathcal{S}}}$}. |  | (5.15) |

The proof of Theorem [5.2](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem2 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.1](https://arxiv.org/html/2512.14991v1#A3.SS1 "C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

Next, we show that the estimated value functions satisfy a local Lipschitz property.

###### Theorem 5.3.

Under Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), with probability at least 1−3​δ1-3\delta, for all (h,k)∈[H]×[K](h,k)\in[H]\times[K], x1,x2∈ℝd𝒮x\_{1},x\_{2}\in\mathbb{R}^{d\_{\mathcal{S}}},

|  |  |  |
| --- | --- | --- |
|  | |V¯hk​(x1)−V¯hk​(x2)|≤C^h​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖,\displaystyle\Big|\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})\Big|\leq\widehat{C}\_{h}\Big(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m}\Big)\|x\_{1}-x\_{2}\|, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^h:=C^h​(m,Ch,C~h,D),\displaystyle\widehat{C}\_{h}:=\widehat{C}\_{h}(m,C\_{h},\widetilde{C}\_{h},D), |  | (5.16) |

with ChC\_{h} defined in ([5.3](https://arxiv.org/html/2512.14991v1#S5.E3 "In 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and C~h\widetilde{C}\_{h} defined in ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Note that the initialization in ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), together with the subsequently constructed value estimates in ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"))–([5.14](https://arxiv.org/html/2512.14991v1#S5.E14 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), plays a pivotal role in establishing the local Lipschitz property. The proof underscores the challenges and complexities introduced by the polynomial structure inherent to our setting, which is different from (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)). The detailed proof of Theorem [5.3](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem3 "Theorem 5.3. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is provided in Appendix [C.2](https://arxiv.org/html/2512.14991v1#A3.SS2 "C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

Applying Lemma [B.4](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem4 "Lemma B.4. ‣ B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") in the same fashion as in the proof of Theorem [4.4](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") yields the following corollary.

###### Corollary 5.4.

Assume the same assumptions as in Theorem [4.4](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). With probability at least 1−2​δ1-2\delta, for any (h,k)∈[H−1]×[K],B∈𝒫hk(h,k)\in[H-1]\times[K],B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and any (x,a)∈B(x,a)\in B, we have the following:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | |𝔼X∼T¯hk(⋅|B)​[V¯h+1k​(X)]−𝔼Y∼Th(⋅|x,a)​[V¯h+1k​(Y)]|\displaystyle\left|\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[\overline{V}\_{h+1}^{k}(Y)]\right| |  | (5.17) |
|  |  | ≤\displaystyle\leq | C^maxC¯max(T-UCBhk(B)+LV(δ,∥x~(oB)∥)T-BIAS(B)),\displaystyle\,\,\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm T-UCB}\_{h}^{k}(B)+L\_{V}(\delta,\|\tilde{x}(^{o}B)\|)\,\,\mbox{\rm T-BIAS}(B)\Big), |  |

where C^max:=maxh∈[H]⁡C^h\widehat{C}\_{\max}:=\max\_{h\in[H]}\widehat{C}\_{h} with C^h\widehat{C}\_{h} defined in ([5.16](https://arxiv.org/html/2512.14991v1#S5.E16 "In Theorem 5.3. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C¯max\overline{C}\_{\max} in ([4.13](https://arxiv.org/html/2512.14991v1#S4.E13 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), x~\tilde{x} in ([4.5](https://arxiv.org/html/2512.14991v1#S4.E5 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), Bo{}^{o}B in ([4.6](https://arxiv.org/html/2512.14991v1#S4.E6 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and LVL\_{V} in ([4.12](https://arxiv.org/html/2512.14991v1#S4.E12 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

We then bound the difference between the Q-estimators and the true Q-functions in the following Theorem [5.5](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem5 "Theorem 5.5. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Proposition [5.6](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem6 "Proposition 5.6. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Theorem 5.5.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. The following inequality holds with probability at least 1−3​δ1-3\delta, for any (h,k)∈[H]×[K](h,k)\in[H]\times[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0 , and (x,a)∈B(x,a)\in B,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Q¯Hk​(B)−QH∗​(x,a)\displaystyle\overline{Q}\_{H}^{k}(B)-Q\_{H}^{\*}(x,a) | ≤\displaystyle\leq | 2​C^maxC¯max​(R-UCBHk​(B)+R-BIAS​(B));\displaystyle 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{H}^{k}(B)+\mbox{\rm R-BIAS}(B)\Big); |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Q¯hk​(B)−Qh∗​(x,a)\displaystyle\overline{Q}\_{h}^{k}(B)-Q\_{h}^{\*}(x,a) | ≤\displaystyle\leq | 2​C^maxC¯max​(R-UCBhk​(B)+T-UCBhk​(B)+BIAS​(B))\displaystyle 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{h}^{k}(B)+\mbox{\rm T-UCB}\_{h}^{k}(B)+{\rm BIAS}(B)\Big) |  | (5.18) |
|  |  |  | +𝔼X∼Th(⋅|x,a)​[V¯h+1k​(X)]−𝔼X∼Th(⋅|x,a)​[Vh+1∗​(X)],h<H.\displaystyle+\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(X)],h<H. |  |

The proof of Theorem [5.5](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem5 "Theorem 5.5. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.3](https://arxiv.org/html/2512.14991v1#A3.SS3 "C.3 Proof of Theorem 5.5 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Proposition 5.6.

Assume that Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. For any (h,k)∈[H]×[K](h,k)\in[H]\times[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)=0n\_{h}^{k}(B)=0, (x,a)∈B(x,a)\in B,
the following inequality holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q¯hk(B)−Qh∗(x,a)≤2C~hD(1+(∥x~(oB)∥+D)m+1)diam(B),\displaystyle\overline{Q}\_{h}^{k}(B)-Q\_{h}^{\*}(x,a)\leq 2\frac{\widetilde{C}\_{h}}{D}(1+(\|\tilde{x}(^{o}B)\|+D)^{m+1}){\rm diam}(B), |  | (5.19) |

where C~h\widetilde{C}\_{h} is defined in ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

The proof of Proposition [5.6](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem6 "Proposition 5.6. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.4](https://arxiv.org/html/2512.14991v1#A3.SS4 "C.4 Proof of Proposition 5.6 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

We also have the following bounds on value function estimators evaluated at XhkX\_{h}^{k}.

###### Proposition 5.7.

For any (h,k)∈[H]×[K](h,k)\in[H]\times[K], conditioned on Xhk∈𝒮1X\_{h}^{k}\in\mathcal{S}\_{1}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯hk−1(Xhk)≤Q¯hk−1(Bhk)+Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk),\displaystyle\overline{V}\_{h}^{k-1}(X\_{h}^{k})\leq\overline{Q}\_{h}^{k-1}(B\_{h}^{k})+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}), |  | (5.20) |

where BhkB\_{h}^{k} is selected according to Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Bhko{}^{o}B\_{h}^{k} is defined in ([4.6](https://arxiv.org/html/2512.14991v1#S4.E6 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

The proof of Proposition [5.7](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem7 "Proposition 5.7. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.5](https://arxiv.org/html/2512.14991v1#A3.SS5 "C.5 Proof of Proposition 5.7 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

### 5.2 Upper bound via clipping

In this subsection, we use the Clipping method (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53), Section E) to obtain an upper bound for

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δh(k):=V¯hk−1​(Xhk)−Vhπ~k​(Xhk),\displaystyle\Delta\_{h}^{(k)}:=\overline{V}\_{h}^{k-1}(X\_{h}^{k})-V\_{h}^{\tilde{\pi}^{k}}(X\_{h}^{k}), |  | (5.21) |

with terminal condition ΔH+1(k)=0\Delta\_{H+1}^{(k)}=0. Here {π~k}k∈[K]\{\tilde{\pi}^{k}\}\_{k\in[K]} is defined in ([3.4](https://arxiv.org/html/2512.14991v1#S3.E4 "In Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). he upper bound of Δh(k)\Delta\_{h}^{(k)} will play an important role in controlling the final regret bound.

The clip function is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | CLIP​(ν1|ν2):=ν1​𝕀ν1≥ν2,∀ν1,ν2∈ℝ.\displaystyle{\rm CLIP}(\nu\_{1}|\nu\_{2}):=\nu\_{1}\mathbb{I}\_{\nu\_{1}\geq\nu\_{2}},\forall\nu\_{1},\nu\_{2}\in\mathbb{R}. |  | (5.22) |

Intuitively, ν2\nu\_{2} is used to clip ν1\nu\_{1}, as it takes the value of ν1\nu\_{1} if and only if ν1≥ν2\nu\_{1}\geq\nu\_{2} and its value is zero otherwise.

Before proceeding, we introduce a few useful notations:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | G~​aph​(x,a)\displaystyle{\rm\widetilde{G}ap}\_{h}(x,a) | :=\displaystyle:= | Vh∗​(x)−Qh∗​(x,a);\displaystyle V\_{h}^{\*}(x)-Q\_{h}^{\*}(x,a); |  | (5.23) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Gaph​(B)\displaystyle{\rm Gap}\_{h}(B) | :=\displaystyle:= | min(x,a)∈B⁡G~​aph​(x,a);\displaystyle\min\_{(x,a)\in B}{\rm\widetilde{G}ap}\_{h}(x,a); |  | (5.24) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | fh+1k−1​(Xhk,Ahk)\displaystyle f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k}) | :=\displaystyle:= | 𝔼Y∼Th(⋅|Xhk,Ahk)​[V¯h+1k−1​(Y)]−𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1∗​(Y)],h<H,\displaystyle\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[\overline{V}\_{h+1}^{k-1}(Y)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\*}(Y)],h<H, |  | (5.25) |

with terminal fH+1k−1​(XHk,AHk)=0f\_{H+1}^{k-1}(X\_{H}^{k},A\_{H}^{k})=0.

Also, to further ease the notation, for (h,k)∈[H]×[K],Bhk∈𝒫hk−1(h,k)\in[H]\times[K],B\_{h}^{k}\in\mathcal{P}\_{h}^{k-1} we denote:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Ghk​(Bhk)\displaystyle G\_{h}^{k}(B\_{h}^{k}) | :=\displaystyle:= | {2C~hD(1+(∥x~(oBhk)∥+D)m+1)diam(Bhk),ifh∈[H],nhk−1(Bhk)=0,k≥1;2​C^maxC¯max​(R-UCBhk−1​(Bhk)+T-UCBhk−1​(Bhk)+BIAS​(Bhk))+Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk),ifh<H,nhk−1(Bhk)>0,k>1;2​C^maxC¯max​(R-UCBhk−1​(Bhk)+R-BIAS​(Bhk))+Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk),ifh=H,nhk−1(Bhk)>0,k>1,\displaystyle\left\{\begin{array}[]{lll}2\frac{\widetilde{C}\_{h}}{D}(1+(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m+1}){\rm diam}(B\_{h}^{k}),\,\,\,\,\mbox{if}\,\,h\in[H],n\_{h}^{k-1}(B\_{h}^{k})=0,k\geq 1;\\ 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{h}^{k-1}(B\_{h}^{k})+\mbox{\rm T-UCB}\_{h}^{k-1}(B\_{h}^{k})+{\rm BIAS}(B\_{h}^{k})\Big)\\ +C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}),\,\,\,\,\mbox{if}\,\,h<H,n\_{h}^{k-1}(B\_{h}^{k})>0,k>1;\\ 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{h}^{k-1}(B\_{h}^{k})+\mbox{\rm R-BIAS}(B\_{h}^{k})\Big)\\ +C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}),\,\,\,\,\mbox{if}\,\,h=H,n\_{h}^{k-1}(B\_{h}^{k})>0,k>1,\end{array}\right. |  | (5.31) |

where x~\tilde{x} is defined in ([4.5](https://arxiv.org/html/2512.14991v1#S4.E5 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C~h\widetilde{C}\_{h} in ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ChC\_{h} in ([5.3](https://arxiv.org/html/2512.14991v1#S5.E3 "In 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C¯max\overline{C}\_{\max} in ([4.13](https://arxiv.org/html/2512.14991v1#S4.E13 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C^max\widehat{C}\_{\max} in ([5.17](https://arxiv.org/html/2512.14991v1#S5.E17 "In Corollary 5.4. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). In addition, BhkB\_{h}^{k} is selected according to Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Bhko{}^{o}B\_{h}^{k} is defined in ([4.6](https://arxiv.org/html/2512.14991v1#S4.E6 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Remark 5.8 (Role of Ghk​(Bhk)G\_{h}^{k}(B\_{h}^{k})).

We remark that Ghk​(Bhk)G\_{h}^{k}(B\_{h}^{k}) represents the overall bonus terms and bias of the estimate w.r.t the selected block BhkB\_{h}^{k}. By "clipping" it with the gap term, it provides a useful upper bound for us to control the final regret; see more analysis in Lemma [5.17](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem17 "Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Theorem 5.9.

Suppose Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. With probability at least 1−3​δ1-3\delta, for all (h,k)∈[H]×[K](h,k)\in[H]\times[K], Bhk∈𝒫hk−1B\_{h}^{k}\in\mathcal{P}\_{h}^{k-1}, we have that:

|  |  |  |
| --- | --- | --- |
|  | Δh(k)≤CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+(1+1H)​fh+1k−1​(Xhk,Ahk)+Qh∗​(Xhk,Ahk)−Vhπ~k​(Xhk).\displaystyle\Delta\_{h}^{(k)}\leq{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\,\,\Bigg|\,\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+\Big(1+\frac{1}{H}\Big)f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k})+Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k})-V\_{h}^{\tilde{\pi}^{k}}(X\_{h}^{k}). |  |

The proof of Theorem [5.9](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem9 "Theorem 5.9. ‣ 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.6](https://arxiv.org/html/2512.14991v1#A3.SS6 "C.6 Proof of Theorem 5.9 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

### 5.3 Concentrations on the size of JρKJ\_{\rho}^{K} and initial value function

In this subsection, we provide some useful concentrations before establishing the final regret bound.

We categorize the sample trajectories into two types: those remains within 𝒮1\mathcal{S}\_{1} for the entire episode, denoted by

|  |  |  |  |
| --- | --- | --- | --- |
|  | JρK:={k∈[K]:maxh∈[H]⁡‖Xhk‖≤ρ},\displaystyle J\_{\rho}^{K}:=\left\{k\in[K]:\max\_{h\in[H]}\|X\_{h}^{k}\|\leq\rho\right\}, |  | (5.32) |

and those
exceeds 𝒮1\mathcal{S}\_{1}.
We also denote

|  |  |  |
| --- | --- | --- |
|  | Ik:=𝕀{k∈JρK},pρk=ℙ​(k∈JρK)=𝔼​[Ik],andK0=∑k=1KIk=|JρK|.\displaystyle I\_{k}:=\mathbb{I}\_{\{k\in J^{K}\_{\rho}\}},\quad p\_{\rho}^{k}=\mathbb{P}\left(k\in J^{K}\_{\rho}\right)=\mathbb{E}[I\_{k}],\quad\mbox{and}\quad K\_{0}=\sum\_{k=1}^{K}I\_{k}=|J\_{\rho}^{K}|. |  |

According to Corollary [2.3](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we know that

|  |  |  |  |
| --- | --- | --- | --- |
|  | pρk≥1−Mpρp, and hence ​𝔼​[K0]≥K​(1−Mpρp).\displaystyle p\_{\rho}^{k}\geq 1-\frac{M\_{p}}{\rho^{p}},\mbox{ and hence }\mathbb{E}[K\_{0}]\geq K\left(1-\frac{M\_{p}}{\rho^{p}}\right). |  | (5.33) |

We also have the following concentration bound for K0K\_{0}.

###### Proposition 5.10.

Suppose Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. The following holds with probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | K−K0≤K​Mpρp+2​K​log⁡(1δ).\displaystyle K-K\_{0}\leq\frac{KM\_{p}}{\rho^{p}}+\sqrt{2K\log\left(\frac{1}{\delta}\right)}. |  |

The proof of Proposition [5.10](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem10 "Proposition 5.10. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.7](https://arxiv.org/html/2512.14991v1#A3.SS7 "C.7 Proof of Proposition 5.10 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

Next, we present a concentration result for value functions associated with state processes that exit the ball of radius ρ\rho.

###### Theorem 5.11.

Suppose Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. For any policy π\pi, we have the following holds with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k∈[K]\JρK|V1π​(X1k)|≤K​κm+1​(δ,ρ)+C~1​(1+ρm+1)​(K−K0),\displaystyle\sum\_{k\in[K]\backslash J\_{\rho}^{K}}|V\_{1}^{\pi}(X\_{1}^{k})|\leq K\kappa\_{m+1}(\delta,\rho)+\widetilde{C}\_{1}\Big(1+\rho^{m+1}\Big)(K-K\_{0}), |  | (5.34) |

where κm+1:(0,1]×(ℝ+∪{0})↦ℝ+\kappa\_{m+1}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | κm+1​(δ,y):=1δ​C~1​(𝔼ξ∼Ξ​[‖ξ‖p]yp+𝔼ξ∼Ξ​[‖ξ‖p]yp−(m+1)),\displaystyle\kappa\_{m+1}(\delta,y):=\frac{1}{\delta}\widetilde{C}\_{1}\Big(\frac{\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]}{y^{p}}+\frac{\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]}{y^{p-(m+1)}}\Big), |  | (5.35) |

and C~1\widetilde{C}\_{1} is defined in ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

The proof of Theorem [5.11](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem11 "Theorem 5.11. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.8](https://arxiv.org/html/2512.14991v1#A3.SS8 "C.8 Proof of Theorem 5.11 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

### 5.4 Regret composition

In this subsection, we provide the regret analysis of Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). In Theorem [5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we bound the regret by separating two types of episodes.

###### Theorem 5.12.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. With probability at least 1−6​δ1-6\delta, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Regret​(K)\displaystyle{\rm Regret}(K) | ≤\displaystyle\leq | e2​∑h=1H∑k∈J1CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ)\displaystyle e^{2}\sum\_{h=1}^{H}\sum\_{k\in J\_{1}}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)} |  |
|  |  |  | +2​K​κm+1​(δ,ρ)+4​C~1​(L~3+ρm+1+e2​L~2​H​(Mp​Kδ)m+1p)​(Mpρp​K+2​K​log⁡(1δ)),\displaystyle+2K\kappa\_{m+1}(\delta,\rho)+4\widetilde{C}\_{1}\Big(\widetilde{L}\_{3}+\rho^{m+1}+e^{2}\widetilde{L}\_{2}H\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}\Big)\left(\frac{M\_{p}}{\rho^{p}}K+\sqrt{2K\log\Big(\frac{1}{\delta}\Big)}\right), |  |

where L~1,L~2\widetilde{L}\_{1},\widetilde{L}\_{2} depends only on m,D,d𝒮,C~max,Cmaxm,D,d\_{\mathcal{S}},\widetilde{C}\_{\max},C\_{\max} and L~3:=1+e2​L~2​H\widetilde{L}\_{3}:=1+e^{2}\widetilde{L}\_{2}H
with

|  |  |  |  |
| --- | --- | --- | --- |
|  | C~max:=maxh∈[H]⁡C~h,Cmax:=maxh∈[H]⁡Ch.\displaystyle\widetilde{C}\_{\max}:=\max\_{h\in[H]}\widetilde{C}\_{h},\quad C\_{\max}:=\max\_{h\in[H]}C\_{h}. |  | (5.36) |

Here C~h\widetilde{C}\_{h} is defined in ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ChC\_{h} in ([5.3](https://arxiv.org/html/2512.14991v1#S5.E3 "In 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C~\widetilde{C} in ([4.14](https://arxiv.org/html/2512.14991v1#S4.E14 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), η\eta in ([4.7](https://arxiv.org/html/2512.14991v1#S4.E7 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), Gaph{\rm Gap}\_{h} in ([5.24](https://arxiv.org/html/2512.14991v1#S5.E24 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), GhkG\_{h}^{k} in ([5.31](https://arxiv.org/html/2512.14991v1#S5.E31 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and κm+1\kappa\_{m+1} in ([5.35](https://arxiv.org/html/2512.14991v1#S5.E35 "In Theorem 5.11. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). In addition, BhkB\_{h}^{k} is selected according to Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

The proof of Theorem [5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") is deferred to Appendix [C.10](https://arxiv.org/html/2512.14991v1#A3.SS10 "C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

Before deriving the ultimate regret bound, we introduce the key concepts of near-optimal sets and zooming dimensions, which are commonly used in the contextual bandits literature to bound an algorithm’s regret (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)). However, in our setting, where the state space is unbounded and the reward function is polynomial, these concepts require modification.

###### Definition 5.13 (Near optimal set).

The near optimal set of Z¯\bar{Z} for a given value rr is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zhr,ρ={(x,a)∈Z¯|G~​aph​(x,a)≤g¯​(δ,x)​(H+1)​r},\displaystyle Z\_{h}^{r,\rho}=\Big\{(x,a)\in\bar{Z}\,\Big|\,{\rm\widetilde{G}ap}\_{h}(x,a)\leq\bar{g}(\delta,x)(H+1)r\Big\}, |  | (5.37) |

where the partition space Z¯\overline{Z} is defined in ([3.1](https://arxiv.org/html/2512.14991v1#S3.E1 "In Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and g¯:(0,1]×ℝd𝒮↦ℝ+\bar{g}:(0,1]\times\mathbb{R}^{d\_{\mathcal{S}}}\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g¯​(δ,x):=2​g3​(δ,‖x‖+D)+3​C¯max​(1+2​(‖x‖+2​D)m)+2​C~maxD​(1+(‖x‖+D)m+1).\displaystyle\bar{g}(\delta,x):=2g\_{3}(\delta,\|x\|+D)+3\overline{C}\_{\max}\Big(1+2(\|x\|+2D)^{m}\Big)+2\frac{\widetilde{C}\_{\max}}{D}\Big(1+(\|x\|+D)^{m+1}\Big). |  | (5.38) |

Also, g3:(0,1]×(ℝ+∪{0})↦ℝ+g\_{3}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g3​(δ,y):=2​C^maxC¯max+2​C^maxC¯max​g2​(δ,y)+Cmax​(1+2​(y+D)m),\displaystyle g\_{3}(\delta,y):=2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}+2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}g\_{2}(\delta,y)+C\_{\max}\Big(1+2(y+D)^{m}\Big), |  | (5.39) |

where g2g\_{2} is defined in ([5.2](https://arxiv.org/html/2512.14991v1#S5.E2 "In 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C¯max\overline{C}\_{\max} is defined in ([4.13](https://arxiv.org/html/2512.14991v1#S4.E13 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C~max\widetilde{C}\_{\max} and CmaxC\_{\max} are defined in ([5.36](https://arxiv.org/html/2512.14991v1#S5.E36 "In Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and C^max\widehat{C}\_{\max} is defined in ([5.17](https://arxiv.org/html/2512.14991v1#S5.E17 "In Corollary 5.4. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

While the quantity G~​aph​(x,a){\rm\widetilde{G}ap}\_{h}(x,a) is commonly used to measure the sub-optimality of a given action, we introduce g¯​(δ,x)\bar{g}(\delta,x) to capture the polynomial structure of the entire system. This quantity provides an alternative perspective, serving as a measure of the learning difficulty within our algorithm.

In the following regret analysis, we demonstrate that the algorithm’s regret can be bounded in terms of the size of near-optimal sets. Note that the near-optimal set typically resides on a manifold of much lower dimension than d𝒮+d𝒜d\_{\mathcal{S}}+d\_{\mathcal{A}}. For instance, this occurs in several cases discussed in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)).

To quantify the size of near-optimal sets, we introduce the concepts of packing, packing numbers, and zooming dimension.

###### Definition 5.14 (rr-packing and rr-packing number, Definition 4.2.4 in (Vershynin, [2018](https://arxiv.org/html/2512.14991v1#bib.bib58))).

* •

  For a given r>0r>0 and a compact set 𝒰\mathcal{U}, an r-packing P𝒰r⊂𝒰{\rm P}\_{\mathcal{U}}^{r}\subset\mathcal{U} is a set such that ‖x−x′‖>r\|x-x^{\prime}\|>r for any two distinct x,x′∈P𝒰rx,x^{\prime}\in{\rm P}\_{\mathcal{U}}^{r}.
* •

  We define the rr-packing number of 𝒰\mathcal{U}, denoted Nr​(𝒰)N\_{r}(\mathcal{U}), as the maximum cardinality among all rr-packings of 𝒰\mathcal{U}.

###### Definition 5.15 (Zooming dimension and maximum zooming dimension).

The step-hh zooming dimension zh,cz\_{h,c} with a given positive constant cc is defined as

|  |  |  |
| --- | --- | --- |
|  | zh,c=inf{d>0:Nr​(Zhr,ρ)ρd𝒮≤c​r−d,∀0<r≤D,∀ρ>D}.\displaystyle z\_{h,c}=\inf\left\{d>0\,:\,\frac{N\_{r}(Z\_{h}^{r,\rho})}{\rho^{d\_{\mathcal{S}}}}\leq c\,r^{-d},\forall 0<r\leq D,\forall\rho>D\right\}. |  |

The maximum zooming dimension zm​a​x,cz\_{max,c} is defined as

|  |  |  |
| --- | --- | --- |
|  | zmax,c=maxh∈[H]⁡zh,c.\displaystyle z\_{\max,c}=\max\_{h\in[H]}z\_{h,c}. |  |

In the above, we modify the concept of zooming dimension in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) to adapt to the current unbounded state setting, such that the zooming dimension defined here is independent of ρ\rho. This is crucial to obtain potentially improved regret bounds by utilizing the zooming dimension instead of the ambient dimension d𝒮+d𝒜d\_{\mathcal{S}}+d\_{\mathcal{A}} in the context of an unbounded state setting.

###### Remark 5.16 (Choice of cc in Definition [5.15](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem15 "Definition 5.15 (Zooming dimension and maximum zooming dimension). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

In Definition [5.15](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem15 "Definition 5.15 (Zooming dimension and maximum zooming dimension). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), if we take c≥C𝒮,𝒜:=2d𝒮​Γ​(d𝒮+d𝒜2+1)​a¯d𝒜Γ​(d𝒮2+1)​Γ​(d𝒜2+1)c\geq C\_{\mathcal{S},\mathcal{A}}:=\frac{2^{d\_{\mathcal{S}}}\Gamma(\frac{d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2}+1)\bar{a}^{d\_{\mathcal{A}}}}{\Gamma(\frac{d\_{\mathcal{S}}}{2}+1)\Gamma(\frac{d\_{\mathcal{A}}}{2}+1)}, then it holds that zh,c≤d𝒮+d𝒜z\_{h,c}\leq d\_{\mathcal{S}}+d\_{\mathcal{A}}.

To see this, first note that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Nr​(Zhr,ρ)\displaystyle N\_{r}(Z\_{h}^{r,\rho}) | ≤\displaystyle\leq | Nr​(Z¯)≤Γ​(d𝒮+d𝒜2+1)Γ​(d𝒮2+1)​Γ​(d𝒜2+1)​(ρ+Dr)d𝒮​(a¯r)d𝒜\displaystyle N\_{r}(\bar{Z})\leq\frac{\Gamma(\frac{d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2}+1)}{\Gamma(\frac{d\_{\mathcal{S}}}{2}+1)\Gamma(\frac{d\_{\mathcal{A}}}{2}+1)}\left(\frac{\rho+D}{r}\right)^{d\_{\mathcal{S}}}\left(\frac{\bar{a}}{r}\right)^{d\_{\mathcal{A}}} |  | (5.40) |
|  |  | ≤\displaystyle\leq | C𝒮,𝒜​ρd𝒮rd𝒮+d𝒜≤c​ρd𝒮rd𝒮+d𝒜.\displaystyle C\_{\mathcal{S},\mathcal{A}}\frac{\rho^{d\_{\mathcal{S}}}}{r^{d\_{\mathcal{S}}+d\_{\mathcal{A}}}}\leq c\frac{\rho^{d\_{\mathcal{S}}}}{r^{d\_{\mathcal{S}}+d\_{\mathcal{A}}}}. |  |

Rearrange ([5.40](https://arxiv.org/html/2512.14991v1#S5.E40 "In Remark 5.16 (Choice of 𝑐 in Definition 5.15). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and we get:

|  |  |  |
| --- | --- | --- |
|  | Nr​(Zhr,ρ)ρd𝒮≤c​r−(d𝒮+d𝒜).\displaystyle\frac{N\_{r}(Z\_{h}^{r,\rho})}{\rho^{d\_{\mathcal{S}}}}\leq cr^{-(d\_{\mathcal{S}}+d\_{\mathcal{A}})}. |  |

Hence, by Definition [5.15](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem15 "Definition 5.15 (Zooming dimension and maximum zooming dimension). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we have zh,c≤d𝒮+d𝒜z\_{h,c}\leq d\_{\mathcal{S}}+d\_{\mathcal{A}}.

In light of Remark [5.15](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem15 "Definition 5.15 (Zooming dimension and maximum zooming dimension). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we take c≥C𝒮,𝒜c\geq C\_{\mathcal{S},\mathcal{A}} throughout the rest of the paper. This ensures that the zooming dimension does not exceed the ambient dimension d𝒮+d𝒜d\_{\mathcal{S}}+d\_{\mathcal{A}}.

We now restate Theorem F.3 of (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) in a form suited to our setting with an unbounded state space and polynomial rewards. The proof is deferred to Appendix [C.11.1](https://arxiv.org/html/2512.14991v1#A3.SS11.SSS1 "C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Lemma 5.17 (Theorem F.3 in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53))).

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold.Then for any given constant r0>0r\_{0}>0 we have the following:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ∑h∑k∈JρKCLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\,\Bigg|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg) |  | (5.41) |
|  |  | ≤\displaystyle\leq | ∑h=1H(2​g3​(δ,ρ+D)​K​r0+g4​(δ,ρ+D)​∑r≥r0,r∈ℛNr​(Zhr,ρ)​1r),\displaystyle\sum\_{h=1}^{H}\,\,\left(2g\_{3}(\delta,\rho+D)Kr\_{0}+g\_{4}(\delta,\rho+D)\sum\_{r\geq r\_{0},r\in\mathcal{R}}N\_{r}(Z\_{h}^{r,\rho})\frac{1}{r}\right), |  |

where ℛ:={r|∃h∈[H],k∈JρK,diam​(Bhk)=r}\mathcal{R}:=\{r\,\,|\,\,\exists h\in[H],k\in J\_{\rho}^{K},{\rm diam}(B\_{h}^{k})=r\}. Here JρKJ\_{\rho}^{K} is defined in ([5.32](https://arxiv.org/html/2512.14991v1#S5.E32 "In 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C¯max\overline{C}\_{\max} in ([4.13](https://arxiv.org/html/2512.14991v1#S4.E13 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), Gaph{\rm Gap}\_{h} in ([5.24](https://arxiv.org/html/2512.14991v1#S5.E24 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), GhkG\_{h}^{k} in ([5.31](https://arxiv.org/html/2512.14991v1#S5.E31 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), g1g\_{1} in ([4.21](https://arxiv.org/html/2512.14991v1#S4.E21 "In 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), g3g\_{3} in ([5.39](https://arxiv.org/html/2512.14991v1#S5.E39 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and g¯\bar{g} in ([5.38](https://arxiv.org/html/2512.14991v1#S5.E38 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). In addition, g4:(0,1]×(ℝ+∪{0})↦ℝ+g\_{4}:(0,1]\times(\mathbb{R}\_{+}\cup\{0\})\mapsto\mathbb{R}\_{+} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g4​(δ,y):=g3​(δ,y)​g1​(δ,y)2+(2​a¯)d𝒜Dd𝒮+d𝒜−2​(d𝒮+d𝒜)d𝒮+d𝒜2​yd𝒮​g¯​(δ,y).\displaystyle g\_{4}(\delta,y):=g\_{3}(\delta,y)g\_{1}(\delta,y)^{2}+\frac{(2\bar{a})^{d\_{\mathcal{A}}}}{D^{d\_{\mathcal{S}}+d\_{\mathcal{A}}-2}}(d\_{\mathcal{S}}+d\_{\mathcal{A}})^{\frac{d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2}}y^{d\_{\mathcal{S}}}\bar{g}(\delta,y). |  | (5.42) |

Note that the upper bound in ([5.41](https://arxiv.org/html/2512.14991v1#S5.E41 "In Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for any generic r0>0r\_{0}>0. The choice of r0r\_{0} is to be specified in the final regret analysis (see Theorem [5.19](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem19 "Theorem 5.19. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Finally, we are ready to provide the regret bound.

###### Theorem 5.18.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. With probability at least 1−6​δ1-6\delta, we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Regret​(K)\displaystyle{\rm Regret}(K) | ≤\displaystyle\leq | e2​∑h=1H(2​g3​(δ,ρ+D)​K​r0+g4​(δ,ρ+D)​∑r≥r0,r∈ℛNr​(Zhr,ρ)​1r)\displaystyle e^{2}\sum\_{h=1}^{H}\,\,\left(2g\_{3}(\delta,\rho+D)Kr\_{0}+g\_{4}(\delta,\rho+D)\sum\_{r\geq r\_{0},r\in\mathcal{R}}N\_{r}(Z\_{h}^{r,\rho})\frac{1}{r}\right) |  | (5.43) |
|  |  |  | +2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ)+2​K​κm+1​(δ,ρ)\displaystyle+2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)}+2K\kappa\_{m+1}(\delta,\rho) |  |
|  |  |  | +4​C~1​(L~3+ρm+1+e2​L~2​H​(Mp​Kδ)m+1p)​(Mpρp​K+2​K​log⁡(1δ)),\displaystyle+4\widetilde{C}\_{1}\Big(\widetilde{L}\_{3}+\rho^{m+1}+e^{2}\widetilde{L}\_{2}H\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}\Big)\left(\frac{M\_{p}}{\rho^{p}}K+\sqrt{2K\log\Big(\frac{1}{\delta}\Big)}\right), |  |

where g3g\_{3} is defined in ([5.39](https://arxiv.org/html/2512.14991v1#S5.E39 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), g4g\_{4} is defined in ([5.42](https://arxiv.org/html/2512.14991v1#S5.E42 "In Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), C~1\widetilde{C}\_{1} is defined in ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and κm+1\kappa\_{m+1} is defined in ([5.35](https://arxiv.org/html/2512.14991v1#S5.E35 "In Theorem 5.11. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Furthermore, if we set ρ=Mp1p​Kβ\rho=M\_{p}^{\frac{1}{p}}K^{\beta}, r0=Kγr\_{0}=K^{\gamma}, then:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Regret​(K)\displaystyle{\rm Regret}(K) | ≲\displaystyle\lesssim | Cmax​Mpm+1p​H​K1+γ+(m+1)​β​(log⁡(2​H​K2δ))m2\displaystyle C\_{\max}M\_{p}^{\frac{m+1}{p}}HK^{1+\gamma+(m+1)\beta}{{\Bigg(\log\left(\frac{2HK^{2}}{\delta}\right)\Bigg)^{\frac{m}{2}}}} |  | (5.44) |
|  |  |  | +(Cmax​C¯max2+Cmax)​∑h=1HMp2​d𝒮+3​m+5p​H​K(2​d𝒮+3​m+5)​β−γ​(zh,c+1)​(log⁡(2​H​K2δ))3​m2+2\displaystyle+(C\_{\max}\overline{C}\_{\max}^{2}+C\_{\max})\sum\_{h=1}^{H}M\_{p}^{\frac{2d\_{\mathcal{S}}+3m+5}{p}}HK^{(2d\_{\mathcal{S}}+3m+5)\beta-\gamma(z\_{h,c}+1)}{{\Bigg(\log\left(\frac{2HK^{2}}{\delta}\right)\Bigg)^{\frac{3m}{2}+2}}} |  |
|  |  |  | +L~1​H​Mpm+1p​K12+m+1p+C~1​(Mp+Mpm+1p)​K1−(p−(m+1))​β\displaystyle+\sqrt{\widetilde{L}\_{1}H}M\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+\frac{m+1}{p}}+\widetilde{C}\_{1}(M\_{p}+M\_{p}^{\frac{m+1}{p}})K^{1-(p-(m+1))\beta} |  |
|  |  |  | +C~1​Mpm+1p​K12+(m+1)​β+Mp1+m+1p​K1+m+1p−p​β+H​Mpm+1p​K12+m+1p,\displaystyle+\widetilde{C}\_{1}M\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+(m+1)\beta}+M\_{p}^{1+\frac{m+1}{p}}K^{1+\frac{m+1}{p}-p\beta}+HM\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+\frac{m+1}{p}}, |  |

where ≲\lesssim omits constants that are independent of H,KH,K.

###### Proof.

Take ρ=Mp1p​Kβ\rho=M\_{p}^{\frac{1}{p}}K^{\beta} and r0=Kγr\_{0}=K^{\gamma} in Theorem [5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we have with probability at least 1−6​δ1-6\delta:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Regret​(K)\displaystyle{\rm Regret}(K) |  | (5.45) |
|  |  | ≤\displaystyle\leq | e2​∑h=1H∑k∈J1CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ)\displaystyle e^{2}\sum\_{h=1}^{H}\sum\_{k\in J\_{1}}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)} |  |
|  |  |  | +2​K​κm+1​(δ,ρ)+4​C~1​(L~3+ρm+1+e2​L~2​H​(Mp​Kδ)m+1p)​(Mpρp​K+2​K​log⁡(1δ))\displaystyle+2K\kappa\_{m+1}(\delta,\rho)+4\widetilde{C}\_{1}\Big(\widetilde{L}\_{3}+\rho^{m+1}+e^{2}\widetilde{L}\_{2}H\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}\Big)\left(\frac{M\_{p}}{\rho^{p}}K+\sqrt{2K\log\Big(\frac{1}{\delta}\Big)}\right) |  |
|  |  | ≤\displaystyle\leq | e2​∑h=1H(2​g3​(δ,ρ+D)​K​r0+g4​(δ,ρ+D)​∑r≥r0,r∈ℛNr​(Zhr,ρ)​1r)\displaystyle e^{2}\sum\_{h=1}^{H}\,\,\left(2g\_{3}(\delta,\rho+D)Kr\_{0}+g\_{4}(\delta,\rho+D)\sum\_{r\geq r\_{0},r\in\mathcal{R}}N\_{r}(Z\_{h}^{r,\rho})\frac{1}{r}\right) |  |
|  |  |  | +2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ)+2​K​κm+1​(δ,ρ)\displaystyle+2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)}+2K\kappa\_{m+1}(\delta,\rho) |  |
|  |  |  | +4​C~1​(L~3+ρm+1+e2​L~2​H​(Mp​Kδ)m+1p)​(Mpρp​K+2​K​log⁡(1δ))\displaystyle+4\widetilde{C}\_{1}\Big(\widetilde{L}\_{3}+\rho^{m+1}+e^{2}\widetilde{L}\_{2}H\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}\Big)\left(\frac{M\_{p}}{\rho^{p}}K+\sqrt{2K\log\Big(\frac{1}{\delta}\Big)}\right) |  |
|  |  | ≲\displaystyle\lesssim | Cmax​Mpm+1p​H​K1+γ+(m+1)​β​(log⁡(2​H​K2δ))m2\displaystyle C\_{\max}M\_{p}^{\frac{m+1}{p}}HK^{1+\gamma+(m+1)\beta}{{\Bigg(\log\left(\frac{2HK^{2}}{\delta}\right)\Bigg)^{\frac{m}{2}}}} |  |
|  |  |  | +(Cmax​C¯max2+Cmax)​∑h=1HMp2​d𝒮+3​m+5p​H​K(2​d𝒮+3​m+5)​β−γ​(zh,c+1)​(log⁡(2​H​K2δ))3​m2+2\displaystyle+(C\_{\max}\overline{C}\_{\max}^{2}+C\_{\max})\sum\_{h=1}^{H}M\_{p}^{\frac{2d\_{\mathcal{S}}+3m+5}{p}}HK^{(2d\_{\mathcal{S}}+3m+5)\beta-\gamma(z\_{h,c}+1)}{{\Bigg(\log\left(\frac{2HK^{2}}{\delta}\right)\Bigg)^{\frac{3m}{2}+2}}} |  |
|  |  |  | +L~1​H​Mpm+1p​K12+m+1p+C~1​(Mp+Mpm+1p)​K1−(p−(m+1))​β\displaystyle+\sqrt{\widetilde{L}\_{1}H}M\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+\frac{m+1}{p}}+\widetilde{C}\_{1}(M\_{p}+M\_{p}^{\frac{m+1}{p}})K^{1-(p-(m+1))\beta} |  |
|  |  |  | +C~1​Mpm+1p​K12+(m+1)​β+Mp1+m+1p​K1+m+1p−p​β+H​Mpm+1p​K12+m+1p,\displaystyle+\widetilde{C}\_{1}M\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+(m+1)\beta}+M\_{p}^{1+\frac{m+1}{p}}K^{1+\frac{m+1}{p}-p\beta}+HM\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+\frac{m+1}{p}}, |  |

where the second inequality is due to ([5.41](https://arxiv.org/html/2512.14991v1#S5.E41 "In Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the fact that Nr​(Zhr,ρ)ρd𝒮≤c​r−zh,c\frac{N\_{r}(Z\_{h}^{r,\rho})}{\rho^{d\_{\mathcal{S}}}}\leq cr^{-z\_{h,c}}.
∎

We now derive the optimal order by selecting hyperparameters to balance the competing terms.

###### Theorem 5.19.

Take the same assumptions in Theorem [5.18](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem18 "Theorem 5.18. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). The optimal regret order on KK in ([5.44](https://arxiv.org/html/2512.14991v1#S5.E44 "In Theorem 5.18. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) is achieved as 1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)} if we
take

|  |  |  |
| --- | --- | --- |
|  | β=p+(m+1)​(zmax,c+2)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4),γ=(2​d𝒮+2​m+4)​β2−1zmax,c+2.\displaystyle\beta=\frac{p+(m+1)(z\_{\max,c}+2)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)},\quad\gamma=\frac{(2d\_{\mathcal{S}}+2m+4)\beta\_{2}-1}{z\_{\max,c}+2}. |  |

Then with probability at least 1−6​δ1-6\delta, the following optimal regret bound holds that:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Regret​(K)\displaystyle{\rm Regret}(K) |  | (5.46) |
|  |  | ≲\displaystyle\lesssim | Cmax​Mpm+1p​H​K1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)​(log⁡(2​H​K2δ))m2\displaystyle C\_{\max}M\_{p}^{\frac{m+1}{p}}HK^{1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}}{{\Bigg(\log\left(\frac{2HK^{2}}{\delta}\right)\Bigg)^{\frac{m}{2}}}} |  |
|  |  |  | +(Cmax​C¯max2+Cmax)​∑h=1HMp2​d𝒮+3​m+5p​H​K1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)​(log⁡(2​H​K2δ))3​m2+2\displaystyle+(C\_{\max}\overline{C}\_{\max}^{2}+C\_{\max})\sum\_{h=1}^{H}M\_{p}^{\frac{2d\_{\mathcal{S}}+3m+5}{p}}HK^{1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}}{{\Bigg(\log\left(\frac{2HK^{2}}{\delta}\right)\Bigg)^{\frac{3m}{2}+2}}} |  |
|  |  |  | +L~1​H​Mpm+1p​K12+m+1p+C~1​(Mp+Mpm+1p)​K1−(p−m−1)​(p+(m+1)​(zmax,c+2))p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)\displaystyle+\sqrt{\widetilde{L}\_{1}H}M\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+\frac{m+1}{p}}+\widetilde{C}\_{1}(M\_{p}+M\_{p}^{\frac{m+1}{p}})K^{1-\frac{(p-m-1)(p+(m+1)(z\_{\max,c}+2))}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}} |  |
|  |  |  | +C~1​Mpm+1p​K12+(m+1)​p+(m+1)2​(zmax,c+2)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)+Mp1+m+1p​K1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)\displaystyle+\widetilde{C}\_{1}M\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+\frac{(m+1)p+(m+1)^{2}(z\_{\max,c}+2)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}}+M\_{p}^{1+\frac{m+1}{p}}K^{1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}} |  |
|  |  |  | +H​Mpm+1p​K12+m+1p,\displaystyle+HM\_{p}^{\frac{m+1}{p}}K^{\frac{1}{2}+\frac{m+1}{p}}, |  |

###### Proof.

To find the optimal orders in ([5.44](https://arxiv.org/html/2512.14991v1#S5.E44 "In Theorem 5.18. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) with respect to KK, it is sufficient to solve the minimization problem of the following objective function U​(β,γ)U(\beta,\gamma).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U​(β,γ)\displaystyle U(\beta,\gamma) | :=\displaystyle:= | max{1+γ+(m+1)β,(2d𝒮+3m+5)β−γ(zmax,c+1),\displaystyle\max\Big\{1+\gamma+(m+1)\beta,(2d\_{\mathcal{S}}+3m+5)\beta-\gamma(z\_{\max,c}+1), |  |
|  |  |  | 12+m+1p,12+(m+1)β,1−(p−(m+1))β,1+m+1p−pβ}.\displaystyle\qquad\quad\frac{1}{2}+\frac{m+1}{p},\frac{1}{2}+(m+1)\beta,1-(p-(m+1))\beta,1+\frac{m+1}{p}-p\beta\Big\}. |  |

We analyze the problem under two regimes: (1) β≥1p\beta\geq\frac{1}{p} and (2) β<1p\beta<\frac{1}{p}.

Case (1): In this regime, we can simplify ([5.4](https://arxiv.org/html/2512.14991v1#S5.Ex46 "5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) as
U​(β,γ)=max⁡{1+γ+(m+1)​β,(2​d𝒮+3​m+5)​β−γ​(zmax,c+1),12+(m+1)​β}U(\beta,\gamma)=\max\Big\{1+\gamma+(m+1)\beta,(2d\_{\mathcal{S}}+3m+5)\beta-\gamma(z\_{\max,c}+1),\frac{1}{2}+(m+1)\beta\Big\}. Clearly, over this region, the minimizer (β1,γ1)(\beta\_{1},\gamma\_{1}) satisfies the following equation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1+γ1+(m+1)​β1\displaystyle 1+\gamma\_{1}+(m+1)\beta\_{1} | =\displaystyle= | (2​d𝒮+3​m+5)​β1−γ1​(zmax,c+1),\displaystyle(2d\_{\mathcal{S}}+3m+5)\beta\_{1}-\gamma\_{1}(z\_{\max,c}+1), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | β1\displaystyle\beta\_{1} | =\displaystyle= | 1p.\displaystyle\frac{1}{p}. |  |

By straightforward calculations, we get γ1=2​d𝒮+2​m+4−pp​(zmax,c+2)\gamma\_{1}=\frac{2d\_{\mathcal{S}}+2m+4-p}{p(z\_{\max,c}+2)} and U​(β1,γ1)=1−(p−(m+1)​(zmax,c+4)−2​d𝒮−2)p​(zmax,c+2)U(\beta\_{1},\gamma\_{1})=1-\frac{(p-(m+1)(z\_{\max,c}+4)-2d\_{\mathcal{S}}-2)}{{p(z\_{\max,c}+2)}}.

Case (2):
In this regime, we can simplify ([5.4](https://arxiv.org/html/2512.14991v1#S5.Ex46 "5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) as
U​(β,γ)=max⁡{1+γ+(m+1)​β,(2​d𝒮+3​m+5)​β−γ​(zmax,c+1),12+m+1p,1+m+1p−p​β}U(\beta,\gamma)=\max\Big\{1+\gamma+(m+1)\beta,(2d\_{\mathcal{S}}+3m+5)\beta-\gamma(z\_{\max,c}+1),\frac{1}{2}+\frac{m+1}{p},1+\frac{m+1}{p}-p\beta\Big\}. Then the minimum of U​(⋅,⋅)U(\cdot,\cdot) shall be U​(β2,γ2)U(\beta\_{2},\gamma\_{2}) where (β2,γ2)(\beta\_{2},\gamma\_{2}) satisfies:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1+γ2+(m+1)​β2\displaystyle 1+\gamma\_{2}+(m+1)\beta\_{2} | =\displaystyle= | (2​d𝒮+3​m+5)​β2−γ2​(zmax,c+1),\displaystyle(2d\_{\mathcal{S}}+3m+5)\beta\_{2}-\gamma\_{2}(z\_{\max,c}+1), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1+m+1p−p​β2\displaystyle 1+\frac{m+1}{p}-p\beta\_{2} | =\displaystyle= | 1+γ2+(m+1)​β2.\displaystyle 1+\gamma\_{2}+(m+1)\beta\_{2}. |  |

By straightforward calculations, we get
β2=p+(m+1)​(zmax,c+2)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)\beta\_{2}=\frac{p+(m+1)(z\_{\max,c}+2)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}, γ2=(2​d𝒮+2​m+4)​β2−1zmax,c+2\gamma\_{2}=\frac{(2d\_{\mathcal{S}}+2m+4)\beta\_{2}-1}{z\_{\max,c}+2} and U​(β2,γ2)=1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)U(\beta\_{2},\gamma\_{2})=1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}.

In addition, we can show that U​(β1,γ1)>U​(β2,γ2)U(\beta\_{1},\gamma\_{1})>U(\beta\_{2},\gamma\_{2}).

Therefore, the optimal leading order on KK is achieved at 1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)} if we
take β=p+(m+1)​(zmax,c+2)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)\beta=\frac{p+(m+1)(z\_{\max,c}+2)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)} and γ=(2​d𝒮+2​m+4)​β2−1zmax,c+2\gamma=\frac{(2d\_{\mathcal{S}}+2m+4)\beta\_{2}-1}{z\_{\max,c}+2}. Combined with ([5.44](https://arxiv.org/html/2512.14991v1#S5.E44 "In Theorem 5.18. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we can verify that ([5.46](https://arxiv.org/html/2512.14991v1#S5.E46 "In Theorem 5.19. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds with probability at least 1−6​δ1-6\delta.
∎

###### Remark 5.20 (Dependence on HH).

Following the usual convention in (Domingues et al., [2021](https://arxiv.org/html/2512.14991v1#bib.bib17); Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)), we suppress the dependence of the Lipschitz constants on the horizon HH, and thus the dependence of Cmax,C¯max,C~max,C~1,L~1C\_{\max},\overline{C}\_{\max},\widetilde{C}\_{\max},\widetilde{C}\_{1},\widetilde{L}\_{1} on HH in Theorem [5.19](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem19 "Theorem 5.19. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). In the bounded reward and bounded state space setting, this dependence can be removed by appropriately rescaling the system (see Lemma 2.4 in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53))). Extending such an argument to our framework with unbounded state spaces and reward functions, however, might be more difficult.

###### Remark 5.21 (Comparison of our regret to the literature).

Note that

|  |  |  |
| --- | --- | --- |
|  | 1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)→zmax,c+1zmax,c+21-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}\rightarrow\frac{z\_{\max,c}+1}{z\_{\max,c}+2} |  |

as pp tends to infinity. This suggests that if the initial distribution has all moments bounded, we recover the regret of the AdaMB algorithm proposed in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) for bounded state space in terms of the episode number KK.

A detailed comparison between our algorithms and those proposed in (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) is presented in Table [1](https://arxiv.org/html/2512.14991v1#S5.T1 "Table 1 ‣ Remark 5.21 (Comparison of our regret to the literature). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), where zmax,c′z^{\prime}\_{\max,c} is defined in Definition 2.7 of (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)).

On one hand, our dependence on
HH is linear, obtained by applying Lipschitz-type properties of the value functions. In contrast, (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) incurs a higher-order dependence on
HH, since their analysis relies on the fact that cumulative rewards over
HH time steps are bounded by
HH. However, in both our work and theirs, the dependence of the Lipschitz constants on
HH is masked. Consequently, the comparison in terms of the order of
HH may not be fully accurate, and we therefore prefer to place less emphasis on it.

|  |  |  |  |
| --- | --- | --- | --- |
| AdaMB | AdaQL | APL-Diffusion | APL-Diffusion |
| (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) | (Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)) | (ours) | (ours) (p↦∞)(p\mapsto\infty) |
| H32​Kzmax,c′+max⁡{d𝒮,2}−1zmax,c′+max⁡{d𝒮,2}H^{\frac{3}{2}}K^{\frac{{z^{\prime}\_{\max,c}}+\max\{d\_{\mathcal{S}},2\}-1}{{z^{\prime}\_{\max,c}}+\max\{d\_{\mathcal{S}},2\}}} | H52​Kzmax,c′+1zmax,c′+2H^{\frac{5}{2}}K^{\frac{{z^{\prime}\_{\max,c}}+1}{{z^{\prime}\_{\max,c}}+2}} | H​K1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)HK^{1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)}} | H​Kzmax,c+1zmax,c+2HK^{\frac{z\_{\max,c}+1}{z\_{\max,c}+2}} |

Table 1: Comparison of the regret orders.

###### Remark 5.22 (Without knowing KK a priori.).

To achieve a regret order as indicated in Theorem [5.19](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem19 "Theorem 5.19. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we need to know the total number of episodes a prior as the hyper-parameters ρ\rho and r0r\_{0} depend on KK. When KK is not known in advance, the classic doubling trick (Besson and Kaufmann, [2018](https://arxiv.org/html/2512.14991v1#bib.bib7)) can be applied to achieve the same order of regret (see Algorithm [6](https://arxiv.org/html/2512.14991v1#alg6 "Algorithm 6 ‣ Remark 5.22 (Without knowing 𝐾 a priori.). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Algorithm 6  The Doubling Trick

Initialize: K0K\_{0}

for i∈{0,1,2,⋯,n}i\in\{0,1,2,\cdots,n\} do

Ki←2i​K0K\_{i}\leftarrow 2^{i}K\_{0}

Run Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") for KiK\_{i} episodes.

end for

Denote κ=1−p2−(m+1)2​(zmax,c+2)−(m+1)​(2​d𝒮+2​m+4)p​(p+m+1)​(zmax,c+2)+p​(2​d𝒮+2​m+4)\kappa=1-\frac{p^{2}-(m+1)^{2}(z\_{\max,c}+2)-(m+1)(2d\_{\mathcal{S}}+2m+4)}{p(p+m+1)(z\_{\max,c}+2)+p(2d\_{\mathcal{S}}+2m+4)} and Ktotal=∑i=1nKi=K0​∑i=1n2i=K0​(2n+1−1)K\_{\rm total}=\sum\_{i=1}^{n}K\_{i}=K\_{0}\sum\_{i=1}^{n}2^{i}=K\_{0}(2^{n+1}-1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nR​(Ki)=∑i=1n(2i)κ​∑i=1n2κ​i≈2κ​(n+1)−12κ−1≈(Ktotal)κ.\displaystyle\sum\_{i=1}^{n}R(K\_{i})=\sum\_{i=1}^{n}(2^{i})^{\kappa}\sum\_{i=1}^{n}2^{\kappa i}\approx\frac{2^{\kappa(n+1)}-1}{2^{\kappa}-1}\approx(K\_{\rm total})^{\kappa}. |  | (5.48) |

## 6 Numerical experiments

We illustrate the performance of the APL-Diffusion Algorithm with two examples. The first is a toy one-dimensional problem, featuring a reward function with quadratic growth and dynamics followed by a mean-reverting process. The second example involves a mean-variance portfolio optimization problem, where the state process represents asset prices and the controls correspond to the allocation of wealth among portfolio assets.

### 6.1 A one-dimensional example

We first illustrate the performance using a tractable one-dimensional problem. Let us take the state space as 𝒮=ℝ\mathcal{S}=\mathbb{R} and the action space as [0,10][0,10].

##### Set-up.

The experiment set-up is specified as follows.

* •

  Dynamics and reward: for h∈[H−1]h\in[H-1], μh​(x,a)=0.05−0.1​x+0.01​a\mu\_{h}(x,a)=0.05-0.1x+0.01a, σh​(x,a)=0.1\sigma\_{h}(x,a)=0.1, X1=4X\_{1}=4, Rh​(x,a)∼𝒩​((x−a)2,0.01)R\_{h}(x,a)\sim\mathcal{N}((x-a)^{2},0.01).
* •

  Model parameters: H=10H=10, K=2000K=2000, ρ=10\rho=10, ∀h∈[H],C~h=5,D=10​2,Δ=1\forall h\in[H],\widetilde{C}\_{h}=5,D=10\sqrt{2},\Delta=1.
* •

  Initialization: For any
  h∈[H],k∈[K]h\in[H],k\in[K], and B∈𝒫h0B\in\mathcal{P}\_{h}^{0}, we set

  |  |  |  |
  | --- | --- | --- |
  |  | 𝒫h0={[0,10]×[0,10],[10,0]×[0,10]},Q¯h0​(⋅)=1837.1,Q¯hk​(Z¯∁)=−505,\displaystyle\mathcal{P}\_{h}^{0}=\{[0,10]\times[0,10],[10,0]\times[0,10]\},\,\,\overline{Q}\_{h}^{0}(\cdot)=1837.1,\,\,\overline{Q}\_{h}^{k}(\bar{Z}^{\complement})=-505, |  |
  |  |  |  |
  | --- | --- | --- |
  |  | V~h0​(S)=1837.1,S=Γ𝒮​(B),V¯h0​(x)=5+5​‖x‖2​ for ​x∈ℝd𝒮.\displaystyle\widetilde{V}\_{h}^{0}(S)=1837.1,\,\,S=\Gamma\_{\mathcal{S}}(B),\,\,\overline{V}\_{h}^{0}(x)=5+5\|x\|^{2}\mbox{ for }x\in\mathbb{R}^{d\_{\mathcal{S}}}. |  |

##### Adaptive partition and convergence.

In Figure [2](https://arxiv.org/html/2512.14991v1#S6.F2 "Figure 2 ‣ Regret order. ‣ 6.1 A one-dimensional example ‣ 6 Numerical experiments ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), our algorithm adaptively refines the partition granularity in regions where the underlying Qh∗Q\_{h}^{\*} values are high (with high confidence). Notably, the ground truth optimal action a∗a^{\*} which is equal to 10 with high probability, unknown to the algorithm, falls within these finely partitioned regions, highlighting the algorithm’s effectiveness and superior performance in efficient discretization.

In addition, Figure [3](https://arxiv.org/html/2512.14991v1#S6.F3 "Figure 3 ‣ Regret order. ‣ 6.1 A one-dimensional example ‣ 6 Numerical experiments ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-(a) shows that the estimated Vπ~V^{\widetilde{\pi}} rapidly converge to the optimal level, indicating a fast convergence rate of the algorithm.

##### Regret order.

In Figure [3](https://arxiv.org/html/2512.14991v1#S6.F3 "Figure 3 ‣ Regret order. ‣ 6.1 A one-dimensional example ‣ 6 Numerical experiments ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-(b),we present the log-log plot of cumulative regret versus episode index, focusing on the regime where performance has stabilized. By fitting a linear regression model to the data, we estimate the regret order based on the slope of the fitted linear line. The estimated slope is 0.69 which is smaller than the worst case regret order of value 1+d𝒮+d𝒜2+d𝒮+d𝒜=34\frac{1+d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2+d\_{\mathcal{S}}+d\_{\mathcal{A}}}=\frac{3}{4}.

![Refer to caption](heat_map.png)


Figure 2: Demonstration of the adaptive partition from the APL-Diffusion algorithm for 𝒫92000\mathcal{P}\_{9}^{2000}.



![Refer to caption](estimated_vpi_simple_1.png)


(a) Estimated Vπ~V^{\widetilde{\pi}} (per episode) throughout training.

![Refer to caption](linear_fit_simple_2000.png)


(b) Estimating regret order via linear regression: log(cumulative regret) with respect to log(episode).

Figure 3: Algorithm performance.

### 6.2 Mean-variance portfolio optimization

We next evaluate the performance of the APL-Diffusion Algorithm in the context of mean-variance portfolio optimization with multiple assets. In this setting, the agent learns to determine the optimal allocation of wealth across a basket of securities, balancing expected return against portfolio variance.

We consider a market with nn assets. One of the assets is a risk-free asset with interest rate r0>0r\_{0}>0. For h∈[H−1]h\in[H-1], the price follows:

|  |  |  |
| --- | --- | --- |
|  | Yh+1−Yh=r0​Yh​Δ,\displaystyle Y\_{h+1}-Y\_{h}=r\_{0}Y\_{h}\Delta, |  |

with initial condition Y1=y>0.Y\_{1}=y>0.

The other five assets are stocks whose price processes follow, for h∈[H−1]h\in[H-1],

|  |  |  |
| --- | --- | --- |
|  | Zh+1i−Zhi=bi​Zhi​Δ+σi​Zhi​Bhi​Δ,\displaystyle Z^{i}\_{h+1}-Z^{i}\_{h}=b^{i}Z\_{h}^{i}\Delta+\sigma^{i}Z\_{h}^{i}B\_{h}^{i}\sqrt{\Delta}, |  |

with initial condition Z1i=zi>0Z^{i}\_{1}=z^{i}>0. Here, bi>r0b^{i}>r\_{0} is the appreciation rate and σi>0\sigma^{i}>0 is the volatility of the stock ii (i=1,⋯,n−1i=1,\cdots,n-1).

Consider an investor who invests ahia\_{h}^{i} proportion of the wealth to stock ZiZ^{i} at time hh, with the remaining proportion 1−∑i=1n−1ahi1-\sum\_{i=1}^{n-1}a\_{h}^{i} to the risk-free asset,
then the wealth process follows, for h∈[H−1]h\in[H-1],

|  |  |  |
| --- | --- | --- |
|  | Xh+1−Xh=(r0​Xh+∑i=1n−1(bi−r0)​Xh​ahi)​Δ+∑i=1n−1σi​Xh​ahi​Bhi​Δ,\displaystyle X\_{h+1}-X\_{h}=\left(r\_{0}X\_{h}+\sum\_{i=1}^{n-1}(b^{i}-r\_{0})X\_{h}a\_{h}^{i}\right)\Delta+\sum\_{i=1}^{n-1}\sigma^{i}X\_{h}a^{i}\_{h}B\_{h}^{i}\sqrt{\Delta}, |  |

with initial condition X1=x1>0.X\_{1}=x\_{1}>0.
Here we restrict that 0≤ahi≤1,∑i=1n−1ahi≤10\leq a\_{h}^{i}\leq 1,\sum\_{i=1}^{n-1}a\_{h}^{i}\leq 1.

The reward function is set as

|  |  |  |
| --- | --- | --- |
|  | Rh​(x,a)=δ0, for ​h∈[H−1], and ​RH​(x,a)=δ(ν−x)​x.\displaystyle R\_{h}(x,a)=\delta\_{0},\mbox{ for }h\in[H-1],\mbox{ and }R\_{H}(x,a)=\delta\_{(\nu-x)x}. |  |

###### Remark 6.1.

It is worth emphasizing that in this experiment setting, the volatility can become arbitrarily small, and the drift and volatility coefficients may fail to be Lipschitz continuous with respect to the action variable. These conditions fall outside the scope of Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), which are required for our theoretical regret guarantees. However, empirical results demonstrate that the APL-Diffusion Algorithm maintains strong performance despite the violation of these assumptions. This suggests that the algorithm exhibits robustness and practical effectiveness beyond the confines of the theoretical framework.

##### Set-up.

We specify the parameters governing the system dynamics and reward function, along with other model configurations and initialization settings, as follows.

* •

  We take n=6n=6 in this example with 55 risky assets and 11 risk-free asset.
* •

  Dynamics and reward:
  r0=0.05,bi=0.15,σi=0.2,ν=10,X1=2,(i=1,⋯,5).r\_{0}=0.05,b^{i}=0.15,\sigma^{i}=0.2,\nu=10,X\_{1}=2,(i=1,\cdots,5).
* •

  Model parameters: H=30H=30, K=2000K=2000, ρ=10\rho=10, ∀h∈[H],C~h=1\forall h\in[H],\widetilde{C}\_{h}=1, Δ=152\Delta=\frac{1}{52}.
* •

  Initialization:222Note that in this application, the action domain is not a hypercube as assumed in the earlier section. Consequently, both the initialization and block-splitting procedures are modified accordingly. We define the initial partition as 𝒫h0={[0,ρ]×𝒜,[−ρ,0]×𝒜}\mathcal{P}\_{h}^{0}=\{[0,\rho]\times\mathcal{A},[-\rho,0]\times\mathcal{A}\} and initialize the estimators as Q¯h0​(⋅)=C~h​(1+ρm+1)\overline{Q}\_{h}^{0}(\cdot)=\widetilde{C}\_{h}(1+\rho^{m+1}) and V~h0(.)=C~h(1+ρm+1)\widetilde{V}\_{h}^{0}(.)=\widetilde{C}\_{h}(1+\rho^{m+1}). For Q¯hk​(Z¯∁)\overline{Q}\_{h}^{k}(\bar{Z}^{\complement}) and V¯h0\overline{V}\_{h}^{0}, we adopt the same values as in ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). When splitting a block, we divide the corresponding one-dimensional state space into two halves, and partition the five-dimensional isosceles right simplex action space into thirty-two isosceles right simplex of equal size.
  ∀h∈[H],∀k∈[K],B∈𝒫h0\forall h\in[H],\forall k\in[K],B\in\mathcal{P}\_{h}^{0},

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | 𝒫h0\displaystyle\mathcal{P}\_{h}^{0} | =\displaystyle= | {[0,10]×𝒜,[−10,0]×𝒜},where ​𝒜={a:ai≥0,∑i=15ai≤1,i=1,2,3,4,5},\displaystyle\{[0,10]\times\mathcal{A},[-10,0]\times\mathcal{A}\},\mbox{where }\mathcal{A}=\left\{a:a\_{i}\geq 0,\sum\_{i=1}^{5}a\_{i}\leq 1,i=1,2,3,4,5\right\}, |  |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | Q¯h0​(⋅)\displaystyle\overline{Q}\_{h}^{0}(\cdot) | =\displaystyle= | 101,Q¯hk​(Z¯∁)=−101,V~h0​(S)=101,S=Γ𝒮​(B),V¯h0​(x)=‖x‖2+101​ for ​x∈ℝd𝒮.\displaystyle 101,\,\,\overline{Q}\_{h}^{k}(\bar{Z}^{\complement})=-101,\,\,\widetilde{V}\_{h}^{0}(S)=101,S=\Gamma\_{\mathcal{S}}(B),\overline{V}\_{h}^{0}(x)=\|x\|^{2}+101\mbox{ for }x\in\mathbb{R}^{d\_{\mathcal{S}}}. |  |

##### Reward convergence and regret order.

In Figure [3](https://arxiv.org/html/2512.14991v1#S6.F3 "Figure 3 ‣ Regret order. ‣ 6.1 A one-dimensional example ‣ 6 Numerical experiments ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-(a), we see the rapid convergence of estimated Vπ~V^{\widetilde{\pi}} towards the optimal value. In Figure [3](https://arxiv.org/html/2512.14991v1#S6.F3 "Figure 3 ‣ Regret order. ‣ 6.1 A one-dimensional example ‣ 6 Numerical experiments ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-(b), we present the log-log plot of cumulative regret versus episode index, focusing on the regime where performance has stabilized. By fitting a linear regression model to the data, we estimate the regret order based on the slope of the fitted linear line. The estimated slope is 0.78, which is lower than the worst-case theoretical regret bound with value 1+d𝒮+d𝒜2+d𝒮+d𝒜=78\frac{1+d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2+d\_{\mathcal{S}}+d\_{\mathcal{A}}}=\frac{7}{8}.
This indicates an improved empirical performance relative to the worst-case scenario guarantee.

![Refer to caption](estimated_vpi_initial2_2000.png)


(a) Estimated Vπ~V^{\widetilde{\pi}} (per episode) throughout training.

![Refer to caption](linear_fit_mv_initial2_2000.png)


(b) Estimating regret order via linear regression: log(cumulative regret) with respect to log(episode).

Figure 4: Algorithm performance.

## 7 Conclusion

This work develops a model-based learning framework for episodic control in diffusion-type systems, with unbounded state space, continuous action space, and polynomially growing reward functions. This setting has broad class of applications in finance and economics but less understood in the learning literature. The proposed algorithm incorporates a novel adaptive partitioning scheme, specifically designed to address the challenges posed by the unboundedness and variability of the underlying dynamics. The analytical framework departs significantly from existing approaches in the literature, which typically rely on boundedness assumptions and compact state spaces. We derive regret bounds for the algorithm that recover classical rates in bounded settings and substantially extend their applicability to more general settings. Finally, we validate the effectiveness of our approach through numerical experiments, including applications to high-dimensional problems such as multi-asset mean-variance portfolio selection.

## References

* Almgren and Chriss [2001]

  Robert Almgren and Neil Chriss.
  Optimal execution of portfolio transactions.
  *Journal of Risk*, 3:5–40, 2001.
* Auer et al. [2008]

  Peter Auer, Thomas Jaksch, and Ronald Ortner.
  Near-optimal regret bounds for reinforcement learning.
  *Advances in neural information processing systems*, 21, 2008.
* Azar et al. [2017]

  Mohammad Gheshlaghi Azar, Ian Osband, and Rémi Munos.
  Minimax regret bounds for reinforcement learning.
  In *International conference on machine learning*, pages
  263–272. PMLR, 2017.
* Bayraktar and Kara [2023]

  Erhan Bayraktar and Ali Devran Kara.
  Approximate q learning for controlled diffusion processes and its
  near optimality.
  *SIAM Journal on Mathematics of Data Science*, 5(3):615–638, 2023.
* Bercu and Touati [2008]

  Bernard Bercu and Abderrahmen Touati.
  Exponential inequalities for self-normalized martingales with
  applications.
  *The Annals of Applied Probability*, 18:1848–1869,
  2008.
* Bertsekas and Tsitsiklis [1996]

  Dimitri Bertsekas and John N Tsitsiklis.
  *Neuro-dynamic programming*.
  Athena Scientific, 1996.
* Besson and Kaufmann [2018]

  Lilian Besson and Emilie Kaufmann.
  What doubling tricks can and can’t do for multi-armed bandits.
  *arXiv preprint arXiv:1803.06971*, 2018.
* Bhatia et al. [2017]

  Rajendra Bhatia, Tanvi Jain, and Yongdo Lim.
  On the bures–wasserstein distance between positive definite
  matrices.
  *Expositiones Mathematicae*, 2017.
  URL <https://api.semanticscholar.org/CorpusID:119151863>.
* Black and Litterman [1992]

  Fischer Black and Robert Litterman.
  Global portfolio optimization.
  *Financial analysts journal*, 48(5):28–43,
  1992.
* Blommestein and Turner [2012]

  Hans J Blommestein and Philip Turner.
  Interactions between sovereign debt management and monetary policy
  under fiscal dominance and financial instability.
  2012.
* Bubeck et al. [2011]

  Sébastien Bubeck, Rémi Munos, Gilles Stoltz, and Csaba Szepesvári.
  X-armed bandits.
  *Journal of Machine Learning Research*, 12(5), 2011.
* Carr et al. [2001]

  Peter Carr, Helyette Geman, and Dilip B Madan.
  Pricing and hedging in incomplete markets.
  *Journal of financial economics*, 62(1):131–167, 2001.
* Cartea et al. [2015]

  Álvaro Cartea, Sebastian Jaimungal, and José Penalva.
  *Algorithmic and high-frequency trading*.
  Cambridge University Press, 2015.
* Dai et al. [2025]

  Min Dai, Yuchao Dong, Yanwei Jia, and Xun Yu Zhou.
  Data-driven merton’s strategies via policy randomization.
  *arXiv preprint arXiv*, 2312, 2025.
* Dann et al. [2017]

  Christoph Dann, Tor Lattimore, and Emma Brunskill.
  Unifying pac and regret: Uniform pac bounds for episodic
  reinforcement learning.
  *Advances in Neural Information Processing Systems*, 30, 2017.
* Dayan and Watkins [1992]

  Peter Dayan and CJCH Watkins.
  Q-learning.
  *Machine learning*, 8(3):279–292, 1992.
* Domingues et al. [2021]

  Omar Darwiche Domingues, Pierre Ménard, Matteo Pirotta, Emilie Kaufmann,
  and Michal Valko.
  Kernel-based reinforcement learning: A finite-time analysis.
  In *International Conference on Machine Learning*, pages
  2783–2792. PMLR, 2021.
* Dong et al. [2019]

  Jiayu Dong, Lin F Wang, and Nan Jiang.
  Provably efficient exploration in policy optimization.
  In *NeurIPS*, 2019.
* Du et al. [2020]

  Wenxin Du, Carolin E Pflueger, and Jesse Schreger.
  Sovereign debt portfolios, bond risks, and the credibility of
  monetary policy.
  *The Journal of Finance*, 75(6):3097–3138,
  2020.
* Duffie et al. [1997]

  Darrell Duffie, Wendell Fleming, H Mete Soner, and Thaleia Zariphopoulou.
  Hedging in incomplete markets with hara utility.
  *Journal of Economic Dynamics and Control*, 21(4-5):753–782, 1997.
* Fan et al. [2020]

  Jianqing Fan, Zhaoran Wang, Yuchen Xie, and Zhuoran Yang.
  A theoretical analysis of deep q-learning.
  In *Learning for dynamics and control*, pages 486–489. PMLR,
  2020.
* Fazel et al. [2018]

  Maryam Fazel, Rong Ge, Sham Kakade, and Mehran Mesbahi.
  Global convergence of policy gradient methods for the linear
  quadratic regulator.
  In *International conference on machine learning*, pages
  1467–1476. PMLR, 2018.
* Fu et al. [2020]

  Zuyue Fu, Zhuoran Yang, and Zhaoran Wang.
  Single-timescale actor-critic provably finds globally optimal policy.
  *arXiv preprint arXiv:2008.00483*, 2020.
* Givens and Shortt [1984]

  Clark R. Givens and R. M. Shortt.
  A class of wasserstein metrics for probability distributions.
  *Michigan Mathematical Journal*, 31:231–240, 1984.
  URL <https://api.semanticscholar.org/CorpusID:121338763>.
* Guo et al. [2023]

  Xin Guo, Xinyu Li, and Renyuan Xu.
  Fast policy learning for linear quadratic control with entropy
  regularization.
  *arXiv preprint arXiv:2311.14168*, 2023.
* Hambly et al. [2021]

  Ben Hambly, Renyuan Xu, and Huining Yang.
  Policy gradient methods for the noisy linear quadratic regulator over
  a finite horizon.
  *SIAM Journal on Control and Optimization*, 59(5):3359–3391, 2021.
* Hambly et al. [2023]

  Ben Hambly, Renyuan Xu, and Huining Yang.
  Recent advances in reinforcement learning in finance.
  *Mathematical Finance*, 33(3):437–503,
  2023.
* Han et al. [2023]

  Xia Han, Ruodu Wang, and Xun Yu Zhou.
  Choquet regularization for continuous-time reinforcement learning.
  *SIAM Journal on Control and Optimization*, 61(5):2777–2801, 2023.
* He et al. [2015]

  Xue Dong He, Hanqing Jin, and Xun Yu Zhou.
  Dynamic portfolio choice when risk is measured by weighted var.
  *Mathematics of Operations Research*, 40(3):773–796, 2015.
* Hsu et al. [2011]

  Daniel J. Hsu, Sham M. Kakade, and Tong Zhang.
  A tail inequality for quadratic forms of subgaussian random vectors.
  *ArXiv*, abs/1110.2842, 2011.
  URL <https://api.semanticscholar.org/CorpusID:14207616>.
* Huang et al. [2025]

  Yilie Huang, Yanwei Jia, and Xun Yu Zhou.
  Sublinear regret for a class of continuous-time linear-quadratic
  reinforcement learning problems.
  *SIAM Journal on Control and Optimization*, 63(5):3452–3474, 2025.
* Jaakkola et al. [1993]

  Tommi Jaakkola, Michael Jordan, and Satinder Singh.
  Convergence of stochastic iterative dynamic programming algorithms.
  *Advances in neural information processing systems*, 6, 1993.
* Jia and Zhou [2022]

  Yanwei Jia and Xun Yu Zhou.
  Policy evaluation and temporal-difference learning in continuous time
  and space: A martingale approach.
  *Journal of Machine Learning Research*, 23(154):1–55, 2022.
* Jia and Zhou [2023]

  Yanwei Jia and Xun Yu Zhou.
  q-learning in continuous time.
  *Journal of Machine Learning Research*, 24(161):1–61, 2023.
* Jin et al. [2020]

  Chi Jin, Zhuoran Yang, Zhaoran Wang, and Michael I Jordan.
  Provably efficient reinforcement learning with linear function
  approximation.
  In *Conference on learning theory*, pages 2137–2143. PMLR,
  2020.
* Kakade [2003]

  Sham Machandranath Kakade.
  *On the sample complexity of reinforcement learning*.
  University of London, University College London (United Kingdom),
  2003.
* Kar and Singh [2024]

  Avik Kar and Rahul Singh.
  Adaptive discretization-based non-episodic reinforcement learning in
  metric spaces.
  *arXiv e-prints*, pages arXiv–2405, 2024.
* Kara and Yuksel [2023]

  Ali Devran Kara and Serdar Yuksel.
  Q-learning for continuous state and action mdps under average cost
  criteria.
  *arXiv preprint arXiv:2308.07591*, 2023.
* Kiran et al. [2021]

  B Ravi Kiran, Ibrahim Sobh, Victor Talpaert, Patrick Mannion, Ahmad A
  Al Sallab, Senthil Yogamani, and Patrick Pérez.
  Deep reinforcement learning for autonomous driving: A survey.
  *IEEE transactions on intelligent transportation systems*,
  23(6):4909–4926, 2021.
* Kleinberg et al. [2008]

  Robert Kleinberg, Aleksandrs Slivkins, and Eli Upfal.
  Multi-armed bandits in metric spaces.
  In *Proceedings of the fortieth annual ACM symposium on Theory
  of computing*, pages 681–690, 2008.
* Kleinberg et al. [2019]

  Robert Kleinberg, Aleksandrs Slivkins, and Eli Upfal.
  Bandits and experts in metric spaces.
  *Journal of the ACM (JACM)*, 66(4):1–77,
  2019.
* Kober et al. [2013]

  Jens Kober, J Andrew Bagnell, and Jan Peters.
  Reinforcement learning in robotics: A survey.
  *The International Journal of Robotics Research*, 32(11):1238–1274, 2013.
* Lazaric et al. [2012]

  Alessandro Lazaric, Mohammad Ghavamzadeh, and Rémi Munos.
  Finite-sample analysis of least-squares policy iteration.
  *The Journal of Machine Learning Research*, 13(1):3041–3074, 2012.
* McCallum [1996]

  Andrew Kachites McCallum.
  Reinforcement learning with selective perception and hidden state.
  In *Machine Learning Proceedings 1996*, pages 271–278. Morgan
  Kaufmann, 1996.
* Munos and Moore [2002]

  Rémi Munos and Andrew Moore.
  Variable resolution discretization in optimal control.
  In *Machine Learning*, pages 291–323, 2002.
* Munos and Szepesvári [2008]

  Rémi Munos and Csaba Szepesvári.
  Finite-time bounds for fitted value iteration.
  *Journal of Machine Learning Research*, 9:815–857,
  2008.
* Nguyen et al. [2023]

  Viet Anh Nguyen, Soroosh Shafiee, Damir Filipović, and Daniel Kuhn.
  Mean-covariance robust risk measurement, 2023.
* Ortner et al. [2014]

  Ronald Ortner, Daniil Ryabko, and Peter Auer.
  Regret bounds for reinforcement learning with model selection.
  *Machine Learning*, 96(3):217–261, 2014.
* Pazis and Parr [2013]

  Jason Pazis and Ronald Parr.
  Pac optimal exploration in continuous space markov decision
  processes.
  In *AAAI*, 2013.
* Puterman [2014]

  Martin L Puterman.
  *Markov decision processes: discrete stochastic dynamic
  programming*.
  John Wiley & Sons, 2014.
* Schmitt [1992]

  Bernhard A. Schmitt.
  Perturbation bounds for matrix square roots and pythagorean sums.
  *Linear Algebra and its Applications*, 174:215–227,
  1992.
  ISSN 0024-3795.
  doi: https://doi.org/10.1016/0024-3795(92)90052-C.
  URL
  <https://www.sciencedirect.com/science/article/pii/002437959290052C>.
* Shalev-Shwartz et al. [2016]

  Shai Shalev-Shwartz, Shaked Shammah, and Amnon Shashua.
  Safe, multi-agent, reinforcement learning for autonomous driving.
  *arXiv preprint arXiv:1610.03295*, 2016.
* Sinclair et al. [2023]

  Sean R Sinclair, Siddhartha Banerjee, and Christina Lee Yu.
  Adaptive discretization in online reinforcement learning.
  *Operations Research*, 71(5):1636–1652,
  2023.
* Slivkins [2011]

  Aleksandrs Slivkins.
  Contextual bandits with similarity information.
  In *Proceedings of the 24th annual Conference On Learning
  Theory*, pages 679–702. JMLR Workshop and Conference Proceedings, 2011.
* Strehl and Littman [2006]

  Alexander L Strehl and Michael L Littman.
  Pac model-free reinforcement learning.
  In *ICML*, 2006.
* Tektas et al. [2005]

  Arzu Tektas, E Nur Ozkan-Gunay, and Gokhan Gunay.
  Asset and liability management in financial crisis.
  *The Journal of Risk Finance*, 6(2):135–149, 2005.
* Tsitsiklis and Van Roy [1996]

  John Tsitsiklis and Benjamin Van Roy.
  Analysis of temporal-diffference learning with function
  approximation.
  *Advances in neural information processing systems*, 9, 1996.
* Vershynin [2018]

  Roman Vershynin.
  *High-dimensional probability: An introduction with applications
  in data science*, volume 47.
  Cambridge university press, 2018.
* Wainwright [2019]

  Martin J Wainwright.
  *High-dimensional statistics: A non-asymptotic viewpoint*,
  volume 48.
  Cambridge university press, 2019.
* Wang et al. [2020]

  Haoran Wang, Thaleia Zariphopoulou, and Xun Yu Zhou.
  Reinforcement learning in continuous time and space: A stochastic
  control approach.
  *Journal of Machine Learning Research*, 21(198):1–34, 2020.
* Wang et al. [2019]

  Lingxiao Wang, Qi Cai, Zhuoran Yang, and Zhaoran Wang.
  Neural policy gradient methods: Global optimality and rates of
  convergence.
  *arXiv preprint arXiv:1909.01150*, 2019.
* Winkelbauer [2012]

  Andreas Winkelbauer.
  Moments and absolute moments of the normal distribution.
  *arXiv preprint arXiv:1209.4340*, 2012.
* Yong and Zhou [1999]

  Jiongmin Yong and Xun Yu Zhou.
  *Stochastic controls: Hamiltonian systems and HJB equations*,
  volume 43.
  Springer Science & Business Media, 1999.
* Yu et al. [2021]

  Chao Yu, Jiming Liu, Shamim Nemati, and Guosheng Yin.
  Reinforcement learning in healthcare: A survey.
  *ACM Computing Surveys (CSUR)*, 55(1):1–36,
  2021.
* Zhang and Suen [2025]

  Suyanpeng Zhang and Sze-chuan Suen.
  State discretization for continuous-state mdps in infectious disease
  control.
  *IISE Transactions on Healthcare Systems Engineering*,
  15(1):96–115, 2025.
* Zhao et al. [2020]

  Wenshuai Zhao, Jorge Peña Queralta, and Tomi Westerlund.
  Sim-to-real transfer in deep reinforcement learning for robotics: a
  survey.
  In *2020 IEEE symposium series on computational intelligence
  (SSCI)*, pages 737–744. IEEE, 2020.
* Zhou and Li [2000]

  Xun Yu Zhou and Duan Li.
  Continuous-time mean-variance portfolio selection: A stochastic lq
  framework.
  *Applied Mathematics and Optimization*, 42:19–33,
  2000.

## Appendix A Technical details in Section [2](https://arxiv.org/html/2512.14991v1#S2 "2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

### A.1 Proof of Proposition [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

We first prove 𝔼​[‖X2‖p]<c˘1​(1+𝔼​[‖X1‖p])\mathbb{E}[\|X\_{2}\|^{p}]<\breve{c}\_{1}(1+\mathbb{E}[\|X\_{1}\|^{p}]) for some constant c˘1\breve{c}\_{1}.
By the dynamics of state process, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖X2‖\displaystyle\|X\_{2}\| | ≤\displaystyle\leq | ‖X1‖+‖μ1​(X1,A1)‖​Δ+‖σ1​(X1,A1)‖​‖B1‖​Δ\displaystyle\|X\_{1}\|+\|\mu\_{1}(X\_{1},A\_{1})\|\Delta+\|\sigma\_{1}(X\_{1},A\_{1})\|\|B\_{1}\|\sqrt{\Delta} |  |
|  |  | ≤\displaystyle\leq | ‖X1‖+(L0+ℓμ​(‖X1‖+a¯))​Δ+(L0+ℓσ​(‖X1‖+a¯))​‖B1‖​Δ\displaystyle\|X\_{1}\|+(L\_{0}+\ell\_{\mu}(\|X\_{1}\|+\bar{a}))\Delta+(L\_{0}+\ell\_{\sigma}(\|X\_{1}\|+\bar{a}))\|B\_{1}\|\sqrt{\Delta} |  |
|  |  | =\displaystyle= | (1+ℓμ​Δ+ℓσ​‖B1‖​Δ)​‖X1‖+(ℓμ​a¯+L0)​Δ+(ℓσ​a¯+L0)​‖B1‖​Δ.\displaystyle(1+\ell\_{\mu}\Delta+\ell\_{\sigma}\|B\_{1}\|\sqrt{\Delta})\|X\_{1}\|+(\ell\_{\mu}\bar{a}+L\_{0})\Delta+(\ell\_{\sigma}\bar{a}+L\_{0})\|B\_{1}\|\sqrt{\Delta}. |  |

So for any p≥1p\geq 1, there exists a constant c˘3\breve{c}\_{3} depending on pp only, such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖X2‖p\displaystyle\|X\_{2}\|^{p} | ≤\displaystyle\leq | c˘3​((1+ℓμ​Δ+ℓσ​‖B1‖​Δ)p​‖X1‖p+((ℓμ​a¯+L0)​Δ+(ℓσ​a¯+L0)​‖B1‖​Δ)p)\displaystyle\breve{c}\_{3}\left((1+\ell\_{\mu}\Delta+\ell\_{\sigma}\|B\_{1}\|\sqrt{\Delta})^{p}\|X\_{1}\|^{p}+((\ell\_{\mu}\bar{a}+L\_{0})\Delta+(\ell\_{\sigma}\bar{a}+L\_{0})\|B\_{1}\|\sqrt{\Delta})^{p}\right) |  |
|  |  | ≤\displaystyle\leq | c˘3​(c˘3​(1+ℓμp​Δp+ℓσp​‖B1‖p​Δp/2)​‖X1‖p+c˘3​((ℓμ​a¯+L0)p​Δp+(ℓσ​a¯+L0)p​‖B1‖p​Δp2)).\displaystyle\breve{c}\_{3}\left(\breve{c}\_{3}(1+\ell\_{\mu}^{p}\Delta^{p}+\ell\_{\sigma}^{p}\|B\_{1}\|^{p}\Delta^{p/2})\|X\_{1}\|^{p}+\breve{c}\_{3}((\ell\_{\mu}\bar{a}+L\_{0})^{p}\Delta^{p}+(\ell\_{\sigma}\bar{a}+L\_{0})^{p}\|B\_{1}\|^{p}\Delta^{\frac{p}{2}})\right). |  |

Together with the fact that B1B\_{1} is independent with X1X\_{1}, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝔼​[‖X2‖p]\displaystyle\mathbb{E}[\|X\_{2}\|^{p}] | ≤\displaystyle\leq | c˘32((1+ℓμpΔp+ℓσp𝔼[∥B1∥p]Δp/2)𝔼[∥X1∥p]\displaystyle\breve{c}\_{3}^{2}\Big((1+\ell\_{\mu}^{p}\Delta^{p}+\ell\_{\sigma}^{p}\mathbb{E}[\|B\_{1}\|^{p}]\Delta^{p/2})\mathbb{E}[\|X\_{1}\|^{p}] |  | (A.1) |
|  |  |  | +(ℓμa¯+L0)pΔp+(ℓσa¯+L0)p𝔼[∥B1∥p]Δp2)\displaystyle+(\ell\_{\mu}\bar{a}+L\_{0})^{p}\Delta^{p}+(\ell\_{\sigma}\bar{a}+L\_{0})^{p}\mathbb{E}[\|B\_{1}\|^{p}]\Delta^{\frac{p}{2}}\Big) |  |
|  |  | ≤\displaystyle\leq | c˘4​(1+𝔼​[‖X1‖p]),\displaystyle\breve{c}\_{4}(1+\mathbb{E}[\|X\_{1}\|^{p}]), |  |

for some constant c˘4\breve{c}\_{4} depending only on p,Δ,ℓμ,ℓσ,a¯,L0p,\Delta,\ell\_{\mu},\ell\_{\sigma},\bar{a},L\_{0}.

By the same argument, we have
𝔼[∥X3∥p]≤c˘4(1+𝔼[∥X2∥p)≤c˘5(1+𝔼[∥X1∥p])\mathbb{E}[\|X\_{3}\|^{p}]\leq\breve{c}\_{4}(1+\mathbb{E}[\|X\_{2}\|^{p})\leq\breve{c}\_{5}(1+\mathbb{E}[\|X\_{1}\|^{p}])
for some c˘5\breve{c}\_{5} depending only on c˘4,\breve{c}\_{4},
as well as 𝔼​[‖Xh‖p]≤c˘h+2​(1+𝔼​[‖X1‖p])\mathbb{E}[\|X\_{h}\|^{p}]\leq\breve{c}\_{h+2}(1+\mathbb{E}[\|X\_{1}\|^{p}]) for some c˘h+3\breve{c}\_{h+3} depending only on p,Δ,ℓμ,ℓσ,a¯,L0p,\Delta,\ell\_{\mu},\ell\_{\sigma},\bar{a},L\_{0}.

Finally,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[suph∈[H]‖Xh‖p]<∑h∈[H]𝔼​[‖Xh‖p]≤M​(1+𝔼​[‖X1‖p]),\mathbb{E}\left[\sup\_{h\in[H]}\|X\_{h}\|^{p}\right]<\sum\_{h\in[H]}\mathbb{E}[\|X\_{h}\|^{p}]\leq M(1+\mathbb{E}[\|X\_{1}\|^{p}]), |  |

where MM only depends on p,Δ,ℓμ,ℓσ,a¯,L0p,\Delta,\ell\_{\mu},\ell\_{\sigma},\bar{a},L\_{0} and HH.

∎

### A.2 Proof of Proposition [2.4](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem4 "Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

In this proof, we will often use the fact that for any functions ff and gg on the same domain, we have

|  |  |  |
| --- | --- | --- |
|  | |maxx⁡f​(x)−maxy⁡g​(y)|≤maxx⁡|f​(x)−g​(x)|;|\max\_{x}f(x)-\max\_{y}g(y)|\leq\max\_{x}|f(x)-g(x)|; |  |

and for any nonnegative real numbers a,b,ca,b,c, any integer m>0m>0,

|  |  |  |
| --- | --- | --- |
|  | (a+b+c)m≤k3​(m)​(am+bm+cm)(a+b+c)^{m}\leq k\_{3}(m)(a^{m}+b^{m}+c^{m}) |  |

for some function k3​(⋅)k\_{3}(\cdot).

We prove the statement by backward induction. For the last step h=Hh=H, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |VH∗​(x1)−VH∗​(x2)|\displaystyle\left|V^{\*}\_{H}(x\_{1})-V\_{H}^{\*}(x\_{2})\right| | =\displaystyle= | |maxa∈A⁡R¯H​(x1,a)−maxb∈A⁡R¯H​(x2,b)|\displaystyle\left|\max\_{a\in A}\bar{R}\_{H}(x\_{1},a)-\max\_{b\in A}\bar{R}\_{H}(x\_{2},b)\right| |  |
|  |  | ≤\displaystyle\leq | maxa∈A⁡|R¯H​(x1,a)−R¯H​(x2,a)|\displaystyle\max\_{a\in A}|\bar{R}\_{H}(x\_{1},a)-\bar{R}\_{H}(x\_{2},a)| |  |
|  |  | ≤\displaystyle\leq | ℓr​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖).\displaystyle\ell\_{r}\Big(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m}\Big)\,\Big(\|x\_{1}-x\_{2}\|\Big). |  |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯H:=ℓr,\displaystyle\overline{C}\_{H}:=\ell\_{r}, |  | (A.2) |

with ℓr\ell\_{r} defined in ([2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Now suppose the inequality ([2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for h=j>0h=j>0. We study the inequality for h=j−1h=j-1. For any state x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}} and any action a∈𝒜a\in\mathcal{A}, denote by X(x,a):=x+μj−1​(x,a)​Δ+σj−1​(x,a)​Bj−1​ΔX^{(x,a)}:=x+\mu\_{j-1}(x,a)\Delta+\sigma\_{j-1}(x,a)B\_{j-1}\sqrt{\Delta}.

From ([2.3](https://arxiv.org/html/2512.14991v1#S2.E3 "In Bellman equation for optimal policy. ‣ 2.1 Value function, Bellman equations and evaluation criterion ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we know that
Vj−1∗​(x)=maxa∈A⁡{R¯j−1​(x,a)+𝔼​[Vj∗​(X(x,a))]}V^{\*}\_{j-1}(x)=\max\_{a\in A}\{\bar{R}\_{j-1}(x,a)+\mathbb{E}[V\_{j}^{\*}(X^{(x,a)})]\}. Hence,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | |Vj−1∗​(x)−Vj−1∗​(y)|\displaystyle|V^{\*}\_{j-1}(x)-V^{\*}\_{j-1}(y)| |  | (A.3) |
|  |  | ≤\displaystyle\leq | maxa∈A⁡|R¯j−1​(x,a)+𝔼​[Vj∗​(X(x,a))]−R¯j−1​(y,a)−𝔼​[Vj∗​(X(y,a))]|\displaystyle\max\_{a\in A}|\bar{R}\_{j-1}(x,a)+\mathbb{E}[V^{\*}\_{j}(X^{(x,a)})]-\bar{R}\_{j-1}(y,a)-\mathbb{E}[V^{\*}\_{j}(X^{(y,a)})]| |  |
|  |  | ≤\displaystyle\leq | maxa∈A⁡|R¯j−1​(x,a)−R¯j−1​(y,a)|+maxa∈A⁡𝔼​[|Vj∗​(X(x,a))−Vj∗​(X(y,a))|].\displaystyle\max\_{a\in A}|\bar{R}\_{j-1}(x,a)-\bar{R}\_{j-1}(y,a)|+\max\_{a\in A}\mathbb{E}[|V^{\*}\_{j}(X^{(x,a)})-V^{\*}\_{j}(X^{(y,a)})|]. |  |

The first term in ([A.3](https://arxiv.org/html/2512.14991v1#A1.E3 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) is bounded by
ℓr​(1+‖x‖m+‖y‖m)​‖x−y‖\ell\_{r}(1+\|x\|^{m}+\|y\|^{m})\|x-y\|, so it suffices to estimate the second term in ([A.3](https://arxiv.org/html/2512.14991v1#A1.E3 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

By the induction hypothesis, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Vj∗​(X(x,a))−Vj∗​(X(y,a))|≤C¯j​(1+‖X(x,a)‖m+‖X(y,a)‖m)​‖X(x,a)−X(y,a)‖.\displaystyle|V^{\*}\_{j}(X^{(x,a)})-V^{\*}\_{j}(X^{(y,a)})|\leq\overline{C}\_{j}(1+\|X^{(x,a)}\|^{m}+\|X^{(y,a)}\|^{m})\|X^{(x,a)}-X^{(y,a)}\|. |  | (A.4) |

Note that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖X(x,a)‖m\displaystyle\|X^{(x,a)}\|^{m} | ≤\displaystyle\leq | (‖x‖+(L0+ℓμ​(‖x‖+a¯))​Δ+(L0+ℓσ​(‖x‖+a¯))​‖Bj−1‖​Δ)m\displaystyle\left(\|x\|+(L\_{0}+\ell\_{\mu}(\|x\|+\bar{a}))\Delta+(L\_{0}+\ell\_{\sigma}(\|x\|+\bar{a}))\|B\_{j-1}\|\sqrt{\Delta}\right)^{m} |  | (A.5) |
|  |  | ≤\displaystyle\leq | k3(m)(1+ℓμΔ)m∥x∥m+((L0+a¯)ℓμΔ)m+(L0+ℓσ(∥x∥+a¯))m∥Bj−1∥m)\displaystyle k\_{3}(m)\left(1+\ell\_{\mu}\Delta)^{m}\|x\|^{m}+((L\_{0}+\bar{a})\ell\_{\mu}\Delta)^{m}+(L\_{0}+\ell\_{\sigma}(\|x\|+\bar{a}))^{m}\|B\_{j-1}\|^{m}\right) |  |
|  |  | =\displaystyle= | c˘1+c˘2​‖Bj−1‖m+(c˘3+c˘4​‖Bj−1‖m)​‖x‖m,\displaystyle\breve{c}\_{1}+\breve{c}\_{2}\|B\_{j-1}\|^{m}+(\breve{c}\_{3}+\breve{c}\_{4}\|B\_{j-1}\|^{m})\|x\|^{m}, |  |

where c˘i\breve{c}\_{i} are all constant depending only on m,ℓμ,ℓσ,Δ,L0,a¯m,\ell\_{\mu},\ell\_{\sigma},\Delta,L\_{0},\bar{a}. Hence, we also have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ‖X(x,a)−X(y,a)‖\displaystyle\|X^{(x,a)}-X^{(y,a)}\| |  | (A.6) |
|  |  | ≤\displaystyle\leq | ‖x−y‖+‖μj−1​(x,a)−μj−1​(y,a)‖​Δ+‖σj−1​(x,a)−σj−1​(y,a)‖​Δ​‖Bj−1‖\displaystyle\|x-y\|+\|\mu\_{j-1}(x,a)-\mu\_{j-1}(y,a)\|\Delta+\|\sigma\_{j-1}(x,a)-\sigma\_{j-1}(y,a)\|\sqrt{\Delta}\|B\_{j-1}\| |  |
|  |  | ≤\displaystyle\leq | (1+ℓμ​Δ)​‖x−y‖+ℓσ​‖x−y‖​Δ​‖Bj−1‖.\displaystyle(1+\ell\_{\mu}\Delta)\|x-y\|+\ell\_{\sigma}\|x-y\|\sqrt{\Delta}\|B\_{j-1}\|. |  |

By ([A.5](https://arxiv.org/html/2512.14991v1#A1.E5 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([A.6](https://arxiv.org/html/2512.14991v1#A1.E6 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ‖X(x,a)‖m​‖X(x,a)−X(y,a)‖\displaystyle\|X^{(x,a)}\|^{m}\|X^{(x,a)}-X^{(y,a)}\| |  | (A.7) |
|  |  | ≤\displaystyle\leq | ((c˘1+c˘2∥Bj−1∥m)+(c˘3+c˘4∥Bj−1∥m))∥x∥m)(1+ℓμΔ+ℓσΔ∥Bj−1∥)∥x−y∥\displaystyle\Big((\breve{c}\_{1}+\breve{c}\_{2}\|B\_{j-1}\|^{m})+(\breve{c}\_{3}+\breve{c}\_{4}\|B\_{j-1}\|^{m}))\|x\|^{m}\Big)(1+\ell\_{\mu}\Delta+\ell\_{\sigma}\sqrt{\Delta}\|B\_{j-1}\|)\|x-y\| |  |
|  |  | =\displaystyle= | ‖x−y‖​(f1​(‖Bj−1‖)+f2​(‖Bj−1‖)​‖x‖m),\displaystyle\|x-y\|\Big(f\_{1}(\|B\_{j-1}\|)+f\_{2}(\|B\_{j-1}\|)\|x\|^{m}\Big), |  |

where f1​(z)=c˘5+c˘6​z+c˘7​zm+c˘8​zm+1f\_{1}(z)=\breve{c}\_{5}+\breve{c}\_{6}z+\breve{c}\_{7}z^{m}+\breve{c}\_{8}z^{m+1}
and f2​(z)=c˘9+c˘10​z+c˘11​zm+c˘12​zm+1f\_{2}(z)=\breve{c}\_{9}+\breve{c}\_{10}z+\breve{c}\_{11}z^{m}+\breve{c}\_{12}z^{m+1},
with c˘i\breve{c}\_{i} depends only on C¯j,m,a¯,Δ,ℓμ,ℓσ,L0\overline{C}\_{j},m,\bar{a},\Delta,\ell\_{\mu},\ell\_{\sigma},L\_{0}.

By the fact that 𝔼​[‖Bj−1‖q]\mathbb{E}\big[\|B\_{j-1}\|^{q}\big] is a finite constant for any integer qq, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖X(x,a)‖m​‖X(x,a)−X(y,a)‖]≤c˘13​(1+‖x‖m)​‖x−y‖.\displaystyle\mathbb{E}\big[\|X^{(x,a)}\|^{m}\|X^{(x,a)}-X^{(y,a)}\|\big]\leq\breve{c}\_{13}(1+\|x\|^{m})\|x-y\|. |  | (A.8) |

for some c˘13\breve{c}\_{13} only depending on C¯j,m,a¯,Δ,ℓμ,ℓσ,L0\overline{C}\_{j},m,\bar{a},\Delta,\ell\_{\mu},\ell\_{\sigma},L\_{0}.

Similarly, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖X(y,a)‖m​‖X(x,a)−X(y,a)‖]≤c˘13​(1+‖x‖m)​‖x−y‖.\displaystyle\mathbb{E}[\|X^{(y,a)}\|^{m}\|X^{(x,a)}-X^{(y,a)}\|]\leq\breve{c}\_{13}(1+\|x\|^{m})\|x-y\|. |  | (A.9) |

Applying ([A.6](https://arxiv.org/html/2512.14991v1#A1.E6 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([A.8](https://arxiv.org/html/2512.14991v1#A1.E8 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([A.9](https://arxiv.org/html/2512.14991v1#A1.E9 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) to ([A.4](https://arxiv.org/html/2512.14991v1#A1.E4 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Vj−1∗​(X(x,a))−Vj−1∗​(X(y,a))]≤c˘14​(1+‖x‖m+‖y‖m)​‖x−y‖,\displaystyle\mathbb{E}\left[V^{\*}\_{j-1}(X^{(x,a)})-V^{\*}\_{j-1}(X^{(y,a)})\right]\leq\breve{c}\_{14}(1+\|x\|^{m}+\|y\|^{m})\|x-y\|, |  | (A.10) |

with c˘14=C¯j​(2​c˘9+(1+ℓμ​Δ+ℓσ​Δ​𝔼​[‖Bj−1‖]))\breve{c}\_{14}=\overline{C}\_{j}\Big(2\breve{c}\_{9}+(1+\ell\_{\mu}\Delta+\ell\_{\sigma}\sqrt{\Delta}\mathbb{E}[\|B\_{j-1}\|])\Big).

Finally, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯j−1:=ℓr+c˘14,\displaystyle\overline{C}\_{j-1}:=\ell\_{r}+\breve{c}\_{14}, |  | (A.11) |

and we have shown that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Vj−1∗​(x)−Vj−1∗​(y)|≤C¯j−1​(1+‖x‖m+‖y‖m)​‖x−y‖.\displaystyle|V^{\*}\_{j-1}(x)-V^{\*}\_{j-1}(y)|\leq\overline{C}\_{j-1}(1+\|x\|^{m}+\|y\|^{m})\|x-y\|. |  | (A.12) |

∎

### A.3 Proof of Proposition [2.5](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

We prove the statement by backward induction.

For the last step h=Hh=H,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |VHπ​(x)|\displaystyle|V\_{H}^{\pi}(x)| | =\displaystyle= | |𝔼a∼πH​(x)​[R¯H​(x,a)]|\displaystyle|\mathbb{E}\_{a\sim\pi\_{H}(x)}[\bar{R}\_{H}(x,a)]| |  | (A.13) |
|  |  | ≤\displaystyle\leq | 𝔼a∼πH​(x)​[|R¯H​(x,a)−R¯H​(0,0)|+|R¯H​(0,0)|]\displaystyle\mathbb{E}\_{a\sim\pi\_{H}(x)}[|\bar{R}\_{H}(x,a)-\bar{R}\_{H}(0,0)|+|\bar{R}\_{H}(0,0)|] |  |
|  |  | ≤\displaystyle\leq | ℓr​(‖x‖m+1)​(‖x‖+a¯)+L0\displaystyle\ell\_{r}(\|x\|^{m}+1)(\|x\|+\bar{a})+L\_{0} |  |
|  |  | ≤\displaystyle\leq | ℓr​‖x‖m+1+ℓr​a¯​(mm+1​‖x‖m+1+1m+1)+ℓr​(1m+1​‖x‖m+1+mm+1)+ℓr​a¯+L0\displaystyle\ell\_{r}\|x\|^{m+1}+\ell\_{r}\bar{a}\left(\frac{m}{m+1}\|x\|^{m+1}+\frac{1}{m+1}\right)+\ell\_{r}\left(\frac{1}{m+1}\|x\|^{m+1}+\frac{m}{m+1}\right)+\ell\_{r}\bar{a}+L\_{0} |  |
|  |  | ≤\displaystyle\leq | C~H​(‖x‖m+1+1),\displaystyle\widetilde{C}\_{H}(\|x\|^{m+1}+1), |  |

where C~H:=max⁡{ℓr​(1+a¯​m+1m+1),ℓr​(a¯+mm+1+a¯)+L0}\widetilde{C}\_{H}:=\max\{\ell\_{r}(1+\frac{\bar{a}m+1}{m+1}),\ell\_{r}(\frac{\bar{a}+m}{m+1}+\bar{a})+L\_{0}\}. Here, the first equality holds by ([2.1](https://arxiv.org/html/2512.14991v1#S2.Ex5 "Bellman equation for generic policy. ‣ 2.1 Value function, Bellman equations and evaluation criterion ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the second inequality holds by Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), and the third inequality holds due to the fact that ‖x‖m≤mm+1​‖x‖m+1+1m+1\|x\|^{m}\leq\frac{m}{m+1}\|x\|^{m+1}+\frac{1}{m+1} and ‖x‖≤1m+1​‖x‖m+1+mm+1\|x\|\leq\frac{1}{m+1}\|x\|^{m+1}+\frac{m}{m+1} . Now suppose the inequality ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for h=j>0h=j>0. We now prove the inequality for h=j−1h=j-1:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |Vj−1π​(x)|\displaystyle|V\_{j-1}^{\pi}(x)| | ≤\displaystyle\leq | 𝔼a∼πj−1​(x)​[|R¯j−1​(x,a)|]+𝔼Xj∼Tj−1(⋅|x,a),a∼πj−1(x)​[|Vjπ​(Xj)||Xj−1=x]\displaystyle\mathbb{E}\_{a\sim\pi\_{j-1}(x)}\Big[|\bar{R}\_{j-1}(x,a)|\Big]+\mathbb{E}\_{X\_{j}\sim T\_{j-1}(\cdot|x,a),a\sim\pi\_{j-1}(x)}\Big[\Big|V\_{j}^{\pi}(X\_{j})\Big||X\_{j-1}=x\Big] |  | (A.14) |
|  |  | ≤\displaystyle\leq | ℓr​(‖x‖m+1)​(a¯+‖x‖)+L0+𝔼Xj∼Tj−1(⋅|x,a),a∼πj−1(x)​[C~j​(‖Xj‖m+1+1)|Xj−1=x]\displaystyle\ell\_{r}(\|x\|^{m}+1)(\overline{a}+\|x\|)+L\_{0}+\mathbb{E}\_{X\_{j}\sim T\_{j-1}(\cdot|x,a),a\sim\pi\_{j-1}(x)}\Big[\widetilde{C}\_{j}(\|X\_{j}\|^{m+1}+1)|X\_{j-1}=x\Big] |  |
|  |  | ≤\displaystyle\leq | ℓr​‖x‖m+1+ℓr​a¯​(mm+1​‖x‖m+1+1m+1)+ℓr​(1m+1​‖x‖m+1+mm+1)+ℓr​a¯+L0\displaystyle\ell\_{r}\|x\|^{m+1}+\ell\_{r}\bar{a}\left(\frac{m}{m+1}\|x\|^{m+1}+\frac{1}{m+1}\right)+\ell\_{r}\left(\frac{1}{m+1}\|x\|^{m+1}+\frac{m}{m+1}\right)+\ell\_{r}\bar{a}+L\_{0} |  |
|  |  |  | +C~j+C~j​c˘4​(1+‖x‖m+1)\displaystyle+\widetilde{C}\_{j}+\widetilde{C}\_{j}\breve{c}\_{4}(1+\|x\|^{m+1}) |  |
|  |  | ≤\displaystyle\leq | C~j−1​(‖x‖m+1+1),\displaystyle\widetilde{C}\_{j-1}(\|x\|^{m+1}+1), |  |

where c˘4\breve{c}\_{4} depends only on m,Δ,ℓμ,ℓσ,a¯,L0m,\Delta,\ell\_{\mu},\ell\_{\sigma},\bar{a},L\_{0}, and we define C~j−1:=max{ℓr(1+a¯​m+1m+1)+C~jc˘4,ℓr(a¯+mm+1+a¯+C~j}\widetilde{C}\_{j-1}:=\max\{\ell\_{r}(1+\frac{\bar{a}m+1}{m+1})+\widetilde{C}\_{j}\breve{c}\_{4},\ell\_{r}(\frac{\bar{a}+m}{m+1}+\bar{a}+\widetilde{C}\_{j}\}. Here, the first inequality holds due to ([2.1](https://arxiv.org/html/2512.14991v1#S2.Ex5 "Bellman equation for generic policy. ‣ 2.1 Value function, Bellman equations and evaluation criterion ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and triangle inequality, the second inequality holds by Assumption [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). In addition, the third inequality holds due to the fact that ‖x‖m≤mm+1​‖x‖m+1+1m+1\|x\|^{m}\leq\frac{m}{m+1}\|x\|^{m+1}+\frac{1}{m+1}, ‖x‖≤1m+1​‖x‖m+1+mm+1\|x\|\leq\frac{1}{m+1}\|x\|^{m+1}+\frac{m}{m+1} and an argument simular to ([A.1](https://arxiv.org/html/2512.14991v1#A1.E1 "In A.1 Proof of Proposition 2.2 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼Xj∼Tj−1(⋅|x,a),a∼πj−1(x)​[‖Xj‖m+1|Xj−1=x]≤c˘4​(1+‖x‖m+1).\displaystyle\mathbb{E}\_{X\_{j}\sim T\_{j-1}(\cdot|x,a),a\sim\pi\_{j-1}(x)}\Big[\|X\_{j}\|^{m+1}|X\_{j-1}=x\Big]\leq\breve{c}\_{4}(1+\|x\|^{m+1}). |  |

∎

### A.4 Local lipschitz property for optimal Q function

In this subsection, we establish the local Lipschitz property of the optimal QQ-function. This result plays an important role in the proof of Lemma [5.17](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem17 "Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). The proof follows the same general strategy as that for the Lipschitz property of the optimal value function. For completeness, we present the full argument here.

###### Proposition A.1.

Suppose Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [2.2](https://arxiv.org/html/2512.14991v1#S2.Thmassumption2 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. Then for all h∈[H]h\in[H], it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Qh∗​(x1,a1)−Qh∗​(x2,a2)|≤2​C¯h​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖+‖a1−a2‖),\displaystyle|Q\_{h}^{\*}(x\_{1},a\_{1})-Q\_{h}^{\*}(x\_{2},a\_{2})|\leq 2\overline{C}\_{h}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|), |  | (A.15) |

where C¯h\overline{C}\_{h} is defined in ([2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Proof.

We prove the statement by backward induction. For the last step h=Hh=H, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |QH∗​(x1,a1)−QH∗​(x2,a2)|\displaystyle|Q\_{H}^{\*}(x\_{1},a\_{1})-Q\_{H}^{\*}(x\_{2},a\_{2})| | =\displaystyle= | |R¯H​(x1,a1)−R¯H​(x2,a2)|\displaystyle|\bar{R}\_{H}(x\_{1},a\_{1})-\bar{R}\_{H}(x\_{2},a\_{2})| |  |
|  |  | ≤\displaystyle\leq | ℓr​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖+‖a1−a2‖)\displaystyle\ell\_{r}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|) |  |
|  |  | ≤\displaystyle\leq | 2​C¯H​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖+‖a1−a2‖),\displaystyle 2\overline{C}\_{H}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|), |  |

where the first inequality holds due to ([2.2](https://arxiv.org/html/2512.14991v1#S2.Ex14 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the second inequality holds due to the fact that C¯H=ℓr\overline{C}\_{H}=\ell\_{r} by ([A.2](https://arxiv.org/html/2512.14991v1#A1.E2 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Then suppose the inequality ([A.15](https://arxiv.org/html/2512.14991v1#A1.E15 "In Proposition A.1. ‣ A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for h=j>1h=j>1. We then study the inequality for h=j−1h=j-1.

For any state xx at time j−1j-1 and any action a∈𝒜a\in\mathcal{A}, denote by X(x,a):=x+μj−1​(x,a)​Δ+σj−1​(x,a)​Bj−1​ΔX^{(x,a)}:=x+\mu\_{j-1}(x,a)\Delta+\sigma\_{j-1}(x,a)B\_{j-1}\sqrt{\Delta} the next state.

By ([2.4](https://arxiv.org/html/2512.14991v1#S2.E4 "In Bellman equation for optimal policy. ‣ 2.1 Value function, Bellman equations and evaluation criterion ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) we know
Qj−1∗​(x,a)=R¯j−1​(x,a)+𝔼​[Vj∗​(X(x,a))].Q^{\*}\_{j-1}(x,a)=\bar{R}\_{j-1}(x,a)+\mathbb{E}[V\_{j}^{\*}(X^{(x,a)})].

Therefore

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | |Qj−1∗​(x1,a1)−Qj−1∗​(x2,a2)|\displaystyle|Q\_{j-1}^{\*}(x\_{1},a\_{1})-Q\_{j-1}^{\*}(x\_{2},a\_{2})| |  | (A.16) |
|  |  | ≤\displaystyle\leq | |Qj−1∗​(x1,a1)−Qj−1∗​(x2,a1)|+|Qj−1∗​(x2,a1)−Qj−1∗​(x2,a2)|\displaystyle|Q\_{j-1}^{\*}(x\_{1},a\_{1})-Q\_{j-1}^{\*}(x\_{2},a\_{1})|+|Q\_{j-1}^{\*}(x\_{2},a\_{1})-Q\_{j-1}^{\*}(x\_{2},a\_{2})| |  |
|  |  | ≤\displaystyle\leq | |R¯j−1​(x1,a1)−R¯j−1​(x2,a1)|+|R¯j−1​(x2,a1)−R¯j−1​(x2,a2)|⏟(I)\displaystyle\underbrace{|\bar{R}\_{j-1}(x\_{1},a\_{1})-\bar{R}\_{j-1}(x\_{2},a\_{1})|+|\bar{R}\_{j-1}(x\_{2},a\_{1})-\bar{R}\_{j-1}(x\_{2},a\_{2})|}\_{(I)} |  |
|  |  |  | +𝔼​[|Vj∗​(X(x1,a1))−Vj∗​(X(x2,a1))|]⏟(I​I)+𝔼​[|Vj∗​(X(x2,a1))−Vj∗​(X(x2,a2))|]⏟(I​I​I).\displaystyle+\underbrace{\mathbb{E}[|V\_{j}^{\*}(X^{(x\_{1},a\_{1})})-V\_{j}^{\*}(X^{(x\_{2},a\_{1})})|]}\_{(II)}+\underbrace{\mathbb{E}[|V\_{j}^{\*}(X^{(x\_{2},a\_{1})})-V\_{j}^{\*}(X^{(x\_{2},a\_{2})})|]}\_{(III)}. |  |

For term (I), by ([2.2](https://arxiv.org/html/2512.14991v1#S2.Ex14 "Assumption 2.2 (Regularity of the reward). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I)≤ℓr​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖+‖a1−a2‖).\displaystyle(I)\leq\ell\_{r}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|). |  | (A.17) |

For term (II), by ([A.10](https://arxiv.org/html/2512.14991v1#A1.E10 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I​I)≤c˘14​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖,\displaystyle(II)\leq\breve{c}\_{14}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})\|x\_{1}-x\_{2}\|, |  | (A.18) |

where c˘14\breve{c}\_{14} is defined in ([A.10](https://arxiv.org/html/2512.14991v1#A1.E10 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Next, we handle term (III). By Theorem [2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"),
we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Vj∗​(X(x2,a1))−Vj∗​(X(x2,a2))|≤C¯j​(1+‖X(x2,a1)‖m+‖X(x2,a2)‖m)​‖X(x2,a1)−X(x2,a2)‖.\displaystyle|V^{\*}\_{j}(X^{(x\_{2},a\_{1})})-V^{\*}\_{j}(X^{(x\_{2},a\_{2})})|\leq\overline{C}\_{j}(1+\|X^{(x\_{2},a\_{1})}\|^{m}+\|X^{(x\_{2},a\_{2})}\|^{m})\|X^{(x\_{2},a\_{1})}-X^{(x\_{2},a\_{2})}\|. |  | (A.19) |

By ([A.5](https://arxiv.org/html/2512.14991v1#A1.E5 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{‖X(x2,a1)‖m,‖X(x2,a2)‖m}≤c˘1+c˘2​‖Bj−1‖m+(c˘3+c˘4​‖Bj−1‖m)​‖x2‖m,\displaystyle\max\Big\{\|X^{(x\_{2},a\_{1})}\|^{m},\|X^{(x\_{2},a\_{2})}\|^{m}\Big\}\leq\breve{c}\_{1}+\breve{c}\_{2}\|B\_{j-1}\|^{m}+(\breve{c}\_{3}+\breve{c}\_{4}\|B\_{j-1}\|^{m})\|x\_{2}\|^{m}, |  | (A.20) |

where c˘1,c˘2,c˘3,c˘4\breve{c}\_{1},\breve{c}\_{2},\breve{c}\_{3},\breve{c}\_{4} are defined in ([A.5](https://arxiv.org/html/2512.14991v1#A1.E5 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

By Assumption ([2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ‖X(x2,a1)−X(x2,a2)‖\displaystyle\|X^{(x\_{2},a\_{1})}-X^{(x\_{2},a\_{2})}\| |  | (A.21) |
|  |  | ≤\displaystyle\leq | ‖μj−1​(x2,a1)−μj−1​(x2,a2)‖​Δ+‖σj−1​(x2,a1)−σj−1​(x2,a2)‖​Δ​‖Bj−1‖\displaystyle\|\mu\_{j-1}(x\_{2},a\_{1})-\mu\_{j-1}(x\_{2},a\_{2})\|\Delta+\|\sigma\_{j-1}(x\_{2},a\_{1})-\sigma\_{j-1}(x\_{2},a\_{2})\|\sqrt{\Delta}\|B\_{j-1}\| |  |
|  |  | ≤\displaystyle\leq | (1+ℓμ​Δ)​‖a1−a2‖+ℓσ​‖a1−a2‖​Δ​‖Bj−1‖.\displaystyle(1+\ell\_{\mu}\Delta)\|a\_{1}-a\_{2}\|+\ell\_{\sigma}\|a\_{1}-a\_{2}\|\sqrt{\Delta}\|B\_{j-1}\|. |  |

By ([A.20](https://arxiv.org/html/2512.14991v1#A1.E20 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([A.21](https://arxiv.org/html/2512.14991v1#A1.E21 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | (‖X(x2,a1)‖m+‖X(x2,a2)‖m)​‖X(x2,a1)−X(x2,a2)‖\displaystyle(\|X^{(x\_{2},a\_{1})}\|^{m}+\|X^{(x\_{2},a\_{2})}\|^{m})\|X^{(x\_{2},a\_{1})}-X^{(x\_{2},a\_{2})}\| |  | (A.22) |
|  |  | ≤\displaystyle\leq | 2((c˘1+c˘2∥Bj−1∥m)+(c˘3+c˘4∥Bj−1∥m))∥x2∥m)(1+ℓμΔ+ℓσΔ∥Bj−1∥)∥a1−a2∥\displaystyle 2\Big((\breve{c}\_{1}+\breve{c}\_{2}\|B\_{j-1}\|^{m})+(\breve{c}\_{3}+\breve{c}\_{4}\|B\_{j-1}\|^{m}))\|x\_{2}\|^{m}\Big)(1+\ell\_{\mu}\Delta+\ell\_{\sigma}\sqrt{\Delta}\|B\_{j-1}\|)\|a\_{1}-a\_{2}\| |  |
|  |  | =\displaystyle= | 2​‖a1−a2‖​(f1​(‖Bj−1‖)+f2​(‖Bj−1‖)​‖x2‖m),\displaystyle 2\|a\_{1}-a\_{2}\|\Big(f\_{1}(\|B\_{j-1}\|)+f\_{2}(\|B\_{j-1}\|)\|x\_{2}\|^{m}\Big), |  |

where f1​(z)=c˘5+c˘6​z+c˘7​zm+c˘8​zm+1f\_{1}(z)=\breve{c}\_{5}+\breve{c}\_{6}z+\breve{c}\_{7}z^{m}+\breve{c}\_{8}z^{m+1}
and f2​(z)=c˘9+c˘10​z+c˘11​zm+c˘12​zm+1f\_{2}(z)=\breve{c}\_{9}+\breve{c}\_{10}z+\breve{c}\_{11}z^{m}+\breve{c}\_{12}z^{m+1}
with c˘i\breve{c}\_{i} all defined in ([A.7](https://arxiv.org/html/2512.14991v1#A1.E7 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

By the fact that 𝔼​[‖Bj−1‖q]\mathbb{E}\big[\|B\_{j-1}\|^{q}\big] is a finite constant for any integer qq, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(‖X(x2,a1)‖m+‖X(x2,a2)‖m)​‖X(x2,a1)−X(x2,a2)‖]≤2​c˘13​(1+‖x2‖m)​‖a1−a2‖.\displaystyle\mathbb{E}[(\|X^{(x\_{2},a\_{1})}\|^{m}+\|X^{(x\_{2},a\_{2})}\|^{m})\|X^{(x\_{2},a\_{1})}-X^{(x\_{2},a\_{2})}\|]\leq 2\breve{c}\_{13}(1+\|x\_{2}\|^{m})\|a\_{1}-a\_{2}\|. |  | (A.23) |

for c˘13\breve{c}\_{13} defined in ([A.8](https://arxiv.org/html/2512.14991v1#A1.E8 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Combine ([A.21](https://arxiv.org/html/2512.14991v1#A1.E21 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([A.23](https://arxiv.org/html/2512.14991v1#A1.E23 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) in ([A.19](https://arxiv.org/html/2512.14991v1#A1.E19 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I​I​I)≤2​c˘14​(1+‖x2‖m)​‖a1−a2‖,\displaystyle(III)\leq 2\breve{c}\_{14}(1+\|x\_{2}\|^{m})\|a\_{1}-a\_{2}\|, |  | (A.24) |

with c˘14\breve{c}\_{14} defined in ([A.10](https://arxiv.org/html/2512.14991v1#A1.E10 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Applying ([A.17](https://arxiv.org/html/2512.14991v1#A1.E17 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([A.18](https://arxiv.org/html/2512.14991v1#A1.E18 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([A.24](https://arxiv.org/html/2512.14991v1#A1.E24 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) to ([A.16](https://arxiv.org/html/2512.14991v1#A1.E16 "In A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we get:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Qj−1∗​(x1,a1)−Qj−1∗​(x2,a2)|\displaystyle|Q\_{j-1}^{\*}(x\_{1},a\_{1})-Q\_{j-1}^{\*}(x\_{2},a\_{2})| | ≤\displaystyle\leq | (ℓr+2​c˘14)​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖+‖a1−a2‖)\displaystyle(\ell\_{r}+2\breve{c}\_{14})(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|) |  |
|  |  | ≤\displaystyle\leq | 2​C¯j−1​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖+‖a1−a2‖),\displaystyle 2\overline{C}\_{j-1}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|), |  |

where the second inequality holds due to ([A.11](https://arxiv.org/html/2512.14991v1#A1.E11 "In A.2 Proof of Proposition 2.4 ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
∎

## Appendix B Technical details in Section [4](https://arxiv.org/html/2512.14991v1#S4 "4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

### B.1 Lemma [B.1](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1 Lemma B.1 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Lemma B.1.

For all (h,k)∈[H−1]×[K](h,k)\in{[H-1]\times[K]}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xh+1ki−XhkiΔ|(Xhki,Ahki)∼𝒩​(μh​(Xhki,Ahki),Σh​(Xhki,Ahki)Δ);\displaystyle\frac{X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}}}{\Delta}\,\Big|\,(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})\sim\mathcal{N}\Bigg(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}}),\frac{\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{\Delta}\Bigg); |  | (B.1) |
|  |  |  |
| --- | --- | --- |
|  | μ^hk​(B)−∑i=1nhk​(B)μh​(Xhki,Ahki)nhk​(B)|(Xhk1,Ahk1,…,Xhknhk​(B),Ahknhk​(B))∼𝒩​(0,∑i=1nhk​(B)Σh​(Xhki,Ahki)n2​Δ).\displaystyle\widehat{\mu}\_{h}^{k}(B)-\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\,\Big|\,(X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...,X\_{h}^{k\_{n\_{h}^{k}(B)}},A\_{h}^{k\_{n\_{h}^{k}(B)}})\sim\mathcal{N}\Bigg(0,\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n^{2}\Delta}\Bigg). |  |

###### Proof.

The first and second statements are straightforward by the definition in ([2.1](https://arxiv.org/html/2512.14991v1#S2.E1 "In 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the independence among Xh+1k1−Xhk1,…,Xh+1knhk​(B)−Xhknhk​(B)X\_{h+1}^{k\_{1}}-X\_{h}^{k\_{1}},...,X\_{h+1}^{k\_{n\_{h}^{k}(B)}}-X\_{h}^{k\_{n\_{h}^{k}(B)}} given Xhk1,Ahk1,…,Xhknhk​(B),Ahknhk​(B)X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...,X\_{h}^{k\_{n\_{h}^{k}(B)}},A\_{h}^{k\_{n\_{h}^{k}(B)}}.
∎

### B.2 Lemma [B.2](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.2 Lemma B.2 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Lemma B.2.

The following holds for all (h,k)∈[H−1]×[K](h,k)\in[H-1]\times[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} such that for n∈ℕ+n\in\mathbb{N}\_{+}:

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯​[Σ~hk​(B)]=∑i=1nhk​(B)(Σh​(Xhki,Ahki)+(μh​(Xhki,Ahki)−𝔼¯​[μ^hk​(B)])​(μh​(Xhki,Ahki)−𝔼¯​[μ^hk​(B)])⊤​Δ)nhk​(B).\displaystyle\overline{\mathbb{E}}\big[\widetilde{\Sigma}\_{h}^{k}(B)\big]=\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Big(\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})+\big(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\big)\big(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\big)^{\top}\Delta\Big)}{n\_{h}^{k}(B)}. |  |

###### Proof.

From Lemma [B.1](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1 Lemma B.1 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") we know that

|  |  |  |
| --- | --- | --- |
|  | Xh+1ki−XhkiΔ|(Xhki,Ahki)∼𝒩​(μh​(Xhki,Ahki),Σh​(Xhki,Ahki)Δ).\displaystyle\frac{X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}}}{\Delta}\,\Big|\,(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})\sim\mathcal{N}\left(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}}),\frac{\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{\Delta}\right). |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | Xh+1ki−Xhki−Δ​𝔼¯​[μ^hk​(B)]nhk​(B)​Δ|(Xhk1,Ahk1,…)∼𝒩​((μh​(Xhki,Ahki)−𝔼¯​[μ^hk​(B)])​Δnhk​(B),Σh​(Xhki,Ahki)nhk​(B)),\displaystyle\frac{X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}}-\Delta\overline{\mathbb{E}}[\widehat{\mu}^{k}\_{h}(B)]}{\sqrt{n\_{h}^{k}(B)\Delta}}\,\Big|\,(X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...)\sim\mathcal{N}\left(\frac{\big(\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\big)\sqrt{\Delta}}{\sqrt{n\_{h}^{k}(B)}},\frac{\Sigma\_{h}\left(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}}\right)}{n\_{h}^{k}(B)}\right), |  |

where the expression for the conditional mean follows the independence and the property of Gaussian distribution.
∎

### B.3 Proof of Proposition [4.1](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

For fixed h,kh,k and B∈𝒫hkB\in\mathcal{P}\_{h}^{k} s.t. nhk​(B)>0n\_{h}^{k}(B)>0, according to Lemma [B.1](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1 Lemma B.1 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we have for all z∈ℝd𝒮z\in\mathbb{R}^{d\_{\mathcal{S}}},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼¯​[exp⁡(z⊤​(μ^hk​(B)−𝔼¯​[μ^hk​(B)]))]\displaystyle\overline{\mathbb{E}}\Big[\exp\Big(z^{\top}\big(\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\big)\Big)\Big] | ≤\displaystyle\leq | exp⁡(12​‖z‖2​‖∑i=1nhk​(B)Σh​(Xhki,Ahki)n2​Δ‖)\displaystyle\exp\Big(\frac{1}{2}\|z\|^{2}\left\|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n^{2}\Delta}\right\|\Big) |  |
|  |  | ≤\displaystyle\leq | exp⁡(12​‖z‖2​∑i=1nhk​(B)‖σh​(Xhki,Ahki)‖2n2​Δ)\displaystyle\exp\Big(\frac{1}{2}\|z\|^{2}\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\|\sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})\|^{2}}{n^{2}\Delta}\Big) |  |
|  |  | ≤\displaystyle\leq | exp⁡(12​‖z‖2​η(∥x~(oB)∥)2nhk​(B)​Δ).\displaystyle\exp\Big(\frac{1}{2}\|z\|^{2}\frac{\eta(\|\tilde{x}(^{o}B)\|)^{2}}{n\_{h}^{k}(B)\Delta}\Big). |  |

Then Theorem 1 in [Hsu et al., [2011](https://arxiv.org/html/2512.14991v1#bib.bib30)] guarantees that:

|  |  |  |
| --- | --- | --- |
|  | ℙ¯​(‖μ^hk​(B)−𝔼¯​[μ^hk​(B)]‖2≥η(∥x~(oB)∥)2nhk​(B)​Δ​(d𝒮+2​d𝒮​log⁡(H​K2δ)+2​log⁡(H​K2δ)))≤δH​K2.\displaystyle\overline{\mathbb{P}}\left(\Big\|\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big\|^{2}\geq\frac{\eta(\|\tilde{x}(^{o}B)\|)^{2}}{n\_{h}^{k}(B)\Delta}\Bigg(d\_{\mathcal{S}}+2d\_{\mathcal{S}}\sqrt{\log\Big(\frac{HK^{2}}{\delta}\Big)}+2\log\Big(\frac{HK^{2}}{\delta}\Big)\Bigg)\right)\leq\frac{\delta}{HK^{2}}. |  |

Note that d𝒮+2​d𝒮​log⁡(H​K2δ)+2​log⁡(H​K2δ)≤(d𝒮+2​log⁡(H​K2δ))2d\_{\mathcal{S}}+2d\_{\mathcal{S}}\sqrt{\log\Big(\frac{HK^{2}}{\delta}\Big)}+2\log\Big(\frac{HK^{2}}{\delta}\Big)\leq\left(\sqrt{d\_{\mathcal{S}}}+\sqrt{2\log\Big(\frac{HK^{2}}{\delta}\Big)}\right)^{2}, hence we have:

|  |  |  |
| --- | --- | --- |
|  | ℙ¯(∥μ^hk(B)−𝔼¯[μ^hk(B)]∥≥κμ(δ,∥x~(oB)∥,nhk(B)))≤δH​K2.\displaystyle\overline{\mathbb{P}}\Big(\Big\|\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big\|\geq\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\Big)\leq\frac{\delta}{HK^{2}}. |  |

Taking expectations on both side, we have:

|  |  |  |
| --- | --- | --- |
|  | ℙ(∥μ^hk(B)−𝔼¯[μ^hk(B)]∥≥κμ(δ,∥x~(oB)∥,nhk(B)))≤δH​K2.\displaystyle\mathbb{P}\Big(\Big\|\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big\|\geq\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\Big)\leq\frac{\delta}{HK^{2}}. |  |

Then taking a union bound, we get:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | ℙ(∩h=1H−1∩k=1K∩B∈𝒫hk,nhk​(B)>0{∥μ^hk(B)−𝔼¯[μ^hk(B)]∥≤κμ(δ,∥x~(oB)∥,nhk(B))})\displaystyle\mathbb{P}\Bigg(\cap\_{h=1}^{H-1}\cap\_{k=1}^{K}\cap\_{B\in\mathcal{P}\_{h}^{k},n\_{h}^{k}(B)>0}\Bigg\{\Big\|\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big\|\leq\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\Bigg\}\Bigg) |  |
|  |  | =\displaystyle= | ℙ(∩h=1H−1∩k=1K∩nhk​(Bhk)=1,Bhk∈𝒫hk−1K{∥μ^hk(Bhk)−𝔼¯[μ^hk(Bhk)]∥≤κμ(δ,∥x~(oBhk)∥,nhk(Bhk))})\displaystyle\mathbb{P}\Bigg(\cap\_{h=1}^{H-1}\cap\_{k=1}^{K}\cap\_{n\_{h}^{k}(B\_{h}^{k})=1,B\_{h}^{k}\in\mathcal{P}\_{h}^{k-1}}^{K}\Bigg\{\Big\|\widehat{\mu}\_{h}^{k}(B\_{h}^{k})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B\_{h}^{k})]\Big\|\leq\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|,n\_{h}^{k}(B\_{h}^{k}))\Bigg\}\Bigg) |  |
|  |  | ≥\displaystyle\geq | 1−∑h=1H−1∑k=1K∑nhk​(Bhk)=1,Bhk∈𝒫hkKℙ(∥μ^hk(Bhk)−𝔼¯[μ^hk(Bhk)]∥≥κμ(δ,∥x~(oBhk)∥,nhk(Bhk)))\displaystyle 1-\sum\_{h=1}^{H-1}\sum\_{k=1}^{K}\sum\_{n\_{h}^{k}(B\_{h}^{k})=1,B\_{h}^{k}\in\mathcal{P}\_{h}^{k}}^{K}\mathbb{P}\Big(\Big\|\widehat{\mu}\_{h}^{k}(B\_{h}^{k})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B\_{h}^{k})]\Big\|\geq\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|,n\_{h}^{k}(B\_{h}^{k}))\Big) |  |
|  |  | ≥\displaystyle\geq | 1−δ,\displaystyle 1-\delta, |  |

where BhkB\_{h}^{k} is selected according to Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), and note that μ^hk​(Bhk)\widehat{\mu}\_{h}^{k}(B\_{h}^{k}) depends on nhk​(Bhk)n\_{h}^{k}(B\_{h}^{k}). The first equality holds since only the estimate for the selected block BhkB\_{h}^{k} is updated for each (h,k)(h,k) pair. The first inequality holds since, for a countable set of events E1,E2,…,E\_{1},E\_{2},..., we have ℙ​(∩iEi)≥1−∑iℙ​(Ei∁)\mathbb{P}(\cap\_{i}E\_{i})\geq 1-\sum\_{i}\mathbb{P}(E\_{i}^{\complement}).

∎

### B.4 Proof of Proposition [4.2](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

For any h,k∈[H−1]×[K]h,k\in{[H-1]\times[K]} and B∈𝒫hk,nhk​(B)>0B\in\mathcal{P}\_{h}^{k},n\_{h}^{k}(B)>0, denote Zi:=Xh+1ki−Xhki−Δ​𝔼¯​[μ^hk​(B)]ΔZ\_{i}:=\frac{X\_{h+1}^{k\_{i}}-X\_{h}^{k\_{i}}-\Delta\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]}{\sqrt{\Delta}}, then by Lemma [B.2](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.2 Lemma B.2 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Σ~hk​(B)−𝔼¯​[Σ~hk​(B)]\displaystyle\widetilde{\Sigma}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)] | =\displaystyle= | ∑i=1nhk​(B)Zi​Zi⊤nhk​(B)−∑i=1nhk​(B)𝔼¯​[Zi]​𝔼¯​[Zi⊤]nhk​(B)−∑i=1nhk​(B)𝕍¯​[Zi]nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}Z\_{i}Z\_{i}^{\top}}{n\_{h}^{k}(B)}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\overline{\mathbb{E}}[Z\_{i}]\overline{\mathbb{E}}[Z\_{i}^{\top}]}{n\_{h}^{k}(B)}-\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\overline{\mathbb{V}}[Z\_{i}]}{n\_{h}^{k}(B)} |  |
|  |  | =\displaystyle= | ∑i=1nhk​(B)(Zi​xi⊤−𝔼¯​[Zi​Zi⊤])nhk​(B).\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\Big(Z\_{i}x\_{i}^{\top}-\overline{\mathbb{E}}[Z\_{i}Z\_{i}^{\top}]\Big)}{n\_{h}^{k}(B)}. |  |

Notice that Z1,…,Znhk​(B)Z\_{1},...,Z\_{n\_{h}^{k}(B)} are conditionally independent given Xhk1,Ahk1,…,Xhknhk​(B),Ahknhk​(B)X\_{h}^{k\_{1}},A\_{h}^{k\_{1}},...,X\_{h}^{k\_{n\_{h}^{k}(B)}},A\_{h}^{k\_{n\_{h}^{k}(B)}} and they share the same sub-Gaussian variance proxy η(∥x~(oB)∥)\eta(\|\tilde{x}(^{o}B)\|) with ∥Σh(Xhki,Ahki)∥≤η(∥x~(oB)∥)2\|\Sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})\|\leq\eta(\|\tilde{x}(^{o}B)\|)^{2}.
  
Then by Theorem 6.5 in [Wainwright, [2019](https://arxiv.org/html/2512.14991v1#bib.bib59)], there exist universal constants D1>0,D2>1D\_{1}>0,D\_{2}>1 and D3>0D\_{3}>0 such that:

|  |  |  |
| --- | --- | --- |
|  | ℙ¯(∥Σ~hk(B)−𝔼¯[Σ~hk(B)]∥≥η(∥x~(oB)∥)2(D1(d𝒮nhk​(B)+d𝒮nhk​(B))+ϵ))≤D2e−D3​nhk​(B)​min⁡{ϵ,ϵ2}.\displaystyle\overline{\mathbb{P}}\left(\Big\|\widetilde{\Sigma}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Big\|\geq\eta(\|\tilde{x}(^{o}B)\|)^{2}\left(D\_{1}\left(\sqrt{\frac{d\_{\mathcal{S}}}{n\_{h}^{k}(B)}}+\frac{d\_{\mathcal{S}}}{n\_{h}^{k}(B)}\right)+\epsilon\right)\right)\leq D\_{2}e^{-D\_{3}n\_{h}^{k}(B)\min\{\epsilon,\epsilon^{2}\}}. |  |

Notice that for a,b,c∈ℝa,b,c\in\mathbb{R}, we have max⁡{a,b}≤a+b\max\{a,b\}\leq a+b and 1c≤1c\frac{1}{c}\leq\sqrt{\frac{1}{c}} for c≥1c\geq 1.Therefore, we conclude that:

|  |  |  |
| --- | --- | --- |
|  | ℙ¯(∥Σ~hk(B)−𝔼¯[Σ~hk(B)]∥≥κΣ(δ,∥x~(oB)∥,nhk(B)))≤δH​K2.\displaystyle\overline{\mathbb{P}}\Bigg(\Big\|\widetilde{\Sigma}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Big\|\geq\kappa\_{\Sigma}\Big(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B)\Big)\Bigg)\leq\frac{\delta}{HK^{2}}. |  |

Taking expectations, we have:

|  |  |  |
| --- | --- | --- |
|  | ℙ(∥Σ~hk(B)−𝔼¯[Σ~hk(B)]∥≥κΣ(δ,∥x~(oB)∥,nhk(B)))≤δH​K2.\displaystyle\mathbb{P}\Bigg(\Big\|\widetilde{\Sigma}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Big\|\geq\kappa\_{\Sigma}\Big(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B)\Big)\Bigg)\leq\frac{\delta}{HK^{2}}. |  |

Then taking a union bound, we get:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | ℙ(∩h=1H−1∩k=1K∩B∈𝒫hk,nhk​(B)>0∥Σ~hk(B)−𝔼¯[Σ~hk(B)]∥≤κΣ(δ,∥x~(oB)∥,nhk(B))})\displaystyle\mathbb{P}\Bigg(\cap\_{h=1}^{H-1}\cap\_{k=1}^{K}\cap\_{B\in\mathcal{P}\_{h}^{k},n\_{h}^{k}(B)>0}\Big\|\widetilde{\Sigma}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Big\|\leq\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\Bigg\}\Bigg) |  |
|  |  | =\displaystyle= | ℙ(∩h=1H−1∩k=1K∩nhk​(Bhk)=1K∥Σ~hk(Bhk)−𝔼¯[Σ~hk(Bhk)]∥≤κΣ(δ,∥x~(oBhk)∥,nhk(Bhk))})\displaystyle\mathbb{P}\Bigg(\cap\_{h=1}^{H-1}\cap\_{k=1}^{K}\cap\_{n\_{h}^{k}(B\_{h}^{k})=1}^{K}\Big\|\widetilde{\Sigma}\_{h}^{k}(B\_{h}^{k})-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B\_{h}^{k})]\Big\|\leq\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|,n\_{h}^{k}(B\_{h}^{k}))\Bigg\}\Bigg) |  |
|  |  | ≥\displaystyle\geq | 1−∑h=1H−1∑k=1K∑nhk​(Bhk)=1Kℙ(∥Σ~hk(Bhk)−𝔼¯[Σ~hk(Bhk)]∥≥κΣ(δ,∥x~(oBhk)∥,nhk(Bhk)))\displaystyle 1-\sum\_{h=1}^{H-1}\sum\_{k=1}^{K}\sum\_{n\_{h}^{k}(B\_{h}^{k})=1}^{K}\mathbb{P}\Bigg(\Big\|\widetilde{\Sigma}\_{h}^{k}(B\_{h}^{k})-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B\_{h}^{k})]\Big\|\geq\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|,n\_{h}^{k}(B\_{h}^{k}))\Bigg) |  |
|  |  | ≥\displaystyle\geq | 1−δ,\displaystyle 1-\delta, |  |

where BhkB\_{h}^{k} is selected according to Algorithm [2](https://arxiv.org/html/2512.14991v1#alg2 "Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and note that Σ~hk​(Bhk)\widetilde{\Sigma}\_{h}^{k}(B\_{h}^{k}) depends on nhk​(Bhk)n\_{h}^{k}(B\_{h}^{k}). The first equality holds since only the estimate for the selected block BhkB\_{h}^{k} is updated for each (h,k)(h,k) pair. The first inequality holds since, for a countable set of events E1,E2,…,E\_{1},E\_{2},..., we have ℙ​(∩iEi)≥1−∑iℙ​(Ei∁)\mathbb{P}(\cap\_{i}E\_{i})\geq 1-\sum\_{i}\mathbb{P}(E\_{i}^{\complement}).

∎

### B.5 Proof of Theorem [4.3](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

We have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲¯2​(𝒩​(μ^hk​(B)​Δ,Σ^hk​(B)​Δ),𝒩​(μh​(x,a)​Δ,Σh​(x,a)​Δ))\displaystyle\overline{\mathcal{W}}\_{2}\Big(\mathcal{N}(\widehat{\mu}\_{h}^{k}(B)\Delta,\widehat{\Sigma}\_{h}^{k}(B)\Delta),\mathcal{N}(\mu\_{h}(x,a)\Delta,\Sigma\_{h}(x,a)\Delta)\Big) |  | (B.2) |
|  |  | =\displaystyle= | (∥μ^hk(B)Δ−μh(x,a)Δ∥2\displaystyle\Bigg(\|\widehat{\mu}\_{h}^{k}(B)\Delta-\mu\_{h}(x,a)\Delta\|^{2} |  |
|  |  |  | +Tr(Σ^hk(B)Δ+Σh(x,a)Δ−2((Σ^hk(B)Δ)12(Σh(x,a)Δ)(Σ^hk(B)Δ)12)12))12\displaystyle+{\rm Tr}\Big(\widehat{\Sigma}\_{h}^{k}(B)\Delta+\Sigma\_{h}(x,a)\Delta-2((\widehat{\Sigma}\_{h}^{k}(B)\Delta)^{\frac{1}{2}}(\Sigma\_{h}(x,a)\Delta)(\widehat{\Sigma}\_{h}^{k}(B)\Delta)^{\frac{1}{2}})^{\frac{1}{2}}\Big)\Bigg)^{\frac{1}{2}} |  |
|  |  | ≤\displaystyle\leq | ‖μ^hk​(B)​Δ−μh​(x,a)​Δ‖2+‖(Σ^hk​(B)​Δ)12−(Σh​(x,a)​Δ)12‖F2\displaystyle\sqrt{\|\widehat{\mu}\_{h}^{k}(B)\Delta-\mu\_{h}(x,a)\Delta\|^{2}+\|(\widehat{\Sigma}\_{h}^{k}(B)\Delta)^{\frac{1}{2}}-(\Sigma\_{h}(x,a)\Delta)^{\frac{1}{2}}\|\_{F}^{2}} |  |
|  |  | ≤\displaystyle\leq | ‖μ^hk​(B)​Δ−μh​(x,a)​Δ‖+‖(Σ^hk​(B)​Δ)12−(Σh​(x,a)​Δ)12‖F\displaystyle\|\widehat{\mu}\_{h}^{k}(B)\Delta-\mu\_{h}(x,a)\Delta\|+\|(\widehat{\Sigma}\_{h}^{k}(B)\Delta)^{\frac{1}{2}}-(\Sigma\_{h}(x,a)\Delta)^{\frac{1}{2}}\|\_{F} |  |
|  |  | ≤\displaystyle\leq | ‖μ^hk​(B)​Δ−μh​(x,a)​Δ‖⏟(I)+1λ​‖Σ^hk​(B)​Δ12−Σh​(x,a)​Δ12‖F⏟(I​I).\displaystyle\underbrace{\|\widehat{\mu}\_{h}^{k}(B)\Delta-\mu\_{h}(x,a)\Delta\|}\_{(I)}+\underbrace{\frac{1}{\sqrt{\lambda}}\|\widehat{\Sigma}\_{h}^{k}(B)\Delta^{\frac{1}{2}}-\Sigma\_{h}(x,a)\Delta^{\frac{1}{2}}\|\_{F}}\_{(II)}. |  |

Here, the first equality holds by Proposition 7 in [Givens and Shortt, [1984](https://arxiv.org/html/2512.14991v1#bib.bib24)] and the first inequality holds by Theorem 1 in [Bhatia et al., [2017](https://arxiv.org/html/2512.14991v1#bib.bib8)]. The second inequality holds since a2+b2≤a+b\sqrt{a^{2}+b^{2}}\leq a+b for a≥0,b≥0a\geq 0,b\geq 0; and, to get the third inequality, we apply (1.1)-(1.3) in [Schmitt, [1992](https://arxiv.org/html/2512.14991v1#bib.bib51)] and ([2.5](https://arxiv.org/html/2512.14991v1#S2.E5 "In Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

For term (I), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖μ^hk​(B)​Δ−μh​(x,a)​Δ‖≤‖μ^hk​(B)​Δ−𝔼¯​[μ^hk​(B)]​Δ‖+‖𝔼¯​[μ^hk​(B)]​Δ−μh​(x,a)​Δ‖.\displaystyle\big\|\widehat{\mu}\_{h}^{k}(B)\Delta-\mu\_{h}(x,a)\Delta\big\|\leq\big\|\widehat{\mu}\_{h}^{k}(B)\Delta-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Delta\big\|+\big\|\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Delta-\mu\_{h}(x,a)\Delta\big\|. |  | (B.3) |

For term (II), we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 1λ​‖Σ^hk​(B)​Δ12−Σh​(x,a)​Δ12‖F\displaystyle\frac{1}{\sqrt{\lambda}}\|\widehat{\Sigma}\_{h}^{k}(B)\Delta^{\frac{1}{2}}-\Sigma\_{h}(x,a)\Delta^{\frac{1}{2}}\|\_{F} |  | (B.4) |
|  |  | ≤\displaystyle\leq | 1λ(∥Σ^hk(B)Δ12−Σ~hk(B)Δ12∥F+∥Σ~hk(B)Δ12−𝔼¯[Σ~hk(B)]Δ12∥F\displaystyle\frac{1}{\sqrt{\lambda}}(\|\widehat{\Sigma}\_{h}^{k}(B)\Delta^{\frac{1}{2}}-\widetilde{\Sigma}\_{h}^{k}(B)\Delta^{\frac{1}{2}}\|\_{F}+\|\widetilde{\Sigma}\_{h}^{k}(B)\Delta^{\frac{1}{2}}-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Delta^{\frac{1}{2}}\|\_{F} |  |
|  |  |  | +∥𝔼¯[Σ~hk(B)]Δ12−Σh(x,a)Δ12∥F)\displaystyle+\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Delta^{\frac{1}{2}}-\Sigma\_{h}(x,a)\Delta^{\frac{1}{2}}\|\_{F}) |  |
|  |  | ≤\displaystyle\leq | 1λ(∥(μ^hk(B)−𝔼¯[μ^hk(B)])∥2Δ32+d𝒮∥Σ~hk(B)Δ12−𝔼¯[Σ~hk(B)]Δ12∥\displaystyle\frac{1}{\sqrt{\lambda}}\Big(\Big\|\Big(\widehat{\mu}\_{h}^{k}(B)-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\Big)\Big\|^{2}\Delta^{\frac{3}{2}}+\sqrt{d\_{\mathcal{S}}}\|\widetilde{\Sigma}\_{h}^{k}(B)\Delta^{\frac{1}{2}}-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Delta^{\frac{1}{2}}\| |  |
|  |  |  | +∥𝔼¯[Σ~hk(B)]Δ12−Σh(x,a)Δ12∥F).\displaystyle+\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]\Delta^{\frac{1}{2}}-\Sigma\_{h}(x,a)\Delta^{\frac{1}{2}}\|\_{F}\Big). |  |

Here, we apply ([4.2](https://arxiv.org/html/2512.14991v1#S4.E2 "In 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) to get the first inequality and ([4.3](https://arxiv.org/html/2512.14991v1#S4.E3 "In 2nd item ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) to get the second inequality.

Note that by Propositions [4.1](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [4.2](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we have ([4.8](https://arxiv.org/html/2512.14991v1#S4.E8 "In Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([4.9](https://arxiv.org/html/2512.14991v1#S4.E9 "In Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) hold. Combine ([4.8](https://arxiv.org/html/2512.14991v1#S4.E8 "In Proposition 4.1. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([4.9](https://arxiv.org/html/2512.14991v1#S4.E9 "In Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([B.2](https://arxiv.org/html/2512.14991v1#A2.E2 "In B.5 Proof of Theorem 4.3 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([B.3](https://arxiv.org/html/2512.14991v1#A2.E3 "In B.5 Proof of Theorem 4.3 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([B.4](https://arxiv.org/html/2512.14991v1#A2.E4 "In B.5 Proof of Theorem 4.3 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we verify that it holds with probability at least 1−2​δ1-2\delta that, for any (h,k)×[H−1]×[K](h,k)\times[H-1]\times[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and any (x,a)∈B(x,a)\in B,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | 𝒲¯2​(𝒩​(μ^hk​(B)​Δ,Σ^hk​(B)​Δ),𝒩​(μh​(x,a)​Δ,Σh​(x,a)​Δ))\displaystyle\overline{\mathcal{W}}\_{2}\Big(\mathcal{N}(\widehat{\mu}\_{h}^{k}(B)\Delta,\widehat{\Sigma}\_{h}^{k}(B)\Delta),\mathcal{N}(\mu\_{h}(x,a)\Delta,\Sigma\_{h}(x,a)\Delta)\Big) |  |
|  |  | ≤\displaystyle\leq | Δκμ(δ,∥x~(oB)∥,nhk(B))+Δ32λκμ(δ,∥x~(oB)∥,nhk(B))2+d𝒮​Δ12λκΣ(δ,∥x~(oB)∥,nhk(B))\displaystyle\Delta\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))+\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}}\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{2}+\frac{\sqrt{d\_{\mathcal{S}}}\Delta^{\frac{1}{2}}}{\sqrt{\lambda}}\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B)) |  |
|  |  |  | +‖𝔼¯​[μ^hk​(B)]−μh​(x,a)‖​Δ+‖𝔼¯​[Σ~hk​(B)]−Σh​(x,a)‖​Δλ.\displaystyle+\Big\|\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]-\mu\_{h}(x,a)\Big\|\Delta+\Big\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}^{k}(B)]-\Sigma\_{h}(x,a)\Big\|\frac{\sqrt{\Delta}}{\sqrt{\lambda}}. |  |

∎

### B.6 Proof of Theorem [4.4](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

We first introduce two technical lemmas.

###### Lemma B.3.

Suppose Z∼𝒩​(μ,Σ)Z\sim\mathcal{N}(\mu,\Sigma) with μ∈ℝd\mu\in\mathbb{R}^{d}, Σ∈ℝd×d\Sigma\in\mathbb{R}^{d\times d} and Σ⪰0\Sigma\succeq 0, then ∀q∈ℕ+\forall q\in\mathbb{N}^{+}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔼Z∼𝒩​(μ,Σ)​[‖Z‖2​q])12≤C~​(q,d)​(‖μ‖q+‖Σ‖q2),\displaystyle(\mathbb{E}\_{Z\sim\mathcal{N}(\mu,\Sigma)}[\|Z\|^{2q}])^{\frac{1}{2}}\leq\widetilde{C}(q,d)(\|\mu\|^{q}+\|\Sigma\|^{\frac{q}{2}}), |  | (B.5) |

where C~​(q,d)\widetilde{C}(q,d) is defined in ([4.14](https://arxiv.org/html/2512.14991v1#S4.E14 "In 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Proof.

Denote ZjZ\_{j} as the jjth random variable of the random vector ZZ, and hence Zj∼𝒩​(μj,Σj​j)Z\_{j}\sim\mathcal{N}(\mu\_{j},\Sigma\_{jj}) where μj\mu\_{j} is the jjth component of μ\mu and Σj​j\Sigma\_{jj} is the (j,j)(j,j)th component of Σ\Sigma. Therefore,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (𝔼Z∼𝒩​(μ,Σ)​[‖Z‖]2​q)12\displaystyle(\mathbb{E}\_{Z\sim\mathcal{N}(\mu,\Sigma)}[\|Z\|]^{2q})^{\frac{1}{2}} | =\displaystyle= | (𝔼Z∼𝒩​(μ,Σ)​[Z12+…+Zd2]q)12\displaystyle\Big(\mathbb{E}\_{Z\sim\mathcal{N}(\mu,\Sigma)}[Z\_{1}^{2}+...+Z\_{d}^{2}]^{q}\Big)^{\frac{1}{2}} |  | (B.6) |
|  |  | ≤\displaystyle\leq | (dq−1​∑j=1d𝔼Zj∼𝒩​(μj,Σj​j)​[Zj]2​q)12\displaystyle\Big(d^{q-1}\sum\_{j=1}^{d}\mathbb{E}\_{Z\_{j}\sim\mathcal{N}(\mu\_{j},\Sigma\_{jj})}[Z\_{j}]^{2q}\Big)^{\frac{1}{2}} |  |
|  |  | ≤\displaystyle\leq | dq−12​∑j=1d(𝔼Zj∼𝒩​(μj,Σj​j)​[|Zj−μj|+|μj|]2​q)12\displaystyle d^{\frac{q-1}{2}}\sum\_{j=1}^{d}\Big(\mathbb{E}\_{Z\_{j}\sim\mathcal{N}(\mu\_{j},\Sigma\_{jj})}[|Z\_{j}-\mu\_{j}|+|\mu\_{j}|]^{2q}\Big)^{\frac{1}{2}} |  |
|  |  | ≤\displaystyle\leq | dq−12​∑j=1d(22​q−1​(𝔼Zj∼𝒩​(μj,Σj​j)​[|Zj−μj|]2​q+|μj|2​q))12,\displaystyle d^{\frac{q-1}{2}}\sum\_{j=1}^{d}\Big(2^{2q-1}(\mathbb{E}\_{Z\_{j}\sim\mathcal{N}(\mu\_{j},\Sigma\_{jj})}[|Z\_{j}-\mu\_{j}|]^{2q}+|\mu\_{j}|^{2q})\Big)^{\frac{1}{2}}, |  |

where the first inequality holds by the power-mean inequality.
The second inequality follows from a+b≤a+b\sqrt{a+b}\leq\sqrt{a}+\sqrt{b} when a,b>0a,b>0.

According to [Winkelbauer, [2012](https://arxiv.org/html/2512.14991v1#bib.bib62)], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼Zj∼𝒩​(μj,Σj​j)​[|Zj−μj|]2​q=2q​Γ​(q+12)π​(Σj​j)q.\displaystyle\mathbb{E}\_{Z\_{j}\sim\mathcal{N}(\mu\_{j},\Sigma\_{jj})}[|Z\_{j}-\mu\_{j}|]^{2q}=\frac{2^{q}\Gamma(q+\frac{1}{2})}{\sqrt{\pi}}(\Sigma\_{jj})^{q}. |  | (B.7) |

Hence, combining ([B.6](https://arxiv.org/html/2512.14991v1#A2.E6 "In B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([B.7](https://arxiv.org/html/2512.14991v1#A2.E7 "In B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (𝔼Z∼𝒩​(μ,Σ)​[‖Z‖]2​q)12\displaystyle(\mathbb{E}\_{Z\sim\mathcal{N}(\mu,\Sigma)}[\|Z\|]^{2q})^{\frac{1}{2}} | ≤\displaystyle\leq | dq−12​Σj=1d​(22​q−1​(𝔼Zj∼𝒩​(μj,Σj​j)​[|Zj−μj|]2​q+|μj|2​q))12\displaystyle d^{\frac{q-1}{2}}\Sigma\_{j=1}^{d}\Big(2^{2q-1}(\mathbb{E}\_{Z\_{j}\sim\mathcal{N}(\mu\_{j},\Sigma\_{jj})}[|Z\_{j}-\mu\_{j}|]^{2q}+|\mu\_{j}|^{2q})\Big)^{\frac{1}{2}} |  | (B.8) |
|  |  | ≤\displaystyle\leq | dq−12​Σj=1d​(22​q−1​(2q​Γ​(q+12)π​(Σj​j)q+|μj|2​q))12\displaystyle d^{\frac{q-1}{2}}\Sigma\_{j=1}^{d}\Big(2^{2q-1}(\frac{2^{q}\Gamma(q+\frac{1}{2})}{\sqrt{\pi}}(\Sigma\_{jj})^{q}+|\mu\_{j}|^{2q})\Big)^{\frac{1}{2}} |  |
|  |  | ≤\displaystyle\leq | dq−12Σj=1d(22​q−1(2q​Γ​(q+12)π(dq2∥Σ∥q+∥μ∥2​q))12\displaystyle d^{\frac{q-1}{2}}\Sigma\_{j=1}^{d}\Big(2^{2q-1}(\frac{2^{q}\Gamma(q+\frac{1}{2})}{\sqrt{\pi}}(d^{\frac{q}{2}}\|\Sigma\|^{q}+\|\mu\|^{2q})\Big)^{\frac{1}{2}} |  |
|  |  | ≤\displaystyle\leq | C~​(q,d)​(‖μ‖q+‖Σ‖q2),\displaystyle\widetilde{C}(q,d)(\|\mu\|^{q}+\|\Sigma\|^{\frac{q}{2}}), |  |

where third inequality holds due to Σj​j≤d​‖Σ‖\Sigma\_{jj}\leq\sqrt{d}\|\Sigma\| and μj≤‖μ‖\mu\_{j}\leq\|\mu\|.
∎

###### Lemma B.4.

Suppose a function U:ℝd↦ℝU:\mathbb{R}^{d}\mapsto\mathbb{R} has the following property:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |U​(x1)−U​(x2)|≤C˘​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖,\displaystyle|U(x\_{1})-U(x\_{2})|\leq\breve{C}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})\|x\_{1}-x\_{2}\|, |  | (B.9) |

where C˘\breve{C} is a constant. Then it holds that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | |𝔼X∼T¯hk(⋅|B)​[U​(X)]−𝔼Y∼Th(⋅|x,a)​[U​(Y)]|\displaystyle\left|\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[U(X)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[U(Y)]\right| |  | (B.10) |
|  |  | ≤\displaystyle\leq | LU​(B,x,a)​𝒲¯2​(𝒩​(μ^hk​(B)​Δ,Σ^hk​(B)​Δ),𝒩​(μh​(x,a)​Δ,Σh​(x,a)​Δ)),\displaystyle L\_{U}(B,x,a)\overline{\mathcal{W}}\_{2}\Big(\mathcal{N}(\widehat{\mu}\_{h}^{k}(B)\Delta,\widehat{\Sigma}\_{h}^{k}(B)\Delta),\mathcal{N}(\mu\_{h}(x,a)\Delta,\Sigma\_{h}(x,a)\Delta)\Big), |  |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | LU​(B,x,a):\displaystyle L\_{U}(B,x,a): | =\displaystyle= | 3C˘(1+C~(m,d)(∥μ^hk(B)∥mΔm\displaystyle\sqrt{3}\breve{C}\Big(1+\widetilde{C}(m,d)(\|\widehat{\mu}\_{h}^{k}(B)\|^{m}\Delta^{m} |  |
|  |  |  | +∥Σ^hk(B)∥m2Δm2+∥μh(x,a)∥mΔm+∥Σh(x,a)∥m2Δm2)).\displaystyle+\|\widehat{\Sigma}\_{h}^{k}(B)\|^{\frac{m}{2}}\Delta^{\frac{m}{2}}+\|\mu\_{h}(x,a)\|^{m}\Delta^{m}+\|\Sigma\_{h}(x,a)\|^{\frac{m}{2}}\Delta^{\frac{m}{2}})\Big). |  |

###### Proof.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | |𝔼X∼T¯hk(⋅|B)​[U​(X)]−𝔼Y∼Th(⋅|x,a)​[U​(Y)]|\displaystyle\left|\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[U(X)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[U(Y)]\right| |  | (B.11) |
|  |  | ≤\displaystyle\leq | 𝔼X∼T¯hk(⋅|B),Y∼Th(⋅|x,a)​[|U​(X)−U​(Y)|]\displaystyle\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B),Y\sim{T}\_{h}(\cdot|x,a)}[\left|U(X)-U(Y)\right|] |  |
|  |  | ≤\displaystyle\leq | C˘​𝔼X∼T¯hk(⋅|B),Y∼Th(⋅|x,a)​[(1+‖X‖m+‖Y‖m)​(‖X−Y‖)]\displaystyle\breve{C}\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B),Y\sim{T}\_{h}(\cdot|x,a)}\Big[\Big(1+\|X\|^{m}+\|Y\|^{m}\Big)\Big(\|X-Y\|\Big)\Big] |  |
|  |  | ≤\displaystyle\leq | C˘​(𝔼X∼T¯hk(⋅|B),Y∼Th(⋅|x,a)​[1+‖X‖2​m+‖Y‖2​m])12​(𝔼X∼T¯hk(⋅|B),Y∼Th(⋅|x,a)​[‖X−Y‖2])12\displaystyle\breve{C}\Big(\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B),Y\sim{T}\_{h}(\cdot|x,a)}[1+\|X\|^{2m}+\|Y\|^{2m}]\Big)^{\frac{1}{2}}\Big(\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B),Y\sim{T}\_{h}(\cdot|x,a)}[\|X-Y\|^{2}]\Big)^{\frac{1}{2}} |  |
|  |  | ≤\displaystyle\leq | 3​C˘​(1+(𝔼X∼T¯hk(⋅|B)​[‖X‖2​m])12+(𝔼Y∼Th(⋅|x,a)​[‖Y‖2​m])12)​(𝔼X∼T¯hk(⋅|B),Y∼Th(⋅|x,a)​[‖X−Y‖2])12\displaystyle\sqrt{3}\breve{C}\Big(1+(\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\|X\|^{2m}])^{\frac{1}{2}}+(\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[\|Y\|^{2m}])^{\frac{1}{2}}\Big)\Big(\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B),Y\sim{T}\_{h}(\cdot|x,a)}[\|X-Y\|^{2}]\Big)^{\frac{1}{2}} |  |
|  |  | ≤\displaystyle\leq | 3​C˘​(1+C~​(m,d)​(‖μ^hk​(B)‖m​Δm+‖Σ^hk​(B)‖m2​Δm2+‖μh​(x,a)‖m​Δm+‖Σh​(x,a)‖m2​Δm2))\displaystyle\sqrt{3}\breve{C}\Big(1+\widetilde{C}(m,d)(\|\widehat{\mu}\_{h}^{k}(B)\|^{m}\Delta^{m}+\|\widehat{\Sigma}\_{h}^{k}(B)\|^{\frac{m}{2}}\Delta^{\frac{m}{2}}+\|\mu\_{h}(x,a)\|^{m}\Delta^{m}+\|\Sigma\_{h}(x,a)\|^{\frac{m}{2}}\Delta^{\frac{m}{2}})\Big) |  |
|  |  |  | ×(EX∼T¯hk(⋅|B),Y∼Th(⋅|x,a)​‖X−Y‖2)12,\displaystyle\qquad\times\Big({E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B),Y\sim{T}\_{h}(\cdot|x,a)}\|X-Y\|^{2}\Big)^{\frac{1}{2}}, |  |

where the second inequality holds due to ([B.9](https://arxiv.org/html/2512.14991v1#A2.E9 "In Lemma B.4. ‣ B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the third inequality holds by Hölder’s inequality and the last inequality holds due to ([B.5](https://arxiv.org/html/2512.14991v1#A2.E5 "In Lemma B.3. ‣ B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Note that ([B.11](https://arxiv.org/html/2512.14991v1#A2.E11 "In B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for any joint distribution (coupling) of T¯hk(⋅|B)\bar{T}\_{h}^{k}(\cdot|B) and Th(⋅|x,a){T}\_{h}(\cdot|x,a), hence we may choose the one which can minimize (𝔼X∼T¯hk(⋅|B),Y∼Th(⋅|x,a)​[‖X−Y‖2])12\Big(\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B),Y\sim{T}\_{h}(\cdot|x,a)}[\|X-Y\|^{2}]\Big)^{\frac{1}{2}}. Then we obtain the following:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |𝔼X∼T¯hk(⋅|B)​[U​(X)]−𝔼Y∼Th(⋅|x,a)​[U​(Y)]|\displaystyle\left|\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[U(X)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[U(Y)]\right| |  |
|  |  | ≤\displaystyle\leq | LU​(B,x,a)​𝒲¯2​(𝒩​(μ^hk​(B)​Δ,Σ^hk​(B)​Δ),𝒩​(μh​(x,a)​Δ,Σh​(x,a)​Δ)).\displaystyle L\_{U}(B,x,a)\,\overline{\mathcal{W}}\_{2}\Big(\mathcal{N}(\widehat{\mu}\_{h}^{k}(B)\Delta,\widehat{\Sigma}\_{h}^{k}(B)\Delta),\mathcal{N}(\mu\_{h}(x,a)\Delta,\Sigma\_{h}(x,a)\Delta)\Big). |  |

∎

Then with the two lemmas above, we are ready to provide the proof for Theorem [4.4](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Proof.

From ([2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we know Vh+1∗V\_{h+1}^{\*} has local lipschitz property required to apply Theorem [B.4](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem4 "Lemma B.4. ‣ B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), so ([B.10](https://arxiv.org/html/2512.14991v1#A2.E10 "In Lemma B.4. ‣ B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for U=Vh+1∗U=V\_{h+1}^{\*} with C˘=C¯h+1\breve{C}=\overline{C}\_{h+1}.

For the drift term, with probability at least 1−δ1-\delta, it holds that, ∀(h,k)∈[H−1]×[K]\forall(h,k)\in[H-1]\times[K] and ∀B∈𝒫hk\forall B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖μ^hk​(B)‖m\displaystyle\|\widehat{\mu}\_{h}^{k}(B)\|^{m} | ≤\displaystyle\leq | (‖μ^hk​(B)−𝔼¯​[μ^hk​(B)]‖+‖𝔼¯​[μ^hk​(B)]‖)m\displaystyle\Big(\|\widehat{\mu}\_{h}^{k}(B)-\bar{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\|+\|\bar{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\|\Big)^{m} |  | (B.12) |
|  |  | ≤\displaystyle\leq | 2m​(‖μ^hk​(B)−𝔼¯​[μ^hk​(B)]‖m+‖𝔼¯​[μ^hk​(B)]‖m)\displaystyle 2^{m}\Big(\|\widehat{\mu}\_{h}^{k}(B)-\bar{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\|^{m}+\|\bar{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\|^{m}\Big) |  |
|  |  | ≤\displaystyle\leq | 2m(κμ(δ,∥x~(oB)∥,nhk(B))m+η(∥x~(oB)∥)m),\displaystyle 2^{m}\Bigg(\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{m}+\eta(\|\tilde{x}(^{o}B)\|)^{m}\Bigg), |  |

where the second inequality holds by power-mean inequality.

Let Z:=‖𝔼¯​[Σ~h​(B)]‖Z:=\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}(B)]\|, we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Z\displaystyle Z | ≤\displaystyle\leq | ∑i=1n‖σh​(Xhki,Ahki)‖2nhk​(B)+∑i=1nhk​(B)‖μh​(Xhki,Ahki)−𝔼¯​[μ^hk​(B)]‖2nhk​(B)​Δ\displaystyle\frac{\sum\_{i=1}^{n}\|\sigma\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})\|^{2}}{n\_{h}^{k}(B)}+\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\|\mu\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\overline{\mathbb{E}}[\widehat{\mu}\_{h}^{k}(B)]\|^{2}}{n\_{h}^{k}(B)}\Delta |  | (B.13) |
|  |  | ≤\displaystyle\leq | η(∥x~(oB)∥)2+L2D2Δ,\displaystyle\eta(\|\tilde{x}(^{o}B)\|)^{2}+L^{2}D^{2}\Delta, |  |

where the last inequality holds by ([4.7](https://arxiv.org/html/2512.14991v1#S4.E7 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Then similar to ([B.12](https://arxiv.org/html/2512.14991v1#A2.E12 "In B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), with probability at least 1−δ1-\delta, it holds that ∀(h,k)∈[H−1]×[K]\forall(h,k)\in[H-1]\times[K], ∀B∈𝒫hk\forall B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖Σ^hk​(B)‖m2\displaystyle\|\widehat{\Sigma}\_{h}^{k}(B)\|^{\frac{m}{2}} | ≤\displaystyle\leq | (‖Σ^hk​(B)−Σ~h​(B)‖+‖Σ~h​(B)−𝔼¯​[Σ~h​(B)]‖+‖𝔼¯​[Σ~h​(B)]‖)m2\displaystyle(\|\widehat{\Sigma}\_{h}^{k}(B)-\widetilde{\Sigma}\_{h}(B)\|+\|\widetilde{\Sigma}\_{h}(B)-\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}(B)]\|+\|\overline{\mathbb{E}}[\widetilde{\Sigma}\_{h}(B)]\|)^{\frac{m}{2}} |  | (B.14) |
|  |  | ≤\displaystyle\leq | 3m2(κμ(δ,∥x~(oB)∥,nhk(B))mΔm2\displaystyle 3^{\frac{m}{2}}\Bigg(\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{m}\Delta^{\frac{m}{2}} |  |
|  |  |  | +κΣ(δ,∥x~(oB)∥,nhk(B))m2+(η(∥x~(oB)∥)2+L2D2Δ)m2),\displaystyle+\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{\frac{m}{2}}+\Big(\eta(\|\tilde{x}(^{o}B)\|)^{2}+L^{2}D^{2}\Delta\Big)^{\frac{m}{2}}\Bigg), |  |

where the second inequality holds due to ([4.3](https://arxiv.org/html/2512.14991v1#S4.E3 "In 2nd item ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and Proposition [4.2](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

Therefore, with probability at least 1−2​δ1-2\delta , it holds that ∀(h,k)∈[H−1]×[K]\forall(h,k)\in[H-1]\times[K], ∀B∈𝒫hk\forall B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and ∀(x,a)∈B\forall(x,a)\in B:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | |𝔼X∼T¯hk(⋅|B)​[Vh+1∗​(X)]−𝔼Y∼Th(⋅|x,a)​[Vh+1∗​(Y)]|\displaystyle\left|\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[V\_{h+1}^{\*}(X)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(Y)]\right| |  | (B.15) |
|  |  | ≤\displaystyle\leq | 3C¯h+1(1+C~(m,d𝒮)(∥μ^hk(B)∥mΔm+∥Σ^hk(B)∥m2Δm2+∥μh(x,a)∥mΔm\displaystyle\sqrt{3}\,\overline{C}\_{h+1}\Big(1+{\widetilde{C}(m,d\_{\mathcal{S}})}(\|\widehat{\mu}\_{h}^{k}(B)\|^{m}\Delta^{m}+\|\widehat{\Sigma}\_{h}^{k}(B)\|^{\frac{m}{2}}\Delta^{\frac{m}{2}}+\|\mu\_{h}(x,a)\|^{m}\Delta^{m} |  |
|  |  |  | +∥Σh(x,a)∥m2Δm2))×𝒲¯2(𝒩(μ^hk(B)Δ,Σ^hk(B)Δ),𝒩(μh(x,a)Δ,Σh(x,a)Δ))\displaystyle\quad+\|\Sigma\_{h}(x,a)\|^{\frac{m}{2}}\Delta^{\frac{m}{2}})\Big)\times\overline{\mathcal{W}}\_{2}\Big(\mathcal{N}(\widehat{\mu}\_{h}^{k}(B)\Delta,\widehat{\Sigma}\_{h}^{k}(B)\Delta),\mathcal{N}(\mu\_{h}(x,a)\Delta,\Sigma\_{h}(x,a)\Delta)\Big) |  |
|  |  | ≤\displaystyle\leq | 3C¯max(1+C~(m,d𝒮)(2m(κμ(δ,∥x~(oB)∥,nhk(B))m+η(∥x~(oB)∥)m)Δm\displaystyle\sqrt{3}\,\overline{C}\_{\max}\Bigg(1+{\widetilde{C}(m,d\_{\mathcal{S}})}\Bigg(2^{m}\Big(\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{m}+\eta(\|\tilde{x}(^{o}B)\|)^{m}\Big)\Delta^{m} |  |
|  |  |  | +3m2(κμ(δ,∥x~(oB)∥,nhk(B))mΔm2+κΣ(δ,∥x~(oB)∥,nhk(B))m2\displaystyle\quad+3^{\frac{m}{2}}\Big(\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{m}\Delta^{\frac{m}{2}}+\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{\frac{m}{2}} |  |
|  |  |  | +(η(∥x~(oB)∥)2+L2D2Δ)m2)Δm2\displaystyle\quad+\Big(\eta(\|\tilde{x}(^{o}B)\|)^{2}+L^{2}D^{2}\Delta\Big)^{\frac{m}{2}}\Big)\Delta^{\frac{m}{2}} |  |
|  |  |  | +η(∥x~(oB)∥)mΔm+η(∥x~(oB)∥)mΔm2))\displaystyle\quad+\eta(\|\tilde{x}(^{o}B)\|)^{m}\Delta^{m}+\eta(\|\tilde{x}(^{o}B)\|)^{m}\Delta^{\frac{m}{2}}\Bigg)\Bigg) |  |
|  |  |  | ×(κμ(δ,∥x~(oB)∥,nhk(B))Δ+κμ(δ,∥x~(oB)∥,nhk(B))2Δ32λ\displaystyle\quad\times\Big(\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\Delta+\kappa\_{\mu}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))^{2}\frac{\Delta^{\frac{3}{2}}}{\sqrt{\lambda}} |  |
|  |  |  | +κΣ(δ,∥x~(oB)∥,nhk(B))d𝒮​Δ12λ+T-BIAS(B))\displaystyle\quad+\kappa\_{\Sigma}(\delta,\|\tilde{x}(^{o}B)\|,n\_{h}^{k}(B))\frac{\sqrt{d\_{\mathcal{S}}}\Delta^{\frac{1}{2}}}{\sqrt{\lambda}}+\mbox{\rm T-BIAS}(B)\Big) |  |
|  |  | ≤\displaystyle\leq | T-UCBhk(B)+LV(δ,∥x~(oB)∥)T-BIAS(B),\displaystyle\mbox{\rm T-UCB}\_{h}^{k}(B)+L\_{V}(\delta,\|\tilde{x}(^{o}B)\|)\,\,\mbox{\rm T-BIAS}(B), |  |

where the first inequality holds due to Lemma [B.4](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem4 "Lemma B.4. ‣ B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). In addition, the second inequality holds due to ([B.12](https://arxiv.org/html/2512.14991v1#A2.E12 "In B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([B.14](https://arxiv.org/html/2512.14991v1#A2.E14 "In B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the power-mean inequality and ([4.10](https://arxiv.org/html/2512.14991v1#S4.E10 "In Theorem 4.3. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). Finally, the third inequality holds since nhk​(B)≥1\sqrt{n\_{h}^{k}(B)}\geq 1.

∎

### B.7 Proof of Lemma [4.6](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

For B∈𝒫hkB\in\mathcal{P}\_{h}^{k}, h∈[H]h\in[H] and k∈JρKk\in J\_{\rho}^{K}:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | CONFhk​(B)\displaystyle{\rm CONF}\_{h}^{k}(B) | =\displaystyle= | g1(δ,∥x~(oB)∥)nhk​(B)\displaystyle\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|)}{\sqrt{n\_{h}^{k}(B)}} |  | (B.16) |
|  |  | ≤\displaystyle\leq | g1(δ,∥x~(opar(B))∥)nhk​(par​(B))=CONFhk​(par​(B))\displaystyle\frac{g\_{1}(\delta,\|\tilde{x}(^{o}{\rm par}(B))\|)}{\sqrt{n\_{h}^{k}({\rm par}(B))}}={\rm CONF}\_{h}^{k}({\rm par}(B)) |  |
|  |  | ≤\displaystyle\leq | diam​(par​(B))=2​diam​(B),\displaystyle{\rm diam}({\rm par}(B))=2\,\,{\rm diam}(B), |  |

where par​(B){\rm par}(B) is the parent block of BB and we use the fact that Bo=opar​(B){}^{o}B=\,^{o}{\rm par}(B).

Rearranging ([B.16](https://arxiv.org/html/2512.14991v1#A2.E16 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | nhk​(B)≥(g1(δ,∥x~(oB)∥)2​diam​(B))2.\displaystyle n\_{h}^{k}(B)\geq\Big(\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|)}{2\,\,{\rm diam}(B)}\Big)^{2}. |  | (B.17) |

In addition, nhk​(B)n\_{h}^{k}(B) must satisfy CONFhk​(B)>diam​(B){\rm CONF}\_{h}^{k}(B)>{\rm diam}(B), hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | nhk​(B)<(g1(δ,∥x~(oB)∥)diam​(B))2.\displaystyle n\_{h}^{k}(B)<\Big(\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|)}{{\rm diam}(B)}\Big)^{2}. |  | (B.18) |

Let l​(B)l(B) be the total number of ancestors of BB in the adaptive partition and denote them as B0,B1,…,Bl​(B)−1B\_{0},B\_{1},...,B\_{l(B)-1} arranged in descending order of size. Also denote BB as Bl​(B)B\_{l(B)} for consistency. Then we have

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nhk​(B)diam​(Bhki)nhk​(B)≤∑l=0l​(B)−1|{k′:Bhk′=Bl}|​diam​(Bl)∑l=0l​(B)−1|{k′:Bhk′=Bl}|.\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}\leq\frac{\sum\_{l=0}^{l(B)-1}|\{k^{\prime}:B\_{h}^{k^{\prime}}=B\_{l}\}|{\rm diam}(B\_{l})}{\sum\_{l=0}^{l(B)-1}|\{k^{\prime}:B\_{h}^{k^{\prime}}=B\_{l}\}|}. |  |

By ([B.17](https://arxiv.org/html/2512.14991v1#A2.E17 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([B.18](https://arxiv.org/html/2512.14991v1#A2.E18 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")):

|  |  |  |
| --- | --- | --- |
|  | |{k′:Bhk′=Bl}|≤(g1(δ,∥x~(oB)∥)diam​(B))2−(g1(δ,∥x~(oB)∥)2​diam​(B))2=34​g1(δ,∥x~(oB)∥)2diam​(Bl)2.\displaystyle|\{k^{\prime}:B\_{h}^{k^{\prime}}=B\_{l}\}|\leq\left(\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|)}{{\rm diam}(B)}\right)^{2}-\left(\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|)}{2\,\,{\rm diam}(B)}\right)^{2}=\frac{3}{4}\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|)^{2}}{{\rm diam}(B\_{l})^{2}}. |  |

Note that diam​(Bl)=2−l​D{\rm diam}(B\_{l})=2^{-l}D, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑i=1nhk​(B)diam​(Bhki)nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)} | ≤\displaystyle\leq | ∑l=0l​(B)−1|{k′:Bhk′=Bl}|​diam​(Bl)∑l=0l​(B)−1|{k′:Bhk′=Bl}|\displaystyle\frac{\sum\_{l=0}^{l(B)-1}|\{k^{\prime}:B\_{h}^{k^{\prime}}=B\_{l}\}|{\rm diam}(B\_{l})}{\sum\_{l=0}^{l(B)-1}|\{k^{\prime}:B\_{h}^{k^{\prime}}=B\_{l}\}|} |  |
|  |  | ≤\displaystyle\leq | ∑l=0l​(B)−12−l​22​l∑l=0l​(B)−122​l​D≤4×2−l​(B)​D=4​diam​(B).\displaystyle\frac{\sum\_{l=0}^{l(B)-1}2^{-l}2^{2l}}{\sum\_{l=0}^{l(B)-1}2^{2l}}D\leq 4\times 2^{-l(B)}D=4\,\,{\rm diam}(B). |  |

Then since diam​(Bhki)≤D{\rm diam}(B\_{h}^{k\_{i}})\leq D, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑i=1nhk​(B)diam​(Bhki)2nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})^{2}}{n\_{h}^{k}(B)} | ≤\displaystyle\leq | ∑i=1nhk​(B)diam​(Bhki)nhk​(B)​D\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}D |  |
|  |  | ≤\displaystyle\leq | 4​D​diam​(B),\displaystyle 4D\,\ {\rm diam}(B), |  |

where the second inequality holds due to ([4.22](https://arxiv.org/html/2512.14991v1#S4.E22 "In Lemma 4.6. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
∎

## Appendix C Technical details in Section [5](https://arxiv.org/html/2512.14991v1#S5 "5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

### C.1 Proof of Theorem [5.2](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem2 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

We first state a proposition before proving the main theorem.

###### Proposition C.1.

With the same assumptions as in Theorem [4.5](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), the following inequality holds for all (h,k)∈[H]×[K](h,k)\in[H]\times[K], B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and any (x,a)∈B(x,a)\in B:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)−R¯h​(x,a)|≤R-BIAS​(B).\displaystyle\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\bar{R}\_{h}(x,a)\right|\leq\mbox{\rm R-BIAS}(B). |  | (C.1) |

###### Proof of Proposition [C.1](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem1 "Proposition C.1. ‣ C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |∑i=1nhk​(B)R¯h​(Xhki,Ahki)nhk​(B)−R¯h​(x,a)|\displaystyle\left|\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})}{n\_{h}^{k}(B)}-\bar{R}\_{h}(x,a)\right| | ≤\displaystyle\leq | ∑i=1nhk​(B)|R¯h​(Xhki,Ahki)−R¯h​(x,a)|nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}|\bar{R}\_{h}(X\_{h}^{k\_{i}},A\_{h}^{k\_{i}})-\bar{R}\_{h}(x,a)|}{n\_{h}^{k}(B)} |  |
|  |  | ≤\displaystyle\leq | ∑i=1nhk​(B)L​(1+‖Xhki‖m+‖x‖m)​(‖Xhki−x‖+‖Ahki−a‖)nhk​(B)\displaystyle\frac{\sum\_{i=1}^{n\_{h}^{k}(B)}L(1+\|X\_{h}^{k\_{i}}\|^{m}+\|x\|^{m})(\|X\_{h}^{k\_{i}}-x\|+\|A\_{h}^{k\_{i}}-a\|)}{n\_{h}^{k}(B)} |  |
|  |  | ≤\displaystyle\leq | 2L(1+2(∥x~(oB)∥+D)m)∑i=1nhk​(B)diam​(Bhki)nhk​(B)\displaystyle 2L\Big(1+2(\|\tilde{x}(^{o}B)\|+D)^{m}\Big)\sum\_{i=1}^{n\_{h}^{k}(B)}\frac{{\rm diam}(B\_{h}^{k\_{i}})}{n\_{h}^{k}(B)} |  |
|  |  | ≤\displaystyle\leq | R-BIAS​(B).\displaystyle\mbox{\rm R-BIAS}(B). |  |

Here, we apply ([4.22](https://arxiv.org/html/2512.14991v1#S4.E22 "In Lemma 4.6. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) to get the last inequality.
∎

Then we proceed to the proof of Theorem [5.2](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem2 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Proof.

Recall from Theorems [4.4](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [4.5](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we know that with probability at least 1−3​δ1-3\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ([4.4](https://arxiv.org/html/2512.14991v1#S4.Ex20 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([4.18](https://arxiv.org/html/2512.14991v1#S4.E18 "In Theorem 4.5. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) hold simultaneously,\displaystyle\eqref{eq:transition kernel wasserstein local lipschitz all together}\mbox{ and }\eqref{eq:reward high prob bound}\mbox{ hold simultaneously}, |  | (C.2) |

This fact serves as a building block of the proof.

For k=0k=0, with the initialization of (Q¯h0(\overline{Q}\_{h}^{0}, V~h0)h∈[H]\widetilde{V}\_{h}^{0})\_{h\in[H]} in ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we know ([5.2](https://arxiv.org/html/2512.14991v1#S5.Ex10 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds.
Now assume that ([5.2](https://arxiv.org/html/2512.14991v1#S5.Ex10 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for k−1k-1 and we prove it holds for kk.

For the case of h=Hh=H:
For B∈𝒫HkB\in\mathcal{P}\_{H}^{k} with nHk​(B)>0n\_{H}^{k}(B)>0 and for any (x,a)∈B(x,a)\in B, note that by ([4.18](https://arxiv.org/html/2512.14991v1#S4.E18 "In Theorem 4.5. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.1](https://arxiv.org/html/2512.14991v1#A3.E1 "In Proposition C.1. ‣ C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) :

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^Hk​(B)−R¯H​(x,a)≥−R-UCBHk​(B)−R-BIAS​(B).\displaystyle\widehat{R}\_{H}^{k}(B)-\bar{R}\_{H}(x,a)\geq-\mbox{\rm R-UCB}\_{H}^{k}(B)-\mbox{\rm R-BIAS}(B). |  | (C.3) |

Therefore
Q¯Hk​(B)=R^Hk​(B)+R-UCBHk​(B)+R-BIAS​(B)≥QH∗​(x,a).\overline{Q}\_{H}^{k}(B)=\widehat{R}\_{H}^{k}(B)+\mbox{\rm R-UCB}\_{H}^{k}(B)+\mbox{\rm R-BIAS}(B)\geq Q\_{H}^{\*}(x,a). For B∈𝒫HkB\in\mathcal{P}\_{H}^{k} with nHk​(B)=0n\_{H}^{k}(B)=0, by ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")),
we have Q¯Hk​(B)=Q¯H0​(B)≥QH∗​(x,a).\overline{Q}\_{H}^{k}(B)=\overline{Q}\_{H}^{0}(B)\geq Q\_{H}^{\*}(x,a). So we proved the first inequality in ([5.2](https://arxiv.org/html/2512.14991v1#S5.Ex10 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

For any S∈Γ𝒮​(𝒫Hk)S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{H}^{k}) and any x∈Sx\in S,
we have V~Hk−1​(S)≥VH∗​(x)\widetilde{V}\_{H}^{k-1}(S)\geq V^{\*}\_{H}(x) by induction.
Furthermore,

|  |  |  |
| --- | --- | --- |
|  | V~Hk​(S)=maxB∈𝒫Hk,Γ𝒮​(B)⊃S⁡Q¯Hk​(B)≥Q¯Hk​(B∗)≥QH∗​(x,aH∗​(x))=VH∗​(x),\displaystyle\widetilde{V}\_{H}^{k}(S)=\max\_{B\in\mathcal{P}\_{H}^{k},\Gamma\_{\mathcal{S}}(B)\supset S}\overline{Q}\_{H}^{k}(B)\geq\overline{Q}\_{H}^{k}(B^{\*})\geq Q\_{H}^{\*}(x,a\_{H}^{\*}(x))=V\_{H}^{\*}(x), |  |

where B∗∈𝒫HkB^{\*}\in\mathcal{P}\_{H}^{k} is defined such that (x,aH∗​(x))∈B∗(x,a\_{H}^{\*}(x))\in B^{\*}. Hence
we have V~Hk​(S)≥VH∗​(x)\widetilde{V}\_{H}^{k}(S)\geq V^{\*}\_{H}(x).

Finally, we check V¯Hk​(x)≥VH∗​(x)\bar{V}^{k}\_{H}(x)\geq V\_{H}^{\*}(x). For any x∈𝒮1x\in\mathcal{S}\_{1}, there exits some S′∈Γ𝒮​(𝒫Hk)S^{\prime}\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{H}^{k}) such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V¯Hk​(x)\displaystyle\overline{V}\_{H}^{k}(x) | =\displaystyle= | V~hk​(S′)+CH​(1+‖x‖m+‖x~​(S′)‖m)​‖x−x~​(S′)‖\displaystyle\widetilde{V}\_{h}^{k}(S^{\prime})+C\_{H}(1+\|x\|^{m}+\|\tilde{x}(S^{\prime})\|^{m})\|x-\tilde{x}(S^{\prime})\| |  |
|  |  | ≥\displaystyle\geq | VH∗​(x~​(S′))+CH​(1+‖x‖m+‖x~​(S′)‖m)​‖x−x~​(S′)‖\displaystyle V\_{H}^{\*}(\tilde{x}(S^{\prime}))+C\_{H}(1+\|x\|^{m}+\|\tilde{x}(S^{\prime})\|^{m})\|x-\tilde{x}(S^{\prime})\| |  |
|  |  | ≥\displaystyle\geq | VH∗​(x),\displaystyle V\_{H}^{\*}(x), |  |

where the last inequality holds since |VH∗​(x~​(S′))−VH∗​(x)|≤CH​(1+‖x‖m+‖x~​(S′)‖m)​‖x−x~​(S′)‖|V\_{H}^{\*}(\tilde{x}(S^{\prime}))-V\_{H}^{\*}(x)|\leq C\_{H}(1+\|x\|^{m}+\|\tilde{x}(S^{\prime})\|^{m})\|x-\tilde{x}(S^{\prime})\| by ([2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

For x∈ℝd𝒮∖𝒮1x\in\mathbb{R}^{d\_{\mathcal{S}}}\setminus\mathcal{S}\_{1}, by ([5.10](https://arxiv.org/html/2512.14991v1#S5.E10 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we know that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V¯Hk​(x)\displaystyle\overline{V}\_{H}^{k}(x) | =\displaystyle= | V¯Hk​(ρ‖x‖​x)+CH​(1+‖x‖m+ρm)​‖(1−ρ‖x‖)​x‖\displaystyle\overline{V}\_{H}^{k}\left(\frac{\rho}{\|x\|}x\right)+C\_{H}(1+\|x\|^{m}+\rho^{m})\left\|\left(1-\frac{\rho}{\|x\|}\right)x\right\| |  |
|  |  | ≥\displaystyle\geq | VH∗​(ρ‖x‖​x)+CH​(1+‖x‖m+ρm)​‖(1−ρ‖x‖)​x‖\displaystyle V\_{H}^{\*}(\frac{\rho}{\|x\|}x)+C\_{H}(1+\|x\|^{m}+\rho^{m})\left\|(1-\frac{\rho}{\|x\|})x\right\| |  |
|  |  | ≥\displaystyle\geq | VH∗​(x),\displaystyle V\_{H}^{\*}(x), |  |

where the first inequality holds since ρ‖x‖​x∈𝒮1\frac{\rho}{\|x\|}x\in\mathcal{S}\_{1}.

Induction (h+1↦hh+1\mapsto h):
Assume ([5.2](https://arxiv.org/html/2512.14991v1#S5.Ex10 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds for h+1h+1 and we now show it also holds for hh.

For B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, by ([4.18](https://arxiv.org/html/2512.14991v1#S4.E18 "In Theorem 4.5. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.1](https://arxiv.org/html/2512.14991v1#A3.E1 "In Proposition C.1. ‣ C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^hk​(B)−R¯h​(x,a)≥−R-UCBhk​(B)−R-BIAS​(B).\displaystyle\widehat{R}\_{h}^{k}(B)-\bar{R}\_{h}(x,a)\geq-\mbox{\rm R-UCB}\_{h}^{k}(B)-\mbox{\rm R-BIAS}(B). |  | (C.4) |

We also have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 𝔼X∼T¯hk(⋅|B)​[V¯h+1k​(X)]−𝔼X∼Th(⋅|x,a)​[Vh+1∗​(X)]\displaystyle\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(X)] |  | (C.5) |
|  |  | ≥\displaystyle\geq | 𝔼X∼T¯hk(⋅|B)​[Vh+1∗​(X)]−𝔼X∼Th(⋅|x,a)​[Vh+1∗​(X)]\displaystyle\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[V\_{h+1}^{\*}(X)]-\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(X)] |  |
|  |  | ≥\displaystyle\geq | −T-UCBhk(B)−LV(δ,∥x~(oB)∥)T-BIAS(B).\displaystyle-\mbox{\rm T-UCB}\_{h}^{k}(B)-L\_{V}(\delta,\|\tilde{x}(^{o}B)\|)\mbox{\rm T-BIAS}(B). |  |

The first inequality holds by induction hypothesis on h+1h+1 and the second inequality holds due to ([4.4](https://arxiv.org/html/2512.14991v1#S4.Ex20 "Theorem 4.4. ‣ 4.2 Concentration inequalities for transition kernel estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([4.23](https://arxiv.org/html/2512.14991v1#S4.E23 "In Theorem 4.7. ‣ 4.4 Bias of the estimators ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Combining ([C.4](https://arxiv.org/html/2512.14991v1#A3.E4 "In C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.5](https://arxiv.org/html/2512.14991v1#A3.E5 "In C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have

|  |  |  |
| --- | --- | --- |
|  | Q¯hk​(B)=R^hk​(B)+R-UCBhk​(B)+𝔼X∼T¯hk(⋅|B)​[V¯h+1k​(X)]+T-UCBhk​(B)+BIAS​(B)≥Qh∗​(x,a).\overline{Q}\_{h}^{k}(B)=\widehat{R}\_{h}^{k}(B)+\mbox{\rm R-UCB}\_{h}^{k}(B)+\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\overline{V}\_{h+1}^{k}(X)]+\mbox{\rm T-UCB}\_{h}^{k}(B)+{\rm BIAS}(B)\geq Q\_{h}^{\*}(x,a). |  |

For B∈𝒫hkB\in\mathcal{P}\_{h}^{k} with nhk​(B)=0n\_{h}^{k}(B)=0, by ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we also have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q¯hk​(B)=Q¯h0​(B)≥Qh∗​(x,a).\displaystyle\overline{Q}\_{h}^{k}(B)=\overline{Q}\_{h}^{0}(B)\geq Q\_{h}^{\*}(x,a). |  | (C.6) |

For any S∈Γ𝒮​(𝒫hk)S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k}) and any x∈Sx\in S,
V~hk−1​(S)≥Vh∗​(x)\widetilde{V}\_{h}^{k-1}(S)\geq V^{\*}\_{h}(x) holds by induction, and

|  |  |  |
| --- | --- | --- |
|  | maxB∈𝒫hk,Γ𝒮​(B)⊃S⁡Q¯hk​(B)≥Q¯hk​(B∗)≥Qh∗​(x,ah∗​(x))=Vh∗​(x),\max\_{B\in\mathcal{P}\_{h}^{k},\Gamma\_{\mathcal{S}}(B)\supset S}\overline{Q}\_{h}^{k}(B)\geq\overline{Q}\_{h}^{k}(B^{\*})\geq Q\_{h}^{\*}(x,a\_{h}^{\*}(x))=V\_{h}^{\*}(x), |  |

where B∗∈𝒫hkB^{\*}\in\mathcal{P}\_{h}^{k} is the block containing (x,ah∗​(x))(x,a\_{h}^{\*}(x)).
Hence V~hk​(S)≥Vh∗​(x).\widetilde{V}\_{h}^{k}(S)\geq V^{\*}\_{h}(x).

Finally, for any x∈𝒮1x\in\mathcal{S}\_{1}, there exists a S′∈Γ𝒮​(𝒫hk)S^{\prime}\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k}) such that,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V¯hk​(x)\displaystyle\overline{V}\_{h}^{k}(x) | =\displaystyle= | V~hk​(S′)+Ch​(1+‖x‖m+‖x~​(S′)‖m)​‖x−x~​(S′)‖\displaystyle\widetilde{V}\_{h}^{k}(S^{\prime})+C\_{h}(1+\|x\|^{m}+\|\tilde{x}(S^{\prime})\|^{m})\|x-\tilde{x}(S^{\prime})\| |  |
|  |  | ≥\displaystyle\geq | Vh∗​(x~​(S′))+Ch​(1+‖x‖m+‖x~​(S′)‖m)​‖x−x~​(S′)‖\displaystyle V\_{h}^{\*}(\tilde{x}(S^{\prime}))+C\_{h}(1+\|x\|^{m}+\|\tilde{x}(S^{\prime})\|^{m})\|x-\tilde{x}(S^{\prime})\| |  |
|  |  | ≥\displaystyle\geq | Vh∗​(x),\displaystyle V\_{h}^{\*}(x), |  |

where the last inequality holds since |Vh∗​(x~​(S′))−Vh∗​(x)|≤Ch​(1+‖x‖m+‖x~​(S′)‖m)​‖x−x~​(S′)‖|V\_{h}^{\*}(\tilde{x}(S^{\prime}))-V\_{h}^{\*}(x)|\leq C\_{h}(1+\|x\|^{m}+\|\tilde{x}(S^{\prime})\|^{m})\|x-\tilde{x}(S^{\prime})\| by ([2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

For x∈ℝd𝒮∖𝒮1x\in\mathbb{R}^{d\_{\mathcal{S}}}\setminus\mathcal{S}\_{1}, we know that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V¯hk​(x)\displaystyle\overline{V}\_{h}^{k}(x) | =\displaystyle= | V¯hk​(ρ‖x‖​x)+Ch​(1+‖x‖m+ρm)​‖(1−ρ‖x‖)​x‖\displaystyle\overline{V}\_{h}^{k}\left(\frac{\rho}{\|x\|}x\right)+C\_{h}(1+\|x\|^{m}+\rho^{m})\left\|\left(1-\frac{\rho}{\|x\|}\right)x\right\| |  |
|  |  | ≥\displaystyle\geq | Vh∗​(ρ‖x‖​x)+Ch​(1+‖x‖m+ρm)​‖(1−ρ‖x‖)​x‖\displaystyle V\_{h}^{\*}(\frac{\rho}{\|x\|}x)+C\_{h}(1+\|x\|^{m}+\rho^{m})\left\|(1-\frac{\rho}{\|x\|})x\right\| |  |
|  |  | ≥\displaystyle\geq | Vh∗​(x),\displaystyle V\_{h}^{\*}(x), |  |

where the first inequality holds since ρ‖x‖​x∈𝒮1\frac{\rho}{\|x\|}x\in\mathcal{S}\_{1}.
∎

### C.2 Proof of Theorem [5.3](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem3 "Theorem 5.3. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

We divide the proof subject into three cases.

Case (1) ‖x1‖≤ρ,‖x2‖≤ρ\|x\_{1}\|\leq\rho,\|x\_{2}\|\leq\rho. Without lose of generality, let us assume ‖x1‖≥‖x2‖\|x\_{1}\|\geq\|x\_{2}\|.

For i=1,2i=1,2, define S¯i:=arg⁡minS∈ΓS​(𝒫hk)⁡Vh,klocal​(xi,S)\overline{S}\_{i}:=\arg\min\_{S\in\Gamma\_{S}(\mathcal{P}\_{h}^{k})}V\_{h,k}^{\rm local}(x\_{i},S), and denote S~i\widetilde{S}\_{i} as the state block such that xi∈S~ix\_{i}\in\widetilde{S}\_{i} and S~i∈Γ𝒮​(𝒫hk)\widetilde{S}\_{i}\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h}^{k}).
Then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯hk​(xi)=Vh,klocal​(xi,S¯i)≤Vh,klocal​(xi,S~i).\displaystyle\overline{V}\_{h}^{k}(x\_{i})=V\_{h,k}^{\rm local}(x\_{i},\overline{S}\_{i})\leq V\_{h,k}^{\rm local}(x\_{i},\tilde{S}\_{i}). |  | (C.7) |

By the last inequality, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ‖xi−x~​(S¯i)‖\displaystyle\|x\_{i}-\tilde{x}(\overline{S}\_{i})\| |  | (C.8) |
|  |  | ≤\displaystyle\leq | V~hk​(S~i)+Ch​(1+‖xi‖m+‖x~​(S~i)‖m)​‖xi−x~​(S~i)‖−V~hk​(S¯i)Ch​(1+‖xi‖m+‖x~​(S¯i)‖m)\displaystyle\frac{\widetilde{V}\_{h}^{k}(\widetilde{S}\_{i})+C\_{h}\Big(1+\|x\_{i}\|^{m}+\|\tilde{x}(\widetilde{S}\_{i})\|^{m}\Big)\|x\_{i}-\tilde{x}(\widetilde{S}\_{i})\|-\widetilde{V}\_{h}^{k}(\overline{S}\_{i})}{C\_{h}\Big(1+\|x\_{i}\|^{m}+\|\tilde{x}(\overline{S}\_{i})\|^{m}\Big)} |  |
|  |  | ≤\displaystyle\leq | |V~hk​(S~i)|+|V~hk​(S¯i)|+Ch​(1+‖xi‖m+‖x~​(S~i)‖m)​DCh​(1+‖xi‖m+‖x~​(S¯i)‖m)\displaystyle\frac{\Big|\widetilde{V}\_{h}^{k}(\widetilde{S}\_{i})\Big|+\Big|\widetilde{V}\_{h}^{k}(\overline{S}\_{i})\Big|+C\_{h}\Big(1+\|x\_{i}\|^{m}+\|\tilde{x}(\widetilde{S}\_{i})\|^{m}\Big)D}{C\_{h}\Big(1+\|x\_{i}\|^{m}+\|\tilde{x}(\overline{S}\_{i})\|^{m}\Big)} |  |
|  |  | ≤\displaystyle\leq | C~h​(2+(‖xi‖+2​D)m+1+(‖x~​(S¯i)‖+2​D)m+1)+Ch​(1+‖xi‖m+(‖xi‖+D)m)​DCh​(1+‖xi‖m+‖x~​(S¯i)‖m)\displaystyle\frac{\widetilde{C}\_{h}\Big(2+(\|x\_{i}\|+2D)^{m+1}+(\|\tilde{x}(\overline{S}\_{i})\|+2D)^{m+1}\Big)+C\_{h}\Big(1+\|x\_{i}\|^{m}+(\|x\_{i}\|+D)^{m}\Big)D}{C\_{h}\Big(1+\|x\_{i}\|^{m}+\|\tilde{x}(\overline{S}\_{i})\|^{m}\Big)} |  |
|  |  | ≤\displaystyle\leq | C~h​(2+2m​‖xi‖m+1+2m​‖x~​(S¯i)‖m+1+22​m+1​Dm+1)Ch​(1+‖xi‖m+‖x~​(S¯i)‖m)\displaystyle\frac{\widetilde{C}\_{h}\Big(2+2^{m}\|x\_{i}\|^{m+1}+2^{m}\|\tilde{x}(\overline{S}\_{i})\|^{m+1}+2^{2m+1}D^{m+1}\Big)}{C\_{h}\Big(1+\|x\_{i}\|^{m}+\|\tilde{x}(\overline{S}\_{i})\|^{m}\Big)} |  |
|  |  |  | +Ch​(1+(2m−1+1)​‖xi‖m+2m−1​Dm)​DCh​(1+‖xi‖m+‖x~​(S¯i)‖m)\displaystyle\,\,+\frac{C\_{h}\Big(1+(2^{m-1}+1)\|x\_{i}\|^{m}+2^{m-1}D^{m}\Big)D}{C\_{h}\Big(1+\|x\_{i}\|^{m}+\|\tilde{x}(\overline{S}\_{i})\|^{m}\Big)} |  |
|  |  | ≤\displaystyle\leq | 12​(‖xi‖+‖x~​(S¯i)‖)+c˘0,\displaystyle\frac{1}{2}(\|x\_{i}\|+\|\tilde{x}(\overline{S}\_{i})\|)+\breve{c}\_{0}, |  |

where c˘0\breve{c}\_{0} a positive constant depending on D,m,Ch,C~hD,m,C\_{h},\widetilde{C}\_{h}.
The first inequality holds due to ([C.7](https://arxiv.org/html/2512.14991v1#A3.E7 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the definition of Vh,klocal(.,.)V\_{h,k}^{\rm local}(.,.) in ([5.12](https://arxiv.org/html/2512.14991v1#S5.E12 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). The third inequality holds with probability at least 1−3​δ1-3\delta due to ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), Theorem [5.2](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem2 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), and the fact that ‖x−x~​(S~i)‖≤D\|x-\tilde{x}(\widetilde{S}\_{i})\|\leq D. The fourth inequality holds due to the power-mean inequality. The last inequality holds by the fact that Ch≥2m+1​C~hC\_{h}\geq 2^{m+1}\widetilde{C}\_{h}.

By the triangle inequalty ‖x~​(S¯i)‖−‖xi‖≤‖xi−x~​(S¯i)‖\|\tilde{x}(\overline{S}\_{i})\|-\|x\_{i}\|\leq\|x\_{i}-\tilde{x}(\overline{S}\_{i})\| and ([C.8](https://arxiv.org/html/2512.14991v1#A3.E8 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖x~​(S¯i)‖≤3​‖xi‖+2​c˘0.\displaystyle\|\tilde{x}(\overline{S}\_{i})\|\leq 3\|x\_{i}\|+2\breve{c}\_{0}. |  | (C.9) |

Now we are ready to bound |V¯hk​(x1)−V¯hk​(x2)||\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})| by two terms.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |V¯hk​(x1)−V¯hk​(x2)|\displaystyle|\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})| |  |
|  |  | =\displaystyle= | (V¯hk​(x1)−V¯hk​(x2))​𝕀{V¯hk​(x1)−V¯hk​(x2)≥0}+(V¯hk​(x2)−V¯hk​(x1))​𝕀{V¯hk​(x1)−V¯hk​(x2)<0}\displaystyle(\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2}))\mathbb{I}\_{\{\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})\geq 0\}}+(\overline{V}\_{h}^{k}(x\_{2})-\overline{V}\_{h}^{k}(x\_{1}))\mathbb{I}\_{\{\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})<0\}} |  |
|  |  | ≤\displaystyle\leq | |Vh,klocal​(x1,S¯2)−Vh,klocal​(x2,S¯2)|⏟(I)+|Vh,klocal​(x2,S¯1)−VH,klocal​(x1,S¯1)|⏟(I​I),\displaystyle\underbrace{\Big|V\_{h,k}^{\rm local}(x\_{1},\overline{S}\_{2})-V\_{h,k}^{\rm local}(x\_{2},\overline{S}\_{2})\Big|}\_{(I)}+\underbrace{\Big|V\_{h,k}^{\rm local}(x\_{2},\overline{S}\_{1})-V\_{H,k}^{\rm local}(x\_{1},\overline{S}\_{1})\Big|}\_{(II)}, |  |

where the inequality holds due to ([C.7](https://arxiv.org/html/2512.14991v1#A3.E7 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

For term (I),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |Vh,klocal​(x1,S¯2)−Vh,klocal​(x2,S¯2)|\displaystyle\Big|V\_{h,k}^{\rm local}(x\_{1},\overline{S}\_{2})-V\_{h,k}^{\rm local}(x\_{2},\overline{S}\_{2})\Big| |  |
|  |  | ≤\displaystyle\leq | Ch​(1+‖x~​(S¯2)‖m)​‖x1−x2​‖+Ch|​‖x1‖m​‖x1−x~​(S¯2)‖−‖x2‖m​‖x2−x~​(S¯2)‖|\displaystyle C\_{h}\Bigg(1+\|\tilde{x}(\overline{S}\_{2})\|^{m}\Bigg)\|x\_{1}-x\_{2}\|+C\_{h}\Bigg|\|x\_{1}\|^{m}\|x\_{1}-\tilde{x}(\overline{S}\_{2})\|-\|x\_{2}\|^{m}\|x\_{2}-\tilde{x}(\overline{S}\_{2})\|\Bigg| |  |
|  |  | ≤\displaystyle\leq | Ch​(1+(3​‖x2‖+2​c˘0)m)​‖x1−x2‖+‖x1‖m​‖x1−x2‖+(4​‖x2‖+2​c˘0)​|‖x1‖m−‖x2‖m|,\displaystyle C\_{h}\Bigg(1+(3\|x\_{2}\|+2\breve{c}\_{0})^{m}\Bigg)\|x\_{1}-x\_{2}\|+\|x\_{1}\|^{m}\|x\_{1}-x\_{2}\|+(4\|x\_{2}\|+2\breve{c}\_{0})\Big|\|x\_{1}\|^{m}-\|x\_{2}\|^{m}\Big|, |  |

where the first inequality holds by triangle inequality and the second inequality holds due to ([C.9](https://arxiv.org/html/2512.14991v1#A3.E9 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Similarly, for term (II):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |Vh,klocal​(x2,S¯1)−VH,klocal​(x1,S¯1)|\displaystyle\Big|V\_{h,k}^{\rm local}(x\_{2},\overline{S}\_{1})-V\_{H,k}^{\rm local}(x\_{1},\overline{S}\_{1})\Big| |  |
|  |  | ≤\displaystyle\leq | Ch​(1+(3​‖x1‖+2​c˘0)m)​‖x1−x2‖+‖x2‖m​‖x1−x2‖+(4​‖x1‖+2​c˘0)​|‖x1‖m−‖x2‖m|.\displaystyle C\_{h}\Bigg(1+(3\|x\_{1}\|+2\breve{c}\_{0})^{m}\Bigg)\|x\_{1}-x\_{2}\|+\|x\_{2}\|^{m}\|x\_{1}-x\_{2}\|+(4\|x\_{1}\|+2\breve{c}\_{0})\Big|\|x\_{1}\|^{m}-\|x\_{2}\|^{m}\Big|. |  |

It is clear that m=0m=0 is a trivial case, so we only consider m≥1m\geq 1, with which we have

|  |  |  |
| --- | --- | --- |
|  | |‖x1‖m−‖x2‖m|≤(m−1)​‖x1‖m−1​‖x1−x2‖, and ​‖x1‖m−1≤m−1m​‖x1‖m+1m.\Big|\|x\_{1}\|^{m}-\|x\_{2}\|^{m}\Big|\leq(m-1)\|x\_{1}\|^{m-1}\|x\_{1}-x\_{2}\|,\mbox{ and }\|x\_{1}\|^{m-1}\leq\frac{m-1}{m}\|x\_{1}\|^{m}+\frac{1}{m}. |  |

Combine ([C.2](https://arxiv.org/html/2512.14991v1#A3.Ex29 "C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.2](https://arxiv.org/html/2512.14991v1#A3.Ex31 "C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.2](https://arxiv.org/html/2512.14991v1#A3.Ex32 "C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the facts above, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |V¯hk​(x1)−V¯hk​(x2)|≤c˘h1​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖,\displaystyle|\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})|\leq\breve{c}^{1}\_{h}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})\|x\_{1}-x\_{2}\|, |  | (C.13) |

where c˘h1\breve{c}^{1}\_{h} depends only on Ch,C~h,m,DC\_{h},\widetilde{C}\_{h},m,D.

Case (2) ‖x1‖>ρ,‖x2‖≤ρ\|x\_{1}\|>\rho,\|x\_{2}\|\leq\rho. In this case,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |V¯hk​(x1)−V¯hk​(x2)|\displaystyle\Big|\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})\Big| | =\displaystyle= | |V¯hk​(ρ‖x1‖​x1)−V¯hk​(x2)+Ch​(1+‖x1‖m+ρm)​(‖x1‖−ρ)|\displaystyle\Big|\overline{V}\_{h}^{k}\Big(\frac{\rho}{\|x\_{1}\|}x\_{1}\Big)-\overline{V}\_{h}^{k}(x\_{2})+C\_{h}(1+\|x\_{1}\|^{m}+\rho^{m})(\|x\_{1}\|-\rho)\Big| |  | (C.14) |
|  |  | ≤\displaystyle\leq | c˘h3​(1+2​ρm)​‖ρ‖x1‖​x1−x2‖+Ch​(1+‖x1‖m+ρm)​(‖x1‖−ρ)\displaystyle\breve{c}^{3}\_{h}(1+2\rho^{m})\Big\|\frac{\rho}{\|x\_{1}\|}x\_{1}-x\_{2}\Big\|+C\_{h}(1+\|x\_{1}\|^{m}+\rho^{m})(\|x\_{1}\|-\rho) |  |
|  |  | ≤\displaystyle\leq | c˘h4​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖,\displaystyle\breve{c}^{4}\_{h}\Big(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m}\Big)\|x\_{1}-x\_{2}\|, |  |

where the first inequality holds due to ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) , ([5.12](https://arxiv.org/html/2512.14991v1#S5.E12 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.13](https://arxiv.org/html/2512.14991v1#A3.E13 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")); the second inequality holds due to ‖ρ‖x1‖​x1−x2‖≤‖x1−x2‖\|\frac{\rho}{\|x\_{1}\|}x\_{1}-x\_{2}\|\leq\|x\_{1}-x\_{2}\| and ‖x1‖−ρ≤‖x1−x2‖\|x\_{1}\|-\rho\leq\|x\_{1}-x\_{2}\| ; and finally, the third inequality holds since ρm≤‖x1‖m\rho^{m}\leq\|x\_{1}\|^{m}. Note that c˘h4\breve{c}^{4}\_{h} depends only on Ch,C~h,m,DC\_{h},\widetilde{C}\_{h},m,D.

Case (3) ‖x1‖>ρ,‖x2‖>ρ\|x\_{1}\|>\rho,\|x\_{2}\|>\rho. In this case,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |V¯hk​(x1)−V¯hk​(x2)|\displaystyle\Big|\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})\Big| | =\displaystyle= | |V¯hk(ρ‖x1‖x1)−V¯hk(ρ‖x2‖x2)+Ch(1+ρm)(∥x1∥−∥x2∥)\displaystyle\Big|\overline{V}\_{h}^{k}\Big(\frac{\rho}{\|x\_{1}\|}x\_{1}\Big)-\overline{V}\_{h}^{k}\Big(\frac{\rho}{\|x\_{2}\|}x\_{2}\Big)+C\_{h}(1+\rho^{m})(\|x\_{1}\|-\|x\_{2}\|) |  | (C.15) |
|  |  |  | +Ch∥x1∥m(∥x1∥−ρ)−Ch∥x2∥m(∥x2∥−ρ)|\displaystyle+C\_{h}\|x\_{1}\|^{m}(\|x\_{1}\|-\rho)-C\_{h}\|x\_{2}\|^{m}(\|x\_{2}\|-\rho)\Big| |  |
|  |  | ≤\displaystyle\leq | |V¯hk​(ρ‖x1‖​x1)−V¯hk​(ρ‖x2‖​x2)|+|Ch​(1+ρm)​(‖x1‖−‖x2‖)|\displaystyle\Big|\overline{V}\_{h}^{k}\Big(\frac{\rho}{\|x\_{1}\|}x\_{1}\Big)-\overline{V}\_{h}^{k}\Big(\frac{\rho}{\|x\_{2}\|}x\_{2}\Big)\Big|+\Big|C\_{h}(1+\rho^{m})(\|x\_{1}\|-\|x\_{2}\|)\Big| |  |
|  |  |  | +|Ch​‖x1‖m​(‖x1‖−ρ)−Ch​‖x2‖m​(‖x2‖−ρ)‖\displaystyle+\Big|C\_{h}\|x\_{1}\|^{m}(\|x\_{1}\|-\rho)-C\_{h}\|x\_{2}\|^{m}(\|x\_{2}\|-\rho)\Big\| |  |
|  |  | ≤\displaystyle\leq | c˘h3​(1+2​ρm)​‖ρ‖x1‖​x1−ρ‖x2‖​x2​‖+Ch​(1+ρm)|​‖x1‖−‖x2‖|\displaystyle\breve{c}^{3}\_{h}(1+2\rho^{m})\Big\|\frac{\rho}{\|x\_{1}\|}x\_{1}-\frac{\rho}{\|x\_{2}\|}x\_{2}\Big\|+C\_{h}(1+\rho^{m})\Big|\|x\_{1}\|-\|x\_{2}\|\Big| |  |
|  |  |  | +Ch​|‖x1‖m+1−‖x2‖m+1​|+ρ​Ch|​‖x1‖m−‖x2‖m|\displaystyle+C\_{h}\Big|\|x\_{1}\|^{m+1}-\|x\_{2}\|^{m+1}\Big|+\rho C\_{h}\Big|\|x\_{1}\|^{m}-\|x\_{2}\|^{m}\Big| |  |
|  |  | ≤\displaystyle\leq | c˘h5​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖,\displaystyle\breve{c}^{5}\_{h}\Big(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m}\Big)\|x\_{1}-x\_{2}\|, |  |

where the second inequality holds due to ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([5.12](https://arxiv.org/html/2512.14991v1#S5.E12 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.13](https://arxiv.org/html/2512.14991v1#A3.E13 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). In addition, the third inequality holds due to the facts that |am−bm|≤|a−b|​(a+b)m−1|a^{m}-b^{m}|\leq|a-b|(a+b)^{m-1} for a,b≥0a,b\geq 0 and ‖ρ‖x1‖​x1−ρ‖x2‖​x2‖≤‖x1−x2‖\|\frac{\rho}{\|x\_{1}\|}x\_{1}-\frac{\rho}{\|x\_{2}\|}x\_{2}\|\leq\|x\_{1}-x\_{2}\|. Also, the fourth inequality holds since ρm≤‖x1‖m+‖x2‖m\rho^{m}\leq\|x\_{1}\|^{m}+\|x\_{2}\|^{m}. c˘h5\breve{c}^{5}\_{h} depends only on Ch,C~h,m,DC\_{h},\widetilde{C}\_{h},m,D.

Finally, let C^h=max⁡{c˘h3,c˘h4,c˘h5}\widehat{C}\_{h}=\max\{\breve{c}^{3}\_{h},\breve{c}^{4}\_{h},\breve{c}^{5}\_{h}\}, combine ([C.13](https://arxiv.org/html/2512.14991v1#A3.E13 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.14](https://arxiv.org/html/2512.14991v1#A3.E14 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.15](https://arxiv.org/html/2512.14991v1#A3.E15 "In C.2 Proof of Theorem 5.3 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we conclude that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |V¯hk​(x1)−V¯hk​(x2)|≤C^h​(1+‖x1‖m+‖x2‖m)​‖x1−x2‖.\displaystyle|\overline{V}\_{h}^{k}(x\_{1})-\overline{V}\_{h}^{k}(x\_{2})|\leq\widehat{C}\_{h}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})\|x\_{1}-x\_{2}\|. |  | (C.16) |

∎

### C.3 Proof of Theorem [5.5](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem5 "Theorem 5.5. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

Combine Theorem [4.5](https://arxiv.org/html/2512.14991v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), Proposition [C.1](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem1 "Proposition C.1. ‣ C.1 Proof of Theorem 5.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), Corollary [5.4](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem4 "Corollary 5.4. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), and the fact that
C^maxC¯max>1\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}>1, we have the following result. With probability at least 1−3​δ1-3\delta, it holds that ∀(h,k)∈[H]×[K]\forall(h,k)\in[H]\times[K], ∀B∈𝒫hk\forall B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and ∀(x,a)∈B\forall(x,a)\in B:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^hk​(B)−R¯h​(x,a)≤C^maxC¯max​(R-UCBhk​(B)+R-BIAS​(B));\displaystyle\widehat{R}\_{h}^{k}(B)-\bar{R}\_{h}(x,a)\leq\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{h}^{k}(B)+\mbox{\rm R-BIAS}(B)\Big); |  | (C.17) |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 𝔼X∼T¯hk(⋅|B)​[V¯h+1k​(X)]−𝔼X∼Th(⋅|x,a)​[V¯h+1k​(X)]\displaystyle\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[\overline{V}\_{h+1}^{k}(X)] |  | (C.18) |
|  |  | ≤\displaystyle\leq | C^maxC¯max(T-UCBhk(B)+LV(δ,∥x~(oB)∥)T-BIAS(B)).\displaystyle\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm T-UCB}\_{h}^{k}(B)+L\_{V}(\delta,\|\tilde{x}(^{o}B)\|)\mbox{\rm T-BIAS}(B)\Big). |  |

Also, we have the following decomposition:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | 𝔼X∼T¯hk(⋅|B)​[V¯h+1k​(X)]−𝔼X∼Th(⋅|x,a)​[Vh+1∗​(X)]\displaystyle\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(X)] |  |
|  |  | =\displaystyle= | 𝔼X∼T¯hk(⋅|B)​[V¯h+1k​(X)]−𝔼X∼Th(⋅|x,a)​[V¯h+1k​(X)]+𝔼X∼Th(⋅|x,a)​[V¯h+1k​(X)]−𝔼X∼Th(⋅|x,a)​[Vh+1∗​(X)].\displaystyle\mathbb{E}\_{X\sim\bar{T}\_{h}^{k}(\cdot|B)}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[\overline{V}\_{h+1}^{k}(X)]+\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{X\sim{T}\_{h}(\cdot|x,a)}[V\_{h+1}^{\*}(X)]. |  |

Combining the results in ([C.17](https://arxiv.org/html/2512.14991v1#A3.E17 "In C.3 Proof of Theorem 5.5 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.18](https://arxiv.org/html/2512.14991v1#A3.E18 "In C.3 Proof of Theorem 5.5 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.3](https://arxiv.org/html/2512.14991v1#A3.Ex43 "C.3 Proof of Theorem 5.5 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), it holds with probability at least 1−3​δ1-3\delta that, ∀(h,k)∈[H]×[K]\forall(h,k)\in[H]\times[K], ∀B∈𝒫hk\forall B\in\mathcal{P}\_{h}^{k} with nhk​(B)>0n\_{h}^{k}(B)>0, and ∀(x,a)∈B\forall(x,a)\in B:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Q¯hk​(B)−Qh∗​(x,a)\displaystyle\overline{Q}\_{h}^{k}(B)-Q\_{h}^{\*}(x,a) | ≤\displaystyle\leq | 2​C^maxC¯max​(R-UCBhk​(B)+T-UCBhk​(B)+BIAS​(B))\displaystyle 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{h}^{k}(B)+\mbox{\rm T-UCB}\_{h}^{k}(B)+{\rm BIAS}(B)\Big) |  |
|  |  |  | +𝔼X∼Th(⋅|x,a)​[V¯h+1k​(X)]−𝔼X∼Th(⋅|x,a)​[Vh+1∗​(X)],h<H,\displaystyle+\mathbb{E}\_{X\sim{T}\_{h(\cdot|x,a)}}[\overline{V}\_{h+1}^{k}(X)]-\mathbb{E}\_{X\sim{T}\_{h(\cdot|x,a)}}[V\_{h+1}^{\*}(X)],\,\,h<H, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Q¯Hk​(B)−QH∗​(x,a)\displaystyle\overline{Q}\_{H}^{k}(B)-Q\_{H}^{\*}(x,a) | ≤\displaystyle\leq | 2​C^maxC¯max​(R-UCBHk​(B)+R-BIAS​(B)).\displaystyle 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{H}^{k}(B)+\mbox{\rm R-BIAS}(B)\Big). |  |

∎

### C.4 Proof of Proposition [5.6](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem6 "Proposition 5.6. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

Since nhk​(B)=0n\_{h}^{k}(B)=0, we must have B∈𝒫h0B\in\mathcal{P}\_{h}^{0}, diam​(B)=D{\rm diam}(B)=D, Q¯hk​(B)=Q¯h0​(B)\overline{Q}\_{h}^{k}(B)=\overline{Q}\_{h}^{0}(B) and Bo=B{}^{o}B=B. Hence

|  |  |  |
| --- | --- | --- |
|  | Q¯hk(B)−Qh∗(x,a)≤Q¯h0(B)+|Vh∗(x)|≤2C~hD(1+(∥x~(oB)∥+D)m+1)diam(B),\overline{Q}\_{h}^{k}(B)-Q\_{h}^{\*}(x,a)\leq\overline{Q}\_{h}^{0}(B)+|V\_{h}^{\*}(x)|\leq 2\frac{\widetilde{C}\_{h}}{D}(1+(\|\tilde{x}(^{o}B)\|+D)^{m+1}){\rm diam}(B), |  |

where the last inequality holds by ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

∎

### C.5 Proof of Proposition [5.7](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem7 "Proposition 5.7. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

Note that conditioned on Xhk∈𝒮1X\_{h}^{k}\in\mathcal{S}\_{1}, we have Bhk∈𝒫hk−1B\_{h}^{k}\in\mathcal{P}\_{h}^{k-1}. We then divide the proof into two cases: (1) k>1k>1 and (2) k=1k=1.

Case (1). For k>1k>1, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | V¯hk−1​(Xhk)\displaystyle\overline{V}\_{h}^{k-1}(X\_{h}^{k}) | ≤\displaystyle\leq | V~hk−1(Γ𝒮(Bhk))+Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)\displaystyle\widetilde{V}\_{h}^{k-1}(\Gamma\_{\mathcal{S}}(B\_{h}^{k}))+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}) |  | (C.20) |
|  |  | =\displaystyle= | maxB∈Phk−1:Γ𝒮​(Bhk)⊂Γ𝒮​(B)Q¯hk−1(B)+Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)\displaystyle\max\_{B\in P\_{h}^{k-1}:\Gamma\_{\mathcal{S}}(B\_{h}^{k})\subset\Gamma\_{\mathcal{S}}(B)}\overline{Q}\_{h}^{k-1}(B)+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}) |  |
|  |  | =\displaystyle= | Q¯hk−1(Bhk)+Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk).\displaystyle\overline{Q}\_{h}^{k-1}(B\_{h}^{k})+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}). |  |

The first inequality holds by the definition of V¯hk−1​(Xhk)\overline{V}\_{h}^{k-1}(X\_{h}^{k}) in ([5.8](https://arxiv.org/html/2512.14991v1#S5.E8 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([5.12](https://arxiv.org/html/2512.14991v1#S5.E12 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and the first equality holds due to the greedy selection rule (line [2](https://arxiv.org/html/2512.14991v1#alg2.l2 "In Algorithm 2 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) in Algorithm [1](https://arxiv.org/html/2512.14991v1#alg1 "Algorithm 1 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

Case (2).
For k=1k=1, we have

|  |  |  |
| --- | --- | --- |
|  | V¯h0(Xh1)≤Q¯h0(Bh1)+Ch(1+2(∥x~(oBh1)∥+D)m)diam(Bh1).\displaystyle\overline{V}\_{h}^{0}(X\_{h}^{1})\leq\overline{Q}\_{h}^{0}(B\_{h}^{1})+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{1})\|+D)^{m}){\rm diam}(B\_{h}^{1}). |  |

This inequality holds due to the initial estimators we set in ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the fact that Bh1o=Bh1{}^{o}B\_{h}^{1}=B\_{h}^{1} since Bh1∈𝒫h0B\_{h}^{1}\in\mathcal{P}\_{h}^{0}.
∎

### C.6 Proof of Theorem [5.9](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem9 "Theorem 5.9. ‣ 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

By the definition in ([5.23](https://arxiv.org/html/2512.14991v1#S5.E23 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")),

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Gaph​(Bhk)\displaystyle{\rm Gap}\_{h}(B\_{h}^{k}) | ≤\displaystyle\leq | G~​aph​(Xhk,Ahk)\displaystyle{\rm\widetilde{G}ap}\_{h}(X\_{h}^{k},A\_{h}^{k}) |  | (C.21) |
|  |  | ≤\displaystyle\leq | V¯hk−1​(Xhk)−Qh∗​(Xhk,Ahk)\displaystyle\overline{V}\_{h}^{k-1}(X\_{h}^{k})-Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k}) |  |
|  |  | ≤\displaystyle\leq | Q¯hk−1(Bhk)−Qh∗(Xhk,Ahk)+Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)\displaystyle\overline{Q}\_{h}^{k-1}(B\_{h}^{k})-Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k})+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}) |  |
|  |  | ≤\displaystyle\leq | Ghk​(Bhk)+fh+1k−1​(Xhk,Ahk):=ϕ1+ϕ2,\displaystyle G\_{h}^{k}(B\_{h}^{k})+f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k}):=\phi\_{1}+\phi\_{2}, |  |

in which the second inequality holds due to Theorem [5.2](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem2 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") , the third inequality holds by ([5.20](https://arxiv.org/html/2512.14991v1#S5.E20 "In Proposition 5.7. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). and the fourth inequality holds due to ([5.5](https://arxiv.org/html/2512.14991v1#S5.Ex14 "Theorem 5.5. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([5.19](https://arxiv.org/html/2512.14991v1#S5.E19 "In Proposition 5.6. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). In the last line, we use the simplified notations ϕ1:=Ghk​(Bhk)\phi\_{1}:=G\_{h}^{k}(B\_{h}^{k}) and ϕ2:=fh+1k−1​(Xhk,Ahk)\phi\_{2}:=f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k}).

Let ϕ:=V¯hk−1​(Xhk)−Qh∗​(Xhk,Ahk)\phi:=\overline{V}\_{h}^{k-1}(X\_{h}^{k})-Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k}). We claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ≤CLIP​(ϕ1|Gaph​(Bhk)H+1)+(1+1H)​ϕ2.\displaystyle\phi\leq{\rm CLIP}\Bigg(\phi\_{1}\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+\Big(1+\frac{1}{H}\Big)\phi\_{2}. |  | (C.22) |

When ϕ1≥Gaph​(Bhk)H+1\phi\_{1}\geq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}, ([C.22](https://arxiv.org/html/2512.14991v1#A3.E22 "In C.6 Proof of Theorem 5.9 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) is trivial.
So we only need to prove the claim when
ϕ1<Gaph​(Bhk)H+1\phi\_{1}<\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}. In this case,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gaph​(Bhk)≤ϕ1+ϕ2≤Gaph​(Bhk)H+1+ϕ2.\displaystyle{\rm Gap}\_{h}(B\_{h}^{k})\leq\phi\_{1}+\phi\_{2}\leq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}+\phi\_{2}. |  | (C.23) |

Rearranging terms in ([C.23](https://arxiv.org/html/2512.14991v1#A3.E23 "In C.6 Proof of Theorem 5.9 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have
Gaph​(Bhk)≤H+1H​ϕ2{\rm Gap}\_{h}(B\_{h}^{k})\leq\frac{H+1}{H}\phi\_{2}, and hence
ϕ1+ϕ2≤1H+1​H+1H​ϕ2+ϕ2=(1+1H)​ϕ2.\phi\_{1}+\phi\_{2}\leq\frac{1}{H+1}\frac{H+1}{H}\phi\_{2}+\phi\_{2}=(1+\frac{1}{H})\phi\_{2}.
This implies that

|  |  |  |
| --- | --- | --- |
|  | ϕ≤ϕ1+ϕ2≤CLIP​(ϕ1|Gaph​(Bhk)H+1)+(1+1H)​ϕ2.\phi\leq\phi\_{1}+\phi\_{2}\leq{\rm CLIP}\Bigg(\phi\_{1}\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+\Big(1+\frac{1}{H}\Big)\phi\_{2}. |  |

With the inequality ([C.22](https://arxiv.org/html/2512.14991v1#A3.E22 "In C.6 Proof of Theorem 5.9 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Δh(k)\displaystyle\Delta\_{h}^{(k)} | =\displaystyle= | V¯hk−1​(Xhk)−Qh∗​(Xhk,Ahk)+Qh∗​(Xhk,Ahk)−Vhπ~k​(Xhk)\displaystyle\overline{V}\_{h}^{k-1}(X\_{h}^{k})-Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k})+Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k})-V\_{h}^{\tilde{\pi}^{k}}(X\_{h}^{k}) |  | (C.24) |
|  |  | ≤\displaystyle\leq | CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+(1+1H)​fh+1k−1​(Xhk,Ahk)+Qh∗​(Xhk,Ahk)−Vhπ~k​(Xhk),\displaystyle{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+\Big(1+\frac{1}{H}\Big)f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k})+Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k})-V\_{h}^{\tilde{\pi}^{k}}(X\_{h}^{k}), |  |

∎

### C.7 Proof of Proposition [5.10](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem10 "Proposition 5.10. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

Let 𝒢k=σ​((Xhk′,Ahk′,rhk′)h∈[H],k′≤k)\mathcal{G}\_{k}=\sigma((X\_{h}^{k^{\prime}},A\_{h}^{k^{\prime}},r\_{h}^{k^{\prime}})\_{h\in[H]},k^{\prime}\leq k) be the information generated up to episode kk with 𝒢0\mathcal{G}\_{0} being the null information. Then we have 𝔼​[Ik|𝒢k−1]≥1−Mpρp\mathbb{E}[I\_{k}|\mathcal{G}\_{k-1}]\geq 1-\frac{M\_{p}}{\rho^{p}} given ([5.33](https://arxiv.org/html/2512.14991v1#S5.E33 "In 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Let Y0=0Y\_{0}=0 and Yk=∑i=1k(Ik−𝔼​[Ik|𝒢k−1])Y\_{k}=\sum\_{i=1}^{k}(I\_{k}-\mathbb{E}[I\_{k}|\mathcal{G}\_{k-1}]) for k>1k>1.
Then it is clear that {Yk}k=0,1,…,K\{Y\_{k}\}\_{k=0,1,...,K} is a martingale and we have |Yk−Yk−1|≤1|Y\_{k}-Y\_{k-1}|\leq 1. By Azuma-Hoeffding inequality, for any ϵ>0\epsilon>0 we have

|  |  |  |
| --- | --- | --- |
|  | ℙ​(YK−Y0≤−ϵ)≤exp⁡(−ϵ22​K).\displaystyle\mathbb{P}(Y\_{K}-Y\_{0}\leq-\epsilon)\leq\exp\left(-\frac{\epsilon^{2}}{2K}\right). |  |

By the fact that YK=K0−K​𝔼​[Ik|𝒢k−1]≤K0−K​(1−Mpρp)Y\_{K}=K\_{0}-K\mathbb{E}[I\_{k}|\mathcal{G}\_{k-1}]\leq K\_{0}-K\left(1-\frac{M\_{p}}{\rho^{p}}\right), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(K0−K​(1−Mpρp)≥−ϵ)≥ℙ​(YK−Y0≥−ϵ)≥1−exp⁡(−ϵ22​K).\mathbb{P}\left(K\_{0}-K\left(1-\frac{M\_{p}}{\rho^{p}}\right)\geq-\epsilon\right)\geq\mathbb{P}(Y\_{K}-Y\_{0}\geq-\epsilon)\geq 1-\exp\left(-\frac{\epsilon^{2}}{2K}\right). |  | (C.25) |

Let δ=exp⁡(−ϵ22​K)\delta=\exp(-\frac{\epsilon^{2}}{2K}), then we have ([5.10](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem10 "Proposition 5.10. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) hold with probability at least 1−δ1-\delta.
∎

### C.8 Proof of Theorem [5.11](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem11 "Theorem 5.11. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

Denote sets J1J\_{1} and J2J\_{2} as the following:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J1\displaystyle J\_{1} | :=\displaystyle:= | {k∈[K]:‖X1k‖>ρ},\displaystyle\left\{k\in[K]:\|X\_{1}^{k}\|>\rho\right\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J2\displaystyle J\_{2} | :=\displaystyle:= | {k∈[K]:‖X1k‖≤ρ,suph=2,…,H‖Xhk‖>ρ}.\displaystyle\left\{k\in[K]:\|X\_{1}^{k}\|\leq\rho,\sup\_{h=2,...,H}\|X\_{h}^{k}\|>\rho\right\}. |  |

Then it is clear that J1∪J2=[K]\JρKJ\_{1}\cup J\_{2}=[K]\backslash J\_{\rho}^{K} and J1∩J2=∅J\_{1}\cap J\_{2}=\emptyset. Further denote Ki=|Ji|K\_{i}=|J\_{i}| for i=1,2i=1,2, then K−K0=K1+K2K-K\_{0}=K\_{1}+K\_{2}. With these notation, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∑k∈J\JρK|V1π​(X1k)|\displaystyle\sum\_{k\in J\backslash J\_{\rho}^{K}}|V\_{1}^{\pi}(X\_{1}^{k})| | =\displaystyle= | ∑k∈J1|V1π​(X1k)|+∑k∈J2|V1π​(X1k)|\displaystyle\sum\_{k\in J\_{1}}|V\_{1}^{\pi}(X\_{1}^{k})|+\sum\_{k\in J\_{2}}|V\_{1}^{\pi}(X\_{1}^{k})| |  | (C.26) |
|  |  | =\displaystyle= | ∑k=1K|V1π​(X1k)|​𝕀{‖X1k‖>ρ}+∑k∈J2|V1π​(X1k)|\displaystyle\sum\_{k=1}^{K}|V\_{1}^{\pi}(X\_{1}^{k})|\mathbb{I}\_{\{\|X\_{1}^{k}\|>\rho\}}+\sum\_{k\in J\_{2}}|V\_{1}^{\pi}(X\_{1}^{k})| |  |
|  |  | ≤\displaystyle\leq | ∑k=1KC~1​(‖X1k‖m+1+1)​𝕀{‖X1k‖>ρ}+C~1​(K−K0)​(ρm+1+1),\displaystyle\sum\_{k=1}^{K}\widetilde{C}\_{1}\Big(\|X\_{1}^{k}\|^{m+1}+1\Big)\mathbb{I}\_{\{\|X\_{1}^{k}\|>\rho\}}+\widetilde{C}\_{1}(K-K\_{0})\Big(\rho^{m+1}+1\Big), |  |

where the inequality holds due to Proposition [2.5](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

Let Y:=∑k=1KC~1​(‖X1k‖m+1+1)​𝕀{‖X1k‖>ρ}Y:=\sum\_{k=1}^{K}\widetilde{C}\_{1}\Big(\|X\_{1}^{k}\|^{m+1}+1\Big)\mathbb{I}\_{\{\|X\_{1}^{k}\|>\rho\}}, then

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝔼​[Y]\displaystyle\mathbb{E}[Y] | ≤\displaystyle\leq | K​C~1​(ℙ​(‖ξ‖>ρ)+𝔼ξ∼Ξ​[‖ξ‖m+1​𝕀{‖ξ‖>ρ}])\displaystyle K\widetilde{C}\_{1}\Big(\mathbb{P}(\|\xi\|>\rho)+\mathbb{E}\_{\xi\sim\Xi}\big[\|\xi\|^{m+1}\mathbb{I}\_{\{\|\xi\|>\rho\}}\big]\Big) |  | (C.27) |
|  |  | ≤\displaystyle\leq | K​C~1​(𝔼ξ∼Ξ​[‖ξ‖p]ρp+(𝔼ξ∼Ξ​[‖ξ‖p])m+1p​(ℙ​(‖ξ‖>ρ))1−m+1p)\displaystyle K\widetilde{C}\_{1}\Big(\frac{\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]}{\rho^{p}}+\big(\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]\big)^{\frac{m+1}{p}}(\mathbb{P}(\|\xi\|>\rho))^{1-\frac{m+1}{p}}\Big) |  |
|  |  | ≤\displaystyle\leq | K​C~1​(𝔼ξ∼Ξ​[‖ξ‖p]ρp+𝔼ξ∼Ξ​[‖ξ‖p]ρp−(m+1))=δ​K​κm+1​(δ,ρ),\displaystyle K\widetilde{C}\_{1}\Big(\frac{\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]}{\rho^{p}}+\frac{\mathbb{E}\_{\xi\sim\Xi}[\|\xi\|^{p}]}{\rho^{p-(m+1)}}\Big)=\delta K\kappa\_{m+1}(\delta,\rho), |  |

where the second inequality holds by applying Hölder’s inequality. By this inequality,
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Y≥K​κm+1​(δ,ρ))≤ℙ​(Y≥𝔼​[Y]δ)≤δ,\displaystyle\mathbb{P}\Big(Y\geq K\kappa\_{m+1}(\delta,\rho)\Big)\leq\mathbb{P}\left(Y\geq\frac{\mathbb{E}[Y]}{\delta}\right)\leq\delta, |  | (C.28) |

where the last inequality holds by Markov inequality.
Putting ([C.26](https://arxiv.org/html/2512.14991v1#A3.E26 "In C.8 Proof of Theorem 5.11 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.28](https://arxiv.org/html/2512.14991v1#A3.E28 "In C.8 Proof of Theorem 5.11 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) together,
we have ([5.34](https://arxiv.org/html/2512.14991v1#S5.E34 "In Theorem 5.11. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) holds with probability at least 1−δ1-\delta.
∎

### C.9 Lemma [C.2](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem2 "Lemma C.2 (Theorem F.1 in [Sinclair et al., 2023]). ‣ C.9 Lemma C.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

We adapt Theorem F.1 from [Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)], stated below with minor modifications to suit our setting.

###### Lemma C.2 (Theorem F.1 in [Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)]).

It holds that

|  |  |  |
| --- | --- | --- |
|  | (1+1H)​fh+1k−1​(Xhk,Ahk)+Qh∗​(Xhk,Ahk)−Vhπ~k​(Xhk)≤(1+1H)​(Δh+1(k)+ξh+1k),\Big(1+\frac{1}{H}\Big)f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k})+Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k})-V\_{h}^{\tilde{\pi}^{k}}(X\_{h}^{k})\leq\Big(1+\frac{1}{H}\Big)(\Delta\_{h+1}^{(k)}+\xi\_{h+1}^{k}), |  |

in which for h<Hh<H

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξh+1k\displaystyle\xi\_{h+1}^{k} | :=\displaystyle:= | 𝔼Y∼Th(⋅|Xhk,Ahk)​[V¯h+1k−1​(Y)]−𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1π~k​(Y)]−(V¯h+1k−1​(Xh+1k)−Vh+1π~k​(Xh+1k))\displaystyle\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[\overline{V}\_{h+1}^{k-1}(Y)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\tilde{\pi}^{k}}(Y)]-(\overline{V}\_{h+1}^{k-1}(X\_{h+1}^{k})-V\_{h+1}^{\tilde{\pi}^{k}}(X\_{h+1}^{k})) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ζh+1k\displaystyle\zeta\_{h+1}^{k} | :=\displaystyle:= | R¯h​(Xhk,Ahk)−𝔼a∼πhk​(Xhk)​[R¯h​(Xhk,a)]\displaystyle\bar{R}\_{h}(X\_{h}^{k},A\_{h}^{k})-\mathbb{E}\_{a\sim\pi\_{h}^{k}(X\_{h}^{k})}[\bar{R}\_{h}(X\_{h}^{k},a)] |  |
|  |  |  | +𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1π~k​(Y)]−𝔼a∼πhk(Xhk),Y′∼Th(⋅|Xhk,a)​[Vh+1π~k​(Y′)],\displaystyle+\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\tilde{\pi}^{k}}(Y)]-\mathbb{E}\_{a\sim\pi\_{h}^{k}(X\_{h}^{k}),Y^{{}^{\prime}}\sim{T}\_{h}(\cdot|X\_{h}^{k},a)}[V\_{h+1}^{\tilde{\pi}^{k}}(Y^{{}^{\prime}})], |  |

ξH+1k:=0\xi\_{H+1}^{k}:=0 and ζH+1k:=R¯H​(XHk,AHk)−𝔼a∼πHk​(XHk)​[R¯H​(XHk,a)]\zeta\_{H+1}^{k}:=\bar{R}\_{H}(X\_{H}^{k},A\_{H}^{k})-\mathbb{E}\_{a\sim\pi\_{H}^{k}(X\_{H}^{k})}[\bar{R}\_{H}(X\_{H}^{k},a)]. In addition, Δh+1(k)\Delta\_{h+1}^{(k)} is defined in ([5.21](https://arxiv.org/html/2512.14991v1#S5.E21 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) for h<Hh<H, ΔH+1(k):=0\Delta\_{H+1}^{(k)}:=0, and fh+1k−1​(Xhk,Ahk)f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k}) is defined in ([5.25](https://arxiv.org/html/2512.14991v1#S5.E25 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Proof.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | (1+1H)​fh+1k−1​(Xhk,Ahk)+Qh∗​(Xhk,Ahk)−Vhπ~k​(Xhk)\displaystyle\Big(1+\frac{1}{H}\Big)f\_{h+1}^{k-1}(X\_{h}^{k},A\_{h}^{k})+Q\_{h}^{\*}(X\_{h}^{k},A\_{h}^{k})-V\_{h}^{\tilde{\pi}^{k}}(X\_{h}^{k}) |  |
|  |  | =\displaystyle= | (1+1H)​(𝔼Y∼Th(⋅|Xhk,Ahk)​[V¯h+1k−1​(Y)]−𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1∗​(Y)])+R¯h​(Xhk,Ahk)\displaystyle\Big(1+\frac{1}{H}\Big)\Big(\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[\overline{V}\_{h+1}^{k-1}(Y)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\*}(Y)]\Big)+\bar{R}\_{h}(X\_{h}^{k},A\_{h}^{k}) |  |
|  |  |  | +𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1∗​(Y)]−𝔼a∼πhk​(Xhk)​[R¯h​(Xhk,a)]−𝔼a∼πhk(Xhk),Y′∼Th(⋅|Xhk,a)​[Vh+1π~k​(Y′)]\displaystyle+\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\*}(Y)]-\mathbb{E}\_{a\sim\pi\_{h}^{k}(X\_{h}^{k})}[\bar{R}\_{h}(X\_{h}^{k},a)]-\mathbb{E}\_{a\sim\pi\_{h}^{k}(X\_{h}^{k}),Y^{{}^{\prime}}\sim{T}\_{h}(\cdot|X\_{h}^{k},a)}[V\_{h+1}^{\tilde{\pi}^{k}}(Y^{{}^{\prime}})] |  |
|  |  | ≤\displaystyle\leq | (1+1H)​(𝔼Y∼Th(⋅|Xhk,Ahk)​[V¯h+1k−1​(Y)]−𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1∗​(Y)])\displaystyle\Big(1+\frac{1}{H}\Big)\Big(\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[\overline{V}\_{h+1}^{k-1}(Y)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\*}(Y)]\Big) |  |
|  |  |  | +(1+1H)​(𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1∗​(Y)]−𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1π~k​(Y)])\displaystyle+\Big(1+\frac{1}{H}\Big)\Big(\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\*}(Y)]-\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\tilde{\pi}^{k}}(Y)]\Big) |  |
|  |  |  | +R¯h​(Xhk,Ahk)−𝔼a∼πhk​(Xhk)​[R¯h​(Xhk,a)]\displaystyle+\bar{R}\_{h}(X\_{h}^{k},A\_{h}^{k})-\mathbb{E}\_{a\sim\pi\_{h}^{k}(X\_{h}^{k})}[\bar{R}\_{h}(X\_{h}^{k},a)] |  |
|  |  |  | +𝔼Y∼Th(⋅|Xhk,Ahk)​[Vh+1π~k​(Y)]−𝔼a∼πhk(Xhk),Y′∼Th(⋅|Xhk,a)​[Vh+1π~k​(Y′)]\displaystyle+\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[V\_{h+1}^{\tilde{\pi}^{k}}(Y)]-\mathbb{E}\_{a\sim\pi\_{h}^{k}(X\_{h}^{k}),Y^{{}^{\prime}}\sim{T}\_{h}(\cdot|X\_{h}^{k},a)}[V\_{h+1}^{\tilde{\pi}^{k}}(Y^{{}^{\prime}})] |  |
|  |  | =\displaystyle= | (1+1H)​(Δh+1(k)+ξh+1k)+ζh+1k,\displaystyle\Big(1+\frac{1}{H}\Big)(\Delta\_{h+1}^{(k)}+\xi\_{h+1}^{k})+\zeta\_{h+1}^{k}, |  |

where the first inequality holds due to ([2.1](https://arxiv.org/html/2512.14991v1#S2.Ex5 "Bellman equation for generic policy. ‣ 2.1 Value function, Bellman equations and evaluation criterion ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
∎

### C.10 Proof of Theorem [5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

Before the proof of Theorem [5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we introduce several technical lemmas.

We first provide a high probability bound for the state process that holds simultaneously across all episodes. For convenience, we denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z:=suph∈[H],k∈[K]‖Xhk‖.\displaystyle Z:=\sup\_{h\in[H],k\in[K]}\|X\_{h}^{k}\|. |  | (C.29) |

###### Lemma C.3.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. We have:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Z≤(K​Mpδ)1p)≥1−δ.\displaystyle\mathbb{P}\Big(Z\leq\Big(\frac{KM\_{p}}{\delta}\Big)^{\frac{1}{p}}\Big)\geq 1-\delta. |  |

###### Proof.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℙ​(Z≤(K​MpK)1p)\displaystyle\mathbb{P}\Big(Z\leq\Big(\frac{KM\_{p}}{K}\Big)^{\frac{1}{p}}\Big) | ≥\displaystyle\geq | 1−∑k=1Kℙ​(suph∈[H]‖Xhk‖≥(K​Mpδ)1p)\displaystyle 1-\sum\_{k=1}^{K}\mathbb{P}\Big(\sup\_{h\in[H]}\|X\_{h}^{k}\|\geq\Big(\frac{KM\_{p}}{\delta}\Big)^{\frac{1}{p}}\Big) |  |
|  |  | ≥\displaystyle\geq | 1−K​MpK​Mpδ\displaystyle 1-K\frac{M\_{p}}{\frac{KM\_{p}}{\delta}} |  |
|  |  | =\displaystyle= | 1−δ,\displaystyle 1-\delta, |  |

where the first inequality holds by the union bound (namely, for a countable set of events E1,E2,…E\_{1},E\_{2},..., we have ℙ​(∩iEi)≥1−∑iℙ​(Ei∁)\mathbb{P}(\cap\_{i}E\_{i})\geq 1-\sum\_{i}\mathbb{P}(E\_{i}^{\complement})) and the second inequality holds due to Corollary [2.3](https://arxiv.org/html/2512.14991v1#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").
∎

Unlike the bounded state space setting in [Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)], the martingale difference term ξh+1k\xi\_{h+1}^{k} in our setting is unbounded. Therefore, we need a more general version of the martingale concentration inequality instead of the usual Azuma-Hoeffding inequality.

###### Lemma C.4.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. We have:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(∑h=1H∑k=1Kξh+1k≤2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ))≥1−5​δ,\displaystyle\mathbb{P}\Bigg(\sum\_{h=1}^{H}\sum\_{k=1}^{K}\xi\_{h+1}^{k}\leq 2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)}\Bigg)\geq 1-5\delta, |  |

where L~1\widetilde{L}\_{1} is defined in ([5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Proof.

With probability at least 1−3​δ1-3\delta, it holds that, for x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}}, h∈[H−1]h\in[H-1] and k>1k>1, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |V¯h+1k−1​(x)|\displaystyle|\overline{V}\_{h+1}^{k-1}(x)| | ≤\displaystyle\leq | max⁡{|Vh+1,k−1local​(x,S′)|,|Vh+1∗​(x)|}\displaystyle\max\{|V\_{h+1,k-1}^{\rm local}(x,S^{\prime})|,|V\_{h+1}^{\*}(x)|\} |  |
|  |  | ≤\displaystyle\leq | V~h+10​(S′)+Ch​(1+‖x‖m+‖x~​(S′)‖m)​(‖x‖+‖x~​(S′)‖)\displaystyle\widetilde{V}\_{h+1}^{0}(S^{\prime})+C\_{h}\Big(1+\|x\|^{m}+\|\tilde{x}(S^{\prime})\|^{m}\Big)(\|x\|+\|\tilde{x}(S^{\prime})\|) |  |
|  |  | ≤\displaystyle\leq | c˘1​‖x‖m+1+c˘2,\displaystyle\breve{c}\_{1}\|x\|^{m+1}+\breve{c}\_{2}, |  |

where S′=arg⁡minS∈Γ𝒮​(𝒫h+1k−1)⁡Vh+1,k−1local​(x,S)S^{\prime}=\operatorname\*{\arg\min}\_{S\in\Gamma\_{\mathcal{S}}(\mathcal{P}\_{h+1}^{k-1})}V\_{h+1,k-1}^{\rm local}(x,S), and c˘1,c˘2\breve{c}\_{1},\breve{c}\_{2} depend only on m,D,Cmax,C~maxm,D,C\_{\max},\widetilde{C}\_{\max}. The first inequality holds due to Theorem [5.2](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem2 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and the third line of ([5.12](https://arxiv.org/html/2512.14991v1#S5.E12 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). In addition, the second inequality holds due to ([5.1](https://arxiv.org/html/2512.14991v1#S5.Ex2 "Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the fact that V~h+1k−1​(S′)≤V~h+10​(S′)\widetilde{V}\_{h+1}^{k-1}(S^{\prime})\leq\widetilde{V}\_{h+1}^{0}(S^{\prime}) according to the second line of ([5.12](https://arxiv.org/html/2512.14991v1#S5.E12 "In Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and the fact that ‖x−x~​(S′)‖≤‖x‖+‖x~​(S′)‖\|x-\tilde{x}(S^{\prime})\|\leq\|x\|+\|\tilde{x}(S^{\prime})\|. Finally, the third inequality holds due to the fact that ‖x~​(S′)‖≤‖x‖+D\|\tilde{x}(S^{\prime})\|\leq\|x\|+D.

In addition, note that ([C.10](https://arxiv.org/html/2512.14991v1#A3.Ex82 "C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) also holds for k=1k=1, x∈ℝd𝒮x\in\mathbb{R}^{d\_{\mathcal{S}}}, and h∈[H−1]h\in[H-1].

Let ℱh,k=σ((Xhk′,Ahk′,rhk′),h′≤h,k′≤k)\mathcal{F}\_{h,k}=\sigma((X\_{h}^{k^{\prime}},A\_{h}^{k^{\prime}},r\_{h}^{k^{\prime}}),h^{\prime}\leq h,k^{\prime}\leq k). We next show that we can bound (ξh+1k)2(\xi\_{h+1}^{k})^{2} and 𝔼​[(ξh+1k)2|ℱh,k]\mathbb{E}[(\xi\_{h+1}^{k})^{2}|\mathcal{F}\_{h,k}] by polynomials of ZZ.

To proceed, we will often use the fact that for n,q∈ℕ+n,q\in\mathbb{N}\_{+}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∑i=1nai)q≤nq−1​∑i=1naiq\displaystyle(\sum\_{i=1}^{n}a\_{i})^{q}\leq n^{q-1}\sum\_{i=1}^{n}a\_{i}^{q} |  | (C.30) |

and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝔼X∼Th(⋅|Xhk,Ahk)​[‖X‖q]\displaystyle\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[\|X\|^{q}] | ≤\displaystyle\leq | (𝔼X∼Th(⋅|Xhk,Ahk)​[‖X‖2​q])12\displaystyle(\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[\|X\|^{2q}])^{\frac{1}{2}} |  | (C.31) |
|  |  | ≤\displaystyle\leq | C~​(q,d𝒮)​(‖μh​(Xhk,Ahk)‖q+‖Σh​(Xhk,Ahk)‖q2)\displaystyle\widetilde{C}(q,d\_{\mathcal{S}})(\|\mu\_{h}(X\_{h}^{k},A\_{h}^{k})\|^{q}+\|\Sigma\_{h}(X\_{h}^{k},A\_{h}^{k})\|^{\frac{q}{2}}) |  |
|  |  | ≤\displaystyle\leq | 2​C~​(q,d𝒮)​η​(Xhk)q,\displaystyle 2\widetilde{C}(q,d\_{\mathcal{S}})\eta(X\_{h}^{k})^{q}, |  |

where the second inequality holds due to Lemma [B.3](https://arxiv.org/html/2512.14991v1#A2.Thmtheorem3 "Lemma B.3. ‣ B.6 Proof of Theorem 4.4 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and the third inequality holds due to ([4.7](https://arxiv.org/html/2512.14991v1#S4.E7 "In 4.1 Concentration of the estimators for drift and volatility ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Then with probability at least 1−3​δ1-3\delta, the following inequality holds for h∈[H]h\in[H] and k∈[K]k\in[K]:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (ξh+1k)2\displaystyle(\xi\_{h+1}^{k})^{2} | ≤\displaystyle\leq | (𝔼X∼Th(⋅|Xhk,Ahk)[|V¯h+1k−1(X)|]+𝔼X∼Th(⋅|Xhk,Ahk)[|Vh+1π~k(X)|]\displaystyle\Big(\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[|\overline{V}\_{h+1}^{k-1}(X)|]+\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[|V\_{h+1}^{\tilde{\pi}^{k}}(X)|] |  | (C.32) |
|  |  |  | +|V¯h+1k−1(Xh+1k)|+|Vh+1π~k(Xh+1k)|)2\displaystyle+|\overline{V}\_{h+1}^{k-1}(X\_{h+1}^{k})|+|V\_{h+1}^{\tilde{\pi}^{k}}(X\_{h+1}^{k})|\Big)^{2} |  |
|  |  | ≤\displaystyle\leq | 4((𝔼X∼Th(⋅|Xhk,Ahk)[|V¯h+1k−1(X)|])2+(𝔼X∼Th(⋅|Xhk,Ahk)[|Vh+1π~k(X)|])2\displaystyle 4\Big((\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[|\overline{V}\_{h+1}^{k-1}(X)|])^{2}+(\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[|V\_{h+1}^{\tilde{\pi}^{k}}(X)|])^{2} |  |
|  |  |  | +(V¯h+1k−1(Xh+1k))2+(Vh+1π~k(Xh+1k))2)\displaystyle+(\overline{V}\_{h+1}^{k-1}(X\_{h+1}^{k}))^{2}+(V\_{h+1}^{\tilde{\pi}^{k}}(X\_{h+1}^{k}))^{2}\Big) |  |
|  |  | ≤\displaystyle\leq | c˘3​Z2​m+2+c˘4,\displaystyle\breve{c}\_{3}Z^{2m+2}+\breve{c}\_{4}, |  |

where c˘3,c˘4\breve{c}\_{3},\breve{c}\_{4} depends only on C~max,Cmax,m,D,d𝒮\widetilde{C}\_{\max},C\_{\max},m,D,d\_{\mathcal{S}}. The last inequality holds due to ([C.10](https://arxiv.org/html/2512.14991v1#A3.Ex82 "C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([2.8](https://arxiv.org/html/2512.14991v1#S2.E8 "In Proposition 2.5. ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.30](https://arxiv.org/html/2512.14991v1#A3.E30 "In C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.31](https://arxiv.org/html/2512.14991v1#A3.E31 "In C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the fact that ‖Xhk‖≤Z\|X\_{h}^{k}\|\leq Z for (h,k)∈[H]×[K](h,k)\in[H]\times[K].

Similarly, with probability at least 1−3​δ1-3\delta, the following inequality holds for h∈[H]h\in[H] and k∈[K]k\in[K]:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 𝔼​[(ξh+1k)2|ℱh,k]\displaystyle\mathbb{E}[(\xi\_{h+1}^{k})^{2}|\mathcal{F}\_{h,k}] |  | (C.33) |
|  |  | ≤\displaystyle\leq | 𝔼Y∼Th(⋅|Xhk,Ahk)[(𝔼X∼Th(⋅|Xhk,Ahk)[|V¯h+1k−1(X)|]+𝔼X∼Th(⋅|Xhk,Ahk)[|Vh+1π~k(X)|]\displaystyle\mathbb{E}\_{Y\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}\Bigg[\Big(\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[|\overline{V}\_{h+1}^{k-1}(X)|]+\mathbb{E}\_{X\sim{T}\_{h}(\cdot|X\_{h}^{k},A\_{h}^{k})}[|V\_{h+1}^{\tilde{\pi}^{k}}(X)|] |  |
|  |  |  | +|V¯h+1k−1(Y)|+|Vh+1π~k(Y)|)2]\displaystyle\qquad\qquad\qquad\qquad+|\overline{V}\_{h+1}^{k-1}(Y)|+|V\_{h+1}^{\tilde{\pi}^{k}}(Y)|\Big)^{2}\Bigg] |  |
|  |  | ≤\displaystyle\leq | c˘5​Z2​m+2+c˘6,\displaystyle\breve{c}\_{5}Z^{2m+2}+\breve{c}\_{6}, |  |

where c˘5,c˘6\breve{c}\_{5},\breve{c}\_{6} depends only on C~max,Cmax,m,D,d𝒮\widetilde{C}\_{\max},C\_{\max},m,D,d\_{\mathcal{S}}.

Define Mh+1,k:=∑h′≤h,k′≤kξh+1kM\_{h+1,k}:=\sum\_{h^{\prime}\leq h,k^{\prime}\leq k}\xi\_{h+1}^{k}. It is clear that Mh+1,kM\_{h+1,k} is a square integrable martingale. Then by Theorem 2.1 in [Bercu and Touati, [2008](https://arxiv.org/html/2512.14991v1#bib.bib5)], for any a,b>0a,b>0 we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|MH+1,K|≥a,⟨M⟩H+1,K+[M]H+1,K≤b)≤2​exp⁡(−a22​b),\displaystyle\mathbb{P}\Big(|M\_{H+1,K}|\geq a,\langle M\rangle\_{H+1,K}+[M]\_{H+1,K}\leq b\Big)\leq 2\exp{(-\frac{a^{2}}{2b})}, |  | (C.34) |

where [M]H+1,K=∑h∈[H],k∈[K](ξh+1k)2,⟨M⟩H+1,K=∑h∈[H],k∈[K]𝔼​[(ξh+1k)2|ℱh,k][M]\_{H+1,K}=\sum\_{h\in[H],k\in[K]}(\xi\_{h+1}^{k})^{2},\langle M\rangle\_{H+1,K}=\sum\_{h\in[H],k\in[K]}\mathbb{E}[(\xi\_{h+1}^{k})^{2}|\mathcal{F}\_{h,k}].

Therefore, we have for any a,b,c>0a,b,c>0:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ℙ​(|MH+1,K|≥a)\displaystyle\mathbb{P}(|M\_{H+1,K}|\geq a) |  | (C.35) |
|  |  | ≤\displaystyle\leq | ℙ​(|MH+1,K|≥a,⟨M⟩H+1,K+[M]H+1,K≤b)+ℙ​(⟨M⟩H+1,K+[M]H+1,K≥b)\displaystyle\mathbb{P}(|M\_{H+1,K}|\geq a,\langle M\rangle\_{H+1,K}+[M]\_{H+1,K}\leq b)+\mathbb{P}(\langle M\rangle\_{H+1,K}+[M]\_{H+1,K}\geq b) |  |
|  |  | ≤\displaystyle\leq | 2​exp⁡(−a22​b)+ℙ​(⟨M⟩H+1,K+[M]H+1,K≥b,Z≤c)+ℙ​(Z≥c).\displaystyle 2\exp{(-\frac{a^{2}}{2b})}+\mathbb{P}(\langle M\rangle\_{H+1,K}+[M]\_{H+1,K}\geq b,Z\leq c)+\mathbb{P}(Z\geq c). |  |

Let a=2​b​log⁡(2δ)a=\sqrt{2b\log(\frac{2}{\delta})}, b=2​H​K​(c˘3+c˘4+c˘5+c˘6)​(c2​m+2+1)b=2HK(\breve{c}\_{3}+\breve{c}\_{4}+\breve{c}\_{5}+\breve{c}\_{6})(c^{2m+2}+1), and c=(Mp​Kδ)1pc=\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{1}{p}}, we get that:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(⟨M⟩H+1,K+[M]H+1,K≥b,Z≤c)≤3​δ, and ​ℙ​(Z≥c)≤δ,\displaystyle\mathbb{P}\Big(\langle M\rangle\_{H+1,K}+[M]\_{H+1,K}\geq b,Z\leq c\Big)\leq 3\delta,\textit{ and }\mathbb{P}\Big(Z\geq c\Big)\leq\delta, |  |

where the first inequality holds since with probability at least 1−3​δ1-3\delta, for any h∈[H]h\in[H] and k∈[K]k\in[K], it holds that ([C.32](https://arxiv.org/html/2512.14991v1#A3.E32 "In C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.33](https://arxiv.org/html/2512.14991v1#A3.E33 "In C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Hence, we conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|MH+1,K|≤2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ))≥1−5​δ,\displaystyle\mathbb{P}\Bigg(|M\_{H+1,K}|\leq 2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)}\,\,\Bigg)\geq 1-5\delta, |  | (C.36) |

where L~1=c˘3+c˘4+c˘5+c˘6\widetilde{L}\_{1}=\breve{c}\_{3}+\breve{c}\_{4}+\breve{c}\_{5}+\breve{c}\_{6}.
∎

###### Lemma C.5.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. We have:

|  |  |  |
| --- | --- | --- |
|  | ℙ(|∑h=1H∑k∈[K]\JρKKξh+1k|≤e2L~2H(K​Mpρp+2Klog(1δ))((Mp​Kδ)m+1p+1))≥1−2δ,\displaystyle\mathbb{P}\Big(\Big|\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}^{K}\xi\_{h+1}^{k}\Big|\leq e^{2}\widetilde{L}\_{2}H\Big(\frac{KM\_{p}}{\rho^{p}}+\sqrt{2K\log(\frac{1}{\delta}})\Big)\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}+1\Big)\Big)\geq 1-2\delta, |  |

where L~2\widetilde{L}\_{2} is defined in ([5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Proof.

By similar methods to show ([C.32](https://arxiv.org/html/2512.14991v1#A3.E32 "In C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) in the proof of Lemma [C.4](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem4 "Lemma C.4. ‣ C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we can show that

|  |  |  |
| --- | --- | --- |
|  | |ξh+1k|≤c˘1​Zm+1+c˘2,\displaystyle|\xi\_{h+1}^{k}|\leq\breve{c}\_{1}Z^{m+1}+\breve{c}\_{2}, |  |

where c˘1,c˘2\breve{c}\_{1},\breve{c}\_{2} depends only on C~max,Cmax,m,D,d𝒮\widetilde{C}\_{\max},C\_{\max},m,D,d\_{\mathcal{S}}.

Therefore, let L~2=c˘1+c˘2\widetilde{L}\_{2}=\breve{c}\_{1}+\breve{c}\_{2}, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ℙ(|∑h=1H∑k∈[K]\JρKKξh+1k|≤e2L~2H(K​Mpρp+2Klog(1δ))((Mp​Kδ)m+1p+1))\displaystyle\mathbb{P}\Big(\Big|\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}^{K}\xi\_{h+1}^{k}\Big|\leq e^{2}\widetilde{L}\_{2}H\Big(\frac{KM\_{p}}{\rho^{p}}+\sqrt{2K\log(\frac{1}{\delta}})\Big)\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}+1\Big)\Big) |  | (C.37) |
|  |  | ≥\displaystyle\geq | ℙ(∑h=1H∑k∈[K]\JρKK|ξh+1k|≤e2L~2H(K​Mpρp+2Klog(1δ))((Mp​Kδ)m+1p+1))\displaystyle\mathbb{P}\Big(\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}^{K}\Big|\xi\_{h+1}^{k}\Big|\leq e^{2}\widetilde{L}\_{2}H\Big(\frac{KM\_{p}}{\rho^{p}}+\sqrt{2K\log(\frac{1}{\delta}})\Big)\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}+1\Big)\Big) |  |
|  |  | ≥\displaystyle\geq | ℙ(H(K−K0)(c˘1Zm+1+c˘2)≤e2L~2H(K​Mpρp+2Klog(1δ))((Mp​Kδ)m+1p+1))\displaystyle\mathbb{P}\Big(H(K-K\_{0})(\breve{c}\_{1}Z^{m+1}+\breve{c}\_{2})\leq e^{2}\widetilde{L}\_{2}H\Big(\frac{KM\_{p}}{\rho^{p}}+\sqrt{2K\log(\frac{1}{\delta}})\Big)\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}+1\Big)\Big) |  |
|  |  | ≥\displaystyle\geq | 1−2​δ,\displaystyle 1-2\delta, |  |

where the last inequality holds due to Proposition [5.10](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem10 "Proposition 5.10. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Lemma [C.3](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem3 "Lemma C.3. ‣ C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").
∎

Similarly, we can prove the following lemmas for {ζh+1k}(h,k)∈[H]×[K]\{\zeta\_{h+1}^{k}\}\_{(h,k)\in[H]\times[K]} in the same fashion as the proof of Lemma [C.4](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem4 "Lemma C.4. ‣ C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [C.5](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Lemma C.6.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. We have:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(∑h=1H∑k=1Kζh+1k≤2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ))≥1−2​δ,\displaystyle\mathbb{P}\Bigg(\sum\_{h=1}^{H}\sum\_{k=1}^{K}\zeta\_{h+1}^{k}\leq 2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)}\Bigg)\geq 1-2\delta, |  |

where L~1\widetilde{L}\_{1} is defined in ([5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

###### Lemma C.7.

Assume Assumptions [2.1](https://arxiv.org/html/2512.14991v1#S2.Thmassumption1 "Assumption 2.1 (Regularity of the dynamics). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")-[2.3](https://arxiv.org/html/2512.14991v1#S2.Thmassumption3 "Assumption 2.3 (Regularity of the initial distribution). ‣ 2.2 Outstanding assumptions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") hold. We have:

|  |  |  |
| --- | --- | --- |
|  | ℙ(|∑h=1H∑k∈[K]\JρKKζh+1k|≤e2L~2H(K​Mpρp+2Klog(1δ))((Mp​Kδ)m+1p+1))≥1−2δ,\displaystyle\mathbb{P}\Big(\Big|\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}^{K}\zeta\_{h+1}^{k}\Big|\leq e^{2}\widetilde{L}\_{2}H\Big(\frac{KM\_{p}}{\rho^{p}}+\sqrt{2K\log(\frac{1}{\delta}})\Big)\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}+1\Big)\Big)\geq 1-2\delta, |  |

where L~2\widetilde{L}\_{2} is defined in ([5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Then with the five lemmas above, we are ready to provide the proof for Theorem [5.12](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem12 "Theorem 5.12. ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

###### Proof.

Combine Theorem [5.9](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem9 "Theorem 5.9. ‣ 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), Lemma [C.2](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem2 "Lemma C.2 (Theorem F.1 in [Sinclair et al., 2023]). ‣ C.9 Lemma C.2 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), and the fact that (1+1H)H≤e\Big(1+\frac{1}{H}\Big)^{H}\leq e, with probability at least 1−3​δ1-3\delta, we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∑k∈JρKΔ1(k)\displaystyle\sum\_{k\in J\_{\rho}^{K}}\Delta\_{1}^{(k)} | ≤\displaystyle\leq | ∑k∈JρKCLIP​(G1k​(B1k)|Gap1​(B1k)H+1)+(1+1H)​(∑k∈JρKΔ2(k)+∑k∈JρKξ2k)+∑k∈JρKζ2k\displaystyle\sum\_{k\in J\_{\rho}^{K}}{\rm CLIP}\Bigg(G\_{1}^{k}(B\_{1}^{k})\Bigg|\frac{{\rm Gap}\_{1}(B\_{1}^{k})}{H+1}\Bigg)+\Big(1+\frac{1}{H}\Big)\Big(\sum\_{k\in J\_{\rho}^{K}}\Delta\_{2}^{(k)}+\sum\_{k\in J\_{\rho}^{K}}\xi\_{2}^{k}\Big)+\sum\_{k\in J\_{\rho}^{K}}\zeta\_{2}^{k} |  | (C.39) |
|  |  | ≤\displaystyle\leq | ∑h=1H∑k∈JρK(1+1H)2​(h−1)​CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)\displaystyle\sum\_{h=1}^{H}\sum\_{k\in J\_{\rho}^{K}}\Big(1+\frac{1}{H}\Big)^{2(h-1)}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg) |  |
|  |  |  | +∑h=1H∑k∈JρK(1+1H)2​h​ξh+1k+∑h=1H∑k∈JρKζh+1k\displaystyle+\sum\_{h=1}^{H}\sum\_{k\in J\_{\rho}^{K}}\Big(1+\frac{1}{H}\Big)^{2h}\xi\_{h+1}^{k}+\sum\_{h=1}^{H}\sum\_{k\in J\_{\rho}^{K}}\zeta\_{h+1}^{k} |  |
|  |  | ≤\displaystyle\leq | e2​∑h=1H∑k∈JρKCLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+2​e2​∑h=1H∑k∈JρKξh+1k+∑h=1H∑k∈JρKζh+1k\displaystyle e^{2}\sum\_{h=1}^{H}\sum\_{k\in J\_{\rho}^{K}}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+2e^{2}\sum\_{h=1}^{H}\sum\_{k\in J\_{\rho}^{K}}\xi\_{h+1}^{k}+\sum\_{h=1}^{H}\sum\_{k\in J\_{\rho}^{K}}\zeta\_{h+1}^{k} |  |
|  |  | ≤\displaystyle\leq | e2​∑h=1H∑k∈JρKCLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+2​e2​∑h=1H∑k∈[K]ξh+1k+2​e2​|∑h=1H∑k∈[K]\JρKξh+1k|\displaystyle e^{2}\sum\_{h=1}^{H}\sum\_{k\in J\_{\rho}^{K}}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+2e^{2}\sum\_{h=1}^{H}\sum\_{k\in[K]}\xi\_{h+1}^{k}+2e^{2}\Big|\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}\xi\_{h+1}^{k}\Big| |  |
|  |  |  | +∑h=1H∑k∈[K]ζh+1k+|∑h=1H∑k∈[K]\JρKζh+1k|.\displaystyle+\sum\_{h=1}^{H}\sum\_{k\in[K]}\zeta\_{h+1}^{k}+\Big|\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}\zeta\_{h+1}^{k}\Big|. |  |

By combining Theorems [5.9](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem9 "Theorem 5.9. ‣ 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), [5.10](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem10 "Proposition 5.10. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and [5.11](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem11 "Theorem 5.11. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"), we get that with probability at least 1−6​δ1-6\delta, it holds that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Regret​(K)\displaystyle{\rm Regret}(K) | ≤\displaystyle\leq | ∑k∈JρK(V¯1k−1​(X1k)−V1π~k​(X1k))+∑k∈J\JρK(|V1∗​(X1k)|+|V1π~k​(X1k)|)\displaystyle\sum\_{k\in J\_{\rho}^{K}}(\overline{V}\_{1}^{k-1}(X\_{1}^{k})-V\_{1}^{\tilde{\pi}^{k}}(X\_{1}^{k}))+\sum\_{k\in J\backslash J\_{\rho}^{K}}(|V\_{1}^{\*}(X\_{1}^{k})|+|V\_{1}^{\tilde{\pi}^{k}}(X\_{1}^{k})|) |  |
|  |  | ≤\displaystyle\leq | ∑k∈JρKΔ1(k)+2​(K​κm+1​(δ,ρ)+C~1​(1+ρm+1)​(K−K0))\displaystyle\sum\_{k\in J\_{\rho}^{K}}\Delta\_{1}^{(k)}+2\Big(K\kappa\_{m+1}(\delta,\rho)+\widetilde{C}\_{1}\Big(1+\rho^{m+1}\Big)(K-K\_{0})\Big) |  |
|  |  | ≤\displaystyle\leq | e2​∑h=1H∑k∈J1CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+2​e2​∑h=1H∑k∈[K]ξh+1k+2​e2​|∑h=1H∑k∈[K]\JρKξh+1k|\displaystyle e^{2}\sum\_{h=1}^{H}\sum\_{k\in J\_{1}}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+2e^{2}\sum\_{h=1}^{H}\sum\_{k\in[K]}\xi\_{h+1}^{k}+2e^{2}\Big|\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}\xi\_{h+1}^{k}\Big| |  |
|  |  |  | +∑h=1H∑k∈[K]ζh+1k+|∑h=1H∑k∈[K]\JρKζh+1k|\displaystyle+\sum\_{h=1}^{H}\sum\_{k\in[K]}\zeta\_{h+1}^{k}+\Big|\sum\_{h=1}^{H}\sum\_{k\in[K]\backslash J\_{\rho}^{K}}\zeta\_{h+1}^{k}\Big| |  |
|  |  |  | +2​K​κm+1​(δ,ρ)+4​C~1​(1+ρm+1)​(Mpρp​K+2​K​log⁡(1δ))\displaystyle+2K\kappa\_{m+1}(\delta,\rho)+4\widetilde{C}\_{1}\Big(1+\rho^{m+1}\Big)\left(\frac{M\_{p}}{\rho^{p}}K+\sqrt{2K\log\Big(\frac{1}{\delta}\Big)}\right) |  |
|  |  | ≤\displaystyle\leq | e2​∑h=1H∑k∈J1CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)+2​e2​L~1​H​K​((Mp​Kδ)2​m+2p+1)​log⁡(2δ)\displaystyle e^{2}\sum\_{h=1}^{H}\sum\_{k\in J\_{1}}{\rm CLIP}\Bigg(G\_{h}^{k}(B\_{h}^{k})\Bigg|\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Bigg)+2e^{2}\sqrt{\widetilde{L}\_{1}HK\Big(\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{2m+2}{p}}+1\Big)\log\Big(\frac{2}{\delta}\Big)} |  |
|  |  |  | +2​K​κm+1​(δ,ρ)+4​C~1​(L~3+ρm+1+e2​L~2​H​(Mp​Kδ)m+1p)​(Mpρp​K+2​K​log⁡(1δ)),\displaystyle+2K\kappa\_{m+1}(\delta,\rho)+4\widetilde{C}\_{1}\Big(\widetilde{L}\_{3}+\rho^{m+1}+e^{2}\widetilde{L}\_{2}H\Big(\frac{M\_{p}K}{\delta}\Big)^{\frac{m+1}{p}}\Big)\left(\frac{M\_{p}}{\rho^{p}}K+\sqrt{2K\log\Big(\frac{1}{\delta}\Big)}\right), |  |

where J=[K]J=[K] and JρKJ\_{\rho}^{K} is defined in ([5.32](https://arxiv.org/html/2512.14991v1#S5.E32 "In 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
The first inequality holds due to Theorem [5.2](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem2 "Theorem 5.2. ‣ Design of value estimators. ‣ 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). The second inequality holds due to Theorem [5.11](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem11 "Theorem 5.11. ‣ 5.3 Concentrations on the size of 𝐽_𝜌^𝐾 and initial value function ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes"). The third inequality holds due to ([C.39](https://arxiv.org/html/2512.14991v1#A3.E39 "In C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). Finally, the last inequality holds due to Lemma [C.4](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem4 "Lemma C.4. ‣ C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") and Lemma [C.5](https://arxiv.org/html/2512.14991v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.10 Proof of Theorem 5.12 ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").
∎

### C.11 Technical results modified from [Sinclair et al., [2023](https://arxiv.org/html/2512.14991v1#bib.bib53)]

#### C.11.1 Proof of Lemma [5.17](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem17 "Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")

###### Proof.

We firstly split ∑h∑k∈JρKCLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}{\rm CLIP}\Big(G\_{h}^{k}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big) into two terms.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ∑h∑k∈JρKCLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}{\rm CLIP}\Big(G\_{h}^{k}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big) |  | (C.40) |
|  |  | =\displaystyle= | ∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)>0CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)⏟(I)\displaystyle\underbrace{\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})>0}{\rm CLIP}\Big(G\_{h}^{k}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big)}\_{(I)} |  |
|  |  |  | +∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)=0CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)⏟(I​I).\displaystyle+\underbrace{\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})=0}{\rm CLIP}\Big(G\_{h}^{k}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big)}\_{(II)}. |  |

Then we handle these two terms separately.

Bound for Term (I):

For fixed (h,k)(h,k), if nhk−1​(Bhk)>0n\_{h}^{k-1}(B\_{h}^{k})>0, then:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Ghk​(Bhk)\displaystyle G\_{h}^{k}(B\_{h}^{k}) | =\displaystyle= | 2​C^maxC¯max​(R-UCBhk−1​(Bhk)+T-UCBhk−1​(Bhk)+BIAS​(Bhk))\displaystyle 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big(\mbox{\rm R-UCB}\_{h}^{k-1}(B\_{h}^{k})+\mbox{\rm T-UCB}\_{h}^{k-1}(B\_{h}^{k})+{\rm BIAS}(B\_{h}^{k})\Big) |  | (C.41) |
|  |  |  | +Ch(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)\displaystyle+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm diam}(B\_{h}^{k}) |  |
|  |  | ≤\displaystyle\leq | 2C^maxC¯max(CONFhk−1(Bhk)+g2(δ,∥x~(oBhk)∥)CONFhk−1(Bhk))\displaystyle 2\frac{\widehat{C}\_{\max}}{\overline{C}\_{\max}}\Big({\rm CONF}\_{h}^{k-1}(B\_{h}^{k})+g\_{2}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\Big) |  |
|  |  |  | +Ch(1+2(∥x~(oBhk)∥+D)m)CONFhk−1(Bhk)\displaystyle+C\_{h}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}){\rm CONF}\_{h}^{k-1}(B\_{h}^{k}) |  |
|  |  | =\displaystyle= | g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk),\displaystyle g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|)\,\,{\rm CONF}\_{h}^{k-1}(B\_{h}^{k}), |  |

where g2g\_{2} is defined in ([5.2](https://arxiv.org/html/2512.14991v1#S5.E2 "In 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and g3g\_{3} is defined in ([5.39](https://arxiv.org/html/2512.14991v1#S5.E39 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). The first equality holds by the definition of Ghk​(Bhk)G\_{h}^{k}(B\_{h}^{k}) in ([5.31](https://arxiv.org/html/2512.14991v1#S5.E31 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). The inequality holds because

* (a)

  R-UCBhk−1​(Bhk)+T-UCBhk−1​(Bhk)≤CONFhk−1​(Bhk)\mbox{\rm R-UCB}\_{h}^{k-1}(B\_{h}^{k})+\mbox{\rm T-UCB}\_{h}^{k-1}(B\_{h}^{k})\leq{\rm CONF}\_{h}^{k-1}(B\_{h}^{k}) by ([4.20](https://arxiv.org/html/2512.14991v1#S4.E20 "In 4.3 Concentration on reward estimators and properties of adaptive partition ‣ 4 Concentration inequalities of the estimators ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")),
* (b)

  BIAS(Bhk)=g2(δ,∥x~(oBhk)∥)diam(Bhk){\rm BIAS}(B\_{h}^{k})=g\_{2}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|)\,\,{\rm diam}(B\_{h}^{k}) by ([5.2](https://arxiv.org/html/2512.14991v1#S5.E2 "In 5.1 Construction of value estimators ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and
* (c)

  diam​(Bhk)≤CONFhk−1​(Bhk){\rm diam}(B\_{h}^{k})\leq{\rm CONF}\_{h}^{k-1}(B\_{h}^{k}) by the Splitting Rule in line [1](https://arxiv.org/html/2512.14991v1#alg4.l1 "In Algorithm 4 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes") of Algorithm [4](https://arxiv.org/html/2512.14991v1#alg4 "Algorithm 4 ‣ Initial state partition. ‣ 3 Algorithm design ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes").

The last equality holds by ([5.39](https://arxiv.org/html/2512.14991v1#S5.E39 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

By definition of the CLIP(⋅|.){\rm CLIP}(\cdot|.) function in ([5.22](https://arxiv.org/html/2512.14991v1#S5.E22 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.41](https://arxiv.org/html/2512.14991v1#A3.E41 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) implies that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)\displaystyle{\rm CLIP}\Big(G\_{h}^{k}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big) | ≤\displaystyle\leq | CLIP(g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)|Gaph​(Bhk)H+1)\displaystyle{\rm CLIP}\Big(g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|)\,\,{\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big) |  |
|  |  | =\displaystyle= | g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)𝕀{g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)≥Gaph​(Bhk)H+1}.\displaystyle g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|)\,\,{\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\mathbb{I}\_{\left\{g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\geq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\right\}}. |  |

Next, we find an upper bound for 𝕀{g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)≥Gaph​(Bhk)H+1}\mathbb{I}\_{\left\{g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\geq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\right\}}.

Note that for (x1,a1),(x2,a2)∈ℝd𝒮×𝒜(x\_{1},a\_{1}),(x\_{2},a\_{2})\in\mathbb{R}^{d\_{\mathcal{S}}}\times\mathcal{A}, by ([2.7](https://arxiv.org/html/2512.14991v1#S2.E7 "In Proposition 2.4 (Local Lipschitz property of the value function). ‣ 2.3 Properties of the dynamics and value functions ‣ 2 Mathematical set-up ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([A.15](https://arxiv.org/html/2512.14991v1#A1.E15 "In Proposition A.1. ‣ A.4 Local lipschitz property for optimal Q function ‣ Appendix A Technical details in Section 2 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |G~​aph​(x1,a1)−G~​aph​(x2,a2)|≤3​C¯max​(1+‖x1‖m+‖x2‖m)​(‖x1−x2‖+‖a1−a2‖).\displaystyle|{\rm\widetilde{G}ap}\_{h}(x\_{1},a\_{1})-{\rm\widetilde{G}ap}\_{h}(x\_{2},a\_{2})|\leq 3{\overline{C}\_{\max}(1+\|x\_{1}\|^{m}+\|x\_{2}\|^{m})}(\|x\_{1}-x\_{2}\|+\|a\_{1}-a\_{2}\|). |  | (C.43) |

Then by definition in ([5.23](https://arxiv.org/html/2512.14991v1#S5.E23 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.43](https://arxiv.org/html/2512.14991v1#A3.E43 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G~aph(center(Bhk))≤Gaph(Bhk)+3C¯max(1+2(∥x~(oBhk)∥+D)m))diam(Bhk).\displaystyle{\rm\widetilde{G}ap}\_{h}({\rm center}(B\_{h}^{k}))\leq{\rm Gap}\_{h}(B\_{h}^{k})+3{\overline{C}\_{\max}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m}))}{\rm diam}(B\_{h}^{k}). |  | (C.44) |

In addition, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | (H+1)g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)+3C¯max(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)\displaystyle(H+1)g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|)\,\,{\rm CONF}\_{h}^{k-1}(B\_{h}^{k})+3{\overline{C}\_{\max}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m})}{\rm diam}(B\_{h}^{k}) |  | (C.45) |
|  |  | ≤\displaystyle\leq | 2((H+1)g3(δ,∥x~(oBhk)∥)+3C¯max(1+2(∥x~(oBhk)∥+D)m))diam(Bhk)\displaystyle 2\Big((H+1)g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|)+3\overline{C}\_{\max}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m})\Big){\rm diam}(B\_{h}^{k}) |  |
|  |  | ≤\displaystyle\leq | g¯​(δ,x~​(Bhk))​(H+1)​diam​(Bhk),\displaystyle\bar{g}(\delta,\tilde{x}(B\_{h}^{k}))(H+1){\rm diam}(B\_{h}^{k}), |  |

where the first inequality holds due to ([B.16](https://arxiv.org/html/2512.14991v1#A2.E16 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the second inequality holds due to ([5.38](https://arxiv.org/html/2512.14991v1#S5.E38 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Therefore,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 𝕀{g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)≥Gaph​(Bhk)H+1}\displaystyle\mathbb{I}\_{\left\{g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\geq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\right\}} |  | (C.46) |
|  |  | =\displaystyle= | 𝕀{(H+1)g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)≥Gaph(Bhk)}\displaystyle\mathbb{I}\_{\left\{(H+1)g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\geq{\rm Gap}\_{h}(B\_{h}^{k})\right\}} |  |
|  |  | ≤\displaystyle\leq | 𝕀{g¯(δ,x~(Bhk))(H+1)diam(Bhk)≥Gaph(Bhk)+3C¯max(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)}\displaystyle\mathbb{I}\_{\left\{\bar{g}(\delta,\tilde{x}(B\_{h}^{k}))(H+1){\rm diam}(B\_{h}^{k})\geq{\rm Gap}\_{h}(B\_{h}^{k})+3{\overline{C}\_{\max}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m})}{\rm diam}(B\_{h}^{k})\right\}} |  |
|  |  | ≤\displaystyle\leq | 𝕀{g¯​(δ,x~​(Bhk))​(H+1)​diam​(Bhk)≥G~​aph​(center​(Bhk))}\displaystyle\mathbb{I}\_{\left\{\bar{g}(\delta,\tilde{x}(B\_{h}^{k}))(H+1){\rm diam}(B\_{h}^{k})\geq{\rm\widetilde{G}ap}\_{h}({\rm center}(B\_{h}^{k}))\right\}} |  |
|  |  | ≤\displaystyle\leq | 𝕀{center​(Bhk)∈Zhdiam​(Bhk),ρ},\displaystyle\mathbb{I}\_{\left\{{\rm center}(B\_{h}^{k})\in Z\_{h}^{{\rm diam}(B\_{h}^{k}),\rho}\right\}}, |  |

where the first inequality holds by ([C.45](https://arxiv.org/html/2512.14991v1#A3.E45 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the second inequality holds by ([C.44](https://arxiv.org/html/2512.14991v1#A3.E44 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the last inequality holds by ([5.37](https://arxiv.org/html/2512.14991v1#S5.E37 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Then,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | ∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)>0CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})>0}{\rm CLIP}\Big(G\_{h}^{k}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big) |  | (C.47) |
|  |  | ≤\displaystyle\leq | ∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)>0CLIP(g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)|Gaph​(Bhk)H+1)\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})>0}{\rm CLIP}\Big(g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big) |  |
|  |  | =\displaystyle= | ∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)>0g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)𝕀{g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)≥Gaph​(Bhk)H+1}\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})>0}g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\mathbb{I}\_{\{g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\geq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\}} |  |
|  |  | ≤\displaystyle\leq | ∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)>0g3(δ,∥x~(oBhk)∥)CONFhk−1(Bhk)𝕀{center​(Bhk)∈Zhdiam​(Bhk),ρ,l}\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})>0}g\_{3}(\delta,\|\tilde{x}(^{o}B\_{h}^{k})\|){\rm CONF}\_{h}^{k-1}(B\_{h}^{k})\mathbb{I}\_{\{{\rm center}(B\_{h}^{k})\in Z\_{h}^{{\rm diam}(B\_{h}^{k}),\rho,l}\}} |  |
|  |  | =\displaystyle= | ∑h∑r∈ℛ∑B:diam​(B)=r∑k:Bhk=B,nhk−1​(Bhk)>0g3(δ,∥x~(oB)∥)CONFhk−1(B)𝕀{center​(B)∈Zhr,ρ}\displaystyle\sum\_{h}\sum\_{r\in\mathcal{R}}\sum\_{B:{\rm diam}(B)=r}\sum\_{k:B\_{h}^{k}=B,n\_{h}^{k-1}(B\_{h}^{k})>0}g\_{3}(\delta,\|\tilde{x}(^{o}B)\|){\rm CONF}\_{h}^{k-1}(B)\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}} |  |
|  |  | =\displaystyle= | ∑h∑r∈ℛ,r<r0∑B:diam​(B)=r∑k:Bhk=B,nhk−1​(Bhk)>0g3(δ,∥x~(oB)∥)CONFhk−1(B)𝕀{center​(B)∈Zhr,ρ}\displaystyle\sum\_{h}\sum\_{r\in\mathcal{R},r<r\_{0}}\sum\_{B:{\rm diam}(B)=r}\sum\_{k:B\_{h}^{k}=B,n\_{h}^{k-1}(B\_{h}^{k})>0}g\_{3}(\delta,\|\tilde{x}(^{o}B)\|){\rm CONF}\_{h}^{k-1}(B)\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}} |  |
|  |  |  | +∑h∑r∈ℛ,r≥r0∑B:diam​(B)=r∑k:Bhk=B,nhk−1​(Bhk)>0g3(δ,∥x~(oB)∥)CONFhk−1(B)𝕀{center​(B)∈Zhr,ρ}\displaystyle+\sum\_{h}\sum\_{r\in\mathcal{R},r\geq r\_{0}}\sum\_{B:{\rm diam}(B)=r}\sum\_{k:B\_{h}^{k}=B,n\_{h}^{k-1}(B\_{h}^{k})>0}g\_{3}(\delta,\|\tilde{x}(^{o}B)\|){\rm CONF}\_{h}^{k-1}(B)\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}} |  |
|  |  | ≤\displaystyle\leq | 2g3(δ,ρ+D)Kr0+g3(δ,ρ+D)g1(δ,ρ+D)×\displaystyle 2g\_{3}(\delta,\rho+D)Kr\_{0}+g\_{3}(\delta,\rho+D)g\_{1}(\delta,\rho+D)\times |  |
|  |  |  | ∑h∑r∈ℛ,r≥r0∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}​∑k:Bhk=B1nhk−1​(B),\displaystyle\sum\_{h}\sum\_{r\in\mathcal{R},r\geq r\_{0}}\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}\sum\_{k:B\_{h}^{k}=B}\frac{1}{\sqrt{n\_{h}^{k-1}(B)}}, |  |

where the first inequality holds by ([C.11.1](https://arxiv.org/html/2512.14991v1#A3.Ex119 "C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the second inequality holds by ([C.46](https://arxiv.org/html/2512.14991v1#A3.E46 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and the last inequality holds due to ([B.16](https://arxiv.org/html/2512.14991v1#A2.E16 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

To bound the second term above,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | g3​(δ,ρ+D)​g1​(δ,ρ+D)​∑h∑r∈ℛ,r≥r0∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}​∑k:Bhk=B1nhk−1​(B)\displaystyle g\_{3}(\delta,\rho+D)g\_{1}(\delta,\rho+D)\sum\_{h}\sum\_{r\in\mathcal{R},r\geq r\_{0}}\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}\sum\_{k:B\_{h}^{k}=B}\frac{1}{\sqrt{n\_{h}^{k-1}(B)}} |  | (C.48) |
|  |  | ≤\displaystyle\leq | g3(δ,ρ+D)g1(δ,ρ+D)×\displaystyle g\_{3}(\delta,\rho+D)g\_{1}(\delta,\rho+D)\times |  |
|  |  |  | ∑h∑r∈ℛ,r≥r0∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}​∫x=0nmax​(B)−nmin​(B)1x+nmin​(B)​𝑑x\displaystyle\qquad\sum\_{h}\sum\_{r\in\mathcal{R},r\geq r\_{0}}\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}\int\_{x=0}^{n\_{\max}(B)-n\_{\min}(B)}\frac{1}{\sqrt{x+n\_{\min}(B)}}\,dx |  |
|  |  | ≤\displaystyle\leq | 2​g3​(δ,ρ+D)​g1​(δ,ρ+D)​∑h∑r∈ℛ,r≥r0∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}​nmax​(B)\displaystyle 2g\_{3}(\delta,\rho+D)g\_{1}(\delta,\rho+D)\sum\_{h}\sum\_{r\in\mathcal{R},r\geq r\_{0}}\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}\sqrt{n\_{\max}(B)} |  |
|  |  | ≤\displaystyle\leq | 2​g3​(δ,ρ+D)​g1​(δ,ρ+D)​∑h∑r∈ℛ,r≥r0∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}​g1​(δ,ρ+D)r\displaystyle 2g\_{3}(\delta,\rho+D)g\_{1}(\delta,\rho+D)\sum\_{h}\sum\_{r\in\mathcal{R},r\geq r\_{0}}\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}\frac{g\_{1}(\delta,\rho+D)}{r} |  |
|  |  | ≤\displaystyle\leq | 2​g3​(δ,ρ+D)​g1​(δ,ρ+D)2​∑h∑r∈ℛ,r≥r0Nr​(Zhr,ρ)​1r,\displaystyle 2g\_{3}(\delta,\rho+D)g\_{1}(\delta,\rho+D)^{2}\sum\_{h}\sum\_{r\in\mathcal{R},r\geq r\_{0}}N\_{r}(Z\_{h}^{r,\rho})\frac{1}{r}, |  |

where nmax​(B)=(g1(δ,∥x~(oB)∥diam​(B))2,nmin​(B)=(g1(δ,∥x~(oB)∥2​d​i​a​m​(B))2n\_{\max}(B)=(\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|}{{\rm diam}(B)})^{2},n\_{\min}(B)=(\frac{g\_{1}(\delta,\|\tilde{x}(^{o}B)\|}{2{\rm diam}(B)})^{2}. The first inequality holds due to the fact that nmin​(B)≤nhk−1​(B)<nmax​(B)n\_{\min}(B)\leq n\_{h}^{k-1}(B)<n\_{\max}(B) by ([B.17](https://arxiv.org/html/2512.14991v1#A2.E17 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([B.18](https://arxiv.org/html/2512.14991v1#A2.E18 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). The second inequality holds by the fact that ∫ab1y​𝑑y≤2​b\int\_{a}^{b}\frac{1}{\sqrt{y}}\,dy\leq 2\sqrt{b} for b>a>0b>a>0. The fourth inequality holds due to ([B.18](https://arxiv.org/html/2512.14991v1#A2.E18 "In B.7 Proof of Lemma 4.6 ‣ Appendix B Technical details in Section 4 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the last inequality holds due to the fact that ∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}≤Nr​(Zhr,ρ)\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}\leq N\_{r}(Z\_{h}^{r,\rho}). This fact holds since the distance between the centers of two blocks B1B\_{1} and B2B\_{2} with same diameter rr is at least rr.

Bound for Term (II): Next we bound Term (II) in ([C.40](https://arxiv.org/html/2512.14991v1#A3.E40 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

For fixed (h,k)(h,k), if nhk−1​(Bhk)=0n\_{h}^{k-1}(B\_{h}^{k})=0, then diam​(Bhk)=D{\rm diam}(B\_{h}^{k})=D.

We now find an upper bound for 𝕀{Ghk​(Bhk)≥Gaph​(Bhk)H+1}\mathbb{I}\_{\left\{G\_{h}^{k}(B\_{h}^{k})\geq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\right\}}. Note that by ([5.31](https://arxiv.org/html/2512.14991v1#S5.E31 "In 5.2 Upper bound via clipping ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([5.38](https://arxiv.org/html/2512.14991v1#S5.E38 "In Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) we have:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | (H+1)Ghk(Bhk)+3C¯max(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)\displaystyle(H+1)G\_{h}^{k}(B\_{h}^{k})+3{\overline{C}\_{\max}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m})}{\rm diam}(B\_{h}^{k}) |  | (C.49) |
|  |  | ≤\displaystyle\leq | g¯​(δ,x~​(Bhk))​(H+1)​diam​(Bhk).\displaystyle\bar{g}(\delta,\tilde{x}(B\_{h}^{k}))(H+1){\rm diam}(B\_{h}^{k}). |  |

Therefore,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝕀{Ghk​(Bhk)≥Gaph​(Bhk)H+1}\displaystyle\mathbb{I}\_{\left\{G\_{h}^{k}(B\_{h}^{k})\geq\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\right\}} | =\displaystyle= | 𝕀{g¯(δ,x~(Bhk))(H+1)diam(Bhk)≥Gaph(Bhk)+3C¯max(1+2(∥x~(oBhk)∥+D)m)diam(Bhk)}\displaystyle\mathbb{I}\_{\left\{\bar{g}(\delta,\tilde{x}(B\_{h}^{k}))(H+1){\rm diam}(B\_{h}^{k})\geq{\rm Gap}\_{h}(B\_{h}^{k})+3{\overline{C}\_{\max}(1+2(\|\tilde{x}(^{o}B\_{h}^{k})\|+D)^{m})}{\rm diam}(B\_{h}^{k})\right\}} |  | (C.50) |
|  |  | ≤\displaystyle\leq | 𝕀{g¯​(δ,x~​(Bhk))​(H+1)​diam​(Bhk)≥G~​aph​(center​(Bhk))}\displaystyle\mathbb{I}\_{\left\{\bar{g}(\delta,\tilde{x}(B\_{h}^{k}))(H+1){\rm diam}(B\_{h}^{k})\geq{\rm\widetilde{G}ap}\_{h}({\rm center}(B\_{h}^{k}))\right\}} |  |
|  |  | ≤\displaystyle\leq | 𝕀{center​(Bhk)∈Zhdiam​(Bhk),ρ},\displaystyle\mathbb{I}\_{\left\{{\rm center}(B\_{h}^{k})\in Z\_{h}^{{\rm diam}(B\_{h}^{k}),\rho}\right\}}, |  |

where the first inequality holds by ([C.49](https://arxiv.org/html/2512.14991v1#A3.E49 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), the second inequality holds by ([C.44](https://arxiv.org/html/2512.14991v1#A3.E44 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and the third inequality holds by ([5.13](https://arxiv.org/html/2512.14991v1#S5.Thmtheorem13 "Definition 5.13 (Near optimal set). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).

Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | ∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)=0CLIP​(Ghk​(Bhk)|Gaph​(Bhk)H+1)\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})=0}{\rm CLIP}\Big(G\_{h}^{k}(B\_{h}^{k})\,\Big|\,\frac{{\rm Gap}\_{h}(B\_{h}^{k})}{H+1}\Big) |  |
|  |  | ≤\displaystyle\leq | ∑h∑k∈JρK∑Bhk:nhk−1​(Bhk)=0g¯(δ,x~(oBhk))diam(Bhk)𝕀{center​(Bhk)∈Zhdiam​(Bhk),ρ}\displaystyle\sum\_{h}\sum\_{k\in J\_{\rho}^{K}}\sum\_{B\_{h}^{k}:n\_{h}^{k-1}(B\_{h}^{k})=0}\bar{g}(\delta,\tilde{x}(^{o}B\_{h}^{k})){\rm diam}(B\_{h}^{k})\mathbb{I}\_{\left\{{\rm center}(B\_{h}^{k})\in Z\_{h}^{{\rm diam}(B\_{h}^{k}),\rho}\right\}} |  |
|  |  | =\displaystyle= | ∑h∑r=D∑B:diam​(B)=r∑k:Bhk=B,nhk−1​(Bhk)=0g¯(δ,x~(oB))diam(B)𝕀{center​(B)∈Zhr,ρ}\displaystyle\sum\_{h}\sum\_{r=D}\sum\_{B:{\rm diam}(B)=r}\sum\_{k:B\_{h}^{k}=B,n\_{h}^{k-1}(B\_{h}^{k})=0}\bar{g}(\delta,\tilde{x}(^{o}B)){\rm diam}(B)\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}} |  |
|  |  | ≤\displaystyle\leq | g¯​(δ,ρ+D)​D​∑h∑r=D∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}​|{k:Bhk=B,nhk−1​(Bhk)=0}|,\displaystyle\bar{g}(\delta,\rho+D)D\sum\_{h}\sum\_{r=D}\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}|\{k:B\_{h}^{k}=B,n\_{h}^{k-1}(B\_{h}^{k})=0\}|, |  |
|  |  | ≤\displaystyle\leq | (d𝒮+d𝒜)d𝒮+d𝒜2​(ρ+D)d𝒮​(2​a¯)d𝒜Dd𝒮+d𝒜−1​g¯​(δ,ρ+D)​∑h∑r=D∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ},\displaystyle(d\_{\mathcal{S}}+d\_{\mathcal{A}})^{\frac{d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2}}\frac{(\rho+D)^{d\_{\mathcal{S}}}(2\bar{a})^{d\_{\mathcal{A}}}}{D^{d\_{\mathcal{S}}+d\_{\mathcal{A}}-1}}\bar{g}(\delta,\rho+D)\sum\_{h}\sum\_{r=D}\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}, |  |
|  |  | ≤\displaystyle\leq | (d𝒮+d𝒜)d𝒮+d𝒜2​(ρ+D)d𝒮​(2​a¯)d𝒜Dd𝒮+d𝒜−2​g¯​(δ,ρ+D)​∑h∑r=DNr​(Zhr,ρ)​1r.\displaystyle(d\_{\mathcal{S}}+d\_{\mathcal{A}})^{\frac{d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2}}\frac{(\rho+D)^{d\_{\mathcal{S}}}(2\bar{a})^{d\_{\mathcal{A}}}}{D^{d\_{\mathcal{S}}+d\_{\mathcal{A}}-2}}\bar{g}(\delta,\rho+D)\sum\_{h}\sum\_{r=D}N\_{r}(Z\_{h}^{r,\rho})\frac{1}{r}. |  |

The first inequality holds due to ([C.49](https://arxiv.org/html/2512.14991v1#A3.E49 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")) and ([C.50](https://arxiv.org/html/2512.14991v1#A3.E50 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")). The third inequality holds since |{k:Bhk=B,nhk−1​(Bhk)=0}|≤|𝒫h0|≤(d𝒮+d𝒜)d𝒮+d𝒜2​(ρ+D)d𝒮​(2​a¯)d𝒜Dd𝒮+d𝒜|\{k:B\_{h}^{k}=B,n\_{h}^{k-1}(B\_{h}^{k})=0\}|\leq|\mathcal{P}\_{h}^{0}|\leq(d\_{\mathcal{S}}+d\_{\mathcal{A}})^{\frac{d\_{\mathcal{S}}+d\_{\mathcal{A}}}{2}}\frac{(\rho+D)^{d\_{\mathcal{S}}}(2\bar{a})^{d\_{\mathcal{A}}}}{D^{d\_{\mathcal{S}}+d\_{\mathcal{A}}}}, and the last inequality holds due to the fact that ∑B:diam​(B)=r𝕀{center​(B)∈Zhr,ρ}≤Nr​(Zhr,ρ)\sum\_{B:{\rm diam}(B)=r}\mathbb{I}\_{\{{\rm center}(B)\in Z\_{h}^{r,\rho}\}}\leq N\_{r}(Z\_{h}^{r,\rho}). This fact holds since the distance between the centers of two blocks B1B\_{1} and B2B\_{2} with the same diameter rr is at least rr.

Finally, combining ([C.47](https://arxiv.org/html/2512.14991v1#A3.E47 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.48](https://arxiv.org/html/2512.14991v1#A3.E48 "In C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), ([C.11.1](https://arxiv.org/html/2512.14991v1#A3.Ex147 "C.11.1 Proof of Lemma 5.17 ‣ C.11 Technical results modified from [Sinclair et al., 2023] ‣ Appendix C Technical details in Section 5 ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), and noting the definition of g4(.,.)g\_{4}(.,.) in ([5.42](https://arxiv.org/html/2512.14991v1#S5.E42 "In Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")), we verify ([5.41](https://arxiv.org/html/2512.14991v1#S5.E41 "In Lemma 5.17 (Theorem F.3 in (Sinclair et al., 2023)). ‣ 5.4 Regret composition ‣ 5 Regret analysis ‣ Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes")).
∎