---
authors:
- Jian'an Zhang
doc_id: arxiv:2511.17304v1
family_id: arxiv:2511.17304
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement
  Learning on Volatility Law Manifolds
url_abs: http://arxiv.org/abs/2511.17304v1
url_html: https://arxiv.org/html/2511.17304v1
venue: arXiv q-fin
version: 1
year: 2025
---


ZhangJian’an
  
Guanghua School of Management, Peking University
  
Peking University
  
Beijing, China
  
2501111059@stu.pku.edu.cn

###### Abstract

We study reinforcement learning (RL) on volatility surfaces through the lens of *Scientific AI*: can axiomatic market laws, enforced as soft penalties on a learned world model, reliably align high-capacity RL agents with no-arbitrage structure, or do they merely induce Goodhart-style exploitation of model artefacts?

Starting from classical static no-arbitrage conditions for implied volatility, we construct a finite-dimensional convex *volatility law manifold* of admissible total-variance surfaces, together with a metric-based *law-penalty functional* and a domain-agnostic *Graceful Failure Index* (GFI) that normalizes law degradation under shocks. A synthetic generator produces trajectories that are exactly law-consistent, while a recurrent neural world model is trained without law regularization and therefore predicts surfaces that deviate from the law manifold in structured ways.

On top of this testbed we introduce a *Goodhart decomposition* of reward, r=rℳ+r⟂r=r^{\mathcal{M}}+r^{\perp}, where rℳr^{\mathcal{M}} is the on-manifold component and r⟂r^{\perp} is *ghost arbitrage* arising purely from off-manifold prediction errors. We prove three flagship results: (i) a *ghost-arbitrage incentive* theorem showing that naive PPO-type RL is structurally driven to increase 𝔼​[r⟂]\mathbb{E}[r^{\perp}] whenever ghost arbitrage is available; (ii) a *law-strength trade-off* theorem establishing that increasing the weight on law penalties inevitably worsens P&L beyond a quantifiable threshold; and (iii) a *no-free-lunch* theorem stating that, under a law-consistent world model and a law-aligned structural class of strategies, unconstrained law-seeking RL cannot Pareto-dominate structural baselines on P&L, law penalties, and GFI.

Empirically, on a volatility world model calibrated to SPX/VIX-like grids, we compare naive RL, law-penalized and selection-only RL variants against simple structural baselines (Zero-Hedge, Vol-Trend, Random-Gaussian) across baseline and shocked regimes. In our experiments, structural baselines form the empirical law-strength frontier: they attain Sharpe ratios around 2–3 with low law penalties and GFI near zero, while all law-seeking RL variants achieve non-positive mean P&L and substantially higher GFI, despite being explicitly penalized for law violations. Frontier and diagnostic plots show that RL improvements in P&L are systematically accompanied by movement into high-penalty, high-GFI regions, consistent with our theoretical analysis.

Overall, volatility serves as a concrete case study where *reward shaping with verifiable penalties is not sufficient for law alignment*. Our framework—combining law manifolds, Goodhart decomposition, GFI, and law-strength frontiers—provides a reusable template for stress-testing Scientific AI systems and RL with verifiable rewards in other axiom-constrained domains such as yield curves, credit term structures, and physics-informed models.

*K*eywords volatility surfaces, reinforcement learning, axiomatic finance, no-arbitrage, law manifolds, Goodhart’s law, world models, scientific AI

## 1 Introduction

### 1.1 Scientific AI testbed: volatility law manifolds

In recent years, “AI for Science” has emerged as a central theme in machine learning, emphasizing scientific understanding and hypothesis-testing rather than purely predictive or profit-driven performance [[35](https://arxiv.org/html/2511.17304v1#bib.bib35), [36](https://arxiv.org/html/2511.17304v1#bib.bib36), [34](https://arxiv.org/html/2511.17304v1#bib.bib34)]. A key lesson from this line of work is that many scientific domains are governed by *axioms*—conservation laws, monotonicity constraints, or no-arbitrage principles—that carve out a structured admissible subset inside a high-dimensional function space. Scientific machine learning then seeks not only to interpolate observations, but to understand how learning agents interact with these law-constrained spaces under model misspecification, limited data, and changing environments.

Implied-volatility (IV) surfaces are a canonical example of such an axiomatic system in quantitative finance. Classical results show that no-arbitrage constraints—such as non-negativity of butterfly spreads, monotonicity in maturity, and convexity in strike—translate into linear or convex inequalities on total-variance smiles and surfaces [[1](https://arxiv.org/html/2511.17304v1#bib.bib1), [2](https://arxiv.org/html/2511.17304v1#bib.bib2), [3](https://arxiv.org/html/2511.17304v1#bib.bib3), [5](https://arxiv.org/html/2511.17304v1#bib.bib5), [6](https://arxiv.org/html/2511.17304v1#bib.bib6), [7](https://arxiv.org/html/2511.17304v1#bib.bib7)]. These conditions define a structured admissible subset of discretized surfaces that we refer to as a *volatility law manifold*. Recent work has revisited arbitrage-free interpolation and extrapolation of IV surfaces using convex optimization and sparse modeling [[14](https://arxiv.org/html/2511.17304v1#bib.bib14)], arbitrage-aware parametric families, and deep neural networks that aim to respect or softly penalize violations of these constraints [[68](https://arxiv.org/html/2511.17304v1#bib.bib68), [10](https://arxiv.org/html/2511.17304v1#bib.bib10), [15](https://arxiv.org/html/2511.17304v1#bib.bib15)]. In parallel, deep learning has been applied to option pricing and hedging via PDE and BSDE solvers [[30](https://arxiv.org/html/2511.17304v1#bib.bib30), [31](https://arxiv.org/html/2511.17304v1#bib.bib31)], and to rough or stochastic volatility models where direct calibration is challenging [[10](https://arxiv.org/html/2511.17304v1#bib.bib10)].

Our starting point is to treat this volatility-curve setting as a *Scientific AI testbed* rather than a trading system. We assume that the data-generating process—a synthetic but financially meaningful IV-surface generator—is exactly law-consistent: every realized surface lies on the no-arbitrage manifold defined by classical butterfly and calendar conditions [[1](https://arxiv.org/html/2511.17304v1#bib.bib1), [2](https://arxiv.org/html/2511.17304v1#bib.bib2), [6](https://arxiv.org/html/2511.17304v1#bib.bib6)]. A neural *world model* is trained to approximate this generator from data, similar in spirit to world-model approaches in model-based reinforcement learning (RL) [[40](https://arxiv.org/html/2511.17304v1#bib.bib40), [41](https://arxiv.org/html/2511.17304v1#bib.bib41), [42](https://arxiv.org/html/2511.17304v1#bib.bib42), [43](https://arxiv.org/html/2511.17304v1#bib.bib43), [44](https://arxiv.org/html/2511.17304v1#bib.bib44), [45](https://arxiv.org/html/2511.17304v1#bib.bib45)]. RL agents then interact only with the learned world model, never with the ground-truth generator. This creates a clean separation between a law-consistent environment and a potentially law-violating model, opening a “ghost channel” for agents to exploit model artefacts.

World models and latent dynamics learning have become central tools for sample-efficient RL in complex domains such as Atari, control, and strategy games [[40](https://arxiv.org/html/2511.17304v1#bib.bib40), [41](https://arxiv.org/html/2511.17304v1#bib.bib41), [42](https://arxiv.org/html/2511.17304v1#bib.bib42), [43](https://arxiv.org/html/2511.17304v1#bib.bib43), [47](https://arxiv.org/html/2511.17304v1#bib.bib47), [48](https://arxiv.org/html/2511.17304v1#bib.bib48), [49](https://arxiv.org/html/2511.17304v1#bib.bib49)]. At the same time, RL has a long history in quantitative finance, including early work on direct reinforcement learning for trading [[63](https://arxiv.org/html/2511.17304v1#bib.bib63), [64](https://arxiv.org/html/2511.17304v1#bib.bib64)], deep RL for portfolio management and execution [[65](https://arxiv.org/html/2511.17304v1#bib.bib65), [66](https://arxiv.org/html/2511.17304v1#bib.bib66), [67](https://arxiv.org/html/2511.17304v1#bib.bib67)], and deep hedging using neural networks trained on simulated scenarios [[68](https://arxiv.org/html/2511.17304v1#bib.bib68)]. Yet most of these studies focus on realized P&L, with limited attention to how learned policies interact with structural market axioms. Our goal is not to propose another trading system, but to use an RL-in-IV-surfaces setup as a controlled *experiment* on law-aligned learning and Goodhart phenomena.

A parallel literature in scientific machine learning has emphasized the incorporation of physical or axiomatic structure into learning systems via physics-informed neural networks [[32](https://arxiv.org/html/2511.17304v1#bib.bib32), [34](https://arxiv.org/html/2511.17304v1#bib.bib34)], relational inductive biases [[39](https://arxiv.org/html/2511.17304v1#bib.bib39)], and hybrid mechanistic–ML models [[36](https://arxiv.org/html/2511.17304v1#bib.bib36), [35](https://arxiv.org/html/2511.17304v1#bib.bib35)]. These works typically enforce or strongly bias the model toward satisfying known laws during training. In contrast, recent AI-safety and alignment research has documented how RL agents can exploit imperfect reward channels or specification gaps, a phenomenon often traced back to Goodhart’s law [[74](https://arxiv.org/html/2511.17304v1#bib.bib74), [75](https://arxiv.org/html/2511.17304v1#bib.bib75), [76](https://arxiv.org/html/2511.17304v1#bib.bib76), [77](https://arxiv.org/html/2511.17304v1#bib.bib77), [78](https://arxiv.org/html/2511.17304v1#bib.bib78), [79](https://arxiv.org/html/2511.17304v1#bib.bib79)]. This has led to proposals for RL with verifiable or externally checked rewards (RLVR) [[82](https://arxiv.org/html/2511.17304v1#bib.bib82)], where parts of the reward signal are computed via trusted procedures or checkers.

Our work bridges these lines of research in a finance-specific but conceptually general way. We design an axiomatic evaluation pipeline in which (i) a volatility law manifold encodes no-arbitrage axioms; (ii) a neural world model approximates a law-consistent generator but introduces model-induced “ghost” arbitrage opportunities; and (iii) RL agents are trained either with or without access to a *verifiable* law-penalty signal. We then ask a scientific question: when we add such verifiable penalties as soft terms in the RL objective, on top of a law-consistent ground-truth world, do we actually obtain more law-aligned and robust policies, or do we merely shift Goodhart behaviour onto model artefacts?

To foreshadow our main numerical findings, we consider a simple zero-position baseline (Zero-Hedge) that never trades. In our main setting, Zero-Hedge achieves mean step P&L of approximately 0.01910.0191 with a Graceful Failure Index (GFI) essentially zero and moderate law penalties, reflecting that the underlying world is law-consistent and shocks are symmetric. By contrast, a wide range of law-seeking RL variants—including soft-penalty PPO with a law-weight sweep (the “law-strength frontier”) and a selection-only variant that uses law penalties only for model selection—all attain *non-positive* mean step P&L and substantially worse GFI values (typically ≥1.6\geq 1.6), despite being explicitly penalized for law violations during training. In other words, once structural baselines are included, law-seeking RL has no free lunch: it fails to dominate even trivial strategies on the joint axes of profitability, law alignment, and tail risk.

### 1.2 Contributions

This paper makes four primary contributions, organized around an axiomatic evaluation framework rather than a specific trading algorithm.

##### C1 – Axiomatic evaluation framework.

Starting from any finite collection of convex or linear axioms on a discretized observable field, we construct (i) a law manifold ℳ\mathcal{M} in total-variance coordinates for implied-volatility surfaces, (ii) a metric-based law-penalty functional ℒϕ\mathcal{L}\_{\phi} that measures distance to ℳ\mathcal{M}, (iii) a domain-agnostic Graceful Failure Index (GFI) that normalizes degradation of law metrics under shocks, and (iv) *law-strength frontiers* that jointly organize profitability, law alignment, and tail robustness as a function of law-penalty weight λ\lambda and strategy class. While we instantiate this framework in an IV-surface world, the construction applies equally to other axiom-constrained systems such as yield curves, credit term structures, and physical fields constrained by conservation laws [[32](https://arxiv.org/html/2511.17304v1#bib.bib32), [34](https://arxiv.org/html/2511.17304v1#bib.bib34), [35](https://arxiv.org/html/2511.17304v1#bib.bib35)].

##### C2 – Ghost arbitrage & Goodhart decomposition.

We formalize a Goodhart-style decomposition of reward on law manifolds,

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=rℳ+r⟂,r=r^{\mathcal{M}}+r^{\perp}, |  | (1) |

where rℳr^{\mathcal{M}} is the on-manifold reward that would be obtained under a perfectly law-consistent world, and r⟂r^{\perp} is an off-manifold “ghost arbitrage” component induced by the neural world model. We show how this decomposition can be implemented using a projection operator onto ℳ\mathcal{M} in total-variance space and an explicit law-penalty functional, making the ghost component measurable and analyzable. This connects Goodhart’s law in AI safety [[74](https://arxiv.org/html/2511.17304v1#bib.bib74), [75](https://arxiv.org/html/2511.17304v1#bib.bib75), [78](https://arxiv.org/html/2511.17304v1#bib.bib78)] with concrete financial law violations (e.g., butterfly or calendar arbitrage) in our IV-surface testbed.

##### C3 – Flagship incentive and trade-off results.

On top of this axiomatic pipeline, we establish three central theoretical results that together form a no-free-lunch story for law-seeking RL. Theorem 4.1 (*Ghost-arbitrage incentive for naive RL*) shows that, under mild assumptions, naive PPO-type RL is structurally incentivized to increase 𝔼​[r⟂]\mathbb{E}[r^{\perp}] whenever structural law-consistent baselines already approximate the on-manifold optimum. Theorem 4.3 and Corollary 4.4 (*Law-strength trade-off*) prove that increasing the law-penalty weight λ\lambda inevitably worsens P&L beyond a threshold: the empirical law-strength frontier we observe in experiments is a structural trade-off, not an artefact of hyperparameters. Finally, Theorem 8.1 (*No-free-lunch for law-seeking RL*) shows that, given a law-consistent world model and a sufficiently rich structural baseline class 𝒮\mathcal{S}, unconstrained law-seeking RL cannot simultaneously dominate 𝒮\mathcal{S} on P&L and on all law metrics unless it effectively recovers a policy in 𝒮\mathcal{S}.

##### C4 – Design lessons for law-aligned learning and RLVR.

Our analysis yields practical design lessons that generalize beyond volatility modeling. First, merely adding soft law penalties to the reward is insufficient for robust law alignment: RL agents systematically exploit ghost arbitrage channels in the world model, or else sacrifice P&L without achieving net law improvements. Second, law alignment benefits from *structural* interventions such as hard constraints, projection layers onto ℳ\mathcal{M}, and structured policy classes that encode hedging logic, echoing observations from physics-informed learning and scientific ML [[32](https://arxiv.org/html/2511.17304v1#bib.bib32), [34](https://arxiv.org/html/2511.17304v1#bib.bib34), [36](https://arxiv.org/html/2511.17304v1#bib.bib36)]. Third, our pipeline serves as a reusable testbed for RL with verifiable rewards (RLVR) [[82](https://arxiv.org/html/2511.17304v1#bib.bib82)]: law penalties here are fully verifiable and domain-grounded, yet we still observe Goodhart-like failures when structural constraints are absent.

### 1.3 Scope and novelty

##### Geometric/systematization of known results.

Section [2](https://arxiv.org/html/2511.17304v1#S2 "2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") recasts classical no-arbitrage characterizations of admissible IV surfaces—butterfly convexity, calendar monotonicity, and related inequalities [[1](https://arxiv.org/html/2511.17304v1#bib.bib1), [2](https://arxiv.org/html/2511.17304v1#bib.bib2), [3](https://arxiv.org/html/2511.17304v1#bib.bib3), [5](https://arxiv.org/html/2511.17304v1#bib.bib5), [6](https://arxiv.org/html/2511.17304v1#bib.bib6), [7](https://arxiv.org/html/2511.17304v1#bib.bib7)]—as a finite-dimensional convex polyhedral law manifold in total-variance coordinates. This representation theorem does not aim to replace existing no-arbitrage results; instead, it systematizes them into a form amenable to projection, distance computation, and integration into learning systems.

##### New concepts and metrics.

The concrete ghost-arbitrage decomposition on a learned world model, the construction of law-strength frontiers, and the definition of the GFI are new. They are designed to be domain-agnostic: given any axiom-constrained system and an exogenous notion of shock, the same machinery can be instantiated to quantify how agents trade off performance, law alignment, and tail robustness, extending ideas from scientific ML and AI-for-Science benchmarks [[35](https://arxiv.org/html/2511.17304v1#bib.bib35), [36](https://arxiv.org/html/2511.17304v1#bib.bib36), [32](https://arxiv.org/html/2511.17304v1#bib.bib32), [34](https://arxiv.org/html/2511.17304v1#bib.bib34)].

##### New theoretical results.

Our main theoretical novelties lie in Theorem 4.1, Theorem 4.3 with Corollary 4.4, and Theorem 8.1. Together, they formalize: (i) an incentive for naive RL to exploit ghost arbitrage in law-consistent worlds; (ii) a structural law-strength trade-off that bounds achievable P&L for any given level of law penalty; and (iii) a no-free-lunch result for unconstrained law-seeking RL relative to a law-consistent structural baseline class 𝒮\mathcal{S}. We stress that these are not new no-arbitrage theorems per se, but results about RL behaviour on top of an axiomatic evaluation pipeline. Our contribution is to show, both theoretically and empirically, that soft law penalties on a learned world model do not automatically yield law-aligned robustness once structural baselines are taken into account.

##### Scope disclaimer.

We work with a finite-dimensional convex template: our “law manifold” is a structured subset of a discretized IV-surface grid, not a smooth manifold in the differential-geometric sense. We retain the term “manifold” for continuity with the broader literature on manifold-constrained learning, but in our volatility instantiation ℳvol\mathcal{M}^{\mathrm{vol}} is a convex polyhedral subset defined by linear inequalities and positivity constraints. Our theorems are proved under this finite-dimensional convex template and a specific class of model-based RL algorithms; a fully general analysis for infinite-dimensional function spaces and arbitrary RL algorithms is left for future work.

### 1.4 Key concepts at a glance

Given the number of concepts introduced, we summarize the most important ones in Table [1](https://arxiv.org/html/2511.17304v1#S1.T1 "Table 1 ‣ 1.4 Key concepts at a glance ‣ 1 Introduction ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). Each concept is defined precisely in later sections; here we provide a high-level description and a pointer.

Table 1: Key concepts at a glance. Formal definitions and constructions are given in the indicated sections.

| Concept | Plain-English description | Section |
| --- | --- | --- |
| Law manifold ℳ\mathcal{M} | Admissible subset of discretized IV surfaces satisfying butterfly, calendar, and related no-arbitrage axioms. | Sec. 2.0–2.1 |
| Law penalty ℒϕ\mathcal{L}\_{\phi} | Distance-based functional measuring how far a surface lies outside ℳ\mathcal{M}, with ϕ\phi encoding the chosen metric (e.g., squared ℓ2\ell\_{2} in total-variance space). | Sec. 2.3 |
| Ghost arbitrage r⟂r^{\perp} | Component of reward obtainable only by moving off ℳ\mathcal{M} through world-model artefacts; vanishes under a perfectly law-consistent environment. | Sec. 2.4, 3.3 |
| Law-strength frontier | Trade-off curve tracing profitability, law alignment, and tail risk as a function of law-penalty weight λ\lambda and strategy class. | Sec. 4.4, 7.3 |
| Graceful Failure Index (GFI) | Normalized measure of how much law metrics (e.g., mean penalty, coverage) degrade under shocks relative to baseline conditions. | Sec. 4.4, 6.3 |
| Structural class 𝒮\mathcal{S} | Low-capacity, law-consistent strategies such as Zero-Hedge and Vol-Trend that serve as structural baselines. | Sec. 5, 8.1 |
| Neural world model | Learned dynamics model for IV surfaces that approximates the law-consistent generator but opens a ghost channel for arbitrage. | Sec. 3 |

### 1.5 Research questions

The paper is organized around three research questions (RQs) that probe different aspects of law-seeking RL on axiomatic pipelines.

##### RQ1 – Do law penalties help naive RL?

Does law-penalized RL actually reduce law violations and improve graceful failure compared to naive RL on the *same* learned world model? If soft penalties are effective, we should observe strictly better GFI and law metrics (mean and max law penalty, law coverage) at comparable P&L along the law-strength frontier. If not, we obtain a negative result for soft-penalty shaping: verifiable law penalties alone do not suffice to align RL with axioms in the presence of model-induced ghost arbitrage.

##### RQ2 – How does RL compare to structural baselines?

How do RL policies (naive, soft law-seeking, and selection-only) compare to structural baselines (such as Zero-Hedge, Random-Gaussian, and Vol-Trend) on the joint risk–law trade-off, both under baseline conditions and under volatility shocks? We evaluate these policies relative to a structural Pareto frontier induced by 𝒮\mathcal{S} in the space of P&L, law metrics, and tail-risk measures such as Value-at-Risk (VaR) and Conditional VaR (CVaR) [[21](https://arxiv.org/html/2511.17304v1#bib.bib21), [22](https://arxiv.org/html/2511.17304v1#bib.bib22)]. This addresses whether law-seeking RL provides any Pareto improvement once simple, law-consistent strategies are included.

##### RQ3 – When does law-seeking RL have no free lunch?

Under what assumptions on the structural class 𝒮\mathcal{S}, the unconstrained policy class Π\Pi, and the neural world model do we obtain a no-free-lunch result for law-seeking RL? Theorem 8.1 formalizes one such setting: if 𝒮\mathcal{S} already approximates the on-manifold optimum and the world model introduces a non-trivial ghost component, then either RL behaves like a structural strategy in 𝒮\mathcal{S} or it fails to dominate 𝒮\mathcal{S} jointly on P&L and law metrics. Section 8.1 spells out the assumptions and proof sketch, and Section 8.2 discusses how this volatility-specific case informs broader questions in law-aligned learning and RL with verifiable rewards [[75](https://arxiv.org/html/2511.17304v1#bib.bib75), [76](https://arxiv.org/html/2511.17304v1#bib.bib76), [74](https://arxiv.org/html/2511.17304v1#bib.bib74), [82](https://arxiv.org/html/2511.17304v1#bib.bib82)].

In the remainder of the paper, we address RQ1–RQ3 in order. Section 2 formalizes law manifolds, penalties, and the Goodhart decomposition. Section 3 introduces the synthetic law-consistent IV generator and the neural world model. Section 4 develops incentive and trade-off results for law-seeking RL, and Section 5 defines structural baselines. Section 6 details the experimental protocol, and Section 7 presents empirical results on dynamics plots, law-strength frontiers, and diagnostic scatter/histograms. Section 8 discusses the no-free-lunch theorem and implications for RLVR and scientific AI, and Section 9 concludes.

## 2 Axiomatic Volatility Law Manifolds

### 2.0 Finite-Dimensional Convex Template and Notation

In this section we formalize the notion of a *law manifold* as a finite-dimensional convex subset of a discretized function space, induced by a collection of axioms. We emphasize from the outset that our construction is intentionally elementary:

> We use a simple finite-dimensional convex template; our “manifold” is a structured subset in discretized coordinates, not a smooth differentiable manifold in the differential-geometry sense. We keep the term *manifold* for continuity with the broader literature on manifold-constrained learning and manifold regularization [[28](https://arxiv.org/html/2511.17304v1#bib.bib28), [29](https://arxiv.org/html/2511.17304v1#bib.bib29)], although in our discretized volatility setting ℳvol\mathcal{M}^{\mathrm{vol}} is a convex polyhedral subset of a Euclidean space.

##### General template.

Let d∈ℕd\in\mathbb{N} and consider a finite-dimensional observation space

|  |  |  |
| --- | --- | --- |
|  | 𝒴⊆ℝd,\mathcal{Y}\subseteq\mathbb{R}^{d}, |  |

equipped with the standard Euclidean inner product and norm ∥⋅∥2\|\cdot\|\_{2}. We think of y∈𝒴y\in\mathcal{Y} as a discretized field: a yield curve, an implied-volatility surface, or any other structured observable.

We assume that the domain is endowed with a finite family of convex *axiom functions*

|  |  |  |
| --- | --- | --- |
|  | Ai:𝒴→ℝ,i=1,…,m,A\_{i}:\mathcal{Y}\to\mathbb{R},\qquad i=1,\dots,m, |  |

encoding domain-specific constraints (e.g., butterfly or calendar conditions in volatility, or monotonicity of yields). We write A​(y)≤0A(y)\leq 0 as shorthand for the componentwise inequalities Ai​(y)≤0A\_{i}(y)\leq 0 for all ii.

###### Definition 1 (Law manifold).

Given convex axiom functions {Ai}i=1m\{A\_{i}\}\_{i=1}^{m}, the associated *law manifold* is

|  |  |  |
| --- | --- | --- |
|  | ℳ:={y∈𝒴:Ai​(y)≤0​ for all ​i=1,…,m}.\mathcal{M}\;:=\;\bigl\{\,y\in\mathcal{Y}:A\_{i}(y)\leq 0\text{ for all }i=1,\dots,m\,\bigr\}. |  |

In general ℳ\mathcal{M} is a closed convex subset of ℝd\mathbb{R}^{d} whenever each AiA\_{i} is lower semicontinuous and convex. In many practical cases—including our volatility and yield-curve examples below—the constraints are linear or piecewise linear, so that ℳ\mathcal{M} is a polyhedron.

##### Law-penalty functional.

To quantify violations of the axioms, we define a *law-penalty functional* via a generalized distance to ℳ\mathcal{M}.

###### Definition 2 (Law-penalty functional).

Let ϕ:ℝd→[0,∞)\phi:\mathbb{R}^{d}\to[0,\infty) be a continuous function with ϕ​(0)=0\phi(0)=0 and ϕ​(z)→∞\phi(z)\to\infty as ‖z‖2→∞\|z\|\_{2}\to\infty (e.g., ϕ​(z)=12​‖z‖22\phi(z)=\tfrac{1}{2}\|z\|\_{2}^{2} or a weighted Sobolev norm). Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒϕ​(y):=infy~∈ℳϕ​(y−y~),y∈𝒴.\mathcal{L}\_{\phi}(y)\;:=\;\inf\_{\tilde{y}\in\mathcal{M}}\,\phi(y-\tilde{y}),\qquad y\in\mathcal{Y}. |  | (2) |

When ϕ​(z)=12​‖z‖22\phi(z)=\tfrac{1}{2}\|z\|\_{2}^{2} and ℳ\mathcal{M} is closed and convex, ℒϕ​(y)\mathcal{L}\_{\phi}(y) reduces to the squared Euclidean distance to ℳ\mathcal{M}. More general choices of ϕ\phi allow us to reweight different coordinates, incorporate smoothness, or emphasize particular directions in state space, in the spirit of manifold regularization [[28](https://arxiv.org/html/2511.17304v1#bib.bib28)].

##### Non-financial example: yield curves.

To underline transferability beyond volatility, consider a discretized yield curve

|  |  |  |
| --- | --- | --- |
|  | y=(y1,…,yJ)∈ℝJ,y=(y\_{1},\dots,y\_{J})\in\mathbb{R}^{J}, |  |

where yjy\_{j} denotes the continuously compounded spot yield for maturity τj\tau\_{j}, with 0<τ1<⋯<τJ0<\tau\_{1}<\dots<\tau\_{J}. Classical term-structure theory [[18](https://arxiv.org/html/2511.17304v1#bib.bib18)] and curve-construction practice [[17](https://arxiv.org/html/2511.17304v1#bib.bib17)] suggest axioms such as:

1. 1.

   *Monotonicity*: yields are non-decreasing in maturity,
   yj+1≥yj∀j.y\_{j+1}\geq y\_{j}\quad\forall j.
2. 2.

   *Convexity of discount factors*: implied by non-negative forward rates, giving linear inequalities in yy.

These conditions can be encoded as linear maps Ai​(y)A\_{i}(y), yielding a polyhedral law manifold ℳyc⊂ℝJ\mathcal{M}^{\mathrm{yc}}\subset\mathbb{R}^{J} and an associated law penalty ℒϕyc\mathcal{L}\_{\phi}^{\mathrm{yc}} measuring monotonicity/convexity violations. Our volatility manifold in Sections [2.1](https://arxiv.org/html/2511.17304v1#S2.SS1 "2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[2.3](https://arxiv.org/html/2511.17304v1#S2.SS3 "2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") is an instance of this general template.

##### Notation summary.

Throughout the paper we use the following notation; we repeat it here for convenience.

1. 1.

   yy: generic observable (e.g., yield curve, volatility surface) in a finite-dimensional space 𝒴⊆ℝd\mathcal{Y}\subseteq\mathbb{R}^{d}.
2. 2.

   ℳ\mathcal{M}: generic law manifold (closed convex subset of ℝd\mathbb{R}^{d}) induced by axioms.
3. 3.

   σ\sigma: implied volatility on a maturity–log-moneyness grid; w=σ2​Tw=\sigma^{2}T denotes total variance, our primary state variable for volatility.
4. 4.

   ℳvol\mathcal{M}^{\mathrm{vol}}: volatility-specific law manifold defined in Section [2.1](https://arxiv.org/html/2511.17304v1#S2.SS1 "2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
5. 5.

   ℒϕ\mathcal{L}\_{\phi}: law-penalty functional defined in ([2](https://arxiv.org/html/2511.17304v1#S2.E2 "In Definition 2 (Law-penalty functional). ‣ Law-penalty functional. ‣ 2.0 Finite-Dimensional Convex Template and Notation ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")); in experiments we take ϕ​(z)=12​‖z‖22\phi(z)=\tfrac{1}{2}\|z\|\_{2}^{2} on the total-variance grid.
6. 6.

   Πℳ\Pi\_{\mathcal{M}}: metric projection onto ℳ\mathcal{M} (in Euclidean norm), whose existence and regularity rely on closedness and convexity [[26](https://arxiv.org/html/2511.17304v1#bib.bib26)].
7. 7.

   rℳr^{\mathcal{M}}, r⟂r^{\perp}: on-manifold reward and *ghost-arbitrage* components of the reward, defined via projection in Section [2.4](https://arxiv.org/html/2511.17304v1#S2.SS4 "2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

### 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron

We now instantiate the general template for implied volatility surfaces. Let C​(K,T)C(K,T) denote the (discounted) price of a European call with strike KK and maturity TT, and σ​(K,T)\sigma(K,T) its Black–Scholes implied volatility. Following standard practice [[2](https://arxiv.org/html/2511.17304v1#bib.bib2), [1](https://arxiv.org/html/2511.17304v1#bib.bib1)], we work in terms of total variance

|  |  |  |
| --- | --- | --- |
|  | w​(K,T):=σ​(K,T)2​T,w(K,T):=\sigma(K,T)^{2}T, |  |

discretized on a finite grid of maturities T1<⋯<TNTT\_{1}<\dots<T\_{N\_{T}} and log-moneyness k1<⋯<kNKk\_{1}<\dots<k\_{N\_{K}}.

Classical static no-arbitrage conditions for European options (no butterfly arbitrage across strikes and no calendar arbitrage across maturities) can be expressed as linear inequalities in either call prices or total variance, see e.g. [[16](https://arxiv.org/html/2511.17304v1#bib.bib16), [8](https://arxiv.org/html/2511.17304v1#bib.bib8)]. We briefly summarize the discretized form relevant to our construction.

##### Butterfly (strike) convexity.

For each fixed maturity TiT\_{i}, the call price as a function of strike must be convex and decreasing. On a grid {kj}\{k\_{j}\} this gives discrete convexity constraints such as

|  |  |  |
| --- | --- | --- |
|  | Ci,j−1−2​Ci,j+Ci,j+1≥0,C\_{i,j-1}-2C\_{i,j}+C\_{i,j+1}\geq 0, |  |

and monotonicity constraints Ci,j+1≤Ci,jC\_{i,j+1}\leq C\_{i,j} for all jj. These translate into linear inequalities in wi,jw\_{i,j} via the Black–Scholes formula.

##### Calendar monotonicity.

For each fixed strike (log-moneyness) kjk\_{j}, call prices must be increasing in maturity, yielding

|  |  |  |
| --- | --- | --- |
|  | Ci+1,j≥Ci,jfor all ​i.C\_{i+1,j}\geq C\_{i,j}\quad\text{for all }i. |  |

Again, these can be expressed as linear inequalities in (wi,j)(w\_{i,j}) using the monotonicity of Black–Scholes prices in variance.

Collecting all discrete butterfly and calendar inequalities, we obtain a linear mapping

|  |  |  |
| --- | --- | --- |
|  | Avol:ℝdvol→ℝm,A^{\mathrm{vol}}:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathbb{R}^{m}, |  |

where dvol=NT​NKd\_{\mathrm{vol}}=N\_{T}N\_{K} is the number of grid points and mm is the number of constraints.

###### Definition 3 (Volatility law manifold).

Let w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}} denote the vector of total variances on the (T,k)(T,k)-grid. The *volatility law manifold* is the polyhedral set

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳvol:={w∈ℝdvol:Avol​w≤0},\mathcal{M}^{\mathrm{vol}}\;:=\;\bigl\{\,w\in\mathbb{R}^{d\_{\mathrm{vol}}}:A^{\mathrm{vol}}w\leq 0\,\bigr\}, |  | (3) |

where Avol​w≤0A^{\mathrm{vol}}w\leq 0 encodes all discretized butterfly and calendar no-arbitrage inequalities, as well as basic box constraints wmin≤wi,j≤wmaxw\_{\min}\leq w\_{i,j}\leq w\_{\max}.

The following proposition packages the textbook no-arbitrage conditions into a geometric representation.

###### Proposition 1 (Axiomatic representation of volatility law manifold).

Assume that the discretized butterfly and calendar constraints are given as a finite system of linear inequalities Avol​w≤bA^{\mathrm{vol}}w\leq b for some matrix Avol∈ℝm×dvolA^{\mathrm{vol}}\in\mathbb{R}^{m\times d\_{\mathrm{vol}}} and vector b∈ℝmb\in\mathbb{R}^{m}. Then:

1. 1.

   ℳvol\mathcal{M}^{\mathrm{vol}} is a non-empty, closed, convex polyhedron in ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.
2. 2.

   Any total-variance surface ww corresponding to a static-arbitrage-free implied volatility surface lies in ℳvol\mathcal{M}^{\mathrm{vol}}.

###### Proof sketch.

Closedness and convexity follow directly from the fact that ℳvol\mathcal{M}^{\mathrm{vol}} is the intersection of finitely many closed half-spaces {w:aℓ⊤​w≤bℓ}\{w:a\_{\ell}^{\top}w\leq b\_{\ell}\} and box constraints. Non-emptiness is guaranteed by the existence of at least one model (e.g., a Black–Scholes surface with constant volatility) satisfying the inequalities. The mapping from continuous no-arbitrage conditions to discrete linear constraints is standard; see e.g. [[2](https://arxiv.org/html/2511.17304v1#bib.bib2)], [[8](https://arxiv.org/html/2511.17304v1#bib.bib8)] and references therein. A detailed construction and proof are given in Appendix A.
∎

### 2.2 Geometry and Convexity Properties

The closed and convex nature of ℳvol\mathcal{M}^{\mathrm{vol}} is more than a technicality: it ensures the existence of well-behaved projection operators and law penalties.

###### Proposition 2 (Closedness, convexity, and metric projection).

The volatility law manifold ℳvol\mathcal{M}^{\mathrm{vol}} defined in ([3](https://arxiv.org/html/2511.17304v1#S2.E3 "In Definition 3 (Volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) is a non-empty, closed, convex subset of ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}. Consequently:

1. 1.

   For every w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}} there exists a unique Euclidean projection

   |  |  |  |
   | --- | --- | --- |
   |  | Πℳvol​(w):=arg⁡minw~∈ℳvol⁡‖w−w~‖2.\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w):=\arg\min\_{\tilde{w}\in\mathcal{M}^{\mathrm{vol}}}\|w-\tilde{w}\|\_{2}. |  |
2. 2.

   The projection operator Πℳvol:ℝdvol→ℳvol\Pi\_{\mathcal{M}^{\mathrm{vol}}}:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathcal{M}^{\mathrm{vol}} is 11-Lipschitz:

   |  |  |  |
   | --- | --- | --- |
   |  | ‖Πℳvol​(w)−Πℳvol​(w′)‖2≤‖w−w′‖2∀w,w′.\|\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w)-\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w^{\prime})\|\_{2}\leq\|w-w^{\prime}\|\_{2}\quad\forall w,w^{\prime}. |  |

###### Proof sketch.

Closedness and convexity follow from Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). The properties of Πℳvol\Pi\_{\mathcal{M}^{\mathrm{vol}}} are standard for projections onto closed convex sets in Hilbert spaces; see, e.g., [[26](https://arxiv.org/html/2511.17304v1#bib.bib26), Chap. 3]. Full details are provided in Appendix A.
∎

The existence and regularity of Πℳvol\Pi\_{\mathcal{M}^{\mathrm{vol}}} allow us to treat law penalties as squared distances to the manifold and to define projection-based decompositions of reward functionals later on.

### 2.3 Law-Penalty Functionals and Ghost Sensitivity

We now specialize the general law-penalty functional ([2](https://arxiv.org/html/2511.17304v1#S2.E2 "In Definition 2 (Law-penalty functional). ‣ Law-penalty functional. ‣ 2.0 Finite-Dimensional Convex Template and Notation ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) to the volatility setting. Let w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}} denote a (possibly law-violating) total-variance surface, and let

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(z)=12​‖z‖22,z∈ℝdvol.\phi(z)\;=\;\frac{1}{2}\|z\|\_{2}^{2},\qquad z\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  | (4) |

We define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒvol(w):=infw~∈ℳvol12∥w−w~∥22=12dist(w,ℳvol)2,\mathcal{L}\_{\mathrm{vol}}(w)\;:=\;\inf\_{\tilde{w}\in\mathcal{M}^{\mathrm{vol}}}\frac{1}{2}\|w-\tilde{w}\|\_{2}^{2}\;=\;\frac{1}{2}\operatorname{dist}(w,\mathcal{M}^{\mathrm{vol}})^{2}, |  | (5) |

where dist⁡(w,ℳvol):=‖w−Πℳvol​(w)‖2\operatorname{dist}(w,\mathcal{M}^{\mathrm{vol}}):=\|w-\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w)\|\_{2}.

In practice we implement ℒvol\mathcal{L}\_{\mathrm{vol}} via a sum of local violations (e.g., squared negative parts of discrete butterfly and calendar inequalities), which is equivalent to ([5](https://arxiv.org/html/2511.17304v1#S2.E5 "In 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) up to scaling on our discretization.

###### Lemma 1 (Local Lipschitz continuity of law penalty).

The volatility law-penalty functional ℒvol\mathcal{L}\_{\mathrm{vol}} in ([5](https://arxiv.org/html/2511.17304v1#S2.E5 "In 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) is locally Lipschitz on ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.

###### Proof sketch.

ℒvol​(w)=12​‖w−Πℳvol​(w)‖22\mathcal{L}\_{\mathrm{vol}}(w)=\tfrac{1}{2}\|w-\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w)\|\_{2}^{2} and Πℳvol\Pi\_{\mathcal{M}^{\mathrm{vol}}} is 1-Lipschitz by Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). Thus ℒvol\mathcal{L}\_{\mathrm{vol}} is the composition of Lipschitz maps and a smooth quadratic, which yields local Lipschitz continuity; see also standard results on Moreau envelopes [[26](https://arxiv.org/html/2511.17304v1#bib.bib26)]. A full proof is given in Appendix A.
∎

The following basic property connects ℒvol\mathcal{L}\_{\mathrm{vol}} with axiomatic consistency and will be used repeatedly when interpreting empirical law metrics.

###### Proposition 3 (Zero penalty iff axiomatic consistency).

For any w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}},

|  |  |  |
| --- | --- | --- |
|  | ℒvol​(w)=0⟺w∈ℳvol.\mathcal{L}\_{\mathrm{vol}}(w)=0\quad\Longleftrightarrow\quad w\in\mathcal{M}^{\mathrm{vol}}. |  |

###### Proof sketch.

If w∈ℳvolw\in\mathcal{M}^{\mathrm{vol}} then choosing w~=w\tilde{w}=w in ([5](https://arxiv.org/html/2511.17304v1#S2.E5 "In 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields ℒvol​(w)=0\mathcal{L}\_{\mathrm{vol}}(w)=0. Conversely, if ℒvol​(w)=0\mathcal{L}\_{\mathrm{vol}}(w)=0 then the infimum in ([5](https://arxiv.org/html/2511.17304v1#S2.E5 "In 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) is attained at w~⋆=Πℳvol​(w)\tilde{w}^{\star}=\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w) with ‖w−w~⋆‖2=0\|w-\tilde{w}^{\star}\|\_{2}=0, hence w=w~⋆∈ℳvolw=\tilde{w}^{\star}\in\mathcal{M}^{\mathrm{vol}}. Details appear in Appendix A.
∎

###### Remark 1 (Choice of ϕ\phi and ghost sensitivity).

The choice ϕ​(z)=12​‖z‖22\phi(z)=\tfrac{1}{2}\|z\|\_{2}^{2} treats all grid points uniformly and yields a particularly simple gradient

|  |  |  |
| --- | --- | --- |
|  | ∇ℒvol​(w)=w−Πℳvol​(w)\nabla\mathcal{L}\_{\mathrm{vol}}(w)=w-\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w) |  |

almost everywhere. Alternative choices of ϕ\phi (e.g., weighted ℓ2\ell\_{2} norms emphasizing short maturities, or discrete Sobolev norms penalizing roughness in TT and kk) change the relative sensitivity of ℒϕ\mathcal{L}\_{\phi} to localized versus global law violations. Exploring how this affects the *ghost arbitrage* exploited by RL policies is an interesting axis for future work.

### 2.4 Goodhart Decomposition on Law Manifolds (Conceptual)

The law manifold and penalty enable a conceptual decomposition of any reward functional into an on-manifold and an off-manifold (ghost-arbitrage) component. This decomposition underlies our Goodhart-style analysis of RL in later sections and is instantiated concretely for our world model in Section 3.3.

Let r:ℝdvol→ℝr:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathbb{R} denote a generic reward functional of a total-variance surface ww (e.g., the one-step P&L of a hedging strategy). We assume that rr is locally Lipschitz on ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}, a mild condition satisfied in all our models.

###### Definition 4 (Projection-based Goodhart decomposition).

Let Πℳvol\Pi\_{\mathcal{M}^{\mathrm{vol}}} be the metric projection onto ℳvol\mathcal{M}^{\mathrm{vol}}. Define the *on-manifold* reward

|  |  |  |
| --- | --- | --- |
|  | rℳ​(w):=r​(Πℳvol​(w)),r^{\mathcal{M}}(w):=r\bigl(\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w)\bigr), |  |

and the *ghost-arbitrage* component

|  |  |  |
| --- | --- | --- |
|  | r⟂​(w):=r​(w)−rℳ​(w).r^{\perp}(w):=r(w)-r^{\mathcal{M}}(w). |  |

We refer to the decomposition

|  |  |  |
| --- | --- | --- |
|  | r​(w)=rℳ​(w)+r⟂​(w)r(w)=r^{\mathcal{M}}(w)+r^{\perp}(w) |  |

as the *Goodhart decomposition* of rr on the volatility law manifold.

By construction, rℳr^{\mathcal{M}} depends on ww only through its projection onto ℳvol\mathcal{M}^{\mathrm{vol}}, and is thus invariant under off-manifold perturbations that leave Πℳvol​(w)\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w) unchanged. The residual r⟂r^{\perp} captures gains or losses that arise solely from moving away from the law manifold—precisely the *ghost arbitrage* channel that law-seeking RL may exploit.

###### Definition 5 (Ghost arbitrage).

The *ghost-arbitrage reward* associated with a reward functional rr and law manifold ℳvol\mathcal{M}^{\mathrm{vol}} is the component r⟂r^{\perp} in Definition [4](https://arxiv.org/html/2511.17304v1#Thmdefinition4 "Definition 4 (Projection-based Goodhart decomposition). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). A policy that maximizes 𝔼​[r⟂]\mathbb{E}[r^{\perp}] subject to small ℒvol\mathcal{L}\_{\mathrm{vol}} can be said to exploit ghost arbitrage: it harvests reward from off-manifold distortions that are negligible under the coarse law penalty but significant for P&L.

The following proposition makes explicit how the magnitude of ghost arbitrage is controlled by the distance to the law manifold whenever rr is Lipschitz. This link is used later when we interpret empirical law penalties and our Graceful Failure Index.

###### Proposition 4 (Ghost reward bounded by law distance).

Suppose rr is LrL\_{r}-Lipschitz on ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}} with respect to ∥⋅∥2\|\cdot\|\_{2}. Then for all ww,

|  |  |  |
| --- | --- | --- |
|  | |r⟂​(w)|=|r​(w)−rℳ​(w)|≤Lr​dist⁡(w,ℳvol)=Lr​2​ℒvol​(w).|r^{\perp}(w)|=\bigl|r(w)-r^{\mathcal{M}}(w)\bigr|\leq L\_{r}\,\operatorname{dist}\bigl(w,\mathcal{M}^{\mathrm{vol}}\bigr)=L\_{r}\sqrt{2\,\mathcal{L}\_{\mathrm{vol}}(w)}. |  |

###### Proof sketch.

By the Lipschitz property of rr,

|  |  |  |
| --- | --- | --- |
|  | |r​(w)−rℳ​(w)|=|r​(w)−r​(Πℳvol​(w))|≤Lr​‖w−Πℳvol​(w)‖2=Lr​dist⁡(w,ℳvol).|r(w)-r^{\mathcal{M}}(w)|=\bigl|r(w)-r(\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w))\bigr|\leq L\_{r}\,\|w-\Pi\_{\mathcal{M}^{\mathrm{vol}}}(w)\|\_{2}=L\_{r}\,\operatorname{dist}(w,\mathcal{M}^{\mathrm{vol}}). |  |

Using ℒvol(w)=12dist(w,ℳvol)2\mathcal{L}\_{\mathrm{vol}}(w)=\tfrac{1}{2}\operatorname{dist}(w,\mathcal{M}^{\mathrm{vol}})^{2} from ([5](https://arxiv.org/html/2511.17304v1#S2.E5 "In 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields the final identity. A more general version, allowing non-Euclidean ϕ\phi, is treated in Appendix A.
∎

Proposition [4](https://arxiv.org/html/2511.17304v1#Thmproposition4 "Proposition 4 (Ghost reward bounded by law distance). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") shows that, in a purely metric sense, large ghost rewards require non-negligible law violations. The central question of this paper is whether, under a learned world model, RL training can nonetheless systematically exploit directions in which ghost reward grows “too quickly” relative to the coarse law-penalty captured by ℒvol\mathcal{L}\_{\mathrm{vol}}, leading to misaligned but high-P&L policies. This question is addressed empirically in Sections [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and theoretically in Theorems 4.1 and 8.1.

## 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions

In this section we formalize the dynamic data-generating process for implied-volatility surfaces and the learned neural world model on which all reinforcement-learning (RL) agents are trained. The key structural feature is that the *synthetic generator* is, by construction, perfectly law-consistent—its surfaces lie on the polyhedral law manifold ℳvol\mathcal{M}^{\mathrm{vol}} almost surely—whereas the neural world model is trained purely by prediction error and hence produces *law-violating* surfaces with non-zero probability. This mismatch opens a *ghost channel* for RL to exploit off-manifold artefacts, even though the underlying ground truth never leaves ℳvol\mathcal{M}^{\mathrm{vol}}.

### 3.1 Synthetic law-consistent generator

We consider a discrete time grid t=0,1,…,Tt=0,1,\dots,T and a rectangular grid of maturities and strikes

|  |  |  |
| --- | --- | --- |
|  | 𝒯={T1,…,TM},𝒦={K1,…,KK},\mathcal{T}=\{T\_{1},\dots,T\_{M}\},\qquad\mathcal{K}=\{K\_{1},\dots,K\_{K}\}, |  |

with T1≈1​MT\_{1}\approx 1\text{M} and TM≈2​YT\_{M}\approx 2\text{Y}, and K1≈0.5​StK\_{1}\approx 0.5S\_{t}, KK≈1.5​StK\_{K}\approx 1.5S\_{t} at each time tt, chosen to roughly mirror SPX/VIX market conventions.111The exact grid is not essential; any finite grid of maturities and moneyness levels can be handled by the law manifold construction in Sec. [2](https://arxiv.org/html/2511.17304v1#S2 "2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). We denote by

|  |  |  |
| --- | --- | --- |
|  | σt=σt​(Ti,Kj)∈ℝM×K,wt=σt2⊙T∈ℝM×K\sigma\_{t}=\sigma\_{t}(T\_{i},K\_{j})\in\mathbb{R}^{M\times K},\qquad w\_{t}=\sigma\_{t}^{2}\odot T\in\mathbb{R}^{M\times K} |  |

the implied-volatility and total-variance surfaces at time tt, where TT is broadcast across strikes. In vectorized form we identify wtw\_{t} with an element of ℝd\mathbb{R}^{d} with d=M​Kd=MK, and we write wt∈ℳvolw\_{t}\in\mathcal{M}^{\mathrm{vol}} when all static no-arbitrage constraints (butterfly, calendar) are satisfied on the discrete grid (Sec. [2](https://arxiv.org/html/2511.17304v1#S2 "2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

##### Law-consistent ground truth.

The *ground-truth world* is specified by a Markovian generator

|  |  |  |
| --- | --- | --- |
|  | G⋆:𝒮→𝒮×ℳvol,(st+1,wt+1)=G⋆​(st),G^{\star}:\mathcal{S}\to\mathcal{S}\times\mathcal{M}^{\mathrm{vol}},\qquad(s\_{t+1},w\_{t+1})=G^{\star}(s\_{t}), |  |

where sts\_{t} is a latent state that may contain the underlying spot StS\_{t}, latent volatility factors, and other macro state variables. In practice we instantiate G⋆G^{\star} as a multi-factor stochastic-volatility model with jumps and rough components,222E.g., a Heston-like model with stochastic variance and stochastic volatility-of-volatility, optionally enriched with rough volatility factors as in [[9](https://arxiv.org/html/2511.17304v1#bib.bib9)], coupled to an SVI-type implied-vol parametrization [[8](https://arxiv.org/html/2511.17304v1#bib.bib8)]. whose parameters are randomized across trajectories to induce a diverse ensemble of surfaces reminiscent of SPX/VIX dynamics [e.g. [2](https://arxiv.org/html/2511.17304v1#bib.bib2), [6](https://arxiv.org/html/2511.17304v1#bib.bib6), [11](https://arxiv.org/html/2511.17304v1#bib.bib11)].

At each time step, raw model-implied option prices are numerically projected onto the static no-arbitrage polyhedron ℳvol\mathcal{M}^{\mathrm{vol}} using the construction of Sec. [2](https://arxiv.org/html/2511.17304v1#S2 "2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), and implied volatilities are recovered from these arbitrage-free prices. As a result, the data-generating distribution ℙ⋆\mathbb{P}^{\star} over trajectories (wt)t=0T(w\_{t})\_{t=0}^{T} is *law-consistent by design*.

###### Definition 6 (Law-consistent synthetic generator).

A stochastic process (wt)t=0T(w\_{t})\_{t=0}^{T} taking values in ℝd\mathbb{R}^{d} is said to be *law-consistent* with respect to a law manifold ℳ⊂ℝd\mathcal{M}\subset\mathbb{R}^{d} if

|  |  |  |
| --- | --- | --- |
|  | ℙ(wt∈ℳ for all t=0,…,T)=1.\mathbb{P}\big(w\_{t}\in\mathcal{M}\text{ for all }t=0,\dots,T\big)=1. |  |

We call G⋆G^{\star} a *law-consistent generator* if the trajectory (wt)(w\_{t}) it induces satisfies this condition for ℳ=ℳvol\mathcal{M}=\mathcal{M}^{\mathrm{vol}}.

###### Proposition 5 (Support of the synthetic generator).

Let (wt)t=0T(w\_{t})\_{t=0}^{T} be generated by G⋆G^{\star} as above, with static no-arbitrage imposed at each time via projection onto ℳvol\mathcal{M}^{\mathrm{vol}}. Then

|  |  |  |
| --- | --- | --- |
|  | supp​ℙ⋆⊆(ℳvol)T+1,\mathrm{supp}\,\mathbb{P}^{\star}\subseteq\big(\mathcal{M}^{\mathrm{vol}}\big)^{T+1}, |  |

i.e., ℙ⋆\mathbb{P}^{\star} is supported on the product of the volatility law manifold at all times.

###### Proof sketch.

By construction, every step of G⋆G^{\star} maps into ℳvol\mathcal{M}^{\mathrm{vol}}: the raw option prices are obtained from a stochastic-volatility model, and then the resulting surface is projected onto ℳvol\mathcal{M}^{\mathrm{vol}} as in Sec. [2](https://arxiv.org/html/2511.17304v1#S2 "2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). Thus wt∈ℳvolw\_{t}\in\mathcal{M}^{\mathrm{vol}} almost surely for all tt. The support statement follows from the definition of product measures. A detailed measure-theoretic proof is given in Appendix B.1.
∎

Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") highlights the asymmetry that drives our ghost-arbitrage story: the *true* dynamics never leave the law manifold, whereas the learned world model in the next subsection is not constrained in this way.

##### Transferability beyond volatility.

The same construction immediately extends to other axiom-constrained financial objects such as yield curves and credit curves: there, yty\_{t} is a discretized term structure, ℳ\mathcal{M} encodes monotonicity and convexity constraints [e.g. [19](https://arxiv.org/html/2511.17304v1#bib.bib19), [20](https://arxiv.org/html/2511.17304v1#bib.bib20)], and G⋆G^{\star} is any arbitrage-free term-structure model. Our volatility case thus serves as a concrete, high-dimensional instance of a more general Scientific AI template.

### 3.2 Neural world model and approximation gap

RL agents do not interact with G⋆G^{\star} directly. Instead, in the spirit of model-based RL and world models [[40](https://arxiv.org/html/2511.17304v1#bib.bib40), HafnerEtAl2019PlaNet, HafnerEtAl2020Dreamer, [45](https://arxiv.org/html/2511.17304v1#bib.bib45)], they are trained entirely on rollouts generated by a learned dynamics model (the *world model*) fitted to trajectories from G⋆G^{\star}.

##### Architecture and training.

Let LL be the length of the look-back window. At each time tt, we define the input

|  |  |  |
| --- | --- | --- |
|  | xt:=(wt−L+1,…,wt)∈(ℝd)L,x\_{t}:=\big(w\_{t-L+1},\dots,w\_{t}\big)\in\big(\mathbb{R}^{d}\big)^{L}, |  |

and we train a recurrent neural network with parameters θ\theta,

|  |  |  |
| --- | --- | --- |
|  | fθ:(ℝd)L→ℝd,w^t+1=fθ​(xt),f\_{\theta}:\big(\mathbb{R}^{d}\big)^{L}\to\mathbb{R}^{d},\qquad\hat{w}\_{t+1}=f\_{\theta}(x\_{t}), |  |

to minimize the mean-squared prediction error

|  |  |  |
| --- | --- | --- |
|  | ℛ​(θ):=𝔼ℙ⋆​[‖fθ​(xt)−wt+1‖22]≈1N​∑n=1N‖fθ​(xt(n))−wt+1(n)‖22\mathcal{R}(\theta):=\mathbb{E}\_{\mathbb{P}^{\star}}\big[\|f\_{\theta}(x\_{t})-w\_{t+1}\|\_{2}^{2}\big]\approx\frac{1}{N}\sum\_{n=1}^{N}\|f\_{\theta}(x\_{t}^{(n)})-w\_{t+1}^{(n)}\|\_{2}^{2} |  |

over a dataset of NN trajectories sampled from G⋆G^{\star}. In practice, fθf\_{\theta} is implemented as a GRU/LSTM encoder over (wt−L+1,…,wt)(w\_{t-L+1},\dots,w\_{t}) followed by a fully connected decoder to the next total-variance surface, as commonly used in spatio-temporal forecasting [e.g. [72](https://arxiv.org/html/2511.17304v1#bib.bib72), [73](https://arxiv.org/html/2511.17304v1#bib.bib73)].

Crucially, *no law penalties are used when training the world model*: the loss is purely predictive. Thus, even though all training targets wt+1w\_{t+1} lie in ℳvol\mathcal{M}^{\mathrm{vol}}, the predictions w^t+1\hat{w}\_{t+1} are unconstrained and may lie outside the manifold.

###### Definition 7 (Approximation residual and ghost channel).

Let θ⋆\theta^{\star} be any (local) minimizer of ℛ​(θ)\mathcal{R}(\theta), and write

|  |  |  |
| --- | --- | --- |
|  | w^t+1=fθ⋆​(xt),et+1:=w^t+1−wt+1\hat{w}\_{t+1}=f\_{\theta^{\star}}(x\_{t}),\qquad e\_{t+1}:=\hat{w}\_{t+1}-w\_{t+1} |  |

for the corresponding prediction and residual. We define the *approximation gap* as

|  |  |  |
| --- | --- | --- |
|  | ε2:=𝔼ℙ⋆​[‖et+1‖22]=ℛ​(θ⋆),\varepsilon^{2}:=\mathbb{E}\_{\mathbb{P}^{\star}}\big[\|e\_{t+1}\|\_{2}^{2}\big]=\mathcal{R}(\theta^{\star}), |  |

and the *ghost channel* as the random variable

|  |  |  |
| --- | --- | --- |
|  | rt+1⟂:=r​(w^t+1,at)−r​(wt+1ℳ,at),r^{\perp}\_{t+1}:=r(\hat{w}\_{t+1},a\_{t})-r(w^{\mathcal{M}}\_{t+1},a\_{t}), |  |

where rr is the one-step P&L functional, ata\_{t} is the agent’s action, and wt+1ℳ:=Πℳvol​(w^t+1)w^{\mathcal{M}}\_{t+1}:=\Pi\_{\mathcal{M}^{\mathrm{vol}}}(\hat{w}\_{t+1}) is the metric projection of the prediction onto the law manifold (Def. [2](https://arxiv.org/html/2511.17304v1#Thmdefinition2 "Definition 2 (Law-penalty functional). ‣ Law-penalty functional. ‣ 2.0 Finite-Dimensional Convex Template and Notation ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

Here, rt+1⟂r^{\perp}\_{t+1} is precisely the off-manifold component in the Goodhart decomposition (Sec. LABEL:subsec:goodhart-conceptual); it captures how much extra P&L the agent obtains by exploiting law-violating predictions rather than their arbitrage-free projection.

###### Proposition 6 (Approximation gap induces a ghost channel).

Suppose the following conditions hold:

1. (i)

   The approximation gap is non-zero: ε2=𝔼​[‖et+1‖22]>0\varepsilon^{2}=\mathbb{E}[\|e\_{t+1}\|\_{2}^{2}]>0.
2. (ii)

   The reward is locally differentiable in ww with gradient gt+1:=∇wr​(wt+1,at)g\_{t+1}:=\nabla\_{w}r(w\_{t+1},a\_{t}).
3. (iii)

   The residual et+1e\_{t+1} has a component in the normal cone of ℳvol\mathcal{M}^{\mathrm{vol}} at wt+1w\_{t+1} with non-zero covariance:

   |  |  |  |
   | --- | --- | --- |
   |  | Cov​(PNℳ​(wt+1)​et+1,gt+1)≠0,\mathrm{Cov}\big(P\_{N\_{\mathcal{M}}(w\_{t+1})}e\_{t+1},\,g\_{t+1}\big)\neq 0, |  |

   where PNℳ​(wt+1)P\_{N\_{\mathcal{M}}(w\_{t+1})} denotes orthogonal projection onto the normal cone Nℳ​(wt+1)N\_{\mathcal{M}}(w\_{t+1}).

Then, for sufficiently small residuals (in the sense of a local linearization),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[rt+1⟂]≈𝔼​[gt+1⊤​PNℳ​(wt+1)​et+1]≠0,\mathbb{E}\big[r^{\perp}\_{t+1}\big]\approx\mathbb{E}\big[g\_{t+1}^{\top}P\_{N\_{\mathcal{M}}(w\_{t+1})}e\_{t+1}\big]\neq 0, |  |

so the world model induces a non-trivial ghost channel. In particular, if gt+1g\_{t+1} is positively correlated with PNℳ​(wt+1)​et+1P\_{N\_{\mathcal{M}}(w\_{t+1})}e\_{t+1}, then 𝔼​[rt+1⟂]>0\mathbb{E}[r^{\perp}\_{t+1}]>0 and there exist states where moving off-manifold strictly improves expected P&L.

###### Proof sketch.

By the law-consistency of G⋆G^{\star}, we have wt+1∈ℳvolw\_{t+1}\in\mathcal{M}^{\mathrm{vol}} almost surely. For small residuals, a first-order Taylor approximation yields

|  |  |  |
| --- | --- | --- |
|  | r​(w^t+1,at)≈r​(wt+1,at)+gt+1⊤​et+1.r(\hat{w}\_{t+1},a\_{t})\approx r(w\_{t+1},a\_{t})+g\_{t+1}^{\top}e\_{t+1}. |  |

Meanwhile, the projection wt+1ℳ=Πℳ​(w^t+1)w^{\mathcal{M}}\_{t+1}=\Pi\_{\mathcal{M}}(\hat{w}\_{t+1}) removes the component of et+1e\_{t+1} that lies in the normal cone Nℳ​(wt+1)N\_{\mathcal{M}}(w\_{t+1}) (by optimality conditions for convex projections), so to first order we have

|  |  |  |
| --- | --- | --- |
|  | r​(wt+1ℳ,at)≈r​(wt+1,at)+gt+1⊤​PTℳ​(wt+1)​et+1,r(w^{\mathcal{M}}\_{t+1},a\_{t})\approx r(w\_{t+1},a\_{t})+g\_{t+1}^{\top}P\_{T\_{\mathcal{M}}(w\_{t+1})}e\_{t+1}, |  |

where Tℳ​(wt+1)T\_{\mathcal{M}}(w\_{t+1}) is the tangent cone and PTℳP\_{T\_{\mathcal{M}}} the corresponding projector. Their difference is

|  |  |  |
| --- | --- | --- |
|  | rt+1⟂≈gt+1⊤​(I−PTℳ​(wt+1))​et+1=gt+1⊤​PNℳ​(wt+1)​et+1.r^{\perp}\_{t+1}\approx g\_{t+1}^{\top}\big(I-P\_{T\_{\mathcal{M}}(w\_{t+1})}\big)e\_{t+1}=g\_{t+1}^{\top}P\_{N\_{\mathcal{M}}(w\_{t+1})}e\_{t+1}. |  |

Taking expectations under ℙ⋆\mathbb{P}^{\star} and using assumption (iii) yields the claim. Rigorous error bounds for the linearization and a detailed cone-decomposition argument are provided in Appendix B.2.
∎

Proposition [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") formalizes the intuitive statement that *any* non-zero approximation gap with a component normal to the law manifold, combined with a reward that is monotone in that direction, will generically open a ghost channel. In Sec. [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") we show empirically that RL agents indeed learn to exploit this channel.

### 3.3 Instantiating the Goodhart decomposition for volatility

We now instantiate the conceptual Goodhart decomposition of Sec. LABEL:subsec:goodhart-conceptual in the concrete volatility setting. For each predicted surface w^t+1=fθ⋆​(xt)\hat{w}\_{t+1}=f\_{\theta^{\star}}(x\_{t}), we compute:

1. 1.

   The metric projection onto the volatility law manifold:

   |  |  |  |
   | --- | --- | --- |
   |  | wt+1ℳ:=Πℳvol​(w^t+1)=arg⁡minw′∈ℳvol⁡ϕ​(w^t+1−w′),w^{\mathcal{M}}\_{t+1}:=\Pi\_{\mathcal{M}^{\mathrm{vol}}}(\hat{w}\_{t+1})=\arg\min\_{w^{\prime}\in\mathcal{M}^{\mathrm{vol}}}\phi\big(\hat{w}\_{t+1}-w^{\prime}\big), |  |

   where ϕ\phi is the squared ℓ2\ell\_{2} norm in total-variance space, consistent with the law-penalty functional ℒϕ\mathcal{L}\_{\phi} of Sec. LABEL:sec:law-penalty.
2. 2.

   The on-manifold reward component

   |  |  |  |
   | --- | --- | --- |
   |  | rt+1ℳ:=r​(wt+1ℳ,at),r^{\mathcal{M}}\_{t+1}:=r\big(w^{\mathcal{M}}\_{t+1},a\_{t}\big), |  |

   obtained by evaluating the P&L functional under the projected surface.
3. 3.

   The ghost-arbitrage component

   |  |  |  |
   | --- | --- | --- |
   |  | rt+1⟂:=r​(w^t+1,at)−rt+1ℳ.r^{\perp}\_{t+1}:=r\big(\hat{w}\_{t+1},a\_{t}\big)-r^{\mathcal{M}}\_{t+1}. |  |

By construction we have the exact decomposition

|  |  |  |
| --- | --- | --- |
|  | r​(w^t+1,at)=rt+1ℳ+rt+1⟂,r\big(\hat{w}\_{t+1},a\_{t}\big)=r^{\mathcal{M}}\_{t+1}+r^{\perp}\_{t+1}, |  |

where rt+1ℳr^{\mathcal{M}}\_{t+1} is the reward that would be obtained if the world model were first projected back to the law manifold, and rt+1⟂r^{\perp}\_{t+1} captures the incremental reward purely due to law-violating predictions. Note that, because the ground truth never leaves ℳvol\mathcal{M}^{\mathrm{vol}} (Prop. [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), any systematic pattern in rt+1⟂r^{\perp}\_{t+1} is necessarily a *model-induced artefact*.

###### Remark 2 (Consistency of projection operator).

For consistency with Sec. LABEL:sec:law-penalty, we use the same projection operator Πℳvol\Pi\_{\mathcal{M}^{\mathrm{vol}}} both in defining the law penalty ℒϕ\mathcal{L}\_{\phi} and in the Goodhart decomposition. Algorithmically, Πℳvol\Pi\_{\mathcal{M}^{\mathrm{vol}}} is implemented via a convex quadratic program that enforces butterfly and calendar inequalities on the total-variance grid, closely related to static-arbitrage projection procedures in the option-pricing literature [[12](https://arxiv.org/html/2511.17304v1#bib.bib12), [13](https://arxiv.org/html/2511.17304v1#bib.bib13), [11](https://arxiv.org/html/2511.17304v1#bib.bib11)]. This ensures that any off-manifold advantage measured by r⟂r^{\perp} is directly comparable to the law-penalty metrics reported later.

### 3.4 World-model diagnostics and dynamics plots

Before training any RL agents, we empirically characterize the behavior of the neural world model and its law violations. Two diagnostics play a central role:

##### Prediction accuracy.

We track both the training and validation mean-squared error

|  |  |  |
| --- | --- | --- |
|  | MSEtrain​(t):=1Ntrain​∑n‖fθ⋆​(xt(n))−wt+1(n)‖22,\mathrm{MSE}\_{\mathrm{train}}(t):=\frac{1}{N\_{\mathrm{train}}}\sum\_{n}\|f\_{\theta^{\star}}(x\_{t}^{(n)})-w\_{t+1}^{(n)}\|\_{2}^{2}, |  |

and likewise for MSEval​(t)\mathrm{MSE}\_{\mathrm{val}}(t). Typical dynamics plots (family “Dynamics Plots”, see Sec. [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) show fast initial reduction in MSE followed by a plateau, as in standard world-model training [[40](https://arxiv.org/html/2511.17304v1#bib.bib40), HafnerEtAl2020Dreamer]. This confirms that fθ⋆f\_{\theta^{\star}} has learned a non-trivial approximation of the dynamics.

##### Law penalties of predictions vs. ground truth.

More importantly for our purposes, we compare the law penalties

|  |  |  |
| --- | --- | --- |
|  | ℒϕ​(wt+1)≡0,ℒϕ​(w^t+1)=ϕ​(w^t+1−Πℳvol​(w^t+1))\mathcal{L}\_{\phi}(w\_{t+1})\equiv 0,\qquad\mathcal{L}\_{\phi}(\hat{w}\_{t+1})=\phi\big(\hat{w}\_{t+1}-\Pi\_{\mathcal{M}^{\mathrm{vol}}}(\hat{w}\_{t+1})\big) |  |

over time. By Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), the ground-truth trajectories satisfy ℒϕ​(wt+1)=0\mathcal{L}\_{\phi}(w\_{t+1})=0 up to numerical tolerance, whereas the predictions exhibit a strictly positive distribution of law penalties.

###### Lemma 2 (Non-trivial off-manifold mass of the world model).

Assume that fθ⋆f\_{\theta^{\star}} is not exactly equal to the Bayes-optimal regressor fBayes​(xt):=𝔼​[wt+1|xt]f^{\mathrm{Bayes}}(x\_{t}):=\mathbb{E}[w\_{t+1}\,|\,x\_{t}] and that the law manifold ℳvol\mathcal{M}^{\mathrm{vol}} has non-empty interior within the support of wt+1w\_{t+1}. Then there exists δ>0\delta>0 such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℒϕ​(w^t+1)>δ)>0,\mathbb{P}\big(\mathcal{L}\_{\phi}(\hat{w}\_{t+1})>\delta\big)>0, |  |

i.e., the world model assigns non-zero probability mass to surfaces at a positive distance from ℳvol\mathcal{M}^{\mathrm{vol}}.

###### Proof sketch.

If fθ⋆≡fBayesf\_{\theta^{\star}}\equiv f^{\mathrm{Bayes}} and the conditional distribution of wt+1w\_{t+1} given xtx\_{t} were a Dirac mass on ℳvol\mathcal{M}^{\mathrm{vol}}, then w^t+1\hat{w}\_{t+1} would almost surely lie in ℳvol\mathcal{M}^{\mathrm{vol}} and the law penalty would vanish. In our finite-data, finite-capacity setting, both approximation error (difference between fθ⋆f\_{\theta^{\star}} and fBayesf^{\mathrm{Bayes}}) and intrinsic conditional variance generically ensure that w^t+1\hat{w}\_{t+1} has a non-degenerate distribution around wt+1w\_{t+1}, which in turn implies a positive-distance shell around ℳvol\mathcal{M}^{\mathrm{vol}} is hit with non-zero probability. A rigorous argument using continuity of ℒϕ\mathcal{L}\_{\phi} and support properties of fθ⋆​(xt)f\_{\theta^{\star}}(x\_{t}) is given in Appendix B.3.
∎

In our experiments, dynamics plots of ℒϕ​(w^t+1)\mathcal{L}\_{\phi}(\hat{w}\_{t+1}) show a stationary distribution with mean on the order of 10−310^{-3}–10−210^{-2}, while ℒϕ​(wt+1)\mathcal{L}\_{\phi}(w\_{t+1}) remains at numerical zero. Combined with Proposition [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and Lemma [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), this empirically confirms that the Neural world model is both (i) sufficiently accurate to serve as a plausible environment for RL, and (ii) sufficiently misaligned with the axioms to open a statistically significant ghost channel. The remainder of the paper investigates how different RL variants and structural baselines interact with this channel.

## 4 RL on Volatility World Models: Incentives and Law-Strength

In this section, we formalize the Markov decision process (MDP) induced by the volatility world model of Section [3](https://arxiv.org/html/2511.17304v1#S3 "3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), instantiate several RL variants as *stress-tests* of the axiomatic pipeline, and develop our flagship incentive and trade-off results. Throughout, we treat RL as a tool for probing how generic policy-gradient methods interact with the law manifold ℳvol\mathcal{M}^{\mathrm{vol}}, the ghost channel r⟂r^{\perp}, and the law-penalty functional ℒϕ\mathcal{L}\_{\phi}, rather than as an attempt to build a production trading system.

### 4.1 MDP formulation on the world model

Let 𝒲⊂ℝdw\mathcal{W}\subset\mathbb{R}^{d\_{w}} denote the discretized total-variance grid (Section LABEL:sec:axiomatic\_manifold), and let 𝒳\mathcal{X} collect auxiliary market covariates (e.g., spot price, realized variance estimates). We define the state space as

|  |  |  |
| --- | --- | --- |
|  | 𝒮:=𝒲K×𝒳,\mathcal{S}\;:=\;\mathcal{W}^{K}\times\mathcal{X}, |  |

where a state st=(wt−K+1:t,xt)s\_{t}=(w\_{t-K+1:t},x\_{t}) concatenates a history window of KK total-variance surfaces and covariates.333In our experiments we take KK in the range 88–1616, similar to recurrent world-model setups in model-based RL [[40](https://arxiv.org/html/2511.17304v1#bib.bib40), HafnerPlaNet2019, HafnerDreamer2020].

The action at∈𝒜a\_{t}\in\mathcal{A} represents a hedge/portfolio vector (e.g., positions in underlying and options), following the deep-hedging literature [[69](https://arxiv.org/html/2511.17304v1#bib.bib69)]. The action space 𝒜\mathcal{A} is a compact subset of ℝda\mathbb{R}^{d\_{a}} defined by position and capital constraints.

##### World-model transition.

Given sts\_{t} and ata\_{t}, the next volatility surface wt+1w\_{t+1} is sampled from the world model

|  |  |  |
| --- | --- | --- |
|  | wt+1∼P^θ(⋅∣wt−K+1:t,xt,at),w\_{t+1}\sim\hat{P}\_{\theta}(\cdot\mid w\_{t-K+1:t},x\_{t},a\_{t}), |  |

where P^θ\hat{P}\_{\theta} is the GRU/LSTM-based predictor of Section [3](https://arxiv.org/html/2511.17304v1#S3 "3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). We then update covariates xt+1x\_{t+1} via a deterministic or stochastic rule xt+1=f​(xt,wt+1,at,εt+1)x\_{t+1}=f(x\_{t},w\_{t+1},a\_{t},\varepsilon\_{t+1}), giving the transition kernel

|  |  |  |
| --- | --- | --- |
|  | Pθ​(st+1∣st,at)=P^θ​(wt+1∣wt−K+1:t,xt,at)​δf​(xt,wt+1,at,εt+1)​(xt+1).P\_{\theta}(s\_{t+1}\mid s\_{t},a\_{t})\;=\;\hat{P}\_{\theta}(w\_{t+1}\mid w\_{t-K+1:t},x\_{t},a\_{t})\,\delta\_{f(x\_{t},w\_{t+1},a\_{t},\varepsilon\_{t+1})}(x\_{t+1}). |  |

##### Reward decomposition.

The per-step reward is the PnL plus (optionally) a law penalty:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rλ​(st,at,st+1):=PnL​(st,at,st+1)⏟economic payoff−λ​ℒϕ​(wt+1)⏟law penalty,r\_{\lambda}(s\_{t},a\_{t},s\_{t+1})\;:=\;\underbrace{\mathrm{PnL}(s\_{t},a\_{t},s\_{t+1})}\_{\text{economic payoff}}\;-\;\lambda\,\underbrace{\mathcal{L}\_{\phi}\!\bigl(w\_{t+1}\bigr)}\_{\text{law penalty}}, |  | (6) |

where λ≥0\lambda\geq 0 is the law-penalty weight. For λ=0\lambda=0 we recover the naive PnL-driven RL setting. Using the projection operator Πℳ\Pi\_{\mathcal{M}} from Definition LABEL:def:projection\_law\_manifold, we further decompose

|  |  |  |  |
| --- | --- | --- | --- |
|  | rλ=rℳ−λ​ℒϕ+r⟂,rℳ​(st,at,st+1):=PnL​(Πℳ​(wt+1),at),r⟂:=PnL​(wt+1,at)−rℳ,r\_{\lambda}=r^{\mathcal{M}}-\lambda\mathcal{L}\_{\phi}+r^{\perp},\qquad r^{\mathcal{M}}(s\_{t},a\_{t},s\_{t+1}):=\mathrm{PnL}\bigl(\Pi\_{\mathcal{M}}(w\_{t+1}),a\_{t}\bigr),\quad r^{\perp}:=\mathrm{PnL}(w\_{t+1},a\_{t})-r^{\mathcal{M}}, |  | (7) |

in direct correspondence with the Goodhart decomposition of Section LABEL:subsec:goodhart\_generic. The term r⟂r^{\perp} is the *ghost-arbitrage component* induced by world-model prediction error.

##### Objective and policy class.

We consider stationary stochastic policies πθ​(a∣s)\pi\_{\theta}(a\mid s) parameterized by neural networks, as in actor–critic and PPO-style methods [[49](https://arxiv.org/html/2511.17304v1#bib.bib49), [50](https://arxiv.org/html/2511.17304v1#bib.bib50), [53](https://arxiv.org/html/2511.17304v1#bib.bib53)]. For a given λ\lambda, the discounted infinite-horizon objective is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jλ​(π):=𝔼π​[∑t=0∞γt​rλ​(st,at,st+1)]=Jℳ​(π)−λ​Jlaw​(π)+J⟂​(π),J\_{\lambda}(\pi)\;:=\;\mathbb{E}\_{\pi}\!\left[\sum\_{t=0}^{\infty}\gamma^{t}r\_{\lambda}(s\_{t},a\_{t},s\_{t+1})\right]\;=\;J^{\mathcal{M}}(\pi)-\lambda\,J^{\mathrm{law}}(\pi)+J^{\perp}(\pi), |  | (8) |

where

|  |  |  |
| --- | --- | --- |
|  | Jℳ​(π):=𝔼π​[∑tγt​rtℳ],Jlaw​(π):=𝔼π​[∑tγt​ℒϕ​(wt)],J⟂​(π):=𝔼π​[∑tγt​rt⟂].J^{\mathcal{M}}(\pi):=\mathbb{E}\_{\pi}\!\Big[\sum\_{t}\gamma^{t}r^{\mathcal{M}}\_{t}\Big],\qquad J^{\mathrm{law}}(\pi):=\mathbb{E}\_{\pi}\!\Big[\sum\_{t}\gamma^{t}\mathcal{L}\_{\phi}(w\_{t})\Big],\qquad J^{\perp}(\pi):=\mathbb{E}\_{\pi}\!\Big[\sum\_{t}\gamma^{t}r^{\perp}\_{t}\Big]. |  |

In practice, our experiments use finite-horizon episodes (T≈64T\approx 64) and average per-step PnL and law penalties; the theoretical development is presented in the discounted limit for notational clarity.

##### Algorithmic choice.

We instantiate PPO-style actor–critic [[53](https://arxiv.org/html/2511.17304v1#bib.bib53)] with a clipped surrogate objective and generalized advantage estimation [[52](https://arxiv.org/html/2511.17304v1#bib.bib52)], which is standard for continuous-control RL and has seen use in financial RL and hedging [[67](https://arxiv.org/html/2511.17304v1#bib.bib67), [69](https://arxiv.org/html/2511.17304v1#bib.bib69)]. Crucially, PPO is only one representative of the broad class of policy-gradient RL algorithms; our incentive results hold for any method whose updates approximate the policy gradient of JλJ\_{\lambda} [[49](https://arxiv.org/html/2511.17304v1#bib.bib49), [51](https://arxiv.org/html/2511.17304v1#bib.bib51)].

### 4.2 Naive RL and ghost-arbitrage incentive

We first analyze the case λ=0\lambda=0, where the agent optimizes pure PnL on the world model. By the decomposition ([7](https://arxiv.org/html/2511.17304v1#S4.E7 "In Reward decomposition. ‣ 4.1 MDP formulation on the world model ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | J0​(π)=Jℳ​(π)+J⟂​(π).J\_{0}(\pi)=J^{\mathcal{M}}(\pi)+J^{\perp}(\pi). |  | (9) |

Let 𝒮\mathcal{S} denote a *structural baseline class* of low-capacity, law-consistent strategies (Section [5](https://arxiv.org/html/2511.17304v1#S5 "5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), such as zero-hedge and vol-trend heuristics, satisfying

|  |  |  |
| --- | --- | --- |
|  | Jlaw​(πS)≈0,πS∈𝒮.J^{\mathrm{law}}(\pi^{S})\approx 0,\qquad\pi^{S}\in\mathcal{S}. |  |

We assume 𝒮\mathcal{S} approximates the best *on-manifold* hedge:

###### Assumption 1 (On-manifold near-optimality of structural class).

There exists π𝒮⋆∈𝒮\pi^{\star}\_{\mathcal{S}}\in\mathcal{S} and ε𝒮≥0\varepsilon\_{\mathcal{S}}\geq 0 such that

|  |  |  |
| --- | --- | --- |
|  | Jℳ​(π)≤Jℳ​(π𝒮⋆)+ε𝒮for all ​π∈Π,J^{\mathcal{M}}(\pi)\;\leq\;J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}}\qquad\text{for all }\pi\in\Pi, |  |

where Π\Pi is the RL policy class.

Assumption [1](https://arxiv.org/html/2511.17304v1#Thmassumption1 "Assumption 1 (On-manifold near-optimality of structural class). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") is a *design choice*: we deliberately choose baselines that are simple but well-aligned with the axioms, in the spirit of deep-hedging strategies optimized directly on market dynamics [[69](https://arxiv.org/html/2511.17304v1#bib.bib69), [71](https://arxiv.org/html/2511.17304v1#bib.bib71)]. Under this assumption, the only systematic way for π∈Π\pi\in\Pi to outperform π𝒮⋆\pi^{\star}\_{\mathcal{S}} on the world model is through the ghost component J⟂​(π)J^{\perp}(\pi).

###### Theorem 1 (Ghost-arbitrage incentive for naive RL).

Suppose Assumption [1](https://arxiv.org/html/2511.17304v1#Thmassumption1 "Assumption 1 (On-manifold near-optimality of structural class). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") holds, and let

|  |  |  |
| --- | --- | --- |
|  | π0⋆∈arg⁡maxπ∈Π⁡J0​(π)\pi^{\star}\_{0}\in\arg\max\_{\pi\in\Pi}J\_{0}(\pi) |  |

be a global maximizer of J0J\_{0} over Π\Pi. Then:

1. 1.

   If supπ∈ΠJ0​(π)>Jℳ​(π𝒮⋆)+ε𝒮\sup\_{\pi\in\Pi}J\_{0}(\pi)>J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}}, any maximizer π0⋆\pi^{\star}\_{0} satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | J⟂​(π0⋆)≥supπ∈ΠJ0​(π)−Jℳ​(π𝒮⋆)−ε𝒮> 0.J^{\perp}(\pi^{\star}\_{0})\;\geq\;\sup\_{\pi\in\Pi}J\_{0}(\pi)-J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})-\varepsilon\_{\mathcal{S}}\;>\;0. |  | (10) |

   In particular, the excess value over the structural baseline is entirely attributable to ghost arbitrage.
2. 2.

   If, in addition, JℳJ^{\mathcal{M}} has a local maximum at some π¯∈Π\bar{\pi}\in\Pi with Jℳ​(π¯)≈Jℳ​(π𝒮⋆)J^{\mathcal{M}}(\bar{\pi})\approx J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}}), and the policy-gradient theorem holds [[49](https://arxiv.org/html/2511.17304v1#bib.bib49)], then the policy gradient near π¯\bar{\pi} satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇θJ0​(πθ)|θ=θ¯≈∇θJ⟂​(πθ)|θ=θ¯,\nabla\_{\theta}J\_{0}(\pi\_{\theta})\Big|\_{\theta=\bar{\theta}}\;\approx\;\nabla\_{\theta}J^{\perp}(\pi\_{\theta})\Big|\_{\theta=\bar{\theta}}, |  | (11) |

   so gradient-based RL updates are locally driven by increasing J⟂J^{\perp}.

##### Proof sketch.

Part (i) follows directly from the decomposition ([9](https://arxiv.org/html/2511.17304v1#S4.E9 "In 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")):

|  |  |  |
| --- | --- | --- |
|  | J0​(π)=Jℳ​(π)+J⟂​(π)≤Jℳ​(π𝒮⋆)+ε𝒮+J⟂​(π),J\_{0}(\pi)=J^{\mathcal{M}}(\pi)+J^{\perp}(\pi)\;\leq\;J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}}+J^{\perp}(\pi), |  |

so any π\pi achieving value strictly above Jℳ​(π𝒮⋆)+ε𝒮J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}} must have J⟂​(π)>0J^{\perp}(\pi)>0. Applying this to π0⋆\pi^{\star}\_{0} yields ([10](https://arxiv.org/html/2511.17304v1#S4.E10 "In item 1 ‣ Theorem 1 (Ghost-arbitrage incentive for naive RL). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). For (ii), the policy-gradient theorem expresses ∇θJ0​(πθ)\nabla\_{\theta}J\_{0}(\pi\_{\theta}) as an expectation over on-policy trajectories weighted by the advantage function [[49](https://arxiv.org/html/2511.17304v1#bib.bib49), [51](https://arxiv.org/html/2511.17304v1#bib.bib51)]. Near a local maximum of JℳJ^{\mathcal{M}}, the contribution of ∇θJℳ\nabla\_{\theta}J^{\mathcal{M}} is negligible, so ∇θJ0≈∇θJ⟂\nabla\_{\theta}J\_{0}\approx\nabla\_{\theta}J^{\perp}, yielding ([11](https://arxiv.org/html/2511.17304v1#S4.E11 "In item 2 ‣ Theorem 1 (Ghost-arbitrage incentive for naive RL). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). A fully rigorous treatment, including conditions on function approximation and local optimality, is provided in Appendix C.1. ∎

#### 4.2.1 Economic interpretation

Theorem [1](https://arxiv.org/html/2511.17304v1#Thmtheorem1 "Theorem 1 (Ghost-arbitrage incentive for naive RL). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") formalizes a simple but crucial economic intuition:

1. 1.

   Structural baselines 𝒮\mathcal{S}, such as zero-hedge and vol-trend strategies, are built to respect the axioms and approximate on-manifold optimal hedging. They *do not attempt* to exploit model misspecification.
2. 2.

   Once 𝒮\mathcal{S} has exhausted most of the on-manifold value JℳJ^{\mathcal{M}}, any additional performance that naive RL achieves on the *learned world model* must come from J⟂J^{\perp}, i.e., ghost arbitrage driven by prediction artifacts, not genuine admissible edge.
3. 3.

   Gradient-based RL is locally steered by ∇θJ⟂\nabla\_{\theta}J^{\perp}, so it is *structurally incentivized* to move into regions of the state–action space where the world model violates axioms in a “profitable” way.

This explains the empirical pattern in Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"): naive PPO achieves high PnL in-sample on the world model but exhibits systematically higher law penalties and Graceful Failure Index (GFI) than structural baselines, both in baseline and shocked environments. Rather than discovering better law-consistent hedges, the agent learns to exploit the ghost channel opened by P^θ\hat{P}\_{\theta}.

### 4.3 Law-penalized and selection-only RL variants

To test whether explicit law penalties mitigate ghost arbitrage, we consider two standard ways of injecting constraints into RL [[55](https://arxiv.org/html/2511.17304v1#bib.bib55), [57](https://arxiv.org/html/2511.17304v1#bib.bib57), [62](https://arxiv.org/html/2511.17304v1#bib.bib62)].

##### Soft law-seeking RL (gradient shaping).

We define the *soft law-seeking* objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jλsoft​(π):=𝔼π​[∑t=0∞γt​(PnLt−λ​ℒϕ​(wt+1))]=J0​(π)−λ​Jlaw​(π),J\_{\lambda}^{\mathrm{soft}}(\pi)\;:=\;\mathbb{E}\_{\pi}\!\Bigg[\sum\_{t=0}^{\infty}\gamma^{t}\Big(\mathrm{PnL}\_{t}-\lambda\mathcal{L}\_{\phi}(w\_{t+1})\Big)\Bigg]\;=\;J\_{0}(\pi)-\lambda\,J^{\mathrm{law}}(\pi), |  | (12) |

with λ>0\lambda>0. PPO is trained directly on JλsoftJ\_{\lambda}^{\mathrm{soft}}, so the law penalty appears inside the gradient. This mirrors classical Lagrangian and regularized RL approaches for safety and risk constraints [[54](https://arxiv.org/html/2511.17304v1#bib.bib54), [55](https://arxiv.org/html/2511.17304v1#bib.bib55), [59](https://arxiv.org/html/2511.17304v1#bib.bib59), [56](https://arxiv.org/html/2511.17304v1#bib.bib56)].

##### Selection-only RL (post-hoc shaping).

In the *selection-only* variant, we train policies on pure PnL,

|  |  |  |
| --- | --- | --- |
|  | J0train​(π):=J0​(π),J\_{0}^{\mathrm{train}}(\pi):=J\_{0}(\pi), |  |

but use law metrics only for early stopping and model selection:

|  |  |  |
| --- | --- | --- |
|  | πsel⋆∈arg⁡maxπ∈𝒞⁡{J0​(π)​subject to​Jlaw​(π)≤τ},\pi^{\star}\_{\mathrm{sel}}\in\arg\max\_{\pi\in\mathcal{C}}\Big\{J\_{0}(\pi)\;\text{subject to}\;J^{\mathrm{law}}(\pi)\leq\tau\Big\}, |  |

where 𝒞\mathcal{C} is the candidate set of checkpointed policies along training and τ\tau is a user-chosen law budget. This is analogous to *post-hoc* constraint enforcement in distributional and risk-sensitive RL [[57](https://arxiv.org/html/2511.17304v1#bib.bib57), [61](https://arxiv.org/html/2511.17304v1#bib.bib61)].

##### Summary.

Soft law-seeking RL tests whether shaping the gradient with ℒϕ\mathcal{L}\_{\phi} can guide policy updates away from ghost arbitrage; selection-only RL tests whether post-hoc model selection, without modifying the training dynamics, is sufficient. As Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") will show, neither variant restores Pareto dominance over structural baselines.

### 4.4 Law-strength frontier and Graceful Failure Index

We now formalize the *law-strength frontier* and the *Graceful Failure Index* (GFI), which jointly organize profitability, law alignment, and robustness under shocks.

#### 4.4.1 Law-strength frontier

Let Λ⊂[0,∞)\Lambda\subset[0,\infty) be a finite set of penalty weights (e.g., Λ={0,5,10,20,40}\Lambda=\{0,5,10,20,40\}) and let 𝒜RL\mathcal{A}\_{\mathrm{RL}} be the set of RL variants (naive, soft, selection-only). For each (λ,v)∈Λ×𝒜RL(\lambda,v)\in\Lambda\times\mathcal{A}\_{\mathrm{RL}} and each structural baseline b∈𝒮b\in\mathcal{S}, we compute aggregate metrics:

|  |  |  |
| --- | --- | --- |
|  | μPnL​(π),σPnL​(π),μlaw​(π),VaRα​(π),CVaRα​(π),GFI​(π),\mu^{\mathrm{PnL}}(\pi),\quad\sigma^{\mathrm{PnL}}(\pi),\quad\mu^{\mathrm{law}}(\pi),\quad\mathrm{VaR}\_{\alpha}(\pi),\quad\mathrm{CVaR}\_{\alpha}(\pi),\quad\mathrm{GFI}(\pi), |  |

in both baseline and shocked environments (Section [6.3](https://arxiv.org/html/2511.17304v1#S6.SS3 "6.3 Metrics on three axes ‣ 6 Experimental Setup ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). Define the *law space* and *risk space*

|  |  |  |
| --- | --- | --- |
|  | ℒspace:=ℝ≥02(mean / max law penalty, coverage),ℛspace:=ℝ3(Sharpe, VaR, CVaR).\mathcal{L}\_{\mathrm{space}}:=\mathbb{R}\_{\geq 0}^{2}\quad(\text{mean / max law penalty, coverage}),\qquad\mathcal{R}\_{\mathrm{space}}:=\mathbb{R}^{3}\quad(\text{Sharpe, VaR, CVaR}). |  |

The empirical law-strength frontier is then the Pareto frontier of achievable tuples

|  |  |  |
| --- | --- | --- |
|  | ℱ:={(μlaw​(π),GFI​(π),μPnL​(π),VaRα​(π),CVaRα​(π)):π∈Πfrontier},\mathcal{F}:=\left\{\left(\mu^{\mathrm{law}}(\pi),\mathrm{GFI}(\pi),\mu^{\mathrm{PnL}}(\pi),\mathrm{VaR}\_{\alpha}(\pi),\mathrm{CVaR}\_{\alpha}(\pi)\right):\;\pi\in\Pi\_{\mathrm{frontier}}\right\}, |  |

where Πfrontier\Pi\_{\mathrm{frontier}} collects policies that are undominated with respect to the partial order

|  |  |  |
| --- | --- | --- |
|  | (ℓ1,g1,p1,v1,c1)⪯(ℓ2,g2,p2,v2,c2)⇔{ℓ1≤ℓ2,g1≤g2,p1≥p2,v1≥v2,c1≥c2.(\ell\_{1},g\_{1},p\_{1},v\_{1},c\_{1})\preceq(\ell\_{2},g\_{2},p\_{2},v\_{2},c\_{2})\iff\left\{\begin{aligned} &\ell\_{1}\leq\ell\_{2},\quad g\_{1}\leq g\_{2},\\ &p\_{1}\geq p\_{2},\quad v\_{1}\geq v\_{2},\quad c\_{1}\geq c\_{2}.\end{aligned}\right. |  |

Structurally, this recovers a multi-objective RL viewpoint [[58](https://arxiv.org/html/2511.17304v1#bib.bib58)] with objectives “profitability” vs “law alignment” vs “tail robustness”; the law-strength frontier is the set of efficient trade-offs in this space.

#### 4.4.2 Graceful Failure Index

We now define the GFI as a normalized measure of how law metrics degrade under shocks relative to a reference policy.

Let ξ∈[0,ξ¯]\xi\in[0,\bar{\xi}] denote a scalar shock intensity parameter (e.g., multiplying long variance and spot volatility), and let M​(π;ξ)M(\pi;\xi) be a scalar law metric (such as mean law penalty) for policy π\pi under shock ξ\xi. Fix a reference policy πref\pi\_{\mathrm{ref}} (e.g., naive RL or a structural baseline). We define the *infinitesimal GFI* as

|  |  |  |  |
| --- | --- | --- | --- |
|  | GFI​(π):=∂∂ξ​M​(π;ξ)|ξ=0∂∂ξ​M​(πref;ξ)|ξ=0,\mathrm{GFI}(\pi):=\frac{\left.\dfrac{\partial}{\partial\xi}M(\pi;\xi)\right|\_{\xi=0}}{\left.\dfrac{\partial}{\partial\xi}M(\pi\_{\mathrm{ref}};\xi)\right|\_{\xi=0}}, |  | (13) |

provided the denominator is non-zero. In practice, we approximate this by a finite-difference estimator

|  |  |  |
| --- | --- | --- |
|  | GFI^​(π)=M​(π;ξshock)−M​(π;0)M​(πref;ξshock)−M​(πref;0)+ε,\widehat{\mathrm{GFI}}(\pi)=\frac{M(\pi;\xi\_{\mathrm{shock}})-M(\pi;0)}{M(\pi\_{\mathrm{ref}};\xi\_{\mathrm{shock}})-M(\pi\_{\mathrm{ref}};0)+\varepsilon}, |  |

for a fixed shock level ξshock\xi\_{\mathrm{shock}} and small ε>0\varepsilon>0 for numerical stability. Values GFI​(π)<1\mathrm{GFI}(\pi)<1 indicate that π\pi degrades more *gracefully* than the reference, while GFI​(π)>1\mathrm{GFI}(\pi)>1 indicates worse degradation.

###### Remark 3 (Domain-agnostic design).

The definition ([13](https://arxiv.org/html/2511.17304v1#S4.E13 "In 4.4.2 Graceful Failure Index ‣ 4.4 Law-strength frontier and Graceful Failure Index ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) only requires: (i) an axiom-constrained system with a law penalty MM and (ii) a tunable shock parameter ξ\xi. As such, GFI extends immediately to other settings such as monotone yield curves, convex credit spreads, or physics-informed dynamics [[33](https://arxiv.org/html/2511.17304v1#bib.bib33), [37](https://arxiv.org/html/2511.17304v1#bib.bib37), [38](https://arxiv.org/html/2511.17304v1#bib.bib38)]. In Section [9](https://arxiv.org/html/2511.17304v1#S9 "9 Discussion and Conclusion ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") we argue that GFI can serve as a generic metric for *law-aligned graceful failure* in Scientific AI.

### 4.5 Law-strength trade-off

We finally formalize a structural trade-off between PnL and law alignment as the penalty weight λ\lambda increases. To simplify notation, define

|  |  |  |
| --- | --- | --- |
|  | L​(π):=Jlaw​(π),P​(π):=JPnL​(π):=Jℳ​(π)+J⟂​(π),L(\pi):=J^{\mathrm{law}}(\pi),\qquad P(\pi):=J^{\mathrm{PnL}}(\pi):=J^{\mathcal{M}}(\pi)+J^{\perp}(\pi), |  |

and let

|  |  |  |
| --- | --- | --- |
|  | 𝒢:={(L​(π),P​(π)):π∈Π}⊂ℝ≥0×ℝ\mathcal{G}:=\Big\{(L(\pi),P(\pi)):\pi\in\Pi\Big\}\subset\mathbb{R}\_{\geq 0}\times\mathbb{R} |  |

be the achievable law–PnL set. The soft law-seeking objective can be written

|  |  |  |
| --- | --- | --- |
|  | Jλsoft​(π)=P​(π)−λ​L​(π).J\_{\lambda}^{\mathrm{soft}}(\pi)=P(\pi)-\lambda L(\pi). |  |

###### Assumption 2 (Convex achievability and monotone trade-off).

The set 𝒢\mathcal{G} is compact and convex, and its lower-left Pareto boundary

|  |  |  |
| --- | --- | --- |
|  | ∂𝒢={(L,P)∈𝒢:there is no ​(L′,P′)∈𝒢​ with ​L′≤L,P′≥P,(L′,P′)≠(L,P)}\partial\mathcal{G}=\left\{(L,P)\in\mathcal{G}:\text{there is no }(L^{\prime},P^{\prime})\in\mathcal{G}\text{ with }L^{\prime}\leq L,\ P^{\prime}\geq P,\ (L^{\prime},P^{\prime})\neq(L,P)\right\} |  |

can be parameterized as the graph of a strictly decreasing, continuous function P⋆​(L)P^{\star}(L) on an interval [Lmin,Lmax][L\_{\min},L\_{\max}].

Assumption [2](https://arxiv.org/html/2511.17304v1#Thmassumption2 "Assumption 2 (Convex achievability and monotone trade-off). ‣ 4.5 Law-strength trade-off ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") is a standard regularity condition in multi-objective optimization and regularized RL [[58](https://arxiv.org/html/2511.17304v1#bib.bib58), [59](https://arxiv.org/html/2511.17304v1#bib.bib59)]: it states that (i) all relevant trade-offs between law penalties and PnL are attainable and (ii) lowering law penalties necessarily sacrifices some PnL in an average sense.

###### Theorem 2 (Law-strength trade-off).

Suppose Assumption [2](https://arxiv.org/html/2511.17304v1#Thmassumption2 "Assumption 2 (Convex achievability and monotone trade-off). ‣ 4.5 Law-strength trade-off ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") holds. For each λ≥0\lambda\geq 0, let

|  |  |  |
| --- | --- | --- |
|  | πλ⋆∈arg⁡maxπ∈Π⁡Jλsoft​(π)\pi\_{\lambda}^{\star}\in\arg\max\_{\pi\in\Pi}J\_{\lambda}^{\mathrm{soft}}(\pi) |  |

and denote (Lλ,Pλ):=(L​(πλ⋆),P​(πλ⋆))(L\_{\lambda},P\_{\lambda}):=(L(\pi\_{\lambda}^{\star}),P(\pi\_{\lambda}^{\star})). Then:

1. 1.

   For all λ1<λ2\lambda\_{1}<\lambda\_{2}, we have

   |  |  |  |
   | --- | --- | --- |
   |  | Lλ1≥Lλ2,Pλ1≥Pλ2.L\_{\lambda\_{1}}\;\geq\;L\_{\lambda\_{2}},\qquad P\_{\lambda\_{1}}\;\geq\;P\_{\lambda\_{2}}. |  |

   In words, increasing the law-penalty weight λ\lambda weakly decreases both the expected law penalty and the expected PnL.
2. 2.

   Moreover, if P⋆​(L)P^{\star}(L) is strictly concave on [Lmin,Lmax][L\_{\min},L\_{\max}], then the dependence λ↦(Lλ,Pλ)\lambda\mapsto(L\_{\lambda},P\_{\lambda}) traces out the Pareto frontier ∂𝒢\partial\mathcal{G}, and PλP\_{\lambda} is strictly decreasing in λ\lambda on any interval where LλL\_{\lambda} decreases.

##### Proof sketch.

Maximizing Jλsoft​(π)J\_{\lambda}^{\mathrm{soft}}(\pi) is equivalent to maximizing the linear functional P−λ​LP-\lambda L over the convex set 𝒢\mathcal{G}. For each λ\lambda, the optimizer (Lλ,Pλ)(L\_{\lambda},P\_{\lambda}) lies on the supporting line of 𝒢\mathcal{G} with slope −λ-\lambda. As λ\lambda increases, the supporting line rotates clockwise, shifting its tangency point along the Pareto boundary ∂𝒢\partial\mathcal{G}. This yields Lλ1≥Lλ2L\_{\lambda\_{1}}\geq L\_{\lambda\_{2}} and Pλ1≥Pλ2P\_{\lambda\_{1}}\geq P\_{\lambda\_{2}} for λ1<λ2\lambda\_{1}<\lambda\_{2}. Strict concavity of P⋆P^{\star} ensures that the tangency point is unique, and the mapping λ↦(Lλ,Pλ)\lambda\mapsto(L\_{\lambda},P\_{\lambda}) is strictly monotone along ∂𝒢\partial\mathcal{G}. A formal proof using convex analysis and subgradient conditions is provided in Appendix C.2. ∎

Theorem [2](https://arxiv.org/html/2511.17304v1#Thmtheorem2 "Theorem 2 (Law-strength trade-off). ‣ 4.5 Law-strength trade-off ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") shows that the *existence* of a law-strength trade-off is *structural*, not accidental: under mild convexity and monotonicity assumptions, one cannot increase λ\lambda to reduce law penalties without also reducing PnL. Combining this with Theorem [1](https://arxiv.org/html/2511.17304v1#Thmtheorem1 "Theorem 1 (Ghost-arbitrage incentive for naive RL). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), we obtain:

###### Corollary 1 (Inevitability of trade-off relative to naive RL).

Let (L0,P0)(L\_{0},P\_{0}) be the law–PnL pair of a naive-RL optimizer π0⋆\pi\_{0}^{\star} (with λ=0\lambda=0) and suppose Assumption [2](https://arxiv.org/html/2511.17304v1#Thmassumption2 "Assumption 2 (Convex achievability and monotone trade-off). ‣ 4.5 Law-strength trade-off ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") holds. For any λ>0\lambda>0 such that Lλ<L0L\_{\lambda}<L\_{0}, we necessarily have Pλ<P0P\_{\lambda}<P\_{0}. In particular, no soft-penalized RL policy can simultaneously maintain naive-level PnL and significantly lower law penalties.

Corollary [1](https://arxiv.org/html/2511.17304v1#Thmcorollary1 "Corollary 1 (Inevitability of trade-off relative to naive RL). ‣ Proof sketch. ‣ 4.5 Law-strength trade-off ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") underpins our empirical law-strength frontiers in Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"): once structural baselines and naive RL define the upper envelope of P⋆​(L)P^{\star}(L), all law-seeking RL variants lie strictly inside the Pareto region—they cannot *escape* the ghost-arbitrage incentive without sacrificing PnL, and they cannot outperform structurally law-aligned baselines without implicitly mimicking them.

Connection to entropy-regularized and constrained RL.
Our analysis parallels and complements classical results on entropy-regularized MDPs [[59](https://arxiv.org/html/2511.17304v1#bib.bib59), [60](https://arxiv.org/html/2511.17304v1#bib.bib60)] and constrained policy optimization [[54](https://arxiv.org/html/2511.17304v1#bib.bib54), [55](https://arxiv.org/html/2511.17304v1#bib.bib55)]: while those works study trade-offs between reward and entropy or safety constraints, we focus on trade-offs between PnL and *axiomatic law penalties*. In all cases, linear scalarization via a Lagrange multiplier (here, λ\lambda) induces a structural frontier over achievable objectives; our novelty lies in instantiating this in an axiomatic volatility world, decomposed into on-manifold and ghost-arbitrage components.

## 5 Structural Baselines: Axiomatic Strategy Class 𝒮\mathcal{S}

In this section we instantiate a low-capacity, structurally constrained strategy class
𝒮\mathcal{S} and three representative baselines—Zero-Hedge, Random-Gaussian, and
Vol-Trend—that serve as a proxy for *law-aligned* behavior on the volatility
law manifold. Rather than competing with state-of-the-art reinforcement-learning (RL)
trading systems, our goal is to contrast high-capacity, unconstrained RL policies with
simple, interpretable and structurally law-consistent strategies, in the spirit of
classical replication and hedging approaches [[70](https://arxiv.org/html/2511.17304v1#bib.bib70), [67](https://arxiv.org/html/2511.17304v1#bib.bib67), [23](https://arxiv.org/html/2511.17304v1#bib.bib23), [24](https://arxiv.org/html/2511.17304v1#bib.bib24)].

Throughout this section, we work in the MDP setting, with
state space 𝒮\mathcal{S}, action space 𝒜⊂ℝk\mathcal{A}\subset\mathbb{R}^{k}, and
one-step P&L reward r​(st,at)r(s\_{t},a\_{t}) generated from the world model. We denote by 𝖫𝖺𝗐𝖯𝖾𝗇𝖺𝗅𝗍𝗒​(st)\mathsf{LawPenalty}(s\_{t}) the
per-step law penalty ℒϕ\mathcal{L}\_{\phi} evaluated on the (predicted) implied volatility
surface associated with state sts\_{t}.

### 5.1 Baseline definitions and structural priors

We first define a *structural strategy class* 𝒮\mathcal{S} and then specify three
baseline strategies bZH,bRG,bVT∈𝒮b^{\mathrm{ZH}},b^{\mathrm{RG}},b^{\mathrm{VT}}\in\mathcal{S}.

###### Definition 8 (Structural strategy class 𝒮\mathcal{S}).

Let f:𝒮→ℝmf:\mathcal{S}\to\mathbb{R}^{m} be a fixed feature map extracting low-dimensional
state descriptors (e.g., realized variance, term-structure slope, realized trend).
We define the structural class

|  |  |  |
| --- | --- | --- |
|  | 𝒮:={πθ:𝒮→𝒜|πθ​(s)=g​(θ⊤​f​(s)),θ∈Θ⊂ℝm,g​ scalar Lipschitz, odd, and bounded},\mathcal{S}:=\Bigl\{\pi\_{\theta}:\mathcal{S}\to\mathcal{A}\,\Big|\,\pi\_{\theta}(s)=g\bigl(\theta^{\top}f(s)\bigr),~\theta\in\Theta\subset\mathbb{R}^{m},~g\text{ scalar Lipschitz, odd, and bounded}\Bigr\}, |  |

where Θ\Theta is a compact parameter set and gg encodes a saturating leverage map
(e.g., g​(u)=κ​tanh⁡(u)g(u)=\kappa\tanh(u) with κ>0\kappa>0 a leverage cap).

Thus, 𝒮\mathcal{S} consists of *one-factor* or low-factor
trend/risk-based strategies familiar from classical managed-futures and option-hedging
literature [[24](https://arxiv.org/html/2511.17304v1#bib.bib24), [23](https://arxiv.org/html/2511.17304v1#bib.bib23)]. We now instantiate
three members of 𝒮\mathcal{S} used in our experiments.

#### 5.1.1 Zero-Hedge: law-neutral benchmark

The Zero-Hedge baseline bZHb^{\mathrm{ZH}} is defined by the identically zero policy,

|  |  |  |  |
| --- | --- | --- | --- |
|  | bZH​(st)≡0for all ​st∈𝒮.b^{\mathrm{ZH}}(s\_{t})\equiv 0\quad\text{for all }s\_{t}\in\mathcal{S}. |  | (14) |

Economically, this corresponds to holding only the initial portfolio and never
rebalancing; P&L arises solely from the exogenous cash-flow profile of the hedged
position (e.g., short option) and the law-consistent volatility generator. In our
setting, bZHb^{\mathrm{ZH}} provides a *law-neutral* benchmark: it neither
attempts to exploit ghost arbitrage nor introduces additional exposures that correlate
with law violations.

#### 5.1.2 Random-Gaussian: unconstrained exploration probe

The Random-Gaussian baseline bRGb^{\mathrm{RG}} applies a Gaussian random policy
conditioned on low-dimensional state features:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bRG​(st)=κ​ξt,ξt∼𝒩​(0,Σ​(f​(st))),b^{\mathrm{RG}}(s\_{t})=\kappa\,\xi\_{t},\qquad\xi\_{t}\sim\mathcal{N}\!\bigl(0,\Sigma(f(s\_{t}))\bigr), |  | (15) |

where κ>0\kappa>0 scales overall leverage and Σ​(⋅)\Sigma(\cdot) is a diagonal covariance
matrix whose entries depend on simple risk features (e.g., inverse realized volatility).
Random policies of this form appear as sanity-check baselines in RL for trading and
hedging [[25](https://arxiv.org/html/2511.17304v1#bib.bib25), [67](https://arxiv.org/html/2511.17304v1#bib.bib67)], and here serve as a *noisy probe*
of how a generic, non-structured policy interacts with ghost arbitrage in the learned
world model.

#### 5.1.3 Vol-Trend: parametric volatility trend-following

The Vol-Trend baseline bVTb^{\mathrm{VT}} is a simple parametric strategy inspired by
time-series momentum and volatility trend-following
[[24](https://arxiv.org/html/2511.17304v1#bib.bib24), [70](https://arxiv.org/html/2511.17304v1#bib.bib70)]. Let
σ^t​(K,T)\widehat{\sigma}\_{t}(K,T) be the predicted implied volatility surface at time tt, and
let σ¯t\bar{\sigma}\_{t} denote a scalar summary statistic capturing its *level* or
*slope*, such as

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ¯t:=1|𝒢|​∑(K,T)∈𝒢σ^t​(K,T),\bar{\sigma}\_{t}:=\frac{1}{|\mathcal{G}|}\sum\_{(K,T)\in\mathcal{G}}\widehat{\sigma}\_{t}(K,T), |  | (16) |

where 𝒢\mathcal{G} is a pre-specified grid of strikes and maturities. Define a
trend signal by an exponentially weighted moving average (EWMA)

|  |  |  |
| --- | --- | --- |
|  | τt:=EWMAβ​(σ¯t−σ¯t−1),β∈(0,1).\tau\_{t}:=\mathrm{EWMA}\_{\beta}(\bar{\sigma}\_{t}-\bar{\sigma}\_{t-1}),\qquad\beta\in(0,1). |  |

The Vol-Trend policy takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | bVT​(st)=κ​tanh⁡(θ​τt),b^{\mathrm{VT}}(s\_{t})=\kappa\,\tanh(\theta\,\tau\_{t}), |  | (17) |

for parameters θ∈ℝ\theta\in\mathbb{R} and leverage cap κ>0\kappa>0. Positions are
allocated across option buckets (e.g., short-dated ATM, mid-maturity OTM) in fixed
proportions, so that bVTb^{\mathrm{VT}} is a one-factor trend-following strategy in
*implied volatility* rather than in the underlying price.

By construction, both bZHb^{\mathrm{ZH}} and bVTb^{\mathrm{VT}} live inside the
structural class 𝒮\mathcal{S} of Definition [8](https://arxiv.org/html/2511.17304v1#Thmdefinition8 "Definition 8 (Structural strategy class 𝒮). ‣ 5.1 Baseline definitions and structural priors ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") for a suitable
choice of features ff and parameter sets Θ\Theta, whereas bRGb^{\mathrm{RG}} can be
seen as a stochastic perturbation of a mean-zero element of 𝒮\mathcal{S}.

#### 5.1.4 Fairness of comparison

Compared to the high-capacity policy class used by PPO-type RL agents,
the structural class 𝒮\mathcal{S} is deliberately low-dimensional and heavily
regularized. From a “benchmarking” perspective this creates a capacity mismatch:
RL policies can in principle approximate arbitrary non-linear hedging rules, whereas
bZHb^{\mathrm{ZH}}, bRGb^{\mathrm{RG}} and bVTb^{\mathrm{VT}} are effectively one- or
few-parameter strategies.

This asymmetry is *by design* and aligns with our no-free-lunch theme:
structural strategies in 𝒮\mathcal{S} are intended as proxies for law-aligned and
axiom-consistent behavior, much like classical delta-vega hedges and
trend-following overlays [[23](https://arxiv.org/html/2511.17304v1#bib.bib23), [24](https://arxiv.org/html/2511.17304v1#bib.bib24)].
Our central question is therefore not whether high-capacity RL can match the P&L of
low-capacity strategies (it almost always can in-sample), but whether *unconstrained
law-seeking RL can *dominate* such structural strategies on both profitability
and axiomatic law metrics*.

### 5.2 Law-alignment properties of structural baselines

We now formalize the notion that structural baselines are, in an appropriate sense,
*law-aligned*: they do not systematically exploit off-manifold ghost arbitrage and
tend to exhibit lower Graceful Failure Index (GFI) under volatility shocks than
unconstrained RL policies.

Let 𝖫𝖺𝗐𝖯𝖾𝗇𝖺𝗅𝗍𝗒​(st)\mathsf{LawPenalty}(s\_{t}) denote the per-step law penalty
ℒϕ​(σ^t)\mathcal{L}\_{\phi}(\widehat{\sigma}\_{t}) computed from the world model prediction, and
write

|  |  |  |
| --- | --- | --- |
|  | 𝖫𝖯¯​(π):=𝔼π​[𝖫𝖺𝗐𝖯𝖾𝗇𝖺𝗅𝗍𝗒​(st)],GFI​(π)\overline{\mathsf{LP}}(\pi):=\mathbb{E}\_{\pi}\bigl[\mathsf{LawPenalty}(s\_{t})\bigr],\qquad\mathrm{GFI}(\pi) |  |

for the expected law penalty and Graceful Failure Index of policy π\pi under the
baseline vs. shock environments (Section [4.4](https://arxiv.org/html/2511.17304v1#S4.SS4 "4.4 Law-strength frontier and Graceful Failure Index ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

###### Definition 9 (Law-aligned strategy class).

A set of policies 𝒮\mathcal{S} is *law-aligned* with respect to a world model
if there exist constants CLP,CGFI<∞C\_{\mathrm{LP}},C\_{\mathrm{GFI}}<\infty such that

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒮𝖫𝖯¯​(π)≤CLP,supπ∈𝒮GFI​(π)≤CGFI,\sup\_{\pi\in\mathcal{S}}\overline{\mathsf{LP}}(\pi)\leq C\_{\mathrm{LP}},\qquad\sup\_{\pi\in\mathcal{S}}\mathrm{GFI}(\pi)\leq C\_{\mathrm{GFI}}, |  |

and these bounds are strictly smaller than the corresponding suprema over the full
unconstrained policy class Π\Pi used by RL.

Intuitively, Definition [9](https://arxiv.org/html/2511.17304v1#Thmdefinition9 "Definition 9 (Law-aligned strategy class). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") says that law-aligned classes
cannot arbitrarily amplify law violations or shock sensitivity by “chasing” ghost
arbitrage. We now state a structural result that justifies using our baselines as
proxies for such a class.

###### Proposition 7 (Law-alignment of structural baselines).

Assume the volatility generator is law-consistent
(σt∈ℳvol\sigma\_{t}\in\mathcal{M}^{\mathrm{vol}} almost surely) and the world model satisfies
the Lipschitz and bounded-error conditions of Proposition.
Then there exist constants CLP,CGFI<∞C\_{\mathrm{LP}},C\_{\mathrm{GFI}}<\infty, depending only
on the generator and world-model error, such that:

1. 1.

   The structural class 𝒮\mathcal{S} of Definition [8](https://arxiv.org/html/2511.17304v1#Thmdefinition8 "Definition 8 (Structural strategy class 𝒮). ‣ 5.1 Baseline definitions and structural priors ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") is
   law-aligned in the sense of Definition [9](https://arxiv.org/html/2511.17304v1#Thmdefinition9 "Definition 9 (Law-aligned strategy class). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
2. 2.

   In particular, the baselines bZHb^{\mathrm{ZH}} and bVTb^{\mathrm{VT}} satisfy

   |  |  |  |
   | --- | --- | --- |
   |  | 𝖫𝖯¯​(bZH),𝖫𝖯¯​(bVT)≤CLP,GFI​(bZH),GFI​(bVT)≤CGFI,\overline{\mathsf{LP}}(b^{\mathrm{ZH}}),~\overline{\mathsf{LP}}(b^{\mathrm{VT}})\leq C\_{\mathrm{LP}},\qquad\mathrm{GFI}(b^{\mathrm{ZH}}),~\mathrm{GFI}(b^{\mathrm{VT}})\leq C\_{\mathrm{GFI}}, |  |

   with CLPC\_{\mathrm{LP}} and CGFIC\_{\mathrm{GFI}} strictly below the empirical levels
   attained by unconstrained RL policies in our experiments.
3. 3.

   The Random-Gaussian baseline bRGb^{\mathrm{RG}} has
   𝖫𝖯¯​(bRG)≤CLP′\overline{\mathsf{LP}}(b^{\mathrm{RG}})\leq C\_{\mathrm{LP}}^{\prime} and
   GFI​(bRG)≤CGFI′\mathrm{GFI}(b^{\mathrm{RG}})\leq C\_{\mathrm{GFI}}^{\prime} for some finite
   CLP′,CGFI′C\_{\mathrm{LP}}^{\prime},C\_{\mathrm{GFI}}^{\prime}, but these bounds are typically looser than
   for bZH,bVTb^{\mathrm{ZH}},b^{\mathrm{VT}}, reflecting its noisier, less structured
   behavior.

##### Proof sketch.

Because the volatility generator is law-consistent, any law violations arise solely
from the world-model approximation error.So that
𝖫𝖺𝗐𝖯𝖾𝗇𝖺𝗅𝗍𝗒​(st)\mathsf{LawPenalty}(s\_{t}) is uniformly bounded on bounded subsets of the state space.
For policies in 𝒮\mathcal{S}, the boundedness of gg and compactness of Θ\Theta
imply a uniform bound on trading exposures and hence on the induced state process,
yielding uniform upper bounds on 𝖫𝖯¯\overline{\mathsf{LP}} and GFI.

For bZHb^{\mathrm{ZH}}, the policy takes no action, so its state process coincides with
the exogenous world-model trajectory; thus 𝖫𝖯¯​(bZH)\overline{\mathsf{LP}}(b^{\mathrm{ZH}})
and GFI​(bZH)\mathrm{GFI}(b^{\mathrm{ZH}}) coincide with the “background” law-violation
profile of the world model under shocks. For
bVTb^{\mathrm{VT}}, the one-factor trend signal and bounded leverage ensure that
positions respond smoothly to volatility changes, so that the policy does not
systematically seek states with elevated law penalties; this yields bounds comparable
to bZHb^{\mathrm{ZH}}.

By contrast, unconstrained RL policies can amplify exposure precisely in regions where
the ghost component r⟂r^{\perp} is large, leading to
higher empirical 𝖫𝖯¯\overline{\mathsf{LP}} and GFI levels. A rigorous argument based on
Lyapunov-type bounds on the Markov chain induced by 𝒮\mathcal{S} vs. Π\Pi is given
in Appendix D.

Proposition [7](https://arxiv.org/html/2511.17304v1#Thmproposition7 "Proposition 7 (Law-alignment of structural baselines). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") formalizes a key design choice of our
experimental pipeline: structural baselines are not merely “toy competitors”, but
represent an axiomatic, law-aligned class 𝒮\mathcal{S} against which the performance
of unconstrained RL can be meaningfully compared. In Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"),
we will see that, empirically, Zero-Hedge and Vol-Trend sit on or near the empirical
*law-strength frontier*, while law-seeking RL variants lie strictly below them in
the P&L–law-penalty–GFI space.

## 6 Experimental Setup

In this section, we specify the environments, training protocols, and evaluation metrics used to stress-test law-seeking reinforcement learning (RL) on volatility world models. Throughout, RL is treated as a *diagnostic instrument* for our axiomatic pipeline rather than as a production trading system. The design is intentionally simple but structured, so that the relationship between axioms, world-model misspecification, and policy behavior can be analyzed with minimal confounders.

### 6.1 Environments: baseline vs shock

We work with the synthetic generator and volatility law manifold ℳvol\mathcal{M}\_{\mathrm{vol}} introduced in the previous sections. The generator produces discrete-time trajectories of total-variance surfaces

|  |  |  |
| --- | --- | --- |
|  | {wt}t=0T,wt∈ℳvol⊂ℝd,\{w\_{t}\}\_{t=0}^{T},\qquad w\_{t}\in\mathcal{M}\_{\mathrm{vol}}\subset\mathbb{R}^{d}, |  |

defined on a fixed maturity–strike grid. The grid is chosen to roughly mirror an SPX/VIX-style market: maturities range from 1 month to 2 years in monthly or bimonthly steps, and strikes range from 0.5×0.5\times to 1.5×1.5\times spot in a small number of relative moneyness buckets. This keeps the problem from being a purely toy example while maintaining a finite-dimensional convex template.

##### Baseline regime.

In the *baseline* regime, the generator parameters yield a stationary, law-consistent world:

|  |  |  |
| --- | --- | --- |
|  | wt∈ℳvolalmost surely for all ​t.w\_{t}\in\mathcal{M}\_{\mathrm{vol}}\quad\text{almost surely for all }t. |  |

We denote by ℙbase\mathbb{P}^{\text{base}} the induced distribution over full episodes

|  |  |  |
| --- | --- | --- |
|  | τ={(wt,St,at,Δ​PnLt)}t=0T−1,\tau=\{(w\_{t},S\_{t},a\_{t},\Delta\mathrm{PnL}\_{t})\}\_{t=0}^{T-1}, |  |

where StS\_{t} denotes the underlying index level, ata\_{t} is the chosen hedge action, and Δ​PnLt\Delta\mathrm{PnL}\_{t} is the instantaneous P&L generated by the environment given (wt,St,at)(w\_{t},S\_{t},a\_{t}). By construction, all static no-arbitrage axioms are satisfied by wtw\_{t}; any law violations can only arise from the *world model* predictions, not from the generator.

##### Shock regime.

To probe robustness and graceful failure, we introduce a *shock* regime in which the same axioms hold, but the volatility regime is stressed. The idea is to change the distribution of trajectories—not the underlying laws.

Operationally, we decompose the total variance wtw\_{t} into a “long-variance” component and a “spot-variance” component:

|  |  |  |
| --- | --- | --- |
|  | wt=wtlong+wtspot,w\_{t}=w\_{t}^{\text{long}}+w\_{t}^{\text{spot}}, |  |

where wtlongw\_{t}^{\text{long}} aggregates longer maturities and wtspotw\_{t}^{\text{spot}} aggregates short maturities and near-spot behaviour. The *shock transformation* is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | wtshock:=αlong​wtlong+αspot​wtspot,w\_{t}^{\mathrm{shock}}:=\alpha\_{\text{long}}\,w\_{t}^{\text{long}}+\alpha\_{\text{spot}}\,w\_{t}^{\text{spot}}, |  | (18) |

with (αlong,αspot)=(4,2)(\alpha\_{\text{long}},\alpha\_{\text{spot}})=(4,2) in our main experiments, i.e., we quadruple the long-term variance level and double the spot volatility component. The underlying index dynamics StS\_{t} are adjusted consistently with the increased variance, so that no obvious static arbitrage is created by the transformation.

We denote by ℙshock\mathbb{P}^{\mathrm{shock}} the distribution over episodes generated by applying ([18](https://arxiv.org/html/2511.17304v1#S6.E18 "In Shock regime. ‣ 6.1 Environments: baseline vs shock ‣ 6 Experimental Setup ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) within the same structural model. In particular:

1. 1.

   the same axioms defining ℳvol\mathcal{M}\_{\mathrm{vol}} remain valid for the *ground-truth* generator,
2. 2.

   but trajectories seen by the neural world model and RL policies lie in a higher-volatility regime, with steeper term-structure and fatter tails.

This baseline–shock pair (ℙbase,ℙshock)(\mathbb{P}^{\text{base}},\mathbb{P}^{\mathrm{shock}}) underpins the definition of the Graceful Failure Index in later sections.

##### World model vs generator.

Crucially, the shock is applied at the level of the *underlying generator*, while the world model (and its parameters) are kept fixed. This mimics a realistic situation where a risk model trained in one regime is deployed in another, without retraining, and any change in behaviour is due to distribution shift rather than to an updated model.

### 6.2 Training regimes and λ\lambda-grid

We now specify how RL policies are trained on the fixed world model, and how the law-strength parameter λ\lambda is swept.

##### RL objective and λ\lambda-penalization.

Let πθ\pi\_{\theta} denote a stochastic policy with parameters θ\theta (e.g., a Gaussian policy whose mean and log-standard deviation are given by an MLP over the state). For a given λ≥0\lambda\geq 0, we define the law-penalized return

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jλ​(θ):=𝔼​[∑t=0T−1γt​(Δ​PnLt−λ​ℒϕ​(wt))],J\_{\lambda}(\theta):=\mathbb{E}\Bigg[\sum\_{t=0}^{T-1}\gamma^{t}\Big(\Delta\mathrm{PnL}\_{t}-\lambda\,\mathcal{L}\_{\phi}(w\_{t})\Big)\Bigg], |  | (19) |

where γ∈(0,1)\gamma\in(0,1) is a discount factor, Δ​PnLt\Delta\mathrm{PnL}\_{t} is the step P&L produced by the world model, and ℒϕ​(wt)\mathcal{L}\_{\phi}(w\_{t}) is the law penalty at time tt computed from the world model’s predicted total variance (Section 2). In all experiments, we fix the discount factor and penalty functional and vary *only* λ\lambda and the training regime.

##### Naive RL.

*Naive RL* corresponds to λ=0\lambda=0, i.e.,

|  |  |  |
| --- | --- | --- |
|  | J0​(θ)=𝔼​[∑t=0T−1γt​Δ​PnLt],J\_{0}(\theta)=\mathbb{E}\Bigg[\sum\_{t=0}^{T-1}\gamma^{t}\Delta\mathrm{PnL}\_{t}\Bigg], |  |

so that the agent is trained to maximize P&L alone, without any explicit concern for law penalties. This serves as a reference point for understanding the ghost-arbitrage incentive established in Theorem 4.1.

##### Soft law-seeking RL.

For each λ∈{5,10,20,40}\lambda\in\{5,10,20,40\}, *soft law-seeking RL* directly optimizes Jλ​(θ)J\_{\lambda}(\theta). The gradient of the PPO objective is thus shaped by both P&L and the law penalty. Intuitively, larger λ\lambda should discourage trajectories that significantly violate the volatility axioms, at the cost of accepting lower P&L when the two are in conflict.

##### Selection-only RL.

*Selection-only RL* keeps the training objective purely P&L-based (J0J\_{0}), but varies the stopping time and model selection based on law metrics:

1. 1.

   For each random seed, we store checkpoints along training at regular intervals.
2. 2.

   After training, we evaluate each checkpoint on a held-out set of episodes and compute a scalar law-alignment score (e.g., a weighted combination of mean law penalty and GFI).
3. 3.

   A selection functional SS then picks the checkpoint minimizing this law score, subject to mild constraints on P&L (e.g., not falling below a naive-RL baseline by more than a threshold).

This variant tests whether, *even if training is naive*, intelligent selection based on law metrics can recover law-aligned behaviour.

##### Statistical protocol.

Each configuration (algorithm ×\times λ\lambda value) is currently trained with a single random seed. For each trained policy, we evaluate a large number of episodes under both ℙbase\mathbb{P}^{\text{base}} and ℙshock\mathbb{P}^{\mathrm{shock}} to estimate metrics (means, Sharpe, law penalties, VaR, CVaR, GFI).

In this single-seed regime, our results should be interpreted as a detailed *case study*: the curves and summary metrics are representative of one run per configuration, not averaged across many trainings. The pipeline is, however, designed to support multi-seed experiments:

1. 1.

   In a multi-seed setting, we would report, for each metric and configuration, the empirical mean and standard error across seeds, and display error bars or confidence bands on frontier plots.
2. 2.

   None of the definitions or plots need to change for multi-seed; only the aggregation layer is different.

### 6.3 Metrics on three axes

We evaluate policies along three complementary axes: profitability, law alignment, and tail robustness. All numerical summaries and plots in the results section are derived from the metrics defined here.

##### Profitability.

Let Δ​PnLt\Delta\mathrm{PnL}\_{t} denote the per-step P&L. For a fixed policy π\pi, we define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μpnl​(π)\displaystyle\mu\_{\mathrm{pnl}}(\pi) | :=𝔼​[Δ​PnLt],\displaystyle:=\mathbb{E}[\Delta\mathrm{PnL}\_{t}], |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σpnl​(π)\displaystyle\sigma\_{\mathrm{pnl}}(\pi) | :=Var​[Δ​PnLt].\displaystyle:=\sqrt{\mathrm{Var}[\Delta\mathrm{PnL}\_{t}]}. |  | (21) |

The per-step Sharpe ratio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sharpe​(π):=μpnl​(π)σpnl​(π)+ε,\mathrm{Sharpe}(\pi):=\frac{\mu\_{\mathrm{pnl}}(\pi)}{\sigma\_{\mathrm{pnl}}(\pi)+\varepsilon}, |  | (22) |

with a small ε>0\varepsilon>0 added only for numerical stability when the variance is very small. In tables, we report both (μpnl,Sharpe)(\mu\_{\mathrm{pnl}},\mathrm{Sharpe}) so that high-return/high-volatility and low-return/low-volatility policies can be distinguished.

##### Law alignment.

For each step, the world model induces a total-variance prediction wtw\_{t} from which we compute the law penalty ℒϕ​(wt)\mathcal{L}\_{\phi}(w\_{t}) as defined in Section 2. We then aggregate:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μlaw​(π)\displaystyle\mu\_{\mathrm{law}}(\pi) | :=𝔼​[ℒϕ​(wt)],\displaystyle:=\mathbb{E}[\mathcal{L}\_{\phi}(w\_{t})], |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒmax​(π)\displaystyle\mathcal{L}\_{\max}(\pi) | :=𝔼​[max0≤t<T⁡ℒϕ​(wt)].\displaystyle:=\mathbb{E}\Big[\max\_{0\leq t<T}\mathcal{L}\_{\phi}(w\_{t})\Big]. |  | (24) |

The *law coverage* at threshold τ>0\tau>0 is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Coverτ​(π):=𝔼​[𝟏​{ℒϕ​(wt)<τ}],\mathrm{Cover}\_{\tau}(\pi):=\mathbb{E}\big[\mathbf{1}\{\mathcal{L}\_{\phi}(w\_{t})<\tau\}\big], |  | (25) |

and we report coverage at τ=0.003\tau=0.003 and τ=0.006\tau=0.006 in our experiments.

The *Graceful Failure Index* (GFI), introduced earlier on the theoretical side, is instantiated here as

|  |  |  |  |
| --- | --- | --- | --- |
|  | GFI​(π):=μlawshock​(π)−μlawbase​(π)Ishock,\mathrm{GFI}(\pi):=\frac{\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi)-\mu\_{\mathrm{law}}^{\text{base}}(\pi)}{I\_{\mathrm{shock}}}, |  | (26) |

where μlawshock\mu\_{\mathrm{law}}^{\mathrm{shock}} and μlawbase\mu\_{\mathrm{law}}^{\text{base}} are mean law penalties under the shock and baseline regimes, and IshockI\_{\mathrm{shock}} is a scalar encoding the shock intensity (e.g., a norm of (αlong−1,αspot−1)(\alpha\_{\text{long}}-1,\alpha\_{\text{spot}}-1)). Lower GFI indicates that law metrics degrade less per unit of shock, i.e., more graceful failure.

##### Tail robustness.

To quantify downside risk, we consider per-step losses

|  |  |  |
| --- | --- | --- |
|  | X:=−Δ​PnLtX:=-\Delta\mathrm{PnL}\_{t} |  |

and compute:

1. 1.

   the 5%5\% *Value-at-Risk* (VaR), defined as the upper 5%5\%-quantile of XX,
2. 2.

   the corresponding *Conditional Value-at-Risk* (CVaR), defined as the conditional expectation of XX beyond that quantile.

We report VaR5%\mathrm{VaR}\_{5\%} and CVaR5%\mathrm{CVaR}\_{5\%} under both baseline and shock regimes, and their differences (Δ​VaR,Δ​CVaR)(\Delta\mathrm{VaR},\Delta\mathrm{CVaR}) serve as tail-robustness indicators. Policies with small increases (or even decreases) in VaR/CVaR under shock are considered more robust in the tails.

### 6.4 Implementation and reproducibility

Finally, we summarize the implementation details and the way figures are organized.

##### Software and hardware.

All experiments are implemented in Python using a standard deep-learning framework for neural networks and a Gym-style interface for the volatility environment. The world model and RL policies are trained on a single GPU with a modest amount of memory (e.g., 12–24 GB), while evaluation runs are CPU-bound. The code is organized so that all hyperparameters, random seeds, and experiment configurations are specified in a small number of configuration files.

##### Hyperparameters.

We use an actor–critic architecture with:

1. 1.

   a shared multilayer perceptron encoder for the state,
2. 2.

   separate heads for the policy mean, policy log-standard deviation, and value function,
3. 3.

   PPO-style clipped policy updates with a fixed number of epochs per batch,
4. 4.

   mini-batches containing a few thousand environment steps per update,
5. 5.

   standard optimizers and learning rates in a narrow range.

These hyperparameters are kept fixed across naive RL, soft law-seeking RL, and selection-only RL; only λ\lambda and the training regime differ. Structural baselines are implemented as closed-form or low-dimensional parametric strategies with no trainable weights.

##### Figure families and outputs.

The experimental pipeline produces fourteen figures, which we categorize into three families that are repeatedly referenced later:

1. 1.

   Dynamics Plots (e.g., Figs. 3–7): time-series of per-step P&L and law penalties for representative policies in baseline and shock regimes.
2. 2.

   Frontier Plots (e.g., Figs. 8–10): law-strength frontiers that plot mean law penalty, GFI, and other law metrics against profitability metrics across different λ\lambda and across RL vs structural baselines.
3. 3.

   Diagnostic Plots (e.g., Figs. 11–13): scatter plots and histograms of P&L vs law penalties, VaR, CVaR, and related quantities, used to interpret whether observed trade-offs arise from systematic behaviour or a small number of extreme paths.

Together, these figures provide a multi-perspective view of each policy: how it behaves over time, where it lies on the law-strength frontier, and why it occupies that position from a distributional standpoint. This structure will be used in the next section to present and interpret our empirical findings.

## 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers

In this section, we address RQ1–RQ3 empirically using the volatility world model, RL variants, and structural baselines introduced in Secs. [3](https://arxiv.org/html/2511.17304v1#S3 "3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[5](https://arxiv.org/html/2511.17304v1#S5 "5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
Our analysis is supported by thirteen figures, stored as
Figure\_1.png–Figure\_13.png, and by explicit numerical
summaries drawn from the console outputs:

1. 1.

   Figure [1(a)](https://arxiv.org/html/2511.17304v1#S7.F1.sf1 "In Figure 1 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") (Figure\_1.png):
   schematic overview of the axiomatic evaluation pipeline
   (axioms →\to law manifold →\to neural world model →\to RL and structural baselines).
2. 2.

   Figure [1(b)](https://arxiv.org/html/2511.17304v1#S7.F1.sf2 "In Figure 1 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") (Figure\_2.png):
   diagnostics for the volatility world model, comparing train/validation errors
   and law penalties of predictions vs. the law-consistent generator.
3. 3.

   Figures [2(a)](https://arxiv.org/html/2511.17304v1#S7.F2.sf1 "In Figure 2 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[3](https://arxiv.org/html/2511.17304v1#S7.F3 "Figure 3 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
   (Figure\_3.png–Figure\_7.png):
   *Dynamics plots*, showing time series of step P&L and law penalties
   under the baseline and shock regimes for naive RL, law-seeking RL, and
   structural baselines.
4. 4.

   Figures [4(a)](https://arxiv.org/html/2511.17304v1#S7.F4.sf1 "In Figure 4 ‣ 7.2.1 Baseline vs. shock metrics ‣ 7.2 RQ2 – RL vs. structural baselines under shocks ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[4(c)](https://arxiv.org/html/2511.17304v1#S7.F4.sf3 "In Figure 4 ‣ 7.2.1 Baseline vs. shock metrics ‣ 7.2 RQ2 – RL vs. structural baselines under shocks ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
   (Figure\_8.png–Figure\_10.png):
   *Frontier plots*, tracing law-strength frontiers
   (GFI vs. law penalty, and tail risk vs. law penalty) across RL variants
   and structural baselines.
5. 5.

   Figures [5(a)](https://arxiv.org/html/2511.17304v1#S7.F5.sf1 "In Figure 5 ‣ 7.3.3 Diagnostic plots: ruling out trivial artefacts ‣ 7.3 Law-strength frontiers and Pareto dominance ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[5(c)](https://arxiv.org/html/2511.17304v1#S7.F5.sf3 "In Figure 5 ‣ 7.3.3 Diagnostic plots: ruling out trivial artefacts ‣ 7.3 Law-strength frontiers and Pareto dominance ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
   (Figure\_11.png–Figure\_13.png):
   *Diagnostic plots*, including scatter/heatmaps of step P&L vs. law
   penalty and histograms of law penalties, for RL policies and baselines.

We highlight the most informative patterns in the main text and relegate
additional runs to the Appendix; throughout, we phrase our statements as
*case-study observations* and explicitly connect them, where appropriate,
to the structural incentive and trade-off results.

### 7.1 RQ1 – Do law penalties help naive RL?

RQ1 asks whether adding law penalties to naive RL improves law alignment and
graceful failure at comparable profitability.

#### 7.1.1 Dynamics patterns (subset of dynamics plots)

Figure [2(a)](https://arxiv.org/html/2511.17304v1#S7.F2.sf1 "In Figure 2 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") (Figure\_3.png) shows a
representative baseline-regime episode for naive RL (PPO on pure P&L) and a
soft law-seeking variant with λ=20\lambda=20.
The top panel plots step P&L, while the bottom panel plots the corresponding
step-wise law penalty ℒϕ\mathcal{L}\_{\phi}.
In this particular run, we observe that naive RL tends to maintain slightly
higher step P&L on average, at the cost of moderately elevated law penalties,
whereas the λ=20\lambda=20 law-seeking policy reduces some of the largest
penalties but does not improve—and often worsens—the P&L path.

Figure [2(b)](https://arxiv.org/html/2511.17304v1#S7.F2.sf2 "In Figure 2 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") (Figure\_4.png) reports the same
comparison under the shock regime (long variance ×4\times 4, spot volatility
×2\times 2).
The shock amplifies both P&L variability and law penalties.
In our runs, the naive RL policy exhibits higher volatility in both P&L and
ℒϕ\mathcal{L}\_{\phi}, while the λ=20\lambda=20 policy appears somewhat more
conservative but does not clearly dominate in terms of drawdowns.
These observations are consistent with the incentive picture: naive RL is tempted to exploit off-manifold
ghost arbitrage, which can generate both higher P&L spikes and larger law
violations.

To place RL in context, Figure [2(c)](https://arxiv.org/html/2511.17304v1#S7.F2.sf3 "In Figure 2 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
(Figure\_5.png) overlays time-series trajectories for
naive RL, law-seeking RL, and the structural baselines (Zero-Hedge,
Vol-Trend, Random-Gaussian) in the baseline regime.
Figure [2(d)](https://arxiv.org/html/2511.17304v1#S7.F2.sf4 "In Figure 2 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") (Figure\_6.png) repeats this
comparison under shock, and Figure [3](https://arxiv.org/html/2511.17304v1#S7.F3 "Figure 3 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
(Figure\_7.png) presents side-by-side trajectories for a single policy
across the two regimes.
In our runs, the structural baselines exhibit comparatively smooth P&L paths
and low law penalties, while RL trajectories are more erratic and spend
substantial time in higher-penalty regions, foreshadowing the quantitative
metrics reported below.

We deliberately restrict the main text to these representative dynamics plots;
additional realizations, including different λ\lambda values and seeds, are
provided in the Appendix and show qualitatively similar patterns.

![Refer to caption](Figure_1.png)


(a) Axiomatic evaluation pipeline:
market axioms induce a law manifold ℳvol\mathcal{M}^{\text{vol}};
a synthetic generator produces law-consistent trajectories;
a neural world model approximates dynamics; RL variants and
structural baselines are evaluated on the induced law-strength
frontiers.

![Refer to caption](Figure_2.png)


(b) World-model diagnostics: training vs. validation error
(top) and comparison of law penalties for ground-truth vs. predicted
surfaces (bottom), illustrating that the neural world model
introduces law-violating deviations (ghost channel).

Figure 1: Overview of the axiomatic volatility testbed and diagnostics
of the learned world model.



![Refer to caption](Figure_3.png)


(a) Baseline-regime dynamics for naive RL (PPO on P&L)
and a soft law-seeking RL variant with λ=20\lambda=20.
Top: step P&L; bottom: law penalty ℒϕ\mathcal{L}\_{\phi}.
Naive RL attains slightly higher P&L but at the cost of
moderately larger penalties.

![Refer to caption](Figure_4.png)


(b) Shock-regime dynamics (long variance ×4\times 4,
spot vol ×2\times 2) for the same policies as in
Fig. [2(a)](https://arxiv.org/html/2511.17304v1#S7.F2.sf1 "In Figure 2 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
The shock amplifies variability in both P&L and law penalties;
naive RL exhibits larger spikes in both, consistent with
ghost-arbitrage incentives.

![Refer to caption](Figure_5.png)


(c) Baseline-regime dynamics for RL and structural baselines:
naive RL, law-seeking RL, Zero-Hedge, Vol-Trend, and Random-Gaussian.
Structural baselines display smoother P&L and lower law penalties,
whereas RL trajectories are more volatile and occasionally visit
high-penalty regions.

![Refer to caption](Figure_6.png)


(d) Shock-regime dynamics for RL and structural baselines,
analogous to Fig. [2(c)](https://arxiv.org/html/2511.17304v1#S7.F2.sf3 "In Figure 2 ‣ 7.1.1 Dynamics patterns (subset of dynamics plots) ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
Shocks induce larger fluctuations in all strategies, but
structural baselines remain relatively stable compared to RL
policies.

Figure 2: Dynamics plots (baseline and shock) for RL variants and
structural baselines.
We observe more erratic, higher-penalty trajectories for RL
compared to structurally constrained baselines.

![Refer to caption](Figure_7.png)


Figure 3: Baseline vs. shock comparison for a fixed strategy
(e.g., naive RL or Vol-Trend), illustrating the change in P&L
and law penalties across regimes.
This visualization underlies the computation of the Graceful
Failure Index (GFI) discussed

#### 7.1.2 Aggregate metrics: baseline vs. shock for RL variants

Table [2](https://arxiv.org/html/2511.17304v1#S7.T2 "Table 2 ‣ 7.1.2 Aggregate metrics: baseline vs. shock for RL variants ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") summarizes the key metrics for RL
variants and structural baselines under the baseline and shock regimes,
computed from the evaluation runs described.
We report mean and standard deviation of step P&L, Sharpe ratio, mean law
penalty, Graceful Failure Index (GFI), law coverage at the
pen<0.006\mathrm{pen}<0.006 threshold, and 5% VaR/CVaR of step P&L.

| Strategy | Regime | Mean P&L | Std P&L | Sharpe | Mean Pen. | GFI | Cov<0.006 | VaR5 | CVaR5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Naive RL (PPO) | Baseline | −0.0022-0.0022 | 0.01270.0127 | −0.17-0.17 | 0.006990.00699 | 1.271.27 | 0.610.61 | −0.0228-0.0228 | −0.0261-0.0261 |
| Law-Seeking RL (PPO) | Baseline | −0.0150-0.0150 | 0.01290.0129 | −1.16-1.16 | 0.007860.00786 | 1.661.66 | 0.570.57 | −0.0361-0.0361 | −0.0394-0.0394 |
| Zero-Hedge | Baseline | 0.01910.0191 | 0.00640.0064 | 2.992.99 | 0.005500.00550 | 0.000.00 | 0.690.69 | 0.01390.0139 | 0.01390.0139 |
| Random-Gaussian | Baseline | 0.00990.0099 | 0.01070.0107 | 0.920.92 | 0.005510.00551 | 1.211.21 | 0.690.69 | −0.0088-0.0088 | −0.0161-0.0161 |
| Vol-Trend | Baseline | 0.01460.0146 | 0.00740.0074 | 1.961.96 | 0.005340.00534 | 0.000.00 | 0.690.69 | 0.00450.0045 | 0.00330.0033 |
| Naive RL (PPO) | Shock | 0.00160.0016 | 0.02280.0228 | 0.070.07 | 0.007210.00721 | 1.991.99 | 0.610.61 | −0.0369-0.0369 | −0.0415-0.0415 |
| Law-Seeking RL (PPO) | Shock | −0.0111-0.0111 | 0.02340.0234 | −0.48-0.48 | 0.008090.00809 | 2.322.32 | 0.570.57 | −0.0508-0.0508 | −0.0557-0.0557 |
| Zero-Hedge | Shock | 0.01930.0193 | 0.00670.0067 | 2.892.89 | 0.005720.00572 | 0.000.00 | 0.690.69 | 0.01390.0139 | 0.01390.0139 |
| Random-Gaussian | Shock | 0.00980.0098 | 0.01530.0153 | 0.650.65 | 0.005720.00572 | 1.991.99 | 0.690.69 | −0.0153-0.0153 | −0.0297-0.0297 |
| Vol-Trend | Shock | 0.01400.0140 | 0.01020.0102 | 1.381.38 | 0.006400.00640 | 0.380.38 | 0.650.65 | −0.0019-0.0019 | −0.0039-0.0039 |

Table 2: Aggregate metrics for RL variants and structural baselines in
baseline vs. shock regimes, using the three axes of
Sec.
Values are drawn directly from the evaluation logs: mean and standard
deviation of step P&L, Sharpe ratio, mean law penalty, Graceful Failure
Index (GFI), law coverage at pen<0.006\mathrm{pen}<0.006, and 5% VaR/CVaR.

We now turn to aggregate metrics for naive and law-seeking RL policies under
the baseline and shock regimes.
Recall that our metrics fall along three axes
(Sec. [6](https://arxiv.org/html/2511.17304v1#S6 "6 Experimental Setup ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")): profitability, law alignment, and tail
robustness.

For naive RL (PPO on pure P&L), the baseline-regime metrics (Table [2](https://arxiv.org/html/2511.17304v1#S7.T2 "Table 2 ‣ 7.1.2 Aggregate metrics: baseline vs. shock for RL variants ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) are:
mean step P&L ≈−0.0022\approx-0.0022, standard deviation ≈0.0127\approx 0.0127,
Sharpe ratio ≈−0.17\approx-0.17, mean law penalty
LawPenalty≈0.00699\mathrm{LawPenalty}\approx 0.00699, and Graceful Failure Index
GFI≈1.27\mathrm{GFI}\approx 1.27, with coverage
Cov​(pen<0.006)≈0.61\mathrm{Cov}(\mathrm{pen}<0.006)\approx 0.61.
Under shock, naive RL exhibits a slightly higher mean step P&L
(≈0.0016\approx 0.0016) due to the shifted distribution, but also larger tail risk
(VaR≈5−0.0369{}\_{5}\approx-0.0369, CVaR≈5−0.0415{}\_{5}\approx-0.0415) and increased GFI
(≈1.99\approx 1.99), indicating a non-trivial deterioration in law metrics and
tail robustness.

For a representative soft law-seeking RL variant (e.g., λ=10\lambda=10),
we observe baseline mean step P&L in the range [−0.02,−0.01][-0.02,-0.01] with similar
or slightly reduced law penalties compared to naive RL, but systematically
worse Sharpe ratios and larger GFIs (e.g., GFI≈1.66\mathrm{GFI}\approx 1.66 for one
of our main runs).
Under shock, these law-seeking policies continue to exhibit negative mean
P&L and do not achieve better VaR or CVaR than naive RL at comparable law
penalties.

##### Case-study interpretation.

Empirically, in this case study, we do not observe soft law-seeking RL
achieving strictly better GFI or law penalties at comparable P&L to naive RL.
Where law penalties are reduced, P&L and Sharpe typically decline as well.
This is consistent with the structural law-strength trade-off of theorem, which predicts that increasing
λ\lambda beyond a threshold must worsen expected P&L by at least a
quantifiable amount if law penalties are to be meaningfully reduced.
We emphasize that these conclusions are based on single- or few-seed runs and
should be interpreted as case-study evidence rather than formal statistical
claims.

### 7.2 RQ2 – RL vs. structural baselines under shocks

RQ2 compares RL policies to structural baselines (Zero-Hedge, Vol-Trend,
Random-Gaussian) on the risk–law trade-off, especially under shocks.

#### 7.2.1 Baseline vs. shock metrics

To unpack the frontier picture, we summarize the key baseline vs. shock
metrics that underlie Figures [4(a)](https://arxiv.org/html/2511.17304v1#S7.F4.sf1 "In Figure 4 ‣ 7.2.1 Baseline vs. shock metrics ‣ 7.2 RQ2 – RL vs. structural baselines under shocks ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[4(c)](https://arxiv.org/html/2511.17304v1#S7.F4.sf3 "In Figure 4 ‣ 7.2.1 Baseline vs. shock metrics ‣ 7.2 RQ2 – RL vs. structural baselines under shocks ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
These are already included in Table [2](https://arxiv.org/html/2511.17304v1#S7.T2 "Table 2 ‣ 7.1.2 Aggregate metrics: baseline vs. shock for RL variants ‣ 7.1 RQ1 – Do law penalties help naive RL? ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), but we
highlight the structural baselines here.

In the baseline regime, Zero-Hedge achieves mean step P&L
≈0.0191\approx 0.0191 with standard deviation ≈0.0064\approx 0.0064, Sharpe
≈2.99\approx 2.99, mean law penalty ≈0.0055\approx 0.0055, and essentially zero GFI
(our normalization sets GFI=0\mathrm{GFI}=0 for this reference point).
Vol-Trend attains mean step P&L ≈0.0146\approx 0.0146, Sharpe ≈1.96\approx 1.96,
and similar law penalties (≈0.0053\approx 0.0053), again with negligible GFI.
Random-Gaussian yields mean step P&L around 0.010.01, moderate volatility, and
moderate law penalties, serving as a noisy exploration proxy.

Under shock, Zero-Hedge remains remarkably stable:
mean step P&L ≈0.0193\approx 0.0193, Sharpe ≈2.89\approx 2.89, and GFI still near
zero, reflecting almost unchanged law metrics between regimes.
Vol-Trend experiences a modest decline in Sharpe (from ≈1.96\approx 1.96 to
≈1.38\approx 1.38) and a slight increase in law penalties, but its GFI remains
small.
Random-Gaussian shows a more noticeable degradation in tail risk, but its GFI
is still lower than those of RL policies.

By contrast, naive and law-seeking RL variants exhibit negative or near-zero
mean P&L and substantially larger GFIs, particularly under shock.
This suggests that, in our setting, high-capacity unconstrained RL does not
outperform low-capacity but structurally law-aligned strategies when evaluated
on the combined axes of profitability, law alignment, and graceful failure.

![Refer to caption](Figure_8.png)


(a) GFI vs. mean law penalty.
Zero-Hedge and Vol-Trend lie near the empirical Pareto frontier with low
GFI and low penalties; RL variants occupy interior points with higher GFI.

![Refer to caption](Figure_9.png)


(b) VaR5 vs. mean law penalty.
Structural baselines dominate RL variants in tail robustness at comparable
penalty levels.

![Refer to caption](Figure_10.png)


(c) CVaR5 vs. mean law penalty.
As with VaR5, structural baselines trace the outer frontier, and RL
variants remain strictly dominated.

Figure 4: Law-strength frontiers for GFI, VaR5, and CVaR5 vs. mean
law penalty, corresponding to Figure\_8.png–Figure\_10.png.
Structural baselines (Zero-Hedge, Vol-Trend) form the empirical Pareto
frontier, while RL variants lie in the interior.

#### 7.2.2 Tail robustness and graceful failure

In our experiments, RL variants—both naive and law-seeking—exhibit
pronounced degradation in tail metrics under shock.
For example, a naive RL policy may transition from
VaR5≈−0.023\mathrm{VaR}\_{5}\approx-0.023, CVaR5≈−0.026\mathrm{CVaR}\_{5}\approx-0.026 in the
baseline regime to VaR5≈−0.037\mathrm{VaR}\_{5}\approx-0.037,
CVaR5≈−0.042\mathrm{CVaR}\_{5}\approx-0.042 under shock, and its GFI correspondingly
increases by roughly +0.7+0.7.
Law-seeking RL policies show similar or worse shifts in tail risk.

Structural baselines, in contrast, form an empirical frontier in the
tail-robustness–law space: Zero-Hedge and Vol-Trend maintain relatively
favorable VaR and CVaR at given law-penalty levels, and their positions change
only mildly under shock.
Random-Gaussian occupies an intermediate region, with greater sensitivity to
shock but still performing better on tail metrics than many RL variants at
similar law penalties.

##### Case-study interpretation.

In this volatility testbed, our case-study observations suggest that
structural baselines exhibit more graceful failure under shocks than
unconstrained RL policies, both in terms of GFI and tail risk.

### 7.3 Law-strength frontiers and Pareto dominance

We now directly address RQ3 by examining law-strength frontiers and diagnostic
plots that link back to the no-free-lunch story of Theorem [3](https://arxiv.org/html/2511.17304v1#Thmtheorem3 "Theorem 3 (No-free-lunch for unconstrained law-seeking RL). ‣ Proof sketch. ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

#### 7.3.1 Frontier plots: GFI vs. law penalty

Figure [4(a)](https://arxiv.org/html/2511.17304v1#S7.F4.sf1 "In Figure 4 ‣ 7.2.1 Baseline vs. shock metrics ‣ 7.2 RQ2 – RL vs. structural baselines under shocks ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") can be viewed as a law-strength
frontier: each RL variant (naive, soft law-seeking with
λ∈{5,10,20,40}\lambda\in\{5,10,20,40\}, selection-only), together with structural
baselines, is represented as a point in the plane of (mean law penalty,
GFI).
By varying λ\lambda and including different strategy classes, we trace out
a family of frontiers.

To make the connection with the underlying numerical results explicit,
Table [3](https://arxiv.org/html/2511.17304v1#S7.T3 "Table 3 ‣ 7.3.1 Frontier plots: GFI vs. law penalty ‣ 7.3 Law-strength frontiers and Pareto dominance ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") lists the baseline-regime metrics for the
λ\lambda-sweep (including selection-only) and structural baselines.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy / λ\lambda | Mean P&L | Std P&L | Sharpe | Mean Pen. | GFI | Cov<0.006 | VaR5 | CVaR5 |
| Naive RL (λ=0\lambda=0) | −0.0022-0.0022 | 0.01270.0127 | −0.17-0.17 | 0.006990.00699 | 1.271.27 | 0.610.61 | −0.0228-0.0228 | −0.0261-0.0261 |
| Soft RL (λ=5\lambda=5) | −0.0202-0.0202 | 0.01200.0120 | −1.68-1.68 | 0.006470.00647 | 2.072.07 | 0.630.63 | −0.0399-0.0399 | −0.0429-0.0429 |
| Soft RL (λ=10\lambda=10) | −0.0175-0.0175 | 0.01230.0123 | −1.42-1.42 | 0.003710.00371 | 2.812.81 | 0.800.80 | −0.0354-0.0354 | −0.0387-0.0387 |
| Soft RL (λ=20\lambda=20) | −0.0204-0.0204 | 0.01310.0131 | −1.56-1.56 | 0.003960.00396 | 3.073.07 | 0.780.78 | −0.0414-0.0414 | −0.0454-0.0454 |
| Soft RL (λ=40\lambda=40) | −0.0092-0.0092 | 0.00540.0054 | −1.71-1.71 | 0.004740.00474 | 0.840.84 | 0.730.73 | −0.0134-0.0134 | −0.0134-0.0134 |
| Selection-only RL | −0.0223-0.0223 | 0.01390.0139 | −1.60-1.60 | 0.007920.00792 | 2.042.04 | 0.570.57 | −0.0448-0.0448 | −0.0489-0.0489 |
| Zero-Hedge | 0.01910.0191 | 0.00640.0064 | 2.992.99 | 0.005500.00550 | 0.000.00 | 0.690.69 | 0.01390.0139 | 0.01390.0139 |
| Random-Gaussian | 0.00990.0099 | 0.01070.0107 | 0.920.92 | 0.005510.00551 | 1.211.21 | 0.690.69 | −0.0088-0.0088 | −0.0161-0.0161 |
| Vol-Trend | 0.01460.0146 | 0.00740.0074 | 1.961.96 | 0.005340.00534 | 0.000.00 | 0.690.69 | 0.00450.0045 | 0.00330.0033 |

Table 3: Baseline-regime law-strength frontier metrics for RL variants
(naive, soft law-seeking with λ∈{5,10,20,40}\lambda\in\{5,10,20,40\}, and
selection-only) and structural baselines (Zero-Hedge, Random-Gaussian,
Vol-Trend).
All values are taken from the Frontier (Baseline) block of the
evaluation logs.

##### Headline conclusion.

In our experiments, for all tested λ\lambda, no RL point lies on the
empirical Pareto frontier once Zero-Hedge and Vol-Trend are included.

To make this more concrete, consider policies whose mean law penalty lies in
the band [0.0053,0.0057][0.0053,0.0057].
Within this band:

1. 1.

   Zero-Hedge attains Sharpe ≈3.0\approx 3.0 and GFI ≈0\approx 0.
2. 2.

   The best RL variant in the same band has Sharpe <0<0 and GFI >1.5>1.5.

We emphasize that we compare within such penalty bands rather than by
cherry-picking isolated points; similar dominance patterns hold across other
bands where both RL and baselines are present.

#### 7.3.2 Frontier plots: VaR/CVaR vs. law penalty

Figures [4(b)](https://arxiv.org/html/2511.17304v1#S7.F4.sf2 "In Figure 4 ‣ 7.2.1 Baseline vs. shock metrics ‣ 7.2 RQ2 – RL vs. structural baselines under shocks ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and [4(c)](https://arxiv.org/html/2511.17304v1#S7.F4.sf3 "In Figure 4 ‣ 7.2.1 Baseline vs. shock metrics ‣ 7.2 RQ2 – RL vs. structural baselines under shocks ‣ 7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
provide analogous frontiers in the
( mean law penalty, VaR5/CVaR5 ) planes.
Here too, structural baselines define the outer frontier:
for a given law penalty, they offer strictly better or comparable tail
robustness, while RL variants occupy interior regions.

Taken together, the GFI and tail-risk frontiers support the qualitative
implication: soft-penalized RL
cannot simultaneously match structural baselines on law metrics and P&L in
this axiomatic pipeline, and empirically appears strictly dominated.

#### 7.3.3 Diagnostic plots: ruling out trivial artefacts

Finally, we examine diagnostic plots to rule out trivial explanations such as
isolated outliers or a few pathological episodes.

![Refer to caption](Figure_11.png)


(a) Diagnostic scatter plot of step P&L vs. law penalty for RL
policies and structural baselines, aggregating across episodes and
regimes.
RL points form dense clusters in moderate-to-high penalty regions,
whereas structural baselines remain near low-penalty, moderate-P&L
regions.

![Refer to caption](Figure_12.png)


(b) Histogram of law penalties for RL policies (naive and
law-seeking).
The distribution exhibits a noticeable heavy tail, indicating that RL
spends substantial time in high-penalty regions of the law space.

![Refer to caption](Figure_13.png)


(c) Histogram of law penalties for structural baselines
(Zero-Hedge, Vol-Trend, Random-Gaussian).
Baselines concentrate their mass near low penalty, consistent with their
structural law alignment and low GFI.

Figure 5: Diagnostic plots
for RL policies and structural baselines.
These plots indicate that RL systematically occupies higher-penalty
regions than structurally constrained strategies.

##### Case-study interpretation.

These diagnostic plots reinforce the frontier analysis: in this axiomatic
volatility testbed, unconstrained RL policies systematically exploit ghost
arbitrage channels opened by the world model, leading to higher law penalties
and less graceful failure than structurally constrained baselines.
This empirical picture is consistent with the no-free-lunch theorem and supports our overarching claim that reward shaping
with soft penalties is insufficient for law alignment without structural
constraints or projection.

## 8 No-Free-Lunch for Law-Seeking RL

In this section we formalize the informal story, and show that under explicit assumptions on the structural class 𝒮\mathcal{S}, the unconstrained policy class Π\Pi, and the volatility world model, *law-seeking RL has no free lunch*. In particular, any unconstrained RL policy that strictly improves on the PnL of a law-consistent structural benchmark must incur strictly worse law metrics and/or Graceful Failure Index (GFI). We then relate this result to recent work on Reinforcement Learning with Verifiable Rewards (RLVR) and law-aligned reasoning, before briefly discussing limitations and future axes.

### 8.1 Assumptions and theorem statement

We first make the structural assumptions that connect the abstract decomposition of Section to the volatility world model of Section [3](https://arxiv.org/html/2511.17304v1#S3 "3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and the RL variants. For clarity we work at the level of *stationary policies* and their induced trajectory distributions.

###### Definition 10 (Performance and law-metric vector).

For any stationary policy π∈Π\pi\in\Pi interacting with the volatility world model, denote by

|  |  |  |
| --- | --- | --- |
|  | J​(π):=(𝔼​[R​(π)],−𝔼​[ℒϕ​(π)],−GFI​(π))∈ℝ3J(\pi):=\Big(\mathbb{E}[R(\pi)],-\mathbb{E}[\mathcal{L}\_{\phi}(\pi)],-\mathrm{GFI}(\pi)\Big)\in\mathbb{R}^{3} |  |

its *performance–law vector*, where:

1. 1.

   𝔼​[R​(π)]\mathbb{E}[R(\pi)] is the expected cumulative (or average) PnL,
2. 2.

   𝔼​[ℒϕ​(π)]\mathbb{E}[\mathcal{L}\_{\phi}(\pi)] is the expected law-penalty functional, and
3. 3.

   GFI​(π)\mathrm{GFI}(\pi) is the Graceful Failure Index.

We write J​(π)≽J​(π′)J(\pi)\succcurlyeq J(\pi^{\prime}) if each component is at least as good (higher PnL, lower law penalty, lower GFI), and J​(π)≻J​(π′)J(\pi)\succ J(\pi^{\prime}) if the inequality is strict in at least one coordinate.

We now formalize the role of the structural baseline class 𝒮\mathcal{S} introduced, which includes Zero-Hedge and Vol-Trend as concrete instances.

###### Assumption 3 (Structural class and world-model properties).

We assume:

1. 1.

   Law-consistent structural class. The structural class 𝒮⊂Π\mathcal{S}\subset\Pi is non-empty, convex, and *law-consistent* in the sense that for all s∈𝒮s\in\mathcal{S},

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[ℒϕ​(s)]≤Lmax𝒮andGFI​(s)≤GFImax𝒮,\mathbb{E}[\mathcal{L}\_{\phi}(s)]\leq L\_{\max}^{\mathcal{S}}\quad\text{and}\quad\mathrm{GFI}(s)\leq\mathrm{GFI}\_{\max}^{\mathcal{S}}, |  |

   for some finite constants Lmax𝒮,GFImax𝒮L\_{\max}^{\mathcal{S}},\mathrm{GFI}\_{\max}^{\mathcal{S}}.
   Moreover, there exists s⋆∈𝒮s^{\star}\in\mathcal{S} such that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[R​(s⋆)]≥supπ∈Π:𝔼​[ℒϕ​(π)]=0𝔼​[R​(π)]−ε𝒮,\mathbb{E}[R(s^{\star})]\geq\sup\_{\pi\in\Pi\;:\;\mathbb{E}[\mathcal{L}\_{\phi}(\pi)]=0}\mathbb{E}[R(\pi)]-\varepsilon\_{\mathcal{S}}, |  |

   i.e., 𝒮\mathcal{S} contains a near-optimal on-manifold hedge.
2. 2.

   Rich unconstrained class. The unconstrained policy class Π\Pi is rich enough to strictly contain 𝒮\mathcal{S} and to reach off-manifold regions: for any δ>0\delta>0 there exists π∈Π\pi\in\Pi such that 𝔼​[ℒϕ​(π)]≥δ\mathbb{E}[\mathcal{L}\_{\phi}(\pi)]\geq\delta.
3. 3.

   World-model ghost coupling. Under the volatility world model, the Goodhart decomposition applies, and there exist constants α>0\alpha>0 and β≥0\beta\geq 0 such that for any policy π∈Π\pi\in\Pi,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼​[r⟂​(π)]≥α​𝔼​[ℒϕ​(π)]−β,\mathbb{E}[r^{\perp}(\pi)]\;\geq\;\alpha\,\mathbb{E}[\mathcal{L}\_{\phi}(\pi)]-\beta, |  | (27) |

   where r⟂r^{\perp} is the off-manifold ghost component of reward from Definition [5](https://arxiv.org/html/2511.17304v1#Thmdefinition5 "Definition 5 (Ghost arbitrage). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). In particular, 𝔼​[r⟂​(π)]\mathbb{E}[r^{\perp}(\pi)] cannot be positive without incurring non-trivial law penalties on average.
4. 4.

   Shock structure. The shock regime modifies the underlying law-consistent generator(long-var ×4\times 4, spot vol ×2\times 2) while keeping the world model and policies fixed. The resulting change in law penalties enters GFI linearly as defined in Section.

Assumption [3](https://arxiv.org/html/2511.17304v1#Thmassumption3 "Assumption 3 (Structural class and world-model properties). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")(A1) formalizes the idea that Zero-Hedge and Vol-Trend are representatives of a small, law-aligned, but near-optimal structural class 𝒮\mathcal{S}, while (A2)–(A3) encode the existence of a non-trivial ghost channel in the world model that couples off-manifold deviations to reward. Assumption [3](https://arxiv.org/html/2511.17304v1#Thmassumption3 "Assumption 3 (Structural class and world-model properties). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")(A4) connects law penalties under shocks to the GFI used throughout our empirical analysis.

We next introduce a simple Pareto notion relative to 𝒮\mathcal{S}.

###### Definition 11 (Structural Pareto dominance).

We say that a policy π∈Π\pi\in\Pi *structurally dominates* the class 𝒮\mathcal{S} if

|  |  |  |
| --- | --- | --- |
|  | J​(π)≽J​(s)for all ​s∈𝒮,J(\pi)\succcurlyeq J(s)\quad\text{for all }s\in\mathcal{S}, |  |

and J​(π)≻J​(s¯)J(\pi)\succ J(\bar{s}) for at least one s¯∈𝒮\bar{s}\in\mathcal{S}. In other words, π\pi is at least as good as every s∈𝒮s\in\mathcal{S} on PnL, law penalties, and GFI, and strictly better on at least one coordinate.

Our main no-free-lunch theorem shows that such structural dominance is impossible under Assumption [3](https://arxiv.org/html/2511.17304v1#Thmassumption3 "Assumption 3 (Structural class and world-model properties). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

###### Lemma 3 (Ghost improvement requires law degradation).

Under Assumption [3](https://arxiv.org/html/2511.17304v1#Thmassumption3 "Assumption 3 (Structural class and world-model properties). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), for any policy π∈Π\pi\in\Pi satisfying
𝔼​[r⟂​(π)]>0\mathbb{E}[r^{\perp}(\pi)]>0,
we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ℒϕ​(π)]≥βαandGFI​(π)≥GFImax𝒮+ΔGFI,\mathbb{E}[\mathcal{L}\_{\phi}(\pi)]\;\geq\;\frac{\beta}{\alpha}\quad\text{and}\quad\mathrm{GFI}(\pi)\;\geq\;\mathrm{GFI}\_{\max}^{\mathcal{S}}+\Delta\_{\mathrm{GFI}}, |  |

for some ΔGFI>0\Delta\_{\mathrm{GFI}}>0 that depends on the shock structure in (A4). In particular, any policy that gains positive expected ghost arbitrage must incur strictly higher law penalties and GFI than the best structural baselines.

##### Proof sketch.

The inequality ([27](https://arxiv.org/html/2511.17304v1#S8.E27 "In item 3 ‣ Assumption 3 (Structural class and world-model properties). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) implies
𝔼​[ℒϕ​(π)]≥(𝔼​[r⟂​(π)]+β)/α\mathbb{E}[\mathcal{L}\_{\phi}(\pi)]\geq(\mathbb{E}[r^{\perp}(\pi)]+\beta)/\alpha,
so 𝔼​[r⟂​(π)]>0\mathbb{E}[r^{\perp}(\pi)]>0 enforces a positive lower bound on 𝔼​[ℒϕ​(π)]\mathbb{E}[\mathcal{L}\_{\phi}(\pi)]. The shock structure in (A4) implies that, for fixed policy and world model, GFI increases monotonically with the shocked-minus-baseline law-penalty difference. Since 𝒮\mathcal{S} is law-consistent and near-on-manifold by (A1), any policy with strictly larger average law penalty than 𝒮\mathcal{S} must also exhibit strictly larger GFI. A detailed construction of ΔGFI\Delta\_{\mathrm{GFI}} and the monotonicity argument is given in Appendix E. ∎

We are now ready to state our flagship no-free-lunch theorem.

###### Theorem 3 (No-free-lunch for unconstrained law-seeking RL).

Suppose Assumption [3](https://arxiv.org/html/2511.17304v1#Thmassumption3 "Assumption 3 (Structural class and world-model properties). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") holds. Let πRL∈Π\pi^{\text{RL}}\in\Pi be any limit point of an unconstrained law-seeking RL procedure (naive, soft-penalized, or selection-only) trained on the volatility world model. If

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[R​(πRL)]>sups∈𝒮𝔼​[R​(s)]−ε𝒮,\mathbb{E}[R(\pi^{\text{RL}})]\;>\;\sup\_{s\in\mathcal{S}}\mathbb{E}[R(s)]-\varepsilon\_{\mathcal{S}}, |  |

then πRL\pi^{\text{RL}} cannot structurally dominate 𝒮\mathcal{S}: there must exist s∈𝒮s\in\mathcal{S} for which

|  |  |  |
| --- | --- | --- |
|  | J​(πRL)⋡J​(s).J(\pi^{\text{RL}})\not\succcurlyeq J(s). |  |

Equivalently, any unconstrained law-seeking RL policy that strictly improves (up to ε𝒮\varepsilon\_{\mathcal{S}}) upon the PnL of 𝒮\mathcal{S} must worsen at least one of the law metrics (expected law penalty or GFI).

##### Proof sketch.

We decompose reward into on-manifold and ghost components as in Section, writing

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[R​(π)]=𝔼​[Rℳ​(π)]+𝔼​[r⟂​(π)].\mathbb{E}[R(\pi)]\;=\;\mathbb{E}[R^{\mathcal{M}}(\pi)]+\mathbb{E}[r^{\perp}(\pi)]. |  |

By (A1), the class 𝒮\mathcal{S} contains a policy s⋆s^{\star} that is ε𝒮\varepsilon\_{\mathcal{S}}-optimal among all law-consistent policies, so any policy π\pi satisfying 𝔼​[R​(π)]>𝔼​[R​(s⋆)]\mathbb{E}[R(\pi)]>\mathbb{E}[R(s^{\star})] must achieve strictly larger expected ghost component:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[r⟂​(π)]>𝔼​[r⟂​(s⋆)].\mathbb{E}[r^{\perp}(\pi)]\;>\;\mathbb{E}[r^{\perp}(s^{\star})]. |  |

Since 𝒮\mathcal{S} is law-consistent, 𝔼​[r⟂​(s⋆)]\mathbb{E}[r^{\perp}(s^{\star})] is bounded above by zero (or a small constant absorbed into ε𝒮\varepsilon\_{\mathcal{S}}), so π\pi must satisfy 𝔼​[r⟂​(π)]>0\mathbb{E}[r^{\perp}(\pi)]>0. Lemma [3](https://arxiv.org/html/2511.17304v1#Thmlemma3 "Lemma 3 (Ghost improvement requires law degradation). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") then implies that π\pi necessarily incurs strictly larger average law penalties and GFI than the best elements of 𝒮\mathcal{S}. Hence J​(π)J(\pi) cannot dominate J​(s)J(s) for all s∈𝒮s\in\mathcal{S}.

Applying this argument to πRL\pi^{\text{RL}} shows that any unconstrained law-seeking RL limit point that improves PnL relative to 𝒮\mathcal{S} must pay for this improvement with worse law metrics, ruling out structural dominance. A fully rigorous proof, including technical conditions on convergence of the RL training dynamics and integrability of the law metrics, is provided in Appendix E. ∎

Theorem [3](https://arxiv.org/html/2511.17304v1#Thmtheorem3 "Theorem 3 (No-free-lunch for unconstrained law-seeking RL). ‣ Proof sketch. ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") provides a theoretical counterpart to the empirical story in Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). The structural baselines (Zero-Hedge and Vol-Trend) inhabit a law-consistent region of the law-strength frontier, while RL policies that attempt to improve PnL through the ghost channel are forced, by Lemma [3](https://arxiv.org/html/2511.17304v1#Thmlemma3 "Lemma 3 (Ghost improvement requires law degradation). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), to move outward along the law-penalty and GFI axes. This is precisely the Pareto-dominance pattern we observed in Figures.

### 8.2 RLVR and law-aligned reasoning: analogies and caveats

Recent work on Reinforcement Learning with Verifiable Rewards (RLVR) has shown that, for mathematical reasoning and related tasks, combining verifiable outcome signals with process-level feedback can significantly improve reliability over standard preference-based RLHF. In these settings, a *verifiable checker* evaluates candidate solutions or intermediate reasoning steps, producing a structured reward signal that is, at least in principle, resistant to some forms of reward hacking.

Our axiomatic volatility setting can be interpreted as a stylized analogue of RLVR:

1. 1.

   The no-arbitrage axioms and the law manifold ℳvol\mathcal{M}^{\text{vol}} play the role of a verifiable checker that deterministically determines whether a surface is admissible and how badly it violates the axioms.
2. 2.

   The law-penalty functional ℒϕ\mathcal{L}\_{\phi} and GFI are analogous to structured correctness scores in RLVR, quantifying how well a policy respects axioms under both baseline and shocked environments.
3. 3.

   Ghost arbitrage r⟂r^{\perp} corresponds to reward obtained in regions where the checker is informative but the learning dynamics exploit systematic modelling errors, leading to misalignment between high reward and true law-consistent performance.

From this perspective, Theorem [3](https://arxiv.org/html/2511.17304v1#Thmtheorem3 "Theorem 3 (No-free-lunch for unconstrained law-seeking RL). ‣ Proof sketch. ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and our empirical results highlight a concrete failure mode for RL with verifiable penalties: even when the checker is mathematically correct on the generator support, the combination of function approximation, world-model error, and broad policy classes can create exploitable ghost channels, through which RL can improve the measured reward while degrading law alignment. This resonates with observations in RLVR that combining process and outcome rewards requires careful design to avoid unintended incentives and reward hacking.

At the same time, our scope is deliberately modest. We do *not* claim a general impossibility result for RLVR. Rather, our volatility case illustrates one concrete setting in which verifiable penalties and axiomatic structure, by themselves, are insufficient to guarantee law alignment in the presence of model misspecification and unconstrained policy classes. In particular, our findings suggest that:

1. 1.

   Structural restrictions on policies (e.g., restricting Π\Pi to a parametric hedge family) and
2. 2.

   Hard projection or constrained training of world models onto the law manifold

may be necessary complements to verifiable law penalties, if one wishes to avoid ghost arbitrage in similar scientific AI testbeds.

### 8.3 Limitations and future axes

We briefly summarize the main limitations of our no-free-lunch analysis and point to concrete extensions.

First, we do not train *structurally constrained* RL agents whose policy class coincides with the structural family 𝒮\mathcal{S} (e.g., Vol-Trend parametrizations). As a result, our empirical comparison does not fully disentangle the contribution of the learning algorithm from that of the function class: it remains an open question whether carefully designed RL within 𝒮\mathcal{S} could match or slightly improve upon hand-crafted baselines without opening a ghost channel.

Second, our world model is trained without hard projection onto ℳvol\mathcal{M}^{\text{vol}}, and our assumptions on the ghost coupling ([27](https://arxiv.org/html/2511.17304v1#S8.E27 "In item 3 ‣ Assumption 3 (Structural class and world-model properties). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) are only partially validated empirically. A natural next step is to compare unconstrained world models with hard-constrained or projected variants, and to evaluate whether such models reduce or eliminate the ghost arbitrage term r⟂r^{\perp} in practice.

Despite these limitations, Theorem [3](https://arxiv.org/html/2511.17304v1#Thmtheorem3 "Theorem 3 (No-free-lunch for unconstrained law-seeking RL). ‣ Proof sketch. ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), Lemma [3](https://arxiv.org/html/2511.17304v1#Thmlemma3 "Lemma 3 (Ghost improvement requires law degradation). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), and the empirical Pareto patterns in Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") together provide a coherent no-free-lunch narrative: in our volatility law-manifold testbed, high-capacity unconstrained law-seeking RL cannot simultaneously match the PnL and law-alignment performance of simple structural baselines without collapsing back into their structural class.

Appendix pointer. Full proofs of Lemma [3](https://arxiv.org/html/2511.17304v1#Thmlemma3 "Lemma 3 (Ghost improvement requires law degradation). ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and Theorem [3](https://arxiv.org/html/2511.17304v1#Thmtheorem3 "Theorem 3 (No-free-lunch for unconstrained law-seeking RL). ‣ Proof sketch. ‣ 8.1 Assumptions and theorem statement ‣ 8 No-Free-Lunch for Law-Seeking RL ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), together with technical assumptions on RL convergence and integrability, are provided in Appendix E.

## 9 Discussion and Conclusion

In this section we summarize our findings as a *negative but constructive* scientific result, formulate concrete design recommendations and testable predictions, and highlight the broader transferability of our axiomatic evaluation template beyond volatility.

### 9.1 Negative but constructive result

Our main empirical and theoretical message is deliberately two-sided.

##### Negative.

In our volatility law-manifold testbed, *unconstrained law-seeking RL fails to outperform simple structural baselines* (Zero-Hedge and Vol-Trend) on any of the three main axes—profitability (mean PnL / Sharpe), law alignment (mean and tail law penalties, law coverage, GFI), and tail robustness (VaR5, CVaR5):

1. 1.

   Naive PPO on the world model attains mean step PnL around −0.0022-0.0022 in the baseline regime with GFI ≈1.27\approx 1.27, while law-seeking PPO variants with λ∈{5,10,20,40}\lambda\in\{5,10,20,40\} often yield *more negative* mean PnL (e.g., −0.0150-0.0150) and higher GFI (≈1.66\approx 1.66), despite explicit law penalties.
2. 2.

   In contrast, structural baselines sit on or near the empirical Pareto frontier: Zero-Hedge achieves mean step PnL ≈0.0191\approx 0.0191 (baseline) and ≈0.0193\approx 0.0193 (shock) with GFI essentially zero and modest law penalties, while Vol-Trend achieves PnL ≈0.0146→0.0140\approx 0.0146\to 0.0140 with relatively low law penalties and small GFI.
3. 3.

   Law-strength frontier plots (GFI vs law penalty, VaR/CVaR vs law penalty) show that, once these structural baselines are included, no RL variant occupies a Pareto-optimal point: all RL points lie *strictly inside* the frontier formed by Zero-Hedge and Vol-Trend.

##### Constructive.

At the same time, the paper is constructive in several respects:

1. 1.

   We introduce a general *axiomatic evaluation pipeline* based on law manifolds, metric-based law-penalty functionals, and a structured Goodhart decomposition r=rℳ+r⟂r=r^{\mathcal{M}}+r^{\perp}.
2. 2.

   We define a domain-agnostic *Graceful Failure Index* (GFI) and *law-strength frontiers* that jointly organize profitability, law alignment, and tail robustness under explicit shocks.
3. 3.

   We prove structural results (Theorem 4.1, Theorem 4.3 with Corollary 4.4, and Theorem 8.1) that formalize ghost-arbitrage incentives and no-free-lunch trade-offs for unconstrained law-seeking RL, and we show empirically that the observed frontiers are consistent with these results.

##### One-sentence answers to RQ1–RQ3.

We conclude this subsection with concise answers to the research questions posed in Section [1](https://arxiv.org/html/2511.17304v1#S1 "1 Introduction ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

1. 1.

   RQ1 (Do law penalties help naive RL?). In our volatility world-model case study, soft law penalties and selection-only model choice *do not* yield policies with strictly better law metrics (GFI, law penalties) at comparable PnL to naive PPO; instead they typically worsen PnL while only modestly improving law alignment, consistent with the structural trade-off in Theorem 4.3.
2. 2.

   RQ2 (RL vs structural baselines under shocks). Structural baselines (Zero-Hedge, Vol-Trend) form an empirical Pareto frontier in PnL–law–tail space that is robust to shocks, while all tested RL variants (naive, law-seeking, selection-only) remain strictly dominated on at least one axis, in line with the ghost-arbitrage incentive picture of Theorem 4.1.
3. 3.

   RQ3 (When does law-seeking RL have no free lunch?). Under explicit assumptions on the structural class 𝒮\mathcal{S}, the policy class Π\Pi, and the world model’s ghost coupling, Theorem 8.1 shows that any unconstrained law-seeking RL policy that improves PnL over 𝒮\mathcal{S} must worsen law metrics and/or GFI, yielding a no-free-lunch result that matches the empirical law-strength frontiers of Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

### 9.2 Design recommendations and testable predictions

Our negative result is intended to be *useful*: it points to concrete directions where future work can intervene. We highlight three design recommendations, each accompanied by an observable criterion that makes the recommendation empirically testable.

##### Hard constraints and projection.

Rather than relying solely on soft penalties in the reward, future systems should enforce axioms via *hard constraints and projection* in both the world model and policy updates.

1. 1.

   For the world model, this means training under a projected loss, where each predicted surface is mapped to Πℳ​(w)\Pi\_{\mathcal{M}}(w) in total-variance space before computing reconstruction error; this would directly suppress ghost channels at the model level.
2. 2.

   For policies, this suggests incorporating projections onto ℳvol\mathcal{M}^{\text{vol}} in policy evaluation, or imposing hard constraints on action maps so that implied surfaces remain on or near the manifold by construction.

*Observable criterion:* Success of this approach would manifest as *uniformly lower GFI*—i.e., smaller increases in law penalties and law-violation frequency under shocks—without a significant loss in Sharpe or mean PnL relative to our current frontier curves. In law-strength plots, projected models should move points *downward* (lower GFI) while leaving the horizontal PnL coordinate nearly unchanged.

##### Structured policy classes.

Our results consistently show that simple structural strategies (Zero-Hedge, Vol-Trend) dominate unconstrained RL. This suggests a design where policy classes are themselves *structured*, mirroring the structural class 𝒮\mathcal{S} defined in Section.

1. 1.

   Concretely, policy networks could be replaced or augmented by parametric families of volatility hedges (e.g., Vol-Trend with a small number of interpretable parameters) that are guaranteed to preserve certain law properties.
2. 2.

   RL would then be used to fit parameters within this structural family, rather than to search over arbitrary high-capacity function approximators that can freely exploit ghost arbitrage.

*Observable criterion:* If successful, structural baselines like Zero-Hedge and Vol-Trend would lie *inside* the policy class Π\Pi, and RL training would *recover* or slightly improve upon them without moving off-manifold. In our metrics, this would appear as new RL points coinciding with or marginally improving the structural frontier, rather than sitting strictly inside it.

##### Joint alignment of world model and policy.

Finally, our Goodhart decomposition r=rℳ+r⟂r=r^{\mathcal{M}}+r^{\perp} makes clear that misalignment can arise from both the world model and the policy. A more promising avenue is therefore to jointly regularize both components.

1. 1.

   World models can be trained with explicit law penalties, projections, or multi-task objectives that penalize violations of no-arbitrage inequalities alongside prediction error.
2. 2.

   Policies can be trained with law-aware objectives that down-weight or explicitly penalize trajectories whose rewards are dominated by the ghost component r⟂r^{\perp}.

*Observable criterion:* We would expect a *measurable reduction in the empirical contribution of r⟂r^{\perp}* in the Goodhart decomposition: for policies trained under joint alignment, the estimated 𝔼​[r⟂]\mathbb{E}[r^{\perp}] should shrink relative to 𝔼​[rℳ]\mathbb{E}[r^{\mathcal{M}}], and scatter/diagnostic plots analogous to Figures should show reduced mass in high-penalty, high-ghost regions.

### 9.3 Transferable template and broader impact

Although our case study is anchored in implied volatility surfaces, the conceptual tools we introduce are intentionally *template-like* and readily transferable to other axiom-constrained domains.

##### Template tools.

Three components are particularly reusable:

1. 1.

   Axiomatic law manifolds. Any system with known structural constraints—e.g., monotone yield curves, convex credit term structures, physics-constrained PDE solutions—can be recast as a law manifold ℳ={y:A​(y)≤0}\mathcal{M}=\{y:A(y)\leq 0\} in a discretized coordinate system.
2. 2.

   Law-penalty functionals and GFI. Given ℳ\mathcal{M}, one can define metric-based law penalties ℒϕ​(y)\mathcal{L}\_{\phi}(y) and a domain-agnostic Graceful Failure Index that measures the degradation of law metrics under shocks or distribution shifts.
3. 3.

   Law-strength frontiers and Goodhart decomposition. For any combination of world model and RL or control algorithm, one can plot law-strength frontiers and perform a Goodhart decomposition to separate on-manifold performance from ghost exploitation.

##### Yield-curve example.

As a concrete non-financial (in the sense of non-equity-volatility) instantiation, consider discretized yield curves. Here yy is a vector of yields at different maturities, ℳyc\mathcal{M}^{\text{yc}} encodes monotonicity and convexity constraints (no negative forward rates, no butterfly arbitrage across maturities), and ℒϕ\mathcal{L}\_{\phi} penalizes violations of these inequalities. A synthetic generator could produce law-consistent yield trajectories, a world model could approximate their dynamics, and RL agents could be tasked with hedging interest-rate exposures. Our pipeline would then apply verbatim: law-strength frontiers would compare RL-based hedges to structural curve strategies, GFI would quantify robustness to rate shocks, and a Goodhart decomposition would reveal whether RL exploits law-violating yield shapes induced by model error.

Beyond yield curves, similar constructions are natural for:

1. 1.

   credit term structures constrained by monotonicity and positivity,
2. 2.

   physical fields governed by PDEs (with residuals forming the law penalty),
3. 3.

   and other Scientific AI settings where axioms or conservation laws define an admissible set of states.

##### Broader impact.

Our main contribution is thus not a particular trading system, but a *reusable template* for stress-testing Scientific AI systems on axiomatic pipelines. Volatility serves as an especially revealing testbed because its axioms are well-understood, law violations have clear financial meaning, and world-model errors naturally create ghost arbitrage channels. We hope that the combination of:

1. 1.

   a formal axiomatic manifold,
2. 2.

   explicit Goodhart decompositions,
3. 3.

   law-strength frontiers and GFI,
4. 4.

   and a no-free-lunch theorem for unconstrained law-seeking RL

will prove useful in other domains where the central question is not “can RL optimize this objective?” but rather “does RL, when combined with approximate models and verifiable law penalties, discover law-aligned solutions or exploit artefacts?”.

Answering this question rigorously will require further theoretical development, richer empirical testbeds, and closer interaction between domain experts and learning theorists. Our volatility case study represents one step in that direction: a concrete, mathematically structured environment where Scientific AI methods can be subjected to the same kind of stress tests that financial models have long faced in practice.

## Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds

### A.1 Proof of Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

###### Proof of Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

We work throughout in the finite-dimensional Euclidean space
ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}
equipped with its standard inner product
⟨⋅,⋅⟩\langle\cdot,\cdot\rangle
and norm
∥⋅∥2\|\cdot\|\_{2}.
We write the rows of AvolA^{\mathrm{vol}} as
(aℓ⊤)ℓ=1m(a\_{\ell}^{\top})\_{\ell=1}^{m},
so that the constraint system
Avol​w≤bA^{\mathrm{vol}}w\leq b can be written componentwise as

|  |  |  |
| --- | --- | --- |
|  | aℓ⊤​w≤bℓ,ℓ=1,…,m.a\_{\ell}^{\top}w\;\leq\;b\_{\ell},\qquad\ell=1,\dots,m. |  |

##### Step 1: Polyhedral structure, closedness and convexity.

For each ℓ∈{1,…,m}\ell\in\{1,\dots,m\}, define the closed half-space

|  |  |  |
| --- | --- | --- |
|  | Hℓ:={w∈ℝdvol:aℓ⊤​w≤bℓ}.H\_{\ell}\;:=\;\bigl\{w\in\mathbb{R}^{d\_{\mathrm{vol}}}:a\_{\ell}^{\top}w\leq b\_{\ell}\bigr\}. |  |

Since aℓ⊤​w−bℓa\_{\ell}^{\top}w-b\_{\ell} is an affine (hence continuous) function of ww, we can write
Hℓ=(aℓ⊤​w−bℓ)−1​((−∞,0])H\_{\ell}=(a\_{\ell}^{\top}w-b\_{\ell})^{-1}((-\infty,0]),
i.e. as the inverse image of the closed set (−∞,0](-\infty,0] under a continuous map. Therefore each HℓH\_{\ell} is closed. Moreover, each HℓH\_{\ell} is convex because for any w1,w2∈Hℓw\_{1},w\_{2}\in H\_{\ell} and any θ∈[0,1]\theta\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | aℓ⊤​(θ​w1+(1−θ)​w2)=θ​aℓ⊤​w1+(1−θ)​aℓ⊤​w2≤θ​bℓ+(1−θ)​bℓ=bℓ,a\_{\ell}^{\top}\bigl(\theta w\_{1}+(1-\theta)w\_{2}\bigr)=\theta a\_{\ell}^{\top}w\_{1}+(1-\theta)a\_{\ell}^{\top}w\_{2}\leq\theta b\_{\ell}+(1-\theta)b\_{\ell}=b\_{\ell}, |  |

so that θ​w1+(1−θ)​w2∈Hℓ\theta w\_{1}+(1-\theta)w\_{2}\in H\_{\ell}.

By assumption, the set defined by the discretized butterfly and calendar constraints is

|  |  |  |
| --- | --- | --- |
|  | ℳvol=⋂ℓ=1mHℓ∩B,\mathcal{M}^{\mathrm{vol}}\;=\;\bigcap\_{\ell=1}^{m}H\_{\ell}\;\cap\;B, |  |

where
B⊂ℝdvolB\subset\mathbb{R}^{d\_{\mathrm{vol}}} denotes the (finite) collection of box constraints (e.g. lower and upper bounds on each component wiw\_{i} reflecting positivity and crude upper bounds on total variance). Concretely, we may write

|  |  |  |
| --- | --- | --- |
|  | B=∏i=1dvol[w¯i,w¯i]B\;=\;\prod\_{i=1}^{d\_{\mathrm{vol}}}[\underline{w}\_{i},\overline{w}\_{i}] |  |

for some scalars w¯i≤w¯i\underline{w}\_{i}\leq\overline{w}\_{i}; this is a Cartesian product of closed intervals and is therefore a non-empty compact convex subset of ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.

Since arbitrary intersections of closed sets are closed and intersections of convex sets are convex, it follows that

|  |  |  |
| --- | --- | --- |
|  | ℳvol=(⋂ℓ=1mHℓ)∩B\mathcal{M}^{\mathrm{vol}}=\left(\bigcap\_{\ell=1}^{m}H\_{\ell}\right)\cap B |  |

is closed and convex. Furthermore, by definition ℳvol\mathcal{M}^{\mathrm{vol}} is the intersection of finitely many closed half-spaces and a box; hence ℳvol\mathcal{M}^{\mathrm{vol}} is a *polyhedron* in the sense of convex analysis, i.e. a set of the form

|  |  |  |
| --- | --- | --- |
|  | ℳvol={w∈ℝdvol:A′​w≤b′}\mathcal{M}^{\mathrm{vol}}=\{w\in\mathbb{R}^{d\_{\mathrm{vol}}}:A^{\prime}w\leq b^{\prime}\} |  |

for some matrix A′A^{\prime} and vector b′b^{\prime}. This establishes that ℳvol\mathcal{M}^{\mathrm{vol}} is a closed convex polyhedron, apart from non-emptiness, which we now address.

##### Step 2: Non-emptiness via a Black–Scholes surface.

We show that there exists at least one total-variance vector wBS∈ℝdvolw^{\mathrm{BS}}\in\mathbb{R}^{d\_{\mathrm{vol}}} satisfying all of the inequalities Avol​w≤bA^{\mathrm{vol}}w\leq b, and hence
wBS∈ℳvolw^{\mathrm{BS}}\in\mathcal{M}^{\mathrm{vol}}.

Consider a constant-volatility Black–Scholes model with volatility parameter σ0>0\sigma\_{0}>0. On a continuous grid of maturities T>0T>0 and log-strikes kk, the corresponding total variance is

|  |  |  |
| --- | --- | --- |
|  | wBS​(T,k)=σ02​T.w^{\mathrm{BS}}(T,k)=\sigma\_{0}^{2}T. |  |

In particular, for any fixed TT, the map k↦wBS​(T,k)k\mapsto w^{\mathrm{BS}}(T,k) is *constant* in kk, and for any fixed kk, the map T↦wBS​(T,k)T\mapsto w^{\mathrm{BS}}(T,k) is strictly increasing and linear in TT.

Let {Tj}j=1NT\{T\_{j}\}\_{j=1}^{N\_{T}} be the finite set of maturities in our discretization, and {ki}i=1NK\{k\_{i}\}\_{i=1}^{N\_{K}} the finite set of log-strikes, so that
dvol=NT​NKd\_{\mathrm{vol}}=N\_{T}N\_{K}.
We construct the discretized total-variance vector wBS∈ℝdvolw^{\mathrm{BS}}\in\mathbb{R}^{d\_{\mathrm{vol}}} by setting

|  |  |  |
| --- | --- | --- |
|  | wi​jBS:=wBS​(Tj,ki)=σ02​Tj,1≤i≤NK, 1≤j≤NT.w^{\mathrm{BS}}\_{ij}:=w^{\mathrm{BS}}(T\_{j},k\_{i})=\sigma\_{0}^{2}T\_{j},\qquad 1\leq i\leq N\_{K},\ 1\leq j\leq N\_{T}. |  |

By construction we have, for each fixed maturity TjT\_{j},

|  |  |  |
| --- | --- | --- |
|  | wi+1,jBS−2​wi,jBS+wi−1,jBS=σ02​Tj−2​σ02​Tj+σ02​Tj=0w^{\mathrm{BS}}\_{i+1,j}-2w^{\mathrm{BS}}\_{i,j}+w^{\mathrm{BS}}\_{i-1,j}=\sigma\_{0}^{2}T\_{j}-2\sigma\_{0}^{2}T\_{j}+\sigma\_{0}^{2}T\_{j}=0 |  |

for all interior strikes ki−1,ki,ki+1k\_{i-1},k\_{i},k\_{i+1}. Thus the discrete second differences in strike are non-negative (indeed, identically zero), which implies that all *butterfly* constraints of the form

|  |  |  |
| --- | --- | --- |
|  | αi,j⊤​w≥0or equivalently−αi,j⊤​w≤0\alpha\_{i,j}^{\top}w\;\geq 0\quad\text{or equivalently}\quad-\alpha\_{i,j}^{\top}w\leq 0 |  |

are satisfied by wBSw^{\mathrm{BS}}.

Similarly, for each fixed strike kik\_{i} and consecutive maturities Tj<Tj+1T\_{j}<T\_{j+1}, we have

|  |  |  |
| --- | --- | --- |
|  | wi,j+1BS−wi,jBS=σ02​(Tj+1−Tj)≥ 0,w^{\mathrm{BS}}\_{i,j+1}-w^{\mathrm{BS}}\_{i,j}=\sigma\_{0}^{2}(T\_{j+1}-T\_{j})\;\geq\;0, |  |

so any discrete *calendar* constraints of the form
wi,j+1−wi,j≥0w\_{i,j+1}-w\_{i,j}\geq 0
(or again, linearly transformed into the system Avol​w≤bA^{\mathrm{vol}}w\leq b) are satisfied by wBSw^{\mathrm{BS}} with strict inequality when Tj+1>TjT\_{j+1}>T\_{j}.

Finally, because the Black–Scholes model is a classical example of a static-arbitrage-free implied volatility surface, its total-variance surface obeys the continuous-time no-arbitrage conditions (monotonicity in maturity, convexity in strike, and appropriate limiting behavior in the wings). Our discretization has been constructed exactly so that each continuous no-arbitrage condition, when evaluated on the finite grid {(Tj,ki)}\{(T\_{j},k\_{i})\}, yields one of the linear inequalities encoded in the rows of AvolA^{\mathrm{vol}}, possibly after simple positive scalings and translations. Therefore, by construction of the constraint system Avol​w≤bA^{\mathrm{vol}}w\leq b, we have

|  |  |  |
| --- | --- | --- |
|  | Avol​wBS≤b.A^{\mathrm{vol}}w^{\mathrm{BS}}\leq b. |  |

In particular,
wBS∈⋂ℓ=1mHℓw^{\mathrm{BS}}\in\bigcap\_{\ell=1}^{m}H\_{\ell},
and, choosing the box BB sufficiently large to contain the range {wi​jBS}\{w^{\mathrm{BS}}\_{ij}\} (which is trivially possible), we have wBS∈Bw^{\mathrm{BS}}\in B. Hence wBS∈ℳvolw^{\mathrm{BS}}\in\mathcal{M}^{\mathrm{vol}}, and ℳvol\mathcal{M}^{\mathrm{vol}} is non-empty.

Combining Steps 1 and 2, we conclude that ℳvol\mathcal{M}^{\mathrm{vol}} is a non-empty, closed, convex polyhedron in ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}, proving item (1).

##### Step 3: Static-arbitrage-free surfaces lie in ℳvol\mathcal{M}^{\mathrm{vol}}.

We now prove item (2). Let w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}} be the discretized total-variance surface associated with a continuous implied volatility surface (T,k)↦σ​(T,k)(T,k)\mapsto\sigma(T,k) that is static-arbitrage-free in the classical sense (no butterfly or calendar arbitrage). We show that w∈ℳvolw\in\mathcal{M}^{\mathrm{vol}}.

By definition, absence of static arbitrage implies in particular that, for each fixed maturity TT, the call price K↦C​(T,K)K\mapsto C(T,K) is a decreasing, convex function of strike KK. Expressing call prices in terms of total variance and log-strike and differentiating under mild regularity conditions yields that, for each fixed maturity TT, the total-variance function k↦w​(T,k)k\mapsto w(T,k) is convex in kk in an appropriate sense. In particular, for any three equally spaced log-strikes ki−1<ki<ki+1k\_{i-1}<k\_{i}<k\_{i+1} in our discretization we have

|  |  |  |
| --- | --- | --- |
|  | w​(T,ki)≤12​w​(T,ki−1)+12​w​(T,ki+1),w(T,k\_{i})\;\leq\;\frac{1}{2}w(T,k\_{i-1})+\frac{1}{2}w(T,k\_{i+1}), |  |

which is precisely the statement that the discrete second difference
w​(T,ki+1)−2​w​(T,ki)+w​(T,ki−1)w(T,k\_{i+1})-2w(T,k\_{i})+w(T,k\_{i-1})
is non-negative.

When we restrict to the grid {(Tj,ki)}\{(T\_{j},k\_{i})\} and collect the values
wi​j=w​(Tj,ki)w\_{ij}=w(T\_{j},k\_{i})
into the vector w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}}, each discrete convexity inequality becomes a linear constraint of the form

|  |  |  |
| --- | --- | --- |
|  | αi,j⊤​w≥0or equivalently−αi,j⊤​w≤0,\alpha\_{i,j}^{\top}w\geq 0\quad\text{or equivalently}\quad-\alpha\_{i,j}^{\top}w\leq 0, |  |

for an appropriate coefficient vector αi,j∈ℝdvol\alpha\_{i,j}\in\mathbb{R}^{d\_{\mathrm{vol}}} with only three non-zero entries at indices corresponding to (i−1,j),(i,j),(i+1,j)(i-1,j),(i,j),(i+1,j).

Similarly, absence of calendar arbitrage implies that, for fixed strike KK (equivalently fixed log-strike kk), the call price T↦C​(T,K)T\mapsto C(T,K) is non-decreasing in maturity TT. Translating this condition into total variance under mild regularity conditions yields that, for fixed kik\_{i}, the map T↦w​(T,ki)T\mapsto w(T,k\_{i}) is non-decreasing. Restricting again to the discretization {Tj}\{T\_{j}\} and collecting into ww, each such monotonicity condition gives a linear inequality of the form

|  |  |  |
| --- | --- | --- |
|  | βi,j⊤​w≥0⇔−βi,j⊤​w≤0,\beta\_{i,j}^{\top}w\geq 0\quad\Leftrightarrow\quad-\beta\_{i,j}^{\top}w\leq 0, |  |

where βi,j\beta\_{i,j} has two non-zero entries, corresponding to the pair (i,j+1)(i,j+1) and (i,j)(i,j).

By construction of the matrix AvolA^{\mathrm{vol}} and vector bb, *every* such discretized butterfly and calendar inequality appears as a row of AvolA^{\mathrm{vol}} (possibly after positive scaling and absorption of constant terms into bb), and the box constraints simply enforce crude lower and upper bounds on total variance that are trivially satisfied by any economically reasonable static-arbitrage-free surface (e.g., non-negativity of variance and boundedness over a finite set of maturities and strikes).

Thus, for a static-arbitrage-free surface, we have that all discretized no-arbitrage constraints hold simultaneously, which is equivalent to

|  |  |  |
| --- | --- | --- |
|  | Avol​w≤bandw∈B.A^{\mathrm{vol}}w\leq b\quad\text{and}\quad w\in B. |  |

Therefore w∈⋂ℓ=1mHℓ∩B=ℳvolw\in\bigcap\_{\ell=1}^{m}H\_{\ell}\cap B=\mathcal{M}^{\mathrm{vol}}. This proves that any static-arbitrage-free total-variance surface lies in ℳvol\mathcal{M}^{\mathrm{vol}}, establishing item (2).

##### Conclusion.

Steps 1–3 together prove that ℳvol\mathcal{M}^{\mathrm{vol}} is a non-empty, closed, convex polyhedron, and that any static-arbitrage-free total-variance surface lies in ℳvol\mathcal{M}^{\mathrm{vol}}. This completes the proof of Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
∎

### A.2 Proof of Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

###### Proof of Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

Recall from Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") that
ℳvol⊂ℝdvol\mathcal{M}\_{\mathrm{vol}}\subset\mathbb{R}^{d\_{\mathrm{vol}}} is non-empty, closed, and convex.
We work throughout in the Euclidean space ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}
equipped with its standard inner product ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle and norm
∥⋅∥2\|\cdot\|\_{2}.

##### Step 1: Existence of a minimizer.

Fix w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}} and consider the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minw~∈ℳvol⁡fw​(w~)withfw​(w~):=12​‖w~−w‖22.\min\_{\tilde{w}\in\mathcal{M}\_{\mathrm{vol}}}\;f\_{w}(\tilde{w})\quad\text{with}\quad f\_{w}(\tilde{w}):=\frac{1}{2}\,\|\tilde{w}-w\|\_{2}^{2}. |  | (28) |

The objective fwf\_{w} is continuous and *coercive* in the sense that

|  |  |  |
| --- | --- | --- |
|  | ‖w~‖2→∞⟹fw​(w~)=12​‖w~−w‖22→∞.\|\tilde{w}\|\_{2}\to\infty\quad\Longrightarrow\quad f\_{w}(\tilde{w})=\frac{1}{2}\|\tilde{w}-w\|\_{2}^{2}\to\infty. |  |

We now show that ([28](https://arxiv.org/html/2511.17304v1#A1.E28 "In Step 1: Existence of a minimizer. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) admits at least one minimizer in ℳvol\mathcal{M}\_{\mathrm{vol}}.

Define the infimum value

|  |  |  |
| --- | --- | --- |
|  | αw:=infw~∈ℳvolfw​(w~)∈[0,+∞).\alpha\_{w}:=\inf\_{\tilde{w}\in\mathcal{M}\_{\mathrm{vol}}}f\_{w}(\tilde{w})\in[0,+\infty). |  |

By definition of infimum, there exists a sequence (w~n)n≥1⊂ℳvol(\tilde{w}\_{n})\_{n\geq 1}\subset\mathcal{M}\_{\mathrm{vol}}
such that
fw​(w~n)→αwf\_{w}(\tilde{w}\_{n})\to\alpha\_{w}
as n→∞n\to\infty.
We first show that (w~n)(\tilde{w}\_{n}) is bounded. Suppose by contradiction that
‖w~n‖2→∞\|\tilde{w}\_{n}\|\_{2}\to\infty along some subsequence. Then by coercivity of
fwf\_{w} we would have fw​(w~n)→∞f\_{w}(\tilde{w}\_{n})\to\infty along that subsequence,
contradicting the fact that fw​(w~n)f\_{w}(\tilde{w}\_{n}) converges to the finite value
αw\alpha\_{w}. Hence (w~n)(\tilde{w}\_{n}) is bounded in ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.

Since we are in finite dimension, every bounded sequence has a convergent
subsequence. Thus there exists a subsequence (which we do not relabel) and a
limit point w~⋆∈ℝdvol\tilde{w}^{\star}\in\mathbb{R}^{d\_{\mathrm{vol}}} such that

|  |  |  |
| --- | --- | --- |
|  | w~n→w~⋆as ​n→∞.\tilde{w}\_{n}\to\tilde{w}^{\star}\quad\text{as }n\to\infty. |  |

Because ℳvol\mathcal{M}\_{\mathrm{vol}} is closed, and each w~n∈ℳvol\tilde{w}\_{n}\in\mathcal{M}\_{\mathrm{vol}}, the limit
w~⋆\tilde{w}^{\star} must also satisfy w~⋆∈ℳvol\tilde{w}^{\star}\in\mathcal{M}\_{\mathrm{vol}}.

By continuity of fwf\_{w}, we have

|  |  |  |
| --- | --- | --- |
|  | fw​(w~⋆)=limn→∞fw​(w~n)=αw.f\_{w}(\tilde{w}^{\star})=\lim\_{n\to\infty}f\_{w}(\tilde{w}\_{n})=\alpha\_{w}. |  |

Therefore w~⋆\tilde{w}^{\star} attains the infimum of ([28](https://arxiv.org/html/2511.17304v1#A1.E28 "In Step 1: Existence of a minimizer. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),
so a minimizer exists and we may define

|  |  |  |
| --- | --- | --- |
|  | Πℳvol​(w):=w~⋆.\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w):=\tilde{w}^{\star}. |  |

##### Step 2: Uniqueness of the minimizer.

We now show that the minimizer is unique. The function fwf\_{w} is not only
continuous but *strictly convex* on ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}:
for any x,y∈ℝdvolx,y\in\mathbb{R}^{d\_{\mathrm{vol}}}, x≠yx\neq y, and any
θ∈(0,1)\theta\in(0,1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | fw​(θ​x+(1−θ)​y)\displaystyle f\_{w}(\theta x+(1-\theta)y) | =12​‖θ​x+(1−θ)​y−w‖22\displaystyle=\frac{1}{2}\|\theta x+(1-\theta)y-w\|\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​‖θ​(x−w)+(1−θ)​(y−w)‖22\displaystyle=\frac{1}{2}\big\|\theta(x-w)+(1-\theta)(y-w)\big\|\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <12​(θ​‖x−w‖22+(1−θ)​‖y−w‖22)\displaystyle<\frac{1}{2}\big(\theta\|x-w\|\_{2}^{2}+(1-\theta)\|y-w\|\_{2}^{2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =θ​fw​(x)+(1−θ)​fw​(y),\displaystyle=\theta f\_{w}(x)+(1-\theta)f\_{w}(y), |  |

where the strict inequality follows from strict convexity of the squared norm
unless x−wx-w and y−wy-w are linearly dependent with the same direction and
norm, which can only happen if x=yx=y.

Assume, for contradiction, that there exist two distinct minimizers
w~1,w~2∈ℳvol\tilde{w}\_{1},\tilde{w}\_{2}\in\mathcal{M}\_{\mathrm{vol}} of ([28](https://arxiv.org/html/2511.17304v1#A1.E28 "In Step 1: Existence of a minimizer. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), i.e.,

|  |  |  |
| --- | --- | --- |
|  | fw​(w~1)=fw​(w~2)=αw,w~1≠w~2.f\_{w}(\tilde{w}\_{1})=f\_{w}(\tilde{w}\_{2})=\alpha\_{w},\qquad\tilde{w}\_{1}\neq\tilde{w}\_{2}. |  |

Because ℳvol\mathcal{M}\_{\mathrm{vol}} is convex, their midpoint
w~θ:=12​w~1+12​w~2\tilde{w}\_{\theta}:=\tfrac{1}{2}\tilde{w}\_{1}+\tfrac{1}{2}\tilde{w}\_{2}
also lies in ℳvol\mathcal{M}\_{\mathrm{vol}}.
By strict convexity,

|  |  |  |
| --- | --- | --- |
|  | fw​(w~θ)<12​fw​(w~1)+12​fw​(w~2)=αw,f\_{w}(\tilde{w}\_{\theta})<\frac{1}{2}f\_{w}(\tilde{w}\_{1})+\frac{1}{2}f\_{w}(\tilde{w}\_{2})=\alpha\_{w}, |  |

contradicting the fact that αw\alpha\_{w} is the infimum over ℳvol\mathcal{M}\_{\mathrm{vol}}.
Therefore the minimizer of ([28](https://arxiv.org/html/2511.17304v1#A1.E28 "In Step 1: Existence of a minimizer. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) is unique, and the
mapping w↦Πℳvol​(w)w\mapsto\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w) is well-defined on all of
ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.

##### Step 3: First-order optimality and firm non-expansiveness.

The projection Πℳvol​(w)\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w) can be characterized by a classical
first-order optimality condition for convex minimization over a closed convex
set. Let w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}} be arbitrary and denote
w~:=Πℳvol​(w)\tilde{w}:=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w).
Since ℳvol\mathcal{M}\_{\mathrm{vol}} is closed and convex and fwf\_{w} is differentiable and strictly convex, we know that w~\tilde{w} is the unique point in ℳvol\mathcal{M}\_{\mathrm{vol}} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨w~−w,z−w~⟩≥ 0for all ​z∈ℳvol.\langle\tilde{w}-w,z-\tilde{w}\rangle\;\geq\;0\quad\text{for all }z\in\mathcal{M}\_{\mathrm{vol}}. |  | (29) |

Indeed, this is the variational inequality corresponding to optimality of
w~\tilde{w} for the minimization of fwf\_{w} over ℳvol\mathcal{M}\_{\mathrm{vol}}; see, e.g., standard
results on projections in Hilbert spaces.

Let now w,w′∈ℝdvolw,w^{\prime}\in\mathbb{R}^{d\_{\mathrm{vol}}} be arbitrary, and set

|  |  |  |
| --- | --- | --- |
|  | p:=Πℳvol​(w),q:=Πℳvol​(w′).p:=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w),\qquad q:=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w^{\prime}). |  |

Applying ([29](https://arxiv.org/html/2511.17304v1#A1.E29 "In Step 3: First-order optimality and firm non-expansiveness. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) with the pair (w,p)(w,p) and the choice
z=q∈ℳvolz=q\in\mathcal{M}\_{\mathrm{vol}} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨p−w,q−p⟩≥ 0.\langle p-w,q-p\rangle\;\geq\;0. |  | (30) |

Similarly, applying ([29](https://arxiv.org/html/2511.17304v1#A1.E29 "In Step 3: First-order optimality and firm non-expansiveness. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) with the pair (w′,q)(w^{\prime},q) and the
choice z=pz=p yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨q−w′,p−q⟩≥ 0.\langle q-w^{\prime},p-q\rangle\;\geq\;0. |  | (31) |

Adding ([30](https://arxiv.org/html/2511.17304v1#A1.E30 "In Step 3: First-order optimality and firm non-expansiveness. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and ([31](https://arxiv.org/html/2511.17304v1#A1.E31 "In Step 3: First-order optimality and firm non-expansiveness. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), and recalling that
⟨q−w′,p−q⟩=−⟨q−w′,q−p⟩\langle q-w^{\prime},p-q\rangle=-\langle q-w^{\prime},q-p\rangle, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≤⟨p−w,q−p⟩+⟨q−w′,p−q⟩\displaystyle\leq\langle p-w,q-p\rangle+\langle q-w^{\prime},p-q\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨p−w,q−p⟩−⟨q−w′,q−p⟩\displaystyle=\langle p-w,q-p\rangle-\langle q-w^{\prime},q-p\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨(p−w)−(q−w′),q−p⟩\displaystyle=\langle(p-w)-(q-w^{\prime}),q-p\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨(w′−w)−(q−p),q−p⟩\displaystyle=\langle(w^{\prime}-w)-(q-p),q-p\rangle |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =⟨w′−w,q−p⟩−‖q−p‖22.\displaystyle=\langle w^{\prime}-w,q-p\rangle-\|q-p\|\_{2}^{2}. |  | (32) |

Rearranging ([32](https://arxiv.org/html/2511.17304v1#A1.E32 "In Step 3: First-order optimality and firm non-expansiveness. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) gives the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖p−q‖22≤⟨w′−w,q−p⟩.\|p-q\|\_{2}^{2}\;\leq\;\langle w^{\prime}-w,q-p\rangle. |  | (33) |

Taking absolute values and applying the Cauchy–Schwarz inequality to the right-hand side yields

|  |  |  |
| --- | --- | --- |
|  | ‖p−q‖22≤|⟨w′−w,q−p⟩|≤‖w′−w‖2​‖q−p‖2.\|p-q\|\_{2}^{2}\leq|\langle w^{\prime}-w,q-p\rangle|\leq\|w^{\prime}-w\|\_{2}\,\|q-p\|\_{2}. |  |

If p≠qp\neq q, we can divide both sides by ‖p−q‖2>0\|p-q\|\_{2}>0 and obtain

|  |  |  |
| --- | --- | --- |
|  | ‖p−q‖2≤‖w′−w‖2.\|p-q\|\_{2}\leq\|w^{\prime}-w\|\_{2}. |  |

If p=qp=q, the inequality trivially holds as equality.
Thus, for every w,w′∈ℝdvolw,w^{\prime}\in\mathbb{R}^{d\_{\mathrm{vol}}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Πℳvol​(w)−Πℳvol​(w′)‖2≤‖w−w′‖2.\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w^{\prime})\|\_{2}\leq\|w-w^{\prime}\|\_{2}. |  | (34) |

That is, the projection operator Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} is *non-expansive*, with
Lipschitz constant equal to 1.

##### Conclusion.

We have shown that ℳvol\mathcal{M}\_{\mathrm{vol}} is non-empty, closed, and convex (by
Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), that the Euclidean projection
onto ℳvol\mathcal{M}\_{\mathrm{vol}} exists and is unique for every w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}}, and that
Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} is 11-Lipschitz in the Euclidean norm. This completes the
proof of Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
∎

### A.3 Proof of Lemma [1](https://arxiv.org/html/2511.17304v1#Thmlemma1 "Lemma 1 (Local Lipschitz continuity of law penalty). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

###### Proof of Lemma [1](https://arxiv.org/html/2511.17304v1#Thmlemma1 "Lemma 1 (Local Lipschitz continuity of law penalty). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

Recall the definition of the volatility law-penalty functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒvol​(w):=12​‖w−Πℳvol​(w)‖22,w∈ℝdvol,\mathcal{L}\_{\mathrm{vol}}(w):=\frac{1}{2}\,\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2}^{2},\qquad w\in\mathbb{R}^{d\_{\mathrm{vol}}}, |  | (35) |

where ℳvol⊂ℝdvol\mathcal{M}\_{\mathrm{vol}}\subset\mathbb{R}^{d\_{\mathrm{vol}}} is the volatility law manifold
(cf. Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and
Πℳvol:ℝdvol→ℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}}:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathcal{M}\_{\mathrm{vol}} is the Euclidean projection
(cf. Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

We show that ℒvol\mathcal{L}\_{\mathrm{vol}} is *locally Lipschitz* on ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}},
i.e., for every compact set K⊂ℝdvolK\subset\mathbb{R}^{d\_{\mathrm{vol}}} there exists
LK<∞L\_{K}<\infty such that

|  |  |  |
| --- | --- | --- |
|  | |ℒvol​(w1)−ℒvol​(w2)|≤LK​‖w1−w2‖2for all ​w1,w2∈K.|\mathcal{L}\_{\mathrm{vol}}(w\_{1})-\mathcal{L}\_{\mathrm{vol}}(w\_{2})|\;\leq\;L\_{K}\,\|w\_{1}-w\_{2}\|\_{2}\quad\text{for all }w\_{1},w\_{2}\in K. |  |

##### Step 1: Basic Lipschitz properties of the projection.

Define the *residual map*

|  |  |  |
| --- | --- | --- |
|  | h​(w):=w−Πℳvol​(w),w∈ℝdvol.h(w):=w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w),\qquad w\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  |

By Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), the projection Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} is
non-expansive:

|  |  |  |
| --- | --- | --- |
|  | ‖Πℳvol​(w1)−Πℳvol​(w2)‖2≤‖w1−w2‖2for all ​w1,w2∈ℝdvol.\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{1})-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{2})\|\_{2}\leq\|w\_{1}-w\_{2}\|\_{2}\quad\text{for all }w\_{1},w\_{2}\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  |

It follows that the residual map hh is globally Lipschitz with constant 22.
Indeed, for any w1,w2∈ℝdvolw\_{1},w\_{2}\in\mathbb{R}^{d\_{\mathrm{vol}}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖h​(w1)−h​(w2)‖2\displaystyle\|h(w\_{1})-h(w\_{2})\|\_{2} | =‖(w1−Πℳvol​(w1))−(w2−Πℳvol​(w2))‖2\displaystyle=\big\|(w\_{1}-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{1}))-(w\_{2}-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{2}))\big\|\_{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖w1−w2‖2+‖Πℳvol​(w1)−Πℳvol​(w2)‖2\displaystyle\leq\|w\_{1}-w\_{2}\|\_{2}+\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{1})-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{2})\|\_{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖w1−w2‖2+‖w1−w2‖2\displaystyle\leq\|w\_{1}-w\_{2}\|\_{2}+\|w\_{1}-w\_{2}\|\_{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​‖w1−w2‖2.\displaystyle=2\,\|w\_{1}-w\_{2}\|\_{2}. |  | (36) |

Thus hh is 22-Lipschitz on all of ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.

##### Step 2: Bounding the residual on bounded sets.

Fix a radius R>0R>0 and consider the closed Euclidean ball

|  |  |  |
| --- | --- | --- |
|  | BR:={w∈ℝdvol:‖w‖2≤R}.B\_{R}:=\{w\in\mathbb{R}^{d\_{\mathrm{vol}}}:\|w\|\_{2}\leq R\}. |  |

We first show that ‖h​(w)‖\|h(w)\| is uniformly bounded on BRB\_{R}.

Let w0:=0w\_{0}:=0 be the origin. Since ℳvol\mathcal{M}\_{\mathrm{vol}} is non-empty
(Proposition [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), the projection
Πℳvol​(w0)\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{0}) is well-defined and finite.
Denote c0:=‖Πℳvol​(0)‖2<∞c\_{0}:=\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(0)\|\_{2}<\infty.

For any w∈BRw\in B\_{R}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Πℳvol​(w)‖2\displaystyle\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2} | ≤‖Πℳvol​(w)−Πℳvol​(0)‖2+‖Πℳvol​(0)‖2\displaystyle\leq\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(0)\|\_{2}+\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(0)\|\_{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤‖w−0‖2+c0≤R+c0,\displaystyle\leq\|w-0\|\_{2}+c\_{0}\leq R+c\_{0}, |  | (37) |

where we used non-expansiveness of Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} and ‖w‖2≤R\|w\|\_{2}\leq R.

Hence, for any w∈BRw\in B\_{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖h​(w)‖2\displaystyle\|h(w)\|\_{2} | =‖w−Πℳvol​(w)‖2\displaystyle=\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖w‖2+‖Πℳvol​(w)‖2\displaystyle\leq\|w\|\_{2}+\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤R+(R+c0)\displaystyle\leq R+(R+c\_{0}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​R+c0.\displaystyle=2R+c\_{0}. |  | (38) |

Define the constant

|  |  |  |
| --- | --- | --- |
|  | KR:=2​R+c0.K\_{R}:=2R+c\_{0}. |  |

Then ‖h​(w)‖2≤KR\|h(w)\|\_{2}\leq K\_{R} for all w∈BRw\in B\_{R}.

##### Step 3: Lipschitz continuity of the squared norm of the residual.

Rewrite ℒvol\mathcal{L}\_{\mathrm{vol}} in terms of hh:

|  |  |  |
| --- | --- | --- |
|  | ℒvol​(w)=12​‖h​(w)‖22.\mathcal{L}\_{\mathrm{vol}}(w)=\frac{1}{2}\,\|h(w)\|\_{2}^{2}. |  |

Let w1,w2∈BRw\_{1},w\_{2}\in B\_{R} be arbitrary, and set
h1:=h​(w1)h\_{1}:=h(w\_{1}), h2:=h​(w2)h\_{2}:=h(w\_{2}).
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℒvol​(w1)−ℒvol​(w2)|\displaystyle|\mathcal{L}\_{\mathrm{vol}}(w\_{1})-\mathcal{L}\_{\mathrm{vol}}(w\_{2})| | =12​|‖h1‖22−‖h2‖22|\displaystyle=\frac{1}{2}\,\big|\|h\_{1}\|\_{2}^{2}-\|h\_{2}\|\_{2}^{2}\big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​|⟨h1+h2,h1−h2⟩|\displaystyle=\frac{1}{2}\,|\langle h\_{1}+h\_{2},\,h\_{1}-h\_{2}\rangle| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤12​(‖h1‖2+‖h2‖2)​‖h1−h2‖2.\displaystyle\leq\frac{1}{2}\,\big(\|h\_{1}\|\_{2}+\|h\_{2}\|\_{2}\big)\,\|h\_{1}-h\_{2}\|\_{2}. |  | (39) |

From ([38](https://arxiv.org/html/2511.17304v1#A1.E38 "In Step 2: Bounding the residual on bounded sets. ‣ A.3 Proof of Lemma 1 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we have
‖h1‖2≤KR\|h\_{1}\|\_{2}\leq K\_{R} and ‖h2‖2≤KR\|h\_{2}\|\_{2}\leq K\_{R}.
Moreover, by ([36](https://arxiv.org/html/2511.17304v1#A1.E36 "In Step 1: Basic Lipschitz properties of the projection. ‣ A.3 Proof of Lemma 1 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),
‖h1−h2‖2≤2​‖w1−w2‖2\|h\_{1}-h\_{2}\|\_{2}\leq 2\,\|w\_{1}-w\_{2}\|\_{2}.
Substituting these bounds into ([39](https://arxiv.org/html/2511.17304v1#A1.E39 "In Step 3: Lipschitz continuity of the squared norm of the residual. ‣ A.3 Proof of Lemma 1 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℒvol​(w1)−ℒvol​(w2)|\displaystyle|\mathcal{L}\_{\mathrm{vol}}(w\_{1})-\mathcal{L}\_{\mathrm{vol}}(w\_{2})| | ≤12​(KR+KR)​(2​‖w1−w2‖2)\displaystyle\leq\frac{1}{2}\,(K\_{R}+K\_{R})\,\big(2\,\|w\_{1}-w\_{2}\|\_{2}\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​KR​‖w1−w2‖2.\displaystyle=2K\_{R}\,\|w\_{1}-w\_{2}\|\_{2}. |  | (40) |

Recalling that KR=2​R+c0K\_{R}=2R+c\_{0}, we can rewrite ([40](https://arxiv.org/html/2511.17304v1#A1.E40 "In Step 3: Lipschitz continuity of the squared norm of the residual. ‣ A.3 Proof of Lemma 1 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) as

|  |  |  |
| --- | --- | --- |
|  | |ℒvol​(w1)−ℒvol​(w2)|≤LR​‖w1−w2‖2,LR:=2​(2​R+c0),∀w1,w2∈BR.|\mathcal{L}\_{\mathrm{vol}}(w\_{1})-\mathcal{L}\_{\mathrm{vol}}(w\_{2})|\leq L\_{R}\,\|w\_{1}-w\_{2}\|\_{2},\quad L\_{R}:=2(2R+c\_{0}),\quad\forall\,w\_{1},w\_{2}\in B\_{R}. |  |

Thus ℒvol\mathcal{L}\_{\mathrm{vol}} is Lipschitz on each ball BRB\_{R}, with Lipschitz constant LRL\_{R}
depending only on RR and the fixed constant c0c\_{0}.

##### Step 4: Local Lipschitz continuity.

A function that is Lipschitz on every bounded ball in ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}
is, by definition, *locally Lipschitz*. More precisely, for any compact set
K⊂ℝdvolK\subset\mathbb{R}^{d\_{\mathrm{vol}}}, there exists R>0R>0 such that
K⊂BRK\subset B\_{R}; then the Lipschitz constant LRL\_{R} from ([40](https://arxiv.org/html/2511.17304v1#A1.E40 "In Step 3: Lipschitz continuity of the squared norm of the residual. ‣ A.3 Proof of Lemma 1 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"))
works for all w1,w2∈Kw\_{1},w\_{2}\in K. Therefore, ℒvol\mathcal{L}\_{\mathrm{vol}} is locally Lipschitz on
ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.

##### Remark.

The above argument is self-contained and uses only the non-expansiveness of the
projection onto a closed convex set. An alternative viewpoint, standard in
convex analysis, is to note that ℒvol\mathcal{L}\_{\mathrm{vol}} coincides with the *squared
distance function* to the non-empty closed convex set ℳvol\mathcal{M}\_{\mathrm{vol}}, which is known
to be Fréchet differentiable on ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}} with
11-Lipschitz gradient (see, e.g., BauschkeCombettes2011 [[26](https://arxiv.org/html/2511.17304v1#bib.bib26), Prop. 12.29–12.30]).
In particular, the gradient mapping is globally Lipschitz, which again implies
that ℒvol\mathcal{L}\_{\mathrm{vol}} is locally Lipschitz. We include the direct argument above to keep
the presentation self-contained.

This completes the proof of Lemma [1](https://arxiv.org/html/2511.17304v1#Thmlemma1 "Lemma 1 (Local Lipschitz continuity of law penalty). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
∎

### A.4 Proof of Proposition [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

###### Proof of Proposition [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

Recall the definition of the volatility law-penalty functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒvol​(w):=12​‖w−Πℳvol​(w)‖22,w∈ℝdvol,\mathcal{L}\_{\mathrm{vol}}(w):=\frac{1}{2}\,\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2}^{2},\qquad w\in\mathbb{R}^{d\_{\mathrm{vol}}}, |  | (41) |

where ℳvol⊂ℝdvol\mathcal{M}\_{\mathrm{vol}}\subset\mathbb{R}^{d\_{\mathrm{vol}}} is the volatility law
manifold and Πℳvol:ℝdvol→ℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}}:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathcal{M}\_{\mathrm{vol}} is the
Euclidean projection (Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). We show that

|  |  |  |
| --- | --- | --- |
|  | ℒvol​(w)=0⟺w∈ℳvol.\mathcal{L}\_{\mathrm{vol}}(w)=0\quad\Longleftrightarrow\quad w\in\mathcal{M}\_{\mathrm{vol}}. |  |

##### (⇒\Rightarrow) If w∈ℳvolw\in\mathcal{M}\_{\mathrm{vol}} then ℒvol​(w)=0\mathcal{L}\_{\mathrm{vol}}(w)=0.

Assume w∈ℳvolw\in\mathcal{M}\_{\mathrm{vol}}. By the definition of the Euclidean projection, any point
w~∈ℳvol\tilde{w}\in\mathcal{M}\_{\mathrm{vol}} satisfies

|  |  |  |
| --- | --- | --- |
|  | ‖Πℳvol​(w)−w‖2≤‖w~−w‖2.\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)-w\|\_{2}\leq\|\tilde{w}-w\|\_{2}. |  |

In particular, we may take w~=w\tilde{w}=w itself, which is feasible since
w∈ℳvolw\in\mathcal{M}\_{\mathrm{vol}}. This yields

|  |  |  |
| --- | --- | --- |
|  | ‖Πℳvol​(w)−w‖2≤‖w−w‖2=0.\|\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)-w\|\_{2}\leq\|w-w\|\_{2}=0. |  |

By non-negativity of the norm, we must have equality, hence

|  |  |  |
| --- | --- | --- |
|  | Πℳvol​(w)=w.\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)=w. |  |

Substituting this into ([41](https://arxiv.org/html/2511.17304v1#A1.E41 "In A.4 Proof of Proposition 3 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) gives

|  |  |  |
| --- | --- | --- |
|  | ℒvol​(w)=12​‖w−Πℳvol​(w)‖22=12​‖w−w‖22=0.\mathcal{L}\_{\mathrm{vol}}(w)=\frac{1}{2}\,\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2}^{2}=\frac{1}{2}\,\|w-w\|\_{2}^{2}=0. |  |

Thus w∈ℳvol⟹ℒvol​(w)=0w\in\mathcal{M}\_{\mathrm{vol}}\implies\mathcal{L}\_{\mathrm{vol}}(w)=0.

##### (⇐\Leftarrow) If ℒvol​(w)=0\mathcal{L}\_{\mathrm{vol}}(w)=0 then w∈ℳvolw\in\mathcal{M}\_{\mathrm{vol}}.

Now assume ℒvol​(w)=0\mathcal{L}\_{\mathrm{vol}}(w)=0. By ([41](https://arxiv.org/html/2511.17304v1#A1.E41 "In A.4 Proof of Proposition 3 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) we have

|  |  |  |
| --- | --- | --- |
|  | 0=ℒvol​(w)=12​‖w−Πℳvol​(w)‖22.0=\mathcal{L}\_{\mathrm{vol}}(w)=\frac{1}{2}\,\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2}^{2}. |  |

Since the Euclidean norm is non-negative and vanishes only at zero, this
implies

|  |  |  |
| --- | --- | --- |
|  | ‖w−Πℳvol​(w)‖2=0⟹w=Πℳvol​(w).\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2}=0\quad\Longrightarrow\quad w=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w). |  |

The projection Πℳvol​(w)\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w) takes values in ℳvol\mathcal{M}\_{\mathrm{vol}} by construction, so
w=Πℳvol​(w)∈ℳvolw=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\in\mathcal{M}\_{\mathrm{vol}}. Hence ℒvol​(w)=0⟹w∈ℳvol\mathcal{L}\_{\mathrm{vol}}(w)=0\implies w\in\mathcal{M}\_{\mathrm{vol}}.

##### Alternative viewpoint via distance to closed sets.

For completeness, we note that ([41](https://arxiv.org/html/2511.17304v1#A1.E41 "In A.4 Proof of Proposition 3 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) can be written as

|  |  |  |
| --- | --- | --- |
|  | ℒvol​(w)=12​dist2​(w,ℳvol),dist​(w,ℳvol):=infw~∈ℳvol‖w−w~‖2,\mathcal{L}\_{\mathrm{vol}}(w)=\frac{1}{2}\,\mathrm{dist}^{2}(w,\mathcal{M}\_{\mathrm{vol}}),\qquad\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}}):=\inf\_{\tilde{w}\in\mathcal{M}\_{\mathrm{vol}}}\|w-\tilde{w}\|\_{2}, |  |

where the infimum is attained at Πℳvol​(w)\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w) because ℳvol\mathcal{M}\_{\mathrm{vol}} is
non-empty, closed, and convex
(Propositions [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).
By basic properties of distance functions to closed sets in Hilbert spaces, one has

|  |  |  |
| --- | --- | --- |
|  | dist​(w,ℳvol)=0⟺w∈ℳvol¯=ℳvol.\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}})=0\quad\Longleftrightarrow\quad w\in\overline{\mathcal{M}\_{\mathrm{vol}}}=\mathcal{M}\_{\mathrm{vol}}. |  |

Since ℒvol​(w)=12​dist2​(w,ℳvol)\mathcal{L}\_{\mathrm{vol}}(w)=\tfrac{1}{2}\mathrm{dist}^{2}(w,\mathcal{M}\_{\mathrm{vol}}), this is equivalent to

|  |  |  |
| --- | --- | --- |
|  | ℒvol​(w)=0⟺w∈ℳvol,\mathcal{L}\_{\mathrm{vol}}(w)=0\quad\Longleftrightarrow\quad w\in\mathcal{M}\_{\mathrm{vol}}, |  |

which is precisely the statement of Proposition [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

This completes the proof.
∎

### A.5 Proof of Proposition [4](https://arxiv.org/html/2511.17304v1#Thmproposition4 "Proposition 4 (Ghost reward bounded by law distance). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

###### Proof.

Recall the setting and notation:

1. 1.

   The volatility law manifold ℳvol⊂ℝdvol\mathcal{M}\_{\mathrm{vol}}\subset\mathbb{R}^{d\_{\mathrm{vol}}} is non-empty, closed, and convex by Propositions [1](https://arxiv.org/html/2511.17304v1#Thmproposition1 "Proposition 1 (Axiomatic representation of volatility law manifold). ‣ Calendar monotonicity. ‣ 2.1 Volatility-Specific Law Manifold: From Textbook Axioms to a Polyhedron ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
2. 2.

   The Euclidean projection Πℳvol:ℝdvol→ℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}}:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathcal{M}\_{\mathrm{vol}} is well-defined and 11-Lipschitz
   (Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).
3. 3.

   The law-penalty functional is given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ℒvol​(w):=12​‖w−Πℳvol​(w)‖22=12​dist2​(w,ℳvol),w∈ℝdvol,\mathcal{L}\_{\mathrm{vol}}(w):=\frac{1}{2}\bigl\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\bigr\|\_{2}^{2}=\frac{1}{2}\,\mathrm{dist}^{2}\bigl(w,\mathcal{M}\_{\mathrm{vol}}\bigr),\qquad w\in\mathbb{R}^{d\_{\mathrm{vol}}}, |  | (42) |

   where dist​(w,ℳvol):=infw~∈ℳvol‖w−w~‖2\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}}):=\inf\_{\tilde{w}\in\mathcal{M}\_{\mathrm{vol}}}\|w-\tilde{w}\|\_{2}.
4. 4.

   The on-manifold and ghost reward components are

   |  |  |  |
   | --- | --- | --- |
   |  | rℳ​(w):=r​(Πℳvol​(w)),r⟂​(w):=r​(w)−rℳ​(w).r^{\mathcal{M}}(w):=r\bigl(\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\bigr),\qquad r^{\perp}(w):=r(w)-r^{\mathcal{M}}(w). |  |

Assume that r:ℝdvol→ℝr:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathbb{R} is LrL\_{r}-Lipschitz with respect to the Euclidean norm, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |r​(w)−r​(w′)|≤Lr​‖w−w′‖2∀w,w′∈ℝdvol.|r(w)-r(w^{\prime})|\leq L\_{r}\,\|w-w^{\prime}\|\_{2}\qquad\forall\,w,w^{\prime}\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  | (43) |

We now prove the bound

|  |  |  |
| --- | --- | --- |
|  | |r⟂​(w)|=|r​(w)−rℳ​(w)|≤Lr​dist​(w,ℳvol)=Lr​2​ℒvol​(w),∀w∈ℝdvol.|r^{\perp}(w)|=\bigl|r(w)-r^{\mathcal{M}}(w)\bigr|\leq L\_{r}\,\mathrm{dist}\bigl(w,\mathcal{M}\_{\mathrm{vol}}\bigr)=L\_{r}\sqrt{2\,\mathcal{L}\_{\mathrm{vol}}(w)},\qquad\forall\,w\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  |

##### Step 1: Bounding the ghost component by the distance to ℳvol\mathcal{M}\_{\mathrm{vol}}.

Fix any w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}}. By the definition of rℳr^{\mathcal{M}} and the Lipschitz property ([43](https://arxiv.org/html/2511.17304v1#A1.E43 "In A.5 Proof of Proposition 4 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |r⟂​(w)|\displaystyle|r^{\perp}(w)| | =|r​(w)−rℳ​(w)|=|r​(w)−r​(Πℳvol​(w))|\displaystyle=\bigl|r(w)-r^{\mathcal{M}}(w)\bigr|=\bigl|r(w)-r(\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w))\bigr| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Lr​‖w−Πℳvol​(w)‖2.\displaystyle\leq L\_{r}\bigl\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\bigr\|\_{2}. |  |

By the definition of the distance function and properties of the projection,

|  |  |  |
| --- | --- | --- |
|  | ‖w−Πℳvol​(w)‖2=dist​(w,ℳvol),\bigl\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\bigr\|\_{2}=\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}}), |  |

since Πℳvol​(w)\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w) is a minimizer of w~↦‖w−w~‖2\tilde{w}\mapsto\|w-\tilde{w}\|\_{2} over w~∈ℳvol\tilde{w}\in\mathcal{M}\_{\mathrm{vol}} . Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | |r⟂​(w)|≤Lr​dist​(w,ℳvol).|r^{\perp}(w)|\leq L\_{r}\,\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}}). |  | (44) |

##### Step 2: Expressing the distance via ℒvol\mathcal{L}\_{\mathrm{vol}}.

From the definition ([42](https://arxiv.org/html/2511.17304v1#A1.E42 "In item 3 ‣ A.5 Proof of Proposition 4 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we have

|  |  |  |
| --- | --- | --- |
|  | dist​(w,ℳvol)=‖w−Πℳvol​(w)‖2=2​ℒvol​(w).\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}})=\bigl\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\bigr\|\_{2}=\sqrt{2\,\mathcal{L}\_{\mathrm{vol}}(w)}. |  |

Substituting this identity into ([44](https://arxiv.org/html/2511.17304v1#A1.E44 "In Step 1: Bounding the ghost component by the distance to ℳᵥₒₗ. ‣ A.5 Proof of Proposition 4 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields

|  |  |  |
| --- | --- | --- |
|  | |r⟂​(w)|≤Lr​dist​(w,ℳvol)=Lr​2​ℒvol​(w).|r^{\perp}(w)|\leq L\_{r}\,\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}})=L\_{r}\sqrt{2\,\mathcal{L}\_{\mathrm{vol}}(w)}. |  |

Since w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}} was arbitrary, the inequality holds for all ww.

##### Remark on optimality of the bound.

The inequality in Proposition [4](https://arxiv.org/html/2511.17304v1#Thmproposition4 "Proposition 4 (Ghost reward bounded by law distance). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") is sharp in the sense that, for fixed ℳvol\mathcal{M}\_{\mathrm{vol}} and Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}}, one can construct Lipschitz functions rr that nearly saturate the bound. For example, if rr is chosen to be affine in the normal direction to ℳvol\mathcal{M}\_{\mathrm{vol}} at some point, with gradient of norm LrL\_{r}, then along rays orthogonal to ℳvol\mathcal{M}\_{\mathrm{vol}} we obtain

|  |  |  |
| --- | --- | --- |
|  | |r​(w)−r​(Πℳvol​(w))|≈Lr​‖w−Πℳvol​(w)‖2,|r(w)-r(\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w))|\approx L\_{r}\,\|w-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(w)\|\_{2}, |  |

up to second-order curvature effects of ℳvol\mathcal{M}\_{\mathrm{vol}}. Thus the scaling |r⟂​(w)|=O​(dist​(w,ℳvol))|r^{\perp}(w)|=O(\mathrm{dist}(w,\mathcal{M}\_{\mathrm{vol}})) and the constant LrL\_{r} cannot, in general, be improved under the sole assumption ([43](https://arxiv.org/html/2511.17304v1#A1.E43 "In A.5 Proof of Proposition 4 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

##### Extension to non-Euclidean penalties (informal).

In the main text we focus on the Euclidean penalty ([42](https://arxiv.org/html/2511.17304v1#A1.E42 "In item 3 ‣ A.5 Proof of Proposition 4 ‣ Appendix A Proofs for Section 2: Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). If instead ℒvol\mathcal{L}\_{\mathrm{vol}} is defined via a strictly convex norm ∥⋅∥ϕ\|\cdot\|\_{\phi} or a strongly convex gauge ϕ\phi, i.e.,

|  |  |  |
| --- | --- | --- |
|  | ℒvolϕ​(w):=12​distϕ2​(w,ℳvol),distϕ​(w,ℳvol):=infw~∈ℳvol‖w−w~‖ϕ,\mathcal{L}\_{\mathrm{vol}}^{\phi}(w):=\frac{1}{2}\,\mathrm{dist}\_{\phi}^{2}(w,\mathcal{M}\_{\mathrm{vol}}),\qquad\mathrm{dist}\_{\phi}(w,\mathcal{M}\_{\mathrm{vol}}):=\inf\_{\tilde{w}\in\mathcal{M}\_{\mathrm{vol}}}\|w-\tilde{w}\|\_{\phi}, |  |

and rr is LrϕL\_{r}^{\phi}-Lipschitz with respect to ∥⋅∥ϕ\|\cdot\|\_{\phi}, the same argument yields

|  |  |  |
| --- | --- | --- |
|  | |r⟂​(w)|≤Lrϕ​distϕ​(w,ℳvol)=Lrϕ​2​ℒvolϕ​(w).|r^{\perp}(w)|\leq L\_{r}^{\phi}\,\mathrm{dist}\_{\phi}(w,\mathcal{M}\_{\mathrm{vol}})=L\_{r}^{\phi}\sqrt{2\,\mathcal{L}\_{\mathrm{vol}}^{\phi}(w)}. |  |

In finite dimensions, norm equivalence further implies that such bounds can be translated between different choices of ϕ\phi at the expense of multiplicative constants depending only on the norms;We keep the Euclidean version in Proposition [4](https://arxiv.org/html/2511.17304v1#Thmproposition4 "Proposition 4 (Ghost reward bounded by law distance). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") as it is the one used in our experiments.

This concludes the proof.
∎

## Appendix B Proofs for Section 3: Volatility World Model

### B.1 Proof of Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

We now provide a detailed measure-theoretic proof of Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

Recall the statement:

###### Proposition (Support of the synthetic generator).

Let (wt)t=0T(w\_{t})\_{t=0}^{T} be generated by G⋆G^{\star} as above, with static no-arbitrage imposed at each time via projection onto ℳvol\mathcal{M}\_{\mathrm{vol}}. Then

|  |  |  |
| --- | --- | --- |
|  | supp​ℙ⋆⊆(ℳvol)T+1,\mathrm{supp}\,\mathbb{P}^{\star}\subseteq\big(\mathcal{M}\_{\mathrm{vol}}\big)^{T+1}, |  |

i.e., ℙ⋆\mathbb{P}^{\star} is supported on the product of the volatility law manifold at all times.

###### Proof.

We first recall the construction of the synthetic generator G⋆G^{\star} from the main text and make it explicit in measure-theoretic terms.

##### Step 0: Probability space and random paths.

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be an underlying probability space supporting all driving randomness (e.g., Brownian motions, volatility factors, etc.) of the stochastic-volatility model used to generate “raw” option prices or total-variance surfaces.

For each t=0,…,Tt=0,\dots,T, let

|  |  |  |
| --- | --- | --- |
|  | yt:Ω→ℝdvoly\_{t}:\Omega\to\mathbb{R}^{d\_{\mathrm{vol}}} |  |

denote the *raw* (not yet projected) total-variance surface at time tt, obtained from the chosen parametric or factor model (Heston, rough volatility, SVI parameter dynamics, etc.; see, e.g., BayerFrizGatheral2016 [[9](https://arxiv.org/html/2511.17304v1#bib.bib9), [8](https://arxiv.org/html/2511.17304v1#bib.bib8)]). We assume that each yty\_{t} is Borel measurable.

The *law-consistent synthetic generator* G⋆G^{\star} then applies the projection onto the volatility law manifold ℳvol\mathcal{M}\_{\mathrm{vol}} at each time tt:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt​(ω):=Πℳvol​(yt​(ω)),ω∈Ω,t=0,…,T.w\_{t}(\omega):=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}\bigl(y\_{t}(\omega)\bigr),\qquad\omega\in\Omega,\;t=0,\dots,T. |  | (45) |

Here Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} is the Euclidean projection operator introduced in Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), which maps ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}} into ℳvol\mathcal{M}\_{\mathrm{vol}}.

We then define the (T+1)(T+1)-dimensional random vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(ω):=(w0​(ω),…,wT​(ω))∈(ℝdvol)T+1.W(\omega):=\bigl(w\_{0}(\omega),\dots,w\_{T}(\omega)\bigr)\in\big(\mathbb{R}^{d\_{\mathrm{vol}}}\bigr)^{T+1}. |  | (46) |

By construction, WW is Borel measurable, and we denote its law by

|  |  |  |
| --- | --- | --- |
|  | ℙ⋆:=ℙ∘W−1,\mathbb{P}^{\star}:=\mathbb{P}\circ W^{-1}, |  |

a probability measure on (ℝdvol)T+1\big(\mathbb{R}^{d\_{\mathrm{vol}}}\bigr)^{T+1}.

##### Step 1: Pointwise inclusion wt​(ω)∈ℳvolw\_{t}(\omega)\in\mathcal{M}\_{\mathrm{vol}} almost surely.

By Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), ℳvol\mathcal{M}\_{\mathrm{vol}} is non-empty, closed, and convex, and the projection Πℳvol:ℝdvol→ℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}}:\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathcal{M}\_{\mathrm{vol}} is well-defined and single-valued. In particular,

|  |  |  |
| --- | --- | --- |
|  | Πℳvol​(x)∈ℳvolfor all ​x∈ℝdvol.\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(x)\in\mathcal{M}\_{\mathrm{vol}}\quad\text{for all }x\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  |

Applying this to x=yt​(ω)x=y\_{t}(\omega), the definition ([45](https://arxiv.org/html/2511.17304v1#A2.E45 "In Step 0: Probability space and random paths. ‣ B.1 Proof of Proposition 5 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) implies that for every ω∈Ω\omega\in\Omega and every tt,

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt​(ω)∈ℳvol.w\_{t}(\omega)\in\mathcal{M}\_{\mathrm{vol}}. |  | (47) |

Thus, for each fixed tt, we have

|  |  |  |
| --- | --- | --- |
|  | ℙ​(wt∈ℳvol)=1.\mathbb{P}\bigl(w\_{t}\in\mathcal{M}\_{\mathrm{vol}}\bigr)=1. |  |

##### Step 2: Product inclusion for the path WW.

Using ([47](https://arxiv.org/html/2511.17304v1#A2.E47 "In Step 1: Pointwise inclusion 𝑤_𝑡⁢(𝜔)∈ℳᵥₒₗ almost surely. ‣ B.1 Proof of Proposition 5 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) for all t=0,…,Tt=0,\dots,T, we obtain

|  |  |  |
| --- | --- | --- |
|  | W​(ω)=(w0​(ω),…,wT​(ω))∈ℳvolT+1for all ​ω∈Ω.W(\omega)=(w\_{0}(\omega),\dots,w\_{T}(\omega))\in\mathcal{M}\_{\mathrm{vol}}^{T+1}\quad\text{for all }\omega\in\Omega. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(W∈ℳvolT+1)=1.\mathbb{P}\bigl(W\in\mathcal{M}\_{\mathrm{vol}}^{T+1}\bigr)=1. |  | (48) |

This already implies that the support of ℙ⋆\mathbb{P}^{\star} (the law of WW) must lie inside ℳvolT+1\mathcal{M}\_{\mathrm{vol}}^{T+1}. To make this precise, we recall the definition of support.

##### Step 3: Support of a probability measure and restriction to ℳvolT+1\mathcal{M}\_{\mathrm{vol}}^{T+1}.

Let (E,ℰ)(E,\mathcal{E}) be a measurable space, and μ\mu a probability measure on EE. The *support* of μ\mu, denoted supp⁡μ\operatorname{supp}\,\mu, is the closed set

|  |  |  |
| --- | --- | --- |
|  | supp⁡μ:={x∈E:μ​(U)>0​ for every open neighborhood ​U​ of ​x}.\operatorname{supp}\,\mu:=\bigl\{x\in E:\mu\bigl(U\bigr)>0\text{ for every open neighborhood }U\text{ of }x\bigr\}. |  |

We will use the following standard lemma.

###### Lemma 4 (Support of a measure carried by a closed set).

Let EE be a metric space, and let C⊆EC\subseteq E be a closed set. Suppose μ\mu is a Borel probability measure on EE such that μ​(C)=1\mu(C)=1. Then

|  |  |  |
| --- | --- | --- |
|  | supp⁡μ⊆C.\operatorname{supp}\,\mu\subseteq C. |  |

###### Proof of Lemma [4](https://arxiv.org/html/2511.17304v1#Thmlemma4 "Lemma 4 (Support of a measure carried by a closed set). ‣ Step 3: Support of a probability measure and restriction to ℳᵥₒₗ^{𝑇+1}. ‣ B.1 Proof of Proposition 5 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

Let x∈supp⁡μx\in\operatorname{supp}\,\mu. Suppose, for contradiction, that x∉Cx\notin C. Since CC is closed, its complement C∁C^{\complement} is open and contains xx. Thus there exists an open neighborhood UU of xx with U⊆C∁U\subseteq C^{\complement}. Then

|  |  |  |
| --- | --- | --- |
|  | μ​(U)≤μ​(C∁)=1−μ​(C)=0,\mu(U)\leq\mu(C^{\complement})=1-\mu(C)=0, |  |

contradicting the definition of support, which requires μ​(U)>0\mu(U)>0 for every open neighborhood UU of xx. Hence x∈Cx\in C. Since x∈supp⁡μx\in\operatorname{supp}\,\mu was arbitrary, we conclude supp⁡μ⊆C\operatorname{supp}\,\mu\subseteq C.
∎

##### Step 4: Applying the lemma to ℙ⋆\mathbb{P}^{\star} and ℳvolT+1\mathcal{M}\_{\mathrm{vol}}^{T+1}.

We now take E=(ℝdvol)T+1E=\big(\mathbb{R}^{d\_{\mathrm{vol}}}\bigr)^{T+1}, equipped with its usual product topology and Borel σ\sigma-algebra. The set ℳvol\mathcal{M}\_{\mathrm{vol}} is closed in ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}} by Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), hence ℳvolT+1\mathcal{M}\_{\mathrm{vol}}^{T+1} is closed in the product topology of EE. By ([48](https://arxiv.org/html/2511.17304v1#A2.E48 "In Step 2: Product inclusion for the path 𝑊. ‣ B.1 Proof of Proposition 5 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),

|  |  |  |
| --- | --- | --- |
|  | ℙ⋆​(ℳvolT+1)=ℙ​(W∈ℳvolT+1)=1.\mathbb{P}^{\star}\bigl(\mathcal{M}\_{\mathrm{vol}}^{T+1}\bigr)=\mathbb{P}\bigl(W\in\mathcal{M}\_{\mathrm{vol}}^{T+1}\bigr)=1. |  |

Applying Lemma [4](https://arxiv.org/html/2511.17304v1#Thmlemma4 "Lemma 4 (Support of a measure carried by a closed set). ‣ Step 3: Support of a probability measure and restriction to ℳᵥₒₗ^{𝑇+1}. ‣ B.1 Proof of Proposition 5 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") with C=ℳvolT+1C=\mathcal{M}\_{\mathrm{vol}}^{T+1} and μ=ℙ⋆\mu=\mathbb{P}^{\star} yields

|  |  |  |
| --- | --- | --- |
|  | supp⁡ℙ⋆⊆ℳvolT+1.\operatorname{supp}\,\mathbb{P}^{\star}\subseteq\mathcal{M}\_{\mathrm{vol}}^{T+1}. |  |

This is exactly the claim of Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"):

|  |  |  |
| --- | --- | --- |
|  | supp​ℙ⋆⊆(ℳvol)T+1.\mathrm{supp}\,\mathbb{P}^{\star}\subseteq\big(\mathcal{M}\_{\mathrm{vol}}\big)^{T+1}. |  |

##### Step 5: Interpretation.

From a modelling standpoint, the proposition formalizes the claim that the synthetic generator G⋆G^{\star} produces only paths of total-variance surfaces (wt)t=0T(w\_{t})\_{t=0}^{T} that are *everywhere law-consistent*, in the sense of lying on the volatility law manifold at each time. The law ℙ⋆\mathbb{P}^{\star} of the generated paths is therefore entirely concentrated on the set ℳvolT+1\mathcal{M}\_{\mathrm{vol}}^{T+1} of sequences of admissible surfaces. This is the precise sense in which we refer to G⋆G^{\star} as a “law-consistent ground-truth world” in the main text.

This completes the proof.
∎

### B.2 Proof of Proposition [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

In this subsection we provide a detailed proof of Proposition [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), making precise the local linearization and the cone decomposition used in the main text.

Recall the setting: for each time step tt, the law-consistent generator G⋆G^{\star} produces wt+1∈ℳvolw\_{t+1}\in\mathcal{M}\_{\mathrm{vol}} almost surely (Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), the world model produces a prediction

|  |  |  |
| --- | --- | --- |
|  | w^t+1=fθ​(w≤t,a≤t)∈ℝdvol,\hat{w}\_{t+1}=f\_{\theta}(w\_{\leq t},a\_{\leq t})\in\mathbb{R}^{d\_{\mathrm{vol}}}, |  |

and the residual is

|  |  |  |
| --- | --- | --- |
|  | et+1:=w^t+1−wt+1.e\_{t+1}:=\hat{w}\_{t+1}-w\_{t+1}. |  |

We denote by wt+1ℳ:=Πℳvol​(w^t+1)w\_{t+1}^{\mathcal{M}}:=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{w}\_{t+1}) the projection of the prediction onto the volatility law manifold. The *ghost reward* at time t+1t+1 is

|  |  |  |
| --- | --- | --- |
|  | rt+1⟂:=r​(w^t+1,at)−r​(wt+1ℳ,at),r^{\perp}\_{t+1}:=r(\hat{w}\_{t+1},a\_{t})-r(w\_{t+1}^{\mathcal{M}},a\_{t}), |  |

where r​(⋅,at)r(\cdot,a\_{t}) is the one-step reward as a function of the surface ww for a fixed action ata\_{t}.

We restate the proposition for convenience.

###### Proposition 8 (Approximation gap induces a ghost channel).

Suppose the following conditions hold:

1. (i)

   The approximation gap is non-zero:

   |  |  |  |
   | --- | --- | --- |
   |  | ε2:=𝔼​[‖et+1‖22]>0.\varepsilon^{2}:=\mathbb{E}\big[\|e\_{t+1}\|\_{2}^{2}\big]>0. |  |
2. (ii)

   The reward is locally differentiable in ww with gradient

   |  |  |  |
   | --- | --- | --- |
   |  | gt+1:=∇wr​(wt+1,at),g\_{t+1}:=\nabla\_{w}r(w\_{t+1},a\_{t}), |  |

   and ∇wr​(⋅,at)\nabla\_{w}r(\cdot,a\_{t}) is locally Lipschitz in a neighborhood of the law-consistent path.
3. (iii)

   The residual et+1e\_{t+1} has a component in the normal cone of ℳvol\mathcal{M}\_{\mathrm{vol}} at wt+1w\_{t+1} with non-zero covariance with the gradient:

   |  |  |  |
   | --- | --- | --- |
   |  | Cov​(PNℳvol​(wt+1)​et+1,gt+1)≠0,\mathrm{Cov}\big(P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1},\,g\_{t+1}\big)\neq 0, |  |

   where PNℳvol​(wt+1)P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})} denotes orthogonal projection onto the normal cone Nℳvol​(wt+1)N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1}).

Then, for sufficiently small residuals (in the sense of a local linearization),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[rt+1⟂]≈𝔼​[gt+1⊤​PNℳvol​(wt+1)​et+1]≠0,\mathbb{E}\big[r^{\perp}\_{t+1}\big]\approx\mathbb{E}\big[g\_{t+1}^{\top}P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}\big]\neq 0, |  |

so the world model induces a non-trivial ghost channel. In particular, if gt+1g\_{t+1} is positively correlated with PNℳvol​(wt+1)​et+1P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}, then 𝔼​[rt+1⟂]>0\mathbb{E}[r^{\perp}\_{t+1}]>0 and there exist states where moving off-manifold strictly improves expected P&L.

###### Proof.

We work under the law-consistent measure ℙ⋆\mathbb{P}^{\star} of the generator G⋆G^{\star}, under which wt+1∈ℳvolw\_{t+1}\in\mathcal{M}\_{\mathrm{vol}} almost surely (Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). We suppress the explicit dependence on tt when it does not create ambiguity.

##### Step 1: Local Taylor expansion of the reward.

Fix a compact set K⊂ℝdvolK\subset\mathbb{R}^{d\_{\mathrm{vol}}} containing the realized wt+1w\_{t+1} and all admissible w^t+1\hat{w}\_{t+1} and wt+1ℳw\_{t+1}^{\mathcal{M}} with high probability (a standard truncation argument; see below). By assumption (ii), for each fixed ata\_{t}, the map

|  |  |  |
| --- | --- | --- |
|  | r​(⋅,at):ℝdvol→ℝr(\cdot,a\_{t}):\mathbb{R}^{d\_{\mathrm{vol}}}\to\mathbb{R} |  |

is differentiable on KK, with gradient ∇wr​(⋅,at)\nabla\_{w}r(\cdot,a\_{t}) locally Lipschitz.

Hence, by the mean value theorem in Banach spaces, for each ω∈Ω\omega\in\Omega we can write

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | r​(w^t+1,at)\displaystyle r(\hat{w}\_{t+1},a\_{t}) | =r​(wt+1,at)+gt+1⊤​et+1+ρt+1(1),\displaystyle=r(w\_{t+1},a\_{t})+g\_{t+1}^{\top}e\_{t+1}+\rho\_{t+1}^{(1)}, |  | (49) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | r​(wt+1ℳ,at)\displaystyle r(w\_{t+1}^{\mathcal{M}},a\_{t}) | =r​(wt+1,at)+gt+1⊤​(wt+1ℳ−wt+1)+ρt+1(2),\displaystyle=r(w\_{t+1},a\_{t})+g\_{t+1}^{\top}(w\_{t+1}^{\mathcal{M}}-w\_{t+1})+\rho\_{t+1}^{(2)}, |  | (50) |

where the remainder terms satisfy the quadratic bounds

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ρt+1(1)|\displaystyle|\rho\_{t+1}^{(1)}| | ≤L∇r2​‖et+1‖22,\displaystyle\leq\tfrac{L\_{\nabla r}}{2}\|e\_{t+1}\|\_{2}^{2}, |  | (51) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ρt+1(2)|\displaystyle|\rho\_{t+1}^{(2)}| | ≤L∇r2​‖wt+1ℳ−wt+1‖22,\displaystyle\leq\tfrac{L\_{\nabla r}}{2}\|w\_{t+1}^{\mathcal{M}}-w\_{t+1}\|\_{2}^{2}, |  | (52) |

for some local Lipschitz constant L∇r>0L\_{\nabla r}>0 depending only on KK and ata\_{t}.

Subtracting ([50](https://arxiv.org/html/2511.17304v1#A2.E50 "In Step 1: Local Taylor expansion of the reward. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) from ([49](https://arxiv.org/html/2511.17304v1#A2.E49 "In Step 1: Local Taylor expansion of the reward. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1⟂=gt+1⊤​(et+1−(wt+1ℳ−wt+1))+(ρt+1(1)−ρt+1(2)).r^{\perp}\_{t+1}=g\_{t+1}^{\top}\Big(e\_{t+1}-(w\_{t+1}^{\mathcal{M}}-w\_{t+1})\Big)+\big(\rho\_{t+1}^{(1)}-\rho\_{t+1}^{(2)}\big). |  | (53) |

##### Step 2: Tangent–normal cone decomposition of the residual.

Since wt+1∈ℳvolw\_{t+1}\in\mathcal{M}\_{\mathrm{vol}} and ℳvol\mathcal{M}\_{\mathrm{vol}} is closed and convex (Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we may consider the tangent cone Tℳvol​(wt+1)T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1}) and the normal cone Nℳvol​(wt+1)N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Tℳvol​(wt+1)\displaystyle T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1}) | :=⋃α>0α​(ℳvol−wt+1)¯,\displaystyle:=\overline{\bigcup\_{\alpha>0}\alpha\,(\mathcal{M}\_{\mathrm{vol}}-w\_{t+1})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Nℳvol​(wt+1)\displaystyle N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1}) | :={v∈ℝdvol:v⊤​(z−wt+1)≤0​∀z∈ℳvol}.\displaystyle:=\{v\in\mathbb{R}^{d\_{\mathrm{vol}}}:v^{\top}(z-w\_{t+1})\leq 0\ \forall z\in\mathcal{M}\_{\mathrm{vol}}\}. |  |

Both are closed convex cones, and they are polar to each other:

|  |  |  |
| --- | --- | --- |
|  | Nℳvol​(wt+1)=Tℳvol​(wt+1)∘,Tℳvol​(wt+1)=Nℳvol​(wt+1)∘.N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})=T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})^{\circ},\qquad T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})=N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})^{\circ}. |  |

By the Moreau decomposition for closed convex cones (see, e.g., BauschkeCombettes2011 [[26](https://arxiv.org/html/2511.17304v1#bib.bib26), Thm. 6.29]), every vector z∈ℝdvolz\in\mathbb{R}^{d\_{\mathrm{vol}}} admits a unique decomposition

|  |  |  |
| --- | --- | --- |
|  | z=PTℳvol​(wt+1)​z+PNℳvol​(wt+1)​z,z=P\_{T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}z+P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}z, |  |

where PTP\_{T} and PNP\_{N} denote the orthogonal projections onto Tℳvol​(wt+1)T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1}) and Nℳvol​(wt+1)N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1}), respectively.

Applying this to et+1e\_{t+1}, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | et+1=et+1tan+et+1norm,et+1tan:=PTℳvol​(wt+1)​et+1,et+1norm:=PNℳvol​(wt+1)​et+1.e\_{t+1}=e\_{t+1}^{\mathrm{tan}}+e\_{t+1}^{\mathrm{norm}},\qquad e\_{t+1}^{\mathrm{tan}}:=P\_{T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1},\;e\_{t+1}^{\mathrm{norm}}:=P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}. |  | (54) |

##### Step 3: Local behavior of the projection Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}}.

We next relate wt+1ℳw\_{t+1}^{\mathcal{M}} to wt+1w\_{t+1} and et+1e\_{t+1}.

By definition,

|  |  |  |
| --- | --- | --- |
|  | wt+1ℳ=Πℳvol​(w^t+1)=arg⁡minz∈ℳvol⁡‖w^t+1−z‖22.w\_{t+1}^{\mathcal{M}}=\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{w}\_{t+1})=\arg\min\_{z\in\mathcal{M}\_{\mathrm{vol}}}\|\hat{w}\_{t+1}-z\|\_{2}^{2}. |  |

Since wt+1∈ℳvolw\_{t+1}\in\mathcal{M}\_{\mathrm{vol}}, for small ‖et+1‖2\|e\_{t+1}\|\_{2} the minimizer wt+1ℳw\_{t+1}^{\mathcal{M}} lies in a neighborhood where ℳvol\mathcal{M}\_{\mathrm{vol}} is locally well-approximated by its tangent cone at wt+1w\_{t+1}. Under a standard regularity condition (e.g., wt+1w\_{t+1} is a point of *prox-regularity* of ℳvol\mathcal{M}\_{\mathrm{vol}}; ), the projection mapping Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} is directionally differentiable at wt+1w\_{t+1} and its first-order behavior is given by orthogonal projection onto the tangent cone:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt+1ℳ−wt+1=PTℳvol​(wt+1)​et+1+δt+1,w\_{t+1}^{\mathcal{M}}-w\_{t+1}=P\_{T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}+\delta\_{t+1}, |  | (55) |

where the remainder δt+1\delta\_{t+1} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖δt+1‖2≤CΠ​‖et+1‖22\|\delta\_{t+1}\|\_{2}\leq C\_{\Pi}\|e\_{t+1}\|\_{2}^{2} |  | (56) |

for some constant CΠ>0C\_{\Pi}>0 in a neighborhood of wt+1w\_{t+1}. Intuitively, to first order, Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} keeps the tangential component of et+1e\_{t+1} but kills the normal component; the error δt+1\delta\_{t+1} is of second order in ‖et+1‖2\|e\_{t+1}\|\_{2}.

Substituting ([55](https://arxiv.org/html/2511.17304v1#A2.E55 "In Step 3: Local behavior of the projection Π_ℳᵥₒₗ. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) into ([53](https://arxiv.org/html/2511.17304v1#A2.E53 "In Step 1: Local Taylor expansion of the reward. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and using ([54](https://arxiv.org/html/2511.17304v1#A2.E54 "In Step 2: Tangent–normal cone decomposition of the residual. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1⟂\displaystyle r^{\perp}\_{t+1} | =gt+1⊤​(et+1−(wt+1ℳ−wt+1))+(ρt+1(1)−ρt+1(2))\displaystyle=g\_{t+1}^{\top}\big(e\_{t+1}-(w\_{t+1}^{\mathcal{M}}-w\_{t+1})\big)+\big(\rho\_{t+1}^{(1)}-\rho\_{t+1}^{(2)}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =gt+1⊤​(et+1tan+et+1norm−PTℳvol​(wt+1)​et+1−δt+1)+(ρt+1(1)−ρt+1(2))\displaystyle=g\_{t+1}^{\top}\big(e\_{t+1}^{\mathrm{tan}}+e\_{t+1}^{\mathrm{norm}}-P\_{T\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}-\delta\_{t+1}\big)+\big(\rho\_{t+1}^{(1)}-\rho\_{t+1}^{(2)}\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =gt+1⊤​et+1norm−gt+1⊤​δt+1+(ρt+1(1)−ρt+1(2)).\displaystyle=g\_{t+1}^{\top}e\_{t+1}^{\mathrm{norm}}-g\_{t+1}^{\top}\delta\_{t+1}+\big(\rho\_{t+1}^{(1)}-\rho\_{t+1}^{(2)}\big). |  | (57) |

##### Step 4: Bounding the higher-order error.

We now bound the total remainder term

|  |  |  |
| --- | --- | --- |
|  | ηt+1:=−gt+1⊤​δt+1+(ρt+1(1)−ρt+1(2)).\eta\_{t+1}:=-g\_{t+1}^{\top}\delta\_{t+1}+\big(\rho\_{t+1}^{(1)}-\rho\_{t+1}^{(2)}\big). |  |

Using Cauchy–Schwarz, ([56](https://arxiv.org/html/2511.17304v1#A2.E56 "In Step 3: Local behavior of the projection Π_ℳᵥₒₗ. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), and the boundedness of gt+1g\_{t+1} on KK (say ‖gt+1‖2≤G\|g\_{t+1}\|\_{2}\leq G almost surely on KK), we have

|  |  |  |
| --- | --- | --- |
|  | |gt+1⊤​δt+1|≤‖gt+1‖2​‖δt+1‖2≤G​CΠ​‖et+1‖22.|g\_{t+1}^{\top}\delta\_{t+1}|\leq\|g\_{t+1}\|\_{2}\|\delta\_{t+1}\|\_{2}\leq GC\_{\Pi}\|e\_{t+1}\|\_{2}^{2}. |  |

Combining this with ([51](https://arxiv.org/html/2511.17304v1#A2.E51 "In Step 1: Local Taylor expansion of the reward. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and ([52](https://arxiv.org/html/2511.17304v1#A2.E52 "In Step 1: Local Taylor expansion of the reward. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), and using ‖wt+1ℳ−wt+1‖2≤‖et+1‖2\|w\_{t+1}^{\mathcal{M}}-w\_{t+1}\|\_{2}\leq\|e\_{t+1}\|\_{2} (since wt+1ℳw\_{t+1}^{\mathcal{M}} is the closest point in ℳvol\mathcal{M}\_{\mathrm{vol}} to w^t+1\hat{w}\_{t+1} and wt+1∈ℳvolw\_{t+1}\in\mathcal{M}\_{\mathrm{vol}}), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ηt+1|≤Ctot​‖et+1‖22|\eta\_{t+1}|\leq C\_{\mathrm{tot}}\|e\_{t+1}\|\_{2}^{2} |  | (58) |

for some constant Ctot>0C\_{\mathrm{tot}}>0.

Substituting ([57](https://arxiv.org/html/2511.17304v1#A2.E57 "In Step 3: Local behavior of the projection Π_ℳᵥₒₗ. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and taking expectations yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[rt+1⟂]=𝔼​[gt+1⊤​et+1norm]+𝔼​[ηt+1],\mathbb{E}[r^{\perp}\_{t+1}]=\mathbb{E}\big[g\_{t+1}^{\top}e\_{t+1}^{\mathrm{norm}}\big]+\mathbb{E}[\eta\_{t+1}], |  | (59) |

with |𝔼​[ηt+1]|≤Ctot​𝔼​[‖et+1‖22]=Ctot​ε2|\mathbb{E}[\eta\_{t+1}]|\leq C\_{\mathrm{tot}}\mathbb{E}[\|e\_{t+1}\|\_{2}^{2}]=C\_{\mathrm{tot}}\varepsilon^{2} by assumption (i).

##### Step 5: Non-trivial ghost channel from covariance structure.

By definition of et+1norme\_{t+1}^{\mathrm{norm}} in ([54](https://arxiv.org/html/2511.17304v1#A2.E54 "In Step 2: Tangent–normal cone decomposition of the residual. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we have

|  |  |  |
| --- | --- | --- |
|  | et+1norm=PNℳvol​(wt+1)​et+1.e\_{t+1}^{\mathrm{norm}}=P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}. |  |

Assumption (iii) states that the covariance

|  |  |  |
| --- | --- | --- |
|  | Cov​(et+1norm,gt+1)=𝔼​[(et+1norm−𝔼​[et+1norm])​(gt+1−𝔼​[gt+1])⊤]\mathrm{Cov}\big(e\_{t+1}^{\mathrm{norm}},g\_{t+1}\big)=\mathbb{E}\Big[\big(e\_{t+1}^{\mathrm{norm}}-\mathbb{E}[e\_{t+1}^{\mathrm{norm}}]\big)\big(g\_{t+1}-\mathbb{E}[g\_{t+1}]\big)^{\top}\Big] |  |

is non-zero. In particular, the scalar random variable

|  |  |  |
| --- | --- | --- |
|  | Zt+1:=gt+1⊤​et+1normZ\_{t+1}:=g\_{t+1}^{\top}e\_{t+1}^{\mathrm{norm}} |  |

has non-zero covariance with itself along at least one direction, implying that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Zt+1]=𝔼​[gt+1⊤​et+1norm]≠0\mathbb{E}[Z\_{t+1}]=\mathbb{E}\big[g\_{t+1}^{\top}e\_{t+1}^{\mathrm{norm}}\big]\neq 0 |  | (60) |

unless the mean terms 𝔼​[et+1norm]\mathbb{E}[e\_{t+1}^{\mathrm{norm}}] and 𝔼​[gt+1]\mathbb{E}[g\_{t+1}] are tuned to perfectly cancel the covariance contribution; this would be an exceptional, measure-zero configuration in parameter space. To avoid such pathological cancellation, we interpret assumption (iii) as requiring that the inner product gt+1⊤​et+1normg\_{t+1}^{\top}e\_{t+1}^{\mathrm{norm}} has a non-degenerate distribution with non-zero mean.444Formally, one may replace the covariance condition in assumption (iii) by the simpler requirement 𝔼​[gt+1⊤​PNℳvol​(wt+1)​et+1]≠0\mathbb{E}[g\_{t+1}^{\top}P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}]\neq 0. We keep the covariance phrasing to emphasize the geometric correlation between the gradient and the normal component.

Substituting ([60](https://arxiv.org/html/2511.17304v1#A2.E60 "In Step 5: Non-trivial ghost channel from covariance structure. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) into ([59](https://arxiv.org/html/2511.17304v1#A2.E59 "In Step 4: Bounding the higher-order error. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[rt+1⟂]=𝔼​[gt+1⊤​PNℳvol​(wt+1)​et+1]+𝔼​[ηt+1],\mathbb{E}[r^{\perp}\_{t+1}]=\mathbb{E}\big[g\_{t+1}^{\top}P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}\big]+\mathbb{E}[\eta\_{t+1}], |  | (61) |

with 𝔼​[ηt+1]\mathbb{E}[\eta\_{t+1}] bounded by ([58](https://arxiv.org/html/2511.17304v1#A2.E58 "In Step 4: Bounding the higher-order error. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

##### Step 6: Small-residual regime and sign of the ghost reward.

Assumption (i) states that the world model approximation error is non-zero in mean-square:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖et+1‖22]=ε2>0.\mathbb{E}[\|e\_{t+1}\|\_{2}^{2}]=\varepsilon^{2}>0. |  |

Suppose in addition that the training of the world model has reduced the error variance so that ε2\varepsilon^{2} is *small*. Then from ([58](https://arxiv.org/html/2511.17304v1#A2.E58 "In Step 4: Bounding the higher-order error. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[ηt+1]|≤Ctot​ε2,|\mathbb{E}[\eta\_{t+1}]|\leq C\_{\mathrm{tot}}\varepsilon^{2}, |  |

which can be made arbitrarily small by improving the world model (e.g., increasing capacity or training time), while the leading term

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[gt+1⊤​PNℳvol​(wt+1)​et+1]\mathbb{E}\big[g\_{t+1}^{\top}P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}\big] |  |

remains of order ε\varepsilon in general, as it is linear in et+1e\_{t+1}.

Consequently, for sufficiently small ε\varepsilon we have the first-order approximation

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[rt+1⟂]≈𝔼​[gt+1⊤​PNℳvol​(wt+1)​et+1],\mathbb{E}[r^{\perp}\_{t+1}]\approx\mathbb{E}\big[g\_{t+1}^{\top}P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}\big], |  |

with the difference bounded by O​(ε2)O(\varepsilon^{2}). Under the non-degeneracy condition in ([60](https://arxiv.org/html/2511.17304v1#A2.E60 "In Step 5: Non-trivial ghost channel from covariance structure. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), this leading term is non-zero, which yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[rt+1⟂]≠0\mathbb{E}[r^{\perp}\_{t+1}]\neq 0 |  |

for sufficiently small approximation error ε\varepsilon.

Finally, if the correlation between gt+1g\_{t+1} and PNℳvol​(wt+1)​et+1P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1} is *positive* in the sense that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[gt+1⊤​PNℳvol​(wt+1)​et+1]>0,\mathbb{E}\big[g\_{t+1}^{\top}P\_{N\_{\mathcal{M}\_{\mathrm{vol}}}(w\_{t+1})}e\_{t+1}\big]>0, |  |

then ([61](https://arxiv.org/html/2511.17304v1#A2.E61 "In Step 5: Non-trivial ghost channel from covariance structure. ‣ B.2 Proof of Proposition 6 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) implies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[rt+1⟂]>0\mathbb{E}[r^{\perp}\_{t+1}]>0 |  |

for sufficiently small ε\varepsilon. In particular, there exists a set of states of positive probability where rt+1⟂>0r^{\perp}\_{t+1}>0, so moving off the volatility law manifold along the normal directions strictly increases expected one-step P&L. This is precisely the “ghost channel” exploited by naive RL and law-seeking RL in the main text.

This completes the proof.
∎

### B.3 Proof of Lemma [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

In this subsection we give a more detailed argument for Lemma [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), making precise the informal statement in the main text that a finite-capacity, unconstrained neural world model will, under mild regularity conditions, place non-trivial probability mass off the volatility law manifold.

Recall the statement.

###### Lemma (Non-trivial off-manifold mass of the world model).

Assume that fθ⋆f\_{\theta^{\star}} is not exactly equal to the Bayes-optimal regressor fBayes​(xt):=𝔼​[wt+1|xt]f^{\mathrm{Bayes}}(x\_{t}):=\mathbb{E}[w\_{t+1}\,|\,x\_{t}] and that the law manifold ℳvol\mathcal{M}^{\mathrm{vol}} has non-empty interior within the support of wt+1w\_{t+1}. Then there exists δ>0\delta>0 such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℒϕ​(w^t+1)>δ)>0,\mathbb{P}\big(\mathcal{L}\_{\phi}(\hat{w}\_{t+1})>\delta\big)>0, |  |

i.e., the world model assigns non-zero probability mass to surfaces at a positive distance from ℳvol\mathcal{M}^{\mathrm{vol}}.

##### Setup and additional regularity.

Let XtX\_{t} denote the (vector) state at time tt and Wt+1:=wt+1W\_{t+1}:=w\_{t+1} the total-variance surface generated by the law-consistent generator G⋆G^{\star} at time t+1t+1. We write

|  |  |  |
| --- | --- | --- |
|  | fBayes​(x):=𝔼​[Wt+1∣Xt=x],W^t+1:=w^t+1:=fθ⋆​(Xt).f^{\mathrm{Bayes}}(x):=\mathbb{E}[W\_{t+1}\mid X\_{t}=x],\qquad\hat{W}\_{t+1}:=\hat{w}\_{t+1}:=f\_{\theta^{\star}}(X\_{t}). |  |

By Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and convexity of ℳvol\mathcal{M}\_{\mathrm{vol}}, we have

|  |  |  |
| --- | --- | --- |
|  | Wt+1∈ℳvol​a.s.⟹fBayes​(Xt)∈ℳvol​a.s.,W\_{t+1}\in\mathcal{M}\_{\mathrm{vol}}\ \text{a.s.}\qquad\Longrightarrow\qquad f^{\mathrm{Bayes}}(X\_{t})\in\mathcal{M}\_{\mathrm{vol}}\ \text{a.s.}, |  |

since conditional expectations of random variables supported on a closed convex set remain in that set.

We also recall from Proposition [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") that for any w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}},

|  |  |  |
| --- | --- | --- |
|  | ℒϕ​(w)=0⟺w∈ℳvol,\mathcal{L}\_{\phi}(w)=0\quad\Longleftrightarrow\quad w\in\mathcal{M}\_{\mathrm{vol}}, |  |

and from Lemma [1](https://arxiv.org/html/2511.17304v1#Thmlemma1 "Lemma 1 (Local Lipschitz continuity of law penalty). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") that ℒϕ\mathcal{L}\_{\phi} is continuous (indeed locally Lipschitz) on ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}.

To make the genericity argument precise, we introduce a mild regularity hypothesis on the joint distribution of (Xt,W^t+1)(X\_{t},\hat{W}\_{t+1}).

Regularity assumption (B.3).
We assume:

1. (a)

   The state XtX\_{t} has a distribution whose support supp⁡(Xt)\operatorname{supp}(X\_{t}) is not a single point and contains a non-empty open subset UX⊂ℝdXU\_{X}\subset\mathbb{R}^{d\_{X}}.
2. (b)

   The trained world model fθ⋆:ℝdX→ℝdvolf\_{\theta^{\star}}\colon\mathbb{R}^{d\_{X}}\to\mathbb{R}^{d\_{\mathrm{vol}}} is continuous on UXU\_{X} (this is satisfied by standard neural networks with continuous activations).
3. (c)

   The image fθ⋆​(UX)f\_{\theta^{\star}}(U\_{X}) is not contained in any (dvol−1)(d\_{\mathrm{vol}}-1)-dimensional affine subspace of ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}} (a genericity condition on the parameter choice θ⋆\theta^{\star}).

Assumption (B.3) is very mild in practice: for typical neural network parametrizations with random initialization and gradient-based training, the set of parameters for which fθf\_{\theta} maps UXU\_{X} into a fixed lower-dimensional affine subspace has Lebesgue measure zero in parameter space.

We now prove that, under the assumptions of Lemma [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and (B.3), the world model places non-trivial mass at positive distance from ℳvol\mathcal{M}\_{\mathrm{vol}}.

###### Proof.

Define the *distance-to-manifold* function

|  |  |  |
| --- | --- | --- |
|  | dℳvol​(w):=dist⁡(w,ℳvol)=infz∈ℳvol‖w−z‖2,w∈ℝdvol.d\_{\mathcal{M}\_{\mathrm{vol}}}(w):=\operatorname{dist}(w,\mathcal{M}\_{\mathrm{vol}})=\inf\_{z\in\mathcal{M}\_{\mathrm{vol}}}\|w-z\|\_{2},\qquad w\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  |

By closedness of ℳvol\mathcal{M}\_{\mathrm{vol}} (Proposition [2](https://arxiv.org/html/2511.17304v1#Thmproposition2 "Proposition 2 (Closedness, convexity, and metric projection). ‣ 2.2 Geometry and Convexity Properties ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), dℳvold\_{\mathcal{M}\_{\mathrm{vol}}} is continuous and

|  |  |  |
| --- | --- | --- |
|  | dℳvol​(w)=0⇔w∈ℳvol.d\_{\mathcal{M}\_{\mathrm{vol}}}(w)=0\iff w\in\mathcal{M}\_{\mathrm{vol}}. |  |

By Proposition [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), ℒϕ\mathcal{L}\_{\phi} and dℳvold\_{\mathcal{M}\_{\mathrm{vol}}} have the same zero set, and continuity of ℒϕ\mathcal{L}\_{\phi} implies that for every δ>0\delta>0 there exists η​(δ)>0\eta(\delta)>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | dℳvol​(w)>η​(δ)⟹ℒϕ​(w)>δ,∀w∈ℝdvol.d\_{\mathcal{M}\_{\mathrm{vol}}}(w)>\eta(\delta)\ \Longrightarrow\ \mathcal{L}\_{\phi}(w)>\delta,\qquad\forall w\in\mathbb{R}^{d\_{\mathrm{vol}}}. |  | (62) |

Thus it suffices to show that there exists η>0\eta>0 such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(dℳvol​(W^t+1)>η)>0.\mathbb{P}\big(d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})>\eta\big)>0. |  |

##### Step 1: Existence of a prediction point outside ℳvol\mathcal{M}\_{\mathrm{vol}}.

We first argue that, under our assumptions, the image of fθ⋆f\_{\theta^{\star}} cannot be contained in ℳvol\mathcal{M}\_{\mathrm{vol}}.

Suppose for contradiction that

|  |  |  |  |
| --- | --- | --- | --- |
|  | fθ⋆​(x)∈ℳvolfor all ​x∈supp⁡(Xt).f\_{\theta^{\star}}(x)\in\mathcal{M}\_{\mathrm{vol}}\quad\text{for all }x\in\operatorname{supp}(X\_{t}). |  | (63) |

In particular, for x∈supp⁡(Xt)x\in\operatorname{supp}(X\_{t}) we have W^t+1∈ℳvol\hat{W}\_{t+1}\in\mathcal{M}\_{\mathrm{vol}} almost surely and hence dℳvol​(W^t+1)=0d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})=0 and ℒϕ​(W^t+1)=0\mathcal{L}\_{\phi}(\hat{W}\_{t+1})=0 almost surely. This is exactly the negation of the lemma’s conclusion.

We now show that ([63](https://arxiv.org/html/2511.17304v1#A2.E63 "In Step 1: Existence of a prediction point outside ℳᵥₒₗ. ‣ B.3 Proof of Lemma 2 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) is incompatible with the combination of (i) fθ⋆≠fBayesf\_{\theta^{\star}}\neq f^{\mathrm{Bayes}} and (B.3), given that ℳvol\mathcal{M}\_{\mathrm{vol}} has non-empty interior within the support of Wt+1W\_{t+1}.

Because ℳvol\mathcal{M}\_{\mathrm{vol}} has non-empty interior and Wt+1W\_{t+1} is supported on ℳvol\mathcal{M}\_{\mathrm{vol}} (Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), there exists a point w∘∈ℳvolw^{\circ}\in\mathcal{M}\_{\mathrm{vol}} and r>0r>0 such that

|  |  |  |
| --- | --- | --- |
|  | B​(w∘,r):={w∈ℝdvol:‖w−w∘‖2<r}⊂ℳvolB(w^{\circ},r):=\{w\in\mathbb{R}^{d\_{\mathrm{vol}}}:\|w-w^{\circ}\|\_{2}<r\}\subset\mathcal{M}\_{\mathrm{vol}} |  |

and ℙ​(Wt+1∈B​(w∘,r))>0\mathbb{P}(W\_{t+1}\in B(w^{\circ},r))>0. Since fBayes​(Xt)=𝔼​[Wt+1∣Xt]f^{\mathrm{Bayes}}(X\_{t})=\mathbb{E}[W\_{t+1}\mid X\_{t}] takes values in the convex set ℳvol\mathcal{M}\_{\mathrm{vol}}, there exists x∘∈supp⁡(Xt)x^{\circ}\in\operatorname{supp}(X\_{t}) such that

|  |  |  |
| --- | --- | --- |
|  | fBayes​(x∘)∈B​(w∘,r/2)⊂int⁡(ℳvol).f^{\mathrm{Bayes}}(x^{\circ})\in B(w^{\circ},r/2)\subset\operatorname{int}(\mathcal{M}\_{\mathrm{vol}}). |  |

By the assumption fθ⋆≠fBayesf\_{\theta^{\star}}\neq f^{\mathrm{Bayes}} in L2​(ℙ)L^{2}(\mathbb{P}), there exists a set A⊂supp⁡(Xt)A\subset\operatorname{supp}(X\_{t}) with ℙ​(Xt∈A)>0\mathbb{P}(X\_{t}\in A)>0 such that

|  |  |  |
| --- | --- | --- |
|  | fθ⋆​(x)≠fBayes​(x)for all ​x∈A.f\_{\theta^{\star}}(x)\neq f^{\mathrm{Bayes}}(x)\quad\text{for all }x\in A. |  |

Under Assumption (B.3)(a)–(b), the support supp⁡(Xt)\operatorname{supp}(X\_{t}) contains an open set UXU\_{X} on which fθ⋆f\_{\theta^{\star}} is continuous, and we may without loss of generality assume that A∩UXA\cap U\_{X} has positive probability (otherwise we restrict attention to a smaller open subset with positive mass).

Pick x1∈A∩UXx\_{1}\in A\cap U\_{X} with fθ⋆​(x1)≠fBayes​(x1)f\_{\theta^{\star}}(x\_{1})\neq f^{\mathrm{Bayes}}(x\_{1}). Consider the continuous path in input space given by

|  |  |  |
| --- | --- | --- |
|  | γ​(α):=(1−α)​x∘+α​x1,α∈[0,1],\gamma(\alpha):=(1-\alpha)x^{\circ}+\alpha x\_{1},\qquad\alpha\in[0,1], |  |

which lies in UXU\_{X} since UXU\_{X} is open and convex in a neighborhood of x∘x^{\circ} and x1x\_{1} (we can always restrict to a sufficiently small line segment if necessary). Define

|  |  |  |
| --- | --- | --- |
|  | h​(α):=fθ⋆​(γ​(α)),b​(α):=fBayes​(γ​(α)).h(\alpha):=f\_{\theta^{\star}}(\gamma(\alpha)),\qquad b(\alpha):=f^{\mathrm{Bayes}}(\gamma(\alpha)). |  |

By continuity of fθ⋆f\_{\theta^{\star}} and fBayesf^{\mathrm{Bayes}} on UXU\_{X}, both hh and bb are continuous on [0,1][0,1]. At α=0\alpha=0 we have b​(0)∈int⁡(ℳvol)b(0)\in\operatorname{int}(\mathcal{M}\_{\mathrm{vol}}) and h​(0)∈ℳvolh(0)\in\mathcal{M}\_{\mathrm{vol}} by ([63](https://arxiv.org/html/2511.17304v1#A2.E63 "In Step 1: Existence of a prediction point outside ℳᵥₒₗ. ‣ B.3 Proof of Lemma 2 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). At α=1\alpha=1 we have b​(1)∈ℳvolb(1)\in\mathcal{M}\_{\mathrm{vol}} and h​(1)∈ℳvolh(1)\in\mathcal{M}\_{\mathrm{vol}} by ([63](https://arxiv.org/html/2511.17304v1#A2.E63 "In Step 1: Existence of a prediction point outside ℳᵥₒₗ. ‣ B.3 Proof of Lemma 2 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), but h​(1)≠b​(1)h(1)\neq b(1) by choice of x1x\_{1}.

Thus the difference d​(α):=h​(α)−b​(α)d(\alpha):=h(\alpha)-b(\alpha) is a continuous map with d​(1)≠0d(1)\neq 0. Since ℳvol\mathcal{M}\_{\mathrm{vol}} contains an open ball around b​(0)b(0), there exists ρ∈(0,r/2)\rho\in(0,r/2) such that

|  |  |  |
| --- | --- | --- |
|  | B​(b​(0),ρ)⊂ℳvol.B\bigl(b(0),\rho\bigr)\subset\mathcal{M}\_{\mathrm{vol}}. |  |

If it happened that h​(α)∈ℳvolh(\alpha)\in\mathcal{M}\_{\mathrm{vol}} for all α∈[0,1]\alpha\in[0,1], then the curve h​([0,1])h([0,1]) would be a continuous path in ℳvol\mathcal{M}\_{\mathrm{vol}} connecting h​(0)h(0) and h​(1)h(1), both of which lie in ℳvol\mathcal{M}\_{\mathrm{vol}}. This is not impossible *per se*; however, given the genericity Assumption (B.3)(c), which rules out that fθ⋆​(UX)f\_{\theta^{\star}}(U\_{X}) is constrained to a lower-dimensional surface within ℳvol\mathcal{M}\_{\mathrm{vol}}, we can exclude the degenerate situation where the entire image of the line segment γ​([0,1])\gamma([0,1]) under fθ⋆f\_{\theta^{\star}} remains inside ℳvol\mathcal{M}\_{\mathrm{vol}} while differing from fBayesf^{\mathrm{Bayes}} on a set of positive measure.

Formally, since b​(0)b(0) lies in the interior of ℳvol\mathcal{M}\_{\mathrm{vol}} and h​(0)∈ℳvolh(0)\in\mathcal{M}\_{\mathrm{vol}}, there is an open neighborhood VV of γ​(0)\gamma(0) such that b​(V)b(V) and h​(V)h(V) both intersect B​(b​(0),ρ)B(b(0),\rho) in sets of positive Lebesgue measure. Under (B.3)(c), the continuous map fθ⋆f\_{\theta^{\star}} cannot, on VV, be constrained to the (dvol−1)(d\_{\mathrm{vol}}-1)-dimensional manifold ∂ℳvol\partial\mathcal{M}\_{\mathrm{vol}}; hence there must exist some x~∈V\tilde{x}\in V such that

|  |  |  |
| --- | --- | --- |
|  | fθ⋆​(x~)∉ℳvol.f\_{\theta^{\star}}(\tilde{x})\notin\mathcal{M}\_{\mathrm{vol}}. |  |

Since V⊂supp⁡(Xt)V\subset\operatorname{supp}(X\_{t}) and ℙ​(Xt∈V)>0\mathbb{P}(X\_{t}\in V)>0, this implies

|  |  |  |
| --- | --- | --- |
|  | ℙ​(fθ⋆​(Xt)∉ℳvol)>0.\mathbb{P}\big(f\_{\theta^{\star}}(X\_{t})\notin\mathcal{M}\_{\mathrm{vol}}\big)>0. |  |

Equivalently, there exists at least one point w∗∈ℝdvol∖ℳvolw^{\ast}\in\mathbb{R}^{d\_{\mathrm{vol}}}\setminus\mathcal{M}\_{\mathrm{vol}} that is attained by W^t+1\hat{W}\_{t+1} with positive probability.

We have thus shown that ([63](https://arxiv.org/html/2511.17304v1#A2.E63 "In Step 1: Existence of a prediction point outside ℳᵥₒₗ. ‣ B.3 Proof of Lemma 2 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) cannot hold under the assumptions of the lemma together with (B.3). Therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(W^t+1∉ℳvol)>0.\mathbb{P}\big(\hat{W}\_{t+1}\notin\mathcal{M}\_{\mathrm{vol}}\big)>0. |  | (64) |

##### Step 2: From off-manifold predictions to a positive-distance shell.

Since ℳvol\mathcal{M}\_{\mathrm{vol}} is closed and W^t+1\hat{W}\_{t+1} is a random element of ℝdvol\mathbb{R}^{d\_{\mathrm{vol}}}, the continuous distance function dℳvold\_{\mathcal{M}\_{\mathrm{vol}}} satisfies

|  |  |  |
| --- | --- | --- |
|  | {W^t+1∉ℳvol}={dℳvol​(W^t+1)>0}.\{\hat{W}\_{t+1}\notin\mathcal{M}\_{\mathrm{vol}}\}=\{d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})>0\}. |  |

By ([64](https://arxiv.org/html/2511.17304v1#A2.E64 "In Step 1: Existence of a prediction point outside ℳᵥₒₗ. ‣ B.3 Proof of Lemma 2 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), the event {dℳvol​(W^t+1)>0}\{d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})>0\} has positive probability. Define

|  |  |  |
| --- | --- | --- |
|  | Z:=dℳvol​(W^t+1)≥0.Z:=d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})\geq 0. |  |

Then ℙ​(Z>0)>0\mathbb{P}(Z>0)>0. Since ZZ is a non-negative random variable, we can write its distribution function as

|  |  |  |
| --- | --- | --- |
|  | FZ​(η):=ℙ​(Z≤η),η≥0.F\_{Z}(\eta):=\mathbb{P}(Z\leq\eta),\qquad\eta\geq 0. |  |

By right-continuity of FZF\_{Z} and ℙ​(Z>0)>0\mathbb{P}(Z>0)>0, there must exist η0>0\eta\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Z>η0)=1−FZ​(η0)>0.\mathbb{P}(Z>\eta\_{0})=1-F\_{Z}(\eta\_{0})>0. |  |

Equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(dℳvol​(W^t+1)>η0)>0.\mathbb{P}\big(d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})>\eta\_{0}\big)>0. |  | (65) |

##### Step 3: Translating distance to law penalty.

Finally, we use the monotonic relationship between distance and law penalty. By continuity of ℒϕ\mathcal{L}\_{\phi} and the fact that ℒϕ​(w)=0\mathcal{L}\_{\phi}(w)=0 if and only if dℳvol​(w)=0d\_{\mathcal{M}\_{\mathrm{vol}}}(w)=0 (Proposition [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), there exists a strictly increasing continuous function

|  |  |  |
| --- | --- | --- |
|  | ψ:[0,∞)→[0,∞),ψ​(0)=0,\psi:[0,\infty)\to[0,\infty),\qquad\psi(0)=0, |  |

such that for all w∈ℝdvolw\in\mathbb{R}^{d\_{\mathrm{vol}}},

|  |  |  |
| --- | --- | --- |
|  | ℒϕ​(w)≥ψ​(dℳvol​(w)),\mathcal{L}\_{\phi}(w)\geq\psi\big(d\_{\mathcal{M}\_{\mathrm{vol}}}(w)\big), |  |

and ψ​(u)>0\psi(u)>0 for all u>0u>0. For instance, in the concrete squared-distance case ℒϕ​(w)=12​dℳvol​(w)2\mathcal{L}\_{\phi}(w)=\frac{1}{2}d\_{\mathcal{M}\_{\mathrm{vol}}}(w)^{2} we may take ψ​(u)=12​u2\psi(u)=\frac{1}{2}u^{2}.

Set

|  |  |  |
| --- | --- | --- |
|  | δ:=ψ​(η0)>0.\delta:=\psi(\eta\_{0})>0. |  |

Then on the event {dℳvol​(W^t+1)>η0}\{d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})>\eta\_{0}\} we have

|  |  |  |
| --- | --- | --- |
|  | ℒϕ​(W^t+1)≥ψ​(dℳvol​(W^t+1))>ψ​(η0)=δ.\mathcal{L}\_{\phi}(\hat{W}\_{t+1})\geq\psi\big(d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})\big)>\psi(\eta\_{0})=\delta. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℒϕ​(W^t+1)>δ)≥ℙ​(dℳvol​(W^t+1)>η0)>0,\mathbb{P}\big(\mathcal{L}\_{\phi}(\hat{W}\_{t+1})>\delta\big)\geq\mathbb{P}\big(d\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{W}\_{t+1})>\eta\_{0}\big)>0, |  |

by ([65](https://arxiv.org/html/2511.17304v1#A2.E65 "In Step 2: From off-manifold predictions to a positive-distance shell. ‣ B.3 Proof of Lemma 2 ‣ Appendix B Proofs for Section 3: Volatility World Model ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). This is precisely the claim of Lemma [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

##### Remark.

Note that the assumption fθ⋆≠fBayesf\_{\theta^{\star}}\neq f^{\mathrm{Bayes}} is used here only to rule out the trivial case where the world model has converged exactly to the Bayes regressor, which is law-consistent by construction. The non-trivial content of the lemma is provided by the genericity condition (B.3), which encodes the intuition that a high-capacity, unconstrained neural world model trained without law penalties will almost surely deviate from ℳvol\mathcal{M}\_{\mathrm{vol}} on a set of positive probability. Under these conditions, Lemma [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") shows that the world model opens a *ghost channel* in the sense of Sec. 3.3, providing room for RL to exploit off-manifold arbitrage opportunities.
∎

## Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength

### C.1 Proof of Theorem [1](https://arxiv.org/html/2511.17304v1#Thmtheorem1 "Theorem 1 (Ghost-arbitrage incentive for naive RL). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

In this appendix we provide a detailed proof of the ghost-arbitrage incentive
result stated in Theorem [1](https://arxiv.org/html/2511.17304v1#Thmtheorem1 "Theorem 1 (Ghost-arbitrage incentive for naive RL). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). For convenience we first
recall the main objects and Assumption [1](https://arxiv.org/html/2511.17304v1#Thmassumption1 "Assumption 1 (On-manifold near-optimality of structural class). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

##### Preliminaries and notation.

Let Π\Pi denote the (parameterized) policy class under consideration and let
𝒮\mathcal{S} denote the structural strategy class introduced in Section. For any π∈Π\pi\in\Pi we consider three
performance functionals:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J0​(π)\displaystyle J\_{0}(\pi) | :=𝔼​[∑t=0T−1γt​rt|π],\displaystyle:=\mathbb{E}\Bigg[\sum\_{t=0}^{T-1}\gamma^{t}\,r\_{t}\,\Big|\,\pi\Bigg], |  | (66) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Jℳ​(π)\displaystyle J^{\mathcal{M}}(\pi) | :=𝔼​[∑t=0T−1γt​rtℳ|π],\displaystyle:=\mathbb{E}\Bigg[\sum\_{t=0}^{T-1}\gamma^{t}\,r^{\mathcal{M}}\_{t}\,\Big|\,\pi\Bigg], |  | (67) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J⟂​(π)\displaystyle J^{\perp}(\pi) | :=𝔼​[∑t=0T−1γt​rt⟂|π],\displaystyle:=\mathbb{E}\Bigg[\sum\_{t=0}^{T-1}\gamma^{t}\,r^{\perp}\_{t}\,\Big|\,\pi\Bigg], |  | (68) |

where rtr\_{t} is the realized P&L reward at step tt in the world model,
rtℳr^{\mathcal{M}}\_{t} is the on-manifold reward obtained by replacing the
predicted surface w^t+1\hat{w}\_{t+1} with its projection
Πℳvol​(w^t+1)\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{w}\_{t+1}), and
rt⟂:=rt−rtℳr^{\perp}\_{t}:=r\_{t}-r^{\mathcal{M}}\_{t} is the ghost reward component.
By linearity of expectation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | J0​(π)=Jℳ​(π)+J⟂​(π),∀π∈Π.J\_{0}(\pi)=J^{\mathcal{M}}(\pi)+J^{\perp}(\pi),\qquad\forall\pi\in\Pi. |  | (69) |

##### Structural near-optimality assumption.

We recall the structural approximation assumption used in the main text.

###### Assumption 4 (Structural near-optimality of 𝒮\mathcal{S}).

There exist a structural policy π𝒮⋆∈𝒮\pi^{\star}\_{\mathcal{S}}\in\mathcal{S}
and a constant ε𝒮≥0\varepsilon\_{\mathcal{S}}\geq 0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈ΠJℳ​(π)≤Jℳ​(π𝒮⋆)+ε𝒮.\sup\_{\pi\in\Pi}J^{\mathcal{M}}(\pi)\;\leq\;J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}}. |  | (70) |

That is, the structural class 𝒮\mathcal{S} (Zero-Hedge, Vol-Trend, etc.)
approximates the globally optimal on-manifold performance within a gap
ε𝒮\varepsilon\_{\mathcal{S}}.

Note that by definition π𝒮⋆∈𝒮⊆Π\pi^{\star}\_{\mathcal{S}}\in\mathcal{S}\subseteq\Pi,
so it is admissible in the unconstrained policy class as well.

We now restate the theorem and prove both parts.

###### Theorem 4.

Suppose Assumption [4](https://arxiv.org/html/2511.17304v1#Thmassumption4 "Assumption 4 (Structural near-optimality of 𝒮). ‣ Structural near-optimality assumption. ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") holds, and let

|  |  |  |
| --- | --- | --- |
|  | π0⋆∈arg⁡maxπ∈Π⁡J0​(π)\pi^{\star}\_{0}\in\arg\max\_{\pi\in\Pi}J\_{0}(\pi) |  |

be a global maximizer of J0J\_{0} over Π\Pi. Then:

1. 1.

   If

   |  |  |  |
   | --- | --- | --- |
   |  | supπ∈ΠJ0​(π)>Jℳ​(π𝒮⋆)+ε𝒮,\sup\_{\pi\in\Pi}J\_{0}(\pi)>J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}}, |  |

   any maximizer π0⋆\pi^{\star}\_{0} satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | J⟂​(π0⋆)≥supπ∈ΠJ0​(π)−Jℳ​(π𝒮⋆)−ε𝒮> 0.J^{\perp}(\pi^{\star}\_{0})\;\geq\;\sup\_{\pi\in\Pi}J\_{0}(\pi)-J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})-\varepsilon\_{\mathcal{S}}\;>\;0. |  | (71) |

   In particular, the excess value over the structural baseline is entirely
   attributable to ghost arbitrage.
2. 2.

   If, in addition, JℳJ^{\mathcal{M}} has a local maximum at some
   π¯=πθ¯∈Π\bar{\pi}=\pi\_{\bar{\theta}}\in\Pi with
   Jℳ​(π¯)≈Jℳ​(π𝒮⋆)J^{\mathcal{M}}(\bar{\pi})\approx J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}}),
   and the policy-gradient theorem holds [[49](https://arxiv.org/html/2511.17304v1#bib.bib49)],
   then the policy gradient near π¯\bar{\pi} satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇θJ0​(πθ)|θ=θ¯≈∇θJ⟂​(πθ)|θ=θ¯,\nabla\_{\theta}J\_{0}(\pi\_{\theta})\Big|\_{\theta=\bar{\theta}}\;\approx\;\nabla\_{\theta}J^{\perp}(\pi\_{\theta})\Big|\_{\theta=\bar{\theta}}, |  | (72) |

   so gradient-based RL updates are locally driven by increasing J⟂J^{\perp}.

###### Proof.

We treat parts (i) and (ii) separately.

##### Proof of part (i).

Fix any π∈Π\pi\in\Pi. Combining the decomposition
([69](https://arxiv.org/html/2511.17304v1#A3.E69 "In Preliminaries and notation. ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) with
Assumption ([70](https://arxiv.org/html/2511.17304v1#A3.E70 "In Assumption 4 (Structural near-optimality of 𝒮). ‣ Structural near-optimality assumption. ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J0​(π)\displaystyle J\_{0}(\pi) | =Jℳ​(π)+J⟂​(π)\displaystyle=J^{\mathcal{M}}(\pi)+J^{\perp}(\pi) |  | (73) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤(Jℳ​(π𝒮⋆)+ε𝒮)+J⟂​(π),\displaystyle\leq\bigl(J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}}\bigr)+J^{\perp}(\pi), |  | (74) |

so for any π∈Π\pi\in\Pi,

|  |  |  |  |
| --- | --- | --- | --- |
|  | J⟂​(π)≥J0​(π)−Jℳ​(π𝒮⋆)−ε𝒮.J^{\perp}(\pi)\;\geq\;J\_{0}(\pi)-J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})-\varepsilon\_{\mathcal{S}}. |  | (75) |

Now consider a maximizer π0⋆∈arg⁡maxπ∈Π⁡J0​(π)\pi^{\star}\_{0}\in\arg\max\_{\pi\in\Pi}J\_{0}(\pi).
By definition,

|  |  |  |
| --- | --- | --- |
|  | J0​(π0⋆)=supπ∈ΠJ0​(π).J\_{0}(\pi^{\star}\_{0})=\sup\_{\pi\in\Pi}J\_{0}(\pi). |  |

Substituting π=π0⋆\pi=\pi^{\star}\_{0} into
([75](https://arxiv.org/html/2511.17304v1#A3.E75 "In Proof of part (i). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J⟂​(π0⋆)\displaystyle J^{\perp}(\pi^{\star}\_{0}) | ≥J0​(π0⋆)−Jℳ​(π𝒮⋆)−ε𝒮\displaystyle\geq J\_{0}(\pi^{\star}\_{0})-J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})-\varepsilon\_{\mathcal{S}} |  | (76) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =supπ∈ΠJ0​(π)−Jℳ​(π𝒮⋆)−ε𝒮.\displaystyle=\sup\_{\pi\in\Pi}J\_{0}(\pi)-J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})-\varepsilon\_{\mathcal{S}}. |  | (77) |

Under the stated strict inequality

|  |  |  |
| --- | --- | --- |
|  | supπ∈ΠJ0​(π)>Jℳ​(π𝒮⋆)+ε𝒮,\sup\_{\pi\in\Pi}J\_{0}(\pi)>J^{\mathcal{M}}(\pi^{\star}\_{\mathcal{S}})+\varepsilon\_{\mathcal{S}}, |  |

the right-hand side of ([77](https://arxiv.org/html/2511.17304v1#A3.E77 "In Proof of part (i). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) is strictly
positive, which implies

|  |  |  |
| --- | --- | --- |
|  | J⟂​(π0⋆)>0.J^{\perp}(\pi^{\star}\_{0})>0. |  |

This establishes ([71](https://arxiv.org/html/2511.17304v1#A3.E71 "In item 1 ‣ Theorem 4. ‣ Structural near-optimality assumption. ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and shows that any excess
value of the naive-RL maximizer over the structural near-optimal on-manifold
performance must be entirely carried by the ghost component J⟂J^{\perp}.
In particular, there is no room to explain the advantage of π0⋆\pi^{\star}\_{0}
over π𝒮⋆\pi^{\star}\_{\mathcal{S}} by on-manifold improvements alone.

##### Proof of part (ii).

We now consider the local gradient behavior. Let
πθ∈Π\pi\_{\theta}\in\Pi denote a differentiable parametrization of policies
with parameter vector θ∈ℝp\theta\in\mathbb{R}^{p}, and suppose that
π¯=πθ¯\bar{\pi}=\pi\_{\bar{\theta}} is such that JℳJ^{\mathcal{M}} has a local
maximum at θ¯\bar{\theta}, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jℳ​(πθ¯)≥Jℳ​(πθ)for all θ in a neighborhood of θ¯.J^{\mathcal{M}}(\pi\_{\bar{\theta}})\geq J^{\mathcal{M}}(\pi\_{\theta})\quad\text{for all $\theta$ in a neighborhood of $\bar{\theta}$}. |  | (78) |

*Step 1: Gradient decomposition.*
By ([69](https://arxiv.org/html/2511.17304v1#A3.E69 "In Preliminaries and notation. ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),

|  |  |  |
| --- | --- | --- |
|  | J0​(πθ)=Jℳ​(πθ)+J⟂​(πθ),∀θ.J\_{0}(\pi\_{\theta})=J^{\mathcal{M}}(\pi\_{\theta})+J^{\perp}(\pi\_{\theta}),\qquad\forall\theta. |  |

Assume that JℳJ^{\mathcal{M}} and J⟂J^{\perp} are (Fréchet) differentiable
with respect to θ\theta on an open neighborhood of θ¯\bar{\theta}; this is
standard under the conditions of the policy-gradient theorem, which ensures
differentiability of J0J\_{0} [[49](https://arxiv.org/html/2511.17304v1#bib.bib49), [51](https://arxiv.org/html/2511.17304v1#bib.bib51)].
Then, by linearity of differentiation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θJ0​(πθ)=∇θJℳ​(πθ)+∇θJ⟂​(πθ),for all θ near θ¯.\nabla\_{\theta}J\_{0}(\pi\_{\theta})=\nabla\_{\theta}J^{\mathcal{M}}(\pi\_{\theta})+\nabla\_{\theta}J^{\perp}(\pi\_{\theta}),\qquad\text{for all $\theta$ near $\bar{\theta}$}. |  | (79) |

*Step 2: Vanishing on-manifold gradient at a local maximum.*
Under the local maximality condition ([78](https://arxiv.org/html/2511.17304v1#A3.E78 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),
the first-order necessary condition for unconstrained optimization gives

|  |  |  |
| --- | --- | --- |
|  | ∇θJℳ​(πθ)|θ=θ¯=0.\nabla\_{\theta}J^{\mathcal{M}}(\pi\_{\theta})\big|\_{\theta=\bar{\theta}}=0. |  |

(If Π\Pi is itself subject to additional parameter constraints, one may
interpret this as a vanishing gradient along feasible directions; the
argument below is then applied in the corresponding tangent space.)

Substituting this into ([79](https://arxiv.org/html/2511.17304v1#A3.E79 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θJ0​(πθ)|θ=θ¯=∇θJ⟂​(πθ)|θ=θ¯.\nabla\_{\theta}J\_{0}(\pi\_{\theta})\Big|\_{\theta=\bar{\theta}}=\nabla\_{\theta}J^{\perp}(\pi\_{\theta})\Big|\_{\theta=\bar{\theta}}. |  | (80) |

Thus, *exactly at* θ¯\bar{\theta}, the naive-RL gradient coincides with
the ghost-gradient ∇θJ⟂\nabla\_{\theta}J^{\perp}; all infinitesimal improvement
directions for J0J\_{0} come from changing the ghost component.

*Step 3: Interpretation via the policy-gradient theorem.*
The policy-gradient theorem for episodic MDPs
(e.g. [[49](https://arxiv.org/html/2511.17304v1#bib.bib49), [51](https://arxiv.org/html/2511.17304v1#bib.bib51)]) states that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θJ0​(πθ)=𝔼πθ​[∑t=0T−1∇θlog⁡πθ​(at∣st)​At(0)],\nabla\_{\theta}J\_{0}(\pi\_{\theta})=\mathbb{E}\_{\pi\_{\theta}}\Bigg[\sum\_{t=0}^{T-1}\nabla\_{\theta}\log\pi\_{\theta}(a\_{t}\mid s\_{t})\,A^{(0)}\_{t}\Bigg], |  | (81) |

where At(0)A^{(0)}\_{t} is an advantage function associated with the total reward
rtr\_{t} and the expectation is over trajectories generated by πθ\pi\_{\theta}
in the world model. Similarly, using rtℳr^{\mathcal{M}}\_{t} and rt⟂r^{\perp}\_{t} as
rewards in the same MDP, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇θJℳ​(πθ)\displaystyle\nabla\_{\theta}J^{\mathcal{M}}(\pi\_{\theta}) | =𝔼πθ​[∑t=0T−1∇θlog⁡πθ​(at∣st)​At(ℳ)],\displaystyle=\mathbb{E}\_{\pi\_{\theta}}\Bigg[\sum\_{t=0}^{T-1}\nabla\_{\theta}\log\pi\_{\theta}(a\_{t}\mid s\_{t})\,A^{(\mathcal{M})}\_{t}\Bigg], |  | (82) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇θJ⟂​(πθ)\displaystyle\nabla\_{\theta}J^{\perp}(\pi\_{\theta}) | =𝔼πθ​[∑t=0T−1∇θlog⁡πθ​(at∣st)​At(⟂)],\displaystyle=\mathbb{E}\_{\pi\_{\theta}}\Bigg[\sum\_{t=0}^{T-1}\nabla\_{\theta}\log\pi\_{\theta}(a\_{t}\mid s\_{t})\,A^{(\perp)}\_{t}\Bigg], |  | (83) |

for appropriate advantage functions At(ℳ)A^{(\mathcal{M})}\_{t} and
At(⟂)A^{(\perp)}\_{t}.

By construction rt=rtℳ+rt⟂r\_{t}=r^{\mathcal{M}}\_{t}+r^{\perp}\_{t} and linearity of the
value-function operators, one can choose the advantage functions such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | At(0)=At(ℳ)+At(⟂),∀t,A^{(0)}\_{t}=A^{(\mathcal{M})}\_{t}+A^{(\perp)}\_{t},\qquad\forall t, |  | (84) |

which recovers ([79](https://arxiv.org/html/2511.17304v1#A3.E79 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) when substituted into
([81](https://arxiv.org/html/2511.17304v1#A3.E81 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

At θ=θ¯\theta=\bar{\theta}, the local optimality of JℳJ^{\mathcal{M}}
implies that the contribution of At(ℳ)A^{(\mathcal{M})}\_{t} integrates to zero
in ([82](https://arxiv.org/html/2511.17304v1#A3.E82 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")); equivalently,
∇θJℳ​(πθ)|θ=θ¯=0\nabla\_{\theta}J^{\mathcal{M}}(\pi\_{\theta})|\_{\theta=\bar{\theta}}=0.
Hence, by ([81](https://arxiv.org/html/2511.17304v1#A3.E81 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"))–([83](https://arxiv.org/html/2511.17304v1#A3.E83 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and
([84](https://arxiv.org/html/2511.17304v1#A3.E84 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we recover the exact equality
([80](https://arxiv.org/html/2511.17304v1#A3.E80 "In Proof of part (ii). ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

In practice, when JℳJ^{\mathcal{M}} is only approximately locally maximal
(e.g., due to finite-sample estimation and function approximation error),
we obtain the approximate relation

|  |  |  |
| --- | --- | --- |
|  | ∥∇θJ0(πθ)|θ=θ¯−∇θJ⟂(πθ)|θ=θ¯∥=∥∇θJℳ(πθ)|θ=θ¯∥≈0,\big\|\nabla\_{\theta}J\_{0}(\pi\_{\theta})\big|\_{\theta=\bar{\theta}}-\nabla\_{\theta}J^{\perp}(\pi\_{\theta})\big|\_{\theta=\bar{\theta}}\big\|=\big\|\nabla\_{\theta}J^{\mathcal{M}}(\pi\_{\theta})\big|\_{\theta=\bar{\theta}}\big\|\approx 0, |  |

which justifies the “≈\approx” symbol in
([72](https://arxiv.org/html/2511.17304v1#A3.E72 "In item 2 ‣ Theorem 4. ‣ Structural near-optimality assumption. ‣ C.1 Proof of Theorem 1 ‣ Appendix C Proofs for Section 4:RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) of the main text.

Combining Steps 1–3, we conclude that near a local maximizer of the
on-manifold performance JℳJ^{\mathcal{M}}, the gradient of the naive-RL
objective J0J\_{0} is dominated (indeed, at the maximizer: entirely given) by
the ghost-gradient ∇θJ⟂\nabla\_{\theta}J^{\perp}. This formalizes the statement
that gradient-based RL is locally incentivized to move into directions which
increase the expected ghost component, completing the proof of part (ii).
∎

## Appendix D Proofs for Section 5:Structural Baselines

### D.1 Proof of Proposition [7](https://arxiv.org/html/2511.17304v1#Thmproposition7 "Proposition 7 (Law-alignment of structural baselines). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")

In this appendix we provide a more detailed argument for the
law-alignment properties of the structural baselines and, more generally,
of the structural class 𝒮\mathcal{S} introduced in
Definition [8](https://arxiv.org/html/2511.17304v1#Thmdefinition8 "Definition 8 (Structural strategy class 𝒮). ‣ 5.1 Baseline definitions and structural priors ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). We work under the standing assumptions
of Section [3](https://arxiv.org/html/2511.17304v1#S3 "3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

##### Setup and notation.

Recall that the (law-consistent) generator G⋆G^{\star} produces total-variance
surfaces (wt)t≥0(w\_{t})\_{t\geq 0} with wt∈ℳvolw\_{t}\in\mathcal{M}\_{\mathrm{vol}} almost surely for all tt, cf. Proposition [5](https://arxiv.org/html/2511.17304v1#Thmproposition5 "Proposition 5 (Support of the synthetic generator). ‣ Law-consistent ground truth. ‣ 3.1 Synthetic law-consistent generator ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). The world model
fθ⋆f\_{\theta^{\star}} takes as input a feature vector xtx\_{t} (which may include
past surfaces and positions) and outputs a prediction
w^t+1=fθ⋆​(xt)\hat{w}\_{t+1}=f\_{\theta^{\star}}(x\_{t}), with approximation residual

|  |  |  |
| --- | --- | --- |
|  | et+1:=w^t+1−wt+1.e\_{t+1}:=\hat{w}\_{t+1}-w\_{t+1}. |  |

The volatility law-penalty functional is

|  |  |  |
| --- | --- | --- |
|  | ℒvol​(w^t+1)=12​dist​(w^t+1,ℳvol)2=12​‖w^t+1−Πℳvol​(w^t+1)‖22,\mathcal{L}\_{\mathrm{vol}}(\hat{w}\_{t+1})=\frac{1}{2}\,\mathrm{dist}\bigl(\hat{w}\_{t+1},\mathcal{M}\_{\mathrm{vol}}\bigr)^{2}=\frac{1}{2}\bigl\|\hat{w}\_{t+1}-\Pi\_{\mathcal{M}\_{\mathrm{vol}}}(\hat{w}\_{t+1})\bigr\|\_{2}^{2}, |  |

where Πℳvol\Pi\_{\mathcal{M}\_{\mathrm{vol}}} is the Euclidean projection onto ℳvol\mathcal{M}\_{\mathrm{vol}}.

For a policy π\pi, we denote by
𝖫𝖯¯​(π)\overline{\mathsf{LP}}(\pi) the long-run average (or finite-horizon
normalized) law penalty,
and by GFI​(π)\mathrm{GFI}(\pi) its Graceful Failure Index, as defined in
Section [4.4](https://arxiv.org/html/2511.17304v1#S4.SS4 "4.4 Law-strength frontier and Graceful Failure Index ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"). We recall that these quantities have
the schematic form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖫𝖯¯​(π)\displaystyle\overline{\mathsf{LP}}(\pi) | ≈1T​∑t=0T−1𝔼​[ℒvol​(w^t+1)|π],\displaystyle\approx\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{E}\bigl[\mathcal{L}\_{\mathrm{vol}}(\hat{w}\_{t+1})\,\big|\,\pi\bigr], |  | (85) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | GFI​(π)\displaystyle\mathrm{GFI}(\pi) | =μlawshock​(π)−μlawbase​(π)Ishock,\displaystyle=\frac{\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi)-\mu\_{\mathrm{law}}^{\text{base}}(\pi)}{I\_{\mathrm{shock}}}, |  | (86) |

where μlawbase​(π)\mu\_{\mathrm{law}}^{\text{base}}(\pi) and
μlawshock​(π)\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi) are aggregate law metrics in baseline
and shock regimes, and Ishock>0I\_{\mathrm{shock}}>0 encodes shock intensity (which is
fixed for all policies).

Finally, by Definition [8](https://arxiv.org/html/2511.17304v1#Thmdefinition8 "Definition 8 (Structural strategy class 𝒮). ‣ 5.1 Baseline definitions and structural priors ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), a structural policy
π∈𝒮\pi\in\mathcal{S} is of the form

|  |  |  |
| --- | --- | --- |
|  | at=π​(st)=gθ​(zt),a\_{t}=\pi(s\_{t})=g\_{\theta}(z\_{t}), |  |

where ztz\_{t} is a low-dimensional signal (e.g. realized vol trend) and
gθg\_{\theta} is a Lipschitz parametric map with bounded leverage,
‖gθ​(z)‖≤Lmax\|g\_{\theta}(z)\|\leq L\_{\max} for all zz and all θ∈Θ\theta\in\Theta,
with Θ\Theta compact. The baselines bZHb^{\mathrm{ZH}} (Zero-Hedge),
bVTb^{\mathrm{VT}} (Vol-Trend), and bRGb^{\mathrm{RG}} (Random-Gaussian)
are specific instances in 𝒮\mathcal{S}.

The proof proceeds in three steps. First, we show that law penalties are
uniformly bounded in terms of the world-model error. Second, we use the
structural priors of 𝒮\mathcal{S} to obtain uniform moment bounds on the
state process and hence on the residuals et+1e\_{t+1}. Third, we translate
these to bounds on 𝖫𝖯¯\overline{\mathsf{LP}} and GFI.

##### Step 1: Bounding law penalties by world-model error.

By Proposition [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), we know that
ℒvol​(wt+1)=0\mathcal{L}\_{\mathrm{vol}}(w\_{t+1})=0 whenever wt+1∈ℳvolw\_{t+1}\in\mathcal{M}\_{\mathrm{vol}}. Since the generator is
law-consistent, wt+1∈ℳvolw\_{t+1}\in\mathcal{M}\_{\mathrm{vol}} almost surely, and thus for any
realization of wt+1w\_{t+1} and any prediction w^t+1\hat{w}\_{t+1} we have

|  |  |  |
| --- | --- | --- |
|  | dist​(w^t+1,ℳvol)≤‖w^t+1−wt+1‖2=‖et+1‖2.\mathrm{dist}\bigl(\hat{w}\_{t+1},\mathcal{M}\_{\mathrm{vol}}\bigr)\;\leq\;\|\hat{w}\_{t+1}-w\_{t+1}\|\_{2}=\|e\_{t+1}\|\_{2}. |  |

Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒvol​(w^t+1)=12​dist​(w^t+1,ℳvol)2≤12​‖et+1‖22.\mathcal{L}\_{\mathrm{vol}}(\hat{w}\_{t+1})=\frac{1}{2}\mathrm{dist}\bigl(\hat{w}\_{t+1},\mathcal{M}\_{\mathrm{vol}}\bigr)^{2}\;\leq\;\frac{1}{2}\|e\_{t+1}\|\_{2}^{2}. |  | (87) |

Taking expectations conditional on the policy π\pi and the regime
(baseline or shock), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ℒvol​(w^t+1)|π]≤12​𝔼​[‖et+1‖22|π].\mathbb{E}\bigl[\mathcal{L}\_{\mathrm{vol}}(\hat{w}\_{t+1})\,\big|\,\pi\bigr]\;\leq\;\frac{1}{2}\,\mathbb{E}\bigl[\|e\_{t+1}\|\_{2}^{2}\,\big|\,\pi\bigr]. |  | (88) |

Thus, uniform control of the second moment of the approximation error
et+1e\_{t+1} under a policy class implies uniform control of the law
penalties under that class.

##### Step 2: Uniform second-moment bounds for structural policies.

By Proposition [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and the conditions
stated there, the world model fθ⋆f\_{\theta^{\star}} is Lipschitz in its
input xtx\_{t}, and the approximation error et+1e\_{t+1} is bounded (in second
moment) on bounded subsets of the input space. Concretely, there exist
constants Lf,Ce<∞L\_{f},C\_{e}<\infty such that, for any two inputs x,x′x,x^{\prime},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖fθ⋆​(x)−fθ⋆​(x′)‖2\displaystyle\|f\_{\theta^{\star}}(x)-f\_{\theta^{\star}}(x^{\prime})\|\_{2} | ≤Lf​‖x−x′‖2,\displaystyle\leq L\_{f}\|x-x^{\prime}\|\_{2}, |  | (89) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | sup‖x‖≤R𝔼​[‖fθ⋆​(x)−wt+1‖22|xt=x]\displaystyle\sup\_{\|x\|\leq R}\mathbb{E}\bigl[\|f\_{\theta^{\star}}(x)-w\_{t+1}\|\_{2}^{2}\,\big|\,x\_{t}=x\bigr] | ≤Ce​(R),for each finite R>0,\displaystyle\leq C\_{e}(R),\quad\text{for each finite $R>0$,} |  | (90) |

where Ce​(R)C\_{e}(R) is non-decreasing in RR.

The key structural property of 𝒮\mathcal{S} is that it induces a
*bounded-exposure* Markov chain on the joint state
(wt,ht,zt)(w\_{t},h\_{t},z\_{t}), where hth\_{t} denotes the position vector (portfolio
holdings) and ztz\_{t} denotes the low-dimensional signals. More precisely:

###### Lemma 5 (Uniform moment control under 𝒮\mathcal{S}).

Under the law-consistent generator and the structural priors of
Definition [8](https://arxiv.org/html/2511.17304v1#Thmdefinition8 "Definition 8 (Structural strategy class 𝒮). ‣ 5.1 Baseline definitions and structural priors ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") (bounded leverage LmaxL\_{\max},
compact parameter set Θ\Theta, and Lipschitz gg), there exists
a constant Cstate<∞C\_{\mathrm{state}}<\infty such that for every structural
policy π∈𝒮\pi\in\mathcal{S} and every tt,

|  |  |  |
| --- | --- | --- |
|  | 𝔼π​[‖xt‖22]≤Cstate,\mathbb{E}\_{\pi}\bigl[\|x\_{t}\|\_{2}^{2}\bigr]\leq C\_{\mathrm{state}}, |  |

where xtx\_{t} is the world-model input constructed from (wt,ht,zt)(w\_{t},h\_{t},z\_{t}).

###### Proof.

(Sketch.) The generator G⋆G^{\star} yields an exogenous process (wt)(w\_{t})
whose second moments are bounded over the finite horizon t=0,…,Tt=0,\dots,T,
by standard properties of the underlying stochastic-volatility model and
the projection onto ℳvol\mathcal{M}\_{\mathrm{vol}} (see, e.g., stability of affine and rough
volatility models [[9](https://arxiv.org/html/2511.17304v1#bib.bib9), [8](https://arxiv.org/html/2511.17304v1#bib.bib8)]).
The signals ztz\_{t} are Lipschitz functions of (w0,…,wt)(w\_{0},\dots,w\_{t}) (e.g.,
realized-vol trends, moving averages), and thus inherit bounded second
moments over t=0,…,Tt=0,\dots,T.

For a structural policy π∈𝒮\pi\in\mathcal{S}, the position process
ht=gθ​(zt)h\_{t}=g\_{\theta}(z\_{t}) satisfies
‖ht‖2≤Lmax\|h\_{t}\|\_{2}\leq L\_{\max} almost surely for all tt, by bounded leverage
and compact Θ\Theta. Hence 𝔼​[‖ht‖22]≤Lmax2\mathbb{E}[\|h\_{t}\|\_{2}^{2}]\leq L\_{\max}^{2} for all tt.
Since xtx\_{t} is built from (wt,ht,zt)(w\_{t},h\_{t},z\_{t}) via a fixed, Lipschitz
feature map (stacking, scaling, etc.), we obtain
𝔼π​[‖xt‖22]≤Cstate\mathbb{E}\_{\pi}[\|x\_{t}\|\_{2}^{2}]\leq C\_{\mathrm{state}} for some finite constant
CstateC\_{\mathrm{state}} independent of π∈𝒮\pi\in\mathcal{S} and tt.
A fully rigorous version uses a Lyapunov-function argument for the
Markov chain induced by 𝒮\mathcal{S}; see Appendix D.1.
∎

Combining Lemma [5](https://arxiv.org/html/2511.17304v1#Thmlemma5 "Lemma 5 (Uniform moment control under 𝒮). ‣ Step 2: Uniform second-moment bounds for structural policies. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") with
([90](https://arxiv.org/html/2511.17304v1#A4.E90 "In Step 2: Uniform second-moment bounds for structural policies. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we obtain a uniform bound on the second
moment of the residuals under 𝒮\mathcal{S}: there exists
C¯e<∞\bar{C}\_{e}<\infty such that, for all π∈𝒮\pi\in\mathcal{S} and all tt,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π​[‖et+1‖22]=𝔼π​[𝔼​[‖et+1‖22∣xt]]≤𝔼π​[Ce​(‖xt‖)]≤C¯e,\mathbb{E}\_{\pi}\bigl[\|e\_{t+1}\|\_{2}^{2}\bigr]=\mathbb{E}\_{\pi}\Bigl[\,\mathbb{E}\bigl[\|e\_{t+1}\|\_{2}^{2}\mid x\_{t}\bigr]\Bigr]\;\leq\;\mathbb{E}\_{\pi}\bigl[C\_{e}(\|x\_{t}\|)\bigr]\;\leq\;\bar{C}\_{e}, |  | (91) |

where we used monotonicity of Ce​(⋅)C\_{e}(\cdot) and the uniform bound
𝔼π​[‖xt‖22]≤Cstate\mathbb{E}\_{\pi}[\|x\_{t}\|\_{2}^{2}]\leq C\_{\mathrm{state}}.

##### Step 3: Bounds on 𝖫𝖯¯\overline{\mathsf{LP}} and GFI.

Using ([88](https://arxiv.org/html/2511.17304v1#A4.E88 "In Step 1: Bounding law penalties by world-model error. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and
([91](https://arxiv.org/html/2511.17304v1#A4.E91 "In Step 2: Uniform second-moment bounds for structural policies. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we obtain that for any
π∈𝒮\pi\in\mathcal{S} and any tt,

|  |  |  |
| --- | --- | --- |
|  | 𝔼π​[ℒvol​(w^t+1)]≤12​𝔼π​[‖et+1‖22]≤12​C¯e.\mathbb{E}\_{\pi}\bigl[\mathcal{L}\_{\mathrm{vol}}(\hat{w}\_{t+1})\bigr]\;\leq\;\frac{1}{2}\,\mathbb{E}\_{\pi}\bigl[\|e\_{t+1}\|\_{2}^{2}\bigr]\;\leq\;\frac{1}{2}\bar{C}\_{e}. |  |

Substituting into ([85](https://arxiv.org/html/2511.17304v1#A4.E85 "In Setup and notation. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and taking the supremum over
π∈𝒮\pi\in\mathcal{S} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒮𝖫𝖯¯(π)≤12C¯e=:CLP<∞.\sup\_{\pi\in\mathcal{S}}\overline{\mathsf{LP}}(\pi)\;\leq\;\frac{1}{2}\bar{C}\_{e}=:C\_{\mathrm{LP}}<\infty. |  | (92) |

This shows that 𝒮\mathcal{S} is law-aligned in the sense of
Definition [9](https://arxiv.org/html/2511.17304v1#Thmdefinition9 "Definition 9 (Law-aligned strategy class). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), establishing item (i) of the
proposition.

For the GFI, recall its definition in ([86](https://arxiv.org/html/2511.17304v1#A4.E86 "In Setup and notation. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). The
numerator is the difference in aggregate law metrics between the shock
and baseline regimes. Under our shock design (multiplying long variance
and spot volatility by bounded factors), the generator remains
law-consistent and the world model is evaluated on a distorted, but
still bounded, region of the state space. By the same reasoning as above
(with possibly different constants), there exist finite constants
ClawbaseC\_{\mathrm{law}}^{\text{base}} and ClawshockC\_{\mathrm{law}}^{\mathrm{shock}} such
that for all π∈𝒮\pi\in\mathcal{S},

|  |  |  |
| --- | --- | --- |
|  | μlawbase​(π)≤Clawbase,μlawshock​(π)≤Clawshock.\mu\_{\mathrm{law}}^{\text{base}}(\pi)\leq C\_{\mathrm{law}}^{\text{base}},\qquad\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi)\leq C\_{\mathrm{law}}^{\mathrm{shock}}. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | |μlawshock(π)−μlawbase(π)|≤Clawbase+Clawshock=:C~law<∞\bigl|\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi)-\mu\_{\mathrm{law}}^{\text{base}}(\pi)\bigr|\;\leq\;C\_{\mathrm{law}}^{\text{base}}+C\_{\mathrm{law}}^{\mathrm{shock}}=:\widetilde{C}\_{\mathrm{law}}<\infty |  | (93) |

for all π∈𝒮\pi\in\mathcal{S}. Since Ishock>0I\_{\mathrm{shock}}>0 is fixed and does not
depend on π\pi, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒮GFI(π)=supπ∈𝒮μlawshock​(π)−μlawbase​(π)Ishock≤C~lawIshock=:CGFI<∞.\sup\_{\pi\in\mathcal{S}}\mathrm{GFI}(\pi)=\sup\_{\pi\in\mathcal{S}}\frac{\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi)-\mu\_{\mathrm{law}}^{\text{base}}(\pi)}{I\_{\mathrm{shock}}}\;\leq\;\frac{\widetilde{C}\_{\mathrm{law}}}{I\_{\mathrm{shock}}}=:C\_{\mathrm{GFI}}<\infty. |  | (94) |

This establishes the existence of a finite constant CGFIC\_{\mathrm{GFI}}
depending only on the generator, the shock specification, and the
world-model error, proving item (i) and the first part of item (ii).

##### Baselines bZHb^{\mathrm{ZH}} and bVTb^{\mathrm{VT}}.

We now specialize to the two deterministic baselines.

*Zero-Hedge bZHb^{\mathrm{ZH}}.*
By definition, bZHb^{\mathrm{ZH}} takes no positions,
ht≡0h\_{t}\equiv 0, at all times. The state process affecting the world
model thus reduces to the exogenous generator path (wt,zt)(w\_{t},z\_{t}), and the
residual distribution is precisely the “background” world-model error
profile studied in Section. In particular, the bounds
([91](https://arxiv.org/html/2511.17304v1#A4.E91 "In Step 2: Uniform second-moment bounds for structural policies. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), ([92](https://arxiv.org/html/2511.17304v1#A4.E92 "In Step 3: Bounds on (𝖫𝖯)̄ and GFI. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), and
([94](https://arxiv.org/html/2511.17304v1#A4.E94 "In Step 3: Bounds on (𝖫𝖯)̄ and GFI. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) hold with π=bZH\pi=b^{\mathrm{ZH}}. Empirically, this
baseline indeed exhibits the smallest observed law penalties and GFI,
matching the theoretical role of bZHb^{\mathrm{ZH}} as the law-neutral
benchmark.

*Vol-Trend bVTb^{\mathrm{VT}}.*
The Vol-Trend baseline applies a one-factor trend-following rule with
bounded leverage, ht=gθVT​(zt)h\_{t}=g\_{\theta^{\mathrm{VT}}}(z\_{t}), where
ztz\_{t} encodes recent volatility trends and gθVTg\_{\theta^{\mathrm{VT}}} is
Lipschitz with ‖gθVT​(z)‖≤Lmax\|g\_{\theta^{\mathrm{VT}}}(z)\|\leq L\_{\max} for all
zz. As in Lemma [5](https://arxiv.org/html/2511.17304v1#Thmlemma5 "Lemma 5 (Uniform moment control under 𝒮). ‣ Step 2: Uniform second-moment bounds for structural policies. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), this ensures that positions
respond smoothly to volatility changes and remain uniformly bounded in
second moment, so that (wt,zt,ht)(w\_{t},z\_{t},h\_{t}) stays in a bounded region of the
state space. Therefore the same world-model error and law-penalty bounds
apply, and we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝖫𝖯¯​(bZH),𝖫𝖯¯​(bVT)≤CLP,GFI​(bZH),GFI​(bVT)≤CGFI.\overline{\mathsf{LP}}(b^{\mathrm{ZH}}),~\overline{\mathsf{LP}}(b^{\mathrm{VT}})\leq C\_{\mathrm{LP}},\qquad\mathrm{GFI}(b^{\mathrm{ZH}}),~\mathrm{GFI}(b^{\mathrm{VT}})\leq C\_{\mathrm{GFI}}. |  |

This proves item (ii), with the empirical strictness “below unconstrained
RL levels” arising from the ghost-incentive effect(naive RL actively amplifies exposure
in regions where the ghost component r⟂r^{\perp} is large, whereas
bZHb^{\mathrm{ZH}} and bVTb^{\mathrm{VT}} do not target such regions).

##### Random-Gaussian baseline bRGb^{\mathrm{RG}}.

Finally, consider the Random-Gaussian baseline bRGb^{\mathrm{RG}}, which
draws actions from a Gaussian distribution
at∼𝒩​(0,Σa)a\_{t}\sim\mathcal{N}(0,\Sigma\_{a}) with fixed covariance Σa\Sigma\_{a},
possibly truncated to enforce a leverage bound. Provided
tr​(Σa)<∞\mathrm{tr}(\Sigma\_{a})<\infty and the truncation is such that
𝔼​[‖at‖22]≤Lmax′<∞\mathbb{E}[\|a\_{t}\|\_{2}^{2}]\leq L\_{\max}^{\prime}<\infty, we obtain moment bounds on the
position process (ht)(h\_{t}) analogous to those for bVTb^{\mathrm{VT}},
although with larger constants reflecting the additional randomness.
Repeating the argument leading to
([91](https://arxiv.org/html/2511.17304v1#A4.E91 "In Step 2: Uniform second-moment bounds for structural policies. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"))–([94](https://arxiv.org/html/2511.17304v1#A4.E94 "In Step 3: Bounds on (𝖫𝖯)̄ and GFI. ‣ D.1 Proof of Proposition 7 ‣ Appendix D Proofs for Section 5:Structural Baselines ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), we find
finite constants CLP′,CGFI′<∞C\_{\mathrm{LP}}^{\prime},C\_{\mathrm{GFI}}^{\prime}<\infty such that

|  |  |  |
| --- | --- | --- |
|  | 𝖫𝖯¯​(bRG)≤CLP′,GFI​(bRG)≤CGFI′.\overline{\mathsf{LP}}(b^{\mathrm{RG}})\leq C\_{\mathrm{LP}}^{\prime},\qquad\mathrm{GFI}(b^{\mathrm{RG}})\leq C\_{\mathrm{GFI}}^{\prime}. |  |

In general one expects CLP′,CGFI′C\_{\mathrm{LP}}^{\prime},C\_{\mathrm{GFI}}^{\prime} to be larger
than CLP,CGFIC\_{\mathrm{LP}},C\_{\mathrm{GFI}}, because bRGb^{\mathrm{RG}}
explores a wider range of states and can occasionally spend more time in
regions where the world-model error and induced law penalties are
higher. This matches the empirical role of bRGb^{\mathrm{RG}} as a noisy,
less structured baseline.

Collecting the above bounds, we see that the structural class
𝒮\mathcal{S} is uniformly law-aligned, and that the specific structural
baselines bZHb^{\mathrm{ZH}} and bVTb^{\mathrm{VT}} enjoy particularly
favorable law-penalty and GFI levels relative to unconstrained RL
policies. This completes the proof of
Proposition [7](https://arxiv.org/html/2511.17304v1#Thmproposition7 "Proposition 7 (Law-alignment of structural baselines). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

## Appendix E Empirical Results: From RL Dynamics to Law-Strength Frontiers (Supplementary)

In this appendix we provide complementary quantitative details to Section. We (i) restate the full metric tables for
all strategies in both baseline and shock regimes, (ii) tabulate the
law-strength frontier points used in Figures, and (iii) describe the precise numerical
procedures used to construct the frontiers and diagnostic plots.

Throughout, all metrics are computed on the same evaluation trajectories
used to generate Figures, and hence are fully consistent with
the summary numbers reported.

### E.1 Full metrics: baseline regime

Table [4](https://arxiv.org/html/2511.17304v1#A5.T4 "Table 4 ‣ E.1 Full metrics: baseline regime ‣ Appendix E Empirical Results: From RL Dynamics to Law-Strength Frontiers (Supplementary) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") reports the complete set of
step-wise metrics for all RL and structural strategies in the baseline
regime, corresponding to the top half of
Table in the main text. We include mean and
standard deviation of step P&L, Sharpe ratio, mean and maximum
law-penalty, law-adjusted return, Graceful Failure Index (GFI), law
coverage at two thresholds, and 5%5\% tail risk measures (VaR and
CVaR).

Table 4: Full step-wise metrics for all strategies in the *baseline* regime.
Mean and standard deviation of step P&L, Sharpe ratio, mean and maximum law penalty,
law-adjusted return, Graceful Failure Index (GFI), law coverage at two thresholds,
and 5%5\% tail risk measures (VaR5, CVaR5).
All numbers are computed on the same evaluation trajectories

| Strategy | Mean P&L | Std P&L | Sharpe | Mean LawPen | Max LawPen | Law-Adj Ret | GFI | LawCov <0.003<0.003 | LawCov <0.006<0.006 | VaR5 / CVaR5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Naive RL (PPO) | −0.0022-0.0022 | 0.01270.0127 | −0.1696-0.1696 | 0.0069940.006994 | 0.0208500.020850 | −0.0057-0.0057 | 1.26751.2675 | 0.53060.5306 | 0.61220.6122 | −0.0228-0.0228 / −0.0261-0.0261 |
| Law-Seeking RL (PPO) | −0.0150-0.0150 | 0.01290.0129 | −1.1564-1.1564 | 0.0078610.007861 | 0.0225540.022554 | −0.0189-0.0189 | 1.66211.6621 | 0.48980.4898 | 0.57140.5714 | −0.0361-0.0361 / −0.0394-0.0394 |
| Zero-Hedge baseline | 0.01910.0191 | 0.00640.0064 | 2.99442.9944 | 0.0055010.005501 | 0.0183180.018318 | 0.01640.0164 | 0.00000.0000 | 0.61220.6122 | 0.69390.6939 | 0.01390.0139 / 0.01390.0139 |
| Random-Gaussian baseline | 0.00990.0099 | 0.01070.0107 | 0.92350.9235 | 0.0055100.005510 | 0.0206860.020686 | 0.00720.0072 | 1.20621.2062 | 0.62040.6204 | 0.69180.6918 | −0.0088-0.0088 / −0.0161-0.0161 |
| Vol-Trend baseline | 0.01460.0146 | 0.00740.0074 | 1.96361.9636 | 0.0053440.005344 | 0.0171730.017173 | 0.01190.0119 | 0.00000.0000 | 0.61220.6122 | 0.69390.6939 | 0.00450.0045 / 0.00330.0033 |

As noted in Section, the baseline regime already
exhibits the main qualitative pattern: the structurally constrained
baselines (Zero-Hedge, Vol-Trend) lie in a region of high Sharpe and
moderate law penalties, with GFI effectively zero, while all RL
variants—including law-seeking PPO—display negative mean P&L and
substantially higher GFI values.

### E.2 Full metrics: shock regime

In which we
apply a volatility shock (long-variance multiplier 44, spot-vol
multiplier 22) to the underlying generator while keeping the world
model fixed.

Table 5: Baseline-regime metrics for all law-strength frontier points:
Naive RL (λ=0\lambda=0), soft law-seeking RL for λ∈{5,10,20,40}\lambda\in\{5,10,20,40\},
selection-only RL, and structural baselines. These are the points
used to construct the law-strength frontier and diagnostic plots

| Strategy / λ\lambda | Mean P&L | Std P&L | Sharpe | Mean LawPen | Max LawPen | Law-Adj Ret | GFI | LawCov <0.003<0.003 | LawCov <0.006<0.006 | VaR5 / CVaR5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Naive RL (λ=0\lambda=0) | −0.0022-0.0022 | 0.01270.0127 | −0.1696-0.1696 | 0.0069940.006994 | 0.0208500.020850 | −0.0057-0.0057 | 1.26751.2675 | 0.53060.5306 | 0.61220.6122 | −0.0228-0.0228 / −0.0261-0.0261 |
| Soft RL (λ=5\lambda=5) | −0.0202-0.0202 | 0.01200.0120 | −1.6753-1.6753 | 0.0064720.006472 | 0.0199560.019956 | −0.0234-0.0234 | 2.06632.0663 | 0.55100.5510 | 0.63270.6327 | −0.0399-0.0399 / −0.0429-0.0429 |
| Soft RL (λ=10\lambda=10) | −0.0175-0.0175 | 0.01230.0123 | −1.4248-1.4248 | 0.0037090.003709 | 0.0131690.013169 | −0.0194-0.0194 | 2.80592.8059 | 0.73470.7347 | 0.79590.7959 | −0.0354-0.0354 / −0.0387-0.0387 |
| Soft RL (λ=20\lambda=20) | −0.0204-0.0204 | 0.01310.0131 | −1.5629-1.5629 | 0.0039620.003962 | 0.0142510.014251 | −0.0224-0.0224 | 3.07283.0728 | 0.71430.7143 | 0.77550.7755 | −0.0414-0.0414 / −0.0454-0.0454 |
| Soft RL (λ=40\lambda=40) | −0.0092-0.0092 | 0.00540.0054 | −1.7138-1.7138 | 0.0047370.004737 | 0.0158880.015888 | −0.0116-0.0116 | 0.84430.8443 | 0.65310.6531 | 0.73470.7347 | −0.0134-0.0134 / −0.0134-0.0134 |
| Selection-only RL | −0.0223-0.0223 | 0.01390.0139 | −1.6028-1.6028 | 0.0079230.007923 | 0.0228270.022827 | −0.0263-0.0263 | 2.04072.0407 | 0.48980.4898 | 0.57140.5714 | −0.0448-0.0448 / −0.0489-0.0489 |
| Zero-Hedge baseline | 0.01910.0191 | 0.00640.0064 | 2.99442.9944 | 0.0055010.005501 | 0.0183180.018318 | 0.01640.0164 | 0.00000.0000 | 0.61220.6122 | 0.69390.6939 | 0.01390.0139 / 0.01390.0139 |
| Random-Gaussian baseline | 0.00990.0099 | 0.01070.0107 | 0.92350.9235 | 0.0055100.005510 | 0.0206860.020686 | 0.00720.0072 | 1.20621.2062 | 0.62040.6204 | 0.69180.6918 | −0.0088-0.0088 / −0.0161-0.0161 |
| Vol-Trend baseline | 0.01460.0146 | 0.00740.0074 | 1.96361.9636 | 0.0053440.005344 | 0.0171730.017173 | 0.01190.0119 | 0.00000.0000 | 0.61220.6122 | 0.69390.6939 | 0.00450.0045 / 0.00330.0033 |

The law-strength frontier plots in
Figures correspond to projections of Table [5](https://arxiv.org/html/2511.17304v1#A5.T5 "Table 5 ‣ E.2 Full metrics: shock regime ‣ Appendix E Empirical Results: From RL Dynamics to Law-Strength Frontiers (Supplementary) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") onto
two-dimensional planes, for example:

1. 1.

   mean law penalty vs. GFI,
2. 2.

   mean law penalty vs. Sharpe,
3. 3.

   mean law penalty vs. VaR5 or CVaR5.

Within the law-penalty band [0.0053,0.0057][0.0053,0.0057] highlighted, Zero-Hedge lies near the lower boundary
with high Sharpe and GFI ≈0\approx 0, while the closest RL variants in
the band have Sharpe <0<0 and GFI >1.5>1.5, illustrating the empirical
Pareto dominance emphasized in the main text.

### E.3 Frontier construction and banding procedure

For completeness, we describe the numerical procedure used to construct the law-strength frontiers and penalty bands.

##### Policy set.

We collect the following set of evaluated policies:

1. 1.

   Naive RL (PPO) trained on pure P&L,
2. 2.

   soft law-seeking RL for λ∈{5,10,20,40}\lambda\in\{5,10,20,40\},
3. 3.

   selection-only RL (trained on P&L, selected by law metrics),
4. 4.

   structural baselines: Zero-Hedge, Random-Gaussian, Vol-Trend.

For each policy we compute the metric vector

|  |  |  |
| --- | --- | --- |
|  | 𝐦​(π)=(μP&L​(π),σP&L​(π),Sharpe​(π),μlaw​(π),GFI​(π),VaR5​(π),CVaR5​(π)),\mathbf{m}(\pi)=\bigl(\mu\_{\mathrm{P\&L}}(\pi),\;\sigma\_{\mathrm{P\&L}}(\pi),\;\mathrm{Sharpe}(\pi),\;\mu\_{\mathrm{law}}(\pi),\;\mathrm{GFI}(\pi),\;\mathrm{VaR}\_{5}(\pi),\;\mathrm{CVaR}\_{5}(\pi)\bigr), |  |

with components given explicitly in
Tables [4](https://arxiv.org/html/2511.17304v1#A5.T4 "Table 4 ‣ E.1 Full metrics: baseline regime ‣ Appendix E Empirical Results: From RL Dynamics to Law-Strength Frontiers (Supplementary) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")–[5](https://arxiv.org/html/2511.17304v1#A5.T5 "Table 5 ‣ E.2 Full metrics: shock regime ‣ Appendix E Empirical Results: From RL Dynamics to Law-Strength Frontiers (Supplementary) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

##### Penalty banding.

To compare policies at similar levels of law violation, we discretize
the range of mean law penalties
μlaw​(π)\mu\_{\mathrm{law}}(\pi) into contiguous bands

|  |  |  |
| --- | --- | --- |
|  | Bk=[ℓk,uk),k=1,…,K,B\_{k}=\bigl[\ell\_{k},u\_{k}\bigr),\qquad k=1,\dots,K, |  |

where (ℓk,uk)(\ell\_{k},u\_{k}) are chosen such that the bands roughly align with
the empirical distribution of μlaw​(π)\mu\_{\mathrm{law}}(\pi) across policies.
For the numerical example in Section [7](https://arxiv.org/html/2511.17304v1#S7 "7 Empirical Results: From RL Dynamics to Law-Strength Frontiers ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), we use the
band [0.0053,0.0057][0.0053,0.0057] that contains the Zero-Hedge baseline and at
least one RL policy. For each band BkB\_{k} we identify the subset

|  |  |  |
| --- | --- | --- |
|  | Πk:={π:μlaw​(π)∈Bk},\Pi\_{k}:=\bigl\{\pi:\mu\_{\mathrm{law}}(\pi)\in B\_{k}\bigr\}, |  |

and perform intra-band comparisons of Sharpe, GFI, VaR5,
and CVaR5.

##### Pareto frontier extraction.

Given a subset of metrics (μlaw,Sharpe)(\mu\_{\mathrm{law}},\mathrm{Sharpe}),
(μlaw,GFI)(\mu\_{\mathrm{law}},\mathrm{GFI}), or
(μlaw,CVaR5)(\mu\_{\mathrm{law}},\mathrm{CVaR}\_{5}), we say that a policy
π\pi *Pareto-dominates* another policy π′\pi^{\prime} if it is no worse
on all objectives and strictly better on at least one. For example, in
the (μlaw,Sharpe)(\mu\_{\mathrm{law}},\mathrm{Sharpe}) plane we define

|  |  |  |
| --- | --- | --- |
|  | π≻π′⟺μlaw​(π)≤μlaw​(π′)​and​Sharpe​(π)≥Sharpe​(π′),\pi\succ\pi^{\prime}\quad\Longleftrightarrow\quad\mu\_{\mathrm{law}}(\pi)\leq\mu\_{\mathrm{law}}(\pi^{\prime})\;\text{and}\;\mathrm{Sharpe}(\pi)\geq\mathrm{Sharpe}(\pi^{\prime}), |  |

with at least one strict inequality. The empirical law-strength
frontier is the set

|  |  |  |
| --- | --- | --- |
|  | ℱ:={π:∄​π′​such that​π′≻π}.\mathcal{F}:=\bigl\{\pi:\nexists\pi^{\prime}\ \text{such that}\ \pi^{\prime}\succ\pi\bigr\}. |  |

In all planes considered, the points corresponding to Zero-Hedge and
Vol-Trend lie on ℱ\mathcal{F}, while all RL variants lie strictly
inside the frontier: there exists at least one structural baseline that
has both (i) weakly lower mean law penalty and (ii) strictly better
Sharpe, GFI, or tail risk. This is the empirical content of the
Pareto-dominance statements.

### E.4 Additional notes on dynamics and diagnostics

For completeness, we briefly comment on the additional curves and histograms:

1. 1.

   Dynamics Plots
   Each panel shows time-series of cumulative P&L and mean
   law penalty across episodes for Naive RL, a representative
   law-seeking RL variant (e.g. λ=20\lambda=20), and a structural
   baseline. The additional curves omitted from the main text for
   brevity (e.g. λ=5,10,40\lambda=5,10,40) display the same qualitative
   pattern: increasing λ\lambda reduces law penalties at the cost
   of lower P&L, in line with the structural trade-off.
2. 2.

   Diagnostic Plots.
   The scatter plots aggregate step-level observations of
   P&L vs. law penalty across many episodes. The high-density
   clusters for RL policies lie in regions of elevated law
   penalty, while structural baselines concentrate near lower
   penalty bands. Histograms of law penalty show that RL policies
   allocate substantial mass to the right tail of the penalty
   distribution, consistent with exploiting the ghost channel
   r⟂r^{\perp} identified in
   Proposition [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

These supplementary plots are therefore consistent with, and reinforce,
the three main empirical takeaways:
(i) law penalties do not rescue naive RL from ghost arbitrage, (ii)
structural baselines define an empirical law-strength frontier, and
(iii) unconstrained law-seeking RL lies strictly inside this frontier in
our volatility world-model testbed.

## Appendix F No-Free-Lunch for Law-Seeking RL (Proofs)

This appendix provides a detailed proof of the no-free-lunch result stated as Theorem.
We proceed in three steps: (i) we recall the performance and law-metric
quantities used in the main result, (ii) we formalize a mild
ghost–law monotonicity condition that links off-manifold reward to
law metrics, and (iii) we give a detailed proof of the theorem.

### F.1 Preliminaries: performance, law metrics, and decomposition

Recall from Sections [2](https://arxiv.org/html/2511.17304v1#S2 "2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"),
[3](https://arxiv.org/html/2511.17304v1#S3 "3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")that for any stationary
policy π\pi in the unconstrained policy class Π\Pi we have:

1. 1.

   A *baseline* environment distribution
   ℙbase\mathbb{P}^{\text{base}} over episodes generated by the
   law-consistent synthetic generator and the world model.
2. 2.

   A *shock* distribution ℙshock\mathbb{P}^{\mathrm{shock}} describing
   the same world model, but driven by shocked long-variance and spot
   volatility factors.
3. 3.

   A per-step reward r​(st,at)r(s\_{t},a\_{t}) that can be decomposed as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | r​(st,at)=rℳ​(st,at)+r⟂​(st,at),r(s\_{t},a\_{t})=r^{\mathcal{M}}(s\_{t},a\_{t})\;+\;r^{\perp}(s\_{t},a\_{t}), |  | (95) |

   where rℳr^{\mathcal{M}} is the on-manifold component defined by
   projection onto the volatility law manifold ℳvol\mathcal{M}\_{\mathrm{vol}} and r⟂r^{\perp} is
   the ghost (off-manifold) component; see
   Propositions [4](https://arxiv.org/html/2511.17304v1#Thmproposition4 "Proposition 4 (Ghost reward bounded by law distance). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") and
   [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").

We denote by J0​(π)J\_{0}(\pi) the expected (per-step or per-episode) P&L
under the baseline regime:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J0(π):=𝔼ℙbase[r(st,at)],at∼π(⋅∣st),J\_{0}(\pi):=\mathbb{E}\_{\mathbb{P}^{\text{base}}}\Bigl[r(s\_{t},a\_{t})\Bigr],\qquad a\_{t}\sim\pi(\cdot\mid s\_{t}), |  | (96) |

and similarly define the on-manifold and ghost components

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jℳ​(π):=𝔼ℙbase​[rℳ​(st,at)],J⟂​(π):=𝔼ℙbase​[r⟂​(st,at)],J^{\mathcal{M}}(\pi):=\mathbb{E}\_{\mathbb{P}^{\text{base}}}\bigl[r^{\mathcal{M}}(s\_{t},a\_{t})\bigr],\qquad J^{\perp}(\pi):=\mathbb{E}\_{\mathbb{P}^{\text{base}}}\bigl[r^{\perp}(s\_{t},a\_{t})\bigr], |  | (97) |

so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J0​(π)=Jℳ​(π)+J⟂​(π).J\_{0}(\pi)=J^{\mathcal{M}}(\pi)+J^{\perp}(\pi). |  | (98) |

##### Law metrics.

For each policy π\pi we also consider a vector of law metrics,
measuring law violations and robustness:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(π):=(μlawbase​(π),μlawshock​(π),GFI​(π))∈ℝ3,\ell(\pi):=\Bigl(\mu\_{\mathrm{law}}^{\text{base}}(\pi),\;\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi),\;\mathrm{GFI}(\pi)\Bigr)\in\mathbb{R}^{3}, |  | (99) |

where:

1. 1.

   μlawbase​(π)\mu\_{\mathrm{law}}^{\text{base}}(\pi) is the mean step
   law-penalty under ℙbase\mathbb{P}^{\text{base}},
2. 2.

   μlawshock​(π)\mu\_{\mathrm{law}}^{\mathrm{shock}}(\pi) is the mean step law-penalty
   under ℙshock\mathbb{P}^{\mathrm{shock}}, and
3. 3.

   GFI​(π)\mathrm{GFI}(\pi) is the Graceful Failure Index introduced in
   Section [4.4](https://arxiv.org/html/2511.17304v1#S4.SS4 "4.4 Law-strength frontier and Graceful Failure Index ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), which normalizes the change in
   law metrics between baseline and shock by the shock intensity
   IshockI\_{\mathrm{shock}}.

We write ℓ​(π)≤lawℓ​(π′)\ell(\pi)\leq\_{\mathrm{law}}\ell(\pi^{\prime}) if each component of
ℓ​(π)\ell(\pi) is less than or equal to the corresponding component of
ℓ​(π′)\ell(\pi^{\prime}), i.e. if policy π\pi is at least as law-aligned and
robust as π′\pi^{\prime}.

##### Structural class.

The structural strategy class 𝒮\mathcal{S}, introduced in
Section, is a low-capacity, law-aligned
subset of Π\Pi consisting of structurally constrained strategies such
as Zero-Hedge and Vol-Trend. We assume that 𝒮\mathcal{S} satisfies the
*near-optimal on-manifold* property of
Assumption [1](https://arxiv.org/html/2511.17304v1#Thmassumption1 "Assumption 1 (On-manifold near-optimality of structural class). ‣ 4.2 Naive RL and ghost-arbitrage incentive ‣ 4 RL on Volatility World Models: Incentives and Law-Strength ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"):
there exists π𝒮⋆∈𝒮\pi\_{\mathcal{S}}^{\star}\in\mathcal{S} and
ε𝒮≥0\varepsilon\_{\mathcal{S}}\geq 0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jℳ​(π)≤Jℳ​(π𝒮⋆)+ε𝒮for all π∈Π with trajectories supported on ℳvol,J^{\mathcal{M}}(\pi)\;\leq\;J^{\mathcal{M}}(\pi\_{\mathcal{S}}^{\star})+\varepsilon\_{\mathcal{S}}\qquad\text{for all $\pi\in\Pi$ with trajectories supported on $\mathcal{M}\_{\mathrm{vol}}$,} |  | (100) |

and ℓ​(π𝒮⋆)\ell(\pi\_{\mathcal{S}}^{\star}) is uniformly small in the sense of
Proposition [7](https://arxiv.org/html/2511.17304v1#Thmproposition7 "Proposition 7 (Law-alignment of structural baselines). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds") (law-aligned class).

### F.2 Ghost–law monotonicity

The results show that in our volatility world-model
testbed:

1. 1.

   the ghost reward r⟂r^{\perp} is generated by deviations in the
   normal cone Nℳvol​(w)N\_{\mathcal{M}\_{\mathrm{vol}}}(w) to the volatility law manifold,
2. 2.

   the law penalty ℒvol\mathcal{L}\_{\mathrm{vol}} grows with the
   squared distance to ℳvol\mathcal{M}\_{\mathrm{vol}} (Propositions [3](https://arxiv.org/html/2511.17304v1#Thmproposition3 "Proposition 3 (Zero penalty iff axiomatic consistency). ‣ 2.3 Law-Penalty Functionals and Ghost Sensitivity ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
   and [4](https://arxiv.org/html/2511.17304v1#Thmproposition4 "Proposition 4 (Ghost reward bounded by law distance). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),
3. 3.

   the Graceful Failure Index GFI\mathrm{GFI} captures the
   *relative increase* in law penalties under shock.

These observations motivate the following mild monotonicity condition
linking ghost reward and law metrics.

Assumption E.1 (Ghost–law monotonicity).
*There exists a law-aligned structural reference policy
π𝒮⋆∈𝒮\pi\_{\mathcal{S}}^{\star}\in\mathcal{S} and a non-decreasing function
ψ:ℝ+3→ℝ+\psi:\mathbb{R}\_{+}^{3}\to\mathbb{R}\_{+} with ψ​(0,0,0)=0\psi(0,0,0)=0 such that for
every policy π∈Π\pi\in\Pi we have*

|  |  |  |  |
| --- | --- | --- | --- |
|  | J⟂​(π)−J⟂​(π𝒮⋆)≤ψ​((ℓ​(π)−ℓ​(π𝒮⋆))+),J^{\perp}(\pi)-J^{\perp}(\pi\_{\mathcal{S}}^{\star})\;\leq\;\psi\Bigl(\bigl(\ell(\pi)-\ell(\pi\_{\mathcal{S}}^{\star})\bigr)\_{+}\Bigr), |  | (101) |

*where (⋅)+(\cdot)\_{+} denotes component-wise positive part. In particular,
if ℓ​(π)≤lawℓ​(π𝒮⋆)\ell(\pi)\leq\_{\mathrm{law}}\ell(\pi\_{\mathcal{S}}^{\star}) then
J⟂​(π)≤J⟂​(π𝒮⋆)J^{\perp}(\pi)\leq J^{\perp}(\pi\_{\mathcal{S}}^{\star}).*

Intuitively, Assumption E.1 states that *any additional ghost
reward beyond what is available to the structural class must be paid
for by worse law metrics*. In our volatility setting, the existence of
such a function ψ\psi is supported by:

1. 1.

   the Lipschitz bound of Proposition [4](https://arxiv.org/html/2511.17304v1#Thmproposition4 "Proposition 4 (Ghost reward bounded by law distance). ‣ 2.4 Goodhart Decomposition on Law Manifolds (Conceptual) ‣ 2 Axiomatic Volatility Law Manifolds ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"),
   which controls |r⟂​(w)||r^{\perp}(w)| in terms of the distance to ℳvol\mathcal{M}\_{\mathrm{vol}};
2. 2.

   the definition of law penalties and GFI as functions of the
   same distance and its behavior under shock;
3. 3.

   the law-aligned nature of π𝒮⋆\pi\_{\mathcal{S}}^{\star} guaranteed
   by Proposition [7](https://arxiv.org/html/2511.17304v1#Thmproposition7 "Proposition 7 (Law-alignment of structural baselines). ‣ 5.2 Law-alignment properties of structural baselines ‣ 5 Structural Baselines: Axiomatic Strategy Class 𝒮 ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"), which ensures that
   ℓ​(π𝒮⋆)\ell(\pi\_{\mathcal{S}}^{\star}) is close to the best achievable law
   metrics given the world-model approximation error.

Thus, in the neighborhood of π𝒮⋆\pi\_{\mathcal{S}}^{\star}, additional
ghost reward can only be obtained by moving further away from the law
manifold, which necessarily worsens at least one component of the law
metric vector.

### F.3 Proof of the no-free-lunch theorem

We now give a detailed proof of the no-free-lunch result stated as theorem. For clarity we restate the theorem in a
slightly more quantitative form.

###### Theorem (No-free-lunch for unconstrained law-seeking RL).

Assume:

1. 1.

   The structural class 𝒮\mathcal{S} is law-aligned and
   near-optimal on-manifold in the sense of
   ([100](https://arxiv.org/html/2511.17304v1#A6.E100 "In Structural class. ‣ F.1 Preliminaries: performance, law metrics, and decomposition ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), with reference policy
   π𝒮⋆\pi\_{\mathcal{S}}^{\star}.
2. 2.

   The world model induces a non-trivial ghost channel as in
   Propositions [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
   and [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds").
3. 3.

   Ghost–law monotonicity (Assumption E.1) holds for
   π𝒮⋆\pi\_{\mathcal{S}}^{\star}.

Then for any η>ε𝒮\eta>\varepsilon\_{\mathcal{S}} and any policy
π∈Π\pi\in\Pi satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | J0​(π)≥J0​(π𝒮⋆)+η,J\_{0}(\pi)\;\geq\;J\_{0}(\pi\_{\mathcal{S}}^{\star})+\eta, |  | (102) |

we must have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(π)≰lawℓ​(π𝒮⋆),\ell(\pi)\not\leq\_{\mathrm{law}}\ell(\pi\_{\mathcal{S}}^{\star}), |  | (103) |

i.e., at least one component of the law metric vector is strictly worse
for π\pi than for π𝒮⋆\pi\_{\mathcal{S}}^{\star}. In particular, no policy
π∈Π\pi\in\Pi can strictly dominate π𝒮⋆\pi\_{\mathcal{S}}^{\star} on all axes
(P&L, law penalties, and GFI).

###### Proof.

Fix η>ε𝒮\eta>\varepsilon\_{\mathcal{S}} and suppose, for contradiction,
that there exists a policy π∈Π\pi\in\Pi such that
([102](https://arxiv.org/html/2511.17304v1#A6.E102 "In Theorem (No-free-lunch for unconstrained law-seeking RL). ‣ F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) holds and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(π)≤lawℓ​(π𝒮⋆).\ell(\pi)\leq\_{\mathrm{law}}\ell(\pi\_{\mathcal{S}}^{\star}). |  | (104) |

We will show that this contradicts the decomposition
([98](https://arxiv.org/html/2511.17304v1#A6.E98 "In F.1 Preliminaries: performance, law metrics, and decomposition ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), near-optimality
([100](https://arxiv.org/html/2511.17304v1#A6.E100 "In Structural class. ‣ F.1 Preliminaries: performance, law metrics, and decomposition ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), and ghost–law monotonicity
([101](https://arxiv.org/html/2511.17304v1#A6.E101 "In F.2 Ghost–law monotonicity ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).

Step 1: Decomposing the P&L difference.
By ([98](https://arxiv.org/html/2511.17304v1#A6.E98 "In F.1 Preliminaries: performance, law metrics, and decomposition ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), for any π\pi we have

|  |  |  |
| --- | --- | --- |
|  | J0​(π)=Jℳ​(π)+J⟂​(π).J\_{0}(\pi)=J^{\mathcal{M}}(\pi)+J^{\perp}(\pi). |  |

Therefore,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J0​(π)−J0​(π𝒮⋆)\displaystyle J\_{0}(\pi)-J\_{0}(\pi\_{\mathcal{S}}^{\star}) | =(Jℳ​(π)−Jℳ​(π𝒮⋆))+(J⟂​(π)−J⟂​(π𝒮⋆)).\displaystyle=\bigl(J^{\mathcal{M}}(\pi)-J^{\mathcal{M}}(\pi\_{\mathcal{S}}^{\star})\bigr)+\bigl(J^{\perp}(\pi)-J^{\perp}(\pi\_{\mathcal{S}}^{\star})\bigr). |  | (105) |

Step 2: Bounding the on-manifold component.
By near-optimality of π𝒮⋆\pi\_{\mathcal{S}}^{\star} on the law manifold,
([100](https://arxiv.org/html/2511.17304v1#A6.E100 "In Structural class. ‣ F.1 Preliminaries: performance, law metrics, and decomposition ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jℳ​(π)≤Jℳ​(π𝒮⋆)+ε𝒮for all π∈Π.J^{\mathcal{M}}(\pi)\;\leq\;J^{\mathcal{M}}(\pi\_{\mathcal{S}}^{\star})+\varepsilon\_{\mathcal{S}}\qquad\text{for all $\pi\in\Pi$.} |  | (106) |

Substituting ([106](https://arxiv.org/html/2511.17304v1#A6.E106 "In F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) into
([105](https://arxiv.org/html/2511.17304v1#A6.E105 "In F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | J0​(π)−J0​(π𝒮⋆)≤ε𝒮+(J⟂​(π)−J⟂​(π𝒮⋆)).J\_{0}(\pi)-J\_{0}(\pi\_{\mathcal{S}}^{\star})\;\leq\;\varepsilon\_{\mathcal{S}}+\bigl(J^{\perp}(\pi)-J^{\perp}(\pi\_{\mathcal{S}}^{\star})\bigr). |  | (107) |

Step 3: Applying ghost–law monotonicity.
By the assumption ([104](https://arxiv.org/html/2511.17304v1#A6.E104 "In F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")),
ℓ​(π)≤lawℓ​(π𝒮⋆)\ell(\pi)\leq\_{\mathrm{law}}\ell(\pi\_{\mathcal{S}}^{\star}), we have

|  |  |  |
| --- | --- | --- |
|  | (ℓ​(π)−ℓ​(π𝒮⋆))+=0,\bigl(\ell(\pi)-\ell(\pi\_{\mathcal{S}}^{\star})\bigr)\_{+}=0, |  |

so ghost–law monotonicity ([101](https://arxiv.org/html/2511.17304v1#A6.E101 "In F.2 Ghost–law monotonicity ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | J⟂​(π)−J⟂​(π𝒮⋆)≤ψ​(0,0,0)=0.J^{\perp}(\pi)-J^{\perp}(\pi\_{\mathcal{S}}^{\star})\;\leq\;\psi(0,0,0)=0. |  | (108) |

Combining ([107](https://arxiv.org/html/2511.17304v1#A6.E107 "In F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) and
([108](https://arxiv.org/html/2511.17304v1#A6.E108 "In F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | J0​(π)−J0​(π𝒮⋆)≤ε𝒮.J\_{0}(\pi)-J\_{0}(\pi\_{\mathcal{S}}^{\star})\;\leq\;\varepsilon\_{\mathcal{S}}. |  | (109) |

Step 4: Contradiction.
However, by assumption ([102](https://arxiv.org/html/2511.17304v1#A6.E102 "In Theorem (No-free-lunch for unconstrained law-seeking RL). ‣ F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")) we have

|  |  |  |
| --- | --- | --- |
|  | J0​(π)−J0​(π𝒮⋆)≥η>ε𝒮,J\_{0}(\pi)-J\_{0}(\pi\_{\mathcal{S}}^{\star})\;\geq\;\eta\;>\;\varepsilon\_{\mathcal{S}}, |  |

which contradicts ([109](https://arxiv.org/html/2511.17304v1#A6.E109 "In F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). Therefore no policy
π\pi can simultaneously satisfy ([102](https://arxiv.org/html/2511.17304v1#A6.E102 "In Theorem (No-free-lunch for unconstrained law-seeking RL). ‣ F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds"))
and ([104](https://arxiv.org/html/2511.17304v1#A6.E104 "In F.3 Proof of the no-free-lunch theorem ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). Equivalently, any policy achieving an
improvement in baseline P&L of more than ε𝒮\varepsilon\_{\mathcal{S}}
over the structural reference π𝒮⋆\pi\_{\mathcal{S}}^{\star} must have at
least one law metric strictly worse than that of
π𝒮⋆\pi\_{\mathcal{S}}^{\star}, i.e. ℓ​(π)≰lawℓ​(π𝒮⋆)\ell(\pi)\not\leq\_{\mathrm{law}}\ell(\pi\_{\mathcal{S}}^{\star}).

In particular, if we interpret the triple

|  |  |  |
| --- | --- | --- |
|  | (−J0​(π),ℓ​(π))∈ℝ1+3\bigl(-J\_{0}(\pi),\;\ell(\pi)\bigr)\in\mathbb{R}^{1+3} |  |

as a four-dimensional loss vector (profitability vs. law alignment and
robustness), then π𝒮⋆\pi\_{\mathcal{S}}^{\star} cannot be strictly
Pareto-dominated by any policy in Π\Pi. This is the claimed
no-free-lunch property.
∎

### F.4 Discussion of assumptions and empirical alignment

The proof above separates the no-free-lunch result into three conceptually
distinct ingredients:

1. 1.

   *On-manifold near-optimality of 𝒮\mathcal{S}.*
   The structural class 𝒮\mathcal{S} contains a policy
   π𝒮⋆\pi\_{\mathcal{S}}^{\star} that is nearly optimal in terms of
   on-manifold P&L, as quantified by
   ([100](https://arxiv.org/html/2511.17304v1#A6.E100 "In Structural class. ‣ F.1 Preliminaries: performance, law metrics, and decomposition ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")). Empirically this corresponds to
   the observation that Zero-Hedge and Vol-Trend already sit very
   close to the empirical law-strength frontier.
2. 2.

   *Non-trivial ghost channel.*
   The world model induces off-manifold reward r⟂r^{\perp} that is
   non-zero whenever predictions deviate from ℳvol\mathcal{M}\_{\mathrm{vol}}
   (Propositions [6](https://arxiv.org/html/2511.17304v1#Thmproposition6 "Proposition 6 (Approximation gap induces a ghost channel). ‣ Architecture and training. ‣ 3.2 Neural world model and approximation gap ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")
   and [2](https://arxiv.org/html/2511.17304v1#Thmlemma2 "Lemma 2 (Non-trivial off-manifold mass of the world model). ‣ Law penalties of predictions vs. ground truth. ‣ 3.4 World-model diagnostics and dynamics plots ‣ 3 Volatility World Model: Law-Consistent Ground Truth vs Law-Violating Predictions ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")), creating the possibility of
   “ghost arbitrage”.
3. 3.

   *Ghost–law monotonicity.*
   Assumption E.1 formalizes the idea that exploiting the ghost channel
   necessarily worsens law metrics: additional ghost reward cannot be
   obtained at fixed or improved law penalties and GFI.

In our volatility world-model testbed, these three conditions are
jointly consistent with the empirical findings of
Section:

1. 1.

   The structural baselines achieve high Sharpe and low GFI while
   remaining close to the law manifold, in line with
   near-optimality ([100](https://arxiv.org/html/2511.17304v1#A6.E100 "In Structural class. ‣ F.1 Preliminaries: performance, law metrics, and decomposition ‣ Appendix F No-Free-Lunch for Law-Seeking RL (Proofs) ‣ Law-Strength Frontiers and a No-Free-Lunch Result for Law-Seeking Reinforcement Learning on Volatility Law Manifolds")).
2. 2.

   Naive and law-seeking RL policies that outperform 𝒮\mathcal{S}
   in raw P&L do so only by moving into high-penalty, high-GFI
   regions, as evidenced by the frontier and diagnostic plots.
3. 3.

   No RL policy lies on the empirical law-strength frontier once
   the structural baselines are included, which matches the
   impossibility of strict dominance established by the theorem.

## References

* [1]

  B. Dupire.
  Pricing with a smile.
  Risk, 7(1):18–20, 1994.
* [2]

  J. Gatheral.
  The Volatility Surface: A Practitioner’s Guide.
  John Wiley & Sons, 2006.
* [3]

  M. R. Fengler.
  Semiparametric Modeling of Implied Volatility.
  Springer, 2005.
* [4]

  P. Carr and D. B. Madan.
  Option valuation using the fast Fourier transform.
  Journal of Computational Finance, 2(4):61–73, 1999.
* [5]

  R. W. Lee.
  The moment formula for implied volatility at extreme strikes.
  Mathematical Finance, 14(3):469–480, 2004.
* [6]

  R. Cont and P. Tankov.
  Financial Modelling with Jump Processes.
  Chapman and Hall/CRC, 2004.
* [7]

  L. Bergomi.
  Stochastic Volatility Modeling.
  Chapman and Hall/CRC, 2016.
* [8]

  J. Gatheral and A. Jacquier.
  Arbitrage-free SVI volatility surfaces.
  Quantitative Finance, 14(1):59–71, 2014.
* [9]

  C. Bayer, P. Friz, and J. Gatheral.
  Pricing under rough volatility.
  Quantitative Finance, 16(6):887–904, 2016.
* [10]

  B. Horváth, A. Muguruza, and M. Tomas.
  Deep learning volatility: Deep calibration of rough stochastic volatility models.
  Quantitative Finance, 21(1):11–29, 2021.
* [11]

  B. Horváth, A. Jacquier, and C. Kovács.
  Deep learning volatility.
  Quantitative Finance, 21(11):1763–1783, 2021.
* [12]

  A. Itkin.
  Calibration of local stochastic volatility models to market data.
  Journal of Computational Finance, 18(3):1–46, 2015.
* [13]

  S. De Marco and P. Henry-Labordère.
  Linking vanillas and VIX options: A constrained optimization approach.
  Journal of Computational Finance, 19(1):29–64, 2015.
* [14]

  D. Guterding.
  A sparse modeling approach to the arbitrage-free interpolation of plain-vanilla option prices and implied volatilities.
  Risks, 11(1):1–28, 2023.
* [15]

  J. Ruf and W. Wang.
  Neural network-based option pricing.
  arXiv preprint arXiv:1912.02710, 2020.
* [16]

  P. Carr and D. B. Madan.
  A note on sufficient conditions for no arbitrage.
  Available at SSRN, 2005.
* [17]

  P. S. Hagan and G. West.
  Interpolation methods for curve construction.
  Applied Mathematical Finance, 13(2):89–129, 2006.
* [18]

  D. Filipović.
  Term-Structure Models: A Graduate Course.
  Springer, 2009.
* [19]

  D. Filipović.
  Consistency Problems for Heath–Jarrow–Morton Interest Rate Models.
  Springer, 2001.
* [20]

  T. Björk and B. J. Christensen.
  Interest rate dynamics and consistent forward rate curves.
  Mathematical Finance, 9(4):323–348, 1999.
* [21]

  P. Artzner, F. Delbaen, J.-M. Eber, and D. Heath.
  Coherent measures of risk.
  Mathematical Finance, 9(3):203–228, 1999.
* [22]

  R. T. Rockafellar and S. Uryasev.
  Optimization of conditional value-at-risk.
  Journal of Risk, 2(3):21–42, 2000.
* [23]

  Á. Cartea, S. Jaimungal, and J. Penalva.
  Algorithmic and High-Frequency Trading.
  Cambridge University Press, 2015.
* [24]

  B. Hurst, Y. H. Ooi, and L. H. Pedersen.
  A century of evidence on trend-following investing.
  Journal of Portfolio Management, 44(1):15–29, 2017.
* [25]

  Z. Zhang and S. Zohren.
  Deep reinforcement learning for trading.
  Journal of Financial Data Science, 2(2):25–40, 2020.
* [26]

  H. H. Bauschke and P. L. Combettes.
  Convex Analysis and Monotone Operator Theory in Hilbert Spaces.
  Springer, 2011.
* [27]

  S. N. Cohen and R. J. Elliott.
  Stochastic Calculus and Applications.
  Birkhäuser, 2nd edition, 2015.
* [28]

  M. Belkin, P. Niyogi, and V. Sindhwani.
  Manifold regularization: A geometric framework for learning from labeled and unlabeled examples.
  Journal of Machine Learning Research, 7:2399–2434, 2006.
* [29]

  C. Fefferman, S. Mitter, and H. Narayanan.
  Testing the manifold hypothesis.
  Journal of the American Mathematical Society, 29(4):983–1049, 2016.
* [30]

  J. Han, A. Jentzen, and W. E.
  Solving high-dimensional partial differential equations using deep learning.
  Proceedings of the National Academy of Sciences, 115(34):8505–8510, 2018.
* [31]

  C. Beck, S. Becker, P. Cheridito, A. Jentzen, and A. Neufeld.
  Machine learning approximation algorithms for high-dimensional fully nonlinear partial differential equations and second-order backward SDEs.
  Journal of Scientific Computing, 79(3):1393–1438, 2019.
* [32]

  M. Raissi, P. Perdikaris, and G. E. Karniadakis.
  Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.
  Journal of Computational Physics, 378:686–707, 2019.
* [33]

  M. Raissi, P. Perdikaris, and G. E. Karniadakis.
  Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.
  Journal of Computational Physics, 378:686–707, 2019.
* [34]

  G. E. Karniadakis, I. G. Kevrekidis, L. Lu, P. Perdikaris, S. Wang, and L. Yang.
  Physics-informed machine learning.
  Acta Numerica, 30:1–146, 2021.
* [35]

  G. Carleo, J. Cirac, K. Cranmer, et al.
  Machine learning and the physical sciences.
  Reviews of Modern Physics, 91(4):045002, 2019.
* [36]

  J. Willard, X. Jia, S. Xu, M. Steinbach, and V. Kumar.
  Integrating physics-based modeling with machine learning: A survey.
  ACM Computing Surveys, 52(3):1–39, 2020.
* [37]

  C. Beck, C. Ehlers, et al.
  Solving stochastic differential equations and Kolmogorov equations by deep learning.
  Annals of Applied Probability, 31(4):1917–1966, 2021.
* [38]

  J. Brandstetter, M. Welling, and A. Ansuini.
  Message passing neural PDE solvers.
  In International Conference on Learning Representations, 2022.
* [39]

  P. W. Battaglia, J. B. Hamrick, V. Bapst, et al.
  Relational inductive biases, deep learning, and graph networks.
  arXiv preprint arXiv:1806.01261, 2018.
* [40]

  D. Ha and J. Schmidhuber.
  World models.
  arXiv preprint arXiv:1803.10122, 2018.
* [41]

  D. Hafner, T. Lillicrap, M. Norouzi, and J. Ba.
  Learning latent dynamics for planning from pixels.
  In Proceedings of the 36th International Conference on Machine Learning, 2019.
* [42]

  D. Hafner, T. Lillicrap, M. Norouzi, and J. Ba.
  Dream to control: Learning behaviors by latent imagination.
  In International Conference on Learning Representations, 2020.
* [43]

  D. Hafner, J. Pasukonis, J. Ba, and M. Norouzi.
  Mastering diverse domains with world models.
  arXiv preprint arXiv:2301.04104, 2023.
* [44]

  K. Chua, R. Calandra, R. McAllister, and S. Levine.
  Deep reinforcement learning in a handful of trials using probabilistic dynamics models.
  In Advances in Neural Information Processing Systems, 2018.
* [45]

  M. Janner, J. Fu, M. Zhang, and S. Levine.
  When to trust your model: Model-based policy optimization.
  In Advances in Neural Information Processing Systems, 2019.
* [46]

  Ł. Kaiser, M. Babaeizadeh, P. Milos, B. Osinski, R. Campbell, K. Czechowski, D. Erhan, C. Finn, P. Kozakowski, S. Levine, et al.
  Model-based reinforcement learning for Atari.
  In International Conference on Learning Representations, 2020.
* [47]

  J. Schrittwieser, I. Antonoglou, T. Hubert, et al.
  Mastering Atari, Go, chess and shogi by planning with a learned model.
  Nature, 588:604–609, 2020.
* [48]

  V. Mnih, K. Kavukcuoglu, D. Silver, et al.
  Human-level control through deep reinforcement learning.
  Nature, 518:529–533, 2015.
* [49]

  R. S. Sutton and A. G. Barto.
  Reinforcement Learning: An Introduction.
  MIT Press, 2nd edition, 2018.
* [50]

  V. R. Konda and J. N. Tsitsiklis.
  Actor-critic algorithms.
  In Advances in Neural Information Processing Systems, pages 1008–1014, 2000.
* [51]

  P. S. Thomas.
  Bias in natural actor-critic algorithms.
  In Proceedings of the 31st International Conference on Machine Learning, pages 441–448, 2014.
* [52]

  J. Schulman, P. Moritz, S. Levine, M. I. Jordan, and P. Abbeel.
  High-dimensional continuous control using generalized advantage estimation.
  In International Conference on Learning Representations, 2016.
* [53]

  J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov.
  Proximal policy optimization algorithms.
  arXiv preprint arXiv:1707.06347, 2017.
* [54]

  E. Altman.
  Constrained Markov Decision Processes.
  Chapman & Hall/CRC, 1999.
* [55]

  J. Achiam, D. Held, A. Tamar, and P. Abbeel.
  Constrained policy optimization.
  In International Conference on Machine Learning, pages 22–31, 2017.
* [56]

  S. Mannor and J. N. Tsitsiklis.
  Mean-variance optimization in Markov decision processes.
  Operations Research, 59(2):350–367, 2011.
* [57]

  Y. Chow, A. Tamar, S. Mannor, and M. Pavone.
  Risk-sensitive and robust decision-making: A CVaR optimization approach.
  In Advances in Neural Information Processing Systems, pages 1522–1530, 2015.
* [58]

  D. M. Roijers, P. Vamplew, S. Whiteson, and R. Dazeley.
  A survey of multi-objective sequential decision-making.
  Journal of Artificial Intelligence Research, 48:67–113, 2013.
* [59]

  G. Neu, A. György, and C. Szepesvári.
  A unified view of entropy-regularized Markov decision processes.
  In Advances in Neural Information Processing Systems, 2017.
* [60]

  M. Geist, B. Scherrer, and O. Pietquin.
  A theory of regularized Markov decision processes.
  In Proceedings of the 36th International Conference on Machine Learning, pages 2160–2169, 2019.
* [61]

  Y. Jiang, et al.
  Towards safe reinforcement learning: A survey and outlook.
  arXiv preprint arXiv:2109.14597, 2021.
* [62]

  Z. Hou, Y. Chen, and M. Wang.
  Regularized policy optimization in MDPs with constraints.
  SIAM Journal on Optimization, 31(1):192–223, 2021.
* [63]

  J. Moody and M. Saffell.
  Learning to trade via direct reinforcement.
  IEEE Transactions on Neural Networks, 12(4):875–889, 2001.
* [64]

  Y. Deng, F. Bao, Y. Kong, Z. Ren, and Q. Dai.
  Deep direct reinforcement learning for financial signal representation and trading.
  IEEE Transactions on Neural Networks and Learning Systems, 28(3):653–664, 2016.
* [65]

  Z. Jiang, D. Xu, and J. Liang.
  A deep reinforcement learning framework for the financial portfolio management problem.
  arXiv preprint arXiv:1706.10059, 2017.
* [66]

  X.-Y. Liu, R. Yang, Z. Zhu, et al.
  FinRL: A deep reinforcement learning library for quantitative finance.
  ACM Transactions on Management Information Systems, 12(2):1–30, 2021.
* [67]

  P. N. Kolm and G. Ritter.
  Dynamic replication and hedging: A reinforcement learning approach.
  The Journal of Financial Data Science, 1(2):71–88, 2019.
* [68]

  H. Buehler, L. Gonon, J. Teichmann, and B. Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [69]

  H. Buehler, L. Gonon, J. Teichmann, and B. Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [70]

  H. Buehler, L. Gonon, J. Teichmann, and B. Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [71]

  A. Carbonneau and F. Godin.
  Deep hedging of derivatives with transaction costs and different risk criteria.
  Journal of Computational Finance, 24(2):1–31, 2020.
* [72]

  D. Salinas, V. Flunkert, J. Gasthaus, and T. Januschowski.
  DeepAR: Probabilistic forecasting with autoregressive recurrent networks.
  International Journal of Forecasting, 36(3):1181–1191, 2020.
* [73]

  G. Zerveas, S. Jayaraman, D. Patel, A. Bhamidipati, C. Eickhoff, J. Lévy, and X. Binefa.
  A transformer-based framework for multivariate time series representation learning.
  In Proceedings of the 27th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pages 2114–2124, 2021.
* [74]

  D. Manheim and S. Garrabrant.
  Categorizing variants of Goodhart’s law.
  arXiv preprint arXiv:1803.04585, 2019.
* [75]

  D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. Mané.
  Concrete problems in AI safety.
  arXiv preprint arXiv:1606.06565, 2016.
* [76]

  J. Leike, M. Martic, V. Krakovna, et al.
  AI safety gridworlds.
  In Proceedings of the Thirty-First AAAI Conference on Artificial Intelligence, 2017.
* [77]

  T. Everitt, M. Hutter, and J. Leike.
  Reinforcement learning with a corrupted reward channel.
  arXiv preprint arXiv:1705.08417, 2017.
* [78]

  D. Krueger, T. Maharaj, S. Rahman, et al.
  Hidden incentives in deep reinforcement learning.
  In Advances in Neural Information Processing Systems, 2020.
* [79]

  M. Pan, et al.
  The effects of reward misspecification: Mapping and mitigating misaligned models.
  arXiv preprint arXiv:2209.14935, 2022.
* [80]

  C. F. Hayes, E. Bargiacchi, et al.
  A practical guide to multi-objective reinforcement learning and planning.
  Autonomous Agents and Multi-Agent Systems, 36:1–35, 2022.
* [81]

  Unknown.
  Placeholder entry for the key WangRLAlpha2019. No reliable bibliographic information could be identified; please replace this with the correct reference or remove the citation.
  2019.
* [82]

  A. Neelakantan, et al.
  Placeholder for “Reinforcement learning with verifiable rewards”. No corresponding published work could be found; please update or delete this citation.
  2025.