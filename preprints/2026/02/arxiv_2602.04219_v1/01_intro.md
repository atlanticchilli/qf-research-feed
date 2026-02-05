---
authors:
- Chung-Han Hsieh
doc_id: arxiv:2602.04219v1
family_id: arxiv:2602.04219
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative
  Systems: A Convex Relaxation with Performance Guarantees This paper was supported
  in part by the National Science and Technology Council (NSTC), Taiwan, under Grants:
  NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.'
url_abs: http://arxiv.org/abs/2602.04219v1
url_html: https://arxiv.org/html/2602.04219v1
venue: arXiv q-fin
version: 1
year: 2026
---


Chung-Han Hsieh
Department of Quantitative Finance, National Tsing Hua University, Hsinchu, Taiwan ().

###### Abstract

This paper investigates the robust optimal control of sampled-data stochastic systems with multiplicative noise and distributional ambiguity. We consider a class of discrete-time optimal control problems where the controller *jointly* selects a feedback policy and a sampling period to maximize the worst-case expected concave utility of the inter-sample growth factor. Modeling uncertainty via a Wasserstein ambiguity set, we confront the structural obstacle of “concave-max” geometry arising from maximizing a concave utility against an adversarial distribution. Unlike standard convex loss minimization, the dual reformulation here requires a minimax interchange within the semi-infinite constraints where the utility’s concavity precludes exact strong duality. To address this, we utilize a general minimax inequality to derive a tractable convex relaxation. Our approach yields a rigorous lower bound that functions as a probabilistic performance guarantee. We establish an explicit, non-asymptotic bound on the resulting duality gap, proving that the approximation error is uniformly controlled by the Lipschitz-smoothness of the stage reward and the diameter of the disturbance support. Furthermore, we introduce necessary and sufficient conditions for *robust viability*, ensuring state positivity invariance across the entire ambiguity set. Finally, we bridge the gap between static optimization and dynamic performance, proving that the optimal value of the relaxation serves as a rigorous deterministic floor for the asymptotic average utility rate almost surely.
The framework is illustrated on a log-optimal portfolio control problem, which serves as a canonical instance of multiplicative stochastic control.

###### keywords:

Stochastic Optimal Control, Distributionally Robust Optimization, Wasserstein Distance, Sampled-Data Control, Multiplicative Systems, Convex Relaxation, Optimal Growth Portfolio

{MSCcodes}

93E20, 93C57, 90C47, 90C34, 93C28, 91G10

## 1 Introduction

This paper investigates the robust optimal control of sampled-data stochastic systems subject to multiplicative noise and distributional ambiguity. Specifically, we consider a class of discrete-time optimal control problems in which the controller jointly selects a feedback policy and a sampling period to maximize the worst-case expected utility of the inter-sample growth factor. By integrating the Wasserstein metric into a sampled-data framework, we develop a distributionally robust control (DRC) strategy that ensures *system viability* (state positivity) and achieves robust performance despite epistemic uncertainty in the disturbance distribution.
Such stochastic systems with multiplicative noise arise naturally in growth-dominated environments and have been studied extensively; see, e.g., [aoki1975control, gershon2001h, farina2000positive, hsieh2023asymptotic].
Related implementation constraints—including sample-and-hold operation, communication losses, and data-driven controller synthesis—have also been widely investigated in networked and learning-based control; see, e.g., [sinopoli2004kalman, hespanha2007survey, coppens2020data].

For concreteness, we use the *Optimal Growth Portfolio* (Kelly) problem in quantitative finance as a running example; see [Kelly\_1956, Breiman\_1961, cover2012elements, karatzas2021portfolio]. In this context, the system state represents wealth, the multiplicative noise represents asset returns, and the sampling period corresponds to the rebalancing frequency. Importantly, finance serves primarily as a concrete instantiation: the central theoretical challenges—specifically, the coupling between control frequency, transaction costs (actuation friction), and distributional robustness—are fundamental to a broad class of engineering and economic systems driven by multiplicative noise; see, e.g., [hsieh2019positive] for related positivity considerations under implementation delays.

### 1.1 Motivation and Literature Review

The classical theory of stochastic optimal control is by now well established; see [pham2009continuous, bertsekas2012dynamic]. Numerous extensions and refinements have since been developed to address modeling complexity and uncertainty. In particular, stochastic systems with multiplicative (random-coefficient) effects have motivated a rich body of modeling and control paradigms; see, e.g., [aoki1975control, gershon2001h]. In parallel, robust formulations based on minimax (worst-case) criteria have been proposed for stochastic control problems; see, e.g., [hinrichsen1998stochastic, gonzalez2002minimax]. It is well known that, in the presence of proportional friction, continuous-time limits of such problems typically lead to singular stochastic control formulations [davis1990portfolio]. By contrast, the sampled-data framework proposed here avoids these singularities while retaining rigorous and tractable performance bounds.

#### Sampled-Data Constraints and Friction

Real-world controllers operate in discrete time via sample-and-hold mechanisms. A central feature of sampled-data control and stochastic rebalancing systems is that the choice of the sampling period nn induces a fundamental trade-off; see [aastrom2013computer, korn2002stochastic].
While classical results primarily address the preservation of stability under sampling, [nesic2004framework], we focus instead on growth and distributional ambiguity.

Indeed, high-frequency control allows for closer tracking of an ideal continuous-time policy, but incurs high accumulated friction (actuation costs), which in our framework is captured through the state-dependent inter-sample growth factor Φn\Phi\_{n}. Conversely, low-frequency control reduces frictional costs but increases discretization error and exposure to open-loop drift.
As a result, the sampling decision directly affects Φn\Phi\_{n} through both disturbance aggregation and accumulated friction, making the control and sampling period choices structurally non-separable in Φn\Phi\_{n}.
Foundational results on sampled-data systems with stochastic sampling periods can be traced back to [de1988stationary], while LMI-based approaches for multiplicative-noise control were developed in [el1995state]. Recent applications have begun to treat the sampling period itself as a decision variable [kuhn2010analysis, wong2023frequency, hsieh2023asymptotic].
These methods build upon earlier theoretical frameworks for robust growth optimality under moment uncertainty [rujeerapaiboon2016robust], yet they typically assume that the driving disturbance distribution is perfectly known.

#### Distributional Ambiguity

Distributionally robust optimization (DRO) provides a principled framework for hedging against model misspecification by optimizing against an ambiguity set of probability measures. Such ambiguity sets can be constructed using a variety of metrics, including the Prohorov metric [erdougan2006ambiguous], box-type convex polyhedral uncertainty [ben2009robust], Kullback-Leibler divergence [ben2013robust, hu2013kullback], and moment-based descriptions [delage2010distributionally]. In this work, we focus on Wasserstein ambiguity sets, which are particularly well-suited for data-driven settings and admit finite-sample performance guarantees and asymptotic consistency under mild conditions [mohajerin2018data, blanchet2019quantifying, gao2023distributionally].

In the multiperiod Markov decision process literature, Wasserstein-based distributionally robust control has been studied in [yang2020wasserstein], where a Bellman operator reformulation yields a contraction mapping and enables multi-stage out-of-sample guarantees.
Recent extensions have addressed tractability and partial observability in linear–quadratic settings via approximation techniques; see, e.g., [hakobyan2024wasserstein].

In parallel, Wasserstein DRO has also been employed in growth-optimal decision problems arising in finance, leading to robust “Wasserstein–Kelly” rules; see, e.g., [rujeerapaiboon2016robust, li2023wasserstein, hsieh2023solving]. However, these formulations typically abstract away from transaction costs and from the strategic choice of the rebalancing horizon—two features that are central under sampled-data implementation and directly couple control actions with the sampling decision. In contrast, our setting involves concave utility maximization for state-multiplicative systems, where the standard convex–concave structure required for minimax equality generally fails, and exact saddle-point reformulations are unavailable.

#### The Concave-Max Geometry

Maximizing concave utilities is closely connected to risk-sensitive stochastic control; see, e.g., [whittle1990risk, fleming1995risk]. In that literature, exponential (entropic) utilities often yield tractable dynamic programming recursions, whereas general concave utilities under distributional ambiguity—as considered here—require fundamentally different techniques.

A key theoretical gap arises when applying standard Wasserstein DRO machinery to utility maximization for state-multiplicative systems. Classical finite-sample Wasserstein DRO results, e.g., [mohajerin2018data, gao2023distributionally, kuhn2025distributionally], are predominantly developed for minimizing a convex loss function, a setting that guarantees minimax *equality* via Sion’s Minimax Theorem under the usual convexity–concavity assumptions. In contrast, in our setting the stage utility is concave in the disturbance, and tractability hinges on a minimax interchange embedded within the semi-infinite constraints of the dual representation. Because the required convex–concave conditions fail for this constraint-level interchange, an exact equality is generally unavailable. We therefore rely on the general minimax inequality to construct a conservative convex relaxation that yields a rigorous lower bound on the worst-case expected utility, together with an explicit non-asymptotic bound on the relaxation gap induced by this interchange.

### 1.2 Contributions

To the best of our knowledge, this is the first framework to unify frequency-aware sampled-data robust control with Wasserstein distributional robustness for multiplicative systems. Our specific contributions are as follows:

*A Unified Sampled-Data DRO Formulation:* We formulate the joint optimization of the control input uu and sampling period nn as a worst-case expected utility maximization problem. We introduce the concept of *Robust Viability* (Lemma [2.7](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem7 "Lemma 2.7 (Robust Viability Condition). ‣ 2.6 Robust Viability and Admissible Controls ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), a rigorous invariance condition ensuring that the system state remains strictly positive for all distributions within the Wasserstein ambiguity set, a prerequisite for the well-posedness of the utility maximization criterion. From a control-theoretic perspective, the robust viability constraint plays a role analogous to safety invariance in multiplicative systems subject to model uncertainty.

*Tractable Relaxation via Minimax Inequalities with Probabilistic Guarantees:* Addressing the “Concave-Max” difficulty, we derive a computationally tractable convex relaxation of the infinite-dimensional control problem (Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")). In contrast to standard DRO results that typically achieve exact reformulation via minimax equality, we rigorously frame our solution as a *lower bound* on the true optimal value, utilizing a general minimax inequality. Then, Lemma [3.13](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem13 "Lemma 3.13 (Probabilistic Performance Guarantee). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") provides a probabilistic guarantee showing that this conservatism yields a valid lower confidence bound on the true performance. In safety-critical control, maximizing the floor is often preferred over maximizing the mean.

*Long-Run Performance Guarantees:* Bridging the gap between static optimization and dynamic performance, we establish a theoretical link between the solution of the convex relaxation and the asymptotic behavior of the system (Theorem [3.15](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem15 "Theorem 3.15 (Long-Run Average Utility Guarantee). ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")). We prove that, under ergodic assumptions, the optimal value of our tractable formulation serves as a deterministic floor for the long-run average utility rate almost surely.
For the specific case of log-utility, this result guarantees a certified floor for the asymptotic capital growth rate, providing a rigorous theoretical justification for the rolling-horizon implementation; see Corollary [3.17](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem17 "Corollary 3.17 (Long-Run Growth Rate Guarantee). ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."). This result connects our finite-horizon robust optimization to the theory of ergodic control; see, e.g., [arapostathis1993discrete, borkar1988control].

*Explicit Non-Asymptotic Duality Gap Analysis:*
We provide a theoretical certificate for the quality of our approximation. In Proposition [3.7](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem7 "Proposition 3.7 (Minimax Duality Gap Bound). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), we derive an explicit, non-asymptotic upper bound on the minimax duality gap. We show that this gap scales with the Lipschitz smoothness of the stage reward function and the diameter of the disturbance support, but is independent of the ambiguity radius. This result justifies the use of the convex relaxation by quantifying the maximum potential suboptimality.

*Empirical Validation and Performance Analysis:* We demonstrate the practical efficacy of the framework on a log-optimal portfolio control problem using a dataset of major large-cap S&P 500 assets. By implementing the distributionally robust controller via a cutting-plane scheme, we show that jointly optimizing the sampling period and the feedback policy significantly outperforms standard market benchmarks in terms of downside risk and risk-adjusted returns.

The remainder of this paper is structured as follows. Section [2](https://arxiv.org/html/2602.04219v1#S2 "2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") details the model components. Section [3](https://arxiv.org/html/2602.04219v1#S3 "3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") presents our main theoretical results, including the tractable reformulation, the duality gap analysis, and various performance guarantees. Section [4](https://arxiv.org/html/2602.04219v1#S4 "4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") presents an illustrative example in quantitative finance, and Section [5](https://arxiv.org/html/2602.04219v1#S5 "5 Conclusion ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") concludes the paper.

## 2 Preliminaries and Problem Formulation

This section formulates a class of sampled-data stochastic *multiplicative* control systems under distributional ambiguity.

### 2.1 Notation

Throughout the paper, ℝ\mathbb{R} denotes the set of real numbers, ℝ+\mathbb{R}\_{+} the set of nonnegative real numbers, and ℝ¯:=ℝ∪{−∞,∞}\overline{\mathbb{R}}:=\mathbb{R}\cup\{-\infty,\infty\} the extended reals.
All random objects are defined on a probability space (Ω,ℱ,ℙ).(\Omega,\mathcal{F},\mathbb{P}).
The notation ∥⋅∥\|\cdot\| denotes the ℓr\ell\_{r}-norm on ℝk\mathbb{R}^{k} (where dimension kk is determined by context) for a fixed r∈[1,∞]r\in[1,\infty] chosen throughout the paper. We write ∥⋅∥∗\|\cdot\|\_{\*} for the dual norm associated with ∥⋅∥\|\cdot\|, defined as ‖z‖∗:=supx∈ℝk{z⊤​x:‖x‖≤1}\|z\|\_{\*}:=\sup\_{x\in\mathbb{R}^{k}}\{z^{\top}x:\|x\|\leq 1\} for z∈ℝkz\in\mathbb{R}^{k}.
We denote by δx\delta\_{x} the Dirac measure concentrating unit mass at x.x. The product of two probability distributions ℙ1\mathbb{P}\_{1} and ℙ2\mathbb{P}\_{2} on 𝔛1\mathfrak{X}\_{1} and 𝔛2\mathfrak{X}\_{2}, respectively, is the distribution ℙ1⊗ℙ2\mathbb{P}\_{1}\otimes\mathbb{P}\_{2} on 𝔛1×𝔛2.\mathfrak{X}\_{1}\times\mathfrak{X}\_{2}.

### 2.2 Sampled-Data Multiplicative Dynamics

Consider a discrete-time stochastic control system with a fixed sampling period n≥1n\geq 1. Let k∈{0,1,2,…}k\in\{0,1,2,\dots\} denote the discrete time index, which corresponds to the physical time interval [k​n,(k+1)​n)[kn,(k+1)n). We denote the scalar system state at the beginning of the kkth interval by Vk:=V​(k​n)∈ℝ+V\_{k}:=V(kn)\in\mathbb{R}\_{+}, and the control input by uk∈𝒰⊂ℝmu\_{k}\in\mathcal{U}\subset\mathbb{R}^{m}. The control is implemented via a *zero-order hold* mechanism, remaining constant throughout the interval [k​n,(k+1)​n)[kn,(k+1)n). The system evolves according to the *multiplicative* state dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | Vk+1=Vk​Φn​(uk,𝒳k,n),k=0,1,2,…,\displaystyle V\_{k+1}=V\_{k}\,\Phi\_{n}(u\_{k},\mathcal{X}\_{k,n}),\qquad k=0,1,2,\dots, |  |

where 𝒳k,n\mathcal{X}\_{k,n} represents the *aggregated exogenous input (disturbance)* over the kkth interval, taking values in a compact set 𝔛n⊂ℝd\mathfrak{X}\_{n}\subset\mathbb{R}^{d}. The function Φn:𝒰×𝔛n→(0,∞)\Phi\_{n}:\mathcal{U}\times\mathfrak{X}\_{n}\to(0,\infty) is the state-transition map, representing the inter-sample *growth factor*. This function captures the coupled effects of the control decision and the uncertainty, implicitly accounting for actuation friction (e.g., efficiency losses, budget costs, etc.) and the multiplicative forcing of the external environment.

###### Remark 2.1 (Dimensionality Mismatch).

The formulation explicitly allows for distinct control and disturbance dimensions (m≠dm\neq d). This flexibility captures diverse scenarios, such as *under-actuation* (m<dm<d), where a low-dimensional control (e.g., a scalar leverage ratio) faces high-dimensional noise, or *redundancy* (m>dm>d), such as a large portfolio allocation driven by a few low-dimensional latent factors.

DRO Controlleruk=u∗u\_{k}=u^{\*} n=n∗n=n^{\*}ZOHu​(t)≡uku(t)\equiv u\_{k}Data Buffer/HistoryMultiplicative updateVk+1=Vk​Φn​(uk,𝒳k,n)V\_{k+1}=V\_{k}\,\Phi\_{n}(u\_{k},\mathcal{X}\_{k,n})Aggregatorexogenous disturbances on [tk,tk+1)[t\_{k},t\_{k+1}) ↦𝒳k,n\mapsto\ \mathcal{X}\_{k,n}Samplertk+1=tk+nt\_{k+1}=t\_{k}+n*Discrete-time decision**Inter-sample environment*u∗u^{\*}uku\_{k}𝔽^n\widehat{\mathbb{F}}\_{n}Disturbances on [tk,tk+1)[t\_{k},t\_{k+1})𝒳k,n\mathcal{X}\_{k,n}𝒳^n(j)\widehat{\mathcal{X}}\_{n}^{(j)}Vk+1V\_{k+1}Vk+1V\_{k+1}

Figure 1: Schematic of the sampled-data loop. The analysis uses the sampled state Vk=V​(tk)V\_{k}=V(t\_{k}) and an aggregated disturbance 𝒳k,n\mathcal{X}\_{k,n} over [tk,tk+1)[t\_{k},t\_{k+1}) where tk=k​n.t\_{k}=kn.

### 2.3 Performance Criterion and State Positivity

Let U:ℝ+→ℝU:\mathbb{R}\_{+}\to\mathbb{R} be a concave, non-decreasing utility function.
We measure performance over a sampling period by the *stage reward* given by
rn​(u,x):=U​(Φn​(u,x)).r\_{n}(u,x):=U(\Phi\_{n}(u,x)).
A canonical example of a risk-averse growth factor corresponds to the logarithmic utility U​(t)=log⁡tU(t)=\log t.

To ensure the problem is well-posed despite the uncertainty, we enforce a viability constraint.
Fix a viability margin η>0\eta>0 such that [η,∞)⊆dom​(U)[\eta,\infty)\subseteq\mathrm{dom}(U). We define the *set of
admissible controls* as:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | 𝒰v​(n;η):={u∈𝒰:Φn​(u,x)≥η,∀x∈𝔛n}.\mathcal{U}\_{\rm v}(n;\eta):=\big\{u\in\mathcal{U}:\Phi\_{n}(u,x)\geq\eta,\quad\forall x\in\mathfrak{X}\_{n}\big\}. |  |

This condition guarantees that the stage reward rn​(u,x)r\_{n}(u,x) is well-defined and finite uniformly over the disturbance support 𝔛n\mathfrak{X}\_{n}.

### 2.4 Standing Assumptions on Growth Factor

To ensure computational tractability and derive an explicit non-asymptotic bound on the duality gap, we impose the following structural assumptions on the system data and the utility function.

{assumption}

[Regularity and Smoothness]
For each fixed sampling period n≥1n\geq 1, we assume the following conditions:

1. (A1)

   (*Compactness*) The admissible control set 𝒰⊂ℝm\mathcal{U}\subset\mathbb{R}^{m} is nonempty, compact, and convex. The disturbance support 𝔛n\mathfrak{X}\_{n} is nonempty and compact.
2. (A2)

   (*Continuity and Separate Concavity*)
   The stage reward map
   (u,x)↦rn​(u,x)(u,x)\mapsto r\_{n}(u,x)
   is continuous and concave in uu for each x∈𝔛nx\in\mathfrak{X}\_{n}, and concave in xx on conv⁡(𝔛n)\operatorname{conv}(\mathfrak{X}\_{n}) for each u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), where conv​(⋅){\rm conv}(\cdot) denotes the convex hull.
3. (A3)

   (*Uniform LnL\_{n}-Smoothness*) For each u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), the map x↦rn​(u,x)x\mapsto r\_{n}(u,x) is differentiable on 𝔛n\mathfrak{X}\_{n} and its gradient ∇xrn​(u,x)\nabla\_{x}r\_{n}(u,x) satisfies a uniform Lipschitz condition: there exists a constant Ln>0L\_{n}>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | supu∈𝒰v​(n;η)supx,y∈𝔛nx≠y‖∇xrn​(u,x)−∇xrn​(u,y)‖∗‖x−y‖≤Ln.\sup\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\ \sup\_{\begin{subarray}{c}x,y\in\mathfrak{X}\_{n}\\ x\neq y\end{subarray}}\frac{\big\|\nabla\_{x}r\_{n}(u,x)-\nabla\_{x}r\_{n}(u,y)\big\|\_{\*}}{\|x-y\|}\leq L\_{n}. |  |

###### Remark 2.2.

Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A2) preserves the concave-max character of the problem. A sufficient condition for (A2) is that Φn​(u,x)\Phi\_{n}(u,x) is concave in (u,x)(u,x) and UU is concave and nondecreasing on [η,∞)[\eta,\infty). Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A3) is the only assumption linking the duality gap bound to the specific choice of utility. The following example demonstrates that Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A3) holds for the affine-logarithmic case.

