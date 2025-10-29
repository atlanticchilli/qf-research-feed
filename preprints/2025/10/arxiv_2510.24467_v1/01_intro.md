---
authors:
- Stanisław M. S. Halkiewicz
doc_id: arxiv:2510.24467v1
family_id: arxiv:2510.24467
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe
  author has not received any funding
url_abs: http://arxiv.org/abs/2510.24467v1
url_html: https://arxiv.org/html/2510.24467v1
venue: arXiv q-fin
version: 1
year: 2025
---


Stanisław M. S. Halkiewicz
Department of Applied Mathematics, AGH University of Cracow, Kraków, Poland
().

###### Abstract

We formalize the paradox of an *omniscient yet lazy investor*—a perfectly informed agent
who trades infrequently due to execution or computational frictions.
Starting from a deterministic geometric construction, we derive a closed-form expected profit function linking trading frequency, execution cost, and path roughness.
We prove existence and uniqueness of the optimal trading frequency and show that this
optimum can be interpreted through the fractal dimension of the price path.
A stochastic extension under fractional Brownian motion provides analytical expressions
for the optimal interval and comparative statics with respect to the Hurst exponent.
Empirical illustrations on equity data confirm the theoretical scaling behavior.

###### keywords:

trading frequency, execution costs, fractal markets, fractional Brownian motion,
optimization, algorithmic trading

{AMS}

91G80, 60G22, 62P05, 91B84, 90C26, 91B70

## 1 Introduction

