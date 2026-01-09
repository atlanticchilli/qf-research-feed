---
authors:
- Bastien Baude
- Damien Challet
- Ioane Muni Toke
doc_id: arxiv:2601.03799v1
family_id: arxiv:2601.03799
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal execution on Uniswap v2/v3 under transient price impact
url_abs: http://arxiv.org/abs/2601.03799v1
url_html: https://arxiv.org/html/2601.03799v1
venue: arXiv q-fin
version: 1
year: 2026
---


Bastien Baude111[bastien.baude@centralesupelec.fr](mailto:bastien.baude@centralesupelec.fr)  Damien Challet222[damien.challet@centralesupelec.fr](mailto:damien.challet@centralesupelec.fr)  Ioane Muni Toke333[ioane.muni-toke@centralesupelec.fr](mailto:ioane.muni-toke@centralesupelec.fr)
  
  
Université Paris-Saclay, CentraleSupélec, Laboratoire MICS
  
91192 Gif-sur-Yvette, France

###### Abstract

We study the optimal liquidation of a large position on Uniswap v2 and Uniswap v3 in discrete time. The instantaneous price impact is derived from the AMM pricing rule. Transient impact is modeled to capture either exponential or approximately power-law decay, together with a permanent component. In the Uniswap v2 setting, we obtain optimal strategies in closed-form under general price dynamics. For Uniswap v3, we consider a two-layer liquidity framework, which naturally extends to multiple layers. We address the problem using dynamic programming under geometric Brownian motion dynamics and approximate the solution numerically using a discretization scheme. We obtain optimal strategies akin to classical ones in the LOB literature, with features specific to Uniswap. In particular, we show how the liquidity profile influences them.

Keywords – Decentralized finance, decentralized exchange, automated market makers, Uniswap, market microstructure, optimal execution, optimal scheduling problem.

## 1 Introduction

Crypto-assets are primarily traded on two types of venues: Centralized Exchanges (CEXs) and Decentralized Exchanges (DEXs). Whereas CEXs rely on Limit Order Books (LOBs) to match buyers and sellers, DEXs execute transactions on blockchain networks using liquidity pools. Liquidity Providers (LPs) deposit crypto-assets into these pools, while Liquidity Takers (LTs) trade against them. Transaction terms are set by algorithmic pricing rules known as Automated Market Makers (AMMs). Fees are charged on trades and shared between LPs and DEXs.

