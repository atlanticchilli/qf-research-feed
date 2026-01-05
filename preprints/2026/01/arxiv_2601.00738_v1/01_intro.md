---
authors:
- Aleksei Adadurov
- Sergey Barseghyan
- Anton Chtepine
- Antero Eloranta
- Andrei Sebyakin
- Arsenii Valitov
doc_id: arxiv:2601.00738v1
family_id: arxiv:2601.00738
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2601.00738v1
url_html: https://arxiv.org/html/2601.00738v1
venue: arXiv q-fin
version: 1
year: 2026
---

Second Thoughts: How 1-second subslots transform CEX-DEX Arbitrage on Ethereum

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Aleksei Adadurov |  | Sergey Barseghyan |  | Anton Chtepine |
| nuconstruct |  | nuconstruct |  | nuconstruct |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Antero Eloranta |  | Andrei Sebyakin |  | Arsenii Valitov |
| nuconstruct |  | nuconstruct |  | nuconstruct |

Abstract

This paper examines the impact of reducing Ethereum slot time on decentralized exchange activity, with a focus on CEX-DEX arbitrage behavior. We develop a trading model where the agent’s DEX transaction is not guaranteed to land, and the agent explicitly accounts for this execution risk when deciding whether to pursue arbitrage opportunities.

We compare agent behavior under Ethereum’s default 12-second slot time environment with a faster regime that offers 1-second subslot execution. The simulations, calibrated to Binance and Uniswap v3 data from July to September 2025, show that faster slot times increase arbitrage transaction count by 535% and trading volume by 203% on average.

The increase in CEX-DEX arbitrage activity under 1-second subslots is driven by the reduction in variance of both successful and failed trade outcomes, increasing the risk-adjusted returns and making CEX-DEX arbitrage more appealing.

Keywords: MEV, DEX arbitrage, subslots, preconfirmations, market microstructure, execution risk

## 1 Introduction

One of the most active sources of DEX volume on Ethereum is arbitrage between centralized and decentralized exchanges. The strategy is simple: when the prices between a CEX (e.g., Binance) and a DEX (e.g., Uniswap) differ, a trader can exploit such an opportunity by simultaneously buying on the cheaper venue and selling on the more expensive one, thus capturing the spread. However, this strategy is not risk-free: while the CEX leg is executed almost instantaneously, the DEX leg must wait for block inclusion, which is not guaranteed. DEX transactions can fail for multiple reasons, such as insufficient priority fees, another trader capturing the same opportunity, latency, or even the block builder censoring the transaction.

The risk of executing a DEX leg and its relationship to slot times is the focus of our paper. We model a trading agent who knows that their on-chain transaction may fail to land and who incorporates this uncertainty into their entry and exit decisions. The essence of the setup is as follows: the agent faces a known probability α\alpha of successfully executing the DEX leg, and if it fails, they must decide how to manage their resulting delta exposure.

The motivation for the paper comes from the interest in understanding how Ethereum slot time reduction would affect the largest portion of DEX volume. We consider a theoretical protocol that operates in 1-second subslots, providing a faster feedback loop for traders compared to Ethereum’s native 12-second slots. The question we address is: how does faster execution change arbitrageurs’ behavior, and what are the downstream effects on DEX activity?

