---
authors:
- Otar Sepper
doc_id: arxiv:2603.09164v1
family_id: arxiv:2603.09164
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Contents
url_abs: http://arxiv.org/abs/2603.09164v1
url_html: https://arxiv.org/html/2603.09164v1
venue: arXiv q-fin
version: 1
year: 2026
---

Title:


Content selection saved. Describe the issue below:

Description:

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.09164v1 [q-fin.RM] 10 Mar 2026

Slippage-at-Risk (SaR):

A Forward-Looking Liquidity Risk Framework
  
for Perpetual Futures Exchanges

Otar Sepper

SepperLabs

Formerly Gauntlet

otar@sepperlabs.com

March 2026

We introduce Slippage-at-Risk (SaR), a quantitative framework for measuring liquidity risk in perpetual futures exchanges. Unlike backward-looking metrics such as Value-at-Risk computed on historical returns or realized deficit distributions, SaR provides a *forward-looking* assessment of liquidation execution risk derived from current order book microstructure. The framework comprises three complementary metrics: SaR​(α)\mathrm{SaR}(\alpha), the cross-sectional slippage quantile; ESaR​(α)\mathrm{ESaR}(\alpha), the expected slippage in the distributional tail; and TSaR​(α)\mathrm{TSaR}(\alpha), the aggregate dollar-denominated tail slippage. We extend the base framework with a *concentration adjustment* that penalizes fragile liquidity structures where a small number of market makers dominate quote provision. Drawing on recent work by Chitra et al. (2025) on autodeleveraging mechanisms and insurance fund optimization, we establish a direct mapping from SaR metrics to optimal capital requirements. Empirical analysis using Hyperliquid order book data, including the October 10, 2025 liquidation cascade, demonstrates SaR’s predictive validity as a leading indicator of systemic stress. We conclude with practical implementation guidance and discuss philosophical implications for risk management in decentralized financial systems.

Keywords: Liquidity risk, perpetual futures, order book microstructure, autodeleveraging, insurance fund, DeFi risk management

## 1 Introduction

### 1.1 Motivation

Perpetual futures have emerged as the dominant derivative instrument in cryptocurrency markets, with daily trading volumes regularly exceeding $100 billion across major venues. Unlike traditional futures contracts with fixed expiration dates, perpetuals use a funding rate mechanism to maintain price alignment with spot markets, enabling indefinite position holding. This innovation has democratized access to leveraged trading, but introduced novel systemic risks that existing frameworks do not adequately address.

The core vulnerability lies in the interaction between leverage, liquidations, and order book liquidity. When a leveraged position’s collateral falls below maintenance requirements, the exchange must liquidate it - selling long positions or buying back short positions at prevailing market prices. During periods of market stress, cascading liquidations can overwhelm available liquidity, resulting in execution prices far worse than theoretical bankruptcy prices. The resulting bad debt - the shortfall between bankruptcy price and actual execution price - must be absorbed by the exchange’s insurance fund or socialized across profitable traders through autodeleveraging (ADL).

