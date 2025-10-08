---
authors:
- Jian'an Zhang
doc_id: arxiv:2510.04555v1
family_id: arxiv:2510.04555
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with
  a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets'
url_abs: http://arxiv.org/abs/2510.04555v1
url_html: https://arxiv.org/html/2510.04555v1
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

We introduce Tail-Safe, a deployability-oriented framework for derivatives hedging that unifies *distributional, risk-sensitive reinforcement learning* with a *white-box* safety layer tailored to financial constraints.
The learning module combines an IQN-based distributional critic with a CVaR objective (IQN–CVaR–PPO), and is stabilized by a *Tail-Coverage Controller* that regulates quantile sampling via temperature tilting and tail-boosting to preserve effective tail mass at small α\alpha.
The safety module solves a convex *CBF–QP* at every step, enforcing discrete-time control barrier inequalities together with a finance-specific constraint set (ellipsoidal no-trade band, box/rate limits, and a sign-consistency gate).
Crucially, the safety layer is *explainable*: it exposes active sets, tightness, rate utilization, gate scores, slack, and solver status—a self-contained audit trail aligned with model-risk governance.

We provide formal guarantees: (i) *robust forward invariance* of the safe set under bounded model mismatch; (ii) a *minimal-deviation projection* interpretation of the QP; (iii) a *KL–DRO* upper bound showing that per-state KL regularization controls worst-case CVaR; (iv) *concentration* and sample-complexity of the temperature-tilted CVaR estimator with explicit coverage-mismatch terms; (v) a *CVaR trust-region* improvement inequality under KL-limited updates; (vi) *feasibility persistence* via expiry-aware NTB shrinkage and rate tightening; and (vii) *negative-advantage suppression* induced by the sign-consistency gate.
Empirically, in arbitrage-free, microstructure-aware synthetic markets (SSVI→\!\rightarrowDupire→\!\rightarrowVIX with ABIDES/MockLOB execution), Tail-Safe improves left-tail risk while preserving central performance and yields zero hard-constraint violations whenever the QP is feasible with zero slack.
We also map telemetry to governance workflows (dashboards, triggers, and incident taxonomy) to support auditability.
Limitations include the use of synthetic environments, simplified execution, and the absence of real-data replay; these are deliberate to isolate methodological contributions and are actionable in future work.

*K*eywords risk-sensitive reinforcement learning, distributional RL, CVaR, trust-region methods, control barrier functions (CBFs), quadratic programming (QP), safe RL, explainable AI, deep hedging, arbitrage-free volatility (SSVI, Dupire), VIX, market microstructure, distributionally robust optimization (DRO), PPO, IQN, model risk governance

## 1 Introduction

