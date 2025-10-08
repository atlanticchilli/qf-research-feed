---
authors:
- Jian'an Zhang
doc_id: arxiv:2510.04569v1
family_id: arxiv:2510.04569
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A
  Constrained RL and Stochastic Control Bridge'
url_abs: http://arxiv.org/abs/2510.04569v1
url_html: https://arxiv.org/html/2510.04569v1
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

We formulate option market making as a *constrained, risk-sensitive* stochastic control problem in which the policy must jointly optimize trading revenues and maintain an *arbitrage-free, smooth* implied-volatility (IV) surface. Concretely, a fully differentiable eSSVI layer is embedded *inside* the learning loop, enforcing static no-arbitrage (butterfly/calendar) through smoothed lattice penalties while the agent controls half-spreads, delta-hedging intensity, and structured surface deformations (state-dependent ρ\rho-shift and ψ\psi-scale). Executions are *intensity-driven* and respond monotonically to spreads and relative mispricing; tail risk is shaped with a differentiable *CVaR* objective via the Rockafellar–Uryasev program. Theoretically, we prove: (i) grid-consistency and convergence rates for butterfly/calendar surrogates; (ii) a primal–dual grounding of a learnable *dual* action that acts as a state-dependent Lagrange multiplier; (iii) differentiable CVaR estimators with mixed pathwise/likelihood-ratio gradients and epi-convergence to the nonsmooth objective; (iv) an eSSVI wing-growth bound consistent with Lee’s moment constraints; and (v) policy-gradient validity under smooth surrogates. In simulation (Heston fallback; ABIDES-ready), the agent achieves *positive adjusted P&L* in most intraday segments while keeping calendar violations at numerical zero and butterfly violations at the numerical floor; ex-post tails remain realistic and tunable through the CVaR weight. The five control heads admit clear economic semantics and analytic sensitivities, yielding a *white-box* reinforcement learner that unifies pricing consistency and execution control in a reproducible pipeline.

*K*eywords Option market making; implied volatility surface; arbitrage-free modeling; eSSVI; SVI; risk-sensitive reinforcement learning; constrained MDP (CMDP); policy gradient; Proximal Policy Optimization (PPO); primal–dual optimization; intensity-based executions; Hawkes/point processes; delta/vega/vanna; stochastic control; agent-based simulation; neural-SDE; deep hedging

## 1 Introduction

