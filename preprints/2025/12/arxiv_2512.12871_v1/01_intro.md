---
authors:
- Millend Roy
- Agostino Capponi
- Vladimir Pyltsov
- Yinbo Hu
- Vijay Modi
doc_id: arxiv:2512.12871v1
family_id: arxiv:2512.12871
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'CapOptix: An Options-Framework for Capacity Market Pricing'
url_abs: http://arxiv.org/abs/2512.12871v1
url_html: https://arxiv.org/html/2512.12871v1
venue: arXiv q-fin
version: 1
year: 2025
---


Millend Roy ,
Agostino Capponi ,
Vladimir Pyltsov ,
Yinbo Hu , and Vijay Modi 
Millend Roy and Agostino Capponi are with the Department of
Industrial Engineering and Operations Research, Columbia University, New York 10027, New York, USA (e-mail: millend.roy@columbia.edu; ac3827@columbia.edu). Agostino Capponi holds a courtesy appointment at the Columbia Business School.Vladimir Pyltsov, Yinbo Hu and Vijay Modi are with the Department of Mechanical Engineering, Columbia University, New York 10027, New York, USA (e-mail: v.pyltsov@columbia.edu, yh3184@columbia.edu, modi@columbia.edu).

###### Abstract

Electricity markets are under increasing pressure to maintain reliability amidst rising renewable penetration, demand variability, and occasional price shocks. Traditional capacity market designs often fall short in addressing this by relying on expected-value metrics of energy unserved, which overlook risk exposure in such systems. In this work, we present CapOptix, a capacity pricing framework that interprets capacity commitments as reliability options, i.e., financial derivatives of wholesale electricity prices. CapOptix characterizes the capacity premia charged by accounting for structural price shifts modeled by the Markov Regime Switching Process. We apply the framework to historical price data from multiple electricity markets and compare the resulting premium ranges with existing capacity remuneration mechanisms.

††publicationid: pubid: 0000–0000/00$00.00 © 2025 IEEE

## I Introduction

The global energy transition toward renewable and low-carbon generation introduces fundamental challenges for electricity markets and system operators [kirschen2018fundamentals]. As reliance on intermittent energy sources increases, so does the frequency and intensity of demand-supply imbalances, commonly referred to as security of supply problems [creti2019economics]. These imbalances arising not only from renewable intermittency [IEMRE] but also from extreme weather events, transmission congestion, unplanned outages, or scheduled maintenance, can result in periods of system stress where available generation falls short of demand.

In an energy-only market, generators are compensated solely based on the spot price of electricity, with scarcity-driven price spikes expected to incentivize investment [conejo2016investment]. However, this mechanism fails in practice, leading to what is widely recognized as the missing money problem [stoft2002power], elevating revenue uncertainty [morales2013integrating]. This growing disconnect between the system’s long-term generation adequacy needs and short-term market incentives highlights the necessity of complementary mechanisms like the Capacity Remuneration Mechanism (CRM), which is a set of policy tools explicitly designed to remunerate generators for maintaining available capacity, even when not actively dispatched [creti2019economics].

Several types of CRMs [kirschen2018fundamentals] have been adopted across electricity markets which include: capacity payments, which offer administratively determined compensation for availability (e.g., Portugal [CEER2019\_Portugal], Spain [IEEFA2016\_SpainCapacity]); capacity obligations, which require load-serving entities to contract sufficient capacity to meet expected load (e.g., Midcontinent Independent System Operator (MISO) [MISO2023\_BPM011], California Independent System Operator (CAISO) [CAISO2024\_Section43A]); strategic reserves, where specific plants are withdrawn from the market and retained for emergency use (e.g., Sweden [Svk2023\_CapacityMechanism], Germany [creti2019economics]); and capacity auctions, which rely on market-based price discovery to procure capacity for future delivery (e.g., Pennsylvania, New Jersey, Maryland Interconnection (PJM) [PJMFactSheet2025], New York Independent System Operator (NYISO) [nyiso\_capacity\_market]). A notable variant of the auction approach [capacity\_market\_carmton] is the reliability option, implemented in regions like ISO New England [ISO\_NE\_IMMU\_2008], Italy [RSE\_CapacityMarket\_2024].

While these mechanisms reflect diverse regulatory preferences and market conditions, a unified, risk-sensitive framework for pricing capacity efficiently remains absent. Many suffer from inefficient price signals, rigid administrative rules, or poor alignment with investment risk. For years, the Federal Energy Regulatory Commission (FERC) and some Regional Transmission Organizations (RTOs) have said capacity-market prices are too low [AAGAARD2022101335]. Paradoxically, under the current market design principles, the evidence points the other way [AAGAARD2022101335]: “These markets buy more capacity than what reliability actually needs.”
Because the demand curve is set by administrators, it leads to systematic over-procurement, and consumers end up paying billions for extra capacity they don’t use regularly. Bhagwat et al. [bhagwat2017effectiveness]’s agent-based NYISO Installed Capacity market model, Chattopadhyay et al. [chattopadhyay2015capacity]’s Cournot with transmission, Hach et al. [hach2016capacity]’s dynamic investment, and Bothwell et al. [bothwell2017crediting]’s equilibrium crediting models improve price formation and investment insights but rely on expected values of energy unserved, overlooking extreme scarcity events that dominate high-renewable grids. These events are better captured using jump processes, which are rarely applied to capacity pricing.111A notable exception is Andreis et al. [ANDREIS2020104705], who derive closed-form reliability option premia, but they ignore regime shifts, scarcity-hour illiquidity, and structural market volatility. Jump-diffusion models have instead been widely used for spot price risk management [pricing\_mean\_reverting].

Among the available designs, reliability options (RO) stand out as a market-compatible approach. These are derivative-like contracts that pay generators a premium to supply energy at a capped strike price during scarcity periods. The core idea is to identify all potential events where supply shortfalls and corresponding price spikes may occur, and to compute the aggregate discounted financial impact ahead of time. This aggregated-discounted impact is precisely the compensation, or capacity premium, demanded by generators to supply electricity under these circumstances.

In practice, the premium is discovered through an auction in which generators bid for RO contracts. Motivated by the option-like payoff structure of these contracts, we develop CapOptix, a pricing framework that formalizes the value of the capacity premium using the theory of financial options.222Auction formats (e.g., descending-clock or sealed-bid auctions) determine how generators’ valuations are translated into bids and clearing prices. Our focus in this paper is on the underlying economic value of the reliability option as a contingent claim on scarcity prices, not on strategic bidding behavior. An explicit auction-design analysis would be complementary to, rather than a substitute for, the derivative-based valuation framework we propose.

