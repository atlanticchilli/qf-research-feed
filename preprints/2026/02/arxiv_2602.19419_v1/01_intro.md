---
authors:
- Pranay Anchuri
doc_id: arxiv:2602.19419v1
family_id: arxiv:2602.19419
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds*
  Optimal Impulse Control in Concentrated AMMs'
url_abs: http://arxiv.org/abs/2602.19419v1
url_html: https://arxiv.org/html/2602.19419v1
venue: arXiv q-fin
version: 1
year: 2026
---


Pranay Anchuri

###### Abstract

Concentrated liquidity provision in decentralized exchanges presents a fundamental Impulse Control problem. Liquidity Providers (LPs) face a non-trivial trade-off between maximizing fee accrual through tight price-range concentration and minimizing the friction costs of rebalancing, including gas fees and swap slippage. Existing methods typically employ heuristic or threshold strategies that fail to account for market dynamics.

This paper formulates liquidity management as an optimal control problem and derives the corresponding Hamilton-Jacobi-Bellman quasi-variational inequality (HJB-QVI). We present an approximate solution RAmmStein, a Deep Reinforcement Learning method that incorporates the mean-reversion speed (θ\theta) of an Ornstein-Uhlenbeck process among other features as input to the model. We demonstrate that the agent learns to separate the state space into regions of action and inaction.

We evaluate the framework using high-frequency 1Hz Coinbase trade data comprising over 6.8M trades. Experimental results show that RAmmStein achieves a superior net ROI of 0.72% compared to both passive and aggressive strategies. Notably, the agent reduces rebalancing frequency by 67% compared to a greedy rebalancing while maintaining 88% active time. Our results demonstrate that regime-aware laziness can significantly improve capital efficiency by preserving the returns that would otherwise be eroded by the operational costs.

\*\*footnotetext: The authors clarify that RAmmStein bears no relation to the German industrial metal band of a similar name. We simply find that the free-boundary of our HJB-QVI solution is as solid as a stone (Stein).

## I Introduction