Uniswap has played a central role in defining the architecture of DEXs. Uniswap v1, launched in 2018, allows users to trade crypto-assets against Ethereum (ETH) and introduced the Constant Product AMM (CPAMM). This mechanism was formalized and generalized in Uniswap v2 (Adams et al., [2020](https://arxiv.org/html/2601.03799v1#bib.bib16 "Uniswap v2 core")) which supports arbitrary crypto-asset pairs. Uniswap v3 (Adams et al., [2021](https://arxiv.org/html/2601.03799v1#bib.bib17 "Uniswap v3 core")), extends the CPAMM by introducing the concept of Concentrated Liquidity AMM (CLAMM). LPs are no longer required to allocate capital across the entire price range; instead, they can specify custom price intervals in which their liquidity is active. Alternative AMMs have emerged to address specific types of crypto-asset pairs, for example Curve (Egorov, [2019](https://arxiv.org/html/2601.03799v1#bib.bib19 "StableSwap - efficient mechanism for stablecoin liquidity")) and Balancer (Martinelli and Mushegian, [2019](https://arxiv.org/html/2601.03799v1#bib.bib20 "A non-custodial portfolio manager, liquidity provider, and price sensor")).

The Total Value Locked (TVL) refers to the value of the crypto-assets, generally expressed in dollars, held in liquidity pools. As of September 2025, TVL across all DEXs was $​25​b\mathdollar 25\text{b},444Data sourced from DefiLlama, available at <https://defillama.com/protocols/dexs>. with an average daily trading volume of $​12.5​b\mathdollar 12.5\text{b}. Uniswap had $​6​b\mathdollar 6\text{b} in TVL and processed an average daily volume of $​4.5​b\mathdollar 4.5\text{b}.

The challenge faced by LTs when executing large trades on LOBs has been extensively studied in the literature. The Almgren-Chriss framework (Almgren and Chriss, [1999](https://arxiv.org/html/2601.03799v1#bib.bib2 "Value under liquidation"), [2001](https://arxiv.org/html/2601.03799v1#bib.bib3 "Optimal execution of portfolio transactions")) pioneers optimal execution modelling by formulating the trade-off between execution costs and the risk of adverse price movements during execution. The model, written in discrete time, combines linear instantaneous and permanent price impacts with a Bachelier dynamic for the fundamental price. The continuous-time counterpart with nonlinear instantaneous impact is developed in Almgren ([2003](https://arxiv.org/html/2601.03799v1#bib.bib4 "Optimal execution with nonlinear impact functions and trading-enhanced risk")). Several extensions are proposed in Guéant ([2016](https://arxiv.org/html/2601.03799v1#bib.bib5 "The financial mathematics of market liquidity: From optimal execution to market making")) and Cartea et al. ([2015](https://arxiv.org/html/2601.03799v1#bib.bib6 "Algorithmic and high-frequency trading")). While the Almgren-Chriss model includes instantaneous and permanent price impacts, it assumes no gradual recovery of the price following a trade. This intermediate regime, known as transient market impact, is accounted for in Obizhaeva and Wang ([2013](https://arxiv.org/html/2601.03799v1#bib.bib7 "Optimal trading strategy and supply/demand dynamics")); their model has been extended in various directions; see Alfonsi et al. ([2010](https://arxiv.org/html/2601.03799v1#bib.bib9 "Optimal execution strategies in limit order books with general shape functions"), [2008](https://arxiv.org/html/2601.03799v1#bib.bib8 "Constrained portfolio liquidation in a limit order book model")) and Gatheral et al. ([2012](https://arxiv.org/html/2601.03799v1#bib.bib10 "Transient linear price impact and Fredholm integral equations")); Curato et al. ([2017](https://arxiv.org/html/2601.03799v1#bib.bib11 "Optimal execution with non-linear transient market impact")). Notably, Alfonsi et al. ([2010](https://arxiv.org/html/2601.03799v1#bib.bib9 "Optimal execution strategies in limit order books with general shape functions")) generalize the model to arbitrary LOB shape functions. While CPAMMs can be seen as LOBs with virtual shape functions (Tran et al., [2024](https://arxiv.org/html/2601.03799v1#bib.bib30 "Order book inspired automated market making")), the results of Alfonsi et al. ([2010](https://arxiv.org/html/2601.03799v1#bib.bib9 "Optimal execution strategies in limit order books with general shape functions")) do not apply as these shapes depend on the stochastic spot price and the assumption of infinite LOB depth does not hold.

Few works have addressed the optimal execution problem on AMMs. Cartea et al. ([2025](https://arxiv.org/html/2601.03799v1#bib.bib26 "Decentralised finance and automated market making: Execution and speculation")) develop a continuous-time model in the spirit of Almgren-Chriss, applied to CPAMMs. A first-order approximation is used for the instantaneous price impact, while the permanent impact is assumed to be linear. Different price dynamics are considered, involving both CEX and DEX. However, to the best of our knowledge, the literature has not yet addressed the optimal execution problem on AMMs under transient price impact.

In this paper, we study the optimal execution problem under transient price impact, first on CPAMMs and then CLAMMs. The spot price is modeled as the combination of three components: (i) a fundamental price process; (ii) the cumulative price impact induced by past trades; and (iii) a transient impact model. The instantaneous price impact is derived from the AMM pricing rule. Following Cartea et al. ([2025](https://arxiv.org/html/2601.03799v1#bib.bib26 "Decentralised finance and automated market making: Execution and speculation")), we consider a first-order expansion, under which the price impact depends on the square root of the spot price and is therefore stochastic. In the spirit of Obizhaeva and Wang ([2013](https://arxiv.org/html/2601.03799v1#bib.bib7 "Optimal trading strategy and supply/demand dynamics")), transient price impact is described by a combination of exponential kernels in order to capture either exponential or approximately power-law decay, together with a permanent component. The execution problem is formulated in discrete time and consists in maximizing the expected total cash-flow resulting from liquidation. For CPAMMs, we obtain closed-form solutions under general fundamental price dynamics. For CLAMMs, we consider a two-layer liquidity framework and formulate the problem in a dynamic programming framework under geometric Brownian motion. We then propose a numerical scheme to approximate the solution. Under zero-drift fundamental price dynamics and a first-order approximation, the solution on CPAMMs is independent of the liquidity, whereas on CLAMMs, it adapts to both liquidity levels and the position of the spot price relative to the price threshold where liquidity changes.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2601.03799v1#S2 "2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") introduces the optimal execution problem on CPAMMs under transient price impact and provides closed-form solutions under general fundamental price dynamics. Anticipating that no closed-form solution is available in the CLAMMs case, the problem is also reformulated and solved within a dynamic programming framework under geometric Brownian motion assumption. Several scenarios are then considered to illustrate the results. Section [3](https://arxiv.org/html/2601.03799v1#S3 "3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") turns to the CLAMMs case and presents a numerical scheme to approximate the solution. Results are illustrated within a two-layer liquidity framework, which naturally extends to multiple layers.

## 2 The optimal scheduling problem on Uniswap v2

### 2.1 Mathematical framework

We consider a liquidity pool governed by a Constant Product Automated Market Maker (CPAMM), following the Uniswap v2 design. The pool consists of two tokens (i.e., crypto-assets), denoted by token aa (e.g., ETH) and token bb (e.g., USDT), with reserves qaq^{a} and qbq^{b} respectively. The constant product formula defining the AMM is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qa​qb=L2,q^{a}q^{b}=L^{2}, |  | (1) |

where LL is the liquidity of the pool. The spot price of token aa in terms of token bb (e.g., the price of ETH in USDT) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p=qbqa.p=\frac{q^{b}}{q^{a}}. |  | (2) |

Liquidity takers execute trades against the pool. Suppose a trader wants to sell δa>0\delta^{a}>0 units of token aa: the AMM determines the amount δb>0\delta^{b}>0 of token bb to be received by solving:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qa+δa)​(qb−δb)=L2,(q^{a}+\delta^{a})(q^{b}-\delta^{b})=L^{2}, |  | (3) |

assuming no fees. Fees are discussed in Section [2.4](https://arxiv.org/html/2601.03799v1#S2.SS4 "2.4 Incorporating fees ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). The trade is settled in such a way that the constant product formula ([1](https://arxiv.org/html/2601.03799v1#S2.E1 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) remains satisfied after the swap. Solving ([3](https://arxiv.org/html/2601.03799v1#S2.E3 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) for δb\delta^{b} yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δb=qb−L2qa+δa.\delta^{b}=q^{b}-\frac{L^{2}}{q^{a}+\delta^{a}}. |  | (4) |

From ([1](https://arxiv.org/html/2601.03799v1#S2.E1 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) and ([2](https://arxiv.org/html/2601.03799v1#S2.E2 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the reserves can be expressed in terms of liquidity and spot price:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qa=Lp,qb=L​p.q^{a}=\frac{L}{\sqrt{p}},\quad q^{b}=L\sqrt{p}. |  | (5) |

Substituting into ([4](https://arxiv.org/html/2601.03799v1#S2.E4 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the amount δb\delta^{b} received by the trader becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δb=δa​p1+δa​pL≈δa​p​(1−δa​pL),\delta^{b}=\frac{\delta^{a}p}{1+\frac{\delta^{a}\sqrt{p}}{L}}\approx\delta^{a}p\Big(1-\frac{\delta^{a}\sqrt{p}}{L}\Big), |  | (6) |

where the approximation corresponds to a first-order Taylor expansion in the dimensionless term δa​pL=δaqa\frac{\delta^{a}\sqrt{p}}{L}=\frac{\delta^{a}}{q^{a}}. This assumes that the trade size is small relative to the reserve of token aa.

We now define the execution price of the trade, denoted by p¯\overline{p}, as the average exchange rate obtained over the entire trade:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p¯=δbδa=p1+δa​pL≈p​(1−δa​pL),\overline{p}=\frac{\delta^{b}}{\delta^{a}}=\frac{p}{1+\frac{\delta^{a}\sqrt{p}}{L}}\approx p\Big(1-\frac{\delta^{a}\sqrt{p}}{L}\Big), |  | (7) |

where the approximation corresponds to a first-order expansion in δa​pL\frac{\delta^{a}\sqrt{p}}{L}. This represents the effective price paid by the trader per unit of token aa over the full trade. In contrast to the spot price pp, which reflects the marginal price before the trade, the execution price accounts for the cumulative effect of moving along the AMM curve. As emphasized in Cartea et al. ([2025](https://arxiv.org/html/2601.03799v1#bib.bib26 "Decentralised finance and automated market making: Execution and speculation")), Equation ([7](https://arxiv.org/html/2601.03799v1#S2.E7 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is explicitly derived from the AMM pricing rule, in contrast to LOBs, where execution costs are model-dependent. Next, the slippage is defined as the relative deviation of the execution price from the spot price. From the first-order expansion in ([7](https://arxiv.org/html/2601.03799v1#S2.E7 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), it is approximated by −δa​pL-\frac{\delta^{a}\sqrt{p}}{L}. The slope of the slippage with respect to trade size depends on the spot price and therefore becomes stochastic under stochastic spot price dynamics.

The post-swap spot price is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p+=qb−δbqa+δa=p(1+δa​pL)2≈p​(1−2​δa​pL),p^{+}=\frac{q^{b}-\delta^{b}}{q^{a}+\delta^{a}}=\frac{p}{\big(1+\frac{\delta^{a}\sqrt{p}}{L}\big)^{2}}\approx p\Big(1-\frac{2\delta^{a}\sqrt{p}}{L}\Big), |  | (8) |

where the approximation also corresponds to a first-order expansion in δa​pL\frac{\delta^{a}\sqrt{p}}{L}. This expression reflects the marginal price immediately after the trade and thus incorporates the impact induced by the trade size. The relative price impact is defined as the relative difference between the post-swap spot price and the pre-swap spot price. From the first-order expansion in ([8](https://arxiv.org/html/2601.03799v1#S2.E8 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), it is approximated by −2​δa​pL-\frac{2\delta^{a}\sqrt{p}}{L}, twice the slippage.

### 2.2 Optimal execution strategy

#### 2.2.1 Problem formulation

We consider the problem of a trader willing to execute a large sell order of size ξ>0\xi>0 of token aa over a fixed time horizon TT. The time interval [0,T][0,T] is divided into a regular partition: 0=t0<t1<⋯<tN=T0=t\_{0}<t\_{1}<\cdots<t\_{N}=T, with constant time step Δ=TN\Delta=\frac{T}{N}. At each time tnt\_{n}, the trader sells an amount δn\delta\_{n} (for the sake of readability, the superscript aa is omitted), subject to the volume constraint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=0Nδn=ξ.\sum^{N}\_{n=0}\delta\_{n}=\xi. |  | (9) |

Although the problem is formulated for a large sell order, the large buy order case is analogous.

We assume that the spot price is a combination of three components: (i) a fundamental price process, treated as an exogenous stochastic process capturing market volatility and external factors; (ii) the cumulative price impact induced by previous trades; and (iii) the resilience of the liquidity pool, reflecting the gradual recovery of the spot price following each trade. First, we denote by (fm)m=0N(f\_{m})^{N}\_{m=0} the fundamental price process, with f0f\_{0} given as a deterministic initial price. The fundamental price may be interpreted as a reference price, such as the CEX price under the assumption of no friction between CEX and DEX markets. More generally, it corresponds to the spot price from the DEX that would have prevailed in the absence of price impact from the trader’s execution schedule, and thus our model also covers crypto-assets not listed on CEXs. Second, the impact on the spot price at time tmt\_{m} induced by the previous trades (δn)n=0m−1(\delta\_{n})^{m-1}\_{n=0} is derived from the price impact formula ([8](https://arxiv.org/html/2601.03799v1#S2.E8 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). Third, the resilience of the liquidity pool is given by a convex combination of exponential price recovery terms. Hence, we write the spot price at time tmt\_{m}, for m=0,…,Nm=0,\ldots,N, as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pm=fm​(1−∑n=0m−1∑j=0Jωj​e−ρj​(m−n)​Δ​2​δn​fnL),p\_{m}=f\_{m}\Big(1-\sum^{m-1}\_{n=0}\sum^{J}\_{j=0}\omega\_{j}e^{-\rho\_{j}(m-n)\Delta}\frac{2\delta\_{n}\sqrt{f\_{n}}}{L}\Big), |  | (10) |

where (ρj)j=0J(\rho\_{j})^{J}\_{j=0} are resilience parameters and (ωj)j=0J(\omega\_{j})^{J}\_{j=0} the associated weights, satisfying ρj≥0\rho\_{j}\geq 0, ωj≥0\omega\_{j}\geq 0 for j=0,…,Jj=0,\ldots,J and ∑j=0Jωj=1\sum^{J}\_{j=0}\omega\_{j}=1. A permanent impact component can be accounted for by taking a resilience parameter to zero. Equation ([10](https://arxiv.org/html/2601.03799v1#S2.E10 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is constructed by successively applying the relative price impact formula ([8](https://arxiv.org/html/2601.03799v1#S2.E8 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) induced by previous trades, combined with a first-order expansion in the dimensionless terms (δn​fnL)n=0m−1(\frac{\delta\_{n}\sqrt{f\_{n}}}{L})^{m-1}\_{n=0}. Then, we multiply the relative price impacts by the resilience factors (∑j=0Jωj​e−(m−n)​Δ​ρj)n=0m−1(\sum^{J}\_{j=0}\omega\_{j}e^{-(m-n)\Delta\rho\_{j}})^{m-1}\_{n=0}. Moreover, the liquidity of the pool is assumed to remain constant throughout the trading horizon, i.e., LPs are passive. This modeling choice is supported by the empirical findings of Cartea et al. ([2025](https://arxiv.org/html/2601.03799v1#bib.bib26 "Decentralised finance and automated market making: Execution and speculation")), who report limited LP activity relative to LTs and stable pool liquidity over the relevant execution horizons.

The cash-flow at time tmt\_{m} from selling δm\delta\_{m} units is derived by substituting the spot price from ([10](https://arxiv.org/html/2601.03799v1#S2.E10 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) into the cash-flow formula ([6](https://arxiv.org/html/2601.03799v1#S2.E6 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) and is also a first-order expansion in the dimensionless terms (δn​fnL)n=0m−1(\frac{\delta\_{n}\sqrt{f\_{n}}}{L})^{m-1}\_{n=0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞m=δm​fm​(1−∑n=0m−1∑j=0Jωj​e−ρj​(m−n)​Δ​2​δn​fnL−δm​fmL).\mathcal{C}\_{m}=\delta\_{m}f\_{m}\Big(1-\sum^{m-1}\_{n=0}\sum^{J}\_{j=0}\omega\_{j}e^{-\rho\_{j}(m-n)\Delta}\frac{2\delta\_{n}\sqrt{f\_{n}}}{L}-\frac{\delta\_{m}\sqrt{f\_{m}}}{L}\Big). |  | (11) |

The execution price that determines the cash-flow at time tmt\_{m} combines two effects both resulting from the trader’s actions: the cumulative impact of past trades on the spot price and the slippage induced by the current trade.

We now formulate the execution problem of the trader. The objective is to determine the optimal sequence of trade sizes δ=(δ0,…,δN)⊤\delta=\big(\delta\_{0},\ldots,\delta\_{N}\big)^{\top} that maximizes the expected total cash-flow, corresponding to the sum over time of the contributions defined in ([11](https://arxiv.org/html/2601.03799v1#S2.E11 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), subject to the volume constraint ([9](https://arxiv.org/html/2601.03799v1#S2.E9 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ∗=argmax𝛿\displaystyle\delta^{\*}=\underset{\delta}{\mathrm{argmax}} | 𝔼​[∑n=0N𝒞n]\displaystyle\mathbb{E}\Big[\sum^{N}\_{n=0}\mathcal{C}\_{n}\Big] |  | (12) |
|  | s.t. | ∑n=0Nδn=ξ.\displaystyle\sum^{N}\_{n=0}\delta\_{n}=\xi. |  |

The constraint ensures that the full order of size ξ\xi is executed over the time interval [0,T][0,T]. The trades are not a priori required to be non-negative, as depending on the dynamics of the fundamental price, it may be optimal to buy (or oversell relative to ξ\xi) and later unwind the excess.

#### 2.2.2 General solution

We now state the general closed-form solution to the execution problem ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), formulated using the first-order cash-flow expression ([11](https://arxiv.org/html/2601.03799v1#S2.E11 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

###### Proposition 1 (General solution).

The optimal execution schedule is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗=(ξ−L2​𝟙⊤​A−1​B)​A−1​𝟙𝟙⊤​A−1​𝟙+(L2​𝟙⊤​A−1​B)​A−1​B𝟙⊤​A−1​B,\delta^{\*}=\Big(\xi-\frac{L}{2}\mathbbm{1}^{\top}A^{-1}B\Big)\frac{A^{-1}\mathbbm{1}}{\mathbbm{1}^{\top}A^{-1}\mathbbm{1}}+\Big(\frac{L}{2}\mathbbm{1}^{\top}A^{-1}B\Big)\frac{A^{-1}B}{\mathbbm{1}^{\top}A^{-1}B}, |  | (13) |

where 𝟙=(1,…,1)⊤\mathbbm{1}=\big(1,\ldots,1\big)^{\top}, the components of the vector B∈ℝN+1B\in\mathbb{R}^{N+1} are defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bm=𝔼​[fm],B\_{m}=\mathbb{E}[f\_{m}], |  | (14) |

and the entries of the matrix A∈ℝ(N+1)×(N+1)A\in\mathbb{R}^{(N+1)\times(N+1)} are given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Am​n={∑j=0Jωj​e−ρj​(m−n)​Δ​𝔼​[fm​fn]if ​n≤m∑j=0Jωj​e−ρj​(n−m)​Δ​𝔼​[fn​fm]if ​n>m.A\_{mn}=\left\{\begin{array}[]{ll}\sum^{J}\_{j=0}\omega\_{j}e^{-\rho\_{j}(m-n)\Delta}\mathbb{E}[f\_{m}\sqrt{f\_{n}}]&\mbox{if }n\leq m\\ \sum^{J}\_{j=0}\omega\_{j}e^{-\rho\_{j}(n-m)\Delta}\mathbb{E}[f\_{n}\sqrt{f\_{m}}]&\mbox{if }n>m.\end{array}\right. |  | (15) |

Equation ([13](https://arxiv.org/html/2601.03799v1#S2.E13 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) shows that the optimal execution schedule δ∗\delta^{\*} can be expressed as a linear combination of two distinct profiles: one driven by resilience and expected price impacts (A−1​𝟙A^{-1}\mathbbm{1}), and another that also accounts for the expected price trajectory (A−1​BA^{-1}B). This linear combination reflects the trade-off between minimizing market impact and exploiting expected price dynamics. The respective weights depend on the total order size ξ\xi and the liquidity level LL.

###### Corollary 1 (Martingale case).

If the fundamental price process is a martingale, the optimal solution ([13](https://arxiv.org/html/2601.03799v1#S2.E13 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗=ξ​A−1​𝟙𝟙⊤​A−1​𝟙,\delta^{\*}=\xi\frac{A^{-1}\mathbbm{1}}{\mathbbm{1}^{\top}A^{-1}\mathbbm{1}}, |  | (16) |

where the matrix AA is defined in ([15](https://arxiv.org/html/2601.03799v1#S2.E15 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

In the martingale case, the solution is independent of the liquidity level LL: although liquidity affects the overall cost of execution, it does not influence the shape of the optimal schedule in the martingale case. The execution strategy is fully determined by the structure of resilience and expected price impacts. Recall that this result is valid only at first order, i.e., when trades are small compared to the pool size.

###### Corollary 2 (Geometric Brownian motion case).

We assume that the fundamental price follows a geometric Brownian motion evaluated at discrete times tmt\_{m}, for m=0,…,Nm=0,\ldots,N:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fm=f0​e(μ−σ22)​m​Δ+σ​Wm,f\_{m}=f\_{0}e^{(\mu-\frac{\sigma^{2}}{2})m\Delta+\sigma W\_{m}}, |  | (17) |

where f0f\_{0} is the initial fundamental price, μ\mu the drift, σ\sigma the volatility and WmW\_{m} denotes the Brownian motion at time tmt\_{m}. Under the condition μ<3​σ24+4​minj⁡ρj\mu<\frac{3\sigma^{2}}{4}+4\min\_{j}\rho\_{j}, the optimal strategy δ∗\delta^{\*} is unique. Moreover, in the single exponential kernel setting (J=0J=0), the inverse of matrix AA admits a closed-form expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A−1=1f0​f0​[1+a2γ1−aγ10⋯0−aγ11γ1+a2γ2−aγ2⋯00−aγ21γ2+a2γ3⋯0⋮⋮⋮⋱−aγN000−aγN1γN],A^{-1}=\frac{1}{f\_{0}\sqrt{f\_{0}}}\begin{bmatrix}1+\frac{a^{2}}{\gamma\_{1}}&-\frac{a}{\gamma\_{1}}&0&\cdots&0\\ -\frac{a}{\gamma\_{1}}&\frac{1}{\gamma\_{1}}+\frac{a^{2}}{\gamma\_{2}}&-\frac{a}{\gamma\_{2}}&\cdots&0\\ 0&-\frac{a}{\gamma\_{2}}&\frac{1}{\gamma\_{2}}+\frac{a^{2}}{\gamma\_{3}}&\cdots&0\\ \vdots&\vdots&\vdots&\ddots&-\frac{a}{\gamma\_{N}}\\ 0&0&0&-\frac{a}{\gamma\_{N}}&\frac{1}{\gamma\_{N}}\end{bmatrix}, |  | (18) |

where a=e−(ρ−μ)​Δa=e^{-(\rho-\mu)\Delta}, bn=e(3​μ2+3​σ28)​n​Δb\_{n}=e^{\big(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8}\big)n\Delta} and γn=bn−a2​bn−1\gamma\_{n}=b\_{n}-a^{2}b\_{n-1} for n=1,…,Nn=1,\ldots,N.

The proofs are provided in Appendix [A](https://arxiv.org/html/2601.03799v1#A0.SS1 "A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). While the inverse of AA can be expressed explicitly in the single exponential kernel case, it must be computed numerically in the general multi-kernel setting.

#### 2.2.3 Dynamic programming

Anticipating that no general solution will be available in the CLAMMs case, we reformulate the execution problem ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) within a dynamic programming framework. We distinguish between two settings: the closed-loop case, which includes price feedback, and the open-loop case, which does not (Kirk, [2004](https://arxiv.org/html/2601.03799v1#bib.bib29 "Optimal control theory: An introduction")). We start with the closed-loop formulation, in which the state variables at time tnt\_{n} are given by the triplet (xn,(Inj)j=0J,fn)(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{n}), where xnx\_{n} is the remaining inventory, InjI^{j}\_{n} the cumulative price impacts induced by the jj-th resilience factor and fnf\_{n} the fundamental price. The remaining inventory evolves according to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {x0=ξxn+1=xn−δn.\left\{\begin{array}[]{ll}x\_{0}=\xi\\ x\_{n+1}=x\_{n}-\delta\_{n}.\end{array}\right. |  | (19) |

The dynamics of the cumulative price impacts are derived from ([10](https://arxiv.org/html/2601.03799v1#S2.E10 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) and read:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {I0j=0In+1j=e−ρj​Δ​(Inj+2​δn​fnL),\left\{\begin{array}[]{ll}I^{j}\_{0}=0\\ I^{j}\_{n+1}=e^{-\rho\_{j}\Delta}\Big(I^{j}\_{n}+\frac{2\delta\_{n}\sqrt{f\_{n}}}{L}\Big),\end{array}\right. |  | (20) |

for j=0,…,Jj=0,\ldots,J.

Let vn​(xn,(Inj)j=0J,fn)v\_{n}(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{n}) denote the value function, representing the maximal expected proceeds from liquidating xnx\_{n} units over the periods tn,…,tNt\_{n},\ldots,t\_{N}, given the current cumulative price impacts and fundamental price. From ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the associated Bellman equation reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vn​(xn,(Inj)j=0J,fn)=supδnδn​fn​(1−∑j=0Jωj​Inj−δn​fnL)+𝔼​[vn+1​(xn+1,(In+1j)j=0J,fn+1)|fn].v\_{n}(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{n})=\sup\_{\delta\_{n}}\ \delta\_{n}f\_{n}\big(1-\sum^{J}\_{j=0}\omega\_{j}I^{j}\_{n}-\frac{\delta\_{n}\sqrt{f\_{n}}}{L}\big)+\mathbb{E}\Big[v\_{n+1}(x\_{n+1},(I^{j}\_{n+1})^{J}\_{j=0},f\_{n+1})|f\_{n}\Big]. |  | (21) |

To satisfy the volume constraint ([9](https://arxiv.org/html/2601.03799v1#S2.E9 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the terminal condition enforces complete liquidation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vN​(xN,(INj)j=0J,fN)=xN​fN​(1−∑j=0Jωj​INj−xN​fNL),v\_{N}(x\_{N},(I^{j}\_{N})^{J}\_{j=0},f\_{N})=x\_{N}f\_{N}\Big(1-\sum^{J}\_{j=0}\omega\_{j}I^{j}\_{N}-\frac{x\_{N}\sqrt{f\_{N}}}{L}\Big), |  | (22) |

which corresponds to selling the entire remaining inventory xNx\_{N} at tNt\_{N} in a single trade.

In contrast to Proposition [1](https://arxiv.org/html/2601.03799v1#Thmproposition1 "Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), where the dynamics of the fundamental price remain unspecified, solving the Bellman equation and deriving the value function requires specifying them. We assume that the fundamental price follows a geometric Brownian motion ([17](https://arxiv.org/html/2601.03799v1#S2.E17 "In Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). The explicit value function and optimal control in a closed-loop setting are provided in the following proposition.

###### Proposition 2 (Dynamic programming: closed-loop solution).

Under the geometric Brownian motion assumption ([17](https://arxiv.org/html/2601.03799v1#S2.E17 "In Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the value function reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vn​(xn,(Inj)j=0J,fn)=xn​fn​(An+∑j=0JBnj​Inj+Cn​xn​fn)+fn​(Dn+∑j=0JEnj​Inj+∑j1=0J∑j2=0JFnj1,j2​Inj1​Inj2),v\_{n}(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{n})=x\_{n}f\_{n}\Big(A\_{n}+\sum^{J}\_{j=0}B^{j}\_{n}I^{j}\_{n}+C\_{n}x\_{n}\sqrt{f\_{n}}\Big)+\sqrt{f\_{n}}\Big(D\_{n}+\sum^{J}\_{j=0}E^{j}\_{n}I^{j}\_{n}+\sum^{J}\_{j\_{1}=0}\sum^{J}\_{j\_{2}=0}F^{j\_{1},j\_{2}}\_{n}I^{j\_{1}}\_{n}I^{j\_{2}}\_{n}\Big), |  | (23) |

and the optimal control:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δn∗​(xn,(Inj)j=0J,fn)=12​ϕn+1​fn​[θn+11+∑j=0JInj​θn+12,j+xn​fn​θn+13],\delta^{\*}\_{n}(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{n})=\frac{1}{2\phi\_{n+1}\sqrt{f\_{n}}}\Big[\theta^{1}\_{n+1}+\sum^{J}\_{j=0}I^{j}\_{n}\theta^{2,j}\_{n+1}+x\_{n}\sqrt{f\_{n}}\theta^{3}\_{n+1}\Big], |  | (24) |

where the coefficients ϕn+1\phi\_{n+1}, θn+11\theta^{1}\_{n+1}, (θn+12,j1)j1=0J\big(\theta^{2,j\_{1}}\_{n+1}\big)^{J}\_{j\_{1}=0} and θn+13\theta^{3}\_{n+1} are defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn+1=1L+2L​∑j=0JBn+1j​e(μ−ρj)​Δ−Cn+1​e(3​μ2+3​σ28)​Δ−4L2​∑j1=0J∑j2=0JFn+1j1,j2​e(μ2−ρj1−ρj2−σ28)​Δ,\phi\_{n+1}=\frac{1}{L}+\frac{2}{L}\sum^{J}\_{j=0}B^{j}\_{n+1}e^{(\mu-\rho\_{j})\Delta}-C\_{n+1}e^{(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8})\Delta}-\frac{4}{L^{2}}\sum^{J}\_{j\_{1}=0}\sum^{J}\_{j\_{2}=0}F^{j\_{1},j\_{2}}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j\_{1}}-\rho\_{j\_{2}}-\frac{\sigma^{2}}{8})\Delta}, |  | (25) |

and,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θn+11\displaystyle\theta^{1}\_{n+1} | =1−An+1​eμ​Δ+2L​∑j=0JEn+1j​e(μ2−ρj−σ28)​Δ,\displaystyle=1-A\_{n+1}e^{\mu\Delta}+\frac{2}{L}\sum^{J}\_{j=0}E^{j}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j}-\frac{\sigma^{2}}{8})\Delta}, |  | (26) |
|  | θn+12,j1\displaystyle\theta^{2,j\_{1}}\_{n+1} | =−ωj1−Bn+1j1​e(μ−ρj1)​Δ+4L​∑j2=0JFn+1j1,j2​e(μ2−ρj1−ρj2−σ28)​Δ,\displaystyle=-\omega\_{j\_{1}}-B^{j\_{1}}\_{n+1}e^{(\mu-\rho\_{j\_{1}})\Delta}+\frac{4}{L}\sum^{J}\_{j\_{2}=0}F^{j\_{1},j\_{2}}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j\_{1}}-\rho\_{j\_{2}}-\frac{\sigma^{2}}{8})\Delta}, |  |
|  | θn+13\displaystyle\theta^{3}\_{n+1} | =2L​∑j=0JBn+1j​e(μ−ρj)​Δ−2​Cn+1​e(3​μ2+3​σ28)​Δ.\displaystyle=\frac{2}{L}\sum^{J}\_{j=0}B^{j}\_{n+1}e^{(\mu-\rho\_{j})\Delta}-2C\_{n+1}e^{(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8})\Delta}. |  |

The coefficients An,(Bnj)j=0J,Cn,Dn,(En)j=0JA\_{n},(B^{j}\_{n})^{J}\_{j=0},C\_{n},D\_{n},(E\_{n})^{J}\_{j=0} and (Fn)j1,j2=0J(F\_{n})^{J}\_{j\_{1},j\_{2}=0} are determined recursively as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {An=An+1​eμ​Δ+12​ϕn+1​θn+11​θn+13Bnj=Bn+1j​e(μ−ρj)​Δ+12​ϕn+1​θn+12,j​θn+13Cn=Cn+1​e(3​μ2+3​σ28)​Δ+14​ϕn+1​(θn+13)2Dn=Dn+1​e(μ2−σ28)​Δ+14​ϕn+1​(θn+11)2Enj=En+1j​e(μ2−ρj−σ28)​Δ+12​ϕn+1​θn+11​θn+12,jFnj1,j2=Fn+1j1,j2​e(μ2−ρj1−ρj2−σ28)​Δ+14​ϕn+1​θn+12,j1​θn+12,j2,\left\{\begin{array}[]{ll}A\_{n}=A\_{n+1}e^{\mu\Delta}+\frac{1}{2\phi\_{n+1}}\theta^{1}\_{n+1}\theta^{3}\_{n+1}\\ B^{j}\_{n}=B^{j}\_{n+1}e^{(\mu-\rho\_{j})\Delta}+\frac{1}{2\phi\_{n+1}}\theta^{2,j}\_{n+1}\theta^{3}\_{n+1}\\ C\_{n}=C\_{n+1}e^{(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8})\Delta}+\frac{1}{4\phi\_{n+1}}(\theta^{3}\_{n+1})^{2}\\ D\_{n}=D\_{n+1}e^{(\frac{\mu}{2}-\frac{\sigma^{2}}{8})\Delta}+\frac{1}{4\phi\_{n+1}}(\theta^{1}\_{n+1})^{2}\\ E^{j}\_{n}=E^{j}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j}-\frac{\sigma^{2}}{8})\Delta}+\frac{1}{2\phi\_{n+1}}\theta^{1}\_{n+1}\theta^{2,j}\_{n+1}\\ F^{j\_{1},j\_{2}}\_{n}=F^{j\_{1},j\_{2}}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j\_{1}}-\rho\_{j\_{2}}-\frac{\sigma^{2}}{8})\Delta}+\frac{1}{4\phi\_{n+1}}\theta^{2,j\_{1}}\_{n+1}\theta^{2,j\_{2}}\_{n+1},\\ \end{array}\right. |  | (27) |

with terminal conditions AN=1A\_{N}=1, BNj=−ωjB^{j}\_{N}=-\omega\_{j}, CN=−1LC\_{N}=-\frac{1}{L}, DN=ENj=FNj1,j2=0D\_{N}=E^{j}\_{N}=F^{j\_{1},j\_{2}}\_{N}=0.

Details on the derivation are provided in Appendix [A](https://arxiv.org/html/2601.03799v1#A0.SS1 "A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). Whereas the general solution from Proposition [1](https://arxiv.org/html/2601.03799v1#Thmproposition1 "Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") is static, the closed-loop solution is dynamic as it adjusts its execution path in response to price feedback.

We now turn to the open-loop formulation of the execution problem ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). The fundamental price is removed from the set of state variables and the problem is reformulated in expectation under the geometric Brownian motion assumption ([17](https://arxiv.org/html/2601.03799v1#S2.E17 "In Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). Consequently, the strategy does not incorporate feedback from the evolving fundamental price during execution. We introduce I~nj\tilde{I}^{j}\_{n} the cumulative mean price impact at time tnt\_{n} induced by the jj-th resilience factor, for j=0,…,Jj=0,\ldots,J. The dynamics are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {I~0j=0I~n+1j=e−Δ​ρj​(I~nj+2​δn​f0L​e(μ2+3​σ28)​n​Δ).\left\{\begin{array}[]{ll}\tilde{I}^{j}\_{0}=0\\ \tilde{I}^{j}\_{n+1}=e^{-\Delta\rho\_{j}}\Big(\tilde{I}^{j}\_{n}+\frac{2\delta\_{n}\sqrt{f\_{0}}}{L}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})n\Delta}\Big).\end{array}\right. |  | (28) |

Inventory also evolves according to ([19](https://arxiv.org/html/2601.03799v1#S2.E19 "In 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

Next, we denote the value function by v~\tilde{v}, and the Bellman equation reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v~n​(xn,(I~nj)j=0J)=supδnδn​f0​eμ​n​Δ​(1−∑j=0Jωj​I~nj−δn​f0L​e(μ2+3​σ28)​n​Δ)+v~n+1​(xn+1,(I~n+1j)j=0J).\tilde{v}\_{n}(x\_{n},(\tilde{I}^{j}\_{n})^{J}\_{j=0})=\sup\_{\delta\_{n}}\ \delta\_{n}f\_{0}e^{\mu n\Delta}\big(1-\sum^{J}\_{j=0}\omega\_{j}\tilde{I}^{j}\_{n}-\frac{\delta\_{n}\sqrt{f\_{0}}}{L}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})n\Delta}\big)+\tilde{v}\_{n+1}(x\_{n+1},(\tilde{I}^{j}\_{n+1})^{J}\_{j=0}). |  | (29) |

To satisfy the volume constraint ([9](https://arxiv.org/html/2601.03799v1#S2.E9 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the terminal condition also enforces complete liquidation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v~N​(xN,(I~Nj)j=0J)=xN​f0​eμ​N​Δ​(1−∑j=0Jωj​I~Nj−xN​f0L​e(μ2+3​σ28)​N​Δ).\tilde{v}\_{N}(x\_{N},(\tilde{I}^{j}\_{N})^{J}\_{j=0})=x\_{N}f\_{0}e^{\mu N\Delta}\big(1-\sum^{J}\_{j=0}\omega\_{j}\tilde{I}^{j}\_{N}-\frac{x\_{N}\sqrt{f\_{0}}}{L}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})N\Delta}\big). |  | (30) |

The explicit value function and optimal control in the open-loop setting are provided in the following proposition.

###### Proposition 3 (Dynamic programming: open-loop solution).

Under the geometric Brownian motion assumption ([17](https://arxiv.org/html/2601.03799v1#S2.E17 "In Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the value function reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v~n​(xn,(I~nj)j=0J)=xn​f0​(A~n+∑j=0JB~nj​I~nj+C~n​xn​f0)+f0​(D~n+∑j=0JE~nj​I~nj+∑j1=0J∑j2=0JF~nj1,j2​I~nj1​I~nj2),\tilde{v}\_{n}(x\_{n},(\tilde{I}^{j}\_{n})^{J}\_{j=0})=x\_{n}f\_{0}\Big(\tilde{A}\_{n}+\sum^{J}\_{j=0}\tilde{B}^{j}\_{n}\tilde{I}^{j}\_{n}+\tilde{C}\_{n}x\_{n}\sqrt{f\_{0}}\Big)+\sqrt{f\_{0}}\Big(\tilde{D}\_{n}+\sum^{J}\_{j=0}\tilde{E}^{j}\_{n}\tilde{I}^{j}\_{n}+\sum^{J}\_{j\_{1}=0}\sum^{J}\_{j\_{2}=0}\tilde{F}^{j\_{1},j\_{2}}\_{n}\tilde{I}^{j\_{1}}\_{n}\tilde{I}^{j\_{2}}\_{n}\Big), |  | (31) |

and the optimal control:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δn∗​(xn,(I~nj)j=0J)=12​ϕ~n+1​f0​[θ~n+11+∑j=0JI~nj​θ~n+12,j+xn​f0​θ~n+13],\delta^{\*}\_{n}(x\_{n},(\tilde{I}^{j}\_{n})^{J}\_{j=0})=\frac{1}{2\tilde{\phi}\_{n+1}\sqrt{f\_{0}}}\Big[\tilde{\theta}^{1}\_{n+1}+\sum^{J}\_{j=0}\tilde{I}^{j}\_{n}\tilde{\theta}^{2,j}\_{n+1}+x\_{n}\sqrt{f\_{0}}\tilde{\theta}^{3}\_{n+1}\Big], |  | (32) |

where the coefficients ϕ~n+1\tilde{\phi}\_{n+1}, θ~n+11\tilde{\theta}^{1}\_{n+1}, (θ~n+12,j1)j1=0J\big(\tilde{\theta}^{2,j\_{1}}\_{n+1}\big)^{J}\_{j\_{1}=0} and θ~n+13\tilde{\theta}^{3}\_{n+1} are defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ~n+1=1L​e(3​μ2+3​σ28)​n​Δ+2L​∑j=0JB~n+1j​e−ρj​Δ​e(μ2+3​σ28)​n​Δ−C~n+1−4L2​∑j1=0J∑j2=0JF~n+1j1,j2​e−(ρj1+ρj2)​Δ​e(μ+3​σ24)​n​Δ,\tilde{\phi}\_{n+1}=\frac{1}{L}e^{(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8})n\Delta}+\frac{2}{L}\sum^{J}\_{j=0}\tilde{B}^{j}\_{n+1}e^{-\rho\_{j}\Delta}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})n\Delta}-\tilde{C}\_{n+1}-\frac{4}{L^{2}}\sum^{J}\_{j\_{1}=0}\sum^{J}\_{j\_{2}=0}\tilde{F}^{j\_{1},j\_{2}}\_{n+1}e^{-(\rho\_{j\_{1}}+\rho\_{j\_{2}})\Delta}e^{(\mu+\frac{3\sigma^{2}}{4})n\Delta}, |  | (33) |

and,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θ~n+11\displaystyle\tilde{\theta}^{1}\_{n+1} | =eμ​n​Δ−A~n+1+2L​∑j=0JE~n+1j​e−ρj​Δ​e(μ2+3​σ28)​n​Δ,\displaystyle=e^{\mu n\Delta}-\tilde{A}\_{n+1}+\frac{2}{L}\sum^{J}\_{j=0}\tilde{E}^{j}\_{n+1}e^{-\rho\_{j}\Delta}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})n\Delta}, |  | (34) |
|  | θ~n+12,j1\displaystyle\tilde{\theta}^{2,j\_{1}}\_{n+1} | =−ωj1​eμ​n​Δ−B~n+1j1​e−ρj1​Δ+4L​∑j2=0JF~n+1j1,j2​e−(ρj1+ρj2)​Δ​e(μ2+3​σ28)​n​Δ,\displaystyle=-\omega\_{j\_{1}}e^{\mu n\Delta}-\tilde{B}^{j\_{1}}\_{n+1}e^{-\rho\_{j\_{1}}\Delta}+\frac{4}{L}\sum^{J}\_{j\_{2}=0}\tilde{F}^{j\_{1},j\_{2}}\_{n+1}e^{-(\rho\_{j\_{1}}+\rho\_{j\_{2}})\Delta}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})n\Delta}, |  |
|  | θ~n+13\displaystyle\tilde{\theta}^{3}\_{n+1} | =2L​∑j=0JB~n+1j​e−ρj​Δ​e(μ2+3​σ28)​n​Δ−2​C~n+1.\displaystyle=\frac{2}{L}\sum^{J}\_{j=0}\tilde{B}^{j}\_{n+1}e^{-\rho\_{j}\Delta}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})n\Delta}-2\tilde{C}\_{n+1}. |  |

The coefficients A~n,(B~nj)j=0J,C~n,D~n,(E~n)j=0J\tilde{A}\_{n},(\tilde{B}^{j}\_{n})^{J}\_{j=0},\tilde{C}\_{n},\tilde{D}\_{n},(\tilde{E}\_{n})^{J}\_{j=0} and (F~n)j1,j2=0J(\tilde{F}\_{n})^{J}\_{j\_{1},j\_{2}=0} are determined recursively as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {A~n=A~n+1+12​ϕ~n+1​θ~n+11​θ~n+13B~nj=B~n+1j​e−ρj​Δ+12​ϕ~n+1​θ~n+12,j​θ~n+13C~n=C~n+1+14​ϕ~n+1​(θ~n+13)2D~n=D~n+1+14​ϕ~n+1​(θ~n+11)2E~nj=E~n+1j​e−ρj​Δ+12​ϕ~n+1​θ~n+11​θ~n+12,jF~nj1,j2=F~n+1j1,j2​e−(ρj1+ρj2)​Δ+14​ϕ~n+1​θ~n+12,j1​θ~n+12,j2,\left\{\begin{array}[]{ll}\tilde{A}\_{n}=\tilde{A}\_{n+1}+\frac{1}{2\tilde{\phi}\_{n+1}}\tilde{\theta}^{1}\_{n+1}\tilde{\theta}^{3}\_{n+1}\\ \tilde{B}^{j}\_{n}=\tilde{B}^{j}\_{n+1}e^{-\rho\_{j}\Delta}+\frac{1}{2\tilde{\phi}\_{n+1}}\tilde{\theta}^{2,j}\_{n+1}\tilde{\theta}^{3}\_{n+1}\\ \tilde{C}\_{n}=\tilde{C}\_{n+1}+\frac{1}{4\tilde{\phi}\_{n+1}}(\tilde{\theta}^{3}\_{n+1})^{2}\\ \tilde{D}\_{n}=\tilde{D}\_{n+1}+\frac{1}{4\tilde{\phi}\_{n+1}}(\tilde{\theta}^{1}\_{n+1})^{2}\\ \tilde{E}^{j}\_{n}=\tilde{E}^{j}\_{n+1}e^{-\rho\_{j}\Delta}+\frac{1}{2\tilde{\phi}\_{n+1}}\tilde{\theta}^{1}\_{n+1}\tilde{\theta}^{2,j}\_{n+1}\\ \tilde{F}^{j\_{1},j\_{2}}\_{n}=\tilde{F}^{j\_{1},j\_{2}}\_{n+1}e^{-(\rho\_{j\_{1}}+\rho\_{j\_{2}})\Delta}+\frac{1}{4\tilde{\phi}\_{n+1}}\tilde{\theta}^{2,j\_{1}}\_{n+1}\tilde{\theta}^{2,j\_{2}}\_{n+1},\\ \end{array}\right. |  | (35) |

with terminal conditions A~N=eμ​N​Δ\tilde{A}\_{N}=e^{\mu N\Delta}, B~Nj=−ωj​eμ​N​Δ\tilde{B}^{j}\_{N}=-\omega\_{j}e^{\mu N\Delta}, C~N=−1L​e(μ2+3​σ28)​N​Δ\tilde{C}\_{N}=-\frac{1}{L}e^{(\frac{\mu}{2}+\frac{3\sigma^{2}}{8})N\Delta}, D~N=E~Nj=F~Nj1,j2=0\tilde{D}\_{N}=\tilde{E}^{j}\_{N}=\tilde{F}^{j\_{1},j\_{2}}\_{N}=0.

The open-loop solution is set at time t0t\_{0} and is not adjusted during execution as in the general solution of Proposition [1](https://arxiv.org/html/2601.03799v1#Thmproposition1 "Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). In particular, when the fundamental price follows a geometric Brownian motion, numerical experiments show that the open-loop solution coincides with the solution of Corollary [2](https://arxiv.org/html/2601.03799v1#Thmcorollary2 "Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), which is unsurprising. An analogous result is established by Alfonsi et al. ([2010](https://arxiv.org/html/2601.03799v1#bib.bib9 "Optimal execution strategies in limit order books with general shape functions")) in a distinct framework. Here, the recursive scheme is more complex and prevents a similar derivation.

### 2.3 Numerical results

#### 2.3.1 Illustrations

![Refer to caption](x1.png)


Figure 1: Optimal execution schedule under the three scenarios (relative to the initial trade for the sake of comparison); T=1T=1, N=10N=10, ξ=1\xi=1, L=1000L=1000, f0=1f\_{0}=1, μ=0\mu=0 and σ=0.3\sigma=0.3.

We illustrate the optimal trading strategy when the fundamental price follows a geometric Brownian motion using the closed-form expression of Corollary [2](https://arxiv.org/html/2601.03799v1#Thmcorollary2 "Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") with the following set of parameters: T=1T=1, N=10N=10, ξ=1\xi=1, f0=1f\_{0}=1, L=1000L=1000, μ=0\mu=0 and σ=0.3\sigma=0.3. In the single-kernel setting, the closed-form inverse of AA given in ([18](https://arxiv.org/html/2601.03799v1#S2.E18 "In Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is used, whereas in the general multi-kernel case, it is computed numerically. Three scenarios are investigated and Figure [1](https://arxiv.org/html/2601.03799v1#S2.F1 "Figure 1 ‣ 2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") displays the corresponding optimal execution schedules. We compare them to classical ones from the LOB literature. Even though our focus is on optimal execution on CPAMMs, comparisons with the LOB literature remain relevant as CPAMMs can be seen as LOBs with virtual shape functions (Tran et al., [2024](https://arxiv.org/html/2601.03799v1#bib.bib30 "Order book inspired automated market making")).

##### Scenario 1 (exponential resilience)

We first examine exponential resilience with no permanent impact, setting J=0J=0 and ρ=3\rho=3. With a single exponential kernel (i.e., J=0J=0), the index jj in ([10](https://arxiv.org/html/2601.03799v1#S2.E10 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is omitted. The resulting optimal strategy exhibits features reminiscent of a bucket-shaped profile, characterized by identical trades at the beginning and end of the trading horizon, and smaller constant sized trades in between. A symmetric bucket-shaped profile was originally observed in Obizhaeva and Wang ([2013](https://arxiv.org/html/2601.03799v1#bib.bib7 "Optimal trading strategy and supply/demand dynamics")) without risk aversion. However, the bucket-shaped profile obtained here is asymmetric, with the initial trade larger than the final one. Appendix [B](https://arxiv.org/html/2601.03799v1#A0.SS2 "B Optimal execution on Uniswap v2: the two-period martingale case ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact") establishes this property and studies the sensitivity of the strategy to model parameters, both within a two-period framework. Moreover, the intermediate trades are not equal and exhibit a slight downward slope, a feature also observed in Obizhaeva and Wang ([2013](https://arxiv.org/html/2601.03799v1#bib.bib7 "Optimal trading strategy and supply/demand dynamics")) when risk aversion is included in the objective function. We recover a similar pattern here despite the absence of risk aversion. We interpret this behavior as a consequence of stochastic price impact and slippage, which introduces uncertainty into execution. This asymmetry becomes more pronounced as the volatility parameter increases, reflecting a stronger incentive to front-load execution because of higher expected price impact and slippage of future trades (see Section [2.3.2](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS2 "2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

##### Scenario 2 (power-law resilience)

Next, a power-law-like resilience with no permanent impact is considered. The power-law kernel is approximated by a convex combinations of exponential kernels:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1+α​m​Δ)−β≈∑j=0Jωj​e−ρj​m​Δ,(1+\alpha m\Delta)^{-\beta}\approx\sum^{J}\_{j=0}\omega\_{j}e^{-\rho\_{j}m\Delta}, |  | (36) |

where α≥0\alpha\geq 0 is a scaling parameter and β≥0\beta\geq 0 denotes the power-law exponent. Given α\alpha and β\beta, the resilience parameters (ρj)j=0J(\rho\_{j})^{J}\_{j=0} and the associated weights (ωj)j=0J(\omega\_{j})^{J}\_{j=0} are obtained numerically by fitting the power-law kernel over the interval [0,T][0,T]. To do so, we use the SLSQP algorithm provided by the Scipy minimize function. We set α=10\alpha=10 and β=0.8\beta=0.8. In this setting, we take J=1J=1, which provides an accurate approximation of the power-law kernel. An advanced calibration methodology for larger values of JJ is presented in Bochud and Challet ([2007](https://arxiv.org/html/2601.03799v1#bib.bib15 "Optimal approximations of power laws with exponentials: Application to volatility models with long memory")). The optimal execution schedule exhibits an asymmetric U-shaped profile, with trade sizes gradually increasing toward both ends of the trading interval. A symmetric U-shape profile is presented in Bouchaud et al. ([2018](https://arxiv.org/html/2601.03799v1#bib.bib12 "Trades, quotes and prices: Financial markets under the microscope"), Section 21.2) and obtained under power-law decaying propagators without risk aversion whereas an asymmetric U-shape profile is obtained in Busseti and Lillo ([2012](https://arxiv.org/html/2601.03799v1#bib.bib13 "Calibration of optimal execution of financial transactions in the presence of transient market impact")) by incorporating risk aversion. As in Scenario 11, we obtain an asymmetric profile despite the absence of risk aversion. This asymmetry also arises from the stochastic nature of market impact and slippage in our CPAMM framework.

##### Scenario 3 (predominant permanent impact)

Finally, we consider a scenario under predominant permanent impact and limited exponential resilience, with parameters: J=1J=1, ω0=0.99\omega\_{0}=0.99, ρ0=0\rho\_{0}=0, ω1=0.01\omega\_{1}=0.01 and ρ1=5\rho\_{1}=5. The resulting optimal execution schedule is close to a front-loaded profile, in the spirit of the Almgren-Chriss schedule under a mean-variance objective (Almgren and Chriss, [2001](https://arxiv.org/html/2601.03799v1#bib.bib3 "Optimal execution of portfolio transactions")). Despite the front-loaded nature of the schedule, the final trade remains significant relative to the previous ones, resulting in a hybrid between a front-loaded and a bucket-shaped profile.

#### 2.3.2 Sensitivity analysis

![Refer to caption](x2.png)


(a) Influence of σ\sigma; ρ=3\rho=3

![Refer to caption](x3.png)


(b) Influence of ρ\rho; σ=0.3\sigma=0.3

Figure 2: Influence of the parameters on the optimal execution schedule under scenario 11 (exponential resilience); T=1T=1, N=10N=10, ξ=1\xi=1, L=1000L=1000, f0=1f\_{0}=1, μ=0\mu=0 and J=0J=0.

##### Influence of the volatility

In the single-kernel case (J=0J=0), corresponding to scenario 11 (exponential resilience), Figure [2(a)](https://arxiv.org/html/2601.03799v1#S2.F2.sf1 "In Figure 2 ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") illustrates the influence of the volatility parameter σ\sigma. As the volatility increases, the execution profile skews toward the beginning of the trading schedule. Indeed, the model allocates larger trade sizes at earlier stages, at the expense of the terminal ones. This behavior reflects the incentive of the trader to front-load execution because of higher expected price impact of future trades.

![Refer to caption](x4.png)


(a) Influence of β\beta under scenario 22 (power-law resilience)

![Refer to caption](x5.png)


(b) Influence of ω0\omega\_{0} under scenario 33 (predominant permanent impact); ρ0=0\rho\_{0}=0, ρ1=5\rho\_{1}=5

Figure 3: Influence of the parameters on the optimal execution schedule; T=1T=1, N=10N=10, ξ=1\xi=1, L=1000L=1000, f0=1f\_{0}=1, μ=0\mu=0, σ=0.3\sigma=0.3 and J=1J=1.

##### Influence of the resilience

Still under scenario 11 (exponential resilience) in the single-kernel setting (J=0J=0), Figure [2(b)](https://arxiv.org/html/2601.03799v1#S2.F2.sf2 "In Figure 2 ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") shows the influence of the resilience parameter ρ\rho on the execution profile. As the resilience increases, the execution profile exhibits an upward parallel shift centered on the intermediate trades. Both the initial and terminal trades decrease in size, while intermediate trades are amplified. This shift enables the strategy to benefit from a stronger mean-reverting effect in prices, thereby reducing overall impact. Then, Figure [3(a)](https://arxiv.org/html/2601.03799v1#S2.F3.sf1 "In Figure 3 ‣ Influence of the volatility ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") illustrates the influence of the power-law exponent β\beta in the two-kernels setting (J=1J=1), corresponding to scenario 22 (power-law resilience). The resilience parameters are calibrated via the procedure described in Section [2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1 "2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). As β\beta increases, the model also increases the size of the intermediary trades. Moreover, a higher β\beta concentrates the resilience dynamics around a single dominant factor, thereby flattening the U-shaped profile. Finally, Figure [3(b)](https://arxiv.org/html/2601.03799v1#S2.F3.sf2 "In Figure 3 ‣ Influence of the volatility ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") examines the effect of the permanent component of price impact under scenario 33 (predominant permanent impact). As the permanent impact becomes increasingly predominant, the execution strategy shifts toward a more front-loaded profile. When impact is fully permanent (i.e., ω0=1\omega\_{0}=1), the optimal strategy consists in liquidating the entire inventory at the first time step, as no mean-reverting effect remains to be exploited.

![Refer to caption](x6.png)


(a) Execution profiles

![Refer to caption](x7.png)


(b) Inventory paths

Figure 4: Influence of the trading frequency on the optimal execution schedule under scenario 11 (exponential resilience); T=1T=1, ξ=1\xi=1, L=1000L=1000, f0=1f\_{0}=1, μ=0\mu=0, σ=0.3\sigma=0.3, J=0J=0 and ρ=3\rho=3.

##### Influence of the trading frequency

Figures [4(a)](https://arxiv.org/html/2601.03799v1#S2.F4.sf1 "In Figure 4 ‣ Influence of the resilience ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), [4(b)](https://arxiv.org/html/2601.03799v1#S2.F4.sf2 "In Figure 4 ‣ Influence of the resilience ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") display the effect of the trading frequency NN on both the optimal execution profile and the resulting inventory path in the scenario 11 (exponential resilience). As NN increases, all intermediary trades decrease uniformly, and both the initial and final trades also decrease. Nevertheless, the overall structure of the strategy remains unchanged: the inventory paths intersect at all common time steps, indicating that the underlying execution dynamics are preserved.

![Refer to caption](x8.png)


(a) Influence of LL; μ=0.001\mu=0.001

![Refer to caption](x9.png)


(b) Influence of LL; μ=−0.001\mu=-0.001

Figure 5: Influence of the liquidity with non-zero drift on the optimal execution schedule under scenario 11 (exponential resilience); T=1T=1, N=10N=10, ξ=1\xi=1, f0=1f\_{0}=1, σ=0.3\sigma=0.3, J=0J=0 and ρ=3\rho=3.

##### Influence of the liquidity

While liquidity has no impact on the optimal strategy in the martingale setting, it plays a significant role when the drift is non-zero. This effect is illustrated in Figures [5(a)](https://arxiv.org/html/2601.03799v1#S2.F5.sf1 "In Figure 5 ‣ Influence of the trading frequency ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), [5(b)](https://arxiv.org/html/2601.03799v1#S2.F5.sf2 "In Figure 5 ‣ Influence of the trading frequency ‣ 2.3.2 Sensitivity analysis ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). When the drift is positive, the optimal strategy reduces the size of the early trades and favors liquidation closer to maturity in order to benefit from the expected price increase induced by the positive drift. As the liquidity of the pool increases, the strategy further decreases the size of the early trades, and once liquidity is sufficiently high, the strategy involves buying at the beginning of the period and unwinding the position at maturity. When the drift is negative the reasoning is reversed and the strategy tends to sell more at the beginning of the period and buy back at maturity in order to benefit from the expected price decrease.

#### 2.3.3 Open-loop versus closed-loop

|  | scenario 11 | scenario 22 | scenario 33 |
| --- | --- | --- | --- |
| ℰmean\mathcal{E}^{\text{mean}} (in basis points) | 33 | 22 | 22 |
| ℰmax\mathcal{E}^{\text{max}} (in basis points) | 1717 | 99 | 55 |

Table 1: Mean and maximum absolute differences between open-loop and closed-loop evaluated along the mean price trajectory optimal execution schedules; T=1T=1, N=10N=10, ξ=1\xi=1, L=1000L=1000, f0=1f\_{0}=1, μ=0\mu=0 and σ=0.3\sigma=0.3.

First, we compare the optimal strategy obtained in the open-loop setting, as formulated in Proposition [3](https://arxiv.org/html/2601.03799v1#Thmproposition3 "Proposition 3 (Dynamic programming: open-loop solution). ‣ 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), with the closed-loop counterpart from Proposition [2](https://arxiv.org/html/2601.03799v1#Thmproposition2 "Proposition 2 (Dynamic programming: closed-loop solution). ‣ 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") evaluated along the mean fundamental price trajectory. We compute the mean and maximum absolute differences (expressed in basis points) across the three scenarios introduced in Section [2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1 "2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), as summarized in Table [1](https://arxiv.org/html/2601.03799v1#S2.T1 "Table 1 ‣ 2.3.3 Open-loop versus closed-loop ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). The mean and maximum absolute differences, denoted respectively by ℰmean\mathcal{E}^{\text{mean}} and ℰmax\mathcal{E}^{\text{max}}, are computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰmean=1N+1​∑n=0N|δn∗​(xn,(Inj)j=0J,f0​eμ​n​Δ)−δ~n∗​(xn,(I~nj)j=0J)|,\mathcal{E}^{\text{mean}}=\frac{1}{N+1}\sum^{N}\_{n=0}\Big|\delta^{\*}\_{n}\big(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{0}e^{\mu n\Delta}\big)-\tilde{\delta}^{\*}\_{n}(x\_{n},(\tilde{I}^{j}\_{n})^{J}\_{j=0})\Big|, |  | (37) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰmax=maxn=0,…,N⁡|δn∗​(xn,(Inj)j=0J,f0​eμ​n​Δ)−δ~n∗​(xn,(I~nj)j=0J)|.\mathcal{E}^{\text{max}}=\max\_{n=0,\ldots,N}\Big|\delta^{\*}\_{n}\big(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{0}e^{\mu n\Delta}\big)-\tilde{\delta}^{\*}\_{n}(x\_{n},(\tilde{I}^{j}\_{n})^{J}\_{j=0})\Big|. |  | (38) |

Both the remaining inventory and the cumulative price impacts are computed forward in time according to their respective dynamics. Across all three scenarios, the open-loop and closed-loop evaluated along the mean fundamental price trajectory strategies yield similar results.

![Refer to caption](x10.png)


(a) Execution under mean, upward and downward price trajectories

![Refer to caption](x11.png)


(b) Execution under mean, upward and downward bumped price trajectories

Figure 6: Closed-loop optimal execution schedules evaluated along mean, upward and downward price trajectories; T=1T=1, N=10N=10, ξ=1\xi=1, L=1000L=1000, f0=1f\_{0}=1, μ=0\mu=0, σ=0.3\sigma=0.3, J=0J=0 and ρ=3\rho=3.

Second, under scenario 11 (exponential resilience) from Section [2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1 "2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), we compare the optimal strategy in the closed-loop setting evaluated along the mean fundamental price trajectory with those obtained under the following upward and downward price trajectories:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fm±=f0​e(μ−σ22)​m​Δ±3​σ​m​Δ.f^{\pm}\_{m}=f\_{0}e^{(\mu-\frac{\sigma^{2}}{2})m\Delta\pm 3\sigma m\sqrt{\Delta}}. |  | (39) |

Figure [6(a)](https://arxiv.org/html/2601.03799v1#S2.F6.sf1 "In Figure 6 ‣ 2.3.3 Open-loop versus closed-loop ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") presents the resulting execution schedules. At the initial time, the executed trades are identical across trajectories. As prices diverge from the mean trajectory, the strategy adjusts accordingly. In the case of a persistently upward trend, it accelerates liquidation to benefit from rising prices. More specifically, when the observed prices exceed the expected ones, the strategy executes larger trades than it would have under the mean trajectory, seizing the opportunity to sell at more favorable prices. Conversely, when the observed price falls below the mean trajectory, the strategy sells less.

Finally, we analyze the optimal strategy under fundamental price trajectories subject to a persistent upward or downward multiplicative price bump e(μ−σ22)​Δ±3​σ​Δe^{(\mu-\frac{\sigma^{2}}{2})\Delta\pm 3\sigma\sqrt{\Delta}}, applied just before tn=0.5t\_{n}=0.5. The corresponding schedules are displayed in Figure [6(b)](https://arxiv.org/html/2601.03799v1#S2.F6.sf2 "In Figure 6 ‣ 2.3.3 Open-loop versus closed-loop ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). In this case, the strategy reacts immediately at the time of the shock, then returns to the initial profile, shifted to account for changes in remaining inventory.

### 2.4 Incorporating fees

In this section, we discuss the integration of a swap fee ϕ\phi into the execution framework, the constant product formula ([3](https://arxiv.org/html/2601.03799v1#S2.E3 "In 2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) now reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qa+(1−ϕ)​δa)​(qb−δb)=L2.(q^{a}+(1-\phi)\delta^{a})(q^{b}-\delta^{b})=L^{2}. |  | (40) |

In Uniswap v2, the swap fee is applied to the input amount and is fixed at ϕ=0.3%\phi=0.3\%. After the swap, liquidity is updated to L+=(qa+δa)​(qb−δb)L^{+}=\sqrt{(q^{a}+\delta^{a})(q^{b}-\delta^{b})} to reflect the fee-adjusted reserves. Equation ([40](https://arxiv.org/html/2601.03799v1#S2.E40 "In 2.4 Incorporating fees ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is valid only for positive trades (i.e., sell orders), since applying it to negative trades (i.e., buy orders) would imply that fees are received by the trader rather than paid to the pool. In this restricted setting, the optimal scheduling problem ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) still admits a closed-form solution, with appropriate adjustments to account for fees. Empirically, for the scenarios considered in Section [2.3](https://arxiv.org/html/2601.03799v1#S2.SS3 "2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), we observe that a fee level of ϕ=0.3%\phi=0.3\% affects cash-flows but has negligible influence on the resulting optimal strategies. Extending the model to handle negative trades would require adjusting the fee structure depending on the sign of the trade, which considerably complicates the modeling framework without giving fundamental new insights. For these reasons, we omit fees in the paper.

## 3 From Uniswap v2 to v3

### 3.1 A two-layer liquidity framework

![Refer to caption](x12.png)


Figure 7: Illustration of the two-layer liquidity profile. For a given trade size, the dashed zone indicates the price interval where the trade may cause the spot price to cross from the high-liquidity layer to the low-liquidity one; L0=1000L\_{0}=1000, L1=500L\_{1}=500, f0=1f\_{0}=1 and p¯=0.95\overline{p}=0.95.

In Uniswap v3, each LP chooses over which price interval they wish to provide liquidity. As a result, liquidity depends on the spot price in contrast to the constant liquidity of Uniswap v2. Here, we consider a two-layer liquidity framework, which naturally extends to multiple layers: L0L\_{0} when the spot price is above the price threshold p¯\overline{p}, and L1<L0L\_{1}<L\_{0} when the spot price is below p¯\overline{p}. Figure [7](https://arxiv.org/html/2601.03799v1#S3.F7 "Figure 7 ‣ 3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") illustrates the liquidity profile as a function of the spot price. We consider the same execution problem ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), reformulated within a dynamic programming framework under a closed-loop setting as in Section [2.2.3](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS3 "2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). In the two-layer liquidity framework, both cash-flows and price impacts depend on whether the spot price is above or below the threshold p¯\overline{p}. A third case arises when the spot price lies above p¯\overline{p}, but the execution causes it to cross the threshold. In this case, both the total cash flows and the aggregate price impact are decomposed into two parts: one corresponding to the execution above the threshold, and the other to the execution below it. The corresponding dynamics of the cumulative price impacts read:

|  |  |  |  |
| --- | --- | --- | --- |
|  | In+1j={e−ρj​Δ​(Inj+2​δn​fnL1)if ​pn≤p¯e−ρj​Δ​(Inj+2​δ¯n​fnL0+2​(δn−δ¯n)​p¯L1)if ​pn>p¯​ and ​δn>δ¯ne−ρj​Δ​(Inj+2​δn​fnL0)if ​pn>p¯​ and ​δn≤δ¯n,I^{j}\_{n+1}=\left\{\begin{array}[]{ll}e^{-\rho\_{j}\Delta}\big(I^{j}\_{n}+\frac{2\delta\_{n}\sqrt{f\_{n}}}{L\_{1}}\big)&\mbox{if }p\_{n}\leq\overline{p}\\ e^{-\rho\_{j}\Delta}\big(I^{j}\_{n}+\frac{2\overline{\delta}\_{n}\sqrt{f\_{n}}}{L\_{0}}+\frac{2(\delta\_{n}-\overline{\delta}\_{n})\sqrt{\overline{p}}}{L\_{1}}\big)&\mbox{if }p\_{n}>\overline{p}\mbox{ and }\delta\_{n}>\overline{\delta}\_{n}\\ e^{-\rho\_{j}\Delta}\big(I^{j}\_{n}+\frac{2\delta\_{n}\sqrt{f\_{n}}}{L\_{0}}\big)&\mbox{if }p\_{n}>\overline{p}\mbox{ and }\delta\_{n}\leq\overline{\delta}\_{n},\end{array}\right. |  | (41) |

for j=0,…,Jj=0,\ldots,J where I0j=0I^{j}\_{0}=0 and the quantity δ¯n\overline{\delta}\_{n} corresponds to the trade size that brings the post-swap price down to the threshold p¯\overline{p}, starting from an initial spot price above the threshold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ¯n=L02​fn​fn​(pn−p¯).\overline{\delta}\_{n}=\frac{L\_{0}}{2f\_{n}\sqrt{f\_{n}}}\big(p\_{n}-\overline{p}\big). |  | (42) |

The dynamics of the inventory remain unchanged from Section [2.2.3](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS3 "2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").

In this framework, the Bellman equation reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vn​(xn,(Inj)j=0J,fn)=supδn𝒞n+𝔼​[vn+1​(xn+1,(In+1j)j=0J,fn+1)|fn],v\_{n}(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{n})=\sup\_{\delta\_{n}}\ \mathcal{C}\_{n}+\mathbb{E}\Big[v\_{n+1}(x\_{n+1},(I^{j}\_{n+1})^{J}\_{j=0},f\_{n+1})|f\_{n}\Big], |  | (43) |

where the cash-flow at time tnt\_{n} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞n={δn​fn​(1−∑j=0Jωj​Inj−δn​fnL1)if ​pn≤p¯δ¯n​fn​(1−∑j=0Jωj​Inj−δ¯n​fnL0)+(δn−δ¯n)​p¯​(1−∑j=0Jωj​Inj−(δn−δ¯n)​p¯L1)if ​pn>p¯​ and ​δn>δ¯nδn​fn​(1−∑j=0Jωj​Inj−δn​fnL0)if ​pn>p¯​ and ​δn≤δ¯n.\mathcal{C}\_{n}=\left\{\begin{array}[]{ll}\delta\_{n}f\_{n}\big(1-\sum^{J}\_{j=0}\omega\_{j}I^{j}\_{n}-\frac{\delta\_{n}\sqrt{f\_{n}}}{L\_{1}}\big)&\mbox{if }p\_{n}\leq\overline{p}\\ \begin{array}[]{@{}l}\overline{\delta}\_{n}f\_{n}\big(1-\sum^{J}\_{j=0}\omega\_{j}I^{j}\_{n}-\frac{\overline{\delta}\_{n}\sqrt{f\_{n}}}{L\_{0}}\big)\\ \quad\ +\ (\delta\_{n}-\overline{\delta}\_{n})\overline{p}\big(1-\sum^{J}\_{j=0}\omega\_{j}I^{j}\_{n}-\frac{(\delta\_{n}-\overline{\delta}\_{n})\sqrt{\overline{p}}}{L\_{1}}\big)\end{array}&\mbox{if }p\_{n}>\overline{p}\mbox{ and }\delta\_{n}>\overline{\delta}\_{n}\\ \delta\_{n}f\_{n}\big(1-\sum^{J}\_{j=0}\omega\_{j}I^{j}\_{n}-\frac{\delta\_{n}\sqrt{f\_{n}}}{L\_{0}}\big)&\mbox{if }p\_{n}>\overline{p}\mbox{ and }\delta\_{n}\leq\overline{\delta}\_{n}.\end{array}\right. |  | (44) |

To satisfy the volume constraint ([9](https://arxiv.org/html/2601.03799v1#S2.E9 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the terminal condition of the value function enforces complete liquidation using δN=xN\delta\_{N}=x\_{N} in ([44](https://arxiv.org/html/2601.03799v1#S3.E44 "In 3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

Because of the discontinuities in the model, closed-form expressions are no longer available. Therefore, in the following section, we present a numerical method to approximate the optimal strategy.

### 3.2 Discretization scheme

We present a numerical method to approximate the value function and the corresponding optimal control under the two-layer liquidity framework introduced in Section [3.1](https://arxiv.org/html/2601.03799v1#S3.SS1 "3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). We also assume that the fundamental price follows a geometric Brownian motion, as described in Section [2.2.3](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS3 "2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). We adopt a discretization scheme, starting with the price domain. The price grid is defined for kf∈{0,…,Kf}k\_{f}\in\{0,\ldots,K\_{f}\} as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f(kf)=eY(kf),Y(kf)=mT+z​σT​(2​kf−KfKf),f^{(k\_{f})}=e^{Y^{(k\_{f})}},\quad Y^{(k\_{f})}=m\_{T}+z\sigma\_{T}\Big(\frac{2k\_{f}-K\_{f}}{K\_{f}}\Big), |  | (45) |

where z>0z>0 controls the grid width, while mT=log⁡(f0)+(μ−σ22)​Tm\_{T}=\log(f\_{0})+(\mu-\frac{\sigma^{2}}{2})T and σT=σ​T\sigma\_{T}=\sigma\sqrt{T} correspond to the mean and standard deviation of the log-price at maturity. An alternative would be to use adaptive grids based on the mean and standard deviation of the log-price over time. We tested both fixed and adaptive grids: fixed grids yield more stable numerical results.

Next, we discretize the inventory and cumulative price impact spaces. For kx∈{0,…,Kx}k\_{x}\in\{0,\ldots,K\_{x}\}, the inventory grid is defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x(kx)=kx​ξKx,x^{(k\_{x})}=\frac{k\_{x}\xi}{K\_{x}}, |  | (46) |

and for kij∈{0,…,KI}k^{j}\_{i}\in\{0,\ldots,K\_{I}\}, the grid associated with the cumulative impact induced by the jj-th resilience factor is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I(kij)=e−ρj​Δ​2​kij​ξ​f(Kf)L1​KI.I^{(k^{j}\_{i})}=e^{-\rho\_{j}\Delta}\frac{2k^{j}\_{i}\xi\sqrt{f^{(K\_{f})}}}{L\_{1}K\_{I}}. |  | (47) |

To approximate the conditional expectation in the Bellman equation, we introduce log-price midpoints between each Y(kf)Y^{(k\_{f})}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y(kf±)=12​(Y(kf)+Y(kf±1)),y^{(k^{\pm}\_{f})}=\frac{1}{2}\big(Y^{(k\_{f})}+Y^{(k\_{f}\pm 1)}\big), |  | (48) |

with boundary values y(0−)=−∞y^{(0^{-})}=-\infty and y(Kf+)=+∞y^{(K^{+}\_{f})}=+\infty to encompass the entire price domain. Given a current price f(k)f^{(k)}, the conditional expectation of the value function at the next time step is approximated by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[vn+1​(xn+1,(In+1j)j=0J,fn+1)|fn=f(k)]≈∑q=0Kfωk→q​vn+1​(xn+1,(In+1j)j=0J,f(q)),\mathbb{E}\big[v\_{n+1}(x\_{n+1},(I^{j}\_{n+1})^{J}\_{j=0},f\_{n+1})|f\_{n}=f^{(k)}\big]\approx\sum^{K\_{f}}\_{q=0}\omega\_{k\rightarrow q}v\_{n+1}(x\_{n+1},(I^{j}\_{n+1})^{J}\_{j=0},f^{(q)}), |  | (49) |

where the transition probability weights ωk→q\omega\_{k\rightarrow q} are computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωk→q=Φ​(y(q+)−μks)−Φ​(y(q−)−μks),\omega\_{k\rightarrow q}=\Phi(\frac{y^{(q+)}-\mu\_{k}}{s})-\Phi(\frac{y^{(q-)}-\mu\_{k}}{s}), |  | (50) |

with μk=log⁡(f(k))+(μ−σ22)​Δ\mu\_{k}=\log(f^{(k)})+(\mu-\frac{\sigma^{2}}{2})\Delta, s=σ​Δs=\sigma\sqrt{\Delta} and Φ\Phi denotes the standard normal cumulative distribution function.

The algorithm proceeds backward in time. The terminal condition of the value function is given by ([44](https://arxiv.org/html/2601.03799v1#S3.E44 "In 3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) using δN=xN\delta\_{N}=x\_{N}. Then, starting from this terminal condition and applying the Bellman recursion, we estimate the value function and the corresponding optimal control at each grid point of the fundamental price, inventory and cumulative impacts, using the approximation of the conditional expectation ([49](https://arxiv.org/html/2601.03799v1#S3.E49 "In 3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). Moreover, for a given inventory level indexed by kxk\_{x}, the supremum in the Bellman equation ([43](https://arxiv.org/html/2601.03799v1#S3.E43 "In 3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is evaluated over a discrete set of trade sizes drawn from the inventory grid: x(k)x^{(k)} for k∈0,…,kxk\in{0,\ldots,k\_{x}}. This restriction enforces non-negativity of trades, thereby introducing no-buy constraints into the optimization. This design choice is motivated by computational efficiency and by the empirical observation that none of the optimal profiles in the martingale case involve buy orders (see Section [2.3](https://arxiv.org/html/2601.03799v1#S2.SS3 "2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). We therefore restrict the use of the algorithm to the martingale case (μ=0\mu=0). Taking μ≠0\mu\neq 0 and allowing for buy orders would simply require extending the grid over which the supremum is computed. Appendix [C](https://arxiv.org/html/2601.03799v1#A0.SS3 "C Backward algorithm ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact") provides a pseudocode of the backward algorithm. In Appendix [D](https://arxiv.org/html/2601.03799v1#A0.SS4 "D Consistency and stability checks ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), we present consistency checks within the Uniswap v2 framework to empirically validate our numerical method. Specifically, we compare the numerical results in the particular case where L0=L1L\_{0}=L\_{1} with the closed-form solution derived in Section [2.2.3](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS3 "2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), both evaluated along the mean price trajectory. Results show that the discretization scheme yields accurate estimates of the optimal strategy in the Uniswap v2 framework.

### 3.3 Numerical results

Let us analyze the impact of the threshold price p¯\overline{p} relative to the initial price f0f\_{0} on the optimal execution strategy evaluated along the mean price trajectory. The schedules are computed using the discretization scheme described in Section [3.2](https://arxiv.org/html/2601.03799v1#S3.SS2 "3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), and correspond to the solution to the dynamic programming problem under the two-layer liquidity profile introduced in Section [3.1](https://arxiv.org/html/2601.03799v1#S3.SS1 "3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). We adopt a grid resolution of Kf=500K\_{f}=500, Kx=250K\_{x}=250 and KI=500K\_{I}=500. In Appendix [D](https://arxiv.org/html/2601.03799v1#A0.SS4 "D Consistency and stability checks ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), we vary the grid sizes to assess the stability of the numerical scheme. The threshold level is expressed in terms of a spread s¯\overline{s}, defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p¯=f0+s¯.\overline{p}=f\_{0}+\overline{s}. |  | (51) |

We distinguish three regimes depending on the position of the threshold p¯\overline{p} relative to the initial price f0f\_{0}.

![Refer to caption](x13.png)


(a) Low price threshold regime

![Refer to caption](x14.png)


(b) Regime with a price threshold close to the initial spot price

![Refer to caption](x15.png)


(c) High price threshold regime

Figure 8: Influence of the spread s¯\overline{s} on the optimal execution schedule; T=1T=1, N=10N=10, ξ=1\xi=1, L0=1000L\_{0}=1000, L1=500L\_{1}=500, f0=1f\_{0}=1, μ=0\mu=0, σ=0.3\sigma=0.3, J=0J=0, ρ=3\rho=3, Kf=500K\_{f}=500, Kx=250K\_{x}=250 and KI=500K\_{I}=500.

##### Low price threshold regime

In Figure [8(a)](https://arxiv.org/html/2601.03799v1#S3.F8.sf1 "In Figure 8 ‣ 3.3 Numerical results ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), we present the execution strategies for spreads ranging from −5000-5000bps to −100-100bps. When the threshold price lies far below the initial price (s¯=−5000\overline{s}=-5000bps), the optimal execution strategy coincides with the strategy obtained in the Uniswap v2 framework. Indeed, the probability that the price reaches the low-liquidity zone before maturity is very low. Consequently, the model disregards the discontinuity in liquidity and proceeds as if the pool exhibited constant liquidity. Then, as the threshold gradually approaches f0f\_{0}, the execution strategy progressively front-loads the trades. Indeed, we observe a skew in the execution profile, with more volume executed in the early steps of the horizon. This adjustment reflects the increasing probability, driven by price volatility, that the threshold will be crossed before maturity. In anticipation of the associated cost increase in the low-liquidity regime, the model accelerates execution to mitigate potential higher slippage and price impact.

![Refer to caption](x16.png)


Figure 9: Influence of L1L\_{1} on the optimal execution schedule; T=1T=1, N=10N=10, ξ=1\xi=1, L0=1000L\_{0}=1000, f0=1f\_{0}=1, s¯=0\overline{s}=0, μ=0\mu=0, σ=0.3\sigma=0.3, J=0J=0, ρ=3\rho=3, Kf=500K\_{f}=500, Kx=250K\_{x}=250 and KI=500K\_{I}=500.

##### Regime with a price threshold close to the initial spot price

The execution strategies for spreads ranging from −100-100bps to 0bps are reported in Figure [8(b)](https://arxiv.org/html/2601.03799v1#S3.F8.sf2 "In Figure 8 ‣ 3.3 Numerical results ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). When the threshold level is equal to the initial price (s¯=0\overline{s}=0), the optimal execution strategy consists of full liquidation at maturity. As previously mentioned, the strategy is evaluated along the mean price trajectory, which, in this case, remains at the threshold throughout the trading horizon. Consequently, the trader holds his position, waiting for a favorable price movement to benefit from lower costs in the higher-liquidity zone. Figure [9](https://arxiv.org/html/2601.03799v1#S3.F9 "Figure 9 ‣ Low price threshold regime ‣ 3.3 Numerical results ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") illustrates the influence of the lower-layer liquidity parameter L1L\_{1} on the optimal strategy. As L1L\_{1} approaches L0L\_{0}, the optimal strategy gradually transitions from full liquidation at maturity to the Uniswap v2 optimal execution schedule when L1L\_{1} reaches L0L\_{0}.

##### High price threshold regime

Figure [8(c)](https://arxiv.org/html/2601.03799v1#S3.F8.sf3 "In Figure 8 ‣ 3.3 Numerical results ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") illustrates the execution profiles for spreads ranging from 0bps to 50005000bps. Strategies for spreads under 100100bps are omitted as they yield similar results. When the threshold price is set above the initial price, the execution strategy shifts again toward earlier liquidation. The probability of entering the low-liquidity region becomes lower, and the model gradually converges toward the same constant-liquidity execution profile. Indeed, when the fundamental price is a martingale, the optimal strategy under constant liquidity is independent of the liquidity level (see Section [2.2](https://arxiv.org/html/2601.03799v1#S2.SS2 "2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

## 4 Discussion and conclusion

In this paper, we study the optimal execution problem on AMMs, aiming to maximize the sum of expected cash-flows under transient price impact. The study covers both CPAMMs (Uniswap v2) and CLAMMs (Uniswap v3). We derive closed-form solutions under general fundamental price dynamics for CPAMMs, and analyze the resulting strategies when the fundamental price follows a geometric Brownian motion. We also solve the reformulated problem within a dynamic programming framework to allow for price feedback during execution. For CLAMMs, closed-form solutions are no longer available and the optimal strategy is then approximated numerically using a discretization scheme. The analysis is developed within a two-layer liquidity framework, which naturally extends to multiple layers. Numerical results are obtained using synthetic data. The application to real market data, including the calibration of resilience kernels, will be conducted in a companion paper.

In the CPAMMs case, exponential resilience leads to an asymmetric bucket-shaped execution profile, while power-law-like resilience results in an asymmetric U-shaped profile. In the literature, such asymmetries typically stem from risk aversion. In our setting, they arise from the endogenous and stochastic nature of market impact and slippage. Incorporating a mean-variance objective function following the approach of Almgren and Chriss ([2001](https://arxiv.org/html/2601.03799v1#bib.bib3 "Optimal execution of portfolio transactions")) would enrich the model from a risk-management perspective but would pose significant mathematical challenges which we leave for future investigation.

The optimal execution strategy on CPAMMs, based on a first-order approximation, is independent of the liquidity level of the pool in the martingale setting. In contrast, under the two-layer liquidity profile of CLAMMs, the strategy depends on both the liquidity levels and the position of the spot price relative to the price threshold at which the liquidity changes. When liquidity is more favorable, the strategy tends to front-load execution to reduce exposure to the risk of falling into the low-liquidity region following an adverse price movement, where execution costs are higher. Conversely, when the liquidity level is less favorable, the strategy postpones execution, waiting for a favorable price movement to benefit from lower costs in the higher-liquidity zone. We believe that this work may help practitioners in the DeFi ecosystem better understand execution mechanisms and reduce associated costs.

Finally, we assume that the liquidity of the pool is constant throughout the trading horizon, i.e., LPs remain passive. In the spirit of Cartea et al. ([2025](https://arxiv.org/html/2601.03799v1#bib.bib26 "Decentralised finance and automated market making: Execution and speculation")), a natural extension would be to incorporate stochastic liquidity dynamics.

## Acknowledgments

The authors would like to thank Mohamed Frihat, Vincent Danos, Hamza El Khalloufi and Alejandro Roigé Vázquez for fruitful discussions.

This work used HPC resources from the “Mésocentre” computing center of CentraleSupélec and École Normale Supérieure Paris-Saclay supported by CNRS and Région Île-de-France.

## Disclosure of interest

The authors have no competing interests to declare.

## References

* H. Adams, N. Zinsmeister, and D. Robinson (2020)
  Uniswap v2 core.
  Note: Available at <https://app.uniswap.org/whitepaper.pdf>
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p2.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* H. Adams, N. Zinsmeister, M. Salem, R. Keefer, and D. Robinson (2021)
  Uniswap v3 core.
  Note: Available at <https://app.uniswap.org/whitepaper-v3.pdf>
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p2.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* A. Alfonsi, A. Fruth, and A. Schied (2008)
  Constrained portfolio liquidation in a limit order book model.
  Banach Center Publications 83,  pp. 9–25.
  Cited by: [§A.2](https://arxiv.org/html/2601.03799v1#A0.SS1.SSS2.2.p2.8 "Proof. ‣ A.2 Proof of Corollary 2 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* A. Alfonsi, A. Fruth, and A. Schied (2010)
  Optimal execution strategies in limit order books with general shape functions.
  Quantitative Finance 10 (2),  pp. 143–157.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§2.2.3](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS3.p8.1 "2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* R. Almgren and N. Chriss (1999)
  Value under liquidation.
  Risk 12 (12),  pp. 61–63.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* R. Almgren and N. Chriss (2001)
  Optimal execution of portfolio transactions.
  Journal of Risk 3,  pp. 5–40.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1.Px3.p1.5 "Scenario 3 (predominant permanent impact) ‣ 2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§4](https://arxiv.org/html/2601.03799v1#S4.p2.1 "4 Discussion and conclusion ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* R. F. Almgren (2003)
  Optimal execution with nonlinear impact functions and trading-enhanced risk.
  Applied Mathematical Finance 10 (1),  pp. 1–18.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* T. Bochud and D. Challet (2007)
  Optimal approximations of power laws with exponentials: Application to volatility models with long memory.
  Quantitative Finance 7 (6),  pp. 585–589.
  Cited by: [§2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1.Px2.p1.12 "Scenario 2 (power-law resilience) ‣ 2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* J. Bouchaud, J. Bonart, J. Donier, and M. Gould (2018)
  Trades, quotes and prices: Financial markets under the microscope.
   Cambridge University Press.
  Cited by: [§2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1.Px2.p1.12 "Scenario 2 (power-law resilience) ‣ 2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* E. Busseti and F. Lillo (2012)
  Calibration of optimal execution of financial transactions in the presence of transient market impact.
  Journal of Statistical Mechanics: Theory and Experiment 2012 (09),  pp. P09010.
  Cited by: [§2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1.Px2.p1.12 "Scenario 2 (power-law resilience) ‣ 2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* Á. Cartea, F. Drissi, and M. Monga (2025)
  Decentralised finance and automated market making: Execution and speculation.
  Journal of Economic Dynamics and Control 177,  pp. 105134.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p5.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§1](https://arxiv.org/html/2601.03799v1#S1.p6.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§2.1](https://arxiv.org/html/2601.03799v1#S2.SS1.p4.5 "2.1 Mathematical framework ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§2.2.1](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS1.p2.14 "2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§4](https://arxiv.org/html/2601.03799v1#S4.p4.1 "4 Discussion and conclusion ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* Á. Cartea, S. Jaimungal, and J. Penalva (2015)
  Algorithmic and high-frequency trading.
   Cambridge University Press.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* G. Curato, J. Gatheral, and F. Lillo (2017)
  Optimal execution with non-linear transient market impact.
  Quantitative Finance 17 (1),  pp. 41–54.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* M. Egorov (2019)
  StableSwap - efficient mechanism for stablecoin liquidity.
  Note: Available at <https://classic.curve.finance/files/stableswap-paper.pdf>
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p2.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* J. Gatheral, A. Schied, and A. Slynko (2012)
  Transient linear price impact and Fredholm integral equations.
  Mathematical Finance: An International Journal of Mathematics, Statistics and Financial Economics 22 (3),  pp. 445–474.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* O. Guéant (2016)
  The financial mathematics of market liquidity: From optimal execution to market making.
  Vol. 33, CRC Press.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* D. E. Kirk (2004)
  Optimal control theory: An introduction.
   Courier Corporation.
  Cited by: [§2.2.3](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS3.p1.6 "2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* F. Martinelli and N. Mushegian (2019)
  A non-custodial portfolio manager, liquidity provider, and price sensor.
  Note: Available at <https://docs.balancer.fi/whitepaper.pdf>
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p2.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* A. A. Obizhaeva and J. Wang (2013)
  Optimal trading strategy and supply/demand dynamics.
  Journal of Financial markets 16 (1),  pp. 1–32.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§1](https://arxiv.org/html/2601.03799v1#S1.p6.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1.Px1.p1.4 "Scenario 1 (exponential resilience) ‣ 2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").
* T. Tran, D. A. Tran, and T. Nguyen (2024)
  Order book inspired automated market making.
  IEEE Access 12,  pp. 36743–36763.
  Cited by: [§1](https://arxiv.org/html/2601.03799v1#S1.p4.1 "1 Introduction ‣ Optimal execution on Uniswap v2/v3 under transient price impact"),
  [§2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1.p1.8 "2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").

## Appendix

### A Proofs

#### A.1 Proof of Proposition [1](https://arxiv.org/html/2601.03799v1#Thmproposition1 "Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") and Corollary [1](https://arxiv.org/html/2601.03799v1#Thmcorollary1 "Corollary 1 (Martingale case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")

###### Proof.

By introducing a Lagrange multiplier λ∈ℝ\lambda\in\mathbb{R} for the equality ∑m=0Nδm=ξ\sum^{N}\_{m=0}\delta\_{m}=\xi in ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), we obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ∗=argmax𝛿\displaystyle\delta^{\*}=\underset{\delta}{\mathrm{argmax}} | 𝔼​[∑n=0N𝒞n]+λ​(ξ−∑n=0Nδn).\displaystyle\mathbb{E}\Big[\sum^{N}\_{n=0}\mathcal{C}\_{n}\Big]+\lambda\big(\xi-\sum^{N}\_{n=0}\delta\_{n}\big). |  | (52) |

For m=0,…,Nm=0,\ldots,N, the first-order condition from ([52](https://arxiv.org/html/2601.03799v1#A0.E52 "In Proof. ‣ A.1 Proof of Proposition 1 and Corollary 1 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂δm​𝔼​[∑n=0N𝒞n]=λ,\frac{\partial}{\partial\delta\_{m}}\mathbb{E}\Big[\sum^{N}\_{n=0}\mathcal{C}\_{n}\Big]=\lambda, |  | (53) |

where,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂∂δm​𝔼​[∑n=0N𝒞n]=𝔼​[fm]\displaystyle\frac{\partial}{\partial\delta\_{m}}\mathbb{E}\Big[\sum^{N}\_{n=0}\mathcal{C}\_{n}\Big]=\mathbb{E}[f\_{m}] | −2L​∑n=0mδn∗​(∑j=0Jωj​e−ρj​(m−n)​Δ​𝔼​[fm​fn])\displaystyle-\frac{2}{L}\sum^{m}\_{n=0}\delta^{\*}\_{n}\Big(\sum^{J}\_{j=0}\omega\_{j}e^{-\rho\_{j}(m-n)\Delta}\mathbb{E}[f\_{m}\sqrt{f\_{n}}]\Big) |  | (54) |
|  |  | −2L​∑n=m+1Nδn∗​(∑j=0Jωj​e−ρj​(n−m)​Δ​𝔼​[fn​fm]).\displaystyle-\frac{2}{L}\sum^{N}\_{n=m+1}\delta^{\*}\_{n}\Big(\sum^{J}\_{j=0}\omega\_{j}e^{-\rho\_{j}(n-m)\Delta}\mathbb{E}[f\_{n}\sqrt{f\_{m}}]\Big). |  |

We can rewrite the N+1N+1 first-order conditions ([53](https://arxiv.org/html/2601.03799v1#A0.E53 "In Proof. ‣ A.1 Proof of Proposition 1 and Corollary 1 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) in compact matrix form as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​δ∗=L2​(B−λ​𝟙),A\delta^{\*}=\frac{L}{2}\big(B-\lambda\mathbbm{1}\big), |  | (55) |

where 𝟙=(1,…,1)⊤\mathbbm{1}=\big(1,\ldots,1\big)^{\top}. The vector B∈ℝN+1B\in\mathbb{R}^{N+1} and the matrix A∈ℝ(N+1)×(N+1)A\in\mathbb{R}^{(N+1)\times(N+1)}, defined in ([14](https://arxiv.org/html/2601.03799v1#S2.E14 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) and ([15](https://arxiv.org/html/2601.03799v1#S2.E15 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) respectively, are derived from ([54](https://arxiv.org/html/2601.03799v1#A0.E54 "In Proof. ‣ A.1 Proof of Proposition 1 and Corollary 1 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). Substituting ([55](https://arxiv.org/html/2601.03799v1#A0.E55 "In Proof. ‣ A.1 Proof of Proposition 1 and Corollary 1 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) in the volume constraint ([9](https://arxiv.org/html/2601.03799v1#S2.E9 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗=𝟙⊤​A−1​B−2​ξL𝟙⊤​A−1​𝟙,\lambda^{\*}=\frac{\mathbbm{1}^{\top}A^{-1}B-\frac{2\xi}{L}}{\mathbbm{1}^{\top}A^{-1}\mathbbm{1}}, |  | (56) |

and plugging λ∗\lambda^{\*} in ([55](https://arxiv.org/html/2601.03799v1#A0.E55 "In Proof. ‣ A.1 Proof of Proposition 1 and Corollary 1 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) yields the closed-form optimal execution schedule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗=L2​(A−1​B−λ∗​A−1​𝟙).\delta^{\*}=\frac{L}{2}(A^{-1}B-\lambda^{\*}A^{-1}\mathbbm{1}). |  | (57) |

When the fundamental price process is a martingale, the expected price at each time step remains constant and equal to the initial price. The vector BB reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B=f0​𝟙.B=f\_{0}\mathbbm{1}. |  | (58) |

Plugging ([58](https://arxiv.org/html/2601.03799v1#A0.E58 "In Proof. ‣ A.1 Proof of Proposition 1 and Corollary 1 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) into the general solution ([57](https://arxiv.org/html/2601.03799v1#A0.E57 "In Proof. ‣ A.1 Proof of Proposition 1 and Corollary 1 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the optimal execution schedule simplifies to ([16](https://arxiv.org/html/2601.03799v1#S2.E16 "In Corollary 1 (Martingale case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).
∎

#### A.2 Proof of Corollary [2](https://arxiv.org/html/2601.03799v1#Thmcorollary2 "Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")

###### Proof.

Under the geometric Brownian motion assumption ([17](https://arxiv.org/html/2601.03799v1#S2.E17 "In Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), the expectations appearing in ([14](https://arxiv.org/html/2601.03799v1#S2.E14 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) and ([15](https://arxiv.org/html/2601.03799v1#S2.E15 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) admit closed-form expressions. For m=0,…,Nm=0,\ldots,N, the expected fundamental price reads 𝔼​[fm]=f0​eμ​m​Δ\mathbb{E}[f\_{m}]=f\_{0}e^{\mu m\Delta}. Moreover, for n≤mn\leq m, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[fm​fn]=f0​f0​eμ​(m+n2)​Δ+3​σ28​n​Δ,\mathbb{E}[f\_{m}\sqrt{f\_{n}}]=f\_{0}\sqrt{f\_{0}}e^{\mu(m+\frac{n}{2})\Delta+\frac{3\sigma^{2}}{8}n\Delta}, |  | (59) |

and for n>mn>m:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[fn​fm]=f0​f0​eμ​(n+m2)​Δ+3​σ28​m​Δ.\mathbb{E}[f\_{n}\sqrt{f\_{m}}]=f\_{0}\sqrt{f\_{0}}e^{\mu(n+\frac{m}{2})\Delta+\frac{3\sigma^{2}}{8}m\Delta}. |  | (60) |

We start with a single resilience factor (i.e., J=0J=0), for which the matrix AA from ([15](https://arxiv.org/html/2601.03799v1#S2.E15 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) takes the following form, up to the multiplicative factor f0​f0f\_{0}\sqrt{f\_{0}}, which is omitted for notational clarity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A=[b0a​b0a2​b0a3​b0⋯aN​b0a​b0b1a​b1a2​b1⋯aN−1​b1a2​b0a​b1b2a​b2⋯aN−2​b2a3​b0a2​b1a​b2b3⋯aN−3​b3⋮⋮⋮⋮⋱⋮aN​b0aN−1​b1aN−2​b2aN−3​b3⋯bN].A=\begin{bmatrix}b\_{0}&ab\_{0}&a^{2}b\_{0}&a^{3}b\_{0}&\cdots&a^{N}b\_{0}\\ ab\_{0}&b\_{1}&ab\_{1}&a^{2}b\_{1}&\cdots&a^{N-1}b\_{1}\\ a^{2}b\_{0}&ab\_{1}&b\_{2}&ab\_{2}&\cdots&a^{N-2}b\_{2}\\ a^{3}b\_{0}&a^{2}b\_{1}&ab\_{2}&b\_{3}&\cdots&a^{N-3}b\_{3}\\ \vdots&\vdots&\vdots&\vdots&\ddots&\vdots\\ a^{N}b\_{0}&a^{N-1}b\_{1}&a^{N-2}b\_{2}&a^{N-3}b\_{3}&\cdots&b\_{N}\end{bmatrix}. |  | (61) |

where a=e−(ρ−μ)​Δa=e^{-(\rho-\mu)\Delta} and bn=e(3​μ2+3​σ28)​n​Δb\_{n}=e^{\big(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8}\big)n\Delta}. Let e0,…,eNe\_{0},\ldots,e\_{N} denote the canonical basis of ℝN+1\mathbb{R}^{N+1} and, in the spirit of Alfonsi et al. ([2008](https://arxiv.org/html/2601.03799v1#bib.bib8 "Constrained portfolio liquidation in a limit order book model")), we define the vectors v0,…,vNv\_{0},\ldots,v\_{N} by the recursive formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {v0=e0vn=vn−1​a+en​γn,\left\{\begin{array}[]{ll}v\_{0}=e\_{0}\\ v\_{n}=v\_{n-1}a+e\_{n}\sqrt{\gamma\_{n}},\end{array}\right. |  | (62) |

where γn=bn−a2​bn−1\gamma\_{n}=b\_{n}-a^{2}b\_{n-1} for n=1,…,Nn=1,\ldots,N, with γ0=1\gamma\_{0}=1, and subject to the condition on the drift: μ<3​σ24+4​ρ\mu<\frac{3\sigma^{2}}{4}+4\rho to ensure γn>0\gamma\_{n}>0 for n=1,…,Nn=1,\ldots,N. This condition is automatically satisfied in the martingale case (i.e., when μ=0\mu=0). The matrix AA is the corresponding Gram matrix: ⟨vm,vn⟩=a|m−n|​bmin⁡(m,n)=Am​n\langle v\_{m},v\_{n}\rangle=a^{|m-n|}b\_{\min(m,n)}=A\_{mn} for m=0,…,Nm=0,\ldots,N and n=0,…,Nn=0,\ldots,N. Indeed, first by induction: ⟨vn,vn⟩=bn\langle v\_{n},v\_{n}\rangle=b\_{n}. Second, for n<mn<m we have: ⟨vm,vn⟩=am−n​⟨vn,vn⟩\langle v\_{m},v\_{n}\rangle=a^{m-n}\langle v\_{n},v\_{n}\rangle and for m<nm<n: ⟨vm,vn⟩=an−m​⟨vm,vm⟩\langle v\_{m},v\_{n}\rangle=a^{n-m}\langle v\_{m},v\_{m}\rangle. Thus, the matrix AA is positive definite. Therefore, the objective function is strictly concave as the associated Hessian matrix is given by −2L​A-\frac{2}{L}A. In addition, the volume constraint ∑n=0Nδn=ξ\sum\_{n=0}^{N}\delta\_{n}=\xi defines a convex feasible set. Together, these properties guarantee that the optimal strategy δ∗\delta^{\*} in ([13](https://arxiv.org/html/2601.03799v1#S2.E13 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is the unique maximizer of the execution problem ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

From the recursive formula ([62](https://arxiv.org/html/2601.03799v1#A0.E62 "In Proof. ‣ A.2 Proof of Corollary 2 ‣ A Proofs ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), we also have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vn=∑k=0n[an−k​γk]​ek.v\_{n}=\sum^{n}\_{k=0}\big[a^{n-k}\sqrt{\gamma\_{k}}\big]e\_{k}. |  | (63) |

Let VV be the upper triangular matrix whose columns are the vectors v0,…,vNv\_{0},\ldots,v\_{N}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V=[1aa2⋯aN0γ1a​γ1⋯aN−1​γ100γ2⋯aN−2​γ2⋮⋮⋮⋱⋮000⋯γN].V=\begin{bmatrix}1&a&a^{2}&\cdots&a^{N}\\ 0&\sqrt{\gamma\_{1}}&a\sqrt{\gamma\_{1}}&\cdots&a^{N-1}\sqrt{\gamma\_{1}}\\ 0&0&\sqrt{\gamma\_{2}}&\cdots&a^{N-2}\sqrt{\gamma\_{2}}\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&\sqrt{\gamma\_{N}}\end{bmatrix}. |  | (64) |

Then, A=V⊤​VA=V^{\top}V. Indeed, for any m=0,…,Nm=0,\ldots,N and n=0,…,Nn=0,\ldots,N:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (V⊤​V)m​n=∑k=0NVk​m​Vk​n=∑k=0min⁡(m,n)Vk​m​Vk​n,(V^{\top}V)\_{mn}=\sum\_{k=0}^{N}V\_{km}V\_{kn}=\sum\_{k=0}^{\min(m,n)}V\_{km}V\_{kn}, |  | (65) |

since VV is upper triangular. Substituting the expression for Vk​mV\_{km} and Vk​nV\_{kn}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (V⊤​V)m​n=∑k=0min⁡(m,n)[am−k​γk]​[an−k​γk]=am+n​∑k=0min⁡(m,n)a−2​k​(bk−a2​bk−1),(V^{\top}V)\_{mn}=\sum\_{k=0}^{\min(m,n)}\left[a^{m-k}\sqrt{\gamma\_{k}}\right]\left[a^{n-k}\sqrt{\gamma\_{k}}\right]=a^{m+n}\sum\_{k=0}^{\min(m,n)}a^{-2k}\big(b\_{k}-a^{2}b\_{k-1}\big), |  | (66) |

where b−1=0b\_{-1}=0. This sum telescopes to a−2​min⁡(m,n)​bmin⁡(m,n)a^{-2\min(m,n)}b\_{\min(m,n)}, yielding (V⊤​V)m​n=a|m−n|​bmin⁡(m,n)=Am​n(V^{\top}V)\_{mn}=a^{|m-n|}b\_{\min(m,n)}=A\_{mn}. The diagonals coefficients of the upper triangular matrix VV are all strictly positives. Then, VV is invertible and A−1=V−1​(V−1)⊤A^{-1}=V^{-1}(V^{-1})^{\top}. Finally, the inverse matrix A−1A^{-1} is tridiagonal and is given by ([18](https://arxiv.org/html/2601.03799v1#S2.E18 "In Corollary 2 (Geometric Brownian motion case). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).

In the general multi-kernel case, let e0,…,eNe\_{0},\ldots,e\_{N} denote the canonical basis of ℝN+1\mathbb{R}^{N+1}, and let f0,…,fJf\_{0},\ldots,f\_{J} denote the canonical basis of ℝJ+1\mathbb{R}^{J+1}. For j=0,…,Jj=0,\ldots,J, we define the vectors v0j,…,vNjv^{j}\_{0},\ldots,v^{j}\_{N} by the recursive formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {v0j=e0vnj=vn−1j​aj+en​bn−aj2​bn−1,\left\{\begin{array}[]{ll}v^{j}\_{0}=e\_{0}\\ v^{j}\_{n}=v^{j}\_{n-1}a\_{j}+e\_{n}\sqrt{b\_{n}-a^{2}\_{j}b\_{n-1}},\end{array}\right. |  | (67) |

where aj=e−(ρj−μ)​Δa\_{j}=e^{-(\rho\_{j}-\mu)\Delta}, bn=e(3​μ2+3​σ28)​n​Δb\_{n}=e^{\big(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8}\big)n\Delta} and subject to the condition on the drift: μ<3​σ24+4​minj⁡ρj\mu<\frac{3\sigma^{2}}{4}+4\min\_{j}\rho\_{j}, to ensure bn−aj2​bn−1>0b\_{n}-a^{2}\_{j}b\_{n-1}>0 for n=1,…,Nn=1,\ldots,N and j=0,…,Jj=0,\ldots,J. Then, we define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vn=∑j=0Jωj​(fj⊗vnj).v\_{n}=\sum^{J}\_{j=0}\sqrt{\omega\_{j}}(f\_{j}\otimes v^{j}\_{n}). |  | (68) |

The matrix AA is the corresponding Gram matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨vm,vn⟩=∑j=0Jωj​⟨vmj,vnj⟩=∑j=0Jωj​aj|m−n|​bmin⁡(m,n)=Am​n.\langle v\_{m},v\_{n}\rangle=\sum^{J}\_{j=0}\omega\_{j}\langle v^{j}\_{m},v^{j}\_{n}\rangle=\sum^{J}\_{j=0}\omega\_{j}a^{|m-n|}\_{j}b\_{\min(m,n)}=A\_{mn}. |  | (69) |

Following the same arguments as in the single resilience factor case, the objective function is strictly concave and the optimal strategy δ∗\delta^{\*} in ([13](https://arxiv.org/html/2601.03799v1#S2.E13 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) is the unique maximizer of the execution problem ([12](https://arxiv.org/html/2601.03799v1#S2.E12 "In 2.2.1 Problem formulation ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). However, the methodology used to derive the inverse of AA in the single-kernel case does not extend to the general multi-kernel setting.
∎

#### A.3 Proof of Proposition [2](https://arxiv.org/html/2601.03799v1#Thmproposition2 "Proposition 2 (Dynamic programming: closed-loop solution). ‣ 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")

###### Proof.

We consider the ansatz ([23](https://arxiv.org/html/2601.03799v1#S2.E23 "In Proposition 2 (Dynamic programming: closed-loop solution). ‣ 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) with coefficients An,(Bnj)j=0J,Cn,Dn,(En)j=0JA\_{n},(B^{j}\_{n})^{J}\_{j=0},C\_{n},D\_{n},(E\_{n})^{J}\_{j=0} and (Fn)j1,j2=0J(F\_{n})^{J}\_{j\_{1},j\_{2}=0} determined by backward recursion. Substituting ([23](https://arxiv.org/html/2601.03799v1#S2.E23 "In Proposition 2 (Dynamic programming: closed-loop solution). ‣ 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) into the Bellman equation ([21](https://arxiv.org/html/2601.03799v1#S2.E21 "In 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) yields a quadratic objective in δn\delta\_{n}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vn​(xn,(Inj)j=0J,fn)=supδn\displaystyle v\_{n}(x\_{n},(I^{j}\_{n})^{J}\_{j=0},f\_{n})=\sup\_{\delta\_{n}} | −δn2fnfn[1L+2L∑j=0JBn+1je(μ−ρj)​Δ−Cn+1e(3​μ2+3​σ28)​Δ\displaystyle-\delta^{2}\_{n}f\_{n}\sqrt{f\_{n}}\Big[\frac{1}{L}+\frac{2}{L}\sum^{J}\_{j=0}B^{j}\_{n+1}e^{(\mu-\rho\_{j})\Delta}-C\_{n+1}e^{(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8})\Delta} |  | (70) |
|  |  | −4L2∑j1=0J∑j2=0JFn+1j1,j2e(μ2−ρj1−ρj2−σ28)​Δ]\displaystyle-\frac{4}{L^{2}}\sum^{J}\_{j\_{1}=0}\sum^{J}\_{j\_{2}=0}F^{j\_{1},j\_{2}}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j\_{1}}-\rho\_{j\_{2}}-\frac{\sigma^{2}}{8})\Delta}\Big] |  |
|  |  | +δn[fn(1−An+1eμ​Δ+2L∑j=0JEn+1je(μ2−ρj−σ28)​Δ)\displaystyle+\delta\_{n}\Big[f\_{n}\big(1-A\_{n+1}e^{\mu\Delta}+\frac{2}{L}\sum^{J}\_{j=0}E^{j}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j}-\frac{\sigma^{2}}{8})\Delta}\big) |  |
|  |  | +fn​∑j1=0JInj1​(−ωj1−Bn+1j1​e(μ−ρj1)​Δ+4L​∑j2=0JFn+1j1,j2​e(μ2−ρj1−ρj2−σ28)​Δ)\displaystyle+f\_{n}\sum^{J}\_{j\_{1}=0}I^{j\_{1}}\_{n}\big(-\omega\_{j\_{1}}-B^{j\_{1}}\_{n+1}e^{(\mu-\rho\_{j\_{1}})\Delta}+\frac{4}{L}\sum^{J}\_{j\_{2}=0}F^{j\_{1},j\_{2}}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j\_{1}}-\rho\_{j\_{2}}-\frac{\sigma^{2}}{8})\Delta}\big) |  |
|  |  | +xnfnfn(2L∑j=0JBn+1je(μ−ρj)​Δ−2Cn+1e(3​μ2+3​σ28)​Δ)]\displaystyle+x\_{n}f\_{n}\sqrt{f\_{n}}\big(\frac{2}{L}\sum^{J}\_{j=0}B^{j}\_{n+1}e^{(\mu-\rho\_{j})\Delta}-2C\_{n+1}e^{(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8})\Delta}\big)\Big] |  |
|  |  | +xn​fn​[An+1​eμ​Δ+∑j=0JBn+1j​e(μ−ρj)​Δ​Inj+Cn+1​e(3​μ2+3​σ28)​Δ​xn​fn]\displaystyle+x\_{n}f\_{n}\Big[A\_{n+1}e^{\mu\Delta}+\sum^{J}\_{j=0}B^{j}\_{n+1}e^{(\mu-\rho\_{j})\Delta}I^{j}\_{n}+C\_{n+1}e^{(\frac{3\mu}{2}+\frac{3\sigma^{2}}{8})\Delta}x\_{n}\sqrt{f\_{n}}\Big] |  |
|  |  | +fn[Dn+1e(μ2−σ28)​Δ+∑j=0JEn+1je(μ2−ρj−σ28)​ΔInj\displaystyle+\sqrt{f\_{n}}\Big[D\_{n+1}e^{(\frac{\mu}{2}-\frac{\sigma^{2}}{8})\Delta}+\sum^{J}\_{j=0}E^{j}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j}-\frac{\sigma^{2}}{8})\Delta}I^{j}\_{n} |  |
|  |  | +∑j1=0J∑j2=0JFn+1j1,j2e(μ2−ρj1−ρj2−σ28)​ΔInj1Inj2],\displaystyle+\sum^{J}\_{j\_{1}=0}\sum^{J}\_{j\_{2}=0}F^{j\_{1},j\_{2}}\_{n+1}e^{(\frac{\mu}{2}-\rho\_{j\_{1}}-\rho\_{j\_{2}}-\frac{\sigma^{2}}{8})\Delta}I^{j\_{1}}\_{n}I^{j\_{2}}\_{n}\Big], |  |

and leads to the explicit control ([24](https://arxiv.org/html/2601.03799v1#S2.E24 "In Proposition 2 (Dynamic programming: closed-loop solution). ‣ 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")). The substitution of the optimal control into the Bellman equation ([21](https://arxiv.org/html/2601.03799v1#S2.E21 "In 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) and the terminal condition ([22](https://arxiv.org/html/2601.03799v1#S2.E22 "In 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), and identification of coefficients in the polynomial basis yields the backward recursions ([27](https://arxiv.org/html/2601.03799v1#S2.E27 "In Proposition 2 (Dynamic programming: closed-loop solution). ‣ 2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")).
∎

### B Optimal execution on Uniswap v2: the two-period martingale case

In the case μ=0\mu=0, N=1N=1 and J=0J=0, the matrix AA defined in ([15](https://arxiv.org/html/2601.03799v1#S2.E15 "In Proposition 1 (General solution). ‣ 2.2.2 General solution ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A=f0​f0​[1e−ρ​Δe−ρ​Δe3​σ28​Δ].A=f\_{0}\sqrt{f\_{0}}\begin{bmatrix}1&e^{-\rho\Delta}\\ e^{-\rho\Delta}&e^{\frac{3\sigma^{2}}{8}\Delta}\end{bmatrix}. |  | (71) |

The corresponding optimal trades are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ0∗=ξ​e3​σ28​Δ−e−ρ​Δe3​σ28​Δ+1−2​e−ρ​Δ,δ1∗=ξ​1−e−ρ​Δe3​σ28​Δ+1−2​e−ρ​Δ.\delta^{\*}\_{0}=\xi\frac{e^{\frac{3\sigma^{2}}{8}\Delta}-e^{-\rho\Delta}}{e^{\frac{3\sigma^{2}}{8}\Delta}+1-2e^{-\rho\Delta}},\ \delta^{\*}\_{1}=\xi\frac{1-e^{-\rho\Delta}}{e^{\frac{3\sigma^{2}}{8}\Delta}+1-2e^{-\rho\Delta}}. |  | (72) |

A direct comparison yields δ0∗>δ1∗\delta^{\*}\_{0}>\delta^{\*}\_{1} which establishes that the first trade is larger than the last one in the two-period framework, consistently with the numerical observations reported in Section [2.3.1](https://arxiv.org/html/2601.03799v1#S2.SS3.SSS1 "2.3.1 Illustrations ‣ 2.3 Numerical results ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact").

Differentiating with respect to volatility σ\sigma gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂δ0∗∂σ=ξ​3​σ4​Δ​e3​σ28​Δ​1−e−ρ​Δ(e3​σ28​Δ+1−2​e−ρ​Δ)2>0,\frac{\partial\delta^{\*}\_{0}}{\partial\sigma}=\xi\frac{3\sigma}{4}\Delta e^{\frac{3\sigma^{2}}{8}\Delta}\frac{1-e^{-\rho\Delta}}{\big(e^{\frac{3\sigma^{2}}{8}\Delta}+1-2e^{-\rho\Delta}\big)^{2}}>0, |  | (73) |

showing that higher volatility increases the size of the initial trade. Differentiation with respect to the resilience parameter ρ\rho gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂δ0∗∂ρ=ξ​Δ​e−ρ​Δ​1−e3​σ28​Δ(e3​σ28​Δ+1−2​e−ρ​Δ)2<0,\frac{\partial\delta^{\*}\_{0}}{\partial\rho}=\xi\Delta e^{-\rho\Delta}\frac{1-e^{\frac{3\sigma^{2}}{8}\Delta}}{\big(e^{\frac{3\sigma^{2}}{8}\Delta}+1-2e^{-\rho\Delta}\big)^{2}}<0, |  | (74) |

which indicates that faster price recovery of the liquidity pool reduces the size of the initial trade.

Finally, we study the asymptotic behavior of the optimal trades. When volatility becomes large, the solution converges to a fully front-loaded strategy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limσ→+∞δ0∗=ξ,limσ→+∞δ1∗=0.\lim\_{\sigma\rightarrow+\infty}\delta^{\*}\_{0}=\xi,\ \lim\_{\sigma\rightarrow+\infty}\delta^{\*}\_{1}=0. |  | (75) |

When the resilience parameter becomes large, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limρ→+∞δ0∗=ξ​e3​σ28​Δe3​σ28​Δ+1,limρ→+∞δ1∗=ξ​1e3​σ28​Δ+1.\lim\_{\rho\rightarrow+\infty}\delta^{\*}\_{0}=\xi\frac{e^{\frac{3\sigma^{2}}{8}\Delta}}{e^{\frac{3\sigma^{2}}{8}\Delta}+1},\ \lim\_{\rho\rightarrow+\infty}\delta^{\*}\_{1}=\xi\frac{1}{e^{\frac{3\sigma^{2}}{8}\Delta}+1}. |  | (76) |

In this regime, the price recovers instantaneously, and the trade allocation reflects only the effects of volatility, with a persistent asymmetry favoring earlier execution under higher expected price impact.

### C Backward algorithm

Under the two-layer liquidity framework introduced in Section [3.1](https://arxiv.org/html/2601.03799v1#S3.SS1 "3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), the backward algorithm is provided in the form of pseudocode in Algorithm [1](https://arxiv.org/html/2601.03799v1#alg1 "Algorithm 1 ‣ C Backward algorithm ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact").

Algorithm 1  Two-layer liquidity backward algorithm

* -

  The strategy parameters: T,NT,N and ξ\xi
* -

  The market parameters: f0,p¯,L0f\_{0},\overline{p},L\_{0} and L1L\_{1}
* -

  The model parameters: J,(ρj)j=0J,(ωj)j=0J,μJ,(\rho\_{j})^{J}\_{j=0},(\omega\_{j})^{J}\_{j=0},\mu and σ\sigma
* -

  The grid parameters: Kx,KI,KfK\_{x},K\_{I},K\_{f} and zz

* -

  The estimated optimal execution strategy δ∗\delta^{\*}
* -

  The associated value function vv

Set the grids according to ([45](https://arxiv.org/html/2601.03799v1#S3.E45 "In 3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), ([46](https://arxiv.org/html/2601.03799v1#S3.E46 "In 3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")), ([47](https://arxiv.org/html/2601.03799v1#S3.E47 "In 3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) and ([48](https://arxiv.org/html/2601.03799v1#S3.E48 "In 3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"))

Set vNv\_{N} according to ([43](https://arxiv.org/html/2601.03799v1#S3.E43 "In 3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact")) ⊳\triangleright The terminal value function is initialized.

for n=N−1,…,0n=N-1,\ldots,0 do ⊳\triangleright Backward iteration.

for kf=0,…,Kfk\_{f}=0,\ldots,K\_{f}, kx=0,…,Kxk\_{x}=0,\ldots,K\_{x}, kij=0,…,KIk^{j}\_{i}=0,\ldots,K\_{I}, j=0,…,Jj=0,\ldots,J do

for k=0,…,kxk=0,\ldots,k\_{x} do

Set δn=x(k)\delta\_{n}=x^{(k)} ⊳\triangleright Candidate trade from the inventory grid.

Compute the resulting cash-flow 𝒞n​(x(kx),(I(kij))j=0J,f(kf),δn)\mathcal{C}\_{n}(x^{(k\_{x})},(I^{(k^{j}\_{i})})^{J}\_{j=0},f^{(k\_{f})},\delta\_{n}) from ([44](https://arxiv.org/html/2601.03799v1#S3.E44 "In 3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"))

Update the cumulative price impacts In+1j​(x(kx),(I(kij))j=0J,f(kf),δn)I^{j}\_{n+1}(x^{(k\_{x})},(I^{(k^{j}\_{i})})^{J}\_{j=0},f^{(k\_{f})},\delta\_{n}) from ([41](https://arxiv.org/html/2601.03799v1#S3.E41 "In 3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"))

Update the remaining inventory xn+1=x(kx)−δnx\_{n+1}=x^{(k\_{x})}-\delta\_{n}

Perform a (J+1J+1)-d linear interpolation to derive vn+1​(x(kx),(I(kij))j=0J,f(kf))v\_{n+1}(x^{(k\_{x})},(I^{(k^{j}\_{i})})^{J}\_{j=0},f^{(k\_{f})}) for kf=0,…,Kfk\_{f}=0,\ldots,K\_{f}

Estimate the conditional expectation v¯n+1\overline{v}\_{n+1} using ([49](https://arxiv.org/html/2601.03799v1#S3.E49 "In 3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"))

Store the total value 𝒞n+v¯n+1\mathcal{C}\_{n}+\overline{v}\_{n+1} for each candidate trade δn\delta\_{n}

end for

Determine the optimal trade:

|  |  |  |
| --- | --- | --- |
|  | δn∗​(x(kx),(I(kij))j=0J,f(kf))=argmaxδn​𝒞n+v¯n+1\delta^{\*}\_{n}(x^{(k\_{x})},(I^{(k^{j}\_{i})})^{J}\_{j=0},f^{(k\_{f})})=\underset{\delta\_{n}}{\mathrm{argmax}}\ \mathcal{C}\_{n}+\overline{v}\_{n+1} |  |

Update the value function vn​(x(kx),(I(kij))j=0J,f(kf))v\_{n}(x^{(k\_{x})},(I^{(k^{j}\_{i})})^{J}\_{j=0},f^{(k\_{f})}) accordingly

end for

end for

### D Consistency and stability checks

![Refer to caption](x17.png)


(a) Mean absolute error

![Refer to caption](x18.png)


(b) Maximum absolute error

Figure 10: Mean and maximum absolute error with respect to KIK\_{I} and KfK\_{f} for Kx=250K\_{x}=250 in the Uniswap v2 framework; T=1T=1, N=10N=10, ξ=1\xi=1, L=1000L=1000, f0=1f\_{0}=1, μ=0\mu=0, σ=0.3\sigma=0.3, J=0J=0 and ρ=3\rho=3.

First, we present consistency checks conducted within the Uniswap v2 framework. We compare the numerical results obtained using the algorithm introduced in Section [3.2](https://arxiv.org/html/2601.03799v1#S3.SS2 "3.2 Discretization scheme ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), when the liquidity layers coincide (i.e., L0=L1L\_{0}=L\_{1}) with the closed-form solution derived in Section [2.2.3](https://arxiv.org/html/2601.03799v1#S2.SS2.SSS3 "2.2.3 Dynamic programming ‣ 2.2 Optimal execution strategy ‣ 2 The optimal scheduling problem on Uniswap v2 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), both evaluated along the mean price trajectory. Specifically, we fix Kx=250K\_{x}=250 and compute the maximum and mean absolute errors for different values of the grid sizes KfK\_{f} and KIK\_{I}. Results are reported in Figures [10(a)](https://arxiv.org/html/2601.03799v1#A0.F10.sf1 "In Figure 10 ‣ D Consistency and stability checks ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), [10(b)](https://arxiv.org/html/2601.03799v1#A0.F10.sf2 "In Figure 10 ‣ D Consistency and stability checks ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact") and demonstrate that the discretization scheme provides accurate estimates of the optimal strategy in the Uniswap v2 framework. These results also indicate that the accuracy of the numerical solution is more sensitive to the price grid size than to that of the cumulative market impact. Indeed, once KIK\_{I} exceeds 3030, both mean and maximum errors remain nearly unchanged for fixed values of KfK\_{f}.

![Refer to caption](x19.png)


(a) Mean absolute deviation

![Refer to caption](x20.png)


(b) Maximum absolute deviation

Figure 11: Mean and maximum absolute deviation with respect to KIK\_{I} and KfK\_{f} for Kx=250K\_{x}=250 in the two-layer liquidity framework; T=1T=1, N=10N=10, ξ=1\xi=1, L0=1000L\_{0}=1000, L1=500L\_{1}=500, f0=1f\_{0}=1, s¯=−25\overline{s}=-25bps, μ=0\mu=0, σ=0.3\sigma=0.3, J=0J=0 and ρ=3\rho=3.

Second, we assess the stability of the numerical scheme within the two-layer liquidity framework introduced in Section [3.1](https://arxiv.org/html/2601.03799v1#S3.SS1 "3.1 A two-layer liquidity framework ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact") by varying the grid resolution. We fix the threshold level at s¯=−25\overline{s}=-25bps and set Kx=250K\_{x}=250. We compute the maximum and mean absolute deviations relative to a reference solution obtained with the high-resolution configuration (Kf=500K\_{f}=500, Kx=250K\_{x}=250, and KI=500K\_{I}=500), presented in Section [3.3](https://arxiv.org/html/2601.03799v1#S3.SS3 "3.3 Numerical results ‣ 3 From Uniswap v2 to v3 ‣ Optimal execution on Uniswap v2/v3 under transient price impact"). The results, reported in Figures [11(a)](https://arxiv.org/html/2601.03799v1#A0.F11.sf1 "In Figure 11 ‣ D Consistency and stability checks ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), [11(b)](https://arxiv.org/html/2601.03799v1#A0.F11.sf2 "In Figure 11 ‣ D Consistency and stability checks ‣ Appendix ‣ Optimal execution on Uniswap v2/v3 under transient price impact"), show that the deviation consistently decreases as the grid resolution increases. Moreover, as in the Uniswap v2 setting, accuracy is more sensitive to the resolution of the price grid than to that of the cumulative impact grid. Finally, the computational cost of the high-resolution configuration is significant, requiring approximately 4545 minutes. However, with a coarser grid of Kf=250K\_{f}=250, Kx=250K\_{x}=250, and KI=50K\_{I}=50, the computation time drops to 22 minutes, with a maximum deviation of 0.01050.0105 and a mean deviation of 0.00450.0045.