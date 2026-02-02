---
authors:
- Robert de Witt
- Mikko S. Pakkanen
doc_id: arxiv:2601.22113v2
family_id: arxiv:2601.22113
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Diverse Approaches to Optimal Execution Schedule Generation
url_abs: http://arxiv.org/abs/2601.22113v2
url_html: https://arxiv.org/html/2601.22113v2
venue: arXiv q-fin
version: 2
year: 2026
---


Robert de Witt
  
Imperial College London
  
Bank of America Securities
  
London, United Kingdom
  
robert.de-witt23@imperial.ac.uk
  
robert.de\_witt@bofa.com
&Mikko S. Pakkanen
  
Department of Mathematics
  
Imperial College London
  
London, United Kingdom
  
m.pakkanen@imperial.ac.uk
The views, opinions and conclusions expressed here are solely those of the authors and do not necessarily reflect the views or policies of the Bank of America, or any other institution with which the authors are affiliated. No responsibility should be attributed to those institutions . This article has not been reviewed, approved, or endorsed by the authors’ employers or any affiliated organizations

###### Abstract

We present the first application of MAP-Elites, a quality-diversity algorithm,
to trade execution. Rather than searching for a single optimal policy,
MAP-Elites generates a diverse portfolio of regime-specialist strategies
indexed by liquidity and volatility conditions. Individual specialists achieve
8-10% performance improvements within their behavioural niches, while other
cells show degradation, suggesting opportunities for ensemble approaches that
combine improved specialists with the baseline PPO policy. Results indicate
that quality-diversity methods offer promise for regime-adaptive execution,
though substantial computational resources per behavioural cell may be required
for robust specialist development across all market conditions.

To ensure experimental integrity, we develop a calibrated Gymnasium environment
focused on order scheduling rather than tactical placement decisions. The
simulator features a transient impact model with exponential decay and
square-root volume scaling, fit to 400+ U.S. equities with R2>0.02R^{2}>0.02
out-of-sample. Within this environment, two Proximal Policy Optimization
architectures—both MLP and CNN feature extractors—demonstrate substantial
improvements over industry baselines, with the CNN variant achieving 2.13 bps
arrival slippage versus 5.23 bps for VWAP on 4,900 out-of-sample orders
($21B notional). These results validate both the simulation realism and
provide strong single-policy baselines for quality-diversity methods.

*Keywords* Optimal Execution ⋅\cdot
Reinforcement Learning ⋅\cdot
Market Impact ⋅\cdot
Transient Impact ⋅\cdot
Quality-Diversity ⋅\cdot
MAP-Elites ⋅\cdot
Algorithmic Trading ⋅\cdot
Robotics

## 1 Introduction

Optimal Execution


Empirical Impact Models
(e.g., Bouchaud Propagator)
Calibrated decay kernel, transient impact, concave scaling

Classical Models
(e.g., Almgren–Chriss)
Mean–variance optimisation, constant volatility, stationary impact

Reinforcement Learning Approaches
Agent–environment loop, adaptive policies, simulation-trained

This Work:
Novel RL Optimal Execution
PPO, MAP-Elites, High-fidelity Gymnasium environment, calibrated transient impact, realistic order generation, vectorised simulation


Figure 1: Evolution of optimal execution approaches: from classical models to empirical impact models to reinforcement learning, with this work positioned at the intersection of empirically calibrated models and RL methods.

