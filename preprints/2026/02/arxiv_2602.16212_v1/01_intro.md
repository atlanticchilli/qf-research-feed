---
authors:
- German Nova Orozco
- Duy-Minh Dang
- Peter A. Forsyth
doc_id: arxiv:2602.16212v1
family_id: arxiv:2602.16212
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization
  under Systematic Longevity Risk'
url_abs: http://arxiv.org/abs/2602.16212v1
url_html: https://arxiv.org/html/2602.16212v1
venue: arXiv q-fin
version: 1
year: 2026
---


German Nova Orozco
School of Mathematics and Physics, The University of Queensland, St Lucia, Brisbane 4072, Australia,
email: g.novaorozco@student.uq.edu.au
  
Duy-Minh Dang
School of Mathematics and Physics, The University of Queensland, St Lucia, Brisbane 4072, Australia,
email: duyminh.dang@uq.edu.au
  
Peter A. Forsyth
David R. Cheriton School of Computer Science, University of Waterloo, Waterloo ON, N2L 3G1, Canada,
email: paforsyt@uwaterloo.ca

###### Abstract

Money-back guarantees (MBGs) are features of pooled retirement income products that address bequest concerns by ensuring the initial premium is returned through lifetime payments or, upon early death, as a death benefit to the estate.
This paper studies optimal retirement decumulation in an individual tontine account with an MBG overlay under international diversification and systematic longevity risk. The retiree chooses withdrawals and asset allocation dynamically to trade off expected total withdrawals (EW) against the Conditional Value-at-Risk (CVaR) of terminal wealth, subject to realistic investment constraints.
The optimization is solved under a plan-to-live convention, while stochastic mortality affects outcomes through its impact on mortality credits at the pool level.
We develop a neural-network based computational approach for the resulting high-dimensional, constrained control problem. The MBG is priced ex post under
the induced EW–CVaR optimal policy via a simulation-based actuarial rule that combines expected guarantee costs with a prudential tail buffer.
Using long-horizon historical return data expressed in real domestic-currency terms, we find that international diversification and longevity pooling jointly deliver the largest improvements in the EW–CVaR trade-off, while stochastic mortality shifts the frontier modestly in the expected direction. The optimal controls use foreign equity primarily as a state-dependent catch-up instrument, and implied MBG loads are driven mainly by tail outcomes (and the chosen prudential buffer) rather than by mean payouts.

Keywords: defined contribution, tontine, money-back guarantee, stochastic mortality, portfolio optimization, Conditional Value-at-Risk, neural network

AMS Subject Classification: 93E20, 91G10, 91B30, 62P05, 68T07

## 1 Introduction

