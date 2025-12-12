---
authors:
- Ting-Jung Lee
- W. Brent Lindquist
- Svetlozar T. Rachev
- Abootaleb Shirvani
doc_id: arxiv:2512.10823v1
family_id: arxiv:2512.10823
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets'
url_abs: http://arxiv.org/abs/2512.10823v1
url_html: https://arxiv.org/html/2512.10823v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ting-Jung Lee


W. Brent Lindquist
Department of Mathematics & Statistics, Texas Tech University, Lubbock, TX 79409-1042, USA;
brent.lindquist@ttu.edu, zari.rachev@ttu.edu

Svetlozar T. Rachev
Department of Mathematics & Statistics, Texas Tech University, Lubbock, TX 79409-1042, USA;
brent.lindquist@ttu.edu, zari.rachev@ttu.edu

Abootaleb Shirvani
Department of Mathematical Science, Kean University, Union, NJ 07083, USA;
ashirvan@kean.edu

###### Abstract

This paper addresses a critical inconsistency in models of the term structure of interest rates (TSIR),
where zero–coupon bonds are priced under risk–neutral measures distinct from those used
in equity markets.
We propose a unified TSIR framework that treats zero–coupon bonds as European options with
deterministic payoffs ensuring that they are priced under the same risk–neutral measure
that governs equity derivatives.
Using put–call parity, we extract zero–coupon bond implied yield curves from S&P 500
index options and compare them with the US daily treasury par yield curves.
As the implied yield curves contain maturity time TT and strike price KK as independent variables,
we investigate the K−K-dependence of the implied yield curve.
Our findings, that at–the–money, option–implied yield curves provide the closest
match to treasury par yield curves, support the view that the equity options market
contains information that is highly relevant for the TSIR.
By insisting that the risk–neutral measure used for bond valuation is the same as
that revealed by equity derivatives, we offer a new organizing principle for
future TSIR research.

## 1 Introduction

