---
authors:
- Yining Ding
- Ruyi Liu
- Marek Rutkowski
doc_id: arxiv:2603.07863v1
family_id: arxiv:2603.07863
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Choice of Collateral Currency in Differential Swaps
url_abs: http://arxiv.org/abs/2603.07863v1
url_html: https://arxiv.org/html/2603.07863v1
venue: arXiv q-fin
version: 1
year: 2026
---


Yining Dinga\,{}^{a}, Ruyi Liub\,{}^{b} and Marek Rutkowskia,c\,{}^{a,c}
  
  
  
  
  
a{}^{a\,}School of Mathematics and Statistics, University of Sydney
  
Sydney, NSW 2006, Australia
  
  
b{}^{b\,}School of Mathematics and Statistics, University of New South Wales
  
Sydney, NSW 2033, Australia
  
  
c{}^{c\,}Faculty of Mathematics and Information Science, Warsaw University of Technology
  
00-661 Warszawa, Poland

###### Abstract

The role of collateral in derivative pricing has evolved beyond credit risk mitigation, particularly following the global financial crisis, when funding costs and basis spreads became central to valuation practices. This development coincided with the transition from the London Interbank Offered Rate (LIBOR) to risk-free rates (RFRs) and the increasing standardization of collateralised trading. We study the valuation and hedging of a class of differential swaps
referencing backward-looking averages of overnight rates,
with SOFR swaps appearing as a particular instance. The focus is on the impact of the collateral currency. Extending earlier results Ding et al. [Math. Finance 36 (2026), pp. 180–202], we allow the collateral account to be denominated in a currency different from that of the contractual cash flows and derive explicit pricing and hedging strategies using a futures-based replication approach.

We show that the choice of collateral currency can have a non-trivial effect on both valuation and risk management. In particular, foreign-currency collateral can introduce additional risk exposures even when contractual cash flows are entirely denominated in the domestic currency. Numerical study demonstrates that collateral effects can lead to significant valuation adjustments and therefore need to be properly incorporated in modern multi-currency modelling frameworks.

Keywords:
swap, SOFR, €STR, multi-currency CSA, SOFR futures, proportional collateralisation, risk management
  
MSC:
60H10, 60H30, 91G30, 91G40

## 1 Introduction

