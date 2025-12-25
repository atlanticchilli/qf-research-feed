---
authors:
- Wenqing Zhang
doc_id: arxiv:2512.21115v1
family_id: arxiv:2512.21115
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Discrete-time asset price bubbles with short sales prohibitions under model
  uncertainty
url_abs: http://arxiv.org/abs/2512.21115v1
url_html: https://arxiv.org/html/2512.21115v1
venue: arXiv q-fin
version: 1
year: 2025
---


Wenqing Zhang
Corresponding author, School of Mathematics, Shandong University, PR China, (zhangwendy@mail.sdu.edu.cn).

###### Abstract

In this study, we investigate asset price bubbles in a discrete-time, discrete-state market under model uncertainty and short sales prohibitions.
Building on a new fundamental theorem of asset pricing and a superhedging duality in this setting, we introduce a notion of bubble based on a novel definition of the fundamental price, and analyze their types and characterization.
We show that two distinct types of bubbles arise, depending on the maturity structure of the asset.
For assets with bounded maturity and no dividend payments, the GG-supermartingale property of prices provides a necessary and sufficient condition for the existence of bubbles.
In contrast, when maturity is unbounded, the infi-supermartingale property yields a necessary condition, while the GG-supermartingale property remains sufficient.
Moreover, there is no bubble under a strengthened no dominance condition.
As applications, we examine price bubbles for several standard contingent claims.
We show that put-call parity generally fails for fundamental prices, whereas it holds for market prices under no dominance assumption.
Furthermore, we establish bounds for the fundamental and market prices of American call options in terms of the corresponding European call prices, adjusted by the associated bubble components.

KEYWORDS: Asset price bubbles; Discrete time and states; Sublinear expectation; Short sales prohibitions; Contingent claims

## 1 Introduction