Modern AI agents for derivatives hedging and portfolio risk management must remain *tail-safe*, *robust under distribution shift*, and *auditable* for model risk governance and regulatory review. In equity–volatility books such as SPX–VIX, a small number of rare but consequential events (flash crashes, volatility spikes, liquidity droughts) dominate economic capital, PnL attribution, and operational risk. Agents optimized purely for risk-neutral or average performance—e.g., standard reinforcement learning (RL) objectives or black-box deep hedgers—can look competitive ex post yet still incur catastrophic left-tail losses, violate hard business rules (leverage, short-sale limits, liquidity/min-trade-size, turnover and drawdown constraints), or fail under microstructure stress [[6](https://arxiv.org/html/2510.04555v1#bib.bib6), [10](https://arxiv.org/html/2510.04555v1#bib.bib10), [11](https://arxiv.org/html/2510.04555v1#bib.bib11), [12](https://arxiv.org/html/2510.04555v1#bib.bib12)]. These shortcomings are amplified when training is performed in stylized simulators that under-represent jump risk, regime changes, or execution frictions. At the same time, realistic deployment requires reasoning about market impact, order-book dynamics, and latency that classical optimal execution models capture only partially [[1](https://arxiv.org/html/2510.04555v1#bib.bib1), [5](https://arxiv.org/html/2510.04555v1#bib.bib5), [2](https://arxiv.org/html/2510.04555v1#bib.bib2)]. Taken together, these pressures motivate methods that (i) *optimize tail risk* rather than only the mean, (ii) *guarantee state-wise safety by construction* at execution time, and (iii) *explain interventions* through telemetry that supports model validation and external audit.

##### From risk-neutral RL to risk-sensitive, distributional RL.

A central ingredient is to reason about *distributions of returns* rather than their expectations. Distributional RL explicitly models the random return ZπZ^{\pi} and its quantiles, enabling direct access to tail statistics and risk measures (e.g., VaR/CVaR) that are meaningful for trading books [[13](https://arxiv.org/html/2510.04555v1#bib.bib13), [14](https://arxiv.org/html/2510.04555v1#bib.bib14)]. On-policy trust-region style updates (TRPO/PPO) stabilize training through KL control and clipping, reducing policy oscillations that can otherwise translate into erratic trading [[15](https://arxiv.org/html/2510.04555v1#bib.bib15), [16](https://arxiv.org/html/2510.04555v1#bib.bib16)]. Building on these foundations, risk-sensitive RL incorporates coherent risk measures and chance constraints into the objective or constraints of the Markov decision process, yielding actor–critic and policy-gradient algorithms with convergence guarantees [[17](https://arxiv.org/html/2510.04555v1#bib.bib17), [19](https://arxiv.org/html/2510.04555v1#bib.bib19), [18](https://arxiv.org/html/2510.04555v1#bib.bib18)]. Recent advances scale CVaR-style training, improve tail estimators, and study policy updates under distribution shift and partial model misspecification [[35](https://arxiv.org/html/2510.04555v1#bib.bib35), [36](https://arxiv.org/html/2510.04555v1#bib.bib36), [37](https://arxiv.org/html/2510.04555v1#bib.bib37)]. These directions are especially pertinent in finance, where left-tail losses dominate risk budgets, and where audits require transparent objectives and measurable risk appetites [[9](https://arxiv.org/html/2510.04555v1#bib.bib9), [11](https://arxiv.org/html/2510.04555v1#bib.bib11), [10](https://arxiv.org/html/2510.04555v1#bib.bib10), [12](https://arxiv.org/html/2510.04555v1#bib.bib12)]. In this work we adopt distributional critics and quantile-based losses together with explicit CVaR optimization to shape the tail, while retaining PPO-style update discipline to keep policy drift controlled during training.

##### Safety by construction via control barrier functions (CBFs).

Even with risk-sensitive training, *state-wise* safety constraints (e.g., leverage ≤\leq cap, inventory/rate boxes, NTB and sign consistency) must be satisfied at each decision, not only on average. Typical safe RL approaches enforce constraints asymptotically, in expectation, or via learned proxies, leaving residual violation risk during exploration or regime shifts [[20](https://arxiv.org/html/2510.04555v1#bib.bib20), [21](https://arxiv.org/html/2510.04555v1#bib.bib21), [22](https://arxiv.org/html/2510.04555v1#bib.bib22)]. CBF-based safety layers provide a complementary, *white-box* mechanism: a control barrier function h​(x)h(x) defines a forward-invariant safe set 𝒮={x:h​(x)≥0}\mathcal{S}=\{x:h(x)\geq 0\}; at each step a convex quadratic program (QP) minimally modifies a nominal action u0u\_{0} to ensure a discrete-time CBF condition such as

|  |  |  |
| --- | --- | --- |
|  | h​(xt+1)−(1−α)​h​(xt)≥ 0,h(x\_{t+1})-(1-\alpha)h(x\_{t})\;\geq\;0, |  |

subject to box/rate and market constraints, where α∈(0,1]\alpha\in(0,1] regulates conservatism [[23](https://arxiv.org/html/2510.04555v1#bib.bib23), [24](https://arxiv.org/html/2510.04555v1#bib.bib24)]. The CBF literature now includes high-order and robust variants, differentiable formulations for learning, discrete-time treatments, and observer/disturbance-aware designs suitable for implementation [[25](https://arxiv.org/html/2510.04555v1#bib.bib25), [26](https://arxiv.org/html/2510.04555v1#bib.bib26), [27](https://arxiv.org/html/2510.04555v1#bib.bib27), [28](https://arxiv.org/html/2510.04555v1#bib.bib28), [29](https://arxiv.org/html/2510.04555v1#bib.bib29), [30](https://arxiv.org/html/2510.04555v1#bib.bib30), [31](https://arxiv.org/html/2510.04555v1#bib.bib31), [32](https://arxiv.org/html/2510.04555v1#bib.bib32)]. For financial RL, a CBF–QP safety layer is attractive because it (i) encodes leverage, liquidity, and sign-consistency gates *by construction*; (ii) exposes KKT multipliers, active sets, and slack, yielding human-interpretable *reasons* for action overrides; and (iii) composes with arbitrary nominal policies without retraining.

##### Robustness to model misspecification via distributional robustness and KL control.

Agents trained on synthetic markets inevitably face deployment regimes with different volatility-of-volatility, jump intensities, liquidity states, and order-flow autocorrelations. Distributionally robust MDPs (DRMDPs) guard against such misspecification by optimizing worst-case value within ambiguity sets defined by ff-divergence or Wasserstein balls; practical algorithms cover online/offline and model-based/model-free settings [[37](https://arxiv.org/html/2510.04555v1#bib.bib37), [35](https://arxiv.org/html/2510.04555v1#bib.bib35), [36](https://arxiv.org/html/2510.04555v1#bib.bib36), [38](https://arxiv.org/html/2510.04555v1#bib.bib38)]. In parallel, KL-regularized policy updates—as in TRPO/PPO—admit a robust-optimization reading: a per-state KL penalty is the Fenchel dual of an adversary constrained to a KL ball around the behavior distribution, providing an interpretable *risk-budget knob* for conservatism during tail-focused learning [[15](https://arxiv.org/html/2510.04555v1#bib.bib15), [16](https://arxiv.org/html/2510.04555v1#bib.bib16)]. We further view adversarial/stress-testing methods from robust RL as complementary tools to expose fragilities before live trading [[34](https://arxiv.org/html/2510.04555v1#bib.bib34), [33](https://arxiv.org/html/2510.04555v1#bib.bib33)].

##### Finance-grounded synthetic evaluation.

Auditable studies require *arbitrage-free* yet *stressable* simulators. Practitioners routinely calibrate SSVI volatility surfaces under static no-arbitrage constraints [[3](https://arxiv.org/html/2510.04555v1#bib.bib3)] and derive state-dependent dynamics via Dupire local volatility [[4](https://arxiv.org/html/2510.04555v1#bib.bib4)]. VIX-consistent legs can be inferred from the surface, enabling joint SPX–VIX exposures. Execution realism demands microstructure-aware simulators and impact models: Almgren–Chriss captures linear temporary impact and risk/cost trade-offs, while Obizhaeva–Wang models transient resilience [[1](https://arxiv.org/html/2510.04555v1#bib.bib1), [5](https://arxiv.org/html/2510.04555v1#bib.bib5)]. Open-source agent-based platforms such as ABIDES and ABIDES-Gym bring limit-order books, latencies, and interacting agents to RL research, bridging the gap between stylized price processes and exchange-like environments [[7](https://arxiv.org/html/2510.04555v1#bib.bib7), [8](https://arxiv.org/html/2510.04555v1#bib.bib8), [39](https://arxiv.org/html/2510.04555v1#bib.bib39)]. This stack—SSVI→\!\toDupire→\!\toVIX with LOB execution and impact—has become common in surveys and practice for reproducible stress testing and policy benchmarking [[10](https://arxiv.org/html/2510.04555v1#bib.bib10), [11](https://arxiv.org/html/2510.04555v1#bib.bib11), [12](https://arxiv.org/html/2510.04555v1#bib.bib12)].

##### This paper: Tail-Safe hedging with an explainable safety layer.

We propose Tail-Safe, a hybrid *learn–then–filter* framework for SPX–VIX hedging that combines risk-sensitive learning with white-box safety and robustness. (i) The learning component trains a distributional critic with CVaR objectives, stabilized by a *quantile-coverage controller* that tracks the effective tail mass during training to reduce estimator variance and policy churn. (ii) The execution component enforces *state-wise* constraints via a finance-specific CBF–QP layer that implements NTB shrinkage, box/rate limits, and sign-consistency, while exporting telemetry (active-set identity, tightest constraint, slack/rate utilization) suitable for audit. Policy updates follow KL-regularized PPO with an EMA reference policy to cap per-epoch drift [[16](https://arxiv.org/html/2510.04555v1#bib.bib16)]. Evaluation occurs in an arbitrage-free SSVI→\!\rightarrowDupire→\!\rightarrowVIX pipeline with ABIDES/LOB execution and classical impact models [[3](https://arxiv.org/html/2510.04555v1#bib.bib3), [4](https://arxiv.org/html/2510.04555v1#bib.bib4), [7](https://arxiv.org/html/2510.04555v1#bib.bib7), [1](https://arxiv.org/html/2510.04555v1#bib.bib1), [5](https://arxiv.org/html/2510.04555v1#bib.bib5)].

##### Mathematical guarantees and explainability (paper highlights).

To meet top-tier standards and strengthen interpretability, we develop and prove:

* •

  Discrete-time invariance & minimal-deviation (Theorem 1). For the proposed discrete-time CBF constraints, if the QP is feasible with zero slack, the safe set is forward-invariant. The HH-metric objective selects the uniquely closest feasible action to the nominal proposal, making the safety intervention *predictable* and *stable* [[23](https://arxiv.org/html/2510.04555v1#bib.bib23), [25](https://arxiv.org/html/2510.04555v1#bib.bib25)].
* •

  DRO–KL equivalence (Theorem 2). A per-state KL penalty in PPO corresponds to the Fenchel dual of a KL-ball worst-case objective, quantifying conservatism and providing a tunable *risk budget* that links trust-region size to adversarial uncertainty [[35](https://arxiv.org/html/2510.04555v1#bib.bib35), [36](https://arxiv.org/html/2510.04555v1#bib.bib36), [15](https://arxiv.org/html/2510.04555v1#bib.bib15)].
* •

  Tail-coverage stabilization (Theorem 3). A PID-style quantile-coverage controller stabilizes the Monte Carlo CVaR estimator by regulating effective tail mass around a scheduled α\alpha, yielding finite-sample variance control and bounding the gap between scheduled and realized tail coverage under mild regularity.
* •

  Feasibility under tail guards (Proposition 1). With expiry-aware NTB shrinkage, sign-consistency gates, and realistic microstructure and inventory envelopes (rate/box limits), the safety QP admits a nonempty feasible set and avoids deadlock in stressed conditions.
* •

  Telemetry–KKT correspondence (Lemma 1). Tightness indicators and dual variables map one-to-one to business-rule interventions (leverage/short-sale/rate caps), producing auditable, human-readable explanations of *why* and *by how much* a proposed trade was modified.

##### Contributions.

(1) Tail-risk learning with stability. We integrate distributional RL (IQN) and CVaR objectives with a *quantile-coverage controller* and PPO+KL updates, improving left-tail behavior without large policy drift [[13](https://arxiv.org/html/2510.04555v1#bib.bib13), [14](https://arxiv.org/html/2510.04555v1#bib.bib14), [16](https://arxiv.org/html/2510.04555v1#bib.bib16)].
  
(2) White-box CBF–QP safety. We design a finance-specific CBF–QP that enforces NTB, box/rate, and sign-consistency gates with telemetry, enabling *explainable* state-wise safety consistent with the control literature [[23](https://arxiv.org/html/2510.04555v1#bib.bib23), [25](https://arxiv.org/html/2510.04555v1#bib.bib25), [22](https://arxiv.org/html/2510.04555v1#bib.bib22)].
  
(3) Robustness to shift. We couple KL-regularized updates with DRO-motivated penalties to guard against simulator misspecification and out-of-distribution stress [[35](https://arxiv.org/html/2510.04555v1#bib.bib35), [36](https://arxiv.org/html/2510.04555v1#bib.bib36), [37](https://arxiv.org/html/2510.04555v1#bib.bib37)].
  
(4) Finance-grounded evaluation. We build an arbitrage-free SSVI/Dupire/VIX simulator with ABIDES execution and impact models to enable reproducible, stressable studies aligned with practitioner workflows [[3](https://arxiv.org/html/2510.04555v1#bib.bib3), [4](https://arxiv.org/html/2510.04555v1#bib.bib4), [7](https://arxiv.org/html/2510.04555v1#bib.bib7), [1](https://arxiv.org/html/2510.04555v1#bib.bib1), [5](https://arxiv.org/html/2510.04555v1#bib.bib5)].

##### Positioning and outlook.

Compared with black-box deep hedgers or unconstrained RL, Tail-Safe delivers: (i) *hard safety* by construction with audit-ready telemetry; (ii) *tail shaping* via stabilized CVaR learning; and (iii) *robustness* through DRO/KL regularization—all within markets that respect no-arbitrage and microstructure. This responds to recent surveys calling for safe, trustworthy, and explainable financial RL [[10](https://arxiv.org/html/2510.04555v1#bib.bib10), [11](https://arxiv.org/html/2510.04555v1#bib.bib11), [12](https://arxiv.org/html/2510.04555v1#bib.bib12)]. Beyond SPX–VIX, the framework extends to multi-asset books with cross-gamma and funding constraints, richer impact/latency models, and formal certificates for state-dependent CBF margins and DRMDPs [[25](https://arxiv.org/html/2510.04555v1#bib.bib25), [38](https://arxiv.org/html/2510.04555v1#bib.bib38)]. We view these directions as necessary steps toward deployable, regulator-ready AI agents for real-world hedging.

## 2 Preliminaries & Problem Setting

We consider a synthetic yet finance-grounded evaluation stack for equity–volatility hedging (e.g., SPX–VIX) that is *arbitrage-free*, *microstructure-aware*, and *stressable*.
The market generator follows a calibrated no-arbitrage implied-volatility pipeline SSVI→\!\rightarrowDupire→\!\rightarrowVIX, while order execution is simulated through an agent-based limit-order-book (LOB) environment (ABIDES/MockLOB) with temporary and transient impact.
This section formalizes the environment, the agent interface (states/actions/inventory), loss and tail-risk metrics, and the occupancy and KL notions used later.

### 2.1 Arbitrage-Free Volatility Surfaces via SSVI

For each maturity τ>0\tau>0, denote by w​(k,τ)w(k,\tau) the total implied variance at log-moneyness k=log⁡(K/Fτ)k=\log(K/F\_{\tau}).
We parameterize ww using the *SSVI* family [[3](https://arxiv.org/html/2510.04555v1#bib.bib3)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | w​(k,τ)=θ​(τ)2​(1+ρ​(τ)​φ​(τ)​k+(φ​(τ)​k+ρ​(τ))2+1−ρ​(τ)2),w(k,\tau)\;=\;\frac{\theta(\tau)}{2}\left(1\;+\;\rho(\tau)\,\varphi(\tau)\,k\;+\;\sqrt{\big(\varphi(\tau)\,k+\rho(\tau)\big)^{2}+1-\rho(\tau)^{2}}\right), |  | (1) |

where θ​(τ)>0\theta(\tau)>0 is the ATM total variance term-structure, φ​(τ)>0\varphi(\tau)>0 the shape, and ρ​(τ)∈(−1,1)\rho(\tau)\!\in\!(-1,1) the skew parameter.
SSVI admits tractable *static no-arbitrage* conditions (no butterfly/calendar arbitrage) as simple inequalities on (θ,φ,ρ)(\theta,\varphi,\rho) across maturities, yielding a calibrated surface free of static arbitrage [[3](https://arxiv.org/html/2510.04555v1#bib.bib3)].
We fit (θ,φ,ρ)(\theta,\varphi,\rho) on SPX option data slices or stylized templates and use ([1](https://arxiv.org/html/2510.04555v1#S2.E1 "In 2.1 Arbitrage-Free Volatility Surfaces via SSVI ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) as the *sole* input to downstream local-volatility and variance measures.

### 2.2 Local Volatility via Dupire

Let C​(t,K)C(t,K) be the time-tt undiscounted call price with strike KK implied by the SSVI surface.
Under mild regularity and risk-neutrality, the *Dupire* local variance σloc2​(t,K)\sigma\_{\mathrm{loc}}^{2}(t,K) satisfies [[4](https://arxiv.org/html/2510.04555v1#bib.bib4)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σloc2​(t,K)=∂tC​(t,K)12​K2​∂K​KC​(t,K),∂K​KC​(t,K)>0.\sigma\_{\mathrm{loc}}^{2}(t,K)\;=\;\frac{\partial\_{t}C(t,K)}{\tfrac{1}{2}K^{2}\,\partial\_{KK}C(t,K)}\,,\qquad\partial\_{KK}C(t,K)>0. |  | (2) |

We numerically evaluate the derivatives of CC from the SSVI-implied smiles and generate price paths by simulating the local-volatility diffusion d​St=rt​St​d​t+σloc​(t,St)​St​d​WtdS\_{t}=r\_{t}S\_{t}\,dt+\sigma\_{\mathrm{loc}}(t,S\_{t})S\_{t}\,dW\_{t}, where rtr\_{t} is the (possibly term-structured) risk-free rate.
This produces an arbitrage-consistent equity leg with skews and term-structure inherited from SSVI.

### 2.3 VIX Leg from Surface-Consistent Variance

Consistent with variance-swap replication [[41](https://arxiv.org/html/2510.04555v1#bib.bib41)], the *30-day VIX* at time tt can be computed from out-of-the-money option prices on the surface as (continuous limit, simplified form; see Cboe white paper [[42](https://arxiv.org/html/2510.04555v1#bib.bib42)]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIX2​(t)=2T​er​T​(∫0FP​(K,T)K2​𝑑K+∫F∞C​(K,T)K2​𝑑K),T=30D,\mathrm{VIX}^{2}(t)\;=\;\frac{2}{T}\,e^{rT}\left(\int\_{0}^{F}\frac{P(K,T)}{K^{2}}\,dK\;+\;\int\_{F}^{\infty}\frac{C(K,T)}{K^{2}}\,dK\right),\qquad T=\text{30D}, |  | (3) |

where FF is the forward, and P,CP,C are OTM put/call prices derived from the SSVI surface at horizon TT.
We thus construct a *surface-consistent* VIX leg—either as a tradable future proxy or as options on VIX—ensuring joint equity–volatility dynamics coherent with the SSVI/Dupire world.

### 2.4 Execution, Microstructure, and Impact

We embed the above market into an agent-based discrete-event LOB simulator using ABIDES/ABIDES-Gym [[7](https://arxiv.org/html/2510.04555v1#bib.bib7), [40](https://arxiv.org/html/2510.04555v1#bib.bib40)], which exposes realistic order matching, latency, and interacting background agents.
Our execution price model follows classical impact literature [[1](https://arxiv.org/html/2510.04555v1#bib.bib1), [5](https://arxiv.org/html/2510.04555v1#bib.bib5), [46](https://arxiv.org/html/2510.04555v1#bib.bib46)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ptexec\displaystyle p\_{t}^{\mathrm{exec}} | =mt+st2​sgn​(ut)+η​ut+∑j=0∞G​(j)​ut−j,\displaystyle=m\_{t}\;+\;\frac{s\_{t}}{2}\,\mathrm{sgn}(u\_{t})\;+\;\eta\,u\_{t}\;+\;\sum\_{j=0}^{\infty}G(j)\,u\_{t-j}, |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | qt+1\displaystyle q\_{t+1} | =qt+ut,Πt+1−Πt=qt​(mt+1−mt)−Cost​(ut),\displaystyle=q\_{t}+u\_{t},\qquad\Pi\_{t+1}-\Pi\_{t}\;=\;q\_{t}\,(m\_{t+1}-m\_{t})\;-\;\mathrm{Cost}(u\_{t}), |  | (5) |

where mtm\_{t} is the mid-price, sts\_{t} the spread, utu\_{t} the signed trade size, η\eta the *temporary* (linear) impact coefficient (Almgren–Chriss), and G​(⋅)G(\cdot) a *transient* resilience kernel (Obizhaeva–Wang).
The realized trading cost Cost​(ut)\mathrm{Cost}(u\_{t}) aggregates spread, temporary impact, and transient slippage implied by the ABIDES fill process.
We adopt *no-dynamic-arbitrage* constraints on impact to avoid price manipulation [[46](https://arxiv.org/html/2510.04555v1#bib.bib46)].

##### Stress dimensions.

For systematic OOD testing, we perturb SSVI parameters (θ,φ,ρ)(\theta,\varphi,\rho) (level/slope/curvature), equity–vol correlation, and impact strength/decay, as well as time-to-expiry (near-expiry regimes).
All stress configurations remain free of *static* arbitrage by construction (§[2.1](https://arxiv.org/html/2510.04555v1#S2.SS1 "2.1 Arbitrage-Free Volatility Surfaces via SSVI ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

### 2.5 Task, Agent Interface, and Loss

We consider a finite-horizon, discrete-time hedging task t=0,1,…,T−1t=0,1,\dots,T{-}1.
At time tt, the agent observes a state xt∈ℝdx\_{t}\in\mathbb{R}^{d} (prices/Greeks/surface features/time-to-expiry/inventory/LOB and execution features) and issues an action ut∈ℝmu\_{t}\in\mathbb{R}^{m} (trade vector across SPX/VIX instruments).
Inventory qtq\_{t} evolves per ([4](https://arxiv.org/html/2510.04555v1#S2.E4 "In 2.4 Execution, Microstructure, and Impact ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
Let ΠT​(π;ω)\Pi\_{T}(\pi;\omega) denote terminal P&L under policy π\pi on path ω\omega; we define *loss* as LT​(π;ω)=−ΠT​(π;ω)L\_{T}(\pi;\omega)=-\,\Pi\_{T}(\pi;\omega), including transaction costs and slippage from the execution adapter.

### 2.6 Risk Measures: VaR and ES/CVaR

For a confidence level α∈(0,1)\alpha\in(0,1) and random loss LL, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα(L)=inf{z∈ℝ:ℙ(L≤z)≥α},ESα(L)=𝔼[L|L≥VaRα(L)],\operatorname{VaR}\_{\alpha}(L)\;=\;\inf\{z\in\mathbb{R}:\;\mathbb{P}(L\leq z)\geq\alpha\},\qquad\operatorname{ES}\_{\alpha}(L)\;=\;\mathbb{E}\!\left[L\,\middle|\,L\geq\operatorname{VaR}\_{\alpha}(L)\right], |  | (6) |

i.e., *Expected Shortfall* (a.k.a. CVaR) is the conditional mean of losses beyond VaR.
ES is a coherent risk measure [[44](https://arxiv.org/html/2510.04555v1#bib.bib44)] and admits convex optimization surrogates [[43](https://arxiv.org/html/2510.04555v1#bib.bib43)].
We will evaluate policies using absolute-loss VaRα\operatorname{VaR}\_{\alpha} and ESα\operatorname{ES}\_{\alpha} together with central-performance ratios.

### 2.7 Occupancy Measures and Policy KL

Let π​(u|x)\pi(u|x) denote the stochastic policy, and let dπ​(x)d\_{\pi}(x) be the *state occupancy* over the finite horizon:
dπ​(x)=1T​∑t=0T−1ℙπ​(xt=x)d\_{\pi}(x)=\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{P}\_{\pi}(x\_{t}=x).
We also use the *discounted* occupancy when appropriate.
For conservatism, per-state *Kullback–Leibler* (KL) regularization between the updated policy and a reference πref\pi\_{\mathrm{ref}} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | KL(π(⋅|x)∥πref(⋅|x))=∫π(u|x)logπ​(u|x)πref​(u|x)du,\mathrm{KL}\!\big(\pi(\cdot|x)\,\|\,\pi\_{\mathrm{ref}}(\cdot|x)\big)\;=\;\int\pi(u|x)\,\log\frac{\pi(u|x)}{\pi\_{\mathrm{ref}}(u|x)}\,du, |  | (7) |

and aggregated across x∼dπx\sim d\_{\pi}.
KL plays a dual role: (i) as a *trust-region* step-size proxy in policy optimization and (ii) as a distributionally robust regularizer (Fenchel dual of a KL-ball worst-case objective), thus controlling sensitivity to simulator misspecification [[45](https://arxiv.org/html/2510.04555v1#bib.bib45), [43](https://arxiv.org/html/2510.04555v1#bib.bib43)].

### 2.8 Notation Summary

Table 1: Notation used throughout the paper (symbols refer to their values at time tt unless otherwise noted).

| Symbol | Meaning |
| --- | --- |
| StS\_{t} | Underlying equity mid-price; KK strike; FF forward |
| w​(k,τ)w(k,\tau) | Total implied variance at log-moneyness kk and maturity τ\tau (SSVI; Eq. ([1](https://arxiv.org/html/2510.04555v1#S2.E1 "In 2.1 Arbitrage-Free Volatility Surfaces via SSVI ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))) |
| σloc​(t,S)\sigma\_{\mathrm{loc}}(t,S) | Dupire local volatility (Eq. ([2](https://arxiv.org/html/2510.04555v1#S2.E2 "In 2.2 Local Volatility via Dupire ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))) |
| VIX​(t)\mathrm{VIX}(t) | 30D variance index computed from OTM option integrals (Eq. ([3](https://arxiv.org/html/2510.04555v1#S2.E3 "In 2.3 VIX Leg from Surface-Consistent Variance ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))) |
| mt,stm\_{t},s\_{t} | LOB mid-price and bid–ask spread |
| ut,qtu\_{t},q\_{t} | Trade vector (signed); inventory vector |
| ptexecp\_{t}^{\mathrm{exec}} | Execution price with spread/temporary/transient impact (Eq. ([4](https://arxiv.org/html/2510.04555v1#S2.E4 "In 2.4 Execution, Microstructure, and Impact ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))) |
| ΠT\Pi\_{T} | Terminal P&L; LT=−ΠTL\_{T}=-\Pi\_{T} loss |
| VaRα,ESα\operatorname{VaR}\_{\alpha},\operatorname{ES}\_{\alpha} | Tail risk measures at confidence α\alpha (§[2.6](https://arxiv.org/html/2510.04555v1#S2.SS6 "2.6 Risk Measures: VaR and ES/CVaR ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) |
| π​(u|x)\pi(u|x), πref​(u|x)\pi\_{\mathrm{ref}}(u|x) | Stochastic policy and EMA reference policy |
| dπ​(x)d\_{\pi}(x) | (Discounted) state occupancy under π\pi (§[2.7](https://arxiv.org/html/2510.04555v1#S2.SS7 "2.7 Occupancy Measures and Policy KL ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) |
| KL​(π∥πref)\mathrm{KL}(\pi\|\pi\_{\mathrm{ref}}) | Per-state Kullback–Leibler divergence (Eq. ([7](https://arxiv.org/html/2510.04555v1#S2.E7 "In 2.7 Occupancy Measures and Policy KL ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))) |
| rtr\_{t} | Risk-free rate; TT hedging horizon length (steps); Δ​t\Delta t step size |

##### Remark (calibration and units).

All option prices are undiscounted unless stated otherwise; rtr\_{t} denotes continuously compounded rates.
We report P&L in currency units and normalize risk (e.g., ES) by notional or premium where indicated for comparability across scenarios.

## 3 Method: Tail-Safe Hedging Framework

This section presents Tail-Safe: a hybrid *learn–then–filter* framework that couples risk-sensitive, distributional reinforcement learning with a *white-box* CBF–QP safety layer.
Section [3.1](https://arxiv.org/html/2510.04555v1#S3.SS1 "3.1 Risk-Sensitive RL with IQN–CVaR–PPO ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") details the IQN–CVaR–PPO learner and its KL-/entropy-regularized objective;
Section [3.2](https://arxiv.org/html/2510.04555v1#S3.SS2 "3.2 Tail-Coverage Controller: Temperature Sampling and Tail-Boost ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") introduces a *Tail-Coverage Controller* that stabilizes low-α\alpha CVaR estimation via temperature-based quantile sampling and tail-boosting;
Section [3.3](https://arxiv.org/html/2510.04555v1#S3.SS3 "3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") specifies the discrete-time CBF constraints, the ellipsoidal no-trade band (NTB), box/rate limits, and a sign-consistency gate, together with audit-ready telemetry.
Figure [1](https://arxiv.org/html/2510.04555v1#S3.F1 "Figure 1 ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") summarizes the overall architecture.

![Refer to caption](model.png)


Figure 1: Tail-Safe overview. (a) Market & Execution: SSVI →\rightarrow Dupire →\rightarrow 30D VIX; ABIDES/MockLOB execution with temporary and transient impact.
(b) IQN–CVaR–PPO: distributional critic via quantile regression, PPO with KL and entropy regularization.
(c) White-box CBF–QP safety layer: discrete-time CBF, ellipsoidal NTB, box/rate limits, and a sign-consistency gate solved as a convex QP.
(d) Telemetry & risk metrics: VaR/ES\mathrm{VaR}/\mathrm{ES}, policy KL, tail coverage, active-set, tightest-constraint ID, rate utilization, gate score, and slack.

### 3.1 Risk-Sensitive RL with IQN–CVaR–PPO

##### Quantile networks and the CVaR objective.

Distributional RL models the return distribution Zπ​(x,u)Z\_{\pi}(x,u) instead of its mean [[13](https://arxiv.org/html/2510.04555v1#bib.bib13)].
Implicit Quantile Networks (IQN) learn a differentiable quantile function Qψ​(x,u;τ)≈FZπ(⋅|x,u)−1​(τ)Q\_{\psi}(x,u;\tau)\!\approx\!F^{-1}\_{Z\_{\pi}(\cdot|x,u)}(\tau) [[14](https://arxiv.org/html/2510.04555v1#bib.bib14)].
Let loss be L=−ZL=-Z. For xx fixed, the conditional CVaR admits the quantile integral

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(L|x)=1α​∫0αFL|x−1​(τ)​𝑑τ≈1K​α​∑k=1K𝟏​{τk≤α}​L^​(x,τk),\mathrm{CVaR}\_{\alpha}(L\,|\,x)\;=\;\frac{1}{\alpha}\int\_{0}^{\alpha}F^{-1}\_{L\,|\,x}(\tau)\,d\tau\;\approx\;\frac{1}{K\alpha}\sum\_{k=1}^{K}\mathbf{1}\{\tau\_{k}\leq\alpha\}\,\widehat{L}(x,\tau\_{k}), |  | (8) |

with τk∼𝒰​(0,1)\tau\_{k}\!\sim\!\mathcal{U}(0,1) (or, in our case, a temperature-tilted distribution; cf. §[3.2](https://arxiv.org/html/2510.04555v1#S3.SS2 "3.2 Tail-Coverage Controller: Temperature Sampling and Tail-Boost ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and L^​(x,τ)=−𝔼u∼π(⋅|x)​[Qψ​(x,u;τ)]\widehat{L}(x,\tau)=-\,\mathbb{E}\_{u\sim\pi(\cdot|x)}[Q\_{\psi}(x,u;\tau)].
At the episode level we use the Rockafellar–Uryasev CVaR surrogate [[43](https://arxiv.org/html/2510.04555v1#bib.bib43)] (or its quantile approximation) and train with Monte Carlo estimates.

##### CVaR-weighted advantage and PPO updates.

Let Vαπ​(x)≈CVaRα​(L|x)V\_{\alpha}^{\pi}(x)\!\approx\!\mathrm{CVaR}\_{\alpha}(L\,|\,x) and define a *CVaR-weighted* generalized advantage

|  |  |  |  |
| --- | --- | --- | --- |
|  | At(α)≈∑l=0∞(γ​λ)l​(ℓt+l−V^α​(xt+l)+γ​V^α​(xt+l+1)),A\_{t}^{(\alpha)}\;\approx\;\sum\_{l=0}^{\infty}(\gamma\lambda)^{l}\Big(\ell\_{t+l}-\widehat{V}\_{\alpha}(x\_{t+l})+\gamma\,\widehat{V}\_{\alpha}(x\_{t+l+1})\Big), |  | (9) |

where ℓt\ell\_{t} is a one-step loss (including spread, temporary impact, and transient slippage) and the structure mirrors GAE [[47](https://arxiv.org/html/2510.04555v1#bib.bib47)] with a CVaR baseline.
The actor uses PPO [[16](https://arxiv.org/html/2510.04555v1#bib.bib16)] with KL and entropy regularization:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒactor=𝔼t[min(rt(θ)At(α),clip(rt(θ),1−ϵ,1+ϵ)At(α))]+λKL𝔼x[KL(πθ(⋅|x)∥πref(⋅|x))]+λent𝔼x[ℋ(πθ(⋅|x))],\mathcal{L}\_{\text{actor}}=\mathbb{E}\_{t}\!\left[\min\!\Big(r\_{t}(\theta)\,A\_{t}^{(\alpha)},\;\mathrm{clip}(r\_{t}(\theta),1-\epsilon,1+\epsilon)\,A\_{t}^{(\alpha)}\Big)\right]\;+\;\lambda\_{\mathrm{KL}}\,\mathbb{E}\_{x}\big[\mathrm{KL}(\pi\_{\theta}(\cdot|x)\,\|\,\pi\_{\mathrm{ref}}(\cdot|x))\big]\;+\;\lambda\_{\mathrm{ent}}\,\mathbb{E}\_{x}[\mathcal{H}(\pi\_{\theta}(\cdot|x))], |  | (10) |

with rt​(θ)=πθ​(ut|xt)/πθold​(ut|xt)r\_{t}(\theta)=\pi\_{\theta}(u\_{t}|x\_{t})/\pi\_{\theta\_{\mathrm{old}}}(u\_{t}|x\_{t}) and πref\pi\_{\mathrm{ref}} an EMA reference policy.
The KL term serves as a trust-region proxy [[15](https://arxiv.org/html/2510.04555v1#bib.bib15), [48](https://arxiv.org/html/2510.04555v1#bib.bib48)] and admits a DRO interpretation (see §4).
The critic minimizes the quantile Huber loss for QψQ\_{\psi} [[14](https://arxiv.org/html/2510.04555v1#bib.bib14)].

##### Implementation notes.

Trajectories are collected *through* the safety filter (Sec. [3.3](https://arxiv.org/html/2510.04555v1#S3.SS3 "3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), i.e., the actor proposes utnomu\_{t}^{\mathrm{nom}} which is minimally corrected by the CBF–QP into utu\_{t}.
We log solver telemetry (active constraints, tightness, rate utilization, gate scores, slack, status/time) to support both training diagnostics and audit trails.
KL and entropy coefficients can be scheduled to avoid premature collapse and to match the tightening of α\alpha [[16](https://arxiv.org/html/2510.04555v1#bib.bib16)].

### 3.2 Tail-Coverage Controller: Temperature Sampling and Tail-Boost

##### Motivation.

For small α\alpha (e.g., 1%−5%1\%\!-\!5\%), uniform quantile sampling yields few tail samples and high variance, destabilizing training.
We therefore introduce *temperature-tilted* quantile sampling and an explicit *tail-boost*, combined with a PID controller to track a target *effective tail mass*.

##### Temperature-tilted sampling and importance weights.

Define the sampling density over τ∈[0,1]\tau\in[0,1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pT​(τ)∝e−τ/T,T∈[Tmin,Tmax],p\_{T}(\tau)\;\propto\;e^{-\tau/T},\qquad T\in[T\_{\min},T\_{\max}], |  | (11) |

so that smaller TT emphasizes low quantiles.
With τk∼pT\tau\_{k}\!\sim\!p\_{T}, we use self-normalized importance weights wk∝1/pT​(τk)w\_{k}\propto 1/p\_{T}(\tau\_{k}) to form an unbiased CVaR estimator (concentration bounds in §4; see also standard results on self-normalized importance sampling [[50](https://arxiv.org/html/2510.04555v1#bib.bib50)]).
Additionally, for τ≤α\tau\leq\alpha we assign a *tail-boost* factor γtail≥1\gamma\_{\mathrm{tail}}\!\geq\!1 to increase the effective tail count.

##### Coverage metric and PID tracking.

Let the *effective tail mass* within a minibatch be

|  |  |  |
| --- | --- | --- |
|  | w^=1K​∑k=1K𝟏​{τk≤α}.\widehat{w}\;=\;\frac{1}{K}\sum\_{k=1}^{K}\mathbf{1}\{\tau\_{k}\leq\alpha\}. |  |

Given a target wtargetw\_{\mathrm{target}} (e.g., 1.5​α1.5\alpha), define error e=wtarget−w^e=w\_{\mathrm{target}}-\widehat{w} and update (T,γtail)(T,\gamma\_{\mathrm{tail}}) via discrete PID (clipped to feasible ranges):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Tn+1\displaystyle T\_{n+1} | =clip​(Tn+κP​en+κI​∑j=1nej+κD​(en−en−1),Tmin,Tmax),\displaystyle=\mathrm{clip}\!\left(T\_{n}+\kappa\_{P}e\_{n}+\kappa\_{I}\sum\_{j=1}^{n}e\_{j}+\kappa\_{D}(e\_{n}-e\_{n-1}),\;T\_{\min},T\_{\max}\right), |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γtail,n+1\displaystyle\gamma\_{\mathrm{tail},\,n+1} | =clip​(γtail,n+ηP​en+ηI​∑j=1nej+ηD​(en−en−1),γmin,γmax).\displaystyle=\mathrm{clip}\!\left(\gamma\_{\mathrm{tail},\,n}+\eta\_{P}e\_{n}+\eta\_{I}\sum\_{j=1}^{n}e\_{j}+\eta\_{D}(e\_{n}-e\_{n-1}),\;\gamma\_{\min},\gamma\_{\max}\right). |  | (13) |

PID design and anti-windup follow classical practice [[51](https://arxiv.org/html/2510.04555v1#bib.bib51)].
We employ an α\alpha schedule that tightens from a permissive level (e.g., 0.100.10) toward the target (e.g., 0.0250.025), while the controller stabilizes w^\widehat{w}; the PPO KL penalty can be increased in tandem to limit policy drift [[16](https://arxiv.org/html/2510.04555v1#bib.bib16), [15](https://arxiv.org/html/2510.04555v1#bib.bib15), [48](https://arxiv.org/html/2510.04555v1#bib.bib48)].

### 3.3 White-Box CBF–QP Safety Layer

##### Discrete-time CBF constraints.

Let hi​(x)≥0h\_{i}(x)\!\geq\!0 denote the ii-th safety function and consider a local affine state update xt+1=f​(xt)+g​(xt)​utx\_{t+1}=f(x\_{t})+g(x\_{t})u\_{t}.
We enforce discrete-time CBF conditions [[23](https://arxiv.org/html/2510.04555v1#bib.bib23), [24](https://arxiv.org/html/2510.04555v1#bib.bib24)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(f​(xt)+g​(xt)​ut)−(1−κi​Δ​t)​hi​(xt)≥−ζi,ζi≥0,κi>0,h\_{i}\!\big(f(x\_{t})+g(x\_{t})u\_{t}\big)\;-\;(1-\kappa\_{i}\Delta t)\,h\_{i}(x\_{t})\;\geq\;-\,\zeta\_{i},\qquad\zeta\_{i}\geq 0,\;\kappa\_{i}>0, |  | (14) |

where slack variables are heavily penalized and only activated when unavoidable (robust margins are analyzed in §4).

##### Ellipsoidal NTB, box/rate limits, and a sign-consistency gate.

Let b⋆​(x)b^{\star}(x) be a target exposure vector (e.g., delta/vega) and b​(x,u)b(x,u) the exposure after action uu.
Define the *ellipsoidal no-trade band* (NTB)

|  |  |  |  |
| --- | --- | --- | --- |
|  | e​(x,u)=b​(x,u)−b⋆​(x),e⊤​M​e≤bmax,M≻0,e(x,u)\;=\;b(x,u)-b^{\star}(x),\qquad e^{\top}Me\;\leq\;b\_{\max},\quad M\succ 0, |  | (15) |

and *box/rate* limits umin≤ut≤umaxu\_{\min}\!\leq\!u\_{t}\!\leq\!u\_{\max}, ‖ut−ut−1‖2≤rmax\|u\_{t}-u\_{t-1}\|\_{2}\!\leq\!r\_{\max}.
We further require a *sign-consistency gate*

|  |  |  |  |
| --- | --- | --- | --- |
|  | gcons​(x,u)=minj=1,…,J⁡⟨u,∇^​Π(j)​(x)⟩−δadv≥ 0,g\_{\mathrm{cons}}(x,u)\;=\;\min\_{j=1,\dots,J}\,\langle u,\widehat{\nabla}\Pi^{(j)}(x)\rangle\;-\;\delta\_{\mathrm{adv}}\;\geq\;0, |  | (16) |

so that trades align with an ensemble of interpretable signals (e.g., advantage-proxy gradients from the distributional critic or pricing/hedging sensitivities) [[53](https://arxiv.org/html/2510.04555v1#bib.bib53)].
Near expiry or under extreme volatility, we shrink bmax←ηb​bmaxb\_{\max}\!\leftarrow\!\eta\_{b}b\_{\max} and tighten rmax←ηr​rmaxr\_{\max}\!\leftarrow\!\eta\_{r}r\_{\max} with ηb,ηr∈(0,1)\eta\_{b},\eta\_{r}\in(0,1) to improve feasibility and stability.

##### QP formulation and minimal-deviation projection.

Given the actor’s proposal utnomu\_{t}^{\mathrm{nom}}, we compute the closest safe action utu\_{t} by solving the convex QP

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minut,ζ≥0\displaystyle\min\_{u\_{t},\;\zeta\geq 0}\quad | 12​(ut−utnom)⊤​H​(ut−utnom)+c⊤​ut+ρ​‖ζ‖1\displaystyle\frac{1}{2}\,(u\_{t}-u\_{t}^{\mathrm{nom}})^{\top}H\,(u\_{t}-u\_{t}^{\mathrm{nom}})\;+\;c^{\top}u\_{t}\;+\;\rho\,\|\zeta\|\_{1} |  | (17) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | CBF: ​hi​(f​(xt)+g​(xt)​ut)−(1−κi​Δ​t)​hi​(xt)≥−ζi,∀i,\displaystyle\text{CBF: }h\_{i}(f(x\_{t})+g(x\_{t})u\_{t})-(1-\kappa\_{i}\Delta t)\,h\_{i}(x\_{t})\geq-\zeta\_{i},\;\forall i, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | NTB: ​e​(xt,ut)⊤​M​e​(xt,ut)≤bmax,Box/Rate: ​umin≤ut≤umax,‖ut−ut−1‖2≤rmax,\displaystyle\text{NTB: }e(x\_{t},u\_{t})^{\top}Me(x\_{t},u\_{t})\leq b\_{\max},\qquad\text{Box/Rate: }u\_{\min}\!\leq\!u\_{t}\!\leq\!u\_{\max},\;\|u\_{t}-u\_{t-1}\|\_{2}\leq r\_{\max}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Gate: ​gcons​(xt,ut)≥0.\displaystyle\text{Gate: }g\_{\mathrm{cons}}(x\_{t},u\_{t})\geq 0. |  |

Here H≻0H\!\succ\!0 defines the deviation metric, cc encodes linear trading frictions, and ρ≫0\rho\!\gg\!0 penalizes any slack.
We use OSQP [[52](https://arxiv.org/html/2510.04555v1#bib.bib52)] with warm starts for efficiency and robustness; see [[49](https://arxiv.org/html/2510.04555v1#bib.bib49)] for background on convex QPs.
When ζ=0\zeta=0, ([14](https://arxiv.org/html/2510.04555v1#S3.E14 "In Discrete-time CBF constraints. ‣ 3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) implies forward invariance of the safe set; the quadratic objective makes utu\_{t} the HH-metric projection of utnomu\_{t}^{\mathrm{nom}} onto the feasible set (formalized in §4).

##### Telemetry for auditability and operations.

For each step, the solver returns: active\_set (indices of active constraints), tightest\_id, rate\_util =‖ut−ut−1‖2/rmax=\|u\_{t}{-}u\_{t-1}\|\_{2}/r\_{\max}, gate\_score =gcons​(xt,ut)=g\_{\mathrm{cons}}(x\_{t},u\_{t}), slack\_sum =‖ζ‖1=\|\zeta\|\_{1}, and solver\_status/time.
We penalize nonzero slack or non-optimal statuses in the RL reward and log incidents for post-hoc audit, closing the loop between *explainable interception* and *governance*.

##### Pseudocode: training loop and safety filter.

Algorithm 1  Tail-Safe IQN–CVaR–PPO (on-policy training)

1: Initialize actor θ\theta, critic ψ\psi, reference policy πref←πθ\pi\_{\mathrm{ref}}\!\leftarrow\!\pi\_{\theta}, temperature TT, tail-boost γtail\gamma\_{\mathrm{tail}}, and target coverage wtargetw\_{\mathrm{target}}.

2: for iterations k=1,2,…k=1,2,\dots do

3:  Collect trajectories using the safety filter (Alg. [2](https://arxiv.org/html/2510.04555v1#alg2 "Algorithm 2 ‣ Pseudocode: training loop and safety filter. ‣ 3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) to obtain {(xt,ut,rt,telemetryt)}\{(x\_{t},u\_{t},r\_{t},\text{telemetry}\_{t})\}.

4:  Sample quantiles τk∼pT\tau\_{k}\!\sim\!p\_{T} (Eq. ([11](https://arxiv.org/html/2510.04555v1#S3.E11 "In Temperature-tilted sampling and importance weights. ‣ 3.2 Tail-Coverage Controller: Temperature Sampling and Tail-Boost ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))) and apply tail-boost to τ≤α\tau\!\leq\!\alpha.

5:  Update critic QψQ\_{\psi} by minimizing the quantile Huber loss (IQN).

6:  Estimate VαV\_{\alpha} and A(α)A^{(\alpha)} via Eqs. ([8](https://arxiv.org/html/2510.04555v1#S3.E8 "In Quantile networks and the CVaR objective. ‣ 3.1 Risk-Sensitive RL with IQN–CVaR–PPO ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))–([9](https://arxiv.org/html/2510.04555v1#S3.E9 "In CVaR-weighted advantage and PPO updates. ‣ 3.1 Risk-Sensitive RL with IQN–CVaR–PPO ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")); update actor by minimizing Eq. ([10](https://arxiv.org/html/2510.04555v1#S3.E10 "In CVaR-weighted advantage and PPO updates. ‣ 3.1 Risk-Sensitive RL with IQN–CVaR–PPO ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

7:  Compute w^=1K​∑𝟏​{τ≤α}\widehat{w}=\frac{1}{K}\sum\mathbf{1}\{\tau\leq\alpha\} and update (T,γtail)(T,\gamma\_{\mathrm{tail}}) using the PID rules ([12](https://arxiv.org/html/2510.04555v1#S3.E12 "In Coverage metric and PID tracking. ‣ 3.2 Tail-Coverage Controller: Temperature Sampling and Tail-Boost ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) (with clipping).

8:  Tighten α\alpha according to a schedule; update πref\pi\_{\mathrm{ref}} via EMA; log policy KL and telemetry summaries.

9: end for




Algorithm 2  CBF–QP safety filter (per step)

1: Inputs: xtx\_{t}, proposed action utnomu\_{t}^{\mathrm{nom}}, previous action ut−1u\_{t-1}, params (H,M,bmax,rmax,umin,umax,κ,Δ​t)(H,M,b\_{\max},r\_{\max},u\_{\min},u\_{\max},\kappa,\Delta t).

2: Formulate QP ([17](https://arxiv.org/html/2510.04555v1#S3.E17 "In QP formulation and minimal-deviation projection. ‣ 3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) with discrete CBF, NTB, box/rate limits, and sign-consistency gate; near expiry, shrink bmax←ηb​bmaxb\_{\max}\!\leftarrow\!\eta\_{b}b\_{\max} and rmax←ηr​rmaxr\_{\max}\!\leftarrow\!\eta\_{r}r\_{\max}.

3: Solve the QP (warm-start) to obtain utu\_{t}, active set, tightest constraint, slack ζ\zeta, and solver status/time.

4: Emit telemetry: active\_set, tightest\_id, rate\_util, gate\_score, slack\_sum, solver\_status/time.

5: If ζ>0\zeta>0 or status ≠\neq optimal, add a penalty to the RL reward and log the event; otherwise execute utu\_{t} and advance the environment to xt+1x\_{t+1}.

6: Return utu\_{t} and telemetry.

## 4 Theoretical Results

We formalize guarantees for the proposed Tail-Safe framework.
Our results cover (i) *robust forward invariance* of the discrete-time CBF constraints under bounded model mismatch,
(ii) the *minimal-deviation* nature of the QP safety layer,
(iii) a *KL–DRO* upper bound linking per-state KL regularization to distributional robustness,
(iv) *concentration* and sample-complexity of the temperature-tilted CVaR estimator with a coverage controller,
(v) a *trust-region improvement* inequality for CVaR with KL-limited policy updates,
(vi) *feasibility persistence* under tail guards, and
(vii) *negative-advantage suppression* induced by the sign-consistency gate.
Complete proofs are deferred to Appendix A (with subsections indicated after each result).

Throughout, let ∥⋅∥\|\cdot\| denote the Euclidean norm, ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle the Euclidean inner product, and 𝔹r​(x)\mathbb{B}\_{r}(x) the closed ball of radius rr.
We reuse notation from Sections [2](https://arxiv.org/html/2510.04555v1#S2 "2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")–[3](https://arxiv.org/html/2510.04555v1#S3 "3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

### Theorem 1 (robust forward invariance of the safety set)

###### Assumption 1 (Local dynamics and mismatch).

There exist locally Lipschitz functions f,gf,g and an additive disturbance wtw\_{t} such that the state update obeys
xt+1=f​(xt)+g​(xt)​ut+wtx\_{t+1}=f(x\_{t})+g(x\_{t})u\_{t}+w\_{t} with ‖wt‖≤w¯\|w\_{t}\|\leq\bar{w} almost surely.
For each barrier hi:ℝd→ℝh\_{i}:\mathbb{R}^{d}\to\mathbb{R} there is an Li>0L\_{i}>0 with |hi​(x)−hi​(y)|≤Li​‖x−y‖|h\_{i}(x)-h\_{i}(y)|\leq L\_{i}\|x-y\|.

###### Assumption 2 (Discrete-time CBF constraint with margin).

At time tt, the QP safety layer enforces for each ii:

|  |  |  |
| --- | --- | --- |
|  | hi​(f​(xt)+g​(xt)​ut)−(1−κi​Δ​t)​hi​(xt)≥εi,κi>0,h\_{i}\!\big(f(x\_{t})+g(x\_{t})u\_{t}\big)-(1-\kappa\_{i}\Delta t)\,h\_{i}(x\_{t})\;\geq\;\varepsilon\_{i},\qquad\kappa\_{i}>0, |  |

with margin εi≥Li​w¯\varepsilon\_{i}\geq L\_{i}\bar{w}.

###### Theorem 1 (Robust forward invariance).

Under Assumptions [1](https://arxiv.org/html/2510.04555v1#Thmassumption1 "Assumption 1 (Local dynamics and mismatch). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")–[2](https://arxiv.org/html/2510.04555v1#Thmassumption2 "Assumption 2 (Discrete-time CBF constraint with margin). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), if hi​(xt)≥0h\_{i}(x\_{t})\geq 0 for all ii, then hi​(xt+1)≥0h\_{i}(x\_{t+1})\geq 0 for all ii.
Hence the safe set 𝒞:={x:hi​(x)≥0,∀i}\mathcal{C}:=\{x:\,h\_{i}(x)\geq 0,\,\forall i\} is forward invariant.

##### Proof sketch.

Using Lipschitzness,
hi​(xt+1)≥hi​(f+g​ut)−Li​‖wt‖≥(1−κi​Δ​t)​hi​(xt)+εi−Li​w¯≥0h\_{i}(x\_{t+1})\geq h\_{i}(f+gu\_{t})-L\_{i}\|w\_{t}\|\geq(1-\kappa\_{i}\Delta t)h\_{i}(x\_{t})+\varepsilon\_{i}-L\_{i}\bar{w}\geq 0.
A full inductive argument is given in Appendix A.1.
(See also robust CBF analyses such as [[30](https://arxiv.org/html/2510.04555v1#bib.bib30), [31](https://arxiv.org/html/2510.04555v1#bib.bib31)].)

### Proposition 1 (minimal-deviation HH-metric projection)

###### Assumption 3 (Convex feasibility).

For fixed xtx\_{t}, the feasible action set 𝒮​(xt)\mathcal{S}(x\_{t}) induced by the constraints in ([14](https://arxiv.org/html/2510.04555v1#S3.E14 "In Discrete-time CBF constraints. ‣ 3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), ([15](https://arxiv.org/html/2510.04555v1#S3.E15 "In Ellipsoidal NTB, box/rate limits, and a sign-consistency gate. ‣ 3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), and the box/rate and gate constraints is nonempty, closed, and convex in uu (this holds under affine-in-uu CBF surrogates/linearizations and convex NTB/box/rate/gate specifications).

###### Proposition 1 (Shifted projection).

Let H≻0H\!\succ\!0, c∈ℝmc\in\mathbb{R}^{m}, and ρ\rho be sufficiently large so that the QP ([17](https://arxiv.org/html/2510.04555v1#S3.E17 "In QP formulation and minimal-deviation projection. ‣ 3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) is solved with ζ=0\zeta=0.
Then its unique optimizer ut⋆u\_{t}^{\star} satisfies

|  |  |  |
| --- | --- | --- |
|  | ut⋆=arg⁡minu∈𝒮​(xt)⁡12​‖u−(utnom−H−1​c)‖H2,u\_{t}^{\star}\;=\;\arg\min\_{u\in\mathcal{S}(x\_{t})}\frac{1}{2}\,\|u-(u\_{t}^{\mathrm{nom}}-H^{-1}c)\|\_{H}^{2}, |  |

i.e., ut⋆u\_{t}^{\star} is the HH-metric projection of the *shifted anchor* utnom−H−1​cu\_{t}^{\mathrm{nom}}-H^{-1}c onto 𝒮​(xt)\mathcal{S}(x\_{t}).

##### Proof sketch.

Completing the square yields
12​(u−unom)⊤​H​(u−unom)+c⊤​u=12​‖u−(unom−H−1​c)‖H2+const\tfrac{1}{2}(u-u^{\mathrm{nom}})^{\top}H(u-u^{\mathrm{nom}})+c^{\top}u=\tfrac{1}{2}\|u-(u^{\mathrm{nom}}-H^{-1}c)\|\_{H}^{2}+\mathrm{const}.
Strict convexity plus convex feasibility implies uniqueness; KKT conditions characterize the projection.
Details are in Appendix A.2 (cf. [[49](https://arxiv.org/html/2510.04555v1#bib.bib49)]).

### Theorem 2 (KL–DRO upper bound and conservatism of per-state KL)

###### Assumption 4 (CVaR surrogate).

For α∈(0,1)\alpha\in(0,1) and any threshold t∈ℝt\in\mathbb{R}, define ϕt​(z)=(z−t)+\phi\_{t}(z)=(z-t)\_{+} and
CVaRα​(L)=mint⁡t+1α​𝔼​[ϕt​(L)]\mathrm{CVaR}\_{\alpha}(L)=\min\_{t}\,t+\tfrac{1}{\alpha}\,\mathbb{E}[\phi\_{t}(L)] [[43](https://arxiv.org/html/2510.04555v1#bib.bib43)].

###### Assumption 5 (Path-wise KL radius and occupancy control).

Let 𝒬ρ={Q:KL​(Q∥P)≤ρ}\mathcal{Q}\_{\rho}=\{Q:\mathrm{KL}(Q\|P)\leq\rho\} be a KL ball around a reference path distribution PP (the simulator/behavior distribution).
Assume per-state policy KL is bounded: KL(π′(⋅|x)∥πref(⋅|x))≤β\mathrm{KL}(\pi^{\prime}(\cdot|x)\|\pi\_{\mathrm{ref}}(\cdot|x))\leq\beta for all xx in the support,
and the induced pathwise KL satisfies ρ≤Cocc​β\rho\leq C\_{\mathrm{occ}}\,\beta for some constant CoccC\_{\mathrm{occ}} depending on the horizon and mixing/occupancy properties (cf. Pinsker-type arguments and standard occupancy coupling).

###### Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism).

For any η>0\eta>0,

|  |  |  |
| --- | --- | --- |
|  | supQ∈𝒬ρCVaRα​(L)≤mint∈ℝ⁡{t+1α​η​(ρ+log⁡𝔼P​[eη​ϕt​(L)])}.\sup\_{Q\in\mathcal{Q}\_{\rho}}\mathrm{CVaR}\_{\alpha}(L)\;\leq\;\min\_{t\in\mathbb{R}}\left\{\,t+\frac{1}{\alpha\eta}\Big(\rho+\log\mathbb{E}\_{P}\!\big[e^{\eta\,\phi\_{t}(L)}\big]\Big)\right\}. |  |

Moreover, under Assumption [5](https://arxiv.org/html/2510.04555v1#Thmassumption5 "Assumption 5 (Path-wise KL radius and occupancy control). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") the RHS is upper-bounded by the same expression with ρ\rho replaced by Cocc​βC\_{\mathrm{occ}}\beta.
Hence, penalizing per-state KL by λKL⋅𝔼x[KL(π(⋅|x)∥πref(⋅|x))]\lambda\_{\mathrm{KL}}\!\cdot\!\mathbb{E}\_{x}[\mathrm{KL}(\pi(\cdot|x)\|\pi\_{\mathrm{ref}}(\cdot|x))] controls a KL–DRO upper bound on the CVaR surrogate and thus quantifies conservatism.

##### Proof sketch.

Apply the Donsker–Varadhan variational inequality to 𝔼Q​[ϕt​(L)]\mathbb{E}\_{Q}[\phi\_{t}(L)] [[54](https://arxiv.org/html/2510.04555v1#bib.bib54)], then minimize over tt.
Relate pathwise KL to the expected per-state KL via occupancy coupling and Pinsker’s inequality (see, e.g., [[15](https://arxiv.org/html/2510.04555v1#bib.bib15), [48](https://arxiv.org/html/2510.04555v1#bib.bib48), [55](https://arxiv.org/html/2510.04555v1#bib.bib55), [56](https://arxiv.org/html/2510.04555v1#bib.bib56)]).
Appendix A.3 provides details.

### Theorem 3 (bias/variance and sample complexity of the CVaR estimator)

###### Assumption 6 (Temperature sampling, bounded importance weights, bounded loss).

Quantiles are sampled from pT​(τ)∝e−τ/Tp\_{T}(\tau)\propto e^{-\tau/T} on [0,1][0,1] with T∈[Tmin,Tmax]T\in[T\_{\min},T\_{\max}] and pT​(τ)≥pmin>0p\_{T}(\tau)\geq p\_{\min}>0.
Self-normalized importance weights are wk∝1/pT​(τk)w\_{k}\propto 1/p\_{T}(\tau\_{k}) (normalized within the batch).
Losses are almost surely bounded: |L|≤B|L|\leq B.

Define the self-normalized estimator (with tail-boost implemented by oversampling, absorbed into pTp\_{T}):

|  |  |  |
| --- | --- | --- |
|  | CVaR^α=∑k=1Kwk​ 1​{τk≤α}​L(τk)∑k=1Kwk​ 1​{τk≤α},αeff:=𝔼​[𝟏​{τ≤α}].\widehat{\mathrm{CVaR}}\_{\alpha}=\frac{\sum\_{k=1}^{K}w\_{k}\,\mathbf{1}\{\tau\_{k}\leq\alpha\}\,L^{(\tau\_{k})}}{\sum\_{k=1}^{K}w\_{k}\,\mathbf{1}\{\tau\_{k}\leq\alpha\}},\quad\alpha\_{\mathrm{eff}}:=\mathbb{E}[\mathbf{1}\{\tau\leq\alpha\}]\,. |  |

###### Theorem 3 (Concentration of the temperature-tilted CVaR estimator).

Under Assumption [6](https://arxiv.org/html/2510.04555v1#Thmassumption6 "Assumption 6 (Temperature sampling, bounded importance weights, bounded loss). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), for any δ∈(0,1)\delta\in(0,1), with probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | |CVaR^α−CVaRα|≤C1​B​log⁡(2/δ)K​αeff⏟variance term+C2​B​|αeff−α|⏟coverage mismatch,\big|\widehat{\mathrm{CVaR}}\_{\alpha}-\mathrm{CVaR}\_{\alpha}\big|\;\leq\;\underbrace{C\_{1}\,B\,\sqrt{\frac{\log(2/\delta)}{K\,\alpha\_{\mathrm{eff}}}}}\_{\text{variance term}}\;+\;\underbrace{C\_{2}\,B\,\big|\alpha\_{\mathrm{eff}}-\alpha\big|}\_{\text{coverage mismatch}}, |  |

for absolute constants C1,C2C\_{1},C\_{2} depending on pminp\_{\min} and the self-normalization scheme.
In particular, the PID controller that tracks αeff≈wtarget\alpha\_{\mathrm{eff}}\!\approx\!w\_{\mathrm{target}} (with wtargetw\_{\mathrm{target}} close to α\alpha) reduces the coverage-mismatch bias and improves the rate constant in the variance term.

##### Proof sketch.

Combine self-normalized importance sampling concentration (e.g., empirical Bernstein/Hoeffding-style bounds for ratio estimators) with bounded weights and losses [[50](https://arxiv.org/html/2510.04555v1#bib.bib50)].
A first-order expansion quantifies the effect of replacing α\alpha by αeff\alpha\_{\mathrm{eff}}; the controller reduces this mismatch.
See Appendix A.4 for a full derivation.

### Theorem 4 (trust-region improvement inequality for CVaR with KL limits)

###### Assumption 7 (Per-state KL constraint and smoothness).

For a policy update π′=π+Δ\pi^{\prime}\!=\!\pi+\Delta, assume KL(π′(⋅|x)∥π(⋅|x))≤β\mathrm{KL}(\pi^{\prime}(\cdot|x)\|\pi(\cdot|x))\leq\beta for all xx and that the one-step loss ℓ\ell is LL-Lipschitz in actions and states under the dynamics in Assumption [1](https://arxiv.org/html/2510.04555v1#Thmassumption1 "Assumption 1 (Local dynamics and mismatch). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").
Let Jα​(π)=CVaRα​(LT​(π))J\_{\alpha}(\pi)=\mathrm{CVaR}\_{\alpha}(L\_{T}(\pi)) for horizon TT.

###### Theorem 4 (CVaR trust-region improvement).

There exists a constant Cα>0C\_{\alpha}>0 (depending on LL, TT, and loss bounds) such that

|  |  |  |
| --- | --- | --- |
|  | Jα​(π′)≤Jα​(π)+𝔼x∼dπ,u∼π​[ω​(x,u)​A~π(α)​(x,u)]+Cα​β+o​(‖Δ‖),J\_{\alpha}(\pi^{\prime})\;\leq\;J\_{\alpha}(\pi)\;+\;\mathbb{E}\_{x\sim d\_{\pi},\,u\sim\pi}\!\big[\omega(x,u)\,\tilde{A}\_{\pi}^{(\alpha)}(x,u)\big]\;+\;C\_{\alpha}\,\sqrt{\beta}\;+\;o(\|\Delta\|), |  |

where ω=π′(⋅|x)/π(⋅|x)\omega=\pi^{\prime}(\cdot|x)/\pi(\cdot|x) and A~π(α)\tilde{A}\_{\pi}^{(\alpha)} is the CVaR-weighted advantage (cf. ([9](https://arxiv.org/html/2510.04555v1#S3.E9 "In CVaR-weighted advantage and PPO updates. ‣ 3.1 Risk-Sensitive RL with IQN–CVaR–PPO ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))).
Thus, a small KL radius β\beta controls the degradation term, yielding a trust-region style guarantee for the CVaR objective.

##### Proof sketch.

Adapt the performance-difference lemma to the CVaR surrogate (replace value with CVaR baseline), then bound the state-distribution shift by total variation and Pinsker’s inequality TV≤12​KL\mathrm{TV}\leq\sqrt{\tfrac{1}{2}\mathrm{KL}} [[15](https://arxiv.org/html/2510.04555v1#bib.bib15), [48](https://arxiv.org/html/2510.04555v1#bib.bib48), [55](https://arxiv.org/html/2510.04555v1#bib.bib55)].
Smoothness of ℓ\ell and the horizon accumulation yield Cα​βC\_{\alpha}\sqrt{\beta}.
A detailed derivation is given in Appendix A.5.

### Theorem 5 (feasibility persistence under tail guards)

###### Assumption 8 (Lipschitz constraints and affine exposure map).

Assume e​(x,u)=A​(x)​u−d​(x)e(x,u)=A(x)u-d(x) with AA, dd locally Lipschitz, M≻0M\succ 0, and that box/rate sets are convex.
Let the CBF surrogates used in the QP be affine in uu for fixed xx.

###### Assumption 9 (Margins at time tt).

Suppose at time tt the NTB and rate constraints hold with margins
e​(xt,ut)⊤​M​e​(xt,ut)≤bmax−δbe(x\_{t},u\_{t})^{\top}Me(x\_{t},u\_{t})\leq b\_{\max}-\delta\_{b} and ‖ut−ut−1‖2≤rmax−δr\|u\_{t}-u\_{t-1}\|\_{2}\leq r\_{\max}-\delta\_{r} for some δb,δr>0\delta\_{b},\delta\_{r}>0.

###### Theorem 5 (Persistence via NTB shrinkage and rate tightening).

Under Assumptions [1](https://arxiv.org/html/2510.04555v1#Thmassumption1 "Assumption 1 (Local dynamics and mismatch). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [8](https://arxiv.org/html/2510.04555v1#Thmassumption8 "Assumption 8 (Lipschitz constraints and affine exposure map). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), and [9](https://arxiv.org/html/2510.04555v1#Thmassumption9 "Assumption 9 (Margins at time 𝑡). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"),
there exist shrinkage factors ηb,ηr∈(0,1)\eta\_{b},\eta\_{r}\in(0,1), computable from local Lipschitz constants of (A,d,f,g)(A,d,f,g) and (κi)(\kappa\_{i}) and the disturbance bound w¯\bar{w}, such that replacing bmax←ηb​bmaxb\_{\max}\!\leftarrow\!\eta\_{b}b\_{\max} and rmax←ηr​rmaxr\_{\max}\!\leftarrow\!\eta\_{r}r\_{\max} guarantees that the QP at time t+1t{+}1 remains feasible with ζ=0\zeta=0.
Equivalently, the feasible set intersection (CBF, NTB, box, rate, gate) remains nonempty at t+1t{+}1.

##### Proof sketch.

Use tube arguments: with Lipschitz dynamics and constraints, the next-state feasible set contains a ball around the previous safe action projected by the rate set.
Choosing (ηb,ηr)(\eta\_{b},\eta\_{r}) to upper bound drift induced by (xt→xt+1)(x\_{t}\!\to\!x\_{t+1}) and disturbance keeps the intersection nonempty.
Full details appear in Appendix A.6 (see also viability arguments in robust CBF literature [[30](https://arxiv.org/html/2510.04555v1#bib.bib30)]).

### Proposition 2 (negative-advantage suppression by sign-consistency)

###### Assumption 10 (Gate alignment and mismatch).

For each xx, let gcons​(x,u)=minj≤J⁡⟨u,∇^​Π(j)​(x)⟩−δadvg\_{\mathrm{cons}}(x,u)=\min\_{j\leq J}\langle u,\widehat{\nabla}\Pi^{(j)}(x)\rangle-\delta\_{\mathrm{adv}} with δadv≥0\delta\_{\mathrm{adv}}\geq 0.
Assume there exists a unit vector v​(x)v(x) such that
‖∇^​Π(j)​(x)−v​(x)‖≤ϵg\|\widehat{\nabla}\Pi^{(j)}(x)-v(x)\|\leq\epsilon\_{g} for all jj, and that the CVaR-weighted advantage satisfies a local linearization
A~π(α)​(x,u)≈⟨u,∇A~π(α)​(x)⟩\tilde{A}\_{\pi}^{(\alpha)}(x,u)\approx\langle u,\nabla\tilde{A}\_{\pi}^{(\alpha)}(x)\rangle with ∠​(∇A~π(α)​(x),v​(x))≤ϵθ\angle(\nabla\tilde{A}\_{\pi}^{(\alpha)}(x),v(x))\leq\epsilon\_{\theta}.

###### Proposition 2 (Gate-induced lower bound).

Under Assumption [10](https://arxiv.org/html/2510.04555v1#Thmassumption10 "Assumption 10 (Gate alignment and mismatch). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), any action uu passing the gate (gcons​(x,u)≥0g\_{\mathrm{cons}}(x,u)\geq 0) obeys

|  |  |  |
| --- | --- | --- |
|  | 𝔼[A~π(α)(x,u)|x]≥−ξ(ϵg,ϵθ,δadv,∥u∥),\mathbb{E}\!\left[\tilde{A}\_{\pi}^{(\alpha)}(x,u)\,\middle|\,x\right]\;\geq\;-\,\xi(\epsilon\_{g},\epsilon\_{\theta},\delta\_{\mathrm{adv}},\|u\|), |  |

for an explicit function ξ\xi that vanishes as (ϵg,ϵθ)→0(\epsilon\_{g},\epsilon\_{\theta})\!\to\!0 and increases with δadv\delta\_{\mathrm{adv}} and ‖u‖\|u\|.
In particular, for sufficiently small alignment errors the gate suppresses negative CVaR-advantage trades up to a controlled tolerance.

##### Proof sketch.

Gate feasibility implies ⟨u,v​(x)⟩≥δadv−‖u‖​ϵg\langle u,v(x)\rangle\geq\delta\_{\mathrm{adv}}-\|u\|\epsilon\_{g}.
Using the angle bound between v​(x)v(x) and ∇A~π(α)​(x)\nabla\tilde{A}\_{\pi}^{(\alpha)}(x) and Cauchy–Schwarz yields
⟨u,∇A~π(α)​(x)⟩≥‖u‖​(δadv/‖u‖−ϵg)​cos⁡ϵθ−‖u‖​𝒪​(ϵg)\langle u,\nabla\tilde{A}\_{\pi}^{(\alpha)}(x)\rangle\geq\|u\|(\delta\_{\mathrm{adv}}/\|u\|-\epsilon\_{g})\cos\epsilon\_{\theta}-\|u\|\,\mathcal{O}(\epsilon\_{g}),
which provides the claimed lower bound.
Formal constants are derived in Appendix A.7.

Remarks.
(i) Theorems [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and [5](https://arxiv.org/html/2510.04555v1#Thmtheorem5 "Theorem 5 (Persistence via NTB shrinkage and rate tightening). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") formalize *hard safety* by construction plus feasibility resilience under tail guards, connecting solver telemetry to auditable interventions.
(ii) Theorems [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") justify the PPO+KL design for tail-risk optimization: per-state KL acts as a DRO-style conservatism control while ensuring trust-region stability.
(iii) Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") shows why the coverage controller reduces variance and bias in CVaR estimation as α\alpha tightens.

## 5 Experiments in Arbitrage-Free Synthetic Markets

We evaluate Tail-Safe in a synthetic yet finance-grounded environment that is (i) *arbitrage-free* by construction (SSVI→\!\rightarrowDupire→\!\rightarrowVIX), (ii) *microstructure-aware* through ABIDES/MockLOB execution with spread, temporary, and transient impact, and (iii) *stressable* along interpretable dimensions (level/slope/curvature of the volatility surface, equity–volatility correlation, impact strength/decay, and time-to-expiry).
All results are reported with *unified sample sizes* and *multiple random seeds*, with uncertainty quantified by paired bootstrap confidence intervals [[58](https://arxiv.org/html/2510.04555v1#bib.bib58), [59](https://arxiv.org/html/2510.04555v1#bib.bib59)].
This section details the protocol, metrics, results, ablations, and safety telemetry.

### 5.1 Protocol

##### ID/OOD split and stress dimensions.

We generate a calibrated SSVI surface family w​(k,τ)w(k,\tau) satisfying static no-arbitrage (Sec. [2.1](https://arxiv.org/html/2510.04555v1#S2.SS1 "2.1 Arbitrage-Free Volatility Surfaces via SSVI ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), transform it to Dupire local volatility (Sec. [2.2](https://arxiv.org/html/2510.04555v1#S2.SS2 "2.2 Local Volatility via Dupire ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), and construct a surface-consistent 30D VIX leg (Sec. [2.3](https://arxiv.org/html/2510.04555v1#S2.SS3 "2.3 VIX Leg from Surface-Consistent Variance ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
We define *in-distribution* (ID) scenarios by sampling around the baseline calibration and *out-of-distribution* (OOD) scenarios by perturbing:

1. 1.

   Level/slope/curvature of the SSVI parameters (θ,φ,ρ)(\theta,\varphi,\rho) across maturities;
2. 2.

   Equity–volatility correlation regimes (including extreme negative spikes);
3. 3.

   Impact strength/decay in the execution model (spread, temporary coefficient η\eta, transient kernel GG);
4. 4.

   Time-to-expiry, emphasizing near-expiry regimes where greeks and liquidity risks intensify.

All stressed configurations remain free of *static* arbitrage by construction.

##### Unified sample sizes and multiple seeds.

To ensure fair comparisons, each method/variant is evaluated on the *same* set of scenario seeds and the same number of paths per seed.
When legacy artifacts contain differing sample sizes (e.g., n=400n{=}400 vs. n=200n{=}200), we *re-subsample/pair* to a common effective nn per seed, and we report all statistics with *paired* uncertainty across methods.
This protocol reduces variance inflation and follows best practices in RL evaluation [[60](https://arxiv.org/html/2510.04555v1#bib.bib60)].

##### Training and evaluation schedules.

Policies are trained with the IQN–CVaR–PPO learner (Sec. [3.1](https://arxiv.org/html/2510.04555v1#S3.SS1 "3.1 Risk-Sensitive RL with IQN–CVaR–PPO ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) using the Tail-Coverage Controller (Sec. [3.2](https://arxiv.org/html/2510.04555v1#S3.SS2 "3.2 Tail-Coverage Controller: Temperature Sampling and Tail-Boost ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and the white-box CBF–QP safety layer (Sec. [3.3](https://arxiv.org/html/2510.04555v1#S3.SS3 "3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) *active during data collection and evaluation*.
The CVaR level α\alpha tightens from a permissive value (e.g., 0.100.10) toward the target (e.g., 0.0250.025) according to a cosine schedule; KL and entropy coefficients are co-scheduled to limit policy drift.
All wall-clock budgets, iteration counts, and solver tolerances are reported in the reproducibility checklist (Appendix C).

### 5.2 Metrics

##### Tail risk and central performance.

We report absolute-loss VaRα\operatorname{VaR}\_{\alpha} and ESα\operatorname{ES}\_{\alpha} (Sec. [2.6](https://arxiv.org/html/2510.04555v1#S2.SS6 "2.6 Risk Measures: VaR and ES/CVaR ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), along with mean, standard deviation, and portfolio-style ratios:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sharpe | =𝔼​[Π]Var​(Π),(zero risk-free benchmark)​[[61](https://arxiv.org/html/2510.04555v1#bib.bib61)],\displaystyle=\frac{\mathbb{E}[\Pi]}{\sqrt{\mathrm{Var}(\Pi)}},\qquad\text{(zero risk-free benchmark)}~\cite[cite]{[\@@bibref{}{Sharpe1994}{}{}]}, |  | (18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sortino | =𝔼​[Π]𝔼[min(Π,0)2],(downside deviation)​[[62](https://arxiv.org/html/2510.04555v1#bib.bib62)],\displaystyle=\frac{\mathbb{E}[\Pi]}{\sqrt{\mathbb{E}[\min(\Pi,0)^{2}]}},\qquad\text{(downside deviation)}~\cite[cite]{[\@@bibref{}{SortinoPrice1994}{}{}]}, |  | (19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ω​(τ0)\displaystyle\Omega(\tau\_{0}) | =∫τ0∞(1−FΠ​(z))​𝑑z∫−∞τ0FΠ​(z)​𝑑z,τ0=0,(Omega ratio)​[[63](https://arxiv.org/html/2510.04555v1#bib.bib63)].\displaystyle=\frac{\int\_{\tau\_{0}}^{\infty}\big(1-F\_{\Pi}(z)\big)\,dz}{\int\_{-\infty}^{\tau\_{0}}F\_{\Pi}(z)\,dz},\quad\tau\_{0}{=}0,\qquad\text{(Omega ratio)}~\cite[cite]{[\@@bibref{}{KeatingShadwick2002}{}{}]}. |  | (20) |

We visualize distributions with ECDFs and histograms and annotate tail quantiles.

##### Stability and regularization.

We track (i) *policy KL step* 𝔼x[KL(π(⋅|x)∥πref(⋅|x))]\mathbb{E}\_{x}[\mathrm{KL}(\pi(\cdot|x)\|\pi\_{\mathrm{ref}}(\cdot|x))] per update, (ii) *effective tail coverage* w^\widehat{w} relative to the target wtargetw\_{\mathrm{target}}, and (iii) *entropy* of the policy.

##### Safety telemetry.

From the CBF–QP solver, we log active\_set, tightest\_id, rate\_util, gate\_score, slack\_sum, and solver\_status/time (Sec. [3.3](https://arxiv.org/html/2510.04555v1#S3.SS3 "3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), and report:
(i) frequency of the tightest constraints, (ii) slack mass and feasibility rate, and (iii) median/P95 solver time per step.

##### Uncertainty quantification and tests.

For each statistic we report 95%95\% paired bootstrap CIs across scenario paths and seeds [[58](https://arxiv.org/html/2510.04555v1#bib.bib58), [59](https://arxiv.org/html/2510.04555v1#bib.bib59)].
When multiple metrics are tested simultaneously, pp-values are FDR-adjusted using Benjamini–Hochberg [[64](https://arxiv.org/html/2510.04555v1#bib.bib64)].
Effect sizes for pairwise comparisons are summarized via the Vargha–Delaney A^12\hat{A}\_{12} statistic [[65](https://arxiv.org/html/2510.04555v1#bib.bib65)].

### 5.3 Results

##### Distributional evidence.

Figure [2](https://arxiv.org/html/2510.04555v1#S5.F2 "Figure 2 ‣ Distributional evidence. ‣ 5.3 Results ‣ 5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") overlays ECDFs of P&L; Tail-Safe shifts the 11–3%3\% left tail rightwards while keeping the central mass comparable to the QP-only baseline (consistent with the CVaR objective).
Figure [3](https://arxiv.org/html/2510.04555v1#S5.F3 "Figure 3 ‣ Distributional evidence. ‣ 5.3 Results ‣ 5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") shows thinner negative tails for Tail-Safe; premium-normalized variants (not shown) display narrower dispersion.

![Refer to caption](overlay_ecdf.png)


Figure 2: PnL ECDF (overlay). Tail-Safe vs. QP-only baseline on matched scenarios and unified sample sizes. Shaded bands (if present) indicate 95%95\% paired bootstrap CIs at each quantile (Appendix B).

![Refer to caption](overlay_hist.png)


Figure 3: PnL distribution (overlay). Negative tails thin out under Tail-Safe, while the bulk remains comparable. Vertical lines annotate VaRα\operatorname{VaR}\_{\alpha} and ESα\operatorname{ES}\_{\alpha}.

##### Per-variant panels.

Figure [4](https://arxiv.org/html/2510.04555v1#S5.F4 "Figure 4 ‣ Per-variant panels. ‣ 5.3 Results ‣ 5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") reports ECDF/histogram for the QP-only baseline; Figure [5](https://arxiv.org/html/2510.04555v1#S5.F5 "Figure 5 ‣ Per-variant panels. ‣ 5.3 Results ‣ 5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") reports the same for Tail-Safe.
In both, tail markers highlight VaRα\operatorname{VaR}\_{\alpha} and ESα\operatorname{ES}\_{\alpha} at the evaluation α\alpha level.

![Refer to caption](baseline_ecdf.png)


(a) Baseline ECDF

![Refer to caption](baseline_hist.png)


(b) Baseline histogram (+VaR/ES)

Figure 4: QP-only Baseline. Unified samples; tail annotations correspond to α\alpha used at evaluation.



![Refer to caption](tailsafe_ecdf.png)


(a) Tail-Safe ECDF

![Refer to caption](tailsafe_hist.png)


(b) Tail-Safe histogram (+VaR/ES)

Figure 5: Tail-Safe. Left-tail improvement with central mass preserved

##### Training dynamics.

We observe small per-update policy KL (e.g., within a narrow band consistent with the PPO clip parameter), stable effective tail coverage w^≈wtarget\widehat{w}\!\approx\!w\_{\mathrm{target}} across the α\alpha schedule, and smooth critic losses; a single conservative spike in KL can occur when tightening α\alpha, after which EMA referencing re-stabilizes updates (Appendix C: logs and plots).

### 5.4 Ablations

We ablate the key design components to attribute gains and understand failure modes:

1. 1.

   No coverage controller (uniform quantiles): degrades tail estimation and increases training variance; CVaR improvements diminish, especially at small α\alpha.
2. 2.

   No KL–DRO (λKL=0\lambda\_{\mathrm{KL}}{=}0): increases policy drift; occasional regressions in tail metrics under OOD stress.
3. 3.

   No tail guards in QP (no NTB shrinkage / no sign gate): higher drawdowns near expiry and during correlation spikes; feasibility rate decreases.
4. 4.

   Risk-neutral RL + CBF–QP (no CVaR objective): preserves hard safety but does not systematically improve the left tail relative to Tail-Safe.

Table 2: Ablation matrix (qualitative summary). “↑\uparrow”/“↓\downarrow” indicate consistent directional changes vs. Tail-Safe; blank indicates neutral/mixed.

| Variant | ESα | VaRα | Mean/Sharpe | Coverage w^\widehat{w} | Feasibility | Solver time |
| --- | --- | --- | --- | --- | --- | --- |
| No coverage controller | ↑\uparrow (worse) | ↑\uparrow | ↓\downarrow | unstable | ∼\sim | ∼\sim |
| No KL–DRO | ↑\uparrow (worse) | ↑\uparrow | mixed | ∼\sim | ∼\sim | ∼\sim |
| No tail guards (QP) | ↑\uparrow near expiry | ↑\uparrow | ↓\downarrow | ∼\sim | ↓\downarrow | ∼\sim |
| Risk-neutral RL + CBF–QP | ↑\uparrow vs. Tail-Safe | ↑\uparrow | mixed | ∼\sim | ∼\sim | ∼\sim |

### 5.5 Safety Telemetry

##### Active constraints and tightness.

We report the empirical distribution of tightest\_id across time/episodes (Appendix C: bar plots).
Near expiry, NTB and rate caps dominate; during volatility spikes, the sign-consistency gate activates more frequently, suppressing reactive trades.

##### Slack and feasibility.

By construction, when the QP is feasible with ζ=0\zeta{=}0, there are *zero* hard-constraint violations (Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
We tabulate the feasibility rate and the distribution of slack\_sum; infeasibility incidents are rare and trigger a shaped penalty and logging (Appendix C: incident table).

##### Solver latency.

We summarize solver time per step (median/P95) and success rates for OSQP.
Warm starts and modest conditioning of HH keep solve times stable across stress regimes.

### 5.6 Takeaways

Tail-Safe delivers (i) *hard safety with explanations* (active-set, tightness, rate/gate telemetry), (ii) *tail shaping* (improved left-tail metrics as α\alpha tightens) with comparable central performance, and (iii) *robustness under shift* via KL-regularized updates and tail-coverage stabilization.
These properties hold across ID and OOD stress regimes in arbitrage-free, microstructure-aware markets.

## 6 Explainability & Governance

This section operationalizes Tail-Safe for auditability and oversight.
We (i) map solver and learner *telemetry* to concrete *governance workflows* (who inspects which signals and how thresholds trigger actions),
(ii) instantiate common *business rules* (leverage, liquidity, short-sale, drawdown) as white-box CBF constraints together with human-readable interception rationales, and
(iii) define an incident taxonomy and escalation playbook consistent with financial model-risk guidance (e.g., SR 11-7, BCBS 239, NIST AI RMF) [[66](https://arxiv.org/html/2510.04555v1#bib.bib66), [67](https://arxiv.org/html/2510.04555v1#bib.bib67), [68](https://arxiv.org/html/2510.04555v1#bib.bib68)].

### 6.1 Telemetry-to-Governance Mapping

The CBF–QP solver and the RL learner emit stepwise and aggregate telemetry (Sec. [3.3](https://arxiv.org/html/2510.04555v1#S3.SS3 "3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")):
active\_set, tightest\_id, rate\_util, gate\_score, slack\_sum, solver\_status/time, the per-update policy KL\_step, the effective tail coverage w^\widehat{w}, and the CVaR schedule α\alpha.
Table [3](https://arxiv.org/html/2510.04555v1#S6.T3 "Table 3 ‣ 6.1 Telemetry-to-Governance Mapping ‣ 6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") translates these signals into dashboard tiles, thresholds, owners, and actions.
Thresholds are conservative defaults; institution-specific limits can be codified in a policy registry with versioning (Appendix C).

Table 3: Telemetry →\rightarrow governance workflow mapping. “Owner” follows a RACI-style assignment: Trader (TR), Market Risk (MR), Model Risk Management (MRM), Compliance (CO), Operations (OPS), Internal Audit (IA).

| Signal | Dashboard tile | Threshold (example) | Owner | Action on breach |
| --- | --- | --- | --- | --- |
| tightest\_id | Constraint frequency barplot | NTB or Rate >> 60% for 1d | MR →\rightarrow TR | Tighten bands; reschedule |
| slack\_sum | Slack mass time series | Any >0>0 (event) | MRM/CO | Incident; penalty; freeze size |
| solver\_status/time | P95 latency/solve status | P95 >> 20ms or nonoptimal >>0.1% | OPS | Warm-start; failover; add capacity |
| rate\_util | Rate utilization histogram | P95 >0.9>0.9 for 1h | MR →\rightarrow TR | Cut rmaxr\_{\max}; stagger hedges |
| gate\_score | Gate pass-rate | Pass-rate <85%<85\% intraday | MRM | Audit; recal δadv\delta\_{\mathrm{adv}} |
| KL\_step | Policy KL per update | P95 >β⋆>\beta^{\star} | MRM | ↑λKL\uparrow\lambda\_{\mathrm{KL}}; slow schedule |
| w^\widehat{w} vs. wtargetw\_{\mathrm{target}} | Tail coverage gauge | |w^−wtarget|>0.02|\widehat{w}-w\_{\mathrm{target}}|>0.02 | MRM | PID retune; ↑\uparrowbatch |
| α\alpha schedule | CVaR level tracker | Failed to tighten on time | MRM | Hold; check variance |

##### Explanation artifacts.

For each interception (i.e., when utnom≠utu\_{t}^{\mathrm{nom}}\neq u\_{t}), we log a structured *Explanation Record*:
(i) IDs/names of the active constraints (from active\_set),
(ii) the *tightest* constraint and its slack/multiplier,
(iii) the HH-metric deviation ‖ut−utnom‖H\|u\_{t}{-}u\_{t}^{\mathrm{nom}}\|\_{H},
(iv) human-readable rule names (e.g., “Leverage limit”), and
(v) a natural-language rationale template (below).
Records are immutable and indexed for audit queries (Appendix C.2: storage schema).

### 6.2 Business Rules as CBF Constraints (with Explanations)

We instantiate common policy limits as barrier functions hi​(x)≥0h\_{i}(x)\!\geq\!0; each one admits a plain-language explanation and a quantitative telemetry view.

Table 4: Business rules →\rightarrow CBF instantiation and explanation.

| Rule | CBF form (illustrative) | Explanation (human-readable) |
| --- | --- | --- |
| Leverage cap | hlev​(x)=Lmax−Lev​(x)h\_{\mathrm{lev}}(x)=L\_{\max}-\mathrm{Lev}(x) | “Leverage cannot exceed LmaxL\_{\max}; trade reduced to keep hlev≥0h\_{\mathrm{lev}}\geq 0.” |
| Liquidity budget | hliq​(x,u)=Vavail​(x)−‖u‖Λh\_{\mathrm{liq}}(x,u)=V\_{\mathrm{avail}}(x)-\|u\|\_{\Lambda} | “Order size limited by available depth/impact budget.” |
| Short-sale limit | hshort​(x)=Qmin−qshort​(x)h\_{\mathrm{short}}(x)=Q\_{\min}-q\_{\mathrm{short}}(x) | “Short inventory cannot breach QminQ\_{\min}.” |
| Drawdown guard | hdd​(x)=Dmax−DD​(x)h\_{\mathrm{dd}}(x)=D\_{\max}-\mathrm{DD}(x) | “Cumulative drawdown kept below DmaxD\_{\max}.” |
| Rate cap | implicit via ‖ut−ut−1‖2≤rmax\|u\_{t}{-}u\_{t-1}\|\_{2}\leq r\_{\max} | “Adjustment rate bounded by rmaxr\_{\max} to avoid whipsaw.” |
| NTB (ellipsoid) | e⊤​M​e≤bmaxe^{\top}Me\leq b\_{\max} | “Exposure error confined within the no-trade band.” |
| Sign gate | gcons​(x,u)≥0g\_{\mathrm{cons}}(x,u)\geq 0 | “Trade direction must align with signals beyond δadv\delta\_{\mathrm{adv}}.” |

##### Illustrative explanations.

For each rule, the solver’s KKT multipliers quantify *how binding* the rule is; we surface them as “tightness” bars in the dashboard.
For example, if tightest\_id corresponds to *Rate cap*, the explanation highlights the capped step and suggests staggering or a temporary rmaxr\_{\max} reduction.

### 6.3 Incident Taxonomy and Escalation Playbook

We classify events into three severities with actionable responses and owners.

Table 5: Incident taxonomy and escalation.

| Severity | Condition | Owner | Response |
| --- | --- | --- | --- |
| S1 (soft intercept) | utnom≠utu\_{t}^{\mathrm{nom}}\neq u\_{t}, ‖ζ‖1=0\|\zeta\|\_{1}=0 | TR/MR | Log record; no halt; monitor tightest frequencies |
| S2 (hard intercept) | ‖ζ‖1>0\|\zeta\|\_{1}>0 or repeated rate saturation | MRM/CO | Apply penalty; partial freeze; review constraints; RCA within 1d |
| S3 (solver failure) | Non-optimal status or timeout | OPS/MRM | Failover; revert to baseline QP-only; RCA within 4h; postmortem |

##### Trigger logic (runtime).

The following policies are enforced online and recorded for audit (pseudo-code; full governance rules in Appendix C.3):

* •

  Slack trigger: if slack\_sum>0\texttt{slack\\_sum}>0 for kk consecutive steps (k∈[1,3]k\!\in\![1,3]), (i) downscale action norm by η<1\eta\!<\!1, (ii) raise alert to MRM, (iii) freeze size upon repeat.
* •

  Rate saturation trigger: if rate\_util>0.95\texttt{rate\\_util}>0.95 at P95 over 10 minutes, tighten rmaxr\_{\max} by factor ηr\eta\_{r} and stagger orders.
* •

  Gate trigger: if gate pass-rate drops below 85%85\% intraday, increase δadv\delta\_{\mathrm{adv}} and review signals; if unresolved, switch to QP-only baseline.
* •

  KL drift trigger: if KL\_step>β⋆\texttt{KL\\_step}>\beta^{\star} at P95 for 5 updates, raise λKL\lambda\_{\mathrm{KL}} and slow the α\alpha schedule.

### 6.4 Audit Queries and Periodic Reviews

In addition to runtime triggers, periodic reviews (weekly/monthly) support compliance and internal audit:

1. 1.

   Constraint mix: distribution of tightest\_id by regime (ID/OOD, expiry buckets), highlighting persistent bottlenecks.
2. 2.

   Intercept cost: average HH-norm deviation ‖u−unom‖H\|u{-}u^{\mathrm{nom}}\|\_{H} and its contribution to P&L shortfall (Appendix C.4 decomposition).
3. 3.

   Feasibility trend: time series of feasibility rate and slack mass; root-cause analysis for S2/S3 spikes.
4. 4.

   Tail control: realized ESα\operatorname{ES}\_{\alpha} vs. scheduled α\alpha; coverage tracking (w^,wtarget)(\widehat{w},w\_{\mathrm{target}}).
5. 5.

   Change control: diffs in policy parameters and constraint registries; sign-offs by MRM/CO; SR 11-7 documentation hooks [[66](https://arxiv.org/html/2510.04555v1#bib.bib66)].

##### Human-readable & machine-readable parity.

Every interception has (i) a natural-language rationale (template above) and (ii) a structured record (IDs, multipliers, thresholds, margins).
This parity serves both reviewers and automated conformance checks (BCBS 239 data lineage and auditability requirements) [[67](https://arxiv.org/html/2510.04555v1#bib.bib67)].

### 6.5 Risk, Compliance, and Scope Notes

*Scope.* Tail-Safe enforces selected constraints by construction and exposes telemetry for others.
Constraints whose surrogates are only approximate (e.g., complex liquidity or borrow availability) are flagged as “monitor-only” with thresholds and escalation but not guaranteed by the CBF invariance (Sec. [4](https://arxiv.org/html/2510.04555v1#S4 "4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

*Residual risk.* When the QP is infeasible (rare), we document the fallback (penalty + baseline), the magnitude/duration, and the mitigation timeline, aligning with MRM incident handling [[66](https://arxiv.org/html/2510.04555v1#bib.bib66), [68](https://arxiv.org/html/2510.04555v1#bib.bib68)].
Broader regulatory mapping (e.g., model lifecycle, validation independence, change control) is included in Appendix C (Governance Checklist).

## 7 Limitations and Scope

We summarize the principal limitations of Tail-Safe to clarify the scope of our claims. These caveats are intended to be candid and actionable without diminishing the theoretical contributions in Sections [3](https://arxiv.org/html/2510.04555v1#S3 "3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")–[4](https://arxiv.org/html/2510.04555v1#S4 "4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"). Where appropriate, we outline concrete paths to address each limitation in future work.

##### Synthetic market only.

All experiments (Sec. [5](https://arxiv.org/html/2510.04555v1#S5 "5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) are conducted in an *arbitrage-free but synthetic* environment built from SSVI →\rightarrow Dupire →\rightarrow VIX (§[2.1](https://arxiv.org/html/2510.04555v1#S2.SS1 "2.1 Arbitrage-Free Volatility Surfaces via SSVI ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")–[2.3](https://arxiv.org/html/2510.04555v1#S2.SS3 "2.3 VIX Leg from Surface-Consistent Variance ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
While this stack ensures static no-arbitrage and inherits stylized skew/term-structure, it does not capture the full richness of historical dynamics (macro news, regime shifts, structural breaks, jumps, cross-sectional co-movement, borrow frictions, corporate actions).
*Scope:* Our empirical claims (tail-shaping, feasibility rates, telemetry behavior) pertain to this controlled setting.
*Next steps:* historical *replay* against top-of-book/L1 or full LOB data; *semi-synthetic* playback injecting real returns with simulated fills; and *conditional stress* using realized event calendars.

##### Simplified execution and microstructure.

The execution adapter abstracts to spread, linear temporary impact, and a transient resilience kernel (Sec. [2.4](https://arxiv.org/html/2510.04555v1#S2.SS4 "2.4 Execution, Microstructure, and Impact ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
It omits queue-reactive dynamics, order priority, asymmetric information/adverse selection, hidden liquidity, fee/rebate tiers, tick-size effects, and venue fragmentation.
*Scope:* Results on cost and latency are indicative, not definitive, for live markets.
*Next steps:* queue-based impact models, order-cancels-replace loops, latency/jitter modeling, cross-venue routing, and *empirical* calibration to venue-level impact curves.

##### Approximation in safety-layer modeling.

The discrete-time CBF constraints rely on local models xt+1=f​(xt)+g​(xt)​utx\_{t+1}=f(x\_{t})+g(x\_{t})u\_{t} and Lipschitz/mismatch bounds (Assumption [1](https://arxiv.org/html/2510.04555v1#Thmassumption1 "Assumption 1 (Local dynamics and mismatch). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
Barrier functions encode business rules via convex surrogates and linearizations in uu (Assumption [3](https://arxiv.org/html/2510.04555v1#Thmassumption3 "Assumption 3 (Convex feasibility). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
*Scope:* The *forward-invariance guarantee* (Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) holds when the QP is feasible with zero slack ( ζ=0\zeta{=}0) and the margin condition is satisfied.
When the QP is infeasible (rare in our synthetic tests), the layer reverts to penalties and logging; it does not *guarantee* satisfaction.
*Next steps:* robust/tube CBFs, disturbance observers, set-valued dynamics, and feasibility recovery strategies; formal analysis of linearization error budgets (Appendix A.6 road map).

##### Estimator variance and controller tuning.

The temperature-tilted CVaR estimator is self-normalized and subject to variance/bias trade-offs controlled by (T,γtail)(T,\gamma\_{\mathrm{tail}}) and the coverage controller (Sec. [3.2](https://arxiv.org/html/2510.04555v1#S3.SS2 "3.2 Tail-Coverage Controller: Temperature Sampling and Tail-Boost ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
*Scope:* The concentration result (Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) holds under bounded losses and weights, and for an *effective* tail mass close to the target; misspecification of these conditions can inflate variance.
*Next steps:* adaptive batch-sizing, control-theoretic anti-windup, and doubly-robust estimators for tail integrals.

##### Trust-region and robustness assumptions.

The DRO bound (Theorem [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) relies on occupancy coupling to relate pathwise and per-state KL;
the CVaR trust-region result (Theorem [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) uses Lipschitz smoothness and Pinsker-type bounds to control distribution shift.
*Scope:* These are standard but *local* assumptions; violations (e.g., abrupt policy changes, heavy-tailed losses) can weaken constants or rates.
*Next steps:* stronger coupling via mixing coefficients or spectral gaps; nonasymptotic pathwise bounds; heavy-tail robustification.

##### Metric coverage.

We optimize and report CVaR/ES at a given α\alpha (§[2.6](https://arxiv.org/html/2510.04555v1#S2.SS6 "2.6 Risk Measures: VaR and ES/CVaR ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")); other tail functionals (extreme quantiles, expectiles, drawdown risk, spectral measures) are not directly optimized.
*Scope:* Improvements outside the targeted α\alpha are empirical rather than guaranteed.
*Next steps:* multi-level or spectral risk objectives; path-dependent risk control (drawdown CBFs) with proofs paralleling Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

##### Generalization across books and instruments.

We focus on a stylized SPX–VIX hedging book.
*Scope:* Constraints and signals (NTB, sign gate) are finance-specific but not yet validated for rates/credit/commodities or multi-currency portfolios.
*Next steps:* multi-asset extension with cross-gamma/vega and inventory coupling; borrow/rehypothecation constraints; FX basis and curve risk.

##### Governance and compliance boundaries.

The telemetry-to-governance mapping (Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) aligns with common guidance, but it is not a substitute for institution-specific model governance (validation independence, challenger models, change control).
*Scope:* We provide an *operational* starting point (dashboards, triggers, audit records) rather than a complete compliance program.
*Next steps:* integration with enterprise MRM workflows (SR 11-7/BCBS 239/NIST AI RMF), automated conformance checks, and periodic model risk reviews.

##### Ethical and adversarial considerations.

We do not model adversarial behavior (probing, spoofing, latency games) against the agent or the execution venue.
*Scope:* Safety guarantees are not security guarantees.
*Next steps:* adversarial stress testing, red-team evaluations, and anomaly detection hooks tied to telemetry.

##### Computational constraints.

Real-time feasibility depends on solver latency, model size, and hardware. Our OSQP-based implementation meets timing in the synthetic setup, but live deployments may face tighter budgets.
*Scope:* The results demonstrate feasibility *in silico*.
*Next steps:* problem sparsity exploitation, warm-start policies, batching, and hardware acceleration.

##### Summary of claims.

(i) *Hard safety* is guaranteed by construction *only* when the QP is feasible with zero slack and under the margin conditions (Thm. [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"));
(ii) *Tail improvements* are demonstrated empirically in arbitrage-free synthetic markets and supported by estimator concentration (Thm. [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and trust-region reasoning (Thm. [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"));
(iii) *Explainability* follows from the CBF–QP’s active-set/dual telemetry and the projection interpretation (Prop. [1](https://arxiv.org/html/2510.04555v1#Thmproposition1 "Proposition 1 (Shifted projection). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
Real-data backtesting and broader market coverage are deliberately left to future work to preserve a clean separation between theory and synthetic evaluation.

## 8 Related Work

We review connections to prior work on (i) deep hedging and RL in finance, (ii) risk-sensitive/CVaR reinforcement learning, (iii) safety filters and control-barrier-function (CBF) methods for safe RL, (iv) distributionally robust RL (DRO-RL), and (v) explainability and governance for financial ML. Our approach differs by combining *distributional, CVaR-optimized learning* with a *white-box CBF–QP safety layer* that provides *stepwise audit telemetry* and by establishing *theoretical guarantees* (Sec. [4](https://arxiv.org/html/2510.04555v1#S4 "4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) that link KL-regularized policy updates to a KL–DRO upper bound and a CVaR trust-region improvement inequality, while proving robust forward invariance and feasibility persistence for the safety layer.

##### Deep hedging and RL in finance.

Deep hedging learns nonparametric hedge policies under frictions and liquidity constraints [[6](https://arxiv.org/html/2510.04555v1#bib.bib6)], and recent surveys catalogue advances in trading/hedging RL [[10](https://arxiv.org/html/2510.04555v1#bib.bib10), [11](https://arxiv.org/html/2510.04555v1#bib.bib11), [12](https://arxiv.org/html/2510.04555v1#bib.bib12)].
Other lines integrate microstructure and execution—from Almgren–Chriss and Obizhaeva–Wang impact models [[1](https://arxiv.org/html/2510.04555v1#bib.bib1), [5](https://arxiv.org/html/2510.04555v1#bib.bib5)] to agent-based LOB simulators (ABIDES) [[7](https://arxiv.org/html/2510.04555v1#bib.bib7), [40](https://arxiv.org/html/2510.04555v1#bib.bib40)] and market-microstructure monographs [[77](https://arxiv.org/html/2510.04555v1#bib.bib77)].
Tail-Safe differs in three respects: (i) it *optimizes a tail risk* (CVaR) rather than mean performance, (ii) it enforces *hard state-wise constraints by construction* using a CBF–QP filter with telemetry, and (iii) it provides *formal guarantees* on safety invariance, DRO conservatism via KL, and trust-region CVaR improvement (Theorems [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

##### Risk-sensitive RL and CVaR objectives.

Risk-sensitive RL with coherent risk measures (e.g., CVaR) has been studied via policy gradients and actor–critic methods [[17](https://arxiv.org/html/2510.04555v1#bib.bib17), [19](https://arxiv.org/html/2510.04555v1#bib.bib19), [18](https://arxiv.org/html/2510.04555v1#bib.bib18)], with distributional critics (IQN) offering flexible quantile modeling [[13](https://arxiv.org/html/2510.04555v1#bib.bib13), [14](https://arxiv.org/html/2510.04555v1#bib.bib14)].
Recent works explore scalable or constrained CVaR optimization and robust variants [[37](https://arxiv.org/html/2510.04555v1#bib.bib37), [35](https://arxiv.org/html/2510.04555v1#bib.bib35), [36](https://arxiv.org/html/2510.04555v1#bib.bib36)].
Our contribution is orthogonal: we introduce a *coverage-controlled* quantile sampling scheme that directly stabilizes the *estimation error* of CVaR at small α\alpha (Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), and couple it with a *white-box* safety layer; we also provide a *CVaR trust-region inequality* under per-state KL limits (Theorem [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

##### Safe RL: shielding, projection, and CBF-based filters.

Safe RL surveys cover constraint handling via penalties, Lagrangians, shielding, and model-based fallback [[69](https://arxiv.org/html/2510.04555v1#bib.bib69), [22](https://arxiv.org/html/2510.04555v1#bib.bib22)].
Shielding for discrete MDPs uses a precomputed safety automaton to override unsafe actions [[70](https://arxiv.org/html/2510.04555v1#bib.bib70)]; action projection in continuous control enforces linearized safety via a QP layer [[71](https://arxiv.org/html/2510.04555v1#bib.bib71)].
In control theory, CBF–QP methods enforce forward invariance of safe sets at each step [[23](https://arxiv.org/html/2510.04555v1#bib.bib23), [24](https://arxiv.org/html/2510.04555v1#bib.bib24)], with robust/high-order/differentiable extensions [[30](https://arxiv.org/html/2510.04555v1#bib.bib30), [26](https://arxiv.org/html/2510.04555v1#bib.bib26), [27](https://arxiv.org/html/2510.04555v1#bib.bib27), [25](https://arxiv.org/html/2510.04555v1#bib.bib25)].
Differentiable optimization layers (QP/convex) have also been embedded in deep models [[72](https://arxiv.org/html/2510.04555v1#bib.bib72), [73](https://arxiv.org/html/2510.04555v1#bib.bib73)].
Tail-Safe leverages *discrete-time* CBF constraints specialized to finance (ellipsoidal NTB, box/rate, sign-consistency gate), *proves* robust forward invariance under bounded mismatch (Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and minimal-deviation projection (Proposition [1](https://arxiv.org/html/2510.04555v1#Thmproposition1 "Proposition 1 (Shifted projection). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), and *surfaces KKT/active-set telemetry* to enable audit workflows (Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
Compared to generic projection/shielding, our layer is domain-specific (exposure- and microstructure-aware) and backed by an incident-handling governance mapping.

##### Distributionally robust RL (DRO-RL).

Robust MDPs with uncertainty sets date back to classical analyses [[74](https://arxiv.org/html/2510.04555v1#bib.bib74), [75](https://arxiv.org/html/2510.04555v1#bib.bib75)], with modern variants using ff-divergences or Wasserstein ambiguity sets for policy evaluation and learning [[76](https://arxiv.org/html/2510.04555v1#bib.bib76), [35](https://arxiv.org/html/2510.04555v1#bib.bib35), [36](https://arxiv.org/html/2510.04555v1#bib.bib36)].
In parallel, KL-regularized policy optimization (TRPO/PPO) has a long-standing trust-region interpretation [[15](https://arxiv.org/html/2510.04555v1#bib.bib15), [16](https://arxiv.org/html/2510.04555v1#bib.bib16)] and has been adapted to constrained settings [[48](https://arxiv.org/html/2510.04555v1#bib.bib48)].
We bridge these threads by showing that per-state KL penalties control a *KL–DRO upper bound* on the CVaR surrogate (Theorem [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and yield a *CVaR trust-region improvement* bound (Theorem [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))—to our knowledge, such a pairing of DRO interpretation and CVaR performance-difference analysis has not been stated explicitly for the finance setting with a safety filter.

##### Explainability and governance in financial ML.

Interpretability surveys argue for transparent mechanisms over post-hoc explanations in high-stakes domains [[78](https://arxiv.org/html/2510.04555v1#bib.bib78), [79](https://arxiv.org/html/2510.04555v1#bib.bib79), [80](https://arxiv.org/html/2510.04555v1#bib.bib80)].
Financial firms operate under model-risk governance such as SR 11-7 and BCBS 239, requiring documentation, monitoring, and auditable decision records.
Our telemetry-to-governance mapping (Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) uses *white-box* CBF–QP artifacts (active sets, multipliers, slack, rate utilization, gate scores) to produce *structured* and *human-readable* rationale for each interception, aligning methodologically with those expectations while preserving by-construction safety guarantees.

##### Summary of differences.

Relative to prior deep hedging and RL-in-finance work, Tail-Safe provides (i) *formal tail-risk learning guarantees* (coverage-controlled CVaR estimation and trust-region inequality), (ii) a *finance-specialized, auditable* CBF–QP safety layer with invariance and projection properties, and (iii) a *DRO-consistent* view of KL-regularized updates.
This combination targets *deployable* hedging: robust to distribution shift, safe by construction, and explainable to risk managers and auditors.

## 9 Conclusion

We presented Tail-Safe, a deployability-oriented framework for hedging under market frictions that unifies *distributional, risk-sensitive learning* with a *white-box* safety layer.
On the learning side, we optimize tail risk via IQN–CVaR–PPO and stabilize small-α\alpha training through a *Tail-Coverage Controller* that regulates quantile sampling with temperature and tail-boost.
On the safety side, we enforce state-wise constraints by construction with a finance-specialized CBF–QP filter—combining discrete-time CBF inequalities, an ellipsoidal no-trade band (NTB), box/rate limits, and a sign-consistency gate—and expose *audit-ready telemetry* (active sets, tightness, slack, rate utilization, gate scores, solver status).

##### Theoretical guarantees.

We established a suite of results that elevate Tail-Safe from a pragmatic recipe to a principled method:
(i) *robust forward invariance* of the safety set under bounded model mismatch (Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"));
(ii) a *minimal-deviation* projection interpretation of the safety QP (Proposition [1](https://arxiv.org/html/2510.04555v1#Thmproposition1 "Proposition 1 (Shifted projection). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"));
(iii) a *KL–DRO upper bound* connecting per-state KL regularization to distributionally robust CVaR control (Theorem [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"));
(iv) *concentration and sample-complexity* of the temperature-tilted CVaR estimator with explicit coverage-mismatch terms (Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"));
(v) a *CVaR trust-region improvement* inequality under KL limits (Theorem [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"));
(vi) *feasibility persistence* guarantees for expiry-aware NTB shrinkage and rate tightening (Theorem [5](https://arxiv.org/html/2510.04555v1#Thmtheorem5 "Theorem 5 (Persistence via NTB shrinkage and rate tightening). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")); and
(vii) *negative-advantage suppression* induced by the sign-consistency gate (Proposition [2](https://arxiv.org/html/2510.04555v1#Thmproposition2 "Proposition 2 (Gate-induced lower bound). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
Formal proofs are deferred to Appendix A.

##### Empirical evidence and governance.

In arbitrage-free, microstructure-aware synthetic markets (SSVI→\!\rightarrowDupire→\!\rightarrowVIX with ABIDES/MockLOB execution), Tail-Safe achieves *left-tail improvements* while preserving central performance, with *zero* hard-constraint violations whenever the QP is feasible with zero slack.
Results are reported with unified sample sizes, multiple seeds, and paired bootstrap confidence intervals.
Beyond performance metrics, we demonstrate *operational explainability*: solver/learner telemetry is mapped to governance dashboards and incident playbooks (Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), providing structured, human-readable rationales for each interception alongside machine-verifiable records.

##### Scope and limitations.

Our empirical claims are confined to synthetic but finance-grounded settings; the execution layer abstracts queue-reactive and venue-specific effects; and some guarantees require feasibility and margin conditions (Sec. [7](https://arxiv.org/html/2510.04555v1#S7 "7 Limitations and Scope ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
These boundaries are deliberate: they isolate the methodological core and create a clean landing zone for subsequent validation.

##### Outlook.

We see three promising thrusts for future work.
*(A) Real-data validation:* historical replays with top-of-book or full LOB feeds; semi-synthetic playback that couples realized returns with simulated fills; and event-conditioned stress studies.
*(B) Richer safety and robustness:* queue-reactive impact, borrow/rehypothecation constraints, drawdown and path-dependent CBFs, heavy-tail robust estimators, and tighter pathwise DRO couplings.
*(C) Broader portfolios and lifecycles:* multi-asset books with cross-gamma/vega limits, cross-currency hedging, offline/online hybrids, and deeper integration with enterprise model-risk workflows (change control, challenger models, periodic validation).

##### Final remark.

Tail-Safe aims to narrow the gap between modern RL and institutional requirements by offering *tail-aware learning*, *by-construction safety*, and *auditability* in one coherent framework.
We hope the blend of theory, engineering, and governance presented here provides a reproducible baseline—and a stepping stone toward trustworthy, regulation-ready AI for financial risk management.

## Appendix A Proofs for Section [4](https://arxiv.org/html/2510.04555v1#S4 "4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")

This appendix provides complete proofs for Theorems [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [5](https://arxiv.org/html/2510.04555v1#Thmtheorem5 "Theorem 5 (Persistence via NTB shrinkage and rate tightening). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and Propositions [1](https://arxiv.org/html/2510.04555v1#Thmproposition1 "Proposition 1 (Shifted projection). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [2](https://arxiv.org/html/2510.04555v1#Thmproposition2 "Proposition 2 (Gate-induced lower bound). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").
We use the notation and assumptions introduced in Sections [2](https://arxiv.org/html/2510.04555v1#S2 "2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")–[4](https://arxiv.org/html/2510.04555v1#S4 "4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").
For a positive definite matrix H≻0H\succ 0, we write ‖v‖H:=v⊤​H​v\|v\|\_{H}:=\sqrt{v^{\top}Hv} and ⟨a,b⟩H:=a⊤​H​b\langle a,b\rangle\_{H}:=a^{\top}Hb.

### A.1 Proof of Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (robust forward invariance)

###### Lemma 1 (Lipschitz pushforward under bounded disturbance).

Let h:ℝd→ℝh:\mathbb{R}^{d}\!\to\!\mathbb{R} be LL-Lipschitz. If ‖w‖≤w¯\|w\|\leq\bar{w}, then for any z∈ℝdz\in\mathbb{R}^{d},
h​(z+w)≥h​(z)−L​w¯.h(z+w)\geq h(z)-L\bar{w}.

###### Proof.

By Lipschitz continuity, |h​(z+w)−h​(z)|≤L​‖w‖≤L​w¯|h(z+w)-h(z)|\leq L\|w\|\leq L\bar{w}, hence h​(z+w)≥h​(z)−L​w¯h(z+w)\geq h(z)-L\bar{w}.
∎

###### Proof of Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

Fix tt and an index ii. By Assumption [1](https://arxiv.org/html/2510.04555v1#Thmassumption1 "Assumption 1 (Local dynamics and mismatch). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), xt+1=f​(xt)+g​(xt)​ut+wtx\_{t+1}=f(x\_{t})+g(x\_{t})u\_{t}+w\_{t} with ‖wt‖≤w¯\|w\_{t}\|\leq\bar{w}, and by Assumption [2](https://arxiv.org/html/2510.04555v1#Thmassumption2 "Assumption 2 (Discrete-time CBF constraint with margin). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(f​(xt)+g​(xt)​ut)−(1−κi​Δ​t)​hi​(xt)≥εi≥Li​w¯.h\_{i}\!\big(f(x\_{t})+g(x\_{t})u\_{t}\big)-(1-\kappa\_{i}\Delta t)h\_{i}(x\_{t})\geq\varepsilon\_{i}\geq L\_{i}\bar{w}. |  | (21) |

Applying Lemma [1](https://arxiv.org/html/2510.04555v1#Thmlemma1 "Lemma 1 (Lipschitz pushforward under bounded disturbance). ‣ A.1 Proof of Theorem 1 (robust forward invariance) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") with z=f​(xt)+g​(xt)​utz=f(x\_{t})+g(x\_{t})u\_{t} and w=wtw=w\_{t} gives

|  |  |  |
| --- | --- | --- |
|  | hi​(xt+1)≥hi​(f​(xt)+g​(xt)​ut)−Li​w¯≥([21](https://arxiv.org/html/2510.04555v1#A1.E21 "In A.1 Proof of Theorem 1 (robust forward invariance) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))(1−κi​Δ​t)​hi​(xt)+εi−Li​w¯≥(1−κi​Δ​t)​hi​(xt).h\_{i}(x\_{t+1})\;\geq\;h\_{i}\!\big(f(x\_{t})+g(x\_{t})u\_{t}\big)-L\_{i}\bar{w}\;\stackrel{{\scriptstyle\eqref{eq:margin-app}}}{{\geq}}\;(1-\kappa\_{i}\Delta t)h\_{i}(x\_{t})+\varepsilon\_{i}-L\_{i}\bar{w}\;\geq\;(1-\kappa\_{i}\Delta t)h\_{i}(x\_{t}). |  |

If hi​(xt)≥0h\_{i}(x\_{t})\geq 0, then hi​(xt+1)≥0h\_{i}(x\_{t+1})\geq 0. By induction over tt, the set 𝒞={x:hi​(x)≥0,∀i}\mathcal{C}=\{x:\,h\_{i}(x)\geq 0,\,\forall i\} is forward invariant.
∎

### A.2 Proof of Proposition [1](https://arxiv.org/html/2510.04555v1#Thmproposition1 "Proposition 1 (Shifted projection). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (minimal-deviation projection)

###### Lemma 2 (Strict convexity and uniqueness).

Under Assumption [3](https://arxiv.org/html/2510.04555v1#Thmassumption3 "Assumption 3 (Convex feasibility). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), if H≻0H\succ 0 and the feasible set 𝒮​(xt)\mathcal{S}(x\_{t}) is nonempty, closed, and convex, then the QP ([17](https://arxiv.org/html/2510.04555v1#S3.E17 "In QP formulation and minimal-deviation projection. ‣ 3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) with ζ=0\zeta=0 has a unique minimizer.

###### Proof.

The objective u↦12​‖u−unom‖H2+c⊤​uu\mapsto\frac{1}{2}\|u-u^{\mathrm{nom}}\|\_{H}^{2}+c^{\top}u is strictly convex due to H≻0H\succ 0. A strictly convex function over a nonempty, closed, convex set attains its minimum at a unique point.
∎

###### Proof of Proposition [1](https://arxiv.org/html/2510.04555v1#Thmproposition1 "Proposition 1 (Shifted projection). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

Completing the square yields

|  |  |  |
| --- | --- | --- |
|  | 12​(u−unom)⊤​H​(u−unom)+c⊤​u=12​‖u−(unom−H−1​c)‖H2+const,\frac{1}{2}(u-u^{\mathrm{nom}})^{\top}H(u-u^{\mathrm{nom}})+c^{\top}u=\frac{1}{2}\big\|u-(u^{\mathrm{nom}}-H^{-1}c)\big\|\_{H}^{2}+\mathrm{const}, |  |

where the constant does not depend on uu. Hence minimizing the QP with ζ=0\zeta=0 over 𝒮​(xt)\mathcal{S}(x\_{t}) is equivalent to projecting unom−H−1​cu^{\mathrm{nom}}-H^{-1}c onto 𝒮​(xt)\mathcal{S}(x\_{t}) in the HH-norm. Uniqueness follows from Lemma [2](https://arxiv.org/html/2510.04555v1#Thmlemma2 "Lemma 2 (Strict convexity and uniqueness). ‣ A.2 Proof of Proposition 1 (minimal-deviation projection) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").
∎

### A.3 Proof of Theorem [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (KL–DRO upper bound)

We recall the Donsker–Varadhan variational inequality (e.g., [[54](https://arxiv.org/html/2510.04555v1#bib.bib54), [55](https://arxiv.org/html/2510.04555v1#bib.bib55)]): for any measurable φ\varphi and probability measures Q,PQ,P with Q≪PQ\ll P,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼Q​[φ]≤1η​(KL​(Q∥P)+log⁡𝔼P​[eη​φ]),∀η>0.\mathbb{E}\_{Q}[\varphi]\;\leq\;\frac{1}{\eta}\Big(\mathrm{KL}(Q\|P)+\log\mathbb{E}\_{P}[e^{\eta\varphi}]\Big),\quad\forall\,\eta>0. |  | (22) |

###### Proof of Theorem [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

By Assumption [4](https://arxiv.org/html/2510.04555v1#Thmassumption4 "Assumption 4 (CVaR surrogate). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), for any t∈ℝt\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | CVaRα​(L)=mint⁡{t+1α​𝔼Q​[(L−t)+]}≤t+1α​𝔼Q​[ϕt​(L)],\mathrm{CVaR}\_{\alpha}(L)\;=\;\min\_{t}\,\Big\{t+\frac{1}{\alpha}\mathbb{E}\_{Q}[(L-t)\_{+}]\Big\}\;\leq\;t+\frac{1}{\alpha}\mathbb{E}\_{Q}[\phi\_{t}(L)], |  |

where ϕt​(z)=(z−t)+\phi\_{t}(z)=(z-t)\_{+}. Taking the supremum over Q∈𝒬ρ={Q:KL​(Q∥P)≤ρ}Q\in\mathcal{Q}\_{\rho}=\{Q:\mathrm{KL}(Q\|P)\leq\rho\} and applying ([22](https://arxiv.org/html/2510.04555v1#A1.E22 "In A.3 Proof of Theorem 2 (KL–DRO upper bound) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) to φ=ϕt​(L)\varphi=\phi\_{t}(L) gives

|  |  |  |
| --- | --- | --- |
|  | supQ∈𝒬ρCVaRα​(L)≤mint⁡{t+1α​supQ∈𝒬ρ𝔼Q​[ϕt​(L)]}≤mint⁡{t+1α​η​(ρ+log⁡𝔼P​[eη​ϕt​(L)])}.\sup\_{Q\in\mathcal{Q}\_{\rho}}\mathrm{CVaR}\_{\alpha}(L)\;\leq\;\min\_{t}\left\{t+\frac{1}{\alpha}\sup\_{Q\in\mathcal{Q}\_{\rho}}\mathbb{E}\_{Q}[\phi\_{t}(L)]\right\}\;\leq\;\min\_{t}\left\{t+\frac{1}{\alpha\eta}\Big(\rho+\log\mathbb{E}\_{P}[e^{\eta\phi\_{t}(L)}]\Big)\right\}. |  |

Under Assumption [5](https://arxiv.org/html/2510.04555v1#Thmassumption5 "Assumption 5 (Path-wise KL radius and occupancy control). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), the pathwise radius satisfies ρ≤Cocc​β\rho\leq C\_{\mathrm{occ}}\beta, thus yielding the second claim. This shows that penalizing the per-state KL to keep β\beta small controls a KL–DRO upper bound on the CVaR surrogate.
∎

### A.4 Proof of Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (temperature-tilted CVaR concentration)

We treat CVaR^α\widehat{\mathrm{CVaR}}\_{\alpha} as a self-normalized importance sampling (SNIS) ratio estimator over the *tail block* {τ≤α}\{\tau\leq\alpha\}. Let Ik=𝟏​{τk≤α}I\_{k}=\mathbf{1}\{\tau\_{k}\leq\alpha\} and define

|  |  |  |
| --- | --- | --- |
|  | Xk=wk​Ik​L(τk),Yk=wk​Ik,CVaR^α=∑k=1KXk∑k=1KYk.X\_{k}\;=\;w\_{k}I\_{k}L^{(\tau\_{k})},\qquad Y\_{k}\;=\;w\_{k}I\_{k},\qquad\widehat{\mathrm{CVaR}}\_{\alpha}\;=\;\frac{\sum\_{k=1}^{K}X\_{k}}{\sum\_{k=1}^{K}Y\_{k}}. |  |

We use that |L|≤B|L|\leq B and pT​(τ)≥pmin>0p\_{T}(\tau)\geq p\_{\min}>0 (Assumption [6](https://arxiv.org/html/2510.04555v1#Thmassumption6 "Assumption 6 (Temperature sampling, bounded importance weights, bounded loss). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), hence wk≤1/pmin=:Wmaxw\_{k}\leq 1/p\_{\min}=:W\_{\max} and |Xk|≤B​Wmax|X\_{k}|\leq BW\_{\max}, 0≤Yk≤Wmax0\leq Y\_{k}\leq W\_{\max}.

###### Lemma 3 (Concentration for SNIS ratios with bounded weights).

Let (Xk,Yk)k=1K(X\_{k},Y\_{k})\_{k=1}^{K} be i.i.d. pairs with |Xk|≤a|X\_{k}|\leq a, 0≤Yk≤b0\leq Y\_{k}\leq b, and denote
μX=𝔼​[X1]\mu\_{X}=\mathbb{E}[X\_{1}], μY=𝔼​[Y1]>0\mu\_{Y}=\mathbb{E}[Y\_{1}]>0. Then for any δ∈(0,1)\delta\in(0,1), with probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | |∑k=1KXk∑k=1KYk−μXμY|≤2​aμY​log⁡(4/δ)2​K+2​b​|μX|μY2​log⁡(4/δ)2​K.\left|\frac{\sum\_{k=1}^{K}X\_{k}}{\sum\_{k=1}^{K}Y\_{k}}-\frac{\mu\_{X}}{\mu\_{Y}}\right|\;\leq\;\frac{2a}{\mu\_{Y}}\sqrt{\frac{\log(4/\delta)}{2K}}\;+\;\frac{2b|\mu\_{X}|}{\mu\_{Y}^{2}}\sqrt{\frac{\log(4/\delta)}{2K}}. |  |

###### Proof.

Write SX:=∑k=1KXkS\_{X}:=\sum\_{k=1}^{K}X\_{k}, SY:=∑k=1KYkS\_{Y}:=\sum\_{k=1}^{K}Y\_{k}. Note that

|  |  |  |
| --- | --- | --- |
|  | SXSY−μXμY=SX​μY−μX​SYSY​μY=μY​(SX−K​μX)−μX​(SY−K​μY)SY​μY.\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}=\frac{S\_{X}\mu\_{Y}-\mu\_{X}S\_{Y}}{S\_{Y}\mu\_{Y}}=\frac{\mu\_{Y}(S\_{X}-K\mu\_{X})-\mu\_{X}(S\_{Y}-K\mu\_{Y})}{S\_{Y}\mu\_{Y}}. |  |

Hence on any event where SY>0S\_{Y}>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |SXSY−μXμY|≤μY​|SX−K​μX|+|μX|​|SY−K​μY|SY​μY.\left|\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}\right|\leq\frac{\mu\_{Y}\,|S\_{X}-K\mu\_{X}|+|\mu\_{X}|\,|S\_{Y}-K\mu\_{Y}|}{S\_{Y}\,\mu\_{Y}}. |  | (23) |

We control numerator and denominator separately.

Step 1: Hoeffding bounds for SXS\_{X} and SYS\_{Y}.
Since Xk∈[−a,a]X\_{k}\in[-a,a], Hoeffding’s inequality yields, for any tX>0t\_{X}>0,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|1K​SX−μX|≥tX)≤2​exp⁡(−2​K​tX2(2​a)2)=2​exp⁡(−K​tX22​a2).\mathbb{P}\!\left(\left|\frac{1}{K}S\_{X}-\mu\_{X}\right|\geq t\_{X}\right)\leq 2\exp\!\left(-\frac{2Kt\_{X}^{2}}{(2a)^{2}}\right)=2\exp\!\left(-\frac{Kt\_{X}^{2}}{2a^{2}}\right). |  |

Similarly, Yk∈[0,b]Y\_{k}\in[0,b] implies, for any tY>0t\_{Y}>0,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|1K​SY−μY|≥tY)≤2​exp⁡(−2​K​tY2b2).\mathbb{P}\!\left(\left|\frac{1}{K}S\_{Y}-\mu\_{Y}\right|\geq t\_{Y}\right)\leq 2\exp\!\left(-\frac{2Kt\_{Y}^{2}}{b^{2}}\right). |  |

Choose

|  |  |  |
| --- | --- | --- |
|  | tX=a​2​log⁡(4/δ)K,tY=b2​K​log⁡(4/δ).t\_{X}\;=\;a\sqrt{\frac{2\log(4/\delta)}{K}},\qquad t\_{Y}\;=\;\frac{b}{\sqrt{2K}}\sqrt{\log(4/\delta)}. |  |

Then, by a union bound, with probability at least 1−δ1-\delta we have simultaneously

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ:|SX−KμX|≤KtX,|SY−KμY|≤KtY.\mathcal{E}:\quad|S\_{X}-K\mu\_{X}|\leq Kt\_{X},\qquad|S\_{Y}-K\mu\_{Y}|\leq Kt\_{Y}. |  | (24) |

Step 2: keep the denominator away from zero.
On ℰ\mathcal{E} we have the deterministic lower bound

|  |  |  |
| --- | --- | --- |
|  | SY≥K​(μY−tY).S\_{Y}\;\geq\;K(\mu\_{Y}-t\_{Y}). |  |

If tY≤μY/2t\_{Y}\leq\mu\_{Y}/2 (which is a mild requirement for KK; see below), then SY≥K​μY/2S\_{Y}\geq K\mu\_{Y}/2. Even without this simplification, from ([23](https://arxiv.org/html/2510.04555v1#A1.E23 "In A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and ([24](https://arxiv.org/html/2510.04555v1#A1.E24 "In A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) we obtain on ℰ\mathcal{E}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |SXSY−μXμY|\displaystyle\left|\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}\right| | ≤μY​(K​tX)+|μX|​(K​tY)K​(μY−tY)​μY\displaystyle\leq\frac{\mu\_{Y}\,(Kt\_{X})+|\mu\_{X}|\,(Kt\_{Y})}{K(\mu\_{Y}-t\_{Y})\,\mu\_{Y}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =tXμY−tY+|μX|μY⋅tYμY−tY.\displaystyle=\frac{t\_{X}}{\mu\_{Y}-t\_{Y}}\;+\;\frac{|\mu\_{X}|}{\mu\_{Y}}\cdot\frac{t\_{Y}}{\mu\_{Y}-t\_{Y}}. |  |

If tY≤μY/2t\_{Y}\leq\mu\_{Y}/2, then μY−tY≥μY/2\mu\_{Y}-t\_{Y}\geq\mu\_{Y}/2, hence

|  |  |  |
| --- | --- | --- |
|  | |SXSY−μXμY|≤2​tXμY+2​|μX|μY2​tY.\left|\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}\right|\;\leq\;\frac{2t\_{X}}{\mu\_{Y}}\;+\;\frac{2|\mu\_{X}|}{\mu\_{Y}^{2}}\,t\_{Y}. |  |

Finally substitute our tX,tYt\_{X},t\_{Y} choices to get

|  |  |  |
| --- | --- | --- |
|  | |SXSY−μXμY|≤2​aμY​log⁡(4/δ)2​K+2​b​|μX|μY2​log⁡(4/δ)2​K,\left|\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}\right|\;\leq\;\frac{2a}{\mu\_{Y}}\sqrt{\frac{\log(4/\delta)}{2K}}\;+\;\frac{2b|\mu\_{X}|}{\mu\_{Y}^{2}}\sqrt{\frac{\log(4/\delta)}{2K}}, |  |

which is the claimed bound.

Remark on the condition tY≤μY/2t\_{Y}\leq\mu\_{Y}/2.
Because tY=b2​K​log⁡(4/δ)t\_{Y}=\frac{b}{\sqrt{2K}}\sqrt{\log(4/\delta)}, a sufficient condition is
K≥2​b2μY2​log⁡4δK\geq\frac{2b^{2}}{\mu\_{Y}^{2}}\log\!\frac{4}{\delta}.
If KK is smaller, we can keep the more general denominator factor μY−tY\mu\_{Y}-t\_{Y} in the bound, i.e.,

|  |  |  |
| --- | --- | --- |
|  | |SXSY−μXμY|≤tXμY−tY+|μX|μY⋅tYμY−tY,\left|\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}\right|\leq\frac{t\_{X}}{\mu\_{Y}-t\_{Y}}+\frac{|\mu\_{X}|}{\mu\_{Y}}\cdot\frac{t\_{Y}}{\mu\_{Y}-t\_{Y}}, |  |

which reduces to the displayed result once μY−tY≥μY/2\mu\_{Y}-t\_{Y}\geq\mu\_{Y}/2.
∎

###### Lemma 4 (Tail-mass and divergence control).

Let τ∼pT\tau\sim p\_{T} on [0,1][0,1] and I=𝟏​{τ≤α}I=\mathbf{1}\{\tau\leq\alpha\}, α∈(0,1)\alpha\in(0,1). Define the *effective tail mass* αeff:=𝔼​[I]=∫0αpT​(τ)​𝑑τ\alpha\_{\mathrm{eff}}:=\mathbb{E}[I]=\int\_{0}^{\alpha}p\_{T}(\tau)\,d\tau. Then:

1. (i)

   For *unnormalized* importance weights w​(τ)=1/pT​(τ)w(\tau)=1/p\_{T}(\tau), one has

   |  |  |  |
   | --- | --- | --- |
   |  | μY:=𝔼​[w​(τ)​I]=∫0α1pT​(τ)​pT​(τ)​𝑑τ=α.\mu\_{Y}\;:=\;\mathbb{E}[w(\tau)\,I]=\int\_{0}^{\alpha}\frac{1}{p\_{T}(\tau)}\,p\_{T}(\tau)\,d\tau=\alpha. |  |
2. (ii)

   The deviation of the effective tail mass from the uniform baseline is controlled by total variation:

   |  |  |  |
   | --- | --- | --- |
   |  | |αeff−α|=|∫0α(pT​(τ)−1)​𝑑τ|≤‖pT−Unif‖TV:=12​∫01|pT​(τ)−1|​𝑑τ.|\alpha\_{\mathrm{eff}}-\alpha|=\left|\int\_{0}^{\alpha}\big(p\_{T}(\tau)-1\big)\,d\tau\right|\;\leq\;\|p\_{T}-\mathrm{Unif}\|\_{\mathrm{TV}}:=\frac{1}{2}\int\_{0}^{1}\big|p\_{T}(\tau)-1\big|\,d\tau. |  |

###### Proof.

(i) is a direct computation using the definition of unnormalized importance weights. In particular, the expected *weighted* indicator integrates to the Lebesgue measure of the tail set [0,α][0,\alpha], namely α\alpha.

For (ii), recall the variational characterization of total variation distance between two probability measures with densities pTp\_{T} and qq on [0,1][0,1]:

|  |  |  |
| --- | --- | --- |
|  | ‖pT−q‖TV=supA⊆[0,1]|∫A(pT​(τ)−q​(τ))​𝑑τ|=12​∫01|pT​(τ)−q​(τ)|​𝑑τ.\|p\_{T}-q\|\_{\mathrm{TV}}=\sup\_{A\subseteq[0,1]}\left|\int\_{A}\big(p\_{T}(\tau)-q(\tau)\big)\,d\tau\right|=\frac{1}{2}\int\_{0}^{1}|p\_{T}(\tau)-q(\tau)|\,d\tau. |  |

Taking q≡1q\equiv 1 (the density of the Unif​[0,1]\mathrm{Unif}[0,1] law) and the particular measurable set A=[0,α]A=[0,\alpha] gives

|  |  |  |
| --- | --- | --- |
|  | |αeff−α|=|∫[0,α](pT−1)​𝑑τ|≤supA|∫A(pT−1)​𝑑τ|=‖pT−Unif‖TV.|\alpha\_{\mathrm{eff}}-\alpha|=\left|\int\_{[0,\alpha]}(p\_{T}-1)\,d\tau\right|\leq\sup\_{A}\left|\int\_{A}(p\_{T}-1)\,d\tau\right|=\|p\_{T}-\mathrm{Unif}\|\_{\mathrm{TV}}. |  |

This proves the claim.

Remark (self-normalized weights).
If one uses *self-normalized* importance weights w~k=w​(τk)/∑j=1Kw​(τj)\tilde{w}\_{k}=w(\tau\_{k})/\sum\_{j=1}^{K}w(\tau\_{j}) *within a batch*, then 𝔼​[w~​I]\mathbb{E}[\tilde{w}\,I] no longer equals α\alpha exactly because of the random denominator. However, for i.i.d. sampling and bounded weights (w≤1/pminw\leq 1/p\_{\min}), the deviation is of order Oℙ​(1/K)O\_{\mathbb{P}}(1/\sqrt{K}) by a delta-method expansion of the ratio estimator. In our concentration analysis we upper bound the ratio using the *unnormalized* moments (μX,μY)(\mu\_{X},\mu\_{Y}) and control the self-normalization effect inside the constants (cf. Lemma [3](https://arxiv.org/html/2510.04555v1#Thmlemma3 "Lemma 3 (Concentration for SNIS ratios with bounded weights). ‣ A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
∎

###### Proof of Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

Let Uk:=𝟏​{τk≤α}U\_{k}:=\mathbf{1}\{\tau\_{k}\leq\alpha\}, w​(τ)=1/pT​(τ)w(\tau)=1/p\_{T}(\tau), and define

|  |  |  |
| --- | --- | --- |
|  | Xk:=w​(τk)​Uk​L(τk),Yk:=w​(τk)​Uk,SX:=∑k=1KXk,SY:=∑k=1KYk,X\_{k}:=w(\tau\_{k})\,U\_{k}\,L^{(\tau\_{k})},\qquad Y\_{k}:=w(\tau\_{k})\,U\_{k},\qquad S\_{X}:=\sum\_{k=1}^{K}X\_{k},\quad S\_{Y}:=\sum\_{k=1}^{K}Y\_{k}, |  |

so that the self-normalized importance-sampling (SNIS) estimator can be written as
CVaR^α=SX/SY\widehat{\mathrm{CVaR}}\_{\alpha}=S\_{X}/S\_{Y}. Assume |L|≤B|L|\leq B and pT​(τ)≥pmin>0p\_{T}(\tau)\geq p\_{\min}>0, hence w​(τ)≤Wmax:=1/pminw(\tau)\leq W\_{\max}:=1/p\_{\min}. Set
μX:=𝔼​[X1]\mu\_{X}:=\mathbb{E}[X\_{1}], μY:=𝔼​[Y1]\mu\_{Y}:=\mathbb{E}[Y\_{1}]; for *unnormalized* weights one has μY=α\mu\_{Y}=\alpha (Lemma [4](https://arxiv.org/html/2510.04555v1#Thmlemma4 "Lemma 4 (Tail-mass and divergence control). ‣ A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")(i)). Let αeff:=ℙ​(τ≤α)=∫0αpT​(τ)​𝑑τ\alpha\_{\mathrm{eff}}:=\mathbb{P}(\tau\leq\alpha)=\int\_{0}^{\alpha}p\_{T}(\tau)d\tau.

##### Step 1: Bernstein bounds for the numerator and denominator.

We have |Xk|≤B​Wmax|X\_{k}|\leq BW\_{\max}, 0≤Yk≤Wmax0\leq Y\_{k}\leq W\_{\max}, and

|  |  |  |
| --- | --- | --- |
|  | σX2:=Var​(X1)≤𝔼​[X12]≤B2​Wmax2​αeff,σY2:=Var​(Y1)≤𝔼​[Y12]≤Wmax2​αeff.\sigma\_{X}^{2}:=\mathrm{Var}(X\_{1})\leq\mathbb{E}[X\_{1}^{2}]\leq B^{2}W\_{\max}^{2}\,\alpha\_{\mathrm{eff}},\qquad\sigma\_{Y}^{2}:=\mathrm{Var}(Y\_{1})\leq\mathbb{E}[Y\_{1}^{2}]\leq W\_{\max}^{2}\,\alpha\_{\mathrm{eff}}. |  |

Bernstein’s inequality yields, for any tX,tY>0t\_{X},t\_{Y}>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|SXK−μX|≥tX)\displaystyle\mathbb{P}\!\left(\left|\frac{S\_{X}}{K}-\mu\_{X}\right|\geq t\_{X}\right) | ≤2​exp⁡(−K​tX22​σX2+23​B​Wmax​tX),\displaystyle\leq 2\exp\!\left(-\frac{Kt\_{X}^{2}}{2\sigma\_{X}^{2}+\frac{2}{3}BW\_{\max}t\_{X}}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|SYK−μY|≥tY)\displaystyle\mathbb{P}\!\left(\left|\frac{S\_{Y}}{K}-\mu\_{Y}\right|\geq t\_{Y}\right) | ≤2​exp⁡(−K​tY22​σY2+23​Wmax​tY).\displaystyle\leq 2\exp\!\left(-\frac{Kt\_{Y}^{2}}{2\sigma\_{Y}^{2}+\frac{2}{3}W\_{\max}t\_{Y}}\right). |  |

Choose absolute constants c1,c2>0c\_{1},c\_{2}>0 and set

|  |  |  |
| --- | --- | --- |
|  | tX:=c1​B​Wmax​(2​αeff​log⁡(4/δ)K+log⁡(4/δ)K),tY:=c2​Wmax​(2​αeff​log⁡(4/δ)K+log⁡(4/δ)K).t\_{X}:=c\_{1}\,BW\_{\max}\!\left(\sqrt{\frac{2\alpha\_{\mathrm{eff}}\log(4/\delta)}{K}}+\frac{\log(4/\delta)}{K}\right),\quad t\_{Y}:=c\_{2}\,W\_{\max}\!\left(\sqrt{\frac{2\alpha\_{\mathrm{eff}}\log(4/\delta)}{K}}+\frac{\log(4/\delta)}{K}\right). |  |

By a union bound, with probability at least 1−δ1-\delta the event

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ:|SXK−μX|≤tX,|SYK−μY|≤tY\mathcal{E}:\quad\Big|\tfrac{S\_{X}}{K}-\mu\_{X}\Big|\leq t\_{X},\qquad\Big|\tfrac{S\_{Y}}{K}-\mu\_{Y}\Big|\leq t\_{Y} |  | (25) |

holds simultaneously.

##### Step 2: ratio linearization and denominator control.

Using the algebraic identity

|  |  |  |
| --- | --- | --- |
|  | SXSY−μXμY=μY​(SX−K​μX)−μX​(SY−K​μY)SY​μY,\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}=\frac{\mu\_{Y}(S\_{X}-K\mu\_{X})-\mu\_{X}(S\_{Y}-K\mu\_{Y})}{S\_{Y}\,\mu\_{Y}}, |  |

we obtain, on {SY>0}\{S\_{Y}>0\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |SXSY−μXμY|≤μY​|SX−K​μX|+|μX|​|SY−K​μY|SY​μY.\left|\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}\right|\leq\frac{\mu\_{Y}|S\_{X}-K\mu\_{X}|+|\mu\_{X}||S\_{Y}-K\mu\_{Y}|}{S\_{Y}\,\mu\_{Y}}. |  | (26) |

On ℰ\mathcal{E}, SY≥K​(μY−tY)S\_{Y}\geq K(\mu\_{Y}-t\_{Y}). For unnormalized weights, μY=α\mu\_{Y}=\alpha; if KK is such that tY≤α/2t\_{Y}\leq\alpha/2 (e.g., K≥2​Wmax2α2​log⁡(4/δ)K\geq\tfrac{2W\_{\max}^{2}}{\alpha^{2}}\log(4/\delta) suffices), then SY≥K​α/2S\_{Y}\geq K\alpha/2 and therefore, combining ([25](https://arxiv.org/html/2510.04555v1#A1.E25 "In Step 1: Bernstein bounds for the numerator and denominator. ‣ A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and ([26](https://arxiv.org/html/2510.04555v1#A1.E26 "In Step 2: ratio linearization and denominator control. ‣ A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | |SXSY−μXμY|≤2​tXα+2​|μX|α2​tY.\left|\frac{S\_{X}}{S\_{Y}}-\frac{\mu\_{X}}{\mu\_{Y}}\right|\leq\frac{2t\_{X}}{\alpha}+\frac{2|\mu\_{X}|}{\alpha^{2}}t\_{Y}. |  | (27) |

Moreover |μX|=|𝔼​[L​Y]|≤B​𝔼​[Y]=B​α|\mu\_{X}|=|\mathbb{E}[L\,Y]|\leq B\,\mathbb{E}[Y]=B\alpha. Substituting tX,tYt\_{X},t\_{Y} into ([27](https://arxiv.org/html/2510.04555v1#A1.E27 "In Step 2: ratio linearization and denominator control. ‣ A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) yields, on ℰ\mathcal{E},

|  |  |  |
| --- | --- | --- |
|  | |CVaR^α−CVaRα|≤C1​B​(Wmaxα)​αeff​log⁡(4/δ)K+C1′​B​(Wmaxα)​log⁡(4/δ)K,\left|\widehat{\mathrm{CVaR}}\_{\alpha}-\mathrm{CVaR}\_{\alpha}\right|\leq C\_{1}B\left(\frac{W\_{\max}}{\alpha}\right)\sqrt{\frac{\alpha\_{\mathrm{eff}}\log(4/\delta)}{K}}\;+\;C\_{1}^{\prime}B\left(\frac{W\_{\max}}{\alpha}\right)\frac{\log(4/\delta)}{K}, |  |

for absolute constants C1,C1′C\_{1},C\_{1}^{\prime} (absorbing c1,c2c\_{1},c\_{2}). Treating the evaluation level α\alpha as a fixed constant and absorbing WmaxW\_{\max} into C1C\_{1}, the leading term takes the canonical form

|  |  |  |
| --- | --- | --- |
|  | |CVaR^α−CVaRα|≤C1​B​log⁡(4/δ)K​αeff+C1′​B​log⁡(4/δ)K.\left|\widehat{\mathrm{CVaR}}\_{\alpha}-\mathrm{CVaR}\_{\alpha}\right|\leq C\_{1}B\sqrt{\frac{\log(4/\delta)}{K\,\alpha\_{\mathrm{eff}}}}\;+\;C\_{1}^{\prime}B\frac{\log(4/\delta)}{K}. |  |

##### Step 3: coverage mismatch between αeff\alpha\_{\mathrm{eff}} and α\alpha.

Write CVaRβ=1β​∫0βq​(u)​𝑑u\mathrm{CVaR}\_{\beta}=\frac{1}{\beta}\int\_{0}^{\beta}q(u)\,du, q​(u):=FL−1​(u)q(u):=F^{-1}\_{L}(u).
For |q|≤B|q|\leq B and any β,β′>0\beta,\beta^{\prime}>0,

|  |  |  |
| --- | --- | --- |
|  | |CVaRβ−CVaRβ′|≤|1β−1β′|​|∫0min⁡{β,β′}q|+1max⁡{β,β′}​|∫min⁡{β,β′}max⁡{β,β′}q|≤C2​B​|β−β′|,\left|\mathrm{CVaR}\_{\beta}-\mathrm{CVaR}\_{\beta^{\prime}}\right|\leq\left|\frac{1}{\beta}-\frac{1}{\beta^{\prime}}\right|\!\left|\int\_{0}^{\min\{\beta,\beta^{\prime}\}}q\right|+\frac{1}{\max\{\beta,\beta^{\prime}\}}\left|\int\_{\min\{\beta,\beta^{\prime}\}}^{\max\{\beta,\beta^{\prime}\}}q\right|\leq C\_{2}B\,|\beta-\beta^{\prime}|, |  |

for a constant C2C\_{2} depending only on a lower bound of β,β′\beta,\beta^{\prime} (e.g., C2≤2/αminC\_{2}\leq 2/\alpha\_{\min} if β,β′∈[αmin,1]\beta,\beta^{\prime}\in[\alpha\_{\min},1]). Hence

|  |  |  |
| --- | --- | --- |
|  | |CVaRαeff−CVaRα|≤C2​B​|αeff−α|≤C2​B​‖pT−Unif‖TV,\big|\mathrm{CVaR}\_{\alpha\_{\mathrm{eff}}}-\mathrm{CVaR}\_{\alpha}\big|\leq C\_{2}B\,|\alpha\_{\mathrm{eff}}-\alpha|\leq C\_{2}B\,\|p\_{T}-\mathrm{Unif}\|\_{\mathrm{TV}}, |  |

where the last inequality uses Lemma [4](https://arxiv.org/html/2510.04555v1#Thmlemma4 "Lemma 4 (Tail-mass and divergence control). ‣ A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")(ii). This is precisely the *coverage-mismatch* term controlled by the coverage PID.

##### Step 4: union bound and conclusion.

Combining the SNIS ratio deviation (Step 2) on event ℰ\mathcal{E} (which holds with probability ≥1−δ\geq 1-\delta) with the coverage-mismatch bound (Step 3), and absorbing the lower-order O​(log⁡K/K)O(\log K/K) term into the leading constant, we obtain that with probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | |CVaR^α−CVaRα|≤C1​B​log⁡(2/δ)K​αeff+C2​B​|αeff−α|\boxed{\;\left|\widehat{\mathrm{CVaR}}\_{\alpha}-\mathrm{CVaR}\_{\alpha}\right|\;\leq\;C\_{1}B\sqrt{\frac{\log(2/\delta)}{K\,\alpha\_{\mathrm{eff}}}}\;+\;C\_{2}B\,|\alpha\_{\mathrm{eff}}-\alpha|\;} |  |

for universal constants C1,C2C\_{1},C\_{2} depending only on pminp\_{\min} (via WmaxW\_{\max}) and the admissible range of α\alpha. This proves Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").
∎

### A.5 Proof of Theorem [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (CVaR trust-region improvement)

We adapt the policy performance difference argument to the CVaR surrogate in a finite-horizon setting.

###### Lemma 5 (Occupancy shift under per-state KL).

Let {P(⋅∣x,a)}\{P(\cdot\mid x,a)\} be the Markov kernel of the environment on a finite horizon t=0,…,T−1t=0,\dots,T{-}1, and let ptπp\_{t}^{\pi}, ptπ′p\_{t}^{\pi^{\prime}} be the state marginals at step tt under policies π\pi and π′\pi^{\prime} with the same initial distribution p0p\_{0}. Define the (undiscounted) occupancy measures
dπ:=1T​∑t=0T−1ptπ,dπ′:=1T​∑t=0T−1ptπ′.d\_{\pi}:=\frac{1}{T}\sum\_{t=0}^{T-1}p\_{t}^{\pi},\;d\_{\pi^{\prime}}:=\frac{1}{T}\sum\_{t=0}^{T-1}p\_{t}^{\pi^{\prime}}.
Assume (Assumption [7](https://arxiv.org/html/2510.04555v1#Thmassumption7 "Assumption 7 (Per-state KL constraint and smoothness). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) that for all xx,
KL(π′(⋅∣x)∥π(⋅∣x))≤β.\mathrm{KL}\!\big(\pi^{\prime}(\cdot\mid x)\,\|\,\pi(\cdot\mid x)\big)\leq\beta.
Then

|  |  |  |
| --- | --- | --- |
|  | ‖dπ′−dπ‖1≤CT​β,CT=12​(T−1),\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}\;\leq\;C\_{T}\,\sqrt{\beta},\qquad C\_{T}=\sqrt{\tfrac{1}{2}}\,(T-1)\,, |  |

and more generally CT=O​(T)C\_{T}=O(T) if one replaces the crude stepwise accumulation by a mixing-aware constant (see the remark below).

###### Proof.

Step 1: one-step TV deviation between policies via Pinsker.
By Pinsker’s inequality, for every state xx,

|  |  |  |
| --- | --- | --- |
|  | TV(π′(⋅∣x),π(⋅∣x)):=12∥π′(⋅∣x)−π(⋅∣x)∥1≤12KL(π′(⋅∣x)∥π(⋅∣x))≤ε,ε:=β2.\mathrm{TV}\big(\pi^{\prime}(\cdot\mid x),\pi(\cdot\mid x)\big):=\tfrac{1}{2}\|\pi^{\prime}(\cdot\mid x)-\pi(\cdot\mid x)\|\_{1}\;\leq\;\sqrt{\tfrac{1}{2}\,\mathrm{KL}\big(\pi^{\prime}(\cdot\mid x)\,\|\,\pi(\cdot\mid x)\big)}\;\leq\;\varepsilon,\quad\varepsilon:=\sqrt{\tfrac{\beta}{2}}. |  |

Step 2: recursion for state-marginal differences.
Let Δt:=‖ptπ′−ptπ‖1\Delta\_{t}:=\|p\_{t}^{\pi^{\prime}}-p\_{t}^{\pi}\|\_{1}. Since p0π′=p0πp\_{0}^{\pi^{\prime}}=p\_{0}^{\pi}, we have Δ0=0\Delta\_{0}=0. The next-step marginals satisfy

|  |  |  |
| --- | --- | --- |
|  | pt+1π​(x′)=∑x∑aptπ​(x)​π​(a∣x)​P​(x′∣x,a),pt+1π′​(x′)=∑x∑aptπ′​(x)​π′​(a∣x)​P​(x′∣x,a).p\_{t+1}^{\pi}(x^{\prime})=\sum\_{x}\sum\_{a}\,p\_{t}^{\pi}(x)\,\pi(a\mid x)\,P(x^{\prime}\mid x,a),\qquad p\_{t+1}^{\pi^{\prime}}(x^{\prime})=\sum\_{x}\sum\_{a}\,p\_{t}^{\pi^{\prime}}(x)\,\pi^{\prime}(a\mid x)\,P(x^{\prime}\mid x,a). |  |

Subtract and take ℓ1\ell\_{1}-norm:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δt+1\displaystyle\Delta\_{t+1} | =‖pt+1π′−pt+1π‖1\displaystyle=\big\|p\_{t+1}^{\pi^{\prime}}-p\_{t+1}^{\pi}\big\|\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∥∑x(ptπ′(x)−ptπ(x))∑aπ(a∣x)P(⋅∣x,a)∥1+∥∑xptπ′(x)∑a(π′(a∣x)−π(a∣x))P(⋅∣x,a)∥1\displaystyle\leq\left\|\sum\_{x}\big(p\_{t}^{\pi^{\prime}}(x)-p\_{t}^{\pi}(x)\big)\,\sum\_{a}\pi(a\mid x)\,P(\cdot\mid x,a)\right\|\_{1}+\left\|\sum\_{x}p\_{t}^{\pi^{\prime}}(x)\,\sum\_{a}\big(\pi^{\prime}(a\mid x)-\pi(a\mid x)\big)\,P(\cdot\mid x,a)\right\|\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:At+Bt.\displaystyle=:A\_{t}+B\_{t}. |  |

For AtA\_{t}, note that for any probability vector qq and any Markov kernel KK, ‖q​K‖1=‖q‖1\|qK\|\_{1}=\|q\|\_{1}; hence

|  |  |  |
| --- | --- | --- |
|  | At≤∑x|ptπ′​(x)−ptπ​(x)|=Δt.A\_{t}\leq\sum\_{x}|p\_{t}^{\pi^{\prime}}(x)-p\_{t}^{\pi}(x)|=\Delta\_{t}. |  |

For BtB\_{t}, use convexity of the ℓ1\ell\_{1}-norm and that each P(⋅∣x,a)P(\cdot\mid x,a) is a probability vector:

|  |  |  |
| --- | --- | --- |
|  | Bt≤∑xptπ′(x)∥π′(⋅∣x)−π(⋅∣x)∥1≤2ε∑xptπ′(x)=2ε.B\_{t}\leq\sum\_{x}p\_{t}^{\pi^{\prime}}(x)\,\big\|\pi^{\prime}(\cdot\mid x)-\pi(\cdot\mid x)\big\|\_{1}\leq 2\varepsilon\sum\_{x}p\_{t}^{\pi^{\prime}}(x)=2\varepsilon. |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | Δt+1≤Δt+2​ε,⇒Δt≤ 2​t​εby induction (with Δ0=0).\Delta\_{t+1}\;\leq\;\Delta\_{t}+2\varepsilon,\qquad\Rightarrow\qquad\Delta\_{t}\;\leq\;2t\,\varepsilon\quad\text{by induction (with $\Delta\_{0}=0$).} |  |

Step 3: average (undiscounted) occupancy deviation.
By convexity of ∥⋅∥1\|\cdot\|\_{1} and the definition dπ=1T​∑t=0T−1ptπd\_{\pi}=\tfrac{1}{T}\sum\_{t=0}^{T-1}p\_{t}^{\pi},

|  |  |  |
| --- | --- | --- |
|  | ‖dπ′−dπ‖1=‖1T​∑t=0T−1(ptπ′−ptπ)‖1≤1T​∑t=0T−1Δt≤1T​∑t=0T−12​t​ε=ε​(T−1)=12​(T−1)​β.\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}=\left\|\frac{1}{T}\sum\_{t=0}^{T-1}\big(p\_{t}^{\pi^{\prime}}-p\_{t}^{\pi}\big)\right\|\_{1}\;\leq\;\frac{1}{T}\sum\_{t=0}^{T-1}\Delta\_{t}\;\leq\;\frac{1}{T}\sum\_{t=0}^{T-1}2t\,\varepsilon=\varepsilon\,(T-1)=\sqrt{\tfrac{1}{2}}\,(T-1)\sqrt{\beta}. |  |

This proves the stated bound with CT=12​(T−1)C\_{T}=\sqrt{\tfrac{1}{2}}\,(T-1).
∎

*Remark (mixing-aware constants).*
If the Markov chain under π\pi has a Dobrushin (contraction) coefficient η∈[0,1)\eta\in[0,1) so that
‖q​Kπ−q′​Kπ‖1≤η​‖q−q′‖1\|qK^{\pi}-q^{\prime}K^{\pi}\|\_{1}\leq\eta\,\|q-q^{\prime}\|\_{1} for all distributions q,q′q,q^{\prime} (here KπK^{\pi} is the one-step kernel marginalized by π\pi), then the recursion improves to
Δt+1≤η​Δt+2​ε\Delta\_{t+1}\leq\eta\,\Delta\_{t}+2\varepsilon and one gets
Δt≤2​ε​1−ηt1−η\Delta\_{t}\leq 2\varepsilon\,\frac{1-\eta^{t}}{1-\eta} and
‖dπ′−dπ‖1≤2​εT​(1−η)​∑t=0T−1(1−ηt)≤2​ε1−η\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}\leq\frac{2\varepsilon}{T(1-\eta)}\sum\_{t=0}^{T-1}(1-\eta^{t})\leq\frac{2\varepsilon}{1-\eta},
which removes the linear dependence on TT in the well-mixed regime.

###### Lemma 6 (CVaR performance expansion under importance reweighting).

Fix horizon TT and confidence α∈(0,1)\alpha\in(0,1). Let Jα​(π)=CVaRα​(LT​(π))J\_{\alpha}(\pi)=\mathrm{CVaR}\_{\alpha}(L\_{T}(\pi)) be defined via the Rockafellar–Uryasev surrogate:

|  |  |  |
| --- | --- | --- |
|  | Jα​(π)=mint∈ℝ⁡{t+1α​𝔼π​[(LT−t)+]}.J\_{\alpha}(\pi)\;=\;\min\_{t\in\mathbb{R}}\left\{\,t+\frac{1}{\alpha}\,\mathbb{E}\_{\pi}\big[(L\_{T}-t)\_{+}\big]\right\}. |  |

Let t⋆​(π)t^{\star}(\pi) be any minimizer for π\pi, and define the per-step CVaR advantage A~π(α)​(x,u)\tilde{A}\_{\pi}^{(\alpha)}(x,u) relative to the baseline induced by t⋆​(π)t^{\star}(\pi).111Formally, one can define a stepwise surrogate ft(α)​(x,u)f\_{t}^{(\alpha)}(x,u) whose cumulative expectation equals α−1​𝔼π​[(LT−t⋆​(π))+]−α−1​𝔼π​[(LT−t⋆​(π))+∣xt]\alpha^{-1}\mathbb{E}\_{\pi}[(L\_{T}-t^{\star}(\pi))\_{+}]-\alpha^{-1}\mathbb{E}\_{\pi}[(L\_{T}-t^{\star}(\pi))\_{+}\,\mid\,x\_{t}] and set A~π(α)​(x,u)=ft(α)​(x,u)\tilde{A}\_{\pi}^{(\alpha)}(x,u)=f\_{t}^{(\alpha)}(x,u) so that 𝔼u∼π(⋅∣x)​[A~π(α)​(x,u)]=0\mathbb{E}\_{u\sim\pi(\cdot\mid x)}[\tilde{A}\_{\pi}^{(\alpha)}(x,u)]=0. This mirrors the construction of GAE but for the CVaR surrogate.
Then, for a small policy perturbation π′=π+Δ\pi^{\prime}=\pi+\Delta,

|  |  |  |
| --- | --- | --- |
|  | Jα​(π′)=Jα​(π)+𝔼x∼dπ,u∼π(⋅∣x)​[ω​(x,u)​A~π(α)​(x,u)]+R​(Δ),J\_{\alpha}(\pi^{\prime})=J\_{\alpha}(\pi)+\mathbb{E}\_{x\sim d\_{\pi},\,u\sim\pi(\cdot\mid x)}\!\big[\omega(x,u)\,\tilde{A}\_{\pi}^{(\alpha)}(x,u)\big]+R(\Delta), |  |

where ω​(x,u):=π′​(u∣x)/π​(u∣x)\omega(x,u):=\pi^{\prime}(u\mid x)/\pi(u\mid x) and the remainder satisfies

|  |  |  |
| --- | --- | --- |
|  | |R​(Δ)|≤C′​‖dπ′−dπ‖1,|R(\Delta)|\;\leq\;C^{\prime}\,\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}, |  |

with C′C^{\prime} depending on the Lipschitz/boundedness constants of the surrogate and the one-step loss (Assumption [7](https://arxiv.org/html/2510.04555v1#Thmassumption7 "Assumption 7 (Per-state KL constraint and smoothness). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

###### Proof.

Step 1: fix the threshold and linearize the objective.
By definition of t⋆​(π)t^{\star}(\pi),

|  |  |  |
| --- | --- | --- |
|  | Jα​(π)=t⋆​(π)+1α​𝔼π​[ϕ​(LT)],ϕ​(z):=(z−t⋆​(π))+.J\_{\alpha}(\pi)=t^{\star}(\pi)+\frac{1}{\alpha}\,\mathbb{E}\_{\pi}\big[\phi(L\_{T})\big],\quad\phi(z):=(z-t^{\star}(\pi))\_{+}. |  |

For the perturbed policy, we have the upper bound

|  |  |  |
| --- | --- | --- |
|  | Jα​(π′)≤t⋆​(π)+1α​𝔼π′​[ϕ​(LT)],J\_{\alpha}(\pi^{\prime})\;\leq\;t^{\star}(\pi)+\frac{1}{\alpha}\,\mathbb{E}\_{\pi^{\prime}}\big[\phi(L\_{T})\big], |  |

since t⋆​(π)t^{\star}(\pi) need not be optimal for π′\pi^{\prime}.

Step 2: decompose the change of expectation by steps.
Let gt​(x,u)g\_{t}(x,u) denote the (measurable) contribution at step tt to the surrogate such that

|  |  |  |
| --- | --- | --- |
|  | 1α​𝔼π​[ϕ​(LT)]=1T​∑t=0T−1𝔼x∼ptπ​𝔼u∼π(⋅∣x)​[gt​(x,u)],\frac{1}{\alpha}\,\mathbb{E}\_{\pi}\big[\phi(L\_{T})\big]\;=\;\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{E}\_{x\sim p\_{t}^{\pi}}\,\mathbb{E}\_{u\sim\pi(\cdot\mid x)}[\,g\_{t}(x,u)\,], |  |

and the analogous identity holds for π′\pi^{\prime}. (This is standard: unroll the horizon-TT expectation and assign to each (xt,ut)(x\_{t},u\_{t}) the conditional-increment of the CVaR surrogate; exact form is immaterial for the linearization.)

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1α​𝔼π′​[ϕ​(LT)]−1α​𝔼π​[ϕ​(LT)]\displaystyle\frac{1}{\alpha}\,\mathbb{E}\_{\pi^{\prime}}[\phi(L\_{T})]-\frac{1}{\alpha}\,\mathbb{E}\_{\pi}[\phi(L\_{T})] | =1T​∑t=0T−1{𝔼x∼ptπ′​𝔼u∼π′(⋅∣x)​[gt​(x,u)]−𝔼x∼ptπ​𝔼u∼π(⋅∣x)​[gt​(x,u)]}\displaystyle=\frac{1}{T}\sum\_{t=0}^{T-1}\!\left\{\mathbb{E}\_{x\sim p\_{t}^{\pi^{\prime}}}\mathbb{E}\_{u\sim\pi^{\prime}(\cdot\mid x)}[g\_{t}(x,u)]-\mathbb{E}\_{x\sim p\_{t}^{\pi}}\mathbb{E}\_{u\sim\pi(\cdot\mid x)}[g\_{t}(x,u)]\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1T​∑t=0T−1𝔼x∼ptπ​𝔼u∼π(⋅∣x)​[(ω​(x,u)−1)​gt​(x,u)]⏟importance term\displaystyle=\underbrace{\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{E}\_{x\sim p\_{t}^{\pi}}\mathbb{E}\_{u\sim\pi(\cdot\mid x)}\!\big[(\omega(x,u)-1)\,g\_{t}(x,u)\big]}\_{\text{importance term}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1T​∑t=0T−1𝔼x∼ptπ′−ptπ​𝔼u∼π′(⋅∣x)​[gt​(x,u)]⏟state-distribution remainder.\displaystyle\qquad+\underbrace{\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{E}\_{x\sim p\_{t}^{\pi^{\prime}}-p\_{t}^{\pi}}\mathbb{E}\_{u\sim\pi^{\prime}(\cdot\mid x)}[g\_{t}(x,u)]}\_{\text{state-distribution remainder}}. |  |

Step 3: identify the CVaR advantage and bound the remainder.
Define the baseline bt​(x):=𝔼u∼π(⋅∣x)​[gt​(x,u)]b\_{t}(x):=\mathbb{E}\_{u\sim\pi(\cdot\mid x)}[g\_{t}(x,u)] and set
A~π(α)​(x,u):=gt​(x,u)−bt​(x)\tilde{A}\_{\pi}^{(\alpha)}(x,u):=g\_{t}(x,u)-b\_{t}(x) so that
𝔼u∼π(⋅∣x)​[A~π(α)​(x,u)]=0\mathbb{E}\_{u\sim\pi(\cdot\mid x)}[\tilde{A}\_{\pi}^{(\alpha)}(x,u)]=0 for all xx.
Then the importance term equals

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=0T−1𝔼x∼ptπ​𝔼u∼π(⋅∣x)​[ω​(x,u)​A~π(α)​(x,u)],\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{E}\_{x\sim p\_{t}^{\pi}}\mathbb{E}\_{u\sim\pi(\cdot\mid x)}\!\big[\omega(x,u)\,\tilde{A}\_{\pi}^{(\alpha)}(x,u)\big], |  |

and by convexity of the ℓ1\ell\_{1}-norm,

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=0T−1𝔼x∼ptπ​[⋅]=𝔼x∼dπ​[⋅].\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{E}\_{x\sim p\_{t}^{\pi}}[\cdot]=\mathbb{E}\_{x\sim d\_{\pi}}[\cdot]. |  |

For the remainder, assume |gt​(x,u)|≤G|g\_{t}(x,u)|\leq G uniformly (this follows from the bounded one-step loss and the Lipschitz/smoothness in Assumption [7](https://arxiv.org/html/2510.04555v1#Thmassumption7 "Assumption 7 (Per-state KL constraint and smoothness). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")); then

|  |  |  |
| --- | --- | --- |
|  | |1T​∑t=0T−1𝔼x∼ptπ′−ptπ​𝔼u∼π′(⋅∣x)​[gt​(x,u)]|≤GT​∑t=0T−1‖ptπ′−ptπ‖1=G​‖dπ′−dπ‖1.\left|\frac{1}{T}\sum\_{t=0}^{T-1}\mathbb{E}\_{x\sim p\_{t}^{\pi^{\prime}}-p\_{t}^{\pi}}\mathbb{E}\_{u\sim\pi^{\prime}(\cdot\mid x)}[g\_{t}(x,u)]\right|\;\leq\;\frac{G}{T}\sum\_{t=0}^{T-1}\|p\_{t}^{\pi^{\prime}}-p\_{t}^{\pi}\|\_{1}\;=\;G\,\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}. |  |

Collecting all pieces,

|  |  |  |
| --- | --- | --- |
|  | Jα​(π′)−Jα​(π)≤𝔼x∼dπ,u∼π​[ω​(x,u)​A~π(α)​(x,u)]+G​‖dπ′−dπ‖1,J\_{\alpha}(\pi^{\prime})-J\_{\alpha}(\pi)\;\leq\;\mathbb{E}\_{x\sim d\_{\pi},\,u\sim\pi}\!\big[\omega(x,u)\,\tilde{A}\_{\pi}^{(\alpha)}(x,u)\big]+G\,\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}, |  |

and a symmetric argument (or replacing π\pi and π′\pi^{\prime}) yields the same lower bound up to constants, which we summarize as
|R​(Δ)|≤C′​‖dπ′−dπ‖1|R(\Delta)|\leq C^{\prime}\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}.
∎

###### Proof of Theorem [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

Recall from Lemma [6](https://arxiv.org/html/2510.04555v1#Thmlemma6 "Lemma 6 (CVaR performance expansion under importance reweighting). ‣ A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") that for any horizon TT and confidence level α∈(0,1)\alpha\in(0,1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jα​(π′)=Jα​(π)+𝔼x∼dπ,u∼π(⋅∣x)​[ω​(x,u)​A~π(α)​(x,u)]⏟importance (first-order) term+R​(Δ)⏟state-distribution remainder,J\_{\alpha}(\pi^{\prime})=J\_{\alpha}(\pi)+\underbrace{\mathbb{E}\_{x\sim d\_{\pi},\,u\sim\pi(\cdot\mid x)}\!\big[\omega(x,u)\,\tilde{A}\_{\pi}^{(\alpha)}(x,u)\big]}\_{\text{importance (first-order) term}}+\underbrace{R(\Delta)}\_{\text{state-distribution remainder}}, |  | (28) |

where ω​(x,u)=π′​(u∣x)/π​(u∣x)\omega(x,u)=\pi^{\prime}(u\mid x)/\pi(u\mid x) and |R​(Δ)|≤C′​‖dπ′−dπ‖1|R(\Delta)|\leq C^{\prime}\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1} for a constant C′C^{\prime} depending on the Lipschitz/boundedness constants of the one-step surrogate (Assumption [7](https://arxiv.org/html/2510.04555v1#Thmassumption7 "Assumption 7 (Per-state KL constraint and smoothness). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
By Lemma [5](https://arxiv.org/html/2510.04555v1#Thmlemma5 "Lemma 5 (Occupancy shift under per-state KL). ‣ A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), if KL(π′(⋅∣x)∥π(⋅∣x))≤β\mathrm{KL}\!\big(\pi^{\prime}(\cdot\mid x)\|\pi(\cdot\mid x)\big)\leq\beta for all xx, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖dπ′−dπ‖1≤CT​β,CT=12​(T−1)(or O​(T) with mixing-aware refinement).\|d\_{\pi^{\prime}}-d\_{\pi}\|\_{1}\;\leq\;C\_{T}\sqrt{\beta},\qquad C\_{T}=\sqrt{\tfrac{1}{2}}\,(T-1)\quad\text{(or $O(T)$ with mixing-aware refinement).} |  | (29) |

Combining ([28](https://arxiv.org/html/2510.04555v1#A1.E28 "In A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and ([29](https://arxiv.org/html/2510.04555v1#A1.E29 "In A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jα​(π′)≤Jα​(π)+𝔼x∼dπ,u∼π​[ω​A~π(α)]+C′​CT​β.J\_{\alpha}(\pi^{\prime})\leq J\_{\alpha}(\pi)+\mathbb{E}\_{x\sim d\_{\pi},\,u\sim\pi}\!\big[\omega\,\tilde{A}\_{\pi}^{(\alpha)}\big]+C^{\prime}C\_{T}\sqrt{\beta}. |  | (30) |

It remains to justify that higher-order terms in the Taylor expansion of the CVaR surrogate w.r.t. policy parameters are o​(‖Δ‖)o(\|\Delta\|), and that the first-order term is well-defined under the per-state KL constraint.

##### Control of higher-order terms.

Let θ\theta parametrize πθ\pi\_{\theta} and θ′=θ+Δ\theta^{\prime}=\theta+\Delta parametrize π′\pi^{\prime}.
Under Assumption [7](https://arxiv.org/html/2510.04555v1#Thmassumption7 "Assumption 7 (Per-state KL constraint and smoothness). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (bounded/smooth one-step loss, bounded horizon), the Rockafellar–Uryasev surrogate
t+α−1​𝔼πθ​[(LT−t)+]t+\alpha^{-1}\mathbb{E}\_{\pi\_{\theta}}[(L\_{T}-t)\_{+}] is locally twice differentiable in θ\theta (Clarke subdifferential reduces to gradient almost everywhere because the hinge is averaged over bounded losses). Thus a second-order Taylor expansion around θ\theta yields

|  |  |  |
| --- | --- | --- |
|  | Jα​(πθ′)=Jα​(πθ)+⟨∇θJα​(πθ),Δ⟩+12​Δ⊤​Hθ​Δ+r​(Δ),J\_{\alpha}(\pi\_{\theta^{\prime}})=J\_{\alpha}(\pi\_{\theta})+\langle\nabla\_{\theta}J\_{\alpha}(\pi\_{\theta}),\,\Delta\rangle+\frac{1}{2}\,\Delta^{\top}H\_{\theta}\Delta+r(\Delta), |  |

with ‖Hθ‖≤CH\|H\_{\theta}\|\leq C\_{H} locally and r​(Δ)=o​(‖Δ‖2)r(\Delta)=o(\|\Delta\|^{2}).
The first-order term equals the importance-weighted advantage in ([28](https://arxiv.org/html/2510.04555v1#A1.E28 "In A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), while the quadratic term is O​(‖Δ‖2)O(\|\Delta\|^{2}).
Since the per-state KL bound β\beta implies a total-variation bound TV​(π′,π)≤β/2\mathrm{TV}(\pi^{\prime},\pi)\leq\sqrt{\beta/2} pointwise (Pinsker), standard inequalities (e.g., Bretagnolle–Huber) give ‖Δ‖=O​(β)\|\Delta\|=O(\sqrt{\beta}) in a local chart, hence
Δ⊤​Hθ​Δ=O​(β)\Delta^{\top}H\_{\theta}\Delta=O(\beta) and is dominated by the O​(β)O(\sqrt{\beta}) term in ([30](https://arxiv.org/html/2510.04555v1#A1.E30 "In A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
Therefore the collected higher-order contribution is o​(‖Δ‖)=o​(β)o(\|\Delta\|)=o(\sqrt{\beta}).

##### Well-posedness of the first-order term.

For each xx, the ratio ω(⋅)=π′(⋅∣x)/π(⋅∣x)\omega(\cdot)=\pi^{\prime}(\cdot\mid x)/\pi(\cdot\mid x) satisfies 𝔼u∼π(⋅∣x)​[ω]=1\mathbb{E}\_{u\sim\pi(\cdot\mid x)}[\omega]=1 and

|  |  |  |
| --- | --- | --- |
|  | 𝔼u∼π(⋅∣x)[|ω−1|]≤ 2TV(π′(⋅∣x),π(⋅∣x))≤2​β,\mathbb{E}\_{u\sim\pi(\cdot\mid x)}[|\omega-1|]\;\leq\;2\,\mathrm{TV}\!\big(\pi^{\prime}(\cdot\mid x),\pi(\cdot\mid x)\big)\;\leq\;\sqrt{2\beta}, |  |

by Pinsker. If |A~π(α)​(x,u)|≤G|\tilde{A}\_{\pi}^{(\alpha)}(x,u)|\leq G uniformly (as in Lemma [6](https://arxiv.org/html/2510.04555v1#Thmlemma6 "Lemma 6 (CVaR performance expansion under importance reweighting). ‣ A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), then

|  |  |  |
| --- | --- | --- |
|  | |𝔼u∼π(⋅∣x)​[(ω−1)​A~π(α)​(x,u)]|≤G​𝔼u∼π​[|ω−1|]≤G​2​β.\Big|\mathbb{E}\_{u\sim\pi(\cdot\mid x)}\big[(\omega-1)\tilde{A}\_{\pi}^{(\alpha)}(x,u)\big]\Big|\leq G\,\mathbb{E}\_{u\sim\pi}[|\omega-1|]\leq G\sqrt{2\beta}. |  |

Averaging over x∼dπx\sim d\_{\pi} preserves the bound, so the first-order term is finite and Lipschitz in β\sqrt{\beta}.

##### Conclusion.

Set Cα:=C′​CTC\_{\alpha}:=C^{\prime}C\_{T}; it depends on the horizon TT, the one-step Lipschitz constant, and the envelope GG of the CVaR surrogate, but is independent of β\beta. Incorporating the o​(‖Δ‖)=o​(β)o(\|\Delta\|)=o(\sqrt{\beta}) residual into the right-hand side of ([30](https://arxiv.org/html/2510.04555v1#A1.E30 "In A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) yields

|  |  |  |
| --- | --- | --- |
|  | Jα​(π′)≤Jα​(π)+𝔼x∼dπ,u∼π​[ω​A~π(α)​(x,u)]+Cα​β+o​(β),J\_{\alpha}(\pi^{\prime})\;\leq\;J\_{\alpha}(\pi)+\mathbb{E}\_{x\sim d\_{\pi},\,u\sim\pi}\!\big[\omega\,\tilde{A}\_{\pi}^{(\alpha)}(x,u)\big]+C\_{\alpha}\sqrt{\beta}+o(\sqrt{\beta}), |  |

which is the claimed CVaR trust-region improvement inequality.
∎

### A.6 Proof of Theorem [5](https://arxiv.org/html/2510.04555v1#Thmtheorem5 "Theorem 5 (Persistence via NTB shrinkage and rate tightening). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (feasibility persistence)

We show that shrinking the NTB radius and tightening the rate cap can maintain feasibility at the next step under Lipschitz dynamics.

###### Lemma 7 (Lipschitz variation of exposure error).

Under Assumption [8](https://arxiv.org/html/2510.04555v1#Thmassumption8 "Assumption 8 (Lipschitz constraints and affine exposure map). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), suppose e:𝒳×𝒰→ℝqe:\mathcal{X}\times\mathcal{U}\to\mathbb{R}^{q} is given by
e​(x,u)=A​(x)​u−d​(x)e(x,u)=A(x)u-d(x), where A:𝒳→ℝq×mA:\mathcal{X}\to\mathbb{R}^{q\times m} and d:𝒳→ℝqd:\mathcal{X}\to\mathbb{R}^{q}
are locally Lipschitz on a neighborhood 𝒩x\mathcal{N}\_{x} of xtx\_{t}. Assume the action set is compact (e.g., by box/rate limits), so that u,ut∈𝒰u,u\_{t}\in\mathcal{U} with ‖u‖≤Umax\|u\|\leq U\_{\max} and ‖ut‖≤Umax\|u\_{t}\|\leq U\_{\max}.
Then there exist finite constants Lex,Leu>0L\_{e}^{x},L\_{e}^{u}>0 (depending on 𝒩x\mathcal{N}\_{x} and 𝒰\mathcal{U}) such that for all (x,u)(x,u) in a neighborhood of (xt,ut)(x\_{t},u\_{t}),

|  |  |  |
| --- | --- | --- |
|  | ‖e​(x,u)−e​(xt,ut)‖≤Lex​‖x−xt‖+Leu​‖u−ut‖.\|e(x,u)-e(x\_{t},u\_{t})\|\;\leq\;L\_{e}^{x}\,\|x-x\_{t}\|\;+\;L\_{e}^{u}\,\|u-u\_{t}\|. |  |

###### Proof.

Fix a compact neighborhood 𝒦x⊂𝒩x\mathcal{K}\_{x}\subset\mathcal{N}\_{x} of xtx\_{t} and a compact set 𝒦u⊂𝒰\mathcal{K}\_{u}\subset\mathcal{U} containing utu\_{t} and all feasible uu in a local tube around utu\_{t} (the existence is guaranteed by box/rate constraints). Because AA and dd are locally Lipschitz on 𝒩x\mathcal{N}\_{x}, there exist finite moduli LA,Ld>0L\_{A},L\_{d}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖A​(x)−A​(y)‖≤LA​‖x−y‖,‖d​(x)−d​(y)‖≤Ld​‖x−y‖,∀x,y∈𝒦x,\|A(x)-A(y)\|\leq L\_{A}\|x-y\|,\qquad\|d(x)-d(y)\|\leq L\_{d}\|x-y\|,\qquad\forall x,y\in\mathcal{K}\_{x}, |  |

where ∥⋅∥\|\cdot\| on matrices denotes the operator norm induced by the Euclidean vector norm.
Furthermore, since AA is continuous on the compact set 𝒦x\mathcal{K}\_{x}, the bound

|  |  |  |
| --- | --- | --- |
|  | MA:=supx∈𝒦x‖A​(x)‖<∞M\_{A}\;:=\;\sup\_{x\in\mathcal{K}\_{x}}\|A(x)\|\;<\;\infty |  |

holds. Now decompose

|  |  |  |
| --- | --- | --- |
|  | e​(x,u)−e​(xt,ut)=A​(x)​(u−ut)+(A​(x)−A​(xt))​ut−(d​(x)−d​(xt)).e(x,u)-e(x\_{t},u\_{t})=A(x)(u-u\_{t})\;+\;\big(A(x)-A(x\_{t})\big)u\_{t}\;-\;\big(d(x)-d(x\_{t})\big). |  |

Taking norms and using the triangle inequality together with the bounds above yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖e​(x,u)−e​(xt,ut)‖\displaystyle\|e(x,u)-e(x\_{t},u\_{t})\| | ≤‖A​(x)‖​‖u−ut‖+‖A​(x)−A​(xt)‖​‖ut‖+‖d​(x)−d​(xt)‖\displaystyle\leq\|A(x)\|\,\|u-u\_{t}\|\;+\;\|A(x)-A(x\_{t})\|\,\|u\_{t}\|\;+\;\|d(x)-d(x\_{t})\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤MA​‖u−ut‖+LA​‖x−xt‖​‖ut‖+Ld​‖x−xt‖\displaystyle\leq M\_{A}\,\|u-u\_{t}\|\;+\;L\_{A}\,\|x-x\_{t}\|\,\|u\_{t}\|\;+\;L\_{d}\,\|x-x\_{t}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤MA​‖u−ut‖+(LA​Umax+Ld)​‖x−xt‖.\displaystyle\leq M\_{A}\,\|u-u\_{t}\|\;+\;(L\_{A}U\_{\max}+L\_{d})\,\|x-x\_{t}\|. |  |

Hence the claim holds with

|  |  |  |
| --- | --- | --- |
|  | Leu:=MA,Lex:=LA​Umax+Ld,L\_{e}^{u}:=M\_{A},\qquad L\_{e}^{x}:=L\_{A}U\_{\max}+L\_{d}, |  |

which depend only on the chosen compact neighborhoods 𝒦x\mathcal{K}\_{x} and 𝒦u\mathcal{K}\_{u} (and thus are uniform locally around (xt,ut)(x\_{t},u\_{t})).
∎

###### Lemma 8 (State drift bound).

Under Assumption [1](https://arxiv.org/html/2510.04555v1#Thmassumption1 "Assumption 1 (Local dynamics and mismatch). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), there exists Lx>0L\_{x}>0 such that, for all feasible xtx\_{t} in a compact tube 𝒦x\mathcal{K}\_{x} and actions utu\_{t} in a compact set 𝒦u\mathcal{K}\_{u},

|  |  |  |
| --- | --- | --- |
|  | ‖xt+1−xt‖≤Lx​(‖ut‖+1)+w¯.\|x\_{t+1}-x\_{t}\|\;\leq\;L\_{x}\big(\|u\_{t}\|+1\big)\;+\;\bar{w}. |  |

###### Proof.

The dynamics are xt+1=f​(xt)+g​(xt)​ut+wtx\_{t+1}=f(x\_{t})+g(x\_{t})u\_{t}+w\_{t}, with ‖wt‖≤w¯\|w\_{t}\|\leq\bar{w}. Fix compact sets 𝒦x∋xt\mathcal{K}\_{x}\ni x\_{t} and 𝒦u∋ut\mathcal{K}\_{u}\ni u\_{t} that contain the closed-loop trajectory locally (box/rate constraints and the CBF conditions ensure such compactness). Since ff and gg are locally Lipschitz (hence continuous), the suprema

|  |  |  |
| --- | --- | --- |
|  | Mf:=supx∈𝒦x‖f​(x)−x‖<∞,Mg:=supx∈𝒦x‖g​(x)‖<∞M\_{f}\;:=\;\sup\_{x\in\mathcal{K}\_{x}}\|f(x)-x\|\;<\;\infty,\qquad M\_{g}\;:=\;\sup\_{x\in\mathcal{K}\_{x}}\|g(x)\|\;<\;\infty |  |

are finite. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖xt+1−xt‖\displaystyle\|x\_{t+1}-x\_{t}\| | =‖f​(xt)−xt+g​(xt)​ut+wt‖\displaystyle=\|f(x\_{t})-x\_{t}+g(x\_{t})u\_{t}+w\_{t}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖f​(xt)−xt‖+‖g​(xt)‖​‖ut‖+‖wt‖\displaystyle\leq\|f(x\_{t})-x\_{t}\|+\|g(x\_{t})\|\,\|u\_{t}\|+\|w\_{t}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Mf+Mg​‖ut‖+w¯.\displaystyle\leq M\_{f}+M\_{g}\,\|u\_{t}\|+\bar{w}. |  |

Finally, let Lx:=max⁡{Mf,Mg}L\_{x}:=\max\{M\_{f},M\_{g}\}. Then Mf+Mg​‖ut‖≤Lx​(1+‖ut‖)M\_{f}+M\_{g}\,\|u\_{t}\|\leq L\_{x}(1+\|u\_{t}\|), and the displayed inequality becomes

|  |  |  |
| --- | --- | --- |
|  | ‖xt+1−xt‖≤Lx​(‖ut‖+1)+w¯,\|x\_{t+1}-x\_{t}\|\leq L\_{x}(\|u\_{t}\|+1)+\bar{w}, |  |

as claimed. The constant LxL\_{x} depends only on the local compact tube 𝒦x\mathcal{K}\_{x} and thus is uniform along any trajectory that remains in 𝒦x\mathcal{K}\_{x}.
∎

##### Remarks.

(i) Lemma [7](https://arxiv.org/html/2510.04555v1#Thmlemma7 "Lemma 7 (Lipschitz variation of exposure error). ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") makes explicit how the exposure map’s sensitivity to state and action splits into a term controlled by a uniform operator-norm bound on A​(⋅)A(\cdot) and a term proportional to the Lipschitz modulus of A​(⋅)A(\cdot) times a local action bound UmaxU\_{\max}, plus the Lipschitz modulus of d​(⋅)d(\cdot).
(ii) Lemma [8](https://arxiv.org/html/2510.04555v1#Thmlemma8 "Lemma 8 (State drift bound). ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") uses only *boundedness on compact sets* for f​(⋅)−idf(\cdot)-\mathrm{id} and g​(⋅)g(\cdot); stronger bounds (e.g., contraction or Jacobian bounds) would refine LxL\_{x} but are not needed for feasibility persistence in Theorem [5](https://arxiv.org/html/2510.04555v1#Thmtheorem5 "Theorem 5 (Persistence via NTB shrinkage and rate tightening). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

###### Proof of Theorem [5](https://arxiv.org/html/2510.04555v1#Thmtheorem5 "Theorem 5 (Persistence via NTB shrinkage and rate tightening). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

Fix a time tt and suppose the QP at tt is solved with ζ=0\zeta=0 (strict feasibility) and with the stated margins in Assumption [9](https://arxiv.org/html/2510.04555v1#Thmassumption9 "Assumption 9 (Margins at time 𝑡). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"):

|  |  |  |
| --- | --- | --- |
|  | (NTB)e​(xt,ut)⊤​M​e​(xt,ut)≤bmax−δb,(rate)‖ut−ut−1‖2≤rmax−δr,\text{(NTB)}\quad e(x\_{t},u\_{t})^{\top}Me(x\_{t},u\_{t})\;\leq\;b\_{\max}-\delta\_{b},\qquad\text{(rate)}\quad\|u\_{t}-u\_{t-1}\|\_{2}\;\leq\;r\_{\max}-\delta\_{r}, |  |

for some δb,δr>0\delta\_{b},\delta\_{r}>0. Throughout, we work on a compact tube 𝒦x×𝒦u\mathcal{K}\_{x}\times\mathcal{K}\_{u} containing (xt,ut)(x\_{t},u\_{t}) (guaranteed by box/rate constraints), so local Lipschitz and boundedness moduli are finite.

We will exhibit a *feasible witness* for the QP at time t+1t{+}1 under the tightened parameters

|  |  |  |
| --- | --- | --- |
|  | bmax′:=ηb​bmax,rmax′:=ηr​rmax,ηb,ηr∈(0,1),b\_{\max}^{\prime}:=\eta\_{b}\,b\_{\max},\qquad r\_{\max}^{\prime}:=\eta\_{r}\,r\_{\max},\qquad\eta\_{b},\eta\_{r}\in(0,1), |  |

and then appeal to convexity to conclude nonemptiness of the feasible set. Our candidate is the *zero-adjustment action*

|  |  |  |
| --- | --- | --- |
|  | u~t+1:=ut.\tilde{u}\_{t+1}:=u\_{t}. |  |

##### Step 1: box and rate constraints.

Box constraints are unchanged in the theorem statement; since utu\_{t} satisfied them at time tt, the same utu\_{t} satisfies them at time t+1t{+}1. For the tightened rate cap we have

|  |  |  |
| --- | --- | --- |
|  | ‖u~t+1−ut‖2=0≤rmax′=ηr​rmax∀ηr∈(0,1),\|\tilde{u}\_{t+1}-u\_{t}\|\_{2}=0\;\leq\;r\_{\max}^{\prime}=\eta\_{r}r\_{\max}\qquad\forall\,\eta\_{r}\in(0,1), |  |

so the rate constraint holds *trivially* for any ηr∈(0,1)\eta\_{r}\in(0,1). (No extra condition such as ηr≤1−δr/rmax\eta\_{r}\leq 1-\delta\_{r}/r\_{\max} is needed when u~t+1=ut\tilde{u}\_{t+1}=u\_{t}.)

##### Step 2: NTB constraint under shrinkage.

Let vt:=e​(xt,ut)v\_{t}:=e(x\_{t},u\_{t}) and vt+1:=e​(xt+1,ut)v\_{t+1}:=e(x\_{t+1},u\_{t}). By Lemma [7](https://arxiv.org/html/2510.04555v1#Thmlemma7 "Lemma 7 (Lipschitz variation of exposure error). ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and Lemma [8](https://arxiv.org/html/2510.04555v1#Thmlemma8 "Lemma 8 (State drift bound). ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥vt+1−vt∥≤Lex∥xt+1−xt∥≤Lex(Lx(∥ut∥+1)+w¯)=:Δe.\|v\_{t+1}-v\_{t}\|\;\leq\;L\_{e}^{x}\|x\_{t+1}-x\_{t}\|\;\leq\;L\_{e}^{x}\Big(L\_{x}(\|u\_{t}\|+1)+\bar{w}\Big)\;=:\Delta\_{e}. |  | (31) |

Using eigenvalue bounds for quadratic forms,

|  |  |  |
| --- | --- | --- |
|  | vt+1⊤​M​vt+1≤λmax​(M)​‖vt+1‖2≤λmax​(M)​(‖vt‖+‖vt+1−vt‖)2≤λmax​(M)​(bmax−δbλmin​(M)+Δe)2,v\_{t+1}^{\top}Mv\_{t+1}\;\leq\;\lambda\_{\max}(M)\,\|v\_{t+1}\|^{2}\;\leq\;\lambda\_{\max}(M)\,\big(\|v\_{t}\|+\|v\_{t+1}-v\_{t}\|\big)^{2}\;\leq\;\lambda\_{\max}(M)\,\Big(\sqrt{\tfrac{b\_{\max}-\delta\_{b}}{\lambda\_{\min}(M)}}+\Delta\_{e}\Big)^{2}, |  |

where we used ‖vt‖2≤(bmax−δb)/λmin​(M)\|v\_{t}\|^{2}\leq(b\_{\max}-\delta\_{b})/\lambda\_{\min}(M), since vt⊤​M​vt≤bmax−δbv\_{t}^{\top}Mv\_{t}\leq b\_{\max}-\delta\_{b}. Therefore a sufficient condition for the tightened NTB,

|  |  |  |
| --- | --- | --- |
|  | vt+1⊤​M​vt+1≤bmax′=ηb​bmax,v\_{t+1}^{\top}Mv\_{t+1}\;\leq\;b\_{\max}^{\prime}=\eta\_{b}b\_{\max}, |  |

is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηb≥ηb⋆:=λmax​(M)bmax​(bmax−δbλmin​(M)+Δe)2.\eta\_{b}\;\geq\;\eta\_{b}^{\star}\;:=\;\frac{\lambda\_{\max}(M)}{b\_{\max}}\,\Big(\sqrt{\tfrac{b\_{\max}-\delta\_{b}}{\lambda\_{\min}(M)}}+\Delta\_{e}\Big)^{2}. |  | (32) |

This is feasible (i.e., ηb⋆<1\eta\_{b}^{\star}<1) provided

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δe<bmaxλmax​(M)−bmax−δbλmin​(M).\Delta\_{e}\;<\;\sqrt{\frac{b\_{\max}}{\lambda\_{\max}(M)}}\;-\;\sqrt{\frac{b\_{\max}-\delta\_{b}}{\lambda\_{\min}(M)}}. |  | (33) |

The right-hand side is positive as soon as δb>0\delta\_{b}>0. Inequality ([33](https://arxiv.org/html/2510.04555v1#A1.E33 "In Step 2: NTB constraint under shrinkage. ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) holds by choosing the local tube small enough (reducing the bound on ‖ut‖\|u\_{t}\| and using the given w¯\bar{w}) so that the state drift bound in ([31](https://arxiv.org/html/2510.04555v1#A1.E31 "In Step 2: NTB constraint under shrinkage. ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) is sufficiently small. Under ([33](https://arxiv.org/html/2510.04555v1#A1.E33 "In Step 2: NTB constraint under shrinkage. ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), pick any ηb∈(ηb⋆,1)\eta\_{b}\in(\eta\_{b}^{\star},1) to satisfy the tightened NTB.

##### Step 3: CBF constraints.

Let us denote the discrete-time CBF map at state xx by

|  |  |  |
| --- | --- | --- |
|  | 𝒞i​(x,u):=hi​(f​(x)+g​(x)​u)−(1−κi​Δ​t)​hi​(x).\mathcal{C}\_{i}(x,u):=h\_{i}(f(x)+g(x)u)-(1-\kappa\_{i}\Delta t)\,h\_{i}(x). |  |

At time tt, strict feasibility with ζ=0\zeta=0 and the margin construction (Assumption [2](https://arxiv.org/html/2510.04555v1#Thmassumption2 "Assumption 2 (Discrete-time CBF constraint with margin). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") in Theorem [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) give

|  |  |  |
| --- | --- | --- |
|  | 𝒞i​(xt,ut)≥εiwithεi≥Li​w¯> 0.\mathcal{C}\_{i}(x\_{t},u\_{t})\;\geq\;\varepsilon\_{i}\quad\text{with}\quad\varepsilon\_{i}\geq L\_{i}\bar{w}\;>\;0. |  |

By local Lipschitzness of hih\_{i}, ff, and gg on 𝒦x×𝒦u\mathcal{K}\_{x}\times\mathcal{K}\_{u}, there exists a constant L𝒞,i>0L\_{\mathcal{C},i}>0 such that

|  |  |  |
| --- | --- | --- |
|  | |𝒞i​(x′,u)−𝒞i​(x,u)|≤L𝒞,i​‖x′−x‖∀(x′,x,u)∈𝒦x×𝒦x×𝒦u.\big|\mathcal{C}\_{i}(x^{\prime},u)-\mathcal{C}\_{i}(x,u)\big|\;\leq\;L\_{\mathcal{C},i}\,\|x^{\prime}-x\|\qquad\forall(x^{\prime},x,u)\in\mathcal{K}\_{x}\times\mathcal{K}\_{x}\times\mathcal{K}\_{u}. |  |

Therefore, using Lemma [8](https://arxiv.org/html/2510.04555v1#Thmlemma8 "Lemma 8 (State drift bound). ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"),

|  |  |  |
| --- | --- | --- |
|  | 𝒞i​(xt+1,ut)≥𝒞i​(xt,ut)−L𝒞,i​‖xt+1−xt‖≥εi−L𝒞,i​(Lx​(‖ut‖+1)+w¯).\mathcal{C}\_{i}(x\_{t+1},u\_{t})\;\geq\;\mathcal{C}\_{i}(x\_{t},u\_{t})-L\_{\mathcal{C},i}\|x\_{t+1}-x\_{t}\|\;\geq\;\varepsilon\_{i}-L\_{\mathcal{C},i}\big(L\_{x}(\|u\_{t}\|+1)+\bar{w}\big). |  |

Define the *CBF residual*

|  |  |  |
| --- | --- | --- |
|  | ρi:=εi−L𝒞,i​(Lx​(‖ut‖+1)+w¯).\rho\_{i}\;:=\;\varepsilon\_{i}-L\_{\mathcal{C},i}\big(L\_{x}(\|u\_{t}\|+1)+\bar{w}\big). |  |

By shrinking the local tube (equivalently, bounding ‖ut‖\|u\_{t}\| more tightly) we can ensure ρi>0\rho\_{i}>0 for all ii, hence

|  |  |  |
| --- | --- | --- |
|  | 𝒞i​(xt+1,ut)≥ρi> 0,\mathcal{C}\_{i}(x\_{t+1},u\_{t})\;\geq\;\rho\_{i}\;>\;0, |  |

i.e., the CBF inequalities remain strictly feasible at t+1t{+}1 for the witness u~t+1=ut\tilde{u}\_{t+1}=u\_{t}.

##### Step 4: sign-consistency gate.

Assume the gate map gcons​(x,u)g\_{\mathrm{cons}}(x,u) is locally Lipschitz in xx uniformly in u∈𝒦uu\in\mathcal{K}\_{u} with modulus LgL\_{g}, and that at time tt the margin

|  |  |  |
| --- | --- | --- |
|  | gcons​(xt,ut)≥δg> 0g\_{\mathrm{cons}}(x\_{t},u\_{t})\;\geq\;\delta\_{g}\;>\;0 |  |

holds (this is typical since the solver returns positive gate scores when the constraint is inactive). Then

|  |  |  |
| --- | --- | --- |
|  | gcons​(xt+1,ut)≥gcons​(xt,ut)−Lg​‖xt+1−xt‖≥δg−Lg​(Lx​(‖ut‖+1)+w¯),g\_{\mathrm{cons}}(x\_{t+1},u\_{t})\;\geq\;g\_{\mathrm{cons}}(x\_{t},u\_{t})-L\_{g}\,\|x\_{t+1}-x\_{t}\|\;\geq\;\delta\_{g}-L\_{g}\big(L\_{x}(\|u\_{t}\|+1)+\bar{w}\big), |  |

which remains nonnegative once the local tube is chosen so that δg>Lg​(Lx​(‖ut‖+1)+w¯)\delta\_{g}>L\_{g}(L\_{x}(\|u\_{t}\|+1)+\bar{w}).

##### Step 5: conclusion.

Collecting the four constraint families:
(i) box and (tightened) rate constraints hold for u~t+1=ut\tilde{u}\_{t+1}=u\_{t};
(ii) the tightened NTB holds provided ([32](https://arxiv.org/html/2510.04555v1#A1.E32 "In Step 2: NTB constraint under shrinkage. ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))–([33](https://arxiv.org/html/2510.04555v1#A1.E33 "In Step 2: NTB constraint under shrinkage. ‣ A.6 Proof of Theorem 5 (feasibility persistence) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) and the choice ηb∈(ηb⋆,1)\eta\_{b}\in(\eta\_{b}^{\star},1);
(iii) the CBF inequalities remain strictly feasible thanks to the residual ρi>0\rho\_{i}>0;
(iv) the gate remains nonnegative by continuity and the margin δg>0\delta\_{g}>0.

Therefore u~t+1\tilde{u}\_{t+1} is a feasible point of the *tightened* constraint set at state xt+1x\_{t+1} with ζ=0\zeta=0. Since all constraints are convex in uu (affine CBF surrogates, ellipsoidal NTB, box/rate, and a convex gate), the feasible set at t+1t{+}1 is nonempty and closed, and thus the QP at t+1t{+}1 is feasible with ζ=0\zeta=0. This establishes *feasibility persistence* under the stated tail guards.
∎

### A.7 Proof of Proposition [2](https://arxiv.org/html/2510.04555v1#Thmproposition2 "Proposition 2 (Gate-induced lower bound). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") (negative-advantage suppression)

###### Lemma 9 (Alignment inequality).

Let v,g∈ℝmv,g\in\mathbb{R}^{m} be unit vectors with angle ∠​(v,g)=θ∈[0,π]\angle(v,g)=\theta\in[0,\pi], i.e., ⟨v,g⟩=cos⁡θ\langle v,g\rangle=\cos\theta. Then for any u∈ℝmu\in\mathbb{R}^{m},

|  |  |  |
| --- | --- | --- |
|  | ⟨u,g⟩≥⟨u,v⟩​cos⁡θ−‖u‖​sin⁡θ.\langle u,g\rangle\;\geq\;\langle u,v\rangle\cos\theta\;-\;\|u\|\,\sin\theta. |  |

Moreover, the bound is tight: equality holds whenever uu lies in the plane spanned by {v,g}\{v,g\} and has a component orthogonal to vv aligned with the orthogonal component of gg.

###### Proof.

Complete vv to an orthonormal basis {v,v⟂(1),…,v⟂(m−1)}\{v,v\_{\perp}^{(1)},\dots,v\_{\perp}^{(m-1)}\} with v⟂(1)v\_{\perp}^{(1)} chosen in the plane span​{v,g}\mathrm{span}\{v,g\} such that

|  |  |  |
| --- | --- | --- |
|  | g=(cos⁡θ)​v+(sin⁡θ)​v⟂(1).g=(\cos\theta)\,v+(\sin\theta)\,v\_{\perp}^{(1)}. |  |

Decompose u=α​v+∑i=1m−1βi​v⟂(i)u=\alpha v+\sum\_{i=1}^{m-1}\beta\_{i}v\_{\perp}^{(i)}. Then

|  |  |  |
| --- | --- | --- |
|  | ⟨u,g⟩=α​cos⁡θ+β1​sin⁡θ.\langle u,g\rangle\;=\;\alpha\cos\theta\;+\;\beta\_{1}\sin\theta. |  |

Using |β1|≤∑i=1m−1βi2≤‖u‖|\beta\_{1}|\leq\sqrt{\sum\_{i=1}^{m-1}\beta\_{i}^{2}}\leq\|u\| and α=⟨u,v⟩\alpha=\langle u,v\rangle, we obtain

|  |  |  |
| --- | --- | --- |
|  | ⟨u,g⟩≥⟨u,v⟩​cos⁡θ−‖u‖​sin⁡θ.\langle u,g\rangle\;\geq\;\langle u,v\rangle\cos\theta\;-\;\|u\|\,\sin\theta. |  |

Tightness: if uu lies in span​{v,v⟂(1)}\mathrm{span}\{v,v\_{\perp}^{(1)}\} and β1=−‖u‖\beta\_{1}=-\|u\| (i.e., the entire orthogonal component of uu is opposite to v⟂(1)v\_{\perp}^{(1)}), the inequality is attained with equality.
∎

###### Proof of Proposition [2](https://arxiv.org/html/2510.04555v1#Thmproposition2 "Proposition 2 (Gate-induced lower bound). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

Fix a state xx and write, for brevity, v:=v​(x)v:=v(x) (the consensus direction of the ensemble signals) and gα:=∇A~π(α)​(x)/‖∇A~π(α)​(x)‖g\_{\alpha}:=\nabla\tilde{A}\_{\pi}^{(\alpha)}(x)/\|\nabla\tilde{A}\_{\pi}^{(\alpha)}(x)\| (the unit CVaR-advantage direction). We proceed in three steps.

##### Step 1: from gate feasibility to a lower bound along vv.

By Assumption [10](https://arxiv.org/html/2510.04555v1#Thmassumption10 "Assumption 10 (Gate alignment and mismatch). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), for all j∈{1,…,J}j\in\{1,\ldots,J\} one has

|  |  |  |
| --- | --- | --- |
|  | ‖∇^​Π(j)​(x)−v‖≤ϵg.\|\widehat{\nabla}\Pi^{(j)}(x)-v\|\;\leq\;\epsilon\_{g}. |  |

For any feasible uu with gcons​(x,u)≥0g\_{\mathrm{cons}}(x,u)\geq 0, we have

|  |  |  |
| --- | --- | --- |
|  | minj⁡⟨u,∇^​Π(j)​(x)⟩≥δadv.\min\_{j}\langle u,\widehat{\nabla}\Pi^{(j)}(x)\rangle\;\geq\;\delta\_{\mathrm{adv}}. |  |

For each jj, write

|  |  |  |
| --- | --- | --- |
|  | ⟨u,v⟩=⟨u,∇^​Π(j)​(x)⟩+⟨u,v−∇^​Π(j)​(x)⟩≥δadv−‖u‖​‖v−∇^​Π(j)​(x)‖≥δadv−‖u‖​ϵg.\langle u,v\rangle\;=\;\langle u,\widehat{\nabla}\Pi^{(j)}(x)\rangle\;+\;\langle u,\,v-\widehat{\nabla}\Pi^{(j)}(x)\rangle\;\geq\;\delta\_{\mathrm{adv}}\;-\;\|u\|\,\|v-\widehat{\nabla}\Pi^{(j)}(x)\|\;\geq\;\delta\_{\mathrm{adv}}\;-\;\|u\|\,\epsilon\_{g}. |  |

Taking the minimum over jj preserves the inequality, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨u,v⟩≥δadv−‖u‖​ϵg.\langle u,v\rangle\;\geq\;\delta\_{\mathrm{adv}}\;-\;\|u\|\,\epsilon\_{g}. |  | (34) |

##### Step 2: project the lower bound from vv onto the CVaR-advantage direction gαg\_{\alpha}.

Assumption [10](https://arxiv.org/html/2510.04555v1#Thmassumption10 "Assumption 10 (Gate alignment and mismatch). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") further states that the angle between vv and gαg\_{\alpha} is bounded: ∠​(v,gα)≤ϵθ\angle(v,g\_{\alpha})\leq\epsilon\_{\theta}. Applying Lemma [9](https://arxiv.org/html/2510.04555v1#Thmlemma9 "Lemma 9 (Alignment inequality). ‣ A.7 Proof of Proposition 2 (negative-advantage suppression) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") with g=gαg=g\_{\alpha} yields

|  |  |  |
| --- | --- | --- |
|  | ⟨u,gα⟩≥⟨u,v⟩​cos⁡ϵθ−‖u‖​sin⁡ϵθ.\langle u,g\_{\alpha}\rangle\;\geq\;\langle u,v\rangle\cos\epsilon\_{\theta}\;-\;\|u\|\sin\epsilon\_{\theta}. |  |

Combining with ([34](https://arxiv.org/html/2510.04555v1#A1.E34 "In Step 1: from gate feasibility to a lower bound along 𝑣. ‣ A.7 Proof of Proposition 2 (negative-advantage suppression) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨u,gα⟩≥(δadv−‖u‖​ϵg)​cos⁡ϵθ−‖u‖​sin⁡ϵθ.\langle u,g\_{\alpha}\rangle\;\geq\;\big(\delta\_{\mathrm{adv}}-\|u\|\,\epsilon\_{g}\big)\cos\epsilon\_{\theta}\;-\;\|u\|\sin\epsilon\_{\theta}. |  | (35) |

##### Step 3: first-order lower bound for the CVaR-advantage and remainder control.

Let Gα​(x):=‖∇A~π(α)​(x)‖G\_{\alpha}(x):=\|\nabla\tilde{A}\_{\pi}^{(\alpha)}(x)\|. A first-order Taylor expansion of the scalar map u↦A~π(α)​(x,u)u\mapsto\tilde{A}\_{\pi}^{(\alpha)}(x,u) at u=0u=0 gives

|  |  |  |
| --- | --- | --- |
|  | A~π(α)​(x,u)=Gα​(x)​⟨u,gα⟩+Rα​(x,u),\tilde{A}\_{\pi}^{(\alpha)}(x,u)\;=\;G\_{\alpha}(x)\,\langle u,g\_{\alpha}\rangle\;+\;R\_{\alpha}(x,u), |  |

where Rα​(x,u)R\_{\alpha}(x,u) is the Taylor remainder. If ∇A~π(α)​(x,⋅)\nabla\tilde{A}\_{\pi}^{(\alpha)}(x,\cdot) is LαL\_{\alpha}-Lipschitz in uu locally (a standard assumption inherited from the bounded/smooth one-step losses and the bounded horizon), then

|  |  |  |
| --- | --- | --- |
|  | |Rα​(x,u)|≤Lα2​‖u‖2for ‖u‖ in a local tube.|R\_{\alpha}(x,u)|\;\leq\;\tfrac{L\_{\alpha}}{2}\,\|u\|^{2}\quad\text{for $\|u\|$ in a local tube.} |  |

Combining with ([35](https://arxiv.org/html/2510.04555v1#A1.E35 "In Step 2: project the lower bound from 𝑣 onto the CVaR-advantage direction 𝑔_𝛼. ‣ A.7 Proof of Proposition 2 (negative-advantage suppression) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) yields the pointwise lower bound

|  |  |  |
| --- | --- | --- |
|  | A~π(α)​(x,u)≥Gα​(x)​[(δadv−‖u‖​ϵg)​cos⁡ϵθ−‖u‖​sin⁡ϵθ]−Lα2​‖u‖2.\tilde{A}\_{\pi}^{(\alpha)}(x,u)\;\geq\;G\_{\alpha}(x)\Big[\big(\delta\_{\mathrm{adv}}-\|u\|\,\epsilon\_{g}\big)\cos\epsilon\_{\theta}-\|u\|\sin\epsilon\_{\theta}\Big]\;-\;\tfrac{L\_{\alpha}}{2}\,\|u\|^{2}. |  |

Taking conditional expectation given xx (which leaves the deterministic right-hand side unchanged if uu is deterministic given xx, or replaces ‖u‖\|u\| by 𝔼​[‖u‖∣x]\mathbb{E}[\|u\|\mid x] in the stochastic case and then uses Jensen/triangle inequalities) gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[A~π(α)​(x,u)∣x]≥−ξ​(ϵg,ϵθ,δadv,‖u‖;Gα,Lα),\mathbb{E}\!\left[\tilde{A}\_{\pi}^{(\alpha)}(x,u)\mid x\right]\;\geq\;-\,\xi(\epsilon\_{g},\epsilon\_{\theta},\delta\_{\mathrm{adv}},\|u\|;G\_{\alpha},L\_{\alpha}), |  |

with the explicit tolerance function

|  |  |  |
| --- | --- | --- |
|  | ξ​(⋅):=(Gα​(x)​[‖u‖​ϵg​cos⁡ϵθ+‖u‖​sin⁡ϵθ−δadv​cos⁡ϵθ]+Lα2​‖u‖2)+,\xi(\cdot)\;:=\;\left(G\_{\alpha}(x)\Big[\|u\|\,\epsilon\_{g}\cos\epsilon\_{\theta}+\|u\|\sin\epsilon\_{\theta}-\delta\_{\mathrm{adv}}\cos\epsilon\_{\theta}\Big]+\tfrac{L\_{\alpha}}{2}\,\|u\|^{2}\right)\_{+}, |  |

where (⋅)+(\cdot)\_{+} denotes positive part. In particular, as (ϵg,ϵθ)→0(\epsilon\_{g},\epsilon\_{\theta})\to 0 and for fixed δadv>0\delta\_{\mathrm{adv}}>0, ξ​(⋅)→(Lα2​‖u‖2−Gα​(x)​δadv)+\xi(\cdot)\to\big(\tfrac{L\_{\alpha}}{2}\|u\|^{2}-G\_{\alpha}(x)\delta\_{\mathrm{adv}}\big)\_{+}, i.e., the gate suppresses negative CVaR-advantage up to the second-order Taylor remainder. For sufficiently small ‖u‖\|u\| or larger δadv\delta\_{\mathrm{adv}}, the negative-advantage region is eliminated.
∎

### Auxiliary notes on constants and domains

All Lipschitz and boundedness constants are understood to hold on a compact subset containing the closed-loop trajectories (guaranteed during training/evaluation by box/rate constraints and statewise CBF conditions). The “O​(T)O(T)” dependence in Lemma [5](https://arxiv.org/html/2510.04555v1#Thmlemma5 "Lemma 5 (Occupancy shift under per-state KL). ‣ A.5 Proof of Theorem 4 (CVaR trust-region improvement) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") can be refined under mixing assumptions but suffices for trust-region purposes. The SNIS bound in Lemma [3](https://arxiv.org/html/2510.04555v1#Thmlemma3 "Lemma 3 (Concentration for SNIS ratios with bounded weights). ‣ A.4 Proof of Theorem 3 (temperature-tilted CVaR concentration) ‣ Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") can be strengthened via empirical Bernstein inequalities or self-normalized martingale bounds; we use a Hoeffding-style presentation for clarity, which already gives the O~​((K​αeff)−1/2)\tilde{O}\!\big((K\alpha\_{\mathrm{eff}})^{-1/2}\big) rate stated in Theorem [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

Cross-references.

* •

  Section [4](https://arxiv.org/html/2510.04555v1#S4 "4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"): statements of Theorems [1](https://arxiv.org/html/2510.04555v1#Thmtheorem1 "Theorem 1 (Robust forward invariance). ‣ Theorem 1 (robust forward invariance of the safety set) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [2](https://arxiv.org/html/2510.04555v1#Thmtheorem2 "Theorem 2 (Donsker–Varadhan bound and per-state KL conservatism). ‣ Theorem 2 (KL–DRO upper bound and conservatism of per-state KL) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [3](https://arxiv.org/html/2510.04555v1#Thmtheorem3 "Theorem 3 (Concentration of the temperature-tilted CVaR estimator). ‣ Theorem 3 (bias/variance and sample complexity of the CVaR estimator) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [4](https://arxiv.org/html/2510.04555v1#Thmtheorem4 "Theorem 4 (CVaR trust-region improvement). ‣ Theorem 4 (trust-region improvement inequality for CVaR with KL limits) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [5](https://arxiv.org/html/2510.04555v1#Thmtheorem5 "Theorem 5 (Persistence via NTB shrinkage and rate tightening). ‣ Theorem 5 (feasibility persistence under tail guards) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and Propositions [1](https://arxiv.org/html/2510.04555v1#Thmproposition1 "Proposition 1 (Shifted projection). ‣ Proposition 1 (minimal-deviation 𝐻-metric projection) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"), [2](https://arxiv.org/html/2510.04555v1#Thmproposition2 "Proposition 2 (Gate-induced lower bound). ‣ Proposition 2 (negative-advantage suppression by sign-consistency) ‣ 4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").
* •

  Appendix C (Reproducibility & Governance): data/seed pairing for CIs; telemetry storage schema; dashboard triggers referenced in Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets").

## Appendix B Implementation Notes and Additional Materials

This appendix complements the main text and the proofs in Appendix [A](https://arxiv.org/html/2510.04555v1#A1 "Appendix A Proofs for Section 4 ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") with implementation and reproducibility details.
We avoid introducing new figures or numeric results; instead, we provide concrete procedures, schemas, and checklists that allow faithful reproduction of the experiments and governance flows referenced in the main paper.

### B.1 Implementation Notes: Market, Execution, and Safety Layer

#### B.1 SSVI calibration (no-arbitrage)

We fit the SSVI surface w​(k,τ)w(k,\tau) (Eq. ([1](https://arxiv.org/html/2510.04555v1#S2.E1 "In 2.1 Arbitrage-Free Volatility Surfaces via SSVI ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets"))) to option mid quotes under static no-arbitrage constraints.

* •

  Objective. Minimize a robust loss
  ℒ​(θ,φ,ρ)=∑(k,τ)ℓ​(σ^imp​(k,τ;θ,φ,ρ)−σimpmkt​(k,τ))\mathcal{L}(\theta,\varphi,\rho)=\sum\_{(k,\tau)}\ell\!\big(\hat{\sigma}\_{\mathrm{imp}}(k,\tau;\theta,\varphi,\rho)-\sigma\_{\mathrm{imp}}^{\mathrm{mkt}}(k,\tau)\big)
  where ℓ\ell is Huber or Tukey; σ^imp\hat{\sigma}\_{\mathrm{imp}} derives from ww.
* •

  Constraints. Enforce Gatheral–Jacquier sufficient conditions across maturities to preclude butterfly/calendar arbitrage [[3](https://arxiv.org/html/2510.04555v1#bib.bib3)]. We implement as bound and inequality constraints in a constrained optimizer (e.g., interior-point).
* •

  Smoothing. Penalize roughness along (k,τ)(k,\tau):
  λk​‖∂k2w‖22+λτ​‖∂τ2w‖22\lambda\_{k}\|\partial\_{k}^{2}w\|\_{2}^{2}+\lambda\_{\tau}\|\partial\_{\tau}^{2}w\|\_{2}^{2} (finite differences); this aids Dupire stability.
* •

  Diagnostics. Reject fits where convexity (in KK) of call prices implied by the surface is violated beyond tolerance.

#### B.2 Dupire local volatility (numerics)

* •

  Call grid. Build a call surface C​(t,K)C(t,K) from SSVI via Black–Scholes inversion and put-call parity; interpolate with a monotone C2C^{2} spline in KK and a C1C^{1} spline in tt.
* •

  Derivatives. Compute ∂tC\partial\_{t}C and ∂K​KC\partial\_{KK}C by finite differences with Tikhonov regularization: minimize
  ‖Dt​C−∂tC‖22+ηt​‖∂t2C‖22\|D\_{t}C-\partial\_{t}C\|\_{2}^{2}+\eta\_{t}\|\partial\_{t}^{2}C\|\_{2}^{2} and analogously for ∂K​KC\partial\_{KK}C to stabilize Eq. ([2](https://arxiv.org/html/2510.04555v1#S2.E2 "In 2.2 Local Volatility via Dupire ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
* •

  Positivity. Enforce ∂K​KC≥ϵK​K>0\partial\_{KK}C\geq\epsilon\_{KK}>0; if violated locally, project to the nearest positive value to avoid singularities in Eq. ([2](https://arxiv.org/html/2510.04555v1#S2.E2 "In 2.2 Local Volatility via Dupire ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).
* •

  Simulator. Evolve StS\_{t} with Euler–Maruyama on a nonuniform time grid refined near expiry; clamp σloc\sigma\_{\mathrm{loc}} to a bounded interval to avoid stiffness.

#### B.3 VIX computation (OTM integral)

* •

  Discretization. Approximate Eq. ([3](https://arxiv.org/html/2510.04555v1#S2.E3 "In 2.3 VIX Leg from Surface-Consistent Variance ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) by midpoint or Simpson quadrature over available strikes; extrapolate tails using power-law decay anchored at the last observed OTM points.
* •

  Parity & OTM selection. Use put-call parity to synthesize missing sides and include only OTM quotes: puts for K<FK<F, calls for K>FK>F.
* •

  Non-negativity. Truncate negative integrand contributions (due to noise) at zero to preserve variance interpretation.

#### B.4 Execution adapter (ABIDES/MockLOB)

* •

  Fills. Submit marketable or limit orders to the LOB; record partial fills, cancellations, and realized slippage.
* •

  Impact. Implement Eq. ([4](https://arxiv.org/html/2510.04555v1#S2.E4 "In 2.4 Execution, Microstructure, and Impact ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")) with a linear temporary component η​ut\eta u\_{t} and a decaying transient kernel G​(j)G(j); ensure no-dynamic-arbitrage conditions [[46](https://arxiv.org/html/2510.04555v1#bib.bib46)].
* •

  Latency. Add fixed or random latency; batch orders to emulate smart routing without venue modeling.

#### B.5 CBF–QP layer (assembly & numerics)

* •

  Linearization. Where hi​(f​(x)+g​(x)​u)h\_{i}(f(x)+g(x)u) is nonlinear in uu, use a first-order expansion around (xt,utnom)(x\_{t},u\_{t}^{\mathrm{nom}}) for the QP and re-solve with warm-start (one SQP step per environment step).
* •

  Scaling. Diagonal-scale the QP (row/col) to improve conditioning; choose HH as a scaled identity or Fisher-like metric from policy covariance.
* •

  Warm-start. Initialize with u=ut−1u=u\_{t-1} and duals from the previous solve; set OSQP tolerances to meet per-step latency budgets.
* •

  Slack policy. Penalize ‖ζ‖1\|\zeta\|\_{1} with large ρ\rho; audit any ζ>0\zeta>0 events (Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

### B.2 Reproducibility & Governance Checklist (referenced as Appendix C)

#### C.1 Environment and determinism

* •

  Record random seeds for Python/NumPy/PyTorch/ABIDES; fix CuDNN determinism flags where applicable.
* •

  Log package versions and OS/hardware details; pin dependency hashes.

#### C.2 Artifact manifest

* •

  Configs: YAML/JSON files for market generator (SSVI/Dupire/VIX), execution, RL hyperparameters, and CBF–QP settings.
* •

  Outputs: per-episode CSV of P&L, per-step telemetry logs (Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")), and summary JSONs for metrics.
* •

  Provenance: Git commit hash and config fingerprint embedded in each artifact.

#### C.3 Paired evaluation protocol

* •

  Use the same scenario seeds and path indices across methods; when legacy runs have different nn, downsample to a common effective nn *per seed*.
* •

  Compute 95%95\% paired bootstrap CIs with stratification by seed (Sec. [5](https://arxiv.org/html/2510.04555v1#S5 "5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

#### C.4 Governance triggers and storage

* •

  Implement the online triggers in Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") as rules bound to telemetry streams with persistent queues.
* •

  Store *Explanation Records* with immutable IDs, timestamps, and hashes; ensure read-only access for internal audit.

### B.3 Statistical Protocols (referenced as Appendix B)

#### B.6 Paired bootstrap for metrics

We use stratified paired bootstrap across seeds. For each bootstrap replicate: sample seeds with replacement, then sample paths (indices) with replacement *within* each seed; compute per-method statistics; record differences. Confidence intervals are empirical quantiles in the main text already outlines a variant for Δ​ES\Delta\mathrm{ES}).

#### B.7 Multiple testing & effect sizes

* •

  Adjust pp-values across metrics by Benjamini–Hochberg (FDR control).
* •

  Report Vargha–Delaney A^12\hat{A}\_{12} for effect sizes; interpret A^12∈[0,1]\hat{A}\_{12}\in[0,1] with 0.50.5 as no effect.

#### B.8 Ratio metrics

For Sharpe/Sortino/Ω\Omega, prefer *paired* computation (same path pairing) and report CIs via bootstrap on the *ratio* directly; avoid delta-method linearization unless moments are well-behaved.

### B.4 Hyperparameters & Search Spaces

We list *recommended ranges* (not the specific values used in any run) to guide replication. These ranges are standard for PPO-style training and convex safety layers; they are *not* new numerical results.

Table 6: Recommended hyperparameter ranges (to be tuned per hardware/time budget).

| Component | Range / Notes |
| --- | --- |
| PPO clip ϵ\epsilon | small to moderate (e.g., [0.05,0.3][0.05,0.3]) |
| KL coeff λKL\lambda\_{\mathrm{KL}} | increase as α\alpha tightens; grid over [10−3,10−1][10^{-3},10^{-1}] |
| Entropy coeff λent\lambda\_{\mathrm{ent}} | decay schedule; start in [10−3,10−2][10^{-3},10^{-2}] |
| IQN quantiles per update KK | increase with smaller α\alpha; e.g., [64,512][64,512] |
| Temperature TT | controller-managed in [Tmin,Tmax][T\_{\min},T\_{\max}] with Tmin>0T\_{\min}>0 |
| Tail-boost γtail\gamma\_{\mathrm{tail}} | controller-managed in [1,γmax][1,\gamma\_{\max}] |
| α\alpha schedule | from ≈0.10\approx 0.10 to target (e.g., 0.0250.025) in stages |
| CBF gains κi\kappa\_{i} | choose for desired contraction; constant or state-dependent |
| QP metric HH | scaled identity or diag of action covariance |
| Rate cap rmaxr\_{\max} | align with execution latency and LOB depth |
| NTB (M,bmax)(M,b\_{\max}) | M≻0M\succ 0; bmaxb\_{\max} shrinks near expiry |
| Sign gate δadv\delta\_{\mathrm{adv}} | small positive threshold; calibrated via telemetry |

### B.5 Safety Telemetry Schema (extended)

We provide a machine-readable schema for *Explanation Records* and stepwise telemetry (human-readable templates are in Sec. [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")). The schema is language-agnostic; below is a JSON-like sketch.

```
Record {
  run_id: string, episode_id: int, step: int, timestamp: iso8601,
  state_hash: string, action_nominal: vector[m], action_safe: vector[m],
  H_norm_deviation: float,
  active_set: array[int], tightest_id: int,
  multipliers: array[float],         // KKT duals if exposed
  rate_util: float, gate_score: float,
  slack_sum: float, solver_status: string, solver_time_ms: float,
  rule_names: array[string],         // human-friendly names for active_set
  rationale_text: string,            // filled from template
  kl_step: float, tail_coverage: float, alpha: float
}
```

### B.6 Failure Modes & Debugging Playbook

##### High variance in CVaR estimate.

Symptoms: oscillatory w^\widehat{w}, noisy gradients, stalled improvements. Actions: widen batch size; increase TT (less tilt); increase γtail\gamma\_{\mathrm{tail}} cautiously; strengthen KL; enable gradient clipping.

##### Frequent QP infeasibility.

Symptoms: positive slack\_sum, solver fallbacks. Actions: relax NTB or box bounds; add expiry-aware shrinkage earlier; reduce rate cap; improve linearization (two SQP inner steps); check scaling.

##### Gate over-blocking.

Symptoms: low pass-rate, missed opportunities. Actions: reduce δadv\delta\_{\mathrm{adv}}; increase ensemble diversity; use moving-average signals; add confidence thresholds.

##### Latency spikes.

Symptoms: P95 solver time breaches. Actions: pre-factor HH; prune inactive constraints; warm-start duals; increase OSQP ADMM iterations budget only when needed.

### B.7 Extended Notation and Acronyms

Table 7: Extended notation and acronyms (complements Table [1](https://arxiv.org/html/2510.04555v1#S2.T1 "Table 1 ‣ 2.8 Notation Summary ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")).

|  |  |
| --- | --- |
| Symbol/Acronym | Description |
| IQN | Implicit Quantile Network (distributional critic) |
| CBF | Control Barrier Function |
| QP | Quadratic Program |
| NTB | No-Trade Band (ellipsoidal exposure tolerance) |
| SNIS | Self-Normalized Importance Sampling |
| EMA | Exponential Moving Average (reference policy) |
| PPO | Proximal Policy Optimization |
| DRO | Distributionally Robust Optimization |
| BH-FDR | Benjamini–Hochberg False Discovery Rate |
| δadv\delta\_{\mathrm{adv}} | Advantage threshold in sign-consistency gate |
| κi\kappa\_{i} | CBF contraction gains |
| ρ\rho | Slack penalty coefficient in QP |

### B.8 Ethical Use and Risk Notices

This research concerns algorithmic decision-making in financial contexts. The safety guarantees discussed in Sec. [4](https://arxiv.org/html/2510.04555v1#S4 "4 Theoretical Results ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") are *operational* (state-wise constraints under feasibility) and do not constitute guarantees of fairness, market integrity, or cybersecurity. Live deployment requires additional controls (surveillance, abuse detection, red-team adversarial tests), appropriate disclosures, and adherence to applicable regulations and firm-specific policies.

Pointers back to the main text.
Appendix [B.1](https://arxiv.org/html/2510.04555v1#A2.SS1 "B.1 Implementation Notes: Market, Execution, and Safety Layer ‣ Appendix B Implementation Notes and Additional Materials ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") supports Sections [2.1](https://arxiv.org/html/2510.04555v1#S2.SS1 "2.1 Arbitrage-Free Volatility Surfaces via SSVI ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets")–[2.4](https://arxiv.org/html/2510.04555v1#S2.SS4 "2.4 Execution, Microstructure, and Impact ‣ 2 Preliminaries & Problem Setting ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and [3.3](https://arxiv.org/html/2510.04555v1#S3.SS3 "3.3 White-Box CBF–QP Safety Layer ‣ 3 Method: Tail-Safe Hedging Framework ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets");
Appendix [B.2](https://arxiv.org/html/2510.04555v1#A2.SS2 "B.2 Reproducibility & Governance Checklist (referenced as Appendix C) ‣ Appendix B Implementation Notes and Additional Materials ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") implements the reproducibility and governance references in Sections [5](https://arxiv.org/html/2510.04555v1#S5 "5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and [6](https://arxiv.org/html/2510.04555v1#S6 "6 Explainability & Governance ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets");
Appendix [B.3](https://arxiv.org/html/2510.04555v1#A2.SS3 "B.3 Statistical Protocols (referenced as Appendix B) ‣ Appendix B Implementation Notes and Additional Materials ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") details the statistical procedures referenced in Section [5](https://arxiv.org/html/2510.04555v1#S5 "5 Experiments in Arbitrage-Free Synthetic Markets ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets");
Appendix [B.4](https://arxiv.org/html/2510.04555v1#A2.SS4 "B.4 Hyperparameters & Search Spaces ‣ Appendix B Implementation Notes and Additional Materials ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") summarizes tunable ranges without adding numerical results;
Appendix [B.5](https://arxiv.org/html/2510.04555v1#A2.SS5 "B.5 Safety Telemetry Schema (extended) ‣ Appendix B Implementation Notes and Additional Materials ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") and [B.6](https://arxiv.org/html/2510.04555v1#A2.SS6 "B.6 Failure Modes & Debugging Playbook ‣ Appendix B Implementation Notes and Additional Materials ‣ Tail-Safe Hedging: Explainable Risk-Sensitive Reinforcement Learning with a White-Box CBF–QP Safety Layer in Arbitrage-Free Markets") provide operational scaffolding for audits and incident response.

## References

* [1]

  Robert Almgren and Neil Chriss.
  Optimal Execution of Portfolio Transactions.
  *Journal of Risk*, 3:5–39, 2001.
* [2]

  Albert S. Kyle.
  Continuous Auctions and Insider Trading.
  *Econometrica*, 53(6):1315–1335, 1985.
* [3]

  Jim Gatheral and Antoine Jacquier.
  Arbitrage-free SVI volatility surfaces.
  *Quantitative Finance*, 14(1):59–71, 2014.
* [4]

  Bruno Dupire.
  Pricing with a Smile.
  *Risk*, 7:18–20, 1994.
* [5]

  Anna Obizhaeva and Jiang Wang.
  Optimal trading strategy and supply/demand dynamics.
  *Journal of Financial Markets*, 16(1):1–32, 2013.
* [6]

  Hans Bühler, Lukas Gonon, Josef Teichmann, and Ben Wood.
  Deep Hedging.
  *Quantitative Finance*, 19(8):1271–1291, 2019.
* [7]

  David Byrd, Maria Hybinette, and Tucker Balch.
  ABIDES: Towards High-Fidelity Multi-Agent Market Simulation.
  In *Proceedings of the 2020 ACM SIGSIM Conference on Principles of Advanced Discrete Simulation (PADS)*, 2020.
* [8]

  David Byrd, Maria Hybinette, and Tucker Balch.
  ABIDES: Towards High-Fidelity Market Simulation for AI Research.
  arXiv:1904.12066, 2019.
* [9]

  Bryan T. Kelly and Dacheng Xiu.
  Financial Machine Learning.
  *Foundations and Trends in Finance*, 13(3–4):205–363, 2023.
  doi:10.1561/0500000064.
* [10]

  Ben Hambly, Xunyu Xu, and Haotian Yang.
  Recent advances in reinforcement learning in finance.
  *Mathematical Finance*, 33(3):437–503, 2023.
* [11]

  Shuo Sun, Rundong Wang, and Bo An.
  Reinforcement Learning for Quantitative Trading: A Survey.
  *ACM Transactions on Intelligent Systems and Technology*, 14(3):1–29, 2023.
* [12]

  Nikolaos Pippas, Çagatay Turkay, and Elliot A. Ludvig.
  The Evolution of Reinforcement Learning in Quantitative Finance: A Survey.
  *ACM Computing Surveys*, 2025.
  Early access. doi:10.1145/3733714.
* [13]

  Marc G. Bellemare, Will Dabney, and Rémi Munos.
  A Distributional Perspective on Reinforcement Learning.
  In *Proceedings of ICML*, 2017.
* [14]

  Will Dabney, Georg Ostrovski, David Silver, and Rémi Munos.
  Implicit Quantile Networks for Distributional Reinforcement Learning.
  In *Proceedings of ICML*, pages 1096–1105, 2018.
* [15]

  John Schulman, Sergey Levine, Philipp Moritz, Michael I. Jordan, and Pieter Abbeel.
  Trust Region Policy Optimization.
  In *Proceedings of ICML*, 2015.
* [16]

  John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
  Proximal Policy Optimization Algorithms.
  arXiv:1707.06347, 2017.
* [17]

  Yinlam Chow and Mohammad Ghavamzadeh.
  Algorithms for CVaR Optimization in MDPs.
  In *NeurIPS*, 2014.
* [18]

  Yinlam Chow, Aviv Tamar, Shie Mannor, and Marco Pavone.
  Risk-Constrained Reinforcement Learning with Percentile Risk Criteria.
  *Journal of Machine Learning Research*, 18(167):1–51, 2018.
* [19]

  Aviv Tamar, Yinlam Chow, Mohammad Ghavamzadeh, and Shie Mannor.
  Policy Gradient for Coherent Risk Measures.
  In *NeurIPS*, 2015.
* [20]

  Alex Ray, Joshua Achiam, and Dario Amodei.
  Benchmarking Safe Exploration in Deep Reinforcement Learning.
  OpenAI Technical Report, 2019.
* [21]

  Jiawei Ji et al.
  Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark.
  In *NeurIPS Datasets and Benchmarks*, 2023.
* [22]

  Weiye Zhao, Tairan He, Rui Chen, Tianhao Wei, and Changliu Liu.
  State-wise Safe Reinforcement Learning: A Survey.
  In *IJCAI*, pages 6882–6890, 2023.
* [23]

  Aaron D. Ames, Xiangru Xu, Jessy W. Grizzle, and Paulo Tabuada.
  Control Barrier Function Based Quadratic Programs for Safety Critical Systems.
  *IEEE Transactions on Automatic Control*, 62(8):3861–3876, 2017.
* [24]

  Aaron D. Ames et al.
  Control Barrier Functions: Theory and Applications.
  arXiv:1903.11199, 2019.
* [25]

  Ayush Garg, Shishir Kolathaya, Ian R. Manchester, Aaron D. Ames, Sertac Karaman, et al.
  Advances in the Theory of Control Barrier Functions.
  *Annual Reviews in Control*, 2024.
* [26]

  Qinlin Ma et al.
  Differentiable Control Barrier Functions for Learning of Safe Robot Control.
  In *European Control Conference (ECC)*, 2022.
* [27]

  Zengyi Yang, Shishir Kolathaya, and Aaron D. Ames.
  Differentiable Safe Controller Design through Control Barrier Functions.
  *IEEE Control Systems Letters*, 6:1024–1029, 2022.
* [28]

  Wenceslao Shaw-Cortez and Dimos V. Dimarogonas.
  Designing Performance-Critical Controllers with Control Barrier Functions.
  arXiv:2208.02319, 2022.
* [29]

  Jason J. Choi, Donggun Lee, Koushil Sreenath, Claire J. Tomlin, and Sylvia L. Herbert.
  Robust Control Barrier–Value Functions for Safety-Critical Control.
  arXiv:2107.01188, 2021.
* [30]

  Miodrag Jankovic.
  Robust Control Barrier Functions for Constrained Control of Nonlinear Systems.
  *Automatica*, 96:359–367, 2018.
* [31]

  Xiangru Xu, Paulo Tabuada, Jessy W. Grizzle, and Aaron D. Ames.
  Robustness of Control Barrier Functions for Safety Critical Control.
  *IFAC-PapersOnLine*, 48(27):54–61, 2015.
* [32]

  Yujie Wang and Xiangru Xu.
  Disturbance-Observer-based Robust Control Barrier Functions.
  Technical report, 2024.
  URL: <https://xu.me.wisc.edu/wp-content/uploads/sites/1196/2024/04/Disturbance-Observer-based-Robust-Control-Barrier-Functions.pdf>.
* [33]

  Aviral Kumar, Aurick Zhou, George Tucker, and Sergey Levine.
  Conservative Q-Learning for Offline Reinforcement Learning.
  In *NeurIPS*, 2020.
* [34]

  Lerrel Pinto, James Davidson, Rahul Sukthankar, and Abhinav Gupta.
  Robust Adversarial Reinforcement Learning.
  In *Proceedings of ICML*, 2017.
* [35]

  Ce Lu, Hao Wang, and Lin Chen.
  On Distributionally Robust Reinforcement Learning with Total Variation Distance.
  In *NeurIPS*, 2024.
* [36]

  Karthik Sundhar Ramesh and Sanjiban Choudhury.
  Distributionally Robust Model-Based Reinforcement Learning.
  In *Proceedings of the 41st International Conference on Machine Learning (ICML)*, 2024.
* [37]

  Pu Shi, Chris Russell, Pietro Lió, and Dmitry Kazhdan.
  Worst-Case Performance and Fairness in Offline Reinforcement Learning.
  *Journal of Machine Learning Research*, 25(151):1–61, 2024.
* [38]

  Shuo Liu, Yingying Ma, Pan Li, Liwei Wang, and Zhi-Hua Zhou.
  Learning Distributionally Robust Linear Mixture MDPs.
  arXiv:2505.18044, 2025.
* [39]

  David Byrd et al.
  ABIDES-Gym: Gym Environments for Multi-Agent Discrete Event Simulation and Application to Financial Markets.
  arXiv:2110.14771, 2021.
* [40]

  Selim Amrouni, Aymeric Moulin, Jared Vann, Svitlana Vyetrenko, Tucker Balch, and Manuela Veloso.
  ABIDES-Gym: Gym Environments for Multi-Agent Discrete Event Simulation and Application to Financial Markets.
  In *Proceedings of the Second ACM International Conference on AI in Finance (ICAIF)*, 2021.
* [41]

  Kresimir Demeterfi, Emanuel Derman, Michael Kamal, and Joseph Zou.
  A Guide to Volatility and Variance Swaps.
  Goldman Sachs Quantitative Strategies Research, Technical Report, 1999.
* [42]

  Cboe Global Markets.
  White Paper: The Cboe Volatility Index (VIX®).
  Cboe, 2019.
  URL: <https://www.cboe.com/tradable_products/vix/>.
* [43]

  R. Tyrrell Rockafellar and Stanislav Uryasev.
  Optimization of Conditional Value-at-Risk.
  *Journal of Risk*, 2(3):21–41, 2000.
* [44]

  Carlo Acerbi and Dirk Tasche.
  On the coherence of Expected Shortfall.
  *Journal of Banking & Finance*, 26(7):1487–1503, 2002.
* [45]

  Solomon Kullback and Richard A. Leibler.
  On Information and Sufficiency.
  *The Annals of Mathematical Statistics*, 22(1):79–86, 1951.
* [46]

  Jim Gatheral.
  No-dynamic-arbitrage and market impact.
  *Quantitative Finance*, 10(7):749–759, 2010.
* [47]

  John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel.
  High-Dimensional Continuous Control Using Generalized Advantage Estimation.
  In *Proceedings of the International Conference on Learning Representations (ICLR)*, 2016.
* [48]

  Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel.
  Constrained Policy Optimization.
  In *Proceedings of the 34th International Conference on Machine Learning (ICML)*, pages 22–31, 2017.
* [49]

  Stephen Boyd and Lieven Vandenberghe.
  *Convex Optimization*.
  Cambridge University Press, 2004.
* [50]

  Art B. Owen.
  *Monte Carlo Theory, Methods and Examples*.
  Stanford University, 2013. Available online.
* [51]

  Karl J. Åström and Tore Hägglund.
  *PID Controllers: Theory, Design, and Tuning*.
  Instrument Society of America, 1995.
* [52]

  Bartolomeo Stellato, Goran Banjac, Paul Goulart, Alberto Bemporad, and Stephen Boyd.
  OSQP: An Operator Splitting Solver for Quadratic Programs.
  *Mathematical Programming Computation*, 12(4):637–672, 2020.
* [53]

  Richard S. Sutton and Andrew G. Barto.
  *Reinforcement Learning: An Introduction (2nd Edition)*.
  MIT Press, 2018.
* [54]

  Monroe D. Donsker and S. R. Srinivasa Varadhan.
  Asymptotic Evaluation of Certain Markov Process Expectations for Large Time, I.
  *Communications on Pure and Applied Mathematics*, 28(1):1–47, 1975.
* [55]

  Imre Csiszár and János Körner.
  *Information Theory: Coding Theorems for Discrete Memoryless Systems*.
  Cambridge University Press, Second edition, 2011.
* [56]

  Hongseok Namkoong and John C. Duchi.
  Stochastic Gradient Methods for Distributionally Robust Optimization with ff-Divergences.
  In *NeurIPS*, 2017.
* [57]

  Sham Kakade and John Langford.
  Approximately Optimal Approximate Reinforcement Learning.
  In *Proceedings of the 19th International Conference on Machine Learning (ICML)*, 2002.
* [58]

  Bradley Efron.
  Bootstrap Methods: Another Look at the Jackknife.
  *The Annals of Statistics*, 7(1):1–26, 1979.
* [59]

  A. C. Davison and D. V. Hinkley.
  *Bootstrap Methods and their Application*.
  Cambridge University Press, 1997.
* [60]

  Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger.
  Deep Reinforcement Learning that Matters.
  In *Proceedings of the AAAI Conference on Artificial Intelligence*, 2018.
* [61]

  William F. Sharpe.
  The Sharpe Ratio.
  *The Journal of Portfolio Management*, 21(1):49–58, 1994.
* [62]

  Frank A. Sortino and Lee N. Price.
  Performance Measurement in a Downside Risk Framework.
  *Journal of Investing*, 3(3):59–64, 1994.
* [63]

  Con Keating and William F. Shadwick.
  A Universal Performance Measure.
  Working Paper, The Finance Development Centre, 2002.
* [64]

  Yoav Benjamini and Yosef Hochberg.
  Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing.
  *Journal of the Royal Statistical Society: Series B (Methodological)*, 57(1):289–300, 1995.
* [65]

  András Vargha and Harold D. Delaney.
  A Critique and Improvement of the CL Common Language Effect Size Statistics of McGraw and Wong.
  *Journal of Educational and Behavioral Statistics*, 25(2):101–132, 2000.
* [66]

  Board of Governors of the Federal Reserve System.
  SR 11-7: Guidance on Model Risk Management.
  2011.
  URL: <https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm>.
* [67]

  Basel Committee on Banking Supervision.
  Principles for effective risk data aggregation and risk reporting.
  January 2013.
* [68]

  National Institute of Standards and Technology.
  Artificial Intelligence Risk Management Framework (AI RMF 1.0).
  NIST AI 100-1, 2023.
* [69]

  Javier García and Fernando Fernández.
  A Comprehensive Survey on Safe Reinforcement Learning.
  *Journal of Machine Learning Research*, 16(1):1437–1480, 2015.
* [70]

  Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Kámán, Jan Kretínský, Scott Niekum, and Ufuk Topcu.
  Safe Reinforcement Learning via Shielding.
  In *AAAI Conference on Artificial Intelligence*, 2018.
* [71]

  Gal Dalal, Elad Gilboa, Shie Mannor, and Nahum Shimkin.
  Safe Exploration in Continuous Action Spaces.
  In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, 2018.
* [72]

  Brandon Amos and J. Zico Kolter.
  OptNet: Differentiable Optimization as a Layer in Neural Networks.
  In *Proceedings of the 34th International Conference on Machine Learning (ICML)*, 2017.
* [73]

  Akshay Agrawal, Brandon Amos, Shane Barratt, Stephen Boyd, Steven Diamond, and J. Zico Kolter.
  Differentiable Convex Optimization Layers.
  In *Advances in Neural Information Processing Systems (NeurIPS)*, 2019.
* [74]

  Garud N. Iyengar.
  Robust Dynamic Programming.
  *Mathematics of Operations Research*, 30(2):257–280, 2005.
* [75]

  Arnab Nilim and Laurent El Ghaoui.
  Robust Control of Markov Decision Processes with Uncertain Transition Matrices.
  *Operations Research*, 53(5):780–798, 2005.
* [76]

  Esther Derman, Huan Xu, and Shie Mannor.
  Distributionally Robust Policy Evaluation and Optimization.
  In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, 2018.
* [77]

  Álvaro Cartea, Sebastian Jaimungal, and José Penalva.
  *Algorithmic and High-Frequency Trading*.
  Cambridge University Press, 2015.
* [78]

  Finale Doshi-Velez and Been Kim.
  Towards a Rigorous Science of Interpretable Machine Learning.
  arXiv:1702.08608, 2017.
* [79]

  Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pedreschi.
  A Survey of Methods for Explaining Black Box Models.
  *ACM Computing Surveys*, 51(5):93, 2018.
* [80]

  Cynthia Rudin.
  Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead.
  *Nature Machine Intelligence*, 1(5):206–215, 2019.