We simulate a range of possible future price paths to evaluate the expected payoff of the reliability option, thereby deriving the capacity premium as the fair value of that option. Additionally, CapOptix prescribes suitable values for its design parameters, i.e., (i) Strike Price through tail-risk awareness: We prove that the inherent option structure aligns with tail-risk-aware metrics such as Conditional Value-at-Risk (CVaR), enabling strike price selection to be the system’s α\alpha-quantile risk set by the operator (typically, known as option-based portfolio insurance (OBPI) [PeroldSharpe1995]).
(ii) Minimum Contract Duration by cost-revenue break-even: We show that the resulting capacity premia converges to the Net Cost of New Entry (NetCONE)333Check [here](https://www.pjm.com/-/media/committees-groups/committees/mrc/2023/20230920/20230920-item-06---1-local-considerations-of-net-cone---presentation.ashx) and Section [III](https://arxiv.org/html/2512.12871v1#S3 "III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing") for NetCONE details. (a critical benchmark to assess provision of sufficient investment incentives), determining minimum contract durations for investment viability.

We validate the generality and effectiveness of the approach by conducting empirical simulations using real-world data from New York (NYISO), California (CAISO), Texas (ERCOT), Germany, and Italy, each characterized by different levels of price volatility, renewable penetration, and regulatory design. To account for this heterogeneity, CapOptix explores a suite of stochastic processes to model electricity prices, including (i) a mean-reverting process with Poisson jumps, (ii) Generalized Autoregressive Conditional Heteroskedasticity (GARCH) processes [bollerslev1986generalized] with jumps, and (iii) Markov regime-switching models with a mean-reverting behavior that can capture both long-term structural shifts and sudden, rare events such as market shocks or extreme weather-induced supply disruptions. By tailoring the price dynamics to each region’s empirical characteristics, we ensure that the derived capacity premia accurately reflect the local market conditions.

## II Modeling Assumptions and Specifications

We use option pricing theory from finance to accurately estimate capacity premia. In this section, we first list the assumptions for our problem formulation and then dive into the details on how to model it.

###### Assumption 1 (Price-Taking Behavior).

Upon constructing the generation portfolio, the generator retains the right to participate in wholesale electricity markets or engage in forward contracts. The generator works as a price taker, i.e., it can respond to market prices but does not influence them.

###### Assumption 2 (Constant O&M Rate).

We levelize the operating-and-maintenance expense per unit of installed capacity and assume it is constant over the horizon [0,T+τ][0,T+\tau], O&M​(t)=O&M\text{O\&M}(t)\;=\;\text{O\&M} for 0≤t≤T+τ0\leq t\leq T+\tau.

For a price-taking capacity provider, especially for a renewable portfolio player, O&M is typically an order of magnitude smaller than the market-clearing energy price; consequently, modeling time-varying O&M has a negligible effect on the revenue-cost balance and is omitted for tractability.

###### Assumption 3 (Scarcity–pricing).

For every delivery time tt the energy price StS\_{t} satisfies: St=sbaset+φ​(Zt​(ℛ))S\_{t}\;=\;s\_{\text{base}\_{t}}\;+\;\varphi\!\bigl(Z\_{t}(\mathcal{R})\bigr),
where sbasets\_{\text{base}\_{t}} is the energy-only price that is last bid price by the marginal generator, Zt​(ℛ)Z\_{t}(\mathcal{R}) is the *instantaneous generation shortfall i.e. difference between the highest supply bid volume to the lowest demand bid volume*444In reality, it is difficult to analyze shortfall from real-world data since the logged data includes imports to meet the excess demand or demand gets curtailed when not met. Note that StS\_{t} is generally the price of short-term markets like the day-ahead market or real-time market. At times of excess demand, the supply and demand bids do not intersect, leading to extrapolation or shifting of curves to find the non-materialized clearing point.
, and φ:ℝ+→ℝ+\varphi:\mathbb{R}\_{+}\to\mathbb{R}\_{+} is a shortfall to price map, where φ\varphi is strictly increasing for z>0z>0.

Having specified the assumptions, we now present the model.

1. 1.

   At contract initiation (t=0t=0), the capacity provider receives an upfront premium from the load-serving entities (LSEs). Over the preparation horizon [0,T][0,T], the provider undertakes capacity planning and investment to ensure readiness for future delivery obligations.
2. 2.

   Throughout [0,T+τ][0,T+\tau], the provider may participate in wholesale, bilateral, and futures markets to finance infrastructure and manage capital risk.
3. 3.

   During the delivery period [T,T+τ][T,T+\tau], the LSEs hold the option without obligation to procure electricity at the strike price KtK\_{t} whenever market prices exceed it. In such cases, the provider must supply power at KtK\_{t} or refund the difference (St−Kt)(S\_{t}-K\_{t}), ensuring the LSE is fully hedged against scarcity price spikes.

Capacity market contracts commit to clear a fixed capacity QQ for delivery at each interval τi\tau\_{i}. To draw an analogy, electricity delivered during times t=[T,T+τ][T,T+\tau], within the capacity limits of Q, is akin to holding a portfolio of τ\tau options that can be exercised at different maturity dates spanning over T to T+τT+\tau. This is equivalent to a strip of τ\tau European Call Options maturing on successive time intervals from TT to T+τT+\tau, each exercisable if market conditions justify.

This setup enables a tractable formulation for pricing the capacity premium based on classical financial option theory.

###### Proposition 1 (Capacity Premium as a Strip of European Options).

Let {St}t≥0\{S\_{t}\}\_{t\geq 0} denote the stochastic process representing the wholesale electricity spot price. Suppose a capacity contract provides a fixed capacity QQ over the delivery window [T,T+τ][T,T+\tau], where TT is the infrastructure maturity time and τ\tau is the delivery period. The strike price is predetermined as KtK\_{t}555While in practice, the strike price KtK\_{t} varies across delivery intervals [ANDREIS2020104705] due to changes in raw material costs, marginal plant efficiency, or market conditions. Since such fluctuations follow a typical mean-reverting behavior, there exists no persistent drift, and the expected price level remains ”stable” over time. To ensure tractability and to preserve contract attractiveness for LSEs, who value price certainty, while computing our results, we assume a constant KK throughout the contract period. Frequent variations in KtK\_{t} could erode LSE confidence and deter from option contract participation similar to the problem of valuation uncertainty in OTC options [duffie2011dark].
.
Then, the capacity premium C​(0,S0)C(0,S\_{0}) charged per unit of contracted capacity QQ at the initial time t=0t=0 is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(0,S0)=∑t=TT+τe−r​t​𝔼​[(St−Kt)+]​Δ​t\displaystyle C(0,S\_{0})=\sum\_{t=T}^{T+\tau}e^{-rt}\,\mathbb{E}\left[\left(S\_{t}-K\_{t}\right)^{+}\right]\Delta t |  | (1) |

where [⋅]+=max⁡(⋅,0)[\cdot]^{+}=\max(\cdot,0), rr is the risk-free discount and Δ​t\Delta t is the sample time of delivery (e.g., 15 mins or hourly).

Here, we calculate 𝔼​[⋅]\mathbb{E}[\cdot] using the risk-neutral pricing measure666ISO/RTO prices are realized physical prices and are naturally modeled under the historical measure ℙ\mathbb{P}. In contrast, power forwards and futures traded on financial exchanges (e.g., EEX, CME) are priced for hedging and are approximated by risk-neutral expectations. For our empirical results, we work directly under ℙ\mathbb{P}, using realized ISO prices to compute RO premia..

## III Contract Duration for new Capacities

In this section, we estimate one of the key parameters of the option pricing model, i.e., the contract duration τ\tau, which directly influences the premium value.

We start by defining Net Cost of New Entry (N​e​t​C​O​N​ENetCONE) by accounting explicitly for the revenues that a newly constructed generating resource expects to earn from energy and ancillary services (AS) markets.

###### Definition 1 (NetCONE).

NetCONE represents the residual annual revenue required beyond market-based earnings from energy and ancillary services (AS) to ensure new investments in generation capacity are financially viable.

|  |  |  |
| --- | --- | --- |
|  | N​e​t​C​O​N​E=C​O​N​E−𝔼​[Revenue from ​(E​n​e​r​g​y+A​S)]NetCONE=CONE-\mathbb{E}[\text{Revenue from }(Energy+AS)] |  |

where C​O​N​ECONE (Cost of New Entry) is the annualized total fixed cost (capital investment, fixed Operations and Management (O&M), financing) required to build and operate a new generating resource per MW-year.

However, under Reliability Options (RO), capacity providers forgo revenues from energy markets above a strike price KK and are compensated from the upfront R​ORO premium. Consequently, under the RO structure, the premium closely aligns with N​e​t​C​O​N​ENetCONE.

###### Proposition 2.

Under the reliability options framework, the optimal capacity remuneration, i.e., the reliability option premium (CC), is equal to the N​e​t​C​O​N​ENetCONE.

For investment viability, the total expected present value of revenues must equal or exceed the total present value of costs, i.e., P​V​(T​o​t​a​l​R​e​v​e​n​u​e)≥P​V​(T​o​t​a​l​C​o​s​t)PV(TotalRevenue)\geq PV(TotalCost).
From a break-even perspective, the above equation becomes :

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​V​(T​o​t​a​l​R​e​v​e​n​u​e)=P​V​(T​o​t​a​l​C​o​s​t).\displaystyle PV(TotalRevenue)=PV(TotalCost). |  | (2) |

We represent the present value of total cost in terms of C​O​N​ECONE. Since C​O​N​ECONE is an annualized cost 777Continuous discounting is a modeling convenience while summation denotes payments are settled discretely (eg, monthly) in practice., then

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​V​(T​o​t​a​l​C​o​s​t)=∑0T+τe−r​t​C​O​N​E⋅Δ​t.\displaystyle PV(TotalCost)=\sum\_{0}^{T+\tau}e^{-rt}CONE\cdot\Delta t. |  | (3) |

This represents the present value of paying CONE continuously over [0,T] years, discounted at the rate r.

Under ROs as discussed in Section [II](https://arxiv.org/html/2512.12871v1#S2 "II Modeling Assumptions and Specifications ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), the present value of the total revenue comes from:-

* •

  RO Premium (C) : A one-time present-value payment (i.e. ∑TT+τe−r​t​𝔼​[(St−Kt)+]​Δ​t\sum\_{T}^{T+\tau}e^{-rt}\,\mathbb{E}\left[(S\_{t}-K\_{t})^{+}\right]\,\Delta t) at time 0.
* •

  Energy revenues (R1) before the RO contract (0​ to ​T0\text{ to }T): Selling electricity freely at market prices StS\_{t} amounts to ∑0Te−r​t​𝔼​[St]​Δ​t\sum\_{0}^{T}e^{-rt}\,\mathbb{E}[S\_{t}]\,\Delta t.
* •

  Energy revenues (R2) during the RO contract period (T​ to ​T+τT\text{ to }T+\tau): Selling electricity at the capped strike price KtK\_{t} i.e. at min⁡{St,Kt}\min\{S\_{t},K\_{t}\}, aggregates to a value of ∑TT+τe−r​t​𝔼​[min⁡(St,Kt)]​Δ​t\sum\_{T}^{T+\tau}e^{-rt}\,\mathbb{E}\left[\min(S\_{t},K\_{t})\right]\,\Delta t.

Therefore, if we simplify C​O​N​ECONE into capital expenditure (C​a​p​E​xCapEx) and O&MO\&M, and break down the revenue into its constituent terms,
and apply the identity min⁡(St,Kt)+(St−Kt)+=St\min(S\_{t},K\_{t})+(S\_{t}-K\_{t})^{+}=S\_{t}, then the Eq [2](https://arxiv.org/html/2512.12871v1#S3.E2 "In III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing") simplifies to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑0T+τe−r​t​𝔼​[St]​Δ​t=CapEx+O&M⋅∑0T+τe−r​t​Δ​t\displaystyle\sum\_{0}^{T+\tau}e^{-rt}\mathbb{E}[S\_{t}]\,\Delta t=\text{CapEx}+\text{O\&M}\cdot\sum\_{0}^{T+\tau}e^{-rt}\Delta t |  | (4) |

We, then use Eq. [4](https://arxiv.org/html/2512.12871v1#S3.E4 "In III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing") to calculate the minimum required contract duration. The general break-even condition above does not admit a closed-form solution for τ\tau. Therefore, given any expected revenue path, the present value of revenue and cost can be evaluated numerically, and the contract duration τ∗\tau^{\*} can be solved iteratively by increasing the value of τ\tau.

## IV Reliability Metrics and Strike Price

As power systems evolve, driven by high shares of renewable energy and decentralized generation, so too must the metrics used to evaluate capacity adequacy. This section introduces and motivates a shift from traditional adequacy metrics like Expected Energy Unserved (EEU), toward a more risk-aware, distribution-sensitive metric, namely Conditional Value-at-Risk (CVaR), to evaluate reliability and help in capacity procurement. Additionally, here, we discuss how risk aversion can be adjusted by altering the strike price, another key parameter set for calculating the premium.

Here, first we formally define unserved energy (energy defecit) or excess demand at any time tt under a capacity portfolio ℛ\mathcal{R} as Zt​(ℛ)=Dt−Gt​(ℛ)Z\_{t}(\mathcal{R})=D\_{t}-G\_{t}(\mathcal{R}), where DtD\_{t} is the total energy demand and GtG\_{t} includes the available renewable and conventional generation respectively. Let there be nn hours in the contract period τ\tau, for which we assess reliability.

### IV-A Conditional Value-at-Risk (CVaR)

We begin by recalling the definition of CVaR [mcneil2015quantitative]. Let ZZ be a random variable that represents the total unserved energy in the evaluation period, i.e., Z=∑t=1n[Zt]+Z=\sum\_{t=1}^{n}[Z\_{t}]^{+}. We define FZ(.)F\_{Z}(.) as the cumulative distribution function (CDF) of ZZ.

###### Definition 2 (Conditional Value-at-Risk (CVaR)).

Let ZZ be a continuously distributed random variable with finite expectation i.e. 𝔼​[|Z|]<∞\mathbb{E}[|Z|]<\infty and let α∈(0,1)\alpha\in(0,1). We define C​V​a​RαCVaR\_{\alpha} as the conditional expectation of ZZ given that it exceeds the α−q​u​a​n​t​i​l​e\alpha-quantile :

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(Z)\displaystyle\text{CVaR}\_{\alpha}(Z) | =𝔼​[Z∣Z≥qα​(Z)]=11−α​∫α1qu​(Z)​𝑑u\displaystyle=\mathbb{E}[Z\mid Z\geq q\_{\alpha}(Z)]=\frac{1}{1-\alpha}\int\_{\alpha}^{1}q\_{u}(Z)\,du |  |

Intuitively, C​V​a​RαCVaR\_{\alpha} is the EEU in the worst 1−α1-\alpha fraction of the assessment period, where E​E​U=𝔼​[∑t=1n[Zt]+]EEU=\mathbb{E}\left[\sum\_{t=1}^{n}[Z\_{t}]^{+}\right].

###### Proposition 3 (CVaR representation).

As α→0\alpha\to 0, C​V​a​Rα→E​E​UCVaR\_{\alpha}\to EEU and as α→1\alpha\to 1, C​V​a​Rα→ess​sup⁡ZCVaR\_{\alpha}\to\operatorname\*{ess\,sup}Z. This corresponds to the worst case (most extreme) blackout level.

### IV-B Reliability Options align with CVaR of Shortfall

###### Lemma 1 (RO premium as price–tail CVaR).

Let StS\_{t} be continuously distributed energy spot prices with finite expectation at each delivery time t∈[T,T+τ]t\in[T,T+\tau], and fix α∈(0,1)\alpha\in(0,1). Choose the strike so that Kt=qα​(St)K\_{t}=q\_{\alpha}(S\_{t}). Then, the RO premium of Proposition [1](https://arxiv.org/html/2512.12871v1#Thmproposition1 "Proposition 1 (Capacity Premium as a Strip of European Options). ‣ II Modeling Assumptions and Specifications ‣ CapOptix: An Options-Framework for Capacity Market Pricing") can be rewritten in the form of a linear combination of CVaRα​(St)\mathrm{CVaR}\_{\alpha}(S\_{t}) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(0,S0)\displaystyle C(0,S\_{0}) | =∑t=TT+τe−r​t​(1−α)​(CVaRα​(St)−Kt)​Δ​t.\displaystyle=\sum\_{t=T}^{T+\tau}e^{-rt}(1-\alpha)\bigl(\mathrm{CVaR}\_{\alpha}(S\_{t})-K\_{t}\bigr)\Delta t. |  |

###### Definition 3 (Marginal value of lost load (VOLL)).

Let φ:ℝ+→ℝ+\varphi:\mathbb{R}\_{+}\to\mathbb{R}\_{+} be the scarcity map that converts
non-negative shortfall zz into a scarcity adder in price units (e.g., $/MWh).
Then, we define the *marginal VOLL* as VOLL≐φ′​(z)\mathrm{VOLL}\;\doteq\;\varphi^{\prime}(z).

Economically, φ′​(z)\varphi^{\prime}(z) is the marginal scarcity price per additional unit of shortfall and VOLL>0\mathrm{VOLL}>0 asserts that any positive shortfall raises the price by at least a fixed slope.

###### Theorem 1 (Alignment of RO premium with CVaR of shortfall).

Fix α∈(0,1)\alpha\in(0,1) and a delivery time tt. Under the scarcity-pricing Assumption [3](https://arxiv.org/html/2512.12871v1#Thmassumption3 "Assumption 3 (Scarcity–pricing). ‣ II Modeling Assumptions and Specifications ‣ CapOptix: An Options-Framework for Capacity Market Pricing") i.e., St=sbase,t+φ​(Zt+​(ℛ))S\_{t}=s\_{\text{base},t}+\varphi\bigl(Z\_{t}^{+}(\mathcal{R})\bigr), if zα:=qα​(Zt+​(ℛ))z\_{\alpha}:=q\_{\alpha}\bigl(Z\_{t}^{+}(\mathcal{R})\bigr), then
Kt:=qα​(St)=sbase,t+φ​(zα)K\_{t}:=q\_{\alpha}(S\_{t})=s\_{\text{base},t}+\varphi(z\_{\alpha}). Therefore, the RO premium in Proposition [1](https://arxiv.org/html/2512.12871v1#Thmproposition1 "Proposition 1 (Capacity Premium as a Strip of European Options). ‣ II Modeling Assumptions and Specifications ‣ CapOptix: An Options-Framework for Capacity Market Pricing") can be written as, C​(0,S0)C(0,S\_{0}) =

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=TT+τe−r​t​V​O​L​L​(1−α)​(CVaRα​(Zt+​(ℛ))−zα)​Δ​t.\displaystyle\sum\_{t=T}^{T+\tau}e^{-rt}VOLL(1-\alpha)\,\Bigl(\mathrm{CVaR}\_{\alpha}\bigl(Z\_{t}^{+}(\mathcal{R})\bigr)-z\_{\alpha}\Bigr)\Delta t. |  | (5) |

## V Reliability Options as Capacity Auctions

The contractual form of capacity auctions and reliability options on cleared resources diverges in several ways.

###### Definition 4 (CA Payment Stream).

Under a capacity auction, a generator receives the deterministic payment ΠcapCA=M​Q,\Pi^{\textrm{CA}}\_{\text{cap}}=M\,Q,
where MM is the per unit capacity payment in CA, and, when dispatched at time tt, it earns the spot energy revenue of

|  |  |  |
| --- | --- | --- |
|  | ΠengCA​(t)=St​qt,0≤qt≤Q.\Pi^{\textrm{CA}}\_{\text{eng}}(t)=S\_{t}\,q\_{t},\qquad 0\leq q\_{t}\leq Q. |  |

Total payoff in the delivery period of τ\tau is : ΠCA=ΠcapCA+∑0τe−r​t​ΠengCA​(t)​Δ​t\Pi^{\textrm{CA}}=\Pi^{\textrm{CA}}\_{\text{cap}}+\sum\_{0}^{\tau}e^{-rt}\Pi^{\textrm{CA}}\_{\text{eng}}(t)\,\Delta t.

###### Definition 5 (RO Payment Stream).

With an RO, the generator receives the upfront premium ΠpremRO=C​Q,\Pi^{\textrm{RO}}\_{\text{prem}}=C\,Q,
and energy payments as

|  |  |  |
| --- | --- | --- |
|  | ΠengRO​(t)=qt​min⁡(St,K)0≤qt≤Q.\Pi^{\textrm{RO}}\_{\text{eng}}(t)=q\_{t}\min(S\_{t},K)\qquad 0\leq q\_{t}\leq Q. |  |

Hence, total payoff ΠRO=ΠpremRO+∑0τe−r​t​ΠengRO​(t)​Δ​t\Pi^{\textrm{RO}}=\Pi^{\textrm{RO}}\_{\text{prem}}+\sum\_{0}^{\tau}e^{-rt}\Pi^{\textrm{RO}}\_{\text{eng}}(t)\,\Delta t.

###### Proposition 4 (Consumers favour RO over CA).

Suppose ISO sets the RO premium at the CA payment, i.e. C=MC=M. Then,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ΠRO]<𝔼​[ΠCA],whenever ​Pr⁡[St>Kt]>0.\mathbb{E}\!\bigl[\Pi^{\mathrm{RO}}\bigr]\;<\;\mathbb{E}\!\bigl[\Pi^{\mathrm{CA}}\bigr],\qquad\text{whenever }\Pr[S\_{t}>K\_{t}]>0. |  |

###### Remark 1 (Overcompensation by CA).

The proposition formalizes that *capacity payments & uncapped locational marginal prices* over-compensate suppliers relative to the consumer’s risk, whereas RO contracts right-size the transfer by internalizing scarcity-price risk.

## VI Modeling Prices as Stochastic Processes and Premium as Option Derivative

In this section, we present the stochastic models,
focusing on Markov Regime Switching Process (other models are mentioned in Appendix [A](https://arxiv.org/html/2512.12871v1#A1 "Appendix A Other Stochastic Models ‣ CapOptix: An Options-Framework for Capacity Market Pricing")), to represent the underlying dynamics of wholesale electricity prices. These models are essential to capture key characteristics of electricity markets such as pronounced volatility, sudden structural breaks, and abrupt price spikes - that critically influence the valuation of capacity market premia. Price trajectories vary significantly across different electricity markets (Figure [1](https://arxiv.org/html/2512.12871v1#S7.F1 "Figure 1 ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing")). It is evident that no single stochastic model, even with parameter adjustments, is sufficient to capture the full range of observed behaviors. Relying on a model calibrated to a calm historical period risks severely underestimating market risk - a limitation seen in much of the prior literature [ANDREIS2020104705], which often fits a single process to a narrow time window.

To address this, we adopt a Markov Regime-Switching framework. Here, a latent Markov chain captures regime shifts, while the price evolution within each regime is modeled using the most appropriate process. This flexible architecture allows the framework to adapt seamlessly between stable and stressed conditions, avoiding the pitfalls of one-size-fits-all modeling.

### VI-A Distribution Comparison Metrics

Here, we first discuss the statistical distance measures to compare simulated (SS) vs empirical (PP) wholesale energy market price distributions, where prices (StS\_{t}) are expressed in $/MWh. The following statistical distances are used:

* •

  Weighted KL Divergence (W​e​i​g​h​t​e​d​K​Lr​i​g​h​tWeightedKL\_{right}):

  |  |  |  |
  | --- | --- | --- |
  |  | DKL(w)​(P∥S)=∑xw​(x)​P​(x)​log⁡P​(x)S​(x),D\_{\text{KL}}^{(w)}(P\,\|\,S)=\sum\_{x}w(x)\,P(x)\log\frac{P(x)}{S(x)}, |  |

  |  |  |  |
  | --- | --- | --- |
  |  | w​(x)>1​if ​x∈tailw(x)>1\;\;\text{if }x\in\text{tail} |  |

  It is a tail sensitive extension of Kullback–Leibler (KL) divergence, where higher weights are assigned to the right tail of the distribution.
* •

  Tail Wasserstein (TailWass):

  |  |  |  |
  | --- | --- | --- |
  |  | Wα​(P,S)=infγ∈Γ​(P,S)∫x∈tailα|x−y|​𝑑γ​(x,y)W\_{\alpha}(P,S)=\inf\_{\gamma\in\Gamma(P,S)}\int\_{x\in\text{tail}\_{\alpha}}|x-y|\,d\gamma(x,y) |  |

  It is a modification of the Wasserstein distance restricted to the upper tail (e.g., prices above the 95th percentile).

### VI-B Markov Regime Switching Model (MRSM)

Here, we discuss the Markov Regime Switching Model to represent historical prices through distinct states or “regimes”, each governing a different phase of the price process, and assume that the future prices will evolve within one of these estimated regimes.

###### Definition 6 (Markov–Switching AR⁡(p)\operatorname{AR}(p) model).

Let {St}t≥0\{S\_{t}\}\_{t\geq 0} be the (observed) wholesale-price series and {Rt}t≥0\{R\_{t}\}\_{t\geq 0} an unobserved, finite‐state Markov chain taking values in the set of regimes {1,…,R}\{1,\dots,R\}.
The process (of order pp) is specified by the pair of equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=μRt+∑i=1pϕi,Rt​St−i+ϵt\displaystyle S\_{t}=\mu\_{R\_{t}}+\sum\_{i=1}^{p}\phi\_{i,R\_{t}}S\_{t-i}+\epsilon\_{t} |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Rt=j|Rt−1=i)=πi​j,∀i,j∈{1,⋯,R}\displaystyle\mathbb{P}(R\_{t}=j|R\_{t-1}=i)=\pi\_{ij},\quad\forall i,j\in\{1,\cdots,R\} |  | (7) |

with μr\mu\_{r} as regime-specific intercept (long-run mean); ϕi,r\phi\_{i,r} is the autoregressive coefficients of order i=1,…,pi=1,\dots,p in regime rr; εt\varepsilon\_{t} represents i.i.d. innovations εt∼𝒩​(0,σr′⁣ 2)\varepsilon\_{t}\sim\mathcal{N}\!\bigl(0,\sigma\_{r}^{\prime\,2}\bigr) whenever Rt=rR\_{t}=r; and 𝚷=[πi​j]\bm{\Pi}=[\pi\_{ij}] is an R×RR\times R transition matrix of the latent Markov chain which captures the transition probability from one regime to the other.
Equation ([6](https://arxiv.org/html/2512.12871v1#S6.E6 "In Definition 6 (Markov–Switching AR(𝑝) model). ‣ VI-B Markov Regime Switching Model (MRSM) ‣ VI Modeling Prices as Stochastic Processes and Premium as Option Derivative ‣ CapOptix: An Options-Framework for Capacity Market Pricing")) states that *conditional* on the regime Rt=rR\_{t}=r the prices follow an AR⁡(p)\operatorname{AR}(p) with parameters (μr,ϕ1,r,…,ϕp,r,σr′⁣ 2)(\mu\_{r},\phi\_{1,r},\dots,\phi\_{p,r},\sigma\_{r}^{\prime\,2}). Equation ([7](https://arxiv.org/html/2512.12871v1#S6.E7 "In Definition 6 (Markov–Switching AR(𝑝) model). ‣ VI-B Markov Regime Switching Model (MRSM) ‣ VI Modeling Prices as Stochastic Processes and Premium as Option Derivative ‣ CapOptix: An Options-Framework for Capacity Market Pricing")) lets the model switch stochastically between regimes, thereby capturing structural breaks, volatility bursts, or changes in mean reversion that are typical of electricity markets.

Now, even though we observe StS\_{t}, when we sign the contract (i.e., t=0t=0), we do not observe the latent regime state RtR\_{t} at any time tt after signing the contract. So, our goal is to infer RtR\_{t} based on the historical energy prices. This follows the Hamilton Iterative Filtering Algorithm, which is described in Appendix [A-B](https://arxiv.org/html/2512.12871v1#A1.SS2 "A-B Markov Regime Switching Process ‣ Appendix A Other Stochastic Models ‣ CapOptix: An Options-Framework for Capacity Market Pricing"). To get an idea of the number of regimes existing in the historical dataset, we use K-Means clustering and also infer the latent regime state RtR\_{t} for all times tt.

Algorithm 1  Monte Carlo for Markov Regime-Switching OU

1:

2:T,τT,\tau: start and length of capacity delivery windo.w

3:rr: risk-free rate.

4:KK: strike (capacity cap price).

5:S0,R0S\_{0},R\_{0}: initial value of the OU process and regime.

6:{κr,θr,σr}\{\kappa\_{r},\theta\_{r},\sigma\_{r}\}: OU parameters for each regime rr.

7:π\pi: transition matrix or generator for Markov chain {Rt}\{R\_{t}\}

8:NpathsN\_{\text{paths}}: number of Monte Carlo sample paths

9:NN: number of time steps from TT to T+τT+\tau

10:Δ​upre←TNpre\Delta u\_{\text{pre}}\leftarrow\frac{T}{N\_{\text{pre}}} ⊳\triangleright Time step from 0 to TT

11:Δ​u←τN\Delta u\leftarrow\frac{\tau}{N} ⊳\triangleright Time step from TT to T+τT+\tau

12:capacityPremium ←0\leftarrow 0

13:for p=1p=1 to NpathsN\_{\text{paths}} do

14:  (S,R)←(S0,R0)(S,R)\leftarrow(S\_{0},R\_{0})

15:  for k=1k=1 to NpreN\_{\text{pre}} do

16:   R←sample\_next\_regime​(R,π,Δ​upre)R\leftarrow\text{sample\\_next\\_regime}(R,\pi,\Delta u\_{\text{pre}})

17:   S←OU\_step​(S,κR,θR,σR,Δ​upre)S\leftarrow\text{OU\\_step}(S,\kappa\_{R},\theta\_{R},\sigma\_{R},\Delta u\_{\text{pre}})

18:  end for

19:  sumPayoff←0\text{sumPayoff}\leftarrow 0

20:  for k=0k=0 to NN do

21:   uk←T+k⋅Δ​uu\_{k}\leftarrow T+k\cdot\Delta u

22:   R←sample\_next\_regime​(R,π,Δ​u)R\leftarrow\text{sample\\_next\\_regime}(R,\pi,\Delta u)

23:   S←OU\_step​(S,κR,θR,σR,Δ​u)S\leftarrow\text{OU\\_step}(S,\kappa\_{R},\theta\_{R},\sigma\_{R},\Delta u)

24:   payoff←max⁡(S−K, 0)\texttt{payoff}\leftarrow\max(S-K,\,0)

25:   discf←exp⁡(−r⋅uk)\texttt{discf}\leftarrow\exp(-r\cdot u\_{k})

26:   sumPayoff←sumPayoff+payoff⋅discf⋅Δ​u\text{sumPayoff}\leftarrow\text{sumPayoff}+\texttt{payoff}\cdot\texttt{discf}\cdot\Delta u

27:  end for

28:  pathPremium​[p]←sumPayoff\texttt{pathPremium}[p]\leftarrow\text{sumPayoff}

29:end for

30:capacityPremium←1Npaths​∑p=1NpathspathPremium​[p]\texttt{capacityPremium}\leftarrow\frac{1}{N\_{\text{paths}}}\sum\_{p=1}^{N\_{\text{paths}}}\texttt{pathPremium}[p]

31:return capacityPremium

Next, for each regime r∈Rtr\in R\_{t}, we couple the MRSM model with the mean-reverting OU process. Therefore, the final capacity premium charged at time t=0t=0 is given by: C​(0,S0)=∑t=TT+τe−r​t​𝔼​[{St−K}+|S0,R0]​Δ​tC(0,S\_{0})=\sum\_{t=T}^{T+\tau}e^{-rt}\mathbb{E}[\{S\_{t}-K\}^{+}|S\_{0},R\_{0}]\Delta t. But now, 𝔼​[{St−K}+|S0,R0]\mathbb{E}[\{S\_{t}-K\}^{+}|S\_{0},R\_{0}] must account for all possible regime paths that the Markov chain RtR\_{t} may take between time 0 and t. Because each regime has different OU parameters, we can not have a closed-form solution for the model. The distribution of StS\_{t} being a mixture of normals conditional on the path of regimes makes it all the more difficult.

Therefore, we use Monte Carlo Simulation as described in Algorithm [1](https://arxiv.org/html/2512.12871v1#alg1 "Algorithm 1 ‣ VI-B Markov Regime Switching Model (MRSM) ‣ VI Modeling Prices as Stochastic Processes and Premium as Option Derivative ‣ CapOptix: An Options-Framework for Capacity Market Pricing") to simulate many paths of {Rt}\{R\_{t}\} and {St}\{S\_{t}\} from t=Tt=T to T+τT+\tau, to come up with the final capacity premium.

## VII Experiments and Results

![Refer to caption](images/prices_NYISO.png)


(a) New York (NYISO): Energy price series from 2016 to 2024. Sharp spikes, alongside brief negative prices are visible despite lower average volatility.

![Refer to caption](images/prices_Germany.png)


(b) Germany: Day-ahead prices from 2019 to 2024, capturing long-term stability and recent disruptions from 2022 onwards.

Figure 1: Electricity prices across NYISO, and Germany.

For our analysis, we retrieve publicly available electricity price (e.g., see Figure [1](https://arxiv.org/html/2512.12871v1#S7.F1 "Figure 1 ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing")), consumption, and generation data from multiple regional sources.
(i) Data for New York is sourced from the NYISO [Settlement archives](https://www.nyiso.com/energy-market-operational-data), which include historical 5-minute cleared real-time price information and capacity allocations monthly. These prices are averaged across 11 load zones, weighted by zonal loads at each hour. (ii) In the case of CAISO, we use hourly day-ahead price data from the [U.S. Energy Information Administration (EIA)](https://www.eia.gov/electricity/wholesalemarkets/data.php?rto=caiso) and average them across three zones (NP-15, SP-15, and ZP-26). (iii) Similarly, we use the average day-ahead bus price data from the [EIA](https://www.eia.gov/electricity/wholesalemarkets/data.php?rto=ercot) to model Electric Reliability Council of Texas (ERCOT) prices. (iv) German energy price data is retrieved from the [SMARD (Strommarktdaten) platform](https://www.smard.de/home/downloadcenter/download-marktdaten/), operated by the German Federal Network Agency. We use hourly day-ahead prices for the DE/LU bidding zone. (v) For Italy, we rely on day-ahead price and dispatch data from the [Gestore Mercati Energetici](https://dati.terna.it/download-center#/fabbisogno/fabbisogno-italia) (GMI - the Italian Power Exchange).

### VII-A Case Study: Capacity Premium in Germany

The German spot market offers a vivid natural experiment in *exogenous regime changes*: (i) the 2018-2021 oversupply of renewables that depressed prices to negative values and (ii) the price increase for 2021-2023. Each episode created a distinct state characterized by a dramatically different mean value and volatility that an ISO must price into forward capacity contracts. We use SMARD hourly prices from January 2019 to March 2024 (Figure [1](https://arxiv.org/html/2512.12871v1#S7.F1 "Figure 1 ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing")b).

#### Rolling-window features and K-Means Clustering.

To capture these structural breaks, we engineer a 30-day rolling *Mean*, *Volatility*, and *Log-Return*. The elbow test on kk-means inertia produces a value of k=3k=3 as the best number of clusters observed from the data. Therefore, we next use Markov Autoregression using 3 regimes.

#### Markov Auto-Regession.

From the Bayesian Information Criterion (BIC) (we check this for each regime), we see a strong decay after lag 2 but significant dependencies till a lag of 24. Now, Markov Autoregression requires conditioning on both past observations and past regimes. The likelihood involves terms of the form: P(St|St−1,…,St−p,Rt,…,Rt−p)P\left(S\_{t}\middle|S\_{t-1},\dots,S\_{t-p},R\_{t},\dots,R\_{t-p}\right), which depend on an unobserved sequence of latent regimes. As a result, maximum-likelihood estimation (MLE) suffers from exponential path explosion: for lag order pp and kk regimes, the likelihood marginalizes over kp+1k^{p+1} possible regime paths, rendering direct estimation computationally prohibitive.
So, we stick to a lower order of 2. We, therefore, restrict our attention to the AR(pp) model with p=2p=2 and run Markov AutoRegression with 3 state regimes (Figure [2(a)](https://arxiv.org/html/2512.12871v1#S7.F2.sf1 "In Figure 2 ‣ Markov Auto-Regession. ‣ VII-A Case Study: Capacity Premium in Germany ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing")). The parameters for each of the regimes are summarized in Table [I](https://arxiv.org/html/2512.12871v1#S7.T1 "TABLE I ‣ Markov Auto-Regession. ‣ VII-A Case Study: Capacity Premium in Germany ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing").

![Refer to caption](images/regimes_MAR.png)


(a) Regimes from MRSM.

![Refer to caption](images/LHS_RHS.png)


(b) Contract Duration: τ∼6\tau\sim 6 yrs.

Figure 2: MRSM regimes and contract-duration with C​a​p​E​x=1,290,806CapEx=1{,}290{,}806 €/MW, and O&M=52O\&M=52k €/MW-yr.




TABLE I: Parameters for the 3-state AutoRegression Process.

| Regime | Constant | σ′⁣2\sigma^{\prime 2} | AR(1) | AR(2) | Mean | Var |
| --- | --- | --- | --- | --- | --- | --- |
| 2 (Low) | 84.02 | 21.42 | 1.48 | -0.48 | 41.89 | 531.30 |
| 0 (Med) | 115.07 | 214.24 | 1.47 | -0.52 | 115.66 | 4622.64 |
| 1 (High) | 326.55 | 1174.99 | 1.51 | -0.56 | 301.45 | 23725.24 |




TABLE II: OU parameters, from AR-derived matrices.

| Regime | κ\kappa | θ\theta | σ\sigma |
| --- | --- | --- | --- |
| 2 (Low) | 264.94 | 41.89 | 531.05 |
| 0 (Med) | 324.25 | 115.66 | 1730.65 |
| 1 (High) | 320.45 | 301.45 | 3897.34 |

#### OU Process Estimation for each regime.

We then compute the MLE parameters of the underlying OU process for each regime, which is described in Table [II](https://arxiv.org/html/2512.12871v1#S7.T2 "TABLE II ‣ Markov Auto-Regession. ‣ VII-A Case Study: Capacity Premium in Germany ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing").

#### Calculating Contract Duration τ\tau.

From Section [III](https://arxiv.org/html/2512.12871v1#S3 "III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), we confirm that under a properly calibrated RO contract for a natural gas combined cycle (NGCC) based energy producer, τ=6\tau=6 years is necessary and sufficient for the cost recovery of C​a​p​E​xCapEx and O&MO\&M expenditures (Figure [2(b)](https://arxiv.org/html/2512.12871v1#S7.F2.sf2 "In Figure 2 ‣ Markov Auto-Regession. ‣ VII-A Case Study: Capacity Premium in Germany ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing")) 888The CapEx anchor $1.291M/MW ($1,291/kW) sits within recent NGCC capital-cost ranges ([Lazard LCOE 2025, see p. 36](https://www.lazard.com/media/eijnqja3/lazards-lcoeplus-june-2025.pdf): $1,200–$1,600/kW). The O&MO\&M assumption $52k/MW-yr is conservative but consistent with U.S. capacity-market studies when firm gas, property tax, and insurance are included (PJM 2025 CONE mentioned [here](https://www.pjm.com/-/media/DotCom/committees-groups/committees/mic/2025/20250221-special/pjm-qr-cone-and-vrr-curve-deck.pdf) says levelized fixed O&M ≈\approx $38–$60/kW-yr across zones)..

#### Premia Charged.

The final capacity premium charged at time t=0t=0, for T = 1 yrs, τ\tau = 6 yrs, K = 150 €/MWh, r = 2.64%, is then given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(0,S0)⏟€M​W\displaystyle\underbrace{C(0,S\_{0})}\_{\frac{\text{\texteuro}}{MW}} | =∑t=TT+τe−r​t​𝔼​[{St−K}+|S0,R0]⏟€M​W​h​Δ​t⏟1​h​r\displaystyle=\sum\_{t=T}^{T+\tau}e^{-rt}\underbrace{\mathbb{E}[\{S\_{t}-K\}^{+}|S\_{0},R\_{0}]}\_{\frac{\text{\texteuro}}{MWh}}\underbrace{\Delta t}\_{1hr} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =294,775.92​ €/M​W\displaystyle=294,775.92\text{ \texteuro}/MW |  |

Let’s denote AA as the levelized annual premium (€/MWyr). Because the premium is paid at the *start* of each year, its present value is C=∑n=0τ−1A​e−r​nC=\sum\_{n=0}^{\tau-1}A\,e^{-rn}. Hence the levelized annual payment is A=C/(∑n=0τ−1e−r​n)A=C/({\sum\_{n=0}^{\tau-1}e^{-rn}}). If instead the premium were paid *continuously* over the interval [T,T+τ][T,T+\tau], the equivalence condition becomes
A=C​r/(1−e−r​τ)A=\;Cr/({1-e^{-r\tau}}). This yields the premium as € ​52,428/M​W​y​r\text{\texteuro }52,428/MWyr.

![Refer to caption](images/sensitivityanalysis_tau1.png)

![Refer to caption](images/sensitivityanalysis_tau2.png)

Figure 3: Sensitivity Analysis of Premium with respect to τ\tau, by varying TT, rr and KK.



![Refer to caption](images/sensitivity_K1.png)

![Refer to caption](images/sensitivity_K2.png)

Figure 4: Sensitivity Analysis of Premium with respect to KK, by varying TT, rr and τ\tau.

#### Sensitivity Analysis of Capacity Premium in Germany.

To understand how market design parameters affect the reliability option premium in Germany, we conduct a sensitivity analysis with respect to contract duration (τ\tau) and strike price (KK). Figure [3](https://arxiv.org/html/2512.12871v1#S7.F3 "Figure 3 ‣ Premia Charged. ‣ VII-A Case Study: Capacity Premium in Germany ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing") and [4](https://arxiv.org/html/2512.12871v1#S7.F4 "Figure 4 ‣ Premia Charged. ‣ VII-A Case Study: Capacity Premium in Germany ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing") show that the premium is highly sensitive to both factors. Longer contract durations yield significantly higher premia, as they ensure more prolonged protection against scarcity events, increasing the expected payoff of the option. However premium charged per year for each MW decreases with the increase in contract duration, which proves the sub-linear growth of premium values.

Higher strikes make the option cheaper since it triggers less often and pays less when it does, especially in Germany, where outsized spikes are rare. The shaded area shows how results change when we vary contract length, discount rate, and the threshold. On the right, we show the same relationship but annualized to € per MW-year; annualizing removes most of the variation.
These relationships are nonlinear and emphasize the need for regulators to carefully calibrate τ\tau and KK to ensure investor incentives while guaranteeing system adequacy.

### VII-B Empirical Benchmarking - Comparison of ROs with Existing Mechanisms in different electricity markets

TABLE III: Goodness-of-fit metrics comparing simulated price distributions against observed prices across regions.

| Region | Model Name | W​e​i​g​h​t​e​d​K​Lr​i​g​h​tWeightedKL\_{right} | TailWass |
| --- | --- | --- | --- |
| Texas (ERCOT) | MRSM-OU | 1.73 | ×\times |
| OU-jumps | 0.09 | 454.12 |
| GARCH | 0.05 | 147.93 |
| New York (NYISO) | MRSM-OU | 0.82 | ×\times |
| OU-jumps | 0.0014 | 51.04 |
| GARCH | 0.0009 | 6.44 |
| California (CAISO) | MRSM-OU | 2.29 | ×\times |
| OU-jumps | 0.013 | 48.19 |
| GARCH | 0.017 | 79.27 |
| Italy | MRSM-OU | 0.008 | 9.71 |
| OU-jumps | 0.063 | 95.45 |
| GARCH | 0.041 | 78.28 |
| Germany | MRSM-OU | 0.21 | 46.21 |
| OU-jumps | 0.26 | 79.84 |
| GARCH | 0.32 | 318.33 |




TABLE IV: Comparing capacity pricing mechanisms across selected electricity markets.
CRM payments for ROs reflect only premium values computed at the minimum contract duration for viability.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Region | Model Fitted (with jumps) | Regime | Spot Price Dynamics | | CRM | Strike Price (K) | Min. Contract | CRM Payment | Energy-only Rev |
| μ\mu | σ\sigma | type | (-/MWh) | Duration (τ\tau yrs) | (-/MWyr) | (-/MWyr) |
| Texas (ERCOT) | GARCH | – | 56.02 | 380.45 | – | – | – | – | 417.5k $ |
| RO | 284.29 $ | 5 | 71k $ | 296k $ |
| New York (NYISO) | GARCH | – | 36.44 | 49.90 | CA | – | 8 | 23k $ | 311k $ |
| RO | 90.91 $ | 8 | 16k $ | 297k $ |
| California (CAISO) | OU | – | 51.13 | 57.74 | CO | – | 1 | 100k $ | 497k $ |
| RO | 135.71 $ | 3 | 21k $ | 450k $ |
| Italy | MRSM-OU | R1 | 66.96 | 32.29 | RO | 85 € | 15 | 70k € | 728k € |
| R2 | 306.52 | 115.76 | RO | 85 € | 2 | 11k € | 728k € |
| Germany | MRSM-OU | R1 | 33.76 | 9.23 | SR RO | – 125 € | 2 6 | 63k € 52k € | – 540k € |
| R2 | 82.84 | 27.86 |
| R3 | 216.73 | 107.49 |

Based on the tail-sensitive metrics from Table [III](https://arxiv.org/html/2512.12871v1#S7.T3 "TABLE III ‣ VII-B Empirical Benchmarking - Comparison of ROs with Existing Mechanisms in different electricity markets ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), we select the best model for each region to compute the capacity premia.

Table [IV](https://arxiv.org/html/2512.12871v1#S7.T4 "TABLE IV ‣ VII-B Empirical Benchmarking - Comparison of ROs with Existing Mechanisms in different electricity markets ‣ VII Experiments and Results ‣ CapOptix: An Options-Framework for Capacity Market Pricing") compares our reliability-option (RO) valuations against two polar cases.
At one end is the *energy-only* paradigm - Texas (ERCOT), where generators rely solely on spot-market earnings. Given the distribution of Texas energy prices, a GARCH model with jumps provides the best fit. We set α=0.95\alpha=0.95 to model the strike price, yielding K=284.29​$/MWhK=284.29\mathdollar/\text{MWh}. Break-even analysis indicates a minimum contract duration of five years for project viability through ROs.
In theory, if the strike price KK and premium CC satisfy the “option-parity” identity used in Eq [4](https://arxiv.org/html/2512.12871v1#S3.E4 "In III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), the present value of an energy-only stream should equal that of an RO stream (premium plus capped energy). In practice, if we consider revenues earned across all operating hours for a five-year horizon, the levelized energy-only income rises to $417.5k/MW-yr999If reserves fall dangerously low, ERCOT declares emergency conditions and deploys pre-arranged interruptible load resources, which are paid (check [Emergency Response Services](https://www.ercot.com/services/programs/load/eils) for reference) to stop using power immediately. In our baseline calculations, we abstract out such emergency intervention payments. Explicitly modeling such payments would further narrow the gap between the baseline and ROs., with a present value of $1.99M/MW, that is about 12% higher than the $1.75M/MW (combined capacity and energy revenues) obtained under ROs. This gap of 12% reflects the model-driven error of the fitted stochastic process’s representation of ERCOT prices.

At the other extreme are the existing capacity mechanisms:

(i) The New York Independent System Operator (NYISO) procures capacity through a statewide Installed Capacity (ICAP) market101010It serves as the reference capacity zone for the entire state, but excluding transmission-constrained areas such as NYC and Zones H, I, and K. These constrained zones clear at higher prices due to local deliverability limits, while the statewide reference zone reflects unconstrained conditions..
Based on NYISO historical ICAP data from 2011–2022, the average clearing price in the statewide reference zone is approximately $23k/MW-yr, which we adopt as the capacity payment in our net present value (NPV) analysis [nyiso\_capacity\_market]. From the break-even analysis, we calculate an eight-year contract duration (considering NYISO’s annual capacity obligation reset) for both ROs and CAs. Additionally, for ROs, we set a strike price of $90.91/MWh (i.e., from α=0.95\alpha=0.95). When compared to the RO premium estimate of $16 k/MW-yr, the two mechanisms exhibit near-parity (the $7k/MWyr gap in the CRM payments can be easily closed using an auction process). This suggests that, at the statewide level, an RO design could deliver comparable cost recovery for generators as the existing ICAP construct. The slightly higher energy revenue for CAs is a result of Remark [1](https://arxiv.org/html/2512.12871v1#Thmremark1 "Remark 1 (Overcompensation by CA). ‣ V Reliability Options as Capacity Auctions ‣ CapOptix: An Options-Framework for Capacity Market Pricing") indicating over-compensation.

(ii) California’s Capacity Obligation (CO) mechanism is implemented through the Resource Adequacy (RA) program, overseen by the California Public Utilities Commission [CAISO2024\_Section43A]. We use the 2022 Average Price111111Check Section 4, Table 6 of the 2022 Resource Adequacy Report [here](https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/energy-division/documents/resource-adequacy-homepage/2022-ra-report_05022024.pdf). of $8.31/kW-month - assuming this rate is levelized across the year. Converting to a $/MW-yr basis, we get $ 99,720/MW-yr, which is much higher (almost 5×5\times, unlikely that such a gap could be closed through auction adjustments alone) than the premium payment of $21k /MW-yr estimated by ROs. We assume a one-year contract duration, as prices are recalibrated annually based on Load Serving Entity (LSE) filings, for COs. On the other hand, the strike price and the contract duration are set as $ 135.71/MWh (from α=0.95\alpha=0.95) and 3 years (from break-even analysis), respectively. Thus, this fixed capacity payment still leads to over-compensation, similar to our findings in the NYISO case.

(iii) The Italian capacity market uses ROs as CRMs. They clear prices for existing (1-year contracts) and new capacity (15-year contracts) separately [RSE\_CapacityMarket\_2024]. From the 2024 auction, a new capacity entrant receives €70,000/MW-yr. The scheme follows a reliability options design with a daily updated strike price linked to MGP-GAS and MI-GAS market prices; for simplicity, we hold it fixed at the peaker reference level of €85/MWh (2018–2019)121212Check strike price on page 2 of the [ARERA Strategic Plan 2019-2021](https://www.arera.it/fileadmin/allegati/audizioni/pubbliche/19/EFET.pdf).. Notably, this legacy RO tariff no longer reflects post-2022 volatility, potentially inflating premia. A regime-switching approach, thus, could better capture such structural shifts (although sufficient data per regime remains a limitation) and can bring down the cost to the consumers.

(iv) The German capacity framework operates under a strategic reserve (SR) model, structured into three reserve categories: grid reserves (primarily for redispatch), capacity reserves (for resource adequacy), and security standbys131313Check [here](https://systemmarkt.net/Mediathek/20221207_Strategic_Reserves_SysteMarket.pdf) for details on capacity remuneration in Germany.. Capacity reserves141414Check [here](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Versorgungssicherheit/KapRes/start.html) for details on capacity reserves. are auction-based and are contracted for two-year periods. For the 2022–2024 performance period, the capacity reserve auction cleared at €62,940/MW-year151515Check [here](https://www.netztransparenz.de/en/Ancillary-Services/System-operations/Capacity-reserve/Publications-on-the-2022-2024-performance-period) for the levy value for capacity reserve plants.. Participation in the SR mechanism requires generators to withdraw from the regular energy market, thus resulting in no revenues earned from the energy-only market. Comparing this with ROs, by setting a strike price of €125/MWh161616See [here](https://www.arera.it/fileadmin/allegati/docs/17/592-17.pdf) for details in latest economic parameters. and contract duration of 6 years, we are able to achieve a higher net income (of almost €1.5M/MW) for the generators sufficient for cost recovery.
  
Together, these findings highlight how well-calibrated ROs occupy a middle ground: they close the missing-money gap without imposing the systematic over-payments.

## VIII Conclusion

In summary, CapOptix is a financial options–based framework that calibrates reliability options to deliver realistic, risk-adjusted incentives. Using a modular stochastic engine built on regime-switching, Ornstein–Uhlenbeck, and jump–diffusion dynamics, we show through multi-region simulations for New York, California, Texas, Italy, and Germany that reliability options priced via CapOptix can recover costs while aligning generator incentives with system reliability, outperforming traditional mechanisms such as capacity auctions, strategic reserves, and centralized obligations in terms of preserving market signals and providing effective hedging against scarcity-driven price volatility. Our results indicate that CapOptix yields economically meaningful premia and contract durations that mitigate overpayment yet secure investment, offering regulators and system operators a transparent design tool.

## Appendix A Other Stochastic Models

### A-A Mean-Reverting Ornstein-Uhlenbeck (OU) Process

In many electricity markets, especially those with relatively stable supply-demand dynamics, prices tend to exhibit mean-reverting behavior.
We model it using an OU process [uhlenbeck1930theory]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=κ​(θ−St)​d​t+σ​d​Wt,∀t∈[0,T+τ]\displaystyle dS\_{t}=\kappa(\theta-S\_{t})dt+\sigma dW\_{t},\forall t\in[0,T+\tau] |  | (8) |

where, θ\theta is the long-term mean and κ>0\kappa>0 is the speed of mean reversion. We estimate these parameters by maximizing the log-likelihood of the observed data.

###### Lemma 2 (OU Process is Gaussian and Stationary).

The solution to the Ornstein–Uhlenbeck process is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​e−κ​t+θ​(1−e−κ​t)+σ​∫0te−κ​(t−s)​𝑑Ws.\displaystyle S\_{t}=S\_{0}e^{-\kappa t}+\theta(1-e^{-\kappa t})+\sigma\int\_{0}^{t}e^{-\kappa(t-s)}dW\_{s}. |  | (9) |

Then, St∼𝒩​(μt,σt2)S\_{t}\sim\mathcal{N}(\mu\_{t},\sigma\_{t}^{2}), where μt=S0​e−κ​t+θ​(1−e−κ​t),\mu\_{t}=S\_{0}e^{-\kappa t}+\theta(1-e^{-\kappa t}), and σt2=σ22​κ​(1−e−2​κ​t)\sigma\_{t}^{2}=\frac{\sigma^{2}}{2\kappa}(1-e^{-2\kappa t}).

To model the infrequent energy price spikes, we now extend the OU model by introducing a jump component as follows:

###### Assumption 4 (Jumps).

Jumps have two components -

(i) Size of jumps: We assume the size of the jumps YtY\_{t} are normally distributed (i.e. Yt∼𝒩​(μy,σy2)Y\_{t}\sim\mathcal{N}(\mu\_{y},\sigma\_{y}^{2})).

(ii) Arrivals: We assume that Jump arrivals (NtN\_{t}) follow Poisson​(λ)\text{Poisson}(\lambda) to count the number of jumps up to time tt, where λ\lambda denotes the average jump intensity.
Therefore, the change in the number of jumps over a small interval is :

|  |  |  |
| --- | --- | --- |
|  | d​Nt={1,with probability ​(λ​d​t)0,with probability ​(1−λ​d​t)dN\_{t}=\begin{cases}1,&\text{with probability }(\lambda dt)\\ 0,&\text{with probability }(1-\lambda dt)\end{cases} |  |

The Jump component is independent to the Brownian Motion and the Jump size is independent of the arrivals.

This accounts for rare but significant price disruptions due to market shocks. Hence,

|  |  |  |
| --- | --- | --- |
|  | d​St=κ​(θ−St)​d​t+σ​d​Wt+Yt⋅d​Nt.\displaystyle dS\_{t}=\kappa(\theta-S\_{t})dt+\sigma dW\_{t}+Y\_{t}\cdot dN\_{t}. |  |

Due to the compound nature of the jumps and the absence of closed-form expressions for the option value, we estimate the capacity premium using Monte Carlo simulations.

### A-B Markov Regime Switching Process

###### Definition 7 (Filtered regime probability).

For each regime j∈{1,…,R}j\in\{1,\dots,R\} define

|  |  |  |
| --- | --- | --- |
|  | εj,t=ℙ​(Rt=j|Ωt;θ)Ωt:={St,St−1,…},\varepsilon\_{j,t}=\mathbb{P}(R\_{t}=j|\Omega\_{t};\theta)\qquad\Omega\_{t}:=\{S\_{t},S\_{t-1},\dots\}, |  |

i.e. the posterior probability that the system is in regime jj after observing prices up to tt.

In the above equation, θ\theta represents the parameter set from historical price data. Each regime j is defined by the parameter set θj={μj,ϕ1,j,⋯,ϕp,j,σj2}\theta\_{j}=\{\mu\_{j},\phi\_{1,j},\cdots,\phi\_{p,j},\sigma\_{j}^{2}\}. The full model includes - regime switching parameters {θ1,⋯,θR}\{\theta\_{1},\cdots,\theta\_{R}\} and transition probabilities πi.j\pi\_{i.j} as parameters. To estimate the parameters (θ\theta) of the model, we maximize the log-likelihood of the observed data. Since no closed-form solution exists, we use gradient-based methods like L−B​F​G​SL-BFGS to solve it.

###### Lemma 3 (Hamilton filter recursion [hamilton1989]).

Given filtered probabilities εi,t−1\varepsilon\_{i,t-1} for all ii, the one-step prediction ε~j,t\tilde{\varepsilon}\_{j,t}, observation likelihood ℒt(j)\mathcal{L}\_{t}^{(j)}, normalizing constant LtL\_{t}, and posterior update εj,t\varepsilon\_{j,t} are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε~j,t\displaystyle\tilde{\varepsilon}\_{j,t} | :=∑i=1Rπi​j​εi,t−1,ℒt(j):=12​π​σj′⁣2​exp⁡{−(St−S^t(j))22​σj′⁣2},\displaystyle:=\sum\_{i=1}^{R}\pi\_{ij}\,\varepsilon\_{i,t-1},\quad\mathcal{L}\_{t}^{(j)}:=\frac{1}{\sqrt{2\pi\sigma\_{j}^{\prime 2}}}\,\exp\!\Bigl\{-\tfrac{(S\_{t}-\hat{S}\_{t}^{(j)})^{2}}{2\sigma\_{j}^{\prime 2}}\Bigr\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt\displaystyle L\_{t} | :=∑j=1Rε~j,t​ℒt(j),εj,t:=ε~j,t​ℒt(j)Lt,\displaystyle:=\sum\_{j=1}^{R}\tilde{\varepsilon}\_{j,t}\,\mathcal{L}\_{t}^{(j)},\quad\varepsilon\_{j,t}:=\frac{\tilde{\varepsilon}\_{j,t}\,\mathcal{L}\_{t}^{(j)}}{L\_{t}}, |  |

where
S^t(j)=μj+∑k=1pϕk,j​St−k.\hat{S}\_{t}^{(j)}=\mu\_{j}+\sum\_{k=1}^{p}\phi\_{k,j}S\_{t-k}.

###### Lemma 4 (Discrete–to–continuous mapping, single–order case).

Fix a regime r∈{1,…,R}r\in\{1,\dots,R\} and sampling step Δ​t>0\Delta t>0. Assume the price dynamics in that regime are observed at integer multiples of Δ​t\Delta t and satisfy the AR(1)

|  |  |  |
| --- | --- | --- |
|  | St+Δ​t=μr+ϕ1,r​St+εt+Δ​t,εt+Δ​t∼𝒩​(0,σr′⁣ 2).S\_{t+\Delta t}\;=\;\mu\_{r}+\phi\_{1,r}\,S\_{t}+\varepsilon\_{t+\Delta t},\qquad\varepsilon\_{t+\Delta t}\sim\mathcal{N}(0,\sigma\_{r}^{\prime\,2}). |  |

Then there exists a scalar OU process for s∈[t,t+Δ​t)s\in[t,t+\Delta t), d​Ss=κr​(θr−Ss)​d​s+σr​d​WsdS\_{s}\;=\;\kappa\_{r}\!\bigl(\theta\_{r}-S\_{s}\bigr)\,ds+\sigma\_{r}\,dW\_{s},
with parameters (in terms of AR(1) parameters) given by :

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | κr\displaystyle\kappa\_{r} | =−ln⁡ϕ1,rΔ​t,\displaystyle=-\frac{\ln\phi\_{1,r}}{\Delta t}, | θr\displaystyle\theta\_{r} | =μr1−ϕ1,r,\displaystyle=\frac{\mu\_{r}}{1-\phi\_{1,r}}, | σr\displaystyle\sigma\_{r} | =σr′Δ​t​2​ln⁡ϕ1,rϕ1,r2−1.\displaystyle=\frac{\sigma\_{r}^{\prime}}{\sqrt{\Delta t}}\,\sqrt{\frac{2\ln\phi\_{1,r}}{\phi\_{1,r}^{2}-1}}. |  |

## Appendix B Deferred Proofs

### B-A Proof of Proposition [1](https://arxiv.org/html/2512.12871v1#Thmproposition1 "Proposition 1 (Capacity Premium as a Strip of European Options). ‣ II Modeling Assumptions and Specifications ‣ CapOptix: An Options-Framework for Capacity Market Pricing")

###### Proof.

The capacity contract is a sequence (or strip) of European call options, each maturing at time t∈[T,T+τ]t\in[T,T+\tau], with the same strike price KtK\_{t}, reflecting the capped energy price the LSE pays during shortage periods.

Each such option yields a payoff of (St−Kt)+(S\_{t}-K\_{t})^{+}, exercised only when St>KtS\_{t}>K\_{t}. By the principle of risk-neutral valuation, the present value of a single option expiring at time tt is:

|  |  |  |
| --- | --- | --- |
|  | Ct=e−r​t​𝔼ℚ​[(St−K)+]C\_{t}=e^{-rt}\,\mathbb{E}^{\mathbb{Q}}\left[(S\_{t}-K)^{+}\right] |  |

Since delivery happens across multiple periods t∈[T,T+τ]t\in[T,T+\tau], the total capacity premium is the sum of all such option values, scaled by QQ, yielding:

|  |  |  |
| --- | --- | --- |
|  | C​(0,S0)=Q​∑t=TT+τCt​Δ​t=Q​∑t=TT+τe−r​t​𝔼ℚ​[(St−K)+]​Δ​tC(0,S\_{0})=Q\sum\_{t=T}^{T+\tau}C\_{t}\Delta t=Q\sum\_{t=T}^{T+\tau}e^{-rt}\,\mathbb{E}^{\mathbb{Q}}\left[(S\_{t}-K)^{+}\right]\Delta t |  |

∎

### B-B Proof of Proposition [2](https://arxiv.org/html/2512.12871v1#Thmproposition2 "Proposition 2. ‣ III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing")

###### Proof.

By Eq [2](https://arxiv.org/html/2512.12871v1#S3.E2 "In III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), Eq [3](https://arxiv.org/html/2512.12871v1#S3.E3 "In III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), and from Def [1](https://arxiv.org/html/2512.12871v1#Thmdefinition1 "Definition 1 (NetCONE). ‣ III Contract Duration for new Capacities ‣ CapOptix: An Options-Framework for Capacity Market Pricing") we have :
C=∫0T+τe−r​t​CONE ​𝑑t−R​1−R​2≈N​e​t​C​O​N​EC=\int\_{0}^{T+\tau}e^{-rt}\text{CONE }dt-R1-R2\approx NetCONE.
∎

### B-C Proof of Proposition [3](https://arxiv.org/html/2512.12871v1#Thmproposition3 "Proposition 3 (CVaR representation). ‣ IV-A Conditional Value-at-Risk (CVaR) ‣ IV Reliability Metrics and Strike Price ‣ CapOptix: An Options-Framework for Capacity Market Pricing")

###### Proof.

As α→0\alpha\to 0, q0​(Z)=0q\_{0}(Z)=0. Therefore, CVaR0​(Z)=𝔼​[Z∣Z≥0]=𝔼​[Z]=E​E​U\text{CVaR}\_{0}(Z)=\mathbb{E}[Z\mid Z\geq 0]=\mathbb{E}[Z]=EEU.

Now, for α→1\alpha\to 1, let M∗:=ess​sup⁡ZM^{\ast}:=\operatorname\*{ess\,sup}Z. To prove the upper bound, fix ε>0\varepsilon>0. By definition of M∗M^{\ast} we have ℙ​(Z>M∗+ε)=0\mathbb{P}(Z>M^{\ast}+\varepsilon)=0, so qu​(Z)≤M∗+εq\_{u}(Z)\leq M^{\ast}+\varepsilon ∀u∈(0,1)\forall u\in(0,1). Hence,

|  |  |  |
| --- | --- | --- |
|  | CVaRα​(Z)=11−α​∫α1qu​(Z)​𝑑u≤M∗+ε\mathrm{CVaR}\_{\alpha}(Z)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}q\_{u}(Z)\,du\leq M^{\ast}+\varepsilon |  |

∀α\forall\alpha, which yields lim supα↑1CVaRα​(Z)≤M∗\limsup\_{\alpha\uparrow 1}\mathrm{CVaR}\_{\alpha}(Z)\leq M^{\ast} as ε↓0\varepsilon\downarrow 0.

To prove the lower bound, fix ε>0\varepsilon>0. Since M∗M^{\ast} is the smallest almost-sure upper bound, M∗−εM^{\ast}-\varepsilon is not an upper bound and ℙ​(Z>M∗−ε)>0\mathbb{P}(Z>M^{\ast}-\varepsilon)>0, so u0:=FZ​(M∗−ε)<1u\_{0}:=F\_{Z}(M^{\ast}-\varepsilon)<1.
For any u>u0u>u\_{0} one must have qu​(Z)≥M∗−εq\_{u}(Z)\geq M^{\ast}-\varepsilon, and therefore, for all α>u0\alpha>u\_{0},

|  |  |  |
| --- | --- | --- |
|  | CVaRα​(Z)=11−α​∫α1qu​(Z)​𝑑u≥M∗−ε.\mathrm{CVaR}\_{\alpha}(Z)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}q\_{u}(Z)\,du\geq M^{\ast}-\varepsilon. |  |

Thus lim infα↑1CVaRα​(Z)≥M∗\liminf\_{\alpha\uparrow 1}\mathrm{CVaR}\_{\alpha}(Z)\geq M^{\ast} as ε↓0\varepsilon\downarrow 0.
∎

### B-D Proof of Proposition [4](https://arxiv.org/html/2512.12871v1#Thmproposition4 "Proposition 4 (Consumers favour RO over CA). ‣ V Reliability Options as Capacity Auctions ‣ CapOptix: An Options-Framework for Capacity Market Pricing")

###### Proof.

With C=MC=M,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ΠRO]\displaystyle\mathbb{E}\!\bigl[\Pi^{\mathrm{RO}}\bigr] | =M​Q+∫0τe−r​t​𝔼​[min⁡(St,K)​qt]​𝑑t,\displaystyle=MQ+\int\_{0}^{\tau}e^{-rt}\,\mathbb{E}\!\bigl[\min(S\_{t},K)\,q\_{t}\bigr]\,dt, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ΠCA]\displaystyle\mathbb{E}\!\bigl[\Pi^{\mathrm{CA}}\bigr] | =M​Q+∫0τe−r​t​𝔼​[St​qt]​𝑑t.\displaystyle=MQ+\int\_{0}^{\tau}e^{-rt}\,\mathbb{E}[S\_{t}q\_{t}]\,dt. |  |

Because min⁡(St,K)≤St\min(S\_{t},K)\leq S\_{t} pointwise and the inequality is strict with
positive probability when St>KS\_{t}>K, the integral part of the RO payoff is
strictly smaller, proving the result.
∎

### B-E Proof of Lemma [1](https://arxiv.org/html/2512.12871v1#Thmlemma1 "Lemma 1 (RO premium as price–tail CVaR). ‣ IV-B Reliability Options align with CVaR of Shortfall ‣ IV Reliability Metrics and Strike Price ‣ CapOptix: An Options-Framework for Capacity Market Pricing")

###### Proof.

Given StS\_{t}, with CDF FSt​(s)F\_{S\_{t}}(s) and PDF fSt​(s)f\_{S\_{t}}(s) :

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(St−Kt)+]\displaystyle\mathbb{E}[(S\_{t}-K\_{t})^{+}] | =∫(St−Kt)​𝑑ℙ​(St>Kt)\displaystyle=\int(S\_{t}-K\_{t})d\mathbb{P}(S\_{t}>K\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Kt∞(s−Kt)​fSt​(s)​𝑑s\displaystyle=\int\_{K\_{t}}^{\infty}(s-K\_{t})f\_{S\_{t}}(s)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Kt∞s​fSt​(s)​𝑑s−∫Kt∞K​fSt​(s)​𝑑s\displaystyle=\int\_{K\_{t}}^{\infty}sf\_{S\_{t}}(s)ds-\int\_{K\_{t}}^{\infty}Kf\_{S\_{t}}(s)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−α)​C​V​a​Rα​(St)−Kt​(1−FSt​(Kt))\displaystyle=(1-\alpha)CVaR\_{\alpha}(S\_{t})-K\_{t}(1-F\_{S\_{t}}(K\_{t})) |  |

The last line is by the definition of C​V​a​RCVaR, where qα​(St)=Ktq\_{\alpha}(S\_{t})=K\_{t}. Thus, by quantile definition, we have FSt​(Kt)=αF\_{S\_{t}}(K\_{t})=\alpha.
∎

### B-F Proof of Theorem [1](https://arxiv.org/html/2512.12871v1#Thmtheorem1 "Theorem 1 (Alignment of RO premium with CVaR of shortfall). ‣ IV-B Reliability Options align with CVaR of Shortfall ‣ IV Reliability Metrics and Strike Price ‣ CapOptix: An Options-Framework for Capacity Market Pricing")

###### Proof.

By the scarcity-pricing Assumption [3](https://arxiv.org/html/2512.12871v1#Thmassumption3 "Assumption 3 (Scarcity–pricing). ‣ II Modeling Assumptions and Specifications ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), we have
St=sbase,t+φ​(Zt+​(ℛ))S\_{t}=s\_{\text{base},t}+\varphi\bigl(Z\_{t}^{+}(\mathcal{R})\bigr).
On the relevant tail region, we assume a linear scarcity response with slope VOLL>0\mathrm{VOLL}>0, i.e., φ​(z)=φ​(0)+VOLL​z\varphi(z)=\varphi(0)+\mathrm{VOLL}\,z, so that

|  |  |  |
| --- | --- | --- |
|  | St=sbase,t+φ​(0)+VOLL​Zt+​(ℛ).S\_{t}=s\_{\text{base},t}+\varphi(0)+\mathrm{VOLL}\,Z\_{t}^{+}(\mathcal{R}). |  |

Since StS\_{t} is an affine, strictly increasing function of
Zt+​(ℛ)Z\_{t}^{+}(\mathcal{R}), quantiles and CVaR transform linearly. Writing
zα:=qα​(Zt+​(ℛ))z\_{\alpha}:=q\_{\alpha}(Z\_{t}^{+}(\mathcal{R})), we obtain

|  |  |  |
| --- | --- | --- |
|  | Kt=qα​(St)=sbase,t+φ​(0)+VOLL​zα,K\_{t}=q\_{\alpha}(S\_{t})=s\_{\text{base},t}+\varphi(0)+\mathrm{VOLL}\,z\_{\alpha}, |  |

|  |  |  |
| --- | --- | --- |
|  | CVaRα​(St)=sbase,t+φ​(0)+VOLL​CVaRα​(Zt+​(ℛ)).\mathrm{CVaR}\_{\alpha}(S\_{t})=s\_{\text{base},t}+\varphi(0)+\mathrm{VOLL}\,\mathrm{CVaR}\_{\alpha}\bigl(Z\_{t}^{+}(\mathcal{R})\bigr). |  |

Subtracting the two,

|  |  |  |
| --- | --- | --- |
|  | CVaRα​(St)−Kt=VOLL​(CVaRα​(Zt+​(ℛ))−zα).\mathrm{CVaR}\_{\alpha}(S\_{t})-K\_{t}=\mathrm{VOLL}\,\Bigl(\mathrm{CVaR}\_{\alpha}\bigl(Z\_{t}^{+}(\mathcal{R})\bigr)-z\_{\alpha}\Bigr). |  |

By Lemma [1](https://arxiv.org/html/2512.12871v1#Thmlemma1 "Lemma 1 (RO premium as price–tail CVaR). ‣ IV-B Reliability Options align with CVaR of Shortfall ‣ IV Reliability Metrics and Strike Price ‣ CapOptix: An Options-Framework for Capacity Market Pricing"), for this choice of KtK\_{t} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(St−Kt)+]\displaystyle\mathbb{E}\bigl[(S\_{t}-K\_{t})^{+}\bigr] | =(1−α)​(CVaRα​(St)−Kt)\displaystyle=(1-\alpha)\,\bigl(\mathrm{CVaR}\_{\alpha}(S\_{t})-K\_{t}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−α)​VOLL​(CVaRα​(Zt+​(ℛ))−zα).\displaystyle=(1-\alpha)\,\mathrm{VOLL}\,\Bigl(\mathrm{CVaR}\_{\alpha}\bigl(Z\_{t}^{+}(\mathcal{R})\bigr)-z\_{\alpha}\Bigr). |  |

Substituting this expression into the RO premium formula of Proposition [1](https://arxiv.org/html/2512.12871v1#Thmproposition1 "Proposition 1 (Capacity Premium as a Strip of European Options). ‣ II Modeling Assumptions and Specifications ‣ CapOptix: An Options-Framework for Capacity Market Pricing") yields the expression of Theorem [1](https://arxiv.org/html/2512.12871v1#Thmtheorem1 "Theorem 1 (Alignment of RO premium with CVaR of shortfall). ‣ IV-B Reliability Options align with CVaR of Shortfall ‣ IV Reliability Metrics and Strike Price ‣ CapOptix: An Options-Framework for Capacity Market Pricing").
∎

### B-G Proof of Lemma [2](https://arxiv.org/html/2512.12871v1#Thmlemma2 "Lemma 2 (OU Process is Gaussian and Stationary). ‣ A-A Mean-Reverting Ornstein-Uhlenbeck (OU) Process ‣ Appendix A Other Stochastic Models ‣ CapOptix: An Options-Framework for Capacity Market Pricing")

###### Proof.

Let integrating factor be eκ​te^{\kappa t}. Multiply both sides of the SDE by eκ​te^{\kappa t}, and apply product rule in stochastic calculus:

|  |  |  |
| --- | --- | --- |
|  | d​(eκ​t​St)=eκ​t​d​St+κ​eκ​t​St​d​t=eκ​t​κ​θ​d​t+eκ​t​σ​d​Wt.d(e^{\kappa t}S\_{t})=e^{\kappa t}dS\_{t}+\kappa e^{\kappa t}S\_{t}dt=e^{\kappa t}\kappa\theta\,dt+e^{\kappa t}\sigma\,dW\_{t}. |  |

Therefore, we integrate both sides from 0 to tt to get St=μt+σ​∫0te−κ​(t−s)​𝑑WsS\_{t}=\mu\_{t}+\sigma\int\_{0}^{t}e^{-\kappa(t-s)}dW\_{s}, where μt=S0​e−κ​t+θ​(1−e−κ​t)\mu\_{t}=S\_{0}e^{-\kappa t}+\theta(1-e^{-\kappa t}).

The stochastic integral ∫0te−κ​(t−s)​𝑑Ws\int\_{0}^{t}e^{-\kappa(t-s)}dW\_{s} is a normally distributed random variable with mean zero and variance:

|  |  |  |
| --- | --- | --- |
|  | Var​(∫0te−κ​(t−s)​𝑑Ws)=∫0te−2​κ​(t−s)​𝑑s=1−e−2​κ​t2​κ.\mathrm{Var}\left(\int\_{0}^{t}e^{-\kappa(t-s)}dW\_{s}\right)=\int\_{0}^{t}e^{-2\kappa(t-s)}ds=\frac{1-e^{-2\kappa t}}{2\kappa}. |  |

Therefore, the variance of StS\_{t} is: σt2=σ2⋅1−e−2​κ​t2​κ\sigma\_{t}^{2}=\sigma^{2}\cdot\frac{1-e^{-2\kappa t}}{2\kappa}.

Hence, we conclude St∼𝒩​(μt,σt2)S\_{t}\sim\mathcal{N}(\mu\_{t},\sigma\_{t}^{2}), where μt=S0​e−κ​t+θ​(1−e−κ​t)\mu\_{t}=S\_{0}e^{-\kappa t}+\theta(1-e^{-\kappa t}), and σt2=σ22​κ​(1−e−2​κ​t)\sigma\_{t}^{2}=\frac{\sigma^{2}}{2\kappa}(1-e^{-2\kappa t}).

As t→∞t\to\infty, St→𝒩​(θ,σ22​κ)S\_{t}\to\mathcal{N}(\theta,\frac{\sigma^{2}}{2\kappa}), so the process is asymptotically stationary with limiting mean θ\theta and variance σ22​κ\frac{\sigma^{2}}{2\kappa}.
∎