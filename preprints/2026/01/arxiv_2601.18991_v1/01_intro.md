---
authors:
- Hardhik Mohanty
- Bhaskar Krishnamachari
doc_id: arxiv:2601.18991v1
family_id: arxiv:2601.18991
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market
  Dynamics
url_abs: http://arxiv.org/abs/2601.18991v1
url_html: https://arxiv.org/html/2601.18991v1
venue: arXiv q-fin
version: 1
year: 2026
---


Hardhik Mohanty
  
Bhaskar Krishnamachari

###### Abstract

USDC and USDT are the dominant stablecoins pegged to $1 with a total market capitalization of over $300B and rising. Stablecoins make dollar value globally accessible with secure transfer and settlement. Yet in practice, these stablecoins experience periods of stress and de-pegging from their $1 target, posing significant systemic risks. The behavior of market participants during these stress events and the collective actions that either restore or break the peg are not well understood.
This paper addresses the question: who restores the peg? We develop a dynamic, agent-based mean-field game framework for fiat-collateralized stablecoins, in which a large population of arbitrageurs and retail traders strategically interacts across explicit primary (mint/redeem) and secondary (exchange) markets during a de-peg episode. The key advantage of this equilibrium formulation is that it endogenously maps market frictions into a market-clearing price path and implied net order flows, allowing us to attribute peg-reverting pressure by channel and to stress-test when a given mechanism becomes insufficient for recovery.
Using three historical de-peg events, we show that the calibrated equilibrium reproduces observed recovery half-lives and yields an order flow decomposition in which system-wide stress is predominantly stabilized by primary-market arbitrage, whereas episodes with impaired primary redemption require a joint recovery via both primary and secondary markets. Finally, a quantitative sensitivity analysis of primary-rail frictions identifies a non-linear breakdown threshold. Beyond this point, secondary-market liquidity acts mainly as a second-order amplifier around this primary-market bottleneck.

## I Introduction

