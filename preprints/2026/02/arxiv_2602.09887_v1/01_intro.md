---
authors:
- Sunghun Ko
doc_id: arxiv:2602.09887v1
family_id: arxiv:2602.09887
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Partially Active Automated Market Makers
url_abs: http://arxiv.org/abs/2602.09887v1
url_html: https://arxiv.org/html/2602.09887v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ko Sunghun111kosunghun317@matroos.xyz, Matroos Labs and Department of Mathematical Sciences, KAIST.

###### Abstract

We introduce a new class of automated market maker (AMM), the *partially active automated market maker* (PA-AMM). PA-AMM divides its reserves into two parts, the active and the passive parts, and uses only the active part for trading. At the top of every block, such a division is done again to keep the active reserves always being λ\lambda-portion of total reserves, where λ∈(0,1]\lambda\in(0,1] is an activeness parameter. We show that this simple mechanism reduces adverse selection costs, measured by loss-versus-rebalancing (LVR), and thereby improves the wealth of liquidity providers (LPs) relative to plain constant-function market makers (CFMMs). As a trade-off, the asset weights within a PA-AMM pool may deviate from their target weights implied by its invariant curve. Motivated by the optimal index-tracking problem literature, we also propose and solve an optimization problem that balances such deviation and the reduction of LVR.

## 1 Introduction

### 1.1 Background and Related Works

