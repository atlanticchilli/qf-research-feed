---
authors:
- Nikhil Devanathan
- Logan Bell
- Dylan Rueter
- Stephen Boyd
doc_id: arxiv:2603.07881v1
family_id: arxiv:2603.07881
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Distributed Method for Cooperative Transaction Cost Mitigation
url_abs: http://arxiv.org/abs/2603.07881v1
url_html: https://arxiv.org/html/2603.07881v1
venue: arXiv q-fin
version: 1
year: 2026
---


Nikhil Devanathan
  
Logan Bell
  
Dylan Rueter
  
Stephen Boyd

###### Abstract

Funds at large portfolio management firms may consist of many portfolio
managers (PMs), each managing a portion of the fund and optimizing a
distinct objective. Although the PMs determine
their trades independently, the trade lists may be netted and executed by the
firm. These net trades may be sufficiently large to impact the market prices,
so the PMs may realize prices on their trades that are different
from the observed midpoint price of the assets before execution. These
transaction costs generally reduce the returns of a portfolio over time. We
propose a simple protocol, based on methods from distributed convex
optimization, by which a firm can communicate estimated transaction costs to
its PMs, and the PMs can potentially revise their
trades to realize reduced transaction costs. This protocol does not require the
PMs to disclose their method of determining trades to the firm
or to each other, nor does it require the PMs to communicate
their trade lists with each other. As the number of adjustment rounds grows,
the trades converge to the ones that are optimal for the firm. As a practical
matter we observe that even just a few rounds of adjustment lead to substantial
savings for the firm and the PMs.

## 1 Introduction

#### The coordination problem.

We consider the setting of a systematic firm with multiple PMs managing
independent investment sleeves (sub-portfolios) of a single fund111This paper is a purely mathematical contribution to distributed
optimization in the context of portfolio management. It does not
describe, reference, or prescribe the practices of any specific firm.
By *netting* trade lists, we refer to the mathematical aggregation
of individual trade lists into a single net trade vector. In practice,
the internal crossing of trade lists is a regulated activity; we
exclusively consider the case in which crossing is entirely permissible
and make no assertions about its applicability in any particular
regulatory or operational context.
We assume, as a modeling abstraction, that there exists a central entity
within the firm charged with aggregating the PMs’ trade lists and
executing the resulting net trade on the market. This is a simplifying
modeling device.
Finally, we use the term *cooperative* throughout this paper in its
game-theoretic sense, and not
in the colloquial sense of informal coordination or agreement between
parties..
Each PM determines their desired trading actions by
solving a specific optimization problem, but the outcomes of these actions
are often coupled at the firm level. This coupling arises when the cost or
utility realized by the firm depends on the aggregate actions of the PMs.

A primary example of this is netted transaction costs. The firm may net the
trade lists of all the PMs and execute the net trade on the market. Trading
impacts market prices, resulting in transaction costs that depend on the
aggregate trades. Similar coupling can arise from shared borrow costs or
firmwide risk constraints. The challenge is to coordinate the PMs to optimize a
global firm objective while respecting the autonomy and private information of
the individual PMs.

#### Joint transaction cost optimization.

We assume that all PMs determine their trade lists by solving an optimization
problem, typically convex, that takes into account their views of future risk
and returns, the cost of holding short positions, and the cost of trading, as
well as portfolio specific constraints, such as limits on what assets can be
held. To find the optimal trades taking the netted transaction cost into
account, we can collect all PMs’ optimization problems, sum their objectives,
and subtract the transaction cost associated with the net trades. The
individual optimization problems associated with each portfolio are now coupled
through the net trade transaction cost. If the optimization problems used by
each PM are convex, we obtain a large convex optimization problem, which
determines all trades simultaneously, minimizing the total transaction cost to the
firm, in addition to maximizing each PM’s objective. We refer to this as the
joint problem, since all the trades are found by solving a single optimization
problem that takes the net trade transaction cost into account.

#### Distributed solution of the joint problem.

We propose a distributed method to solve the joint problem. This iterative
method proceeds in rounds in which each PM adjusts their trade lists. In each
round each PM communicates their proposed trade list to a central
entity within the firm. The central entity nets the trade lists and
broadcasts back to the PMs information about the net trades. Based on this
information each PM modifies their optimization problem slightly, adding a
discount or premium to each asset, to account for the net trade transaction
cost.

The specific methods that the central entity and the PMs use come directly
from well-known methods for distributed optimization. Because of this, if the
adjustment rounds are continued, the PM trade lists converge to their joint
optimal values. But in this distributed method the PMs never divulge their
trade lists, or their strategies, to other PMs or indeed even the central
entity. In each round they simply take in information from the central
entity, modify their problems, and solve them to obtain the modified trade
list.

We observe that in practice, just a few rounds of adjustment are enough to
substantially reduce the transaction cost to the firm.

### 1.1 Prior work

#### Transaction costs.

