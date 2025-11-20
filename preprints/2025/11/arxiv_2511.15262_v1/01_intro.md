---
authors:
- Tomas Espana
- Yadh Hafsi
- Fabrizio Lillo
- Edoardo Vittori
doc_id: arxiv:2511.15262v1
family_id: arxiv:2511.15262
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution'
url_abs: http://arxiv.org/abs/2511.15262v1
url_html: https://arxiv.org/html/2511.15262v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tomas Espana1
Yadh Hafsi2
Fabrizio
Lillo3
Edoardo Vittori4
  
1 ORFE, Princeton University, Princeton, NJ, USA
  
2 CMAP, École Polytechnique, Palaiseau, France
  
3 Scuola Normale Superiore, Pisa, Italy
  
4 Intesa Sanpaolo, Milan, Italy
  
tomas.espana@princeton.eduyadh.hafsi@polytechnique.edu, [![[Uncaptioned image]](orcid.png)](https://orcid.org/https://orcid.org/0009-0001-0686-0349)fabrizio.lillo@sns.it, [![[Uncaptioned image]](orcid.png)](https://orcid.org/https://orcid.org/0000-0002-4931-4057)edoardo.vittori@intesasanpaolo.com

(November 19, 2025)

###### Abstract

We investigate the use of Reinforcement Learning for the optimal execution of meta-orders, where the objective is to execute incrementally large orders while minimizing implementation shortfall and market impact over an extended period of time. Departing from traditional parametric approaches to price dynamics and impact modeling, we adopt a model-free, data-driven framework. Since policy optimization requires counterfactual feedback that historical data cannot provide, we employ the Queue-Reactive Model to generate realistic and tractable limit order book simulations that encompass transient price impact, and nonlinear and dynamic order flow responses. Methodologically, we train a Double Deep Q-Network agent on a state space comprising time, inventory, price, and depth variables, and evaluate its performance against established benchmarks. Numerical simulation results show that the agent learns a policy that is both strategic and tactical, adapting effectively to order book conditions and outperforming standard approaches across multiple training configurations. These findings provide strong evidence that model-free Reinforcement Learning can yield adaptive and robust solutions to the optimal execution problem.

Keywords : Optimal Execution, Reinforcement Learning, Queue-Reactive Model, Limit Order Book, Market Microstructure, Price impact.

## 1 Introduction

Executing large orders efficiently is a fundamental challenge in electronic financial markets. Large transactions, typically initiated by institutional investors such as banks, asset managers, hedge funds, or proprietary trading firms, often consume visible liquidity across multiple price levels of the limit order book (LOB), generating significant price impact. This impact is manifested through both immediate price shifts and subsequent order flow reactions and motivates the need for execution strategies that optimally balance market impact against timing risk. Consequently, the design of optimal execution strategies has become a central topic in market microstructure and algorithmic trading research.

Several studies have deepened the theoretical and empirical understanding of market impact. Refs [bouchaud2003fluctuations] and [bouchaud2009markets] documented the transient and concave nature of impact, highlighting its origin in the interplay between order flow, liquidity consumption, and market participant behavior. These empirical findings motivated the introduction of new constraints and mechanisms in the optimal execution problem. The first formal treatment of the problem is due to [optimal\_bertsimas\_1998], who derive closed-form solutions under specific assumptions using dynamic programming. This framework was extended by [almgren], who introduced both permanent and temporary market impact components, as well as a risk-aversion parameter. Subsequent research has generalized the Almgren-Chriss model along several dimensions (see [optimal\_almgren\_2003, optimal\_huberman\_2005, optimal\_gatheral\_2011, optimal\_almgren\_2012, optimal\_obizhaeva\_2013, optimal\_cheridito\_2014, gueant2015general, optimal\_cartea\_2015, incorporating\_cartea\_2016, optimal\_curato\_2017, optimal\_digiacinto\_2022, optimal\_cartea\_2022, chevalier2024, chevalier2025]). Notably, [gatheral2012transient] established that transient impact models must satisfy a no-dynamic-arbitrage condition, which tightly links the functional form of impact decay to the underlying price dynamics. This result rules out many ad-hoc impact kernels and provides structural constraints on any admissible transient impact model. [optimal\_obizhaeva\_2013] further developed this direction by introducing a continuous-time propagator model in which impact decays through limit-order-book resilience.

Although these developments significantly enriched our understanding of execution costs and impact mechanisms, they still rely on strong parametric and structural assumptions that might be in contrast with the true data generating process and might be difficult to calibrate empirically. Model parameters such as impact coefficients, volatility processes, and resilience rates remain highly context-dependent and vary across time and assets, limiting the robustness of these approaches. In fact, traditional methods for solving stochastic control problems face limitations. Closed-form solutions are rare and require restrictive assumptions on the model dynamics and objective function. Numerical approaches typically involve solving the Hamilton-Jacobi-Bellman (HJB) equation, quasi-variational inequalities, or backward stochastic differential equations (BSDEs). These formulations often rely on viscosity solution theory to establish existence, uniqueness, and regularity of the value function. Yet, the associated numerical schemes, such as Monte Carlo methods for BSDEs and finite-difference methods for PDEs, suffer from the curse of dimensionality. As a result, these techniques are generally limited to problems with low-dimensional state spaces.

#### Related Works.

To address these limitations, reinforcement learning methods [reinforcement\_sutton\_1998] have emerged as data-driven and model-free alternatives for sequential decision problems. Unlike classical approaches, reinforcement learning (RL) does not require strong parametric assumptions on market dynamics. In the context of optimal execution, RL provides a flexible framework to learn trading policies directly from simulated or historical market data. The first application of RL to optimal execution was introduced by [reinforcement\_nevmyvaka\_2006], who trained a tabular Q-learning agent to minimize implementation shortfall using historical trade data. Building on this, [hendricks\_2014] proposed a hybrid approach that combined the Almgren–Chriss (AC) model with Q-learning, allowing the agent to adjust its execution trajectory dynamically based on the observed market state. To overcome the limitations of tabular methods in high-dimensional settings, [double\_ning\_2018] employed Double Deep Q-Networks (DDQN) (see [humanlevel\_mnih\_2015, vanhasselt\_2016]), integrating deep neural networks with Q-learning to generalize across continuous state spaces and mitigate value overestimation bias. More recently, [macri\_2024] applied DDQN within the AC framework under time-varying liquidity conditions, demonstrating improved performance relative to benchmark strategies, while [endtoend\_lin\_2020] employed Proximal Policy Optimization (PPO) (see [proximal\_schulman\_2017]) to train agents that learn directly from limit order book data using sparse reward structures.

Existing approaches rely on specific market impact assumptions and on historical data, which do not capture how market conditions evolve in response to trading actions. It therefore remains unclear what reinforcement learning algorithms can learn in more realistic, microstructure-based settings that incorporate endogenous market impact. In this work, we address this question using a limit order book (LOB) simulator that models both direct market impact, from liquidity consumption, and indirect impact, from participants’ reactions to trades. Many market simulators have been proposed in the literature, including agent-based models [abides\_byrd\_2020, minimal\_alfi\_2009, econophysics\_chakraborti\_2011, agentbased\_hamill\_2015] and generative models [generating\_li\_2020, learning\_coletta\_2022, limit\_cont\_2023, generative\_nagy\_2023, lobbench\_nagy\_2025]. Recent studies have explored such simulation-based frameworks [hafsi2024optimal, cheridito2025reinforcement]. While these approaches can capture complex market behaviors, they can be more difficult to implement and calibrate, and, more importantly, they often lack analytical tractability.

#### Main Contributions.

We employ the Queue Reactive Model (QRM) (see [huang\_2015]). The QRM provides a realistic yet tractable description of short-term limit-order-book dynamics. Instead of assuming that price changes follow a simple diffusion, it treats the best bid and ask as queues of standing orders that evolve through limit-order arrivals, cancellations, and market-order executions. The rates at which these events occur depend on the current state of the book, particularly the size imbalance between the bid and ask queues, which means that the model naturally links order-flow pressure to short-term price movements. When either queue is depleted, the price moves by one tick, and new queue sizes are redrawn from empirical distributions calibrated to market data. This simple mechanism reproduces key microstructure features such as liquidity resilience, mean-reverting price behavior, and transient price impact: a trade that consumes liquidity temporarily shifts the state of the book, altering subsequent order flow and gradually decaying as liquidity replenishes. Because QRM captures both direct and indirect market impact within a statistically grounded framework, it serves as a practical simulator of endogenous market reactions.

The goal of this paper is to propose a methodology to build a theoretically grounded and microstructure-consistent training and testing environment for RL. Specifically, the QRM is analytically tractable and ergodic, reproducing key stylized facts of LOB dynamics such as resilience, transient impact, and order-flow imbalance. We use model parameters calibrated from real market data and train an RL agent in this environment to learn execution strategies that generalize across endogenous market states. In contrast to existing approaches, our framework captures both direct impact (via liquidity consumption) and indirect impact (via feedback effects on order flow), offering a more realistic and interpretable platform for learning execution policies.

Calibrate QRM on real market dataLearn optimal execution strategy with RL in ergodic environmentDeploy in real market environment


Figure 1: Proposed methodology: learning optimal execution strategies using RL.

This paper is organized as follows. Section [2](https://arxiv.org/html/2511.15262v1#S2 "2 Problem Formulation ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") formalizes the optimal execution problem and establishes the notation used throughout. Section [3](https://arxiv.org/html/2511.15262v1#S3 "3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") introduces the Queue-Reactive Model (QRM), which provides the market environment. Section [4](https://arxiv.org/html/2511.15262v1#S4 "4 Optimal Execution Setting ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") embeds this problem within a Reinforcement Learning (RL) and Markov Decision Process (MDP) framework, describing how learning-based agents interact with the market. Finally, Section [5](https://arxiv.org/html/2511.15262v1#S5 "5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") presents and discusses the results of our experiments.

## 2 Problem Formulation

The optimal execution problem consists in executing a trade of X0X\_{0} shares over a fixed time horizon [0,T][0,T]. We consider here the problem of optimally executing a buy metaorder. When constructing such a strategy, it is essential to account for the immediate transaction impact of trades, their temporary price effects, and the potential long-term consequences arising from persistent market responses. A terminal penalty term may also be introduced to reflect the cost associated with failing to complete the purchase by the end of the horizon.

In a discrete-time setting with N+1N{+}1 decision points, the purchasing strategy is formulated as a sequential decision process, in which the trader determines the quantity Δ​xτk\Delta x\_{\tau\_{k}} to buy at each time step τk=k​T/N\tau\_{k}\!=\!kT/N, for k∈{0,…,N}k\!\in\!\{0,\ldots,N\}, with τ0=0\tau\_{0}\!=\!0 and τN=T\tau\_{N}\!=\!T. The cumulative purchases form a trajectory {xτ0,…,xτN}\{x\_{\tau\_{0}},\ldots,x\_{\tau\_{N}}\}, where xτkx\_{\tau\_{k}} denotes the cumulative number of shares acquired by time τk\tau\_{k}. By construction, x0=0x\_{0}\!=\!0, and full completion requires xT=X0x\_{T}\!=\!X\_{0} at the terminal time. Let PτkP\_{\tau\_{k}} denote the average execution price for the purchase Δ​xτk=xτk−xτk−1\Delta x\_{\tau\_{k}}\!=\!x\_{\tau\_{k}}\!-\!x\_{\tau\_{k-1}}, which depends on both the current and all preceding trades and incorporates all transaction costs. The objective of a risk-neutral trader is to minimize the expected total cost of purchase over the horizon TT:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minx∈𝒜⁡𝔼​[∑k=0NPτk​Δ​xτk],where𝒜={(xτ0,xτ1,…,xτN)∈ℝ+N+1:∑k=0NΔ​xτk=X0}.\begin{gathered}\min\_{x\in\mathcal{A}}\mathbb{E}\left[\sum\_{k=0}^{N}P\_{\tau\_{k}}\Delta x\_{\tau\_{k}}\right],\\ \text{where}\quad\mathcal{A}=\Big\{(x\_{\tau\_{0}},x\_{\tau\_{1}},\ldots,x\_{\tau\_{N}})\in\mathbb{R}^{N+1}\_{+}:\sum\_{k=0}^{N}\Delta x\_{\tau\_{k}}=X\_{0}\Big\}.\end{gathered} |  | (1) |

The cost functional in Equation ([1](https://arxiv.org/html/2511.15262v1#S2.E1 "Equation 1 ‣ 2 Problem Formulation ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")) is directly related to the Implementation Shortfall (IS) measure introduced by [Perold1988], which quantifies the deviation between the realized cost of execution and the cost that would have been incurred had all shares been purchased instantaneously at the initial market price P0P\_{0}. Formally, for a purchasing strategy, the IS is defined as

|  |  |  |
| --- | --- | --- |
|  | IS=∑k=0NPτk​Δ​xτk−X0​P0,\text{IS}=\sum\_{k=0}^{N}P\_{\tau\_{k}}\,\Delta x\_{\tau\_{k}}-X\_{0}P\_{0}, |  |

where the first term represents the realized cost of execution and the second term
corresponds to the paper cost associated with immediate execution at P0P\_{0}. Minimizing the expected total cost is therefore equivalent to minimizing the expected IS, since the benchmark term X0​P0X\_{0}P\_{0} is constant and independent of the trading strategy.
Economically, this formulation captures the fundamental trade-off between
*market impact* and *timing risk* as in [almgren]: executing too quickly increases costs through adverse price impact,
while executing too slowly exposes the trader to unfavorable price movements. Hence, minimizing the expected IS is equivalent to finding the purchasing trajectory
that optimally balances liquidity consumption and exposure to price risk.

## 3 The Queue-Reactive Model

The QRM, introduced by [huang\_2015], provides a stochastic representation of the limit order book specifically tailored to large-tick assets. This mechanism enables the model to reproduce the stylized facts
in high-frequency markets, including the persistence of order-flow imbalance, asymmetric liquidity profiles, and mean-reverting mid-price dynamics.

### 3.1 Description of the Market Simulation

At each time tt, the state of the LOB is represented by a 2​K2K-dimensional vector

|  |  |  |
| --- | --- | --- |
|  | X​(t)=(q−K​(t),…,q−1​(t),q1​(t),…,qK​(t)),X(t)=(q\_{-K}(t),\ldots,q\_{-1}(t),q\_{1}(t),\ldots,q\_{K}(t)), |  |

where KK denotes the number of visible price levels on each side of the book. The quantity qi​(t)q\_{i}(t) denotes the standing volume at level QiQ\_{i} at time tt priced at

|  |  |  |
| --- | --- | --- |
|  | pi=pref+i​δ2,∀i∈{−K,…,−1,1,…,K},p\_{i}=p\_{\mathrm{ref}}+\frac{i\,\delta}{2},\quad\forall i\in\{-K,\ldots,-1,1,\ldots,K\}, |  |

with δ\delta the tick size and prefp\_{\mathrm{ref}} an unobservable *reference price* centered within the LOB. By convention, Q−iQ\_{-i} denotes a bid level and QiQ\_{i} an ask level. Formally, X​(t)X(t) evolves as a continuous-time Markov jump process taking values in ℕ2​K\mathbb{N}^{2K} with generator matrix ℒ\mathcal{L} specified by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒl,l+ei=fi​(l),\displaystyle\mathcal{L}\_{l,l+e\_{i}}=f\_{i}(l), |  | (2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒl,l−ei=gi​(l),\displaystyle\mathcal{L}\_{l,l-e\_{i}}=g\_{i}(l), |  | (3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒl,l=−∑p≠lℒl,p,\displaystyle\mathcal{L}\_{l,l}=-\sum\_{p\neq l}\mathcal{L}\_{l,p}, |  | (4) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒl,p=0otherwise,\displaystyle\mathcal{L}\_{l,p}=0\quad\text{otherwise}, |  | (5) |

with l=(l−K,…,l−1,l1,…,lK)∈ℕ2​Kl=(l\_{-K},\ldots,l\_{-1},l\_{1},\ldots,l\_{K})\in\mathbb{N}^{2K} and eie\_{i} denoting the vector ii of the canonical basis of ℝ2​K\mathbb{R}^{2K}. Each queue qi​(t)q\_{i}(t) evolves as a one-dimensional birth–death process governed by the state-dependent intensities λiL​(qi​(t))\lambda\_{i}^{L}(q\_{i}(t)) for limit order arrivals, λiM​(qi​(t))\lambda\_{i}^{M}(q\_{i}(t)) for market orders consuming liquidity at level ii, and λiC​(qi​(t))\lambda\_{i}^{C}(q\_{i}(t)) for order cancellations. Note there is no bid-ask distinction as we suppose bid-ask symmetry. The transition rates at time tt are

|  |  |  |
| --- | --- | --- |
|  | fi​(X​(t))=λiL​(qi​(t)),andgi​(X​(t))=λiM​(qi​(t))+λiC​(qi​(t)),f\_{i}(X(t))=\lambda\_{i}^{L}(q\_{i}(t)),\penalty 10000\ \penalty 10000\ \textrm{and}\penalty 10000\ \penalty 10000\ g\_{i}(X(t))=\lambda\_{i}^{M}(q\_{i}(t))+\lambda\_{i}^{C}(q\_{i}(t)), |  |

for all i∈[−K,…,−1,1,…,K]i\in[-K,\dots,-1,1,\dots,K]. Conditionally on the current state of the book, order arrivals at each level follow independent Poisson processes. The dependence of intensities on queue sizes induces both auto and cross correlations in the order flow, producing realistic microstructural dynamics.

###### Remark 3.1.

We retain Model 1 of [huang\_2015], where the intensities λiL\lambda\_{i}^{L}, λiM\lambda\_{i}^{M}, and λiC\lambda\_{i}^{C} depend solely on the size of the corresponding queue qi​(t)q\_{i}(t). Empirical calibration in [huang\_2015] shows that this specification captures most of the variation in order‐flow intensities, with only minor gains in likelihood from adding neighboring queues or imbalance. Later studies [ergodicity\_huang\_2017] confirm that richer dependencies mainly improve qualitative realism, while the overall quantitative fit remains comparable.

### 3.2 Invariant Distribution and Ergodicity

Under mild assumptions, [huang\_2015] prove that the 2​K2K-dimensional Markov jump process XX is ergodic. This means that there exists a unique invariant probability measure π\pi and that the process converges to it from any start.

###### Theorem 3.1 (Ergodicity).

Assume that

1. (i)

   there exist Cbound∈ℕC\_{\mathrm{bound}}\in\mathbb{N} and δ0>0\delta\_{0}>0 such that, for all i∈[−K,…,−1,1,…,K]i\in[-K,\dots,-1,1,\dots,K] and any p=(p−K,…,p−1,p1,…,pK)∈ℕ2​Kp=(p\_{-K},\ldots,p\_{-1},p\_{1},\ldots,p\_{K})\in\mathbb{N}^{2K} with pi>Cboundp\_{i}>C\_{\mathrm{bound}}, we have

   |  |  |  |
   | --- | --- | --- |
   |  | fi​(p)−gi​(p)≤−δ0;f\_{i}(p)-g\_{i}(p)\leq-\delta\_{0}; |  |
2. (ii)

   there exists H>0H>0 such that ∑ifi​(p)≤H\sum\_{i}f\_{i}(p)\leq H for every state p∈ℕ2​Kp\in\mathbb{N}^{2K}.

Then XX is non-explosive, irreducible, positive recurrent, and therefore
ergodic with a unique invariant probability measure π\pi.

###### Proof.

See Theorem 2.12.1 in [huang\_2015].
∎

The invariant distribution πi\pi\_{i} of the limit QiQ\_{i} is given by the intensities of the process introduced previously. Define the arrival/departure ratio ρi\rho\_{i} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρi​(n)=λiL​(n)λiC​(n+1)+λiM​(n+1).\displaystyle\rho\_{i}(n)=\frac{\lambda\_{i}^{L}(n)}{\lambda\_{i}^{C}(n+1)+\lambda\_{i}^{M}(n+1)}. |  | (6) |

The invariant distribution satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi​(0)=(1+∑n=1∞∏j=1nρi​(j−1))−1,andπi​(n)=πi​(0)​∏j=1nρi​(j−1).\displaystyle\pi\_{i}(0)=\left(1+\sum\_{n=1}^{\infty}\prod\_{j=1}^{n}\rho\_{i}(j-1)\right)^{-1},\penalty 10000\ \penalty 10000\ \textrm{and}\penalty 10000\ \penalty 10000\ \pi\_{i}(n)=\pi\_{i}(0)\prod\_{j=1}^{n}\rho\_{i}(j-1). |  | (7) |

### 3.3 Price Dynamics

The process XX described above characterizes the LOB dynamics for a fixed reference price prefp\_{\mathrm{ref}}. To endogenize price movements, two additional parameters are introduced, θ\theta and θreinit\theta^{\mathrm{reinit}}. Whenever the mid-price pmidp\_{\mathrm{mid}} changes, the reference price prefp\_{\mathrm{ref}} moves by one tick in the same direction with probability θ\theta, provided that the corresponding best queue is depleted (q±1=0q\_{\pm 1}\!=\!0). Following such a reference-price change, the LOB state is either redrawn from its invariant distribution π\pi, centered around the new prefp\_{\mathrm{ref}}, with probability θreinit\theta^{\mathrm{reinit}}, or the standing volumes are shifted accordingly with probability 1−θreinit1\!-\!\theta^{\mathrm{reinit}}. Figure [2](https://arxiv.org/html/2511.15262v1#S3.F2 "Figure 2 ‣ 3.3 Price Dynamics ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") illustrates these mechanisms when a market order depletes the best ask volume.

pref=pmid=1.005p\_{\mathrm{ref}}\!=\!p\_{\mathrm{mid}}\!=\!1.005MO at best ask0.980.991.001.011.021.031.04pref=pmid=1.015p\_{\mathrm{ref}}\!=\!p\_{\mathrm{mid}}\!=\!1.0150.980.991.001.011.021.031.04pmid=1.01p\_{\mathrm{mid}}\!=\!1.01pref=1.015p\_{\mathrm{ref}}\!=\!1.0150.980.991.001.011.021.031.04pref=1.005p\_{\mathrm{ref}}\!=\!1.005pmid=1.01p\_{\mathrm{mid}}\!=\!1.010.980.991.001.011.021.031.04θ\theta1−θ1-\thetaθreinit\theta^{\mathrm{reinit}}1−θreinit1-\theta^{\mathrm{reinit}}


Figure 2: QRM response to consuming the best ask q1q\_{1} at time tt with tick size δ=0.01\delta=0.01. The root node shows a typical LOB state just before the trade at time t−t^{-}, with volumes drawn from the invariant distribution, while the leaf nodes depict the possible post-trade configurations generated by the QRM dynamics at time tt.

In [huang\_2015], the authors of interpret parameter θreinit\theta^{\mathrm{reinit}} as quantifying the proportion of price changes associated with exogenous information shocks. Following such shocks, market participants typically rebalance their order flows around the new reference price almost instantaneously. The empirical calibration of [huang\_2015] using France Télécom (Euronext Paris) data from January 20102010 to March 20122012, yields θ=0.7\theta\!=\!0.7 and θreinit=0.85\theta^{\mathrm{reinit}}\!=\!0.85,
implying that most price adjustments are accompanied by rapid order-book reconfigurations. Although this value may seem high, since volatility models generally attribute around 80%80\% of price variance to endogenous, self-referential mechanisms (see for example [trades\_bouchaud\_2018]), it can alternatively be understood as the probability that the order book refills following a price movement driven either by market makers or by algorithmic liquidity provision. Henceforth, unless otherwise stated, we adopt the same calibration as [huang\_2015] and use the same order-flow intensities.

### 3.4 Market impact

In this Section, we explore the joint role of (θ,θreinit)(\theta,\theta^{\mathrm{reinit}}) in shaping liquidity dynamics. To this end, we analyze how the QRM responds when an external trader consumes the entire best ask volume q1q\_{1}, as shown in Figure [2](https://arxiv.org/html/2511.15262v1#S3.F2 "Figure 2 ‣ 3.3 Price Dynamics ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"). This controlled perturbation shows that different parameter combinations give rise to distinct market-impact regimes, where some configurations lead to prices mean-reverting after the trade, corresponding to a transient impact, while others result in prices continuing to rise on average, corresponding to a permanent impact.

Let tk−t\_{k}^{-} denote the time just before a buy MO at the best ask that consumes all the best ask volume and pkp\_{k} the associated mid-price after. The index kk runs over all the events, and not only the MOs. Furthermore, we assume pref​(tk−)=pmid​(tk−)p\_{\mathrm{ref}}(t\_{k}^{-})\!=\!p\_{\mathrm{mid}}(t\_{k}^{-}), with the surrounding volumes q±iq\_{\pm i} sampled from the invariant distribution, consistent with the ergodicity of the process XX under mild conditions. For simplicity, all queues q±iq\_{\pm i} are considered non-empty, as this represents the typical configuration of the invariant distribution π\pi. When the LOB is redrawn from π\pi, we assume without loss of generality that all queues are non-empty, as the contribution of empty queues cancels out on average by bid–ask symmetry. The expected mid-price jump after consuming the best ask is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Δ​pk]:=𝔼​[pk−pk−1]=(1+θ​θreinit)​δ2,\displaystyle\mathbb{E}[\Delta p\_{k}]:=\mathbb{E}[p\_{k}-p\_{k-1}]=(1+\theta\,\theta^{\mathrm{reinit}})\frac{\delta}{2}, |  | (8) |

where δ\delta is the tick size. As expected, 𝔼​[Δ​pk]\mathbb{E}[\Delta p\_{k}] increases with both θ\theta and θreinit\theta^{\mathrm{reinit}}, consistent with the behavior observed in Figure [3](https://arxiv.org/html/2511.15262v1#S3.F3 "Figure 3 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution").

![Refer to caption](x1.png)


Figure 3: Average mid-price across 20,00020{,}000 simulations in which a trader systematically buys the entire best ask at fixed time intervals (vertical dashed lines). We set θ=0.7\theta\!=\!0.7.

Consider now the next event k+1k\!+\!1 that updates the LOB.
With probability θ​θreinit\theta\theta^{\mathrm{reinit}}, the book is redrawn from its invariant distribution and the mid-price remains unchanged on average.
With probability θ​(1−θreinit)\theta(1\!-\!\theta^{\mathrm{reinit}}), a bid refill occurs, increasing the price by δ/2\delta/2;
conversely, with probability (1−θ)(1\!-\!\theta), an ask refill occurs, decreasing the price by δ/2\delta/2 and inducing mean reversion. These last two events provide a first-order approximation, as in the large-tick regime the next events are typically bid or ask refills. Averaging over these outcomes yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Δ​pk+1]=[θ​(2−θreinit)−1]​δ2,\mathbb{E}[\Delta p\_{k+1}]=\big[\theta(2-\theta^{\mathrm{reinit}})-1\big]\frac{\delta}{2}, |  | (9) |

which holds on very short time scales only. The sign of θ​(2−θreinit)−1\theta(2-\theta^{\mathrm{reinit}})\!-\!1 delineates the post-trade regime:
a positive value implies that the quote adjustment after the trade is on average in the same direction of the trade, while a negative value indicates a mean reversion of the midprice after the trade.

In order to numerically test this expression, we initialize the LOB by sampling it from the invariant distribution and then we "send" a buy market order that completely depletes the best ask. Here and in the following we set the tick size at δ=0.01\delta=0.01. Figure [4](https://arxiv.org/html/2511.15262v1#S3.F4 "Figure 4 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") illustrates the contour plot of the estimated 𝔼​[Δ​pk+1]\mathbb{E}[\Delta p\_{k+1}] for different values of θ,θreinit∈[0.5,1.0]\theta,\theta^{\mathrm{reinit}}\!\in\![0.5,1.0]. The dashed black line in the figure denotes the theoretical frontier 𝔼​[Δ​pk+1]=0\mathbb{E}[\Delta p\_{k+1}]\!=\!0 described by Equation ([9](https://arxiv.org/html/2511.15262v1#S3.E9 "Equation 9 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")), aligning closely with the empirical phase boundary (white region).

![Refer to caption](x2.png)


(a) Short term.

![Refer to caption](x3.png)


(b) Long term.

Figure 4: Heatmaps of expected immediate price change 𝔼​[Δ​pk+1]\mathbb{E}[\Delta p\_{k+1}] (left) and cumulative impact 𝔼​[pk+75−pk]\mathbb{E}[p\_{k+75}\!-\!p\_{k}] averaged over 20,00020{,}000 simulations (right) starting from a stationary LOB state with an exogenous trader consuming the best ask. The black cross marks (θ,θreinit)=(0.7,0.85)(\theta,\theta^{\text{reinit}})\!=\!(0.7,0.85).

We now numerically study the long term behavior of the price after an ask depleting market order. The difficulty of course is to establish, for the different parameter configurations, when the asymptotic value of the price has been reached. We first consider a fixed time interval and estimate 𝔼​[pk+75−pk]\mathbb{E}[p\_{k+75}\!-\!p\_{k}] as a function of (θ,θreinit)(\theta,\theta^{\text{reinit}}) (see Figure [4](https://arxiv.org/html/2511.15262v1#S3.F4 "Figure 4 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")). We observe that prices consistently exhibit long-term mean reversion across all parameter configurations. The only exception is the white region in the top-right corner of Figure [4](https://arxiv.org/html/2511.15262v1#S3.F4 "Figure 4 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"), which occurs because for large values of both θ\theta and θreinit\theta^{\mathrm{reinit}} the
volumes are almost always redrawn from the invariant distribution around the updated reference price. As θ\theta and θreinit\theta^{\mathrm{reinit}} decrease, prices exhibit a stronger mean reversion (blue regions), with the long-term intensity of this effect governed primarily by θ\theta. As shown in Figure [2](https://arxiv.org/html/2511.15262v1#S3.F2 "Figure 2 ‣ 3.3 Price Dynamics ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"), there are two scenarios after buying the best ask: either the LOB is redrawn from its invariant distribution, or there is a bid-ask refill. When the LOB is redrawn from the invariant distribution, the average mid-price remains constant due to bid–ask symmetry. Thus, this scenario does not contribute to the observed mid-price changes, which are entirely accounted for by the bid-ask refill scenarios (see Appendix [B.2](https://arxiv.org/html/2511.15262v1#A2.SS2 "B.2 Market Impact ‣ Appendix B Additional Plots ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")).

![Refer to caption](x4.png)


(a) (θ,θreinit)=(0.7,0.85)(\theta,\theta^{\mathrm{reinit}})\!=\!(0.7,0.85).

![Refer to caption](x5.png)


(b) (θ,θreinit)=(0.9,0.6)(\theta,\theta^{\mathrm{reinit}})\!=\!(0.9,0.6).

Figure 5: Evolution of 𝔼​[pk]\mathbb{E}[p\_{k}] after buying the best ask at k=0k\!=\!0, averaged over 1,000,0001{,}000{,}000 simulations. The mid-price before the trade is 100.005100.005 (horizontal dashed line).

To investigate in more detail the price reversion after a trade, we now fix the value of (θ,θreinit)(\theta,\theta^{\mathrm{reinit}}) and study the average price dynamics via numerical simulations. As before, we draw the initial state of the LOB from the invariant distribution and then we consider two scenarios: in the first, as above, we send a buy market order of size equal to the best ask, while in the second the size is half of the best ask volume111Since QRM orders have integer size, we set the market order size to the floor of half the ask volume.. We make this choice because the RL algorithm used below will have these options (plus the choice of not trading) in the action space. Figure [5](https://arxiv.org/html/2511.15262v1#S3.F5 "Figure 5 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") shows the average price trajectories for two configurations of (θ,θreinit)(\theta,\theta^{\text{reinit}}). We observe that in both cases, when the market order depletes the best ask, the price displays a clear mean reversion, which can be very slow as in the right top panel. On the contrary, when the size of the market order is half the volume at the best ask (clearly without mechanically moving the price), the price trends in the same direction of the trade. This difference indicates that the impact model associated with the QRM is inherently nonlinear in the trade size, differently from reduced form standard models used in optimal execution, such as Almgren & Chriss or the Transient Impact Model222Interestingly, extensions of the Transient Impact Model with more propagators, such as the one in [Taranto03062018], are able to reproduce the behavior in Figure [5](https://arxiv.org/html/2511.15262v1#S3.F5 "Figure 5 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"). However the closed form solution for the optimal execution problem is not known in this case. [bouchaud2003fluctuations]. This implies that the optimal trading for the QRM should tactically place market orders of a size which depends, among other things, on the state of the LOB and this makes the problem inherently complex justifying the adoption of deep RL to solve it. Moreover, we expect that the price trajectory after a trade depends also on the absolute volume at the ask and not only on the fraction of it taken by the trade333We cannot test it directly with this type of simulations because it depends on the correlation between consecutive queue sizes, which is zero when sampling from the invariant distribution. In fact, when the best ask has a small volume, it is likely that the second best ask volume is also small, inducing the possibility of a trending price in the direction of the depleting market order.. We will add this variable in the state space of the RL algorithm and we will show below that it brings a significant contribution to its performance.

###### Remark 3.2.

From an implementation perspective, the simulator is designed such that when the trader consumes the full best ask, triggering a mid-price change, the QRM reacts identically to a mid-price change generated endogenously within the model, since it does not differentiate between endogenous and exogenous price movements.

## 4 Optimal Execution Setting

### 4.1 Markov Decision Process Embedding

The execution problem is formulated as a Markov Decision Process (MDP). The MDP is defined as a tuple ⟨𝒮,𝒜,ℙ,ℛ,γ,μ⟩\langle\mathcal{S},\mathcal{A},\mathbb{P},\mathcal{R},\gamma,\mu\rangle (see [puterman2014markov]), where 𝒮\mathcal{S} is the state space, 𝒜\mathcal{A} the action space, ℙ(⋅|s,a)\mathbb{P}(\cdot|s,a) is a Markovian transition model that assigns to each state-action pair (s,a)(s,a) the probability of reaching the next state s′s^{\prime}, ℛ​(s,a)\mathcal{R}(s,a) is a bounded reward function, γ∈[0,1[\gamma\!\in\![0,1[ is the discount factor, and μ\mu is the distribution of the initial state.

#### State space

Each state sτks\_{\tau\_{k}} at time τk\tau\_{k} for k∈{0,…​n}k\!\in\!\{0,\dots n\} is defined as

|  |  |  |
| --- | --- | --- |
|  | sτk=(τk,inventoryτk,best ask priceτk,best bid volumeτk,best ask volumeτk).\displaystyle s\_{\tau\_{k}}=\big(\,\tau\_{k},\;\text{inventory}\_{\tau\_{k}},\;\text{best ask price}\_{\;\tau\_{k}},\;\text{best bid volume}\_{\;\tau\_{k}},\;\text{best ask volume}\_{\;\tau\_{k}}\,\big). |  |

This constitutes a minimal state representation. The agent is informed of the remaining time, its current inventory, and relevant local market conditions in terms of price and liquidity. In particular, the inclusion of both best bid and best ask volumes allows the agent to infer volume imbalance, a well-established short-term predictor of price movements in market microstructure (see [pulido2024understandingworstkeptsecrethighfrequency]). A state is considered terminal either when the time horizon TT is reached or when the agent has fully executed its inventory prior to TT.

#### Action space

Since the QRM is designed to model large-tick stocks, the action space is constructed so that the agent may consume at most the best ask volume, as trading beyond the first depth level is prohibitively costly.
Empirical evidence supports that traders rarely consume more than the first level (see [Pomponio2010]). The action space therefore consists of percentages, where taking an action of, say, 50%50\% at time τk\tau\_{k} corresponds to buying half of the best available ask at time τk−\tau\_{k}^{-}.
This formulation enables the RL agent to adjust its trading volume proportionally to prevailing market conditions: executing 50%50\% of the available best when liquidity is high is more profitable than when liquidity is low, while the market impact in both cases remains comparable.

In the QRM, the state variables qiq\_{i} at each depth ii are expressed in units normalized by the *Average Event Size* (AESi)(\text{AES}\_{i}), which represents the mean event size across limit, market, and cancel orders observed at level QiQ\_{i}.
Accordingly, the executable quantities Δ​xτk\Delta x\_{\tau\_{k}} are integer-valued, xτk∈ℕx\_{\tau\_{k}}\in\mathbb{N}.
In what follows, we focus on a simplified action space,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜={0%,50%,100%},\displaystyle\mathcal{A}=\{0\%,50\%,100\%\}, |  | (10) |

which allows the agent either to remain inactive, consume half the entire best ask or the entire best ask, thereby accelerating convergence during training.

#### Reward function

In this work, our goal is to minimize the expected implementation shortfall under the risk-neutral probability measure. The instantaneous reward at time τk\tau\_{k} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rτk=Δ​xτk​(P0−Pτk)−α​1l{τk=T}​(X0−xT),\displaystyle r\_{\tau\_{k}}=\Delta x\_{\tau\_{k}}(P\_{0}-P\_{\tau\_{k}})-\alpha\mbox{1\hskip-2.5ptl}\_{\{\tau\_{k}=T\}}(X\_{0}-x\_{T}), |  | (11) |

where P0P\_{0} denotes the initial midprice, Δ​xτk\Delta x\_{\tau\_{k}} the number of shares executed, α>0\alpha>0 a positive constant and PτkP\_{\tau\_{k}} the execution price, which in our setting is always the best ask. A terminal penalty is applied if the agent fails to fully execute the inventory by the end of the horizon.
This penalty is equal to the number of shares remaining to be executed, scaled by a final penalty parameter α\alpha, thereby encouraging complete execution of the X0X\_{0} shares before time TT. For higher risk aversion, the execution horizon TT may be shortened to limit price-risk exposure.

### 4.2 Reinforcement Learning

In this paper, we employ Deep Reinforcement Learning to approximate the optimal execution schedule within the QRM model. Specifically, we adopt the Double Deep Q-Network (DDQN) algorithm [vanhasselt\_2016], a model-free, online, off-policy reinforcement learning approach, which provides a model-agnostic solution to the optimal execution problem.

In this work, we focus on the Double Deep Q-Network (DDQN) algorithm as it provided the best learning results. Algorithm [1](https://arxiv.org/html/2511.15262v1#alg1 "Algorithm 1 ‣ 4.2 Reinforcement Learning ‣ 4 Optimal Execution Setting ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") presents the training procedure for a Double Deep Q-Network (DDQN) agent.

Algorithm 1  DDQN Algorithm in the QRM environment

1:Initialize QmainQ\_{\text{main}} (random weights), Qtgt←QmainQ\_{\text{tgt}}\leftarrow Q\_{\text{main}};

2:Replay memory (size LL), ϵ=1\epsilon=1, batch size bb, episodes MM, c<1c<1;

3:Set QRM parameters and market state S0S\_{0}, inventory q0q\_{0}.

4:for i=1i=1 to MM do

5:  Initialize the QRM simulation

6:  for t=1t=1 to NN do

7:   st←Q​R​M​(t)s\_{t}\leftarrow QRM(t)

8:   at←{random actionw.p. ​ϵarg⁡maxa⁡Qmain​(st,a|θmain)w.p. ​1−ϵa\_{t}\leftarrow\begin{cases}\text{random action}&\text{w.p. }\epsilon\\
\arg\max\limits\_{a}Q\_{\text{main}}(s\_{t},a|\theta\_{\text{main}})&\text{w.p. }1-\epsilon\end{cases}

9:   Execute ata\_{t} in QRM ⇒\Rightarrow new state sts\_{t}, observe reward rtr\_{t}

10:   Store (st,rt,at,st+1)(s\_{t},r\_{t},a\_{t},s\_{t+1}) in memory

11:   if |Memory|≥b|\text{Memory}|\geq b then

12:     Sample (stj,rtj,atj,st+1j)j=1b(s^{j}\_{t},r^{j}\_{t},a^{j}\_{t},s^{j}\_{t+1})\_{j=1}^{b}

13:     a∗,j=arg⁡maxa⁡Qmain​(st+1j,a|θmain)a^{\*,j}=\arg\max\limits\_{a}Q\_{\text{main}}(s^{j}\_{t+1},a|\theta\_{\text{main}})

14:     yj=rtj+γ​Qtgt​(st+1j,a∗,j|θtgt)y^{j}=r^{j}\_{t}+\gamma Q\_{\text{tgt}}(s^{j}\_{t+1},a^{\*,j}|\theta\_{\text{tgt}})

15:     Update θmain\theta\_{\text{main}} minimizing
ℒ=1b​∑j(yj−Qmain​(stj,atj|θmain))2\mathcal{L}=\frac{1}{b}\sum\_{j}(y^{j}-Q\_{\text{main}}(s^{j}\_{t},a^{j}\_{t}|\theta\_{\text{main}}))^{2}

16:   end if

17:   if tmodm=0t\bmod m=0 then

18:     ϵ←ϵ−c\epsilon\leftarrow\epsilon-c,  θtgt←θmain\theta\_{\text{tgt}}\leftarrow\theta\_{\text{main}}

19:   end if

20:  end for

21:end for

Two neural networks are initialized: the main network QmainQ\_{\text{main}} for action selection, and the target network QtgtQ\_{\text{tgt}} for value estimation. At each time step, the agent observes the current state and selects an action via an ϵ\epsilon-greedy policy that balances exploration and exploitation. The resulting transition and reward are stored in a replay buffer. Once the buffer reaches a sufficient size, mini-batches are sampled to update QmainQ\_{\text{main}} by minimizing the Bellman loss using target values computed from QtgtQ\_{\text{tgt}}. Every mm steps, the target network is synchronized with the main network and the exploration rate ϵ\epsilon is decayed. This iterative process allows the agent to approximate the optimal action–value function while controlling value overestimation. After training, QmainQ\_{\text{main}} serves as the agent’s policy for decision-making in the environment.

We consider a finite-horizon setting with exponentially discounted future rewards by the factor γ\gamma. More specifically, the per-step reward entering the Bellman recursion is

|  |  |  |
| --- | --- | --- |
|  | rk:=r​(sτk,aτk)=aτk​(P0−Pτk)−α​ 1{τk=T}​(X0−xT).r\_{k}:=r(s\_{\tau\_{k}},a\_{\tau\_{k}})=a\_{\tau\_{k}}\,(P\_{0}-P\_{\tau\_{k}})-\alpha\,\mathbf{1}\_{\{\tau\_{k}=T\}}\,(X\_{0}-x\_{T}). |  |

A trajectory is a sequence of states, actions, and rewards up to a stopping time τ\tau, i.e.,

|  |  |  |
| --- | --- | --- |
|  | (s0,a0,r1,s1,a1,r2,…,sτ−1,aτ−1,rτ).(s\_{0},a\_{0},r\_{1},s\_{1},a\_{1},r\_{2},...,s\_{\tau-1},a\_{\tau-1},r\_{\tau}). |  |

Given a policy π\mathcal{\pi} we can define the State-Action Value Function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qπ​(s,a)=𝔼π​[∑i=1τγi−1​ri|s0=s,a0=a],Q\_{\mathcal{\pi}}(s,a)=\mathbb{E}\_{\pi}[\sum\_{i=1}^{\tau}\gamma^{i-1}r\_{i}|s\_{0}=s,a\_{0}=a], |  | (12) |

which represents the expected return from state ss if we take action aa and then we follow the policy π\pi and can be recursively defined by the following Bellman equation [bellman1966dynamic],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qπ​(s,a)=r​(s,a)+γ​𝔼s′∼𝒫(⋅|s,a)a′∼π(⋅|s′)​[Qπ​(s′,a′)].Q\_{\pi}(s,a)=r(s,a)+\gamma\mathbb{E}\_{\begin{subarray}{c}s^{\prime}\sim\mathcal{P}(\cdot|s,a)\\ a^{\prime}\sim\pi(\cdot|s^{\prime})\end{subarray}}\big[Q\_{\pi}(s^{\prime},a^{\prime})\big]. |  | (13) |

Solving the MDP means finding the optimal policy π∗\pi^{\*} which is the policy that maximizes the objective

|  |  |  |
| --- | --- | --- |
|  | Jπ:=𝔼πs0∼μ​[∑i=1τγi−1​ri].J\_{\pi}:=\underset{s\_{0}\sim\mu}{\mathbb{E}\_{\pi}}\Big[\sum\_{i=1}^{\tau}\gamma^{i-1}r\_{i}\Big]. |  |

## 5 Experiments and results

In this section we present the results of our numerical investigations. The aim of the experiments is to study whether the DDQN agent is able to find robust optimal execution strategies without any form of knowledge of the underlying impact model. We focus here on the best-performing configuration, while additional experiments exploring alternative state and action spaces are reported in Appendix [C](https://arxiv.org/html/2511.15262v1#A3 "Appendix C Additional Experiments with Reduced State Spaces ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") for comparison.

### 5.1 Benchmark Strategies

To evaluate the DQN policy, we introduce a set of benchmark execution strategies designed to minimize Implementation Shortfall (IS) and provide a basis for performance comparison.

#### Baseline Model

We consider the Time-Weighted Average Price (TWAP) benchmark, in which the trader executes X0X\_{0} number of shares uniformly over a fixed horizon [0,T][0,T] divided into N discrete intervals. The trading rate is constant, given by
Δ​x∗=(X0N,…,X0N)\Delta x^{\*}=\left(\frac{X\_{0}}{N},\dots,\frac{X\_{0}}{N}\right),
or equivalently, the number of executed shares after time step τk\tau\_{k} is equal to xτk∗=k​X0Nx^{\*}\_{\tau\_{k}}=k\frac{X\_{0}}{N}, for k=0,…,Nk=0,\dots,N.
For a risk-neutral trader, this policy coincides with the Almgren–Chriss (A&C) solution [almgren], whose objective is to minimize the expected Implementation Shortfall (IS). Under the standard A&C assumptions of linear permanent and temporary market impact, and asset price dynamics following a Brownian motion with constant volatility, the TWAP is the optimal strategy.

#### The Percentage of Posted Volume Benchmark

We introduce a family of new benchmarks we call Percentage Of Posted Volume (POPV). More precisely, we define POPVi\text{POPV}\_{i} as the strategy that purchases a fixed fraction (50% or 100%) of the available volume at the best ask every ii time steps, while remaining inactive otherwise. The intuition behind this strategy is to exploit pauses in execution during which prices tend to mean revert (see Figure [3](https://arxiv.org/html/2511.15262v1#S3.F3 "Figure 3 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")).

### 5.2 Training Configuration

#### Algorithm parametrization

In our implementation, we employ fully connected feed-forward neural networks comprising 5 layers, each with 3030 hidden units and leaky-ReLU activation functions. We use the ADAM optimizer for optimization. The RL agent is trained on approximately 500,000500,000 episodes. The epsilon-greedy exploration policy starts at 1.01.0 and decays linearly to 0.010.01 over the first 3%3\% of training. We set the final penalty α=1.0\alpha\!=\!1.0. The parameters used to calibrate the algorithm are reported in Table [1](https://arxiv.org/html/2511.15262v1#S5.T1 "Table 1 ‣ Algorithm parametrization ‣ 5.2 Training Configuration ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"). The parameters not shown in the table change depending on the experiments and are reported below accordingly.

|  |  |  |  |
| --- | --- | --- | --- |
| DDQN Parameters |  | Model Parameters |  |
| NN layers | 5 | Time horizon (T) | 600 s |
| Hidden nodes | 30 | Time intervals (NN) | 25 |
| ADAM lr | 1e-4 | Shares to execute (X0X\_{0}) | 25 |
| Batch size (bb) | 1,024 | Final Penalty (α\alpha) | 1.0 |
| Replay memory (LL) | 1e6 | θ\theta | 0.7 |
| Target update (mm) | 1e3 | θreinit\theta^{\mathrm{reinit}} | 0.85 |
| Training episodes (MM) | 5e5 |  |  |
| Test episodes (BB) | 2e4 |  |  |
| Discount factor (γ\gamma) | 0.995 |  |  |

*Note.* The target update mm is in number of environment steps (not episodes).

Table 1: Fixed parameters used in the DDQN algorithm.

#### Feature Normalization

As the learning model relies on neural networks, all input features are normalized. Time and inventory are linearly rescaled to the interval [−1,1][-1,1], while prices and volumes are standardized using z-score normalization.

### 5.3 Simulation under Market-Calibrated Dynamics

#### Environment Setup.

In this section, we adopt the calibration proposed in [huang\_2015], with parameters θ=0.7\theta\!=\!0.7 and θreinit=0.85\theta^{\text{reinit}}\!=\!0.85, and use identical order-flow intensities. These parameters were calibrated on France Télécom (Euronext Paris) using data from January 20102010 to March 20122012, where the average bid–ask spread was approximately 1.431.43 ticks. The agent wants to buy 2525 shares and may remain inactive or purchase half or the entire best ask volume at each decision point, i.e., 𝒜={0%,50%,100%}\mathcal{A}\!=\!\{0\%,50\%,100\%\}. We simulate 600600 seconds of the QRM with a trader time step of 2525 seconds, meaning the agent can act at τ0=0\tau\_{0}\!=\!0 and subsequently every 2525 seconds. Each of these 2525 second interval is called Trader Step. This combination of parameters is designed to balance execution urgency with tactical flexibility. The number of shares to execute is large enough to require multiple market interventions, yet not so large relative to the time horizon that the optimal policy collapses into systematic buying at every step. This setup allows us to assess whether the RL agent can learn to wait for favorable market conditions and adapt its trading behavior accordingly. To compare the description in events given above with the one in seconds used here, it is useful to remark that there are on average 77 events per second .

We benchmark the RL agent against the strategies introduced in Section [5.1](https://arxiv.org/html/2511.15262v1#S5.SS1 "5.1 Benchmark Strategies ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"): TWAP, POPV1, POPV2, POPV3 and POPV4. For a fair comparison, POPV1 and POPV2 take action 50%50\% while POPV3 and POPV4 take action 100%100\%. Executing 50% of the posted volume results in a higher Implementation Shortfall (IS) due to reduced market impact compared to the more aggressive 100% setting. Moreover, it is necessary to ensure that the entire inventory is executed within the specified time horizon. This constraint justifies using only POPV1 and POPV2 for the 50%50\% action, as the slower execution of POPV3 and POPV4 would prevent full completion. Conversely, in the 100%100\% action, POPV1 and POPV2 become overly aggressive and yield worse IS, motivating the focus on POPV3 and POPV4. To assess statistical significance, we performed a one-sided Welch’s t-test to determine whether the best-performing strategy has a significantly higher average IS than the second-best. Statistical significance is indicated by asterisks: (\*) for p<0.05p<0.05, (\*\*) for p<0.01p<0.01, and (\*\*\*) for p<0.001p<0.001. To ensure comparability across methods, when the agent fails to fully execute its inventory, a final trade is executed at an additional time step and its cost is included in the IS.

#### Learning Dynamics and Q-Value Analysis.

We consider the 55-dimensional state space that has been introduced in Section [4.1](https://arxiv.org/html/2511.15262v1#S4.SS1 "4.1 Markov Decision Process Embedding ‣ 4 Optimal Execution Setting ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"). The learning curve in Figure [6](https://arxiv.org/html/2511.15262v1#S5.F6 "Figure 6 ‣ Learning Dynamics and Q-Value Analysis. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") shows steady reward improvement with convergence around 5050k episodes, while the TD loss decreases smoothly and stabilizes at low values444Note that the reward initially decreases. Under our chosen parameter configuration (in particular, the episode length and the magnitude of the admissible actions), a nearly random policy in the early ϵ\epsilon-greedy phase trades aggressively enough to execute most of the inventory before the time horizon, so the initial reward is relatively high. As ϵ\epsilon decreases and the policy becomes more structured, the agent temporarily learns to trade more cautiously, leaving a non-negligible inventory at maturity and thus suffering a larger terminal penalty, which explains the drop in reward. After this transient phase, the agent adjusts its strategy, and the reward increases and eventually converges.. This indicates that the DDQN agent learned a stable and well-optimized policy throughout the training.

![Refer to caption](x6.png)


(a) Final reward.

![Refer to caption](x7.png)


(b) Temporal difference loss.

Figure 6: Learning across 6,240,0006{,}240{,}000 environment steps (≈500,000\approx 500{,}000 episodes).

To assess the quality of the learning, we analyze the Q-values for all actions in Figures [7](https://arxiv.org/html/2511.15262v1#S5.F7 "Figure 7 ‣ Learning Dynamics and Q-Value Analysis. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"), [7](https://arxiv.org/html/2511.15262v1#S5.F7 "Figure 7 ‣ Learning Dynamics and Q-Value Analysis. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"), and [7](https://arxiv.org/html/2511.15262v1#S5.F7 "Figure 7 ‣ Learning Dynamics and Q-Value Analysis. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"). More precisely, we plot the Q-values of the trained RL agent as a function of inventory and time, when the ask price is equal to the arrival price and the bid and ask volumes are equal to their average values.

![Refer to caption](x8.png)


(a) Q-values for action 0%.

![Refer to caption](x9.png)


(b) Q-values for action 50%.

![Refer to caption](x10.png)


(c) Q-values for action 100%.

Figure 7: Q-value surfaces at P=P0P\!=\!P\_{0} with mean bid and ask volumes.

All plots reveal that, for a fixed inventory, Q-values decline over time as the remaining horizon shortens, reflecting the agent’s increasing risk of incomplete execution, which is penalized in the reward function. The lowest Q-values are observed at the terminal time TT, representing a lower bound on the execution cost. Furthermore, execution costs tend to rise with larger inventories, consistent with the greater market impact and urgency associated with executing larger positions. Moreover, execution costs tend to rise with larger inventories.

#### Performance Evaluation Against Baselines.

Table [2](https://arxiv.org/html/2511.15262v1#S5.T2 "Table 2 ‣ Performance Evaluation Against Baselines. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") reports the performance of the DDQN agent compared to benchmark strategies. Since the reward function is defined as the negative of the IS, minimizing IS is equivalent to maximizing the reward.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | POPV1 | POPV2 | POPV3 | POPV4 | TWAP | DDQN |
| Mean | -0.343 | -0.342 | -0.400 | -0.399 | -0.365 | −0.259∗⁣∗∗\mathbf{-0.259}^{\*\*\*} |
| Std | 0.378 | 0.472 | 0.388 | 0.437 | 0.652 | 0.631 |

Table 2: Reward results on 20,00020{,}000 test episodes.

It is clear that the RL agent achieves the best overall performance, with a significantly higher average reward than all benchmarks. As shown in Figure [8](https://arxiv.org/html/2511.15262v1#S5.F8 "Figure 8 ‣ Performance Evaluation Against Baselines. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"), it matches TWAP’s best-case performance while maintaining limited worst-case losses.

![Refer to caption](x11.png)


Figure 8: Reward distribution for the different tested strategies.

We checked how often the different strategies are unable to complete the purchase within the time window. We find that the DDQN agent fails to fully complete the purchase in only 0.045%0.045\% of episodes, with an average of 1.441.44 shares remaining. In comparison, POPV2 fails in 0.035%0.035\% of episodes, leaving an average of 2.142.14 shares and POPV4 fails in 0.265% of episodes, leaving an average of 2.51 shares. Thus, we can safely conclude that the considered strategies almost always complete the trading program.

#### Trading Patterns and Tactical Adaptation.

Optimal execution problems are typically addressed using a two-layer framework consisting of strategy and tactic. The strategy component determines the overall trading schedule, namely the number of shares to execute within each time interval (see Figure [9](https://arxiv.org/html/2511.15262v1#S5.F9 "Figure 9 ‣ Trading Patterns and Tactical Adaptation. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")). The tactic component, on the other hand, governs how these scheduled orders are executed within each interval (see Figures [11](https://arxiv.org/html/2511.15262v1#S5.F11 "Figure 11 ‣ Trading Patterns and Tactical Adaptation. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")). The following figures report results averaged over 20,000 test episodes.

![[Uncaptioned image]](x12.png)



Figure 9: Average execution trajectory of the different tested strategies as a function of time (measured in trader step).

Figure [9](https://arxiv.org/html/2511.15262v1#S5.F9 "Figure 9 ‣ Trading Patterns and Tactical Adaptation. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") displays the average execution trajectory of the RL agent compared with those of TWAP and POPV. The DDQN trajectory remains approximately linear for most of the trading horizon, becoming slightly concave only near completion. This pattern contrasts with the more uniform or front-loaded behavior of the rule-based benchmarks and highlights the dynamic adjustment of execution pace observed in the DDQN runs.

The figure, however, should be properly interpreted as it might convey the wrong impression that the DDQN strategy is static (as the TWAP or, more generally, the AC solution). First of all we show that the time needed to complete the execution with the DDQN strategy is highly variable. Figure [10](https://arxiv.org/html/2511.15262v1#S5.F10 "Figure 10 ‣ Trading Patterns and Tactical Adaptation. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") shows the distribution of the metaorder execution time, i.e. the number of trader steps required to complete the execution under the DDQN policy. Short episodes correspond to periods of abundant liquidity at the best ask, whereas longer episodes occur when the agent waits for more favorable trading opportunities. This broad distribution contrasts with the sharply peaked episode length profiles of benchmark strategies (see Figure [15](https://arxiv.org/html/2511.15262v1#A2.F15 "Figure 15 ‣ B.3 POPV Benchmarks ‣ Appendix B Additional Plots ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")), underscoring the adaptive nature of the learned policy. Finally, the decline in density a few steps before the time horizon indicates that the RL agent has correctly internalized the terminal penalty, completing execution by the time horizon.

![[Uncaptioned image]](x13.png)



Figure 10: Distribution of the metaorder execution time in number of trader steps.

Second, even restricting to episodes with the same metaorder execution length, we observe a large variability in the strategy. To show this, we compute for each metaorder execution time the average and variance of the gaps between consecutive executions, as shown in Figure [11](https://arxiv.org/html/2511.15262v1#S5.F11 "Figure 11 ‣ Trading Patterns and Tactical Adaptation. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") (gaps are measured in time steps: a gap of zero indicates two executions occurred at consecutive time steps).

![Refer to caption](x14.png)

![Refer to caption](x15.png)

Figure 11: Boxplots of average gaps (left) and gap variance (right) between consecutive executions per episode length for the DDQN strategy.

The broad interquartile ranges and long whiskers indicate that the RL agent does not trade at uniform intervals: even for episodes of comparable duration, the spacing between trades varies substantially. This variability becomes more pronounced for longer episodes, suggesting that the agent adjusts its trading frequency dynamically over time rather than following a fixed temporal schedule. Such heterogeneity across episodes of equal length implies that execution timing depends strongly on the prevailing market conditions. The resulting behavior is therefore tactical in nature, as the agent adapts its actions in response to short-term liquidity and price dynamics rather than adhering to a predetermined strategic rhythm.

To conclude, the DDQN trajectory exhibits a distinctly nonlinear, state-dependent profile: execution is accelerated under favorable conditions and decelerated as the horizon shortens. This pattern reflects a learned balance between immediacy and market impact, driven by the temporal structure of Q-value updates and declining continuation value near maturity. The resulting behavior demonstrates that the DDQN policy learns both strategic and tactical dimensions of execution, dynamically adapting to market states beyond the capability of fixed benchmark strategies (see [reinforcement\_nevmyvaka\_2006]).

#### Feature Importance.

To identify the main drivers of the RL agent’s decisions, we perform an input-gradient analysis and the results are shown in Table [3](https://arxiv.org/html/2511.15262v1#S5.T3 "Table 3 ‣ Feature Importance. ‣ 5.3 Simulation under Market-Calibrated Dynamics ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") (see also Appendix [A](https://arxiv.org/html/2511.15262v1#A1 "Appendix A Feature Importance ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")).

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Feature | |  | | --- | | Gradient | | (Action 0%0\%) | | |  | | --- | | Gradient | | (Action 50%50\%) | | |  | | --- | | Gradient | | (Action 100%100\%) | |
| Inventory | 0.40 | 0.37 | 0.41 |
| Ask Price | 0.34 | 0.34 | 0.35 |
| Time | 0.10 | 0.07 | 0.06 |
| Ask Volume | 0.07 | 0.07 | 0.07 |
| Bid Volume | 0.06 | 0.05 | 0.04 |

Table 3: Input-gradient for actions 0%0\%, 50%50\% and 100%100\%.

The results indicate that the ask price and inventory are the primary determinants of action selection, suggesting that the agent mainly reacts to immediate market conditions. In contrast, the influence of time is small and decreases with action magnitude. The larger the executed volume, the less significant the time feature, reinforcing that the learned policy is tactical and adaptive rather than schedule-driven. These findings are consistent with a complementary SHAP value analysis555Results are available upon request..

### 5.4 Robustness to Different Market Conditions

To test robustness, the RL policy trained at (θ,θreinit)=(0.7,0.85)(\theta,\theta^{\mathrm{reinit}})\!=\!(0.7,0.85) is evaluated across QRM simulations with θ,θreinit∈[0.5,1.0]\theta,\theta^{\mathrm{reinit}}\in[0.5,1.0]. Figure [12](https://arxiv.org/html/2511.15262v1#S5.F12 "Figure 12 ‣ 5.4 Robustness to Different Market Conditions ‣ 5 Experiments and results ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") shows that it consistently exceeds the best benchmark, achieving up to 27% higher performance. This demonstrates that the learned policy generalizes well to different market regimes and can be relied upon to maintain strong performance under varying conditions.

![Refer to caption](x16.png)


Figure 12: Heatmap of the relative difference between the average reward of the RL agent vs the best benchmark (TWAP in all the cases), averaged over 10,000 simulations.

## 6 Conclusion

In this work, we proposed a reinforcement-learning framework for optimal execution within the Queue-Reactive Model (QRM). By leveraging the ergodicity and microstructural features of the QRM, including its state-dependent order-flow intensities, its stochastic queue dynamics, and its endogenous liquidity replenishment mechanisms, we produced a simulation environment that captures both direct liquidity consumption and indirect order-flow responses. Training a Double Deep Q-Network (DDQN) in this setting shows that the RL agent learns execution strategies that are tactically adaptive and strategically robust. Across all configurations, the agent consistently outperforms standard benchmarks such as TWAP, adjusting to local liquidity and short-term price pressure rather than following a fixed schedule. Analyses of execution timing, Q-values, and feature importance confirm that the policy internalizes subtle microstructural patterns, including nonlinear impact and volume-imbalance effects.

Possible extensions include adding limit-order placement and queue-management decisions to balance passive and aggressive execution. Extending the methodology to multi-asset execution problems would introduce cross-impact effects and portfolio-level constraints, broadening the scope of the approach. Another potential direction is to integrate predictive alpha signals into the state space so that the agent jointly optimizes execution and directional positioning, thereby connecting optimal trading and optimal execution.

## Acknowledgements

Yadh Hafsi acknowledges the support of the Chaire Risque Financiers, Société Générale, at École Polytechnique.

## Appendix A Feature Importance

We draw NN transitions (s,a)(s,a) from the replay buffer and compute the corresponding Q-values Q​(s,a)Q(s,a). For each input feature sis\_{i}, we evaluate the gradient
gi=∂Q​(s,a)∂si,g\_{i}=\frac{\partial Q(s,a)}{\partial s\_{i}},
take its absolute value, and average across all NN sampled transitions. The resulting per-feature scores quantify how variations in each state variable influence the Q-value. This gradient-based method requires only a single backward pass per state–action pair.

## Appendix B Additional Plots

### B.1 Invariant Distribution

![Refer to caption](x17.png)


Figure 13: Invariant distribution of Q±1,Q±2,Q±3Q\_{\pm 1},Q\_{\pm 2},Q\_{\pm 3}, taken from [huang\_2015].

### B.2 Market Impact

We provide additional details on the bid and ask refill scenarios mentioned in Section [3.4](https://arxiv.org/html/2511.15262v1#S3.SS4 "3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") to clarify the mechanism behind the price mean reversion observed after sending a market order that consumes the entire best ask. In a bid-refill scenario (see Figure [14](https://arxiv.org/html/2511.15262v1#A2.F14 "Figure 14 ‣ B.2 Market Impact ‣ Appendix B Additional Plots ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")), price initially increases because the most probable subsequent event after buying the best ask is a limit order placement at the best bid, which raises the mid-price from 100.010100.010 to 100.015100.015. Logically, the same phenomenon happens when θ=0\theta\!=\!0 and we observe that the trajectories coincide over short horizons. However, simulations indicate that this new liquidity typically vanishes rapidly, causing the mid-price to return to its previous level. When the reference price then decreases to 100.005100.005 (with probability θ\theta) and volumes are redrawn from the invariant distribution (with probability θ​θreinit\theta\theta^{\mathrm{reinit}}), the average mid-price settles half a tick below its initial value. This mechanism occurs frequently enough to produce systematic mean reversion, driven by the interaction between the calibrated intensities and (θ,θreinit)(\theta,\theta^{\mathrm{reinit}}). In contrast, when θ=0\theta\!=\!0, the mid-price increases by half a tick, as expected.

![Refer to caption](x18.png)


(a) Bid refill following a buy order with (θ,θreinit)=(0.7,0.85)(\theta,\theta^{\mathrm{reinit}})\!=\!(0.7,0.85).

![Refer to caption](x19.png)


(b) Ask refill following a buy order with (θ,θreinit)=(0.7,0.85)(\theta,\theta^{\mathrm{reinit}})\!=\!(0.7,0.85).

Figure 14: Evolution of 𝔼​[pk]\mathbb{E}[p\_{k}] after buying the best ask at k=0k\!=\!0, averaged over 1,000,0001{,}000{,}000 simulations. The black dotted line denotes the reference case θ=0\theta\!=\!0. The mid-price before the trade is 100.005100.005.

In the ask-refill scenario (see Figure [14](https://arxiv.org/html/2511.15262v1#A2.F14 "Figure 14 ‣ B.2 Market Impact ‣ Appendix B Additional Plots ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")), the opposite sequence occurs. These two price response patterns are consistently observed across all tested parameter combinations. However, the aggregate results (see Figure [5](https://arxiv.org/html/2511.15262v1#S3.F5 "Figure 5 ‣ 3.4 Market impact ‣ 3 The Queue-Reactive Model ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution")) vary according to the relative weighting of each of these bid-ask refill scenarios, determined by the probabilities (θ,θreinit)(\theta,\theta^{\mathrm{reinit}}).

### B.3 POPV Benchmarks

![Refer to caption](x20.png)


(a) POPV1.

![Refer to caption](x21.png)


(b) POPV2.

![Refer to caption](x22.png)


(c) POPV3.

![Refer to caption](x23.png)


(d) POPV4.

Figure 15: Episode length distribution of the POPV benchmarks.

## Appendix C Additional Experiments with Reduced State Spaces

We evaluate multiple state-space configurations to examine how the dimensionality of the input representation influences the agent’s performance. These configurations help isolate the contribution of individual market features such as best ask volume and bid-ask imbalance. The following results correspond to the case of a binary action space, 𝒜={0%,100%}\mathcal{A}\!=\!\{0\%,100\%\}. For feature importance, we report only the input-gradient analysis, as similar patterns were observed with the SHAP-value analysis. The following figures report results averaged over 20,000 test episodes.

### C.1 Reduced Model: 3D State and Binary Action Space

In this first configuration, we consider a minimal 3-dimensional state space that includes the remaining inventory, the time and the best ask price. We report the results of the trained RL agent and of the benchmarks in Table [4](https://arxiv.org/html/2511.15262v1#A3.T4 "Table 4 ‣ C.1 Reduced Model: 3D State and Binary Action Space ‣ Appendix C Additional Experiments with Reduced State Spaces ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") and show the reward distribution in Fig. [18](https://arxiv.org/html/2511.15262v1#A3.F18 "Figure 18 ‣ C.1 Reduced Model: 3D State and Binary Action Space ‣ Appendix C Additional Experiments with Reduced State Spaces ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"). The RL agent has the second best average reward after TWAP. We observe that TWAP exhibits a much larger variance in rewards compared to DDQN. This stems from the fact that TWAP is entirely agnostic to price and order book dynamics: it performs poorly when prices trend upward and favorably when they decline, resulting in high variability in realized rewards. Thus, the performance of the RL agent is not satisfactory: we would expect it to perform better than TWAP as it is better informed.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | POPV1 | POPV2 | POPV3 | POPV4 | TWAP | DDQN |
| Mean | -0.413 | -0.408 | -0.400 | -0.399 | −0.365∗∗\mathbf{-0.365}^{\*\*} | -0.386 |
| Std | 0.279 | 0.342 | 0.388 | 0.437 | 0.652 | 0.473 |

Table 4: Reward results. POPV1, POPV2, POPV3, TWAP and DDQN fully execute on all episodes. POPV4 has 2.51 shares remaining in average on 53 episodes (0.265%).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Feature | |  | | --- | | Gradient | | (Action 0%0\%) | | |  | | --- | | Gradient | | (Action 100%100\%) | |
| Inventory | 0.45 | 0.42 |
| Ask Price | 0.25 | 0.26 |
| Time | 0.19 | 0.10 |

Table 5: Input-gradient for actions 0%0\% and 100%100\%.



![Refer to caption](x24.png)


Figure 16: Reward distribution.

![Refer to caption](x25.png)


Figure 17: Average inventory trajectory.

![Refer to caption](x26.png)


Figure 18: Episode length distribution.

### C.2 Reduced Model: 4D State and Binary Action Space

In this second configuration, we consider a 4-dimensional state space that includes the remaining inventory, the time, the best ask price and best ask volume. The rationale for including the best ask volume is that it provides the agent with information about the number of shares that would be executed if it decided to consume the entire best ask volume. This feature is particularly relevant because the distribution of best ask volumes is highly right-skewed and exhibits a heavy tail. Thus, the agent can take advantage of unusually large volumes to execute substantial trades in a single action. The results are reported in Table [6](https://arxiv.org/html/2511.15262v1#A3.T6 "Table 6 ‣ C.2 Reduced Model: 4D State and Binary Action Space ‣ Appendix C Additional Experiments with Reduced State Spaces ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"): the RL agent outperforms all the benchmarks in terms of average IS. Figure [21](https://arxiv.org/html/2511.15262v1#A3.F21 "Figure 21 ‣ C.2 Reduced Model: 4D State and Binary Action Space ‣ Appendix C Additional Experiments with Reduced State Spaces ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution") shows that the episodes are longer compared to those of the 3-dimensional state-space agent, indicating that the agent has learned to act more patiently in order to exploit more favorable future prices.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | POPV1 | POPV2 | POPV3 | POPV4 | TWAP | DDQN |
| Mean | -0.413 | -0.408 | -0.400 | -0.399 | -0.365 | −0.325∗⁣∗∗\mathbf{-0.325}^{\*\*\*} |
| Std | 0.279 | 0.342 | 0.388 | 0.437 | 0.652 | 0.594 |

Table 6: Reward results. POPV1, POPV2, POPV3 and TWAP fully execute on all episodes. POPV4 has 2.51 shares remaining in average on 53 episodes (0.265%). DDQN has 6.77 shares remaining in average on 31 episodes (0.155%).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Feature | |  | | --- | | Gradient | | (Action 0%0\%) | | |  | | --- | | Gradient | | (Action 100%100\%) | |
| Inventory | 0.33 | 0.31 |
| Ask Price | 0.25 | 0.26 |
| Time | 0.12 | 0.07 |
| Ask Volume | 0.06 | 0.06 |

Table 7: Input-gradient for actions 0%0\% and 100%100\%.



![Refer to caption](x27.png)


Figure 19: Reward distribution.

![Refer to caption](x28.png)


Figure 20: Average inventory trajectory.

![Refer to caption](x29.png)


Figure 21: Episode length distribution.

### C.3 Reduced Model: 5D State and Binary Action Space

In this third configuration, we consider a 5-dimensional state space that includes the remaining inventory, the time, the best ask price and the best bid-ask volume. The rationale behind adding the best bid volume is that it informs the agent of the volume imbalance, a well-established short-term predictor of price movements in market microstructure. The results are reported in Table [8](https://arxiv.org/html/2511.15262v1#A3.T8 "Table 8 ‣ C.3 Reduced Model: 5D State and Binary Action Space ‣ Appendix C Additional Experiments with Reduced State Spaces ‣ Reinforcement Learning in Queue-Reactive Models: Application to Optimal Execution"): the RL agent outperforms all the benchmarks.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | POPV1 | POPV2 | POPV3 | POPV4 | TWAP | DDQN |
| Mean | -0.413 | -0.408 | -0.400 | -0.399 | -0.365 | −0.290∗⁣∗∗\mathbf{-0.290}^{\*\*\*} |
| Std | 0.279 | 0.342 | 0.388 | 0.437 | 0.652 | 0.541 |

Table 8: Reward results. POPV1, POPV2, POPV3 and TWAP fully execute on all episodes. POPV4 has 2.51 shares remaining in average on 53 episodes (0.265%). DDQN has 2.33 shares remaining in average on 3 episodes (0.015%).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Feature | |  | | --- | | Gradient | | (Action 0%0\%) | | |  | | --- | | Gradient | | (Action 100%100\%) | |
| Inventory | 0.44 | 0.40 |
| Ask Price | 0.29 | 0.30 |
| Time | 0.12 | 0.06 |
| Ask Volume | 0.07 | 0.07 |
| Bid Volume | 0.06 | 0.03 |

Table 9: Input-gradient for actions 0%0\% and 100%100\%.



![Refer to caption](x30.png)


Figure 22: Reward distribution.

![Refer to caption](x31.png)


Figure 23: Average inventory trajectory.

![Refer to caption](x32.png)


Figure 24: Episode length distribution.



![Refer to caption](x33.png)

![Refer to caption](x34.png)

Figure 25: Boxplots of average gaps (left) and gap variance (right) between consecutive executions per episode length.



![Refer to caption](x35.png)


(a) Q-values for action 0%.

![Refer to caption](x36.png)


(b) Q-values for action 100%.

Figure 26: Q-value surfaces when the price equals P0P\_{0} and the best bid/ask volumes are equal to their means.

### C.4 Comparing Models with Different State and Action Spaces

We summarize and compare the RL performances across all combinations of state and action spaces explored. For the 2-dimensional action space 𝒜={0%,100%}\mathcal{A}=\{0\%,100\%\}, the algorithms DDQN1, DDQN2, and DDQN3 correspond to state spaces of dimensions 3, 4, and 5, respectively. The model denoted DDQN4 refers to the best-performing agent trained with a 3-dimensional action space 𝒜={0%,50%,100%}\mathcal{A}=\{0\%,50\%,100\%\} and a 5-dimensional state representation. Our study shows that the RL agent’s performance gradually increases by extending the state and action space.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | TWAP | DDQN1 | DDQN2 | DDQN3 | DDQN4 |
| Mean | -0.365 | -0.386 | -0.325 | -0.290 | −0.259∗⁣∗∗\mathbf{-0.259}^{\*\*\*} |
| Std | 0.652 | 0.473 | 0.594 | 0.541 | 0.631 |

Table 10: Reward results for different state and action space dimensions.



![Refer to caption](x37.png)


(a) Histogram.

![Refer to caption](x38.png)

(b) Boxplot showing the mean.

Figure 27: Reward distribution.