---
authors:
- Tarun Chitra
- Nagu Thogiti
- Mauricio Jean Pieer Trujillo Ramirez
- Victor Xu
doc_id: arxiv:2602.15182v1
family_id: arxiv:2602.15182
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Autodeleveraging as Online Learning
url_abs: http://arxiv.org/abs/2602.15182v1
url_html: https://arxiv.org/html/2602.15182v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tarun Chitra
  
Nagu Thogiti
  
Mauricio Jean Pieer Trujillo Ramirez
  
Victor Xu

(February 2026)

###### Abstract

Autodeleveraging (ADL) is a last-resort loss socialization mechanism used by perpetual futures venues when liquidation and insurance buffers are insufficient to restore solvency.
Despite the scale of perpetual futures markets, ADL has received limited formal treatment as a sequential control problem.
This paper provides a concise formalization of ADL as online learning on a PNL-haircut domain: at each round, the venue selects a solvency budget and a set of profitable trader accounts.
The profitable accounts are liquidated to cover shortfalls up to the solvency budget, with the aim of recovering exchange-wide solvency.
In this model, ADL haircuts apply to positive PNL (unrealized gains), not to posted collateral principal.
Using our online learning model, we provide robustness results and theoretical upper bounds on how poorly a mechanism can perform at recovering solvency.
We apply our model to the October 10, 2025 Hyperliquid stress episode.
The regret caused by Hyperliquid’s production ADL queue is about 50% of an upper bound on regret, calibrated to this event, while our optimized algorithm achieves about 2.6% of the same bound.
In dollar terms, the production ADL model over liquidates trader profits by up to $51.7M.
We also counterfactually evaluated algorithms inspired by our online learning framework that perform better and found that the best algorithm reduces overshoot to $3M.
Our results provide simple, implementable mechanisms for improving ADL in live perpetuals exchanges.

## 1 Introduction

Perpetual futures (or simply, perpetuals) are expiryless derivatives that provide linear, delta-one exposure to an underlying asset with margin instead of full notional outlay.
Economically, they are close to contracts for difference (CFDs): participants exchange value as marks move, rather than exchanging the underlying asset itself.
This design is why perpetuals are both simple to reason about and capital-efficient for directional risk transfer, and it explains their dominance in crypto derivatives trading [[1](https://arxiv.org/html/2602.15182v1#bib.bib13 "Short communication: a primer on perpetuals")].
In 2024, centralized exchanges processed roughly $58.5T in perpetuals notional versus roughly $17.4T in spot volume, a ratio of about 3.3x in favor of perpetuals [[6](https://arxiv.org/html/2602.15182v1#bib.bib17 "State of crypto perpetuals 2024"), [5](https://arxiv.org/html/2602.15182v1#bib.bib18 "2025 q1 crypto industry report")].

Perpetuals are popular because traders can scale exposure linearly with leverage while avoiding duration risk (e.g. contract roll schedules).
But the absence of expiry does not remove risk; it changes how risk must be managed.
In particular, perpetuals replace expiry settlement with continuous margining and funding-rate transfers, so both traders and the venue must manage solvency continuously rather than only at settlement checkpoints.

#### Risk Management.

Compared to dated futures, collateral management in perpetuals is more path-dependent.
Dated futures clear at expiry and have standard variation margin cycles, whereas perpetuals remain open indefinitely and use funding payments to tether perpetual future prices to spot.
A positive funding rate transfers value from longs to shorts, while a negative rate reverses the direction.
This creates a carry cost (or carry income) that forces users to actively manage leverage, holding horizon, and basis exposure over time [[1](https://arxiv.org/html/2602.15182v1#bib.bib13 "Short communication: a primer on perpetuals")].

Risk management needs to be viewed from both the microeconomic (trader) perspective and the macroeconomic perspective of the exchange.
At the trader level, solvency means a position’s assets exceed its liabilities, which is enforced by margin requirements, liquidations, and funding transfers.
At the venue level, solvency means aggregate trader claims remain supportable at the exchange level.
We formalize this in §[2](https://arxiv.org/html/2602.15182v1#S2 "2 Background ‣ Autodeleveraging as Online Learning").

#### Residual Loss Management.

It is possible for venue-level risk management to fail, leading to a net insolvency.
When an exchange is in such an insolvent state, traders cannot withdraw their full collateral and earned profits.
Define the exchange’s shortfall as the positive gap between exchange liabilities and exchange assets.
Residual loss management in the face of insolvencies involves two options for resolving how much traders can withdraw from the exchange: how much of that shortfall does the exchange cover immediately, and which traders bears those losses.
This separation is useful because two venues can cover the same shortfall (in dollar terms) while inducing very different fairness and incentive outcomes depending on how the burden is allocated.

Traditional finance has analogous machinery in the form of central clearing parties (CCPs).
CCP utilize techniques such as default waterfalls and variation-margin gains haircutting (VMGH) to allocate residual losses across surviving members under predefined rules [[11](https://arxiv.org/html/2602.15182v1#bib.bib14 "Does a central clearing counterparty reduce counterparty risk?"), [7](https://arxiv.org/html/2602.15182v1#bib.bib15 "Principles for financial market infrastructures")].
Some allocations are approximately proportional to exposure or gains, while others are layered by membership class, collateral seniority, or administrative uplift rules, which is explicitly non-pro-rata in burden [[12](https://arxiv.org/html/2602.15182v1#bib.bib16 "2022 credit workshop: congestion revenue rights (crr)")].
Perpetuals venues face the same design problem under faster time constraints and thinner legal settlement buffers due to the bearer asset nature of cryptocurrencies.

#### Autodeleveraging.

Autodeleveraging (ADL) is an algorithmic form of residual loss management: the venue enforces a deterministic rule to reduce profits from winning positions, utilizing these seized profits to close a shortfall in real time.
Operationally, this is a positive-PNL haircut: a winner can lose part of unrealized gains while posted collateral principal remains protected.
In most traditional finance settings, residual losses are reconciled asynchronously through legal and institutional processes after the event.
For bearer, self-custodied crypto systems, delayed discretionary recovery is often infeasible and solvency restoration must be executable by rule at event time.

ADL directly implements both parts of residual-loss design: *severity* (how much shortfall is covered now) and *allocation* (which winners are deleveraged first and by how much).
While there are numerous allocation rules that can be used to implement ADL, two rules dominate: the rules used by the exchanges Binance and Hyperliquid.
Binance-style ADL uses a queue priority based on profitability and leverage to rank who is deleveraged first [[3](https://arxiv.org/html/2602.15182v1#bib.bib2 "What is auto-deleveraging (adl) and how does it work?")].
Hyperliquid publishes deterministic liquidation and ADL logic in venue documentation and executes these transitions on a publicly readable state machine [[16](https://arxiv.org/html/2602.15182v1#bib.bib19 "Liquidations")].
When residual losses occur repeatedly, usage of ADL can naturally be formulated as an online decision problem: each round reveals realized shortfall and market state, a policy chooses an allocation, and performance is measured by cumulative regret against benchmark policies.
To our knowledge, formal analysis of this problem is still sparse, with the paper [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")] providing the most complete treatment to date giving an ADL trilemma and a broader mechanism space than production queue rules.

#### October 10, 2025.

The October 10–11, 2025 stress episode is the key empirical motivation for this paper.
Contemporaneous reporting describes one of the largest liquidation cascades in crypto derivatives and broad ADL activation across major venues, including Hyperliquid and Binance [[18](https://arxiv.org/html/2602.15182v1#bib.bib6 "’Largest ever’ crypto liquidation event wipes out 6,300 wallets on hyperliquid"), [3](https://arxiv.org/html/2602.15182v1#bib.bib2 "What is auto-deleveraging (adl) and how does it work?")].
The critical difference for measurement is observability: Binance is centralized, so researchers do not get a fully auditable public state for each ADL decision, while Hyperliquid exposes enough public state to reconstruct event-time mechanics in detail.

Using the public Hyperliquid reconstruction artifacts, the event spans 21:16–21:27 UTC on October 10, 2025, with $2,103,111,431 in observed liquidations.
One can view roughly 16 iterative instances of ADL usage over that duration.
ADL, historically, was designed as a last resort mechanism that is only used a once to recover solvency as opposed to being used sequentially.
A natural series of questions arise: How do we analyze the impact of such repeated usage of ADL? Does the mechanism increase or reduce solvency upon iterated usage? What is the optimal policy for repeated ADL usage?

#### This paper.

We formalize repeated ADL as an online decision problem over rounds and evaluate a two-term objective that can be measured from public replay data: tracking error and burden concentration.
We then analyze this objective theoretically and empirically with dynamic regret.
Relative to [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], our contributions are:

* •

  an explicit public-data observation model and clear replay assumptions for policy comparison,
* •

  regret-based evaluation focused on deployable policy classes (with ex post reference policies reported separately),
* •

  queue-stability diagnostics linked to convex extreme-point instability (monotonicity violations and adjacent-round rank stability),
* •

  an execution-price estimation extension that separates ex ante and ex post benchmarks and yields a bound on cumulative execution-induced failure VTV\_{T}.

Formally, we show that fixed-priority queues can incur linear regret, while adaptive controllers for the same objective can achieve sublinear regret.
We also analyze robustness under execution-price uncertainty.
Relative to [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], our key theoretical addition is an explicit severity-variation term PTθP\_{T}^{\theta}, which links regret to ex ante/ex post execution mismatch and closeout-liquidity instability.
This directly addresses critique points about benchmark interpretation, timing of available information, and execution sensitivity raised in [[22](https://arxiv.org/html/2602.15182v1#bib.bib9 "Autodeleveraging, hyperliquid, and the $653m debate"), [21](https://arxiv.org/html/2602.15182v1#bib.bib10 "ADL trilemma, assumption j.3, and dan robinson’s critique and tarun’s paper fixes"), [23](https://arxiv.org/html/2602.15182v1#bib.bib11 "Beyond queues — understanding auto-deleveraging from first principles")].

On the empirical side, under an explicit public-data replay model for October 10, 2025, we find that Hyperliquid’s production ADL policy overshoots by between $45.0M and $51.7M.
We compare observed performance to an instance-calibrated regret bound from Proposition [1](https://arxiv.org/html/2602.15182v1#Thmproposition1 "Proposition 1 (Deficit-weighted severity bound with explicit constants). ‣ 3.8 Basic regret bound for the objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
Using this calibrated scale, production reaches about 50.0%50.0\% of the bound.
Our no-regret online algorithm is vector mirror descent (using only start-of-round information), which reaches about 3.4%3.4\% of the same bound.
Our analysis improves the empirical analysis of [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], where the authors did not explicitly compare empirical performance to theory.

## 2 Background

### 2.1 Perpetuals exchanges and funding mechanics

A *perpetuals futures exchange* is a derivatives venue that allows traders to take leveraged long or short exposure to a continuous, expiryless futures contract.
Traders post collateral (margin) to keep positions solvent, and the venue uses a funding-rate transfer between longs and shorts to keep futures prices aligned with spot.

Each trader ii has an account and we denote the set of active accounts at time tt by ℐt\mathcal{I}\_{t}.
For each account ii, let their signed position size be qi,tq\_{i,t}.
An account i∈ℐti\in\mathcal{I}\_{t} if qi,t≠0q\_{i,t}\neq 0.
Similarly, let the mark price be mtm\_{t}, and index/spot reference be sts\_{t} at time tt.
The distinction between mtm\_{t} and sts\_{t} is operationally important.
The index/spot reference sts\_{t} is an external anchor (typically a composite spot index), while the mark mtm\_{t} is the venue’s internal fair-price input for margin and liquidation logic.
Funding is designed to control the basis mt−stm\_{t}-s\_{t}, but the two prices can diverge during stress.
Ignoring fees for notation, one-step price PNL is Δ​PNLi,tprice=qi,t​(mt−mt−1)\Delta\mathrm{PNL}\_{i,t}^{\mathrm{price}}=q\_{i,t}(m\_{t}-m\_{t-1}).
Perpetuals additionally include funding transfers to keep futures and spot aligned. A reduced-form update is Δ​PNLi,tfund=−ft​qi,t​mt\Delta\mathrm{PNL}\_{i,t}^{\mathrm{fund}}=-f\_{t}\,q\_{i,t}\,m\_{t},
where ftf\_{t} is signed funding (positive values transfer from longs to shorts).
The total PNL increment is therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​PNLi,t=Δ​PNLi,tprice+Δ​PNLi,tfund,PNLi,t:=∑τ≤tΔ​PNLi,τ.\Delta\mathrm{PNL}\_{i,t}=\Delta\mathrm{PNL}\_{i,t}^{\mathrm{price}}+\Delta\mathrm{PNL}\_{i,t}^{\mathrm{fund}},\qquad\mathrm{PNL}\_{i,t}:=\sum\_{\tau\leq t}\Delta\mathrm{PNL}\_{i,\tau}. |  | (1) |

We note that this view of PNL accounting follows [[1](https://arxiv.org/html/2602.15182v1#bib.bib13 "Short communication: a primer on perpetuals"), [15](https://arxiv.org/html/2602.15182v1#bib.bib27 "Fundamentals of perpetual futures")].

### 2.2 Assets, liabilities, and solvency

For each position 𝔭i,t\mathfrak{p}\_{i,t}, we use the same balance-sheet convention as the full model: trader assets are posted collateral and trader liabilities are the negative of PNL. Formally,
Ai,ttr=ci,tA^{\mathrm{tr}}\_{i,t}=c\_{i,t} and Li,ttr=−PNLi,tL^{\mathrm{tr}}\_{i,t}=-\mathrm{PNL}\_{i,t},
so trader equity is
ei,t=Ai,ttr−Li,ttr=ci,t+PNLi,te\_{i,t}=A^{\mathrm{tr}}\_{i,t}-L^{\mathrm{tr}}\_{i,t}=c\_{i,t}+\mathrm{PNL}\_{i,t}.
This matches the standard interpretation: if PNLi,t<0\mathrm{PNL}\_{i,t}<0, the account owes the venue; if PNLi,t>0\mathrm{PNL}\_{i,t}>0, the venue owes the account.

At the venue level, exchange assets and liabilities are aggregates of trader-side quantities:
Atx=∑i∈ℐtAi,ttrA\_{t}^{x}=\sum\_{i\in\mathcal{I}\_{t}}A\_{i,t}^{\mathrm{tr}} and Ltx=∑i∈ℐtLi,ttrL\_{t}^{x}=\sum\_{i\in\mathcal{I}\_{t}}L\_{i,t}^{\mathrm{tr}}.
Therefore exchange solvency is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Atx≥Ltx⟺𝖲𝗈𝗅𝗏t​(𝒫t)=Atx−Ltx≥0.A\_{t}^{x}\geq L\_{t}^{x}\quad\Longleftrightarrow\quad\mathsf{Solv}\_{t}(\mathcal{P}\_{t})=A\_{t}^{x}-L\_{t}^{x}\geq 0. |  | (2) |

Using the position-level equity definition above, this becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖲𝗈𝗅𝗏t​(𝒫t)=∑𝔭∈𝒫tet​(𝔭)=∑i∈ℐtei,t.\mathsf{Solv}\_{t}(\mathcal{P}\_{t})=\sum\_{\mathfrak{p}\in\mathcal{P}\_{t}}e\_{t}(\mathfrak{p})=\sum\_{i\in\mathcal{I}\_{t}}e\_{i,t}. |  | (3) |

An exchange is insolvent when 𝖲𝗈𝗅𝗏t​(𝒫t)≤0\mathsf{Solv}\_{t}(\mathcal{P}\_{t})\leq 0. Equivalently, the exchange-level residual shortfall is
So St=(−𝖲𝗈𝗅𝗏t​(𝒫t))+S\_{t}=\big(-\mathsf{Solv}\_{t}(\mathcal{P}\_{t})\big)\_{+}.
When St>0S\_{t}>0, the venue must either socialize losses (ADL), inject external capital, or remain undercollateralized.

### 2.3 Liquidations

When a user’s equity approaches zero, the venue liquidates some or all of the position.
We denote by Δ​qi,t\Delta q\_{i,t} the amount of trader ii’s position that is liquidated at time tt, with Δ​qi,t≤qi,t\Delta q\_{i,t}\leq q\_{i,t}.
For this paper, only three prices matter:

* •

  pbk​(𝔭i,t)p^{\mathrm{bk}}(\mathfrak{p}\_{i,t}): bankruptcy price, defined as the mark price mtm\_{t} such that ei,t=0e\_{i,t}=0.
* •

  pliq​(𝔭i,t)p^{\mathrm{liq}}(\mathfrak{p}\_{i,t}): liquidation trigger price, typically tied to maintenance margin.
* •

  pliq,exec​(𝔭i,t,Δ​qi,t)p^{\mathrm{liq,exec}}(\mathfrak{p}\_{i,t},\Delta q\_{i,t}): realized order-book execution price for the liquidation trade.

The precise algorithms for liquidation vary from venue to venue.
These details are elided here as we focus on what happens when these algorithms fail.
We say that a liquidation fails and creates bad debt when execution is worse than bankruptcy:

* •

  Long closeout: shortfall if pliq,exec<pbkp^{\mathrm{liq,exec}}<p^{\mathrm{bk}}.
* •

  Short closeout: shortfall if pliq,exec>pbkp^{\mathrm{liq,exec}}>p^{\mathrm{bk}}.

We note that liquidations may be full (Δ​qi,t=qi,t\Delta q\_{i,t}=q\_{i,t}) or partial (Δ​qi,t<qi,t\Delta q\_{i,t}<q\_{i,t}).

### 2.4 Exchange risk management

In practice, solvency enforcement is complex because the exchange generally cannot always liquidate positions at the mark price mtm\_{t}.
For instance, if the order book on an exchange has less liquidity than Δ​qi,t\Delta q\_{i,t}, then the liquidation cannot be fully executed.
The transaction costs of risk reduction are nondeterministic and depend on factors such as liquidity depth, market impact, order book elasticity, and the execution strategy employed.

When approaching the solvency boundary (i.e. when bad debt occurs), the key region is where positions appear solvent at mark price but not at expected liquidation execution price.
A standard response is partial liquidation up to the bankruptcy boundary, with ADL used for any remaining deficit.

#### Why real-time deterministic socialization is common in crypto venues.

Compared with traditional clearing ecosystems, crypto perpetual venues operate with 24/7 markets, global pseudonymous membership, rapid withdrawal optionality, and limited ex post legal netting capacity.
When a stress event occurs, delayed discretionary recovery can trigger immediate run risk because users can attempt to exit collateral before losses are allocated.
Deterministic rule-based ADL therefore acts as an operational commitment device: losses are allocated at event time under public rules instead of relying on subsequent legal reconciliation.

### 2.5 Positions and exchange position set

An exchange is defined by a set of *positions* that represent user accounts.
We define a per user account position object, 𝔭i,t=(qi,t,p¯i,t,ci,t,PNLi,t,ei,t)\mathfrak{p}\_{i,t}=\big(q\_{i,t},\bar{p}\_{i,t},c\_{i,t},\mathrm{PNL}\_{i,t},e\_{i,t}\big):
where qi,tq\_{i,t} is signed contract size, p¯i,t\bar{p}\_{i,t} is average entry basis, ci,tc\_{i,t} is posted collateral, PNLi,t\mathrm{PNL}\_{i,t} is mark-to-market profit and loss, and ei,te\_{i,t} is account equity.
The set of active positions at round tt is 𝒫t={𝔭i,t:i∈ℐt}\mathcal{P}\_{t}=\{\mathfrak{p}\_{i,t}:i\in\mathcal{I}\_{t}\}.

### 2.6 Insolvency and deficits

Let Lt⊆ℐtL\_{t}\subseteq\mathcal{I}\_{t} be accounts with negative expected equity following liquidation.
The deficit at round tt is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt=∑j∈Lt(−ej,t​(pliq,exec​(𝔭j,t,qj,t)))+.D\_{t}=\sum\_{j\in L\_{t}}(-e\_{j,t}(p^{\mathrm{liq,exec}}(\mathfrak{p}\_{j,t},q\_{j,t})))\_{+}. |  | (4) |

We abuse notation and refer to ej,t​(pliq,exec​(𝔭j,t,qj,t))e\_{j,t}(p^{\mathrm{liq,exec}}(\mathfrak{p}\_{j,t},q\_{j,t})) as the trader’s equity if their PNL was computed with the mark price mt=pliq,execm\_{t}=p^{\mathrm{liq,exec}}.
The deficit represents the total negative equity in the system and represents the notional value of positions that need to be closed to preserve solvency.

Next, define the winner set Wt={i∈ℐt:𝔭i,t∈𝒫t,PNLi,t>0}W\_{t}=\{i\in\mathcal{I}\_{t}:\mathfrak{p}\_{i,t}\in\mathcal{P}\_{t},\ \mathrm{PNL}\_{i,t}>0\}, with PNL haircut capacity ui,t=(PNLi,t)+u\_{i,t}=(\mathrm{PNL}\_{i,t})\_{+} and Ut=∑i∈Wtui,tU\_{t}=\sum\_{i\in W\_{t}}u\_{i,t}.
The capacity UtU\_{t} is the maximum amount of profit that can be haircut to cover the deficit DtD\_{t}.
This paper uses strict PNL-only haircuts: ADL reallocates positive PNL and does not haircut protected collateral.
In particular, each account-level seizure satisfies 0≤xi,t≤ui,t0\leq x\_{i,t}\leq u\_{i,t}, so aggregate budget can only come from positive PNL capacity.
If Dt>0D\_{t}>0 and St<0S\_{t}<0, liquidation alone cannot restore solvency and the venue must socialize losses, inject outside capital, or remain undercollateralized.

## 3 Autodeleveraging

We formulate autodeleveraging (ADL) as a sequential online decision problem: each round reveals a state, the venue chooses a feasible action, losses are realized, and the system transitions under unknown dynamics.
This follows canonical online learning and reinforcement learning formulations [[24](https://arxiv.org/html/2602.15182v1#bib.bib20 "Online convex programming and generalized infinitesimal gradient ascent"), [14](https://arxiv.org/html/2602.15182v1#bib.bib21 "Introduction to online convex optimization"), [20](https://arxiv.org/html/2602.15182v1#bib.bib22 "Reinforcement learning: an introduction")].

### 3.1 ADL Rounds

Operationally, upon realizing a reference price sts\_{t} that causes Dt>0D\_{t}>0, the venue executes a sequence of operations: attempt liquidation, absorb residual bad debt with insurance when available, and finally, invoke ADL on winners if deficits remain.
In this paper, a *round* is a defined as a contiguous sequence of order book fills created by an ADL algorithm.
That is, a round consists of the set of negative equity positions that are closed by matching with order book positions under a single execution of an ADL algorithm.
While ADL was initially constructed on the assumption that it would be used for a single round, October 10, 2025 demonstrated that this is not true in extreme stress scenarios.

### 3.2 Lifecycle of an ADL Round

A single ADL round has an execution lifecycle that separates severity choice (i.e. how much of the negative equity should be socialized) from allocation and matching (i.e. who should cover the negative equity positions).
First, the venue measures residual loser-side deficit DtD\_{t} and chooses a budget to socialized, BtB\_{t} (or equivalently chooses θt∈(0,1)\theta\_{t}\in(0,1) and sets Bt=θt​DtB\_{t}=\theta\_{t}D\_{t}).
Determining severity is the core of the ADL problem because required ADL transfer sizes qkADLq\_{k}^{\mathrm{ADL}} are endogenous to liquidation outcomes: negative equity positions that are closed cross the order book at uncertain liquidation prices pkliq,execp\_{k}^{\mathrm{liq,exec}}.
These prices are unknown ex ante and must be estimated in live ADL policies.
Second, the ADL policy chooses winner-side reductions xi,tx\_{i,t} (e.g. queue, pro-rata, or another policy).
Third, ADL matches winners (positive equity positions) and losers (negative equity positions to be closed) at the bankruptcy transfer price pkbkp\_{k}^{\mathrm{bk}} of the loser (deterministic given the marked state).
Figure [2](https://arxiv.org/html/2602.15182v1#A1.F2 "Figure 2 ‣ A.1 Empirical workflow ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning") summarizes this lifecycle and where the benchmark BtneededB\_{t}^{\mathrm{needed}} is measured.

### 3.3 Haircut Benchmark

For an ADL transfer kk in round tt, let pkliq,execp\_{k}^{\mathrm{liq,exec}} be realized liquidation execution price, pkbkp\_{k}^{\mathrm{bk}} the bankruptcy transfer price used by ADL matching, and qkADLq\_{k}^{\mathrm{ADL}} the signed ADL transfer quantity.
In live operation, liquidation execution prices are not known ex ante, so the venue uses an estimator p^kliq,exec\hat{p}\_{k}^{\mathrm{liq,exec}} and an implied estimated quantity q^kADL\hat{q}\_{k}^{\mathrm{ADL}}.
These quantities are used to estimate what fraction of the deficit will be covered by ADL (i.e. severity).
A natural benchmark for estimating the shortfall covered is the expected budget to socialize via ADL:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B^tneeded=∑k∈t|p^kliq,exec−pkbk|​|q^kADL|.\widehat{B}\_{t}^{\mathrm{needed}}=\sum\_{k\in t}\left|\hat{p}\_{k}^{\mathrm{liq,exec}}-p\_{k}^{\mathrm{bk}}\right|\,|\hat{q}\_{k}^{\mathrm{ADL}}|. |  | (5) |

This can be interpreted as the ADL algorithm’s ex ante estimate of the shortfall covered in one ADL round.
Note that because it can only realize pliq,execp^{\mathrm{liq,exec}} ex post, we also need to compare to the realized, ex post benchmark:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Btneeded=∑k∈t|pkliq,exec−pkbk|​|qkADL|.B\_{t}^{\mathrm{needed}}=\sum\_{k\in t}\left|p\_{k}^{\mathrm{liq,exec}}-p\_{k}^{\mathrm{bk}}\right|\,|q\_{k}^{\mathrm{ADL}}|. |  | (6) |

But note that live, online ADL algorithms cannot directly use BtneededB\_{t}^{\mathrm{needed}}; it will only be a benchmark for theoretical analysis.

#### Units and interpretation.

Most quantities in this paper are dollar-valued (for example DtD\_{t}, BtneededB\_{t}^{\mathrm{needed}}, and HtH\_{t}), so reported losses and totals are in dollars.
The main unitless quantity is severity θt∈[0,1]\theta\_{t}\in[0,1], defined by Bt=θt​DtB\_{t}=\theta\_{t}D\_{t}, which is the fraction of the observed deficit socialized in round tt.
Over- and under-socialization are then dollar gaps between HtH\_{t} and BtneededB\_{t}^{\mathrm{needed}}.

### 3.4 State, action, and policy spaces

Let rounds be indexed by t=1,…,Tt=1,\dots,T.
Using the position-set notation from §[2](https://arxiv.org/html/2602.15182v1#S2 "2 Background ‣ Autodeleveraging as Online Learning"), define state space 𝒮\mathcal{S} and action space 𝒜\mathcal{A} as follows.

#### State.

Round state is st=(𝒫t,Dt,Wt,ut,ζt)∈𝒮s\_{t}=\big(\mathcal{P}\_{t},D\_{t},W\_{t},u\_{t},\zeta\_{t}\big)\in\mathcal{S}, where 𝒫t\mathcal{P}\_{t} is the exchange position set, DtD\_{t} is residual deficit, WtW\_{t} is the winner index set, and ut=(ui,t)i∈Wtu\_{t}=(u\_{i,t})\_{i\in W\_{t}} are winner capacities.
Here ζt\zeta\_{t} is an auxiliary vector of round-start, policy-observable market signals (e.g., price and volatility snapshots, spread/depth summaries, and recent liquidation-flow aggregates).

#### Action.

An ADL action is at=(Bt,xt)∈𝒜​(st)a\_{t}=(B\_{t},x\_{t})\in\mathcal{A}(s\_{t}), with aggregate budget BtB\_{t} and allocation vector xt=(xi,t)i∈Wtx\_{t}=(x\_{i,t})\_{i\in W\_{t}}.
The feasible action set is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜​(st)={(B,x): 0≤B≤Ut, 0≤xi≤ui,t,∑i∈Wtxi=B}.\mathcal{A}(s\_{t})=\left\{(B,x):\ 0\leq B\leq U\_{t},\ 0\leq x\_{i}\leq u\_{i,t},\ \sum\_{i\in W\_{t}}x\_{i}=B\right\}. |  | (7) |

Equivalent parameterization uses severity θt∈[0,1]\theta\_{t}\in[0,1] and haircut fractions hi,t∈[0,1]h\_{i,t}\in[0,1]: Bt=θt​Dt,xi,t=hi,t​(ui,t+ε)B\_{t}=\theta\_{t}D\_{t},\ x\_{i,t}=h\_{i,t}(u\_{i,t}+\varepsilon).
Here ε>0\varepsilon>0 is a small numerical regularizer (in the same units as ui,tu\_{i,t} and DtD\_{t}) used only to avoid divide-by-zero or near-zero denominators in normalized ratios (e.g., xi,t/(ui,t+ε)x\_{i,t}/(u\_{i,t}+\varepsilon) and θtneeded=Btneeded/(Dt+ε)\theta\_{t}^{\mathrm{needed}}=B\_{t}^{\mathrm{needed}}/(D\_{t}+\varepsilon)).

#### Policy.

An ADL policy is a history-dependent map πt:ℋt→𝒜​(st)\pi\_{t}:\mathcal{H}\_{t}\to\mathcal{A}(s\_{t}), with ℋt=(s1,a1,…,st−1,at−1,st)\mathcal{H}\_{t}=(s\_{1},a\_{1},\dots,s\_{t-1},a\_{t-1},s\_{t}).
State transitions follow unknown stochastic dynamics st+1=Ft​(st,at,ωt)s\_{t+1}=F\_{t}(s\_{t},a\_{t},\omega\_{t}) with shock ωt\omega\_{t}.

### 3.5 Canonical policy examples

There are two high-level ADL policy families used in practice and analysis: queue-based policies and partial haircut policies.

#### Queue-based Policies.

Queueing policies first choose a score si,ts\_{i,t} for each winner, then order positions by score, then close positions in that order.
Formally, if σt\sigma\_{t} is a permutation that orders the scores, i.e.
sσt​(1),t≥⋯≥sσt​(|Wt|),t,s\_{\sigma\_{t}(1),t}\geq\cdots\geq s\_{\sigma\_{t}(|W\_{t}|),t},
then queue allocation greedily fills budget BtB\_{t}: top-ranked accounts are fully closed, with xσt​(j),t=uσt​(j),tx\_{\sigma\_{t}(j),t}=u\_{\sigma\_{t}(j),t}.
That is, if i⋆=min⁡{j:∑i=1jxσt​(i),t≥Bt}i^{\star}=\min\{j:\sum\_{i=1}^{j}x\_{\sigma\_{t}(i),t}\geq B\_{t}\}, then positions σt​(1),…,σt​(i∗−1)\sigma\_{t}(1),\ldots,\sigma\_{t}(i^{\*}-1) are fully closed while σt​(i∗)\sigma\_{t}(i^{\*}) is partially closed.
This structure can produce 100%100\% haircuts for early queue positions.

#### Partial Haircut Policies.

Partial haircut policies distribute round budget across winners so no touched account is fully closed during ADL.
Writing hi,t=xi,t/(ui,t+ε)h\_{i,t}=x\_{i,t}/(u\_{i,t}+\varepsilon), these policies enforce hi,t<1h\_{i,t}<1 for participating winners (equivalently, a hard cap hi,t≤h¯<1h\_{i,t}\leq\bar{h}<1).
This avoids queue-style full closeout of a position and smooths the burden across accounts due to the budget constraint.

*Pro-Rata Policy.*
The quintessential partial haircut policy is pro-rata.
This policy allocates proportionally to positive-PNL capacity: xi,tPR=ui,tUt​Btx^{\mathrm{PR}}\_{i,t}=\frac{u\_{i,t}}{U\_{t}}\,B\_{t}.
This equalizes haircut fraction xi,t/ui,tx\_{i,t}/u\_{i,t} across winners and is the canonical fairness benchmark.
In the full model, this benchmark is additionally motivated by axiomatic fairness: under Sybil resistance, scale invariance, and monotonicity, capped pro-rata is the unique stable allocation family [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")].
Moreover, multiple live protocols utilize this rule in practice (e.g. Drift and Paradex) [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")].

*Min-max Integer Linear Program (ILP).*
In practice, perpetuals exchanges represent contracts (e.g.,  user positions) as integer counts.
For instance, a single contract might represent a position of size 0.1 BTC.
To ensure that such integrality constraints are met, the pro-rata policy is modified to a rounding integer linear program.
This program minimizes worst-account burden subject to exact budget and lot-feasible execution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minx,z⁡zs.t.∑i∈Wtxi=Bt, 0≤xi≤ui,t,xiui,t+ε≤z,xi∈𝒢i,t,\min\_{x,z}\ z\quad\text{s.t.}\quad\sum\_{i\in W\_{t}}x\_{i}=B\_{t},\ \ 0\leq x\_{i}\leq u\_{i,t},\ \ \frac{x\_{i}}{u\_{i,t}+\varepsilon}\leq z,\ \ x\_{i}\in\mathcal{G}\_{i,t}, |  | (8) |

where 𝒢i,t\mathcal{G}\_{i,t} is the contract integral constant for account ii.
We note that in [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], it was shown that the empirical rounding error from using the ILP (versus pro-rata) can add up to millions of dollars in practice.

### 3.6 Per-round optimization objective

Each round requires two linked choices: severity (how much budget BtB\_{t} to raise) and allocation (how to split BtB\_{t} across winners).
As such, objective should penalize both solvency-tracking error and how concentrated haircuts are.
A natural asymmetric round loss is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ~t​(xt)=λunder​[Btneeded−Ht]++λover​[Ht−Btneeded]++λfair​Γt​(xt,ut),\tilde{\ell}\_{t}(x\_{t})=\lambda\_{\mathrm{under}}[B\_{t}^{\mathrm{needed}}-H\_{t}]\_{+}+\lambda\_{\mathrm{over}}[H\_{t}-B\_{t}^{\mathrm{needed}}]\_{+}+\lambda\_{\mathrm{fair}}\,\Gamma\_{t}(x\_{t},u\_{t}), |  | (9) |

where Ht=∑ixi,tH\_{t}=\sum\_{i}x\_{i,t} and Γt\Gamma\_{t} is a concentration functional.
The undershoot and overshoot terms encode solvency-tracking asymmetry, while Γt\Gamma\_{t} captures how fairly losses are divided amongst users.

For online control and empirical comparability under partial observability, we deploy the convex surrogate

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt​(xt)=λtrack​|Ht−Btneeded|+λfair​maxi∈Wt⁡xi,tui,t+ε.\ell\_{t}(x\_{t})=\lambda\_{\mathrm{track}}\left|H\_{t}-B\_{t}^{\mathrm{needed}}\right|+\lambda\_{\mathrm{fair}}\max\_{i\in W\_{t}}\frac{x\_{i,t}}{u\_{i,t}+\varepsilon}. |  | (10) |

The fairness proxy is the largest fraction of available positive PNL seized from any winner, which matches the burden-concentration diagnostic used in policy evaluation.
Equivalently, writing hi,t=xi,t/(ui,t+ε)h\_{i,t}=x\_{i,t}/(u\_{i,t}+\varepsilon), the objective penalizes maxi⁡hi,t\max\_{i}h\_{i,t}: this is a worst-hit-participant criterion and corresponds to the min–max burden objective used in our ILP benchmark (Appendix [C.1](https://arxiv.org/html/2602.15182v1#A3.SS1 "C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")).
As both terms are convex on the feasible polytope (see Appendix [C.1](https://arxiv.org/html/2602.15182v1#A3.SS1 "C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")), we can solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt∈arg⁡minx∈𝒳t⁡ℓt​(x),𝒳t={x:∃Bt​s.t.​(Bt,x)∈𝒜​(st)}.x\_{t}\in\arg\min\_{x\in\mathcal{X}\_{t}}\ell\_{t}(x),\qquad\mathcal{X}\_{t}=\{x:\exists B\_{t}\ \text{s.t.}\ (B\_{t},x)\in\mathcal{A}(s\_{t})\}. |  | (11) |

*Tracking-versus-allocation decomposition.*
Under exact budget execution, feasibility enforces Ht=∑ixi,t=BtH\_{t}=\sum\_{i}x\_{i,t}=B\_{t}, so |Ht−Btneeded|=|Bt−Btneeded|\left|H\_{t}-B\_{t}^{\mathrm{needed}}\right|=\left|B\_{t}-B\_{t}^{\mathrm{needed}}\right|.
However, this implies that if there is positive tracking error, then it is because the severity (i.e.,  the budget) was chosen incorrectly.
We note that the tracking error is primarily driven by the choice of severity, whereas queue/pro-rata choice primarily affects burden allocation (the fairness term).
In practice, additional tracking error can still arise from integral constraints, partial fills/latency, and ex-ante execution-price estimation error.

### 3.7 Static and Dynamic Regret

We use standard online-learning definitions of static and dynamic regret [[24](https://arxiv.org/html/2602.15182v1#bib.bib20 "Online convex programming and generalized infinitesimal gradient ascent"), [14](https://arxiv.org/html/2602.15182v1#bib.bib21 "Introduction to online convex optimization"), [19](https://arxiv.org/html/2602.15182v1#bib.bib23 "Understanding machine learning: from theory to algorithms"), [2](https://arxiv.org/html/2602.15182v1#bib.bib24 "Non-stationary stochastic optimization")].
We connect these to instance-dependent guarantees that scale with realized gradient magnitude or loss curvature rather than horizon alone [[10](https://arxiv.org/html/2602.15182v1#bib.bib25 "Adaptive subgradient methods for online learning and stochastic optimization"), [13](https://arxiv.org/html/2602.15182v1#bib.bib26 "A second-order bound with excess losses")].
For a policy sequence π={xt}t=1T\pi=\{x\_{t}\}\_{t=1}^{T}, static regret is

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTstatic​(π)=∑t=1Tℓt​(xt)−minx∈𝒳​∑t=1Tℓt​(x),\mathrm{Reg}^{\mathrm{static}}\_{T}(\pi)=\sum\_{t=1}^{T}\ell\_{t}(x\_{t})-\min\_{x\in\mathcal{X}}\sum\_{t=1}^{T}\ell\_{t}(x), |  | (12) |

and dynamic regret against comparator sequence {xt⋆}\{x\_{t}^{\star}\} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn​(π)=∑t=1Tℓt​(xt)−∑t=1Tℓt​(xt⋆).\mathrm{Reg}^{\mathrm{dyn}}\_{T}(\pi)=\sum\_{t=1}^{T}\ell\_{t}(x\_{t})-\sum\_{t=1}^{T}\ell\_{t}(x\_{t}^{\star}). |  | (13) |

For empirical claims, we make the comparator class explicit.
Let 𝒫\mathcal{P} be the implementable policy library used in replay.
Policy-class regret is

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegT𝒫​(π)=∑t=1Tℓt​(xtπ)−minπ′∈𝒫​∑t=1Tℓt​(xtπ′).\mathrm{Reg}^{\mathcal{P}}\_{T}(\pi)=\sum\_{t=1}^{T}\ell\_{t}(x\_{t}^{\pi})-\min\_{\pi^{\prime}\in\mathcal{P}}\sum\_{t=1}^{T}\ell\_{t}(x\_{t}^{\pi^{\prime}}). |  | (14) |

We also isolate scalar tracking regret:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTtrack​(π)=∑t=1T|Htπ−Btneeded|−minπ′∈𝒫​∑t=1T|Htπ′−Btneeded|.\mathrm{Reg}^{\mathrm{track}}\_{T}(\pi)=\sum\_{t=1}^{T}\left|H\_{t}^{\pi}-B\_{t}^{\mathrm{needed}}\right|-\min\_{\pi^{\prime}\in\mathcal{P}}\sum\_{t=1}^{T}\left|H\_{t}^{\pi^{\prime}}-B\_{t}^{\mathrm{needed}}\right|. |  | (15) |

Terminology is fixed throughout:
*tracking error* means |Ht−Btneeded|\left|H\_{t}-B\_{t}^{\mathrm{needed}}\right|,
*overshoot* means [Ht−Btneeded]+[H\_{t}-B\_{t}^{\mathrm{needed}}]\_{+},
and *undershoot* means [Btneeded−Ht]+[B\_{t}^{\mathrm{needed}}-H\_{t}]\_{+}.
Finally, for objective diagnostics we use

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛttrack=λtrack​|Ht−Btneeded|,ℛtfairness=λfair​maxi∈Wt⁡xi,tui,t+ε,ℛttotal=ℛttrack+ℛtfairness.\mathcal{R}\_{t}^{\mathrm{track}}=\lambda\_{\mathrm{track}}\left|H\_{t}-B\_{t}^{\mathrm{needed}}\right|,\quad\mathcal{R}\_{t}^{\mathrm{fairness}}=\lambda\_{\mathrm{fair}}\max\_{i\in W\_{t}}\frac{x\_{i,t}}{u\_{i,t}+\varepsilon},\quad\mathcal{R}\_{t}^{\mathrm{total}}=\mathcal{R}\_{t}^{\mathrm{track}}+\mathcal{R}\_{t}^{\mathrm{fairness}}. |  | (16) |

### 3.8 Basic regret bound for the objective

For the objective ([9](https://arxiv.org/html/2602.15182v1#S3.E9 "In 3.6 Per-round optimization objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning")) in this paper, the tightest and most interpretable bound is the one-dimensional severity result below.
This result upper bounds the regret in terms of the deficit and the variation of the severity.

###### Proposition 1 (Deficit-weighted severity bound with explicit constants).

Consider the one-dimensional severity parameterization Bt=θt​DtB\_{t}=\theta\_{t}D\_{t}, θt∈[0,1]\theta\_{t}\in[0,1], with loss ℓtθ(θt)=Dt|θt−θtneeded|,,θtneeded=min{1,BtneededDt+ε}\ell\_{t}^{\theta}(\theta\_{t})=D\_{t}\left|\theta\_{t}-\theta\_{t}^{\mathrm{needed}}\right|,,\theta\_{t}^{\mathrm{needed}}=\min\!\left\{1,\frac{B\_{t}^{\mathrm{needed}}}{D\_{t}+\varepsilon}\right\}
Let comparator path variation be PTθ=∑t=2T|θt⋆−θt−1⋆|P\_{T}^{\theta}=\sum\_{t=2}^{T}\left|\theta\_{t}^{\star}-\theta\_{t-1}^{\star}\right|.
Projected OGD on [0,1][0,1] with step η>0\eta>0 satisfies
RegTdyn,θ≤1+2​PTθ2​η+η2​∑t=1TDt2,\mathrm{Reg}^{\mathrm{dyn},\theta}\_{T}\leq\frac{1+2P\_{T}^{\theta}}{2\eta}\;+\;\frac{\eta}{2}\sum\_{t=1}^{T}D\_{t}^{2},
since |∂ℓtθ|≤Dt|\partial\ell\_{t}^{\theta}|\leq D\_{t}.
With
η⋆=(1+2​PTθ)/∑tDt2\eta^{\star}=\sqrt{(1+2P\_{T}^{\theta})/\sum\_{t}D\_{t}^{2}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn,θ≤(1+2​PTθ)​∑t=1TDt2.\mathrm{Reg}^{\mathrm{dyn},\theta}\_{T}\leq\sqrt{(1+2P\_{T}^{\theta})\sum\_{t=1}^{T}D\_{t}^{2}}. |  | (17) |

This bound has an intuitive two-factor form.
∑tDt2\sum\_{t}D\_{t}^{2} captures event scale: larger deficits make the episode harder to reduce for any policy.
PTθP\_{T}^{\theta} captures how quickly target severity moves across rounds.
In ADL, this variation is larger when exchanges mispredict ex post liquidation execution prices (forcing repeated severity corrections) and when closeout liquidity is poor (execution outcomes become more unstable round to round).
So the same mechanism can have low regret in calm, predictable episodes and much higher regret in bursty, illiquid cascades even at similar notional scale.
Relative to prior ADL analysis in [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], this explicit PTθP\_{T}^{\theta} term makes the execution and liquidity costs visible in the bound itself.
In this sense, the bound is instance-calibrated: since the per-round slope is |∂ℓtθ|≤Dt|\partial\ell\_{t}^{\theta}|\leq D\_{t}, the rate depends on ∑tDt2\sqrt{\sum\_{t}D\_{t}^{2}}, analogous to adaptive/second-order OCO bounds [[10](https://arxiv.org/html/2602.15182v1#bib.bib25 "Adaptive subgradient methods for online learning and stochastic optimization"), [13](https://arxiv.org/html/2602.15182v1#bib.bib26 "A second-order bound with excess losses")].
This is exactly the lens used in §[5](https://arxiv.org/html/2602.15182v1#S5 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning") to interpret October 10.
Full proofs are in Appendix [B](https://arxiv.org/html/2602.15182v1#A2 "Appendix B Regret Bounds and Proofs ‣ Autodeleveraging as Online Learning").

## 4 Regret Minimization

This section analyzes regret minimization for the ADL objective ([9](https://arxiv.org/html/2602.15182v1#S3.E9 "In 3.6 Per-round optimization objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning")).
We show why queue-based policies are structurally high-regret, characterize trade-offs among no-regret controllers, and connect these predictions to empirical diagnostics.

### 4.1 Why queue policies are structurally high-regret

Queue mechanisms impose a fixed ranking map and then allocate budget greedily.
In nonstationary episodes, ADL regret has two main channels: *tracking error* from severity mismatch (BtB\_{t} vs. BtneededB\_{t}^{\mathrm{needed}}) and *fairness error* from burden concentration.
The fixed queue map mainly drives the fairness error by repeatedly overloading top-ranked winners, while severity mistakes are amplified by rounding, partial fills, and execution uncertainty.
Hence queue policies are expected to accumulate regret quickly in clustered-stress episodes, as in October 10, 2025.
We first illustrate this explicitly with a single example.

#### Fixed queue policies can incur linear regret.

Consider two winning accounts i∈{1,2}i\in\{1,2\}, an exact round budget Bt=1B\_{t}=1, a feasible set
𝒳t={x∈ℝ+2:x1+x2=1, 0≤xi≤ui,t}\mathcal{X}\_{t}=\{x\in\mathbb{R}\_{+}^{2}:\ x\_{1}+x\_{2}=1,\ 0\leq x\_{i}\leq u\_{i,t}\},
and consider the fairness-only loss ℓt​(x)=λfair​maxi⁡xiui,t\ell\_{t}(x)=\lambda\_{\mathrm{fair}}\max\_{i}\frac{x\_{i}}{u\_{i,t}}.
Let capacities alternate with M>1M>1:

|  |  |  |
| --- | --- | --- |
|  | (u1,t,u2,t)={(1,M),t​odd,(M,1),t​even.(u\_{1,t},u\_{2,t})=\begin{cases}(1,M),&t\ \text{odd},\\ (M,1),&t\ \text{even}.\end{cases} |  |

Now impose a fixed queue that always serves account 11 first and greedily fills the full budget before considering account 22. Since u1,t≥1u\_{1,t}\geq 1 in every round, this queue always outputs xtqueue=(1,0)x\_{t}^{\mathrm{queue}}=(1,0).
Its per-round loss is then:

|  |  |  |
| --- | --- | --- |
|  | ℓt​(xtqueue)={λfair​max⁡{1, 0/M}=λfair,t​odd,λfair​max⁡{1/M, 0}=λfair/M,t​even.\ell\_{t}(x\_{t}^{\mathrm{queue}})=\begin{cases}\lambda\_{\mathrm{fair}}\max\{1,\ 0/M\}=\lambda\_{\mathrm{fair}},&t\ \text{odd},\\ \lambda\_{\mathrm{fair}}\max\{1/M,\ 0\}=\lambda\_{\mathrm{fair}}/M,&t\ \text{even}.\end{cases} |  |

A dynamic comparator that allocates to the higher-capacity account each round chooses

|  |  |  |
| --- | --- | --- |
|  | xt⋆={(0,1),t​odd,(1,0),t​even,x\_{t}^{\star}=\begin{cases}(0,1),&t\ \text{odd},\\ (1,0),&t\ \text{even},\end{cases} |  |

which yields ℓt​(xt⋆)=λfair/M\ell\_{t}(x\_{t}^{\star})=\lambda\_{\mathrm{fair}}/M in every round. Therefore, for even TT,

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn​(queue)=∑t=1T[ℓt​(xtqueue)−ℓt​(xt⋆)]=T2​λfair​(1−1M)=Ω​(T).\mathrm{Reg}^{\mathrm{dyn}}\_{T}(\mathrm{queue})=\sum\_{t=1}^{T}\left[\ell\_{t}(x\_{t}^{\mathrm{queue}})-\ell\_{t}(x\_{t}^{\star})\right]=\frac{T}{2}\lambda\_{\mathrm{fair}}\!\left(1-\frac{1}{M}\right)=\Omega(T). |  | (18) |

So even with exact budget tracking (x1,t+x2,t=Btx\_{1,t}+x\_{2,t}=B\_{t} each round), a fixed queue can accumulate linear fairness regret under alternating round geometry.

### 4.2 Estimation of pexecp^{\mathrm{exec}}: tracking failure beyond regret

In practice, regret is a coarse measurement that doesn’t account for how execution costs impact tracking error.
Execution costs can make realized severity too low to cover deficits.
In this section, we adapt our regret bounds to include execution-based failure modes.

#### Why execution-price estimation enters tracking.

As feasibility enforces Ht=∑i∈Wtxi,t=BtH\_{t}=\sum\_{i\in W\_{t}}x\_{i,t}=B\_{t}, within-round allocation does not by itself create tracking error.
Tracking error is mainly due to the choice of severity θt\theta\_{t}, which chooses Bt=θt​DtB\_{t}=\theta\_{t}D\_{t}.
Severity depends on ADL quantities qkADLq\_{k}^{\mathrm{ADL}}, which are only known ex post because they are induced by uncertain liquidation execution at price pkliq,execp\_{k}^{\mathrm{liq,exec}}.

#### Estimated versus ex post benchmarks.

Let Δ​pk,t​(q):=|pk,texec,liq​(q)−pk,tbk|\Delta p\_{k,t}(q):=|p^{\mathrm{exec,liq}}\_{k,t}(q)-p^{\mathrm{bk}}\_{k,t}|, where pbkp^{\mathrm{bk}} is the bankruptcy transfer price
used for matching. The ex post (policy-comparable) needed benchmark is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Btneeded:=∑k∈tΔ​pk,t​(qk,tA​D​L)​|qk,tADL|.B\_{t}^{\mathrm{needed}}:=\sum\_{k\in t}\Delta p\_{k,t}(q^{ADL}\_{k,t})\,|q\_{k,t}^{\mathrm{ADL}}|. |  | (19) |

In deployment, the venue does not know qk,tADLq\_{k,t}^{\mathrm{ADL}} when choosing severity and therefore uses q^k,tADL\hat{q}\_{k,t}^{\mathrm{ADL}} from p^k,tliq,exec​(⋅)\hat{p}^{\mathrm{liq,exec}}\_{k,t}(\cdot).
We analogously define Δ​p^k,t​(q):=|p^k,texec,liq​(q)−pk,tbk|\Delta\hat{p}\_{k,t}(q):=|\hat{p}^{\mathrm{exec,liq}}\_{k,t}(q)-p^{\mathrm{bk}}\_{k,t}| and

|  |  |  |  |
| --- | --- | --- | --- |
|  | B^tneeded:=∑k∈tΔ​p^k,t​(q^k,tA​D​L)​|q^k,tADL|.\widehat{B}\_{t}^{\mathrm{needed}}:=\sum\_{k\in t}\Delta\hat{p}\_{k,t}(\hat{q}^{ADL}\_{k,t})\,|\hat{q}\_{k,t}^{\mathrm{ADL}}|. |  | (20) |

An ADL mechanism aims to target Ht≈B^tneededH\_{t}\approx\widehat{B}\_{t}^{\mathrm{needed}} to reduce severity tracking error.

#### What is new in this separation.

Relative to [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], we explicitly separate the ex ante quantity used to make decisions (B^tneeded\widehat{B}\_{t}^{\mathrm{needed}}) from the ex post replay benchmark used for evaluation (BtneededB\_{t}^{\mathrm{needed}}).
This yields a sharper interpretation: regret against the ex ante target measures online control quality, while the ex ante/ex post gap isolates execution-model error and liquidity-driven mismatch.
This is intended as a direct correction to known measurement ambiguities discussed in public critiques [[22](https://arxiv.org/html/2602.15182v1#bib.bib9 "Autodeleveraging, hyperliquid, and the $653m debate"), [23](https://arxiv.org/html/2602.15182v1#bib.bib11 "Beyond queues — understanding auto-deleveraging from first principles")] of the first paper to formalize ADL [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")].

#### Ex post severity error.

When execution is underestimated, HtH\_{t} can fall short of BtneededB\_{t}^{\mathrm{needed}}, so we track this gap directly via

|  |  |  |  |
| --- | --- | --- | --- |
|  | VT:=∑t=1T[Btneeded−Ht]+,V\_{T}\;:=\;\sum\_{t=1}^{T}\big[B\_{t}^{\mathrm{needed}}-H\_{t}\big]\_{+}, |  | (21) |

which can be large even when regret is small.

#### Total Tracking Error Minimization.

We now consider a notion of total tracking error, which is the sum of regret and ex post severity error.
Let ℓt​(x;b)\ell\_{t}(x;b) denote the deployed convex surrogate with tracking target bb:

|  |  |  |
| --- | --- | --- |
|  | ℓt​(x;b):=λtrack​|𝟏⊤​x−b|+λfair​maxi∈Wt⁡xi,tui,t+ε.\ell\_{t}(x;b):=\lambda\_{\mathrm{track}}\,\big|{\bf 1}^{\top}x-b\big|+\lambda\_{\mathrm{fair}}\max\_{i\in W\_{t}}\frac{x\_{i,t}}{u\_{i,t}+\varepsilon}. |  |

In Appendix [D](https://arxiv.org/html/2602.15182v1#A4 "Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning"), we show that for any policy sequence π={xt}\pi=\{x\_{t}\} and comparator class 𝒫\mathcal{P}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1Tℓt​(xt)≤minπ′∈𝒫​∑t=1Tℓt​(xtπ′)+RegT𝒫​(π;ℓ^)⏟online control / optimization error+2​λtrack​∑t=1T|Btneeded−B^tneeded|⏟execution-estimation error.\sum\_{t=1}^{T}\ell\_{t}(x\_{t})\;\leq\;\min\_{\pi^{\prime}\in\mathcal{P}}\sum\_{t=1}^{T}\ell\_{t}(x^{\pi^{\prime}}\_{t})\;+\;\underbrace{\mathrm{Reg}^{\mathcal{P}}\_{T}(\pi;\hat{\ell})}\_{\text{online control / optimization error}}\;+\;\underbrace{2\lambda\_{\mathrm{track}}\sum\_{t=1}^{T}\big|B\_{t}^{\mathrm{needed}}-\widehat{B}\_{t}^{\mathrm{needed}}\big|}\_{\text{execution-estimation error}}. |  | (22) |

When Ht≈B^tneededH\_{t}\approx\widehat{B}\_{t}^{\mathrm{needed}}, ex post severity error scales with optimistic estimation error:
VT≲∑t=1T[Btneeded−B^tneeded]+V\_{T}\lesssim\sum\_{t=1}^{T}[B\_{t}^{\mathrm{needed}}-\widehat{B}\_{t}^{\mathrm{needed}}]\_{+}.
Appendix [D](https://arxiv.org/html/2602.15182v1#A4 "Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") gives the formal statement and proof of ([22](https://arxiv.org/html/2602.15182v1#S4.E22 "In Total Tracking Error Minimization. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning")).

#### Linear Impact Model.

To illustrate how queues can underperform other ADL mechanisms, we consider a simple linear price impact model for execution cost.
This model is stylized, but it clearly shows how estimation error can shift performance from sublinear to linear.

Our linear model assumes that at each time tt, ptliq,exec​(q)=pmark∓αt​qp^{\mathrm{liq,exec}}\_{t}(q)=p^{\mathrm{mark}}\mp\alpha\_{t}q, for an unknown local slope αt\alpha\_{t}.
Note that the sign of αt\alpha\_{t} is direction-dependent: use −- for liquidating long inventory (sell pressure lowers execution price) and ++ for liquidating short inventory (buy pressure raises execution price).
We assume that ex ante, prior to executing an ADL mechanism, the designer estimates a slope α^t\hat{\alpha}\_{t} and sets p^texec,liq​(q)=ptmark∓α^t​q\hat{p}^{\mathrm{exec,liq}}\_{t}(q)=p^{\mathrm{mark}}\_{t}\mp\hat{\alpha}\_{t}q.
Using equations ([20](https://arxiv.org/html/2602.15182v1#S4.E20 "In Estimated versus ex post benchmarks. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning")) and ([19](https://arxiv.org/html/2602.15182v1#S4.E19 "In Estimated versus ex post benchmarks. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning")), this implies that

|  |  |  |
| --- | --- | --- |
|  | Btneeded−B^tneeded≤∑k∈t|pk,texec,liq​(qk,tA​D​L)−p^k,texec,liq​(qk,tA​D​L)|​|qk,tA​D​L|=|αt−α^t|​(∑k∈t|qk,tA​D​L|2)B\_{t}^{\mathrm{needed}}-\hat{B}\_{t}^{\mathrm{needed}}\leq\sum\_{k\in t}|p^{\mathrm{exec,liq}}\_{k,t}(q\_{k,t}^{ADL})-\hat{p}^{\mathrm{exec,liq}}\_{k,t}(q\_{k,t}^{ADL})||q\_{k,t}^{ADL}|=|\alpha\_{t}-\hat{\alpha}\_{t}|\left(\sum\_{k\in t}|q\_{k,t}^{ADL}|^{2}\right) |  |

If for some Q>0Q>0, we have qk,tA​D​L≤Qq\_{k,t}^{ADL}\leq Q, then |Btneeded−B^tneeded|≤Q2​|αt−α^t|\left|B\_{t}^{\mathrm{needed}}-\hat{B}\_{t}^{\mathrm{needed}}\right|\leq Q^{2}|\alpha\_{t}-\hat{\alpha}\_{t}| round-wise.
This implies that, for example, if the mechanism estimates α^t\hat{\alpha}\_{t} such that |α^t−αt|=O​(1T)|\hat{\alpha}\_{t}-\alpha\_{t}|=O(\frac{1}{\sqrt{T}}), then VT=O​(T)V\_{T}=O(\sqrt{T}).
On the other hand, if for some C>0C>0, |αt−α^t|≥C|\alpha\_{t}-\hat{\alpha}\_{t}|\geq C, then VT=Ω​(T)V\_{T}=\Omega(T).
In Appendix [D](https://arxiv.org/html/2602.15182v1#A4 "Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning"), we formalize this in Proposition [10](https://arxiv.org/html/2602.15182v1#Thmproposition10 "Proposition 10 (Bounding 𝑉_𝑇 under a linear execution model). ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") and show that if the total estimation error ∑t|αt−α^t|\sum\_{t}|\alpha\_{t}-\hat{\alpha}\_{t}| is sufficiently smooth then we have sublinear regret.
Note that one can interpret this result as saying that an ADL mechanism can handle a constant number (in TT) of large misestimations and still have low severity tracking error.

### 4.3 Queue Instability

Given tracking errors, a natural question to ask is how robust ADL mechanisms are to perturbations.
We study this theoretically using convex analysis (Appendix [C](https://arxiv.org/html/2602.15182v1#A3 "Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")) and a linear impact feedback model (Appendix [D](https://arxiv.org/html/2602.15182v1#A4 "Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning")).
The main critique is not that queue allocation must always break immediate solvency restoration.
When budget execution is exact (Ht=BtH\_{t}=B\_{t}) and matching is fixed, immediate tracking is primarily a severity-choice question.
Queue failure instead appears through mechanism quality: discontinuity of the allocation map, rank instability under small perturbations, and strict dominance gaps under min–max burden objectives.
These are the channels used below and in Section [5](https://arxiv.org/html/2602.15182v1#S5 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning") to evaluate queue performance.

#### Linear Impact Model.

Under the linear impact model, Appendix [D](https://arxiv.org/html/2602.15182v1#A4 "Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") (Proposition [11](https://arxiv.org/html/2602.15182v1#Thmproposition11 "Proposition 11 (Queues induce Ω⁢(𝑇) effective execution nonstationarity under churn). ‣ D.5 A churn-robust instability result for queues ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning")) shows that a fixed queue ordering can create Ω​(T)\Omega(T) variation in effective liquidation conditions, even when accounts do not return once closed.
On the same sequence, smooth mixing policies keep this variation bounded.
The effect is indirect: allocation changes which winners are closed each round, which changes next-round state composition and can change later liquidation slopes.
In Section [5](https://arxiv.org/html/2602.15182v1#S5 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning"), replay keeps the realized market path fixed, so we do not estimate the size of this feedback effect; we leave that quantification to future work.

#### Convex Analysis.

In Appendix [C](https://arxiv.org/html/2602.15182v1#A3 "Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning"), we use convex geometry to demonstrate a similar lack of queue robustness.
We define a feasibility polytope that represents the set of feasible severities and allocations that can be chosen.
We show that queue mechanisms correspond to extreme points of this polytope.
This implies, in particular, that arbitrarily small changes in scores can lead to large changes in ADL allocation.
The empirical instability diagnostics in Section [5](https://arxiv.org/html/2602.15182v1#S5 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning") (monotonicity violations and adjacent-round rank stability) are intended to measure this convex geometric instability.

## 5 Empirical Analysis

We study the October 10, 2025 Hyperliquid stress event using public replay artifacts from [[8](https://arxiv.org/html/2602.15182v1#bib.bib4 "HyperMultiAssetedADL: hyperliquid liquidation replay")], canonical event data from [[9](https://arxiv.org/html/2602.15182v1#bib.bib5 "HyperReplay: canonical 10/10 event data"), [17](https://arxiv.org/html/2602.15182v1#bib.bib12 "Autodeleveraging-analysis")].
The 21:16–21:27 UTC window contains about $2.103B in liquidations and decomposes into T=16T=16 ADL rounds using the methodology of [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")].
This clustered-round structure is the empirical motivation for online evaluation.
Unless stated otherwise, empirical counts are reported at the canonical ADL-event level rather than per-user or per-fill derived rows.

#### Observation model and replay invariants.

Claims are made under a public-data observation model, not full internal-ledger reconstruction.
Across counterfactual policies, replay holds fixed round boundaries, loser deficits DtD\_{t}, winner sets WtW\_{t}, winner capacities ui,tu\_{i,t}, the observable round-start context ζt\zeta\_{t}, bankruptcy transfer prices pkbkp\_{k}^{\mathrm{bk}}, and the realized market price path.
Policy differences therefore enter through severity and allocation, not through re-labeling the round state.

#### What is not modeled.

We do not model policy feedback into liquidation behavior, order-book resilience, HLP/market-maker participation, strategic order placement, or withdrawals during the event.
Results should therefore be interpreted as partial-equilibrium policy comparisons on a fixed realized path, not as a full market-equilibrium simulation.

#### Markout horizon and economic interpretation.

As in [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], we use markout to estimate the counterfactual value of a position closed by ADL.
The horizon parameter Δ\Delta is swept from immediate to short-horizon evaluation windows.
Economically, this captures plausible unwind-value uncertainty in stressed books rather than a single point estimate.

#### Policy classes and information sets.

We evaluate production Hyperliquid queue, integer pro-rata, continuous pro-rata, vector mirror descent, and min-max ILP under the same replay rounds.
Deployable policies (production queue, integer pro-rata, vector mirror descent) use only round-start inputs.
Ex post reference policies (continuous pro-rata, min-max ILP) use realized replay quantities unavailable at decision time and are reported only as reference lower bounds.

For policy π\pi, define the round-level concentration ratio mtπ:=maxi∈Wt⁡xi,tπui,t+εm\_{t}^{\pi}:=\max\_{i\in W\_{t}}\frac{x\_{i,t}^{\pi}}{u\_{i,t}+\varepsilon}.
In the empirical decomposition, we report

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt,empλ​(π)=|Htπ−Btneeded|+λ​Btneeded​|mtπ−mtILP|,\ell\_{t,\mathrm{emp}}^{\lambda}(\pi)=\left|H\_{t}^{\pi}-B\_{t}^{\mathrm{needed}}\right|\;+\;\lambda\,B\_{t}^{\mathrm{needed}}\left|m\_{t}^{\pi}-m\_{t}^{\mathrm{ILP}}\right|, |  | (23) |

where mtILPm\_{t}^{\mathrm{ILP}} is the min–max ILP reference concentration on the same replay round.

#### Metric glossary.

We report cumulative objective value Lλ​(π)=∑tℓt,empλ​(π)L^{\lambda}(\pi)=\sum\_{t}\ell\_{t,\mathrm{emp}}^{\lambda}(\pi), its tracking and fairness components T​(π)T(\pi) and F​(π)F(\pi), and policy-class regret only when explicitly labeled.

### 5.1 Empirical Objective and Regret Diagnostics

The falsifiable prediction is that, on fixed replay rounds with fixed state trajectory, adaptive/smoother policies achieve lower cumulative tracking and fairness components than queue baselines.
We tested this on the October 10 replay data, and the results ranked policies as predicted, with Hyperliquid’s production queue the worst performer (Table [2](https://arxiv.org/html/2602.15182v1#A1.T2 "Table 2 ‣ A.3 Regret decomposition ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), Figures [8](https://arxiv.org/html/2602.15182v1#A1.F8 "Figure 8 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), [7](https://arxiv.org/html/2602.15182v1#A1.F7 "Figure 7 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), and [4](https://arxiv.org/html/2602.15182v1#A1.F4 "Figure 4 ‣ A.3 Regret decomposition ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning")).

#### Main findings.

When λ=1\lambda=1, production queue has T​(π)=$​53.78T(\pi)=\mathdollar 53.78M tracking component and F​(π)=$​11.08F(\pi)=\mathdollar 11.08M fairness component, for Lλ​(π)=$​64.86L^{\lambda}(\pi)=\mathdollar 64.86M total (Table [2](https://arxiv.org/html/2602.15182v1#A1.T2 "Table 2 ‣ A.3 Regret decomposition ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), Figure [8](https://arxiv.org/html/2602.15182v1#A1.F8 "Figure 8 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning")).
At Δ=0\Delta=0, production overshoot [Ht−Btneeded]+[H\_{t}-B\_{t}^{\mathrm{needed}}]\_{+} is about $45.0M; under short-horizon markout sweep it remains $45.0M–$51.7M (Figure [3](https://arxiv.org/html/2602.15182v1#A1.F3 "Figure 3 ‣ A.2 Headline event values ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning")).
Decompositions are shown in Figures [5](https://arxiv.org/html/2602.15182v1#A1.F5 "Figure 5 ‣ A.3 Regret decomposition ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), [7](https://arxiv.org/html/2602.15182v1#A1.F7 "Figure 7 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), and [9](https://arxiv.org/html/2602.15182v1#A1.F9 "Figure 9 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning").

#### Deployable subset (deployment-relevant).

Within deployable policies, production cumulative objective value is $64.86M, versus $3.40M (integer pro-rata) and $4.41M (vector mirror descent), a reduction of roughly one order of magnitude.
This ordering is visible in Table [2](https://arxiv.org/html/2602.15182v1#A1.T2 "Table 2 ‣ A.3 Regret decomposition ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning") and Figures [8](https://arxiv.org/html/2602.15182v1#A1.F8 "Figure 8 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning") and [9](https://arxiv.org/html/2602.15182v1#A1.F9 "Figure 9 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning").
Ex post reference policies are lower still, but these require information that is unavailable when the decision is made.

#### Interpretation.

The key empirical quantity is the gap between executed severity HtH\_{t} and the replay transfer benchmark BtneededB\_{t}^{\mathrm{needed}}.
In this event, production queue both overshoots this benchmark and concentrates burden on a smaller set of winners than the best deployable alternatives (Figures [3](https://arxiv.org/html/2602.15182v1#A1.F3 "Figure 3 ‣ A.2 Headline event values ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), [6](https://arxiv.org/html/2602.15182v1#A1.F6 "Figure 6 ‣ A.3 Regret decomposition ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning"), and [4](https://arxiv.org/html/2602.15182v1#A1.F4 "Figure 4 ‣ A.3 Regret decomposition ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning")).

### 5.2 Queue Instability

Queue robustness is evaluated with two diagnostics: monotonicity violations (adjacent inversions after ADL) and adjacent-round rank stability of normalized burden.
Results are consistent with Appendix [C](https://arxiv.org/html/2602.15182v1#A3 "Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning"): production queue has much higher inversion rates (about 11.4%11.4\%) than vector mirror descent (about 0.64%0.64\%) and pro-rata (approximately 0%0\%), and lower rank stability (about 0.340.34 vs 0.720.72 for vector and 0.860.86 for pro-rata).
Definitions and full plots are in Appendix [C](https://arxiv.org/html/2602.15182v1#A3 "Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning") and Figures [12](https://arxiv.org/html/2602.15182v1#A1.F12 "Figure 12 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning") and [13](https://arxiv.org/html/2602.15182v1#A1.F13 "Figure 13 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning").

### 5.3 Instance-Calibrated Upper Envelope

From Proposition [1](https://arxiv.org/html/2602.15182v1#Thmproposition1 "Proposition 1 (Deficit-weighted severity bound with explicit constants). ‣ 3.8 Basic regret bound for the objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
RegTdyn,θ≤(1+2​PTθ)​∑t=1TDt2.\mathrm{Reg}^{\mathrm{dyn},\theta}\_{T}\leq\sqrt{(1+2P\_{T}^{\theta})\sum\_{t=1}^{T}D\_{t}^{2}}.
Using replay-derived estimates, P^Tθ=7.06\widehat{P}\_{T}^{\theta}=7.06 for T=16T=16, define the instance-calibrated upper envelope

|  |  |  |
| --- | --- | --- |
|  | ℬinst:=(1+2​P^Tθ)​∑t=1TDt2≈$​129.7​M.\mathcal{B}\_{\mathrm{inst}}:=\sqrt{(1+2\widehat{P}\_{T}^{\theta})\sum\_{t=1}^{T}D\_{t}^{2}}\approx\mathdollar 129.7\text{M}. |  |

This is not an information-theoretic worst-case statement; it is an episode-calibrated envelope obtained by plugging realized deficits and estimated variation into Proposition [1](https://arxiv.org/html/2602.15182v1#Thmproposition1 "Proposition 1 (Deficit-weighted severity bound with explicit constants). ‣ 3.8 Basic regret bound for the objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
Production cumulative objective value is $64.86M, i.e. about 50.0%50.0\% of ℬinst\mathcal{B}\_{\mathrm{inst}}.
The best baseline that uses only start-of-round information has $3.40M (about 2.6%2.6\% of ℬinst\mathcal{B}\_{\mathrm{inst}}), so roughly 47.4%47.4\% of ℬinst\mathcal{B}\_{\mathrm{inst}} reflects avoidable production loss on this path.
Figures [10](https://arxiv.org/html/2602.15182v1#A1.F10 "Figure 10 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning") and [11](https://arxiv.org/html/2602.15182v1#A1.F11 "Figure 11 ‣ A.4 Additional regret diagnostics ‣ Appendix A Figures and Tables ‣ Autodeleveraging as Online Learning") plot total objective against this bound.

## 6 Conclusion

This paper studied the theoretical and empirical properties of autodeleveraging policies under repeated use.
We formulated a compact online-learning model and used it to evaluate ADL performance on October 10, 2025.
A key clarification is the distinction between exchange deficit DtD\_{t}, replay transfer benchmark BtneededB\_{t}^{\mathrm{needed}}, and realized winner haircut HtH\_{t}.
Under this accounting, production queue exhibits large over-socialization relative to BtneededB\_{t}^{\mathrm{needed}}, while online-feasible alternatives materially reduce tracking component and total objective.
Replay-oracle baselines (i.e., policies that use ex post replay quantities unavailable at round start) are useful upper bounds, but are not interpreted as deployment-feasible event-time controllers.
Our queue-instability analysis gives a churn-robust structural critique: discontinuous extreme-point selection can induce high effective nonstationarity under repeated rounds, though the empirical magnitude of this feedback channel remains to be identified.
Our results complement those of [[4](https://arxiv.org/html/2602.15182v1#bib.bib1 "Autodeleveraging: impossibilities and optimization")], in that we provide a positive result relative to that paper’s negative result of the so-called ADL trilemma.

## References

* [1]
  G. Angeris, T. Chitra, A. Evans, and M. Lorig (2023)
  Short communication: a primer on perpetuals.
  SIAM Journal on Financial Mathematics 14 (1),  pp. SC17–SC30.
  External Links: [Document](https://dx.doi.org/10.1137/22M1520931)
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px1.p1.1 "Risk Management. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§1](https://arxiv.org/html/2602.15182v1#S1.p1.1 "1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§2.1](https://arxiv.org/html/2602.15182v1#S2.SS1.p2.19 "2.1 Perpetuals exchanges and funding mechanics ‣ 2 Background ‣ Autodeleveraging as Online Learning").
* [2]
  O. Besbes, Y. Gur, and A. Zeevi (2015)
  Non-stationary stochastic optimization.
  Operations Research 63 (5),  pp. 1227–1244.
  Cited by: [§3.7](https://arxiv.org/html/2602.15182v1#S3.SS7.p1.1 "3.7 Static and Dynamic Regret ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
* [3]
  Binance (2019)
  What is auto-deleveraging (adl) and how does it work?.
  Note: [Binance support documentation](https://www.binance.info/en-ZA/support/faq/detail/360033525471)Updated Sept. 10, 2025
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px3.p2.1 "Autodeleveraging. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px4.p1.1 "October 10, 2025. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning").
* [4]
  T. Chitra (2026)
  Autodeleveraging: impossibilities and optimization.
  Note: arXiv preprint [2512.01112](https://arxiv.org/abs/2512.01112)
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px3.p2.1 "Autodeleveraging. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px5.p1.1 "This paper. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px5.p2.1 "This paper. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px5.p3.2 "This paper. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§3.5](https://arxiv.org/html/2602.15182v1#S3.SS5.SSS0.Px2.p2.2 "Partial Haircut Policies. ‣ 3.5 Canonical policy examples ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
  [§3.5](https://arxiv.org/html/2602.15182v1#S3.SS5.SSS0.Px2.p3.2 "Partial Haircut Policies. ‣ 3.5 Canonical policy examples ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
  [§3.8](https://arxiv.org/html/2602.15182v1#S3.SS8.p2.5 "3.8 Basic regret bound for the objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
  [§4.2](https://arxiv.org/html/2602.15182v1#S4.SS2.SSS0.Px3.p1.2 "What is new in this separation. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning"),
  [§5](https://arxiv.org/html/2602.15182v1#S5.SS0.SSS0.Px3.p1.1 "Markout horizon and economic interpretation. ‣ 5 Empirical Analysis ‣ Autodeleveraging as Online Learning"),
  [§5](https://arxiv.org/html/2602.15182v1#S5.p1.1 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning"),
  [§6](https://arxiv.org/html/2602.15182v1#S6.p1.4 "6 Conclusion ‣ Autodeleveraging as Online Learning").
* [5]
  CoinGecko Research (2025)
  2025 q1 crypto industry report.
  Note: [CoinGecko industry report](https://www.coingecko.com/research/publications/2025-q1-crypto-report)Accessed Nov. 5, 2025
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.p1.1 "1 Introduction ‣ Autodeleveraging as Online Learning").
* [6]
  CoinGecko Research (2025)
  State of crypto perpetuals 2024.
  Note: [CoinGecko market report](https://assets.coingecko.com/reports/2025/CoinGecko-State-of-Crypto-Perpetuals-Market.pdf)Accessed Oct. 13, 2025
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.p1.1 "1 Introduction ‣ Autodeleveraging as Online Learning").
* [7]
  Committee on Payments and Market Infrastructures and International Organization of Securities Commissions (2012)
  Principles for financial market infrastructures.
  Note: [BIS/IOSCO report](https://www.bis.org/cpmi/publ/d101a.pdf)Implementation and disclosure framework used by CCPs
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px2.p2.1 "Residual Loss Management. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning").
* [8]
  Conejo Capital (2025)
  HyperMultiAssetedADL: hyperliquid liquidation replay.
  Note: [GitHub: ConejoCapital/HyperMultiAssetedADL](https://github.com/ConejoCapital/HyperMultiAssetedADL)
  Cited by: [§5](https://arxiv.org/html/2602.15182v1#S5.p1.1 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning").
* [9]
  Conejo Capital (2025)
  HyperReplay: canonical 10/10 event data.
  Note: [GitHub: HyperReplay canonical data](https://github.com/ConejoCapital/HyperReplay/tree/main/data/canonical)
  Cited by: [§5](https://arxiv.org/html/2602.15182v1#S5.p1.1 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning").
* [10]
  J. Duchi, E. Hazan, and Y. Singer (2011)
  Adaptive subgradient methods for online learning and stochastic optimization.
  Journal of Machine Learning Research 12 (61),  pp. 2121–2159.
  Cited by: [Appendix B](https://arxiv.org/html/2602.15182v1#A2.p1.1 "Appendix B Regret Bounds and Proofs ‣ Autodeleveraging as Online Learning"),
  [§3.7](https://arxiv.org/html/2602.15182v1#S3.SS7.p1.1 "3.7 Static and Dynamic Regret ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
  [§3.8](https://arxiv.org/html/2602.15182v1#S3.SS8.p2.5 "3.8 Basic regret bound for the objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
* [11]
  D. Duffie and H. Zhu (2011)
  Does a central clearing counterparty reduce counterparty risk?.
  Review of Asset Pricing Studies 1 (1),  pp. 74–95.
  External Links: [Document](https://dx.doi.org/10.1093/rapstu/rar001)
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px2.p2.1 "Residual Loss Management. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning").
* [12]
  ERCOT (2022)
  2022 credit workshop: congestion revenue rights (crr).
  Note: [ERCOT workshop slides](https://www.ercot.com/files/docs/2022/02/07/2022_02%20CRR.pdf)See slide 137 for an example loss-allocation mechanism
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px2.p2.1 "Residual Loss Management. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning").
* [13]
  P. Gaillard, G. Stoltz, and T. van Erven (2014)
  A second-order bound with excess losses.
  In Proceedings of The 27th Conference on Learning Theory,
  PMLR, Vol. 35,  pp. 176–196.
  Cited by: [Appendix B](https://arxiv.org/html/2602.15182v1#A2.p1.1 "Appendix B Regret Bounds and Proofs ‣ Autodeleveraging as Online Learning"),
  [§3.7](https://arxiv.org/html/2602.15182v1#S3.SS7.p1.1 "3.7 Static and Dynamic Regret ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
  [§3.8](https://arxiv.org/html/2602.15182v1#S3.SS8.p2.5 "3.8 Basic regret bound for the objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
* [14]
  E. Hazan (2016)
  Introduction to online convex optimization.
  Vol. 2, Foundations and Trends in Optimization.
  Cited by: [Appendix B](https://arxiv.org/html/2602.15182v1#A2.p1.1 "Appendix B Regret Bounds and Proofs ‣ Autodeleveraging as Online Learning"),
  [§3.7](https://arxiv.org/html/2602.15182v1#S3.SS7.p1.1 "3.7 Static and Dynamic Regret ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
  [§3](https://arxiv.org/html/2602.15182v1#S3.p1.1 "3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
* [15]
  S. He, A. Manela, O. Ross, and V. von Wachter (2022)
  Fundamentals of perpetual futures.
  arXiv preprint arXiv:2212.06888.
  Cited by: [§2.1](https://arxiv.org/html/2602.15182v1#S2.SS1.p2.19 "2.1 Perpetuals exchanges and funding mechanics ‣ 2 Background ‣ Autodeleveraging as Online Learning").
* [16]
  Hyperliquid (2025)
  Liquidations.
  Note: [Hyperliquid documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations)Accessed Nov. 2, 2025
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px3.p2.1 "Autodeleveraging. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning").
* [17]
  pluriholonomic (2026)
  Autodeleveraging-analysis.
  Note: [GitHub: pluriholonomic/autodeleveraging-analysis](https://github.com/pluriholonomic/autodeleveraging-analysis)Open-source reconstruction code and data artifacts
  Cited by: [§5](https://arxiv.org/html/2602.15182v1#S5.p1.1 "5 Empirical Analysis ‣ Autodeleveraging as Online Learning").
* [18]
  F. Rodrigues, S. Reynolds, and C. L. (ed.) (2025)
  ’Largest ever’ crypto liquidation event wipes out 6,300 wallets on hyperliquid.
  Note: [CoinDesk report](https://www.coindesk.com/markets/2025/10/11/largest-ever-crypto-liquidation-event-wipes-out-6-300-wallets-on-hyperliquid)Oct. 11, 2025
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px4.p1.1 "October 10, 2025. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning").
* [19]
  S. Shalev-Shwartz and S. Ben-David (2014)
  Understanding machine learning: from theory to algorithms.
   Cambridge University Press.
  Cited by: [§3.7](https://arxiv.org/html/2602.15182v1#S3.SS7.p1.1 "3.7 Static and Dynamic Regret ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
* [20]
  R. S. Sutton and A. G. Barto (2018)
  Reinforcement learning: an introduction.
  2 edition, MIT Press.
  Cited by: [Appendix B](https://arxiv.org/html/2602.15182v1#A2.p1.1 "Appendix B Regret Bounds and Proofs ‣ Autodeleveraging as Online Learning"),
  [§3](https://arxiv.org/html/2602.15182v1#S3.p1.1 "3 Autodeleveraging ‣ Autodeleveraging as Online Learning").
* [21]
  N. Thogiti (2025-12)
  ADL trilemma, assumption j.3, and dan robinson’s critique and tarun’s paper fixes.
  Note: [Blog post](https://thogiti.github.io/2025/12/14/ADL-Trilemma-Dan-Critique-Tarun-paper-fixes.html)
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px5.p2.1 "This paper. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning").
* [22]
  N. Thogiti (2025-12)
  Autodeleveraging, hyperliquid, and the $653m debate.
  Note: [Blog post](https://thogiti.github.io/2025/12/11/Autodeleveraging-Hyperliquid-653M-debate.html)
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px5.p2.1 "This paper. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§4.2](https://arxiv.org/html/2602.15182v1#S4.SS2.SSS0.Px3.p1.2 "What is new in this separation. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning").
* [23]
  N. Thogiti (2026-01)
  Beyond queues — understanding auto-deleveraging from first principles.
  Note: [Blog post](https://thogiti.github.io/2026/01/18/understanding-auto-deleveraging-ADL.html)
  Cited by: [§1](https://arxiv.org/html/2602.15182v1#S1.SS0.SSS0.Px5.p2.1 "This paper. ‣ 1 Introduction ‣ Autodeleveraging as Online Learning"),
  [§4.2](https://arxiv.org/html/2602.15182v1#S4.SS2.SSS0.Px3.p1.2 "What is new in this separation. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning").
* [24]
  M. Zinkevich (2003)
  Online convex programming and generalized infinitesimal gradient ascent.
  In Proceedings of the 20th International Conference on Machine Learning (ICML),
   pp. 928–936.
  Cited by: [Appendix B](https://arxiv.org/html/2602.15182v1#A2.p1.1 "Appendix B Regret Bounds and Proofs ‣ Autodeleveraging as Online Learning"),
  [§3.7](https://arxiv.org/html/2602.15182v1#S3.SS7.p1.1 "3.7 Static and Dynamic Regret ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning"),
  [§3](https://arxiv.org/html/2602.15182v1#S3.p1.1 "3 Autodeleveraging ‣ Autodeleveraging as Online Learning").

## Appendix A Figures and Tables

### A.1 Empirical workflow

![Refer to caption](figures/fig1-obs-model-adl-paper.png)


Figure 1: Observation model and replay workflow used for policy evaluation on October 10, 2025.



1. Liquidation + insurance stage leaves residual shortfall DtD\_{t}.2. Venue chooses ADL severity Bt=θt​DtB\_{t}=\theta\_{t}D\_{t} using an estimate p^kliq,exec\hat{p}\_{k}^{\mathrm{liq,exec}}, which determines expected ADL transfer sizes q^kADL\hat{q}\_{k}^{\mathrm{ADL}}.3. ADL policy allocates winner-side reductions xi,tx\_{i,t}(queue/pro-rata/online optimizer).4. ADL matches winners and losers at bankruptcy transfer prices pkbkp\_{k}^{\mathrm{bk}}.5. Ex post benchmarkBtneeded=∑k|pkliq,exec−pkbk|​|qkADL|B\_{t}^{\mathrm{needed}}=\sum\_{k}|p\_{k}^{\mathrm{liq,exec}}-p\_{k}^{\mathrm{bk}}||q\_{k}^{\mathrm{ADL}}| is computed.6. Remaining deficit and state update determine whether another ADL round is needed.


(a) TikZ lifecycle schematic.

![Refer to caption](figures/fig2_adl_lifecycle_mermaid.png)


(b) Mermaid lifecycle schematic (alternate rendering).

Figure 2: Lifecycle of an ADL round (Figure 2a–2b).

### A.2 Headline event values

| Quantity | Value |
| --- | --- |
| Total liquidations in window | $2,103,111,431 |
| Number of global rounds (5s gap) | 16 |
| Aggregate loser deficit ∑tDt\sum\_{t}D\_{t} | ≈\approx $100.1M |
| Aggregate needed budget ∑tBtneeded\sum\_{t}B\_{t}^{\mathrm{needed}} | ≈\approx $15.1M |
| Aggregate production haircut ∑tHtprod​(0)\sum\_{t}H\_{t}^{\mathrm{prod}}(0) | ≈\approx $60.1M |
| *Production overshoot vs needed* O​(0)O(0) | $45,028,665.72 |
| Short-horizon sensitivity band for O​(Δ)O(\Delta) | about $45.0M–$51.7M |

Table 1: Headline values under the PNL-haircut accounting used in this paper.

![Refer to caption](figures/02_overshoot_vs_horizon.png)


Figure 3: Horizon sensitivity of production overshoot O​(Δ)O(\Delta), where Δ\Delta is the markout/holding-time evaluation offset.

### A.3 Regret decomposition

![Refer to caption](figures/10b_fairness_regret.png)


Figure 4: Cumulative fairness component by policy.



| Policy | Tracking component ($) | Fairness component ($) | Total objective ($) |
| --- | --- | --- | --- |
| Production queue | 53,782,490.53 | 11,077,031.68 | 64,859,522.21 |
| Integer pro-rata | 3,020,120.65 | 384,064.35 | 3,404,185.00 |
| Vector mirror-descent | 1,793,022.03 | 2,620,345.57 | 4,413,367.61 |
| Min-max ILP | 106,205.81 | 0.00 | 106,205.81 |
| Continuous pro-rata | ≈\approx0 | 2,732,437.29 | 2,732,437.29 |

Table 2: Cumulative objective decomposition over 16 rounds. Fairness component is the capacity-normalized max-burden gap to the min-max ILP baseline, scaled by BtneededB\_{t}^{\mathrm{needed}}.

![Refer to caption](figures/05_policy_per_wave_performance.png)


Figure 5: Per-round policy performance against needed budget targets.

![Refer to caption](figures/06_policy_per_wave_cumulative_overshoot.png)


Figure 6: Cumulative overshoot by policy over 16 rounds.

### A.4 Additional regret diagnostics

![Refer to caption](figures/10a_overshoot_regret.png)


Figure 7: Tracking component decomposition across policies.

![Refer to caption](figures/10c_total_regret.png)


Figure 8: Total objective decomposition across policies.

![Refer to caption](figures/09_cumulative_regret_historical.png)


Figure 9: Cumulative objective trajectories over the event path.

![Refer to caption](figures/15_regret_to_severity_bound_ratio.png)


Figure 10: Cumulative trajectory over rounds of policy total objective as a percentage of the cumulative instance-calibrated upper envelope (bound baseline =100%=100\%; final-round envelope about $​129.7\mathdollar 129.7M).

![Refer to caption](figures/12_cumulative_bound_vs_regret.png)


Figure 11: Cumulative trajectory of the instance-calibrated upper envelope versus realized production total objective.



| Robustness axis | Result |
| --- | --- |
| Fairness-weight sweep λ∈[0.5,2]\lambda\in[0.5,2] | Production remains about 40–46×40\text{--}46\times worse than replay-oracle per-round references. |
| Short-horizon markout sweep Δ\Delta | Production overshoot band remains high at about $45.0M–$51.7M. |

Table 3: Robustness summary for the main empirical ordering claims.

![Refer to caption](figures/13_monotonicity_violations_by_policy.png)


Figure 12: Monotonicity-stability diagnostic by policy: mean adjacent post-haircut order violations.

![Refer to caption](figures/14_queue_rank_stability_by_policy.png)


Figure 13: Queue-position stability proxy by policy: adjacent-round rank correlation of normalized burden.

## Appendix B Regret Bounds and Proofs

In this Appendix, we provide (for completeness) a number of regret bounds that are useful in practice.
These results are standard and can be found in, e.g., [[24](https://arxiv.org/html/2602.15182v1#bib.bib20 "Online convex programming and generalized infinitesimal gradient ascent"), [14](https://arxiv.org/html/2602.15182v1#bib.bib21 "Introduction to online convex optimization"), [20](https://arxiv.org/html/2602.15182v1#bib.bib22 "Reinforcement learning: an introduction")], with instance-dependent refinements discussed in adaptive and second-order analyses [[10](https://arxiv.org/html/2602.15182v1#bib.bib25 "Adaptive subgradient methods for online learning and stochastic optimization"), [13](https://arxiv.org/html/2602.15182v1#bib.bib26 "A second-order bound with excess losses")].

###### Proposition 2 (Static regret bound).

If each ℓt\ell\_{t} is convex and GG-Lipschitz on a domain of diameter DD, projected mirror descent with step size η≍1/T\eta\asymp 1/\sqrt{T} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTstatic=O​(G​D​T).\mathrm{Reg}^{\mathrm{static}}\_{T}=O(GD\sqrt{T}). |  | (24) |

###### Proof.

For projected mirror descent (Euclidean case), the standard one-step inequality gives, for any comparator x⋆x^{\star},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt​(xt)−ℓt​(x⋆)≤‖xt−x⋆‖22−‖xt+1−x⋆‖222​η+η2​‖gt‖22,\ell\_{t}(x\_{t})-\ell\_{t}(x^{\star})\leq\frac{\|x\_{t}-x^{\star}\|\_{2}^{2}-\|x\_{t+1}-x^{\star}\|\_{2}^{2}}{2\eta}+\frac{\eta}{2}\|g\_{t}\|\_{2}^{2}, |  | (25) |

where gt∈∂ℓt​(xt)g\_{t}\in\partial\ell\_{t}(x\_{t}) and ‖gt‖2≤G\|g\_{t}\|\_{2}\leq G.
Summing over t=1,…,Tt=1,\dots,T and using domain diameter DD yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1T(ℓt​(xt)−ℓt​(x⋆))≤D22​η+η​G2​T2.\sum\_{t=1}^{T}\big(\ell\_{t}(x\_{t})-\ell\_{t}(x^{\star})\big)\leq\frac{D^{2}}{2\eta}+\frac{\eta G^{2}T}{2}. |  | (26) |

Optimizing in η\eta gives η⋆=D/(G​T)\eta^{\star}=D/(G\sqrt{T}) and bound G​D​TGD\sqrt{T}, i.e. O​(G​D​T)O(GD\sqrt{T}).
∎

###### Proposition 3 (Dynamic regret with comparator variation).

Let PTx⋆=∑t=2T‖xt⋆−xt−1⋆‖P\_{T}^{x^{\star}}=\sum\_{t=2}^{T}\|x\_{t}^{\star}-x\_{t-1}^{\star}\| be path variation of a dynamic comparator sequence.
Then for convex GG-Lipschitz losses on diameter-DD domains, mirror-descent dynamic regret scales as

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn=O​(G​D​T+G​PTx⋆).\mathrm{Reg}^{\mathrm{dyn}}\_{T}=O\!\left(GD\sqrt{T}+GP\_{T}^{x^{\star}}\right). |  | (27) |

###### Proof.

Start from the static telescoping inequality applied against a changing comparator xt⋆x\_{t}^{\star}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1T(ℓt​(xt)−ℓt​(xt⋆))≤‖x1−x1⋆‖222​η+η2​∑t=1T‖gt‖22+12​η​∑t=2TΔt,\sum\_{t=1}^{T}\big(\ell\_{t}(x\_{t})-\ell\_{t}(x\_{t}^{\star})\big)\leq\frac{\|x\_{1}-x\_{1}^{\star}\|\_{2}^{2}}{2\eta}+\frac{\eta}{2}\sum\_{t=1}^{T}\|g\_{t}\|\_{2}^{2}+\frac{1}{2\eta}\sum\_{t=2}^{T}\Delta\_{t}, |  | (28) |

where
Δt:=‖xt−xt⋆‖22−‖xt−xt−1⋆‖22.\Delta\_{t}:=\|x\_{t}-x\_{t}^{\star}\|\_{2}^{2}-\|x\_{t}-x\_{t-1}^{\star}\|\_{2}^{2}.
By expansion,
Δt≤2​‖xt−xt⋆‖2​‖xt⋆−xt−1⋆‖2≤2​D​‖xt⋆−xt−1⋆‖2.\Delta\_{t}\leq 2\|x\_{t}-x\_{t}^{\star}\|\_{2}\|x\_{t}^{\star}-x\_{t-1}^{\star}\|\_{2}\leq 2D\|x\_{t}^{\star}-x\_{t-1}^{\star}\|\_{2}.
Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn≤D2+2​D​PTx⋆2​η+η​G2​T2.\mathrm{Reg}^{\mathrm{dyn}}\_{T}\leq\frac{D^{2}+2DP\_{T}^{x^{\star}}}{2\eta}+\frac{\eta G^{2}T}{2}. |  | (29) |

Choosing η≍D/(G​T)\eta\asymp D/(G\sqrt{T}) gives O​(G​D​T+G​PTx⋆)O(GD\sqrt{T}+GP\_{T}^{x^{\star}}).
∎

###### Proposition 4 (Loss-specific gradient and diameter constants).

For
ℓt​(x)=λtrack​|𝟏⊤​x−bt|+λfair​maxi⁡xi/(ui,t+ε)\ell\_{t}(x)=\lambda\_{\mathrm{track}}|{\mathbf{1}}^{\top}x-b\_{t}|+\lambda\_{\mathrm{fair}}\max\_{i}x\_{i}/(u\_{i,t}+\varepsilon),
Let nt=|Wt|n\_{t}=|W\_{t}|, Ut=∑i∈Wtui,tU\_{t}=\sum\_{i\in W\_{t}}u\_{i,t}, nmax=maxt⁡ntn\_{\max}=\max\_{t}n\_{t}, Umax=maxt⁡UtU\_{\max}=\max\_{t}U\_{t}.
Then any subgradient gt∈∂ℓt​(xt)g\_{t}\in\partial\ell\_{t}(x\_{t}) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖gt‖2≤λtrack​nt+λfairε≤G⋆,\|g\_{t}\|\_{2}\leq\lambda\_{\mathrm{track}}\sqrt{n\_{t}}+\frac{\lambda\_{\mathrm{fair}}}{\varepsilon}\leq G\_{\star}, |  | (30) |

with
G⋆=λtrack​nmax+λfair/ε.G\_{\star}=\lambda\_{\mathrm{track}}\sqrt{n\_{\max}}+\lambda\_{\mathrm{fair}}/\varepsilon.
Also, for any x,y∈𝒳tx,y\in\mathcal{X}\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖x−y‖2≤2​Ut≤D⋆,D⋆=2​Umax.\|x-y\|\_{2}\leq\sqrt{2}\,U\_{t}\leq D\_{\star},\qquad D\_{\star}=\sqrt{2}\,U\_{\max}. |  | (31) |

Hence mirror descent admits

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTstatic≤D⋆​G⋆​T.\mathrm{Reg}^{\mathrm{static}}\_{T}\leq D\_{\star}G\_{\star}\sqrt{T}. |  | (32) |

###### Proof.

Write gt=gttrack+gtfairg\_{t}=g\_{t}^{\mathrm{track}}+g\_{t}^{\mathrm{fair}}.
For tracking term |𝟏⊤​x−bt||{\mathbf{1}}^{\top}x-b\_{t}|, a subgradient is ±𝟏\pm{\mathbf{1}}, so
‖gttrack‖2≤λtrack​nt.\|g\_{t}^{\mathrm{track}}\|\_{2}\leq\lambda\_{\mathrm{track}}\sqrt{n\_{t}}.
For fairness term ft​(x)=maxi⁡xi/(ui,t+ε)f\_{t}(x)=\max\_{i}x\_{i}/(u\_{i,t}+\varepsilon), let
It​(x)=arg⁡maxi⁡xi/(ui,t+ε)I\_{t}(x)=\arg\max\_{i}x\_{i}/(u\_{i,t}+\varepsilon).
Any subgradient has coordinates

|  |  |  |
| --- | --- | --- |
|  | [gtfair]j={λfair​αj/(uj,t+ε),j∈It​(x),0,j∉It​(x),[g\_{t}^{\mathrm{fair}}]\_{j}=\begin{cases}\lambda\_{\mathrm{fair}}\alpha\_{j}/(u\_{j,t}+\varepsilon),&j\in I\_{t}(x),\\ 0,&j\notin I\_{t}(x),\end{cases} |  |

with αj≥0\alpha\_{j}\geq 0 and ∑j∈It​(x)αj=1\sum\_{j\in I\_{t}(x)}\alpha\_{j}=1.
Therefore
‖gtfair‖2≤λfair/ε.\|g\_{t}^{\mathrm{fair}}\|\_{2}\leq\lambda\_{\mathrm{fair}}/\varepsilon.
Triangle inequality gives G⋆G\_{\star}.

For diameter, feasibility implies xi≥0x\_{i}\geq 0 and ∑ixi=Bt≤Ut\sum\_{i}x\_{i}=B\_{t}\leq U\_{t}, so
‖x‖2≤‖x‖1≤Ut.\|x\|\_{2}\leq\|x\|\_{1}\leq U\_{t}.
Then ‖x−y‖2≤‖x‖2+‖y‖2≤2​Ut\|x-y\|\_{2}\leq\|x\|\_{2}+\|y\|\_{2}\leq 2U\_{t}.
Using the simplex geometry with equal mass bound tightens to 2​Ut\sqrt{2}U\_{t}, giving D⋆D\_{\star}.
Plug G⋆,D⋆G\_{\star},D\_{\star} into Proposition A.1.
∎

###### Proposition 5 (Sharper dynamic bound for path-dependent rounds).

Let
PT=∑t=2T‖xt⋆−xt−1⋆‖2P\_{T}=\sum\_{t=2}^{T}\|x\_{t}^{\star}-x\_{t-1}^{\star}\|\_{2}
be comparator path variation.
For step size η>0\eta>0, projected mirror descent satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn≤D⋆2+2​D⋆​PT2​η+η2​∑t=1T‖gt‖22.\mathrm{Reg}^{\mathrm{dyn}}\_{T}\leq\frac{D\_{\star}^{2}+2D\_{\star}P\_{T}}{2\eta}+\frac{\eta}{2}\sum\_{t=1}^{T}\|g\_{t}\|\_{2}^{2}. |  | (33) |

Choosing
η⋆=(D⋆2+2​D⋆​PT)/∑t‖gt‖22\eta^{\star}=\sqrt{(D\_{\star}^{2}+2D\_{\star}P\_{T})/\sum\_{t}\|g\_{t}\|\_{2}^{2}}
gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn≤(D⋆2+2​D⋆​PT)​∑t=1T‖gt‖22≤G⋆​T​(D⋆2+2​D⋆​PT).\mathrm{Reg}^{\mathrm{dyn}}\_{T}\leq\sqrt{(D\_{\star}^{2}+2D\_{\star}P\_{T})\sum\_{t=1}^{T}\|g\_{t}\|\_{2}^{2}}\leq G\_{\star}\sqrt{T(D\_{\star}^{2}+2D\_{\star}P\_{T})}. |  | (34) |

###### Proof.

This is Proposition A.2 with explicit constants from Proposition A.3 substituted into the dynamic mirror-descent inequality before step-size optimization.
∎

### B.1 Proof of Proposition [1](https://arxiv.org/html/2602.15182v1#Thmproposition1 "Proposition 1 (Deficit-weighted severity bound with explicit constants). ‣ 3.8 Basic regret bound for the objective ‣ 3 Autodeleveraging ‣ Autodeleveraging as Online Learning")

In one dimension with θt∈[0,1]\theta\_{t}\in[0,1], projected OGD update is
θt+1=Π[0,1]​(θt−η​gt)\theta\_{t+1}=\Pi\_{[0,1]}(\theta\_{t}-\eta g\_{t})
with
gt∈∂ℓtθ​(θt).g\_{t}\in\partial\ell\_{t}^{\theta}(\theta\_{t}).
Since
ℓtθ​(θ)=Dt​|θ−θtneeded|,\ell\_{t}^{\theta}(\theta)=D\_{t}|\theta-\theta\_{t}^{\mathrm{needed}}|,
any subgradient has magnitude |gt|≤Dt|g\_{t}|\leq D\_{t}.

For dynamic comparator {θt⋆}\{\theta\_{t}^{\star}\}, the one-dimensional dynamic OGD inequality gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1T(ℓtθ​(θt)−ℓtθ​(θt⋆))≤(θ1−θ1⋆)22​η+12​η​∑t=2TΔt+η2​∑t=1Tgt2,\sum\_{t=1}^{T}\big(\ell\_{t}^{\theta}(\theta\_{t})-\ell\_{t}^{\theta}(\theta\_{t}^{\star})\big)\leq\frac{(\theta\_{1}-\theta\_{1}^{\star})^{2}}{2\eta}+\frac{1}{2\eta}\sum\_{t=2}^{T}\Delta\_{t}+\frac{\eta}{2}\sum\_{t=1}^{T}g\_{t}^{2}, |  | (35) |

where
Δt:=(θt−θt⋆)2−(θt−θt−1⋆)2.\Delta\_{t}:=(\theta\_{t}-\theta\_{t}^{\star})^{2}-(\theta\_{t}-\theta\_{t-1}^{\star})^{2}.
Because θt,θt⋆∈[0,1]\theta\_{t},\theta\_{t}^{\star}\in[0,1],
|θt−θt⋆|≤1|\theta\_{t}-\theta\_{t}^{\star}|\leq 1
and
Δt≤2​|θt⋆−θt−1⋆|.\Delta\_{t}\leq 2|\theta\_{t}^{\star}-\theta\_{t-1}^{\star}|.
Define
PTθ=∑t=2T|θt⋆−θt−1⋆|.P\_{T}^{\theta}=\sum\_{t=2}^{T}|\theta\_{t}^{\star}-\theta\_{t-1}^{\star}|.
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn,θ≤1+2​PTθ2​η+η2​∑t=1TDt2.\mathrm{Reg}^{\mathrm{dyn},\theta}\_{T}\leq\frac{1+2P\_{T}^{\theta}}{2\eta}+\frac{\eta}{2}\sum\_{t=1}^{T}D\_{t}^{2}. |  | (36) |

Minimizing the RHS over η>0\eta>0 yields
η⋆=(1+2​PTθ)/∑tDt2\eta^{\star}=\sqrt{(1+2P\_{T}^{\theta})/\sum\_{t}D\_{t}^{2}}
and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | RegTdyn,θ≤(1+2​PTθ)​∑t=1TDt2.\mathrm{Reg}^{\mathrm{dyn},\theta}\_{T}\leq\sqrt{(1+2P\_{T}^{\theta})\sum\_{t=1}^{T}D\_{t}^{2}}. |  | (37) |

## Appendix C Queue Instability: Extreme-Point Selection

We fix a round and suppress the time index. Let WW be the winner set with n:=|W|n:=|W| winners.
Let u∈ℝ+nu\in\mathbb{R}^{n}\_{+} denote the per-winner PNL haircut capacities and let
U:=∑i=1nuiU:=\sum\_{i=1}^{n}u\_{i}. For a fixed round budget B∈[0,U]B\in[0,U], define the feasibility polytope

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(B,u):={x∈ℝn:0≤xi≤ui∀i,∑i=1nxi=B}.X(B,u):=\left\{x\in\mathbb{R}^{n}:0\leq x\_{i}\leq u\_{i}\ \ \forall i,\ \ \sum\_{i=1}^{n}x\_{i}=B\right\}. |  | (38) |

This is the intersection of a box with an affine hyperplane, hence a bounded polytope.

###### Definition 1 (Queue allocation map).

Let s∈ℝns\in\mathbb{R}^{n} be a score vector and let σ​(s)\sigma(s) be a permutation such that
sσ​(1)>sσ​(2)>⋯>sσ​(n)s\_{\sigma(1)}>s\_{\sigma(2)}>\cdots>s\_{\sigma(n)}.
The (greedy) queue allocation associated with σ\sigma is Qσ​(B,u)∈X​(B,u)Q\_{\sigma}(B,u)\in X(B,u) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | xσ​(j):=min⁡{uσ​(j),B−∑ℓ<jxσ​(ℓ)},j=1,…,n,x\_{\sigma(j)}:=\min\left\{u\_{\sigma(j)},\ B-\sum\_{\ell<j}x\_{\sigma(\ell)}\right\},\qquad j=1,\dots,n, |  | (39) |

and xσ​(j):=0x\_{\sigma(j)}:=0 for all jj after the budget is exhausted.

###### Definition 2 (Extreme point and instability).

A point x∈X​(B,u)x\in X(B,u) is an *extreme point* (vertex) if it cannot be written as a nontrivial
convex combination of two distinct points in X​(B,u)X(B,u).
A mapping F:ℝn→ℝnF:\mathbb{R}^{n}\to\mathbb{R}^{n} is *Lipschitz* if there exists L<∞L<\infty with
‖F​(s)−F​(s′)‖1≤L​‖s−s′‖∞\|F(s)-F(s^{\prime})\|\_{1}\leq L\|s-s^{\prime}\|\_{\infty} for all s,s′s,s^{\prime}.

###### Lemma 1 (Vertices of the capped simplex).

Assume 0<B<U0<B<U and ui>0u\_{i}>0 for all ii. A point x∈X​(B,u)x\in X(B,u) is an extreme point if and only if
*at most one* coordinate satisfies 0<xi<ui0<x\_{i}<u\_{i} (equivalently, at least n−1n-1 coordinates are at
a bound 0 or uiu\_{i}).

###### Proof.

(*Only if*.) Suppose x∈X​(B,u)x\in X(B,u) has two distinct coordinates p≠qp\neq q with
0<xp<up0<x\_{p}<u\_{p} and 0<xq<uq0<x\_{q}<u\_{q}. Let d:=ep−eqd:=e\_{p}-e\_{q}, where epe\_{p} is the ppth standard basis vector.
Since xpx\_{p} and xqx\_{q} are strictly interior, there exists ϵ>0\epsilon>0 such that
x±ϵ​dx\pm\epsilon d satisfies 0≤(x±ϵ​d)i≤ui0\leq(x\pm\epsilon d)\_{i}\leq u\_{i} for all ii.
Moreover, ∑i(x±ϵ​d)i=∑ixi±ϵ​(1−1)=B\sum\_{i}(x\pm\epsilon d)\_{i}=\sum\_{i}x\_{i}\pm\epsilon(1-1)=B, so x±ϵ​d∈X​(B,u)x\pm\epsilon d\in X(B,u).
But then

|  |  |  |
| --- | --- | --- |
|  | x=12​(x+ϵ​d)+12​(x−ϵ​d)x=\tfrac{1}{2}(x+\epsilon d)+\tfrac{1}{2}(x-\epsilon d) |  |

is a nontrivial convex combination of two distinct feasible points, so xx is not extreme.

(*If*.) Conversely, assume x∈X​(B,u)x\in X(B,u) has at most one coordinate kk with 0<xk<uk0<x\_{k}<u\_{k}.
Suppose x=θ​y+(1−θ)​zx=\theta y+(1-\theta)z for some θ∈(0,1)\theta\in(0,1) and y,z∈X​(B,u)y,z\in X(B,u).
For any index ii with xi=0x\_{i}=0, feasibility implies yi≥0y\_{i}\geq 0 and zi≥0z\_{i}\geq 0 and thus
0=xi=θ​yi+(1−θ)​zi0=x\_{i}=\theta y\_{i}+(1-\theta)z\_{i} forces yi=zi=0y\_{i}=z\_{i}=0.
Similarly, for any index ii with xi=uix\_{i}=u\_{i}, feasibility implies yi≤uiy\_{i}\leq u\_{i} and zi≤uiz\_{i}\leq u\_{i} and thus
ui=xi=θ​yi+(1−θ)​ziu\_{i}=x\_{i}=\theta y\_{i}+(1-\theta)z\_{i} forces yi=zi=uiy\_{i}=z\_{i}=u\_{i}.
Therefore yi=zi=xiy\_{i}=z\_{i}=x\_{i} for all i≠ki\neq k. Using the budget constraint ∑iyi=∑izi=B\sum\_{i}y\_{i}=\sum\_{i}z\_{i}=B and
∑i≠kyi=∑i≠kzi=∑i≠kxi\sum\_{i\neq k}y\_{i}=\sum\_{i\neq k}z\_{i}=\sum\_{i\neq k}x\_{i}, we conclude yk=zk=xky\_{k}=z\_{k}=x\_{k} as well.
Hence y=z=xy=z=x, so xx is extreme.
∎

###### Proposition 6 (Queue allocations are vertices).

For any permutation σ\sigma and any (B,u)(B,u) with 0<B<U0<B<U, the queue output x=Qσ​(B,u)x=Q\_{\sigma}(B,u)
is an extreme point of X​(B,u)X(B,u).

###### Proof.

By Definition [1](https://arxiv.org/html/2602.15182v1#Thmdefinition1 "Definition 1 (Queue allocation map). ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning"), the queue output x=Qσ​(B,u)x=Q\_{\sigma}(B,u) satisfies:
there exists an index mm (the last touched account) such that
xσ​(j)=uσ​(j)x\_{\sigma(j)}=u\_{\sigma(j)} for all j<mj<m, xσ​(m)∈[0,uσ​(m)]x\_{\sigma(m)}\in[0,u\_{\sigma(m)}], and xσ​(j)=0x\_{\sigma(j)}=0 for all j>mj>m.
Thus at most one coordinate can be strictly interior, i.e., satisfy 0<xi<ui0<x\_{i}<u\_{i}.
By Lemma [1](https://arxiv.org/html/2602.15182v1#Thmlemma1 "Lemma 1 (Vertices of the capped simplex). ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning"), xx is an extreme point of X​(B,u)X(B,u).
∎

###### Proposition 7 (Queue = linear optimization over the polytope).

Fix a score vector ss with strict ordering sσ​(1)>⋯>sσ​(n)s\_{\sigma(1)}>\cdots>s\_{\sigma(n)}.
Then Qσ​(B,u)Q\_{\sigma}(B,u) is the unique optimizer of the linear program

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈X​(B,u)⁡⟨s,x⟩.\max\_{x\in X(B,u)}\ \langle s,x\rangle. |  | (40) |

In particular, queues implement *extreme-point selection* in the feasibility polytope.

###### Proof.

This is the fractional knapsack (greedy) structure. Let σ\sigma order scores strictly decreasing.
Consider any feasible x∈X​(B,u)x\in X(B,u). If there exist indices p,qp,q with sp>sqs\_{p}>s\_{q} but xp<upx\_{p}<u\_{p} and xq>0x\_{q}>0,
then for sufficiently small ϵ>0\epsilon>0 the modified allocation x~:=x+ϵ​(ep−eq)\tilde{x}:=x+\epsilon(e\_{p}-e\_{q}) remains feasible
(same argument as in Lemma [1](https://arxiv.org/html/2602.15182v1#Thmlemma1 "Lemma 1 (Vertices of the capped simplex). ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")) and strictly improves the objective:

|  |  |  |
| --- | --- | --- |
|  | ⟨s,x~⟩−⟨s,x⟩=ϵ​(sp−sq)>0.\langle s,\tilde{x}\rangle-\langle s,x\rangle=\epsilon(s\_{p}-s\_{q})>0. |  |

Therefore, in any optimizer, whenever some lower-scored coordinate has positive mass, all higher-scored
coordinates must already be saturated at their upper bounds. This forces the greedy prefix structure:
fill xσ​(1)x\_{\sigma(1)} up to uσ​(1)u\_{\sigma(1)}, then xσ​(2)x\_{\sigma(2)}, and so on, with at most one partially-filled index.
That structure is exactly Qσ​(B,u)Q\_{\sigma}(B,u) from ([39](https://arxiv.org/html/2602.15182v1#A3.E39 "In Definition 1 (Queue allocation map). ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")).
Strict ordering implies uniqueness.
∎

###### Proposition 8 (Fundamental instability of queues).

Assume there exist two distinct indices i≠ji\neq j with ui≥Bu\_{i}\geq B and uj≥Bu\_{j}\geq B.
Let Q​(s)Q(s) denote the queue allocation induced by ordering scores ss (with any deterministic tie-breaking).
Then Q​(⋅)Q(\cdot) is not continuous (hence not Lipschitz): for every δ>0\delta>0 there exist score vectors
s,s′s,s^{\prime} with ‖s−s′‖∞≤δ\|s-s^{\prime}\|\_{\infty}\leq\delta but

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Q​(s)−Q​(s′)‖1=2​B.\|Q(s)-Q(s^{\prime})\|\_{1}=2B. |  | (41) |

Thus, arbitrarily small perturbations in scores can induce order-one changes in allocations and queue positions.

###### Proof.

Pick distinct indices i≠ji\neq j with ui≥Bu\_{i}\geq B and uj≥Bu\_{j}\geq B.
Fix any δ>0\delta>0, and define two score vectors s,s′∈ℝns,s^{\prime}\in\mathbb{R}^{n} by

|  |  |  |
| --- | --- | --- |
|  | si=δ,sj=0,sk=−1(k∉{i,j}),si′=0,sj′=δ,sk′=−1(k∉{i,j}).s\_{i}=\delta,\ s\_{j}=0,\ \ s\_{k}=-1\ \ (k\notin\{i,j\}),\qquad s^{\prime}\_{i}=0,\ s^{\prime}\_{j}=\delta,\ \ s^{\prime}\_{k}=-1\ \ (k\notin\{i,j\}). |  |

Then ‖s−s′‖∞=δ\|s-s^{\prime}\|\_{\infty}=\delta.
Under ss, the top-ranked coordinate is ii, and since ui≥Bu\_{i}\geq B the greedy queue allocates all budget to ii:
Q​(s)=B​eiQ(s)=Be\_{i}. Under s′s^{\prime}, the top-ranked coordinate is jj and similarly Q​(s′)=B​ejQ(s^{\prime})=Be\_{j}.
Hence

|  |  |  |
| --- | --- | --- |
|  | ‖Q​(s)−Q​(s′)‖1=‖B​ei−B​ej‖1=2​B.\|Q(s)-Q(s^{\prime})\|\_{1}=\|Be\_{i}-Be\_{j}\|\_{1}=2B. |  |

Since δ\delta is arbitrary, Q​(⋅)Q(\cdot) cannot be continuous, and therefore cannot be Lipschitz.
∎

### C.1 Duality and Queue Position

In this section, we prove a stronger version of the result for fairness using convex duality.
We again fix a round and suppress the time index. Let X​(B,u)X(B,u) be the feasibility polytope in
([38](https://arxiv.org/html/2602.15182v1#A3.E38 "In Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")). For any feasible allocation x∈X​(B,u)x\in X(B,u), define the
*capacity-normalized burden* (haircut fraction)

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(x):=xiui∈[0,1](ui>0).h\_{i}(x):=\frac{x\_{i}}{u\_{i}}\in[0,1]\quad(u\_{i}>0). |  | (42) |

Define the *worst-burden* (equivalently, the top queue position under the induced burden ranking)

|  |  |  |  |
| --- | --- | --- | --- |
|  | z​(x):=maxi∈[n]⁡hi​(x).z(x):=\max\_{i\in[n]}h\_{i}(x). |  | (43) |

Mechanism-design interpretation: if agents experience disutility as an increasing function of hih\_{i},
then minimizing z​(x)z(x) is a Rawlsian or max–min fairness criterion that protects the worst-hit participant.

#### Min–max burden program and its dual.

Consider the min–max fairness allocation problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minx∈X​(B,u)⁡z​(x)=minx∈X​(B,u)⁡maxi⁡xiui.\min\_{x\in X(B,u)}\ z(x)\;=\;\min\_{x\in X(B,u)}\ \max\_{i}\frac{x\_{i}}{u\_{i}}. |  | (44) |

Introducing an epigraph variable z≥0z\geq 0 yields the equivalent linear program

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minx,z\displaystyle\min\_{x,z} | z\displaystyle z |  | (P) |
|  | s.t. | ∑i=1nxi=B,\displaystyle\sum\_{i=1}^{n}x\_{i}=B, |  |
|  |  | 0≤xi≤ui,i=1,…,n,\displaystyle 0\leq x\_{i}\leq u\_{i},\qquad i=1,\dots,n, |  |
|  |  | xi≤z​ui,i=1,…,n,\displaystyle x\_{i}\leq zu\_{i},\qquad i=1,\dots,n, |  |
|  |  | z≥0.\displaystyle z\geq 0. |  |

The dual of ([P](https://arxiv.org/html/2602.15182v1#A3.Ex12 "In Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")) collapses to a one-dimensional shadow-price constraint:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxy≥0\displaystyle\max\_{y\geq 0} | y​B\displaystyle yB |  | (D) |
|  | s.t. | y​∑i=1nui≤1.\displaystyle y\sum\_{i=1}^{n}u\_{i}\leq 1. |  |

The dual variable yy is the shadow price of the budget constraint under the egalitarian objective.

###### Proof of dual form ([D](https://arxiv.org/html/2602.15182v1#A3.Ex13 "In Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")).

We derive the dual of ([P](https://arxiv.org/html/2602.15182v1#A3.Ex12 "In Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")) (ignoring indices with ui=0u\_{i}=0).
Form the Lagrangian with multiplier α∈ℝ\alpha\in\mathbb{R} for ∑ixi=B\sum\_{i}x\_{i}=B,
multipliers μi≥0\mu\_{i}\geq 0 for constraints xi−z​ui≤0x\_{i}-zu\_{i}\leq 0, multipliers νi≥0\nu\_{i}\geq 0 for −xi≤0-x\_{i}\leq 0,
and multiplier ρ≥0\rho\geq 0 for −z≤0-z\leq 0:

|  |  |  |
| --- | --- | --- |
|  | ℒ​(x,z;α,μ,ν,ρ)=z+α​(∑ixi−B)+∑iμi​(xi−z​ui)+∑iνi​(−xi)+ρ​(−z).\mathcal{L}(x,z;\alpha,\mu,\nu,\rho)=z+\alpha\Big(\sum\_{i}x\_{i}-B\Big)+\sum\_{i}\mu\_{i}(x\_{i}-zu\_{i})+\sum\_{i}\nu\_{i}(-x\_{i})+\rho(-z). |  |

Collecting terms gives

|  |  |  |
| --- | --- | --- |
|  | ℒ=z​(1−∑iμi​ui−ρ)+∑ixi​(α+μi−νi)−α​B.\mathcal{L}=z\Big(1-\sum\_{i}\mu\_{i}u\_{i}-\rho\Big)+\sum\_{i}x\_{i}(\alpha+\mu\_{i}-\nu\_{i})-\alpha B. |  |

For the infimum over (x,z)(x,z) to be finite, we require
α+μi−νi=0\alpha+\mu\_{i}-\nu\_{i}=0 for all ii (so νi=α+μi≥0\nu\_{i}=\alpha+\mu\_{i}\geq 0) and
1−∑iμi​ui−ρ=01-\sum\_{i}\mu\_{i}u\_{i}-\rho=0 with ρ≥0\rho\geq 0 (so ∑iμi​ui≤1\sum\_{i}\mu\_{i}u\_{i}\leq 1).
Under these conditions, infx,zℒ=−α​B\inf\_{x,z}\mathcal{L}=-\alpha B.
Let y:=−αy:=-\alpha. For any optimal dual solution we may assume y≥0y\geq 0 since B>0B>0 and the objective is y​ByB.
Moreover, the constraint νi=α+μi≥0\nu\_{i}=\alpha+\mu\_{i}\geq 0 becomes μi≥y\mu\_{i}\geq y.
To maximize y​ByB subject to ∑iμi​ui≤1\sum\_{i}\mu\_{i}u\_{i}\leq 1 and μi≥y\mu\_{i}\geq y, we set μi=y\mu\_{i}=y for all ii,
yielding the single constraint y​∑iui≤1y\sum\_{i}u\_{i}\leq 1.
Thus the dual reduces to ([D](https://arxiv.org/html/2602.15182v1#A3.Ex13 "In Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")).
∎

###### Proposition 9 (Duality-implied elimination of queue positions and dominance over queues).

Assume |W|=n≥2|W|=n\geq 2, ui>0u\_{i}>0 for all ii, and 0<B<U0<B<U.
Let xMMx^{\mathrm{MM}} be the optimizer of ([44](https://arxiv.org/html/2602.15182v1#A3.E44 "In Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")) and let xQ=Qσ​(B,u)x^{Q}=Q\_{\sigma}(B,u) be any queue allocation.

1. 1.

   *(Structure / no queue positions).*
   The min–max optimizer is unique and equals pro-rata:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | xiMM=BU​ui,i=1,…,n,x^{\mathrm{MM}}\_{i}=\frac{B}{U}\,u\_{i},\qquad i=1,\dots,n, |  | (45) |

   and therefore hi​(xMM)=B/Uh\_{i}(x^{\mathrm{MM}})=B/U for all ii (all burdens equalized).
2. 2.

   *(Strict worst-burden improvement).*
   Every queue has strictly worse worst-burden:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | z​(xQ)>z​(xMM)=BU,z(x^{Q})>z(x^{\mathrm{MM}})=\frac{B}{U}, |  | (46) |

   unless only one account has positive capacity (the degenerate n=1n=1 case).
3. 3.

   *(Monotonicity).*
   Define post-ADL remaining endowment ri​(x):=ui−xir\_{i}(x):=u\_{i}-x\_{i}.
   Under pro-rata ([45](https://arxiv.org/html/2602.15182v1#A3.E45 "In item 1 ‣ Proposition 9 (Duality-implied elimination of queue positions and dominance over queues). ‣ Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")), ri​(xMM)=(1−BU)​uir\_{i}(x^{\mathrm{MM}})=(1-\tfrac{B}{U})u\_{i},
   so ui≥uj⇒ri​(xMM)≥rj​(xMM)u\_{i}\geq u\_{j}\Rightarrow r\_{i}(x^{\mathrm{MM}})\geq r\_{j}(x^{\mathrm{MM}}) (no inversions).
   Conversely, for any strict queue rule, there exist feasible (B,u)(B,u) such that the induced post-ADL ordering
   violates monotonicity (hence creates inversions in queue-position diagnostics).

###### Proof.

*Part 1 (Structure / uniqueness).*
By weak duality, any feasible (x,z)(x,z) to ([P](https://arxiv.org/html/2602.15182v1#A3.Ex12 "In Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")) must satisfy

|  |  |  |
| --- | --- | --- |
|  | B=∑ixi≤∑iz​ui=z​U⇒z≥BU.B=\sum\_{i}x\_{i}\leq\sum\_{i}zu\_{i}=zU\quad\Rightarrow\quad z\geq\frac{B}{U}. |  |

The pro-rata allocation xMM=(B/U)​ux^{\mathrm{MM}}=(B/U)u is feasible and attains z=B/Uz=B/U (since xiMM/ui=B/Ux\_{i}^{\mathrm{MM}}/u\_{i}=B/U),
so it is optimal.
Uniqueness follows because at z⋆=B/Uz^{\star}=B/U the constraints xi≤z⋆​uix\_{i}\leq z^{\star}u\_{i} sum to
∑ixi≤z⋆​U=B\sum\_{i}x\_{i}\leq z^{\star}U=B, but feasibility requires ∑ixi=B\sum\_{i}x\_{i}=B, hence *all* inequalities must bind:
xi=z⋆​uix\_{i}=z^{\star}u\_{i} for every ii.

*Part 2 (Strict dominance over queues).*
Let xQ=Qσ​(B,u)x^{Q}=Q\_{\sigma}(B,u).
If the first-ranked account has uσ​(1)≥Bu\_{\sigma(1)}\geq B, then the queue allocates xσ​(1)Q=Bx^{Q}\_{\sigma(1)}=B and all others 0,
so z​(xQ)=B/uσ​(1)z(x^{Q})=B/u\_{\sigma(1)}.
Since n≥2n\geq 2 and ui>0u\_{i}>0 for all ii, we have uσ​(1)<Uu\_{\sigma(1)}<U, and therefore

|  |  |  |
| --- | --- | --- |
|  | z​(xQ)=Buσ​(1)>BU=z​(xMM).z(x^{Q})=\frac{B}{u\_{\sigma(1)}}>\frac{B}{U}=z(x^{\mathrm{MM}}). |  |

If instead uσ​(1)<Bu\_{\sigma(1)}<B, then the queue fully saturates σ​(1)\sigma(1), so xσ​(1)Q=uσ​(1)x^{Q}\_{\sigma(1)}=u\_{\sigma(1)}
and hence z​(xQ)=1z(x^{Q})=1.
Because 0<B<U0<B<U, we have B/U<1B/U<1, so again z​(xQ)=1>B/Uz(x^{Q})=1>B/U.
This proves ([46](https://arxiv.org/html/2602.15182v1#A3.E46 "In item 2 ‣ Proposition 9 (Duality-implied elimination of queue positions and dominance over queues). ‣ Min–max burden program and its dual. ‣ C.1 Duality and Queue Position ‣ Appendix C Queue Instability: Extreme-Point Selection ‣ Autodeleveraging as Online Learning")).

*Part 3 (Monotonicity and inversions).*
Under pro-rata, ri​(xMM)=ui−xiMM=(1−BU)​uir\_{i}(x^{\mathrm{MM}})=u\_{i}-x^{\mathrm{MM}}\_{i}=(1-\tfrac{B}{U})u\_{i},
so ui≥uj⇒ri​(xMM)≥rj​(xMM)u\_{i}\geq u\_{j}\Rightarrow r\_{i}(x^{\mathrm{MM}})\geq r\_{j}(x^{\mathrm{MM}}).

For a strict queue rule, pick any two indices i,ji,j with ui>uj>0u\_{i}>u\_{j}>0 and set B=uiB=u\_{i}.
Assume the queue ranks ii ahead of jj (this happens for some (s,σ)(s,\sigma) by strictness).
Then the queue fully exhausts ii: xi=uix\_{i}=u\_{i} and does not touch jj: xj=0x\_{j}=0.
Thus ri=0<rj=ujr\_{i}=0<r\_{j}=u\_{j}, which is a monotonicity violation (an inversion) in the post-ADL ordering.
∎

## Appendix D Execution-price estimation and failure metrics

This appendix formalizes bounds on the execution-estimation term introduced in Section [4.2](https://arxiv.org/html/2602.15182v1#S4.SS2 "4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning").
We (i) state the execution model and estimator assumptions, (ii) prove the regret–failure decomposition
([22](https://arxiv.org/html/2602.15182v1#S4.E22 "In Total Tracking Error Minimization. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning")), (iii) prove Proposition [10](https://arxiv.org/html/2602.15182v1#Thmproposition10 "Proposition 10 (Bounding 𝑉_𝑇 under a linear execution model). ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning"), and (iv) prove
Proposition [11](https://arxiv.org/html/2602.15182v1#Thmproposition11 "Proposition 11 (Queues induce Ω⁢(𝑇) effective execution nonstationarity under churn). ‣ D.5 A churn-robust instability result for queues ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning"), a churn-robust queue-instability result.

###### Proposition 10 (Bounding VTV\_{T} under a linear execution model).

Assume a scalar linear execution model with unknown impact slope αt∈[0,αmax]\alpha\_{t}\in[0,\alpha\_{\max}] and a per-round
quantity scale Qt≤QQ\_{t}\leq Q such that the ex post benchmark can be written as
Btneeded=αt​Qt2B\_{t}^{\mathrm{needed}}=\alpha\_{t}Q\_{t}^{2} and the ex ante benchmark as B^tneeded=α^t​Qt2\widehat{B}\_{t}^{\mathrm{needed}}=\hat{\alpha}\_{t}Q\_{t}^{2}.
Suppose the severity controller tracks the ex ante benchmark (Ht=B^tneededH\_{t}=\widehat{B}\_{t}^{\mathrm{needed}}) and the slope estimate
α^t\hat{\alpha}\_{t} is produced by projected online gradient descent on the convex losses |α−αt||\alpha-\alpha\_{t}| over [0,αmax][0,\alpha\_{\max}].
Then the cumulative undershoot satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | VT≤Q2​(C1​αmax​T+C2​PTα),V\_{T}\;\leq\;Q^{2}\Big(C\_{1}\,\alpha\_{\max}\sqrt{T}+C\_{2}\,P\_{T}^{\alpha}\Big), |  | (47) |

for universal constants C1,C2C\_{1},C\_{2}.

Note that Proposition [10](https://arxiv.org/html/2602.15182v1#Thmproposition10 "Proposition 10 (Bounding 𝑉_𝑇 under a linear execution model). ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") isolates the core mechanism: the variation of execution conditions across rounds,
captured by PTαP\_{T}^{\alpha}, governs cumulative failure more than the magnitude of any single round.
Large one-off deficits increase the scale through QQ, but sustained regime-switching in liquidity produces Ω​(T)\Omega(T) under-coverage
even when the controller is otherwise no-regret.

### D.1 Setup and notation

Fix a horizon of ADL rounds t=1,…,Tt=1,\dots,T. Let Ht=𝟏⊤​xtH\_{t}={\bf 1}^{\top}x\_{t} be the executed severity in dollars.
Let BtneededB\_{t}^{\mathrm{needed}} denote the ex post benchmark and B^tneeded\widehat{B}\_{t}^{\mathrm{needed}} the ex ante benchmark
computed from estimated quantities q^\hat{q} as in ([19](https://arxiv.org/html/2602.15182v1#S4.E19 "In Estimated versus ex post benchmarks. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning"))–([20](https://arxiv.org/html/2602.15182v1#S4.E20 "In Estimated versus ex post benchmarks. ‣ 4.2 Estimation of 𝑝ᵉˣᵉᶜ: tracking failure beyond regret ‣ 4 Regret Minimization ‣ Autodeleveraging as Online Learning")).
Define the cumulative undershoot (failure) metric

|  |  |  |
| --- | --- | --- |
|  | VT:=∑t=1T[Btneeded−Ht]+.V\_{T}:=\sum\_{t=1}^{T}[B\_{t}^{\mathrm{needed}}-H\_{t}]\_{+}. |  |

Define the deployed convex surrogate with target bb:

|  |  |  |
| --- | --- | --- |
|  | ℓt​(x;b):=λtrack​|𝟏⊤​x−b|+λfair​maxi∈Wt⁡xi,tui,t+ε.\ell\_{t}(x;b):=\lambda\_{\mathrm{track}}|{\bf 1}^{\top}x-b|+\lambda\_{\mathrm{fair}}\max\_{i\in W\_{t}}\frac{x\_{i,t}}{u\_{i,t}+\varepsilon}. |  |

Write ℓt​(x):=ℓt​(x;Btneeded)\ell\_{t}(x):=\ell\_{t}(x;B\_{t}^{\mathrm{needed}}) and ℓ^t​(x):=ℓt​(x;B^tneeded)\hat{\ell}\_{t}(x):=\ell\_{t}(x;\widehat{B}\_{t}^{\mathrm{needed}}).

### D.2 Execution model and estimator

We use a local directional linear impact model (a standard first-order approximation):
for a signed closeout quantity q≥0q\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ptliq,exec​(q)=ptmark−αt​q(sell / close long),p^{\mathrm{liq,exec}}\_{t}(q)=p^{\mathrm{mark}}\_{t}-\alpha\_{t}q\qquad\text{(sell / close long)}, |  | (48) |

and the symmetric buy-side variant ptliq,exec​(q)=ptmark+αt​qp^{\mathrm{liq,exec}}\_{t}(q)=p^{\mathrm{mark}}\_{t}+\alpha\_{t}q for closing shorts.
We treat αt∈[0,αmax]\alpha\_{t}\in[0,\alpha\_{\max}] as the local liquidity slope in round tt.

#### Scalar reduction.

To isolate the estimation channel, we work with an aggregated scalar sufficient statistic Qt≥0Q\_{t}\geq 0 (a round-level
quantity scale), and assume the benchmark can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Btneeded=αt​Qt2,B^tneeded=α^t​Qt2,Qt≤Q.B\_{t}^{\mathrm{needed}}=\alpha\_{t}Q\_{t}^{2},\qquad\widehat{B}\_{t}^{\mathrm{needed}}=\hat{\alpha}\_{t}Q\_{t}^{2},\qquad Q\_{t}\leq Q. |  | (49) |

This abstraction is justified by the fact that linear impact implies gap×\timesquantity is quadratic in a quantity scale.

#### Multiple fills and directionality

Extensions to multiple fills and directionality follow by summing quadratics, which preserves the same proof structure.

#### Online estimator.

We estimate αt\alpha\_{t} with projected online gradient descent on the convex losses

|  |  |  |
| --- | --- | --- |
|  | ϕt​(α):=|α−αt|,α∈[0,αmax],\phi\_{t}(\alpha):=|\alpha-\alpha\_{t}|,\qquad\alpha\in[0,\alpha\_{\max}], |  |

using the update

|  |  |  |
| --- | --- | --- |
|  | α^t+1=Π[0,αmax]​(α^t−η​gt),gt∈∂ϕt​(α^t).\hat{\alpha}\_{t+1}=\Pi\_{[0,\alpha\_{\max}]}\Big(\hat{\alpha}\_{t}-\eta\,g\_{t}\Big),\qquad g\_{t}\in\partial\phi\_{t}(\hat{\alpha}\_{t}). |  |

### D.3 Regret–failure decomposition

###### Lemma 2 (Loss perturbation bound).

For any xx and any targets b,b^b,\hat{b},

|  |  |  |
| --- | --- | --- |
|  | |ℓt​(x;b)−ℓt​(x;b^)|≤λtrack​|b−b^|.\big|\ell\_{t}(x;b)-\ell\_{t}(x;\hat{b})\big|\leq\lambda\_{\mathrm{track}}\,|b-\hat{b}|. |  |

###### Proof.

The fairness term does not depend on bb. For the tracking term,
||H−b|−|H−b^||≤|b−b^|\big||H-b|-|H-\hat{b}|\big|\leq|b-\hat{b}| by the reverse triangle inequality.
∎

###### Lemma 3 (Comparator transfer).

Let 𝒫\mathcal{P} be any comparator class. Then for any policy π\pi with sequence {xt}\{x\_{t}\},

|  |  |  |
| --- | --- | --- |
|  | ∑t=1Tℓt​(xt)≤minπ′∈𝒫​∑t=1Tℓt​(xtπ′)+RegT𝒫​(π;ℓ^)+2​λtrack​∑t=1T|Btneeded−B^tneeded|.\sum\_{t=1}^{T}\ell\_{t}(x\_{t})\leq\min\_{\pi^{\prime}\in\mathcal{P}}\sum\_{t=1}^{T}\ell\_{t}(x^{\pi^{\prime}}\_{t})+\mathrm{Reg}\_{T}^{\mathcal{P}}(\pi;\hat{\ell})+2\lambda\_{\mathrm{track}}\sum\_{t=1}^{T}|B\_{t}^{\mathrm{needed}}-\widehat{B}\_{t}^{\mathrm{needed}}|. |  |

###### Proof.

Apply Lemma [2](https://arxiv.org/html/2602.15182v1#Thmlemma2 "Lemma 2 (Loss perturbation bound). ‣ D.3 Regret–failure decomposition ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") to both π\pi and any comparator π′\pi^{\prime}:

|  |  |  |
| --- | --- | --- |
|  | ℓt​(xt)≤ℓ^t​(xt)+λtrack​|bt−b^t|,ℓ^t​(xtπ′)≤ℓt​(xtπ′)+λtrack​|bt−b^t|.\ell\_{t}(x\_{t})\leq\hat{\ell}\_{t}(x\_{t})+\lambda\_{\mathrm{track}}|b\_{t}-\hat{b}\_{t}|,\qquad\hat{\ell}\_{t}(x\_{t}^{\pi^{\prime}})\leq\ell\_{t}(x\_{t}^{\pi^{\prime}})+\lambda\_{\mathrm{track}}|b\_{t}-\hat{b}\_{t}|. |  |

Summing over tt and subtracting ∑tℓ^t​(xtπ′)\sum\_{t}\hat{\ell}\_{t}(x\_{t}^{\pi^{\prime}}) yields the claim after minimizing over π′∈𝒫\pi^{\prime}\in\mathcal{P}.
∎

### D.4 Proof of Proposition [10](https://arxiv.org/html/2602.15182v1#Thmproposition10 "Proposition 10 (Bounding 𝑉_𝑇 under a linear execution model). ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning")

###### Lemma 4 (Failure is optimistic estimation under target tracking).

If the controller tracks the ex ante benchmark exactly, i.e. Ht=B^tneededH\_{t}=\widehat{B}\_{t}^{\mathrm{needed}}, then

|  |  |  |
| --- | --- | --- |
|  | VT=∑t=1T[Btneeded−B^tneeded]+.V\_{T}=\sum\_{t=1}^{T}[B\_{t}^{\mathrm{needed}}-\widehat{B}\_{t}^{\mathrm{needed}}]\_{+}. |  |

###### Proof.

Immediate from the definition VT=∑t[Btneeded−Ht]+V\_{T}=\sum\_{t}[B\_{t}^{\mathrm{needed}}-H\_{t}]\_{+}.
∎

###### Lemma 5 (Quadratic scaling).

Under ([49](https://arxiv.org/html/2602.15182v1#A4.E49 "In Scalar reduction. ‣ D.2 Execution model and estimator ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning")),

|  |  |  |
| --- | --- | --- |
|  | [Btneeded−B^tneeded]+=[αt−α^t]+​Qt2≤|αt−α^t|​Qt2≤Q2​|αt−α^t|.[B\_{t}^{\mathrm{needed}}-\widehat{B}\_{t}^{\mathrm{needed}}]\_{+}=[\alpha\_{t}-\hat{\alpha}\_{t}]\_{+}\,Q\_{t}^{2}\leq|\alpha\_{t}-\hat{\alpha}\_{t}|\,Q\_{t}^{2}\leq Q^{2}\,|\alpha\_{t}-\hat{\alpha}\_{t}|. |  |

###### Proof.

Algebra plus Qt≤QQ\_{t}\leq Q.
∎

###### Lemma 6 (Dynamic tracking bound for the slope estimator).

Let PTα:=∑t=2T|αt−αt−1|P\_{T}^{\alpha}:=\sum\_{t=2}^{T}|\alpha\_{t}-\alpha\_{t-1}|.
There exist universal constants C1,C2C\_{1},C\_{2} and a choice of step size η\eta such that the projected OGD estimator satisfies

|  |  |  |
| --- | --- | --- |
|  | ∑t=1T|α^t−αt|≤C1​αmax​T+C2​PTα.\sum\_{t=1}^{T}|\hat{\alpha}\_{t}-\alpha\_{t}|\leq C\_{1}\,\alpha\_{\max}\sqrt{T}+C\_{2}\,P\_{T}^{\alpha}. |  |

###### Proof.

This is a specialization of standard mirror-descent dynamic-regret bounds to the 1D convex, 1-Lipschitz losses
ϕt​(α)=|α−αt|\phi\_{t}(\alpha)=|\alpha-\alpha\_{t}| on the diameter-αmax\alpha\_{\max} domain [0,αmax][0,\alpha\_{\max}].
Take the dynamic comparator αt⋆=αt\alpha\_{t}^{\star}=\alpha\_{t}, for which ∑tϕt​(αt⋆)=0\sum\_{t}\phi\_{t}(\alpha\_{t}^{\star})=0, so the dynamic regret upper bound
becomes an upper bound on ∑t|α^t−αt|\sum\_{t}|\hat{\alpha}\_{t}-\alpha\_{t}|.
Concretely, a standard bound of the form
RegTdyn≤O​(G​D​T+G​PTα)\mathrm{Reg}^{\mathrm{dyn}}\_{T}\leq O(GD\sqrt{T}+GP\_{T}^{\alpha}) with G=1G=1, D=αmaxD=\alpha\_{\max}
yields the stated form (absorbing constants).
∎

###### Proof of Proposition [10](https://arxiv.org/html/2602.15182v1#Thmproposition10 "Proposition 10 (Bounding 𝑉_𝑇 under a linear execution model). ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning").

By Lemma [4](https://arxiv.org/html/2602.15182v1#Thmlemma4 "Lemma 4 (Failure is optimistic estimation under target tracking). ‣ D.4 Proof of Proposition 10 ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") and Lemma [5](https://arxiv.org/html/2602.15182v1#Thmlemma5 "Lemma 5 (Quadratic scaling). ‣ D.4 Proof of Proposition 10 ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning"),

|  |  |  |
| --- | --- | --- |
|  | VT≤Q2​∑t=1T|α^t−αt|.V\_{T}\leq Q^{2}\sum\_{t=1}^{T}|\hat{\alpha}\_{t}-\alpha\_{t}|. |  |

Apply Lemma [6](https://arxiv.org/html/2602.15182v1#Thmlemma6 "Lemma 6 (Dynamic tracking bound for the slope estimator). ‣ D.4 Proof of Proposition 10 ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") to complete the proof.
∎

### D.5 A churn-robust instability result for queues

This section replaces the earlier two-account score-perturbation argument with a stronger churn-robust statement.
In practice, queue mechanisms frequently fully close early-ranked accounts, which removes them from the winner set and changes subsequent round geometry.
The result below shows that *this churn alone* is sufficient to induce Ω​(T)\Omega(T) effective execution nonstationarity.

###### Definition 3 (Churn / removal rule).

Fix initial winners W1W\_{1}. Given an allocation xtx\_{t}, define the next-round winner set by removing any fully
closed winner:

|  |  |  |
| --- | --- | --- |
|  | Wt+1:={i∈Wt:xi,t<ui}.W\_{t+1}:=\{i\in W\_{t}:x\_{i,t}<u\_{i}\}. |  |

That is, if an account is fully haircutted (xi,t=uix\_{i,t}=u\_{i}), it is closed and never returns.

###### Proposition 11 (Queues induce Ω​(T)\Omega(T) effective execution nonstationarity under churn).

Fix a horizon T≥2T\geq 2. Let the initial winner set contain N:=2​TN:=2T distinct accounts,
W1={1,2,…,2​T}W\_{1}=\{1,2,\dots,2T\}, each with identical capacity ui≡1u\_{i}\equiv 1.
Let the per-round budget be constant Bt≡1B\_{t}\equiv 1 and define executed quantities by qi,t​(π):=xi,t​(π)q\_{i,t}(\pi):=x\_{i,t}(\pi).
Assign per-account impact slopes alternating along the (fixed) queue order:

|  |  |  |
| --- | --- | --- |
|  | α2​k−1=αmin,α2​k=αmax,k=1,…,T,\alpha\_{2k-1}=\alpha\_{\min},\qquad\alpha\_{2k}=\alpha\_{\max},\qquad k=1,\dots,T, |  |

with 0≤αmin<αmax0\leq\alpha\_{\min}<\alpha\_{\max}.
Define the policy-induced effective slope by

|  |  |  |
| --- | --- | --- |
|  | α¯t​(π):=∑i∈Wtαi​qi,t​(π)2∑i∈Wtqi,t​(π)2.\bar{\alpha}\_{t}(\pi):=\frac{\sum\_{i\in W\_{t}}\alpha\_{i}\,q\_{i,t}(\pi)^{2}}{\sum\_{i\in W\_{t}}q\_{i,t}(\pi)^{2}}. |  |

Consider the greedy queue policy with fixed ordering σ​(i)=i\sigma(i)=i (no score perturbations) that fills budget
by fully closing the earliest available account. Under the churn rule above,

|  |  |  |
| --- | --- | --- |
|  | α¯t​(queue)∈{αmin,αmax}andPTα¯​(queue):=∑t=2T|α¯t​(queue)−α¯t−1​(queue)|=(T−1)​(αmax−αmin)=Ω​(T).\bar{\alpha}\_{t}(\mathrm{queue})\in\{\alpha\_{\min},\alpha\_{\max}\}\quad\text{and}\quad P\_{T}^{\bar{\alpha}(\mathrm{queue})}:=\sum\_{t=2}^{T}|\bar{\alpha}\_{t}(\mathrm{queue})-\bar{\alpha}\_{t-1}(\mathrm{queue})|=(T-1)(\alpha\_{\max}-\alpha\_{\min})=\Omega(T). |  |

In contrast, the pro-rata policy on the *same instance* allocates xi,tP​R=Bt/N=1/(2​T)x\_{i,t}^{PR}=B\_{t}/N=1/(2T) to every
account each round, so no account is fully closed for t≤Tt\leq T and therefore Wt≡W1W\_{t}\equiv W\_{1}.
Moreover α¯t​(pro​-​rata)≡(αmin+αmax)/2\bar{\alpha}\_{t}(\mathrm{pro\text{-}rata})\equiv(\alpha\_{\min}+\alpha\_{\max})/2 for all tt, hence
PTα¯​(pro​-​rata)=0P\_{T}^{\bar{\alpha}(\mathrm{pro\text{-}rata})}=0.

###### Proof.

*Queue.* Because Bt=1B\_{t}=1 and each active account has ui=1u\_{i}=1, the greedy queue allocation at round tt
places the entire budget on the first available account in the fixed ordering:

|  |  |  |
| --- | --- | --- |
|  | xtQ=et(in the initial indexing),xi,tQ=1​ for ​i=t,xi,tQ=0​ for ​i≠t,x^{Q}\_{t}=e\_{t}\quad\text{(in the initial indexing)},\qquad x^{Q}\_{i,t}=1\text{ for }i=t,\ \ x^{Q}\_{i,t}=0\text{ for }i\neq t, |  |

and then removes that fully closed account from Wt+1W\_{t+1}. With qi,t=xi,tq\_{i,t}=x\_{i,t}, we have
∑iqi,t2=1\sum\_{i}q\_{i,t}^{2}=1 and therefore

|  |  |  |
| --- | --- | --- |
|  | α¯t​(queue)=αt.\bar{\alpha}\_{t}(\mathrm{queue})=\alpha\_{t}. |  |

By construction αt\alpha\_{t} alternates between αmin\alpha\_{\min} and αmax\alpha\_{\max} across t=1,…,Tt=1,\dots,T, so
|α¯t−α¯t−1|=αmax−αmin|\bar{\alpha}\_{t}-\bar{\alpha}\_{t-1}|=\alpha\_{\max}-\alpha\_{\min} for each t≥2t\geq 2, yielding
PTα¯​(queue)=(T−1)​(αmax−αmin)P\_{T}^{\bar{\alpha}(\mathrm{queue})}=(T-1)(\alpha\_{\max}-\alpha\_{\min}).

*Pro-rata.* Pro-rata allocates xi,tP​R=1/(2​T)x\_{i,t}^{PR}=1/(2T) to each account each round. Over TT rounds, each
account receives total haircut T⋅(1/(2​T))=1/2<ui=1T\cdot(1/(2T))=1/2<u\_{i}=1, hence no account is fully closed and WtW\_{t} is constant.
Since all qi,t2q\_{i,t}^{2} are equal within a round, α¯t\bar{\alpha}\_{t} equals the average of the αi\alpha\_{i} values in W1W\_{1}.
Because exactly half of the accounts have slope αmin\alpha\_{\min} and half have αmax\alpha\_{\max}, this average is
(αmin+αmax)/2(\alpha\_{\min}+\alpha\_{\max})/2, constant over tt. Thus PTα¯​(pro​-​rata)=0P\_{T}^{\bar{\alpha}(\mathrm{pro\text{-}rata})}=0.
∎

###### Remark 1 (Interpretation).

Proposition [11](https://arxiv.org/html/2602.15182v1#Thmproposition11 "Proposition 11 (Queues induce Ω⁢(𝑇) effective execution nonstationarity under churn). ‣ D.5 A churn-robust instability result for queues ‣ Appendix D Execution-price estimation and failure metrics ‣ Autodeleveraging as Online Learning") shows that queue-induced churn can convert *static* cross-sectional
heterogeneity (fixed {αi}\{\alpha\_{i}\}) into *maximally nonstationary* time-series behavior in the effective
execution slope. This removes repeated-account availability and round-by-round score-perturbation assumptions.