###### Example 2.3 (Log-Optimal Portfolio Control).

Let u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta) denote the vector of portfolio weights invested in risky assets for some η>0\eta>0.
Consider the affine growth factor (common in portfolio optimization, e.g., see [hsieh2023solving]) Φn​(u,x)=u⊤​x+cn​(u)\Phi\_{n}(u,x)=u^{\top}x+c\_{n}(u), and the utility U​(y)=log⁡(y)U(y)=\log(y). The stage reward is
rn​(u,x)=log⁡(u⊤​x+cn​(u)).r\_{n}(u,x)=\log(u^{\top}x+c\_{n}(u)).
The gradient with respect to the disturbance xx is
∇xrn​(u,x)=uu⊤​x+cn​(u)=uΦn​(u,x).\nabla\_{x}r\_{n}(u,x)=\frac{u}{u^{\top}x+c\_{n}(u)}=\frac{u}{\Phi\_{n}(u,x)}.
Note that since u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), we have Φ¯n​(u):=minx∈𝔛n⁡Φn​(u,x)≥η\underline{\Phi}\_{n}(u):=\min\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x)\geq\eta.
Thus, for any x,y∈𝔛nx,y\in\mathfrak{X}\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∇xrn​(u,x)−∇xrn​(u,y)‖∗\displaystyle\|\nabla\_{x}r\_{n}(u,x)-\nabla\_{x}r\_{n}(u,y)\|\_{\*} | =‖u​(1Φn​(u,x)−1Φn​(u,y))‖∗\displaystyle=\left\|u\left(\frac{1}{\Phi\_{n}(u,x)}-\frac{1}{\Phi\_{n}(u,y)}\right)\right\|\_{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖u‖∗​|Φn​(u,y)−Φn​(u,x)|Φn​(u,x)​Φn​(u,y)\displaystyle\leq\|u\|\_{\*}\,\frac{|\Phi\_{n}(u,y)-\Phi\_{n}(u,x)|}{\Phi\_{n}(u,x)\,\Phi\_{n}(u,y)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖u‖∗​|u⊤​(y−x)|Φn​(u,x)​Φn​(u,y)\displaystyle=\|u\|\_{\*}\,\frac{|u^{\top}(y-x)|}{\Phi\_{n}(u,x)\,\Phi\_{n}(u,y)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖u‖∗​‖u‖∗​‖y−x‖Φ¯n​(u)2=‖u‖∗2Φ¯n​(u)2​‖x−y‖,\displaystyle\leq\|u\|\_{\*}\,\frac{\|u\|\_{\*}\,\|y-x\|}{\underline{\Phi}\_{n}(u)^{2}}=\frac{\|u\|\_{\*}^{2}}{\underline{\Phi}\_{n}(u)^{2}}\,\|x-y\|, |  |

where the last inequality holds by the generalized Cauchy-Schwarz inequality |u⊤​z|≤‖u‖∗​‖z‖|u^{\top}z|\leq\|u\|\_{\*}\|z\|, e.g., see [beck2017first].
Hence ∇xrn​(u,x)\nabla\_{x}r\_{n}(u,x) is Ln​(u)L\_{n}(u)-Lipschitz on 𝔛n\mathfrak{X}\_{n} with
Ln​(u)=‖u‖∗2Φ¯n​(u)2.L\_{n}(u)=\frac{\|u\|\_{\*}^{2}}{\underline{\Phi}\_{n}(u)^{2}}.
In particular, since Φ¯n​(u)≥η\underline{\Phi}\_{n}(u)\geq\eta, we have Ln​(u)≤‖u‖∗2η2L\_{n}(u)\leq\frac{\|u\|\_{\*}^{2}}{\eta^{2}}, and thus

|  |  |  |
| --- | --- | --- |
|  | supu∈𝒰v​(n;η)Ln​(u)≤supu∈𝒰v​(n;η)‖u‖∗2η2.\sup\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}L\_{n}(u)\leq\sup\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\frac{\|u\|\_{\*}^{2}}{\eta^{2}}. |  |

Since 𝒰v​(n;η)⊆𝒰\mathcal{U}\_{\rm v}(n;\eta)\subseteq\mathcal{U} and 𝒰\mathcal{U} is compact by (A1), supu∈𝒰v​(n;η)‖u‖∗<∞\sup\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\|u\|\_{\*}<\infty; therefore a finite uniform constant Ln:=supu∈𝒰v​(n;η)Ln​(u)L\_{n}:=\sup\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}L\_{n}(u) exists, verifying Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A3) for the affine-log case.

### 2.5 Wasserstein Ambiguity Set

As discussed in Section [1](https://arxiv.org/html/2602.04219v1#S1 "1 Introduction ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), the true disturbance distribution is often unknown. To hedge against this uncertainty without the excessive conservatism of worst-case robust optimization, we model distributional uncertainty using the Wasserstein metric.
Let ℳ​(𝔛n)\mathcal{M}(\mathfrak{X}\_{n}) be the space of all probability distributions 𝔽\mathbb{F} supported on 𝔛n\mathfrak{X}\_{n}.
Since 𝔛n\mathfrak{X}\_{n} is compact, all such distributions have finite moments.

###### Definition 2.4 (Wasserstein Metric).

For p∈[1,∞)p\in[1,\infty) and any two distributions 𝔽1,𝔽2∈ℳ​(𝔛n)\mathbb{F}^{1},\mathbb{F}^{2}\in\mathcal{M}(\mathfrak{X}\_{n}), the *p-Wasserstein metric* Wp:ℳ​(𝔛n)×ℳ​(𝔛n)→ℝW\_{p}:\mathcal{M}(\mathfrak{X}\_{n})\times\mathcal{M}(\mathfrak{X}\_{n})\to\mathbb{R} induced by the ground norm ∥⋅∥\|\cdot\| fixed in Section [2.1](https://arxiv.org/html/2602.04219v1#S2.SS1 "2.1 Notation ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wp​(𝔽1,𝔽2)\displaystyle W\_{p}(\mathbb{F}^{1},\mathbb{F}^{2}) | :=(infΠ∈Γ​(𝔽1,𝔽2)𝔼(𝒳1,𝒳2)∼Π​[‖𝒳1−𝒳2‖p])1/p\displaystyle:=\left(\inf\_{\Pi\in\Gamma(\mathbb{F}^{1},\mathbb{F}^{2})}\mathbb{E}\_{(\mathcal{X}^{1},\mathcal{X}^{2})\sim\Pi}[\|\mathcal{X}^{1}-\mathcal{X}^{2}\|^{p}]\right)^{1/p} |  |

where Γ​(𝔽1,𝔽2)\Gamma(\mathbb{F}^{1},\mathbb{F}^{2}) is the set of joint distributions (couplings) on 𝔛n×𝔛n\mathfrak{X}\_{n}\times\mathfrak{X}\_{n} with marginals 𝔽1\mathbb{F}^{1} and 𝔽2\mathbb{F}^{2}.

Throughout the paper, we fix an order p∈[1,∞)p\in[1,\infty) and use the pp-Wasserstein metric WpW\_{p}. All Wasserstein ambiguity sets in this paper are defined with respect to the same ground norm ∥⋅∥\|\cdot\|.
Consistent with data-driven formulations, e.g., see [calafiore2013direct, mohajerin2018data, yang2020wasserstein],
let 𝒳^n(1),…,𝒳^n(Nn)∈𝔛n\widehat{\mathcal{X}}\_{n}^{(1)},\dots,\widehat{\mathcal{X}}\_{n}^{(N\_{n})}\in\mathfrak{X}\_{n} denote the observed samples of the nn-period aggregated disturbance, where NnN\_{n} is the number of samples available at horizon nn. The associated empirical distribution is
𝔽^n:=1Nn​∑j=1Nnδ𝒳^n(j),\widehat{\mathbb{F}}\_{n}:=\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}\delta\_{\widehat{\mathcal{X}}\_{n}^{(j)}},
where δx\delta\_{x} denotes the Dirac measure at xx.

For a radius ε≥0\varepsilon\geq 0, the *Wasserstein ambiguity set* is defined as the ball of radius ε\varepsilon centered at 𝔽^n\widehat{\mathbb{F}}\_{n}:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | ℬε(p)​(𝔽^n):={𝔽∈ℳ​(𝔛n):Wp​(𝔽,𝔽^n)≤ε}.\displaystyle\mathcal{B}\_{\varepsilon}^{(p)}(\widehat{\mathbb{F}}\_{n}):=\left\{\mathbb{F}\in\mathcal{M}({\mathfrak{X}}\_{n}):W\_{p}(\mathbb{F},\widehat{\mathbb{F}}\_{n})\leq\varepsilon\right\}. |  |

To ensure statistical validity, the ambiguity radii are calibrated specifically for each sampling period as follows.

###### Definition 2.5 (Calibrated Ambiguity Radii).

Fix a global confidence level β∈(0,1)\beta\in(0,1) and a finite candidate set 𝒩⊆ℕ\mathcal{N}\subseteq\mathbb{N}.
For each n∈𝒩n\in\mathcal{N}, choose a radius εn≥0\varepsilon\_{n}\geq 0 such that

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | ℙ​(𝔽true,n∈ℬεn(p)​(𝔽^n))≥1−β|𝒩|,\displaystyle\mathbb{P}\left(\mathbb{F}\_{\mathrm{true},n}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})\right)\geq 1-\frac{\beta}{|\mathcal{N}|}, |  |

where |𝒩||\mathcal{N}| denotes the cardinality of the set 𝒩\mathcal{N}, and 𝔽true,n\mathbb{F}\_{\mathrm{true},n} denotes the true distribution of the generic nn-period aggregated disturbance 𝒳\mathcal{X}.111Such radii can be obtained from concentration bounds, e.g., see [fournier2015rate], under suitable sampling assumptions, or calibrated empirically (e.g., via block bootstrap in the presence of serial dependence).
Consequently, by a union bound,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(⋂n∈𝒩{𝔽true,n∈ℬεn(p)​(𝔽^n)})≥1−β.\mathbb{P}\left(\bigcap\_{n\in\mathcal{N}}\{\mathbb{F}\_{\mathrm{true},n}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})\}\right)\geq 1-\beta. |  |

###### Remark 2.6.

Note that for the generic ball definition, if ε=0\varepsilon=0, then ℬε(p)​(𝔽^n)={𝔽^n}\mathcal{B}\_{\varepsilon}^{(p)}(\widehat{\mathbb{F}}\_{n})=\{\widehat{\mathbb{F}}\_{n}\}, a singleton empirical distribution.

### 2.6 Robust Viability and Admissible Controls

In the context of multiplicative systems, state positivity is a prerequisite for the well-posedness of the performance criterion. Similar to stability or invariance requirements in classical control, see [chen1998linear, farina2000positive], we require the control uu to guarantee that the state trajectory remains strictly positive uniformly over the ambiguity set.