Automated market makers (AMMs) have gained popularity and become a dominant type of decentralized exchange (DEX) on blockchains due to their simplicity and low computational and operational costs. However, because of their passive nature, AMM quotes cannot be updated in real time, and liquidity providers (LPs) suffer from adverse selection. More specifically, since asset prices are often discovered on centralized exchanges (CEXs) and AMMs lack access to off-chain information about the true value of assets, arbitrageurs can exploit stale AMM quotes and take profit. Such profit is estimated to reach over 230230 million USD between August 2023 and March 2025 [[38](https://arxiv.org/html/2602.09887v1#bib.bib1 "Measuring cex-dex extracted value and searcher profitability: the darkest of the mev dark forest")].

There has been extensive work on the structure and magnitude of such losses, both theoretically and empirically. In their early attempts practitioners used the notion of “impermanent loss” (sometimes called “divergence loss”) as a cost of liquidity provision [[31](https://arxiv.org/html/2602.09887v1#bib.bib24 "Understanding uniswap returns"), [32](https://arxiv.org/html/2602.09887v1#bib.bib23 "Uniswap: a good deal for liquidity providers?"), [3](https://arxiv.org/html/2602.09887v1#bib.bib26 "UNISWAP: impermanent loss and risk profile of a liquidity provider"), [16](https://arxiv.org/html/2602.09887v1#bib.bib25 "Impermanent loss and bancor v2")]. In their seminal work of [[27](https://arxiv.org/html/2602.09887v1#bib.bib2 "Automated market making and loss-versus-rebalancing")], Milionis et al. proposed a notion of *loss-versus-rebalancing* (LVR), an analogous of markout in the sense that they both measure quality of each trade with price shortly or immediately after the trade, as a metric to measure the loss (i.e., the cost) of liquidity providers (LPs) of AMMs from adverse selection. It has become a go-to metric for measuring loss from CEX-DEX arbitrage. Initially, its closed-form formula was based on assumptions of an ideal situation (Poisson block arrivals, no friction in arbitrageurs’ trades, no gas fee), but such assumptions were relaxed and further generalized in subsequent works [[28](https://arxiv.org/html/2602.09887v1#bib.bib28 "Automated market making and arbitrage profits in the presence of fees"), [29](https://arxiv.org/html/2602.09887v1#bib.bib27 "Loss-versus-rebalancing under deterministic and generalized block-times"), [35](https://arxiv.org/html/2602.09887v1#bib.bib37 "Arbitrage with bounded liquidity")]. A notion of *predictable loss* (PL) was also proposed in [[12](https://arxiv.org/html/2602.09887v1#bib.bib3 "Predictable losses of liquidity provision in constant function markets and concentrated liquidity markets")], which is a generalised version of (LVR) and consists of a convexity cost and an opportunity cost. With additional assumptions such as zero opportunity cost and the asset price following geometric Brownian motion with constant volatility, the PL degenerates to the LVR.

Moreover, studies on optimal liquidity provision, which concern the selection of the fee rate and the liquidity provision range that balances fee revenue from noise traders and losses to arbitrageurs [[19](https://arxiv.org/html/2602.09887v1#bib.bib30 "Optimal fees for geometric mean market makers"), [13](https://arxiv.org/html/2602.09887v1#bib.bib29 "Decentralized finance and automated market making: predictable loss and optimal liquidity provision"), [33](https://arxiv.org/html/2602.09887v1#bib.bib31 "A tick-by-tick solution for concentrated liquidity provisioning"), [4](https://arxiv.org/html/2602.09887v1#bib.bib32 "Fees in amms: a quantitative study"), [26](https://arxiv.org/html/2602.09887v1#bib.bib33 "The cost of permissionless liquidity provision in automated market makers"), [37](https://arxiv.org/html/2602.09887v1#bib.bib34 "The impact of market conditions and fee algorithms on the design of a competitive amm"), [10](https://arxiv.org/html/2602.09887v1#bib.bib35 "Optimal fees for liquidity provision in automated market makers")], have emerged. Especially, these studies collectively indicate that the optimal choice is determined by various factors, such as the arrival rate and distribution of order size of noise traders, asset volatility, competition between liquidity providers, and the parameters determined by underlying blockchains, such as gas fee costs and the time interval between two consecutive blocks.

Many mechanisms that mitigate LVR and protect LPs have also been proposed. These proposed mechanisms fall largely into three categories: batch execution of trades [[34](https://arxiv.org/html/2602.09887v1#bib.bib4 "Augmenting batch exchanges with constant function market makers"), [11](https://arxiv.org/html/2602.09887v1#bib.bib5 "Arbitrageurs’ profits, lvr, and sandwich attacks: batch trading as an amm design response")], dynamic fee rates [[15](https://arxiv.org/html/2602.09887v1#bib.bib6 "Designing a dynamic fee policy that outperforms all uniswap eth/usdc pools"), [14](https://arxiv.org/html/2602.09887v1#bib.bib7 "Strategic bonding curves in automated market makers"), [18](https://arxiv.org/html/2602.09887v1#bib.bib8 "Automatic market-making with dynamic peg"), [6](https://arxiv.org/html/2602.09887v1#bib.bib36 "Optimal dynamic fees in automated market makers")], and discriminatory quotes based on (inferred) toxicity of orders [[9](https://arxiv.org/html/2602.09887v1#bib.bib39 "Mooniswap"), [1](https://arxiv.org/html/2602.09887v1#bib.bib9 "Am-amm: an auction-managed automated market maker"), [36](https://arxiv.org/html/2602.09887v1#bib.bib10 "[BIP-295] fee discount for cowswap solvers")]. These approaches can be effective, but they often require additional infrastructure (e.g., an off-chain batcher, an administrator, or specialized auction mechanisms), rely on timely and robust information updates (e.g., oracles and/or order-flow inference), and may reduce atomic composability or increase implementation complexity.

There is another lens for viewing the AMMs: as a portfolio of assets that performs rebalancing at each block to keep each asset’s capital allocation close to its target weight.222Note that the target weight of each asset need not be kept fixed. For instance, the weight of assets in a Uniswap V3 LP position may vary as prices move within the liquidity range if the range is finite [[2](https://arxiv.org/html/2602.09887v1#bib.bib21 "Uniswap v3 core")]. Balancer’s liquidity bootstrapping pool (LBP) is an example of CFMM with time-varying weights [[7](https://arxiv.org/html/2602.09887v1#bib.bib20 "Liquidity bootstrapping pool")]. If asset prices move, the relative weights of assets within the portfolio deviate from their target weights, and AMMs rebalance the portfolio to target weights by allowing arbitrageurs to trade freely as long as the invariant is met, which is effectively an indirect way of submitting a market order. Within such a framework, CFMMs and the aforementioned improved mechanisms operate suboptimally in the sense that they immediately remove any deviation beyond a certain threshold from the target weights, that is, if the arbitrage happens in current block and the true price of the asset remains the same in the next block, no trade from arbitrageurs will happen even with zero friction since the opportunity has already gone in the last block. In the optimal index-tracking and optimal execution literature, this is rarely optimal. An optimal policy often comprises two components: a no-trading-zone and an execution plan, which it follows when a weight discrepancy escapes that no-trading-zone [[8](https://arxiv.org/html/2602.09887v1#bib.bib13 "Optimization methods for financial index tracking: from theory to practice"), [17](https://arxiv.org/html/2602.09887v1#bib.bib16 "Optimal portfolio rebalancing with transaction costs"), [24](https://arxiv.org/html/2602.09887v1#bib.bib17 "Optimal rebalancing of portfolios with transaction costs"), [22](https://arxiv.org/html/2602.09887v1#bib.bib18 "Dynamic trading with predictable returns and transaction costs"), [23](https://arxiv.org/html/2602.09887v1#bib.bib19 "Dynamic portfolio choice with frictions")]. Optimal execution is usually not a single large market order that is filled immediately, but rather a series of sub-orders executed over time [[5](https://arxiv.org/html/2602.09887v1#bib.bib11 "Optimal execution of portfolio transactions"), [30](https://arxiv.org/html/2602.09887v1#bib.bib12 "Optimal trading strategy and supply/demand dynamics")]. Except [[21](https://arxiv.org/html/2602.09887v1#bib.bib14 "MEV capture through time-advantaged arbitrage")], to our knowledge, there is no study on the mechanisms for AMMs that perform such *gradual* rebalancing to align the price at AMMs to the true price of assets.

### 1.2 Our Contributions

In this paper, we introduce a new class of AMMs, *partially active automated market makers* (PA-AMMs), that controls the *rebalancing speed* by allowing only a fraction of the pool’s liquidity to be available for trading in each block. We also provide a rigorous proof that controlling the rebalancing speed is indeed equivalent to determining the fraction of liquidity available in a single block.

Briefly, at the top of each block, the pool partitions its reserves into an *active* portion that can be traded in the current block and a *passive* portion that remains idle. The pool then quotes using only the active reserves and its invariant function φ\varphi. This partition is refreshed at the top of each block, so that a λ∈(0,1]\lambda\in(0,1] fraction of the total liquidity remains active at all times. The special case of λ=1\lambda=1 recovers the standard fully-active CFMM with invariant function φ\varphi.

When λ<1\lambda<1, the pool executes only a λ\lambda-fraction of the immediate rebalancing that would occur under a CFMM, thereby reducing the exposure to per-block adverse-selection. As a trade-off, the pool’s marginal price may deviate from the external reference price, and therefore, the asset allocation implied by its invariant function and the marginal price may diverge from its target allocation. Such tracking error becomes more severe as the activeness parameter λ\lambda decreases. Throughout the paper, we formalize this trade-off, define and solve the optimization problem of determining the optimal activeness level λ∗\lambda^{\*} that balances the trade-off. We also observe an increase in liquidity per unit of LP supply, due to the concavity of φ\varphi.

To our knowledge, this is the first study in the AMM and DeFi literature to explicitly and systematically examine the importance of the execution-speed perspective of rebalancing policy for AMM performance.

### 1.3 Roadmap

The paper is organized as follows. [Section˜2](https://arxiv.org/html/2602.09887v1#S2 "2 Preliminaries ‣ Partially Active Automated Market Makers") reviews concepts and notation around CFMMs and the underlying model setup that our analysis is based upon. [Section˜3](https://arxiv.org/html/2602.09887v1#S3 "3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers") defines PA-AMMs and derives the gap dynamics, stationary behavior, and the implied LVR rate. [Section˜4](https://arxiv.org/html/2602.09887v1#S4 "4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers") formulates and solves the optimal-activeness problem. In [Section˜5](https://arxiv.org/html/2602.09887v1#S5 "5 Conclusion ‣ Partially Active Automated Market Makers") we conclude with implications, limitations (e.g., fees and gas costs), and directions for future work.

## 2 Preliminaries

In this section, we recall the preliminary concepts and notations on AMMs that will be used throughout the paper. Note that although our work can be extended to cases with more than two assets, we focus on the two-asset case for notational simplicity. For a more detailed explanation, we refer the reader to check [[20](https://arxiv.org/html/2602.09887v1#bib.bib22 "Liquidity provider returns in geometric mean markets")].

### 2.1 Constant Function Market Makers

Let *invariant function* φ:ℝ+2→ℝ+\varphi:\mathbb{R}^{2}\_{+}\to\mathbb{R}\_{+} be C3C^{3}, strictly concave, and 11-homogeneous. Then the *constant function market maker* (CFMM) with reserves RR is a trader who accepts any trade (change of reserves) Δ​R\Delta R as long as the invariant holds, i.e., φ​(R+Δ​R)≥φ​(R)\varphi(R+\Delta R)\geq\varphi(R). The value of φ\varphi for given (x,y)(x,y) is called a *liquidity*. *The marginal (spot) price of asset XX in terms of asset YY* is then given by

|  |  |  |
| --- | --- | --- |
|  | Pmargin​(x,y)=−d​yd​x|R=(x,y)=φx​(x,y)φy​(x,y).P\_{\mathrm{margin}}(x,y)=\left.-\frac{dy}{dx}\right|\_{R=(x,y)}=\frac{\varphi\_{x}(x,y)}{\varphi\_{y}(x,y)}\,. |  |

We will denote the *log marginal price* by pmargin​(x,y)=log⁡Pmargin​(x,y)p\_{\mathrm{margin}}(x,y)=\log P\_{\mathrm{margin}}(x,y). We also define the reparametrization R​(L,p)=(x​(L,p),y​(L,p))R(L,p)=(x(L,p),y(L,p)) of reserves which satisfies

|  |  |  |
| --- | --- | --- |
|  | φ​(R​(L,p))=Landpmargin​(R​(L,p))=p.\varphi(R(L,p))=L\quad\text{and}\quad p\_{\mathrm{margin}}(R(L,p))=p\,. |  |

We will often abbreviate into x​(p)x(p) and y​(p)y(p) when liquidity LL remains same in the context. We also introduce a notion of *pool value* V​(L,P,S)≔S​x​(L,log⁡P)+y​(L,log⁡P)V(L,P,S)\coloneqq S\,x(L,\log P)+y(L,\log P), which is the total value of the pool with reserves R​(L,log⁡P)R(L,\log P) when the true price of asset XX (in terms of YY) is SS. Again, when it is clear that LL remains constant, we may abbreviate it into V​(P,S)V(P,S) or even V​(P)V(P) when P=SP=S. We further assume that φ\varphi is sufficiently smooth so that the aforementioned notions are all well-defined.

###### Example 1.

A geometric mean market maker (G3Ms) is a CFMM with invariant function φ\varphi defined as

|  |  |  |
| --- | --- | --- |
|  | φ​(x1,x2,⋯,xn)≔∏i=1nxiwi,\varphi(x\_{1},x\_{2},\cdots,x\_{n})\coloneqq\prod^{n}\_{i=1}x\_{i}^{w\_{i}}, |  |

where (wi)i∈[n](w\_{i})\_{i\in[n]} is weight of ii-th asset satisfying ∑i=1nwi=1\sum^{n}\_{i=1}w\_{i}=1. For two-assets G3M with reserves (x,y)(x,y) and weights (θ,1−θ)(\theta,1-\theta), the marginal price of asset XX in terms of asset YY is then:

|  |  |  |
| --- | --- | --- |
|  | Pmargin​(x,y)=θ1−θ⋅yx,P\_{\mathrm{margin}}(x,y)=\frac{\theta}{1-\theta}\cdot\frac{y}{x}, |  |

and for given log marginal price pp and liquidity LL, the reserves (x,y)(x,y) are:

|  |  |  |
| --- | --- | --- |
|  | x​(L,p)=L​(θ1−θ⋅e−p)1−θ,y​(L,p)=L​(1−θθ⋅ep)θ.x(L,p)=L\left(\frac{\theta}{1-\theta}\cdot e^{-p}\right)^{1-\theta},\quad y(L,p)=L\left(\frac{1-\theta}{\theta}\cdot e^{p}\right)^{\theta}. |  |

### 2.2 Setup

Throughout the paper, we assume that the quote asset YY is a stablecoin and the base asset XX is a risky asset whose (true) price follows geometric Brownian motion. That is, SnS\_{n}, the price of XX at block nn, satisfies:

|  |  |  |
| --- | --- | --- |
|  | log⁡Sn=log⁡Sn−1+εn,\log S\_{n}=\log S\_{n-1}+\varepsilon\_{n}, |  |

where εn∼𝒩​(μ​Δ​t,σ2​Δ​t),∀n∈ℕ\varepsilon\_{n}\sim\mathcal{N}(\mu\Delta t,\sigma^{2}\Delta t),\,\forall n\in\mathbb{N} i.i.d. and Δ​t\Delta t is the block time.

We further assume that there are infinitely many arbitrageurs competing with one another to arbitrage against the AMMs, and that there is no retail investor for simplicity. They are risk-neutral and myopic, in the sense that they care only about maximizing the immediately available profit at a given block if they win the opportunity. We also assume that gas cost is negligible and there is no friction in trading at centralized exchanges (CEXs), meaning that on CEXs, they can trade asset XX for asset YY at SnS\_{n} for any amount at block nn. As a result, for CFMMs with no swap fee, the pool’s spot price PmarginP\_{\mathrm{margin}} always coincides with the true market price after arbitrageurs’ trades.

### 2.3 Loss-versus-rebalancing

Based on this setup, the loss of LPs to arbitrageurs, *loss-versus-rebalancing* (LVR), is measured by the difference in the total value of assets within the pool before and after the arbitrage, i.e., V​(P,S)−V​(S)V(P,S)-V(S).333Note that this value is always greater than or equal to zero due to the concavity of φ\varphi. We recall the classical result introduced in [[27](https://arxiv.org/html/2602.09887v1#bib.bib2 "Automated market making and loss-versus-rebalancing")] where limit on the block time Δ​t→0\Delta t\to 0 is taken:

###### Proposition 1 (Theorem 1 of [[27](https://arxiv.org/html/2602.09887v1#bib.bib2 "Automated market making and loss-versus-rebalancing")]).

Loss-versus-rebalancing takes the form

|  |  |  |
| --- | --- | --- |
|  | LVRt=∫0tLVR¯​(Ps)​𝑑s,∀t≥0,\mathrm{LVR}\_{t}=\int^{t}\_{0}\overline{\mathrm{LVR}}(P\_{s})\,ds,\quad\forall t\geq 0, |  |

where we define, for P≥0P\geq 0, the instantaneous LVR by

|  |  |  |
| --- | --- | --- |
|  | LVR¯​(P)≔−σ2​P22​V′′​(P)≥0.\overline{\mathrm{LVR}}(P)\coloneqq-\frac{\sigma^{2}P^{2}}{2}V^{\prime\prime}(P)\geq 0\,. |  |

In particular, LVR\mathrm{LVR} is a non-negative, non-decreasing, and predictable process.

###### Example 2.

For instance, when the invariant curve is given by weighted geometric mean, i.e., the CFMM is geometric mean market maker (G3M) with weights (θ,1−θ)(\theta,1-\theta), the instantaneous rate of LVR becomes

|  |  |  |
| --- | --- | --- |
|  | LVR¯​(P)=σ22​θ​(1−θ)​V​(P).\overline{\mathrm{LVR}}(P)=\frac{\sigma^{2}}{2}\theta(1-\theta)V(P)\,. |  |

This LVR rate for CFMMs will serve as a baseline for measuring PA-AMM’s performance in the subsequent section.

## 3 PA-AMM and Its Properties

In this section, we introduce the partially active automated market maker (PA-AMM) and its properties.

### 3.1 The Partial Usage of Reserves and Periodic Rebalancing

The PA-AMM partitions the pool’s total reserves RtotalR\_{\text{total}} into two distinct components: active reserves (RactiveR\_{\text{active}}) and passive reserves (RpassiveR\_{\text{passive}}). The underlying invariant function φ\varphi enforces trading constraints solely on the active portion, thereby limiting the liquidity available for immediate arbitrage within any single block. The mechanism ensures that the active-passive division is done exactly once at the beginning of each block, triggered by the first interaction (swap, addition, or removal of liquidity) of that block.444Note that the rebalancing period does not need to be fixed as 1. For instance, rebalancing may occur every N≥2N\geq 2 blocks.

Let nn denote the current block height and nlastn\_{\text{last}} the block height of the last interaction. The rebalancing rule resets the active reserves to a fraction λ∈(0,1]\lambda\in(0,1] of the total equity, while keeping intact the remaining (1−λ)(1-\lambda) fraction in the passive reserves, unavailable for trading. This ensures that only a λ\lambda-fraction of the total liquidity is exposed to arbitrageurs at the top of each block. Subsequent trades within the same block execute against this static RactiveR\_{\text{active}} until the next block increments. The complete logic for rebalancing and swapping is formalized in [Algorithm˜1](https://arxiv.org/html/2602.09887v1#alg1 "In 3.1 The Partial Usage of Reserves and Periodic Rebalancing ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers").

Algorithm 1  Rebalancing and swap of PA-AMM

1:Global State:

2: Ractive,Rpassive∈ℝ+2R\_{\text{active}},R\_{\text{passive}}\in\mathbb{R}\_{+}^{2} ⊳\triangleright Current active and passive reserves

3: nlast∈ℕn\_{\text{last}}\in\mathbb{N} ⊳\triangleright Block number of last rebalance

4: λ∈(0,1]\lambda\in(0,1] ⊳\triangleright Activeness parameter

5:procedure Rebalance

6:  if block.number >nlast>n\_{\text{last}} then ⊳\triangleright Check if this is the first interaction in the block

7:   Rtotal←Ractive+RpassiveR\_{\text{total}}\leftarrow R\_{\text{active}}+R\_{\text{passive}}

8:   Ractive←λ⋅RtotalR\_{\text{active}}\leftarrow\lambda\cdot R\_{\text{total}} ⊳\triangleright Reset active reserves to λ\lambda portion of total reserves

9:   Rpassive←(1−λ)⋅RtotalR\_{\text{passive}}\leftarrow(1-\lambda)\cdot R\_{\text{total}} ⊳\triangleright Remaining liquidity is kept idle

10:   nlast←block.numbern\_{\text{last}}\leftarrow\text{block.number}

11:  end if

12:end procedure

13:procedure Swap(Δ​x,Δ​y\Delta x,\Delta y) ⊳\triangleright Executes an exchange Δ​x,Δ​y\Delta x,\Delta y

14:  Rebalance

15:  assert φ​(Ractive+(Δ​x,Δ​y))≥φ​(Ractive)\varphi(R\_{\text{active}}+(\Delta x,\Delta y))\geq\varphi(R\_{\text{active}}) ⊳\triangleright Check if invariant is preserved

16:  Ractivex←Ractivex+Δ​xR\_{\text{active}}^{x}\leftarrow R\_{\text{active}}^{x}+\Delta x

17:  Ractivey←Ractivey+Δ​yR\_{\text{active}}^{y}\leftarrow R\_{\text{active}}^{y}+\Delta y

18:end procedure

We remark that the rebalancing at most once per block is crucial; without such a limit, the trader can split her trade into many smaller trades and may obtain a better overall quote. In particular, in the extreme case where rebalancing occurs after each trade and the trader splits the order into infinitely many orders of infinitesimal size, the quote given by PA-AMM becomes the same as that of CFMM.555The similar happens in [[11](https://arxiv.org/html/2602.09887v1#bib.bib5 "Arbitrageurs’ profits, lvr, and sandwich attacks: batch trading as an amm design response")], which makes batching to be essential in their mechanism. This observation also tells us that while the liquidity available within *a single block* is only λ\lambda-fraction of corresponding CFMM with the same reserves, over *multiple blocks*, both PA-AMM and CFMM provide the same amount of liquidity to traders, and this is what separates PA-AMM from simply depositing λ\lambda-fraction of capital to CFMMs.666In the sense that the trader should divide the order into many sub-orders and gradually submit them over multiple blocks for optimal execution, one may consider PA-AMM as a form of implementation of a fully continuous exchange proposed in [[25](https://arxiv.org/html/2602.09887v1#bib.bib15 "Toward a fully continuous exchange")], given that the block arrival interval Δ​t\Delta t is short enough.

### 3.2 The Dynamics

We now derive the various properties of PA-AMM for the case of φ\varphi being a G3M with weights (θ,1−θ)(\theta,1-\theta), i.e., φ​(x,y)=xθ​y1−θ\varphi(x,y)=x^{\theta}y^{1-\theta} for θ∈(0,1)\theta\in(0,1). Note that the results can be generalized to a broader class of CFMMs which satisfy certain conditions on the regularity of φ\varphi. The detailed conditions are given in the [Remark˜1](https://arxiv.org/html/2602.09887v1#Thmremark1 "Remark 1. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers").

Let RnR\_{n}, LnL\_{n}, and pnp\_{n} be total reserves, liquidity, and log marginal price calculated from total reserves *after* the arbitrageurs’ trades at block nn (i.e., Ln=φ​(Rn),pn=pmargin​(Rn),Rn=R​(Ln,pn)L\_{n}=\varphi(R\_{n}),p\_{n}=p\_{\mathrm{margin}}(R\_{n}),R\_{n}=R(L\_{n},p\_{n})). Let sns\_{n} be the log of the true market price at block nn which follows Brownian motion as we discussed in [Section˜2](https://arxiv.org/html/2602.09887v1#S2 "2 Preliminaries ‣ Partially Active Automated Market Makers"), so that εn≔(sn−sn−1)∼𝒩​(μ​Δ​t,σ2​Δ​t)\varepsilon\_{n}\coloneqq(s\_{n}-s\_{n-1})\sim\mathcal{N}(\mu\Delta t,\sigma^{2}\Delta t). We define gntop≔sn−pn−1g\_{n}^{\mathrm{top}}\coloneqq s\_{n}-p\_{n-1} as the gap between the true market price and the marginal price of active reserves *before* the arbitrageurs’ trades at block nn. Throughout the paper, we will often denote it by gng\_{n} when no confusion arises. We define gnbot≔sn−png\_{n}^{\mathrm{bot}}\coloneqq s\_{n}-p\_{n} as the gap between the spot price of the asset at the AMM pool and the true price *after* the arbitrageur’s trades as well. The following proposition tells us that there exists a unique stationary distribution πΔ​t\pi\_{\Delta t} of the gap process {gn}n∈ℕ\{g\_{n}\}\_{n\in\mathbb{N}} with the estimation on its second moment up to leading order.

###### Proposition 2.

For any Δ​t>0\Delta t>0 and λ∈(0,1]\lambda\in(0,1] there exists a unique stationary distribution πΔ​t\pi\_{\Delta t} of the top-of-block gap process {gn}n∈ℕ\{g\_{n}\}\_{n\in\mathbb{N}}, and for g∼πΔ​tg\sim\pi\_{\Delta t}, as Δ​t→0\Delta t\to 0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[g2]=σ2​Δ​tλ​(2−λ)+O​(Δ​t3/2).\mathbb{E}[g^{2}]=\frac{\sigma^{2}\Delta t}{\lambda(2-\lambda)}+O(\Delta t^{3/2})\,. |  | (1) |

###### Proof.

See [Section˜A.1](https://arxiv.org/html/2602.09887v1#A1.SS1 "A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers").
∎

###### Remark 1.

The proof of [Proposition˜2](https://arxiv.org/html/2602.09887v1#Thmprop2 "Proposition 2. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers") relies on two structural properties of the induced one-step gap map: (i) the gap update can be written as an iterated random function gn+1=Ψ​(gn)+εn+1g\_{n+1}=\Psi(g\_{n})+\varepsilon\_{n+1} (or more generally gn+1=Ψ​(pn−1,gn)+εng\_{n+1}=\Psi(p\_{n-1},g\_{n})+\varepsilon\_{n}), and (ii) the map Ψ\Psi is uniformly contractive, i.e., supg|Ψ′​(g)|<1\sup\_{g}|\Psi^{\prime}(g)|<1 or supp,p+g∈K|∂gΨ​(p,g)|<1\sup\_{p,\,p+g\in K}|\partial\_{g}\Psi(p,g)|<1 on a compact price region KK.
Therefore, for any CFMM whose marginal-price map pmarginp\_{\mathrm{margin}} is sufficiently smooth and non-degenerate on a compact region KK of log prices, the same coupling/contraction argument yields existence and uniqueness of a stationary distribution for the gap process as long as the pool state and the reference price remain in KK. In practice, this “compactness” assumption can be interpreted as restricting attention to horizons where the asset price stays within a plausible range; the constants in the moment bounds then depend on KK.

From above proposition we derive several consequences that will be used throughout the paper. All of them follow directly from (i) the explicit one-block update map and (ii) a second-order Taylor expansion in the gap. The following corollary provides the justification for replacing the complex exact dynamics with a tractable linear AR(1) process in [Section˜4](https://arxiv.org/html/2602.09887v1#S4 "4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers"). Specifically, it shows that the nonlinearity in the gap process is of a higher order than the quadratic cost terms, rendering it negligible in the derivation of the leading-order optimal control.

###### Corollary 1.

Let φ\varphi be a G3M with weights (θ,1−θ)(\theta,1-\theta). Then, for any fixed δ>0\delta>0, there exists Cδ<∞C\_{\delta}<\infty depending only on δ,θ,λ\delta,\theta,\lambda, such that for all |g|≤δ|g|\leq\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | gn+1=εn+1+(1−λ)​gn+r​(gn),|r​(gn)|≤Cδ​gn2.g\_{n+1}=\varepsilon\_{n+1}+(1-\lambda)g\_{n}+r(g\_{n}),\qquad|r(g\_{n})|\leq C\_{\delta}g\_{n}^{2}. |  | (2) |

In particular, since g=Op​(Δ​t)g=O\_{p}(\sqrt{\Delta t}), the nonlinearity satisfies r​(g)=Op​(Δ​t)r(g)=O\_{p}(\Delta t), and for objectives whose leading term is quadratic in the gap (e.g., F​(g,λ)=a​(λ)​g2+o​(g2)F(g,\lambda)=a(\lambda)g^{2}+o(g^{2})), the contribution of the nonlinear remainder is of O​(Δ​t3/2)O(\Delta t^{3/2}) while FF is of O​(Δ​t)O(\Delta t). Therefore replacing the exact one-block gap map by its AR(1) linearization does not change the leading-order optimal control in [Section˜4](https://arxiv.org/html/2602.09887v1#S4 "4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers").

We next show that the liquidity per unit of LP supply grows over time even with a zero swap fee rate, due to the concavity of φ\varphi. Since we focus on the G3M case, the statement follows from an explicit closed-form computation and a Taylor expansion. A generalization to typical CFMMs, omitted here, contains a pn−1p\_{n-1}-dependent coefficient in gn2g\_{n}^{2} term.

###### Corollary 2.

Let φ​(x,y)=xθ​y1−θ\varphi(x,y)=x^{\theta}y^{1-\theta} for θ∈(0,1)\theta\in(0,1) and ℓn≔log⁡Ln\ell\_{n}\coloneqq\log L\_{n}, the *log-liquidity* of pool at block
nn after arbitrage. Then as gn→0g\_{n}\to 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓn−ℓn−1=12​λ​(1−λ)​θ​(1−θ)​gn2+O​(|gn|3).\ell\_{n}-\ell\_{n-1}=\frac{1}{2}\lambda(1-\lambda)\,\theta(1-\theta)\,g\_{n}^{2}\;+\;O(|g\_{n}|^{3}). |  | (3) |

Consequently, under the stationary regime gn∼πΔ​tg\_{n}\sim\pi\_{\Delta t} and Δ​t→0\Delta t\to 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limΔ​t→0𝔼​[ℓn−ℓn−1]Δ​t=12​λ​(1−λ)​θ​(1−θ)​limΔ​t→0𝔼​[gn2]Δ​t=θ​(1−θ)​σ22⋅1−λ2−λ.\lim\_{\Delta t\to 0}\frac{\mathbb{E}[\ell\_{n}-\ell\_{n-1}]}{\Delta t}=\frac{1}{2}\lambda(1-\lambda)\theta(1-\theta)\lim\_{\Delta t\to 0}\frac{\mathbb{E}[g\_{n}^{2}]}{\Delta t}=\frac{\theta(1-\theta)\sigma^{2}}{2}\cdot\frac{1-\lambda}{2-\lambda}. |  | (4) |

Notice that the coefficient λ​(1−λ)\lambda(1-\lambda) in [Equation˜3](https://arxiv.org/html/2602.09887v1#S3.E3 "In Corollary 2. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers") is maximized at λ=12\lambda=\tfrac{1}{2}, i.e., for a fixed small gap gng\_{n}, this choice maximizes the leading-order *per-block* increase of log-liquidity.777This is what FM-AMM introduced in [[11](https://arxiv.org/html/2602.09887v1#bib.bib5 "Arbitrageurs’ profits, lvr, and sandwich attacks: batch trading as an amm design response")] is maximizing for. The main difference is that FM-AMM closes the gap entirely, rather than partially, by leveraging the presence of a batcher that orchestrates the entire order flow from various entities. In contrast, the instantaneous rate is decreasing in λ\lambda on (0,1](0,1], and is maximized in the limit λ↓0\lambda\downarrow 0.

Next is the asymptotic analysis of loss-versus-rebalancing (LVR) for PA-AMM. Again, in the G3M case, this is an explicit computation followed by a Taylor expansion.

###### Corollary 3.

Let VnV\_{n} be the pool value at block nn after arbitrage with reference price as the pool’s marginal price,

|  |  |  |
| --- | --- | --- |
|  | Vn≔V​(Ln,Pn)=epn​x​(Ln,pn)+y​(Ln,pn).V\_{n}\coloneqq V(L\_{n},P\_{n})=e^{p\_{n}}x(L\_{n},p\_{n})+y(L\_{n},p\_{n}). |  |

Then as gn→0g\_{n}\to 0, the loss-versus-rebalancing at block nn,

|  |  |  |
| --- | --- | --- |
|  | LVRn≔V​(Ln−1,Pn−1,Sn)−V​(Ln,Pn,Sn),\mathrm{LVR}\_{n}\coloneqq V(L\_{n-1},P\_{n-1},S\_{n})-V(L\_{n},P\_{n},S\_{n}), |  |

satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | LVRn=λ2​θ​(1−θ)​Vn−1​gn2+O​(|gn|3).\mathrm{LVR}\_{n}=\frac{\lambda}{2}\,\theta(1-\theta)\,V\_{n-1}\,g\_{n}^{2}\;+\;O(|g\_{n}|^{3}). |  | (5) |

In particular, the *normalized* LVR LVR~n≔LVRn/Vn−1\widetilde{\mathrm{LVR}}\_{n}\coloneqq\mathrm{LVR}\_{n}/V\_{n-1} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | LVR~n=λ2​θ​(1−θ)​gn2+O​(|gn|3).\widetilde{\mathrm{LVR}}\_{n}=\frac{\lambda}{2}\,\theta(1-\theta)\,g\_{n}^{2}\;+\;O(|g\_{n}|^{3}). |  | (6) |

Under the stationary regime gn∼πΔ​tg\_{n}\sim\pi\_{\Delta t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | limΔ​t→0𝔼​[LVR~n]Δ​t=λ2​θ​(1−θ)​limΔ​t→0𝔼​[gn2]Δ​t=θ​(1−θ)​σ22​(2−λ).\lim\_{\Delta t\to 0}\frac{\mathbb{E}[\widetilde{\mathrm{LVR}}\_{n}]}{\Delta t}=\frac{\lambda}{2}\theta(1-\theta)\lim\_{\Delta t\to 0}\frac{\mathbb{E}[g\_{n}^{2}]}{\Delta t}=\frac{\theta(1-\theta)\sigma^{2}}{2(2-\lambda)}. |  | (7) |

By putting θ=12\theta=\frac{1}{2} and λ=1\lambda=1 into [Corollary˜3](https://arxiv.org/html/2602.09887v1#Thmcoro3 "Corollary 3. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers"), one recovers the result in [[27](https://arxiv.org/html/2602.09887v1#bib.bib2 "Automated market making and loss-versus-rebalancing")] on the instantaneous rate of LVR for CPMMs.

We note that [Corollaries˜2](https://arxiv.org/html/2602.09887v1#Thmcoro2 "Corollary 2. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers") and [3](https://arxiv.org/html/2602.09887v1#Thmcoro3 "Corollary 3. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers") together reveal a fundamental trade-off between the price gap and LVR reduction. Such a trade-off persists even when the true price is not a Brownian motion; [Figure˜1](https://arxiv.org/html/2602.09887v1#S3.F1 "In 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers") illustrates the results of the simulation using historical ETH price data. In short, as λ\lambda decreases, even in the absence of swap fees, liquidity per unit of LP token supply may grow over time, and LVR decreases. However, smaller λ\lambda results in more tracking error and reduced liquidity per single block.

In a more realistic model that allows positive swap fee rates and accounts order flow from noise traders, the two will together have a mixed effect. Reduced λ\lambda allows the LPs to set a lower swap fee rate and attract more order flow from retail while bearing the same adverse selection cost as its CFMM equivalent. However, as liquidity available per block declines, the price impact as a function of swap size will become steeper and eventually overwhelm the benefit of the lower fee rate. Whether this results in an increased share of noise traders’ order flow depends on how one models and sets the parameters of their demand, and it is beyond the scope of this paper.

![Refer to caption](x1.png)


Figure 1: 
Left. The efficient frontier of instantaneous LVR and the variance of price gap.
Middle. The cumulative LVR over time for λ∈[0.25,0.5,0.75,1]\lambda\in[0.25,0.5,0.75,1].
Right. The price gap over time for λ∈[0.25,0.5,0.75,1]\lambda\in[0.25,0.5,0.75,1]. For the middle and right panels, we used the historical ETH price from May 2025 to October 2025. All of the pools were initialized with 10001000 ETH and an equivalent amount of USDT.

## 4 Finding Optimal λ\lambda

As we saw in [Section˜3](https://arxiv.org/html/2602.09887v1#S3 "3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers"), PA-AMM introduces a fundamental trade-off: smaller activeness λ\lambda reduces loss to arbitrageurs (loss-versus-rebalancing, LVR), but increases the typical price gap between the pool’s marginal price and the true price. For G3Ms, this trade-off admits a natural portfolio interpretation. A G3M with weights (θ,1−θ)(\theta,1-\theta) can be viewed as a constant-weight portfolio that aims to keep the risky-asset value share as θ\theta. Liquidity providers (LPs) therefore face two sources of dissatisfaction: (i) a deviations of the pool’s post-arbitrage portfolio weights from their target (tracking error),888Note that the arbitrageurs always come first at each block, thus what investors (LPs) face is the post-arbitrage portfolio. and (ii) the cost of maintaining the target weights, which is the value transferred to arbitrageurs (LVR) in frictionless environment.

In this section, we formalize this trade-off as a discounted infinite-horizon stochastic control problem, where {λn}n∈ℕ\{\lambda\_{n}\}\_{n\in\mathbb{N}} is the control and the (linearized) gap process is the state. We then derive a closed-form expression for the small-Δ​t\Delta t optimal activeness λ∗\lambda^{\ast}.

### 4.1 The Problem

We start by defining the tracking error. As we mentioned above, a two-asset G3M with weights (θ,1−θ)(\theta,1-\theta) can be interpreted as a constant-weight portfolio; when the pool’s marginal price coincides with the true price, the value share invested in the risky asset XX equals θ\theta. Accordingly, we define the (post-arbitrage) risky-asset weight at block nn by

|  |  |  |
| --- | --- | --- |
|  | wn≔Sn​xnSn​xn+yn,w\_{n}\;\coloneqq\;\frac{S\_{n}\,x\_{n}}{S\_{n}\,x\_{n}+y\_{n}}, |  |

where (xn,yn)=Rn(x\_{n},y\_{n})=R\_{n} denotes the total reserves *after* arbitrage at block nn, and Sn=esnS\_{n}=e^{s\_{n}} is the true price. We take the tracking error to be the squared deviation from the target weight:

|  |  |  |
| --- | --- | --- |
|  | TEn≔(wn−θ)2.\mathrm{TE}\_{n}\;\coloneqq\;(w\_{n}-\theta)^{2}. |  |

The following lemma connects this definition to the (post-arbitrage) price gap.

###### Lemma 1.

Let φ​(x,y)=xθ​y1−θ\varphi(x,y)=x^{\theta}y^{1-\theta} with θ∈(0,1)\theta\in(0,1). For
gnbotg\_{n}^{\mathrm{bot}}, the post-arbitrage log-price gap at block nn, as gnbot→0g\_{n}^{\mathrm{bot}}\to 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | wn−θ=θ​(1−θ)​gnbot+O​((gnbot)2),TEn=θ2​(1−θ)2​(gnbot)2+O​(|gnbot|3).w\_{n}-\theta\;=\;\theta(1-\theta)\,g\_{n}^{\mathrm{bot}}\;+\;O((g\_{n}^{\mathrm{bot}})^{2}),\qquad\mathrm{TE}\_{n}\;=\;\theta^{2}(1-\theta)^{2}\,(g\_{n}^{\mathrm{bot}})^{2}\;+\;O(|g\_{n}^{\mathrm{bot}}|^{3}). |  | (8) |

Moreover, gnbot=Ψ​(gn)g\_{n}^{\mathrm{bot}}=\Psi(g\_{n}) where gn=sn−pn−1g\_{n}=s\_{n}-p\_{n-1} is the pre-arbitrage (top-of-the-block) gap and
Ψ​(g)=(1−λn)​g+O​(g2)\Psi(g)=(1-\lambda\_{n})g+O(g^{2}). Hence, as gn→0g\_{n}\to 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | TEn=θ2​(1−θ)2​(1−λn)2​gn2+O​(|gn|3).\mathrm{TE}\_{n}\;=\;\theta^{2}(1-\theta)^{2}\,(1-\lambda\_{n})^{2}g\_{n}^{2}\;+\;O(|g\_{n}|^{3}). |  | (9) |

###### Proof.

See [Section˜A.2](https://arxiv.org/html/2602.09887v1#A1.SS2 "A.2 Proof of Lemma˜1 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers").
∎

By [Lemmas˜1](https://arxiv.org/html/2602.09887v1#Thmlem1 "Lemma 1. ‣ 4.1 The Problem ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers") and [3](https://arxiv.org/html/2602.09887v1#Thmcoro3 "Corollary 3. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers"), both TEn\mathrm{TE}\_{n} and LVR~n\widetilde{\mathrm{LVR}}\_{n} admit quadratic-leading expansions in the gap. To leading order, we have

|  |  |  |
| --- | --- | --- |
|  | TEn≈θ2​(1−θ)2​(1−λn)2​gn2,LVR~n≈λn2​θ​(1−θ)​gn2,\mathrm{TE}\_{n}\approx\theta^{2}(1-\theta)^{2}(1-\lambda\_{n})^{2}g\_{n}^{2},\qquad\widetilde{\mathrm{LVR}}\_{n}\approx\frac{\lambda\_{n}}{2}\theta(1-\theta)g\_{n}^{2}, |  |

and for the portfolio manager who weights the LVR cost γ′\gamma^{\prime} times more than the tracking error, the one-stage cost becomes

|  |  |  |
| --- | --- | --- |
|  | TEn+γ′​LVR~n∝((1−λn)2+γ​λn)​gn2,\mathrm{TE}\_{n}+\gamma^{\prime}\widetilde{\mathrm{LVR}}\_{n}\propto((1-\lambda\_{n})^{2}+\gamma\lambda\_{n})g\_{n}^{2}\,, |  |

where γ≔γ′2​θ​(1−θ)\gamma\coloneqq\frac{\gamma^{\prime}}{2\theta(1-\theta)} is the constant that absorbs the fixed factors for notational convenience. We define the objective functional as a weighted sum of one-stage costs discounted at a rate ϱ>0\varrho>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​({λn})≔𝔼​[∑n=1∞e−ϱ​n​Δ​t​(TEn+γ′​LVR~n)].\mathcal{J}(\{\lambda\_{n}\})\;\coloneqq\;\mathbb{E}\!\left[\sum\_{n=1}^{\infty}e^{-\varrho n\Delta t}\big(\mathrm{TE}\_{n}+\gamma^{\prime}\,\widetilde{\mathrm{LVR}}\_{n}\big)\right]\,. |  | (10) |

Since multiplicative constants do not affect the optimizer of {λn}\{\lambda\_{n}\}, we work with the leading-order approximate objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​({λn})≈𝔼​[∑n=1∞e−ϱ​n​Δ​t​((1−λn)2+γ​λn)​gn2].\mathcal{J}(\{\lambda\_{n}\})\;\approx\;\mathbb{E}\!\left[\sum\_{n=1}^{\infty}e^{-\varrho n\Delta t}\Big((1-\lambda\_{n})^{2}+\gamma\lambda\_{n}\Big)g\_{n}^{2}\right]. |  | (11) |

We further assume that there exists a strictly positive lower bound λ¯\underline{\lambda} on possible λn\lambda\_{n} to ensure the finiteness of the moments of gng\_{n} and the validity of its linearized update rule, which justifies the solution introduced below under a small Δ​t\Delta t regime.999We also remark that [[19](https://arxiv.org/html/2602.09887v1#bib.bib30 "Optimal fees for geometric mean market makers")] defined a loss functional of almost the same form to find the optimal fee rate. The main difference is that here we optimize for the activeness λ\lambda while fixing the fee rate to 0. The final optimization problem we solve is then:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min{λn}n∈ℕ\displaystyle\min\_{\{\lambda\_{n}\}\_{n\in\mathbb{N}}} | 𝔼​[∑n=1∞e−ϱ​n​Δ​t​((1−λn)2+γ​λn)​gn2]\displaystyle\mathbb{E}\!\left[\sum\_{n=1}^{\infty}e^{-\varrho n\Delta t}\Big((1-\lambda\_{n})^{2}+\gamma\lambda\_{n}\Big)g\_{n}^{2}\right] |  | (12) |
|  | subject to | gn+1=(1−λn)​gn+εn+1,εn+1∼𝒩​(μ​Δ​t,σ2​Δ​t)i.i.d.,\displaystyle g\_{n+1}=(1-\lambda\_{n})g\_{n}+\varepsilon\_{n+1},\quad\varepsilon\_{n+1}\sim\mathcal{N}(\mu\Delta t,\sigma^{2}\Delta t)\quad\text{i.i.d.,} |  |
|  |  | λn∈[λ¯,1].\displaystyle\lambda\_{n}\in[\underline{\lambda},1]. |  |

### 4.2 Solution

The solution to our problem always and uniquely exists within [λ¯,1][\underline{\lambda},1], for small enough Δ​t\Delta t, i.e., a fast enough block production regime.

###### Theorem 1.

The optimal policy (for g≠0g\neq 0) is of feedback form

|  |  |  |  |
| --- | --- | --- | --- |
|  | λopt​(g)=clip​(1−γ2​(1+β​v2)+β​(2​v2​μ​Δ​t+v1)2​(1+β​v2)⋅1g,λ¯,1),\lambda^{\mathrm{opt}}(g)\;=\;\mathrm{clip}\left(1-\frac{\gamma}{2(1+\beta v\_{2})}+\frac{\beta(2v\_{2}\mu\Delta t+v\_{1})}{2(1+\beta v\_{2})}\cdot\frac{1}{g},\underline{\lambda},1\right), |  | (13) |

where clip​(x,l,u)≔min⁡(max⁡(x,l),u)\mathrm{clip}(x,l,u)\coloneqq\min(\max(x,l),u), β≔e−ϱ​Δ​t\beta\coloneqq e^{-\varrho\Delta t}, and (v2,v1,v0)(v\_{2},v\_{1},v\_{0}) are the coefficients of the quadratic value function V​(g)=v2​g2+v1​g+v0V(g)=v\_{2}g^{2}+v\_{1}g+v\_{0} uniquely solving the Bellman equation. Moreover, as Δ​t→0\Delta t\to 0, the state-dependent term vanishes under the stationary scaling g=Op​(Δ​t)g=O\_{p}(\sqrt{\Delta t}), and the optimal activeness converges to the constant

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗​(γ)≔1+1+2​γ1+γ+1+2​γ,\lambda^{\ast}(\gamma)\coloneqq\frac{1+\sqrt{1+2\gamma}}{1+\gamma+\sqrt{1+2\gamma}}, |  | (14) |

i.e., λopt​(g)=λ∗​(γ)+Op​(Δ​t)\lambda^{\mathrm{opt}}(g)=\lambda^{\ast}(\gamma)+O\_{p}(\sqrt{\Delta t}).

###### Proof.

See [Section˜A.3](https://arxiv.org/html/2602.09887v1#A1.SS3 "A.3 Proof of Theorem˜1 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers").
∎

![Refer to caption](x2.png)


Figure 2: (Left) Leading-order loss λ↦𝔼​[((1−λ)2+γ​λ)​g2]\lambda\mapsto\mathbb{E}[((1-\lambda)^{2}+\gamma\lambda)g^{2}] for γ=4\gamma=4 under the stationary
AR(1) approximation. (Right) The small-Δ​t\Delta t asymptotic optimizer λ∗​(γ)\lambda^{\ast}(\gamma) for γ∈[0,10]\gamma\in[0,10].

## 5 Conclusion

In this work, we introduced a new class of AMM, named PA-AMM, that partitions liquidity into two types, active and passive, and uses only the active portion for trading, thereby limiting the available liquidity within a single block. Such a limit effectively works by gradually executing the rebalancing trade over time, eventually reducing LVR and improving LPs’ wealth. As a trade-off, the pool’s marginal price may deviate from the true market price. We defined and solved the optimization problem that balances this trade-off.

However, in this work, we abstracted away the gas cost and set the trading fee to 0. Future work is needed to extend the model to a more realistic setting. In that setting, the optimization problem would need to be adjusted to find an optimal combination of fee rate and activeness. Also, in our work, the relative weight of the rebalancing cost, γ\gamma, was held constant. One may consider a variant in which γ\gamma varies according to market conditions, such as volatility. Adding the order flow from noise traders, which would likely increase with λ\lambda, to the optimization problem would also be an interesting direction.

We conclude with a remark on potential applications. Given that the loss incurred by LPs to arbitrageurs for each block is a λ\lambda share of the maximum possible loss, PA-AMM may be a better option for liquidity provision to prediction markets, where LPs face much larger adverse selection costs. Consider a CFMM with two underlying tokens, YES and NO, for a given topic. In this market, LPs’ wealth could go to zero within a single block, since one of the tokens will become 0 in value after the arrival of informed traders (arbitrageurs). That is, no matter how small the difference, if LPs’ withdrawals occur after arbitrageurs’ taker orders, LPs will lose all their wealth. This is not the case for PA-AMM, where LPs lose only a λ\lambda portion of their wealth per block; thus, the lower the latency, the less they lose, making the loss a continuous function of latency, which could potentially incentivize the LPs to provide more liquidity.

## References

* [1]
  A. Adams, C. C. Moallemi, S. Reynolds, and D. Robinson (2024)
  Am-amm: an auction-managed automated market maker.
  arXiv preprint arXiv:2403.03367.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [2]
  H. Adams, N. Zinsmeister, M. Salem, R. Keefer, and D. Robinson (2021)
  Uniswap v3 core.
  Note: <https://uniswap.org/whitepaper-v3.pdf>
  Cited by: [footnote 2](https://arxiv.org/html/2602.09887v1#footnote2 "In 1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [3]
  A. A. Aigner and G. Dhaliwal (2021-06)
  UNISWAP: impermanent loss and risk profile of a liquidity provider.
  Technical report
   SSRN.
  Note: SSRN Working Paper. Posted Jul 8, 2021; Date Written Jun 23, 2021. DOI: 10.2139/ssrn.3872531
  External Links: [Link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3872531)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [4]
  A. Alexander and L. Fritz (2024)
  Fees in amms: a quantitative study.
  arXiv preprint arXiv:2406.12417.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p3.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [5]
  R. Almgren and N. Chriss (2001)
  Optimal execution of portfolio transactions.
  Journal of Risk 3 (2),  pp. 5–39.
  External Links: [Link](https://www.risk.net/journal-risk/2161150/optimal-execution-portfolio-transactions),
  [Document](https://dx.doi.org/10.21314/JOR.2001.041)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [6]
  L. Baggiani, M. Herdegen, and L. Sánchez-Betancourt (2025)
  Optimal dynamic fees in automated market makers.
  arXiv preprint arXiv:2506.02869.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [7]
  Balancer
  Liquidity bootstrapping pool.
  Note: <https://docs.balancer.fi/concepts/explore-available-balancer-pools/liquidity-bootstrapping-pool.html>
  Cited by: [footnote 2](https://arxiv.org/html/2602.09887v1#footnote2 "In 1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [8]
  K. Benidis, Y. Feng, and D. P. Palomar (2018)
  Optimization methods for financial index tracking: from theory to practice.
  Foundations and Trends® in Optimization 3 (3),  pp. 171–279.
  External Links: [Link](http://dx.doi.org/10.1561/2400000021),
  [Document](https://dx.doi.org/10.1561/2400000021),
  ISSN 2167-3888
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [9]
  A. Bukov and M. Melnik (2020)
  Mooniswap.
  Note: <https://blockchainwelt.de/wp-content/uploads/2023/05/1inch-whitepaper.pdf>
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [10]
  S. Campbell, P. Bergault, J. Milionis, and M. Nutz (2025)
  Optimal fees for liquidity provision in automated market makers.
  arXiv preprint arXiv:2508.08152.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p3.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [11]
  A. Canidio and R. Fritsch (2023)
  Arbitrageurs’ profits, lvr, and sandwich attacks: batch trading as an amm design response.
  arXiv preprint arXiv:2307.02074.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers"),
  [footnote 5](https://arxiv.org/html/2602.09887v1#footnote5 "In 3.1 The Partial Usage of Reserves and Periodic Rebalancing ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers"),
  [footnote 7](https://arxiv.org/html/2602.09887v1#footnote7 "In 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers").
* [12]
  Á. Cartea, F. Drissi, and M. Monga (2023)
  Predictable losses of liquidity provision in constant function markets and concentrated liquidity markets.
  Applied Mathematical Finance 30 (2),  pp. 69–93.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [13]
  Á. Cartea, F. Drissi, and M. Monga (2024)
  Decentralized finance and automated market making: predictable loss and optimal liquidity provision.
  SIAM Journal on Financial Mathematics 15 (3),  pp. 931–959.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p3.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [14]
  Á. Cartea, F. Drissi, L. Sánchez-Betancourt, D. Siska, and L. Szpruch (2024)
  Strategic bonding curves in automated market makers.
  SSRN preprint.
  External Links: 5018420,
  [Document](https://dx.doi.org/10.2139/ssrn.5018420),
  [Link](https://dx.doi.org/10.2139/ssrn.5018420)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [15]
  CrocSwap (2022)
  Designing a dynamic fee policy that outperforms all uniswap eth/usdc pools.
  Note: <https://crocswap.medium.com/designing-a-dynamic-fee-policy-that-outperforms-all-uniswap-eth-usdc-pools-8948b0cc72ab>
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [16]
  Deribit Insights (2020-07)
  Impermanent loss and bancor v2.
  Note: <https://insights.deribit.com/market-research/impermanence-loss-and-bancor-v2/>
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [17]
  C. Donohue and K. Yip (2003)
  Optimal portfolio rebalancing with transaction costs.
  The Journal of Portfolio Management 29 (4),  pp. 49–63.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2003.319894)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [18]
  M. Egorov (2021)
  Automatic market-making with dynamic peg.
  Note: <https://docs.curve.finance/assets/pdf/whitepaper_cryptoswap.pdf>
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [19]
  A. Evans, G. Angeris, and T. Chitra (2021)
  Optimal fees for geometric mean market makers.
  In International Conference on Financial Cryptography and Data Security,
   pp. 65–79.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p3.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers"),
  [footnote 9](https://arxiv.org/html/2602.09887v1#footnote9 "In 4.1 The Problem ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers").
* [20]
  A. Evans (2020)
  Liquidity provider returns in geometric mean markets.
  arXiv preprint arXiv:2006.08806.
  Cited by: [§2](https://arxiv.org/html/2602.09887v1#S2.p1.1 "2 Preliminaries ‣ Partially Active Automated Market Makers").
* [21]
  R. Fritsch, M. I. Silva, A. Mamageishvili, B. Livshits, and E. W. Felten (2024)
  MEV capture through time-advantaged arbitrage.
  arXiv preprint arXiv:2410.10797.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [22]
  N. Gârleanu and L. H. Pedersen (2013)
  Dynamic trading with predictable returns and transaction costs.
  The Journal of Finance 68 (6),  pp. 2309–2340.
  External Links: [Document](https://dx.doi.org/10.1111/jofi.12080)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [23]
  N. Gârleanu and L. H. Pedersen (2016)
  Dynamic portfolio choice with frictions.
  Journal of Economic Theory 165,  pp. 487–516.
  External Links: [Document](https://dx.doi.org/10.1016/j.jet.2016.06.001)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [24]
  H. Holden and L. Holden (2013)
  Optimal rebalancing of portfolios with transaction costs.
  Stochastics 85 (3),  pp. 371–394.
  External Links: [Document](https://dx.doi.org/10.1080/17442508.2011.651219)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [25]
  A. S. Kyle and J. Lee (2017-11)
  Toward a fully continuous exchange.
  Oxford Review of Economic Policy 33 (4),  pp. 650–675.
  External Links: ISSN 0266-903X,
  [Document](https://dx.doi.org/10.1093/oxrep/grx042),
  [Link](https://doi.org/10.1093/oxrep/grx042),
  https://academic.oup.com/oxrep/article-pdf/33/4/650/21515800/grx042.pdf
  Cited by: [footnote 6](https://arxiv.org/html/2602.09887v1#footnote6 "In 3.1 The Partial Usage of Reserves and Periodic Rebalancing ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers").
* [26]
  J. Ma and D. Crapis (2024)
  The cost of permissionless liquidity provision in automated market makers.
  In The International Conference on Mathematical Research for Blockchain Economy,
   pp. 55–69.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p3.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [27]
  J. Milionis, C. C. Moallemi, T. Roughgarden, and A. L. Zhang (2022)
  Automated market making and loss-versus-rebalancing.
  arXiv preprint arXiv:2208.06046.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers"),
  [§2.3](https://arxiv.org/html/2602.09887v1#S2.SS3.p1.2 "2.3 Loss-versus-rebalancing ‣ 2 Preliminaries ‣ Partially Active Automated Market Makers"),
  [§3.2](https://arxiv.org/html/2602.09887v1#S3.SS2.p7.2 "3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers"),
  [Proposition 1](https://arxiv.org/html/2602.09887v1#Thmprop1 "Proposition 1 (Theorem 1 of [27]). ‣ 2.3 Loss-versus-rebalancing ‣ 2 Preliminaries ‣ Partially Active Automated Market Makers").
* [28]
  J. Milionis, C. C. Moallemi, and T. Roughgarden (2024)
  Automated market making and arbitrage profits in the presence of fees.
  In International Conference on Financial Cryptography and Data Security,
   pp. 159–171.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [29]
  A. Nezlobin and M. Tassy (2025)
  Loss-versus-rebalancing under deterministic and generalized block-times.
  arXiv preprint arXiv:2505.05113.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [30]
  A. A. Obizhaeva and J. Wang (2013)
  Optimal trading strategy and supply/demand dynamics.
  Journal of Financial markets 16 (1),  pp. 1–32.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p5.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [31]
  Pintail (2019)
  Understanding uniswap returns.
  Note: Medium
  External Links: [Link](https://pintail.medium.com/understanding-uniswap-returns-cc593f3499ef)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [32]
  Pintail (2019)
  Uniswap: a good deal for liquidity providers?.
  Note: Medium
  External Links: [Link](https://pintail.medium.com/uniswap-a-good-deal-for-liquidity-providers-104c0b6816f2)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [33]
  C. Powers (2024)
  A tick-by-tick solution for concentrated liquidity provisioning.
  arXiv preprint arXiv:2405.18728.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p3.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [34]
  G. Ramseyer, M. Goyal, A. Goel, and D. Mazières (2024)
  Augmenting batch exchanges with constant function market makers.
  In Proceedings of the 25th ACM Conference on Economics and Computation,
   pp. 986–1016.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [35]
  C. Schlegel and Q. Kilbourn (2025)
  Arbitrage with bounded liquidity.
  arXiv preprint arXiv:2507.02027.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p2.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [36]
  solarcurve (2023)
  [BIP-295] fee discount for cowswap solvers.
  Note: <https://forum.balancer.fi/t/bip-295-fee-discount-for-cowswap-solvers/4785>
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p4.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [37]
  V. Volosnikov, A. Pimenov, and V. Tikhomirov (2024-01-29)
  The impact of market conditions and fee algorithms on the design of a competitive amm.
  Technical report
   Algebra Protocol.
  External Links: [Link](https://algebra.finance/static/the-impact-of-market-conditions-and-fee-algorithms-on-the-design-of-a-competitive-amm.pdf)
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p3.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").
* [38]
  F. Wu, D. Sui, T. Thiery, and M. Pai (2025)
  Measuring cex-dex extracted value and searcher profitability: the darkest of the mev dark forest.
  arXiv preprint arXiv:2507.13023.
  Cited by: [§1.1](https://arxiv.org/html/2602.09887v1#S1.SS1.p1.1 "1.1 Background and Related Works ‣ 1 Introduction ‣ Partially Active Automated Market Makers").

## Appendix A Proofs

### A.1 Proof of [Proposition˜2](https://arxiv.org/html/2602.09887v1#Thmprop2 "Proposition 2. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers")

###### Proof.

Recall that the underlying CFMM invariant is φ​(x,y)=xθ​y1−θ\varphi(x,y)=x^{\theta}y^{1-\theta} with θ∈(0,1)\theta\in(0,1). Fix λ∈(0,1]\lambda\in(0,1] and let εn∼𝒩​(μ​Δ​t,σ2​Δ​t)\varepsilon\_{n}\sim\mathcal{N}(\mu\Delta t,\sigma^{2}\Delta t) i.i.d. For G3M, one checks that

|  |  |  |
| --- | --- | --- |
|  | pmargin​((1−λ)​R​(1,p)+λ​R​(1,p+g))=p+log⁡(1−λ+λ​eθ​g)−log⁡(1−λ+λ​e−(1−θ)​g).p\_{\mathrm{margin}}\big((1-\lambda)R(1,p)+\lambda R(1,p+g)\big)=p+\log\!\big(1-\lambda+\lambda e^{\theta g}\big)-\log\!\big(1-\lambda+\lambda e^{-(1-\theta)g}\big). |  |

Hence, the exact one-step recursion of the top-gap is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | gn+1=εn+1+Ψ​(gn),Ψ​(g)≔g−(log⁡(1−λ+λ​eθ​g)−log⁡(1−λ+λ​e−(1−θ)​g)).g\_{n+1}=\varepsilon\_{n+1}+\Psi(g\_{n}),\qquad\Psi(g)\coloneqq g-\Big(\log(1-\lambda+\lambda e^{\theta g})-\log(1-\lambda+\lambda e^{-(1-\theta)g})\Big). |  | (15) |

In particular, Ψ\Psi does not depend on pp. We first compute Ψ′​(g)\Psi^{\prime}(g). Differentiating,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ′​(g)=1−λ​θ​eθ​g1−λ+λ​eθ​g−λ​(1−θ)​e−(1−θ)​g1−λ+λ​e−(1−θ)​g.\Psi^{\prime}(g)=1-\frac{\lambda\theta e^{\theta g}}{1-\lambda+\lambda e^{\theta g}}-\frac{\lambda(1-\theta)e^{-(1-\theta)g}}{1-\lambda+\lambda e^{-(1-\theta)g}}. |  | (16) |

Since each fraction of ([16](https://arxiv.org/html/2602.09887v1#A1.E16 "Equation 16 ‣ Proof. ‣ A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")) satiesfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​θ​eθ​g1−λ+λ​eθ​g\displaystyle\frac{\lambda\theta e^{\theta g}}{1-\lambda+\lambda e^{\theta g}} | ≥λ​θif ​g≥0,\displaystyle\geq\lambda\theta\quad\text{if }g\geq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(1−θ)​e−(1−θ)​g1−λ+λ​e−(1−θ)​g\displaystyle\frac{\lambda(1-\theta)e^{-(1-\theta)g}}{1-\lambda+\lambda e^{-(1-\theta)g}} | ≥λ​(1−θ)if ​g≤0,\displaystyle\geq\lambda(1-\theta)\quad\text{if }g\leq 0, |  |

while always lie in [0,θ]\left[0,\theta\right] and [0,1−θ]\left[0,1-\theta\right], respectively, we have

|  |  |  |
| --- | --- | --- |
|  | 0≤Ψ′​(g)≤1−λ​min⁡{θ,(1−θ)}≕ρ∈(0,1).0\leq\Psi^{\prime}(g)\leq 1-\lambda\min\{\theta,(1-\theta)\}\eqqcolon\rho\in(0,1). |  |

Combining Ψ​(0)=0\Psi(0)=0 and the mean value theorem one gets

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Ψ​(g)|≤ρ​|g|,∀g∈ℝ,|\Psi(g)|\leq\rho|g|,\qquad\forall g\in\mathbb{R}, |  | (17) |

and more generally |Ψ​(g)−Ψ​(h)|≤ρ​|g−h||\Psi(g)-\Psi(h)|\leq\rho|g-h| for all g,hg,h. Define the random affine map Fε​(x)≔Ψ​(x)+εF\_{\varepsilon}(x)\coloneqq\Psi(x)+\varepsilon. Then ([15](https://arxiv.org/html/2602.09887v1#A1.E15 "Equation 15 ‣ Proof. ‣ A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")) is gn+1=Fεn+1​(gn)g\_{n+1}=F\_{\varepsilon\_{n+1}}(g\_{n}). Couple two versions {gn}\{g\_{n}\}, {gn′}\{g^{\prime}\_{n}\} by using the same innovations εn\varepsilon\_{n}. Then by the Lipschitz property of Ψ\Psi,

|  |  |  |
| --- | --- | --- |
|  | |gn+1−gn+1′|=|Ψ​(gn)−Ψ​(gn′)|≤ρ​|gn−gn′|≤ρn​|g1−g1′|.|g\_{n+1}-g^{\prime}\_{n+1}|=|\Psi(g\_{n})-\Psi(g^{\prime}\_{n})|\leq\rho|g\_{n}-g^{\prime}\_{n}|\leq\rho^{n}|g\_{1}-g^{\prime}\_{1}|. |  |

Therefore, the coupled distance contracts exponentially almost surely. Since Ψ\Psi is globally Lipschitz with constant ρ<1\rho<1, the Markov chain is a contractive iterated random function, and it admits a unique invariant distribution and converges to it geometrically.

For the second part, let g∼πΔ​tg\sim\pi\_{\Delta t} and let ε\varepsilon be an independent copy of εn+1\varepsilon\_{n+1}. Then g​=𝑑​Ψ​(g)+εg\overset{d}{=}\Psi(g)+\varepsilon.
Taking absolute values and using ([17](https://arxiv.org/html/2602.09887v1#A1.E17 "Equation 17 ‣ Proof. ‣ A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")),

|  |  |  |
| --- | --- | --- |
|  | |g|≤|Ψ​(g)|+|ε|≤ρ​|g|+|ε|,|g|\leq|\Psi(g)|+|\varepsilon|\leq\rho|g|+|\varepsilon|, |  |

hence |g|≤(1−ρ)−1​|ε||g|\leq(1-\rho)^{-1}|\varepsilon| in LmL^{m} for any m≥1m\geq 1. More precisely, iterating as in a geometric series yields

|  |  |  |
| --- | --- | --- |
|  | ‖g‖m≤11−ρ​‖ε‖m,m≥1.\|g\|\_{m}\leq\frac{1}{1-\rho}\,\|\varepsilon\|\_{m},\qquad m\geq 1. |  |

Since ε∼𝒩​(μ​Δ​t,σ2​Δ​t)\varepsilon\sim\mathcal{N}(\mu\Delta t,\sigma^{2}\Delta t), we have ‖ε‖m=O​(Δ​t)\|\varepsilon\|\_{m}=O(\sqrt{\Delta t}), so in particular

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[g2]=O​(Δ​t),𝔼​[|g|3]=O​(Δ​t3/2),𝔼​[g4]=O​(Δ​t2).\mathbb{E}[g^{2}]=O(\Delta t),\qquad\mathbb{E}[|g|^{3}]=O(\Delta t^{3/2}),\qquad\mathbb{E}[g^{4}]=O(\Delta t^{2}). |  | (18) |

A direct computation gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ψ′′​(g)\displaystyle\Psi^{\prime\prime}(g) | =−∂2∂g2​(log⁡(1−λ+λ​eθ​g)−log⁡(1−λ+λ​e−(1−θ)​g))\displaystyle=-\,\frac{\partial^{2}}{\partial g^{2}}\Big(\log(1-\lambda+\lambda e^{\theta g})-\log(1-\lambda+\lambda e^{-(1-\theta)g})\Big) |  | (19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−λ​(1−λ)​[θ2​eθ​g(1−λ+λ​eθ​g)2−(1−θ)2​e−(1−θ)​g(1−λ+λ​e−(1−θ)​g)2].\displaystyle=-\lambda(1-\lambda)\!\left[\frac{\theta^{2}e^{\theta g}}{(1-\lambda+\lambda e^{\theta g})^{2}}-\frac{(1-\theta)^{2}e^{-(1-\theta)g}}{(1-\lambda+\lambda e^{-(1-\theta)g})^{2}}\right]. |  | (20) |

Using supz>0z(A+B​z)2=14​A​B\sup\_{z>0}\frac{z}{(A+Bz)^{2}}=\frac{1}{4AB}, we get the global bound

|  |  |  |
| --- | --- | --- |
|  | supg∈ℝ|Ψ′′​(g)|≤λ​(1−λ)​(θ2​14​λ​(1−λ)+(1−θ)24​λ​(1−λ))=θ2+(1−θ)24≤14.\sup\_{g\in\mathbb{R}}|\Psi^{\prime\prime}(g)|\leq\lambda(1-\lambda)\left(\theta^{2}\frac{1}{4\lambda(1-\lambda)}+\frac{(1-\theta)^{2}}{4\lambda(1-\lambda)}\right)=\frac{\theta^{2}+(1-\theta)^{2}}{4}\leq\frac{1}{4}. |  |

Therefore, using Taylor’s theorem, one gets

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(g)=(1−λ)​g+r​(g),|r​(g)|≤12​supu∈ℝ|Ψ′′​(u)|​g2≤18​g2,∀g∈ℝ.\Psi(g)=(1-\lambda)g+r(g),\qquad|r(g)|\leq\frac{1}{2}\sup\_{u\in\mathbb{R}}|\Psi^{\prime\prime}(u)|\,g^{2}\leq\frac{1}{8}g^{2},\quad\forall g\in\mathbb{R}. |  | (21) |

Using stationarity g​=𝑑​Ψ​(g)+εg\overset{d}{=}\Psi(g)+\varepsilon with g⟂⟂εg\perp\!\!\!\perp\varepsilon,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[g2]=𝔼​[Ψ​(g)2]+𝔼​[ε2]+2​𝔼​[Ψ​(g)]​𝔼​[ε].\mathbb{E}[g^{2}]=\mathbb{E}[\Psi(g)^{2}]+\mathbb{E}[\varepsilon^{2}]+2\,\mathbb{E}[\Psi(g)]\,\mathbb{E}[\varepsilon]. |  |

Write Ψ​(g)=(1−λ)​g+r​(g)\Psi(g)=(1-\lambda)g+r(g) as in ([21](https://arxiv.org/html/2602.09887v1#A1.E21 "Equation 21 ‣ Proof. ‣ A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")). Expanding and rearranging, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(2−λ)​𝔼​[g2]=𝔼​[ε2]+2​(1−λ)​𝔼​[g]​𝔼​[ε]+2​𝔼​[r​(g)]​𝔼​[ε]+2​(1−λ)​𝔼​[g​r​(g)]+𝔼​[r​(g)2].\lambda(2-\lambda)\mathbb{E}[g^{2}]=\mathbb{E}[\varepsilon^{2}]+2(1-\lambda)\mathbb{E}[g]\,\mathbb{E}[\varepsilon]+2\,\mathbb{E}[r(g)]\,\mathbb{E}[\varepsilon]+2(1-\lambda)\mathbb{E}[g\,r(g)]+\mathbb{E}[r(g)^{2}]. |  | (22) |

Now we bound the error terms. First, 𝔼​[ε]=μ​Δ​t\mathbb{E}[\varepsilon]=\mu\Delta t and 𝔼​[ε2]=σ2​Δ​t+μ2​Δ​t2\mathbb{E}[\varepsilon^{2}]=\sigma^{2}\Delta t+\mu^{2}\Delta t^{2}. Second, taking expectations in g=Ψ​(g)+εg=\Psi(g)+\varepsilon gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[g]=(1−λ)​𝔼​[g]+𝔼​[r​(g)]+𝔼​[ε]⟹λ​𝔼​[g]=𝔼​[r​(g)]+μ​Δ​t.\mathbb{E}[g]=(1-\lambda)\mathbb{E}[g]+\mathbb{E}[r(g)]+\mathbb{E}[\varepsilon]\quad\Longrightarrow\quad\lambda\,\mathbb{E}[g]=\mathbb{E}[r(g)]+\mu\Delta t. |  |

Using |r​(g)|≤18​g2|r(g)|\leq\frac{1}{8}g^{2} and 𝔼​[g2]=O​(Δ​t)\mathbb{E}[g^{2}]=O(\Delta t) from ([18](https://arxiv.org/html/2602.09887v1#A1.E18 "Equation 18 ‣ Proof. ‣ A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")), we get 𝔼​[r​(g)]=O​(Δ​t)\mathbb{E}[r(g)]=O(\Delta t), hence 𝔼​[g]=O​(Δ​t)\mathbb{E}[g]=O(\Delta t). Therefore 𝔼​[g]​𝔼​[ε]=O​(Δ​t2)\mathbb{E}[g]\mathbb{E}[\varepsilon]=O(\Delta t^{2}) and 𝔼​[r​(g)]​𝔼​[ε]=O​(Δ​t2)\mathbb{E}[r(g)]\mathbb{E}[\varepsilon]=O(\Delta t^{2}). Next, by |r​(g)|≤18​g2|r(g)|\leq\frac{1}{8}g^{2} and ([18](https://arxiv.org/html/2602.09887v1#A1.E18 "Equation 18 ‣ Proof. ‣ A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")),

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[g​r​(g)]|≤𝔼​[|g|​|r​(g)|]≤18​𝔼​[|g|3]=O​(Δ​t3/2),|\mathbb{E}[g\,r(g)]|\leq\mathbb{E}[|g|\,|r(g)|]\leq\frac{1}{8}\mathbb{E}[|g|^{3}]=O(\Delta t^{3/2}), |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[r​(g)2]≤164​𝔼​[g4]=O​(Δ​t2).\mathbb{E}[r(g)^{2}]\leq\frac{1}{64}\mathbb{E}[g^{4}]=O(\Delta t^{2}). |  |

Plugging these into ([22](https://arxiv.org/html/2602.09887v1#A1.E22 "Equation 22 ‣ Proof. ‣ A.1 Proof of Proposition˜2 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")) yields

|  |  |  |
| --- | --- | --- |
|  | λ​(2−λ)​𝔼​[g2]=σ2​Δ​t+O​(Δ​t3/2).\lambda(2-\lambda)\mathbb{E}[g^{2}]=\sigma^{2}\Delta t+O(\Delta t^{3/2}). |  |

Thus

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[g2]=σ2​Δ​tλ​(2−λ)+O​(Δ​t3/2),\mathbb{E}[g^{2}]=\frac{\sigma^{2}\Delta t}{\lambda(2-\lambda)}+O(\Delta t^{3/2}), |  |

which is the desired leading-order stationary second moment expansion.
∎

### A.2 Proof of [Lemma˜1](https://arxiv.org/html/2602.09887v1#Thmlem1 "Lemma 1. ‣ 4.1 The Problem ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers")

###### Proof.

Recall that for G3M the marginal price Pmargin=θ1−θ​yxP\_{\mathrm{margin}}=\frac{\theta}{1-\theta}\frac{y}{x}. At the post-arbitrage reserves (xn,yn)(x\_{n},y\_{n}), we have yn=1−θθ​Pn​xny\_{n}=\frac{1-\theta}{\theta}P\_{n}x\_{n} where Pn=epnP\_{n}=e^{p\_{n}}. Therefore

|  |  |  |
| --- | --- | --- |
|  | wn=Sn​xnSn​xn+yn=Sn​xnSn​xn+1−θθ​Pn​xn=11+1−θθ​PnSn=11+1−θθ​e−(sn−pn)=f​(gnbot),w\_{n}=\frac{S\_{n}x\_{n}}{S\_{n}x\_{n}+y\_{n}}=\frac{S\_{n}x\_{n}}{S\_{n}x\_{n}+\frac{1-\theta}{\theta}P\_{n}x\_{n}}=\frac{1}{1+\frac{1-\theta}{\theta}\frac{P\_{n}}{S\_{n}}}=\frac{1}{1+\frac{1-\theta}{\theta}e^{-(s\_{n}-p\_{n})}}=f(g\_{n}^{\mathrm{bot}}), |  |

where f​(u)≔(1+1−θθ​e−u)−1f(u)\coloneqq\big(1+\frac{1-\theta}{\theta}e^{-u}\big)^{-1}. One checks f​(0)=θf(0)=\theta and

|  |  |  |
| --- | --- | --- |
|  | f′​(u)=1−θθ​e−u(1+1−θθ​e−u)2,f′​(0)=1−θθ(1+1−θθ)2=θ​(1−θ).f^{\prime}(u)=\frac{\frac{1-\theta}{\theta}e^{-u}}{\big(1+\frac{1-\theta}{\theta}e^{-u}\big)^{2}},\qquad f^{\prime}(0)=\frac{\frac{1-\theta}{\theta}}{(1+\frac{1-\theta}{\theta})^{2}}=\theta(1-\theta). |  |

Hence wn−θ=f′​(0)​gnbot+O​((gnbot)2)w\_{n}-\theta=f^{\prime}(0)\,g\_{n}^{\mathrm{bot}}+O((g\_{n}^{\mathrm{bot}})^{2}), giving ([8](https://arxiv.org/html/2602.09887v1#S4.E8 "Equation 8 ‣ Lemma 1. ‣ 4.1 The Problem ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers")). The second statement comes directly from [Corollary˜1](https://arxiv.org/html/2602.09887v1#Thmcoro1 "Corollary 1. ‣ 3.2 The Dynamics ‣ 3 PA-AMM and Its Properties ‣ Partially Active Automated Market Makers").
∎

### A.3 Proof of [Theorem˜1](https://arxiv.org/html/2602.09887v1#Thmthm1 "Theorem 1. ‣ 4.2 Solution ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers")

###### Proof.

Let u≔1−λ∈[0,1−λ¯]u\coloneqq 1-\lambda\in[0,1-\underline{\lambda}]. The dynamics becomes gn+1=un​gn+εn+1g\_{n+1}=u\_{n}g\_{n}+\varepsilon\_{n+1}, and the one-stage cost is

|  |  |  |
| --- | --- | --- |
|  | L​(g,u)=(u2+γ​(1−u))​g2=(u2−γ​u+γ)​g2.L(g,u)=\big(u^{2}+\gamma(1-u)\big)g^{2}=(u^{2}-\gamma u+\gamma)g^{2}. |  |

The Bellman equation is then

|  |  |  |
| --- | --- | --- |
|  | V​(g)=minu∈[0,1−λ¯]⁡{(u2−γ​u+γ)​g2+β​𝔼​[V​(u​g+ε)]}.V(g)=\min\_{u\in[0,1-\underline{\lambda}]}\Big\{(u^{2}-\gamma u+\gamma)g^{2}+\beta\,\mathbb{E}\big[V(ug+\varepsilon)\big]\Big\}. |  |

We adopt the quadratic ansatz V​(g)=v2​g2+v1​g+v0V(g)=v\_{2}g^{2}+v\_{1}g+v\_{0} with v2>0v\_{2}>0. Write m≔𝔼​[ε]=μ​Δ​tm\coloneqq\mathbb{E}[\varepsilon]=\mu\Delta t and s2≔𝔼​[ε2]=σ2​Δ​t+μ2​Δ​t2s\_{2}\coloneqq\mathbb{E}[\varepsilon^{2}]=\sigma^{2}\Delta t+\mu^{2}\Delta t^{2}. Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(u​g+ε)2]=u2​g2+2​u​g​m+s2,𝔼​[u​g+ε]=u​g+m,\mathbb{E}[(ug+\varepsilon)^{2}]=u^{2}g^{2}+2ug\,m+s\_{2},\qquad\mathbb{E}[ug+\varepsilon]=ug+m, |  |

and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[V​(u​g+ε)]\displaystyle\mathbb{E}[V(ug+\varepsilon)] | =v2​𝔼​[(u​g+ε)2]+v1​𝔼​[u​g+ε]+v0\displaystyle=v\_{2}\,\mathbb{E}[(ug+\varepsilon)^{2}]+v\_{1}\,\mathbb{E}[ug+\varepsilon]+v\_{0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =v2​(u2​g2+2​u​g​m+s2)+v1​(u​g+m)+v0.\displaystyle=v\_{2}(u^{2}g^{2}+2ugm+s\_{2})+v\_{1}(ug+m)+v\_{0}. |  |

Substituting into the Bellman objective yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(u;g)\displaystyle Q(u;g) | =(u2−γ​u+γ)​g2+β​(v2​(u2​g2+2​u​g​m+s2)+v1​(u​g+m)+v0)\displaystyle=(u^{2}-\gamma u+\gamma)g^{2}+\beta\Big(v\_{2}(u^{2}g^{2}+2ugm+s\_{2})+v\_{1}(ug+m)+v\_{0}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1+β​v2)​g2​u2+(−γ​g2+β​(2​v2​m+v1)​g)​u+γ​g2+β​(v2​s2+v1​m+v0).\displaystyle=(1+\beta v\_{2})g^{2}u^{2}\;+\;\Big(-\gamma g^{2}+\beta(2v\_{2}m+v\_{1})g\Big)u\;+\;\gamma g^{2}\;+\;\beta(v\_{2}s\_{2}+v\_{1}m+v\_{0}). |  |

For each fixed g≠0g\neq 0, this is a strictly convex quadratic function of uu since 1+β​v2>01+\beta v\_{2}>0. Thus the unconstrained minimizer satisfies ∂uQ​(u;g)=0\partial\_{u}Q(u;g)=0, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 2​(1+β​v2)​g2​u+(−γ​g2+β​(2​v2​m+v1)​g)=0,2(1+\beta v\_{2})g^{2}u+\Big(-\gamma g^{2}+\beta(2v\_{2}m+v\_{1})g\Big)=0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | uopt​(g)=γ2​(1+β​v2)−β​(2​v2​m+v1)2​(1+β​v2)⋅1g.u^{\mathrm{opt}}(g)=\frac{\gamma}{2(1+\beta v\_{2})}-\frac{\beta(2v\_{2}m+v\_{1})}{2(1+\beta v\_{2})}\cdot\frac{1}{g}. |  |

Using λ=1−u\lambda=1-u and enforcing the admissible interval λ∈[λ¯,1]\lambda\in[\underline{\lambda},1] yields the clipped feedback form ([13](https://arxiv.org/html/2602.09887v1#S4.E13 "Equation 13 ‣ Theorem 1. ‣ 4.2 Solution ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers")). When g=0g=0, the one-stage cost is zero for any λ\lambda, and we set λopt​(0)\lambda^{\mathrm{opt}}(0) by continuity.

To identify (v2,v1,v0)(v\_{2},v\_{1},v\_{0}), we use the identity minu⁡(A​u2+B​u)=−B2/(4​A)\min\_{u}(Au^{2}+Bu)=-B^{2}/(4A) when A>0A>0. Here A=(1+β​v2)​g2A=(1+\beta v\_{2})g^{2} and B=−γ​g2+β​(2​v2​m+v1)​gB=-\gamma g^{2}+\beta(2v\_{2}m+v\_{1})g, so

|  |  |  |
| --- | --- | --- |
|  | minu⁡Q​(u;g)=γ​g2+β​(v2​s2+v1​m+v0)−(−γ​g2+β​(2​v2​m+v1)​g)24​(1+β​v2)​g2.\min\_{u}Q(u;g)=\gamma g^{2}+\beta(v\_{2}s\_{2}+v\_{1}m+v\_{0})-\frac{\big(-\gamma g^{2}+\beta(2v\_{2}m+v\_{1})g\big)^{2}}{4(1+\beta v\_{2})g^{2}}. |  |

Expand the square in the last term:

|  |  |  |
| --- | --- | --- |
|  | (−γ​g2+β​(2​v2​m+v1)​g)2=γ2​g4−2​γ​β​(2​v2​m+v1)​g3+β2​(2​v2​m+v1)2​g2.\big(-\gamma g^{2}+\beta(2v\_{2}m+v\_{1})g\big)^{2}=\gamma^{2}g^{4}-2\gamma\beta(2v\_{2}m+v\_{1})g^{3}+\beta^{2}(2v\_{2}m+v\_{1})^{2}g^{2}. |  |

Dividing by g2g^{2} gives

|  |  |  |
| --- | --- | --- |
|  | (−γ​g2+β​(2​v2​m+v1)​g)2g2=γ2​g2−2​γ​β​(2​v2​m+v1)​g+β2​(2​v2​m+v1)2.\frac{\big(-\gamma g^{2}+\beta(2v\_{2}m+v\_{1})g\big)^{2}}{g^{2}}=\gamma^{2}g^{2}-2\gamma\beta(2v\_{2}m+v\_{1})g+\beta^{2}(2v\_{2}m+v\_{1})^{2}. |  |

Therefore the Bellman equation V​(g)=v2​g2+v1​g+v0=minu⁡Q​(u;g)V(g)=v\_{2}g^{2}+v\_{1}g+v\_{0}=\min\_{u}Q(u;g) implies coefficient matching:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v2\displaystyle v\_{2} | =γ−γ24​(1+β​v2),\displaystyle=\gamma-\frac{\gamma^{2}}{4(1+\beta v\_{2})}, |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v1\displaystyle v\_{1} | =γ​β​(2​v2​m+v1)2​(1+β​v2),\displaystyle=\frac{\gamma\beta(2v\_{2}m+v\_{1})}{2(1+\beta v\_{2})}, |  | (24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v0\displaystyle v\_{0} | =β​(v2​s2+v1​m+v0)−β2​(2​v2​m+v1)24​(1+β​v2).\displaystyle=\beta(v\_{2}s\_{2}+v\_{1}m+v\_{0})-\frac{\beta^{2}(2v\_{2}m+v\_{1})^{2}}{4(1+\beta v\_{2})}. |  | (25) |

Equation ([23](https://arxiv.org/html/2602.09887v1#A1.E23 "Equation 23 ‣ Proof. ‣ A.3 Proof of Theorem˜1 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")) is a scalar Riccati equation. Rearranging,

|  |  |  |
| --- | --- | --- |
|  | v2​(1+β​v2)=γ​(1+β​v2)−γ24⟺β​v22+(1−β​γ)​v2+(γ24−γ)=0,v\_{2}(1+\beta v\_{2})=\gamma(1+\beta v\_{2})-\frac{\gamma^{2}}{4}\quad\Longleftrightarrow\quad\beta v\_{2}^{2}+(1-\beta\gamma)v\_{2}+\Big(\frac{\gamma^{2}}{4}-\gamma\Big)=0, |  |

and taking the positive root yields

|  |  |  |
| --- | --- | --- |
|  | v2=−(1−β​γ)+(1−β​γ)2−β​(γ2−4​γ)2​β.v\_{2}=\frac{-(1-\beta\gamma)+\sqrt{(1-\beta\gamma)^{2}-\beta(\gamma^{2}-4\gamma)}}{2\beta}. |  |

Next, solving ([24](https://arxiv.org/html/2602.09887v1#A1.E24 "Equation 24 ‣ Proof. ‣ A.3 Proof of Theorem˜1 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")) gives

|  |  |  |
| --- | --- | --- |
|  | v1​(2​(1+β​v2)−γ​β)=2​γ​β​v2​m⟹v1=2​γ​β​v2​μ​Δ​t2+2​β​v2−γ​β.v\_{1}\Big(2(1+\beta v\_{2})-\gamma\beta\Big)=2\gamma\beta v\_{2}m\quad\Longrightarrow\quad v\_{1}=\frac{2\gamma\beta v\_{2}\,\mu\Delta t}{2+2\beta v\_{2}-\gamma\beta}. |  |

Finally, ([25](https://arxiv.org/html/2602.09887v1#A1.E25 "Equation 25 ‣ Proof. ‣ A.3 Proof of Theorem˜1 ‣ Appendix A Proofs ‣ Partially Active Automated Market Makers")) yields the explicit expression for v0v\_{0}.

For the small-Δ​t\Delta t limit, note that β=e−ϱ​Δ​t=1+O​(Δ​t)\beta=e^{-\varrho\Delta t}=1+O(\Delta t) and m=μ​Δ​tm=\mu\Delta t, so v1=O​(Δ​t)v\_{1}=O(\Delta t). Under the stationary scaling g=Op​(Δ​t)g=O\_{p}(\sqrt{\Delta t}), the state-dependent term in ([13](https://arxiv.org/html/2602.09887v1#S4.E13 "Equation 13 ‣ Theorem 1. ‣ 4.2 Solution ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers")) satisfies

|  |  |  |
| --- | --- | --- |
|  | β​(2​v2​μ​Δ​t+v1)g=Op​(Δ​t),\frac{\beta(2v\_{2}\mu\Delta t+v\_{1})}{g}=O\_{p}(\sqrt{\Delta t}), |  |

hence λopt​(g)\lambda^{\mathrm{opt}}(g) becomes asymptotically constant. Setting β=1\beta=1 and m=0m=0 in the leading-order term yields

|  |  |  |
| --- | --- | --- |
|  | v2→γ−1+1+2​γ2,λ∗=1−γ2​(1+v2)=1+1+2​γ1+γ+1+2​γ,v\_{2}\to\frac{\gamma-1+\sqrt{1+2\gamma}}{2},\qquad\lambda^{\ast}=1-\frac{\gamma}{2(1+v\_{2})}=\frac{1+\sqrt{1+2\gamma}}{1+\gamma+\sqrt{1+2\gamma}}, |  |

proving ([14](https://arxiv.org/html/2602.09887v1#S4.E14 "Equation 14 ‣ Theorem 1. ‣ 4.2 Solution ‣ 4 Finding Optimal 𝜆 ‣ Partially Active Automated Market Makers")).
∎