Market making in options traditionally sits at the intersection of three disciplines: (i) microstructure-aware control of quotes and inventory, (ii) arbitrage-consistent construction of implied-volatility (IV) surfaces, and (iii) risk management under severe tail events. Classical models formalize quoting and inventory control as stochastic control problems and illuminate structural trade-offs between spread revenue and inventory risk [[1](https://arxiv.org/html/2510.04569v1#bib.bib1), [2](https://arxiv.org/html/2510.04569v1#bib.bib2), [3](https://arxiv.org/html/2510.04569v1#bib.bib3), [4](https://arxiv.org/html/2510.04569v1#bib.bib4), [5](https://arxiv.org/html/2510.04569v1#bib.bib5), [6](https://arxiv.org/html/2510.04569v1#bib.bib6)]. Concurrently, the volatility-modeling literature has developed parametric families (SVI/SSVI/eSSVI) and general principles that enforce static no-arbitrage across strikes and maturities [[23](https://arxiv.org/html/2510.04569v1#bib.bib23), [20](https://arxiv.org/html/2510.04569v1#bib.bib20), [14](https://arxiv.org/html/2510.04569v1#bib.bib14), [15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16), [17](https://arxiv.org/html/2510.04569v1#bib.bib17), [18](https://arxiv.org/html/2510.04569v1#bib.bib18), [19](https://arxiv.org/html/2510.04569v1#bib.bib19)]. Yet, in both academic studies and practice, these pieces are often optimized in isolation: first calibrate a no-arbitrage surface, and only then design execution/hedging policies. This separation hampers interpretability and can mask failure modes when pricing consistency interacts with execution frictions and downside risk.

#### Problem.

We ask whether one can *unify* pricing consistency and decision-making by embedding an *arbitrage-free, fully differentiable* IV surface [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16)] *inside* an agent-based market-making loop, while directly controlling tail risk via coherent risk measures such as CVaR [[29](https://arxiv.org/html/2510.04569v1#bib.bib29), [30](https://arxiv.org/html/2510.04569v1#bib.bib30), [32](https://arxiv.org/html/2510.04569v1#bib.bib32), [33](https://arxiv.org/html/2510.04569v1#bib.bib33), [34](https://arxiv.org/html/2510.04569v1#bib.bib34)]. This brings stochastic control and modern reinforcement learning (RL) into a single, risk-sensitive framework where the policy co-evolves quotes, hedges, and surface deformations subject to no-arbitrage and smoothness constraints.
Concretely, let the system state xt=(St,LOBt,IVt,Qt,…)x\_{t}=(S\_{t},\,\text{LOB}\_{t},\,\text{IV}\_{t},\,Q\_{t},\ldots) aggregate mid-price, order-book features, a finite-dimensional IV-surface parameterization, and inventory; an action ata\_{t} selects half-spreads δt​(k,T)\delta\_{t}(k,T), hedge intensities hth\_{t}, and low-dimensional surface adjustments Δ​θt\Delta\theta\_{t}. The maker receives marked-to-market revenue from fills, pays execution and inventory costs, and is penalized for *(i)* shape violations (butterfly/calendar), *(ii)* lack of smoothness, and *(iii)* tail losses via CVaRq\mathrm{CVaR}\_{q} of the PnL distribution. The core question is whether such a loop can *learn* to place prices and size trades that are *internally consistent* (no static arbitrage), *microstructure-aware*, and *tail-safe*.

#### Why now?

Two developments make this integration timely. First, high-fidelity agent-based simulators and microstructure datasets enable reproducible experimentation with event-level feedbacks—order flow, fills, and price impact—without relying on fragile stylized approximations [[11](https://arxiv.org/html/2510.04569v1#bib.bib11), [10](https://arxiv.org/html/2510.04569v1#bib.bib10), [8](https://arxiv.org/html/2510.04569v1#bib.bib8), [9](https://arxiv.org/html/2510.04569v1#bib.bib9), [37](https://arxiv.org/html/2510.04569v1#bib.bib37), [38](https://arxiv.org/html/2510.04569v1#bib.bib38)]. These environments support point-process order-flow models and execution rules that determine which quotes actually trade and at what slippage. Second, the IV-surface literature now provides *constructive* characterizations of butterfly/calendar no-arbitrage and robust calibration procedures for SVI/SSVI/eSSVI [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16), [39](https://arxiv.org/html/2510.04569v1#bib.bib39), [19](https://arxiv.org/html/2510.04569v1#bib.bib19), [17](https://arxiv.org/html/2510.04569v1#bib.bib17), [18](https://arxiv.org/html/2510.04569v1#bib.bib18)]. The eSSVI map is *amenable to differentiation*, allowing gradient-based learning while preserving static no-arbitrage by design. In parallel, risk-sensitive RL has matured beyond heuristic penalties, offering principled algorithms and sample-complexity guarantees for CVaR-type objectives [[32](https://arxiv.org/html/2510.04569v1#bib.bib32), [33](https://arxiv.org/html/2510.04569v1#bib.bib33), [34](https://arxiv.org/html/2510.04569v1#bib.bib34), [35](https://arxiv.org/html/2510.04569v1#bib.bib35), [36](https://arxiv.org/html/2510.04569v1#bib.bib36)]. These advances sit alongside “deep hedging” and arbitrage-free neural-SDE market models that make end-to-end learning compatible with financial constraints [[25](https://arxiv.org/html/2510.04569v1#bib.bib25), [27](https://arxiv.org/html/2510.04569v1#bib.bib27), [26](https://arxiv.org/html/2510.04569v1#bib.bib26), [28](https://arxiv.org/html/2510.04569v1#bib.bib28)]. The confluence of (i) differentiable, arbitrage-free surfaces, (ii) event-level simulators, and (iii) risk-sensitive policy optimization enables a unified treatment of pricing and control.

#### Our approach in brief.

We formulate option market making as a *risk-sensitive stochastic control* problem. The *state* includes path features (returns, realized variance), surface statistics (eSSVI parameters, curvature), and microstructure variables (queue sizes, imbalance). The *actions* jointly choose half-spreads δt​(k,T)\delta\_{t}(k,T), hedge intensities hth\_{t}, and low-rank eSSVI parameter perturbations Δ​θt\Delta\theta\_{t} constrained to the no-arbitrage manifold. The *reward* is

|  |  |  |
| --- | --- | --- |
|  | Rt=spread revenue−impact/fees−λQ​‖Qt+1‖2−λarb​Φarb​(θt+1)⏟butterfly & calendarsurrogatesR\_{t}\;=\;\text{spread revenue}-\text{impact/fees}-\lambda\_{Q}\|Q\_{t+1}\|^{2}-\lambda\_{\text{arb}}\underbrace{\Phi\_{\text{arb}}(\theta\_{t+1})}\_{\begin{subarray}{c}\text{butterfly \& calendar}\\ \text{surrogates}\end{subarray}} |  |

and the *training objective* maximizes expected cumulative reward subject to a CVaR regularizer on episodic PnL:

|  |  |  |
| --- | --- | --- |
|  | maxπ⁡𝔼π​[∑tγt​Rt]−λCVaR⋅CVaRq​(−PnL​(τ)).\max\_{\pi}\;\;\mathbb{E}\_{\pi}\!\Big[\sum\_{t}\gamma^{t}R\_{t}\Big]\;-\;\lambda\_{\mathrm{CVaR}}\cdot\mathrm{CVaR}\_{q}\!\big(-\mathrm{PnL}(\tau)\big). |  |

A differentiable eSSVI layer [[15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16)] produces internally consistent quotes and surfaces while serving gradients to the policy; executions are intensity-driven and coupled to mispricing and spreads, consistent with point-process order flow [[12](https://arxiv.org/html/2510.04569v1#bib.bib12), [13](https://arxiv.org/html/2510.04569v1#bib.bib13)]. We combine a short *supervised warm start* (matching stylized optimal quotes/inventory targets) with PPO [[44](https://arxiv.org/html/2510.04569v1#bib.bib44), [45](https://arxiv.org/html/2510.04569v1#bib.bib45)], annealing structural weights so the agent first discovers revenue, then tightens arbitrage and tail discipline.

#### Making arbitrage constraints differentiable and useful.

A central design choice is to transform hard butterfly/calendar conditions into smooth penalties usable by policy gradients. For eSSVI parameters θ=(ρ,η,λ,…)\theta=(\rho,\eta,\lambda,\ldots), we define surrogate functionals Φbut​(θ)\Phi\_{\text{but}}(\theta) and Φcal​(θ)\Phi\_{\text{cal}}(\theta) that are (i) zero on the admissible region characterized in [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16)], (ii) positive and *Lipschitz-smooth* elsewhere, and (iii) *directionally aligned* with the exact Karush–Kuhn–Tucker multipliers of the constrained calibration problem. This provides informative gradients that penalize nascent arbitrage while permitting small, structure-preserving deformations. The penalties are coupled to *shape priors* (bounded skew/smile curvature, term-structure smoothness) derived from [[20](https://arxiv.org/html/2510.04569v1#bib.bib20), [19](https://arxiv.org/html/2510.04569v1#bib.bib19), [18](https://arxiv.org/html/2510.04569v1#bib.bib18), [17](https://arxiv.org/html/2510.04569v1#bib.bib17)].

#### Microstructure-consistent executions.

We model arrivals on each (k,T)(k,T) bucket as conditionally independent point processes with intensities

|  |  |  |
| --- | --- | --- |
|  | λt±​(k,T)=Λ​(±Δ​Pt​(k,T)⏟maker price – reference,δt​(k,T),imbalancet,queuet),\lambda\_{t}^{\pm}(k,T)\;=\;\Lambda\!\Big(\pm\underbrace{\Delta P\_{t}(k,T)}\_{\text{maker price -- reference}},\,\delta\_{t}(k,T),\,\text{imbalance}\_{t},\,\text{queue}\_{t}\Big), |  |

where Λ\Lambda is decreasing in adverse price terms and increasing in offered liquidity, consistent with [[13](https://arxiv.org/html/2510.04569v1#bib.bib13), [8](https://arxiv.org/html/2510.04569v1#bib.bib8)]. Impact enters both through (i) temporary execution costs and (ii) state transitions that modify future intensities via queue depletion and imbalance—a channel emphasized by [[6](https://arxiv.org/html/2510.04569v1#bib.bib6)]. This endogenous feedback loop makes spread-setting and inventory control *joint*, and highlights the benefit of embedding pricing consistency *inside* the policy so that quoted surfaces remain arbitrage-free even when inventories or impact shocks push quotes to extremes.

#### Risk-sensitive learning with financial semantics.

We implement CVaR through a convex auxiliary variable zz and sample-based shortfall losses, following [[29](https://arxiv.org/html/2510.04569v1#bib.bib29), [30](https://arxiv.org/html/2510.04569v1#bib.bib30)] and the policy-gradient extensions in [[32](https://arxiv.org/html/2510.04569v1#bib.bib32), [33](https://arxiv.org/html/2510.04569v1#bib.bib33), [34](https://arxiv.org/html/2510.04569v1#bib.bib34)]. The training objective becomes

|  |  |  |
| --- | --- | --- |
|  | minz⁡z+1(1−q)​𝔼​[(−PnL​(τ)−z)+]−1λCVaR​𝔼​[∑tγt​Rt],\min\_{z}\;\;z+\frac{1}{(1-q)}\,\mathbb{E}\big[(-\mathrm{PnL}(\tau)-z)\_{+}\big]\;-\;\frac{1}{\lambda\_{\mathrm{CVaR}}}\,\mathbb{E}\!\Big[\sum\_{t}\gamma^{t}R\_{t}\Big], |  |

for which we derive a variance-reduced gradient estimator using generalized advantage estimation [[45](https://arxiv.org/html/2510.04569v1#bib.bib45)] and stratified tail sampling. Financially, CVaR focuses learning on the regimes that matter (illiquidity, gap risk), aligning statistical training with risk oversight.

#### Diagnostics and *white-box* explainability.

To support audit and debugging, the agent logs: (i) active arbitrage penalties and their gradients, (ii) inventory and exposure trajectories, (iii) per-bucket fill intensities vs. realized fills, and (iv) a decomposition of episodic PnL into spread, impact, carry, and penalty rebates. These ledgers make it possible to answer *why* a specific surface deformation or spread change occurred (e.g., “calendar penalty rising at T=2T=2M forced upward adjustment of long-dated variance”).

#### Contributions.

1. 1.

   A two-way bridge between stochastic control and deep RL. We integrate an arbitrage-free eSSVI surface into the control loop, so classical no-arbitrage structure *constrains* learning while learned controls *co-evolve* the surface under microstructure frictions [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16), [13](https://arxiv.org/html/2510.04569v1#bib.bib13), [8](https://arxiv.org/html/2510.04569v1#bib.bib8)]. The surface acts both as pricing engine and differentiable prior, tightening exploration to financially admissible regions.
2. 2.

   Risk-sensitive reinforcement learning with financial semantics. Our training objective explicitly includes CVaR alongside arbitrage and smoothness, linking Whittle/Howard-style risk-sensitive control to modern policy gradients [[40](https://arxiv.org/html/2510.04569v1#bib.bib40), [29](https://arxiv.org/html/2510.04569v1#bib.bib29), [32](https://arxiv.org/html/2510.04569v1#bib.bib32), [33](https://arxiv.org/html/2510.04569v1#bib.bib33), [34](https://arxiv.org/html/2510.04569v1#bib.bib34)]. We provide tail-focused estimators compatible with event-level simulators.
3. 3.

   Mathematical guarantees inside the loop (to be proved in Section [6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). We state and prove: (*i*) differentiability and Lipschitz properties of our butterfly/calendar surrogate penalties over eSSVI parameters; (*ii*) existence of optimal stationary policies for the regularized risk-sensitive objective under compactness and linear-growth conditions; (*iii*) a calibration-stability proposition showing that small dual-penalty perturbations preserve no-arbitrage in the eSSVI map; and (*iv*) a CVaR policy-gradient identity with variance-reduced Monte Carlo estimators.
4. 4.

   Reproducible agent-based evaluation. We prioritize ABIDES-style sources with a calibrated Heston fallback [[37](https://arxiv.org/html/2510.04569v1#bib.bib37), [24](https://arxiv.org/html/2510.04569v1#bib.bib24)], releasing logs, figures, and scripts for the full pipeline.111We intentionally defer live-data backtests and focus on a simulation-first study consistent with recent reproducibility trends in market microstructure [[37](https://arxiv.org/html/2510.04569v1#bib.bib37), [38](https://arxiv.org/html/2510.04569v1#bib.bib38), [8](https://arxiv.org/html/2510.04569v1#bib.bib8)].

#### Positioning vis-à-vis recent 2024–2025 developments.

Recent theory demonstrates strategic interactions between brokers, informed traders, and competing market makers [[41](https://arxiv.org/html/2510.04569v1#bib.bib41), [42](https://arxiv.org/html/2510.04569v1#bib.bib42), [43](https://arxiv.org/html/2510.04569v1#bib.bib43)]. Our framework is complementary: rather than modeling competition or information per se, we guarantee *internal pricing consistency* of the maker’s surface during learning, which is orthogonal to—and potentially composable with—competitive or informed-flow models. On the modeling side, arbitrage-free neural-SDEs and deep-hedging pipelines inform our differentiable design and stress-testing tools [[27](https://arxiv.org/html/2510.04569v1#bib.bib27), [26](https://arxiv.org/html/2510.04569v1#bib.bib26), [25](https://arxiv.org/html/2510.04569v1#bib.bib25)]. On the control side, risk-sensitive RL with CVaR has progressed to provable and scalable algorithms [[34](https://arxiv.org/html/2510.04569v1#bib.bib34), [35](https://arxiv.org/html/2510.04569v1#bib.bib35), [36](https://arxiv.org/html/2510.04569v1#bib.bib36)]; our contribution is to *instantiate* those principles in a financially structured environment where no-arbitrage is enforced *inside* the objective.

#### Roadmap and theoretical content.

Section [2](https://arxiv.org/html/2510.04569v1#S2 "2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") establishes notation and background, reviews arbitrage-free eSSVI parameterizations, static no-arbitrage conditions, and the risk-sensitive CMDP formulation.
Section [3](https://arxiv.org/html/2510.04569v1#S3 "3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") formulates the integrated model—combining the eSSVI surface, intensity-based execution, delta-hedging, and CVaR-shaped reward—within a differentiable, arbitrage-consistent control loop.
Section [4](https://arxiv.org/html/2510.04569v1#S4 "4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") details the two-stage learning procedure (*warm-start + PPO*) and interprets the state-dependent *dual* head as a learnable Lagrange multiplier.
Section [5](https://arxiv.org/html/2510.04569v1#S5 "5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") analyzes the interpretability of controls, deriving analytic sensitivities of quotes, intensities, and Greeks with respect to each action dimension.
Section [6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") presents the complete set of theoretical results—Theorems T1–T6 and Propositions P7–P8—establishing lattice-consistency, primal–dual structure, differentiable CVaR estimation, wing-growth bounds, policy-gradient validity, and interpretability guarantees.
Sections [8](https://arxiv.org/html/2510.04569v1#S8 "8 Discussion ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[9](https://arxiv.org/html/2510.04569v1#S9 "9 Conclusion ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") discuss limitations, extensions, and broader implications for robust and interpretable reinforcement learning in quantitative markets.

Notation. We use StS\_{t} for the mid price, k=log⁡(K/S)k=\log(K/S) for log-moneyness, TT for maturity, w​(k,T)w(k,T) for total variance, σ​(k,T)=w/T\sigma(k,T)=\sqrt{w/T} for IV, and standard Black–Scholes notation [[21](https://arxiv.org/html/2510.04569v1#bib.bib21), [22](https://arxiv.org/html/2510.04569v1#bib.bib22)]. CVaR at tail level qq is denoted CVaRq\mathrm{CVaR}\_{q} [[29](https://arxiv.org/html/2510.04569v1#bib.bib29)].

## 2 Preliminaries & Problem Setup

This section fixes notation, recalls an arbitrage-free extended SSVI (eSSVI) parameterization for implied-volatility (IV) surfaces, formalizes static no-arbitrage (butterfly and calendar), and introduces the risk measure (cvar) and our constrained MDP (cmdp) formulation.

### 2.1 Notation and timing conventions

We consider a single underlying with mid price process (St)t≥0(S\_{t})\_{t\geq 0} observed on an intraday grid t=0,1,…,Tdayt=0,1,\dots,T\_{\text{day}}. Let K>0K>0 denote strike and

|  |  |  |
| --- | --- | --- |
|  | k≡log⁡(KSt)(log-moneyness).k\equiv\log\!\left(\frac{K}{S\_{t}}\right)\quad\text{(log-moneyness).} |  |

We work with maturities T∈𝒯={Tm}m=1MT\in\mathcal{T}=\{T\_{m}\}\_{m=1}^{M}. Total variance is w​(k,T)w(k,T) and the Black–Scholes IV is σ​(k,T)=w​(k,T)/T\sigma(k,T)=\sqrt{w(k,T)/T}. We use CBS​(S,K,T,σ)C^{\mathrm{BS}}(S,K,T,\sigma) for the Black–Scholes call price and the standard Greeks. Discrete grids for moneyness and maturities are

|  |  |  |
| --- | --- | --- |
|  | 𝒦={kj}j=1J,𝒯={Tm}m=1M.\mathcal{K}=\{k\_{j}\}\_{j=1}^{J},\qquad\mathcal{T}=\{T\_{m}\}\_{m=1}^{M}. |  |

Throughout, σ​(⋅)\sigma(\cdot) denotes the logistic sigmoid and ReLU​(x)=max⁡{x,0}\mathrm{ReLU}(x)=\max\{x,0\} the hinge map (smoothed in practice).

### 2.2 Arbitrage-free eSSVI recap

For each maturity TmT\_{m}, eSSVI parameterizes total variance as

|  |  |  |  |
| --- | --- | --- | --- |
|  | wm​(k)=θm2​(1+ρm​ϕm​k+(ϕm​k+ρm)2+(1−ρm2)),w\_{m}(k)=\frac{\theta\_{m}}{2}\Bigl(1+\rho\_{m}\phi\_{m}k+\sqrt{(\phi\_{m}k+\rho\_{m})^{2}+(1-\rho\_{m}^{2})}\Bigr), |  | (1) |

with parameters θm>0\theta\_{m}>0, ρm∈(−1,1)\rho\_{m}\in(-1,1), and ϕm>0\phi\_{m}>0; see [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16)]. We use the numerically convenient reparametrization

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡θm∈ℝ,ρm=tanh⁡(ρmraw),ψm∈[0,ψmax​(ρm)),ϕm=ψm/θm.\log\theta\_{m}\in\mathbb{R},\qquad\rho\_{m}=\tanh(\rho^{\mathrm{raw}}\_{m}),\qquad\psi\_{m}\in\bigl[0,\ \psi\_{\max}(\rho\_{m})\bigr),\qquad\phi\_{m}=\psi\_{m}/\sqrt{\theta\_{m}}. |  | (2) |

Here ψm≡ϕm​θm\psi\_{m}\equiv\phi\_{m}\sqrt{\theta\_{m}} scales the ATM skew. The classical SSVI butterfly-free sufficient condition is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤ψm≤21+|ρm|for all ​m,0\leq\psi\_{m}\leq\frac{2}{1+|\rho\_{m}|}\quad\text{for all }m, |  | (3) |

which we enforce by a smooth squashing into the open interval [0,ψmax​(ρm))[0,\psi\_{\max}(\rho\_{m})) with ψmax​(ρ)=21+|ρ|−εψ\psi\_{\max}(\rho)=\tfrac{2}{1+|\rho|}-\varepsilon\_{\psi} for a small εψ>0\varepsilon\_{\psi}>0 [[14](https://arxiv.org/html/2510.04569v1#bib.bib14)]. To stabilize far-wing growth we cap the product

|  |  |  |  |
| --- | --- | --- | --- |
|  | θm​ϕm=ψm​θm≤τmax,\theta\_{m}\phi\_{m}=\psi\_{m}\sqrt{\theta\_{m}}\ \leq\ \tau\_{\max}, |  | (4) |

via a differentiable rescaling, which controls linear growth of wm​(k)w\_{m}(k) as |k|→∞|k|\to\infty and is consistent with Lee’s moment bounds [[20](https://arxiv.org/html/2510.04569v1#bib.bib20)]. Under ([3](https://arxiv.org/html/2510.04569v1#S2.E3 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), Black–Scholes prices CBS​(S,K,Tm,wm/Tm)C^{\mathrm{BS}}(S,K,T\_{m},\sqrt{w\_{m}/T\_{m}}) inherit smoothness in (θm,ρm,ψm)(\theta\_{m},\rho\_{m},\psi\_{m}), and the full eSSVI layer is end-to-end differentiable.

#### Calendar structure.

Sufficient conditions that preclude calendar arbitrage (no negative time value) can be expressed in terms of monotonicity of ATM variance θ​(T)\theta(T) and the joint evolution of (ρ​(T),ψ​(T))(\rho(T),\psi(T)); see [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [15](https://arxiv.org/html/2510.04569v1#bib.bib15), [16](https://arxiv.org/html/2510.04569v1#bib.bib16)] for explicit constructions. In our learning setting we additionally enforce calendar monotonicity on the *price* lattice via a smooth surrogate; see §[2.3](https://arxiv.org/html/2510.04569v1#S2.SS3 "2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

### 2.3 Static no-arbitrage: butterfly and calendar

Static no-arbitrage imposes convexity of call prices in KK (butterfly) for fixed TT and monotonicity in TT (calendar) for fixed KK:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Butterfly) | ∂K​KC​(S,K,T)≥ 0,\displaystyle\partial\_{KK}C(S,K,T)\ \geq\ 0, |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Calendar) | ∂TC​(S,K,T)≥ 0.\displaystyle\partial\_{T}C(S,K,T)\ \geq\ 0. |  | (6) |

On a discrete lattice, we measure violations with differentiable surrogates (normalizing by typical scales to balance maturities):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | BF\displaystyle\mathrm{BF} | ≡1M​∑m=1M1|𝒦′|​∑K∈𝒦′ReLU​(−ΔK2​Cm​(K)Δ​K2)/C¯m,\displaystyle\equiv\frac{1}{M}\sum\_{m=1}^{M}\frac{1}{|\mathcal{K}^{\prime}|}\sum\_{K\in\mathcal{K}^{\prime}}\mathrm{ReLU}\!\Bigl(-\frac{\Delta\_{K}^{2}C\_{m}(K)}{\Delta K^{2}}\Bigr)\Big/\bar{C}\_{m}, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CAL\displaystyle\mathrm{CAL} | ≡1M−1​∑m=1M−11|𝒦|​∑K∈𝒦ReLU​(Cm​(K)−Cm+1​(K))/C¯m,m+1,\displaystyle\equiv\frac{1}{M-1}\sum\_{m=1}^{M-1}\frac{1}{|\mathcal{K}|}\sum\_{K\in\mathcal{K}}\mathrm{ReLU}\!\bigl(C\_{m}(K)-C\_{m+1}(K)\bigr)\Big/\bar{C}\_{m,m+1}, |  | (8) |

where Cm​(K)C\_{m}(K) denotes CBSC^{\mathrm{BS}} at maturity TmT\_{m}, 𝒦′\mathcal{K}^{\prime} is an evenly spaced strike lattice, and C¯m,C¯m,m+1\bar{C}\_{m},\bar{C}\_{m,m+1} are level normalizers (e.g., mean absolute prices) that stabilize the penalty magnitudes across mm. The maps in ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) are piecewise smooth; in practice we replace ReLU\mathrm{ReLU} by a softplus to ensure C1C^{1}-smoothness, which we exploit for policy gradients.

###### Assumption 1 (Smoothness and bounds).

For all mm, the parameter tuple (θm,ρm,ψm)(\theta\_{m},\rho\_{m},\psi\_{m}) stays in a compact set where ([3](https://arxiv.org/html/2510.04569v1#S2.E3 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and ([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) hold, maturities satisfy 0<T1<⋯<TM0<T\_{1}<\cdots<T\_{M}, the strike lattice has bounded spacing Δ​K\Delta K, and the Black–Scholes inputs are clamped away from degeneracy (Tm≥Tmin>0T\_{m}\geq T\_{\min}>0, σ≥σmin>0\sigma\geq\sigma\_{\min}>0).

Under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), Cm​(K)C\_{m}(K) and the surrogates BF,CAL\mathrm{BF},\mathrm{CAL} are locally Lipschitz in (θ,ρ,ψ)(\theta,\rho,\psi), with constants depending on (Tmin,σmin,Δ​K,τmax)(T\_{\min},\sigma\_{\min},\Delta K,\tau\_{\max}); see [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [16](https://arxiv.org/html/2510.04569v1#bib.bib16)] for background on SSVI/eSSVI regularity.

### 2.4 Tail risk: Conditional Value-at-Risk

We adopt Conditional Value-at-Risk (cvar) at tail level q∈(0,1)q\in(0,1) as the downside risk functional for (negative) P&L XX [[29](https://arxiv.org/html/2510.04569v1#bib.bib29), [30](https://arxiv.org/html/2510.04569v1#bib.bib30)]. Using the Rockafellar–Uryasev representation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRq​(X)=minη∈ℝ⁡{η+11−q​𝔼​[(X−η)−]},\mathrm{CVaR}\_{q}(X)\ =\ \min\_{\eta\in\mathbb{R}}\ \Bigl\{\ \eta\ +\ \frac{1}{1-q}\,\mathbb{E}\bigl[(X-\eta)\_{-}\bigr]\ \Bigr\}, |  | (9) |

where (x)−=max⁡{−x,0}(x)\_{-}=\max\{-x,0\}. CVaR is coherent [[47](https://arxiv.org/html/2510.04569v1#bib.bib47), [46](https://arxiv.org/html/2510.04569v1#bib.bib46)], convex in the loss distribution, and admits unbiased (or bias-controlled) gradient estimators via the subdifferential of ([9](https://arxiv.org/html/2510.04569v1#S2.E9 "In 2.4 Tail risk: Conditional Value-at-Risk ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) [[32](https://arxiv.org/html/2510.04569v1#bib.bib32), [33](https://arxiv.org/html/2510.04569v1#bib.bib33), [34](https://arxiv.org/html/2510.04569v1#bib.bib34)]. In implementation we use a smooth replacement for (⋅)−(\cdot)\_{-} (e.g., softplus) and a small Monte Carlo batch per step to estimate CVaRq\mathrm{CVaR}\_{q} and its gradient.

### 2.5 Constrained MDP (cmdp) formulation

We cast option market making as a discounted *constrained* MDP

|  |  |  |
| --- | --- | --- |
|  | ℳ=(𝒮,𝒜,P,r,γ,d0;{gj}j=1J),\mathcal{M}=(\mathcal{S},\mathcal{A},P,r,\gamma,d\_{0};\ \{g\_{j}\}\_{j=1}^{J}), |  |

with state space 𝒮\mathcal{S} (price-path features, surface summaries), action space 𝒜\mathcal{A} (half-spread, hedge intensity, and structured eSSVI deformations such as ρ\rho-shift and ψ\psi-scale), transition kernel P(⋅|s,a)P(\cdot|s,a) capturing price evolution and executions, discount γ∈(0,1)\gamma\in(0,1), initial distribution d0d\_{0}, instantaneous reward r​(s,a,s′)r(s,a,s^{\prime}), and constraint functions gj​(s,a,s′)g\_{j}(s,a,s^{\prime}) (e.g., arbitrage and smooth-shape proxies). The (risk-sensitive) objective reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxπ𝔼π​[∑t=0∞γt​r​(st,at,st+1)]−λrisk​CVaRq​(∑t=0∞γt​ℓ​(st,at,st+1)),\max\_{\pi}\ \ \mathbb{E}\_{\pi}\!\Big[\sum\_{t=0}^{\infty}\gamma^{t}\,r(s\_{t},a\_{t},s\_{t+1})\Big]\ -\ \lambda\_{\mathrm{risk}}\,\mathrm{CVaR}\_{q}\!\Big(\sum\_{t=0}^{\infty}\gamma^{t}\,\ell(s\_{t},a\_{t},s\_{t+1})\Big), |  | (10) |

subject to long-run constraints

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π​[∑t=0∞γt​gj​(st,at,st+1)]≤εj,j=1,…,J,\mathbb{E}\_{\pi}\!\Big[\sum\_{t=0}^{\infty}\gamma^{t}\,g\_{j}(s\_{t},a\_{t},s\_{t+1})\Big]\ \leq\ \varepsilon\_{j},\qquad j=1,\dots,J, |  | (11) |

where ℓ\ell is a (nonnegative) loss proxy for tail-risk shaping and λrisk≥0\lambda\_{\mathrm{risk}}\geq 0 trades off mean performance and tail control. Typical constraints include:

* •

  *Arbitrage consistency*: garb​(s,a)≡BF​(s,a)+CAL​(s,a)g\_{\mathrm{arb}}(s,a)\equiv\mathrm{BF}(s,a)+\mathrm{CAL}(s,a) using ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).
* •

  *Shape smoothness*: gshape​(s,a)g\_{\mathrm{shape}}(s,a) penalizing cross-maturity parameter variation, e.g., ‖Δ​θ‖22+‖Δ​ρ‖22+‖Δ​ψ‖22\|\Delta\theta\|\_{2}^{2}+\|\Delta\rho\|\_{2}^{2}+\|\Delta\psi\|\_{2}^{2}.

A standard way to solve ([10](https://arxiv.org/html/2510.04569v1#S2.E10 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([11](https://arxiv.org/html/2510.04569v1#S2.E11 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) uses a Lagrangian with nonnegative multipliers λ∈ℝ+J\lambda\in\mathbb{R}\_{+}^{J},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(π,λ)=𝔼π​[∑tγt​rt]−λrisk​CVaRq​(∑tγt​ℓt)−∑j=1Jλj​(𝔼π​[∑tγt​gj,t]−εj),\mathcal{L}(\pi,\lambda)\ =\ \mathbb{E}\_{\pi}\!\Big[\sum\_{t}\gamma^{t}\,r\_{t}\Big]\ -\ \lambda\_{\mathrm{risk}}\,\mathrm{CVaR}\_{q}\!\Big(\sum\_{t}\gamma^{t}\ell\_{t}\Big)\ -\ \sum\_{j=1}^{J}\lambda\_{j}\Big(\mathbb{E}\_{\pi}\!\big[\sum\_{t}\gamma^{t}g\_{j,t}\big]-\varepsilon\_{j}\Big), |  | (12) |

and seeks a saddle point maxπ⁡minλ≥0⁡ℒ​(π,λ)\max\_{\pi}\min\_{\lambda\geq 0}\mathcal{L}(\pi,\lambda). Under compactness and a Slater condition, occupancy-measure convexity yields strong duality for CMDPs [[48](https://arxiv.org/html/2510.04569v1#bib.bib48), [49](https://arxiv.org/html/2510.04569v1#bib.bib49)]. We will exploit ([12](https://arxiv.org/html/2510.04569v1#S2.E12 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) in §[3](https://arxiv.org/html/2510.04569v1#S3 "3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") by (i) embedding BF\mathrm{BF}/CAL\mathrm{CAL} directly in the reward as differentiable penalties and (ii) introducing a *state-dependent* dual control (“dual”) that lets the policy raise or lower arbitrage pressure on the fly, while the base multipliers λ\lambda are annealed across episodes.

###### Assumption 2 (Well-posedness of the CMDP).

The action set is compact; r,ℓ,gjr,\ell,g\_{j} are bounded and locally Lipschitz in the eSSVI parameters under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"); and the Markov kernel P(⋅|s,a)P(\cdot|s,a) is weakly continuous. Then optimal stationary (possibly randomized) policies exist [[49](https://arxiv.org/html/2510.04569v1#bib.bib49), [48](https://arxiv.org/html/2510.04569v1#bib.bib48)], and policy-gradient methods are justified by dominated convergence arguments when using smooth surrogates in ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

#### Summary.

The eSSVI layer ([1](https://arxiv.org/html/2510.04569v1#S2.E1 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) provides an *arbitrage-consistent* and *differentiable* pricing map; the static-no-arbitrage surrogates ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) translate no-butterfly and no-calendar into smooth penalties; CVaR ([9](https://arxiv.org/html/2510.04569v1#S2.E9 "In 2.4 Tail risk: Conditional Value-at-Risk ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) supplies a coherent tail-risk objective; and the CMDP ([10](https://arxiv.org/html/2510.04569v1#S2.E10 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([11](https://arxiv.org/html/2510.04569v1#S2.E11 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) binds them into a single risk-sensitive control problem.

## 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP

We now instantiate the ingredients of §[2](https://arxiv.org/html/2510.04569v1#S2 "2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") into a *constrained*, risk-sensitive control model. The agent acts on spreads, hedging intensity, and structured deformations of an *arbitrage-free, differentiable* eSSVI surface. Executions are *intensity-driven* and respond monotonically to spreads and relative mispricing. The reward combines quoting and hedging P&L with *smooth* arbitrage proxies and a CVaR-based tail penalty. Throughout we assume Assumptions [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and [2](https://arxiv.org/html/2510.04569v1#Thmassumption2 "Assumption 2 (Well-posedness of the CMDP). ‣ 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

### 3.1 State, action, transition, and reward

#### State.

At decision time tt, the state st∈𝒮s\_{t}\in\mathcal{S} aggregates (i) mid-price features, (ii) surface summaries, and (iii) recent actions:

|  |  |  |
| --- | --- | --- |
|  | st=[fprice​(S0:t),ftime​(t/Tday),fsurf​(θ^,ρ^,ψ^),fctrl​(αt−1,hedget−1)],s\_{t}=\bigl[f\_{\mathrm{price}}(S\_{0:t}),\ f\_{\mathrm{time}}(t/T\_{\text{day}}),\ f\_{\mathrm{surf}}(\widehat{\theta},\widehat{\rho},\widehat{\psi}),\ f\_{\mathrm{ctrl}}(\alpha\_{t-1},\mathrm{hedge}\_{t-1})\bigr], |  |

where fsurff\_{\mathrm{surf}} may include ATM level/slope derived from the *current* eSSVI estimate and fpricef\_{\mathrm{price}} includes rescaled returns or realized volatility.

#### Action.

The agent chooses a continuous action vector

|  |  |  |
| --- | --- | --- |
|  | at=(αt,hedget,ψ​-scalet,ρ​-shiftt,dualt)∈𝒜,a\_{t}=(\alpha\_{t},\ \mathrm{hedge}\_{t},\ \psi\text{-scale}\_{t},\ \rho\text{-shift}\_{t},\ \mathrm{dual}\_{t})\in\mathcal{A}, |  |

with components squashed to physical ranges:

|  |  |  |
| --- | --- | --- |
|  | αt∈[0,αmax],hedget∈[0,1],ψ​-scalet∈[ψmin,ψmax],ρ​-shiftt∈[−ρmax,ρmax],dualt∈[0,∞).\alpha\_{t}\in[0,\alpha\_{\max}],\quad\mathrm{hedge}\_{t}\in[0,1],\quad\psi\text{-scale}\_{t}\in[\psi\_{\min},\psi\_{\max}],\quad\rho\text{-shift}\_{t}\in[-\rho\_{\max},\rho\_{\max}],\quad\mathrm{dual}\_{t}\in[0,\infty). |  |

The *quoted* surface parameters at maturity TmT\_{m} are obtained from the current estimate (θm,ρm,ψm)(\theta\_{m},\rho\_{m},\psi\_{m}) by a structured, differentiable perturbation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~m=ψm⋅ψ​-scalet,ρ~m=ρm+ρ​-shiftt,θ~m=θm,\tilde{\psi}\_{m}=\psi\_{m}\cdot\psi\text{-scale}\_{t},\qquad\tilde{\rho}\_{m}=\rho\_{m}+\rho\text{-shift}\_{t},\qquad\tilde{\theta}\_{m}=\theta\_{m}, |  | (13) |

followed by the eSSVI map ([1](https://arxiv.org/html/2510.04569v1#S2.E1 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and the wing cap ([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). The action thus co-evolves the surface while retaining differentiability and static-arbitrage safeguards.

#### Quoting and spreads.

For log-moneyness k∈𝒦k\in\mathcal{K} and maturity TmT\_{m}, the mid-quote is the Black–Scholes call price on the *quoted* surface

|  |  |  |  |
| --- | --- | --- | --- |
|  | midm(k)=CBS(St,K=Stek,Tm,σ~m(k)),\mathrm{mid}\_{m}(k)=C^{\mathrm{BS}}\!\bigl(S\_{t},\ K=S\_{t}e^{k},\ T\_{m},\ \tilde{\sigma}\_{m}(k)\bigr), |  | (14) |

where σ~m​(k)=w~m​(k)/Tm\tilde{\sigma}\_{m}(k)=\sqrt{\tilde{w}\_{m}(k)/T\_{m}} and w~m\tilde{w}\_{m} is ([1](https://arxiv.org/html/2510.04569v1#S2.E1 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with (θ~,ρ~,ψ~)(\tilde{\theta},\tilde{\rho},\tilde{\psi}).
A volatility-proportional half-spread maps αt\alpha\_{t} to prices:

|  |  |  |  |
| --- | --- | --- | --- |
|  | spread​(m,k)2≡αt​St​σ~m​(k)​Tm​s0,\frac{\mathrm{spread}(m,k)}{2}\equiv\alpha\_{t}\ S\_{t}\ \tilde{\sigma}\_{m}(k)\ \sqrt{T\_{m}}\ s\_{0}, |  | (15) |

so that ask=mid+spread/2\mathrm{ask}=\mathrm{mid}+\mathrm{spread}/2 and bid=mid−spread/2\mathrm{bid}=\mathrm{mid}-\mathrm{spread}/2.

#### Intensity-based executions.

Let Cm⋆​(k)C^{\star}\_{m}(k) denote the *latent* fair price (from a held-out “true” surface). Buy/sell intensities respond to relative mispricing and spreads via a smooth, monotone link [[12](https://arxiv.org/html/2510.04569v1#bib.bib12), [13](https://arxiv.org/html/2510.04569v1#bib.bib13), [8](https://arxiv.org/html/2510.04569v1#bib.bib8)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λbuy​(m,k)\displaystyle\lambda\_{\mathrm{buy}}(m,k) | =λ0​w​(k)​[1−σ​(β​{askm​(k)−Cm⋆​(k)})],\displaystyle=\lambda\_{0}\,w(k)\,\Bigl[1-\sigma\bigl(\beta\{\mathrm{ask}\_{m}(k)-C^{\star}\_{m}(k)\}\bigr)\Bigr], |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λsell​(m,k)\displaystyle\lambda\_{\mathrm{sell}}(m,k) | =λ0​w​(k)​[1−σ​(β​{Cm⋆​(k)−bidm​(k)})],\displaystyle=\lambda\_{0}\,w(k)\,\Bigl[1-\sigma\bigl(\beta\{C^{\star}\_{m}(k)-\mathrm{bid}\_{m}(k)\}\bigr)\Bigr], |  | (17) |

where w​(k)=exp⁡(−|k|/κ)w(k)=\exp(-|k|/\kappa) emphasizes ATM demand and σ​(⋅)\sigma(\cdot) is logistic. Expected fills vbuy/sell=λbuy/sellv\_{\mathrm{buy/sell}}=\lambda\_{\mathrm{buy/sell}} are used in the *per-step* reward to reduce variance; Poisson sampling is retained for CVaR estimation in §[3.3](https://arxiv.org/html/2510.04569v1#S3.SS3 "3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

#### Hedging and P&L.

The net option delta under expected fills is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δtnet=∑m,k(vsell​(m,k)−vbuy​(m,k))​ΔmBS​(k),\Delta^{\mathrm{net}}\_{t}=\sum\_{m,k}\bigl(v\_{\mathrm{sell}}(m,k)-v\_{\mathrm{buy}}(m,k)\bigr)\ \Delta^{\mathrm{BS}}\_{m}(k), |  | (18) |

and delta-hedging P&L is

|  |  |  |  |
| --- | --- | --- | --- |
|  | PNLthedge=hedget​Δtnet​(St+1−St).\mathrm{PNL}^{\mathrm{hedge}}\_{t}=\mathrm{hedge}\_{t}\ \Delta^{\mathrm{net}}\_{t}\ \bigl(S\_{t+1}-S\_{t}\bigr). |  | (19) |

The quoting P&L from expected fills is

|  |  |  |  |
| --- | --- | --- | --- |
|  | PNLtquote=∑m,k[vbuy​(m,k)​(askm​(k)−Cm⋆​(k))+vsell​(m,k)​(Cm⋆​(k)−bidm​(k))].\mathrm{PNL}^{\mathrm{quote}}\_{t}=\sum\_{m,k}\Bigl[v\_{\mathrm{buy}}(m,k)\ \bigl(\mathrm{ask}\_{m}(k)-C^{\star}\_{m}(k)\bigr)+v\_{\mathrm{sell}}(m,k)\ \bigl(C^{\star}\_{m}(k)-\mathrm{bid}\_{m}(k)\bigr)\Bigr]. |  | (20) |

#### Smooth arbitrage and shape penalties.

We penalize static-arbitrage surrogates and cross-maturity roughness:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Shapet=mean​(‖Δ​θ~‖22+‖Δ​ρ~‖22+‖Δ​ψ~‖22),Arbt=BFt+CALt,\mathrm{Shape}\_{t}=\mathrm{mean}\bigl(\|\Delta\tilde{\theta}\|\_{2}^{2}+\|\Delta\tilde{\rho}\|\_{2}^{2}+\|\Delta\tilde{\psi}\|\_{2}^{2}\bigr),\qquad\mathrm{Arb}\_{t}=\mathrm{BF}\_{t}+\mathrm{CAL}\_{t}, |  | (21) |

with BF,CAL\mathrm{BF},\mathrm{CAL} from ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) evaluated on (θ~,ρ~,ψ~)(\tilde{\theta},\tilde{\rho},\tilde{\psi}) at time tt. Softplus smoothing yields C1C^{1} maps w.r.t. actions via the chain rule.

#### Per-step reward.

Define raw revenue PNLtraw=PNLtquote+PNLthedge\mathrm{PNL}^{\mathrm{raw}}\_{t}=\mathrm{PNL}^{\mathrm{quote}}\_{t}+\mathrm{PNL}^{\mathrm{hedge}}\_{t}. The (penalized) reward is

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=PNLtraw−λshape​Shapet−(λarb+dualt)​Arbt−λcvar​CVaR^q,t−,r\_{t}=\mathrm{PNL}^{\mathrm{raw}}\_{t}-\lambda\_{\mathrm{shape}}\ \mathrm{Shape}\_{t}-\bigl(\lambda\_{\mathrm{arb}}+\mathrm{dual}\_{t}\bigr)\ \mathrm{Arb}\_{t}-\lambda\_{\mathrm{cvar}}\ \widehat{\mathrm{CVaR}}^{-}\_{q,t}, |  | (22) |

where CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} is the training-time estimator described in §[3.3](https://arxiv.org/html/2510.04569v1#S3.SS3 "3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), and dualt≥0\mathrm{dual}\_{t}\geq 0 acts as a *state-dependent* multiplier that tightens arbitrage pressure on demand.

#### Transition kernel.

The controlled Markov kernel P(⋅|st,at)P(\cdot|s\_{t},a\_{t}) advances (i) the mid-price (via ABIDES-style replay or a calibrated Heston step [[37](https://arxiv.org/html/2510.04569v1#bib.bib37), [24](https://arxiv.org/html/2510.04569v1#bib.bib24)]), (ii) the eSSVI estimate (e.g., a mean-reverting filter toward latent parameters), and (iii) any auxiliary state features. Weak continuity holds under standard discretizations and bounded parameter updates.

### 3.2 Discrete consistency of BF/CAL surrogates

We recall the continuous no-arbitrage conditions ([5](https://arxiv.org/html/2510.04569v1#S2.E5 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([6](https://arxiv.org/html/2510.04569v1#S2.E6 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and their discrete surrogates ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). The following results (proved in §[6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) justify our use of lattice penalties during learning.

###### Proposition 1 (Grid-consistency of butterfly surrogate).

Fix TmT\_{m} and suppose C​(⋅,Tm)∈C2C(\cdot,T\_{m})\in C^{2} on a compact strike interval. If ∂K​KC​(⋅,Tm)≥0\partial\_{KK}C(\cdot,T\_{m})\geq 0 on that interval, then for any sequence of evenly spaced lattices with spacing Δ​K→0\Delta K\to 0 we have BFm→0\mathrm{BF}\_{m}\to 0. Conversely, if there exists K0K\_{0} with ∂K​KC​(K0,Tm)<0\partial\_{KK}C(K\_{0},T\_{m})<0, then BFm>0\mathrm{BF}\_{m}>0 for all sufficiently fine lattices. The convergence is locally uniform under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

###### Proposition 2 (Grid-consistency of calendar surrogate).

Fix KK and suppose C​(K,⋅)∈C1C(K,\cdot)\in C^{1} and ∂TC​(K,T)≥0\partial\_{T}C(K,T)\geq 0 on [T1,TM][T\_{1},T\_{M}]. For any maturity grids with mesh Δ​T→0\Delta T\to 0, the calendar surrogate satisfies maxm⁡CALm→0\max\_{m}\mathrm{CAL}\_{m}\to 0. If, instead, ∂TC​(K0,T0)<0\partial\_{T}C(K\_{0},T\_{0})<0 at some (K0,T0)(K\_{0},T\_{0}), then CALm>0\mathrm{CAL}\_{m}>0 for the adjacent pair containing T0T\_{0} on sufficiently fine grids.

###### Remark 1.

The normalizers C¯m,C¯m,m+1\bar{C}\_{m},\bar{C}\_{m,m+1} render BF,CAL\mathrm{BF},\mathrm{CAL} approximately scale-invariant across maturities; softplus smoothing of the hinge terms makes the penalties C1C^{1}, enabling stable policy gradients through ([21](https://arxiv.org/html/2510.04569v1#S3.E21 "In Smooth arbitrage and shape penalties. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and ([22](https://arxiv.org/html/2510.04569v1#S3.E22 "In Per-step reward. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

The propositions formalize the intuition that our lattice penalties are *consistent* with continuous no-arbitrage while remaining differentiable and numerically stable for learning (compare [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [16](https://arxiv.org/html/2510.04569v1#bib.bib16), [18](https://arxiv.org/html/2510.04569v1#bib.bib18)]).

### 3.3 CVaR as the tail-risk term and a differentiable estimator

We control downside risk via CVaRq\mathrm{CVaR}\_{q} at level q∈(0,1)q\in(0,1), using the Rockafellar–Uryasev program ([9](https://arxiv.org/html/2510.04569v1#S2.E9 "In 2.4 Tail risk: Conditional Value-at-Risk ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with a smooth hinge. In our setting we estimate a *per-step* downside CVaR proxy by sampling execution and price scenarios conditioned on (st,at)(s\_{t},a\_{t}).

#### Scenario construction.

Given expected intensities vbuy/sellv\_{\mathrm{buy/sell}} from ([16](https://arxiv.org/html/2510.04569v1#S3.E16 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([17](https://arxiv.org/html/2510.04569v1#S3.E17 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), we draw Poisson volumes
v~buy/sell∼Pois​(vbuy/sell)\tilde{v}\_{\mathrm{buy/sell}}\sim\mathrm{Pois}(v\_{\mathrm{buy/sell}})
and perturb the next price change by
Δ~​S∼𝒩​(Δ​S,ς2)\tilde{\Delta}S\sim\mathcal{N}(\Delta S,\varsigma^{2})
with Δ​S=St+1−St\Delta S=S\_{t+1}-S\_{t} and a small variance ς2\varsigma^{2} calibrated to intraday noise. For each scenario we compute

|  |  |  |
| --- | --- | --- |
|  | PNL~t=PNLtquote​(v~)+hedget​Δtnet​Δ~​S,\tilde{\mathrm{PNL}}\_{t}=\mathrm{PNL}^{\mathrm{quote}}\_{t}(\tilde{v})+\mathrm{hedge}\_{t}\,\Delta^{\mathrm{net}}\_{t}\,\tilde{\Delta}S, |  |

and plug into the smooth RU objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaR^q,t−≡minη∈ℝ⁡{η+11−q​𝔼^​[sτ​(η−PNL~t)]},\widehat{\mathrm{CVaR}}^{-}\_{q,t}\equiv\min\_{\eta\in\mathbb{R}}\ \Bigl\{\ \eta+\frac{1}{1-q}\ \widehat{\mathbb{E}}\bigl[s\_{\tau}(\eta-\tilde{\mathrm{PNL}}\_{t})\bigr]\ \Bigr\}, |  | (23) |

where sτ​(x)s\_{\tau}(x) is a temperature-τ\tau softplus approximation of x+=max⁡{x,0}x\_{+}=\max\{x,0\} and 𝔼^\widehat{\mathbb{E}} averages over the Monte Carlo batch.

#### Differentiability and gradients.

The composition in ([23](https://arxiv.org/html/2510.04569v1#S3.E23 "In Scenario construction. ‣ 3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) is C1C^{1} in (η,at)(\eta,a\_{t}) for τ>0\tau>0, and admits pathwise derivatives w.r.t. actions via the chain rule because (i) v~\tilde{v} is drawn from Poisson laws with parameters differentiable in ata\_{t} (using LR/score-function gradients), (ii) Δ~​S\tilde{\Delta}S is a reparameterized Gaussian, and (iii) PNLtquote\mathrm{PNL}^{\mathrm{quote}}\_{t} and Δtnet\Delta^{\mathrm{net}}\_{t} are differentiable in the quoted surface parameters (hence in actions) under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"). The following theorem (proved in §[6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) formalizes the estimator.

###### Theorem 1 (CVaR policy-gradient identity with smoothing).

Under Assumptions [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and [2](https://arxiv.org/html/2510.04569v1#Thmassumption2 "Assumption 2 (Well-posedness of the CMDP). ‣ 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), for fixed q∈(0,1)q\in(0,1) and τ>0\tau>0, the smoothed RU objective ([23](https://arxiv.org/html/2510.04569v1#S3.E23 "In Scenario construction. ‣ 3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) yields a well-defined gradient ∇atCVaR^q,t−\nabla\_{a\_{t}}\widehat{\mathrm{CVaR}}^{-}\_{q,t} with bounded variance for finite Monte Carlo batches, combining (a) reparameterization for Δ~​S\tilde{\Delta}S and (b) likelihood-ratio terms for v~\tilde{v}. As τ↓0\tau\downarrow 0, CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} and its gradient converge to those of the nonsmooth RU functional in ([9](https://arxiv.org/html/2510.04569v1#S2.E9 "In 2.4 Tail risk: Conditional Value-at-Risk ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) in the sense of epi-convergence and subgradient convergence [[29](https://arxiv.org/html/2510.04569v1#bib.bib29), [32](https://arxiv.org/html/2510.04569v1#bib.bib32), [33](https://arxiv.org/html/2510.04569v1#bib.bib33), [34](https://arxiv.org/html/2510.04569v1#bib.bib34)].

#### Primal–dual view.

Combining ([22](https://arxiv.org/html/2510.04569v1#S3.E22 "In Per-step reward. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with the CMDP Lagrangian ([12](https://arxiv.org/html/2510.04569v1#S2.E12 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), the fixed λarb,λshape,λcvar\lambda\_{\mathrm{arb}},\lambda\_{\mathrm{shape}},\lambda\_{\mathrm{cvar}} play the role of base multipliers, while dualt\mathrm{dual}\_{t} is a *state-dependent* corrective multiplier that lets the policy adapt arbitrage pressure online. This is compatible with primal–dual and trust-region methods in CMDPs [[48](https://arxiv.org/html/2510.04569v1#bib.bib48), [49](https://arxiv.org/html/2510.04569v1#bib.bib49), [52](https://arxiv.org/html/2510.04569v1#bib.bib52), [53](https://arxiv.org/html/2510.04569v1#bib.bib53), [50](https://arxiv.org/html/2510.04569v1#bib.bib50)].

## 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual

We optimize the risk-sensitive, constrained objective from §[2.5](https://arxiv.org/html/2510.04569v1#S2.SS5 "2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") using a two-stage scheme: a *supervised warm-start* that anchors early exploration to a conservative baseline and a *PPO* phase that maximizes the penalized reward while annealing structural weights. A key design choice is a *state-dependent dual action* that serves as a learnable approximation to a *Lagrange multiplier* for the static no-arbitrage constraints (formalized in §[6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

### 4.1 Policy class and parameterization

The stochastic policy πϑ​(z∣s)\pi\_{\vartheta}(z\mid s) outputs *raw* actions z∈ℝ5z\in\mathbb{R}^{5} with a Gaussian head

|  |  |  |
| --- | --- | --- |
|  | πϑ​(z∣s)=𝒩​(μϑ​(s),diag​(σϑ2​(s))),\pi\_{\vartheta}(z\mid s)=\mathcal{N}\bigl(\mu\_{\vartheta}(s),\ \mathrm{diag}(\sigma\_{\vartheta}^{2}(s))\bigr), |  |

and maps zz to *physical* actions a=squash​(z)a=\mathrm{squash}(z) via elementwise transforms consistent with §[3.1](https://arxiv.org/html/2510.04569v1#S3.SS1 "3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"):

|  |  |  |
| --- | --- | --- |
|  | α=αmax​σ​(z1),hedge=σ​(z2),ψ​-scale=ψmin+(ψmax−ψmin)​σ​(z3),ρ​-shift=ρmax​tanh⁡(z4),dual=softplus​(z5).\alpha=\alpha\_{\max}\,\sigma(z\_{1}),\quad\mathrm{hedge}=\sigma(z\_{2}),\quad\psi\text{-scale}=\psi\_{\min}+(\psi\_{\max}-\psi\_{\min})\,\sigma(z\_{3}),\quad\rho\text{-shift}=\rho\_{\max}\tanh(z\_{4}),\quad\mathrm{dual}=\mathrm{softplus}(z\_{5}). |  |

The critic Vω​(s)V\_{\omega}(s) shares no weights with the actor. Unless stated, both are two-layer MLPs with tanh\tanh activations, and the actor’s log⁡σϑ\log\sigma\_{\vartheta} is state-dependent but bounded in [log⁡σmin,log⁡σmax][\log\sigma\_{\min},\log\sigma\_{\max}].

### 4.2 Stage I: Supervised warm-start

To stabilize early exploration near the arbitrage-feasible region, we regress the *squashed* actor output towards a robust baseline action a⋆=(α⋆,hedge⋆,ψ​-scale⋆,ρ​-shift⋆,dual⋆)a^{\star}=(\alpha^{\star},\mathrm{hedge}^{\star},\psi\text{-scale}^{\star},\rho\text{-shift}^{\star},\mathrm{dual}^{\star}) with

|  |  |  |
| --- | --- | --- |
|  | a⋆=(0.01, 0.5, 1.0, 0.0, 0.0),a^{\star}=(0.01,\ 0.5,\ 1.0,\ 0.0,\ 0.0), |  |

minimizing the mean-squared error on states ss sampled from the initial environment distribution (and/or replay of a few short rollouts):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒwarm(ϑ)=𝔼s∼𝒟0∥squash(μϑ(s))−a⋆∥22+λent𝔼s[ℋ(πϑ(⋅∣s))].\mathcal{L}\_{\mathrm{warm}}(\vartheta)\ =\ \mathbb{E}\_{s\sim\mathcal{D}\_{0}}\ \big\|\,\mathrm{squash}(\mu\_{\vartheta}(s))\ -\ a^{\star}\,\big\|\_{2}^{2}\ +\ \lambda\_{\mathrm{ent}}\,\mathbb{E}\_{s}\big[\mathcal{H}(\pi\_{\vartheta}(\cdot\mid s))\big]. |  | (24) |

This *anchors spreads and hedging* and keeps the eSSVI deformation small so that BF/CAL penalties remain near zero at initialization. We use Adam for a small number of steps (e.g., 500500–10001000) with early stopping when BF+CAL\mathrm{BF}+\mathrm{CAL} falls below a target tolerance (see §[3.2](https://arxiv.org/html/2510.04569v1#S3.SS2 "3.2 Discrete consistency of BF/CAL surrogates ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

### 4.3 Stage II: PPO with structural annealing

Let τ=(st,zt,at,rt,st+1)t=0T−1\tau=(s\_{t},z\_{t},a\_{t},r\_{t},s\_{t+1})\_{t=0}^{T-1} be on-policy trajectories. PPO [[44](https://arxiv.org/html/2510.04569v1#bib.bib44)] maximizes the clipped surrogate with generalized advantage estimation (GAE) [[45](https://arxiv.org/html/2510.04569v1#bib.bib45)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒPPO​(ϑ)\displaystyle\mathcal{L}\_{\mathrm{PPO}}(\vartheta)\ | =𝔼[min(rt(ϑ)A^t,clip(rt(ϑ),1−ϵ,1+ϵ)A^t)]−cv𝔼[(Vω(st)−R^t)2]+cℋ𝔼[ℋ(πϑ(⋅∣st))],\displaystyle=\ \mathbb{E}\Big[\min\big(r\_{t}(\vartheta)\,\hat{A}\_{t},\ \mathrm{clip}(r\_{t}(\vartheta),1-\epsilon,1+\epsilon)\,\hat{A}\_{t}\big)\Big]-c\_{v}\,\mathbb{E}\big[(V\_{\omega}(s\_{t})-\hat{R}\_{t})^{2}\big]+c\_{\mathcal{H}}\,\mathbb{E}\big[\mathcal{H}(\pi\_{\vartheta}(\cdot\mid s\_{t}))\big], |  | (25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | rt​(ϑ)\displaystyle r\_{t}(\vartheta) | =πϑ​(zt∣st)πϑold​(zt∣st),A^t=∑l=0L−1(γ​λ)l​δt+l,δt=rt+γ​Vω​(st+1)−Vω​(st).\displaystyle=\frac{\pi\_{\vartheta}(z\_{t}\mid s\_{t})}{\pi\_{\vartheta\_{\mathrm{old}}}(z\_{t}\mid s\_{t})},\qquad\hat{A}\_{t}=\sum\_{l=0}^{L-1}(\gamma\lambda)^{l}\,\delta\_{t+l},\qquad\delta\_{t}=r\_{t}+\gamma V\_{\omega}(s\_{t+1})-V\_{\omega}(s\_{t}). |  |

Here rtr\_{t} includes *all* penalties via the reward definition ([22](https://arxiv.org/html/2510.04569v1#S3.E22 "In Per-step reward. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). We normalize advantages per batch, clip gradients, and train for several epochs per update with minibatches.

#### Structural weight annealing.

To separate *discovery* (revenue) from *discipline* (arbitrage/shape), we anneal the base multipliers linearly across episodes:

|  |  |  |
| --- | --- | --- |
|  | λshape:0→λshapemax,λarb:0→λarbmax,λcvar:λcvarmin→λcvarmax.\lambda\_{\mathrm{shape}}:0\ \to\ \lambda\_{\mathrm{shape}}^{\max},\qquad\lambda\_{\mathrm{arb}}:0\ \to\ \lambda\_{\mathrm{arb}}^{\max},\qquad\lambda\_{\mathrm{cvar}}:\ \lambda\_{\mathrm{cvar}}^{\min}\ \to\ \lambda\_{\mathrm{cvar}}^{\max}. |  |

This schedule reduces early sensitivity to surrogate curvature and mitigates premature collapse of the actor’s exploration.

### 4.4 A state-dependent dual as a learnable Lagrange multiplier

Recall the CMDP Lagrangian in ([12](https://arxiv.org/html/2510.04569v1#S2.E12 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). In classical primal–dual schemes, multipliers λ≥0\lambda\geq 0 evolve by dual ascent proportional to constraint violations [[48](https://arxiv.org/html/2510.04569v1#bib.bib48), [52](https://arxiv.org/html/2510.04569v1#bib.bib52), [53](https://arxiv.org/html/2510.04569v1#bib.bib53)]. Our design introduces a *state-dependent* *dual action* dualt≥0\mathrm{dual}\_{t}\geq 0 and defines the *effective* multiplier for static arbitrage as

|  |  |  |  |
| --- | --- | --- | --- |
|  | λeff​(st,at)≡λarb+dualt.\lambda\_{\mathrm{eff}}(s\_{t},a\_{t})\ \equiv\ \lambda\_{\mathrm{arb}}\ +\ \mathrm{dual}\_{t}. |  | (26) |

The per-step reward in ([22](https://arxiv.org/html/2510.04569v1#S3.E22 "In Per-step reward. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) contains the term −λeff​Arbt-\lambda\_{\mathrm{eff}}\,\mathrm{Arb}\_{t}. Although maximizing the *instantaneous* reward pushes dualt↓0\mathrm{dual}\_{t}\downarrow 0, the *long-horizon* objective trades off current penalty against future gains from moving the policy toward regions where Arb\mathrm{Arb} is easier to satisfy (and the eSSVI deformation becomes cheaper). In §[6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), we formalize this intuition by showing that, under ergodicity and smoothness, the policy gradient couples dualt\mathrm{dual}\_{t} positively with predicted violations, yielding a *learned* approximation to dual ascent. Concretely, a first-order stationarity condition implies that at an optimal (regular) policy, the advantage of increasing dual\mathrm{dual} is proportional to a discounted sum of future Arb\mathrm{Arb} terms, leading to dualt>0\mathrm{dual}\_{t}>0 whenever short-term violations reduce long-term return.

###### Remark 2 (Optional regularization of the dual head).

To improve numerical conditioning, one may add a small quadratic regularizer ηdual​𝔼​[dualt2]\eta\_{\mathrm{dual}}\mathbb{E}[\,\mathrm{dual}\_{t}^{2}\,] or an entropy bonus on z5z\_{5}, keeping the dual head responsive but bounded. This does not change the primal–dual interpretation.

### 4.5 Stability heuristics and schedules

#### Bounded exploration and value targets.

We clamp log⁡σϑ\log\sigma\_{\vartheta} to control exploration; we also clip the value target R^t\hat{R}\_{t} to stabilise critic updates. Reward/advantage whitening further reduces gradient variance.

#### Curriculum over CVaR estimation.

Scenario count for CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} (§[3.3](https://arxiv.org/html/2510.04569v1#S3.SS3 "3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) increases across training (e.g., NMC:16→64N\_{\mathrm{MC}}:16\to 64), matching the annealed λcvar\lambda\_{\mathrm{cvar}} and reducing estimator bias as the policy stabilizes; cf. [[56](https://arxiv.org/html/2510.04569v1#bib.bib56)].

#### Trust-region flavor.

While PPO lacks the exact monotonic improvement guarantee of TRPO [[57](https://arxiv.org/html/2510.04569v1#bib.bib57)], small clip ϵ\epsilon, advantage normalization, and gradient clipping approximate a trust region in practice. The Lipschitz properties of the smoothed surrogates (BF/CAL) from §[3.2](https://arxiv.org/html/2510.04569v1#S3.SS2 "3.2 Discrete consistency of BF/CAL surrogates ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") further help keep updates local.

### 4.6 Algorithm

Algorithm 1  Warm-Start + PPO with State-Dependent Dual

1: Input: actor πϑ\pi\_{\vartheta}, critic VωV\_{\omega}, schedules for (λshape,λarb,λcvar)(\lambda\_{\mathrm{shape}},\lambda\_{\mathrm{arb}},\lambda\_{\mathrm{cvar}})

2: Warm-start: sample states s∼𝒟0s\sim\mathcal{D}\_{0}; minimize ℒwarm​(ϑ)\mathcal{L}\_{\mathrm{warm}}(\vartheta) ([24](https://arxiv.org/html/2510.04569v1#S4.E24 "In 4.2 Stage I: Supervised warm-start ‣ 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); stop when BF+CAL≤τarb\mathrm{BF}+\mathrm{CAL}\leq\tau\_{\mathrm{arb}}

3: for episodes e=1,…,Ee=1,\dots,E do

4:  Set multipliers according to schedules; reset env; t←0t\leftarrow 0

5:  while episode not done do

6:   Observe sts\_{t}; sample zt∼πϑ(⋅∣st)z\_{t}\sim\pi\_{\vartheta}(\cdot\mid s\_{t}); set at=squash​(zt)a\_{t}=\mathrm{squash}(z\_{t})

7:   Quote via eSSVI deformation; compute intensities and expected fills; get rtr\_{t} via ([22](https://arxiv.org/html/2510.04569v1#S3.E22 "In Per-step reward. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))

8:   Step environment to st+1s\_{t+1}; store (st,zt,at,rt,st+1)(s\_{t},z\_{t},a\_{t},r\_{t},s\_{t+1})

9:   t←t+1t\leftarrow t+1

10:  end while

11:  Compute A^t\hat{A}\_{t} (GAE) and R^t\hat{R}\_{t}; normalize A^t\hat{A}\_{t}

12:  for epoch =1,…,K=1,\dots,K do

13:   Sample minibatches; ascend ∇ϑℒPPO​(ϑ)\nabla\_{\vartheta}\mathcal{L}\_{\mathrm{PPO}}(\vartheta) ([25](https://arxiv.org/html/2510.04569v1#S4.E25 "In 4.3 Stage II: PPO with structural annealing ‣ 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with gradient clipping

14:   Update critic by minimizing 𝔼​(Vω−R^)2\mathbb{E}(V\_{\omega}-\hat{R})^{2}

15:  end for

16: end for

#### Theoretical pointers to §[6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

We will show: (i) *Policy-gradient validity* with smoothed BF/CAL and CVaR estimators (Theorem [1](https://arxiv.org/html/2510.04569v1#Thmtheorem1 "Theorem 1 (CVaR policy-gradient identity with smoothing). ‣ Differentiability and gradients. ‣ 3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), (ii) *Grid-consistency* of surrogates (Propositions [1](https://arxiv.org/html/2510.04569v1#Thmproposition1 "Proposition 1 (Grid-consistency of butterfly surrogate). ‣ 3.2 Discrete consistency of BF/CAL surrogates ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[2](https://arxiv.org/html/2510.04569v1#Thmproposition2 "Proposition 2 (Grid-consistency of calendar surrogate). ‣ 3.2 Discrete consistency of BF/CAL surrogates ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), and (iii) a *primal–dual interpretation* of the state-dependent dual—under mild ergodicity and Lipschitz assumptions, the gradient of the long-run return w.r.t. the dual head correlates with discounted violation, implementing an implicit dual ascent.222See also classical Lagrangian CMDP analyses [[48](https://arxiv.org/html/2510.04569v1#bib.bib48)] and modern constrained policy optimization [[52](https://arxiv.org/html/2510.04569v1#bib.bib52), [53](https://arxiv.org/html/2510.04569v1#bib.bib53)].

## 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks

We show how each control dimension

|  |  |  |
| --- | --- | --- |
|  | at=(αt,hedget,ψ​-scalet,ρ​-shiftt,dualt)a\_{t}=(\alpha\_{t},\ \mathrm{hedge}\_{t},\ \psi\text{-scale}\_{t},\ \rho\text{-shift}\_{t},\ \mathrm{dual}\_{t}) |  |

affects quoting (mid,ask,bid\mathrm{mid},\mathrm{ask},\mathrm{bid}), execution intensities, and Greeks in closed form (or via stable chain rules). Throughout, we write w~m​(k)\tilde{w}\_{m}(k), σ~m​(k)=w~m​(k)/Tm\tilde{\sigma}\_{m}(k)=\sqrt{\tilde{w}\_{m}(k)/T\_{m}} for the *quoted* eSSVI surface obtained after the action-induced deformation ([13](https://arxiv.org/html/2510.04569v1#S3.E13 "In Action. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), and Cm​(K)≡CBS​(St,K,Tm,σ~m​(k))C\_{m}(K)\equiv C^{\mathrm{BS}}\!\big(S\_{t},K,T\_{m},\tilde{\sigma}\_{m}(k)\big) for the Black–Scholes call with log-moneyness k=log⁡(K/St)k=\log(K/S\_{t}). We set the risk-free rate and carry to zero for clarity; standard adjustments are straightforward [[61](https://arxiv.org/html/2510.04569v1#bib.bib61), [62](https://arxiv.org/html/2510.04569v1#bib.bib62), [63](https://arxiv.org/html/2510.04569v1#bib.bib63)].

### 5.1 Derivative templates through the eSSVI layer

Let w↦σ=w/Tw\mapsto\sigma=\sqrt{w/T} and CBS​(S,K,T,σ)C^{\mathrm{BS}}(S,K,T,\sigma) be C1C^{1}. Denote BS Vega by

|  |  |  |
| --- | --- | --- |
|  | 𝒱≡∂CBS∂σ​(S,K,T,σ),∂CBS∂w=∂CBS∂σ⋅∂σ∂w=𝒱2​σ​T.\mathcal{V}\equiv\frac{\partial C^{\mathrm{BS}}}{\partial\sigma}(S,K,T,\sigma),\qquad\frac{\partial C^{\mathrm{BS}}}{\partial w}=\frac{\partial C^{\mathrm{BS}}}{\partial\sigma}\cdot\frac{\partial\sigma}{\partial w}=\frac{\mathcal{V}}{2\sigma T}. |  |

For eSSVI total variance wm​(k)w\_{m}(k) in ([1](https://arxiv.org/html/2510.04569v1#S2.E1 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), write g​(k;ρ,ϕ)=(ϕ​k+ρ)2+(1−ρ2)g(k;\rho,\phi)=\sqrt{(\phi k+\rho)^{2}+(1-\rho^{2})}. One obtains (see Appendix §[Appendix D: eSSVI and Black–Scholes Derivatives](https://arxiv.org/html/2510.04569v1#Ax4 "Appendix D: eSSVI and Black–Scholes Derivatives ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂w∂θ\displaystyle\frac{\partial w}{\partial\theta} | =12​(1+ρ​ϕ​k+g),∂w∂ρ=θ2​ϕ​k​(1+1g),\displaystyle=\frac{1}{2}\Big(1+\rho\phi k+g\Big),\qquad\frac{\partial w}{\partial\rho}=\frac{\theta}{2}\,\phi k\Big(1+\frac{1}{g}\Big), |  | (27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂w∂ϕ\displaystyle\frac{\partial w}{\partial\phi} | =θ2​(ρ​k+(ϕ​k+ρ)​kg).\displaystyle=\frac{\theta}{2}\left(\rho k+\frac{(\phi k+\rho)k}{g}\right). |  |

Under our action map (θ~=θ,ρ~=ρ+ρ​-shift,ϕ~=ϕ⋅ψ​-scale\tilde{\theta}=\theta,\ \tilde{\rho}=\rho+\rho\text{-shift},\ \tilde{\phi}=\phi\cdot\psi\text{-scale}), the chain rule yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂w~∂(ρ​-shift)=∂w∂ρ|(θ~,ρ~,ϕ~),∂w~∂(ψ​-scale)=∂w∂ϕ|(θ~,ρ~,ϕ~)⋅ϕ.\frac{\partial\tilde{w}}{\partial(\rho\text{-shift})}=\left.\frac{\partial w}{\partial\rho}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})},\qquad\frac{\partial\tilde{w}}{\partial(\psi\text{-scale})}=\left.\frac{\partial w}{\partial\phi}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})}\cdot\phi. |  | (28) |

Therefore, for any parameter p∈{ρ​-shift,ψ​-scale}p\in\{\rho\text{-shift},\psi\text{-scale}\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂midm​(k)∂p=𝒱m​(k)2​σ~m​(k)​Tm⋅∂w~m​(k)∂p.\frac{\partial\,\mathrm{mid}\_{m}(k)}{\partial p}=\frac{\mathcal{V}\_{m}(k)}{2\,\tilde{\sigma}\_{m}(k)\,T\_{m}}\cdot\frac{\partial\tilde{w}\_{m}(k)}{\partial p}. |  | (29) |

#### ATM invariance.

At k=0k=0, g​(0;ρ,ϕ)=1g(0;\rho,\phi)=1 and ∂w/∂ρ=∂w/∂ϕ=0\partial w/\partial\rho=\partial w/\partial\phi=0. Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂mid∂(ρ​-shift)|k=0=∂mid∂(ψ​-scale)|k=0=0,\left.\frac{\partial\mathrm{mid}}{\partial(\rho\text{-shift})}\right|\_{k=0}=\left.\frac{\partial\mathrm{mid}}{\partial(\psi\text{-scale})}\right|\_{k=0}=0, |  | (30) |

showing that ρ\rho- and ϕ\phi-type deformations tilt the wings but do *not* change the ATM level to first order; ATM is governed by θ\theta (total variance) [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [20](https://arxiv.org/html/2510.04569v1#bib.bib20)].

### 5.2 Sensitivities of mid/ask/bid to each control

Recall ask=mid+α​St​σ~​T​s0\mathrm{ask}=\mathrm{mid}+\alpha S\_{t}\tilde{\sigma}\sqrt{T}\,s\_{0} and bid=mid−α​St​σ~​T​s0\mathrm{bid}=\mathrm{mid}-\alpha S\_{t}\tilde{\sigma}\sqrt{T}\,s\_{0} from ([15](https://arxiv.org/html/2510.04569v1#S3.E15 "In Quoting and spreads. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). For any parameter pp that affects σ~\tilde{\sigma} (e.g., ρ\rho-shift, ψ\psi-scale),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ask∂p\displaystyle\frac{\partial\,\mathrm{ask}}{\partial p} | =∂mid∂p+α​St​s0​T​∂σ~∂p=𝒱2​σ~​T​∂w~∂p+α​St​s0​T​(12​σ~​T​∂w~∂p),\displaystyle=\frac{\partial\,\mathrm{mid}}{\partial p}+\alpha S\_{t}s\_{0}\sqrt{T}\,\frac{\partial\tilde{\sigma}}{\partial p}=\frac{\mathcal{V}}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}+\alpha S\_{t}s\_{0}\sqrt{T}\left(\frac{1}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}\right), |  | (31) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂bid∂p\displaystyle\frac{\partial\,\mathrm{bid}}{\partial p} | =𝒱2​σ~​T​∂w~∂p−α​St​s0​T​(12​σ~​T​∂w~∂p).\displaystyle=\frac{\mathcal{V}}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}-\alpha S\_{t}s\_{0}\sqrt{T}\left(\frac{1}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}\right). |  |

For the half-spread α\alpha,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂mid∂α=0,∂ask∂α=St​σ~​T​s0>0,∂bid∂α=−St​σ~​T​s0<0,\frac{\partial\,\mathrm{mid}}{\partial\alpha}=0,\qquad\frac{\partial\,\mathrm{ask}}{\partial\alpha}=S\_{t}\tilde{\sigma}\sqrt{T}\,s\_{0}\ >0,\qquad\frac{\partial\,\mathrm{bid}}{\partial\alpha}=-S\_{t}\tilde{\sigma}\sqrt{T}\,s\_{0}\ <0, |  | (32) |

which formalizes the intuitive widening of quotes with α\alpha.

### 5.3 Intensity responses to controls

From ([16](https://arxiv.org/html/2510.04569v1#S3.E16 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([17](https://arxiv.org/html/2510.04569v1#S3.E17 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with ub=β​(ask−C⋆)u\_{b}=\beta(\mathrm{ask}-C^{\star}), us=β​(C⋆−bid)u\_{s}=\beta(C^{\star}-\mathrm{bid}),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂λbuy∂p\displaystyle\frac{\partial\lambda\_{\mathrm{buy}}}{\partial p} | =−λ0​w​(k)​σ′​(ub)​β​∂ask∂p,∂λsell∂p=+λ0​w​(k)​σ′​(us)​β​∂bid∂p,\displaystyle=-\lambda\_{0}\,w(k)\,\sigma^{\prime}(u\_{b})\,\beta\,\frac{\partial\mathrm{ask}}{\partial p},\qquad\frac{\partial\lambda\_{\mathrm{sell}}}{\partial p}=+\lambda\_{0}\,w(k)\,\sigma^{\prime}(u\_{s})\,\beta\,\frac{\partial\mathrm{bid}}{\partial p}, |  | (33) |

for any parameter pp that enters via the quotes (including α\alpha, ρ\rho-shift, ψ\psi-scale). Because σ′>0\sigma^{\prime}>0,

###### Proposition 3 (Monotonicity in the half-spread).

For all (m,k)(m,k), ∂λbuy/∂α<0\partial\lambda\_{\mathrm{buy}}/\partial\alpha<0 and ∂λsell/∂α<0\partial\lambda\_{\mathrm{sell}}/\partial\alpha<0. Hence both expected buy and sell volumes decrease when the half-spread increases.

###### Proof sketch.

Combine ([32](https://arxiv.org/html/2510.04569v1#S5.E32 "In 5.2 Sensitivities of mid/ask/bid to each control ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with ([33](https://arxiv.org/html/2510.04569v1#S5.E33 "In 5.3 Intensity responses to controls ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).
∎

For shape controls, the sign depends on ∂w~/∂p\partial\tilde{w}/\partial p via ([31](https://arxiv.org/html/2510.04569v1#S5.E31 "In 5.2 Sensitivities of mid/ask/bid to each control ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). At ATM, ([30](https://arxiv.org/html/2510.04569v1#S5.E30 "In ATM invariance. ‣ 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) implies ∂λbuy/∂p=∂λsell/∂p=0\partial\lambda\_{\mathrm{buy}}/\partial p=\partial\lambda\_{\mathrm{sell}}/\partial p=0 to first order, whereas OTM/ITM intensities respond through the induced skew changes.

### 5.4 Greeks and hedging: Delta & Vega sensitivities

Let Δ=∂CBS/∂S\Delta=\partial C^{\mathrm{BS}}/\partial S and Vanna=∂2CBS/(∂S​∂σ)\mathrm{Vanna}=\partial^{2}C^{\mathrm{BS}}/(\partial S\,\partial\sigma) (the cross sensitivity) [[61](https://arxiv.org/html/2510.04569v1#bib.bib61), [62](https://arxiv.org/html/2510.04569v1#bib.bib62), [63](https://arxiv.org/html/2510.04569v1#bib.bib63)]. For any parameter pp that affects σ~\tilde{\sigma},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Δ∂p\displaystyle\frac{\partial\Delta}{\partial p} | =∂Δ∂σ​∂σ~∂p=Vanna⋅12​σ~​T​∂w~∂p,\displaystyle=\frac{\partial\Delta}{\partial\sigma}\,\frac{\partial\tilde{\sigma}}{\partial p}=\mathrm{Vanna}\cdot\frac{1}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}, |  | (34) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝒱∂p\displaystyle\frac{\partial\mathcal{V}}{\partial p} | =∂𝒱∂σ​∂σ~∂p=Volga⋅12​σ~​T​∂w~∂p,Volga=∂2CBS∂σ2.\displaystyle=\frac{\partial\mathcal{V}}{\partial\sigma}\,\frac{\partial\tilde{\sigma}}{\partial p}=\mathrm{Volga}\cdot\frac{1}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p},\qquad\mathrm{Volga}=\frac{\partial^{2}C^{\mathrm{BS}}}{\partial\sigma^{2}}. |  |

Consequently, the net expected delta in ([18](https://arxiv.org/html/2510.04569v1#S3.E18 "In Hedging and P&L. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Δtnet∂p\displaystyle\frac{\partial\Delta^{\mathrm{net}}\_{t}}{\partial p} | =∑m,k(∂vsell∂p−∂vbuy∂p)⏟flow shift​ΔmBS​(k)+∑m,k(vsell−vbuy)⏟exposure⋅Vannam​(k)​12​σ~m​Tm​∂w~m​(k)∂p.\displaystyle=\sum\_{m,k}\underbrace{\Big(\frac{\partial v\_{\mathrm{sell}}}{\partial p}-\frac{\partial v\_{\mathrm{buy}}}{\partial p}\Big)}\_{\text{flow shift}}\Delta^{\mathrm{BS}}\_{m}(k)+\sum\_{m,k}\underbrace{\big(v\_{\mathrm{sell}}-v\_{\mathrm{buy}}\big)}\_{\text{exposure}}\cdot\mathrm{Vanna}\_{m}(k)\frac{1}{2\tilde{\sigma}\_{m}T\_{m}}\frac{\partial\tilde{w}\_{m}(k)}{\partial p}. |  | (35) |

The first term reflects *how the order flow moves* with a control (via ([33](https://arxiv.org/html/2510.04569v1#S5.E33 "In 5.3 Intensity responses to controls ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))); the second term is the *pure Greek effect*.

#### Hedging control.

The hedging P&L sensitivity is immediate from ([19](https://arxiv.org/html/2510.04569v1#S3.E19 "In Hedging and P&L. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂PNLthedge∂(hedget)=Δtnet​(St+1−St),\frac{\partial\,\mathrm{PNL}^{\mathrm{hedge}}\_{t}}{\partial(\mathrm{hedge}\_{t})}=\Delta^{\mathrm{net}}\_{t}\,(S\_{t+1}-S\_{t}), |  | (36) |

so the gradient sign aligns with the realized move and net delta at step tt. Over horizons, PPO/GAE (with γ<1\gamma<1) uses this local signal to adapt the hedge intensity toward volatility regimes where |Δnet||\Delta^{\mathrm{net}}| is costly.

### 5.5 Putting it together: A local Jacobian of economic signs

Collect the leading-order (per strike/maturity) sign effects:

|  |  |  |
| --- | --- | --- |
|  | Quantityαhedgeψ​-scaleρ​-shiftdualmid00±(wings; 0​at ATM)±(wings; 0​at ATM)0ask+0±±0bid−0±±0λbuy−0∓∓0λsell−0±±0Δnetambiguous0flow±/Greek±flow±/Greek±0𝒱​(Vega)00±±0Arb=BF+CAL00nonnegative drift (penalty)nonnegative drift (penalty)↓\begin{array}[]{c|ccccc}\text{Quantity}&\alpha&\mathrm{hedge}&\psi\text{-scale}&\rho\text{-shift}&\mathrm{dual}\\ \hline\cr\mathrm{mid}&0&0&\pm\ (\text{wings};\ 0\ \text{at ATM})&\pm\ (\text{wings};\ 0\ \text{at ATM})&0\\ \mathrm{ask}&+&0&\pm&\pm&0\\ \mathrm{bid}&-&0&\pm&\pm&0\\ \lambda\_{\mathrm{buy}}&-&0&\mp&\mp&0\\ \lambda\_{\mathrm{sell}}&-&0&\pm&\pm&0\\ \Delta^{\mathrm{net}}&\text{ambiguous}&0&\text{flow}\ \pm\ /\ \text{Greek}\ \pm&\text{flow}\ \pm\ /\ \text{Greek}\ \pm&0\\ \mathcal{V}\ \text{(Vega)}&0&0&\pm&\pm&0\\ \mathrm{Arb}=\mathrm{BF}+\mathrm{CAL}&0&0&\text{nonnegative drift (penalty)}&\text{nonnegative drift (penalty)}&\downarrow\end{array} |  |

*Notes:* (i) For ψ\psi-scale and ρ\rho-shift, “±\pm” depends on kk (wing) and sign​(∂w~/∂p)\mathrm{sign}(\partial\tilde{w}/\partial p) per ([28](https://arxiv.org/html/2510.04569v1#S5.E28 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); at ATM the effect is zero to first order by ([30](https://arxiv.org/html/2510.04569v1#S5.E30 "In ATM invariance. ‣ 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). (ii) The dual control decreases Arb\mathrm{Arb} via an *implicit* primal–dual mechanism (see §[4.4](https://arxiv.org/html/2510.04569v1#S4.SS4 "4.4 A state-dependent dual as a learnable Lagrange multiplier ‣ 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and the theorem in §[6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); its direct effect on quotes/Greeks is null.

### 5.6 Implications for learning and diagnostics

#### Explainability during training.

Equations ([31](https://arxiv.org/html/2510.04569v1#S5.E31 "In 5.2 Sensitivities of mid/ask/bid to each control ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([33](https://arxiv.org/html/2510.04569v1#S5.E33 "In 5.3 Intensity responses to controls ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) imply that *narrowing* spreads increases both buy- and sell-side intensities (symmetrically at ATM) and raises fill risk; shape controls then *tilt* this response across wings without moving ATM to first order. Monitoring the empirical correlation between αt\alpha\_{t} and λbuy/sell\lambda\_{\mathrm{buy/sell}} is thus a diagnostic for the intensity link.

#### Reconciling P&L and no-arbitrage.

Because Arb\mathrm{Arb} penalizes convexity/monotonicity breaches, the ψ\psi- and ρ\rho-heads should learn to *minimize* the cost
BF+CAL\mathrm{BF}+\mathrm{CAL} while allocating skew where it produces the largest marginal gain in PNLquote\mathrm{PNL}^{\mathrm{quote}}. The Jacobian in §[5.5](https://arxiv.org/html/2510.04569v1#S5.SS5 "5.5 Putting it together: A local Jacobian of economic signs ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") predicts that the optimizer prefers small wing deformations in regions where |∂w~∂p||\frac{\partial\tilde{w}}{\partial p}| is large *but* Arb\mathrm{Arb} curvature is flat.

#### Tail-sensitive adjustments.

Since CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} is computed from perturbed volumes and price moves, the chain-rule links in ([33](https://arxiv.org/html/2510.04569v1#S5.E33 "In 5.3 Intensity responses to controls ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([35](https://arxiv.org/html/2510.04569v1#S5.E35 "In 5.4 Greeks and hedging: Delta & Vega sensitivities ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) propagate ψ\psi-/ρ\rho-changes to the tail objective. Empirically, increasing λcvar\lambda\_{\mathrm{cvar}} should shift mass from aggressive spreads to larger hedge intensities when Vanna\mathrm{Vanna} indicates vulnerable wings (cf. ([34](https://arxiv.org/html/2510.04569v1#S5.E34 "In 5.4 Greeks and hedging: Delta & Vega sensitivities ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))).

#### Takeaway.

The five controls have clear economic semantics: α\alpha trades revenue for flow and inventory risk; ψ\psi-/ρ\rho-controls tilt the surface without moving ATM to first order; hedge\mathrm{hedge} directly scales exposure; and dual\mathrm{dual} adapts arbitrage pressure. The derived sensitivities provide *white-box* explanations for the learned policy and suggest diagnostics and regularizers that respect financial structure.

## 6 Theory

This section formalizes the mathematical guarantees underlying our arbitrage-consistent, risk-sensitive control scheme. We assume the notation and conditions of §[2](https://arxiv.org/html/2510.04569v1#S2 "2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–§[5](https://arxiv.org/html/2510.04569v1#S5 "5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"). Recall Assumptions [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (smoothness and bounds for the eSSVI layer) and [2](https://arxiv.org/html/2510.04569v1#Thmassumption2 "Assumption 2 (Well-posedness of the CMDP). ‣ 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (well-posedness of the CMDP). Unless stated otherwise, all expectations are taken under the policy-induced law.

### 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence

###### Theorem 2 (T1: Butterfly surrogate consistency and rate).

Fix a maturity TmT\_{m} and a compact strike interval [Kmin,Kmax][K\_{\min},K\_{\max}]. Suppose K↦C​(S,K,Tm)K\mapsto C(S,K,T\_{m}) is C3C^{3} and satisfies the continuous no-butterfly condition ∂K​KC≥0\partial\_{KK}C\geq 0 on this interval. Let {𝒦h′}\{\mathcal{K}^{\prime}\_{h}\} be evenly spaced strike lattices of mesh Δ​Kh→0\Delta K\_{h}\to 0. Then the discrete butterfly surrogate

|  |  |  |
| --- | --- | --- |
|  | BFm(h)≡1|𝒦h′|​∑K∈𝒦h′ReLU​(−ΔK2​C​(S,K,Tm)Δ​Kh2)/C¯m\mathrm{BF}\_{m}^{(h)}\equiv\frac{1}{|\mathcal{K}^{\prime}\_{h}|}\sum\_{K\in\mathcal{K}^{\prime}\_{h}}\mathrm{ReLU}\!\left(-\frac{\Delta\_{K}^{2}C(S,K,T\_{m})}{\Delta K\_{h}^{2}}\right)\Big/\bar{C}\_{m} |  |

converges to 0 with rate BFm(h)=𝒪​(Δ​Kh2)\mathrm{BF}\_{m}^{(h)}=\mathcal{O}(\Delta K\_{h}^{2}). Conversely, if there exists K0K\_{0} with ∂K​KC​(S,K0,Tm)<0\partial\_{KK}C(S,K\_{0},T\_{m})<0, then lim infh→∞BFm(h)>0\liminf\_{h\to\infty}\mathrm{BF}\_{m}^{(h)}>0. The same statements hold with softplus smoothing of the hinge, with identical rates.

###### Sketch.

Taylor’s theorem with remainder yields ΔK2​C/Δ​K2=∂K​KC​(K∗)+𝒪​(Δ​K2)\Delta\_{K}^{2}C/\Delta K^{2}=\partial\_{KK}C(K^{\ast})+\mathcal{O}(\Delta K^{2}) uniformly. If ∂K​KC≥0\partial\_{KK}C\geq 0, the negative part is of order 𝒪​(Δ​K2)\mathcal{O}(\Delta K^{2}), hence the average (after normalization) vanishes at the same rate. If curvature is negative at K0K\_{0}, uniform continuity implies a neighborhood with strictly negative curvature; the finite-difference operator detects this on fine lattices. Full proof: Appendix A.1.
∎

###### Theorem 3 (T2: Calendar surrogate consistency and rate).

Fix a strike KK and suppose T↦C​(S,K,T)T\mapsto C(S,K,T) is C2C^{2} on [T1,TM][T\_{1},T\_{M}] with ∂TC≥0\partial\_{T}C\geq 0. For evenly spaced maturity grids with mesh Δ​Th→0\Delta T\_{h}\to 0, the calendar surrogate

|  |  |  |
| --- | --- | --- |
|  | CALm(h)≡1|𝒦|​∑K∈𝒦ReLU​(C​(S,K,Tm)−C​(S,K,Tm+1))/C¯m,m+1\mathrm{CAL}\_{m}^{(h)}\equiv\frac{1}{|\mathcal{K}|}\sum\_{K\in\mathcal{K}}\mathrm{ReLU}\Big(C(S,K,T\_{m})-C(S,K,T\_{m+1})\Big)\Big/\bar{C}\_{m,m+1} |  |

satisfies maxm⁡CALm(h)=𝒪​(Δ​Th)\max\_{m}\mathrm{CAL}^{(h)}\_{m}=\mathcal{O}(\Delta T\_{h}). If there exist (K0,T0)(K\_{0},T\_{0}) with ∂TC​(S,K0,T0)<0\partial\_{T}C(S,K\_{0},T\_{0})<0, then the surrogate for the corresponding adjacent pair stays bounded away from 0 for hh large. Softplus smoothing preserves the rates.

###### Sketch.

Mean-value expansion C​(Tm+1)−C​(Tm)=∂TC​(ξ)​Δ​T+𝒪​(Δ​T2)C(T\_{m+1})-C(T\_{m})=\partial\_{T}C(\xi)\Delta T+\mathcal{O}(\Delta T^{2}) and monotonicity yield the rate; a strict violation implies a persistent positive hinge on fine grids. Full proof: Appendix A.2.
∎

### 6.2 T3: Lagrangian relaxation of the CMDP and the role of the dual action

###### Theorem 4 (T3.1: Strong duality for the CMDP).

Consider the CMDP defined by ([10](https://arxiv.org/html/2510.04569v1#S2.E10 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([11](https://arxiv.org/html/2510.04569v1#S2.E11 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with discount γ∈(0,1)\gamma\in(0,1), compact action sets, bounded measurable r,ℓ,gjr,\ell,g\_{j}, and weakly continuous P(⋅∣s,a)P(\cdot\mid s,a). Suppose there exists a strictly feasible policy (Slater condition). Then the occupancy-measure LP of the CMDP satisfies strong duality, i.e.,

|  |  |  |
| --- | --- | --- |
|  | supπinfλ≥0ℒ​(π,λ)=infλ≥0supπℒ​(π,λ),\sup\_{\pi}\ \inf\_{\lambda\geq 0}\ \mathcal{L}(\pi,\lambda)\ =\ \inf\_{\lambda\geq 0}\ \sup\_{\pi}\ \mathcal{L}(\pi,\lambda), |  |

with the Lagrangian ℒ\mathcal{L} given in ([12](https://arxiv.org/html/2510.04569v1#S2.E12 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Moreover, there exists a stationary (possibly randomized) optimal policy.

###### Sketch.

Standard reduction to an infinite-dimensional LP in occupancy measures yields convex primal and concave dual under discounting; Slater’s condition ensures zero duality gap [[48](https://arxiv.org/html/2510.04569v1#bib.bib48), [49](https://arxiv.org/html/2510.04569v1#bib.bib49)]. Existence follows by compactness and measurable selection. Full details: Appendix A.3.
∎

###### Theorem 5 (T3.2: Gradient alignment of the learnable dual with dual ascent).

Let the actor be Gaussian with a separate “dual” head dη​(s)=softplus​(νη​(s))d\_{\eta}(s)=\mathrm{softplus}(\nu\_{\eta}(s)), entering the reward as −(λarb+dη​(st))​Arbt-\big(\lambda\_{\mathrm{arb}}+d\_{\eta}(s\_{t})\big)\mathrm{Arb}\_{t}. Under Assumptions [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[2](https://arxiv.org/html/2510.04569v1#Thmassumption2 "Assumption 2 (Well-posedness of the CMDP). ‣ 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), bounded score functions, and the policy-gradient theorem [[65](https://arxiv.org/html/2510.04569v1#bib.bib65), [66](https://arxiv.org/html/2510.04569v1#bib.bib66)], the gradient of the long-run return w.r.t. η\eta satisfies

|  |  |  |
| --- | --- | --- |
|  | ∇ηJ​(η)=−𝔼π​[∑t≥0γt​A^t​σ​(νη​(st))​∇ηνη​(st)​Arbt],\nabla\_{\eta}J(\eta)\ =\ -\,\mathbb{E}\_{\pi}\!\left[\sum\_{t\geq 0}\gamma^{t}\,\hat{A}\_{t}\,\sigma\!\big(\nu\_{\eta}(s\_{t})\big)\,\nabla\_{\eta}\nu\_{\eta}(s\_{t})\ \mathrm{Arb}\_{t}\right], |  |

where A^t\hat{A}\_{t} denotes any unbiased advantage estimator. Hence the update η←η+α​∇ηJ\eta\leftarrow\eta+\alpha\nabla\_{\eta}J correlates positively with a discounted measure of violations, implementing an *implicit* dual ascent on the arbitrage constraint.

###### Sketch.

Apply the policy-gradient theorem; the only dependence of the return on η\eta is through dηd\_{\eta} and the induced trajectory distribution. The score of the dual head multiplies −Arbt-\mathrm{Arb}\_{t} in the per-step reward, yielding the stated sign structure, with advantage weighting ensuring long-run credit. See Appendix A.4 for details (including baseline/compatibility variants and boundedness of ∇ηJ\nabla\_{\eta}J).
∎

### 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability

###### Theorem 6 (T4.1: RU representation and epi-convergence).

Let XθX\_{\theta} be a real-valued loss depending on parameters θ\theta. The RU functional

|  |  |  |
| --- | --- | --- |
|  | Φq​(θ)≡infη∈ℝ{η+11−q​𝔼​(Xθ−η)−}\Phi\_{q}(\theta)\equiv\inf\_{\eta\in\mathbb{R}}\ \Big\{\ \eta+\tfrac{1}{1-q}\,\mathbb{E}(X\_{\theta}-\eta)\_{-}\ \Big\} |  |

equals CVaRq​(Xθ)\mathrm{CVaR}\_{q}(X\_{\theta}); it is convex in the distribution of XθX\_{\theta} and lower semicontinuous. If we replace (⋅)−(\cdot)\_{-} by a temperature-τ\tau softplus sτ​(⋅)s\_{\tau}(\cdot), then Φq,τ​(θ)\Phi\_{q,\tau}(\theta) epi-converges to Φq​(θ)\Phi\_{q}(\theta) as τ↓0\tau\downarrow 0 and the minimizers ητ∗\eta\_{\tau}^{\ast} converge to VaR minimizers.

###### Sketch.

Classical RU results [[29](https://arxiv.org/html/2510.04569v1#bib.bib29), [30](https://arxiv.org/html/2510.04569v1#bib.bib30)]; epi-convergence under smooth approximations follows from variational analysis [[64](https://arxiv.org/html/2510.04569v1#bib.bib64)]. Proof: Appendix A.5.
∎

###### Theorem 7 (T4.2: Differentiable CVaR estimators and gradient validity).

Consider the per-step smoothed objective CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} in ([23](https://arxiv.org/html/2510.04569v1#S3.E23 "In Scenario construction. ‣ 3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with scenario generation (v~,Δ~​S)(\tilde{v},\tilde{\Delta}S) and actions ata\_{t}. Under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), bounded intensities, and reparameterizable Gaussians for Δ~​S\tilde{\Delta}S, the gradient ∇atCVaR^q,t−\nabla\_{a\_{t}}\widehat{\mathrm{CVaR}}^{-}\_{q,t} exists and admits a mixed pathwise/likelihood-ratio estimator with finite variance for finite batches. As τ↓0\tau\downarrow 0, the gradients converge (in the sense of subgradients) to those of the nonsmooth RU functional.

###### Sketch.

Smoothness of sτs\_{\tau}, reparameterization for Δ~​S\tilde{\Delta}S, and score-function identities for Poisson v~\tilde{v} (with bounded parameters) yield unbiased estimators with finite variance [[56](https://arxiv.org/html/2510.04569v1#bib.bib56)]. Convergence as τ↓0\tau\downarrow 0 follows from [[64](https://arxiv.org/html/2510.04569v1#bib.bib64)]. Full proof: Appendix A.5.
∎

### 6.4 T5: eSSVI wing growth bound and relation to Lee’s moment constraints

###### Theorem 8 (T5: Linear wing-growth bound under a θ​ϕ\theta\phi cap).

For eSSVI at maturity TmT\_{m}, assume the cap θm​ϕm≤τmax\theta\_{m}\phi\_{m}\leq\tau\_{\max} and |ρm|≤1|\rho\_{m}|\leq 1. Then as |k|→∞|k|\to\infty,

|  |  |  |
| --- | --- | --- |
|  | lim sup|k|→∞wm​(k)|k|≤θm​|ϕm|2​(1+|ρm|)≤τmax.\limsup\_{|k|\to\infty}\frac{w\_{m}(k)}{|k|}\ \leq\ \frac{\theta\_{m}|\phi\_{m}|}{2}\,(1+|\rho\_{m}|)\ \leq\ \tau\_{\max}. |  |

Consequently, the implied variance slope wm​(k)|k|\frac{w\_{m}(k)}{|k|} is uniformly bounded by τmax\tau\_{\max}, consistent with Lee’s moment formula; in particular, enforcing τmax<2\tau\_{\max}<2 respects the Lee upper barrier for absence of explosive moments [[20](https://arxiv.org/html/2510.04569v1#bib.bib20)].

###### Sketch.

For large |k||k|, g​(k;ρ,ϕ)=(ϕ​k+ρ)2+(1−ρ2)≤|ϕ|​|k|+|ρ|g(k;\rho,\phi)=\sqrt{(\phi k+\rho)^{2}+(1-\rho^{2})}\leq|\phi||k|+|\rho|. Then

|  |  |  |
| --- | --- | --- |
|  | wm​(k)=θm2​(1+ρm​ϕm​k+g)≤θm2​(1+|ρm|​|ϕm|​|k|+|ϕm|​|k|+|ρm|),w\_{m}(k)=\tfrac{\theta\_{m}}{2}\big(1+\rho\_{m}\phi\_{m}k+g\big)\ \leq\ \tfrac{\theta\_{m}}{2}\Big(1+|\rho\_{m}||\phi\_{m}||k|+|\phi\_{m}||k|+|\rho\_{m}|\Big), |  |

so lim supwm​(k)/|k|≤θm​|ϕm|2​(1+|ρm|)≤τmax\limsup w\_{m}(k)/|k|\leq\tfrac{\theta\_{m}|\phi\_{m}|}{2}(1+|\rho\_{m}|)\leq\tau\_{\max} since (1+|ρ|)/2≤1(1+|\rho|)/2\leq 1. Full details and the connection to moment constraints: Appendix A.6.
∎

### 6.5 T6: Differentiability/boundedness ⇒\Rightarrow policy-gradient validity

###### Theorem 9 (T6: Existence and boundedness of the policy gradient).

Assume: (i) compact action sets; (ii) the actor is Gaussian with state-dependent mean and bounded log-standard deviations; (iii) rewards are bounded and C1C^{1} in actions through the eSSVI layer and smoothed surrogates (BF/CAL, CVaR), with uniform Lipschitz constants on the admissible set (Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); (iv) the Markov kernel is weakly continuous and the return is geometrically discounted. Then the policy gradient ∇ϑJ​(ϑ)\nabla\_{\vartheta}J(\vartheta) exists, is finite, and equals the standard likelihood-ratio form of the policy-gradient theorem [[65](https://arxiv.org/html/2510.04569v1#bib.bib65), [66](https://arxiv.org/html/2510.04569v1#bib.bib66)]. Moreover, ‖∇ϑJ​(ϑ)‖\|\nabla\_{\vartheta}J(\vartheta)\| is bounded on compact parameter sets, and the PPO surrogate gradient is a consistent stochastic estimator under mini-batch sampling.

###### Sketch.

Bounded rewards and discounting imply J​(ϑ)J(\vartheta) is finite. The score ∇ϑlog⁡πϑ​(z|s)\nabla\_{\vartheta}\log\pi\_{\vartheta}(z|s) is bounded due to bounded log-stds. Lipschitz continuity of the smoothed surrogates (by Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and §[3.2](https://arxiv.org/html/2510.04569v1#S3.SS2 "3.2 Discrete consistency of BF/CAL surrogates ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) yields dominated convergence, justifying interchange of gradient and expectation. The policy-gradient identity follows from [[65](https://arxiv.org/html/2510.04569v1#bib.bib65)]; boundedness on compacts is immediate. Full proof: Appendix A.7.
∎

### 6.6 P7–P8: Monotonicity and sensitivity results for interpretability

###### Proposition 4 (P7: Monotonicity of intensities in the half-spread).

With intensities ([16](https://arxiv.org/html/2510.04569v1#S3.E16 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([17](https://arxiv.org/html/2510.04569v1#S3.E17 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and σ′​(x)>0\sigma^{\prime}(x)>0, we have for all (m,k)(m,k):

|  |  |  |
| --- | --- | --- |
|  | ∂λbuy∂α=−λ0​w​(k)​σ′​(β​(ask−C⋆))​β​∂ask∂α⏟S​σ~​T​s0>0< 0,∂λsell∂α=+λ0​w​(k)​σ′​(β​(C⋆−bid))​β​∂bid∂α⏟−S​σ~​T​s0<0< 0.\frac{\partial\lambda\_{\mathrm{buy}}}{\partial\alpha}\ =\ -\lambda\_{0}\,w(k)\,\sigma^{\prime}\!\big(\beta(\mathrm{ask}-C^{\star})\big)\,\beta\,\underbrace{\frac{\partial\mathrm{ask}}{\partial\alpha}}\_{S\tilde{\sigma}\sqrt{T}\,s\_{0}>0}\ <\ 0,\\ \frac{\partial\lambda\_{\mathrm{sell}}}{\partial\alpha}\ =\ +\lambda\_{0}\,w(k)\,\sigma^{\prime}\!\big(\beta(C^{\star}-\mathrm{bid})\big)\,\beta\,\underbrace{\frac{\partial\mathrm{bid}}{\partial\alpha}}\_{-S\tilde{\sigma}\sqrt{T}\,s\_{0}<0}\ <\ 0. |  |

Hence expected buy/sell volumes are strictly decreasing in the half-spread α\alpha.

###### Sketch.

Immediate from ([32](https://arxiv.org/html/2510.04569v1#S5.E32 "In 5.2 Sensitivities of mid/ask/bid to each control ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and the chain rule in ([33](https://arxiv.org/html/2510.04569v1#S5.E33 "In 5.3 Intensity responses to controls ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Full proof: Appendix A.8.
∎

###### Proposition 5 (P8: Sensitivities of price and Greeks to ρ\rho-shift and ψ\psi-scale).

Under the eSSVI map ([1](https://arxiv.org/html/2510.04569v1#S2.E1 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and deformation ([13](https://arxiv.org/html/2510.04569v1#S3.E13 "In Action. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), for any maturity TmT\_{m} and log-moneyness kk,

|  |  |  |
| --- | --- | --- |
|  | ∂midm​(k)∂p=𝒱m​(k)2​σ~m​(k)​Tm⋅∂w~m​(k)∂p,p∈{ρ​-shift,ψ​-scale},\frac{\partial\,\mathrm{mid}\_{m}(k)}{\partial p}=\frac{\mathcal{V}\_{m}(k)}{2\,\tilde{\sigma}\_{m}(k)T\_{m}}\cdot\frac{\partial\tilde{w}\_{m}(k)}{\partial p},\qquad p\in\{\rho\text{-shift},\psi\text{-scale}\}, |  |

with ∂w~/∂p\partial\tilde{w}/\partial p given by ([28](https://arxiv.org/html/2510.04569v1#S5.E28 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). At ATM (k=0k=0) the first-order sensitivities vanish, i.e.,
∂mid/∂(ρ​-shift)=∂mid/∂(ψ​-scale)=0\partial\mathrm{mid}/\partial(\rho\text{-shift})=\partial\mathrm{mid}/\partial(\psi\text{-scale})=0,
and the corresponding Delta/Vega sensitivities obey ([34](https://arxiv.org/html/2510.04569v1#S5.E34 "In 5.4 Greeks and hedging: Delta & Vega sensitivities ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

###### Sketch.

Chain rule through w↦σ↦CBSw\mapsto\sigma\mapsto C^{\mathrm{BS}} and the eSSVI derivatives in ([27](https://arxiv.org/html/2510.04569v1#S5.E27 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). At k=0k=0 the partials in ([27](https://arxiv.org/html/2510.04569v1#S5.E27 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) vanish, yielding ATM invariance. Full proof: Appendix A.8.
∎

#### Discussion.

Theorems [2](https://arxiv.org/html/2510.04569v1#Thmtheorem2 "Theorem 2 (T1: Butterfly surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[9](https://arxiv.org/html/2510.04569v1#Thmtheorem9 "Theorem 9 (T6: Existence and boundedness of the policy gradient). ‣ 6.5 T6: Differentiability/boundedness ⇒ policy-gradient validity ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and Propositions [4](https://arxiv.org/html/2510.04569v1#Thmproposition4 "Proposition 4 (P7: Monotonicity of intensities in the half-spread). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[5](https://arxiv.org/html/2510.04569v1#Thmproposition5 "Proposition 5 (P8: Sensitivities of price and Greeks to 𝜌-shift and 𝜓-scale). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") provide a mathematically consistent backbone for our *in-the-loop* arbitrage penalties, CVaR shaping, and control semantics. In particular, T1–T2 justify the use of smoothed lattice penalties during learning; T3 connects our learnable *dual* to primal–dual optimization; T4 makes the tail objective differentiable and statistically estimable; T5 ensures wing stability consistent with Lee’s bounds; T6 legitimizes policy-gradient updates under our smooth rewards; and P7–P8 deliver *white-box* interpretability of the control heads.

## 7 Experiments (Simulation-only, Reproducible)

### 7.1 7.1 Setup and Metrics

We evaluate the proposed agent in a simulation-only regime using the calibrated *Heston fallback* configuration, consistent with §[3](https://arxiv.org/html/2510.04569v1#S3 "3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"). Eight intraday episodes are simulated, each consisting of 780 decision steps (approximately one trading day). The state transitions use the stochastic Heston dynamics:

|  |  |  |
| --- | --- | --- |
|  | d​St=μ​St​d​t+vt​St​d​WtS,d​vt=κ​(v¯−vt)​d​t+ξ​vt​d​Wtv,dS\_{t}=\mu S\_{t}\,dt+\sqrt{v\_{t}}S\_{t}\,dW\_{t}^{S},\qquad dv\_{t}=\kappa(\bar{v}-v\_{t})\,dt+\xi\sqrt{v\_{t}}\,dW\_{t}^{v}, |  |

with ρS,v=−0.5\rho\_{S,v}=-0.5 and parameters calibrated to typical SPX intraday variance.

The same architecture, hyperparameters, and annealing schedule as in Appendix [Appendix B: Implementation Details and Hyperparameters](https://arxiv.org/html/2510.04569v1#Ax2 "Appendix B: Implementation Details and Hyperparameters ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") are used throughout. The base setup uses:

|  |  |  |
| --- | --- | --- |
|  | (λ0,β,κ,s0)=(0.8,35,0.25,0.1),(\lambda\_{0},\beta,\kappa,s\_{0})=(0.8,35,0.25,0.1), |  |

with λshape:0→0.5\lambda\_{\mathrm{shape}}:0\!\to\!0.5, λarb:0→0.05\lambda\_{\mathrm{arb}}:0\!\to\!0.05, and λcvar=0.01\lambda\_{\mathrm{cvar}}=0.01 fixed.

We log both per-step and per-episode metrics:

* •

  Adjusted P&L PNLadj=PNLraw−penalties\mathrm{PNL}^{\mathrm{adj}}=\mathrm{PNL}^{\mathrm{raw}}-\text{penalties},
* •

  No-arbitrage surrogates (BF, CAL),
* •

  Shape regularization magnitude,
* •

  Tail metrics (empirical VaR5%\mathrm{VaR}\_{5\%}, CVaR5%\mathrm{CVaR}\_{5\%}),
* •

  Behavior indicators: average spread, hedge ratio, and action standard deviation.

#### Artifacts.

All experiment logs and artifacts are released for reproducibility:
artifacts/run\_log.csv, artifacts/step\_log.csv,
artifacts/artifacts.npz, and configuration file settings.json.
All figures (Figs. [1](https://arxiv.org/html/2510.04569v1#S7.F1 "Figure 1 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) are automatically generated from these artifacts.

### 7.2 7.2 Main Results

#### Revenue and stability.

Figure [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(a) shows that the agent achieves a stable improvement after episode 2, maintaining positive adjusted P&L in six of eight runs. PPO training stabilizes the exploration variance (act\_std) and avoids collapse.

#### No-arbitrage enforcement.

As shown in Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(b), calendar violations remain numerically zero throughout training, while butterfly penalties stay at the numerical floor. Shape regularization maintains values around 10−310^{-3}, indicating a smooth term-structure.

#### Tail behavior.

The per-step P&L histogram in Fig. [1](https://arxiv.org/html/2510.04569v1#S7.F1 "Figure 1 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(a) reveals a realistic left tail with VaR5%≈−1.31\mathrm{VaR}\_{5\%}\!\approx\!-1.31 and CVaR5%≈−2.16\mathrm{CVaR}\_{5\%}\!\approx\!-2.16. This tail thickness remains stable across episodes, confirming the effectiveness of the CVaR shaping.

#### Surface quality.

Figure [1](https://arxiv.org/html/2510.04569v1#S7.F1 "Figure 1 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(b) compares the quoted and true surfaces across three maturities; the shapes are virtually indistinguishable, confirming the in-loop arbitrage consistency.

#### Behavioral adaptation.

During training, the average hedge ratio increases from 0.410.41 to 0.530.53, while the mean half-spread αt\alpha\_{t} slightly declines. This indicates that the agent shifts from spread-driven revenue to active risk hedging as arbitrage penalties strengthen.

Table 1: Key metrics aggregated across 8 intraday segments.

| Metric | Value | Evidence |
| --- | --- | --- |
| Segments with PNLadj>0\mathrm{PNL}^{\mathrm{adj}}>0 | 6/8 | Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(a) |
| Calendar violation (CAL) | ≈0\approx 0 | Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(b) |
| Butterfly violation (BF) | numerical floor | Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(b) |
| Shape magnitude | 10−310^{-3} | Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(b) |
| VaR5%\mathrm{VaR}\_{5\%} | −1.31-1.31 | Fig. [1](https://arxiv.org/html/2510.04569v1#S7.F1 "Figure 1 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(a) |
| CVaR5%\mathrm{CVaR}\_{5\%} | −2.16-2.16 | Fig. [1](https://arxiv.org/html/2510.04569v1#S7.F1 "Figure 1 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(a) |
| Avg hedge ratio | 0.41→0.530.41\to 0.53 | Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(c) |
| Mean spread | slightly down | Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(c) |

### 7.3 7.3 Diagnostics and Ablations

#### Without arbitrage penalties.

Removing BF/CAL raises small local arbitrage violations and destabilizes surface smoothness, visible in Fig. [1](https://arxiv.org/html/2510.04569v1#S7.F1 "Figure 1 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(b) (deep wings diverge).

#### Without CVaR shaping.

Disabling the CVaR term thickens the left tail of the P&L distribution (heavier drawdowns), though mean returns rise slightly.

#### Without warm-start.

Training from scratch causes unstable early episodes and large variance in adjusted P&L (consistent with Fig. [2](https://arxiv.org/html/2510.04569v1#S7.F2 "Figure 2 ‣ Interpretation. ‣ 7.3 7.3 Diagnostics and Ablations ‣ 7 Experiments (Simulation-only, Reproducible) ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")(a)).

#### Interpretation.

Together these confirm that arbitrage surrogates and CVaR terms improve both *financial soundness* (surface consistency, controlled tails) and *training stability*.

![Refer to caption](pnl_hist_cvar.png)


(a) Per-step P&L distribution with tail markers (VaR5%,CVaR5%\mathrm{VaR}\_{5\%},\mathrm{CVaR}\_{5\%}).

![Refer to caption](surface_compare.png)


(b) True vs. quoted σ​(k)\sigma(k) across maturities.

Figure 1: Ex-post tail risk and surface fidelity.



![Refer to caption](training_reward_pnl.png)


(a) Training reward and adjusted P&L.

![Refer to caption](training_arb_shape.png)


(b) BF/CAL and shape penalties.

![Refer to caption](training_risk_behavior.png)


(c) Risk and behavior metrics (CVaR, hedge, spread, std).

Figure 2: Training dynamics, constraints, and behavior across episodes.

## 8 Discussion

We discuss limitations and threats to validity, then outline extensions that would strengthen external validity and broaden scope.

### 8.1 Limitations and threats to validity

#### Simulator realism and exogeneity.

Our main results are obtained in a *simulation-only* regime using a Heston fallback; ABIDES-style sources are supported but not enabled in the reported runs. Consequently, (i) order flow is exogenous and summarized by smooth intensity maps (logistic in mispricing), (ii) queue position, tick discreteness, venue fees/rebates, and latency are abstracted away, and (iii) self-impact and cross-venue liquidity fragmentation are not modeled. These choices prioritize differentiability and reproducibility, but they understate endogenous feedbacks observed in live limit-order books (cf. [[8](https://arxiv.org/html/2510.04569v1#bib.bib8), [37](https://arxiv.org/html/2510.04569v1#bib.bib37)]).

#### Static (not dynamic) arbitrage.

The BF/CAL penalties enforce *static* no-arbitrage on a finite lattice (§[3.2](https://arxiv.org/html/2510.04569v1#S3.SS2 "3.2 Discrete consistency of BF/CAL surrogates ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). They do not rule out *dynamic* arbitrage across time, nor do they capture all edge cases under extreme extrapolation. While Theorems [2](https://arxiv.org/html/2510.04569v1#Thmtheorem2 "Theorem 2 (T1: Butterfly surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[3](https://arxiv.org/html/2510.04569v1#Thmtheorem3 "Theorem 3 (T2: Calendar surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") establish lattice consistency, practical detection still depends on grid resolution and normalizers.

#### Hedging granularity and risk factors.

The hedging term uses delta only; higher-order exposures (gamma/vega/vanna) and financing constraints are not penalized in the reward. In volatile regimes, neglecting these terms may understate tail losses (§[5](https://arxiv.org/html/2510.04569v1#S5 "5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

#### Tail objective estimation.

We shape per-step tails via a smoothed RU program with small Monte Carlo batches; this is a surrogate for episode-level tail control. Estimator variance and smoothing bias are controlled but nonzero (§[3.3](https://arxiv.org/html/2510.04569v1#S3.SS3 "3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), Theorem [7](https://arxiv.org/html/2510.04569v1#Thmtheorem7 "Theorem 7 (T4.2: Differentiable CVaR estimators and gradient validity). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

#### Warm-start and sensitivity.

The supervised warm start is practically helpful but introduces a prior over the policy class. Hyperparameters (clip ϵ\epsilon, entropy, annealing schedules) affect stability; while our theory (T6) ensures gradient validity, it does not deliver global convergence guarantees.

#### Single-asset focus.

We restrict to one underlying and do not model cross-asset or cross-expiry static arbitrage simultaneously (e.g., calendar/vertical spreads across multiple names), which would require additional constraints and data.

### 8.2 Extensions and research agenda

#### Live-like microstructure.

Move to ABIDES/ABIDES-Gym as the default source and calibrate execution intensities to *queue-aware* statistics (e.g., imbalance, depth, immediate fill probabilities). Introduce explicit fees/rebates, tick size, and latency; add a propagator or resilience model to encode self-impact.

#### Point-process calibration.

Replace the parsimonious logistic map by Hawkes/ACD models estimated from data [[13](https://arxiv.org/html/2510.04569v1#bib.bib13)], preserving differentiability via reparameterized simulators or score-function estimators. This connects the intensity layer to observed clustering and reflexivity.

#### Richer risk shaping.

Augment the loss proxy ℓ\ell to include gamma/vega costs and inventory financing; test portfolio-level CVaR and spectral risk measures [[46](https://arxiv.org/html/2510.04569v1#bib.bib46), [50](https://arxiv.org/html/2510.04569v1#bib.bib50)]. Explore distributionally robust (DRO) variants where CVaR is evaluated under ambiguity sets.

#### Primal–dual algorithms.

Replace the heuristic dual head with a *trained multiplier* updated by dual ascent (RCPO/CPO) [[53](https://arxiv.org/html/2510.04569v1#bib.bib53), [52](https://arxiv.org/html/2510.04569v1#bib.bib52)] and compare with state-dependent duals. This would more tightly align practice with T3 and clarify trade-offs between feasibility and return.

#### Cross-asset and cross-constraint surfaces.

Extend eSSVI to multi-asset settings with joint static-arbitrage constraints (e.g., spread options, calendar across underlyings). Investigate neural-SDE priors informed by arbitrage-free conditions [[26](https://arxiv.org/html/2510.04569v1#bib.bib26)] and study how constraints propagate through portfolio risk.

#### Learning variants and variance reduction.

Consider natural-gradient or trust-region control [[57](https://arxiv.org/html/2510.04569v1#bib.bib57), [58](https://arxiv.org/html/2510.04569v1#bib.bib58)]; use batched antithetic sampling and control variates for CVaR (§[3.3](https://arxiv.org/html/2510.04569v1#S3.SS3 "3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) to reduce variance; evaluate off-policy baselines with safety layers.

#### Stress tests and shifts.

Benchmark under heavy tails, jumps, volatility regime switches, and correlation shocks; run adversarial tests where the latent surface deviates from the model family to probe robustness of BF/CAL surrogates and the wing cap (T5).

#### Interpretability at scale.

Leverage the sensitivities in §[5](https://arxiv.org/html/2510.04569v1#S5 "5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") to build monitors (e.g., ∂λ/∂α\partial\lambda/\partial\alpha, ATM invariance checks) and attribution tools (e.g., vanna- and volga-based diagnostics) that explain policy updates during training and in deployment-like simulations.

### 8.3 Ethics and responsible use

Our work is *simulation-only*. While our design emphasizes no-arbitrage and tail control, algorithmic market making may affect liquidity, stability, and fairness. Any transfer to live venues should include kill-switches, conservative constraints, and external stress testing. We encourage the community to report failure cases alongside average-case gains and to use open, reproducible benchmarks.

## 9 Conclusion

We proposed a *risk-sensitive, arbitrage-consistent* framework for option market making that embeds a fully differentiable eSSVI surface *inside* the learning loop. The problem is cast as a constrained MDP whose reward balances quoting/hedging revenues with smooth static no-arbitrage penalties and a CVaR tail term. We proved (i) *grid-consistency* of butterfly/calendar surrogates (T1–T2), (ii) *primal–dual* grounding of a state-dependent dual action (T3), (iii) differentiable *CVaR* estimators via the Rockafellar–Uryasev program (T4), (iv) a *wing-growth* bound aligning eSSVI with Lee’s moments (T5), and (v) *policy-gradient validity* under smooth surrogates (T6).

In simulations, the agent achieved positive adjusted P&L in most intraday segments while maintaining calendar violations at numerical zero and butterfly violations at the numerical floor, with realistic left tails. The control heads are economically interpretable: spreads trade revenue for flow, ρ\rho/ψ\psi shape the wings without moving ATM to first order, hedging scales exposure, and the dual adapts arbitrage pressure.

Beyond this paper, we envision the framework as a *benchmark* for evaluating methods that must honor pricing consistency and execution control jointly. Promising directions include ABIDES-first experiments, calibrated point-process executions, portfolio-level risk shaping, and multi-asset arbitrage constraints. We hope this work helps establish a reproducible path for *robust, interpretable AI* in quantitative markets, where financial structure and modern reinforcement learning meet in a principled way.

## Appendix A: Detailed Proofs for Section [6](https://arxiv.org/html/2510.04569v1#S6 "6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")

This appendix contains complete proofs for Theorems [2](https://arxiv.org/html/2510.04569v1#Thmtheorem2 "Theorem 2 (T1: Butterfly surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[9](https://arxiv.org/html/2510.04569v1#Thmtheorem9 "Theorem 9 (T6: Existence and boundedness of the policy gradient). ‣ 6.5 T6: Differentiability/boundedness ⇒ policy-gradient validity ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and
Propositions [4](https://arxiv.org/html/2510.04569v1#Thmproposition4 "Proposition 4 (P7: Monotonicity of intensities in the half-spread). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[5](https://arxiv.org/html/2510.04569v1#Thmproposition5 "Proposition 5 (P8: Sensitivities of price and Greeks to 𝜌-shift and 𝜓-scale). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"). We keep the notation and assumptions
from §[2](https://arxiv.org/html/2510.04569v1#S2 "2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–§[5](https://arxiv.org/html/2510.04569v1#S5 "5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"). Throughout, C​(S,K,T)C(S,K,T) denotes the
Black–Scholes (BS) call price under the quoted eSSVI surface with
T≥Tmin>0T\geq T\_{\min}>0 and σ≥σmin>0\sigma\geq\sigma\_{\min}>0 (Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).
For compactness, we write C​(K,T)≡C​(St,K,T)C(K,T)\equiv C(S\_{t},K,T) at a fixed decision time tt.

#### A.0 Regularity lemma (used repeatedly).

###### Lemma 1 (BS regularity in strikes and maturities).

Under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), for any fixed S>0S>0 and T∈[Tmin,Tmax]T\in[T\_{\min},T\_{\max}],
the function K↦C​(S,K,T,σ)K\mapsto C(S,K,T,\sigma) is C∞C^{\infty} on (0,∞)(0,\infty).
Similarly, T↦C​(S,K,T,σ)T\mapsto C(S,K,T,\sigma) is C∞C^{\infty} on [Tmin,Tmax][T\_{\min},T\_{\max}]
whenever σ​(⋅,⋅)\sigma(\cdot,\cdot) is C1C^{1} and bounded away from both 0 and ∞\infty
on its domain. Moreover, if w​(k,T)w(k,T) is C1C^{1} in (k,T)(k,T) and the eSSVI parameters
lie in a compact set satisfying ([3](https://arxiv.org/html/2510.04569v1#S2.E3 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")),
then K↦C​(S,K,T)K\mapsto C(S,K,T) and T↦C​(S,K,T)T\mapsto C(S,K,T) inherit C∞C^{\infty}–regularity
with bounded derivatives on compact subsets.

###### Proof.

Step 1 (Analyticity of the Black–Scholes formula).
For T>0T>0 and σ>0\sigma>0, define

|  |  |  |
| --- | --- | --- |
|  | d±=log⁡(S/K)±12​σ2​Tσ​T,C​(S,K,T,σ)=S​Φ​(d+)−K​Φ​(d−),d\_{\pm}=\frac{\log(S/K)\pm\frac{1}{2}\sigma^{2}T}{\sigma\sqrt{T}},\qquad C(S,K,T,\sigma)=S\Phi(d\_{+})-K\Phi(d\_{-}), |  |

where Φ\Phi is the standard normal CDF with density φ​(x)=12​π​e−x2/2\varphi(x)=\tfrac{1}{\sqrt{2\pi}}e^{-x^{2}/2}.
Each d±d\_{\pm} is analytic in (K,T,σ)(K,T,\sigma) on the open set
𝒟=(0,∞)×(0,∞)×(0,∞)\mathcal{D}=(0,\infty)\times(0,\infty)\times(0,\infty) because
log⁡(S/K)\log(S/K), σ2​T\sigma^{2}T, and (σ​T)−1(\sigma\sqrt{T})^{-1} are analytic in their arguments.
Since Φ\Phi and φ\varphi are entire, the composition and linear combination in
C​(S,K,T,σ)C(S,K,T,\sigma) preserve analyticity; thus CC is real analytic in
(K,T,σ)(K,T,\sigma) on 𝒟\mathcal{D}, implying that it is C∞C^{\infty} in all variables.

Step 2 (First- and second-order derivatives in KK).
Standard differentiation yields

|  |  |  |
| --- | --- | --- |
|  | ∂C∂K=−Φ​(d−),∂2C∂K2=φ​(d−)K​σ​T.\frac{\partial C}{\partial K}=-\Phi(d\_{-}),\qquad\frac{\partial^{2}C}{\partial K^{2}}=\frac{\varphi(d\_{-})}{K\sigma\sqrt{T}}. |  |

Because φ\varphi is bounded by 1/2​π1/\sqrt{2\pi} and
K≥Kmin>0K\geq K\_{\min}>0, σ≥σmin>0\sigma\geq\sigma\_{\min}>0, T≥Tmin>0T\geq T\_{\min}>0
under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"),

|  |  |  |
| --- | --- | --- |
|  | |∂2C∂K2|≤12​π​Kmin​σmin​Tmin.\bigg|\frac{\partial^{2}C}{\partial K^{2}}\bigg|\leq\frac{1}{\sqrt{2\pi}\,K\_{\min}\sigma\_{\min}\sqrt{T\_{\min}}}. |  |

Higher-order partial derivatives with respect to KK can be expressed as finite
linear combinations of terms of the form
K−r​Hn​(d−)​φ​(d−)​(σ​T)−sK^{-r}H\_{n}(d\_{-})\varphi(d\_{-})(\sigma\sqrt{T})^{-s}
for Hermite polynomials HnH\_{n}, hence are also bounded on compact subsets.
Therefore K↦C​(S,K,T,σ)K\mapsto C(S,K,T,\sigma) is C∞C^{\infty} with bounded derivatives
of all orders on any compact interval of (0,∞)(0,\infty).

Step 3 (Regularity in TT for fixed KK).
Differentiate CC w.r.t. TT:

|  |  |  |
| --- | --- | --- |
|  | ∂C∂T=S​σ2​T​φ​(d+)−K​σ2​T​φ​(d−)+(S​Φ′​(d+)​∂d+∂T−K​Φ′​(d−)​∂d−∂T),\frac{\partial C}{\partial T}=\frac{S\sigma}{2\sqrt{T}}\varphi(d\_{+})-\frac{K\sigma}{2\sqrt{T}}\varphi(d\_{-})+\Big(S\Phi^{\prime}(d\_{+})\,\frac{\partial d\_{+}}{\partial T}-K\Phi^{\prime}(d\_{-})\,\frac{\partial d\_{-}}{\partial T}\Big), |  |

and use Φ′=φ\Phi^{\prime}=\varphi.
Each derivative ∂Td±\partial\_{T}d\_{\pm}
is a rational function of (log⁡(S/K),T,σ)(\log(S/K),T,\sigma) whose denominator contains
(σ​T)3(\sigma\sqrt{T})^{3}, hence bounded on
𝒟cpt=[Kmin,Kmax]×[Tmin,Tmax]×[σmin,σmax]\mathcal{D}\_{\mathrm{cpt}}=[K\_{\min},K\_{\max}]\times[T\_{\min},T\_{\max}]\times[\sigma\_{\min},\sigma\_{\max}].
Because φ\varphi is bounded and smooth, every term is continuous and bounded,
and recursive differentiation shows that all higher ∂TnC\partial\_{T}^{n}C are bounded on compacts.
Hence T↦C​(S,K,T,σ)T\mapsto C(S,K,T,\sigma) is C∞C^{\infty} with bounded derivatives.

Step 4 (Composition with the implied-volatility map).
Define

|  |  |  |
| --- | --- | --- |
|  | k=log⁡(K/S),σ​(k,T)=w​(k,T)T.k=\log(K/S),\qquad\sigma(k,T)=\sqrt{\frac{w(k,T)}{T}}. |  |

Under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"),
w​(k,T)w(k,T) is C1C^{1} in (k,T)(k,T) with bounded partial derivatives, and the eSSVI
parameters belong to a compact set where θ>0\theta>0 and the
no-arbitrage constraints ([3](https://arxiv.org/html/2510.04569v1#S2.E3 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))
ensure 0<wmin≤w​(k,T)≤wmax<∞0<w\_{\min}\leq w(k,T)\leq w\_{\max}<\infty.
Therefore σ​(k,T)∈[σmin,σmax]\sigma(k,T)\in[\sigma\_{\min},\sigma\_{\max}] for some positive bounds
and is C1C^{1} (indeed analytic) on any compact subset of (k,T)(k,T).

Step 5 (Chain rule for KK- and TT-dependence).
Consider the composite mapping

|  |  |  |
| --- | --- | --- |
|  | (K,T)⟼(K,T,σ​(log⁡(K/S),T))⟼C​(S,K,T,σ​(log⁡(K/S),T)).(K,T)\ \longmapsto\ (K,T,\sigma(\log(K/S),T))\ \longmapsto\ C(S,K,T,\sigma(\log(K/S),T)). |  |

The first arrow is C∞C^{\infty} because log⁡(K/S)\log(K/S) and σ​(⋅,⋅)\sigma(\cdot,\cdot) are C∞C^{\infty},
and the second arrow is C∞C^{\infty} by Step 1.
Hence (K,T)↦C​(S,K,T)(K,T)\mapsto C(S,K,T) is C∞C^{\infty} on any compact subset of (0,∞)×[Tmin,Tmax](0,\infty)\times[T\_{\min},T\_{\max}].
Boundedness of partial derivatives follows from the chain rule:
each mixed derivative of order r+sr+s
is a finite sum of products of bounded partials of CC in (K,T,σ)(K,T,\sigma)
and bounded partials of σ​(log⁡(K/S),T)\sigma(\log(K/S),T), all uniformly bounded on compacts.
Therefore K↦C​(S,K,T)K\mapsto C(S,K,T) and T↦C​(S,K,T)T\mapsto C(S,K,T)
are C∞C^{\infty} with uniformly bounded derivatives on compact subsets.

Step 6 (Remarks on generality).
The assumption w∈C1w\in C^{1} suffices for differentiability of σ\sigma
and hence of CC.
If ww were only CrC^{r}, the conclusion would weaken to CrC^{r}
regularity, whereas for eSSVI (analytic in its parameters) we
recover full C∞C^{\infty} regularity with bounded derivatives.
This ensures that all differential operators used in
([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and Theorems [2](https://arxiv.org/html/2510.04569v1#Thmtheorem2 "Theorem 2 (T1: Butterfly surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[3](https://arxiv.org/html/2510.04569v1#Thmtheorem3 "Theorem 3 (T2: Calendar surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")
are well-defined and numerically stable.
∎

### A.1 Proof of Theorem [2](https://arxiv.org/html/2510.04569v1#Thmtheorem2 "Theorem 2 (T1: Butterfly surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (Butterfly surrogate consistency and rate)

###### Proof of Theorem [2](https://arxiv.org/html/2510.04569v1#Thmtheorem2 "Theorem 2 (T1: Butterfly surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

Fix TmT\_{m} and an evenly spaced strike lattice 𝒦h′\mathcal{K}^{\prime}\_{h} with spacing
Δ​Kh→0\Delta K\_{h}\to 0 on [Kmin,Kmax][K\_{\min},K\_{\max}]. Define the central second-difference
operator at K∈𝒦h′K\in\mathcal{K}^{\prime}\_{h} (excluding endpoints):

|  |  |  |
| --- | --- | --- |
|  | Dh(2)​C​(K)≡C​(K+Δ​Kh)−2​C​(K)+C​(K−Δ​Kh)Δ​Kh2.D\_{h}^{(2)}C(K)\ \equiv\ \frac{C(K+\Delta K\_{h})-2C(K)+C(K-\Delta K\_{h})}{\Delta K\_{h}^{2}}. |  |

By Lemma [1](https://arxiv.org/html/2510.04569v1#Thmlemma1 "Lemma 1 (BS regularity in strikes and maturities). ‣ A.0 Regularity lemma (used repeatedly). ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), K↦C​(K,Tm)K\mapsto C(K,T\_{m}) is C∞C^{\infty} on any compact
subset of (0,∞)(0,\infty) that contains the lattice; in particular C∈C4C\in C^{4} there.
The classical error expansion for central differences yields

|  |  |  |
| --- | --- | --- |
|  | Dh(2)​C​(K)=∂K​KC​(K,Tm)+Δ​Kh212​∂K​K​K​KC​(ξK,Tm),D\_{h}^{(2)}C(K)\ =\ \partial\_{KK}C(K,T\_{m})\ +\ \frac{\Delta K\_{h}^{2}}{12}\,\partial\_{KKKK}C(\xi\_{K},T\_{m}), |  |

for some ξK\xi\_{K} between K−Δ​KhK-\Delta K\_{h} and K+Δ​KhK+\Delta K\_{h} (Peano form). Hence

|  |  |  |
| --- | --- | --- |
|  | |Dh(2)​C​(K)−∂K​KC​(K,Tm)|≤Δ​Kh212​supx∈[Kmin−Δ​Kh,Kmax+Δ​Kh]|∂K​K​K​KC​(x,Tm)|=𝒪​(Δ​Kh2).\left|D\_{h}^{(2)}C(K)-\partial\_{KK}C(K,T\_{m})\right|\ \leq\ \frac{\Delta K\_{h}^{2}}{12}\,\sup\_{x\in[K\_{\min}-\Delta K\_{h},K\_{\max}+\Delta K\_{h}]}\big|\partial\_{KKKK}C(x,T\_{m})\big|\ =\ \mathcal{O}(\Delta K\_{h}^{2}). |  |

*(i) Nonnegative curvature case.)* If ∂K​KC≥0\partial\_{KK}C\geq 0 on the interval,
then Dh(2)​C​(K)≥−c​Δ​Kh2D\_{h}^{(2)}C(K)\geq-c\,\Delta K\_{h}^{2} for some c<∞c<\infty independent of KK.
Therefore the negative part satisfies (Dh(2)​C​(K))−≤c​Δ​Kh2\big(D\_{h}^{(2)}C(K)\big)\_{-}\leq c\,\Delta K\_{h}^{2},
and the averaged, normalized surrogate obeys
BFm(h)≤(c/C¯m)​Δ​Kh2=𝒪​(Δ​Kh2)\mathrm{BF}\_{m}^{(h)}\leq(c/\bar{C}\_{m})\,\Delta K\_{h}^{2}=\mathcal{O}(\Delta K\_{h}^{2}),
implying BFm(h)→0\mathrm{BF}\_{m}^{(h)}\to 0 with the claimed rate. Replacing ReLU\mathrm{ReLU}
by a softplus x↦τ​log⁡(1+ex/τ)x\mapsto\tau\log(1+e^{x/\tau}) does not affect the rate because
softplus​(−x)≤x−\mathrm{softplus}(-x)\leq x\_{-} and softplus​(−x)↓x−\mathrm{softplus}(-x)\downarrow x\_{-} as τ↓0\tau\downarrow 0 uniformly on compacts.

*(ii) Negative curvature at some point.)* If there exists K0K\_{0} with
∂K​KC​(K0,Tm)<0\partial\_{KK}C(K\_{0},T\_{m})<0, continuity of ∂K​KC\partial\_{KK}C implies a neighborhood
UU of K0K\_{0} where ∂K​KC≤−ϵ\partial\_{KK}C\leq-\epsilon for some ϵ>0\epsilon>0.
For hh small enough so that Δ​Kh<δ​(U)\Delta K\_{h}<\delta(U), the error term
Δ​Kh212​∂K​K​K​KC​(ξ)\frac{\Delta K\_{h}^{2}}{12}\partial\_{KKKK}C(\xi) is o​(1)o(1) uniformly and cannot
offset −ϵ-\epsilon. Thus Dh(2)​C​(K)≤−ϵ/2D\_{h}^{(2)}C(K)\leq-\epsilon/2 for K∈U∩𝒦h′K\in U\cap\mathcal{K}^{\prime}\_{h}
and all sufficiently small hh, producing a strictly positive average of
ReLU​(−Dh(2)​C​(K))\mathrm{ReLU}(-D\_{h}^{(2)}C(K)). Hence lim infh→∞BFm(h)>0\liminf\_{h\to\infty}\mathrm{BF}\_{m}^{(h)}>0.
∎

### A.2 Proof of Theorem [3](https://arxiv.org/html/2510.04569v1#Thmtheorem3 "Theorem 3 (T2: Calendar surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (Calendar surrogate consistency and rate)

###### Proof of Theorem [3](https://arxiv.org/html/2510.04569v1#Thmtheorem3 "Theorem 3 (T2: Calendar surrogate consistency and rate). ‣ 6.1 T1–T2: Consistency of BF/CAL surrogates and grid convergence ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

Fix S>0S>0 and a strike KK in a compact interval [Kmin,Kmax]⊂(0,∞)[K\_{\min},K\_{\max}]\subset(0,\infty),
and let {Tm}m=1M\{T\_{m}\}\_{m=1}^{M} be an evenly–spaced maturity grid on [T1,TM][T\_{1},T\_{M}] with mesh
Δ​Th=Tm+1−Tm↓0\Delta T\_{h}=T\_{m+1}-T\_{m}\downarrow 0 as h→∞h\to\infty. Denote

|  |  |  |
| --- | --- | --- |
|  | ΔT​C​(K;Tm)≡C​(S,K,Tm+1)−C​(S,K,Tm),CALm(h)≡1|𝒦|​∑K∈𝒦ReLU​(C​(S,K,Tm)−C​(S,K,Tm+1))C¯m,m+1.\Delta\_{T}C(K;T\_{m})\ \equiv\ C(S,K,T\_{m+1})-C(S,K,T\_{m}),\qquad\mathrm{CAL}^{(h)}\_{m}\ \equiv\ \frac{1}{|\mathcal{K}|}\sum\_{K\in\mathcal{K}}\frac{\mathrm{ReLU}\big(C(S,K,T\_{m})-C(S,K,T\_{m+1})\big)}{\bar{C}\_{m,m+1}}. |  |

By Lemma [1](https://arxiv.org/html/2510.04569v1#Thmlemma1 "Lemma 1 (BS regularity in strikes and maturities). ‣ A.0 Regularity lemma (used repeatedly). ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), T↦C​(S,K,T)T\mapsto C(S,K,T) is C2C^{2} on [T1,TM][T\_{1},T\_{M}]
for each K∈[Kmin,Kmax]K\in[K\_{\min},K\_{\max}], with derivatives bounded uniformly on the compact
rectangle [Kmin,Kmax]×[T1,TM][K\_{\min},K\_{\max}]\times[T\_{1},T\_{M}].333In particular,
sup(K,T)|∂TC​(S,K,T)|<∞\sup\_{(K,T)}|\partial\_{T}C(S,K,T)|<\infty and
sup(K,T)|∂T​TC​(S,K,T)|<∞\sup\_{(K,T)}|\partial\_{TT}C(S,K,T)|<\infty on this compact.
We also assume the level normalizers C¯m,m+1>0\bar{C}\_{m,m+1}>0 are uniformly bounded away from zero and above on compacts; this holds, for instance, if they are defined as averages of
{|C​(S,K,Tm)|,|C​(S,K,Tm+1)|}\{|C(S,K,T\_{m})|,|C(S,K,T\_{m+1})|\} over K∈𝒦K\in\mathcal{K} with a KK–grid that
contains an ATM neighborhood (then call prices are uniformly bounded away from 0 and SS on compacts).

(i) Monotone case: ∂TC≥0\partial\_{T}C\geq 0.
If ∂TC​(S,K,T)≥0\partial\_{T}C(S,K,T)\geq 0 for all T∈[T1,TM]T\in[T\_{1},T\_{M}] at the fixed KK, then by the mean–value theorem there exists ξm∈(Tm,Tm+1)\xi\_{m}\in(T\_{m},T\_{m+1}) such that

|  |  |  |
| --- | --- | --- |
|  | ΔT​C​(K;Tm)=∂TC​(S,K,ξm)​Δ​Th≥ 0.\Delta\_{T}C(K;T\_{m})\ =\ \partial\_{T}C(S,K,\xi\_{m})\,\Delta T\_{h}\ \geq\ 0. |  |

Equivalently, C​(S,K,Tm)−C​(S,K,Tm+1)≤0C(S,K,T\_{m})-C(S,K,T\_{m+1})\leq 0, hence
ReLU​(C​(S,K,Tm)−C​(S,K,Tm+1))=0\mathrm{ReLU}\big(C(S,K,T\_{m})-C(S,K,T\_{m+1})\big)=0 *exactly* for every mm and every KK. Averaging over KK and dividing by any positive C¯m,m+1\bar{C}\_{m,m+1} preserves zeros; thus

|  |  |  |
| --- | --- | --- |
|  | CALm(h)≡0for all ​h,m.\mathrm{CAL}^{(h)}\_{m}\equiv 0\qquad\text{for all }h,\ m. |  |

Consequently, maxm⁡CALm(h)=0→0\max\_{m}\mathrm{CAL}^{(h)}\_{m}=0\to 0 as h→∞h\to\infty.
If, instead of the hard hinge, we use the softplus smoothing sτ​(x)=τ​log⁡(1+ex/τ)s\_{\tau}(x)=\tau\log(1+e^{x/\tau}) (τ>0\tau>0) in the definition of CALm(h)\mathrm{CAL}^{(h)}\_{m}, then for all x≤0x\leq 0,
sτ​(x)≤τ​log⁡2s\_{\tau}(x)\leq\tau\log 2 and in fact sτ​(−y)≤τ​e−y/τs\_{\tau}(-y)\leq\tau e^{-y/\tau} for y≥0y\geq 0; hence the smoothed calendar penalty is uniformly bounded by O​(τ)O(\tau) and converges to 0 as τ↓0\tau\downarrow 0, uniformly in hh.

(ii) Upper bound (rate) under local Lipschitzness.
Assume only that T↦C​(S,K,T)T\mapsto C(S,K,T) is C1C^{1} with ∂TC\partial\_{T}C locally Lipschitz on [T1,TM][T\_{1},T\_{M}] for each KK (this holds by Lemma [1](https://arxiv.org/html/2510.04569v1#Thmlemma1 "Lemma 1 (BS regularity in strikes and maturities). ‣ A.0 Regularity lemma (used repeatedly). ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Then the second–order Taylor expansion yields, uniformly on compacts,

|  |  |  |
| --- | --- | --- |
|  | ΔT​C​(K;Tm)=∂TC​(S,K,Tm)​Δ​Th+12​∂T​TC​(S,K,ζm)​Δ​Th2,ζm∈(Tm,Tm+1).\Delta\_{T}C(K;T\_{m})\ =\ \partial\_{T}C(S,K,T\_{m})\,\Delta T\_{h}\ +\ \frac{1}{2}\,\partial\_{TT}C(S,K,\zeta\_{m})\,\Delta T\_{h}^{2},\quad\zeta\_{m}\in(T\_{m},T\_{m+1}). |  |

Therefore, whenever ∂TC≥0\partial\_{T}C\geq 0, any *numerical* negative part of ΔT​C\Delta\_{T}C (if it occurs due to discretization or smoothing) is at most of order O​(Δ​Th2)O(\Delta T\_{h}^{2}). After dividing by C¯m,m+1≥cnorm>0\bar{C}\_{m,m+1}\geq c\_{\mathrm{norm}}>0 and averaging over KK, we obtain the conservative bound

|  |  |  |
| --- | --- | --- |
|  | maxm⁡CALm(h)≤C​Δ​Th\max\_{m}\mathrm{CAL}^{(h)}\_{m}\ \leq\ C\,\Delta T\_{h} |  |

for some constant CC independent of hh (here we used that the number of terms scales like 1/Δ​Th1/\Delta T\_{h} when taking a maximum over mm, hence the O​(Δ​Th2)O(\Delta T\_{h}^{2}) local effect leads to an O​(Δ​Th)O(\Delta T\_{h}) global envelope). This bound is not tight in the monotone case (where the exact value is zero), but suffices for consistency.

(iii) Detection of violations: ∂TC<0\partial\_{T}C<0 somewhere.
Suppose there exist (K0,T0)(K\_{0},T\_{0}) and ε>0\varepsilon>0 such that
∂TC​(S,K0,T0)≤−ε\partial\_{T}C(S,K\_{0},T\_{0})\leq-\varepsilon.
By continuity of ∂TC\partial\_{T}C, there exists a neighborhood UK×UT⊂[Kmin,Kmax]×[T1,TM]U\_{K}\times U\_{T}\subset[K\_{\min},K\_{\max}]\times[T\_{1},T\_{M}] with K0∈UKK\_{0}\in U\_{K} and T0∈UTT\_{0}\in U\_{T} such that

|  |  |  |
| --- | --- | --- |
|  | ∂TC​(S,K,T)≤−ε2for all ​(K,T)∈UK×UT.\partial\_{T}C(S,K,T)\leq-\tfrac{\varepsilon}{2}\qquad\text{for all }(K,T)\in U\_{K}\times U\_{T}. |  |

For hh sufficiently large, the maturity mesh admits an adjacent pair (Tm,Tm+1)⊂UT(T\_{m},T\_{m+1})\subset U\_{T}; then for each K∈UKK\in U\_{K},

|  |  |  |
| --- | --- | --- |
|  | ΔT​C​(K;Tm)=∂TC​(S,K,ξm)​Δ​Th≤−ε2​Δ​Th,ξm∈(Tm,Tm+1)⊂UT.\Delta\_{T}C(K;T\_{m})=\partial\_{T}C(S,K,\xi\_{m})\,\Delta T\_{h}\leq-\tfrac{\varepsilon}{2}\,\Delta T\_{h},\quad\xi\_{m}\in(T\_{m},T\_{m+1})\subset U\_{T}. |  |

Therefore the calendar hinge is strictly positive on that pair:

|  |  |  |
| --- | --- | --- |
|  | ReLU​(C​(S,K,Tm)−C​(S,K,Tm+1))=−ΔT​C​(K;Tm)≥ε2​Δ​Th,K∈UK.\mathrm{ReLU}\big(C(S,K,T\_{m})-C(S,K,T\_{m+1})\big)=-\,\Delta\_{T}C(K;T\_{m})\ \geq\ \tfrac{\varepsilon}{2}\,\Delta T\_{h},\quad K\in U\_{K}. |  |

Averaging over the KK–grid, the contribution of the indices with K∈UKK\in U\_{K} occupies a fixed positive fraction ρK∈(0,1]\rho\_{K}\in(0,1] of the grid for all fine meshes; dividing by C¯m,m+1≤Cnorm\bar{C}\_{m,m+1}\leq C\_{\mathrm{norm}} yields

|  |  |  |
| --- | --- | --- |
|  | CALm(h)≥ρKCnorm​ε2​Δ​Th> 0for all sufficiently small ​Δ​Th.\mathrm{CAL}^{(h)}\_{m}\ \geq\ \frac{\rho\_{K}}{C\_{\mathrm{norm}}}\,\frac{\varepsilon}{2}\,\Delta T\_{h}\ >\ 0\qquad\text{for all sufficiently small }\Delta T\_{h}. |  |

Hence the violation is *detected* by a strictly positive calendar surrogate on the adjacent pair containing T0T\_{0} for all sufficiently fine grids. As Δ​Th↓0\Delta T\_{h}\downarrow 0, this lower bound scales linearly in Δ​Th\Delta T\_{h}, which is the sharp local rate implied by the mean–value theorem.

(iv) Smoothed surrogate.
If we replace ReLU\mathrm{ReLU} by the softplus sτs\_{\tau}, then in case (iii) with ΔT​C≤−(ε/2)​Δ​Th\Delta\_{T}C\leq-(\varepsilon/2)\Delta T\_{h} we get the lower bound

|  |  |  |
| --- | --- | --- |
|  | sτ​(C​(S,K,Tm)−C​(S,K,Tm+1))=sτ​(−ΔT​C​(K;Tm))≥sτ​((ε/2)​Δ​Th)≥ε4​Δ​Thfor ​Δ​Th≤2​τ,s\_{\tau}\!\big(C(S,K,T\_{m})-C(S,K,T\_{m+1})\big)=s\_{\tau}\!\big(-\Delta\_{T}C(K;T\_{m})\big)\ \geq\ s\_{\tau}\!\big((\varepsilon/2)\Delta T\_{h}\big)\ \geq\ \frac{\varepsilon}{4}\,\Delta T\_{h}\quad\text{for }\Delta T\_{h}\leq 2\tau, |  |

using sτ​(x)≥12​xs\_{\tau}(x)\geq\tfrac{1}{2}x for x∈[0,2​τ]x\in[0,2\tau].
Thus the smoothed calendar surrogate also detects violations with an O​(Δ​Th)O(\Delta T\_{h}) lower bound for sufficiently fine meshes relative to τ\tau. In the monotone case, sτ​(x)≤τ​log⁡2s\_{\tau}(x)\leq\tau\log 2 for x≤0x\leq 0, so CALm(h)≤(τ​log⁡2)/cnorm→0\mathrm{CAL}^{(h)}\_{m}\leq(\tau\log 2)/c\_{\mathrm{norm}}\to 0 as τ↓0\tau\downarrow 0, uniformly in hh.

Combining (i)–(iv) proves the claims: (a) if ∂TC≥0\partial\_{T}C\geq 0 on the interval, then maxm⁡CALm(h)→0\max\_{m}\mathrm{CAL}^{(h)}\_{m}\to 0 (indeed equals 0 for the hard hinge); (b) if there is a point where ∂TC<0\partial\_{T}C<0, then for all sufficiently fine grids the adjacent pair containing that point yields a strictly positive calendar surrogate whose magnitude is Ω​(Δ​Th)\Omega(\Delta T\_{h}), i.e., the discrete penalty consistently *detects* monotonicity violations as the mesh is refined.
∎

### A.3 Proof of Theorem [4](https://arxiv.org/html/2510.04569v1#Thmtheorem4 "Theorem 4 (T3.1: Strong duality for the CMDP). ‣ 6.2 T3: Lagrangian relaxation of the CMDP and the role of the dual action ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (CMDP strong duality)

###### Proof of Theorem [4](https://arxiv.org/html/2510.04569v1#Thmtheorem4 "Theorem 4 (T3.1: Strong duality for the CMDP). ‣ 6.2 T3: Lagrangian relaxation of the CMDP and the role of the dual action ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

We give a fully explicit occupancy–measure formulation, derive the dual LP (Bellman–type inequalities with Lagrange multipliers), and then establish zero duality gap and existence of a stationary optimal policy. We first treat the *risk–neutral* constrained MDP and then explain how the argument extends to the risk–sensitive (CVaR–augmented) objective via an epigraph reformulation.

#### Setup and notation.

Let (𝒮,𝒜)(\mathcal{S},\mathcal{A}) be Borel state and compact action spaces, P(⋅∣s,a)P(\cdot\mid s,a) a weakly continuous transition kernel, initial distribution d0d\_{0}, discount γ∈(0,1)\gamma\in(0,1), bounded measurable reward r:𝒮×𝒜→ℝr:\mathcal{S}\times\mathcal{A}\to\mathbb{R}, and bounded measurable constraint costs gj:𝒮×𝒜→ℝg\_{j}:\mathcal{S}\times\mathcal{A}\to\mathbb{R}, j=1,…,Jj=1,\dots,J. A (stationary, randomized) policy π(⋅∣s)\pi(\cdot\mid s) is a probability measure on 𝒜\mathcal{A} for each ss. Define the *discounted occupancy measure* of π\pi by

|  |  |  |
| --- | --- | --- |
|  | xπ​(B):=(1−γ)​𝔼π​[∑t=0∞γt​ 1​{(st,at)∈B}],B∈ℬ​(𝒮×𝒜).x\_{\pi}(B)\ :=\ (1-\gamma)\,\mathbb{E}\_{\pi}\!\left[\sum\_{t=0}^{\infty}\gamma^{t}\,\mathbf{1}\{(s\_{t},a\_{t})\in B\}\right],\qquad B\in\mathcal{B}(\mathcal{S}\times\mathcal{A}). |  |

If xπx\_{\pi} admits a density (w.r.t. a product reference measure), we use the same symbol xπ​(s,a)≥0x\_{\pi}(s,a)\geq 0. The marginal dπ​(s)=∫𝒜xπ​(s,a)​𝑑ad\_{\pi}(s)=\int\_{\mathcal{A}}x\_{\pi}(s,a)\,da satisfies dπ∈𝒫​(𝒮)d\_{\pi}\in\mathcal{P}(\mathcal{S}) and the *flow constraints*

|  |  |  |  |
| --- | --- | --- | --- |
|  | dπ​(s)=(1−γ)​d0​(s)+γ​∫𝒮×𝒜xπ​(s′,a′)​P​(s∣s′,a′)​𝑑s′​𝑑a′,for all ​s∈𝒮,d\_{\pi}(s)\ =\ (1-\gamma)d\_{0}(s)+\gamma\int\_{\mathcal{S}\times\mathcal{A}}x\_{\pi}(s^{\prime},a^{\prime})\,P(s\mid s^{\prime},a^{\prime})\,ds^{\prime}\,da^{\prime},\quad\text{for all }s\in\mathcal{S}, |  | (37) |

and xπ​(s,a)=dπ​(s)​π​(a∣s)x\_{\pi}(s,a)=d\_{\pi}(s)\pi(a\mid s) (disintegration). Conversely, any nonnegative measure xx on 𝒮×𝒜\mathcal{S}\times\mathcal{A} that satisfies ([37](https://arxiv.org/html/2510.04569v1#Ax1.E37 "In Setup and notation. ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) corresponds to at least one stationary randomized policy via the above disintegration (define π(⋅∣s)\pi(\cdot\mid s) arbitrarily when d​(s)=0d(s)=0).

#### Primal LP over occupancy measures.

Denote ⟨f,x⟩=∫f​(s,a)​x​(s,a)​𝑑s​𝑑a\langle f,x\rangle=\int f(s,a)\,x(s,a)\,ds\,da. The discounted CMDP can be written as the infinite–dimensional LP

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maximize | ⟨r,x⟩\displaystyle\langle r,\ x\rangle |  | (38) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to | ∫𝒜x​(s,a)​𝑑a−γ​∫𝒮×𝒜x​(s′,a′)​P​(s∣s′,a′)​𝑑s′​𝑑a′=(1−γ)​d0​(s)∀s,\displaystyle\int\_{\mathcal{A}}x(s,a)\,da-\gamma\int\_{\mathcal{S}\times\mathcal{A}}x(s^{\prime},a^{\prime})\,P(s\mid s^{\prime},a^{\prime})\,ds^{\prime}\,da^{\prime}=(1-\gamma)d\_{0}(s)\quad\forall s, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟨gj,x⟩≤εj,j=1,…,J,x≥ 0​ (measure).\displaystyle\langle g\_{j},\ x\rangle\ \leq\ \varepsilon\_{j},\quad j=1,\dots,J,\qquad x\ \geq\ 0\ \text{ (measure)}. |  |

Under boundedness and weak continuity, the feasible set is nonempty; by assumption there exists a *strictly feasible* policy (Slater’s condition): there is x0x^{0} satisfying ([37](https://arxiv.org/html/2510.04569v1#Ax1.E37 "In Setup and notation. ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and ⟨gj,x0⟩<εj\langle g\_{j},x^{0}\rangle<\varepsilon\_{j} for all jj.

#### Dual LP (Bellman inequalities with multipliers).

Introduce dual variables v:𝒮→ℝv:\mathcal{S}\to\mathbb{R} (a bounded measurable “value” function) for the flow constraints and λ∈ℝ+J\lambda\in\mathbb{R}\_{+}^{J} for the inequality constraints. The Lagrangian is

|  |  |  |
| --- | --- | --- |
|  | ℒ​(x,v,λ)=⟨r,x⟩+∑sv​(s)​[(1−γ)​d0​(s)−(∫𝒜x​(s,a)​𝑑a−γ​∫x​(s′,a′)​P​(s∣s′,a′))⏟=⁣:(𝒜​x)​(s)]−∑j=1Jλj​(⟨gj,x⟩−εj).\mathcal{L}(x,v,\lambda)\ =\ \langle r,\ x\rangle+\sum\_{s}v(s)\Big[(1-\gamma)d\_{0}(s)-\underbrace{\Big(\textstyle\int\_{\mathcal{A}}x(s,a)\,da-\gamma\!\!\int x(s^{\prime},a^{\prime})P(s\mid s^{\prime},a^{\prime})\Big)}\_{=:\,(\mathcal{A}x)(s)}\Big]\ -\ \sum\_{j=1}^{J}\lambda\_{j}(\langle g\_{j},x\rangle-\varepsilon\_{j}). |  |

Rearranging the terms depending on xx yields

|  |  |  |
| --- | --- | --- |
|  | ℒ​(x,v,λ)=(1−γ)​∑sv​(s)​d0​(s)+∑j=1Jλj​εj+∫𝒮×𝒜{r​(s,a)−∑j=1Jλj​gj​(s,a)−v​(s)+γ​𝔼​[v​(s′)∣s,a]}​x​(s,a)​𝑑s​𝑑a.\mathcal{L}(x,v,\lambda)=(1-\gamma)\sum\_{s}v(s)\,d\_{0}(s)\ +\ \sum\_{j=1}^{J}\lambda\_{j}\,\varepsilon\_{j}\ +\ \int\_{\mathcal{S}\times\mathcal{A}}\Big\{r(s,a)-\sum\_{j=1}^{J}\lambda\_{j}g\_{j}(s,a)-v(s)+\gamma\,\mathbb{E}[v(s^{\prime})\mid s,a]\Big\}\,x(s,a)\,ds\,da. |  |

Taking the supremum over x≥0x\geq 0 (measures) enforces the pointwise constraint on the integrand:

|  |  |  |
| --- | --- | --- |
|  | r​(s,a)−∑j=1Jλj​gj​(s,a)−v​(s)+γ​∫v​(s′)​P​(d​s′∣s,a)≤ 0for all ​(s,a),r(s,a)-\sum\_{j=1}^{J}\lambda\_{j}g\_{j}(s,a)-v(s)+\gamma\int v(s^{\prime})\,P(ds^{\prime}\mid s,a)\ \leq\ 0\quad\text{for all }(s,a), |  |

otherwise supx≥0ℒ=∞\sup\_{x\geq 0}\mathcal{L}=\infty. Thus the dual problem is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minimize | (1−γ)​∑sv​(s)​d0​(s)+∑j=1Jλj​εj\displaystyle(1-\gamma)\sum\_{s}v(s)d\_{0}(s)\ +\ \sum\_{j=1}^{J}\lambda\_{j}\varepsilon\_{j} |  | (39) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to | v​(s)≥r​(s,a)−∑j=1Jλj​gj​(s,a)+γ​𝔼​[v​(s′)∣s,a],∀(s,a),\displaystyle v(s)\ \geq\ r(s,a)-\sum\_{j=1}^{J}\lambda\_{j}g\_{j}(s,a)+\gamma\,\mathbb{E}[v(s^{\prime})\mid s,a],\quad\forall(s,a), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λ∈ℝ+J,v∈ℬ​(𝒮).\displaystyle\lambda\in\mathbb{R}\_{+}^{J},\qquad v\in\mathcal{B}(\mathcal{S}). |  |

These are the usual Bellman–type inequalities for the Lagrangian–modified reward rλ​(s,a)=r​(s,a)−∑jλj​gj​(s,a)r\_{\lambda}(s,a)=r(s,a)-\sum\_{j}\lambda\_{j}g\_{j}(s,a).

#### Zero duality gap.

By construction ([38](https://arxiv.org/html/2510.04569v1#Ax1.E38 "In Primal LP over occupancy measures. ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([39](https://arxiv.org/html/2510.04569v1#Ax1.E39 "In Dual LP (Bellman inequalities with multipliers). ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) form a convex primal–dual pair over a nonempty feasible set. The primal is linear in the measure xx with affine constraints (flow equalities and linear inequalities); the dual is linear in (v,λ)(v,\lambda) with linear (Bellman–type) inequalities. Under Slater’s condition (strict feasibility) and boundedness of r,gjr,g\_{j} (ensuring finite optimal value), standard infinite–dimensional LP duality for discounted MDPs implies *strong duality*:

|  |  |  |
| --- | --- | --- |
|  | supx​feasible⟨r,x⟩=infv,λ​s.t.v​satisfies ([39](https://arxiv.org/html/2510.04569v1#Ax1.E39 "In Dual LP (Bellman inequalities with multipliers). ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))(1−γ)​⟨v,d0⟩+λ⊤​ε.\sup\_{x\ \text{feasible}}\langle r,\ x\rangle\ =\ \inf\_{\begin{subarray}{c}v,\lambda\ \text{s.t.}\\ v\ \text{satisfies }\eqref{eq:dual}\end{subarray}}(1-\gamma)\,\langle v,\ d\_{0}\rangle+\lambda^{\top}\varepsilon. |  |

See [[48](https://arxiv.org/html/2510.04569v1#bib.bib48), Chs. 6–7] and [[49](https://arxiv.org/html/2510.04569v1#bib.bib49), Ch. 6]. (Sketch: the feasible set of xx is weak–∗ compact in the dual of Cb​(𝒮×𝒜)C\_{b}(\mathcal{S}\times\mathcal{A}); the constraint operator is weak–∗ continuous; Slater implies closedness of the constraint cone and zero gap via a separation theorem.)

#### Existence of a stationary optimal policy.

Let x⋆x^{\star} be a primal optimizer (which exists by compactness and upper semicontinuity of the objective on the feasible set). Define its state marginal d⋆​(s)=∫𝒜x⋆​(s,a)​𝑑ad^{\star}(s)=\int\_{\mathcal{A}}x^{\star}(s,a)\,da and a stationary policy

|  |  |  |
| --- | --- | --- |
|  | π⋆​(a∣s):={x⋆​(s,a)d⋆​(s),d⋆​(s)>0,any fixed distribution on 𝒜,d⋆​(s)=0.\pi^{\star}(a\mid s)\ :=\ \begin{cases}\frac{x^{\star}(s,a)}{d^{\star}(s)},&d^{\star}(s)>0,\\ \text{any fixed distribution on $\mathcal{A}$},&d^{\star}(s)=0.\end{cases} |  |

Then (d⋆,π⋆)(d^{\star},\pi^{\star}) satisfies the flow constraints ([37](https://arxiv.org/html/2510.04569v1#Ax1.E37 "In Setup and notation. ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), hence xπ⋆=x⋆x\_{\pi^{\star}}=x^{\star} is the occupancy measure induced by π⋆\pi^{\star}. Consequently π⋆\pi^{\star} achieves the primal optimal value ⟨r,x⋆⟩\langle r,\ x^{\star}\rangle and satisfies the constraints ⟨gj,x⋆⟩≤εj\langle g\_{j},\ x^{\star}\rangle\leq\varepsilon\_{j}. This proves the existence of an optimal stationary (possibly randomized) policy. Measurability of π⋆\pi^{\star} follows from measurable disintegration (the Radon–Nikodym derivative of x⋆x^{\star} w.r.t. its state marginal), and compactness of 𝒜\mathcal{A} guarantees that optimizing pointwise Bellman inequalities admits measurable selectors.

#### Complementary slackness and Lagrangian saddle point.

Let (v⋆,λ⋆)(v^{\star},\lambda^{\star}) solve the dual and π⋆\pi^{\star} the primal. Then, with rλ⋆=r−∑jλj⋆​gjr\_{\lambda^{\star}}=r-\sum\_{j}\lambda^{\star}\_{j}g\_{j}, the Bellman inequality is tight π⋆\pi^{\star}–a.s.:

|  |  |  |
| --- | --- | --- |
|  | v⋆(s)=rλ⋆(s,a)+γ𝔼[v⋆(s′)∣s,a],a∼π⋆(⋅∣s),v^{\star}(s)\ =\ r\_{\lambda^{\star}}(s,a)+\gamma\,\mathbb{E}[v^{\star}(s^{\prime})\mid s,a],\qquad a\sim\pi^{\star}(\cdot\mid s), |  |

and complementary slackness holds: λj⋆​(⟨gj,xπ⋆⟩−εj)=0\lambda^{\star}\_{j}\big(\langle g\_{j},x\_{\pi^{\star}}\rangle-\varepsilon\_{j}\big)=0. Therefore (π⋆,λ⋆)(\pi^{\star},\lambda^{\star}) is a *Lagrangian saddle point*, i.e.

|  |  |  |
| --- | --- | --- |
|  | ℒ​(π⋆,λ)≤ℒ​(π⋆,λ⋆)≤ℒ​(π,λ⋆),∀(π,λ≥0),\mathcal{L}(\pi^{\star},\lambda)\ \leq\ \mathcal{L}(\pi^{\star},\lambda^{\star})\ \leq\ \mathcal{L}(\pi,\lambda^{\star}),\qquad\forall(\pi,\lambda\geq 0), |  |

which is the strong–duality statement in Theorem [4](https://arxiv.org/html/2510.04569v1#Thmtheorem4 "Theorem 4 (T3.1: Strong duality for the CMDP). ‣ 6.2 T3: Lagrangian relaxation of the CMDP and the role of the dual action ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

#### Extension to the risk–sensitive (CVaR) objective.

In the main text, the objective includes a convex risk penalty λrisk​Ψ​(x)\lambda\_{\mathrm{risk}}\Psi(x), where Ψ\Psi is the (discounted) CVaR functional of the return distribution (see §[6.3](https://arxiv.org/html/2510.04569v1#S6.SS3 "6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). To keep the LP structure, one may either absorb the term into a modified reward when Ψ\Psi is linear in xx (not the case for CVaR), or use an *epigraph* reformulation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maximize | ⟨r,x⟩−λrisk​z\displaystyle\langle r,\ x\rangle\ -\ \lambda\_{\mathrm{risk}}\,z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to | flow constraints and ​x≥0,Ψ​(x)≤z,\displaystyle\text{flow constraints and }x\geq 0,\qquad\Psi(x)\ \leq\ z, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟨gj,x⟩≤εj,j=1,…,J.\displaystyle\langle g\_{j},\ x\rangle\ \leq\ \varepsilon\_{j},\ \ j=1,\dots,J. |  |

The RU program represents CVaR as a pointwise infimum of linear functionals in the loss distribution (see Theorem [6](https://arxiv.org/html/2510.04569v1#Thmtheorem6 "Theorem 6 (T4.1: RU representation and epi-convergence). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Hence Ψ\Psi is closed and convex, and the epigraph constraint is convex. Under Slater (existence of a strictly feasible (x0,z0)(x^{0},z^{0}) with Ψ​(x0)<z0\Psi(x^{0})<z^{0} and ⟨gj,x0⟩<εj\langle g\_{j},x^{0}\rangle<\varepsilon\_{j}), Fenchel–Rockafellar duality yields zero duality gap for this convex program; the dual gains an additional scalar multiplier for the epigraph constraint which recovers the “risk multiplier” λrisk\lambda\_{\mathrm{risk}} in the Lagrangian ([12](https://arxiv.org/html/2510.04569v1#S2.E12 "In 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). The rest of the proof (existence of stationary optimizers via disintegration) is unaffected because feasibility still reduces to discounted flow constraints and x≥0x\geq 0.

#### Conclusion.

We have exhibited the primal LP over occupancy measures ([38](https://arxiv.org/html/2510.04569v1#Ax1.E38 "In Primal LP over occupancy measures. ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), its Bellman–type dual ([39](https://arxiv.org/html/2510.04569v1#Ax1.E39 "In Dual LP (Bellman inequalities with multipliers). ‣ A.3 Proof of Theorem 4 (CMDP strong duality) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), strong duality under Slater’s condition, and existence of a stationary optimal policy via measurable disintegration. The risk–sensitive extension via the epigraph of CVaR preserves zero duality gap. This proves Theorem [4](https://arxiv.org/html/2510.04569v1#Thmtheorem4 "Theorem 4 (T3.1: Strong duality for the CMDP). ‣ 6.2 T3: Lagrangian relaxation of the CMDP and the role of the dual action ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").
∎

### A.4 Proof of Theorem [5](https://arxiv.org/html/2510.04569v1#Thmtheorem5 "Theorem 5 (T3.2: Gradient alignment of the learnable dual with dual ascent). ‣ 6.2 T3: Lagrangian relaxation of the CMDP and the role of the dual action ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (learnable dual alignment)

###### Proof of Theorem [5](https://arxiv.org/html/2510.04569v1#Thmtheorem5 "Theorem 5 (T3.2: Gradient alignment of the learnable dual with dual ascent). ‣ 6.2 T3: Lagrangian relaxation of the CMDP and the role of the dual action ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

Consider the policy with an independent Gaussian head for the raw dual coordinate:
z5∼𝒩​(μη​(s),σ52​(s))z\_{5}\sim\mathcal{N}(\mu\_{\eta}(s),\sigma\_{5}^{2}(s)), and dη​(s)=softplus​(z5)d\_{\eta}(s)=\mathrm{softplus}(z\_{5}).
The per-step reward contains the term
−(λarb+dη​(st))​Arbt-\big(\lambda\_{\mathrm{arb}}+d\_{\eta}(s\_{t})\big)\,\mathrm{Arb}\_{t}.
Let J​(η)J(\eta) be the discounted return. By the reparameterized policy-gradient theorem
[[65](https://arxiv.org/html/2510.04569v1#bib.bib65), [66](https://arxiv.org/html/2510.04569v1#bib.bib66)], for any unbiased advantage
estimator A^t\hat{A}\_{t},

|  |  |  |
| --- | --- | --- |
|  | ∇ηJ​(η)=𝔼​[∑t≥0γt​∇ημη​(st)​𝔼​[∂μdη​(st)|st]⏟=𝔼​[σ​(z5)|st]⋅∂rt∂dη⏟−Arbt​A^t(compat)],\nabla\_{\eta}J(\eta)\ =\ \mathbb{E}\Big[\sum\_{t\geq 0}\gamma^{t}\,\nabla\_{\eta}\mu\_{\eta}(s\_{t})\,\underbrace{\mathbb{E}\big[\partial\_{\mu}d\_{\eta}(s\_{t})\,\big|\,s\_{t}\big]}\_{=\ \mathbb{E}[\sigma(z\_{5})\,|\,s\_{t}]}\ \cdot\ \underbrace{\frac{\partial r\_{t}}{\partial d\_{\eta}}}\_{-\mathrm{Arb}\_{t}}\ \hat{A}\_{t}^{\mathrm{(compat)}}\Big], |  |

where we used ∂softplus​(x)/∂x=σ​(x)\partial\mathrm{softplus}(x)/\partial x=\sigma(x) and the compatibility
form (or, equivalently, the score-function identity for the z5z\_{5}-head).
For bounded σ5​(s)\sigma\_{5}(s), the inner expectation reduces to a smooth factor
𝔼​[σ​(z5)|st]\mathbb{E}[\sigma(z\_{5})\,|\,s\_{t}] that is lower bounded away from zero on compacts.
Hence

|  |  |  |
| --- | --- | --- |
|  | ∇ηJ​(η)=−𝔼​[∑t≥0γt​𝔼​[σ​(z5)|st]⏟positive​Arbt​∇ημη​(st)​A^t].\nabla\_{\eta}J(\eta)\ =\ -\,\mathbb{E}\left[\sum\_{t\geq 0}\gamma^{t}\,\underbrace{\mathbb{E}[\sigma(z\_{5})\,|\,s\_{t}]}\_{\text{positive}}\,\mathrm{Arb}\_{t}\,\nabla\_{\eta}\mu\_{\eta}(s\_{t})\,\hat{A}\_{t}\right]. |  |

Interpreting −Arbt​A^t-\mathrm{Arb}\_{t}\hat{A}\_{t} as a discounted measure of how increasing
the dual improves long-run return, we obtain the stated sign structure:
updates increase μη\mu\_{\eta} (hence dηd\_{\eta}) where the product
Arbt​A^t\mathrm{Arb}\_{t}\hat{A}\_{t} is positive in expectation, i.e., in regions with binding arbitration cost. Boundedness follows from bounded A^t\hat{A}\_{t} (discounted, bounded rewards) and bounded scores (finite σ5\sigma\_{5}). The same conclusion holds under the likelihood-ratio form without reparameterization.
∎

### A.5 Proofs of Theorems [6](https://arxiv.org/html/2510.04569v1#Thmtheorem6 "Theorem 6 (T4.1: RU representation and epi-convergence). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[7](https://arxiv.org/html/2510.04569v1#Thmtheorem7 "Theorem 7 (T4.2: Differentiable CVaR estimators and gradient validity). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (RU CVaR, smoothing, gradients)

###### Proof of Theorem [6](https://arxiv.org/html/2510.04569v1#Thmtheorem6 "Theorem 6 (T4.1: RU representation and epi-convergence). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

We prove (i) the Rockafellar–Uryasev (RU) representation, (ii) convexity and
lower semicontinuity, (iii) existence of minimizers, and (iv) epi-convergence
of the smoothed functional Φq,τ\Phi\_{q,\tau} to Φq\Phi\_{q} as τ↓0\tau\downarrow 0.

#### (i) RU representation.

Fix q∈(0,1)q\in(0,1) and a (real-valued) loss random variable XθX\_{\theta} indexed by a parameter θ\theta (the policy/state–action in our application). Define

|  |  |  |
| --- | --- | --- |
|  | Φq​(θ):=infη∈ℝ{η+11−q​𝔼​[(Xθ−η)−]}.\Phi\_{q}(\theta)\ :=\ \inf\_{\eta\in\mathbb{R}}\Big\{\,\eta+\frac{1}{1-q}\,\mathbb{E}\big[(X\_{\theta}-\eta)\_{-}\big]\Big\}. |  |

By [[29](https://arxiv.org/html/2510.04569v1#bib.bib29), [30](https://arxiv.org/html/2510.04569v1#bib.bib30)], Φq​(θ)=CVaRq​(Xθ)\Phi\_{q}(\theta)=\mathrm{CVaR}\_{q}(X\_{\theta}) and the set of minimizers

|  |  |  |
| --- | --- | --- |
|  | arg⁡minη⁡{η+11−q​𝔼​[(Xθ−η)−]}\arg\min\_{\eta}\ \Big\{\eta+\frac{1}{1-q}\,\mathbb{E}[(X\_{\theta}-\eta)\_{-}]\Big\} |  |

coincides with the set of qq-level VaR values (possibly an interval if the distribution has a flat segment at the qq-quantile). Moreover, any minimizer η⋆\eta^{\star} satisfies the RU first-order condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0∈ 1−11−q​ℙ​(Xθ≤η⋆)+∂Iℝ​(η⋆),0\ \in\ 1-\frac{1}{1-q}\,\mathbb{P}\big(X\_{\theta}\leq\eta^{\star}\big)\ +\ \partial I\_{\mathbb{R}}(\eta^{\star}), |  | (40) |

which reduces to ℙ​(Xθ≤η⋆)∈[1−q,1]\mathbb{P}(X\_{\theta}\leq\eta^{\star})\in[1-q,1] if the subgradient at η⋆\eta^{\star} is nonempty; when XθX\_{\theta} has a continuous distribution at level qq, the condition simplifies to ℙ​(Xθ≤η⋆)=1−q\mathbb{P}(X\_{\theta}\leq\eta^{\star})=1-q.

#### (ii) Convexity and lower semicontinuity.

For fixed η\eta, the map X↦(X−η)−X\mapsto(X-\eta)\_{-} is convex and lower semicontinuous (lsc); hence X↦𝔼​[(X−η)−]X\mapsto\mathbb{E}[(X-\eta)\_{-}] is convex in law. The infimum over η\eta of affine functionals in (η,ℒ​(X))(\eta,\mathcal{L}(X)) preserves convexity in ℒ​(X)\mathcal{L}(X), so Φq​(θ)\Phi\_{q}(\theta) is convex in the law of XθX\_{\theta}. Lower semicontinuity of Φq\Phi\_{q} in θ\theta follows from Fatou’s lemma under mild integrability (Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and bounded rewards in our setting ensure 𝔼​|Xθ|<∞\mathbb{E}|X\_{\theta}|<\infty uniformly on compact parameter sets).

#### (iii) Existence of minimizers in η\eta.

For any fixed θ\theta, the function
η↦η+11−q​𝔼​[(Xθ−η)−]\eta\mapsto\eta+\frac{1}{1-q}\mathbb{E}[(X\_{\theta}-\eta)\_{-}] is proper, convex, and coercive: as η→−∞\eta\to-\infty, the first term dominates; as η→+∞\eta\to+\infty, (Xθ−η)−→0(X\_{\theta}-\eta)\_{-}\to 0, so the objective grows like η\eta. Hence a minimizer exists and the set of minimizers is a nonempty closed interval (VaR set).

#### (iv) Epi-convergence with softplus smoothing.

Let sτ​(u)=τ​log⁡(1+eu/τ)s\_{\tau}(u)=\tau\log(1+e^{u/\tau}) be a softplus approximation of u+=max⁡{u,0}u\_{+}=\max\{u,0\} with the identities

|  |  |  |
| --- | --- | --- |
|  | 0≤sτ​(u)−u+≤τ​log⁡2,sτ′​(u)=σ​(u/τ)∈(0,1).0\ \leq\ s\_{\tau}(u)-u\_{+}\ \leq\ \tau\log 2,\qquad s\_{\tau}^{\prime}(u)=\sigma(u/\tau)\in(0,1). |  |

Define the smoothed functional

|  |  |  |
| --- | --- | --- |
|  | Φq,τ​(θ):=infη∈ℝ{η+11−q​𝔼​[sτ​(Xθ−η)]}.\Phi\_{q,\tau}(\theta)\ :=\ \inf\_{\eta\in\mathbb{R}}\left\{\eta+\frac{1}{1-q}\,\mathbb{E}\big[s\_{\tau}(X\_{\theta}-\eta)\big]\right\}. |  |

Because sτs\_{\tau} is convex and pointwise converges to u+u\_{+} as τ↓0\tau\downarrow 0, the integrand epi-converges to (Xθ−η)+(X\_{\theta}-\eta)\_{+} (equivalently, (−Xθ+η)−(-X\_{\theta}+\eta)\_{-}), uniformly on compact sets in η\eta by the bound τ​log⁡2\tau\log 2. By [[64](https://arxiv.org/html/2510.04569v1#bib.bib64), Thm. 7.33], epi-convergence is preserved under integration and infimal convolution with an affine term; therefore

|  |  |  |
| --- | --- | --- |
|  | Φq,τ→epiΦqas ​τ↓0.\Phi\_{q,\tau}\ \xrightarrow{\ \mathrm{epi}\ }\ \Phi\_{q}\qquad\text{as }\tau\downarrow 0. |  |

Consequently, any cluster point ητ⋆\eta\_{\tau}^{\star} of minimizers of the inner problem converges to the VaR set, and Φq,τ​(θ)→Φq​(θ)\Phi\_{q,\tau}(\theta)\to\Phi\_{q}(\theta).

This proves Theorem [6](https://arxiv.org/html/2510.04569v1#Thmtheorem6 "Theorem 6 (T4.1: RU representation and epi-convergence). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").
∎

###### Proof of Theorem [7](https://arxiv.org/html/2510.04569v1#Thmtheorem7 "Theorem 7 (T4.2: Differentiable CVaR estimators and gradient validity). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

We establish differentiability and a valid gradient estimator for the smoothed per-step RU objective, and then show convergence to (a selection of) the subgradient of the nonsmooth objective as τ↓0\tau\downarrow 0.

#### Setting and notation.

Fix a state–action pair (st,at)(s\_{t},a\_{t}) and define the per-step random loss

|  |  |  |
| --- | --- | --- |
|  | Lt​(ω;at):=−PNL~t​(ω;at),L\_{t}(\omega;a\_{t})\ :=\ -\,\tilde{\mathrm{PNL}}\_{t}(\omega;a\_{t}), |  |

where ω\omega collects the scenario draws. In our construction,
ω=(v~,Δ~​S)\omega=(\tilde{v},\tilde{\Delta}S) with v~∼Pois​(v​(at))\tilde{v}\sim\mathrm{Pois}(v(a\_{t})),
v:𝒜→(0,∞)v:\mathcal{A}\to(0,\infty) smooth and bounded, and
Δ~​S=Δ​S+ς​ξ\tilde{\Delta}S=\Delta S+\varsigma\xi, ξ∼𝒩​(0,1)\xi\sim\mathcal{N}(0,1) independent.
We define the smoothed RU objective at step tt:

|  |  |  |
| --- | --- | --- |
|  | hτ​(at,η):=η+11−q​𝔼ω​[sτ​(Lt​(ω;at)−η)],CVaR^q,t−​(at):=infη∈ℝhτ​(at,η).h\_{\tau}(a\_{t},\eta)\ :=\ \eta+\frac{1}{1-q}\,\mathbb{E}\_{\omega}\big[s\_{\tau}(L\_{t}(\omega;a\_{t})-\eta)\big],\qquad\widehat{\mathrm{CVaR}}^{-}\_{q,t}(a\_{t})\ :=\ \inf\_{\eta\in\mathbb{R}}h\_{\tau}(a\_{t},\eta). |  |

#### (i) Differentiability of hτh\_{\tau} in ata\_{t} and interchange of ∇\nabla and 𝔼\mathbb{E}.

Under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), the quoted surface and BS maps are C1C^{1} with bounded Jacobians; the intensity parameters v​(at)v(a\_{t}) are C1C^{1} and bounded; and sτs\_{\tau} is C1C^{1} and Lipschitz. Hence Lt​(⋅;at)L\_{t}(\cdot\,;a\_{t}) is C1C^{1} in ata\_{t} for every scenario ω\omega. Moreover there exists an integrable random bound G​(ω)G(\omega) with

|  |  |  |
| --- | --- | --- |
|  | ‖∇atLt​(ω;at)‖≤G​(ω)and𝔼​[G​(ω)]<∞,\big\|\nabla\_{a\_{t}}L\_{t}(\omega;a\_{t})\big\|\ \leq\ G(\omega)\quad\text{and}\quad\mathbb{E}[G(\omega)]<\infty, |  |

because LtL\_{t} is a composition of bounded Lipschitz maps (quotes, Greeks, intensities) applied to bounded random inputs (Poisson with bounded mean and Gaussian with fixed variance). Then, by dominated convergence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇athτ​(at,η)=11−q​𝔼​[sτ′​(Lt​(ω;at)−η)​∇atLt​(ω;at)].\nabla\_{a\_{t}}h\_{\tau}(a\_{t},\eta)\ =\ \frac{1}{1-q}\,\mathbb{E}\!\left[s\_{\tau}^{\prime}\!\big(L\_{t}(\omega;a\_{t})-\eta\big)\,\nabla\_{a\_{t}}L\_{t}(\omega;a\_{t})\right]. |  | (41) |

Since sτ′∈(0,1)s\_{\tau}^{\prime}\in(0,1), the integrand is integrable.

#### (ii) Mixed pathwise / likelihood-ratio (LR) gradient.

Write ω=(v~,ξ)\omega=(\tilde{v},\xi) with ξ∼𝒩​(0,1)\xi\sim\mathcal{N}(0,1) and v~∼Pois​(v​(at))\tilde{v}\sim\mathrm{Pois}(v(a\_{t})). For any integrable f​(v~,ξ)f(\tilde{v},\xi),

|  |  |  |
| --- | --- | --- |
|  | ∇at𝔼v~,ξ​[f]=𝔼v~,ξ​[∇atf​(v~,ξ)]+𝔼v~,ξ​[f​(v~,ξ)​∇atlog⁡pv~​(v~;at)],\nabla\_{a\_{t}}\,\mathbb{E}\_{\tilde{v},\xi}[f]\ =\ \mathbb{E}\_{\tilde{v},\xi}\Big[\nabla\_{a\_{t}}f(\tilde{v},\xi)\Big]\ +\ \mathbb{E}\_{\tilde{v},\xi}\Big[f(\tilde{v},\xi)\,\nabla\_{a\_{t}}\log p\_{\tilde{v}}(\tilde{v};a\_{t})\Big], |  |

where pv~p\_{\tilde{v}} is the Poisson pmf with parameter v​(at)v(a\_{t}) and
∇atlog⁡pv~​(v~;at)=(v~−v​(at))​∇atlog⁡v​(at)\nabla\_{a\_{t}}\log p\_{\tilde{v}}(\tilde{v};a\_{t})=(\tilde{v}-v(a\_{t}))\,\nabla\_{a\_{t}}\log v(a\_{t}).
Applying this to the integrand in ([41](https://arxiv.org/html/2510.04569v1#Ax1.E41 "In (i) Differentiability of ℎ_𝜏 in 𝑎_𝑡 and interchange of ∇ and 𝔼. ‣ A.5 Proofs of Theorems 6–7 (RU CVaR, smoothing, gradients) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and using the pathwise derivative for the Gaussian perturbation (reparameterization trick) yields the implementable estimator:

|  |  |  |
| --- | --- | --- |
|  | ∇athτ​(at,η)=11−q​𝔼​[sτ′​(Lt−η)​(∇atLt⏟pathwise in ​ξ+Lt​∇atlog⁡pv~​(v~;at)⏟LR in ​v~)].\nabla\_{a\_{t}}h\_{\tau}(a\_{t},\eta)=\frac{1}{1-q}\,\mathbb{E}\!\left[s\_{\tau}^{\prime}\!\big(L\_{t}-\eta\big)\,\Big(\underbrace{\nabla\_{a\_{t}}L\_{t}}\_{\text{pathwise in }\xi}\ +\ \underbrace{L\_{t}\,\nabla\_{a\_{t}}\log p\_{\tilde{v}}(\tilde{v};a\_{t})}\_{\text{LR in }\tilde{v}}\Big)\right]. |  |

Boundedness of sτ′s\_{\tau}^{\prime} and of the Poisson score (since v​(at)v(a\_{t}) is bounded away from ∞\infty and from 0 on the admissible set) ensures finite Monte Carlo variance for finite batch sizes.

#### (iii) Differentiability of the *minimized* smoothed objective.

Define ητ⋆​(at)∈arg⁡minη⁡hτ​(at,η)\eta^{\star}\_{\tau}(a\_{t})\in\arg\min\_{\eta}h\_{\tau}(a\_{t},\eta). The function hτh\_{\tau} is strictly convex in η\eta (as sτs\_{\tau} is strictly convex), and ∂ηhτ​(at,η)=1−11−q​𝔼​[sτ′​(Lt​(ω;at)−η)]\partial\_{\eta}h\_{\tau}(a\_{t},\eta)=1-\frac{1}{1-q}\,\mathbb{E}[s\_{\tau}^{\prime}(L\_{t}(\omega;a\_{t})-\eta)] is continuous and strictly increasing in η\eta; hence ητ⋆​(at)\eta^{\star}\_{\tau}(a\_{t}) is unique and continuous in ata\_{t} by the implicit function theorem. By Danskin’s envelope theorem (for unconstrained, unique inner minimizers),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇atCVaR^q,t−​(at)=∇athτ​(at,ητ⋆​(at))=11−q​𝔼​[sτ′​(Lt−ητ⋆​(at))​∇atLt],\nabla\_{a\_{t}}\ \widehat{\mathrm{CVaR}}^{-}\_{q,t}(a\_{t})=\nabla\_{a\_{t}}\ h\_{\tau}\big(a\_{t},\eta^{\star}\_{\tau}(a\_{t})\big)=\frac{1}{1-q}\,\mathbb{E}\big[s\_{\tau}^{\prime}\!\big(L\_{t}-\eta^{\star}\_{\tau}(a\_{t})\big)\,\nabla\_{a\_{t}}L\_{t}\big], |  | (42) |

with the mixed pathwise/LR form as above.

#### (iv) Limit as τ↓0\tau\downarrow 0: convergence to a (sub)gradient of RU.

As τ↓0\tau\downarrow 0, sτ​(u)↓u+s\_{\tau}(u)\downarrow u\_{+} and sτ′​(u)→𝟏​{u>0}s\_{\tau}^{\prime}(u)\to\mathbf{1}\{u>0\} pointwise. Moreover, by Theorem [6](https://arxiv.org/html/2510.04569v1#Thmtheorem6 "Theorem 6 (T4.1: RU representation and epi-convergence). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), ητ⋆​(at)→η⋆​(at)∈VaRq\eta^{\star}\_{\tau}(a\_{t})\to\eta^{\star}(a\_{t})\in\mathrm{VaR}\_{q} (possibly a set; any selection suffices). Using dominated convergence and the boundedness of ∇atLt\nabla\_{a\_{t}}L\_{t}, ([42](https://arxiv.org/html/2510.04569v1#Ax1.E42 "In (iii) Differentiability of the minimized smoothed objective. ‣ A.5 Proofs of Theorems 6–7 (RU CVaR, smoothing, gradients) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) converges to

|  |  |  |
| --- | --- | --- |
|  | limτ↓0∇atCVaR^q,t−​(at)=11−q​𝔼​[𝟏​{Lt>η⋆​(at)}​∇atLt],\lim\_{\tau\downarrow 0}\ \nabla\_{a\_{t}}\ \widehat{\mathrm{CVaR}}^{-}\_{q,t}(a\_{t})=\frac{1}{1-q}\,\mathbb{E}\big[\mathbf{1}\{L\_{t}>\eta^{\star}(a\_{t})\}\,\nabla\_{a\_{t}}L\_{t}\big], |  |

which is a valid selection from the subdifferential of the nonsmooth RU functional (when the cdf has a flat segment at η⋆\eta^{\star}, one obtains a set of subgradients corresponding to indicator values in [0,1][0,1] on the tie set {Lt=η⋆}\{L\_{t}=\eta^{\star}\}). This matches the well-known CVaR gradient identity used in risk-sensitive reinforcement learning [[32](https://arxiv.org/html/2510.04569v1#bib.bib32), [33](https://arxiv.org/html/2510.04569v1#bib.bib33), [34](https://arxiv.org/html/2510.04569v1#bib.bib34)].

#### (v) Practical estimator and variance control.

A finite-sample, unbiased estimator follows by Monte Carlo with NN scenarios:

|  |  |  |
| --- | --- | --- |
|  | ∇^at​CVaR^q,t−=1(1−q)​N​∑i=1Nsτ′​(Lt(i)−η^τ⋆)​(∇atLt(i)+Lt(i)​∇atlog⁡pv~​(v~(i);at)),\widehat{\nabla}\_{a\_{t}}\ \widehat{\mathrm{CVaR}}^{-}\_{q,t}=\frac{1}{(1-q)N}\sum\_{i=1}^{N}s\_{\tau}^{\prime}\!\big(L\_{t}^{(i)}-\hat{\eta}^{\star}\_{\tau}\big)\,\Big(\nabla\_{a\_{t}}L\_{t}^{(i)}+L\_{t}^{(i)}\,\nabla\_{a\_{t}}\log p\_{\tilde{v}}(\tilde{v}^{(i)};a\_{t})\Big), |  |

where η^τ⋆\hat{\eta}^{\star}\_{\tau} minimizes the sample objective
η+1(1−q)​N​∑isτ​(Lt(i)−η)\eta+\frac{1}{(1-q)N}\sum\_{i}s\_{\tau}(L\_{t}^{(i)}-\eta). Antithetic sampling for the Gaussian part and a state-dependent control variate for the LR term (subtracting a baseline) reduce variance [[56](https://arxiv.org/html/2510.04569v1#bib.bib56)]. As τ↓0\tau\downarrow 0 and N→∞N\to\infty, the estimator converges in probability to the RU subgradient above.

This proves Theorem [7](https://arxiv.org/html/2510.04569v1#Thmtheorem7 "Theorem 7 (T4.2: Differentiable CVaR estimators and gradient validity). ‣ 6.3 T4: Rockafellar–Uryasev CVaR, smoothing, and differentiability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").
∎

### A.6 Proof of Theorem [8](https://arxiv.org/html/2510.04569v1#Thmtheorem8 "Theorem 8 (T5: Linear wing-growth bound under a 𝜃⁢ϕ cap). ‣ 6.4 T5: eSSVI wing growth bound and relation to Lee’s moment constraints ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (eSSVI wing-growth bound and Lee)

###### Proof of Theorem [8](https://arxiv.org/html/2510.04569v1#Thmtheorem8 "Theorem 8 (T5: Linear wing-growth bound under a 𝜃⁢ϕ cap). ‣ 6.4 T5: eSSVI wing growth bound and relation to Lee’s moment constraints ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

Recall the (per-maturity) eSSVI total variance

|  |  |  |
| --- | --- | --- |
|  | w​(k)=θ2​(1+ρ​ϕ​k+g​(k;ρ,ϕ)),g​(k;ρ,ϕ):=(ϕ​k+ρ)2+(1−ρ2).w(k)\;=\;\frac{\theta}{2}\Big(1+\rho\,\phi\,k\;+\;g(k;\rho,\phi)\Big),\qquad g(k;\rho,\phi)\;:=\;\sqrt{(\phi k+\rho)^{2}+(1-\rho^{2})}\,. |  |

We establish a sharp linear upper bound for w​(k)w(k) as |k|→∞|k|\to\infty and then connect it to Lee’s moment constraints.

#### Step 1: Two–sided elementary bounds for g​(k;ρ,ϕ)g(k;\rho,\phi).

Set a:=ϕ​k+ρa:=\phi k+\rho and b:=1−ρ2∈[0,1]b:=1-\rho^{2}\in[0,1]. For any a≠0a\neq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |a|≤a2+b≤|a|+b2​|a|.|a|\ \leq\ \sqrt{a^{2}+b}\ \leq\ |a|+\frac{b}{2|a|}\,. |  | (43) |

The left inequality is trivial; the right follows from a2+b−|a|=ba2+b+|a|≤b2​|a|\sqrt{a^{2}+b}-|a|=\frac{b}{\sqrt{a^{2}+b}+|a|}\leq\frac{b}{2|a|}. With a=ϕ​k+ρa=\phi k+\rho and b=1−ρ2b=1-\rho^{2}, ([43](https://arxiv.org/html/2510.04569v1#Ax1.E43 "In Step 1: Two–sided elementary bounds for 𝑔⁢(𝑘;𝜌,ϕ). ‣ A.6 Proof of Theorem 8 (eSSVI wing-growth bound and Lee) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ϕ​k+ρ|≤g​(k;ρ,ϕ)≤|ϕ​k+ρ|+1−ρ22​|ϕ​k+ρ|.|\phi k+\rho|\ \leq\ g(k;\rho,\phi)\ \leq\ |\phi k+\rho|\;+\;\frac{1-\rho^{2}}{2\,|\phi k+\rho|}\,. |  | (44) |

#### Step 2: Asymptotic upper bound for w​(k)/|k|w(k)/|k|.

Using ([44](https://arxiv.org/html/2510.04569v1#Ax1.E44 "In Step 1: Two–sided elementary bounds for 𝑔⁢(𝑘;𝜌,ϕ). ‣ A.6 Proof of Theorem 8 (eSSVI wing-growth bound and Lee) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")),

|  |  |  |
| --- | --- | --- |
|  | w​(k)|k|=θ2​|k|​(1+ρ​ϕ​k+g​(k;ρ,ϕ))≤θ2​|k|​(1+ρ​ϕ​k+|ϕ​k+ρ|+1−ρ22​|ϕ​k+ρ|).\frac{w(k)}{|k|}\;=\;\frac{\theta}{2|k|}\Big(1+\rho\phi k+g(k;\rho,\phi)\Big)\;\leq\;\frac{\theta}{2|k|}\Big(1+\rho\phi k+|\phi k+\rho|+\frac{1-\rho^{2}}{2|\phi k+\rho|}\Big). |  |

Since |ϕ​k+ρ|≤|ϕ|​|k|+|ρ||\phi k+\rho|\leq|\phi|\,|k|+|\rho| and ρ​ϕ​k≤|ρ|​|ϕ|​|k|\rho\phi k\leq|\rho|\,|\phi|\,|k|, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | w​(k)|k|\displaystyle\frac{w(k)}{|k|} | ≤θ2​(1|k|+|ρ|​|ϕ|+|ϕ|+|ρ||k|+1−ρ22​|k|​|ϕ​k+ρ|)\displaystyle\leq\frac{\theta}{2}\left(\frac{1}{|k|}+|\rho|\,|\phi|+|\phi|+\frac{|\rho|}{|k|}+\frac{1-\rho^{2}}{2|k|\,|\phi k+\rho|}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =θ​|ϕ|2​(1+|ρ|)+θ2​(1+|ρ||k|+1−ρ22​|k|​|ϕ​k+ρ|)⏟→ 0​ as ​|k|⁣→∞.\displaystyle=\frac{\theta|\phi|}{2}\,(1+|\rho|)\;+\;\underbrace{\frac{\theta}{2}\left(\frac{1+|\rho|}{|k|}+\frac{1-\rho^{2}}{2|k|\,|\phi k+\rho|}\right)}\_{\to\,0\ \text{ as }\ |k|\to\infty}. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim sup|k|→∞w​(k)|k|≤θ​|ϕ|2​(1+|ρ|).\limsup\_{|k|\to\infty}\frac{w(k)}{|k|}\ \leq\ \frac{\theta|\phi|}{2}\,(1+|\rho|)\,. |  | (45) |

#### Step 3: Uniformity over parameter compacts and the cap.

Under the eSSVI admissibility and compactness assumptions (Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") together with ([3](https://arxiv.org/html/2510.04569v1#S2.E3 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))), we have |ρ|≤1|\rho|\leq 1 and the wing cap θ​ϕ≤τmax\theta\phi\leq\tau\_{\max} (with θ>0\theta>0, ϕ≥0\phi\geq 0). Therefore,

|  |  |  |
| --- | --- | --- |
|  | θ​|ϕ|2​(1+|ρ|)≤θ​ϕ2⋅2=θ​ϕ≤τmax,\frac{\theta|\phi|}{2}\,(1+|\rho|)\ \leq\ \frac{\theta\phi}{2}\cdot 2\ =\ \theta\phi\ \leq\ \tau\_{\max}\,, |  |

and ([45](https://arxiv.org/html/2510.04569v1#Ax1.E45 "In Step 2: Asymptotic upper bound for 𝑤⁢(𝑘)/|𝑘|. ‣ A.6 Proof of Theorem 8 (eSSVI wing-growth bound and Lee) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) implies the *uniform* bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim sup|k|→∞w​(k)|k|≤τmax.\limsup\_{|k|\to\infty}\frac{w(k)}{|k|}\ \leq\ \tau\_{\max}\,. |  | (46) |

Because the parameter set is compact and the remainder in Step 2 is uniform on compacts (the denominator |ϕ​k+ρ||\phi k+\rho| grows like |k||k| whenever |k||k| is large), the same bound holds uniformly across maturities whose parameters lie in the same compact admissible set.

#### Step 4: One–sided limits k→±∞k\to\pm\infty (optional refinement).

By applying ([44](https://arxiv.org/html/2510.04569v1#Ax1.E44 "In Step 1: Two–sided elementary bounds for 𝑔⁢(𝑘;𝜌,ϕ). ‣ A.6 Proof of Theorem 8 (eSSVI wing-growth bound and Lee) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) separately on k→+∞k\to+\infty and k→−∞k\to-\infty, one also gets

|  |  |  |
| --- | --- | --- |
|  | lim supk→+∞w​(k)k≤θ​ϕ2​(1+ρ),lim supk→−∞w​(k)−k≤θ​ϕ2​(1−ρ),\limsup\_{k\to+\infty}\frac{w(k)}{k}\ \leq\ \frac{\theta\phi}{2}\,(1+\rho),\qquad\limsup\_{k\to-\infty}\frac{w(k)}{-k}\ \leq\ \frac{\theta\phi}{2}\,(1-\rho), |  |

and hence max⁡{lim supk→+∞w​(k)/k,lim supk→−∞w​(k)/(−k)}≤θ​|ϕ|2​(1+|ρ|)\max\{\limsup\_{k\to+\infty}w(k)/k,\ \limsup\_{k\to-\infty}w(k)/(-k)\}\leq\frac{\theta|\phi|}{2}(1+|\rho|). This refinement is sometimes convenient when mapping to the right/left Lee slopes.

#### Step 5: Connection to Lee’s moment formula.

Lee [[20](https://arxiv.org/html/2510.04569v1#bib.bib20)] shows that the (total) implied variance wings obey

|  |  |  |
| --- | --- | --- |
|  | lim supk→+∞w​(k)k≤ψR,lim supk→−∞w​(k)−k≤ψL,\limsup\_{k\to+\infty}\frac{w(k)}{k}\ \leq\ \psi\_{R},\qquad\limsup\_{k\to-\infty}\frac{w(k)}{-k}\ \leq\ \psi\_{L}, |  |

with ψR,ψL∈[0,2]\psi\_{R},\psi\_{L}\in[0,2] determined by the highest finite moments of the risk–neutral distribution (precisely, ψ=2−2​1+α\psi=2-2\sqrt{1+\alpha} when 𝔼​[ST1+α]<∞\mathbb{E}[S\_{T}^{1+\alpha}]<\infty). In particular, any *no–moment–explosion* configuration enforces ψR,ψL≤2\psi\_{R},\psi\_{L}\leq 2. Our bound ([46](https://arxiv.org/html/2510.04569v1#Ax1.E46 "In Step 3: Uniformity over parameter compacts and the cap. ‣ A.6 Proof of Theorem 8 (eSSVI wing-growth bound and Lee) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) shows that imposing the cap θ​ϕ≤τmax\theta\phi\leq\tau\_{\max} with

|  |  |  |
| --- | --- | --- |
|  | τmax<2\tau\_{\max}<2 |  |

forces both right and left slopes to lie strictly below the Lee barrier 22, uniformly across maturities in the admissible set, and hence is *consistent* with moment finiteness and precludes pathological wing explosions. This directly motivates the cap in ([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) as an in–the–loop regularization that aligns the learned surface with Lee’s asymptotic constraints.

#### Step 6: Finite–kk uniform bound (explicit ε\varepsilon–control).

For completeness, given any ε>0\varepsilon>0 there exists Kε<∞K\_{\varepsilon}<\infty such that for all |k|≥Kε|k|\geq K\_{\varepsilon},

|  |  |  |
| --- | --- | --- |
|  | w​(k)|k|≤θ​|ϕ|2​(1+|ρ|)+ε.\frac{w(k)}{|k|}\ \leq\ \frac{\theta|\phi|}{2}(1+|\rho|)\ +\ \varepsilon\,. |  |

Indeed, take KεK\_{\varepsilon} so that 1+|ρ||k|≤ε\frac{1+|\rho|}{|k|}\leq\varepsilon and 1−ρ22​|k|​|ϕ​k+ρ|≤ε\frac{1-\rho^{2}}{2|k||\phi k+\rho|}\leq\varepsilon for all |k|≥Kε|k|\geq K\_{\varepsilon}; this choice is uniform over the parameter compact (because the latter controls |ρ||\rho| and ensures |ϕ||\phi| is bounded away from infinity and, if desired, from zero on the admissible region).

Combining Steps 1–6 proves the theorem.
∎

### A.7 Proof of Theorem [9](https://arxiv.org/html/2510.04569v1#Thmtheorem9 "Theorem 9 (T6: Existence and boundedness of the policy gradient). ‣ 6.5 T6: Differentiability/boundedness ⇒ policy-gradient validity ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (policy-gradient existence and boundedness)

###### Proof of Theorem [9](https://arxiv.org/html/2510.04569v1#Thmtheorem9 "Theorem 9 (T6: Existence and boundedness of the policy gradient). ‣ 6.5 T6: Differentiability/boundedness ⇒ policy-gradient validity ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

We prove that (i) the discounted return J​(ϑ)J(\vartheta) is finite and measurable on compact parameter sets; (ii) the likelihood–ratio (LR) policy–gradient identity holds and ∇ϑJ​(ϑ)\nabla\_{\vartheta}J(\vartheta) exists; (iii) ‖∇ϑJ​(ϑ)‖\|\nabla\_{\vartheta}J(\vartheta)\| is bounded on compacts; and (iv) the PPO surrogate gradient is a consistent estimator.

#### Preliminaries and notation.

Let {πϑ(⋅∣s):ϑ∈Θ}\{\pi\_{\vartheta}(\cdot\mid s):\vartheta\in\Theta\} be a Gaussian policy with state–dependent mean and diagonal standard deviations whose logs are clamped in [log⁡σmin,log⁡σmax][\log\sigma\_{\min},\log\sigma\_{\max}] uniformly in ϑ\vartheta. Let (st,at)​\_​t≥0(s\_{t},a\_{t})\\_{t\geq 0} be the Markov process induced by πϑ\pi\_{\vartheta} and kernel P(⋅∣s,a)P(\cdot\mid s,a) (weakly continuous by Assumption [2](https://arxiv.org/html/2510.04569v1#Thmassumption2 "Assumption 2 (Well-posedness of the CMDP). ‣ 2.5 Constrained MDP (cmdp) formulation ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Rewards are bounded and C1C^{1} in the action via the composition

|  |  |  |
| --- | --- | --- |
|  | rt=r​(st,at,st+1)=PNLquote+PNLhedge⏟BS/eSSVI C1−λshape​Shape−(λarb+dual)​(BF+CAL)−λcvar​CVaR^q,t−,r\_{t}\;=\;r(s\_{t},a\_{t},s\_{t+1})\;=\;\underbrace{\mathrm{PNL}^{\mathrm{quote}}+\mathrm{PNL}^{\mathrm{hedge}}}\_{\text{BS/eSSVI $C^{1}$}}\;-\;\lambda\_{\mathrm{shape}}\mathrm{Shape}-\;(\lambda\_{\mathrm{arb}}+\mathrm{dual})\,(\mathrm{BF}+\mathrm{CAL})-\;\lambda\_{\mathrm{cvar}}\widehat{\mathrm{CVaR}}^{-}\_{q,t}, |  |

where BF,CAL\mathrm{BF},\mathrm{CAL} use softplus smoothing (Appendix [Appendix E: Smoothed BF/CAL Penalties and Lipschitz Bounds](https://arxiv.org/html/2510.04569v1#Ax5 "Appendix E: Smoothed BF/CAL Penalties and Lipschitz Bounds ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} is the smoothed RU objective (Appendix [A.5 Proofs of Theorems 6–7 (RU CVaR, smoothing, gradients)](https://arxiv.org/html/2510.04569v1#Ax1.SSx5 "A.5 Proofs of Theorems 6–7 (RU CVaR, smoothing, gradients) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Denote the discounted return G=∑t≥0γt​rtG=\sum\_{t\geq 0}\gamma^{t}r\_{t} and value J​(ϑ)=𝔼ϑ​[G]J(\vartheta)=\mathbb{E}\_{\vartheta}[G].

#### Step 1: J​(ϑ)J(\vartheta) is finite and measurable on compacts.

By bounded rewards |rt|≤Rmax|r\_{t}|\leq R\_{\max} a.s. and γ∈(0,1)\gamma\in(0,1),

|  |  |  |
| --- | --- | --- |
|  | |J​(ϑ)|≤𝔼ϑ​[∑t≥0γt​|rt|]≤Rmax1−γ<∞.|J(\vartheta)|\;\leq\;\mathbb{E}\_{\vartheta}\Big[\sum\_{t\geq 0}\gamma^{t}|r\_{t}|\Big]\;\leq\;\frac{R\_{\max}}{1-\gamma}\;<\infty. |  |

Measurability of JJ in ϑ\vartheta follows from the dominated convergence theorem (DCT) because the trajectory law depends continuously on ϑ\vartheta (weak continuity of PP, continuity of πϑ\pi\_{\vartheta}, compact Θ\Theta) and |G|≤Rmax/(1−γ)|G|\leq R\_{\max}/(1-\gamma).

#### Step 2: LR policy–gradient identity and existence.

Write the trajectory density under ϑ\vartheta as

|  |  |  |
| --- | --- | --- |
|  | pϑ​(τ)=d0​(s0)​∏t≥0πϑ​(at∣st)​P​(st+1∣st,at),τ=(s0,a0,s1,a1,…).p\_{\vartheta}(\tau)\;=\;d\_{0}(s\_{0})\prod\_{t\geq 0}\pi\_{\vartheta}(a\_{t}\mid s\_{t})\,P(s\_{t+1}\mid s\_{t},a\_{t}),\qquad\tau=(s\_{0},a\_{0},s\_{1},a\_{1},\ldots). |  |

Assumptions ensure πϑ​(a∣s)>0\pi\_{\vartheta}(a\mid s)>0 for all actions (Gaussian with bounded std) and PP independent of ϑ\vartheta. Then

|  |  |  |
| --- | --- | --- |
|  | ∇ϑJ​(ϑ)=∇ϑ​∫G​(τ)​pϑ​(τ)​𝑑τ=∫G​(τ)​pϑ​(τ)​∇ϑlog⁡pϑ​(τ)​𝑑τ=𝔼ϑ​[G​(τ)​∑t≥0∇ϑlog⁡πϑ​(at∣st)],\nabla\_{\vartheta}J(\vartheta)=\nabla\_{\vartheta}\int G(\tau)\,p\_{\vartheta}(\tau)\,d\tau=\int G(\tau)\,p\_{\vartheta}(\tau)\,\nabla\_{\vartheta}\log p\_{\vartheta}(\tau)\,d\tau=\mathbb{E}\_{\vartheta}\!\left[\,G(\tau)\sum\_{t\geq 0}\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\_{t}\mid s\_{t})\,\right], |  |

where interchange of ∇\nabla and ∫\int is justified by DCT as follows. The score ∇ϑlog⁡πϑ​(a∣s)\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\mid s) is uniformly bounded on Θ\Theta:
for a diagonal Gaussian with stds in [σmin,σmax][\sigma\_{\min},\sigma\_{\max}],

|  |  |  |
| --- | --- | --- |
|  | ∥∇ϑlogπϑ(a∣s)∥=∥∇ϑ[−12∑i(ai−μi)2σi2−∑ilogσi]∥≤Cπ\left\|\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\mid s)\right\|=\left\|\nabla\_{\vartheta}\left[-\tfrac{1}{2}\sum\_{i}\tfrac{(a\_{i}-\mu\_{i})^{2}}{\sigma\_{i}^{2}}-\sum\_{i}\log\sigma\_{i}\right]\right\|\leq C\_{\pi} |  |

for some CπC\_{\pi} (bounded mean and log-std networks on a compact parameter set).
Thus

|  |  |  |
| --- | --- | --- |
|  | |G(τ)∑t≥0∇ϑlogπϑ(at∣st)|≤Rmax1−γ∑t≥0∥∇ϑlogπϑ(at∣st)∥≤Rmax1−γ∑t≥0Cπγt=Cπ​Rmax(1−γ)2,\left|G(\tau)\sum\_{t\geq 0}\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\_{t}\mid s\_{t})\right|\leq\frac{R\_{\max}}{1-\gamma}\,\sum\_{t\geq 0}\|\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\_{t}\mid s\_{t})\|\leq\frac{R\_{\max}}{1-\gamma}\,\sum\_{t\geq 0}C\_{\pi}\,\gamma^{t}=\frac{C\_{\pi}R\_{\max}}{(1-\gamma)^{2}}, |  |

where we used that adding a γt\gamma^{t} factor is standard after centering with a baseline (see below); otherwise one can apply the equivalent state–action value form with QπQ^{\pi} to absorb the discount. Hence DCT applies, proving existence and the LR form.

A variance–reduced form is obtained by subtracting a baseline b​(st)b(s\_{t}):

|  |  |  |
| --- | --- | --- |
|  | ∇ϑJ​(ϑ)=𝔼ϑ​[∑t≥0γt​∇ϑlog⁡πϑ​(at∣st)​(Qπ​(st,at)−b​(st))],\nabla\_{\vartheta}J(\vartheta)=\mathbb{E}\_{\vartheta}\Bigg[\sum\_{t\geq 0}\gamma^{t}\,\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\_{t}\mid s\_{t})\,\big(Q^{\pi}(s\_{t},a\_{t})-b(s\_{t})\big)\Bigg], |  |

with QπQ^{\pi} the discounted state–action value. Choosing b​(s)=Vπ​(s)b(s)=V^{\pi}(s) yields the advantage AπA^{\pi}; bounded rewards imply |Qπ|≤Rmax/(1−γ)|Q^{\pi}|\leq R\_{\max}/(1-\gamma) and |Aπ|≤2​Rmax/(1−γ)|A^{\pi}|\leq 2R\_{\max}/(1-\gamma).

#### Step 3: Boundedness of ∇ϑJ​(ϑ)\nabla\_{\vartheta}J(\vartheta) on compacts.

Using the advantage form with any bounded baseline,

|  |  |  |
| --- | --- | --- |
|  | ∥∇ϑJ(ϑ)∥≤𝔼ϑ[∑t≥0γt∥∇ϑlogπϑ(at∣st)∥|Aπ(st,at)|]≤∑t≥0γtCπ2​Rmax1−γ=2​Cπ​Rmax(1−γ)2.\big\|\nabla\_{\vartheta}J(\vartheta)\big\|\leq\mathbb{E}\_{\vartheta}\left[\sum\_{t\geq 0}\gamma^{t}\,\|\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\_{t}\mid s\_{t})\|\,|A^{\pi}(s\_{t},a\_{t})|\right]\leq\sum\_{t\geq 0}\gamma^{t}\,C\_{\pi}\,\frac{2R\_{\max}}{1-\gamma}=\frac{2C\_{\pi}R\_{\max}}{(1-\gamma)^{2}}. |  |

Thus the gradient norm is bounded uniformly in ϑ∈Θ\vartheta\in\Theta (compact).

#### Step 4: Why rtr\_{t} is C1C^{1} and Lipschitz in actions.

Each reward component is a C1C^{1} composition with bounded Jacobians on the admissible set (Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")):

* •

  BS/eSSVI pricing and Greeks are C∞C^{\infty} (Lemma [1](https://arxiv.org/html/2510.04569v1#Thmlemma1 "Lemma 1 (BS regularity in strikes and maturities). ‣ A.0 Regularity lemma (used repeatedly). ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") and Appendix [Appendix D: eSSVI and Black–Scholes Derivatives](https://arxiv.org/html/2510.04569v1#Ax4 "Appendix D: eSSVI and Black–Scholes Derivatives ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); the action deformations (ψ​-scale,ρ​-shift)(\psi\text{-scale},\rho\text{-shift}) enter linearly and the wing cap is implemented via a smooth rescaling.
* •

  BF,CAL\mathrm{BF},\mathrm{CAL} use softplus smoothing of finite–difference operators (Appendix [Appendix E: Smoothed BF/CAL Penalties and Lipschitz Bounds](https://arxiv.org/html/2510.04569v1#Ax5 "Appendix E: Smoothed BF/CAL Penalties and Lipschitz Bounds ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), hence C1C^{1} and locally Lipschitz in the eSSVI parameters, thus in actions by chain rule.
* •

  CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} is the smoothed RU value with a unique inner minimizer ητ⋆​(at)\eta\_{\tau}^{\star}(a\_{t}); Danskin’s theorem (Appendix [A.5 Proofs of Theorems 6–7 (RU CVaR, smoothing, gradients)](https://arxiv.org/html/2510.04569v1#Ax1.SSx5 "A.5 Proofs of Theorems 6–7 (RU CVaR, smoothing, gradients) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) gives C1C^{1} dependence on ata\_{t} and bounded gradient via mixed pathwise/LR estimators.

Therefore rtr\_{t} is C1C^{1} and globally Lipschitz in actions on the admissible set with constant LrL\_{r}.

#### Step 5: PPO surrogate gradient consistency.

Consider the PPO objective

|  |  |  |
| --- | --- | --- |
|  | ℒPPO​(ϑ)=𝔼​[min⁡(rt​(ϑ)​A^t,clip​(rt​(ϑ),1−ϵ,1+ϵ)​A^t)]−cv​𝔼​(Vω−R^)2+cℋ​𝔼​ℋ​(πϑ),\mathcal{L}\_{\mathrm{PPO}}(\vartheta)=\mathbb{E}\Big[\min\big(r\_{t}(\vartheta)\,\hat{A}\_{t},\ \mathrm{clip}(r\_{t}(\vartheta),1-\epsilon,1+\epsilon)\,\hat{A}\_{t}\big)\Big]-c\_{v}\,\mathbb{E}(V\_{\omega}-\hat{R})^{2}+c\_{\mathcal{H}}\,\mathbb{E}\mathcal{H}(\pi\_{\vartheta}), |  |

with importance ratio rt​(ϑ)=πϑ​(at∣st)/πϑold​(at∣st)r\_{t}(\vartheta)=\pi\_{\vartheta}(a\_{t}\mid s\_{t})/\pi\_{\vartheta\_{\mathrm{old}}}(a\_{t}\mid s\_{t}), advantage estimator A^t\hat{A}\_{t}, and ϵ∈(0,1)\epsilon\in(0,1). The clipping enforces

|  |  |  |
| --- | --- | --- |
|  | |rt​(ϑ)​A^t−clip​(rt​(ϑ),1−ϵ,1+ϵ)​A^t|≤2​ϵ​|A^t|.|r\_{t}(\vartheta)\hat{A}\_{t}-\mathrm{clip}(r\_{t}(\vartheta),1-\epsilon,1+\epsilon)\hat{A}\_{t}|\leq 2\epsilon\,|\hat{A}\_{t}|. |  |

Since |A^t|≤CA:=2​Rmax/(1−γ)|\hat{A}\_{t}|\leq C\_{A}:=2R\_{\max}/(1-\gamma) (bounded–reward GAE with λ∈[0,1]\lambda\in[0,1]), the per–sample contribution to ∇ϑℒPPO\nabla\_{\vartheta}\mathcal{L}\_{\mathrm{PPO}} is uniformly bounded by a constant depending on (ϵ,CA,Cπ)(\epsilon,C\_{A},C\_{\pi}). Under standard regularity (weak continuity of PP, continuity of πϑ\pi\_{\vartheta}), the law of minibatches converges weakly as batch size →∞\to\infty; the boundedness and continuity of the integrand imply that the empirical gradient converges in probability to the population gradient (uniform law of large numbers). Moreover, when ϵ↓0\epsilon\downarrow 0, the clipped surrogate gradient approaches the LR gradient of J​(ϑ)J(\vartheta); for fixed small ϵ\epsilon, the bias is controlled by the bound above and vanishes as training steps shrink (trust–region interpretation).

#### Step 6: Interchanging limits and gradients.

For completeness, we justify interchanging (i) the ∇ϑ\nabla\_{\vartheta} operator with the infinite discounted sum and (ii) expectations. Because |rt|≤Rmax|r\_{t}|\leq R\_{\max} and ‖∇ϑlog⁡πϑ‖≤Cπ\|\nabla\_{\vartheta}\log\pi\_{\vartheta}\|\leq C\_{\pi}, we have

|  |  |  |
| --- | --- | --- |
|  | ∑t≥0γt𝔼[∥∇ϑlogπϑ(at∣st)∥|Qπ(st,at)|]≤∑t≥0γtCπRmax1−γ=Cπ​Rmax(1−γ)2<∞,\sum\_{t\geq 0}\gamma^{t}\,\mathbb{E}\big[\|\nabla\_{\vartheta}\log\pi\_{\vartheta}(a\_{t}\mid s\_{t})\|\ |Q^{\pi}(s\_{t},a\_{t})|\big]\leq\sum\_{t\geq 0}\gamma^{t}\,C\_{\pi}\frac{R\_{\max}}{1-\gamma}=\frac{C\_{\pi}R\_{\max}}{(1-\gamma)^{2}}\,<\infty, |  |

so Fubini–Tonelli and dominated convergence apply to exchange ∇\nabla, ∑\sum, and 𝔼\mathbb{E}. This completes the proof.

#### Conclusion.

We have shown that J​(ϑ)J(\vartheta) is finite and differentiable with LR gradient; the gradient norm is uniformly bounded on compact Θ\Theta; and PPO’s clipped surrogate gradient is a consistent estimator with controlled bias/variance. Hence Theorem [9](https://arxiv.org/html/2510.04569v1#Thmtheorem9 "Theorem 9 (T6: Existence and boundedness of the policy gradient). ‣ 6.5 T6: Differentiability/boundedness ⇒ policy-gradient validity ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") holds.
∎

### A.8 Proofs of Propositions [4](https://arxiv.org/html/2510.04569v1#Thmproposition4 "Proposition 4 (P7: Monotonicity of intensities in the half-spread). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")–[5](https://arxiv.org/html/2510.04569v1#Thmproposition5 "Proposition 5 (P8: Sensitivities of price and Greeks to 𝜌-shift and 𝜓-scale). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (monotonicity and sensitivities)

###### Proof of Proposition [4](https://arxiv.org/html/2510.04569v1#Thmproposition4 "Proposition 4 (P7: Monotonicity of intensities in the half-spread). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (Monotonicity in the half-spread).

Recall the half–spread mapping ([15](https://arxiv.org/html/2510.04569v1#S3.E15 "In Quoting and spreads. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))
spread​(m,k)2=α​St​σ~m​(k)​Tm​s0,\frac{\mathrm{spread}(m,k)}{2}=\alpha\,S\_{t}\,\tilde{\sigma}\_{m}(k)\sqrt{T\_{m}}\,s\_{0},
and the identities in ([32](https://arxiv.org/html/2510.04569v1#S5.E32 "In 5.2 Sensitivities of mid/ask/bid to each control ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")):
∂mid/∂α=0,∂ask/∂α=St​σ~​T​s0>0,∂bid/∂α=−St​σ~​T​s0<0.\partial\mathrm{mid}/\partial\alpha=0,\ \partial\mathrm{ask}/\partial\alpha=S\_{t}\tilde{\sigma}\sqrt{T}\,s\_{0}>0,\ \partial\mathrm{bid}/\partial\alpha=-S\_{t}\tilde{\sigma}\sqrt{T}\,s\_{0}<0.
With ub=β​(ask−C⋆)u\_{b}=\beta(\mathrm{ask}-C^{\star}) and us=β​(C⋆−bid)u\_{s}=\beta(C^{\star}-\mathrm{bid}), and using
the intensity maps ([16](https://arxiv.org/html/2510.04569v1#S3.E16 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([17](https://arxiv.org/html/2510.04569v1#S3.E17 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) together with
σ′​(x)>0\sigma^{\prime}(x)>0 (logistic derivative), we get

|  |  |  |
| --- | --- | --- |
|  | ∂λbuy∂α=−λ0​w​(k)​σ′​(ub)​β​∂ask∂α<0,∂λsell∂α=+λ0​w​(k)​σ′​(us)​β​∂bid∂α<0,\frac{\partial\lambda\_{\mathrm{buy}}}{\partial\alpha}=-\lambda\_{0}w(k)\,\sigma^{\prime}(u\_{b})\,\beta\,\frac{\partial\mathrm{ask}}{\partial\alpha}<0,\qquad\frac{\partial\lambda\_{\mathrm{sell}}}{\partial\alpha}=+\lambda\_{0}w(k)\,\sigma^{\prime}(u\_{s})\,\beta\,\frac{\partial\mathrm{bid}}{\partial\alpha}<0, |  |

since w​(k)>0w(k)>0, β>0\beta>0, and the signs of the α\alpha–derivatives of quotes are fixed.
Therefore both expected buy and sell intensities decrease strictly with α\alpha. This
holds pointwise for each (m,k)(m,k) and is uniform on compact parameter domains by
Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").
∎

###### Proof of Proposition [5](https://arxiv.org/html/2510.04569v1#Thmproposition5 "Proposition 5 (P8: Sensitivities of price and Greeks to 𝜌-shift and 𝜓-scale). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (Sensitivities to ρ\rho-shift and ψ\psi-scale).

The statement consists of three parts: (i) a chain–rule identity for the sensitivity
of the mid price to a shape control parameter p∈{ρ​-shift,ψ​-scale}p\in\{\rho\text{-shift},\psi\text{-scale}\};
(ii) ATM invariance (k=0k=0) of first–order effects; and (iii) corresponding Delta/Vega
sensitivities.

#### (i) Chain–rule for mid sensitivity.

Let w~m​(k)\tilde{w}\_{m}(k) denote the total variance from the *quoted* (action–deformed)
eSSVI parameters (θ~,ρ~,ψ~)(\tilde{\theta},\tilde{\rho},\tilde{\psi}); σ~m​(k)=w~m​(k)/Tm\tilde{\sigma}\_{m}(k)=\sqrt{\tilde{w}\_{m}(k)/T\_{m}}; and
midm(k)=CBS(St,K=Stek,Tm,σ~m(k)).\mathrm{mid}\_{m}(k)=C^{\mathrm{BS}}(S\_{t},K=S\_{t}e^{k},T\_{m},\tilde{\sigma}\_{m}(k)).
By the BS chain rule (Appendix [Appendix D: eSSVI and Black–Scholes Derivatives](https://arxiv.org/html/2510.04569v1#Ax4 "Appendix D: eSSVI and Black–Scholes Derivatives ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), writing 𝒱m​(k)=∂CBS/∂σ\mathcal{V}\_{m}(k)=\partial C^{\mathrm{BS}}/\partial\sigma,

|  |  |  |
| --- | --- | --- |
|  | ∂midm​(k)∂p=∂CBS∂σ⋅∂σ~m​(k)∂p=𝒱m​(k)⋅12​σ~m​(k)​Tm⋅∂w~m​(k)∂p,\frac{\partial\,\mathrm{mid}\_{m}(k)}{\partial p}=\frac{\partial C^{\mathrm{BS}}}{\partial\sigma}\cdot\frac{\partial\tilde{\sigma}\_{m}(k)}{\partial p}=\mathcal{V}\_{m}(k)\cdot\frac{1}{2\,\tilde{\sigma}\_{m}(k)\,T\_{m}}\cdot\frac{\partial\tilde{w}\_{m}(k)}{\partial p}, |  |

which is exactly ([29](https://arxiv.org/html/2510.04569v1#S5.E29 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). It remains to compute ∂w~/∂p\partial\tilde{w}/\partial p.
Using the eSSVI derivatives ([27](https://arxiv.org/html/2510.04569v1#S5.E27 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), the action deformation ([13](https://arxiv.org/html/2510.04569v1#S3.E13 "In Action. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))
yields

|  |  |  |
| --- | --- | --- |
|  | ∂w~m​(k)∂(ρ​-shift)=∂w∂ρ|(θ~,ρ~,ϕ~),∂w~m​(k)∂(ψ​-scale)=∂w∂ϕ|(θ~,ρ~,ϕ~)⋅ϕ,\frac{\partial\tilde{w}\_{m}(k)}{\partial(\rho\text{-shift})}=\left.\frac{\partial w}{\partial\rho}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})},\qquad\frac{\partial\tilde{w}\_{m}(k)}{\partial(\psi\text{-scale})}=\left.\frac{\partial w}{\partial\phi}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})}\cdot\phi, |  |

which is ([28](https://arxiv.org/html/2510.04569v1#S5.E28 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Substituting into the chain rule completes (i).

#### (ii) ATM invariance of first–order effects.

At k=0k=0, let g​(0;ρ,ϕ)=ρ2+(1−ρ2)=1g(0;\rho,\phi)=\sqrt{\rho^{2}+(1-\rho^{2})}=1. From ([27](https://arxiv.org/html/2510.04569v1#S5.E27 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")),

|  |  |  |
| --- | --- | --- |
|  | ∂w∂ρ|k=0=θ2​(ϕ⋅0+ρ​(ϕ⋅0+ρ)−ρg)=0,∂w∂ϕ|k=0=θ2​(ρ⋅0+(ϕ⋅0+ρ)​0g)=0.\left.\frac{\partial w}{\partial\rho}\right|\_{k=0}=\frac{\theta}{2}\left(\phi\cdot 0+\frac{\rho(\phi\cdot 0+\rho)-\rho}{g}\right)=0,\qquad\left.\frac{\partial w}{\partial\phi}\right|\_{k=0}=\frac{\theta}{2}\left(\rho\cdot 0+\frac{(\phi\cdot 0+\rho)0}{g}\right)=0. |  |

Hence ∂w~/∂(ρ​-shift)=0\partial\tilde{w}/\partial(\rho\text{-shift})=0 and
∂w~/∂(ψ​-scale)=0\partial\tilde{w}/\partial(\psi\text{-scale})=0 at k=0k=0, which via (i) implies

|  |  |  |
| --- | --- | --- |
|  | ∂midm​(k)∂(ρ​-shift)|k=0=∂midm​(k)∂(ψ​-scale)|k=0=0.\left.\frac{\partial\,\mathrm{mid}\_{m}(k)}{\partial(\rho\text{-shift})}\right|\_{k=0}=\left.\frac{\partial\,\mathrm{mid}\_{m}(k)}{\partial(\psi\text{-scale})}\right|\_{k=0}=0. |  |

Therefore, to first order, ρ\rho– and ψ\psi–deformations only *tilt the wings* and do not move the ATM mid. This is ([30](https://arxiv.org/html/2510.04569v1#S5.E30 "In ATM invariance. ‣ 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

#### (iii) Delta and Vega sensitivities.

Write BS Delta Δ=∂CBS/∂S\Delta=\partial C^{\mathrm{BS}}/\partial S and denote
Vanna Vanna=∂2CBS/(∂S​∂σ)\mathrm{Vanna}=\partial^{2}C^{\mathrm{BS}}/(\partial S\,\partial\sigma) and
Volga Volga=∂2CBS/∂σ2\mathrm{Volga}=\partial^{2}C^{\mathrm{BS}}/\partial\sigma^{2} (Appendix [Appendix D: eSSVI and Black–Scholes Derivatives](https://arxiv.org/html/2510.04569v1#Ax4 "Appendix D: eSSVI and Black–Scholes Derivatives ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Using chain rule,

|  |  |  |
| --- | --- | --- |
|  | ∂Δ∂p=∂Δ∂σ⋅∂σ~∂p=Vanna⋅12​σ~​T​∂w~∂p,∂𝒱∂p=∂𝒱∂σ⋅∂σ~∂p=Volga⋅12​σ~​T​∂w~∂p,\frac{\partial\Delta}{\partial p}=\frac{\partial\Delta}{\partial\sigma}\cdot\frac{\partial\tilde{\sigma}}{\partial p}=\mathrm{Vanna}\cdot\frac{1}{2\,\tilde{\sigma}\,T}\,\frac{\partial\tilde{w}}{\partial p},\qquad\frac{\partial\mathcal{V}}{\partial p}=\frac{\partial\mathcal{V}}{\partial\sigma}\cdot\frac{\partial\tilde{\sigma}}{\partial p}=\mathrm{Volga}\cdot\frac{1}{2\,\tilde{\sigma}\,T}\,\frac{\partial\tilde{w}}{\partial p}, |  |

which matches ([34](https://arxiv.org/html/2510.04569v1#S5.E34 "In 5.4 Greeks and hedging: Delta & Vega sensitivities ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). In particular, the *sign* of these sensitivities is governed by the sign of ∂w~/∂p\partial\tilde{w}/\partial p, i.e., by the local skew effect induced by ρ\rho–shift or ψ\psi–scale. At k=0k=0, these first–order sensitivities vanish by (ii). Away from ATM, the sign flips across wings according to the sign of kk and the local values of (ρ~,ϕ~)(\tilde{\rho},\tilde{\phi}).

#### Uniform boundedness on compacts.

Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") (parameter compactness and the cap ([4](https://arxiv.org/html/2510.04569v1#S2.E4 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))) together with Lemma [1](https://arxiv.org/html/2510.04569v1#Thmlemma1 "Lemma 1 (BS regularity in strikes and maturities). ‣ A.0 Regularity lemma (used repeatedly). ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") imply uniform bounds on 𝒱\mathcal{V}, Vanna\mathrm{Vanna}, Volga\mathrm{Volga} and on the Jacobians of the eSSVI map on any compact (k,T)(k,T)–grid. Because σ~≥σmin>0\tilde{\sigma}\geq\sigma\_{\min}>0 and T≥Tmin>0T\geq T\_{\min}>0, all multipliers 1/(2​σ~​T)1/(2\tilde{\sigma}T) are uniformly bounded as well. Hence the sensitivities above are uniformly bounded on compacts.

#### Consequences for intensities and net delta.

Combining (i) with ([31](https://arxiv.org/html/2510.04569v1#S5.E31 "In 5.2 Sensitivities of mid/ask/bid to each control ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([33](https://arxiv.org/html/2510.04569v1#S5.E33 "In 5.3 Intensity responses to controls ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), any shape control pp modifies intensities through the induced change in w~\tilde{w} and hence in ask/bid\mathrm{ask}/\mathrm{bid}; at ATM the first–order intensity response vanishes because ∂w~/∂p=0\partial\tilde{w}/\partial p=0. For net delta, the sensitivity formula ([35](https://arxiv.org/html/2510.04569v1#S5.E35 "In 5.4 Greeks and hedging: Delta & Vega sensitivities ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) follows by differentiating ([18](https://arxiv.org/html/2510.04569v1#S3.E18 "In Hedging and P&L. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and using the product rule: a *flow shift* term from ∂vbuy/sell/∂p\partial v\_{\mathrm{buy/sell}}/\partial p (via ([33](https://arxiv.org/html/2510.04569v1#S5.E33 "In 5.3 Intensity responses to controls ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))) plus a *Greek* term weighted by (vsell−vbuy)(v\_{\mathrm{sell}}-v\_{\mathrm{buy}}) and Vanna\mathrm{Vanna}.

These prove all claims in Proposition [5](https://arxiv.org/html/2510.04569v1#Thmproposition5 "Proposition 5 (P8: Sensitivities of price and Greeks to 𝜌-shift and 𝜓-scale). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").
∎

###### Proof of Proposition [5](https://arxiv.org/html/2510.04569v1#Thmproposition5 "Proposition 5 (P8: Sensitivities of price and Greeks to 𝜌-shift and 𝜓-scale). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").

We provide a detailed chain of equalities and bounds for the three claims:
(i) the mid–price sensitivity identity; (ii) ATM invariance of first–order
effects; and (iii) the Delta/Vega sensitivities. Throughout we work at a fixed
maturity T>0T>0 and log–moneyness k=log⁡(K/S)k=\log(K/S), and write
w~=w~​(k,T)\tilde{w}=\tilde{w}(k,T) for the *quoted* (action–deformed) eSSVI total
variance, σ~=w~/T\tilde{\sigma}=\sqrt{\tilde{w}/T}, and
mid=CBS​(S,K,T,σ~)\mathrm{mid}=C^{\mathrm{BS}}(S,K,T,\tilde{\sigma}).
The BS Vega is 𝒱:=∂CBS/∂σ\mathcal{V}:=\partial C^{\mathrm{BS}}/\partial\sigma.

#### (i) Chain rule for mid sensitivity.

For any scalar control p∈{ρ​-shift,ψ​-scale}p\in\{\rho\text{-shift},\psi\text{-scale}\}, by the chain rule,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂mid∂p=∂CBS∂σ​∂σ~∂p=𝒱​12​σ~​T​∂w~∂p,\frac{\partial\,\mathrm{mid}}{\partial p}=\frac{\partial C^{\mathrm{BS}}}{\partial\sigma}\,\frac{\partial\tilde{\sigma}}{\partial p}=\mathcal{V}\,\frac{1}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}, |  | (47) |

because σ~=w~/T\tilde{\sigma}=\sqrt{\tilde{w}/T} implies
∂σ~/∂p=(2​σ~​T)−1​∂w~/∂p\partial\tilde{\sigma}/\partial p=(2\tilde{\sigma}T)^{-1}\,\partial\tilde{w}/\partial p.
This is exactly ([29](https://arxiv.org/html/2510.04569v1#S5.E29 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

It remains to express ∂w~/∂p\partial\tilde{w}/\partial p in terms of eSSVI parameters.
Let w=w​(k;θ,ρ,ϕ)w=w(k;\theta,\rho,\phi) be the eSSVI total variance ([1](https://arxiv.org/html/2510.04569v1#S2.E1 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with

|  |  |  |
| --- | --- | --- |
|  | g​(k;ρ,ϕ)=(ϕ​k+ρ)2+(1−ρ2).g(k;\rho,\phi)=\sqrt{(\phi k+\rho)^{2}+(1-\rho^{2})}. |  |

From Appendix [Appendix D: eSSVI and Black–Scholes Derivatives](https://arxiv.org/html/2510.04569v1#Ax4 "Appendix D: eSSVI and Black–Scholes Derivatives ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), we recall

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂w∂θ=12​(1+ρ​ϕ​k+g),∂w∂ρ=θ2​(ϕ​k+ρ​(ϕ​k+ρ)−ρg),∂w∂ϕ=θ2​(ρ​k+(ϕ​k+ρ)​kg).\frac{\partial w}{\partial\theta}=\frac{1}{2}\,(1+\rho\phi k+g),\quad\frac{\partial w}{\partial\rho}=\frac{\theta}{2}\left(\phi k+\frac{\rho(\phi k+\rho)-\rho}{g}\right),\quad\frac{\partial w}{\partial\phi}=\frac{\theta}{2}\left(\rho k+\frac{(\phi k+\rho)k}{g}\right). |  | (48) |

Under the action deformation ([13](https://arxiv.org/html/2510.04569v1#S3.E13 "In Action. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")),

|  |  |  |
| --- | --- | --- |
|  | (θ,ρ,ϕ)⟼(θ~,ρ~,ϕ~)=(θ,ρ+ρ​-shift,ϕ⋅ψ​-scale),(\theta,\rho,\phi)\ \longmapsto\ (\tilde{\theta},\tilde{\rho},\tilde{\phi})=(\theta,\ \rho+\rho\text{-shift},\ \phi\cdot\psi\text{-scale}), |  |

and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂w~∂(ρ​-shift)=∂w∂ρ|(θ~,ρ~,ϕ~),∂w~∂(ψ​-scale)=∂w∂ϕ|(θ~,ρ~,ϕ~)⋅ϕ.\frac{\partial\tilde{w}}{\partial(\rho\text{-shift})}=\left.\frac{\partial w}{\partial\rho}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})},\qquad\frac{\partial\tilde{w}}{\partial(\psi\text{-scale})}=\left.\frac{\partial w}{\partial\phi}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})}\cdot\phi. |  | (49) |

Substituting ([49](https://arxiv.org/html/2510.04569v1#Ax1.E49 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and ([48](https://arxiv.org/html/2510.04569v1#Ax1.E48 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) into ([47](https://arxiv.org/html/2510.04569v1#Ax1.E47 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) proves the mid–price sensitivity identity.

#### (ii) ATM invariance (k=0k=0).

At the money (k=0k=0), we have g​(0;ρ,ϕ)=ρ2+(1−ρ2)=1g(0;\rho,\phi)=\sqrt{\rho^{2}+(1-\rho^{2})}=1. Evaluating
([48](https://arxiv.org/html/2510.04569v1#Ax1.E48 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) at k=0k=0 gives

|  |  |  |
| --- | --- | --- |
|  | ∂w∂ρ|k=0=θ2​(ϕ⋅0+ρ​(ϕ⋅0+ρ)−ρ1)=0,∂w∂ϕ|k=0=θ2​(ρ⋅0+(ϕ⋅0+ρ)⋅01)=0.\left.\frac{\partial w}{\partial\rho}\right|\_{k=0}=\frac{\theta}{2}\left(\phi\cdot 0+\frac{\rho(\phi\cdot 0+\rho)-\rho}{1}\right)=0,\qquad\left.\frac{\partial w}{\partial\phi}\right|\_{k=0}=\frac{\theta}{2}\left(\rho\cdot 0+\frac{(\phi\cdot 0+\rho)\cdot 0}{1}\right)=0. |  |

By ([49](https://arxiv.org/html/2510.04569v1#Ax1.E49 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")),
∂w~/∂(ρ​-shift)=∂w~/∂(ψ​-scale)=0\partial\tilde{w}/\partial(\rho\text{-shift})=\partial\tilde{w}/\partial(\psi\text{-scale})=0 at k=0k=0,
and hence ([47](https://arxiv.org/html/2510.04569v1#Ax1.E47 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) yields

|  |  |  |
| --- | --- | --- |
|  | ∂mid∂(ρ​-shift)|k=0=∂mid∂(ψ​-scale)|k=0=0,\left.\frac{\partial\,\mathrm{mid}}{\partial(\rho\text{-shift})}\right|\_{k=0}=\left.\frac{\partial\,\mathrm{mid}}{\partial(\psi\text{-scale})}\right|\_{k=0}=0, |  |

which is the ATM first–order invariance ([30](https://arxiv.org/html/2510.04569v1#S5.E30 "In ATM invariance. ‣ 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). Economically,
ρ\rho/ϕ\phi deformations tilt the *wings* and leave the ATM level unchanged to first order; only θ\theta moves the ATM [[14](https://arxiv.org/html/2510.04569v1#bib.bib14), [20](https://arxiv.org/html/2510.04569v1#bib.bib20)].

#### (iii) Delta and Vega sensitivities.

Let Δ=∂CBS/∂S\Delta=\partial C^{\mathrm{BS}}/\partial S and 𝒱=∂CBS/∂σ\mathcal{V}=\partial C^{\mathrm{BS}}/\partial\sigma be the BS Delta and Vega, and denote the cross– and second–order sensitivities

|  |  |  |
| --- | --- | --- |
|  | Vanna=∂2CBS∂S​∂σ,Volga=∂2CBS∂σ2.\mathrm{Vanna}=\frac{\partial^{2}C^{\mathrm{BS}}}{\partial S\,\partial\sigma},\qquad\mathrm{Volga}=\frac{\partial^{2}C^{\mathrm{BS}}}{\partial\sigma^{2}}. |  |

Using the chain rule w.r.t. any p∈{ρ​-shift,ψ​-scale}p\in\{\rho\text{-shift},\psi\text{-scale}\},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Δ∂p\displaystyle\frac{\partial\Delta}{\partial p} | =∂Δ∂σ​∂σ~∂p=Vanna⋅12​σ~​T​∂w~∂p,\displaystyle=\frac{\partial\Delta}{\partial\sigma}\,\frac{\partial\tilde{\sigma}}{\partial p}=\mathrm{Vanna}\cdot\frac{1}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}, |  | (50) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝒱∂p\displaystyle\frac{\partial\mathcal{V}}{\partial p} | =∂𝒱∂σ​∂σ~∂p=Volga⋅12​σ~​T​∂w~∂p.\displaystyle=\frac{\partial\mathcal{V}}{\partial\sigma}\,\frac{\partial\tilde{\sigma}}{\partial p}=\mathrm{Volga}\cdot\frac{1}{2\tilde{\sigma}T}\,\frac{\partial\tilde{w}}{\partial p}. |  |

These match ([34](https://arxiv.org/html/2510.04569v1#S5.E34 "In 5.4 Greeks and hedging: Delta & Vega sensitivities ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")). In particular,
the *sign* of both sensitivities is controlled by the sign of ∂w~/∂p\partial\tilde{w}/\partial p,
i.e., by whether the deformation increases or decreases total variance at (k,T)(k,T).
At k=0k=0, we have ∂w~/∂p=0\partial\tilde{w}/\partial p=0 for p∈{ρ​-shift,ψ​-scale}p\in\{\rho\text{-shift},\psi\text{-scale}\}
by (ii), hence the first–order Delta/Vega sensitivities vanish at ATM.

#### (iv) Continuity and boundedness on compacts.

Under Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), the admissible parameter set is compact,
T≥Tmin>0T\geq T\_{\min}>0, and σ~≥σmin>0\tilde{\sigma}\geq\sigma\_{\min}>0; together with
Lemma [1](https://arxiv.org/html/2510.04569v1#Thmlemma1 "Lemma 1 (BS regularity in strikes and maturities). ‣ A.0 Regularity lemma (used repeatedly). ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"), this implies 𝒱,Vanna,Volga\mathcal{V},\mathrm{Vanna},\mathrm{Volga} are continuous and uniformly bounded on any compact (k,T)(k,T)–grid, and the eSSVI Jacobians in ([48](https://arxiv.org/html/2510.04569v1#Ax1.E48 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) are uniformly bounded as well. Consequently, the prefactor 1/(2​σ~​T)1/(2\tilde{\sigma}T) is uniformly bounded and the product representations ([47](https://arxiv.org/html/2510.04569v1#Ax1.E47 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([50](https://arxiv.org/html/2510.04569v1#Ax1.E50 "In (iii) Delta and Vega sensitivities. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) are uniformly bounded on compacts.

#### (v) Wing sign structure (qualitative).

From ([48](https://arxiv.org/html/2510.04569v1#Ax1.E48 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), away from ATM the terms involving kk dominate:

|  |  |  |
| --- | --- | --- |
|  | sign⁡(∂w∂ϕ)≈sign⁡(k),sign⁡(∂w∂ρ)≈sign⁡(ϕ​k),\operatorname{sign}\!\Big(\frac{\partial w}{\partial\phi}\Big)\ \approx\ \operatorname{sign}(k),\qquad\operatorname{sign}\!\Big(\frac{\partial w}{\partial\rho}\Big)\ \approx\ \operatorname{sign}(\phi k), |  |

modulo the gg–normalization. Thus ψ\psi–scale and ρ\rho–shift typically increase variance on one wing and decrease it on the other, reproducing the expected skew tilts; the sensitivities of mid/Delta/Vega inherit these signs via ([47](https://arxiv.org/html/2510.04569v1#Ax1.E47 "In (i) Chain rule for mid sensitivity. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) and ([50](https://arxiv.org/html/2510.04569v1#Ax1.E50 "In (iii) Delta and Vega sensitivities. ‣ A.8 Proofs of Propositions 4–5 (monotonicity and sensitivities) ‣ Appendix A: Detailed Proofs for Section 6 ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

Combining (i)–(v) proves Proposition [5](https://arxiv.org/html/2510.04569v1#Thmproposition5 "Proposition 5 (P8: Sensitivities of price and Greeks to 𝜌-shift and 𝜓-scale). ‣ 6.6 P7–P8: Monotonicity and sensitivity results for interpretability ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge").
∎

## Appendix B: Implementation Details and Hyperparameters

#### Networks and parameterization.

Actor/critic are two-layer MLPs with tanh\tanh activations. The actor outputs state-dependent mean and diagonal log-std for the *raw* action z∈ℝ5z\in\mathbb{R}^{5}; physical actions aa follow the squashing map in §[4.1](https://arxiv.org/html/2510.04569v1#S4.SS1 "4.1 Policy class and parameterization ‣ 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"). The critic Vω​(s)V\_{\omega}(s) is independent.

#### Default hyperparameters (reproduce main figures).

Table [2](https://arxiv.org/html/2510.04569v1#Ax2.T2 "Table 2 ‣ Default hyperparameters (reproduce main figures). ‣ Appendix B: Implementation Details and Hyperparameters ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") lists the values used for all results. These match the settings referenced in settings.json.

Table 2: Hyperparameters and defaults (simulation-only runs).

|  |  |
| --- | --- |
| Component | Value |
| Actor/critic MLP | hidden size 6464, 2 layers, tanh\tanh |
| Actor log-std range | [log⁡10−3,log⁡0.5][\log 10^{-3},\ \log 0.5] (per-dimension clamp) |
| Optimizer | Adam (3×10−43\times 10^{-4}), grad clip 1.01.0 |
| PPO | clip ϵ=0.2\epsilon=0.2, GAE (γ,λ)=(0.99,0.95)(\gamma,\lambda)=(0.99,0.95), value loss 0.50.5, entropy 10−310^{-3} |
| Warm-start | 800800 steps toward a⋆=(0.01,0.5,1.0,0.0,0.0)a^{\star}=(0.01,0.5,1.0,0.0,0.0), loss ([24](https://arxiv.org/html/2510.04569v1#S4.E24 "In 4.2 Stage I: Supervised warm-start ‣ 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| Annealing | λshape:0→0.5\lambda\_{\mathrm{shape}}:0\!\to\!0.5, λarb:0→0.05\lambda\_{\mathrm{arb}}:0\!\to\!0.05, λcvar:0.01\lambda\_{\mathrm{cvar}}:0.01 (fixed) |
| eSSVI cap | τmax\tau\_{\max} s.t. θ​ϕ≤τmax\theta\phi\leq\tau\_{\max} (Theorem [8](https://arxiv.org/html/2510.04569v1#Thmtheorem8 "Theorem 8 (T5: Linear wing-growth bound under a 𝜃⁢ϕ cap). ‣ 6.4 T5: eSSVI wing growth bound and relation to Lee’s moment constraints ‣ 6 Theory ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| BF/CAL smoothing | softplus temperature τarb=10−3\tau\_{\mathrm{arb}}=10^{-3} |
| CVaR | q=0.05q=0.05, NMC=64N\_{\mathrm{MC}}=64, softplus temperature τcvar=10−3\tau\_{\mathrm{cvar}}=10^{-3} |
| Intensity | λ0=0.8\lambda\_{0}=0.8, β=35\beta=35, w​(k)=exp⁡(−|k|/0.25)w(k)=\exp(-|k|/0.25) |
| Spread scale | s0=0.10s\_{0}=0.10 |
| Grids | T∈{7,14,21,30,60,90}/252T\in\{7,14,21,30,60,90\}/252; k∈[−0.35,0.35]k\in[-0.35,0.35] with 2121 points |
| Episodes & seed | 88 episodes; seed =0=0 |

#### Numerical guards.

Clamp T≥Tmin>0T\geq T\_{\min}>0, σ≥σmin>0\sigma\geq\sigma\_{\min}>0; apply nan\_to\_num to all intermediate tensors; keep ψ\psi in [0,ψmax​(ρ))[0,\psi\_{\max}(\rho)) with ψmax​(ρ)=21+|ρ|−εψ\psi\_{\max}(\rho)=\frac{2}{1+|\rho|}-\varepsilon\_{\psi}, εψ>0\varepsilon\_{\psi}>0 (cf. ([3](https://arxiv.org/html/2510.04569v1#S2.E3 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))).

## Appendix C: Environment and Training Pseudocode (Expanded)

Algorithm 2  Environment step st,at↦st+1,rts\_{t},a\_{t}\mapsto s\_{t+1},r\_{t} (expanded)

1: Input: state sts\_{t}, action at=(α,hedge,ψ​-scale,ρ​-shift,dual)a\_{t}=(\alpha,\mathrm{hedge},\psi\text{-scale},\rho\text{-shift},\mathrm{dual})

2: Deform eSSVI params: (θ~,ρ~,ψ~)←(θ,ρ+ρ​-shift,ψ⋅ψ​-scale)(\tilde{\theta},\tilde{\rho},\tilde{\psi})\leftarrow(\theta,\rho+\rho\text{-shift},\psi\cdot\psi\text{-scale}); enforce θ​ϕ≤τmax\theta\phi\leq\tau\_{\max}

3: Compute w~​(k,T)\tilde{w}(k,T) via ([1](https://arxiv.org/html/2510.04569v1#S2.E1 "In 2.2 Arbitrage-free eSSVI recap ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), σ~=w~/T\tilde{\sigma}=\sqrt{\tilde{w}/T}; mid/quotes via ([14](https://arxiv.org/html/2510.04569v1#S3.E14 "In Quoting and spreads. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), ([15](https://arxiv.org/html/2510.04569v1#S3.E15 "In Quoting and spreads. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))

4: Intensities via ([16](https://arxiv.org/html/2510.04569v1#S3.E16 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([17](https://arxiv.org/html/2510.04569v1#S3.E17 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); expected fills vbuy/sellv\_{\mathrm{buy/sell}}

5: Compute PNLtquote\mathrm{PNL}^{\mathrm{quote}}\_{t} by ([20](https://arxiv.org/html/2510.04569v1#S3.E20 "In Hedging and P&L. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); Δtnet\Delta^{\mathrm{net}}\_{t} by ([18](https://arxiv.org/html/2510.04569v1#S3.E18 "In Hedging and P&L. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); PNLthedge\mathrm{PNL}^{\mathrm{hedge}}\_{t} by ([19](https://arxiv.org/html/2510.04569v1#S3.E19 "In Hedging and P&L. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))

6: Compute BF,CAL\mathrm{BF},\mathrm{CAL} via ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) (softplus); Shape\mathrm{Shape} via ([21](https://arxiv.org/html/2510.04569v1#S3.E21 "In Smooth arbitrage and shape penalties. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))

7: Estimate CVaR^q,t−\widehat{\mathrm{CVaR}}^{-}\_{q,t} via ([23](https://arxiv.org/html/2510.04569v1#S3.E23 "In Scenario construction. ‣ 3.3 CVaR as the tail-risk term and a differentiable estimator ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) with NMCN\_{\mathrm{MC}} scenarios

8: Reward rtr\_{t} by ([22](https://arxiv.org/html/2510.04569v1#S3.E22 "In Per-step reward. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); update eSSVI estimate (e.g., mean-reverting filter toward latent surface)

9: Advance mid price St+1S\_{t+1} (Heston step); form st+1s\_{t+1}; return (st+1,rt)(s\_{t+1},r\_{t})




Algorithm 3  PPO update (implementation details)

1: Collect NN steps on-policy; compute A^t\hat{A}\_{t} with GAE; normalize per batch

2: Compute clipped surrogate ([25](https://arxiv.org/html/2510.04569v1#S4.E25 "In 4.3 Stage II: PPO with structural annealing ‣ 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")); take KK epochs with minibatches

3: Critic target R^t=A^t+Vω​(st)\hat{R}\_{t}=\hat{A}\_{t}+V\_{\omega}(s\_{t}); value loss 0.5​‖R^t−Vω​(st)‖20.5\|\hat{R}\_{t}-V\_{\omega}(s\_{t})\|^{2}

4: Entropy bonus on raw zz for all heads (including dual); clamp log⁡σ\log\sigma to control exploration

5: Anneal (λshape,λarb,λcvar)(\lambda\_{\mathrm{shape}},\lambda\_{\mathrm{arb}},\lambda\_{\mathrm{cvar}}) per episode

## Appendix D: eSSVI and Black–Scholes Derivatives

#### eSSVI partials.

With g​(k;ρ,ϕ)=(ϕ​k+ρ)2+(1−ρ2)g(k;\rho,\phi)=\sqrt{(\phi k+\rho)^{2}+(1-\rho^{2})}, we have

|  |  |  |
| --- | --- | --- |
|  | ∂w∂θ=12​(1+ρ​ϕ​k+g),∂w∂ρ=θ2​(ϕ​k+ρ​(ϕ​k+ρ)−ρg),∂w∂ϕ=θ2​(ρ​k+(ϕ​k+ρ)​kg).\frac{\partial w}{\partial\theta}=\frac{1}{2}\,(1+\rho\phi k+g),\quad\frac{\partial w}{\partial\rho}=\frac{\theta}{2}\Big(\phi k+\frac{\rho(\phi k+\rho)-\rho}{g}\Big),\quad\frac{\partial w}{\partial\phi}=\frac{\theta}{2}\Big(\rho k+\frac{(\phi k+\rho)k}{g}\Big). |  |

Action map sensitivity (cf. ([28](https://arxiv.org/html/2510.04569v1#S5.E28 "In 5.1 Derivative templates through the eSSVI layer ‣ 5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))):

|  |  |  |
| --- | --- | --- |
|  | ∂w~∂(ρ​-shift)=∂w∂ρ|(θ~,ρ~,ϕ~),∂w~∂(ψ​-scale)=∂w∂ϕ|(θ~,ρ~,ϕ~)⋅ϕ.\frac{\partial\tilde{w}}{\partial(\rho\text{-shift})}=\left.\frac{\partial w}{\partial\rho}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})},\qquad\frac{\partial\tilde{w}}{\partial(\psi\text{-scale})}=\left.\frac{\partial w}{\partial\phi}\right|\_{(\tilde{\theta},\tilde{\rho},\tilde{\phi})}\cdot\phi. |  |

#### BS Greeks.

Let d±=log⁡(S/K)±12​σ2​Tσ​Td\_{\pm}=\frac{\log(S/K)\pm\frac{1}{2}\sigma^{2}T}{\sigma\sqrt{T}} (zero rate/carry).
Then Delta Δ=Φ​(d+)\Delta=\Phi(d\_{+}), Vega 𝒱=S​T​φ​(d+)\mathcal{V}=S\sqrt{T}\,\varphi(d\_{+}), Vanna =∂2C/(∂S​∂σ)=T​φ​(d+)​(1−d+​d−)=\partial^{2}C/(\partial S\,\partial\sigma)=\sqrt{T}\,\varphi(d\_{+})\,(1-d\_{+}d\_{-}), Volga =∂2C/∂σ2=S​T​φ​(d+)​d+​d−=\partial^{2}C/\partial\sigma^{2}=S\sqrt{T}\,\varphi(d\_{+})\,d\_{+}d\_{-}, where Φ\Phi and φ\varphi are standard normal cdf/pdf. Chain rules used in §[5](https://arxiv.org/html/2510.04569v1#S5 "5 Interpretability of Controls: Local Sensitivities of Quotes, Intensities, and Greeks ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge") follow by substitution with σ~=w~/T\tilde{\sigma}=\sqrt{\tilde{w}/T}.

## Appendix E: Smoothed BF/CAL Penalties and Lipschitz Bounds

#### Softplus smoothing.

For ReLU​(x)=max⁡{x,0}\mathrm{ReLU}(x)=\max\{x,0\} use sτ​(x)=τ​log⁡(1+ex/τ)s\_{\tau}(x)=\tau\log(1+e^{x/\tau}) with τ∈(0,1]\tau\in(0,1].
Then |sτ​(x)−x+|≤τ​log⁡2|s\_{\tau}(x)-x\_{+}|\leq\tau\log 2, sτ′​(x)=σ​(x/τ)∈(0,1)s^{\prime}\_{\tau}(x)=\sigma(x/\tau)\in(0,1), sτ′′​(x)=σ​(x/τ)​(1−σ​(x/τ))/τ≤(4​τ)−1s^{\prime\prime}\_{\tau}(x)=\sigma(x/\tau)(1-\sigma(x/\tau))/\tau\leq(4\tau)^{-1}.

#### Lipschitz constants.

Let C​(⋅)C(\cdot) be C2C^{2} in KK on the lattice hull and bounded by |C|≤MC|C|\leq M\_{C}, |∂K​KC|≤M2|\partial\_{KK}C|\leq M\_{2}. For grid spacing Δ​K\Delta K, the map C↦BFC\mapsto\mathrm{BF} using sτs\_{\tau} is Lipschitz with constant LBF≤1|𝒦′|​∑K1C¯m​1Δ​K2L\_{\mathrm{BF}}\leq\frac{1}{|\mathcal{K}^{\prime}|}\sum\_{K}\frac{1}{\bar{C}\_{m}}\frac{1}{\Delta K^{2}} times sup|sτ′|≤1\sup|s^{\prime}\_{\tau}|\leq 1, multiplied by the linear operator norm of central second differences (bounded on compacts). An analogous bound holds for CAL\mathrm{CAL} with LCAL≤1|𝒦|​∑K1/C¯m,m+1L\_{\mathrm{CAL}}\leq\frac{1}{|\mathcal{K}|}\sum\_{K}{1}/{\bar{C}\_{m,m+1}}.

#### Gradient stability.

Because sτ′∈(0,1)s^{\prime}\_{\tau}\in(0,1) and CC is C1C^{1} in eSSVI parameters (Appendix [Appendix D: eSSVI and Black–Scholes Derivatives](https://arxiv.org/html/2510.04569v1#Ax4 "Appendix D: eSSVI and Black–Scholes Derivatives ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), gradients of BF,CAL\mathrm{BF},\mathrm{CAL} w.r.t. actions are bounded by a constant that scales with (Δ​K)−2(\Delta K)^{-2} and the chain-rule Jacobian of the eSSVI layer, which is bounded on the admissible set (Assumption [1](https://arxiv.org/html/2510.04569v1#Thmassumption1 "Assumption 1 (Smoothness and bounds). ‣ 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

## Appendix F: CVaR Estimation—Inner Minimization and Variance Control

#### Inner minimization in RU.

For fixed scenarios {PNL~t(i)}i=1N\{\tilde{\mathrm{PNL}}^{(i)}\_{t}\}\_{i=1}^{N} and temperature τ\tau, the smoothed RU objective is

|  |  |  |
| --- | --- | --- |
|  | h^τ​(η)=η+1(1−q)​N​∑i=1Nsτ​(η−PNL~t(i)).\hat{h}\_{\tau}(\eta)=\eta+\frac{1}{(1-q)N}\sum\_{i=1}^{N}s\_{\tau}(\eta-\tilde{\mathrm{PNL}}^{(i)}\_{t}). |  |

It is strictly convex in η\eta with derivative
h^τ′​(η)=1+1(1−q)​N​∑iσ​((η−PNL~t(i))/τ)\hat{h}^{\prime}\_{\tau}(\eta)=1+\frac{1}{(1-q)N}\sum\_{i}\sigma\big((\eta-\tilde{\mathrm{PNL}}^{(i)}\_{t})/\tau\big).
A unique minimizer is found by Newton or bisection (monotone derivative); initialize at the empirical qq-quantile and perform a few Newton steps with step-size damping. As τ↓0\tau\downarrow 0, ητ∗→VaRq\eta^{\ast}\_{\tau}\to\mathrm{VaR}\_{q}.

#### Gradient estimators.

With pathwise Δ~​S\tilde{\Delta}S and LR for Poisson v~\tilde{v},

|  |  |  |
| --- | --- | --- |
|  | ∇atCVaR^q,t−=1(1−q)​N​∑i=1Nsτ′​(ητ∗−PNL~t(i))​(−∇atPNL~t(i)+PNL~t(i)​∇atlog⁡p​(v~(i);at)),\nabla\_{a\_{t}}\widehat{\mathrm{CVaR}}^{-}\_{q,t}=\frac{1}{(1-q)N}\sum\_{i=1}^{N}s^{\prime}\_{\tau}\!\big(\eta^{\ast}\_{\tau}-\tilde{\mathrm{PNL}}^{(i)}\_{t}\big)\,\left(-\nabla\_{a\_{t}}\tilde{\mathrm{PNL}}^{(i)}\_{t}+\tilde{\mathrm{PNL}}^{(i)}\_{t}\,\nabla\_{a\_{t}}\log p(\tilde{v}^{(i)};a\_{t})\right), |  |

where the second term vanishes if volumes are kept deterministic in the reward and only resampled for CVaR.

#### Variance reduction.

Use antithetic ξ\xi for Δ~​S\tilde{\Delta}S, control variates for LR (subtract a state-dependent baseline), and mini-batch normalization; increase NMCN\_{\mathrm{MC}} along training (cf. §[4.5](https://arxiv.org/html/2510.04569v1#S4.SS5 "4.5 Stability heuristics and schedules ‣ 4 Learning Scheme: Warm-Start + PPO with a Learnable Dual ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")).

## Appendix J: Notation Summary

Table 3: Main symbols used in the paper.

|  |  |
| --- | --- |
| Symbol | Meaning |
| StS\_{t} | mid price at time tt |
| KK, kk | strike and log-moneyness (k=log⁡(K/S)k=\log(K/S)) |
| TmT\_{m} | maturity mm; 𝒯={Tm}m=1M\mathcal{T}=\{T\_{m}\}\_{m=1}^{M} |
| w​(k,T)w(k,T), σ​(k,T)\sigma(k,T) | total variance, implied volatility (σ=w/T\sigma=\sqrt{w/T}) |
| (θ,ρ,ψ)(\theta,\rho,\psi) | eSSVI parameters; ϕ=ψ/θ\phi=\psi/\sqrt{\theta} |
| mid\mathrm{mid}, ask\mathrm{ask}, bid\mathrm{bid} | quotes via ([14](https://arxiv.org/html/2510.04569v1#S3.E14 "In Quoting and spreads. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")), ([15](https://arxiv.org/html/2510.04569v1#S3.E15 "In Quoting and spreads. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| λbuy/sell\lambda\_{\mathrm{buy/sell}} | execution intensities ([16](https://arxiv.org/html/2510.04569v1#S3.E16 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([17](https://arxiv.org/html/2510.04569v1#S3.E17 "In Intensity-based executions. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| Δnet\Delta^{\mathrm{net}} | net delta under expected fills ([18](https://arxiv.org/html/2510.04569v1#S3.E18 "In Hedging and P&L. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| BF\mathrm{BF}, CAL\mathrm{CAL} | static no-arbitrage surrogates ([7](https://arxiv.org/html/2510.04569v1#S2.E7 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"))–([8](https://arxiv.org/html/2510.04569v1#S2.E8 "In 2.3 Static no-arbitrage: butterfly and calendar ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| Shape\mathrm{Shape} | cross-maturity smoothness penalty ([21](https://arxiv.org/html/2510.04569v1#S3.E21 "In Smooth arbitrage and shape penalties. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| CVaRq\mathrm{CVaR}\_{q} | conditional value-at-risk at tail level qq ([9](https://arxiv.org/html/2510.04569v1#S2.E9 "In 2.4 Tail risk: Conditional Value-at-Risk ‣ 2 Preliminaries & Problem Setup ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| α\alpha, hedge\mathrm{hedge} | half-spread, hedge intensity (actions) |
| ψ\psi-scale, ρ\rho-shift | action-induced eSSVI deformations ([13](https://arxiv.org/html/2510.04569v1#S3.E13 "In Action. ‣ 3.1 State, action, transition, and reward ‣ 3 Arbitrage-Free Surface + Execution + Hedging as a Constrained MDP ‣ Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge")) |
| dual\mathrm{dual} | state-dependent dual action (effective multiplier) |

## References

* [1]

  T. Ho and H. R. Stoll.
  Optimal dealer pricing under transactions and return uncertainty.
  Journal of Financial Economics, 9(1):47–73, 1981.
* [2]

  L. R. Glosten and P. R. Milgrom.
  Bid, ask and transaction prices in a specialist market with
  heterogeneously informed traders.
  Journal of Financial Economics, 14(1):71–100, 1985.
* [3]

  A. S. Kyle.
  Continuous auctions and insider trading.
  Econometrica, 53(6):1315–1335, 1985.
* [4]

  M. Avellaneda and S. Stoikov.
  High-frequency trading in a limit order book.
  Quantitative Finance, 8(3):217–224, 2008.
* [5]

  O. Guéant, C.-A. Lehalle, and J. Fernandez-Tapia.
  Dealing with the inventory risk: A solution to the market making
  problem.
  Mathematics and Financial Economics, 7(4):477–507, 2013.
* [6]

  Á. Cartea, S. Jaimungal, and J. Penalva.
  Algorithmic and High-Frequency Trading.
  Cambridge University Press, 2015.
* [7]

  Á. Cartea and S. Jaimungal.
  Buy low, sell high: A high frequency trading perspective.
  SIAM Journal on Financial Mathematics, 5(1):415–444, 2014.
* [8]

  R. Cont, A. Kukanov, and S. Stoikov.
  The price impact of order book events: An empirical study.
  Journal of Financial Econometrics, 12(1):47–88, 2014.
* [9]

  A. Kirilenko, A. S. Kyle, M. Samadi, and T. Tuzun.
  The flash crash: High-frequency trading in an electronic market.
  Journal of Finance, 72(3):967–998, 2017.
* [10]

  J. Hasbrouck.
  Empirical Market Microstructure.
  Oxford University Press, 2007.
* [11]

  M. D. Gould, M. A. Porter, S. Williams, M. McDonald, D. J. Fenn, and S. D.
  Howison.
  Limit order books: A survey.
  Quantitative Finance, 13(11):1709–1742, 2013.
* [12]

  A. G. Hawkes.
  Spectra of some self-exciting and mutually exciting point processes.
  Biometrika, 58(1):83–90, 1971.
* [13]

  E. Bacry, I. Mastromatteo, and J.-F. Muzy.
  Hawkes processes in finance.
  Market Microstructure and Liquidity, 1(1):1550005, 2015.
* [14]

  J. Gatheral and A. Jacquier.
  Arbitrage-free SVI volatility surfaces.
  Quantitative Finance, 14(1):59–71, 2014.
* [15]

  S. Hendriks and C. Martini.
  The extended SSVI volatility surface.
  Journal of Computational Finance, 22(5):25–39, 2019.
* [16]

  C. Martini and A. Mingone.
  No-arbitrage SVI.
  SIAM Journal on Financial Mathematics, 13(1):227–261, 2022.
* [17]

  P. Carr and D. Madan.
  A note on sufficient conditions for no arbitrage.
  Finance Research Letters, 2(3):125–130, 2005.
* [18]

  M. Roper.
  Arbitrage-free implied volatility surfaces.
  University of Sydney Preprint, 2010.
  URL: <https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2010/roper-9.pdf>.
* [19]

  V. Durrleman.
  From implied to spot volatilities.
  Finance and Stochastics, 13(2):241–272, 2009.
* [20]

  R. W. Lee.
  The moment formula for implied volatility at extreme strikes.
  Mathematical Finance, 14(3):469–480, 2004.
* [21]

  F. Black and M. Scholes.
  The pricing of options and corporate liabilities.
  Journal of Political Economy, 81(3):637–654, 1973.
* [22]

  R. C. Merton.
  Theory of rational option pricing.
  Bell Journal of Economics and Management Science, 4(1):141–183, 1973.
* [23]

  D. T. Breeden and R. H. Litzenberger.
  Prices of state-contingent claims implicit in option prices.
  Journal of Business, 51(4):621–651, 1978.
* [24]

  S. L. Heston.
  A closed-form solution for options with stochastic volatility with
  applications to bond and currency options.
  Review of Financial Studies, 6(2):327–343, 1993.
* [25]

  H. Bühler, L. Gonon, J. Teichmann, and B. Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [26]

  S. N. Cohen, C. Reisinger, and S. Wang.
  Estimating risks of option books using neural-SDE market models.
  Journal of Computational Finance, 2023.
* [27]

  S. N. Cohen, C. Reisinger, and S. Wang.
  Arbitrage-free neural-SDE market models.
  arXiv preprint arXiv:2105.11053, 2021.
* [28]

  M. Wiese, B. Knob, R. Korn, and P. Kretschmer.
  Deep hedging: Learning to simulate equity option markets.
  arXiv preprint arXiv:1911.01700, 2019.
* [29]

  R. T. Rockafellar and S. Uryasev.
  Optimization of conditional value-at-risk.
  Journal of Risk, 2:21–42, 2000.
* [30]

  R. T. Rockafellar and S. Uryasev.
  Conditional value-at-risk for general loss distributions.
  Journal of Banking & Finance, 26(7):1443–1471, 2002.
* [31]

  G. Ch. Pflug.
  Some remarks on the value-at-risk and the conditional value-at-risk.
  In S. Uryasev, editor, Probabilistic Constrained Optimization:
  Methodology and Applications, pages 272–281. Springer, 2000.
* [32]

  Y. Chow and M. Ghavamzadeh.
  Algorithms for CVaR optimization in MDPs.
  In Advances in Neural Information Processing Systems, pages
  3509–3517, 2014.
* [33]

  A. Tamar, Y. Chow, M. Ghavamzadeh, and S. Mannor.
  Policy gradient for coherent risk measures.
  In Advances in Neural Information Processing Systems, 2015.
* [34]

  Y. Chow, M. Ghavamzadeh, L. Janson, and M. Pavone.
  Risk-constrained reinforcement learning with percentile risk
  criteria.
  Journal of Machine Learning Research, 18(167):1–51, 2018.
* [35]

  K. Wang et al.
  Near-minimax-optimal risk-sensitive reinforcement learning with
  CVaR.
  In Advances in Neural Information Processing Systems, 2023.
* [36]

  X. Ni, J. Gao, et al.
  Risk-sensitive reward-free reinforcement learning with CVaR.
  In Proceedings of the 41st International Conference on Machine
  Learning (PMLR), 2024.
* [37]

  D. Byrd, M. Hybinette, T. Balch, et al.
  ABIDES: Towards high-fidelity market simulation for AI research.
  arXiv:1904.12066, 2020.
* [38]

  S. Amrouni, P. Stone, T. Balch, et al.
  ABIDES-Gym: Gym environments for multi-agent discrete event
  simulation of limit order books.
  In ACM International Conference on AI in Finance (ICAIF), 2021.
* [39]

  R. Cont et al.
  Simulation of arbitrage-free implied volatility surfaces.
  Applied Economics Letters, 2023.
* [40]

  R. A. Howard and J. E. Matheson.
  Risk-sensitive Markov decision processes.
  Management Science, 18(7):356–369, 1972.
* [41]

  P. Bergault and L. Sánchez-Betancourt.
  A mean field game between informed traders and a broker.
  SIAM Journal on Financial Mathematics, 16(2):358–388, 2025.
* [42]

  Á. Cartea and L. Sánchez-Betancourt.
  Brokers and informed traders: Dealing with toxic flow and extracting
  trading signals.
  SIAM Journal on Financial Mathematics, 16(2):243–270, 2025.
* [43]

  R. Boyce, M. Herdegen, and L. Sánchez-Betancourt.
  Market making with exogenous competition.
  SIAM Journal on Financial Mathematics, 16(2):692–706, 2025.
* [44]

  J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov.
  Proximal policy optimization algorithms.
  arXiv:1707.06347, 2017.
* [45]

  J. Schulman, P. Moritz, S. Levine, M. I. Jordan, and P. Abbeel.
  High-dimensional continuous control using generalized advantage
  estimation.
  In International Conference on Learning Representations, 2016.
* [46]

  C. Acerbi and D. Tasche.
  On the coherence of expected shortfall.
  Journal of Banking & Finance, 26(7):1487–1503, 2002.
* [47]

  P. Artzner, F. Delbaen, J.-M. Eber, and D. Heath.
  Coherent measures of risk.
  Mathematical Finance, 9(3):203–228, 1999.
* [48]

  E. Altman.
  Constrained Markov Decision Processes.
  Chapman and Hall/CRC, 1999.
* [49]

  M. L. Puterman.
  Markov Decision Processes: Discrete Stochastic Dynamic
  Programming.
  John Wiley & Sons, 1994.
* [50]

  A. Ruszczyński.
  Risk-averse dynamic programming for Markov decision processes.
  Mathematics of Operations Research, 35(1):226–248, 2010.
* [51]

  A. Shapiro, D. Dentcheva, and A. Ruszczyński.
  Lectures on Stochastic Programming: Modeling and Theory.
  SIAM, 2nd edition, 2014.
* [52]

  J. Achiam, D. Held, A. Tamar, and P. Abbeel.
  Constrained policy optimization.
  In Proceedings of the 34th International Conference on Machine
  Learning, pages 22–31, 2017.
* [53]

  C. Tessler, D. J. Mankowitz, and S. Mannor.
  Reward constrained policy optimization.
  In Proceedings of the 22nd International Conference on
  Artificial Intelligence and Statistics (PMLR), pages 3111–3120, 2019.
* [54]

  F. Abergel and A. Jedidi.
  A long-memory model for order flow.
  Quantitative Finance, 15(7):1129–1137, 2015.
* [55]

  J.-P. Bouchaud, J. Bonart, J. Donier, and A. Gould.
  Trades, Quotes and Prices: Financial Markets Under the
  Microscope.
  Cambridge University Press, 2018.
* [56]

  P. Glasserman.
  Monte Carlo Methods in Financial Engineering.
  Springer, 2004.
* [57]

  J. Schulman, S. Levine, P. Abbeel, M. Jordan, and P. Moritz.
  Trust region policy optimization.
  In Proceedings of the 32nd International Conference on Machine
  Learning, pages 1889–1897, 2015.
* [58]

  S. M. Kakade.
  A natural policy gradient.
  In Advances in Neural Information Processing Systems, pages
  1531–1538, 2002.
* [59]

  P. Henderson, R. Islam, P. Bachman, J. Pineau, D. Precup, and D. Meger.
  Deep reinforcement learning that matters.
  Proceedings of the AAAI Conference on Artificial Intelligence,
  32, 2018.
* [60]

  D. P. Kingma and J. Ba.
  Adam: A method for stochastic optimization.
  arXiv:1412.6980, 2014.
* [61]

  J. C. Hull.
  Options, Futures, and Other Derivatives.
  Pearson, 10th edition, 2018.
* [62]

  E. G. Haug.
  The Complete Guide to Option Pricing Formulas.
  McGraw-Hill, 2nd edition, 2007.
* [63]

  P. Wilmott.
  Paul Wilmott on Quantitative Finance.
  Wiley, 2nd edition, 2006.
* [64]

  R. T. Rockafellar and R. J.-B. Wets.
  Variational Analysis.
  Springer, 1998.
* [65]

  R. S. Sutton, D. McAllester, S. Singh, and Y. Mansour.
  Policy gradient methods for reinforcement learning with function
  approximation.
  In Advances in Neural Information Processing Systems, pages
  1057–1063, 2000.
* [66]

  P. Marbach and J. N. Tsitsiklis.
  Simulation-based optimization of Markov reward processes.
  IEEE Transactions on Automatic Control, 46(2):191–209, 2001.