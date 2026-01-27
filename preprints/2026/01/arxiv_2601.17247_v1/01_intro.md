---
authors:
- Julius Graf
- Thibaut Mastrolia
doc_id: arxiv:2601.17247v1
family_id: arxiv:2601.17247
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Learning Market Making with Closing Auctions
url_abs: http://arxiv.org/abs/2601.17247v1
url_html: https://arxiv.org/html/2601.17247v1
venue: arXiv q-fin
version: 1
year: 2026
---


Julius Graf111julius.graf@berkeley.edu   and  Thibaut Mastrolia222mastrolia@berkeley.edu
  
Department of Industrial Engineering and Operations Research
  
University of California, Berkeley, USA.

###### Abstract

In this work, we investigate the market-making problem on a trading session in which a continuous phase on a limit order book is followed by a closing auction. Whereas standard optimal market-making models typically rely on terminal inventory penalties to manage end-of-day risk, ignoring the significant liquidity events available in closing auctions, we propose a Deep Q-Learning framework that explicitly incorporates this mechanism. We introduce a market-making framework designed to explicitly anticipate the closing auction, continuously refining the projected clearing price as the trading session evolves. We develop a generative stochastic market model to simulate the trading session and to emulate the market. Our theoretical model and Deep Q-Learning method is applied on the generator in two settings: (1) when the mid price follows a rough Heston model with generative data from this stochastic model; and (2) when the mid price corresponds to historical data of assets from the S&P 500 index and the performance of our algorithm is compared with classical benchmarks from optimal market making.

Key words: optimal market making, auction trading, reinforcement learning, Markov Decision Process, Deep Q-Learning, regret analysis.

## 1 Introduction

### 1.1 Reinforcement learning and market making