Transaction costs have been extensively studied in the context of portfolio
optimization. Many works have examined modeling transaction costs, and some
common models include a linear transaction cost model
[[LCP+19](#bib.bib10 "Transaction costs of factor-investing strategies"), [LEL00](#bib.bib12 "Optimal portfolio management with transactions costs and capital gains taxes")], a quadratic
transaction cost model [[CLR+19](#bib.bib14 "A note on portfolio optimization with quadratic transaction costs")], and a 3/2-power transaction cost
model [[BBD+17](#bib.bib11 "Multi-period trading via convex optimization"), [BJK+24](#bib.bib5 "Markowitz portfolio construction at seventy")]. Other works have considered
piecewise-affine transaction cost models [[BVF+19](#bib.bib6 "Dealing with complex transaction costs in portfolio management")] and a model
where the transaction cost is a fixed fraction of the portfolio value
[[MP95](#bib.bib7 "OPTIMAL portfolio management with fixed transaction costs"), [MOG15](#bib.bib9 "Portfolio optimization and transaction costs")]. These works largely build on
Markowitz’s mean-variance optimization framework [[MAR52](#bib.bib15 "PORTFOLIO selection")]
and integrate transaction costs into a Markowitz portfolio optimization
problem. All of these papers, however, only consider the problem of optimizing
the portfolio of a single PM.

#### Distributed optimization.

In the context of jointly optimizing the objectives of multiple agents in a
distributed setting, operator splitting methods such as the alternating
direction method of multipliers (ADMM) are well studied
[[BPC+10](#bib.bib1 "Distributed optimization and statistical learning via the alternating direction method of multipliers"), [RY22](#bib.bib2 "Large-scale convex optimization: algorithms & analyses via monotone operators"), [CHW15](#bib.bib17 "Multi-agent distributed optimization via inexact consensus admm"), [SYP16](#bib.bib18 "Fast admm algorithm for distributed optimization with adaptive penalty"), [YGJ+22](#bib.bib19 "A survey of admm variants for distributed optimization: problems, algorithms and features")].
We refer to a survey of methods in distributed optimization for a thorough
discussion of other methods used to solve multi-agent sharing problems
[[YYW+19](#bib.bib16 "A survey of distributed optimization")]. In portfolio optimization, distributed methods have been
studied to allow multiple agents to collaboratively optimize a single portfolio
based on observations each agent has made of asset returns and covariances
[[CS13](#bib.bib20 "Distributed pareto optimization via diffusion strategies")].

## 2 Mathematical formulation

### 2.1 Preliminaries

There are MM PMs at the same firm, each of whom manages a
portfolio of NN assets, but with different goals and mandates. Each portfolio
manager ii has a net asset value (NAV) Vi>0V^{i}>0, and the firm’s total NAV
is V=∑i=1MViV=\sum\_{i=1}^{M}V^{i}. We define the relative
NAV weight of each PM as λi=Vi/V\lambda^{i}=V^{i}/V.

Each PM determines their trades in terms of portfolio weights.
We denote the trade weight vector of PM ii as xi∈RNx^{i}\in{\mbox{\bf R}}^{N}, where xjix^{i}\_{j} is the change in weight allocated to asset jj, with
xji<0x^{i}\_{j}<0 meaning a reduction in weight. The corresponding trade list in
shares is xi​Vi/px^{i}V^{i}/p, where p∈R++Np\in{\mbox{\bf R}}\_{++}^{N} is the vector of asset
prices and the division is elementwise.

The firm collects the trades and executes the net trade in the market. Since
portfolios have different sizes, the firm’s net trade weight is the
NAV-weighted sum of individual trade weights:

|  |  |  |
| --- | --- | --- |
|  | z=∑i=1Mλi​xi.z=\sum\_{i=1}^{M}\lambda^{i}x^{i}. |  |

If zj=0z\_{j}=0, it means that shares of asset jj are exchanged between the MM
funds in proportion to their NAVs, and none are transacted in the market. The
net trade in shares is z​V/pzV/p.

When the trade lists are produced, the asset prices are given by pref∈R++Np\_{\text{ref}}\in{\mbox{\bf R}}\_{++}^{N}, so the reference cost of the net trade is (pref)T​(z​V/pref)=V​𝟏T​z(p\_{\text{ref}})^{T}(zV/p\_{\text{ref}})=V\mathbf{1}^{T}z. The trades
are executed at the realized prices preal∈R++Np\_{\text{real}}\in{\mbox{\bf R}}^{N}\_{++}, and the
realized cost differs due to market impact. The difference is interpreted as a
transaction cost, which is typically nonnegative, although it can be negative
if the trades of portfolio ii tend to go against the net trades, i.e., xjix^{i}\_{j}
and zjz\_{j} have different signs.

#### Transaction cost models.

There are many models of transaction cost. Since transaction costs depend on
the actual shares traded, we express them in terms of the net trade weight zz
and the firm’s total NAV. The simplest model includes only the bid-ask price
spread of each asset. Here, the reference price is the midpoint of the bid and
ask prices when the trade lists are produced, but we execute purchases at the
ask price and sales at the bid price. The resulting transaction cost is (1/2)​κT​|z|(1/2)\kappa^{T}|z|, where κj\kappa\_{j} is the bid-ask spread of asset jj expressed as
a fraction of price (unitless), and the absolute value is taken elementwise.
More complex models also take into account the effect of large orders eating
through the order book. One common form, expressed in terms of trade weights,
is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕtc​(z)=(1/2)​κspreadT​|z|+κimpactT​|z|3/2,\phi^{\text{tc}}(z)=(1/2)\kappa\_{\text{spread}}^{T}|z|+\kappa\_{\text{impact}}^{T}|z|^{3/2}, |  | (1) |

with

|  |  |  |
| --- | --- | --- |
|  | (κimpact)j=bj​νjωj/V(\kappa\_{\text{impact}})\_{j}=\frac{b\_{j}\nu\_{j}}{\sqrt{\omega\_{j}/V}} |  |

where (κspread)j(\kappa\_{\text{spread}})\_{j} is the bid-ask spread of asset jj expressed
as a fraction of price (unitless); bjb\_{j} is the market impact coefficient for
asset jj (unitless); νj\nu\_{j} is the returns volatility of asset jj (unitless)
over the period considered for optimization; and ωj\omega\_{j} is the dollar volume of
asset jj over the period considered for optimization. The ratio ωj/V\omega\_{j}/V can be interpreted as the market volume expressed in units of
portfolio weight. The 3/23/2 power is taken elementwise. This models the
(predicted) transaction cost to execute the net trade zz, expressed as a
fraction of NAV.

#### Portfolio manager objectives.

We suppose that PM ii
has a closed, convex, proper objective function
fi:RN→R∪{+∞}f^{i}:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}\cup\{+\infty\} such that fi​(x)f^{i}(x) represents the
negative of the PM’s expected return net of fees and costs
(possibly risk adjusted), expressed as a fraction of NAV, for trade weights x∈RNx\in{\mbox{\bf R}}^{N}, for i=1,…,Mi=1,\ldots,M. This formulation ensures that all portfolio
manager objectives are of similar scale and directly comparable.
Additionally, we assume that portfolio
manager ii determines their trade weights xix^{i} such that
xi=arg⁡minx⁡fi​(x)x^{i}=\arg\min\_{x}f^{i}(x). Note that fif^{i} can incorporate constraints. For
example, if PM ii solves the problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimizef~i​(xi)subject toxi∈𝒳i,\begin{array}[]{ll}\mbox{minimize}&\tilde{f}^{i}(x^{i})\\ \mbox{subject to}&x^{i}\in\mathcal{X}^{i},\end{array} |  | (2) |

with variable xix^{i}, where 𝒳i\mathcal{X}^{i} is the set of feasible trade weights
for PM ii, then fi​(xi)=f~i​(xi)+I𝒳i​(xi)f^{i}(x^{i})=\tilde{f}^{i}(x^{i})+I\_{\mathcal{X}^{i}}(x^{i}), where
I𝒳iI\_{\mathcal{X}^{i}} is the indicator function of the feasible set
𝒳i\mathcal{X}^{i}. This construction is used in §[4](#S4 "4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"). Common
constraints that may be included in 𝒳i\mathcal{X}^{i} include risk limits
(bounding portfolio volatility), turnover limits (restricting the magnitude of
trades), leverage constraints (bounding the sum of absolute weights), and
active risk constraints (requiring that the optimized portfolio has limited
deviation from a target or benchmark portfolio).

#### Firm objective.

The firm’s goal is to enable the portfolio
managers to achieve their objectives, while simultaneously minimizing the
transaction costs incurred by the firm as a whole. The firm’s total ex
ante penalty is therefore the NAV-weighted sum of the PMs’ objective functions
plus the modeled transaction cost of the net trade. The problem of minimizing
this total penalty can be formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimize∑i=1Mλi​fi​(xi)+γtc​ϕtc​(z)subject toz=∑i=1Mλi​xi\begin{array}[]{ll}\mbox{minimize}&\sum\_{i=1}^{M}\lambda^{i}f^{i}(x^{i})+\gamma\_{\text{tc}}\phi^{\text{tc}}(z)\\ \mbox{subject to}&z=\sum\_{i=1}^{M}\lambda^{i}x^{i}\end{array} |  | (3) |

where γtc>0\gamma\_{\text{tc}}>0 is a scaling parameter for the transaction cost
term. The NAV weights λi\lambda^{i} ensure that the contribution of each PM to
the firm objective is proportional to their portfolio size. The inclusion of
γtc\gamma\_{\text{tc}} is a practical matter: scaling the transaction cost term
often improves firm performance.

#### Note.

The formulation ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) describes the
problem of minimizing the penalty to the firm as a whole (or equivalently,
maximizing the firm’s reward). Since the trade weights of the PMs
are coupled through the transaction cost term in the objective, the trades
of each PM will be influenced by the trades of the other
PMs. It is indeterminate how this will affect the performance
of every PM. We will show in appendix [B](#A2 "Appendix B Portfolio manager results ‣ A Distributed Method for Cooperative Transaction Cost Mitigation") that it
is demonstrably not the case that every PM will realize greater
performance by cooperating in this manner as opposed to acting independently. As
such, solving ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) is primarily of interest to firms that view
each PM as an investible asset. Such firms are only concerned
with the performance of the whole portfolio (the firm) and not the individual
assets (the PMs).

In principle, PMs could game the system by artificially scaling
up their objective functions (say, by a factor of 1000) to receive priority in
the firm optimization. However, we assume such gaming does not occur, as we
consider the cooperative case where PMs act in good faith toward
the firm objective.

### 2.2 Alternating direction method of multipliers

The alternating direction method of multipliers (ADMM) is a well-known
iterative method [[BPC+10](#bib.bib1 "Distributed optimization and statistical learning via the alternating direction method of multipliers")] that can be used to solve problems
of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimizef​(x)+g​(z)subject toA​x+B​z=c\begin{array}[]{ll}\mbox{minimize}&f(x)+g(z)\\ \mbox{subject to}&Ax+Bz=c\end{array} |  | (4) |

with variables x∈Rnx\in{\mbox{\bf R}}^{n} and z∈Rmz\in{\mbox{\bf R}}^{m}, where A∈Rp×nA\in{\mbox{\bf R}}^{p\times n}, B∈Rp×mB\in{\mbox{\bf R}}^{p\times m}, and c∈Rpc\in{\mbox{\bf R}}^{p} are constants. The ADMM
algorithm is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xk+1\displaystyle x^{k+1} | =\displaystyle= | argminx(f​(x)+(uk)T​(A​x+B​zk−c)+ρ2​‖A​x+B​zk−c‖22)\displaystyle\mathop{\rm argmin}\_{x}\left(f(x)+(u^{k})^{T}(Ax+Bz^{k}-c)+\frac{\rho}{2}\|Ax+Bz^{k}-c\|\_{2}^{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | zk+1\displaystyle z^{k+1} | =\displaystyle= | argminz(g​(z)+(uk)T​(A​xk+1+B​z−c)+ρ2​‖A​xk+1+B​z−c‖22)\displaystyle\mathop{\rm argmin}\_{z}\left(g(z)+(u^{k})^{T}(Ax^{k+1}+Bz-c)+\frac{\rho}{2}\|Ax^{k+1}+Bz-c\|\_{2}^{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uk+1\displaystyle u^{k+1} | =\displaystyle= | uk+φ​ρ​(A​xk+1+B​zk+1−c)\displaystyle u^{k}+\varphi\rho(Ax^{k+1}+Bz^{k+1}-c) |  |

where ρ>0\rho>0 is a penalty parameter and φ∈(0,1+52)\varphi\in(0,\frac{1+\sqrt{5}}{2})
is a step-size parameter [[RY22](#bib.bib2 "Large-scale convex optimization: algorithms & analyses via monotone operators")].

#### Reformulating the firm problem.

To apply ADMM, we first introduce the NAV-scaled trade weights x~i=λi​xi\tilde{x}^{i}=\lambda^{i}x^{i}, which represent the contribution of PM ii to the firm’s net
trade. The firm problem ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) can then be written as

|  |  |  |
| --- | --- | --- |
|  | minimize∑i=1Mλi​fi​(x~i/λi)+g​(z)subject to∑i=1Mx~i−z=0\begin{array}[]{ll}\mbox{minimize}&\sum\_{i=1}^{M}\lambda^{i}f^{i}(\tilde{x}^{i}/\lambda^{i})+g(z)\\ \mbox{subject to}&\sum\_{i=1}^{M}\tilde{x}^{i}-z=0\end{array} |  |

where g​(z)=ϕtc​(z)+I𝒵​(z)g(z)=\phi^{\text{tc}}(z)+I\_{\mathcal{Z}}(z) is the sum of the
transaction cost and the indicator function of the feasible set 𝒵\mathcal{Z}.
Following the dummy variables technique described in
[[RY22](#bib.bib2 "Large-scale convex optimization: algorithms & analyses via monotone operators"), Chapter 8], we introduce new variables
z1,…,zM∈RNz^{1},\ldots,z^{M}\in{\mbox{\bf R}}^{N} and eliminate zz to obtain the equivalent problem

|  |  |  |
| --- | --- | --- |
|  | minimize∑i=1Mλi​fi​(x~i/λi)+g​(∑i=1Mzi)subject tox~i−zi=0,i=1,…,M.\begin{array}[]{ll}\mbox{minimize}&\sum\_{i=1}^{M}\lambda^{i}f^{i}(\tilde{x}^{i}/\lambda^{i})+g(\sum\_{i=1}^{M}z^{i})\\ \mbox{subject to}&\tilde{x}^{i}-z^{i}=0,\quad i=1,\ldots,M.\end{array} |  |

To improve practical convergence, we introduce a diagonal scaling matrix
D∈R++N×ND\in{\mbox{\bf R}}\_{++}^{N\times N} and scale the constraints by DD to obtain the
equivalent problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimize∑i=1Mλi​fi​(x~i/λi)+g​(∑i=1Mzi)subject toD​x~i−D​zi=0,i=1,…,M.\begin{array}[]{ll}\mbox{minimize}&\sum\_{i=1}^{M}\lambda^{i}f^{i}(\tilde{x}^{i}/\lambda^{i})+g(\sum\_{i=1}^{M}z^{i})\\ \mbox{subject to}&D\tilde{x}^{i}-Dz^{i}=0,\quad i=1,\ldots,M.\end{array} |  | (5) |

As shown in appendix [A](#A1 "Appendix A ADMM for the firm problem ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"), applying ADMM to problem
([5](#S2.E5 "In Reformulating the firm problem. ‣ 2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) with initial dual variables satisfying
u1,0=⋯=uM,0u^{1,0}=\cdots=u^{M,0} allows us to derive the update rules. Writing the
updates in terms of the original PM trade weights xi=x~i/λix^{i}=\tilde{x}^{i}/\lambda^{i}
and defining the sharing update signal

|  |  |  |
| --- | --- | --- |
|  | ℓk=uk+ρM​(−D​zsumk+D​∑j=1Mλj​xj,k),\ell^{k}=u^{k}+\frac{\rho}{M}\left(-Dz\_{\text{sum}}^{k}+D\sum\_{j=1}^{M}\lambda^{j}x^{j,k}\right), |  |

we obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xi,k+1\displaystyle x^{i,k+1} | =\displaystyle= | argminx(λi​fi​(x)+λi​(ℓk)T​D​x+ρ2​‖λi​D​(x−xi,k)‖22)\displaystyle\mathop{\rm argmin}\_{x}\left(\lambda^{i}f^{i}(x)+\lambda^{i}(\ell^{k})^{T}Dx+\frac{\rho}{2}\|\lambda^{i}D(x-x^{i,k})\|\_{2}^{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | zsumk+1\displaystyle z\_{\text{sum}}^{k+1} | =\displaystyle= | argminz(g​(z)−(uk)T​D​z+ρ2​M​‖D​z−∑i=1Mλi​D​xi,k+1‖22)\displaystyle\mathop{\rm argmin}\_{z}\left(g(z)-(u^{k})^{T}Dz+\frac{\rho}{2M}\|Dz-{\textstyle\sum\_{i=1}^{M}\lambda^{i}Dx^{i,k+1}}\|\_{2}^{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uk+1\displaystyle u^{k+1} | =\displaystyle= | uk+φ​ρM​(−D​zsumk+1+∑j=1Mλj​D​xj,k+1)\displaystyle u^{k}+\frac{\varphi\rho}{M}(-Dz\_{\text{sum}}^{k+1}+{\textstyle\sum\_{j=1}^{M}\lambda^{j}Dx^{j,k+1}}) |  |

### 2.3 Protocol

The ADMM updates for solving ([5](#S2.E5 "In Reformulating the firm problem. ‣ 2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) can be computed in a
distributed manner, such that the PMs do not need to share their
objectives with each other or with the firm. Our distributed protocol works by
performing a fixed number of iterations of ADMM. While this does not produce an
exact solution to ([5](#S2.E5 "In Reformulating the firm problem. ‣ 2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")), we show empirically in
§[4](#S4 "4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation") that even a few ADMM iterations is sufficient to
substantially refine the trade lists proposed by the PMs.

Algorithm 1  Transaction cost mitigation protocol

1:Initialization:

2: Fix iteration count KK, step-size φ\varphi, penalty parameter ρ\rho, and diagonal scaling matrix D∈R++N×ND\in{\mbox{\bf R}}\_{++}^{N\times N}

3: Portfolio managers initialize: xi,0←argminxfi​(x)x^{i,0}\leftarrow\mathop{\rm argmin}\_{x}f^{i}(x) for i=1,…,Mi=1,\ldots,M

4: Central planner receives NAV-weighted net trade ∑i=1Mλi​xi,0\sum\_{i=1}^{M}\lambda^{i}x^{i,0} and initializes zsum0z\_{\text{sum}}^{0}, u0←𝟎Nu^{0}\leftarrow\mathbf{0}\_{N}

5:

6:for k=0,1,…,K−1k=0,1,\ldots,K-1 do

7:  Step 1: Distributed update

8:   Central planner broadcasts signal:

9:    ℓk←uk+ρM​(−D​zsumk+D​∑i=1Mλi​xi,k)\ell^{k}\leftarrow u^{k}+\frac{\rho}{M}\left(-Dz\_{\text{sum}}^{k}+D\sum\_{i=1}^{M}\lambda^{i}x^{i,k}\right)

10:   Each PM ii updates:

11:    xi,k+1←argminx(λi​fi​(x)+λi​(ℓk)T​D​x+ρ2​‖λi​D​(x−xi,k)‖22)x^{i,k+1}\leftarrow\mathop{\rm argmin}\_{x}\left(\lambda^{i}f^{i}(x)+\lambda^{i}(\ell^{k})^{T}Dx+\frac{\rho}{2}\|\lambda^{i}D(x-x^{i,k})\|\_{2}^{2}\right)

12:

13:  Step 2: Gathered update

14:   Central planner receives NAV-weighted net trade ∑i=1Mλi​xi,k+1\sum\_{i=1}^{M}\lambda^{i}x^{i,k+1} and updates:

15:    zsumk+1←argminz(g​(z)−(uk)T​D​z+ρ2​M​‖D​z−D​∑i=1Mλi​xi,k+1‖22)z\_{\text{sum}}^{k+1}\leftarrow\mathop{\rm argmin}\_{z}\left(g(z)-(u^{k})^{T}Dz+\frac{\rho}{2M}\left\|Dz-D\sum\_{i=1}^{M}\lambda^{i}x^{i,k+1}\right\|\_{2}^{2}\right)

16:    uk+1←uk+φ​ρM​(D​∑i=1Mλi​xi,k+1−D​zsumk+1)u^{k+1}\leftarrow u^{k}+\frac{\varphi\rho}{M}\left(D\sum\_{i=1}^{M}\lambda^{i}x^{i,k+1}-Dz\_{\text{sum}}^{k+1}\right)

#### Comments.

The PM update in Step 1 can be interpreted as re-solving the PM’s original
optimization problem with two modifications: a linear price adjustment term
(ℓk)T​D​x(\ell^{k})^{T}Dx that encodes discounts or premiums based on the net trade, and a
quadratic stability penalty ρ2​‖λi​D​(x−xi,k)‖22\frac{\rho}{2}\|\lambda^{i}D(x-x^{i,k})\|\_{2}^{2} that
discourages large deviations from the previous trade list.

Notice that in the proposed algorithm, none of the PMs share their
trade lists with other PMs, and the PMs do not
share their objectives with the central planner. This structure preserves privacy
and prevents undesirable competition between PMs while also
minimizing costs for the entire firm.

### 2.4 Hyperparameters and tuning

#### Choice of scaling matrix.

The diagonal scaling matrix DD is used to improve
practical convergence of the algorithm.
The choice of DD can be motivated by approximating
the transaction cost function. We can approximate the 3/23/2-power model with a
simpler one that is quadratic in trades, ϕ~tc​(z)=κspreadT​|z|+zT​𝐝𝐢𝐚𝐠(κimpact)​z\tilde{\phi}^{\text{tc}}(z)=\kappa\_{\text{spread}}^{T}|z|+z^{T}\mathop{\bf diag{}}(\kappa\_{\text{impact}})z. The Hessian of the
quadratic part of this approximation is 2​𝐝𝐢𝐚𝐠(κimpact)2\mathop{\bf diag{}}(\kappa\_{\text{impact}}). In ADMM,
the quadratic penalty on the consensus variable is weighted by D2D^{2}. A common
heuristic is to align this penalty with the curvature of the objective by setting
D2D^{2} to be proportional to the Hessian of the centralized cost function’s
quadratic part. This suggests the practical choice Dj​j=2​(κimpact)jD\_{jj}=\sqrt{2(\kappa\_{\text{impact}})\_{j}}.

#### Choice of penalty and dual extrapolation parameters.

From [[RY22](#bib.bib2 "Large-scale convex optimization: algorithms & analyses via monotone operators")], the objective value will converge to the global
optimum if ρ>0\rho>0 and φ∈(0,1+52)\varphi\in(0,\frac{1+\sqrt{5}}{2}). The penalty
parameter ρ\rho controls the strength of the consensus constraint, where
smaller values of ρ\rho result in larger changes in each iteration. While
larger steps may seem desirable, excessively large steps may lead to
overcorrection. The dual extrapolation parameter φ\varphi controls the dual
variable update; a common choice is φ=1\varphi=1, though values up to
1+52≈1.618\frac{1+\sqrt{5}}{2}\approx 1.618 can accelerate convergence. Empirically, we
find the choices ρ=10.0\rho=10.0 and φ=1\varphi=1 to work well in the backtest in
§[4](#S4 "4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").

#### Choice of iteration count.

As the iteration count KK is increased, the resulting trade lists will more
closely approximate the solution to ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")). As such, for firms
that prioritize the firm’s returns and desire to solve ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"))
exactly, a larger KK is preferred. For firms that prioritize the independence
of the PMs and wish only to provide a mechanism for the
PMs to account for transaction costs, a smaller value of KK
(such as K=1K=1) will minimally alter the initial trade lists of the portfolio
managers while potentially providing a substantial benefit in terms of
transaction cost mitigation.

## 3 Extensions and variations

#### Firmwide constraints.

The firm might have constraints on the
aggregate trades and portfolio weights. For example, market availability
imposes box constraints on the net trade weights zz. The firm might also have
constraints that limit the net exposure to any one asset class, limit the
leverage, or limit the turnover. We denote the set of feasible aggregate trade
weights as 𝒵\mathcal{Z}. In this case, the firm’s problem becomes

|  |  |  |
| --- | --- | --- |
|  | minimize∑i=1Mλi​fi​(xi)+ϕtc​(z)subject toz=∑i=1Mλi​xiz∈𝒵.\begin{array}[]{ll}\mbox{minimize}&\sum\_{i=1}^{M}\lambda^{i}f^{i}(x^{i})+\phi^{\text{tc}}(z)\\ \mbox{subject to}&z=\sum\_{i=1}^{M}\lambda^{i}x^{i}\\ &z\in\mathcal{Z}.\end{array} |  |

This problem can be written in the form ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) by taking

|  |  |  |
| --- | --- | --- |
|  | ϕ~tc​(z)={ϕtc​(z),if z∈𝒵+∞,otherwise.\tilde{\phi}^{\text{tc}}(z)=\begin{cases}\phi^{\text{tc}}(z),&\text{if $z\in\mathcal{Z}$}\\ +\infty,&\text{otherwise.}\end{cases} |  |

This is a convex function when 𝒵\mathcal{Z} is convex. Algorithm [1](#alg1 "Algorithm 1 ‣ 2.3 Protocol ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")
then applies.

#### Shorting costs.

When the firm nets positions across portfolio
managers, it only pays borrowing costs on the net short position rather than the
gross short positions of individual portfolios. This coupling can be
incorporated into the framework by adding a shorting cost term
ϕshort​(z)\phi^{\text{short}}(z) to the firm objective in ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")), and the
ADMM updates extend naturally. Other coupling terms arising from shared
resources or firmwide constraints can be handled similarly.

## 4 Backtest

We present a backtest of our protocol
over historical data to illustrate the potential returns that can be
achieved by mitigating transaction costs in a firm-wide manner.
The code to reproduce our experiment can be found at

> <https://github.com/cvxgrp/coop_t_code>.

### 4.1 Backtest setup

#### Data.

We use historical market data for U.S. equities obtained from the LSEG (Refinitiv)
database. Our universe consists of N=434N=434 assets drawn from historical S&P 500
constituents, filtered to those with sufficient data history and sorted by market
capitalization at the end of the sample period. For each asset, we obtain adjusted
daily trade prices, bid and ask prices, and trading volumes, where the adjustments
account for stock splits and dividends. The bid-ask spread, used in
the transaction cost model ([1](#S2.E1 "In Transaction cost models. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")), is computed as the absolute difference
between ask and bid prices. Missing values are forward-filled. We also obtain the
3-month U.S. Treasury Bill rate from the Federal Reserve Economic Data (FRED)
database, which serves as the risk-free rate rrfr\_{\text{rf}} in the PM
objectives. The data spans July 2000 to April 2025.

This asset selection procedure introduces survivorship and lookahead bias, as we
select assets based on their market capitalization at the end of the sample period
rather than at each point in time. This is acceptable for our purposes: the goal is
to evaluate the relative benefit of the cooperative protocol compared to independent
optimization, not to demonstrate an investable strategy. Since both protocols
operate on the same asset universe, the comparison remains valid.

#### Transaction cost model.

The transaction cost model ([1](#S2.E1 "In Transaction cost models. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) requires the spread parameter
κspread\kappa\_{\text{spread}}, the market impact coefficient bb, the volatility
ν\nu, and the dollar volume ω\omega for each asset. The spread parameter is
obtained directly from the bid-ask spread data. We set the market impact
coefficient bj=1b\_{j}=1 for all assets. The volatility νj\nu\_{j} is taken from the
diagonal of the factor model covariance estimate described below. The dollar
volume ωj\omega\_{j} is computed as the product of the trading volume in shares and the
asset price. For shorting costs, we use the risk-free rate as a proxy for the
borrow cost, applied uniformly across all assets.

#### Policies.

We simulate a firm with M=4M=4 PMs. In each period of the backtest, each
PM determines their desired trades by solving the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimize−αT​w−rrf​c+γrisk​srisk+γturn​sturn+γtc​ϕtc​(z)+γshort​ϕshort​(z)subject tow−wcurr=z1−𝟏T​w=c‖w‖1≤L|w|≤C𝟏T​max⁡(0,−w)≤S‖w−wcurr‖2+|c−ccurr|≤2​T+sturn‖Σ1/2​w‖2≤σtarget+srisk\begin{array}[]{ll}\mbox{minimize}&-\alpha^{T}w-r\_{\text{rf}}c+\gamma\_{\text{risk}}s\_{\text{risk}}+\gamma\_{\text{turn}}s\_{\text{turn}}+\gamma\_{\text{tc}}\phi^{\text{tc}}(z)+\gamma\_{\text{short}}\phi^{\text{short}}(z)\\ \mbox{subject to}&w-w\_{\text{curr}}=z\\ &1-\mathbf{1}^{T}w=c\\ &\|w\|\_{1}\leq L\\ &|w|\leq C\\ &\mathbf{1}^{T}\max(0,-w)\leq S\\ &\|w-w\_{\text{curr}}\|\_{2}+|c-c\_{\text{curr}}|\leq 2T+s\_{\text{turn}}\\ &\|\Sigma^{1/2}w\|\_{2}\leq\sigma\_{\text{target}}+s\_{\text{risk}}\end{array} |  | (6) |

with NN tradable assets and:

* •

  Variables:

  + –

    w∈RNw\in{\mbox{\bf R}}^{N}, portfolio weights
  + –

    c∈Rc\in{\mbox{\bf R}}, cash position
  + –

    z∈RNz\in{\mbox{\bf R}}^{N}, trade weights
  + –

    srisk∈R+s\_{\text{risk}}\in{\mbox{\bf R}}\_{+}, risk slack variable
  + –

    sturn∈R+s\_{\text{turn}}\in{\mbox{\bf R}}\_{+}, turnover slack variable
* •

  Data:

  + –

    wcurr∈RNw\_{\text{curr}}\in{\mbox{\bf R}}^{N}, current portfolio weights
  + –

    ccurr∈Rc\_{\text{curr}}\in{\mbox{\bf R}}, current cash position
  + –

    rrf∈Rr\_{\text{rf}}\in{\mbox{\bf R}}, risk-free rate
* •

  Models:

  + –

    α∈RN\alpha\in{\mbox{\bf R}}^{N}, expected asset returns
  + –

    Σ∈RN×N\Sigma\in{\mbox{\bf R}}^{N\times N}, asset covariance matrix
  + –

    ϕtc:RN→R+\phi^{\text{tc}}:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}\_{+}, transaction cost function
  + –

    ϕshort:RN→R+\phi^{\text{short}}:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}\_{+}, shorting cost function,
    ϕshort​(w)=rrf​∑j=1Nmax⁡(0,−wj)\phi^{\text{short}}(w)=r\_{\text{rf}}\sum\_{j=1}^{N}\max(0,-w\_{j})
* •

  Parameters:

  + –

    L∈R+L\in{\mbox{\bf R}}\_{+}, leverage limit
  + –

    C∈R+C\in{\mbox{\bf R}}\_{+}, concentration limit
  + –

    S∈R+S\in{\mbox{\bf R}}\_{+}, shorting limit
  + –

    T∈R+T\in{\mbox{\bf R}}\_{+}, turnover limit
  + –

    σtarget∈R+\sigma\_{\text{target}}\in{\mbox{\bf R}}\_{+}, target risk
  + –

    γrisk∈R++\gamma\_{\text{risk}}\in{\mbox{\bf R}}\_{++}, risk penalty weight
  + –

    γturn∈R++\gamma\_{\text{turn}}\in{\mbox{\bf R}}\_{++}, turnover penalty weight
  + –

    γtc∈R++\gamma\_{\text{tc}}\in{\mbox{\bf R}}\_{++}, transaction cost penalty weight
  + –

    γshort∈R++\gamma\_{\text{short}}\in{\mbox{\bf R}}\_{++}, shorting cost penalty weight

Each PM solves an optimization problem of the form above, with
identical constraint parameters but differing in their alpha estimates α\alpha,
risk targets σtarget\sigma\_{\text{target}}, tradable asset universes, and initial net
asset values (NAVs). The common parameters used across all PMs
are listed in Table [1](#S4.T1 "Table 1 ‣ Policies. ‣ 4.1 Backtest setup ‣ 4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"). These values represent typical
institutional constraints and are consistent with parameters used in prior work
on systematic portfolio optimization [[BJK+24](#bib.bib5 "Markowitz portfolio construction at seventy")]. The risk targets
σtarget\sigma\_{\text{target}} are drawn uniformly at random from [6%,15%][6\%,15\%]
annualized, and the initial NAVs are drawn log-uniformly from 106.510^{6.5} to
107.510^{7.5} dollars. Each PM is assigned a random subset of 75%
of the assets in the universe that they can trade and hold.

| Parameter | Symbol | Value |
| --- | --- | --- |
| Leverage limit | LL | 1.5 |
| Concentration limit | CC | 0.2 |
| Shorting limit | SS | 0.5 |
| Turnover limit | TT | 0.2 |
| Risk penalty weight | γrisk\gamma\_{\text{risk}} | 20 |
| Turnover penalty weight | γturn\gamma\_{\text{turn}} | 1 |
| Transaction cost coefficient | γtc\gamma\_{\text{tc}} | 0.15 |
| Shorting cost coefficient | γshort\gamma\_{\text{short}} | 1 |

Table 1: Common constraint and penalty parameters used across all PMs.

All PMs
use a common risk model. The details of the PM alphas, asset
universes, and common risk model are described in the following paragraphs.

This formulation is inspired by the paper [[BJK+24](#bib.bib5 "Markowitz portfolio construction at seventy")], and is intended
to represent a reasonable method for systematic portfolio optimization. This problem
is an instance of problem ([2](#S2.E2 "In Portfolio manager objectives. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")).

#### Cooperative protocols.

We implement and compare four models
(protocols) of PM cooperation:

* •

  independent: The baseline protocol where each portfolio
  manager solves their optimization problem independently, accounting for
  their own estimated transaction costs without coordination.
* •

  full\_cooperative: An idealized protocol that solves problem
  ([3](#S2.E3 "In Firm objective. ‣ 2.1 Preliminaries ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) directly, combining all PMs’ objectives
  into a single optimization problem with a joint transaction cost term applied
  to the net firm trade and a firm-wide shorting cost term as described in
  §[3](#S3 "3 Extensions and variations ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"). The transaction and shorting cost terms are scaled by
  γtc\gamma\_{\text{tc}} and γshort\gamma\_{\text{short}}, respectively, matching the
  parameters used in the individual PM policies. This requires gathering all
  the problem data from the PMs to solve as implemented.
* •

  admm\_2\_iter: The distributed ADMM protocol described in
  §[2.3](#S2.SS3 "2.3 Protocol ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation") with K=2K=2 iterations, which approximately solves the same
  problem as full\_cooperative without requiring PMs
  to share their complete objectives with the firm or each other. The ADMM
  hyperparameters are set as described in §[2.4](#S2.SS4 "2.4 Hyperparameters and tuning ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* •

  admm\_5\_iter: The ADMM protocol with K=5K=5 iterations,
  providing a closer approximation to the full\_cooperative solution.

#### Synthetic alpha generation.

To evaluate our protocol under controlled conditions, we generate synthetic
alpha estimates with known statistical properties rather than using proprietary
trading signals. Each PM receives a noised estimate of future
returns, calibrated to achieve a target Information Coefficient (IC)—the
cross-sectional correlation between the alpha estimate and realized returns.

For PM ii, the synthetic alpha estimate at time tt is

|  |  |  |
| --- | --- | --- |
|  | R^t(i)=c(i)​(Rt+Et(i)),\hat{R}\_{t}^{(i)}=c^{(i)}(R\_{t}+E\_{t}^{(i)}), |  |

where Rt∈RNR\_{t}\in{\mbox{\bf R}}^{N} is the vector of realized returns over a 42-day
forward-looking window, Et(i)∈RNE\_{t}^{(i)}\in{\mbox{\bf R}}^{N} is a noise vector, and
c(i)>0c^{(i)}>0 is a scaling factor. The noise variance is calibrated such that
the correlation between R^t(i)\hat{R}\_{t}^{(i)} and RtR\_{t} equals the target IC for
strategy ii. Specifically, if the target IC is ρ(i)\rho^{(i)}, then the scaling
factor is c(i)=(ρ(i))2c^{(i)}=(\rho^{(i)})^{2} and the noise scaling factor is
v(i)=1/(ρ(i))2−1v^{(i)}=\sqrt{1/(\rho^{(i)})^{2}-1}.

The noise process EtE\_{t} (stacked across all strategies) follows a vector
autoregressive process of order 1 (VAR(1)):

|  |  |  |
| --- | --- | --- |
|  | Et=Φ​Et−1+Ut,E\_{t}=\Phi E\_{t-1}+U\_{t}, |  |

where Φ\Phi is a block-diagonal matrix with strategy-specific temporal
autocorrelation coefficients ϕ(i)\phi^{(i)} on the diagonal blocks, and UtU\_{t} is
an innovation vector. The stationary covariance of EtE\_{t} has the Kronecker
structure ΣE=SE⊗ΣAsset\Sigma\_{E}=S\_{E}\otimes\Sigma\_{\text{Asset}}, where
ΣAsset\Sigma\_{\text{Asset}} is the empirical asset return covariance and SES\_{E}
encodes cross-strategy correlations scaled by the noise factors v(i)v^{(i)}. The
innovation covariance ΣU\Sigma\_{U} is determined from the discrete-time Lyapunov
equation ΣE=Φ​ΣE​ΦT+ΣU\Sigma\_{E}=\Phi\Sigma\_{E}\Phi^{T}+\Sigma\_{U}. The synthetic alpha
parameters are summarized in Table [2](#S4.T2 "Table 2 ‣ Synthetic alpha generation. ‣ 4.1 Backtest setup ‣ 4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").

| Parameter | Value |
| --- | --- |
| Target IC (per PM) | 𝒰​[0.06,0.10]\mathcal{U}[0.06,0.10] |
| Temporal autocorrelation ϕ(k)\phi^{(k)} | 𝒰​[0.75,0.85]\mathcal{U}[0.75,0.85] |
| Cross-strategy noise correlation | 0.30.3 |
| Forward return horizon | 42 days |

Table 2: Synthetic alpha generation parameters. 𝒰​[a,b]\mathcal{U}[a,b] denotes a
uniform distribution over [a,b][a,b].

Note that these alpha estimates are not
investable in practice, as they rely on noised versions of true future returns,
which are unknowable. The PMs and their alpha models should be
treated as proxies for realistic systematic portfolio optimization strategies
rather than as implementable trading strategies.

#### Covariance matrix estimation.

All PMs share a common
risk model based on a low-rank factor structure. For each time tt, we estimate
the covariance matrix Σt=Ft​FtT+Dt\Sigma\_{t}=F\_{t}F\_{t}^{T}+D\_{t}, where Ft∈RN×JF\_{t}\in{\mbox{\bf R}}^{N\times J} is the factor loading matrix with J=15J=15 factors, and Dt∈RN×ND\_{t}\in{\mbox{\bf R}}^{N\times N} is a diagonal matrix of idiosyncratic variances.

The estimation procedure uses a 42-day forward-looking window. At each time tt,
we compute the realized returns over the subsequent 42 trading days and estimate
per-asset volatilities as the standard deviation over this window. Returns are
standardized by these volatilities and winsorized at ±4.2\pm 4.2 standard
deviations to reduce the influence of outliers. We then compute the sample
correlation matrix of the winsorized standardized returns and extract the top
JJ eigenvectors and eigenvalues. The factor loadings are constructed as Ft=diag​(σt)​Qt​Λt1/2F\_{t}=\text{diag}(\sigma\_{t})Q\_{t}\Lambda\_{t}^{1/2}, where σt\sigma\_{t} is the vector of
asset volatilities, QtQ\_{t} contains the top JJ eigenvectors, and Λt\Lambda\_{t} is
the diagonal matrix of corresponding eigenvalues. The idiosyncratic variances
are set to the residual variance not explained by the factors.

This forward-looking estimation is not implementable in practice, as it uses
future information. However, for the purpose of evaluating the cooperative
trading protocol under controlled conditions, this approach ensures that the
risk model accurately reflects the true covariance structure during the backtest
period.

### 4.2 Results

In Table [3](#S4.T3 "Table 3 ‣ 4.2 Results ‣ 4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"), we present the top-level performance statistics
for the firm in each of the backtest scenarios. Since the underlying strategies are
synthetic, the absolute performance figures are not meaningful in themselves; what
matters is the relative improvement achieved through cooperation. We observe that
the cooperative protocols all significantly outperform the independent protocol in
terms of return, volatility, and Sharpe ratio. In comparison, the difference between the ADMM protocols
and the full joint protocol is not as pronounced, and all three attain nearly identical
Sharpe ratios. We break down the performance by PM in appendix [B](#A2 "Appendix B Portfolio manager results ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").

|  | Return | Volatility | Sharpe |
| --- | --- | --- | --- |
| independent | 15.63%15.63\% | 9.77%9.77\% | 1.601.60 |
| full\_cooperative | 17.59%17.59\% | 8.58%8.58\% | 2.052.05 |
| admm\_2\_iter | 18.70%18.70\% | 9.16%9.16\% | 2.042.04 |
| admm\_5\_iter | 18.63%18.63\% | 8.96%8.96\% | 2.082.08 |

Table 3: Performance statistics by backtest scenario.

![Refer to caption](2603.07881v1/x1.png)


Figure 1: Firm’s cumulative returns by backtest scenario.

![Refer to caption](2603.07881v1/x2.png)


Figure 2: Firm’s cumulative transaction costs by backtest scenario.

We show the firm’s cumulative returns and cumulative transaction costs in each backtest
scenario in Figures [1](#S4.F1 "Figure 1 ‣ 4.2 Results ‣ 4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation") and [2](#S4.F2 "Figure 2 ‣ 4.2 Results ‣ 4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"), respectively.
As should be expected, the full joint protocol achieves the lowest
transaction costs, and more iterations of the ADMM protocol seem to result in lower
transaction costs. Performing 2 iterations of ADMM already achieves a substantial
reduction in transaction costs, and performing 5 iterations yields approximately 75%
of the savings of the full joint protocol, and there is very little difference between
the cumulative returns of the ADMM protocols and the full joint protocol.

## 5 Conclusion

We have presented a distributed protocol, based on ADMM, that enables portfolio
managers within a firm to coordinate their trades and reduce transaction costs
without revealing their objectives to each other or to the firm. Our
backtest demonstrates that even a small number of coordination rounds can
substantially reduce the transaction costs incurred by the firm on its net
trades.

It is important to note the limitations of this approach. The protocol does not
guarantee improved returns or Sharpe ratios for the firm or for individual
PMs. The effect on PM-level performance is
indeterminate: while we expect every PM to experience reduced
transaction costs through cooperation, this does not necessarily translate to
improved returns, as the coordination may alter the composition of trades in
ways that affect other aspects of performance. What this method does provide is
a principled mechanism for reducing frictional costs that would otherwise erode
returns.

For firms structured as collections of independent sleeves or subsidiary funds,
where net trades are executed centrally, this protocol offers a practical path
to capturing the benefits of trade netting while preserving the autonomy and
privacy of individual PMs.

## 6 Acknowledgements

We thank Ronald Kahn for helpful discussions about transaction cost models.

## References

* [BVF+19]
  P. Beraldi, A. Violi, M. Ferrara, C. Ciancio, and B. A. Pansera (2019-04)
  Dealing with complex transaction costs in portfolio management.
  Annals of Operations Research 299 (1–2),  pp. 7–22.
  External Links: ISSN 1572-9338,
  [Link](http://dx.doi.org/10.1007/s10479-019-03210-5),
  [Document](https://dx.doi.org/10.1007/s10479-019-03210-5)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [BJK+24]
  S. Boyd, K. Johansson, R. Kahn, P. Schiele, and T. Schmelzer (2024-06)
  Markowitz portfolio construction at seventy.
  The Journal of Portfolio Management 50 (8),  pp. 117–160.
  External Links: ISSN 2168-8656,
  [Link](http://dx.doi.org/10.3905/jpm.2024.50.8.117),
  [Document](https://dx.doi.org/10.3905/jpm.2024.50.8.117)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"),
  [§4.1](#S4.SS1.SSS0.Px3.p2.6 "Policies. ‣ 4.1 Backtest setup ‣ 4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"),
  [§4.1](#S4.SS1.SSS0.Px3.p4.1 "Policies. ‣ 4.1 Backtest setup ‣ 4 Backtest ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [BBD+17]
  S. P. Boyd, E. Busseti, S. Diamond, R. N. Kahn, K. Koh, P. Nystrup, and J. Speth (2017)
  Multi-period trading via convex optimization.
  Found. Trends Optim. 3 (1),  pp. 1–76.
  External Links: [Link](https://doi.org/10.1561/2400000023),
  [Document](https://dx.doi.org/10.1561/2400000023)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [BPC+10]
  S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein (2010)
  Distributed optimization and statistical learning via the alternating direction method of multipliers.
  Foundations and Trends in Machine Learning 3 (1),  pp. 1–122.
  Cited by: [§1.1](#S1.SS1.SSS0.Px2.p1.1 "Distributed optimization. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"),
  [§2.2](#S2.SS2.p1.8 "2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [CHW15]
  T. Chang, M. Hong, and X. Wang (2015)
  Multi-agent distributed optimization via inexact consensus admm.
  IEEE Transactions on Signal Processing 63 (2),  pp. 482–497.
  External Links: [Document](https://dx.doi.org/10.1109/TSP.2014.2367458)
  Cited by: [§1.1](#S1.SS1.SSS0.Px2.p1.1 "Distributed optimization. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [CS13]
  J. Chen and A. H. Sayed (2013)
  Distributed pareto optimization via diffusion strategies.
  IEEE Journal of Selected Topics in Signal Processing 7 (2),  pp. 205–220.
  External Links: [Document](https://dx.doi.org/10.1109/JSTSP.2013.2246763)
  Cited by: [§1.1](#S1.SS1.SSS0.Px2.p1.1 "Distributed optimization. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [CLR+19]
  P. Chen, E. Lezmi, T. Roncalli, and J. Xu (2019)
  A note on portfolio optimization with quadratic transaction costs.
  SSRN Electronic Journal.
  External Links: ISSN 1556-5068,
  [Link](http://dx.doi.org/10.2139/ssrn.3683466),
  [Document](https://dx.doi.org/10.2139/ssrn.3683466)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [LEL00]
  H. E. Leland (2000)
  Optimal portfolio management with transactions costs and capital gains taxes.
  SSRN Electronic Journal.
  External Links: ISSN 1556-5068,
  [Link](http://dx.doi.org/10.2139/ssrn.206871),
  [Document](https://dx.doi.org/10.2139/ssrn.206871)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [LCP+19]
  F. Li, T. Chow, A. Pickard, and Y. Garg (2019-03)
  Transaction costs of factor-investing strategies.
  Financial Analysts Journal 75 (2),  pp. 62–78.
  External Links: ISSN 1938-3312,
  [Link](http://dx.doi.org/10.1080/0015198X.2019.1567190),
  [Document](https://dx.doi.org/10.1080/0015198x.2019.1567190)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [MOG15]
  R. Mansini, W. Ogryczak, and M. Grazia Speranza (2015-05-11)
  Portfolio optimization and transaction costs.
  In Quantitative Financial Risk Management,
   pp. 212–241.
  External Links: ISBN 9781119080305,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1002/9781119080305.ch8),
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119080305.ch8),
  https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781119080305.ch8
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [MAR52]
  H. Markowitz (1952-03)
  PORTFOLIO selection.
  The Journal of Finance 7 (1),  pp. 77–91.
  External Links: ISSN 1540-6261,
  [Link](http://dx.doi.org/10.1111/j.1540-6261.1952.tb01525.x),
  [Document](https://dx.doi.org/10.1111/j.1540-6261.1952.tb01525.x)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [MP95]
  A. J. Morton and S. R. Pliska (1995-10)
  OPTIMAL portfolio management with fixed transaction costs.
  Mathematical Finance 5 (4),  pp. 337–356.
  External Links: ISSN 1467-9965,
  [Link](http://dx.doi.org/10.1111/j.1467-9965.1995.tb00071.x),
  [Document](https://dx.doi.org/10.1111/j.1467-9965.1995.tb00071.x)
  Cited by: [§1.1](#S1.SS1.SSS0.Px1.p1.1 "Transaction costs. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [RY22]
  E. K. Ryu and W. Yin (2022-11)
  Large-scale convex optimization: algorithms & analyses via monotone operators.
   Cambridge University Press.
  External Links: ISBN 9781009160858,
  [Link](http://dx.doi.org/10.1017/9781009160865),
  [Document](https://dx.doi.org/10.1017/9781009160865)
  Cited by: [§1.1](#S1.SS1.SSS0.Px2.p1.1 "Distributed optimization. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"),
  [§2.2](#S2.SS2.SSS0.Px1.p1.6 "Reformulating the firm problem. ‣ 2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"),
  [§2.2](#S2.SS2.p1.7 "2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"),
  [§2.4](#S2.SS4.SSS0.Px2.p1.9 "Choice of penalty and dual extrapolation parameters. ‣ 2.4 Hyperparameters and tuning ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [SYP16]
  C. Song, S. Yoon, and V. Pavlovic (2016-02)
  Fast admm algorithm for distributed optimization with adaptive penalty.
  Proceedings of the AAAI Conference on Artificial Intelligence 30 (1).
  External Links: ISSN 2159-5399,
  [Link](http://dx.doi.org/10.1609/aaai.v30i1.10069),
  [Document](https://dx.doi.org/10.1609/aaai.v30i1.10069)
  Cited by: [§1.1](#S1.SS1.SSS0.Px2.p1.1 "Distributed optimization. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [YYW+19]
  T. Yang, X. Yi, J. Wu, Y. Yuan, D. Wu, Z. Meng, Y. Hong, H. Wang, Z. Lin, and K. H. Johansson (2019)
  A survey of distributed optimization.
  Annual Reviews in Control 47,  pp. 278–305.
  External Links: ISSN 1367-5788,
  [Link](http://dx.doi.org/10.1016/j.arcontrol.2019.05.006),
  [Document](https://dx.doi.org/10.1016/j.arcontrol.2019.05.006)
  Cited by: [§1.1](#S1.SS1.SSS0.Px2.p1.1 "Distributed optimization. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
* [YGJ+22]
  Y. Yang, X. Guan, Q. Jia, L. Yu, B. Xu, and C. J. Spanos (2022)
  A survey of admm variants for distributed optimization: problems, algorithms and features.
   arXiv.
  External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2208.03700),
  [Link](https://arxiv.org/abs/2208.03700)
  Cited by: [§1.1](#S1.SS1.SSS0.Px2.p1.1 "Distributed optimization. ‣ 1.1 Prior work ‣ 1 Introduction ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").

## Appendix A ADMM for the firm problem

Recall that we define the NAV-scaled trade weights x~i=λi​xi\tilde{x}^{i}=\lambda^{i}x^{i}. Applying ADMM to ([5](#S2.E5 "In Reformulating the firm problem. ‣ 2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation")) yields the iterates (written in
terms of x~i\tilde{x}^{i}):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x~i,k+1\displaystyle\tilde{x}^{i,k+1} | =\displaystyle= | argminx~(λi​fi​(x~/λi)+(ui,k)T​(D​x~−D​zi,k)+ρ2​‖D​x~−D​zi,k‖22)\displaystyle\mathop{\rm argmin}\_{\tilde{x}}\left(\lambda^{i}f^{i}(\tilde{x}/\lambda^{i})+(u^{i,k})^{T}(D\tilde{x}-Dz^{i,k})+\frac{\rho}{2}\|D\tilde{x}-Dz^{i,k}\|\_{2}^{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | zk+1\displaystyle z^{k+1} | =\displaystyle= | argmin(z1,…,zM)(g​(∑i=1Mzi)+∑i=1M[(ui,k)T​(D​x~i,k+1−D​zi)+ρ2​‖D​x~i,k+1−D​zi‖22])\displaystyle\mathop{\rm argmin}\_{(z^{1},\ldots,z^{M})}\left(g({\textstyle\sum\_{i=1}^{M}z^{i}})+\sum\_{i=1}^{M}\left[(u^{i,k})^{T}(D\tilde{x}^{i,k+1}-Dz^{i})+\frac{\rho}{2}\|D\tilde{x}^{i,k+1}-Dz^{i}\|\_{2}^{2}\right]\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ui,k+1\displaystyle u^{i,k+1} | =\displaystyle= | ui,k+φ​ρ​(D​x~i,k+1−D​zi,k+1).\displaystyle u^{i,k}+\varphi\rho(D\tilde{x}^{i,k+1}-Dz^{i,k+1}). |  |

If ADMM is initialized with u1,0=⋯=uM,0u^{1,0}=\cdots=u^{M,0}, then
u1,k=⋯=uM,ku^{1,k}=\cdots=u^{M,k} and D​x~1,k−D​z1,k=⋯=D​x~M,k−D​zM,kD\tilde{x}^{1,k}-Dz^{1,k}=\cdots=D\tilde{x}^{M,k}-Dz^{M,k} at
each iteration kk. We can show this inductively. Suppose
u1,k=⋯=uM,ku^{1,k}=\cdots=u^{M,k} and rewrite the zz-update by introducing auxiliary
variable zsumz\_{\text{sum}}, solving the problem

|  |  |  |
| --- | --- | --- |
|  | minimizeg​(zsum)−(uk)T​(D​zsum)+∑i=1Mρ2​‖D​x~i,k+1−D​zi‖22subject to∑i=1Mzi=zsum\begin{array}[]{ll}\mbox{minimize}&g(z\_{\text{sum}})-(u^{k})^{T}(Dz\_{\text{sum}})+\sum\_{i=1}^{M}\frac{\rho}{2}\|D\tilde{x}^{i,k+1}-Dz^{i}\|\_{2}^{2}\\ \mbox{subject to}&\sum\_{i=1}^{M}z^{i}=z\_{\text{sum}}\end{array} |  |

with variables z1,…,zMz^{1},\ldots,z^{M} and zsumz\_{\text{sum}}. Solving first for
z1,…,zMz^{1},\ldots,z^{M} and then for zsumz\_{\text{sum}} gives
zi,k+1=x~i,k+1−1M​∑j=1Mx~j,k+1+1M​zsumk+1z^{i,k+1}=\tilde{x}^{i,k+1}-\frac{1}{M}\sum\_{j=1}^{M}\tilde{x}^{j,k+1}+\frac{1}{M}z\_{\text{sum}}^{k+1}, where zsumk+1z\_{\text{sum}}^{k+1} is given
by

|  |  |  |
| --- | --- | --- |
|  | zsumk+1=argminz(g​(z)−(uk)T​D​z+ρ2​M​‖D​z−∑i=1MD​x~i,k+1‖22).z\_{\text{sum}}^{k+1}=\mathop{\rm argmin}\_{z}\left(g(z)-(u^{k})^{T}Dz+\frac{\rho}{2M}\|Dz-{\textstyle\sum\_{i=1}^{M}D\tilde{x}^{i,k+1}}\|\_{2}^{2}\right). |  |

In particular,
D​x~i,k+1−D​zi,k+1=−1M​D​zsumk+1+1M​∑j=1MD​x~j,k+1D\tilde{x}^{i,k+1}-Dz^{i,k+1}=-\frac{1}{M}Dz\_{\text{sum}}^{k+1}+\frac{1}{M}\sum\_{j=1}^{M}D\tilde{x}^{j,k+1} for i=1,…,Mi=1,\ldots,M, which is constant across ii. Consequently,
from the uu-update

|  |  |  |
| --- | --- | --- |
|  | ui,k+1=uk+φ​ρ​(D​x~i,k+1−D​zi,k+1)=uk+φ​ρM​(−D​zsumk+1+∑j=1MD​x~j,k+1),u^{i,k+1}=u^{k}+\varphi\rho(D\tilde{x}^{i,k+1}-Dz^{i,k+1})=u^{k}+\frac{\varphi\rho}{M}(-Dz\_{\text{sum}}^{k+1}+{\textstyle\sum\_{j=1}^{M}D\tilde{x}^{j,k+1}}), |  |

we also have u1,k+1=⋯=uM,k+1u^{1,k+1}=\cdots=u^{M,k+1}.

We can also rewrite the x~\tilde{x}-update in terms of zsumz\_{\text{sum}}. Substituting
zi,k=x~i,k−1M​∑j=1Mx~j,k+1M​zsumkz^{i,k}=\tilde{x}^{i,k}-\frac{1}{M}\sum\_{j=1}^{M}\tilde{x}^{j,k}+\frac{1}{M}z\_{\text{sum}}^{k}
into the x~\tilde{x}-update, expanding the quadratic term, and eliminating terms
constant with respect to x~\tilde{x}, and defining the sharing update signal

|  |  |  |
| --- | --- | --- |
|  | ℓk=uk+ρM​(−D​zsumk+D​∑j=1Mx~j,k),\ell^{k}=u^{k}+\frac{\rho}{M}\left(-Dz\_{\text{sum}}^{k}+D\sum\_{j=1}^{M}\tilde{x}^{j,k}\right), |  |

we get

|  |  |  |
| --- | --- | --- |
|  | x~i,k+1=argminx~(λi​fi​(x~/λi)+(ℓk)T​D​x~+ρ2​‖D​x~−D​x~i,k‖22).\tilde{x}^{i,k+1}=\mathop{\rm argmin}\_{\tilde{x}}\left(\lambda^{i}f^{i}(\tilde{x}/\lambda^{i})+(\ell^{k})^{T}D\tilde{x}+\frac{\rho}{2}\|D\tilde{x}-D\tilde{x}^{i,k}\|\_{2}^{2}\right). |  |

Substituting x~=λi​x\tilde{x}=\lambda^{i}x and x~j,k=λj​xj,k\tilde{x}^{j,k}=\lambda^{j}x^{j,k}
and simplifying, we obtain the update in terms of the original PM trade weights xix^{i}:

|  |  |  |
| --- | --- | --- |
|  | xi,k+1=argminx(λi​fi​(x)+λi​(ℓk)T​D​x+ρ2​‖λi​D​(x−xi,k)‖22).x^{i,k+1}=\mathop{\rm argmin}\_{x}\left(\lambda^{i}f^{i}(x)+\lambda^{i}(\ell^{k})^{T}Dx+\frac{\rho}{2}\|\lambda^{i}D(x-x^{i,k})\|\_{2}^{2}\right). |  |

Combining these new iterates gives the update rules described in
§[2.2](#S2.SS2 "2.2 Alternating direction method of multipliers ‣ 2 Mathematical formulation ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").

## Appendix B Portfolio manager results

Figures [6](#A2.F6 "Figure 6 ‣ Appendix B Portfolio manager results ‣ A Distributed Method for Cooperative Transaction Cost Mitigation") and [10](#A2.F10 "Figure 10 ‣ Appendix B Portfolio manager results ‣ A Distributed Method for Cooperative Transaction Cost Mitigation") show the PM’s
cumulative returns and cumulative transaction costs by backtest scenario, respectively.
Backtest statistics for each PM are presented in Table [7](#A2.T7 "Table 7 ‣ Appendix B Portfolio manager results ‣ A Distributed Method for Cooperative Transaction Cost Mitigation").
We do expect that every PM experiences
lower transaction costs, which we see in Figure [10](#A2.F10 "Figure 10 ‣ Appendix B Portfolio manager results ‣ A Distributed Method for Cooperative Transaction Cost Mitigation"), but this method
offers no guarantee that every PM realizes greater returns or Sharpe
ratio through cooperation. In particular, we observe that PM 2 experiences worse
performance through cooperation compared to optimizing independently post 2010.

![Refer to caption](2603.07881v1/x3.png)


(a) PM 1

![Refer to caption](2603.07881v1/x4.png)


(a) PM 2

![Refer to caption](2603.07881v1/x5.png)


(a) PM 3


![Refer to caption](2603.07881v1/x6.png)


(a) PM 4



Figure 6: Portfolio managers’ cumulative returns by backtest scenario.

![Refer to caption](2603.07881v1/x7.png)


(a) PM 1

![Refer to caption](2603.07881v1/x8.png)


(a) PM 2

![Refer to caption](2603.07881v1/x9.png)


(a) PM 3


![Refer to caption](2603.07881v1/x10.png)


(a) PM 4



Figure 10: Portfolio managers’ cumulative transaction costs by backtest scenario.



|  | Return | Volatility | Sharpe |
| --- | --- | --- | --- |
| independent | 15.45%15.45\% | 12.57%12.57\% | 1.231.23 |
| full\_cooperative | 18.23%18.23\% | 11.14%11.14\% | 1.641.64 |
| admm\_2\_iter | 19.15%19.15\% | 11.85%11.85\% | 1.621.62 |
| admm\_5\_iter | 19.42%19.42\% | 11.65%11.65\% | 1.671.67 |

(a) PM 1



|  | Return | Volatility | Sharpe |
| --- | --- | --- | --- |
| independent | 14.79%14.79\% | 13.38%13.38\% | 1.101.10 |
| full\_cooperative | 14.39%14.39\% | 12.39%12.39\% | 1.161.16 |
| admm\_2\_iter | 15.70%15.70\% | 12.95%12.95\% | 1.211.21 |
| admm\_5\_iter | 15.49%15.49\% | 12.67%12.67\% | 1.221.22 |

(a) PM 2



|  | Return | Volatility | Sharpe |
| --- | --- | --- | --- |
| independent | 19.02%19.02\% | 12.34%12.34\% | 1.541.54 |
| full\_cooperative | 20.54%20.54\% | 11.34%11.34\% | 1.811.81 |
| admm\_2\_iter | 21.87%21.87\% | 11.69%11.69\% | 1.871.87 |
| admm\_5\_iter | 21.65%21.65\% | 11.42%11.42\% | 1.901.90 |

(a) PM 3




|  | Return | Volatility | Sharpe |
| --- | --- | --- | --- |
| independent | 15.42%15.42\% | 13.09%13.09\% | 1.181.18 |
| full\_cooperative | 17.10%17.10\% | 12.28%12.28\% | 1.391.39 |
| admm\_2\_iter | 18.60%18.60\% | 12.28%12.28\% | 1.511.51 |
| admm\_5\_iter | 17.06%17.06\% | 12.31%12.31\% | 1.391.39 |

(a) PM 4



Table 7: Performance statistics by backtest scenario for each PM.

BETA