The October 10, 2025, Hyperliquid event starkly illustrated these dynamics: $2.1 billion in liquidations over 12 minutes generated $304.5 million in deficits requiring socialization, with the exchange’s queue-based ADL policy expending $704.6 million in haircuts - an 8×\times overutilization relative to the actual deficit [[2](#bib.bib2)]. This event was not a black swan but rather the predictable consequence of thin order books under stress conditions that were, in principle, observable before the cascade began.

### 1.2 The Gap in Existing Approaches

Current risk management frameworks for perpetuals exchanges exhibit several critical limitations:

1. 1.

   Backward-looking metrics: Traditional Value-at-Risk (VaR) and Expected Shortfall (ES) are computed on historical return distributions. They capture past volatility, but they provide no direct measurement of current capacity to absorb liquidations.
2. 2.

   Undefined for new assets: Historical deficit-based metrics cannot be computed for newly listed tokens that have not yet experienced stress events. This creates a dangerous blind spot precisely where risk is highest - illiquid markets with unproven depth.
3. 3.

   Static calibration: Position limits and leverage caps are typically set at the time of listing and adjusted infrequently, failing to adapt to evolving liquidity conditions.
4. 4.

   Ignoring microstructure: The order book - the actual resource that determines execution quality - is rarely incorporated into formal risk metrics.

### 1.3 Contribution and Outline

This paper introduces Slippage-at-Risk (SaR), a framework that directly addresses these limitations by measuring liquidation execution risk from the observable order book state. Our contributions are:

1. 1.

   Core Framework (Section [3](#S3 "3 The Slippage-at-Risk Framework")): We define the slippage function Si​(Q)S\_{i}(Q) and derive three complementary metrics: SaR​(α)\mathrm{SaR}(\alpha), ESaR​(α)\mathrm{ESaR}(\alpha), and TSaR​(α)\mathrm{TSaR}(\alpha). We establish their interpretation as cross-sectional liquidity quantiles and discuss notional calibration.
2. 2.

   Concentration Adjustment (Section [4](#S4 "4 Concentration Adjustment")): We formalize the fragility of concentrated liquidity and derive a haircut formula based on the Herfindahl-Hirschman Index (HHI) that adjusts slippage upward for books dominated by few providers.
3. 3.

   Theoretical Connections (Section [5](#S5 "5 Theoretical Connections")): We establish the causal chain from order book depth to deficit distributions and derive the SaR-implied insurance fund formula, connecting our work to Chitra et al. (2025).
4. 4.

   Extensions (Section [6](#S6 "6 Extensions")): We extend the framework to incorporate cascade effects, time dynamics, cross-token correlation, and spoofing detection.
5. 5.

   Empirical Analysis (Section [7](#S7 "7 Empirical Analysis")): We apply the framework to Hyperliquid order book data, validate SaR’s predictive properties, and analyze the October 10, 2025 event.
6. 6.

   Implementation and Implications (Sections [8](#S8 "8 Implementation Guide")–[9](#S9 "9 Conclusion")): We provide practical guidance for deployment and discuss broader implications for DeFi risk management.

## 2 Preliminaries: Perpetuals Exchange Mechanics

We briefly review the mechanics of perpetual futures exchanges, following the notation of Chitra et al. (2025). Readers familiar with these concepts may proceed to Section [3](#S3 "3 The Slippage-at-Risk Framework").

### 2.1 Positions and Leverage

A position on a perpetuals exchange is a tuple pi=(qi,ci,ti,bi)p\_{i}=(q\_{i},c\_{i},t\_{i},b\_{i}) where:

* •

  qi∈ℝq\_{i}\in\mathbb{R} is the signed quantity (positive for long, negative for short)
* •

  ci>0c\_{i}>0 is the collateral posted
* •

  tit\_{i} is the entry timestamp
* •

  bi∈{−1,+1}b\_{i}\in\{-1,+1\} indicates direction (long/short)

The *leverage* of position ii at time tt is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓi,t=pt⋅|qi|ci,t\ell\_{i,t}=\frac{p\_{t}\cdot|q\_{i}|}{c\_{i,t}} |  | (1) |

where ptp\_{t} is the mark price and ci,tc\_{i,t} is current collateral (initial collateral adjusted for realized PnL and funding payments). Exchanges impose a maximum leverage ℓmax\ell\_{\max}, typically 10-100×\times depending on the asset.

### 2.2 Margin Requirements and Liquidation

Positions are subject to two margin thresholds:

* •

  Initial Margin (IM): Minimum collateral required to open a position, typically IM=1/ℓmax\mathrm{IM}=1/\ell\_{\max} of notional.
* •

  Maintenance Margin (MM): Minimum collateral required to keep a position open, typically MM=μ⋅IM\mathrm{MM}=\mu\cdot\mathrm{IM} for some μ∈(0,1)\mu\in(0,1).

The *equity* of position ii at time tt is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ei,t=ci,t+PnLi,t=ci,t+qi​(pt−pti)e\_{i,t}=c\_{i,t}+\mathrm{PnL}\_{i,t}=c\_{i,t}+q\_{i}(p\_{t}-p\_{t\_{i}}) |  | (2) |

A position is liquidated when equity falls below maintenance margin:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ei,t<MMi⟹liquidation triggerede\_{i,t}<\mathrm{MM}\_{i}\implies\text{liquidation triggered} |  | (3) |

Define the *bankruptcy price* pibkp\_{i}^{\mathrm{bk}} as the price at which equity equals zero:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pibk=pti−ciqi(for longs)p\_{i}^{\mathrm{bk}}=p\_{t\_{i}}-\frac{c\_{i}}{q\_{i}}\quad\text{(for longs)} |  | (4) |

and the *liquidation price* piliqp\_{i}^{\mathrm{liq}} as the price at which equity equals maintenance margin.

### 2.3 Execution and Bad Debt

When liquidating position ii with quantity Δ​qi=−qi\Delta q\_{i}=-q\_{i}, the exchange executes a market order that consumes order book liquidity. The *execution price* piexecp\_{i}^{\mathrm{exec}} depends on available depth. Under a linear market impact model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | piexec=pt−λ2​Δ​qip\_{i}^{\mathrm{exec}}=p\_{t}-\frac{\lambda}{2}\Delta q\_{i} |  | (5) |

where λ>0\lambda>0 is the impact coefficient.

Bad debt arises when execution price is worse than bankruptcy price. For a liquidated position ii, the deficit is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di=max⁡(0,qi⋅(pibk−piexec))D\_{i}=\max\!\Big(0,\;q\_{i}\cdot\big(p\_{i}^{\mathrm{bk}}-p\_{i}^{\mathrm{exec}}\big)\Big) |  | (6) |

That is, Di>0D\_{i}>0 only when the position is closed at a price beyond its bankruptcy level, generating a loss that must be absorbed by the insurance fund.

Total deficit at time TT is DT=∑iDiD\_{T}=\sum\_{i}D\_{i} over all liquidated positions.

### 2.4 Insurance Fund and Autodeleveraging

The insurance fund IFt\mathrm{IF}\_{t} absorbs deficits up to its capacity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IFt+1=IFt+(liquidation fees)+(trading fees)−min⁡{IFt,Dt}\mathrm{IF}\_{t+1}=\mathrm{IF}\_{t}+\text{(liquidation fees)}+\text{(trading fees)}-\min\{\mathrm{IF}\_{t},D\_{t}\} |  | (7) |

When Dt>IFtD\_{t}>\mathrm{IF}\_{t}, the residual Rt=max⁡(0,Dt−IFt)R\_{t}=\max(0,D\_{t}-\mathrm{IF}\_{t}) triggers autodeleveraging: profitable positions are forcibly closed to cover the shortfall. Different ADL policies (Queue, Pro-Rata, Risk-Aware Pro-Rata) allocate haircuts differently across winners, with significant implications for fairness and revenue [[2](#bib.bib2)].

## 3 The Slippage-at-Risk Framework

### 3.1 Setup and Notation

Consider a perpetuals exchange at time tt listing NN tokens indexed by i∈{1,…,N}i\in\{1,\ldots,N\}. For each token ii, we observe:

* •

  pi,tp\_{i,t}: mid-price
* •

  OIi,t\mathrm{OI}\_{i,t}: open interest (total outstanding notional)
* •

  Bi​(⋅)B\_{i}(\cdot): bid-side cumulative depth function
* •

  Ai​(⋅)A\_{i}(\cdot): ask-side cumulative depth function

The order book is represented as a set of limit orders. On the bid side, let {(pkb,qkb)}k=1Kb\{(p\_{k}^{b},q\_{k}^{b})\}\_{k=1}^{K\_{b}} denote price-quantity pairs with p1b>p2b>⋯>pKbbp\_{1}^{b}>p\_{2}^{b}>\cdots>p\_{K\_{b}}^{b}. The cumulative depth at price pp is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bi​(p)=∑k:pkb≥pqkbB\_{i}(p)=\sum\_{k:p\_{k}^{b}\geq p}q\_{k}^{b} |  | (8) |

with analogous definition for the ask side.

### 3.2 The Slippage Function

###### Definition 3.1 (Slippage Function).

For token ii, the *slippage function* Si:ℝ+→ℝ+S\_{i}:\mathbb{R}\_{+}\to\mathbb{R}\_{+} measures the volume-weighted average execution shortfall when liquidating notional quantity QQ:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Si​(Q)=1Q​∫0Q[pmid−p​(q)]​𝑑qS\_{i}(Q)=\frac{1}{Q}\int\_{0}^{Q}\left[p\_{\mathrm{mid}}-p(q)\right]dq |  | (9) |

where p​(q)p(q) is the marginal execution price for the qq-th unit.

For a discrete order book, slippage is computed by walking the book. Algorithm [1](#alg1 "Algorithm 1 ‣ 3.2 The Slippage Function ‣ 3 The Slippage-at-Risk Framework") provides the pseudocode.

Algorithm 1  Compute Slippage from Order Book

order\_book = list of (price, size) sorted best-to-worst

QQ = quantity to liquidate, mid\_price = reference price

Slippage as percentage of mid\_price

remaining←Q\texttt{remaining}\leftarrow Q;    total\_cost←0\texttt{total\\_cost}\leftarrow 0

for each level (price,size)(\texttt{price},\texttt{size}) in order\_book do

fill←min⁡(size,remaining)\texttt{fill}\leftarrow\min(\texttt{size},\texttt{remaining})

total\_cost←total\_cost+fill×(mid\_price−price)\texttt{total\\_cost}\leftarrow\texttt{total\\_cost}+\texttt{fill}\times(\texttt{mid\\_price}-\texttt{price})

remaining←remaining−fill\texttt{remaining}\leftarrow\texttt{remaining}-\texttt{fill}

if remaining=0\texttt{remaining}=0 then exit loop

end if

end for

if remaining>0\texttt{remaining}>0 then return ∞\infty ⊳\triangleright Insufficient liquidity

end if

return total\_cost/(Q×mid\_price)\texttt{total\\_cost}\,/\,(Q\times\texttt{mid\\_price}) ⊳\triangleright As percentage

###### Example 3.2.

Liquidating 100 BTC at mid = $60,000 with total cost of $180,000 gives slippage = 3%.

###### Remark 3.3 (Directional Slippage).

Liquidations are directional: long liquidations sell into bids, short liquidations buy into asks. Define:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sibid​(Q)\displaystyle S\_{i}^{\mathrm{bid}}(Q) | :slippage from selling ​Q​ (long liquidations)\displaystyle:\ \text{slippage from selling }Q\text{ (long liquidations)} |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Siask​(Q)\displaystyle S\_{i}^{\mathrm{ask}}(Q) | :slippage from buying ​Q​ (short liquidations)\displaystyle:\ \text{slippage from buying }Q\text{ (short liquidations)} |  | (11) |

In practice, use the direction matching dominant positioning. If open interest is skewed long, SibidS\_{i}^{\mathrm{bid}} is the relevant measure.

### 3.3 Notional Calibration

The quantity QiQ\_{i} at which to evaluate slippage should reflect a stress liquidation scenario. We parameterize:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qi=min⁡(β⋅OIi,VaR0.95​(Position Sizei))Q\_{i}=\min\left(\beta\cdot\mathrm{OI}\_{i},\,\mathrm{VaR}\_{0.95}(\text{Position Size}\_{i})\right) |  | (12) |

where:

* •

  β∈[0.05,0.20]\beta\in[0.05,0.20] is the *stress parameter*, representing the fraction of open interest that liquidates simultaneously in a stress scenario.
* •

  VaR0.95​(Position Sizei)\mathrm{VaR}\_{0.95}(\text{Position Size}\_{i}) caps QiQ\_{i} at the 95th percentile of historical position sizes, preventing extreme outliers from dominating.

###### Remark 3.4 (Choosing β\beta).

The appropriate stress parameter depends on market conditions:

* •

  Normal conditions: β=0.05\beta=0.05-0.100.10
* •

  Elevated volatility: β=0.10\beta=0.10-0.150.15
* •

  Crisis scenarios: β=0.15\beta=0.15-0.200.20

During the October 10, 2025 Hyperliquid event, realized liquidations represented approximately 15% of pre-event open interest for affected tokens.

### 3.4 Cross-Sectional SaR

###### Definition 3.5 (Slippage-at-Risk).

The *Slippage-at-Risk* at confidence level α∈(0,1)\alpha\in(0,1) is the α\alpha-quantile of slippage across all tokens:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SaR​(α)=inf{s∈ℝ+:1N​∑i=1N𝟏​{Si​(Qi)≤s}≥α}\mathrm{SaR}(\alpha)=\inf\left\{s\in\mathbb{R}\_{+}:\frac{1}{N}\sum\_{i=1}^{N}\mathbf{1}\{S\_{i}(Q\_{i})\leq s\}\geq\alpha\right\} |  | (13) |

Interpretation: SaR​(0.95)=3%\mathrm{SaR}(0.95)=3\% means that 95% of tokens have slippage at or below 3% when liquidating their calibrated stress notional. The remaining 5% are “tail” tokens with critically thin liquidity.

### 3.5 Expected Slippage at Risk (ESaR)

###### Definition 3.6 (Expected Slippage at Risk).

The *Expected Slippage at Risk* is the conditional expected slippage among tail tokens:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESaR​(α)=𝔼​[Si​(Qi)​|Si​(Qi)>​SaR​(α)]\mathrm{ESaR}(\alpha)=\mathbb{E}\left[S\_{i}(Q\_{i})\,\big|\,S\_{i}(Q\_{i})>\mathrm{SaR}(\alpha)\right] |  | (14) |

ESaR\mathrm{ESaR} measures the *severity* of tail liquidity risk, not merely its boundary. It is the slippage analog of Expected Shortfall in the VaR literature.

### 3.6 Total Dollar Slippage at Risk (TSaR)

###### Definition 3.7 (Total Dollar Slippage at Risk).

The *Total Dollar Slippage at Risk* aggregates dollar-denominated slippage from tail tokens:

|  |  |  |  |
| --- | --- | --- | --- |
|  | TSaR$​(α)=∑i:Si​(Qi)>SaR​(α)Si​(Qi)⋅Qi\mathrm{TSaR}\_{\mathdollar}(\alpha)=\sum\_{i:S\_{i}(Q\_{i})>\mathrm{SaR}(\alpha)}S\_{i}(Q\_{i})\cdot Q\_{i} |  | (15) |

TSaR$\mathrm{TSaR}\_{\mathdollar} represents the *total execution shortfall* that would materialize if stress liquidations occurred across all tail tokens simultaneously. This quantity maps directly to potential deficit exposure.

### 3.7 Weighted SaR

The basic SaR\mathrm{SaR} treats all tokens equally. For risk management purposes, weighting by exposure is often more appropriate:

###### Definition 3.8 (Open Interest-Weighted SaR).

|  |  |  |  |
| --- | --- | --- | --- |
|  | SaRw​(α)=inf{s∈ℝ+:∑i:Si​(Qi)≤sOIi∑i=1NOIi≥α}\mathrm{SaR}^{w}(\alpha)=\inf\left\{s\in\mathbb{R}\_{+}:\frac{\sum\_{i:S\_{i}(Q\_{i})\leq s}\mathrm{OI}\_{i}}{\sum\_{i=1}^{N}\mathrm{OI}\_{i}}\geq\alpha\right\} |  | (16) |

SaRw​(0.95)\mathrm{SaR}^{w}(0.95) answers: “What slippage level contains 95% of the open interest (not 95% of tokens)?” This weights toward tokens with larger aggregate positions.

## 4 Concentration Adjustment

### 4.1 The Fragility of Concentrated Liquidity

Raw slippage Si​(Q)S\_{i}(Q) measures depth but ignores its *structure*. Two order books with identical depth profiles can have vastly different fragility:

###### Example 4.1.

Consider two order books, each with $1M total bid-side liquidity:

* •

  Book A (Distributed): 100 market makers, each providing $10,000
* •

  Book B (Concentrated): 2 market makers, each providing $500,000

Both yield S​(Q)=sS(Q)=s for some quantity QQ. However, if one participant withdraws:

* •

  Book A loses 1% of depth
* •

  Book B loses 50% of depth

Book B’s apparent liquidity is fragile - it can vanish suddenly if a dominant provider exits.

This fragility is especially concerning in the context of:

* •

  Spoofing: Artificial liquidity placed to manipulate prices, withdrawn before execution
* •

  Correlated withdrawal: Market makers pulling quotes simultaneously during stress
* •

  Single points of failure: Dominant providers experiencing technical issues or insolvency

### 4.2 Concentration Metrics

For token ii, let MiM\_{i} accounts provide liquidity with quantities ℓ1,…,ℓMi\ell\_{1},\ldots,\ell\_{M\_{i}}. Define shares:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wm=ℓm∑j=1Miℓj,m=1,…,Miw\_{m}=\frac{\ell\_{m}}{\sum\_{j=1}^{M\_{i}}\ell\_{j}},\quad m=1,\ldots,M\_{i} |  | (17) |

###### Definition 4.2 (Herfindahl-Hirschman Index).

|  |  |  |  |
| --- | --- | --- | --- |
|  | HHIi=∑m=1Miwm2\mathrm{HHI}\_{i}=\sum\_{m=1}^{M\_{i}}w\_{m}^{2} |  | (18) |

Properties:

* •

  HHI∈[1/M,1]\mathrm{HHI}\in[1/M,1]
* •

  HHI=1/M\mathrm{HHI}=1/M when liquidity is uniformly distributed
* •

  HHI=1\mathrm{HHI}=1 when a single provider supplies all liquidity (monopoly)

###### Definition 4.3 (Effective Number of Providers).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Neff=1HHIN\_{\mathrm{eff}}=\frac{1}{\mathrm{HHI}} |  | (19) |

NeffN\_{\mathrm{eff}} represents the number of equal-sized providers that would produce the observed concentration. In the example above, Book A has Neff=100N\_{\mathrm{eff}}=100 while Book B has Neff=2N\_{\mathrm{eff}}=2.

###### Definition 4.4 (Top-kk Concentration Ratio).

|  |  |  |  |
| --- | --- | --- | --- |
|  | CRk=∑m=1kw(m)\mathrm{CR}\_{k}=\sum\_{m=1}^{k}w\_{(m)} |  | (20) |

where w(m)w\_{(m)} is the mm-th largest share. CR1\mathrm{CR}\_{1} measures dominance of the single largest provider.

### 4.3 The Concentration Haircut

We now derive a haircut that adjusts slippage upward based on concentration.

#### 4.3.1 Withdrawal Scenario Analysis

Consider the scenario where provider mm withdraws. Let Si(−m)​(Q)S\_{i}^{(-m)}(Q) denote slippage computed on the residual book. The *withdrawal-based haircut* is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hiwithdraw=Si(−1)​(Q)−Si​(Q)Si​(Q)=Si(−1)​(Q)Si​(Q)−1h\_{i}^{\mathrm{withdraw}}=\frac{S\_{i}^{(-1)}(Q)-S\_{i}(Q)}{S\_{i}(Q)}=\frac{S\_{i}^{(-1)}(Q)}{S\_{i}(Q)}-1 |  | (21) |

where (−1)(-1) indicates removal of the largest provider.

#### 4.3.2 Connection Between HHI and Withdrawal Impact

###### Proposition 4.5.

Assume slippage scales inversely with depth: S∝1/LS\propto 1/L where LL is total liquidity. If provider mm is selected uniformly at random to withdraw, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[S(−m)S−1]=𝔼​[wm1−wm]≈HHI1−1/M+O​(HHI2)\mathbb{E}\left[\frac{S^{(-m)}}{S}-1\right]=\mathbb{E}\left[\frac{w\_{m}}{1-w\_{m}}\right]\approx\frac{\mathrm{HHI}}{1-1/M}+O(\mathrm{HHI}^{2}) |  | (22) |

for small concentration.

###### Proof.

After provider mm withdraws, remaining depth is (1−wm)​L(1-w\_{m})L. Under linear slippage:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S(−m)S=L(1−wm)​L=11−wm\frac{S^{(-m)}}{S}=\frac{L}{(1-w\_{m})L}=\frac{1}{1-w\_{m}} |  | (23) |

Thus:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[11−wm−1]=𝔼​[wm1−wm]\mathbb{E}\left[\frac{1}{1-w\_{m}}-1\right]=\mathbb{E}\left[\frac{w\_{m}}{1-w\_{m}}\right] |  | (24) |

For small wmw\_{m}, wm1−wm≈wm+wm2+O​(wm3)\frac{w\_{m}}{1-w\_{m}}\approx w\_{m}+w\_{m}^{2}+O(w\_{m}^{3}). Taking expectation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[wm1−wm]≈𝔼​[wm]+𝔼​[wm2]=1M+HHI\mathbb{E}\left[\frac{w\_{m}}{1-w\_{m}}\right]\approx\mathbb{E}[w\_{m}]+\mathbb{E}[w\_{m}^{2}]=\frac{1}{M}+\mathrm{HHI} |  | (25) |

Rearranging yields the result.
∎

#### 4.3.3 Parametric Haircut Formula

Based on the above analysis, we propose:

###### Definition 4.6 (Concentration Haircut).

|  |  |  |  |
| --- | --- | --- | --- |
|  | hiconc=λ⋅max⁡(0,NtargetNeff(i)−1)+μ⋅max⁡(0,CR1(i)−CR1thresh)h\_{i}^{\mathrm{conc}}=\lambda\cdot\max\!\left(0,\;\frac{N\_{\mathrm{target}}}{N\_{\mathrm{eff}}^{(i)}}-1\right)+\mu\cdot\max\!\left(0,\;\mathrm{CR}\_{1}^{(i)}-\mathrm{CR}\_{1}^{\mathrm{thresh}}\right) |  | (26) |

where:

* •

  NtargetN\_{\mathrm{target}}: target number of effective providers (e.g., 10-20)
* •

  CR1thresh\mathrm{CR}\_{1}^{\mathrm{thresh}}: maximum acceptable share for top provider (e.g., 0.25)
* •

  λ,μ>0\lambda,\mu>0: sensitivity parameters (typically λ=0.5\lambda=0.5, μ=0.3\mu=0.3)

The first term penalizes books with too few effective providers. The second term adds an extra penalty when a single account dominates, which may indicate spoofing.

### 4.4 Concentration-Adjusted Slippage and SaR

###### Definition 4.7 (Adjusted Slippage).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Siadj​(Q)=Si​(Q)⋅(1+hiconc)S\_{i}^{\mathrm{adj}}(Q)=S\_{i}(Q)\cdot\left(1+h\_{i}^{\mathrm{conc}}\right) |  | (27) |

All SaR metrics are then computed using adjusted slippage values:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SaRadj​(α)\displaystyle\mathrm{SaR}^{\mathrm{adj}}(\alpha) | =quantileα​({Siadj​(Qi)}i=1N)\displaystyle=\text{quantile}\_{\alpha}\left(\{S\_{i}^{\mathrm{adj}}(Q\_{i})\}\_{i=1}^{N}\right) |  | (28) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ESaRadj​(α)\displaystyle\mathrm{ESaR}^{\mathrm{adj}}(\alpha) | =𝔼​[Siadj​|Siadj>​SaRadj​(α)]\displaystyle=\mathbb{E}\left[S\_{i}^{\mathrm{adj}}\,|\,S\_{i}^{\mathrm{adj}}>\mathrm{SaR}^{\mathrm{adj}}(\alpha)\right] |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | TSaR$adj​(α)\displaystyle\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}(\alpha) | =∑i:Siadj>SaRadj​(α)Siadj​(Qi)⋅Qi\displaystyle=\sum\_{i:S\_{i}^{\mathrm{adj}}>\mathrm{SaR}^{\mathrm{adj}}(\alpha)}S\_{i}^{\mathrm{adj}}(Q\_{i})\cdot Q\_{i} |  | (30) |

## 5 Theoretical Connections

### 5.1 The Causal Chain: From Order Books to Deficits

Liquidation deficits emerge through a clear causal process:

Liquidity Withdrawal →\;\to\; Thin Order Books →\;\to\; High Slippage →\;\to\; Bad Debt →\;\to\; ADL/Socialization

SaR measures the *upstream* cause (liquidity conditions), while VaR on historical deficits measures the *downstream* consequence. SaR is a *leading indicator* - liquidity withdrawal precedes and predicts cascade events.

### 5.2 Forward-Looking vs. Backward-Looking Metrics

Table 1: Comparison of Risk Metrics

| Metric | Basis | Nature | Information Source | Defined For |
| --- | --- | --- | --- | --- |
| Historical VaR | Returns | Backward | Past price moves | All assets |
| Deficit VaR | Historical deficits | Backward | Past ADL events | Assets with history |
| SaR | Order book depth | Forward | Current MM beliefs | All assets |
| SaR-implied VaR | SaR distribution | Forward | Current liquidity | All assets |

The forward-looking nature of SaR has critical advantages:

1. 1.

   Universally defined: Computable for any token with an order book, regardless of crisis history.
2. 2.

   Encodes market maker beliefs: Order book depth reflects liquidity providers’ assessments of risk.
3. 3.

   Leading indicator: Liquidity withdrawal →\to SaR increases →\to (lag) →\to cascade →\to VaR reacts. SaR flags risk at step 2, potentially days before the event.

### 5.3 Optimal Insurance Fund Sizing

Chitra et al. (2025) derive the optimal insurance fund by minimizing expected total cost:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IF∗=argminIF≥0​{r⋅IF+κ⋅𝔼​[max⁡(0,D−IF)]}\mathrm{IF}^{\*}=\text{argmin}\_{\mathrm{IF}\geq 0}\left\{r\cdot\mathrm{IF}+\kappa\cdot\mathbb{E}[\max(0,D-\mathrm{IF})]\right\} |  | (31) |

where:

* •

  rr: opportunity cost per unit capital held in IF
* •

  κ\kappa: reputation/social cost per unit deficit socialized
* •

  DD: random deficit

###### Theorem 5.1 (Chitra et al. (2025)).

The optimal insurance fund is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IF∗=VaR1−r/κ​(D)\mathrm{IF}^{\*}=\mathrm{VaR}\_{1-r/\kappa}(D) |  | (32) |

i.e., the (1−r/κ)(1-r/\kappa)-quantile of the deficit distribution.

### 5.4 SaR-Implied Insurance Fund

If deficits are driven primarily by slippage during cascades, we can approximate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D≈c⋅TSaR$​(α)D\approx c\cdot\mathrm{TSaR}\_{\mathdollar}(\alpha) |  | (33) |

where c>1c>1 captures the amplification from maintenance margin gaps, fees, and cascade dynamics.

###### Corollary 5.2 (SaR-Implied Insurance Fund).

Under the slippage-driven deficit approximation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IF∗≈c⋅TSaR$adj​(rκ)\mathrm{IF}^{\*}\approx c\cdot\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}\left(\frac{r}{\kappa}\right) |  | (34) |

Interpretation: Size the insurance fund based on current liquidity conditions, not historical deficit data. For newly listed tokens with no crisis history, the SaR-implied IF provides actionable guidance. In typical exchange settings, r/κ≈0.05r/\kappa\approx 0.05 (opportunity cost is much smaller than reputational cost), yielding IF∗≈c⋅TSaR$adj​(0.05)\mathrm{IF}^{\*}\approx c\cdot\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}(0.05).

###### Remark 5.3 (Calibrating cc).

The proportionality constant cc depends on:

* •

  Maintenance margin buffer (larger buffer →\to smaller cc)
* •

  Liquidation fee structure
* •

  Cascade amplification dynamics

Empirically, c∈[1.5,3.0]c\in[1.5,3.0] is typical, with higher values during volatile periods.

## 6 Extensions

### 6.1 Cascade Adjustment

Liquidations trigger feedback loops: price impact from liquidation A pushes other positions toward their liquidation prices, triggering more liquidations. We incorporate this via leverage-weighted slippage:

###### Definition 6.1 (Cascade-Adjusted Slippage).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sicascade​(Q)=Si​(Q)⋅(1+γ⋅ℓ¯i)S\_{i}^{\mathrm{cascade}}(Q)=S\_{i}(Q)\cdot\left(1+\gamma\cdot\bar{\ell}\_{i}\right) |  | (35) |

where ℓ¯i\bar{\ell}\_{i} is the average leverage on positions in token ii, and γ>0\gamma>0 is the cascade sensitivity parameter.

Higher leverage implies more positions near liquidation thresholds, amplifying cascade potential.

### 6.2 Time Dynamics and Regime Detection

Liquidity is non-stationary. Track rolling statistics for regime detection:

###### Definition 6.2 (SaR Time Series Statistics).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SaR-Levelt\displaystyle\text{SaR-Level}\_{t} | =𝔼τ∈[t−T,t]​[SaRτ​(α)]\displaystyle=\mathbb{E}\_{\tau\in[t-T,t]}[\mathrm{SaR}\_{\tau}(\alpha)] |  | (36) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SaR-Dispersiont\displaystyle\text{SaR-Dispersion}\_{t} | =Varτ∈[t−T,t]​[SaRτ​(α)]\displaystyle=\sqrt{\mathrm{Var}\_{\tau\in[t-T,t]}[\mathrm{SaR}\_{\tau}(\alpha)]} |  | (37) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SaR-Volt\displaystyle\text{SaR-Vol}\_{t} | =std​(SaRt−k,…,SaRt)\displaystyle=\text{std}\left(\mathrm{SaR}\_{t-k},\ldots,\mathrm{SaR}\_{t}\right) |  | (38) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SaR-Trendt\displaystyle\text{SaR-Trend}\_{t} | =β^​ from ​SaRτ=a+b​τ+ϵτ\displaystyle=\hat{\beta}\text{ from }\mathrm{SaR}\_{\tau}=a+b\tau+\epsilon\_{\tau} |  | (39) |

Warning signals:

* •

  Rising SaR-Level: Systemic liquidity deterioration
* •

  Widening SaR-Dispersion: Bifurcation between liquid and illiquid tokens
* •

  High SaR-Vol: Unstable liquidity regime - itself a risk factor
* •

  Positive SaR-Trend: Sustained liquidity withdrawal

### 6.3 Cross-Token Correlation

During market stress, liquidations cluster across tokens. For portfolio-level risk:

###### Definition 6.3 (Correlated TSaR).

|  |  |  |  |
| --- | --- | --- | --- |
|  | TSaRport=∑i,jρi​j⋅Slippagei⋅Slippagej\mathrm{TSaR}^{\mathrm{port}}=\sqrt{\sum\_{i,j}\rho\_{ij}\cdot\text{Slippage}\_{i}\cdot\text{Slippage}\_{j}} |  | (40) |

where ρi​j\rho\_{ij} is the correlation of liquidation events between tokens ii and jj.

### 6.4 Spoofing Detection

Beyond concentration, spoofing exhibits specific signatures:

* •

  Quote flickering: High cancel/replace ratio
* •

  Depth retreat: Liquidity pulls away as price approaches
* •

  Asymmetric books: One side much deeper than the other

Define a spoofing risk score:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Spoofi=f​(cancel ratei,retreat ratei,asymmetryi)\text{Spoof}\_{i}=f\left(\text{cancel rate}\_{i},\text{retreat rate}\_{i},\text{asymmetry}\_{i}\right) |  | (41) |

and incorporate into the total haircut:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hitotal=hiconc+δ⋅Spoofih\_{i}^{\mathrm{total}}=h\_{i}^{\mathrm{conc}}+\delta\cdot\text{Spoof}\_{i} |  | (42) |

## 7 Empirical Analysis

### 7.1 Data Description

We analyze order book data from Hyperliquid, a decentralized perpetuals exchange. The dataset comprises:

* •

  Period: October 9 - November 3, 2025 (26 days)
* •

  Tokens: 184 actively traded perpetual contracts
* •

  Order book snapshots: 5-minute frequency, full depth to 2500 bps
* •

  Account-level attribution: Available for concentration metrics via on-chain data
* •

  Open interest: 15-minute snapshots per token
* •

  Liquidation records: Timestamp, size, execution price

Table 2: Summary Statistics: Order Book Data

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Statistic | Mean | Median | Std | Min | Max |
| Tokens per snapshot | 184 | 184 | 0 | 184 | 184 |
| Bid depth at 100bps ($M) | 5.47 | 0.42 | 38.2 | 0.001 | 6,487 |
| Ask depth at 100bps ($M) | 5.31 | 0.39 | 36.8 | 0.001 | 5,892 |
| Total exchange depth ($M) | 974 | 891 | 312 | 284 | 2,847 |
| Open interest per token ($M) | 46.2 | 8.4 | 142.3 | 0.02 | 2,180 |
| Total exchange OI ($B) | 8.51 | 7.91 | 1.84 | 5.42 | 12.31 |
| NeffN\_{\mathrm{eff}} (effective providers) | 8.4 | 5.2 | 9.1 | 1.1 | 47.3 |

The data spans a period of significant market activity, including the October 10, 2025 liquidation cascade which saw total exchange OI decline from $9.8B to $6.1B within hours.

### 7.2 SaR Computation and Characteristics

We compute SaR metrics using β=0.10\beta=0.10 (10% stress scenario) and bid-side depth at 100 basis points. Figure [1](#S7.F1 "Figure 1 ‣ 7.2 SaR Computation and Characteristics ‣ 7 Empirical Analysis") shows the cross-sectional distribution of concentration-adjusted slippage.

![Refer to caption](2603.09164v1/figure1_slippage_distribution.png)


Figure 1: Cross-sectional distribution of concentration-adjusted slippage across 184 tokens. The vertical line indicates SaRadj​(0.95)=3.47%\mathrm{SaR}^{\mathrm{adj}}(0.95)=3.47\%. The 9 tokens to the right (5% tail) exhibit elevated liquidity risk.




Table 3: SaR Metrics Summary (Full Sample Period)

|  |  |  |
| --- | --- | --- |
| Metric | Value | Interpretation |
| SaR​(0.95)\mathrm{SaR}(0.95) | 2.84% | 95% of tokens have slippage ≤\leq 2.84% |
| SaRadj​(0.95)\mathrm{SaR}^{\mathrm{adj}}(0.95) | 3.47% | After concentration adjustment |
| ESaRadj​(0.95)\mathrm{ESaR}^{\mathrm{adj}}(0.95) | 8.92% | Average slippage among tail tokens |
| TSaR$adj​(0.95)\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}(0.95) | $127.4M | Total dollar slippage exposure |
| Tokens in tail | 9 | 5% of 184 tokens |
| Tail OI share | 2.3% | $196M of $8.51B |

![Refer to caption](2603.09164v1/figure2_sar_timeseries.png)


Figure 2: Evolution of SaR and ESaR over the sample period. The spike during October 10-11 corresponds to the liquidation cascade event. Note that SaR began rising 6-12 hours before the cascade peak, demonstrating its leading indicator properties.

### 7.3 Concentration Analysis

We find significant heterogeneity in liquidity concentration across tokens. Major tokens (BTC, ETH, SOL) exhibit distributed liquidity with Neff>20N\_{\mathrm{eff}}>20, while many smaller tokens show concentrated structures vulnerable to withdrawal.

![Refer to caption](2603.09164v1/figure3_concentration_scatter.png)


Figure 3: Relationship between effective number of providers (NeffN\_{\mathrm{eff}}) and raw slippage. Tokens in the lower-left quadrant (low NeffN\_{\mathrm{eff}}, moderate raw slippage) receive the largest concentration haircuts. The horizontal line indicates Ntarget=15N\_{\mathrm{target}}=15.




Table 4: Concentration Statistics by Asset Class

| Asset Class | N Tokens | Mean NeffN\_{\mathrm{eff}} | Mean CR1\mathrm{CR}\_{1} | Mean Haircut |
| --- | --- | --- | --- | --- |
| Major (OI >> $500M) | 5 | 31.2 | 0.08 | 0% |
| Midcap ($50M-$500M) | 23 | 14.7 | 0.16 | 12% |
| Smallcap ($5M-$50M) | 68 | 6.8 | 0.28 | 47% |
| Micro (<< $5M) | 88 | 3.2 | 0.41 | 89% |

The concentration haircut substantially increases adjusted slippage for illiquid tokens: micro-cap tokens see their effective slippage nearly double on average.

### 7.4 Validation: SaR as Leading Indicator

We test whether SaR predicts subsequent deficit events using lead-lag correlation analysis. For each 6-hour window, we compute the correlation between SaR metrics and realized liquidation deficits (total bad debt generated).

Table 5: Lead-Lag Correlation: SaR vs. Realized Deficits

| Lag (hours) | SaR(0.95) | ESaR(0.95) | TSaR$(0.95) |
| --- | --- | --- | --- |
| −24-24 | 0.31 | 0.38 | 0.42 |
| −12-12 | 0.47 | 0.54 | 0.61 |
| −6-6 | 0.58 | 0.67 | 0.73 |
| 0 | 0.72 | 0.79 | 0.84 |
| +6+6 | 0.43 | 0.48 | 0.51 |
| +12+12 | 0.28 | 0.31 | 0.34 |
| +24+24 | 0.19 | 0.22 | 0.24 |

*Note: Correlations are computed over rolling 6-hour windows. Negative lags indicate SaR leading deficits.*

![Refer to caption](2603.09164v1/figure5_leadlag_heatmap.png)


Figure 4: Lead-lag correlation heatmap between SaR metrics and realized deficits. The gradient from left to right shows that SaR metrics lead deficit events by 6-24 hours.

Key findings:

1. 1.

   Peak correlation at lag 0: SaR metrics are most correlated with contemporaneous deficits (as expected, since both reflect current stress).
2. 2.

   Significant predictive power at negative lags: TSaR shows 0.61 correlation with deficits 12 hours in the future and 0.42 correlation at 24 hours. This demonstrates SaR’s value as an early warning system.
3. 3.

   TSaR outperforms: Dollar-denominated TSaR has stronger predictive power than percentage-based SaR, likely because it captures both liquidity thinness and exposure magnitude.
4. 4.

   Asymmetric decay: Correlations decay faster for positive lags than negative lags, confirming that SaR leads rather than lags deficit events.

Granger Causality Test:

We conduct a Granger causality test with 4 lags (24 hours at 6-hour frequency):

| Null Hypothesis | F-statistic | p-value |
| --- | --- | --- |
| TSaR does not Granger-cause Deficits | 8.47 | <0.001<0.001 |
| Deficits does not Granger-cause TSaR | 2.13 | 0.087 |

We find that TSaR Granger-causes deficits (F = 8.47, p << 0.001), while the reverse is not statistically significant. This provides evidence that SaR is a genuine leading indicator, not merely a coincident measure.

### 7.5 Case Study: October 10, 2025

The October 10, 2025 Hyperliquid cascade provides a natural experiment for validating the SaR framework. Between 20:00 and 21:15 UTC, a sharp price decline across major cryptocurrencies triggered cascading liquidations totaling $2.1 billion in notional.

#### 7.5.1 Pre-Event Conditions

Table 6: SaR Metrics: 24 Hours Before October 10 Event

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Metric | Oct 9, 08:00 | Oct 9, 20:00 | Oct 10, 08:00 | Oct 10, 20:00 |
| SaRadj​(0.95)\mathrm{SaR}^{\mathrm{adj}}(0.95) | 2.41% | 2.68% | 3.12% | 11.47% |
| ESaRadj​(0.95)\mathrm{ESaR}^{\mathrm{adj}}(0.95) | 6.82% | 7.54% | 8.91% | 28.34% |
| TSaR$adj​(0.95)\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}(0.95) | $89.2M | $118.7M | $156.3M | $847.2M |
| Tokens in tail | 7 | 9 | 11 | 31 |
| Total exchange depth | $1,124M | $987M | $742M | $284M |

![Refer to caption](2603.09164v1/figure8_depth_collapse.png)


Figure 5: Order book depth collapse during the October 10 cascade. Total exchange depth at 100bps fell from $1.12B to $284M - a 75% decline - in the 36 hours preceding the event.

Key observations:

1. 1.

   Depth deterioration: Total exchange depth at 100bps fell from $1.12B to $284M in the 36 hours preceding the event - a 75% decline. This was visible in real-time.
2. 2.

   SaR escalation: SaRadj​(0.95)\mathrm{SaR}^{\mathrm{adj}}(0.95) rose from 2.41% to 3.12% in the 24 hours before the cascade, a 30% increase that would have triggered alerts under our recommended thresholds.
3. 3.

   Tail expansion: The number of tokens in the liquidity tail grew from 7 to 11, indicating systemic (not idiosyncratic) stress.
4. 4.

   TSaR surge: Dollar-denominated tail exposure grew from $89M to $156M before the event, then spiked to $847M during the cascade as depth collapsed.

#### 7.5.2 Realized vs. Predicted Slippage

We compare pre-event SaR predictions (computed at 08:00 on October 10) with actual realized slippage during the cascade (20:00-21:15).

![Refer to caption](2603.09164v1/figure4_validation_scatter.png)


Figure 6: Scatter plot comparing pre-event adjusted slippage predictions (x-axis) with realized slippage during the October 10 cascade (y-axis). The strong correlation (R2=0.78R^{2}=0.78) validates SaR’s predictive accuracy. The slope >1>1 indicates the model slightly underpredicted realized slippage, consistent with cascade amplification effects.

Regression results:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Realized Slippagei=0.42+1.12×Siadj+ϵi\text{Realized Slippage}\_{i}=0.42+1.12\times S\_{i}^{\mathrm{adj}}+\epsilon\_{i} |  | (43) |

* •

  R2=0.78R^{2}=0.78
* •

  Slope 95% CI: [1.03,1.21][1.03,1.21]
* •

  The positive intercept and slope >1>1 suggest the model is slightly conservative, which is appropriate for risk management.

#### 7.5.3 Insurance Fund Implications

From Chitra et al. (2025), the October 10 event generated $304.5M in deficits. We compute the SaR-implied insurance fund using pre-event data:

Table 7: Insurance Fund Sizing: SaR-Implied vs. Actual

| Metric | Value ($M) | Notes |
| --- | --- | --- |
| Actual Hyperliquid IF (pre-event) | ∼\sim25 | Estimated from public data |
| Realized deficit | 304.5 | From Chitra et al. (2025) |
| SaR-implied IF (c=2.0c=2.0) | 312.6 | Using Oct 10, 08:00 TSaR |
| SaR-implied IF (c=2.5c=2.5) | 390.8 | Conservative estimate |

![Refer to caption](2603.09164v1/figure7_if_comparison.png)


Figure 7: Insurance fund sizing comparison. The SaR-implied IF ($312.6M with c=2.0c=2.0) closely matches the realized deficit ($304.5M), while the actual IF ($25M) was an order of magnitude too small.

Using the formula IF∗=c⋅TSaR$adj​(0.05)\mathrm{IF}^{\*}=c\cdot\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}(0.05) with c=2.0c=2.0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IF∗=2.0×$​156.3​M=$​312.6​M\mathrm{IF}^{\*}=2.0\times\mathdollar 156.3\text{M}=\mathdollar 312.6\text{M} |  | (44) |

This closely matches the realized deficit of $304.5M, validating the SaR-implied insurance fund methodology. The actual IF of ∼\sim$25M was an order of magnitude too small, a gap that was identifiable from SaR metrics hours before the cascade.

#### 7.5.4 Concentration Effects During the Cascade

The October 10 event revealed dramatic concentration effects as market makers withdrew:

Table 8: Concentration Dynamics During October 10 Cascade

| Time (UTC) | Mean NeffN\_{\mathrm{eff}} | Mean CR1\mathrm{CR}\_{1} | Tokens with Neff<3N\_{\mathrm{eff}}<3 |
| --- | --- | --- | --- |
| Oct 10, 18:00 | 8.7 | 0.24 | 42 |
| Oct 10, 20:00 | 5.2 | 0.38 | 89 |
| Oct 10, 21:00 | 2.8 | 0.51 | 134 |
| Oct 10, 22:00 | 4.1 | 0.42 | 97 |
| Oct 11, 00:00 | 6.9 | 0.31 | 61 |

![Refer to caption](2603.09164v1/figure6_concentration_dynamics.png)


Figure 8: Concentration dynamics during the October 10 cascade. Left: Mean NeffN\_{\mathrm{eff}} collapsed from 8.7 to 2.8 at the cascade peak while CR1\mathrm{CR}\_{1} spiked to 0.51. Right: 73% of tokens had critically low concentration (Neff<3N\_{\mathrm{eff}}<3) at peak stress.

At the cascade peak (21:00 UTC), 73% of tokens had Neff<3N\_{\mathrm{eff}}<3, meaning effective liquidity was provided by fewer than 3 participants. This extreme concentration amplified slippage far beyond what raw depth metrics would suggest.

## 8 Implementation Guide

### 8.1 Data Requirements

1. 1.

   Order book snapshots: Full depth profile at regular intervals (minimum 1-minute frequency recommended)
2. 2.

   Account-level attribution: Required for concentration metrics; available on fully on-chain DEXs
3. 3.

   Open interest: Per-token, for notional calibration
4. 4.

   Position distribution: Historical position sizes for VaR-based QQ cap

### 8.2 Computation Pipeline

Algorithm [2](#alg2 "Algorithm 2 ‣ 8.2 Computation Pipeline ‣ 8 Implementation Guide") provides the complete SaR computation pipeline.

Algorithm 2  SaR Computation Pipeline

tokens = list of {order\_book, open\_interest, provider\_shares}

α\alpha = confidence level (e.g., 0.95), β\beta = liquidation fraction (e.g., 0.05)

liquidation\_cap = maximum single liquidation size

SaR​(α)\mathrm{SaR}(\alpha), ESaR​(α)\mathrm{ESaR}(\alpha), TSaR$​(α)\mathrm{TSaR}\_{\mathdollar}(\alpha)

Step 1: Compute concentration-adjusted slippage for each token

for each token ii do

Qi←min⁡(β×OIi,liquidation\_cap)Q\_{i}\leftarrow\min(\beta\times\mathrm{OI}\_{i},\texttt{liquidation\\_cap}) ⊳\triangleright Liquidation quantity

Si←Slippage​(order\_booki,Qi,mid\_pricei)S\_{i}\leftarrow\textsc{Slippage}(\texttt{order\\_book}\_{i},Q\_{i},\texttt{mid\\_price}\_{i}) ⊳\triangleright Raw slippage

HHIi←∑m(sharem)2\mathrm{HHI}\_{i}\leftarrow\sum\_{m}(\texttt{share}\_{m})^{2};    Neff←1/HHIiN\_{\mathrm{eff}}\leftarrow 1/\mathrm{HHI}\_{i};    CR1←maxm⁡(sharem)\mathrm{CR}\_{1}\leftarrow\max\_{m}(\texttt{share}\_{m})

hi←0.5⋅max⁡(0, 15/Neff−1)+0.3⋅max⁡(0,CR1−0.5)h\_{i}\leftarrow 0.5\cdot\max(0,\,15/N\_{\mathrm{eff}}-1)+0.3\cdot\max(0,\,\mathrm{CR}\_{1}-0.5) ⊳\triangleright Haircut

Siadj←Si⋅(1+hi)S\_{i}^{\mathrm{adj}}\leftarrow S\_{i}\cdot(1+h\_{i}) ⊳\triangleright Adjusted slippage

end for

Step 2: Compute portfolio-level risk metrics

Sort {Siadj}\{S\_{i}^{\mathrm{adj}}\} in ascending order

SaR​(α)←S(⌈α​N⌉)adj\mathrm{SaR}(\alpha)\leftarrow S^{\mathrm{adj}}\_{(\lceil\alpha N\rceil)} ⊳\triangleright Slippage at α\alpha-th percentile

tail←{i:Siadj>SaR​(α)}\texttt{tail}\leftarrow\{i:S\_{i}^{\mathrm{adj}}>\mathrm{SaR}(\alpha)\} ⊳\triangleright Tail tokens

ESaR​(α)←1|tail|​∑i∈tailSiadj\mathrm{ESaR}(\alpha)\leftarrow\frac{1}{|\texttt{tail}|}\sum\_{i\in\texttt{tail}}S\_{i}^{\mathrm{adj}} ⊳\triangleright Mean tail slippage

TSaR$​(α)←∑i∈tailSiadj⋅Qi\mathrm{TSaR}\_{\mathdollar}(\alpha)\leftarrow\sum\_{i\in\texttt{tail}}S\_{i}^{\mathrm{adj}}\cdot Q\_{i} ⊳\triangleright Total dollar exposure

return SaR​(α)\mathrm{SaR}(\alpha), ESaR​(α)\mathrm{ESaR}(\alpha), TSaR$​(α)\mathrm{TSaR}\_{\mathdollar}(\alpha)

### 8.3 Parameter Calibration

Table 9: Recommended Parameter Values

| Parameter | Symbol | Recommended | Notes |
| --- | --- | --- | --- |
| Stress fraction | β\beta | 0.10 | Increase to 0.15-0.20 in volatility |
| Confidence level | α\alpha | 0.95 | Standard tail threshold |
| Target providers | NtargetN\_{\mathrm{target}} | 15 | Higher for major tokens |
| Max top share | CR1thresh\mathrm{CR}\_{1}^{\mathrm{thresh}} | 0.25 | Flag potential spoofing |
| Provider sensitivity | λ\lambda | 0.5 | Calibrate to withdrawal events |
| Dominance sensitivity | μ\mu | 0.3 | Calibrate to withdrawal events |
| Deficit multiplier | cc | 2.0-2.5 | Higher during volatility |

### 8.4 Monitoring and Alerts

Table 10: Recommended Alert Thresholds

| Alert Type | Condition | Severity | Action |
| --- | --- | --- | --- |
| SaR Level | SaRadj​(0.95)>3%\mathrm{SaR}^{\mathrm{adj}}(0.95)>3\% | Warning | Review tail tokens |
| SaR Level | SaRadj​(0.95)>5%\mathrm{SaR}^{\mathrm{adj}}(0.95)>5\% | Critical | Reduce leverage limits |
| TSaR Exposure | TSaR$adj​(0.95)>2×IF\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}(0.95)>2\times\mathrm{IF} | Critical | Halt new positions in tail |
| Concentration | Neff<3N\_{\mathrm{eff}}<3 for any token | Warning | Flag for review |
| Concentration | CR1>0.5\mathrm{CR}\_{1}>0.5 for any token | Critical | Investigate spoofing |
| Trend | SaR-Trend positive for 24h | Warning | Prepare contingencies |
| Depth | Exchange depth down >>30% in 12h | Critical | Activate circuit breakers |

## 9 Conclusion

### 9.1 Summary of Contributions

This paper introduced Slippage-at-Risk (SaR), a forward-looking framework for measuring liquidity risk in perpetual futures exchanges. Our key contributions are:

1. 1.

   Novel metrics: SaR​(α)\mathrm{SaR}(\alpha), ESaR​(α)\mathrm{ESaR}(\alpha), and TSaR$​(α)\mathrm{TSaR}\_{\mathdollar}(\alpha) provide complementary views on cross-sectional liquidity risk.
2. 2.

   Concentration adjustment: The HHI-based haircut accounts for the fragility of concentrated liquidity structures.
3. 3.

   Theoretical foundation: We established the causal chain from microstructure to deficits and derived the SaR-implied insurance fund formula.
4. 4.

   Empirical validation: Analysis of Hyperliquid data demonstrates SaR’s predictive validity, including for the October 10, 2025 cascade.

### 9.2 Practical Implications

For exchange operators and risk managers:

* •

  Insurance fund sizing: Use IF∗≈c⋅TSaR$adj​(r/κ)\mathrm{IF}^{\*}\approx c\cdot\mathrm{TSaR}\_{\mathdollar}^{\mathrm{adj}}(r/\kappa) for dynamic, forward-looking capital requirements. Our analysis suggests c≈2.0c\approx 2.0 provides accurate sizing.
* •

  Position limits: Tighten limits on tokens with persistent tail membership or high concentration (Neff<5N\_{\mathrm{eff}}<5).
* •

  New listings: SaR provides risk assessment for tokens with no deficit history - critical for responsible exchange expansion.
* •

  Early warning: Monitor SaR-Trend and depth deterioration for 12-24 hour advance warning of potential cascades.

### 9.3 Philosophical Implications

The SaR framework embodies a broader principle: *measure the cause, not the consequence*. Traditional risk metrics focus on realized outcomes (returns, deficits); SaR focuses on the underlying resource (liquidity) that determines those outcomes. This forward-looking orientation aligns with the ethos of proactive risk management.

In decentralized finance, where code is law and interventions are costly, anticipatory metrics are especially valuable. SaR provides a quantitative basis for the intuition that liquidity is the lifeblood of markets - thin books are not merely inconvenient but systemically risky.

### 9.4 Limitations and Future Work

Several limitations warrant future investigation:

* •

  Data requirements: Account-level attribution is essential for concentration metrics but may not be available on all venues.
* •

  Model assumptions: The slippage-to-deficit proportionality (cc) is empirically calibrated and may vary across market conditions.
* •

  Cross-margin: This paper focuses on isolated margin; extension to cross-margin portfolios requires additional modeling.
* •

  Adversarial manipulation: Sophisticated actors may game SaR by temporarily inflating depth.

## References

* [1]

  Almgren, R. and Chriss, N. (2001).
  Optimal execution of portfolio transactions.
  Journal of Risk, 3:5–40.
* [2]

  Chitra, T., Evans, A., and Angeris, G. (2025).
  Autodeleveraging: Mechanism design and optimizations.
  arXiv preprint arXiv:2512.01112.
* [3]

  Cont, R., Kukanov, A., and Stoikov, S. (2014).
  The price impact of order book events.
  Journal of Financial Econometrics, 12(1):47–88.
* [4]

  Embrechts, P., Klüppelberg, C., and Mikosch, T. (1997).
  Modelling Extremal Events for Insurance and Finance.
  Springer.
* [5]

  Guéant, O., Lehalle, C.-A., and Fernandez-Tapia, J. (2012).
  Optimal portfolio liquidation with limit orders.
  SIAM Journal on Financial Mathematics, 3(1):498–530.
* [6]

  Hasbrouck, J. (2007).
  Empirical Market Microstructure.
  Oxford University Press.
* [7]

  Kyle, A. S. (1985).
  Continuous auctions and insider trading.
  Econometrica, 53(6):1315–1335.
* [8]

  Obizhaeva, A. A. and Wang, J. (2013).
  Optimal trading strategy and supply/demand dynamics.
  Journal of Financial Markets, 16(1):1–32.

## Appendix A Proofs

### A.1 Proof of Proposition [4.5](#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3.2 Connection Between HHI and Withdrawal Impact ‣ 4.3 The Concentration Haircut ‣ 4 Concentration Adjustment") (HHI and Withdrawal Impact)

###### Proof.

Let total depth be L=∑mℓmL=\sum\_{m}\ell\_{m} and shares wm=ℓm/Lw\_{m}=\ell\_{m}/L. Under the linear slippage model, S=k/LS=k/L for some constant kk depending on order quantity.

After provider mm withdraws, remaining depth is L(−m)=L−ℓm=L​(1−wm)L^{(-m)}=L-\ell\_{m}=L(1-w\_{m}). Hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S(−m)=kL​(1−wm)=S1−wmS^{(-m)}=\frac{k}{L(1-w\_{m})}=\frac{S}{1-w\_{m}} |  | (45) |

The relative increase is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S(−m)S−1=11−wm−1=wm1−wm\frac{S^{(-m)}}{S}-1=\frac{1}{1-w\_{m}}-1=\frac{w\_{m}}{1-w\_{m}} |  | (46) |

If provider mm is selected uniformly at random:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[wm1−wm]=1M​∑m=1Mwm1−wm\mathbb{E}\left[\frac{w\_{m}}{1-w\_{m}}\right]=\frac{1}{M}\sum\_{m=1}^{M}\frac{w\_{m}}{1-w\_{m}} |  | (47) |

For small wmw\_{m} (many providers), Taylor expand:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wm1−wm=wm+wm2+wm3+⋯≈wm+wm2\frac{w\_{m}}{1-w\_{m}}=w\_{m}+w\_{m}^{2}+w\_{m}^{3}+\cdots\approx w\_{m}+w\_{m}^{2} |  | (48) |

Taking expectation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[wm1−wm]\displaystyle\mathbb{E}\left[\frac{w\_{m}}{1-w\_{m}}\right] | ≈𝔼​[wm]+𝔼​[wm2]\displaystyle\approx\mathbb{E}[w\_{m}]+\mathbb{E}[w\_{m}^{2}] |  | (49) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1M​∑mwm+1M​∑mwm2\displaystyle=\frac{1}{M}\sum\_{m}w\_{m}+\frac{1}{M}\sum\_{m}w\_{m}^{2} |  | (50) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1M⋅1+1M⋅M⋅HHI\displaystyle=\frac{1}{M}\cdot 1+\frac{1}{M}\cdot M\cdot\mathrm{HHI} |  | (51) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1M+HHI\displaystyle=\frac{1}{M}+\mathrm{HHI} |  | (52) |

For large MM, 1/M≈01/M\approx 0, and:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[S(−m)S−1]≈HHI+O​(HHI2)\mathbb{E}\left[\frac{S^{(-m)}}{S}-1\right]\approx\mathrm{HHI}+O(\mathrm{HHI}^{2}) |  | (53) |

Rearranging gives the stated result.
∎

## Appendix B Additional Empirical Results

### B.1 Full Token-Level Results

Table 11: Token-Level SaR Metrics (Top 20 by OI)

| Token | OI ($M) | Q ($M) | S​(Q)S(Q) | NeffN\_{\mathrm{eff}} | CR1\mathrm{CR}\_{1} | Haircut | SadjS^{\mathrm{adj}} |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 2,180 | 218.0 | 0.42% | 47.3 | 0.05 | 0% | 0.42% |
| ETH | 1,847 | 184.7 | 0.51% | 38.6 | 0.06 | 0% | 0.51% |
| SOL | 892 | 89.2 | 0.78% | 29.4 | 0.08 | 0% | 0.78% |
| HYPE | 634 | 63.4 | 1.24% | 12.8 | 0.14 | 8% | 1.34% |
| XRP | 412 | 41.2 | 0.93% | 18.2 | 0.11 | 0% | 0.93% |
| DOGE | 287 | 28.7 | 1.47% | 11.4 | 0.18 | 16% | 1.70% |
| AVAX | 198 | 19.8 | 1.82% | 8.7 | 0.21 | 36% | 2.48% |
| LINK | 176 | 17.6 | 1.63% | 9.2 | 0.19 | 32% | 2.15% |
| ARB | 142 | 14.2 | 2.14% | 7.1 | 0.24 | 56% | 3.34% |
| OP | 128 | 12.8 | 2.38% | 6.4 | 0.26 | 68% | 4.00% |
| SUI | 118 | 11.8 | 2.67% | 5.8 | 0.28 | 79% | 4.78% |
| APT | 96 | 9.6 | 2.91% | 5.2 | 0.31 | 94% | 5.65% |
| INJ | 84 | 8.4 | 3.24% | 4.7 | 0.33 | 110% | 6.80% |
| TIA | 72 | 7.2 | 3.58% | 4.2 | 0.36 | 129% | 8.20% |
| SEI | 61 | 6.1 | 3.92% | 3.8 | 0.39 | 147% | 9.68% |
| RNDR | 54 | 5.4 | 4.31% | 3.4 | 0.42 | 168% | 11.55% |
| FET | 47 | 4.7 | 4.78% | 3.1 | 0.45 | 192% | 13.96% |
| NEAR | 42 | 4.2 | 5.12% | 2.8 | 0.47 | 214% | 16.08% |
| STX | 38 | 3.8 | 5.67% | 2.5 | 0.51 | 250% | 19.85% |
| WIF | 34 | 3.4 | 6.24% | 2.2 | 0.54 | 291% | 24.38% |

*Note: Data represents average values over the sample period. Haircuts computed with Ntarget=15N\_{\mathrm{target}}=15, CR1thresh=0.25\mathrm{CR}\_{1}^{\mathrm{thresh}}=0.25, λ=0.5\lambda=0.5, μ=0.3\mu=0.3.*

## Appendix C Symbol Reference

Table 12: Symbol Reference

| Symbol | Description |
| --- | --- |
| Si​(Q)S\_{i}(Q) | Slippage function for token ii at quantity QQ |
| SaR​(α)\mathrm{SaR}(\alpha) | α\alpha-quantile of slippage across all tokens |
| ESaR​(α)\mathrm{ESaR}(\alpha) | Expected slippage conditional on exceeding SaR​(α)\mathrm{SaR}(\alpha) |
| TSaR$​(α)\mathrm{TSaR}\_{\mathdollar}(\alpha) | Total dollar slippage from tail tokens |
| HHI\mathrm{HHI} | Herfindahl-Hirschman Index (concentration measure) |
| NeffN\_{\mathrm{eff}} | Effective number of liquidity providers (=1/HHI=1/\mathrm{HHI}) |
| CRk\mathrm{CR}\_{k} | Top-kk concentration ratio |
| hiconch\_{i}^{\mathrm{conc}} | Concentration haircut for token ii |
| SiadjS\_{i}^{\mathrm{adj}} | Concentration-adjusted slippage |
| α\alpha | Confidence level for SaR computation |
| β\beta | Stress parameter (fraction of OI in stress scenario) |
| λ\lambda | Provider concentration sensitivity (haircut parameter) |
| μ\mu | Dominance sensitivity (haircut parameter) |
| QiQ\_{i} | Stress notional for token ii |
| OIi\mathrm{OI}\_{i} | Open interest for token ii |
| IF∗\mathrm{IF}^{\*} | Optimal insurance fund size |
| rr | Opportunity cost per unit capital |
| κ\kappa | Reputation/social cost per unit deficit |
| cc | Slippage-to-deficit proportionality constant |
| DTD\_{T} | Total deficit at time TT |
| RTR\_{T} | Residual deficit after IF depletion |
| ℓi,t\ell\_{i,t} | Leverage of position ii at time tt |
| pibkp\_{i}^{\mathrm{bk}} | Bankruptcy price for position ii |
| piliqp\_{i}^{\mathrm{liq}} | Liquidation price for position ii |
| piexecp\_{i}^{\mathrm{exec}} | Execution price for position ii |

BETA