Related Literature. CEX-DEX Arbitrage Empirics. A growing number of papers study the scale and structure of cross-domain arbitrage between centralized and decentralized exchanges. [[1](https://arxiv.org/html/2601.00738v1#bib.bib1)] provides a systematic analysis of CEX-DEX arbitrage on Ethereum, identifying over 157,000 arbitrage transactions between May and July 2023. Their research shows that nearly all CEX-DEX arbitrages execute at the top of blocks, confirming that these opportunities require priority access. The paper also documents significant market concentration: a single searcher (0xa69) captured 55.7% of all identified arbitrages, while beaverbuild dominated market share at 41.8%. Starting from this foundation, [[4](https://arxiv.org/html/2601.00738v1#bib.bib4)] extends the analysis to 19 months of data (from August 2023 to March 2025), estimating the total extracted value of $233.8 million across 7.2 million CEX-DEX arbitrages. Their findings reveal increasing centralization, with three searchers capturing three-quarters of both volume and extracted value, and demonstrate that searcher profitability is tightly linked to vertical integration with block builders.

The relationship between CEX-DEX arbitrage and block building competition is examined in [[3](https://arxiv.org/html/2601.00738v1#bib.bib3)] and [[5](https://arxiv.org/html/2601.00738v1#bib.bib5)]. [[3](https://arxiv.org/html/2601.00738v1#bib.bib3)] shows that CeFi-DeFi arbitrage opportunities materially alter MEV-Boost auction bid profiles, with builders who have access to CEX-DEX flow gaining decisive advantages during periods of high volatility. [[5](https://arxiv.org/html/2601.00738v1#bib.bib5)] confirms that integrated high-frequency trading builders who extract top-of-block opportunities are favored to win block auctions precisely when the price volatility is increased, contributing to the observed concentration where three builders produce 80% of all MEV-Boost blocks.

Block Time and LP Losses. The theoretical relationship between block time and arbitrage losses is formalized by the Loss-Versus-Rebalancing (LVR) framework, which predicts that LP losses scale with B​T\sqrt{BT}, where B​TBT is block time. However, [[2](https://arxiv.org/html/2601.00738v1#bib.bib2)] extends this model to incorporate transaction costs and shows that the B​T\sqrt{BT}-approximation breaks down on chains with significant base fees. Their simulations show that when transaction costs are non-trivial, LP losses depend on multiple interacting factors: base fees, swap fees, and block times, with the relative importance varying by pool characteristics.

Preconfirmations. Recent work has begun to formalize preconfirmations as a distinct service layer in Ethereum’s execution pipeline. While preconfirmations represent the closest analog to our theoretical protocol currently being researched, they differ fundamentally in scope: preconfirmations guarantee transaction inclusion but do not provide intermediate state commitments during execution. The framework in [[6](https://arxiv.org/html/2601.00738v1#bib.bib6)] introduces a fulfillment-delivery paradigm borrowed from supply-chain logistics, in which specialized fulfillers (i.e., block builders) issue real-time commitments that transactions will be included, while deliverers (i.e., validators) guarantee eventual on-chain confirmation. Within this paradigm, preconfirmations are interpreted as a tool for reducing transaction execution risk without requiring validator centralization, because economically specialized entities (e.g., builders) can provide commitments while the underlying validator set remains decentralized and compatible with solo staking.

Empirical evidence on the economic impact of preconfirmations for validators is still limited. Using early mainnet data from August 2025, [[7](https://arxiv.org/html/2601.00738v1#bib.bib7)] measures how running preconfirmation services affects realized block value and finds that, at the 75th percentile of blocks, validators with preconfirmations observe higher block value than standard validators. However, the study emphasizes that the sample is small and the results are not yet statistically significant.

An alternative line of work studies preconfirmations when validators themselves act as preconfirmation providers instead of relying on external gateway architectures. Under this assumption, [[8](https://arxiv.org/html/2601.00738v1#bib.bib8)] shows that preconfirmations create new MEV capture channels and materially alter timing games: searchers face heightened risk of early termination and therefore bid more aggressively earlier in the block auction, which in turn incentivizes earlier transaction submission. The same work argues that validators can preconfirm their own transactions to capture on-chain arbitrage and liquidation opportunities, estimating that a validator with 1% stake penetration could earn roughly $345,600 in incremental annual MEV, representing about a 25% increase—higher than the current increase from timing games that add roughly 10% to MEV revenue.

Finally, [[9](https://arxiv.org/html/2601.00738v1#bib.bib9)] analyzes whether execution preconfirmations can be made economically sustainable for proposers relative to the current MEV-Boost regime. The paper models Dependent Sub-Slot Auctions in which each preconfirmation depends on expected future block and preconfirmation value, and shows that these auctions can increase expected proposer revenue even in the absence of explicit preconfirmation-specific tips. In their design, a builder who preconfirms the Nth\text{N}^{\text{th}} transaction captures all subsequent revenue in the slot, effectively tying preconfirmation incentives to the future flow of MEV.

Our Contribution. We complement the literature in two ways. First, unlike the empirical studies that document realized arbitrage outcomes, we model the decision-making problem facing a CEX-DEX arbitrageur under execution uncertainty. This perspective reveals why observed arbitrage activity may substantially understate the latent demand for faster execution: many profitable opportunities are foregone not because they do not exist but because rational agents decline to attempt them given current confirmation times. Second, we focus on execution guarantees that can be provided without protocol-level changes, making our analysis applicable to a range of possible mechanism designs, including but not limited to preconfirmations.

Most importantly, we model a realistic trading agent who accounts for execution uncertainty. This agent does not simply attempt every profitable opportunity. Instead, they evaluate the risk-adjusted expected value of entry, considering both the probability of DEX leg failure and the costs of closing an unsuccessful position. This behavioral realism proves crucial for understanding how faster execution affects market outcomes.

Our results show that faster execution substantially increases on-chain arbitrage activity. For a risk-averse agent with 35% probability of landing the DEX leg, transaction counts increase by 535% when moving from 12-second to 1-second confirmation times. Volume increases by up to 203%.

## 2 DEX Price Interpolation

The simulation framework models the interaction between centralized and decentralized exchange prices over time. In this paper, we study the difference between confirmation intervals: under Ethereum’s default configuration, DEX transactions can be executed every 12 seconds at slot boundaries, while under faster execution regimes, transactions can be executed every second within subslots. Historical DEX prices are readily available and can be used for 12-second slot benchmark simulations. For a faster regime, we need a framework to interpolate these prices for 1-second subslots.

Our framework includes three components. First, we start with a historical price for a current slot. It is also a price for the initial subslot. Next, we derive a price pDEX​(ti)p^{\text{DEX}}(t\_{i}) of the ii-th subslot from a price pDEX​(ti−1)p^{\text{DEX}}(t\_{i-1}) of the (i−1)(i-1)-th subslot. To do this, we apply (1) arbitrage transactions from the previous slot if present, (2) CEX-DEX price reversion to model how DEX prices adjust to off-chain information between arbitrage events, and (3) noise trading to capture non-arbitrage DEX activity. Each component addresses a specific modeling challenge and, thus, we run simulations with different combinations to assess robustness.

The subslot price interpolation mechanism is depicted in [Figure 1](https://arxiv.org/html/2601.00738v1#S2.F1 "Figure 1 ‣ 2 DEX Price Interpolation"). All other market mechanics remain constant, allowing us to isolate the effect of confirmation speed.

012122424P0P\_{0}Slot nnSlot n+1n+1slotsubslotTime, tt (seconds)Price, PPCEX mid priceDEX slot priceDEX subslot price


Figure 1: Price dynamics and subslot structure within Ethereum slots. The CEX mid price (blue) updates continuously, while the DEX slot price (red) updates only at slot boundaries every 12 seconds. DEX subslot prices (green) are interpolated from the CEX price at 1-second intervals within each slot.

We use data from July to September 2025, including millisecond-level best bid and ask prices from Binance and all swap transactions from Uniswap v3 ETH-USDC pools at the 30 basis point, 5 basis point, and 1 basis point tiers.

### 2.1 Noise Trading

It is known that arbitrageurs are not the only participants trading on DEXs. Hedgers, retail users, and other non-arbitrage traders generate transaction flow that moves prices independently of CEX-DEX spreads. In order to include other market participants and avoid overstating the predictability of DEX price movements, we incorporate ”noise trading”.

We classify historical Uniswap v3 transactions as either arbitrage or noise based on their characteristics. A trade is considered arbitrage if it satisfies all of the following four conditions: (1) it is the first transaction in a block, (2) the pre-trade CEX-DEX price discrepancy exceeds the pool fee, (3) the trade moves the DEX price toward the CEX price, and (4) the post-trade price discrepancy remains equal to or above the pool fee. All other transactions are classified as noise.

From July to September 2025 data, we estimate probability distributions for both the number of noise trades per block and the price impact of individual noise trades. Price impacts are rounded to the nearest basis point, and observations with absolute impact exceeding 30 basis points are excluded as outliers. During simulation, we sample a random number of noise trades with random price impacts every 12 seconds and distribute them randomly across the DEX execution subslots.

### 2.2 CEX-DEX Price Reversion

DEX prices can be adjusted toward CEX prices through channels other than direct arbitrage. For example, informed traders may update their limit orders, or market makers may rebalance inventory. In order to capture this gradual price convergence, we implement a regression-based reversion mechanism.

The idea is to estimate how much the DEX price typically moves in response to a given CEX price change and then use this relationship to revert DEX prices to CEX between arbitrage events. Let pCEX​(t)p^{\text{CEX}}(t) and pDEX​(t)p^{\text{DEX}}(t) denote the CEX and DEX prices at time tt. Then, for consecutive timestamps ti−1t\_{i-1} and tit\_{i}, define simple returns:

|  |  |  |
| --- | --- | --- |
|  | riCEX=pCEX​(ti)−pCEX​(ti−1)pCEX​(ti−1),riDEX=pDEX​(ti)−pDEX​(ti−1)pDEX​(ti−1)r^{\text{CEX}}\_{i}=\frac{p^{\text{CEX}}(t\_{i})-p^{\text{CEX}}(t\_{i-1})}{p^{\text{CEX}}(t\_{i-1})},\quad r^{\text{DEX}}\_{i}=\frac{p^{\text{DEX}}(t\_{i})-p^{\text{DEX}}(t\_{i-1})}{p^{\text{DEX}}(t\_{i-1})} |  |

Then, we partition of the time axis into semi-open intervals Fk=(τk−1,τk]F\_{k}=(\tau\_{k-1},\tau\_{k}] and estimate a linear model within each interval:

|  |  |  |
| --- | --- | --- |
|  | riDEX=β0(k)+β1(k)​riCEX+εi,εi​∼iid​𝒩​(0,σk2)r^{\text{DEX}}\_{i}=\beta^{(k)}\_{0}+\beta^{(k)}\_{1}r^{\text{CEX}}\_{i}+\varepsilon\_{i},\quad\varepsilon\_{i}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^{2}\_{k}) |  |

The OLS estimate of the coefficients is as follows:

|  |  |  |
| --- | --- | --- |
|  | β^1(k)=∑(rCEX,rDEX)∈Fk(rCEX−r¯kCEX)​(rDEX−r¯kDEX)∑(rCEX,rDEX)∈Fk(rCEX−r¯kCEX)2,β^0(k)=r¯kDEX−β^1(k)​r¯kCEX\hat{\beta}^{(k)}\_{1}=\frac{\sum\limits\_{(r^{\text{CEX}},r^{\text{DEX}})\in F\_{k}}(r^{\text{CEX}}-\bar{r}^{\text{CEX}}\_{k})(r^{\text{DEX}}-\bar{r}^{\text{DEX}}\_{k})}{\sum\limits\_{(r^{\text{CEX}},r^{\text{DEX}})\in F\_{k}}(r^{\text{CEX}}-\bar{r}^{\text{CEX}}\_{k})^{2}},\quad\hat{\beta}^{(k)}\_{0}=\bar{r}^{\text{DEX}}\_{k}-\hat{\beta}^{(k)}\_{1}\bar{r}^{\text{CEX}}\_{k} |  |

For any timestamp tit\_{i} within interval FkF\_{k}, where the CEX price is observed but the DEX price is not yet updated, we predict:

|  |  |  |
| --- | --- | --- |
|  | r^iDEX=β^0(k)+β^1(k)​riCEX\hat{r}^{\text{DEX}}\_{i}=\hat{\beta}^{(k)}\_{0}+\hat{\beta}^{(k)}\_{1}r^{\text{CEX}}\_{i} |  |

and obtain the reverted DEX price from the most recent observed DEX price pDEX​(ti−1)p^{\text{DEX}}(t\_{i-1}):

|  |  |  |
| --- | --- | --- |
|  | p^DEX​(ti)=pDEX​(ti−1)​(1+r^iDEX)\hat{p}^{\text{DEX}}(t\_{i})=p^{\text{DEX}}(t\_{i-1})(1+\hat{r}^{\text{DEX}}\_{i}) |  |

It is also important to note that the coefficients are recalibrated at each interval boundary to allow the CEX-DEX relationship to vary over time.

## 3 Modeling the Trading Agent

CEX-DEX arbitrage exploits price discrepancies between centralized and decentralized exchanges. When the DEX price is below the CEX bid, or above the CEX ask, an arbitrageur can buy on the DEX and sell on the CEX, or vice versa, to capture the spread. The strategy, which is depicted in [Figure 2](https://arxiv.org/html/2601.00738v1#S3.F2 "Figure 2 ‣ 3 Modeling the Trading Agent"), appears straightforward, but the execution introduces significant complications.

The core risk is that the two legs of the trade are executed asynchronously. Assuming infinite liquidity and instant and guaranteed execution on Binance, the CEX leg settlement bears no risks, but the DEX leg needs to be included in a block. If the DEX transaction fails to land, due to competition from other arbitrageurs, network congestion, among other reasons, the trader is left with unhedged exposure. They have already committed to one side of the trade and must now close out the position at potentially unfavorable prices.

01212242436364848606072723,3903{,}3903,3953{,}3953,4003{,}4003,4053{,}4053,4103{,}4103,4153{,}415ArbitrageopportunityDEXupdateSlot nnSlot n+1n{+}1Slot n+2n{+}2Slot n+3n{+}3Slot n+4n{+}4Slot n+5n{+}5Time (seconds)Price (USDC per ETH)CEX mid priceDEX price

|  |
| --- |
| Buy DEX, Sell CEX |
| Buy CEX, Sell DEX |



Figure 2: The CEX-DEX arbitrage strategy over six Ethereum slots. The CEX mid price (blue line) updates continuously at millisecond frequency, while the DEX price (red line) updates only at 12-second slot boundaries following arbitrage execution. Green regions represent opportunities to buy on DEX and sell on CEX; orange regions represent the reverse direction.

We model an agent who explicitly accounts for this risk. The agent has a fixed probability α∈(0,1)\alpha\in(0,1) of successfully landing the DEX leg of any attempted arbitrage. If the leg fails, the agent must decide how to manage the resulting exposure: close immediately on the CEX, retry the DEX trade in the next slot, or wait for better conditions. This fallback logic, combined with risk-averse preferences over profit variance, determines which opportunities the agent chooses to pursue.

Throughout the paper, we consider the arbitrage strategy of buying QQ units on the DEX and selling QQ units on the CEX 111The opposite strategy of buying QQ units on the CEX and selling QQ units on the DEX has the same logic with signs flipped. When the DEX price is above the CEX ask, one would buy on CEX and sell on DEX. So, we consider the case mentioned above without loss of generality, as the other case is symmetric, and the logic remains the same.. Let pbidCEX​(t)p^{\text{CEX}}\_{\text{bid}}(t) and paskCEX​(t)p^{\text{CEX}}\_{\text{ask}}(t) denote the CEX bid and ask prices, and let pDEX​(tn)p^{\text{DEX}}(t\_{n}) denote the DEX price at slot nn, where tn=n​τt\_{n}=n\tau is the timestamp of slot nn and τ\tau is the slot duration (i.e., 12 seconds by default, 1 second under faster execution). Key parameters include the time step δ\delta (i.e., 1 second), the risk-aversion coefficient of the agent λ\lambda, and the minimum profit threshold θ\theta for the entry.

### 3.1 Simple Model

In the simple model, the agent attempts to take every detected arbitrage opportunity without regard to execution risk. When an opportunity arises, which is defined as the CEX-DEX spread exceeding the pool fee, the agent immediately submits both legs of the trade.

With probability α\alpha, the DEX leg lands successfully, and the agent captures the full arbitrage profit:

|  |  |  |
| --- | --- | --- |
|  | πs=Q​(pbidCEX​(tn)−pDEX​(tn))\pi^{s}=Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{DEX}}(t\_{n})\bigr) |  |

With probability 1−α1-\alpha, the DEX leg fails. The agent has already sold on the CEX and must now close the short position. In the simple model, we assume that the agent simply buys back on the CEX one second later, paying the ask price and crossing the spread:

|  |  |  |
| --- | --- | --- |
|  | πf=Q​(pbidCEX​(tn)−paskCEX​(tn+δ))\pi^{f}=Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{CEX}}\_{\text{ask}}(t\_{n}+\delta)\bigr) |  |

This model serves as a benchmark. In this setup, the agent’s behavior is mechanical, as they act at every opportunity, so differences between 12-second and 1-second environments reflect only the change in opportunity frequency, not any strategic adaptation.

### 3.2 Risk-Averse Model

The risk-averse model endows the agent with two capabilities absent from the simple model: selective entry based on risk-adjusted expected profit and optimal fallback decision when trades fail. In this model, we study two main mechanisms: entry decision and fallback logic.

Entry decision. The agent enters an arbitrage opportunity only if the risk-adjusted expected profit exceeds a threshold θ\theta. Let π​(tn)\pi(t\_{n}) denote the random profit from attempting arbitrage at slot nn. Hence, the expected profit is as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(π​(tn)|ℱtn)=α​Q​(pbidCEX​(tn)−pDEX​(tn))+(1−α)​𝔼​(Vf​(tn,1,1)|ℱtn)\mathbb{E}\bigl(\pi(t\_{n})|\mathcal{F}\_{t\_{n}}\bigr)=\alpha Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{DEX}}(t\_{n})\bigr)+(1-\alpha)\mathbb{E}\bigl(V^{f}(t\_{n,1},1)|\mathcal{F}\_{t\_{n}}\bigr) |  |

where Vf​(tn,1,1)V^{f}(t\_{n,1},1) is the value function for the fallback problem, which will be defined below, and ℱtn\mathcal{F}\_{t\_{n}} is the information set at time tnt\_{n}. Next, we define Xs=Q​(pbidCEX​(tn)−pDEX​(tn))X^{s}=Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{DEX}}(t\_{n})\bigr) as the profit conditional on success and Xf=Vf​(tn,1,1)X^{f}=V^{f}(t\_{n,1},1) as the random profit conditional on failure. Hence, the variance of profit is:

|  |  |  |
| --- | --- | --- |
|  | Var​(π​(tn)|ℱtn)=α​(1−α)​(Xs−𝔼​(Xf|ℱtn))2+(1−α)​Var​(Xf|ℱtn)\text{Var}\bigl(\pi(t\_{n})|\mathcal{F}\_{t\_{n}}\bigr)=\alpha(1-\alpha)\biggl(X^{s}-\mathbb{E}\bigl(X^{f}|\mathcal{F}\_{t\_{n}}\bigr)\biggr)^{2}+(1-\alpha)\text{Var}\bigl(X^{f}|\mathcal{F}\_{t\_{n}}\bigr) |  |

Therefore, the agent enters if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(π​(tn)|ℱtn)−λ​Var​(π​(tn)|ℱtn)≥θ\mathbb{E}\bigl(\pi(t\_{n})|\mathcal{F}\_{t\_{n}}\bigr)-\lambda\sqrt{\text{Var}\bigl(\pi(t\_{n})|\mathcal{F}\_{t\_{n}}\bigr)}\geq\theta |  | (1) |

Fallback logic. When the DEX leg fails, the agent holds an open CEX position that must eventually be closed. At each decision point tn+k,mt\_{n+k,m} (at slot n+kn+k, subslot mm) after kk failed DEX attempts, the agent chooses among three options:

1. Close immediately: Buy back on the CEX at the current ask price. Hence, the profit is deterministic:

|  |  |  |
| --- | --- | --- |
|  | πc​(tn+k,m)=Q​(pbidCEX​(tn)−paskCEX​(tn+k,m))\pi^{c}(t\_{n+k,m})=Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{CEX}}\_{\text{ask}}(t\_{n+k,m})\bigr) |  |

2. Retry on DEX: Submit a new DEX buy order at the current DEX price and wait for the next slot. If the retry succeeds (with probability α\alpha):

|  |  |  |
| --- | --- | --- |
|  | πr​(tn+k,m|Ln+k=1)=Q​(pbidCEX​(tn)−pDEX​(tn+k))\pi^{r}\bigl(t\_{n+k,m}|L\_{n+k}=1\bigr)=Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{DEX}}(t\_{n+k})\bigr) |  |

On the contrary, if the retry fails (with probability 1−α1-\alpha), the agent enters the fallback problem again at the next slot with one additional failed attempt:

|  |  |  |
| --- | --- | --- |
|  | πr​(tn+k,m|Ln+k=0)=Vf​(tn+k+1,0,k+1)\pi^{r}\bigl(t\_{n+k,m}|L\_{n+k}=0\bigr)=V^{f}(t\_{n+k+1,0},k+1) |  |

That is, the expected profit from retrying equals:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(πr​(tn+k,m)|ℱtn+k,m)=α​Q​(pbidCEX​(tn)−pDEX​(tn+k))+(1−α)​𝔼​(Vf​(tn+k+1,0,k+1)|ℱtn+k,m)\mathbb{E}\bigl(\pi^{r}(t\_{n+k,m})|\mathcal{F}\_{t\_{n+k,m}}\bigr)=\alpha Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{DEX}}(t\_{n+k})\bigr)+(1-\alpha)\mathbb{E}\bigl(V^{f}(t\_{n+k+1,0},k+1)|\mathcal{F}\_{t\_{n+k,m}}\bigr) |  |

3. Wait: Do nothing for one time step and reassess at tn+k,m+1t\_{n+k,m+1}:

|  |  |  |
| --- | --- | --- |
|  | πw​(tn+k,m)=Vf​(tn+k,m+1,k)\pi^{w}(t\_{n+k,m})=V^{f}(t\_{n+k,m+1},k) |  |

In the end, the agent selects the option with the highest risk-adjusted utility:

|  |  |  |
| --- | --- | --- |
|  | uc​(tn+k,m)=πc​(tn+k,m)u^{c}(t\_{n+k,m})=\pi^{c}(t\_{n+k,m}) |  |

|  |  |  |
| --- | --- | --- |
|  | ur​(tn+k,m)=𝔼​(πr​(tn+k,m)|ℱtn+k,m)−λ​Var​(πr​(tn+k,m)|ℱtn+k,m)u^{r}(t\_{n+k,m})=\mathbb{E}\bigl(\pi^{r}\bigl(t\_{n+k,m})|\mathcal{F}\_{t\_{n+k,m}}\bigr)-\lambda\sqrt{\text{Var}\bigl(\pi^{r}(t\_{n+k,m})|\mathcal{F}\_{t\_{n+k,m}}\bigr)} |  |

|  |  |  |
| --- | --- | --- |
|  | uw​(tn+k,m)=𝔼​(πw​(tn+k,m)|ℱtn+k,m)−λ​Var​(πw​(tn+k,m)|ℱtn+k,m)u^{w}(t\_{n+k,m})=\mathbb{E}\bigl(\pi^{w}\bigl(t\_{n+k,m})|\mathcal{F}\_{t\_{n+k,m}}\bigr)-\lambda\sqrt{\text{Var}\bigl(\pi^{w}(t\_{n+k,m})|\mathcal{F}\_{t\_{n+k,m}}\bigr)} |  |

Hence, the value function is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vf​(tn+k,m,k)=max⁡{uc​(tn+k,m),ur​(tn+k,m),uw​(tn+k,m)}V^{f}(t\_{n+k,m},k)=\max\bigl\{u^{c}(t\_{n+k,m}),u^{r}(t\_{n+k,m}),u^{w}(t\_{n+k,m})\bigr\} |  | (2) |

subject to constraints: retry is only available if there is sufficient time before slot end (m≤M−M¯m\leq M-\bar{M}), wait is only available within a slot (m<Mm<M), and after k¯\bar{k} failed attempts, the agent must close. The fallback logic is depicted in [Figure 3](https://arxiv.org/html/2601.00738v1#S3.F3 "Figure 3 ‣ 3.2 Risk-Averse Model ‣ 3 Modeling the Trading Agent").

Fallback Logic After Failed DEX Transaction


DEX Transaction Failed
Open position with delta exposure
State: (tn+k,m,k)(t\_{n+k,m},k) failed attempts

Evaluate Options
max⁡(Uc,Ur,Uw)\max(U^{c},U^{r},U^{w})

Close via CEX
- Buy QQ tokens on CEX now
- Lock in loss/gain immediately
- No variance (certain outcome)

Retry via DEX
- Submit new DEX order
- Constraint: m≤M−M¯m\leq M-\bar{M}
- Wait for the next confirmation step

Wait for better conditions
- Do nothing for δ\delta seconds
- Constraint: m<Mm<M
- Reassess at tn+k,m+1t\_{n+k,m+1}

Position Closed
Final PnL realized

Position Closed
Final PnL realized

Still Exposed
Enter fallback at
tn+k+1,0t\_{n+k+1,0} (k+1)

Re-evaluate
Back to decision
node at tn+k,m+1t\_{n+k,m+1}

Success (α\alpha)

Failure (1−α1-\alpha)


Figure 3: Decision tree showing fallback logic after a failed DEX transaction.

Price dynamics for expectation computation. Computing the value function requires modeling future prices. Here, we assume CEX log-returns follow a Gaussian random walk:

|  |  |  |
| --- | --- | --- |
|  | log⁡pmidCEX​(tn+k,m)=log⁡pmidCEX​(tn+k,0)+∑j=1mεj,εj∼𝒩​(0,σ2​δ)\log p^{\text{CEX}}\_{\text{mid}}(t\_{n+k,m})=\log p^{\text{CEX}}\_{\text{mid}}(t\_{n+k,0})+\sum^{m}\_{j=1}\varepsilon\_{j},\quad\varepsilon\_{j}\sim\mathcal{N}(0,\sigma^{2}\delta) |  |

with bid and ask prices given by pbidCEX=(1−β)​pmidCEXp^{\text{CEX}}\_{\text{bid}}=(1-\beta)p^{\text{CEX}}\_{\text{mid}} and paskCEX=(1+β)​pmidCEXp^{\text{CEX}}\_{\text{ask}}=(1+\beta)p^{\text{CEX}}\_{\text{mid}} where β\beta is the half-spread. DEX prices are updated only at slot boundaries and track the CEX mid-price with mean-reverting basis risk η\eta:

|  |  |  |
| --- | --- | --- |
|  | pDEX​(tn+k)=pmidCEX​(tn+k)+ηn+kp^{\text{DEX}}(t\_{n+k})=p^{\text{CEX}}\_{\text{mid}}(t\_{n+k})+\eta\_{n+k} |  |

Computational approach. We solve the value function by backward induction with Monte Carlo estimation at each node. The terminal condition is forced closure at k=k¯k=\bar{k}:

|  |  |  |
| --- | --- | --- |
|  | Vf​(tn+k¯,m,k¯)=Q​(pbidCEX​(tn)−paskCEX​(tn+k¯,m))V^{f}(t\_{n+\bar{k},m},\bar{k})=Q\bigl(p^{\text{CEX}}\_{\text{bid}}(t\_{n})-p^{\text{CEX}}\_{\text{ask}}(t\_{n+\bar{k},m})\bigr) |  |

Recursion proceeds in two nested loops: an outer loop over failed attempts (k=k¯−1,…,0k=\bar{k}-1,...,0) and an inner loop over subslots within each slot (m=M,…,0m=M,...,0). At each state, we simulate NN price paths to estimate the expectation and variance of each option, and then select the option with the highest risk-adjusted utility.

## 4 Simulation Design

The simulation models the competitive dynamics between agents operating CEX-DEX arbitrage bots. Agent 1 represents the participant whose behavior we analyze in detail, while Agent 2 represents the aggregate behavior of all other market participants. The two agents compete for arbitrage opportunities, but only one can successfully execute the DEX leg of any given trade.

When an arbitrage opportunity arises, multiple agents might attempt to capture it, but blockchain constraints ensure only one transaction can succeed. When Agent 1 attempts an opportunity, they win with probability α\alpha. When Agent 1 fails or chooses not to attempt to land their DEX transaction, Agent 2 automatically succeeds and captures the arbitrage profit. Conversely, when Agent 1 succeeds, Agent 2’s transaction fails.

This competitive structure introduces execution risk that fundamentally shapes agent behavior. In the simple model, both agents attempt every detected opportunity regardless of expected outcomes. In the risk-averse model, Agent 1 evaluates each opportunity’s risk-adjusted expected value before entering, while Agent 2 continues to pursue all opportunities. When Agent 1 declines to enter based on unfavorable risk-return characteristics, Agent 2 captures the arbitrage. Agent 2 represents a simplified aggregate of market participants who close failed positions immediately on the CEX, while Agent 1 employs the risk-averse fallback logic described in [Section 3.2](https://arxiv.org/html/2601.00738v1#S3.SS2 "3.2 Risk-Averse Model ‣ 3 Modeling the Trading Agent"), potentially waiting for better conditions or retrying on the DEX.

The core objective of the simulation is to quantify how faster execution guarantees change arbitrageur behavior and market outcomes. For each of the four configurations listed below, we run parallel simulations under two execution regimes. In the 12-second execution regime, DEX transactions can only be executed at Ethereum slot boundaries, occurring every 12 seconds: this represents the simple environment where arbitrageurs face substantial execution windows and corresponding uncertainty. In the 1-second execution regime, DEX transactions can be executed every second through subslot confirmations: this represents the improved environment where arbitrageurs receive faster execution guarantees.

Configuration Space. We evaluate agent behavior across multiple environmental configurations to assess the robustness of our findings. Each configuration combines two binary design choices that capture different aspects of market microstructure.

The first choice is CEX-DEX price reversion. When enabled, subslot DEX prices gradually adjust toward CEX prices between arbitrage events using the regression-based mechanism described in [Section 2.2](https://arxiv.org/html/2601.00738v1#S2.SS2 "2.2 CEX-DEX Price Reversion ‣ 2 DEX Price Interpolation"). This captures informed trading that occurs independently of direct arbitrage.

The second choice is noise trading. When enabled, the simulation incorporates random non-arbitrage transactions whose frequency and price impact are sampled from empirical distributions estimated from data. This captures retail flow and other trading activity unrelated to CEX-DEX arbitrage.

These two binary choices yield four distinct configurations, ranging from a minimal environment with no reversion and no noise, to an environment incorporating both components. The results of these configurations are then compared to an agent with the current 12-second confirmation interval.

Key assumptions. The simulation relies on several key assumptions. On the execution side: all validators are opted in to providing fast execution guarantees; hence, there are no missed slots, and DEX transactions can occur every second; gas fees are zero; agents cannot run out of capital, meaning liquidity constraints do not affect execution, and there are no fees other than DEX pool fees. On the arbitrage side: every top-of-block arbitrage opportunity is executed; arbitrages are executed with the optimal trade size, moving the DEX price to one pool fee from CEX bid or ask; infinite liquidity exists at the best bid and ask on Binance, and execution on Binance is instant and guaranteed. On market structure: DEX pools are constant-product (Uniswap v2-style); liquidity is constant except for the increase from swap fees, and all pools start with identical initial liquidity for comparability.

Parameters. For parameters used by both models, Agent 1’s winning probability is set to α=0.35\alpha=0.35, and the CEX-DEX reversion interval window is 300 seconds. For parameters specific to the risk-averse model, the risk-aversion coefficient is λ=0.01\lambda=0.01, the entry threshold is θ=0\theta=0, and Monte Carlo estimation uses 16 paths at each node. The decision wait horizon is 3 seconds, and the maximum wait time is also 3 seconds. Robustness tests vary α∈{0.20,0.35,0.50}\alpha\in\{0.20,0.35,0.50\} and λ∈{0,0.01,0.03}\lambda\in\{0,0.01,0.03\}.

Combined effect of changes. To assess the overall impact across all three pools, we compute a weighted average of the pool-specific changes in transaction counts and volume. The weights reflect each pool’s historical share of arbitrage activity during the observation period.
For transaction counts, the 30, 5, and 1 basis point pools represent 3.7%, 33.1%, and 63.2% of total arbitrage transactions, respectively. For trading volume, these pools account for 28.6%, 50.3%, and 21.1% of total arbitrage volume, respectively.

## 5 Results

We examine the impact of reducing the confirmation interval from 12 seconds to 1 second on transaction frequency and trading volume across different configurations and fee-tier pools, comparing simple and risk-averse agent models. All reported ranges reflect aggregated results across all fee levels and configurations for an agent with a 35% probability of successfully executing a DEX leg.

Transaction Frequency. We measure transaction frequency as the number of transactions landed by the agent. In the simple model, transaction counts increase substantially across all pools. Across all configurations and fee tiers, the simple model exhibits increases ranging from 218% to 663%.

The risk-averse model exhibited an even greater increase in transaction frequency, with a transaction count increase ranging from 294% to 1386%. However, it is important to note that most scenarios fall below an increase of 600% with the 1386% being present in a single configuration where, while the percentage change is big, the absolute number of transactions is quite small.

The pattern across fee tiers reflects the economics of arbitrage at different spread levels. Lower-fee pools have tighter spreads and more marginal opportunities. Under a 12-second confirmation, many of these opportunities are not worth pursuing because the execution window is long enough that adverse price moves can wipe out the slim profit margin. Under 1-second confirmation, the risk is compressed, and more marginal opportunities become viable.

The weighted average of transaction number increase across different pools varies between 356% and 412% for the simple model depending on the configuration, with the average of noise with and without reversion configurations being 371%. Similarly, for the risk-averse model, the weighted increase varies between 378% and 567%, with the average of two configurations being 535%.

Trading Volume. Trading volume, measured in terms of Ethereum, shows more nuanced patterns than changes in number of transactions. In the simple model, the volume changes exhibit increases ranging from 98% to 273% depending on the configuration. Similarly to the trading frequency, the increase is closer to the lower end of the range for the 30 basis point pool and closer to the higher end for the 5 and 1 basis point pools. The risk-averse model showed similar patterns with increases ranging from 121% to 375%.

The volume increases are concentrated in lower-fee pools. The intuition here is as follows: when more marginal opportunities become viable, the average trade size may fall (as marginal opportunities tend to have smaller optimal trade sizes), but the total number of trades increases by enough to raise aggregate volume. In higher-fee pools, where opportunities are already large and infrequent, faster confirmations do not as dramatically expand the viable opportunity set.

It is important to note that these ranges represent outcomes under different configurations; however, since gas fees are not incorporated into the model, the upper bounds of these ranges might overestimate the increase for the 1-basis-point and 5-basis-point pools, where the economic viability of frequent small transactions would be constrained by transaction costs in practice.

When weighing the volume increases based on the arbitrage volume across different pools, the average increase in volume for the three pools varies between 148% and 211% for the simple model, with the average being 168%. Similarly, for the risk-averse model, the overall increase varies between 159% and 243%, with the average being 203%.

Robustness Tests. To assess the robustness of these findings, we conducted an additional set of simulations for the risk-averse model under the reversion and noise trading configuration. We varied Agent 1’s win probability α∈{0.20,0.35,0.50}\alpha\in\{0.20,0.35,0.50\} and the risk aversion parameter λ∈{0,0.01,0.03}\lambda\in\{0,0.01,0.03\}, and compared outcomes when the confirmation interval is reduced from 12 seconds to 1 second.

In the 5 basis point pool, across all combinations in this grid, transaction counts increased by 416–530%, and ETH trading volume increased by 146–186%. In the 30 basis point pool, transaction counts increased by 1152–1468%, and ETH volume changes ranged between a 317% increase and a 385% increase. Overall, changes in transaction counts and volume are of the same magnitude when comparing agents with identical parameters under 12-second versus 1-second confirmation intervals, suggesting that the main results are robust to reasonable variations in win probability and risk aversion.

## 6 Conclusion

This paper examines how reducing blockchain execution times affects decentralized exchange activity, focusing on the behavior of CEX-DEX arbitrageurs. Our contribution is as much methodological as empirical: we develop a simulation framework combining empirical price anchoring, noise-trading dynamics, CEX–DEX arbitrage mechanics, and a risk-averse decision model. The agent we model takes execution risk seriously, incorporating DEX transaction uncertainty into both entry decisions and fallback strategies. This setup captures a fundamental reality of on-chain trading that prior work has largely abstracted away.

Under reasonable assumptions about agent risk preferences and inclusion probabilities, the shift from a 12-second to a 1-second execution environment increases the number of arbitrage transactions by 535%, with effects concentrated in lower-fee pools where marginal opportunities become newly viable. Faster execution also reduces profit variance by compressing the window for adverse price moves during failed-trade recovery.

Several limitations are worth mentioning. Our model assumes zero gas fees, which may overstate the viability of small trades in low-fee pools. Also, the agent’s probability of landing DEX trades is fixed rather than endogenously determined by competition; in equilibrium, faster execution might attract more arbitrageurs and compress α\alpha. These extensions remain for future work.

## Appendix A Appendix

Below are tables with exhaustive results for different configurations.

### Table A1

Changes in the simple agent’s metrics for the 30 bps pool when confirmation frequency is decreased to 1 second.

| Configuration | Δ\Delta PnL | Δ\Delta ETH Vol. | Δ\Delta USDC Vol. | Δ\Delta Txns |
| --- | --- | --- | --- | --- |
| no reversion, no noise | +113%+113\% | +118%+118\% | +116%+116\% | +294%+294\% |
| no reversion, noise | +97%+97\% | +98%+98\% | +97%+97\% | +218%+218\% |
| reversion, no noise | +276%+276\% | +273%+273\% | +265%+265\% | +663%+663\% |
| reversion, noise | +218%+218\% | +211%+211\% | +205%+205\% | +478%+478\% |

### Table A2

Changes in the simple agent’s metrics for the 5 bps pool when confirmation frequency is decreased to 1 second.

| Configuration | Δ\Delta PnL | Δ\Delta ETH Vol. | Δ\Delta USDC Vol. | Δ\Delta Txns |
| --- | --- | --- | --- | --- |
| no reversion, no noise | +138%+138\% | +158%+158\% | +157%+157\% | +308%+308\% |
| no reversion, noise | +135%+135\% | +151%+151\% | +150%+150\% | +274%+274\% |
| reversion, no noise | +147%+147\% | +174%+174\% | +172%+172\% | +345%+345\% |
| reversion, noise | +144%+144\% | +165%+165\% | +164%+164\% | +313%+313\% |

### Table A3

Changes in the simple agent’s metrics for the 1 bp pool when confirmation frequency is decreased to 1 second.

| Configuration | Δ\Delta PnL | Δ\Delta ETH Vol. | Δ\Delta USDC Vol. | Δ\Delta Txns |
| --- | --- | --- | --- | --- |
| no reversion, no noise | +195%+195\% | +203%+203\% | +202%+202\% | +420%+420\% |
| no reversion, noise | +207%+207\% | +200%+200\% | +199%+199\% | +408%+408\% |
| reversion, no noise | +207%+207\% | +205%+205\% | +204%+204\% | +432%+432\% |
| reversion, noise | +212%+212\% | +202%+202\% | +201%+201\% | +420%+420\% |

### Table A4

Changes in the risk-averse agent’s metrics for the 30 bps pool when confirmation frequency is decreased to 1 second.
Note: For the table below, it is important to note that while the changes in the number of transactions in terms of percentages are great for certain configurations, the numbers are small in absolute terms.

| Configuration | Δ\Delta PnL | Δ\Delta ETH Vol. | Δ\Delta USDC Vol. | Δ\Delta Txns |
| --- | --- | --- | --- | --- |
| no reversion, no noise | +114%+114\% | +121%+121\% | +119%+119\% | +294%+294\% |
| no reversion, noise | +119%+119\% | +126%+126\% | +124%+124\% | +336%+336\% |
| reversion, no noise | +282%+282\% | +274%+274\% | +267%+267\% | +639%+639\% |
| reversion, noise | +365%+365\% | +375%+375\% | +365%+365\% | +1386%+1386\% |

### Table A5

Changes in the risk-averse agent’s metrics for the 5 bps pool when confirmation frequency is decreased to 1 second.

| Configuration | Δ\Delta PnL | Δ\Delta ETH Vol. | Δ\Delta USDC Vol. | Δ\Delta Txns |
| --- | --- | --- | --- | --- |
| no reversion, no noise | +135%+135\% | +158%+158\% | +157%+157\% | +307%+307\% |
| no reversion, noise | +137%+137\% | +162%+162\% | +161%+161\% | +444%+444\% |
| reversion, no noise | +145%+145\% | +174%+174\% | +173%+173\% | +345%+345\% |
| reversion, noise | +147%+147\% | +179%+179\% | +178%+178\% | +500%+500\% |

### Table A6

Changes in the risk-averse agent’s metrics for the 1 bp pool when confirmation frequency is decreased to 1 second.

| Configuration | Δ\Delta PnL | Δ\Delta ETH Vol. | Δ\Delta USDC Vol. | Δ\Delta Txns |
| --- | --- | --- | --- | --- |
| no reversion, no noise | +151%+151\% | +205%+205\% | +204%+204\% | +419%+419\% |
| no reversion, noise | +151%+151\% | +205%+205\% | +205%+205\% | +544%+544\% |
| reversion, no noise | +158%+158\% | +208%+208\% | +207%+207\% | +472%+472\% |
| reversion, noise | +161%+161\% | +206%+206\% | +206%+206\% | +554%+554\% |

### Table A7

Combined effect across three pools, weighted by historical transaction counts and volume, showing changes when confirmation frequency is decreased to 1 second.

|  | Simple | | Risk-averse | |
| --- | --- | --- | --- | --- |
| Configuration | Δ\Delta ETH Vol. | Δ\Delta Txns | Δ\Delta ETH Vol. | Δ\Delta Txns |
| no reversion, no noise | +158%+158\% | +378%+378\% | +159%+159\% | +378%+378\% |
| no reversion, noise | +148%+148\% | +356%+356\% | +163%+163\% | +503%+503\% |
| reversion, no noise | +211%+211\% | +412%+412\% | +212%+212\% | +437%+437\% |
| reversion, noise | +188%+188\% | +387%+387\% | +243%+243\% | +567%+567\% |

## References

* [1]

  Empirical Analysis of Cross Domain CEX-DEX Arbitrage on Ethereum.
  Ethereum Research, December 2023. URL:
  <https://ethresear.ch/t/empirical-analysis-of-cross-domain-cex-dex-arbitrage-on-ethereum/17620>
* [2]

  CEX/DEX arbitrage, transaction fees, block times, and LP profits.
  Ethereum Research, May 2024. URL:
  <https://ethresear.ch/t/cex-dex-arbitrage-transaction-fees-block-times-and-lp-profits/19444>
* [3]

  The Influence of CeFi-DeFi Arbitrage on MEV-Boost Auction Bid Profiles.
  Ethereum Research, October 2023. URL:
  <https://ethresear.ch/t/the-influence-of-cefi-defi-arbitrage-on-mev-boost-auction-bid-profiles/17258>
* [4]

  F. Wu, D. Sui, T. Thiery, and M. Pai.
  Measuring CEX-DEX Extracted Value and Searcher Profitability: The Darkest of the MEV Dark Forest, August 2025. arXiv:2507.13023 [cs.CR]. URL: <https://arxiv.org/abs/2507.13023>
* [5]

  B. Öz, D. Sui, T. Thiery, and F. Matthes. Who Wins Ethereum Block Building Auctions and Why? July 2024. arXiv:2407.13931 [cs.CE]. URL: <https://arxiv.org/abs/2407.13931>
* [6]

  Preconfirmations: The Fulfillment–Delivery Paradigm. URL:
  <https://paragraph.com/@preconf/preconfirmations-the-fulfillment-delivery-paradigm>
* [7]

  Measuring Validator Economics Under Preconfirmations: Early Mainnet Evidence.
  Ethereum Research, September 2025. URL:
  <https://ethresear.ch/t/measuring-validator-economics-under-preconfirmations-early-mainnet-evidence/23066>
* [8]

  Preconfirmations Under the No Lens.
  Ethereum Research, 2024. URL:
  <https://ethresear.ch/t/preconfirmations-under-the-no-lens/19975>
* [9]

  Analysing Expected Proposer Revenue from Preconfirmations.
  Lido Research, 2024. URL:
  <https://research.lido.fi/t/analysing-expected-proposer-revenue-from-preconfirmations/8954>