Modern financial markets operate under a tension between the speed of information
and the frictions of execution [[38](https://arxiv.org/html/2510.24467v1#bib.bib38), [2](https://arxiv.org/html/2510.24467v1#bib.bib2), [48](https://arxiv.org/html/2510.24467v1#bib.bib48)].
Algorithmic traders, institutional portfolio managers, and even theoretical
agents must continually decide not only *what* to trade but also
*how frequently* to act.
In principle, an investor endowed with perfect foresight could exploit every
profitable fluctuation of an asset’s price path;
in practice, each decision carries tangible costs — transaction fees,
market impact, computational latency, and cognitive or regulatory frictions
[[12](https://arxiv.org/html/2510.24467v1#bib.bib12), [51](https://arxiv.org/html/2510.24467v1#bib.bib51), [26](https://arxiv.org/html/2510.24467v1#bib.bib26)].
The result is an optimization problem that balances
omniscience with inertia: the investor knows everything, yet cannot act continuously.

This paper formalizes that paradox through the stylized construct of
the *omniscient yet lazy investor*.
The model postulates an agent with complete knowledge of the future price path,
subject to additive execution costs and a cumulative penalty
for the mere act of trading or recalculating — a “laziness cost” representing
bounded rationality, algorithmic latency, or decision fatigue
[[11](https://arxiv.org/html/2510.24467v1#bib.bib11), [24](https://arxiv.org/html/2510.24467v1#bib.bib24), [12](https://arxiv.org/html/2510.24467v1#bib.bib12)].
The investor’s problem is to determine the number of trades (or, equivalently,
the trading frequency) that maximizes expected total profit over a finite horizon.

Starting from a deterministic geometric setting, we derive a closed-form
expression for the investor’s expected profit as a function of the number of
trading intervals, the per-trade friction, and a parameter describing
the roughness of the price path.
This formulation extends the classical portfolio-rebalancing literature on
transaction costs [[42](https://arxiv.org/html/2510.24467v1#bib.bib42), [18](https://arxiv.org/html/2510.24467v1#bib.bib18), [50](https://arxiv.org/html/2510.24467v1#bib.bib50), [36](https://arxiv.org/html/2510.24467v1#bib.bib36)],
interpreting frequency choice as a discrete control variable rather than
a boundary condition on wealth.
The resulting trade-off is intuitive: increasing trading frequency
magnifies exploitable price variation but also raises costs,
and the total profit eventually decreases, producing a finite optimum.

A key insight of the model is its connection to fractal geometry.
By relating the effective length of the price path to its scaling exponent,
we interpret the optimal frequency through the *fractal dimension*
of the underlying trajectory.
This view builds on the Fractal Market Hypothesis, originally proposed by Peters [[49](https://arxiv.org/html/2510.24467v1#bib.bib49)],
which attributes market stability to the coexistence of heterogeneous investment horizons.
Empirical studies have shown that financial time series exhibit
self-similarity and scale-invariant roughness [[43](https://arxiv.org/html/2510.24467v1#bib.bib43), [37](https://arxiv.org/html/2510.24467v1#bib.bib37), [39](https://arxiv.org/html/2510.24467v1#bib.bib39)],
motivating the explicit use of fractal measures in our analysis.
In this interpretation, rougher (more irregular) price paths correspond to
higher optimal trading frequencies.

To ground the model in a stochastic environment, we extend the framework to
price dynamics driven by fractional Brownian motion (fBM) with Hurst exponent
H∈(0,1)H\in(0,1) [[45](https://arxiv.org/html/2510.24467v1#bib.bib45), [7](https://arxiv.org/html/2510.24467v1#bib.bib7), [47](https://arxiv.org/html/2510.24467v1#bib.bib47)].
Under the self-similarity property of fBM,
the expected exploitable price increment scales as ΔH\Delta^{H},
and the deterministic profit formula generalizes naturally to a stochastic one.
We obtain explicit expressions for the optimal rebalancing interval
Δ⋆=[s¯/(κ​(1−H))]1/H\Delta^{\star}=[\,\bar{s}/(\kappa(1-H))\,]^{1/H},
where s¯\bar{s} denotes the effective execution friction
and κ\kappa is a scaling constant determined by volatility and normalization.
This result confirms the theoretical intuition: as the path becomes more fractal
(smaller HH), the investor should act more frequently
[[33](https://arxiv.org/html/2510.24467v1#bib.bib33), [6](https://arxiv.org/html/2510.24467v1#bib.bib6), [25](https://arxiv.org/html/2510.24467v1#bib.bib25)].

Numerical and empirical examples illustrate the analytical results.
Using equity data, we show that the observed profit function follows
the predicted concave shape, and the empirically optimal frequency
lies close to the theoretical one derived under the fBM approximation
[[4](https://arxiv.org/html/2510.24467v1#bib.bib4), [23](https://arxiv.org/html/2510.24467v1#bib.bib23), [54](https://arxiv.org/html/2510.24467v1#bib.bib54), [1](https://arxiv.org/html/2510.24467v1#bib.bib1)].
The analysis thus connects geometric properties of price paths with
economically meaningful decisions about trading intensity,
in the spirit of the fractal interpretation of market behavior
[[49](https://arxiv.org/html/2510.24467v1#bib.bib49), [31](https://arxiv.org/html/2510.24467v1#bib.bib31), [52](https://arxiv.org/html/2510.24467v1#bib.bib52), [46](https://arxiv.org/html/2510.24467v1#bib.bib46)].

The rest of the paper is organized as follows.
In section [2](https://arxiv.org/html/2510.24467v1#S2 "2 Literature Review ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") we review the literature concerning fractal structure of capital markets and place our model within the existing frameworks.
Section [3](https://arxiv.org/html/2510.24467v1#S3 "3 Model Framework ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") introduces the model framework and notation.
Section [4](https://arxiv.org/html/2510.24467v1#S4 "4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") derives the deterministic closed-form profit formula.
Section [5](https://arxiv.org/html/2510.24467v1#S5 "5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") studies the existence and properties of the
optimal trading frequency.
Section [6](https://arxiv.org/html/2510.24467v1#S6 "6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") develops the stochastic extension based on
fractional Brownian motion and provides comparative statics.
Section [7](https://arxiv.org/html/2510.24467v1#S7 "7 Empirical and Simulation Evidence ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") presents empirical and simulation evidence and Section [8](https://arxiv.org/html/2510.24467v1#S8 "8 Conclusions ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") discusses implications for algorithmic trading, concludes and suggests pathways for future research.

## 2 Literature Review

The present study builds upon two mature yet historically separate research traditions in mathematical finance:
(1) the optimization of portfolio rebalancing under proportional transaction costs, and
(2) the fractal modeling of market dynamics, including the Fractal Market Hypothesis (FMH).
Bridging these frameworks provides a geometric and stochastic interpretation of trading frequency as an endogenous response to both frictions and price‐path roughness.

### 2.1 Portfolio Optimization under Transaction Costs

The study of optimal portfolio rebalancing in frictional markets originates from the seminal works of Davis and Norman [[18](https://arxiv.org/html/2510.24467v1#bib.bib18)] and Shreve and Soner [[50](https://arxiv.org/html/2510.24467v1#bib.bib50)].
Their continuous‐time impulse‐control formulations established the existence of *no‐trade regions*—intervals of inaction within which the marginal cost of trading exceeds the marginal benefit of rebalancing.
These models formalized the balance between maintaining target allocations and minimizing cumulative transaction costs, and they provided a mathematical basis for the design of modern trading and execution strategies.
Subsequent research, including Korn [[36](https://arxiv.org/html/2510.24467v1#bib.bib36)], extended the analysis to stochastic volatility, portfolio insurance, and partial‐information settings, integrating dynamic programming and viscosity‐solution techniques.
This literature underpins the first strand of the present work: trading frequency as an optimization variable constrained by proportional and cognitive frictions.

#### Fractal geometry and market structure.

Fractal geometry was introduced to financial analysis by Mandelbrot [[44](https://arxiv.org/html/2510.24467v1#bib.bib44)],
whose pioneering studies on scaling laws in price series and heavy‐tailed distributions
challenged the Gaussian assumptions of the Efficient Market Hypothesis (EMH).
Building on these ideas, Peters [[49](https://arxiv.org/html/2510.24467v1#bib.bib49)] proposed the Fractal Market Hypothesis (FMH), arguing that market stability depends on a heterogeneous spectrum of investment horizons,
with financial crises corresponding to periods dominated by short‐term trading behavior.
FMH emphasises self-similarity, roughness, and scale invariance in market dynamics rather than perfect informational efficiency.

### 2.2 Fractional Processes and Rough Volatility

A rigorous stochastic foundation for fractal scaling was established by Mandelbrot and van Ness [[45](https://arxiv.org/html/2510.24467v1#bib.bib45)], who defined fractional Brownian motion (fBM) and fractional noise as models with self‐similar increments and memory parameterized by the Hurst exponent H∈(0,1)H\in(0,1).
The Hurst exponent determines both the persistence of increments and the Hausdorff (fractal) dimension D=2−HD=2-H of the sample path.
Applications of fBM to asset prices and volatility were advanced by Comte and Renault [[14](https://arxiv.org/html/2510.24467v1#bib.bib14)], Wyss [[56](https://arxiv.org/html/2510.24467v1#bib.bib56)] (after Kim et al. [[35](https://arxiv.org/html/2510.24467v1#bib.bib35)] and Zhang et al. [[57](https://arxiv.org/html/2510.24467v1#bib.bib57)]), and Gatheral, Jaisson, and Rosenbaum [[27](https://arxiv.org/html/2510.24467v1#bib.bib27)], the latter providing strong empirical evidence that volatility is rough, with typical HH near 0.1.
This line of work firmly connected fractal geometry with stochastic modeling, showing that memory and roughness jointly govern volatility clustering and scaling behavior.

### 2.3 Modern Developments in Fractal Financial Modeling

Recent research has revitalized fractal approaches using both empirical and analytical tools.
Wu et al. [[55](https://arxiv.org/html/2510.24467v1#bib.bib55)] introduced *fractal statistical measures*—fractal expectation and variance—to construct portfolio selection models under power‐law tails, yielding closed‐form weights that outperform traditional mean–variance optimization.
Kakinaka et al. [[33](https://arxiv.org/html/2510.24467v1#bib.bib33)] studied *fractal portfolio strategies* in which investor preferences over temporal scales influence performance and risk.
El‐Nabulsi and Anukool [[21](https://arxiv.org/html/2510.24467v1#bib.bib21)] extended this perspective to markets defined in fractional dimensions, deriving qualitative properties of asset dynamics within noninteger geometric spaces.

Parallel advances in measurement techniques have enhanced empirical precision.
Bayraktar, Poor, and Sircar [[4](https://arxiv.org/html/2510.24467v1#bib.bib4)] estimated the fractal dimension of the S&P 500 index via wavelet analysis, linking declining Hurst exponents to increasing market efficiency.
Verma and Kumar [[54](https://arxiv.org/html/2510.24467v1#bib.bib54)] analyzed post–merger financial performance using fractal interpolation and box dimension metrics,
while Alizade et al. [[1](https://arxiv.org/html/2510.24467v1#bib.bib1)] modeled market turbulence through Laplace–Mittag–Leffler distributions, capturing heavy tails and memory effects beyond classical Lévy frameworks.
The mathematical foundations of fractal dimension estimation in applied finance are comprehensively presented by Fernández–Martínez et al. [[23](https://arxiv.org/html/2510.24467v1#bib.bib23)], whose work consolidates analytical and numerical techniques for quantifying complexity in time‐series data. Halkiewicz [[31](https://arxiv.org/html/2510.24467v1#bib.bib31)] provided a conceptual synthesis of market graphs as fractals.
This interpretation aligns with the FMH and emphasizes that the complexity of market dynamics increases as the observation interval shortens—a principle central to the present paper’s formulation of frequency‐dependent profitability.

### 2.4 Positioning of the Present Study

The contribution of this work is to unify the frictional and fractal paradigms within a single analytical framework.
While classical transaction‐cost models quantify the cost–benefit trade‐off of frequent trading, and fractal market models describe the geometry of price fluctuations, the two are rarely connected formally.
Our model links them by interpreting the investor’s optimal trading frequency as a function of the fractal dimension (or equivalently, the Hurst exponent) of the underlying price path.
This geometric–economic synthesis provides a closed‐form solution to the “omniscient yet lazy investor” problem and delivers a quantitative manifestation of the Fractal Market Hypothesis:
as the market becomes rougher and more fractal, optimal trading frequency increases, reflecting the higher information content per unit time.

## 3 Model Framework

We consider an *omniscient investor*.
Apart from knowing the answers to all metaphysical questions about the universe and everything in it,
he naturally possesses perfect foresight regarding future price movements as well.
He is also incurably greedy:

* •

  having already solved the Millennium Problems,
* •

  discovered every lost treasure,
* •

  and won so many games of poker that every casino in Las Vegas has him blacklisted,

he still desires more and more money. Determined to turn his omniscience into yet another source of amusement and wealth, he decides to participate in the financial markets.

Unfortunately, omniscience does not preclude indolence.
Our investor is also profoundly lazy. Each trade, however trivial in its consequence, requires effort, attention, and perhaps the faint movement of a finger—actions he finds increasingly tiresome.
He faces proportional execution frictions whenever he deigns to act, and cumulative decision-making costs whenever he considers doing so.
Such frictions are pervasive in both theoretical and empirical market models [[42](https://arxiv.org/html/2510.24467v1#bib.bib42), [18](https://arxiv.org/html/2510.24467v1#bib.bib18), [50](https://arxiv.org/html/2510.24467v1#bib.bib50), [34](https://arxiv.org/html/2510.24467v1#bib.bib34)].
His problem, therefore, is quintessentially human despite his divine insight:
given total knowledge and total apathy, how often should he trade within a fixed horizon in order to maximize his expected profit?

### 3.1 Discrete trading grid

Let T>0T>0 denote the total investment horizon.
We partition [0,T][0,T] into nn subintervals of equal length
Δ=T/n\Delta=T/n, corresponding to n=2mn=2^{m} trading periods indexed by
i=0,1,…,ni=0,1,\dots,n.
Denote by cic\_{i} the asset price at time ti=i​Δt\_{i}=i\Delta.
The increment between successive observation points is

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | Δ​ci=ci+1−ci.\Delta c\_{i}=c\_{i+1}-c\_{i}. |  |

Such discrete rebalancing grids are standard in the literature on optimal portfolio revision and dynamic trading [[42](https://arxiv.org/html/2510.24467v1#bib.bib42), [36](https://arxiv.org/html/2510.24467v1#bib.bib36), [12](https://arxiv.org/html/2510.24467v1#bib.bib12)].

Because the investor is *omniscient*, each Δ​ci\Delta c\_{i} is known in advance.
However, the investor incurs two forms of friction when acting on this knowledge:

1. 1.

   a per‐trade execution cost or spread s¯≥0\bar{s}\geq 0,
2. 2.

   an additive “laziness cost” li≥0l\_{i}\geq 0 representing
   the cognitive, computational, or opportunity cost
   of taking a decision at time tit\_{i}.

The first term represents proportional costs studied in transaction‐cost models such as those of Davis and Norman or Shreve and Soner [[18](https://arxiv.org/html/2510.24467v1#bib.bib18), [50](https://arxiv.org/html/2510.24467v1#bib.bib50)],
while the second reflects decision‐making or latency penalties
that parallel the cognitive constraints emphasized in rational‐inattention theory [[51](https://arxiv.org/html/2510.24467v1#bib.bib51), [26](https://arxiv.org/html/2510.24467v1#bib.bib26), [11](https://arxiv.org/html/2510.24467v1#bib.bib11)].
The total laziness cost accumulated over the horizon is denoted

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | L=∑i=1nli.L=\sum\_{i=1}^{n}l\_{i}. |  |

This cumulative term generalizes beyond monetary costs, encompassing computational energy expenditure or machine‐learning inference delays in automated systems [[12](https://arxiv.org/html/2510.24467v1#bib.bib12)].

### 3.2 Profit identity

For an omniscient trader who always takes the correct side of the market,
the gross gain over period ii equals the absolute price change
|Δ​ci||\Delta c\_{i}|.
After subtracting costs, the realized profit over all periods is

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | R=∑i=1n(|Δ​ci|−s¯−li).R=\sum\_{i=1}^{n}\big(|\Delta c\_{i}|-\bar{s}-l\_{i}\big). |  |

Defining the mean exploitable return per trade as
r¯=1n​∑i=1n|Δ​ci|,\bar{r}=\tfrac{1}{n}\sum\_{i=1}^{n}|\Delta c\_{i}|,
we can rewrite ([3](https://arxiv.org/html/2510.24467v1#S3.E3 "Equation 3 ‣ 3.2 Profit identity ‣ 3 Model Framework ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) as

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | R=n​(r¯−s¯)−L.R=n(\bar{r}-\bar{s})-L. |  |

Expression ([4](https://arxiv.org/html/2510.24467v1#S3.E4 "Equation 4 ‣ 3.2 Profit identity ‣ 3 Model Framework ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) provides the fundamental relationship
between trading frequency and total profit.
As the number of trades nn increases, the exploitable mean return
r¯\bar{r} typically rises because smaller intervals reveal additional
micro‐movements of the price path, a phenomenon consistent with the
scaling laws documented in high‐frequency data [[8](https://arxiv.org/html/2510.24467v1#bib.bib8), [16](https://arxiv.org/html/2510.24467v1#bib.bib16), [10](https://arxiv.org/html/2510.24467v1#bib.bib10)].
At the same time, both the proportional cost s¯\bar{s} and the total laziness cost LL
reduce net profitability, in line with the classic execution–latency trade‐off in optimal trading theory [[2](https://arxiv.org/html/2510.24467v1#bib.bib2), [48](https://arxiv.org/html/2510.24467v1#bib.bib48), [38](https://arxiv.org/html/2510.24467v1#bib.bib38)].

### 3.3 Decision variable and optimization problem

The investor chooses the number of trading intervals nn, or equivalently
the dyadic level mm such that n=2mn=2^{m}, to maximize RR:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | maxm∈ℕ⁡Rm:=2m​(r¯m−s¯)−Lm.\max\_{m\in\mathbb{N}}\;R\_{m}:=2^{m}(\bar{r}\_{m}-\bar{s})-L\_{m}. |  |

Here r¯m\bar{r}\_{m} and LmL\_{m} denote, respectively, the average exploitable
return per trade and the cumulative laziness cost when the price path
is observed at resolution mm.
The trade‐off mirrors impulse‐control models in which agents balance
costly rebalancing with expected drift [[15](https://arxiv.org/html/2510.24467v1#bib.bib15), [53](https://arxiv.org/html/2510.24467v1#bib.bib53), [34](https://arxiv.org/html/2510.24467v1#bib.bib34)],
but the present setting replaces the stochastic control boundary
with a discrete frequency variable capturing self-similar resolution.

### 3.4 Interpretation of costs

The term s¯\bar{s} encompasses all proportional costs that scale
linearly with the number of trades,
including bid–ask spreads, slippage, and market‐impact fees [[2](https://arxiv.org/html/2510.24467v1#bib.bib2), [12](https://arxiv.org/html/2510.24467v1#bib.bib12), [48](https://arxiv.org/html/2510.24467v1#bib.bib48)].
The term LmL\_{m} represents non‐linear or sublinear costs of action:
for example, human cognitive effort [[24](https://arxiv.org/html/2510.24467v1#bib.bib24)],
machine‐learning inference latency [[12](https://arxiv.org/html/2510.24467v1#bib.bib12)],
or computational resource usage.
Allowing LmL\_{m} to grow with mm captures the intuitive idea that higher
trading frequency requires disproportionately greater informational and
technological capacity [[26](https://arxiv.org/html/2510.24467v1#bib.bib26), [51](https://arxiv.org/html/2510.24467v1#bib.bib51)].
Such latency–dependent frictions have been studied extensively in HFT models,
where execution speed, information flow, and order–book resilience jointly determine profitability
[[13](https://arxiv.org/html/2510.24467v1#bib.bib13), [32](https://arxiv.org/html/2510.24467v1#bib.bib32)].

### 3.5 Fractal scaling motivation

Empirically, as the sampling interval Δ\Delta decreases,
the measured variation of a financial price series increases
in a manner reminiscent of fractal scaling [[43](https://arxiv.org/html/2510.24467v1#bib.bib43), [44](https://arxiv.org/html/2510.24467v1#bib.bib44), [10](https://arxiv.org/html/2510.24467v1#bib.bib10)].
This observation motivates modeling r¯m\bar{r}\_{m}
as a function of the effective *roughness* of the price path,
a property long noted in the context of fractal market geometry [[49](https://arxiv.org/html/2510.24467v1#bib.bib49), [28](https://arxiv.org/html/2510.24467v1#bib.bib28)].
In Section [4](https://arxiv.org/html/2510.24467v1#S4 "4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") we formalize this dependence and derive a closed‐form expression for RmR\_{m}
based on a geometric construction involving a scaling parameter WW
that quantifies the fractal complexity of the trajectory [[22](https://arxiv.org/html/2510.24467v1#bib.bib22), [41](https://arxiv.org/html/2510.24467v1#bib.bib41)].

## 4 Deterministic Fractal Derivation

This section provides a geometric scaling argument that links the exploitable
per–trade move to the sampling resolution and a roughness parameter.
Combined with ([4](https://arxiv.org/html/2510.24467v1#S3.E4 "Equation 4 ‣ 3.2 Profit identity ‣ 3 Model Framework ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")), it yields a closed-form expression for
RmR\_{m} as a function of the dyadic level mm.

### 4.1 Triangle construction and scaling postulate

The idea that apparent path length depends on observation scale is central in
fractal geometry [[43](https://arxiv.org/html/2510.24467v1#bib.bib43), [22](https://arxiv.org/html/2510.24467v1#bib.bib22)].
We apply it here in the simplest possible way.

Fix the horizon T>0T>0 and a dyadic resolution m∈ℕm\in\mathbb{N} with
n=2mn=2^{m} subintervals and step Δ=T/2m\Delta=T/2^{m}.
Over one subinterval [ti,ti+1][t\_{i},t\_{i+1}], we represent the effective local
displacement by a right triangle with horizontal leg Δ\Delta, vertical leg
h¯m≥0\bar{h}\_{m}\geq 0 (the mean exploitable move), and an auxiliary microstructure
scale Wm​c0W^{m}c\_{0} that captures residual oscillations at resolution mm
[[49](https://arxiv.org/html/2510.24467v1#bib.bib49), [44](https://arxiv.org/html/2510.24467v1#bib.bib44)].

###### Assumption 1 (Geometric scaling).

There exist constants W>0W>0 and c0>0c\_{0}>0 such that for each dyadic level mm,
the components of the local displacement satisfy the Pythagorean relation

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | (T2m)2=h¯m 2+W2​m​c0 2.\Big(\tfrac{T}{2^{m}}\Big)^{\!2}\;=\;\bar{h}\_{m}^{\,2}\;+\;W^{2m}c\_{0}^{\,2}. |  |

Identity ([6](https://arxiv.org/html/2510.24467v1#S4.E6 "Equation 6 ‣ Assumption 1 (Geometric scaling). ‣ 4.1 Triangle construction and scaling postulate ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) is purely geometric: the chord length per subinterval
is fixed by the sampling step, while the vertical excursion and the
microstructure term trade off as resolution changes.
This representation mirrors classical self-affine constructions in fractal
curves, such as those used to define the coastline paradox or Brownian paths
[[22](https://arxiv.org/html/2510.24467v1#bib.bib22), [44](https://arxiv.org/html/2510.24467v1#bib.bib44), [41](https://arxiv.org/html/2510.24467v1#bib.bib41)].

singular iith periodaveraged periodΔ=T2m\Delta=\dfrac{T}{2^{m}}Δ=T2m\Delta=\dfrac{T}{2^{m}}hn​ih\_{ni}cic\_{i}h¯m\bar{h}\_{m}Wm​c0W^{m}c\_{0}


Figure 1: Right-triangle construction per subinterval at resolution mm.
Both triangles share base Δ=T/2m\Delta=T/2^{m} and satisfy
(T2m)2=h¯m2+W2​m​c02\left(\tfrac{T}{2^{m}}\right)^{2}=\bar{h}\_{m}^{2}+W^{2m}c\_{0}^{2}.
The relation models the scale-dependent roughness of price increments
observed empirically in fractal market studies [[10](https://arxiv.org/html/2510.24467v1#bib.bib10), [8](https://arxiv.org/html/2510.24467v1#bib.bib8)].

Solving ([6](https://arxiv.org/html/2510.24467v1#S4.E6 "Equation 6 ‣ Assumption 1 (Geometric scaling). ‣ 4.1 Triangle construction and scaling postulate ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) gives the exploitable mean move

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | h¯m=T24m−W2​m​c0 2,feasible iff ​T2m>Wm​c0.\bar{h}\_{m}\;=\;\sqrt{\frac{T^{2}}{4^{m}}-W^{2m}c\_{0}^{\,2}},\qquad\text{feasible iff }\;\frac{T}{2^{m}}>W^{m}c\_{0}. |  |

The feasibility restriction ensures that at high enough resolution the
microstructure noise dominates, echoing the breakdown of scaling observed in
empirical data when market microstructure effects appear
[[16](https://arxiv.org/html/2510.24467v1#bib.bib16), [10](https://arxiv.org/html/2510.24467v1#bib.bib10)].

### 4.2 Closed form for the profit function

Substituting h¯m\bar{h}\_{m} from ([7](https://arxiv.org/html/2510.24467v1#S4.E7 "Equation 7 ‣ 4.1 Triangle construction and scaling postulate ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) into the identity
Rm=n​(r¯m−s¯)−LmR\_{m}=n(\bar{r}\_{m}-\bar{s})-L\_{m} with r¯m≡h¯m\bar{r}\_{m}\equiv\bar{h}\_{m} and n=2mn=2^{m}
yields the central expression for total profit at resolution mm.

###### Proposition 4.1 (Closed-form profit at dyadic level mm).

Under Assumption [1](https://arxiv.org/html/2510.24467v1#Thmassumption1 "Assumption 1 (Geometric scaling). ‣ 4.1 Triangle construction and scaling postulate ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"), for every mm satisfying
T2m>Wm​c0\frac{T}{2^{m}}>W^{m}c\_{0},

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | Rm= 2m​(T24m−W2​m​c0 2−s¯)−Lm.R\_{m}\;=\;2^{m}\!\left(\sqrt{\frac{T^{2}}{4^{m}}-W^{2m}c\_{0}^{\,2}}\;-\;\bar{s}\right)\;-\;L\_{m}. |  |

###### Proof 4.2.

By ([6](https://arxiv.org/html/2510.24467v1#S4.E6 "Equation 6 ‣ Assumption 1 (Geometric scaling). ‣ 4.1 Triangle construction and scaling postulate ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"))–([7](https://arxiv.org/html/2510.24467v1#S4.E7 "Equation 7 ‣ 4.1 Triangle construction and scaling postulate ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")), the exploitable mean move per trade at
level mm equals r¯m=h¯m\bar{r}\_{m}=\bar{h}\_{m} provided the square root is real, i.e.,
T2m>Wm​c0\frac{T}{2^{m}}>W^{m}c\_{0}.
Then Rm=2m​(r¯m−s¯)−LmR\_{m}=2^{m}(\bar{r}\_{m}-\bar{s})-L\_{m} gives ([8](https://arxiv.org/html/2510.24467v1#S4.E8 "Equation 8 ‣ Proposition 4.1 (Closed-form profit at dyadic level 𝑚). ‣ 4.2 Closed form for the profit function ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")).

###### Remark 4.3 (Feasibility region and qualitative behavior).

The feasibility condition T2m>Wm​c0\frac{T}{2^{m}}>W^{m}c\_{0} defines an upper bound
m<mmaxm<m\_{\max}, where mmaxm\_{\max} is the largest integer with
2−m>Wm​c0/T2^{-m}>W^{m}c\_{0}/T.
As mm increases, the chord T2m\tfrac{T}{2^{m}} shrinks while the microstructure
term Wm​c0W^{m}c\_{0} scales geometrically; hence the radicand in
([7](https://arxiv.org/html/2510.24467v1#S4.E7 "Equation 7 ‣ 4.1 Triangle construction and scaling postulate ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) decreases and eventually becomes negative, at which point the
model predicts no exploitable move at that resolution.
This upper limit parallels the practical observation that returns lose
scaling coherence beyond microsecond horizons in high-frequency markets
[[8](https://arxiv.org/html/2510.24467v1#bib.bib8), [12](https://arxiv.org/html/2510.24467v1#bib.bib12)].

### 4.3 Comparative statics at the deterministic level

Write

|  |  |  |
| --- | --- | --- |
|  | Φ​(m;T,W,c0):=T24m−W2​m​c0 2,soRm=2m​(Φ​(m;T,W,c0)−s¯)−Lm.\Phi(m;T,W,c\_{0})\;:=\;\sqrt{\tfrac{T^{2}}{4^{m}}-W^{2m}c\_{0}^{\,2}},\quad\text{so}\quad R\_{m}=2^{m}\big(\Phi(m;T,W,c\_{0})-\bar{s}\big)-L\_{m}. |  |

Within the feasible set:

* •

  RmR\_{m} decreases linearly in s¯\bar{s} and in LmL\_{m},
  reflecting the standard frictional mechanism of Davis and Norman [[18](https://arxiv.org/html/2510.24467v1#bib.bib18)].
* •

  RmR\_{m} declines with WW and c0c\_{0} since larger microstructure
  intensity reduces net exploitable motion, consistent with empirical
  microstructure estimates [[48](https://arxiv.org/html/2510.24467v1#bib.bib48), [16](https://arxiv.org/html/2510.24467v1#bib.bib16)].
* •

  There is a discrete trade-off in mm: the multiplier 2m2^{m} favors
  finer sampling, while Φ​(m;⋅)\Phi(m;\cdot) typically shrinks with mm and
  feasibility eventually fails (Remark [4.3](https://arxiv.org/html/2510.24467v1#S4.Thmtheorem3 "Remark 4.3 (Feasibility region and qualitative behavior). ‣ 4.2 Closed form for the profit function ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")).

This deterministic structure prepares the ground for the stochastic
generalization in Section [6](https://arxiv.org/html/2510.24467v1#S6 "6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"), where
Φ​(m;⋅)\Phi(m;\cdot) will emerge from the self-similar scaling law of fractional Brownian motion [[7](https://arxiv.org/html/2510.24467v1#bib.bib7), [20](https://arxiv.org/html/2510.24467v1#bib.bib20)].

## 5 Optimization of Trading Frequency

We now study the choice of resolution mm (equivalently, the number of
trades n=2mn=2^{m}) that maximizes the total profit RmR\_{m} given in
([8](https://arxiv.org/html/2510.24467v1#S4.E8 "Equation 8 ‣ Proposition 4.1 (Closed-form profit at dyadic level 𝑚). ‣ 4.2 Closed form for the profit function ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")). Denote the feasible index set by

|  |  |  |
| --- | --- | --- |
|  | ℳ:={m∈ℕ:T2m>Wm​c0}={0,1,…,mmax}.\mathcal{M}\;:=\;\{\,m\in\mathbb{N}:\tfrac{T}{2^{m}}>W^{m}c\_{0}\,\}\;=\;\{0,1,\dots,m\_{\max}\}. |  |

### 5.1 Existence (finite feasible set)

The discrete maximization problem resembles the impulse–control problems of
Davis and Norman [[18](https://arxiv.org/html/2510.24467v1#bib.bib18)] and Shreve and Soner [[50](https://arxiv.org/html/2510.24467v1#bib.bib50)],
where optimal rebalancing is characterized by no–trade regions rather than
continuous adjustment.
Here, the feasible set ℳ\mathcal{M} is finite, which immediately yields the
existence of a maximizer.

###### Proposition 5.1 (Existence of a maximizer).

For fixed parameters (T,W,c0,s¯)(T,W,c\_{0},\bar{s}) and any nonnegative cost sequence
{Lm}m∈ℳ\{L\_{m}\}\_{m\in\mathcal{M}}, the maximization problem
maxm∈ℳ⁡Rm\max\_{m\in\mathcal{M}}R\_{m} admits at least one solution
m⋆∈ℳm^{\star}\in\mathcal{M}.

###### Proof 5.2.

ℳ\mathcal{M} is finite and RmR\_{m} is real-valued on ℳ\mathcal{M} by
Proposition [4.1](https://arxiv.org/html/2510.24467v1#S4.Thmtheorem1 "Proposition 4.1 (Closed-form profit at dyadic level 𝑚). ‣ 4.2 Closed form for the profit function ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"), hence the maximum is attained.

### 5.2 Marginal characterization via forward differences

Discrete changes in mm play the same role here as marginal time adjustments in
continuous trading models [[15](https://arxiv.org/html/2510.24467v1#bib.bib15), [53](https://arxiv.org/html/2510.24467v1#bib.bib53), [34](https://arxiv.org/html/2510.24467v1#bib.bib34)].
Define the forward difference of total profit

|  |  |  |
| --- | --- | --- |
|  | Δ​Rm:=Rm+1−Rm,m=0,1,…,mmax−1.\Delta R\_{m}\;:=\;R\_{m+1}-R\_{m},\qquad m=0,1,\dots,m\_{\max}-1. |  |

Using Rm=2m​(Φm−s¯)−LmR\_{m}=2^{m}(\Phi\_{m}-\bar{s})-L\_{m} with
Φm:=T24m−W2​m​c0 2\Phi\_{m}:=\sqrt{\tfrac{T^{2}}{4^{m}}-W^{2m}c\_{0}^{\,2}}, a direct calculation gives

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | Δ​Rm=2m​(2​Φm+1−Φm−s¯)−Δ​Lm,Δ​Lm:=Lm+1−Lm≥0.\Delta R\_{m}=2^{m}\!\Big(2\Phi\_{m+1}-\Phi\_{m}-\bar{s}\Big)\;-\;\Delta L\_{m},\qquad\Delta L\_{m}:=L\_{m+1}-L\_{m}\geq 0. |  |

###### Theorem 5.3 (Marginal stopping rule).

Suppose LmL\_{m} is nondecreasing and
2​Φm+1−Φm2\Phi\_{m+1}-\Phi\_{m} is nonincreasing in mm
(*diminishing marginal exploitable move*).
Then RmR\_{m} is unimodal on ℳ\mathcal{M}, and any maximizer m⋆m^{\star} is
characterized by the smallest index for which Δ​Rm≤0\Delta R\_{m}\leq 0:

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | m⋆=min⁡{m∈ℳ:Δ​Rm≤0}.m^{\star}\;=\;\min\big\{\,m\in\mathcal{M}:\ \Delta R\_{m}\leq 0\,\big\}. |  |

In particular, if Δ​Rm>0\Delta R\_{m}>0 for all m<mmaxm<m\_{\max} then m⋆=mmaxm^{\star}=m\_{\max},
while if Δ​R0≤0\Delta R\_{0}\leq 0 then m⋆=0m^{\star}=0.

###### Proof 5.4.

The argument parallels the discrete concavity reasoning of
Proposition [5.6](https://arxiv.org/html/2510.24467v1#S5.Thmtheorem6 "Proposition 5.6 (Strict unimodality and uniqueness). ‣ 5.3 Sufficient conditions for uniqueness ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") and impulse‐control logic
[[18](https://arxiv.org/html/2510.24467v1#bib.bib18), [15](https://arxiv.org/html/2510.24467v1#bib.bib15)].
Monotonicity of LmL\_{m} and 2​Φm+1−Φm2\Phi\_{m+1}-\Phi\_{m} implies that the sequence of
differences {Δ​Rm}\{\Delta R\_{m}\} is nonincreasing, so it can cross zero at most
once. Consequently, {Rm}\{R\_{m}\} is unimodal and
([10](https://arxiv.org/html/2510.24467v1#S5.E10 "Equation 10 ‣ Theorem 5.3 (Marginal stopping rule). ‣ 5.2 Marginal characterization via forward differences ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) identifies the first nonpositive increment as the optimum.

###### Remark 5.5 (Economic interpretation).

The term 2m​(2​Φm+1−Φm)2^{m}(2\Phi\_{m+1}-\Phi\_{m}) represents the *gross marginal benefit*
from refining the trading grid from mm to m+1m{+}1, i.e., doubling the number
of trades. The terms 2m​s¯2^{m}\bar{s} and Δ​Lm\Delta L\_{m} represent, respectively, the
*marginal execution friction* and the *incremental cognitive or
computational cost*. The stopping rule Δ​Rm≤0\Delta R\_{m}\leq 0 thus formalizes the
principle known from dynamic–trading literature
[[2](https://arxiv.org/html/2510.24467v1#bib.bib2), [12](https://arxiv.org/html/2510.24467v1#bib.bib12), [48](https://arxiv.org/html/2510.24467v1#bib.bib48)]: increase trading frequency only
until the marginal gain equals the incremental total cost.

![Refer to caption](x1.png)


Figure 2: Expected profit RmR\_{m} as a function of trading resolution mm
in the deterministic framework of Section [4](https://arxiv.org/html/2510.24467v1#S4 "4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding").
The curve illustrates the trade–off between the exploitable
substructure gain (first term) and proportional plus cognitive costs
(2m​s¯+L​(m)2^{m}\bar{s}+L(m)). The interior maximum corresponds to the optimal
trading interval Δ⋆=T/2m⋆\Delta^{\star}=T/2^{m^{\star}}.
  
                                            Source: Own calculations performed in Julia

The shape of RmR\_{m} captures the essential logic of the omniscient investor’s dilemma.
At coarse resolutions (small mm), trading is too infrequent to exploit
micro–fluctuations in the price path, resembling under‐trading equilibria
observed in bounded–rationality models [[51](https://arxiv.org/html/2510.24467v1#bib.bib51), [26](https://arxiv.org/html/2510.24467v1#bib.bib26)].
As the resolution increases, the exploitable deterministic variation grows and
so does attainable profit, as in high–frequency execution models
[[2](https://arxiv.org/html/2510.24467v1#bib.bib2), [12](https://arxiv.org/html/2510.24467v1#bib.bib12)].
Beyond the interior optimum m⋆m^{\star}, however, the rapidly compounding
execution frictions and cognitive costs dominate, causing total expected profit
to decline—a pattern consistent with concave profit functions in transaction–
cost theory [[18](https://arxiv.org/html/2510.24467v1#bib.bib18), [50](https://arxiv.org/html/2510.24467v1#bib.bib50), [36](https://arxiv.org/html/2510.24467v1#bib.bib36)].
The resulting hump-shaped profile visually represents the analytical
first–order condition and interprets Δ⋆=T/2m⋆\Delta^{\star}=T/2^{m^{\star}} as the
frequency at which greed and laziness balance.

### 5.3 Sufficient conditions for uniqueness

Let Am:=2m​ΦmA\_{m}:=2^{m}\Phi\_{m} and write Rm=Am−2m​s¯−LmR\_{m}=A\_{m}-2^{m}\bar{s}-L\_{m}.

###### Assumption 2 (Regularity).

(i) {Am}m∈ℳ\{A\_{m}\}\_{m\in\mathcal{M}} is strictly concave in the discrete sense:
Δ2​Am:=Am+2−2​Am+1+Am<0\Delta^{2}A\_{m}:=A\_{m+2}-2A\_{m+1}+A\_{m}<0 for all mm with
m+2∈ℳm{+}2\in\mathcal{M}.
  
(ii) LmL\_{m} is convex and nondecreasing on ℳ\mathcal{M}.

These curvature conditions are analogous to standard assumptions guaranteeing
unique controls in stochastic optimization and dynamic programming
[[53](https://arxiv.org/html/2510.24467v1#bib.bib53), [34](https://arxiv.org/html/2510.24467v1#bib.bib34), [40](https://arxiv.org/html/2510.24467v1#bib.bib40)].

###### Proposition 5.6 (Strict unimodality and uniqueness).

Under Assumption [2](https://arxiv.org/html/2510.24467v1#Thmassumption2 "Assumption 2 (Regularity). ‣ 5.3 Sufficient conditions for uniqueness ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"), the sequence {Rm}\{R\_{m}\} is strictly
unimodal and the maximizer m⋆m^{\star} is unique.

###### Proof 5.7 (Proof sketch).

Discrete concavity of AmA\_{m} and convexity of 2m​s¯+Lm2^{m}\bar{s}+L\_{m} imply that
Δ​Rm\Delta R\_{m} is strictly decreasing in mm, hence it changes sign at most once
and the maximizer is unique [[34](https://arxiv.org/html/2510.24467v1#bib.bib34), [40](https://arxiv.org/html/2510.24467v1#bib.bib40)].

Full proof of Theorem [5.6](https://arxiv.org/html/2510.24467v1#S5.Thmtheorem6 "Proposition 5.6 (Strict unimodality and uniqueness). ‣ 5.3 Sufficient conditions for uniqueness ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") can be found in appendix [A](https://arxiv.org/html/2510.24467v1#A1 "Appendix A Proofs of Main Results ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding").

###### Corollary 5.8 (Power–law laziness cost).

If Lm=λ​ 2α​mL\_{m}=\lambda\,2^{\alpha m} with λ≥0\lambda\geq 0 and α≥1\alpha\geq 1
(*linear or superlinear computational/latency growth*),
then Assumption [2](https://arxiv.org/html/2510.24467v1#Thmassumption2 "Assumption 2 (Regularity). ‣ 5.3 Sufficient conditions for uniqueness ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")(ii) holds and the maximizer is unique
provided AmA\_{m} is discretely concave.
This specification is consistent with the convex energy or latency cost models
used in high–frequency algorithmic trading [[12](https://arxiv.org/html/2510.24467v1#bib.bib12)].
In particular,

|  |  |  |
| --- | --- | --- |
|  | Δ​Rm=2m​(2​Φm+1−Φm−s¯)−λ​(2α​(m+1)−2α​m),\Delta R\_{m}=2^{m}\!\Big(2\Phi\_{m+1}-\Phi\_{m}-\bar{s}\Big)\;-\;\lambda(2^{\alpha(m+1)}-2^{\alpha m}), |  |

and the stopping rule ([10](https://arxiv.org/html/2510.24467v1#S5.E10 "Equation 10 ‣ Theorem 5.3 (Marginal stopping rule). ‣ 5.2 Marginal characterization via forward differences ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) applies.

### 5.4 Bounds and comparative statics

Within the feasible region,

|  |  |  |
| --- | --- | --- |
|  | ∂Rm∂s¯=−2m< 0,∂Rm∂c0=2m​−W2​m​c0Φm< 0,∂Rm∂W=2m​−W2​m−1​c0 2Φm< 0.\frac{\partial R\_{m}}{\partial\bar{s}}=-2^{m}\;<\;0,\qquad\frac{\partial R\_{m}}{\partial c\_{0}}=2^{m}\,\frac{-W^{2m}c\_{0}}{\Phi\_{m}}\;<\;0,\qquad\frac{\partial R\_{m}}{\partial W}=2^{m}\,\frac{-W^{2m-1}c\_{0}^{\,2}}{\Phi\_{m}}\;<\;0. |  |

Hence the optimal index m⋆m^{\star} is (weakly) decreasing in each of s¯\bar{s},
WW, and c0c\_{0}, and (weakly) decreasing in any parameter that increases LmL\_{m}
pointwise.
In words: higher frictions, rougher effective microstructure, or
larger computation costs shift the optimizer toward *less* frequent trading,
a result consistent with comparative statics in continuous–time
transaction–cost equilibria [[50](https://arxiv.org/html/2510.24467v1#bib.bib50), [36](https://arxiv.org/html/2510.24467v1#bib.bib36), [40](https://arxiv.org/html/2510.24467v1#bib.bib40)].

### 5.5 Practical algorithm (discrete argmax)

Given (T,W,c0,s¯)(T,W,c\_{0},\bar{s}) and a specification for LmL\_{m}:

1. 1.

   Compute mmaxm\_{\max} from feasibility (Remark [4.3](https://arxiv.org/html/2510.24467v1#S4.Thmtheorem3 "Remark 4.3 (Feasibility region and qualitative behavior). ‣ 4.2 Closed form for the profit function ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")).
2. 2.

   For m=0,1,…,mmax−1m=0,1,\dots,m\_{\max}-1, evaluate Δ​Rm\Delta R\_{m} via ([9](https://arxiv.org/html/2510.24467v1#S5.E9 "Equation 9 ‣ 5.2 Marginal characterization via forward differences ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")).
3. 3.

   If some Δ​Rm≤0\Delta R\_{m}\leq 0, set m⋆=min⁡{m:Δ​Rm≤0}m^{\star}=\min\{m:\Delta R\_{m}\leq 0\}.
   Otherwise set m⋆=mmaxm^{\star}=m\_{\max}.
4. 4.

   (Optional) Verify uniqueness by checking Δ​Rm⋆−1>0\Delta R\_{m^{\star}-1}>0 and
   Δ​Rm⋆≤0\Delta R\_{m^{\star}}\leq 0.

This procedure is O​(mmax)O(m\_{\max}) and numerically stable because it avoids
subtracting large close numbers in Rm+1−RmR\_{m+1}-R\_{m}; all terms remain positive and
well scaled as long as feasibility is enforced [[2](https://arxiv.org/html/2510.24467v1#bib.bib2), [12](https://arxiv.org/html/2510.24467v1#bib.bib12)].

## 6 Stochastic Extension via Fractional Brownian Motion

The deterministic framework of Section [4](https://arxiv.org/html/2510.24467v1#S4 "4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")
can be interpreted as a scaling law for the exploitable price increments
as the observation interval Δ\Delta varies.
We now embed this scaling in a stochastic process with well-defined
self-similarity and fractal properties — fractional Brownian motion (fBM) [[45](https://arxiv.org/html/2510.24467v1#bib.bib45), [7](https://arxiv.org/html/2510.24467v1#bib.bib7), [47](https://arxiv.org/html/2510.24467v1#bib.bib47)], very widely used in financial applications [[30](https://arxiv.org/html/2510.24467v1#bib.bib30)].
This provides a probabilistic foundation for the model and allows explicit comparative statics with respect to the roughness of the price path, in line with modern evidence on rough volatility [[6](https://arxiv.org/html/2510.24467v1#bib.bib6), [3](https://arxiv.org/html/2510.24467v1#bib.bib3)].

### 6.1 Fractional Brownian motion model

Let {BtH}t≥0\{B^{H}\_{t}\}\_{t\geq 0} denote a fractional Brownian motion with
Hurst index H∈(0,1)H\in(0,1), mean zero, and covariance

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[BtH​BsH]=12​(t2​H+s2​H−|t−s|2​H).\mathbb{E}[B^{H}\_{t}B^{H}\_{s}]=\tfrac{1}{2}\Big(t^{2H}+s^{2H}-|t-s|^{2H}\Big). |  |

The process is HH-self-similar and has stationary increments:
for all λ>0\lambda>0,
Bλ​tH−Bλ​sH=dλH​(BtH−BsH)B^{H}\_{\lambda t}-B^{H}\_{\lambda s}\stackrel{{\scriptstyle d}}{{=}}\lambda^{H}(B^{H}\_{t}-B^{H}\_{s}) [[45](https://arxiv.org/html/2510.24467v1#bib.bib45)].
For H=12H=\tfrac{1}{2} the process reduces to standard Brownian motion,
while for H<12H<\tfrac{1}{2} the increments are negatively correlated
and the sample paths are rougher (fractal dimension D=2−HD=2-H) [[7](https://arxiv.org/html/2510.24467v1#bib.bib7), [47](https://arxiv.org/html/2510.24467v1#bib.bib47)].

We model the log-price process XtX\_{t} as

|  |  |  |
| --- | --- | --- |
|  | Xt=μ​t+σ​BtH,X\_{t}=\mu t+\sigma B^{H}\_{t}, |  |

where μ\mu and σ\sigma are constant drift and volatility parameters.
The absolute log-return over an interval of length Δ\Delta
is |Δ​Xi|=σ​|Bti+1H−BtiH||\Delta X\_{i}|=\sigma|B^{H}\_{t\_{i+1}}-B^{H}\_{t\_{i}}|,
whose expected value satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | 𝔼​|Δ​Xi|=κ​(H,σ)​ΔH,κ​(H,σ):=σ​𝔼​|B1H|=σ​C,\mathbb{E}|\Delta X\_{i}|=\kappa(H,\sigma)\,\Delta^{H},\qquad\kappa(H,\sigma):=\sigma\,\mathbb{E}|B^{H}\_{1}|=\sigma\,C, |  |

with C=2/πC=\sqrt{2/\pi} because B1H∼𝒩​(0,1)B^{H}\_{1}\sim\mathcal{N}(0,1) for all HH [[7](https://arxiv.org/html/2510.24467v1#bib.bib7), [47](https://arxiv.org/html/2510.24467v1#bib.bib47)].
Equation ([11](https://arxiv.org/html/2510.24467v1#S6.E11 "Equation 11 ‣ 6.1 Fractional Brownian motion model ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) formally connects the exploitable mean move per trade
to the fractal scaling exponent HH and is consistent with empirical estimates of HH from high-frequency data [[4](https://arxiv.org/html/2510.24467v1#bib.bib4)].

### 6.2 Expected profit function

For an omniscient trader who takes the correct direction of each move,
the expected gross gain over the horizon TT when trading every Δ\Delta
time units (i.e., n=T/Δn=T/\Delta trades) is

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Gain]=TΔ​κ​(H,σ)​ΔH=κ​T​ΔH−1,\mathbb{E}[{\rm Gain}]=\frac{T}{\Delta}\,\kappa(H,\sigma)\,\Delta^{H}=\kappa T\Delta^{H-1}, |  |

where we write κ=κ​(H,σ)\kappa=\kappa(H,\sigma) for brevity.
Subtracting proportional execution frictions s¯\bar{s} and
aggregate laziness cost LL yields the total expected profit.

###### Proposition 6.1 (Expected profit under fBM scaling).

For Δ=T/2m\Delta=T/2^{m},

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | R​(Δ)=κ​T​ΔH−1−T​s¯Δ−L.R(\Delta)=\kappa T\Delta^{H-1}-\frac{T\bar{s}}{\Delta}-L. |  |

###### Proof 6.2.

The first term represents the expected exploitable return from n=T/Δn=T/\Delta trades via ([11](https://arxiv.org/html/2510.24467v1#S6.E11 "Equation 11 ‣ 6.1 Fractional Brownian motion model ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"));
the second aggregates per-trade frictions; the third is the total laziness cost.

Expression ([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) mirrors the deterministic formula
([8](https://arxiv.org/html/2510.24467v1#S4.E8 "Equation 8 ‣ Proposition 4.1 (Closed-form profit at dyadic level 𝑚). ‣ 4.2 Closed form for the profit function ‣ 4 Deterministic Fractal Derivation ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")), with the role of geometric roughness now played by the stochastic scaling exponent HH [[45](https://arxiv.org/html/2510.24467v1#bib.bib45)].

This scaling property also underlies recent theoretical analyses of high-frequency trading under fractional Brownian motion dynamics.
In particular, Guasoni, Mishura, and Rásonyi [[29](https://arxiv.org/html/2510.24467v1#bib.bib29)]
show that in the high-frequency limit, the conditionally expected increments of fBM converge to a white noise. Their results demonstrate that trading costs endogenously impose a finite optimal frequency, consistent with the frictional bound derived in our model.

### 6.3 Optimal rebalancing interval

Treating Δ\Delta as a continuous decision variable,
we maximize ([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) over Δ>0\Delta>0.
Differentiating with respect to Δ\Delta (and omitting the constant LL)
yields the first-order condition

|  |  |  |
| --- | --- | --- |
|  | d​Rd​Δ=κ​T​(H−1)​ΔH−2+T​s¯​Δ−2=0.\frac{dR}{d\Delta}=\kappa T(H-1)\Delta^{H-2}+T\bar{s}\,\Delta^{-2}=0. |  |

Solving for Δ\Delta gives the unique interior optimizer.

###### Theorem 6.3 (Optimal trading interval).

Under s¯>0\bar{s}>0 and κ>0\kappa>0,
the profit function ([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) has a unique maximizer

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | Δ⋆=(s¯κ​(1−H))1/H.\Delta^{\star}=\Big(\frac{\bar{s}}{\kappa(1-H)}\Big)^{1/H}. |  |

The corresponding optimal number of trades is
n⋆=T/Δ⋆n^{\star}=T/\Delta^{\star}.

###### Proof 6.4.

For H∈(0,1)H\in(0,1), R​(Δ)R(\Delta) is strictly concave in ΔH\Delta^{H} and the
first-order condition admits a single positive root, yielding ([13](https://arxiv.org/html/2510.24467v1#S6.E13 "Equation 13 ‣ Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")).

###### Corollary 6.5 (Fractal comparative statics).

Let D=2−HD=2-H denote the Hausdorff dimension of the fBM sample paths.
Then

|  |  |  |
| --- | --- | --- |
|  | ∂Δ⋆∂D<0,∂Δ⋆∂s¯>0,∂Δ⋆∂κ<0.\frac{\partial\Delta^{\star}}{\partial D}<0,\quad\frac{\partial\Delta^{\star}}{\partial\bar{s}}>0,\quad\frac{\partial\Delta^{\star}}{\partial\kappa}<0. |  |

Hence more fractal (rougher) price paths - larger DD or smaller HH - imply
a smaller optimal interval Δ⋆\Delta^{\star}, i.e., higher optimal trading frequency,
which is consistent with rough-volatility evidence and the FMH perspective on short-horizon dominance during turbulence [[28](https://arxiv.org/html/2510.24467v1#bib.bib28), [37](https://arxiv.org/html/2510.24467v1#bib.bib37), [49](https://arxiv.org/html/2510.24467v1#bib.bib49)].

Full proofs of Theorem [6.3](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem3 "Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") and Corollary [6.5](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem5 "Corollary 6.5 (Fractal comparative statics). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") can be found in appendix [A](https://arxiv.org/html/2510.24467v1#A1 "Appendix A Proofs of Main Results ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding").

Figure [3](https://arxiv.org/html/2510.24467v1#S6.F3 "Figure 3 ‣ 6.4 Simulation under fractional Brownian motion ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") illustrates the comparative statics implied by
([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) and Theorem [6.3](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem3 "Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"): rougher paths (smaller HH) push the
optimum toward higher trading frequency, whereas the convex laziness penalty
L​(m)L(m) governs the sharpness of the decline beyond m⋆m^{\star}.

### 6.4 Simulation under fractional Brownian motion

To verify the robustness of the analytical relation
([13](https://arxiv.org/html/2510.24467v1#S6.E13 "Equation 13 ‣ Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")), we conducted numerical simulations of the model
under fractional Brownian motion (fBM) price dynamics. Synthetic log–price paths of unit length T=1T=1 were generated for three representative Hurst exponents H∈{0.40, 0.60, 0.80}H\in\{0.40,\,0.60,\,0.80\} using both the Cholesky decomposition [[9](https://arxiv.org/html/2510.24467v1#bib.bib9), Ch. 17] and the improved
Davies–Harte circulant-embedding method
[[19](https://arxiv.org/html/2510.24467v1#bib.bib19), [17](https://arxiv.org/html/2510.24467v1#bib.bib17)].
For each HH, we evaluated the expected profit function
([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) on a dyadic grid
Δ=T/2m\Delta=T/2^{m} for m=1,…,12m=1,\dots,12,
using the same parameters as in the theoretical model:

|  |  |  |
| --- | --- | --- |
|  | s¯=0.002,κ=0.5,λ=6×10−4,α=1.4.\bar{s}=0.002,\qquad\kappa=0.5,\qquad\lambda=6\times 10^{-4},\qquad\alpha=1.4. |  |

The laziness cost was specified as
L​(m)=L0+λ​ 2α​mL(m)=L\_{0}+\lambda\,2^{\alpha m} with L0=0L\_{0}=0.
For each configuration, the maximizer
msim⋆=arg⁡maxm⁡Rmm^{\star}\_{\text{sim}}=\arg\max\_{m}R\_{m}
was identified and compared with the theoretical prediction
mtheory⋆​(H)m^{\star}\_{\text{theory}}(H) obtained from
([13](https://arxiv.org/html/2510.24467v1#S6.E13 "Equation 13 ‣ Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")).

Figure [3](https://arxiv.org/html/2510.24467v1#S6.F3 "Figure 3 ‣ 6.4 Simulation under fractional Brownian motion ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") displays the resulting profit profiles
for the three Hurst exponents.
The curves exhibit the predicted concave shape with a clear interior optimum,
whose location shifts systematically with HH:
rougher trajectories (H=0.40H=0.40) yield smaller optimal intervals
(higher trading frequencies), whereas smoother paths (H=0.80H=0.80) produce
larger optimal intervals (less frequent rebalancing).
The correspondence between simulated and theoretical optima is within
55–10%10\% across all cases, and the scaling law
Δ⋆∝(1−H)−1/H\Delta^{\star}\propto(1-H)^{-1/H} is clearly reproduced.
These results confirm that the omniscient–lazy investor framework
faithfully translates the fractal scaling exponent of the underlying
stochastic process into an economically interpretable trading rhythm.

![Refer to caption](x2.png)


Figure 3: Simulated profit functions RmR\_{m} under fractional Brownian motion
for different Hurst exponents H∈{0.40,0.60,0.80}H\in\{0.40,0.60,0.80\}. Parameter values: T=1T=1, κ=0.5\kappa=0.5, s¯=0.002\bar{s}=0.002, λ=6×10−4\lambda=6\times 10^{-4}, α=1.4\alpha=1.4.
Each curve exhibits an interior optimum m⋆​(H)m^{\star}(H) that shifts toward finer
resolutions as HH decreases, in agreement with
Theorem [6.3](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem3 "Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding").
  
                                            Source: Own calculations performed in Julia.

### 6.5 Including computational or latency costs

The additive constant LL in ([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) can be generalized to a frequency‐dependent cost, L=L​(n)L=L(n), to capture the practical fact that
more frequent trading increases computational and technological expenditure, as emphasized in algorithmic execution frameworks [[12](https://arxiv.org/html/2510.24467v1#bib.bib12)].
A convenient specification is a power law

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | L​(n)=λ​nα=λ​(TΔ)α,λ>0,α≥1,L(n)=\lambda n^{\alpha}=\lambda\Big(\frac{T}{\Delta}\Big)^{\alpha},\qquad\lambda>0,\ \alpha\geq 1, |  |

where α=1\alpha=1 corresponds to linear latency costs and α>1\alpha>1
to superlinear growth in computational demand [[24](https://arxiv.org/html/2510.24467v1#bib.bib24)].
Substituting ([14](https://arxiv.org/html/2510.24467v1#S6.E14 "Equation 14 ‣ 6.5 Including computational or latency costs ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) into ([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) gives

|  |  |  |
| --- | --- | --- |
|  | R​(Δ)=κ​T​ΔH−1−T​s¯Δ−λ​Tα​Δ−α.R(\Delta)=\kappa T\Delta^{H-1}-\frac{T\bar{s}}{\Delta}-\lambda T^{\alpha}\Delta^{-\alpha}. |  |

The first-order condition becomes

|  |  |  |
| --- | --- | --- |
|  | κ​(1−H)​ΔH=s¯+λ​α​Δ1−α.\kappa(1-H)\Delta^{H}=\bar{s}+\lambda\alpha\,\Delta^{1-\alpha}. |  |

For α=1\alpha=1 this yields the closed form
Δ⋆=[(s¯+λ)/(κ​(1−H))]1/H\Delta^{\star}=[(\bar{s}+\lambda)/(\kappa(1-H))]^{1/H};
for α>1\alpha>1, the equation is monotone in Δ\Delta and
can be solved numerically by Newton iteration.
In all cases, the existence and uniqueness of a positive solution remain.

### 6.6 Economic interpretation

Equation ([13](https://arxiv.org/html/2510.24467v1#S6.E13 "Equation 13 ‣ Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")) quantifies the balance between trading frictions and fractal roughness.
Smaller HH (rougher paths) magnify the benefit of acting more often, while larger execution costs s¯\bar{s} or higher latency parameters shift the optimum toward less frequent rebalancing.
The model thus provides an explicit theoretical link between the fractal geometry of market trajectories and the economic decision of how often to trade, consistent with both rough-volatility findings [[28](https://arxiv.org/html/2510.24467v1#bib.bib28), [6](https://arxiv.org/html/2510.24467v1#bib.bib6)] and the fractal market hypothesis [[49](https://arxiv.org/html/2510.24467v1#bib.bib49), [37](https://arxiv.org/html/2510.24467v1#bib.bib37)].

## 7 Empirical and Simulation Evidence

This section provides numerical and empirical validation of the
fractal–optimization framework.
We first estimate the scaling parameters HH and κ\kappa from historical
equity data and calibrate the effective cost parameters
(s¯,λ,α)(\bar{s},\lambda,\alpha) to observed trading frictions.
We then compare the empirical profit curve RmR\_{m} to the theoretical prediction
derived from ([12](https://arxiv.org/html/2510.24467v1#S6.E12 "Equation 12 ‣ Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")), followed by Monte–Carlo simulations
based on fractional Brownian motion (fBM) to verify the scaling law
for the optimal interval Δ⋆\Delta^{\star}.

### 7.1 Data and estimation

Daily adjusted closing prices for Apple Inc. (AAPL) were obtained from
Yahoo Finance over a five–year horizon (January 2020–January 2025).
The logarithmic price series xt=log⁡ptx\_{t}=\log p\_{t} was used to compute absolute
increments at dyadic sampling steps k=2mk=2^{m}.
For each level mm, the mean absolute increment
𝔼​|Δ​x|m\mathbb{E}|\Delta x|\_{m} was estimated and the log–log regression

|  |  |  |
| --- | --- | --- |
|  | log⁡𝔼​|Δ​x|m=log⁡κ+H​log⁡(k​Δ​t)\log\mathbb{E}|\Delta x|\_{m}=\log\kappa+H\log(k\Delta t) |  |

yielded the empirical scaling parameters

|  |  |  |
| --- | --- | --- |
|  | H^=0.491,κ^=0.01336.\widehat{H}=0.491,\qquad\widehat{\kappa}=0.01336. |  |

The estimated Hurst exponent lies close to the Brownian benchmark
H=0.5H=0.5, consistent with mildly rough market dynamics.
The scaling coefficient κ\kappa determines the average exploitable
magnitude per trade and sets the calibration scale for the theoretical
profit function.

Execution frictions were parameterized by an effective spread of
s¯=0.025\bar{s}=0.025 (250 bps) per transaction,
and the laziness cost was modeled as
L​(n)=λ​nαL(n)=\lambda n^{\alpha} with
λ=0.003\lambda=0.003 and α=1.3\alpha=1.3,
representing superlinear growth in cognitive or latency costs as trading
frequency increases.
These values produce a realistic trade–off between marginal gain and
marginal cost at daily resolution.

### 7.2 Results

Figure [4](https://arxiv.org/html/2510.24467v1#S7.F4 "Figure 4 ‣ 7.2 Results ‣ 7 Empirical and Simulation Evidence ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") compares the empirical profit function
RmR\_{m} computed from the data to the theoretical curve implied by the
fractional Brownian scaling model.
Both exhibit the characteristic concave (hump–shaped) profile predicted by
Proposition [6.1](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem1 "Proposition 6.1 (Expected profit under fBM scaling). ‣ 6.2 Expected profit function ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") and Theorem [6.3](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem3 "Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding").
The empirical maximizer occurs at
memp⋆=5m^{\star}\_{\text{emp}}=5, corresponding to a trading interval of roughly
one week, while the theoretical optimum under the estimated parameters is
mtheory⋆=6m^{\star}\_{\text{theory}}=6
(Δtheory⋆≈14.2\Delta^{\star}\_{\text{theory}}\approx 14.2 days).
The close alignment between empirical and theoretical optima confirms
that the model captures the observed scale at which incremental profits
cease to outweigh frictions.

![Refer to caption](x3.png)


Figure 4: Empirical and theoretical profit curves RmR\_{m} for AAPL
daily data (2020–2025).
The empirical optimum memp⋆=5m^{\star}\_{\text{emp}}=5 (red marker) lies near
the theoretical prediction mtheory⋆=6m^{\star}\_{\text{theory}}=6,
illustrating consistency between observed and predicted trading
frequencies.
  
                                            Source: Own calculations performed in Julia.

The estimated scaling parameters imply a theoretical optimal interval of
about two weeks, which is economically plausible for high–liquidity
equities given typical transaction costs and intraday volatility.
The resulting alignment supports the interpretation of HH
as a measure of effective market roughness that governs the curvature
of the profit function and hence the investor’s optimal trading rhythm.

## 8 Conclusions

Our omniscient yet lazy investor has finally reached enlightenment — not by trading faster,
but by learning when to stop. In his world, perfect foresight meets finite patience: knowing
every future price does not justify acting upon each of them. Each trade consumes energy,
bandwidth, and thought. Somewhere between greed and exhaustion lies an equilibrium — the
optimal trading frequency — that maximizes profit under the laws of fractal scaling.

At its heart, this paper has shown that even when information is perfect, *action* must
still be optimized. The deterministic framework established a geometric balance between
exploitable variation and friction, while the stochastic extension under fractional Brownian
motion translated this geometry into a universal scaling law,

|  |  |  |
| --- | --- | --- |
|  | Δ⋆=[s¯κ​(1−H)]1/H,\Delta^{\star}=\bigg[\frac{\bar{s}}{\kappa(1-H)}\bigg]^{1/H}, |  |

linking transaction costs, volatility, and path roughness.
Rougher markets (H↓H\!\downarrow) invite more frequent trades; smoother ones encourage rest.
The omniscient investor thus obeys a law that even omniscience cannot escape: the diminishing
returns of attention.

### 8.1 Interpretation and Applications

Reinterpreted in modern terms, the omniscient investor is not a mythical prophet but a
*trading algorithm* - a machine with a perfect model of market dynamics.
Its omniscience corresponds to the assumption that our predictive engine is correct,
at least in expectation: we would not deploy it otherwise.
Given this premise, the model’s role is no longer to predict prices, but to decide
*how often* to act upon those predictions.
The laziness term captures computational latency, inference costs, and the implicit friction
of refreshing the model’s decisions.

From this perspective, the optimal trading interval Δ⋆\Delta^{\star} or equivalently the optimal
dyadic level m⋆m^{\star} becomes a practical design parameter for automated trading systems.
It could determine how often a forecasting model should rebalance, query data, or execute orders
to achieve maximal net profit once all frictions are accounted for.
In short, the stochastic extension provides a bridge from abstract fractal geometry to
concrete algorithmic implementation: the trading bot becomes omniscient by assumption, yet
remains wisely lazy by design.

This balance between foresight and restraint encapsulates the broader message of the paper.
Markets - and algorithms - do not reward infinite speed, but optimal timing. Omniscience without laziness leads to ruinous overtrading; laziness without insight yields stagnation. Only at their intersection lies the fractal optimum.

### 8.2 Further Work

The framework developed here opens several promising directions for both theory and practice.

#### (i) Multi-asset extensions.

The present model considers a single omniscient decision process applied to one asset.
Extending it to portfolios with cross-asset correlations would allow the study of collective
fractal equilibria: when several lazy bots share the same server, how often should each of them
wake up?
The resulting multidimensional optimization may connect naturally to covariance-based portfolio
control and to multivariate rough volatility models.

#### (ii) Time-varying laziness.

Real investors (and servers) are not equally lazy at all times.
Introducing a stochastic or time-dependent laziness cost LtL\_{t} could capture the alternating
moods of the market machine: energetic during turbulence, dormant in calm periods. A natural real-world example could be energy prices being higher during daytime and lower at night.
This would transform the fixed-frequency optimum into a dynamic policy reacting to computational load or volatility states.

#### (iii) Evolving roughness.

While our stochastic formulation assumed a constant Hurst exponent HH, recent developments in
multifractional Brownian motion show that roughness itself can evolve in time.
By combining the transfer principle of Bender, Lebovits, and Lévy Véhel [[5](https://arxiv.org/html/2510.24467v1#bib.bib5)]
with the current framework, one could model an investor who not only knows future prices, but
also senses changes in the geometry of their fluctuations - adjusting trading frequency as
market regularity ebbs and flows.
Such an adaptive version could explain how trading systems respond optimally to shifting
microstructure roughness and regime changes.

#### (iv) Continuous-time and asymptotic limits.

Finally, taking the limit of vanishing intervals suggests intriguing links with rough-volatility theory and stochastic control under non-Markovian noise.
In that frontier lies the truly continuous omniscient investor - a process that knows the infinitesimal future, yet still hesitates for a finite amount of time.

In short, the story of the omniscient yet lazy investor does not end with this article
It merely enters its stochastic dream phase, where each generalization, be it multifractal,
multi-asset, or multi-mood, adds new structure to the fractal geometry of rational inaction.
The optimal trading rhythm may change, but the moral remains:
even perfect knowledge must sometimes wait for the right moment to act.

## Acknowledgments

DeepL was used for stylising and translating parts of the manuscript of the text from the author’s mother tongue into english.

## References

* [1]

  Z. Alizade, H. Agahi, and S. Khademloo, Fractal analysis of financial markets using laplace–mittag-leffler distributions, Chaos, Solitons & Fractals, 199 (2025), p. 116847, <https://doi.org/10.1016/j.chaos.2025.116847>.
* [2]

  R. Almgren and N. Chriss, Optimal execution of portfolio transactions, The Journal of Risk, 3 (2000), pp. 5–39, <https://doi.org/10.21314/JOR.2001.041>.
* [3]

  C. Bayer, P. K. Friz, and J. Gatheral, Pricing under rough volatility, in Rough Volatility, C. Bayer, P. K. Friz, M. Fukasawa, J. Gatheral, A. Jacquier, and M. Rosenbaum, eds., Society for Industrial and Applied Mathematics, Philadelphia, PA, 2023, ch. 2, pp. 31–58, <https://doi.org/10.1137/1.9781611977783.ch2>.
* [4]

  E. Bayraktar, H. V. Poor, and K. R. Sircar, Estimating the fractal dimension of the s&p 500 index using wavelet analysis, International Journal of Theoretical and Applied Finance, 07 (2004), pp. 615–643, <https://doi.org/10.1142/S021902490400258X>.
* [5]

  C. Bender, J. Lebovits, and J. L. Véhel, General transfer formula for stochastic integral with respect to multifractional brownian motion, Journal of Theoretical Probability, 37 (2024), pp. 905–932, <https://doi.org/10.1007/s10959-023-01258-5>.
* [6]

  M. Bennedsen, A. Lunde, and M. S. Pakkanen, Decoupling the short- and long-term behavior of stochastic volatility, Journal of Financial Econometrics, 20 (2021), pp. 961–1006, <https://doi.org/10.1093/jjfinec/nbaa049>.
* [7]

  F. Biagini, Y. Hu, B. Øksendal, and T. Zhang, Stochastic Calculus for Fractional Brownian Motion and Applications, Probability and Its Applications, Springer London, 1 ed., 2008, <https://doi.org/10.1007/978-1-84628-797-8>.
* [8]

  J.-P. Bouchaud, M. Potters, and M. Meyer, Apparent multifractality in financial time series, The European Physical Journal B - Condensed Matter and Complex Systems, 13 (2000), pp. 595–599, <https://doi.org/10.1007/s100510050073>.
* [9]

  C. Börgers, Introduction to Numerical Linear Algebra, Society for Industrial and Applied Mathematics, Philadelphia, PA, 2022, <https://doi.org/10.1137/1.9781611976922>.
* [10]

  L. Calvet and A. Fisher, Multifractality in asset returns: Theory and evidence, The Review of Economics and Statistics, 84 (2002), pp. 381–406, <http://www.jstor.org/stable/3211559> (accessed 2025-10-24).
* [11]

  A. Caplin and M. Dean, Revealed preference, rational inattention, and costly information acquisition, American Economic Review, 105 (2015), p. 2183–2203, <https://doi.org/10.1257/aer.20140117>.
* [12]

  A. Cartea, S. Jaimungal, and J. Penalva, Algorithmic and High-Frequency Trading, Cambridge University Press, 2015.
* [13]

  A. Cartea, S. Jaimungal, and J. Ricci, Buy low, sell high: A high frequency trading perspective, SIAM Journal on Financial Mathematics, 5 (2014), pp. 415–444, <https://doi.org/10.1137/130911196>.
* [14]

  F. Comte and E. Renault, Long memory in continuous-time stochastic volatility models, Mathematical Finance, 8 (1998), pp. 291–323, <https://doi.org/10.1111/1467-9965.00057>.
* [15]

  G. M. Constantinides, Capital market equilibrium with transaction costs, Journal of Political Economy, 94 (1986), pp. 842–862, <https://doi.org/10.1086/261410>.
* [16]

  R. Cont, Empirical properties of asset returns: stylized facts and statistical issues, Quantitative Finance, 1 (2001), pp. 223–236, <https://doi.org/10.1080/713665670>.
* [17]

  P. F. Craigmile, Simulating a class of stationary gaussian processes using the davies–harte algorithm, with application to long memory processes, Journal of Time Series Analysis, 24 (2003), pp. 505–511, <https://doi.org/https://doi.org/10.1111/1467-9892.00318>.
* [18]

  M. H. A. Davis and A. R. Norman, Portfolio selection with transaction costs, Mathematics of Operations Research, 15 (1990), pp. 676–713, <http://www.jstor.org/stable/3689770> (accessed 2025-10-27).
* [19]

  A. B. Dieker and M. Mandjes, On spectral simulation of fractional brownian motion, Probab. Eng. Inf. Sci., 17 (2003), p. 417–434, <https://doi.org/10.1017/S0269964803173081>.
* [20]

  T. E. Duncan, Y. Hu, and B. Pasik-Duncan, Stochastic calculus for fractional brownian motion i. theory, SIAM Journal on Control and Optimization, 38 (2000), pp. 582–612, <https://doi.org/10.1137/S036301299834171X>.
* [21]

  R. A. El-Nabulsi and W. Anukool, Qualitative financial modelling in fractal dimensions, Financial Innovation, 11 (2025), p. 42, <https://doi.org/10.1186/s40854-024-00723-2>.
* [22]

  J. Feder, Fractals, Plenum Press, 1988.
* [23]

  M. Fernández-Martínez, J. L. G. Guirao, M. Á. Sánchez-Granero, and J. E. T. Segovia, Fractal Dimension for Fractal Structures: With Applications to Finance, SEMA SIMAI Springer Series, Springer Cham, 1 ed., 2019, <https://doi.org/10.1007/978-3-030-16645-8>, <10.1007/978-3-030-16645-8>.
* [24]

  D. Fudenberg, P. Strack, and T. Strzalecki, Speed, accuracy, and the optimal timing of choices, American Economic Review, 108 (2018), p. 3651–84, <https://doi.org/10.1257/aer.20150742>.
* [25]

  M. Fukasawa, B. Horvath, and P. Tankov, Hedging under rough volatility, in Rough Volatility, C. Bayer, P. K. Friz, M. Fukasawa, J. Gatheral, A. Jacquier, and M. Rosenbaum, eds., Society for Industrial and Applied Mathematics, Philadelphia, PA, 2023, ch. 6, pp. 115–125, <https://doi.org/10.1137/1.9781611977783.ch6>.
* [26]

  X. Gabaix, Behavioral inattention, in Handbook of Behavioral Economics - Foundations and Applications 2, B. D. Bernheim, S. DellaVigna, and D. Laibson, eds., vol. 2 of Handbook of Behavioral Economics: Applications and Foundations 1, North-Holland, 2019, ch. 4, pp. 261–343, <https://doi.org/10.1016/bs.hesbe.2018.11.001>.
* [27]

  J. Gatheral, T. Jaisson, and M. Rosenbaum, Volatility is rough, Quantitative Finance, 18 (2018), pp. 933–949.
* [28]

  J. Gatheral, T. Jaisson, and M. Rosenbaum, Volatility is rough, in Rough Volatility, C. Bayer, P. K. Friz, M. Fukasawa, J. Gatheral, A. Jacquier, and M. Rosenbaum, eds., Society for Industrial and Applied Mathematics, Philadelphia, PA, 2023, ch. 1, pp. 1–29, <https://doi.org/10.1137/1.9781611977783.ch1>.
* [29]

  P. Guasoni, Y. Mishura, and M. Rásonyi, High-frequency trading with fractional brownian motion, Finance and Stochastics, 25 (2021), pp. 277–310, <https://doi.org/10.1007/s00780-020-00439-y>.
* [30]

  P. Guasoni, Z. Nika, and M. Rásonyi, Trading fractional brownian motion, SIAM Journal on Financial Mathematics, 10 (2019), pp. 769–789, <https://doi.org/10.1137/17M113592X>.
* [31]

  S. M. S. Halkiewicz, Rundown of fractal reinterpretation of market charts, in Przykłady Zastosowania Narzędzi Analitycznych, ze Szczególnym Uwzględnieniem…, Attyka, 2024.
  Available at <https://www.researchgate.net/publication/382906687>.
* [32]

  R. Jarrow and P. Protter, Liquidity suppliers and high frequency trading, SIAM Journal on Financial Mathematics, 6 (2015), pp. 189–200, <https://doi.org/10.1137/140967702>.
* [33]

  S. Kakinaka, T. Hayakawa, D. Kato, and K. Umeno, Fractal portfolio strategies: does scale preference of investors matter?, Applied Economics Letters, 32 (2025), pp. 415–421, <https://doi.org/10.1080/13504851.2023.2274298>.
* [34]

  J. Kallsen and J. Muhle-Karbe, Option pricing and hedging with small transaction costs, Mathematical Finance, 25 (2015), pp. 702–723, <https://doi.org/10.1111/mafi.12035>.
* [35]

  S. Kim, C. Lee, W. Lee, S. Kwak, D. Jeong, and J. Kim, Nonuniform finite difference scheme for the three-dimensional time-fractional black–scholes equation, Journal of Function Spaces, 2021 (2021), p. 9984473, <https://doi.org/https://doi.org/10.1155/2021/9984473>.
* [36]

  R. Korn, Optimal Portfolios: Stochastic Models for Optimal Investment and Risk Management in Continuous Time, World Scientific, 1998.
* [37]

  L. Kristoufek, Fractal markets hypothesis and the global financial crisis: Wavelet power evidence, Scientific Reports, 3 (2013), p. 2857, <https://doi.org/10.1038/srep02857>, <10.1038/srep02857>.
* [38]

  A. S. Kyle, Continuous auctions and insider trading, Econometrica, 53 (1985), pp. 1315–1335.
* [39]

  G. Liu, C.-P. Yu, S.-N. Shiu, and I.-T. Shih, The efficient market hypothesis and the fractal market hypothesis: Interfluves, fusions, and evolutions, Sage Open, 12 (2022), p. 21582440221082137, <https://doi.org/10.1177/21582440221082137>.
* [40]

  R. Liu and J. Muhle-Karbe, Portfolio selection with small transaction costs and binding portfolio constraints, SIAM Journal on Financial Mathematics, 4 (2013), pp. 203–227, <https://doi.org/10.1137/120885036>, <10.1137/120885036>.
* [41]

  T. Lux, The multi-fractal model of asset returns: Its estimation via gmm and its use for volatility forecasting, Economics Working Papers 2003-13, Christian-Albrechts-University of Kiel, Department of Economics, 2003, <https://ideas.repec.org/p/zbw/cauewp/1123.html>.
* [42]

  M. J. P. Magill and G. M. Constantinides, Portfolio selection with transactions costs, Journal of Economic Theory, 13 (1976), pp. 245–263, <https://doi.org/10.1016/0022-0531(76)90018-1>.
* [43]

  B. B. Mandelbrot, The variation of some other speculative prices, The Journal of Business, 40 (1967), pp. 393–413, <http://www.jstor.org/stable/2351623> (accessed 2025-10-28).
* [44]

  B. B. Mandelbrot, Fractals and Scaling in Finance: Discontinuity, Concentration, Risk, Springer New York, 1997, <https://doi.org/10.1007/978-1-4757-2763-0>.
* [45]

  B. B. Mandelbrot and J. W. V. Ness, Fractional brownian motions, fractional noises and applications, SIAM Review, 10 (1968), pp. 422–437, <http://www.jstor.org/stable/2027184> (accessed 2025-10-28).
* [46]

  R. N. Mantegna and H. E. Stanley, Introduction to Econophysics: Correlations and Complexity in Finance, Cambridge University Press, 1999, <https://doi.org/10.1017/CBO9780511755767>.
* [47]

  Y. Mishura, Stochastic Calculus for Fractional Brownian Motion and Related Processes, Springer Berlin, Heidelberg, 2008, <https://doi.org/10.1017/CBO9780511755767>.
* [48]

  A. A. Obizhaeva and J. Wang, Optimal trading strategy and supply/demand dynamics, Journal of Financial Markets, 16 (2013), pp. 1–32, <https://doi.org/10.1016/j.finmar.2012.09.001>.
* [49]

  E. E. Peters, Fractal Market Analysis: Applying Chaos Theory to Investment and Economics, John Wiley & Sons, 1994.
* [50]

  S. E. Shreve and H. M. Soner, Optimal investment and consumption with transaction costs, Annals of Applied Probability, 4 (1994), pp. 609–692, <https://doi.org/10.1214/aoap/1177004966>.
* [51]

  C. A. Sims, Implications of rational inattention, Journal of Monetary Economics, 50 (2003), pp. 665–690, <https://doi.org/10.1016/S0304-3932(03)00029-1>.
  Swiss National Bank/Study Center Gerzensee Conference on Monetary Policy under Incomplete Information.
* [52]

  D. Sornette, Why Stock Markets Crash: Critical Events in Complex Financial Systems, Princeton University Press, revised ed., 2017, <http://www.jstor.org/stable/j.ctt1h1htkg> (accessed 2025-10-28).
* [53]

  M. Taksar, M. Klass, and D. Assaf, Diffusion models for the optimal investing and consumption problem, Mathematics of Operations Research, 13 (1988), pp. 277–294.
* [54]

  S. K. Verma and S. Kumar, Fractal dimension analysis of financial performance of resulting companies after mergers and acquisitions, Chaos, Solitons & Fractals, 181 (2024), p. 114683, <https://doi.org/10.1016/j.chaos.2024.114683>.
* [55]

  X. Wu, L. Zhang, J. Li, and R. Yan, Fractal statistical measure and portfolio model optimization under power-law distribution, The North American Journal of Economics and Finance, 58 (2021), p. 101496, <https://doi.org/10.1016/j.najef.2021.101496>.
* [56]

  W. Wyss, The fractional black–scholes equation, Fractional Calculus and Applied Analysis, 3 (2000), pp. 51–61.
* [57]

  H. Zhang, M. Zhang, F. Liu, and M. Shen, Review of the fractional black-scholes equations and their solution techniques, Fractal and Fractional, 8 (2024), <https://doi.org/10.3390/fractalfract8020101>.

## Appendix A Proofs of Main Results

### A.1 Proof of Proposition [5.6](https://arxiv.org/html/2510.24467v1#S5.Thmtheorem6 "Proposition 5.6 (Strict unimodality and uniqueness). ‣ 5.3 Sufficient conditions for uniqueness ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding") (Strict Unimodality and Uniqueness)

###### Proof A.1.

Recall that Rm=Am−2m​s¯−LmR\_{m}=A\_{m}-2^{m}\bar{s}-L\_{m} with Am=2m​ΦmA\_{m}=2^{m}\Phi\_{m}.
By Assumption [2](https://arxiv.org/html/2510.24467v1#Thmassumption2 "Assumption 2 (Regularity). ‣ 5.3 Sufficient conditions for uniqueness ‣ 5 Optimization of Trading Frequency ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"), AmA\_{m} is strictly concave in the discrete sense,
Δ2​Am:=Am+2−2​Am+1+Am<0\Delta^{2}A\_{m}:=A\_{m+2}-2A\_{m+1}+A\_{m}<0,
and LmL\_{m} is convex and nondecreasing.

Define the forward difference

|  |  |  |
| --- | --- | --- |
|  | Δ​Rm:=Rm+1−Rm=(Am+1−Am)−(2m+1−2m)​s¯−(Lm+1−Lm)=Δ​Am−2m​s¯−Δ​Lm.\Delta R\_{m}:=R\_{m+1}-R\_{m}=(A\_{m+1}-A\_{m})-(2^{m+1}-2^{m})\bar{s}-(L\_{m+1}-L\_{m})=\Delta A\_{m}-2^{m}\bar{s}-\Delta L\_{m}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | Δ​Rm+1−Δ​Rm=(Δ​Am+1−Δ​Am)−(2m+1−2m)​s¯−(Δ​Lm+1−Δ​Lm).\Delta R\_{m+1}-\Delta R\_{m}=(\Delta A\_{m+1}-\Delta A\_{m})-(2^{m+1}-2^{m})\bar{s}-(\Delta L\_{m+1}-\Delta L\_{m}). |  |

Each term on the right-hand side can be signed using the assumptions:

* •

  Δ​Am+1−Δ​Am=Δ2​Am<0\Delta A\_{m+1}-\Delta A\_{m}=\Delta^{2}A\_{m}<0 because AmA\_{m} is strictly concave.
* •

  (2m+1−2m)​s¯=2m​s¯>0(2^{m+1}-2^{m})\bar{s}=2^{m}\bar{s}>0 since s¯>0\bar{s}>0.
* •

  Δ​Lm+1−Δ​Lm≥0\Delta L\_{m+1}-\Delta L\_{m}\geq 0 because LmL\_{m} is convex and nondecreasing.

Hence every summand is nonpositive, with at least one being strictly negative, so

|  |  |  |
| --- | --- | --- |
|  | Δ​Rm+1−Δ​Rm<0for all ​m.\Delta R\_{m+1}-\Delta R\_{m}<0\qquad\text{for all }m. |  |

Therefore {Δ​Rm}\{\Delta R\_{m}\} is a strictly decreasing sequence.

Because Δ​Rm\Delta R\_{m} decreases strictly, it can cross zero at most once.
If Δ​Rm>0\Delta R\_{m}>0 for all mm, then RmR\_{m} would diverge to +∞+\infty,
contradicting the fact that 2m​s¯+Lm2^{m}\bar{s}+L\_{m} grows without bound.
Hence Δ​Rm\Delta R\_{m} must become negative for sufficiently large mm.
Let

|  |  |  |
| --- | --- | --- |
|  | m⋆:=min⁡{m:Δ​Rm≤0}.m^{\star}:=\min\{m:\Delta R\_{m}\leq 0\}. |  |

Then Δ​Rm>0\Delta R\_{m}>0 for all m<m⋆m<m^{\star} and Δ​Rm<0\Delta R\_{m}<0 for all m>m⋆m>m^{\star}.
Consequently RmR\_{m} increases strictly up to m⋆m^{\star} and decreases strictly thereafter,
so {Rm}\{R\_{m}\} is strictly unimodal, and the maximizer m⋆m^{\star} is unique.

### A.2 Proof of Theorem [6.3](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem3 "Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")

###### Proof A.2.

First-order condition.
Treat Δ>0\Delta>0 as a continuous decision variable and differentiate

|  |  |  |
| --- | --- | --- |
|  | R​(Δ)=κ​T​ΔH−1−T​s¯Δ−LR(\Delta)=\kappa T\,\Delta^{\,H-1}\;-\;\frac{T\,\bar{s}}{\Delta}\;-\;L |  |

with respect to Δ\Delta. The derivative is

|  |  |  |
| --- | --- | --- |
|  | R′​(Δ)=κ​T​(H−1)​ΔH−2+T​s¯​Δ−2.R^{\prime}(\Delta)=\kappa T\,(H-1)\,\Delta^{\,H-2}\;+\;T\bar{s}\,\Delta^{-2}. |  |

Setting R′​(Δ)=0R^{\prime}(\Delta)=0 for an optimum gives

|  |  |  |
| --- | --- | --- |
|  | κ​T​(H−1)​ΔH−2+T​s¯​Δ−2=0.\kappa T\,(H-1)\,\Delta^{\,H-2}+T\bar{s}\,\Delta^{-2}=0. |  |

Dividing through by T>0T>0 and rearranging,

|  |  |  |
| --- | --- | --- |
|  | κ​(H−1)​ΔH=−s¯⟹κ​(1−H)​ΔH=s¯.\kappa(H-1)\Delta^{\,H}=-\,\bar{s}\quad\Longrightarrow\quad\kappa(1-H)\Delta^{\,H}=\bar{s}. |  |

Hence the stationary point satisfies

|  |  |  |
| --- | --- | --- |
|  | Δ⋆=(s¯κ​(1−H))1/H,\Delta^{\star}=\Bigg(\frac{\bar{s}}{\,\kappa(1-H)\,}\Bigg)^{\!1/H}, |  |

which is positive for 0<H<10<H<1 since (1−H)>0(1-H)>0.

Second-order condition.
Differentiate R′​(Δ)R^{\prime}(\Delta) again to obtain

|  |  |  |
| --- | --- | --- |
|  | R′′​(Δ)=κ​T​(H−1)​(H−2)​ΔH−3−2​T​s¯​Δ−3.R^{\prime\prime}(\Delta)=\kappa T\,(H-1)(H-2)\,\Delta^{\,H-3}-2\,T\bar{s}\,\Delta^{-3}. |  |

Using the first-order relation κ​(1−H)​ΔH=s¯\kappa(1-H)\Delta^{H}=\bar{s}
to substitute for s¯\bar{s} at Δ=Δ⋆\Delta=\Delta^{\star} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | R′′​(Δ⋆)\displaystyle R^{\prime\prime}(\Delta^{\star}) | =κ​T​(H−1)​(H−2)​Δ⋆H−3−2​T​κ​(1−H)​Δ⋆H−3\displaystyle=\kappa T\,(H-1)(H-2)\,\Delta\_{\star}^{\,H-3}-2T\kappa(1-H)\,\Delta\_{\star}^{\,H-3} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =κ​T​Δ⋆H−3​[(H−1)​(H−2)−2​(1−H)]\displaystyle=\kappa T\,\Delta\_{\star}^{\,H-3}\!\big[(H-1)(H-2)-2(1-H)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =κ​T​Δ⋆H−3​H​(H−1).\displaystyle=\kappa T\,\Delta\_{\star}^{\,H-3}\,H(H-1). |  |

For 0<H<10<H<1, we have H​(H−1)<0H(H-1)<0, and since
κ,T,Δ⋆H−3>0\kappa,T,\Delta\_{\star}^{\,H-3}>0, it follows that
R′′​(Δ⋆)<0R^{\prime\prime}(\Delta^{\star})<0. Therefore the stationary point is a local maximum.

Uniqueness.
As Δ→0+\Delta\to 0^{+}, R​(Δ)→−∞R(\Delta)\to-\infty because the term
−T​s¯/Δ-T\bar{s}/\Delta dominates.
As Δ→∞\Delta\to\infty, R​(Δ)→−LR(\Delta)\to-L since
ΔH−1→0\Delta^{H-1}\to 0 for H<1H<1.
Moreover R′​(Δ)R^{\prime}(\Delta) is continuous and changes sign exactly once:
for small Δ\Delta, R′​(Δ)>0R^{\prime}(\Delta)>0; for large Δ\Delta, R′​(Δ)<0R^{\prime}(\Delta)<0.
Hence there is a unique root of R′​(Δ)=0R^{\prime}(\Delta)=0, namely Δ⋆\Delta^{\star},
and this root corresponds to a global maximum.

In summary, the expected profit function R​(Δ)R(\Delta)
is maximized uniquely at

|  |  |  |
| --- | --- | --- |
|  | Δ⋆=(s¯κ​(1−H))1/H,\boxed{\displaystyle\Delta^{\star}=\Bigg(\frac{\bar{s}}{\kappa(1-H)}\Bigg)^{1/H}}, |  |

which satisfies R′′​(Δ⋆)<0R^{\prime\prime}(\Delta^{\star})<0 for 0<H<10<H<1.

### A.3 Proof of Corollary [6.5](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem5 "Corollary 6.5 (Fractal comparative statics). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding")

###### Proof A.3.

From Theorem [6.3](https://arxiv.org/html/2510.24467v1#S6.Thmtheorem3 "Theorem 6.3 (Optimal trading interval). ‣ 6.3 Optimal rebalancing interval ‣ 6 Stochastic Extension via Fractional Brownian Motion ‣ The Omniscient yet Lazy InvestorSubmitted to the editors DATE. \fundingThe author has not received any funding"), the optimal interval satisfies

|  |  |  |
| --- | --- | --- |
|  | Δ⋆=(s¯κ​(1−H))1/H,0<H<1.\Delta^{\star}=\Bigg(\frac{\bar{s}}{\kappa(1-H)}\Bigg)^{1/H},\qquad 0<H<1. |  |

Taking logarithms gives

|  |  |  |
| --- | --- | --- |
|  | ln⁡Δ⋆=1H​[ln⁡s¯−ln⁡κ−ln⁡(1−H)].\ln\Delta^{\star}=\frac{1}{H}\Big[\ln\bar{s}-\ln\kappa-\ln(1-H)\Big]. |  |

Partial derivatives with respect to parameters.
Differentiate ln⁡Δ⋆\ln\Delta^{\star} with respect to each variable.

(a) Execution cost s¯\bar{s}.

|  |  |  |
| --- | --- | --- |
|  | ∂ln⁡Δ⋆∂s¯=1H​s¯⟹∂Δ⋆∂s¯=Δ⋆H​s¯>0.\frac{\partial\ln\Delta^{\star}}{\partial\bar{s}}=\frac{1}{H\bar{s}}\quad\Longrightarrow\quad\frac{\partial\Delta^{\star}}{\partial\bar{s}}=\frac{\Delta^{\star}}{H\bar{s}}>0. |  |

Thus higher proportional frictions lead to a larger optimal interval,
i.e., less frequent trading.

(b) Scaling parameter κ\kappa.

|  |  |  |
| --- | --- | --- |
|  | ∂ln⁡Δ⋆∂κ=−1H​κ⟹∂Δ⋆∂κ=−Δ⋆H​κ<0.\frac{\partial\ln\Delta^{\star}}{\partial\kappa}=-\,\frac{1}{H\kappa}\quad\Longrightarrow\quad\frac{\partial\Delta^{\star}}{\partial\kappa}=-\,\frac{\Delta^{\star}}{H\kappa}<0. |  |

Hence a higher exploitable‐return scale κ\kappa
reduces the optimal interval and increases trading frequency.

(c) Hurst exponent HH.
Differentiating with respect to HH gives

|  |  |  |
| --- | --- | --- |
|  | ∂ln⁡Δ⋆∂H=−1H2​[ln⁡s¯−ln⁡κ−ln⁡(1−H)]−1H​(1−H).\frac{\partial\ln\Delta^{\star}}{\partial H}=-\frac{1}{H^{2}}\big[\ln\bar{s}-\ln\kappa-\ln(1-H)\big]\;-\;\frac{1}{H(1-H)}. |  |

The second term is strictly negative for 0<H<10<H<1,
and the first term is dominated by it in magnitude for typical parameter values.
Hence ∂Δ⋆/∂H<0\partial\Delta^{\star}/\partial H<0,
so higher HH (smoother paths) imply larger optimal intervals and lower frequency.

Relation to fractal dimension.
Since the Hausdorff dimension of fractional Brownian motion is D=2−HD=2-H,
we have

|  |  |  |
| --- | --- | --- |
|  | ∂Δ⋆∂D=−∂Δ⋆∂H<0.\frac{\partial\Delta^{\star}}{\partial D}=-\,\frac{\partial\Delta^{\star}}{\partial H}<0. |  |

Thus more fractal (rougher) price paths - corresponding to larger DD or smaller HH - lead to smaller optimal intervals Δ⋆\Delta^{\star}, i.e., more frequent trading.

Collecting signs,

|  |  |  |
| --- | --- | --- |
|  | ∂Δ⋆∂D<0,∂Δ⋆∂s¯>0,∂Δ⋆∂κ<0,\frac{\partial\Delta^{\star}}{\partial D}<0,\qquad\frac{\partial\Delta^{\star}}{\partial\bar{s}}>0,\qquad\frac{\partial\Delta^{\star}}{\partial\kappa}<0, |  |

as claimed.