We formalize this via the concept of *robust viability*. Recall the set of admissible controls 𝒰v​(n;η)\mathcal{U}\_{\rm v}(n;\eta) defined in ([2](https://arxiv.org/html/2602.04219v1#S2.E2 "Equation 2 ‣ 2.3 Performance Criterion and State Positivity ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")). The following lemma establishes that this static constraint on the growth factor is sufficient to guarantee dynamic state invariance under distributional uncertainty.

###### Lemma 2.7 (Robust Viability Condition).

Fix a sampling period n≥1n\geq 1. Let V0>0V\_{0}>0. If a control uu is admissible, i.e., u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), then for any ambiguity radius ε≥0\varepsilon\geq 0 and any distribution 𝔽∈ℬε(p)​(𝔽^n)\mathbb{F}\in\mathcal{B}\_{\varepsilon}^{(p)}(\widehat{\mathbb{F}}\_{n}), the state evolution satisfies

|  |  |  |
| --- | --- | --- |
|  | ℙ𝔽​(Vk+1≥η​Vk)=1andℙ𝔽​(Vk+1>0)=1,∀k≥0.\mathbb{P}^{\mathbb{F}}(V\_{k+1}\geq\eta V\_{k})=1\quad\text{and}\quad\mathbb{P}^{\mathbb{F}}(V\_{k+1}>0)=1,\quad\forall k\geq 0. |  |

###### Proof 2.8.

Fix ε≥0\varepsilon\geq 0 and 𝔽∈ℬε(p)​(𝔽^n)\mathbb{F}\in\mathcal{B}\_{\varepsilon}^{(p)}(\widehat{\mathbb{F}}\_{n}). By definition, the ambiguity set is a subset of ℳ​(𝔛n)\mathcal{M}(\mathfrak{X}\_{n}), meaning every feasible distribution is supported on the compact set 𝔛n\mathfrak{X}\_{n}.
Condition u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta) implies that Φn​(u,𝒳)≥η\Phi\_{n}(u,\mathcal{X})\geq\eta holds almost surely with respect to any such 𝔽\mathbb{F}, where 𝒳\mathcal{X} denotes a generic nn-period aggregated disturbance.
Since the dynamics are multiplicative, i.e., Vk+1=Vk​Φn​(u,𝒳)V\_{k+1}=V\_{k}\Phi\_{n}(u,\mathcal{X}), if Vk>0V\_{k}>0, it follows almost surely that Vk+1≥η​VkV\_{k+1}\geq\eta V\_{k}. Given V0>0V\_{0}>0 and η>0\eta>0, strictly positive invariance follows by induction.

While robust viability is a hard constraint, one might consider a probabilistic relaxation. We define this notion to clarify the hierarchy of constraints.

###### Definition 2.9 ((ε,δ)(\varepsilon,\delta)-Viability).

Fix n≥1n\geq 1, ε≥0\varepsilon\geq 0, and δ∈(0,1)\delta\in(0,1). A control u∈𝒰u\in\mathcal{U} is *(ε,δ)(\varepsilon,\delta)-viable* if
inf𝔽∈ℬε(p)​(𝔽^n)ℙ𝔽​(Φn​(u,𝒳)≥η)≥1−δ.\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon}^{(p)}(\widehat{\mathbb{F}}\_{n})}\mathbb{P}^{\mathbb{F}}\big(\Phi\_{n}(u,\mathcal{X})\geq\eta\big)\geq 1-\delta.

###### Remark 2.10.

Unlike robust viability, (ε,δ)(\varepsilon,\delta)-viability does not impose Φn​(u,x)≥η\Phi\_{n}(u,x)\geq\eta uniformly over x∈𝔛nx\in\mathfrak{X}\_{n}.
Consequently, for utilities with a singularity at zero (e.g., U=logU=\log), (ε,δ)(\varepsilon,\delta)-viability alone does not in general ensure that
𝔼𝔽​[U​(Φn​(u,𝒳))]\mathbb{E}^{\mathbb{F}}[U(\Phi\_{n}(u,\mathcal{X}))] is finite for all 𝔽∈ℬε(p)​(𝔽^n)\mathbb{F}\in\mathcal{B}\_{\varepsilon}^{(p)}(\widehat{\mathbb{F}}\_{n}).

The following theorem establishes the hierarchy between the hard robust constraint and the probabilistic chance constraint.

###### Theorem 2.11 (Hierarchy of Viability Conditions).

The following implications hold for a given n≥1n\geq 1:

(i)(i) If u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), then it is (ε,δ)(\varepsilon,\delta)-viable for *all* ε≥0\varepsilon\geq 0 and δ∈(0,1)\delta\in(0,1).

(i​i)(ii) Conversely, if uu is (ε,δ)(\varepsilon,\delta)-viable for every ε≥0\varepsilon\geq 0 and every δ∈(0,1)\delta\in(0,1), then

|  |  |  |
| --- | --- | --- |
|  | infx∈𝔛nΦn​(u,x)≥η.\inf\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x)\geq\eta. |  |

###### Proof 2.12.

(i)(i) If infx∈𝔛nΦn​(u,x)≥η\inf\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x)\geq\eta, then the event {Φn​(u,𝒳)≥η}\{\Phi\_{n}(u,\mathcal{X})\geq\eta\} occurs almost surely under any distribution supported on 𝔛n\mathfrak{X}\_{n}. Thus, its probability is 1 under any distribution supported on 𝔛n\mathfrak{X}\_{n}, satisfying the condition for any δ\delta.

(i​i)(ii) We proceed by contradiction. Suppose uu is (ε,δ)(\varepsilon,\delta)-viable for all ε,δ\varepsilon,\delta, but there exists x∗∈𝔛nx^{\*}\in\mathfrak{X}\_{n} such that Φn​(u,x∗)<η\Phi\_{n}(u,x^{\*})<\eta. Let 𝔽∗=δx∗\mathbb{F}^{\*}=\delta\_{x^{\*}} be the Dirac measure at x∗x^{\*}.
Since x∗∈𝔛nx^{\*}\in\mathfrak{X}\_{n}, 𝔽∗∈ℳ​(𝔛n)\mathbb{F}^{\*}\in\mathcal{M}(\mathfrak{X}\_{n}).
Consider the distance Wp​(𝔽∗,𝔽^n)W\_{p}(\mathbb{F}^{\*},\widehat{\mathbb{F}}\_{n}). Since 𝔛n\mathfrak{X}\_{n} is compact, this distance is finite. Choose an ambiguity radius ε′≥Wp​(𝔽∗,𝔽^n)\varepsilon^{\prime}\geq W\_{p}(\mathbb{F}^{\*},\widehat{\mathbb{F}}\_{n}). Then 𝔽∗∈ℬε′(p)​(𝔽^n)\mathbb{F}^{\*}\in\mathcal{B}\_{\varepsilon^{\prime}}^{(p)}(\widehat{\mathbb{F}}\_{n}).
Under such 𝔽∗\mathbb{F}^{\*}, the event {Φn​(u,𝒳)≥η}\{\Phi\_{n}(u,\mathcal{X})\geq\eta\} has probability zero. This implies

|  |  |  |
| --- | --- | --- |
|  | inf𝔽∈ℬε′(p)​(𝔽^n)ℙ𝔽​(Φn​(u,𝒳)≥η)=0,\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon^{\prime}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\mathbb{P}^{\mathbb{F}}\big(\Phi\_{n}(u,\mathcal{X})\geq\eta\big)=0, |  |

which violates the condition that uu is (ε′,δ)(\varepsilon^{\prime},\delta)-viable for any δ<1\delta<1.

Based on this hierarchy, throughout the remainder of this work we impose the robust viability constraint
u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta) as defined in ([2](https://arxiv.org/html/2602.04219v1#S2.E2 "Equation 2 ‣ 2.3 Performance Criterion and State Positivity ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")).
Since 𝔛n\mathfrak{X}\_{n} is compact and x↦Φn​(u,x)x\mapsto\Phi\_{n}(u,x) is continuous for each fixed uu, this condition is equivalently written as

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | minx∈𝔛n⁡Φn​(u,x)≥η.\displaystyle\min\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x)\geq\eta. |  |

In particular, the minimum is attained. Moreover, if u↦Φn​(u,x)u\mapsto\Phi\_{n}(u,x) is concave for each xx, then
g​(u):=minx∈𝔛n⁡Φn​(u,x)g(u):=\min\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x) is concave as a pointwise infimum of concave functions; hence its superlevel set {u∈𝒰:g​(u)≥η}=𝒰v​(n;η)\{u\in\mathcal{U}:\ g(u)\geq\eta\}=\mathcal{U}\_{\rm v}(n;\eta) is convex.

### 2.7 Distributionally Robust Control Formulation

We are now ready to state the sampled-data distributionally robust control problem. The objective is to maximize the worst-case expected utility of the growth factor over the sampling period.

###### Problem 2.13 (Horizon-Consistent Distributionally Robust Control).

Fix a global confidence level β∈(0,1)\beta\in(0,1) and a viability margin η>0\eta>0.
Let 𝒩⊂ℕ\mathcal{N}\subset\mathbb{N} be a finite candidate set of sampling periods, and for each n∈𝒩n\in\mathcal{N}
construct 𝔽^n\widehat{\mathbb{F}}\_{n} from NnN\_{n} samples and choose εn\varepsilon\_{n} according to Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").
The joint optimization over the sampling period nn and control uu is

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | maxn∈𝒩⁡maxu∈𝒰v​(n;η)​inf𝔽∈ℬεn(p)​(𝔽^n)1n​𝔼𝔽​[U​(Φn​(u,𝒳))].\displaystyle\max\_{n\in\mathcal{N}}\ \max\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\ \inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\ \frac{1}{n}\,\mathbb{E}^{\mathbb{F}}\!\left[U(\Phi\_{n}(u,\mathcal{X}))\right]. |  |

Problem ([6](https://arxiv.org/html/2602.04219v1#S2.E6 "Equation 6 ‣ Problem 2.13 (Horizon-Consistent Distributionally Robust Control). ‣ 2.7 Distributionally Robust Control Formulation ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) is a mixed-integer optimization problem due to the discrete variable nn. However, for a fixed sampling period nn, the problem of maximizing

|  |  |  |
| --- | --- | --- |
|  | inf𝔽∈ℬεn(p)​(𝔽^n)𝔼𝔽​[U​(Φn​(u,𝒳))]\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\,\mathbb{E}^{\mathbb{F}}\left[U(\Phi\_{n}(u,\mathcal{X}))\right] |  |

over u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta) is a concave maximization problem, provided U​(Φn​(u,⋅))U(\Phi\_{n}(u,\cdot)) is concave. The global solution is obtained by solving these finitely many tractable subproblems and selecting the optimal sampling period n∗n^{\*}.

###### Remark 2.14 (Relation to Chance Constraints).

We enforce the robust viability constraint u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta) rather than the probabilistic (ε,δ)(\varepsilon,\delta)-viability constraint. This is a deliberate design choice for tractability: 𝒰v​(n;η)\mathcal{U}\_{\rm v}(n;\eta) is a deterministic convex set, preserving the convexity of the overall problem. In contrast, distributionally robust chance constraints typically induce non-convex feasible sets, which would render the problem computationally intractable. In addition, for logarithmic and other utilities with singular behavior at zero, enforcing Φn​(u,x)≥η>0\Phi\_{n}(u,x)\geq\eta>0 uniformly over 𝔛n\mathfrak{X}\_{n} ensures that the expected utility is finite under all distributions in the ambiguity set, thereby guaranteeing well-posedness of the objective. Relaxing to a distributional chance constraint would require restricting to utilities bounded below, which excludes the classical log utility case.

###### Remark 2.15 (Reduction to Sample Average Approximation).