The global financial crisis of 2007–2009 and the subsequent move toward central clearing and strengthened margining practices contributed to the market-wide dominance of collateralised trading in over-the-counter (OTC) derivatives.
In parallel, international standards on margin requirements for non-centrally cleared derivatives emphasise the exchange of variation margin as a key tool for limiting counterparty exposure and systemic risk [[3](#bib.bib2 "Margin requirements for non-centrally cleared derivatives")].
Beyond its role in credit risk mitigation, collateralisation has economically meaningful pricing implications: theory and evidence indicate that collateral provisions can affect swap rates and, more broadly, the valuation of interest-rate derivatives [[23](#bib.bib3 "The impact of collateralization on swap rates")].
Consequently, fixed income markets adopted a post-crisis pricing architecture in which discounting is aligned with collateral remuneration (OIS/CSA discounting) and curve construction becomes explicitly multi-curve [[5](#bib.bib5 "Two curves, one price: pricing and hedging interest rate derivatives decoupling forwarding and discounting yield curves"), [20](#bib.bib4 "The irony in derivatives discounting part ii: the crisis"), [26](#bib.bib6 "Modern LIBOR market models: using different curves for projecting rates and for discounting")].

This paper studies a question that naturally arises in a collateralised multi-curve environment:
*how does the choice of collateral currency affect the valuation and hedging of USD-referencing derivatives?*
While it is common to view a USD interest-rate product as being collateralised in USD, in practice the collateral currency specified in a CSA may differ from the payoff currency.
For example, USD SOFR trades may be collateralised with EUR cash remunerated at the euro short-term rate, €STR [[25](#bib.bib11 "An overview of the valuation of collateralized derivative contracts")].
In such cases, the collateral remuneration rate is no longer aligned with the payoff currency curve, and the resulting effective discounting and funding economics become intrinsically cross-currency
[[17](#bib.bib12 "Derivative pricing under asymmetric and imperfect collateralization and CVA"), [25](#bib.bib11 "An overview of the valuation of collateralized derivative contracts")]. Moreover, when a collateral agreement admits a *set* of eligible collateral currencies with low-friction substitution, the posting party effectively holds an option to choose the cheapest collateral to deliver.
This observation has been emphasized in the collateral currency choice literature and leads naturally to a cheapest-to-deliver (CTD) interpretation of collateral eligibility [[16](#bib.bib35 "Choice of collateral currency"), [30](#bib.bib59 "Cheapest-to-deliver collateral: a common factor approach")].
Related valuation formulae for contingent claims involving currency dislocations between contractual and collateral cashflows can be found in
[[14](#bib.bib33 "A note on construction of multiple swap curves with and without collateral"), [15](#bib.bib34 "On the term structure of interest rates with basis spreads, collateral and multiple currencies"), [18](#bib.bib38 "Cross currency Heath-Jarrow-Morton framework in the multiple-curve setting"), [19](#bib.bib37 "Cross currency valuation and hedging in the multiple curve framework")], in contrast to our setup, these papers use the unsecured funding rate as the numeraire.

The market context is further shaped by benchmark reform and the transition away from IBORs [[12](#bib.bib13 "Reforming LIBOR and other financial market benchmarks")].
Within the resulting RFR-based market structure, exchange-traded futures linked to SOFR and €STR provide natural and standardized hedging instruments for short-rate risk.
Recent work on derivatives referencing backward-looking overnight rates develops pricing and hedging frameworks in which RFR futures play a central role as hedging instruments [[6](#bib.bib14 "Pricing and hedging of SOFR derivatives"), [11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")].
Because futures are exchange-traded instruments with daily settlement, classical forward–futures distinctions and convexity effects remain relevant when interpreting futures-implied rates and when constructing hedging strategies
[[10](#bib.bib16 "The relation between forward prices and futures prices"), [22](#bib.bib15 "Forward contracts and futures contracts")]. These features make futures-based replication particularly well-suited for modelling and hedging collateralised derivatives in modern RFR markets.

Multi-curve interest-rate modelling and OIS/CSA discounting are now standard ingredients of post-crisis fixed income markets.
Early contributions formalised the need to separate forwarding and discounting curves and derived no-arbitrage price relations under multi-curve term structures [[5](#bib.bib5 "Two curves, one price: pricing and hedging interest rate derivatives decoupling forwarding and discounting yield curves"), [20](#bib.bib4 "The irony in derivatives discounting part ii: the crisis"), [26](#bib.bib6 "Modern LIBOR market models: using different curves for projecting rates and for discounting")].
Recently, a generalized Heath–Jarrow–Morton framework was developed to model term structures driven by overnight rates with stochastic discontinuities, providing no-arbitrage conditions and affine semimartingale specifications with pricing and hedging results [[13](#bib.bib7 "Term structure modeling with overnight rates beyond stochastic continuity")]. Related valuation formulae for contingent claims involving currency dislocations between contractual and collateral cash flows can be found in [[14](#bib.bib33 "A note on construction of multiple swap curves with and without collateral"), [15](#bib.bib34 "On the term structure of interest rates with basis spreads, collateral and multiple currencies"), [18](#bib.bib38 "Cross currency Heath-Jarrow-Morton framework in the multiple-curve setting"), [19](#bib.bib37 "Cross currency valuation and hedging in the multiple curve framework")], but, in contrast to our setup, these papers use the unsecured funding rate as the numeraire.
More broadly, collateralised valuation connects discounting to the collateral remuneration rate under idealised assumptions, and a range of frameworks extend this logic to incorporate imperfect collateralisation, haircuts, asymmetries, and funding considerations [[9](#bib.bib17 "Counterparty credit risk, collateral and funding: with pricing cases for all asset classes"), [17](#bib.bib12 "Derivative pricing under asymmetric and imperfect collateralization and CVA"), [25](#bib.bib11 "An overview of the valuation of collateralized derivative contracts")].
At the same time, there is an active debate on the interpretation and accounting status of funding valuation adjustments, with contrasting views on whether dealer funding costs should enter fair value [[2](#bib.bib19 "Funding value adjustments"), [21](#bib.bib18 "Valuing derivatives: funding value adjustments and fair value")].

A recent study by the International Monetary Fund (IMF) highlights that cross-border transactions involving multiple currencies introduce additional foreign exchange risk, thus increasing cross-border transaction costs [[1](#bib.bib9 "A multi-currency exchange and contracting platform. International Monetary Fund, Working paper 22/217")]. In multi-currency settings, derivative values can depend on the collateral currency and, consequently, incorporate basis-like cross-currency quantities even for single-currency payoffs.
Collateralised valuation can be formulated in an arbitrage-free framework under an arbitrary numeraire, without requiring the existence of a risk-free short rate, thus clarifying the role of the pricing measure and the associated funding account [[24](#bib.bib8 "Pricing collateralized derivatives with an arbitrary numeraire")].
Our work connects these strands to the specific post-LIBOR reality of USD SOFR and EUR €STR markets.

A key message, sometimes overlooked in practice, is that *collateral currency choice can generate a genuinely non-trivial risk exposure even when contractual cash flows are entirely denominated in the domestic currency*.
For instance, consider a USD SOFR-referencing claim collateralised in EUR cash (remunerated at €STR).
In this case, the associated collateral account and the effective rate introduce an additional stochastic driver into the wealth dynamics, so that hedging solely with domestic SOFR instruments leaves a systematic residual exposure (and hence P&L leakage).
Within our futures-based replication framework, this additional *collateral-currency risk* remains *explicitly hedgeable*:
the required hedge ratios in SOFR and €STR futures are obtained in Proposition [5.2](#S5.Thmpro2 "Proposition 5.2. ‣ 5.2 Hedging under proportional foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), and their effectiveness and residual replication errors are quantified in the numerical experiments of Section [6.4](#S6.SS4 "6.4 Hedging of domestic and foreign sources of risk ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps").

The main object of the study is a class of USD-referencing *differential swaps* under backward-looking overnight rate conventions.
This class is specified at the level of a generic payoff functional, and several standard USD rates products are recovered for particular parameter choices.
In particular, the forward-starting SOFR swap is obtained as a special case and provides a concrete benchmark for our valuation and hedging results. We compare the valuation and hedging under USD cash collateral with the corresponding quantities under EUR cash collateral remunerated at
€STR, allowing for proportional (partial) collateralisation.

Within this setup, our main contributions are as follows.
First, we provide an explicit valuation framework for USD-referencing claims under proportional foreign collateralisation, by working under the pricing measure associated with the effective rate, which interpolates between the hedger’s funding rate and the collateral remuneration rate.
Second, we show that foreign-currency collateral generates a non-trivial risk exposure even when all contractual cash flows are domestic, and we characterise precisely how this risk enters both valuation and replication.
Third, we develop a tractable futures-based hedging methodology and derive explicit hedge ratios in SOFR and €STR futures.
Finally, we quantify the economic importance of collateral currency choice via numerical studies, including valuation shifts, a cheapest-to-deliver mechanism when multiple collateral currencies are eligible, and simulation-based assessments of hedge effectiveness.

The remainder of the paper is organised as follows.
Section [2](#S2 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps") introduces the condensed two-currency collateralised market, specifies proportional collateralisation, and formalises the admissible class of collateralised futures trading strategies together with the pricing martingale measure induced by the effective rate.
Section [3](#S3 "3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") presents the cross-currency term-structure specification, including the dynamics of the relevant traded futures under the pricing measure.
Section [4](#S4 "4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") derives arbitrage-free valuation results for USD-referencing differential swaps under collateral currency choice, covering both the fully foreign-collateralised benchmark and proportional foreign collateralisation, and then extends
the analysis to multi-period swaps.
Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") develops the corresponding replication and futures-based hedging framework using SOFR and €STR futures.
Section [6](#S6 "6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") provides numerical illustrations of valuation impacts and the CTD mechanism, and reports simulation-based hedging experiments.
In particular, we quantify the residual risk attributable *solely* to foreign-currency collateralisation: hedging with domestic futures alone leaves a systematic, economically non-trivial exposure of the order of 5%5\% in our baseline specifications.

## 2 Collateralised Trading Strategies and Pricing Measure

This section fixes notation and records a self-contained, model-free setup for collateralisation, funding, and futures-based self-financing trading in a two-currency market. We focus on the ingredients that will be used repeatedly in the valuation and replication results, namely the domestic/foreign overnight benchmarks (SOFR and €STR), the associated traded futures, proportional foreign collateralisation, and the induced effective rate rβr^{\beta} that governs the wealth dynamics.

The presentation is intentionally condensed. We first summarise the relevant market conventions and linked instruments, then formalise admissible collateralised futures strategies together with their self-financing condition, and finally introduce the pricing martingale measure associated with the effective rate rβr^{\beta}.

The setup of this section is model-free and does not rely on a specific term-structure specification. Pricing is formulated under the pricing martingale measure ℚ~\widetilde{\mathbb{Q}} induced by proportional collateralisation (see Definition [2.6](#S2.Thmdefi6 "Definition 2.6. ‣ 2.4 Pricing martingale measure ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps")). In Section [3](#S3 "3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") we subsequently specify a concrete cross-currency term-structure model under the domestic martingale measure ℚ\mathbb{Q} and verify that, within that specification, ℚ~\widetilde{\mathbb{Q}} coincides with ℚ\mathbb{Q}. For a more detailed discussion, we refer to our earlier papers [[6](#bib.bib14 "Pricing and hedging of SOFR derivatives"), [11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")].

### 2.1 Risk-free rates and related futures

By convention, the *domestic* currency is USD, the *foreign* currency is EUR, and the exchange rate at time tt is denoted by QtQ\_{t}. Although we use
USD and EUR for concreteness, the foreign currency and its associated overnight benchmark can be replaced by any other currency RFR pair.

Throughout this section, we fix an accrual period [U,T][U,T] with 0≤U<T0\leq U<T and set
δ:=T−U\delta:=T-U. For notational convenience, whenever no confusion arises, we suppress the dependence of futures quotes on [U,T][U,T]. The domestic overnight benchmark is
SOFR and the foreign overnight benchmark is €STR with respective
compound averages given by the following definition, which is based on a continuous time
proxy for the actual market conventions.

###### Definition 2.1.

Let the 𝔽\mathbb{F}-adapted processes rdr^{d} and rfr^{f} represent the instantaneous SOFR and
€STR rates, respectively. The continuously compounded *SOFR account* BdB^{d} satisfies

|  |  |  |
| --- | --- | --- |
|  | Btd=exp⁡(∫0trud​d​u),t≥0,B^{d}\_{t}=\exp\Big(\int\_{0}^{t}r^{d}\_{u}\,\mathop{}\!du\Big),\qquad t\geq 0, |  |

and the backward-looking *SOFR Average* over [U,T][U,T] is

|  |  |  |
| --- | --- | --- |
|  | Rd​(U,T):=1δ​(exp⁡(∫UTrud​d​u)−1)=1δ​(BTdBUd−1).R^{d}(U,T):=\frac{1}{\delta}\Big(\exp\Big(\int\_{U}^{T}r^{d}\_{u}\,\mathop{}\!du\Big)-1\Big)=\frac{1}{\delta}\Big(\frac{B^{d}\_{T}}{B^{d}\_{U}}-1\Big). |  |

Similarly, the continuously compounded *€STR account* BfB^{f} satisfies

|  |  |  |
| --- | --- | --- |
|  | Btf=exp⁡(∫0truf​d​u),t≥0,B^{f}\_{t}=\exp\Big(\int\_{0}^{t}r^{f}\_{u}\,\mathop{}\!du\Big),\qquad t\geq 0, |  |

and the backward-looking *€STR Average* over [U,T][U,T] is

|  |  |  |
| --- | --- | --- |
|  | Rf​(U,T):=1δ​(exp⁡(∫UTruf​d​u)−1)=1δ​(BTfBUf−1).R^{f}(U,T):=\frac{1}{\delta}\Big(\exp\Big(\int\_{U}^{T}r^{f}\_{u}\,\mathop{}\!du\Big)-1\Big)=\frac{1}{\delta}\Big(\frac{B^{f}\_{T}}{B^{f}\_{U}}-1\Big). |  |

Both Rd​(U,T)R^{d}(U,T) and Rf​(U,T)R^{f}(U,T) are backward-looking so, in particular, they are ℱT\mathcal{F}\_{T}-measurable but not
ℱt\mathcal{F}\_{t}-measurable for t<Tt<T. Futures written on these realised averages will be our primary hedging instruments.

###### Definition 2.2.

A *SOFR futures* contract for the accrual period [U,T][U,T] is a futures contract referencing the
SOFR Average Rd​(U,T)R^{d}(U,T), and its quoted futures rate is denoted by Ftd​(U,T)F^{d}\_{t}(U,T) for
t∈[0,T]t\in[0,T]. An analogous *€STR futures* contract is defined with the quoted futures rate Ftf​(U,T)F^{f}\_{t}(U,T).

The spot value of entering a futures contract is zero if we ignore initial/variation margin mechanics. The semimartingale dynamics of FdF^{d} and FfF^{f} will be specified later once we introduce an explicit
term-structure model in Section [3](#S3 "3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").

### 2.2 Differential swaps and collateral conventions

We work throughout in a two-economy setting and we allow the collateral currency to be specified independently of the payoff currency. This separation is the source of both the valuation impact and the additional hedgeable exposure studied later in the paper.

We start by specifying a generic shape of the payoff of the swap contract. To keep the framework flexible, we introduce a one-parameter family indexed by a real constant γ\gamma, which scales the foreign overnight-rate leg. Varying
γ\gamma allows the same notation to cover several distinct products within a unified pricing and hedging setup that enjoys the additivity property.

###### Definition 2.3.

A single-period SOFR/€STR swap over [U,T][U,T], settled in arrears at TT, is a contract settled in domestic currency with the following net payoff: at time TT, the long party receives the floating amount δ​Rd​(U,T)\delta R^{d}(U,T) based on the domestic overnight rate and pays the floating amount δ​γ​Rf​(U,T)\delta\gamma R^{f}(U,T) based on the foreign overnight rate together with a fixed margin δ​κ\delta\kappa.
Equivalently, the net cash flow at time TT for the long party is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃𝐒Tγ,κ​(U,T)=δ​(Rd​(U,T)−γ​Rf​(U,T)−κ)​P,{\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)=\delta\big(R^{d}(U,T)-\gamma R^{f}(U,T)-\kappa\big)P, |  | (2.1) |

where PP denotes the notional amount denominated in the domestic currency.

Let QtQ\_{t} denote the spot FX rate, quoted as units of domestic currency per one unit of foreign currency.
A distinctive feature of the differential-swap specification is that the contractual payoff is *domestic-currency settled* and does not involve QQ explicitly.
In contrast to a cross-currency basis swap, where FX conversion implies an explicit dependence on the exchange rate in the cashflow specification, see [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")].

###### Remark 2.1.

Definition [2.3](#S2.Thmdefi3 "Definition 2.3. ‣ 2.2 Differential swaps and collateral conventions ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps") and its multi-period extension is tailored to cover several instances of swap contracts that occur in market practice. When γ=0\gamma=0, the payoff given by ([2.1](#S2.E1 "In Definition 2.3. ‣ 2.2 Differential swaps and collateral conventions ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps")) reduces to a standard single-period SOFR swap: it is intrinsically domestic, although the associated CSA can specify either domestic or foreign collateralisation.
When γ≠0\gamma\neq 0, the contract becomes a *differential swap* driven by domestic and foreign overnight rates.
It is sometimes referred to as a *quanto swap* when the constant γ\gamma is interpreted as a predetermined conversion factor, for example, a fixed USD/EUR exchange rate.
For further background on differential swaps in a LIBOR setting, see Wei [[29](#bib.bib1 "Valuing differential swaps")].

Furthermore, to isolate the incremental impact of *collateral currency choice* (as opposed to payoff design), we set γ=0\gamma=0 in the numerical study of Section [6](#S6 "6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps").
When γ≠0\gamma\neq 0, the foreign rate rfr^{f} affects the valuation and hedging through two conceptually distinct channels: first, via the collateral remuneration convention and, second, through the foreign rate component of the contractual payoff. In that case, the appearance of foreign-rate hedging instruments is largely expected, since the payoff itself loads directly on the foreign curve. By contrast, when γ=0\gamma=0, the SOFR swap payoff is purely domestic and independent of rfr^{f}. Hence any non-trivial exposure to the foreign economy, and any need to use *foreign* futures for replication, is attributable *solely* to foreign-currency collateralisation. This choice therefore provides a clean control setting in which the magnitude of collateral-induced risk can be quantified in a transparent way.

We model the collateral process as the variation margin posted/received over the lifetime of the trade and remunerated at a rate
linked to the *collateral currency*. The proportionality parameter β\beta specifies the degree of collateralisation in a
reduced-form way: at any time, a fraction β\beta of the current mark-to-market swap value is treated as collateralised (hence accruing at
the collateral remuneration rate), while the remaining fraction 1−β1-\beta is treated as uncollateralised exposure, which is then funded at the
hedger’s funding rate. This convention captures, in stylized form, the effect of thresholds, haircuts, and partial posting: for example,
β=1\beta=1 corresponds to full collateralisation, whereas β=0\beta=0 corresponds to the uncollateralised benchmark. More general
CSAs (e.g., with several eligible collateral currencies, time-dependent posting rules, or switching/mixing conventions)
can be incorporated by allowing the time and state-dependent remuneration/funding mix. The proportional rule is adopted here because it leads to a transparent pricing measure and explicit replication formulae; the detailed mathematical derivations are given in Section [2.3](#S2.SS3 "2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps").

Under the Gaussian term structure specification introduced later in Section [3](#S3 "3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), the relevant conditional
expectations factorise into products of fictitious bond prices multiplied by deterministic “convexity correction” terms. We
compute these corrections explicitly in Section [4.1](#S4.SS1 "4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") and then exploit the corresponding factorization to derive the closed-form
hedge ratios. This is consistent with the broader convexity-adjustment methodology used in backward-looking rate products.

### 2.3 collateralised futures strategies

We consider trading in domestic SOFR futures and foreign €STR futures. Let FdF^{d}
and FfF^{f} be continuous semimartingales representing the respective futures *prices/rates*
(depending on the market quotation convention, this only affects affine transformations). We also introduce the hedge funding account BhB^{h} defined by

|  |  |  |
| --- | --- | --- |
|  | d​Bth=rth​Bth​d​t,B0h=1,\mathop{}\!dB^{h}\_{t}=r^{h}\_{t}\,B^{h}\_{t}\,\mathop{}\!dt,\qquad B^{h}\_{0}=1, |  |

where rhr^{h} is an 𝔽\mathbb{F}-adapted funding rate.

###### Definition 2.4.

A *futures trading strategy* is an ℝ3{\mathbb{R}}^{3}-valued, 𝔽\mathbb{F}-adapted process
φ=(φ0,φd,φf)\varphi=(\varphi^{0},\varphi^{d},\varphi^{f}), where φd\varphi^{d} and φf\varphi^{f} represent positions in SOFR futures and
€STR futures, respectively, and φ0\varphi^{0} is the cash (funding) position. Since the
marked-to-market value of a futures position is zero, the value of the strategy equals

|  |  |  |
| --- | --- | --- |
|  | Vtp​(φ)=φt0​Bth,t∈[0,T].V\_{t}^{p}(\varphi)=\varphi^{0}\_{t}\,B^{h}\_{t},\qquad t\in[0,T]. |  |

Let CC denote the collateral balance *expressed in USD* (the domestic currency). We use the sign
convention that Ct>0C\_{t}>0 corresponds to the collateral *received* by the hedger and Ct<0C\_{t}<0 corresponds to the
collateral *posted* by the hedger. We adopt the daily settlement market convention and assume
that the hedger either pays or receives the accrued interest on the collateral balance, depending on
the sign of CC. Specifically, let Ct′C^{\prime}\_{t} be the collateral balance expressed in units of the *collateral currency*
and let QtQ\_{t} be the FX rate converting one unit of the collateral currency into USD (the domestic price to one unit of foreign currency). The USD value of collateral is then given by

|  |  |  |
| --- | --- | --- |
|  | Ct:=Ct′​Qt.C\_{t}:=C^{\prime}\_{t}\,Q\_{t}. |  |

In particular, if collateral is posted in USD then Qt≡1Q\_{t}\equiv 1.
The collateral remuneration rate is denoted by rcr^{c}.
More precisely, when collateral is posted in the domestic currency (USD) we write

|  |  |  |
| --- | --- | --- |
|  | rc=rd+αc,d,r^{c}=r^{d}+\alpha^{c,d}, |  |

where αc,d\alpha^{c,d} denotes the spread between the domestic collateral remuneration rate and the domestic overnight rate.
Similarly, when collateral is posted in the foreign currency (EUR) we write

|  |  |  |
| --- | --- | --- |
|  | rc=rf+αc,f,r^{c}=r^{f}+\alpha^{c,f}, |  |

where αc,f\alpha^{c,f} denotes the spread. Here, αc,d\alpha^{c,d} and αc,f\alpha^{c,f} are deterministic functions, integrable on [0,T][0,T] for every T>0T>0. In Sections 4–5 we focus on foreign collateralisation and the symbol rcr^{c} invariably denotes there the foreign collateral remuneration rate.

Under the daily settlement assumption, a key feature is that a foreign futures position (settled in EUR) has to
be represented in USD. Daily settlement (together with Itô’s product rule) generates an additional
quadratic covariation term between the FX rate QQ and the foreign futures process FfF^{f}. For a detailed discussion, please refer to [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")]. This motivates
the USD-valued foreign-futures gains process Ff,qF^{f,q} defined below.

###### Definition 2.5.

A collateralised futures strategy (φ,C)=(φ0,φd,φf,C)(\varphi,C)=(\varphi^{0},\varphi^{d},\varphi^{f},C) is *self-financing* if its
value process Vtp​(φ,C):=φt0​BthV\_{t}^{p}(\varphi,C):=\varphi\_{t}^{0}B^{h}\_{t} satisfies, for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtp​(φ,C)\displaystyle V\_{t}^{p}(\varphi,C) | =V0p​(φ,C)+∫0tφu0​d​Buh+Ct−∫0truc​Cu​d​u+∫0tφud​d​Fud+∫0tφuf​d​Fuf,q,\displaystyle=V\_{0}^{p}(\varphi,C)+\int\_{0}^{t}\varphi^{0}\_{u}\,\mathop{}\!dB^{h}\_{u}+C\_{t}-\int\_{0}^{t}r^{c}\_{u}\,C\_{u}\,\mathop{}\!du+\int\_{0}^{t}\varphi^{d}\_{u}\,\mathop{}\!dF^{d}\_{u}+\int\_{0}^{t}\varphi^{f}\_{u}\,\mathop{}\!dF^{f,q}\_{u}, |  |

or, equivalently,

|  |  |  |
| --- | --- | --- |
|  | d​Vtp​(φ,C)=rth​Vtp​(φ,C)​d​t+d​Ct−rtc​Ct​d​t+φtd​d​Ftd+φtf​d​Ftf,q,\mathop{}\!dV\_{t}^{p}(\varphi,C)=r^{h}\_{t}V\_{t}^{p}(\varphi,C)\,\mathop{}\!dt+\mathop{}\!dC\_{t}-r^{c}\_{t}C\_{t}\,\mathop{}\!dt+\varphi^{d}\_{t}\,\mathop{}\!dF^{d}\_{t}+\varphi^{f}\_{t}\,\mathop{}\!dF^{f,q}\_{t}, |  |

where we define the auxiliary process Ff,qF^{f,q} to represent gains from position in foreign futures (e.g.,
€STR futures) expressed in the domestic currency via

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ftf,q:=F0f,q+∫0tQu​d​Fuf+⟨Q,Ff⟩t,F^{f,q}\_{t}:=F^{f,q}\_{0}+\int\_{0}^{t}Q\_{u}\,\mathop{}\!dF^{f}\_{u}+\langle{Q,F^{f}}\rangle\_{t}, |  | (2.2) |

where ⟨Q,Ff⟩t\langle{Q,F^{f}}\rangle\_{t} denotes the quadratic covariation process.

We define the hedger’s *wealth process* as V​(φ,C):=Vp​(φ,C)−CV(\varphi,C):=V^{p}(\varphi,C)-C. A direct computation shows that

|  |  |  |
| --- | --- | --- |
|  | d​Vt​(φ,C)=rth​Vt​(φ,C)​d​t−(rtc−rth)​Ct​d​t+φtd​d​Ftd+φtf​d​Ftf,q.\mathop{}\!dV\_{t}(\varphi,C)=r^{h}\_{t}V\_{t}(\varphi,C)\,\mathop{}\!dt-(r^{c}\_{t}-r^{h}\_{t})C\_{t}\,\mathop{}\!dt+\varphi^{d}\_{t}\,\mathop{}\!dF^{d}\_{t}+\varphi^{f}\_{t}\,\mathop{}\!dF^{f,q}\_{t}. |  |

In particular, if rc=rhr^{c}=r^{h}, then collateralisation has no effect on wealth dynamics.

Next, we impose proportional collateralisation Ct=−βt​Vt​(φ,C)C\_{t}=-\beta\_{t}V\_{t}(\varphi,C), where β\beta is a non-negative, 𝔽\mathbb{F}-adapted process (typically, β∈[0,1]\beta\in[0,1] in applications). Then V​(φ,C)V(\varphi,C) satisfies

|  |  |  |
| --- | --- | --- |
|  | Vt​(φ,C)=V0​(φ,C)+∫0truβ​Vu​(φ,C)​d​u+∫0tφud​d​Fud+∫0tφuf​d​Fuf,q,V\_{t}(\varphi,C)=V\_{0}(\varphi,C)+\int\_{0}^{t}r^{\beta}\_{u}\,V\_{u}(\varphi,C)\,\mathop{}\!du+\int\_{0}^{t}\varphi^{d}\_{u}\,\mathop{}\!dF^{d}\_{u}+\int\_{0}^{t}\varphi^{f}\_{u}\,\mathop{}\!dF^{f,q}\_{u}, |  |

where the *effective funding rate* rβr^{\beta} equals

|  |  |  |
| --- | --- | --- |
|  | rβ:=(1−β)​rh+β​rc.r^{\beta}:=(1-\beta)r^{h}+\beta\,r^{c}. |  |

Let BβB^{\beta} be the fictitious account with d​Btβ=rtβ​Btβ​d​t\mathop{}\!dB^{\beta}\_{t}=r^{\beta}\_{t}B^{\beta}\_{t}\,\mathop{}\!dt
and, by convention, B0β=1B^{\beta}\_{0}=1.

###### Proposition 2.1.

Let (φ,C)(\varphi,C) be a self-financing collateralised futures strategy with C=−β​V​(φ,C)C=-\beta V(\varphi,C).
Then the discounted wealth V~β​(φ,C):=(Bβ)−1​V​(φ,C)\widetilde{V}^{\beta}(\varphi,C):=(B^{\beta})^{-1}V(\varphi,C) satisfies

|  |  |  |
| --- | --- | --- |
|  | V~tβ​(φ,C)=V~0β​(φ,C)+G~tβ​(φ,C),\widetilde{V}\_{t}^{\beta}(\varphi,C)=\widetilde{V}\_{0}^{\beta}(\varphi,C)+\widetilde{G}\_{t}^{\beta}(\varphi,C), |  |

where the discounted gains process is

|  |  |  |
| --- | --- | --- |
|  | G~tβ​(φ,C)=∫0t(Buβ)−1​φud​d​Fud+∫0t(Buβ)−1​φuf​d​Fuf,q.\widetilde{G}\_{t}^{\beta}(\varphi,C)=\int\_{0}^{t}(B^{\beta}\_{u})^{-1}\varphi^{d}\_{u}\,\mathop{}\!dF^{d}\_{u}+\int\_{0}^{t}(B^{\beta}\_{u})^{-1}\varphi^{f}\_{u}\,\mathop{}\!dF^{f,q}\_{u}. |  |

Under proportional collateralisation the collateral account does not need to be modelled explicitly. The impact of collateral enters the wealth dynamics only through the drift term governed by
rβr^{\beta}, while all stochastic risk exposures are carried by the traded futures components FdF^{d} and
FfF^{f}. Imposing Ct=−βt​Vt​(φ,C)C\_{t}=-\beta\_{t}V\_{t}(\varphi,C) therefore converts the collateral carry into a
position-dependent drift adjustment: a fraction βt\beta\_{t} of the position is effectively funded at the
collateral remuneration rate rtcr^{c}\_{t}, while the remaining fraction is funded at rthr^{h}\_{t}. This yields
the effective funding rate rtβ=(1−βt)​rth+βt​rtcr^{\beta}\_{t}=(1-\beta\_{t})r^{h}\_{t}+\beta\_{t}r^{c}\_{t} that appears in the drift of V​(φ,C)V(\varphi,C)
and motivates the fictitious numeraire BβB^{\beta}. When rh=rcr^{h}=r^{c} collateralisation is immaterial,
when β≡0\beta\equiv 0 funding is entirely at rhr^{h}, and when β≡1\beta\equiv 1 the drift is governed
by rcr^{c}, reflecting the full collateral funding under the adopted convention. Although our assumptions on funding and collateral could be formulated in a more general way, as in [[8](#bib.bib22 "Valuation and hedging of contracts with funding costs and collateralization")] and related treatments in [[4](#bib.bib20 "A unified approach to xVA with CSA discounting and initial margin"), [7](#bib.bib21 "Arbitrage-free pricing of derivatives in nonlinear market models")],
here we intentionally adopt a relatively simple specification, which allows us to derive closed-form
solutions for both arbitrage-free pricing and hedging strategies for differential swaps.

### 2.4 Pricing martingale measure

The following definition of a *pricing martingale measure* was introduced in [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")].

###### Definition 2.6.

A probability measure ℚ~\widetilde{\mathbb{Q}} is called a *pricing martingale measure (PMM)*
for the date UU if ℚ~\widetilde{\mathbb{Q}} is equivalent to the statistical measure ℙ{\mathbb{P}} on (Ω,ℱT)(\Omega,\mathcal{F}\_{T}) and,
for any self-financing collateralised futures strategy (φ,C)(\varphi,C) with arbitrary proportional
collateralisation level β\beta, the process (V~tβ​(φ,C))t∈[0,U](\widetilde{V}^{\beta}\_{t}(\varphi,C))\_{t\in[0,U]} is a
ℚ~\widetilde{\mathbb{Q}}-local martingale.

As customary, admissible strategies are restricted to those for which V~β\widetilde{V}^{\beta} is bounded from below
(to rule out doubling strategies). It should be noted that, in view of Proposition [2.1](#S2.Thmpro1 "Proposition 2.1. ‣ 2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"), the probability measure ℚ~\widetilde{\mathbb{Q}} introduced in Definition [2.6](#S2.Thmdefi6 "Definition 2.6. ‣ 2.4 Pricing martingale measure ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps") does not depend on a choice of the process β\beta. To establish the existence of a PMM it suffices (and is essentially necessary) to specify an arbitrage-free
joint model for the drivers of (Fd,Ff,q)(F^{d},F^{f,q}) under some candidate pricing measure and then verify the local martingale property (see Proposition [3.1](#S3.Thmpro1 "Proposition 3.1. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps")).

###### Definition 2.7.

A collateralised contract (XT,β)(X\_{T},\beta) with terminal payoff XTX\_{T} is *attainable* if there exists an admissible self-financing collateralised futures strategy (φ,C)(\varphi,C) with C=−β​VC=-\beta V such that VT​(φ,C)=XTV\_{T}(\varphi,C)=X\_{T}.

###### Proposition 2.2.

Assume that (BTβ)−1​XT(B^{\beta}\_{T})^{-1}X\_{T} is ℚ~\widetilde{\mathbb{Q}}-integrable and (XT,β)(X\_{T},\beta) is attainable. Then the arbitrage-free price process satisfies, for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | πtβ​(XT)=Btβ​𝔼ℚ~​[(BTβ)−1​XT|ℱt].\pi\_{t}^{\beta}(X\_{T})=B^{\beta}\_{t}\,\mathbb{E}\_{\widetilde{\mathbb{Q}}}\!\left[(B^{\beta}\_{T})^{-1}X\_{T}\,\big|\,\mathcal{F}\_{t}\right]. |  | (2.3) |

For brevity, we will sometimes write Xtβ:=πtβ​(XT)X^{\beta}\_{t}:=\pi^{\beta}\_{t}(X\_{T}), so that XTβ=XTX^{\beta}\_{T}=X\_{T}. In addition, we will use the following notation for the collateralisation level of reference when β=1\beta=1

|  |  |  |
| --- | --- | --- |
|  | πtc​(XT):=πtβ​(XT)\pi\_{t}^{c}(X\_{T}):=\pi\_{t}^{\beta}(X\_{T}) |  |

and we write correspondingly Xtc:=πtc​(XT)X^{c}\_{t}:=\pi\_{t}^{c}(X\_{T}).
Note that β≡1\beta\equiv 1 yields rβ≡rcr^{\beta}\equiv r^{c} and Bβ≡BcB^{\beta}\equiv B^{c}.

## 3 Cross-Currency Term Structure Model

This section introduces a tractable cross-currency term structure specification used to obtain explicit futures dynamics, hedge ratios, and numerical illustrations in later sections. Building on the model-free collateralised trading framework and the pricing martingale measure introduced in Section [2](#S2 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"), we now impose a concrete Gaussian specification for the joint dynamics of the domestic and foreign overnight rates and the FX rate.

Section [3.1](#S3.SS1 "3.1 Cross-currency model specification ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") records a standing assumption that fixes the Vasicek–Garman–Kohlhagen dynamics of (rd,rf,Q)(r^{d},r^{f},Q) under the domestic martingale measure ℚ\mathbb{Q} and the corresponding dynamics under the foreign martingale measure ℚ^\widehat{\mathbb{Q}}. Section [3.2](#S3.SS2 "3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") introduces auxiliary conditional discount factors under ℚ\mathbb{Q} and ℚ^\widehat{\mathbb{Q}} and summarises their diffusion coefficients, which serve as convenient inputs for futures dynamics and hedging ratios. Section [3.3](#S3.SS3 "3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") states the diffusion structure of the traded SOFR and €STR futures and verifies that, within this specification, the pricing martingale measure ℚ~\widetilde{\mathbb{Q}} induced by proportional collateralisation coincides with ℚ\mathbb{Q}. Finally, Section [3.4](#S3.SS4 "3.4 Restricted completeness ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") establishes a restricted completeness property for the class of claims considered in this work.

### 3.1 Cross-currency model specification

In a multi-curve cross-currency setting, the same economic model can be presented through several equivalent choices of numeraires and pricing measures. To avoid an extended discussion of measure construction, we record below a single standing assumption that fixes (i) the joint dynamics of the domestic and foreign short rates and the FX rate under a domestic pricing measure ℚ\mathbb{Q}, and (ii) the associated foreign martingale measure ℚ^\widehat{\mathbb{Q}} obtained by an explicit Girsanov transform. All subsequent pricing and hedging arguments rely only on this specification. For background and derivations in the classical cross-currency setting, we refer to [[27](#bib.bib47 "Martingale methods in financial modelling"), Chapter 14] and [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")].

We interpret r¯d\bar{r}^{d} (resp. r¯f\bar{r}^{f}) as the money-market rate that prevails in the domestic (resp. foreign)
fixed-income market, so that the corresponding money-market accounts satisfy

|  |  |  |
| --- | --- | --- |
|  | d​B¯td=r¯td​B¯td​d​t,d​B¯tf=r¯tf​B¯tf​d​t.\mathop{}\!d\bar{B}^{d}\_{t}=\bar{r}^{d}\_{t}\,\bar{B}^{d}\_{t}\,\mathop{}\!dt,\qquad\mathop{}\!d\bar{B}^{f}\_{t}=\bar{r}^{f}\_{t}\,\bar{B}^{f}\_{t}\,\mathop{}\!dt. |  |

We write

|  |  |  |
| --- | --- | --- |
|  | r¯td:=rtd+αtd,r¯tf:=rtf+αtf,λtq:=αtd−αtf,\bar{r}^{d}\_{t}:=r^{d}\_{t}+\alpha^{d}\_{t},\qquad\bar{r}^{f}\_{t}:=r^{f}\_{t}+\alpha^{f}\_{t},\qquad\lambda^{q}\_{t}:=\alpha^{d}\_{t}-\alpha^{f}\_{t}, |  |

where αd,αf\alpha^{d},\alpha^{f} are deterministic spreads (integrable on [0,T][0,T] for every T>0T>0). In particular,
r¯td−r¯tf=rtd−rtf+λtq\bar{r}^{d}\_{t}-\bar{r}^{f}\_{t}=r^{d}\_{t}-r^{f}\_{t}+\lambda^{q}\_{t}.
The deterministic spreads αd\alpha^{d} and αf\alpha^{f} allow for a multi-curve adjustment between the overnight benchmarks (rd,rf)(r^{d},r^{f}) and the money-market rates (r¯d,r¯f)(\bar{r}^{d},\bar{r}^{f}).

We assume that under ℚ\mathbb{Q} the processes Z1,Z2,Z3Z^{1},Z^{2},Z^{3} are one-dimensional Brownian motions with
instantaneous covariations

|  |  |  |
| --- | --- | --- |
|  | d⟨Zi,Zj⟩t=ρi​jdt.i,j∈{1,2,3}.\mathop{}\!d\langle{Z^{i},Z^{j}}\rangle\_{t}=\rho\_{ij}\,\mathop{}\!dt.\qquad i,j\in\{1,2,3\}. |  |

###### Assumption 3.1.

Under the domestic pricing measure ℚ\mathbb{Q}, the domestic and foreign overnight rates rd,rfr^{d},r^{f} follow Vasicek dynamics and the FX rate QQ (the domestic price to one unit of foreign currency) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​rtd\displaystyle\mathop{}\!dr^{d}\_{t} | =(a−b​rtd)​d​t+σ​d​Zt1,\displaystyle=(a-br^{d}\_{t})\mathop{}\!dt+\sigma\mathop{}\!dZ^{1}\_{t}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​rtf\displaystyle\mathop{}\!dr^{f}\_{t} | =(c^−b^​rtf)​d​t+σ^​d​Zt2,\displaystyle=(\widehat{c}-\widehat{b}\,r^{f}\_{t})\mathop{}\!dt+\widehat{\sigma}\mathop{}\!dZ^{2}\_{t}, |  | (3.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Qt\displaystyle\mathop{}\!dQ\_{t} | =Qt​(rtd−rtf+λtq)​d​t+Qt​σ¯​d​Zt3,\displaystyle=Q\_{t}(r^{d}\_{t}-r^{f}\_{t}+\lambda^{q}\_{t})\mathop{}\!dt+Q\_{t}\bar{\sigma}\mathop{}\!dZ^{3}\_{t}, |  |

where a,b,σ,c^,b^,σ^,σ¯a,b,\sigma,\widehat{c},\widehat{b},\widehat{\sigma},\bar{\sigma} are positive constants and the processes Z1,Z2Z^{1},Z^{2} and Z3Z^{3} are one-dimensional Brownian motions under ℚ\mathbb{Q} with the correlations ⟨Zi,Zj⟩t=ρi​j​d​t\langle{Z^{i},Z^{j}}\rangle\_{t}=\rho\_{ij}\mathop{}\!dt. Fix T>0T>0 and define the foreign martingale measure ℚ^\widehat{\mathbb{Q}} on (Ω,ℱT)(\Omega,\mathcal{F}\_{T}) by the density

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚ^d​ℚ|ℱT:=ℰTq,ℰtq:=exp⁡(σ¯​Zt3−12​σ¯2​t),t∈[0,T].\frac{d\widehat{\mathbb{Q}}}{d\mathbb{Q}}\Big|\_{\mathcal{F}\_{T}}:=\mathcal{E}^{q}\_{T},\qquad\mathcal{E}^{q}\_{t}:=\exp\!\Big(\bar{\sigma}\,Z^{3}\_{t}-\frac{1}{2}\bar{\sigma}^{2}t\Big),\quad t\in[0,T]. |  | (3.2) |

Then Z^t1=Zt1−σ¯​ρ13​t\widehat{Z}^{1}\_{t}=Z^{1}\_{t}-\bar{\sigma}\rho\_{13}\,t, Z^t2=Zt2−σ¯​ρ23​t\widehat{Z}^{2}\_{t}=Z^{2}\_{t}-\bar{\sigma}\rho\_{23}\,t and
Z^t3=Zt3−σ¯​t\widehat{Z}^{3}\_{t}=Z^{3}\_{t}-\bar{\sigma}\,t are correlated Brownian motions under ℚ^\widehat{\mathbb{Q}}.
Upon setting Rt:=Qt−1R\_{t}:=Q\_{t}^{-1} and a^:=c^+σ^​σ¯​ρ23\widehat{a}:=\widehat{c}+\widehat{\sigma}\,\bar{\sigma}\,\rho\_{23}, the dynamics under ℚ^\widehat{\mathbb{Q}} are

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​rtd\displaystyle\mathop{}\!dr^{d}\_{t} | =(a+σ​σ¯​ρ13−b​rtd)​d​t+σ​d​Z^t1,\displaystyle=\big(a+\sigma\bar{\sigma}\rho\_{13}-br^{d}\_{t}\big)\mathop{}\!dt+\sigma\,\mathop{}\!d\widehat{Z}^{1}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​rtf\displaystyle\mathop{}\!dr^{f}\_{t} | =(a^−b^​rtf)​d​t+σ^​d​Z^t2,\displaystyle=(\widehat{a}-\widehat{b}\,r^{f}\_{t})\mathop{}\!dt+\widehat{\sigma}\,\mathop{}\!d\widehat{Z}^{2}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Rt\displaystyle\mathop{}\!dR\_{t} | =Rt​(rtf−rtd−λtq)​d​t−Rt​σ¯​d​Z^t3.\displaystyle=R\_{t}(r^{f}\_{t}-r^{d}\_{t}-\lambda^{q}\_{t})\mathop{}\!dt-R\_{t}\bar{\sigma}\,\mathop{}\!d\widehat{Z}^{3}\_{t}. |  |

### 3.2 Dynamics of auxiliary discount factors

We introduce auxiliary conditional discount factors associated with the Vasicek specifications of the domestic and foreign overnight rates. These processes are *not* postulated as additional traded securities. Rather, they provide a convenient way to isolate the diffusion terms that ultimately drive the dynamics of traded futures and, consequently, the hedge ratios derived in Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"). Within the present Gaussian term-structure setting, the same quantities can be generated by dynamically traded futures portfolios, so they can be used as computational devices without enlarging the traded asset universe. We now recall standard affine computations for the Vasicek model [[28](#bib.bib58 "An equilibrium characterization of the term structure")].

We begin with the domestic auxiliary factor. For u>0u>0 and t≥0t\geq 0 we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bd​(t,u):=𝔼ℚ​[exp⁡(−∫turvd​d​v)|ℱt].B^{d}(t,u):={{\mathbb{E}}}\_{\mathbb{Q}}\!\left[\exp\!\Big(-\int\_{t}^{u}r^{d}\_{v}\,\mathop{}\!dv\Big)\,\Big|\,\mathcal{F}\_{t}\right]. |  | (3.3) |

For t≥ut\geq u, the conditional expectation reduces to the accrual factor realised, that is,
Bd​(t,u)=exp⁡(∫utrvd​d​v)=(Bud)−1​BtdB^{d}(t,u)=\exp(\int\_{u}^{t}r^{d}\_{v}\,\mathop{}\!dv)=(B^{d}\_{u})^{-1}B^{d}\_{t}, where d​Btd=rtd​Btd​d​t\mathop{}\!dB^{d}\_{t}=r^{d}\_{t}B^{d}\_{t}\,\mathop{}\!dt and
B0d=1B^{d}\_{0}=1. For t≤ut\leq u, the standard arguments for the affine term structure model yield the semimartingale dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Bd​(t,u)=Bd​(t,u)​(rtd​d​t−σ​n​(t,u)​d​Zt1),t∈[0,u],\mathop{}\!dB^{d}(t,u)=B^{d}(t,u)\Big(r^{d}\_{t}\,\mathop{}\!dt\,-\sigma n(t,u)\mathop{}\!dZ^{1}\_{t}\Big),\qquad t\in[0,u], |  | (3.4) |

where n​(t,u):=(1−e−b​(u−t))/bn(t,u):=(1-e^{-b(u-t)})/b.

We define the foreign auxiliary factor analogously, but under the foreign martingale measure ℚ^\widehat{\mathbb{Q}}.
For u>0u>0 and t≥0t\geq 0 we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bf​(t,u):=𝔼ℚ^​[exp⁡(−∫turvf​d​v)|ℱt].B^{f}(t,u):={{\mathbb{E}}}\_{\widehat{\mathbb{Q}}}\!\left[\exp\!\Big(-\int\_{t}^{u}r^{f}\_{v}\,\mathop{}\!dv\Big)\,\Big|\,\mathcal{F}\_{t}\right]. |  | (3.5) |

For t≤ut\leq u, under ℚ^\widehat{\mathbb{Q}} we have the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Bf​(t,u)=Bf​(t,u)​(rtf​d​t−σ^​n^​(t,u)​d​Z^t2),t∈[0,u],\mathop{}\!dB^{f}(t,u)=B^{f}(t,u)\Big(r^{f}\_{t}\,\mathop{}\!dt-\widehat{\sigma}\widehat{n}(t,u)\,\mathop{}\!d\widehat{Z}^{2}\_{t}\Big),\qquad t\in[0,u], |  | (3.6) |

where n^​(t,u):=(1−e−b^​(u−t))/b^\widehat{n}(t,u):=(1-e^{-\widehat{b}(u-t)})/\widehat{b}.

The following remark summarises the diffusion coefficients we will use later. We also record a simple
invariance principle that will be applied repeatedly: while drift terms change under equivalent measure
transformations, the continuous local martingale parts, and hence the diffusion coefficients relevant
for hedging remain unchanged. Specifically, for two continuous semimartingales Y1Y^{1} and Y2Y^{2} we write Y1≃Y2Y^{1}\simeq Y^{2} whenever Y1Y^{1} and Y2Y^{2} have the same continuous local martingale part in their canonical decompositions. If Y1≃Y2Y^{1}\simeq Y^{2} holds under ℚ\mathbb{Q} on (Ω,ℱT)(\Omega,\mathcal{F}\_{T}), then it also holds under any probability measure equivalent to ℚ\mathbb{Q} on (Ω,ℱT)(\Omega,\mathcal{F}\_{T}) and thus also under ℚ^\widehat{\mathbb{Q}}.

###### Remark 3.1.

For any fixed maturity T>0T>0, the process (Bd​(t,T),t≤T)(B^{d}(t,T),\,t\leq T) satisfies

|  |  |  |
| --- | --- | --- |
|  | d​Bd​(t,T)≃Bd​(t,T)​σT​(t)​d​Zt1,σT​(t):=−σ​n​(t,T).\mathop{}\!dB^{d}(t,T)\simeq B^{d}(t,T)\,\sigma\_{T}(t)\,\mathop{}\!dZ^{1}\_{t},\qquad\sigma\_{T}(t):=-\sigma\,n(t,T). |  |

Similarly, for any fixed maturity T>0T>0, the process (Bf​(t,T),t≤T)(B^{f}(t,T),\,t\leq T) satisfies under ℚ^\widehat{\mathbb{Q}}

|  |  |  |
| --- | --- | --- |
|  | d​Bf​(t,T)≃Bf​(t,T)​σ^T​(t)​d​Z^t2,σ^T​(t):=−σ^​n^​(t,T),\mathop{}\!dB^{f}(t,T)\simeq B^{f}(t,T)\,\widehat{\sigma}\_{T}(t)\,\mathop{}\!d\widehat{Z}^{2}\_{t},\qquad\widehat{\sigma}\_{T}(t):=-\widehat{\sigma}\,\widehat{n}(t,T), |  |

and therefore d​Bf​(t,T)≃Bf​(t,T)​σ^T​(t)​d​Zt2\mathop{}\!dB^{f}(t,T)\simeq B^{f}(t,T)\,\widehat{\sigma}\_{T}(t)\,\mathop{}\!dZ^{2}\_{t} under ℚ\mathbb{Q}.

In Sections [3.3](#S3.SS3 "3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") and [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") we will express the diffusion terms of the traded
SOFR and €STR futures, and the corresponding hedge ratios, directly in terms of
σT​(t)\sigma\_{T}(t) and σ^T​(t)\widehat{\sigma}\_{T}(t).

### 3.3 Futures dynamics and the pricing martingale measure

We now summarise the diffusion structure of the traded interest-rate futures that will be used for hedging.
Since explicit Vasicek-based representations are standard, we omit the derivations and refer to
[[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")] for concise proofs and further details. Our emphasis here is on the semimartingale
decompositions and, in particular, on the diffusion coefficients that enter the hedge ratios.

Recall from Definition [2.1](#S2.Thmdefi1 "Definition 2.1. ‣ 2.1 Risk-free rates and related futures ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps") that the backward-looking averages
Rd​(U,T)R^{d}(U,T) (SOFR) and Rf​(U,T)R^{f}(U,T) (€STR) are ℱT\mathcal{F}\_{T}-measurable. The corresponding
futures rates are defined as conditional expectations under the natural pricing measures: SOFR futures
are quoted/settled in the domestic currency and are therefore specified under ℚ\mathbb{Q}, while €STR futures are quoted and settled in the foreign currency and are specified under ℚ^\widehat{\mathbb{Q}}.

###### Definition 3.1.

The *SOFR futures rate* Ftd​(U,T)F^{d}\_{t}(U,T) and the *€STR futures rate* Ftf​(U,T)F^{f}\_{t}(U,T) are defined by

|  |  |  |
| --- | --- | --- |
|  | Ftd​(U,T):=𝔼ℚ​(Rd​(U,T)|ℱt),Ftf​(U,T):=𝔼ℚ^​(Rf​(U,T)|ℱt),t∈[0,T].F^{d}\_{t}(U,T):={{\mathbb{E}}}\_{\mathbb{Q}}\big(R^{d}(U,T)\,\big|\,\mathcal{F}\_{t}\big),\qquad F^{f}\_{t}(U,T):={{\mathbb{E}}}\_{\widehat{\mathbb{Q}}}\big(R^{f}(U,T)\,\big|\,\mathcal{F}\_{t}\big),\qquad t\in[0,T]. |  |

The next remark records the resulting diffusion coefficients. These coefficients will be reused later,
so we state them explicitly and adopt the shorthand notation introduced in
Section [3.2](#S3.SS2 "3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").

###### Remark 3.2.

Let Fd=Fd​(U,T)F^{d}=F^{d}(U,T) and Ff=Ff​(U,T)F^{f}=F^{f}(U,T) be the SOFR and €STR futures rates, respectively.
From [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates"), Proposition 4.3], d​Ftd=νtd​d​Zt1\mathop{}\!dF^{d}\_{t}=\nu^{d}\_{t}\,\mathop{}\!dZ^{1}\_{t}, where

|  |  |  |
| --- | --- | --- |
|  | νtd=δ−1​(1+δ​Ftd​(U,T))​(σU​(t)−σT​(t))=−δ−1​(1+δ​Ftd​(U,T))​σU,T​(t),t∈[0,U],\nu^{d}\_{t}=\delta^{-1}\big(1+\delta F^{d}\_{t}(U,T)\big)(\sigma\_{U}(t)-\sigma\_{T}(t))=-\delta^{-1}\big(1+\delta F^{d}\_{t}(U,T)\big)\sigma\_{U,T}(t),\qquad t\in[0,U], |  |

and

|  |  |  |
| --- | --- | --- |
|  | νtd=−δ−1​(1+δ​Ftd​(U,T))​σT​(t),t∈[U,T].\nu^{d}\_{t}=-\delta^{-1}\big(1+\delta F^{d}\_{t}(U,T)\big)\sigma\_{T}(t),\qquad t\in[U,T]. |  |

From [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates"), Proposition 4.4], d​Ftf=νtf​d​Z^t2\mathop{}\!dF^{f}\_{t}=\nu^{f}\_{t}\,\mathop{}\!d\widehat{Z}^{2}\_{t}, and hence
d​Ftf≃νtf​d​Zt2\mathop{}\!dF^{f}\_{t}\simeq\nu^{f}\_{t}\,\mathop{}\!dZ^{2}\_{t}, where

|  |  |  |
| --- | --- | --- |
|  | νtf=δ−1​(1+δ​Ftf​(U,T))​(σ^U​(t)−σ^T​(t))=−δ−1​(1+δ​Ftf​(U,T))​σ^U,T​(t),t∈[0,U],\nu^{f}\_{t}=\delta^{-1}\big(1+\delta F^{f}\_{t}(U,T)\big)(\widehat{\sigma}\_{U}(t)-\widehat{\sigma}\_{T}(t))=-\delta^{-1}\big(1+\delta F^{f}\_{t}(U,T)\big)\widehat{\sigma}\_{U,T}(t),\qquad t\in[0,U], |  |

and

|  |  |  |
| --- | --- | --- |
|  | νtf=−δ−1​(1+δ​Ftf​(U,T))​σ^T​(t),t∈[U,T].\nu^{f}\_{t}=-\delta^{-1}\big(1+\delta F^{f}\_{t}(U,T)\big)\widehat{\sigma}\_{T}(t),\qquad t\in[U,T]. |  |

Here δ:=T−U\delta:=T-U, and we use the shorthand σU,T​(t):=σT​(t)−σU​(t)\sigma\_{U,T}(t):=\sigma\_{T}(t)-\sigma\_{U}(t) and σ^U,T​(t):=σ^T​(t)−σ^U​(t)\widehat{\sigma}\_{U,T}(t):=\widehat{\sigma}\_{T}(t)-\widehat{\sigma}\_{U}(t).

Next, we reconcile these dynamics with the model-free pricing framework of Section [2](#S2 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps").
Although collateralised valuation and hedging are most conveniently formulated under the pricing
martingale measure (PMM) ℚ~\widetilde{\mathbb{Q}} introduced in Definition [2.6](#S2.Thmdefi6 "Definition 2.6. ‣ 2.4 Pricing martingale measure ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"), the term-structure model above
was specified under ℚ\mathbb{Q}. The following proposition shows that, within the present setting, these two
measures coincide. The key step is to express the foreign futures gains in domestic currency and to
identify its diffusion term under ℚ\mathbb{Q}.

###### Proposition 3.1.

The pricing martingale measure ℚ~\widetilde{\mathbb{Q}} exists and coincides with the domestic martingale measure ℚ\mathbb{Q}.

###### Proof.

Recall from ([2.2](#S2.E2 "In Definition 2.5. ‣ 2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps")) that the domestic-currency value of the foreign futures position satisfies

|  |  |  |
| --- | --- | --- |
|  | Ftf,q=F0f,q+∫0tQu​d​Fuf+⟨Q,Ff⟩t.F^{f,q}\_{t}=F^{f,q}\_{0}+\int\_{0}^{t}Q\_{u}\,\mathop{}\!dF^{f}\_{u}+\langle{Q,F^{f}}\rangle\_{t}. |  |

Using Remark [3.2](#S3.Thmrem2 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") and Z^2=Z2−σ¯​ρ23​t\widehat{Z}^{2}=Z^{2}-\bar{\sigma}\rho\_{23}\,t, we obtain

|  |  |  |
| --- | --- | --- |
|  | d​Ftf,q=Qt​νtf​(d​Z^t2+σ¯​ρ23​d​t)=Qt​νtf​d​Zt2.\mathop{}\!dF^{f,q}\_{t}=Q\_{t}\nu^{f}\_{t}\big(\mathop{}\!d\widehat{Z}^{2}\_{t}+\bar{\sigma}\rho\_{23}\,\mathop{}\!dt\big)=Q\_{t}\nu^{f}\_{t}\,\mathop{}\!dZ^{2}\_{t}. |  |

Hence Ff,qF^{f,q} is a (local) martingale under ℚ\mathbb{Q}. Since FdF^{d} is also a ℚ\mathbb{Q}-martingale by definition, ℚ\mathbb{Q}
is a pricing martingale measure for the traded futures family considered in this paper.
∎

The next remark records the resulting diffusion coefficient for the domestic-currency foreign-futures
process, which will be used repeatedly when expressing hedge ratios in Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps").

###### Remark 3.3.

In particular, d​Ftf,q=νtf,q​d​Zt2\mathop{}\!dF^{f,q}\_{t}=\nu^{f,q}\_{t}\,\mathop{}\!dZ^{2}\_{t} where νtf,q:=Qt​νtf\nu^{f,q}\_{t}:=Q\_{t}\nu^{f}\_{t} and νtf\nu^{f}\_{t} is given in
Remark [3.2](#S3.Thmrem2 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").

### 3.4 Restricted completeness

The three-factor specification we introduced in Assumption [3.1](#S3.Thmhyp1 "Assumption 3.1. ‣ 3.1 Cross-currency model specification ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") implies that the market is incomplete for general ℱT\mathcal{F}\_{T}-measurable claims when trading strategies are restricted to (Fd,Ff)(F^{d},F^{f}). Nevertheless, the products considered in this paper share a structural feature: their discounted price processes do not load on the third Brownian component. Consequently, they are hedgeable using (Fd,Ff,q)(F^{d},F^{f,q}) and thus (Fd,Ff)(F^{d},F^{f}) only. Let 𝔽(2):=(ℱtZ1,Z2)t∈[0,T]{\mathbb{F}}^{(2)}:=(\mathcal{F}\_{t}^{Z^{1},Z^{2}})\_{t\in[0,T]} be the subfiltration generated by (Z1,Z2)(Z^{1},Z^{2}). Here, ℱtZ1,Z2:=σ(Zu1,Zu2: 0≤u≤t)∨𝒩\mathcal{F}\_{t}^{Z^{1},Z^{2}}:=\sigma\!\big(Z^{1}\_{u},Z^{2}\_{u}:\,0\leq u\leq t\big)\vee\mathcal{N} denotes the usual augmentation, where 𝒩\mathcal{N} denotes the collection of ℙ{\mathbb{P}}-null sets in ℱ\mathcal{F}.
Hence (Z1,Z2)(Z^{1},Z^{2}) enjoys the predictable representation property with respect to 𝔽(2){\mathbb{F}}^{(2)}.

###### Proposition 3.2.

Consider a collateralised contract (XT,β)(X\_{T},\beta) with terminal payoff XTX\_{T} at time TT and
proportional collateralisation at rate β\beta. Assume that XT​(BTβ)−1X\_{T}(B^{\beta}\_{T})^{-1} is
ℚ\mathbb{Q}-integrable and that the discounted price process
π~tβ​(XT):=(Btβ)−1​πtβ​(XT)\widetilde{\pi}^{\beta}\_{t}(X\_{T}):=(B^{\beta}\_{t})^{-1}\pi^{\beta}\_{t}(X\_{T}) is 𝔽(2){\mathbb{F}}^{(2)}-adapted.
Then (XT,β)(X\_{T},\beta) can be replicated by a unique admissible self-financing collateralised futures strategy. The corresponding futures positions (φd,φf)(\varphi^{d},\varphi^{f}) are given by

|  |  |  |
| --- | --- | --- |
|  | φd=(νd)−1​ψ1,φf=(νf,q)−1​ψ2,\varphi^{d}=(\nu^{d})^{-1}\psi^{1},\qquad\varphi^{f}=(\nu^{f,q})^{-1}\psi^{2}, |  |

where (ψ1,ψ2)(\psi^{1},\psi^{2}) is the unique 𝔽(2){\mathbb{F}}^{(2)}-predictable process such that

|  |  |  |
| --- | --- | --- |
|  | d​π~tβ​(XT)=(Btβ)−1​(ψt1​d​Zt1+ψt2​d​Zt2).\mathop{}\!d\widetilde{\pi}^{\beta}\_{t}(X\_{T})=\big(B^{\beta}\_{t}\big)^{-1}\big(\psi^{1}\_{t}\,\mathop{}\!dZ^{1}\_{t}+\psi^{2}\_{t}\,\mathop{}\!dZ^{2}\_{t}\big). |  |

###### Proof.

Since π~β​(XT)\widetilde{\pi}^{\beta}(X\_{T}) is a ℚ\mathbb{Q}-martingale and is 𝔽(2){\mathbb{F}}^{(2)}-adapted, the predictable
representation property of (Z1,Z2)(Z^{1},Z^{2}) with respect to 𝔽(2){\mathbb{F}}^{(2)} yields the stated representation.
We have d​Fd=νd​d​Z1\mathop{}\!dF^{d}=\nu^{d}\,\mathop{}\!dZ^{1} and d​Ff,q=νf,q​d​Z2\mathop{}\!dF^{f,q}=\nu^{f,q}\,\mathop{}\!dZ^{2} by Remarks [3.2](#S3.Thmrem2 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") and [3.3](#S3.Thmrem3 "Remark 3.3. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), respectively. Matching diffusion coefficients gives the hedging positions and their uniqueness
follows from the uniqueness of the martingale representation.
∎

###### Remark 3.4.

Proposition [3.2](#S3.Thmpro2 "Proposition 3.2. ‣ 3.4 Restricted completeness ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") is a restricted completeness result for the class of contingent claims whose discounted price processes are 𝔽(2){\mathbb{F}}^{(2)}-adapted or, equivalently, whose martingale representations have zero loading on Z3Z^{3}.
This is precisely the situation encountered in Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") for the collateralised USD-referencing products considered in this paper.

## 4 Arbitrage-Free Pricing under Collateral Currency Choice

This section derives arbitrage-free pricing results for USD-referencing cash flows under collateral currency choice, with particular emphasis on foreign (EUR) cash collateral remunerated at €STR. We work within the model-free collateralised futures framework of Section [2](#S2 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"). According to the Gaussian cross-currency term-structure specification of Section [3](#S3 "3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), the pricing martingale measure ℚ~\widetilde{\mathbb{Q}} exists and coincides with the domestic martingale measure ℚ\mathbb{Q} (see Proposition [3.1](#S3.Thmpro1 "Proposition 3.1. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps")) and thus all pricing representations below are written under ℚ\mathbb{Q}.

We proceed in three steps. First, Section [4.1](#S4.SS1 "4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") records a compact library of convexity-correction identities for conditional expectations of exponentials of integrated short rates, which will be used repeatedly in closed-form computations. Next, Section [4.2](#S4.SS2 "4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") treats the fully foreign collateralised benchmark and we denote the associated pricing operator by πc\pi^{c}. We provide two algebraically equivalent pricing representations: one mirrors the general proportional collateralisation case and is therefore convenient for comparison, while the other is tailored to the subsequent hedging analysis in Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"). Finally, Section [4.3](#S4.SS3 "4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") derives the corresponding pricing results under proportional foreign collateralisation for a general constant β∈[0,1]\beta\in[0,1], and Section [4.4](#S4.SS4 "4.4 Extension to multi-period differential swaps ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") extends the analysis to multi-period swaps and their par rates.

### 4.1 Convexity corrections

Throughout this subsection, we work under the pricing measure ℚ\mathbb{Q} and assume that all volatility loadings appearing in the affine–Gaussian specification are deterministic. The closed-form formulae in Sections [4.2](#S4.SS2 "4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")–[4.3](#S4.SS3 "4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") rely on the fact that conditional expectations of exponentials of *integrated* short rates admit a systematic factorisation into products of (i) powers of fictitious bond prices and (ii) deterministic multiplicative corrections.

Assume a Gaussian specification with deterministic volatility loads for the integrated short rates
∫tTrud​d​u\int\_{t}^{T}r^{d}\_{u}\,\mathop{}\!du and ∫tTruf​d​u\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du, and constant correlations between the relevant Brownian motions.
For any maturity T≥tT\geq t, we have the following notation

|  |  |  |
| --- | --- | --- |
|  | BT​(t,rtd):=Bd​(t,T)=𝔼ℚ​[e−∫tTrud​d​u|ℱt],B^T​(t,rtf):=Bf​(t,T)=𝔼ℚ^​[e−∫tTruf​d​u|ℱt],B\_{T}(t,r^{d}\_{t}):=B^{d}(t,T)={{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}r^{d}\_{u}\,\mathop{}\!du}\,\Big|\,\mathcal{F}\_{t}\right],\qquad\widehat{B}\_{T}(t,r^{f}\_{t}):=B^{f}(t,T)={{\mathbb{E}}}\_{\widehat{\mathbb{Q}}}\!\left[e^{-\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du}\,\Big|\,\mathcal{F}\_{t}\right], |  |

denote the domestic (resp. foreign) fictitious zero-coupon bond prices under the domestic (resp. foreign) pricing measure.
Lemma [4.1](#S4.Thmlem1 "Lemma 4.1. ‣ 4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") is stated without a proof since it is a consequence of Lemma 5.1 in [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")]
and thus the reader is referred to Section 5.1 in [[11](#bib.bib30 "Multi-curve approach to cross-currency basis swaps referencing backward-looking rates")] for a fully general statement.
It shows that any conditional expectation built from integrated short-rate terms of the form

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[exp⁡(a​∫tUrud​d​u+b​∫tTrud​d​u+c​∫tUruf​d​u+d​∫tTruf​d​u)|ℱt],t≤U≤T,a,b,c,d∈ℝ,{{\mathbb{E}}}\_{\mathbb{Q}}\!\left[\exp\!\Big(a\!\int\_{t}^{U}r^{d}\_{u}\,\mathop{}\!du+b\!\int\_{t}^{T}r^{d}\_{u}\,\mathop{}\!du+c\!\int\_{t}^{U}r^{f}\_{u}\,\mathop{}\!du+d\!\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du\Big)\,\Big|\,\mathcal{F}\_{t}\right],\qquad t\leq U\leq T,\quad a,b,c,d\in\mathbb{R}, |  |

admits a factorisation into powers of the fictitious bond prices
BU​(t,rtd)B\_{U}(t,r^{d}\_{t}), BT​(t,rtd)B\_{T}(t,r^{d}\_{t}) and B^U​(t,rtf)\widehat{B}\_{U}(t,r^{f}\_{t}), B^T​(t,rtf)\widehat{B}\_{T}(t,r^{f}\_{t}),
multiplied by a deterministic correction factor (a product of the Γ\Gamma–terms).
Moreover, each correction factor equals 11 whenever its effective coefficient is zero. Consequently, many terms
are automatically dropped when β=0\beta=0 or β=1\beta=1.
The classification of adjustments according to their origin is given in the following lemma.

###### Lemma 4.1.

(i) The *self-adjustment* Γs\Gamma^{s} appears in the following equalities,
which hold for every t∈[0,T]t\in[0,T] and α∈ℝ\alpha\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[exp⁡(−α​∫tTrud​d​u)|ℱt]\displaystyle{{\mathbb{E}}}\_{\mathbb{Q}}\Big[\exp\!\Big(-\alpha\int\_{t}^{T}r^{d}\_{u}\,\mathop{}\!du\Big)\,\Big|\,\mathcal{F}\_{t}\Big] | =[BT​(t,rtd)]α​Γts​(T,α,σT),\displaystyle=[B\_{T}(t,r^{d}\_{t})]^{\alpha}\,\Gamma^{s}\_{t}(T,\alpha,\sigma\_{T}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ^​[exp⁡(−α​∫tTruf​d​u)|ℱt]\displaystyle{{\mathbb{E}}}\_{\widehat{\mathbb{Q}}}\Big[\exp\!\Big(-\alpha\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du\Big)\,\Big|\,\mathcal{F}\_{t}\Big] | =[B^T​(t,rtf)]α​Γts​(T,α,σ^T),\displaystyle=[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\alpha}\,\Gamma^{s}\_{t}(T,\alpha,\widehat{\sigma}\_{T}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Γts​(T,α,σT):=exp⁡(12​∫tTα​(α−1)​σT2​(u)​d​u)\Gamma^{s}\_{t}(T,\alpha,\sigma\_{T}):=\exp\bigg(\frac{1}{2}\int\_{t}^{T}\alpha(\alpha-1)\,\sigma^{2}\_{T}(u)\,\mathop{}\!du\bigg) |  |

and

|  |  |  |
| --- | --- | --- |
|  | Γts​(T,α,σ^T):=exp⁡(12​∫tTα​(α−1)​σ^T2​(u)​d​u).\Gamma^{s}\_{t}(T,\alpha,\widehat{\sigma}\_{T}):=\exp\bigg(\frac{1}{2}\int\_{t}^{T}\alpha(\alpha-1)\,\widehat{\sigma}^{2}\_{T}(u)\,\mathop{}\!du\bigg). |  |

In particular, Γts​(T,1,⋅)=1\Gamma^{s}\_{t}(T,1,\cdot)=1 for every t∈[0,T]t\in[0,T].

(ii) The *maturity-adjustment* Γm\Gamma^{m} occurs when two integrals are driven by the same Brownian motion
but have different ranges. Specifically, for t<U<Tt<U<T and α,β∈ℝ\alpha,\beta\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[exp⁡(−α​∫tUrud​d​u−β​∫tTrud​d​u)|ℱt]\displaystyle{{\mathbb{E}}}\_{\mathbb{Q}}\Big[\exp\!\Big(-\alpha\int\_{t}^{U}r^{d}\_{u}\,\mathop{}\!du-\beta\int\_{t}^{T}r^{d}\_{u}\,\mathop{}\!du\Big)\,\Big|\,\mathcal{F}\_{t}\Big] | =[BU​(t,rtd)]α​[BT​(t,rtd)]β\displaystyle=[B\_{U}(t,r^{d}\_{t})]^{\alpha}[B\_{T}(t,r^{d}\_{t})]^{\beta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×Γts​(U,α,σU)​Γts​(T,β,σT)​Γtm​(U,α​σU,β​σT),\displaystyle\quad\times\Gamma^{s}\_{t}(U,\alpha,\sigma\_{U})\,\Gamma^{s}\_{t}(T,\beta,\sigma\_{T})\,\Gamma^{m}\_{t}(U,\alpha\sigma\_{U},\beta\sigma\_{T}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Γtm​(U,α​σU,β​σT):=exp⁡(∫tUα​β​σU​(u)​σT​(u)​d​u).\Gamma^{m}\_{t}(U,\alpha\sigma\_{U},\beta\sigma\_{T}):=\exp\bigg(\int\_{t}^{U}\alpha\beta\,\sigma\_{U}(u)\sigma\_{T}(u)\,\mathop{}\!du\bigg). |  |

If the relevant terms involve rfr^{f} then the same rule applies with a suitable change in notation.

(iii) The *correlation-adjustment* Γc\Gamma^{c} is present when two integrals have the same range but
are driven by different Brownian motions with a deterministic correlation ρ12\rho\_{12}. We have, for every t∈[0,T]t\in[0,T]
α,β∈ℝ\alpha,\beta\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[exp⁡(−α​∫tTrud​d​u−β​∫tTruf​d​u)|ℱt]\displaystyle{{\mathbb{E}}}\_{\mathbb{Q}}\Big[\exp\!\Big(-\alpha\int\_{t}^{T}r^{d}\_{u}\,\mathop{}\!du-\beta\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du\Big)\,\Big|\,\mathcal{F}\_{t}\Big] | =[BT​(t,rtd)]α​[B^T​(t,rtf)]β\displaystyle=[B\_{T}(t,r^{d}\_{t})]^{\alpha}[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\beta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×Γts​(T,α,σT)​Γts​(T,β,σ^T)​Γtc​(T,α​σT,β​σ^T,ρ12),\displaystyle\quad\times\Gamma^{s}\_{t}(T,\alpha,\sigma\_{T})\,\Gamma^{s}\_{t}(T,\beta,\widehat{\sigma}\_{T})\,\Gamma^{c}\_{t}(T,\alpha\sigma\_{T},\beta\widehat{\sigma}\_{T},\rho\_{12}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Γtc​(T,α​σT,β​σ^T,ρ12):=exp⁡(∫tTα​β​σT​(u)​σ^T​(u)​ρ12​d​u).\Gamma^{c}\_{t}(T,\alpha\sigma\_{T},\beta\widehat{\sigma}\_{T},\rho\_{12}):=\exp\bigg(\int\_{t}^{T}\alpha\beta\sigma\_{T}(u)\widehat{\sigma}\_{T}(u)\,\rho\_{12}\,\mathop{}\!du\bigg). |  |

(iv) The *drift-adjustment* Γ^d\widehat{\Gamma}^{d} arises when the conditional expectation includes an equivalent
change of a probability measure. Then the correction takes the form, for all t∈[0,T]t\in[0,T] and α∈ℝ\alpha\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[exp⁡(−α​∫tTruf​d​u)|ℱt]\displaystyle{{\mathbb{E}}}\_{\mathbb{Q}}\Big[\exp\!\Big(-\alpha\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du\Big)\,\Big|\,\mathcal{F}\_{t}\Big] | =𝔼ℚ^​[exp⁡(−α​∫tTruf​d​u)|ℱt]​Γ^td​(T,σ¯,α​σ^T,ρ23)\displaystyle={{\mathbb{E}}}\_{\widehat{\mathbb{Q}}}\Big[\exp\!\Big(-\alpha\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du\Big)\,\Big|\,\mathcal{F}\_{t}\Big]\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\alpha\widehat{\sigma}\_{T},\rho\_{23}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[B^T​(t,rtf)]α​Γts​(T,α,σ^T)​Γ^td​(T,σ¯,α​σ^T,ρ23),\displaystyle=[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\alpha}\,\Gamma^{s}\_{t}(T,\alpha,\widehat{\sigma}\_{T})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\alpha\widehat{\sigma}\_{T},\rho\_{23}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Γ^td​(T,σ¯,α​σ^T,ρ23):=exp⁡(∫tTσ¯​α​σ^T​(u)​ρ23​d​u).\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\alpha\widehat{\sigma}\_{T},\rho\_{23}):=\exp\bigg(\int\_{t}^{T}\bar{\sigma}\alpha\widehat{\sigma}\_{T}(u)\rho\_{23}\,\mathop{}\!du\bigg). |  |

### 4.2 Pricing of swaps with full foreign collateralisation

We assume throughout that the domestic currency is USD and the domestic overnight rate is SOFR, denoted by rdr^{d}.
The foreign currency is EUR and the foreign overnight rate is €STR, denoted by rfr^{f}.
In this part, we consider a single-period swap of Definition [2.3](#S2.Thmdefi3 "Definition 2.3. ‣ 2.2 Differential swaps and collateral conventions ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps") referencing the accrual period [U,T][U,T] and settled in arrears at TT.
Without loss of generality, we set P=1P=1 in the subsequent pricing formulae, the price for a general notional
is obtained by multiplying by the actual notional amount PP.

We first study the fully foreign-collateralised benchmark with EUR cash collateral remunerated at the foreign collateral rate rc=rf+αc,fr^{c}=r^{f}+\alpha^{c,f}. We denote

|  |  |  |
| --- | --- | --- |
|  | At,Tc,f:=exp⁡(−∫tTαuc,f​𝑑u),A^{c,f}\_{t,T}:=\exp\Big(-\int\_{t}^{T}\alpha^{c,f}\_{u}\,du\Big), |  |

which means that the effective hedge/discount rate is equal to rcr^{c}. Notice that all convexity corrections appearing in Proposition
[4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") are deterministic functions and therefore they will not generate additional hedging terms.
Using the equalities δ​Rd​(U,T)=e∫UTrud​𝑑u−1\delta R^{d}(U,T)=e^{\int\_{U}^{T}r^{d}\_{u}\,du}-1 and δ​Rf​(U,T)=e∫UTruf​𝑑u−1\delta R^{f}(U,T)=e^{\int\_{U}^{T}r^{f}\_{u}\,du}-1, we obtain a convenient decomposition of the cash flow given by ([2.1](#S2.E1 "In Definition 2.3. ‣ 2.2 Differential swaps and collateral conventions ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps")) with P=1P=1

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃𝐒Tγ,κ(U,T)=e∫UTrud​d​u−γe∫UTruf​d​u−(1−γ+δκ)=:IT(1)−γIT(2)−(1−γ+δκ)IT(3).{\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)=e^{\int\_{U}^{T}r^{d}\_{u}\,\mathop{}\!du}-\gamma e^{\int\_{U}^{T}r^{f}\_{u}\,\mathop{}\!du}-(1-\gamma+\delta\kappa)=:I^{(1)}\_{T}-\gamma I^{(2)}\_{T}-(1-\gamma+\delta\kappa)I^{(3)}\_{T}. |  | (4.1) |

###### Proposition 4.1.

The arbitrage-free price of the single-period SOFR/€STR swap with full foreign collateralisation satisfies, for every t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tc,γ,κ​(U,T):=πtc​(𝐃𝐒Tγ,κ​(U,T))=It(1)−γ​It(2)−(1−γ+δ​κ)​It(3).{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T):=\pi^{c}\_{t}\big({\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)\big)=I^{(1)}\_{t}-\gamma I^{(2)}\_{t}-(1-\gamma+\delta\kappa)\,I^{(3)}\_{t}. |  |

(i) The domestic floating component I(1)I^{(1)} is equal to, for every t∈[0,U]t\in[0,U],

|  |  |  |
| --- | --- | --- |
|  | It(1)=At,Tc,f​BU​(t,rtd)​[BT​(t,rtd)]−1​B^T​(t,rtf)​Γt(1)​(U,T),I^{(1)}\_{t}=A^{c,f}\_{t,T}\,B\_{U}(t,r^{d}\_{t})\,[B\_{T}(t,r^{d}\_{t})]^{-1}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)}\_{t}(U,T), |  |

and, for every t∈[U,T]t\in[U,T],

|  |  |  |
| --- | --- | --- |
|  | It(1)=At,Tc,f​(BUd)−1​Btd​[BT​(t,rtd)]−1​B^T​(t,rtf)​Γt(1)​(U,T),I^{(1)}\_{t}=A^{c,f}\_{t,T}\,(B^{d}\_{U})^{-1}B^{d}\_{t}\,[B\_{T}(t,r^{d}\_{t})]^{-1}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)}\_{t}(U,T), |  |

where the convexity correction Γt(1)​(U,T)\Gamma^{(1)}\_{t}(U,T) is given by, for every t∈[0,U]t\in[0,U],

|  |  |  |
| --- | --- | --- |
|  | Γt(1)​(U,T)=Γts​(T,−1,σT)​Γtm​(U,σU,−σT)​Γtc​(U,σU,σ^T,ρ12)​Γtc​(T,−σT,σ^T,ρ12)​Γ^td​(T,σ¯,σ^T,ρ23),\Gamma^{(1)}\_{t}(U,T)=\Gamma^{s}\_{t}(T,-1,\sigma\_{T})\,\Gamma^{m}\_{t}(U,\sigma\_{U},-\sigma\_{T})\,\Gamma^{c}\_{t}(U,\sigma\_{U},\widehat{\sigma}\_{T},\rho\_{12})\,\Gamma^{c}\_{t}(T,-\sigma\_{T},\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}), |  |

and, for every t∈[U,T]t\in[U,T],

|  |  |  |
| --- | --- | --- |
|  | Γt(1)​(U,T)=Γts​(T,−1,σT)​Γtc​(T,−σT,σ^T,ρ12)​Γ^td​(T,σ¯,σ^T,ρ23).\Gamma^{(1)}\_{t}(U,T)=\Gamma^{s}\_{t}(T,-1,\sigma\_{T})\,\Gamma^{c}\_{t}(T,-\sigma\_{T},\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}). |  |

(ii) The foreign floating component I(2)I^{(2)} is equal to, for every t∈[0,U]t\in[0,U],

|  |  |  |
| --- | --- | --- |
|  | It(2)=At,Tc,f​B^U​(t,rtf)​Γt(2)​(U),Γt(2)​(U):=Γ^td​(U,σ¯,σ^U,ρ23),I^{(2)}\_{t}=A^{c,f}\_{t,T}\,\widehat{B}\_{U}(t,r^{f}\_{t})\,\Gamma^{(2)}\_{t}(U),\qquad\Gamma^{(2)}\_{t}(U):=\widehat{\Gamma}^{d}\_{t}(U,\bar{\sigma},\widehat{\sigma}\_{U},\rho\_{23}), |  |

and, for every t∈[U,T]t\in[U,T],

|  |  |  |
| --- | --- | --- |
|  | It(2)=At,Tc,f​exp⁡(∫Utruf​𝑑u)=At,Tc,f​(BUf)−1​Btf.I^{(2)}\_{t}=A^{c,f}\_{t,T}\,\exp\!\Big(\int\_{U}^{t}r^{f}\_{u}\,du\Big)=A^{c,f}\_{t,T}\,(B^{f}\_{U})^{-1}B^{f}\_{t}. |  |

(iii) The fixed component I(3)I^{(3)} is equal to, for every t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | It(3)=At,Tc,f​B^T​(t,rtf)​Γt(3)​(T),Γt(3)​(T):=Γ^td​(T,σ¯,σ^T,ρ23).I^{(3)}\_{t}=A^{c,f}\_{t,T}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(3)}\_{t}(T),\qquad\Gamma^{(3)}\_{t}(T):=\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}). |  |

###### Proof.

In view of ([2.1](#S2.E1 "In Definition 2.3. ‣ 2.2 Differential swaps and collateral conventions ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps")) and equalities
δ​Rd​(U,T)=exp⁡(∫UTrud​𝑑u)−1\delta R^{d}(U,T)=\exp(\int\_{U}^{T}r^{d}\_{u}\,du)-1 and
δ​Rf​(U,T)=exp⁡(∫UTruf​𝑑u)−1\delta R^{f}(U,T)=\exp(\int\_{U}^{T}r^{f}\_{u}\,du)-1,
the terminal payoff can be represented as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃𝐒Tγ,κ​(U,T)=exp⁡(∫UTrud​𝑑u)−γ​exp⁡(∫UTruf​𝑑u)−(1−γ+δ​κ).{\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)=\exp\!\Big(\int\_{U}^{T}r^{d}\_{u}\,du\Big)-\gamma\exp\!\Big(\int\_{U}^{T}r^{f}\_{u}\,du\Big)-(1-\gamma+\delta\kappa). |  | (4.2) |

Under full foreign collateralisation, the effective discount rate equals
rβ=rc=rf+αc,fr^{\beta}=r^{c}=r^{f}+\alpha^{c,f} and thus At,Tβ,f=At,Tc,fA^{\beta,f}\_{t,T}=A^{c,f}\_{t,T}. Hence

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tc,γ,κ​(U,T)=𝔼ℚ​[e−∫tT(ruf+αuc,f)​𝑑u​𝐃𝐒Tγ,κ​(U,T)|ℱt]=It(1)−γ​It(2)−(1−γ+δ​κ)​It(3),{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T)={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T}(r^{f}\_{u}+\alpha^{c,f}\_{u})\,du}\,{\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)\,\Big|\,\mathcal{F}\_{t}\Big]=I^{(1)}\_{t}-\gamma I^{(2)}\_{t}-(1-\gamma+\delta\kappa)I^{(3)}\_{t}, |  |

where we define the three pricing components by linearity.

Domestic floating leg.
For t∈[0,U]t\in[0,U],

|  |  |  |  |
| --- | --- | --- | --- |
|  | It(1)\displaystyle I^{(1)}\_{t} | :=𝔼ℚ​[e−∫tT(ruf+αuc,f)​𝑑u​e∫UTrud​𝑑u|ℱt]=At,Tc,f​𝔼ℚ​[e∫tTrud​𝑑u−∫tUrud​𝑑u−∫tTruf​𝑑u|ℱt],\displaystyle:={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T}(r^{f}\_{u}+\alpha^{c,f}\_{u})\,du}\,e^{\int\_{U}^{T}r^{d}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big]=A^{c,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{\int\_{t}^{T}r^{d}\_{u}\,du-\int\_{t}^{U}r^{d}\_{u}\,du-\int\_{t}^{T}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big], |  |

which yields the stated factorisation in terms of BU​(t,rtd)B\_{U}(t,r^{d}\_{t}), BT​(t,rtd)B\_{T}(t,r^{d}\_{t}) and B^T​(t,rtf)\widehat{B}\_{T}(t,r^{f}\_{t})
with correction term Γt(1)​(U,T)\Gamma^{(1)}\_{t}(U,T).
For t∈[U,T]t\in[U,T] we use e−∫tUrud​𝑑u=e∫Utrud​𝑑u=(BUd)−1​Btde^{-\int\_{t}^{U}r^{d}\_{u}\,du}=e^{\int\_{U}^{t}r^{d}\_{u}\,du}=(B^{d}\_{U})^{-1}B^{d}\_{t} and obtain the
second representation with Γt(1)​(U,T)\Gamma^{(1)}\_{t}(U,T).

Foreign floating leg.
For t∈[0,U]t\in[0,U],

|  |  |  |  |
| --- | --- | --- | --- |
|  | It(2):\displaystyle I^{(2)}\_{t}: | =𝔼ℚ​[e−∫tT(ruf+αuc,f)​𝑑u​e∫UTruf​𝑑u|ℱt]=At,Tc,f​𝔼ℚ​[e−∫tUruf​𝑑u|ℱt]\displaystyle={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T}(r^{f}\_{u}+\alpha^{c,f}\_{u})\,du}\,e^{\int\_{U}^{T}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big]=A^{c,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{U}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =At,Tc,f​B^U​(t,rtf)​Γ^td​(U,σ¯,σ^U,ρ23),\displaystyle=A^{c,f}\_{t,T}\,\widehat{B}\_{U}(t,r^{f}\_{t})\,\widehat{\Gamma}^{d}\_{t}(U,\bar{\sigma},\widehat{\sigma}\_{U},\rho\_{23}), |  |

where the last step follows from the drift-adjustment rule in Lemma [4.1](#S4.Thmlem1 "Lemma 4.1. ‣ 4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps").
For t∈[U,T]t\in[U,T], the quantity exp⁡(−∫tUruf​𝑑u)=exp⁡(∫Utruf​𝑑u)=(BUf)−1​Btf\exp(-\int\_{t}^{U}r^{f}\_{u}\,du)=\exp(\int\_{U}^{t}r^{f}\_{u}\,du)=(B^{f}\_{U})^{-1}B^{f}\_{t}
is ℱt\mathcal{F}\_{t}-measurable, which gives the stated expression.

Fixed leg.
For every t∈[0,T]t\in[0,T]

|  |  |  |
| --- | --- | --- |
|  | It(3):=𝔼ℚ​[e−∫tT(ruf+αuc,f)​𝑑u|ℱt]=At,Tc,f​𝔼ℚ​[e−∫tTruf​𝑑u|ℱt]=At,Tc,f​B^T​(t,rtf)​Γ^td​(T,σ¯,σ^T,ρ23),I^{(3)}\_{t}:={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T}(r^{f}\_{u}+\alpha^{c,f}\_{u})\,du}\,\Big|\,\mathcal{F}\_{t}\Big]=A^{c,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big]=A^{c,f}\_{t,T}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}), |  |

which is the claimed form with Γt(3)​(T)=Γ^td​(T,σ¯,σ^T,ρ23)\Gamma^{(3)}\_{t}(T)=\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}).
∎

For a fully foreign collateralised single-period SOFR/€STR differential swap, one may rewrite the relevant conditional expectation in a factorised form that differs from the usual convexity correction introduced in Section [4.1](#S4.SS1 "4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps").

###### Proposition 4.2.

For every t∈[0,T]t\in[0,T], the arbitrage-free price of the single-period SOFR/€STR swap with full foreign collateralisation satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tc,γ,κ​(U,T):=πtc​(𝐃𝐒Tγ,κ​(U,T))=It(1)−γ​It(2)−(1−γ+δ​κ)​It(3){\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T):=\pi^{c}\_{t}\big({\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)\big)=I^{(1)}\_{t}-\gamma I^{(2)}\_{t}-(1-\gamma+\delta\kappa)I^{(3)}\_{t} |  |

where the foreign floating leg I(2)I^{(2)} and the fixed leg I(3)I^{(3)} are
as given in Proposition [4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") and the price
of the domestic floating leg I(1)I^{(1)} is equal to

|  |  |  |
| --- | --- | --- |
|  | It(1)=At,Tc,f​(1+δ​Ftd​(U,T))​B^T​(t,rtf)​Γt(1)′​(U,T),t∈[0,T],I^{(1)}\_{t}=A^{c,f}\_{t,T}\,\big(1+\delta F^{d}\_{t}(U,T)\big)\widehat{B}\_{T}(t,r^{f}\_{t})\Gamma^{(1)^{\prime}}\_{t}(U,T),\qquad t\in[0,T], |  |

where the modified convexity correction Γt(1)′​(U,T)\Gamma^{(1)^{\prime}}\_{t}(U,T) satisfies, for t∈[0,U]t\in[0,U]

|  |  |  |
| --- | --- | --- |
|  | Γt(1)′​(U,T)=Γtc​(U,σU,σ^T,ρ12)​Γtc​(T,−σT,σ^T,ρ12)​Γ^td​(T,σ¯,σ^T,ρ23)\Gamma^{(1)^{\prime}}\_{t}(U,T)=\Gamma^{c}\_{t}(U,\sigma\_{U},\widehat{\sigma}\_{T},\rho\_{12})\,\Gamma^{c}\_{t}(T,-\sigma\_{T},\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}) |  |

and, for t∈[U,T]t\in[U,T]

|  |  |  |
| --- | --- | --- |
|  | Γt(1)′​(U,T)=Γtc​(T,−σT,σ^T,ρ12)​Γ^td​(T,σ¯,σ^T,ρ23).\Gamma^{(1)^{\prime}}\_{t}(U,T)=\Gamma^{c}\_{t}(T,-\sigma\_{T},\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}). |  |

###### Proof.

It suffices to establish the futures-based representation for the domestic floating component I(1)I^{(1)}. Recall that under full foreign collateralisation,

|  |  |  |
| --- | --- | --- |
|  | It(1)=At,Tc,f​𝔼ℚ​[e∫UTrud​d​u−∫tTruf​d​u|ℱt].I^{(1)}\_{t}=A^{c,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{\int\_{U}^{T}r^{d}\_{u}\,\mathop{}\!du-\int\_{t}^{T}r^{f}\_{u}\,\mathop{}\!du}\,\Big|\,\mathcal{F}\_{t}\Big]. |  |

Using δ​Rd​(U,T)=e∫UTrud​d​u−1\delta R^{d}(U,T)=e^{\int\_{U}^{T}r^{d}\_{u}\,\mathop{}\!du}-1 we obtain

|  |  |  |
| --- | --- | --- |
|  | 1+δ​Ftd​(U,T)=𝔼ℚ​[e∫UTrud​d​u|ℱt],t∈[0,T],1+\delta F^{d}\_{t}(U,T)={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{\int\_{U}^{T}r^{d}\_{u}\,\mathop{}\!du}\,\Big|\,\mathcal{F}\_{t}\Big],\qquad t\in[0,T], |  |

where Fd​(U,T)F^{d}(U,T) is the domestic interest-rate futures of Definition [3.1](#S3.Thmdefi1 "Definition 3.1. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").
Hence, our goal is to factorise the conditional expectation into the product
(1+δ​Ftd​(U,T))​B^T​(t,rtf)\big(1+\delta F^{d}\_{t}(U,T)\big)\widehat{B}\_{T}(t,r^{f}\_{t}) supplemented by a deterministic correction term.

Case t∈[0,U]t\in[0,U].
Applying the same convexity-correction factorisation to the *single* exponential moment
𝔼ℚ​[exp⁡(∫UTrud​d​u)∣ℱt]{{\mathbb{E}}}\_{\mathbb{Q}}\big[\exp(\int\_{U}^{T}r^{d}\_{u}\,\mathop{}\!du)\mid\mathcal{F}\_{t}\big] yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1+δ​Ftd​(U,T)=BU​(t,rtd)​[BT​(t,rtd)]−1​Γts​(T,−1,σT)​Γtm​(U,σU,−σT),t∈[0,U].1+\delta F^{d}\_{t}(U,T)=B\_{U}(t,r^{d}\_{t})\,[B\_{T}(t,r^{d}\_{t})]^{-1}\,\Gamma^{s}\_{t}(T,-1,\sigma\_{T})\,\Gamma^{m}\_{t}(U,\sigma\_{U},-\sigma\_{T}),\qquad t\in[0,U]. |  | (4.3) |

On the other hand, from Proposition [4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), we already have the
bond-based factorisation

|  |  |  |  |
| --- | --- | --- | --- |
|  | It(1)=At,Tc,f​BU​(t,rtd)​[BT​(t,rtd)]−1​B^T​(t,rtf)​Γt(1)​(U,T),t∈[0,U],I^{(1)}\_{t}=A^{c,f}\_{t,T}\,B\_{U}(t,r^{d}\_{t})\,[B\_{T}(t,r^{d}\_{t})]^{-1}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)}\_{t}(U,T),\qquad t\in[0,U], |  | (4.4) |

with

|  |  |  |
| --- | --- | --- |
|  | Γt(1)​(U,T)=Γts​(T,−1,σT)​Γtm​(U,σU,−σT)​Γtc​(U,σU,σ^T,ρ12)​Γtc​(T,−σT,σ^T,ρ12)​Γ^td​(T,σ¯,σ^T,ρ23).\Gamma^{(1)}\_{t}(U,T)=\Gamma^{s}\_{t}(T,-1,\sigma\_{T})\,\Gamma^{m}\_{t}(U,\sigma\_{U},-\sigma\_{T})\,\Gamma^{c}\_{t}(U,\sigma\_{U},\widehat{\sigma}\_{T},\rho\_{12})\,\Gamma^{c}\_{t}(T,-\sigma\_{T},\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\widehat{\sigma}\_{T},\rho\_{23}). |  |

Combining ([4.3](#S4.E3 "In Proof. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")) and ([4.4](#S4.E4 "In Proof. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")), we obtain

|  |  |  |
| --- | --- | --- |
|  | It(1)=At,Tc,f​(1+δ​Ftd​(U,T))​B^T​(t,rtf)​Γt(1)′​(U,T),t∈[0,U],I^{(1)}\_{t}=A^{c,f}\_{t,T}\,\big(1+\delta F^{d}\_{t}(U,T)\big)\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)^{\prime}}\_{t}(U,T),\qquad t\in[0,U], |  |

where Γt(1)′​(U,T)\Gamma^{(1)^{\prime}}\_{t}(U,T) as stated above.

Case t∈[U,T]t\in[U,T].
The same argument applies with BU​(t,rtd)=(BUd)−1​BtdB\_{U}(t,r^{d}\_{t})=(B^{d}\_{U})^{-1}B^{d}\_{t}. This yields the representation with the
corresponding correction Γt(1)′​(U,T)\Gamma^{(1)^{\prime}}\_{t}(U,T), and its explicit form is obtained by the same substitution.
∎

The adjustment introduced in
Proposition [4.2](#S4.Thmpro2 "Proposition 4.2. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")
is not a convexity correction in the sense of Section [4.1](#S4.SS1 "4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), but it plays an analogous role: it is a *modified correlation adjustment* induced by the Gaussian dependence between domestic and foreign short-rate factors. In particular, if the domestic and foreign rate factors are independent (or, more generally, uncorrelated in the Gaussian specification), then this adjustment collapses to one.

###### Remark 4.1.

The pricing formula of
Proposition [4.2](#S4.Thmpro2 "Proposition 4.2. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") is particularly convenient for the hedging analysis in
Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") since, once the floating leg is expressed directly in terms of the traded SOFR futures rate
Fd​(U,T)F^{d}(U,T), the ensuing Itô decomposition can be written in terms of the dynamics of the
domestic futures process. More generally, there is no single “best” closed-form expression: the same price can be given
several equivalent representations and their usefulness depends on the intended application.

### 4.3 Pricing of swaps with proportional foreign collateralisation

We consider a single-period SOFR/€STR payer swap referencing the accrual period [U,T][U,T] and settled in arrears at TT.
The collateral is again posted in the foreign currency
and is remunerated at a rate rc=rf+αc,fr^{c}=r^{f}+\alpha^{c,f}. Under the convention of proportional collateralisation introduced in Section [2.3](#S2.SS3 "2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"),
the collateral funding enters the pricing formula through the effective rate rβ=(1−β)​rh+β​rcr^{\beta}=(1-\beta)r^{h}+\beta r^{c}. Recall that rh=rd+αhr^{h}=r^{d}+\alpha^{h} and rc=rf+αc,fr^{c}=r^{f}+\alpha^{c,f} where αh\alpha^{h} and αc,f\alpha^{c,f} are deterministic spreads and thus

|  |  |  |
| --- | --- | --- |
|  | ruβ=β​ruf+(1−β)​rud+αuβ,f,αβ,f:=β​αc,f+(1−β)​αh.r^{\beta}\_{u}=\beta r^{f}\_{u}+(1-\beta)r^{d}\_{u}+\alpha^{\beta,f}\_{u},\qquad\alpha^{\beta,f}:=\beta\alpha^{c,f}+(1-\beta)\alpha^{h}. |  |

We introduce the extended deterministic discount factor

|  |  |  |
| --- | --- | --- |
|  | At,Tβ,f:=exp⁡(−∫tTαuβ,f​d​u).A^{\beta,f}\_{t,T}:=\exp\Big(-\int\_{t}^{T}\alpha\_{u}^{\beta,f}\,\mathop{}\!du\Big). |  |

The arbitrage-free price process for the swap with proportional foreign collateralisation is denoted by

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(U,T):=πtβ​(𝐃𝐒Tγ,κ​(U,T)),t∈[0,T].{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T):=\pi^{\beta}\_{t}\big({\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)\big),\qquad t\in[0,T]. |  |

For β=1\beta=1 the price 𝐃𝐒tβ,γ,κ​(U,T){\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T) given in
Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") reduces to the
price 𝐃𝐒tc,γ,κ​(U,T){\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T) of the swap with full foreign collateralisation,
which was obtained in Proposition [4.2](#S4.Thmpro2 "Proposition 4.2. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"),
while setting β=0\beta=0 yields the uncollateralised benchmark, which corresponds to effective discounting at the domestic funding rate rhr^{h}.

###### Proposition 4.3.

For every t∈[0,T]t\in[0,T], the arbitrage-free price of the single-period
SOFR/€STR swap with proportional foreign collateralisation at the level
β\beta satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(U,T):=πtβ​(𝐃𝐒Tγ,κ​(U,T))=It(1)−γ​It(2)−(1−γ+δ​κ)​It(3).{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T):=\pi^{\beta}\_{t}\big({\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)\big)=I^{(1)}\_{t}-\gamma I^{(2)}\_{t}-(1-\gamma+\delta\kappa)\,I^{(3)}\_{t}. |  |

(i) The domestic floating component I(1)I^{(1)} equals, for every t∈[0,U]t\in[0,U],

|  |  |  |
| --- | --- | --- |
|  | It(1)=At,Tβ,f​BU​(t,rtd)​[BT​(t,rtd)]−β​[B^T​(t,rtf)]β​Γt(1)​(U,T),I\_{t}^{(1)}=A^{\beta,f}\_{t,T}\,B\_{U}(t,r^{d}\_{t})\,[B\_{T}(t,r^{d}\_{t})]^{-\beta}\,[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\beta}\,\Gamma\_{t}^{(1)}(U,T), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γt(1)​(U,T)\displaystyle\Gamma\_{t}^{(1)}(U,T) | =Γts​(T,−β,σT)​Γts​(T,β,σ^T)​Γtm​(U,σU,−β​σT)​Γtc​(U,σU,β​σ^T,ρ12)\displaystyle=\Gamma^{s}\_{t}(T,-\beta,\sigma\_{T})\Gamma^{s}\_{t}(T,\beta,\widehat{\sigma}\_{T})\,\Gamma^{m}\_{t}(U,\sigma\_{U},-\beta\sigma\_{T})\Gamma^{c}\_{t}(U,\sigma\_{U},\beta\widehat{\sigma}\_{T},\rho\_{12}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×Γtc​(T,−β​σT,β​σ^T,ρ12)​Γ^td​(T,σ¯,β​σ^T,ρ23),\displaystyle\quad\times\Gamma^{c}\_{t}(T,-\beta\sigma\_{T},\beta\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\beta\widehat{\sigma}\_{T},\rho\_{23}), |  |

and, for every t∈[U,T]t\in[U,T],

|  |  |  |
| --- | --- | --- |
|  | It(1)=At,Tβ,f​(BUd)−1​Btd​[BT​(t,rtd)]−β​[B^T​(t,rtf)]β​Γt(1)​(U,T),I\_{t}^{(1)}=A^{\beta,f}\_{t,T}\,(B^{d}\_{U})^{-1}B^{d}\_{t}\,[B\_{T}(t,r^{d}\_{t})]^{-\beta}\,[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\beta}\,\Gamma\_{t}^{(1)}(U,T), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Γt(1)​(U,T)=Γts​(T,−β,σT)​Γts​(T,β,σ^T)​Γtc​(T,−β​σT,β​σ^T,ρ12)​Γ^td​(T,σ¯,β​σ^T,ρ23).\Gamma\_{t}^{(1)}(U,T)=\Gamma^{s}\_{t}(T,-\beta,\sigma\_{T})\Gamma^{s}\_{t}(T,\beta,\widehat{\sigma}\_{T})\,\Gamma^{c}\_{t}(T,-\beta\sigma\_{T},\beta\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\beta\widehat{\sigma}\_{T},\rho\_{23}). |  |

(ii) The foreign floating component I(2)I^{(2)} equals, for every t∈[0,U]t\in[0,U],

|  |  |  |
| --- | --- | --- |
|  | It(2)=At,Tβ,f​B^U​(t,rtf)​[BT​(t,rtd)]1−β​[B^T​(t,rtf)]β−1​Γt(2)​(U,T),I\_{t}^{(2)}=A^{\beta,f}\_{t,T}\,\widehat{B}\_{U}(t,r^{f}\_{t})\,[B\_{T}(t,r^{d}\_{t})]^{1-\beta}\,[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\beta-1}\,\Gamma\_{t}^{(2)}(U,T), |  |

where the deterministic correction is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γt(2)​(U,T)\displaystyle\Gamma\_{t}^{(2)}(U,T) | =Γts​(T,1−β,σT)​Γts​(T,β−1,σ^T)​Γtm​(U,σ^U,(β−1)​σ^T)\displaystyle=\Gamma^{s}\_{t}(T,1-\beta,\sigma\_{T})\,\Gamma^{s}\_{t}(T,\beta-1,\widehat{\sigma}\_{T})\,\Gamma^{m}\_{t}(U,\widehat{\sigma}\_{U},(\beta-1)\widehat{\sigma}\_{T}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×Γtc​(U,(1−β)​σT,σ^U,ρ12)​Γtc​(T,(1−β)​σT,(β−1)​σ^T,ρ12)\displaystyle\quad\times\Gamma^{c}\_{t}(U,(1-\beta)\sigma\_{T},\widehat{\sigma}\_{U},\rho\_{12})\,\Gamma^{c}\_{t}(T,(1-\beta)\sigma\_{T},(\beta-1)\widehat{\sigma}\_{T},\rho\_{12}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×Γ^td​(U,σ¯,σ^U,ρ23)​Γ^td​(T,σ¯,(β−1)​σ^T,ρ23).\displaystyle\quad\times\widehat{\Gamma}^{d}\_{t}(U,\bar{\sigma},\widehat{\sigma}\_{U},\rho\_{23})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},(\beta-1)\widehat{\sigma}\_{T},\rho\_{23}). |  |

For every t∈[U,T]t\in[U,T],

|  |  |  |
| --- | --- | --- |
|  | It(2)=At,Tβ,f​(BUf)−1​Btf​[BT​(t,rtd)]1−β​[B^T​(t,rtf)]β−1​Γt(2)​(T),I\_{t}^{(2)}=A^{\beta,f}\_{t,T}\,(B^{f}\_{U})^{-1}B^{f}\_{t}\,[B\_{T}(t,r^{d}\_{t})]^{1-\beta}\,[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\beta-1}\,\Gamma\_{t}^{(2)}(T), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γt(2)​(T)\displaystyle\Gamma\_{t}^{(2)}(T) | =Γts​(T,1−β,σT)​Γts​(T,β−1,σ^T)​Γtc​(T,(1−β)​σT,(β−1)​σ^T,ρ12)​Γ^td​(T,σ¯,(β−1)​σ^T,ρ23).\displaystyle=\Gamma^{s}\_{t}(T,1-\beta,\sigma\_{T})\,\Gamma^{s}\_{t}(T,\beta-1,\widehat{\sigma}\_{T})\,\Gamma^{c}\_{t}(T,(1-\beta)\sigma\_{T},(\beta-1)\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},(\beta-1)\widehat{\sigma}\_{T},\rho\_{23}). |  |

(iii) The fixed component I(3)I^{(3)} equals, for every t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | It(3)=At,Tβ,f​[BT​(t,rtd)]1−β​[B^T​(t,rtf)]β​Γt(3)​(T),I\_{t}^{(3)}=A^{\beta,f}\_{t,T}\,[B\_{T}(t,r^{d}\_{t})]^{1-\beta}\,[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\beta}\,\Gamma\_{t}^{(3)}(T), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γt(3)​(T)\displaystyle\Gamma\_{t}^{(3)}(T) | =Γts​(T,1−β,σT)​Γts​(T,β,σ^T)​Γtc​(T,(1−β)​σT,β​σ^T,ρ12)​Γ^td​(T,σ¯,β​σ^T,ρ23).\displaystyle=\Gamma^{s}\_{t}(T,1-\beta,\sigma\_{T})\,\Gamma^{s}\_{t}(T,\beta,\widehat{\sigma}\_{T})\,\Gamma^{c}\_{t}(T,(1-\beta)\sigma\_{T},\beta\widehat{\sigma}\_{T},\rho\_{12})\,\widehat{\Gamma}^{d}\_{t}(T,\bar{\sigma},\beta\widehat{\sigma}\_{T},\rho\_{23}). |  |

###### Proof.

Using ([4.2](#S4.E2 "In Proof. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")), we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(U,T)=𝔼ℚ​[e−∫tTruβ​𝑑u​𝐃𝐒Tγ,κ​(U,T)|ℱt]=It(1)−γ​It(2)−(1−γ+δ​κ)​It(3),{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T)={{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}r^{\beta}\_{u}\,du}\,{\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T)\,\Big|\,\mathcal{F}\_{t}\right]=I^{(1)}\_{t}-\gamma I^{(2)}\_{t}-(1-\gamma+\delta\kappa)I^{(3)}\_{t}, |  |

where I(1),I(2),I(3)I^{(1)},I^{(2)},I^{(3)} correspond to the three terms in ([4.2](#S4.E2 "In Proof. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")).

Domestic floating leg.
For t∈[0,U]t\in[0,U],

|  |  |  |  |
| --- | --- | --- | --- |
|  | It(1)\displaystyle I\_{t}^{(1)} | =𝔼ℚ​[e−∫tTruβ​𝑑u​e∫UTrud​𝑑u|ℱt]=At,Tβ,f​𝔼ℚ​[e−∫tT(β​ruf+(1−β)​rud)​𝑑u​e∫UTrud​𝑑u|ℱt]\displaystyle={{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}r^{\beta}\_{u}\,du}\,e^{\int\_{U}^{T}r^{d}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\right]=A^{\beta,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}(\beta r^{f}\_{u}+(1-\beta)r^{d}\_{u})\,du}\,e^{\int\_{U}^{T}r^{d}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =At,Tβ,f​𝔼ℚ​[e∫tTβ​rud​𝑑u−∫tUrud​𝑑u−∫tTβ​ruf​𝑑u|ℱt],\displaystyle=A^{\beta,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{\int\_{t}^{T}\beta r^{d}\_{u}\,du-\int\_{t}^{U}r^{d}\_{u}\,du-\int\_{t}^{T}\beta r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\right], |  |

which yields the factorisation stated with Γt(1)​(U,T)\Gamma^{(1)}\_{t}(U,T) by Lemma [4.1](#S4.Thmlem1 "Lemma 4.1. ‣ 4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps").
For t∈[U,T]t\in[U,T] we use e−∫tUrud​𝑑u=e∫Utrud​𝑑u=(BUd)−1​Btde^{-\int\_{t}^{U}r^{d}\_{u}\,du}=e^{\int\_{U}^{t}r^{d}\_{u}\,du}=(B^{d}\_{U})^{-1}B^{d}\_{t}
and obtain the second representation.

Foreign floating leg.
For t∈[0,U]t\in[0,U],

|  |  |  |  |
| --- | --- | --- | --- |
|  | It(2)\displaystyle I\_{t}^{(2)} | =𝔼ℚ​[e−∫tTruβ​𝑑u​e∫UTruf​𝑑u|ℱt]=At,Tβ,f​𝔼ℚ​[e−∫tT(β​ruf+(1−β)​rud)​𝑑u​e∫UTruf​𝑑u|ℱt]\displaystyle={{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}r^{\beta}\_{u}\,du}\,e^{\int\_{U}^{T}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\right]=A^{\beta,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}(\beta r^{f}\_{u}+(1-\beta)r^{d}\_{u})\,du}\,e^{\int\_{U}^{T}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =At,Tβ,f​𝔼ℚ​[e−(1−β)​∫tTrud​𝑑u+(1−β)​∫tTruf​𝑑u−∫tUruf​𝑑u|ℱt],\displaystyle=A^{\beta,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-(1-\beta)\int\_{t}^{T}r^{d}\_{u}\,du+(1-\beta)\int\_{t}^{T}r^{f}\_{u}\,du-\int\_{t}^{U}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\right], |  |

and Lemma [4.1](#S4.Thmlem1 "Lemma 4.1. ‣ 4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") gives the asserted representation.
For t∈[U,T]t\in[U,T], we use the equalities e−∫tUruf​𝑑u=e∫Utruf​𝑑u=(BUf)−1​Btfe^{-\int\_{t}^{U}r^{f}\_{u}\,du}=e^{\int\_{U}^{t}r^{f}\_{u}\,du}=(B^{f}\_{U})^{-1}B^{f}\_{t}
to obtain the second expression and the adjustment Γt(2)​(T)\Gamma^{(2)}\_{t}(T).

Fixed leg.
Finally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | It(3)\displaystyle I\_{t}^{(3)} | =𝔼ℚ​[e−∫tTruβ​𝑑u|ℱt]=At,Tβ,f​𝔼ℚ​[e−∫tT((1−β)​rud+β​ruf)​𝑑u|ℱt],\displaystyle={{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}r^{\beta}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\right]=A^{\beta,f}\_{t,T}\,{{\mathbb{E}}}\_{\mathbb{Q}}\!\left[e^{-\int\_{t}^{T}((1-\beta)r^{d}\_{u}+\beta r^{f}\_{u})\,du}\,\Big|\,\mathcal{F}\_{t}\right], |  |

so Lemma [4.1](#S4.Thmlem1 "Lemma 4.1. ‣ 4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") yields the stated factorisation with Γt(3)​(T)\Gamma^{(3)}\_{t}(T).
∎

Under our Gaussian specification with deterministic volatilities, all convexity corrections are deterministic functions of time. Hence, they do not introduce any additional hedgeable risk factors: in the Itô decomposition of the price, they only scale the exposure and contribute no new stochastic driver.

### 4.4 Extension to multi-period differential swaps

We extend the single-period pricing results of Section [4.3](#S4.SS3 "4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") to a multi-period SOFR/€STR payer swap with payment dates
T0<T1<⋯<TnT\_{0}<T\_{1}<\cdots<T\_{n} and accrual factors δj:=Tj−Tj−1\delta\_{j}:=T\_{j}-T\_{j-1}.
For j=1,2,…,nj=1,2,\dots,n, the jjth coupon (settled in arrears at TjT\_{j}) equals

|  |  |  |
| --- | --- | --- |
|  | δj​(Rd​(Tj−1,Tj)−γ​Rf​(Tj−1,Tj)−κ)=exp⁡(∫Tj−1Tjrud​𝑑u)−γ​exp⁡(∫Tj−1Tjruf​𝑑u)−(1−γ+δj​κ).\delta\_{j}\big(R^{d}(T\_{j-1},T\_{j})-\gamma R^{f}(T\_{j-1},T\_{j})-\kappa\big)=\exp\!\Big(\int\_{T\_{j-1}}^{T\_{j}}r^{d}\_{u}\,du\Big)-\gamma\exp\!\Big(\int\_{T\_{j-1}}^{T\_{j}}r^{f}\_{u}\,du\Big)-(1-\gamma+\delta\_{j}\kappa). |  |

We assume proportional foreign collateralisation at level β∈[0,1]\beta\in[0,1] with collateral posted in foreign
currency (EUR) and remunerated at rc=rf+αc,fr^{c}=r^{f}+\alpha^{c,f}.
As in the preceding section, the effective hedge rate is

|  |  |  |
| --- | --- | --- |
|  | ruβ=β​ruf+(1−β)​rud+αuβ,f,αβ,f:=β​αc,f+(1−β)​αh,r^{\beta}\_{u}=\beta r^{f}\_{u}+(1-\beta)r^{d}\_{u}+\alpha^{\beta,f}\_{u},\qquad\alpha^{\beta,f}:=\beta\alpha^{c,f}+(1-\beta)\alpha^{h}, |  |

and we set the deterministic factor

|  |  |  |
| --- | --- | --- |
|  | At,Tβ,f:=exp⁡(−∫tTαuβ,f​𝑑u),T≥t.A^{\beta,f}\_{t,T}:=\exp\Big(-\int\_{t}^{T}\alpha^{\beta,f}\_{u}\,du\Big),\qquad T\geq t. |  |

###### Proposition 4.4.

For every t∈[0,Tn]t\in[0,T\_{n}], let k​(t):=min⁡{j∈{1,2,…,n}:t≤Tj}.k(t):=\min\{j\in\{1,2,\dots,n\}:t\leq T\_{j}\}.
Then the arbitrage-free (ex-dividend) price of the multi-period SOFR/€STR swap with proportional foreign collateralisation at level β\beta satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(T0,n)\displaystyle{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(T\_{0},n) | :=πtβ​(∑j=k​(t)nδj​(Rd​(Tj−1,Tj)−γ​Rf​(Tj−1,Tj)−κ))\displaystyle:=\pi^{\beta}\_{t}\!\left(\sum\_{j=k(t)}^{n}\delta\_{j}\big(R^{d}(T\_{j-1},T\_{j})-\gamma R^{f}(T\_{j-1},T\_{j})-\kappa\big)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=k​(t)n(Ij(1)​(t)−γ​Ij(2)​(t)−(1−γ+δj​κ)​Ij(3)​(t)),\displaystyle=\sum\_{j=k(t)}^{n}\Big(I^{(1)}\_{j}(t)-\gamma I^{(2)}\_{j}(t)-(1-\gamma+\delta\_{j}\kappa)\,I^{(3)}\_{j}(t)\Big), |  |

where, for each j=1,2,…,nj=1,2,\dots,n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ij(1)​(t)\displaystyle I^{(1)}\_{j}(t) | :=𝔼ℚ​[e−∫tTjruβ​𝑑u​e∫Tj−1Tjrud​𝑑u|ℱt],Ij(2)​(t):=𝔼ℚ​[e−∫tTjruβ​𝑑u​e∫Tj−1Tjruf​𝑑u|ℱt],\displaystyle:={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T\_{j}}r^{\beta}\_{u}\,du}\,e^{\int\_{T\_{j-1}}^{T\_{j}}r^{d}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big],\quad I^{(2)}\_{j}(t):={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T\_{j}}r^{\beta}\_{u}\,du}\,e^{\int\_{T\_{j-1}}^{T\_{j}}r^{f}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ij(3)​(t)\displaystyle I^{(3)}\_{j}(t) | :=𝔼ℚ​[e−∫tTjruβ​𝑑u|ℱt].\displaystyle:={{\mathbb{E}}}\_{\mathbb{Q}}\Big[e^{-\int\_{t}^{T\_{j}}r^{\beta}\_{u}\,du}\,\Big|\,\mathcal{F}\_{t}\Big]. |  |

(i) If t∈[0,Tj−1]t\in[0,T\_{j-1}], then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ij(1)​(t)\displaystyle I^{(1)}\_{j}(t) | =At,Tjβ,f​BTj−1​(t,rtd)​[BTj​(t,rtd)]−β​[B^Tj​(t,rtf)]β​Γt(1)​(Tj−1,Tj),\displaystyle=A^{\beta,f}\_{t,T\_{j}}\,B\_{T\_{j-1}}(t,r^{d}\_{t})\,[B\_{T\_{j}}(t,r^{d}\_{t})]^{-\beta}\,[\widehat{B}\_{T\_{j}}(t,r^{f}\_{t})]^{\beta}\,\Gamma^{(1)}\_{t}(T\_{j-1},T\_{j}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ij(2)​(t)\displaystyle I^{(2)}\_{j}(t) | =At,Tjβ,f​B^Tj−1​(t,rtf)​[BTj​(t,rtd)]1−β​[B^Tj​(t,rtf)]β−1​Γt(2)​(Tj−1,Tj),\displaystyle=A^{\beta,f}\_{t,T\_{j}}\,\widehat{B}\_{T\_{j-1}}(t,r^{f}\_{t})\,[B\_{T\_{j}}(t,r^{d}\_{t})]^{1-\beta}\,[\widehat{B}\_{T\_{j}}(t,r^{f}\_{t})]^{\beta-1}\,\Gamma^{(2)}\_{t}(T\_{j-1},T\_{j}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ij(3)​(t)\displaystyle I^{(3)}\_{j}(t) | =At,Tjβ,f​[BTj​(t,rtd)]1−β​[B^Tj​(t,rtf)]β​Γt(3)​(Tj).\displaystyle=A^{\beta,f}\_{t,T\_{j}}\,[B\_{T\_{j}}(t,r^{d}\_{t})]^{1-\beta}\,[\widehat{B}\_{T\_{j}}(t,r^{f}\_{t})]^{\beta}\,\Gamma^{(3)}\_{t}(T\_{j}). |  |

(ii) If t∈[Tj−1,Tj]t\in[T\_{j-1},T\_{j}], then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ij(1)​(t)\displaystyle I^{(1)}\_{j}(t) | =At,Tjβ,f​(BTj−1d)−1​Btd​[BTj​(t,rtd)]−β​[B^Tj​(t,rtf)]β​Γt(1)​(Tj),\displaystyle=A^{\beta,f}\_{t,T\_{j}}\,(B^{d}\_{T\_{j-1}})^{-1}B^{d}\_{t}\,[B\_{T\_{j}}(t,r^{d}\_{t})]^{-\beta}\,[\widehat{B}\_{T\_{j}}(t,r^{f}\_{t})]^{\beta}\,\Gamma^{(1)}\_{t}(T\_{j}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ij(2)​(t)\displaystyle I^{(2)}\_{j}(t) | =At,Tjβ,f​(BTj−1f)−1​Btf​[BTj​(t,rtd)]1−β​[B^Tj​(t,rtf)]β−1​Γt(2)​(Tj),\displaystyle=A^{\beta,f}\_{t,T\_{j}}\,(B^{f}\_{T\_{j-1}})^{-1}B^{f}\_{t}\,[B\_{T\_{j}}(t,r^{d}\_{t})]^{1-\beta}\,[\widehat{B}\_{T\_{j}}(t,r^{f}\_{t})]^{\beta-1}\,\Gamma^{(2)}\_{t}(T\_{j}), |  |

and Ij(3)​(t)I^{(3)}\_{j}(t) is the same as in part (i). Moreover, under our Gaussian specification with deterministic volatilities, all correction factors admit closed-form expressions obtained from Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") by substitutions
(U,T)↦(Tj−1,Tj)(U,T)\mapsto(T\_{j-1},T\_{j}) and δ↦δj\delta\mapsto\delta\_{j}.

###### Proof.

Linearity of the pricing operator πtβ​(⋅)\pi^{\beta}\_{t}(\cdot) and additivity of the swap payoff yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(T0,n)\displaystyle{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(T\_{0},n) | =∑j=k​(t)nπtβ​(e∫Tj−1Tjrud​𝑑u−γ​e∫Tj−1Tjruf​𝑑u−(1−γ+δj​κ))\displaystyle=\sum\_{j=k(t)}^{n}\pi^{\beta}\_{t}\!\left(e^{\int\_{T\_{j-1}}^{T\_{j}}r^{d}\_{u}\,du}-\gamma e^{\int\_{T\_{j-1}}^{T\_{j}}r^{f}\_{u}\,du}-(1-\gamma+\delta\_{j}\kappa)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=k​(t)n(Ij(1)​(t)−γ​Ij(2)​(t)−(1−γ+δj​κ)​Ij(3)​(t)).\displaystyle=\sum\_{j=k(t)}^{n}\Big(I^{(1)}\_{j}(t)-\gamma I^{(2)}\_{j}(t)-(1-\gamma+\delta\_{j}\kappa)\,I^{(3)}\_{j}(t)\Big). |  |

Each triple (Ij(1),Ij(2),Ij(3))(I^{(1)}\_{j},I^{(2)}\_{j},I^{(3)}\_{j}) is handled exactly as in the single-period case
(Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")) by replacing (U,T)(U,T) with (Tj−1,Tj)(T\_{j-1},T\_{j})
(and δ\delta with δj\delta\_{j}) and using the identities
BTj−1​(t,rtd)=(BTj−1d)−1​BtdB\_{T\_{j-1}}(t,r^{d}\_{t})=(B^{d}\_{T\_{j-1}})^{-1}B^{d}\_{t} and
e−∫tTj−1ruf​𝑑u=(BTj−1f)−1​Btfe^{-\int\_{t}^{T\_{j-1}}r^{f}\_{u}\,du}=(B^{f}\_{T\_{j-1}})^{-1}B^{f}\_{t} when t≥Tj−1t\geq T\_{j-1}.
∎

###### Corollary 4.1.

The arbitrage-free price of the multi-period SOFR/€STR swap with proportional foreign collateralisation is affine in κ\kappa and can be represented as, for every t∈[0,T0]t\in[0,T\_{0}],

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(T0,n)=∑j=1n(Ij(1)​(t)−γ​Ij(2)​(t)−(1−γ)​Ij(3)​(t))−κ​∑j=1nδj​Ij(3)​(t).{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(T\_{0},n)=\sum\_{j=1}^{n}\Big(I^{(1)}\_{j}(t)-\gamma I^{(2)}\_{j}(t)-(1-\gamma)\,I^{(3)}\_{j}(t)\Big)-\kappa\sum\_{j=1}^{n}\delta\_{j}\,I^{(3)}\_{j}(t). |  | (4.5) |

Since Ij(3)​(t)>0I^{(3)}\_{j}(t)>0 for all jj, the par swap rate
κ⋆=κt⋆​(T0,n;β,γ)\kappa^{\star}=\kappa^{\star}\_{t}(T\_{0},n;\beta,\gamma), which is implicitly
defined through the equality 𝐃𝐒tβ,γ,κ⋆​(T0,n)=0{\rm\bf DS}^{\beta,\gamma,\kappa^{\star}}\_{t}(T\_{0},n)=0, is uniquely given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | κt⋆​(T0,n;β,γ)=∑j=1n(Ij(1)​(t)−γ​Ij(2)​(t)−(1−γ)​Ij(3)​(t))∑j=1nδj​Ij(3)​(t).\kappa^{\star}\_{t}(T\_{0},n;\beta,\gamma)=\frac{\sum\_{j=1}^{n}\Big(I^{(1)}\_{j}(t)-\gamma I^{(2)}\_{j}(t)-(1-\gamma)I^{(3)}\_{j}(t)\Big)}{\sum\_{j=1}^{n}\delta\_{j}I^{(3)}\_{j}(t)}. |  | (4.6) |

Equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(T0,n)=(κt⋆​(T0,n;β,γ)−κ)​∑j=1nδj​Ij(3)​(t).{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(T\_{0},n)=\big(\kappa^{\star}\_{t}(T\_{0},n;\beta,\gamma)-\kappa\big)\,\sum\_{j=1}^{n}\delta\_{j}I^{(3)}\_{j}(t). |  | (4.7) |

###### Remark 4.2.

Proposition [4.4](#S4.Thmpro4 "Proposition 4.4. ‣ 4.4 Extension to multi-period differential swaps ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") covers the case of full foreign collateralisation by setting β=1\beta=1,
and the uncollateralised (domestic funding) benchmark upon setting β=0\beta=0. In both cases, the multi-period price is obtained by the same decomposition with the corresponding specialisation of
convexity corrections.

## 5 Futures-Based Hedging under Collateral Currency Choice

This section develops a futures-based replication and hedging framework for differential swaps under the choice of collateral currency.
Consistent with the trading setup of Section [2](#S2 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"), we restrict the hedging instruments to domestic SOFR futures and foreign €STR futures.
The case γ=0\gamma=0 recovers the SOFR swap as a special instance of the differential-swap family, but the hedging methodology applies throughout.
The position in foreign futures is represented in domestic-currency units through the auxiliary process Ff,qF^{f,q} in ([2.2](#S2.E2 "In Definition 2.5. ‣ 2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps")), which accounts for the quadratic covariation effects induced by daily settlement as well as the FX conversion.
The diffusion inputs required in the derivations in the following are collected in Remarks [3.1](#S3.Thmrem1 "Remark 3.1. ‣ 3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), [3.2](#S3.Thmrem2 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), and [3.3](#S3.Thmrem3 "Remark 3.3. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").

Under proportional collateralisation Ct=−βt​Vt​(φ,C)C\_{t}=-\beta\_{t}V\_{t}(\varphi,C), the cash position is not an independent control:
once the wealth process is replicated, φ0\varphi^{0} is determined by the equality

|  |  |  |
| --- | --- | --- |
|  | (1−βt)​Vt​(φ,C)=Vtp​(φ,C)=φt0​Bth,t∈[0,T].(1-\beta\_{t})V\_{t}(\varphi,C)=V\_{t}^{p}(\varphi,C)=\varphi^{0}\_{t}\,B^{h}\_{t},\qquad t\in[0,T]. |  |

Hence it suffices to identify futures hedge ratios (φd,φf)(\varphi^{d},\varphi^{f}).
We first treat the fully foreign-collateralised benchmark, denoted by the superscript cc (corresponding to
β≡1\beta\equiv 1), and then turn to proportional foreign collateralisation with a constant level β∈[0,1]\beta\in[0,1].

In the fully foreign-collateralised case, we have φ0≡0\varphi^{0}\equiv 0 and replication is entirely funded through the collateral remuneration rate rcr^{c}. To identify the remaining components of the hedging strategy, we will use the futures-based pricing representation from
Proposition [4.2](#S4.Thmpro2 "Proposition 4.2. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), which expresses the floating component directly in terms of the
traded SOFR futures rate and leads to a transparent Itô decomposition. The same replication programme could also be
carried out starting from Proposition [4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), but the resulting dynamics are less
transparent and we do not pursue it here.

### 5.1 Hedging under full foreign collateralisation

To support the pricing results of Section [4.2](#S4.SS2 "4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") by replication, we now construct a
replicating strategy for the single-period SOFR/€STR swap with full foreign collateralisation. The key point is that once the collateral currency is foreign, valuation inherits an additional stochastic driver other than the foreign floating leg through the foreign discounting factor. In the present framework, this additional risk is spanned by the foreign interest-rate futures, so the hedger can neutralize it jointly with the domestic SOFR exposure using *two* traded futures contracts.

We work here under full foreign collateralisation, i.e., β=1\beta=1 and rc=rf+αc,fr^{c}=r^{f}+\alpha^{c,f}, so the effective
rate equals the collateral remuneration rate and the cash component vanishes. Indeed, the collateral rule is
Ct=−Vt​(φ,C)C\_{t}=-V\_{t}(\varphi,C), hence Vtp​(φ,C)=Vt​(φ,C)+Ct=0V\_{t}^{p}(\varphi,C)=V\_{t}(\varphi,C)+C\_{t}=0 and thus φ0≡0\varphi^{0}\equiv 0.
Consequently, replication reduces to the identification of futures hedge ratios (φd,φf)(\varphi^{d},\varphi^{f}) for futures contracts.

In contrast to classical single-period LIBOR swaps, the price process of a SOFR/€STR swap continues to evolve
over the accrual interval [U,T][U,T]. In particular, the hedge ratios are not static in [U,T][U,T] because the (backward-looking) realised rates continue to accumulate, and the futures diffusion coefficients change at t=Ut=U
(see Remark [3.2](#S3.Thmrem2 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps")). As the replicating strategy is expected to be continuous, it is natural to conjecture that φU−d=φU+d\varphi^{d}\_{U^{-}}=\varphi^{d}\_{U^{+}} and φU−f=φU+f\varphi^{f}\_{U^{-}}=\varphi^{f}\_{U^{+}},
which will be shown to hold.

Recall that the single-period SOFR/€STR payer swap over [U,T][U,T] has payoff at TT

|  |  |  |
| --- | --- | --- |
|  | XT=δ​(Rd​(U,T)−γ​Rf​(U,T)−κ)=exp⁡(∫UTrud​d​u)−γ​exp⁡(∫UTruf​d​u)−(1−γ+δ​κ),X\_{T}=\delta\big(R^{d}(U,T)-\gamma R^{f}(U,T)-\kappa\big)=\exp\!\Big(\int\_{U}^{T}r^{d}\_{u}\,\mathop{}\!du\Big)-\gamma\exp\!\Big(\int\_{U}^{T}r^{f}\_{u}\,\mathop{}\!du\Big)-(1-\gamma+\delta\kappa), |  |

where δ=T−U\delta=T-U.
Its fully foreign-collateralised arbitrage-free price, denoted by 𝐃𝐒tc,γ,κ​(U,T){\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T), is given in Proposition [4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"). We now construct an explicit replicating strategy.

###### Proposition 5.1.

Consider the single-period SOFR/€STR swap with terminal payoff
𝐃𝐒Tγ,κ​(U,T){\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T) and full foreign collateralisation. The arbitrage-free price process
𝐃𝐒c,γ,κ​(U,T){\rm\bf DS}^{c,\gamma,\kappa}(U,T) can be replicated by a self-financing collateralised futures strategy
(φ,C)=(φ0,φd,φf,C)(\varphi,C)=(\varphi^{0},\varphi^{d},\varphi^{f},C) with C=−VC=-V and

|  |  |  |
| --- | --- | --- |
|  | Vt​(φ,C)=𝐃𝐒tc,γ,κ​(U,T),t∈[0,T].V\_{t}(\varphi,C)={\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T),\qquad t\in[0,T]. |  |

The hedge ratios are given by φ0≡0\varphi^{0}\equiv 0,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | φtd\displaystyle\varphi^{d}\_{t} | =δ​At,Tc,f​B^T​(t,rtf)​Γt(1)′​(U,T),\displaystyle=\delta\,A^{c,f}\_{t,T}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)^{\prime}}\_{t}(U,T), |  | (5.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | φtf\displaystyle\varphi^{f}\_{t} | =1νtf,q​(σ^T​(t)​𝐃𝐒tc,γ,κ​(U,T)+γ​(σ^T​(t)−𝟏{t≤U}​σ^U​(t))​It(2)),\displaystyle=\frac{1}{\nu^{f,q}\_{t}}\Big(\widehat{\sigma}\_{T}(t)\,{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T)+\gamma(\widehat{\sigma}\_{T}(t)-\mathbf{1}\_{\{t\leq U\}}\,\widehat{\sigma}\_{U}(t))\,I\_{t}^{(2)}\Big), |  | (5.2) |

where:
(i) Γ(1)′​(U,T)\Gamma^{(1)^{\prime}}(U,T) is the modified correlation adjustment of Proposition [4.2](#S4.Thmpro2 "Proposition 4.2. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"),
(ii) σ^T​(t)\widehat{\sigma}\_{T}(t) (resp., σ^U​(t)\widehat{\sigma}\_{U}(t)) is the diffusion coefficient of B^T​(t,rtf)\widehat{B}\_{T}(t,r^{f}\_{t}) (resp., B^U​(t,rtf)\widehat{B}\_{U}(t,r^{f}\_{t})) from Remark [3.1](#S3.Thmrem1 "Remark 3.1. ‣ 3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"),
(iii) νf,q\nu^{f,q} is the diffusion coefficient of Ff,q​(U,T)F^{f,q}(U,T) from Remark [3.3](#S3.Thmrem3 "Remark 3.3. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), and I(2)I^{(2)} is the pricing component of Proposition [4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps").

###### Proof.

The wealth dynamics of any self-financing futures strategy with full foreign collateralisation reduce to φ0≡0\varphi^{0}\equiv 0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt​(φ,C)=rtc​Vt​(φ,C)​d​t+φtd​d​Ftd​(U,T)+φtf​d​Ftf,q​(U,T),\mathop{}\!dV\_{t}(\varphi,C)=r^{c}\_{t}\,V\_{t}(\varphi,C)\,\mathop{}\!dt+\varphi^{d}\_{t}\,\mathop{}\!dF^{d}\_{t}(U,T)+\varphi^{f}\_{t}\,\mathop{}\!dF^{f,q}\_{t}(U,T), |  | (5.3) |

where, by Remark [3.3](#S3.Thmrem3 "Remark 3.3. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), d​Ftf,q​(U,T)=νtf,q​d​Zt2\mathop{}\!dF^{f,q}\_{t}(U,T)=\nu^{f,q}\_{t}\,\mathop{}\!dZ^{2}\_{t} under ℚ\mathbb{Q}.
We seek (φd,φf)(\varphi^{d},\varphi^{f}) such that Vt​(φ,C)=𝐃𝐒tc,γ,κ​(U,T)V\_{t}(\varphi,C)={\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T) for all t∈[0,T]t\in[0,T]. To this end, we work with the price decomposition

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tc,γ,κ​(U,T)=It(1)−γ​It(2)−(1−γ+δ​κ)​It(3),{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T)=I\_{t}^{(1)}-\gamma I\_{t}^{(2)}-(1-\gamma+\delta\kappa)\,I\_{t}^{(3)}, |  |

where I(1)I^{(1)} is given in Proposition [4.2](#S4.Thmpro2 "Proposition 4.2. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") and I(2),I(3)I^{(2)},I^{(3)} are as in Proposition [4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"). In particular, At,Tc,fA^{c,f}\_{t,T} and all correction factors are deterministic functions of tt. Since (Btc)−1​𝐃𝐒tc,γ,κ​(U,T)(B^{c}\_{t})^{-1}{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T) is a ℚ\mathbb{Q}-martingale, it suffices to match the local martingale parts in the Itô decompositions. Using Propositions [4.1](#S4.Thmpro1 "Proposition 4.1. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") and [4.2](#S4.Thmpro2 "Proposition 4.2. ‣ 4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), we obtain, for every t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | It(1)\displaystyle I^{(1)}\_{t} | =At,Tc,f​B^T​(t,rtf)​Γt(1)′​(U,T)​(1+δ​Ftd​(U,T)),\displaystyle=A^{c,f}\_{t,T}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)^{\prime}}\_{t}(U,T)\,\big(1+\delta\,F^{d}\_{t}(U,T)\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | It(2)\displaystyle I^{(2)}\_{t} | =At,Tc,f​B^U​(t,rtf)​Γt(2)​(U)​𝟙{t≤U}+At,Tc,f​(BUf)−1​Btf​𝟙{t>U},\displaystyle=A^{c,f}\_{t,T}\,\widehat{B}\_{U}(t,r^{f}\_{t})\,\Gamma^{(2)}\_{t}(U)\mathds{1}\_{\{t\leq U\}}+A^{c,f}\_{t,T}\,(B^{f}\_{U})^{-1}B^{f}\_{t}\mathds{1}\_{\{t>U\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | It(3)\displaystyle I^{(3)}\_{t} | =At,Tc,f​B^T​(t,rtf)​Γt(3)​(T),\displaystyle=A^{c,f}\_{t,T}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(3)}\_{t}(T), |  |

where Γt(1)′​(U,T),Γt(2)​(U)\Gamma^{(1)^{\prime}}\_{t}(U,T),\Gamma^{(2)}\_{t}(U) and Γt(3)​(T)\Gamma^{(3)}\_{t}(T) are deterministic.
Hence, also using Remark [3.1](#S3.Thmrem1 "Remark 3.1. ‣ 3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​It(1)≃\displaystyle\mathop{}\!dI^{(1)}\_{t}\simeq\; | At,Tc,f​B^T​(t,rtf)​Γt(1)′​(U,T)​δ​d​Ftd​(U,T)+It(1)​σ^T​(t)​d​Zt2,\displaystyle A^{c,f}\_{t,T}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)^{\prime}}\_{t}(U,T)\,\delta\,\mathop{}\!dF^{d}\_{t}(U,T)\;+\;I^{(1)}\_{t}\,\widehat{\sigma}\_{T}(t)\,\mathop{}\!dZ^{2}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​It(2)≃\displaystyle\mathop{}\!dI^{(2)}\_{t}\simeq\; | 𝟏{t≤U}​It(2)​σ^U​(t)​d​Zt2,d​It(3)≃It(3)​σ^T​(t)​d​Zt2,\displaystyle\mathbf{1}\_{\{t\leq U\}}\,I^{(2)}\_{t}\,\widehat{\sigma}\_{U}(t)\,\mathop{}\!dZ^{2}\_{t},\qquad\mathop{}\!dI^{(3)}\_{t}\simeq\;I^{(3)}\_{t}\,\widehat{\sigma}\_{T}(t)\,\mathop{}\!dZ^{2}\_{t}, |  |

where we used d​B^T​(t,rtf)≃B^T​(t,rtf)​σ^T​(t)​d​Zt2\mathop{}\!d\widehat{B}\_{T}(t,r^{f}\_{t})\simeq\widehat{B}\_{T}(t,r^{f}\_{t})\widehat{\sigma}\_{T}(t)\,\mathop{}\!dZ^{2}\_{t} and the fact that I(2)I^{(2)} is of finite variation on [U,T][U,T].

On the one hand, for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐃𝐒tc,γ,κ​(U,T)≃\displaystyle\mathop{}\!d{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T)\simeq\; | At,Tc,f​B^T​(t,rtf)​Γt(1)′​(U,T)​δ​d​Ftd​(U,T)\displaystyle A^{c,f}\_{t,T}\,\widehat{B}\_{T}(t,r^{f}\_{t})\,\Gamma^{(1)^{\prime}}\_{t}(U,T)\,\delta\,\mathop{}\!dF^{d}\_{t}(U,T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(σ^T​(t)​(It(1)−(1−γ+δ​κ)​It(3))−γ​ 1{t≤U}​σ^U​(t)​It(2))​d​Zt2.\displaystyle\quad+\Big(\widehat{\sigma}\_{T}(t)(I^{(1)}\_{t}-(1-\gamma+\delta\kappa)I^{(3)}\_{t})-\gamma\,\mathbf{1}\_{\{t\leq U\}}\widehat{\sigma}\_{U}(t)\,I^{(2)}\_{t}\Big)\,\mathop{}\!dZ^{2}\_{t}. |  |

Since the dependence on Fd​(U,T)F^{d}(U,T) enters only through the term I(1)I^{(1)}, the martingale part of d​𝐃𝐒tc,γ,κ\mathop{}\!d{\rm\bf DS}^{c,\gamma,\kappa}\_{t} generated by d​Ftd​(U,T)\mathop{}\!dF^{d}\_{t}(U,T) yields ([5.1](#S5.E1 "In Proposition 5.1. ‣ 5.1 Hedging under full foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")).

On the other hand, by Remark [3.3](#S3.Thmrem3 "Remark 3.3. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), d​Ftf,q​(U,T)=νtf,q​d​Zt2\mathop{}\!dF^{f,q}\_{t}(U,T)=\nu^{f,q}\_{t}\,\mathop{}\!dZ^{2}\_{t} and thus the term d​Zt2\mathop{}\!dZ^{2}\_{t} can be represented in traded form as
φtf​d​Ftf,q​(U,T)\varphi^{f}\_{t}\,\mathop{}\!dF^{f,q}\_{t}(U,T) provided that

|  |  |  |
| --- | --- | --- |
|  | φtf=1νtf,q​(σ^T​(t)​𝐃𝐒tc,γ,κ​(U,T)+γ​(σ^T​(t)−𝟏{t≤U}​σ^U​(t))​It(2)),\varphi^{f}\_{t}=\frac{1}{\nu^{f,q}\_{t}}\Big(\widehat{\sigma}\_{T}(t)\,{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T)+\gamma(\widehat{\sigma}\_{T}(t)-\mathbf{1}\_{\{t\leq U\}}\,\widehat{\sigma}\_{U}(t))\,I\_{t}^{(2)}\Big), |  |

which is ([5.2](#S5.E2 "In Proposition 5.1. ‣ 5.1 Hedging under full foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")). Hence, the local martingale part of
d​𝐃𝐒tc,γ,κ​(U,T)\mathop{}\!d{\rm\bf DS}^{c,\gamma,\kappa}\_{t}(U,T) coincides with that of the gains term in ([5.3](#S5.E3 "In Proof. ‣ 5.1 Hedging under full foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")).
Since V0​(φ,C)=𝐃𝐒0c,γ,κ​(U,T)V\_{0}(\varphi,C)={\rm\bf DS}^{c,\gamma,\kappa}\_{0}(U,T), the strategy replicates the swap price process.
∎

### 5.2 Hedging under proportional foreign collateralisation

We now consider the single-period SOFR/€STR swap over [U,T][U,T] under proportional foreign collateralisation at a constant level β\beta (as in Section [4.3](#S4.SS3 "4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")).

###### Proposition 5.2.

For a fixed β\beta, consider the single-period SOFR/€STR swap with terminal payoff
𝐃𝐒Tγ,κ​(U,T){\rm\bf DS}^{\gamma,\kappa}\_{T}(U,T) and proportional foreign collateralisation at a constant level β\beta.
Its arbitrage-free price process 𝐃𝐒β,γ,κ​(U,T){\rm\bf DS}^{\beta,\gamma,\kappa}(U,T) can be replicated by a self-financing collateralised futures strategy
(φ,C)=(φ0,φd,φf)(\varphi,C)=(\varphi^{0},\varphi^{d},\varphi^{f}) with C=−β​VC=-\beta V where, for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | φt0=(1−β)​𝐃𝐒tβ,γ,κ​(U,T)Bth\varphi^{0}\_{t}=\frac{(1-\beta)\,{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T)}{B^{h}\_{t}} |  | (5.4) |

and the futures hedge ratios given below.

(i) Domestic futures position.
Let I(1),I(2),I(3)I^{(1)},I^{(2)},I^{(3)} be as in Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"). Then, for every t∈[0,U]t\in[0,U],

|  |  |  |
| --- | --- | --- |
|  | φtd=(σU​(t)−β​σT​(t))​It(1)−γ​(1−β)​σT​(t)​It(2)−(1−γ+δ​κ)​(1−β)​σT​(t)​It(3)νtd,\varphi^{d}\_{t}=\frac{(\sigma\_{U}(t)-\beta\sigma\_{T}(t))\,I^{(1)}\_{t}-\gamma(1-\beta)\sigma\_{T}(t)\,I^{(2)}\_{t}-(1-\gamma+\delta\kappa)(1-\beta)\sigma\_{T}(t)\,I^{(3)}\_{t}}{\nu^{d}\_{t}}, |  |

where νd\nu^{d} is the diffusion coefficient of Fd​(U,T)F^{d}(U,T) (Remark [3.2](#S3.Thmrem2 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps")) and,
for every t∈[U,T]t\in[U,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | φtd\displaystyle\varphi^{d}\_{t} | =−β​σT​(t)​It(1)−γ​(1−β)​σT​(t)​It(2)−(1−γ+δ​κ)​(1−β)​σT​(t)​It(3)νtd\displaystyle=\frac{-\beta\sigma\_{T}(t)\,I^{(1)}\_{t}-\gamma(1-\beta)\sigma\_{T}(t)\,I^{(2)}\_{t}-(1-\gamma+\delta\kappa)(1-\beta)\sigma\_{T}(t)\,I^{(3)}\_{t}}{\nu^{d}\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =δ​(β​It(1)+(1−β)​(γ​It(2)+(1−γ+δ​κ)​It(3)))1+δ​Ftd​(U,T).\displaystyle=\frac{\delta\big(\beta I^{(1)}\_{t}+(1-\beta)\big(\gamma I^{(2)}\_{t}+(1-\gamma+\delta\kappa)I^{(3)}\_{t}\big)\big)}{1+\delta\,F^{d}\_{t}(U,T)}. |  |

(ii) Foreign futures position.
For every t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | φtf=1νtf,q​(β​σ^T​(t)​𝐃𝐒tβ,γ,κ​(U,T)+γ​(σ^T​(t)−𝟏{t≤U}​σ^U​(t))​It(2)),\varphi^{f}\_{t}=\frac{1}{\nu^{f,q}\_{t}}\Big(\beta\,\widehat{\sigma}\_{T}(t)\,{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T)+\gamma\big(\widehat{\sigma}\_{T}(t)-\mathbf{1}\_{\{t\leq U\}}\widehat{\sigma}\_{U}(t)\big)\,I^{(2)}\_{t}\Big), |  |

where νtf,q:=Qt​νtf\nu^{f,q}\_{t}:=Q\_{t}\nu^{f}\_{t} is the diffusion coefficient of Ff,q​(U,T)F^{f,q}(U,T)
(see Remark [3.3](#S3.Thmrem3 "Remark 3.3. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps")).

###### Proof.

Under proportional collateralisation, the wealth of any self-financing strategy satisfies

|  |  |  |
| --- | --- | --- |
|  | d​Vt​(φ,C)=rtβ​Vt​(φ,C)​d​t+φtd​d​Ftd​(U,T)+φtf​d​Ftf,q​(U,T),\mathop{}\!dV\_{t}(\varphi,C)=r^{\beta}\_{t}\,V\_{t}(\varphi,C)\,\mathop{}\!dt+\varphi^{d}\_{t}\,\mathop{}\!dF^{d}\_{t}(U,T)+\varphi^{f}\_{t}\,\mathop{}\!dF^{f,q}\_{t}(U,T), |  |

see Proposition [2.1](#S2.Thmpro1 "Proposition 2.1. ‣ 2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"). For the replicating strategy, it suffices to match the local martingale parts in the Itô decompositions. From Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"),

|  |  |  |
| --- | --- | --- |
|  | 𝐃𝐒tβ,γ,κ​(U,T)=It(1)−γ​It(2)−(1−γ+δ​κ)​It(3),{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T)=I^{(1)}\_{t}-\gamma I^{(2)}\_{t}-(1-\gamma+\delta\kappa)\,I^{(3)}\_{t}, |  |

and all correction factors appearing in I(1),I(2),I(3)I^{(1)},I^{(2)},I^{(3)} are deterministic functions of tt.
We compute below the martingale parts using Itô’s formula and the auxiliary dynamics in Remark [3.1](#S3.Thmrem1 "Remark 3.1. ‣ 3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").

Step 1. We start by examining the diffusion terms in the dynamics of I(1),I(2)I^{(1)},I^{(2)} and I(3)I^{(3)}. First, for I(1)I^{(1)}, Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") yields a factor BU​(t,rtd)B\_{U}(t,r^{d}\_{t}) when t≤Ut\leq U,
and a finite-variation process (BUd)−1​Btd(B^{d}\_{U})^{-1}B^{d}\_{t} when t>Ut>U. This can be expressed as

|  |  |  |
| --- | --- | --- |
|  | d​BU​(t,rtd)≃𝟏{t≤U}​BU​(t,rtd)​σU​(t)​d​Zt1,\mathop{}\!dB\_{U}(t,r^{d}\_{t})\simeq\mathbf{1}\_{\{t\leq U\}}\,B\_{U}(t,r^{d}\_{t})\,\sigma\_{U}(t)\,\mathop{}\!dZ^{1}\_{t}, |  |

together with d​BT​(t,rtd)≃BT​(t,rtd)​σT​(t)​d​Zt1\mathop{}\!dB\_{T}(t,r^{d}\_{t})\simeq B\_{T}(t,r^{d}\_{t})\sigma\_{T}(t)\,\mathop{}\!dZ^{1}\_{t} and
d​B^T​(t,rtf)≃B^T​(t,rtf)​σ^T​(t)​d​Zt2\mathop{}\!d\widehat{B}\_{T}(t,r^{f}\_{t})\simeq\widehat{B}\_{T}(t,r^{f}\_{t})\widehat{\sigma}\_{T}(t)\,\mathop{}\!dZ^{2}\_{t}. Consequently,
for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | t∈[0,T].d​It(1)≃It(1)​((𝟏{t≤U}​σU​(t)−β​σT​(t))​d​Zt1+β​σ^T​(t)​d​Zt2).\qquad t\in[0,T].\mathop{}\!dI^{(1)}\_{t}\simeq I^{(1)}\_{t}\Big(\big(\mathbf{1}\_{\{t\leq U\}}\sigma\_{U}(t)-\beta\sigma\_{T}(t)\big)\mathop{}\!dZ^{1}\_{t}+\beta\widehat{\sigma}\_{T}(t)\,\mathop{}\!dZ^{2}\_{t}\Big). |  | (5.5) |

Next, for I(2)I^{(2)}, Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") contains a factor B^U​(t,rtf)\widehat{B}\_{U}(t,r^{f}\_{t}) when t≤Ut\leq U and

|  |  |  |
| --- | --- | --- |
|  | d​B^U​(t,rtf)≃𝟏{t≤U}​B^U​(t,rtf)​σ^U​(t)​d​Zt2.\mathop{}\!d\widehat{B}\_{U}(t,r^{f}\_{t})\simeq\mathbf{1}\_{\{t\leq U\}}\,\widehat{B}\_{U}(t,r^{f}\_{t})\,\widehat{\sigma}\_{U}(t)\,\mathop{}\!dZ^{2}\_{t}. |  |

Combining this with the diffusion terms of BT​(t,rtd)B\_{T}(t,r^{d}\_{t}) and B^T​(t,rtf)\widehat{B}\_{T}(t,r^{f}\_{t}) gives, for every t∈[0,T]t\in[0,T].

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​It(2)≃It(2)​((1−β)​σT​(t)​d​Zt1+(𝟏{t≤U}​σ^U​(t)+(β−1)​σ^T​(t))​d​Zt2).\mathop{}\!dI^{(2)}\_{t}\simeq I^{(2)}\_{t}\Big((1-\beta)\sigma\_{T}(t)\,\mathop{}\!dZ^{1}\_{t}+\big(\mathbf{1}\_{\{t\leq U\}}\widehat{\sigma}\_{U}(t)+(\beta-1)\widehat{\sigma}\_{T}(t)\big)\mathop{}\!dZ^{2}\_{t}\Big). |  | (5.6) |

It remains to study the term I(3)I^{(3)}.
From Proposition [4.3](#S4.Thmpro3 "Proposition 4.3. ‣ 4.3 Pricing of swaps with proportional foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), we deduce that, for every t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | It(3)=At,Tβ,f​[BT​(t,rtd)]1−β​[B^T​(t,rtf)]β​Γt(3)​(T)I^{(3)}\_{t}=A^{\beta,f}\_{t,T}\,[B\_{T}(t,r^{d}\_{t})]^{1-\beta}\,[\widehat{B}\_{T}(t,r^{f}\_{t})]^{\beta}\,\Gamma^{(3)}\_{t}(T) |  |

and thus, using Remark [3.1](#S3.Thmrem1 "Remark 3.1. ‣ 3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​It(3)≃It(3)​((1−β)​σT​(t)​d​Zt1+β​σ^T​(t)​d​Zt2).\mathop{}\!dI^{(3)}\_{t}\simeq I^{(3)}\_{t}\Big((1-\beta)\sigma\_{T}(t)\,\mathop{}\!dZ^{1}\_{t}+\beta\widehat{\sigma}\_{T}(t)\,\mathop{}\!dZ^{2}\_{t}\Big). |  | (5.7) |

Step 2. We are now ready to identify the hedge ratios. Using ([5.5](#S5.E5 "In Proof. ‣ 5.2 Hedging under proportional foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")), ([5.6](#S5.E6 "In Proof. ‣ 5.2 Hedging under proportional foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")) and ([5.7](#S5.E7 "In Proof. ‣ 5.2 Hedging under proportional foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐃𝐒tβ,γ,κ​(U,T)≃\displaystyle\mathop{}\!d{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T)\simeq\; | ((𝟏{t≤U}​σU​(t)−β​σT​(t))​It(1)−γ​(1−β)​σT​(t)​It(2)−(1−γ+δ​κ)​(1−β)​σT​(t)​It(3))​d​Zt1\displaystyle\Big(\big(\mathbf{1}\_{\{t\leq U\}}\sigma\_{U}(t)-\beta\sigma\_{T}(t)\big)I^{(1)}\_{t}-\gamma(1-\beta)\sigma\_{T}(t)I^{(2)}\_{t}-(1-\gamma+\delta\kappa)(1-\beta)\sigma\_{T}(t)I^{(3)}\_{t}\Big)\mathop{}\!dZ^{1}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(β​σ^T​(t)​It(1)−γ​(𝟏{t≤U}​σ^U​(t)+(β−1)​σ^T​(t))​It(2)−(1−γ+δ​κ)​β​σ^T​(t)​It(3))​d​Zt2.\displaystyle\quad+\Big(\beta\widehat{\sigma}\_{T}(t)I^{(1)}\_{t}-\gamma\big(\mathbf{1}\_{\{t\leq U\}}\widehat{\sigma}\_{U}(t)+(\beta-1)\widehat{\sigma}\_{T}(t)\big)I^{(2)}\_{t}-(1-\gamma+\delta\kappa)\beta\widehat{\sigma}\_{T}(t)I^{(3)}\_{t}\Big)\mathop{}\!dZ^{2}\_{t}. |  |

The d​Zt2\mathop{}\!dZ^{2}\_{t}-coefficient simplifies in terms of 𝐃𝐒tβ,γ,κ​(U,T){\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T) and It(2)I^{(2)}\_{t} as follows

|  |  |  |
| --- | --- | --- |
|  | β​σ^T​(t)​It(1)−γ​(𝟏{t≤U}​σ^U​(t)+(β−1)​σ^T​(t))​It(2)−(1−γ+δ​κ)​β​σ^T​(t)​It(3)\displaystyle\beta\widehat{\sigma}\_{T}(t)I^{(1)}\_{t}-\gamma\big(\mathbf{1}\_{\{t\leq U\}}\widehat{\sigma}\_{U}(t)+(\beta-1)\widehat{\sigma}\_{T}(t)\big)I^{(2)}\_{t}-(1-\gamma+\delta\kappa)\beta\widehat{\sigma}\_{T}(t)I^{(3)}\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =β​σ^T​(t)​(It(1)−γ​It(2)−(1−γ+δ​κ)​It(3))+γ​(σ^T​(t)−𝟏{t≤U}​σ^U​(t))​It(2)\displaystyle=\beta\widehat{\sigma}\_{T}(t)\big(I^{(1)}\_{t}-\gamma I^{(2)}\_{t}-(1-\gamma+\delta\kappa)I^{(3)}\_{t}\big)+\gamma\big(\widehat{\sigma}\_{T}(t)-\mathbf{1}\_{\{t\leq U\}}\widehat{\sigma}\_{U}(t)\big)I^{(2)}\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =β​σ^T​(t)​𝐃𝐒tβ,γ,κ​(U,T)+γ​(σ^T​(t)−𝟏{t≤U}​σ^U​(t))​It(2).\displaystyle=\beta\widehat{\sigma}\_{T}(t)\,{\rm\bf DS}^{\beta,\gamma,\kappa}\_{t}(U,T)+\gamma\big(\widehat{\sigma}\_{T}(t)-\mathbf{1}\_{\{t\leq U\}}\widehat{\sigma}\_{U}(t)\big)I^{(2)}\_{t}. |  |

Furthermore, by Remarks [3.2](#S3.Thmrem2 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps") and [3.3](#S3.Thmrem3 "Remark 3.3. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"),
d​Ftd=νtd​d​Zt1\mathop{}\!dF^{d}\_{t}=\nu^{d}\_{t}\,\mathop{}\!dZ^{1}\_{t}
and
d​Ftf,q=νtf,q​d​Zt2.\mathop{}\!dF^{f,q}\_{t}=\nu^{f,q}\_{t}\,\mathop{}\!dZ^{2}\_{t}.
Matching diffusion coefficients yields the asserted expressions for hedge ratios. Finally, equality ([5.4](#S5.E4 "In Proposition 5.2. ‣ 5.2 Hedging under proportional foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")) follows from (1−β)​Vt​(φ,C)=φt0​Bth(1-\beta)V\_{t}(\varphi,C)=\varphi^{0}\_{t}B^{h}\_{t} with
V​(φ,C)=𝐃𝐒β,γ,κ​(U,T)V(\varphi,C)={\rm\bf DS}^{\beta,\gamma,\kappa}(U,T).
∎

To summarise, the hedging results obtained in this section confirm that the collateral currency affects not only the level
of prices but also the *risk decomposition* of the contract: once collateral is posted in
a foreign currency, the swap value acquires an additional stochastic exposure carried by the foreign discounting component.
In our Gaussian specification with deterministic volatilities, all convexity corrections remain deterministic and thus do not
generate new hedgeable risk factors. Instead, they rescale the sensitivities to the traded futures. As a consequence,
replication reduces to identifying explicit hedge ratios, while the cash account is absent in the fully collateralised benchmark.

The hedging identities above make transparent how collateral currency selection reshapes risk decomposition.
When γ=0\gamma=0, we recover the hedging of a standard single-period SOFR swap under proportional foreign collateralisation.
When γ≠0\gamma\neq 0, the hedge contains an additional foreign rate component associated with the €STR leg, so the strategy resembles a quanto/differential swap hedge in the sense that both domestic and foreign rate risks must be dynamically managed, even though the contract is settled in the domestic currency.

## 6 Numerical Results

The pricing and hedging results in Sections [4.2](#S4.SS2 "4.2 Pricing of swaps with full foreign collateralisation ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps")–[5.2](#S5.SS2 "5.2 Hedging under proportional foreign collateralisation ‣ 5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") apply to a class of single-period payoffs of the form
δ​(Rd​(U,T)−γ​Rf​(U,T)−κ)\delta\big(R^{d}(U,T)-\gamma R^{f}(U,T)-\kappa\big), which includes differential (quanto-type) specifications when γ≠0\gamma\neq 0.
In that case, the foreign factor enters the valuation and hedging problem through two distinct channels: the foreign-currency collateralisation convention and the foreign floating leg of the payoff.
To disentangle the incremental risk attributable *solely* to the choice of collateral currency, we set γ=0\gamma=0 throughout this section.
Hence, the underlying payoff is purely domestic, and any departure from the domestic benchmark in either valuation or hedge ratios can be attributed to the collateral currency and the collateralisation level β\beta.

With γ=0\gamma=0, the experiment can be viewed more generally as studying a domestic USD payoff under *non-domestic collateralisation*. That is, the pricing and hedging results can be interpreted more generally as pertaining to *non-domestic collateralisation*. In the numerical experiments we take EUR as a representative non-domestic collateral currency, but the same formulae apply to any collateral currency once rcr^{c} and the corresponding exchange-traded overnight futures (e.g. TONA for JPY collateral, SONIA for GBP collateral) are introduced in place of €STR.

The goal of this section is to quantify the economic impact of collateral currency choice on the valuation and hedging of single- and multi-period SOFR swaps (corresponding to γ=0\gamma=0) under the Gaussian specification of Section [3](#S3 "3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").
We first report pricing effects in terms of par swap rates and selected parameter sensitivities.
We then assess hedge performance when the continuous-time replication strategies derived in Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") are implemented on a discrete rebalancing grid.

Within this design, the key message is transparent: even when contractual cashflows are domestic, foreign collateralisation can affect both *valuation* through the effective discounting rate and the *risk decomposition* through an additional hedge requirement in foreign futures. Accordingly, we consider two collateral conventions.
In the first, the collateral currency and the proportionality level β\beta are fixed at inception and remain constant throughout the contract life.
In the second, we adopt a cheapest-to-deliver interpretation of a multi-currency CSA, whereby an admissible collateral currency is selected at time 0 and then kept fixed.
This comparison clarifies when collateral optionality manifests itself primarily as an up-front pricing effect and when it generates persistent differences in hedge composition and hedge effectiveness.

### 6.1 Setup and validation of theoretical pricing

We consider SOFR swaps with semi-annual payment dates 0=T0<T1<⋯<Tn=T0=T\_{0}<T\_{1}<\cdots<T\_{n}=T and accrual factors
δj:=Tj−Tj−1=0.5\delta\_{j}:=T\_{j}-T\_{j-1}=0.5. The jjth floating coupon is δj​Rd​(Tj−1,Tj)\delta\_{j}R^{d}(T\_{j-1},T\_{j}) and the fixed coupon is δj​κ\delta\_{j}\kappa,
both settled in arrears at TjT\_{j}. The valuation of the multi-period swap is governed by
[Proposition 4.4](#S4.Thmpro4 "Proposition 4.4. ‣ 4.4 Extension to multi-period differential swaps ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"), and the par swap rate, denoted by κt⋆​(T,β)\kappa^{\star}\_{t}(T,\beta), is computed explicitly via
[Corollary 4.1](#S4.Thmcor1 "Corollary 4.1. ‣ 4.4 Extension to multi-period differential swaps ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") by substituting γ=0\gamma=0, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | κt⋆​(T;β):=κt⋆​(T0,n;β,0)=∑j=1n(Ij(1)​(t)−Ij(3)​(t))∑j=1nδj​Ij(3)​(t).\kappa^{\star}\_{t}(T;\beta):=\kappa^{\star}\_{t}(T\_{0},n;\beta,0)=\frac{\sum\_{j=1}^{n}\big(I^{(1)}\_{j}(t)-I^{(3)}\_{j}(t)\big)}{\sum\_{j=1}^{n}\delta\_{j}\,I^{(3)}\_{j}(t)}. |  | (6.1) |

In the numerical study, we work at inception (t=0t=0) and report κ0⋆​(T;β)\kappa^{\star}\_{0}(T;\beta) for maturities
T∈{1,2,3,5,7,10}T\in\{1,2,3,5,7,10\} years. All numerical results are generated under the domestic pricing martingale measure ℚ\mathbb{Q}
using the joint dynamics postulated in [Assumption 3.1](#S3.Thmhyp1 "Assumption 3.1. ‣ 3.1 Cross-currency model specification ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").

The complete set of baseline parameters, including (ρ12,ρ13,ρ23)(\rho\_{12},\rho\_{13},\rho\_{23}) and the initial values
(r0d,r0f,Q0)(r^{d}\_{0},r^{f}\_{0},Q\_{0}), is reported in [Table 1](#S6.T1 "Table 1 ‣ 6.1 Setup and validation of theoretical pricing ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") and
used throughout this section. The parameters are
*synthetic* rather than the result of a formal calibration: the initial levels (r0d,r0f,Q0)(r^{d}\_{0},r^{f}\_{0},Q\_{0}) are chosen to be
broadly representative of the prevailing USD and EUR overnight rates and the spot FX level, while the remaining parameters are set
to produce a stable benchmark.

Table 1: Baseline parameters.

| Domestic (USD) | | Foreign (EUR) | | FX/Collateral/Discretisation | |
| --- | --- | --- | --- | --- | --- |
| parameter | value | parameter | value | parameter | value |
| aa | 0.1101 | c^\widehat{c} | 0.05799 | σ¯\bar{\sigma} | 0.075 |
| bb | 3 | b^\widehat{b} | 3 | Q0Q\_{0} | 1.178 |
| σ\sigma | 0.012 | σ^\widehat{\sigma} | 0.01 | αc,f\alpha^{c,f} | 0.002 |
| r0dr^{d}\_{0} | 0.0367 | r0fr^{f}\_{0} | 0.01933 | Δ​t\Delta t | 1/2521/252 |
| Correlations | | | | (ρ12,ρ13,ρ23)(\rho\_{12},\rho\_{13},\rho\_{23}) | (0.25,−0.25,0.10)(0.25,-0.25,0.10) |

We work with proportional foreign collateralisation, i.e., with collateral posted in EUR and remunerated at rc=rf+αc,fr^{c}=r^{f}+\alpha^{c,f}.
As in Section [2](#S2 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"), the effective discount rate is rβ=(1−β)​rh+β​rcr^{\beta}=(1-\beta)r^{h}+\beta r^{c}. In the
numerical baseline, we set rh=rdr^{h}=r^{d} (equivalently, αh≡0\alpha^{h}\equiv 0), so that
rβ=(1−β)​rd+β​rcr^{\beta}=(1-\beta)r^{d}+\beta r^{c}.
Recall that the benchmark case of β=0\beta=0 corresponds to the domestic funding case, while β=1\beta=1 corresponds to full foreign
collateralisation. Intermediate values β∈(0,1)\beta\in(0,1) provide a parsimonious proxy for a partial foreign
collateralisation. In all pricing experiments reported below, β\beta is kept constant over the lifetime of the swap.

The core pricing objects, κ0⋆​(T;β)\kappa^{\star}\_{0}(T;\beta), are computed
using closed-form solutions of [Proposition 4.4](#S4.Thmpro4 "Proposition 4.4. ‣ 4.4 Extension to multi-period differential swaps ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") combined with ([6.1](#S6.E1 "In 6.1 Setup and validation of theoretical pricing ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps")) and the Monte Carlo (MC) method is used only as a validation tool. For this purpose, the Gaussian factors
are simulated on a daily grid Δ​t=1/252\Delta t=1/252 to verify that the estimated swap’s value at the closed-form par rate is statistically
consistent with its theoretical null value.

We validate the implementation at two levels. First, for single-period swaps, we compare the closed-form price to the MC
estimate across a grid of accrual intervals (U,T)(U,T) and collateralisation levels β∈{0,0.5,1}\beta\in\{0,0.5,1\}. Second, for multi-period
swaps with semi-annual payment dates, we compute the theoretical par rate κ0⋆​(T;β)\kappa^{\star}\_{0}(T;\beta) and verify that the MC estimate of the swap’s value at κ=κ0⋆​(T;β)\kappa=\kappa^{\star}\_{0}(T;\beta) is
statistically close to 0. In each row of [Table 2](#S6.T2 "Table 2 ‣ 6.1 Setup and validation of theoretical pricing ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps"),
PV closed-form denotes the theoretical initial price, while PV MC is the
Monte Carlo estimate with associated standard errors of the discounted payoff sample reported in the last column. For
single-period swaps, (U,T)(U,T) denotes the accrual
interval, for multi-period swaps, we report T0=0T\_{0}=0 and TT as the final maturity so the intermediate payment dates are
implicit in the semi-annual schedule. [Table 2](#S6.T2 "Table 2 ‣ 6.1 Setup and validation of theoretical pricing ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") shows that the MC deviations are of the same order as the MC
standard error.

Table 2: Monte Carlo validation of theoretical values.

| Product type | UU | TT | β\beta | κ0⋆​(T;β)\kappa^{\star}\_{0}(T;\beta) (%) | PV closed-form | PV MC | MC stderr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Single-period swap | 0.00 | 0.50 | 0.00 | 3.7000 | 1.110e-16 | 4.506e-05 | 2.127e-05 |
| Single-period swap | 0.50 | 1.00 | 0.50 | 3.6984 | 0.000e+00 | 4.146e-05 | 2.768e-05 |
| Single-period swap | 2.50 | 3.00 | 1.00 | 3.7040 | 0.000e+00 | 5.420e-05 | 2.615e-05 |
| Multi-period swap | — | 3.00 | 0.50 | 3.6928 | -1.110e-16 | 4.265e-04 | 8.603e-05 |
| Multi-period swap | — | 5.00 | 1.00 | 3.7040 | 3.331e-16 | 1.834e-04 | 1.153e-04 |

### 6.2 Collateral currency effects: par rates and sensitivities

We now turn to the main pricing implications. Throughout this subsection, the collateral specification is fixed for the life of
the swap. For each β∈[0,1]\beta\in[0,1], we compute the initial par swap rate κ0⋆​(T;β)\kappa^{\star}\_{0}(T;\beta) and address the following questions:
(i) how the par curve shifts with β\beta across maturities and (ii) which model parameters most strongly control the adjustment induced by foreign collateralisation.
[Figure 1](#S6.F1 "Figure 1 ‣ 6.2 Collateral currency effects: par rates and sensitivities ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") plots the closed-form par swap rate κ0⋆​(T;β)\kappa^{\star}\_{0}(T;\beta) across maturities for
β∈{0,0.25,0.5,0.75,1}\beta\in\{0,0.25,0.5,0.75,1\}. In the baseline parameter set, the term
structure of the par rate is decreasing in maturity, and
increasing β\beta shifts the par curve upward. This ordering is economically intuitive when interpreted through the level
difference between the domestic and foreign overnight rates. Under Vasicek’s specification, the long-term means are
θd=a/b\theta\_{d}=a/b and θf=c^/b^\theta\_{f}=\widehat{c}/\widehat{b}, and in the baseline we have θf<θd\theta\_{f}<\theta\_{d}. Thus, moving from β=0\beta=0
(no collateralisation) toward β=1\beta=1 (full foreign collateralisation) replaces discounting primarily at the higher domestic rate by discounting primarily at the lower foreign collateral rate, which in turn increases the present value of swap cash flows
under the foreign collateralisation. Since the par fixed rate is the unique κ\kappa that sets the swap value to zero, the
par curve shifts upward.

![Refer to caption](2603.07863v1/x1.png)


Figure 1: Closed-form par swap rate κ0⋆​(T;β)\kappa^{\star}\_{0}(T;\beta) for maturities T∈{1,2,3,5,7,10}T\in\{1,2,3,5,7,10\} and collateralisation levels
β∈{0,0.25,0.5,0.75,1}\beta\in\{0,0.25,0.5,0.75,1\}.

To isolate the collateralisation effect, we report the par-rate difference

|  |  |  |
| --- | --- | --- |
|  | Δ​κ0⋆​(T;β):=κ0⋆​(T;β)−κ0⋆​(T;0)\Delta\kappa^{\star}\_{0}(T;\beta):=\kappa^{\star}\_{0}(T;\beta)-\kappa^{\star}\_{0}(T;0) |  |

in basis points. [Table 3](#S6.T3 "Table 3 ‣ 6.2 Collateral currency effects: par rates and sensitivities ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") indicates that the adjustment is relatively small for short maturities but becomes
economically meaningful for longer maturities, reaching several basis points at T=10T=10Y for swaps with full foreign collateralisation.
This maturity dependence is consistent with the structure of theoretical expressions: the collateralisation adjustment
accumulates over time through the exponential discount factors and deterministic correction terms, and hence its impact on the
par rate grows with the horizon over which cash flows are collateral-adjusted.

Table 3: Par-rate differences Δ​κ0⋆​(T;β)\Delta\kappa^{\star}\_{0}(T;\beta) (bp) across maturities and collateralisation levels.

| Maturity TT | β=0.25\beta=0.25 | β=0.50\beta=0.50 | β=0.75\beta=0.75 | β=1.00\beta=1.00 |
| --- | --- | --- | --- | --- |
| 1 | 0.19 | 0.38 | 0.57 | 0.76 |
| 2 | 0.37 | 0.75 | 1.12 | 1.50 |
| 3 | 0.55 | 1.11 | 1.67 | 2.23 |
| 5 | 0.91 | 1.83 | 2.75 | 3.68 |
| 7 | 1.26 | 2.52 | 3.80 | 5.09 |
| 10 | 1.75 | 3.52 | 5.32 | 7.15 |

Next, we examine which parameters primarily drive the collateralisation-induced adjustment. For T=5T=5Y we consider
Δ​κ0⋆​(5​Y;1)=κ0⋆​(5​Y;1)−κ0⋆​(5​Y;0)\Delta\kappa^{\star}\_{0}(5\mathrm{Y};1)=\kappa^{\star}\_{0}(5\mathrm{Y};1)-\kappa^{\star}\_{0}(5\mathrm{Y};0) and perform an OAT
±10%\pm 10\% perturbation analysis. [Figure 2](#S6.F2 "Figure 2 ‣ 6.2 Collateral currency effects: par rates and sensitivities ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") reports the resulting tornado diagram. In the set of baseline parameters,
the dominant drivers are the FX volatility σ¯\bar{\sigma} and the domestic–FX correlation ρ13\rho\_{13}, followed by the volatility σ\sigma of the domestic short rate. This pattern reflects the fact that, under [Assumption 3.1](#S3.Thmhyp1 "Assumption 3.1. ‣ 3.1 Cross-currency model specification ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"), the foreign-collateralised
discounting rule interacts with the joint Gaussian dependence of (rd,rf,Q)(r^{d},r^{f},Q) through the deterministic correction factors.
In particular, a higher FX volatility amplifies the magnitude of these corrections,
while the sign and magnitude of ρ13\rho\_{13} determine whether FX shocks tend to co-move with domestic rate shocks in a way that
increases or decreases the collateralisation-induced par swap rate shift.

![Refer to caption](2603.07863v1/x2.png)


Figure 2: OAT ±10%\pm 10\% sensitivity of Δ​κ0⋆​(5​Y;1)\Delta\kappa^{\star}\_{0}(5\mathrm{Y};1) (bp).

### 6.3 Cheapest-to-deliver collateral under currency choice

In the next step, we adopt the classical interpretation of a multi-currency CSA with an admissible set of collateral currencies 𝒞\mathcal{C}, in which the collateral currency is selected at time 0 and then kept fixed for the life of the trade. For the purposes of illustration, it is sufficient to take 𝒞={USD,EUR}\mathcal{C}=\{\mathrm{USD},\mathrm{EUR}\},
and compare the corresponding fixed-collateral par swap rates. Recall from Section [2.3](#S2.SS3 "2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"), in the EUR-collateralised case we have rc=rf+αc,fr^{c}=r^{f}+\alpha^{c,f}, whereas in the USD-collateralised case we write rc=rd+αc,dr^{c}=r^{d}+\alpha^{c,d}. In the numerical experiments of this subsection, we specialise to the case αc,d=0\alpha^{c,d}=0. Hence full USD collateralisation coincides with the benchmark case β=0\beta=0, whereas the EUR collateral corresponds to the full foreign collateralisation, that is, β=1\beta=1. Therefore, the embedded collateral choice effect is fully captured by comparing the two par curves κ0⋆​(T;0)\kappa\_{0}^{\star}(T;0) and
κ0⋆​(T;1)\kappa\_{0}^{\star}(T;1).

![Refer to caption](2603.07863v1/x3.png)


Figure 3: CTD: par-rate spread κ0⋆,(EUR)​(T)−κ0⋆,(USD)​(T)\kappa^{\star,(\mathrm{EUR})}\_{0}(T)-\kappa^{\star,(\mathrm{USD})}\_{0}(T) (bp).

[Figure 3](#S6.F3 "Figure 3 ‣ 6.3 Cheapest-to-deliver collateral under currency choice ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") plots the par-rate spread κ0⋆​(T;1)−κ0⋆​(T;0)\kappa\_{0}^{\star}(T;1)-\kappa\_{0}^{\star}(T;0)
across maturities. This quantity is obtained from the two extreme curves in [Figure 1](#S6.F1 "Figure 1 ‣ 6.2 Collateral currency effects: par rates and sensitivities ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps"): the curve corresponding to full foreign collateralisation lies uniformly above the benchmark curve (β=0)(\beta=0), and the separation between the two curves widens with maturity. Under the present identification, this is precisely the spread between the EUR-collateralised and USD-collateralised par swap rates.

The CTD interpretation formalises this ordering by viewing the admissible set 𝒞={USD,EUR}\mathcal{C}=\{\mathrm{USD},\mathrm{EUR}\} as a choice between two fixed collateral specifications. The payer prefers the collateral currency associated with the lower par fixed rate, whereas the receiver prefers the one associated with the higher par fixed rate. Therefore, the embedded effect of collateral choice is naturally quantified by the difference between the corresponding par curves, and [Figure 3](#S6.F3 "Figure 3 ‣ 6.3 Cheapest-to-deliver collateral under currency choice ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") provides a direct basis-point representation of this separation.

Overall, the pricing results support three conclusions. First, proportional foreign collateralisation induces systematic and maturity-dependent shifts in SOFR par swap rates relative to the benchmark case β=0\beta=0. Second, the sensitivity analysis indicates that the magnitude of the collateralisation adjustment is primarily controlled by volatility and correlation inputs. Third, under a multi-currency CSA, the classical CTD interpretation reduces to a collateral-currency ranking of par swap rates, yielding a transparent and easily reportable measure of the embedded collateral choice effect.

### 6.4 Hedging of domestic and foreign sources of risk

We now turn to hedging implications under proportional foreign collateralisation. As in the pricing numerics, all results are
generated under the domestic pricing measure ℚ\mathbb{Q} and the Gaussian specification in [Assumption 3.1](#S3.Thmhyp1 "Assumption 3.1. ‣ 3.1 Cross-currency model specification ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"). Since the multi-period swap
settles at multiple payment dates, we evaluate hedge performance on a cum-dividend gain process. For a payer SOFR swap with payment
dates {Tj}j=1n\{T\_{j}\}\_{j=1}^{n}, recall the realised period cash flow at TjT\_{j}

|  |  |  |
| --- | --- | --- |
|  | CFj=e∫Tj−1Tjrud​𝑑u−(1+δj​κ),\textbf{CF}\_{j}=e^{\int\_{T\_{j-1}}^{T\_{j}}r^{d}\_{u}\,du}-(1+\delta\_{j}\kappa), |  |

and define the gain process by reinvesting realised cash flows at the effective rate rβr^{\beta}, for tk∈{0,Δ​t,2​Δ​t,…,T}t\_{k}\in\{0,\Delta t,2\Delta t,\dots,T\},

|  |  |  |
| --- | --- | --- |
|  | Gtk:=Vtk+∑j:Tj≤tkCFj​exp⁡(∫Tjtkruβ​𝑑u),G\_{t\_{k}}:=V\_{t\_{k}}+\sum\_{j:T\_{j}\leq t\_{k}}\textbf{CF}\_{j}\exp\!\Big(\int\_{T\_{j}}^{t\_{k}}r^{\beta}\_{u}\,du\Big), |  |

where Δ​t=1/252\Delta t=1/252. This transformation removes jumps at payment dates and yields a natural target for self-financing
replication in discrete time.

In the hedging experiments, we work with a collateralised futures strategy (φ,C)=(φ0,φd,φf)(\varphi,C)=(\varphi^{0},\varphi^{d},\varphi^{f}) in the sense of
[Definition 2.5](#S2.Thmdefi5 "Definition 2.5. ‣ 2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"). Under proportional foreign collateralisation at constant level β∈[0,1]\beta\in[0,1], the margin account is
Ct=−β​XtC\_{t}=-\beta X\_{t}, where XX denotes the value process of the hedging portfolio expressed in domestic currency (USD). Substituting
Ct=−β​XtC\_{t}=-\beta X\_{t} into the self-financing condition in [Definition 2.5](#S2.Thmdefi5 "Definition 2.5. ‣ 2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps") yields the effective drift rβ=(1−β)​rtd+β​(rtf+αc,f),r^{\beta}=(1-\beta)r^{d}\_{t}+\beta(r^{f}\_{t}+\alpha^{c,f}), and the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=rtβ​Xt​d​t+φtd​d​Ftd+φtf​d​Ftf,q,\mathop{}\!dX\_{t}=r^{\beta}\_{t}X\_{t}\,\mathop{}\!dt+\varphi^{d}\_{t}\,\mathop{}\!dF^{d}\_{t}+\varphi^{f}\_{t}\,\mathop{}\!dF^{f,q}\_{t}, |  | (6.2) |

where FdF^{d} denotes the domestic SOFR futures and Ff,qF^{f,q} is the domestic-currency representation of the foreign futures component,
defined as in ([2.2](#S2.E2 "In Definition 2.5. ‣ 2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps")).

In the numerical implementation, we rebalance on a discrete grid 0=t0<t1<⋯<tM=T0=t\_{0}<t\_{1}<\cdots<t\_{M}=T and keep
(φd,φf)(\varphi^{d},\varphi^{f}) piecewise constant on each interval (tm,tm+1](t\_{m},t\_{m+1}]. The portfolio value is evaluated on the daily grid
Δ​t=1/252\Delta t=1/252 by Euler-type discretisation of ([6.2](#S6.E2 "In 6.4 Hedging of domestic and foreign sources of risk ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps")). We set X0=G0X\_{0}=G\_{0} and report the terminal hedging
error εT:=XT−GT\varepsilon\_{T}:=X\_{T}-G\_{T}.

Our first goal is to verify whether the hedging strategies derived in Section [5](#S5 "5 Futures-Based Hedging under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps") are consistent with the closed-form pricing results of Section [4](#S4 "4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps"). It appears that,
under daily rebalancing, the wealth process of the hedging portfolio almost perfectly tracks the price process.
[Figure 4](#S6.F4 "Figure 4 ‣ 6.4 Hedging of domestic and foreign sources of risk ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps") illustrates a representative path, where GG and XX are visually indistinguishable and the pathwise
error remains at the level of numerical precision.

![Refer to caption](2603.07863v1/x4.png)


Figure 4: Gain process GG and hedging portfolio XX, together with the pathwise error X−GX-G (daily rebalancing).

To quantify the economic relevance of domestic versus foreign sources of risk, we compare three hedge sets: no hedge H0H\_{0},
domestic only hedging HdH\_{d} (i.e., using domestic futures only), and domestic and foreign hedging Hd​fH\_{df} (i.e., using domestic and foreign futures). Although
the swap payoff is purely domestic, under foreign collateralisation (β>0\beta>0) the collateral-adjusted prices depend
on (rf,Q)(r^{f},Q) through the effective funding rate rβr^{\beta}, so hedging domestic risk alone does need not eliminate all variance in terminal P&L.

We posit that the contribution of a domestic hedge can be measured by the variance ratio of the terminal hedging error εT:=XT−GT\varepsilon\_{T}:=X\_{T}-G\_{T}. To this end,
we define

|  |  |  |
| --- | --- | --- |
|  | 𝖲𝗁𝖺𝗋𝖾d:=1−Var​(εTHd)Var​(εTH0),\mathsf{Share}\_{d}:=1-\frac{\mathrm{Var}(\varepsilon\_{T}^{H\_{d}})}{\mathrm{Var}(\varepsilon\_{T}^{H\_{0}})}, |  |

that is, the fraction of unhedged terminal variance eliminated by hedging only the domestic component. In the benchmark experiment at
T=5T=5 and β=1\beta=1 under weekly rebalancing, we find
Var​(εTHd)/Var​(εTH0)≈0.05\mathrm{Var}(\varepsilon\_{T}^{H\_{d}})/\mathrm{Var}(\varepsilon\_{T}^{H\_{0}})\approx 0.05, so that the domestic hedge removes the dominant share of terminal
risk while leaving non-negligible residual component.

![Refer to caption](2603.07863v1/x5.png)


Figure 5: Normalised terminal error variance under weekly rebalancing (T=5T=5, β=1\beta=1).

In [Figure 5](#S6.F5 "Figure 5 ‣ 6.4 Hedging of domestic and foreign sources of risk ‣ 6 Numerical Results ‣ Choice of Collateral Currency in Differential Swaps"), we report the corresponding normalised variances. The residual
is not removed by domestic instruments alone: augmenting the hedge with foreign futures reduces the remaining variance to a negligible
level in this experiment. This indicates that, under foreign collateralisation, a small but structural component of terminal hedging
risk is attributable to the foreign rate risk induced by collateral-adjusted discounting.

Taken together, the numerical results confirm that the choice of collateral currency has a tangible effect on par rates and that, once
collateral is posted in a foreign currency, a hedge based solely on domestic instruments leaves a systematic residual exposure.
The next section concludes by summarising the practical implications of these findings for pricing and risk management under modern
multi-currency collateral agreements.

## 7 Conclusions

This paper studies the valuation and hedging of differential swaps when collateral is posted in a foreign currency. Under the domestic pricing measure ℚ\mathbb{Q} and a tractable Gaussian specification, we derive closed-form expressions for prices and hedging strategies of single- and multi-period differential swaps under
proportional foreign collateralisation, expressed in terms of market-observable building blocks and deterministic correction terms. The numerical study shows that the choice of a collateral currency
induces systematic and maturity-dependent shifts in par swap rates and that effect is already visible through a CTD
interpretation of a multi-currency CSA.
A practical implication is that discounting at a purely domestic hedge/funding rate rhr^{h} can entail a significant inaccuracy
even if the contract is only partially foreign collateralised. In particular, when β∈(0,1)\beta\in(0,1) is not close to zero, the effective funding rate
rβ=(1−β)​rh+β​rcr^{\beta}=(1-\beta)r^{h}+\beta r^{c} alters prices and par swap rates, so using rhr^{h} instead of rβr^{\beta} can lead to systematic bias.

On the hedging side, we propose a futures-based self-financing framework and validate its numerical implementation via verification of pathwise replication. In baseline configurations, the dominant hedgeable risk is driven by the domestic rate, and thus positions in domestic futures are capable of removing the bulk of the terminal risk exposure. However, under foreign collateralisation, a residual risk exposure persists when only domestic futures are used for hedging, but it is almost completely eliminated once foreign futures are also included. Although it is a second order effect with respect to the domestic component, the residual risk is not negligible from a risk management perspective for swaps with large notional.

Several natural extensions of this study can be envisaged. First, the same methodology can be applied to a larger set of eligible collateral
currencies and alternative CSA conventions (thresholds, haircuts, remuneration spreads). Second, incorporation of the model’s uncertainty,
transaction costs, and restrictions on hedging instruments would provide a more market-facing assessment of hedge effectiveness.
Finally, a direct model’s calibration to the term-structure and FX option data would allow a quantitative comparison of
collateral-currency premia across market regimes.

Acknowledgements.
The research of R. Liu and M. Rutkowski was supported by the Australian Research Council Discovery Project scheme under grant DP200101550 Fair pricing of superannuation guaranteed benefits under downturn risk. This work was also supported in part by the National Natural Science Foundation of China under Grant 12371447.

## References

* [1]
  T. Adrian, F. Grinberg, T. Mancini-Griffoli, R. M. Townsend, and N. Zhang (November 2022)
  A multi-currency exchange and contracting platform. International Monetary Fund, Working paper 22/217.
   International Monetary Fund.
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [2]
  L. B. G. Andersen, D. Duffie, and Y. Song (2019)
  Funding value adjustments.
  The Journal of Finance 74 (1),  pp. 145–192.
  External Links: [Document](https://dx.doi.org/10.1111/jofi.12739)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [3]
  Basel Committee on Banking Supervision and International Organization of Securities Commissions (2015-03)
  Margin requirements for non-centrally cleared derivatives.
  Technical report
   Bank for International Settlements.
  External Links: [Link](https://www.bis.org/bcbs/publ/d317.pdf)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [4]
  F. Biagini, A. Gnoatto, and I. Oliva (2021)
  A unified approach to xVA with CSA discounting and initial margin.
  SIAM Journal on Financial Mathematics 12 (3),  pp. 1013–1053.
  Cited by: [§2.3](#S2.SS3.p6.15 "2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps").
* [5]
  M. Bianchetti (2009)
  Two curves, one price: pricing and hedging interest rate derivatives decoupling forwarding and discounting yield curves.
  Note: Available at arXiv: <https://arxiv.org/abs/0905.2770>
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [6]
  M. Bickersteth, Y. Ding, and M. Rutkowski (2026)
  Pricing and hedging of SOFR derivatives.
  Mathematical Finance 36 (1),  pp. 180–202.
  External Links: [Document](https://dx.doi.org/10.1111/mafi.70004)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§2](#S2.p3.4 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps").
* [7]
  T. R. Bielecki, I. Cialenco, and M. Rutkowski (2018)
  Arbitrage-free pricing of derivatives in nonlinear market models.
  Probability, Uncertainty and Quantitative Risk 3 (1),  pp. 1229–1258.
  Cited by: [§2.3](#S2.SS3.p6.15 "2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps").
* [8]
  T. R. Bielecki and M. Rutkowski (2015)
  Valuation and hedging of contracts with funding costs and collateralization.
  SIAM Journal on Financial Mathematics 6 (1),  pp. 594–655.
  Cited by: [§2.3](#S2.SS3.p6.15 "2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps").
* [9]
  D. Brigo, M. Morini, and A. Pallavicini (2013)
  Counterparty credit risk, collateral and funding: with pricing cases for all asset classes.
   John Wiley & Sons.
  External Links: ISBN 978-0-470-74846-6
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [10]
  J. C. Cox, J. E. Ingersoll, and S. A. Ross (1981)
  The relation between forward prices and futures prices.
  Journal of Financial Economics 9 (4),  pp. 321–346.
  External Links: [Document](https://dx.doi.org/10.1016/0304-405X%2881%2990002-7)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [11]
  Y. Ding, R. Liu, and M. Rutkowski (2024)
  Multi-curve approach to cross-currency basis swaps referencing backward-looking rates.
  Note: Available at arXiv: <https://arxiv.org/abs/2410.08477>
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§2.2](#S2.SS2.p3.2 "2.2 Differential swaps and collateral conventions ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"),
  [§2.3](#S2.SS3.p3.3 "2.3 collateralised futures strategies ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"),
  [§2.4](#S2.SS4.p1.1 "2.4 Pricing martingale measure ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"),
  [§2](#S2.p3.4 "2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps"),
  [§3.1](#S3.SS1.p1.2 "3.1 Cross-currency model specification ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"),
  [§3.3](#S3.SS3.p1.1 "3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"),
  [Remark 3.2](#S3.Thmrem2.p1.4 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"),
  [Remark 3.2](#S3.Thmrem2.p1.6 "Remark 3.2. ‣ 3.3 Futures dynamics and the pricing martingale measure ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps"),
  [§4.1](#S4.SS1.p2.12 "4.1 Convexity corrections ‣ 4 Arbitrage-Free Pricing under Collateral Currency Choice ‣ Choice of Collateral Currency in Differential Swaps").
* [12]
  D. Duffie and J. C. Stein (2015)
  Reforming LIBOR and other financial market benchmarks.
  Journal of Economic Perspectives 29 (2),  pp. 191–212.
  External Links: [Document](https://dx.doi.org/10.1257/jep.29.2.191)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [13]
  C. Fontana, Z. Grbac, and T. Schmidt (2024)
  Term structure modeling with overnight rates beyond stochastic continuity.
  Mathematical Finance 34 (1),  pp. 151–189.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/mafi.12415)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [14]
  M. Fujii, Y. Shimada, and A. Takahashi (2010)
  A note on construction of multiple swap curves with and without collateral.
  Note: Available at SSRN: <https://ssrn.com/abstract=1440633>
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [15]
  M. Fujii, Y. Shimada, and A. Takahashi (2010)
  On the term structure of interest rates with basis spreads, collateral and multiple currencies.
  Note: Available at SSRN: <https://ssrn.com/abstract=1556487>
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [16]
  M. Fujii and A. Takahashi (2011)
  Choice of collateral currency.
  Risk January,  pp. 120–125.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [17]
  M. Fujii and A. Takahashi (2013)
  Derivative pricing under asymmetric and imperfect collateralization and CVA.
  Quantitative Finance 13 (5),  pp. 749–768.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2012.738931)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [18]
  A. Gnoatto and S. Lavagnini (2023)
  Cross currency Heath-Jarrow-Morton framework in the multiple-curve setting.
  Note: Available at arXiv: <https://arxiv.org/abs/2312.13057>
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [19]
  A. Gnoatto and N. Seiffert (2021)
  Cross currency valuation and hedging in the multiple curve framework.
  SIAM Journal on Financial Mathematics 12 (2),  pp. 967–1012.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [20]
  M. Henrard (2010)
  The irony in derivatives discounting part ii: the crisis.
  Wilmott Journal 2,  pp. 301–316.
  External Links: [Document](https://dx.doi.org/10.1002/wilj.39)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [21]
  J. Hull and A. White (2014)
  Valuing derivatives: funding value adjustments and fair value.
  Financial Analysts Journal 70 (3),  pp. 46–56.
  External Links: [Document](https://dx.doi.org/10.2469/faj.v70.n3.3)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [22]
  R. A. Jarrow and G. S. Oldfield (1981)
  Forward contracts and futures contracts.
  Journal of Financial Economics 9 (4),  pp. 373–382.
  External Links: [Document](https://dx.doi.org/10.1016/0304-405X%2881%2990004-0)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [23]
  M. Johannes and S. Sundaresan (2007)
  The impact of collateralization on swap rates.
  The Journal of Finance 62 (1),  pp. 383–410.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.2007.01210.x)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [24]
  J. Kennedy (2020)
  Pricing collateralized derivatives with an arbitrary numeraire.
  Mathematical Finance 30 (2),  pp. 464–500.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/mafi.12227)
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [25]
  J. Laurent, P. Amzelek, and J. Bonnaud (2014)
  An overview of the valuation of collateralized derivative contracts.
  Review of Derivatives Research 17 (3),  pp. 261–286.
  External Links: [Document](https://dx.doi.org/10.1007/s11147-014-9098-8)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [26]
  F. Mercurio (2010)
  Modern LIBOR market models: using different curves for projecting rates and for discounting.
  International Journal of Theoretical and Applied Finance 13 (1),  pp. 113–137.
  External Links: [Document](https://dx.doi.org/10.1142/S021902491000570X)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps"),
  [§1](#S1.p4.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").
* [27]
  M. Musiela and M. Rutkowski (2005)
  Martingale methods in financial modelling.
  2nd edition, Springer, Berlin Heidelberg.
  Cited by: [§3.1](#S3.SS1.p1.2 "3.1 Cross-currency model specification ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").
* [28]
  O. Vasicek (1977)
  An equilibrium characterization of the term structure.
  Journal of Financial Economics 5 (2),  pp. 177–188.
  External Links: ISSN 0304-405X
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Dynamics of auxiliary discount factors ‣ 3 Cross-Currency Term Structure Model ‣ Choice of Collateral Currency in Differential Swaps").
* [29]
  J. Z. Wei (1994)
  Valuing differential swaps.
  Journal of Derivatives, Spring 1,  pp. 64–76.
  Cited by: [Remark 2.1](#S2.Thmrem1.p1.3 "Remark 2.1. ‣ 2.2 Differential swaps and collateral conventions ‣ 2 Collateralised Trading Strategies and Pricing Measure ‣ Choice of Collateral Currency in Differential Swaps").
* [30]
  F. L. Wolf, L. A. Grzelak, and G. Deelstra (2022)
  Cheapest-to-deliver collateral: a common factor approach.
  Quantitative Finance 22 (4),  pp. 707–723.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2021.1990375)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Choice of Collateral Currency in Differential Swaps").

BETA