The rise of Decentralized Finance (DeFi) has fundamentally changed how digital assets are exchanged on blockchains. Automated Market Makers (AMMs) pioneered by Uniswap [[1](https://arxiv.org/html/2602.19419v1#bib.bib1)] lie at the center of this transformation. AMMs are a class of smart contracts that facilitate trade among digital assets without using a traditional order book. These markets are defined by a mathematical invariant that remains constant as users trade against it. Uniswap V2 is the first generation of such markets that use a so-called constant product invariant: x⋅y=kx\cdot y=k, where xx and yy are the quantities of the assets in the pool. The marginal price offered by the pool is given by the ratio xy\frac{x}{y}. While the design is quite elegant, it suffers from severe capital inefficiency. The capital deployed by liquidity providers is spread across the entire price spectrum to support market making. For stable asset pairs that trade in a narrow price range, a vast majority of the capital deployed in the pool remains unused. Uniswap V3 [[2](https://arxiv.org/html/2602.19419v1#bib.bib2)] addressed this limitation by introducing concentrated liquidity, which allows LPs to provide liquidity in a price range of their choice. However, a position earns fees only when the price falls within its range. This innovation increased capital efficiency by orders of magnitude compared to Uniswap V2.

However, concentrated liquidity introduces a significant operational challenge for liquidity providers: range management. When the price exits the LP’s range, the position becomes inactive and does not earn any fees until (a) the price enters the range naturally, or (b) the LP intervenes and rebalances the position. Each rebalancing event has at least three sources of friction:

1. 1.

   Gas costs: Rebalancing requires at least two on-chain transactions, one to exit the position and another to re-enter at the new price.
2. 2.

   Swap fees: When the price exits, the portfolio is composed of a single asset. A portion of this asset must be swapped for the other asset to create fee-earning liquidity again. This swap has an associated fee.
3. 3.

   Slippage: For large positions, the swap transaction also incurs a slippage cost.

The liquidity provider faces a dilemma: whether to pay the rebalancing costs and hope to recover them via trading fees, or wait for the price to re-enter the range. Often, the cost to maintain a concentrated position exceeds the marginal fee accrued from that concentration. We call this the LP Rebalancing Paradox.

Existing tools and strategies to manage LPs often make suboptimal decisions because they treat all price deviations identically regardless of the underlying market regime. A 1% price deviation in a strongly trending market is fundamentally different from a 1% price change in a mean-reverting regime. Consider the following two scenarios:

* •

  Scenario A: Price exits an LP range during a momentum-driven breakout. It is unlikely that the price reverts to the range in the short term. In this scenario, rebalancing is economically justified.
* •

  Scenario B: Price exits a narrow-range LP during a noise movement around a stable equilibrium. In this scenario, the probability that the price re-enters the range is high. Therefore, paying the rebalancing costs is not justified.

Our paper makes the following novel contributions:

1. 1.

   We formalize liquidity management in concentrated AMMs as an impulse control problem. We derive the corresponding Hamilton-Jacobi-Bellman quasi-variational inequality that completely characterizes the optimal rebalancing policy.
2. 2.

   We introduce the Stein Signal (θ\theta), the mean-reversion parameter of an Ornstein-Uhlenbeck process, as a prior that captures market regime dynamics.
3. 3.

   We develop RAmmStein, a deep reinforcement learning method that approximates the solution of the HJB equation and learns a dynamic boundary separating the continuation region (wait) from the exercise region (rebalance) in the state space.
4. 4.

   We conduct extensive backtesting on real-world high-frequency data from Coinbase, demonstrating that RAmmStein significantly outperforms both passive and aggressive strategies in terms of ROI.

## II Background and Related Work

### II-A Automated Market Makers

Automated Market Makers (AMMs) are a class of decentralized exchange protocols that replace traditional order books with deterministic pricing functions implemented as smart contracts. The most prevalent design paradigm is the Constant Function Market Maker (CFMM), in which the reserves of two assets (x,y)(x,y) must satisfy an invariant φ​(x,y)=k\varphi(x,y)=k after every trade. Uniswap V2 popularized the constant product invariant x⋅y=kx\cdot y=k, distributing liquidity uniformly across all prices from zero to infinity [[1](https://arxiv.org/html/2602.19419v1#bib.bib1)]. Alternative invariants have been proposed to address specific use cases: StableSwap [[3](https://arxiv.org/html/2602.19419v1#bib.bib3)] employs a hybrid invariant that interpolates between constant-product and constant-sum curves, achieving lower slippage for correlated asset pairs, while Orbital [[4](https://arxiv.org/html/2602.19419v1#bib.bib4)] introduces a geometry-aware invariant adapted to anticipated price trajectories.

A fundamental limitation shared by these constant-function designs is that liquidity is allocated globally across the entire price domain. At any given market price, only a narrow band of the deposited reserves actively facilitates trades; the remainder sits idle, earning no fees while still bearing exposure to adverse price movements. This capital inefficiency is particularly acute for asset pairs that trade within a confined range. Uniswap V3 addressed this limitation through the introduction of concentrated liquidity, which we describe next.

### II-B Concentrated Liquidity Mechanics

In Uniswap V3, price ranges have boundaries called ticks. The ii-th tick corresponds to the price 1.0001i1.0001^{i}. An LP specifies a lower tick ili\_{l} and an upper tick iui\_{u}, defining the price bounds pa=1.0001ilp\_{a}=1.0001^{i\_{l}} and pb=1.0001iup\_{b}=1.0001^{i\_{u}}. To open a position, equal value of both assets is deposited into the pool. The virtual liquidity LL within this range is computed as [[5](https://arxiv.org/html/2602.19419v1#bib.bib5)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L=Δ​x1p−1pb=Δ​yp−paL=\frac{\Delta x}{\frac{1}{\sqrt{p}}-\frac{1}{\sqrt{p\_{b}}}}=\frac{\Delta y}{\sqrt{p}-\sqrt{p\_{a}}} |  | (1) |

where Δ​x\Delta x and Δ​y\Delta y are the deposited token quantities and pp is the current price.

The fee accrued by an LP’s position during a time period TT is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fee=VT⋅ϕ⋅LL​PLt​o​t​a​l\text{Fee}=V\_{T}\cdot\phi\cdot\frac{L\_{LP}}{L\_{total}} |  | (2) |

where ϕ\phi is the pool’s fee tier (e.g., 0.05%, 0.30%, or 1.00%), VTV\_{T} is the total trading volume when the price is within the LP’s range.

Critically, when P∉[pa,pb]P\notin[p\_{a},p\_{b}], the position earns zero fees. The LP’s capital is fully converted to a single asset (the less valuable one), and the position remains inactive until the price re-enters the range.

### II-C Impermanent Loss and Rebalancing

Impermanent Loss (IL) refers to the opportunity cost of providing liquidity versus simply holding the underlying assets. Consider the scenario where an LP opens a position when the price is pi​n​i​tp\_{init} and sets a range pa<pi​n​i​t<pbp\_{a}<p\_{init}<p\_{b}. During the course of trading, the price in the pool moves by δ\delta. As the price shifts, the AMM continuously rebalances the LP’s portfolio: the average execution price at which the LP effectively sells asset AA for asset BB lies between pi​n​i​tp\_{init} and pi​n​i​t+δp\_{init}+\delta. The opportunity cost of providing liquidity is then the difference between the value of this rebalanced portfolio and the value of simply holding the original assets at the new price.

For concentrated liquidity positions, this opportunity cost is amplified. Within the active range, higher capital efficiency yields a larger share of trading fees, but once the price exits the range, the position is fully converted to a single asset and ceases to earn fees entirely. Importantly, this opportunity cost arises regardless of the direction of the price movement: whether δ\delta is positive or negative, the IL depends on the magnitude |δ||\delta| of the deviation from the initial price.

These dynamics create a fundamentally complex optimization landscape for managing a liquidity position. The LP faces the following trilemma.

* •

  Maximizing in-range time: The LP earns fees only when the pool price lies within the position’s range. Narrow price ranges improve capital efficiency but are breached by smaller price movements.
* •

  Minimizing rebalancing frequency: Each rebalancing event incurs multiple sources of friction, including explicit costs such as gas fees and swap fees, as well as implicit costs such as slippage and information leakage.
* •

  Managing IL exposure: Aggressive rebalancing crystallizes IL by repeatedly selling low and buying high. Conversely, failure to rebalance leaves capital idle and may further increase the accumulated IL.

Previous work has analyzed IL in concentrated liquidity settings [[6](https://arxiv.org/html/2602.19419v1#bib.bib6), [7](https://arxiv.org/html/2602.19419v1#bib.bib7), [8](https://arxiv.org/html/2602.19419v1#bib.bib8)], deriving closed-form expressions for expected losses under various price path assumptions. However, these analyses typically assume passive position management in which the LP establishes a position and leaves it unchanged. We take a fundamentally different approach by modeling the rebalancing decision as an impulse control problem, where the LP must at each moment decide whether to continue with the current position or jump to a new recentered position. This formulation connects LP management to the rich literature on impulse control in stochastic systems.

### II-D Related Work on Liquidity Provisioning

Several recent works have examined the challenges involved in liquidity provisioning in AMMs. We classify the related work in this area across three themes: a) empirical analyses of LP behavior, b) theoretical frameworks, and c) computational methods.

#### II-D1 Empirical Studies

Heimbach et al. [[9](https://arxiv.org/html/2602.19419v1#bib.bib9)] conducted one of the first empirical analyses of LP behavior in the Uniswap V2 AMM. Their analysis showed that most liquidity providers follow passive strategies and that liquidity provisioning is concentrated in a few pools. Moreover, the impermanent loss dominates the fee revenue generated in pools with volatile asset pairs.
Berg et al. [[10](https://arxiv.org/html/2602.19419v1#bib.bib10)] analyzed Uniswap and SushiSwap and showed that nearly 30% of trades on these exchanges happen at suboptimal rates.
With the introduction of concentrated liquidity in Uniswap V3, Heimbach et al. [[11](https://arxiv.org/html/2602.19419v1#bib.bib11)] showed that LP returns vary widely depending on position width, price volatility, and fee tier. In addition, profitable positions in volatile pools require active management to overcome impermanent losses.
Fritsch [[12](https://arxiv.org/html/2602.19419v1#bib.bib12)] evaluated fixed-range and resetting-interval strategies on Uniswap V3 and found that active strategies can outperform passive strategies. In general, their analyses showed that selecting the right strategy is a non-trivial problem.

#### II-D2 Theoretical Frameworks

Evans [[13](https://arxiv.org/html/2602.19419v1#bib.bib13)] derived LP share returns for geometric mean market makers (such as Uniswap and Balancer) and showed that LP shares replicate derivative payoffs.
Cartea et al. [[14](https://arxiv.org/html/2602.19419v1#bib.bib14)] formulated a continuous-time stochastic control problem for strategic LPs. They introduced the concept of predictable loss (PL) and derived a closed-form optimal strategy (under log-utility conditions) that balances PL and the collected fees.
Milionis et al. [[15](https://arxiv.org/html/2602.19419v1#bib.bib15)] applied Myerson’s optimal auction theory to design incentive-compatible AMMs. In their design, the LP chooses a demand curve that has a bid-ask spread, inducing the traders to submit a true estimate of the asset price to trade in the AMM.
Bar-On and Mansour [[16](https://arxiv.org/html/2602.19419v1#bib.bib16)] framed LP as an online learning problem and provided lower bounds on LP reward using regret minimization without assumptions on future price distributions.

#### II-D3 Computational Methods

Fan et al. [[17](https://arxiv.org/html/2602.19419v1#bib.bib17)] introduced τ\tau-reset strategies for Uniswap V3. They showed that dynamic liquidity provisioning strategies optimized via stochastic optimization techniques exhibit higher LP earnings compared to baseline Uniswap V2 allocation.
Urusov et al. [[18](https://arxiv.org/html/2602.19419v1#bib.bib18)] further extended this using an ML ensemble combined with a backtesting framework to incorporate historical market dynamics.
Zhang et al. [[19](https://arxiv.org/html/2602.19419v1#bib.bib19)] applied a Dueling DDQN with a Loss-Versus-Rebalancing (LVR) reward function that includes hedging via futures. Their agent accounts for gas fees but does not incorporate mean-reversion signals or formulate the problem as impulse control.
Xu and Brini [[20](https://arxiv.org/html/2602.19419v1#bib.bib20)] used Proximal Policy Optimization with an LVR penalty and a rolling window training approach, outperforming passive LP in the majority of evaluation windows.
Jaimungal et al. [[21](https://arxiv.org/html/2602.19419v1#bib.bib21)] solved an HJB equation for optimal AMM trading using the Deep Galerkin Method, but focused on execution strategy rather than LP management.

Our work differs from these approaches in three key ways. First, we formalize LP management as an impulse control problem and derive the HJB-QVI, connecting our agent’s behavior to the optimal control literature.
Second, we introduce the Stein Signal (θ\theta) as a regime indicator that allows the agent to distinguish between temporary noise and long-term trends.
Third, our agent learns a laziness boundary that balances rebalancing costs against the probability of natural price reversion, achieving significant savings by avoiding unnecessary interventions.

### II-E Impulse Control Theory

Optimal control theory studies systems whose state evolves according to known dynamics, subject to control inputs applied over time. The objective is typically to choose a control policy that minimizes a cost functional (or equivalently, maximizes a reward) over a given horizon. The underlying system may evolve deterministically or stochastically, and the control may be applied continuously or at discrete intervention times.

Impulse control problems constitute a subclass of optimal control in which the controller makes discrete interventions at self-selected times, with each intervention incurring a fixed cost independent of the system state. Unlike continuous control, where actions are applied smoothly over time, or optimal stopping, where a single terminal decision is made, impulse control permits an arbitrary sequence of instantaneous interventions separated by periods of passive observation. This framework is particularly well-suited to settings where friction costs render frequent interventions prohibitively expensive—precisely the situation faced by LPs, for whom each rebalancing event incurs gas fees, swap costs, and slippage.

The seminal work by Bensoussan and Lions [[22](https://arxiv.org/html/2602.19419v1#bib.bib22)] established a rigorous mathematical framework for impulse control in diffusion processes. Their key insight was that optimal policies partition the state space into two distinct regions: a continuation region, where the controller optimally waits and allows the system to evolve according to its natural dynamics, and a jump region, where immediate intervention is optimal. The resulting optimal policy exhibits a threshold structure: the controller waits until the system state reaches the boundary between these regions, then intervenes to reset the state. The location of this boundary depends on the running reward, the intervention cost, and the stochastic dynamics of the underlying process.

For a controlled diffusion, the value function V​(x)V(x)—representing the expected discounted future reward from state xx under the optimal policy—satisfies a quasi-variational inequality (QVI). This inequality takes the form of a complementarity condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒ​V​(x)+f​(x),ℳ​V​(x)−V​(x)}=0\max\left\{\mathcal{L}V(x)+f(x),\mathcal{M}V(x)-V(x)\right\}=0 |  | (3) |

where ℒ\mathcal{L} denotes the infinitesimal generator of the diffusion, encoding both the drift and volatility of the process; f​(x)f(x) represents the instantaneous running reward accrued while waiting; and ℳ\mathcal{M} is the intervention operator that maps the current value to the post-jump value minus the jump cost. The QVI asserts that at every point in the state space, at least one of two conditions holds with equality. In the continuation region, the first term equals zero, meaning the value function satisfies the Hamilton-Jacobi-Bellman (HJB) equation—the fundamental partial differential equation of stochastic optimal control that characterizes the value of following an optimal policy in the absence of interventions. In the jump region, the second term equals zero, indicating that the current value exactly equals the value attainable through immediate intervention.

### II-F Mean-Reversion in Market Microstructure

The Ornstein-Uhlenbeck (OU) process originates from the modeling of physical systems that exhibit a mean-reverting tendency. It was introduced by Uhlenbeck and Ornstein [[23](https://arxiv.org/html/2602.19419v1#bib.bib23)] as a physically motivated alternative to Brownian motion, which models purely diffusive, memoryless dynamics. Since the foundational work of Vasicek [[24](https://arxiv.org/html/2602.19419v1#bib.bib24)] on interest rate modeling, the OU process has been extensively employed to capture mean-reverting behavior in financial markets. While long-horizon price movements in efficient markets are generally modeled as geometric Brownian motion, high-frequency price dynamics often exhibit pronounced mean-reversion arising from the microstructure of trading itself. Several mechanisms generate this behavior naturally:

* •

  Market maker inventory management: When a market maker accumulates excessive inventory in one direction, they shade their quotes to encourage offsetting flow, creating a restoring force that pulls prices back toward recent averages.
* •

  Cross-venue arbitrage: When an asset trades on multiple markets and the price dislocates on one venue, arbitrageurs trade against the dislocation, driving the price back toward the consensus level across markets.
* •

  Order book resilience: Large trades that consume liquidity on one side of the book are often followed by the gradual replenishment of limit orders, creating buying pressure after price declines and selling pressure after price increases.

#### II-F1 Stochastic Differential Equations and the OU Process

A continuous-time stochastic process XtX\_{t} is said to satisfy a stochastic differential equation (SDE) if it obeys

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b​(Xt)​d​t+σ​(Xt)​d​Wt,X0=xdX\_{t}=b(X\_{t})\,dt+\sigma(X\_{t})\,dW\_{t},\quad X\_{0}=x |  | (4) |

or equivalently, in integral form,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=x+∫0tb​(Xs)​𝑑s+∫0tσ​(Xs)​𝑑WsX\_{t}=x+\int\_{0}^{t}b(X\_{s})\,ds+\int\_{0}^{t}\sigma(X\_{s})\,dW\_{s} |  | (5) |

where the second integral is an Itô integral with respect to a standard Wiener process WtW\_{t}. The function b​(⋅)b(\cdot) governs the deterministic drift of the system, while σ​(⋅)\sigma(\cdot) modulates the intensity of random fluctuations.

The OU process is the specific case in which the drift is linear and the diffusion coefficient is constant. It satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=θ​(μ−St)​d​t+σ​d​WtdS\_{t}=\theta(\mu-S\_{t})\,dt+\sigma\,dW\_{t} |  | (6) |

The drift term θ​(μ−St)\theta(\mu-S\_{t}) is proportional to the deviation from the long-run mean μ\mu, with θ>0\theta>0 governing the speed of mean-reversion. The stochastic term σ​d​Wt\sigma\,dW\_{t} represents random fluctuations that continuously perturb the process away from equilibrium.

The mean-reverting property of the OU process also admits a statistical interpretation through Stein’s paradox. Stein [[25](https://arxiv.org/html/2602.19419v1#bib.bib25)] demonstrated that shrinkage estimators—which implicitly incorporate mean-reversion assumptions—can dramatically improve estimation accuracy relative to maximum likelihood, even in settings where such assumptions appear unjustified a priori.

The parameter θ\theta is of central importance to our framework. In our context, θ\theta serves as a real-time regime indicator: high values signal a strongly mean-reverting environment where price deviations are likely temporary, while low values indicate trending or random-walk behavior where deviations tend to persist or amplify. Looking ahead, the central insight underlying our approach is that when θ\theta is large, it is preferable for the LP to wait for the price to revert naturally rather than incur the cost of rebalancing; conversely, when θ\theta is small, the price is more likely drifting, and the LP should rebalance promptly or adopt a more conservative position. The characteristic timescale of mean-reversion is given by the half-life t1/2=ln⁡(2)/θt\_{1/2}=\ln(2)/\theta. For θ=0.01\theta=0.01 per second, the half-life is approximately 69 seconds, meaning that a price deviation from μ\mu is expected to decay by half within just over one minute. An LP observing such a θ\theta estimate may rationally defer rebalancing and instead wait for the price to naturally revert into the active range.

### II-G Deep Reinforcement Learning for Finance

Deep Reinforcement Learning (DRL) combines the representational power of neural networks with the sequential decision-making framework of reinforcement learning, enabling agents to learn complex policies directly from high-dimensional observations. This combination has achieved remarkable success across diverse domains, including game playing [[26](https://arxiv.org/html/2602.19419v1#bib.bib26)] and robotic control [[27](https://arxiv.org/html/2602.19419v1#bib.bib27)]. More recently, DRL has emerged as a prominent methodology in quantitative finance. In financial contexts, DRL has been applied to portfolio optimization [[28](https://arxiv.org/html/2602.19419v1#bib.bib28)], where agents learn to dynamically allocate capital across assets; market making [[29](https://arxiv.org/html/2602.19419v1#bib.bib29)], where agents learn quote placement strategies that balance inventory risk against profit opportunities; optimal execution [[30](https://arxiv.org/html/2602.19419v1#bib.bib30)], where agents learn to split large orders across time to minimize market impact; and optimal batch posting [[31](https://arxiv.org/html/2602.19419v1#bib.bib31)], where agents learn to time data batch submissions to minimize posting fees. These applications share a common structure: the agent observes market features, takes actions that affect positions or orders, and receives rewards based on realized profits or costs.

In Reinforcement Learning (RL) [[32](https://arxiv.org/html/2602.19419v1#bib.bib32)], the primary goal is to learn a value function that measures the expected discounted cumulative reward attainable by an agent. Traditional methods, such as tabular value iteration, require repeated sweeps of value and policy improvement to converge. This approach becomes intractable in high-dimensional state spaces, where the number of states grows exponentially with the number of features. In DRL, a deep neural network serves as a function approximator that learns compact representations of these complex state spaces, enabling generalization across similar states.

Building on this, the Deep Q-Network (DQN) architecture introduced by Mnih et al. [[33](https://arxiv.org/html/2602.19419v1#bib.bib33)] represents a foundational approach to value-based DRL. The key insight is to approximate the action-value function Q​(s,a)Q(s,a), which represents the expected cumulative discounted reward from taking action aa in state ss and thereafter following the optimal policy, using a neural network with parameters θ\theta. The network is trained via temporal difference learning [[32](https://arxiv.org/html/2602.19419v1#bib.bib32)]: given a transition (s,a,r,s′)(s,a,r,s^{\prime}), the loss penalizes the squared difference between the current estimate Q​(s,a;θ)Q(s,a;\theta) and the target r+γ​maxa′⁡Q​(s′,a′;θ)r+\gamma\max\_{a^{\prime}}Q(s^{\prime},a^{\prime};\theta), where γ\gamma is the discount factor. DQN introduces two critical mechanisms to stabilize training: (i) experience replay, which stores transitions in a buffer and samples mini-batches uniformly to break temporal correlations; and (ii) a target network, a slowly updated copy of the Q-network used to compute stable target values.

The Double DQN variant, introduced by van Hasselt et al. [[34](https://arxiv.org/html/2602.19419v1#bib.bib34)], addresses an important limitation of standard DQN. Because the same network is used both to select the maximizing action and to evaluate its value, the max operator introduces a systematic upward bias: the maximum of noisy estimates exceeds the true maximum in expectation, leading to overestimation of Q-values. Double DQN decouples these two functions by using the online network for action selection and the target network for value evaluation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=r+γ​Q​(s′,arg⁡maxa′⁡Q​(s′,a′;θ);θ−)y=r+\gamma Q(s^{\prime},\arg\max\_{a^{\prime}}Q(s^{\prime},a^{\prime};\theta);\theta^{-}) |  | (7) |

Here θ\theta denotes the online network parameters and θ−\theta^{-} denotes the target network parameters. This simple modification substantially reduces overestimation bias and improves learning stability.

Our work applies Double DQN to the impulse control problem of LP rebalancing. Although the action space is binary (wait versus rebalance), the optimal policy depends on a complex interplay of factors including price dynamics, regime indicators, and position status. The neural network learns to approximate the boundary between the continuation and jump regions without requiring an explicit solution to the HJB equation, instead discovering this boundary through trial-and-error interaction with a simulated environment.

## III Theoretical Framework

In this section, we describe the theoretical framework used to model the problem of managing a liquidity position in a Uniswap V3-style AMM.

### III-A Problem Statement

Consider a liquidity provider with capital KK deployed in a concentrated position in a Uniswap V3 pool. Instead of using lower and upper ticks, we characterize the position by a center price cc and a total width of 2​w2w. The position earns fees only when the price StS\_{t} lies within the interval [c​(1−w),c​(1+w)][c(1-w),c(1+w)]. When StS\_{t} exits this range, the position becomes entirely single-asset, depending on the direction in which the price exits.

The liquidity provider faces a sequential decision problem over a time horizon [0,T][0,T]. At each instant tt, the provider can choose to either allow the position to continue in its current state or pay a cost CC to recenter it at the current price StS\_{t}. The cost CC encompasses the gas fee for the blockchain transaction, swap fees for rebalancing the token composition, and slippage. The provider’s objective is to choose a sequence of intervention times that maximizes the expected cumulative discounted profit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J=𝔼​[∫0Te−ρ​t​f​(St,ct)​𝑑t−∑ie−ρ​τi​C]J=\mathbb{E}\left[\int\_{0}^{T}e^{-\rho t}f(S\_{t},c\_{t})dt-\sum\_{i}e^{-\rho\tau\_{i}}C\right] |  | (8) |

The first term in the objective function represents the cumulative fee income discounted to present value at rate ρ\rho. The instantaneous fee rate f​(St,ct)f(S\_{t},c\_{t}) is proportional to trading volume when the position is active and zero otherwise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(St,ct)={Vt⋅ϕ⋅LL​PLt​o​t​a​lif ​St∈[ct​(1−w),ct​(1+w)]0otherwisef(S\_{t},c\_{t})=\begin{cases}V\_{t}\cdot\phi\cdot\dfrac{L\_{LP}}{L\_{total}}&\text{if }S\_{t}\in[c\_{t}(1-w),\;c\_{t}(1+w)]\\[6.0pt] 0&\text{otherwise}\end{cases} |  | (9) |

where VtV\_{t} is the instantaneous trading volume, ϕ\phi is the pool fee tier, LL​PL\_{LP} is the LP’s liquidity, and Lt​o​t​a​lL\_{total} is the total pool liquidity.

The second term represents the cumulative intervention costs over the entire horizon, discounted at rate ρ\rho. We assume that each rebalancing event incurs a fixed cost CC.

The expectation in Equation [8](https://arxiv.org/html/2602.19419v1#S3.E8 "In III-A Problem Statement ‣ III Theoretical Framework ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs") is taken over the stochastic price path, and the optimization is over all admissible sequences of intervention times.

This formulation is an instance of the impulse control problems discussed in Section II-D, where the goal is to select discrete intervention times that maximize net reward. As noted therein, the optimal policy for such problems exhibits a threshold structure: there exists a boundary in the state space separating the continuation region, where the provider optimally waits, from the jump region, where immediate intervention is optimal.

### III-B The Price Process Model

We model the mid-price StS\_{t} as an Ornstein-Uhlenbeck process (see Section II-E for background):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=θ​(μ−St)​d​t+σ​d​WtdS\_{t}=\theta(\mu-S\_{t})\,dt+\sigma\,dW\_{t} |  | (10) |

To obtain the closed-form solution, define g​(t)=St​eθ​tg(t)=S\_{t}\,e^{\theta t}. Applying Itô’s lemma:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​g=eθ​t​(θ​St​d​t+d​St)=eθ​t​(θ​μ​d​t+σ​d​Wt)dg=e^{\theta t}\left(\theta S\_{t}\,dt+dS\_{t}\right)=e^{\theta t}\left(\theta\mu\,dt+\sigma\,dW\_{t}\right) |  | (11) |

Integrating both sides from 0 to tt and rearranging yields the explicit solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=μ+(S0−μ)​e−θ​t+σ​∫0te−θ​(t−s)​𝑑WsS\_{t}=\mu+(S\_{0}-\mu)\,e^{-\theta t}+\sigma\int\_{0}^{t}e^{-\theta(t-s)}\,dW\_{s} |  | (12) |

The first two terms describe deterministic relaxation toward the mean μ\mu at rate θ\theta, while the stochastic integral captures the accumulated effect of random perturbations, each exponentially discounted by the time elapsed since its occurrence.

The parameters (θ,μ,σ)(\theta,\mu,\sigma) are estimated via rolling OLS regression on a sliding window of prices. Given discrete prices {S1,…,Sn}\{S\_{1},\ldots,S\_{n}\}, we fit the regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St+1−St=α+β​St+ϵtS\_{t+1}-S\_{t}=\alpha+\beta S\_{t}+\epsilon\_{t} |  | (13) |

The OU parameters are then recovered as θ=−β/Δ​t\theta=-\beta/\Delta t, μ=−α/β\mu=-\alpha/\beta, and σ\sigma is estimated from the residual standard deviation.

A high θ\theta indicates strong mean-reversion (price is likely to return to the mean), while a low θ\theta indicates trending behavior (price deviations tend to persist).

### III-C Optimal Control Framework for LP management

The Hamilton-Jacobi-Bellman (HJB) equation is the central equation in optimal control problems involving continuous-time deterministic and stochastic processes. It is based on Bellman’s principle of optimality, which states that for all initial states and decisions, the remaining decisions must constitute an optimal policy with respect to the state resulting from the first decision.

### 1. Definition of the Value Function

We define the value function V​(S,c,t)V(S,c,t) as the maximum expected discounted profit from time tt to the horizon TT, given the current asset price SS and the current center of the liquidity position cc:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V(S,c,t)=sup{τi}𝔼[∫tTe−ρ​(τ−t)f(Sτ,cτ)dτ−∑τi≥te−ρ​(τi−t)C∣St=S,ct=c]\begin{split}V(S,c,t)=\sup\_{\{\tau\_{i}\}}\mathbb{E}\bigg[\int\_{t}^{T}e^{-\rho(\tau-t)}f(S\_{\tau},c\_{\tau})d\tau\\ -\sum\_{\tau\_{i}\geq t}e^{-\rho(\tau\_{i}-t)}C\mid S\_{t}=S,c\_{t}=c\bigg]\end{split} |  | (14) |

where ff is the instantaneous fee reward and the asset price StS\_{t} follows an OU process:

|  |  |  |
| --- | --- | --- |
|  | d​St=θ​(μ−St)​d​t+σ​d​WtdS\_{t}=\theta(\mu-S\_{t})dt+\sigma dW\_{t} |  |

### 2. Derivation of the HJB for the Continuous Regime

We first define the HJB governing the continuous continuation regime, where the liquidity provider chooses to let the position evolve without any intervention. Without intervention, the center cc remains constant. Applying Bellman’s optimality principle:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V(S,c,t)=maxu𝔼[∫tt+Δ​te−ρ​(τ−t)f(Sτ,c)dτ+e−ρ​Δ​tV(St+Δ​t,c,t+Δt)]\begin{split}V(S,c,t)=\max\_{u}\mathbb{E}\bigg[\int\_{t}^{t+\Delta t}e^{-\rho(\tau-t)}f(S\_{\tau},c)d\tau\\ +e^{-\rho\Delta t}V(S\_{t+\Delta t},c,t+\Delta t)\bigg]\end{split} |  | (15) |

For infinitesimal Δ​t\Delta t, the integral is approximated as f​(S,c)​Δ​tf(S,c)\Delta t. We expand the future value term using Itô’s lemma and the approximation e−ρ​Δ​t≈1−ρ​Δ​te^{-\rho\Delta t}\approx 1-\rho\Delta t to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | V≈𝔼[f(S,c)Δt+(1−ρΔt)(V+∂V∂tΔt+∂V∂SdS+12σ2∂2V∂S2Δt)]\begin{split}V\approx\mathbb{E}\bigg[f(S,c)\Delta t+(1-\rho\Delta t)\bigg(V+\frac{\partial V}{\partial t}\Delta t\\ +\frac{\partial V}{\partial S}dS+\frac{1}{2}\sigma^{2}\frac{\partial^{2}V}{\partial S^{2}}\Delta t\bigg)\bigg]\end{split} |  | (16) |

Substituting the expectation of the OU drift 𝔼​[d​S]=θ​(μ−S)​Δ​t\mathbb{E}[dS]=\theta(\mu-S)\Delta t, dividing by Δ​t\Delta t, and letting Δ​t→0\Delta t\to 0, we obtain the HJB equation for the value function of the LP position in the continuation region:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​V−∂V∂t=f​(S,c)+θ​(μ−S)​∂V∂S+12​σ2​∂2V∂S2\rho V-\frac{\partial V}{\partial t}=f(S,c)+\theta(\mu-S)\frac{\partial V}{\partial S}+\frac{1}{2}\sigma^{2}\frac{\partial^{2}V}{\partial S^{2}} |  | (17) |

### 3. The Impulse Control Quasi-Variational Inequality

In the full sequential decision problem, the provider chooses between two actions: allow the position to evolve naturally or pay a cost CC to rebalance the center to the current price. This implies a discrete jump in the state space where the center is reset to the current market price, c→Sc\to S.

The optimal value function V​(S,c,t)V(S,c,t) must satisfy the following Quasi-Variational Inequality (QVI):

|  |  |  |  |
| --- | --- | --- | --- |
|  | min⁡[ρ​V−∂V∂t−ℒO​U​V−f​(S,c),V​(S,c,t)−(V​(S,S,t)−C)]=0\min\left[\begin{aligned} &\rho V-\frac{\partial V}{\partial t}-\mathcal{L}\_{OU}V-f(S,c),\\ &V(S,c,t)-\left(V(S,S,t)-C\right)\end{aligned}\right]=0 |  | (18) |

where ℒO​U\mathcal{L}\_{OU} is the infinitesimal generator for the OU process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒO​U​V=θ​(μ−S)​∂V∂S+12​σ2​∂2V∂S2\mathcal{L}\_{OU}V=\theta(\mu-S)\frac{\partial V}{\partial S}+\frac{1}{2}\sigma^{2}\frac{\partial^{2}V}{\partial S^{2}} |  | (19) |

The first term captures the mean-reverting drift: when the current price SS is above the long-run mean μ\mu, the drift is negative, reducing VV. The second term captures how uncertainty in the price process affects the value function through the curvature of VV.

This formulation identifies two distinct regions in the state space:

* •

  Continuation Region: The first term in Equation [18](https://arxiv.org/html/2602.19419v1#S3.E18 "In 3. The Impulse Control Quasi-Variational Inequality ‣ III Theoretical Framework ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs") equals zero. The value function evolves according to fee accrual and price dynamics. In this region, the marginal value of waiting exceeds the marginal value of acting.
* •

  Jump Region: The second term in Equation [18](https://arxiv.org/html/2602.19419v1#S3.E18 "In 3. The Impulse Control Quasi-Variational Inequality ‣ III Theoretical Framework ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs") equals zero. The value of the current state (S,c)(S,c) is exactly the value of the recentered state (S,S)(S,S) minus the cost CC.

### III-D The Laziness Principle

We define the Laziness Boundary as the boundary separating these two regions. Although the Double DQN agent learns to approximate this boundary without explicitly solving the QVI, we can characterize its properties by analyzing the trade-off between rebalancing costs and the strength of mean-reversion.

#### III-D1 Rebalancing trade-off

The fundamental question facing an LP when the price exits the active range is whether to rebalance (paying cost CC to restore fee accrual) or wait for the price to re-enter the range naturally. This decision depends critically on the estimated mean-reversion speed θ\theta. To formalize, consider the value of waiting, VwaitV\_{\text{wait}}, from a state where the position is out of range:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vwait​(St)=𝔼​[∫tτe−ρ​(ξ−t)​f​(Sξ)​𝑑ξ+e−ρ​(τ−t)​V​(Sτ)∣St]V\_{\text{wait}}(S\_{t})=\mathbb{E}\left[\int\_{t}^{\tau}e^{-\rho(\xi-t)}f(S\_{\xi})d\xi+e^{-\rho(\tau-t)}V(S\_{\tau})\mid S\_{t}\right] |  | (20) |

where τ\tau is the first passage time at which the price either returns to the active range or exits to a state where rebalancing becomes optimal. Since f​(Sξ)=0f(S\_{\xi})=0 while out of range, the integral term vanishes and VwaitV\_{\text{wait}} reduces to the discounted expected value at the first passage time τ\tau.

#### III-D2 First Passage Probabilities

We now analyze the probability of the process returning to the long-run mean μ\mu before hitting an outer barrier price LL. This is given by the ratio of scale functions [[35](https://arxiv.org/html/2602.19419v1#bib.bib35)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(return)=∫Lsexp⁡(θ​(y−μ)2σ2)​𝑑y∫Lμexp⁡(θ​(y−μ)2σ2)​𝑑yP(\text{return})=\frac{\int\_{L}^{s}\exp\left(\frac{\theta(y-\mu)^{2}}{\sigma^{2}}\right)dy}{\int\_{L}^{\mu}\exp\left(\frac{\theta(y-\mu)^{2}}{\sigma^{2}}\right)dy} |  | (21) |

As the mean-reversion strength θ\theta increases, P​(return)→1P(\text{return})\to 1 even for starting states ss significantly far from μ\mu. This confirms that during periods of high θ\theta, price reversion is nearly certain.

#### III-D3 Option interpretation

When the price exits the range, the liquidity provider holds an American-style option to wait, where CC acts as the strike price and θ\theta governs the option’s moneyness. The DDQN agent learns to approximate the optimal exercise boundary by balancing the cost of foregone fee accrual against the strike price of rebalancing.

### III-E DDQN as an HJB Solver

Equation [18](https://arxiv.org/html/2602.19419v1#S3.E18 "In 3. The Impulse Control Quasi-Variational Inequality ‣ III Theoretical Framework ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs") provides a complete characterization of the optimal policy, but solving it numerically is challenging: the equation is nonlinear due to the min operator, the state space becomes high-dimensional when OU parameters are included, and the parameters themselves are time-varying and estimated with error.

DRL offers an alternative approach that sidesteps explicit solution of the QVI. The key connection is between the HJB equation governing the continuation region and the Bellman equation that underlies Q-learning. Discretizing time into intervals of length Δ​t\Delta t, the HJB equation in the continuation region can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(s,c)=f​(s,c)​Δ​t+e−ρ​Δ​t​𝔼​[V​(St+Δ​t,c)]V(s,c)=f(s,c)\Delta t+e^{-\rho\Delta t}\mathbb{E}[V(S\_{t+\Delta t},c)] |  | (22) |

This can be rewritten as the Bellman equation V​(s)=r+γ​𝔼​[V​(s′)]V(s)=r+\gamma\mathbb{E}[V(s^{\prime})], where γ=e−ρ​Δ​t\gamma=e^{-\rho\Delta t} is the discount factor and r=f​Δ​tr=f\Delta t is the immediate reward.

The Q-function extends this to action-conditioned values. In our setting with two actions—wait (a=0a=0) and rebalance (a=1a=1)—the Q-values are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Q​(s,c,a=0)\displaystyle Q(s,c,a=0) | =f​(s,c)​Δ​t+γ​𝔼​[V​(S′,c)]\displaystyle=f(s,c)\Delta t+\gamma\mathbb{E}[V(S^{\prime},c)] |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Q​(s,c,a=1)\displaystyle Q(s,c,a=1) | =−C+γ​𝔼​[V​(S′,S′)]\displaystyle=-C+\gamma\mathbb{E}[V(S^{\prime},S^{\prime})] |  | (24) |

The value function is then V​(s,c)=maxa⁡Q​(s,c,a)V(s,c)=\max\_{a}Q(s,c,a), and the optimal policy selects the action with higher Q-value. The DDQN algorithm approximates the Q-function using a neural network Q​(s,a;θ)Q(s,a;\theta), where θ\theta denotes the network parameters. Given transitions (s,a,r,s′)(s,a,r,s^{\prime}) sampled from the replay buffer, the network minimizes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ)=𝔼​[(Q​(s,a;θ)−y)2]\mathcal{L}(\theta)=\mathbb{E}\left[\left(Q(s,a;\theta)-y\right)^{2}\right] |  | (25) |

where the target y=r+γ​Q​(s′,arg⁡maxa′⁡Q​(s′,a′;θ);θ−)y=r+\gamma Q(s^{\prime},\arg\max\_{a^{\prime}}Q(s^{\prime},a^{\prime};\theta);\theta^{-}) uses the Double DQN formulation to reduce overestimation bias.

Upon convergence, the learned Q-function implicitly encodes the solution to Equation [18](https://arxiv.org/html/2602.19419v1#S3.E18 "In 3. The Impulse Control Quasi-Variational Inequality ‣ III Theoretical Framework ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs"). The boundary between states where Q​(s,0)>Q​(s,1)Q(s,0)>Q(s,1) and those where Q​(s,1)>Q​(s,0)Q(s,1)>Q(s,0) corresponds to the Laziness Boundary derived from the HJB analysis. The DDQN approach handles nonlinearity through function approximation and naturally accommodates time-varying parameters without requiring closed-form solutions. Notably, the estimated OU parameters are included as input features to the Q-network alongside the state variables, providing the agent with explicit regime information.

## IV Methodology

In this section, we describe how the theoretical framework of Section [III](https://arxiv.org/html/2602.19419v1#S3 "III Theoretical Framework ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs") can be used to build a RAmmStein system that effectively manages liquidity positions in AMMs. Although the description assumes Uniswap V3-style AMMs, the system is sufficiently general to accommodate AMMs with different characteristics.

### IV-A System Architecture

The RAmmStein system consists of three main components:

1. 1.

   Feature Engine: This component is responsible for computing the OU parameters and constructing the state representation.
2. 2.

   Environment Simulator: This simulates the dynamics of liquidity positions, fee accrual, and rebalancing costs.
3. 3.

   DDQN Agent: Learns a solution for the HJB-QVI equation through experience replay and temporal difference learning.

### IV-B State Representation

The agent observes an 8-dimensional state vector 𝐬t\mathbf{s}\_{t} at each timestep, capturing the relationship between the current price StS\_{t}, the position center cc, and the estimated OU parameters. The components are defined as follows:

* •

  Normalized Price Deviation (δp=St/c−1\delta\_{p}=S\_{t}/c-1): Represents the current deviation of the market price from the position center.
* •

  Distance to Edge (de​d​g​ed\_{edge}): A value in the range [−1,1][-1,1] indicating the relative distance to the nearest liquidity range boundary.
* •

  Stein Signal (θ\theta): The mean-reversion speed parameter of the OU process, truncated to [0,1][0,1].
* •

  Mean Deviation (δμ=(μ−St)/St\delta\_{\mu}=(\mu-S\_{t})/S\_{t}): The normalized distance between the current price and the equilibrium price μ\mu to which it is expected to revert.
* •

  Normalized Sigma (σ~\tilde{\sigma}): The diffusion parameter σ\sigma normalized by price, clipped at 0.10.1 to provide a stable volatility signal.
* •

  Active Fraction (ϕa​c​t​i​v​e\phi\_{active}): The cumulative fraction of time the position has spent in-range during the current episode.
* •

  Recent Volatility (vv): Rolling realized volatility (300-second window) clipped at 0.10.1.
* •

  In-Range Indicator (1in1\_{\text{in}}): A binary flag indicating whether the current price StS\_{t} is within the liquidity bounds.

### IV-C Action Space

The action space of the RAmmStein agent is defined as a binary discrete set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜={0,1}\mathcal{A}=\{0,1\} |  | (26) |

where the actions correspond to the following logic:

* •

  a=0a=0 (Hold): The agent remains inactive. The position center stays constant (ct+1=ctc\_{t+1}=c\_{t}), and the system evolves according to the continuation regime.
* •

  a=1a=1 (Rebalance): The agent triggers an immediate rebalancing event. The position center is updated to the current market price, ct+1=Stc\_{t+1}=S\_{t}, and a fixed rebalancing cost CC is incurred.

### IV-D Reward Function

The reward function encodes the agent’s reward after subtracting operational expenses from the total fee revenue. More formally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=Δ​Feest−Δ​GastK⏟Net PnL⋅λ+ϵ⋅1in⏟Active Bonusr\_{t}=\underbrace{\frac{\Delta\text{Fees}\_{t}-\Delta\text{Gas}\_{t}}{K}}\_{\text{Net PnL}}\cdot\lambda+\underbrace{\epsilon\cdot 1\_{\text{in}}}\_{\text{Active Bonus}} |  | (27) |

where:

* •

  Δ​Feest\Delta\text{Fees}\_{t} Total revenue of the position during period tt.
* •

  Δ​Gast\Delta\text{Gas}\_{t} Rebalancing costs incurred (zero if the action is 0).
* •

  KK Initial capital put in the position. This is used to compute ROI.
* •

  λ\lambda A scaling factor to stabilize the training procedure.
* •

  ϵ\epsilon Introduces an inductive bias by encouraging the agent to be in the range.

This reward structure ensures that the agent directly optimizes net ROI.

### IV-E Network Architecture

The Q-function Q​(s,a)Q(s,a) is approximated using a fully-connected neural network. The input layer consists of 8 neurons corresponding to the state vector dimensions, followed by two hidden layers of 128 and 64 neurons with ReLU activations. The output layer comprises 2 neurons representing the Q-values for each action. To ensure training stability, a target network Q−Q^{-} is maintained as described in Section II-F and synchronized with the online network (θ−←θ\theta^{-}\leftarrow\theta) every 100 training steps.

### IV-F Training Procedure

The training procedure is detailed in Algorithm [1](https://arxiv.org/html/2602.19419v1#alg1 "Algorithm 1 ‣ IV-F Training Procedure ‣ IV Methodology ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs"). We use the standard DDQN approach to mitigate overestimation bias by decoupling action selection from target value evaluation. The hyperparameters are listed in Table [I](https://arxiv.org/html/2602.19419v1#S4.T1 "TABLE I ‣ IV-F Training Procedure ‣ IV Methodology ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs").

Algorithm 1  RAmmStein Training

1: Initialize Q-network Q​(s,a;θ)Q(s,a;\theta) with random weights

2: Initialize target network Q−Q^{-} with weights θ−=θ\theta^{-}=\theta

3: Initialize replay buffer 𝒟\mathcal{D} with capacity NN

4: for episode =1=1 to MM do

5:  Sample random starting point in training data

6:  Initialize position at current price

7:  for t=1t=1 to TT do

8:   Observe state sts\_{t}

9:   Select action at={randomw.p. ​ϵarg⁡maxa⁡Q​(st,a)otherwisea\_{t}=\begin{cases}\text{random}&\text{w.p. }\epsilon\\
\arg\max\_{a}Q(s\_{t},a)&\text{otherwise}\end{cases}

10:   Execute action, observe rtr\_{t}, st+1s\_{t+1}

11:   Store (st,at,rt,st+1)(s\_{t},a\_{t},r\_{t},s\_{t+1}) in 𝒟\mathcal{D}

12:   Sample minibatch from 𝒟\mathcal{D}

13:   Compute target: y=r+γ​Q−​(s′,arg⁡maxa′⁡Q​(s′,a′))y=r+\gamma Q^{-}(s^{\prime},\arg\max\_{a^{\prime}}Q(s^{\prime},a^{\prime}))

14:   Update θ\theta by gradient descent on (y−Q​(s,a))2(y-Q(s,a))^{2}

15:   if tmod100=0t\mod 100=0 then

16:    θ−←θ\theta^{-}\leftarrow\theta

17:   end if

18:  end for

19:  Decay ϵ\epsilon

20: end for

  



TABLE I: Training Hyperparameters

| Parameter | Value |
| --- | --- |
| Learning rate | 10−410^{-4} |
| Discount factor γ\gamma | 0.99 |
| Replay buffer size | 100,000 |
| Batch size | 128 |
| Target update frequency | 100 steps |
| ϵ\epsilon start / end / decay | 1.0 / 0.05 / 0.9998 |
| Episodes | 300 |
| Episode length | 36,000 steps (10 hours) |

## V Experimental Setup

### V-A Dataset and Preprocessing

We utilize a comprehensive high-frequency dataset of ETH-USD trades observed on the Coinbase WebSocket feed, spanning two weeks from January 20 to February 3, 2026. This period captures significant market volatility, with a price range of $2,108 to $3,067 and a net price decline of 26.2%. The raw data consists of 6.8 million individual trades and is aggregated into 1Hz OHLCV bars. The one-second resolution is critical for capturing mean-reversion behavior. Lower-frequency data, such as one-minute candles, would obscure the micro-level dynamics.

To get an unbiased estimate of the agent’s performance and prevent look-ahead bias, we divide the dataset into training, validation, and testing subsets: the first 10 days (70%) are used for training, the next 2 days (15%) for validation and hyperparameter tuning, and the final 2 days (15%) for out-of-sample testing.

### V-B Environment and Fee Estimation

The environment is configured to mimic a Uniswap V3-style pool with parameters listed in Table [II](https://arxiv.org/html/2602.19419v1#S5.T2 "TABLE II ‣ V-B Environment and Fee Estimation ‣ V Experimental Setup ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs").
To estimate DEX trading volume from our CEX price source, we adopt a volume scaling approach: VD​E​X=α⋅VC​E​XV\_{DEX}=\alpha\cdot V\_{CEX}, where α=0.10\alpha=0.10. This 10% ratio is consistent with observed market structures for major pairs.

TABLE II: Environment Parameters

| Parameter | Value |
| --- | --- |
| Range width | 0.2% (20 bps) |
| Pool fee tier (ϕ\phi) | 0.05% |
| Gas cost (GG) | $2.00 USD |
| Initial capital (KK) | $10,000 USD |
| Pool TVL (Lp​o​o​lL\_{pool}) | $500,000 |
| DEX/CEX volume ratio (α\alpha) | 10% |

The fee accrual per timestep is computed as Feet=VD​E​X,t⋅ϕ⋅LL​P⋅λLp​o​o​l\text{Fee}\_{t}=V\_{DEX,t}\cdot\phi\cdot\frac{L\_{LP}\cdot\lambda}{L\_{pool}}, where λ\lambda is the concentration multiplier. The total rebalancing cost CC includes both the fixed gas cost GG and a proportional swap fee:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=ϕ⋅0.5⋅K⏟Swap fee+G⏟GasC=\underbrace{\phi\cdot 0.5\cdot K}\_{\text{Swap fee}}+\underbrace{G}\_{\text{Gas}} |  | (28) |

This assumes approximately 50% of the position is swapped to maintain the desired inventory delta during recentering.

### V-C OU Parameter Estimation

The OU parameters are estimated via rolling Ordinary Least Squares (OLS) on a 1,800-second window. We regress St+1−StS\_{t+1}-S\_{t} on StS\_{t} to derive the coefficients (α^t,β^t)(\hat{\alpha}\_{t},\hat{\beta}\_{t}), from which the OU parameters are extracted:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^t=1−β^tΔ​t,μ^t=α^t1−β^t\hat{\theta}\_{t}=\frac{1-\hat{\beta}\_{t}}{\Delta t},\quad\hat{\mu}\_{t}=\frac{\hat{\alpha}\_{t}}{1-\hat{\beta}\_{t}} |  | (29) |

In the dataset, we observe strong mean-reversion (θ>0.01\theta>0.01) in 8.7% of observations. The vast majority exhibit weak mean-reversion. The median θ\theta value is 0.00560.0056, corresponding to a half-life of slightly more than two minutes. This validates our hypothesis that deviations arising from market microstructure typically revert within minutes. During such periods, the optimal strategy for the agent is to wait rather than react.

## VI Comparative Strategies\*\*\*Baseline strategies are named after knights and figures from Arthurian legend, reflecting their personalities.

To evaluate RAmmStein, we compare its performance against four baseline strategies for LP management that range from passive to aggressive liquidity management.

### VI-A The Merlin Baseline (Omniscient Oracle)

This strategy represents an upper bound on the passive performance. The liquidity position is initialized with a range [Smin,Smax][S\_{\text{min}},S\_{\text{max}}] so that the position is active during the entire test.

|  |  |  |  |
| --- | --- | --- | --- |
|  | c=Smin+Smax2,w=Smax−Smin2​cc=\frac{S\_{\text{min}}+S\_{\text{max}}}{2},\quad w=\frac{S\_{\text{max}}-S\_{\text{min}}}{2c} |  | (30) |

This strategy is unrealistic as it requires future knowledge. However, it achieves 100% active time and has no additional costs after initializing the position.

### VI-B The Bedivere Baseline (Fixed Passive)

A narrow 20 bps range is set at the initial price and never adjusted (c=S0,w=0.002c=S\_{0},w=0.002). If the price exits the range, the position remains inactive until it returns naturally. This strategy aims to completely avoid rebalancing costs.

### VI-C The Lancelot Strategy (Greedy Rebalancing)

In this strategy, the position is always in a narrow range around the current price. If the price exits the range, the position is immediately recentered.

|  |  |  |  |
| --- | --- | --- | --- |
|  | If ​St∉[c​(1−w),c​(1+w)]⟹c←St\text{If }S\_{t}\notin[c(1-w),c(1+w)]\implies c\leftarrow S\_{t} |  | (31) |

This strategy aims to maximize the active time and at the same time incurs the maximum rebalancing costs. We show that this myopic behavior does not completely recover the friction costs via the fee.

### VI-D The Galahad Strategy (LSTM)

In this strategy, a Long Short-Term Memory (LSTM) network is trained to predict the future price St+HS\_{t+H} based on historical prices, volume, and OU parameters.

|  |  |  |  |
| --- | --- | --- | --- |
|  | S^t+H=LSTM​(St−L:t,Vt−L:t,θt−L:t,μt−L:t,σt−L:t)\hat{S}\_{t+H}=\text{LSTM}(S\_{t-L:t},V\_{t-L:t},\theta\_{t-L:t},\mu\_{t-L:t},\sigma\_{t-L:t}) |  | (32) |

This strategy recenters the liquidity position at the predicted price. It is more sophisticated than simple threshold-based approaches, but critically, it does not account for rebalancing costs.

### VI-E RAmmStein (Proposed)

Our DDQN-based agent observes the full eight-dimensional state vector and selects the optimal action: at=arg⁡maxa⁡Q​(st,a;θ∗)a\_{t}=\arg\max\_{a}Q(s\_{t},a;\theta^{\*}). The agent learns to wait for the price to re-enter naturally during high-θ\theta regimes.

## VII Evaluation Metrics

We use the following metrics to compare the different strategies:

* •

  Active Fraction (Φ\Phi): The percentage of time the market price resides within the position’s range. Higher values of this metric represent higher asset utilization.
* •

  Normalized Liquidity (Λ\Lambda): A measure of the concentration of the position. This depends inversely on the w\sqrt{w}, (1/w1/\sqrt{w}). A 0.2% width achieves Λ≈22.3×\Lambda\approx 22.3\times.
* •

  Rebalance Count (NN): The total number of discrete rebalancing actions. Lower counts represent lower operational costs.
* •

  Net ROI: The primary metric that the strategies aim to optimize. It is the return on investment after all operational costs:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Net ROI=Total Fees−Total GasInitial Capital\text{Net ROI}=\frac{\text{Total Fees}-\text{Total Gas}}{\text{Initial Capital}} |  | (33) |

## VIII Experimental Results

In this section, we present the results of evaluating the different strategies on the out-of-sample subset of the dataset.

### VIII-A Main Comparison

The primary results are summarized in Table [III](https://arxiv.org/html/2602.19419v1#S8.T3 "TABLE III ‣ VIII-A Main Comparison ‣ VIII Experimental Results ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs"). RAmmStein achieves the highest net ROI of 0.7159%, outperforming all other strategies, including the theoretically superior Merlin baseline.

TABLE III: Strategy Comparison on Test Data

| Strategy | Active% | Rebal. | Accrued Fees ($) | Net ROI |
| --- | --- | --- | --- | --- |
| Merlin (Omniscient) | 100.00% | 1 | 53.18 | 0.4868% |
| Bedivere (Passive) | 31.65% | 1 | 34.87 | 0.3037% |
| Lancelot (Greedy) | 100.00% | 9 | 97.09 | 0.5663% |
| Galahad (LSTM) | 60.67% | 3 | 62.28 | 0.4879% |
| RAmmStein | 88.30% | 3 | 85.08 | 0.7159% |

The fee accrual across strategies is consistent with our simulation model. While Merlin is active during 100% of the test duration with low concentration (λ≈2.36\lambda\approx 2.36), the other concentrated strategies achieve ∼\sim13.4x higher concentration (λ≈31.62\lambda\approx 31.62). The non-linearities between Active% and Fees (between Galahad and Bedivere strategies) are attributable to the non-uniformity of the trading volume.

Despite maintaining a less active time compared to Lancelot (88.3% vs 100%), the agent’s 67% reduction in rebalancing frequency results in significant savings. These savings more than compensate for the slight reduction in fee accrual, leading to a 26% higher net return than the greedy Lancelot strategy.

### VIII-B The θ\theta Effect

Analysis of the trained agent’s QQ-values reveals a clear dependence on the OU parameter θ\theta. This dependence can be visualized in the decision boundary heatmap in Figure [1](https://arxiv.org/html/2602.19419v1#S8.F1 "Figure 1 ‣ VIII-B The θ Effect ‣ VIII Experimental Results ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs"). The heatmap shows the value difference Q​(action=1)−Q​(action=0)Q(\text{action=1})-Q(\text{action=0}) versus the mean-reversion speeds (θ\theta) and the distance of the price to the position’s edge.

![Refer to caption](decision_boundary.png)


Figure 1: Learned decision boundary showing the θ\theta parameter. The heatmap represents the preference for active intervention (Q>0Q>0, red) versus the “option to wait” (Q<0Q<0, green).

We note the following key behaviors of the agent from the heatmap:

* •

  Waiting for reversion: The agent chooses to hold (green, Q value of action=0 is higher) across the vast majority of the state space. This confirms that the agent is patient to wait for the price to recenter and does not chase the total active time at the expense of increased friction costs.
* •

  Asymmetric Rebalancing: The agent exhibits an asymmetric rebalancing threshold. It is visible at the lower edge (y≈−1.0y\approx-1.0) but absent at the upper edge. This observation is consistent with the 26.2% net price decline. The agent has internalized the directional risk and learned to proactively recenter during periods of downward pressure. At the same time, it has also learned to avoid recentering during temporary bounces.
* •

  θ\theta Sensitivity: As θ\theta increases, the boundary for rebalancing shifts. The agent requires deeper deviations before it considers a rebalancing event.
* •

  Non-linear Boundary: The non-linear transition from inaction to action captures the complex relationship between the OU parameters and the rewards.

This visual evidence confirms that RAmmStein has successfully internalized the information provided by the Stein Signal. By calculating the probability of a natural return to range, the agent achieves the 67% reduction in rebalancing frequency observed in the main results.

### VIII-C Gas Sensitivity Analysis

We now evaluate the strategies across varying gas cost regimes in Table [IV](https://arxiv.org/html/2602.19419v1#S8.T4 "TABLE IV ‣ VIII-C Gas Sensitivity Analysis ‣ VIII Experimental Results ‣ RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein thresholds* Optimal Impulse Control in Concentrated AMMs"). RAmmStein maintains a significant advantage (ROI of RAmmStein versus ROI of Lancelot) that scales with the gas costs per intervention.

TABLE IV: Net ROI vs. Gas Cost

| Gas (USD) | Lancelot (Greedy) | RAmmStein |
| --- | --- | --- |
| $1.00 | 0.6568% | 0.7461% |
| $2.00 | 0.5663% | 0.7159% |
| $5.00 | 0.2949% | 0.6253% |
| $10.00 | -0.1575% | 0.4745% |
| $20.00 | -1.0623% | 0.1727% |
| $50.00 | -3.7765% | -0.7326% |

At a $10 gas cost, Lancelot becomes unprofitable due to excessive rebalancing costs, while RAmmStein continues to provide positive returns. We found that the break-even gas cost for Lancelot is ≈9​U​S​D\approx 9USD and for RAmmStein the break-even is at ≈35​U​S​D\approx 35USD, a 4x increase in gas cost tolerance. This highlights the importance of waiting to rebalance.

### VIII-D Decision Analysis

The experimental results show that while Lancelot treats every range exit as a reason to rebalance, RAmmStein learned to defer rebalancing when the market is in a high-θ\theta regime. This selective approach resulted in fewer rebalances and increased ROI over all other strategies.

## IX Discussion

### IX-A The Value of Regime Awareness

Our results clearly show that incorporating market regime information significantly improves LP returns. The OU parameters provide well-defined features capturing regime dynamics that are invisible to models based on price information alone. Our agent learns to quantify the value of the waiting option.

### IX-B Implications for LP Tooling

Existing tools for LP management typically follow a Lancelot-style strategy that chases active time over cost efficiency. Our analysis suggests that ROI can be improved by moving away from fixed heuristics towards models that base decisions on:

* •

  OU parameters that measure mean-reversion strength.
* •

  Conditions for triggering rebalance.
* •

  Costs for rebalancing events.

### IX-C Limitations and Future Work

Several limitations warrant acknowledgment. Our work focuses on a single asset pair; measuring the effectiveness of the approach on more volatile and lower-liquidity pairs remains to be validated. We also assume a fixed pool share for the liquidity provider and that the OU parameters are locally stationary within the estimation window.

Extensions of our work include integration of a gas price prediction into the state to further optimize the timing of the interventions. Moreover, preventing or minimizing MEV risks during rebalancing is an important direction that warrants detailed analysis. Another interesting future research direction is to expand the action space from binary to a continuous one representing the rebalancing width. The continuous action space allows the agent to adjust the concentration parameter based on the market dynamics.

## X Conclusion

This paper introduced RAmmStein, a Deep Reinforcement Learning framework for managing concentrated liquidity positions in AMMs. By framing LP rebalancing as an impulse control problem and incorporating the Ornstein-Uhlenbeck parameters of price dynamics as a prior, our agent learns a dynamic laziness boundary that adapts to the market conditions.

Extensive backtesting on 1Hz data demonstrated that our agent achieves a superior ROI compared to a range of meaningful passive and aggressive baseline strategies.

The key takeaway from our results is that deferring rebalancing decisions preserves capital that would otherwise be eroded by friction costs.

As DeFi matures, we anticipate that ML approaches that incorporate signals from quantitative finance will be increasingly used in liquidity management. RAmmStein presents a step towards that automation.

## Note

This paper has been submitted to the Designing DeFi workshop (<https://www.designingdefi.xyz/>).

## References

* [1]

  H. Adams, N. Zinsmeister, and D. Robinson, “Uniswap v2 core,” 2020. [Online].
  Available: <https://app.uniswap.org/whitepaper.pdf>
* [2]

  H. Adams, N. Zinsmeister, M. Salem, R. Keefer, and D. Robinson, “Uniswap v3
  core,” 2021. [Online]. Available:
  <https://app.uniswap.org/whitepaper-v3.pdf>
* [3]

  M. Egorov, “Stableswap – efficient mechanism for stablecoin liquidity,”
  2019. [Online]. Available:
  <https://berkeley-defi.github.io/assets/material/StableSwap.pdf>
* [4]

  D. White, D. Robinson, and C. Moallemi, “Orbital,” Paradigm, 2025. [Online].
  Available: <https://www.paradigm.xyz/2025/06/orbital>
* [5]

  A. Elsts, “Liquidity math in uniswap v3,” *SSRN Electronic Journal*,
  2023.
* [6]

  S. Loesch, N. Hindman, M. B. Richardson, and N. Welch, “Impermanent loss in
  uniswap v3,” 2021. [Online]. Available:
  <https://arxiv.org/abs/2111.09192>
* [7]

  G. Lambert, “Uniswap v3: A quant framework,” Lambert’s Newsletter, 2022.
* [8]

  J. Milionis, C. C. Moallemi, T. Roughgarden, and A. L. Zhang, “Automated
  market making and loss-versus-rebalancing,” 2022. [Online]. Available:
  <https://arxiv.org/abs/2208.06046>
* [9]

  L. Heimbach, Y. Wang, and R. Wattenhofer, “Behavior of liquidity providers in
  decentralized exchanges,” in *Proc. Crypto Valley Conference on
  Blockchain Technology (CVCBT)*, 2021.
* [10]

  J. A. Berg, R. Fritsch, L. Heimbach, and R. Wattenhofer, “An empirical study
  of market inefficiencies in uniswap and sushiswap,” in *Proc.
  Blockchain*, 2022. [Online]. Available:
  <https://arxiv.org/abs/2203.07774>
* [11]

  L. Heimbach, E. Schertenleib, and R. Wattenhofer, “Risks and returns of
  uniswap v3 liquidity providers,” in *Proc. 4th ACM Conference on
  Advances in Financial Technologies (AFT)*, 2022.
* [12]

  R. Fritsch, “Concentrated liquidity in automated market makers,” in
  *Proc. ACM CCS Workshop on Decentralized Finance and Security (DeFi)*,
  2021.
* [13]

  A. Evans, “Liquidity provider returns in geometric mean markets,” 2020.
  [Online]. Available: <https://arxiv.org/abs/2006.08806>
* [14]

  A. Cartea, F. Drissi, and M. Monga, “Decentralized finance and automated
  market making: Predictable loss and optimal liquidity provision,” *SIAM
  Journal on Financial Mathematics*, vol. 15, no. 3, pp. 931–959, 2024.
* [15]

  J. Milionis, C. C. Moallemi, and T. Roughgarden, “A myersonian framework for
  optimal liquidity provision in automated market makers,” 2023.
* [16]

  Y. Bar-On and Y. Mansour, “Uniswap liquidity provision: An online learning
  approach,” in *Lecture Notes in Computer Science*. Springer, 2023, pp. 247–261.
* [17]

  Z. Fan, F. Marmolejo-Cossío, D. J. Moroz, M. Neuder, R. Rao, and D. C.
  Parkes, “Strategic liquidity provision in uniswap v3,” 2023. [Online].
  Available: <https://arxiv.org/abs/2106.12033>
* [18]

  A. Urusov, R. Berezovskiy, A. Krestenko, and A. Kornilov, “Liquidity provision
  with τ\tau-reset strategies: a dynamic historical liquidity approach,”
  2025. [Online]. Available: <https://arxiv.org/abs/2505.15338>
* [19]

  H. Zhang, X. Chen, and L. F. Yang, “Adaptive liquidity provision in uniswap v3
  with deep reinforcement learning,” 2023. [Online]. Available:
  <https://arxiv.org/abs/2309.10129>
* [20]

  H. Xu and A. Brini, “Improving defi accessibility through efficient liquidity
  provisioning with deep reinforcement learning,” in *Proc. AAAI*, 2025.
  [Online]. Available: <https://arxiv.org/abs/2501.07508>
* [21]

  S. Jaimungal, Y. F. Saporito, M. O. Souza, and Y. Thamsten, “Optimal trading
  in automatic market makers with deep learning,” 2023. [Online]. Available:
  <https://arxiv.org/abs/2304.02180>
* [22]

  A. Bensoussan and J.-L. Lions, *Impulse Control and Quasi-variational
  Inequalities*. Gauthier-Villars, 1984.
* [23]

  G. E. Uhlenbeck and L. S. Ornstein, “On the theory of the brownian motion,”
  *Physical Review*, vol. 36, no. 5, pp. 823–841, 1930.
* [24]

  O. Vasicek, “An equilibrium characterization of the term structure,”
  *Journal of Financial Economics*, vol. 5, no. 2, pp. 177–188, 1977.
* [25]

  B. Efron and C. Morris, “Stein’s paradox in statistics,” *Scientific
  American*, vol. 236, no. 5, pp. 119–127, 1977.
* [26]

  D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. van den Driessche,
  J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, S. Dieleman,
  D. Grewe, J. Nham, N. Kalchbrenner, I. Sutskever, T. Lillicrap, M. Leach,
  K. Kavukcuoglu, T. Graepel, and D. Hassabis, “Mastering the game of go with
  deep neural networks and tree search,” *Nature*, vol. 529, no. 7587,
  pp. 484–489, 2016.
* [27]

  S. Levine, C. Finn, T. Darrell, and P. Abbeel, “End-to-end training of deep
  visuomotor policies,” *Journal of Machine Learning Research*, vol. 17,
  no. 39, pp. 1–40, 2016.
* [28]

  Z. Jiang, D. Xu, and J. Liang, “A deep reinforcement learning framework for
  the financial portfolio management problem,” 2017. [Online]. Available:
  <https://arxiv.org/abs/1706.10059>
* [29]

  T. Spooner, J. Fearnley, R. Savani, and A. Koukorinis, “Market making via
  reinforcement learning,” in *Proceedings of AAMAS*, 2018.
* [30]

  B. Ning, F. H. T. Ling, and S. Jaimungal, “Double deep q-learning for optimal
  execution,” *Applied Mathematical Finance*, vol. 28, no. 4, pp.
  361–380, 2021.
* [31]

  A. Mamageishvili and E. Felten, “Efficient rollup batch posting strategy on
  base layer,” 2023. [Online]. Available:
  <https://fc23.ifca.ai/wtsc/WTSC23_1.pdf>
* [32]

  R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*,
  2nd ed. MIT Press, 2018.
* [33]

  V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare,
  A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski, S. Petersen,
  C. Beattie, A. Sadik, I. Antonoglou, H. King, D. Kumaran, D. Wierstra,
  S. Legg, and D. Hassabis, “Human-level control through deep reinforcement
  learning,” *Nature*, vol. 518, no. 7540, pp. 529–533, 2015.
* [34]

  H. Van Hasselt, A. Guez, and D. Silver, “Deep reinforcement learning with
  double q-learning,” in *Proceedings of AAAI*, 2016.
* [35]

  R. J. Elliott, J. Van Der Hoek, and W. P. Malcolm, “Pairs trading,”
  *Quantitative Finance*, vol. 5, no. 3, pp. 271–276, 2005.