Optimal execution (OE) is a central problem in algorithmic trading, influencing approximately a trillion dollars of daily turnover across global equities and futures markets. It concerns determining how to trade a given order over a predetermined or dynamic horizon while minimising transaction costs relative to a benchmark, typically the *arrival price*—the mid-quote at the time the order is initiated. This performance is often expressed as *implementation shortfall* (Perold,, [1988](https://arxiv.org/html/2601.22113v2#bib.bib21)), the difference between the value of an ideally priced portfolio and the actual cost of implementing it through trading. Transaction costs arise from explicit sources (e.g., commissions and fees) and implicit sources (e.g., market impact and slippage). The execution challenge is compounded by the stochastic nature of prices, variable liquidity conditions, and the trade-off between market impact and timing risk (Almgren and Chriss,, [2001](https://arxiv.org/html/2601.22113v2#bib.bib1)).

The evolution of optimal execution approaches is outlined in Figure [1](https://arxiv.org/html/2601.22113v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Diverse Approaches to Optimal Execution Schedule Generation"). Traditional approaches, such as the seminal Almgren-Chriss framework, cast the execution problem as a mean-variance optimisation in which market impact is modelled as an additive cost and risk is penalised via price variance. While yielding tractable closed-form schedules (e.g., linear, front-loaded, or back-loaded trajectories), these models assume constant volatility, stationary impact functions, and exogenous order flow (Almgren and Chriss,, [2001](https://arxiv.org/html/2601.22113v2#bib.bib1); Obizhaeva and Wang,, [2013](https://arxiv.org/html/2601.22113v2#bib.bib19)). Empirical studies show that market impact scales concavely with order size and decays transiently over time (Bouchaud,, [2010](https://arxiv.org/html/2601.22113v2#bib.bib3); Bouchaud et al.,, [2018](https://arxiv.org/html/2601.22113v2#bib.bib4)), motivating richer dynamic models.

In recent years, alongside other data-driven approaches, reinforcement learning (RL) has emerged as a promising alternative for OE (Nevmyvaka et al.,, [2006](https://arxiv.org/html/2601.22113v2#bib.bib18); Hendricks and Wilcox,, [2014](https://arxiv.org/html/2601.22113v2#bib.bib12)). RL agents can learn adaptive policies that respond to evolving market states without assuming explicit parametric forms for price dynamics or impact decay. The agent-environment loop in Gymnasium (Towers et al.,, [2024](https://arxiv.org/html/2601.22113v2#bib.bib27)) offers a natural abstraction: the agent observes the current market state (e.g., prices, volumes, volatility, time remaining, inventory) and outputs an action representing a trade size or participation rate. The environment then simulates execution, applies market impact, updates the state, and returns a reward signal tied to execution performance. This process enables the agent to learn policies through simulation without incurring the cost and risk of live experimentation; once deployed, such policies can be further adapted using live trading outcomes.

However, much of the existing RL literature for OE suffers from limited realism in backtesting. Many implementations use oversimplified price dynamics (e.g., geometric Brownian motion) or neglect empirically calibrated market impact, while others focus on highly granular limit order book (LOB) simulations that require many structural assumptions and can diverge from practical execution workflows. This paper takes a middle path, avoiding both coarse-grained price-only models and overly complex LOB simulations. It builds a high-fidelity Gymnasium-based back-testing environment calibrated to one year of historical minute-bar data for hundreds of US equities. The environment integrates a transient market impact model fit via cross-validation, realistic order-arrival processes, and configurable state/reward designs, enabling a robust evaluation of RL and baseline strategies.

We utilise this environment to train RL policies designed to decide how much to trade at any point in an order’s lifespan. The generated policy is not concerned with what limit price, type, or venue to use, but rather the schedule of quantities to trade, given a reward-driven objective. With the right reward structure and cost function, this approach could, in principle, generalise beyond volume-weighted average price (VWAP) to improve upon present-day execution schedules such as time-weighted average price (TWAP), percentage of volume (POV), implementation shortfall, or liquidity-seeking strategies. We focus on an optimised VWAP structure which aims to reduce slippage to the order arrival price by allowing some discretion to a base VWAP schedule. We choose this as an initial approach as there are immediate large-scale applications for an optimally performing scheduler. This structure greatly simplifies the action space of the RL algorithm while opening up flexibility for a highly informative state space to act on, increasing the likelihood of superior decisions can be learned in simulation.

A key limitation of existing RL approaches to execution is that they optimise
for a single policy maximizing average performance across all market conditions.
Quality-diversity (QD) algorithms (Chatzilygeroudis et al.,, [2021](https://arxiv.org/html/2601.22113v2#bib.bib6)), developed originally for adaptive robotics,
offer an alternative paradigm. Rather than searching for a single optimum, QD
methods such as MAP-Elites (Mouret and Clune,, [2015](https://arxiv.org/html/2601.22113v2#bib.bib17)) generate portfolios of
high-performing policies, each specialised for different behavioural niches
defined by descriptor features. In robotics, these descriptors might characterise
terrain type or gait stability; in optimal execution, natural descriptors include
market regime (volatility, liquidity), order urgency, or directional momentum.
We apply MAP-Elites using liquidity and volatility as behavioural descriptors to
generate regime-specialist execution policies. To our knowledge, this is the
first application of quality-diversity methods to the optimal execution problem.

The contributions of this work are:

1. 1.

   First application of quality-diversity methods to financial
   execution. We apply MAP-Elites to generate portfolios of regime-specialist
   execution policies indexed by liquidity-volatility descriptors. While
   individual specialists achieve 8-10% improvements in specific niches,
   results reveal challenges in regime classification and training data density
   that motivate future research. To our knowledge, this is the first exploration
   of quality-diversity algorithms for trading.
2. 2.

   Validation of RL under empirically calibrated transient impact.
   Using a propagator model with exponential decay and square-root scaling
   (R2>0.02R^{2}>0.02 out-of-sample), we demonstrate PPO-CNN achieves 59% lower arrival
   slippage than VWAP (2.13 vs 5.23 bps) on $21B test set. This establishes
   both a strong baseline for quality-diversity methods and validates that RL
   can exceed industry benchmarks under realistic impact dynamics.
3. 3.

   GEO: Open-source environment enabling reproducible execution
   research. We plan to release a calibrated Gymnasium simulator with realistic order
   generation, minute-bar execution, and transient impact modeling. This
   infrastructure enables fair comparison of execution algorithms and supports
   future quality-diversity research.

The remainder of this paper is structured as follows. Section [2](https://arxiv.org/html/2601.22113v2#S2 "2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation") introduces the problem formulation and proposed solutions. We begin with the optimal execution set-up, including the formal problem statement, the transient impact model with its calibration, and the construction of raw and derived features. We then introduce reinforcement learning, translating OE into the RL framework and outlining the order generation process. Next, we present the RL methods explored, covering architecture variations (MLP and CNN) of Proximal Policy Optimisation (PPO) and Quality-Diversity approaches (MAP-Elites) and industry-standard execution strategies. Finally, we describe how these components fit into the simulation environment design, including Gymnasium integration and the execution simulator with impact. Section [3](https://arxiv.org/html/2601.22113v2#S3 "3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation") reports the impact model calibration results and compares the performance of the RL agents against standard benchmarks. Section [4](https://arxiv.org/html/2601.22113v2#S4 "4 Discussion ‣ Diverse Approaches to Optimal Execution Schedule Generation") concludes with implications of our findings, limitations of the framework, and potential directions for future research.

## 2 Methods

### 2.1 Optimal Execution Problem Set-up

#### 2.1.1 Fundamental OE problem formulation

We consider the execution of a single parent order of size Q0Q\_{0} shares over a fixed horizon of HH discrete time steps, each corresponding to one minute of market time. The order size Q0Q\_{0}, horizon HH, and stock S0S\_{0} are specified by the portfolio manager. While one could also consider continuous or event-driven time-steps, for simplicity we work with minute-binned outcomes.

The objective is to minimise the *implementation shortfall* (IS) relative to the mid-price (pbid+pask)/2(p\_{\text{bid}}+p\_{\text{ask}})/2 at the start of the order, p0p\_{0}:

|  |  |  |
| --- | --- | --- |
|  | IS=side×(∑t=0H−1ptfill⋅|qt|Q0−p0),\mathrm{IS}=\mathrm{side}\times\left(\frac{\sum\_{t=0}^{H-1}p^{\mathrm{fill}}\_{t}\cdot|q\_{t}|}{Q\_{0}}-p\_{0}\right), |  |

where side∈{+1,−1}\mathrm{side}\in\{+1,-1\} indicates a buy or sell order, and qtq\_{t} is the signed quantity traded at time tt at the price ptfillp^{\text{fill}}\_{t}. This expression is equivalent to the realised VWAP of the executed order minus the benchmark price, scaled by trade direction.

The realised fill price, in reality, is the volume weighted average price (VWAP) of the shares traded in the market. In simulation, ptfillp^{\mathrm{fill}}\_{t} incorporates both the prevailing historical market VWAP and the total price impact ItI\_{t} (immediate plus propagated) generated by the trade. Here ItI\_{t} is modelled through the transient propagator framework (Bouchaud,, [2010](https://arxiv.org/html/2601.22113v2#bib.bib3); Bouchaud et al.,, [2018](https://arxiv.org/html/2601.22113v2#bib.bib4)), detailed in Section [2.1.2](https://arxiv.org/html/2601.22113v2#S2.SS1.SSS2 "2.1.2 Propagator Model (Transient Impact Model) ‣ 2.1 Optimal Execution Problem Set-up ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation"). Incorporating such impact-adjusted fills is one of the key differentiators of this work to ensure realism when training our models.

Since the arrival price is only a single point in time benchmark, to better measure our execution efficiency within the horizon HH, we also consider a second benchmark for robustness: slippage relative to market VWAP

|  |  |  |
| --- | --- | --- |
|  | PVWAP=∑t=0H−1vt​pt∑t=0H−1vt,P^{\mathrm{VWAP}}=\frac{\sum\_{t=0}^{H-1}v\_{t}\,p\_{t}}{\sum\_{t=0}^{H-1}v\_{t}}, |  |

where vtv\_{t} is traded volume and ptp\_{t} is the filled price at time tt.

#### 2.1.2 Propagator Model (Transient Impact Model)

As with all reinforcement learning policy optimisations, the realism of the simulation environment directly impacts the quality of the learned action policy. If the simulation dynamics diverge materially from the “physical laws” governing markets, then the resulting strategies will be suboptimal when deployed. While exchange microstructure rules can be simulated with reasonable fidelity, modelling the impact of incremental orders on market prices at one-minute granularity is far more challenging. Fortunately, thanks to the work of Bouchaud, ([2010](https://arxiv.org/html/2601.22113v2#bib.bib3)); Bouchaud et al., ([2018](https://arxiv.org/html/2601.22113v2#bib.bib4)); Obizhaeva and Wang, ([2013](https://arxiv.org/html/2601.22113v2#bib.bib19)); Gatheral et al., ([2012](https://arxiv.org/html/2601.22113v2#bib.bib10)), the *propagator model* provides a tractable framework to capture transient market impact. This formulation allows the impact of each executed trade to propagate forward in time with a decaying influence on prices. Given our one-minute granularity, where there may be intermittent gaps, we find the transient impact model with an *exponential decay kernel* to be the most suitable for simulation.

##### General formulation.

Let ϵt∈{+1,−1}\epsilon\_{t}\in\{+1,-1\} denote the trade sign (buy or sell), qtq\_{t}
the agent’s traded quantity, and VtV\_{t} the market volume at time tt. The
return at time tt is modelled as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=∑ℓ=1LG​(ℓ)​f​(qt−ℓ,Vt−ℓ)​ϵt−ℓ+ηt,r\_{t}=\sum\_{\ell=1}^{L}G(\ell)\,f(q\_{t-\ell},V\_{t-\ell})\,\epsilon\_{t-\ell}+\eta\_{t}, |  | (1) |

where G​(ℓ)G(\ell) is the propagator kernel describing how impact at lag ℓ\ell
decays over time, f​(q,V)f(q,V) is the instantaneous impact function, and ηt\eta\_{t}
is exogenous noise.

The cumulative transient impact ItI\_{t}, which shifts the fill prices in the execution simulator (cf. Section [2.1](https://arxiv.org/html/2601.22113v2#S2.SS1 "2.1 Optimal Execution Problem Set-up ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation")), is then

|  |  |  |
| --- | --- | --- |
|  | It=∑ℓ=1LG​(ℓ)​f​(vt−ℓ)​ϵt−ℓ.I\_{t}=\sum\_{\ell=1}^{L}G(\ell)\,f(v\_{t-\ell})\,\epsilon\_{t-\ell}. |  |

##### Instantaneous impact.

The instantaneous impact function scales as a power law in the participation rate:

|  |  |  |
| --- | --- | --- |
|  | f​(q,V)=γ​(qV)β,β∈(0,1),f(q,V)=\gamma\left(\frac{q}{V}\right)^{\beta},\quad\beta\in(0,1), |  |

where γ\gamma is a stock- and regime-dependent scale factor, and β\beta
typically lies between 0.4 and 0.7 for equities.
This concavity captures the empirically observed “square-root law” of market impact. At the shortest time scales, however, the impact function is often observed to be closer to linear. For example, Cont et al., ([2014](https://arxiv.org/html/2601.22113v2#bib.bib7)) show that short-horizon price changes are linearly related to order flow imbalance, Tóth et al., ([2011](https://arxiv.org/html/2601.22113v2#bib.bib28)) find an additive linear response kernel across traders, and Bucci et al., ([2019](https://arxiv.org/html/2601.22113v2#bib.bib5)) document a crossover regime between linear and square-root impact. In Section [3](https://arxiv.org/html/2601.22113v2#S3 "3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation"), we empirically compare both functional forms at the one-minute horizon, finding that the square-root law provides superior explanatory power (R2R^{2}) in our dataset.

##### Propagator kernel.

As illustrated in Figure [2](https://arxiv.org/html/2601.22113v2#S2.F2 "Figure 2 ‣ Propagator kernel. ‣ 2.1.2 Propagator Model (Transient Impact Model) ‣ 2.1 Optimal Execution Problem Set-up ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation"), the choice of kernel G​(ℓ)G(\ell) determines how quickly past trades lose their influence on current prices. Empirical studies show that impact is neither permanent (constant G​(ℓ)G(\ell)) nor purely instantaneous (delta kernel), but decays gradually over time. Several functional forms have been proposed, including power-law kernels (Bouchaud,, [2010](https://arxiv.org/html/2601.22113v2#bib.bib3)) and stretched exponentials (Mastromatteo et al.,, [2014](https://arxiv.org/html/2601.22113v2#bib.bib16)).

In this work, we adopt the exponential kernel

|  |  |  |
| --- | --- | --- |
|  | G​(ℓ)=G0​e−ℓ/τ,G(\ell)=G\_{0}\,e^{-\ell/\tau}, |  |

where G0G\_{0} is the immediate impact coefficient, ℓ\ell is the time since the last trade and τ\tau is the characteristic decay horizon in minutes. This form balances tractability with fidelity: it ensures that impact is transient, avoids long-memory tails that can destabilise calibration on finite samples, and is consistent with empirical fits of minute-bar data. The exponential kernel also integrates naturally with reinforcement learning by ensuring a well-behaved, Markovian state evolution.

0224466881010121214141616181820202222242426262828303000.50.511lag ℓ\ell (minutes)Impact [bps]Exponential: e−ℓ/τe^{-\ell/\tau}Power law: (ℓ+ℓ0)−γ(\ell+\ell\_{0})^{-\gamma}Instantaneous: δ​(ℓ)\delta(\ell) (schematic)


Figure 2: Illustrative transient impact kernels in basis points. The instantaneous kernel is shown schematically as a unit impulse; exponential and power-law forms capture transient, decaying impact with different memory.

##### Summary.

Combining the exponential kernel with the power-law impact function yields
the full transient impact model:

|  |  |  |
| --- | --- | --- |
|  | It=∑ℓ=1LG0​e−ℓ/τ​γ​(qt−ℓVt−ℓ)β​ϵt−ℓ,I\_{t}=\sum\_{\ell=1}^{L}G\_{0}\,e^{-\ell/\tau}\,\gamma\left(\frac{q\_{t-\ell}}{V\_{t-\ell}}\right)^{\beta}\,\epsilon\_{t-\ell}, |  |

which adjusts fill prices according to:

|  |  |  |
| --- | --- | --- |
|  | ptfill=ptVWAP​(1+side⋅It).p^{\mathrm{fill}}\_{t}=p^{\mathrm{VWAP}}\_{t}\,\bigl(1+\mathrm{side}\cdot I\_{t}\bigr). |  |

This formulation arises naturally from resilience models
(Obizhaeva and Wang,, [2013](https://arxiv.org/html/2601.22113v2#bib.bib19)), where impact decays as I˙​(t)=−1τ​I​(t)+κ​Q˙​(t)\dot{I}(t)=-\tfrac{1}{\tau}I(t)+\kappa\dot{Q}(t).
Gatheral et al., ([2012](https://arxiv.org/html/2601.22113v2#bib.bib10)) showed that admissible (non-manipulable) kernels
must be completely monotone—i.e., mixtures of exponentials—further justifying
this choice. While Bouchaud’s propagator framework (Bouchaud et al.,, [2018](https://arxiv.org/html/2601.22113v2#bib.bib4))
often employs power-law kernels, the exponential form offers a tractable
Markovian approximation that calibrates well at minute-bar horizons.

### 2.2 Reinforcement Learning Models

We investigate several reinforcement learning (RL) approaches as candidates for improving execution performance beyond traditional benchmark methods such as TWAP, VWAP, and POV. Our analysis begins with variations of Proximal Policy Optimisation (PPO) (Schulman et al.,, [2017](https://arxiv.org/html/2601.22113v2#bib.bib24)), a widely adopted and robust policy-gradient algorithm that has become a standard baseline in sequential decision-making. Building on this foundation, we extend our study to a more exploratory direction: MAP-Elites (Mouret and Clune,, [2015](https://arxiv.org/html/2601.22113v2#bib.bib17)), a quality-diversity algorithm designed to promote behavioural diversity while retaining high-performing strategies. To the best of our knowledge, MAP-Elites has not previously been applied to optimal execution, making its evaluation in this setting a novel contribution of our work.

#### 2.2.1 RL Fundamentals

![Refer to caption](x1.png)


Figure 3: Classic RL Flow diagram, adapted from Sutton and Barto, ([2018](https://arxiv.org/html/2601.22113v2#bib.bib26)).

Reinforcement Learning (RL) is a framework for sequential decision-making in which an agent interacts with an environment in order to maximise cumulative reward (Sutton and Barto,, [2018](https://arxiv.org/html/2601.22113v2#bib.bib26)). As shown in Figure [3](https://arxiv.org/html/2601.22113v2#S2.F3 "Figure 3 ‣ 2.2.1 RL Fundamentals ‣ 2.2 Reinforcement Learning Models ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation"), at each discrete time step tt, the environment is described by a *state* st∈𝒮s\_{t}\in\mathcal{S} that captures the relevant features observable by the agent. In the context of execution, this state might include remaining inventory, elapsed time, spreads, volatility, imbalance, recent trade volumes, prices, or other relevant market information.

The agent selects an *action* at∈𝒜a\_{t}\in\mathcal{A}, which in execution corresponds to how much of the parent order to trade in the next step (for example, a fraction of the current market volume or a deviation from a baseline schedule). The environment responds by transitioning to a new state st+1s\_{t+1} and producing a scalar *reward* rt∈ℝr\_{t}\in\mathbb{R}, which evaluates the quality of the action taken. In execution, rewards are typically designed as the negative of slippage, transaction cost, or schedule deviation, so that higher returns correspond to better execution quality.

A full sequence of states, actions, and rewards is called a *trajectory*,

|  |  |  |
| --- | --- | --- |
|  | τ=(s0,a0,r0,s1,a1,r1,…,sH),\tau=(s\_{0},a\_{0},r\_{0},s\_{1},a\_{1},r\_{1},\dots,s\_{H}), |  |

with horizon HH corresponding to the lifetime of an order. In execution, one trajectory corresponds to a complete order being executed from start to finish.

The objective of RL is to maximise the expected *return* GtG\_{t}, defined as the discounted sum of future rewards:

|  |  |  |
| --- | --- | --- |
|  | Gt=∑k=0∞γk​rt+k,G\_{t}=\sum\_{k=0}^{\infty}\gamma^{k}r\_{t+k}, |  |

where the *discount factor* γ∈[0,1]\gamma\in[0,1] determines how much future rewards influence present decisions. In execution, setting γ\gamma close to 1 ensures that the agent considers the long-term cost of completing an order, while smaller values of γ\gamma emphasise immediate trading costs.

The expected return under policy π\pi can be described using a *value function*,

|  |  |  |
| --- | --- | --- |
|  | Vπ​(s)=𝔼​[Gt∣st=s,π],V^{\pi}(s)=\mathbb{E}[G\_{t}\mid s\_{t}=s,\pi], |  |

which measures the expected execution quality from state ss. More generally, the *action-value function* quantifies the return of taking action aa in state ss and then following π\pi thereafter:

|  |  |  |
| --- | --- | --- |
|  | Qπ​(s,a)=𝔼​[Gt∣st=s,at=a,π].Q^{\pi}(s,a)=\mathbb{E}[G\_{t}\mid s\_{t}=s,a\_{t}=a,\pi]. |  |

The *advantage function* refines this by comparing the value of a particular action to the state average:

|  |  |  |
| --- | --- | --- |
|  | Aπ​(s,a)=Qπ​(s,a)−Vπ​(s).A^{\pi}(s,a)=Q^{\pi}(s,a)-V^{\pi}(s). |  |

In execution, the advantage can be interpreted as whether trading faster or slower than usual at a given state improves performance.

A common challenge in estimating advantages is the high variance of Monte Carlo returns. To mitigate this, Schulman et al., ([2016](https://arxiv.org/html/2601.22113v2#bib.bib23)) introduced *Generalised Advantage Estimation (GAE)*, which mixes nn-step temporal-difference residuals with an exponentially decaying weight λ∈[0,1]\lambda\in[0,1]. GAE defines the advantage estimate as:

|  |  |  |
| --- | --- | --- |
|  | A^tGAE​(γ,λ)=∑l=0∞(γ​λ)l​δt+lV,δtV=rt+γ​V​(st+1)−V​(st),\hat{A}\_{t}^{\mathrm{GAE}(\gamma,\lambda)}=\sum\_{l=0}^{\infty}(\gamma\lambda)^{l}\,\delta\_{t+l}^{V},\qquad\delta\_{t}^{V}=r\_{t}+\gamma V(s\_{t+1})-V(s\_{t}), |  |

where δtV\delta\_{t}^{V} is the one-step temporal-difference (TD) error. Lower values of λ\lambda reduce variance by relying more on shorter-horizon TD estimates, while higher values reduce bias by incorporating longer returns. Proximal Policy Optimisation (PPO) (Schulman et al.,, [2017](https://arxiv.org/html/2601.22113v2#bib.bib24)) commonly employs GAE with λ≈0.95\lambda\approx 0.95 to stabilise training, providing a robust trade-off between bias and variance.

PPO belongs to the family of *actor-critic* methods, where two neural networks are trained jointly:

* •

  The actor represents the policy πθ​(a|s)\pi\_{\theta}(a|s), which outputs a distribution over actions given the current state. In execution, this determines how aggressively to trade at each step.
* •

  The critic estimates the value function Vϕ​(s)V\_{\phi}(s), parameterised by ϕ\phi, which predicts the expected return from state ss.

The critic serves as a baseline for advantage estimation, reducing variance in policy-gradient updates. Concretely, the policy gradient is estimated as

|  |  |  |
| --- | --- | --- |
|  | ∇θJ​(θ)≈𝔼t​[∇θlog⁡πθ​(at|st)​A^t],\nabla\_{\theta}J(\theta)\approx\mathbb{E}\_{t}\left[\nabla\_{\theta}\log\pi\_{\theta}(a\_{t}|s\_{t})\,\hat{A}\_{t}\right], |  |

where A^t\hat{A}\_{t} is provided by GAE. The critic’s role is to supply Vπ​(st)V^{\pi}(s\_{t}) in the advantage calculation, thereby reducing variance compared to pure Monte Carlo returns. This actor-critic loop ensures that PPO can adaptively balance exploration of new execution strategies with exploitation of known good policies.

PPO is particularly well-suited for execution problems. Unlike off-policy
methods, e.g., deep Q networks (DQN) and soft actor-critic (SAC), that can reuse historical data, PPO is on-policy,
meaning it learns only from trajectories generated by its current policy.
While this reduces sample efficiency, it provides more stable learning in
non-stationary environments where market conditions shift. The clipped
objective (detailed in
Section [2.4.1](https://arxiv.org/html/2601.22113v2#S2.SS4.SSS1 "2.4.1 Proximal Policy Optimisation models (PPO) ‣ 2.4 Novel RL Approaches to Optimal Execution ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation")) prevents destructively large policy updates that could catastrophically
degrade execution performance. For execution, where a bad policy update could
mean significant losses if deployed, PPO’s conservative update mechanism is
a significant advantage in ensuring stable progress towards an improved policy.

### 2.3 Gymnasium for Executing Optimally (GEO)

#### 2.3.1 Data: Minute Bar Data

Our back-testing environment is calibrated using minute-bar data from approximately 400 US equities sourced from Mana Tech (Mana Tech LLC,, [2025](https://arxiv.org/html/2601.22113v2#bib.bib15)) for the entirety of the year 2022. Each bar contains bid/ask/mid quotes and displayed depth, trade prices, sided and hidden volumes, among other features. For each symbol and trading day, the dataset provides the variables listed in Table [3](https://arxiv.org/html/2601.22113v2#A1.T3 "Table 3 ‣ A.1 Data Details ‣ Appendix A Appendix ‣ Diverse Approaches to Optimal Execution Schedule Generation") (in Appendix [A](https://arxiv.org/html/2601.22113v2#A1 "Appendix A Appendix ‣ Diverse Approaches to Optimal Execution Schedule Generation")).

Data cleaning steps include forward-filling missing quotes (at most one bar), excluding minute intervals with no reported trades when constructing returns, and filtering extreme return outliers. Stocks with more than 7% missing values were removed to avoid instability. Summary statistics of the resulting dataset are shown in Figure [15](https://arxiv.org/html/2601.22113v2#A1.F15 "Figure 15 ‣ A.1 Data Details ‣ Appendix A Appendix ‣ Diverse Approaches to Optimal Execution Schedule Generation") (in Appendix [A](https://arxiv.org/html/2601.22113v2#A1 "Appendix A Appendix ‣ Diverse Approaches to Optimal Execution Schedule Generation")).

#### 2.3.2 Daily Analytics

From the one-minute level data we construct a set of daily statistics to be used by GEO and by the learning models. These include averages of daily trading volume, spreads, order book depth, and trade count, as well as Parkinson, ([1980](https://arxiv.org/html/2601.22113v2#bib.bib20)) high-low volatility estimates, defined as

|  |  |  |
| --- | --- | --- |
|  | σ^d(n)=14​n​ln⁡2​∑i=0n−1[ln⁡(Pd−iH/Pd−iL)]2,\widehat{\sigma}^{(n)}\_{d}=\sqrt{\frac{1}{4n\ln 2}\sum\_{i=0}^{n-1}\left[\ln(P^{H}\_{d-i}/P^{L}\_{d-i})\right]^{2}}, |  |

over 1-, 2-, and 5-day windows, where intraday high-low ranges are used
to provide robust volatility estimates less sensitive to bid-ask bounce than
close-to-close returns. Detailed definitions of these features are provided in Appendix [A](https://arxiv.org/html/2601.22113v2#A1 "Appendix A Appendix ‣ Diverse Approaches to Optimal Execution Schedule Generation"), Table LABEL:tab:daily\_features\_returned.

#### 2.3.3 Environment Design and Gymnasium Integration

![Refer to caption](images/GEO_Diagram2.png)


Figure 4: Schematic overview of the GEO environment architecture, showing the
interaction between agent, environment, and calibrated market impact model.

The *GEO* backtest environment (Figure [4](https://arxiv.org/html/2601.22113v2#S2.F4 "Figure 4 ‣ 2.3.3 Environment Design and Gymnasium Integration ‣ 2.3 Gymnasium for Executing Optimally (GEO) ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation")) is implemented as a custom Gymnasium environment that adheres to the Gymnasium API (Towers et al.,, [2024](https://arxiv.org/html/2601.22113v2#bib.bib27); Ray Team,, [2025](https://arxiv.org/html/2601.22113v2#bib.bib22); Stable-Baselines3 Developers,, [2025](https://arxiv.org/html/2601.22113v2#bib.bib25)), enabling seamless integration with a wide range of RL algorithms. The design follows three principles:

1. (i)

   *realism*, achieved through historical data-driven calibration of impact and volatility;
2. (ii)

   *modularity*, enabling easy swapping of components such as reward functions or impact models; and
3. (iii)

   *compatibility*, ensuring adherence to Gym’s reset() and step() interface.

Prior researchers have used Gymnasium in simulators such as *ABIDES* and *mbt\_gym*, though their focus has largely been on limit order book (LOB) dynamics (Jerome et al.,, [2023](https://arxiv.org/html/2601.22113v2#bib.bib13); Amrouni et al.,, [2022](https://arxiv.org/html/2601.22113v2#bib.bib2); Hafsi and Vittori,, [2024](https://arxiv.org/html/2601.22113v2#bib.bib11)). In contrast, our framework targets execution at the minute-bar horizon with transient market impact.

The core environment extends Gymnasium’s Env class and supports vectorised execution for efficient parallel simulation of multiple orders, utilising multiple core CPU acceleration. Each episode corresponds to the execution of a single parent order over HH time steps, with each step representing one minute of market time.

The RL execution agent begins from a baseline schedule, defined as a target percentage of expected market volume, and modifies this on a minute-by-minute basis. This design ensures the order is always completed by the horizon HH. At each step, the agent chooses an action ata\_{t} that scales the baseline participation rate up or down. Negative values slow execution, while positive values accelerate it, with at=−1a\_{t}=-1 corresponding to no trading in that step.

Action space:

|  |  |  |
| --- | --- | --- |
|  | a∈{−1,−0.75,−0.5,−0.25,0,0.25,0.5,0.75,1}a\in\{-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1\} |  |

This discrete action space simplifies exploration while providing sufficient
granularity for adaptive scheduling. The symmetric range around zero allows
both acceleration (at>0a\_{t}>0) and deceleration (at<0a\_{t}<0) from
the baseline rate, with at=−1a\_{t}=-1 pausing execution for the current step.

Target rate with action:

|  |  |  |
| --- | --- | --- |
|  | ρtaction=ρttarget⋅(1+at),ρttarget=qtrem𝔼​[Vt,H],\rho^{\mathrm{action}}\_{t}=\rho^{\mathrm{target}}\_{t}\cdot(1+a\_{t}),\quad\rho^{\mathrm{target}}\_{t}=\frac{q^{\mathrm{rem}}\_{t}}{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathbb{E}}[V\_{t,H}]}, |  |

where qtrem=Q0−∑i=0tqiq^{\mathrm{rem}}\_{t}=Q\_{0}-\sum\_{i=0}^{t}q\_{i} is the remaining inventory at step tt, and 𝔼​[Vt,H]\mathbb{E}[V\_{t,H}] is the expected remaining market volume over the interval [t,H][t,H]. The executed quantity is then

|  |  |  |
| --- | --- | --- |
|  | qt=ρtaction⋅Vtmarket.q\_{t}=\rho^{\mathrm{action}}\_{t}\cdot V^{\mathrm{market}}\_{t}. |  |

The environment tracks remaining quantity, elapsed time, arrival slippage, VWAP slippage, holding cost, impact-adjusted fill prices and accumulated impact. State transitions are driven jointly by the agent’s actions and exogenous price changes from historical data.
The agent observes a 13-dimensional feature vector 𝐨t∈ℝ13\mathbf{o}\_{t}\in\mathbb{R}^{13} at each timestep, comprising market state, execution progress, impact metrics, and regime context:

|  |  |  |
| --- | --- | --- |
|  | 𝐨t=[ptmid,Vt,H−t,qtrem,ADV%,EHV%,pt−1fill,qt−1,Itimm,Itcum,parrival,σ(1),σ(5)]T\mathbf{o}\_{t}=\begin{bmatrix}p^{\text{mid}}\_{t},&V\_{t},&H-t,&q^{\text{rem}}\_{t},&\text{ADV\%},&\text{EHV\%},\\ p^{\text{fill}}\_{t-1},&q\_{t-1},&I^{\text{imm}}\_{t},&I^{\text{cum}}\_{t},\\ p^{\text{arrival}},&\sigma^{(1)},&\sigma^{(5)}\end{bmatrix}^{T} |  |

where ptmidp^{\text{mid}}\_{t} is the current mid-price, VtV\_{t} is market volume at time tt, H−tH-t is remaining time steps, qtremq^{\text{rem}}\_{t} is remaining inventory, ADV% and EHV% are order size relative to average daily volume and expected horizon volume, pt−1fillp^{\text{fill}}\_{t-1} and qt−1q\_{t-1} capture the most recent trade, ItimmI^{\text{imm}}\_{t} and ItcumI^{\text{cum}}\_{t} are immediate and accumulated impact costs (in basis points), parrivalp^{\text{arrival}} is the order arrival benchmark, and σ(1),σ(5)\sigma^{(1)},\sigma^{(5)} are 1-day and 5-day Parkinson volatility estimates.

#### 2.3.4 Order Generation

Orders are generated using an order generator inside GEO, which samples from historical order flow characteristics to produce a diverse set of parent orders. Each order is parameterised by:

* •

  Symbol and date, drawn from the historical dataset.
* •

  Time horizon, randomly sampled between 1 and 390 minutes (up to a full trading day).
* •

  Order size, expressed as a percentage of expected horizon volume (EHV), sampled from a configurable distribution to simulate varying levels of urgency.
* •

  Side (+1+1 for buy, −1-1 for sell), chosen with equal probability.

This sampling procedure produces a heterogeneous set of parent orders that vary in size, duration, and liquidity environment, thereby exposing the agent to a broad distribution of execution scenarios. The training dataset is drawn from a historical period strictly preceding the test dataset, ensuring that evaluation is performed under market conditions not encountered during training. This split allows a fair out-of-sample assessment of generalisation performance.

In this project, we use nine months of trading data for training and three months for testing, across the universe in the minute bar dataset defined in Section [2.3.1](https://arxiv.org/html/2601.22113v2#S2.SS3.SSS1 "2.3.1 Data: Minute Bar Data ‣ 2.3 Gymnasium for Executing Optimally (GEO) ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation"). An illustration of the resulting order size and horizon distributions is provided in Figure [5](https://arxiv.org/html/2601.22113v2#S2.F5 "Figure 5 ‣ 2.3.4 Order Generation ‣ 2.3 Gymnasium for Executing Optimally (GEO) ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation").

![Refer to caption](images/order_plots.png)


Figure 5: Sample set of generated orders with impact and decay coefficients, stratified by symbol, size, and time horizon.

#### 2.3.5 Execution Simulation

At each step tt, the agent selects an action ata\_{t} that scales the
baseline participation rate to determine trade size qtq\_{t}, which is then
executed at impact-adjusted prices using the transient impact framework
(Section [2.1.2](https://arxiv.org/html/2601.22113v2#S2.SS1.SSS2 "2.1.2 Propagator Model (Transient Impact Model) ‣ 2.1 Optimal Execution Problem Set-up ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation")).

The remaining inventory evolves as

|  |  |  |
| --- | --- | --- |
|  | qtrem=Q0−∑i=0t−1qi,q^{\mathrm{rem}}\_{t}=Q\_{0}-\sum\_{i=0}^{t-1}q\_{i}, |  |

and the executed quantity in step tt is

|  |  |  |
| --- | --- | --- |
|  | qt=(1+at)​qtrem𝔼​[Vt,H]​Vtmarket,q\_{t}=\bigl(1+a\_{t}\bigr)\,\frac{q^{\mathrm{rem}}\_{t}}{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathbb{E}}[V\_{t,H}]}\,V^{\mathrm{market}}\_{t}, |  |

which ensures that the order is fully completed by the horizon HH.

The execution price is then determined using the propagator model. Specifically, fills are taken at the contemporaneous market VWAP shifted by the cumulative transient impact ItI\_{t} from current and past trades:

|  |  |  |
| --- | --- | --- |
|  | ptfill=ptVWAP​(1+side⋅It),p^{\mathrm{fill}}\_{t}=p^{\mathrm{VWAP}}\_{t}\,\bigl(1+\mathrm{side}\cdot I\_{t}\bigr), |  |

where side∈{+1,−1}\mathrm{side}\in\{+1,-1\} indicates buy or sell.

The environment records both the impact-adjusted execution price ptfillp^{\mathrm{fill}}\_{t} and the realised implementation shortfall at each step, enabling post-hoc analysis of execution quality and fair comparison across policies. Impact model parameters (γ,G0,τ)(\gamma,G\_{0},\tau) are pre-calibrated
per stock (Section [3.1](https://arxiv.org/html/2601.22113v2#S3.SS1 "3.1 Transient Impact Model Calibration ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation")) and assigned to orders
based on their symbol, ensuring consistent dynamics across training and evaluation.

#### 2.3.6 Reward Function

The agent’s reward is the negative of a weighted sum of execution costs:

|  |  |  |
| --- | --- | --- |
|  | rt=−(β1​Carrival+β2​CVWAP,spread+β3​Δ+β4​ζ),r\_{t}=-\bigl(\beta\_{1}C\_{\mathrm{arrival}}+\beta\_{2}C\_{\mathrm{VWAP,spread}}+\beta\_{3}\Delta+\beta\_{4}\zeta\bigr), |  |

where β1,…,β4\beta\_{1},\ldots,\beta\_{4} are researcher-defined weights that reflect the relative priority of each objective. In our experiments, β1..4\beta\_{1..4} are weights reflecting objective priorities. We set
β1=β2=β3=1.0\beta\_{1}=\beta\_{2}=\beta\_{3}=1.0 and β4=0.1\beta\_{4}=0.1, emphasizing slippage
minimization (arrival and VWAP) and schedule adherence while applying a smaller
weight to the completion penalty for numerical balance.

Arrival slippage CarrivalC\_{\mathrm{arrival}}

Carrival=side​(∑τ=0tpτfill​|qτ|∑τ=0t|qτ|−p0).C\_{\mathrm{arrival}}=\mathrm{side}\,\Bigl(\frac{\sum\_{\tau=0}^{t}p^{\mathrm{fill}}\_{\tau}\,|q\_{\tau}|}{\sum\_{\tau=0}^{t}|q\_{\tau}|}-p\_{0}\Bigr).
Execution shortfall vs. arrival mid-price p0p\_{0}.

VWAP slippage CVWAPC\_{\mathrm{VWAP}}

CVWAP=side​(∑τ=0t(pτfill)​|qτ|∑τ=0t|qτ|−PVWAP).C\_{\mathrm{VWAP}}=\mathrm{side}\,\Bigl(\frac{\sum\_{\tau=0}^{t}(p^{\mathrm{fill}}\_{\tau})\,|q\_{\tau}|}{\sum\_{\tau=0}^{t}|q\_{\tau}|}-P^{\mathrm{VWAP}}\Bigr).
VWAP slippage allows us to measure execution efficiency.

Schedule Deviation Δ\Delta

Δ=σminute​|ρactual−ρtarget|ρtarget.\Delta=\sigma\_{\mathrm{minute}}\,\frac{\bigl|\rho\_{\mathrm{actual}}-\rho\_{\mathrm{target}}\bigr|}{\rho\_{\mathrm{target}}}.
Volatility-scaled penalty for departing from the target participation rate, where σminute\sigma\_{\mathrm{minute}} is the per-minute volatility estimate, computed
as σdaily/390\sigma\_{\mathrm{daily}}/\sqrt{390} using daily Parkinson volatility.

Completion penalty ζ\zeta

ζ=σminute​qremQ0.\zeta=\sigma\_{\mathrm{minute}}\,\frac{q\_{\mathrm{rem}}}{Q\_{0}}.
Discourages unfinished inventory; proportional to qremq\_{\mathrm{rem}} and market turbulence.

A negative slippage (buying below the benchmark for buys, or selling above it for sells) contributes positively to the reward via the sign in CarrivalC\_{\mathrm{arrival}} and CVWAP,spreadC\_{\mathrm{VWAP,spread}}.

#### 2.3.7 Baseline Strategies

We construct a set of standard baseline strategies to benchmark the experimental agents against. The implementations for TWAP, VWAP, and POV emulate common execution algorithms, providing realistic reference points. A purely random policy is also included as a noise-driven comparator.

TWAP – Time-Weighted

qtTWAP=Q0H.q\_{t}^{\mathrm{TWAP}}=\frac{Q\_{0}}{H}.
Constant shares each minute.

VWAP – Volume-weighted

qtVWAP=Q0⋅V¯t∑τ=0H−1V¯τ.q\_{t}^{\mathrm{VWAP}}=Q\_{0}\cdot\frac{\bar{V}\_{t}}{\sum\_{\tau=0}^{H-1}\bar{V}\_{\tau}}.
Allocate proportionally to historical intraday volume profile V¯t\bar{V}\_{t},
where V¯t\bar{V}\_{t} is the average market volume at minute tt over the past N
trading days.

POV – Percentage of Volume

qtPOV=ρtarget​Vt,ρtarget=Q0∑τ=0H−1V¯τ.q\_{t}^{\mathrm{POV}}=\rho\_{\mathrm{target}}\,V\_{t},\qquad\rho\_{\mathrm{target}}=\frac{Q\_{0}}{\sum\_{\tau=0}^{H-1}\bar{V}\_{\tau}}.
Trade a fixed participation of *realised* market volume VtV\_{t}; ρtarget\rho\_{\mathrm{target}} chosen to complete in expectation over HH based on historical volume V¯​[a,H]\bar{V}[a,H].

Random – Noise baseline

At each minute draw ata\_{t} from the action set and set



qtRAND=(1+at)​qtrem𝔼​[Vt,H]​Vt,qtrem=Q0−∑i=0t−1qi,q\_{t}^{\mathrm{RAND}}=(1+a\_{t})\,\frac{q^{\mathrm{rem}}\_{t}}{\mathbb{E}[V\_{t,H}]}\,V\_{t},\quad q^{\mathrm{rem}}\_{t}=Q\_{0}-\sum\_{i=0}^{t-1}q\_{i},
so completion is still enforced by the target-rate scaffolding.

All baselines are evaluated within the GEO environment using the same calibrated
transient impact model and fill price mechanism as the RL agents, ensuring fair
comparison. Each baseline executes orders according to its deterministic schedule,
with fills adjusted for market impact via Equation ([1](https://arxiv.org/html/2601.22113v2#S2.E1 "In General formulation. ‣ 2.1.2 Propagator Model (Transient Impact Model) ‣ 2.1 Optimal Execution Problem Set-up ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation")).

### 2.4 Novel RL Approaches to Optimal Execution

#### 2.4.1 Proximal Policy Optimisation models (PPO)

PPO belongs to the family of *policy-gradient methods*, which directly optimise a parametrised policy πθ​(a|s)\pi\_{\theta}(a|s) by estimating gradients of the expected return with respect to the parameters θ\theta. Unlike value-based methods such as Q-learning, which learn an action-value function Q​(s,a)Q(s,a) and act greedily via arg⁡maxa⁡Q​(s,a)\arg\max\_{a}Q(s,a), policy-gradient methods adjust πθ\pi\_{\theta} itself to increase the probability of selecting actions that yield higher returns. Formally,

|  |  |  |
| --- | --- | --- |
|  | ∇θJ​(πθ)=𝔼st∼dπθ,at∼πθ​[∇θlog⁡πθ​(at|st)​Qπθ​(st,at)].\nabla\_{\theta}J(\pi\_{\theta})=\mathbb{E}\_{s\_{t}\sim d^{\pi\_{\theta}},a\_{t}\sim\pi\_{\theta}}\left[\nabla\_{\theta}\log\pi\_{\theta}(a\_{t}|s\_{t})\,Q^{\pi\_{\theta}}(s\_{t},a\_{t})\right]. |  |

PPO is an *on-policy* algorithm, meaning it learns exclusively from trajectories generated by its current policy. This stabilises training but requires discarding past data once the policy updates. By contrast, off-policy methods such as Q-learning or SAC update from a behaviour policy μ≠πθ\mu\neq\pi\_{\theta}, reusing past trajectories to improve sample efficiency.

The key innovation of PPO is its *clipped surrogate loss*, which stabilises learning by preventing excessively large policy updates. With generalised advantage estimation (GAE), the PPO objective is

|  |  |  |
| --- | --- | --- |
|  | LCLIP​(θ)=𝔼t​[min⁡(rt​(θ)​A^t,clip⁡(rt​(θ),1−ϵ,1+ϵ)​A^t)],L^{\text{CLIP}}(\theta)=\mathbb{E}\_{t}\left[\min\Big(r\_{t}(\theta)\,\hat{A}\_{t},\operatorname{clip}\big(r\_{t}(\theta),1-\epsilon,1+\epsilon\big)\,\hat{A}\_{t}\Big)\right], |  |

where

|  |  |  |
| --- | --- | --- |
|  | rt​(θ)=πθ​(at|st)πθold​(at|st).r\_{t}(\theta)=\frac{\pi\_{\theta}(a\_{t}|s\_{t})}{\pi\_{\theta\_{\text{old}}}(a\_{t}|s\_{t})}. |  |

Here, A^t\hat{A}\_{t} denotes the estimated advantage of action ata\_{t} at state sts\_{t}, and ϵ\epsilon (typically 0.10.1-0.30.3) controls the clipping range. The clipping prevents rt​(θ)r\_{t}(\theta) from deviating too far from 11, thereby limiting the size of policy updates. PPO also incorporates a separate value-function loss and an entropy bonus to balance exploitation and exploration.

In addition to the clipped policy objective, PPO optimises a state-value baseline Vϕ​(st)V\_{\phi}(s\_{t}) using a squared-error loss:

|  |  |  |
| --- | --- | --- |
|  | LVF​(ϕ)=𝔼t​[(Vϕ​(st)−R^t)2],L^{\mathrm{VF}}(\phi)=\mathbb{E}\_{t}\Big[\big(V\_{\phi}(s\_{t})-\hat{R}\_{t}\big)^{2}\Big], |  |

where R^t\hat{R}\_{t} is the empirical return or bootstrapped target. This helps reduce variance in policy-gradient updates by ensuring the critic approximates the long-term execution cost of continuing from state sts\_{t}.

To avoid premature convergence to deterministic (and possibly suboptimal) policies, PPO adds an entropy regularisation term:

|  |  |  |
| --- | --- | --- |
|  | Lentropy(θ)=𝔼t[ℋ(πθ(⋅|st))],L^{\mathrm{entropy}}(\theta)=\mathbb{E}\_{t}\big[\mathcal{H}(\pi\_{\theta}(\cdot|s\_{t}))\big], |  |

where ℋ\mathcal{H} is the Shannon entropy. This encourages exploration by rewarding policies that maintain uncertainty over possible actions.

Putting it all together, the PPO loss combines the clipped surrogate policy objective with a value-function regression term and an entropy bonus:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒPPO(θ,ϕ)=𝔼t[\displaystyle\mathcal{L}\_{\mathrm{PPO}}(\theta,\phi)=\mathbb{E}\_{t}\Big[ | min⁡(rt​(θ)​A^t,clip​(rt​(θ),1−ϵ,1+ϵ)​A^t)⏟Lπ\displaystyle\underbrace{\min\!\Big(r\_{t}(\theta)\,\hat{A}\_{t},\mathrm{clip}\!\big(r\_{t}(\theta),1-\epsilon,1+\epsilon\big)\,\hat{A}\_{t}\Big)}\_{L^{\pi}} |  | (2) |
|  |  | −cv​(Vϕ​(st)−R^t)2⏟LV+ce​ℋ(πθ(⋅∣st))⏟LH\displaystyle-c\_{v}\,\underbrace{\big(V\_{\phi}(s\_{t})-\hat{R}\_{t}\big)^{2}}\_{L^{V}}+c\_{e}\,\underbrace{\mathcal{H}\!\big(\pi\_{\theta}(\cdot\mid s\_{t})\big)}\_{L^{H}} |  |
|  |  | −cKLKL(πθold(⋅∣st)∥πθ(⋅∣st))⏟LK​L],\displaystyle-c\_{\mathrm{KL}}\,\underbrace{\mathrm{KL}\!\Big(\pi\_{\theta\_{\mathrm{old}}}(\cdot\mid s\_{t})\|\pi\_{\theta}(\cdot\mid s\_{t})\Big)}\_{L^{KL}}\Big], |  |

We implement PPO agents with two distinct feature extractor architectures. The first is an multilayer perceptron (MLP) extractor, which normalises the flattened observation vector and passes it through two fully connected layers with ReLU activations. This design is lightweight and fast, making it well-suited to compact, tabular state representations. The second applies one-dimensional
convolutions across the feature dimension with three blocks (64, 64, 128 channels),
SiLU activations, and group normalization, providing additional representational
capacity at the cost of increased computation.

Observation Preprocessing: Raw observations are normalised using
running mean and standard deviation estimates maintained across vectorised
environments (Stable-Baselines3 VecNormalize wrapper), ensuring numerical
stability across assets and regimes.

Hyperparameters follow standard PPO best practices (Schulman et al.,, [2017](https://arxiv.org/html/2601.22113v2#bib.bib24)) with
minor adjustments for the execution domain.

Common PPO Settings

Architecture: Shared feature extractor (256-dim); actor MLP [256, 256, 128]; critic MLP [256, 256, 128]; tanh activation.
Optimiser: PPO with clipped surrogate loss LπL^{\pi}, value loss LVL^{V}, entropy bonus LHL^{H}, and KL penalty LK​LL^{KL} (Eq. [2](https://arxiv.org/html/2601.22113v2#S2.E2 "In 2.4.1 Proximal Policy Optimisation models (PPO) ‣ 2.4 Novel RL Approaches to Optimal Execution ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation")).
Key Hyperparameters:

•

Rollout: nsteps=2048n\_{\mathrm{steps}}=2048 per environment, discount γ=0.999\gamma=0.999
•

Batch size: Auto-scaled by rollout size ∈{2048,4096,8192}\in\{2048,4096,8192\}
•

Training: 3 epochs, clip range ϵ≈0.18\epsilon\approx 0.18 (linear decay)
•

Regularization: target KL = 0.02, entropy coefficient = 0.006
•

Value loss coefficient = 0.55, max gradient norm = 0.5
Learning Rate: Linear decay from 3×10−43\times 10^{-4} to 0.
GAE: λ=0.95\lambda=0.95 for advantage estimation.

#### 2.4.2 MAP-Elites: Quality-Diversity Optimisation

Most reinforcement learning algorithms optimise for a single performance objective, aiming to find the policy πθ\pi\_{\theta} that maximises expected return. While this produces a single “best” solution under the training reward, it provides little insight into the diversity of alternative strategies or their robustness under changing market conditions. The *MAP-Elites* algorithm, introduced by Mouret and Clune, ([2015](https://arxiv.org/html/2601.22113v2#bib.bib17)), belongs to the class of *quality-diversity* (QD) methods. Rather than converging on a single optimum, MAP-Elites searches for a collection of high-performing yet behaviourally distinct solutions, yielding a repertoire of policies that together “illuminate” the range of possible strategies.

MAP-Elites Algorithm (overview)

Inputs: behaviour-descriptor mapping b​(π)∈ℝdb(\pi)\in\mathbb{R}^{d}, archive grid 𝒢{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathcal{G}} partitioning descriptor space, quality function Q​(π)Q(\pi), variation operator Var​(⋅)\mathrm{Var}(\cdot).

1.

Initialisation. Generate candidate policies {π(i)}\{\pi^{(i)}\}. For each, evaluate Q​(π(i))Q(\pi^{(i)}) and compute descriptor z(i)=b​(π(i))z^{(i)}=b(\pi^{(i)}).
2.

Archive update. Map z(i)z^{(i)} to grid cell cc. If 𝒢​[c]{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathcal{G}}[c] is empty, insert π(i)\pi^{(i)}; if occupied, replace only if Q​(π(i))Q(\pi^{(i)}) exceeds the incumbent via the quality function.
3.

Variation. Sample elites from 𝒢{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathcal{G}} and generate offspring by perturbing their representation.
4.

Iteration. Evaluate offspring, compute descriptors, and update 𝒢{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathcal{G}}. Iterate until evaluation budget is exhausted.
Output: repertoire 𝒢{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\mathcal{G}} of elites {πc⋆}\{\pi^{\star}\_{c}\}, one per descriptor cell, each maximising Q​(π)Q(\pi) locally.

The quality function Q​(π)Q(\pi) is the negative mean total execution cost averaged
over evaluation episodes, where lower cost (better execution) yields higher quality.
Each policy is evaluated on orders matching its phenotype to ensure fair niche-specific
comparison.

When applying variation to neural networks, we perturb the weights θ\theta that define the extractors allowing for variability. Offspring are generated by applying Gaussian
noise (𝒩​(0,σ2)\mathcal{N}(0,\sigma^{2})) to parent policy parameters. This preserves learned behaviors while introducing
local variation.

Each cell in the archive corresponds to a region of descriptor space. MAP-Elites guarantees that only the best-known policy for each behavioural niche is retained. Over many iterations, the archive becomes populated with a structured set of strategies that are both high quality and diverse.

In our implementation, descriptors are designed to capture the fundamental market dimensions of *liquidity* and *volatility*. Both are normalised by their empirical quantiles across the universe, mapping values to the unit interval [0,1][0,1] in a rank-preserving way:

* •

  Liquidity. Quantile-normalised average daily volume (ADV) of symbol SS:

  |  |  |  |
  | --- | --- | --- |
  |  | bliq​(S)=1N​∑j=1N𝟏​{ADV​(Sj)≤ADV​(S)},b^{\mathrm{liq}}(S)=\frac{1}{N}\sum\_{j=1}^{N}\mathbf{1}\{\mathrm{ADV}(S\_{j})\leq\mathrm{ADV}(S)\}, |  |

  where NN is the number of symbols in the universe.
* •

  Volatility. Quantile-normalised one-day Parkinson estimator:

  |  |  |  |
  | --- | --- | --- |
  |  | bvol​(S)=1N​∑j=1N𝟏​{σ^(1)​(Sj)≤σ^(1)​(S)},b^{\mathrm{vol}}(S)=\frac{1}{N}\sum\_{j=1}^{N}\mathbf{1}\{\widehat{\sigma}^{(1)}(S\_{j})\leq\widehat{\sigma}^{(1)}(S)\}, |  |

  where σ^(1)​(S)=14​ln⁡2​[ln⁡(PHPL)]2\widehat{\sigma}^{(1)}(S)=\sqrt{\tfrac{1}{4\ln 2}\left[\ln\!\left(\tfrac{P^{H}}{P^{L}}\right)\right]^{2}}.

Thus, each policy πθ\pi\_{\theta} is mapped into the two-dimensional descriptor space

|  |  |  |
| --- | --- | --- |
|  | b​(πθ)=(bliq​(S),bvol​(S))∈[0,1]2,b(\pi\_{\theta})=\big(b^{\mathrm{liq}}(S),b^{\mathrm{vol}}(S)\big)\in[0,1]^{2}, |  |

with archive cells representing liquidity-volatility niches.

VolatilityLiquidityQ=0.58Q=0.53Q=0.61Q=0.67Q=0.50Q=0.70
EliteEmpty cell


Figure 6: MAP-Elites archive across liquidity and volatility descriptors. Each filled cell stores the highest-quality policy (elite) discovered in that region.

MAP-Elites offers potential advantages: it may enforce exploration of behaviourally
distinct strategies, produce an interpretable map of “what works where,” provide
robustness through diverse repertoires, and remain agnostic to policy representation.
In this work, we apply MAP-Elites to a PPO-based CNN policy using liquidity-volatility
descriptors to structure the archive. However, as we show in Section [3](https://arxiv.org/html/2601.22113v2#S3 "3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation"),
the practical benefits depend critically on descriptor choice, fitness function
design, and computational budget.

## 3 Results

### 3.1 Transient Impact Model Calibration

We calibrate the propagator model parameters (G0,τ)(G\_{0},\tau) by regressing returns rtr\_{t} onto lagged signed volumes ϵt−ℓ​f​(vt−ℓ)\epsilon\_{t-\ell}f(v\_{t-\ell}) across multiple lags ℓ=1,…,L\ell=1,\dots,L. Parameters are chosen to maximise out-of-sample R2R^{2} across rolling windows of one-minute level data for 400+ S&P 500 stocks during 2022 (excluding stocks with insufficient or missing
one-minute level data).

Two functional forms for f​(v)f(v) were compared: linear and square-root. Consistent with empirical microstructure studies, the square-root form achieved higher mean R2R^{2} across symbols and was adopted as the baseline:

|  |  |  |
| --- | --- | --- |
|  | f​(vt,qt)=γ​|qt|vt,f(v\_{t},q\_{t})=\gamma\sqrt{\tfrac{|q\_{t}|}{v\_{t}}}, |  |

where qtq\_{t} is the signed traded quantity at time tt, and vtv\_{t} is the market volume for the period tt and γ\gamma is the impact coefficient.

The decay kernel G​(ℓ)G(\ell) captures temporal persistence of impact:

|  |  |  |
| --- | --- | --- |
|  | G​(ℓ)=G0​e−ℓ/τ,G(\ell)=G\_{0}\,e^{-\ell/\tau}, |  |

where G0G\_{0} is the immediate impact coefficient, ℓ\ell is the lag since the trade, and τ\tau the characteristic decay horizon.

Calibration is performed via constrained non-linear least squares with economically interpretable bounds:

|  |  |  |
| --- | --- | --- |
|  | G0≥0,τ∈[0.5,180].G\_{0}\geq 0,\qquad\tau\in[0.5,180]. |  |

The necessity of these contraints is demonstrated in Figure [7](https://arxiv.org/html/2601.22113v2#S3.F7 "Figure 7 ‣ 3.1 Transient Impact Model Calibration ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation").

![Refer to caption](images/tau_samples.png)


Figure 7: Constraint necessity: without bounds, τ\tau can turn negative due to noise (Eq. [1](https://arxiv.org/html/2601.22113v2#S2.E1 "In General formulation. ‣ 2.1.2 Propagator Model (Transient Impact Model) ‣ 2.1 Optimal Execution Problem Set-up ‣ 2 Methods ‣ Diverse Approaches to Optimal Execution Schedule Generation")), implying explosion rather than decay.

Figure [8](https://arxiv.org/html/2601.22113v2#S3.F8 "Figure 8 ‣ 3.1 Transient Impact Model Calibration ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation") presents a lagged regression study comparing R2R^{2} of linear and square-root forms at maximum lags LL of 5, 10, and 20 minutes. The square-root function dominates overall, especially for liquid names where concavity captures diminishing marginal impact (Figure [9](https://arxiv.org/html/2601.22113v2#S3.F9 "Figure 9 ‣ 3.1 Transient Impact Model Calibration ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation")).

![Refer to caption](images/lag_study.png)


Figure 8: R2R^{2} comparison of linear vs. square-root instantaneous impact across lags ℓ=1,…,L\ell=1,\dots,L for L∈{5,10,20,30}L\in\{5,10,20,30\}. Square-root dominates in liquid names and shorter horizons.

After cross-validation, we store the best (ℓ,τ,γ)(\ell,\tau,\gamma) and average R¯2\bar{R}^{2} for reuse, retaining only symbols with R¯2>0.02\bar{R}^{2}>0.02. This threshold leaves about two-thirds of the universe available for training and testing. Stocks below this threshold are excluded from the training, validation and test sets.

![Refer to caption](images/linear_vs_sqrt.png)


Figure 9: Aggregate R2R^{2} outcomes: the square-root specification outperforms linear on average, supporting its choice as the baseline model.

### 3.2 RL Performance Results

#### 3.2.1 Evaluation of RL models

For evaluation, we adopt a strict train-test separation based on non-overlapping calendar periods. The training set consists of orders generated between January 1, 2022 and September 30, 2022, while the evaluation set spans October 1 to December 31, 2022.

Training is performed within the GEO environment, which integrates Gymnasium for vectorised simulation. For each experiment, we generate a large set of synthetic parent orders (5,000-25,000 per run) sampled across the universe described. Orders are balanced between buys and sells and cover a range of sizes and horizons. The exact same training and evaluation orders are shared across all policies to guarantee a fair comparison.

We benchmark PPO with multi-layer perceptron (MLP) and convolutional (CNN) feature extractors, MAP-Elites, and baseline strategies (TWAP, VWAP, POV, and Random). To mitigate the influence of outliers, we exclude pathological orders and winsorise evaluation metrics at the 1st and 99th percentiles before aggregation.

#### 3.2.2 PPO Results and Findings

Table [1](https://arxiv.org/html/2601.22113v2#S3.T1 "Table 1 ‣ 3.2.2 PPO Results and Findings ‣ 3.2 RL Performance Results ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation") summarises performance for the two PPO architectures compared to baseline strategies. Metrics are expressed in basis points (bps), with standard errors in parentheses.

| Agent | Count | Notional (Bln) | Arrival Slippage | Duration % | Return | Total Cost | Action % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ppo\_mlp | 4900 | 21.32 | 3.78 (0.93) | 99.2 | -5.19 (1.41) | 178.26 (1.77) | 18.25 (0.06) |
| vwap | 4900 | 21.66 | 5.23 (1.01) | 99.2 | -5.60 (1.43) | 476.11 (6.09) | 12.51 (0.08) |
| random | 4900 | 21.31 | 3.77 (0.96) | 99.2 | -3.46 (1.41) | 217.58 (2.23) | -0.02 (0.06) |
| pov | 4900 | 21.30 | 4.07 (0.97) | 99.3 | -3.87 (1.41) | 211.71 (2.21) | 0.00 (0.00) |
| twap | 4900 | 20.18 | 7.01 (0.90) | 98.8 | 1.70 (1.40) | 302.89 (3.25) | 75.59 (0.05) |
| ppo\_cnn | 4900 | 21.41 | 2.13 (0.92) | 99.2 | -5.68 (1.41) | 178.70 (1.78) | 19.00 (0.06) |

Table 1: Execution summary for PPO and baseline strategies. Arrival slippage, Return, and Total Cost in basis points (bps); Standard errors in parentheses; Duration % is the average portion of of HH before completion; Action is the mean ata\_{t} over all parents; Return: intra-order price drift;

The PPO-CNN model achieves the lowest arrival slippage of all strategies (2.13 bps), a statistically significant improvement where p<0.05p<0.05, relative to VWAP, TWAP, and POV. PPO-MLP delivers performance comparable to the random baseline on slippage but still far outperforms benchmarks on cost. Both PPO agents reduce total cost dramatically, halving costs relative to TWAP (303 bps) and cutting more than 60% compared to VWAP (476 bps).

![Refer to caption](images/ppo_trajectories.png)


Figure 10: Aggregated mean action % ata\_{t} across order horizons, conditioned on price drift relative to order side. PPO agents exhibit front-loading consistent with Almgren-Chriss scheduling.

Both PPO agents adopt a front-loaded pattern consistent with Almgren-Chriss intuition, mitigating holding costs by executing earlier. The CNN variant moderates this front-loading when returns are adverse, suggesting that the temporal structure enables a more nuanced response to price drift (Figures [10](https://arxiv.org/html/2601.22113v2#S3.F10 "Figure 10 ‣ 3.2.2 PPO Results and Findings ‣ 3.2 RL Performance Results ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation") and [11](https://arxiv.org/html/2601.22113v2#S3.F11 "Figure 11 ‣ 3.2.2 PPO Results and Findings ‣ 3.2 RL Performance Results ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation")).

![Refer to caption](images/rl_costs.png)


Figure 11: Decomposition of costs across strategies. PPO agents internalise holding cost, which drives front-loading behaviour.

### 3.3 MAP-Elites Results and Findings

#### 3.3.1 Exploratory Application of MAP-Elites

We conducted a preliminary investigation of MAP-Elites for generating regime-specialist
policies. While quality-diversity approaches have shown promise in robotics
(Mouret and Clune,, [2015](https://arxiv.org/html/2601.22113v2#bib.bib17)), their application to financial execution remains
largely unexplored. We implemented MAP-Elites over volatility (normalised Parkinson) and liquidity (normalised ADV) behavioural descriptors
with a 3×33\times 3 grid, seeding policies from a baseline PPO-CNN model and
evolving them via Gaussian parameter perturbations (σ=0.01\sigma=0.01). Initial
experiments with modest configurations (30-100 iterations) showed promising
in-sample improvements but failed to generalise. We therefore scaled to 500
iterations with 256 children per generation, evaluating 128,000 candidate policies
over 5.5 hours on Apple M4 Max 64GB 16-core CPU.

Table [2](https://arxiv.org/html/2601.22113v2#S3.T2 "Table 2 ‣ 3.3.1 Exploratory Application of MAP-Elites ‣ 3.3 MAP-Elites Results and Findings ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation") presents phenotype-specific performance: each
specialist was evaluated exclusively on test orders matching its liquidity-volatility
cell.
Three cells achieved 8-10% improvements over baseline PPO within their
training niches, while others showed degradation, particularly in
low-liquidity regimes. These findings suggest potential for quality-diversity
methods but indicate that effective deployment requires careful consideration
of regime boundaries, training data density per cell, and selective
application strategies.

![Refer to caption](images/map_elites_not_quite.png)


Figure 12: MAP-Elites archive evolution over 100 iterations. Z-axis indicates fitness (negative total cost). Red plane shows baseline PPO-CNN fitness. Training set (left) achieves improvements across all cells, whereas test set (right) shows mixed generalization with failures in low-liquidity regimes.

![Refer to caption](map_elites_yolo.png)


Figure 13: MAP-Elites archive evolution. 500 iteration run. Z-axis indicates fitness (negative total cost). Red plane shows baseline PPO-CNN fitness. Training set (left) achieves improvements across all cells, whereas test set (right) shows improved results vs. the 100 iteration run.

The archive reveals striking heterogeneity in generalisation. Three cells achieved 8-10% improvements over baseline, with the high-volatility/medium-liquidity cell performing best at +10.3%. Conversely, the high-volatility/low-liquidity cell degraded catastrophically (-30.2%), suggesting overfitting in illiquid regimes. While the overall cell average showed -2.4% degradation, individual specialists demonstrate that regime-specific policies can outperform universal approaches when properly matched to market conditions.

These results motivate development of ensemble routing strategies that selectively
deploy specialists only in regimes where they demonstrate robust out-of-sample
improvements. Such meta-policies are left for future work.

Table 2: MAP-Elites specialist fitness (total cost) performance by market regime

| Volatility | Liquidity | Fitness | vs CNN Policy |
| --- | --- | --- | --- |
| Low | Low | -0.01672 | -3.3% |
| Low | Medium | -0.01637 | -1.2% |
| Low | High | -0.01574 | +2.7% |
| Medium | Low | -0.01834 | -13.3% |
| Medium | Medium | -0.01487 | +8.1% |
| Medium | High | -0.01467 | +9.3% |
| High | Low | -0.02107 | -30.2% |
| High | Medium | -0.01451 | +10.3% |
| High | High | -0.01689 | -4.4% |
| Overall |  | -0.01657 | -2.4% |

## 4 Discussion

### 4.1 GEO Environment and RL Performance

We introduced GEO, a Gymnasium-compatible environment for optimal execution that
integrates calibrated transient impact models with vectorized simulation. GEO’s
design enables direct transfer between backtesting and live deployment, reducing
the sim-to-real gap inherent in custom execution simulators.

Within GEO, PPO-CNN achieved 2.13 bps arrival slippage, outperforming VWAP
(5.23 bps) and TWAP (7.01 bps) by 59% and 70% respectively. Both PPO agents
reduced total costs to 178 bps, roughly half TWAP’s 303 bps, primarily through
front-loaded schedules that internalize holding costs.
Figure [14](https://arxiv.org/html/2601.22113v2#S4.F14 "Figure 14 ‣ 4.1 GEO Environment and RL Performance ‣ 4 Discussion ‣ Diverse Approaches to Optimal Execution Schedule Generation") shows the “anatomy” of a single PPO-CNN order, illustrating how the propagator affects fill prices, how inventory is managed, and how costs accumulate. This integrated view demonstrates how the RL agent perceives state, chooses actions, and experiences costs under the transient impact model.

![Refer to caption](images/anatomy_of_an_order2.png)


Figure 14: Anatomy of a PPO-CNN RL order showing propagator-driven fill prices, remaining inventory, policy actions, immediate impact, and cost decomposition.

The CNN’s advantage over MLP (3.78 bps) despite processing identical 13-dimensional
observations demonstrates that architectural improvements yield measurable gains.
The convolutional layers enable learning joint patterns between correlated features—price,
volume, and inventory states—where the MLP treats each independently. Figure [10](https://arxiv.org/html/2601.22113v2#S3.F10 "Figure 10 ‣ 3.2.2 PPO Results and Findings ‣ 3.2 RL Performance Results ‣ 3 Results ‣ Diverse Approaches to Optimal Execution Schedule Generation")
shows the CNN moderating front-loading during adverse price drift, suggesting
context-dependent adaptation beyond the MLP’s static aggressiveness.

These improvements occur within a simulator calibrating exponential impact decay
on one-minute level data with R2≈R^{2}\approx 0.02-0.10. While this explained variance appears modest,
it reflects realistic microstructure signal-to-noise ratios. The results represent
performance under calibrated impact dynamics, not predictions of live execution.

### 4.2 Quality-Diversity: Current Results and Future Potential

MAP-Elites revealed substantial regime heterogeneity. Three cells achieved 8-10%
improvements, with high-volatility/medium-liquidity reaching +10.3%. However,
high-volatility/low-liquidity degraded -30.2%, and the overall ensemble averaged
-2.4% below baseline.

The pattern is clear: specialists succeed in data-rich regimes with strong signal
(medium liquidity provides training orders, high volatility amplifies impact
patterns) but catastrophically overfit in sparse cells. Our implementation used
simple Gaussian parameter mutations over 500 iterations—a conservative approach
that prioritizes interpretability over computational efficiency.

Recent advances suggest substantial room for improvement. Parallelized quality-diversity
(Lim et al.,, [2023](https://arxiv.org/html/2601.22113v2#bib.bib14)) could reduce the 5.5-hour runtime by orders of magnitude.
Specialized mutation operators for neural networks (Faldor et al.,, [2025](https://arxiv.org/html/2601.22113v2#bib.bib8))
may improve exploration efficiency beyond naive Gaussian noise. Methods designed
for stochastic objectives (Flageat et al.,, [2025](https://arxiv.org/html/2601.22113v2#bib.bib9)) could better handle the
inherent noisiness of financial data, where fitness evaluation on small order
samples introduces high variance.

Effective deployment requires validation-based selection—use only specialists
demonstrating robust out-of-sample gains—and intelligent routing that falls back
to the baseline in low-confidence regimes. The 3×3 grid may be too coarse; finer
phenotype partitions or continuous descriptor spaces warrant investigation. With
these refinements, quality-diversity methods could provide interpretable performance
maps across market regimes while maintaining robustness.

### 4.3 Practical Implications

RL-based execution appears viable for institutional-scale orders where multi-basis-point
improvements justify development costs. The CNN architecture provides a strong
baseline without requiring complex temporal models or extensive feature engineering.
Quality-diversity methods show promise for discovering regime specialists but
require substantial compute and careful validation before deployment.

Key limitations remain: our impact model makes stationarity assumptions, calibration
quality varies across stocks, and all results derive from simulation. Live
validation would address questions of latency, partial fills, and strategic
interaction with other market participants. Nevertheless, these results demonstrate
that RL execution has progressed from academic curiosity toward practical
consideration for well-resourced trading operations.

## Appendix A Appendix

### A.1 Data Details

Table 3: Minute bar dataset: Raw and derived data fields by symbol and trading day.

| Field | Symbol | Type | Description / Formula |
| --- | --- | --- | --- |
| time | tt | Raw | Minute bin within the continuous trading session. |
| trade\_count | ν\nu | Raw | Number of reported trades in the minute. |
| trade\_volume | VtV\_{t} | Raw | Total number of shares traded in the minute. |
| hid\_vol | VthiddenV^{\mathrm{hidden}}\_{t} | Raw | Reported hidden shares traded in the minute. |
| unsided\_vol | VtunsidedV^{\mathrm{unsided}}\_{t} | Raw | Shares traded with unknown aggressor side. |
| sell\_vol | VtsellV^{\mathrm{sell}}\_{t} | Raw | Shares traded on the sell side (aggressive seller). |
| buy\_vol | VtbuyV^{\mathrm{buy}}\_{t} | Raw | Shares traded on the buy side (aggressive buyer). |
| bid\_price | ptbidp^{\mathrm{bid}}\_{t} | Raw | Best bid quote price at the end of the minute. |
| ask\_price | ptaskp^{\mathrm{ask}}\_{t} | Raw | Best ask quote price at the end of the minute. |
| mid\_price | mtm\_{t} | Derived | Mid-quote price: mt=ptbid+ptask2m\_{t}=\frac{p^{\mathrm{bid}}\_{t}+p^{\mathrm{ask}}\_{t}}{2}. |
| bid\_size | δbid\delta\_{\mathrm{bid}} | Raw | Displayed bid size (shares) at the end of the minute. |
| ask\_size | δask\delta\_{\mathrm{ask}} | Raw | Displayed ask size (shares) at the end of the minute. |
| trade\_first | PfirstP\_{\mathrm{first}} | Raw | First trade price in the minute (removed as predominantly missing). |
| trade\_last | PlastP\_{\mathrm{last}} | Raw | Last trade price in the minute. |
| trade\_high | PhighP\_{\mathrm{high}} | Raw | Highest trade price in the minute. |
| trade\_low | PlowP\_{\mathrm{low}} | Raw | Lowest trade price in the minute. |
| vwap | PvwapP\_{\mathrm{vwap}} | Raw | Volume-weighted average trade price in the minute. |
| trade\_imbalance | ϵt\epsilon\_{t} | Derived | Signed volume imbalance: ϵt=Vtbuy−VtsellVt\epsilon\_{t}=\frac{V^{\mathrm{buy}}\_{t}-V^{\mathrm{sell}}\_{t}}{V\_{t}}. |
| volatility | σ\sigma | Derived | Realised volatility from a rolling window (default: 21-min rolling standard deviation of mid-price returns). |

![Refer to caption](images/cleaned_data.png)


Figure 15: Summary statistics of cleaned data.




Table 4: Daily dataset fields returned by the aggregation pipeline (stored output).

| Field | Symbol | Description / Formula |
| --- | --- | --- |
| symbol | SS | Ticker identifier. |
| date | dd | Trading day (YYYYMMDD). |
| adv\_21 | ADV21,d\mathrm{ADV}\_{21,d} | 21-day rolling average daily volume:  ADV21,d=121​∑i=020Vd−i\mathrm{ADV}\_{21,d}=\tfrac{1}{21}\sum\_{i=0}^{20}V\_{d-i} |
| avg\_trade\_count\_21 | ν¯21,d\overline{\nu}\_{21,d} | 21-day rolling average of daily trade counts:  ν¯21,d=121​∑i=020νd−i\overline{\nu}\_{21,d}=\tfrac{1}{21}\sum\_{i=0}^{20}\nu\_{d-i} |
| avg\_spread\_21 | s¯21,d\overline{s}\_{21,d} | 21-day rolling average of the day-level spread metric (units consistent with input spread). |
| avg\_depth\_21 | δ¯21,d\overline{\delta}\_{21,d} | 21-day rolling average of daily depth, where  δd=bid\_sized+ask\_sized2,δ¯21,d=121​∑i=020δd−i\delta\_{d}=\tfrac{\text{bid\\_size}\_{d}+\text{ask\\_size}\_{d}}{2},\quad\overline{\delta}\_{21,d}=\tfrac{1}{21}\sum\_{i=0}^{20}\delta\_{d-i} |
| vwap | PdVWAP∗P^{\mathrm{VWAP}}\_{d}{}^{\ast} | Daily VWAP with fallback: if VWAP is missing, set PdVWAP←∗PdlastP^{\mathrm{VWAP}}\_{d}{}^{\ast}\leftarrow P^{\mathrm{last}}\_{d} (last trade price). |
| daily\_volatility | σ^d(1)\widehat{\sigma}^{(1)}\_{d} | Parkinson volatility (window w=1w{=}1 day), clipped to [10−4,2.0][10^{-4},2.0]:  σ^d(w)=14​w​ln⁡2​∑i=0w−1[ln⁡(Pd−iHPd−iL)]2\widehat{\sigma}^{(w)}\_{d}=\sqrt{\tfrac{1}{4w\ln 2}\sum\_{i=0}^{w-1}\left[\ln\!\left(\tfrac{P^{H}\_{d-i}}{P^{L}\_{d-i}}\right)\right]^{2}} |
| daily\_vol\_lag1 | σ^d(2)\widehat{\sigma}^{(2)}\_{d} | Parkinson volatility (window w=2w{=}2 days), clipped to [10−4,2.0][10^{-4},2.0] (same formula as above with w=2w=2). |
| daily\_vol\_5d | σ^d(5)\widehat{\sigma}^{(5)}\_{d} | Parkinson volatility (window w=5w{=}5 days), clipped to [10−4,2.0][10^{-4},2.0] (same formula as above with w=5w=5). |
| trade\_high | PdHP^{H}\_{d} | Highest trade price of day dd. |
| trade\_low | PdLP^{L}\_{d} | Lowest trade price of day dd. |

### A.2 Full list of performance Metrics

Table 5: Evaluation metrics used to assess execution policy performance.

| Metric | Mathematical Definition |
| --- | --- |
| Arrival price slippage | Carrival=104⋅side​(∑t=0H−1ptfill​qtQ0−p0)/p0C\_{\mathrm{arrival}}=10^{4}\cdot\mathrm{side}\left(\frac{\sum\_{t=0}^{H-1}p^{\mathrm{fill}}\_{t}\,q\_{t}}{Q\_{0}}-p\_{0}\right)\Big/p\_{0} |
| Implementation shortfall vs. arrival mid-price p0p\_{0}, in basis points. | |
| Market VWAP vs. Arrival | CmktVWAP=104⋅(∑t=0H−1ptmkt​Vt∑t=0H−1Vt−p0)/p0C\_{\mathrm{mktVWAP}}=10^{4}\cdot\left(\frac{\sum\_{t=0}^{H-1}p^{\mathrm{mkt}}\_{t}\,V\_{t}}{\sum\_{t=0}^{H-1}V\_{t}}-p\_{0}\right)\Big/p\_{0} |
| Reference measure of how the market VWAP itself moved relative to arrival, isolating market drift. | |
| VWAP slippage | CVWAP=side​(∑t=0H−1(ptfill)​qtQ0−PVWAP)C\_{\mathrm{VWAP}}=\mathrm{side}\left(\frac{\sum\_{t=0}^{H-1}(p^{\mathrm{fill}}\_{t})\,q\_{t}}{Q\_{0}}-P^{\mathrm{VWAP}}\right) |
| Performance relative to the VWAP benchmark | |
| Completion rate | ∑t=0H−1qtQ0\frac{\sum\_{t=0}^{H-1}q\_{t}}{Q\_{0}} |
| Proportion of shares executed by horizon HH; target is 1 (100%). | |
| Horizon usage | tlast​\_​tradeH\frac{t\_{\mathrm{last\\_trade}}}{H} |
| Fraction of horizon consumed before order completion; lower values imply earlier execution. | |
| Action variability | Var​(a0:H−1)\mathrm{Var}\!\big(a\_{0:H-1}\big) |
| Variance of policy actions; high variability may indicate unstable strategies. | |
| No-trade percentage | #​{t:qt=0}H\frac{\#\{\,t:\,q\_{t}=0\,\}}{H} |
| Fraction of minutes where no trades were executed; indicates inactivity. | |
| High-rate in favourable periods | #​{t:qt>ρtarget​Vt∧ptstock<PtVWAP}H\frac{\#\{\,t:\,q\_{t}>\rho\_{\mathrm{target}}V\_{t}\ \wedge\ p^{\mathrm{stock}}\_{t}<P^{\mathrm{VWAP}}\_{t}\,\}}{H} |
| Share of minutes where the agent accelerated trading when the stock outperformed market VWAP. | |
| Low-rate in unfavourable periods | #​{t:qt​<ρtarget​Vt∧ptstock>​PtVWAP}H\frac{\#\{\,t:\,q\_{t}<\rho\_{\mathrm{target}}V\_{t}\ \wedge\ p^{\mathrm{stock}}\_{t}>P^{\mathrm{VWAP}}\_{t}\,\}}{H} |
| Share of minutes where the agent slowed trading when the stock underperformed market VWAP. | |

## References

* Almgren and Chriss, (2001)

  Almgren, R. and Chriss, N. (2001).
  Optimal execution of portfolio transactions.
  The Journal of Risk, 3(2):5–40.
* Amrouni et al., (2022)

  Amrouni, S., Moulin, A., Vann, J., Vyetrenko, S., Balch, T., and Veloso, M.
  (2022).
  ABIDES-gym: gym environments for multi-agent discrete event
  simulation and application to financial markets.
  In Proceedings of the Second ACM International Conference on AI
  in Finance, ICAIF ’21, New York, NY, USA. Association for Computing
  Machinery.
* Bouchaud, (2010)

  Bouchaud, J.-P. (2010).
  Price impact.
  In Encyclopedia of Quantitative Finance. John Wiley & Sons.
* Bouchaud et al., (2018)

  Bouchaud, J.-P., Bonart, J., Donier, J., and Gould, M. (2018).
  The propagator model.
  In Trades, Quotes and Prices: Financial Markets Under the
  Microscope, pages 252–253. Cambridge University Press.
* Bucci et al., (2019)

  Bucci, F., Benzaquen, M., Lillo, F., and Bouchaud, J.-P. (2019).
  Crossover from linear to square-root market impact.
  Physical Review Letters, 122:108302.
* Chatzilygeroudis et al., (2021)

  Chatzilygeroudis, K., Cully, A., Vassiliades, V., and Mouret, J.-B. (2021).
  Quality-diversity optimization: A novel branch of stochastic
  optimization.
  In Pardalos, P. M., Rasskazova, V., and Vrahatis, M. N., editors,
  Black Box Optimization, Machine Learning, and No-Free Lunch Theorems,
  pages 109–135. Springer, Cham.
* Cont et al., (2014)

  Cont, R., Kukanov, A., and Stoikov, S. (2014).
  The price impact of order book events.
  Journal of Financial Econometrics, 12:47–88.
* Faldor et al., (2025)

  Faldor, M., Chalumeau, F., Flageat, M., and Cully, A. (2025).
  Synergizing quality-diversity with descriptor-conditioned
  reinforcement learning.
  ACM Transactions on Evolutionary Learning and Optimization,
  5(1):3 (35 pages).
* Flageat et al., (2025)

  Flageat, M., Huber, J., Helenon, F., Doncieux, S., and Cully, A. (2025).
  Extract-QD framework: A generic approach for quality-diversity in
  noisy, stochastic or uncertain domains.
  In Proceedings of the Genetic and Evolutionary Computation
  Conference, GECCO ’25, pages 140–148, New York, NY, USA. Association for
  Computing Machinery.
* Gatheral et al., (2012)

  Gatheral, J., Schied, A., and Slynko, A. (2012).
  Transient linear price impact and Fredholm integral equations.
  Mathematical Finance, 22(3):445–474.
* Hafsi and Vittori, (2024)

  Hafsi, Y. and Vittori, E. (2024).
  Optimal execution with reinforcement learning.
  arXiv preprint arXiv:2411.06389.
* Hendricks and Wilcox, (2014)

  Hendricks, D. and Wilcox, D. (2014).
  A reinforcement learning extension to the Almgren-Chriss
  framework for optimal trade execution.
  In 2014 IEEE Conference on Computational Intelligence for
  Financial Engineering & Economics (CIFEr), pages 457–464.
* Jerome et al., (2023)

  Jerome, J., Sánchez-Betancourt, L., Savani, R., and Herdegen, M. (2023).
  Mbt-gym: Reinforcement learning for model-based limit order book
  trading.
  In Proceedings of the Fourth ACM International Conference on AI
  in Finance, ICAIF ’23, page 619–627, New York, NY, USA. Association for
  Computing Machinery.
* Lim et al., (2023)

  Lim, B., Allard, M., Grillotti, L., and Cully, A. (2023).
  Accelerated quality-diversity through massive parallelism.
  Transactions on Machine Learning Research.
* Mana Tech LLC, (2025)

  Mana Tech LLC (2025).
  Historical u.s. equities market data.
  <https://manatech.ai/>.
  Accessed: 2025-08-17.
* Mastromatteo et al., (2014)

  Mastromatteo, I., Tóth, B., and Bouchaud, J.-P. (2014).
  Agent-based models for latent liquidity and concave price impact.
  Physical Review Letters, 113(26):268701.
* Mouret and Clune, (2015)

  Mouret, J.-B. and Clune, J. (2015).
  Illuminating search spaces by mapping elites.
  arXiv preprint arXiv:1504.04909.
* Nevmyvaka et al., (2006)

  Nevmyvaka, Y., Feng, Y., and Kearns, M. J. (2006).
  Reinforcement learning for optimized trade execution.
  In Proceedings of the 23rd International Conference on Machine
  Learning (ICML), pages 673–680. ACM.
* Obizhaeva and Wang, (2013)

  Obizhaeva, A. A. and Wang, J. (2013).
  Optimal trading strategy and supply/demand dynamics.
  Journal of Financial Markets, 16(1):1–32.
* Parkinson, (1980)

  Parkinson, M. (1980).
  The extreme value method for estimating the variance of the rate of
  return.
  Journal of Business, 53(1):61–65.
* Perold, (1988)

  Perold, A. F. (1988).
  The implementation shortfall: Paper vs. reality.
  The Journal of Portfolio Management, 14(3):4–9.
* Ray Team, (2025)

  Ray Team (2025).
  RLlib environments: Farama Gymnasium.
  <https://docs.ray.io/en/latest/rllib/rllib-env.html>.
  Accessed: 2026-01-29.
* Schulman et al., (2016)

  Schulman, J., Moritz, P., Levine, S., Jordan, M., and Abbeel, P. (2016).
  High-dimensional continuous control using generalized advantage
  estimation.
  In Proceedings of the International Conference on Learning
  Representations (ICLR).
* Schulman et al., (2017)

  Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O. (2017).
  Proximal policy optimization algorithms.
  arXiv preprint arXiv:1707.06347.
* Stable-Baselines3 Developers, (2025)

  Stable-Baselines3 Developers (2025).
  Using custom environments (Gymnasium interface).
  <https://stable-baselines3.readthedocs.io/en/master/guide/custom_env.html>.
  Accessed: 2026-01-29.
* Sutton and Barto, (2018)

  Sutton, R. S. and Barto, A. G. (2018).
  Reinforcement Learning: An Introduction.
  MIT Press, 2nd edition.
* Towers et al., (2024)

  Towers, M., Kwiatkowski, A., Terry, J., Balis, J. U., De Cola, G., Deleu, T.,
  Goulão, M., Kallinteris, A., Krimmel, M., Arjun, K. G., Perez-Vicente, R.,
  Pierré, A., Schulhoff, S., Tai, J. J., Tan, H., and Younis, O. G. (2024).
  Gymnasium: A standard interface for reinforcement learning
  environments.
  arXiv preprint arXiv:2407.17032.
* Tóth et al., (2011)

  Tóth, B., Lempérière, Y., Deremble, C., de Lataillade, J., Kockelkoren, J.,
  and Bouchaud, J.-P. (2011).
  Anomalous price impact and the critical nature of liquidity in
  financial markets.
  Physical Review X, 1(2):021006.