Fiat-collateralized stablecoins such as USDC and USDT have become a fundamental component of the digital asset ecosystem. With the combined market capitalization exceeding $300 billion as of year 2025, these assets serve as a critical bridge between the traditional financial system and the decentralized finance (DeFi) sector [[15](https://arxiv.org/html/2601.18991v1#bib.bib1 "Taming wildcat stablecoins")]. They function as the primary unit of account, a medium of exchange for 24/7 global settlement, and a core form of collateral for decentralized lending and derivatives protocols. The perceived stability of these assets underpins the valuation and liquidity of thousands of other digital assets. However, this reliance introduces significant risk as these stablecoins are not immune to periods of market stress and can “de-peg” from their $1 target, as evidenced by the acute de-pegging of USDC in March 2023 [[1](https://arxiv.org/html/2601.18991v1#bib.bib2 "Crypto lending and stablecoin de-pegging: key risks and challenges")]. The mechanism that governs these de-peg and re-peg dynamics, particularly the collective behavior of market participants, is not well understood. Therefore, this paper attempts to address the critical question — “who restores the peg?”

The stability of fiat-collateralized stablecoins is maintained by two independent mechanisms as demonstrated in Figure [1](https://arxiv.org/html/2601.18991v1#S1.F1 "Figure 1 ‣ I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"): a primary market where authorized participants (arbitrageurs) can mint or redeem the stablecoin directly with the treasury at the $1 peg, and a diverse ecosystem of secondary markets (e.g., centralized and decentralized exchanges) where the asset is freely traded [[18](https://arxiv.org/html/2601.18991v1#bib.bib3 "What keeps stablecoins stable?")]. The efficacy of this pegging mechanism is critically dependent on the design of the primary arbitrage channel characterized by accessibility, cost, and processing speed [[22](https://arxiv.org/html/2601.18991v1#bib.bib4 "What drives the (in)stability of a stablecoin?")]. These markets are populated by a heterogeneous collection of multiple agents, ranging from arbitrageurs to retail traders.
While arbitrage is a well-known economic mechanism for restoration, the tipping point at which this mechanism fails due to congestion or liquidity drying up remains unknown. It remains unclear how collective actions aggregate to create a specific breakdown point at which the peg collapses, despite rational arbitrage incentives. Our model attempts to quantify this non-linear threshold.

![Refer to caption](x1.png)


Figure 1: Market structure for fiat-collateralized stablecoins. The primary market involves the treasury and arbitrageurs for 1:1 minting and redeeming, while the secondary market includes exchanges and retail traders for buying and selling.

Rigorously modeling this system is challenging because it is a high-dimensional multi-population game with rational agents interacting dynamically in a non-stationary environment [[19](https://arxiv.org/html/2601.18991v1#bib.bib29 "Solving continuous mean field games: deep reinforcement learning for non-stationary dynamics")]. Standard multi-agent reinforcement learning (MARL) or agent-based models (ABM) become computationally intractable as the number of agents (NN) grows, making it difficult to solve for true Nash Equilibria. The Mean-Field Game (MFG) approach overcomes this by approximating the population as a continuum (N→∞N\to\infty), reducing the complexity to a tractable fixed-point problem [[9](https://arxiv.org/html/2601.18991v1#bib.bib22 "A policy iteration method for mean field games")].
We adopt an MFG formulation to provide a dynamic, agent-based representation of stablecoin de-peg episodes. This approach offers critical insights that are inaccessible through existing methodologies [[17](https://arxiv.org/html/2601.18991v1#bib.bib5 "Learning in mean field games: a survey"), [5](https://arxiv.org/html/2601.18991v1#bib.bib6 "Linear-quadratic mean field games")].

While prior works such as [[18](https://arxiv.org/html/2601.18991v1#bib.bib3 "What keeps stablecoins stable?")] and [[27](https://arxiv.org/html/2601.18991v1#bib.bib8 "Primary and secondary markets for stablecoins")] infer reversion dynamics from empirical data, our framework derives these market flows endogenously from the strategic optimization of heterogeneous agents interacting across primary and secondary markets. This endogenous derivation allows us to identify the specific non-linear thresholds where primary market frictions overwhelm arbitrage capacity, a transition that reduced-form models cannot capture. Unlike the static equilibrium analysis in [[22](https://arxiv.org/html/2601.18991v1#bib.bib4 "What drives the (in)stability of a stablecoin?")], our dynamic formulation characterizes the entire temporal profile of peg restoration, including the calculation of recovery half-lives. Furthermore, in contrast to heuristic simulators like DAISIM [[6](https://arxiv.org/html/2601.18991v1#bib.bib20 "Daisim: a computational simulator for the makerdao stablecoin")] and [[10](https://arxiv.org/html/2601.18991v1#bib.bib21 "Algorithmic stablecoins: a simulator for the dual-token model in normal and panic scenarios")] which rely on pre-defined behavior rules, our model computes a formal equilibrium with quantified exploitability. Consequently, we can evaluate peg stability through the lens of ε\varepsilon-Nash robustness, providing a rigorous metric for how rational agents respond to systemic stress across stablecoin markets.

The contributions of this paper are threefold:

* •

  First, we contribute to the literature on digital asset stability by developing a dynamic mean-field game framework that serves as a tractable agent-based model for stablecoin de-peg episodes. To our knowledge, this is the first study to analyze these events through an equilibrium-based representation of dynamic strategic interactions between arbitrageurs and retail traders across both primary and secondary markets.
* •

  Second, we provide a rigorous assessment of the model by calibrating it to three major historical events, including the USDT and USDC de-pegs of 2022 and 2023. We demonstrate that the framework accurately replicates observed price trajectories and recovery half-lives in ways that standard reduced-form regressions fail to achieve.
* •

  Finally, our findings should be of interest to stablecoin issuers and regulators as we identify a non-linear stability threshold for primary-market access. Our analysis reveals that peg restoration is highly sensitive to specific frictions in redemption rails and that secondary market liquidity acts only as a secondary amplifier once these primary bottlenecks are crossed.

The rest of the paper is structured as follows: Section [II](https://arxiv.org/html/2601.18991v1#S2 "II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") reviews the related literature. Section [III](https://arxiv.org/html/2601.18991v1#S3 "III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") presents the dynamic, agent-based mean-field game framework and the market dynamics. Section [IV](https://arxiv.org/html/2601.18991v1#S4 "IV Simulation Parameters ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") describes the baseline calibration and data extraction. Section [V](https://arxiv.org/html/2601.18991v1#S5 "V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") reports the experimental results. Section [VI](https://arxiv.org/html/2601.18991v1#S6 "VI Conclusions and Future Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") concludes and outlines directions for future work.

![Refer to caption](x2.png)


Figure 2: Overview of the Mean-Field Game (MFG) framework used to model agent dynamics for stablecoin markets.

## II Related Work

### II-A Stablecoin Peg Arbitrage and Restoration Mechanics

An increasing body of work studies how stablecoins maintain their pegs and what happens when those pegs come under stress. In a historical and regulatory perspective, Gorton et al. [[15](https://arxiv.org/html/2601.18991v1#bib.bib1 "Taming wildcat stablecoins")] interpret fiat-backed stablecoins as a new form of private bank money and argue that, without bank-style regulation and sufficiently safe collateral, they are vulnerable to runs and failure to trade at par. Lyons et al. [[18](https://arxiv.org/html/2601.18991v1#bib.bib3 "What keeps stablecoins stable?")] use detailed data on treasury trades and order books for Tether to show that reforms which broadened access to primary-market arbitrage, such as migration to Ethereum and decentralized issuance, reduced typical peg deviations by roughly half and that premiums and discounts are shaped by safe-haven demand and collateral constraints. Recent empirical work also begins to quantify which design features and market environments are associated with more frequent or severe de-pegs, including the interaction with crypto lending and leverage [[20](https://arxiv.org/html/2601.18991v1#bib.bib11 "Trading and arbitrage in cryptocurrency markets"), [3](https://arxiv.org/html/2601.18991v1#bib.bib26 "Liquidity shocks, token returns and market capitalization in decentralized finance (defi) markets")]. However, these empirical contributions primarily estimate reduced-form price dynamics and aggregate arbitrage flows and do not explicitly model the strategic interaction of a large population of retail traders and arbitrageurs across primary and secondary venues.

### II-B Market Microstructure of Digital Assets

Our framework explicitly models market frictions, which are now central in the study of digital asset markets. Seminal work by Makarov et al. [[20](https://arxiv.org/html/2601.18991v1#bib.bib11 "Trading and arbitrage in cryptocurrency markets")] documents large and persistent cross-exchange price deviations and shows that a common component in order flow explains much of the common component in returns across bitcoin exchanges, highlighting both segmentation and non-trivial execution costs. Stablecoin-specific work by Pernice et al. [[21](https://arxiv.org/html/2601.18991v1#bib.bib12 "On stablecoin price processes and arbitrage")] develops a continuous-time model of stablecoin prices and arbitrage bounds under collateral and funding frictions, formalizing how redemption costs and balance sheet constraints shape the no-arbitrage region for fiat-backed coins.

Beyond these early contributions, a growing empirical microstructure literature studies order flow, liquidity and price impact in crypto markets, often with an explicit focus on stablecoin pairs [[4](https://arxiv.org/html/2601.18991v1#bib.bib23 "Market impact and efficiency in cryptoassets markets"), [14](https://arxiv.org/html/2601.18991v1#bib.bib24 "Exchange market liquidity prediction with the k-nearest neighbor approach: crypto vs. fiat currencies"), [13](https://arxiv.org/html/2601.18991v1#bib.bib25 "Decentralised finance and automated market making: execution and speculation")].
However, these studies generally treat trader behaviour as reduced-form and do not explicitly solve for the optimal, forward-looking policies of a large population of strategic agents, such as retail traders and arbitrageurs, whose collective actions generate the observed order flow and price dynamics.

### II-C Game-Theoretic Models for Stablecoin Markets

Game-theoretic frameworks have been increasingly used to understand the fundamental drivers of financial system stability. A prominent example in stablecoin markets is the work by Potter et al. [[22](https://arxiv.org/html/2601.18991v1#bib.bib4 "What drives the (in)stability of a stablecoin?")], which provides a game-theoretical model to identify why stablecoins de-peg. Their model analyzes different price equilibria that emerge based on a coin’s underlying architecture and pegging mechanism. This provides a formal basis for comparing the relative price stability of stablecoin designs.

While prior work studies stablecoin architectures through static design and equilibrium comparisons, our approach instead builds a fully dynamic, agent-based MFG that models how a large population of interacting traders and arbitrageurs respond during a de-peg episode. Our methodological approach draws from MFG theory, introduced by Lasry et al. [[16](https://arxiv.org/html/2601.18991v1#bib.bib13 "Mean field games")], with the specific Linear-Quadratic (LQ) framework being formalized in work such as [[5](https://arxiv.org/html/2601.18991v1#bib.bib6 "Linear-quadratic mean field games"), [26](https://arxiv.org/html/2601.18991v1#bib.bib30 "Reinforcement learning in non-stationary discrete-time linear-quadratic mean-field games")].

This framework is particularly suited for analyzing agent dynamics in stablecoin markets and has been successfully applied to models of bank runs [[12](https://arxiv.org/html/2601.18991v1#bib.bib14 "Mean field games of timing and models for bank runs")], which serve as a strong theoretical analogue to a stablecoin de-peg (a run on reserves). Furthermore, MFGs have been used to model market microstructure, particularly the impact of crowd trading on optimal execution [[11](https://arxiv.org/html/2601.18991v1#bib.bib15 "Mean field game of controls and an application to trade crowding")]. More recently, there has been an increasing interest in MFG with the rise of LLM and RL-based agents [[17](https://arxiv.org/html/2601.18991v1#bib.bib5 "Learning in mean field games: a survey")].
To the best of our knowledge, there is currently no dynamic, agent-based MFG model calibrated to observed stablecoin de-peg episodes that explicitly captures the dynamic interaction of multiple strategic agents across primary and secondary markets.

## III Methodology

### III-A Dynamic Mean-Field Game Framework

A dynamic MFG models a system with a continuum of rational, non-atomic agents who interact via a “mean field” [[17](https://arxiv.org/html/2601.18991v1#bib.bib5 "Learning in mean field games: a survey")]. In our model, as illustrated in Figure [2](https://arxiv.org/html/2601.18991v1#S1.F2 "Figure 2 ‣ I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"), this mean field represents the aggregate market state. In our setting, the mean-field state at time tt is μt=(mt,Lt,ϕt,ψt)\mu\_{t}=(m\_{t},L\_{t},\phi\_{t},\psi\_{t}), where mtm\_{t} is the stablecoin mispricing relative to the one-dollar peg, LtL\_{t} is the vector of primary backlogs across chains, ϕt\phi\_{t} is the vector of aggregate secondary flows across venues, and ψt\psi\_{t} is the vector of aggregate primary flows. Different components of μt\mu\_{t} enter different parts of the agent cost functions: mtm\_{t} drives inventory and pricing costs, LtL\_{t} and ψt\psi\_{t} determine primary access costs, and ϕt\phi\_{t} enters the secondary-market congestion term. The net order flow, in turn, determines market-wide variables like price slippage and execution costs.

### III-B Economic Environment and Agent Types

Our model consists of two main components: a multi-population agent system and a multi-venue market microstructure. The market is populated by a continuum of agents, divided into two classes – (1) Retail Traders: A fraction πR\pi\_{R} of the population, characterized by higher execution frictions such as slippage costs κR\kappa\_{R} and inventory aversion ηR\eta\_{R}. They are assumed to trade exclusively in secondary markets. Their state is their inventory qR,tq\_{R,t} and their control variable is their vector of secondary market flows aR,t∈ℝSa\_{R,t}\in\mathbb{R}^{S}. (2) Arbitrageurs: A fraction πA\pi\_{A} of the population, representing sophisticated actors with lower secondary market frictions κA\kappa\_{A} and inventory aversion ηA\eta\_{A}. They have access to both primary and secondary markets. Their state is their inventory qA,tq\_{A,t} and their control variables are secondary market flows aA,t∈ℝSa\_{A,t}\in\mathbb{R}^{S} and primary redemption flows rt∈ℝCr\_{t}\in\mathbb{R}^{C}.

Both agent types solve a discounted LQ optimization problem to minimize a cost functional that combines mispricing exposure, inventory risk, execution costs, and congestion costs. The first term in each objective corresponds to the negative of trading profit from exploiting deviations from the peg, while the remaining terms are cost penalties.
Quadratic execution costs of this type are standard in optimal execution and mean-field trading models, where linear temporary price impact in trade size implies a strictly convex cost term [[2](https://arxiv.org/html/2601.18991v1#bib.bib32 "Optimal execution with nonlinear impact functions and trading-enhanced risk"), [13](https://arxiv.org/html/2601.18991v1#bib.bib25 "Decentralised finance and automated market making: execution and speculation")].
An agent of type i∈{R,A}i\in\{R,A\} chooses control policies (flows) to minimize an expected sum of discounted future costs with discount factor γ∈(0,1)\gamma\in(0,1).
In particular, retail traders solve:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min{aR,t}\displaystyle\min\_{\{a\_{R,t}\}} | 𝔼[∑t=0∞γt(mt​∑s=1SaR,s,t⏟Trading PnL+12​ηR​qR,t2⏟Inventory Cost\displaystyle\mathbb{E}\Bigg[\sum\_{t=0}^{\infty}\gamma^{t}\Big(\underbrace{m\_{t}\sum\_{s=1}^{S}a\_{R,s,t}}\_{\text{Trading PnL}}+\underbrace{\frac{1}{2}\eta\_{R}q\_{R,t}^{2}}\_{\text{Inventory Cost}} |  | (1) |
|  |  | +12​∑s=1SκR,s​aR,s,t2⏟Execution Cost+C​(aR,t,a¯R,t)⏟Congestion Cost)]\displaystyle\qquad\qquad+\underbrace{\frac{1}{2}\sum\_{s=1}^{S}\kappa\_{R,s}a\_{R,s,t}^{2}}\_{\text{Execution Cost}}+\underbrace{C(a\_{R,t},\bar{a}\_{R,t})}\_{\text{Congestion Cost}}\Big)\Bigg] |  |
|  | s.t. | qR,t+1=qR,t+∑s=1SaR,s,t.\displaystyle q\_{R,t+1}=q\_{R,t}+\sum\_{s=1}^{S}a\_{R,s,t}\,. |  |

Here C​(aR,t,a¯R,t)=ξR​aR,t⊤​ϕtC(a\_{R,t},\bar{a}\_{R,t})=\xi\_{R}\,a\_{R,t}^{\top}\phi\_{t} denotes a mean-field congestion cost in secondary markets, which we implement using the aggregate secondary flow ϕt\phi\_{t}, the secondary-flow component of the mean-field state μt\mu\_{t}.

Arbitrageurs solve an analogous control problem that is augmented to account for both secondary and primary flows. Let τc​(Lt)\tau\_{c}(L\_{t}) denote the effective linear cost of routing one unit through primary chain cc, which depends on the backlog state LtL\_{t} and the settlement parameters of the protocol. Then, the arbitrageur control problem is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min{aA,t,rt}\displaystyle\min\_{\{a\_{A,t},r\_{t}\}} | 𝔼[∑t=0∞γt(mt​∑s=1SaA,s,t⏟Secondary Trading PnL+∑c=1Cτc​(Lt)​rc,t⏟Primary Routing Cost+\displaystyle\mathbb{E}\Bigg[\sum\_{t=0}^{\infty}\gamma^{t}\Big(\underbrace{m\_{t}\sum\_{s=1}^{S}a\_{A,s,t}}\_{\text{Secondary Trading PnL}}+\underbrace{\sum\_{c=1}^{C}\tau\_{c}(L\_{t})\,r\_{c,t}}\_{\text{Primary Routing Cost}}+ |  | (2) |
|  |  | ⋯⏟Secondary Costs+12​∑c=1CκP,c​rc,t2⏟Primary Execution Cost+CA​(aA,t,a¯A,t)⏟Congestion Cost)]\displaystyle\underbrace{\cdots}\_{\text{Secondary Costs}}+\underbrace{\frac{1}{2}\sum\_{c=1}^{C}\kappa\_{P,c}r\_{c,t}^{2}}\_{\text{Primary Execution Cost}}+\underbrace{C\_{A}(a\_{A,t},\bar{a}\_{A,t})}\_{\text{Congestion Cost}}\Big)\Bigg] |  |
|  | s.t. | qA,t+1=qA,t+∑s=1SaA,s,t+∑c=1Crc,t.\displaystyle q\_{A,t+1}=q\_{A,t}+\sum\_{s=1}^{S}a\_{A,s,t}+\sum\_{c=1}^{C}r\_{c,t}\,. |  |

The term CA​(aA,t,a¯A,t)=ξA​aA,t⊤​ϕtC\_{A}(a\_{A,t},\bar{a}\_{A,t})=\xi\_{A}\,a\_{A,t}^{\top}\phi\_{t} denotes the congestion cost for arbitrageurs, parameterized by a coefficient ξA\xi\_{A}. In the special case ξR=ξA=0\xi\_{R}=\xi\_{A}=0, the congestion terms vanish and both ([1](https://arxiv.org/html/2601.18991v1#S3.E1 "In III-B Economic Environment and Agent Types ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics")) and ([2](https://arxiv.org/html/2601.18991v1#S3.E2 "In III-B Economic Environment and Agent Types ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics")) reduce to standard discounted LQ control problems with linear state dynamics.

### III-C Stablecoin Market Dynamics

The market environment and mean fields (mispricing, backlog, aggregate primary and secondary flows) evolve based on the aggregate actions of all agents. The secondary and primary markets consist of a set of SS distinct venues (e.g., CEX, DEX) with heterogeneous price impact parameters λs\lambda\_{s} and a set of CC mint/redeem channels (different blockchains) that allow arbitrageurs to mint or redeem stablecoins at the $1 peg, subject to costs κP\kappa\_{P}. The secondary market price deviation (mtm\_{t}) evolves based on the net order flow from all agents and an exogenous shock ϵt\epsilon\_{t} as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | mt+1=\displaystyle m\_{t+1}={} | mt+∑s=1Sλs​(πR​aR,s,t+πA​aA,s,t)\displaystyle m\_{t}+\sum\_{s=1}^{S}\lambda\_{s}\bigl(\pi\_{R}a\_{R,s,t}+\pi\_{A}a\_{A,s,t}\bigr) |  | (3) |
|  |  | +∑c=1Cγc​(πA​rc,t)+ϵt.\displaystyle{}+\sum\_{c=1}^{C}\gamma\_{c}\bigl(\pi\_{A}r\_{c,t}\bigr)+\epsilon\_{t}. |  |

where γc\gamma\_{c} is the parameter coupling primary flows to the secondary market price. The backlog for each channel cc is represented by Lc,tL\_{c,t}. It evolves based on a processing rate δc\delta\_{c} (decay) and new arbitrageur submissions. It represents a mean-field state tracking redemption submissions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lc,t+1=(1−δc)​Lc,t+πA​rc,tL\_{c,t+1}=(1-\delta\_{c})L\_{c,t}+\pi\_{A}r\_{c,t} |  | (4) |

Algorithm 1  MFE Policy Iteration Algorithm

0:  (𝒫,𝒜,ℳ)(\mathcal{P},\mathcal{A},\mathcal{M}), (ϵexploit,ϵμ,kmax)(\epsilon\_{\text{exploit}},\epsilon\_{\mu},k\_{\max})

1:  Initialize: k←0k\leftarrow 0, μ0←{mt,Lt,ϕt,ψt}t=0T\mu^{0}\leftarrow\{m\_{t},L\_{t},\phi\_{t},\psi\_{t}\}\_{t=0}^{T}

2:  repeat

3:   k←k+1k\leftarrow k+1

4:   μprev←μk−1\mu^{\text{prev}}\leftarrow\mu^{k-1}

5:   (ΠR,ΠA)←SolveBestResponse​(𝒫,𝒜,ℳ,μprev)(\Pi\_{R},\Pi\_{A})\leftarrow\textsc{SolveBestResponse}(\mathcal{P},\mathcal{A},\mathcal{M},\mu^{\text{prev}})

6:   μk←UpdateMeanField​(𝒫,𝒜,ℳ,ΠR,ΠA)\mu^{k}\leftarrow\textsc{UpdateMeanField}(\mathcal{P},\mathcal{A},\mathcal{M},\Pi\_{R},\Pi\_{A})

7:   Exploit←ComputeExploitability​(𝒫,𝒜,ℳ,μk)\text{Exploit}\leftarrow\textsc{ComputeExploitability}(\mathcal{P},\mathcal{A},\mathcal{M},\mu^{k})

8:   E←Exploit​[max\_exploit]E\leftarrow\text{Exploit}[\text{max\\_exploit}]

9:   Δμ←∥μpricek−μpriceprev∥∞\Delta\_{\mu}\leftarrow\lVert\mu^{k}\_{\text{price}}-\mu^{\text{prev}}\_{\text{price}}\rVert\_{\infty}

10:  until (E<ϵexploit∧Δμ<ϵμ)∨k≥kmax(E<\epsilon\_{\text{exploit}}\ \land\ \Delta\_{\mu}<\epsilon\_{\mu})\ \lor\ k\geq k\_{\max}

11:  return converged mean field μ∗\mu^{\*} and policies (ΠR,ΠA)(\Pi\_{R},\Pi\_{A})

### III-D Stochastic Volatility and State-Dependent Parameters

To capture realistic, time-varying market stress, the market model incorporates state-dependent dynamics with a stochastic volatility process. The volatility is modeled as a GARCH process [[8](https://arxiv.org/html/2601.18991v1#bib.bib27 "Generalized autoregressive conditional heteroskedasticity")] for the conditional variance σt2\sigma^{2}\_{t} of the exogenous price shock ϵt\epsilon\_{t}. The exogenous shock from Equation [3](https://arxiv.org/html/2601.18991v1#S3.E3 "In III-C Stablecoin Market Dynamics ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") is defined as ϵt=σt​Zt\epsilon\_{t}=\sigma\_{t}Z\_{t}, where Zt∼𝒩​(0,1)Z\_{t}\sim\mathcal{N}(0,1) is a standard normal random variable, and the variance evolves according to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt2=ω+α​ϵt−12+β​σt−12\sigma\_{t}^{2}=\omega+\alpha\epsilon\_{t-1}^{2}+\beta\sigma\_{t-1}^{2} |  | (5) |

where ω,α,β\omega,\alpha,\beta are the standard GARCH parameters calibrated to stablecoin market data.
This time-varying volatility σt\sigma\_{t} directly modulates key parameters of the market environment and agent costs. Agents’ execution frictions (κ\kappa) and inventory aversion (η\eta) are scaled by the current volatility, reflecting increased risk aversion and costs in turbulent markets

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | κi,s,t\displaystyle\kappa\_{i,s,t} | =κi,s,0​(1+ci​σt)\displaystyle=\kappa\_{i,s,0}(1+c\_{i}\sigma\_{t}) |  | (6) |
|  | ηi,t\displaystyle\eta\_{i,t} | =ηi,0​(1+di​σt)\displaystyle=\eta\_{i,0}(1+d\_{i}\sigma\_{t}) |  |

where cic\_{i} and did\_{i} are the risk-scaling sensitivities for agent type i∈{R,A}i\in\{R,A\}. Secondary market price impact (liquidity) also becomes volatility-dependent, with each venue ss having its own sensitivity asa\_{s}

|  |  |  |  |
| --- | --- | --- | --- |
|  | λs,t=λs,0​(1+as​σt)\lambda\_{s,t}=\lambda\_{s,0}(1+a\_{s}\sigma\_{t}) |  | (7) |

Agents employ a softmax-based routing logic to dynamically allocate trades across secondary venues, minimizing their effective, time-varying costs which depend on the now state-dependent impact λs,t\lambda\_{s,t} and frictions κi,s,t\kappa\_{i,s,t}.

### III-E Mean-Field Equilibrium Computation

We solve for the Mean-Field Equilibrium (MFE) computationally. The MFE is a fixed point where the agents’ policies are optimal given the mean field. Also, the mean field is consistent with the aggregation of those policies.
Our approach employs the Policy Iteration algorithm, as detailed in Algorithm [1](https://arxiv.org/html/2601.18991v1#alg1 "Algorithm 1 ‣ III-C Stablecoin Market Dynamics ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"), in line with numerical methods for MFGs and learning-based approaches [[17](https://arxiv.org/html/2601.18991v1#bib.bib5 "Learning in mean field games: a survey"), [9](https://arxiv.org/html/2601.18991v1#bib.bib22 "A policy iteration method for mean field games")]. The algorithm iteratively computes agents’ best-response policies and updates the mean-field dynamics until a fixed point is reached.

The algorithm terminates when two conditions are met: 1) the mean-field trajectory converges, and 2) the system reaches an ϵ\epsilon-Nash equilibrium. We validate the ϵ\epsilon-Nash condition by calculating the exploitability (EE), which measures the maximum profit any agent could gain by deviating from the MFE policy. By ensuring E<ϵe​x​p​l​o​i​tE<\epsilon\_{exploit}, we confirm that no agent has a significant incentive to deviate from the equilibrium policy.

TABLE I: Baseline Model Calibrated Parameters

| Category | Parameter | Value |
| --- | --- | --- |
| Simulation Control | Time horizon (TT) | 4040 |
|  | Discount factor (γ\gamma) | 0.970.97 |
|  | Initial mispricing (m0m\_{0}) | −0.01-0.01 |
|  | Time step (Δ​t\Delta t) | 1.01.0 |
| Market Structure | Secondary venues (SS) | 33 |
|  | Primary channels (CC) | 22 |
|  | Secondary price impact (λs\lambda\_{s}) | [1.6,1.8,2.5][1.6,1.8,2.5] |
|  | Primary price impact (γc\gamma\_{c}) | [2.0,1.4][2.0,1.4] |
|  | Venue weights (ww) | [0.5,0.35,0.15][0.5,0.35,0.15] |
| Agent Population | Retail share (πR\pi\_{R}) | 0.850.85 |
|  | Arbitrageur share (πA\pi\_{A}) | 0.150.15 |
| Retail Costs | Secondary execution (κR\kappa\_{R}) | [2.0,3.0,4.0][2.0,3.0,4.0] |
|  | Inventory aversion (ηR\eta\_{R}) | 0.150.15 |
|  | Congestion cost (ξR\xi\_{R}) | 0.50.5 |
| Arbitrageur Costs | Secondary execution (κA\kappa\_{A}) | [1.2,1.5,2.0][1.2,1.5,2.0] |
|  | Primary execution (κP\kappa\_{P}) | [0.8,0.6][0.8,0.6] |
|  | Inventory aversion (ηA\eta\_{A}) | 0.200.20 |
|  | Congestion cost (ξA\xi\_{A}) | 0.30.3 |



![Refer to caption](results/usdc_2023_depeg_fit.png)

![Refer to caption](results/usdt_2022_depeg_fit.png)

![Refer to caption](results/usdt_2023_depeg_fit.png)

Figure 3: Comparison of the simulated stablecoin price path against the historical observed price data during each de-peg event.



![Refer to caption](results/usdc_2023_depeg_params.png)

![Refer to caption](results/usdt_2022_depeg_params.png)

![Refer to caption](results/usdt_2023_depeg_params.png)

Figure 4: Calibrated model parameters across three distinct market regimes identified during each de-peg event.

### III-F Model Calibration and Parameter Estimation

We calibrate our model by testing it against real-world de-peg events. We do this in two steps: first, we split the event data into phases, and second, we estimate the model’s parameters.
We analyze historical price data by splitting each de-peg event into three distinct, consecutive phases. This helps us see how market behavior changes over time. We define the phases as:

* •

  De-peg Phase: This period starts when the price first drops sharply below $1. It’s marked by high volatility, falling prices, and market stress.
* •

  Recovery Phase: This phase starts from the lowest price (de-peg). It covers the time when the price is clearly climbing back toward $1.
* •

  Stable Phase: This is the final phase where the price has returned to $1 and stays within a normal, tight range.

Market data does not directly reveal many key parameters of the model. We therefore estimate them by fitting the model’s price predictions to observed price dynamics. Following Richiardi et al. [[23](https://arxiv.org/html/2601.18991v1#bib.bib34 "A common protocol for agent-based social simulation")], we treat calibration as a systematic exploration of the admissible parameter space rather than an informal tuning exercise. This “full exploration” principle is particularly important in agent-based models, where non-linear interactions can generate sharp regime changes and multiple locally optimal parameter regions.

We measure the accuracy of the price fit using a score, ℒ​(θ)\mathcal{L}(\theta), such as mean squared error (MSE). We find the best parameters, θ∗\theta^{\*}, by finding the set that gives the lowest MSE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∗=arg⁡minθ⁡ℒ​(θ)=arg⁡minθ⁡[1T​∑t=1T(mt​(θ)−mtobs)2]\theta^{\*}=\arg\min\_{\theta}\mathcal{L}(\theta)=\arg\min\_{\theta}\left[\frac{1}{T}\sum\_{t=1}^{T}(m\_{t}(\theta)-m\_{t}^{\text{obs}})^{2}\right] |  | (8) |

where mt​(θ)m\_{t}(\theta) is model-implied mispricing and mtobsm\_{t}^{\text{obs}} is the empirical mispricing. We solve this non-convex problem using Differential Evolution [[24](https://arxiv.org/html/2601.18991v1#bib.bib28 "Differential evolution: a simple and efficient heuristic for global optimization over continuous spaces")], a population-based global optimizer that improves robustness to local minima.

## IV Simulation Parameters

### IV-A Baseline Calibration

To analyze the model, we first establish a baseline calibration designed to realistically reflect the normal market conditions for fiat-collateralized stablecoins as shown in Table [I](https://arxiv.org/html/2601.18991v1#S3.T1 "TABLE I ‣ III-E Mean-Field Equilibrium Computation ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
For the dynamic environment, we work with a discrete time horizon of T=40T=40 periods and a per–period discount factor of γ=0.97\gamma=0.97, which corresponds to the horizon and discounting used in the calibrated stable regime.

### IV-B Dataset Extraction

For the empirical analysis, we use high–frequency spot price data for the stablecoins USDC and USDT from Binance [[7](https://arxiv.org/html/2601.18991v1#bib.bib31 "Historical market data")]. We extract Kline (candlestick) data from Binance’s public spot market API, which reports open, high, low, close, and traded volume for fixed time intervals.
For the March 2023 USDC de-peg, we use one–minute Klines for USDC/USD on Binance, covering the period from March 11, 2023, to March 15, 2023 (UTC). This window covers the announcement of Silicon Valley Bank’s receivership, the sharp weekend discount in USDC, and the subsequent recovery once primary redemption channels and off–chain reserve access were restored.

For the May 2022 USDT de-peg linked to the TerraUSD collapse, we extract one–minute Klines for USDT/USD trading pair on Binance from May 12, 2022, to May 16, 2022 (UTC).
Finally, for the localized July 2023 USDT dislocation on Binance, we utilize Kline data for the relevant USDT/USD trading pair from July 15, 2023, to July 31, 2023 (UTC).

## V Experimental Results

### V-A Calibration to De-Peg Events

To validate the model against a significant real-world stress event, we fit the dynamic MFG framework to the historical data from three de-peg events. Figure [3](https://arxiv.org/html/2601.18991v1#S3.F3 "Figure 3 ‣ III-E Mean-Field Equilibrium Computation ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") provides a direct comparison of the model’s performance, as it plots the observed historical price against the price path generated by the fitted model. The model captures the key dynamics of the event, including the sharp initial de-peg, high volatility, and the subsequent recovery path back to the peg. We achieve this fit by calibrating the model to reflect the different market regimes of the event.

To give intuition for the calibration, Figure [4](https://arxiv.org/html/2601.18991v1#S3.F4 "Figure 4 ‣ III-E Mean-Field Equilibrium Computation ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") reports the event-specific values of the key execution and liquidity parameters: primary redemption friction κP\kappa\_{P}, secondary execution frictions (retail κR\kappa\_{R} and arbitrageur κA\kappa\_{A}), and venue impact λs\lambda\_{s}. These coefficients enter the quadratic execution and price-impact penalties in the agents’ objectives, so larger values correspond to more expensive, slower, or capacity-constrained trading per unit notional. Across all three events, the calibrated κP\kappa\_{P} is highest in stressed regimes and declines toward the stable regime, consistent with temporary impairment or congestion of mint/redeem rails during acute stress. Secondary frictions κR\kappa\_{R} (and κA\kappa\_{A}) tend to peak in recovery, when order books are thinnest and marginal execution costs are elevated as markets rebalance. The venue-impact terms λs\lambda\_{s} move in the same direction, rising in stressed regimes when a given net flow produces a larger price response. Importantly, these are effective parameters estimated by minimizing the price-path loss over each regime window, so they should be interpreted as capturing the composite of fees, slippage, balance-sheet constraints, and operational delays in that episode. These figures demonstrate the model’s ability to replicate a complex, real-world de-peg by dynamically adjusting parameters to reflect underlying market disruptions, such as primary rail failures and the resulting congestion.

### V-B Estimating the Half-life of De-peg Events

To quantify the peg recovery speed, we estimate the empirical half-life for each de-peg event and compare this metric to the half-life generated by our fitted MFG model. We define the half-life as the time required for the de-peg to decay by 50%. To estimate this from historical data, we follow the autoregressive AR(1) methodology [[18](https://arxiv.org/html/2601.18991v1#bib.bib3 "What keeps stablecoins stable?")]. We fit the mispricing mtm\_{t} to the process mt=ρ​mt−1+ϵtm\_{t}=\rho m\_{t-1}+\epsilon\_{t} and calculate the half-life H​L=ln⁡(2)/(−ln⁡ρ)HL=\ln(2)/(-\ln\rho).

![Refer to caption](results/half_life_comparison_all_events.png)


Figure 5: Historical price trajectories and estimated AR(1) half-lives for the three de-peg events.




TABLE II: Average performance of the dynamic MFG and reduced-form baselines across the three calibrated de-peg events.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | Avg. RMSE | |  | | --- | | Avg. half-life error | | |  | | --- | | Captures agent | | dynamics? | |
| AR(1) | 0.0158 | 0.36 | No |
| ARMA-GARCH | 0.0162 | 0.24 | No |
| ARX | 0.0217 | 1.15 | No |
| Dynamic MFG | 0.0128 | 0.41 | Yes |




TABLE III: Out-of-sample performance of the dynamic MFG on the March 2023 USDC de-peg event under different train/test splits.

| Split ratio | Train RMSE | Test RMSE | Train MAE | Test MAE |
| --- | --- | --- | --- | --- |
| 70/30 | 0.002809 | 0.007234 | 0.001754 | 0.006180 |
| 80/20 | 0.002287 | 0.007048 | 0.001571 | 0.005682 |
| 90/10 | 0.002029 | 0.007272 | 0.001329 | 0.005893 |



![Refer to caption](results/primary_flow_comparison_fast.png)

![Refer to caption](results/primary_flow_comparison_usdt22.png)

![Refer to caption](results/primary_flow_comparison_usdt23.png)

Figure 6: Decomposition of net peg-reverting flows into primary-market mint/redeem flow and secondary-market buying flow on exchanges during each de-peg event. Left: USDC March 2023. Middle: USDT May 2022. Right: USDT July 2023.

Figure [5](https://arxiv.org/html/2601.18991v1#S5.F5 "Figure 5 ‣ V-B Estimating the Half-life of De-peg Events ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") plots the historical price trajectories for the three events, with the empirically estimated half-life for each marked by a vertical dashed line.
For the May 2022 event, both data and model agree on a rapid, sub-3-hour recovery. For the March 2023 event, the model estimates a half-day recovery. For the July 2023 event, the model predicts a 45.9-hour half-life, slightly longer than the 30.7-hour empirical value, but correctly identifies the slow recovery. This result validates that our model, calibrated on agent-level frictions, can translate the micro-level parameters into correct macro-level recovery dynamics.

### V-C Baselines and Model Comparison

To evaluate how much explanatory power we gain from the dynamic MFG relative to standard reduced-form approaches, we benchmark it against three time-series models that are widely used to describe mean-reverting price dynamics [[25](https://arxiv.org/html/2601.18991v1#bib.bib33 "Analysis of financial time series")]. All models are estimated separately for each de-peg episode, using the same calibration windows as those used for the dynamic MFG.

For each de-peg event and each model, we compute two complementary metrics.
Table [II](https://arxiv.org/html/2601.18991v1#S5.T2 "TABLE II ‣ V-B Estimating the Half-life of De-peg Events ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") reports averages of these metrics across the three calibrated de-peg episodes. Among the models, the dynamic MFG achieves the lowest average RMSE and a lower average half-life error than the reduced form baselines taken collectively, even though the AR(1) and ARMA-GARCH specifications achieve slightly smaller half–life errors in isolation. More importantly, only the dynamic MFG explicitly represents interacting retail and arbitrageur populations trading across primary and secondary venues, making it suitable for counterfactual experiments on market structure that are beyond the scope of purely statistical models.

To check that the dynamic MFG does not simply overfit a single calibration window, we also perform a simple out-of-sample evaluation on the March 2023 USDC de-peg. For each of three train/test splits (70/30, 80/20, 90/10), we re-estimate the model on the training segment only and then simulate the price path over the held-out portion of the event. Table [III](https://arxiv.org/html/2601.18991v1#S5.T3 "TABLE III ‣ V-B Estimating the Half-life of De-peg Events ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") reports the resulting root mean squared error and mean absolute error. As the training share increases, in-sample errors decline monotonically, while test RMSE and MAE remain stable in a narrow band around 7×10−37\times 10^{-3} and 6×10−36\times 10^{-3}, respectively. The small variation in test performance across splits suggests that the dynamic MFG captures persistent features of the de-peg dynamics rather than idiosyncratic noise specific to a particular calibration window.

### V-D Decomposition of Peg-Reverting Flows

A key objective of our framework is to identify which participants and channels restore the peg after a de-peg. Using the calibrated model, we decompose the total peg-reverting flows into two components — (1) Primary Market: net mint/redeem flow, accessible only to arbitrageurs and capturing direct redemptions at par, and (2) Secondary Market: net buying on exchanges by all agents, capturing speculative or exchange-based arbitrage. For each event, we quantify these contributions by integrating aggregate primary redemption flow ρp\rho\_{p} and secondary net buying ρs\rho\_{s} over the simulation horizon.

Figure [6](https://arxiv.org/html/2601.18991v1#S5.F6 "Figure 6 ‣ V-B Estimating the Half-life of De-peg Events ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") shows that the dominant restoration channel is event-specific. In the May 2022 USDT episode, stabilization is overwhelmingly driven by primary-market redemptions, consistent with a functional redemption rail and active arbitrage. In the March 2023 USDC episode, the primary channel initially contributes negatively due to impaired minting and redemptions, and recovery reflects a joint role of primary and secondary forces once the primary rails are restored. In the July 2023 USDT venue-level failure, both channels contribute little, consistent with a localized outage that simultaneously blocks primary arbitrage and fragments secondary liquidity.

### V-E Sensitivity to Primary & Secondary Market Structure

![Refer to caption](results/heatmap_primary_vs_secondary.png)

![Refer to caption](results/heatmap_retail_vs_primary.png)

Figure 7: De-peg half-life sensitivity to market frictions κP,κR\kappa\_{P},\kappa\_{R} and composition πR\pi\_{R}.

![Refer to caption](results/market_structure_heatmap_structure_3d.png)


Figure 8: De-peg half-life as a function of retail trader share πR\pi\_{R} and secondary price impact scale λscale\lambda\_{\text{scale}} with fixed primary frictions.



![Refer to caption](results/july23_exploitability_convergence.png)

![Refer to caption](results/july23_wasserstein_convergence.png)

![Refer to caption](results/recovery_regime_comparison.png)

Figure 9: Convergence diagnostics and coupling sensitivity. Left: exploitability E​(π)E(\pi) across policy-iteration steps. Middle: mean-field distance W​(μ)W(\mu) across steps. Right: maximum exploitability at convergence vs coupling strength ξ\xi across de-peg events.

Our event calibrations point to primary mint/redeem friction κP\kappa\_{P} as the main determinant of peg stability, capturing higher redemption fees, tighter access constraints (e.g., KYC or banking limits), and slower settlement on primary rails. We generalize this insight with counterfactual simulations that vary (i) primary versus secondary trading frictions and (ii) market composition under primary-market stress. Figure [7](https://arxiv.org/html/2601.18991v1#S5.F7 "Figure 7 ‣ V-E Sensitivity to Primary & Secondary Market Structure ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") shows that κP\kappa\_{P} is the binding constraint: when the primary channel is inexpensive (roughly κP≤10\kappa\_{P}\leq 10), de-peg half-life remains short (about 2-4 model steps) across a wide range of secondary frictions κR\kappa\_{R} and retail shares πR\pi\_{R}. Once κP\kappa\_{P} rises past a critical range (about 15-18), half-life increases sharply, consistent with a breakdown of mint/redeem arbitrage, and secondary illiquidity becomes relevant mainly in this impaired-primary region.

Holding primary frictions fixed at a moderately stressed level, we then vary secondary-market structure via retail share πR\pi\_{R} and a liquidity-depth scale λscale\lambda\_{\text{scale}} that rescales secondary price impact. Figure [8](https://arxiv.org/html/2601.18991v1#S5.F8 "Figure 8 ‣ V-E Sensitivity to Primary & Secondary Market Structure ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") shows a monotone slowdown in recovery as λscale\lambda\_{\text{scale}} increases (shallower books), with half-life exceeding 30 steps in the thinnest regimes. The slowdown is most pronounced at intermediate retail shares (approximately πR∈[0.4,0.7]\pi\_{R}\in[0.4,0.7]), where substantial retail flow combined with limited depth sustains mispricing and raises the cost of arbitrage. Recovery is faster when the population is heavily driven by arbitrageurs, and it moderates again when the market is almost entirely retail, due to reduced aggregate stabilizing capacity.

### V-F Analysis of Equilibrium Quality and Exploitability

We next examine the quality of the equilibria produced by the policy iteration solver. For any agent type i∈{R,A}i\in\{R,A\} and joint stationary policy π=(πR,πA)\pi=(\pi\_{R},\pi\_{A}), let Ji​(π;μπ)J\_{i}(\pi;\mu^{\pi}) denote the infinite horizon discounted cost defined in (1) and (2) when the mean field path μπ={μtπ}t≥0\mu^{\pi}=\{\mu\_{t}^{\pi}\}\_{t\geq 0} is generated by π\pi and then held fixed. The cost Ji​(π;μπ)J\_{i}(\pi;\mu^{\pi}) is the expected discounted sum of per-period trading PnL and cost terms, measured in dollars per unit notional.

Given a fixed equilibrium environment (π,μπ)(\pi,\mu^{\pi}), the best response πiBR\pi\_{i}^{\mathrm{BR}} for type ii is obtained by solving the same linear quadratic control problem [1](https://arxiv.org/html/2601.18991v1#S3.E1 "In III-B Economic Environment and Agent Types ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") or [2](https://arxiv.org/html/2601.18991v1#S3.E2 "In III-B Economic Environment and Agent Types ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"), but treating the mean field path μπ\mu^{\pi} and the implied congestion terms as exogenous and keeping the policy of the other population π−i\pi\_{-i} fixed. In other words, the deviating population reoptimizes once against the equilibrium environment, while the mean field and the other population do not adjust. We then define the normalized exploitability of π\pi for type ii as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ei​(π)=Ji​(π;μπ)−Ji​(πiBR,π−i;μπ)|Ji​(π;μπ)|.E\_{i}(\pi)=\frac{J\_{i}(\pi;\mu^{\pi})-J\_{i}(\pi\_{i}^{\mathrm{BR}},\pi\_{-i};\mu^{\pi})}{\lvert J\_{i}(\pi;\mu^{\pi})\rvert}. |  | (9) |

This dimensionless quantity measures the fractional improvement in the agent’s value function that can be obtained by a unilateral deviation, on the same infinite-horizon discounted scale as the original objective.

Figure [9](https://arxiv.org/html/2601.18991v1#S5.F9 "Figure 9 ‣ V-E Sensitivity to Primary & Secondary Market Structure ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics") summarizes equilibrium quality and convergence. The policy-iteration solver quickly reaches small arbitrageur exploitability E​(π)E(\pi), with final levels around 10−410^{-4} in Stable, 10−310^{-3} in De-peg, and a few 10−210^{-2} in Recovery, indicating tight ε\varepsilon-Nash behavior under the one-shot deviation test. In parallel, the mean-field path converges rapidly, with the Wasserstein distance W​(μ)W(\mu) between successive trajectories collapsing to a very low stable value, consistent with a strongly contractive fixed-point update across all regimes. Finally, varying the congestion coupling ξ\xi shows that equilibrium quality is robust to stronger mean-field interaction: the maximum converged exploitability remains below a few 10−210^{-2} even at the largest ξ\xi and decays toward 10−410^{-4} as coupling weakens.

## VI Conclusions and Future Work

We develop a dynamic Mean-Field Game framework for fiat-collateralized stablecoins, linking market microstructure, agent incentives, and peg dynamics within a single equilibrium model. Calibrations to three major episodes reproduce key features of observed price paths and half-lives, and allow us to isolate which channel restores the peg under different shocks – directly addressing the central question of “who restores the peg?” in practice. When primary redemption rails remain open, recovery is dominated by direct redemptions. When primary capacity is impaired but not broken, recovery reflects a joint contribution from primary arbitrage and secondary buying. When venue-level infrastructure failures both obstruct redemptions and fragment liquidity, both channels contribute little, and recovery is slow.

A central structural result is a non-linear threshold in primary-market friction. De-peg half-life remains short when primary execution costs stay within a functional range, but rises sharply once primary access becomes sufficiently expensive, beyond which even favorable secondary-market liquidity cannot restore rapid re-pegs. This converts the model into an operational design and risk-management criterion: peg robustness depends not only on reserve quality, but also on the accessibility, speed, fees, and operational resilience of mint and redeem rails, while secondary-market liquidity primarily acts as a complement that limits propagation of localized outages.

An oversimplification is that we work with two representative populations (retail and arbitrageurs) in a tractable LQ equilibrium setting. This abstraction simplifies heterogeneity among liquidity providers and can understate non-linear behavior under extreme stress, including binding constraints and discontinuous primary-rail access. It also treats volatility and liquidity as regime inputs and calibrates primarily to price paths and half-lives, rather than jointly matching flows and order book dynamics. Building on this, future work will incorporate additional agent types and venue-specific constraints, move beyond the LQ specification using learning-based MFG solvers with richer risk objectives and occasionally binding constraints, endogenize liquidity and volatility feedback within the mean field, and validate the model by jointly fitting on-chain flows with high-frequency order book data.

## References

* [1]
  M. Abraham (2024)
  Crypto lending and stablecoin de-pegging: key risks and challenges.
  International Journal of Cryptocurrency Research 4 (1),  pp. 79–100.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p1.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [2]
  R. F. Almgren (2003)
  Optimal execution with nonlinear impact functions and trading-enhanced risk.
  Applied Mathematical Finance 10 (1),  pp. 1–18.
  Cited by: [§III-B](https://arxiv.org/html/2601.18991v1#S3.SS2.p2.2 "III-B Economic Environment and Agent Types ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [3]
  L. Ante (2022)
  Liquidity shocks, token returns and market capitalization in decentralized finance (defi) markets.
  BRL Working Paper Series
  Technical Report 26, Blockchain Research Lab.
  Cited by: [§II-A](https://arxiv.org/html/2601.18991v1#S2.SS1.p1.1 "II-A Stablecoin Peg Arbitrage and Restoration Mechanics ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [4]
  E. Barucci, G. Giuffra Moncayo, and D. Marazzina (2023)
  Market impact and efficiency in cryptoassets markets.
  Digital Finance 5 (3),  pp. 519–562.
  Cited by: [§II-B](https://arxiv.org/html/2601.18991v1#S2.SS2.p2.1 "II-B Market Microstructure of Digital Assets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [5]
  A. Bensoussan, K. C. J. Sung, S. C. P. Yam, and S. Yung (2016)
  Linear-quadratic mean field games.
  Journal of Optimization Theory and Applications 169 (2),  pp. 496–529.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p3.2 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§II-C](https://arxiv.org/html/2601.18991v1#S2.SS3.p2.1 "II-C Game-Theoretic Models for Stablecoin Markets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [6]
  S. Bhat, A. B. Kahya, B. Krishnamachari, and R. Kumar (2021)
  Daisim: a computational simulator for the makerdao stablecoin.
  In 4th International Symposium on Foundations and Applications of Blockchain 2021 (FAB 2021),
   pp. 3:1–3:13.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p4.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [7]
  Binance.US (2025)
  Historical market data.
  Note: <https://www.binance.us/institutions/market-history>
  Cited by: [§IV-B](https://arxiv.org/html/2601.18991v1#S4.SS2.p1.1 "IV-B Dataset Extraction ‣ IV Simulation Parameters ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [8]
  T. Bollerslev (1986)
  Generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics 31 (3),  pp. 307–327.
  Cited by: [§III-D](https://arxiv.org/html/2601.18991v1#S3.SS4.p1.4 "III-D Stochastic Volatility and State-Dependent Parameters ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [9]
  S. Cacace, F. Camilli, and A. Goffi (2021)
  A policy iteration method for mean field games.
  ESAIM: Control, Optimisation and Calculus of Variations 27,  pp. 85.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p3.2 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§III-E](https://arxiv.org/html/2601.18991v1#S3.SS5.p1.1 "III-E Mean-Field Equilibrium Computation ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [10]
  F. Calandra, F. P. Rossi, F. Fabris, and M. Bernardo (2025)
  Algorithmic stablecoins: a simulator for the dual-token model in normal and panic scenarios.
  In 2025 IEEE International Conference on Blockchain and Cryptocurrency (ICBC),
   pp. 1–9.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p4.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [11]
  P. Cardaliaguet and C. Lehalle (2018)
  Mean field game of controls and an application to trade crowding.
  Mathematics and Financial Economics 12 (3),  pp. 335–363.
  Cited by: [§II-C](https://arxiv.org/html/2601.18991v1#S2.SS3.p3.1 "II-C Game-Theoretic Models for Stablecoin Markets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [12]
  R. Carmona, F. Delarue, and D. Lacker (2017)
  Mean field games of timing and models for bank runs.
  Applied Mathematics & Optimization 76 (1),  pp. 217–260.
  Cited by: [§II-C](https://arxiv.org/html/2601.18991v1#S2.SS3.p3.1 "II-C Game-Theoretic Models for Stablecoin Markets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [13]
  Á. Cartea, F. Drissi, and M. Monga (2025)
  Decentralised finance and automated market making: execution and speculation.
  Journal of Economic Dynamics and Control,  pp. 105134.
  Cited by: [§II-B](https://arxiv.org/html/2601.18991v1#S2.SS2.p2.1 "II-B Market Microstructure of Digital Assets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§III-B](https://arxiv.org/html/2601.18991v1#S3.SS2.p2.2 "III-B Economic Environment and Agent Types ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [14]
  K. Cortez, M. d. P. Rodriguez-Garcia, and S. Mongrut (2020)
  Exchange market liquidity prediction with the k-nearest neighbor approach: crypto vs. fiat currencies.
  Mathematics 9 (1),  pp. 56.
  Cited by: [§II-B](https://arxiv.org/html/2601.18991v1#S2.SS2.p2.1 "II-B Market Microstructure of Digital Assets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [15]
  G. B. Gorton and J. Y. Zhang (2023)
  Taming wildcat stablecoins.
  University of Chicago Law Review 90 (3),  pp. 909–972.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p1.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§II-A](https://arxiv.org/html/2601.18991v1#S2.SS1.p1.1 "II-A Stablecoin Peg Arbitrage and Restoration Mechanics ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [16]
  J. Lasry and P. Lions (2007)
  Mean field games.
  Japanese Journal of Mathematics 2 (1),  pp. 229–260.
  Cited by: [§II-C](https://arxiv.org/html/2601.18991v1#S2.SS3.p2.1 "II-C Game-Theoretic Models for Stablecoin Markets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [17]
  M. Laurière, S. Perrin, J. Pérolat, S. Girgin, P. Muller, R. Élie, M. Geist, and O. Pietquin (2022)
  Learning in mean field games: a survey.
  arXiv preprint arXiv:2205.12944.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p3.2 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§II-C](https://arxiv.org/html/2601.18991v1#S2.SS3.p3.1 "II-C Game-Theoretic Models for Stablecoin Markets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§III-A](https://arxiv.org/html/2601.18991v1#S3.SS1.p1.11 "III-A Dynamic Mean-Field Game Framework ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§III-E](https://arxiv.org/html/2601.18991v1#S3.SS5.p1.1 "III-E Mean-Field Equilibrium Computation ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [18]
  R. K. Lyons and G. Viswanath-Natraj (2023)
  What keeps stablecoins stable?.
  Journal of International Money and Finance 131,  pp. 102777.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p2.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§I](https://arxiv.org/html/2601.18991v1#S1.p4.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§II-A](https://arxiv.org/html/2601.18991v1#S2.SS1.p1.1 "II-A Stablecoin Peg Arbitrage and Restoration Mechanics ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§V-B](https://arxiv.org/html/2601.18991v1#S5.SS2.p1.3 "V-B Estimating the Half-life of De-peg Events ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [19]
  L. Magnino, K. Shao, Z. Wu, J. Shen, and M. Lauriere (2025)
  Solving continuous mean field games: deep reinforcement learning for non-stationary dynamics.
  In The Thirty-Ninth Annual Conference on Neural Information Processing Systems,
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p3.2 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [20]
  I. Makarov and A. Schoar (2020)
  Trading and arbitrage in cryptocurrency markets.
  Journal of Financial Economics 135 (2),  pp. 293–319.
  Cited by: [§II-A](https://arxiv.org/html/2601.18991v1#S2.SS1.p1.1 "II-A Stablecoin Peg Arbitrage and Restoration Mechanics ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§II-B](https://arxiv.org/html/2601.18991v1#S2.SS2.p1.1 "II-B Market Microstructure of Digital Assets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [21]
  I. G. A. Pernice (2021)
  On stablecoin price processes and arbitrage.
  In International Conference on Financial Cryptography and Data Security,
   pp. 124–135.
  Cited by: [§II-B](https://arxiv.org/html/2601.18991v1#S2.SS2.p1.1 "II-B Market Microstructure of Digital Assets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [22]
  Y. Potter, K. Pongmala, K. Qin, A. Klages-Mundt, P. Jovanovic, C. Parlour, A. Gervais, and D. Song (2024)
  What drives the (in)stability of a stablecoin?.
  In 2024 IEEE International Conference on Blockchain and Cryptocurrency (ICBC),
   pp. 316–324.
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p2.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§I](https://arxiv.org/html/2601.18991v1#S1.p4.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics"),
  [§II-C](https://arxiv.org/html/2601.18991v1#S2.SS3.p1.1 "II-C Game-Theoretic Models for Stablecoin Markets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [23]
  M. G. Richiardi, R. Leombruni, N. J. Saam, and M. Sonnessa (2006)
  A common protocol for agent-based social simulation.
  Journal of Artificial Societies and Social Simulation 9 (1).
  Cited by: [§III-F](https://arxiv.org/html/2601.18991v1#S3.SS6.p2.1 "III-F Model Calibration and Parameter Estimation ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [24]
  R. Storn and K. Price (1997)
  Differential evolution: a simple and efficient heuristic for global optimization over continuous spaces.
  Journal of Global Optimization 11 (4),  pp. 341–359.
  Cited by: [§III-F](https://arxiv.org/html/2601.18991v1#S3.SS6.p3.4 "III-F Model Calibration and Parameter Estimation ‣ III Methodology ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [25]
  R. S. Tsay (2010)
  Analysis of financial time series.
  3rd edition, John Wiley & Sons, Hoboken, NJ.
  Cited by: [§V-C](https://arxiv.org/html/2601.18991v1#S5.SS3.p1.1 "V-C Baselines and Model Comparison ‣ V Experimental Results ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [26]
  M. A. Uz Zaman, K. Zhang, E. Miehling, and T. Başar (2020)
  Reinforcement learning in non-stationary discrete-time linear-quadratic mean-field games.
  In 2020 59th IEEE Conference on Decision and Control (CDC),
   pp. 2278–2284.
  Cited by: [§II-C](https://arxiv.org/html/2601.18991v1#S2.SS3.p2.1 "II-C Game-Theoretic Models for Stablecoin Markets ‣ II Related Work ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").
* [27]
  C. Watsky, J. Allen, H. Daud, J. Demuth, D. Little, M. Rodden, and A. Seira (2024)
  Primary and secondary markets for stablecoins.
  FEDS Notes.
  Note: Board of Governors of the Federal Reserve System
  Cited by: [§I](https://arxiv.org/html/2601.18991v1#S1.p4.1 "I Introduction ‣ Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics").