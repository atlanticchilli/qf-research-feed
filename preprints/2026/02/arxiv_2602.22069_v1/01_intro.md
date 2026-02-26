---
authors:
- Matthew Willetts
- Christian Harrington
doc_id: arxiv:2602.22069v1
family_id: arxiv:2602.22069
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic
  weight AMMs'
url_abs: http://arxiv.org/abs/2602.22069v1
url_html: https://arxiv.org/html/2602.22069v1
venue: arXiv q-fin
version: 1
year: 2026
---


Matthew Willetts and Christian Harrington

###### Abstract

Dynamic-weight AMMs (aka Temporal Function Market Makers, TFMMs) implement algorithmic asset allocation, analogous to index or smart beta funds, by continuously updating pools’ weights.
A strategy updates target weights over time, and arbitrageurs trade the pool back toward those weights.
This creates a sequence of small, predictable mispricings that grow until taken, effectively executing rebalances as a series of Dutch reverse auctions.
Prior theoretical and simulation work [[1](https://arxiv.org/html/2602.22069v1#bib.bib1)] predicted that this mechanism could outperform CEX-style rebalancing.
We test that claim on two live pools on the QuantAMM protocol, one on Ethereum mainnet and one on Base, across two short rebalancing windows six months apart (July 2025 and January 2026).
We perform block-level arbitrage analysis, and then measure long term outcomes using Loss-vs-Rebalancing (LVR) and Rebalancing-vs-Rebalancing (RVR) benchmarks.
On mainnet, rebalancing becomes markedly more efficient over time (more frequent arbitrage trades with lower value extracted per trade), reaching performance comparable to or better than CEX-based models.
On Base, rebalancing persists even when per-trade extraction is near (or below) zero, consistent with routing-driven execution, and achieves efficiencies that meet or exceed standard “perfect rebalancing” LVR baselines.
These results demonstrate dynamic-weight AMMs as a competitive execution layer for tokenised funds, with superior performance on L2s where routing and lower data costs compress arbitrage spreads.

## 1 Introduction

Temporal Function Market Making (TFMM) pools use AMM mechanisms not for core liquidity providing, but instead as a way to run a time-varying portfolio.
They are geometric mean market maker (G3M) pools where the weights change over time.
The weights *are* the portfolio vector, and when a pool’s holdings are not in alignment with its weights there is an arbitrage opportunity that, when taken, rebalances the pool to its desired holdings.

At a chosen cadence the pool’s quantitative asset management strategy can be run, outputting new target weights (e.g. given recent market data, increase holdings of asset A and reduce holdings of asset B).
Then, analogous to how, when trading on an order book, dividing up a large trade improves execution quality by reducing market impact, the weight change for a TFMM pool is best spread out over time, so the pool interpolated towards the new target holdings.

Arbitrageurs just see a G3M pool with weights that shift.
The pool’s quoted prices drift away from the external market, creating a small arbitrage opportunity that grows over time.
Without arbitrageurs needing to know it, this *is* a Dutch reverse auction [[2](https://arxiv.org/html/2602.22069v1#bib.bib2)]: the pool implicitly offers a rising payment for rebalancing execution, starting at zero after each trade and growing with allocation drift, until an arbitrageur accepts by striking.
The arbitrageur who acts first captures their profit; after the trade, the pool’s reserves snap to market-consistent values, and the cycle repeats until the interpolation is complete.

The competitive arbitrageur ecosystem is the pool’s execution engine; the question is how much this execution costs.
Figure [1](https://arxiv.org/html/2602.22069v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") illustrates this mechanism schematically.
Previous work has characterised this mechanism theoretically [[3](https://arxiv.org/html/2602.22069v1#bib.bib3), [4](https://arxiv.org/html/2602.22069v1#bib.bib4)] and in simulation.
The Loss-versus-Rebalancing (LVR) framework [[5](https://arxiv.org/html/2602.22069v1#bib.bib5), [6](https://arxiv.org/html/2602.22069v1#bib.bib6)] and its extension Rebalancing-versus-Rebalancing (RVR) [[1](https://arxiv.org/html/2602.22069v1#bib.bib1)] provide benchmarks for the cost of AMM-based rebalancing, and the MEV literature [[7](https://arxiv.org/html/2602.22069v1#bib.bib7)] establishes that on-chain arbitrage is mediated by a competitive ecosystem of searchers.

blockarb opportunity (USD)ExecutedExecuted⋯\cdotsefficient arbitrageurinefficient arbitrageurauction cycle 1auction cycle 2Per-block arb opportunity (grows each block)Profitability Threshold (opportunity exceeds frictions)Arbitrageur Execution

Figure 1: The Dutch reverse auction mechanism. Each block, the arb opportunity (red bars) grows as weight changes accumulate. The dashed lines mark arbitrageur cost thresholds; the trade occurs when the opportunity exceeds the leanest arbitrageur’s cost. After the trade the cycle resets.

First we give a per-block empirical analysis of arb dynamics on live dynamic-weight AMM pools on the QuantAMM protocol, the first such study, revealing auction compression in the a six-month period from July 2025 to early 2026.
We identify *incidental routing*—rebalancing that occurs as a side effect of ecosystem-wide DEX routing at near-zero cost to the pool.
We then benchmark the pools’ properties against LVR and RVR.

## 2 Background

#### G3M pools

A geometric mean market maker (G3M) [[8](https://arxiv.org/html/2602.22069v1#bib.bib8), [9](https://arxiv.org/html/2602.22069v1#bib.bib9)] with NN tokens has trading function ∏i=1NRiwi=k\prod\_{i=1}^{N}R\_{i}^{w\_{i}}=k, where 𝐑={Ri}\boldsymbol{\mathbf{R}}=\{R\_{i}\} is the NN-vector of currently-held reserves of each token and the weights 𝐰={wi}\boldsymbol{\mathbf{w}}=\{w\_{i}\}, ∑i=1Nwi=1\sum\_{i=1}^{N}w\_{i}=1 and ∀i​  0≤wi<1\forall i\,\,0\leq w\_{i}<1, control how much value is stored in each token.
The pool’s *actual* value allocation for token ii is θi=Ri​pi∑jRj​pj\theta\_{i}=\frac{R\_{i}\,p\_{i}}{\sum\_{j}R\_{j}\,p\_{j}}.
A fundamental property of G3M pools is that θi=wi\theta\_{i}=w\_{i} only when the pool quotes market prices [[10](https://arxiv.org/html/2602.22069v1#bib.bib10)].
A Temporal Function Market Maker (TFMM) [[11](https://arxiv.org/html/2602.22069v1#bib.bib11), [12](https://arxiv.org/html/2602.22069v1#bib.bib12)] is a G3M where the weights change with time according to a set process.
The trading function becomes ∏i=1NRiwi​(t)=k​(t)\prod\_{i=1}^{N}R\_{i}^{w\_{i}(t)}=k(t).
Within a block weights are constant (i.e. tt is the discrete blocknumber).

When the pool drifts from market prices (due to weight changes or external price movements), θi≠wi\theta\_{i}\neq w\_{i}, until the pool gets arbed.
A pool will not necessarily get arbed immediately, the pool’s own fees mean the price discrepancy has be be ‘large enough‘, and other real world frictions (gas cost, the efficiency of other venues the arbitrageur might use to get into their chosen numeraire at the end of the arbitrage trade, time delays inherent to blockchain systems) increase the effective ‘no-arb region‘ further.

(a) No arbitrage — mpm\_{p} inside bandγ​mu\gamma\,m\_{u}γ−1​mu\gamma^{-1}m\_{u}mum\_{u}mpm\_{p}Market price within band ⇒\Rightarrow no profitable trade exists✓(b) Arbitrage opportunity — mpm\_{p} outside bandγ​mu\gamma\,m\_{u}γ−1​mu\gamma^{-1}m\_{u}mum\_{u}mpm\_{p}profit ∝\propto gapMarket price outside band ⇒\Rightarrow profitable arbitrage trade exists!

(a) The no-arbitrage region for a two token pool.
(a) Market price mpm\_{p} inside the band [γ​mu,γ−1​mu][\gamma m\_{u},\gamma^{-1}m\_{u}] (where mum\_{u} is the price quoted by the pool for a marginal trade): no profitable trade.
(b) Market price mpm\_{p} outside the band: profit proportional to gap. An optimal arbitrageur places mpm\_{p} at the boundary of the *new* band, leaving a residual gap ≈\approx fee (see also Figure [D.4](https://arxiv.org/html/2602.22069v1#A4.F4 "Figure D.4 ‣ Appendix D Finite-size effects on boundary targeting ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")).

t=0t=0equilibriummum\_{u}mpm\_{p}t=1t=1band shiftsΔ​w\Delta wt=2t=2gap growingΔ​w\Delta wt=kt=karb exists!gapt=k+1t\!=\!k\!+\!1gap widenslarger gapt=k+2t\!=\!k\!+\!2post-arb resetarb trade!mpm\_{p}mum\_{u}gap ≈\approx feecycle repeats

(b) Weight changes shift the no-arb band block-by-block.
mum\_{u} (violet) and the band (green) drift rightward while mpm\_{p} (gold) stays fixed.
By t=kt\!=\!k, mpm\_{p} exits the band; the gap widens until an arbitrageur trades at t=k+2t\!=\!k\!+\!2, resetting mum\_{u} so that mpm\_{p} sits at the new boundary. The dashed arrow marks the repeating cycle.

Figure 2: No-arb band mechanics and the weight-driven auction cycle.

#### From weight changes to arbitrage

As the update rule shifts target weights each block, the pool’s quoted marginal price mum\_{u} moves and the no-arb band moves with it.
If external prices are relatively stable, the band “walks away” from the market price (Figure [2(b)](https://arxiv.org/html/2602.22069v1#S2.F2.sf2 "In Figure 2 ‣ G3M pools ‣ 2 Background ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")).

At some block t=kt=k, the market price exits the band and an arb opportunity appears.
The gap grows each block as weights continue to interpolate, until an arbitrageur trades.
The arbitrageur trades just enough to shift mum\_{u} so that mpm\_{p} lands by the boundary of the new band, leaving a residual gap of approximately one fee.
The cycle then repeats, a series of instant runoff Dutch reverse auction, where each block of weight interpolation adds a small increment to the arb opportunity, and the first arbitrageur whose cost falls below the accumulated surplus captures it.

#### Weight interpolation reduces rebalancing cost

Rebalancing by changing weights over time preserves a G3M pool’s value to first order: V′=V+𝒪​(δ​w2)V^{\prime}=V+\mathcal{O}(\delta w^{2}).
This quadratic leading order dependence means total rebalancing cost reduces with the size of constituent weight changes [[12](https://arxiv.org/html/2602.22069v1#bib.bib12)]: splitting a single large weight change Δ​w\Delta w into NN small steps of Δ​w/N\Delta w/N reduces the total arb cost from (Δ​w)2(\Delta w)^{2} to (Δ​w)2/N(\Delta w)^{2}/N.
In the limit of continuous interpolation (N→∞N\to\infty), the theoretical cost vanishes entirely[[12](https://arxiv.org/html/2602.22069v1#bib.bib12)].

QuantAMM pools make use of this by interpolating weights gradually over many blocks rather than making discrete jumps [[4](https://arxiv.org/html/2602.22069v1#bib.bib4)].
The rebalancing costs observed in this paper reflect pools already operating in the many-small-steps regime; costs would be much higher if weights changed in one go.

## 3 Experimental setup

#### Pools and data

We study two QuantAMM pools on different chains, at different scales, each observed at two points six months apart:

|  |  |  |
| --- | --- | --- |
|  | Safe Haven | Base Macro |
| Chain | Ethereum mainnet | Base L2 |
| TVL | ∼{\sim}$300k | ∼{\sim}$50k |
| Launch Date | May 2025 | May 2025 |
| Assets | BTC / PAXG / USDC | AERO / BTC / ETH / USDC |
| Swap fee | 0.3% | 0.3% |
| Protocol fee | 50% of swap fee | 50% of swap fee |
| Block time | 12s | 2s |
| MEV infrastructure | PBS (Flashbots) | Sequencer (FIFO) |

Table 1: The two pools share fee structure and protocol design but differ in TVL (∼50×{\sim}50\times), chain architecture, and block frequency (6×6\times).

For each pool and window, we scrape per-block reserves, weights, prices, and gas statistics, identifying blocks where pool balances change due to swaps then matching each change in reserves to its on-chain transaction.111QuantAMM protocol runs on top of Balancer V3’s vault which keeps 50% of the pool’s swap fee, so pools’ balance deltas must be scaled appropriately before further calculation.

#### Profitability threshold

We construct a time-varying, per-block profitability threshold calibrated against observed arbitrageur costs.
The total cost for an arbitrageur is made up of three components: the EIP-1559 base fee (burned), a priority fee (paid to the block builder), and optionally a direct builder tip [[7](https://arxiv.org/html/2602.22069v1#bib.bib7), [13](https://arxiv.org/html/2602.22069v1#bib.bib13)].
We identify *open-market arbitrageurs*—those whose full cost is visible on-chain—and compute the threshold for a block bb as

|  |  |  |
| --- | --- | --- |
|  | threshold​(b)=baseFee​(b)×G×pETH×μ/ 109,\text{threshold}(b)=\text{baseFee}(b)\times G\times p\_{\text{ETH}}\times\mu\;/\;10^{9}, |  |

where G=450,000G=450{,}000 gas units (median amount for observed arb trades), pETHp\_{\text{ETH}} is the ETH price, and μ\mu is the calibrated markup (capturing the intensity of competition in the arbitrage market).
Looking at open-market trades in July in different arbitrageurs, the mean markup is μ=1.50\mu=1.50.

#### Mispricing

How to measure how far a pool’s mispricing is, in aggregate, to best observe how mispricing builds up over time and is then reduced by an arbitrage trade?
We study multi-token (N=3N=3 or 44) pools here.
We define the *allocation drift* as ∑i|θi−wi|\sum\_{i}|\theta\_{i}-w\_{i}|, which is zero at equilibrium and grows as the pool deviates.
As we will show, this metric produces a clean sawtooth pattern with gradual buildup as the pool drifts, sharp resets when an arbitrageur trades the pool back toward its target allocation, without having to handle or plot ∼N2/2\sim N^{2}/2 pairwise price comparisons.

## 4 Results

First we give extremely fine grained analysis of the arbitrage trades done against these pools over two time short periods where pool weights are changing, each a couple of hours, one in July 2025 a few months after launch, and more recently in Jan 2026.
Second, we give broad, aggregate analysis of these pools since their launch, benchmarking against Loss-versus-Rebalancing (LVR [[5](https://arxiv.org/html/2602.22069v1#bib.bib5)]) and its more realistic extension Rebalancing versus Rebalancing (RVR [[1](https://arxiv.org/html/2602.22069v1#bib.bib1)]) that models the spread and commission fees present when trading on a CEX.

### 4.1 Block-level arbitrage analysis

#### Auction dynamics on Ethereum mainnet

In a two-hour window from the Safe Haven pool on July 22 2025 (10:00–12:00 UTC), we observe 20 trades over 606 blocks.
The allocation drift sawtooth is clean (Figure [3](https://arxiv.org/html/2602.22069v1#S4.F3 "Figure 3 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")): drift builds to 0.5–0.65% between trades, then snaps back as an arbitrageur trades the pool toward its target.
Arbitrage trades occur roughly every 30 blocks (∼{\sim}6 minutes).

The closed-form optimal arbitrage trade [[3](https://arxiv.org/html/2602.22069v1#bib.bib3)] predicts a theoretical maximum extraction of $58.19 over the window.
arbitrageurs empirically extract $51.55, an efficiency ratio of 88.6%.
The gap is explained primarily by conservative trade sizing (Appendix [C](https://arxiv.org/html/2602.22069v1#A3 "Appendix C Practical choices made by Arbitrageurs ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")): arbitrageurs consistently execute ∼60\sim 60% of the optimal trade size while capturing almost all of the available profit, which is natural given that the G3M arb profit function is concave and flat near its maximum (Figure [D.4](https://arxiv.org/html/2602.22069v1#A4.F4 "Figure D.4 ‣ Appendix D Finite-size effects on boundary targeting ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")).

![Refer to caption](2_panel_plots/auction_arb_safe_haven_july_2panel.png)


Figure 3: Safe Haven pool, July 22 2025 (10:00–12:00 UTC), 606 blocks, 20 arb trades.
Top: Allocation drift sawtooth; dashed line = 0.3% pool fee.
Second: Per-block arb profit (green) with floor and calibrated thresholds; red triangles = arbitrage trades. All 20 exceed the realistic threshold.

![Refer to caption](2_panel_plots/auction_arb_safe_haven_january_2panel.png)


Figure 4: Safe Haven pool, January 8 2026 (01:00–03:00 UTC), 591 blocks, 78 trades (∼4×{\sim}4\times July).
The sawtooth is compressed: drift rarely exceeds 0.45% and trades occur every ∼{\sim}90 seconds.
The y-axis scale is ∼4×{\sim}4\times smaller than Figure [3](https://arxiv.org/html/2602.22069v1#S4.F3 "Figure 3 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs"); 32% of trades fall below the standalone threshold.

Six months later, Jan 2026, the same pool looks very different (Figure [4](https://arxiv.org/html/2602.22069v1#S4.F4 "Figure 4 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")).
The sawtooth is compressed: allocation drift barely exceeds 0.4% before an arbitrageur trades.
Instead of 20 trades in two hours, we observe 78—roughly one every 90 seconds.
Per-trade empirical extraction falls from $2.58 to $0.28, and total empirical extraction drops from $51.55 to $22.00 despite nearly 4×4\times more trades (Table [2](https://arxiv.org/html/2602.22069v1#S4.T2 "Table 2 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")).

|  | July 2025 | January 2026 |
| --- | --- | --- |
| Trades (2-hour window) | 20 | 78 |
| Empirical extraction per trade | $2.58 | $0.28 |
| Total empirical extraction | $51.55 | $22.00 |
| Theoretical optimum | $58.19 | $35.82 |
| Max allocation drift | ∼{\sim}0.65% | ∼{\sim}0.45% |
| Blocks between trades | ∼{\sim}30 (∼{\sim}6 min) | ∼{\sim}7.5 (∼{\sim}90 sec) |

Table 2: Safe Haven arb dynamics across two windows. All profit figures are empirical.

This is the dynamic predicted by the Dutch reverse auction framework [[4](https://arxiv.org/html/2602.22069v1#bib.bib4)]: competition among searchers progressively lowers the arbitrage threshold, the auction clears at a lower price, and the pool benefits.

No retail or organic swap flow was detected in either window: every transaction originates from MEV market participants, identified by contract-mediated execution and/or multi-hop routing through 2+ DEXs.
By January, the routing landscape has shifted: Uniswap V4 accounts for 37% of all swap events (up from zero), complex MEV bundles with 4+ legs account for 24% of trades, and the mean all-in cost per transaction fell from $1.08 to $0.20, drive by the Fusaka Upgrade in Dec 2025 (see Appendix [A](https://arxiv.org/html/2602.22069v1#A1 "Appendix A Transaction structure ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") for full breakdown).

![Refer to caption](2_panel_plots/auction_arb_basemacro_jan14_2panel.png)


Figure 5: Base Macro pool, January 14 2026 (08:00–10:00 UTC). The sawtooth is present but individual resets are tiny.
A small number of arb trades here are driven by changes in external asset prices during this weight interpolation, marked in yellow, where we have found them by taking a ‘what for’ approach: if we can still find an arbitrage opportunity in that moment from the current pool reserves, current market prices, and *stale* weights, then we say the trade is ‘price drive’ and is not a key part of our weight-change-rebalance analysis.
Trades resulting in negative profit for the arbitrageur (a zero time markout) we label as ‘incidental routing’; these are legs of arb transactions whose profit is generated elsewhere.

#### Incidental rebalancing on Base L2

The Base Macro pool provides a contrasting case: it sits on a chain with no PBS infrastructure.
In the January window we observe 202 block-to-block balance changes from 225 on-chain transactions.
Per-trade empirical profit is essentially zero: the mean is $0.0004, the median is below $0.001, and 98% of trades extract less than a cent from the pool, many in fact ‘extracting’ less than zero.
These trades, as a result, often add value to the pool, albeit a tiny amount.

These arbitrageurs are not targeting this pool for value extraction.
The pool serves as a routing venue in complex multi-hop arbitrages across the Base DEX ecosystem.
January transactions average 7 swaps across UniV2, V3, and V4, all to handle what amounts to a $20–80 trade through this pool.
The arbitrage profit comes from price discrepancies between *other* pools; the QuantAMM pool happens to be one hop in the route, traded at approximately fair market value.
We call this *incidental routing*, examples of which are marked with a grey 𝗑\mathsf{x} in Figure [5](https://arxiv.org/html/2602.22069v1#S4.F5 "Figure 5 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs").

Yet inventory does shift.
The swaps are directionally correct—arbitrageurs buy whichever token is slightly cheap in the pool and sell whichever is slightly expensive—and the allocation drift still shows its characteristic sawtooth (Figure [5](https://arxiv.org/html/2602.22069v1#S4.F5 "Figure 5 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")), though individual resets are tiny.
The mechanism is straightforward: target weights shift slowly, allocation drift builds, but the resulting mispricing is too small to justify standalone arb after the 0.3% fee plus gas.
Multi-hop arbitrageurs route through the pool anyway as part of a profitable ecosystem-wide route, and the swap moves reserves back toward target.

### 4.2 Benchmarking rebalancing efficiency

Over the period August 2025 to January 2026, the Base Macro exceeded both the LVR benchmark [[5](https://arxiv.org/html/2602.22069v1#bib.bib5)] (a hypothetical frictionless CEX rebalancer executing the same weight trajectory) and the RVR benchmark (a realistic CEX rebalancer that pays commissions and crosses spreads).
Figure [6](https://arxiv.org/html/2602.22069v1#S4.F6 "Figure 6 ‣ 4.2 Benchmarking rebalancing efficiency ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") shows cumulative outperformance of approximately 27 percentage points vs. LVR and 43 percentage points vs. RVR.
This period included episodes of very high volume on Base, which the dynamic-weight strategy was positioned to capture.

These figures reflect the *combined* effect of the pool’s dynamic-weight strategy and its execution efficiency; the comparison does not isolate the rebalancing cost component.
The fact that the pool outperforms even the frictionless LVR benchmark indicates that the strategy’s signal-driven weight changes more than compensate for arb extraction, and the widening gap suggests that execution costs are not eroding returns.

LVR and RVR attempt to benchmark rebalancing efficiency and so they help answer whether dynamic weight AMMs are good portfolio construction infrastructure.
Impermanent loss (IL), meanwhile, measures absolute returns against a counterfactual HODL.
Indeed, a fixed-weight (constant-mix) strategy with perfect LVR-style rebalancing can in some market conditions beat HODL.222Further, is not clear always how to correctly generalise IL when the pool is changing it target weights over time.
IL-type benchmarks thus mix the choice of strategy (how the weights change, or do not change) with rebalancing efficiency.
To the extent they are useful, they are most relevant to a pool’s creator and/or manager in terms of absolute target weight decisions.

LVR   RVR

  

Safe Haven
  
![Refer to caption](lvr-rvr-scale/scraped_2025-08-01_lvr.png)
(a) Mainnet, Aug 2025–Jan 2026.
![Refer to caption](lvr-rvr-scale/scraped_2025-08-01_rvr.png)
(b) Mainnet, same period.

  

Base Macro
  
![Refer to caption](lvr-rvr-scale/scraped_2025-05-15_lvr.png)
(c) Base L2, May 2025–Jan 2026.
![Refer to caption](lvr-rvr-scale/scraped_2025-05-15_rvr.png)
(d) Base L2, same period.

  


Figure 6: Cumulative portfolio value of each pool relative to LVR and RVR benchmarks. LVR [[5](https://arxiv.org/html/2602.22069v1#bib.bib5)] assumes frictionless, continuous rebalancing on a CEX executing the same weight trajectory; RVR [[1](https://arxiv.org/html/2602.22069v1#bib.bib1)] adds realistic spreads and commissions. Values above zero indicate the AMM pool outperforming the benchmark over the period.
Top row: Safe Haven (Ethereum mainnet, August 2025–January 2026). Bottom row: Base Macro (Base L2, May 2025–January 2026). Both pools outperform the realistic RVR benchmark, confirming that AMM-based execution is competitive with CEX rebalancing.
The L2 pool additionally outperforms the frictionless LVR benchmark, consistent with the near or below-zero per-trade costs documented in Section [4.1](https://arxiv.org/html/2602.22069v1#S4.SS1 "4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs").

## 5 Discussion

#### The sawtooth pattern

Over a series of auction cycles, the allocation gap traces a characteristic sawtooth wave (Figure [1](https://arxiv.org/html/2602.22069v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs")).
Each tooth represents one complete auction cycle: a linear ramp as the gap grows block-by-block, followed by an instantaneous reset when an arbitrageur acts.

The height of each tooth—the gap at which an arbitrage trade occurs—is determined by the leanest arbitrageur’s profit threshold.
The shaded triangles above the gas cost line represent the arbitrageurs net profit: the difference between the total gap and the cost of executing the trade.
Compare this schematic with the empirical sawtooth patterns in Figures [3](https://arxiv.org/html/2602.22069v1#S4.F3 "Figure 3 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") and [4](https://arxiv.org/html/2602.22069v1#S4.F4 "Figure 4 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs"): the July data shows tall teeth (large gaps, ∼{\sim}6-minute cycles) while January shows compressed teeth (smaller gaps, ∼{\sim}90-second cycles), exactly as predicted by the expecting competition between arbitrageurs.

#### Profitability thresholding as a diagnostic

The threshold defined in Section [3](https://arxiv.org/html/2602.22069v1#S3.SS0.SSS0.Px2 "Profitability threshold ‣ 3 Experimental setup ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") serves a dual purpose.
Under the assumption that the pool is the sole source of profit, the threshold defines the minimum extraction needed for a standalone arb to be viable.

In July, this assumption holds cleanly: 100% of Safe Haven trades have empirical profit above the realistic threshold (Figure [3](https://arxiv.org/html/2602.22069v1#S4.F3 "Figure 3 ‣ Auction dynamics on Ethereum mainnet ‣ 4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs"), second panel).
In January, 32% of trades fall *below* the threshold—viable only because the arbitrageur is running a multi-venue strategy where gas is amortised across legs.
On Base Macro, nearly 100% of trades fall below the threshold: the pool is rebalanced entirely through incidental routing.

The fraction of trades below the standalone threshold thus provides a simple, observable metric for how much a pool benefits from the routing ecosystem.
As the DEX ecosystem matures [[14](https://arxiv.org/html/2602.22069v1#bib.bib14), [15](https://arxiv.org/html/2602.22069v1#bib.bib15)], more rebalancing shifts from targeted extraction to incidental routing, and the pool’s rebalancing cost falls without any change to its own fee or design.

#### Maturity and Efficiency Summary

New invariants or auction approaches can have a large gap between theoretical perfect efficiency and actual arbitrage discovery and efficiency.
For TFMMs, where in a given block the arbitrage opportunity is presented as if via a completely vanilla G3M, we see that arbitrageurs are consistent and efficient.
Sawtooth patterns in the arbitrage process, most clearly on mainnet, give the clearest picture.
As expected, high frequency, noisier arbitrage is seen when on an L2.

#### LVR and RVR benchmarks

LVR is a simple and clean benchmark (do you beat perfection), but its very simplicity is a limitation: as it does not take into account spreads or costs such as fees for centralised rebalancing, it is of perhaps limited use for comparing or analysing the real-world trade offs of different ways to rebalance a portfolio.
RVR was introduced as an improved model for those evaluating execution mechanisms for practical use.
Despite this, on an L2 rebalancing a portfolio as an AMM beats the perfect rebalancing of LVR.

Simulations in [[1](https://arxiv.org/html/2602.22069v1#bib.bib1)], themselves based on empirical study [[16](https://arxiv.org/html/2602.22069v1#bib.bib16)], do appear to have over-estimated retail volume as a ratio of arbitrage volume at the lower pool TVLs studied here.
This may just be a property of price impact and liquidity depth: noise trade assumptions might still be accurate at higher TVLs.
While noise trading was an over-estimate, upgrades and the rich MEV ecosystem have meant that effective gas costs and trade costs have also been an over-estimated for both mainnet and L2s.
With reduced gas costs the threshold required for dynamic weight AMMs to become more efficient than realistic CEX models (RVR) is lowered.
Practically for L2s we have seen this reduction in gas cost be more important than the reduced estimate of noise models.
More accurate noise modelling has also not been explored in either these empirical results or in simulation work.
Finally, note that simulated work and the empirical analysis here also only tests linear interpolation, non-linear methods exist [[4](https://arxiv.org/html/2602.22069v1#bib.bib4)] that can further reduce the barrier for dynamic weight AMMs to beat realistic and perfect CEX based price taker rebalancing.

## 6 Conclusion

TFMM pools pay for rebalancing through arbitrage: small, predictable Dutch reverse auctions that run continuously on-chain.
Across two live TFMM/QuantAMM pools observed over time we find consistent auction compression: trades become more frequent, extraction per trade falls, transactions become more multi-venue, and a growing share of trades fall below the standalone profitability threshold.

On Ethereum mainnet (Safe Haven pool), the trade rate increases from 20 in a two hour window to 78, while mean per-trade extraction drops from $​2.58\mathdollar 2.58 to $​0.28\mathdollar 0.28, consistent with intensified competition lowering the profit threshold.
On Base (Base Macro pool), extraction is essentially zero (98% of trades extract <$​0.01<\mathdollar 0.01, many <$​0<\mathdollar 0 so in fact they are subsidising the pool) yet the pool still rebalances, indicating a second regime where rebalancing is delivered largely via incidental routing rather than targeted extraction.
These patterns are consistent with external ecosystem maturation
so rebalancing costs can decline over time without changes to pool fee or design, though broader generalisation would require studying more pools, in more market conditions.

## References

* Willetts and Harrington [2024a]

  Matthew Willetts and Christian Harrington.
  Rebalancing-versus-rebalancing: Improving the fidelity of loss-versus-rebalancing, 2024a.
  URL <https://arxiv.org/abs/2410.23404>.
* IBM [2024]

  IBM.
  Dutch reverse auction, 2024.
  URL <https://www.ibm.com/docs/en/emptoris-sourcing/10.1.0?topic=rt-dutch-reverse-auction>.
  IBM Emptoris Sourcing documentation.
* Willetts and Harrington [2024b]

  Matthew Willetts and Christian Harrington.
  Closed-form solutions for generic n-token amm arbitrage, 2024b.
  URL <https://arxiv.org/abs/2402.06731>.
* Willetts and Harrington [2024c]

  Matthew Willetts and Christian Harrington.
  Optimal rebalancing in dynamic amms, 2024c.
  URL <https://arxiv.org/abs/2403.18737>.
* Milionis et al. [2022]

  Jason Milionis, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee Zhang.
  Automated market making and loss-versus-rebalancing, 2022.
* Milionis et al. [2023]

  Jason Milionis, Ciamac C. Moallemi, and Tim Roughgarden.
  Automated market making and arbitrage profits in the presence of fees, 2023.
  URL <https://arxiv.org/abs/2305.14604>.
* Daian et al. [2020]

  Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo Bentov, Lorenz Breidenbach, and Ari Juels.
  Flash boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability.
  In *2020 IEEE Symposium on Security and Privacy (SP)*, pages 910–927. IEEE, 2020.
* Evans [2019]

  Alex Evans.
  Liquidity provider returns in geometric mean markets, 2019.
* Martinelli and Mushegian [2019]

  Fernando Martinelli and Nikolai Mushegian.
  Balancer: A non-custodial portfolio manager, liquidity provider, and price sensor., 2019.
* Angeris et al. [2020]

  Guillermo Angeris, Alex Evans, and Tarun Chitra.
  When does the tail wag the dog? curvature and market making, 2020.
* team [2023a]

  QuantAMM team.
  Temporal-function market making, 2023a.
* team [2023b]

  QuantAMM team.
  Temporal-function market making litepaper, 2023b.
  URL <https://www.quantamm.fi/litepapers>.
* Flashbots [2021]

  Flashbots.
  Flashbots: Frontrunning the mev crisis, 2021.
  URL <https://writings.flashbots.net/>.
* Diamandis et al. [2023]

  Theo Diamandis, Max Resnick, Guillermo Angeris, Tarun Chitra, Alex Evans, and Stephen Boyd.
  An efficient algorithm for optimal routing through constant function market makers, 2023.
* Angeris et al. [2022]

  Guillermo Angeris, Tarun Chitra, Alex Evans, and Stephen Boyd.
  Optimal routing for constant function market makers, 2022.
* Canidio and Fritsch [2024]

  Andrea Canidio and Robin Fritsch.
  Arbitrageurs’ profits, lvr, and sandwich attacks: batch trading as an amm design response, 2024.
  URL <https://arxiv.org/abs/2307.02074>.

## Appendix A Transaction structure

### A.1 Evolving DEX Arb landscape

Even in July 2025, none of the 22 Safe Haven transactions are naive single-venue swaps.
Every transaction is a multi-hop arb routing through the broader DEX ecosystem.
A typical route sends PAXG to the Safe Haven pool and receives WBTC, sells WBTC for WETH on Uniswap V3, sells WETH for USDC, then buys PAXG with USDC to close the loop—four venues in a single atomic transaction.

No retail or organic swap flow was detected in either window: every transaction originates from professional MEV infrastructure, identified by contract-mediated execution, multi-hop routing through 2+ DEXs, and the absence of direct EOA-initiated single-pool swaps.
This means the pool earns no swap fee revenue from non-arb flow; its returns derive entirely from the value generated by dynamic weight changes, net of arb extraction.

By January, the routing landscape has shifted dramatically.
Uniswap V4 accounts for 37% of all swap events (up from zero), KyberSwap Elastic has entered the routing table at 11%, and complex MEV bundles with 4+ swap legs account for 24% of all trades.
The largest single transaction contains 51 swap events across 5 DEX protocols.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | July 2025 | | January 2026 | |
|  | Count | % | Count | % |
| Transaction type |  |  |  |  |
| 2-leg arb | 8 | 36 | 23 | 29 |
| 3-leg arb | 13 | 59 | 25 | 32 |
| Complex bundle (4+ swaps) | 1 | 5 | 19 | 24 |
| Other | — | — | 12 | 15 |
| DEX swap events |  |  |  |  |
| UniV3 | 27 | 77 | 137 | 42 |
| UniV4 | 0 | 0 | 119 | 37 |
| Kyber | 0 | 0 | 34 | 11 |
| UniV2 | 8 | 23 | 31 | 10 |
| All-in cost (mean) | $1.08 | | $0.20 | |
| Base fee share | 82% | | 39% | |
| Priority fee share | 10% | | 59% | |

Table A.1: Transaction complexity, DEX event distribution, and cost decomposition, Safe Haven pool. July costs are dominated by network congestion (base fee at ∼{\sim}0.55 gwei); January by builder inclusion competition (priority fee, with base fee down 12×12\times to ∼{\sim}0.047 gwei). Some arbitrageurs have off-chain builder arrangements that leave no on-chain cost trace.

### A.2 Mainnet gas cost decomposition

The cost structure inverts between observation windows:

| Cost component | July 2025 | January 2026 |
| --- | --- | --- |
| Base fee (burned) | $0.88  (82%) | $0.08  (39%) |
| Priority fee (to builder) | $0.11  (10%) | $0.12  (59%) |
| Builder tip (coinbase transfer) | $0.09  (8%) | $0.01  (2%) |
| Mean all-in cost | $1.08 | $0.20 |

Table A.2: All-in cost decomposition, Safe Haven pool. July is dominated by the base fee (network congestion at ∼{\sim}0.55 gwei mean); January by the priority fee (base fee dropped 12×12\times to ∼{\sim}0.047 gwei, making builder inclusion competition the binding constraint). Some arbitrageurs have off-chain arrangements with builders that leave no on-chain cost trace.

### A.3 Arber consolidation

A natural concern is that consolidation (from 65 unique arbitrageurs in July to 4 dominant bots by January on Base Macro) signals growing extractive power.
The data points in the opposite direction: consolidation coincides with *lower*, not higher, per-trade extraction.
The dominant bots are sophisticated multi-venue routers.
Their efficiency results in faster rebalancing at lower cost.

## Appendix B Arbitrage analysis showing weight changes and cumulative arbitrageur profit

In addition to the plots in §[4.1](https://arxiv.org/html/2602.22069v1#S4.SS1 "4.1 Block-level arbitrage analysis ‣ 4 Results ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs"), we can show for these same time periods the weight changes and cumulative profits made by arbitrageurs.

![Refer to caption](4_panel_plots/auction_arb_safe_haven_july_4panel.png)


Figure B.1: Safe Haven pool, July 22 2025 (10:00–12:00 UTC), 606 blocks, 20 arb trades.
Top: Allocation drift sawtooth; dashed line = 0.3% pool fee.
Second: Per-block arb profit (green) with floor and calibrated thresholds; red triangles = arbitrage trades. All 20 exceed the realistic threshold.
Third: Weight evolution (∼{\sim}0.06% shift over 2 hours).
Bottom: Cumulative extraction—empirical $51.55 is 88.6% of theoretical $58.19.

![Refer to caption](4_panel_plots/auction_arb_safe_haven_january_4panel.png)


Figure B.2: Safe Haven pool, January 8 2026 (01:00–03:00 UTC).

![Refer to caption](4_panel_plots/auction_arb_basemacro_jan14_4panel.png)


Figure B.3: Base Macro pool, January 14 2026 (08:00–10:00 UTC).

## Appendix C Practical choices made by Arbitrageurs

As discussed in the main paper, arbitrageurs can get most of the profit of an arb opportunity while under-sizing their trade.
Comparing empirical trades to the theoretical optimum reveals that arbitrageurs consistently under-trade, executing 54–71% of the optimal trade size while capturing 81–99% of the available profit.
The return-to-trade function is ∼\sim flat in the region of the optimum.
So this is rational: the last 30% of the optimal trade adds little marginal profit but requires that additional capital.

Further, we also observe that arbitrageurs use a small set of pre-computed trade sizes rather than solving the optimum each block.
The PAXG buy amount repeats across trades (e.g. multiple trades use the same trade amounts of 0.1307, 0.1283, 0.1017 PAXG), suggesting a strategy of simulating a number of discrete trade sizes that can capture most of the profit with minimal computational overhead.

## Appendix D Finite-size effects on boundary targeting

Why Optimal Arbs Target the Boundary


An arb’s profit is maximised when the post-trade mum\_{u} places mpm\_{p} at the
no-arb boundary — not when mu=mpm\_{u}=m\_{p}. Trading past that point costs
more in fees than it earns.
(a) Arb profit vs. trade sizetrade sizeprofitoptimumprice impact“naive” (mu=mpm\_{u}\!=\!m\_{p})


profit lost
  
by overtrading
marg. revenue >> feefee >> marg. revenueno tradeboundary(b) Post-trade pool state: optimal vs. naiveBeforemum\_{u}mpm\_{p}full gapOptimalmu′m\_{u}^{\prime}mpm\_{p}≈\approx feemp≈γ​mu′m\_{p}\approx\gamma\,m\_{u}^{\prime} (max profit)Naivemu′′=mpm\_{u}^{\prime\prime}\!=\!m\_{p}gap =0=0mu′′=mpm\_{u}^{\prime\prime}\!=\!m\_{p} (overtraded, less profit)more profit


Intuition: Each marginal unit of trade yields less revenue
(the AMM’s marginal price moves against you) but costs the same fee.
The optimum is where marginal revenue == fee — approximately when
mpm\_{p} reaches the no-arb boundary γ​mu′\gamma\,m\_{u}^{\prime}.
For finite-sized trades, cumulative price impact shifts the true optimum
slightly *inside* the boundary; this slippage grows linearly with
trade size (∼ 0.5{\sim}\,0.5\,bp per 1% of TVL traded).
In the limit of small trades the optimum *is* the boundary.

Figure D.4: Why optimal arbitrage trades target the no-arb boundary.
(a) Arb profit peaks near the trade size that places mpm\_{p} at the boundary γ​mu′\gamma m\_{u}^{\prime}, then declines; a “naive” arb that trades to mu=mpm\_{u}=m\_{p} earns zero.
The profit function is extremely flat near the optimum, explaining why arbitrageurs can under-trade substantially (54–71% of optimal size) while capturing most of the profit (81–99%).
(b) Number-line comparison of pre-trade, optimal post-trade, and naive post-trade states.
The optimal arb leaves a residual gap ≈\approx fee; the naive arb eliminates the gap entirely at the cost of zero profit.

One might think that the optimal arb trade results in the pool quoting market prices post trade.
After all, that is when pool value is minimised.
For pool with zero fees, that is true, but when fees are charged an optimal arbtrade lands the pool’s post-trade quoted prices near but not exactly at the boundary of the no trade region.
Figure [D.4](https://arxiv.org/html/2602.22069v1#A4.F4 "Figure D.4 ‣ Appendix D Finite-size effects on boundary targeting ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") describes why pool’s are taken (near the) the boundary at all.

But why not exactly the boundary?
In fact, for infinitesimal trades the optimal trade does take post-trade quoted prices exactly to the edge.
For trades of finite size relative to pool TVL, cumulative price impact shifts the profit-maximising post-trade price ratio slightly *inside* the no-arb region.

Figure [D.5](https://arxiv.org/html/2602.22069v1#A4.F5 "Figure D.5 ‣ Appendix D Finite-size effects on boundary targeting ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") illustrates this for a two-token equal-weight pool with a 0.3% fee (γ=0.997\gamma=0.997).
Panel (a) shows the post-trade price gap as a function of the initial gap: for any starting deviation outside the band, the optimal trade brings the pool to a post-trade gap that sits just inside [γ,γ−1][\gamma,\gamma^{-1}], not exactly at its edge.
Panel (b) plots the distance from the boundary as a function of trade size (as a fraction of TVL).
The relationship is approximately linear at ∼ 0.5{\sim}\,0.5 basis points per 1% of TVL traded.
Panel (c) shows why this is optimal: the on-shell profit curve as a function of target post-trade gap peaks just inside the boundary (red dot), not at the boundary itself (dashed orange lines) and not at market price (green dotted line at gap =0=0).
Trading past the optimum toward the boundary would cost more in price impact than it earns from the smaller residual gap.

For the pools studied in this paper the effect is small—typical arb trades are ≪ 1%{\ll}\,1\% of TVL, so the optimum is within ∼ 0.1{\sim}\,0.1 bp of the boundary—but it is a systematic bias, not noise.
In the multivariate case the picture is richer: only the pair actively traded is driven to the boundary; other pairwise ratios may remain well inside their bands.

![Refer to caption](g3m_post_trade_deviation.png)


(a) Post-trade gap analysis. *Top left:* post-trade gap vs. initial gap lands near, not at, the boundary (red dashed lines). *Top right:* larger trades (larger initial gaps) push the post-trade ratio further inside the band. *Bottom left:* slippage from boundary grows linearly with trade size at ∼ 0.5{\sim}\,0.5\,bp per 1% TVL.

![Refer to caption](g3m_profit_vs_target.png)


(b) Profit vs. target post-trade gap for a 5% initial deviation. The profit maximum (red dot) falls just inside the no-arb boundary (orange dashed), not at market price (green dotted, gap =0=0). The curve is extremely flat near the maximum, explaining why arbitrageurs can under-trade substantially without sacrificing much profit.

Figure D.5: Finite-size effects on optimal arbitrage in a two-token G3M pool (fee =0.3%=0.3\%, equal weights). The optimal post-trade price ratio lies slightly inside the no-arb boundary, with the deviation growing linearly in trade size. In the limit of small trades, the optimum converges to the boundary exactly.

The Sawtooth Pattern — Continuous View


Over many blocks the “reverse Dutch auction” produces a characteristic
sawtooth wave in the price gap. Each tooth = one complete auction cycle.
Faster weight change ⇒\Rightarrow steeper ramp ⇒\Rightarrow more frequent arb trades.
time (blocks)price gap to no-arb boundarymin. arb cost


auction cycle 1

cycle 2
arb profitgas cost↓\downarrow trade↓\downarrow trade↓\downarrow trade↓\downarrow tradeprofitable zone (above gas cost)


gap ramps up
linearly each block


Figure D.6: The sawtooth pattern in continuous view.
The price gap to the no-arb boundary ramps up linearly each block, then drops to zero when an arbitrageur acts (dashed vertical lines).
The golden triangles above the gas cost line show the profitable zone.
Right-side braces on the first tooth decompose each trade into arb profit (green) and gas cost (blue).
Faster weight changes produce steeper ramps and more frequent trades.

Weight Interpolation Reduces Rebalancing Cost


Splitting a weight update into NN steps reduces total arb cost, because
arb profit scales *super-linearly* (∼Δ​w2\sim\Delta w^{2}) with price gap.
(a) NN-step total cost tiles inside 1-step costΔ​w\Delta wΔ​wN\frac{\Delta w}{N}cost saved(1−1N)​(Δ​w)2\left(1-\tfrac{1}{N}\right)\!(\Delta w)^{2}NN-step total: (Δ​w)2N\frac{(\Delta w)^{2}}{N}1-step cost: (Δ​w)2(\Delta w)^{2}(b) Why: cost is quadratic in gapgaparb costlinearg2g^{2}Δ​w\Delta wΔ​wN\frac{\Delta w}{N}


Quadratic is *flat* at origin:
small Δ​w\Delta w costs almost nothing.
  
Linear cost ⇒\Rightarrow no benefit from splitting.

Key insight: For a G3M pool, rebalancing preserves value to
first order: V′=V+𝒪​(δ​w2)V^{\prime}=V+\mathcal{O}(\delta w^{2}).
Cost is purely second-order (quadratic, not linear), so splitting
Δ​w\Delta w into NN steps of Δ​w/N\Delta w/N gives:
N×(Δ​wN)2=(Δ​w)2N→N→∞ 0\displaystyle N\times\left(\frac{\Delta w}{N}\right)^{\!2}\;=\;\frac{(\Delta w)^{2}}{N}\;\xrightarrow{N\to\infty}\;0


Figure D.7: Weight interpolation reduces rebalancing cost.
(a) Splitting Δ​w\Delta w into NN steps: the NN small-step costs (blue strip) tile into the bottom of the single-step cost (red square), with savings =(1−1/N)​(Δ​w)2=(1-1/N)(\Delta w)^{2}.
(b) The reduction works because arb cost scales as g2g^{2} (solid curve), which is flat near the origin, unlike a linear cost (dashed).
In the limit, total cost (Δ​w)2/N→0(\Delta w)^{2}/N\to 0.

## Appendix E Complete rebalancing lifecycle

Figure [E.8](https://arxiv.org/html/2602.22069v1#A5.F8 "Figure E.8 ‣ Appendix E Complete rebalancing lifecycle ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") provides a detailed block-by-block view of one complete rebalancing cycle using the number-line representation, combining the band mechanics of Figure [2(a)](https://arxiv.org/html/2602.22069v1#S2.F2.sf1 "In Figure 2 ‣ G3M pools ‣ 2 Background ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs") with the auction dynamics of Figure [1](https://arxiv.org/html/2602.22069v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs").

Starting from equilibrium at t0t\_{0} (both mum\_{u} and mpm\_{p} coincide, the band is centred), each block’s weight interpolation shifts the band rightward (t1t\_{1}, t2t\_{2}) while the market price mpm\_{p} stays fixed.
By t3t\_{3}, the market price has fallen outside the left edge of the band and an arb opportunity appears, initially small.
The opportunity grows through t4t\_{4} and t5t\_{5} as the band continues its rightward drift.

At t5t\_{5}, an arbitrageur acts.
The trade shifts mum\_{u} leftward so that mpm\_{p} lands at the left boundary of the new, smaller band.
Crucially, the pool does *not* return to perfect alignment (mu=mpm\_{u}=m\_{p}): a residual gap of approximately one fee remains, as explained in Figure [D.4](https://arxiv.org/html/2602.22069v1#A4.F4 "Figure D.4 ‣ Appendix D Finite-size effects on boundary targeting ‣ Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs").
From t6t\_{6} onward, the cycle restarts: the band resumes its rightward drift, the gap begins to build again, and the next arbitrageur waits for the opportunity to exceed their cost.

Complete Rebalancing Lifecycle — Detailed View


Combining the number-line view of no-arb bands with the auction timeline.
Watch how the band, implied price, and arb opportunity evolve block-by-block.
t0t\_{0}equilibriumt1t\_{1}band shifts rightΔ​w\Delta wt2t\_{2}gap growingΔ​w\Delta wt3t\_{3}arb appears!gapt4t\_{4}opportunity growslarger gapt5t\_{5}large opportunitylarge gapARB TRADEt5+t\_{5}^{+}reset (arb struck)mpm\_{p}mum\_{u}gap ≈\approx feet6t\_{6}new cycle…Δ​w\Delta wt7t\_{7}building againΔ​w\Delta w⋮\vdotstimemum\_{u} (implied)mpm\_{p} (market)no-arb bandgaparb opportunity zonearb trade


Figure E.8: Complete rebalancing lifecycle showing block-by-block evolution of the no-arb band (green rectangle), implied price mum\_{u} (violet dot), and market price mpm\_{p} (gold dot).
Weights interpolate rightward from t0t\_{0} to t5t\_{5}, creating a growing gap.
The arb trade at t5t\_{5} resets mum\_{u} so that mpm\_{p} sits at the band boundary.
At t5+t\_{5}^{+}, a residual gap ≈\approx fee remains.
The cycle restarts from t6t\_{6}.