Asset price bubbles have long attracted the attention of economists.
Classical episodes, such as the Dutch Tulipmania, the Mississippi Bubble, and the South Sea Bubble, have been extensively documented and analyzed (Garber, [1990](https://arxiv.org/html/2512.21115v1#bib.bib13)).
More recently, the bursting of the housing price bubble and its connection to the subprime mortgage crisis has renewed interest in bubble phenomena within both the financial industry and academic research (Jarrow and Protter, [2009](https://arxiv.org/html/2512.21115v1#bib.bib22); Jarrow et al., [2011a](https://arxiv.org/html/2512.21115v1#bib.bib21)).
In general terms, a bubble is a deviation between the trading price of an asset and its underlying value.
The economic literature has examined this deviation from various perspectives in an attempt to explain why and under what conditions bubble arise.
For example, Harrison and Kreps ([1978](https://arxiv.org/html/2512.21115v1#bib.bib14)) showed that speculative trading may cause prices to persistently exceed fundamental values.
Other mechanisms contributing to bubble formation include traders’ myopic behavior (Tirole, [1982](https://arxiv.org/html/2512.21115v1#bib.bib46)), overconfidence (Scheinkman and Xiong, [2003](https://arxiv.org/html/2512.21115v1#bib.bib45)), trend-chasing behavior (Föllmer et al., [2005](https://arxiv.org/html/2512.21115v1#bib.bib11)), and the presence of noise traders (De Long et al., [1990](https://arxiv.org/html/2512.21115v1#bib.bib6)).

In recent decades, a growing literature has leveraged tools from mathematical finance, particularly the theory of (local) martingale, to analyze asset price bubbles.
The martingale approach originated from the seminal work of Loewenstein and Willard ([2000](https://arxiv.org/html/2512.21115v1#bib.bib31)), who introduced a probabilistic framework for studying bubbles, and was further advanced by Cox and Hobson ([2005](https://arxiv.org/html/2512.21115v1#bib.bib5)).
Subsequently contributed include Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)), who considered markets with time-varying local martingale measures, leading to results that differ markedly from classical theory, and Biagini et al. ([2014](https://arxiv.org/html/2512.21115v1#bib.bib3)), who analyzed a flow of equivalent martingale measures under which an asset price initially behaves as a submartingale, later becomes a supermartingale, and eventually returns to zero.
Parallel to these developmeants, numerous studies investigate bubbles across various asset classes, including forwards and futures (Jarrow and Protter, [2009](https://arxiv.org/html/2512.21115v1#bib.bib22)), equities (Jarrow et al., [2011b](https://arxiv.org/html/2512.21115v1#bib.bib27)), foreign exchange (Jarrow and Protter, [2011](https://arxiv.org/html/2512.21115v1#bib.bib26)), bonds (Bilina-Falafala et al., [2016](https://arxiv.org/html/2512.21115v1#bib.bib4)), options (Jarrow and Kwok, [2021](https://arxiv.org/html/2512.21115v1#bib.bib25)), and so on (Jarrow, [2016](https://arxiv.org/html/2512.21115v1#bib.bib18)).

Discrete-time frameworks also play a prominent role in the study of financial markets, owing to their structural simplicity and their closer correspondence to empirically observed price dynamics.
Their tractability makes them especially suitable for modeling periodic collapses and drawdowns characteristic of bubble behavior (Schatz and Sornette, [2020](https://arxiv.org/html/2512.21115v1#bib.bib44)).
From the perspective of financial mathematics, discrete-time models require special attention because strict local martingales and singular processes, central to many continuous-time bubble models, cannot arise; in discrete time, any nonnegative local martingale is necessarily a true martingale (Jarrow and Protter, [2012](https://arxiv.org/html/2512.21115v1#bib.bib20); Herdegen and Kreher, [2022](https://arxiv.org/html/2512.21115v1#bib.bib15)).
This necessitates a separate investigation of bubble phenomena in discrete time.
Indeed, Santos and Woodford ([1997](https://arxiv.org/html/2512.21115v1#bib.bib43)) provided a systematic analysis of the conditions under which rational bubbles emerge in competitive equilibria;
Fukuta ([1998](https://arxiv.org/html/2512.21115v1#bib.bib12)) studied incomplete bursting bubbles and their interrelationships;
and Herdegen and Kreher ([2022](https://arxiv.org/html/2512.21115v1#bib.bib15)) proposed a new definition of bubbles in discrete-time models based on loss of mass in discounted asset prices.

In addition to model structure, short sales restrictions paly a significant role in financial markets, as they help stabilize prices during financial crises and widely implemented in most emerging economies (Pulido, [2014](https://arxiv.org/html/2512.21115v1#bib.bib42)).
However, short sales constraints may also facilitate the formation and persistence of asset price bubbles by impeding arbitrage and contributing to overvaluation (Miller, [1977](https://arxiv.org/html/2512.21115v1#bib.bib32); Jarrow, [2019](https://arxiv.org/html/2512.21115v1#bib.bib19)), and the persistence of such bubbles has been explored in Lim ([2011](https://arxiv.org/html/2512.21115v1#bib.bib30)).
In addition, Hong et al. ([2006](https://arxiv.org/html/2512.21115v1#bib.bib17)) examined the relationship between asset float and bubbles under short sales constraints;
and Kocherlakota ([2008](https://arxiv.org/html/2512.21115v1#bib.bib28)) constructed equilibrium allocations exhibiting bubbles induced by short sales limitations.
Moreover, in many continuous-time models, admissibility conditions requiring wealth processes to remain bounded from below effectively impose implicit short sale constraints, permitting bubble phenomena in otherwise arbitrage-free settings (Jarrow et al., [2010](https://arxiv.org/html/2512.21115v1#bib.bib24)).

Despite the extensive literature on bubbles, relatively little attention has been paid to Knightian uncertainty, an intrinsic feature of modern financial markets.
Knightian uncertainty can invalidate the classical risk-neutral pricing framework, potentially causing abtupt asset price movements without corresponding changes in fundamentals (Epstein and Wang, [1995](https://arxiv.org/html/2512.21115v1#bib.bib10)).
To model such uncertainty, Peng ([1997](https://arxiv.org/html/2512.21115v1#bib.bib33), [2004](https://arxiv.org/html/2512.21115v1#bib.bib35), [2006](https://arxiv.org/html/2512.21115v1#bib.bib36), [2008](https://arxiv.org/html/2512.21115v1#bib.bib37), [2019](https://arxiv.org/html/2512.21115v1#bib.bib38)) introduced sublinear expectation theory, replacing the traditional single probability measure with a family of probability measures, thereby capturing both mean and volatility uncertainty.
This framework has since been widely applied in financial modeling (Epstein and Ji, [2013](https://arxiv.org/html/2512.21115v1#bib.bib8), [2014](https://arxiv.org/html/2512.21115v1#bib.bib9); Peng and Yang, [2022](https://arxiv.org/html/2512.21115v1#bib.bib39); Peng et al., [2023](https://arxiv.org/html/2512.21115v1#bib.bib40)).
Within the context of asset price bubbles, Biagini and Mancin ([2017](https://arxiv.org/html/2512.21115v1#bib.bib2)) offered the first robust definition of asset price bubbles under model uncertainty, establishing fundamental properties of the bubble and analyzing how bubble existence depends on the investor’s set of priors.
In contrast, our framework incorporates not only model uncertainty but also explicit short-sales constraints, leading to several novel and distinct conclusions.

In this paper, we investigate discrete-time asset price bubbles under short selling constraints in the presence of model uncertainty.
We consider a discrete state space Ω={ωk}k∈ℤ+\Omega=\{\omega\_{k}\}\_{k\in\mathbb{Z}^{+}}, and represent model uncertainty by a family of probability measures 𝒫\mathcal{P}. Time is indexed discretely.
For the traded asset, we introduce the discounted wealth process WW associated with the market price StS\_{t}, the discounted dividend process D^t\hat{D}\_{t} and the discounted terminal payoff X^τ\hat{X}\_{\tau}. Specifically,

|  |  |  |
| --- | --- | --- |
|  | Wt=St​I{t<τ}+∑u=0t∧τD^u+X^τ​I{τ≤t}.W\_{t}=S\_{t}I\_{\{t<\tau\}}+\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq t\}}. |  |

Let π\pi denote the trading strategy in the asset, which is restricted to be nonnegative due to the short selling prohibition.
The corresponding discounted value process is then Vt=πt​WtV\_{t}=\pi\_{t}W\_{t}.
Within this framework, we establish a fundamental theorem of asset pricing under model uncertainty. We show that the absence of arbitrage is equivalent to the requirement that

|  |  |  |
| --- | --- | --- |
|  | Wt≥supQ∈𝒬EQ​[WT∣ℱt],W\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{T}\mid\mathcal{F}\_{t}], |  |

that is, WW must be a GG-supermartingale with respect to the set of priors 𝒬\mathcal{Q}.
Building on this result, we derive a super-hedging theorem under short selling constraints and model uncertainty, demonstrating that the minimal super-hedging price of a contingent claim is given by the robust supremum expectation supQ∈𝒬EQ​[f​(ST)]\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})].

Building on the super-hedging price, we introduce a new notion of fundamental price S∗S^{\*} by constructing a super-hedging portfolio for the asset’s cash flows. Formally,

|  |  |  |
| --- | --- | --- |
|  | St∗=supQ∈𝒬EQ[∑u=tτD^u+X^τI{τ<∞}|ℱt].S\_{t}^{\*}=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]. |  |

We first establish that this definition is well-defined, and then analyze its asymptotic behavior.
In particular, we show that the process (St∗)t≥0(S\_{t}^{\*})\_{t\geq 0} converges to 0 q.s.
Using this result, we derive the convergence properties of the associated fundamental wealth process W∗W^{\*} and identify its GG-martingale structure.
The asset price bubble β\beta is then defined as the difference between the market price and the fundamental price:
βt=St−St∗.\beta\_{t}=S\_{t}-S\_{t}^{\*}.
We obtain two distinct forms of bubble dynamics depending on the maturity τ\tau. If τ\tau is bounded, then βt\beta\_{t} is a GG-supermartingale, that is,
βt≥supQ∈𝒬EQ​[βT∣ℱt].\beta\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}].
When τ\tau is unbounded, either allowing P​(τ=∞)>0P(\tau=\infty)>0 or satisfying P​(τ<∞)=1P(\tau<\infty)=1 while remaining unbounded, the bubble process βt\beta\_{t} instead satisfies an infi-supermartingale property, that is, βt≥infQ∈𝒬EQ​[βT∣ℱt].\beta\_{t}\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}].
Several illustrative examples are provided to clarify these behaviors.
We then investigate structural conditions on market prices that characterize the existence of bubbles.
When τ\tau is bounded and the asset pays no dividends, we show that the GG-supermartingale property of the asset is both necessary and sufficient for a bubble to arise.
In contrast, when τ\tau is unbounded, the infi-supermartingale condition is necessary, while the GG-supermartingale condition becomes sufficient.
These results are illustrated in Figure [1](https://arxiv.org/html/2512.21115v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty").

![Refer to caption](bubble.png)


Figure 1: The necessary and sufficient conditions for bubbles

They lead to the following key properties of bubbles: (i) βt≥0\beta\_{t}\geq 0 for all tt; (ii) βτ​I{τ<∞}=0\beta\_{\tau}I\_{\{\tau<\infty\}}=0; (iii) Under bounded τ\tau, if βt=0\beta\_{t}=0 then βT=0\beta\_{T}=0, but this does not hold when τ\tau is unbounded.
Furthermore, by imposing a stronger no dominance condition under model uncertainty, we prove that bubbles cannot exist in such markets.

We then turn to the analysis of bubbles in standard contingent claims, which may originate not only from the underlying asset but also from the market prices of the claims themselves.
Throughout this section, we assume that the asset pays no dividends over the finite horizon [0,T][0,T] with τ>T\tau>T q.s. for some T∈ℝ+T\in\mathbb{R}\_{+}.
After deriving the fundamental price of forward and European options, we show that put-call parity fails at the level of fundamental prices. Specifically

|  |  |  |
| --- | --- | --- |
|  | CtE⁣∗​(K)−PtE⁣∗​(K)≤Ft∗​(K).C\_{t}^{E\*}(K)-P\_{t}^{E\*}(K)\leq F\_{t}^{\*}(K). |  |

When the no dominant condition is additionally imposed, the put-call parity holds for market prices.
We also establish a relationship among the bubbles of various contingent claims:
δtS=δtF≤δtE​C−δtE​P.\delta\_{t}^{S}=\delta\_{t}^{F}\leq\delta\_{t}^{EC}-\delta\_{t}^{EP}.
For American call options, the fundamental price is bounded below by the fundamental price of the corresponding European call and bounded above by the sum of the European call’s fundamental price and the bubble of underlying asset.
This implies that the incremental fundamental value attributable to early exercise cannot exceed the magnitude of the underlying asset’s bubble.
Analogous bounds hold for market prices: the price of an American all can be controlled by the European call price adjusted upward or downward by the relevant bubble components, that is

|  |  |  |
| --- | --- | --- |
|  | δtA​C−δtE​C≤CtA​(K)−CtE​(K)≤δtA​C−δtE​P.\delta\_{t}^{AC}-\delta\_{t}^{EC}\leq C\_{t}^{A}(K)-C\_{t}^{E}(K)\leq\delta\_{t}^{AC}-\delta\_{t}^{EP}. |  |

The main contributions of this paper are threefold:

(i). Incorporating short selling constraints and model uncertainty, we establish a new fundamental theorem of asset pricing and a corresponding super-hedging theorem.
In a discrete time and states framework, we prove that the GG-supermartingale property of the wealth process WW is equivalent to the absence of arbitrage under model uncertainty.
Moreover, the minimal super-hedging cost of a contingent claim is given by the supremum expectation over the set of probability measures 𝒬\mathcal{Q}.

(ii). Building on a new definition of the asset’s fundamental price in the bubble, we analyze the types and characteristics of bubbles, and revisit their existence under a stronger no dominance condition.
Using the super-hedging theorem, we define the fundamental price and establish its well-defined and convergence properties.
Two distinct types of bubbles emerge in this framework, each characterized by specific martingale properties of the asset’s market price.
Under the stronger no dominance condition, we show that bubbles cannot arise.

(iii). We study bubble components in the prices of several standard contingent claims and investigate the relationships between their fundamental and market prices.
For forward contracts and European options, we demonstrate that put-call parity fails for fundamental prices, while it is restored for market prices under the no-dominance assumption.
Furthermore, both the fundamental and market prices of American call options can be bounded by the corresponding European call prices, adjusted by the addition or subtraction of the relevant bubbles.

The remainder of this paper is organized as follows.
Section [2](https://arxiv.org/html/2512.21115v1#S2 "2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") introduces the basic financial market framework and establishes the fundamental theorem of asset pricing together with the super-hedging theorem under short sales prohibitions and model uncertainty.
After providing the fundamental price of asset in the concept of asset bubbles, we provides a detailed analysis of bubbles’ types and characterizations in Section [3](https://arxiv.org/html/2512.21115v1#S3 "3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty").
Subsequently, we examine some standard contingent claims bubbles in Section [4](https://arxiv.org/html/2512.21115v1#S4 "4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty").
Finally, Section [5](https://arxiv.org/html/2512.21115v1#S5 "5 Conclusion ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") concludes the main result in this paper.

## 2 Model setting

### 2.1 Financial market

We consider a discrete sample space Ω={ωk}k∈ℤ+\Omega=\{\omega\_{k}\}\_{k\in\mathbb{Z}^{+}}, where ℤ+\mathbb{Z}^{+} denotes the set of positive integers.
To model Knightian uncertainty in the financial market, we introduce a family of probability measures 𝒫\mathcal{P} to describe the uncertainty law of the nonlinear randomized trial, that is P​(ω)∈𝒫P(\omega)\in\mathcal{P} for all ω∈Ω\omega\in\Omega (see Yang and Zhang ([2024b](https://arxiv.org/html/2512.21115v1#bib.bib48)) for more details).
The market consists of a risky asset and a money market account.
Let S=(St)t≥0S=(S\_{t})\_{t\geq 0} denote the price process of the risky asset, where St≥0S\_{t}\geq 0 and StS\_{t} reflects the ex-dividend price at time tt.
Time evolves on the discrete horizon [0,T¯][0,\bar{T}], where T¯\bar{T} is either a finite integer TT or ∞\infty.
For each P∈𝒫P\in\mathcal{P}, let ℱtP:=σ​(Su, 0≤u≤t)\mathcal{F}\_{t}^{P}:=\sigma(S\_{u},\ 0\leq u\leq t) be the raw filtration generated by the price process, and let ℱtP,c\mathcal{F}\_{t}^{P,c} be its PP-completion. we define the unified filtration

|  |  |  |
| --- | --- | --- |
|  | ℱt:=⋂P∈𝒫FtP,c,\mathcal{F}\_{t}:=\bigcap\_{P\in\mathcal{P}}F\_{t}^{P,c}, |  |

ensuring that all random variables and stopping times introduced below are simultaneously measurable under every prior P∈𝒫P\in\mathcal{P}.
Let τ>0\tau>0 be a stopping time with respect to (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0}, representing the maturity (or default/liquidation time) of the risky asset. Typical economic events triggering τ\tau include bankruptcy, acquisition, merger, or antitrust breakup (Protter ([2013](https://arxiv.org/html/2512.21115v1#bib.bib41))).
Let (Dt)0≤t<τ(D\_{t})\_{0\leq t<\tau} denote the cumulative dividend process, and let XτX\_{\tau} denote the terminal payoff or liquidation value at time τ\tau, with Dt≥0D\_{t}\geq 0 and Xτ≥0X\_{\tau}\geq 0.
The money market account B=(Bt)t≥0B=(B\_{t})\_{t\geq 0} satisfies B0=1B\_{0}=1 and

|  |  |  |
| --- | --- | --- |
|  | Bt=(1+r0)​(1+r1)​⋯​(1+rt),t≥0,B\_{t}=(1+r\_{0})(1+r\_{1})\cdots(1+r\_{t}),\quad t\geq 0, |  |

where rt≥0r\_{t}\geq 0 denotes the spot interest rate over the interval (t,t+1](t,t+1].
Define the discounted wealth process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt=S^t​I{t<τ}+∑u=0t∧τD^u+X^τ​I{τ≤t},t≥0,W\_{t}=\hat{S}\_{t}I\_{\{t<\tau\}}+\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq t\}},\quad t\geq 0, |  | (2.1) |

where S^t=St/Bt,D^u=Du/Bu,X^τ=Xτ/Bτ\hat{S}\_{t}=S\_{t}/B\_{t},\ \hat{D}\_{u}=D\_{u}/B\_{u},\ \hat{X}\_{\tau}=X\_{\tau}/B\_{\tau}. Clearly, Wt≥0W\_{t}\geq 0 for all tt.

A trading strategy consists of an adapted pair of processes (πt,ηt)t≥0(\pi\_{t},\eta\_{t})\_{t\geq 0}, where πt\pi\_{t} and ηt\eta\_{t} denote the holdings in the risky asset and the money market account, respectively.
Short selling of the risky asset is prohibited, so we impose π≥0\pi\geq 0.
The associated discounted portfolio value is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=πt​St​I{t<τ}+ηt,t≥0.V\_{t}=\pi\_{t}S\_{t}I\_{\{t<\tau\}}+\eta\_{t},\quad t\geq 0. |  | (2.2) |

A strategy (π,η)(\pi,\eta) is self-financing if purchases of one asset are financed exclusively through sales of the other. Equivalently (Jarrow et al., [2010](https://arxiv.org/html/2512.21115v1#bib.bib24)), the portfolio value satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=πt​Wt,t≥0.V\_{t}=\pi\_{t}W\_{t},\quad t\geq 0. |  | (2.3) |

Using the representation of WtW\_{t}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=πt​S^t​I{t<τ}+πt​∑u=0t∧τD^u+πt​X^τ​I{τ≤t}=πt​S^t​I{t<τ}+ηt,t≥0,V\_{t}=\pi\_{t}\hat{S}\_{t}I\_{\{t<\tau\}}+\pi\_{t}\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\pi\_{t}\hat{X}\_{\tau}I\_{\{\tau\leq t\}}=\pi\_{t}\hat{S}\_{t}I\_{\{t<\tau\}}+\eta\_{t},\quad t\geq 0, |  | (2.4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt=πt​∑u=0t∧τD^u+πt​X^τ​I{τ≤t}.\eta\_{t}=\pi\_{t}\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\pi\_{t}\hat{X}\_{\tau}I\_{\{\tau\leq t\}}. |  | (2.5) |

Thus, in the self-financing setting, η\eta is completely determined by π\pi, and therefore we henceforth represent trading strategies using only π\pi.

###### Remark 2.1.

As noted by Kwok ([2008](https://arxiv.org/html/2512.21115v1#bib.bib29)), a trading strategy π\pi is self-financing if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=V0+Gt,t≥0V\_{t}=V\_{0}+G\_{t},\quad t\geq 0 |  | (2.6) |

where Gt=∑u=1tπu​Δ​Wu=∑u=1tπu​(Wu−Wu−1)G\_{t}=\sum\_{u=1}^{t}\pi\_{u}\Delta W\_{u}=\sum\_{u=1}^{t}\pi\_{u}(W\_{u}-W\_{u-1}) denotes the cumulative trading gain.
For a self-financing trading strategy, (πt+1−πt)​Wt=0(\pi\_{t+1}-\pi\_{t})W\_{t}=0.
Combining equations ([2.1](https://arxiv.org/html/2512.21115v1#S2.E1 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), ([2.2](https://arxiv.org/html/2512.21115v1#S2.E2 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) and ([2.5](https://arxiv.org/html/2512.21115v1#S2.E5 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), we observe that

|  |  |  |
| --- | --- | --- |
|  | Vt−V0=πt​Wt−π0​W0=∑u=1tπu​Δ​Wu=Gt,t≥0,V\_{t}-V\_{0}=\pi\_{t}W\_{t}-\pi\_{0}W\_{0}=\sum\_{u=1}^{t}\pi\_{u}\Delta W\_{u}=G\_{t},\quad t\geq 0, |  |

showing that the characterizations Vt=πt​WtV\_{t}=\pi\_{t}W\_{t} and Vt=V0+GtV\_{t}=V\_{0}+G\_{t} are equivalent.
Thus, both definitions describe the same class of self-financing trading strategies.

### 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty

Prior to analyzing price bubbles, we first establish the fundamental theorem of asset pricing under model uncertainty and short sales constraints.
To this end, we introduce the notion of arbitrage under model uncertainty using the symbols in this paper, following Definition 3.1 in Yang and Zhang ([2024a](https://arxiv.org/html/2512.21115v1#bib.bib47)), but rewritten using the notation of this paper.

###### Definition 2.1.

A trading strategy π\pi is called an arbitrage over period [0,T][0,T] under model uncertainty if:

(i) π\pi is self-financing;

(ii) V0=0V\_{0}=0;

(iii) VT≥0V\_{T}\geq 0 and supP∈𝒫EP​[VT]>0\sup\_{P\in\mathcal{P}}E\_{P}[V\_{T}]>0,
  
where EP​[⋅]E\_{P}[\cdot] denotes expectation under actual probability measure P∈𝒫P\in\mathcal{P}, and supP∈𝒫P​(ω)>0\sup\_{P\in\mathcal{P}}P(\omega)>0 for all ω∈Ω\omega\in\Omega.
The market is said to satisfy no arbitrage under model uncertainty if no trading strategy π\pi simultaneously satisfies (i)-(iii).

###### Remark 2.2.

Using Remark [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmremark1 "Remark 2.1. ‣ 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), an equivalent formulation is obtained: a self-financing strategy π\pi is an arbitrage opportunity if and only if (i)’ GT≥0G\_{T}\geq 0 and (ii)’ supP∈𝒫EP​[GT]>0\sup\_{P\in\mathcal{P}}E\_{P}[G\_{T}]>0, with supP∈𝒫P​(ω)>0\sup\_{P\in\mathcal{P}}P(\omega)>0 for all ω∈Ω\omega\in\Omega.

To ensure absence of arbitrage in markets with short sales prohibitions, Protter ([2013](https://arxiv.org/html/2512.21115v1#bib.bib41)) introduced a risk neutral probability measure QQ satisfying:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt≥EQ​[WT∣ℱt],0≤t≤T.W\_{t}\geq E\_{Q}[W\_{T}\mid\mathcal{F}\_{t}],\quad 0\leq t\leq T. |  | (2.7) |

Under model uncertainty, however, a single risk neutral probability measure QQ is no longer adequate.
Instead, we consider a family of probability measures 𝒬\mathcal{Q}, which induces a corresponding family of linear expectations EQ​[⋅],Q∈𝒬E\_{Q}[\cdot],\ Q\in\mathcal{Q}.
This naturally leads to the upper envelope over these expectations, following the approach in Yang and Zhang ([2024a](https://arxiv.org/html/2512.21115v1#bib.bib47)). We thus introduce the notion of a strong risk neutral nonlinear expectation.

###### Definition 2.2.

Under model uncertainty and short sales prohibitions, EQ​[⋅],Q∈𝒬E\_{Q}[\cdot],Q\in\mathcal{Q} is called a strong risk neutral nonlinear expectation if

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt≥supQ∈𝒬EQ​[WT∣ℱt],0≤t≤T,W\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{T}\mid\mathcal{F}\_{t}],\quad 0\leq t\leq T, |  | (2.8) |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.

###### Remark 2.3.

Following the terminology of Peng ([2019](https://arxiv.org/html/2512.21115v1#bib.bib38)), the process W=(Wt)0≤t≤TW=(W\_{t})\_{0\leq t\leq T} satisfying ([2.8](https://arxiv.org/html/2512.21115v1#S2.E8 "In Definition 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) is called a GG-supermartingale.
If the risky asset SS pays no dividends, then Definition [2.2](https://arxiv.org/html/2512.21115v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | St≥supQ∈𝒬EQ​[ST∣ℱt],0≤t≤T<τ,S\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}\mid\mathcal{F}\_{t}],\qquad 0\leq t\leq T<\tau, |  | (2.9) |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.
Equation ([2.9](https://arxiv.org/html/2512.21115v1#S2.E9 "In Remark 2.3. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) coincides with Definition 3.4 of Yang and Zhang ([2024a](https://arxiv.org/html/2512.21115v1#bib.bib47)).
In the absence of model uncertainty, Definition [2.2](https://arxiv.org/html/2512.21115v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") reduces to the classical notion of a supermartingale, and ([2.8](https://arxiv.org/html/2512.21115v1#S2.E8 "In Definition 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) coincides with ([2.7](https://arxiv.org/html/2512.21115v1#S2.E7 "In 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).

We now establish the fundamental theorem of asset pricing under model uncertainty and short-sale constraints, by exploiting the relationship between no arbitrage and the existence of a strong risk neutral nonlinear expectation.

###### Theorem 2.1.

Under short sales prohibitions, the market satisfies no arbitrage under model uncertainty if and only if there exists a strong risk neutral nonlinear expectation.

###### Proof.

To prove sufficiency, suppose π\pi satisfies VT≥0V\_{T}\geq 0 and supP∈𝒫Ep​[VT]>0\sup\_{P\in\mathcal{P}}E\_{p}[V\_{T}]>0. Since π\pi is self-financing and supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega, we have

|  |  |  |
| --- | --- | --- |
|  | V0=π0​W0≥supQ∈𝒬EQ​[πT​WT]=supQ∈𝒬EQ​[VT]>0.V\_{0}=\pi\_{0}W\_{0}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[\pi\_{T}W\_{T}]=\sup\_{Q\in\mathcal{Q}}E\_{Q}[V\_{T}]>0. |  |

contradicting V0=0V\_{0}=0. Thus, arbitrage is impossible.

For necessity, consider first a single-period model. Define

|  |  |  |
| --- | --- | --- |
|  | U1={(−V0V1​(ω1)⋯V1​(ωk)⋯)⊤:V satisfies no-arbitrage},U\_{1}=\left\{\begin{pmatrix}-V\_{0}&V\_{1}(\omega\_{1})&\cdots&V\_{1}(\omega\_{k})&\cdots\end{pmatrix}^{\top}:\ \text{$V$ satisfies no-arbitrage}\right\}, |  |

|  |  |  |
| --- | --- | --- |
|  | U2={(x0x1⋯xk⋯)⊤:xi≥0,for all​i∈ℤ+}.U\_{2}=\left\{\begin{pmatrix}x\_{0}&x\_{1}&\cdots&x\_{k}&\cdots\end{pmatrix}^{\top}:x\_{i}\geq 0,\quad\text{for all}\ i\in\mathbb{Z}^{+}\right\}. |  |

No-arbitrage implies U1∩U2={𝟎}U\_{1}\cap U\_{2}=\{\bf{0}\}.
By the Hahn-Banach separating theorem (Aliprantis and Border, [2006](https://arxiv.org/html/2512.21115v1#bib.bib1)), there exist a hyperplane ff and constant aa separating U1U\_{1} and U2∖{𝟎}U\_{2}\setminus\{\bf{0}\}:

|  |  |  |
| --- | --- | --- |
|  | f⋅x>a≥f⋅y,x∈U2∖{0},y∈U1.f\cdot x>a\geq f\cdot y,\quad x\in U\_{2}\setminus\{\textbf{0}\},\ y\in U\_{1}. |  |

Since U1U\_{1} is a linear space and therefore closed under scalar multiplication, it is obviously that a=0a=0.
From f⋅x>0f\cdot x>0 for x∈U2∖{𝟎}x\in U\_{2}\setminus\{{\bf 0}\}, one can infer that

|  |  |  |
| --- | --- | --- |
|  | Q​(ωk):=fkf0>0,fj,j=0,1,⋯,K​ is the entry of ​f.Q(\omega\_{k}):=\frac{f\_{k}}{f\_{0}}>0,\quad f\_{j},j=0,1,\cdots,K\text{ is the entry of }f. |  |

Taking condition f⋅y≤0,y∈U1f\cdot y\leq 0,\ y\in U\_{1} into equation ([2.2](https://arxiv.org/html/2512.21115v1#S2.E2 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), we have

|  |  |  |
| --- | --- | --- |
|  | π0​S0≥∑k=1∞Q​(ωk)​π0​S1​(ωk)​I{1<τ}+(∑k=1∞Q​(ωk)−1)​η0.\pi\_{0}S\_{0}\geq\sum\_{k=1}^{\infty}Q(\omega\_{k})\pi\_{0}S\_{1}(\omega\_{k})I\_{\{1<\tau\}}+(\sum\_{k=1}^{\infty}Q(\omega\_{k})-1)\eta\_{0}. |  |

Let π0=0\pi\_{0}=0 and η0\eta\_{0} can be positive or negative, we obtain ∑k=1∞Q​(ωk)=1\sum\_{k=1}^{\infty}Q(\omega\_{k})=1, indicating that QQ is a probability measure.
Collecting all such probability measures yields a family 𝒬\mathcal{Q} with supQ∈𝒬Q​(ω)≥Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)\geq Q(\omega)>0 for all ω∈Ω\omega\in\Omega.
Applying f⋅y≤0,y∈U1f\cdot y\leq 0,\ y\in U\_{1} to ([2.3](https://arxiv.org/html/2512.21115v1#S2.E3 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) gives W0≥EQ​[W1]W\_{0}\geq E\_{Q}[W\_{1}] for all Q∈𝒬Q\in\mathcal{Q}, hence

|  |  |  |
| --- | --- | --- |
|  | W0≥supQ∈𝒬EQ​[W1], where ​supQ∈𝒬Q​(ω)>0,∀ω∈Ω.W\_{0}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{1}],\quad\text{ where }\sup\_{Q\in\mathcal{Q}}Q(\omega)>0,\ \forall\omega\in\Omega. |  |

For the multi-period case, subadditivity of sublinear expectation yields

|  |  |  |
| --- | --- | --- |
|  | supQ∈𝒬EQ​[WT−Wt∣ℱt]=supQ∈𝒬EQ​[∑u=tT−1(Wu+1−Wu)∣ℱu]≤∑u=tT−1supQ∈𝒬EQ​[Wu+1−Wu∣ℱu]≤0,\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{T}-W\_{t}\mid\mathcal{F}\_{t}]=\sup\_{Q\in\mathcal{Q}}E\_{Q}[\sum\_{u=t}^{T-1}(W\_{u+1}-W\_{u})\mid\mathcal{F}\_{u}]\leq\sum\_{u=t}^{T-1}\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{u+1}-W\_{u}\mid\mathcal{F}\_{u}]\leq 0, |  |

for all 0≤t≤T0\leq t\leq T.
Thus a strong risk neutral nonlinear expectation exists, completing the proof.
∎

###### Remark 2.4.

Theorem [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") shows that a strong risk neutral nonlinear expectation is both necessary and sufficient for no arbitrage under model uncertainty.
This strengthens the result in Yang and Zhang ([2024a](https://arxiv.org/html/2512.21115v1#bib.bib47)), where the strong risk neutral nonlinear expectation is only sufficient, and necessity relies on a weak version.
On the other hand, the family 𝒬\mathcal{Q} in Theorem [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") is more restrictive than in Yang and Zhang ([2024a](https://arxiv.org/html/2512.21115v1#bib.bib47)): here 𝒬\mathcal{Q} consists precisely of those probability measures under which WW is a supermartingale, whereas no such structural requirement is imposed in Yang and Zhang ([2024a](https://arxiv.org/html/2512.21115v1#bib.bib47)).

As an immediate corollary of the fundamental theorem of asset pricing in Theorem [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we study the super-hedging problem for a contingent claim f​(S)f(S) under short sales constraints and model uncertainty.
We construct a super-hedging portfolio consisting of a money market account and risky assets such that its terminal value dominates f​(S)f(S) quasi-surely, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | x+π⋅W0T≥f​(ST),𝒫​-q.s.,x+\pi\cdot W\_{0}^{T}\geq f(S\_{T}),\quad\mathcal{P}\text{-q.s.}, |  | (2.10) |

where π⋅W0T:=∑u=0Tπu​Δ​Wu=∑u=0Tπu​(Wu−Wu−1)\pi\cdot W\_{0}^{T}:=\sum\_{u=0}^{T}\pi\_{u}\Delta W\_{u}=\sum\_{u=0}^{T}\pi\_{u}(W\_{u}-W\_{u-1}).
A property holds 𝒫\mathcal{P}-quasi-surely if it fails only on a polar set AA satisfying supP∈𝒫P​(A)=0\sup\_{P\in\mathcal{P}}P(A)=0.
The super-hedging problem aims to determine the initial capital xx, and subsequently identify the trading strategy π\pi by equation ([2.10](https://arxiv.org/html/2512.21115v1#S2.E10 "In 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).
Before characterizing this initial cost, we impose the following absolute continuous condition associated with the strong neutral nonlinear expectation in ([2.8](https://arxiv.org/html/2512.21115v1#S2.E8 "In Definition 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∃P∈𝒫​ such that ​Q~X≪P​ for each ​X∈ℋ,where ​EQ~X​[X]=supQ∈𝒬EQ​[X].\exists P\in\mathcal{P}\text{ such that }\tilde{Q}\_{X}\ll P\text{ for each }X\in\mathcal{H},\quad\text{where }E\_{\tilde{Q}\_{X}}[X]=\sup\_{Q\in\mathcal{Q}}E\_{Q}[X]. |  | (2.11) |

###### Theorem 2.2.

Under model uncertainty, short sales prohibitions, and the no arbitrage assumption, the super-replication price of the contingent claim f​(ST)f(S\_{T}) is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Π​(f):=\displaystyle\Pi(f):= | inf{x∈ℝ:∃π​such that​x+π⋅W0T≥f​(ST),𝒫​-q.s.}\displaystyle\inf\left\{x\in\mathbb{R}:\ \exists\ \pi\ \text{such that}\ x+\pi\cdot W\_{0}^{T}\geq f(S\_{T}),\ \ \mathcal{P}\text{-q.s.}\right\} |  | (2.12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | supQ∈𝒬EQ​[f​(ST)],\displaystyle\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})],\qquad |  |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega and Q∈𝒬Q\in\mathcal{Q} satisfies the absolutely continuity requirement ([2.11](https://arxiv.org/html/2512.21115v1#S2.E11 "In 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).

###### Proof.

By Theorem [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") and the sub-additivity of the sublinear expectation yields,

|  |  |  |
| --- | --- | --- |
|  | supQ∈𝒬EQ​[π⋅W0T]≤∑u=0TsupQ∈𝒬EQ​[πu​Δ​Wu]≤0.\sup\_{Q\in\mathcal{Q}}E\_{Q}[\pi\cdot W\_{0}^{T}]\leq\sum\_{u=0}^{T}\sup\_{Q\in\mathcal{Q}}E\_{Q}[\pi\_{u}\Delta W\_{u}]\leq 0. |  |

Taking supQ∈𝒬EQ​[⋅]\sup\_{Q\in\mathcal{Q}}E\_{Q}[\cdot] on both sides of ([2.10](https://arxiv.org/html/2512.21115v1#S2.E10 "In 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) gives

|  |  |  |
| --- | --- | --- |
|  | x+supQ∈𝒬EQ​[π⋅W0T]≥supQ∈𝒬EQ​[f​(ST)],x+\sup\_{Q\in\mathcal{Q}}E\_{Q}[\pi\cdot W\_{0}^{T}]\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})], |  |

which implies x≥supQ∈𝒬EQ​[f​(ST)]x\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})]. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(f)=infM≥supQ∈𝒬EQ​[f​(ST)],\Pi(f)=\inf M\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})], |  | (2.13) |

where MM is the set of all feasible initial capitals in ([2.10](https://arxiv.org/html/2512.21115v1#S2.E10 "In 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).

Next, we show that all the inequalities in ([2.13](https://arxiv.org/html/2512.21115v1#S2.E13 "In Proof. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) are in fact identities, let γ:=supQ∈𝒬EQ​[f​(ST)]\gamma:=\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})], we need to verify that infM≤γ\inf M\leq\gamma.
Suppose to the contrary that infM>γ\inf M>\gamma.
Then it is obviously that

|  |  |  |
| --- | --- | --- |
|  | zγ:=(−γf​(ST)​(ω1)⋯f​(ST)​(ωk)⋯)T∉U1,z\_{\gamma}:=\begin{pmatrix}-\gamma&f(S\_{T})(\omega\_{1})&\cdots&f(S\_{T})(\omega\_{k})&\cdots\end{pmatrix}^{T}\notin U\_{1}, |  |

where U1U\_{1} is the set in the proof of Theorem [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty").
Otherwise, if zγ∈U1z\_{\gamma}\in U\_{1}, then there exists (x,π)(x,\pi) such that x=γx=\gamma and x+π⋅W0T=f​(ST)x+\pi\cdot W\_{0}^{T}=f(S\_{T}), implying γ∈M\gamma\in M, contradicting infM>γ\inf M>\gamma.
Therefore, by the Hahn-Banach separation theorem yields a separating hyperplane gg such that

|  |  |  |
| --- | --- | --- |
|  | g⋅y≤0,∀y∈U1andg⋅z>0.g\cdot y\leq 0,\ \forall y\in U\_{1}\quad\text{and}\quad g\cdot z>0. |  |

Normalize so that g0>0g\_{0}>0 and define a probability measure Q​(ωk):=gk/g0>0Q(\omega\_{k}):=g\_{k}/g\_{0}>0.
The condition g⋅y≤0g\cdot y\leq 0 for all y∈U1y\in U\_{1} implies that the process WW is a QQ-supermartingale, hence Q∈𝒬Q\in\mathcal{Q}.
The strict inequality g⋅zγ>0g\cdot z\_{\gamma}>0 translates into

|  |  |  |
| --- | --- | --- |
|  | EQ​[f​(ST)]>γ=supQ∈𝒬EQ​[f​(ST)],E\_{Q}[f(S\_{T})]>\gamma=\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})], |  |

a contradiction.
Therefore, we conclude that

|  |  |  |
| --- | --- | --- |
|  | infM≤γ=supQ∈𝒬EQ​[f​(ST)],\inf M\leq\gamma=\sup\_{Q\in\mathcal{Q}}E\_{Q}[f(S\_{T})], |  |

completing the proof.
∎

## 3 Asset bubbles with short sales prohibitions under model uncertainty

### 3.1 Definition of the asset bubble

An asset price can be decomposed into two components: its market price, denoted by S=(St)t≥0S=(S\_{t})\_{t\geq 0}, and its fundamental price, denoted by S∗=(St∗)t≥0S^{\*}=(S\_{t}^{\*})\_{t\geq 0}.
An asset bubble is then identified as the discrepancy between these two quantities (Jarrow et al., [2006](https://arxiv.org/html/2512.21115v1#bib.bib23); Biagini and Mancin, [2017](https://arxiv.org/html/2512.21115v1#bib.bib2)).
Consequently, a precise specification of the fundamental price is a prerequisite for any rigorous analysis of asset bubbles.
In a classical asset bubble framework, it is commonly to define the fundamental price for a risky asset as the conditional expectation of its discounted future cash flows under an equivalent martingale measure (Jarrow et al., [2006](https://arxiv.org/html/2512.21115v1#bib.bib23)), that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | St∗=EQ[∑u=tτD^u+X^τI{τ<∞}|ℱt],0≤t<τ.S\_{t}^{\*}=E\_{Q}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right],\quad 0\leq t<\tau. |  | (3.1) |

To account for the possibility that bubbles may emerge endogenously over time, Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)) considered an incomplete financial market framework in which the economy undergoes regime shifts, leading to different local martingale measures across time.
In this setting, the fundamental price accounted for probability measures over partitioned time intervals and aggregated their contributions through summation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | St∗=∑i=0∞EQi[∑u=tτD^u+X^τI{τ<∞}|ℱt]I{t∈[σi,σi+1)},0≤t<τ,S\_{t}^{\*}=\sum\_{i=0}^{\infty}E\_{Q^{i}}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]I\_{\{t\in[\sigma\_{i},\ \sigma\_{i+1})\}},\quad 0\leq t<\tau, |  | (3.2) |

where (σi)i≥0(\sigma\_{i})\_{i\geq 0} denote an increasing sequence of random times with σ0=0\sigma\_{0}=0 representing the times of regime shifts in the economy.
Motivated by model uncertainty, we instead consider a family of probability measures 𝒬\mathcal{Q}, and evaluate future cash flows via the upper expectation supQ∈𝒬EQ​[⋅]\sup\_{Q\in\mathcal{Q}}E\_{Q}[\cdot], which induces a sublinear expectation 𝔼​[⋅]\mathbb{E}[\cdot] in the sense of Peng ([2019](https://arxiv.org/html/2512.21115v1#bib.bib38)).
Due to its dynamic consistency, the sublinear expectation framework naturally captures the informational structure required for valuation under interval-based specifications of probability models.
Within this setting, we adopt the framework introduced in Herdegen and Schweizer ([2016](https://arxiv.org/html/2512.21115v1#bib.bib16)) and Biagini and Mancin ([2017](https://arxiv.org/html/2512.21115v1#bib.bib2)), defining the fundamental price S∗S^{\*} as the super-replication price.
In particular, by Theorem [2.2](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), one can construct a trading strategy that super-replicates the asset’s future cash flows.
Accordingly, under short-sale constraints and model uncertainty, the fundamental price of the asset is defined as follows.

###### Definition 3.1.

Under short sales prohibitions and model uncertainty, the fundamental price S∗=(St∗)t∈[0,τ)S^{\*}=(S\_{t}^{\*})\_{t\in[0,\tau)} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | St∗:\displaystyle S\_{t}^{\*}: | =inf{x∈ℝ:∃π such that x+π⋅Wt∞≥∑u=tτD^u+X^τI{τ<∞},𝒫−q.s.},\displaystyle=\inf\left\{x\in\mathbb{R}:\exists\ \pi\text{ such that }x+\pi\cdot W\_{t}^{\infty}\geq\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}},\quad\mathcal{P}-q.s.\right\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =supQ∈𝒬EQ[∑u=tτD^u+X^τI{τ<∞}|ℱt],0≤t<τ,\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right],\quad 0\leq t<\tau, |  | (3.3) |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega, and Q∈𝒬Q\in\mathcal{Q} satisfies the absolutely continuous condition in ([2.11](https://arxiv.org/html/2512.21115v1#S2.E11 "In 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).

###### Remark 3.1.

Note that, in Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), the payoff XτX\_{\tau} is not taken into account on the event τ=∞\tau=\infty.
This exclusion is justified by the fact that the payoff Xτ​I{τ=∞}X\_{\tau}I\_{\{\tau=\infty\}} cannot be realized through any trading strategy, as all such strategies are required to be liquidated in finite time, even though their time horizons may be unbounded.

###### Remark 3.2.

Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") incorporates model uncertainty by evaluating the asset’s cash flows through the supremum of conditional expectations over a family of probability measures.
A related approach is considered in Biagini and Mancin ([2017](https://arxiv.org/html/2512.21115v1#bib.bib2)), where the family of probability measures 𝒬\mathcal{Q} is assumed to be equivalent to the actual probability set 𝒫\mathcal{P}.
In contrast, Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") relaxed this requirement by imposing only absolute continuity, as specified in [2.11](https://arxiv.org/html/2512.21115v1#S2.E11 "In 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty").
In the absence of model uncertainty, the family 𝒬\mathcal{Q} reduces into a single QQ.
In this case, equation ([3.1](https://arxiv.org/html/2512.21115v1#S3.Ex1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) in Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") coincide with the classical representation of the fundamental price given in equation ([3.1](https://arxiv.org/html/2512.21115v1#S3.E1 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).

By virtue of the dynamic consistency of sublinear expectations, the family of probability measures 𝒬\mathcal{Q} generally consists of multiple elements, which may be interpreted as regime-dependent measures associated with different time intervals, rather than a single probability measure.
As a consequence, the proposed framework encompasses and extends the classical settings of Jarrow et al. ([2006](https://arxiv.org/html/2512.21115v1#bib.bib23)) and Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)).
In particular, the fundamental price defined in Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") admits a robust and broader notion of valuation under model uncertainty.
We next establish the well-definedness of the fundamental price S∗S^{\*} and investigate the convergence properties of both the fundamental price S∗S^{\*} and the market price SS.
Before proceeding, we recall several basic concepts from Denis et al. ([2011](https://arxiv.org/html/2512.21115v1#bib.bib7)).
Let ℬ​(Ω)\mathcal{B}(\Omega) denote the Borel σ\sigma-algebra on Ω\Omega, and let L0​(Ω)L^{0}(\Omega) be the space of all ℬ​(Ω)\mathcal{B}(\Omega)-measurable real-valued functions. We set,

|  |  |  |
| --- | --- | --- |
|  | ℒ1​(𝒬):={Y∈L0​(Ω):supQ∈𝒬EQ​[|Y|]<∞}.\mathcal{L}^{1}(\mathcal{Q}):=\left\{Y\in L^{0}(\Omega):\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\left|Y\right|\right]<\infty\right\}. |  |

###### Lemma 3.1.

The fundamental price defined in ([3.1](https://arxiv.org/html/2512.21115v1#S3.Ex1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) is well defined.
Moreover, the market price (St)t≥0(S\_{t})\_{t\geq 0} converges quasi-surely to a limit S∞∈ℒ1​(𝒬)S\_{\infty}\in\mathcal{L}^{1}(\mathcal{Q}), while the fundamental price (St∗)t≥0(S^{\*}\_{t})\_{t\geq 0} converges quasi-surely to 0.

###### Proof.

We first show that St∗S\_{t}^{\*} is well defined.
By definition, it suffices to verify that ∑u=0τD^u+X^τ​I{τ<∞}∈ℒ1​(𝒬)\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\in\mathcal{L}^{1}(\mathcal{Q}) since

|  |  |  |
| --- | --- | --- |
|  | 0≤∑u=tτD^u+X^τ​I{τ<∞}≤∑u=0τD^u+X^τ​I{τ<∞}.0\leq\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\leq\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}. |  |

Under the no arbitrage assumption, the process (Wt)(W\_{t}) is a nonnegative GG-supermartingale.
Hence, by the nonlinear supermartingale convergence theorem (see Peng ([1999](https://arxiv.org/html/2512.21115v1#bib.bib34))), there exists W∞∈ℒ1​(𝒬)W\_{\infty}\in\mathcal{L}^{1}(\mathcal{Q}) such that Wt→W∞W\_{t}\to W\_{\infty}, q.s.
Obverse from ([2.1](https://arxiv.org/html/2512.21115v1#S2.E1 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | W∞=limt→∞Wt=limt→∞(St​I{t<τ}+∑u=0t∧τD^u+X^τ​I{τ≤t})=limt→∞St​I{τ=∞}+∑u=0τD^u+X^τ​I{τ<∞},q.s.W\_{\infty}=\lim\_{t\to\infty}W\_{t}=\lim\_{t\to\infty}(S\_{t}I\_{\{t<\tau\}}+\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq t\}})=\lim\_{t\to\infty}S\_{t}I\_{\{\tau=\infty\}}+\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}},\quad q.s. |  | (3.4) |

Since all terms are nonnegative, it follows that
S∞∈ℒ1​(𝒬)S\_{\infty}\in\mathcal{L}^{1}(\mathcal{Q}) and ∑u=0τD^u+X^τ​I{τ<∞}∈ℒ1​(𝒬)\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\in\mathcal{L}^{1}(\mathcal{Q}), which implies that St∗S\_{t}^{\*} is well defined and that St→S∞S\_{t}\to S\_{\infty} quasi-surely.

We now turn to the convergence of St∗S\_{t}^{\*}.
By Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈𝒬EQ[∑u=tτD^u+X^τI{τ<∞}|ℱt]=−∑u=0tD^u+supQ∈𝒬EQ[∑u=0τD^u+X^τI{τ<∞}|ℱt],\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]=-\sum\_{u=0}^{t}\hat{D}\_{u}+\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right], |  | (3.5) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈𝒬EQ[∑u=0τD^u+X^τI{τ<∞}|ℱt]=supQ∈𝒬EQ[(∑u=0τD^u+X^τ)I{τ<∞}+∑u=0τD^uI{τ=∞}|ℱt].\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau})I\_{\{\tau<\infty\}}+\sum\_{u=0}^{\tau}\hat{D}\_{u}I\_{\{\tau=\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]. |  | (3.6) |

Substituting ([3.6](https://arxiv.org/html/2512.21115v1#S3.E6 "In Proof. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) into ([3.5](https://arxiv.org/html/2512.21115v1#S3.E5 "In Proof. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) and then into ([3.1](https://arxiv.org/html/2512.21115v1#S3.Ex1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), and applying the Dominated convergence theorem for sublinear expectation in discrete states (Yang and Zhang, [2024b](https://arxiv.org/html/2512.21115v1#bib.bib48)), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞St∗\displaystyle\lim\_{t\to\infty}S\_{t}^{\*} | =−∑u=0∞D^uI{τ=∞}+supQ∈𝒬EQlimt→∞[(∑u=0τD^u+X^τ)I{τ<∞}+∑u=0τD^uI{τ=∞}|ℱt]I{τ=∞}\displaystyle=-\sum\_{u=0}^{\infty}\hat{D}\_{u}I\_{\{\tau=\infty\}}+\sup\_{Q\in\mathcal{Q}}E\_{Q}\lim\_{t\to\infty}\left[(\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau})I\_{\{\tau<\infty\}}+\sum\_{u=0}^{\tau}\hat{D}\_{u}I\_{\{\tau=\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]I\_{\{\tau=\infty\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑u=0∞D^uI{τ=∞}+supQ∈𝒬EQ[∑u=0∞D^u|ℱ∞]I{τ=∞}=0,q.s.\displaystyle=-\sum\_{u=0}^{\infty}\hat{D}\_{u}I\_{\{\tau=\infty\}}+\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=0}^{\infty}\hat{D}\_{u}\ \middle|\ \mathcal{F}\_{\infty}\right]I\_{\{\tau=\infty\}}=0,\quad q.s. |  |

This completes the proof.
∎

Given the definition of the fundamental price process S∗S^{\*}, the associated fundamental wealth process W∗=(Wt∗)t≥0W^{\*}=(W\_{t}^{\*})\_{t\geq 0} is naturally induced by the wealth process ([2.1](https://arxiv.org/html/2512.21115v1#S2.E1 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")). More precisely, it is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt∗=St∗​I{t<τ}+∑u=0t∧τD^u+X^τ​I{τ≤t}.W\_{t}^{\*}=S^{\*}\_{t}I\_{\{t<\tau\}}+\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq t\}}. |  | (3.7) |

We then investigate the convergence properties of W∗W^{\*} and establish its G-martingale structure.

###### Lemma 3.2.

The fundamental wealth process (Wt∗)t≥0(W\_{t}^{\*})\_{t\geq 0} is a uniformly integrable G-martingale.
Moreover, it is closed by a terminal value W∞∗∈ℒ1​(𝒬)W\_{\infty}^{\*}\in\mathcal{L}^{1}(\mathcal{Q}).

###### Proof.

We first identify the terminal value of W∗W^{\*}.
By Lemma [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we have St∗→0S\_{t}^{\*}\to 0 quasi-surely as t→∞t\to\infty.
Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | W∞∗=limt→∞Wt∗=limt→∞(St∗​I{t<τ}+∑u=0t∧τD^u+X^τ​I{τ≤t})=∑u=0τD^u+X^τ​I{τ<∞},q.s.W\_{\infty}^{\*}=\lim\_{t\to\infty}W\_{t}^{\*}=\lim\_{t\to\infty}(S^{\*}\_{t}I\_{\{t<\tau\}}+\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq t\}})=\sum\_{u=0}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}},\quad q.s. |  | (3.8) |

From Lemma [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), it follows that W∞∗∈ℒ1​(𝒬)W^{\*}\_{\infty}\in\mathcal{L}^{1}(\mathcal{Q}).
We now verify the GG-martingale property.
Recall equations ([3.4](https://arxiv.org/html/2512.21115v1#S3.E4 "In Proof. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) and ([3.8](https://arxiv.org/html/2512.21115v1#S3.E8 "In Proof. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), it is obviously that W∞=W∞∗+S∞W\_{\infty}=W\_{\infty}^{\*}+S\_{\infty}.
Thus, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈𝒬EQ​[W∞∗∣ℱt]\displaystyle\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}^{\*}\mid\mathcal{F}\_{t}] | =supQ∈𝒬EQ[∑u=0τD^uI{τ≤t}+X^τI{τ≤t}+∑u=0tD^uI{t<τ}+∑u=tτD^uI{t<τ}+X^τI{τ<∞}|ℱt]\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=0}^{\tau}\hat{D}\_{u}I\_{\{\tau\leq t\}}+\hat{X}\_{\tau}I\_{\{\tau\leq t\}}+\sum\_{u=0}^{t}\hat{D}\_{u}I\_{\{t<\tau\}}+\sum\_{u=t}^{\tau}\hat{D}\_{u}I\_{\{t<\tau\}}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supQ∈𝒬EQ[∑u=tτD^u+X^τI{τ<∞}|ℱt]I{t<τ}+(∑u=0tD^uI{t<τ}+∑u=0τD^uI{τ≤t})+X^τI{τ≤t}\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]I\_{\{t<\tau\}}+\left(\sum\_{u=0}^{t}\hat{D}\_{u}I\_{\{t<\tau\}}+\sum\_{u=0}^{\tau}\hat{D}\_{u}I\_{\{\tau\leq t\}}\right)+\hat{X}\_{\tau}I\_{\{\tau\leq t\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =St∗​I{t<τ}+∑u=0t∧τD^u+X^τ​I{τ≤t}=Wt∗.\displaystyle=S\_{t}^{\*}I\_{\{t<\tau\}}+\sum\_{u=0}^{t\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq t\}}=W\_{t}^{\*}. |  |

Hence, (Wt∗)t≥0(W\_{t}^{\*})\_{t\geq 0} is a GG-martingale.
Finally, since Wt∗=supQ∈𝒬EQ​[W∞∗∣ℱt]W\_{t}^{\*}=\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}^{\*}\mid\mathcal{F}\_{t}] and W∞∈ℒ1​(𝒬)W\_{\infty}\in\mathcal{L}^{1}(\mathcal{Q}), it follows that (Wt∗)t≥0(W\_{t}^{\*})\_{t\geq 0} is uniformly integrable and closed by W∞∗W\_{\infty}^{\*}.
This completes the proof.
∎

After introducing the notion of the fundamental price and establishing its main properties, we now formalize the concept of an asset price bubble.

###### Definition 3.2.

The asset price bubble β=(βt)t≥0\beta=(\beta\_{t})\_{t\geq 0} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt:=St−St∗,\beta\_{t}:=S\_{t}-S^{\*}\_{t}, |  | (3.9) |

where StS\_{t} denotes the market price of asset, and St∗S\_{t}^{\*} denotes its fundamental price as defined in ([3.1](https://arxiv.org/html/2512.21115v1#S3.Ex1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).

###### Remark 3.3.

The definition ([3.9](https://arxiv.org/html/2512.21115v1#S3.E9 "In Definition 3.2. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) is standard in the literature; see, for instance, Jarrow et al. ([2006](https://arxiv.org/html/2512.21115v1#bib.bib23), [2010](https://arxiv.org/html/2512.21115v1#bib.bib24)); Protter ([2013](https://arxiv.org/html/2512.21115v1#bib.bib41)); Herdegen and Schweizer ([2016](https://arxiv.org/html/2512.21115v1#bib.bib16)).
Combining the representations of the wealth process WW in ([2.1](https://arxiv.org/html/2512.21115v1#S2.E1 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) and the fundamental wealth process W∗W^{\*} in ([3.7](https://arxiv.org/html/2512.21115v1#S3.E7 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), the bubble process admits the equivalent characterization

|  |  |  |
| --- | --- | --- |
|  | βt=Wt−Wt∗,t<τ.\beta\_{t}=W\_{t}-W\_{t}^{\*},\quad t<\tau. |  |

Thus, the asset price bubble can be interpreted as the excess of market wealth over fundamental wealth.

Under short-sale constraints and model uncertainty, the financial market is assumed to be arbitrage-free.
By Theorem [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), the market wealth process satisfies Wt≥supQ∈𝒬EQ​[W∞∣ℱt]W\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}\mid\mathcal{F}\_{t}] for all t≥0t\geq 0.
Substituting this inequality into the wealth process ([2.1](https://arxiv.org/html/2512.21115v1#S2.E1 "In 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), we obtain that the market price of the asset SS satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | St≥supQ∈𝒬EQ[∑u=tτD^u+X^τI{τ<∞}|ℱt]=St∗,0≤t<τ.S\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]=S\_{t}^{\*},\quad 0\leq t<\tau. |  | (3.10) |

Consequently, the bubble process satisfies βt≥0\beta\_{t}\geq 0 for 0≤t<τ0\leq t<\tau under short sales prohibitions and model uncertainty.
This conclusion is consistent with the classical analysis of Protter ([2013](https://arxiv.org/html/2512.21115v1#bib.bib41)).
We say that a price bubble exists if the bubble process β\beta is nontrivial, that is, there exists t≥0t\geq 0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supP∈𝒫P​(βt>0)>0,\sup\_{P\in\mathcal{P}}P(\beta\_{t}>0)>0, |  | (3.11) |

where supP∈𝒫P​(ω)>0\sup\_{P\in\mathcal{P}}P(\omega)>0 for all ω∈Ω\omega\in\Omega.
And the absence of bubbles corresponds to β=0\beta=0 for all t≥0t\geq 0, 𝒫\mathcal{P}-q.s.
Equation ([3.11](https://arxiv.org/html/2512.21115v1#S3.E11 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) therefore implies that there exists at least one probability measure P∈𝒫P\in\mathcal{P} under which βt>0\beta\_{t}>0 occurs with positive probability.
This notion of bubble existence coincides with the definition adopted in Biagini and Mancin ([2017](https://arxiv.org/html/2512.21115v1#bib.bib2)).

###### Remark 3.4.

Note that negative bubbles may arise in alternative market settings or for certain classes of assets, such as foreign exchange markets.
A systematic analysis of such cases is left for subsequent work.

### 3.2 Types of bubble under uncertainty

Following the definition of the asset price bubble, we examine the classification types of bubbles under the condition of model uncertainty and short sales prohibitions.
In complete and incomplete markets, Jarrow et al. ([2006](https://arxiv.org/html/2512.21115v1#bib.bib23), [2010](https://arxiv.org/html/2512.21115v1#bib.bib24)) classified bubbles in into three types according to the behavior of a stopping time τ\tau: the case P​(τ=∞)>0P(\tau=\infty)>0, the case where τ\tau is unbounded but satisfies P​(τ<∞)=1P(\tau<\infty)=1, and the case where τ\tau is bounded.
When model uncertainty and short sales constraints are imposed, the market structure changes and only two of bubble types arise.
To this end, we first introduce the notion of an infi-supermartingale under model uncertainty.

###### Definition 3.3.

Let Y=(Yt)t≥0Y=(Y\_{t})\_{t\geq 0} denotes a random variable sequence on a discrete state space Ω\Omega. Then YY is called a infi-supermartingale if it satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt≥infQ∈𝒬EQ​[YT∣ℱt],0≤t≤T,Y\_{t}\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[Y\_{T}\mid\mathcal{F}\_{t}],\quad 0\leq t\leq T, |  | (3.12) |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.

###### Remark 3.5.

Observe that, for any random variable YTY\_{T} and any t≤Tt\leq T, infQ∈𝒬EQ​[YT∣ℱt]≤supQ∈𝒬EQ​[YT∣ℱt]\inf\_{Q\in\mathcal{Q}}E\_{Q}[Y\_{T}\mid\mathcal{F}\_{t}]\leq\sup\_{Q\in\mathcal{Q}}E\_{Q}[Y\_{T}\mid\mathcal{F}\_{t}].
Consequently, every GG-supermartingale is also an infi-supermartingale.
Furthermore, in the absence of model uncertainty, when the family of probability measures 𝒬\mathcal{Q} reduces to a singleton QQ, the concepts of GG-supermartingale and infi-supermartingale both coincide with the classical notion of a supermartingale under QQ.

###### Theorem 3.1.

Under short sales prohibitions and model uncertainty, if there exists a nontrivial bubble β\beta in an asset’s price, then we have two possibilities:

(i) βt\beta\_{t} is a infi-supermartingale, if the stopping time τ\tau is unbounded with P​(τ<∞)=1P(\tau<\infty)=1, or satisfies P​(τ=∞)>0P(\tau=\infty)>0.

(ii) βt\beta\_{t} is a G-supermartingale, if the stopping time τ\tau is bounded.

###### Proof.

We begin with the proof of type (ii). Assume that τ<T\tau<T for some finite T∈ℝ+T\in\mathbb{R}^{+}. Then S∞=0S\_{\infty}=0, and consequently W∞=W∞∗W\_{\infty}=W\_{\infty}^{\*}.
Define the auxiliary process

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^t:=Wt−supQ∈𝒬EQ​[W∞∣ℱt].\hat{\beta}\_{t}:=W\_{t}-\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}\mid\mathcal{F}\_{t}]. |  | (3.13) |

Since Wt∗=supQ∈𝒬EQ​[W∞∗∣ℱt]W\_{t}^{\*}=\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}^{\*}\mid\mathcal{F}\_{t}] by Lemma [3.2](https://arxiv.org/html/2512.21115v1#S3.Thmlemma2 "Lemma 3.2. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), it follows that

|  |  |  |
| --- | --- | --- |
|  | βt=Wt−Wt∗=β^t+supQ∈𝒬EQ​[W∞∣ℱt]−Wt∗=β^t+supQ∈𝒬EQ​[W∞∗∣ℱt]−Wt∗=β^t.\beta\_{t}=W\_{t}-W\_{t}^{\*}=\hat{\beta}\_{t}+\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}\mid\mathcal{F}\_{t}]-W\_{t}^{\*}=\hat{\beta}\_{t}+\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}^{\*}\mid\mathcal{F}\_{t}]-W\_{t}^{\*}=\hat{\beta}\_{t}. |  |

When t≥τt\geq\tau, it is obvious that βt=β^t=0\beta\_{t}=\hat{\beta}\_{t}=0, and in particular βT=0\beta\_{T}=0 for T≥tT\geq t.
Suppose that βt\beta\_{t} is not a GG-supermartingale.
Since βt≥0\beta\_{t}\geq 0 by equation ([3.10](https://arxiv.org/html/2512.21115v1#S3.E10 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), under model uncertainty, only the following two cases may occur:

|  |  |  |
| --- | --- | --- |
|  | βt=supQ∈𝒬EQ​[βT∣ℱt]=0 or βt=infQ∈𝒬EQ​[βT∣ℱt]=0,0≤t≤T.\beta\_{t}=\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]=0\quad\text{ or }\quad\beta\_{t}=\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]=0,\quad 0\leq t\leq T. |  |

In either case, βt\beta\_{t} vanishes identically, which contradicts the assumption that a nontrivial asset price bubble exists.
Hence, we obtain βt≥supQ∈𝒬EQ​[βT∣ℱt]≥infQ∈𝒬EQ​[βT∣ℱt]\beta\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}], by Remark [3.5](https://arxiv.org/html/2512.21115v1#S3.Thmremark5 "Remark 3.5. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), this inequality implies that βt\beta\_{t} is a GG-supermartingale. This established assertion (ii).

When τ\tau is unbounded but satisfies P​(τ<∞)=1P(\tau<\infty)=1, we still have S∞=0S\_{\infty}=0 still holds, and consequently βt=β^t\beta\_{t}=\hat{\beta}\_{t} holds.
Combing ([2.8](https://arxiv.org/html/2512.21115v1#S2.E8 "In Definition 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) with ([3.13](https://arxiv.org/html/2512.21115v1#S3.E13 "In Proof. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈𝒬EQ​[−β^T∣ℱt]\displaystyle\sup\_{Q\in\mathcal{Q}}E\_{Q}[-\hat{\beta}\_{T}\mid\mathcal{F}\_{t}] | =supQ∈𝒬EQ​[supQ∈𝒬EQ​[W∞∣ℱT]−WT∣ℱt]≥supQ∈𝒬EQ​[W∞∣ℱt]−supQ∈𝒬EQ​[WT∣ℱt]\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}[\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}\mid\mathcal{F}\_{T}]-W\_{T}\mid\mathcal{F}\_{t}]\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}\mid\mathcal{F}\_{t}]-\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{T}\mid\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥supQ∈𝒬EQ​[W∞∣ℱt]−Wt=−β^t,0≤t≤T.\displaystyle\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{\infty}\mid\mathcal{F}\_{t}]-W\_{t}=-\hat{\beta}\_{t},\qquad 0\leq t\leq T. |  |

Hence βt\beta\_{t} satisfies the defining inequality of an infi-supermartingale.
If P​(τ=∞)>0P(\tau=\infty)>0, then by Remark [3.3](https://arxiv.org/html/2512.21115v1#S3.Thmremark3 "Remark 3.3. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), Lemma [3.2](https://arxiv.org/html/2512.21115v1#S3.Thmlemma2 "Lemma 3.2. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") and ([2.8](https://arxiv.org/html/2512.21115v1#S2.E8 "In Definition 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), we similarly obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈𝒬EQ​[−βT∣ℱt]\displaystyle\sup\_{Q\in\mathcal{Q}}E\_{Q}[-\beta\_{T}\mid\mathcal{F}\_{t}] | =supQ∈𝒬EQ​[WT∗−WT∣ℱt]≥supQ∈𝒬EQ​[WT∗∣ℱt]−supQ∈𝒬EQ​[WT∣ℱt]\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{T}^{\*}-W\_{T}\mid\mathcal{F}\_{t}]\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{T}^{\*}\mid\mathcal{F}\_{t}]-\sup\_{Q\in\mathcal{Q}}E\_{Q}[W\_{T}\mid\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥Wt∗−Wt=−βt,0≤t≤T,\displaystyle\geq W\_{t}^{\*}-W\_{t}=-\beta\_{t},\qquad 0\leq t\leq T, |  |

indicating βt\beta\_{t} is also an infi-supermartingale.
This completes the proof.
∎

###### Remark 3.6.

The classification of asset price bubbles in Theorem [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") differs from the classical three-type framework of Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)).
Specifically, when P​(τ=∞)>0P(\tau=\infty)>0, Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)) showed that the bubble processβt\beta\_{t} is a uniformly integrable local martingale, whereas if τ\tau unbounded with P​(τ<∞)=1P(\tau<\infty)=1, then β\beta is merely a local martingale.
Under model uncertainty and short sales constraints, however, both cases are naturally encompassed by the notion of an infi-supermartingale. Indeed, for any 0≤t≤T0\leq t\leq T,

|  |  |  |
| --- | --- | --- |
|  | βt=EQ​[βT∣ℱt]≥infQ∈𝒬EQ​[βT∣ℱt].\beta\_{t}=E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]. |  |

If τ\tau is a bounded stopping time, Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)) established that βt\beta\_{t} is a strict local martingale, and hence a supermartingale.
In the absence of model uncertainty, the set 𝒬\mathcal{Q} collapses to a singleton, in which case a GG-supermartingale coincides with the classical notion of a supermartingale.

As indicated, Type 1 bubbles arise when an asset has a finite but unbounded lifespan, or an infinite lifespan with a payoff at {τ=∞}\{\tau=\infty\}.
Type 2 bubbles pertain to assets with a bounded lifespan.
Subsequently, we present corresponding examples for different types of stopping time τ\tau.
Following Jarrow et al. ([2006](https://arxiv.org/html/2512.21115v1#bib.bib23)), we take fiat money, declared by government as legal tender, as one such example.

###### Example 3.1.

Let SS denote fiat money. In the benchmark case of a perfectly stable unit of account, we normalize St=1S\_{t}=1 for all t≥0t\geq 0.
Under financial markets with model uncertainty, however, it is inappropriate to model the real value of fiat money as constant.
We therefore assume that the real value of fiat money is given by

|  |  |  |
| --- | --- | --- |
|  | St=1Pt,t≥0,S\_{t}=\frac{1}{P\_{t}},\quad t\geq 0, |  |

where PtP\_{t} denotes a price index (e.g., the consumer price index)
We normalize the initial price level to P0=1P\_{0}=1 and assume that the price index evolves according to Pt+1=Pt​Yt+1P\_{t+1}=P\_{t}Y\_{t+1}, where Yt+1Y\_{t+1} is the one-period inflation factor.
Model uncertainty is introduced by allowing Yt+1∈[y¯,y¯],y¯<1≤y¯Y\_{t+1}\in[\underline{y},\overline{y}],\ \underline{y}<1\leq\overline{y}, thereby capturing the possibility of both deflation and inflation arising from macroeconomic uncertainty.
As before, we assume that fiat money pays no dividends, i.e., D=0D=0, which implies that the fundamental value satisfies St∗=0S\_{t}^{\*}=0 for all t≥0t\geq 0.
Consequently, the entire value of fiat money is attributed to the bubble component βt=St\beta\_{t}=S\_{t}.
For any t≥0t\geq 0, we obtain

|  |  |  |
| --- | --- | --- |
|  | infQ∈𝒬EQ[βt+1∣ℱt]=infQ∈𝒬EQ[1Pt​Yt+1|ℱt]=βt1y¯≤βt.\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{t+1}\mid\mathcal{F}\_{t}]=\inf\_{Q\in\mathcal{Q}}E\_{Q}\left[\frac{1}{P\_{t}Y\_{t+1}}\ \middle|\ \mathcal{F}\_{t}\right]=\beta\_{t}\frac{1}{\overline{y}}\leq\beta\_{t}. |  |

We conclude that the bubble process (βt)t≥0(\beta\_{t})\_{t\geq 0} is an infi-supermartingale with respect to the family of probability measures 𝒬\mathcal{Q}.

To address the case τ<∞\tau<\infty, including situations in which τ\tau is unbounded but satisfies P​(τ<∞)=1P(\tau<\infty)=1, as well as the case of bounded maturity, we consider a simpler and explicit example in a discrete-time setting.
We begin with the former scenario.

###### Example 3.2.

Let Ω={ω1,ω2}\Omega=\{\omega\_{1},\omega\_{2}\}, and let the asset maturity τ\tau be a strictly positive random time such that P​(τ>t)>0P(\tau>t)>0 for all t≥0t\geq 0.
Assume the asset pays no dividends and delivers a unit payoff at maturity τ\tau.
Then, by ([3.1](https://arxiv.org/html/2512.21115v1#S3.Ex1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), the fundamental price process is given by (St∗)t≥0=(I{t<τ})t≥0(S\_{t}^{\*})\_{t\geq 0}=(I\_{\{t<\tau\}})\_{t\geq 0}.
We define a price process SS on a one-step tree and compute the corresponding bubble process β\beta:

|  |  |  |
| --- | --- | --- |
|  | S0=1​↗S1​(ω1)=1.5→β1​(ω1)=0.5↘S1​(ω2)=0.5→β1​(ω1)=−0.5S\_{0}=1\begin{matrix}&\nearrow&S\_{1}(\omega\_{1})=1.5&\to&\beta\_{1}(\omega\_{1})=0.5\\ &\searrow&S\_{1}(\omega\_{2})=0.5&\to&\beta\_{1}(\omega\_{1})=-0.5\end{matrix} |  |

Following Yang and Zhang ([2024b](https://arxiv.org/html/2512.21115v1#bib.bib48)), we characterize the probability set 𝒬\mathcal{Q} by a convex, closed domain 𝒟={θ1:0.2≤θ1≤0.4}\mathcal{D}=\{\theta\_{1}:0.2\leq\theta\_{1}\leq 0.4\}, where θ1=Q​(ω1)\theta\_{1}=Q(\omega\_{1}).
It then follows that β0=0\beta\_{0}=0 and

|  |  |  |
| --- | --- | --- |
|  | infQ∈𝒬EQ​[β1]=infθ1∈[0.2,0.4][0.5​θ1−0.5​(1−θ1)]=−0.3.\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{1}]=\inf\_{\theta\_{1}\in[0.2,0.4]}[0.5\ \theta\_{1}-0.5\ (1-\theta\_{1})]=-0.3. |  |

Consequently, β0>infQ∈𝒬EQ​[β1]\beta\_{0}>\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{1}].
By contrast, if 𝒟={θ1:0.5≤θ1≤0.7}\mathcal{D}=\{\theta\_{1}:0.5\leq\theta\_{1}\leq 0.7\}, then β0=infQ∈𝒬EQ​[β1]=0\beta\_{0}=\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{1}]=0.
In both cases, we obtain βt≥infQ∈𝒬EQ​[βT∣ℱt]\beta\_{t}\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}], illustrating the infi-supermartingale property of the bubble process (βt)t≥0(\beta\_{t})\_{t\geq 0}.

Analogously to Example [3.2](https://arxiv.org/html/2512.21115v1#S3.Thmexample2 "Example 3.2. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we now consider the case in which the maturity τ\tau is bounded.

###### Example 3.3.

In the same discrete framework as in Example [3.2](https://arxiv.org/html/2512.21115v1#S3.Thmexample2 "Example 3.2. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we define the fundamental price S∗S^{\*} and the market price SS on the space Ω={ω1,ω2}\Omega=\{\omega\_{1},\omega\_{2}\}.
Assume that τ<T\tau<T for some fixed T∈ℝ+T\in\mathbb{R}^{+}, and let the probability set 𝒬\mathcal{Q} be represented by a convex closed region 𝒟={θ1:0.2≤θ1≤0.4}\mathcal{D}=\{\theta\_{1}:0.2\leq\theta\_{1}\leq 0.4\} where θ1=Q​(ω1)\theta\_{1}=Q(\omega\_{1}).
As before, we have β0=0\beta\_{0}=0. A direct computation yields

|  |  |  |
| --- | --- | --- |
|  | supQ∈𝒬EQ​[β1]=supθ1∈[0.2,0.4][0.5​θ1−0.5​(1−θ1)]=−0.1.\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{1}]=\sup\_{\theta\_{1}\in[0.2,0.4]}[0.5\ \theta\_{1}-0.5\ (1-\theta\_{1})]=-0.1. |  |

Consequently, β0>supQ∈𝒬EQ​[β1]\beta\_{0}>\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{1}].
If instead 𝒟={θ1:0.2≤θ1≤0.5}\mathcal{D}=\{\theta\_{1}:0.2\leq\theta\_{1}\leq 0.5\}, then β0=supQ∈𝒬EQ​[β1]=0\beta\_{0}=\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{1}]=0.
Therefore, in the case of bounded maturity τ\tau, we obtain βt≥supQ∈𝒬EQ​[βT∣ℱt]\beta\_{t}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}], which illustrates the GG-supermartingale property of the bubble process (βt)t≥0(\beta\_{t})\_{t\geq 0}.

### 3.3 Characterization of bubble under uncertainty

Subsequently, We investigate necessary and sufficient conditions for the existence of price bubbles under model uncertainty and short sales prohibitions.
Our objective is to characterize, based solely on the observed asset price process SS, whether a bubble is present in the market.
As established in Theorem [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), different types of stopping time τ\tau lead to distinct notions of bubbles and, consequently to different martingale properties of the asset price process.
We therefore begin by providing a necessary condition for the existence of a nontrivial bubble under short sales constraints and model uncertainty.

###### Theorem 3.2.

Under short sales prohibitions and model uncertainty, if there exists a nontrivial bubble β\beta in an asset’s price, then we have two possibilities of the market price SS under model uncertainty:

(i) StS\_{t} is a infi-supermartingale if the stopping time τ\tau is unbounded with P​(τ<∞)=1P(\tau<\infty)=1, or satisfies P​(τ=∞)>0P(\tau=\infty)>0.

(ii) StS\_{t} is a G-supermartingale if the stopping time τ\tau is bounded.

###### Proof.

We begin with the proof of (i). Since D^t≥0\hat{D}\_{t}\geq 0 for all t≥0t\geq 0, it follows directly from ([3.1](https://arxiv.org/html/2512.21115v1#S3.Ex1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈𝒬EQ[ST∗∣ℱt]=supQ∈𝒬EQ[∑u=tτD^u−∑u=tTD^u+X^τI{τ<∞}|ℱt]≤St∗, 0≤t≤T.\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}^{\*}\mid\mathcal{F}\_{t}]=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=t}^{\tau}\hat{D}\_{u}-\sum\_{u=t}^{T}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]\leq S\_{t}^{\*},\ \ 0\leq t\leq T. |  | (3.14) |

Combining ([3.14](https://arxiv.org/html/2512.21115v1#S3.E14 "In Proof. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) with Theorem [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=βt+St∗\displaystyle S\_{t}=\beta\_{t}+S\_{t}^{\*} | ≥infQ∈𝒬EQ​[βT∣ℱt]+supQ∈𝒬EQ​[ST∗∣ℱt]=infQ∈𝒬EQ​[βT∣ℱt]−infQ∈𝒬EQ​[−ST∗∣ℱt]\displaystyle\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]+\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}^{\*}\mid\mathcal{F}\_{t}]=\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]-\inf\_{Q\in\mathcal{Q}}E\_{Q}[-S\_{T}^{\*}\mid\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥infQ∈𝒬EQ​[βT+ST∗∣ℱt]=infQ∈𝒬EQ​[ST∣ℱt],0≤t≤T,\displaystyle\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}+S\_{T}^{\*}\mid\mathcal{F}\_{t}]=\inf\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}\mid\mathcal{F}\_{t}],\qquad 0\leq t\leq T, |  |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.
This shows that the market price process (St)t≥0(S\_{t})\_{t\geq 0} is an infi-supermartingale whenever τ\tau is unbounded with P​(τ<∞)=1P(\tau<\infty)=1, or when P​(τ=∞)>0P(\tau=\infty)>0.
We now turn to (ii), if the stopping time τ\tau is bounded, then Theorem [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") together with ([3.14](https://arxiv.org/html/2512.21115v1#S3.E14 "In Proof. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) yields

|  |  |  |
| --- | --- | --- |
|  | St=βt+St∗≥supQ∈𝒬EQ​[βT∣ℱt]+supQ∈𝒬EQ​[ST∗∣ℱt]≥supQ∈𝒬EQ​[ST∣ℱt],0≤t≤T,S\_{t}=\beta\_{t}+S\_{t}^{\*}\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]+\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}^{\*}\mid\mathcal{F}\_{t}]\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}\mid\mathcal{F}\_{t}],\quad 0\leq t\leq T, |  |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.
Hence, (St)t≥0(S\_{t})\_{t\geq 0} is a GG-supermartingale when τ\tau is bounded.
This completes the proof.
∎

We next examine which martingale properties of the market price process allow for the emergence of a bubble.
In particular, we establish sufficient conditions for the existence of a bubble under short-selling constraints and model uncertainty.
For convenience, we impose the simplifying assumption that the asset SS pays no dividends.

###### Theorem 3.3.

Under short sales prohibitions and model uncertainty, assume that the asset price process S=(St)t≥0S=(S\_{t})\_{t\geq 0} pays no dividends.
For any stopping time τ\tau, if SS is a G-supermartingale, then a bubble exists under model uncertainty.

###### Proof.

Under the no dividends assumption, if P​(τ=∞)>0P(\tau=\infty)>0, then the fundamental price satisfies St∗=0S\_{t}^{\*}=0 for all t≥0t\geq 0. Since St≥0S\_{t}\geq 0 and, in real financial markets, StS\_{t} is not identically zero, it follows immediately that βt=St−St∗≥0\beta\_{t}=S\_{t}-S\_{t}^{\*}\geq 0, and there exists some t>0t>0 such that βt>0\beta\_{t}>0. Hence, by equation ([3.11](https://arxiv.org/html/2512.21115v1#S3.E11 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), a price bubble is present.
Next, consider the cases where τ\tau is unbounded with P​(τ<∞)=1P(\tau<\infty)=1, or where τ\tau is bounded.
Suppose, by contradiction, that no price bubble exists; that is, βt=0\beta\_{t}=0 for all t≥0t\geq 0. Then we have

|  |  |  |
| --- | --- | --- |
|  | St=St∗=supQ∈𝒬EQ[X^τI{τ<∞}|ℱt]=supQ∈𝒬EQ[Sτ∣ℱt],0≤t≤τ.S\_{t}=S\_{t}^{\*}=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\ \middle|\ \mathcal{F}\_{t}\right]=\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{\tau}\mid\mathcal{F}\_{t}],\quad 0\leq t\leq\tau. |  |

This implies that StS\_{t} is a GG-martingale, which contradicts the assumption that StS\_{t} is a GG-supermartingale. Therefore, the assumption of no price bubbles is false.
This completes the proof.
∎

###### Remark 3.7.

In the absence of model uncertainty, the notion of a GG-supermartingale in equation ([2.9](https://arxiv.org/html/2512.21115v1#S2.E9 "In Remark 2.3. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) degenerates into a classical supermartingale.
Accordingly, Theorem [3.3](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") recovers the classical result of Protter ([2013](https://arxiv.org/html/2512.21115v1#bib.bib41)).

###### Remark 3.8.

By Theorem [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), the no arbitrage condition under model uncertainty implies that the asset price process SS is a GG-supermartingale. Combined with Theorem [3.3](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), this shows that any non-dividend paying asset whose price is a GG-supermartingale necessarily exhibits a bubble.
Consequently, under no arbitrage with model uncertainty assumption, a financial bubble must arise whenever the asset pays no dividends.

Combining Theorems [3.2](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") and [3.3](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we conclude that when the stopping time τ\tau is bounded and the asset SS pays no dividends, the GG-supermartingle property of SS provides both necessary and sufficient conditions for the existence of a bubble under model uncertainty and short sales prohibitions.
In contrast, when τ\tau is unbounded with P​(τ<∞)=1P(\tau<\infty)=1 or satisfies P​(τ=∞)>0P(\tau=\infty)>0, the infi-supermartingale property of SS is no longer sufficient to ensure the presence of a bubble; in this case, the condition must be strengthened to the GG-supermartingale framework.
For an intuitive illustration of these results, Figure [1](https://arxiv.org/html/2512.21115v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") summarizes the martingale properties of the price process and the corresponding necessary and sufficient conditions for the existence of bubbles under short-selling constraints and model uncertainty.

###### Corollary 3.1.

Under short sales prohibitions and model uncertainty, assume that the asset SS pays no dividends.
Then any nontrivial asset price bubble β\beta satisfies the following properties:

(i) β≥0\beta\geq 0.

(ii) βτ​I{τ<∞}=0\beta\_{\tau}I\_{\{\tau<\infty\}}=0.

(iii) If the stopping time τ\tau is bounded and βt=0\beta\_{t}=0, then βT=0\beta\_{T}=0 for all T≥tT\geq t.
In contrast, this implication generally fails for other types of stopping times, such as unbounded τ\tau with P​(τ<∞)=1P(\tau<\infty)=1 or τ\tau satisfying P​(τ=∞)>0P(\tau=\infty)>0.

###### Proof.

The nonnegativity of β\beta in (i) follows immediately from equation ([3.10](https://arxiv.org/html/2512.21115v1#S3.E10 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).
For (ii), on the event {τ<∞}\{\tau<\infty\}, equation ([3.1](https://arxiv.org/html/2512.21115v1#S3.Ex1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) yields

|  |  |  |
| --- | --- | --- |
|  | βτ=Sτ−Sτ∗=Sτ−supQ∈𝒬EQ​[X^τ​I{τ<∞}∣ℱτ]=0.\beta\_{\tau}=S\_{\tau}-S\_{\tau}^{\*}=S\_{\tau}-\sup\_{Q\in\mathcal{Q}}E\_{Q}[\hat{X}\_{\tau}I\_{\{\tau<\infty\}}\mid\mathcal{F}\_{\tau}]=0. |  |

which proves the claim.
For (iii), suppose that τ\tau is bounded and βt=0\beta\_{t}=0. By Theorem [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we obtain 0≥supQ∈𝒬EQ​[βT∣ℱt]0\geq\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}] for T≥tT\geq t. Since β≥0\beta\geq 0, it follows that

|  |  |  |
| --- | --- | --- |
|  | supQ∈𝒬EQ​[βT∣ℱt]=0,0≤t≤T.\sup\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]=0,\quad 0\leq t\leq T. |  |

Because supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for every ω∈Ω\omega\in\Omega, we conclude that βT=0\beta\_{T}=0 for all T≥tT\geq t.
If, on the other hand, τ\tau is not bounded, then Theorem [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") together with βt=0\beta\_{t}=0 only implies

|  |  |  |
| --- | --- | --- |
|  | infQ∈𝒬EQ​[βT∣ℱt]=0,0≤t≤T.\inf\_{Q\in\mathcal{Q}}E\_{Q}[\beta\_{T}\mid\mathcal{F}\_{t}]=0,\quad 0\leq t\leq T. |  |

However, since supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega, this condition is insufficient to deduce that βT=0\beta\_{T}=0. Hence,the persistence property established in the bounded case does not extend to unbounded stopping times.
This completes the proof.
∎

Property (i) of Corollary [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmcorollary1 "Corollary 3.1. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") asserts that price bubbles are always nonnegative; equivalently, the market price of an asset can never fall below its fundamental value.
Property (ii) further implies that any bubble must collapse at or before the stopping time τ<∞\tau<\infty, since a bubble cannot survive the insolvency of the underlying asset.
Moreover, property (iii) of Corollary [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmcorollary1 "Corollary 3.1. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") shows that when the stopping time τ\tau is bounded, a bubble, once it collapses prior to the asset’s maturity, cannot re-emerge.
In other words, in models with a bounded stopping time, bubbles must either be present from the outset or never arise at all; and if a bubble exists and subsequently bursts, it cannot reform.
This phenomenon admits a natural financial interpretation. If a risky asset is known to default at a deterministic future date, rational investors will anticipate the impending insolvency and reduce their holdings accordingly. Such selling pressure drives down the market price and prevents the formation of new bubbles once an initial bubble has collapsed.
In contrast, for other classes of stopping times, such as unbounded τ\tau with P​(τ<∞)=1P(\tau<\infty)=1 or stopping times satisfying P​(τ=∞)>0P(\tau=\infty)>0, the persistence result in property (iii) no longer holds. In these settings, bubbles may reappear after an initial collapse.
This feature is consistent with empirical evidence from financial markets. In particular, when the asset has an infinite lifetime, or when its liquidation time is unbounded and not observable to market participants, bubbles may repeatedly emerge and collapse over the lifetime of the asset.

### 3.4 No domain under model uncertainty

In the preceding sections, our analysis has been conducted under the no arbitrage assumption in the presence of model uncertainty.
Under this assumption, Remark [3.8](https://arxiv.org/html/2512.21115v1#S3.Thmremark8 "Remark 3.8. ‣ 3.3 Characterization of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") shows that a financial bubble must arise whenever the asset pays no dividends.
If this condition is relaxed to the weaker requirement of no dominance under model uncertainty, it is natural to ask whether bubbles may still occur and, if so, what types of bubbles can emerge in this broader framework.
We begin by introducing the notion of a dominant trading strategy under model uncertainty.

###### Definition 3.4.

A trading strategy π\pi is said to be dominant under model uncertainty if there exists another trading strategy π^\hat{\pi} such that

(i) both π\pi and π~\tilde{\pi} are self-financing;

(ii) V0=V~0V\_{0}=\tilde{V}\_{0}

(iii) VT≥V~TV\_{T}\geq\tilde{V}\_{T} and supP∈𝒫P​[VT>V~T]>0\sup\_{P\in\mathcal{P}}P[V\_{T}>\tilde{V}\_{T}]>0,

where supP∈𝒫P​(ω)>0\sup\_{P\in\mathcal{P}}P(\omega)>0 for all ω∈Ω\omega\in\Omega, and V~0\tilde{V}\_{0} and V~T\tilde{V}\_{T} denote the initial and terminal values of the portfolio associated with π~\tilde{\pi}, respectively.
The market is said to satisfy no dominance under model uncertainty if no trading strategy simultaneously satisfies (i)-(iii).

###### Remark 3.9.

Analogously to Remark [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmremark1 "Remark 2.1. ‣ 2.1 Financial market ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), conditions (ii) and (iii) in Definition [3.4](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition4 "Definition 3.4. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") can equivalently be expressed in terms of gains processes as GT≥G~TG\_{T}\geq\tilde{G}\_{T} and supP∈𝒫P​[GT>G~T]>0\sup\_{P\in\mathcal{P}}P[G\_{T}>\tilde{G}\_{T}]>0.
In the absence of model uncertainty, the set of probability measures 𝒬\mathcal{Q} reduces to a singleton QQ. In this case, Definition [3.4](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition4 "Definition 3.4. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") coincides with the classical definition of dominance introduced in Kwok ([2008](https://arxiv.org/html/2512.21115v1#bib.bib29)).

###### Remark 3.10.

If, in Definition [3.4](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition4 "Definition 3.4. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), there exists a portfolio V~\tilde{V} with zero initial wealth ends up with a nonnegative and strictly positive under at least one model P∈𝒫P\in\mathcal{P}, then the strategy constitutes an arbitrage under model uncertainty.
Consequently, the existence of a dominant trading strategy implies the presence of an arbitrage opportunity in the sense of Definition [2.1](https://arxiv.org/html/2512.21115v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), whereas the converse does not necessarily hold.
Hence, the no arbitrage condition implies the no dominance condition under model uncertainty.

We now investigate the the existence of price bubbles under the no dominant condition, in the presence of short-selling constraints and model uncertainty.

###### Theorem 3.4.

Under short sales prohibitions and model uncertainty, if no dominant trading strategy exists, then no asset price bubble can exist.

###### Proof.

We argue by contradiction.
Suppose that

|  |  |  |
| --- | --- | --- |
|  | St>St∗,∀t≥0,S\_{t}>S\_{t}^{\*},\quad\forall t\geq 0, |  |

and in particular S0>S0∗S\_{0}>S\_{0}^{\*} at time 0.
Then, by equation ([3.11](https://arxiv.org/html/2512.21115v1#S3.E11 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), the price process exhibits a bubble.
By Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), the fundamental value S∗S^{\*} admits a super-replicating representation. In conjunction with the super-replication theorem (Theorem [2.2](https://arxiv.org/html/2512.21115v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.2 Fundamental theorem of asset pricing with short sales prohibitions under model uncertainty ‣ 2 Model setting ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | supQ∈𝒬EQ[∑u=0T¯∧τD^u+X^τI{τ≤T¯}]=inf{x∈ℝ:∃πs.t.x+π⋅W0T¯≥∑u=0T¯∧τD^u+X^τI{τ≤T¯},𝒫−q.s.}\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sum\_{u=0}^{\bar{T}\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq\bar{T}\}}\right]=\inf\left\{x\in\mathbb{R}:\exists\ \pi\ s.t.\ x+\pi\cdot W\_{0}^{\bar{T}}\geq\sum\_{u=0}^{\bar{T}\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq\bar{T}\}},\ \mathcal{P}-q.s.\right\} |  | (3.15) |

Denote x′=infMx^{\prime}=\inf M, where MM is the set of all initial capitals in right side of equation ([3.15](https://arxiv.org/html/2512.21115v1#S3.E15 "In Proof. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | S0>S0∗=x′.S\_{0}>S\_{0}^{\*}=x^{\prime}. |  | (3.16) |

Consider a self-financing portfolio with initial capital V0=x′V\_{0}=x^{\prime} and trading strategy π\pi, whose terminal value is given by
VT¯=x′+π⋅W0T¯.V\_{\bar{T}}=x^{\prime}+\pi\cdot W\_{0}^{\bar{T}}.
Consider another asset with initial value V~0=S0\tilde{V}\_{0}=S\_{0} and terminal payoff
V~T¯=∑u=0T¯∧τD^u+X^τ​I{τ≤T¯}.\tilde{V}\_{\bar{T}}=\sum\_{u=0}^{\bar{T}\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq\bar{T}\}}.
By ([3.15](https://arxiv.org/html/2512.21115v1#S3.E15 "In Proof. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) and ([3.16](https://arxiv.org/html/2512.21115v1#S3.E16 "In Proof. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), it follows that

|  |  |  |
| --- | --- | --- |
|  | GT¯=π⋅W0T¯≥∑u=0T¯∧τD^u+X^τ​I{τ≤T¯}−x′>∑u=0T¯∧τD^u+X^τ​I{τ≤T¯}−S0=G~T¯.G\_{\bar{T}}=\pi\cdot W\_{0}^{\bar{T}}\geq\sum\_{u=0}^{\bar{T}\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq\bar{T}\}}-x^{\prime}>\sum\_{u=0}^{\bar{T}\wedge\tau}\hat{D}\_{u}+\hat{X}\_{\tau}I\_{\{\tau\leq\bar{T}\}}-S\_{0}=\tilde{G}\_{\bar{T}}. |  |

Since supP∈𝒫P​(ω)>0\sup\_{P\in\mathcal{P}}P(\omega)>0 for all ω∈Ω\omega\in\Omega, we conclude

|  |  |  |
| --- | --- | --- |
|  | GT¯>G~T¯ and supP∈𝒫P​[GT¯>G~T¯]>0.G\_{\bar{T}}>\tilde{G}\_{\bar{T}}\quad\text{ and }\quad\sup\_{P\in\mathcal{P}}P[G\_{\bar{T}}>\tilde{G}\_{\bar{T}}]>0. |  |

By Remark [3.9](https://arxiv.org/html/2512.21115v1#S3.Thmremark9 "Remark 3.9. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), this implies the existence of a dominant trading strategy under model uncertainty, contradicting the standing no-dominance assumption.
Therefore, under the no dominant condition, we thus obtain St≤St∗S\_{t}\leq S\_{t}^{\*}. Together with St≥St∗S\_{t}\geq S\_{t}^{\*} from equation ([3.10](https://arxiv.org/html/2512.21115v1#S3.E10 "In 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), we conclude that

|  |  |  |
| --- | --- | --- |
|  | St=St∗,∀t≥0,S\_{t}=S\_{t}^{\*},\quad\forall t\geq 0, |  |

which completes the proof.
∎

###### Remark 3.11.

Theorem [3.4](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") is coincide with the result in Biagini and Mancin ([2017](https://arxiv.org/html/2512.21115v1#bib.bib2)) and shows that, under the no dominant assumption, the presence of any bubble arises precisely from a duality gap in ([3.15](https://arxiv.org/html/2512.21115v1#S3.E15 "In Proof. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).

## 4 Contingent claims bubbles with short sales prohibitions under model uncertainty

In the preceding sections, we analyze price bubbles in the underlying asset SS.
We now turn to the valuation of contingent claims in a financial market with short sales prohibitions and model uncertainty.
Bubbles may influence the valuation of contingent claims in two distinct ways: they may either be inherited from a bubble in the underlying asset price process, or they may be endogenously generated by the contingent claim itself.
In what follows, we focus on standard contingent claims, including forward contracts as well as and European and American call and put options.
For simplify, we assume that the risky asset SS pays no dividends over the time interval [0,T][0,T], and that the stopping time τ\tau satisfies τ>T\tau>T quasi-surely for some T∈ℝ+T\in\mathbb{R}\_{+}.
Under this assumption, the fundamental price of the asset, originally defined in terms of the dividend process D^\hat{D} and the terminal payoff X^\hat{X}, reduces to a single remaining cash flow STS\_{T}. Consequently, the fundamental value of the risky asset is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | St∗=supQ∈𝒬EQ​[ST∣ℱt],S\_{t}^{\*}=\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}\mid\mathcal{F}\_{t}], |  | (4.1) |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.

A contingent claim underlying on the asset SS is defined as a financial contract that delivers a random payoff HT​(S)H\_{T}(S) at maturity TT, where HTH\_{T} is a measurable functional of the price path (St)0≤t≤T(S\_{t})\_{0\leq t\leq T}. We denote by Λt​(H)\Lambda\_{t}(H) the market price of the contingent claim HH at time tt. Since standard contingent claims have bounded maturity, it suffices to consider bubble phenomena over bounded time horizons τ\tau.
In analogy with the fundamental value of the risky asset introduced in Definition [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.1 Definition of the asset bubble ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we define the fundamental price of the contingent claim HH at time t≤Tt\leq T as

|  |  |  |
| --- | --- | --- |
|  | Λt∗​(H)=supQ∈𝒬EQ​[HT​(S)∣ℱt],0≤t≤T,\Lambda\_{t}^{\*}(H)=\sup\_{Q\in\mathcal{Q}}E\_{Q}[H\_{T}(S)\mid\mathcal{F}\_{t}],\quad 0\leq t\leq T, |  |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.
The price bubble associated with the contingent claim is then given by

|  |  |  |
| --- | --- | --- |
|  | δt=Λt​(H)−Λt∗​(H),0≤t≤T.\delta\_{t}=\Lambda\_{t}(H)-\Lambda\_{t}^{\*}(H),\quad 0\leq t\leq T. |  |

### 4.1 Forward contracts and European call and put options

Subsequently, we examine some standard contingent claims written on the same risky asset: a forward contract, a European call option, and a European put option.
A forward contract with delivery price KK and maturity TT yields the terminal payoff ST−KS\_{T}-K, its market price at time tt is denoted by Ft​(K)F\_{t}(K).
A European call option with strike KK and maturity TT pays the payoff (ST−K)+(S\_{T}-K)^{+}, with market price CtE​(K)C\_{t}^{E}(K) at time tt.
Similarly, a European put option with strike KK and maturity TT delivers the payoff (K−ST)+(K-S\_{T})^{+}, and its market price at time tt is denoted by PtE​(K)P\_{t}^{E}(K).
Let Ft∗​(K)F\_{t}^{\*}(K), Ct∗​(K)C\_{t}^{\*}(K), and Pt∗​(K)P\_{t}^{\*}(K) denote the corresponding fundamental prices of the forward contract, the European call option, and the European put option, respectively. These are defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft∗​(K)\displaystyle F\_{t}^{\*}(K) | =supQ∈𝒬EQ​[ST−K∣ℱt],\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}-K\mid\mathcal{F}\_{t}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CtE⁣∗​(K)\displaystyle C\_{t}^{E\*}(K) | =supQ∈𝒬EQ​[(ST−K)+∣ℱt],\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}[(S\_{T}-K)^{+}\mid\mathcal{F}\_{t}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | PtE⁣∗​(K)\displaystyle P\_{t}^{E\*}(K) | =supQ∈𝒬EQ​[(K−ST)+∣ℱt],\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}[(K-S\_{T})^{+}\mid\mathcal{F}\_{t}], |  |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.
We now investigate the relationship among these three fundamental prices in order to assess whether the classical put-call parity continues to hold for fundamental values in the presence of short sales constraints and model uncertainty.
Our analysis shows that, short sales prohibitions and model uncertainty generally lead to a breakdown of put-call parity at the level of fundamental prices.

###### Theorem 4.1.

Under short sales prohibitions and model uncertainty, the fundamental prices of European options and forward contract satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | infQ∈𝒬EQ​[ST−K∣ℱt]≤CtE⁣∗​(K)−PtE⁣∗​(K)\displaystyle\inf\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}-K\mid\mathcal{F}\_{t}]\leq C\_{t}^{E\*}(K)-P\_{t}^{E\*}(K) | ≤supQ∈𝒬EQ​[ST−K∣ℱt]\displaystyle\leq\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}-K\mid\mathcal{F}\_{t}] |  | (4.2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =St∗−K=Ft∗​(K),0≤t≤T,\displaystyle=S\_{t}^{\*}-K=F\_{t}^{\*}(K),\quad 0\leq t\leq T, |  |

where supQ∈𝒬Q​(ω)>0\sup\_{Q\in\mathcal{Q}}Q(\omega)>0 for all ω∈Ω\omega\in\Omega.

###### Proof.

At maturity TT, the payoffs satisfy the identity

|  |  |  |
| --- | --- | --- |
|  | (ST−K)+−(K−ST)+=ST−K.(S\_{T}-K)^{+}-(K-S\_{T})^{+}=S\_{T}-K. |  |

Using the sub-additivity of the sublinear expectation, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | CtE⁣∗​(K)−PtE⁣∗​(K)\displaystyle C\_{t}^{E\*}(K)-P\_{t}^{E\*}(K) | =supQ∈𝒬EQ​[(ST−K)+∣ℱt]−supQ∈𝒬EQ​[(K−ST)+∣ℱt]\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}[(S\_{T}-K)^{+}\mid\mathcal{F}\_{t}]-\sup\_{Q\in\mathcal{Q}}E\_{Q}[(K-S\_{T})^{+}\mid\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supQ∈𝒬EQ​[ST−K∣ℱt]=St∗−K=Ft∗​(K).\displaystyle\leq\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}-K\mid\mathcal{F}\_{t}]=S\_{t}^{\*}-K=F\_{t}^{\*}(K). |  |

Similarly, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | CtE⁣∗​(K)−PtE⁣∗​(K)\displaystyle C\_{t}^{E\*}(K)-P\_{t}^{E\*}(K) | =−infQ∈𝒬EQ​[−(ST−K)+∣ℱt]+infQ∈𝒬EQ​[−(K−ST)+∣ℱt]\displaystyle=-\inf\_{Q\in\mathcal{Q}}E\_{Q}[-(S\_{T}-K)^{+}\mid\mathcal{F}\_{t}]+\inf\_{Q\in\mathcal{Q}}E\_{Q}[-(K-S\_{T})^{+}\mid\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥infQ∈𝒬EQ​[ST−K∣ℱt].\displaystyle\geq\inf\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}-K\mid\mathcal{F}\_{t}]. |  |

This completes the proof.
∎

###### Remark 4.1.

In the absence of model uncertainty, the set of probability measures 𝒬\mathcal{Q} collapses to a singleton QQ.
In this case, both bounds in inequality ([4.2](https://arxiv.org/html/2512.21115v1#S4.E2 "In Theorem 4.1. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) coincide and equal EQ​[ST−K∣ℱt]E\_{Q}[S\_{T}-K\mid\mathcal{F}\_{t}], so that Theorem [4.1](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") recovers the classical put-call parity for fundamental prices, as documented in Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)).

Theorem [4.1](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") establishes that the fundamental price of the forward contract provides an upper bound for the difference between the fundamental prices of the European call and put options.
This result implies that, in general, put-call parity fails to hold at the level of fundamental prices in the presence of short-selling constraints and model uncertainty.
Form a technical perspective, this failure can be attributed to the sub-additively of the sublinear expectation: when expectations are taken with respect to a non-singleton set of probability measures, equality is no longer preserved and only inequalities can be ensured.
From an economic standpoint, short-selling constraints prevent investors from implementing the classical replication strategy underlying put-call parity, since the strategy requires short positions in the underlying asset.
As a consequence, the fundamental call-put spread is dominated by the fundamental forward price, leading the inequality stated in Theorem [4.1](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty").
We now strengthen the no arbitrage condition under model uncertainty by imposing the no dominance assumption.
Under this stronger assumption, the put-call parity relation is restored for market prices.

###### Theorem 4.2.

Under short sales prohibitions and model uncertainty, we assume there is no dominant condition.
Then the put-call parity holds for market prices, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | CtE​(K)−PtE​(K)=St−K=Ft​(K)C\_{t}^{E}(K)-P\_{t}^{E}(K)=S\_{t}-K=F\_{t}(K) |  | (4.3) |

###### Proof.

By the no-dominance assumption (Definition [3.4](https://arxiv.org/html/2512.21115v1#S3.Thmdefinition4 "Definition 3.4. ‣ 3.4 No domain under model uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), any two portfolios that generate identical cash flows at all future times must have the same price at time tt.
Applying this principle to the standard replication argument, where a long position in a European call and a short position in a European put with the same strike KK replicate a forward contract, yields the put-call parity relation ([4.3](https://arxiv.org/html/2512.21115v1#S4.E3 "In Theorem 4.2. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).
∎

Having analyzed put-call parity for both fundamental prices and market prices of standard contingent claims, we now turns to the properties of the associated price bubbles.

###### Theorem 4.3.

Under short sales prohibitions and model uncertainty, we suppose that the no dominance condition holds. Then the corresponding price bubbles satisfy

|  |  |  |
| --- | --- | --- |
|  | δtS=δtF≤δtE​C−δtE​P,0≤t≤T.\delta\_{t}^{S}=\delta\_{t}^{F}\leq\delta\_{t}^{EC}-\delta\_{t}^{EP},\quad 0\leq t\leq T. |  |

###### Proof.

From the representation

|  |  |  |
| --- | --- | --- |
|  | Ft∗​(K)=supQ∈𝒬EQ​[ST∣ℱt]−K,F\_{t}^{\*}(K)=\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}\mid\mathcal{F}\_{t}]-K, |  |

together with equation ([4.1](https://arxiv.org/html/2512.21115v1#S4.E1 "In 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), it follows that

|  |  |  |
| --- | --- | --- |
|  | Ft=St−K=Ft∗​(K)+(St−supQ∈𝒬EQ​[ST∣ℱt])=Ft∗​(K)+(St−St∗).F\_{t}=S\_{t}-K=F\_{t}^{\*}(K)+(S\_{t}-\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}\mid\mathcal{F}\_{t}])=F\_{t}^{\*}(K)+(S\_{t}-S\_{t}^{\*}). |  |

Hence, the bubble of the forward contract coincides with that of the underlying asset, that is, δtF=δtS\delta\_{t}^{F}=\delta\_{t}^{S}.
Next, under the no dominance assumption, combining equations ([4.2](https://arxiv.org/html/2512.21115v1#S4.E2 "In Theorem 4.1. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) and ([4.3](https://arxiv.org/html/2512.21115v1#S4.E3 "In Theorem 4.2. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")) yields

|  |  |  |
| --- | --- | --- |
|  | (CtE​(K)−CtE⁣∗​(K))−(PtE​(K)−PtE⁣∗​(K))≥(Ft​(K)−Ft∗​(K)).(C\_{t}^{E}(K)-C\_{t}^{E\*}(K))-(P\_{t}^{E}(K)-P\_{t}^{E\*}(K))\geq(F\_{t}(K)-F\_{t}^{\*}(K)). |  |

Rewriting this inequality in terms of bubbles gives

|  |  |  |
| --- | --- | --- |
|  | δtF≤δtE​C−δtE​P,\delta\_{t}^{F}\leq\delta\_{t}^{EC}-\delta\_{t}^{EP}, |  |

which completes the proof.
∎

###### Remark 4.2.

Theorem [4.3](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") stands in contrast to the classical results of Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)), where it is shown that European put options do not exhibit price bubbles and that the bubble in a European call option coincides with that of the underlying asset.
In the present framework, however, short-selling constraints combined with model uncertainty fundamentally alter this conclusion. Even when the terminal payoff of a contingent claim is bounded, as in the case of a European put option, its price may still exhibit a bubble.
Moreover, since put-call parity fails for fundamental prices of contingent claims, the bubble in the underlying asset is dominated by the difference between the bubbles in the European call and put options.

### 4.2 American options

After analyzing price bubbles in forward contracts and European options, we proceed to study price bubbles in American options under short-selling constraints and model uncertainty.
We begin by introducing the notion of a fundamental price of American option.
Taking into account the time value of money, which plays a crucial role in determining the optimal early exercise strategies, we define the fundamental price of an American option with payoff function HH and maturity TT as

|  |  |  |
| --- | --- | --- |
|  | ΛtA⁣∗​(H)=supτ∈[t,T]supQ∈𝒬EQ​[Hτ​(S)∣ℱt],\Lambda\_{t}^{A\*}(H)=\sup\_{\tau\in[t,T]}\sup\_{Q\in\mathcal{Q}}E\_{Q}[H\_{\tau}(S)\mid\mathcal{F}\_{t}], |  |

where supQ∈𝒬Q(ω)>)\sup\_{Q\in\mathcal{Q}}Q(\omega)>) for all ω∈Ω\omega\in\Omega.
Let CtA⁣∗​(K)C\_{t}^{A\*}(K) and PtA⁣∗​(K)P\_{t}^{A\*}(K) denote the fundamental prices of American call and put options with strike KK, respectively. Then

|  |  |  |
| --- | --- | --- |
|  | CtA⁣∗(K)=supτ∈[t,T]supQ∈𝒬EQ[(Sτ−KBτ)+|ℱt],PtA⁣∗(K)=supτ∈[t,T]supQ∈𝒬EQ[(KBτ−Sτ)+|ℱt].C\_{t}^{A\*}(K)=\sup\_{\tau\in[t,T]}\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(S\_{\tau}-\frac{K}{B\_{\tau}})^{+}\ \middle|\ \mathcal{F}\_{t}\right],\quad P\_{t}^{A\*}(K)=\sup\_{\tau\in[t,T]}\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(\frac{K}{B\_{\tau}}-S\_{\tau})^{+}\ \middle|\ \mathcal{F}\_{t}\right]. |  |

The corresponding price bubbles of the American call and put options are defined by

|  |  |  |
| --- | --- | --- |
|  | δtA​C=CtA​(K)−CtA⁣∗​(K),δtA​P=PtA​(K)−PtA⁣∗​(K),\delta\_{t}^{AC}=C\_{t}^{A}(K)-C\_{t}^{A\*}(K),\quad\delta\_{t}^{AP}=P\_{t}^{A}(K)-P\_{t}^{A\*}(K), |  |

where CtA​(K)C\_{t}^{A}(K) and PtA​(K)P\_{t}^{A}(K) denote the respective market prices.
In what follows, we first examine the relationship between American and European call options.

###### Theorem 4.4.

For all K≥0K\geq 0, the fundamental prices of American and European call options satisfy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CtE⁣∗​(K)≤CtA⁣∗​(K)≤CtE⁣∗​(K)+δtS.C\_{t}^{E\*}(K)\leq C\_{t}^{A\*}(K)\leq C\_{t}^{E\*}(K)+\delta\_{t}^{S}. |  | (4.4) |

Moreover, the corresponding market prices satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | CtE​(K)+(δtA​C−δtE​C)≤CtA​(K)≤CtE​(K)+(δtA​C−δtE​P).C\_{t}^{E}(K)+(\delta\_{t}^{AC}-\delta\_{t}^{EC})\leq C\_{t}^{A}(K)\leq C\_{t}^{E}(K)+(\delta\_{t}^{AC}-\delta\_{t}^{EP}). |  | (4.5) |

###### Proof.

Since τ=T\tau=T is an admissible stopping time, it follows immediately that

|  |  |  |  |
| --- | --- | --- | --- |
|  | CtE⁣∗(K)=supQ∈𝒬EQ[(ST−KBT)+|Ft]≤supτ∈[t,T]supQ∈𝒬EQ[(Sτ−KBτ)+|Ft]=CtA⁣∗(K),C\_{t}^{E\*}(K)=\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(S\_{T}-\frac{K}{B\_{T}})^{+}\ \middle|\ F\_{t}\right]\leq\sup\_{\tau\in[t,T]}\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(S\_{\tau}-\frac{K}{B\_{\tau}})^{+}\ \middle|\ F\_{t}\right]=C\_{t}^{A\*}(K), |  | (4.6) |

establishing the lower bound in [4.4](https://arxiv.org/html/2512.21115v1#S4.E4 "In Theorem 4.4. ‣ 4.2 American options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty").
To derive the upper bound, observe that for any τ∈[t,T]\tau\in[t,T],

|  |  |  |
| --- | --- | --- |
|  | (Sτ−KBτ)+≤(Sτ∗−KBτ)++δτS.(S\_{\tau}-\frac{K}{B\_{\tau}})^{+}\leq(S\_{\tau}^{\*}-\frac{K}{B\_{\tau}})^{+}+\delta\_{\tau}^{S}. |  |

Taking the supremum over τ\tau and QQ, and using Theorem [3.1](https://arxiv.org/html/2512.21115v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 Types of bubble under uncertainty ‣ 3 Asset bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | supτ∈[t,T]supQ∈𝒬EQ​[δτS∣Ft]=supQ∈𝒬supτ∈[t,T]EQ​[δτS∣Ft]≤δtS.\sup\_{\tau\in[t,T]}\sup\_{Q\in\mathcal{Q}}E\_{Q}[\delta\_{\tau}^{S}\mid F\_{t}]=\sup\_{Q\in\mathcal{Q}}\sup\_{\tau\in[t,T]}E\_{Q}[\delta\_{\tau}^{S}\mid F\_{t}]\leq\delta\_{t}^{S}. |  | (4.7) |

For the remaining term, Jensen’s inequality for sublinear expectations (Peng, [2019](https://arxiv.org/html/2512.21115v1#bib.bib38)), together with ([4.1](https://arxiv.org/html/2512.21115v1#S4.E1 "In 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")), yields

|  |  |  |
| --- | --- | --- |
|  | (Sτ∗−KBτ)+=(supQ∈𝒬EQ[ST∣ℱτ]−KBτ)+≤supQ∈𝒬EQ[(ST−KBτ)+|ℱτ]≤supQ∈𝒬EQ[(ST−KBT)+|ℱτ].(S\_{\tau}^{\*}-\frac{K}{B\_{\tau}})^{+}=(\sup\_{Q\in\mathcal{Q}}E\_{Q}[S\_{T}\mid\mathcal{F}\_{\tau}]-\frac{K}{B\_{\tau}})^{+}\leq\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(S\_{T}-\frac{K}{B\_{\tau}})^{+}\ \middle|\ \mathcal{F}\_{\tau}\right]\leq\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(S\_{T}-\frac{K}{B\_{T}})^{+}\ \middle|\ \mathcal{F}\_{\tau}\right]. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supτ∈[t,T]supQ∈𝒬EQ[(Sτ∗−KBτ)+|Ft]\displaystyle\sup\_{\tau\in[t,T]}\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[(S^{\*}\_{\tau}-\frac{K}{B\_{\tau}})^{+}\ \middle|\ F\_{t}\right] | ≤supτ∈[t,T]supQ∈𝒬EQ[supQ∈𝒬EQ[(ST−KBT)+∣ℱτ]|Ft]\displaystyle\leq\sup\_{\tau\in[t,T]}\sup\_{Q\in\mathcal{Q}}E\_{Q}\left[\sup\_{Q\in\mathcal{Q}}E\_{Q}[(S\_{T}-\frac{K}{B\_{T}})^{+}\mid\mathcal{F}\_{\tau}]\ \middle|\ F\_{t}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =supQ∈𝒬EQ​[(ST−KBT)+∣ℱt].\displaystyle=\sup\_{Q\in\mathcal{Q}}E\_{Q}[(S\_{T}-\frac{K}{B\_{T}})^{+}\mid\mathcal{F}\_{t}]. |  | (4.8) |

Combining these estimates gives

|  |  |  |
| --- | --- | --- |
|  | CtA⁣∗​(K)≤CtE⁣∗​(K)+δtS,C\_{t}^{A\*}(K)\leq C\_{t}^{E\*}(K)+\delta\_{t}^{S}, |  |

which completes the proof of ([4.4](https://arxiv.org/html/2512.21115v1#S4.E4 "In Theorem 4.4. ‣ 4.2 American options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty")).
Finally, since CtA​(K)=CtA⁣∗​(K)+δtA​CC\_{t}^{A}(K)=C\_{t}^{A\*}(K)+\delta\_{t}^{AC} and CtE​(K)=CtE⁣∗​(K)+δtE​CC\_{t}^{E}(K)=C\_{t}^{E\*}(K)+\delta\_{t}^{EC}, it follows immediately that

|  |  |  |
| --- | --- | --- |
|  | CtA​(K)≥CtE​(K)−δtE​C+δtA​C.C\_{t}^{A}(K)\geq C\_{t}^{E}(K)-\delta\_{t}^{EC}+\delta\_{t}^{AC}. |  |

Using Theorem [4.3](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.1 Forward contracts and European call and put options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty"), we also obtain

|  |  |  |
| --- | --- | --- |
|  | CtA​(K)≤CtE⁣∗​(K)−δtE​C+δtS+δtA​C≤CtE​(K)+δtA​C−δtE​P,C\_{t}^{A}(K)\leq C\_{t}^{E\*}(K)-\delta\_{t}^{EC}+\delta\_{t}^{S}+\delta\_{t}^{AC}\leq C\_{t}^{E}(K)+\delta\_{t}^{AC}-\delta\_{t}^{EP}, |  |

which completes the proof.
∎

Theorem [4.4](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 American options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") shows that the fundamental price of an American call option, which incorporates the early exercise feature, is always at least as large as that of its European counterpart.
Moreover, the additional value generated by early exercise at the level of fundamental prices is bounded above by the bubble component of the underlying asset,

|  |  |  |
| --- | --- | --- |
|  | CtA⁣∗​(K)−CtE⁣∗​(K)≤δtS.C\_{t}^{A\*}(K)-C\_{t}^{E\*}(K)\leq\delta\_{t}^{S}. |  |

Thus, even when early exercise is allowed, the incremental fundamental value cannot exceed the size of the underlying asset bubble.
At the level of market prices, Theorem [4.4](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 American options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") further implies

|  |  |  |
| --- | --- | --- |
|  | δtA​C−δtE​C≤CtA​(K)−CtE​(K)≤δtA​C−δtE​P.\delta\_{t}^{AC}-\delta\_{t}^{EC}\leq C\_{t}^{A}(K)-C\_{t}^{E}(K)\leq\delta\_{t}^{AC}-\delta\_{t}^{EP}. |  |

Hence, the admissible range of the American call premium over the European call is entirely determined by the relative magnitudes of the bubble components embedded in the corresponding option prices.

###### Remark 4.3.

Theorem [4.4](https://arxiv.org/html/2512.21115v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.2 American options ‣ 4 Contingent claims bubbles with short sales prohibitions under model uncertainty ‣ Discrete-time asset price bubbles with short sales prohibitions under model uncertainty") contrasts sharply with the classical result of Jarrow et al. ([2010](https://arxiv.org/html/2512.21115v1#bib.bib24)), which showed that, the market prices of European and American call options coincide and equal the fundamental value of American call option.
In our framework, however, short-selling constraints and model uncertainty prevent such equalities from holding.
As a result, only upper and lower bounds for both fundamental and market prices of American call options can be obtained via their European counterparts.

## 5 Conclusion

In this paper, we investigate discrete-time asset price bubbles under short-selling constraints in the presence of model uncertainty.
For a wealth process that combines the market price of a risky asset with accumulated cash flows, we establish a fundamental theorem of asset pricing under short sales prohibitions and model uncertainty by providing the equivalence between the GG-supermartingale property of the wealth process and no arbitrage.
As a direct consequence, we derive a super-hedging theorem, which allows us to introduce a novel notion of the fundamental asset price and, in turn, a corresponding definition of price bubbles.
We verify that this fundamental price is well defined and analyze its convergence properties.
Within this framework, we demonstrate that asset price bubbles can arise in only two distinct forms: infi-supermartingale bubbles and GG-supermartingale bubbles. Several illustrative examples are provided to illustrate these bubbles.
We further derive necessary and sufficient conditions for the existence of bubbles.
When maturity is bounded and the asset pays no dividends, the GG-supermartingale property of the asset price is both necessary and sufficient for the existence of bubbles.
In contrast, when maturity is unbounded, the infi-supermartingale property yields a necessary condition, while the GG-supermartingale property becomes sufficient.
Under the stronger no dominance assumption, price bubbles are ruled out altogether.
Subsequently, we turn to the pricing of standard contingent claims.
We show that, in general, put-call parity fails for fundamental prices, whereas it continues to hold for market prices under the no dominance condition.
Moreover, both the fundamental and market prices of American options can be bounded in terms of their European counterparts, with the bounds explicitly adjusted by the associated bubble components.
In particular, the early-exercise premium is bounded by bubble of the underlying asset in the case of fundamental prices, and by differences between the relevant option bubbles in the case of market prices.
Finally, we outline several directions for future research.
An empirical investigate of asset price bubbles using real financial data represents a natural next step. In addition, extending the present discrete-time framework to a continuous-time setting with short-selling constraints under model uncertainty remains an important topic for future study.

## References

* Aliprantis and Border (2006)

  C.D. Aliprantis and K.C. Border.
  *Infinite dimensional analysis: a hitchhiker’s guide*.
  Springer, 2006.
* Biagini and Mancin (2017)

  F. Biagini and J. Mancin.
  Financial asset price bubbles under model uncertainty.
  *Probability, Uncertainty and Quantitative Risk*, 2(1):14, 2017.
* Biagini et al. (2014)

  F. Biagini, H. Föllmer, and S. Nedelcu.
  Shifting martingale measures and the birth of a bubble as a
  submartingale.
  *Finance and Stochastics*, 18(2):297–326,
  2014.
* Bilina-Falafala et al. (2016)

  R. Bilina-Falafala, R.A. Jarrow, and P. Protter.
  Relative asset price bubbles.
  *Annals of Finance*, 12(2):135–160, 2016.
* Cox and Hobson (2005)

  A. M.G. Cox and D.G. Hobson.
  Local martingales, bubbles and option prices.
  *Finance and Stochastics*, 9(4):477–492,
  2005.
* De Long et al. (1990)

  J.B. De Long, A. Shleifer, L.H. Summers, and R.J. Waldmann.
  Noise trader risk in financial markets.
  *Journal of political Economy*, 98(4):703–738, 1990.
* Denis et al. (2011)

  L. Denis, M. Hu, and S. Peng.
  Function spaces and capacity related to a sublinear expectation:
  Application to g-brownian motion paths.
  *Potential analysis*, 34(2):139–161, 2011.
* Epstein and Ji (2013)

  L. G. Epstein and S. Ji.
  Ambiguous volatility and asset pricing in continuous time.
  *Review of Financial Studies*, 26(7):1740–1786, 2013.
* Epstein and Ji (2014)

  L. G. Epstein and S. Ji.
  Ambiguous volatility, possibility and utility in continuous time.
  *Journal of Mathematical Economics*, 50:269–282,
  2014.
* Epstein and Wang (1995)

  L.G. Epstein and T. Wang.
  Uncertainty, risk-neutral measures and security price booms and
  crashes.
  *Journal of Economic Theory*, 67(1):40–82,
  1995.
* Föllmer et al. (2005)

  H. Föllmer, U. Horst, and A. Kirman.
  Equilibria in financial markets with heterogeneous agents: a
  probabilistic perspective.
  *Journal of Mathematical Economics*, 41(1-2):123–155, 2005.
* Fukuta (1998)

  Y. Fukuta.
  A simple discrete-time approximation of continuous-time bubbles.
  *Journal of Economic Dynamics and control*, 22(6):937–954, 1998.
* Garber (1990)

  P.M. Garber.
  Famous first bubbles.
  *Journal of Economic perspectives*, 4(2):35–54, 1990.
* Harrison and Kreps (1978)

  J.M. Harrison and D.M. Kreps.
  Speculative investor behavior in a stock market with heterogeneous
  expectations.
  *The Quarterly Journal of Economics*, 92(2):323–336, 1978.
* Herdegen and Kreher (2022)

  M. Herdegen and D. Kreher.
  Bubbles in discrete-time models.
  *Finance and Stochastics*, 26(4):899–925,
  2022.
* Herdegen and Schweizer (2016)

  M. Herdegen and M. Schweizer.
  Strong bubbles and strict local martingales.
  *International Journal of Theoretical and Applied Finance*,
  19(4):1650022, 2016.
* Hong et al. (2006)

  H. Hong, J. Scheinkman, and W. Xiong.
  Asset float and speculative bubbles.
  *The journal of finance*, 61(3):1073–1117,
  2006.
* Jarrow (2016)

  R. Jarrow.
  Testing for asset price bubbles: three new approaches.
  *Quantitative Finance Letters*, 4(1):4–9,
  2016.
* Jarrow (2019)

  R. Jarrow.
  Capital asset market equilibrium with liquidity risk, portfolio
  constraints, and asset price bubbles.
  *Mathematics and Financial Economics*, 13(1):115–146, 2019.
* Jarrow and Protter (2012)

  R. Jarrow and P. Protter.
  Discrete versus continuous time models: Local martingales and
  singular processes in asset pricing theory.
  *Finance Research Letters*, 9(2):58–62,
  2012.
* Jarrow et al. (2011a)

  R. Jarrow, Y. Kchia, and P. Protter.
  How to detect an asset bubble.
  *SIAM Journal on Financial Mathematics*, 2(1):839–865, 2011a.
* Jarrow and Protter (2009)

  R. A. Jarrow and P. Protter.
  Forward and futures prices with bubbles.
  *International Journal of Theoretical and Applied Finance*,
  12(07):901–924, 2009.
* Jarrow et al. (2006)

  R. A. Jarrow, P. Protter, and K. Shimbo.
  *Asset price bubbles in a complete market*, pages 105–130.
  In Honor of Dilip B. Madan, 2006.
* Jarrow et al. (2010)

  R. A. Jarrow, P. Protter, and K. Shimbo.
  Asset price bubbles in incomplete markets.
  *Mathematical Finance*, 20(2):145–185,
  2010.
* Jarrow and Kwok (2021)

  R.A. Jarrow and S.S. Kwok.
  Inferring financial bubbles from option data.
  *Journal of Applied Econometrics*, 36(7):1013–1046, 2021.
* Jarrow and Protter (2011)

  R.A. Jarrow and P. Protter.
  Foreign currency bubbles.
  *Review of Derivatives Research*, 14(1):67–83, 2011.
* Jarrow et al. (2011b)

  Robert Jarrow, Younes Kchia, and Philip Protter.
  Is there a bubble in linkedin’s stock price?
  *Portfolio Management Research*, 38(1):125–130, 2011b.
* Kocherlakota (2008)

  N. Kocherlakota.
  Injecting rational bubbles.
  *Journal of Economic Theory*, 142(1):218–232, 2008.
* Kwok (2008)

  Y. K. Kwok.
  *Mathematical models of financial derivatives*.
  Springer, Berlin, 2008.
* Lim (2011)

  B.Y. Lim.
  Short-sale constraints and price bubbles.
  *Journal of Banking and Finance*, 35(9):2443–2453, 2011.
* Loewenstein and Willard (2000)

  M. Loewenstein and G.A. Willard.
  Rational equilibrium asset-pricing bubbles in continuous trading
  models.
  *Journal of Economic Theory*, 91(1):17–58,
  2000.
* Miller (1977)

  E.M. Miller.
  Risk, uncertainty, and divergence of opinion.
  *The Journal of finance*, 32(4):1151–1168,
  1977.
* Peng (1997)

  S. Peng.
  *Backward stochastic differential equations stochastic
  optimization theory and viscosity solutions of HJB equations, in Topics on
  Stochastic Analysis*.
  J. Yan, S. Peng, S. Fang, and L. Wu, Science Press (in Chinese),
  Beijing, 85-138 edition, 1997.
* Peng (1999)

  S. Peng.
  Monotonic limit theorem of bsde and nonlinear decomposition theorem
  of doob-meyers type.
  *Probability Theory and Related Fields*, 113(4):473–499, 1999.
* Peng (2004)

  S. Peng.
  Filtration consistent nonlinear expectations and evaluations of
  contingent claims.
  *Acta Mathematicae Applicatae Sinica*, 20:1–24, 2004.
* Peng (2006)

  S. Peng.
  *Stochastic Analysis and Applications: The Abel Symposium 2005*,
  chapter ”GG-expectation, GG-Brownian motion and related stochastic
  calculus of Itô type”.
  Springer, Berlin Heidelberg, 2006.
* Peng (2008)

  S. Peng.
  Multi-dimensional G-Brownian motion and related stochastic
  calculus under G-expectation.
  *Stochastic Processes and Their Applications*, 118:2223–2253, 2008.
* Peng (2019)

  S. Peng.
  *Nonlinear Expectations and Stochastic Calculus under
  Uncertainty*.
  Springer, Berlin, Heidelberg, 2019.
* Peng and Yang (2022)

  S. Peng and S. Yang.
  Distributional uncertainty of the financial time series measured by
  G-expectation.
  *Theory of Probability and Its Applications*, 66(4):729–741, 2022.
* Peng et al. (2023)

  S. Peng, S. Yang, and J. Yao.
  Improving value-at-risk prediction under model uncertainty.
  *Journal of Financial Econometrics*, 21(1):228–259,
  2023.
* Protter (2013)

  P. Protter.
  *A mathematical theory of financial bubbles*, pages 1–108.
  Springer International Publishing, Cham, 2013.
* Pulido (2014)

  S. Pulido.
  The fundamental theorem of asset pricing, the hedging problem and
  maximal claims in financial markets with short sales prohibitions.
  *The Annals of Applied Probability*, 24(1):54–75, 2014.
* Santos and Woodford (1997)

  M.S. Santos and M. Woodford.
  Rational asset pricing bubbles.
  *Econometrica*, pages 19–57, 1997.
* Schatz and Sornette (2020)

  M. Schatz and D. Sornette.
  Inefficient bubbles and efficient drawdowns in financial markets.
  *International Journal of Theoretical and Applied Finance*,
  23(07):2050047, 2020.
* Scheinkman and Xiong (2003)

  J.A. Scheinkman and W. Xiong.
  Overconfidence and speculative bubbles.
  *Journal of political Economy*, 111(6):1183–1220, 2003.
* Tirole (1982)

  J. Tirole.
  On the possibility of speculation under rational expectations.
  *Econometrica*, 50(5):1163–1181, 1982.
* Yang and Zhang (2024a)

  S. Yang and W. Zhang.
  Asset pricing under model uncertainty with finite time and states.
  *arXiv preprint arXiv:2408.13048*, 2024a.
* Yang and Zhang (2024b)

  S. Yang and W. Zhang.
  Sublinear expectation structure under discrete states space.
  *arXiv preprint arXiv:2403.04324*, 2024b.