The worldwide shift from Defined Benefit (DB) pensions to Defined Contribution (DC)
arrangements is well documented [[40](https://arxiv.org/html/2602.16212v1#bib.bib40), [58](https://arxiv.org/html/2602.16212v1#bib.bib58)].
While DC plans offer flexibility and portability, they also transfer much of the responsibility for managing key retirement risks to individuals.
In particular, upon retirement, a DC member faces the *decumulation problem*:
how to invest and draw down accumulated savings to
support sustainable real (inflation-adjusted) spending under longevity risk (the possibility of outliving savings) and uncertain market returns [[33](https://arxiv.org/html/2602.16212v1#bib.bib33), [5](https://arxiv.org/html/2602.16212v1#bib.bib5), [3](https://arxiv.org/html/2602.16212v1#bib.bib3)]. Rapid
global population ageing further intensifies these challenges
[[60](https://arxiv.org/html/2602.16212v1#bib.bib60)].

To manage longevity risk in practice, many retirees rely on simple spending and asset allocation heuristics, most notably the “4% rule” [[4](https://arxiv.org/html/2602.16212v1#bib.bib4)]
(often paired with a fixed stock–bond mix) and performance-based adjustments
to withdrawals and/or portfolio weights (e.g. [[23](https://arxiv.org/html/2602.16212v1#bib.bib23)]).
These rules are transparent and easy to implement, and this reliance on rule-based decumulation is consistent with the evidence in [[1](https://arxiv.org/html/2602.16212v1#bib.bib1)],
which reports a revealed preference for spending rules among retirees and wealth advisors in DC drawdown settings.
However, because these rules are not derived from a risk–reward optimization, they can be far from efficient under realistic market and wealth conditions (see, e.g. [[17](https://arxiv.org/html/2602.16212v1#bib.bib17), [19](https://arxiv.org/html/2602.16212v1#bib.bib19)]).

As an alternative to rules-based drawdown strategies, retirees can transfer longevity risk to an insurer by purchasing a life annuity. In practice, voluntary annuitization remains limited (e.g. [[42](https://arxiv.org/html/2602.16212v1#bib.bib42)]),
and low demand for life annuities can be rational once bequest motives, illiquidity costs, and product design are taken into account [[33](https://arxiv.org/html/2602.16212v1#bib.bib33)].

In parallel, there has been renewed interest in *pooled* retirement income products that share longevity risk among members while offering greater transparency and flexibility than traditional annuities. Modern tontines and related survivor pools achieve longevity pooling by redistributing the accounts of deceased members to survivors, generating *mortality credits* that can support higher sustainable real (inflation-adjusted) withdrawals for members who remain alive [[16](https://arxiv.org/html/2602.16212v1#bib.bib16), [15](https://arxiv.org/html/2602.16212v1#bib.bib15), [37](https://arxiv.org/html/2602.16212v1#bib.bib37), [22](https://arxiv.org/html/2602.16212v1#bib.bib22)]. The appeal comes with a clear trade–off: mortality credits raise payouts conditional on survival, but wealth is typically forfeited upon death.

In [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], a stochastic optimal control framework is developed
for an individual tontine retirement account. It operationalizes the idea of
modern tontines in an individual setting by adding a tontine overlay that
redistributes the balances of deceased members to survivors. In this
framework, the retiree has full control over both the withdrawal amount
(subject to minimum and maximum constraints) and the asset allocation in the
account. The optimization objective is defined using a risk–reward criterion:
reward is measured by total expected accumulated
real (inflation-adjusted) withdrawals (EW) over a fixed retirement horizon (30 years), while risk is measured by Conditional Value-at-Risk (CVaR), also known as expected shortfall, of end-of-horizon real wealth (assuming the retiree survives to the horizon, i.e. “plan-to-live, not to die”; see, e.g. [[43](https://arxiv.org/html/2602.16212v1#bib.bib43)]).

In that setting, the results in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)] show that longevity pooling can materially improve the withdrawal–risk trade–off relative to non–pooled drawdown strategies and simple constant withdrawal/allocation benchmarks. In particular, for a reasonable level of tail-risk tolerance (CVaR), the tontine overlay delivers substantially higher expected cumulative real withdrawals, even
after allowing for “fees of the order of 50–100 basis points (bps) per year”[[21](https://arxiv.org/html/2602.16212v1#bib.bib21)][Section 1].

This efficiency gain, however, comes at the cost of forfeiting account wealth upon
death, which can limit the appeal of “pure” tontine overlays for retirees with
bequest or estate considerations [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)].
Reflecting this practical constraint, recent industry innovation—particularly in the
Australian superannuation market—has introduced *money-back guarantees* (MBGs),
sometimes described in product disclosures as “money-back protection”, for pooled
retirement income products (e.g. QSuper and MyNorth [[49](https://arxiv.org/html/2602.16212v1#bib.bib49), [38](https://arxiv.org/html/2602.16212v1#bib.bib38)]). An MBG overlay can be added to an otherwise pure tontine, as in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], and ensures that the member receives at least the initial purchase price (a nominal dollar amount fixed at inception) through lifetime withdrawals and/or a death benefit paid to the estate. Because the MBG is settled only upon death and is paid to the estate, it does not affect the account dynamics while the retiree is alive.
Importantly, in practice the funding mechanism for MBGs need not appear as a stand-alone member-level charge and can change over time (e.g. insured funding versus pool-funded self-insurance) [[49](https://arxiv.org/html/2602.16212v1#bib.bib49), [48](https://arxiv.org/html/2602.16212v1#bib.bib48)]. This practical reality motivates cost measures that are economically comparable across operational implementations, rather than tied to any particular fee design.

From the perspective of the entity that ultimately bears the guarantee, whether an insurer or the retirement-income pool, the MBG is a low–frequency, high–severity death–benefit liability: it is triggered only upon death, but conditional on occurrence the payout can be large. Accordingly, the economic cost of an MBG depends not only on expected payouts, but also on tail outcomes and on any prudential buffer/reserving rule used to fund adverse scenarios. Crucially, the distribution of guarantee payouts is endogenous to retiree behavior, since withdrawal and asset allocation choices determine the account balance at death.
Hence, MBG valuation cannot be carried out independently of the retiree’s decumulation
policy, even though the MBG itself does not feed back into the retiree’s optimal controls under the plan-to-live convention.

From a modelling perspective, two aspects are central in tontine decumulation: the specification of the asset market and the treatment of mortality risk.
While most individual account decumulation models assume a domestic stock–bond portfolio, in practice, for retirees, the investable universe is inherently richer and often includes international assets [[56](https://arxiv.org/html/2602.16212v1#bib.bib56), [11](https://arxiv.org/html/2602.16212v1#bib.bib11)]. International diversification is particularly important for investors in countries where the local equity market capitalization is small relative to the global market.
Extending the individual account decumulation setting to allow international diversification is economically important, since it can affect the risk–return trade-offs and, in turn, optimal withdrawal and asset allocation decisions.
Allowing multiple risky asset classes, however, makes the control
problem high-dimensional and renders grid-based dynamic programming
computationally prohibitive. Recent work in portfolio optimization and related control problems has shown that neural network (NN) parameterizations of policies can compute high-dimensional, state-dependent controls without suffering from the curse of dimensionality inherent in grid methods [[31](https://arxiv.org/html/2602.16212v1#bib.bib31), [39](https://arxiv.org/html/2602.16212v1#bib.bib39), [8](https://arxiv.org/html/2602.16212v1#bib.bib8)].

A second modelling aspect is mortality at the pool level: deaths determine the redistribution to surviving members and hence the mortality credits. Following the discussion in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], an important caveat is systematic mortality risk (e.g. unexpected improvements in life expectancy), which is typically ignored when mortality credits are computed from a fixed life table. To capture this source of uncertainty, stochastic mortality specifications such as Lee–Carter (LC) [[30](https://arxiv.org/html/2602.16212v1#bib.bib30)] and Cairns–Blake–Dowd (CBD) [[7](https://arxiv.org/html/2602.16212v1#bib.bib7)] can be used to generate time-varying one-year death probabilities and hence stochastic mortality credits. If mortality improves unexpectedly, realized mortality credits can be lower than anticipated because lighter realized mortality implies fewer deaths and hence less redistribution to survivors. This separates idiosyncratic longevity risk (diversifiable within the pool) from systematic longevity risk (non-diversifiable).

Motivated by the above observations, this paper sets out to achieve three primary objectives. First, we formulate a multi-period EW–CVaR optimal decumulation framework for an individual retirement account with a tontine overlay in an internationally diversified setting with realistic long-horizon DC constraints. The individual optimization problem is solved conditional on survival over a fixed retirement horizon, while stochastic mortality enters through pathwise mortality-credit inputs.
Conditioning on survival to the end of a 30-year horizon (e.g. from age 65 to 95) is a prudent stress test for sustaining real (inflation-adjusted) retirement spending and aligns with the common “plan-to-live, not to die” convention used in practice.111Survival to age 95 from age 65 is far from certain under standard life tables; under recent Australian population life tables, it is about 0.11 for a 65-year-old male.

Second, we develop a computational approach capable of solving the resulting high-dimensional, constrained control problem using NN parameterizations of state-dependent policies, and integrate this with a simulation-based MBG pricing framework under endogenous retiree behavior and alternative prudential-buffer (tail-risk) funding rules for MBGs.

Third, using nearly a century of realized market data, we quantify the impact of international diversification (at the individual account level) and stochastic mortality (at the pool level) on optimal tontine decumulation outcomes, EW–CVaR frontiers, and MBG loads, and assess the relative importance of these modelling dimensions.

Concretely, the numerical illustration is conducted from the perspective of a representative domestic retiree with access to domestic and foreign equity and government bond indices. Foreign returns are converted into domestic-currency real (inflation-adjusted) returns so that outcomes are measured in units of real (inflation-adjusted) retirement spending. The empirical implementation reported in Section [9](https://arxiv.org/html/2602.16212v1#S9 "9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") uses an Australian-investor calibration with long-horizon data, but the modelling and computational framework is not country-specific and can be applied elsewhere given the corresponding asset and mortality inputs.

Our main conclusion is that international diversification is economically material even before tontines. The gains are most pronounced when diversification is combined with a tontine overlay, which is the primary driver of improvements in the EW–CVaR withdrawal–risk trade–off. Allowing for stochastic mortality at the pool level shifts outcomes in the expected direction—longevity improvement reduces mortality credits—but does not alter the qualitative picture. Finally, when MBGs are summarized in equivalent-load terms, the expected-cost (actuarially fair) component is modest in our analysis, while larger implied loads are driven primarily by how strongly the funding rule places weight on tail outcomes (prudential buffers) rather than by mean payouts.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2602.16212v1#S2 "2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") introduces the tontine modelling framework and the mortality specifications (deterministic and stochastic). Section [3](https://arxiv.org/html/2602.16212v1#S3 "3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") describes the money-back guarantee (MBG) overlay mechanism. Section [4](https://arxiv.org/html/2602.16212v1#S4 "4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") presents the stochastic control framework for individual-account decumulation, and Section [5](https://arxiv.org/html/2602.16212v1#S5 "5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") formulates the associated EW–CVaR optimization problem. Section [6](https://arxiv.org/html/2602.16212v1#S6 "6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") develops the NN-based computational approach, and Section [7](https://arxiv.org/html/2602.16212v1#S7 "7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") integrates it with a Monte Carlo pricing method for the MBG. Validation results are reported in Section [8](https://arxiv.org/html/2602.16212v1#S8 "8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"). Section [9](https://arxiv.org/html/2602.16212v1#S9 "9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") presents data construction and preprocessing details,
the internationally diversified tontine results, MBG pricing implications, and sensitivity analyses. Section [10](https://arxiv.org/html/2602.16212v1#S10 "10 Conclusion and future work ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") concludes and outlines directions for future research.

## 2 Tontine modeling

We let 𝒯\mathcal{T} denote the set of pre-determined, equally spaced decision times in [0,T][0,T], at which mortality credit distributions, withdrawals, and portfolio rebalancing occur:222The assumption of equal spacing is made for simplicity. In practice, rebalancing schedules are typically fixed (e.g., semi-annually or annually), rather than irregular.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯={tm∣tm=m​Δ​t,m=0,…,M},Δ​t=T/M,\mathcal{T}=\{t\_{m}\mid t\_{m}=m\Delta t,\ m=0,\ldots,M\},\quad\Delta t=T/M, |  | (2.1) |

where t0=0t\_{0}=0 is the inception time and T>0T>0 is the finite investment horizon.
Throughout we take annual decision times, so Δ​t=1\Delta t=1 year and T=MT=M.

For later use, we define t−=t−εt^{-}=t-\varepsilon and t+=t+εt^{+}=t+\varepsilon to represent the instants just before and after any time t∈[0,T]t\in[0,T], with ε→0+\varepsilon\to 0^{+}. For a generic time-dependent function f​(t)f(t) and any tm∈𝒯t\_{m}\in\mathcal{T}, we write

|  |  |  |
| --- | --- | --- |
|  | fm−=limε→0+f​(tm−ε),fm+=limε→0+f​(tm+ε),f\_{m^{-}}=\lim\_{\varepsilon\to 0^{+}}f(t\_{m}-\varepsilon),\quad f\_{m^{+}}=\lim\_{\varepsilon\to 0^{+}}f(t\_{m}+\varepsilon), |  |

as shorthand for f​(tm−)f(t\_{m}^{-}) and f​(tm+)f(t\_{m}^{+}), respectively.

### 2.1 Modeling of individual tontine accounts

We follow the framework of [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)] for individual
tontine accounts. The tontine pool consists of JJ members, indexed by
j=1,…,Jj=1,\ldots,J. At each time point tm∈𝒯t\_{m}\in\mathcal{T}, we identify the actions that occur at the three successive instants: tm−⟶tm⟶tm+t\_{m}^{-}\;\longrightarrow\;t\_{m}\;\longrightarrow\;t\_{m}^{+}.
These actions apply only in the event of solvency, that is, when the investor’s wealth is strictly positive at time tm−t\_{m}^{-}.

* •

  tm−t\_{m}^{-} (for m=1,…,Mm=1,\ldots,M):
  end-of-period portfolio balances are observed. Accounts of members who died in [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}] are forfeited, and the corresponding mortality credits are immediately distributed to the surviving members, prior to any investor actions
  (i.e. withdrawals and rebalancing).
* •

  tmt\_{m} and tm+t\_{m}^{+} (for m=0,…,M−1m=0,\ldots,M-1): each surviving investor withdraws an amount qmq\_{m} at tmt\_{m}, and then rebalances their portfolio at tm+t\_{m}^{+}.

Between tm−1+t\_{m-1}^{+} and tm−t\_{m}^{-}, m=1,…,Mm=1,\ldots,M, the underlying asset processes and mortality evolve continuously under their respective (stochastic) dynamics.
At tM=Tt\_{M}=T, the portfolio is liquidated with no withdrawal or rebalancing.

To proceed with mortality credits, we introduce the notation for individual account balances and formalize the survival and forfeiture events over [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}]. A detailed discussion of withdrawals, rebalancing, and the incorporation of mortality credits is provided in Section [5](https://arxiv.org/html/2602.16212v1#S5 "5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

We denote by Wm−jW\_{m^{-}}^{j} the real (inflation-adjusted) portfolio balance (or wealth) of member jj at time tm−t\_{m}^{-}, m=0,…,Mm=0,\ldots,M. At the beginning of each period [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}], m=1,2​…​Mm=1,2\ldots M, all pool members are assumed to be alive and each holds an account balance of W(m−1)+j≥0W\_{(m-1)^{+}}^{j}\geq 0. If a member dies during the period, their entire account is forfeited and distributed to the surviving members of the pool as mortality credits. Mathematically, we define the survival indicator and its conditional expectation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏mj={1,member j survives to ​tm−,0,member j dies during ​[tm−1+,tm−],𝔼m−1​[𝟏mj]=1−δm−1j.\mathbf{1}\_{m}^{j}=\begin{cases}1,&\text{member $j$ survives to }t\_{m}^{-},\\[4.0pt] 0,&\text{member $j$ dies during }[t\_{m-1}^{+},t\_{m}^{-}],\end{cases}\qquad\mathbb{E}\_{m-1}\bigl[\mathbf{1}\_{m}^{j}\bigr]=1-\delta\_{m-1}^{j}. |  | (2.2) |

Here, δm−1j\delta\_{m-1}^{j} is the probability that member jj dies in [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}], namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | δm−1j=Prob​(member j dies during ​[tm−1+,tm−]|alive at ​tm−1+).\delta\_{m-1}^{j}\;=\;\mathrm{Prob}\bigl(\text{member $j$ dies during }[t\_{m-1}^{+},t\_{m}^{-}]\,\big|\,\text{alive at }t\_{m-1}^{+}\bigr). |  | (2.3) |

In addition, 𝔼m−1[⋅]=𝔼[⋅∣ℱm−1]\mathbb{E}\_{m-1}[\cdot]=\mathbb{E}[\cdot\mid\mathcal{F}\_{m-1}] denotes expectation conditional on the σ\sigma-algebra
ℱm−1\mathcal{F}\_{m-1}, which contains all information available at tm−1+t\_{m-1}^{+}
(the start of [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}]). If 𝟏mj=0\mathbf{1}\_{m}^{j}=0, the portfolio balance Wm−jW\_{m^{-}}^{j} is forfeited. If 𝟏mj=1\mathbf{1}\_{m}^{j}=1, member jj receives a mortality credit cmjc\_{m}^{j} at time tmt\_{m}.

We now describe how cmjc\_{m}^{j} is determined in two stages: (i) an individual-level fairness condition, and (ii) a pool-level budget constraint.

#### 2.1.1 Individual fairness condition

Assuming no fees—that is, we ignore administration, investment-management, and transaction costs for simplicity—the tontine is structured so that, in every period, participation yields zero expected net gain in advance. In other words, a member’s expected forfeited wealth in case of death during a period is exactly balanced by the expected mortality credit they receive at the end of that period if they survive. Specifically, conditioning on information available at time tm−1+t\_{m-1}^{+}, the fairness condition for the period [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}] is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wm−j​𝔼m−1​[1−𝟏mj]=(1−δm−1j)​𝔼m−1​[cmj|Ωmj],where ​Ωmj={𝟏mj=1,{Wm−k}k=1J}.W\_{m^{-}}^{j}\,\mathbb{E}\_{m-1}\bigl[1-\mathbf{1}\_{m}^{j}\bigr]=(1-\delta\_{m-1}^{j})\,\mathbb{E}\_{m-1}\left[c\_{m}^{j}|~\Omega\_{m}^{j}\right],\quad\text{where }\Omega\_{m}^{j}=\left\{\mathbf{1}\_{m}^{j}=1,\;\big\{W\_{m^{-}}^{k}\big\}\_{k=1}^{J}\right\}. |  | (2.4) |

That is, 𝔼m−1[⋅|Ωmj]\mathbb{E}\_{m-1}[~\cdot~|\Omega\_{m}^{j}] denotes the expectation conditional on all information available at tm−1+t\_{m-1}^{+}, together with
(i) the event that member jj survives the period (𝟏mj=1\mathbf{1}\_{m}^{j}=1), and
(ii) the realized end-of-period wealth balances of all members {Wm−k}k=1J\{W\_{m^{-}}^{k}\}\_{k=1}^{J}, before mortality credits are calculated and distributed.

Solving ([2.4](https://arxiv.org/html/2602.16212v1#S2.E4 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) yields the actuarially fair mortality credit distribution formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼m−1​[cmj|Ωmj]=δm−1j1−δm−1j​Wm−j.\mathbb{E}\_{m-1}\left[c\_{m}^{j}\big|~\Omega\_{m}^{j}\right]=\frac{\delta\_{m-1}^{j}}{1-\delta\_{m-1}^{j}}\,W\_{m^{-}}^{j}. |  | (2.5) |

According to this rule, each surviving member’s expected mortality credit is proportional to their own account balance, scaled by the ratio of their death probability to their survival probability. While the right-hand side of ([2.5](https://arxiv.org/html/2602.16212v1#S2.E5 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) depends only on (Wm−j,δm−1j)(W\_{m^{-}}^{j},\delta\_{m-1}^{j}), this independence is not exact for a finite and heterogeneous pool: it is possible to construct scenarios in which the available forfeitures are insufficient to support ([2.5](https://arxiv.org/html/2602.16212v1#S2.E5 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) simultaneously for all surviving members, leading to a bias that favours some members over others (see the discussion in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)]). Following [[54](https://arxiv.org/html/2602.16212v1#bib.bib54)], we therefore interpret ([2.5](https://arxiv.org/html/2602.16212v1#S2.E5 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) as a large-pool approximation whose accuracy hinges on a *small-bias condition*, stated explicitly in Subsection [2.1.3](https://arxiv.org/html/2602.16212v1#S2.SS1.SSS3 "2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

#### 2.1.2 Pool-level budget constraint

While equation ([2.5](https://arxiv.org/html/2602.16212v1#S2.E5 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) guarantees fairness for each member,
the tontine must also balance cash flows at the pool level: the total
mortality credits paid to surviving members at tmt\_{m} must equal the total wealth
forfeited by deceased ones during the period [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}]. This requirement gives the budget rule333More generally, the mortality credit can be written as
cmj=δm−1j1−δm−1j​Wm−j​Hmjc\_{m}^{j}=\tfrac{\delta\_{m-1}^{j}}{1-\delta\_{m-1}^{j}}\,W\_{m^{-}}^{j}\,H\_{m}^{j},
where Hmj≥0H\_{m}^{j}\geq 0 is a sharing factor. Fairness is preserved by imposing
𝔼m−1​[Hmj|Ωmj]=1\mathbb{E}\_{m-1}[H\_{m}^{j}|\Omega\_{m}^{j}]=1; see [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)] for details.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1J𝟏mj​cmj=∑j=1J(1−𝟏mj)​Wm−j,\sum\_{j=1}^{J}\mathbf{1}\_{m}^{j}\,c\_{m}^{j}\;=\;\sum\_{j=1}^{J}(1-\mathbf{1}\_{m}^{j})\,W\_{m^{-}}^{j}, |  | (2.6) |

which must hold ex post in every period. Because ([2.6](https://arxiv.org/html/2602.16212v1#S2.E6 "In 2.1.2 Pool-level budget constraint ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) must hold with the actual forfeitures and credits—determined by the random, realized number of deaths in the period, which could be different from the expected count—enforcing this budget rule exactly can be cumbersome in a finite pool.
We therefore introduce a practical adjustment in the next subsection.

#### 2.1.3 Large-pool approximation

To obtain a simple, tractable rule, [[54](https://arxiv.org/html/2602.16212v1#bib.bib54)] introduce a pool-wide adjustment factor referred to as the group gain Γm\Gamma\_{m} defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γm=∑k=1J(1−𝟏mk)​Wm−k∑k=1J𝟏mk​δm−1k1−δm−1k​Wm−k.\Gamma\_{m}=\frac{\sum\_{k=1}^{J}(1-\mathbf{1}\_{m}^{k})\,W\_{m^{-}}^{k}}{\sum\_{k=1}^{J}\mathbf{1}\_{m}^{k}\,\dfrac{\delta\_{m-1}^{k}}{1-\delta\_{m-1}^{k}}\,W\_{m^{-}}^{k}}. |  | (2.7) |

Here, the numerator is the realized forfeiture during
[tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}], while the denominator is the total expected
mortality credit for the members who actually survive that period, obtained by
summing the fair-credit expression ([2.5](https://arxiv.org/html/2602.16212v1#S2.E5 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))
δm−1k1−δm−1k​Wm−k\tfrac{\delta\_{m-1}^{k}}{1-\delta\_{m-1}^{k}}\,W\_{m^{-}}^{k} over all kk with
𝟏mk=1\mathbf{1}\_{m}^{k}=1.

Multiplying the fair-credit expectation ([2.5](https://arxiv.org/html/2602.16212v1#S2.E5 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))
by Γm\Gamma\_{m} gives the simplified mortality credit distribution formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | cmj=δm−1j1−δm−1j​Wm−j​Γm,j=1,…,J,c\_{m}^{j}=\frac{\delta\_{m-1}^{j}}{1-\delta\_{m-1}^{j}}\,W\_{m^{-}}^{j}\,\Gamma\_{m},\qquad j=1,\ldots,J, |  | (2.8) |

which satisfies the budget rule ([2.6](https://arxiv.org/html/2602.16212v1#S2.E6 "In 2.1.2 Pool-level budget constraint ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) exactly, even for
finite pools. However, for finite and heterogeneous pools, the sharing rule ([2.8](https://arxiv.org/html/2602.16212v1#S2.E8 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) need not satisfy the individual fairness condition ([2.5](https://arxiv.org/html/2602.16212v1#S2.E5 "In 2.1.1 Individual fairness condition ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) exactly; instead, it can introduce a (typically small) bias in expected gains across members. It is shown in [[54](https://arxiv.org/html/2602.16212v1#bib.bib54)] that this bias is negligible under the following *small-bias condition*: (a) the pool is sufficiently large, and (b) the expected aggregate forfeiture in the period is large compared to any member’s nominal gain, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | δm−1j1−δm−1j​Wm−j≪∑k=1Jδm−1k​Wm−k,j=1,…,J.\frac{\delta\_{m-1}^{j}}{1-\delta\_{m-1}^{j}}\,W\_{m^{-}}^{j}\ll\sum\_{k=1}^{J}\delta\_{m-1}^{k}\,W\_{m^{-}}^{k},\qquad j=1,\ldots,J. |  | (2.9) |

Condition ([2.9](https://arxiv.org/html/2602.16212v1#S2.E9 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is essentially a diversification requirement: no member has an abnormally large share of the pool capital. When ([2.9](https://arxiv.org/html/2602.16212v1#S2.E9 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) holds (and the pool is large enough that realized deaths are close to their expectation), the random group-gain factor satisfies 𝔼​[Γm]≃1\mathbb{E}\!\left[\Gamma\_{m}\right]\simeq 1 with small variance [[54](https://arxiv.org/html/2602.16212v1#bib.bib54)]. Accordingly, we adopt the approximation Γm≡1\Gamma\_{m}\equiv 1 for the remainder of the paper.

With the large-pool approximation Γm≡1\Gamma\_{m}\equiv 1, the member–level mortality
credit distribution rule ([2.8](https://arxiv.org/html/2602.16212v1#S2.E8 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | cmj=δm−1j1−δm−1j​Wm−j,j=1,…,J.c\_{m}^{j}=\frac{\delta\_{m-1}^{j}}{1-\delta\_{m-1}^{j}}\,W\_{m^{-}}^{j},\qquad j=1,\ldots,J. |  | (2.10) |

The rule ([2.10](https://arxiv.org/html/2602.16212v1#S2.E10 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) continues to satisfy, with high accuracy under the large-pool/small-bias assumptions (Condition ([2.9](https://arxiv.org/html/2602.16212v1#S2.E9 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))): (i) Fairness: 𝔼m−1​[cmj|Ωmj]=δm−1j1−δm−1j​Wm−j\mathbb{E}\_{m-1}[c\_{m}^{j}|\Omega\_{m}^{j}]=\dfrac{\delta\_{m-1}^{j}}{1-\delta\_{m-1}^{j}}\,W\_{m^{-}}^{j}, (ii) Budget constraint: Equation ([2.6](https://arxiv.org/html/2602.16212v1#S2.E6 "In 2.1.2 Pool-level budget constraint ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) (exactly when Γm\Gamma\_{m} is retained as in ([2.8](https://arxiv.org/html/2602.16212v1#S2.E8 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), and approximately under the large-pool approximation Γm≡1\Gamma\_{m}\equiv 1), and (iii) Non-negativity: cmj≥0c\_{m}^{j}\geq 0 for all jj.

In our optimal control formulation, we suppress the superscript jj and consider a representative surviving member. The mortality credit distribution rule ([2.10](https://arxiv.org/html/2602.16212v1#S2.E10 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) then reduces to a per-member expression that depends only on the member’s own total wealth at time tm−t\_{m}^{-} and their mortality rate. Based on this, we define the mortality credit cmc\_{m} in terms of the tontine gain rate, denoted by gmg\_{m}, as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | cm=gm​Wm−, wheregm=δm−11−δm−1.c\_{m}=g\_{m}\,W\_{m^{-}},\quad\text{ where}\quad g\_{m}=\frac{\delta\_{m-1}}{1-\delta\_{m-1}}. |  | (2.11) |

The tontine gain rate can be interpreted as
gm=fraction of the cohort expected to diefraction expected to surviveg\_{m}=\tfrac{\text{fraction of the cohort expected to die}}{\text{fraction expected to survive}},
so it represents the proportional uplift each surviving member receives from mortality pooling during [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}]. Equation ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is the key mechanism used to compute mortality credits in the optimal control formulation developed subsequently in the paper.

### 2.2 Mortality models

Recall from ([2.2](https://arxiv.org/html/2602.16212v1#S2.E2 "In 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([2.3](https://arxiv.org/html/2602.16212v1#S2.E3 "In 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) that longevity risk enters the tontine
through the one–year conditional death probabilities
δm−1j\delta\_{m-1}^{j} for each member jj over the interval
[tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}]. In a homogeneous pool, we write
δm−1j≡δm−1\delta\_{m-1}^{j}\equiv\delta\_{m-1}, so that the tontine gain rate gmg\_{m} in
([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is fully determined by the annual sequence
{δm−1}m=1M\{\delta\_{m-1}\}\_{m=1}^{M}. We now describe how this sequence is obtained under
deterministic and stochastic mortality.

#### 2.2.1 Deterministic mortality

In the deterministic case, we work with a standard period life table, such as the
Canadian Pensioner Mortality Tables or Australian mortality from the Human
Mortality Database (HMD) [[25](https://arxiv.org/html/2602.16212v1#bib.bib25)], which provide one–year death
probabilities qx,yq\_{x,y} for an individual aged xx in calendar year yy.
Let the retiree be aged x0x\_{0} at retirement, which occurs in calendar year
y0y\_{0}. In our tontine framework the decision times are measured in years
since retirement, so tm=mt\_{m}=m for m=0,…,Mm=0,\ldots,M with t0=0t\_{0}=0.
At decision time tmt\_{m}, the retiree is age x0+mx\_{0}+m in calendar year
y0+my\_{0}+m.

We extract from the life table the corresponding one–year conditional death
probabilities

|  |  |  |  |
| --- | --- | --- | --- |
|  | δm−1:=qx0+(m−1),y0+(m−1),m=1,…,M.\delta\_{m-1}\;:=\;q\_{x\_{0}+(m-1),\,y\_{0}+(m-1)},\qquad m=1,\ldots,M. |  | (2.12) |

In a homogeneous pool, these probabilities are common to all members, so that
δm−1j=δm−1\delta\_{m-1}^{j}=\delta\_{m-1} for every jj, and both {δm−1}\{\delta\_{m-1}\} and the
corresponding tontine gain rates {gm}={δm−1/(1−δm−1)}\{g\_{m}\}=\{\delta\_{m-1}/(1-\delta\_{m-1})\} are deterministic.

#### 2.2.2 Stochastic mortality

To incorporate systematic longevity risk, we allow the mortality surface to be
generated by a stochastic model in the generalized age–period–cohort (GAPC)
family; see [[62](https://arxiv.org/html/2602.16212v1#bib.bib62)]. Let Dx,yD\_{x,y} denote the number of
deaths at age xx in calendar year yy and Ex,yE\_{x,y} the corresponding central
exposure. We assume

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dx,y∼Poisson​(mx,y​Ex,y),D\_{x,y}\sim\mathrm{Poisson}\bigl(m\_{x,y}\,E\_{x,y}\bigr), |  | (2.13) |

with central death rate mx,ym\_{x,y}. Its systematic component is captured by a
linear predictor

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηx,y=αx+∑i=1Nβx(i)​κy(i)+βx(0)​γy−x,\eta\_{x,y}=\alpha\_{x}+\sum\_{i=1}^{N}\beta\_{x}^{(i)}\,\kappa\_{y}^{(i)}+\beta\_{x}^{(0)}\,\gamma\_{y-x}, |  | (2.14) |

where αx\alpha\_{x} describes the age profile, κy(i)\kappa\_{y}^{(i)} are period factors
and γy−x\gamma\_{y-x} is a cohort effect. A link function gg relates ηx,y\eta\_{x,y}
to the mortality quantity of interest, e.g.

|  |  |  |
| --- | --- | --- |
|  | log⁡mx,y=ηx,yorlogit​qx,y=ηx,y,\log m\_{x,y}=\eta\_{x,y}\quad\text{or}\quad\mathrm{logit}\,q\_{x,y}=\eta\_{x,y}, |  |

with logit​(u)=log⁡(u/(1−u))\mathrm{logit}(u)=\log\bigl(u/(1-u)\bigr) for u∈(0,1)u\in(0,1).
In this general GAPC formulation the cohort term is optional; the specific
Lee–Carter [[30](https://arxiv.org/html/2602.16212v1#bib.bib30)] and Cairns–Blake–Dowd [[7](https://arxiv.org/html/2602.16212v1#bib.bib7)] models used below are special cases that omit the cohort component.

#### Lee–Carter (LC) model

In the Lee–Carter specification, the predictor has a
single age–period term,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηx,y=αx+βx​κy,\eta\_{x,y}=\alpha\_{x}+\beta\_{x}\,\kappa\_{y}, |  | (2.15) |

and we typically set log⁡mx,y=ηx,y\log m\_{x,y}=\eta\_{x,y}. The period index κy\kappa\_{y}
captures the overall mortality level and is commonly modelled as a random walk
with drift,

|  |  |  |  |
| --- | --- | --- | --- |
|  | κy=δ+κy−1+ξy,ξy∼N​(0,σκ2)​i.i.d.\kappa\_{y}=\delta+\kappa\_{y-1}+\xi\_{y},\qquad\xi\_{y}\sim N(0,\sigma\_{\kappa}^{2})\ \text{i.i.d.} |  | (2.16) |

together with the usual identifiability constraints on
(αx,βx,κy)(\alpha\_{x},\beta\_{x},\kappa\_{y}) as implemented in StMoMo
[[62](https://arxiv.org/html/2602.16212v1#bib.bib62)].

#### Cairns–Blake–Dowd (CBD) model

The Cairns–Blake–Dowd model [[7](https://arxiv.org/html/2602.16212v1#bib.bib7)] describes mortality as
approximately linear in age around a reference age x¯\bar{x}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηx,y=κy(1)+(x−x¯)​κy(2).\eta\_{x,y}=\kappa\_{y}^{(1)}+(x-\bar{x})\,\kappa\_{y}^{(2)}. |  | (2.17) |

Here it is natural to work directly with one–year death probabilities and set

|  |  |  |
| --- | --- | --- |
|  | logit​qx,y=ηx,y.\mathrm{logit}\,q\_{x,y}=\eta\_{x,y}. |  |

The bivariate period factor
𝜿y=(κy(1),κy(2))⊤\boldsymbol{\kappa}\_{y}=(\kappa\_{y}^{(1)},\kappa\_{y}^{(2)})^{\top}
is usually specified as a random walk with drift,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜿y=𝜹+𝜿y−1+𝝃y,𝝃y∼N​(𝟎,Σκ)​i.i.d.,\boldsymbol{\kappa}\_{y}=\boldsymbol{\delta}+\boldsymbol{\kappa}\_{y-1}+\boldsymbol{\xi}\_{y},\qquad\boldsymbol{\xi}\_{y}\sim N(\mathbf{0},\Sigma\_{\kappa})\ \text{i.i.d.}, |  | (2.18) |

In contrast to the LC model, no additional identifiability constraints are
required for this basic two–factor CBD specification [[62](https://arxiv.org/html/2602.16212v1#bib.bib62)].

##### From stochastic mortality models to tontine gain rate.

Once an LC or CBD model has been calibrated to historical deaths and exposures,
its fitted and projected period factors determine a surface of
one–year death probabilities {qx,y}\{q\_{x,y}\}. For a representative retiree aged
x0x\_{0} in calendar year y0y\_{0}, with annual decision times tm=mt\_{m}=m and
corresponding calendar years ym=y0+my\_{m}=y\_{0}+m, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | δm−1:=qx0+(m−1),y0+(m−1),m=1,…,M,\delta\_{m-1}\;:=\;q\_{x\_{0}+(m-1),\,y\_{0}+(m-1)},\qquad m=1,\ldots,M, |  | (2.19) |

and in a homogeneous pool we set δm−1j≡δm−1\delta\_{m-1}^{j}\equiv\delta\_{m-1} for all
members jj, exactly as in the deterministic life–table case.
These probabilities feed directly into the tontine gain rate
gm=δm−1/(1−δm−1)g\_{m}=\delta\_{m-1}/(1-\delta\_{m-1}) in ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). Thus the
tontine mechanics developed above apply unchanged; only the sequence
{δm−1}\{\delta\_{m-1}\} differs between deterministic life–table mortality and
stochastic GAPC-based mortality.

###### Remark 2.1 (Mortality inputs in simulation).

The same one–year conditional death probabilities also underpin our simulation
framework. In the deterministic case, the sequence
{δm−1}m=1M\{\delta\_{m-1}\}\_{m=1}^{M} is obtained from a period life table as in
Subsection [2.2.1](https://arxiv.org/html/2602.16212v1#S2.SS2.SSS1 "2.2.1 Deterministic mortality ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), and we take
δm−1(k)≡δm−1\delta\_{m-1}^{(k)}\equiv\delta\_{m-1} on every simulation path, indexed by kk.
Under stochastic LC or CBD mortality, each simulated mortality surface
{qx,y(k)}\{q\_{x,y}^{(k)}\} yields a pathwise sequence
{δm−1(k)}m=1M\{\delta\_{m-1}^{(k)}\}\_{m=1}^{M} via

|  |  |  |  |
| --- | --- | --- | --- |
|  | δm−1(k):=qx0+(m−1),y0+(m−1)(k),m=1,…,M.\delta\_{m-1}^{(k)}\;:=\;q^{(k)}\_{x\_{0}+(m-1),\,y\_{0}+(m-1)},\qquad m=1,\ldots,M. |  | (2.20) |

On path kk, these probabilities are used to construct tontine gain rates
gm(k)=δm−1(k)/(1−δm−1(k))g\_{m}^{(k)}=\delta\_{m-1}^{(k)}/(1-\delta\_{m-1}^{(k)}), m=1,…,Mm=1,\ldots,M,
which enter the wealth recursion in the NN training (Section [6](https://arxiv.org/html/2602.16212v1#S6 "6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))
and are also used to generate death times and payouts in the money-back
guarantee valuation (Section [7](https://arxiv.org/html/2602.16212v1#S7 "7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

## 3 Money-back guarantee overlay

“*Your purchase price is always paid back as either income to you or a death benefit paid to your beneficiaries. If you die, the death benefit is equal to the amount you paid for your Lifetime Pension, less the payments that have gone to you…*”

QSuper’s Lifetime Pension Product Disclosure Statement [[49](https://arxiv.org/html/2602.16212v1#bib.bib49)]

This promise reflects the essence of the MBG, a recent industry innovation introduced by leading Australian superannuation providers, including QSuper and MyNorth [[49](https://arxiv.org/html/2602.16212v1#bib.bib49), [38](https://arxiv.org/html/2602.16212v1#bib.bib38)]. The MBG can be added to an otherwise “pure” tontine and ensures that every dollar a member invests at inception (i.e. their initial contribution or purchase price) is returned—either through lifetime withdrawals or, if the member dies early, as a death benefit paid to their estate.

### 3.1 Description

Specifically, at inception, suppose a member invests an amount L0L\_{0} (ie. the purchase price) to the retirement product with MBG. At each decision time tm∈𝒯t\_{m}\in\mathcal{T}, as in the regular tontine described in Section [2](https://arxiv.org/html/2602.16212v1#S2 "2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), if the member survives to tm−t\_{m}^{-}, they first receive the mortality credit cmc\_{m} defined in ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), then withdraw an amount qmq\_{m}, and rebalance their portfolio. Once cumulative withdrawals reach or exceed the purchase price L0L\_{0}, the MBG becomes inactive.

If the member dies at time τ∈(tm−1+,tm−]\tau\in(t\_{m-1}^{+},t\_{m}^{-}], no further withdrawal occurs,
including the scheduled withdrawal at tmt\_{m}. If their cumulative withdrawals up to
tm−1t\_{m-1} fall short of the purchase price L0L\_{0} (a nominal dollar amount fixed at inception),
the MBG activates. The member’s estate receives the shortfall:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MBG-payout=max⁡(L0−∑ℓ=0mτ−1qℓ​CPIℓCPI0, 0),\text{MBG-payout}=\max\bigg(L\_{0}-\sum\_{\ell=0}^{m\_{\tau}-1}q\_{\ell}\,\frac{\mathrm{CPI}\_{\ell}}{\mathrm{CPI}\_{0}},\,0\bigg), |  | (3.1) |

where mτm\_{\tau} is the time index such that death occurs in the interval
[tmτ−1+,tmτ−][t\_{m\_{\tau}-1}^{+},\,t\_{m\_{\tau}}^{-}], and the right-hand side is expressed in
nominal dollars (unadjusted for inflation).
Here, CPIℓ\mathrm{CPI}\_{\ell} is the consumer-price index at decision time tℓt\_{\ell} (and
CPI0\mathrm{CPI}\_{0} is the index level at inception). Because the guarantee compares nominal cash flows, each real dollar withdrawal qℓq\_{\ell} is first expressed in nominal terms by
multiplying by CPIℓ/CPI0\mathrm{CPI}\_{\ell}/\mathrm{CPI}\_{0} before being summed in ([3.1](https://arxiv.org/html/2602.16212v1#S3.E1 "In 3.1 Description ‣ 3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
For valuation and reporting, this nominal shortfall is converted to a real (inflation-adjusted) amount at inception by multiplying by CPI0/CPImτ\mathrm{CPI}\_{0}/\mathrm{CPI}\_{m\_{\tau}}; see Section [7](https://arxiv.org/html/2602.16212v1#S7 "7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (Eqn. ([7.1](https://arxiv.org/html/2602.16212v1#S7.E1 "In 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))).

While it is straightforward to incorporate time-value discounting, we follow
[[19](https://arxiv.org/html/2602.16212v1#bib.bib19)] in setting the real discount rate to zero.
This conservative assumption, common in retirement-income studies, typically implies a constant discount factor of 1 throughout.

For instance, suppose a retiree makes an initial contribution of $200,000 at t0t\_{0}, and withdrawals are scheduled annually (Δ​t=1\Delta t=1 year). By the end of year 4 (t4t\_{4}), the member has withdrawn a total of $65,000 in nominal terms. If the member then dies during the subsequent interval [t4+,t5−][t\_{4}^{+},t\_{5}^{-}]—that is, sometime between the end of year 4 and the scheduled decision time at year 5—no withdrawal is executed at t5t\_{5}. The MBG is triggered and the member’s estate receives: MBG-payout=max⁡(200,000−65,000, 0)=$​135,000\text{MBG-payout}=\max\bigl(200{,}000-65{,}000,\;0\bigr)=\mathdollar 135{,}000.

###### Remark 3.1 (Timing convention).

In our discrete-time model, we follow the convention that the estate of a member who dies during the interval [tm−1+,tm−][t\_{m-1}^{+},t\_{m}^{-}] receives the MBG payout at the end of that interval. As described in Section [2](https://arxiv.org/html/2602.16212v1#S2 "2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), the member’s account balance at tm−t\_{m}^{-} contributes to the mortality credits distributed to members surviving the period. However, the account is then removed prior to the distribution, and no further withdrawals are made, including the scheduled withdrawal at tmt\_{m}. In the above example,
the MBG amount of $135,000 will be paid at year 5.

This end-of-interval convention is widely adopted in actuarial asset–liability models (see, for example, [[14](https://arxiv.org/html/2602.16212v1#bib.bib14), Section 4] and [[36](https://arxiv.org/html/2602.16212v1#bib.bib36), Section 2]), as it simplifies implementation and introduces only a first-order bias 𝒪​(Δ​t)\mathcal{O}(\Delta t) arising solely from using the end-of-year CPI level when converting between real and nominal amounts. With Δ​t=1\Delta t=1 year, this bias is negligible compared with market and longevity risk.

Importantly, the MBG operates as an overlay implemented at the product/pool level, for example, through pool-funded self-insurance or an external insurance arrangement. Therefore, it does not alter the tontine’s internal mechanics: the pooling of longevity risk, mortality credit distributions, withdrawals, and rebalancing all remain as specified in Section [2](https://arxiv.org/html/2602.16212v1#S2 "2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

In practice, the MBG may be subject to regulatory constraints, such as Australia’s Capital Access Schedule (CAS), which limits the refundable portion of a pension’s purchase price.
While it is straightforward to incorporate the CAS into the model, we do not do so here in order to maintain focus on the core mechanics of the tontine and the MBG overlay pricing. As a result, the recoverable amount under the MBG may be overstated relative to a regulated product.

### 3.2 MBG pricing load

Product disclosures for pooled retirement income products typically emphasize the
presence of MBGs (sometimes described as money-back protection), but the
mechanisms used to fund these guarantees need not appear as stand-alone
member-level charges and can evolve over time.

For QSuper’s Lifetime Pension, used as our industry example, the Product
Disclosure Statement (PDS) introduces “money-back protection” and does not
present it as a stand-alone recurring member-level insurance fee
[[49](https://arxiv.org/html/2602.16212v1#bib.bib49)]. A recent product update further notes that money-back
protection was previously offered through an external insurance policy (ART Life
Insurance Limited), and that from 1 July 2025 the Trustee ceased this insurance
arrangement; instead, “the money-back protection benefit can be funded from the
Lifetime Pension pool directly” [[48](https://arxiv.org/html/2602.16212v1#bib.bib48)][p. 2].

Consistent with this pool-level funding approach, the current PDS explains that
“The Lifetime Pension pool’s annual financial results will affect the annual income
adjustment in the following year. The results include: …\ldots the mortality
experience of the pool …\ldots all fees and costs,” and that “The money-back
protection benefit (if applicable) is paid from the pool”
[[49](https://arxiv.org/html/2602.16212v1#bib.bib49), p. 34, p. 113].

Accordingly, in this paper we treat the MBG funding mechanism as a modelling
choice and summarize its economic cost using an equivalent up-front load
factor fg∈(0,1)f\_{g}\in(0,1). The quantity fg​L0f\_{g}L\_{0} can be interpreted as a transparent
one-time cost measure—equivalently, a proportional reduction in a notional
starting income rate or benefit base—that would finance the MBG under the
pricing rule adopted in this paper. This translation device allows the MBG cost to be
reported in a comparable way across alternative practical implementations
(e.g. pool-funded self-insurance versus insured funding versus implicit benefit
adjustments). Full details of the pricing methodology and its numerical
implementation are provided in Section [7](https://arxiv.org/html/2602.16212v1#S7 "7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

## 4 Stochastic control framework

We now turn to the stochastic control framework, where we model the evolution of an individual member’s portfolio and formulate the associated dynamic optimization problem.
We consider a portfolio held by a domestic investor with access to four real (inflation-adjusted) asset classes:
(i) a domestic stock index fund,
(ii) a domestic bond index fund,
(iii) a foreign stock index fund (converted to domestic currency), and
(iv) a foreign bond index fund (converted to domestic currency).
This setup allows us to examine both an internationally diversified portfolio, which includes all four asset classes, and a non-diversified alternative that is restricted to domestic assets only.
The construction of these indices, the inflation adjustment, and the data sources used for calibration are detailed in Sections [8](https://arxiv.org/html/2602.16212v1#S8 "8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") and [9](https://arxiv.org/html/2602.16212v1#S9 "9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

### 4.1 Index dynamics

For simplicity and clarity, we establish the following notational conventions. A subscript ι∈{d,f}\iota\in\{d,f\} is used to distinguish quantities related to the domestic stock or bond (ι=d\iota=d) from those corresponding to the foreign counterparts (ι=f\iota=f). Additionally, a superscript “ss” denotes quantities associated with stock indices, while a superscript “bb” identifies those related to their bond index counterparts.

Let Sd​(t)S^{{\scalebox{0.7}{$d$}}}(t), Bd​(t)B^{{\scalebox{0.7}{$d$}}}(t), Sf​(t)S^{{\scalebox{0.7}{$f$}}}(t), and Bf​(t)B^{{\scalebox{0.7}{$f$}}}(t) denote the real (inflation-adjusted) *amounts* invested in the stock and bond indices of the domestic and foreign markets, respectively, at time t∈[0,T]t\in[0,T].
To avoid notational clutter, we occasionally use the shorthand notation:
Std≡Sd​(t)S\_{t}^{{\scalebox{0.7}{$d$}}}\equiv S^{{\scalebox{0.7}{$d$}}}(t),
Btd≡Bd​(t)B\_{t}^{{\scalebox{0.7}{$d$}}}\equiv B^{{\scalebox{0.7}{$d$}}}(t),
Stf≡Sf​(t)S\_{t}^{{\scalebox{0.7}{$f$}}}\equiv S^{{\scalebox{0.7}{$f$}}}(t), and
Btf≡Bf​(t)B\_{t}^{{\scalebox{0.7}{$f$}}}\equiv B^{{\scalebox{0.7}{$f$}}}(t).
We denote by {Xt}0≤t≤T\{X\_{t}\}\_{0\leq t\leq T} (resp. by xx) the controlled underlying index process (resp. a generic state of the system), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt(resp. ​x)={(Std,Btd)(resp. ​(sd,bd)),domestic-only,(Std,Btd,Stf,Btf)(resp. ​(sd,bd,sf,bf)),internationally diversified.X\_{t}\quad\left(\text{resp.\ }x\right)=\begin{cases}\bigl(S\_{t}^{{\scalebox{0.7}{$d$}}},\,B\_{t}^{{\scalebox{0.7}{$d$}}}\bigr)\quad\left(\text{resp.\ }(s^{{\scalebox{0.7}{$d$}}},\,b^{{\scalebox{0.7}{$d$}}})\right),&\text{domestic-only},\\[4.0pt] \bigl(S\_{t}^{{\scalebox{0.7}{$d$}}},\,B\_{t}^{{\scalebox{0.7}{$d$}}},\,S\_{t}^{{\scalebox{0.7}{$f$}}},\,B\_{t}^{{\scalebox{0.7}{$f$}}}\bigr)\quad\left(\text{resp.\ }(s^{{\scalebox{0.7}{$d$}}},\,b^{{\scalebox{0.7}{$d$}}},\,s^{{\scalebox{0.7}{$f$}}},\,b^{{\scalebox{0.7}{$f$}}})\right),&\text{internationally diversified}.\end{cases} |  | (4.1) |

Between decision times tm∈𝒯t\_{m}\in\mathcal{T}, the process evolves passively, driven solely by index-return dynamics.
For any t∈[tm+,tm+1−]t\in[t\_{m}^{+},\,t\_{m+1}^{-}], we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=ℳtm,t​(Xtm+,εm+1),t∈[tm+,tm+1−],X\_{t}\;=\;\mathcal{M}\_{t\_{m},t}\bigl(X\_{t\_{m}^{+}},\,\varepsilon\_{m+1}\bigr),\qquad t\in[t\_{m}^{+},\,t\_{m+1}^{-}], |  | (4.2) |

where ℳtm,t\mathcal{M}\_{t\_{m},t} is a transition operator and
εm+1\varepsilon\_{m+1} collects all exogenous drivers acting over the interval [tm+,tm+1−][t\_{m}^{+},\,t\_{m+1}^{-}]. These drivers may include Brownian or jump shocks (in parametric models) or resampled blocks of historical returns (in bootstrapped settings).
The operator ℳtm,t\mathcal{M}\_{t\_{m},t} maps the post-decision state Xtm+X\_{t\_{m}^{+}} and the
exogenous drivers on [tm+,t][t\_{m}^{+},t] to the state XtX\_{t}.

In this paper, we consider two specifications for the driver set εm+1\varepsilon\_{m+1} as follows.

* •

  Parametric (jump–diffusion) model:
  For benchmarking against PDE-based methods, we implement a two-asset domestic-only case
  in which the domestic stock and bond indices {Std}\{S\_{t}^{d}\} and {Btd}\{B\_{t}^{d}\} follow Kou‐type jump–diffusion dynamics with asymmetric double-exponential jumps, capturing empirically observed heavy tails [[28](https://arxiv.org/html/2602.16212v1#bib.bib28)]. The full SDE specification appears in Subsection [8.1](https://arxiv.org/html/2602.16212v1#S8.SS1 "8.1 Asset dynamics ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")
* •

  Historical block bootstrap:
  In our main experiments, both domestic-only and internationally diversified, we simulate asset paths nonparametrically via the stationary block bootstrap [[45](https://arxiv.org/html/2602.16212v1#bib.bib45), [41](https://arxiv.org/html/2602.16212v1#bib.bib41), [46](https://arxiv.org/html/2602.16212v1#bib.bib46), [13](https://arxiv.org/html/2602.16212v1#bib.bib13)].
  Implementation details of the bootstrapping techniques are provided in Subsection [9.1](https://arxiv.org/html/2602.16212v1#S9.SS1 "9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

In both cases, mortality-credit realizations (when applicable) are simulated independently and applied only at tm−t\_{m}^{-}. The resulting dynamics {Xt}0≤t≤T\{X\_{t}\}\_{0\leq t\leq T} from ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) capture the passive evolution of the index values between decision times. Active decisions—mortality updates, withdrawals, and rebalancing—are applied only at {tm}m=0M−1\{t\_{m}\}\_{m=0}^{M-1}, as detailed in the next subsection.

### 4.2 Mortality updates and control framework

We define the investor’s total portfolio wealth, hereafter referred to as “total wealth,” at time tt as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt={Std+Btd,domestic-only,Std+Btd+Stf+Btf,internationally diversified.W\_{t}=\begin{cases}S\_{t}^{{\scalebox{0.7}{$d$}}}+B\_{t}^{{\scalebox{0.7}{$d$}}},&\text{domestic-only},\\[4.0pt] S\_{t}^{{\scalebox{0.7}{$d$}}}+B\_{t}^{{\scalebox{0.7}{$d$}}}+S\_{t}^{{\scalebox{0.7}{$f$}}}+B\_{t}^{{\scalebox{0.7}{$f$}}},&\text{internationally diversified}.\end{cases} |  | (4.3) |

The term “total wealth” refers to the sum of the values of the investor’s (tontine)
account plus any accumulated debt arising from insolvency due to the minimum required
withdrawals. In the event of solvency, we impose the investment constraints that (i)
shorting stock and (ii) using leverage (i.e. borrowing) are not permitted. In case of insolvency, the portfolio is liquidated and trading stops. Debt accumulates at the borrowing rate, and no further mortality credits are applied. Importantly, minimum withdrawals continue in the event of insolvency, so once the account is exhausted, they are funded by borrowing and contribute to the accumulated debt.

Recall the set of decision times 𝒯\mathcal{T} defined in ([2.1](https://arxiv.org/html/2602.16212v1#S2.E1 "In 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). At each tm∈𝒯t\_{m}\in\mathcal{T}, the sequence of actions at tm−→tm→tm+t\_{m}^{-}\!\rightarrow t\_{m}\!\rightarrow t\_{m}^{+} described in Subsection [2.1](https://arxiv.org/html/2602.16212v1#S2.SS1 "2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") applies.
To simplify bookkeeping, we adopt a uniform event structure across all tm∈𝒯t\_{m}\in\mathcal{T}, including time t0t\_{0} for mortality credit and tMt\_{M} for withdrawal as follows:
in the event of solvency at tm−t\_{m^{-}}, namely the total wealth Wm−>0W\_{m^{-}}>0
as defined in ([4.3](https://arxiv.org/html/2602.16212v1#S4.E3 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) the following actions occur:

* •

  At each time tm−t\_{m}^{-}, m=0,1,…,Mm=0,1,\ldots,M, the mortality credit cmc\_{m} defined in ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is applied, with the convention that c0=0c\_{0}=0, since
  no forfeitures have occurred at t0t\_{0}.
* •

  At each time tmt\_{m} (for m=0,…,M−1m=0,\ldots,M-1), the investor withdraws an amount qmq\_{m}, followed by portfolio rebalancing at tm+t\_{m}^{+}. At tMt\_{M}, the portfolio is liquidated (i.e. no rebalancing or withdrawal occurs), and terminal wealth WTW\_{T} is realized. For notational completeness, this is enforced by setting qM=0q\_{M}=0.

To enforce no mortality credit at t=0t=0 and for the case of insolvency, we modify the definition of tontine gain rate gmg\_{m} in ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | gm={(δm−11−δm−1)m=1,…,M,0m=0​ or ​Wm−≤0.g\_{m}=\begin{cases}\left(\frac{\delta\_{m-1}}{1-\delta\_{m-1}}\right)&m=1,\ldots,M,\\ 0&m=0\text{ or }W\_{m^{-}}\leq 0.\end{cases} |  | (4.4) |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | W~m−={(1+gm)​(Sm−d+Bm−d),domestic only,(1+gm)​(Sm−d+Bm−d+Sm−f+Bm−f),internationally diversified.\widetilde{W}\_{m^{-}}\;=\;\begin{cases}(1+g\_{m})\,\left(S\_{m^{-}}^{{\scalebox{0.7}{$d$}}}+B\_{m^{-}}^{{\scalebox{0.7}{$d$}}}\right),&\text{domestic only},\\[6.0pt] (1+g\_{m})\,\left(S\_{m^{-}}^{{\scalebox{0.7}{$d$}}}+B\_{m^{-}}^{{\scalebox{0.7}{$d$}}}+S\_{m^{-}}^{{\scalebox{0.7}{$f$}}}+B\_{m^{-}}^{{\scalebox{0.7}{$f$}}}\right),&\text{internationally diversified}.\end{cases} |  | (4.5) |

That is, W~m−\tilde{W}\_{m^{-}} is the value of the portfolio immediately
after the mortality credit distribution at tm−t\_{m}^{-} but before any
fee, withdrawal, or rebalancing.

Next, we introduce a baseline tontine (management) fee that is deducted once per year, at each decision time tmt\_{m}, m=1,…,Mm=1,\ldots,M. In line with Australian superannuation practice, and in particular the administration fee structure in QSuper’s Lifetime Pension PDS [[49](https://arxiv.org/html/2602.16212v1#bib.bib49)], we model this as a proportional charge on the account balance. Let ϱ∈(0,1)\varrho\in(0,1) denote the yearly fee rate (e.g. ϱ=0.11%\varrho=0.11\% for an 11 bp charge).

To ensure the tontine fee is applied only when the investor is solvent and is omitted at t0t\_{0}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϱm=ϱ​ 1{m≥1,W~m−>0},m=0,…,M,W~m− given by ([4.5](https://arxiv.org/html/2602.16212v1#S4.E5 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).\varrho\_{m}=\varrho\,\mathbf{1}\_{\{\,m\geq 1,\;\widetilde{W}\_{m^{-}}>0\,\}},\qquad m=0,\dots,M,\qquad\text{$\widetilde{W}\_{m^{-}}$ given by \eqref{eq:Wtilde\_def}}. |  | (4.6) |

With the conventions established in ([4.4](https://arxiv.org/html/2602.16212v1#S4.E4 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([4.6](https://arxiv.org/html/2602.16212v1#S4.E6 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),
the total wealth at tm−∈𝒯t\_{m}^{-}\in\mathcal{T} after applying the mortality credit and deducting the tontine fee, and before any investor actions, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wm−=(1−ϱm)​W~m−,W~m− given by ([4.5](https://arxiv.org/html/2602.16212v1#S4.E5 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))W\_{m^{-}}=\bigl(1-\varrho\_{m}\bigr)\widetilde{W}\_{m^{-}},\qquad\text{$\widetilde{W}\_{m^{-}}$ given by \eqref{eq:Wtilde\_def}} |  | (4.7) |

Unless otherwise stated, we use Wm−W\_{m^{-}} to denote the investor’s wealth immediately before withdrawal (and rebalancing), but after mortality credits have been distributed and tontine fees deducted, as defined in ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

Following this, the total wealth after processing the withdrawal amount qmq\_{m} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wm+=Wm−−qm,tm∈𝒯, Wm− given by ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).W\_{m^{+}}=W\_{m^{-}}-q\_{m},\quad t\_{m}\in\mathcal{T},\quad\text{ $W\_{m^{-}}$ given by \eqref{eq:Wm\_post\_tontine}}. |  | (4.8) |

We model the withdrawal amount qmq\_{m} as a withdrawal control, for m=0,…,Mm=0,\ldots,M,
representing a strategy that depends on the total wealth Wm−W\_{m^{-}} and time tmt\_{m}.
Recalling the convention that qM=0q\_{M}=0, we define the withdrawal control function as
qm​(⋅):(Wm−,tm)↦qm=q​(Wm−,tm)q\_{m}(\cdot):(W\_{m^{-}},t\_{m})\mapsto q\_{m}=q(W\_{m^{-}},t\_{m}), where Wm−W\_{m^{-}} is given by ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

At each rebalancing time tmt\_{m}, for m=0,…,M−1m=0,\ldots,M{-}1, we denote the rebalancing control by 𝒑m​(⋅)\boldsymbol{p}\_{m}(\cdot), the vector of proportions of total wealth allocated to the asset indices.
This control depends on the current time tmt\_{m} and on the total wealth Wm+W\_{m^{+}} after the cash withdrawal qmq\_{m} in ([4.8](https://arxiv.org/html/2602.16212v1#S4.E8 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
Formally, 𝒑m​(⋅):(Wm+,tm)↦𝒑m=𝒑​(Wm+,tm)\boldsymbol{p}\_{m}(\cdot):(W\_{m^{+}},t\_{m})\mapsto\boldsymbol{p}\_{m}\;=\;\boldsymbol{p}(W\_{m^{+}},t\_{m}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒑m={(ps,md),domestic‐only case,(ps,md,pb,md,ps,mf),internationally diversified case.\boldsymbol{p}\_{m}=\begin{cases}\bigl(p^{{\scalebox{0.7}{$d$}}}\_{s,m}\bigr),&\text{domestic‐only case},\\[4.0pt] \bigl(p^{{\scalebox{0.7}{$d$}}}\_{s,m},\,p^{{\scalebox{0.7}{$d$}}}\_{b,m},\,p^{{\scalebox{0.7}{$f$}}}\_{s,m}\bigr),&\text{internationally diversified case}.\end{cases} |  | (4.9) |

We denote by Xm+X\_{m^{+}} the state of the system immediately after applying the rebalancing control 𝒑m\boldsymbol{p}\_{m}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xm+={(Sm+d,Bm+d),domestic-only,where ​Sm+d=ps,md​Wm+,Bm+d=pb,md​Wm+,(Sm+d,Bm+d,Sm+f,Bm+f),internationally diversified.where ​{Sm+d=ps,md​Wm+,Bm+d=pb,md​Wm+Sm+f=ps,mf​Wm+,Bm+f=pb,mf​Wm+,X\_{m^{+}}=\begin{cases}\bigl(S\_{m^{+}}^{{\scalebox{0.7}{$d$}}},\,B\_{m^{+}}^{{\scalebox{0.7}{$d$}}}\bigr),&\text{domestic-only},\\[4.0pt] \quad\text{where }S\_{m^{+}}^{{\scalebox{0.7}{$d$}}}=p\_{s,m}^{{\scalebox{0.7}{$d$}}}\,W\_{m^{+}},\quad B\_{m^{+}}^{{\scalebox{0.7}{$d$}}}=p\_{b,m}^{{\scalebox{0.7}{$d$}}}\,W\_{m^{+}},\\[4.0pt] \bigl(S\_{m^{+}}^{{\scalebox{0.7}{$d$}}},\,B\_{m^{+}}^{{\scalebox{0.7}{$d$}}},\,S\_{m^{+}}^{{\scalebox{0.7}{$f$}}},\,B\_{m^{+}}^{{\scalebox{0.7}{$f$}}}\bigr),&\text{internationally diversified}.\\[4.0pt] \quad\text{where }\begin{cases}S\_{m^{+}}^{{\scalebox{0.7}{$d$}}}=p\_{s,m}^{{\scalebox{0.7}{$d$}}}\,W\_{m^{+}},\quad B\_{m^{+}}^{{\scalebox{0.7}{$d$}}}=p\_{b,m}^{{\scalebox{0.7}{$d$}}}\,W\_{m^{+}}\\[4.0pt] S\_{m^{+}}^{{\scalebox{0.7}{$f$}}}=p\_{s,m}^{{\scalebox{0.7}{$f$}}}\,W\_{m^{+}},\quad B\_{m^{+}}^{{\scalebox{0.7}{$f$}}}=p\_{b,m}^{{\scalebox{0.7}{$f$}}}\,W\_{m^{+}},\end{cases}\end{cases} |  | (4.10) |

Here, in the domestic-only case, we define pb,md=1−ps,mdp\_{b,m}^{{\scalebox{0.7}{$d$}}}=1-p\_{s,m}^{{\scalebox{0.7}{$d$}}}, while in the internationally diversified case, pb,mf:=1−ps,md−pb,md−ps,mfp\_{b,m}^{{\scalebox{0.7}{$f$}}}:=1-p\_{s,m}^{{\scalebox{0.7}{$d$}}}-p\_{b,m}^{{\scalebox{0.7}{$d$}}}-p\_{s,m}^{{\scalebox{0.7}{$f$}}}.

We denote by 𝒵q\mathcal{Z}\_{q} and 𝒵p\mathcal{Z}\_{p} the sets of all admissible
withdrawal controls and rebalancing controls, respectively.
For every tm∈𝒯t\_{m}\in\mathcal{T} we require qm∈𝒵qq\_{m}\in\mathcal{Z}\_{q} and
𝒑m∈𝒵p\boldsymbol{p}\_{m}\in\mathcal{Z}\_{p}.
A control at time tmt\_{m} is therefore the pair
(qm​(⋅),𝒑m​(⋅))\bigl(q\_{m}(\cdot),\,\boldsymbol{p}\_{m}(\cdot)\bigr), and we write
𝒵\mathcal{Z} for the set of all such admissible pairs.
The sets are determined by withdrawal constraints (for 𝒵q\mathcal{Z}\_{q})
and investment constraints (for 𝒵p\mathcal{Z}\_{p}).

Contrary to the common perception that retiree spending is largely inflexible from year to year,
survey evidence suggests that retirees adjust their lifestyle in response to cash-flow changes, including
in categories often perceived as “fixed” expenses [[2](https://arxiv.org/html/2602.16212v1#bib.bib2)]. This supports modelling
withdrawals as a flexible control within bounds, rather than as a rigid rule.

To reflect this evidence, and consistent with industry practice, we impose lower and upper bounds,
qminq\_{\min} and qmaxq\_{\max}, on withdrawals. Formally, for tm∈𝒯t\_{m}\in\mathcal{T}, with Wm−W\_{m^{-}} given by
([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), we define the admissible withdrawal control set as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒵q​(Wm−,tm)={[qmin,qmax],tm≠tM,Wm−≥qmax,[qmin,max⁡{qmin,Wm−}],tm≠tM,Wm−<qmax,{0},tm=tM.\mathcal{Z}\_{q}\bigl(W\_{m^{-}},t\_{m}\bigr)=\begin{cases}\bigl[q\_{\min},\,q\_{\max}\bigr],&t\_{m}\neq t\_{M},\;W\_{m^{-}}\geq q\_{\max},\\[4.0pt] \bigl[q\_{\min},\,\max\{q\_{\min},\,W\_{m^{-}}\}\bigr],&t\_{m}\neq t\_{M},\;W\_{m^{-}}<q\_{\max},\\[4.0pt] \{0\},&t\_{m}=t\_{M}.\end{cases} |  | (4.11) |

While somewhat complicated, the piecewise structure in ([4.11](https://arxiv.org/html/2602.16212v1#S4.E11 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) captures the intuition that
the retiree aims to avoid insolvency as much as possible by tightening the upper withdrawal limit
when wealth declines. If wealth falls below qminq\_{\min}, the retiree can still withdraw the minimum
amount, accepting that this may lead to insolvency (i.e. Wm+<0W\_{m^{+}}<0). At the terminal time tMt\_{M},
no withdrawal occurs, as the portfolio is liquidated.

This constraint also admits a natural economic interpretation: qmaxq\_{\max} represents the retiree’s desired annual level of real (inflation-adjusted) spending, while qminq\_{\min} is a contingency floor the retiree is willing to adopt, potentially temporarily, to reduce the risk of depletion. The optimal control, therefore,
uses the flexibility in ([4.11](https://arxiv.org/html/2602.16212v1#S4.E11 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) to preserve higher withdrawals when the account is well funded, but cuts withdrawals toward qminq\_{\min} in adverse market/wealth states to mitigate the long-run consequences of drawing at the maximum rate during a downturn.

This state-contingent spending cut mechanism is closely related to practitioner rules such as the
*Canasta* strategy, which advocates reducing withdrawals following poor market performance.444<https://www.theglobeandmail.com/report-on-business/math-prof-tests-investing-formulas-strategies/article22397218/>;
<https://cs.uwaterloo.ca/~paforsyt/Canasta.html>.
Time-varying bounds (e.g. imposing qmin=qmaxq\_{\min}=q\_{\max} over an initial period to force high early spending)
can also be accommodated, but would mechanically increase the likelihood of early depletion when adverse returns
occur early.

###### Remark 4.1 (Minimum withdrawals under insolvency).

At first sight it might seem natural to cease withdrawals once the account is depleted. However, the lower bound qminq\_{\min} is intended to represent a required minimum level of (real) spending.
Accordingly, when Wm−<qminW\_{m^{-}}<q\_{\min} we still enforce the minimum
withdrawal by allowing Wm+=Wm−−qm<0W\_{m^{+}}=W\_{m^{-}}-q\_{m}<0, which is equivalent to borrowing the
shortfall; the resulting debt then accrues at the borrowing rate. This convention ensures that tail-risk measures of terminal wealth penalize insolvency and, in particular, penalize early depletion more than late depletion (since debt has more time to accumulate).

This convention also admits a practical interpretation in which minimum spending can be
funded from assets outside the managed account (e.g. housing equity monetized via a
reverse mortgage) once financial wealth is exhausted [[44](https://arxiv.org/html/2602.16212v1#bib.bib44)]. This “hedge of last resort” interpretation is also consistent with mental accounting views in which housing wealth is treated as a separate bucket that is tapped only in extreme circumstances, and otherwise can form part of the retiree’s bequest
[[55](https://arxiv.org/html/2602.16212v1#bib.bib55)].

We enforce no leverage and no shortselling when the portfolio is solvent,
and once the account becomes insolvent, we halt trading entirely and direct all wealth to the domestic bond. To define the set of admissible rebalancing controls,
we first introduce

|  |  |  |
| --- | --- | --- |
|  | Δ(k):={(p1,…,pk)∈[0,1]k|∑i=1kpi≤1},𝟎(1):=(0),𝐛(3):=(0,1,0),\Delta^{(k)}:=\Bigl\{(p\_{1},\dots,p\_{k})\in[0,1]^{k}\,\Bigm|\,\sum\_{i=1}^{k}p\_{i}\leq 1\Bigr\},\qquad\mathbf{0}^{(1)}:=(0),\qquad\mathbf{b}^{(3)}:=(0,1,0), |  |

where Δ(k)\Delta^{(k)} denotes the kk-dimensional simplex of explicitly parameterized asset proportions. We set k=1k=1 for the domestic-only portfolio and k=3k=3 for the internationally diversified case.
Under these conventions, the admissible rebalancing control set at time
tm∈𝒯t\_{m}\in\mathcal{T} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒵p​(Wm+,tm)={Δ(k),tm≠tM,Wm+>0,{{𝟎(1)},tm≠tM,Wm+≤0,{𝟎(1)},tm=tM,}domestic-only,or{{𝐛(3)},tm≠tM,Wm+≤0,{𝐛(3)},tm=tM,}internationally diversified.\mathcal{Z}\_{p}\bigl(W\_{m^{+}},t\_{m}\bigr)=\begin{cases}\Delta^{(k)},\qquad~t\_{m}\neq t\_{M},\;W\_{m^{+}}>0,&\\[2.0pt] \left.\begin{cases}\{\mathbf{0}^{(1)}\},&t\_{m}\neq t\_{M},\;W\_{m^{+}}\leq 0,\\[4.0pt] \{\mathbf{0}^{(1)}\},&t\_{m}=t\_{M},\end{cases}\right\}&\qquad\text{domestic-only},\\[8.0pt] \qquad\qquad\qquad\text{or}\\[2.0pt] \left.\begin{cases}\{\mathbf{b}^{(3)}\},&t\_{m}\neq t\_{M},\;W\_{m^{+}}\leq 0,\\[4.0pt] \{\mathbf{b}^{(3)}\},&t\_{m}=t\_{M},\end{cases}\right\}&\qquad\text{internationally diversified}.\end{cases} |  | (4.12) |

Here, Wm+W\_{m^{+}} is the post-withdrawal wealth defined in ([4.8](https://arxiv.org/html/2602.16212v1#S4.E8 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
In the domestic-only case, 𝟎(1)\mathbf{0}^{(1)} corresponds to zero allocation to the explicitly parameterized (domestic stock) asset, implying full allocation to the domestic bond. In the internationally diversified case, 𝐛(3)=(0,1,0)\mathbf{b}^{(3)}=(0,1,0) sets the explicitly parameterized proportions on domestic stock (0), domestic bond (11), and foreign stock (0), thereby assigning zero allocation to the foreign bond.
If withdrawals render the account insolvent (Wm+≤0W\_{m^{+}}\leq 0), trading stops and the negative balance accrues at the borrowing rate (a spread above the bond rate). The portfolio is liquidated at the terminal time tMt\_{M}.

The admissible control set for the pair (qm​(⋅),𝒑m​(⋅))\bigl(q\_{m}(\cdot),\,\boldsymbol{p}\_{m}(\cdot)\bigr),
tm∈𝒯t\_{m}\in\mathcal{T}, can then be written as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qm,𝒑m)∈𝒵​(Wm−,Wm+,tm)=𝒵q​(Wm−,tm)×𝒵p​(Wm+,tm),(\;q\_{m},\boldsymbol{p}\_{m}\;)\in\mathcal{Z}\bigl(W\_{m^{-}},W\_{m^{+}},t\_{m}\bigr)=\mathcal{Z}\_{q}\bigl(W\_{m^{-}},t\_{m}\bigr)\times\mathcal{Z}\_{p}\bigl(W\_{m^{+}},t\_{m}\bigr), |  | (4.13) |

where 𝒵q​(Wm−,tm)\mathcal{Z}\_{q}\bigl(W\_{m^{-}},t\_{m}\bigr) and 𝒵p​(Wm+,tm)\mathcal{Z}\_{p}\bigl(W\_{m^{+}},t\_{m}\bigr)
are defined in ([4.11](https://arxiv.org/html/2602.16212v1#S4.E11 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) and ([4.12](https://arxiv.org/html/2602.16212v1#S4.E12 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), respectively.
Let 𝒜\mathcal{A} be the set of admissible controls, defined as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜={𝒰=(qm,𝒑m)0≤m≤M|(qm,𝒑m)∈𝒵​(Wm−,Wm+,tm)}\mathcal{A}=\left\{\mathcal{U}=\left(q\_{m},\boldsymbol{p}\_{m}\right)\_{0\leq m\leq M}\big|\left(q\_{m},\boldsymbol{p}\_{m}\right)\in\mathcal{Z}\left(W\_{m^{-}},W\_{m^{+}},t\_{m}\right)\right\} |  | (4.14) |

For any tmt\_{m}, we define the subset of controls applicable from tmt\_{m} onwards as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒰m={(qℓ,𝒑ℓ)m≤ℓ≤M|(qℓ,𝒑ℓ)∈𝒵​(Wℓ−,Wℓ+,tℓ)}.\mathcal{U}\_{m}=\left\{\left(q\_{\ell},\boldsymbol{p}\_{\ell}\right)\_{m\leq\ell\leq M}\big|\left(q\_{\ell},\boldsymbol{p}\_{\ell}\right)\in\mathcal{Z}\left(W\_{\ell^{-}},W\_{\ell^{+}},t\_{\ell}\right)\right\}. |  | (4.15) |

## 5 EW–CVaR portfolio formulation

We use CVaR to quantify downside risk in terminal wealth.
Let ψ​(w)\psi(w) denote the probability density function of terminal wealth WTW\_{T}. For a given confidence level α∈(0,1)\alpha\in(0,1) (typically 0.01 or 0.05), the CVaR of WTW\_{T} at level α\alpha is defined by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | CVaRα​(WT)\displaystyle\text{CVaR}\_{\alpha}\left(W\_{T}\right) | =\displaystyle= | 1α​∫−∞VaRα​(WT)w​ψ​(w)​𝑑w.\displaystyle\tfrac{1}{\alpha}\int\_{-\infty}^{\text{VaR}\_{\alpha}\left(W\_{T}\right)}w\ \psi(w)\,dw. |  | (5.1) |

Here, VaRα​(WT)\text{VaR}\_{\alpha}(W\_{T}) is the Value-at-Risk (VaR) of WTW\_{T} at confidence level α\alpha, given by555That is, ∫−∞VaRα​(WT)ψ​(w)​𝑑w=α\int\_{-\infty}^{\text{VaR}\_{\alpha}\left(W\_{T}\right)}\psi(w)\,dw=\alpha.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | VaRα​(WT)\displaystyle\text{VaR}\_{\alpha}\left(W\_{T}\right) | =\displaystyle= | {w|ℙ​[WT≤w]=α}.\displaystyle\left\{\left.w\ \right|\ \mathbb{P}\left[\ W\_{T}\leq w\ \right]=\alpha\right\}. |  | (5.2) |

Intuitively, VaRα​(WT)\text{VaR}\_{\alpha}(W\_{T}) is the wealth threshold that is not exceeded with probability α\alpha, while CVaRα​(WT)\text{CVaR}\_{\alpha}(W\_{T}) represents the expected value of wealth in the worst α\alpha-quantile of the distribution [[52](https://arxiv.org/html/2602.16212v1#bib.bib52)].

For subsequent use, we denote by 𝔼𝒰0X0+,t0+​[WT]\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\left[W\_{T}\right] the expectation of terminal wealth WTW\_{T} under the real-world measure, conditional on the system being in state X0+X\_{0^{+}} at time t0+t\_{0}^{+}, and using the control 𝒰0\mathcal{U}\_{0} over [t0,T][t\_{0},T].
Let x0=X0−x\_{0}=X\_{0^{-}} be the initial state.

Following [[53](https://arxiv.org/html/2602.16212v1#bib.bib53)], the CVaR expression in ([5.1](https://arxiv.org/html/2602.16212v1#S5.E1 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) can be reformulated as a more computationally tractable optimization problem involving a candidate threshold WW that partitions the distribution of WTW\_{T} into its lower tail and the remainder. This leads to

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | CVaRα,𝒰0x0,t0\displaystyle\text{CVaR}\_{\alpha,\,\mathcal{U}\_{0}}^{x\_{0},t\_{0}} | =supW𝔼𝒰0X0+,t0+​[W+1α​min⁡(WT−W, 0)|X0−=x0].\displaystyle=\sup\_{W}\,\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\!\Bigl[W~+~\tfrac{1}{\alpha}\,\min\!\bigl(W\_{T}-W,\,0\bigr)~\big|\,X\_{0^{-}}=x\_{0}\Bigr]. |  |  | (5.3) |

The feasible range of WW in ([5.3](https://arxiv.org/html/2602.16212v1#S5.E3 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) coincides with the set of all possible values for WTW\_{T}.

As a measure of reward, we consider the expected total withdrawals.
For any admissible control 𝒰0∈𝒜\mathcal{U}\_{0}\in\mathcal{A}, we define expected withdrawals (EW)

|  |  |  |  |
| --- | --- | --- | --- |
|  | EW𝒰0x0,t0=𝔼𝒰0X0+,t0+​[∑m=0Mqm]\operatorname{EW}\_{\mathcal{U}\_{0}}^{x\_{0},t\_{0}}=\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\left[\sum\_{m=0}^{M}q\_{m}\right] |  | (5.4) |

where qm=q​(Wm−,tm)q\_{m}=q(W\_{m^{-}},t\_{m}) and Wm−W\_{m^{-}} is defined in ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) (i.e. after mortality credit distribution). Here, we assume the investor survives the full decumulation period, consistent with [[4](https://arxiv.org/html/2602.16212v1#bib.bib4)].

###### Remark 5.1 (Discounting and mortality weighting).

We remark that ([5.4](https://arxiv.org/html/2602.16212v1#S5.E4 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) applies no time discounting.
With all quantities expressed in real (inflation-adjusted) dollars, this is
equivalent to assuming a zero real discount rate.
Over long horizons, short-term real rates have often been modest on average in advanced economies, so adopting a zero real discount rate provides a reasonable and conservative baseline. Although it is straightforward to introduce discounting, we adopt this assumption; see [[19](https://arxiv.org/html/2602.16212v1#bib.bib19)] for further discussion.

In addition, we do not mortality-weight withdrawals by survival probabilities.
Such weighting is natural when valuing cash flows averaged across a population
(e.g. in annuity pricing), but our objective represents the strategy of an
individual retiree: conditional on being alive, the retiree requires the full
spending amount, not its survival-probability-weighted value. For example, if the
probability of surviving to a later age were 50%, mortality-weighting would
mechanically halve the corresponding cash flows (ignoring discounting), even
though the retiree would still require the full amount if alive. Hence, a
conservative approach is to condition on survival to a fixed horizon (age 95 in
our numerical illustration), which is consistent with the Bengen spending-rule
scenario that has proved popular with retirees [[4](https://arxiv.org/html/2602.16212v1#bib.bib4)]. Accordingly, we
condition on survival to the horizon, consistent with the practitioner
“plan-to-live, not to die” convention; see [[43](https://arxiv.org/html/2602.16212v1#bib.bib43)].

The goal is to simultaneously maximize expected withdrawals (EW) and the CVaR of terminal wealth—two objectives that are inherently in conflict. Solving this trade-off requires solving a bi-objective optimization problem. To obtain Pareto-optimal solutions,
we apply a scalarization approach, which converts the bi-objective problem into a single-objective one by combining CVaR and EW using a scalarization parameter γ>0\gamma>0.
Formally, for a given γ>0\gamma>0, we seek a control 𝒰0\mathcal{U}\_{0} that solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝒰0∈𝒜{EW𝒰0x0,t0+γ​CVaRα,𝒰0x0,t0}.\sup\_{\mathcal{U}\_{0}\in\mathcal{A}}\left\{\operatorname{EW}\_{\mathcal{U}\_{0}}^{x\_{0},t\_{0}}+\gamma\,\text{CVaR}\_{\alpha,\,\mathcal{U}\_{0}}^{x\_{0},t\_{0}}\right\}. |  | (5.5) |

###### Remark 5.2 (Pre-commitment and induced time-consistent interpretation).

The scalarized objective in ([5.5](https://arxiv.org/html/2602.16212v1#S5.E5 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is evaluated at t0t\_{0} and thus
defines a *pre-commitment* control: the retiree selects the policy at inception
and then follows it over the horizon. Because CVaRα\mathrm{CVaR}\_{\alpha} is generally not
time-consistent in multi-period settings, the EW–CVaR optimization is formally
time-inconsistent and is often viewed as non-implementable, since at time t>0t>0 the
retiree would typically have an incentive to deviate from the t0t\_{0} pre-commitment
strategy. Nonetheless, we use the pre-commitment formulation to determine the joint optimizer W∗W^{\ast} in ([5.3](https://arxiv.org/html/2602.16212v1#S5.E3 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). Fixing W∗W^{\ast} thereafter yields the equivalent expected-value control problem

|  |  |  |
| --- | --- | --- |
|  | sup𝒰0∈𝒜𝔼𝒰0X0+,t0+​[∑m=0Mqm+γ1−α​min⁡(WT−W∗,0)],\sup\_{\mathcal{U}\_{0}\in\mathcal{A}}\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\!\bigg[\sum\_{m=0}^{M}q\_{m}+\frac{\gamma}{1-\alpha}\min(W\_{T}-W^{\ast},0)\bigg], |  |

which satisfies the Bellman principle and is therefore time-consistent.
Accordingly, we interpret the computed control 𝒰0∗​(γ)\mathcal{U}\_{0}^{\ast}(\gamma) as the
associated *induced time-consistent* strategy determined by (α,γ,W∗)(\alpha,\gamma,W^{\ast})
(see, e.g. [[18](https://arxiv.org/html/2602.16212v1#bib.bib18), [57](https://arxiv.org/html/2602.16212v1#bib.bib57), [10](https://arxiv.org/html/2602.16212v1#bib.bib10)]).

Using ([5.3](https://arxiv.org/html/2602.16212v1#S5.E3 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([5.4](https://arxiv.org/html/2602.16212v1#S5.E4 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), we recast ([5.5](https://arxiv.org/html/2602.16212v1#S5.E5 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) as a control problem involving both system dynamics, mortality credit distributions, withdrawals, and rebalancing actions. For a fixed scalarization parameter γ>0\gamma>0, the pre-commitment EW–CVaR problem, denoted P​C​E​Ct0​(α,γ)PCEC\_{t\_{0}}(\alpha,\gamma), is defined via the value function V​(x0,t0−)V(x\_{0},t\_{0}^{-}) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (PCECt0(α,γ)):V(x0,t0−)=sup𝒰0∈𝒜supW{𝔼𝒰0X0+,t0+[∑m=0Mqm\displaystyle\left(PCEC\_{t\_{0}}(\alpha,\gamma)\right):V\left(x\_{0},t\_{0}^{-}\right)=\sup\_{\mathcal{U}\_{0}\in\mathcal{A}}\,\sup\_{W}\bigg\{\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\bigg[\sum\_{m=0}^{M}q\_{m} | +γ​(W+1α​min⁡(WT−W,0))\displaystyle+\gamma\left(W+\frac{1}{\alpha}\min\left(W\_{T}-W,0\right)\right) |  | (5.6) |
|  |  | +ϵWT|X0−=x0]}\displaystyle\qquad\qquad+\epsilon\,W\_{T}\bigg|X\_{0^{-}}=x\_{0}\bigg]\bigg\} |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to:​{(dynamics){Xt}​ evolves via ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))t∉𝒯,(tontine)Wℓ−​ given by ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),(withdrawal)Wℓ+=Wℓ−−qℓ​ as in ([4.8](https://arxiv.org/html/2602.16212v1#S4.E8 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),(rebalancing)Xℓ+​ as defined in ([4.10](https://arxiv.org/html/2602.16212v1#S4.E10 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), using ​𝒑ℓ​(⋅),(qℓ​(⋅),𝒑ℓ​(⋅))∈𝒵​(Wℓ−,Wℓ+,tℓ),ℓ=0,…,M,}tm∈𝒯.\text{subject to:}\begin{cases}~~\text{(dynamics)}\quad~~\{X\_{t}\}\text{ evolves via }\eqref{eq:dynamics\_generic}&t\notin\mathcal{T},\\[4.0pt] \left.\begin{array}[]{ll}\text{(tontine)}&W\_{\ell^{-}}\text{ given by }\eqref{eq:Wm\_post\_tontine},\\ \text{(withdrawal)}&W\_{\ell^{+}}=W\_{\ell^{-}}-q\_{\ell}\text{ as in }\eqref{eq:Wm\_post\_withdrawal},\\ \text{(rebalancing)}&X\_{\ell^{+}}\text{ as defined in \eqref{eq:Xmplus}, using }\boldsymbol{p}\_{\ell}(\cdot),\\ &(q\_{\ell}(\cdot),\,\boldsymbol{p}\_{\ell}(\cdot))\in\mathcal{Z}(W\_{\ell^{-}},W\_{\ell^{+}},t\_{\ell}),\quad\ell=0,\dots,M,\end{array}\right\}&t\_{m}\in\mathcal{T}.\end{cases} |  | (5.7) |

We denote by 𝒰0∗=𝒰0∗​(γ)\mathcal{U}\_{0}^{\ast}=\mathcal{U}\_{0}^{\ast}(\gamma) the control that attains the supremum in ([5.6](https://arxiv.org/html/2602.16212v1#S5.E6 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))-([5.7](https://arxiv.org/html/2602.16212v1#S5.E7 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), i.e. the optimal policy for a given scalarization parameter γ\gamma.

Note that we have added the extra term 𝔼𝒰0X0+,t0+​[ϵ​WT]\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0^{+}}}\left[\epsilon\,W\_{T}\right] to ([5.6](https://arxiv.org/html/2602.16212v1#S5.E6 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). If we have a maximum withdrawal constraint, and if Wt≫WW\_{t}\gg W as t→Tt\rightarrow T, the controls become ill-posed. In this fortunate state for the investor, we can break investment policy ties either by setting ϵ<0\epsilon<0, which will force investments in bonds, or by setting ϵ>0\epsilon>0, which will force investments into stocks. Choosing |ϵ|≪1|\epsilon|\ll 1 ensures that this term only has an effect if Wt≫WW\_{t}\gg W and t→Tt\rightarrow T. See [[19](https://arxiv.org/html/2602.16212v1#bib.bib19)] for more discussion of this.

We interchange the supremum operators in ([5.6](https://arxiv.org/html/2602.16212v1#S5.E6 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) to express the value function in a more computationally tractable form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x0,t0−)=supWsup𝒰0∈𝒜{𝔼𝒰0X0+,t0+​[∑m=0Mqm+γ​(W+1α​min⁡(WT−W,0))+ϵ​WT|X0−=x0]}.V(x\_{0},t\_{0}^{-})=\sup\_{W}\,\sup\_{\mathcal{U}\_{0}\in\mathcal{A}}\bigg\{\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\bigg[\sum\_{m=0}^{M}q\_{m}+\gamma\big(W+\frac{1}{\alpha}\min\left(W\_{T}-W,0\right)\big)+\epsilon\,W\_{T}\bigg|X\_{0^{-}}=x\_{0}\bigg]\bigg\}. |  | (5.8) |

The inner optimization yields a continuous function of WW, and the optimal threshold W∗​(x0)W^{\*}(x\_{0}) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | W∗​(x0)=arg⁡max𝑊​sup𝒰0∈𝒜{𝔼𝒰0X0+,t0+​[∑m=0Mqm+γ​(W+1α​min⁡(WT−W,0))+ϵ​WT|X0−=x0]}.W^{\*}(x\_{0})=\underset{W}{\arg\max}\,\sup\_{\mathcal{U}\_{0}\in\mathcal{A}}\bigg\{\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\bigg[\sum\_{m=0}^{M}q\_{m}+\gamma\big(W+\frac{1}{\alpha}\min\left(W\_{T}-W,0\right)\big)+\epsilon\,W\_{T}\bigg|X\_{0^{-}}=x\_{0}\bigg]\bigg\}. |  | (5.9) |

Finally, the scalarization parameter γ\gamma reflects the investor’s level of risk aversion. For a given α∈[0,1]\alpha\in[0,1], the EW–CVaR efficient frontier is defined as the following set of points in ℝ2\mathbb{R}^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮(α):{(CVaRα,𝒰0∗x0,t0[WT],EW𝒰0∗x0,t0):γ>0},\displaystyle\mathcal{S}(\alpha):\quad\left\{\left(\text{CVaR}\_{\alpha,\,\mathcal{U}\_{0}^{\ast}}^{x\_{0},t\_{0}}\left[W\_{T}\right],\ \text{EW}\_{\mathcal{U}\_{0}^{\ast}}^{x\_{0},t\_{0}}\right):\gamma>0\right\}, |  | (5.10) |

traced out by solving ([5.6](https://arxiv.org/html/2602.16212v1#S5.E6 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) for each γ>0\gamma>0. In other words, for any fixed level of risk aversion γ\gamma, the corresponding point in ([5.10](https://arxiv.org/html/2602.16212v1#S5.E10 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) cannot be improved in the EW–CVaR sense by any other admissible strategy in 𝒜\mathcal{A}.

## 6 Neural network formulation

Our numerical approach to solving the EW-CVaR stochastic control problem builds on the growing literature that uses NNs to approximate the optimal control directly, avoiding dynamic programming methods [[6](https://arxiv.org/html/2602.16212v1#bib.bib6), [31](https://arxiv.org/html/2602.16212v1#bib.bib31), [50](https://arxiv.org/html/2602.16212v1#bib.bib50), [51](https://arxiv.org/html/2602.16212v1#bib.bib51), [61](https://arxiv.org/html/2602.16212v1#bib.bib61)].
These methods have been termed “global-in-time” machine-learning approaches to stochastic control [[26](https://arxiv.org/html/2602.16212v1#bib.bib26)]. This contrasts with the stacked NN approach, in which a separate NN is used to approximate the control at each rebalancing step [[59](https://arxiv.org/html/2602.16212v1#bib.bib59), [24](https://arxiv.org/html/2602.16212v1#bib.bib24)]. More generally,
these techniques are special cases of “policy function approximation” for optimal stochastic control [[47](https://arxiv.org/html/2602.16212v1#bib.bib47)].

We begin by formulating the NN optimization problem based on the stochastic control structure of the EW–CVaR formulation P​C​E​Ct0​(α,γ)PCEC\_{t\_{0}}(\alpha,\gamma) given in ([5.6](https://arxiv.org/html/2602.16212v1#S5.E6 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([5.7](https://arxiv.org/html/2602.16212v1#S5.E7 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). To this end, for an arbitrary admissible control 𝒰0∈𝒜\mathcal{U}\_{0}\in\mathcal{A} and an arbitrary threshold WW, we define the objective

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(x0,t0−;𝒰0,W)\displaystyle V(x\_{0},t\_{0}^{-};\,\mathcal{U}\_{0},W) | =𝔼𝒰0X0+,t0+​[∑m=0Mqm+γ​(W+1α​min⁡(WT−W, 0))+ϵ​WT|X0−=x0],\displaystyle=\mathbb{E}\_{\mathcal{U}\_{0}}^{X\_{0^{+}},t\_{0}^{+}}\bigg[\sum\_{m=0}^{M}q\_{m}+\gamma\left(W+\frac{1}{\alpha}\min\left(W\_{T}-W,\,0\right)\right)+\epsilon W\_{T}\,\bigg|\,X\_{0^{-}}=x\_{0}\bigg], |  | (6.1) |
|  |  | subject to the dynamics and constraints specified in ([5.7](https://arxiv.org/html/2602.16212v1#S5.E7 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).\displaystyle\text{ subject to the dynamics and constraints specified in \eqref{eq:PCEC\_constraints}}. |  |

Then, the (exact) value function V​(x0,t0−)V(x\_{0},t\_{0}^{-}) of the P​C​E​Ct0​(α,γ)PCEC\_{t\_{0}}(\alpha,\gamma) problem
is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x0,t0−)=supWsup𝒰0∈𝒜V​(x0,t0−;𝒰0,W).V(x\_{0},t\_{0}^{-})=\sup\_{W}\,\sup\_{\mathcal{U}\_{0}\in\mathcal{A}}\,V(x\_{0},t\_{0}^{-};\,\mathcal{U}\_{0},W). |  | (6.2) |

### 6.1 Approximation of admissible control

The essence of our NN approach is to directly approximate an admissible control 𝒰0\mathcal{U}\_{0} in ([6.2](https://arxiv.org/html/2602.16212v1#S6.E2 "In 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))—that is, a sequence of withdrawal and rebalancing decisions (qm​(⋅),𝒑m​(⋅))\bigl(q\_{m}(\cdot),\,\boldsymbol{p}\_{m}(\cdot)\bigr) for m=0,…,Mm=0,\ldots,M—using feedforward, fully connected neural networks. More specifically, given NN parameters
(weights and biases) 𝜽q\boldsymbol{\theta}\_{q} and 𝜽p\boldsymbol{\theta}\_{p}, we denote by q^​(Wm−,tm,𝜽q)\widehat{q}(W\_{m^{-}},t\_{m},\boldsymbol{\theta}\_{q}) and
𝒑^​(Wm+,tm,𝜽p)\widehat{\boldsymbol{p}}(W\_{m^{+}},t\_{m},\boldsymbol{\theta}\_{p})
the NN-based approximations of the withdrawal control qm​(⋅)q\_{m}(\cdot) and the rebalancing control 𝒑m​(⋅)\boldsymbol{p}\_{m}(\cdot), respectively. Formally, we write

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q^m​(⋅):=q^​(Wm−,tm,𝜽q)\displaystyle\widehat{q}\_{m}(\cdot):=\widehat{q}\left(W\_{m^{-}},t\_{m},\boldsymbol{\theta}\_{q}\right) | ≃\displaystyle\simeq | qm​(Wm−,tm),m=0,1,…,M,\displaystyle q\_{m}(W\_{m^{-}},t\_{m}),\quad m=0,1,\ldots,M, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝒑^m​(⋅):=𝒑^​(Wm+,tm,𝜽p)\displaystyle\widehat{\boldsymbol{p}}\_{m}(\cdot):=\widehat{\boldsymbol{p}}\left(W\_{m^{+}},t\_{m},\boldsymbol{\theta}\_{p}\right) | ≃\displaystyle\simeq | 𝒑m​(Wm+,tm),m=0,1,…,M,\displaystyle\boldsymbol{p}\_{m}(W\_{m^{+}},t\_{m}),\quad m=0,1,\ldots,M, |  | (6.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒰0^:={(q^m​(⋅),𝒑^m​(⋅))|m=0,…,M}\displaystyle\widehat{\mathcal{U}\_{0}}:=\left\{(\widehat{q}\_{m}(\cdot),\widehat{\boldsymbol{p}}\_{m}(\cdot))\,\big|\,m=0,\ldots,M\right\} | ≃\displaystyle\simeq | 𝒰0.\displaystyle\mathcal{U}\_{0}. |  |

Here, 𝒰^0\widehat{\mathcal{U}}\_{0} denotes the NN-based approximation of the admissible control 𝒰0∈𝒜\mathcal{U}\_{0}\in\mathcal{A}.

We now approximate 𝒰0\mathcal{U}\_{0} in the objective V​(x0,t0−;𝒰0,W)V(x\_{0},t\_{0}^{-};\,\mathcal{U}\_{0},W), as defined in ([6.1](https://arxiv.org/html/2602.16212v1#S6.E1 "In 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), by a NN-based counterpart 𝒰^0\widehat{\mathcal{U}}\_{0}. This yields the NN-approximated objective VN​N​(x0,t0−;𝒰0^,W)V\_{NN}(x\_{0},t\_{0}^{-};\,\widehat{\mathcal{U}\_{0}},W), defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | VN​N​(x0,t0−;𝒰0^,W)=𝔼𝒰0^X0+,t0+​[∑m=0Mq^m+γ​(W+1α​min⁡(WT−W, 0))+ϵ​WT|X0−=x0],V\_{NN}(x\_{0},t\_{0}^{-};\,\widehat{\mathcal{U}\_{0}},W)=\mathbb{E}\_{\widehat{\mathcal{U}\_{0}}}^{X\_{0^{+}},t\_{0}^{+}}\bigg[\sum\_{m=0}^{M}\widehat{q}\_{m}+\gamma\left(W+\frac{1}{\alpha}\min\left(W\_{T}-W,\,0\right)\right)+\epsilon W\_{T}\,\bigg|\,X\_{0^{-}}=x\_{0}\bigg], |  | (6.4) |

subject to NN-induced system evolution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to ​{(dynamics){Xt}​ evolves via ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),t∉𝒯,(tontine)Wm−​ computed via ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),(withdrawal)Wm+=Wm−−q^m​(⋅)​ as in ([4.8](https://arxiv.org/html/2602.16212v1#S4.E8 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),(rebalancing)Xm+ computed via ([4.10](https://arxiv.org/html/2602.16212v1#S4.E10 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) using ​𝒑^m​(⋅),(q^m​(⋅),𝒑^m​(⋅))∈𝒵​(Wm−,Wm+,tm),m=0,…,M,}tm∈𝒯.\text{subject to~ }\begin{cases}~~\text{(dynamics)}\quad~~\{X\_{t}\}\text{ evolves via }\eqref{eq:dynamics\_generic},&t\notin\mathcal{T},\\[4.0pt] \left.\begin{array}[]{ll}\text{(tontine)}&W\_{m^{-}}\text{ computed via }\eqref{eq:Wm\_post\_tontine},\\ \text{(withdrawal)}&W\_{m^{+}}=W\_{m^{-}}-\widehat{q}\_{m}(\cdot)\text{ as in }\eqref{eq:Wm\_post\_withdrawal},\\ \text{(rebalancing)}&\text{$X\_{m^{+}}$ computed via \eqref{eq:Xmplus} using }\widehat{\boldsymbol{p}}\_{m}(\cdot),\\ &(\widehat{q}\_{m}(\cdot),\,\widehat{\boldsymbol{p}}\_{m}(\cdot))\in\mathcal{Z}\left(W\_{m^{-}},W\_{m^{+}},t\_{m}\right),\\ &\qquad\qquad m=0,\dots,M,\end{array}\right\}&t\_{m}\in\mathcal{T}.\end{cases} |  | (6.5) |

Then, using ([6.2](https://arxiv.org/html/2602.16212v1#S6.E2 "In 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), V​(x0,t0−)V(x\_{0},t\_{0}^{-}) is approximated by a value function induced by the NN-based control, denoted VN​N​(x0,t0−)V\_{NN}(x\_{0},t\_{0}^{-}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x0,t0−)≃VN​N​(x0,t0−):=supWsup𝒰^0∈𝒜VN​N​(x0,t0−;𝒰0^,W).V(x\_{0},t\_{0}^{-})\simeq V\_{NN}\left(x\_{0},t\_{0}^{-}\right):=\sup\_{W}\,\sup\_{\widehat{\mathcal{U}}\_{0}\in\mathcal{A}}\,V\_{NN}(x\_{0},t\_{0}^{-};\,\widehat{\mathcal{U}\_{0}},W). |  | (6.6) |

### 6.2 Network architecture for controls

To approximate the withdrawal and rebalancing controls (qm,𝒑m)(q\_{m},\,\boldsymbol{p}\_{m}) at each decision time tmt\_{m}, we use two fully connected feedforward neural networks: one for withdrawals q^​(⋅)\widehat{q}(\cdot), and one for rebalancing 𝒑^​(⋅)\widehat{\boldsymbol{p}}(\cdot), parameterized by 𝜽q∈ℝνq\boldsymbol{\theta}\_{q}\in\mathbb{R}^{\nu\_{q}} and 𝜽p∈ℝνp\boldsymbol{\theta}\_{p}\in\mathbb{R}^{\nu\_{p}}, respectively. These networks take inputs of the form (Wm±,tm)(W\_{m^{\pm}},t\_{m}), but at different stages of investor actions:
(i) q^​(⋅)\widehat{q}(\cdot) uses pre-withdrawal wealth after mortality credits have been applied, i.e. (Wm−,tm)(W\_{m^{-}},t\_{m}); and (ii) 𝒑^​(⋅)\widehat{\boldsymbol{p}}(\cdot) uses post-withdrawal wealth, i.e. (Wm+,tm)(W\_{m^{+}},t\_{m}).

To enforce the control constraints in ([4.11](https://arxiv.org/html/2602.16212v1#S4.E11 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) and ([4.12](https://arxiv.org/html/2602.16212v1#S4.E12 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) directly within the networks, we apply suitable output activation functions:

* •

  Withdrawal control: Let z∈ℝz\in\mathbb{R} denote the pre-activation output of the withdrawal network’s final layer. We apply a sigmoid transformation scaled by a wealth-dependent range:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | q^​(Wm−,tm,𝜽q)=qmin+max⁡(min⁡(qmax,Wm−)−qmin, 0)⋅11+e−z.\widehat{q}(W\_{m^{-}},t\_{m},\boldsymbol{\theta}\_{q})=q\_{\min}+\max\left(\min(q\_{\max},W\_{m^{-}})-q\_{\min},\,0\right)\cdot\frac{1}{1+e^{-z}}. |  | (6.7) |

  Since the sigmoid function 11+e−z\frac{1}{1+e^{-z}} maps into (0,1)(0,1), this ensures that q^∈𝒵q​(Wm−,tm)\widehat{q}\in\mathcal{Z}\_{q}(W\_{m^{-}},t\_{m}) without introducing additional optimization constraints.
* •

  Rebalancing control:
  Let 𝒑^m=(p^m(1),…,p^m(k+1))\widehat{\boldsymbol{p}}\_{m}=(\widehat{p}\_{m}^{\,(1)},\ldots,\widehat{p}\_{m}^{\,(k+1)}) denote the vector of rebalancing proportions at time tmt\_{m}, where k=1k=1 for the domestic-only portfolio and k=3k=3 for the internationally diversified portfolio. These proportions are obtained by applying a (k+1)(k+1)-way softmax to the logits (z1,…,zk+1)∈ℝk+1(z\_{1},\ldots,z\_{k+1})\in\mathbb{R}^{k+1} output by the network’s final layer:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | p^m(i)=ezi∑ℓ=1k+1ezℓ,i=1,…,k+1.\widehat{p}\_{m}^{\,(i)}=\frac{e^{z\_{i}}}{\sum\_{\ell=1}^{k+1}e^{z\_{\ell}}},\qquad i=1,\ldots,k+1. |  | (6.8) |

  This guarantees p^m(i)∈[0,1]\widehat{p}\_{m}^{\,(i)}\in[0,1] and ∑i=1k+1p^m(i)=1\sum\_{i=1}^{k+1}\widehat{p}\_{m}^{\,(i)}=1. The first kk components p^m(1),…,p^m(k)\widehat{p}\_{m}^{(1)},\ldots,\widehat{p}\_{m}^{\,(k)} correspond to explicitly parameterized proportions, while p^m(k+1)\widehat{p}\_{m}^{\,(k+1)} (e.g. p^m(2)\widehat{p}\_{m}^{\,(2)} when k=1k=1 and p^m(4)\widehat{p}\_{m}^{\,(4)} when k=3k=3) represents the remaining proportion.
  This transformation enforces the admissibility condition 𝒵p​(Wm+,tm)\mathcal{Z}\_{p}(W\_{m^{+}},t\_{m}) automatically, without the need for post-processing or constraints.

Using these activation functions, we reparameterize the NN-based control 𝒰^0\widehat{\mathcal{U}}\_{0} in terms of its underlying network weights and biases (𝜽q,𝜽p)(\boldsymbol{\theta}\_{q},\boldsymbol{\theta}\_{p}). That is, we write VN​N​(x0,t0−;𝒰^0,W)V\_{NN}(x\_{0},t\_{0}^{-};\,\widehat{\mathcal{U}}\_{0},W) as VN​N​(x0,t0−;𝜽q,𝜽p,W)V\_{NN}(x\_{0},t\_{0}^{-};\,\boldsymbol{\theta}\_{q},\boldsymbol{\theta}\_{p},W) to emphasize that the control policies are fully determined by these parameters.

Then, the control optimization problem ([6.6](https://arxiv.org/html/2602.16212v1#S6.E6 "In 6.1 Approximation of admissible control ‣ 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) becomes an unconstrained optimization over the network parameters 𝜽q\boldsymbol{\theta}\_{q}, 𝜽p\boldsymbol{\theta}\_{p}, and the CVaR threshold WW:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VN​N​(x0,t0−)\displaystyle V\_{NN}\left(x\_{0},\,t\_{0}^{-}\right) | =supWsup𝜽q∈ℝνqsup𝜽p∈ℝνpVN​N​(x0,t0−;𝜽q,𝜽p,W)\displaystyle\,=\,\sup\_{W}\,\sup\_{\boldsymbol{\theta}\_{q}\,\in\,\mathbb{R}^{\nu\_{q}}}\,\sup\_{\boldsymbol{\theta}\_{p}\,\in\,\mathbb{R}^{\nu\_{p}}}V\_{NN}\left(x\_{0},\,t\_{0}^{-};\boldsymbol{\theta}\_{q},\,\boldsymbol{\theta}\_{p},\,W\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =sup(W,𝜽q,𝜽p)∈ℝνq+νp+1VN​N​(x0,t0−;𝜽q,𝜽p,W).\displaystyle\,=\,\sup\_{\left(W,\,\boldsymbol{\theta}\_{q},\,\boldsymbol{\theta}\_{p}\right)\,\in\,\mathbb{R}^{\nu\_{q}+\nu\_{p}+1}}V\_{NN}\left(x\_{0},\,t\_{0}^{-};\boldsymbol{\theta}\_{q},\,\boldsymbol{\theta}\_{p},\,W\right). |  | (6.9) |

We denote by 𝜽q∗\boldsymbol{\theta}\_{q}^{\*}, 𝜽p∗\boldsymbol{\theta}\_{p}^{\*}, and W∗W^{\*} the optimal network parameters and threshold.

We emphasize that, while the original control problem is constrained via the admissible set 𝒜\mathcal{A} (see ([4.14](https://arxiv.org/html/2602.16212v1#S4.E14 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))), the reformulated NN objective ([6.2](https://arxiv.org/html/2602.16212v1#S6.Ex3 "6.2 Network architecture for controls ‣ 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is unconstrained in terms of the training variables. This allows the use of standard gradient-based methods for optimization. In our numerical implementation (Sections [9](https://arxiv.org/html/2602.16212v1#S9 "9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")
and [8](https://arxiv.org/html/2602.16212v1#S8 "8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), we use Adam stochastic gradient descent to train the networks and determine the optimal parameters.

### 6.3 Approximation of the NN-induced objective

To evaluate the NN-induced objective in ([6.2](https://arxiv.org/html/2602.16212v1#S6.Ex3 "6.2 Network architecture for controls ‣ 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), we approximate its expectation using a finite set of NN independent sample paths, each representing a full set of exogenous drivers for the asset indices (generated by ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))). Mortality enters only through the pathwise tontine gain rates (see Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
These sample paths are indexed by n=1,…,Nn=1,\ldots,N, and all path-dependent quantities carry the superscript “(n)(n)”. For example, Xt(n)t∈[0,T]{X\_{t}^{(n)}}\_{t\in[0,T]} is the simulated state trajectory for the nn-th path, and WT(n)W\_{T}^{(n)} is the corresponding terminal wealth.

Specifically, given any set of NN parameters (𝜽q,𝜽p)(\boldsymbol{\theta}\_{q},\boldsymbol{\theta}\_{p}) and threshold WW,
the NN-induced objective
VN​N​(x0,t0−;𝜽q,𝜽p,W)V\_{NN}\left(x\_{0},\,t\_{0}^{-};\boldsymbol{\theta}\_{q},\,\boldsymbol{\theta}\_{p},\,W\right)
is approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | VN​N​(x0,t0−;𝜽q,𝜽p,W)≈V^N​N​(x0,t0−,𝜽q,𝜽p,W)V\_{NN}\left(x\_{0},\,t\_{0}^{-};\boldsymbol{\theta}\_{q},\,\boldsymbol{\theta}\_{p},\,W\right)\approx\widehat{V}\_{NN}\left(x\_{0},\,t\_{0}^{-},\,\boldsymbol{\theta}\_{q},\boldsymbol{\theta}\_{p},W\right) |  | (6.10) |

where V^N​N​(x0,t0−,𝜽q,𝜽p,W):=…\widehat{V}\_{NN}\left(x\_{0},\,t\_{0}^{-},\,\boldsymbol{\theta}\_{q},\boldsymbol{\theta}\_{p},W\right):=\ldots

|  |  |  |  |
| --- | --- | --- | --- |
|  | …:=1N​∑n=1N[∑m=0Mq^m​(Wm−(n),tm;𝜽q)+γ​(W+1α​min⁡(WT(n)−W, 0))+ϵ​WT(n)],\ldots:=\frac{1}{N}\sum\_{n=1}^{N}\bigg[\sum\_{m=0}^{M}\widehat{q}\_{m}\big(W\_{m^{-}}^{(n)},t\_{m};\,\boldsymbol{\theta}\_{q}\big)+\gamma\big(W+\tfrac{1}{\alpha}\min(W\_{T}^{(n)}-W,\,0)\big)+\epsilon W\_{T}^{(n)}\bigg], |  | (6.11) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. ​{(dynamics){Xt(n)}​ drawn from the n-th sample path of index returns,(generated by ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")))t∉𝒯,(tontine)Wm−(n)​ computed via ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),using the pathwise gm(n) given by ([4.4](https://arxiv.org/html/2602.16212v1#S4.E4 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))(see Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),(withdrawal)Wm+(n)=Wm−(n)−q^​(Wm−(n),tm,𝜽q),(rebalancing)Xm+(n) computed from ([4.10](https://arxiv.org/html/2602.16212v1#S4.E10 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), using ​𝒑^​(Wm+(n),tm,𝜽p),(q^m​(⋅),𝒑^m​(⋅))∈𝒵​(Wm−(n),Wm+(n),tm),m=0,…,M,}tm∈𝒯.\text{s.t.~ }\begin{cases}~~\text{(dynamics)}\quad~~\{X\_{t}^{(n)}\}\text{ drawn from the $n$-th sample path of index returns},\\ \qquad\qquad\qquad\quad~\text{(generated by \eqref{eq:dynamics\_generic})}&t\notin\mathcal{T},\\[4.0pt] \left.\begin{array}[]{ll}\text{(tontine)}&W\_{m^{-}}^{(n)}\text{ computed via \eqref{eq:Wm\_post\_tontine}},\\ &{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}{\text{using the pathwise $g\_{m}^{(n)}$ given by \eqref{eq:mod\_Tg}}}}{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}{\text{(see Remark~\ref{rm:stochastic\_mortality})}}},\\ \text{(withdrawal)}&W\_{m^{+}}^{(n)}=W\_{m^{-}}^{(n)}-\widehat{q}\big(W\_{m^{-}}^{(n)},t\_{m},\boldsymbol{\theta}\_{q}\big),\\ \text{(rebalancing)}&\text{$X\_{m^{+}}^{(n)}$ computed from \eqref{eq:Xmplus}, using }\widehat{\boldsymbol{p}}\big(W\_{m^{+}}^{(n)},t\_{m},\boldsymbol{\theta}\_{p}\big),\\ &\big(\widehat{q}\_{m}(\cdot),\,\widehat{\boldsymbol{p}}\_{m}(\cdot)\big)\in\mathcal{Z}\left(W\_{m^{-}}^{(n)},W\_{m^{+}}^{(n)},t\_{m}\right),\quad m=0,\dots,M,\end{array}\right\}&t\_{m}\in\mathcal{T}.\end{cases} |  | (6.12) |

For subsequent benchmark comparisons, we generate sample paths using the generic transition dynamics defined in ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), which encapsulate both parametric SDE models and nonparametric bootstrapped trajectories. In our two-asset benchmarks, the dynamics follow a Kou-type jump–diffusion model (see Subsection [8.4](https://arxiv.org/html/2602.16212v1#S8.SS4 "8.4 Validation results ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). For higher-dimensional or empirically calibrated settings, we adopt the block bootstrap methodology described in Section [9](https://arxiv.org/html/2602.16212v1#S9 "9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

As in Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), each simulation path nn carries a
sequence of one–year conditional death probabilities
{δm−1(n)}m=1M\{\delta\_{m-1}^{(n)}\}\_{m=1}^{M}. In the deterministic life–table case these are
path–independent, δm−1(n)≡δm−1\delta\_{m-1}^{(n)}\equiv\delta\_{m-1}, whereas under stochastic
LC/CBD mortality they are read off from the simulated surface {qx,t(n)}\{q\_{x,t}^{(n)}\}.
In both cases we convert δm−1(n)\delta\_{m-1}^{(n)} to tontine gain rates
gm(n)=δm−1(n)/(1−δm−1(n))g\_{m}^{(n)}=\delta\_{m-1}^{(n)}/(1-\delta\_{m-1}^{(n)}) which enter the pathwise
versions of ([4.4](https://arxiv.org/html/2602.16212v1#S4.E4 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) when computing
Wm−(n)W\_{m^{-}}^{(n)} in ([6.12](https://arxiv.org/html/2602.16212v1#S6.E12 "In 6.3 Approximation of the NN-induced objective ‣ 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). Throughout the EW–CVaR
optimization we adopt the ”plan to live” convention: during NN training the member
is assumed to survive the full horizon, so these mortality inputs affect only the
size of the mortality credits, not the termination time of the path.

Given the sample–based objective
V^N​N​(x0,t0−;𝜽𝒒,𝜽𝒑,W)\widehat{V}\_{NN}\!\bigl(x\_{0},t\_{0}^{-};\,\boldsymbol{\theta}\_{\boldsymbol{q}},\boldsymbol{\theta}\_{\boldsymbol{p}},W\bigr)
in ([6.11](https://arxiv.org/html/2602.16212v1#S6.E11 "In 6.3 Approximation of the NN-induced objective ‣ 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([6.12](https://arxiv.org/html/2602.16212v1#S6.E12 "In 6.3 Approximation of the NN-induced objective ‣ 6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), we train the networks by solving the empirical maximization problem666Equivalently, we minimize the empirical loss function
ℒ​(𝜽𝒒,𝜽𝒑,W):=−V^N​N​(x0,t0−;𝜽𝒒,𝜽𝒑,W).\mathcal{L}\bigl(\boldsymbol{\theta}\_{\boldsymbol{q}},\boldsymbol{\theta}\_{\boldsymbol{p}},W\bigr):=-\widehat{V}\_{NN}\!\bigl(x\_{0},t\_{0}^{-};\boldsymbol{\theta}\_{\boldsymbol{q}},\boldsymbol{\theta}\_{\boldsymbol{p}},W\bigr).

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝜽𝒒∗,𝜽𝒑∗,W∗):=arg⁡max𝜽𝒒,𝜽𝒑,W​V^N​N​(x0,t0−;𝜽𝒒,𝜽𝒑,W)(\boldsymbol{\theta}\_{\boldsymbol{q}}^{\*},\boldsymbol{\theta}\_{\boldsymbol{p}}^{\*},W^{\*})\;:=\;\underset{\boldsymbol{\theta}\_{\boldsymbol{q}},\,\boldsymbol{\theta}\_{\boldsymbol{p}},\,W}{\arg\max}\;\widehat{V}\_{NN}\!\bigl(x\_{0},t\_{0}^{-};\boldsymbol{\theta}\_{\boldsymbol{q}},\boldsymbol{\theta}\_{\boldsymbol{p}},W\bigr) |  | (6.13) |

with a gradient-based optimizer, such as Adam stochastic gradient descent.
The resulting parameters define the learned control policies

|  |  |  |
| --- | --- | --- |
|  | q^∗​(⋅):=q^​(⋅;𝜽q∗),𝒑^∗​(⋅):=𝒑^​(⋅;𝜽p∗),\widehat{q}^{\*}(\cdot):=\widehat{q}(\cdot;\,\boldsymbol{\theta}\_{q}^{\*}),\qquad\widehat{\boldsymbol{p}}^{\*}(\cdot):=\widehat{\boldsymbol{p}}(\cdot;\,\boldsymbol{\theta}\_{p}^{\*}), |  |

which yields the NN-based optimal control

|  |  |  |
| --- | --- | --- |
|  | 𝒰^0∗:={(q^m∗​(⋅),𝒑^m∗​(⋅))|m=0,…,M}.\widehat{\mathcal{U}}\_{0}^{\*}:=\bigl\{\,(\widehat{q}\_{m}^{\*}(\cdot),\,\widehat{\boldsymbol{p}}\_{m}^{\*}(\cdot))\;\big|\;m=0,\ldots,M\,\bigr\}. |  |

We evaluate the performance of these trained control policies on out-of-sample or out-of-distribution test paths. Detailed numerical results are presented in Sections [9](https://arxiv.org/html/2602.16212v1#S9 "9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")
and [8](https://arxiv.org/html/2602.16212v1#S8 "8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

## 7 Pricing of the MBG

The optimal withdrawal and rebalancing controls q∗​(⋅)q^{\*}(\cdot) and 𝒑∗​(⋅)\boldsymbol{p}^{\*}(\cdot) of the pre-commitment EW–CVaR problem P​C​E​Ct0​(α,γ)PCEC\_{t\_{0}}(\alpha,\gamma) maximize expected withdrawals conditional on survival—that is, the “plan to live, not to die” objective defined in ([5.4](https://arxiv.org/html/2602.16212v1#S5.E4 "In 5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), which assumes the retiree remains alive throughout the decumulation horizon.

By contrast, the MBG overlay is triggered by early death and guarantees that the member’s cumulative withdrawals, expressed in nominal dollars, are never less than the initial investment L0L\_{0}, as reflected in the payout formula ([3.1](https://arxiv.org/html/2602.16212v1#S3.E1 "In 3.1 Description ‣ 3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
Because the MBG pays any shortfall to the estate only upon death—and never credits the retiree’s account—the payout does not affect the account balance or the decision process. Hence, the control pair (q∗​(⋅),𝒑∗​(⋅))(q^{\*}(\cdot),\boldsymbol{p}^{\*}(\cdot)) remains optimal for the EW-CVaR objective even when the overlay is present.

Since the MBG-payout ([3.1](https://arxiv.org/html/2602.16212v1#S3.E1 "In 3.1 Description ‣ 3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is defined in nominal dollars at the payment time tmτt\_{m\_{\tau}}, the nominal amount must be converted to real units before valuation. Specifically, at time tmτt\_{m\_{\tau}}, the nominal shortfall is multiplied by the CPI ratio CPI0/CPImτ\mathrm{CPI}\_{0}/\mathrm{CPI}\_{m\_{\tau}} to obtain its real
value at t0t\_{0}. This adjustment reflects the end-of-interval convention in Remark [3.1](https://arxiv.org/html/2602.16212v1#S3.Thmremark1 "Remark 3.1 (Timing convention). ‣ 3.1 Description ‣ 3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), under which the MBG-payout is implemented at time tmτt\_{m\_{\tau}}.

With this in mind, we define the random real dollar MBG payout

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zg:=CPI0CPImτ​max⁡(L0−∑ℓ=0mτ−1qℓ∗​(⋅)​CPIℓCPI0,0).Z\_{g}:=\frac{\mathrm{CPI}\_{0}}{\mathrm{CPI}\_{m\_{\tau}}}\,\max\bigl(L\_{0}-\sum\_{\ell=0}^{m\_{\tau}-1}q^{\*}\_{\ell}(\cdot)\,\frac{\mathrm{CPI}\_{\ell}}{\mathrm{CPI}\_{0}},0\bigr). |  | (7.1) |

We note that, equivalently, in ([7.1](https://arxiv.org/html/2602.16212v1#S7.E1 "In 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), the combination of the two CPI ratios—CPIℓ/CPI0\mathrm{CPI}\_{\ell}/\mathrm{CPI}\_{0} inside the sum and CPI0/CPImτ\mathrm{CPI}\_{0}/\mathrm{CPI}\_{m\_{\tau}} outside—acts to express all terms in real dollars at time t0t\_{0}.

### 7.1 Actuarial pricing formula

As discussed in Section [3.2](https://arxiv.org/html/2602.16212v1#S3.SS2 "3.2 MBG pricing load ‣ 3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), money-back protection can be funded through
different mechanisms (e.g. internal pool funding versus external insurance).
To report the economic cost of the MBG in a transparent and implementation-agnostic way, we summarize it using an equivalent up-front load factor fg∈(0,1)f\_{g}\in(0,1) applied to
the initial contribution L0L\_{0}.

All quantities in the pricing rule below are expressed in real (inflation-adjusted) dollars at t0t\_{0}.
We choose fgf\_{g} so that the real value of the load equals the real-world expected MBG payout
plus an explicit prudential buffer based on a tail risk measure
(a standard risk-measure/premium-principle approach in actuarial pricing; see, e.g. [[63](https://arxiv.org/html/2602.16212v1#bib.bib63), [12](https://arxiv.org/html/2602.16212v1#bib.bib12)]).

Formally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | fg​L0=𝔼𝒰0∗x0,t0​[Zg]+λ​CVaRαgx0,t0​[Zg],λ≥0,αg∈(0,1).f\_{g}\,L\_{0}=\mathbb{E}^{\,x\_{0},t\_{0}}\_{\mathcal{U}\_{0}^{\*}}\bigl[Z\_{g}\bigr]\;+\;\lambda\,\mathrm{CVaR}\_{\alpha\_{g}}^{\,x\_{0},t\_{0}}\bigl[Z\_{g}\bigr],\quad\lambda\geq 0,\quad\alpha\_{g}\in(0,1). |  | (7.2) |

* •

  𝔼𝒰0∗x0,t0​[Zg]\mathbb{E}^{\,x\_{0},t\_{0}}\_{\mathcal{U}\_{0}^{\*}}\bigl[Z\_{g}\bigr] is the real-world expectation of the MBG payout ZgZ\_{g}
  (in real t0t\_{0} dollars), evaluated under the wealth process induced by the
  optimal control 𝒰0∗=(q∗​(⋅),𝒑∗​(⋅))\mathcal{U}\_{0}^{\*}=(q^{\*}(\cdot),\boldsymbol{p}^{\*}(\cdot))
  of the problem P​C​E​Ct0​(α,γ)PCEC\_{t\_{0}}(\alpha,\gamma).
* •

  CVaRαgx0,t0​[Zg]\mathrm{CVaR}\_{\alpha\_{g}}^{\,x\_{0},t\_{0}}\bigl[Z\_{g}\bigr] is the CVaR of the same real dollar payout at tail level αg\alpha\_{g},
  computed under the same induced wealth process. The tail level αg\alpha\_{g} is a
  prudential-buffer choice and need not coincide with the confidence level α\alpha
  used in the retiree’s EW–CVaR objective.777The MBG payout is a low-frequency,
  high-severity liability with a heavy-tailed profile, so tail measures such as CVaR
  provide a natural basis for a prudential buffer.
* •

  λ\lambda is the prudential-buffer coefficient: λ=0\lambda=0 corresponds to an
  actuarially fair (expected-cost) equivalent load, while λ>0\lambda>0 adds an explicit
  buffer for adverse outcomes (e.g. to reflect internal risk limits or capital-adequacy
  considerations).

Given (λ,αg)(\lambda,\alpha\_{g}) and the induced payout distribution of ZgZ\_{g} under the optimal policy 𝒰0∗\mathcal{U}\_{0}^{\*}, ([7.2](https://arxiv.org/html/2602.16212v1#S7.E2 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) defines the equivalent load fgf\_{g}. In practice, the same economic cost could be implemented through different mechanisms, such as an implicit reduction in the starting income rate, pool-level self-insurance, or external insurance premia; our use of fgf\_{g} provides a common metric for comparing such designs.

We now give explicit expressions for the two valuation functionals in ([7.2](https://arxiv.org/html/2602.16212v1#S7.E2 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), both expressed in real dollars at time t0t\_{0}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼𝒰0∗x0,t0​[Zg]\displaystyle\mathbb{E}^{\,x\_{0},t\_{0}}\_{\mathcal{U}\_{0}^{\*}}\bigl[Z\_{g}\bigr] | =𝔼𝒰0∗X0+,t0+​[Zg|X0−=x0],\displaystyle=\mathbb{E}\_{\mathcal{U}\_{0}^{\*}}^{X\_{0^{+}},t\_{0}^{+}}\bigl[Z\_{g}\;\big|\;X\_{0^{-}}=x\_{0}\bigr], |  | (7.3) |
|  | CVaRαgx0,t0​[Zg]\displaystyle\mathrm{CVaR}\_{\alpha\_{g}}^{\,x\_{0},t\_{0}}\bigl[Z\_{g}\bigr] | =1αg​𝔼𝒰0∗X0+,t0+​[Zg​ 1{Zg≥VaRαg​(Zg)}|X0−=x0],\displaystyle=\frac{1}{\alpha\_{g}}\,\mathbb{E}\_{\mathcal{U}\_{0}^{\*}}^{X\_{0^{+}},t\_{0}^{+}}\!\Bigl[Z\_{g}\mathbf{1}\_{\{\,Z\_{g}\geq\mathrm{VaR}\_{\alpha\_{g}}(Z\_{g})\}}\;\big|\;X\_{0^{-}}=x\_{0}\Bigr], |  |

subject to system evolution induced by 𝒰0∗=(q∗​(⋅),𝒑∗​(⋅))\mathcal{U}\_{0}^{\*}=(q^{\*}(\cdot),\boldsymbol{p}^{\*}(\cdot)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to ​{(dynamics){Xt}​ evolves via ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),t∉𝒯, 0≤t<tmτ(tontine)Wℓ−​ computed via ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),(withdrawal)Wℓ+=Wℓ−−qℓ∗​(⋅)​ as in ([4.8](https://arxiv.org/html/2602.16212v1#S4.E8 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")),(rebalancing)Xℓ+ computed via ([4.10](https://arxiv.org/html/2602.16212v1#S4.E10 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) using ​𝒑ℓ∗​(⋅),}ℓ=0,…,mτ−1.\text{subject to~ }\begin{cases}~~\text{(dynamics)}\quad~~\{X\_{t}\}\text{ evolves via }\eqref{eq:dynamics\_generic},&t\notin\mathcal{T},\;0\leq t<t\_{m\_{\tau}}\\[4.0pt] \left.\begin{array}[]{ll}\text{(tontine)}&W\_{\ell^{-}}\text{ computed via }\eqref{eq:Wm\_post\_tontine},\\ \text{(withdrawal)}&W\_{\ell^{+}}=W\_{\ell^{-}}-q\_{\ell}^{\*}(\cdot)\text{ as in }\eqref{eq:Wm\_post\_withdrawal},\\ \text{(rebalancing)}&\text{$X\_{\ell^{+}}$ computed via \eqref{eq:Xmplus} using }\boldsymbol{p}\_{\ell}^{\*}(\cdot),\end{array}\right\}&\ell=0,\ldots,m\_{\tau}-1.\end{cases} |  | (7.4) |

###### Remark 7.1 (Interpreting fgf\_{g} in starting–rate terms).

Equation ([7.2](https://arxiv.org/html/2602.16212v1#S7.E2 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) produces an equivalent up-front load fgf\_{g} on the initial
contribution L0L\_{0} (i.e. a one-time cost measure expressed as a proportion of L0L\_{0}).
For ease of interpretation in the numerical results, we also translate fgf\_{g} into an
implied reduction in a notional starting payment rate. Fix a notional starting
payment rate β0\beta\_{0} (per dollar of contribution) for the same tontine design *without*
the MBG. Under the reporting convention that the MBG cost is expressed as an equivalent
up-front adjustment to the initial contribution (or benefit base), the implied post–load
starting rate is βg=(1−fg)​β0\beta\_{g}=(1-f\_{g})\beta\_{0}, i.e. a reduction of fg​β0f\_{g}\beta\_{0} (or
104​fg​β010^{4}f\_{g}\beta\_{0} basis points) from the reference rate.
We emphasize that β0\beta\_{0} is used
only as a translation device for reporting and need not correspond to any specific operational funding mechanism.

### 7.2 Simulation-based numerical methods

The MBG price is estimated from KK independent sample paths, each representing a full set of exogenous drivers for index returns as given by ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), and, when relevant, mortality realizations. These sample paths are indexed by k=1,…,Kk=1,\ldots,K, and all path-dependent quantities carry the superscript (k)(k).

The pricing procedure uses the trained control networks q^∗​(⋅)\widehat{q}^{\*}(\cdot) and 𝒑^∗​(⋅)\widehat{\boldsymbol{p}}^{\*}(\cdot) obtained from Section [6](https://arxiv.org/html/2602.16212v1#S6 "6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), which approximate the optimal withdrawal and rebalancing strategies for the EW–CVaR problem. These controls are held fixed during the MBG valuation and applied across all sample paths.

For each path k=1,…,Kk=1,\ldots,K, the wealth evolution follows the dynamics induced by the control pair
𝒰^0∗=(q^∗​(⋅),𝒑^∗​(⋅))\widehat{\mathcal{U}}\_{0}^{\*}=\bigl(\widehat{q}^{\*}(\cdot),\,\widehat{\boldsymbol{p}}^{\*}(\cdot)\bigr)
obtained in Section [6](https://arxiv.org/html/2602.16212v1#S6 "6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").
We write {Xt(k)}t∈[0,T]\{X\_{t}^{(k)}\}\_{t\in[0,T]} for the resulting state trajectory on path kk;
all withdrawals and allocations at the rebalancing times
tm∈𝒯t\_{m}\in\mathcal{T} are the network outputs
q^∗​(Wm−(k),tm)\widehat{q}^{\*}(W\_{m^{-}}^{(k)},t\_{m}) and
𝒑^∗​(Wm+(k),tm)\widehat{\boldsymbol{p}}^{\*}(W\_{m^{+}}^{(k)},t\_{m})
evaluated with the path-specific inputs.

As summarized in Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), each simulation path kk
is equipped with a sequence of one–year conditional death probabilities
{δm−1(k)}m=1M\{\delta\_{m-1}^{(k)}\}\_{m=1}^{M}. These probabilities are converted to
tontine gain rates gm(k)=δm−1(k)/(1−δm−1(k))g\_{m}^{(k)}=\delta\_{m-1}^{(k)}/\bigl(1-\delta\_{m-1}^{(k)}\bigr)
when computing mortality credits via ([4.4](https://arxiv.org/html/2602.16212v1#S4.E4 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
In addition, they also drive the simulation of death times and MBG payouts along each path as outlined in Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") below.
Together with the domestic CPI series {CPIm}m=0M\{\mathrm{CPI}\_{m}\}\_{m=0}^{M} (one value per decision time),
these mortality inputs determine the timing and real dollar size of the pathwise
MBG payouts.

The simulation-based pricing details are described in Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").
This algorithm computes Monte Carlo estimates
𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}] and CVaR^αg​(Zg)\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g})
of the theoretical valuation functionals
𝔼𝒰0∗x0,t0​[Zg]\mathbb{E}^{\,x\_{0},t\_{0}}\_{\mathcal{U}\_{0}^{\*}}[Z\_{g}] and
CVaRαgx0,t0​[Zg]\mathrm{CVaR}\_{\alpha\_{g}}^{\,x\_{0},t\_{0}}[Z\_{g}] in ([7.3](https://arxiv.org/html/2602.16212v1#S7.E3 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
For each path k=1,…,Kk=1,\ldots,K, we denote by Zg(k)Z\_{g}^{(k)} the simulated real dollar MBG payout, obtained by applying ([7.1](https://arxiv.org/html/2602.16212v1#S7.E1 "In 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) with the path-specific withdrawal history and death time.

Algorithm 7.1  Simulation–based MBG pricing under trained NN controls

1: initialize the index list 𝒦←{1,…,K}\mathcal{K}\leftarrow\{1,\dots,K\};

2: initialise the list 𝒵←[0,…,0]\mathcal{Z}\leftarrow[0,\ldots,0] of length KK;

3: initialize MBG-payouts Zg(k)←0Z\_{g}^{(k)}\leftarrow 0, k=1,…,Kk=1,\ldots,K;

4: initialize cumulative nominal withdrawals 𝒲(k)←0\,\mathcal{W}^{(k)}\!\leftarrow 0,
k=1,…,Kk=1,\ldots,K;

5: initialize X0−(k)=x0X\_{0^{-}}^{(k)}\!=x\_{0} and compute W0−(k)W\_{0^{-}}^{(k)} for all k∈𝒦k\in\mathcal{K};

6: for m=0m=0 to M−1M-1 do

7:  for each k∈𝒦k\in\mathcal{K} do

8:   compute pathwise gm(k)g\_{m}^{(k)} via ([4.4](https://arxiv.org/html/2602.16212v1#S4.E4 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))
(see Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))
and Wm−(k)W\_{m^{-}}^{(k)} via ([4.7](https://arxiv.org/html/2602.16212v1#S4.E7 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"));
{mortality credit}

9:   qm(k)←q^∗​(Wm−(k),tm)q\_{m}^{(k)}\leftarrow\widehat{q}^{\*}\!\bigl(W\_{m^{-}}^{(k)},t\_{m}\bigr); {real dollars}

10:   𝒲(k)←𝒲(k)+qm(k)​CPIm(k)CPI0\mathcal{W}^{(k)}\leftarrow\mathcal{W}^{(k)}+q\_{m}^{(k)}\,\dfrac{\mathrm{CPI}\_{m}^{(k)}}{\mathrm{CPI}\_{0}};
{nominal withdrawal accumulation}

11:   Wm+(k)←Wm−(k)−qm(k)W\_{m^{+}}^{(k)}\leftarrow W\_{m^{-}}^{(k)}-q\_{m}^{(k)};

12:   obtain Xm+(k)X\_{m^{+}}^{(k)} via ([4.10](https://arxiv.org/html/2602.16212v1#S4.E10 "In 4.2 Mortality updates and control framework ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) using
𝒑^∗​(Wm+(k),tm)\widehat{\boldsymbol{p}}^{\*}\!\bigl(W\_{m^{+}}^{(k)},t\_{m}\bigr);
{rebalancing}

13:   compute X(m+1)−(k)X\_{(m+1)^{-}}^{(k)}, k=1,…​Kk=1,\ldots K,
via ([4.2](https://arxiv.org/html/2602.16212v1#S4.E2 "In 4.1 Index dynamics ‣ 4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"));
{simulation over [tm+,tm+1−][t\_{m}^{+},t\_{m+1}^{-}]};

14:   if the member dies in (tm+,tm+1−](t\_{m}^{+},t\_{m+1}^{-}] then

15:    
Zg(k)←CPI0CPIm+1(k)​max⁡(L0−𝒲(k), 0)\displaystyle Z\_{g}^{(k)}\leftarrow\frac{\mathrm{CPI}\_{0}}{{{\mathrm{CPI}\_{m+1}^{(k)}}}}\,\max\Bigl(L\_{0}-\mathcal{W}^{(k)},\,0\Bigr);

16:    set 𝒵(k)←Zg(k)\mathcal{Z}^{(k)}\leftarrow Z\_{g}^{(k)};

17:    remove path kk from list 𝒦\mathcal{K};

18:   end if

19:  end for

20:  if 𝒦=∅\mathcal{K}=\emptyset then

21:   break; {all deaths processed}

22:  end if

23: end for

24: compute sample mean:
E^=1K​∑k=1KZg(k)\displaystyle\widehat{E}\;=\;\frac{1}{K}\sum\_{k=1}^{K}Z\_{g}^{(k)};

25: sort list 𝒵\mathcal{Z} in descending order to obtain
Z(1)≥Z(2)≥⋯≥Z(K)Z\_{(1)}\geq Z\_{(2)}\geq\cdots\geq Z\_{(K)};

26: compute empirical C​V​a​R^αg\widehat{CVaR}\_{\alpha\_{g}}:
C​V​a​R^αg=1⌈αg​K⌉​∑j=1⌈αg​K⌉Z(j)\displaystyle\widehat{CVaR}\_{\alpha\_{g}}\;=\;\frac{1}{\lceil\alpha\_{g}K\rceil}\sum\_{j=1}^{\lceil\alpha\_{g}K\rceil}Z\_{(j)};

27: return (E^,C​V​a​R^αg)\bigl(\widehat{E},\;\widehat{CVaR}\_{\alpha\_{g}}\bigr);

With 𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}] and CVaR^αg​(Zg)\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g})
computed by Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"),
the actuarial load factor fgf\_{g} defined by ([7.2](https://arxiv.org/html/2602.16212v1#S7.E2 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))
is approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^g:=𝔼^​[Zg]+λ​CVaR^αg​(Zg)L0.\widehat{f}\_{g}\;:=\;\frac{\widehat{\mathbb{E}}[Z\_{g}]+\lambda\,\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g})}{L\_{0}}. |  | (7.5) |

In the numerical results, we report f^g\widehat{f}\_{g} (and the associated up-front
deduction f^g​L0\widehat{f}\_{g}L\_{0}).

###### Remark 7.2.

In Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") the test “member dies during
(tm+,tm+1−](t\_{m}^{+},t\_{m+1}^{-}]” (Line [14](https://arxiv.org/html/2602.16212v1#S7.alg1.l14 "In Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) is implemented as a Bernoulli
experiment based on the pathwise probabilities δm(k)\delta\_{m}^{(k)} introduced in
Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").
Concretely, for every path kk and every year mm in which the member
is still alive we draw U∼Uniform​(0,1)U\sim\mathrm{Uniform}(0,1) and declare death
in (tm+,tm+1−](t\_{m}^{+},t\_{m+1}^{-}] when U<δm(k)U<\delta\_{m}^{(k)}.
The corresponding index is then mτ=m+1m\_{\tau}=m+1, so that,
under the timing convention of Remark [3.1](https://arxiv.org/html/2602.16212v1#S3.Thmremark1 "Remark 3.1 (Timing convention). ‣ 3.1 Description ‣ 3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"),
the MBG payment is effected at tmτt\_{m\_{\tau}}.
If no death is recorded up to m=M−1m=M-1, the member is deemed to have
survived the entire horizon and Zg(k)=0Z\_{g}^{(k)}=0 on that path.

###### Remark 7.3 (Inflation treatment in MBG pricing).

In the numerical experiments, wealth is simulated in real (inflation-adjusted)
units using bootstrapped real asset returns, so CPI does not enter the wealth
recursion. CPI is used only in Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") to implement the
money-back test in nominal dollars at the death time and to express the resulting
MBG payout back in real t0t\_{0} dollars.

To obtain a stochastic (pathwise) inflation adjustment consistent with the bootstrap,
the CPI index is treated as an additional series in the resampling procedure:
monthly CPI changes are bootstrapped jointly with the asset-return blocks (preserving
the dependence structure), a CPI index path is reconstructed along each simulated
path, and the corresponding pathwise CPI ratios are used in the nominal–real
conversion step of Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"). See
CPIm(k)\mathrm{CPI}\_{m}^{(k)} on Line [10](https://arxiv.org/html/2602.16212v1#S7.alg1.l10 "In Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") and
CPIm+1(k)\mathrm{CPI}\_{m+1}^{(k)} on Line [15](https://arxiv.org/html/2602.16212v1#S7.alg1.l15 "In Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") of Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

## 8 Benchmark validation

In this section we validate our numerical implementation by replicating, as closely as possible, the synthetic–market results of [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)].
Their study solves an EW–CVaR optimal stochastic control problem for a decumulation portfolio with and without a tontine overlay, using dynamic programming and a PIDE solver, and reports the corresponding efficient frontiers and optimal controls.

We follow the modelling assumptions, data calibration, and base–case investment scenario in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], which are described below, and assume mortality given by the 2014 Canadian Pensioner Mortality Table (CPM2014), treated as a deterministic period life table. In our notation this corresponds to a sequence of one–year conditional death probabilities {δm−1}m=1M\{\delta\_{m-1}\}\_{m=1}^{M} taken directly from CPM2014, with δm−1(n)≡δm−1\delta\_{m-1}^{(n)}\equiv\delta\_{m-1} on every simulation path nn, exactly as in the deterministic case discussed in Subsection [2.2.1](https://arxiv.org/html/2602.16212v1#S2.SS2.SSS1 "2.2.1 Deterministic mortality ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") and Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").
Within this common framework, we compare the EW–CVaR efficient frontiers produced by our NN method with the reference frontiers reported in Figure 1 of [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)].

In the remainder of the paper, we also consider a more general setting with an internationally diversified four–asset opportunity set and stochastic mortality, as developed in Subsection [2.2](https://arxiv.org/html/2602.16212v1#S2.SS2 "2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"). However, the benchmark validation in this section is based solely on the original two domestic assets and deterministic mortality, in order to allow a direct comparison with [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)].

### 8.1 Asset dynamics

For the benchmark we restrict attention to the two domestic assets considered in
[[21](https://arxiv.org/html/2602.16212v1#bib.bib21)]: a broad domestic equity index and a constant–maturity domestic short–term government bond index.
We follow the usual practitioner approach and directly model the returns of the constant–maturity bond index as a stochastic process (see, e.g. [[34](https://arxiv.org/html/2602.16212v1#bib.bib34), [32](https://arxiv.org/html/2602.16212v1#bib.bib32)]). Consistent with the stock index, we assume that the constant–maturity bond index also follows a jump–diffusion specification. Empirical justification for this modelling choice can be found in [[19](https://arxiv.org/html/2602.16212v1#bib.bib19)][Appendix A].

We denote by {St}0≤t≤T\{S\_{t}\}\_{0\leq t\leq T} the real value invested in the domestic stock index at time tt, and {Bt}0≤t≤T\{B\_{t}\}\_{0\leq t\leq T} the real value invested in the
domestic bond index.
In the absence of investor actions (withdrawals or rebalancing), both assets
follow correlated double–exponential jump–diffusion processes as in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)][Section 4].

Let ξs\xi\_{s} be a random variable representing the jump multiplier, such that a jump occurring at time tt results in St=ξs​St−S\_{t}=\xi\_{s}\,S\_{t^{-}}. We assume ln⁡(ξs)\ln(\xi\_{s}) follows an asymmetric double-exponential distribution with probability density function (see [[28](https://arxiv.org/html/2602.16212v1#bib.bib28), [29](https://arxiv.org/html/2602.16212v1#bib.bib29)])

|  |  |  |  |
| --- | --- | --- | --- |
|  | φs​(y)=ζs​ηs,1​e−ηs,1​y​ 1y≥0+(1−ζs)​ηs,2​eηs,2​y​ 1y<0,ζs∈[0,1],ηs,1>1,ηs,2>0.\varphi\_{s}(y)=\zeta\_{s}\,\eta\_{s,1}\,e^{-\eta\_{s,1}y}\,\mathbf{1}\_{y\geq 0}+(1-\zeta\_{s})\,\eta\_{s,2}\,e^{\eta\_{s,2}y}\,\mathbf{1}\_{y<0},\quad\zeta\_{s}\in[0,1],\quad\eta\_{s,1}>1,\quad\eta\_{s,2}>0. |  | (8.1) |

Between rebalancing times, and in the absence of active control, the stock index process {St}\{S\_{t}\} evolves according to the jump-diffusion dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt−=(μs−λs​κs)​d​t+σs​d​Zs​(t)+d​(∑i=1πs​(t)(ξs,i−1)),t∈[tm−1+,tm−],tm−1∈𝒯.\frac{dS\_{t}}{S\_{t^{-}}}=\left(\mu\_{s}-\lambda\_{s}\,\kappa\_{s}\right)dt+\sigma\_{s}\,dZ\_{s}(t)+d\left(\sum\_{i=1}^{\pi\_{s}(t)}(\xi\_{s,i}-1)\right),\quad t\in[t\_{m-1}^{+},\,t\_{m}^{-}],\quad t\_{m-1}\in\mathcal{T}. |  | (8.2) |

Here, μs\mu\_{s} and σs\sigma\_{s} are the (inflation-adjusted) drift and instantaneous volatility, respectively, and {Zs​(t)}t∈[0,T]\{Z\_{s}(t)\}\_{t\in[0,T]} is a standard Brownian motion. The process {πs​(t)}0≤t≤T\{\pi\_{s}(t)\}\_{0\leq t\leq T} is a Poisson process with a constant finite intensity rate λs>0\lambda\_{s}>0.
In ([8.2](https://arxiv.org/html/2602.16212v1#S8.E2 "In 8.1 Asset dynamics ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), the jump amplitudes {ξs,i}i=1∞\{\xi\_{s,i}\}\_{i=1}^{\infty} are
independent and identically distributed (i.i.d.) random variables having the same distribution as ξs\xi\_{s}; κs\kappa\_{s} is the compensated drift adjustment given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | κs=𝔼​[ξs−1]=ζs​ηs,1ηs,1−1+(1−ζs)​ηs,2ηs,2+1−1.\kappa\_{s}=\mathbb{E}[\xi\_{s}-1]=\frac{\zeta\_{s}\,\eta\_{s,1}}{\eta\_{s,1}-1}+\frac{(1-\zeta\_{s})\,\eta\_{s,2}}{\eta\_{s,2}+1}-1. |  | (8.3) |

The Brownian motion {Zs​(t)}t∈[0,T]\{Z\_{s}(t)\}\_{t\in[0,T]}, the Poisson process {πs​(t)}t∈[0,T]\{\pi\_{s}(t)\}\_{t\in[0,T]}, and the jump multipliers {ξs,i}\{\xi\_{s,i}\} are assumed to all be mutually independent.

Similarly, between rebalancing times, the bond index process {Bt}\{B\_{t}\} evolves according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​BtBt−=(μb−λb​κb+μbc​𝟏{Bt−<0})​d​t+σb​d​Zb​(t)+d​(∑i=1πb​(t)(ξb,i−1)),t∈[tm−1+,tm−],tm−1∈𝒯,\frac{dB\_{t}}{B\_{t^{-}}}=\big(\mu\_{b}-\lambda\_{b}\kappa\_{b}+\mu\_{b}^{c}\mathbf{1}\_{\{B\_{t^{-}}<0\}}\big)\,dt+\sigma\_{b}\,dZ\_{b}(t)+d\bigg(\sum\_{i=1}^{\pi\_{b}(t)}(\xi\_{b,i}-1)\bigg),\quad t\in[t\_{m-1}^{+},\,t\_{m}^{-}],\ t\_{m-1}\in\mathcal{T}, |  | (8.4) |

where the parameters in ([8.4](https://arxiv.org/html/2602.16212v1#S8.E4 "In 8.1 Asset dynamics ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) are defined similarly to those in ([8.2](https://arxiv.org/html/2602.16212v1#S8.E2 "In 8.1 Asset dynamics ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
In particular, {πb​(t)}0≤t≤T\{\pi\_{b}(t)\}\_{0\leq t\leq T} is a Poisson process with a positive, finite, constant jump intensity λb\lambda\_{b}. The jump amplitudes {ξb,i}i=1∞\{\xi\_{b,i}\}\_{i=1}^{\infty} are i.i.d. random variables, each distributed as ξb\xi\_{b}, where ln⁡(ξb)\ln(\xi\_{b}) follows an asymmetric double-exponential distribution with probability density function given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | φb​(y)=ζb​ηb,1​e−ηb,1​y​ 1y≥0+(1−ζb)​ηb,2​eηb,2​y​ 1y<0,ζb∈[0,1],ηb,1>1,ηb,2>0.\varphi\_{b}(y)=\zeta\_{b}\,\eta\_{b,1}\,e^{-\eta\_{b,1}y}\,\mathbf{1}\_{y\geq 0}+(1-\zeta\_{b})\,\eta\_{b,2}\,e^{\eta\_{b,2}y}\,\mathbf{1}\_{y<0},\quad\zeta\_{b}\in[0,1],~\eta\_{b,1}>1,~\eta\_{b,2}>0. |  | (8.5) |

In ([8.4](https://arxiv.org/html/2602.16212v1#S8.E4 "In 8.1 Asset dynamics ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), the term μbc​𝟏{Bt−<0}\mu\_{b}^{c}\mathbf{1}\_{\{B\_{t^{-}}<0\}}, the parameter μbc≥0\mu\_{b}^{c}\geq 0 represents the borrowing spread applied when the bond amount becomes negative.
The processes {Zb​(t)}t∈[0,T]\{Z\_{b}(t)\}\_{t\in[0,T]}, {πb​(t)}0≤t≤T\{\pi\_{b}(t)\}\_{0\leq t\leq T}, and the jump mutipliers {ξb,i}\{\xi\_{b,i}\} are assumed to all be mutually independent.

The diffusion components are correlated, d​Zs​(t)​d​Zb​(t)=ρs​b​d​tdZ\_{s}(t)\,dZ\_{b}(t)=\rho\_{sb}\,dt, while all jump processes and jump sizes are mutually independent; namely, the Poisson processes
{πs​(t)}\{\pi\_{s}(t)\}, {πb​(t)}\{\pi\_{b}(t)\} and the corresponding jump multipliers {ξs,i}\{\xi\_{s,i}\},
{ξb,i}\{\xi\_{b,i}\} are mutually independent, and independent of {Zs}\{Z\_{s}\} and {Zb}\{Z\_{b}\}.

### 8.2 Synthetic–market calibration

Following [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], the synthetic market is calibrated to monthly real
total–return series for the CRSP value–weighted equity index and the CRSP US 30–day
T–bill index over the period 1926:1–2020:12, with both series deflated by the US CPI.
In [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], the double–exponential jump–diffusion parameters
(μs,σs,λs,ζs,ηs,1,ηs,2)(\mu\_{s},\sigma\_{s},\lambda\_{s},\zeta\_{s},\eta\_{s,1},\eta\_{s,2}) for the stock index and
(μb,σb,λb,ζb,ηb,1,ηb,2)(\mu\_{b},\sigma\_{b},\lambda\_{b},\zeta\_{b},\eta\_{b,1},\eta\_{b,2}) for the bond index,
together with the diffusion correlation ρs​b\rho\_{sb}, are estimated using the
threshold–based jump filter described therein.
In our validation we do not re–estimate these parameters. Instead, we adopt the
annualized real parameter values reported in Table 1 of [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)],
which we reproduce in Table [8.1](https://arxiv.org/html/2602.16212v1#S8.T1 "Table 8.1 ‣ 8.2 Synthetic–market calibration ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

Table 8.1: Annualized real parameter values for the double–exponential jump–diffusion
model, taken from [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)]. The stock asset is the CRSP
value–weighted total return index; the bond asset is the 30–day US T–bill index,
both deflated by CPI.

| Stock (CRSP) | μs\mu\_{s} | σs\sigma\_{s} | λs\lambda\_{s} | ζs\zeta\_{s} | ηs,1\eta\_{s,1} | ηs,2\eta\_{s,2} | ρs​b\rho\_{sb} |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0.08912 | 0.1460 | 0.3263 | 0.2258 | 4.3625 | 5.5335 | 0.08420 |
| 30–day T–bill | μb\mu\_{b} | σb\sigma\_{b} | λb\lambda\_{b} | ζb\zeta\_{b} | ηb,1\eta\_{b,1} | ηb,2\eta\_{b,2} | ρs​b\rho\_{sb} |
|  | 0.00460 | 0.0130 | 0.5053 | 0.3958 | 65.801 | 57.793 | 0.08420 |

### 8.3 Retirement scenario

The base–case retirement scenario, which underlies the synthetic–market efficient frontiers used for validation, mirrors the specification in Section 11 and Table 3 of [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)]. All monetary quantities are expressed in thousands of real dollars. A concise summary is given in Table [8.2](https://arxiv.org/html/2602.16212v1#S8.T2 "Table 8.2 ‣ 8.3 Retirement scenario ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

Table 8.2: Base–case retirement scenario used for validation, matching the specification in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)]. Monetary units are thousands of real dollars.

|  |  |
| --- | --- |
| Item | Value |
| Retiree | 65–year–old Canadian male |
| Mortality table | CPM2014 (deterministic life table) |
| Investment horizon TT | 30 years |
| Equity index | Real CRSP capitalization–weighted total return index |
| Bond index | Real US 30–day T–bill index |
| Initial wealth W0W\_{0} | 1000 |
| Rebalancing / withdrawal times | t=0,1,…,29t=0,1,\ldots,29 (annual) |
| Minimum annual withdrawal qminq\_{\min} | 40 |
| Maximum annual withdrawal qmaxq\_{\max} | 80 |
| Equity fraction range | pm∈[0,1]p\_{m}\in[0,1] |
| Borrowing spread μbc\mu\_{b}^{c} | 0.02 |
| Tontine gain rate gmg\_{m} | as in Equation ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) |
| Group gain Γm\Gamma\_{m} | 1.0 (as discussed in Subsection [2.1.3](https://arxiv.org/html/2602.16212v1#S2.SS1.SSS3 "2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) |
| Tontine fee ϱ\varrho | 1−e−0.005≈0.004991-e^{-0.005}\approx 0.00499 (49.9 bps/year)888Forsyth et al. [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)] model the tontine fee as a continuously charged rate Tf=0.5%T\_{f}=0.5\% per annum, which enters the wealth recursion through a factor exp⁡(−Tf​Δ​t)\exp(-T\_{f}\Delta t) each year; see, for example, Equations (5.3)–(5.6) in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)]. In this paper, to align with industry practice, we instead deduct a single proportional yearly fee ϱ\varrho at each decision time. We choose ϱ\varrho such that (1−ϱ)=e−Tf(1-\varrho)=e^{-T\_{f}} (with Δ​t=1\Delta t=1), i.e. ϱ=1−e−0.005\varrho=1-e^{-0.005}, so that the effective annual charge matches TfT\_{f}. |
| Risk tail level α\alpha | 0.05 |
| Stabilization parameter ε\varepsilon | −10−4-10^{-4} |
| Market parameters | as in Table [8.1](https://arxiv.org/html/2602.16212v1#S8.T1 "Table 8.1 ‣ 8.2 Synthetic–market calibration ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") |

In this setting, the investor controls annual withdrawals qt∈[qmin,qmax]q\_{t}\in[q\_{\min},q\_{\max}] and the equity fraction pt∈[0,1]p\_{t}\in[0,1]. Wealth can become negative if required withdrawals exceed available funds, in which case the portfolio is liquidated and subsequent withdrawals are financed as debt growing at the bond rate plus the borrowing spread μbc\mu\_{b}^{c}. Mortality enters only through the deterministic life-table probabilities {δm−1}\{\delta\_{m-1}\} from CPM2014, so that all synthetic–market paths share the same mortality profile (Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

The risk–reward trade–off is quantified using expected total withdrawals (EW) and the expected shortfall (ES) at the 5%5\% level of terminal wealth WTW\_{T}, as in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)].

### 8.4 Validation results

We validate our NN implementation by reproducing the synthetic–market
EW–CVaR efficient frontiers reported in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], both with and without a tontine overlay.
Figure [8.1](https://arxiv.org/html/2602.16212v1#S8.F1 "Figure 8.1 ‣ 8.4 Validation results ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") compares the reference frontiers (computed using the PDE-based control method in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)])
with the NN frontiers obtained from our training procedure, together with the constant-withdrawal/constant-allocation benchmark.
Overall, the NN approach yields EW–CVaR efficient frontiers in close agreement with the PDE-based reference and preserves its qualitative 1structure.

As shown in Figure [8.1](https://arxiv.org/html/2602.16212v1#S8.F1 "Figure 8.1 ‣ 8.4 Validation results ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), the NN frontiers closely track the PDE-based reference curves across the range of scalarization parameters γ\gamma used to trace the trade-off. Consistent with the figure, unreported summary errors confirm close agreement in both the annualized expected withdrawal E​[∑mqm]/TE[\sum\_{m}q\_{m}]/T and the corresponding CVaR0.05\mathrm{CVaR}\_{0.05} values along the frontier. The quality of the approximation is similar in the no-tontine case.

Beyond pointwise agreement, the NN frontiers preserve the expected qualitative behavior in γ\gamma: as risk aversion increases, the annualized expected withdrawal decreases and CVaR0.05\mathrm{CVaR}\_{0.05} moves in the corresponding direction.
In particular, the region of the frontier most relevant in practice is nearly indistinguishable from the PDE-based reference in Figure [8.1](https://arxiv.org/html/2602.16212v1#S8.F1 "Figure 8.1 ‣ 8.4 Validation results ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

![[Uncaptioned image]](figs/validation_frontier_update_new.png)

Figure 8.1: Validation of the EW–CVaR efficient frontiers in the
synthetic market. Reference frontiers with and without a tontine overlay,
labelled respectively as “No Tontine (PDE Control)” and
“Tontine (PDE Control)”,
are compared with the corresponding
NN frontiers, together with the constant
withdrawal/constant allocation benchmark. Units: thousands of dollars.

## 9 Internationally diversified portfolios

### 9.1 Asset return data and preprocessing

For the internationally diversified experiments, we take the perspective of a domestic (Australian) investor and work with four indices: Australian equities and government bonds (domestic), and U.S. equities and government bonds (foreign) converted into AUD. All returns are expressed in real (inflation–adjusted) AUD at a monthly frequency.

Our empirical sample runs from 1935:1 to 2022:12. Where necessary, individual series are backcast and truncated so that all four indices and the Australian CPI are jointly available over a common horizon. This long historical panel is used both to describe the “historical market” and as input to the bootstrap simulations described below and in Section [6](https://arxiv.org/html/2602.16212v1#S6 "6 Neural network formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

##### Domestic equity.

As a proxy for the Australian equity market, we construct a capitalization–weighted total return series for the All Ordinaries index. Monthly price levels are taken from the Bloomberg All Ordinaries Price Index (AS30) and combined with trailing dividend yield data from [[35](https://arxiv.org/html/2602.16212v1#bib.bib35)] and the Reserve Bank of Australia (RBA) to impute reinvested dividends prior to the start of the Bloomberg All Ordinaries Accumulation Index (XAOA) in 1999. From 1999 onward, the constructed series is aligned to XAOA, so that the resulting index is a consistent long–horizon Australian equity total return series.

##### Domestic bonds.

The domestic bond asset is represented by a 10–year Commonwealth Government bond total return index constructed from two sources. From December 1935 to December 2011 we use the annual Australian government bond total return series of [[27](https://arxiv.org/html/2602.16212v1#bib.bib27)], which is based on micro–level Commonwealth bond data targeting a 10–year maturity [[9](https://arxiv.org/html/2602.16212v1#bib.bib9)]. We convert this annual total return index to monthly frequency by interpolating the level of the total return index and then computing month–on–month returns. From May 2011 onward we splice in the S&P/ASX Australian Government Bond 7–10 Year Total Return Index (Bloomberg), available at a monthly frequency, to obtain a single long–horizon nominal total return bond index for the Australian market.

##### U.S. equity and bonds.

For the U.S. market, we start from the same CRSP nominal total return series as in Subsection [8.2](https://arxiv.org/html/2602.16212v1#S8.SS2 "8.2 Synthetic–market calibration ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), namely the value–weighted equity index and the 30–day Treasury bill (T–bill) index, both in USD. These nominal USD returns are first converted into AUD using the end–of–month AUD/USD exchange rate, constructed from Federal Reserve Banking and Monetary Statistics archives (January 1935–December 1968) and the RBA historical exchange rate series thereafter, spliced to form a continuous monthly AUD/USD series, and are then placed on the same real AUD basis as the domestic assets via CPI deflation (see below).

##### Inflation and real returns.

Inflation is measured by the Australian Consumer Price Index published by the RBA. The CPI series is obtained entirely from the RBA: from September 2017 onward it is available monthly, while before that date it is published quarterly. We treat the quarterly CPI as the benchmark series and linearly interpolate it to monthly frequency to match the financial data. For each asset we form a nominal total return index, convert U.S. series to AUD where appropriate, and then obtain real returns by deflating with the interpolated Australian CPI. In this way all four assets are expressed in real AUD terms, consistent with the objective of funding real retirement spending for an Australian investor.

##### Historical market and bootstrap sampling.

Future index paths in the internationally diversified experiments are generated nonparametrically using the stationary block bootstrap [[45](https://arxiv.org/html/2602.16212v1#bib.bib45), [46](https://arxiv.org/html/2602.16212v1#bib.bib46), [41](https://arxiv.org/html/2602.16212v1#bib.bib41), [13](https://arxiv.org/html/2602.16212v1#bib.bib13)]. We apply geometrically distributed block lengths and sample blocks of four–asset returns jointly to preserve both cross–sectional correlations and serial dependence. The expected block length is chosen following the data–driven procedure of [[41](https://arxiv.org/html/2602.16212v1#bib.bib41)] applied to each series, and then harmonised across assets to obtain a common effective block size of the order of a few years. All bootstrap sampling is carried out on the preprocessed monthly real AUD return series described above.

##### Return characteristics and dependence structure.

Tables [9.1](https://arxiv.org/html/2602.16212v1#S9.T1 "Table 9.1 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") and [9.2](https://arxiv.org/html/2602.16212v1#S9.T2 "Table 9.2 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")
summarize the preprocessed monthly real AUD returns
across all four assets.

Table 9.1: Summary statistics of monthly real returns (1935:1–2022:12): annualized mean,
annualized geometric mean, and annualized volatility. VaR0.05\mathrm{VaR}\_{0.05} (m) and CVaR0.05\mathrm{CVaR}\_{0.05} (m) report the 5%5\% Value-at-Risk and CVaR of monthly returns.

| Asset | Mean (ann.) | Geo. mean (ann.) | Vol (ann.) | VaR0.05\mathrm{VaR}\_{0.05} (m) | CVaR0.05\mathrm{CVaR}\_{0.05} (m) |
| --- | --- | --- | --- | --- | --- |
| U.S. 30–day T–bill | 0.003 | -0.001 | 0.095 | -0.041 | -0.056 |
| U.S. equity index | 0.082 | 0.071 | 0.165 | -0.064 | -0.096 |
| AU 10–year bond | 0.012 | 0.012 | 0.036 | -0.015 | -0.025 |
| AU equity index | 0.069 | 0.059 | 0.151 | -0.065 | -0.100 |




Table 9.2: Correlation matrix of monthly real returns (1935:1–2022:12).

|  | U.S. 30-day T–bill | U.S. equity | AU 10-year bond | AU equity |
| --- | --- | --- | --- | --- |
| U.S. 30-day T–bill | 1.00 | 0.34 | 0.17 | -0.22 |
| U.S. equity | 0.34 | 1.00 | 0.10 | 0.33 |
| AU 10-year bond | 0.17 | 0.10 | 1.00 | 0.11 |
| AU equity | -0.22 | 0.33 | 0.11 | 1.00 |

As indicated in Tables [9.1](https://arxiv.org/html/2602.16212v1#S9.T1 "Table 9.1 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")–[9.2](https://arxiv.org/html/2602.16212v1#S9.T2 "Table 9.2 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), U.S. equity has the highest
historical average real return in this sample and is
only weakly correlated with Australian equity (correlation ≈0.33\approx 0.33, well below 1)999Over 1990:1–2022:12, the correlation
is 0.48 (vs 0.33 in the full sample), indicating higher dependence in the recent period.. This comparatively low cross-country equity correlation suggests
meaningful scope for international diversification, even among developed equity markets, a point we revisit later.
By contrast, once expressed in real AUD, the U.S. 30–day T–bill has a near–zero average real return and substantial volatility inherited from exchange–rate fluctuations, making short–maturity foreign fixed income a less attractive defensive asset than domestic government bonds. These empirical patterns are revisited when interpreting the optimal controls below.

### 9.2 Mortality assumptions

In the internationally diversified experiments, we model the lifetime of a
65–year–old Australian male and consider both deterministic and stochastic
mortality, consistent with the general framework in
Subsection [2.2](https://arxiv.org/html/2602.16212v1#S2.SS2 "2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") and Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

For the deterministic specification, we use the most recent available
single–year Australian male period life table (mltper\_1x1.txt) from the Human Mortality Database (HMD, [[25](https://arxiv.org/html/2602.16212v1#bib.bib25)]), specifically the 1x1 Australian male life table covering calendar years 1921–2021.101010Available at
<https://www.mortality.org/File/GetDocument/hmd.v6/AUS/STATS/mltper_1x1.txt>.
This table provides annual one–year death probabilities qx,tq\_{x,t} over age
and calendar year. Fixing the retirement age x0x\_{0} and retirement date t0t\_{0},
and taking annual decision times tm=t0+mt\_{m}=t\_{0}+m, the corresponding
conditional death probabilities {δm−1}m=1M\{\delta\_{m-1}\}\_{m=1}^{M} are defined exactly
as in equation ([2.12](https://arxiv.org/html/2602.16212v1#S2.E12 "In 2.2.1 Deterministic mortality ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). In a homogeneous pool we set
δm−1j≡δm−1\delta\_{m-1}^{j}\equiv\delta\_{m-1} for all members jj, and the associated
tontine gain rates gmg\_{m} entering the wealth recursion follow from
equation ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

For stochastic mortality, we work with the same HMD source but use the raw deaths and exposures required for model calibration. Specifically, we extract annual Australian male deaths Dx,tD\_{x,t} and central exposures-to-risk Ex,tcE^{c}\_{x,t} for ages 5555–9595 and calendar years 19871987–20212021 from the HMD tables Deaths\_1x1.txt and Exposures\_1x1.txt.111111Available at
<https://www.mortality.org/File/GetDocument/hmd.v6/AUS/STATS/Deaths_1x1.txt>
and
<https://www.mortality.org/File/GetDocument/hmd.v6/AUS/STATS/Exposures_1x1.txt>
.
When modelling one–year death probabilities qx,tq\_{x,t} (rather than central death rates), we follow [[62](https://arxiv.org/html/2602.16212v1#bib.bib62)] and approximate initial exposures by Ex,t0≈Ex,tc+0.5​Dx,tE^{0}\_{x,t}\approx E^{c}\_{x,t}+0.5\,D\_{x,t}, and then construct the corresponding empirical one–year death probabilities as qx,t:=Dx,t/Ex,t0q\_{x,t}:=D\_{x,t}/E^{0}\_{x,t}.
These historical mortality series are used to calibrate a single–population model
from the generalized age–period–cohort (GAPC) family (such as LC or
CBD models), following Subsection [2.2](https://arxiv.org/html/2602.16212v1#S2.SS2 "2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").
Calibration and forecasting are implemented in R using the
StMoMo package [[62](https://arxiv.org/html/2602.16212v1#bib.bib62)], which casts these
specifications in the GAPC framework. Model–specific identifiability
constraints are those standard in StMoMo; for brevity we do not
reproduce them here, and instead refer the reader to [[62](https://arxiv.org/html/2602.16212v1#bib.bib62)]
for details.

On each simulated path kk, the associated sequence of one–year conditional
death probabilities {δm−1(k)}m=1M\{\delta\_{m-1}^{(k)}\}\_{m=1}^{M} is defined as in ([2.20](https://arxiv.org/html/2602.16212v1#S2.E20 "In Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), and the corresponding pathwise tontine gain
rates gm(k)g\_{m}^{(k)} are obtained via ([2.11](https://arxiv.org/html/2602.16212v1#S2.E11 "In 2.1.3 Large-pool approximation ‣ 2.1 Modeling of individual tontine accounts ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).
As summarized in Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), these sequences
{δm−1(k)}\{\delta\_{m-1}^{(k)}\} (and hence {gm(k)}\{g\_{m}^{(k)}\}) are used
throughout our numerical experiments: they drive mortality credits in the NN
training and efficient–frontier computation, and determine death times and
MBG payouts in the pricing overlay (also see Remark [7.2](https://arxiv.org/html/2602.16212v1#S7.Thmremark2 "Remark 7.2. ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

### 9.3 Experimental setup and scenarios

For the internationally diversified experiments, we retain the same decumulation framework used in the benchmark validation (Table [8.2](https://arxiv.org/html/2602.16212v1#S8.T2 "Table 8.2 ‣ 8.3 Retirement scenario ‣ 8 Benchmark validation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), but now from the perspective of a 65–year–old Australian male retiree investing in the four indices described in Subsection [9.1](https://arxiv.org/html/2602.16212v1#S9.SS1 "9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"). All monetary quantities are interpreted as thousands of real Australian dollars, and the mortality assumptions follow Subsection [9.2](https://arxiv.org/html/2602.16212v1#S9.SS2 "9.2 Mortality assumptions ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

More specifically, the retiree starts at time t0=0t\_{0}=0 with initial wealth W0=1000W\_{0}=1000, corresponding to an initial purchase price L0=1000L\_{0}=1000 for the
tontine product with the embedded MBG overlay described in Section [3](https://arxiv.org/html/2602.16212v1#S3 "3 Money-back guarantee overlay ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").
The planning horizon is T=30T=30 years with annual decision times tm=mt\_{m}=m, m=0,…,Mm=0,\ldots,M, where M=30M=30.
The minimum and maximum annual withdrawals are fixed at qmin=40q\_{\min}=40 and qmax=80q\_{\max}=80. In addition, we also enforce the no–shorting and no–leverage constraints
as in Section [4](https://arxiv.org/html/2602.16212v1#S4 "4 Stochastic control framework ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"). In these experiments, following QSuper’s Lifetime Pension PDS [[49](https://arxiv.org/html/2602.16212v1#bib.bib49)], we use an annual tontine fee of ϱ=0.11%\varrho=0.11\% (11 bps).

Risk and reward are measured by the same EW–CVaR criterion as in Section [5](https://arxiv.org/html/2602.16212v1#S5 "5 EW–CVaR portfolio formulation ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"):
expected total real withdrawals over [0,T][0,T] and CVaRα\mathrm{CVaR}\_{\alpha} of terminal wealth WTW\_{T} at level α=0.05\alpha=0.05.
For a given scalarization parameter γ>0\gamma>0, we first train neural networks to approximate the optimal control 𝒰0∗​(γ)\mathcal{U}\_{0}^{\*}(\gamma) and
compute the corresponding point on the EW–CVaR efficient frontier
under either deterministic table mortality or stochastic GAPC–based mortality. The MBG overlay is then priced ex post, holding 𝒰0∗​(γ)\mathcal{U}\_{0}^{\*}(\gamma) fixed, using the actuarial pricing rule ([7.2](https://arxiv.org/html/2602.16212v1#S7.E2 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) and the simulation procedure in Section [7](https://arxiv.org/html/2602.16212v1#S7 "7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

### 9.4 EW–CVaR efficient frontiers (deterministic mortality)

We now discuss the EW–CVaR efficient frontiers for both cases:
two–asset (domestic–only) and four–asset (internationally diversified).

As in [[21](https://arxiv.org/html/2602.16212v1#bib.bib21)], we include a constant–withdrawal, constant–allocation
benchmark as a reference point on the EW–CVaR frontiers.
In line with the 4% rule of [[4](https://arxiv.org/html/2602.16212v1#bib.bib4)],
the benchmark always
withdraws 4040 (thousand real dollars) per year and maintains fixed portfolio
weights over time. For each case,
we select the benchmark by grid search over asset weights in 10% increments,
choosing the allocation that minimizes the ES (equivalently, maximizes
CVaR0.05\mathrm{CVaR}\_{0.05}) of terminal wealth.

In the two–asset case, the search is over equity fractions
psd∈{0,0.1,…,1}p^{{\scalebox{0.7}{$d$}}}\_{s}\in\{0,0.1,\ldots,1\} with pbd=1−psdp^{{\scalebox{0.7}{$d$}}}\_{b}=1-p^{{\scalebox{0.7}{$d$}}}\_{s}; the best
constant–weight benchmark has a 50% domestic equity allocation and
ES≈−617.1\mathrm{ES}\approx-617.1. In the four–asset case, we
search over all weight vectors on the 10% grid whose components sum to one; the
best benchmark has allocation
(psd,pbd,psf,pbf)=(0.1,0.3,0.2,0.4)(p^{{\scalebox{0.7}{$d$}}}\_{s},p^{{\scalebox{0.7}{$d$}}}\_{b},p^{{\scalebox{0.7}{$f$}}}\_{s},p^{{\scalebox{0.7}{$f$}}}\_{b})=(0.1,0.3,0.2,0.4) with
ES≈−446.1\mathrm{ES}\approx-446.1. These two constant–strategy benchmarks appear as single
points in the efficient–frontier figures for the two–asset and
four–asset experiments, respectively.

![[Uncaptioned image]](figs/2_and_4_asset_EF_deter_mortality_revised_new.png)

  


Figure 9.1: EW–CVaR efficient frontiers for domestic–only (two–asset) and
internationally diversified (four–asset) portfolios, with and without a
tontine overlay. Constant–weight benchmarks are shown as single points.
Units: thousands of real AUD.

Figure [9.1](https://arxiv.org/html/2602.16212v1#S9.F1 "Figure 9.1 ‣ 9.4 EW–CVaR efficient frontiers (deterministic mortality) ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") shows the EW–CVaR efficient frontiers
obtained by NNs with and without a tontine overlay in the
two–asset (domestic–only) and four–asset (internationally diversified) cases,
together with the corresponding constant–weight benchmarks.

We make the following key observations about Figure [9.1](https://arxiv.org/html/2602.16212v1#S9.F1 "Figure 9.1 ‣ 9.4 EW–CVaR efficient frontiers (deterministic mortality) ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"):

* •

  The internationally diversified (four–asset) constant–weight benchmark point lies
  essentially on the two–asset no–tontine frontier.
  Thus, at the 4%–rule withdrawal level, a simple buy–and–hold internationally
  diversified allocation can achieve an EW–CVaR trade–off comparable to that delivered
  by the domestic–only EW–CVaR optimal strategy without a tontine overlay.
  This highlights the strength of international diversification even before adding
  longevity pooling.
* •

  In both the domestic–only and internationally diversified settings,
  the efficient frontiers obtained from our optimization lie well above and to
  the right of their corresponding constant–weight benchmark points.
  This confirms that “4%-rule–style” strategies with fixed withdrawals
  and static allocations are substantially less efficient than the optimal
  dynamic policies obtained from our EW–CVaR optimization.
  For example, even at CVaR0.05​(WT)≈500\mathrm{CVaR}\_{0.05}(W\_{T})\approx 500 (thousand real AUD) at age 95, a very conservative level of terminal-wealth downside protection, the four–asset tontine frontier supports expected annual withdrawals of about 7070 (thousand real AUD), i.e. roughly 7%7\% of initial wealth, compared with the fixed 4040 (thousand, 4%4\%) withdrawal implied by the 4% rule benchmark.
* •

  Comparing the two “no tontine” curves, the four–asset frontier is generally shifted
  upwards and to the right relative to the two–asset frontier over the
  practically relevant range of CVaR0.05\mathrm{CVaR}\_{0.05}.
  Allowing the retiree to invest in both Australian and U.S. assets therefore supports higher annualized withdrawals
  for a similar, or even improved, level of downside risk compared with a purely
  domestic portfolio.

  This is consistent with Tables [9.1](https://arxiv.org/html/2602.16212v1#S9.T1 "Table 9.1 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")–[9.2](https://arxiv.org/html/2602.16212v1#S9.T2 "Table 9.2 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"):
  in this sample, U.S. equity has a higher average real return than Australian equity,
  and the cross–country equity correlation is well below one, so adding foreign equity provides potential to improve the EW–CVaR trade–off even when used selectively rather than through uniformly higher equity exposure.
* •

  For both asset settings, the tontine frontier dominates the corresponding no–tontine frontier, with especially pronounced gains in the four–asset case: over a wide range of scalarization parameters γ\gamma, the four–asset tontine strategies deliver both higher expected annual withdrawals and a much less adverse 5%5\% tail of WTW\_{T} than the corresponding four–asset no–tontine strategies, illustrating the substantial combined benefit of international diversification and longevity pooling under optimal dynamic controls.

In the next subsection, we examine how these frontiers shift when mortality is modelled stochastically.

### 9.5 Effect of stochastic mortality on EW–CVaR frontiers

We now examine how introducing stochastic mortality affects the EW–CVaR efficient frontier in the four–asset tontine setting. Throughout this subsection we keep the assets, fee structure, control constraints, and scalarization setup identical to Subsection [9.4](https://arxiv.org/html/2602.16212v1#S9.SS4 "9.4 EW–CVaR efficient frontiers (deterministic mortality) ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"); only the mortality specification changes.

![[Uncaptioned image]](figs/frontier_SM_2_revised_new.png)



Figure 9.2: EW–CVaR efficient frontiers for the four–asset tontine portfolio under deterministic table mortality and stochastic mortality (LC and CBD models). Units: thousands of real AUD.

Figure [9.2](https://arxiv.org/html/2602.16212v1#S9.F2 "Figure 9.2 ‣ 9.5 Effect of stochastic mortality on EW–CVaR frontiers ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") compares the EW–CVaR efficient frontiers for the four–asset tontine portfolio under three mortality specifications:
(i) deterministic table mortality as in Subsection [9.2](https://arxiv.org/html/2602.16212v1#S9.SS2 "9.2 Mortality assumptions ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"),
(ii) stochastic LC mortality, and
(iii) stochastic CBD mortality.
In all cases we retain the “plan to live” convention: the retiree is assumed to survive to the end of the horizon, so mortality only affects the size of mortality credits through the one–year death probabilities (cf. Remark [2.1](https://arxiv.org/html/2602.16212v1#S2.Thmremark1 "Remark 2.1 (Mortality inputs in simulation). ‣ From stochastic mortality models to tontine gain rate. ‣ Cairns–Blake–Dowd (CBD) model ‣ 2.2 Mortality models ‣ 2 Tontine modeling ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), not the termination time of a path.

A key point for interpretation is that the horizon corresponds to very advanced age (age 95 in the baseline calibration with a 30–year horizon). Consequently, extremely large tail targets for terminal wealth—for example, CVaR0.05​(WT)≈1000\mathrm{CVaR}\_{0.05}(W\_{T})\approx 1000 (thousand real AUD)—are arguably overly conservative, since they imply substantial residual wealth at age 95. In many practical settings, values around CVaR0.05​(WT)≈500\mathrm{CVaR}\_{0.05}(W\_{T})\approx 500 already represent a sizeable buffer that could fund minimum spending well beyond the model horizon. Therefore, the most decision-relevant part of Figure [9.2](https://arxiv.org/html/2602.16212v1#S9.F2 "Figure 9.2 ‣ 9.5 Effect of stochastic mortality on EW–CVaR frontiers ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") is the region to the left of (or up to) roughly CVaR0.05​(WT)=500\mathrm{CVaR}\_{0.05}(W\_{T})=500, where the controls correspond to higher withdrawals rather than preserving large terminal balances.

Over this economically relevant region, the impact of stochastic mortality is visible but modest: the stochastic frontiers track the deterministic table frontier closely, with only a relatively small leftward shift. This shift is consistent with systematic longevity improvement in the stochastic models: when death probabilities fall relative to the baseline table, survivors receive smaller mortality credits, which lowers terminal wealth in the adverse outcomes that drive CVaR0.05​(WT)\mathrm{CVaR}\_{0.05}(W\_{T}).
While systematic longevity risk does erode the benefits of the tontine overlay to some extent, the four–asset tontine portfolio under stochastic mortality still offers an attractive combination of high expected withdrawals and improved CVaR0.05​(WT)\mathrm{CVaR}\_{0.05}(W\_{T}) relative to the domestic–only and constant–weight strategies discussed in
Subsection [9.4](https://arxiv.org/html/2602.16212v1#S9.SS4 "9.4 EW–CVaR efficient frontiers (deterministic mortality) ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (Figure [9.1](https://arxiv.org/html/2602.16212v1#S9.F1 "Figure 9.1 ‣ 9.4 EW–CVaR efficient frontiers (deterministic mortality) ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

A further observaton is that the LC and CBD frontiers are close to each other, with the CBD curve typically lying slightly further to the left. Conditional on modelling systematic longevity risk, the specific choice between LC and CBD therefore has only a relatively minor effect on the EW–CVaR trade–off.

### 9.6 Optimal control heatmaps

To illustrate the structure of the learned policies, Figure [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")
plots the optimal rebalancing controls for the four–asset tontine with stochastic
mortality (LC model) and a representative scalarization parameter
γ=1.5\gamma=1.5. Each panel shows, as a function of time and real wealth, the
fraction of wealth invested in one of the four indices described in
Subsection [9.1](https://arxiv.org/html/2602.16212v1#S9.SS1 "9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), together with the 5th, 50th, and 95th percentiles of the
wealth distribution under the optimal policy. Control heatmaps under deterministic table mortality and the CBD mortality model are qualitatively very similar and are therefore omitted for brevity.

![Refer to caption](x1.png)


(a) Australian equity index (domestic)

![Refer to caption](x2.png)


(b) U.S. equity index

![Refer to caption](x3.png)


(c) Australian 10–year government bond index (domestic)

![Refer to caption](x4.png)


(d) U.S. 30–day T–bill index

Figure 9.3: Optimal rebalancing controls under the four–asset tontine with stochastic
mortality (LC model) for a representative scalarization parameter γ=1.5\gamma=1.5.
Colours show the fraction of wealth invested in each asset as a function of time
and real wealth. Units: thousands of real AUD.

#### 9.6.1 General comments about Figure [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")

We make several qualitative observations from Figure [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"):

* •

  Along the median and upper wealth trajectories, the strategy exhibits a clear
  tilt towards domestic assets: a substantial fraction of wealth is invested in
  Australian securities, with the Australian 10–year government bond
  (Figure [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (c)) acting as the main stabilising asset. Specifically, for moderate
  to high wealth levels, the allocation to the domestic bond is large (typically
  well above 50%), while the U.S. 30–day T–bill (Figure [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (d)) is used only
  marginally.
  This aligns with Table [9.1](https://arxiv.org/html/2602.16212v1#S9.T1 "Table 9.1 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"): the domestic bond index has
  substantially lower volatility and markedly milder 5% monthly tail losses
  (VaR/CVaR) than the U.S. T–bill once returns are expressed in real AUD, supporting
  its role as the primary defensive allocation in the optimal policy.

  Along the 95th–percentile path the equity allocations
  (Figures [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (a) and (b)) are gradually reduced, so that the portfolio becomes
  dominated by the Australian bond index, effectively locking in favourable
  outcomes; any remaining equity risk is taken primarily via the domestic
  market.
* •

  The U.S. equity allocation (Figure [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (b)) is highly state dependent. When wealth
  falls into the lower region of the state space, particularly along and below
  the 5th–percentile path, the policy tilts aggressively toward U.S. equities,
  with weights close to 100%100\% in that asset and very low exposure to domestic
  bonds. This behaviour is concentrated in the extreme low-wealth tail and can be interpreted as a low-probability, last-resort catch-up position, rather than a typical allocation across the state space. When wealth is low, the optimal EW–CVaR policy favours taking additional growth risk in order to improve the expected withdrawal profile, using foreign equity as the primary “catch–up” instrument.

  Tables [9.1](https://arxiv.org/html/2602.16212v1#S9.T1 "Table 9.1 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")–[9.2](https://arxiv.org/html/2602.16212v1#S9.T2 "Table 9.2 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") provide a simple empirical rationale:
  U.S. equity combines the highest historical average real return in the sample with only
  moderate correlation to Australian equity, so it offers both growth upside and diversification
  potential when deployed as a state–dependent catch–up instrument in low–wealth regions.
  This is consistent with related optimal–decumulation evidence that moderate caps on the equity share have little effect on the efficient frontier, with the main control differences concentrated in extreme low–wealth tail states [[20](https://arxiv.org/html/2602.16212v1#bib.bib20)].
* •

  Comparing Figures [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (a) and (b) shows that Australian and U.S. equities play
  different roles. At moderate wealth, the strategy holds a sizeable but
  balanced allocation to Australian equities, while U.S. equity exposure is
  more concentrated in low–wealth regions of the state space. This suggests
  that the optimal policy uses domestic equity as the core growth asset and
  foreign equity as a more opportunistic, high–return lever when the retiree is
  underfunded.

#### 9.6.2 Role of equities in international diversification

To highlight how international diversification is used in the optimal policy, we
compare the four–asset heatmaps in
Figure [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") with the two–asset (domestic–only) counterpart in Figure [9.4](https://arxiv.org/html/2602.16212v1#S9.F4.3 "Figure 9.4 ‣ 9.6.2 Role of equities in international diversification ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

In the domestic–only case (Figure [9.4](https://arxiv.org/html/2602.16212v1#S9.F4.3 "Figure 9.4 ‣ 9.6.2 Role of equities in international diversification ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), the equity fraction
is primarily wealth–dependent rather than strongly time–dependent. Along the
median trajectory the policy remains in a moderate equity region for most of the
horizon (roughly in the 25%25\%–45%45\% range, corresponding to the teal/green colours),
rather than shifting toward near–zero equity late in the horizon. By contrast,
when wealth moves into the low–wealth region near and below the 5th–percentile path,
the heatmap turns red and the policy allocates close to 100%100\% to equities, using
the only available growth asset to improve the expected withdrawal profile when
wealth is small.

![Refer to caption](x5.png)

  


Figure 9.4: Optimal fraction in domestic equities in the two–asset (domestic–only) tontine with stochastic mortality (LC model) for a representative point on the efficient frontier (γ=1.5\gamma=1.5).
Colours show the fraction of wealth invested
in domestic equities as a function of time and real wealth. Units: thousands of real AUD.

In the four–asset case (Figures [9.3](https://arxiv.org/html/2602.16212v1#S9.F3 "Figure 9.3 ‣ 9.6 Optimal control heatmaps ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (a) and (b)), this role is split between Australian and U.S. equities. Domestic equity behaves much like the two–asset equity in relatively well–funded states, forming part of a growth core together with the Australian bond index. However, in low–wealth regions the allocation to U.S. equity becomes predominant, while domestic equity and bond exposures are reduced.

This comparison makes clear that the four–asset improvement in
Figure [9.1](https://arxiv.org/html/2602.16212v1#S9.F1 "Figure 9.1 ‣ 9.4 EW–CVaR efficient frontiers (deterministic mortality) ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") is driven by *how* equity risk is used,
rather than by a uniformly higher equity allocation across all wealth levels.
With only domestic assets, Australian equities must serve both as the core growth
exposure and as the only available “catch–up” lever when wealth is low.
Once U.S. equity is available, the optimal policy can separate these roles:
in better–funded regions it maintains a more balanced, largely domestic mix,
whereas in underfunded regions it shifts predominantly into U.S. equity to seek
additional growth and support the expected withdrawal objective.
In this sense, international diversification adds a second equity “catch–up”
instrument that is activated mainly when the retiree is underfunded, instead of
increasing equity exposure uniformly.

This interpretation is consistent with the return evidence in
Tables [9.1](https://arxiv.org/html/2602.16212v1#S9.T1 "Table 9.1 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")–[9.2](https://arxiv.org/html/2602.16212v1#S9.T2 "Table 9.2 ‣ Return characteristics and dependence structure. ‣ 9.1 Asset return data and preprocessing ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"), which shows that U.S. equity offers slightly higher average real returns than domestic equity and only moderate correlation with Australian equity over the sample period.

### 9.7 MBG pricing results

We now report simulation–based MBG pricing results using the actuarial pricing
formula ([7.2](https://arxiv.org/html/2602.16212v1#S7.E2 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) and the Monte Carlo procedure in
Algorithm [7.1](https://arxiv.org/html/2602.16212v1#S7.alg1 "Algorithm 7.1 ‣ 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"). In all cases, the MBG is priced *ex post*
under the fixed EW–CVaR optimal control as discussed in the previous
subsections. We report Monte Carlo estimates of 𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}] and
CVaR^αg​(Zg)\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g}), and the implied equivalent
up–front load factor f^g\widehat{f}\_{g} computed as in ([7.5](https://arxiv.org/html/2602.16212v1#S7.E5 "In 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

For interpretability, f^g\widehat{f}\_{g} can be read as an equivalent one–time
deduction f^g​L0\widehat{f}\_{g}L\_{0} from the initial purchase price (equivalently, as a
reduction in a notional starting payment rate); see Remark [7.1](https://arxiv.org/html/2602.16212v1#S7.Thmremark1 "Remark 7.1 (Interpreting 𝑓_𝑔 in starting–rate terms). ‣ 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

#### 9.7.1 Base–case MBG load

Table [9.3](https://arxiv.org/html/2602.16212v1#S9.T3 "Table 9.3 ‣ 9.7.1 Base–case MBG load ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") reports MBG pricing results under a
base–case parameter set: scalarization parameter γ=1.5\gamma=1.5 (as used in the
heatmap illustrations), L0=1000L\_{0}=1000 (thousand real AUD), pricing confidence level
αg=5%\alpha\_{g}=5\%, and prudential–buffer coefficient λ=0.5\lambda=0.5.
We apply this same parameter set to four settings—two–asset (domestic–only)
versus four–asset (internationally diversified), each under deterministic table
mortality and stochastic LC mortality. We also report the implied post–load
notional starting payment rate (1−f^g)​β0(1-\widehat{f}\_{g})\beta\_{0} for the reference value
β0=0.05\beta\_{0}=0.05.

| Setting | 𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}] | CVaR^0.05​(Zg)\widehat{\mathrm{CVaR}}\_{0.05}(Z\_{g}) | f^g\widehat{f}\_{g} | (1−f^g)​β0(1-\widehat{f}\_{g})\beta\_{0} |
| --- | --- | --- | --- | --- |
| 2 assets, table mortality | 65.63 | 736.61 | 0.43 | 2.85% |
| 2 assets, LC mortality | 66.67 | 755.47 | 0.44 | 2.80% |
| 4 assets, table mortality | 69.32 | 736.82 | 0.44 | 2.80% |
| 4 assets, LC mortality | 70.69 | 758.28 | 0.45 | 2.75% |

Table 9.3: Base–case parameter set for MBG pricing under EW–CVaR optimal controls:
γ=1.5\gamma=1.5, L0=1000L\_{0}=1000 (thousand real AUD), αg=5%\alpha\_{g}=5\%, λ=0.5\lambda=0.5.
The load f^g\widehat{f}\_{g} is computed from the Monte Carlo estimates via
([7.5](https://arxiv.org/html/2602.16212v1#S7.E5 "In 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). The last column reports the illustrative post–load
notional starting payment rate (1−f^g)​β0(1-\widehat{f}\_{g})\beta\_{0} for the reference
value β0=0.05\beta\_{0}=0.05 (see Remark [7.1](https://arxiv.org/html/2602.16212v1#S7.Thmremark1 "Remark 7.1 (Interpreting 𝑓_𝑔 in starting–rate terms). ‣ 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

Two features stand out. First, the actuarially fair expected–cost component
𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}] is modest (about 6%6\%–7%7\% of L0L\_{0}). Thus, under
actuarially fair pricing (λ=0\lambda=0), the implied equivalent load would
be only f^g≈𝔼^​[Zg]/L0≈5%\widehat{f}\_{g}\approx\widehat{\mathbb{E}}[Z\_{g}]/L\_{0}\approx 5\%–7%7\%,
which translates, for β0=5%\beta\_{0}=5\%, into an illustrative starting-rate reduction
of roughly 2525–3535 bps. Second, the tail measure
CVaR^0.05​(Zg)\widehat{\mathrm{CVaR}}\_{0.05}(Z\_{g}) is large (about 0.740.74–0.760.76 of L0L\_{0},
roughly an order of magnitude larger than 𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}]), so adding
a prudential buffer via λ=0.5\lambda=0.5 yields a substantially larger equivalent
load, f^g≈0.43\widehat{f}\_{g}\approx 0.43–0.450.45, corresponding to a post–load notional
starting payment rate of about 2.75%2.75\%–2.85%2.85\%.

To visualize the distributional features behind this result,
Figure [9.5](https://arxiv.org/html/2602.16212v1#S9.F5 "Figure 9.5 ‣ 9.7.1 Base–case MBG load ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") plots the empirical distribution of the MBG payout
ZgZ\_{g} for the four–asset (internationally diversified) tontine with stochastic
mortality (LC) and γ=1.5\gamma=1.5; the pricing tail level is αg=5%\alpha\_{g}=5\%.
Figure [9.5](https://arxiv.org/html/2602.16212v1#S9.F5 "Figure 9.5 ‣ 9.7.1 Base–case MBG load ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (a) shows the unconditional density of ZgZ\_{g}, which
exhibits a pronounced spike near zero (many scenarios in which the guarantee is
out of the money) and a long right tail. Figure [9.5](https://arxiv.org/html/2602.16212v1#S9.F5 "Figure 9.5 ‣ 9.7.1 Base–case MBG load ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (b) shows
the density conditional on Zg>0Z\_{g}>0, highlighting that when the MBG is triggered
the payout can still be large and widely spread.
In Figure [9.5](https://arxiv.org/html/2602.16212v1#S9.F5 "Figure 9.5 ‣ 9.7.1 Base–case MBG load ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") (a), the pricing threshold is VaR0.05​(Zg)≈575\mathrm{VaR}\_{0.05}(Z\_{g})\approx 575
(thousand real AUD) and the corresponding tail mean is
CVaR0.05​(Zg)≈758\mathrm{CVaR}\_{0.05}(Z\_{g})\approx 758, consistent with
Table [9.3](https://arxiv.org/html/2602.16212v1#S9.T3 "Table 9.3 ‣ 9.7.1 Base–case MBG load ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk").

![Refer to caption](figs/MBG_density_new_corrected.png)


(a) Unconditional density of ZgZ\_{g}

![Refer to caption](figs/MBG_conditional_new_corrected.png)


(b) Density conditional on Zg>0Z\_{g}>0

Figure 9.5: Empirical densities of the MBG payout ZgZ\_{g} (in real dollars at t0t\_{0})
under a representative base–case EW–CVaR optimal control:
the four–asset (internationally diversified) tontine with stochastic mortality (LC),
γ=1.5\gamma=1.5, and αg=5%\alpha\_{g}=5\%.
Units: thousands of real AUD.

For this representative policy and buffer choice, the differences between
(i) domestic–only versus internationally diversified assets and (ii)
deterministic table versus stochastic LC mortality are small in magnitude
relative to the overall load: the resulting f^g\widehat{f}\_{g} values are all close
to 0.430.43–0.450.45. In other words, the dominant driver of the equivalent load is
the tail term in ([7.5](https://arxiv.org/html/2602.16212v1#S7.E5 "In 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")), with only minor variation across the asset
and mortality specifications considered here.

#### 9.7.2 Sensitivity to risk loading and tail confidence level

We next study the sensitivity of the MBG load to (i) the prudential–buffer
parameters (λ,αg)(\lambda,\alpha\_{g}) and (ii) the retiree’s risk–reward preference in
the EW–CVaR optimization, indexed by the scalarization parameter γ\gamma.
Table [9.4](https://arxiv.org/html/2602.16212v1#S9.T4 "Table 9.4 ‣ 9.7.2 Sensitivity to risk loading and tail confidence level ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") presents the results for the four–asset
(internationally diversified) tontine with stochastic mortality (LC model)
across γ∈{1.5,0.5,0.2}\gamma\in\{1.5,0.5,0.2\}, with L0=1000L\_{0}=1000 fixed. For each γ\gamma, we
report the Monte Carlo estimates 𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}] and
CVaR^αg​(Zg)\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g}) together with the implied load estimates
f^g\widehat{f}\_{g} computed from ([7.5](https://arxiv.org/html/2602.16212v1#S7.E5 "In 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")) for λ∈{0,0.5,1}\lambda\in\{0,0.5,1\}.
For fixed (γ,αg)(\gamma,\alpha\_{g}), f^g\widehat{f}\_{g} depends linearly on λ\lambda, with
slope CVaR^αg​(Zg)/L0\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g})/L\_{0}.

Table 9.4: Sensitivity of the Monte Carlo MBG load estimate f^g\widehat{f}\_{g} in the
four–asset tontine under stochastic mortality (LC), for different retiree
risk–reward preferences indexed by γ\gamma.
Parameters: L0=1000L\_{0}=1000 (thousand real AUD), β0=0.05\beta\_{0}=0.05 (translation device; see
Remark [7.1](https://arxiv.org/html/2602.16212v1#S7.Thmremark1 "Remark 7.1 (Interpreting 𝑓_𝑔 in starting–rate terms). ‣ 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")). Part (a): αg=5%\alpha\_{g}=5\%. Part (b): αg=1%\alpha\_{g}=1\%.
f^g\widehat{f}\_{g} is computed via ([7.5](https://arxiv.org/html/2602.16212v1#S7.E5 "In 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

*(a)* αg=5%\alpha\_{g}=5\%
  



γ\gamma
𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}]
CVaR^0.05​(Zg)\widehat{\mathrm{CVaR}}\_{0.05}(Z\_{g})
f^g\widehat{f}\_{g} (λ=0\lambda=0)
f^g\widehat{f}\_{g} (λ=0.5\lambda=0.5)
f^g\widehat{f}\_{g} (λ=1\lambda=1)


1.5
70.69
758.28
0.07
0.45
0.83

0.5
58.12
729.37
0.06
0.42
0.79

0.2
47.50
664.38
0.05
0.38
0.71

*(b)* αg=1%\alpha\_{g}=1\%
  



γ\gamma
𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}]
CVaR^0.01​(Zg)\widehat{\mathrm{CVaR}}\_{0.01}(Z\_{g})
f^g\widehat{f}\_{g} (λ=0\lambda=0)
f^g\widehat{f}\_{g} (λ=0.5\lambda=0.5)
f^g\widehat{f}\_{g} (λ=1\lambda=1)


1.5
70.69
917.55
0.07
0.53
0.99

0.5
58.12
915.19
0.06
0.52
0.97

0.2
47.50
871.95
0.05
0.48
0.92

Table [9.4](https://arxiv.org/html/2602.16212v1#S9.T4 "Table 9.4 ‣ 9.7.2 Sensitivity to risk loading and tail confidence level ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") shows that the dominant drivers of the equivalent
load are the prudential–buffer parameters (λ,αg)(\lambda,\alpha\_{g}). In particular,
λ=0\lambda=0 corresponds to actuarially fair (expected–cost) pricing and
yields a modest load f^g≈5%\widehat{f}\_{g}\approx 5\%–7%7\% across the reported
γ\gamma values (about 2525–3535 bps off a notional β0=5%\beta\_{0}=5\% starting rate).
Introducing a buffer via λ>0\lambda>0 increases the load sharply because
CVaR^αg​(Zg)\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g}) is large relative to
𝔼^​[Zg]\widehat{\mathbb{E}}[Z\_{g}]: for example, at αg=5%\alpha\_{g}=5\% and λ=0.5\lambda=0.5 the
load rises to f^g≈0.38\widehat{f}\_{g}\approx 0.38–0.450.45. Tightening the tail confidence
level from αg=5%\alpha\_{g}=5\% to αg=1%\alpha\_{g}=1\% further increases
CVaR^αg​(Zg)\widehat{\mathrm{CVaR}}\_{\alpha\_{g}}(Z\_{g}) and therefore raises f^g\widehat{f}\_{g}
(e.g., to about 0.480.48–0.530.53 when λ=0.5\lambda=0.5).

Varying γ\gamma affects the load in a secondary, policy–induced way: changing
γ\gamma moves the EW–CVaR optimal policy along the efficient frontier and
thereby shifts the distribution of ZgZ\_{g} (through withdrawal timing and the
resulting account balance at death). Over the ranges considered here, this
effect is modest compared with the direct impact of (λ,αg)(\lambda,\alpha\_{g}) in
([7.5](https://arxiv.org/html/2602.16212v1#S7.E5 "In 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk")).

###### Remark 9.1.

The parameters (λ,αg)(\lambda,\alpha\_{g}) in ([7.2](https://arxiv.org/html/2602.16212v1#S7.E2 "In 7.1 Actuarial pricing formula ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))–([7.5](https://arxiv.org/html/2602.16212v1#S7.E5 "In 7.2 Simulation-based numerical methods ‣ 7 Pricing of the MBG ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk"))
summarize an additional prudential buffer applied to the MBG tail (e.g. reflecting
capital requirements, governance, or other conservatism beyond expected cost).
These parameters are typically not directly observable from public disclosures,
especially when the guarantee is embedded in the quoted payment schedule rather
than shown as an explicit fee component. Consequently, the sensitivity results in
Table [9.4](https://arxiv.org/html/2602.16212v1#S9.T4 "Table 9.4 ‣ 9.7.2 Sensitivity to risk loading and tail confidence level ‣ 9.7 MBG pricing results ‣ 9 Internationally diversified portfolios ‣ Money-Back Tontines for Retirement Decumulation: Neural-Network Optimization under Systematic Longevity Risk") should be interpreted as a pricing stress test:
they quantify how the implied load f^g\widehat{f}\_{g} changes across plausible
buffer choices, holding the underlying EW–CVaR policy and the simulated payout
distribution fixed.

## 10 Conclusion and future work

This paper studies optimal retirement decumulation in an individual tontine account with a MBG overlay in a setting that allows both international diversification and systematic longevity risk at the pool level through stochastic mortality-credit inputs. The retiree’s withdrawal and asset-allocation decisions are determined by an EW–CVaR optimal control problem solved under a plan-to-live convention, and the MBG is priced ex post under the induced optimal policy using a simulation-based actuarial load that incorporates an explicit tail-risk prudential buffer. To compute state-dependent controls in this multi-asset, constrained setting, we develop a NN approach that scales beyond classical grid-based dynamic programming.

Numerically, international diversification improves the achievable EW–CVaR trade-off even before longevity pooling, and the largest gains arise when diversification is combined with a tontine overlay. Incorporating stochastic mortality shifts the efficient frontiers in the expected direction (systematic longevity improvement reduces mortality credits) but does not alter the qualitative structure of the optimal controls. The MBG results highlight a distinct economic mechanism: when expressed in equivalent-load terms, implied MBG loads are driven primarily by prudential buffers that place weight on adverse tail outcomes, rather than by actuarially fair expected payouts.

Several extensions are natural. First, the plan-to-live convention can be relaxed by modelling death as a stopping time and embedding bequest or estate preferences directly in the retiree’s objective. Second, MBG design and valuation could be made more fully endogenous by jointly choosing the guarantee terms and the associated funding/buffer rule, and by incorporating regulatory constraints. Third, the economic environment can be enriched by incorporating additional asset classes and hedging instruments, including alternative equity benchmarks (e.g. equal-weighted indices) and currency-hedged exposures. Finally, stress-testing performance under return and mortality misspecification would help assess the practical robustness of the learned controls.

## References

* [1]

  A. Anarkulova, S. Cederburg, M. S. O’Doherty, and R. W. Sias.
  The safe withdrawal rate: Evidence from a broad sample of developed
  markets.
  Journal of Pension Economics and Finance, 24:464–500, 2025.
* [2]

  Sudipto Banerjee.
  Decoding retiree spending.
  <https://www.troweprice.com/institutional/us/en/insights/articles/2021/q1/decoding-retiree-spending-na.html>,
  2021.
  T. Rowe Price Insights on Retirement.
* [3]

  Maximilian Bär and Nadine Gatzert.
  Products and strategies for the decumulation of wealth during
  retirement: insights from the literature.
  North American Actuarial Journal, 27(2):322–340, 2023.
* [4]

  W. Bengen.
  Determining withdrawal rates using historical data.
  Journal of Financial Planning, 7:171–180, 1994.
* [5]

  Thomas Bernhardt and Catherine Donnelly.
  Modern tontine with bequest: innovation in pooled annuity products.
  Insurance: Mathematics and Economics, 86:168–188, 2019.
* [6]

  Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [7]

  Andrew JG Cairns, David Blake, and Kevin Dowd.
  A two-factor model for stochastic mortality with parameter
  uncertainty: theory and calibration.
  Journal of Risk and Insurance, 73(4):687–718, 2006.
* [8]

  M. Chen, M. Shirazi, P. A. Forsyth, and Y. Li.
  Machine learning and hamilton–jacobi–bellman equation for optimal
  decumulation: A comparison study.
  Journal of Computational Finance, 29(1):77–118, 2025.
* [9]

  Xiaoting Chen, Sherifa Elsherbiny, Ricardo Duque Gabriel, Òscar Jordà,
  Chi Hyun Kim, Moritz Schularick, and Alan M Taylor.
  Documentation on the jst database update 2016–2020, 6th release,
  july 2022, 2022.
* [10]

  Duy-Minh Dang and Chang Chen.
  Multi-period mean-buffered probability of exceedance in Defined
  Contribution portfolio optimization.
  SIAM Journal on Financial Mathematics, 2026.
  to appear.
* [11]

  Giorgio De Santis and Bruno Gerard.
  International asset pricing and portfolio diversification with
  time-varying risk.
  The Journal of Finance, 52(5):1881–1912, 1997.
* [12]

  Michel Denuit, Jan Dhaene, Marc Goovaerts, and Rob Kaas.
  Actuarial Theory for Dependent Risks: Measures, Orders and
  Models.
  John Wiley & Sons, 2005.
* [13]

  Hubert Dichtl, Wolfgang Drobetz, and Martin Wambach.
  Testing rebalancing strategies for stock-bond portfolios across
  different asset allocations.
  Applied Economics, 48(9):772–788, 2016.
* [14]

  David C. M. Dickson, Mary R. Hardy, and Howard R. Waters.
  Actuarial Mathematics for Life Contingent Risks.
  Cambridge University Press, 3 edition, 2020.
* [15]

  Catherine Donnelly.
  Actuarial fairness and solidarity in pooled annuity funds.
  ASTIN Bulletin: The Journal of the IAA, 45(1):49–74, 2015.
* [16]

  Catherine Donnelly, Montserrat Guillén, and Jens Perch Nielsen.
  Bringing cost transparency to the life annuity market.
  Insurance: Mathematics and Economics, 56:14–27, 2014.
* [17]

  P. A. Forsyth, K. R. Vetzal, and G. Westmacott.
  Optimal asset allocation for a DC pension decumulation with a
  variable spending rule.
  ASTIN Bulletin, 50(2):419–447, 2020.
* [18]

  P.A. Forsyth.
  Multiperiod mean conditional value at risk asset allocation: Is it
  advantageous to be time consistent?
  SIAM Journal on Financial Mathematics, 11(2):358–384, 2020.
* [19]

  Peter A Forsyth.
  A stochastic control approach to defined contribution plan
  decumulation: “The Nastiest, Hardest Problem in Finance”.
  North American Actuarial Journal, 26(2):227–251, 2022.
* [20]

  Peter A. Forsyth and George Labahn.
  Numerical methods for optimal decumulation of a defined contribution
  pension plan.
  Working paper, 2026.
* [21]

  Peter A Forsyth, Kenneth R Vetzal, and Graham Westmacott.
  Optimal performance of a tontine overlay subject to withdrawal
  constraints.
  ASTIN Bulletin: The Journal of the IAA, 54(1):94–128, 2024.
* [22]

  Robert K. Fullmer.
  Tontines: A practitioner’s guide to mortality-pooled investments,
  2019.
  Accessed: January 2026.
* [23]

  Jonathan T. Guyton and William J. Klinger.
  Decision rules and maximum initial withdrawal rates.
  Journal of Financial Planning, 19(3):48–58, 2006.
* [24]

  Jiequn Han et al.
  Deep learning approximation for stochastic control problems.
  arXiv preprint arXiv:1611.07422, 2016.
* [25]

  HMD.
  Human mortality database.
  <https://www.mortality.org/>.
  Max Planck Institute for Demographic Research (Germany), University
  of California, Berkeley (USA), and French Institute for Demographic Studies
  (France). Data downloaded on [date], DOI: 10.4054/HMD.Countries.[version
  code].
* [26]

  Ruimeng Hu and Mathieu Laurière.
  Recent developments in machine learning methods for stochastic
  control and games.
  Numerical Algebra, Control and Optimization, 14(3):435–525,
  2024.
* [27]

  Òscar Jordà, Katharina Knoll, Dmitry Kuvshinov, Moritz Schularick, and
  Alan M Taylor.
  The rate of return on everything, 1870–2015.
  The quarterly journal of economics, 134(3):1225–1298, 2019.
* [28]

  S.G. Kou.
  A jump diffusion model for option pricing.
  Management Science, 48:1086–1101, August 2002.
* [29]

  S.G. Kou and H. Wang.
  Option pricing under a double exponential jump diffusion model.
  Management Science, 50(9):1178–1192, September 2004.
* [30]

  Ronald D Lee and Lawrence R Carter.
  Modeling and forecasting us mortality.
  Journal of the American statistical association,
  87(419):659–671, 1992.
* [31]

  Y. Li and P.A. Forsyth.
  A data-driven neural network approach to optimal asset allocation for
  target-based defined contribution pension plans.
  Insurance: Mathematics and Economics, 86:189–204, 2019.
* [32]

  Yijia Lin, Richard D MacMinn, and Ruilin Tian.
  De-risking defined benefit plans.
  Insurance: Mathematics and Economics, 63:52–65, 2015.
* [33]

  B.J. MacDonald, B. Jones, R.J. Morrison, R.L. Brown, and M. Hardy.
  Research and reality: A literature review on drawing down retirement
  savings.
  North American Actuarial Journal, 17(3):181–215, 2013.
* [34]

  Richard MacMinn, Patrick Brockett, Jennifer Wang, Yijia Lin, and Ruilin Tian.
  The securitization of longevity risk and its implications for
  retirement security.
  Recreating sustainable retirement, pages 134–160, 2014.
* [35]

  Thomas Mathews.
  A history of australian equities.
  Research Discussion Paper RDP 2019-04, Reserve Bank of Australia,
  2019.
* [36]

  Moshe A. Milevsky and Thomas S. Salisbury.
  Financial valuation of guaranteed minimum withdrawal benefits.
  Insurance: Mathematics and Economics, 38(1):21–38, 2006.
* [37]

  Moshe A Milevsky and Thomas S Salisbury.
  Optimal retirement income tontines.
  Insurance: Mathematics and economics, 64:91–105, 2015.
* [38]

  MyNorth.
  MyNorth® Super and Pension, Product
  Disclosure Statement – Part A.
  <https://www.northonline.com.au/adviser/products/mynorth-lifetime/mynorth-lifetime-super>,
  October 2024.
  Issue date: 9 October 2024.
* [39]

  C. Ni, Y. Li, P.A. Forsyth, and R. Carroll.
  Optimal asset allocation for outperforming a stochastic benchmark
  target.
  Quantitative Finance, 22(9):1595–1626, 2022.
* [40]

  OECD.
  Pension markets in focus, 2019.
  Accessed: January 2026.
* [41]

  Andrew Patton, Dimitris N Politis, and Halbert White.
  Correction to “automatic block-length selection for the dependent
  bootstrap” by d. politis and h. white.
  Econometric Reviews, 28(4):372–375, 2009.
* [42]

  K. Peijnenburg, T. Nijman, and B.J.M. Werker.
  The annuity puzzle remains a puzzle.
  Journal of Economic Dynamics and Control, 70:18–35, 2016.
* [43]

  Wade D Pfau.
  An overview of retirement income planning.
  Journal of Financial Counseling and Planning, 29(1):114–120,
  2018.
* [44]

  Shaun Pfeiffer, John Salter, and Harold Evensky.
  Increasing the sustainable withdrawal rate using the standby reverse
  mortgage.
  Journal of Financial Planning, 26(12):55–62, 2013.
* [45]

  Dimitris N Politis and Joseph P Romano.
  The stationary bootstrap.
  Journal of the American Statistical association,
  89(428):1303–1313, 1994.
* [46]

  Dimitris N Politis and Halbert White.
  Automatic block-length selection for the dependent bootstrap.
  Econometric reviews, 23(1):53–70, 2004.
* [47]

  W Powell.
  A universal framework for sequential decision problems.
  OR/MS Today February. https://tinyurl. com/PowellORMSfeature,
  2023.
* [48]

  QSuper.
  Product update: Lifetime pension.
  <https://qsuper.qld.gov.au/-/media/pdfs/qsuper-public/publications/ltp-sen-product-update-june-25.pdf>,
  July 2025.
  Accessed: January 2026.
* [49]

  QSuper.
  QSuper Product Disclosure Statement for Income Account and Lifetime
  Pension.
  <https://qsuper.qld.gov.au/pds>, July 2025.
  Issue date: 1 July 2025.
* [50]

  A Max Reppen, H Mete Soner, and Valentin Tissot-Daguette.
  Deep stochastic optimization in finance.
  Digital Finance, 5(1):91–111, 2023.
* [51]

  Anders Max Reppen and Halil Mete Soner.
  Deep empirical risk minimization in finance: Looking into the future.
  Mathematical Finance, 33(1):116–145, 2023.
* [52]

  R.T. Rockafellar and J.O. Royset.
  Random variables, monotone relations, and convex analysis.
  Mathematical Programming, 148:297–331, 2014.
* [53]

  R.T. Rockafellar and S. Uryasev.
  Optimization of conditional value-at-risk.
  Journal of Risk, 2(3):21–41, 2000.
* [54]

  Michael J Sabin and Jonathan Barry Forman.
  The analytics of a single-period tontine.
  Available at SSRN 2874160, 2016.
* [55]

  Hersh M Shefrin and Richard H Thaler.
  The behavioral life-cycle hypothesis.
  Economic inquiry, 26(4):609–643, 1988.
* [56]

  Bruno H Solnik.
  Why not diversify internationally rather than domestically?
  Financial analysts journal, 30(4):48–54, 1974.
* [57]

  M.S. Strub, D. Li, X. Cui, and J. Gao.
  Discrete-time mean-cvar portfolio selection and time-consistency
  induced term structure of the cvar.
  Journal of Economic Dynamics and Control, 108:103751, 2019.
* [58]

  Thinking Ahead Institute.
  Global pension assets study 2023.
  <https://www.thinkingaheadinstitute.org/research-papers/global-pension-assets-study-2023/>,
  2023.
  Accessed: January 2026.
* [59]

  Ka Ho Tsang and Hoi Ying Wong.
  Deep-learning solution to portfolio selection with serially dependent
  returns.
  SIAM Journal on Financial Mathematics, 11(2):593–619, 2020.
* [60]

  United Nations, Department of Economic and Social Affairs, Population
  Division.
  World population prospects 2024, data sources.
  UN DESA/POP/2024/DC/NO. 11, 2024.
* [61]

  Pieter M van Staden, Peter A Forsyth, and Yuying Li.
  A global-in-time neural network approach to dynamic portfolio
  optimization.
  Applied Mathematical Finance, 31(3):131–163, 2024.
* [62]

  Andrés M Villegas, Vladimir K Kaishev, and Pietro Millossovich.
  Stmomo: An r package for stochastic mortality modeling.
  Journal of Statistical Software, 84:1–38, 2018.
* [63]

  Shaun S. Wang.
  A class of distortion operators for pricing financial and insurance
  risks.
  Journal of Risk and Insurance, 67(1):15–36, 2000.