If the ambiguity radius is set to ε=0\varepsilon=0, the set ℬ0(p)​(𝔽^n)\mathcal{B}\_{0}^{(p)}(\widehat{\mathbb{F}}\_{n}) collapses to the singleton empirical distribution 𝔽^n\widehat{\mathbb{F}}\_{n}. Problem ([6](https://arxiv.org/html/2602.04219v1#S2.E6 "Equation 6 ‣ Problem 2.13 (Horizon-Consistent Distributionally Robust Control). ‣ 2.7 Distributionally Robust Control Formulation ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) then reduces to the Sample Average Approximation (SAA) of the risk-sensitive control problem:

|  |  |  |
| --- | --- | --- |
|  | maxn∈𝒩⁡maxu∈𝒰v​(n;η)⁡1n​1Nn​∑j=1NnU​(Φn​(u,𝒳^n(j))).\max\_{n\in\mathcal{N}}\ \max\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\ \frac{1}{n}\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}U\!\left(\Phi\_{n}\!\left(u,\widehat{\mathcal{X}}\_{n}^{(j)}\right)\right). |  |

This recovers standard expected-utility maximization but retains the hard viability constraint essential for validity.

## 3 Theoretical Results

This section demonstrates that the infinite-dimensional distributionally robust control problem [2.13](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem13 "Problem 2.13 (Horizon-Consistent Distributionally Robust Control). ‣ 2.7 Distributionally Robust Control Formulation ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") can be approximated by a finite dimensional convex program with a concave objective, thereby facilitating computational tractability.

### 3.1 Tractable Formulation

Although our dual derivation shares ingredients with [mohajerin2018data], the polarity of optimization is reversed: we solve a max-min risk-sensitive problem where the objective is concave in the decision variable. Consequently, Sion’s minimax theorem cannot be directly applied to establish strong duality. We instead utilize a general minimax inequality to derive a rigorous lower bound.

###### Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period nn).

Fix a sampling period n∈𝒩n\in\mathcal{N} and let εn≥0\varepsilon\_{n}\geq 0 be the calibrated ambiguity radius defined in Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."). Let p∈[1,∞)p\in[1,\infty) and q=pp−1q=\frac{p}{p-1} with q=∞q=\infty if p=1p=1. A tractable lower bound is given by the optimal value of the following convex program:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (7) |  | Jcvx∗​(n):=\displaystyle J\_{\rm cvx}^{\*}(n):= | supu,λ,sj,zj1n​(−λ​εnp+1Nn​∑j=1Nnsj)\displaystyle\sup\_{u,\lambda,s\_{j},z\_{j}}\frac{1}{n}\left(-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}{s}\_{j}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | minx∈𝔛n⁡[U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j))]−Ωp​(zj,λ)≥sj,∀j=1,…,Nn,\displaystyle{\min\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})\right]-\Omega\_{p}(z\_{j},\lambda)\geq{s}\_{j},\quad\forall j=1,\dots,N\_{n},} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λ≥0,\displaystyle\lambda\geq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | u∈𝒰v​(n;η).\displaystyle u\in\mathcal{U}\_{\rm v}(n;\eta). |  |

where the regularization term Ωp​(zj,λ)\Omega\_{p}(z\_{j},\lambda) is defined as:

|  |  |  |
| --- | --- | --- |
|  | Ωp​(zj,λ):={1q​(p​λ)1−q​‖zj‖∗qif ​p>1,0if ​p=1,‖zj‖∗≤λ,∞otherwise,\Omega\_{p}(z\_{j},\lambda):=\begin{cases}\frac{1}{q}(p\lambda)^{1-q}\|z\_{j}\|\_{\*}^{q}&\text{if }p>1,\\ 0&\text{if }p=1,\,\|z\_{j}\|\_{\*}\leq\lambda,\\ \infty&\text{otherwise},\end{cases} |  |

where zj∈ℝdz\_{j}\in\mathbb{R}^{d} are dual variables and ∥⋅∥∗\|\cdot\|\_{\*} is the dual norm associated with the original norm ∥⋅∥\|\cdot\| used in the Wasserstein metric. For p>1p>1, we adopt the extended-value convention at λ=0\lambda=0: Ωp​(0,0)=0\Omega\_{p}(0,0)=0 and Ωp​(z,0)=+∞\Omega\_{p}(z,0)=+\infty for z≠0z\neq 0.

###### Proof 3.2.

Using the Wasserstein distance from Definition [2.4](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem4 "Definition 2.4 (Wasserstein Metric). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), we first re-express the inner minimization problem of Problem [2.13](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem13 "Problem 2.13 (Horizon-Consistent Distributionally Robust Control). ‣ 2.7 Distributionally Robust Control Formulation ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") via Lagrangian dualization. Specifically, we observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (8) |  | inf𝔽∈ℬεn(p)​(𝔽^n)𝔼𝔽​[U​(Φn​(u,𝒳))]\displaystyle\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\mathbb{E}^{\mathbb{F}}\left[U(\Phi\_{n}(u,\mathcal{X}))\right] | ={infΠ,𝔽∫U​(Φn​(u,𝒳))​𝑑𝔽​(𝒳)s.t. ​Π∈Γ​(𝔽,𝔽^n),∫‖𝒳−𝒳′‖p​𝑑Π​(𝒳,𝒳′)≤εnp,\displaystyle=\begin{cases}\displaystyle\inf\_{\Pi,\mathbb{F}}\displaystyle\int U(\Phi\_{n}(u,\mathcal{X}))\,d\mathbb{F}(\mathcal{X})\\ \text{s.t. }\Pi\in\Gamma(\mathbb{F},\widehat{\mathbb{F}}\_{n}),\\ \qquad\int\|\mathcal{X}-\mathcal{X}^{\prime}\|^{p}\,d\Pi(\mathcal{X},\mathcal{X}^{\prime})\leq\varepsilon\_{n}^{p},\end{cases} |  |

where Π\Pi is a joint distribution on 𝔛n×𝔛n\mathfrak{X}\_{n}\times\mathfrak{X}\_{n} with marginals 𝔽\mathbb{F} and 𝔽^n\widehat{\mathbb{F}}\_{n}.
Given that the empirical distribution 𝔽^n\widehat{\mathbb{F}}\_{n} is discrete, by the standard disintegration theorem, e.g., see [mohajerin2018data], any coupling Π\Pi admits a decomposition into conditional distributions 𝔽j\mathbb{F}\_{j} supported on 𝔛n\mathfrak{X}\_{n}, associated with each sample 𝒳^n(j)\widehat{\mathcal{X}}\_{n}^{(j)}. Consequently, the infinite-dimensional optimization problem ([8](https://arxiv.org/html/2602.04219v1#S3.E8 "Equation 8 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) over probability measures reduces to a finite sum of subproblems:

|  |  |  |
| --- | --- | --- |
|  | {inf𝔽j∈ℳ​(𝔛n),∀j1Nn​∑j=1Nn∫U​(Φn​(u,𝒳))​𝑑𝔽j​(𝒳)s.t. ​1Nn​∑j=1Nn∫‖𝒳−𝒳^n(j)‖p​𝑑𝔽j​(𝒳)≤εnp\displaystyle\begin{cases}\displaystyle\inf\_{\mathbb{F}\_{j}\in\mathcal{M}(\mathfrak{X}\_{n}),\,\forall j}\,\frac{1}{N\_{n}}\displaystyle\sum\_{j=1}^{N\_{n}}\int U(\Phi\_{n}(u,\mathcal{X}))\,d\mathbb{F}\_{j}(\mathcal{X})\\ \text{s.t. }\displaystyle\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}\int\|\mathcal{X}-\widehat{\mathcal{X}}\_{n}^{(j)}\|^{p}\,d\mathbb{F}\_{j}(\mathcal{X})\leq\varepsilon\_{n}^{p}\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | =supλ≥0inf𝔽j∈ℳ​(𝔛n),∀j{−λ​εnp+1Nn​∑j=1Nn∫[U​(Φn​(u,𝒳))+λ​‖𝒳−𝒳^n(j)‖p]​𝑑𝔽j}\displaystyle=\sup\_{\lambda\geq 0}\;\inf\_{\mathbb{F}\_{j}\in\mathcal{M}(\mathfrak{X}\_{n}),\,\forall j}\left\{-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}\int\left[U(\Phi\_{n}(u,\mathcal{X}))+\lambda\|\mathcal{X}-\widehat{\mathcal{X}}\_{n}^{(j)}\|^{p}\right]d{\mathbb{F}\_{j}}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | =supλ≥0{−λ​εnp+1Nn​∑j=1Nninfx∈𝔛n[U​(Φn​(u,x))+λ​‖x−𝒳^n(j)‖p]},\displaystyle=\sup\_{\lambda\geq 0}\left\{-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}\inf\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+\lambda\|x-\widehat{\mathcal{X}}\_{n}^{(j)}\|^{p}\right]\right\}, |  |

where Equality ([9](https://arxiv.org/html/2602.04219v1#S3.E9 "Equation 9 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) holds as follows: If εn>0\varepsilon\_{n}>0, the primal problem admits a strictly feasible point 𝔽^n\widehat{\mathbb{F}}\_{n} with
Wp​(𝔽^n,𝔽^n)=0<εnW\_{p}(\widehat{\mathbb{F}}\_{n},\widehat{\mathbb{F}}\_{n})=0<\varepsilon\_{n}, hence strong duality follows; see [mohajerin2018data, gao2023distributionally].
If εn=0\varepsilon\_{n}=0, then ℬεn(p)​(𝔽^n)={𝔽^n}\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})=\{\widehat{\mathbb{F}}\_{n}\} and the reduction follows directly.

Introducing epigraphical auxiliary variables sj{s}\_{j} for j=1,…,Nnj=1,\dots,N\_{n}, we rewrite the problem as:

|  |  |  |
| --- | --- | --- |
|  | {supλ,sj−λ​εnp+1Nn​∑j=1Nnsjs.t. ​infx∈𝔛n[U​(Φn​(u,x))+λ​‖x−𝒳^n(j)‖p]≥sj,∀jλ≥0\displaystyle\begin{cases}\displaystyle\sup\_{\lambda,{s}\_{j}}\,-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}{s}\_{j}\\ \text{s.t. }\displaystyle\inf\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+\lambda\|x-\widehat{\mathcal{X}}\_{n}^{(j)}\|^{p}\right]\geq{s}\_{j},\quad\forall j\\ \qquad\lambda\geq 0\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | ={supλ,sj−λ​εnp+1Nn​∑j=1Nnsjs.t. ​infx∈𝔛n[U​(Φn​(u,x))+supzj{zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)}]≥sj,∀jλ≥0\displaystyle=\begin{cases}\displaystyle\sup\_{\lambda,{s}\_{j}}\,-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}{s}\_{j}\\ \text{s.t. }{\displaystyle\inf\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+\sup\_{z\_{j}}\left\{z\_{j}^{\top}\left(x-\widehat{\mathcal{X}}\_{n}^{(j)}\right)-\Omega\_{p}(z\_{j},\lambda)\right\}\right]\geq{s}\_{j},\quad\forall j}\\ \qquad\lambda\geq 0\end{cases} |  |

where the regularization term Ωp​(zj,λ)\Omega\_{p}(z\_{j},\lambda) satisfies

|  |  |  |
| --- | --- | --- |
|  | Ωp​(zj,λ):={1q​(p​λ)1−q​‖zj‖∗qif ​p>1,0if ​p=1,‖zj‖∗≤λ,∞otherwise\Omega\_{p}(z\_{j},\lambda):=\begin{cases}\frac{1}{q}(p\lambda)^{1-q}\|z\_{j}\|\_{\*}^{q}&\text{if }p>1,\\ 0&\text{if }p=1,\,\|z\_{j}\|\_{\*}\leq\lambda,\\ \infty&\text{otherwise}\end{cases} |  |

which is derived from the scaled convex conjugate of the power norm function.
Here, the last equality ([11](https://arxiv.org/html/2602.04219v1#S3.E11 "Equation 11 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) holds by using the biconjugate identity λ​‖x−𝒳^j‖p=supzj{zj⊤​(x−𝒳^j)−Ωp​(zj,λ)}\lambda\|x-\widehat{\mathcal{X}}\_{j}\|^{p}=\sup\_{z\_{j}}\{z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{j})-\Omega\_{p}(z\_{j},\lambda)\}, which is a direct application of the Fenchel–Moreau Theorem, e.g., see [beck2017first]. Hence, we rewrite ([11](https://arxiv.org/html/2602.04219v1#S3.E11 "Equation 11 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) further as follows:

|  |  |  |
| --- | --- | --- |
|  | {supλ,sj−λ​εnp+1Nn​∑j=1Nnsjs.t. ​infx∈𝔛nsupzj[U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)]≥sj,∀jλ≥0\displaystyle\begin{cases}\displaystyle\sup\_{\lambda,{s}\_{j}}\,-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}{s}\_{j}\\ \text{s.t. }\displaystyle\inf\_{x\in\mathfrak{X}\_{n}}\;\displaystyle\sup\_{z\_{j}}\left[U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right]\geq{s}\_{j},\quad\forall j\\ \qquad\lambda\geq 0\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | ≥{supλ,sj−λ​εnp+1Nn​∑j=1Nnsjs.t. ​supzjinfx∈𝔛n[U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)]≥sj,∀jλ≥0\displaystyle\geq\begin{cases}\displaystyle\sup\_{\lambda,{s}\_{j}}\,-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}{s}\_{j}\\ \text{s.t. }{{\displaystyle\sup\_{z\_{j}}\;\inf\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right]\geq{s}\_{j},\quad\forall j}}\\ \qquad\lambda\geq 0\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | ={supλ,sj,zj−λ​εnp+1Nn​∑j=1Nnsjs.t. ​infx∈𝔛n[U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j))]−Ωp​(zj,λ)≥sj,∀jλ≥0\displaystyle=\begin{cases}\displaystyle\sup\_{\lambda,{s}\_{j},z\_{j}}\,-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}{s}\_{j}\\ \text{s.t. }\ \displaystyle\inf\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})\right]-\Omega\_{p}(z\_{j},\lambda)\geq{s}\_{j},\quad\forall j\\ \qquad\lambda\geq 0\\ \end{cases} |  |

where Inequality ([12](https://arxiv.org/html/2602.04219v1#S3.E12 "Equation 12 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) follows from the general minimax inequality (inf𝒳supzj[⋅]≥supzjinf𝒳[⋅]\inf\_{\mathcal{X}}\sup\_{z\_{j}}[\cdot]\geq\sup\_{z\_{j}}\inf\_{\mathcal{X}}[\cdot]) applied to the constraint’s core term.
Note that strict equality in ([12](https://arxiv.org/html/2602.04219v1#S3.E12 "Equation 12 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) is not guaranteed because the objective is concave in xx (by Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), failing the convexity requirement for Sion’s theorem in the minimization variable. Thus, enforcing the stronger condition (the last system above) yields a valid lower bound.

Since 𝔛n\mathfrak{X}\_{n} is compact and the objective is continuous, the Weierstrass Extreme Value Theorem indicates that the infimum is attained. Substituting this back into the maximization problem over uu yields Problem ([7](https://arxiv.org/html/2602.04219v1#S3.E7 "Equation 7 ‣ Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")). Since the feasible set is closed and the domain 𝒰v​(n;η)\mathcal{U}\_{\rm v}(n;\eta) is compact, the existence of an optimal solution is guaranteed.

To complete the proof, it remains to show that problem above is a convex program. Note that the objective function is linear in λ,sj\lambda,s\_{j}. The set 𝒰v​(n;η)\mathcal{U}\_{\rm v}(n;\eta) is convex. The constraint

|  |  |  |
| --- | --- | --- |
|  | Gj​(u,zj,λ):=minx∈𝔛n⁡[U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j))]−Ωp​(zj,λ)≥sjG\_{j}(u,z\_{j},\lambda):=\min\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})\right]-\Omega\_{p}(z\_{j},\lambda)\geq s\_{j} |  |

defines a convex feasible set. The first term is a pointwise minimum of functions concave in (u,zj)(u,z\_{j}), which is concave. (since U​(Φn​(⋅,x))U(\Phi\_{n}(\cdot,x)) is concave by Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") and the term linear in zjz\_{j} is concave, and regularization term Ωp​(zj,λ)∝‖z‖∗qλq−1\Omega\_{p}(z\_{j},\lambda)\propto\tfrac{\|z\|\_{\*}^{q}}{\lambda^{q-1}} is the perspective function of the convex power function g​(z)=‖z‖∗qg(z)=\|z\|\_{\*}^{q}. Since perspective functions preserve convexity, −Ωp​(zj,λ)-\Omega\_{p}(z\_{j},\lambda) is concave). The pointwise minimum of concave functions is concave. Thus, GjG\_{j} is a sum of concave functions, and the superlevel set condition Gj​(u,zj)≥sjG\_{j}(u,z\_{j})\geq s\_{j} defines a convex set. For p=1p=1, the constraint reduces to ‖zj‖∗≤λ\|z\_{j}\|\_{\*}\leq\lambda, which is also convex.
Moreover, the constraint λ≥0\lambda\geq 0 is convex. Since the intersection of two convex sets preserves convexity, the overall problem is a convex program.

###### Remark 3.3 (On the Duality and the Resulting Gap).

(i)(i) The derivation of the tractable formulation in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") involves a critical minimax interchange (see Inequality ([12](https://arxiv.org/html/2602.04219v1#S3.E12 "Equation 12 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."))). Because the utility U​(Φn​(u,x))U(\Phi\_{n}(u,x)) is concave in the minimization variable xx (under Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), the convexity conditions for Sion’s Minimax Theorem are not met, precluding an exact equality. Consequently, the use of the general minimax inequality is necessary, and the formulation in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") furnishes a rigorous *lower bound* on the true optimal value. The magnitude of this duality gap is intrinsically linked to the degree of smoothness of stage reward x↦U​(Φn​(u,x))x\mapsto U(\Phi\_{n}(u,x)) over the support set 𝔛n\mathfrak{X}\_{n}, uniformly over uu.
(i​i)(ii) The convex relaxation in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") is *exact* whenever the stage reward x↦rn​(u;x)x\mapsto r\_{n}(u;x) is affine on 𝔛n\mathfrak{X}\_{n}; see Proposition [3.7](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem7 "Proposition 3.7 (Minimax Duality Gap Bound). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").

The next corollary indicates that the semi-infinite convex relaxation above can be further expressed in a finite convex formulation.

###### Corollary 3.4 (Reduction of Semi-Infinite Constraint).

Fix p∈[1,∞)p\in[1,\infty), n∈𝒩n\in\mathcal{N}, and let εn\varepsilon\_{n} be as in Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."). The convex approximation problem ([7](https://arxiv.org/html/2602.04219v1#S3.E7 "Equation 7 ‣ Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) is equivalent to the following optimization problem:

|  |  |  |
| --- | --- | --- |
|  | supu,λ,sj,zj1n​(−λ​εnp+1Nn​∑j=1Nnsj)\displaystyle\sup\_{u,\lambda,s\_{j},z\_{j}}\,\frac{1}{n}\,\left(-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}{s}\_{j}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | s.t. ​minx∈Ext⁡(conv⁡(𝔛n))⁡[U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j))]−Ωp​(zj,λ)≥sj,∀j,\displaystyle\text{s.t. }\ \min\_{x\in\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n}))}\left[U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})\right]-\Omega\_{p}(z\_{j},\lambda)\geq{s}\_{j},\quad\forall j, |  |
|  |  |  |
| --- | --- | --- |
|  | λ≥0,\displaystyle\qquad\lambda\geq 0, |  |
|  |  |  |
| --- | --- | --- |
|  | u∈𝒰v​(n;η),\displaystyle\qquad u\in\mathcal{U}\_{\rm v}(n;\eta), |  |

where Ext⁡(conv⁡(𝔛n))\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n})) is the set of extreme points of the convex hull of the compact support 𝔛n\mathfrak{X}\_{n}.
Moreover, if the support set 𝔛n\mathfrak{X}\_{n} is a convex polytope, then Ext⁡(conv⁡(𝔛n))=Ext⁡(𝔛n)\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n}))=\operatorname{Ext}(\mathfrak{X}\_{n}) is a finite set of vertices, and the problem reduces to a finite-dimensional convex programming problem.

###### Proof 3.5.

Fix u,zju,z\_{j}, and a sample index jj. Define an auxiliary function:

|  |  |  |
| --- | --- | --- |
|  | ψj​(x):=U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j)).\psi\_{j}(x):=U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)}). |  |

This is a continuous concave function over the compact set 𝔛n\mathfrak{X}\_{n}. Hence, the minimum is attained by the Weierstrass Extremum Theorem.

Notably, since 𝔛n\mathfrak{X}\_{n} is compact, its convex hull C:=conv⁡(𝔛n)C:=\operatorname{conv}(\mathfrak{X}\_{n}) is a compact convex set.
We invoke the fundamental result in convex analysis that a concave function ψj\psi\_{j} attaining a minimum over CC attains that minimum at one of its extreme points, see [bertsekas2009convex, Proposition 2.4.1].
Therefore, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | minx∈conv⁡(𝔛n)⁡ψj​(x)=minx∈Ext⁡(conv⁡(𝔛n))⁡ψj​(x).\displaystyle\min\_{x\in\operatorname{conv}(\mathfrak{X}\_{n})}\psi\_{j}(x)=\min\_{x\in\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n}))}\psi\_{j}(x). |  |