Modeling the term structure of interest rates (TSIR) is fundamental to financial theory and practice,
yet traditional TSIR models exhibit inconsistencies,
particularly in the valuation of zero–coupon bonds (zero bonds) under risk–neutral measures that differ
from measures used in equity markets.
This separation leads to distinct equivalent martingale measures (EMMs) for equities and fixed–income
securities,
despite the fact that both markets are inherently linked through investor risk preferences,
monetary policy, and market frictions.
As a result, existing models often fail to fully capture the interdependencies between bond and
equity pricing,
leading to systematic pricing discrepancies.
A substantial body of literature, focussed primarily on fixed–income markets, (Section [2](https://arxiv.org/html/2512.10823v1#S2 "2 Literature Review ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets"))
has addressed the challenges of TSIR models from multiple perspectives.
Collectively these studies highlight persistent gaps between theoretical predictions and observed
yield dynamics.

The starting point for our analysis is founded on the first and second fundamental theorems
of asset pricing.
First, in a frictionless market with no arbitrage111More generally, in a market where there is “no free lunch with vanishing risk”.
there exists at least one EMM under which the
discounted prices of all traded assets are martingales
(Harrison and
Kreps, [1979](https://arxiv.org/html/2512.10823v1#bib.bib20); Harrison and
Pliska, [1981](https://arxiv.org/html/2512.10823v1#bib.bib21); Björk, [2009](https://arxiv.org/html/2512.10823v1#bib.bib6); Musiela and
Rutkowski, [2005](https://arxiv.org/html/2512.10823v1#bib.bib30)).
Second, when the market is complete this measure is unique and is empirically identified by the
cross–section of traded contingent claims, in particular by liquid equity options.
Under this EMM, any European contingent claim is valued as the discounted conditional
expectation of its payoff.
A zero bond maturing at time TT with payoff $1 is therefore just a special European claim,
and its price is obtained from the same risk-neutral measure that prices equity options.
This is exactly the logic in Shreve’s treatment of bonds and term–structure models
(Chalasani and
Jha, [1997](https://arxiv.org/html/2512.10823v1#bib.bib9), Chaps. 27, 28),
where the accumulation factor β​(t)\beta(t) is introduced and the bond price B​(t,T)B(t,T) is written
as the risk-neutral expectation of 1/β​(T)1/\beta(T) conditional on the relevant filtration ℱ​(t)\mathcal{F}(t).
Conceptually, the EMM is fixed once and for all by the global securities market;
it is not an object that can be independently chosen inside each asset class.

Under this perspective, the TSIR must be derived using the same risk–neutral measure that
governs equity derivatives.
In macrofinancial language, one may think of the EMM as the “risk–neutral world”
selected by a unique representative central bank that sets the short rate r​(t)r(t)
as the risk–free return for all traded securities, regardless of their volatility.
Once this measure is determined by the prices of equity options in a complete market,
it must also govern the valuation of fixed–income securities, including zero bonds
of all maturities.
Allowing different EMMs for bonds and for equities would immediately open the door
to cross–market arbitrage, since one could replicate the same payoff using securities
priced under two distinct “risk-neutral worlds”.

By contrast, the mainstream TSIR literature typically proceeds as if the fixed–income
market can choose its own EMM independently of the equity market.
Short–rate models such as those by Vasicek ([1977](https://arxiv.org/html/2512.10823v1#bib.bib37)); Cox
et al. ([1985](https://arxiv.org/html/2512.10823v1#bib.bib14)); and Hull and
White ([1990](https://arxiv.org/html/2512.10823v1#bib.bib24)),
as well as forward–rate and market models such as those by Heath
et al. ([1992](https://arxiv.org/html/2512.10823v1#bib.bib22)); Duffie and
Kan ([1996](https://arxiv.org/html/2512.10823v1#bib.bib17)); and
Brace
et al. ([1997](https://arxiv.org/html/2512.10823v1#bib.bib7)) begin by postulating dynamics for the short rate,
the entire forward–rate curve,
or a family of forward LIBOR rates under some reference measure.
An EMM is then constructed so that the discounted bond prices,
or the relevant forward rates, are martingales under this measure.
Within the fixed–income submarket, this construction yields an internally consistent,
arbitrage–free TSIR.
However, this procedure implicitly treats the bond market as if it were governed
by a central bank operating separately from the equity options market.
The fundamental theorems of asset pricing are applied locally to the bond market,
whereas in an integrated capital market they should be applied globally to the
universe of equity, fixed–income, and derivative securities.

Our view is that this modeling practice creates a conceptual gap between
term–structure theory and the general arbitrage pricing paradigm.
Once the equity derivatives market is complete and liquid,
the EMM is no longer a free modeling input for TSIR models;
it has already been identified by the prices of European options on the underlying
equity index.
In particular, the zero bond that pays $1 at time TT should be priced under
exactly the same EMM as any other European claim, and its yield should therefore
be consistent with the option-implied distribution of the underlying equity index
over [0,T][0,T].
In this sense, we argue that much of the TSIR literature has, perhaps inadvertently,
“forgotten” the global nature of the risk–neutral measure emphasized in the foundational
work on arbitrage pricing (Harrison and
Pliska, [1981](https://arxiv.org/html/2512.10823v1#bib.bib21); Shreve, [2004b](https://arxiv.org/html/2512.10823v1#bib.bib35)).

A parallel inconsistency appears in discrete–time models.
In binomial term–structure models and related interest–rate trees,
it is common to choose risk–neutral up and down probabilities in an ad hoc manner,
often setting them equal to one half for convenience,
and then to build bond and interest–rate dynamics under this artificially chosen
risk–neutral measure (see, for example Shreve, [2004a](https://arxiv.org/html/2512.10823v1#bib.bib34)).
Hu et al. ([2020](https://arxiv.org/html/2512.10823v1#bib.bib23)) have shown that such symmetric risk–neutral probabilities are not supported by the
empirical distribution of underlying returns and that they are statistically
misspecified when confronted with equity and option data.
The deeper message is the same: once the EMM has been fixed by traded option prices
in a complete market, it should be used consistently across all derivative and
fixed–income contracts rather than being redefined within each separate modeling context.

The present paper is intended to be “ground breaking” in precisely this conceptual sense.
We close the risk–neutral measure gap between the equity and bond markets by treating
zero bonds explicitly as European options with deterministic payoffs and by
deriving their prices directly from equity option data.
Using put–call parity (PCP) on S&P 500 index options, we construct implied yield curves
for zero bonds and compare these curves with US daily treasury par yield curves.
Because our construction is anchored in the equity options market,
the resulting TSIR is, by design, evaluated under the same EMM that governs equity
derivatives.
This unifies the valuation of fixed–income and equity derivative securities within
a single arbitrage–free framework and eliminates the artificial separation created
when TSIR models choose their own bond–market EMM.
Conceptually, our approach restores the spirit of the fundamental theorem of asset
pricing to term–structure modeling: there is one risk–neutral world,
calibrated in practice from equity options,
and all zero bonds — hence the entire term structure — must be priced in
that world.

This paper is structured as follows.
Section [2](https://arxiv.org/html/2512.10823v1#S2 "2 Literature Review ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") reviews the literature on the TSIR and PCP violations.
Section [3](https://arxiv.org/html/2512.10823v1#S3 "3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") presents the two competing
no–arbitrage formulations of TSIR and discusses their theoretical consistency.
Section [4](https://arxiv.org/html/2512.10823v1#S4 "4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") presents our empirical analysis.
As noted above, we define the implied yield of a zero bond using the European option PCP equation.
We utilized cash-settled call and put options on the S&P 500 index ˆSPX,
as this provides an underlying which represents a broad equity market.
We compared the implied yield to daily treasury par yield curves.
Unlike the par yield curves, which are functions of maturity time TT only,
the option–implied yields depend on TT and strike price KK.
One can think of the implied yields as a family of curves Y(imp)​(t,T;K)Y^{(\text{imp})}(t,T;K)
parameterized by a strike value (equivalently by a moneyness value M=K/StM=K/S\_{t},
where StS\_{t} is the value of ˆSPX at time tt).
Using box-whisker summaries of distributions, we examined the variation of this
family of implied curves, finding that in–the–money and out–of–the–money values of
KK tended to increase deviations of the implied yield from the corresponding treasury par yield,
whereas at–the–money options provided much closer agreement.
Section [5](https://arxiv.org/html/2512.10823v1#S5 "5 Discussion ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") concludes with a discussion of our results.

By no means do we claim that the empirical approach adopted here is definitive.
Rather, at the empirical level the unified EMM perspective enables us to test whether
option–implied, zero bond yields are consistent with observed treasury yields
and to quantify the extent of any residual discrepancies.
Our findings, that at–the–money option–implied yield curves provide the closest
match to treasury par yield curves, support the view that the equity options market
contains information that is highly relevant for the TSIR.
More broadly, by insisting that the EMM used for bond valuation is the same as
that revealed by equity derivatives, we offer a new organizing principle for
future TSIR research.
Existing short–rate, forward–rate, and market models can be reexamined and
recalibrated under the equity–implied EMM, rather than under a bond–specific measure,
thereby reestablishing the coherence of asset pricing across markets.

## 2 Literature Review

The modeling of the TSIR has been one of the central topics in financial economics
since the seminal contributions of Vasicek ([1977](https://arxiv.org/html/2512.10823v1#bib.bib37)) and Cox
et al. ([1985](https://arxiv.org/html/2512.10823v1#bib.bib14)).
These early short–rate models provided tractable frameworks for bond pricing but
struggled to match the observed dynamics of the yield curve.
A significant, arbitrage–free, TSIR model framework was introduced by Heath
et al. ([1992](https://arxiv.org/html/2512.10823v1#bib.bib22)).
In this approach, modeling begins with the dynamics of forward rates and derives the
EMM under which the entire family of zero bonds is arbitrage free.
Duffie and
Kan ([1996](https://arxiv.org/html/2512.10823v1#bib.bib17)); Miltersen
et al. ([1997](https://arxiv.org/html/2512.10823v1#bib.bib28)); Brace
et al. ([1997](https://arxiv.org/html/2512.10823v1#bib.bib7)) derived models with further enhancements under
this TSIR framework.
Fisher ([2004](https://arxiv.org/html/2512.10823v1#bib.bib18)) presented a foundational overview of discrete TSIR modeling approaches.

While these models secured internal consistency, they often relied on assumptions that created
discrepancies when compared with equity–based, risk–neutral valuation.
The equity–based measure reflects probabilities embedded in option prices,
whereas the bond market embeds its own risk–neutral measure inferred from treasury yields
and interest–rate derivatives.
From our perspective, Duffie ([2001](https://arxiv.org/html/2512.10823v1#bib.bib16)) and Shreve ([2004b](https://arxiv.org/html/2512.10823v1#bib.bib35)) significantly advanced the foundations of
asset pricing by establishing that zero bonds should be valued under the same risk–neutral measure
governing equity options.

Despite this, most TSIR models continued to employ distinct EMMs for fixed–income and equity markets,
resulting in inconsistencies across asset classes.
The focus on a TSIR framework divorced from equity markets has resulted in the developments of hypotheses
related to bond prices and the TSIR yield curve.222For US–based studies, the yield curve is usually interpreted to be that of US government treasury
securities.
The expectations hypothesis (Gürkaynak and
Wright, [2012](https://arxiv.org/html/2512.10823v1#bib.bib19)) states that long–term yields are equal to the average
of expected short–term interest rates until the (long–term) maturity date.
(That is, long–term bond rates are solely determined from current and future short–term rates.)
In a more expansive form, this has also been referred to as the spanning hypothesis, which
proposes that the yield curve spans all information relevant for forecasting future yields and returns;
no variables other than those embodied in the current yield curve are needed for forecasting (Bekaert
et al., [2021](https://arxiv.org/html/2512.10823v1#bib.bib4)).
This hypothesis, in either form, has proved troubling as empirical evidence (Cochrane and
Piazzesi, [2005](https://arxiv.org/html/2512.10823v1#bib.bib12); Sarno
et al., [2007](https://arxiv.org/html/2512.10823v1#bib.bib33))
demonstrated that that expectations–based models systematically failed to capture the dynamics of both
short– and long–term yields.
This work pointed to the importance of time–varying risk premia and suggested that the TSIR is likely
to be “considerably more complex” than that suggested by the expectations hypothesis.

A number of studies have established empirical links between macroeconomic factors and the TSIR
(Ang and
Piazzesi, [2003](https://arxiv.org/html/2512.10823v1#bib.bib1); Ludvigson and
Ng, [2009](https://arxiv.org/html/2512.10823v1#bib.bib27); Cooper and
Priestley, [2009](https://arxiv.org/html/2512.10823v1#bib.bib13); Bikbov and
Chernov, [2010](https://arxiv.org/html/2512.10823v1#bib.bib5); Joslin
et al., [2014](https://arxiv.org/html/2512.10823v1#bib.bib25); Cieslak and
Povala, [2015](https://arxiv.org/html/2512.10823v1#bib.bib11)).
This has coincided with the development of macrofinance term structure models (MTSMs) in either, so–called,
reduced or equilibrium forms.
(See Bauer and
Rudebusch ([2017](https://arxiv.org/html/2512.10823v1#bib.bib3), Footnotes 1 and 2) for references.)
In contrast, Duffee ([2013](https://arxiv.org/html/2512.10823v1#bib.bib15)) argued that “none of our models [linking TSIR with the macroeconomy]
is consistent with basic properties of nominal yields”,
while Bauer and
Rudebusch ([2017](https://arxiv.org/html/2512.10823v1#bib.bib3)) and Bauer and
Hamilton ([2018](https://arxiv.org/html/2512.10823v1#bib.bib2)) cited serious small–sample distortions in such studies
and suggested the evidence against the spanning hypothesis “is much weaker than it originally appeared”.
Subsequent model development by Bekaert
et al. ([2021](https://arxiv.org/html/2512.10823v1#bib.bib4)) “resurrected the evidence against the spanning
hypothesis”.

Collectively, this stream of literature highlights both theoretical and empirical tensions in the valuation
of fixed–income securities.
While not questioning the importance of this work,
we note that such TSIR models emphasize no–arbitrage conditions under bond–specific measures,
while asset pricing theory indicates that a unified risk-neutral measure should prevail across equity and
fixed–income markets.

Implicit in our empirical work in Section [4](https://arxiv.org/html/2512.10823v1#S4 "4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") is that any PCP violations should be
infrequent and small in magnitude.
Summarizing existing literature results, Kamara and
Miller ([1995](https://arxiv.org/html/2512.10823v1#bib.bib26)) noted that empirical studies reported
“frequent, substantial violations” of PCP in American options.333For American options, PCP consists of lower and upper bound inequalities
but can be rewritten as an equality by introducing early exercise premium terms for
the call and put options).
Ofek
et al. ([2004](https://arxiv.org/html/2512.10823v1#bib.bib32)) examined the effect of short sales restrictions on PCP violation
of American options and
Nishiotis and
Rompolis ([2019](https://arxiv.org/html/2512.10823v1#bib.bib31)) highlighted how regulatory constraints and short–sale restrictions amplified
violations for American options during the 2008 the US short–sale ban.

In contrast to American options, Kamara and
Miller ([1995](https://arxiv.org/html/2512.10823v1#bib.bib26)) showed that PCP violations
are “less frequent and smaller” for (cash-settled) European options on the S&P 500 index and
are primarily due to “the liquidity risk of adverse price movements from order submission until
order execution”.
An empirical study by Chesney and
Loubergé ([1995](https://arxiv.org/html/2512.10823v1#bib.bib10)) of index options on the Swiss Market Index
found severe PCP violations in that relatively young option market, with the violations decreasing
over the study time period, which the authors attributed to a learning curve by market participants.
They cited transaction costs, short selling restrictions and the impact of block trades as partial
explanations for the persistence of violations.
Mittnik and
Rieken ([2000](https://arxiv.org/html/2512.10823v1#bib.bib29)) simulated trading strategies for exploiting PCP violations for
(the then relatively new) European options on the German DAX index.
The simulations incorporated transaction costs and execution delays, two market frictions that
limit arbitrage.
In general they found that violations occur with statistical significance, but are not economically
exploitable.
As these index options were relatively new, the authors were able to show that, as traders and
market makers became more experienced with the new instrument, violations became less
frequent.
More recently, Steurer
et al. ([2022](https://arxiv.org/html/2512.10823v1#bib.bib36)) examined PCP violations for European options
on the Shanghai Stock Exchange (SSE) 50 ETF which tracks the SSE 50 index.
With the qualification that their study covers only a short time period,
the authors concluded that arbitrage opportunities are “literally not existent”.

We consequently proceed with the assumption that PCP violations of cash-settled,
European index options in the efficient US market are infrequent and small in magnitude.

## 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model

We illustrate the discrepancy in risk–neutral formulations through two propositions
both of which assume a fair (arbitrage–free) valuation of the TSIR.

Consider the stochastic basis
(Ω,𝔽={ℱt,t≥0}⊂ℱ,ℙ)(\Omega,\mathbb{F}=\{\mathcal{F}\_{t},t\geq 0\}\subset\mathcal{F},\mathbb{P})
on a complete probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}).
Let BtB\_{t}, t≥0t\geq 0 denote a standard Brownian motion defined on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P})
with the filtration ℱt=σ​(Bu,0≤u≤t)\mathcal{F}\_{t}=\sigma(B\_{u},0\leq u\leq t), t≥0t\geq 0.
We consider a market (𝒮,ℬ,𝒞)(\mathcal{S},\mathcal{B},\mathcal{C}) consisting, respectively,
of a risky asset, a riskless asset and a European contingent claim (option).
We assume the price StS\_{t} of the risky asset
follows a continuous stochastic process with dynamics given by444The regularity conditions for μt,t≥0{\mu}\_{t},t\geq 0 and σt,t≥0{\sigma}\_{t},t\geq 0 are described in
Duffie ([2001](https://arxiv.org/html/2512.10823v1#bib.bib16), Appendix E).

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=μt​St​d​t+σt​St​d​Bt,t≥0,μt∈R,σt>0,S0>0.dS\_{t}=\mu\_{t}S\_{t}dt+\sigma\_{t}S\_{t}dB\_{t},\hskip 18.49988ptt\geq 0,\ \mu\_{t}\in R,\ \sigma\_{t}>0,\ S\_{0}>0. |  | (1) |

The price βt\beta\_{t} of the riskless asset evolves as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​βt=rt​βt​d​t,β0>0.d\beta\_{t}=r\_{t}\beta\_{t}dt,\hskip 18.49988pt\beta\_{0}>0. |  | (2) |

With the appropriate regularity conditions555The regularity conditions for rt,t≥0r\_{t},t\geq 0 are described in Duffie ([2001](https://arxiv.org/html/2512.10823v1#bib.bib16), Section 5G).
on rtr\_{t}, ([2](https://arxiv.org/html/2512.10823v1#S3.E2 "In 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) has the solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt=exp⁡{∫0trs​𝑑s}.\beta\_{t}=\exp\left\{\int\_{0}^{t}r\_{s}ds\right\}. |  | (3) |

We assume μt\mu\_{t}, σt\sigma\_{t} and rtr\_{t} are ℱ\mathcal{F}–adapted.
The price CtC\_{t} of the option has the dependence Ct=f​(St,t)C\_{t}=f(S\_{t},t), t∈[0,τ]t\in[0,\tau],
with terminal payoff at the maturity time τ\tau, given by Cτ=g​(Sτ)C\_{\tau}=g(S\_{\tau}).666The regularity conditions for f​(x,t)f(x,t), x>0x>0, t∈[0,τ)t\in[0,\tau), and g​(x)g(x), x>0x>0
are described in Duffie ([2001](https://arxiv.org/html/2512.10823v1#bib.bib16), Section 5G).

The market (𝒮,ℬ,𝒞)(\mathcal{S},\mathcal{B},\mathcal{C}) is arbitrage–free and complete provided
the market price of risk
θt=(μt−rt)/σt\theta\_{t}=(\mu\_{t}-r\_{t})/\sigma\_{t} satisfies the condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | θt=μt−rtσt>0,ℙ​-a.s. for all ​t≥0.\theta\_{t}=\frac{\mu\_{t}-r\_{t}}{\sigma\_{t}}>0,\qquad\mathbb{P}\text{-a.s. for all }t\geq 0. |  | (4) |

As a consequence, there exists (Duffie, [2001](https://arxiv.org/html/2512.10823v1#bib.bib16), Sections 6G and 6H) a unique EMM
ℚ\mathbb{Q} such that the standard Brownian motion BtℚB\_{t}^{\mathbb{Q}} on
(Ω,𝔽,ℚ)(\Omega,\mathbb{F},\mathbb{Q}) is related to the natural–world Brownian motion BtB\_{t}
through the market price of risk,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Btℚ=d​Bt+θt​d​t.dB\_{t}^{\mathbb{Q}}=dB\_{t}+\theta\_{t}dt. |  | (5) |

The (risk–neutral) dynamics of 𝒮\mathcal{S} on (Ω,𝔽,ℚ)(\Omega,\mathbb{F},\mathbb{Q}) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=rt​St​d​t+σt​St​d​Btℚ,t∈[0,τ].dS\_{t}=r\_{t}S\_{t}dt+\sigma\_{t}S\_{t}dB\_{t}^{\mathbb{Q}},\qquad t\in[0,\tau]. |  | (6) |

The risk–neutral (fair) value of the contingent claim CC at any time t∈[0,τ)t\in[0,\tau) is given by the
standard risk–neutral valuation formula (Duffie, [2001](https://arxiv.org/html/2512.10823v1#bib.bib16), p116, equation (15))

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct=𝔼tℚ​[e−∫tτrs​𝑑s​g​(Sτ)].C\_{t}=\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{\tau}r\_{s}ds}g(S\_{\tau})\right]. |  | (7) |

The first proposition forms the basis for risk–neutral asset valuation of the TSIR in the
market model defined by ([1](https://arxiv.org/html/2512.10823v1#S3.E1 "In 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets"))–([7](https://arxiv.org/html/2512.10823v1#S3.E7 "In 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")).

###### Proposition 3.1

Consider a unit zero bond 𝒵t\mathcal{Z}\_{t}, for 0≤T≤τ0\leq T\leq\tau,
which can be viewed as an option with maturity TT and payoff g​(𝒵T)=$​1g(\mathcal{Z}\_{T})=\mathdollar 1.
From ([7](https://arxiv.org/html/2512.10823v1#S3.E7 "In 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")), the risk–neutral value of 𝒵t\mathcal{Z}\_{t} for t∈[0,T]t\in[0,T] is given by
(see also, Duffie ([2001](https://arxiv.org/html/2512.10823v1#bib.bib16), p127, equation (21)) or Chalasani and
Jha ([1997](https://arxiv.org/html/2512.10823v1#bib.bib9), p267))

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(t,T)=𝔼tℚ​[e−∫tTrs​𝑑s],t∈[0,T].\Lambda(t,T)=\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}r\_{s}ds}\right],\hskip 18.49988ptt\in[0,T]. |  | (8) |

The collection Λ​(t,T)\Lambda(t,T) or, equivalently, Y​(t,T)=ln⁡Λ​(t,T)Y(t,T)=\ln\Lambda(t,T), for 0≤t≤T≤τ0\leq t\leq T\leq\tau,
defines the TSIR.

The alternate proposition considers the ℱ\mathcal{F}–adapted interest rate process rtr\_{t} defining
the riskless asset price ([3](https://arxiv.org/html/2512.10823v1#S3.E3 "In 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) for t∈[0,T]t\in[0,T].
It assumes the family of all unit zero bonds 𝒵T\mathcal{Z}\_{T} having maturities over the range
0≤T≤τ0\leq T\leq\tau are default–free.
Let

|  |  |  |
| --- | --- | --- |
|  | W​(t,T)​ denote the price of the zero bond ​𝒵T​ at time ​t∈[0,T].W(t,T)\text{ denote the price of the zero bond }\mathcal{Z}\_{T}\text{ at time }t\in[0,T]. |  |

It is assumed that W​(t,T)W(t,T) is adapted to the filtration 𝔽[0,T]={ℱt,t∈[0,T]}\mathbb{F}\_{[0,T]}=\{\mathcal{F}\_{t},t\in[0,T]\}.
The alternative TSIR (ATSIR) is defined as the collection {W​(t,T), 0≤t≤T≤τ}\{W(t,T),\ 0\leq t\leq T\leq\tau\}.

###### Proposition 3.2

The ATSIR is free of arbitrages if and only if there exists a probability measure777ℙ~∼ℙ\tilde{\mathbb{P}}\sim\mathbb{P} states ℙ~\tilde{\mathbb{P}} and ℙ\mathbb{P}
are equivalent probability measures; specifically, for A∈ℱA\in\mathcal{F},
ℙ~​(A)=0\tilde{\mathbb{P}}(A)=0 if only if P​(A)=0P(A)=0.
ℙ~∼ℙ\tilde{\mathbb{P}}\sim\mathbb{P} such that the discounted zero bond price

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(t,T)βt,t∈[0,T]\frac{W(t,T)}{{\beta}\_{t}},\hskip 18.49988ptt\in[0,T] |  | (9) |

is a martingale under the probability space (Ω,𝔽[0,T],ℙ~)(\Omega,\mathbb{F}\_{[0,T]},\tilde{\mathbb{P}}).

As noted in the introduction, the alternate proposition has been widely applied in TSIR
modeling (see e.g.,
Shreve ([2004b](https://arxiv.org/html/2512.10823v1#bib.bib35), Chapter 10), Cairns ([2004](https://arxiv.org/html/2512.10823v1#bib.bib8), Chapters 4–6) and Wu ([2019](https://arxiv.org/html/2512.10823v1#bib.bib38), Chapter 4)).

As the market (𝒮,ℬ,𝒞)(\mathcal{S},\mathcal{B},\mathcal{C}) is assumed to be complete and arbitrage free,
and 𝒞\mathcal{C} can represent any zero bond 𝒵T\mathcal{Z}\_{T},
from the point of view of Proposition [3.1](https://arxiv.org/html/2512.10823v1#S3.Thmproposition1 "Proposition 3.1 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")
it follows that ℙ~\tilde{\mathbb{P}} must coincide with ℚ\mathbb{Q}.
However, Proposition [3.2](https://arxiv.org/html/2512.10823v1#S3.Thmproposition2 "Proposition 3.2 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") claims that ℙ~\tilde{\mathbb{P}} is fundamentally different
from ℚ\mathbb{Q}, leading to inconsistent views.
Proposition [3.2](https://arxiv.org/html/2512.10823v1#S3.Thmproposition2 "Proposition 3.2 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") basically states that there exist two central banks,
one dealing with equity pricing and all options, and another just for the zero bonds.
The measure ℚ\mathbb{Q} is derived from the market price of risk ([4](https://arxiv.org/html/2512.10823v1#S3.E4 "In 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) and is influenced
by the volatility σt\sigma\_{t}, which is a key component of asset pricing models.
In contrast, the measure ℙ~\tilde{\mathbb{P}} is defined independently of θt\theta\_{t} and,
more critically, is indifferent to the volatility σt\sigma\_{t} of the equity market.888Equity market volatility can indeed impact bond yields, as demonstrated by various sources.
1.

The Federal Reserve Bank of St. Louis highlighted that equity market volatility,
tracked by the VIX and realized volatility of returns on the S&P 500,
moves in tandem with bond yields.
Increased equity volatility often leads investors to shift their investments to bonds,
impacting the yield curve and bond performance
(<https://fred.stlouisfed.org/series/EMVMACROINTEREST>).
2.

The CME Group discussed how equity market conditions and the actions of the
Federal Reserve, such as quantitative easing, influence bond yields.
They noted that periods of high equity volatility typically result in lower bond yields
due to increased demand for safer assets
(<https://www.cmegroup.com/education/featured-reports/end-of-the-road-for-the-yield-curve-vs-volatility-cycle.html>).
3.

The Office of Financial Research elaborated on how rising interest rates and
equity market volatility pose risks to insurers’ investment portfolios.
They indicated that insurers exposed to equity market volatility might face reduced liquidity
and increased risk, affecting their bond investment strategies and yields
(<https://www.financialresearch.gov/the-ofr-blog/2022/07/21/Rising-Interest-Rates-Help-Insurers-but-Market-Volatility-Poses-Risk-to-Some/>)

## 4 Empirical Comparison of Yield

The conclusion that Proposition [3.1](https://arxiv.org/html/2512.10823v1#S3.Thmproposition1 "Proposition 3.1 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") provides the appropriate universal
valuation of a TSIR, provides the motivation to compare the yield determined by the
proposition with observed market yields.
We define an implied yield based on the
parity relationship for European put–call pairs of option contracts,
specifically of cash-settled options on the broad market index ˆSPX.
The specific option chains used were for the five trading dates in the period
09–15 October, 2024.999Data source: Yahoo Finance. Accessed 16 October, 2024.
The option chains were based upon close–of–market values of the index.
We took the market yield to be the rates of the US daily treasury par yield curve
for the same five trading days.101010Data source: US Treasury, accessed June 6, 2025.
As 14 October 2024 was a federal holiday, and as the par yield rates had small daily changes,
we obtained equivalent market rates for 14 October by simply averaging those for 11 and 15 October.
We examined the dependence of the implied yield on maturity time and strike price.
We defined two measures of dislocation between the implied yield and
the par yield curve and examined this dislocation as a function of the time to maturity.

### 4.1 Implied Yield as a Function of Strike and Maturity

We define the discount factor of a zero bond (Proposition [3.1](https://arxiv.org/html/2512.10823v1#S3.Thmproposition1 "Proposition 3.1 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) using
the European option PCP equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(t,T,K)=1K​[St+P​(t,T,K)−C​(t,T,K)],\Lambda(t,T,K)=\frac{1}{K}\left[S\_{t}+P(t,T,K)-C(t,T,K)\right], |  | (10) |

where
P​(t,T,K)P(t,T,K) and C​(t,T,K)C(t,T,K) are, respectively, put and call option prices for contracts
having maturity TT and strike price KK,
and StS\_{t} is the spot price of the underlying asset
(in our case the value of the index ˆSPX).
As a consequence of this definition, the discount factor Λ​(t,T,K)\Lambda(t,T,K) is dependent on
TT and KK.
The T,KT,K–dependent yield implied from ([10](https://arxiv.org/html/2512.10823v1#S4.E10 "In 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y​(t,T,K)=−1T−t​ln⁡[Λ​(t,T,K)].Y(t,T,K)=-\frac{1}{T-t}\ln[\Lambda(t,T,K)]. |  | (11) |

We refer to Y​(t,T,K)Y(t,T,K) as the “option implied yield” (implied yield for brevity).
We use the notation Ymkt​(t,T)Y^{\text{mkt}}(t,T) to refer to the rates from the treasury par
yield curves.
From ([11](https://arxiv.org/html/2512.10823v1#S4.E11 "In 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) and ([10](https://arxiv.org/html/2512.10823v1#S4.E10 "In 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")), and noting that StS\_{t}, KK, P​(t,T,K)P(t,T,K) and C​(t,T,K)C(t,T,K)
are always positive, we have111111Technically, ([12a](https://arxiv.org/html/2512.10823v1#S4.E12.1 "In 12 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) should be written C​(t,T,K)<St+P​(t,T,K)<K+C​(t,T,K)C(t,T,K)<S\_{t}+P(t,T,K)<K+C(t,T,K),
but as C​(t,T,K)<StC(t,T,K)<S\_{t} always (otherwise why purchase the call option?),
we have neglected the first inequality.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | Y​(t,T,K)>0​ if ​0\displaystyle Y(t,T,K)>0\text{ if }0 | <Λ​(t,T,K)<1\displaystyle<\Lambda(t,T,K)<1 |  |
|  |  | →St+P​(t,T,K)<K+C​(t,T,K),\displaystyle\rightarrow S\_{t}+P(t,T,K)<K+C(t,T,K), |  | (12a) |
|  | Y​(t,T,K)<0​ if ​1\displaystyle Y(t,T,K)<0\text{ if }1 | <Λ​(t,T,K)\displaystyle<\Lambda(t,T,K) |  |
|  |  | →St+P​(t,T,K)>K+C​(t,T,K).\displaystyle\rightarrow S\_{t}+P(t,T,K)>K+C(t,T,K). |  | (12b) |

![Refer to caption](Y3D1009.png)


Figure 1: 3D scatter plot of implied yields Y​(t,T,K)Y(t,T,K)
versus strike KK and maturity TT for the trading day t=t= 09 October, 2024.

Fig. [1](https://arxiv.org/html/2512.10823v1#S4.F1 "Figure 1 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") presents the implied yield Y​(t,T,K)Y(t,T,K) computed from the option chain of 09 October, 2024.
Fig. [S1](https://arxiv.org/html/2512.10823v1#A1.F1 "Figure S1 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") in the supplementary material presents the implied yields computed for the option chains
of 10–15 October, 2024.
The plot highlights two key features.
First, the implied yield surface appears to be centered close to zero,121212However, the y−y-axis scale of O​(10−2)O\left(10^{-2}\right) is quite large.
consistent with PCP under no–arbitrage.
Second, large, negative values of Y​(t,T,K)Y(t,T,K) occurred more frequently for K<StK<S\_{t}
(i.e., for M=K/St<1M=K/S\_{t}<1)
and short horizons (e.g., T−t≲45T-t\lesssim 45 days).
Writing ([12b](https://arxiv.org/html/2512.10823v1#S4.E12.2 "In 12 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) as (St−K)+P​(t,T,K)>C​(t,T,K)(S\_{t}-K)+P(t,T,K)>C(t,T,K),
we suspect ([12b](https://arxiv.org/html/2512.10823v1#S4.E12.2 "In 12 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) is satisfied for K<StK<S\_{t} when a current value of St−KS\_{t}-K is compared to
either a stale put or call price on a T,KT,K contract at short maturity times.
Yield values stabilize closer to zero as the time to maturity increases.

![Refer to caption](CallContractCounts_20241009.png)


Figure 2: Two-dimensional scatter plot of the number of ˆSPX call contracts versus time
to maturity TT for the option chain of 09 October, 2024.

Our data set consists of a mixture of contract types: daily, monthly, quarterly and longer–term.
Fig. [2](https://arxiv.org/html/2512.10823v1#S4.F2 "Figure 2 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") displays a two dimensional scatter plot of the number of ˆSPX
call contracts versus time to maturity TT for the option chain of 09 October, 2024.
The distribution of contracts exhibits two distinct clusters:
a cluster of contracts consisting of short maturity “dailies” (extending out to T=44T=44 days)
and a cluster extending over longer horizons, which includes monthly, quarterly and
long–term equity anticipation securities.
We refer to the two clusters as “short term” and “long term”.
This clustering pattern was also observed for the put options and appeared in each of the
four option chains studied over the period 10–15 October, 2024
(see Fig. [S2](https://arxiv.org/html/2512.10823v1#A1.F2 "Figure S2 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") in the supplementary material).
To look for potential differences in the implied yield Y​(t,T,K)Y(t,T,K),
we analyzed short– and long–term contracts separately.

![Refer to caption](YTLS_1009_box.png)


Figure 3: Box-whisker summaries of the distributions of the implied yield Y​(t,T)Y(t,T) with maturity
time TT. The panels summarize (left) short–term and (right) long–term contracts.
For better representation, the negative range of the y−y-axis has been truncated;
consequently, negative outliers for small values of TT are not visible.

Fig. [3](https://arxiv.org/html/2512.10823v1#S4.F3 "Figure 3 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") presents box-whisker summaries of the variation of the distribution of Y​(t,T,K)Y(t,T,K)
with strike price KK at each fixed maturity time TT for the data in Fig. [1](https://arxiv.org/html/2512.10823v1#S4.F1 "Figure 1 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets").
The short– and long–term contracts are summarized separately.
(Fig. [S3](https://arxiv.org/html/2512.10823v1#A1.F3 "Figure S3 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") in the supplementary material provides the same summaries for the option chains
of 10–15 October, 2024.)
For fixed TT, we note that the distribution is generally skewed towards negative yield values,
with the skewness most prevalent at the shorter maturity times.
The number of negative yield outliers is more predominant in the long–term contracts.
There is sizable variation in yield values at smaller maturity values, with the variation
significantly diminishing as maturity time increases.
The predominance of negative implied yields computed using PCP cannot be ascribed simply
to effects such as stale call or put prices due to asynchronous trading of contracts.
However, our interest is not in the reason for the negative yields, but rather on effective
measures of the discrepancy between implied and published yield rates.
To compare the implied yield rates Y​(t,T,K)Y(t,T,K) against a published rate Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T) for
day tt requires a method of aggregating the implied rates.
In sections [4.2](https://arxiv.org/html/2512.10823v1#S4.SS2 "4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") and [4.3](https://arxiv.org/html/2512.10823v1#S4.SS3 "4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets"), we consider two aggregation methods.

### 4.2 Median-Strike Aggregation of Implied Option Yields

We considered a “median strike” method,
where the dependence of the implied yield on the strike price is reduced to a median value
at each fixed value of TT.
Specifically, from ([11](https://arxiv.org/html/2512.10823v1#S4.E11 "In 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) we computed131313The median was chosen instead of the mean as it is unaffected by
the magnitude of outlier values.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y(med)​(t,T)=median𝐾​{Y​(t,T,K)}.Y^{(\text{med})}(t,T)=\underset{K}{\text{median}}\{Y(t,T,K)\}. |  | (13) |

We define the maturity–dependent dislocation between the yield ([13](https://arxiv.org/html/2512.10823v1#S4.E13 "In 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets"))
and the market yield by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔY(med)​(t,T)=Y(med)​(t,T)−Y(mkt)​(t,T).\Delta\_{Y}^{(\text{med})}(t,T)=Y^{(\text{med})}(t,T)-Y^{(\text{mkt})}(t,T). |  | (14) |

![Refer to caption](yieldcurve_20241009.png)


Figure 4: PCHIP fits to the 09 October 2024, US daily treasury par yield curve rates for maturities
TT of 1 month through 30 years.
The fit for T<1T<1 month uses the rate for T=1T=1 month.

The treasury par yield curve bill, note and bond rates have maturities T∈{1,2,3,4,6}T\in\{1,2,3,4,6\} months
and T∈{1,2,3,5,7,10,20,30}T\in\{1,2,3,5,7,10,20,30\} years.
As the maturity time of the option chains do not usually align with the par yield curve maturities,
we interpolated the daily par yield curve rates using a piecewise cubic Hermite interpolating polynomial (PCHIP)
to provide a market rate for any option maturity time between one month and 30 years.
For option maturity times below one month, we simply used the one month par yield rate.
Fig. [4](https://arxiv.org/html/2512.10823v1#S4.F4 "Figure 4 ‣ 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") shows the PCHIP fit to the par yield curve rates for 09 October 2024.
The fits to the par yield curve rates for the other four trading days are very similar to that shown in
Fig. [4](https://arxiv.org/html/2512.10823v1#S4.F4 "Figure 4 ‣ 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets").

![Refer to caption](Ymed_short_1009.png)

![Refer to caption](Ymed_long_1009.png)

Figure 5: The implied yield curves (solid line) Y(med)​(t,T)Y^{(\text{med})}(t,T)
and (dashed line) Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T) (PCHIP fit)
as a function of time to maturity TT for t=t= 09 October, 2024.
Given the range of the y−y-axis values, it is difficult to see the variation in Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T)
with TT that is apparent in Fig. [4](https://arxiv.org/html/2512.10823v1#S4.F4 "Figure 4 ‣ 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets").



![Refer to caption](DYMED_short_ALL.png)

![Refer to caption](DYMED_long_ALL.png)

Figure 6: The dislocation ΔY(med)​(t,T)\Delta\_{Y}^{(\text{med})}(t,T) between the US daily treasury par
yield curve and the implied median yield curve from options on ˆSPX for the
(top) short–term and (bottom) long–term maturity contracts.

We found it instructive to plot Y(med)​(t,T)Y^{(\text{med})}(t,T) and Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T) separately on the same plot.
Fig. [5](https://arxiv.org/html/2512.10823v1#S4.F5 "Figure 5 ‣ 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") shows the plots for the short– and long–term contracts of 09 October, 2024.
Fig. [S5](https://arxiv.org/html/2512.10823v1#A1.F5 "Figure S5 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") in the supplementary material shows the plots for the contracts of 10–15 October, 2024.
For clearer visualization of the results, the T−T-axis is displayed using a logarithmic scale for
the long–term contracts.

For the short–term options, the median implied yield essentially hovers around a value that is negative
and less than the market yield curve for that date.
The exception is 15 October, 2024 (Fig. [S5](https://arxiv.org/html/2512.10823v1#A1.F5 "Figure S5 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")),
where the median yield hovers around the market yield curve.
For the long–term options, the median yield monotonically rises through negative values and approaches
the long–maturity treasury yield curve rates at the longest maturity times (which approach five years).

Fig. [6](https://arxiv.org/html/2512.10823v1#S4.F6 "Figure 6 ‣ 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") summarizes the results for all five days of option chains by plotting the yield dislocation
ΔY(med)​(t,T)\Delta\_{Y}^{(\text{med})}(t,T) separately for the short– and long–term contracts.
The short–term median yield curves remain below the market yield curve
while the long–term median yield curves converge consistently to the market yield curve at large maturities.

### 4.3 At–the–Money Put–Call Parity Yields

Examination of the variation of the implied yield at constant strike value suggested a second aggregation
method.

![Refer to caption](YMLS_1009_box.png)


Figure 7: Box-whisker summaries of the distributions of the implied yield Y​(t,M)Y(t,M) with moneyness
M=K/StM=K/S\_{t} . The panels summarize (top) short–term and (bottom) long–term contracts.
For better representation, the negative range of the y−y-axis has been truncated

Fig. [7](https://arxiv.org/html/2512.10823v1#S4.F7 "Figure 7 ‣ 4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") plots box-whisker summaries of the distributions of the implied yield Y​(t,M)Y(t,M)
at constant moneyness values M=K/StM=K/S\_{t} for the short– and long–term contracts for the option
chain of 09 October, 2024.141414In order to account for the large number of strike price values, the data were grouped into strike
price “bins”, as would be done in a histogram.
The strike (and hence moneyness) value characterizing each bin corresponds to the median
of the strike values represented by the bin.
Each box-whisker summarizes the distribution of yield values computed for the strike prices
grouped within the bin.
Fig. [S6](https://arxiv.org/html/2512.10823v1#A1.F6 "Figure S6 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") in the supplementary material plots the box-whisker summaries for the option chains
for 10–15 October, 2024.
An examination of these distributions shows that the interquartile width narrows considerably for M=1M=1.
As MM moves away from unity, the distributions widen and become more negative.
Therefore, as an alternative to the median strike dislocation method ([14](https://arxiv.org/html/2512.10823v1#S4.E14 "In 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")),
we considered the at–the–money (ATM) dislocation measure

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔY(ATM)​(t,T)=Y​(t,T,M=1)−Y(mkt)​(t,T).\Delta\_{Y}^{(\text{ATM})}(t,T)=Y(t,T,M=1)-Y^{(\text{mkt})}(t,T). |  | (15) |

![Refer to caption](YATM_short_1009.png)

![Refer to caption](YATM_long_1009.png)

Figure 8: The yield curves (solid line) Y(ATM)​(t,T)Y^{(\text{ATM})}(t,T)
and (dashed line) Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T) (PCHIP fit)
as a function of time to maturity TT for t=t= 09 October, 2024.



![Refer to caption](DYATM_short_ALL.png)

![Refer to caption](DYATM_long_ALL.png)

Figure 9: Dislocation between the US daily treasury par yield curve and
the implied at–the–money yield curve from options on ˆSPX
for the (top) short–term and (bottom) long–term maturity contracts.
Note the log scale TT–axis in the bottom plot.

Fig. [8](https://arxiv.org/html/2512.10823v1#S4.F8 "Figure 8 ‣ 4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") plots the yield curves Y(ATM)​(t,T)Y^{(\text{ATM})}(t,T) and Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T)
for the short– and long–term contracts of 09 October, 2024.
Fig. [S9](https://arxiv.org/html/2512.10823v1#A1.F9 "Figure S9 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") in the supplementary material shows the plots for the contracts of 10–15 October, 2024.
Fig. [9](https://arxiv.org/html/2512.10823v1#S4.F9 "Figure 9 ‣ 4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") displays ΔY(ATM)​(t,T)\Delta\_{Y}^{(\mathrm{ATM})}(t,T) for each of the five trading days
tt during the week 9–15 October, 2024.
Unlike Y(med)​(t,T)Y^{(\mathrm{med})}(t,T), the values of Y(ATM)​(t,T)Y^{(\mathrm{ATM})}(t,T) tend to be closer to
the US daily treasury par yield curve benchmark values for both short– and long–term options.
The fluctuations tend to be slightly larger for the short–term contracts.
The curve Y(ATM)​(t,T)Y^{(\mathrm{ATM})}(t,T) tends to follow the par yield curve trend for large maturity times
(Figs. [8](https://arxiv.org/html/2512.10823v1#S4.F8 "Figure 8 ‣ 4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") and [S9](https://arxiv.org/html/2512.10823v1#A1.F9 "Figure S9 ‣ Appendix A Supplementary Material ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")),
although there is perhaps a slight indication that the ATM implied yield is deviating below the benchmark
yield at large maturity times (Fig. [9](https://arxiv.org/html/2512.10823v1#S4.F9 "Figure 9 ‣ 4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")).

Referring to Proposition [3.1](https://arxiv.org/html/2512.10823v1#S3.Thmproposition1 "Proposition 3.1 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets"), we note that the natural option
pricing ([8](https://arxiv.org/html/2512.10823v1#S3.E8 "In Proposition 3.1 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) of a unit zero bond contains no strike price KK.
One interpretation of a fixed, K−K-independent payout reflected by ([8](https://arxiv.org/html/2512.10823v1#S3.E8 "In Proposition 3.1 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets"))
is that a zero–bond option is always at–the–money.
This is consistent with our findings of Y(ATM)​(t,T)Y^{(\text{ATM})}(t,T) providing the best fit to
the market yield curve.

## 5 Discussion

We have shown via use of the arbitrage–free PCP formula, that pairs of call and put options
(having common strike price and maturity date) in the ˆSPX option chain for any date tt produce
a wide range of implied yield rates, which may, in fact, be negative.
The variability (Fig. [3](https://arxiv.org/html/2512.10823v1#S4.F3 "Figure 3 ‣ 4.1 Implied Yield as a Function of Strike and Maturity ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")) is larger for shorter term maturity dates.
For in–the–money and and out–of–the–money strike prices,
the implied yields show significant deviation from the US daily treasury par yield curve rates,
which are commonly used as risk free rates in equity markets (Fig. [7](https://arxiv.org/html/2512.10823v1#S4.F7 "Figure 7 ‣ 4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets")).
However, implied yield rates computed from PCP using ATM option prices (Fig. [9](https://arxiv.org/html/2512.10823v1#S4.F9 "Figure 9 ‣ 4.3 At–the–Money Put–Call Parity Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets"))
are consistent with US daily treasury par yield curve rates.

We have argued that ATSIR models that utilize Proposition [3.2](https://arxiv.org/html/2512.10823v1#S3.Thmproposition2 "Proposition 3.2 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") are inconsistent in that they
implicitly assume the existence of two central banks, one dealing with equity and option prices and the other
dealing with zero bonds.
Our empirical work has demonstrate that, if the pricing of a unit zero bond is determined as if the bond were
an option (maturity TT, payoff $1), its price can be determined under the same risk–neutral measure
as that governing equity option markets.
Specifically, we have shown that the US daily treasury par yield rates are consistent with the
arbitrage–free yields obtained from PCP applied to at–the–money
options whose underlying, the S&P 500 index, represents a broad component of the US equity market.
Thus, we argue, Proposition [3.1](https://arxiv.org/html/2512.10823v1#S3.Thmproposition1 "Proposition 3.1 ‣ 3 Two Formulations of Arbitrage–Free TSIR in a Complete Market Model ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets") provides the appropriate theory and
the at–the–money yield provides an appropriate TSIR framework to coherently
unite equity and fixed–income valuation.

## References

* \NAT@swatrue
* Ang and
  Piazzesi (2003)

  Ang, A. and M. Piazzesi (2003).
  A no-arbitrage vector autoregression of term structure dynamics with
  macroeconomic and latent variables.
  Journal of Monetary Economics 50(4), 745––787.
  \NAT@swatrue
* Bauer and
  Hamilton (2018)

  Bauer, M. D. and J. D. Hamilton (2018).
  Robust bond risk premia.
  The Review of Financial Studies 31(2), 399–448.
  \NAT@swatrue
* Bauer and
  Rudebusch (2017)

  Bauer, M. D. and G. D. Rudebusch (2017).
  Resolving the spanning puzzle in macro-finance term structure models.
  Review of Finance 21(2), 511–553.
  \NAT@swatrue
* Bekaert
  et al. (2021)

  Bekaert, G., E. Engstrom, and A. Ermolov (2021).
  Macro risks and the term structure of interest rates.
  Journal of Financial Economics 141, 479–504.
  \NAT@swatrue
* Bikbov and
  Chernov (2010)

  Bikbov, R. and M. Chernov (2010).
  No–arbitrage macroeconomic determinants of the yield curve.
  Journal of Economics 159.
  \NAT@swatrue
* Björk (2009)

  Björk, T. (2009).
  Arbitrage Theory in Continuous Time (3rd ed.).
  Oxford: Oxford University Press.
  \NAT@swatrue
* Brace
  et al. (1997)

  Brace, A., D. G. Gatarek, and M. Musiela (1997).
  The market model of interest rate dynamics.
  Mathematical Finance 7(2), 127––155.
  \NAT@swatrue
* Cairns (2004)

  Cairns, A. J. G. (2004).
  Interest Rate Models: An Introduction.
  Princeton, NJ: Princeton University Press.
  \NAT@swatrue
* Chalasani and
  Jha (1997)

  Chalasani, P. and S. Jha (1997).
  Steven Shreve: Stochastic Calculus and Finance.
  Unpublished manuscript draft. Available at
  <http://efinance.org.cn/cn/FEshuo/stochastic.pdf>.
  \NAT@swatrue
* Chesney and
  Loubergé (1995)

  Chesney, Marc amd Gibson, R. and H. Loubergé (1995).
  Arbitrage trading and index option pricing at SOFFEX: An
  empirical study using daily and intradaily data.
  Finanzmarkt und Portfolio Management 9(1), 36–60.
  \NAT@swatrue
* Cieslak and
  Povala (2015)

  Cieslak, A. and P. Povala (2015).
  Expected returns in treasury bonds.
  The Review of Financial Studies 28(10),
  2859––2901.
  \NAT@swatrue
* Cochrane and
  Piazzesi (2005)

  Cochrane, J. H. and M. Piazzesi (2005).
  Bond risk premia.
  American Economic Review 95(1), 138–160.
  \NAT@swatrue
* Cooper and
  Priestley (2009)

  Cooper, I. and R. Priestley (2009).
  Time-varying risk premiums and the output gap.
  The Review of Financial Studies 22(7), 2801––2833.
  \NAT@swatrue
* Cox
  et al. (1985)

  Cox, J. C., J. E. Ingersoll, and S. A. Ross (1985).
  A theory of the term structure of interest rates.
  Econometrica 53(2), 385–407.
  \NAT@swatrue
* Duffee (2013)

  Duffee, G. R. (2013).
  Bond pricing and the macroeconomy.
  In G. M. Constantinides, M. Harris, and R. M. Stulz (Eds.), Handbook of the Economics of Finance, Volume 2, pp. 907––967.
  Elsevier.
  \NAT@swatrue
* Duffie (2001)

  Duffie, D. (2001).
  Dynamic Asset Pricing Theory (3rd ed.).
  Princeton, NJ: Princeton University Press.
  \NAT@swatrue
* Duffie and
  Kan (1996)

  Duffie, D. and R. Kan (1996).
  A yield-factor model of interest rates.
  Mathematical Finance 6(4), 379–406.
  \NAT@swatrue
* Fisher (2004)

  Fisher, M. (2004).
  Modeling the term structure of interest rates: An introduction.
  Federal Reserve Bank of Atlanta Economic Review 89(3), 41–62.
  \NAT@swatrue
* Gürkaynak and
  Wright (2012)

  Gürkaynak, R. S. and J. H. Wright (2012).
  Macroeconomics and the term structure.
  Journal of Economic Literature 50(2), 331––367.
  \NAT@swatrue
* Harrison and
  Kreps (1979)

  Harrison, J. M. and D. M. Kreps (1979).
  Martingales and arbitrage in multiperiod securities markets.
  Journal of Economic Theory 20(3), 381––408.
  \NAT@swatrue
* Harrison and
  Pliska (1981)

  Harrison, J. M. and S. R. Pliska (1981).
  Martingales and stochastic integrals in the theory of continuous
  trading.
   11(3), 215––260.
  \NAT@swatrue
* Heath
  et al. (1992)

  Heath, D., R. Jarrow, and A. Morton (1992).
  Bond pricing and the term structure of interest rates: A new
  methodology.
  Econometrica 60(1), 77–105.
  \NAT@swatrue
* Hu et al. (2020)

  Hu, Y., A. Shirvani, W. B. Lindquist, F. J. Fabozzi, and S. T. Rachev (2020).
  Option pricing incorporating factor dynamics in complete markets.
  Journal of Risk and Financial Management 13(12), 321.
  \NAT@swatrue
* Hull and
  White (1990)

  Hull, J. C. and A. White (1990).
  Pricing interest-rate-derivative securities.
  Review of Financial Studies 3(4), 573––592.
  \NAT@swatrue
* Joslin
  et al. (2014)

  Joslin, S., M. Priebsch, and K. J. Singleton (2014).
  Risk premiums in dynamic term structure models with unspanned macro
  risks.
   69(3), 1197––1233.
  \NAT@swatrue
* Kamara and
  Miller (1995)

  Kamara, A. and T. W. Miller (1995).
  Daily and intradaily tests of European put-call parity.
  Journal of Financial and Quantitative Analysis 30(4),
  519–539.
  \NAT@swatrue
* Ludvigson and
  Ng (2009)

  Ludvigson, S. C. and S. Ng (2009).
  Macro factors in bond risk premia.
  The Review of Financial Studies 22(12),
  5027––5067.
  \NAT@swatrue
* Miltersen
  et al. (1997)

  Miltersen, K. R., K. Sandmann, and D. Sondermann (1997).
  Closed form solutions for term structure derivatives with log-normal
  interest rates.
  Journal of Finance 52(1), 409––430.
  \NAT@swatrue
* Mittnik and
  Rieken (2000)

  Mittnik, S. and S. Rieken (2000).
  Put-call parity and the informational efficiency of the German
  DAX-index options market.
  International Review of Financial Analysis 9(3),
  259–279.
  \NAT@swatrue
* Musiela and
  Rutkowski (2005)

  Musiela, M. and M. Rutkowski (2005).
  Martingale Methods in Financial Modelling (2nd ed.).
  Berlin: Springer.
  \NAT@swatrue
* Nishiotis and
  Rompolis (2019)

  Nishiotis, G. P. and L. S. Rompolis (2019).
  Put-call parity violations and return predictability: Evidence from
  the 2008 short sale ban.
  Journal of Banking & Finance 106, 276–297.
  \NAT@swatrue
* Ofek
  et al. (2004)

  Ofek, E., M. Richardson, and R. F. Whitelaw (2004).
  Limited arbitrage and short sales restrictions: Evidence from the
  options markets.
  Journal of Financial Economics 74(2), 305–342.
  \NAT@swatrue
* Sarno
  et al. (2007)

  Sarno, L., D. L. Thornton, and G. Valente (2007).
  The empirical failure of the expectations hypothesis of the term
  structure of bond yields.
  Journal of Financial and Quantitative Analysis 42(1),
  81–100.
  \NAT@swatrue
* Shreve (2004a)

  Shreve, S. E. (2004a).
  Stochastic Calculus for Finance I: The Binomial Asset Pricing
  Model.
  New York: Springer.
  \NAT@swatrue
* Shreve (2004b)

  Shreve, S. E. (2004b).
  Stochastic Calculus for Finance II: Continuous-Time Models.
  New York: Springer.
  \NAT@swatrue
* Steurer
  et al. (2022)

  Steurer, E., E. J. Fahling, and J. Du (2022).
  Empirical analysis of potential put-call parity arbitrage
  opportunities with particular focus on the Shanghai Stock Exchange 50
  Index.
  Journal of Financial Risk Management 11(1), 66–78.
  \NAT@swatrue
* Vasicek (1977)

  Vasicek, O. (1977).
  An equilibrium characterization of the term structure.
  Journal of Financial Economics 5(2), 177–188.
  \NAT@swatrue
* Wu (2019)

  Wu, L. (2019).
  Interest Rate Modeling: Theory and Practice (2nd ed.).
  Boca Raton, FL: Chapmsn & Hall/CRC.

## Appendix A Supplementary Material

![Refer to caption](Y3D1010.png)

![Refer to caption](Y3D1011.png)

![Refer to caption](Y3D1014.png)

![Refer to caption](Y3D1015.png)

Figure S1: 
3D scatter plots of implied yields Y​(t,T,K)Y(t,T,K)
versus strike KK and maturity TT for the indicated trading days tt.



![Refer to caption](CallContractCounts_20241010.png)

![Refer to caption](CallContractCounts_20241011.png)

![Refer to caption](CallContractCounts_20241014.png)

![Refer to caption](CallContractCounts_20241015.png)

Figure S2: Two-dimensional scatter plots of the number of ˆSPX call contracts versus time
to maturity TT for the option chains of 10–15 October, 2024.

![Refer to caption](YTLS_1010_box.png)


Figure S3: Box-whisker summaries of the distributions of the implied yield Y​(t,T)Y(t,T) with maturity
time TT (in days). The panels summarize (left) short–term and (right) long–term contracts.
For better representation, the negative range of the y−y-axis has been truncated;
consequently, negative outliers for small values of TT are not visible.



![Refer to caption](YTLS_1011_box.png)

![Refer to caption](YTLS_1014_box.png)

![Refer to caption](YTLS_1015_box.png)

Figure S4: 
(cont.)



![Refer to caption](Ymed_short_1010.png)

![Refer to caption](Ymed_short_1011.png)

![Refer to caption](Ymed_short_1014.png)

![Refer to caption](Ymed_short_1015.png)

![Refer to caption](Ymed_long_1010.png)

![Refer to caption](Ymed_long_1011.png)

![Refer to caption](Ymed_long_1014.png)

![Refer to caption](Ymed_long_1015.png)

Figure S5: (solid line) Y(med)​(t,T)Y^{(\text{med})}(t,T) and (dashed line) Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T) (PCHIP fit)
as a function of time to maturity TT for t=t= 10–15 October, 2024.
(top row) Short–term contracts. (bottom row) Long–term contracts.
Given the range of the y−y-axis values, it is difficult to see the variation in Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T)
with TT for large TT that is apparent in Fig. [4](https://arxiv.org/html/2512.10823v1#S4.F4 "Figure 4 ‣ 4.2 Median-Strike Aggregation of Implied Option Yields ‣ 4 Empirical Comparison of Yield ‣ Option-Implied Zero-Coupon Yields: Unifying Bond and Equity Markets").

![Refer to caption](YMLS_1010_box.png)


Figure S6: Box-whisker summaries of the distributions of the implied yield Y​(t,M)Y(t,M) with moneyness
M=K/StM=K/S\_{t} for 10 October, 2024. The panels summarize (top) short–term and (bottom) long–term contracts.
For better representation, the negative range of the y−y-axis has been truncated



![Refer to caption](YMLS_1011_box.png)

![Refer to caption](YMLS_1014_box.png)

Figure S7: (cont.)

![Refer to caption](YMLS_1015_box.png)


Figure S8: (cont.)



![Refer to caption](YATM_short_1010.png)

![Refer to caption](YATM_short_1011.png)

![Refer to caption](YATM_short_1014.png)

![Refer to caption](YATM_short_1015.png)

![Refer to caption](YATM_long_1010.png)

![Refer to caption](YATM_long_1011.png)

![Refer to caption](YATM_long_1014.png)

![Refer to caption](YATM_long_1015.png)

Figure S9: (solid line) Y(ATM)​(t,T)Y^{(\text{ATM})}(t,T) and (dashed line) Y(mkt)​(t,T)Y^{(\text{mkt})}(t,T) (PCHIP fit)
as a function of time to maturity TT for t=t= 10–15 October, 2024.
(top row) Short–term contracts. (bottom row) Long–term contracts.