Market making is a cornerstone of modern electronic financial markets, providing liquidity by continuously posting buy and sell quotes while managing inventory and adverse selection risk with different participants having diverse objectives. Since the seminal work of Avellaneda and Stoikov [[4](https://arxiv.org/html/2601.17247v1#bib.bib64 "High-frequency trading in a limit order book")] and its extension to explicit solutions in [[28](https://arxiv.org/html/2601.17247v1#bib.bib59 "Dealing with the inventory risk: a solution to the market making problem")], optimal market making has been studied extensively through stochastic control frameworks, leading to tractable strategies that balance expected profit against inventory risk under stylized assumptions on order flow dynamics and price evolution. We refer to [[15](https://arxiv.org/html/2601.17247v1#bib.bib31 "Algorithmic and high-frequency trading")] for a review of the literature on market making and high-frequency trading and to [[5](https://arxiv.org/html/2601.17247v1#bib.bib30 "Algorithmic market making for options"), [6](https://arxiv.org/html/2601.17247v1#bib.bib15 "Market liquidity and competition among designated market makers")] for recent advances in the topic. These models, however, typically rely on parametric assumptions that are difficult to validate empirically and may fail to adapt to the non-stationarity and strategic complexity of real-world markets.

The rapid growth of electronic trading and data availability combined with AI raising influence in financial industry has motivated the use of reinforcement learning as a flexible, data-driven alternative to classical control methods. Reinforcement learning allows a market maker to learn optimal quoting policies directly from interaction with the market, without requiring full knowledge of the underlying dynamics. Recent studies have demonstrated the promise of RL in market making and related problems, showing improved adaptability to complex market conditions, latent regimes, and evolving order flow patterns. The seminal article [[49](https://arxiv.org/html/2601.17247v1#bib.bib56 "Reinforcement learning for optimized trade execution")] introduces a Q-learning algorithm for market making problem on limit order book with many state variables. It has been later extended in for example [[7](https://arxiv.org/html/2601.17247v1#bib.bib6 "Market making via reinforcement learning"), [50](https://arxiv.org/html/2601.17247v1#bib.bib18 "Double deep Q-learning for optimal execution"), [57](https://arxiv.org/html/2601.17247v1#bib.bib54 "Deep learning for limit order books"), [25](https://arxiv.org/html/2601.17247v1#bib.bib57 "Market making with signals through deep reinforcement learning"), [29](https://arxiv.org/html/2601.17247v1#bib.bib29 "Deep reinforcement learning for market making in corporate bonds: beating the curse of dimensionality"), [33](https://arxiv.org/html/2601.17247v1#bib.bib45 "Mbt-gym: reinforcement learning for model-based limit order book trading"), [37](https://arxiv.org/html/2601.17247v1#bib.bib65 "Learning a functional control for high-frequency finance")] and adding regret analysis [[16](https://arxiv.org/html/2601.17247v1#bib.bib53 "Market making without regret"), [12](https://arxiv.org/html/2601.17247v1#bib.bib52 "Logarithmic regret in the ergodic Avellaneda-Stoikov market making model")]. We also refer to [[30](https://arxiv.org/html/2601.17247v1#bib.bib55 "Recent advances in reinforcement learning in finance"), [17](https://arxiv.org/html/2601.17247v1#bib.bib13 "Special issue on machine learning in finance"), [13](https://arxiv.org/html/2601.17247v1#bib.bib14 "Machine learning and data sciences for financial markets: a guide to contemporary practices")] for comprehensive summaries of recent advances in RL techniques in finance.

While the notion of market making is an active topic of research including new developments with reinforcement learning technics, one aspect remains insufficiently explored in the RL-based market making literature. At the end of the day, most of exchanges are closing the market by triggering a closing auction, which plays a fundamental role in price discovery and liquidity provision in modern equity markets. Closing auctions concentrate a significant fraction of daily trading volume and often exhibit dynamics that differ markedly from those observed during continuous trading. Inventory held into the closing auction can be liquidated at a single clearing price, but doing so exposes the market maker to auction-specific price impact, imbalance risk, and strategic interactions. Traditional market making models typically ignore the auction or treat the end-of-day liquidation in an ad-hoc manner, while most reinforcement learning approaches focus exclusively on continuous limit order book trading.

This paper aims to bridge this gap by proposing a reinforcement learning framework for optimal market making that explicitly incorporates regret minimization and a closing auction mechanism. We consider a market maker who operates over a finite horizon, posting bid and ask quotes during continuous trading and facing a terminal liquidation opportunity through a closing auction. The agent does not assume knowledge of the true order arrival intensities, price impact, or auction clearing rules, and instead learns an optimal policy through interaction with the market.

### 1.2 On the importance of (closing) auctions

Early works in financial auctions has been developed in [[36](https://arxiv.org/html/2601.17247v1#bib.bib36 "Continuous auctions and insider trading")]. In this article, Kyle provides the first tractable equilibrium model of a continuous auction with asymmetric information.
It explains how prices aggregate private information through order flow, introducing measure of market depth and price impact. This paper became the benchmark for analyzing liquidity, price discovery, and strategic trading in modern auction-based financial markets. While auction markets have been well-investigated in the economical community for discrete-time model, see for example [[44](https://arxiv.org/html/2601.17247v1#bib.bib28 "Auctions and bidding: a primer"), [59](https://arxiv.org/html/2601.17247v1#bib.bib27 "Optimal dynamic auctions for revenue management"), [43](https://arxiv.org/html/2601.17247v1#bib.bib16 "Putting auction theory to work")] and have known a growing interest, especially since the work of the Nobel laureate Paul Milgrom, it stays challenging at the high frequency-level and for continuous time framework and has been pointed as one of the most challenging question in financial engineering in [[14](https://arxiv.org/html/2601.17247v1#bib.bib40 "The influence of economic research on financial mathematics: evidence from the last 25 years"), Section 5.1].

The big picture of the trading session considered in this paper is the following: along the session a market maker quotes on a limit order book to liquidate her position until the end of the continuous trading time session. Then, the exchange triggers a closing auction for the next minutes of the day. During this auction, order are accumulated by the exchange along time, where participants proposes limit orders at which there are willing to buy or sell the asset with a specific volume, and limit order of the previous continuous trading phase are added as trading block for the auction clearing. At the end of the auction phase, known as the clearing time, a clearing price is set by the exchange to ensure as much transaction as possible to clear the market and trade the asset. This closing auction plays a fundamental role in market liquidation and empowers efficiency of price discovery as explained in [[34](https://arxiv.org/html/2601.17247v1#bib.bib35 "The effect of a closing call auction on market quality and trading strategies"), [53](https://arxiv.org/html/2601.17247v1#bib.bib51 "The growing importance of the closing auction in share trading volumes")]. We also refer to [[45](https://arxiv.org/html/2601.17247v1#bib.bib37 "Auction market design: recent innovations")] for an overview of auction mechanism.

On the one hand, auctions successfully fix mechanical flaws of limit order book like correlation breakdown as explained in [[11](https://arxiv.org/html/2601.17247v1#bib.bib50 "Implementation details for frequent batch auctions: slowing down markets to the blink of an eye")]. On the other hand, unlike a LOB trading, the key challenge of the auction phase is to set an efficient (clearing) price to trade the asset, given the different operations of market participants, known as the price discovery mechanism [[38](https://arxiv.org/html/2601.17247v1#bib.bib34 "Price discovery in auction markets: a look inside the black box"), [8](https://arxiv.org/html/2601.17247v1#bib.bib33 "IPO auctions: english, dutch,… french, and internet"), [9](https://arxiv.org/html/2601.17247v1#bib.bib32 "Price discovery and learning during the preopening period in the paris bourse")].

The benefit of auctions for market quality, as reducing the spread between the clearing price and the efficient price of a risk asset has been investigated in the recent literature, for example [[20](https://arxiv.org/html/2601.17247v1#bib.bib39 "Welfare and optimal trading frequency in dynamic double auctions"), [51](https://arxiv.org/html/2601.17247v1#bib.bib60 "Optimal auction duration: a price formation viewpoint"), [18](https://arxiv.org/html/2601.17247v1#bib.bib38 "AHEAD: ad hoc electronic auction design"), [56](https://arxiv.org/html/2601.17247v1#bib.bib26 "Equity auction dynamics: latent liquidity models with activity acceleration"), [31](https://arxiv.org/html/2601.17247v1#bib.bib25 "Transaction cost (in) transparency: coasian dynamics in frequent batch auctions")] by proposing incentives and optimal fees scheme to mitigate auctions’ flaws [[40](https://arxiv.org/html/2601.17247v1#bib.bib48 "Clearing time randomization and transaction fees for auction market design"), [41](https://arxiv.org/html/2601.17247v1#bib.bib49 "Optimal rebate design: incentives, competition and efficiency in auction markets")].

### 1.3 Methodology, contributions and financial insights

This work proposes a new market-making model based on a reinforcement learning approach, designed to operate over a typical trading session while explicitly anticipating the closing auction at the end of the session. As far as we know, this paper is the first considering a reinforcement learning method for CLOB optimal market making followed by anticipated closing auciton. The proposed reinforcement learning framework relies on Q-learning, originally introduced in [[61](https://arxiv.org/html/2601.17247v1#bib.bib24 "Q-learning")], and on its extension to Deep Q-Learning using neural networks for strategy exploration and selection [[47](https://arxiv.org/html/2601.17247v1#bib.bib17 "Playing atari with deep reinforcement learning"), [22](https://arxiv.org/html/2601.17247v1#bib.bib20 "A theoretical analysis of deep Q-learning")]. These approaches have been successfully applied to a wide range of financial problems, including optimal asset allocation, optimal execution in dark pools, and market making; see, for instance, [[48](https://arxiv.org/html/2601.17247v1#bib.bib23 "Enhancing Q-learning for optimal asset allocation"), [24](https://arxiv.org/html/2601.17247v1#bib.bib22 "Reinforcement learning for market making in a multi-agent dealer market"), [35](https://arxiv.org/html/2601.17247v1#bib.bib21 "Machine learning for market microstructure and high frequency trading"), [50](https://arxiv.org/html/2601.17247v1#bib.bib18 "Double deep Q-learning for optimal execution"), [5](https://arxiv.org/html/2601.17247v1#bib.bib30 "Algorithmic market making for options")].

More specifically, we compare a standard Q-learning approach for market making with closing auction trading to a neural-fitted Q-learning method. The goal of Q-learning is to find the optimal action-value function QQ which yields the optimal policy. Neural-fitted Q-learning consists in parameterizing the action-value function with a neural network QθQ\_{\theta} such that optimization over QQ becomes optimization over the weights θ∈ℝq\theta\in\mathbb{R}^{q}, for some q∈ℕ∗q\in\mathbb{N}^{\*}. In the Neural Fitted Q-Iteration (NFQ) algorithm, the neural network is trained by minimizing a squared temporal-difference error over a batch of sampled transitions using gradient descent [[55](https://arxiv.org/html/2601.17247v1#bib.bib2 "Neural fitted Q iteration–first experiences with a data efficient neural reinforcement learning method")]. Using a deep neural network for QθQ\_{\theta} then leads to the Deep Q-Network (DQN) approach. We refer to [[47](https://arxiv.org/html/2601.17247v1#bib.bib17 "Playing atari with deep reinforcement learning")] where QθQ\_{\theta} was a convolutional neural network (operating on pixels) used to play Atari games and outperform baseline methods. The primary strength of neural-fitted Q-learning is to handle high-dimensional state spaces, as it is the case in our study. The key contribution of DQN is to stabilize Deep Q-Learning through a replay memory 𝒟\mathcal{D} with fixed capacity NN: gradient steps are computed using mini-batches from the replay memory, which avoids the issue of correlated samples in trajectory. Training is furthermore stabilized by fixing the training target. One maintains a target Q-network whose parameters are held fixed for several updates and refreshed periodically [[58](https://arxiv.org/html/2601.17247v1#bib.bib5 "Reinforcement learning: an introduction"), [47](https://arxiv.org/html/2601.17247v1#bib.bib17 "Playing atari with deep reinforcement learning"), [46](https://arxiv.org/html/2601.17247v1#bib.bib4 "Human-level control through deep reinforcement learning")].

As a benchmark, we use the optimal market-making model introduced by [[4](https://arxiv.org/html/2601.17247v1#bib.bib64 "High-frequency trading in a limit order book")] and derived in [[28](https://arxiv.org/html/2601.17247v1#bib.bib59 "Dealing with the inventory risk: a solution to the market making problem")], which allows us to quantitatively assess the efficiency and performance of the Q-learning-based methods considered in this study. We furthermore compare the performance to the time-weighted average price strategy.

The structure of this work is the following. Section [2](https://arxiv.org/html/2601.17247v1#S2 "2 Market model ‣ Learning Market Making with Closing Auctions") describes the general trading session structure investigated. We first introduce the mathematical framework in Section [2.1](https://arxiv.org/html/2601.17247v1#S2.SS1 "2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"), providing rigorous definitions of all stochastic processes, agents, and market participants involved in the model. The continuous trading phase and the auction phase are respectively described in Sections [2.1.1](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS1 "2.1.1 Trading during the continuous phase [0,𝜏ᵒᵖ) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") and [2.1.2](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS2 "2.1.2 Trading during the auction phase [𝜏ᵒᵖ,𝜏^cl) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions").
We then introduce the auction clearing mechanism in Section [2.1.3](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS3 "2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"), where we also state the main theoretical result of this study: the existence of a clearing price under very general supply-demand functions given by Theorem [2.1](https://arxiv.org/html/2601.17247v1#S2.Thmtheorem1 "Theorem 2.1 (Existence of a unique (estimated) clearing price). ‣ 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"). Section [2.1.4](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS4 "2.1.4 Projected hypothetical clearing price during the continuous session ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") proposes an algorithm to predict a hypothetical clearing price during the limit order book trading session and to anticipate the conversion of unmatched limit orders into trade blocks for the future closing auction. This algorithm lies at the core of our contribution, as it directly links market-making decisions in the continuous phase to the projected outcome of the closing auction.
In Section [3](https://arxiv.org/html/2601.17247v1#S3 "3 Markov Decision Process and dynamic programming for optimal market making with closing auction ‣ Learning Market Making with Closing Auctions"), we formulate a Markov Decision Process modeling the market dynamics, the actions of the market maker, and the rewards generated by her activity across both the continuous trading phase and the auction phase. Section [4](https://arxiv.org/html/2601.17247v1#S4 "4 Learning market making with closing auction in an unknown environment ‣ Learning Market Making with Closing Auctions") establishes the regret analysis and introduces the (neural-fitted) Q-learning algorithm employed in our framework. Section [5](https://arxiv.org/html/2601.17247v1#S5 "5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions") recalls the main results of [[4](https://arxiv.org/html/2601.17247v1#bib.bib64 "High-frequency trading in a limit order book"), [28](https://arxiv.org/html/2601.17247v1#bib.bib59 "Dealing with the inventory risk: a solution to the market making problem")], which we use as a benchmark to compare the profit-and-loss (PnL for short) performance of a market maker who anticipates the closing auction with one who does not. Section [6](https://arxiv.org/html/2601.17247v1#S6 "6 Numerical simulations ‣ Learning Market Making with Closing Auctions") explains the numerical methods we considered in this work. Section [6.1](https://arxiv.org/html/2601.17247v1#S6.SS1 "6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") introduces the generative stochastic model of the market we use to simulate the Markov Decision Process for the numerical simulations. Section [6.2](https://arxiv.org/html/2601.17247v1#S6.SS2 "6.2 Benchmark simulations ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") presents the simulation for the two benchmark models use for our comparative study. In Section [6.3](https://arxiv.org/html/2601.17247v1#S6.SS3 "6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions"), we generate synthetic data using a stylized Heston model for the asset price, combined with limit order book parameters calibrated to reflect the projected future closing auction. Section [6.4](https://arxiv.org/html/2601.17247v1#S6.SS4 "6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") presents the numerical results obtained when using historical data of S&P 500 assets for the mid price process.

These numerical results highlight the benefits of anticipating the closing auction, as well as the effectiveness of the proposed Q-learning approach in maximizing the market maker’s PnL over a trading session for both stochastic rough models and historical data from the S&P 500.

## 2 Market model

### 2.1 Mathematical framework and trading phases

Along this work, we fix a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), named the market, where Ω\Omega represents all the possible market configurations, ℱ\mathcal{F} is a σ\sigma-algebra denoting the available information and ℙ\mathbb{P} is the market probability. We consider a financial asset traded on the financial market along a trading session with price evolving randomly. We divide the trading period into two phases: a continuous phase on a limit order book with market makers and takers and an auction phase, seen as a usual closing auction. We fix
two deterministic times 0<τop<τcl0<\tau^{\mathrm{op}}<\tau^{\mathrm{cl}} representing respectively the opening and the closing of the auction phase and denote by h=τcl−τoph=\tau^{\mathrm{cl}}-\tau^{\mathrm{op}} the auction duration. We assume that both (τop,τcl)∈ℕ2(\tau^{\mathrm{op}},\tau^{\mathrm{cl}})\in\mathbb{N}^{2} and hh is a positive integer. Therefore, the trading horizon is divided into a continuous phase [0,τop)[0,\tau^{\mathrm{op}}), in which the trader interacts with the central limit-order book (CLOB) and a fixed length hh closing auction [τop,τcl][\tau^{\mathrm{op}},\tau^{\mathrm{cl}}]. In what follows, we consider a fixed time grid 0=t0<⋯<tn<τop=tn+1<⋯<tm<τcl=tm+10=t\_{0}<\cdots<t\_{n}<\tau^{\mathrm{op}}=t\_{n+1}<\cdots<t\_{m}<\tau^{\mathrm{cl}}=t\_{m+1} for n∈ℕ∗n\in\mathbb{N}^{\*} and m∈ℕ∗m\in\mathbb{N}^{\*}.

We denote by ItI\_{t} the trader’s inventory at time tt. This inventory is positive (resp. negative) for long position (resp. short positions) with respect to the traded risky asset.

We denote by α>0\alpha>0 the tick size of the asset, fixed by the exchange. We will consider three types of market participants in this study:

* •

  a strategic market maker, named the agent, setting limit orders along the day,
* •

  exogenous market makers, fixing limit orders and providing liquidity during the continuous trading session on both side of the LOB and proposing limit prices during the auction session,
* •

  exogenous market takers. These participants submit aggressive market orders during both the CLOB and the auction phases to buy or sell the asset.

While we will focus on the optimization of the agent along the day, we use the term exogenous to emphasize the fact that other market makers and takers’ optimizations are not considered here. We now turn to the details of the trading period [0,τop)∪[τop,τcl][0,\tau^{\mathrm{op}})\cup[\tau^{\mathrm{op}},\tau^{\mathrm{cl}}] composed by continuous trading activities on the CLOB followed by a closing auction.

#### 2.1.1 Trading during the continuous phase [0,τop)[0,\tau^{\mathrm{op}})

During the continuous phase on the LOB, we assume that each market participant observes the mid price Stmid=α​ktmidS\_{t}^{\mathrm{mid}}=\alpha k\_{t}^{\mathrm{mid}} at any time t<τopt<\tau^{\mathrm{op}}, where ktmid∈ℕk^{\mathrm{mid}}\_{t}\in\mathbb{N} represents the number of tick at which the mid price is priced. Exogenous market takers take submit market orders on both side of the market and consume liquidity. The number of market taker arriving on the side ζ∈{+,−}\zeta\in\{+,-\} follows a counting process denoted by NζN^{\zeta}, where ζ=+\zeta=+ denotes the ask side, and ζ=−\zeta=- the bid side. In other words, NtζN\_{t}^{\zeta} market takers have arrived on the side ζ\zeta. We assume that each market taker i≤Ntζi\leq N\_{t}^{\zeta} submits a market order with volume νtζ,i\nu\_{t}^{\zeta,i} on the ζ\zeta side of the CLOB at time tt.

The agent is a market maker and submit limit orders characterized by a limit price denoted by St∙=α​ktS\_{t}^{\bullet}=\alpha k\_{t} at time tt where ktk\_{t} denoted the number of tick chosen at time tt to price the asset, and a proposed volume vtv\_{t}. The agent therefore submits an order characterized by the pair (kt,vt)(k\_{t},v\_{t}) at time tt on the limit order book. We assume that the agent is selling her inventory II on the LOB during the continuous phase. This order is thus a limit order on vt≤Itv\_{t}\leq I\_{t} shares at price St∙=α​ktS\_{t}^{\bullet}=\alpha k\_{t}.

###### Remark 2.1.

Note that δt:=kt−ktmid\delta\_{t}:=k\_{t}-k\_{t}^{\mathrm{mid}} represents the number of tick between the sell limit order proposed by the agent and the mid price, seen as the ask-spread of the agent.

The liquidity provided by exogenous market makers at price level Stζ,j=α​ktζ,jS\_{t}^{\zeta,j}=\alpha k\_{t}^{\zeta,j}, where ktζ,j=ktmid+ζ​jk\_{t}^{\zeta,j}=k\_{t}^{\mathrm{mid}}+\zeta j for j∈ℤj\in\mathbb{Z} and ζ∈{+,−}\zeta\in\{+,-\} is given by the volume Vtζ,jV\_{t}^{\zeta,j} at any time tt. The depth of the order book on side ζ\zeta is given by

|  |  |  |
| --- | --- | --- |
|  | Ltζ=inf{j≥1:Vtζ,j=0}.L\_{t}^{\zeta}=\inf\{j\geq 1:V\_{t}^{\zeta,j}=0\}. |  |

###### Assumption 1.

We assume that all market orders are always executed at any time tt during the LOB session.

Note that this assumption is justified by empirical evidence: market takers are in general small investors. It is consistent with [[51](https://arxiv.org/html/2601.17247v1#bib.bib60 "Optimal auction duration: a price formation viewpoint")] assuming that the LOB is never empty. Regarding now the execution of the limit orders sent by the agent, we will enforce the following assumption.

###### Assumption 2.

The agent is always executed with priority at a fixed depth of the CLOB, i.e., she systematically posts her orders at a predetermined price level and is assumed to be the fastest participant at that level.

In view of this assumption, we can see our agent as a high-frequency trader having a time advantage with respect to other participants.

###### Remark 2.2.

Based on the random arrivals of market takers, there is (at least partial) execution on the order of the agent if given that a market taker arrives at time tt the following condition is satisfied

|  |  |  |
| --- | --- | --- |
|  | ∑i=Nt−+Nt+νt+,i>∑j<ktVt+,j.\sum\_{i=N\_{t-}^{+}}^{N\_{t}^{+}}\nu\_{t}^{+,i}>\sum\_{j<k\_{t}}V\_{t}^{+,j}. |  |

Note that as soon as the buying volume of market takers reaches selling index ktk\_{t} of the agent, her order gets (at least partially) executed.

The number of executed shares at time tt of the agent is then given by

|  |  |  |
| --- | --- | --- |
|  | Et=max⁡(0,min⁡(vt,∑i=Nt−+Nt+νt+,i−∑j<δtVt+,j)).E\_{t}=\max\left(0,\min\left(v\_{t},\sum\_{i=N\_{t-}^{+}}^{N\_{t}^{+}}\nu\_{t}^{+,i}-\sum\_{j<{\delta\_{t}}}V\_{t}^{+,j}\right)\right). |  |

We recall that EtE\_{t} is a random variable since vtv\_{t} and Vt+,jV\_{t}^{+,j} are random. The inventory of the agent between tt and t+Δ​tt+\Delta t is It+Δ​t=It−EtI\_{t+\Delta t}=I\_{t}-E\_{t} for t∈[0,τop)t\in[0,\tau^{\mathrm{op}}) and some Δ​t>0\Delta t>0.

Motivated by the reinforcement learning approach, we assume that the agent will trade during this session until a fixed deterministic time tn<τopt\_{n}<\tau^{\mathrm{op}} before the market switch to the closing auction phase, where nn denotes the number of operations made by the agent along the CLOB session.

#### 2.1.2 Trading during the auction phase [τop,τcl)[\tau^{\mathrm{op}},\tau^{\mathrm{cl}})

At time τop\tau^{\mathrm{op}}, the system transitions to an auction, opened by the exchange. Similarly to [[18](https://arxiv.org/html/2601.17247v1#bib.bib38 "AHEAD: ad hoc electronic auction design"), [40](https://arxiv.org/html/2601.17247v1#bib.bib48 "Clearing time randomization and transaction fees for auction market design")] and motivated by the reinforcement learning approach with the Markov Decision Process modeling the agent interacting with the market, we assume that the agent is setting bids at deterministic fixed time along the auction duration.

###### Assumption 3.

The agent bids along the auction at discrete times τop=tn+1<⋯<tm<τcl\tau^{\mathrm{op}}=t\_{n+1}<\dots<t\_{m}<\tau^{\mathrm{cl}}.

The inventory IτopI\_{\tau^{\mathrm{op}}} of the agent remaining from the continuous phase, i.e. that has not been liquidated, is then traded on this auction. More precisely, for all t∈{tn+1,…,tm}t\in\{t\_{n+1},\dots,t\_{m}\}, the agent observes exogenous market and limit orders arriving on the auction. Market orders are composed by a certain volume to be bought/sold no matter the price is set at the clearing time by the exchange, while limit orders are set along the auction through a supply function (functional volume to sell/buy below/above a certain price). Every market participant can cancel prior orders, unlike in the continuous trading phase. The agent chooses an action, which will be a limit order to submit, and/or the cancellation of a previous order. In this sense, the agent reacts to the environment (since he posts his order after seeing the orders of other market participants). After his final action at the terminal trading time tm<τclt\_{m}<\tau^{\mathrm{cl}}, the system transitions to a final state that will allow to compute the clearing price and the exchanged volume, thus allows to compute the terminal reward of the agent. Exogenous market participants do not modify their offers from tmt\_{m} to τcl\tau^{\mathrm{cl}}. Solely the agent can cancel his older orders and submit a final limit order. Similarly to [[20](https://arxiv.org/html/2601.17247v1#bib.bib39 "Welfare and optimal trading frequency in dynamic double auctions"), [51](https://arxiv.org/html/2601.17247v1#bib.bib60 "Optimal auction duration: a price formation viewpoint"), [41](https://arxiv.org/html/2601.17247v1#bib.bib49 "Optimal rebate design: incentives, competition and efficiency in auction markets")] we assume that the agent submit a linear supply curve to the auction stated in the following assumption.

###### Assumption 4.

The agent has a linear supply curve Σt:p∈α​ℕ⟼Kta​(p−Sta)\Sigma\_{t}:p\in\alpha\mathbb{N}\longmapsto K\_{t}^{a}(p-S\_{t}^{a}) for all t≥τopt\geq\tau^{\mathrm{op}}, where Kta≥0K\_{t}^{a}\geq 0 and Sta∈α​ℕS\_{t}^{a}\in\alpha\mathbb{N}.

At each tj∈{tn+1,…,tm}t\_{j}\in\{t\_{n+1},\dots,t\_{m}\} the agent controls Ktja≥0K\_{t\_{j}}^{a}\geq 0 and Stja∈α​ℕS\_{t\_{j}}^{a}\in\alpha\mathbb{N} so that Σtj​(p)\Sigma\_{t\_{j}}(p) represents the number of shares the agent is willing to sell at price pp. If Σtj​(p)≤0\Sigma\_{t\_{j}}(p)\leq 0 the agent is willing to buy at price pp or below and conversely if Σtj​(p)≥0\Sigma\_{t\_{j}}(p)\geq 0 the agent is willing to sell at price pp or above. We let the supply function unsigned, but the agent will be penalized for dealing on the wrong side i.e., as a buyer while he is supposed to be a seller, similarly to [[40](https://arxiv.org/html/2601.17247v1#bib.bib48 "Clearing time randomization and transaction fees for auction market design")].

We allow the agent to cancel her past bids at unit cost d>0d>0. Let ctj∈{0,1}m−nc\_{t\_{j}}\in\{0,1\}^{m-n} where ctj(s)=1c\_{t\_{j}}^{(s)}=1 if and only if the order at time tn+st\_{n+s} for s∈{1,…,j−1−n}s\in\{1,\ldots,j-1-n\} is canceled exactly at time tjt\_{j} for j∈{n+1,…,m}j\in\{n+1,\ldots,m\}. In particular, ctn+1=𝟎c\_{t\_{n+1}}=\mathbf{0} where 𝟎\mathbf{0} is the m−nm-n-vector with 0 components. We further set θtn=𝟎\theta\_{t\_{n}}=\mathbf{0} and define θtn+1=𝟎\theta\_{t\_{n+1}}=\mathbf{0} and θtj=θtj−1+ctj\theta\_{t\_{j}}=\theta\_{t\_{j-1}}+c\_{t\_{j}}. We write ‖ct‖1\|c\_{t}\|\_{1} the number of cancellations performed at an auction trading time time t∈{tn+1,…,tm}t\in\{t\_{n+1},\dots,t\_{m}\}. Note that t↦‖θt‖1t\mapsto\|\theta\_{t}\|\_{1} is increasing. The agent cancels only once a past order, so that we impose the constraint ctj≤𝟏−θtj−1c\_{t\_{j}}\leq\mathbf{1}-\theta\_{t\_{j-1}} (for 𝟏\mathbf{1} the m−nm-n-vector with 1 components) to ensure that if ctj(s)=1c\_{t\_{j}}^{(s)}=1 for some tn+s<tjt\_{n+s}<t\_{j}, then ctj+1(s)=0c\_{t\_{j+1}}^{(s)}=0, for s∈{1,…,m−n}s\in\{1,\ldots,m-n\}.

At each trading time t∈{tn+1,…,tm}t\in\{t\_{n+1},\dots,t\_{m}\}, the agent submits an order (Kta,Sta,ct)(K\_{t}^{a},S\_{t}^{a},c\_{t}) to the market. Note that with the definition above, ctc\_{t} has no impact on the order (Kta,Sta)(K\_{t}^{a},S\_{t}^{a}), only on orders sent at time strictly before tt. The inventory of the agent remains frozen during the auction, i.e. It=IτopI\_{t}=I\_{\tau^{\mathrm{op}}} for t<τclt<\tau^{\mathrm{cl}}.

During the auction, we suppose in addition that both exogenous market makers and market takers are present in the auction and that the agent has access to full information on their activities. At each trading time tt, the number of bids sent by exogenous market makers is denoted by MtM\_{t}. Each bid sent by these actors is a limit orders, each with volume gi,t​(p)g\_{i,t}(p), which is the supply schedule of the ii-th bid offer present at time tt for i≤Mti\leq M\_{t}. As for the agent, we assume that the other market makers are not "signed", meaning that they are willing to be either seller or buyer depending on the clearing price set by the exchange at τcl\tau^{\mathrm{cl}}.

Market takers submit market orders in the auction. Let Nt+N\_{t}^{+} (resp. Nt−N\_{t}^{-}) be the number of selling (resp. buying) market orders arrived up to time t∈{tn+1,…,tm}t\in\{t\_{n+1},\dots,t\_{m}\}. For ζ∈{+,−}\zeta\in\{+,-\}, market taker i≤Ntζi\leq N\_{t}^{\zeta} submits a volume νtζ,i\nu\_{t}^{\zeta,i}. Market takers can cancel their order along the auction, for instance, volume νtn+sζ,i\nu\_{t\_{n+s}}^{\zeta,i} can be set to zero at a time tjt\_{j} should the market maker of the ii-th bid on side ζ\zeta decide to cancel his order from time tj−1t\_{j-1} to tjt\_{j}, with i≤Ntj−1ζi\leq N\_{t\_{j-1}}^{\zeta}, for all j∈{n+1,…,m}j\in\{n+1,\dots,m\} and s∈{1,…,j−1−n}s\in\{1,\dots,j-1-n\}. If no cancellation occurs, we keep νtj−1ζ,i=νtjζ,i\nu\_{t\_{j-1}}^{\zeta,i}=\nu\_{t\_{j}}^{\zeta,i} for i≤Ntj−1ζi\leq N\_{t\_{j-1}}^{\zeta}. New market orders having arrived at time tt are thus indexed by Ntj−1ζ<i≤NtjζN\_{t\_{j-1}}^{\zeta}<i\leq N\_{t\_{j}}^{\zeta}.

#### 2.1.3 Clearing price rule and estimation along the auction

After time tmt\_{m}, the system moves into a final stage to set the clearing price of the auction. The market makers and takers can first send a last order in the auction, then the agent can still send a final limit order and/or cancel past ones. At time t=τclt=\tau^{\mathrm{cl}}, the auction matches total demand and supply to maximize the exchanged volume at a uniform clearing price SτclclS\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}. The clearing price SτclclS\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}} solves the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1Mtmgi,tm​(p)+∑s=n+1m(1−θτcl(s))​Ktsa​(p−Stsa)+∑ζ∈{+,−}∑i=1Ntmζζ​νtmζ,i=0, for ​p∈ℝ+.\sum\_{i=1}^{M\_{t\_{m}}}g\_{i,t\_{m}}(p)+\sum\_{s=n+1}^{m}\left(1-\theta\_{\tau^{\mathrm{cl}}}^{(s)}\right)K\_{t\_{s}}^{a}(p-S\_{t\_{s}}^{a})+\sum\_{\zeta\in\{+,-\}}\sum\_{i=1}^{N\_{t\_{m}}^{\zeta}}\zeta\nu\_{t\_{m}}^{\zeta,i}=0,\text{ for }p\in\mathbb{R}^{+}. |  | (1) |

Along the auction, we assume that the agent computes the projected clearing price by solving the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1Mtj−1gi,tj−1​(p)+∑s=n+1j−1(1−θtj(s))​Ktsa​(p−Stsa)+∑ζ∈{+,−}∑i=1Ntj−1ζζ​νtj−1ζ,i=0, for ​p∈ℝ+\sum\_{i=1}^{M\_{t\_{j-1}}}g\_{i,t\_{j-1}}(p)+\sum\_{s=n+1}^{j-1}\left(1-\theta\_{t\_{j}}^{(s)}\right)K\_{t\_{s}}^{a}(p-S\_{t\_{s}}^{a})+\sum\_{\zeta\in\{+,-\}}\sum\_{i=1}^{N\_{t\_{j-1}}^{\zeta}}\zeta\nu\_{t\_{j-1}}^{\zeta,i}=0,\text{ for }p\in\mathbb{R}^{+} |  | (2) |

which is the clearing price equation were the auction to close at time tj∈{tn+2,…,tm}∪{τcl}t\_{j}\in\{t\_{n+2},\ldots,t\_{m}\}\cup\{\tau^{\mathrm{cl}}\}. The estimation at time tj=τclt\_{j}=\tau^{\mathrm{cl}} corresponds to solve ([1](https://arxiv.org/html/2601.17247v1#S2.E1 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")) fitting with the exchange clearing rule. We now provide sufficient conditions on ensuring existence of a solution to equation ([2](https://arxiv.org/html/2601.17247v1#S2.E2 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")). Note that this condition is not necessary since for linear supply and demand curve for the agent there always exists a solution, see Proposition [2.1](https://arxiv.org/html/2601.17247v1#S2.Thmproposition1 "Proposition 2.1 (Linear supply curve). ‣ 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") below. This theorem is however the first one as far as we know building a quantitative clearing rule for general supply and demand curve function for an active agent in an auction.

###### Theorem 2.1 (Existence of a unique (estimated) clearing price).

Let tj∈{tn+2,…,tm}∪{τcl}t\_{j}\in\{t\_{n+2},\ldots,t\_{m}\}\cup\{\tau^{\mathrm{cl}}\}. Assume that limp→±∞gi,tj−1​(p)=±∞\lim\limits\_{p\to\pm\infty}g\_{i,t\_{j-1}}(p)=\pm\infty and p⟼gi,tj​(p)p\longmapsto g\_{i,t\_{j}}(p) is continuous and increasing for any i≤Mtj−1i\leq M\_{t\_{j-1}}. Assume moreover that one of the following condition is satisfied

* (a)

  ∑s=n+1j−1(1−θtj(s))​Ktsa=0\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}=0,
* (b)

  ∑s=n+1j−1(1−θtj(s))​Ktsa>0\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}>0 and gi,tj−1g\_{i,t\_{j-1}} are Lipschitz uniformly in ii, that is there exists a constant Ltj>0L\_{t\_{j}}>0 such that for any exogenous market maker i≤Mtj−1i\leq M\_{t\_{j-1}} we have

  |  |  |  |
  | --- | --- | --- |
  |  | |gi,tj−1​(p)−gi,tj−1​(p~)|≤Ltj​|p−p~|.|g\_{i,t\_{j-1}}(p)-g\_{i,t\_{j-1}}(\tilde{p})|\leq L\_{t\_{j}}|p-\tilde{p}|. |  |

  Let

  |  |  |  |
  | --- | --- | --- |
  |  | λtj:=Mtj−1∑s=n+1j−1(1−θtj(s))​Ktsa,\lambda\_{t\_{j}}:=\frac{M\_{t\_{j-1}}}{\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}}, |  |

  with Ltj<1λtjL\_{t\_{j}}<\frac{1}{\lambda\_{t\_{j}}}.

Then, the estimated clearing price equation ([2](https://arxiv.org/html/2601.17247v1#S2.E2 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")) admits a unique solution.

Condition (a) reflects the absence of the agent in the auction. The estimated clearing price can still be set by the agent by observing the activities of other participants. In this case, the clearing price is estimated as the equilibrium between limit orders of exogenous market makers and takers only. Condition (b) corresponds to a situation in which the agent has provided active liquidity in the auction at time tjt\_{j}.

###### Proof of Theorem [2.1](https://arxiv.org/html/2601.17247v1#S2.Thmtheorem1 "Theorem 2.1 (Existence of a unique (estimated) clearing price). ‣ 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions").

Regarding Case (a), the existence of a solution to ([2](https://arxiv.org/html/2601.17247v1#S2.E2 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")) follows directly from the properties of gi,tj−1g\_{i,t\_{j-1}} (increasing, continuous with its limit conditions). Now, consider Case (b) and suppose that the agent has sent at least one order, that is, ∑s=n+1j−1(1−θtj(s))​Ktsa>0\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}>0. Define

|  |  |  |
| --- | --- | --- |
|  | ϕ​(p)=−∑i=1Mtj−1gi,tj−1​(p)+∑ζ∈{+,−}∑i=1Ntj−1ζζ​νtj−1ζ,i−∑s=n+1j−1(1−θtj(s))​Ktsa​Stsa∑s=n+1j−1(1−θtj(s))​Ktsa.\phi(p)=-\frac{\sum\_{i=1}^{M\_{t\_{j-1}}}g\_{i,t\_{j-1}}(p)+\sum\_{\zeta\in\{+,-\}}\sum\_{i=1}^{N\_{t\_{j-1}}^{\zeta}}\zeta\nu\_{t\_{j-1}}^{\zeta,i}-\sum\_{s=n+1}^{j-1}\left(1-\theta\_{t\_{j}}^{(s)}\right)K\_{t\_{s}}^{a}S\_{t\_{s}}^{a}}{\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}}. |  |

We want to ensure the existence of a fixed point of ϕ\phi. for any price p,p~∈ℝp,\tilde{p}\in\mathbb{R} we have

|  |  |  |
| --- | --- | --- |
|  | |ϕ​(p)−ϕ​(p~)|≤∑i=1Mtj−1|gi,tj−1​(p)−gi,tj−1​(p~)|∑s=n+1j−1(1−θtj(s))​Ktsa≤λtj​Ltj​|p−p~|.|\phi(p)-\phi(\tilde{p})|\leq\frac{\sum\_{i=1}^{M\_{t\_{j-1}}}|g\_{i,t\_{j-1}}(p)-g\_{i,t\_{j-1}}(\tilde{p})|}{\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}}\leq\lambda\_{t\_{j}}L\_{t\_{j}}|p-\tilde{p}|. |  |

As soon as Ltj​λtj<1L\_{t\_{j}}\lambda\_{t\_{j}}<1, the function ϕ\phi is a contraction map on ℝ\mathbb{R}.
∎

###### Corollary 2.1.

Assume that the assumptions of Theorem [2.1](https://arxiv.org/html/2601.17247v1#S2.Thmtheorem1 "Theorem 2.1 (Existence of a unique (estimated) clearing price). ‣ 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") in the case (b) are satisfied with ∑s=n+1j−1(1−θtj(s))​Ktsa≥K¯>0\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}\geq\underline{K}>0, and moreover Mtj−1M\_{t\_{j-1}} is bounded by M¯>0\overline{M}>0. Then by choosing Ltj=(1−ε)​K¯/M¯L\_{t\_{j}}=(1-\varepsilon)\underline{K}/\overline{M}-Lipschitz with ε>0\varepsilon>0, there exists a unique clearing price solving the clearing rule ([1](https://arxiv.org/html/2601.17247v1#S2.E1 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")).

###### Proof.

The proof is a direct consequence of the definition of λt−j\lambda\_{t-j} checking that Ltj:=(1−ε)​K¯/M¯<1λtjL\_{t\_{j}}:=(1-\varepsilon)\underline{K}/\overline{M}<\frac{1}{\lambda\_{t\_{j}}}.
∎

###### Remark 2.3.

The additional condition in Corollary [2.1](https://arxiv.org/html/2601.17247v1#S2.Thmcorollary1 "Corollary 2.1. ‣ 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") is equivalent to assume that at time tjt\_{j} the agent has submitted at least one active order in the auction without canceling it before time tjt\_{j}.

Finally and as we have mentioned earlier, our clearing rule recover the one stated in [[51](https://arxiv.org/html/2601.17247v1#bib.bib60 "Optimal auction duration: a price formation viewpoint")] or [[41](https://arxiv.org/html/2601.17247v1#bib.bib49 "Optimal rebate design: incentives, competition and efficiency in auction markets")] for linear supply and demand curve as stated in the following proposition.

###### Proposition 2.1 (Linear supply curve).

Assume that gi,t​(p)=Kti​(p−Sti)g\_{i,t}(p)=K\_{t}^{i}(p-S\_{t}^{i}). Then there exists a unique clearing price solving ([1](https://arxiv.org/html/2601.17247v1#S2.E1 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")) and given by

|  |  |  |
| --- | --- | --- |
|  | p=∑i=1Mtj−1Ktj−1i​Stj−1i+∑s=n+1j−1(1−θtj(s))​Ktsa​Stsa−∑ζ∈{+,−}∑i=1Ntj−1ζζ​νtj−1ζ,i∑i=1Mtj−1Ktj−1i+∑s=n+1j−1(1−θtj(s))​Ktsa.p=\frac{\sum\_{i=1}^{M\_{t\_{j-1}}}K\_{t\_{j-1}}^{i}S\_{t\_{j-1}}^{i}+\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}S\_{t\_{s}}^{a}-\sum\_{\zeta\in\{+,-\}}\sum\_{i=1}^{N\_{t\_{j-1}}^{\zeta}}\zeta\nu\_{t\_{j-1}}^{\zeta,i}}{\sum\_{i=1}^{M\_{t\_{j-1}}}K\_{t\_{j-1}}^{i}+\sum\_{s=n+1}^{j-1}(1-\theta\_{t\_{j}}^{(s)})K\_{t\_{s}}^{a}}. |  |

From now on, we assume that such an estimated clearing price exists and given as the solution to ([1](https://arxiv.org/html/2601.17247v1#S2.E1 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")) at any time tjt\_{j} during the auction.

Note that the executed volume of the agent at the clearing time is given by

|  |  |  |
| --- | --- | --- |
|  | Zτcl=∑s=n+1m(1−θτcl(s))​Ktsa​(Sτclcl−Stsa)Z\_{\tau^{\mathrm{cl}}}=\sum\_{s=n+1}^{m}\left(1-\theta\_{\tau^{\mathrm{cl}}}^{(s)}\right)K\_{t\_{s}}^{a}\left(S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}-S\_{t\_{s}}^{a}\right) |  |

so that Iτcl=Iτop−ZτclI\_{\tau^{\mathrm{cl}}}=I\_{\tau^{\mathrm{op}}}-Z\_{\tau^{\mathrm{cl}}}. Notice that also volume that has been dealed as a buyer will get executed, although the agent is supposed to act as a seller. To account for dealing on the wrong side, the agent will be penalized by receiving a reward penalization on the volumes dealt on the wrong side to compute the objective function in the next section with the Markov Decision Process modeling.

#### 2.1.4 Projected hypothetical clearing price during the continuous session

During the continuous phase [0,τop)[0,\tau^{\mathrm{op}}), we assume that the agent is estimating the clearing price of the auction. For that purpose, the agent observes all outstanding (unexecuted) limit orders and treats them as if they were submitted to a fictitious auction, where they would be jointly matched to infer the implied clearing price. The agent is then creating a projected hypothetical clearing price HtclH\_{t}^{\mathrm{cl}} along the duration of the LOB trading before the closing auction starts. The computation is detailed in algorithm [1](https://arxiv.org/html/2601.17247v1#alg1 "Algorithm 1 ‣ 2.1.4 Projected hypothetical clearing price during the continuous session ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"), the calibration of the different characteristics of the auction prices and parameters comes from [[51](https://arxiv.org/html/2601.17247v1#bib.bib60 "Optimal auction duration: a price formation viewpoint")].

Algorithm 1  Computation of HticlH\_{t\_{i}}^{\mathrm{cl}} for ti∈⟦0,tn⟧t\_{i}\in\llbracket 0,t\_{n}\rrbracket

0: Tick size α>0\alpha>0, smoothing parameter τ∈(0,1]\tau\in(0,1], initial value H0H\_{0}

1: Initialize H0cl←H0H\_{0}^{\mathrm{cl}}\leftarrow H\_{0}

2: for i=1,…,ni=1,\dots,n do

3:  Record standing orders before time tit\_{i} by set Oi⊆(α​ℤ)×ℕO\_{i}\subseteq(\alpha\mathbb{Z})\times\mathbb{N}

4:  𝒳i←proj1⁡(Oi)/α\mathcal{X}\_{i}\leftarrow\operatorname{proj}\_{1}(O\_{i})/\alpha {Standing price levels}

5:  𝒱i←proj2⁡(Oi)\mathcal{V}\_{i}\leftarrow\operatorname{proj}\_{2}(O\_{i}) {Standing volumes}

6:  for k∈𝒳ik\in\mathcal{X}\_{i} do

7:   e^ik←1i​∑s=1i∑v∈𝒱sv​𝟏Os​((α​k,v))\hat{e}\_{i}^{k}\leftarrow\frac{1}{i}\sum\_{s=1}^{i}\sum\_{v\in\mathcal{V}\_{s}}v\mathbf{1}\_{O\_{s}}((\alpha k,v)) {Average volume available at level kk}

8:   ς^ik←1i​∑s=1i(∑v∈𝒱sv​𝟏Os​((α​k,v)))2\hat{\varsigma}\_{i}^{k}\leftarrow\frac{1}{i}\sum\_{s=1}^{i}\left(\sum\_{v\in\mathcal{V}\_{s}}v\mathbf{1}\_{O\_{s}}((\alpha k,v))\right)^{2} {Average squared volume available at level kk}

9:   K^ik←(2​e^ik−ς^ik/e^ik)​α−1\hat{K}\_{i}^{k}\leftarrow(2\hat{e}\_{i}^{k}-\hat{\varsigma}\_{i}^{k}/\hat{e}\_{i}^{k})\alpha^{-1} {Calibrated slope at level kk}

10:  end for

11:  Solve ∑k∈𝒳iK^ik​(α​k−p)=0\sum\_{k\in\mathcal{X}\_{i}}\hat{K}\_{i}^{k}(\alpha k-p)=0 for pp and denote the solution S~ti\tilde{S}\_{t\_{i}} {Clearing price rule}

12:  Hticl←Hti−1cl+τ​(S~ti−Hti−1cl)H\_{t\_{i}}^{\mathrm{cl}}\leftarrow H\_{t\_{i-1}}^{\mathrm{cl}}+\tau(\tilde{S}\_{t\_{i}}-H\_{t\_{i-1}}^{\mathrm{cl}}) {Smoothed update rule}

13: end for

###### Remark 2.4.

In Algorithm [1](https://arxiv.org/html/2601.17247v1#alg1 "Algorithm 1 ‣ 2.1.4 Projected hypothetical clearing price during the continuous session ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"), we implicitly assume OiO\_{i} to be non-empty for all i∈⟦1,τop−1⟧i\in\llbracket 1,\tau^{\mathrm{op}}-1\rrbracket which follows from Assumption [1](https://arxiv.org/html/2601.17247v1#Thmassumption1 "Assumption 1. ‣ 2.1.1 Trading during the continuous phase [0,𝜏ᵒᵖ) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"), all market orders get executed. Thus, we implicitly assume that the edge case, in which there are as many limit orders as market orders on both sides, does not occur in practice.

Finally, the agent is penalized for submitting orders below the clearing price estimate HticlH\_{t\_{i}}^{\mathrm{cl}}. This is because an order with a price below the hypothetical clearing price would tell the agent to rather wait for the auction to liquidate her shares. This penalty will be detailed in the next section as a penalization for the reward function.

## 3 Markov Decision Process and dynamic programming for optimal market making with closing auction

We now turn to the discretization of the problem. In order to well defined the Markov Decision Process associated to the market modeling, we need to enforce the following assumption for the time grid (tj)j∈⟦0,n⟧(t\_{j})\_{j\in\llbracket 0,n\rrbracket} before the closing auction’s opening.

###### Assumption 5.

For all j∈⟦1,n⟧j\in\llbracket 1,n\rrbracket and ζ∈{+,−}\zeta\in\{+,-\}, the discretization (tj)1≤j≤n(t\_{j})\_{1\leq j\leq n} satisfies Ntjζ>Ntj−1ζN\_{t\_{j}}^{\zeta}>N\_{t\_{j-1}}^{\zeta} ℙ\mathbb{P}-almost surely.

Let 𝒯={ti;i∈⟦0,τcl⟧}\mathcal{T}=\{t\_{i};\,i\in\llbracket 0,\tau^{\mathrm{cl}}\rrbracket\}. In the following, we simplify the notations by replacing tit\_{i} with the index ii for any i∈⟦0,m+1⟧i\in\llbracket 0,m+1\rrbracket so that n=τop−1n=\tau^{\mathrm{op}}-1 and m=τcl−1m=\tau^{\mathrm{cl}}-1. Note that this is an abuse of notation since the discretization has to be fixed a posteriori of the realization of NζN^{\zeta} as stated in Assumption [5](https://arxiv.org/html/2601.17247v1#Thmassumption5 "Assumption 5. ‣ 3 Markov Decision Process and dynamic programming for optimal market making with closing auction ‣ Learning Market Making with Closing Auctions"). This simplifies 𝒯\mathcal{T} to be ⟦0,m+1⟧\llbracket 0,m+1\rrbracket. During the continuous phase, the agent does not observe the market takers when he submits his orders. For t∈𝒯t\in\mathcal{T}, after taking action AtA\_{t} in state StS\_{t}, a random number of market orders arrive and imply the execution (or not) of the trader’s orders (and potentially exogenous orders). Note that by Assumption [5](https://arxiv.org/html/2601.17247v1#Thmassumption5 "Assumption 5. ‣ 3 Markov Decision Process and dynamic programming for optimal market making with closing auction ‣ Learning Market Making with Closing Auctions"), new market takers have arrived at any time tt of the continuous phase. It this ensures that any actions taken by the agent will have an impact on the market in the next state.

The market is modeled by a Markov Decision Process denoted by XX and defined for any time t∈𝒯t\in\mathcal{T} as a tuple

|  |  |  |
| --- | --- | --- |
|  | Xt=(Xt1,Xt2,Xt3,Xt4,Xt5,Xt6,Xt7,Xt8,Xt9,Xt10,Xt11,Xt12,Xt13,Xt14,Xt15,Xt16,Xt17),X\_{t}=(X\_{t}^{1},X\_{t}^{2},X\_{t}^{3},X\_{t}^{4},X\_{t}^{5},X\_{t}^{6},X\_{t}^{7},X\_{t}^{8},X\_{t}^{9},X\_{t}^{10},X\_{t}^{11},X\_{t}^{12},X\_{t}^{13},X\_{t}^{14},X\_{t}^{15},X\_{t}^{16},X\_{t}^{17}), |  |

where each attribute encodes one of the market characteristics before the choice of an actions form the market marker as detailed below.

##### State space

* •

  Inventory: Xt1=ItX\_{t}^{1}=I\_{t} represents the inventory of the market maker at time tt;
* •

  Volume executed at the clearing: Xt2=0X\_{t}^{2}=0 for t<τclt<\tau^{\mathrm{cl}} and Xτcl=ZτclX\_{\tau^{\mathrm{cl}}}=Z\_{\tau^{\mathrm{cl}}};
* •

  Hypothetical/estimated auction’s clearing price: Xt3=HtclX\_{t}^{3}=H\_{t}^{\mathrm{cl}} represents the hypothetical clearing price as defined in Section [2.1.4](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS4 "2.1.4 Projected hypothetical clearing price during the continuous session ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") during the continuous trading phase for t<τopt<\tau^{\mathrm{op}} or the estimated clearing price as defined in Section [2.1.3](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS3 "2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") as the solution to Equation ([2](https://arxiv.org/html/2601.17247v1#S2.E2 "In 2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")) during the auction trading phase for τop≤t<τcl\tau^{\mathrm{op}}\leq t<\tau^{\mathrm{cl}};
* •

  Limit order book depth: Xt4=Lt+​𝟏{0≤t≤τop−1}X\_{t}^{4}=L\_{t}^{+}\mathbf{1}\_{\{0\leq t\leq\tau^{\mathrm{op}}-1\}} and Xt5=Lt−​𝟏{0≤t≤τop−1}X\_{t}^{5}=L\_{t}^{-}\mathbf{1}\_{\{0\leq t\leq\tau^{\mathrm{op}}-1\}} represent respectively the depth in the limit order book on the ask (resp. bid) side;
* •

  Number of limit order in the auction: Xt6=Mt​𝟏{t≥τop}X\_{t}^{6}=M\_{t}\mathbf{1}\_{\{t\geq\tau^{\mathrm{op}}\}};
* •

  Number of investors in the auction: Xt7=Nt−+​𝟏{t≥τop}X\_{t}^{7}=N\_{t-}^{+}\mathbf{1}\_{\{t\geq\tau^{\mathrm{op}}\}} and Xt8=Nt−−​𝟏{t≥τop}X\_{t}^{8}=N\_{t-}^{-}\mathbf{1}\_{\{t\geq\tau^{\mathrm{op}}\}} represents respectively the number of aggressive order sent in the auction to buy (resp. sell) the asset;
* •

  Cancellation history: Xt9=θt​𝟏{t≥τop}X\_{t}^{9}=\theta\_{t}\mathbf{1}\_{\{t\geq\tau^{\mathrm{op}}\}} represent the vector of canceled orders in the auction up to time tt;
* •

  mid price: Xt10=StmidX\_{t}^{10}=S\_{t}^{\mathrm{mid}}
* •

  Volume sent by investors in the auction: Xt11=(νt+,i​𝟏{i≤Nt+}​𝟏{t≥τop})1≤i≤𝒩X\_{t}^{11}=(\nu\_{t}^{+,i}\mathbf{1}\_{\{i\leq N\_{t}^{+}\}}\mathbf{1}\_{\{t\geq\tau^{\mathrm{op}}\}})\_{1\leq i\leq\mathcal{N}} and Xt12=(νt−,i​𝟏{i≤Nt−}​𝟏{t≥τop})1≤i≤𝒩X\_{t}^{12}=(\nu\_{t}^{-,i}\mathbf{1}\_{\{i\leq N\_{t}^{-}\}}\mathbf{1}\_{\{t\geq\tau^{\mathrm{op}}\}})\_{1\leq i\leq\mathcal{N}} represent the number of aggressive orders sent in the auction to buy (resp. sell) the asset
* •

  Volume in the limit order book (ask/bid side): Xt13=(Vt+,j​𝟏{j≤Lt+}​𝟏{t≤τop−1})1≤j≤𝒩X\_{t}^{13}=(V\_{t}^{+,j}\mathbf{1}\_{\{j\leq L\_{t}^{+}\}}\mathbf{1}\_{\{t\leq\tau^{\mathrm{op}}-1\}})\_{1\leq j\leq\mathcal{N}} and Xt14=(Vt−,j​𝟏{j≤Lt−}​𝟏{t≤τop−1})1≤j≤𝒩X\_{t}^{14}=(V\_{t}^{-,j}\mathbf{1}\_{\{j\leq L\_{t}^{-}\}}\mathbf{1}\_{\{t\leq\tau^{\mathrm{op}}-1\}})\_{1\leq j\leq\mathcal{N}} are the volume existing in the limit order book on the ask and bid side at any depth
* •

  Limit order in the auction: Xt15=((Kti,Sti))1≤i≤𝒩X\_{t}^{15}=((K\_{t}^{i},S\_{t}^{i}))\_{1\leq i\leq\mathcal{N}}, with Kti=Sti=0K\_{t}^{i}=S\_{t}^{i}=0 if t≤τop−1t\leq\tau^{\mathrm{op}}-1 or i>Mti>M\_{t};
* •

  Price history in the auction: Xt16=Sa​(t)X\_{t}^{16}=S^{a}(t) where Sa​(t):=(Sτopa,…,Sta,0,…,0)S^{a}(t):=(S\_{\tau^{\mathrm{op}}}^{a},\ldots,S^{a}\_{t},0,\ldots,0) represents the vector of limit order prices submitted in the auction up to time tt;
* •

  Supply/Demand slope history: Xt17=Ka​(t)X\_{t}^{17}=K^{a}(t) where Ka​(t):=(Kτopa,…,Kta,0,…,0)K^{a}(t):=(K\_{\tau^{\mathrm{op}}}^{a},\ldots,K\_{t}^{a},0,\ldots,0) represents the slope of the limit order submitted up to time tt.

###### Remark 3.1.

We assume that all numbers of market participants are bounded by 𝒩>0\mathcal{N}>0, the limit order book depth is bounded by ℒ>0\mathcal{L}>0, all volumes are bounded by 𝒱>0\mathcal{V}>0, all prices are bounded by α​ℬ\alpha\mathcal{B} for ℬ>0\mathcal{B}>0. Furthermore, all slopes (i.e., the Ka​(t)K^{a}(t)) lie on a grid with step β\beta by β​𝒦\beta\mathcal{K} for some 𝒦>0\mathcal{K}>0.
We chose the same bound 𝒩>0\mathcal{N}>0 (resp. 𝒱>0\mathcal{V}>0) on the number of (resp. volumes submitted by) market participants for both market makers and investors during the continuous phase and the auction. While one could choose different constants for each type of market participant (for example, because investors are assumed small as per Assumption [1](https://arxiv.org/html/2601.17247v1#Thmassumption1 "Assumption 1. ‣ 2.1.1 Trading during the continuous phase [0,𝜏ᵒᵖ) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions")), we chose the bounds to be large enough to bound all quantities.

###### Remark 3.2.

Recall that the strategic market maker is assumed to submit a linear supply/demand market order of the form
Kta​(p−Sta),K\_{t}^{a}(p-S\_{t}^{a}),
into the auction, as a function of the clearing price pp at time tt. The other limit orders are characterized by general supply/demand functions
gi,t​(p)=Kti​(p−Sti),g\_{i,t}(p)=K\_{t}^{i}(p-S\_{t}^{i}),
where KtiK\_{t}^{i} and StiS\_{t}^{i} denote, respectively, the slope and the reference price of other agent ii’s order. In the case of linear supply/demand functions for the other limit orders, the state variable
Xt15:=((Kti,Sti))1≤i≤𝒩X\_{t}^{15}:=\big((K\_{t}^{i},S\_{t}^{i})\big)\_{1\leq i\leq\mathcal{N}}
collectively represents the slopes and reference prices submitted by the other market participants.

###### Remark 3.3.

Note that X16,X17X^{16},X^{17} are vectors of size m−n+1m-n+1 with 0 components after time tt. This is due to the fact that we require a fixed length on the state attribute independent of the time tt studied.

This defines the non-empty and finite state space

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒳\displaystyle\mathcal{X} | =⟦0,𝒱⟧2×(α​⟦0,ℬ⟧)×⟦0,ℒ⟧2×⟦0,𝒩⟧3×{0,1}m+2×(α​⟦0,ℬ⟧)×⟦0,𝒱⟧2​𝒩\displaystyle=\llbracket 0,\mathcal{V}\rrbracket^{2}\times(\alpha\,\llbracket 0,\mathcal{B}\rrbracket)\times\llbracket 0,\mathcal{L}\rrbracket^{2}\times\llbracket 0,\mathcal{N}\rrbracket^{3}\times\{0,1\}^{m+2}\times(\alpha\,\llbracket 0,\mathcal{B}\rrbracket)\times\llbracket 0,\mathcal{V}\rrbracket^{2\mathcal{N}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×⟦0,𝒱⟧2​ℒ×[(β​⟦0,𝒦⟧)×(α​⟦0,ℬ⟧)]𝒩×(α​⟦0,ℬ⟧)m+2×(β​⟦0,𝒦⟧)m−n\displaystyle\quad\times\llbracket 0,\mathcal{V}\rrbracket^{2\mathcal{L}}\times[(\beta\llbracket 0,\mathcal{K}\rrbracket)\times(\alpha\llbracket 0,\mathcal{B}\rrbracket)]^{\mathcal{N}}\times(\alpha\,\llbracket 0,\mathcal{B}\rrbracket)^{m+2}\times(\beta\,\llbracket 0,\mathcal{K}\rrbracket)^{m-n} |  |

##### Action space.

We now turn to the actions of the strategic market maker. Given a state vector Xt∈𝒳X\_{t}\in\mathcal{X}, we define the action vector AtA\_{t} as

|  |  |  |
| --- | --- | --- |
|  | At=(At1,At2,At3,At4,At5)A\_{t}=(A\_{t}^{1},A\_{t}^{2},A\_{t}^{3},A\_{t}^{4},A\_{t}^{5}) |  |

where each component represents a particular action.

* •

  Volume set in the limit order: At1=vt​𝟏{0≤t≤τop−1}A\_{t}^{1}=v\_{t}\mathbf{1}\_{\{0\leq t\leq\tau^{\mathrm{op}}-1\}};
* •

  Depth in the limit order book: At2=kt​𝟏{0≤t≤τop−1}A\_{t}^{2}=k\_{t}\mathbf{1}\_{\{0\leq t\leq\tau^{\mathrm{op}}-1\}};
* •

  Supply/demand slope and reference price: At3=Kta​𝟏{τop≤t≤τcl−1}A\_{t}^{3}=K\_{t}^{a}\mathbf{1}\_{\{\tau^{\mathrm{op}}\leq t\leq\tau^{\mathrm{cl}}-1\}};
  and At4=Sta​𝟏{τop≤t≤τcl−1}A\_{t}^{4}=S\_{t}^{a}\mathbf{1}\_{\{\tau^{\mathrm{op}}\leq t\leq\tau^{\mathrm{cl}}-1\}}
* •

  Order cancellation in the auction: At5=ct​𝟏{τop≤t≤τcl−1}A\_{t}^{5}=c\_{t}\mathbf{1}\_{\{\tau^{\mathrm{op}}\leq t\leq\tau^{\mathrm{cl}}-1\}}.

This defines the action space 𝒜\mathcal{A} as

|  |  |  |
| --- | --- | --- |
|  | 𝒜=⟦0,𝒱⟧×⟦0,ℒ⟧×(β​⟦0,𝒦⟧)×(α​⟦0,ℬ⟧)×{0,1}τcl\mathcal{A}=\llbracket 0,\mathcal{V}\rrbracket\times\llbracket 0,\mathcal{L}\rrbracket\times(\beta\,\llbracket 0,\mathcal{K}\rrbracket)\times(\alpha\,\llbracket 0,\mathcal{B}\rrbracket)\times\{0,1\}^{\tau^{\mathrm{cl}}} |  |

Recalling that on the limit order book the market maker is liquidating his inventory, hence submits a volume At1≤It=Xt1A\_{t}^{1}\leq I\_{t}=X\_{t}^{1}, at a price α​At2≥Stmid\alpha A\_{t}^{2}\geq S\_{t}^{\mathrm{mid}}. During the auction phase, the market makers can cancel previous orders exactly once, thus At5≤𝟏−θt=1−Xt9A\_{t}^{5}\leq\mathbf{1}-\theta\_{t}=1-X\_{t}^{9}.

###### Definition 3.1 (Admissible actions).

Given a state xx, the set Adm⁡(x)\operatorname{Adm}(x) of admissible actions is defined as

|  |  |  |
| --- | --- | --- |
|  | Adm⁡(x)={a∈𝒜:a1≤x1,a2≥x10​α−1,a5≤𝟏−x9}\operatorname{Adm}(x)=\{a\in\mathcal{A}:a^{1}\leq x^{1},a^{2}\geq x^{10}\alpha^{-1},a^{5}\leq\mathbf{1}-x^{9}\} |  |

###### Definition 3.2 (Admissible policies).

An admissible policy is a map π:x∈𝒳↦π(⋅|x)∈𝒫(Adm(x))\pi\colon x\in\mathcal{X}\mapsto\pi(\cdot|x)\in\mathcal{P}(\operatorname{Adm}(x)), where 𝒫​(Adm⁡(x))\mathcal{P}(\operatorname{Adm}(x)) is the set of probability measures over Adm⁡(x)\operatorname{Adm}(x). We denote Π\Pi the set of these admissible policies. We define the set of greedy policy by the set of map π:𝒳⟶𝒜\pi:\mathcal{X}\longrightarrow\mathcal{A} denoted by Πg\Pi^{g}.

##### Reward.

We define the reward on three separated region as explained below.

1. 1.

   During the continuous trading session for t<τopt<\tau^{\mathrm{op}}. The market maker submit a price St∙=α​At2S\_{t}^{\bullet}=\alpha A\_{t}^{2}. The volume executed is given by EtE\_{t}. The profit is thus given by α​At2×Et\alpha A\_{t}^{2}\times E\_{t}. We moreover assume that the market maker penalizes the execution by comparing the price executed with the hypothetical clearing price Htcl=Xt3H\_{t}^{\mathrm{cl}}=X\_{t}^{3}. If St∙>HtclS\_{t}^{\bullet}>H\_{t}^{\mathrm{cl}}, the market maker receives the full profit otherwise if St∙<HtclS\_{t}^{\bullet}<H\_{t}^{\mathrm{cl}} the market maker may regret the execution. We assume that the difference between X3X^{3} and S∙S^{\bullet} tolerated is given by k⋆​αk^{\star}\alpha for some k⋆k^{\star} fixed. It means that as soon as

   |  |  |  |
   | --- | --- | --- |
   |  | |Htcl−St∙|≤k⋆​α,|H\_{t}^{\mathrm{cl}}-S\_{t}^{\bullet}|\leq k^{\star}\alpha, |  |

   the market maker still get a profit from the execution on the limit order. We thus introduce a penalty function fc:ℝ⟶ℝf^{c}:\mathbb{R}\longrightarrow\mathbb{R} convex, continuous and increasing such that fcf^{c} is zero on ℝ−\mathbb{R}\_{-}, such that the reward of the market maker is given by

   |  |  |  |
   | --- | --- | --- |
   |  | rt​(Xt,At)=St∙​Et​fc​(k⋆​α−(Htcl−St∙)).r\_{t}(X\_{t},A\_{t})=S\_{t}^{\bullet}E\_{t}f^{c}(k^{\star}\alpha-(H\_{t}^{\mathrm{cl}}-S\_{t}^{\bullet})). |  |
2. 2.

   During the auction trading session for τop≤t<τcl\tau^{\mathrm{op}}\leq t<\tau^{\mathrm{cl}}. The market maker submits a slope Kta=At3K\_{t}^{a}=A\_{t}^{3} and a price Sta=At4S\_{t}^{a}=A\_{t}^{4}. The agent receives a fictive reward Kta​Htcl​(Htcl−Sta)K\_{t}^{a}H\_{t}^{\mathrm{cl}}(H\_{t}^{\mathrm{cl}}-S\_{t}^{a}), where HtclH\_{t}^{\mathrm{cl}} is the anticipated clearing price (were the auction to close at time tt. The agent is penalized for canceling previous orders at cost dd per cancellation, yielding a penalty −d​‖ct‖1-d\|c\_{t}\|\_{1}. Finally, the agent is penalized for dealing as a buyer while he is supposed to be a seller. This happens when Htcl≤StaH\_{t}^{\mathrm{cl}}\leq S\_{t}^{a}: the market maker is willing to buy Kta​(Sta−Htcl)K\_{t}^{a}(S\_{t}^{a}-H\_{t}^{\mathrm{cl}}) shares at price HtclH\_{t}^{\mathrm{cl}} or below. We introduce a penalty function fa:ℝ⟶ℝf^{a}:\mathbb{R}\longrightarrow\mathbb{R} concave, continuous and increasing such that faf^{a} is zero on ℝ+\mathbb{R}\_{+}, such that the penalty writes fa​(Kta​Htcl​(Htcl−Sta))f^{a}(K\_{t}^{a}H\_{t}^{\mathrm{cl}}(H\_{t}^{\mathrm{cl}}-S\_{t}^{a})). The reward of the market maker is given by

   |  |  |  |
   | --- | --- | --- |
   |  | rt​(Xt,At)=Kta​Htcl​(Htcl−Sta)+fa​(Kta​Htcl​(Htcl−Sta))−d​‖ct‖1.r\_{t}(X\_{t},A\_{t})=K\_{t}^{a}H\_{t}^{\mathrm{cl}}(H\_{t}^{\mathrm{cl}}-S\_{t}^{a})+f^{a}(K\_{t}^{a}H\_{t}^{\mathrm{cl}}(H\_{t}^{\mathrm{cl}}-S\_{t}^{a}))-d\|c\_{t}\|\_{1}. |  |
3. 3.

   Final reward at the clearing for t=τclt=\tau^{\mathrm{cl}}. At the clearing time, the clearing price SτclclS\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}} is determined and order get matched. The market maker makes the profit or loss

   |  |  |  |
   | --- | --- | --- |
   |  | ∑s=n+1m[Ktsa​Sτclcl​(Sτclcl−Stsa)​(1−θτcl(s))]\sum\_{s=n+1}^{m}\left[K\_{t\_{s}}^{a}S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}\left(S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}-S\_{t\_{s}}^{a}\right)\left(1-\theta\_{\tau^{\mathrm{cl}}}^{(s)}\right)\right] |  |

   based on the orders he sent to the market and did not cancel by the clearing time. The agent is furthermore penalized for holding inventory. We introduce λ>0\lambda>0 as a penalization parameter. Furthermore, the agent is again penalized for wrong-side dealing. The final reward of the market maker is given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | rt​(Xt,At)\displaystyle r\_{t}(X\_{t},A\_{t}) | =∑s=n+1m[Ktsa​Sτclcl​(Sτclcl−Stsa)​(1−θτcl(s))]−λ​|Iτcl|2\displaystyle=\sum\_{s=n+1}^{m}\left[K\_{t\_{s}}^{a}S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}\left(S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}-S\_{t\_{s}}^{a}\right)\left(1-\theta\_{\tau^{\mathrm{cl}}}^{(s)}\right)\right]-\lambda|I\_{\tau^{\mathrm{cl}}}|^{2} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +∑s=n+1mfa​(Ktsa​Sτclcl​(Sτclcl−Stsa)​(1−θτcl(s))).\displaystyle\quad+\sum\_{s=n+1}^{m}f^{a}\left(K\_{t\_{s}}^{a}S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}\left(S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}-S\_{t\_{s}}^{a}\right)\left(1-\theta\_{\tau^{\mathrm{cl}}}^{(s)}\right)\right). |  |

###### Remark 3.4.

In the numerical part we will choose fc​(t)=1k⋆​α​(t)+f^{c}(t)=\frac{1}{k^{\star}\alpha}(t)\_{+} and fa​(t)=−q​(−t)+f^{a}(t)=-q(-t)\_{+} for some q>0q>0. One can interpret the penalty as removing a fraction qq of the reward. With q=1q=1, one obtains no reward for dealing on the wrong side

To summarize, at time t∈𝒯t\in\mathcal{T} the random one-step reward is

|  |  |  |
| --- | --- | --- |
|  | rt​(Xt,At)={St∙​Et​fc​(k⋆​α−(Htcl−St∙)),if ​t<τop,Kta​Htcl​(Htcl−Sta)+fa​(Kta​Htcl​(Htcl−Sta))−d​‖ct‖1,if ​τop≤t<τcl,∑s=n+1m[Ktsa​Sτclcl​(Sτclcl−Stsa)​(1−θτcl(s))]−λ​|Iτcl|2,if ​t=τcl.+∑s=n+1mfa​(Ktsa​Sτclcl​(Sτclcl−Stsa)​(1−θτcl(s)))r\_{t}(X\_{t},A\_{t})=\begin{cases}\displaystyle S\_{t}^{\bullet}E\_{t}f^{c}(k^{\star}\alpha-(H\_{t}^{\mathrm{cl}}-S\_{t}^{\bullet})),&\text{if }t<\tau^{\mathrm{op}},\\ K\_{t}^{a}H\_{t}^{\mathrm{cl}}(H\_{t}^{\mathrm{cl}}-S\_{t}^{a})+f^{a}(K\_{t}^{a}H\_{t}^{\mathrm{cl}}(H\_{t}^{\mathrm{cl}}-S\_{t}^{a}))-d\|c\_{t}\|\_{1},&\text{if }\tau^{\mathrm{op}}\leq t<\tau^{\mathrm{cl}},\\ \sum\_{s=n+1}^{m}\left[K\_{t\_{s}}^{a}S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}\left(S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}-S\_{t\_{s}}^{a}\right)\left(1-\theta\_{\tau^{\mathrm{cl}}}^{(s)}\right)\right]-\lambda|I\_{\tau^{\mathrm{cl}}}|^{2},&\text{if }t=\tau^{\mathrm{cl}}.\\ +\sum\_{s=n+1}^{m}f^{a}\left(K\_{t\_{s}}^{a}S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}\left(S\_{\tau^{\mathrm{cl}}}^{\mathrm{cl}}-S\_{t\_{s}}^{a}\right)\left(1-\theta\_{\tau^{\mathrm{cl}}}^{(s)}\right)\right)\end{cases} |  |

In our setting, the agent chooses action AtA\_{t} in state XtX\_{t}. Then, the executed volume EtE\_{t} is randomly observed. Finally, the agent transitions into state Xt+1X\_{t+1}.

The objective function of the strategic market maker is to maximize, over all π∈Π\pi\in\Pi, the total expected reward, i.e. to solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐏)maximize\displaystyle(\mathbf{P})\quad\operatorname{maximize}\quad | J​(π)=𝔼​[∑t∈𝒯χt​rt​(Xt,At)]\displaystyle J(\pi)=\mathbb{E}\left[\sum\_{t\in\mathcal{T}}\chi^{t}r\_{t}(X\_{t},A\_{t})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | {π∈ΠX0∼μ0At∼π(⋅∣Xt),\displaystyle\left\{\begin{array}[]{ll}\pi\in\Pi\\ X\_{0}\sim\mu\_{0}\\ A\_{t}\sim\pi(\cdot\mid X\_{t})\end{array}\right., |  |

where χ∈(0,1]\chi\in(0,1] denotes a discount factor.
We also define the problem reduced to greedy policies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐏𝐠)maximize\displaystyle\mathbf{(P^{g})}\quad\operatorname{maximize}\quad | J​(π)=𝔼​[∑t∈𝒯χt​rt​(Xt,At)]\displaystyle J(\pi)=\mathbb{E}\left[\sum\_{t\in\mathcal{T}}\chi^{t}r\_{t}(X\_{t},A\_{t})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | {π∈ΠgX0∼μ0At=π​(Xt)\displaystyle\left\{\begin{array}[]{ll}\pi\in\Pi^{g}\\ X\_{0}\sim\mu\_{0}\\ A\_{t}=\pi(X\_{t})\end{array}\right. |  |

We recall that our system is finite in the sense that the number of state, actions, rewards are finite, so that we can reduce our study to greedy policy πg∈Πg\pi^{g}\in\Pi^{g}.

###### Proposition 3.1 (Theorem 6.2.10 in [[52](https://arxiv.org/html/2601.17247v1#bib.bib11 "Markov decision processes: discrete stochastic dynamic programming")]).

(𝐏)\mathbf{(P)} is equivalent to solve (𝐏𝐠)\mathbf{(P^{g})}, that is there exists a greedy policies which is optimal in the set Π\Pi.

## 4 Learning market making with closing auction in an unknown environment

In this section, we explain the numerical method used to solve (𝐏𝐠)(\mathbf{P^{g}}).

### 4.1 Problem formulation

We consider the online episodic RL setting. In this setting, the agent executes the MDP sequentially for EE episodes, each episode being of length m+2m+2 and independent each others. This leads to a total number of episode samples T=(m+2)​ET=(m+2)E. For each episode e∈⟦1,E⟧e\in\llbracket 1,E\rrbracket, an initial state x0,ex\_{0,e} is sampled. The learning process is evaluated by the cumulative regret with respect to a benchmark policy, defined as follows.

###### Definition 4.1.

Given initial states (x0,e)1≤e≤E(x\_{0,e})\_{1\leq e\leq E} that are chosen by the environment, we define the cumulative pseudo regret with respect to a benchmark policy π∘∈Πg\pi^{\circ}\in\Pi^{g} as

|  |  |  |
| --- | --- | --- |
|  | PRegret⁡(T)=∑e=1E(V0π∘​(x0,e)−V0πe​(x0,e))\operatorname{PRegret}(T)=\sum\_{e=1}^{E}(V\_{0}^{\pi^{\circ}}(x\_{0,e})-V\_{0}^{\pi^{e}}(x\_{0,e})) |  |

where T=(m+2)​ET=(m+2)E is the total number of time steps i.e. the sample size, and πe\pi^{e} is the policy at the beginning of episode ee.

###### Remark 4.1.

Note that −PRegret⁡(T)-\operatorname{PRegret}(T) corresponds to the gain the learning policy πe\pi^{e} generates compared with the benchmark policy π^\hat{\pi}.

The environment being unknown, we do not deterministically know the rewards, the initial distribution, and the transition probabilities. We will therefore use a model-free method to find the optimal policy π^\hat{\pi} maximizing JJ. The idea is to approximate the optimal Q-function Qt​(x,a)Q\_{t}(x,a), see [[61](https://arxiv.org/html/2601.17247v1#bib.bib24 "Q-learning")] defined as

|  |  |  |
| --- | --- | --- |
|  | ∀(x,a)∈𝒳×𝒜,Qt​(x,a)=𝔼π​[∑s≥tχs​rs​(Xs,As)∣Xt=x,At=a].\forall(x,a)\in\mathcal{X}\times\mathcal{A},\quad Q\_{t}(x,a)=\mathbb{E}\_{\pi}\left[\sum\_{s\geq t}\chi^{s}r\_{s}(X\_{s},A\_{s})\mid X\_{t}=x,A\_{t}=a\right]. |  |

The classical Q-learning algorithm writes as follows. Whenever a transition (xt,at,rt,xt+1)(x\_{t},a\_{t},r\_{t},x\_{t+1}) is observed, Q-learning forms a one-step target rt+Vt+1​(xt+1)r\_{t}+V\_{t+1}(x\_{t+1}) for the long-run return. The update moves the current entry Qt​(xt,at)Q\_{t}(x\_{t},a\_{t}) a fraction ηk\eta\_{k} toward this target, by reducing the temporal-difference error rt+Vt+1​(xt+1)−Qt​(xt,at)r\_{t}+V\_{t+1}(x\_{t+1})-Q\_{t}(x\_{t},a\_{t}). At time step tt in state xtx\_{t}, if action ata\_{t} is taken and yields return rtr\_{t} before moving to state xt+1x\_{t+1}, then

|  |  |  |
| --- | --- | --- |
|  | Qt​(xt,at)←(1−ηk)​Qt​(xt,at)+ηk​(rt+Vt+1​(xt+1))Q\_{t}(x\_{t},a\_{t})\leftarrow(1-\eta\_{k})Q\_{t}(x\_{t},a\_{t})+\eta\_{k}(r\_{t}+V\_{t+1}(x\_{t+1})) |  |

where kk is the number of time action ata\_{t} has been taken in state xtx\_{t} at time tt so far (one should write kt​(xt,at)k\_{t}(x\_{t},a\_{t}) for rigor). As shown in [[61](https://arxiv.org/html/2601.17247v1#bib.bib24 "Q-learning")], as soon as all the rewards rtr\_{t} are bounded, the learning rates ηk∈[0,1)\eta\_{k}\in[0,1) satisfy

|  |  |  |
| --- | --- | --- |
|  | ∑k=1+∞|ηk|=+∞and∑k=1+∞ηk2<+∞,\sum\_{k=1}^{+\infty}|\eta\_{k}|=+\infty\quad\text{and}\quad\sum\_{k=1}^{+\infty}\eta\_{k}^{2}<+\infty, |  |

then the Q-learning algorithm is converging towards the optimal Q-function Qt∗​(x,a)Q\_{t}^{\*}(x,a).

### 4.2 Neural-fitted Q-learning

The classical Q-learning algorithm would fill a table with (τcl+1)×|𝒳|×|𝒜|(\tau^{\mathrm{cl}}+1)\times|\mathcal{X}|\times|\mathcal{A}| values to approximate the optimal Q-values Qt​(x,a)Q\_{t}(x,a) for all (x,a)∈𝒳×𝒜(x,a)\in\mathcal{X}\times\mathcal{A} and t∈𝒯.t\in\mathcal{T}. Given the size of our state space, this is extremely expensive. We therefore have recourse to neural networks and Deep Q-Learning. First, we render the problem stationary by enriching the state space as 𝒳~=𝒳×𝒯∖{τcl}\tilde{\mathcal{X}}=\mathcal{X}\times\mathcal{T}\setminus\{\tau^{\mathrm{cl}}\} and by writing x~=(x,t)\tilde{x}=(x,t) for x∈𝒳x\in\mathcal{X} and t∈𝒯∖{τcl}t\in\mathcal{T}\setminus\{\tau^{\mathrm{cl}}\}. Let Q~​(x~,a)=Qt​(x,a)\tilde{Q}(\tilde{x},a)=Q\_{t}(x,a).

Deep Q-Learning consists in approximating Q~​(x~,a)\tilde{Q}(\tilde{x},a) with a neural network Q~θ​(x,a)\tilde{Q}\_{\theta}(x,a), for some weight θ∈ℝq\theta\in\mathbb{R}^{q}, where q≥1q\geq 1. Our setting is organized in two phases. While states and actions have been defined in a unified way in Section [3](https://arxiv.org/html/2601.17247v1#S3 "3 Markov Decision Process and dynamic programming for optimal market making with closing auction ‣ Learning Market Making with Closing Auctions") to formulate the MDP, they are inherently different for each phase. We therefore define a separate neural network for each phase:

|  |  |  |
| --- | --- | --- |
|  | ∀(x,a,t)∈𝒳×𝒜×𝒯∖{τcl},Q~θ​(x,t)=Q~ϕ​((x,t),a)​𝟏{t<τop}+Q~ψ​((x,t),a)​𝟏{t≥τop}\forall(x,a,t)\in\mathcal{X}\times\mathcal{A}\times\mathcal{T}\setminus\{\tau^{\mathrm{cl}}\},\quad\tilde{Q}\_{\theta}(x,t)=\tilde{Q}\_{\phi}((x,t),a)\mathbf{1}\_{\{t<\tau^{\mathrm{op}}\}}+\tilde{Q}\_{\psi}((x,t),a)\mathbf{1}\_{\{t\geq\tau^{\mathrm{op}}\}} |  |

where θ=(ϕ,ψ)\theta=(\phi,\psi) and ϕ∈ℝq1,ψ∈ℝq2\phi\in\mathbb{R}^{q\_{1}},\psi\in\mathbb{R}^{q\_{2}} and q1+q2=qq\_{1}+q\_{2}=q. The goal is to train the neural network such that Q~θ\tilde{Q}\_{\theta} approximates as good as possible the Q-function Q~\tilde{Q}. For the terminal state τcl\tau^{\mathrm{cl}}, the Q-function is given by the reward rτclr\_{\tau^{\mathrm{cl}}}, which is why we do not need to define a neural network. We then apply the classical NFQ iteration algorithm from [[55](https://arxiv.org/html/2601.17247v1#bib.bib2 "Neural fitted Q iteration–first experiences with a data efficient neural reinforcement learning method")] with ensuring junction at t=τopt=\tau^{\mathrm{op}} when the phase switch occurs.

Let us now detail how the NFQ algorithm is implemented. We denote the weights for the two neural networks as ϕ\phi and ψ\psi, corresponding to the continuous phase and the auction phase, respectively. At each timestep, in state x~\tilde{x}, the agent selects an action aa, and then receives reward rr before moving to the next state x~′\tilde{x}^{\prime}. One stores the transition (x~,a,r,x~′)(\tilde{x},a,r,\tilde{x}^{\prime}). The action aa is selected according to an exponential ε\varepsilon-greedy schedule, to balance exploration and exploitation. During episode ee, one chooses a=arg⁡maxa∈𝒜⁡Q~​(x~,a)a=\arg\max\_{a\in\mathcal{A}}\tilde{Q}(\tilde{x},a) with probability 1−ε1-\varepsilon and chooses randomly and uniformly an action of 𝒜\mathcal{A} with probability ε\varepsilon. The subsequent state x~′\tilde{x}^{\prime} is samples from the environment.

Depending on which phase the state x~\tilde{x} is in, the transition is memorized in two separate replay buffers for the CLOB phase and for the auction phase. To stabilize the learning, the NFQ algorithm holds target networks parameterized by ϕ−\phi^{-} and ψ−\psi^{-}, which are frozen copies of the weights from the previous iteration. These weights are used to compute the QQ-targets (which correspond to the values rt+Vt+1​(xt+1)r\_{t}+V\_{t+1}(x\_{t+1})). Given the transition (x~j=(xj,tj),aj,rj,x~j′)(\tilde{x}\_{j}=(x\_{j},t\_{j}),a\_{j},r\_{j},\tilde{x}\_{j}^{\prime}), the target values is computed as

|  |  |  |
| --- | --- | --- |
|  | yj=rj+χ​{0 if x~j is a terminal statemaxa′∈𝒜⁡Q~ϕ−​(x~j′,a′) if x~j′ is in the continuous phasemaxa′∈𝒜⁡Q~ψ−​(x~j′,a′) if x~j′ is in the auction phasey\_{j}=r\_{j}+\chi\left\{\begin{array}[]{ll}0&\text{ if $\tilde{x}\_{j}$ is a terminal state}\\ \max\_{a^{\prime}\in\mathcal{A}}\tilde{Q}\_{\phi^{-}}(\tilde{x}\_{j}^{\prime},a^{\prime})&\text{ if $\tilde{x}\_{j}^{\prime}$ is in the continuous phase}\\ \max\_{a^{\prime}\in\mathcal{A}}\tilde{Q}\_{\psi^{-}}(\tilde{x}\_{j}^{\prime},a^{\prime})&\text{ if $\tilde{x}\_{j}^{\prime}$ is in the auction phase}\end{array}\right. |  |

The targets are used to fit Q~ϕ​(x~j,aj)\tilde{Q}\_{\phi}(\tilde{x}\_{j},a\_{j}) and Q~ψ​(x~j,aj)\tilde{Q}\_{\psi}(\tilde{x}\_{j},a\_{j}) against yjy\_{j}. More precisely, at the end of each episode, the weights of the neural networks are updated using mini-batch stochastic gradient descent over MM epochs and batch size BB, with constant learning rate η\eta. We require that B≥N¯B\geq\underline{N} before training starts, to avoid overfitting on the first episodes, and bound B≤N¯B\leq\overline{N} for numerical simplicity. We use the Huber loss, defined as ℓ​(u)=12​u2​𝟏[−1,1]​(u)+(|u|−12)​(1−𝟏[−1,1]​(u))\ell(u)=\frac{1}{2}u^{2}\mathbf{1}\_{[-1,1]}(u)+(|u|-\frac{1}{2})(1-\mathbf{1}\_{[-1,1]}(u)) and a constant learning rate. Once all epochs for episode ee are complete, the target network is hard updated as ϕ−←ϕ\phi^{-}\leftarrow\phi.

| Symbol | Value | Comment |
| --- | --- | --- |
| η\eta | 3×10−43\times 10^{-4} | Learning rate (both nets) |
| MM | 3 | Epochs per episode |
| N¯\overline{N} | 50,000 | Maximum buffer size |
| N¯\underline{N} | 5,000 | Minimum buffer size to launch training |
| χ\chi | 0.990.99 | Discount factor |
| EE | 2,000 | Number of episodes |
| BB | 128 | Batch size |
| τ\tau | 0.95 | Smoothing parameter in Algorithm [1](https://arxiv.org/html/2601.17247v1#alg1 "Algorithm 1 ‣ 2.1.4 Projected hypothetical clearing price during the continuous session ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") |
| H0H\_{0} | 100 | Initial estimated clearing price in Algorithm [1](https://arxiv.org/html/2601.17247v1#alg1 "Algorithm 1 ‣ 2.1.4 Projected hypothetical clearing price during the continuous session ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions") |

Table 1: Neural-fitted Q-iteration parameters

###### Remark 4.2.

The replay buffers are growing with each episode. In our implementation, each episode sees a pass over the whole replay buffer for training. Hence, computations get heavier with each passing episode. There certainly is room for improvement on that point.

###### Remark 4.3.

The exponential ε\varepsilon-greedy schedule reduces the exploration parameter from 1 to 0.01 with a warm-up period of 100100 episodes.

## 5 Theoretical benchmarks

We compare the performance of our NFQ-learned policy against two different theoretical benchmarks for optimal market making. The first benchmark is adapted from the optimal market making models of Avellaneda and Stoikov [[4](https://arxiv.org/html/2601.17247v1#bib.bib64 "High-frequency trading in a limit order book")] later solved explicitly by Guéant, Lehalle and Fernandez-Tapia [[28](https://arxiv.org/html/2601.17247v1#bib.bib59 "Dealing with the inventory risk: a solution to the market making problem")]. We adapt the market making model to liquidation only and without risk aversion for the continuous phase. We then suggest an approximation allowing a straightforward application to our discrete-time setup. The second theoretical benchmark is the time weighted average price policy for the continuous phase. We adopt the same heuristic liquidation rule for the auction phase. For both benchmark, we adopt in the auction phase a heuristic liquidation rule.

### 5.1 Avellaneda-Stoikov optimal market making

In this section, we will recall the main results of [[4](https://arxiv.org/html/2601.17247v1#bib.bib64 "High-frequency trading in a limit order book")] and [[28](https://arxiv.org/html/2601.17247v1#bib.bib59 "Dealing with the inventory risk: a solution to the market making problem")], in the case where the market maker acts as a seller only. We consider the continuous phase, that is t<τopt<\tau^{\mathrm{op}} in what follows. Suppose we consider a continuous time setup, that is we work on [0,tn][0,t\_{n}], where tnt\_{n} is the last time of the continuous phase in our initial framework. The market mid price is assumed to follow an arithmetic Brownian motion d​Stmid=σ​d​Bt\mathrm{d}S\_{t}^{\mathrm{mid}}=\sigma\mathrm{d}B\_{t} with σ>0\sigma>0. We assume
that transactions have constant size Δ\Delta. For simplicity, assume Δ=1\Delta=1. The inventory process writes qt=I0−Ntaq\_{t}=I\_{0}-N\_{t}^{a}, where NaN^{a} is the point process, independent of BB, giving the cumulative number of shares sold by the market maker. Formulated initially by Avellaneda and Stoikov, we assume that the intensity of NaN^{a} depends on the spread δta=kt∙−ktmid\delta\_{t}^{a}=k\_{t}^{\bullet}-k\_{t}^{\mathrm{mid}} via the following relationship:

|  |  |  |
| --- | --- | --- |
|  | λa​(δa)=A​e−α​k​δa,\lambda^{a}(\delta^{a})=Ae^{-\alpha k\delta^{a}}, |  |

for A,k>0A,k>0. The cash process XtX\_{t} of the market maker evolves according to d​Xt=(Stmid+α​δta)​d​Nta\mathrm{d}X\_{t}=(S\_{t}^{\mathrm{mid}}+\alpha\delta\_{t}^{a})\mathrm{d}N\_{t}^{a}. Let T=tnT=t\_{n} and 𝒜~\tilde{\mathcal{A}} be the set of bounded predictable processes. The market maker optimizes

|  |  |  |
| --- | --- | --- |
|  | (𝐌)supδa∈𝒜~𝔼​[XT+qT​STmid](\mathbf{M})\quad\sup\_{\delta^{a}\in\tilde{\mathcal{A}}}\mathbb{E}\left[X\_{T}+q\_{T}S\_{T}^{\mathrm{mid}}\right] |  |

###### Proposition 5.1.

The optimal quotes solving (𝐌)(\mathbf{M}) are given by

|  |  |  |
| --- | --- | --- |
|  | δa,∗​(t,q)=1α​k​[1+ln⁡(vq​(t)vq−1​(t))],\delta^{a,\*}(t,q)=\frac{1}{\alpha k}\left[1+\ln\left(\frac{v\_{q}(t)}{v\_{q-1}(t)}\right)\right], |  |

where

|  |  |  |
| --- | --- | --- |
|  | ∀q∈⟦0,Q⟧,vq​(t)=∑j=0q(A​e−1​(T−t))jj!.\forall q\in\llbracket 0,Q\rrbracket,\quad v\_{q}(t)=\sum\_{j=0}^{q}\frac{(Ae^{-1}(T-t))^{j}}{j!}. |  |

###### Proof.

Note that (𝐌)(\mathbf{M}) corresponds to the risk-neutral market maker γ→0\gamma\to 0 in the standard optimal market making problem investigated in [[4](https://arxiv.org/html/2601.17247v1#bib.bib64 "High-frequency trading in a limit order book"), [28](https://arxiv.org/html/2601.17247v1#bib.bib59 "Dealing with the inventory risk: a solution to the market making problem")]. In this case, one proves that the problem is reduced to find the solution to the ODE system

|  |  |  |
| --- | --- | --- |
|  | vq′​(t)=−A​e−1​vq−1​(t),∀q∈⟦1,Q⟧,v\_{q}^{\prime}(t)=-Ae^{-1}v\_{q-1}(t),\quad\forall q\in\llbracket 1,Q\rrbracket, |  |

and we directly get optimal quotes from [[28](https://arxiv.org/html/2601.17247v1#bib.bib59 "Dealing with the inventory risk: a solution to the market making problem")] when γ→0\gamma\to 0 by

|  |  |  |
| --- | --- | --- |
|  | δa,∗​(t,q)=1α​k​[1+ln⁡(vq​(t)vq−1​(t))].\delta^{a,\*}(t,q)=\frac{1}{\alpha k}\left[1+\ln\left(\frac{v\_{q}(t)}{v\_{q-1}(t)}\right)\right]. |  |

We prove the result by induction. Note that v0=1v\_{0}=1. Assume now that

|  |  |  |
| --- | --- | --- |
|  | vq−1​(t)=∑j=0q−1(A​e−1​(T−t))jj!,q≥1.v\_{q-1}(t)=\sum\_{j=0}^{q-1}\frac{(Ae^{-1}(T-t))^{j}}{j!},\;q\geq 1. |  |

We compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | vq​(t)\displaystyle v\_{q}(t) | =vq​(T)−∫tTvq′​(s)​ds\displaystyle=v\_{q}(T)-\int\_{t}^{T}v\_{q}^{\prime}(s)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1+A​e−1​∫tTvq−1​(s)​ds\displaystyle=1+Ae^{-1}\int\_{t}^{T}v\_{q-1}(s)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1+A​e−1​∑j=0q−1∫tT(A​e−1​(T−s))jj!​ds\displaystyle=1+Ae^{-1}\sum\_{j=0}^{q-1}\int\_{t}^{T}\frac{(Ae^{-1}(T-s))^{j}}{j!}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1+∑j=0q−1(A​e−1)j+1j!​∫0T−tsj​ds\displaystyle=1+\sum\_{j=0}^{q-1}\frac{(Ae^{-1})^{j+1}}{j!}\int\_{0}^{T-t}s^{j}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1+∑j=0q−1(Ae−1(T−t)j+1(j+1)!\displaystyle=1+\sum\_{j=0}^{q-1}\frac{(Ae^{-1}(T-t)^{j+1}}{(j+1)!} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=0q(A​e−1​(T−t))jj!.\displaystyle=\sum\_{j=0}^{q}\frac{(Ae^{-1}(T-t))^{j}}{j!}. |  |

This completes the proof by induction.
∎

The optimal quotes δa,∗​(t,q)\delta^{a,\*}(t,q) derived above hold in continuous time. These quotes yield, at time tt and given the current inventory qq, the optimal quote price (that is Stmid+α​δa,∗​(t,q)S\_{t}^{\mathrm{mid}}+\alpha\delta^{a,\*}(t,q)). However, we work in discrete time in our setting. Therefore, if at the end of period tt, when action (vt,δt)(v\_{t},\delta\_{t}) has been submitted, mtm\_{t} shares have been sold, it can be viewed as if on [t,t+1)[t,t+1), mt/Δm\_{t}/\Delta fills occurred, all at price δa,∗​(t,q)\delta^{a,\*}(t,q). The volume to be submitted is vt=qtv\_{t}=q\_{t} in this approximation. This allows to ensure that if enough market takers come to the market, execution is not limited by the volume exposed by the market taker. The approximation is twofold: each of the fills is at price δa,∗​(t,qt)\delta^{a,\*}(t,q\_{t}) (instead of δa,∗​(s,qs)\delta^{a,\*}(s,q\_{s}) for t≤s<t+1t\leq s<t+1) and we expose the whole current inventory at any time tt. The notion of "exposed volume" does not exist in the continuous time setting because of the fixed transaction size. To conclude, the action of the market maker on the continuous phase writes (qt,δa,∗​(t,qt))(q\_{t},\delta^{a,\*}(t,q\_{t})).

###### Remark 5.1.

Note that whenever δa,∗​(t,qt)\delta^{a,\*}(t,q\_{t}) is not integer, we take the closest integer value instead.

###### Remark 5.2.

When qt=0q\_{t}=0, then δa,∗​(t,0)=(α​k)−1\delta^{a,\*}(t,0)=(\alpha k)^{-1}: if ⌊(α​k)−1⌋=0\lfloor(\alpha k)^{-1}\rfloor=0, then the price quoted will be the mid price exactly.

Once the auction opens, an inventory qτop≥0q\_{\tau^{\mathrm{op}}}\geq 0 remains. We implement the following heuristic policy. Let S~\tilde{S} be the average between the mean and the max price of executed orders during the continuous phase. The whole remaining inventory qτopq\_{\tau^{\mathrm{op}}} is put on the auction at S~\tilde{S}, with supply function g~z​(p)=z​qτop​(p−S~)+\tilde{g}\_{z}(p)=zq\_{\tau^{\mathrm{op}}}(p-\tilde{S})\_{+}. In Section [6](https://arxiv.org/html/2601.17247v1#S6 "6 Numerical simulations ‣ Learning Market Making with Closing Auctions"), we consider z=10z=10. This single order is submitted right at the beginning of the auction, and only potentially executed at the clearing time.

### 5.2 Time-weighted average price benchmark

The second benchmark is deliberately simpler. Given the current inventory qtq\_{t}, the trader submits a deterministic volume
vt=⌈qt/(T−t+1)⌉v\_{t}=\lceil q\_{t}/(T-t+1)\rceil, quoted at the best ask price, i.e. δt=1\delta\_{t}=1. This strategy corresponds to a uniform liquidation of the remaining inventory over the residual trading horizon. However, such a policy does not guarantee full liquidation during the continuous trading phase, as execution is conditional on order matching.
This benchmark coincides with the minimum-impact strategy introduced in the seminal work of Almgren and Chriss [[3](https://arxiv.org/html/2601.17247v1#bib.bib7 "Optimal execution of portfolio transactions")], which minimizes the expected implementation shortfall under market-impact considerations.
For the auction phase, we adopt exactly the same liquidation policy as in the Avellaneda–Stoikov benchmark.

## 6 Numerical simulations

This section employs the generative stochastic market model formulated in Section [2](https://arxiv.org/html/2601.17247v1#S2 "2 Market model ‣ Learning Market Making with Closing Auctions") to simulate continuous trading and closing auctions. We compare an NFQ-learned policy against the two theoretical benchmarks: Avellaneda-Stoikov (AS) strategy, see Section [5.1](https://arxiv.org/html/2601.17247v1#S5.SS1 "5.1 Avellaneda-Stoikov optimal market making ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions") and the TWAP strategy see Section [5.2](https://arxiv.org/html/2601.17247v1#S5.SS2 "5.2 Time-weighted average price benchmark ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions"). The goal of this section is to emphasize the performance of our NFQ-learned policy compared with the benchmarks. We start by generating a emulator of the CLOB followed by the closing auction. The algorithm used to generate the market mechanism is defined in Section [6.1](https://arxiv.org/html/2601.17247v1#S6.SS1 "6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") with Algorithm [2](https://arxiv.org/html/2601.17247v1#alg2 "Algorithm 2 ‣ 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions"). In Section [6.3](https://arxiv.org/html/2601.17247v1#S6.SS3 "6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") we generate mid price process values by using the rough-Heston to describe the evolution of the price of a risky asset, see [[26](https://arxiv.org/html/2601.17247v1#bib.bib8 "Volatility is rough")]. Finally, in Section [6.4](https://arxiv.org/html/2601.17247v1#S6.SS4 "6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions")
we train and test our NFQ-learned policy to find the optimal trading strategy along a trading day with historical data on December 31, 2025 for CAT, PG, GOOGL, JPM and MSFT. In both cases (generated or historical data for the stock price) we note that our learning algorithm outperform the benchmarks on the mean returns.

### 6.1 Generative stochastic market model

We now explain in details our market emulator to generate the financial market in our setting.
The algorithm is describe in Algorithm [2](https://arxiv.org/html/2601.17247v1#alg2 "Algorithm 2 ‣ 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
Not that our emulator is based on empirical studies to model some key components of our model.

Algorithm 2  Generative stochastic model

0: Parameter vector (λ0,vm,γm,V,βa,βb,V∞,ρ,U1,U2,M1,M2,p1,p2,p3,p4)(\lambda\_{0},v\_{m},\gamma\_{m},V,\beta\_{a},\beta\_{b},V\_{\infty},\rho,U\_{1},U\_{2},M\_{1},M\_{2},p\_{1},p\_{2},p\_{3},p\_{4})

1: Sample N+,N−∼PP​(λ0)N^{+},N^{-}\sim\mathrm{PP}(\lambda\_{0}) on [0,τop][0,\tau^{\mathrm{op}}]

2: Define {t^i;i∈⟦0,m⟧}\{\hat{t}\_{i};\,i\in\llbracket 0,m\rrbracket\} as t^0=0\hat{t}\_{0}=0 and

|  |  |  |
| --- | --- | --- |
|  | t^i=min⁡(max⁡(t^i−1+1,τi),τop−1)​𝟏{t^i−1<τop−1}+(τop−1)​𝟏{t^i−1≥τop−1}\hat{t}\_{i}=\min(\max(\hat{t}\_{i-1}+1,\tau\_{i}),\tau^{\mathrm{op}}-1)\mathbf{1}\_{\{\hat{t}\_{i-1}<\tau^{\mathrm{op}}-1\}}+(\tau^{\mathrm{op}}-1)\mathbf{1}\_{\{\hat{t}\_{i-1}\geq\tau^{\mathrm{op}}-1\}} |  |

with τi=max⁡(τi+,τi−)\tau\_{i}=\max(\tau\_{i}^{+},\tau\_{i}^{-}) and τiζ=inf(s≥t^i−1,Nsζ>Nt^i−1ζ)\tau\_{i}^{\zeta}=\inf\left(s\geq\hat{t}\_{i-1},\,N\_{s}^{\zeta}>N\_{\hat{t}\_{i-1}}^{\zeta}\right) for i≥1i\geq 1 and ζ∈{−,+}\zeta\in\{-,+\}.

3: for k=0,…,mk=0,\ldots,m do

4:  Sample Zt^k,ζ,i∼Pareto​(vm,γm)Z\_{\hat{t}\_{k},\zeta,i}\sim\mathrm{Pareto}(v\_{m},\gamma\_{m}) for ζ∈{+,−}\zeta\in\{+,-\} and i≤Nt^k+i\leq N\_{\hat{t}\_{k}}^{+} and let νt^kζ,i=min⁡(Zt^k,ζ,i,V)\nu\_{\hat{t}\_{k}}^{\zeta,i}=\min(Z\_{\hat{t}\_{k},\zeta,i},V)

5:  Sample Vt^kζ,1∼V∞​Beta​(βa,βb)V\_{\hat{t}\_{k}}^{\zeta,1}\sim V\_{\infty}\mathrm{Beta}(\beta\_{a},\beta\_{b}) and let Vt^kζ,j=ρ−1​Vt^kζ,j+1V\_{\hat{t}\_{k}}^{\zeta,j}=\rho^{-1}V\_{\hat{t}\_{k}}^{\zeta,j+1} for j∈⟦1,L⟧j\in\llbracket 1,L\rrbracket

6: end for

7: for k=m+1,…,nk=m+1,\ldots,n do

8:  Sample Bt^k∼ℬ​(p1)B\_{\hat{t}\_{k}}\sim\mathcal{B}(p\_{1}), Dt^k∼ℬ​(p2)D\_{\hat{t}\_{k}}\sim\mathcal{B}(p\_{2}), Jt^k+∼ℬ​(p3)J\_{\hat{t}\_{k}}^{+}\sim\mathcal{B}(p\_{3}), Jt^k−∼ℬ​(p3)J\_{\hat{t}\_{k}}^{-}\sim\mathcal{B}(p\_{3}) and Gt^k∼ℬ​(p4)G\_{\hat{t}\_{k}}\sim\mathcal{B}(p\_{4})

9:  if Bt^k=1B\_{\hat{t}\_{k}}=1 then

10:   Sample Kt^ki∼𝒰​([U1,U2])K\_{\hat{t}\_{k}}^{i}\sim\mathcal{U}([U\_{1},U\_{2}]) and St^ki∼Sτopmid+α​𝒰​(⟦M1,M2⟧)S\_{\hat{t}\_{k}}^{i}\sim S\_{\tau^{\mathrm{op}}}^{\mathrm{mid}}+\alpha\mathcal{U}(\llbracket M\_{1},M\_{2}\rrbracket) {Last belief on the mid price}

11:   New market maker (Kt^ki,St^ki)(K\_{\hat{t}\_{k}}^{i},S\_{\hat{t}\_{k}}^{i}) arrives

12:  end if

13:  if Dt^k=1D\_{\hat{t}\_{k}}=1 and at least one market maker is present then

14:   Cancel a random exogenous supply order

15:  end if

16:  for ζ∈{+,−}\zeta\in\{+,-\} do

17:   if Jt^kζ=1J\_{\hat{t}\_{k}}^{\zeta}=1 and at least one market taker is present on side ζ\zeta then

18:    Sample Zt^k,ζ∼Pareto​(vm,γm)Z\_{\hat{t}\_{k},\zeta}\sim\mathrm{Pareto}(v\_{m},\gamma\_{m}) and let νtζ=min⁡(Zt^k,ζ,V)\nu^{\zeta}\_{t}=\min(Z\_{\hat{t}\_{k},\zeta},V)

19:    New market taker arrives with volume νtζ\nu^{\zeta}\_{t}

20:   end if

21:  end for

22:  if Gt^k=1G\_{\hat{t}\_{k}}=1 then

23:   Cancel a random exogenous market order

24:  end if

25: end for

The input of our emulator are given by
(λ0,vm,γm,V,βa,βb,V∞,ρ,U1,U2,M1,M2,p1,p2,p3,p4)(\lambda\_{0},v\_{m},\gamma\_{m},V,\beta\_{a},\beta\_{b},V\_{\infty},\rho,U\_{1},U\_{2},M\_{1},M\_{2},p\_{1},p\_{2},p\_{3},p\_{4}).

* •

  λ0\lambda\_{0} represents the intensity of the counting processes N+N^{+} and N−N^{-} on the continuous phase, modeled as independent Poisson processes. The two processes are not observable for the agent during the continuous phase, but only during the auction phase. They are sampled in the first step of the algorithm.
* •

  (vm,γm)(v\_{m},\gamma\_{m}) are the parameters of the Pareto distribution modeling the volumes of the limit orders throughout the whole trading sessions. This reproduces the well-known heavy tail behavior of the density of market order size, see for example [[27](https://arxiv.org/html/2601.17247v1#bib.bib3 "Statistical properties of share volume traded in financial markets"), [23](https://arxiv.org/html/2601.17247v1#bib.bib47 "Power laws in economics and finance"), [10](https://arxiv.org/html/2601.17247v1#bib.bib46 "Power laws in economics and finance: some ideas fromphysics")]. The market model allows orders of maximum size VV: greater liquidity takers will accumulate at volume VV.
* •

  (βa,βb)(\beta\_{a},\beta\_{b}) represent the parameters of the Beta distribution modeling the first volume of the limit order book. It is similar to the Beta scaling effect described in for example [[32](https://arxiv.org/html/2601.17247v1#bib.bib43 "Market making with scaled beta policies"), [60](https://arxiv.org/html/2601.17247v1#bib.bib44 "Market making with learned beta policies")]. Note that V∞V\_{\infty} is a rescaling parameter as the Beta distribution has support [0,1][0,1]. Further volumes in the limit order book decay geometrically with parameter ρ∈(0,1]\rho\in(0,1].
* •

  (U1,U2)(U\_{1},U\_{2}) represent the bounds between which exogenous market maker sample their supply slopes from during the auction phase.
* •

  (M1,M2)(M\_{1},M\_{2}) represent the integer bounds of the price at which exogenous market makers quote during the auction phase. Exogenous market makers during the volume are assumed to be sampled as Sti∼Sτopmid+α​𝒰​(⟦M1,M2⟧)S\_{t}^{i}\sim S\_{\tau^{\mathrm{op}}}^{\mathrm{mid}}+\alpha\mathcal{U}(\llbracket M\_{1},M\_{2}\rrbracket) because the auction opening time is the last time market participants see the mid price. Note that this shape of auction price have been introduced in [[19](https://arxiv.org/html/2601.17247v1#bib.bib42 "Equilibria and incentives for illiquid auction markets")].
* •

  (p1,p2,p3,p4)(p\_{1},p\_{2},p\_{3},p\_{4}) represent the probabilities that drive the market structure during the auction phase. A new market maker arrives per step with probability p1p\_{1}, one market maker cancels his order with probability p2p\_{2}, a market taker arrives on either side with probability p3p\_{3}, and a market taker cancels his order with probability p4p\_{4}. These events are sampled using a Bernoulli distribution.

Note that all samples are done independently from each other. We do assume that the limit order book is refreshed from one time step to the next one.

Line 2 of Algorithm [2](https://arxiv.org/html/2601.17247v1#alg2 "Algorithm 2 ‣ 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") defines the time grid {t^i;i∈⟦0,m⟧}\{\hat{t}\_{i};\,i\in\llbracket 0,m\rrbracket\}. The time grid is chosen such that there is at least one market taker on either side of the market at any time t^i\hat{t}\_{i} for i∈⟦0,m⟧i\in\llbracket 0,m\rrbracket. This allows to satisfy Assumption [5](https://arxiv.org/html/2601.17247v1#Thmassumption5 "Assumption 5. ‣ 3 Markov Decision Process and dynamic programming for optimal market making with closing auction ‣ Learning Market Making with Closing Auctions"). Lines 3 to 6 describe the mechanics of the continuous phase. Lines 7 to 24 describe the mechanics of the auction phase.

For the learning process, both Q-networks (Q~ϕ\tilde{Q}\_{\phi} and Q~ψ\tilde{Q}\_{\psi}) are multi-layer perceptrons with three width-16 fully connected hidden layers and ReLU activations. To simplify computations, we pruned the state vector to Xt=(It,Htcl,Lt+,Lt−,Stmid,Vt+,1,Vt−,1)X\_{t}=(I\_{t},H\_{t}^{\mathrm{cl}},L\_{t}^{+},L\_{t}^{-},S\_{t}^{\mathrm{mid}},V\_{t}^{+,1},V\_{t}^{-,1}) for the continuous phase, and Xt=(It,Zt​𝟏{t=τcl},Htcl,Mt,Nt+,Nt−,θt,Stmid)X\_{t}=(I\_{t},Z\_{t}\mathbf{1}\_{\{t=\tau^{\mathrm{cl}}\}},H\_{t}^{\mathrm{cl}},M\_{t},N\_{t}^{+},N\_{t}^{-},\theta\_{t},S\_{t}^{\mathrm{mid}}) for the auction.

###### Remark 6.1.

The neural network structure is intentionally simple to limit computational cost, serving a primarily illustrative purpose. We still expect the model to outperform benchmarks on average but with higher variance, given the low penalty parameters and the agent’s ability to obtain fictive rewards in the closing auction.

| Symbol | Value | Comment |
| --- | --- | --- |
| τop\tau^{\mathrm{op}} | 120 | Auction opening time |
| τcl\tau^{\mathrm{cl}} | 150 | Clearing time |
| I0I\_{0} | 100 | Initial inventory |
| λ0\lambda\_{0} | 11 | Continuous phase Poisson intensity |
| vmv\_{m} | 2 | Pareto distribution scale parameter |
| γm\gamma\_{m} | 2.5 | Pareto distribution shape parameter |
| V∞V\_{\infty} | 15 | Beta distribution scaling parameter |
| βa\beta\_{a} | 2 | First Beta distribution shape parameter |
| βb\beta\_{b} | 5 | Second Beta distribution shape parameter |
| ρ\rho | 12\frac{1}{2} | Limit order book volume decay parameter |
| VV | 30 | Maximum volume admitted by the market |
| U1U\_{1} | 0.1 | Exogenous supply slope lower bound |
| U2U\_{2} | 2.0 | Exogenous supply slope upper bound |
| M1M\_{1} | 10 | Exogenous supply spread upper bound |
| M2M\_{2} | −10-10 | Exogenous supply spread lower bound |
| p1p\_{1} | 0.3 | New market maker arrival probability |
| p2p\_{2} | 0.2 | Market maker cancellation probability |
| p3p\_{3} | 0.3 | New market taker arrival probability |
| p4p\_{4} | 0.1 | Market taker cancellation probability |
| λ\lambda | 0.5 | Inventory penalty |
| qq | 1 | Wrong-side dealing penalty |
| k⋆k^{\star} | 1,000 | Tolerance |
| dd | 0.1 | Cancellation cost per unit |
| α\alpha | 0.01 | Tick size |
| β\beta | 3.33 | Tick size of grid on KaK^{a} |
| 𝒦\mathcal{K} | 10 | Upper bound on Ka/βK^{a}/\beta |

Table 2: Generative stochastic market model parameters

The numerical simulations consist in training the model over 2,000 episodes, before evaluating it on 100 independent episodes.

### 6.2 Benchmark simulations

We start by simulating the optimal strategies for the Benchmarks in Figure [1](https://arxiv.org/html/2601.17247v1#S6.F1 "Figure 1 ‣ 6.2 Benchmark simulations ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions"). On the top left, we show the evolution of the inventories for both AS and TWAP, on the top right we simulate the continuous phase limit price, on the bottom left the optimal volume submitted during the continuous phase, and on the bottom right we show the optimal slope KtK\_{t} during the auction. Note that the TWAP fails to liquidate all the inventory before the auction starts unlike the AS strategy explaining the difference of order executed in the auction between these two benchmarks.

![Refer to caption](figures/benchmark_behavior_episode_2000.png)


Figure 1: Episode 2000 for the benchmarks

### 6.3 Rough Heston model for the mid price: generative data approach

In this section, we generate data from the rough-Heston model. We consider a trading session with a 2 minute continuous phase, followed by a 30 second closing auction.

#### 6.3.1 Numerical method and parameter calibration

In the first numerical implementation, we assume that the mid price StS\_{t} follows a rough Heston model. The motivation is based on the so-called rough volatility of financial assets [[26](https://arxiv.org/html/2601.17247v1#bib.bib8 "Volatility is rough"), bäuerle2020portfolio, [1](https://arxiv.org/html/2601.17247v1#bib.bib9 "Multifactor approximation of rough volatility models")]. Consider ρ∈[−1,1]\rho\in[-1,1] a constant, S0=100S\_{0}=100 (which is the numerical value we work with in this section), V0V\_{0}, HH, θ\theta, λ\lambda and ν\nu be positive constants. Recalling [[26](https://arxiv.org/html/2601.17247v1#bib.bib8 "Volatility is rough"), [54](https://arxiv.org/html/2601.17247v1#bib.bib63 "On the discrete-time simulation of the rough heston model")], the rough Heston model writes

|  |  |  |
| --- | --- | --- |
|  | {St=S0+∫0tSs​Vs​d​(ρ​Bs+1−ρ2​Bs⟂),Vt=V0+∫0tK​(t−s)​((θ−λ​Vs)​d​s+ν​Vs​d​Bs),\begin{cases}S\_{t}&=S\_{0}+\int\_{0}^{t}S\_{s}\sqrt{V\_{s}}\mathrm{d}\big(\rho B\_{s}+\sqrt{1-\rho^{2}}B\_{s}^{\perp}\big),\\ V\_{t}&=V\_{0}+\int\_{0}^{t}K(t-s)\big((\theta-\lambda V\_{s})\mathrm{d}s+\nu\sqrt{V\_{s}}\mathrm{d}B\_{s}\big),\end{cases} |  |

where (B,B⟂)(B,B^{\perp}) are two independent Brownian motions. We used the Euler-type scheme of [[54](https://arxiv.org/html/2601.17247v1#bib.bib63 "On the discrete-time simulation of the rough heston model")] to approximate this rough Heston model. As a reminder, for the grid πn={0=t0n<⋯​tnn=T}\pi\_{n}=\{0=t\_{0}^{n}<\cdots t\_{n}^{n}=T\} (here T=τopT=\tau^{\mathrm{op}} and n=τopn=\tau^{\mathrm{op}}), we set Δ​tk+1n=tk+1n−t^kn\Delta t\_{k+1}^{n}=t\_{k+1}^{n}-\hat{t}\_{k}^{n} for k∈⟦0,n−1⟧k\in\llbracket 0,n-1\rrbracket. Then Stk=exp⁡(Ytk)S\_{t\_{k}}=\exp(Y\_{t\_{k}}) for k∈⟦0,n⟧k\in\llbracket 0,n\rrbracket where

|  |  |  |
| --- | --- | --- |
|  | {Ytk=Y0+∑i=0k−1(−12​(Vti)+​Δ​ti+1n+ρ​(Vti)+​(Bti+1−Bti)+1−ρ2​(Vti)+​(Bti+1⟂−Bti⟂)),Vtk=V0+∑i=0k−1(K​(tk−ti)​(θ−λ​(Vti)+)​Δ​ti+1n+K​(tk−ti)​ν​(Vti)+​(Bti+1−Bti)).\begin{cases}Y\_{t\_{k}}&=Y\_{0}+\sum\_{i=0}^{k-1}\big(-\frac{1}{2}(V\_{t\_{i}})\_{+}\Delta t\_{i+1}^{n}+\rho\sqrt{(V\_{t\_{i}})\_{+}}\left(B\_{{t}\_{i+1}}-B\_{{t}\_{i}}\right)+\sqrt{1-\rho^{2}}\sqrt{(V\_{t\_{i}})\_{+}}\left(B\_{{t}\_{i+1}}^{\perp}-B\_{{t}\_{i}}^{\perp}\right)\big),\\ V\_{t\_{k}}&=V\_{0}+\sum\_{i=0}^{k-1}\big(K({t}\_{k}-{t}\_{i})(\theta-\lambda(V\_{t\_{i}})\_{+})\Delta t\_{i+1}^{n}+K({t}\_{k}-{t}\_{i})\nu\sqrt{(V\_{t\_{i}})\_{+}}\left(B\_{{t}\_{i+1}}-B\_{{t}\_{i}}\big)\right).\end{cases} |  |

In numerical applications, we used H=0.1H=0.1, ρ=−0.7\rho=-0.7, V0=0.02V\_{0}=0.02, θ=0.04\theta=0.04, λ=0.3\lambda=0.3 and ν=0.3\nu=0.3 as calibrated in [[2](https://arxiv.org/html/2601.17247v1#bib.bib66 "Lifting the Heston model")]. We scaled these parameters correctly to the trading period.

Now, one may notice that the AS theoretical benchmark assumes that d​St=σ​d​Bt\mathrm{d}S\_{t}=\sigma\mathrm{d}B\_{t}, instead of the rough Heston model. In this sense, the goal of the numerical simulation is to compare how our NFQ-learned policy performs against a theoretical benchmark, without claiming optimality of this benchmark. We are in fact expecting our model to beat the benchmark (since the benchmark is only optimal for a Bachelier process for the mid price).

We calibrated the value σ\sigma by estimating the standard deviation of the mid price on the trading period. From [[4](https://arxiv.org/html/2601.17247v1#bib.bib64 "High-frequency trading in a limit order book")], we have A=λ0/γmA=\lambda\_{0}/\gamma\_{m} and k=α​Kk=\alpha K. Here, KK is the proportionality constant in the empirical relationship K​Δ​p=ln⁡(Q)K\Delta p=\ln(Q), where Δ​p\Delta p is the move in price when a market order of size QQ arrives. We did a least squares regression to determine KK, by simulating 5,000 samples of the limit order book and market orders Q∼Pareto​(vm,γm)Q\sim\mathrm{Pareto}(v\_{m},\gamma\_{m}).

#### 6.3.2 Learning performance

In Figure [2](https://arxiv.org/html/2601.17247v1#S6.F2 "Figure 2 ‣ 6.3.2 Learning performance ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") we represents on the left the loss associated with the NFQ during the training. We see that the loss during the CLOB session is stable at a low level, while the loss during the auction phase is stable then explodes starting at episode 1,000. This is explained by the fact that after episode 1,000, the loss is not stabilized yet but the NFQ discovers a strategy that outperforms both benchmarks, see Figure [2(b)](https://arxiv.org/html/2601.17247v1#S6.F2.sf2 "In Figure 2 ‣ 6.3.2 Learning performance ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") leading to a decrease of the regret and better reward.

![Refer to caption](figures/dqn_training_loss.png)


(a) Training loss

![Refer to caption](figures/dqn_vs_glft_regret.png)


(b) Regret analysis

Figure 2: Training analysis

We now represents the behavior of the generative stochastic market model and the performance of the NFQ model over the last training episode. Figure [3](https://arxiv.org/html/2601.17247v1#S6.F3 "Figure 3 ‣ 6.3.2 Learning performance ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") below shows (from the left to the right and the top to the bottom) the mid price StmidS\_{t}^{\mathrm{mid}}; the inventory ItI\_{t}; the number of executed shares EtE\_{t}; the quantity HtclH\_{t}^{\mathrm{cl}}, which, as a reminder, is the hypothetical clearing price during the continuous phase and the estimated clearing price during the auction phase; the top-of-book volumes Vt+,1V\_{t}^{+,1} and Vt−1V\_{t}^{-1}; the market order arrivals during the auction phase; the one-step reward RtR\_{t}; the cumulative reward, and the actions (vt,δt)(v\_{t},\delta\_{t}) and (Kta,Sta)(K\_{t}^{a},S\_{t}^{a}).

![Refer to caption](figures/episode_2000.png)


Figure 3: Episode 2000 for the agent

##### Financial insights.

We observe that the inventory of the market maker decays to 0 during the continuous phase, and becomes negative at the clearing time of the auction, as the order of the market taker is executed. This is illustrated by the plot of EtE\_{t}: many orders are executed during the continuous phase, while only one single volume is executed at the end of the auction phase. The estimated clearing price HtclH\_{t}^{\mathrm{cl}} is very stable during the continuous phase. It becomes more variable during the auction phase, as one approaches the clearing time, so more information is available. Finally, the auction allows the agent to obtain important rewards. While these rewards are fictive before the clearing time, even the final reward is very important (the largest reward recorder during the episode) and effectively shows that the closing auction is useful to generate reward.

#### 6.3.3 Returns and performance of the NFQ strategy

In Table [3](https://arxiv.org/html/2601.17247v1#S6.T3 "Table 3 ‣ 6.3.3 Returns and performance of the NFQ strategy ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") we illustrate the mean return, standard deviation of the return, the median return, the mean final inventory, the mean CLOB return and mean auction return for the initial NFQ (before training), AS, TWAP and final NFQ (after training). The second bottom part of the table shows a comparative performance between initial NFQ, AS, TWAP and final NFQ. The final NFQ strategy benefits from the auction trading phase to generate more profit. Note that the variance is however high, as expected and explained in Remark [6.1](https://arxiv.org/html/2601.17247v1#S6.Thmremark1 "Remark 6.1. ‣ 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions"). The final NFQ model does however outperform the two benchmarks on mean returns.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Metric | Initial NFQ | AS | TWAP | Final NFQ |
| Mean Return | 3,536.5 | 9,411.1 | 4,592.5 | 12,169.2 |
| Std Return | 18,612.0 | 1,606.9 | 3,110.4 | 16,552.4 |
| Median Return | 6,493.2 | 9,847.3 | 4,877.7 | 9,752.9 |
| Mean Final Inventory | 10.93 |  |  | 10.98 |
| Mean CLOB Reward | 8,935.7 |  |  | 8,879.1 |
| Mean Auction Reward | -5,399.2 |  |  | 3,290.1 |
| Relative Improvements (Mean Return) | | | | |
| vs Initial NFQ |  | +166.1% | +29.9% | +244.1% |
| vs AS |  |  | -51.2% | +29.3% |
| vs TWAP |  |  |  | +165.0% |

Table 3: Evaluation results on 100 episodes

### 6.4 Historical data

We now consider a trading session of a 2 hour continuous phase, followed by a 30 minute closing auction. Instead of simulating a fictive mid price, we consider realized mid price paths of stocks of the S&P500 index, from December 31, 2025 between 2:30pm and 5pm EST. We train on 1,000 episodes. All other parameters remain identical. For precision, we use the same realized price path of each asset for each episode for the training. The symbol σ^\hat{\sigma} in table [4](https://arxiv.org/html/2601.17247v1#S6.T4 "Table 4 ‣ 6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions") corresponds to the estimated volatility of each stock on the continuous session.

| Symbol | σ^\hat{\sigma} | Initial NFQ | AS | TWAP | Final NFQ | Imp. vs | Imp. vs |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Return | Return | Return | Return | AS (%) | TWAP (%) |
| CAT | 5.77×10−45.77\times 10^{-4} | 8,469.42 | 9,691.33 | 9,774.44 | 15,823.51 | +63.27% | +61.89% |
| PG | 4.10×10−44.10\times 10^{-4} | 8,225.24 | 9,537.41 | 9,713.63 | 14,743.17 | +54.58% | +51.78% |
| GOOGL | 5.90×10−45.90\times 10^{-4} | 8,473.45 | 9,808.40 | 9,933.75 | 13,905.10 | +41.77% | +39.98% |
| JPM | 5.49×10−45.49\times 10^{-4} | 8,293.70 | 9,497.72 | 9,416.98 | 12,655.13 | +33.24% | +34.39% |
| MSFT | 4.12×10−44.12\times 10^{-4} | 8,454.15 | 9,630.56 | 9,465.55 | 10,687.35 | +10.97% | +12.91% |
| Mean |  | 8,383.19 | 9,633.09 | 9,660.87 | 13,562.85 | +40.77% | +40.19% |

Table 4: Comparison of mean returns on 100 episodes

We see that the final NFQ outperforms both benchmarks on average returns. These results advocate for NFQ strategy over the classical AS or TWAP benchmark to maximize the return. We demonstrate that neural-fitted Q-learning can learn policies that outperform theoretical benchmarks on average. These findings suggest that reinforcement learning has the potential to be effective for market making in complex structures beyond simple limit order books with closing auction, as for example workup session or AHEAD mechanism [[21](https://arxiv.org/html/2601.17247v1#bib.bib41 "Size discovery"), [18](https://arxiv.org/html/2601.17247v1#bib.bib38 "AHEAD: ad hoc electronic auction design")] or sequence of periodic auctions [[42](https://arxiv.org/html/2601.17247v1#bib.bib61 "The economics of competitive bidding: a selective survey"), [39](https://arxiv.org/html/2601.17247v1#bib.bib62 "Trading mechanisms in securities markets"), [11](https://arxiv.org/html/2601.17247v1#bib.bib50 "Implementation details for frequent batch auctions: slowing down markets to the blink of an eye")].

## References

* [1]
  E. Abi Jaber and O. El Euch (2019)
  Multifactor approximation of rough volatility models.
  SIAM journal on financial mathematics 10 (2),  pp. 309–349.
  Cited by: [§6.3.1](https://arxiv.org/html/2601.17247v1#S6.SS3.SSS1.p1.8 "6.3.1 Numerical method and parameter calibration ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [2]
  E. Abi Jaber (2019)
  Lifting the Heston model.
  Quantitative finance 19 (12),  pp. 1995–2013.
  Cited by: [§6.3.1](https://arxiv.org/html/2601.17247v1#S6.SS3.SSS1.p1.22 "6.3.1 Numerical method and parameter calibration ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [3]
  R. Almgren and N. Chriss (2001)
  Optimal execution of portfolio transactions.
  Journal of Risk 3,  pp. 5–40.
  Cited by: [§5.2](https://arxiv.org/html/2601.17247v1#S5.SS2.p1.3 "5.2 Time-weighted average price benchmark ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions").
* [4]
  M. Avellaneda and S. Stoikov (2008)
  High-frequency trading in a limit order book.
  Quantitative Finance 8 (3),  pp. 217–224.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p1.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p3.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p4.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§5.1](https://arxiv.org/html/2601.17247v1#S5.SS1.1.p1.2 "Proof. ‣ 5.1 Avellaneda-Stoikov optimal market making ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions"),
  [§5.1](https://arxiv.org/html/2601.17247v1#S5.SS1.p1.12 "5.1 Avellaneda-Stoikov optimal market making ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions"),
  [§5](https://arxiv.org/html/2601.17247v1#S5.p1.1 "5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions"),
  [§6.3.1](https://arxiv.org/html/2601.17247v1#S6.SS3.SSS1.p3.9 "6.3.1 Numerical method and parameter calibration ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [5]
  B. Baldacci, P. Bergault, and O. Guéant (2021)
  Algorithmic market making for options.
  Quantitative Finance 21 (1),  pp. 85–97.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p1.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [6]
  M. Bellia, L. Pelizzon, M. G. Subrahmanyam, and D. Yuferova (2025)
  Market liquidity and competition among designated market makers.
  Management Science 71 (1),  pp. 184–201.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p1.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [7]
  T. Beysolow II (2019)
  Market making via reinforcement learning.
  In Applied Reinforcement Learning with Python: With OpenAI Gym, Tensorflow, and Keras,
   pp. 77–94.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [8]
  B. Biais and A. M. Faugeron-Crouzet (2002)
  IPO auctions: english, dutch,… french, and internet.
  Journal of Financial Intermediation 11 (1),  pp. 9–36.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p3.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [9]
  B. Biais, P. Hillion, and C. Spatt (1999)
  Price discovery and learning during the preopening period in the paris bourse.
  Journal of Political Economy 107 (6),  pp. 1218–1248.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p3.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [10]
  J. Bouchaud (2001)
  Power laws in economics and finance: some ideas fromphysics.
  Quantitative finance 1 (1),  pp. 105.
  Cited by: [2nd item](https://arxiv.org/html/2601.17247v1#S6.I1.i2.p1.3 "In 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [11]
  E. Budish, P. Cramton, and J. Shim (2014)
  Implementation details for frequent batch auctions: slowing down markets to the blink of an eye.
  American Economic Review 104 (5),  pp. 418–424.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p3.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§6.4](https://arxiv.org/html/2601.17247v1#S6.SS4.p2.1 "6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [12]
  J. Cao, D. Šiška, L. Szpruch, and T. Treetanthiploet (2024)
  Logarithmic regret in the ergodic Avellaneda-Stoikov market making model.
  arXiv preprint arXiv:2409.02025.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [13]
  A. Capponi and C. Lehalle (2023)
  Machine learning and data sciences for financial markets: a guide to contemporary practices.
   Cambridge University Press.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [14]
  R. Carmona (2022)
  The influence of economic research on financial mathematics: evidence from the last 25 years.
  Finance and Stochastics 26 (1),  pp. 85–101.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p1.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [15]
  Á. Cartea, S. Jaimungal, and J. Penalva (2015)
  Algorithmic and high-frequency trading.
   Cambridge University Press.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p1.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [16]
  N. Cesa-Bianchi, T. Cesari, R. Colomboni, L. Foscari, and V. Pathak (2024)
  Market making without regret.
  arXiv preprint arXiv:2411.13993.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [17]
  C. Cuchiero, H. Ruimeng, S. Svaluto-Ferro, X. Renyuan, et al. (2024)
  Special issue on machine learning in finance.
  Mathematical Finance 34 (2),  pp. 259–261.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [18]
  J. Derchu, P. Guillot, T. Mastrolia, and M. Rosenbaum (2024)
  AHEAD: ad hoc electronic auction design.
  Frontiers of Mathematical Finance 3 (2),  pp. 163–213.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p4.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§2.1.2](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS2.p1.1 "2.1.2 Trading during the auction phase [𝜏ᵒᵖ,𝜏^cl) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"),
  [§6.4](https://arxiv.org/html/2601.17247v1#S6.SS4.p2.1 "6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [19]
  J. Derchu, D. Kavvathas, T. Mastrolia, and M. Rosenbaum (2023)
  Equilibria and incentives for illiquid auction markets.
  arXiv preprint arXiv:2307.15805, to appear in
  Market Microstructure and Liquidity.
  Cited by: [5th item](https://arxiv.org/html/2601.17247v1#S6.I1.i5.p1.2 "In 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [20]
  S. Du and H. Zhu (2014)
  Welfare and optimal trading frequency in dynamic double auctions.
  Technical report
   National Bureau of Economic Research.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p4.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§2.1.2](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS2.p2.5 "2.1.2 Trading during the auction phase [𝜏ᵒᵖ,𝜏^cl) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions").
* [21]
  D. Duffie and H. Zhu (2017)
  Size discovery.
  The Review of Financial Studies 30 (4),  pp. 1095–1150.
  Cited by: [§6.4](https://arxiv.org/html/2601.17247v1#S6.SS4.p2.1 "6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [22]
  J. Fan, Z. Wang, Y. Xie, and Z. Yang (2020)
  A theoretical analysis of deep Q-learning.
  In Learning for dynamics and control,
   pp. 486–489.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [23]
  X. Gabaix (2009)
  Power laws in economics and finance.
  Annu. Rev. Econ. 1 (1),  pp. 255–294.
  Cited by: [2nd item](https://arxiv.org/html/2601.17247v1#S6.I1.i2.p1.3 "In 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [24]
  S. Ganesh, N. Vadori, M. Xu, H. Zheng, P. Reddy, and M. Veloso (2019)
  Reinforcement learning for market making in a multi-agent dealer market.
  arXiv preprint arXiv:1911.05892.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [25]
  B. Gašperov and Z. Kostanjčar (2021)
  Market making with signals through deep reinforcement learning.
  IEEE access 9,  pp. 61611–61622.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [26]
  J. Gatheral, T. Jaisson, and M. Rosenbaum (2022)
  Volatility is rough.
  In Commodities,
   pp. 659–690.
  Cited by: [§6.3.1](https://arxiv.org/html/2601.17247v1#S6.SS3.SSS1.p1.8 "6.3.1 Numerical method and parameter calibration ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions"),
  [§6](https://arxiv.org/html/2601.17247v1#S6.p1.1 "6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [27]
  P. Gopikrishnan, V. Plerou, X. Gabaix, and H. E. Stanley (2000)
  Statistical properties of share volume traded in financial markets.
  Physical review e 62 (4),  pp. R4493.
  Cited by: [2nd item](https://arxiv.org/html/2601.17247v1#S6.I1.i2.p1.3 "In 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [28]
  O. Guéant, C. Lehalle, and J. Fernandez-Tapia (2013)
  Dealing with the inventory risk: a solution to the market making problem.
  Mathematics and financial economics 7 (4),  pp. 477–507.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p1.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p3.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p4.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§5.1](https://arxiv.org/html/2601.17247v1#S5.SS1.1.p1.2 "Proof. ‣ 5.1 Avellaneda-Stoikov optimal market making ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions"),
  [§5.1](https://arxiv.org/html/2601.17247v1#S5.SS1.1.p1.3 "Proof. ‣ 5.1 Avellaneda-Stoikov optimal market making ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions"),
  [§5.1](https://arxiv.org/html/2601.17247v1#S5.SS1.p1.12 "5.1 Avellaneda-Stoikov optimal market making ‣ 5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions"),
  [§5](https://arxiv.org/html/2601.17247v1#S5.p1.1 "5 Theoretical benchmarks ‣ Learning Market Making with Closing Auctions").
* [29]
  O. Guéant and I. Manziuk (2019)
  Deep reinforcement learning for market making in corporate bonds: beating the curse of dimensionality.
  Applied Mathematical Finance 26 (5),  pp. 387–452.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [30]
  B. Hambly, R. Xu, and H. Yang (2023)
  Recent advances in reinforcement learning in finance.
  Mathematical Finance 33 (3),  pp. 437–503.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [31]
  S. Jantschgi (2024)
  Transaction cost (in) transparency: coasian dynamics in frequent batch auctions.
  Available at SSRN 4861066.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p4.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [32]
  J. Jerome, G. Palmer, and R. Savani (2022)
  Market making with scaled beta policies.
  In Proceedings of the Third ACM International Conference on AI in Finance,
   pp. 214–222.
  Cited by: [3rd item](https://arxiv.org/html/2601.17247v1#S6.I1.i3.p1.4 "In 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [33]
  J. Jerome, L. Sánchez-Betancourt, R. Savani, and M. Herdegen (2023)
  Mbt-gym: reinforcement learning for model-based limit order book trading.
  In Proceedings of the Fourth ACM International Conference on AI in Finance,
   pp. 619–627.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [34]
  E. Kandel, B. Rindi, and L. Bosetti (2012)
  The effect of a closing call auction on market quality and trading strategies.
  Journal of Financial Intermediation 21 (1),  pp. 23–49.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p2.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [35]
  M. Kearns and Y. Nevmyvaka (2013)
  Machine learning for market microstructure and high frequency trading.
  High frequency trading: New realities for traders, markets, and regulators 72,  pp. 1877–1901.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [36]
  A. S. Kyle (1985)
  Continuous auctions and insider trading.
  Econometrica: Journal of the Econometric Society,  pp. 1315–1335.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p1.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [37]
  L. Leal, M. Laurière, and C. Lehalle (2022)
  Learning a functional control for high-frequency finance.
  Quantitative Finance 22 (11),  pp. 1973–1987.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [38]
  A. Madhavan and V. Panchapagesan (2000)
  Price discovery in auction markets: a look inside the black box.
  The Review of Financial Studies 13 (3),  pp. 627–658.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p3.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [39]
  A. Madhavan (1992)
  Trading mechanisms in securities markets.
  the Journal of Finance 47 (2),  pp. 607–641.
  Cited by: [§6.4](https://arxiv.org/html/2601.17247v1#S6.SS4.p2.1 "6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [40]
  T. Mastrolia and T. Xu (2024)
  Clearing time randomization and transaction fees for auction market design.
  arXiv preprint arXiv:2405.09764.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p4.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§2.1.2](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS2.p1.1 "2.1.2 Trading during the auction phase [𝜏ᵒᵖ,𝜏^cl) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"),
  [§2.1.2](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS2.p3.9 "2.1.2 Trading during the auction phase [𝜏ᵒᵖ,𝜏^cl) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions").
* [41]
  T. Mastrolia and T. Xu (2025)
  Optimal rebate design: incentives, competition and efficiency in auction markets.
  arXiv preprint arXiv:2501.12591.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p4.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§2.1.2](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS2.p2.5 "2.1.2 Trading during the auction phase [𝜏ᵒᵖ,𝜏^cl) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"),
  [§2.1.3](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS3.p4.1 "2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions").
* [42]
  P. R. Milgrom (1985)
  The economics of competitive bidding: a selective survey.
  Social goals and social organization: Essays in memory of Elisha Pazner,  pp. 261–292.
  Cited by: [§6.4](https://arxiv.org/html/2601.17247v1#S6.SS4.p2.1 "6.4 Historical data ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [43]
  P. R. Milgrom (2004)
  Putting auction theory to work.
   Cambridge University Press.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p1.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [44]
  P. Milgrom (1989)
  Auctions and bidding: a primer.
  Journal of economic perspectives 3 (3),  pp. 3–22.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p1.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [45]
  P. Milgrom (2019)
  Auction market design: recent innovations.
  Annual Review of Economics 11 (1),  pp. 383–405.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p2.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [46]
  V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski, et al. (2015)
  Human-level control through deep reinforcement learning.
  nature 518 (7540),  pp. 529–533.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p2.9 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [47]
  V. Mnih (2013)
  Playing atari with deep reinforcement learning.
  arXiv preprint arXiv:1312.5602.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p2.9 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [48]
  R. Neuneier (1997)
  Enhancing Q-learning for optimal asset allocation.
  Advances in neural information processing systems 10.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [49]
  Y. Nevmyvaka, Y. Feng, and M. Kearns (2006)
  Reinforcement learning for optimized trade execution.
  In Proceedings of the 23rd international conference on Machine learning,
   pp. 673–680.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [50]
  B. Ning, F. H. T. Lin, and S. Jaimungal (2021)
  Double deep Q-learning for optimal execution.
  Applied Mathematical Finance 28 (4),  pp. 361–380.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [51]
  J. Paul, M. Thibaut, and R. Mathieu (2021)
  Optimal auction duration: a price formation viewpoint.
  Operations Research 69 (6),  pp. 1734–1745.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p4.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§2.1.1](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS1.p4.1 "2.1.1 Trading during the continuous phase [0,𝜏ᵒᵖ) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"),
  [§2.1.2](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS2.p2.5 "2.1.2 Trading during the auction phase [𝜏ᵒᵖ,𝜏^cl) ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"),
  [§2.1.3](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS3.p4.1 "2.1.3 Clearing price rule and estimation along the auction ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions"),
  [§2.1.4](https://arxiv.org/html/2601.17247v1#S2.SS1.SSS4.p1.2 "2.1.4 Projected hypothetical clearing price during the continuous session ‣ 2.1 Mathematical framework and trading phases ‣ 2 Market model ‣ Learning Market Making with Closing Auctions").
* [52]
  M. L. Puterman (2014)
  Markov decision processes: discrete stochastic dynamic programming.
   John Wiley & Sons.
  Cited by: [Proposition 3.1](https://arxiv.org/html/2601.17247v1#S3.Thmproposition1 "Proposition 3.1 (Theorem 6.2.10 in [52]). ‣ Reward. ‣ 3 Markov Decision Process and dynamic programming for optimal market making with closing auction ‣ Learning Market Making with Closing Auctions").
* [53]
  F. Raillon (2020)
  The growing importance of the closing auction in share trading volumes.
  Journal of Securities Operations & Custody 12 (2),  pp. 135–152.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p2.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [54]
  A. Richard, X. Tan, and F. Yang (2023)
  On the discrete-time simulation of the rough heston model.
  SIAM Journal on Financial Mathematics 14 (1),  pp. 223–249.
  Cited by: [§6.3.1](https://arxiv.org/html/2601.17247v1#S6.SS3.SSS1.p1.16 "6.3.1 Numerical method and parameter calibration ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions"),
  [§6.3.1](https://arxiv.org/html/2601.17247v1#S6.SS3.SSS1.p1.8 "6.3.1 Numerical method and parameter calibration ‣ 6.3 Rough Heston model for the mid price: generative data approach ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [55]
  M. Riedmiller (2005)
  Neural fitted Q iteration–first experiences with a data efficient neural reinforcement learning method.
  In European conference on machine learning,
   pp. 317–328.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p2.9 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§4.2](https://arxiv.org/html/2601.17247v1#S4.SS2.p2.12 "4.2 Neural-fitted Q-learning ‣ 4 Learning market making with closing auction in an unknown environment ‣ Learning Market Making with Closing Auctions").
* [56]
  M. Salek, D. Challet, and I. Muni Toke (2024)
  Equity auction dynamics: latent liquidity models with activity acceleration.
  Quantitative Finance 24 (10),  pp. 1381–1398.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p4.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [57]
  J. A. Sirignano (2019)
  Deep learning for limit order books.
  Quantitative Finance 19 (4),  pp. 549–570.
  Cited by: [§1.1](https://arxiv.org/html/2601.17247v1#S1.SS1.p2.1 "1.1 Reinforcement learning and market making ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [58]
  R. S. Sutton, A. G. Barto, et al.
  Reinforcement learning: an introduction.
  Vol. 1.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p2.9 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [59]
  G. Vulcano, G. Van Ryzin, and C. Maglaras (2002)
  Optimal dynamic auctions for revenue management.
  Management Science 48 (11),  pp. 1388–1407.
  Cited by: [§1.2](https://arxiv.org/html/2601.17247v1#S1.SS2.p1.1 "1.2 On the importance of (closing) auctions ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions").
* [60]
  Y. Wang, R. Savani, A. Gu, C. Mascioli, T. Turocy, and M. Wellman (2024)
  Market making with learned beta policies.
  In Proceedings of the 5th ACM International Conference on AI in Finance,
   pp. 643–651.
  Cited by: [3rd item](https://arxiv.org/html/2601.17247v1#S6.I1.i3.p1.4 "In 6.1 Generative stochastic market model ‣ 6 Numerical simulations ‣ Learning Market Making with Closing Auctions").
* [61]
  C. J. Watkins and P. Dayan (1992)
  Q-learning.
  Machine learning 8 (3),  pp. 279–292.
  Cited by: [§1.3](https://arxiv.org/html/2601.17247v1#S1.SS3.p1.1 "1.3 Methodology, contributions and financial insights ‣ 1 Introduction ‣ Learning Market Making with Closing Auctions"),
  [§4.1](https://arxiv.org/html/2601.17247v1#S4.SS1.p2.3 "4.1 Problem formulation ‣ 4 Learning market making with closing auction in an unknown environment ‣ Learning Market Making with Closing Auctions"),
  [§4.1](https://arxiv.org/html/2601.17247v1#S4.SS1.p3.17 "4.1 Problem formulation ‣ 4 Learning market making with closing auction in an unknown environment ‣ Learning Market Making with Closing Auctions").