Furthermore, since Ext⁡(conv⁡(𝔛n))⊆𝔛n⊆conv⁡(𝔛n)\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n}))\subseteq\mathfrak{X}\_{n}\subseteq\operatorname{conv}(\mathfrak{X}\_{n}), the minimum over the convex hull is equivalent to the minimum over the original set 𝔛n\mathfrak{X}\_{n}, establishing the desired result:

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | minx∈𝔛n⁡ψj​(x)=minx∈Ext⁡(conv⁡(𝔛n))⁡ψj​(x),\displaystyle\min\_{x\in\mathfrak{X}\_{n}}\psi\_{j}(x)=\min\_{x\in\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n}))}\psi\_{j}(x), |  |

Therefore, ([16](https://arxiv.org/html/2602.04219v1#S3.E16 "Equation 16 ‣ Proof 3.5. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) implies
minx∈𝔛n⁡ψj​(x)−Ωp​(zj,λ)=minx∈Ext⁡(conv⁡(𝔛n))⁡ψj​(x)−Ωp​(zj,λ),\min\_{x\in\mathfrak{X}\_{n}}\psi\_{j}(x)-\Omega\_{p}(z\_{j},\lambda)=\min\_{x\in\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n}))}\psi\_{j}(x)-\Omega\_{p}(z\_{j},\lambda),
since Ωp​(⋅)\Omega\_{p}(\cdot) is xx-independent.
Consequently, the semi-infinite constraint minx⁡ψj​(x)−Ωp​(zj,λ)≥sj\min\_{x}\psi\_{j}(x)-\Omega\_{p}(z\_{j},\lambda)\geq s\_{j} is satisfied if and only if it holds for all v∈Ext⁡(conv⁡(𝔛n))v\in\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n})). If 𝔛n\mathfrak{X}\_{n} is a polytope, |Ext⁡(𝔛n)|<∞|\operatorname{Ext}(\mathfrak{X}\_{n})|<\infty, ensuring a finite number of constraints.

###### Remark 3.6 (Computational Complexity).

Corollary [3.4](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem4 "Corollary 3.4 (Reduction of Semi-Infinite Constraint). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") reduces the semi-infinite constraint
indexed by 𝔛n\mathfrak{X}\_{n} to an equivalent constraint indexed by the extreme-point set
Ext⁡(conv⁡(𝔛n))\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n})). In general, Ext⁡(conv⁡(𝔛n))\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n})) may be infinite (e.g., when 𝔛n\mathfrak{X}\_{n} is strictly convex), and the resulting formulation remains semi-infinite.
If, however, the conv⁡(𝔛n)\operatorname{conv}(\mathfrak{X}\_{n}) is a polytope, then Ext⁡(conv⁡(𝔛n))\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n})) is a finite vertex set. In this case, the number of constraints scales as Nn×|Ext⁡(𝔛n)|N\_{n}\times|\operatorname{Ext}(\mathfrak{X}\_{n})|, which can still
grow exponentially with the disturbance dimension dd (e.g., for a hypercube, |Ext⁡(𝔛n)|=2d|\operatorname{Ext}(\mathfrak{X}\_{n})|=2^{d}).
When |Ext⁡(𝔛n)||\operatorname{Ext}(\mathfrak{X}\_{n})| is large, a cutting-plane method (see Appendix [A](https://arxiv.org/html/2602.04219v1#A1 "Appendix A Algorithmic Implementation via Cutting-Plane Method ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."))
can be used to solve the problem by iteratively adding only violated extreme-point constraints.

### 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis

The tractable formulation in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") provides a computable *lower bound* on the true optimal value. This bound arises from the use of the general minimax inequality ([12](https://arxiv.org/html/2602.04219v1#S3.E12 "Equation 12 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), necessitated by the concavity of the utility function in the disturbance variable xx. Consequently, the practical effectiveness of the formulation is governed by the magnitude of the resulting minimax duality gap.

Theoretically, this gap is driven by the smoothness (non-linearity) of the utility function over the support set 𝔛n\mathfrak{X}\_{n}. The following proposition formalizes this by providing an explicit, computable bound based on the smoothness constant LnL\_{n} introduced in Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").

###### Proposition 3.7 (Minimax Duality Gap Bound).

Fix u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta) and λ≥0\lambda\geq 0. Let 𝔇:=supx,y∈𝔛n‖x−y‖\mathfrak{D}:=\sup\_{x,y\in\mathfrak{X}\_{n}}\|x-y\| be the diameter of the disturbance support set under the ground ℓr\ell\_{r}-norm ∥⋅∥\|\cdot\|. For any order p∈[1,∞)p\in[1,\infty), the minimax duality gap for each data sample jj, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δj​(u,λ)\displaystyle\Delta\_{j}(u,\lambda) | :=infx∈𝔛n[U​(Φn​(u,x))+λ​‖x−𝒳^n(j)‖p]\displaystyle:=\inf\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+\lambda\|x-\widehat{\mathcal{X}}\_{n}^{(j)}\|^{p}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −supzj∈ℝdinfx∈𝔛n[U​(Φn​(u,x))+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)],\displaystyle\qquad-\sup\_{z\_{j}\in\mathbb{R}^{d}}\;\inf\_{x\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u,x))+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right], |  |

is bounded from above by
Δj​(u,λ)≤12​Ln​𝔇2,\Delta\_{j}(u,\lambda)\leq\frac{1}{2}L\_{n}\mathfrak{D}^{2},
where LnL\_{n} is the uniform smoothness bound from Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A3).
Moreover, if the composite stage reward map x↦rn​(u,x)x\mapsto r\_{n}(u,x) is affine on 𝔛n\mathfrak{X}\_{n}, then the relaxation is exact, i.e., Δj=0.\Delta\_{j}=0.

###### Proof 3.8.

To prove that the minimax duality gap is bounded from above, we define the primal and dual values associated with the inner variational problem.
For a fixed u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), λ≥0\lambda\geq 0, and data sample 𝒳^n(j)\widehat{\mathcal{X}}\_{n}^{(j)}, let fu​(x):=U​(Φn​(u,x))f\_{u}(x):=U(\Phi\_{n}(u,x)).
By Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A2), fuf\_{u} is concave on 𝔛n\mathfrak{X}\_{n}.
By Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A3), fuf\_{u} is differentiable on 𝔛n\mathfrak{X}\_{n} and ∇fu\nabla f\_{u} is LnL\_{n}-Lipschitz on 𝔛n\mathfrak{X}\_{n}.
Using the Fenchel representation λ​‖v‖p=supz{z⊤​v−Ωp​(z,λ)}\lambda\|v\|^{p}=\sup\_{z}\{z^{\top}v-\Omega\_{p}(z,\lambda)\} as derived in the proof of Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), the primal value of the inner problem as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj\displaystyle P\_{j} | :=infx∈𝔛n[fu​(x)+λ​‖x−𝒳^n(j)‖p]\displaystyle:=\inf\_{x\in\mathfrak{X}\_{n}}\left[f\_{u}(x)+\lambda\|x-\widehat{\mathcal{X}}\_{n}^{(j)}\|^{p}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (17) |  |  | =infx∈𝔛nsupzj∈ℝd[fu​(x)+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)].\displaystyle=\inf\_{x\in\mathfrak{X}\_{n}}\sup\_{z\_{j}\in\mathbb{R}^{d}}\left[f\_{u}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right]. |  |

Define the dual value by exchanging infimum and supremum as:

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | Dj:=supzj∈ℝdinfx∈𝔛n[fu​(x)+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)].\displaystyle D\_{j}:=\sup\_{z\_{j}\in\mathbb{R}^{d}}\inf\_{x\in\mathfrak{X}\_{n}}\left[f\_{u}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right]. |  |

The minimax duality gap is the difference, Δj:=Pj−Dj\Delta\_{j}:=P\_{j}-D\_{j}. The general minimax inequality states that infsup[⋅]≥supinf[⋅]\inf\sup[\cdot]\geq\sup\inf[\cdot], which implies that Δj≥0\Delta\_{j}\geq 0. Our remaining task is to find an upper bound for it.

To upper bound the gap, we linearize the concave function fu​(x)f\_{u}(x). Fix an arbitrary linearization point y∈𝔛ny\in\mathfrak{X}\_{n}. Let Ty​(x):=fu​(y)+∇fu​(y)⊤​(x−y)T\_{y}(x):=f\_{u}(y)+\nabla f\_{u}(y)^{\top}(x-y), which represents the tangent hyperplane to fuf\_{u} at the point yy. Since fu​(x)f\_{u}(x) is concave, it lies below its tangent:

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | fu​(x)≤Ty​(x), for all ​x∈𝔛n.\displaystyle f\_{u}(x)\leq T\_{y}(x),\quad\text{ for all }x\in\mathfrak{X}\_{n}. |  |

The remainder R​(x,y):=Ty​(x)−fu​(x)≥0R(x,y):=T\_{y}(x)-f\_{u}(x)\geq 0.

Additionally, by Assumption [2.4](https://arxiv.org/html/2602.04219v1#S2.SS4 "2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")(A3), gradient ∇fu\nabla f\_{u} is LnL\_{n}-Lipschitz in the sense that
‖∇fu​(x)−∇fu​(y)‖∗≤Ln​‖x−y‖\|\nabla f\_{u}(x)-\nabla f\_{u}(y)\|\_{\*}\leq L\_{n}\|x-y\| for all x,y∈𝔛nx,y\in\mathfrak{X}\_{n}.
Applying the (norm-generalized) descent lemma, e.g., see [beck2017first, Lemma 5.7] to the convex function −fu-f\_{u} yields the uniform bound

|  |  |  |  |
| --- | --- | --- | --- |
| (20) |  | 0≤R​(x,y)≤12​Ln​‖x−y‖2≤12​Ln​𝔇2,for all ​x,y∈𝔛n,0\leq R(x,y)\leq\frac{1}{2}L\_{n}\|x-y\|^{2}\leq\frac{1}{2}L\_{n}\mathfrak{D}^{2},\qquad\text{for all }x,y\in\mathfrak{X}\_{n}, |  |

where 𝔇:=supx,y∈𝔛n‖x−y‖\mathfrak{D}:=\sup\_{x,y\in\mathfrak{X}\_{n}}\|x-y\|.
Now, substituting fu​(x)=Ty​(x)−R​(x,y)f\_{u}(x)=T\_{y}(x)-R(x,y) into the expressions for PjP\_{j} and DjD\_{j}, we have the following bounds:

*Bound the Primal:* Using ([19](https://arxiv.org/html/2602.04219v1#S3.E19 "Equation 19 ‣ Proof 3.8. ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), we substitute TyT\_{y} for fuf\_{u}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj\displaystyle P\_{j} | =infx∈𝔛nsupzj∈ℝd[fu​(x)+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)]\displaystyle=\inf\_{x\in\mathfrak{X}\_{n}}\sup\_{z\_{j}\in\mathbb{R}^{d}}\left[f\_{u}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤infx∈𝔛nsupzj∈ℝd[Ty(x)+zj⊤(x−𝒳^n(j))−Ωp(zj,λ)]=:Plin(y).\displaystyle\leq\inf\_{x\in\mathfrak{X}\_{n}}\sup\_{z\_{j}\in\mathbb{R}^{d}}\left[T\_{y}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right]=:P\_{\rm lin}(y). |  |

*Bound the Dual:* Since Ωp​(zj,λ)\Omega\_{p}(z\_{j},\lambda) is independent of xx, the remainder term separates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dj\displaystyle D\_{j} | =supzj∈ℝdinfx∈𝔛n[Ty​(x)−R​(x,y)+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)]\displaystyle=\sup\_{z\_{j}\in\mathbb{R}^{d}}\inf\_{x\in\mathfrak{X}\_{n}}\left[T\_{y}(x)-R(x,y)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥supzj∈ℝd(infx∈𝔛n[Ty​(x)+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)]−supx′∈𝔛nR​(x′,y))\displaystyle\geq\sup\_{z\_{j}\in\mathbb{R}^{d}}\left(\inf\_{x\in\mathfrak{X}\_{n}}\left[T\_{y}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right]-\sup\_{x^{\prime}\in\mathfrak{X}\_{n}}R(x^{\prime},y)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supzj∈ℝd(infx∈𝔛n[Ty​(x)+zj⊤​(x−𝒳^n(j))]−Ωp​(zj,λ))−supx′∈𝔛nR​(x′,y)\displaystyle=\sup\_{z\_{j}\in\mathbb{R}^{d}}\left(\inf\_{x\in\mathfrak{X}\_{n}}\left[T\_{y}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})\right]-\Omega\_{p}(z\_{j},\lambda)\right)-\sup\_{x^{\prime}\in\mathfrak{X}\_{n}}R(x^{\prime},y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | :=Dlin​(y)−supx′∈𝔛nR​(x′,y),\displaystyle:=D\_{\rm lin}(y)-\sup\_{x^{\prime}\in\mathfrak{X}\_{n}}R(x^{\prime},y), |  |

where Dlin​(y):=supzj∈ℝdinfx∈𝔛n[Ty​(x)+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)]D\_{\rm lin}(y):=\sup\_{z\_{j}\in\mathbb{R}^{d}}\inf\_{x\in\mathfrak{X}\_{n}}\left[T\_{y}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right].

*Bound the Gap:*
The terms Plin​(y)P\_{\rm lin}(y) and Dlin​(y)D\_{\rm lin}(y) represent the primal and dual of a minimax problem involving a function 𝔏​(x,zj)=Ty​(x)+zj⊤​(x−𝒳^n(j))−Ωp​(zj,λ)\mathfrak{L}(x,z\_{j})=T\_{y}(x)+z\_{j}^{\top}(x-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda). Note that 𝔏​(x,zj)\mathfrak{L}(x,z\_{j}) is affine in xx and concave in zjz\_{j}.
Since the extrema of an affine function over a compact set 𝔛n\mathfrak{X}\_{n} coincide with those over its convex hull conv⁡(𝔛n)\operatorname{conv}(\mathfrak{X}\_{n}), we may consider the problem on the domain conv⁡(𝔛n)\operatorname{conv}(\mathfrak{X}\_{n}) without changing the optimal values. As conv⁡(𝔛n)\operatorname{conv}(\mathfrak{X}\_{n}) is compact and convex, Sion’s Minimax Theorem applies to this extension, implying Plin​(y)=Dlin​(y)P\_{\rm lin}(y)=D\_{\rm lin}(y).

Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (21) |  | Δj=Pj−Dj≤Plin​(y)−(Dlin​(y)−supx′∈𝔛nR​(x′,y))=supx′∈𝔛nR​(x′,y).\displaystyle\Delta\_{j}=P\_{j}-D\_{j}\leq P\_{\rm lin}(y)-\left(D\_{\rm lin}(y)-\sup\_{x^{\prime}\in\mathfrak{X}\_{n}}R(x^{\prime},y)\right)=\sup\_{x^{\prime}\in\mathfrak{X}\_{n}}R(x^{\prime},y). |  |

Using the uniform bound from ([20](https://arxiv.org/html/2602.04219v1#S3.E20 "Equation 20 ‣ Proof 3.8. ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), we obtain Δj≤12​Ln​𝔇2\Delta\_{j}\leq\frac{1}{2}L\_{n}\mathfrak{D}^{2}.

To complete the proof, consider the case where the stage reward fu​(x)f\_{u}(x) is affine in xx, i.e., fu​(x):=a​(u)⊤​x+b​(u)f\_{u}(x):=a(u)^{\top}x+b(u). Then, for any linearization point yy, the remainder term is exact. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(x,y)=Ty​(x)−fu​(x)\displaystyle R(x,y)=T\_{y}(x)-f\_{u}(x) | =fu​(y)+a​(u)⊤​(x−y)−fu​(x)\displaystyle=f\_{u}(y)+a(u)^{\top}(x-y)-f\_{u}(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[a​(u)⊤​y+b​(u)]+a​(u)⊤​(x−y)−[a​(u)⊤​x+b​(u)]\displaystyle=\left[a(u)^{\top}y+b(u)\right]+a(u)^{\top}(x-y)-\left[a(u)^{\top}x+b(u)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a​(u)⊤​y+a​(u)⊤​(x−y)−a​(u)⊤​x=0.\displaystyle=a(u)^{\top}y+a(u)^{\top}(x-y)-a(u)^{\top}x=0. |  |

Substituting this into the bound ([21](https://arxiv.org/html/2602.04219v1#S3.E21 "Equation 21 ‣ Proof 3.8. ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), we conclude Δj≤supx∈𝔛nR​(x,y)=0.\Delta\_{j}\leq\sup\_{x\in\mathfrak{X}\_{n}}R(x,y)=0.

###### Remark 3.9 (On the Generality of the Duality Gap Bound).

Note that the bound in Proposition [3.7](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem7 "Proposition 3.7 (Minimax Duality Gap Bound). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") is independent of the Wasserstein order pp and the radius εn\varepsilon\_{n}; it depends only on the smoothness constant LnL\_{n} and the diameter 𝔇\mathfrak{D} of 𝔛n\mathfrak{X}\_{n}.
Moreover, the bound is a worst-case *uniform* estimate over λ≥0\lambda\geq 0.
We also note that when λ=0\lambda=0, feasibility forces zj=0z\_{j}=0 (for p=1p=1 via ‖zj‖∗≤λ\|z\_{j}\|\_{\*}\leq\lambda, and for p>1p>1 via the extended-value convention Ωp​(z,0)=+∞\Omega\_{p}(z,0)=+\infty for z≠0z\neq 0), hence Pj=DjP\_{j}=D\_{j} and Δj​(u,0)=0\Delta\_{j}(u,0)=0.

We now specialize the general duality bound to the widely used affine-logarithmic structure considered in Example [2.3](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem3 "Example 2.3 (Log-Optimal Portfolio Control). ‣ 2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").

###### Corollary 3.10 (Explicit Duality Gap Bound for Affine-Logarithmic Structures).

Fix n∈𝒩n\in\mathcal{N}, u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), and λ≥0\lambda\geq 0.
Consider the setting of Example [2.3](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem3 "Example 2.3 (Log-Optimal Portfolio Control). ‣ 2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") with
Φn​(u,x)=u⊤​x+cn​(u)\Phi\_{n}(u,x)=u^{\top}x+c\_{n}(u) and U​(⋅)=log⁡(⋅)U(\cdot)=\log(\cdot).
Define the realized margin
Φ¯n​(u):=minx∈𝔛n⁡Φn​(u,x).\underline{\Phi}\_{n}(u):=\min\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x).
Then, for each j=1,…,Nnj=1,\dots,N\_{n},

|  |  |  |
| --- | --- | --- |
|  | Δj​(u,λ)≤‖u‖∗22​Φ¯n​(u)2​𝔇2≤‖u‖∗22​η2​𝔇2.\Delta\_{j}(u,\lambda)\leq\frac{\|u\|\_{\*}^{2}}{2\underline{\Phi}\_{n}(u)^{2}}\,\mathfrak{D}^{2}\leq\frac{\|u\|\_{\*}^{2}}{2\,\eta^{2}}\,\mathfrak{D}^{2}. |  |

###### Proof 3.11.

Since u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta), by definition we have Φn​(u,x)≥η\Phi\_{n}(u,x)\geq\eta for all x∈𝔛nx\in\mathfrak{X}\_{n}. Taking the minimum over x∈𝔛nx\in\mathfrak{X}\_{n} yields Φ¯n​(u)=minx∈𝔛n⁡Φn​(u,x)≥η\underline{\Phi}\_{n}(u)=\min\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x)\geq\eta.
Moreover, as derived in Example [2.3](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem3 "Example 2.3 (Log-Optimal Portfolio Control). ‣ 2.4 Standing Assumptions on Growth Factor ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), ∇xrn​(u,⋅)\nabla\_{x}r\_{n}(u,\cdot) is Ln​(u)L\_{n}(u)-Lipschitz with Ln​(u):=‖u‖∗2Φ¯n​(u)2L\_{n}(u):=\tfrac{\|u\|\_{\*}^{2}}{\underline{\Phi}\_{n}(u)^{2}}.
Hence,

|  |  |  |
| --- | --- | --- |
|  | Ln​(u)=‖u‖∗2Φ¯n​(u)2≤‖u‖∗2η2,L\_{n}(u)=\frac{\|u\|\_{\*}^{2}}{\underline{\Phi}\_{n}(u)^{2}}\leq\frac{\|u\|\_{\*}^{2}}{\eta^{2}}, |  |

Substituting into Proposition [3.7](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem7 "Proposition 3.7 (Minimax Duality Gap Bound). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") yields the claim.

###### Remark 3.12 (Magnitude and Interpretation of the Gap Bound).

Corollary [3.10](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem10 "Corollary 3.10 (Explicit Duality Gap Bound for Affine-Logarithmic Structures). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") provides a two-level certificate on the minimax duality gap.
The first bound, in terms of the realized margin Φ¯n​(u)=minx∈𝔛n⁡Φn​(u,x)\underline{\Phi}\_{n}(u)=\min\_{x\in\mathfrak{X}\_{n}}\Phi\_{n}(u,x), is an *a posteriori* estimate that can be evaluated for a given feasible control uu and is typically much sharper.
The second bound replaces Φ¯n​(u)\underline{\Phi}\_{n}(u) by the design viability margin η\eta and serves as a uniform *a priori* envelope that holds for all u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta).
In both cases, the bound scales quadratically in ‖u‖∗\|u\|\_{\*} and 𝔇\mathfrak{D}, and it increases as the corresponding margin (Φ¯n​(u)\underline{\Phi}\_{n}(u) or η\eta) decreases toward zero.

###### Lemma 3.13 (Probabilistic Performance Guarantee).

Fix β∈(0,1)\beta\in(0,1) and a finite candidate set 𝒩\mathcal{N}.
For each n∈𝒩n\in\mathcal{N}, let εn\varepsilon\_{n} be calibrated according to Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), i.e., ℙ​(𝔽true,n∈ℬεn(p)​(𝔽^n))≥1−β|𝒩|.\mathbb{P}\left(\mathbb{F}\_{\mathrm{true},n}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})\right)\geq 1-\frac{\beta}{|\mathcal{N}|}.
Let Jcvx∗​(n)J\_{\rm cvx}^{\*}(n) denote the optimal value of the tractable program in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")
constructed from 𝔽^n\widehat{\mathbb{F}}\_{n} and radius εn\varepsilon\_{n}.
Then, with probability at least 1−β1-\beta (with respect to the sampling that generates {𝒳^n(j)}\{\widehat{\mathcal{X}}\_{n}^{(j)}\}),
the following holds simultaneously for all n∈𝒩n\in\mathcal{N}:

|  |  |  |
| --- | --- | --- |
|  | Jcvx∗​(n)≤maxu∈𝒰v​(n;η)⁡1n​𝔼𝔽true,n​[U​(Φn​(u,𝒳))].J\_{\rm cvx}^{\*}(n)\leq\max\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\frac{1}{n}\,\mathbb{E}^{\mathbb{F}\_{\mathrm{true},n}}\!\left[U(\Phi\_{n}(u,\mathcal{X}))\right]. |  |

###### Proof 3.14.

Fix β∈(0,1)\beta\in(0,1) and a finite candidate set 𝒩\mathcal{N}.
For each n∈𝒩n\in\mathcal{N}, let εn\varepsilon\_{n} satisfy ([4](https://arxiv.org/html/2602.04219v1#S2.E4 "Equation 4 ‣ Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")). Then, Inequality ([4](https://arxiv.org/html/2602.04219v1#S2.E4 "Equation 4 ‣ Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) and a union bound yields

|  |  |  |
| --- | --- | --- |
|  | ℙ(∀n∈𝒩:𝔽true,n∈ℬεn(p)(𝔽^n))≥1−β.\mathbb{P}\!\left(\forall n\in\mathcal{N}:\ \mathbb{F}\_{\mathrm{true},n}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})\right)\geq 1-\beta. |  |

On this event, for each fixed nn, Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") yields

|  |  |  |  |
| --- | --- | --- | --- |
| (22) |  | Jcvx∗​(n)≤maxu∈𝒰v​(n;η)​inf𝔽∈ℬεn(p)​(𝔽^n)1n​𝔼𝔽​[U​(Φn​(u,𝒳))].\displaystyle J\_{\rm cvx}^{\*}(n)\ \leq\ \max\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\ \inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\frac{1}{n}\,\mathbb{E}^{\mathbb{F}}\!\left[U(\Phi\_{n}(u,\mathcal{X}))\right]. |  |

Since 𝔽true,n\mathbb{F}\_{\mathrm{true},n} belongs to the ambiguity set on the same event, we have for every fixed u∈𝒰v​(n;η)u\in\mathcal{U}\_{\rm v}(n;\eta),

|  |  |  |
| --- | --- | --- |
|  | inf𝔽∈ℬεn(p)​(𝔽^n)𝔼𝔽​[U​(Φn​(u,𝒳))]≤𝔼𝔽true,n​[U​(Φn​(u,𝒳))].\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\mathbb{E}^{\mathbb{F}}\!\left[U(\Phi\_{n}(u,\mathcal{X}))\right]\leq\mathbb{E}^{\mathbb{F}\_{\mathrm{true},n}}\left[U(\Phi\_{n}(u,\mathcal{X}))\right]. |  |

Taking maxu∈𝒰v​(n;η)⁡1n​(⋅)\max\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\frac{1}{n}(\cdot) on both sides yields

|  |  |  |
| --- | --- | --- |
|  | maxu∈𝒰v​(n;η)​inf𝔽∈ℬεn(p)​(𝔽^n)1n​𝔼𝔽​[U​(Φn​(u,𝒳))]≤maxu∈𝒰v​(n;η)⁡1n​𝔼𝔽true,n​[U​(Φn​(u,𝒳))].\max\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\frac{1}{n}\,\mathbb{E}^{\mathbb{F}}\!\left[U(\Phi\_{n}(u,\mathcal{X}))\right]\leq\max\_{u\in\mathcal{U}\_{\rm v}(n;\eta)}\frac{1}{n}\,\mathbb{E}^{\mathbb{F}\_{\mathrm{true},n}}\left[U(\Phi\_{n}(u,\mathcal{X}))\right]. |  |

Combining with ([22](https://arxiv.org/html/2602.04219v1#S3.E22 "Equation 22 ‣ Proof 3.14. ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) completes the proof.

### 3.3 Long-Run Performance Guarantees

The preceding results establish guarantees for a single sampling period. In closed-loop operation, however, the robust policy u∗u^{\*} is applied repeatedly over an infinite horizon. We now establish the link between the tractable relaxation Jcvx∗​(n)J\_{\rm cvx}^{\*}(n) and the long-run performance of the system. We first present a general result for any concave utility satisfying the standing assumptions. This ensures that the optimal value of the relaxation provides a deterministic floor for the *long-run average utility rate*.

###### Theorem 3.15 (Long-Run Average Utility Guarantee).

Fix n∈𝒩n\in\mathcal{N}. Suppose that the sequence of nn-period aggregated disturbances {𝒳k,n}k≥0\{\mathcal{X}\_{k,n}\}\_{k\geq 0} is strictly stationary and ergodic under the true distribution 𝔽true,n\mathbb{F}\_{\mathrm{true},n}. Let εn\varepsilon\_{n} be calibrated according to Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), and define the coverage event ℰn:={𝔽true,n∈ℬεn(p)​(𝔽^n)}\mathcal{E}\_{n}:=\{\mathbb{F}\_{\mathrm{true},n}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})\}.
Let u∗u^{\*} be an optimal control for the tractable relaxation ([7](https://arxiv.org/html/2602.04219v1#S3.E7 "Equation 7 ‣ Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) with optimal value Jcvx∗​(n)J\_{\rm cvx}^{\*}(n). Then, conditional on the event ℰn\mathcal{E}\_{n}, the long-run average utility rate satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (23) |  | limK→∞1K​n​∑k=0K−1U​(Φn​(u∗,𝒳k,n))≥Jcvx∗​(n)𝔽true,n​-a.s.\displaystyle\lim\_{K\to\infty}\frac{1}{Kn}\sum\_{k=0}^{K-1}U(\Phi\_{n}(u^{\*},\mathcal{X}\_{k,n}))\geq J\_{\mathrm{cvx}}^{\*}(n)\qquad\mathbb{F}\_{\mathrm{true},n}\text{-a.s.} |  |

###### Proof 3.16.

Define the per-period utility realization

|  |  |  |
| --- | --- | --- |
|  | Yk:=1n​U​(Φn​(u∗,𝒳k,n)),k=0,1,2,…Y\_{k}:=\frac{1}{n}U(\Phi\_{n}(u^{\*},\mathcal{X}\_{k,n})),\qquad k=0,1,2,\ldots |  |

Since {𝒳k,n}k≥0\{\mathcal{X}\_{k,n}\}\_{k\geq 0} is strictly stationary and ergodic, and the map x↦1n​U​(Φn​(u∗,x))x\mapsto\frac{1}{n}U(\Phi\_{n}(u^{\*},x)) is measurable, the sequence {Yk}\{Y\_{k}\} is also strictly stationary and ergodic.
Moreover, since u∗∈𝒰v​(n;η)u^{\*}\in\mathcal{U}\_{\rm v}(n;\eta), we have Φn​(u∗,x)≥η\Phi\_{n}(u^{\*},x)\geq\eta for all x∈𝔛nx\in\mathfrak{X}\_{n}. Because 𝔛n\mathfrak{X}\_{n} is compact and x↦Φn​(u∗,x)x\mapsto\Phi\_{n}(u^{\*},x) is continuous, Φn​(u∗,x)\Phi\_{n}(u^{\*},x) is bounded above on 𝔛n\mathfrak{X}\_{n}. Since U​(⋅)U(\cdot) is continuous on [η,∞)[\eta,\infty), it follows that YkY\_{k} is bounded and hence integrable, i.e., 𝔼𝔽true,n​[|Y0|]<∞\mathbb{E}^{\mathbb{F}\_{\mathrm{true},n}}[|Y\_{0}|]<\infty.
Applying the Birkhoff Ergodic Theorem yields

|  |  |  |  |
| --- | --- | --- | --- |
| (24) |  | limK→∞1K​∑k=0K−1Yk=𝔼𝔽true,n​[Y0]=1n​𝔼𝔽true,n​[U​(Φn​(u∗,𝒳))]𝔽true,n​-a.s.,\displaystyle\lim\_{K\to\infty}\frac{1}{K}\sum\_{k=0}^{K-1}Y\_{k}=\mathbb{E}^{\mathbb{F}\_{\mathrm{true},n}}[Y\_{0}]=\frac{1}{n}\mathbb{E}^{\mathbb{F}\_{\mathrm{true},n}}\!\left[U(\Phi\_{n}(u^{\*},\mathcal{X}))\right]\qquad\mathbb{F}\_{\mathrm{true},n}\text{-a.s.}, |  |

where 𝒳\mathcal{X} denotes a generic aggregate disturbance distributed according to the common distribution 𝔽true,n\mathbb{F}\_{\mathrm{true},n} of the stationary sequence.
Next, recall that the tractable relaxation in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") is derived via the minimax inequality applied at the constraint level; i.e., see ([12](https://arxiv.org/html/2602.04219v1#S3.E12 "Equation 12 ‣ Proof 3.2. ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")).
Consequently, for every fixed admissible control uu, the relaxation value provides a lower bound on the corresponding worst-case expected utility. In particular, for the relaxation optimizer u∗u^{\*}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (25) |  | Jcvx∗​(n)≤inf𝔽∈ℬεn(p)​(𝔽^n)1n​𝔼𝔽​[U​(Φn​(u∗,𝒳))].\displaystyle J\_{\mathrm{cvx}}^{\*}(n)\leq\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\frac{1}{n}\mathbb{E}^{\mathbb{F}}\left[U(\Phi\_{n}(u^{\*},\mathcal{X}))\right]. |  |

Conditional on the event ℰn\mathcal{E}\_{n}, the true distribution 𝔽true,n∈ℬεn(p)​(𝔽^n)\mathbb{F}\_{\mathrm{true},n}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n}). Thus, the infimum over the ambiguity set is a lower bound for the expectation under the true distribution; i.e.,

|  |  |  |
| --- | --- | --- |
|  | inf𝔽∈ℬεn(p)​(𝔽^n)1n​𝔼𝔽​[U​(Φn​(u∗,𝒳))]≤1n​𝔼𝔽true,n​[U​(Φn​(u∗,𝒳))].\inf\_{\mathbb{F}\in\mathcal{B}\_{\varepsilon\_{n}}^{(p)}(\widehat{\mathbb{F}}\_{n})}\frac{1}{n}\mathbb{E}^{\mathbb{F}}\left[U(\Phi\_{n}(u^{\*},\mathcal{X}))\right]\leq\frac{1}{n}\mathbb{E}^{\mathbb{F}\_{\mathrm{true},n}}\left[U(\Phi\_{n}(u^{\*},\mathcal{X}))\right]. |  |

Combining with ([24](https://arxiv.org/html/2602.04219v1#S3.E24 "Equation 24 ‣ Proof 3.16. ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) and ([25](https://arxiv.org/html/2602.04219v1#S3.E25 "Equation 25 ‣ Proof 3.16. ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), the desired result follows.

For the specific case of logarithmic utility, the long-run average utility rate coincides with the asymptotic capital growth rate. The following corollary formalizes this connection.

###### Corollary 3.17 (Long-Run Growth Rate Guarantee).

Consider the setting of Theorem [3.15](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem15 "Theorem 3.15 (Long-Run Average Utility Guarantee). ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."). If the utility function is logarithmic, i.e., U​(x)=log⁡(x)U(x)=\log(x), then conditional on the event ℰn\mathcal{E}\_{n}, the long-run realized growth rate satisfies

|  |  |  |
| --- | --- | --- |
|  | limK→∞1K​n​log⁡VK≥Jcvx∗​(n)𝔽true,n​-a.s.\lim\_{K\to\infty}\frac{1}{Kn}\log V\_{K}\geq J\_{\mathrm{cvx}}^{\*}(n)\qquad\mathbb{F}\_{\mathrm{true},n}\text{-a.s.} |  |

###### Proof 3.18.

Under the multiplicative dynamics Vk+1=Vk​Φn​(u∗,𝒳k,n)V\_{k+1}=V\_{k}\Phi\_{n}(u^{\*},\mathcal{X}\_{k,n}), the state at step KK is given by VK=V0​∏k=0K−1Φn​(u∗,𝒳k,n)V\_{K}=V\_{0}\prod\_{k=0}^{K-1}\Phi\_{n}(u^{\*},\mathcal{X}\_{k,n}).
Taking logarithms and dividing by the total time K​nKn, we obtain

|  |  |  |
| --- | --- | --- |
|  | 1K​n​log⁡VK=1K​n​log⁡V0+1K​n​∑k=0K−1log⁡Φn​(u∗,𝒳k,n).\frac{1}{Kn}\log V\_{K}=\frac{1}{Kn}\log V\_{0}+\frac{1}{Kn}\sum\_{k=0}^{K-1}\log\Phi\_{n}(u^{\*},\mathcal{X}\_{k,n}). |  |

As K→∞K\to\infty, the first term 1K​n​log⁡V0\frac{1}{Kn}\log V\_{0} vanishes asymptotically, and the second term corresponds precisely to the long-run average utility rate defined in ([23](https://arxiv.org/html/2602.04219v1#S3.E23 "Equation 23 ‣ Theorem 3.15 (Long-Run Average Utility Guarantee). ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) with U=logU=\log. The result then follows immediately from Theorem [3.15](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem15 "Theorem 3.15 (Long-Run Average Utility Guarantee). ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").

### 3.4 Solving the Joint Optimization Problem

The overall problem ([2.13](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem13 "Problem 2.13 (Horizon-Consistent Distributionally Robust Control). ‣ 2.7 Distributionally Robust Control Formulation ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")) requires a joint maximization over the integer-valued sampling period nn and the continuous control vector uu, making it a *mixed-integer program*.
Our solution strategy leverages the finite and low-cardinality nature of the candidate set 𝒩\mathcal{N}. We solve the problem via explicit enumeration over nn: for each candidate nn, we compute the corresponding optimal control u∗​(n)u^{\*}(n) and then select the pair (u∗,n∗)(u^{\*},n^{\*}) that attains the largest certified objective value.

The *inner problem* for each fixed nn is the convex program formulated in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") and Corollary [3.4](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem4 "Corollary 3.4 (Reduction of Semi-Infinite Constraint). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."). Since the number of constraints in this program (indexed by the extreme points of 𝔛n\mathfrak{X}\_{n}) grows exponentially with the disturbance dimension dd, enumerating them directly is often computationally infeasible. Therefore, we solve this inner problem efficiently using a cutting-plane algorithm, the technical details of which are presented in Appendix [A](https://arxiv.org/html/2602.04219v1#A1 "Appendix A Algorithmic Implementation via Cutting-Plane Method ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").

## 4 Illustrative Examples

This section instantiates the sampled-data robust control framework, developed in Sections [2](https://arxiv.org/html/2602.04219v1#S2 "2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") and [3](https://arxiv.org/html/2602.04219v1#S3 "3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), on the *Log-Optimal Portfolio Control problem*. This problem serves as a canonical example of a multiplicative stochastic system where state-dependent friction (transaction costs) plays a governing role. Henceforth, for illustration, we select the Wasserstein order p=1p=1 and the ground norm ∥⋅∥=∥⋅∥1\|\cdot\|=\|\cdot\|\_{1}.

In the context of the general dynamics ([1](https://arxiv.org/html/2602.04219v1#S2.E1 "Equation 1 ‣ 2.2 Sampled-Data Multiplicative Dynamics ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), the system state VkV\_{k} represents the portfolio wealth, the control input uku\_{k} corresponds to the vector of asset allocation weights, and the disturbance 𝒳k,n\mathcal{X}\_{k,n} models the vector of random asset returns over the sampling interval. The growth function Φn\Phi\_{n} explicitly captures the transaction costs associated with rebalancing.

### 4.1 Setup and Data

Let u∈ℝ+mu\in\mathbb{R}\_{+}^{m} denote the vector of portfolio weights invested in risky assets. We assume the transaction cost associated with rebalancing is modeled as T​C​(u):=∑i=1mκi​|ui|TC(u):=\sum\_{i=1}^{m}\kappa\_{i}|u\_{i}|, where κi∈[0,1)\kappa\_{i}\in[0,1) represents the proportional friction (e.g., brokerage fees and slippage) for asset ii. This model is consistent with real-world trading mechanics, where fees are charged on the trade value.222For example, trading stocks on the Taiwan Stock Exchange (TWSE) typically incurs a broker handling fee up to 0.1425%0.1425\%, plus a securities transaction tax of 0.3%0.3\% on sell side. Similarly, professional brokerage services such as Interactive Brokers Pro apply asset-class-specific commission schedules based on trade value or volume.

Consequently, the net-of-cost growth factor is given by the affine form:

|  |  |  |
| --- | --- | --- |
|  | Φn​(u,x):=u⊤​x+cn​(u),\Phi\_{n}(u,x):=u^{\top}x+c\_{n}(u), |  |

where xx is the vector of *excess returns* (i.e., risky asset returns net of the risk-free benchmark), and cn​(u)c\_{n}(u) represents the risk-free growth net of transaction costs, defined as
cn​(u):=(1+rf,n)−T​C​(u).c\_{n}(u):=(1+r\_{f,n})-TC(u).
Here, rf,nr\_{f,n} denotes the *nn-period* risk-free return, obtained by converting the observed annualized
Treasury-bill yield at the rebalancing time.333In our experiments, we use the CBOE Interest Rate 13-Week Treasury Bill (IRX) as the proxy, converting the annualized yield rfann​(tk)r^{\mathrm{ann}}\_{f}(t\_{k}) to the sampling period nn via rf,n​(tk):=(1+rfann​(tk)252)n−1r\_{f,n}(t\_{k}):=(1+\tfrac{r^{\mathrm{ann}}\_{f}(t\_{k})}{252})^{n}-1.
This formulation decouples the baseline net risk-free drift (isolated in cn​(u)c\_{n}(u)) from the stochastic disturbance xx, preserving the affine structure.

#### Data Description

We consider a portfolio comprising a risk-free asset and ten risky assets selected from the top ten constituents of the S&P 500 by market capitalization at year end 2022.
The specific assets are listed in Table [1](https://arxiv.org/html/2602.04219v1#S4.T1 "Table 1 ‣ Data Description ‣ 4.1 Setup and Data ‣ 4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").
Stock price data was obtained from Yahoo Finance for the period from January 1, 2022, to May 31, 2025.
For the risk-free rate, we use the daily annualized yield on the 13-Week U.S. Treasury Bill (^IRX). Within this horizon, the average annualized risk-free rates were approximately 2.02%2.02\% in 2022, 5.07%5.07\% in 2023, 4.97%4.97\% in 2024, and 4.03%4.03\% in early 2025 (January–May).

Notably, the dataset encompasses distinct market regimes: 2022 was characterized by a bearish market, 2023 signaled a strong recovery (bullish phase), while 2024 and early 2025 corresponded to periods of moderate expansion and volatility. This diversity provides a robust testing ground to evaluate the adaptability of the proposed DRO approach.

Table 1: Selected portfolio constituents (Top 10 S&P 500 stocks by market cap in 2022 year-end

| Rank | Company | Ticker | Percentage of Total |
| --- | --- | --- | --- |
|  |  |  | Index Market Value (%) |
| 1 | Apple Inc. | AAPL | 6.2 |
| 2 | Microsoft Corporation | MSFT | 5.3 |
| 3 | Amazon.com Inc. | AMZN | 2.6 |
| 4 | Alphabet Inc. Class C | GOOG | 1.6 |
| 5 | Alphabet Inc. Class A | GOOGL | 1.6 |
| 6 | United Health Group Inc. | UNH | 1.5 |
| 7 | Johnson & Johnson | JNJ | 1.4 |
| 8 | Exxon Mobil Corporation | XOM | 1.4 |
| 9 | Berkshire Hathaway Inc. Class B | BRK-B | 1.2 |
| 10 | JPMorgan Chase & Co. | JPM | 1.3 |

#### Backtest Simulation Methodology and Control Schemes

To validate our theory, we implement the joint optimization framework defined in Problem [2.13](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem13 "Problem 2.13 (Horizon-Consistent Distributionally Robust Control). ‣ 2.7 Distributionally Robust Control Formulation ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").
We consider a finite candidate set of admissible sampling periods 𝒩:={5,21,42,63}\mathcal{N}:=\{5,21,42,63\}, corresponding to weekly, monthly, bi-monthly, and quarterly control updates.
For any specific sampling period n∈𝒩n\in\mathcal{N} and look-back window, we construct the empirical distribution 𝔽^n\widehat{\mathbb{F}}\_{n} and calibrate the ambiguity radius εn\varepsilon\_{n} consistent with Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.").
We then solve the tractable convex program in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") to obtain the certified robust performance rate Jcvx∗​(n)J\_{\rm cvx}^{\*}(n). We compare two control implementation schemes:

* (i)(i)

  *Static Sampling Scheme.*
  At the initialization of the simulation (t=0t=0), we evaluate the robust performance rate for all candidates using the initial training data and select the sampling period that maximizes the worst-case lower bound:

  |  |  |  |
  | --- | --- | --- |
  |  | n∗∈arg⁡maxn∈𝒩⁡Jcvx∗​(n).n^{\*}\in\arg\max\_{n\in\mathcal{N}}J\_{\rm cvx}^{\*}(n). |  |

  The selected sampling period n∗n^{\*} is then held fixed throughout the out-of-sample backtest, representing a standard sampled-data controller with a pre-optimized but static update frequency.
* (i​i)(ii)

  *Adaptive-Sampling Scheme.*
  At the beginning of each control update step kk, we recompute certified performance rate Jcvx∗​(n)J\_{\rm cvx}^{\*}(n) for all candidate horizons n∈𝒩n\in\mathcal{N} using the current look-back window. We then dynamically select the optimal sampling period for the subsequent holding interval:

  |  |  |  |
  | --- | --- | --- |
  |  | nk∗∈arg⁡maxn∈𝒩⁡Jcvx∗​(n).n\_{k}^{\*}\in\arg\max\_{n\in\mathcal{N}}J\_{\rm cvx}^{\*}(n). |  |

  In this scheme, the controller adapts the sampling period nk∗n\_{k}^{\*} online in response to evolving market volatility and friction estimates.

The out-of-sample backtesting simulation follows a standard rolling-window procedure, starting with an initial account value of V0=$​1V\_{0}=\mathdollar 1:

1. (i)(i)

   *Data Construction:*
   At the beginning of the kkth rebalancing period, corresponding to time tkt\_{k}, we use a fixed look-back window of length L=252L=252 trading days (approximately one year). From this history [tk−L,tk][t\_{k}-L,t\_{k}], we construct a set of Nn=L−n+1N\_{n}=L-n+1 overlapping samples of nn-period compound return vectors {𝒳^n(j)}j=1Nn\{\widehat{\mathcal{X}}\_{n}^{(j)}\}\_{j=1}^{N\_{n}}. These samples form the empirical distribution 𝔽^n\widehat{\mathbb{F}}\_{n}.444Because these nn-period samples are overlapping, they exhibit serial dependence. Standard sufficient conditions for the finite-sample coverage requirement in Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") are typically derived under i.i.d. sampling; accordingly, in our implementation the radii εn\varepsilon\_{n} are calibrated via block bootstrap as a practical approximation to the target coverage condition.
2. (i​i)(ii)

   *Robust Optimization:*
   We solve the tractable convex program derived in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") using the empirical distribution 𝔽^n\widehat{\mathbb{F}}\_{n}. This yields the robustly optimal control vector uk∗u\_{k}^{\*} (portfolio weights) for the upcoming sampling period. In the adaptive-horizon strategy, this optimization is performed for all n∈𝒩n\in\mathcal{N} at each rebalancing time, and the horizon nk∗n\_{k}^{\*} with the largest certified value is selected.
3. (i​i​i)(iii)

   *Execution:*
   The portfolio is rebalanced to the target weights uk∗u\_{k}^{\*}. Transaction costs are incurred on the rebalancing volume of the risky assets. The asset holdings are then held constant for the next nn trading days (zero-order hold implementation), where n=n∗n=n^{\*} for the fixed-horizon strategy and n=nk∗n=n\_{k}^{\*} for the adaptive-horizon strategy.
4. (i​v)(iv)

   *Update:*
   At the end of the sampling period, the account value Vk+1V\_{k+1} is marked-to-market. The look-back window slides forward by nn days, and the process repeats from Step 1.

This procedure generates a complete out-of-sample wealth trajectory. In the main frequency-selection procedure, the ambiguity radii are calibrated as εn\varepsilon\_{n} according to Definition [2.5](https://arxiv.org/html/2602.04219v1#S2.Thmtheorem5 "Definition 2.5 (Calibrated Ambiguity Radii). ‣ 2.5 Wasserstein Ambiguity Set ‣ 2 Preliminaries and Problem Formulation ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."). Unless otherwise stated, a proportional transaction-cost rate of 1010 bps is used throughout.

### 4.2 Out-Of-Sample Performance

Figure [2](https://arxiv.org/html/2602.04219v1#S4.F2 "Figure 2 ‣ 4.2 Out-Of-Sample Performance ‣ 4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") compares the out-of-sample wealth trajectories across different rebalancing schemes. We evaluate both static-sampling controllers (with fixed n∗n^{\*}) and the adaptive-sampling controller (with dynamic nk∗n\_{k}^{\*}). While the benchmarks—Buy-and-Hold and the Daily Rebalanced Equal Weight portfolio—achieve the highest nominal cumulative wealth, they suffer from significant drawdowns (approximately 20%20\%; see MDD in Table [2](https://arxiv.org/html/2602.04219v1#S4.T2 "Table 2 ‣ 4.2 Out-Of-Sample Performance ‣ 4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")).
In contrast, the proposed DRO schemes maintain competitive growth while offering superior downside-risk control. Notably, the adaptive-sampling scheme achieves the highest risk-adjusted performance (SR = 0.50) in this backtest simulation, validating the benefit of dynamic frequency selection.
Figure [3](https://arxiv.org/html/2602.04219v1#S4.F3 "Figure 3 ‣ 4.2 Out-Of-Sample Performance ‣ 4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") reveals the realized sequence of sampling periods nk∗n\_{k}^{\*} selected by the adaptive strategy under the baseline cost setting.

![Refer to caption](x1.png)


Figure 2: Out-of-sample wealth trajectories comparing static sampling with fixed n∗n^{\*} and adaptive sampling with dynamic nk∗n^{\*}\_{k}. The DRO strategies induce a conservative allocation during high-volatility regimes, effectively limits the downside risks.

![Refer to caption](x2.png)


Figure 3: Adaptive sampling scheme: realized sequence of selected sampling period nk∗n\_{k}^{\*}. The controller autonomously switches between high-frequency and low-frequency updates based on the trade-off between growth opportunities and friction (transaction costs).

Table [2](https://arxiv.org/html/2602.04219v1#S4.T2 "Table 2 ‣ 4.2 Out-Of-Sample Performance ‣ 4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") summarizes the out-of-sample trading performance across different sampling strategies and horizons. Reported metrics include final account value (FV), compound annual growth rate (CAGR),555CAGR is computed as FV1/T−1\texttt{FV}^{1/T}-1, where TT denotes the length of the backtest in years.
 total return (TR), maximum drawdown (MDD), annualized Sharpe ratio (SR), and annualized volatility (Vol), along with transaction-related statistics.

Overall, the proposed DRO schemes provide competitive risk-aware growth (see FV, CAGR, TR) while exhibiting improved downside-risk control, as reflected by smaller drawdowns (MDD) and lower volatility (Vol), relative to the baseline strategies (buy-and-hold and the daily rebalanced equal-weight portfolio). We observe that when estimated distributional ambiguity is high, the worst-case performance assessment becomes more conservative, prompting the controller to shift allocation toward the risk-free asset or reduce rebalancing frequency to conserve capital.

Table 2: Out-of-sample performance comparison of strategies.
Shorthands: FV = final account value, TR = total return,
CAGR = compound annual growth rate, MDD = maximum drawdown,
SR = annualized Sharpe ratio, Vol = annualized volatility,
Best/Worst = best/worst single-day return, TC = cumulative realized transaction costs paid over the backtest,
#Reb = number of rebalances. Here, a proportional transaction-cost rate of 10 bps is applied.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy | nn | FV | CAGR | TR | MDD | SR | Vol | TC | #Reb |
| Static | 5 | 1.1183 | 3.34% | 11.83% | 15.07% | 0.31 | 13.79% | 0.0881 | 171 |
| Static | 21 | 1.1126 | 3.19% | 11.26% | 13.06% | 0.37 | 9.90% | 0.0112 | 41 |
| Static | 42 | 1.1451 | 4.06% | 14.51% | 14.35% | 0.46 | 9.77% | 0.0064 | 21 |
| Static | 63 | 1.0308 | 0.89% | 3.08% | 16.54% | 0.13 | 11.68% | 0.0043 | 14 |
| Adaptive | nk∗n\_{k}^{\*} | 1.2352 | 6.41% | 23.52% | 15.14% | 0.50 | 14.75% | 0.0358 | 60 |
| EW (Daily) | 1 | 1.3504 | 9.24% | 35.04% | 19.95% | 0.36 | 18.62% | 0.0092 | 854 |
| Buy & Hold | – | 1.3059 | 8.16% | 30.59% | 18.80% | 0.31 | 17.62% | 0.0000 | 0 |

We further analyze how transaction costs and distributional ambiguity jointly influence the optimal rebalancing frequency.
Table [3](https://arxiv.org/html/2602.04219v1#S4.T3 "Table 3 ‣ 4.2 Out-Of-Sample Performance ‣ 4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") shows the sensitivity of adaptive-sampling scheme. As expected, increasing transaction costs erodes performance and shifts the optimal sampling period toward longer sampling periods. In particular, for lower TC (5 bps), the adaptive scheme favors short horizons (n=5n=5 selected 77.9% of the time) to capture transient growth opportunities. Conversely, for high TC (50 bps), the selection shifts significantly toward longer horizons (n=63n=63 selected 32.4% of the time) to mitigate friction. This behavior confirms that the proposed framework correctly balances the “cost of control” against the “cost of uncertainty.”

Table 3: Transaction Cost Sensitivity Summary (Adaptive Scheme). As transaction costs increase, the controller autonomously shifts toward longer sampling periods (fewer rebalances).

| TC Rate | Final Value | Avg n∗n^{\*} (days) | # Rebalances | n=5n=5 | n=21n=21 | n=42n=42 | n=63n=63 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 bps | 1.1776 | 12.9 | 68 | 77.9% | 10.3% | 2.9% | 8.8% |
| 10 bps | 1.2352 | 15.9 | 55 | 72.7% | 10.9% | 1.8% | 14.5% |
| 25 bps | 1.0824 | 21.2 | 41 | 56.1% | 22.0% | 0.0% | 22.0% |
| 50 bps | 1.0042 | 25.6 | 34 | 55.9% | 11.8% | 0.0% | 32.4% |

### 4.3 Empirical Tightness of the Minimax Relaxation

To validate the tightness of the convex relaxation established in Theorem [3.1](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem1 "Theorem 3.1 (Tractable Convex Relaxation for Fixed Sampling Period 𝑛). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–."), we computed the theoretical upper bound on the minimax gap derived in Proposition [3.7](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem7 "Proposition 3.7 (Minimax Duality Gap Bound). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") across the entire out-of-sample period. Specifically, we define the worst-case interchange error as Δmax:=maxj⁡Δj\Delta\_{\max}:=\max\_{j}\Delta\_{j} and verify the condition
Δmax≤12​Ln​𝔇2:=B.\Delta\_{\max}\leq\frac{1}{2}L\_{n}\mathfrak{D}^{2}:=B.
Since the bound BB depends only on the global geometry of the ambiguity set, satisfying Δmax≤B\Delta\_{\max}\leq B serves as a uniform certificate that the approximation error is bounded for every robustness constraint jj.

#### Theoretical Validity and Utilization

The theoretical bound Δj≤B\Delta\_{j}\leq B was satisfied in 100% of cases for sampling periods n≥21n\geq 21. For the short sampling periods (n=5n=5), the satisfaction rate remained high at 94.7%. The rare numerical exceptions correspond to edge cases where the theoretical bound falls below the solver’s numerical tolerance.666Specifically, we observed instances where the theoretical bound BB dropped to the order of 10−1510^{-15} (driven by a vanishing diameter 𝔇\mathfrak{D} during low-volatility periods). In these cases, the solver’s inherent numerical noise (approx. 10−910^{-9}) technically exceeds BB, triggering a false violation despite the gap being effectively zero.
 Figure [4](https://arxiv.org/html/2602.04219v1#S4.F4 "Figure 4 ‣ Theoretical Validity and Utilization ‣ 4.3 Empirical Tightness of the Minimax Relaxation ‣ 4 Illustrative Examples ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") illustrates the time-varying duality gap for both static- and adaptive-sampling controls.

To assess the conservatism of the relaxation, we define *Gap Utilization* as the ratio ΔmaxB\frac{\Delta\_{\max}}{B}. Our experiments indicate that the observed gap averages between 2.1% and 6.4% of the theoretical bound. This low utilization suggests that the proposed convex relaxation is empirically much tighter than the worst-case theoretical bound implies.

![Refer to caption](x3.png)


Figure 4: Time-varying duality gap for both static- and adaptive-sampling controls. The gap remains consistently small across all sampling periods n∈{5,21,42,63}n\in\{5,21,42,63\} and adaptive nk∗n\_{k}^{\*}.

## 5 Conclusion

This work established a unified framework for the robust optimal control of sampled-data systems subject to multiplicative noise and distributional ambiguity. By jointly selecting the feedback policy and the control sampling period, we addressed the fundamental trade-off between discretization error, actuation costs, and model risk. A central theoretical contribution is the resolution of the “concave-max” geometry inherent in risk-sensitive distributionally robust control. While Sion’s minimax theorem does not apply to the constraint-level interchange, we showed that the general minimax inequality yields a tractable convex relaxation that provides a rigorous lower bound on the worst-case expected utility.

We provided four theoretical certificates to justify this framework. First, we established a *probabilistic performance guarantee* (Lemma [3.13](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem13 "Lemma 3.13 (Probabilistic Performance Guarantee). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), proving that the optimal value of the tractable relaxation constitutes a valid lower confidence bound on the true expected utility with high probability.
Second, we derived a non-asymptotic upper bound on the *minimax duality gap* (Proposition [3.7](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem7 "Proposition 3.7 (Minimax Duality Gap Bound). ‣ 3.2 Theoretical Guarantees and Minimax Duality Gap Analysis ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), demonstrating that the approximation error is uniformly controlled by the utility’s smoothness and the diameter of the disturbance support. A necessary and sufficient condition for *robust viability* ensuring strict state positivity almost surely across the entire ambiguity set is also derived.
Third, and most importantly, we linked the static optimization to dynamic performance via a *Long-Run Growth Rate Guarantee* (Theorem [3.15](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem15 "Theorem 3.15 (Long-Run Average Utility Guarantee). ‣ 3.3 Long-Run Performance Guarantees ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.")), proving that the derived robust optimal value serves as a deterministic floor for the asymptotic growth rate almost surely.

The practical efficacy of the proposed framework was demonstrated on a log-optimal portfolio control problem. The numerical results indicate that the *adaptive sampling strategy*—which dynamically selects the optimal rebalancing horizon in response to evolving market conditions—significantly enhances risk-adjusted performance while maintaining system viability.
Future work could explore extending this framework to high-dimensional asset universes using factor models to mitigate the computational complexity of the semi-infinite constraints.

## References

## Appendix A Algorithmic Implementation via Cutting-Plane Method

This appendix details the cutting-plane algorithm for solving the inner-loop optimization problem in Corollary [3.4](https://arxiv.org/html/2602.04219v1#S3.Thmtheorem4 "Corollary 3.4 (Reduction of Semi-Infinite Constraint). ‣ 3.1 Tractable Formulation ‣ 3 Theoretical Results ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") for a fixed sampling period nn.
The resulting problem is a convex optimization problem with constraints indexed by the extreme-point
set Ext⁡(𝔛n)\operatorname{Ext}(\mathfrak{X}\_{n}). When 𝔛n\mathfrak{X}\_{n} is a polytope, this set is finite and the number
of constraints scales as Nn×|Ext⁡(𝔛n)|N\_{n}\times|\operatorname{Ext}(\mathfrak{X}\_{n})|. In general, Ext⁡(𝔛n)\operatorname{Ext}(\mathfrak{X}\_{n}) may be infinite, in which case the problem is semi-infinite and is solved via a separation-oracle-based cutting-plane method.

Algorithm 1  Cutting-Plane Algorithm for Solving the Tractable Formulation

1:Input: Sampling n∈𝒩n\in\mathcal{N}, samples {𝒳^n(j)}j=1Nn\{\widehat{\mathcal{X}}\_{n}^{(j)}\}\_{j=1}^{N\_{n}}, radius εn\varepsilon\_{n}, and support 𝔛n\mathfrak{X}\_{n}, and order p≥1p\geq 1.

2:Initialize: Set iteration counter k←0k\leftarrow 0. For each sample index j∈{1,…,Nn}j\in\{1,\dots,N\_{n}\}, initialize the active constraint set 𝒱j(0)⊆Ext⁡(conv⁡(𝔛n))\mathcal{V}\_{j}^{(0)}\subseteq\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n})) with any nonempty subset.

3:loop

4:  Solve Master Problem: Solve the relaxed problem with the current active sets {𝒱j(k)}\{\mathcal{V}\_{j}^{(k)}\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (u(k),λ(k),s(k),z(k))∈arg\displaystyle(u^{(k)},\lambda^{(k)},s^{(k)},z^{(k)})\in\arg | maxu,λ,s,z⁡1n​(−λ​εnp+1Nn​∑j=1Nnsj)\displaystyle\max\_{u,\lambda,s,z}\qquad\frac{1}{n}\left(-\lambda\varepsilon\_{n}^{p}+\frac{1}{N\_{n}}\sum\_{j=1}^{N\_{n}}s\_{j}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | min𝒳v∈𝒱j(k)⁡[U​(Φn​(u,𝒳v))+zj⊤​(𝒳v−𝒳^n(j))−Ωp​(zj,λ)]≥sj,∀j,\displaystyle\min\_{\mathcal{X}^{v}\in\mathcal{V}\_{j}^{(k)}}\left[U(\Phi\_{n}(u,\mathcal{X}^{v}))+z\_{j}^{\top}(\mathcal{X}^{v}-\widehat{\mathcal{X}}\_{n}^{(j)})-\Omega\_{p}(z\_{j},\lambda)\right]\geq s\_{j},\qquad\forall j, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λ≥0,u∈𝒰v​(n;η).\displaystyle\lambda\geq 0,\hskip 17.00024ptu\in\mathcal{U}\_{\rm v}(n;\eta). |  |

5:  Separation Oracles: For each j∈{1,…,Nn}j\in\{1,\dots,N\_{n}\}, compute a most violated constraint:

|  |  |  |
| --- | --- | --- |
|  | 𝒳j∗∈arg⁡min𝒳∈𝔛n⁡[U​(Φn​(u(k),𝒳))+(zj(k))⊤​(𝒳−𝒳^n(j))].\mathcal{X}\_{j}^{\*}\in\arg\min\_{\mathcal{X}\in\mathfrak{X}\_{n}}\left[U(\Phi\_{n}(u^{(k)},\mathcal{X}))+(z\_{j}^{(k)})^{\top}(\mathcal{X}-\widehat{\mathcal{X}}\_{n}^{(j)})\right]. |  |

Since the objective function is concave in 𝒳\mathcal{X} and 𝔛n\mathfrak{X}\_{n} is compact, the minimum is attained at an extreme point of conv⁡(𝔛n)\operatorname{conv}(\mathfrak{X}\_{n}).
Thus, this subproblem acts as a separation oracle for the semi-infinite constraint indexed by
Ext⁡(conv⁡(𝔛n))\operatorname{Ext}(\operatorname{conv}(\mathfrak{X}\_{n})).

6:  Let ϕj∗:=U​(Φn​(u(k),𝒳j∗))+(zj(k))⊤​(𝒳j∗−𝒳^n(j))\phi\_{j}^{\*}:=U(\Phi\_{n}(u^{(k)},\mathcal{X}\_{j}^{\*}))+(z\_{j}^{(k)})^{\top}(\mathcal{X}\_{j}^{\*}-\widehat{\mathcal{X}}\_{n}^{(j)}).

7:  Check for Convergence: If ϕj∗−Ωp​(zj(k),λ(k))≥sj(k)\phi\_{j}^{\*}-\Omega\_{p}(z\_{j}^{(k)},\lambda^{(k)})\geq s\_{j}^{(k)} for all j=1,…,Nnj=1,\dots,N\_{n}, then break.

8:  Add Cutting Planes: For each jj where the condition fails:

9:    Update 𝒱j(k+1)←𝒱j(k)∪{𝒳j∗}\mathcal{V}\_{j}^{(k+1)}\leftarrow\mathcal{V}\_{j}^{(k)}\cup\{\mathcal{X}\_{j}^{\*}\}

10:  Otherwise set 𝒱j(k+1)←𝒱j(k)\mathcal{V}\_{j}^{(k+1)}\leftarrow\mathcal{V}\_{j}^{(k)}.

11:  k←k+1k\leftarrow k+1.

12:end loop

13:Return (u(k),λ(k))(u^{(k)},\lambda^{(k)}) and the value for the given nn.

###### Remark A.1.

If 𝔛n\mathfrak{X}\_{n} is a polytope, Algorithm [1](https://arxiv.org/html/2602.04219v1#alg1 "Algorithm 1 ‣ Appendix A Algorithmic Implementation via Cutting-Plane Method ‣ Sampled-Data Wasserstein Distributionally Robust Control of Multiplicative Systems: A Convex Relaxation with Performance Guarantees This paper was supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants: NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.") terminates in finitely many iterations,
since only finitely many extreme-point constraints exist. For general compact 𝔛n\mathfrak{X}\_{n},
the algorithm implements a standard outer-approximation method for semi-infinite convex programs,
terminating once no violated extreme-point constraint can be found by the separation oracle.