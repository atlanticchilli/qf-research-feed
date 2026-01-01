---
authors:
- Alexander M. G. Cox
- Daniel Hernandez-Hernandez
doc_id: arxiv:2512.24371v1
family_id: arxiv:2512.24371
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Utility maximisation with model-independent constraints
url_abs: http://arxiv.org/abs/2512.24371v1
url_html: https://arxiv.org/html/2512.24371v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alexander M. G. Cox
 and 
Daniel Hernandez-Hernandez

(Date: December 30, 2025)

###### Abstract.

We consider an agent who has access to a financial market, including derivative contracts, who looks to maximise her utility. Whilst the agent looks to maximise utility over one probability measure, or class of probability measures, she must also ensure that the mark-to-market value of her portfolio remains above a given threshold. When the mark-to-market value is based on a more pessimistic valuation method, such as model-independent bounds, we recover a novel optimisation problem for the agent where the agents investment problem must satisfy a pathwise constraint.

For complete markets, the expression of the optimal terminal wealth is given, using the max-plus decomposition for supermartingales. Moreover, for the Black-Scholes-Merton model the explicit form of the process involved in such decomposition is obtained, and we are able to investigate numerically optimal portfolios in the presence of options which are mispriced according to the agent’s beliefs.

###### Key words and phrases:

Model-independent constraints, trading restrictions, max-plus decomposition, utility maximization, intrinsic value

Alexander M. G. Cox, Department of Mathematical
Sciences, University of Bath, Bath, U. K..
  
e-mail: a.m.g.cox@bath.ac.uk, web: http://www.maths.bath.ac.uk/∼\simmapamgc/

Daniel Hernández, Department of Probability and Statistics, Research Center for
Mathematics (CIMAT), Mexico.
  
e-mail: dher@cimat.mx, web: http://www.cimat.mx/∼\simdher/

## 1. Introduction

In this paper we consider a utility maximisation problem for an agent who has some modelling beliefs, according to which the agent will aim to maximise her utility, but also some constraints which are based on model-independent considerations. Our basic setting is that the agent assumes they will observe only ‘possible’ paths according to their beliefs, and they will pursue a utility maximisation objective corresponding to their beliefs. We importantly include in our setting both trading in an underlying risky asset, as well as in illiquid derivatives, whose initial price and payoff are known, but no assumptions about the intermediate value can be made. The agent is also being observed by a manager or regulator who does not share the agent’s modelling assumptions, but rather uses other (typically more pessimistic) assumptions. The manager will intervene if their valuation of the agent’s portfolio goes below some given threshold, and the agent will act to avoid this scenario. Note that many real-world trading strategies are subject to related constraints, for example Interactive Brokers, an electronic trading platform, base customer margin requirements on a *portfolio margin* basis, which they state is ‘determined using a “risk-based” pricing model that calculates the largest potential loss of all positions in a product class or group across a range of underlying prices and volatilities’, [[24](https://arxiv.org/html/2512.24371v1#bib.bib24)].111We are grateful to Paulo Guasoni for pointing this out to us.

Under these modelling assumptions, our aim will be to determine the agent’s optimal trading strategy when they are able to take (static) positions in certain options, for example, call options, or other simple derivatives. In the context of some of these options, we will use the notion of an “intrinsic” value of an option, which we think of as the worst-case valuation of the option or portfolio of options, for example (in the absence of interest rates) the intrinsic vale of a long position in a call option with maturity TT and strike KK at time t<Tt<T is (St−K)+(S\_{t}-K)\_{+}, since this can be realised through taking model-independent positions in the underlying asset.

Our approach borrows from the literature model-independent or robust pricing and hedging (see e.g. [[21](https://arxiv.org/html/2512.24371v1#bib.bib21), [13](https://arxiv.org/html/2512.24371v1#bib.bib13), [20](https://arxiv.org/html/2512.24371v1#bib.bib20), [6](https://arxiv.org/html/2512.24371v1#bib.bib6), [15](https://arxiv.org/html/2512.24371v1#bib.bib15), [16](https://arxiv.org/html/2512.24371v1#bib.bib16), [5](https://arxiv.org/html/2512.24371v1#bib.bib5), [10](https://arxiv.org/html/2512.24371v1#bib.bib10), [14](https://arxiv.org/html/2512.24371v1#bib.bib14), [12](https://arxiv.org/html/2512.24371v1#bib.bib12)]). We also use classical results from the theory of utility maximisation in complete markets. Our approach to handling pathwise constraints is heavily inspired by the papers of [[18](https://arxiv.org/html/2512.24371v1#bib.bib18), [19](https://arxiv.org/html/2512.24371v1#bib.bib19)], see also [[3](https://arxiv.org/html/2512.24371v1#bib.bib3), [4](https://arxiv.org/html/2512.24371v1#bib.bib4)].

### 1.1. Basic Problem Formulation

We consider a market on the time interval [0,T][0,T], and we suppose that an asset price (St)t∈[0,T]∈C​([0,T])(S\_{t})\_{t\in[0,T]}\in C([0,T]) is observed, where for the moment we suppose all prices are given in discounted units. We suppose the agent believes that there is a class of probability measures 𝒫\mathcal{P}, and the agent aims to find

|  |  |  |  |
| --- | --- | --- | --- |
| (1.1) |  | supπinfℙ∈𝒫𝔼ℙ​[U​(w0+XTπ)],\sup\_{\pi}\inf\_{\mathbb{P}\in\mathcal{P}}\mathbb{E}^{\mathbb{P}}\left[U\left(w\_{0}+X\_{T}^{\pi}\right)\right], |  |

where UU is a utility function, w0w\_{0} the initial wealth of the agent, and XTπX\_{T}^{\pi} the trading gains of the agent given they follow the trading strategy π\pi.

More generally, we suppose that at time zero, the trader observes additional market information in the form of the prices of other traded derivatives. For example, the agent may observe the prices of call options given by C~​(K)=∫(x−K)+​μ​(d​x)\tilde{C}(K)=\int(x-K)\_{+}\,\mu(\mathrm{d}x) for some probability measure μ\mu (given by the Breeden-Litzenberger formula, [[9](https://arxiv.org/html/2512.24371v1#bib.bib9)]). In this case, the trader may purchase a portfolio of call options with payoff h​(ST)h(S\_{T}) for price ∫h​(x)​μ​(d​x)\int h(x)\,\mu(\mathrm{d}x) at time 0.

In our setup, we will impose a ‘model-independent’ restriction on the trader’s behavior by assuming a specific budget constraint. This constraint will occur when the trader’s portfolio contains derivatives. Our underlying assumption is that, even though the trader may evaluate the ‘correct’ price of the derivative in their model, they are subject to portfolio constraints imposed by a manager or regulator who is much more risk averse, and who values their derivatives using a more conservative set of pricing rules. We will typically call the valuation of the manager or regulator the *intrinsic value* of the derivatives. The canonical example of such a derivative is a call option, where the intrinsic value of the derivative is the ‘zero-volatility’ payoff of the option, or the terminal value of the call option if the asset grows at the (deterministic) interest rate D⋅−1D\_{\cdot}^{-1}.

Of crucial interest to us is that these intrinsic values are in general non-linear, and so choosing to purchase different portfolios of derivatives will have a complex effect on the terminal wealth of the investor, and hence on the optimal investment strategies of the investor. Our usual setup in this paper will be the case where the intrinsic value of the derivative corresponds to the model-independent sub-replication price of the derivative, and in many examples we are able to specifically identify this quantity in terms of the underlying contract.

For example in the case where the agent may purchase a portfolio of calls with payoff h​(ST)h(S\_{T}) then the *intrinsic value* of the portfolio at time tt will be h∗​(St)h^{\*}(S\_{t}), where h∗h^{\*} is the greatest convex minorant (on [0,∞)[0,\infty)) of the function hh. We think of the intrinsic value at time tt, which we write ℐt​(ST)=h∗​(St)\mathcal{I}\_{t}(S\_{T})=h^{\*}(S\_{t}), as the minimum value of the portfolio which can be guaranteed under *any* possible model. For example, if h​(x)=(x−K)+h(x)=(x-K)\_{+}, then h∗​(x)=h​(x)=(x−K)+h^{\*}(x)=h(x)=(x-K)\_{+}, and we confirm that this amount may be realised at time tt through the trading strategy which (if St>KS\_{t}>K) short sells the asset until either the asset drops below KK, or time TT, whichever is earlier. If we write HKt:=inf{r≥t:Sr≤K}H^{t}\_{K}:=\inf\{r\geq t:S\_{r}\leq K\}, then the value of this portfolio at maturity is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ST−K)++(St−ST∧HKt)\displaystyle(S\_{T}-K)\_{+}+(S\_{t}-S\_{T\wedge H^{t}\_{K}}) | ={(ST−K)++(St−K)HKt≤T(ST−K)+(St−ST)HKt>T\displaystyle=\begin{cases}(S\_{T}-K)\_{+}+(S\_{t}-K)&H^{t}\_{K}\leq T\\ (S\_{T}-K)+(S\_{t}-S\_{T})&H^{t}\_{K}>T\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥St−K.\displaystyle\geq S\_{t}-K. |  |

By considering the model where the asset price remains constant, so that the price under this model is equal to the intrinsic value, we conclude that this is the best we can do. Note, in particular, that with this trading strategy the trader’s wealth (including the intrinsic value) at time u>tu>t is always at least SuS\_{u}: that is,

|  |  |  |
| --- | --- | --- |
|  | ℐu​((ST−K)+)+(St−Su∧HKt)≥Su.\mathcal{I}\_{u}((S\_{T}-K)\_{+})+(S\_{t}-S\_{u\wedge H^{t}\_{K}})\geq S\_{u}. |  |

The constraint we impose on our trader is that the trader’s portfolio must satisfy an admissibility constraint, based on the intrinsic value of the derivatives. Specifically, we require the trader’s (intrinsic) wealth at every time tt to satisfy:

|  |  |  |  |
| --- | --- | --- | --- |
| (1.2) |  | Wtπ,h:=Dt−1​(w0−∫h​(x)​μ​(d​x))+ℐt​(h​(ST))+Xtπ≥−α.W\_{t}^{\pi,h}:=D\_{t}^{-1}(w\_{0}-\int h(x)\,\mu(\mathrm{d}x))+\mathcal{I}\_{t}(h(S\_{T}))+X\_{t}^{\pi}\geq-\alpha. |  |

The quantity α\alpha represents a lower bound imposed on the trader’s portfolio value, which is required to be observed at all times. We will call a wealth process which satisfies ([1.2](https://arxiv.org/html/2512.24371v1#S1.E2 "In 1.1. Basic Problem Formulation ‣ 1. Introduction ‣ Utility maximisation with model-independent constraints")) *α\alpha-admissible*.

Our intuition is as follows: the trader will follow her trading strategy π\pi in a manner that maintains ([1.2](https://arxiv.org/html/2512.24371v1#S1.E2 "In 1.1. Basic Problem Formulation ‣ 1. Introduction ‣ Utility maximisation with model-independent constraints")) at all times. Under any probability measure ℙ∈𝒫\mathbb{P}\in\mathcal{P}, this will result in a portfolio which satisfies the constraint. If the real path of the asset does not follow a path which is compatible with any ℙ∈𝒫\mathbb{P}\in\mathcal{P}, then the trader can monitor her wealth, and at the first time the wealth goes below −α-\alpha, then the trader will stop dynamic trading, and simply follow the simple strategy which realises (at worst) the intrinsic value of the asset. Combined with the intrinsic value of the portfolio, this strategy always ensures that the portfolio’s value remains above the lower bound.

Alternatively, one could tell the story from the perspective of a trader who is being monitored by a manager or regulator. The manager is conservative, and will look at the agent’s gains from trade continuously, evaluating their derivative portfolio using a stated, model-independent rule. If the trader’s *intrinsic* wealth goes below the level −α-\alpha, the manager will fire the trader and close out the position with a resulting loss bounded below by α\alpha. As a result, the trader wishes to pursue a strategy which does not result in their dismissal, and hence looks to find a strategy which stays above the intrinsic wealth constraint with probability one (under any model that they believe is possible).

Our results will take two different forms: first we will consider cases where the trader is able to trade dynamically to exploit mispricings, and guarantee a profit under certain conditions on the admissibility level α\alpha; these results will be in a similar spirit to classical model-independent pricing constraints on traded option prices. Second, we will consider utility maximisation problems, where the trader aims to maximise their utility from terminal wealth under the additional constraint that their wealth process is admissible. In this case, we will examine the impact of different choices of derivative portfolios, and will give concrete conclusions about the optimal strategies that should be employed by the investor when faced with various traded options on the market.

###### Remark 1.1.

We note that the notion of intrinsic value introduced above is fairly flexible. For example, above we defined the intrinsic value to be the convex minorant on [0,∞)[0,\infty), which corresponds to the case where it is not believed that the asset price can go negative. However, it is possible also to consider the intrinsic value assuming that asset prices can go below zero (e.g. in the Bachelier model). In this case, it might not be sufficient to consider the convex minorant on [0,∞)[0,\infty), but rather to look at the minorant on ℝ\mathbb{R}. In some cases, this would give different values of the intrinsic process. More generally, intrinsic values arising from robust pricing bounds (i.e. over a class of models) as opposed to model-independent (over all models) bounds are also natural to consider.

This paper is organized as follows: Section 2 introduces the notion of intrinsic value of derivative contracts in terms of a subreplicating submartingale, providing examples for specific
cases. The robust optimization problem of maximizing expected utility of terminal wealth subject to model independent intrinsic budget restrictions is presented in Section 3, together with some implications in the trader’s behavior. Specific results are obtained for the Black-Scholes-Merton model. In Section 4 optimal trading strategies are obtained under the assumption of completeness of the market, with the help of representations of supermartingales.

## 2. Intrinsic Valuation of Derivatives and Trading

We define here our basic market setup. We suppose that there is an underlying asset price process (St)t∈[0,T](S\_{t})\_{t\in[0,T]} which takes values in Ω:=Cs0​([0,T])\Omega:=C\_{s\_{0}}([0,T]), the set of continuous paths ω\omega on [0,T][0,T] with ω​(0)=s0\omega(0)=s\_{0}, and where we equip Ω\Omega with the uniform norm, under which topology Ω\Omega is a Polish space. This space is endowed with the Borel σ−\sigma-algebra 𝔽\mathbb{F}. Our agent believes that the underlying dynamics of SS are governed by a probability measure ℙ∈𝒫\mathbb{P}\in\mathcal{P}, for some class 𝒫\mathcal{P} of probability measures on Ω\Omega. We will typically be interested in statements which hold ℙ\mathbb{P}-a.s. for all ℙ∈𝒫\mathbb{P}\in\mathcal{P}, which we will write as 𝒫\mathcal{P}-a.s.. It is natural therefore to introduce 𝒩​(𝒫):={A∈𝔽:ℙ​(A)=0​∀ℙ∈𝒫}\mathcal{N}(\mathcal{P}):=\{A\in\mathbb{F}:\mathbb{P}(A)=0\ \forall\mathbb{P}\in\mathcal{P}\}. We also introduce the set 𝒬​(𝒫)\mathcal{Q}(\mathcal{P}), the set of martingale measures which are equivalent to some ℙ∈𝒫\mathbb{P}\in\mathcal{P}. The natural filtration generated by SS is denoted by ℱS={ℱtS}\mathcal{F}^{S}=\{\mathcal{F}\_{t}^{S}\}. We also need the filtration ℱ={ℱt;t∈[0,T]}\mathcal{F}=\{\mathcal{F}\_{t};\;t\in[0,T]\}, with ℱt:=ℱt+S=∩s>tℱsS\mathcal{F}\_{t}:=\mathcal{F}^{S}\_{t^{+}}=\cap\_{s>t}\mathcal{F}\_{s}^{S} for t<Tt<T and ℱT:=ℱTS\mathcal{F}\_{T}:=\mathcal{F}\_{T}^{S}, which is the minimal filtration associated to the process SS satisfying the usual conditions, i.e. {ℱt;t∈[0,T]}\{\mathcal{F}\_{t};\;t\in[0,T]\} is an increasing right continuous family of σ−\sigma-fields and completeness with respect to 𝒫\mathcal{P}, by which we mean that 𝒩​(𝒫)⊂ℱ0\mathcal{N}(\mathcal{P})\subset\mathcal{F}\_{0}.
We denote by Λ\Lambda a Meyer σ−\sigma-field which contains the predictable σ−\sigma-field with respect to ℱ\mathcal{F}, that is, the σ−\sigma-field generated by ℱ−\mathcal{F}-adapted, left-continuous processes, and which in turn is contained in the optional σ−\sigma-field with respect to the filtration ℱ\mathcal{F}.

In addition to the risky asset, we suppose there exists a bank account which pays a deterministic (although not necessarily constant) interest rate. We write DtD\_{t} for the discount factor, so the time-0 value of $​1\mathdollar 1 at time tt is DtD\_{t}, or equivalently, $​1\mathdollar 1 invested at time 0 will be worth $​Dt−1\mathdollar D\_{t}^{-1} at time tt. We assume then that DtD\_{t} is decreasing, continuous and D0=1D\_{0}=1.

We also associate with our setup trading strategies π\pi with respect to the filtration ℱ\mathcal{F}. In this paper we do not wish to directly address the specific technicalities of possible trading strategies under model-uncertainty, but refer readers to the large and growing literature for various approaches (e.g. [[16](https://arxiv.org/html/2512.24371v1#bib.bib16), [5](https://arxiv.org/html/2512.24371v1#bib.bib5), [7](https://arxiv.org/html/2512.24371v1#bib.bib7), [22](https://arxiv.org/html/2512.24371v1#bib.bib22), [17](https://arxiv.org/html/2512.24371v1#bib.bib17), [10](https://arxiv.org/html/2512.24371v1#bib.bib10)] among others). The details here will not be important, so we will generally either work in the case where 𝒫\mathcal{P} is a singleton, and classical results are applicable, or else in the case where 𝒫\mathcal{P} is large, and then we will only need to consider very simple trading strategies; see Remark [2.5](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2.2. Dynamic Trading Strategies ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints") below.

Note in particular, that these two cases are essentially the main ones of interest. For example, [[15](https://arxiv.org/html/2512.24371v1#bib.bib15)] show that a robust hedging for a large class of stochastic volatility models essentially reduces to the case where 𝒫\mathcal{P} contains all martingale measures.

We also consider the special ‘classical’ case of model-independent pricing, where

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | 𝒫∘:={ℙ:D​S​ is a non-negative, uniformly integrable martingale}.\mathcal{P}^{\circ}:=\{\mathbb{P}:DS\text{ is a non-negative, uniformly integrable martingale}\}. |  |

This will give rise to our canonical notion of intrinsic value, but other choices will also be possible.

### 2.1. Intrinsic Value of Derivative Contracts

We consider the intrinsic valuation of a derivative contract:

###### Definition 2.1.

A *derivative contract* is a measurable function CT:Ω→ℝC\_{T}:\Omega\to\mathbb{R}. We say that ℐ⋅​(CT)\mathcal{I}\_{\cdot}(C\_{T}) is a *fair intrinsic value* of a derivative contract CTC\_{T} corresponding to the class 𝒫\mathcal{P} of probability measures at time tt, if:

1. (i)

   Dt​ℐt​(CT)D\_{t}\mathcal{I}\_{t}(C\_{T}) is a càdlàg ℚ\mathbb{Q}-ℱ\mathcal{F}-submartingale for all ℚ∈𝒬​(𝒫)\mathbb{Q}\in\mathcal{Q}(\mathcal{P});
2. (ii)

   ℐT​(CT)=CT\mathcal{I}\_{T}(C\_{T})=C\_{T} 𝒫\mathcal{P}-a.s..

As an interesting fact, of course, Dt​ℐt​(CT)≤𝔼ℚ​[DT​CT|ℱt]D\_{t}\mathcal{I}\_{t}(C\_{T})\leq\mathbb{E}^{\mathbb{Q}}\left[D\_{T}C\_{T}|\mathcal{F}\_{t}\right], for all ℚ∈𝒬​(𝒫)\mathbb{Q}\in\mathcal{Q}(\mathcal{P}), where we are assuming throughout that DT​CTD\_{T}C\_{T} satisfy implicitly the required integrability conditions in order that the conditional expectation is well defined. On the other hand, in general, we would hope to find a maximal version of the fair intrinsic price for a given set 𝒫\mathcal{P}, which one could define (except for non-trivial measurability issues!) to be the price of the most expensive model-independent sub-replicating strategy. That is:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | Dtℐt(CT):=sup{x∈ℝ:∃(π) s.t. x+∫tTπrd(DrSr)≤DTCT𝒫−a.s.}.D\_{t}\mathcal{I}\_{t}(C\_{T}):=\sup\{x\in\mathbb{R}:\exists(\pi)\text{ s.t. }x+\int\_{t}^{T}\pi\_{r}\,\mathrm{d}(D\_{r}S\_{r})\leq D\_{T}C\_{T}\quad\mathcal{P}-a.s.{}\}. |  |

Such problems have been considered recently in discrete time ([[6](https://arxiv.org/html/2512.24371v1#bib.bib6), [8](https://arxiv.org/html/2512.24371v1#bib.bib8), [2](https://arxiv.org/html/2512.24371v1#bib.bib2)]) and continuous time ([[16](https://arxiv.org/html/2512.24371v1#bib.bib16), [5](https://arxiv.org/html/2512.24371v1#bib.bib5), [7](https://arxiv.org/html/2512.24371v1#bib.bib7), [22](https://arxiv.org/html/2512.24371v1#bib.bib22), [17](https://arxiv.org/html/2512.24371v1#bib.bib17), [10](https://arxiv.org/html/2512.24371v1#bib.bib10)]), but defining this process in general in continuous time is a non-trivial technical exercise. For the majority of this paper, our aim will be to consider easily specified intrinsic value processes, but we emphasise that in our setup the chosen fair intrinsic value is a part of the modelling framework, and not necessarily a given quantity.

Note in particular that we do not expect the intrinsic price ℐt\mathcal{I}\_{t} to be linear: we do not typically expect for example ℐt​(β​CT)=β​ℐt​(CT)\mathcal{I}\_{t}(\beta C\_{T})=\beta\mathcal{I}\_{t}(C\_{T}) if β<0\beta<0. However, the intrinsic price will generally be positive homogenous, with ℐt​(β​CT)=β​ℐt​(CT)\mathcal{I}\_{t}(\beta C\_{T})=\beta\mathcal{I}\_{t}(C\_{T}) if β≥0\beta\geq 0.

###### Example 2.2.

In the case where 𝒫=𝒫∘\mathcal{P}=\mathcal{P}^{\circ}, see ([2.1](https://arxiv.org/html/2512.24371v1#S2.E1 "In 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints")), and Dt≡1D\_{t}\equiv 1, we can give concrete examples of an intrinsic value process which does in fact satisfy ([2.2](https://arxiv.org/html/2512.24371v1#S2.E2 "In 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints")). Since many of our examples will be based on this specific choice of the intrinsic price process, we denote this specific operator by ℐ∘\mathcal{I}^{\circ}.

1. (i)

   If h:ℝ+→ℝh:\mathbb{R}\_{+}\to\mathbb{R}, then ℐt∘​(h​(ST))=h∗​(St)​𝟏t<T+h​(ST)​𝟏t=T\mathcal{I}^{\circ}\_{t}(h(S\_{T}))=h^{\*}(S\_{t})\boldsymbol{1}\_{t<T}+h(S\_{T})\boldsymbol{1}\_{t=T}, where h∗​(x)h^{\*}(x) is the greatest convex minorant of hh (on ℝ+\mathbb{R}\_{+}). For example, h∗​((x−k)+)=(x−k)+h^{\*}((x-k)\_{+})=(x-k)\_{+}, but h∗​(−(x−k)+)=−xh^{\*}(-(x-k)\_{+})=-x.

   To see this, we first observe that this intrinsic price satisfies all of the conditions of Definition [2.1](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints"). Second, to see that this is the greatest such price, observe that if h∗​(x)h^{\*}(x) is the greatest convex minorant of hh, for x∈(0,∞)x\in(0,\infty) we can find yn≤x≤zny\_{n}\leq x\leq z\_{n} such that

   |  |  |  |
   | --- | --- | --- |
   |  | h∗​(x)=limn→∞[(zn−x)​h​(yn)+(x−yn)​h​(zn)zn−yn].h^{\*}(x)=\lim\_{n\to\infty}\left[\frac{(z\_{n}-x)h(y\_{n})+(x-y\_{n})h(z\_{n})}{z\_{n}-y\_{n}}\right]. |  |

   Now consider the model which is a (uniformly integrable, continuous) martingale, which runs from xx at time t<Tt<T, to either znz\_{n} or yny\_{n} at time TT. Then the fair price of the derivative under this model is exactly [(zn−x)​h​(yn)+(x−yn)​h​(zn)zn−yn]\left[\frac{(z\_{n}-x)h(y\_{n})+(x-y\_{n})h(z\_{n})}{z\_{n}-y\_{n}}\right], and the claim follows. In the presence of non-zero interest rates, it is easy to see by a similar argument that ℐt∘​(h​(ST))=Dt−1​DT​h∗​(DT−1​Dt​St)​𝟏t<T+h​(ST)​𝟏t=T\mathcal{I}^{\circ}\_{t}(h(S\_{T}))=D\_{t}^{-1}D\_{T}h^{\*}(D\_{T}^{-1}D\_{t}S\_{t})\boldsymbol{1}\_{t<T}+h(S\_{T})\boldsymbol{1}\_{t=T}.
2. (ii)

   If 0<T′<T0<T^{\prime}<T then ℐt​(h​(ST′))=h∗​(St)​𝟏t<T′+h​(ST′)​𝟏t≥T′\mathcal{I}\_{t}(h(S\_{T^{\prime}}))=h^{\*}(S\_{t})\boldsymbol{1}\_{t<T^{\prime}}+h(S\_{T^{\prime}})\boldsymbol{1}\_{t\geq T^{\prime}}. This is essentially the same argument as in *(i)*.
3. (iii)

   If B>0B>0 is a fixed barrier, we can consider the
   *one-touch* option, 𝖮𝖳TB:=𝟏ST∗≥B\mathsf{OT}^{B}\_{T}:=\boldsymbol{1}\_{S\_{T}^{\*}\geq B}, where
   St∗=supr≤tSrS\_{t}^{\*}=\sup\_{r\leq t}S\_{r} is the maximum process. In
   particular, it can be checked that one has ℐt​(𝖮𝖳TB)=𝟏St∗≥B\mathcal{I}\_{t}(\mathsf{OT}\_{T}^{B})=\boldsymbol{1}\_{S\_{t}^{\*}\geq B}, while ℐt​(−𝖮𝖳TB)=−StB​𝟏St∗<B,t<T−𝟏St∗≥B\mathcal{I}\_{t}(-\mathsf{OT}\_{T}^{B})=-\frac{S\_{t}}{B}\boldsymbol{1}\_{S\_{t}^{\*}<B,t<T}-\boldsymbol{1}\_{S\_{t}^{\*}\geq B}.

   In fact, in the last case, we can extend some of these ideas. For example, let K<BK<B. Then we have for t≤Tt\leq T

   |  |  |  |
   | --- | --- | --- |
   |  | ℐt​((ST−K)+B−K−𝖮𝖳TB)={0, if ​St∗<B1B−K​[(St−SHB)+(K−St)+], if ​St∗≥B,\mathcal{I}\_{t}\left(\frac{(S\_{T}-K)\_{+}}{B-K}-\mathsf{OT}\_{T}^{B}\right)=\begin{cases}0,&\quad\text{ if }S\_{t}^{\*}<B\\ \frac{1}{B-K}\left[(S\_{t}-S\_{H\_{B}})+(K-S\_{t})\_{+}\right],&\quad\text{ if }S\_{t}^{\*}\geq B\end{cases}, |  |

   where we write HB:=inf{t≥0:St=B}H\_{B}:=\inf\{t\geq 0:S\_{t}=B\}. This is a consequence of the hedge for one-touch options given by [[21](https://arxiv.org/html/2512.24371v1#bib.bib21)].

   We note that the amount (St−SHB)(S\_{t}-S\_{H\_{B}}) is easily constructed from an adapted trading strategy (buy one unit of the asset if it hits BB before TT). Including this additional trading, the intrinsic value of the combined position is then simply (K−St)+​𝟏HB≤t(K-S\_{t})\_{+}\boldsymbol{1}\_{H\_{B}\leq t}.

### 2.2. Dynamic Trading Strategies

We also wish to consider the class of dynamic trading strategies which are available to our agent for investment. Typically we would expect these to be specified as part of the modelling assumptions, and could depend on the choice of 𝒫\mathcal{P}. For example, if 𝒫\mathcal{P} is a singleton, one may be able to use the standard stochastic integral, while for more complex choices of 𝒫\mathcal{P}, one needs to be more careful to admit a measurable choice of the resulting trading strategy.

###### Definition 2.3.

To each choice of *dynamic trading strategy* π\pi, we associate a corresponding *gains process* X⋅π:Ω→C0​([0,T])X\_{\cdot}^{\pi}:\Omega\to C\_{0}([0,T]). We say that a dynamic trading strategy π\pi, or equivalently the gains process X⋅πX^{\pi}\_{\cdot}, is *𝒫\mathcal{P}-admissible*, if there exist a≥0a\geq 0 and a process Γ\Gamma, with Γt≥0\Gamma\_{t}\geq 0 𝒫t\mathcal{P}\_{t}-a.s. for all t≥0t\geq 0, such that sup0≤t≤TΓt\sup\_{0\leq t\leq T}\Gamma\_{t} is ℚ\mathbb{Q}-integrable for any ℚ∈𝒬​(𝒫)\mathbb{Q}\in\mathcal{Q}(\mathcal{P}), and Dt​Xtπ≥−a​(1+Γt)D\_{t}X\_{t}^{\pi}\geq-a(1+\Gamma\_{t}) 𝒫\mathcal{P}-a.s. holds for all tt.

By abuse of notation, we will often write ∫0tπs​d​(Ds​Ss)=Dt​Xtπ\int\_{0}^{t}\pi\_{s}\,\mathrm{d}(D\_{s}S\_{s})=D\_{t}X\_{t}^{\pi}, despite the fact that π\pi may not be explicitly defined as a pathwise object.
In most examples, process Γ\Gamma will be taken without further comment as Γt=1+Dt​|St|\Gamma\_{t}=1+D\_{t}|S\_{t}|, and then Doob’s inequality will give the required integrability provided

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[((1+DT​ST)​log⁡(1+DT​|ST|))+]<∞, for all​ℚ∈𝒬​(𝒫).\mathbb{E}^{\mathbb{Q}}\left[((1+D\_{T}S\_{T})\log(1+D\_{T}|S\_{T}|))\_{+}\right]<\infty,\;\;\;\text{ for all}\;\;\;\mathbb{Q}\in\mathcal{Q}(\mathcal{P}). |  |

Note that we need a constraint on dynamic trading strategies to rule out possible doubling strategies. It is natural to impose conditions which are pathwise and not probabilistic since we are potentially considering multiple pricing measures. Relevant results which show that the pathwise interpretation is sufficient can be found in [[1](https://arxiv.org/html/2512.24371v1#bib.bib1)]. The condition above will naturally be satisfied if (for example) our market includes derivatives whose payoffs have growth rate which is larger than ((1+DT​ST)​log⁡(1+DT​|ST|))+((1+D\_{T}S\_{T})\log(1+D\_{T}|S\_{T}|))\_{+}. We can then deduce from the relevant pathwise condition that the trading portfolio is uniformly integrable. If we have stronger integrability (for example we know 𝔼ℚ​[STp]<∞\mathbb{E}^{\mathbb{Q}}\left[S\_{T}^{p}\right]<\infty for some p>1p>1), then we can weaken the pathwise constraint by increasing Γ\Gamma appropriately.

We make the following definition:

###### Definition 2.4.

We say that 𝒱\mathcal{V} is a set of *admissible dynamic trading strategies* if, for each π∈𝒱\pi\in\mathcal{V}, the gains process XπX^{\pi} is:

1. (i)

   ℱ\mathcal{F}-adapted,
2. (ii)

   𝒫\mathcal{P}-admissible, and
3. (iii)

   Dt​XtπD\_{t}X\_{t}^{\pi} is a ℚ\mathbb{Q}-local martingale for every ℚ∈𝒬​(𝒫)\mathbb{Q}\in\mathcal{Q}(\mathcal{P}).

We further assume that the set 𝒱\mathcal{V} is closed under addition and non-negative scalar multiplication, that is, if π,ψ∈𝒱\pi,\psi\in\mathcal{V} and λ,μ≥0\lambda,\mu\geq 0, then λ​π+μ​ψ∈𝒱\lambda\pi+\mu\psi\in\mathcal{V}, where Xλ​π+μ​ψ:=λ​Xπ+μ​XψX^{\lambda\pi+\mu\psi}:=\lambda X^{\pi}+\mu X^{\psi}.

###### Remark 2.5.

Note that in the case where the asset price process SS is non-negative, the class of simple trading strategies, ie πt=∑i=1n 1{t∈(τi−1,τi]}​ai\pi\_{t}=\sum\_{i=1}^{n}\,\boldsymbol{1}\_{\{t\in(\tau\_{i-1},\tau\_{i}]\}}a\_{i}, where aia\_{i} are bounded and ℱτi\mathcal{F}\_{\tau\_{i}}-measurable, and (τi)i=1n(\tau\_{i})\_{i=1}^{n} is a sequence of increasing, ℱ\mathcal{F}-predictable stopping times in [0,T][0,T], belongs to the set of admissible strategies. Similarly, the *buy-and-hold* strategy is always allowed in a set of admissible dynamic trading strategies.

We can adopt results from Dolinsky-Soner, e.g. [[16](https://arxiv.org/html/2512.24371v1#bib.bib16)] to show that the class of progressively measurable trading strategies includes
finite variation strategies π\pi, defining the stochastic integral pathwise via integration by parts:

|  |  |  |
| --- | --- | --- |
|  | ∫0tπs​d​(Ds​Ss):=πt​Dt​St−π0​S0−∫0tDs​Ss​𝑑πs.\int\_{0}^{t}\pi\_{s}\,\mathrm{d}(D\_{s}S\_{s}):=\pi\_{t}D\_{t}S\_{t}-\pi\_{0}S\_{0}-\int\_{0}^{t}D\_{s}S\_{s}d\pi\_{s}. |  |

This definition is consistent with the stochastic integration for simple trading strategies.

## 3. Trading with constraints on Intrinsic Wealth

### 3.1. General setup and preliminary results

We begin by making the following observation about trading under intrinsic value constraints. We fix a class 𝒫\mathcal{P} of possible probability measures, and a set 𝒱\mathcal{V} of admissible dynamic trading strategies. We first suppose that there is an agent who acts to maximise utility from wealth, and the utility function UU satisfies the Inada conditions (U:[0,∞)→ℝ∪{−∞}U:[0,\infty)\to\mathbb{R}\cup\{-\infty\} is concave increasing and U′​(0)=∞,U′​(∞)=0U^{\prime}(0)=\infty,U^{\prime}(\infty)=0). We suppose that the agent will maximise worst case utility, in the presence of a derivative CTC\_{T} which has been purchased for price c0c\_{0}, so the problem is to find:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | supπ∈𝒱infℙ∈𝒫𝔼ℙ​[U​(DT−1​(w0−c0)+CT+XTπ)],\sup\_{\pi\in\mathcal{V}}\inf\_{\mathbb{P}\in\mathcal{P}}\mathbb{E}^{\mathbb{P}}\left[U\left(D\_{T}^{-1}(w\_{0}-c\_{0})+C\_{T}+X\_{T}^{\pi}\right)\right], |  |

where XtπX\_{t}^{\pi} is the gains from dynamic trading, subject to the *intrinsic budget constraint*

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | Wtπ,C:=Dt−1(w0−c0)+ℐt(CT)+Xtπ≥−Dt−1α,𝒫−a.s.,∀ 0≤t≤T,W\_{t}^{\pi,C}:=D\_{t}^{-1}(w\_{0}-c\_{0})+\mathcal{I}\_{t}(C\_{T})+X\_{t}^{\pi}\geq-D\_{t}^{-1}\alpha,\qquad\mathcal{P}-a.s.{},\forall\;0\leq t\leq T, |  |

where w0,α≥0w\_{0},\alpha\geq 0.

###### Definition 3.1.

We call a trading strategy π∈𝒱\pi\in\mathcal{V} a (w0,α,c0,CT)(w\_{0},\alpha,c\_{0},C\_{T})-intrinsically admissible dynamic trading strategy if WTπ,C≥0W\_{T}^{\pi,C}\geq 0 and ([3.2](https://arxiv.org/html/2512.24371v1#S3.E2 "In 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")) holds. Then, we write π∈𝒱​(w0,α,c0,CT)\pi\in\mathcal{V}(w\_{0},\alpha,c\_{0},C\_{T}).

Our first result describes some simple cases where the trader’s behavior can be easily described.

###### Lemma 3.2.

1. (i)

   Suppose there exists ψ∈𝒱\psi\in\mathcal{V} which 𝒫\mathcal{P}-superreplicates CTC\_{T} for initial value κ\kappa:

   |  |  |  |
   | --- | --- | --- |
   |  | κ+∫0Tψr​d​(Dr​Sr)≥DT​CT,𝒫−a.s.,\kappa+\int\_{0}^{T}\psi\_{r}\,\mathrm{d}(D\_{r}S\_{r})\geq D\_{T}C\_{T},\quad\mathcal{P}-a.s.{}, |  |

   and further

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (3.3) |  | c0+∫0tψr​d​(Dr​Sr)≥Dt​ℐt​(CT),∀t,𝒫−a.s.c\_{0}+\int\_{0}^{t}\psi\_{r}\,\mathrm{d}(D\_{r}S\_{r})\geq D\_{t}\mathcal{I}\_{t}(C\_{T}),\quad\forall t,\mathcal{P}-a.s.{} |  |

   Then if κ<c0\kappa<c\_{0}, the market price of the option, it is never optimal for the trader to purchase the option, that is, for all π∈𝒱​(w0,α,c0,CT)\pi\in\mathcal{V}(w\_{0},\alpha,c\_{0},C\_{T}) there exists π^∈𝒱​(w0,α,0,0)\hat{\pi}\in\mathcal{V}(w\_{0},\alpha,0,0) such that WTπ^≥WTπ,CW\_{T}^{\hat{\pi}}\geq W\_{T}^{\pi,C}.
2. (ii)

   Suppose there exists a strategy ψ∈𝒱\psi\in\mathcal{V} which 𝒫\mathcal{P}-subreplicates CTC\_{T} for initial value κ\kappa:

   |  |  |  |
   | --- | --- | --- |
   |  | κ+∫0Tψr​d​(Dr​Sr)≤DT​CT,𝒫−a.s.,\kappa+\int\_{0}^{T}\psi\_{r}\,\mathrm{d}(D\_{r}S\_{r})\leq D\_{T}C\_{T},\quad\mathcal{P}-a.s.{}, |  |

   such that −ψ∈𝒱-\psi\in\mathcal{V} and the path constraint:

   |  |  |  |
   | --- | --- | --- |
   |  | c0+∫0tψr​d​(Dr​Sr)≤Dt​ℐt​(CT),∀t,𝒫−a.s.c\_{0}+\int\_{0}^{t}\psi\_{r}\,\mathrm{d}(D\_{r}S\_{r})\leq D\_{t}\mathcal{I}\_{t}(C\_{T}),\quad\forall t,\mathcal{P}-a.s.{} |  |

   holds. If κ>c0\kappa>c\_{0}, then the trader can find portfolios with arbitrarily large utility.

###### Proof.

1. (i)

   We compare the strategy which purchases the option for price C0C\_{0}, and follows the (w0,α,c0,CT)(w\_{0},\alpha,c\_{0},C\_{T})-admissible dynamic trading strategy π∈𝒱​(w0,α,c0,CT)\pi\in\mathcal{V}(w\_{0},\alpha,c\_{0},C\_{T}), with the strategy which simply follows the dynamic trading strategy π+ψ\pi+\psi. Since π\pi and ψ\psi are both in 𝒱\mathcal{V}, so too is the combined trading strategy. We need to show that π+ψ∈𝒱​(w0,α,0,0)\pi+\psi\in\mathcal{V}(w\_{0},\alpha,0,0) and WTπ+ψ,0≥WTπ,CW\_{T}^{\pi+\psi,0}\geq W\_{T}^{\pi,C}.

   Now WTπ,C=DT−1​(w0−c0)+CT+XTπ≥0W\_{T}^{\pi,C}=D\_{T}^{-1}(w\_{0}-c\_{0})+C\_{T}+X\_{T}^{\pi}\geq 0 since π∈𝒱​(w0,α,c0,CT)\pi\in\mathcal{V}(w\_{0},\alpha,c\_{0},C\_{T}), and WTπ+ψ,0=DT−1​w0+XTπ+ψ=DT−1​w0+XTπ+XTψ≥DT−1​(w0−κ)+CT+XTπ>WTπ,CW\_{T}^{\pi+\psi,0}=D\_{T}^{-1}w\_{0}+X\_{T}^{\pi+\psi}=D\_{T}^{-1}w\_{0}+X\_{T}^{\pi}+X\_{T}^{\psi}\geq D\_{T}^{-1}(w\_{0}-\kappa)+C\_{T}+X\_{T}^{\pi}>W\_{T}^{\pi,C}. It remains to show that the strategy π+ψ\pi+\psi satisfies ([3.2](https://arxiv.org/html/2512.24371v1#S3.E2 "In 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")). Since π∈𝒱​(w0,α,c0,CT)\pi\in\mathcal{V}(w\_{0},\alpha,c\_{0},C\_{T}), we know that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | −Dt−1​α\displaystyle-D\_{t}^{-1}\alpha | ≤Dt−1​(w0−c0)+ℐt​(CT)+Xtπ\displaystyle\leq D\_{t}^{-1}(w\_{0}-c\_{0})+\mathcal{I}\_{t}(C\_{T})+X\_{t}^{\pi} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤Dt−1​(w0−c0)+(Xtψ+Dt−1​c0)+Xtπ\displaystyle\leq D\_{t}^{-1}(w\_{0}-c\_{0})+\left(X\_{t}^{\psi}+D\_{t}^{-1}c\_{0}\right)+X\_{t}^{\pi} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =Dt−1​w0+Xtπ+ψ\displaystyle=D\_{t}^{-1}w\_{0}+X\_{t}^{\pi+\psi} |  |

   for all t,𝒫−a.s.t,\mathcal{P}-a.s.{}, using ([3.3](https://arxiv.org/html/2512.24371v1#S3.E3 "In item i ‣ Lemma 3.2. ‣ 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")) in the second line.
2. (ii)

   Let λ>0\lambda>0 and suppose the trader buys λ\lambda units of the derivative for price c0c\_{0}, and takes short position −λ​ψt-\lambda\psi\_{t}. Then the traders terminal wealth is:

   |  |  |  |
   | --- | --- | --- |
   |  | WT−λ​ψ,λ​C=DT−1​w0+λ​(CT−XTψ−DT−1​κ)+λ​(κ−c0).W\_{T}^{-\lambda\psi,\lambda C}=D\_{T}^{-1}w\_{0}+\lambda\left(C\_{T}-X\_{T}^{\psi}-D\_{T}^{-1}\kappa\right)+\lambda(\kappa-c\_{0}). |  |

   Since first term in brackets is non-negative, and the second term is strictly positive, the trader’s utility can be made arbitrarily large as λ→∞\lambda\to\infty.

   On the other hand, at any time tt, we have:

   |  |  |  |
   | --- | --- | --- |
   |  | Dt−1​w0+λ​ℐt​(CT)−λ​Xtψ−λ​Dt−1​c0≥Dt−1​w0≥−Dt−1​α,D\_{t}^{-1}w\_{0}+\lambda\mathcal{I}\_{t}(C\_{T})-\lambda X\_{t}^{\psi}-\lambda D\_{t}^{-1}c\_{0}\geq D\_{t}^{-1}w\_{0}\geq-D\_{t}^{-1}\alpha, |  |

   and so the strategy satisfies the trading constraint.

∎

###### Remark 3.3.

1. (a)

   Note that Lemma [3.2](https://arxiv.org/html/2512.24371v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints") can also be applied to shorting an option, by replacing CC by −C-C, and c0c\_{0} by −c0-c\_{0}.
2. (b)

   In ([i](https://arxiv.org/html/2512.24371v1#S3.I1.i1 "item i ‣ Lemma 3.2. ‣ 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")), the pathwise condition is fairly weak: we know κ+DT​XTψ≥DT​CT\kappa+D\_{T}X\_{T}^{\psi}\geq D\_{T}C\_{T}, and hence for any ℚ∈𝒬​(𝒫)\mathbb{Q}\in\mathcal{Q}(\mathcal{P}), using Definitions [2.4](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem4 "Definition 2.4. ‣ 2.2. Dynamic Trading Strategies ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints") and [2.1](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints"), we expect that

   |  |  |  |
   | --- | --- | --- |
   |  | κ+Dt​Xtψ≥κ+𝔼ℚ​[DT​XTψ|ℱt]≥𝔼ℚ​[DT​CT|ℱt]≥ℐt​(CT).\displaystyle\kappa+D\_{t}X\_{t}^{\psi}\geq\kappa+\mathbb{E}^{\mathbb{Q}}\left[D\_{T}X\_{T}^{\psi}|\mathcal{F}\_{t}\right]\geq\mathbb{E}^{\mathbb{Q}}\left[D\_{T}C\_{T}|\mathcal{F}\_{t}\right]\geq\mathcal{I}\_{t}(C\_{T}). |  |

   This is almost sufficient to deduce the pathwise constraint, however there is no guarantee in our setup that this may hold 𝒫\mathcal{P}-almost everywhere for a given tt; there may exist sets of paths which are 𝒫\mathcal{P}-possible, but do not appear under any ℚ∈𝒬​(𝒫)\mathbb{Q}\in\mathcal{Q}(\mathcal{P}) for superhedging problems. See e.g. [[2](https://arxiv.org/html/2512.24371v1#bib.bib2)] for a discussion of this phenomena.

   On the other hand, the corresponding condition in ([ii](https://arxiv.org/html/2512.24371v1#S3.I1.i2 "item ii ‣ Lemma 3.2. ‣ 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")) is much stronger, in particular taking t=0t=0 it already implies that the market price of the option is below its intrinsic value. This reflects the much stronger conclusion possible in ([ii](https://arxiv.org/html/2512.24371v1#S3.I1.i2 "item ii ‣ Lemma 3.2. ‣ 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")).

### 3.2. European Options in the Black-Scholes-Merton model

For motivation, we start by considering the case where the agent believes the underlying model is the Black-Scholes-Merton model. In this case, the set 𝒫\mathcal{P} is a singleton, and moreover, the market is complete, so a desired (non-negative, integrable) terminal wealth XTX\_{T} can be realised through an admissible dynamic trading strategy, with portfolio process π∈𝒱\pi\in\mathcal{V} such that Xtπ=Dt−1​𝔼ℚ​[DT​XT|ℱt]X\_{t}^{\pi}=D\_{t}^{-1}\mathbb{E}^{\mathbb{Q}}\left[D\_{T}X\_{T}|\mathcal{F}\_{t}\right], where ℚ\mathbb{Q} is the usual (unique) risk-neutral measure. We will assume that the intrinsic price value is given by ℐ=ℐ∘\mathcal{I}=\mathcal{I}^{\circ} as described in Example [2.2](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem2 "Example 2.2. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints").

We suppose that our agent holds a European option with terminal value h​(ST)h(S\_{T}), for some measurable function hh such that h​(x)≤a​(1+x)h(x)\leq a(1+x) for some a>0a>0, and we are interested in the admissibility of this simple trading strategy for different values of α\alpha. We can write 𝖡𝖲​(h,t,T,St)\mathsf{BS}(h,t,T,S\_{t}) for the price at time tt of an option with payoff hh, time-to-maturity TT and current asset price StS\_{t}. If the trader purchases the option and trades dynamically to hedge the risk completely, it follows that Xtπ=Dt−1​𝖡𝖲​(h,0,T,S0)−𝖡𝖲​(h,t,T,St)X\_{t}^{\pi}=D\_{t}^{-1}\mathsf{BS}(h,0,T,S\_{0})-\mathsf{BS}(h,t,T,S\_{t}). If the trader follows the strategy of investing in the portfolio hh at price c0c\_{0} and hedging using the strategy π\pi, then the intrinsic portfolio value at time tt is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wtπ,h\displaystyle W\_{t}^{\pi,h} | :=Dt−1​(w0−c0)+ℐt​(h​(ST))+Xtπ\displaystyle:=D\_{t}^{-1}(w\_{0}-c\_{0})+\mathcal{I}\_{t}(h(S\_{T}))+X\_{t}^{\pi} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Dt−1​(w0−c0)+DTDt​h∗​(St​DtDT)+Dt−1​𝖡𝖲​(h,0,T,S0)−𝖡𝖲​(h,t,T,St).\displaystyle\;=D\_{t}^{-1}(w\_{0}-c\_{0})+\frac{D\_{T}}{D\_{t}}h^{\*}\left(S\_{t}\frac{D\_{t}}{D\_{T}}\right)+D\_{t}^{-1}\mathsf{BS}(h,0,T,S\_{0})-\mathsf{BS}(h,t,T,S\_{t}). |  |

Consider initially the case where h​(x)=(x−K)+h(x)=(x-K)\_{+}, for K≥0K\geq 0, write 𝖡𝖲​(h,⋅,⋅,⋅)=𝖡𝖲C​(K,⋅,⋅,⋅)\mathsf{BS}(h,\cdot,\cdot,\cdot)=\mathsf{BS}^{C}(K,\cdot,\cdot,\cdot) and denote by c0​(K)c\_{0}(K) the time-0 market price of the option, which (since we are taking a long position) we expect (but do not need) to be lower than the fair price of the derivative, i.e. c0​(K)<𝖡𝖲C​(K,0,T,S0)c\_{0}(K)<\mathsf{BS}^{C}(K,0,T,S\_{0}). Write Δ​C​(K):=𝖡𝖲C​(K,0,T,S0)−c0​(K)\Delta C(K):=\mathsf{BS}^{C}(K,0,T,S\_{0})-c\_{0}(K), the difference between the fair price and the market price, then our admissibility criteria ([3.2](https://arxiv.org/html/2512.24371v1#S3.E2 "In 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")) for this strategy becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt−1​(w0+Δ​C​(K))+(St−K​DTDt)+−𝖡𝖲C​(K,t,T,St)\displaystyle D\_{t}^{-1}\left(w\_{0}+\Delta C(K)\right)+\left(S\_{t}-K\frac{D\_{T}}{D\_{t}}\right)\_{+}-\mathsf{BS}^{C}(K,t,T,S\_{t}) | ≥−αDt\displaystyle\geq-\frac{\alpha}{D\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔(w0+Δ​C​(K))+(St​Dt−K​DT)+−Dt​𝖡𝖲C​(K,t,T,St)\displaystyle\iff\quad\left(w\_{0}+\Delta C(K)\right)+\left(S\_{t}D\_{t}-KD\_{T}\right)\_{+}-D\_{t}\mathsf{BS}^{C}(K,t,T,S\_{t}) | ≥−α.\displaystyle\geq-\alpha. |  |

Now, noting that t↦Dt​𝖡𝖲C​(K,t,T,s​Dt−1)t\mapsto D\_{t}\mathsf{BS}^{C}(K,t,T,sD\_{t}^{-1}) is decreasing by Jensen’s inequality and the convexity of s↦𝖡𝖲C​(K,t,T,s)s\mapsto\mathsf{BS}^{C}(K,t,T,s), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | inft∈[0,T]s∈[0,∞){(sDt−KDT\displaystyle\inf\_{\begin{subarray}{c}t\in[0,T]\\ s\in[0,\infty)\end{subarray}}\Big\{(sD\_{t}-KD\_{T} | )+−Dt𝖡𝖲C(K,t,T,s)}\displaystyle)\_{+}-D\_{t}\mathsf{BS}^{C}(K,t,T,s)\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inft∈[0,T]s∈[0,∞){(s−K​DT)+−Dt​𝖡𝖲C​(K,t,T,s​Dt−1)}\displaystyle=\inf\_{\begin{subarray}{c}t\in[0,T]\\ s\in[0,\infty)\end{subarray}}\left\{(s-KD\_{T})\_{+}-D\_{t}\mathsf{BS}^{C}(K,t,T,sD\_{t}^{-1})\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =infs∈[0,∞){(s−K​DT)+−𝖡𝖲C​(K,0,T,s)}\displaystyle=\inf\_{s\in[0,\infty)}\left\{(s-KD\_{T})\_{+}-\mathsf{BS}^{C}(K,0,T,s)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−𝖡𝖲C​(K,0,T,K​DT).\displaystyle=-\mathsf{BS}^{C}(K,0,T,KD\_{T}). |  |

We can summarise in the following:

###### Proposition 3.4.

In the Black-Scholes-Merton problem with intrinsic price given by ℐ∘\mathcal{I}^{\circ}, for π\pi the usual delta-hedging of a long position in the European call option with strike KK, then π∈𝒱​(w0,α,c0​(K),(ST−K)+)\pi\in\mathcal{V}(w\_{0},\alpha,c\_{0}(K),(S\_{T}-K)\_{+}) if

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | w0+Δ​C​(K)≥𝖡𝖲C​(K,0,T,K​DT)−α,w\_{0}+\Delta C(K)\geq\mathsf{BS}^{C}(K,0,T,KD\_{T})-\alpha, |  |

where Δ​C​(K):=𝖡𝖲C​(K,0,T,S0)−c0​(K)\Delta C(K):=\mathsf{BS}^{C}(K,0,T,S\_{0})-c\_{0}(K).
Similarly

|  |  |  |
| --- | --- | --- |
|  | −π∈𝒱​(w0,α,−c0​(K),−(ST−K)+)-\pi\in\mathcal{V}(w\_{0},\alpha,-c\_{0}(K),-(S\_{T}-K)\_{+}) |  |

if

|  |  |  |
| --- | --- | --- |
|  | w0+α−Δ​C​(K)≥K​DT.w\_{0}+\alpha-\Delta C(K)\geq KD\_{T}. |  |

###### Proof.

The first part of the result was shown in the discussion preceding the proposition. To prove the second part of the claim, we sell the call and hedge dynamically. Then we have h​(x)=−(x−K)+h(x)=-(x-K)\_{+}, h∗​(x)=−xh^{\*}(x)=-x, and so ℐt​(−(ST−K)+)=−St\mathcal{I}\_{t}(-(S\_{T}-K)\_{+})=-S\_{t}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt−π,h\displaystyle W\_{t}^{-\pi,h} | :=Dt−1​(w0+c0​(K))+ℐt​(−(ST−K)+)+Xt−π\displaystyle:=D\_{t}^{-1}(w\_{0}+c\_{0}(K))+\mathcal{I}\_{t}(-(S\_{T}-K)\_{+})+X\_{t}^{-\pi} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−St+𝖡𝖲C​(K,t,T,St)+Dt−1​(w0+c0​(K)−𝖡𝖲C​(K,0,T,S0)).\displaystyle\;=-S\_{t}+\mathsf{BS}^{C}(K,t,T,S\_{t})+D\_{t}^{-1}(w\_{0}+c\_{0}(K)-\mathsf{BS}^{C}(K,0,T,S\_{0})). |  |

As above, we need to compute:

|  |  |  |  |
| --- | --- | --- | --- |
|  | inft∈[0,T]s∈[0,∞){−s​Dt+Dt​𝖡𝖲C​(K,t,T,s)}\displaystyle\inf\_{\begin{subarray}{c}t\in[0,T]\\ s\in[0,\infty)\end{subarray}}\Big\{-sD\_{t}+D\_{t}\mathsf{BS}^{C}(K,t,T,s)\Big\} | =inft∈[0,T]{Dt​infs∈[0,∞)[−s+𝖡𝖲C​(K,t,T,s)]}\displaystyle=\inf\_{t\in[0,T]}\left\{D\_{t}\inf\_{s\in[0,\infty)}\left[-s+\mathsf{BS}^{C}(K,t,T,s)\right]\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inft∈[0,T]{−Dt​(K​DT​Dt−1)}\displaystyle=\inf\_{t\in[0,T]}\left\{-D\_{t}\left(KD\_{T}D\_{t}^{-1}\right)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−K​DT.\displaystyle=-KD\_{T}. |  |

The conclusion follows.
∎

The term 𝖡𝖲C​(K,0,T,K​DT)\mathsf{BS}^{C}(K,0,T,KD\_{T}) on the right-hand side of ([3.4](https://arxiv.org/html/2512.24371v1#S3.E4 "In Proposition 3.4. ‣ 3.2. European Options in the Black-Scholes-Merton model ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")) is the price of an at-the-money call option with strike KK, and by the Black-Scholes formula, we can rewrite this as K​DT​(1−2​Φ​(σ​T/2))KD\_{T}\left(1-2\Phi(\sigma\sqrt{T}/2)\right). Suppose that w0+α>0w\_{0}+\alpha>0 and the call options are underpriced. Then we can always find some small KK, K<K+​(w0+α):=(w0+α)​DT−1​(1−2​Φ​(σ​T/2))−1K<K\_{+}(w\_{0}+\alpha):=(w\_{0}+\alpha)D\_{T}^{-1}\left(1-2\Phi(\sigma\sqrt{T}/2)\right)^{-1} such that we can buy the call, and hedge dynamically to guarantee a profit. For larger strikes it will not be possible to follow this strategy unless the mis-pricing is sufficiently large. A similar behaviour is observed when the prices are too large, but now the asymmetry in the intrinsic value of the call options makes the critical strike K<K−​(w0+α):=(w0+α)​DT−1K<K\_{-}(w\_{0}+\alpha):=(w\_{0}+\alpha)D\_{T}^{-1}.

### 3.3. Consistency of market prices under constrained trading

Above, we considered only the case where single call options were traded. In reality call options at a range of strikes and maturities are available for trading, and one natural question is whether the prices are consistent. Simple model-free conditions for the absence of arbitrage are well understood, based on simple model-independent arbitrage strategies which can enforce such an arbitrage. In this section, we analyse whether these strategies are available to a trader whose strategies are subject to the admissibility criteria proposed above.

A common setup is to consider the case where call options with all strikes at a given maturity are traded. Then the prices are free of (model-independent) arbitrage only if the market prices for call options, C​(K)C(K), satisfies the conditions: *(i)* CC is convex; *(ii)* CC is decreasing; *(iii)* C​(0)=S0C(0)=S\_{0}; *(iv)* C+′​(0)≥−DTC^{\prime}\_{+}(0)\geq-D\_{T}; moreover, it is commonly assumed that also *(v)* C​(K)→0C(K)\to 0 as K→∞K\to\infty. The first two conditions can classically be enforced by simple arbitrage. In this section, we show that there exist trading strategies in 𝒱\mathcal{V}, which satistfy ([3.2](https://arxiv.org/html/2512.24371v1#S3.E2 "In 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")) for α=0\alpha=0, and generates a strictly positive wealth if any of *(i)*–*(iv)* fail. We note that *(v)* is generally more subtle; see e.g. [[11](https://arxiv.org/html/2512.24371v1#bib.bib11)], but under this further assumption (e.g. [[13](https://arxiv.org/html/2512.24371v1#bib.bib13)]), it follows that there exists a probability measure μ\mu on ℝ+\mathbb{R}\_{+} such that C​(K)=∫(x−K)+​μ​(d​x)C(K)=\int(x-K)\_{+}\,\mu(\mathrm{d}x). We consider a weaker version, which is simply to enforce positivity, which normally follows from the limiting behaviour and the decreasing property.

###### Lemma 3.5.

Suppose that 𝒫\mathcal{P} is given by 𝒫∘\mathcal{P}^{\circ}, ℐ\mathcal{I} is given by ℐ∘\mathcal{I}^{\circ}, and European call options with strike KK and maturity TT can be traded at price C​(K)C(K) at time 0. Suppose that any of *(i)* CC is convex; *(ii)* CC is decreasing; *(iii)* C​(0)=S0C(0)=S\_{0}; *(iv)* C+′​(0)≥−DTC^{\prime}\_{+}(0)\geq-D\_{T}; *(v)* CC is non-negative; fail. Then there exists a portfolio of call options with payoff g​(ST)=∑i=1kai​(ST−Ki)+g(S\_{T})=\sum\_{i=1}^{k}a\_{i}(S\_{T}-K\_{i})\_{+} and price g0=∑i=1kai​C​(Ki)g\_{0}=\sum\_{i=1}^{k}a\_{i}C(K\_{i}) with k∈ℕk\in\mathbb{N}, ai∈ℝa\_{i}\in\mathbb{R}, and ε>0\varepsilon>0 such that 𝒱​(−ε,0,g0,g)\mathcal{V}(-\varepsilon,0,g\_{0},g) is non-empty.

Note that the conclusion of the lemma, 𝒱​(−ε,0,g0,g)\mathcal{V}(-\varepsilon,0,g\_{0},g) is non-empty, is equivalently a formulation of arbitrage in our setting: that is, there exists a portfolio and trading strategy which can be setup with initial capital −ε-\varepsilon, and which will never use our ‘intrinsic capitalisation’ capacity, α\alpha, but will finish with a non-negative wealth. It is easy to check that the strategies we implement are in fact scalable, so that we can in fact find such a strategy for an arbitrary ε>0\varepsilon>0 by a simple scaling argument.

###### Proof.

Suppose that C​(K)C(K) is not convex, then there exists K1<K2<K3K\_{1}<K\_{2}<K\_{3} such that C​(K2)>λ​C​(K1)+(1−λ)​C​(K3)C(K\_{2})>\lambda C(K\_{1})+(1-\lambda)C(K\_{3}), where λ=(K3−K2)/(K3−K1)\lambda=(K\_{3}-K\_{2})/(K\_{3}-K\_{1}). Then the agent should define the function gg such that a1=λa\_{1}=\lambda, a3=(1−λ)a\_{3}=(1-\lambda), and a2=−1a\_{2}=-1.

Choose ε:=−g0=C​(K2)−λ​C​(K1)−(1−λ)​C​(K3)\varepsilon:=-g\_{0}=C(K\_{2})-\lambda C(K\_{1})-(1-\lambda)C(K\_{3}). The agent holds a portfolio of calls with positive payoff

|  |  |  |
| --- | --- | --- |
|  | g​(ST):={0ST∉(K1,K3)λ​(ST−K1)ST∈(K1,K2](1−λ)​(K3−ST)ST∈(K2,K3)g(S\_{T}):=\begin{cases}0&S\_{T}\not\in(K\_{1},K\_{3})\\ \lambda(S\_{T}-K\_{1})&S\_{T}\in(K\_{1},K\_{2}]\\ (1-\lambda)(K\_{3}-S\_{T})&S\_{T}\in(K\_{2},K\_{3})\end{cases} |  |

So we have g∗​(St)=ℐt​(g​(ST))≡0g^{\*}(S\_{t})=\mathcal{I}\_{t}(g(S\_{T}))\equiv 0 for t<Tt<T. Taking the dynamic trading strategy π\pi which is identically zero, we see that our portfolio intrinsic value is Wtπ,g=g​(ST)​𝟏t=TW\_{t}^{\pi,g}=g(S\_{T})\boldsymbol{1}\_{t=T}, which is non-negative under the assumption that CC is not convex, and hence π=∈𝒱(−ε,0,g0,g)\pi=\in\mathcal{V}(-\varepsilon,0,g\_{0},g).

The cases (ii)–(iv) are then essentially identical. For (ii) we suppose there exist K1<K2K\_{1}<K\_{2} with C​(K1)<C​(K2)C(K\_{1})<C(K\_{2}), and pursue the strategy of selling the call with strike K2K\_{2} and buying the call with strike K1K\_{1}. Then we have g​(x)=(x−K1)+−(x−K2)+g(x)=(x-K\_{1})\_{+}-(x-K\_{2})\_{+}, and so g∗​(x)=0g^{\*}(x)=0, and the result follows as above. For (iii) consider either the strategy of selling the asset and buying the call with strike 0, or selling the call with strike 0, and buying the asset. In this case we have ℐt​(ST)=St\mathcal{I}\_{t}(S\_{T})=S\_{t} and ℐt​(−ST)=−St\mathcal{I}\_{t}(-S\_{T})=-S\_{t}, and Xtπ=±(St−Dt−1​S0)X\_{t}^{\pi}=\pm(S\_{t}-D\_{t}^{-1}S\_{0}), and the conclusion follows.

For (iv), we have by (iii) a K>0K>0 such that C​(K)<S0−DT​KC(K)<S\_{0}-D\_{T}K. We sell the asset, and buy the call with strike KK. Then ℐt​((ST−K)+−ST)=(−St)∨(−DT​Dt−1​K)≥−Dt−1​DT​K\mathcal{I}\_{t}((S\_{T}-K)\_{+}-S\_{T})=(-S\_{t})\vee(-D\_{T}D\_{t}^{-1}K)\geq-D\_{t}^{-1}D\_{T}K, and so the intrinsic value of the portfolio at time tt is (−C​(K)+S0)​Dt−1+ℐt​((ST−K)+−ST)>Dt−1​DT​K−Dt−1​DT​K=0(-C(K)+S\_{0})D\_{t}^{-1}+\mathcal{I}\_{t}((S\_{T}-K)\_{+}-S\_{T})>D\_{t}^{-1}D\_{T}K-D\_{t}^{-1}D\_{T}K=0. The case (v) is trivial, we can buy the option for negative price, and hold to maturity.
∎

###### Remark 3.6.

1. (i)

   Note that some of the properties of the ℐ\mathcal{I} operator use the non-negativity of the prices process. Of course, if the asset price can go negative, then some of the conditions given can fail, e.g. in the Bachelier model.
2. (ii)

   Consider the case where *(v)* fails. Then the ‘usual’ arbitrage strategy would be to sell a call with a large strike, which should be worth very little, for approximately limK→∞C​(K)\lim\_{K\to\infty}C(K), and hedge in some way (or just not bother, the model-implied loss will happen with arbitrarily small probability). In our current setup, this will use up some of our lower constraint, since the intrinsic value of this strategy will remain as −St-S\_{t}, no matter how large KK is. In this way, we can ‘use’ spare α\alpha to generate gains, but the cost may be higher than the value of using this capacity elsewhere, depending on other elements.

## 4. Utility Maximisation in Complete Markets

In this section we consider the problem as setup in Section [3.1](https://arxiv.org/html/2512.24371v1#S3.SS1 "3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints") under the additional assumption that the trader believes in a complete market. In this case, the trader can hedge their risk, subject to the condition that the intrinsic value of their portfolio satisfies the wealth constraint, and we try to understand the impact of this on their behavior.

### 4.1. Complete Market Assumption

To make significant progress on this problem, we make the assumption that 𝒫\mathcal{P} is a singleton, and moreover, 𝒫={ℙ}\mathcal{P}=\{\mathbb{P}\}, where ℙ\mathbb{P} is a complete market. In particular, we suppose that there exists a uniformly integrable state-price density process HtH\_{t}, with Ht>0H\_{t}>0 a.s., H0=1H\_{0}=1, such that whenever YY is an ℱT\mathcal{F}\_{T}-measurable random variable with 𝔼[DT−1HT(1+|Y|)log(1+|Y|)+]<∞\mathbb{E}\left[D\_{T}^{-1}H\_{T}(1+|Y|)\log\left(1+|Y|\right)\_{+}\right]<\infty, there exists a 𝒫\mathcal{P}-admissible portfolio π\pi with 𝔼​[HT​Y]+XTπ=Y\mathbb{E}\left[H\_{T}Y\right]+X\_{T}^{\pi}=Y. In such a market, we can define as usual a risk-neutral measure ℚ\mathbb{Q}, by d​ℚd​ℙ|ℱt=Ht​Dt−1\left.\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right|\_{\mathcal{F}\_{t}}=H\_{t}D\_{t}^{-1}. Moreover it follows from our assumptions above that Ht​Dt−1H\_{t}D\_{t}^{-1} is a ℙ\mathbb{P}-martingale.

Additionally, we suppose that a (set of) traded derivatives is available. To each derivative or portfolio of derivatives, we associate a fair intrinsic price process, ℐt​(CT)\mathcal{I}\_{t}(C\_{T}). Note that by Definition [2.1](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints") we have ℐt​(CT)≤Ct:=Ht−1​𝔼​[HT​CT|ℱt]\mathcal{I}\_{t}(C\_{T})\leq C\_{t}:=H\_{t}^{-1}\mathbb{E}\left[H\_{T}C\_{T}|\mathcal{F}\_{t}\right], where CtC\_{t} is the arbitrage-free price of the derivative.

If the investor decides to take a long position in the option, her optimisation problem is:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | maximise ​𝔼​[u​(WTπ,C)], subject to ​π∈𝒱​(w0,α,c0,CT),\text{maximise }\mathbb{E}\left[u(W\_{T}^{\pi,C})\right],\;\text{ subject to }\pi\in\mathcal{V}(w\_{0},\alpha,c\_{0},C\_{T}), |  |

where Wtπ,CW\_{t}^{\pi,C} is given by ([3.2](https://arxiv.org/html/2512.24371v1#S3.E2 "In 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints")); recall Definition [3.1](https://arxiv.org/html/2512.24371v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3.1. General setup and preliminary results ‣ 3. Trading with constraints on Intrinsic Wealth ‣ Utility maximisation with model-independent constraints").

In this section, we solve this problem for specific choices of the derivative CC, and under a range of assumptions on the market measure ℙ\mathbb{P}. Our approach to this problem is based on results of [[18](https://arxiv.org/html/2512.24371v1#bib.bib18)]. In that paper the authors characterise the martingale MtM\_{t} which maximises 𝔼​[u​(MT)]\mathbb{E}\left[u(M\_{T})\right] for a concave function uu subject to the constraint that M0=0M\_{0}=0 and Mt≥JtM\_{t}\geq J\_{t} for some supermartingale JJ. (More generally, if JJ is not a supermartingale, it is trivial that JJ can be replaced by its Snell envelope, i.e. the smallest supermartingale dominating JJ). The main result of [[18](https://arxiv.org/html/2512.24371v1#bib.bib18)] says that, if the supermartingale JtJ\_{t} can be written in the form

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | Jt=𝔼​[supt≤u≤TJu∗|ℱt]J\_{t}=\mathbb{E}\left[\sup\_{t\leq u\leq T}J^{\*}\_{u}|\mathcal{F}\_{t}\right] |  |

for some adapted process J∗J^{\*}, then the martingale Mt:=𝔼​[m∨sup0≤u≤TJu∗|ℱt]M\_{t}:=\mathbb{E}\left[m\vee\sup\_{0\leq u\leq T}J^{\*}\_{u}|\mathcal{F}\_{t}\right], where mm is chosen so that M0=0M\_{0}=0, maximises 𝔼​[u​(MT)]\mathbb{E}\left[u(M\_{T})\right] for any concave function uu, over the class of all martingales starting at 0 which dominate JJ. The proof of this representation theorem can be found in [[19](https://arxiv.org/html/2512.24371v1#bib.bib19)].

Further, in [[18](https://arxiv.org/html/2512.24371v1#bib.bib18)], the authors are able to extend their results to cover the case of utility maximisation problems under certain assumptions on the form of the function uu. We adapt their arguments to apply to our setup. The main complication in the utility maximisation framework is that the expectation and the martingale properties of the wealth are taken under different probability measures (ℙ\mathbb{P} and ℚ\mathbb{Q} respectively). The aim is to put these under the same measure through an appropriate change of measure, and we require the following condition: There exists δ>1\delta>1 such that 𝔼​[HT−δ]<∞\mathbb{E}\left[H^{-\delta}\_{T}\right]<\infty.

Following [[18](https://arxiv.org/html/2512.24371v1#bib.bib18)], we suppose that our utility function is of the form u​(x)=up​(x)=x1−p1−pu(x)=u\_{p}(x)=\frac{x^{1-p}}{1-p}, where 11+δ<p<1\frac{1}{1+\delta}<p<1.

Reformulating ([4.1](https://arxiv.org/html/2512.24371v1#S4.E1 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) using the definition of Wtπ,CW\_{t}^{\pi,C} and the complete market characterisation of admissible dynamic trading strategies, our problem is to choose the ℱT\mathcal{F}\_{T}-measurable random variable XTπX\_{T}^{\pi} to maximise

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[up​(DT−1​(w0−c0)+CT+XTπ)]\mathbb{E}\left[u\_{p}(D\_{T}^{-1}(w\_{0}-c\_{0})+C\_{T}+X\_{T}^{\pi})\right] |  |

subject to 𝔼​[HT​XTπ]=0\mathbb{E}\left[H\_{T}X\_{T}^{\pi}\right]=0, DT−1​(w0−c0)+CT+XTπ≥0D\_{T}^{-1}(w\_{0}-c\_{0})+C\_{T}+X\_{T}^{\pi}\geq 0 and

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | Dt−1​(w0−c0)+ℐt​(CT)+Ht−1​𝔼​[HT​XTπ|ℱt]≥−Dt−1​α,0≤t<T.D\_{t}^{-1}(w\_{0}-c\_{0})+\mathcal{I}\_{t}(C\_{T})+H\_{t}^{-1}\mathbb{E}\left[H\_{T}X\_{T}^{\pi}|\mathcal{F}\_{t}\right]\geq-D\_{t}^{-1}\alpha,\quad 0\leq t<T. |  |

To write our problem in a form where we can apply the results of [[18](https://arxiv.org/html/2512.24371v1#bib.bib18)], we introduce

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | YT:=DT−1​(w0−c0)+CT+XTπ,Y\_{T}:=D\_{T}^{-1}(w\_{0}-c\_{0})+C\_{T}+X\_{T}^{\pi}, |  |

so 𝔼​[HT​YT]=w0+(𝔼​[HT​CT]−c0)\mathbb{E}\left[H\_{T}Y\_{T}\right]=w\_{0}+(\mathbb{E}\left[H\_{T}C\_{T}\right]-c\_{0}) if and only if 𝔼​[HT​XTπ]=0\mathbb{E}\left[H\_{T}X\_{T}^{\pi}\right]=0; recall that 𝔼​[DT−1​HT]=1\mathbb{E}\left[D\_{T}^{-1}H\_{T}\right]=1. Write also Δ​C:=(𝔼​[HT​CT]−c0)\Delta C:=(\mathbb{E}\left[H\_{T}C\_{T}\right]-c\_{0}), the difference between the hedging price (without portfolio constraints) and the market price of the option. Then, in terms of YY, ([4.3](https://arxiv.org/html/2512.24371v1#S4.E3 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) becomes

|  |  |  |
| --- | --- | --- |
|  | ℐt​(CT)+Ht−1​𝔼​[HT​YT|ℱt]−Ht−1​𝔼​[HT​CT|ℱt]≥−Dt−1​α,\mathcal{I}\_{t}(C\_{T})+H\_{t}^{-1}\mathbb{E}\left[H\_{T}Y\_{T}|\mathcal{F}\_{t}\right]-H\_{t}^{-1}\mathbb{E}\left[H\_{T}C\_{T}|\mathcal{F}\_{t}\right]\geq-D\_{t}^{-1}\alpha, |  |

or equivalently, writing

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | Yt:=Ht−1​𝔼​[HT​YT|ℱt],Y\_{t}:=H\_{t}^{-1}\mathbb{E}\left[H\_{T}Y\_{T}|\mathcal{F}\_{t}\right], |  |

we need:

|  |  |  |
| --- | --- | --- |
|  | Dt​Yt≥−α+(Dt​Ht−1)​𝔼​[HT​CT|ℱt]−Dt​ℐt​(CT),Y0=w0+Δ​C.D\_{t}Y\_{t}\geq-\alpha+(D\_{t}H\_{t}^{-1})\mathbb{E}\left[H\_{T}C\_{T}|\mathcal{F}\_{t}\right]-D\_{t}\mathcal{I}\_{t}(C\_{T}),\quad Y\_{0}=w\_{0}+\Delta C. |  |

Note in particular that (Dt​Yt)(D\_{t}Y\_{t}) is a ℚ\mathbb{Q}-martingale.

The issue now is that D​YDY is a martingale under ℚ\mathbb{Q}, while we maximise under the probability ℙ\mathbb{P}. To get around this difficulty we introduce a new measure ℚ¯\overline{\mathbb{Q}} under which the two conditions can be understood for the same measure. For this purpose, we define (ξ⋅)(\xi\_{\cdot}) by

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | ξT:=HT−1p𝔼​[HT1−1p],ξt:=Ht−1​𝔼​[ξT​HT|ℱt].\xi\_{T}:=\frac{H\_{T}^{-\frac{1}{p}}}{\mathbb{E}\left[H\_{T}^{1-\frac{1}{p}}\right]},\quad\xi\_{t}:=H\_{t}^{-1}\mathbb{E}\left[\xi\_{T}H\_{T}|\mathcal{F}\_{t}\right]. |  |

Then ξ0=1\xi\_{0}=1, ξt​Ht\xi\_{t}H\_{t} is a ℙ\mathbb{P}-martingale, and we can define a change of measure d​ℚ¯d​ℙ=ξT​HT\frac{\mathrm{d}\overline{\mathbb{Q}}}{\mathrm{d}\mathbb{P}}=\xi\_{T}H\_{T}.

###### Lemma 4.1.

Under ℚ¯\overline{\mathbb{Q}}, with utility function u=upu=u\_{p}, the problem ([4.1](https://arxiv.org/html/2512.24371v1#S4.E1 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) is equivalent to the problem:

|  |  |  |
| --- | --- | --- |
|  | maximise ​𝔼ℚ¯​[up​(Y¯T)],\text{maximise }\mathbb{E}^{\overline{\mathbb{Q}}}\left[u\_{p}(\overline{Y}\_{T})\right], |  |

subject to

|  |  |  |  |
| --- | --- | --- | --- |
| (4.7) |  | {Y¯ is a non-negative ℚ¯-martingale,Y¯0=w0+Δ​C,Y¯t≥−α​ξt−1​Dt−1−ξt−1​ℐt​(CT)+𝔼ℚ¯​[CT​ξT−1|ℱt].\begin{cases}\overline{Y}&\text{ is a non-negative $\overline{\mathbb{Q}}$-martingale},\\ \overline{Y}\_{0}&=w\_{0}+\Delta C,\\ \overline{Y}\_{t}&\geq-\alpha\xi\_{t}^{-1}D\_{t}^{-1}-\xi\_{t}^{-1}\mathcal{I}\_{t}(C\_{T})+\mathbb{E}^{\overline{\mathbb{Q}}}\left[C\_{T}\xi\_{T}^{-1}|\mathcal{F}\_{t}\right].\end{cases} |  |

Moreover, the optimal terminal wealth WTπ,CW\_{T}^{\pi,C} can be recovered by WTπ,C=ξT​Y¯TW\_{T}^{\pi,C}=\xi\_{T}\overline{Y}\_{T}, where Y¯T\overline{Y}\_{T} is the optimiser for the problem above.

###### Proof.

Let XTπX\_{T}^{\pi} be a candidate solution to ([4.1](https://arxiv.org/html/2512.24371v1#S4.E1 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")), so 𝔼​[HT​XTπ]=0\mathbb{E}\left[H\_{T}X\_{T}^{\pi}\right]=0 and WTπ,C=DT−1​(w0−c0)+CT+XTπ≥0W\_{T}^{\pi,C}=D\_{T}^{-1}(w\_{0}-c\_{0})+C\_{T}+X\_{T}^{\pi}\geq 0. Then, from ([4.4](https://arxiv.org/html/2512.24371v1#S4.E4 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[up​(DT−1​(w0−c0)+CT+XTπ)]=𝔼​[up​(YT)].\mathbb{E}\left[u\_{p}(D\_{T}^{-1}(w\_{0}-c\_{0})+C\_{T}+X\_{T}^{\pi})\right]=\mathbb{E}\left[u\_{p}(Y\_{T})\right]. |  |

Define Y¯t=Yt​ξt−1\overline{Y}\_{t}=Y\_{t}\xi\_{t}^{-1}; see ([4.5](https://arxiv.org/html/2512.24371v1#S4.E5 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")). Then 𝔼ℚ¯​[Y¯T|ℱt]=(ξt​Ht)−1​𝔼​[YT​ξT−1​HT​ξT|ℱt]=Yt​ξt−1=Y¯t\mathbb{E}^{\overline{\mathbb{Q}}}\left[\overline{Y}\_{T}|\mathcal{F}\_{t}\right]=(\xi\_{t}H\_{t})^{-1}\mathbb{E}\left[Y\_{T}\xi^{-1}\_{T}H\_{T}\xi\_{T}|\mathcal{F}\_{t}\right]=Y\_{t}\xi\_{t}^{-1}=\overline{Y}\_{t}. In particular, Y¯\overline{Y} is a ℚ¯\overline{\mathbb{Q}}-martingale, and Y¯T≥0\overline{Y}\_{T}\geq 0, hence Y¯\overline{Y} is a non-negative martingale.

On the other hand, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[up​(YT)]\displaystyle\mathbb{E}\left[u\_{p}(Y\_{T})\right] | =𝔼​[YT1−p1−p]\displaystyle=\mathbb{E}\left[\frac{Y\_{T}^{1-p}}{1-p}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ¯​[(HT​ξT)−1​(Y¯T​ξT)1−p1−p]\displaystyle=\mathbb{E}^{\overline{\mathbb{Q}}}\left[(H\_{T}\xi\_{T})^{-1}\frac{(\overline{Y}\_{T}\xi\_{T})^{1-p}}{1-p}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ¯​[ξT−pHT​up​(Y¯T)]\displaystyle=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\frac{\xi\_{T}^{-p}}{H\_{T}}u\_{p}(\overline{Y}\_{T})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(𝔼​[HT1−1p])p​𝔼ℚ¯​[up​(Y¯T)].\displaystyle=\left(\mathbb{E}\left[H\_{T}^{1-\frac{1}{p}}\right]\right)^{p}\mathbb{E}^{\overline{\mathbb{Q}}}\left[u\_{p}(\overline{Y}\_{T})\right]. |  |

Moreover, the constraints on the lower bound and the initial value of Y¯\overline{Y} follow immediately. As a consequence, any feasible solution YY to the first problem gives rise to a feasible solution Y¯\overline{Y} to the second problem, and the corresponding values differ only by a positive constant multiple. A similar conclusion can be obtained starting with a feasible solution Y¯\overline{Y} to ([4.7](https://arxiv.org/html/2512.24371v1#S4.E7 "In Lemma 4.1. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")), and building a candidate solution to ([4.1](https://arxiv.org/html/2512.24371v1#S4.E1 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")). Since the market is complete, the arbitrage free price and the replication strategy of any contingent claim are uniquely determined, and hence there exists an admissible dynamic trading strategy π\pi such that the ℚ\mathbb{Q}-martingale Dt​XtπD\_{t}X\_{t}^{\pi} replicates the contingent claim DT​ξT​Y¯T−DT​CT−(w0−c0)D\_{T}\xi\_{T}\overline{Y}\_{T}-D\_{T}C\_{T}-(w\_{0}-c\_{0}).
∎

###### Remark 4.2.

Note that the intrinsic wealth constraint process

|  |  |  |  |
| --- | --- | --- | --- |
| (4.8) |  | ζt:=−α​Dt−1​ξt−1−ξt−1​ℐt​(CT)+𝔼ℚ¯​[ξT−1​CT|ℱt]\zeta\_{t}:=-\alpha D\_{t}^{-1}\xi\_{t}^{-1}-\xi\_{t}^{-1}\mathcal{I}\_{t}(C\_{T})+\mathbb{E}^{\overline{\mathbb{Q}}}\left[\xi\_{T}^{-1}C\_{T}|\mathcal{F}\_{t}\right] |  |

is a ℚ¯\overline{\mathbb{Q}}-supermartingale. To see this, we observe that d​ℚ¯d​ℚ=DT​ξT\frac{\mathrm{d}\overline{\mathbb{Q}}}{\mathrm{d}\mathbb{Q}}=D\_{T}\xi\_{T}, so (Dt−1​ξt−1)(D\_{t}^{-1}\xi\_{t}^{-1}) is a ℚ¯\overline{\mathbb{Q}}-martingale, and (Dt​ℐt​(CT))(D\_{t}\mathcal{I}\_{t}(C\_{T})) is a ℚ\mathbb{Q}-submartingale by the assumption that ℐt​(CT)\mathcal{I}\_{t}(C\_{T}) is a fair intrinsic wealth process, so also (ξt−1​ℐt​(CT))(\xi\_{t}^{-1}\mathcal{I}\_{t}(C\_{T})) is a ℚ¯\overline{\mathbb{Q}}-submartingale.

More generally, we can reformulate the conditions in Lemma [4.1](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") that (Y¯)t≤T(\overline{Y})\_{t\leq T} is a non-negative ℚ¯\overline{\mathbb{Q}}-martingale such that Y¯t≥ζt\overline{Y}\_{t}\geq\zeta\_{t} for t≤Tt\leq T in terms of the process

|  |  |  |
| --- | --- | --- |
|  | ζt0:={ζtt<T0t=T.\zeta\_{t}^{0}:=\begin{cases}\zeta\_{t}&t<T\\ 0&t=T\end{cases}. |  |

Specifically, since ζT=−α​DT−1​ξT−1<0\zeta\_{T}=-\alpha D\_{T}^{-1}\xi\_{T}^{-1}<0, the requirement that Y¯\overline{Y} is non-negative and greater than ζt\zeta\_{t} is equivalent to requiring that the process Y¯\overline{Y} is greater than ζ0\zeta^{0}, and further, equivalently, that it is greater than the Snell envelope of ζ0\zeta^{0}, which we denote by ζ∗\zeta^{\*}.

###### Assumption 4.3.

The process ζ∗\zeta^{\*} is a supermartingale of class (𝒟)({\mathcal{D}}) upper semi-continuous in expectation which admits the decomposition in terms of an optional, upper-right semi-continuous process JuζJ\_{u}^{\zeta}, with JTζ=0J\_{T}^{\zeta}=0, as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.9) |  | ζt∗=𝔼ℚ¯​[supt≤u≤TJuζ|ℱt].\zeta\_{t}^{\*}=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{t\leq u\leq T}J\_{u}^{\zeta}|\mathcal{F}\_{t}\right]. |  |

By [[3](https://arxiv.org/html/2512.24371v1#bib.bib3), Theorem 2.9], we have that the representation in ([4.9](https://arxiv.org/html/2512.24371v1#S4.E9 "In Assumption 4.3. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) can be obtained for process ζ∗\zeta^{\*}. Observe that, following [[18](https://arxiv.org/html/2512.24371v1#bib.bib18)] and [[19](https://arxiv.org/html/2512.24371v1#bib.bib19)], in order to obtain this representation
it is sufficient that the filtration {ℱt}\{\mathcal{F}\_{t}\} is quasi-left-continuous.

###### Theorem 4.4.

Suppose that u=upu=u\_{p}, ℐt​(CT)\mathcal{I}\_{t}(C\_{T}) is a fair intrinsic price process and Assumption [4.3](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") holds. Then there exists a feasible solution to ([4.1](https://arxiv.org/html/2512.24371v1#S4.E1 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) if and only if

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ¯​[sup0≤u≤TJuζ]≤w0+Δ​C.\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{0\leq u\leq T}J\_{u}^{\zeta}\right]\leq w\_{0}+\Delta C. |  |

When this condition holds, the optimal terminal wealth WTπW\_{T}^{\pi} solving ([4.1](https://arxiv.org/html/2512.24371v1#S4.E1 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) is given by

|  |  |  |
| --- | --- | --- |
|  | WTπ=ξT​[(sup0≤u≤TJuζ)∨M],W\_{T}^{\pi}=\xi\_{T}\left[\left(\sup\_{0\leq u\leq T}J\_{u}^{\zeta}\right)\vee M\right], |  |

where MM is chosen such that 𝔼ℚ¯​[(sup0≤u≤TJuζ)∨M]=w0+Δ​C\mathbb{E}^{\overline{\mathbb{Q}}}\left[\left(\sup\_{0\leq u\leq T}J\_{u}^{\zeta}\right)\vee M\right]=w\_{0}+\Delta C.

###### Proof.

Under Assumption [4.3](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"), it is immediate that ζ¯t:=𝔼ℚ¯​[sup0≤u≤TJuζ|ℱt]\overline{\zeta}\_{t}:=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{0\leq u\leq T}J\_{u}^{\zeta}|\mathcal{F}\_{t}\right] is a non-negative martingale which dominates ζ∗\zeta^{\*}. Moreover, it is the smallest such martingale.

In particular, if ζ¯0≤w0+Δ​C\overline{\zeta}\_{0}\leq w\_{0}+\Delta C, then there exists a process Y¯\overline{Y} which is feasible for ([4.7](https://arxiv.org/html/2512.24371v1#S4.E7 "In Lemma 4.1. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")). Moreover, since any admissible wealth process gives rise (via the arguments of Lemma [4.1](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) to a non-negative martingale which dominates ζ∗\zeta^{\*}, this is also a necessary condition. The result now follows immediately from [[19](https://arxiv.org/html/2512.24371v1#bib.bib19), Theorem 5.2] 222Note that there is a typographical error in the first bullet point on p.685 of [[19](https://arxiv.org/html/2512.24371v1#bib.bib19)], and this point is not in general correct: in our notation, the choice of MM will in general be less than w0+Δ​Cw\_{0}+\Delta C; we do not usually expect equality except in special cases.
∎

It is now straightforward to deduce the form of the optimal π\pi, using classical methods, see for example [[23](https://arxiv.org/html/2512.24371v1#bib.bib23), Theorem 6.3, Corollary 6.5].

### 4.2. Long position in Call options

In this section we consider the case where the derivative position is a long position in call options. Specifically, we suppose that the agent purchased λ>0\lambda>0 units of a call option with strike KK. As we will see, in this case the form of the optimal terminal wealth can be identified.

We first consider the fair (replication) price of a call option with strike KK at time tt, given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht−1​𝔼​[HT​(ST−K)+|ℱt]\displaystyle H\_{t}^{-1}\mathbb{E}\left[H\_{T}(S\_{T}-K)\_{+}|\mathcal{F}\_{t}\right] | =ξt​𝔼ℚ¯​[ξT−1​(ST−K)+|ℱt]\displaystyle=\xi\_{t}\mathbb{E}^{\overline{\mathbb{Q}}}\left[\xi\_{T}^{-1}(S\_{T}-K)\_{+}|\mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Dt−1​𝔼ℚ​[DT​(ST−K)+|ℱt].\displaystyle=D\_{t}^{-1}\mathbb{E}^{\mathbb{Q}}\left[D\_{T}(S\_{T}-K)\_{+}|\mathcal{F}\_{t}\right]. |  |

In addition, from Example [2.2](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem2 "Example 2.2. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints")([i](https://arxiv.org/html/2512.24371v1#S2.I2.i1 "item i ‣ Example 2.2. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints")), we know that ℐt​(λ​(ST−K)+)=λ​(St−K​DTDt)+\mathcal{I}\_{t}(\lambda(S\_{T}-K)\_{+})=\lambda\left(S\_{t}-K\frac{D\_{T}}{D\_{t}}\right)\_{+}, and so:

|  |  |  |
| --- | --- | --- |
|  | ζt=Dt−1​ξt−1​[−α−λ​(St​Dt−K​DT)++λ​𝔼ℚ​[(ST​DT−K​DT)+|ℱt]].\displaystyle\zeta\_{t}=D\_{t}^{-1}\xi\_{t}^{-1}\left[-\alpha-\lambda(S\_{t}D\_{t}-KD\_{T})\_{+}+\lambda\mathbb{E}^{\mathbb{Q}}\left[(S\_{T}D\_{T}-KD\_{T})\_{+}|\mathcal{F}\_{t}\right]\right]. |  |

Observing that StD:=Dt​StS\_{t}^{D}:=D\_{t}S\_{t} is a ℚ\mathbb{Q}-martingale, and writing KD:=DT​KK^{D}:=D\_{T}K, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.10) |  | ζt=λ​ξt−1​Dt−1​(𝔼ℚ​[LTSD,KD−LtSD,KD|ℱt]−αλ)\zeta\_{t}=\lambda\xi\_{t}^{-1}D\_{t}^{-1}\left(\mathbb{E}^{\mathbb{Q}}\left[L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}|\mathcal{F}\_{t}\right]-\frac{\alpha}{\lambda}\right) |  |

where LSD,KDL^{S^{D},K^{D}} is the local time of the process SDS^{D} at the level KDK^{D}. Recalling again that d​ℚ¯d​ℚ=DT​ξT\frac{\mathrm{d}\overline{\mathbb{Q}}}{\mathrm{d}\mathbb{Q}}=D\_{T}\xi\_{T}, we can also write

|  |  |  |
| --- | --- | --- |
|  | ζt=𝔼ℚ¯​[(λ​(LTSD,KD−LtSD,KD)−α)​ξT−1​DT−1|ℱt].\zeta\_{t}=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\left(\lambda\left(L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)-\alpha\right)\xi\_{T}^{-1}D\_{T}^{-1}|\mathcal{F}\_{t}\right]. |  |

Let us introduce ϕt:=ξt−1​Dt−1\phi\_{t}:=\xi\_{t}^{-1}D\_{t}^{-1}, so we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | (LTSD,KD−LtSD,KD)​ϕT\displaystyle\left(L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\phi\_{T} | =(LTSD,KD−LtSD,KD)​ϕt+∫tTdLsSD,KD​∫tTdϕs\displaystyle=\left(L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\phi\_{t}+\int\_{t}^{T}\mathrm{d}L\_{s}^{S^{D},K^{D}}\int\_{t}^{T}\mathrm{d}\phi\_{s} |  |

and by integration by parts,

|  |  |  |
| --- | --- | --- |
|  | ∫tTdLsSD,KD​∫tTdϕs\displaystyle\int\_{t}^{T}\mathrm{d}L\_{s}^{S^{D},K^{D}}\int\_{t}^{T}\mathrm{d}\phi\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tT(ϕs−ϕt)​dLsSD,KD+∫tT(LsSD,KD−LtSD,KD)​dϕs\displaystyle\quad=\int\_{t}^{T}(\phi\_{s}-\phi\_{t})\,\mathrm{d}L\_{s}^{S^{D},K^{D}}+\int\_{t}^{T}\left(L\_{s}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\,\mathrm{d}\phi\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tTϕs​dLsSD,KD−(LTSD,KD−LtSD,KD)​ϕt+∫tT(LsSD,KD−LtSD,KD)​dϕs\displaystyle\quad=\int\_{t}^{T}\phi\_{s}\,\mathrm{d}L\_{s}^{S^{D},K^{D}}-\left(L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\phi\_{t}+\int\_{t}^{T}\left(L\_{s}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\,\mathrm{d}\phi\_{s} |  |

and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | (LTSD,KD−LtSD,KD)​ϕT\displaystyle\left(L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\phi\_{T} | =∫tTϕs​dLsSD,KD+∫tT(LsSD,KD−LtSD,KD)​dϕs.\displaystyle=\int\_{t}^{T}\phi\_{s}\,\mathrm{d}L\_{s}^{S^{D},K^{D}}+\int\_{t}^{T}\left(L\_{s}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\,\mathrm{d}\phi\_{s}. |  |

Since ϕ\phi is a ℚ¯\overline{\mathbb{Q}}-martingale, it follows that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ¯​[(LTSD,KD−LtSD,KD)​ϕT|ℱt]=𝔼ℚ¯​[∫tTϕs​dLsSD,KD|ℱt].\displaystyle\mathbb{E}^{\overline{\mathbb{Q}}}\left[\left(L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}\right)\phi\_{T}|\mathcal{F}\_{t}\right]=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\int\_{t}^{T}\phi\_{s}\mathrm{d}L\_{s}^{S^{D},K^{D}}|\mathcal{F}\_{t}\right]. |  |

To say more about the optimal strategy in this framework, we then make the following assumption:

###### Assumption 4.5.

Suppose that SS is a time-homogenous, Markov processes under ℚ¯\overline{\mathbb{Q}}, and there exists a measurable function ϕ​(u)\phi(u) such that ϕu=ϕ​(u)\phi\_{u}=\phi(u) when SuD=KDS\_{u}^{D}=K^{D}. That is, ξt​Dt\xi\_{t}D\_{t} does not depend on the past of the process when the discounted price and the discounted strike are equal.

Below we will see that this assumption holds for the case of a
Black-Scholes-Merton model. In particular, it follows from Assumption [4.5](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem5 "Assumption 4.5. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") that

|  |  |  |
| --- | --- | --- |
|  | ρ​(t):={𝔼ℚ¯​[∫tTϕs​dLsSD,KD|StD=KD],t<T−∞,t≥T\displaystyle\rho(t):=\begin{cases}\mathbb{E}^{\overline{\mathbb{Q}}}\left[\int\_{t}^{T}\phi\_{s}\,\mathrm{d}L\_{s}^{S^{D},K^{D}}|S\_{t}^{D}=K^{D}\right],\quad&t<T\\ -\infty,&t\geq T\end{cases} |  |

is well defined.

###### Theorem 4.6.

Suppose that Assumption [4.5](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem5 "Assumption 4.5. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") holds, and in addition, ϕ\phi is a Markov process and

|  |  |  |  |
| --- | --- | --- | --- |
| (4.11) |  | z​(u;λ):=λ​ρ​(u)−α​ϕ​(u)\displaystyle z(u;\lambda):=\lambda\rho(u)-\alpha\phi(u) |  |

is decreasing in uu, for u∈[0,T]u\in[0,T]. Then the process JζJ^{\zeta} involved in the representation of ζ∗\zeta^{\*} in ([4.9](https://arxiv.org/html/2512.24371v1#S4.E9 "In Assumption 4.3. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")), the Snell envelope of ζ0\zeta^{0},
is given by

|  |  |  |
| --- | --- | --- |
|  | Juζ={z​(u;λ)SuD=KD0u=T−∞ otherwise,\displaystyle J\_{u}^{\zeta}=\begin{cases}z(u;\lambda)&S\_{u}^{D}=K^{D}\\ 0&u=T\\ -\infty&\text{ otherwise},\end{cases} |  |

and so

|  |  |  |
| --- | --- | --- |
|  | sup0≤u≤TJuζ={z​(HKD;λ)∨0HKD<T0T∧HKD=T.\displaystyle\sup\_{0\leq u\leq T}J\_{u}^{\zeta}=\begin{cases}z(H\_{K^{D}};\lambda)\vee 0&\quad H\_{K^{D}}<T\\ 0&\quad T\wedge H\_{K^{D}}=T.\end{cases} |  |

###### Proof.

Recall that the process ζ\zeta is defined in ([4.8](https://arxiv.org/html/2512.24371v1#S4.E8 "In Remark 4.2. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")), and consider the process JζJ^{\zeta} defined above.
We first note that the process ζ\zeta can be described as follows. Considering first t=Tt=T, we see immediately that ζT=−α​ϕT\zeta\_{T}=-\alpha\phi\_{T}. In addition, for t<Tt<T, define the stopping time

|  |  |  |  |
| --- | --- | --- | --- |
| (4.12) |  | HKDt:=inf{s≥t:SsD=KD},H\_{K^{D}}^{t}:=\inf\{s\geq t:S\_{s}^{D}=K^{D}\}, |  |

then (ζs∧HKDt)s∈[t,T](\zeta\_{s\wedge H\_{K^{D}}^{t}})\_{s\in[t,T]} is a martingale, and ζt=𝔼ℚ¯​[ζT∧HKDt]\zeta\_{t}=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\zeta\_{T\wedge H\_{K^{D}}^{t}}\right].
Now, observe that ζHKD=z​(HKD;λ)\zeta\_{H\_{K^{D}}}=z(H\_{K^{D}};\lambda) when HKD<TH\_{K^{D}}<T.
Since ζHKD∗≥ζHKD\zeta^{\*}\_{H\_{K^{D}}}\geq\zeta\_{H\_{K^{D}}}, we have that,

|  |  |  |
| --- | --- | --- |
|  | ζHKD∗≥𝔼ℚ¯​[supHKD≤u≤TJuζ|ℱHKD]=ζHKD∨0=z​(HKD;λ)∨0,\zeta^{\*}\_{H\_{K^{D}}}\geq\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{{H\_{K^{D}}}\leq u\leq T}J\_{u}^{\zeta}|\mathcal{F}\_{H\_{K^{D}}}\right]=\zeta\_{{H\_{K^{D}}}}\vee 0=z(H\_{K^{D}};\lambda)\vee 0, |  |

when HKD<TH\_{K^{D}}<T. It follows that

|  |  |  |
| --- | --- | --- |
|  | ζ0∗≥𝔼ℚ¯​[(ζHKD∗∨0)​𝟏HKD<T]≥𝔼ℚ¯​[sup0≤u≤TJuζ].\zeta^{\*}\_{0}\geq\mathbb{E}^{\overline{\mathbb{Q}}}\left[\left(\zeta^{\*}\_{H\_{K^{D}}}\vee 0\right)\boldsymbol{1}\_{H\_{K^{D}}<T}\right]\geq\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{0\leq u\leq T}J\_{u}^{\zeta}\right]. |  |

On the other hand, by construction, 𝔼ℚ¯​[supt≤u≤TJuζ|ℱt]\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{t\leq u\leq T}J\_{u}^{\zeta}|\mathcal{F}\_{t}\right] is a non-negative supermartingale dominating ζt\zeta\_{t}, from which we conclude

|  |  |  |
| --- | --- | --- |
|  | ζt∗=𝔼ℚ¯​[supt≤u≤TJuζ|ℱt],\zeta\_{t}^{\*}=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{t\leq u\leq T}J\_{u}^{\zeta}|\mathcal{F}\_{t}\right], |  |

as required.

∎

###### Remark 4.7.

The assumption that zz is decreasing is necessary to get an explicit expression. In general, we would expect the process JζJ^{\zeta} to take a similar form, but it would no longer be the case that sup0≤u≤TJuζ=z​(HKD;λ)∨0\sup\_{0\leq u\leq T}J\_{u}^{\zeta}=z(H\_{K^{D}};\lambda)\vee 0, and rather, the right-hand side would be a maximum over all possible return times to the level KDK^{D}. In this case, we would expect the function zz at time uu to then only be defined recursively in terms of an expression involving its future values, {z​(s;λ),s∈(u,T]}\{z(s;\lambda),s\in(u,T]\}.

Next result is in fact a special case of the previous more general
result.

###### Corollary 4.8.

Suppose that Assumption [4.5](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem5 "Assumption 4.5. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") holds, α=0\alpha=0, and the function ρ​(t)\rho(t) is strictly positive and decreasing. Then, we have

|  |  |  |
| --- | --- | --- |
|  | sup0≤u≤TJuζ=λ​ρ​(HKD)∨0\displaystyle\sup\_{0\leq u\leq T}J\_{u}^{\zeta}=\lambda\rho(H\_{K^{D}})\vee 0 |  |

where HKD:=inf{t≥0:SuD=KD}H\_{K^{D}}:=\inf\{t\geq 0:S\_{u}^{D}=K^{D}\}.

###### Proof.

Taking z​(u,λ)=λ​ρ​(u)z(u,\lambda)=\lambda\rho(u), and using the fact that ρ\rho is decreasing and strictly positive, the result follows from the expression for JuζJ^{\zeta}\_{u}, taking α=0\alpha=0, since the maximum of this process within the interval [t,T][t,T] will be achieved at the valuation in the left limit tt.
∎

### 4.3. Long positions in Call options in the Black-Scholes-Merton model

We now restrict ourselves to the standard setting of the Black-Scholes-Merton model, so that Dt=e−r​tD\_{t}=\mathrm{e}^{-rt}, d​St=σ​St​d​Bt+μ​St​d​t\mathrm{d}S\_{t}=\sigma S\_{t}\mathrm{d}B\_{t}+\mu S\_{t}\mathrm{d}t, for fixed constants σ,r,μ\sigma,r,\mu, where BtB\_{t} is a ℙ\mathbb{P}-Brownian motion. In this model, we know that

|  |  |  |
| --- | --- | --- |
|  | Ht=exp⁡{−θ​Bt−(12​θ2+r)​t},H\_{t}=\exp\left\{-\theta B\_{t}-\left(\dfrac{1}{2}\theta^{2}+r\right)t\right\}, |  |

where θ=μ−rσ\theta=\frac{\mu-r}{\sigma}, the Sharpe ratio.

Using the fact that ξT=HT−1p​(𝔼​[HT1−1p])−1\xi\_{T}=H\_{T}^{-\frac{1}{p}}\left(\mathbb{E}\left[H\_{T}^{1-\frac{1}{p}}\right]\right)^{-1}, and Ht​ξtH\_{t}\xi\_{t} is a ℙ\mathbb{P}-martingale, one can further see that

|  |  |  |
| --- | --- | --- |
|  | ξt=exp⁡{θp​Bt+r​t+12​θ2​(2​p−1−p−2)​t},\xi\_{t}=\exp\left\{\frac{\theta}{p}B\_{t}+rt+\dfrac{1}{2}\theta^{2}(2p^{-1}-p^{-2})t\right\}, |  |

and therefore

|  |  |  |  |
| --- | --- | --- | --- |
| (4.13) |  | ϕt−1=Dt​ξt=exp⁡{θp​Btℚ−12​θ2p2​t},\displaystyle\phi\_{t}^{-1}=D\_{t}\xi\_{t}=\exp\left\{\frac{\theta}{p}B\_{t}^{\mathbb{Q}}-\dfrac{1}{2}\frac{\theta^{2}}{p^{2}}t\right\}, |  |

where Btℚ:=Bt+θ​tB\_{t}^{\mathbb{Q}}:=B\_{t}+\theta t is a ℚ\mathbb{Q}-Brownian motion. It follows that StD=KDS\_{t}^{D}=K^{D} if and only if:

|  |  |  |  |
| --- | --- | --- | --- |
|  | KD\displaystyle K^{D} | =S0​exp⁡{σ​Btℚ−12​σ2​t}\displaystyle=S\_{0}\exp\left\{\sigma B\_{t}^{\mathbb{Q}}-\dfrac{1}{2}\sigma^{2}t\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.14) |  | ⇔Btℚ\displaystyle\iff B\_{t}^{\mathbb{Q}} | =1σ​[ln⁡(KDS0)+12​σ2​t]\displaystyle=\frac{1}{\sigma}\left[\ln\left(\frac{K^{D}}{S\_{0}}\right)+\dfrac{1}{2}\sigma^{2}t\right] |  |

and hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(t)\displaystyle\phi(t) | =exp⁡{−θp​1σ​[ln⁡(KDS0)+12​σ2​t]+12​θ2p2​t}\displaystyle=\exp\left\{-\frac{\theta}{p}\frac{1}{\sigma}\left[\ln\left(\frac{K^{D}}{S\_{0}}\right)+\dfrac{1}{2}\sigma^{2}t\right]+\dfrac{1}{2}\frac{\theta^{2}}{p^{2}}t\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(S0KD)θσ​p​exp⁡{θ2​p2​(θ−σ​p)​t}.\displaystyle=\left(\frac{S\_{0}}{K^{D}}\right)^{\frac{\theta}{\sigma p}}\exp\left\{\frac{\theta}{2p^{2}}\left(\theta-\sigma p\right)t\right\}. |  |

Note that it follows that Assumption [4.5](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem5 "Assumption 4.5. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") holds, and moreover ϕ\phi is decreasing in tt if θ>0\theta>0 and p​σ>θp\sigma>\theta.

Using from above the fact that d​ℚ¯d​ℚ=DT​ξT\frac{\mathrm{d}\overline{\mathbb{Q}}}{\mathrm{d}\mathbb{Q}}=D\_{T}\xi\_{T}, which is given by ([4.13](https://arxiv.org/html/2512.24371v1#S4.E13 "In 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")), we also see from Girsanov’s Theorem that Btℚ¯:=Btℚ−θp​tB\_{t}^{\overline{\mathbb{Q}}}:=B\_{t}^{\mathbb{Q}}-\frac{\theta}{p}t is a ℚ¯\overline{\mathbb{Q}}-Brownian motion.

In addition, using the Black-Scholes formula, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[LTSD,KD−LtSD,KD|ℱt]=(Φ​(d1)​StD−Φ​(d1−σ​T−t)​KD)−(StD−KD)+\mathbb{E}^{\mathbb{Q}}\left[L\_{T}^{S^{D},K^{D}}-L\_{t}^{S^{D},K^{D}}|\mathcal{F}\_{t}\right]=\left(\Phi(d\_{1})S\_{t}^{D}-\Phi(d\_{1}-\sigma\sqrt{T-t})K^{D}\right)-(S\_{t}^{D}-K^{D})\_{+} |  |

where d1=(log⁡(StDKD)+σ2​T−t/2)/(σ​T−t)d\_{1}=\left(\log\left(\frac{S\_{t}^{D}}{K^{D}}\right)+\sigma^{2}\sqrt{T-t}/2\right)/(\sigma\sqrt{T-t}), and it follows from the argument used to derive ([4.10](https://arxiv.org/html/2512.24371v1#S4.E10 "In 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) that

|  |  |  |
| --- | --- | --- |
|  | ρ​(t)=ϕ​(t)​KD​(2​Φ​(12​σ​T−t)−1).\rho(t)=\phi(t)K^{D}\left(2\Phi\left(\dfrac{1}{2}\sigma\sqrt{T-t}\right)-1\right). |  |

From the fact that ϕ\phi is decreasing, we deduce that Theorem [4.6](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem6 "Theorem 4.6. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")
holds when θ>0\theta>0 and p​σ>θp\sigma>\theta, since in this case z​(⋅;λ)z(\cdot;\lambda), defined by ([4.11](https://arxiv.org/html/2512.24371v1#S4.E11 "In Theorem 4.6. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")), is decreasing. This last fact follows from the following observation, using the previous display.

|  |  |  |  |
| --- | --- | --- | --- |
|  | z​(u;λ)=\displaystyle z(u;\lambda)= | λ​ρ​(u)−α​ϕ​(u)\displaystyle\lambda\rho(u)-\alpha\phi(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −α​ϕ​(u)​[1−λ​KDα​(2​Φ​(12​σ​T−u)−1)]\displaystyle-\alpha\phi(u)\left[1-\frac{\lambda K^{D}}{\alpha}\left(2\Phi(\frac{1}{2}\sigma\sqrt{T-u})-1\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =:\displaystyle=: | −α​ϕ​(u)​g​(u),\displaystyle-\alpha\phi(u)g(u), |  |

with g​(T)=1g(T)=1, g​(0)<1g(0)<1 and g′​(u)>0g^{\prime}(u)>0, for 0<u<T0<u<T. The functions ρ,ϕ\rho,\phi and zz are shown in Figures [1](https://arxiv.org/html/2512.24371v1#S4.F1 "Figure 1 ‣ 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") and [2](https://arxiv.org/html/2512.24371v1#S4.F2 "Figure 2 ‣ 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints").

![Refer to caption](x1.png)


Figure 1.  Plots of the functions ρ\rho and ϕ\phi in the case of the Black-Scholes-Merton model. In this example, ρ\rho represents the additional cost of hedging that needs to be held when StD=KDS\_{t}^{D}=K^{D}, ϕ\phi is the value of the process ϕt\phi\_{t} along the same line.

![Refer to caption](x2.png)


Figure 2.  The plot above shows the function z​(t,λ)z(t,\lambda). The level zz represents the value of the process JζJ^{\zeta} which we will score when we hit the line StD=KDS\_{t}^{D}=K^{D} in order to get the correct form of the process defined in ([4.9](https://arxiv.org/html/2512.24371v1#S4.E9 "In Assumption 4.3. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")).

For y≠xy\neq x, β∈ℝ\beta\in\mathbb{R}, and for a standard Brownian motion BB with B0=0B\_{0}=0, we introduce the hitting time

|  |  |  |
| --- | --- | --- |
|  | Hyβ:=inf{t≥0:x+Bt=y+β​t}\displaystyle H\_{y}^{\beta}:=\inf\{t\geq 0:x+B\_{t}=y+\beta t\} |  |

and define the densities γ0,γ1β,γ2β\gamma\_{0},\gamma\_{1}^{\beta},\gamma\_{2}^{\beta} by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(x+Bt∈A)\displaystyle\mathbb{P}(x+B\_{t}\in A) | =∫Aγ0​(v,t,x)​dv\displaystyle=\int\_{A}\gamma\_{0}(v,t,x)\,\mathrm{d}v |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.15) |  | ℙ​(Hyβ<t)\displaystyle\mathbb{P}(H\_{y}^{\beta}<t) | =∫0tγ1β​(u,x,y)​du\displaystyle=\int\_{0}^{t}\gamma\_{1}^{\beta}(u,x,y)\,\mathrm{d}u |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.16) |  | ℙ​(Hyβ>t,x+Bt∈A)\displaystyle\mathbb{P}(H\_{y}^{\beta}>t,x+B\_{t}\in A) | =∫Aγ2β​(v,t,x,y)​dv\displaystyle=\int\_{A}\gamma\_{2}^{\beta}(v,t,x,y)\,\mathrm{d}v |  |

###### Proposition 4.9.

In the Black-Scholes-Merton model with θ>0,p​σ>θ\theta>0,p\sigma>\theta, zz decreasing and S0≠KDS\_{0}\neq K^{D}, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ¯​[(sup0≤u≤TJuζ)∨M]\displaystyle\mathbb{E}^{\overline{\mathbb{Q}}}\left[\left(\sup\_{0\leq u\leq T}J\_{u}^{\zeta}\right)\vee M\right] | =M+∫0Tγ1β​(u,x,y)​(z​(u;λ)−M)+​du\displaystyle=M+\int\_{0}^{T}\gamma\_{1}^{\beta}(u,x,y)(z(u;\lambda)-M)\_{+}\,\mathrm{d}u |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.17) |  |  | =M+∫0r∗​(M;λ)γ1β​(u,x,y)​(z​(u;λ)−M)​du\displaystyle=M+\int\_{0}^{r^{\*}(M;\lambda)}\gamma\_{1}^{\beta}(u,x,y)(z(u;\lambda)-M)\,\mathrm{d}u |  |

where x=σ−1​log⁡(S0),y=σ−1​log⁡(KD),β=σ/2−θ/px=\sigma^{-1}\log(S\_{0}),y=\sigma^{-1}\log(K^{D}),\beta=\sigma/2-\theta/p, and

|  |  |  |
| --- | --- | --- |
|  | r∗​(M;λ):=inf{u<T:z​(u;λ)<M}∧T.r^{\*}(M;\lambda):=\inf\{u<T:z(u;\lambda)<M\}\wedge T. |  |

###### Proof.

First note that the parameters x,yx,y and β\beta come from the relevant terms in ([4.14](https://arxiv.org/html/2512.24371v1#S4.E14 "In 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) together with Btℚ¯:=Btℚ−θp​tB\_{t}^{\overline{\mathbb{Q}}}:=B\_{t}^{\mathbb{Q}}-\frac{\theta}{p}t.

From Theorem [4.6](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem6 "Theorem 4.6. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") we observe that

|  |  |  |
| --- | --- | --- |
|  | sup0≤u≤TJuζ=z​(HKD;λ)∨0\displaystyle\sup\_{0\leq u\leq T}J\_{u}^{\zeta}=z(H\_{K^{D}};\lambda)\vee 0 |  |

holds, and therefore

|  |  |  |
| --- | --- | --- |
|  | sup0≤u≤TJuζ∨M=M+(z​(HKD;λ)−M)+.\displaystyle\sup\_{0\leq u\leq T}J\_{u}^{\zeta}\vee M=M+(z(H\_{K^{D}};\lambda)-M)\_{+}. |  |

The result now follows upon noting that zz is decreasing and the observation that HKDH\_{K^{D}} has distribution given by γ1β\gamma\_{1}^{\beta}.
∎

We now put together the results of this section to give a complete characterisation of the optimal wealth in the case of a long position in call options.

###### Theorem 4.10.

Suppose the conditions of Proposition [4.9](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem9 "Proposition 4.9. ‣ 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") and Theorem [4.4](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") hold.
Then there exists an admissible trading strategy which is long λ\lambda units of the Call option with strike KK if and only if

|  |  |  |
| --- | --- | --- |
|  | w0+λ​Δ​C≥∫0r∗​(0;λ)γ1β​(u,x,y)​z​(u;λ)​du.w\_{0}+\lambda\Delta C\geq\int\_{0}^{r^{\*}(0;\lambda)}\gamma\_{1}^{\beta}(u,x,y)z(u;\lambda)\,\mathrm{d}u. |  |

If this holds then the value of MM in the trader’s optimal portfolio is the unique solution to the equation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.18) |  | w0+λ​Δ​C\displaystyle w\_{0}+\lambda\Delta C | =M+∫0r∗​(M;λ)γ1β​(u,x,y)​{z​(u;λ)−M}​du,\displaystyle=M+\int\_{0}^{r^{\*}(M;\lambda)}\gamma\_{1}^{\beta}(u,x,y)\left\{z(u;\lambda)-M\right\}\,\mathrm{d}u, |  |

and the optimal utility is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[up​(WTπ,C)]=cp⋅(up​(M)+∫0r∗​(M;λ)γ1β​(s,x,y)​{up​(z​(s;λ))−up​(M)}​ds),\mathbb{E}\left[u\_{p}(W\_{T}^{\pi,C})\right]=c\_{p}\cdot\left(u\_{p}(M)+\int\_{0}^{r^{\*}(M;\lambda)}\gamma\_{1}^{\beta}(s,x,y)\left\{u\_{p}(z(s;\lambda))-u\_{p}(M)\right\}\,\mathrm{d}s\right), |  |

where M:=M​(λ)M:=M(\lambda) is the value given by ([4.18](https://arxiv.org/html/2512.24371v1#S4.E18 "In Theorem 4.10. ‣ 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) and cp=(𝔼​[HT1−1p])pc\_{p}=\left(\mathbb{E}\left[H\_{T}^{1-\frac{1}{p}}\right]\right)^{p}.

###### Proof.

The first claim follows from Proposition [4.9](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem9 "Proposition 4.9. ‣ 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") and Theorem [4.4](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"). It also follows from this and the fact that with positive probability, since S0≠KDS\_{0}\neq K^{D}, HKD≥TH\_{K^{D}}\geq T that a unique value of MM satisfying ([4.18](https://arxiv.org/html/2512.24371v1#S4.E18 "In Theorem 4.10. ‣ 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) exists.

The form of the optimal utility now follows from applying the known distribution of (sup0≤u≤TJuζ)∨M\left(\sup\_{0\leq u\leq T}J\_{u}^{\zeta}\right)\vee M, and the arguments of Lemma [4.1](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints").
∎

###### Remark 4.11.

In general the expression for γ1β\gamma\_{1}^{\beta} does not exist in closed form (unless β=0\beta=0), however it is well known that its Laplace transform can be given in closed form. In combination with the fact that the right hand side of ([4.18](https://arxiv.org/html/2512.24371v1#S4.E18 "In Theorem 4.10. ‣ 4.3. Long positions in Call options in the Black-Scholes-Merton model ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")) is increasing in MM, this means that the optimal value of MM can be found quickly via simple numerical methods.

###### Remark 4.12.

In the case where the initial value of the asset is equal to the at-the-money strike, S0=KDS\_{0}=K^{D}, then HKD≡0H\_{K^{D}}\equiv 0 and so the resulting sup0≤u≤TJuζ\sup\_{0\leq u\leq T}J^{\zeta}\_{u} is fixed. Hence the optimal wealth will also be deterministic, and there hence this case is trivial.

### 4.4. Numerical Results

In the context of the above results, it is possible now to numerically compute various relevant quantities to get a sense of the typical behaviour. We show the results of such numerical computations below.

![Refer to caption](x3.png)


Figure 3.  The figure shows the value of MM as a function of λ\lambda. The parameters used are S0=1.2,K=0.85,T=2,σ=0.5,r=0.01,α=0.4,Δ​C=0.02,p=0.75,θ=0.05S\_{0}=1.2,K=0.85,T=2,\sigma=0.5,r=0.01,\alpha=0.4,\Delta C=0.02,p=0.75,\theta=0.05.

![Refer to caption](x4.png)


Figure 4.  The figure shows the value of r∗​(M​(λ),λ)r^{\*}(M(\lambda),\lambda) as a function of λ\lambda. The parameters are the same as in Figure [3](https://arxiv.org/html/2512.24371v1#S4.F3 "Figure 3 ‣ 4.4. Numerical Results ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"). Note that for λ\lambda small, then M​(λ)≥z​(0;λ)M(\lambda)\geq z(0;\lambda), the intermediate wealth constraint is never binding, and r∗​(M,λ)=0r^{\*}(M,\lambda)=0.

![Refer to caption](x5.png)


Figure 5.  The figure shows the value of the utility as a function of λ\lambda. The parameters are the same as in Figure [3](https://arxiv.org/html/2512.24371v1#S4.F3 "Figure 3 ‣ 4.4. Numerical Results ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"). In this case, the optimal utility occurs when λ≈3.1\lambda\approx 3.1.

We observe that MM appears to be concave in λ\lambda, and we see similar behaviour when we plot the utility, where the optimal value utility is attained for λ\lambda approximately equal to 3.13.1. The value of r∗​(M,λ)r^{\*}(M,\lambda) is increasing in λ\lambda, although there is an initial interval where it is equal to zero, since M​(λ)≥z​(0;λ)M(\lambda)\geq z(0;\lambda), and the intermediate wealth constraint is never binding. Note that this interval also corresponds to linear behaviour for the value of MM as a function of λ\lambda, since here we can directly hedge the exposure, and we always guarantee a terminal wealth equal to w0+λ​Δ​C≡Mw\_{0}+\lambda\Delta C\equiv M.

The explanation for this behaviour can be seen in Figure [6](https://arxiv.org/html/2512.24371v1#S4.F6 "Figure 6 ‣ 4.4. Numerical Results ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"), which shows the cumulative distribution function of the optimal wealth YTY\_{T} for the optimal strategy. We see that as we increase λ\lambda, the mean of the distribution increases, but the variance also increases. The large jump on the left of each distribution function corresponds to the value of MM, and for small values of λ\lambda, then this step corresponds to a large proportion of the distribution. As λ\lambda increases, the proportion of the distribution that is at MM decreases, and the distribution becomes more spread out. As we increase λ\lambda, the mean of the distribution also increases. The optimal choice of λ\lambda is then determined through a trade-off between the mean and variability of the resulting distribution.

![Refer to caption](x6.png)


Figure 6.  The figure shows the cumulative distribution function of the optimal wealth YTY\_{T} for the optimal strategy. In this case, different curves show the effect of different values of λ\lambda. The parameters are the same as in Figure [3](https://arxiv.org/html/2512.24371v1#S4.F3 "Figure 3 ‣ 4.4. Numerical Results ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints").

## 5. Effect of static/dynamic hedging under intrinsic wealth constraints: One-touch options

In this section we consider the impact of intrinsic wealth constraints when hedging a path-dependent option. Specifically, in the case of a one-touch option, we are able to compare the case of hedging dynamically using the underlying asset alone, with the case of completing the hedge using a static position in vanilla options. In this case, we exploit the classical example of a static superhedge of a one-touch option using vanilla options and dynamic trading in the underlying asset due to Hobson [[21](https://arxiv.org/html/2512.24371v1#bib.bib21)]. As we will see, there is strong numerical evidence that even in a complete market setting, where the vanilla options are priced at their replication price, the impact of the static position on the intrinsic wealth constraint is significant, and leads to notable benefits to the trader who looks to sell a one-touch option.

### 5.1. Max-plus representation for the one-touch option

We begin by recalling the definition of the one-touch option, and Hobson’s static superhedging strategy.

A one-touch option is a path-dependent option which pays out a fixed amount if the underlying asset price hits a pre-specified barrier level at any time before maturity. For simplicity, we suppose the barrier crossing is determined in forward price units, and our discount process is Dt=e−r​tD\_{t}=e^{-rt}, with rr a positive constant, under the hypotheses stated in the previous section. From Example [2.2](https://arxiv.org/html/2512.24371v1#S2.Thmtheorem2 "Example 2.2. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints")-[iii](https://arxiv.org/html/2512.24371v1#S2.I2.i3 "item iii ‣ Example 2.2. ‣ 2.1. Intrinsic Value of Derivative Contracts ‣ 2. Intrinsic Valuation of Derivatives and Trading ‣ Utility maximisation with model-independent constraints"), the *one-touch* option has payoff 𝖮𝖳TB:=𝟏{ST∗≥B}\mathsf{OT}^{B}\_{T}:=\boldsymbol{1}\_{\{S\_{T}^{\*}\geq B\}}, where St∗=supr≤tSrS\_{t}^{\*}=\sup\_{r\leq t}S\_{r} is the maximum process and B>0B>0 is a fixed barrier. Recall that the discounted version of SS and BB is denoted by StD=Dt​StS^{D}\_{t}=D\_{t}S\_{t} and BD=DT​BB^{D}=D\_{T}B. Define HB=inf{t≥0:StD≥BD}H\_{B}=\inf\{t\geq 0:S\_{t}^{D}\geq B^{D}\} and the one-touch option can alternatively be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | CT0\displaystyle C^{0}\_{T} | =𝟏{St≥B​Dt−1​DT,for some​t∈[0,T]}\displaystyle=\boldsymbol{1}\_{\{S\_{t}\geq BD\_{t}^{-1}D\_{T},\;\text{for\;some}\;t\in[0,T]\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝟏{StD≥BD,for some​t∈[0,T]}.\displaystyle=\boldsymbol{1}\_{\{S\_{t}^{D}\geq B^{D},\;\text{for\;some}\;t\in[0,T]\}}. |  |

Hobson’s superhedging strategy for the one-touch option consists of a short position in the one-touch option itself, combined with a static position in vanilla Call options and dynamic trading in the underlying asset. Specifically, given K<BK<B fixed, we can consider the portfolio with a payoff C~T0\tilde{C}^{0}\_{T} composed by a long position of 1B−K\frac{1}{B-K} Call options with strike KK and, if SDS^{D} hits BDB^{D} before terminal time TT, short sell 1B−K\frac{1}{B-K} units of asset, that is,

|  |  |  |
| --- | --- | --- |
|  | C~T0=1B−K​(ST−K)++1B−K​{(B​DT​DHB−1)​DHB​DT1−−ST}​𝟏{HB≤T}.\displaystyle\tilde{C}^{0}\_{T}=\frac{1}{B-K}(S\_{T}-K)\_{+}+\frac{1}{B-K}\{(BD\_{T}D^{-1}\_{H\_{B}})D\_{H\_{B}}D\_{T}^{{}\_{-}1}-S\_{T}\}\boldsymbol{1}\_{\{H\_{B}\leq T\}}. |  |

Then, putting together the above expressions, the portfolio value at time TT is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C~T0−CT0\displaystyle\tilde{C}^{0}\_{T}-C^{0}\_{T} | =1B−K​[(ST−K)++(B−ST)​𝟏HB≤T]−𝟏{HB≤T}\displaystyle=\frac{1}{B-K}[(S\_{T}-K)\_{+}+(B-S\_{T})\boldsymbol{1}\_{H\_{B}\leq T}]-\boldsymbol{1}\_{\{H\_{B}\leq T\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={1B−K​(ST−K)+,HB>T1B−K​(K−ST)+,HB≤T.\displaystyle=\begin{cases}\frac{1}{B-K}(S\_{T}-K)\_{+},\;\;&H\_{B}>T\\ \frac{1}{B-K}(K-S\_{T})\_{+},\;\;&H\_{B}\leq T.\end{cases} |  |

Since the right-hand side is always non-negative, we deduce that C~T0\tilde{C}^{0}\_{T} is a superhedge for the one-touch option.

In [[21](https://arxiv.org/html/2512.24371v1#bib.bib21)] it is shown moreover that the superhedging strategy is optimal in the sense that there exists a model under which C~T0=CT0\tilde{C}^{0}\_{T}=C^{0}\_{T} almost surely, and hence the cost of the superhedge is equal to the arbitrage-free price of the one-touch option. Note that the choice of KK is not fixed, but there is a choice of KK which minimises the cost of the superhedge, and this choice of KK corresponds to the model which attains equality.

Notice that from this expression we can deduce that its intrinsic value at time tt has the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐt​(C~T0−CT0)\displaystyle\mathcal{I}\_{t}(\tilde{C}^{0}\_{T}-C^{0}\_{T}) | ={DTDt⋅1B−K​(K−DtDT​St)+,HB≤t≤T0,t<HB∧T\displaystyle=\begin{cases}\frac{D\_{T}}{D\_{t}}\cdot\frac{1}{B-K}(K-\frac{D\_{t}}{D\_{T}}S\_{t})\_{+},\;\;&H\_{B}\leq t\leq T\\ 0,\;\;&t<H\_{B}\wedge T\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={1B−K​(K​DTDt−St)+,HB≤t≤T0,t<HB∧T,\displaystyle=\begin{cases}\frac{1}{B-K}(K\frac{D\_{T}}{D\_{t}}-S\_{t})\_{+},\;\;&H\_{B}\leq t\leq T\\ 0,\;\;&t<H\_{B}\wedge T,\end{cases} |  |

and hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​ℐt​(C~T0−CT0)\displaystyle D\_{t}\mathcal{I}\_{t}(\tilde{C}^{0}\_{T}-C^{0}\_{T}) | ={1B−K​(KD−StD)+,HB≤t≤T0,t<HB∧T,\displaystyle=\begin{cases}\frac{1}{B-K}(K^{D}-S^{D}\_{t})\_{+},\;\;&H\_{B}\leq t\leq T\\ 0,\;\;&t<H\_{B}\wedge T,\end{cases} |  |

which is clearly a ℚ\mathbb{Q}-submartingale.
Then, the intrinsic wealth constraint process (see ([4.8](https://arxiv.org/html/2512.24371v1#S4.E8 "In Remark 4.2. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"))), is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | ζt:=−α​Dt−1​ξt−1−ξt−1​ℐt​(C~T0−CT0)+𝔼ℚ¯​[ξT−1​(C~T0−CT0)|ℱt],t∈[0,T),\zeta\_{t}:=-\alpha D\_{t}^{-1}\xi\_{t}^{-1}-\xi\_{t}^{-1}\mathcal{I}\_{t}(\tilde{C}^{0}\_{T}-C^{0}\_{T})+\mathbb{E}^{\overline{\mathbb{Q}}}\left[\xi\_{T}^{-1}(\tilde{C}^{0}\_{T}-C^{0}\_{T})|\mathcal{F}\_{t}\right],\;\;\;t\in[0,T), |  |

with ξt\xi\_{t} as in ([4.6](https://arxiv.org/html/2512.24371v1#S4.E6 "In 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")). Following the same arguments given in Remark [4.2](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem2 "Remark 4.2. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"), we get that ζt\zeta\_{t} is a ℚ¯\overline{\mathbb{Q}}-supermartingale, and hence

|  |  |  |
| --- | --- | --- |
|  | ζ^t:=Dt​ξt​ζt=−α−Dt​ℐt​(C~T0−CT0)+𝔼ℚ​[DT​(C~T0−CT0)|ℱt],t∈[0,T],\hat{\zeta}\_{t}:=D\_{t}\xi\_{t}\zeta\_{t}=-\alpha-D\_{t}\mathcal{I}\_{t}(\tilde{C}^{0}\_{T}-C^{0}\_{T})+\mathbb{E}^{\mathbb{Q}}\left[D\_{T}(\tilde{C}^{0}\_{T}-C^{0}\_{T})|\mathcal{F}\_{t}\right],\;\;t\in[0,T], |  |

is a ℚ\mathbb{Q}-supermartingale with terminal condition ζ^T=−α\hat{\zeta}\_{T}=-\alpha. To include the non-negativity constraint on the intrinsic wealth at the terminal time, as above we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ^t0\displaystyle\hat{\zeta}\_{t}^{0} | :=ζ^t​𝟏{t<T}={ζ^t,t<T0,t=T.\displaystyle:=\hat{\zeta}\_{t}\boldsymbol{1}\_{\{t<T\}}=\begin{cases}\hat{\zeta}\_{t},&t<T\\ 0,&t=T.\end{cases} |  |

From the previous calculations of the intrinsic value of the derivative, for t<Tt<T, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ^t0=\displaystyle\hat{\zeta}\_{t}^{0}= | −α−1B−K​(KD−StD)+​𝟏{HB≤t<T}\displaystyle-\alpha-\frac{1}{B-K}(K^{D}-S^{D}\_{t})\_{+}\boldsymbol{1}\_{\{H\_{B}\leq t<T\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +DTB−K​{𝔼ℚ​[(ST−K)+​𝟏{HB>T}+(K−ST)+​𝟏{HB≤T}|ℱt]}\displaystyle+\frac{D\_{T}}{B-K}\left\{\mathbb{E}^{\mathbb{Q}}\left[(S\_{T}-K)\_{+}\boldsymbol{1}\_{\{H\_{B}>T\}}+(K-S\_{T})\_{+}\boldsymbol{1}\_{\{H\_{B}\leq T\}}|\mathcal{F}\_{t}\right]\right\} |  |

As a first step, we provide a Max-plus representation for the Snell envelope of ζ^t0\hat{\zeta}\_{t}^{0}, denoted as ζ^t0,∗\hat{\zeta}\_{t}^{0,\*}, under measure ℚ\mathbb{Q}, meaning that there exists a process JuζJ\_{u}^{\zeta} such that

|  |  |  |
| --- | --- | --- |
|  | ζ^t0,∗=𝔼ℚ​[supt≤u≤TJuζ|ℱt].\hat{\zeta}\_{t}^{0,\*}=\mathbb{E}^{\mathbb{Q}}\left[\sup\_{t\leq u\leq T}J\_{u}^{\zeta}|\mathcal{F}\_{t}\right]. |  |

Note that the Snell envelope of ζ^0\hat{\zeta}^{0} is equal to the Snell envelope of ζ^∨0\hat{\zeta}\vee 0, and using the last part of Lemma [A.1](https://arxiv.org/html/2512.24371v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Results on Max-Plus Representations ‣ Utility maximisation with model-independent constraints"), we can get the representation for the later once we have the one for ζ^\hat{\zeta}. The ideas to do this have been already implemented in the proof of Theorem [4.6](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem6 "Theorem 4.6. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"), and
Corollary [4.8](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem8 "Corollary 4.8. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints") for the case when α=0\alpha=0, therefore, we will simply outline the line of argument that should be followed.

First, using the fact that ζ^\hat{\zeta} is a supermartingale, its Max-plus representation can be obtained using the first part of Lemma [A.1](https://arxiv.org/html/2512.24371v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Results on Max-Plus Representations ‣ Utility maximisation with model-independent constraints"), using the analogous class of stopping times as in ([4.12](https://arxiv.org/html/2512.24371v1#S4.E12 "In Proof. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")). Defining

|  |  |  |
| --- | --- | --- |
|  | φℚ​(u)=1B−K​𝔼ℚ​[(KD−STD)+|SuD=KD]−α,\varphi\_{\mathbb{Q}}(u)=\frac{1}{B-K}\mathbb{E}^{\mathbb{Q}}\left[(K^{D}-S^{D}\_{T})\_{+}\;|\;S\_{u}^{D}=K^{D}\right]-\alpha, |  |

it is given by

|  |  |  |
| --- | --- | --- |
|  | Juζ^={−α,u=Tφℚ​(u),u=H∗<T,−∞,otherwise.J\_{u}^{\hat{\zeta}}=\begin{cases}-\alpha,&u=T\\ \varphi\_{\mathbb{Q}}(u),&u=H^{\*}<T,\\ -\infty,&\text{otherwise}.\end{cases} |  |

From here, we can now use Lemma [A.1](https://arxiv.org/html/2512.24371v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Results on Max-Plus Representations ‣ Utility maximisation with model-independent constraints") part (ii), to get the representation for ζ^t0,∗\hat{\zeta}\_{t}^{0,\*},

|  |  |  |
| --- | --- | --- |
|  | Juζ0,∗={(−α+DTB−K​(ST−K)+)+​𝟏{HB>T},u=Tφℚ∗​(u),HB<u<T,SuD=KD−∞,otherwise,J\_{u}^{\zeta^{0,\*}}=\begin{cases}\left(-\alpha+\frac{D\_{T}}{B-K}(S\_{T}-K)\_{+}\right)\_{+}\boldsymbol{1}\_{\{H\_{B}>T\}},&u=T\\ \varphi\_{\mathbb{Q}}^{\*}(u),&H\_{B}<u<T,S\_{u}^{D}=K^{D}\\ -\infty,&\text{otherwise},\end{cases} |  |

where

|  |  |  |
| --- | --- | --- |
|  | φℚ∗​(u)=max⁡{φℚ​(u),0}.\varphi\_{\mathbb{Q}}^{\*}(u)=\max\left\{\varphi\_{\mathbb{Q}}(u),0\right\}. |  |

In this case we can apply Lemma [A.1](https://arxiv.org/html/2512.24371v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Results on Max-Plus Representations ‣ Utility maximisation with model-independent constraints") part (i) with τt:=inf{u≥t:SuD=KD,HB≤u<T}∧T\tau\_{t}:=\inf\{u\geq t:S\_{u}^{D}=K^{D},H\_{B}\leq u<T\}\wedge T.

###### Remark 5.1.

Notice that the Max-plus representation is needed under measure ℚ¯\overline{\mathbb{Q}}, and it can be obtained using Lemma [A.2](https://arxiv.org/html/2512.24371v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Results on Max-Plus Representations ‣ Utility maximisation with model-independent constraints") part (ii), applying to the corresponding Radon-Nikodym derivative martingale {Dt​ξt}\{D\_{t}\xi\_{t}\}; see Remark [4.2](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem2 "Remark 4.2. ‣ 4.1. Complete Market Assumption ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"). This result was not needed in the proof of Theorem [4.6](https://arxiv.org/html/2512.24371v1#S4.Thmtheorem6 "Theorem 4.6. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints")
because the process {ϕt:=ξt−1​Dt−1}\{\phi\_{t}:=\xi\_{t}^{-1}D\_{t}^{-1}\} was implicit in all the calculations where it was involved; see, in particular, [4.11](https://arxiv.org/html/2512.24371v1#S4.E11 "In Theorem 4.6. ‣ 4.2. Long position in Call options ‣ 4. Utility Maximisation in Complete Markets ‣ Utility maximisation with model-independent constraints"), so that we could obtain the representation under the measure ℚ¯\overline{\mathbb{Q}}.

### 5.2. Numerical results

We now present some numerical results which illustrate the impact of the intrinsic wealth constraint when hedging a one-touch option, comparing the case where the trader uses only dynamic trading in the underlying asset, with the case where the trader also holds a static position in vanilla Call options as described above.

Using the max-plus representation described above, we can numerically compute the optimal terminal portfolio wealth for the trader in both cases. Computing this requires numerical evaluation of hitting time densities for Brownian motion with drift, which can be done using standard numerical methods for inversion of the Laplace transform.

In the numerical results below, we consider a trader who sells one-touch options with barrier B=1.9B=1.9 and maturity T=2T=2, in a Black-Scholes-Merton model with parameters S0=1.2,r=0.01,σ=0.5,θ=0.05S\_{0}=1.2,r=0.01,\sigma=0.5,\theta=0.05. The trader has initial wealth w0=0.1w\_{0}=0.1, risk aversion parameter p=0.75p=0.75, and intrinsic wealth constraint parameter α=0.1\alpha=0.1. In this model, the arbitrage-free price of the one-touch option is approximately 0.410.41.

Since we believe the trader will benefit from holding a short position in the one-touch option, we consider the case where the trader is able to sell the one-touch option for a premium to the cost of dynamically replicating. Specifically, we suppose that the trader is able to sell the one-touch option for a premium of Δ​C=0.02\Delta C=0.02 above the replication cost.

![Refer to caption](ExpectedUtilityOT_WithWithoutSH.png)


Figure 7.  The figure shows the expected utility of the trader as a function of the trader’s initial wealth, w0w\_{0}. The solid blue line shows the expected utility when the trader holds a static position in vanilla Call options as part of a superhedging strategy for the one-touch option, while the solid green line shows the expected utility when the trader does not hold the static position. The dashed orange line shows the utility of the trader if they were not to sell the one-touch option at all. Here the superhedge uses call options with strike K=0.1.3K=0.1.3.

In Figure [7](https://arxiv.org/html/2512.24371v1#S5.F7 "Figure 7 ‣ 5.2. Numerical results ‣ 5. Effect of static/dynamic hedging under intrinsic wealth constraints: One-touch options ‣ Utility maximisation with model-independent constraints"), we can see the expected utility of the trader under different scenarios. We observe that when the trader’s initial wealth is small, the benefit of selling the call option does not outweigh the loss that is incurred because the trader must trade in such a way as to avoid breaching the intrinsic wealth constraint. When the wealth is large, both the case with and without the semi-static hedge outperform the case where the trader does not sell the one-touch option, and in both cases the trader is able to exploit the premium received from selling the one-touch at a premium with minimal effect of the intrinsic wealth constraint. Notably, however, the case where the trader holds the semi-static position in vanilla Call options is much more impactful in the case where the trader’s initial wealth is moderate. Moreoever, the initial wealth at which the trader is even able to implement the strategy is much lower in the semi-static case (w0≈0.08w\_{0}\approx 0.08) than in the case without the static hedge (w0≈0.18w\_{0}\approx 0.18).

![Refer to caption](x7.png)


Figure 8.  The figure shows the expected utility of the trader as a function of the wealth w0w\_{0} of trader for different strikes. The utiliy is shown in terms of the difference between the certainty equivalent of the utility with and without the hedge. The plots are shown for a range of stikes KK for the vanilla Call options used in the semi-static hedge.

![Refer to caption](x8.png)


Figure 9.  The plot shows the certainty equivalent of the trader when holding the semi-static hedge as a function of the strike KK of the vanilla Call options used in the hedge. Highlighted is the choice of semi-static hedge which corresponds to the minimal-cost superhedge (’Hobson-optimal KK’). The initial wealth is w0=0.1w\_{0}=0.1.

We can also examine the impact of different choices of the parameter KK. Figure [8](https://arxiv.org/html/2512.24371v1#S5.F8 "Figure 8 ‣ 5.2. Numerical results ‣ 5. Effect of static/dynamic hedging under intrinsic wealth constraints: One-touch options ‣ Utility maximisation with model-independent constraints") shows the expected utility of the trader as a function of initial wealth for a range of different strikes KK used in the semi-static hedge. We observe that there is no uniformly best choice of KK. However there is some evidence in Figure [9](https://arxiv.org/html/2512.24371v1#S5.F9 "Figure 9 ‣ 5.2. Numerical results ‣ 5. Effect of static/dynamic hedging under intrinsic wealth constraints: One-touch options ‣ Utility maximisation with model-independent constraints") that suggests the optimal choice of KK is not exactly the ‘Hobson-optimal’ strike, but this choice is close to optimal.

## 6. Summary and Future Work

In this paper we consider the problem of optimal investment in a portfolio which combines dynamic trading and a static position in options. The novelty in our work comes from a trading constraint which is based on the intrinsic, or worst case value of the option. This setting allows us to develop a framework for hedging which sits between classical and robust settings for option pricing. We are able to develop explicit characterisations of the optimal trading strategy in certain cases, and we are able to see in simple examples how the optimal strategy finds a balance between the desire to maximise expected profit, and the risk associated with extreme positions relative to the trader’s capacity to sustain short-term mark-to-market losses.

Notably, we see in our numerical results that even in a complete market setting, the presence of the intrinsic wealth constraint can have a significant impact on the optimal strategy. In particular, in the case of the one-touch option, we are able to see the benefit of holding semi-static hedging positions in vanilla options, even when these options are priced at their replication cost. This suggests that even in complete market settings, the presence of intrinsic wealth constraints could justify the use of semi-static hedging strategies.

While our explicit results make fairly strong assumptions (for example, complete markets), our framework is flexible, and future work to understand the impact of considering a larger class of possible hedging models (e.g. moving to an incomplete market setting), or allowing for uncertain volatility models, for example, would be interesting to understand.

Acknowledgements:

AC and DHH acknowledge the support of the Royal Society, through the Newton International Fellowship scheme NI160069. The second author is very grateful for the hospitality of the University of Bath.

## Appendix A Results on Max-Plus Representations

In this appendix we prove some results on Max-plus representations for cádlàg supermartingales under specific assumptions on the structure of the supermartingale.

We suppose specifically that the cádlàg supermartingale (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} can be written as a martingale up to a specific exit time. That is, we suppose there exists a maximal family of increasing stopping times {τt;t∈[0,T]}\{\tau\_{t};t\in[0,T]\} such that τt∈[t,T]\tau\_{t}\in[t,T], τt≤τs\tau\_{t}\leq\tau\_{s} for t≤st\leq s,

|  |  |  |  |
| --- | --- | --- | --- |
| (A.1) |  | Xt=𝔼ℚ​[Xτt|ℱt],X\_{t}=\mathbb{E}^{\mathbb{Q}}\left[X\_{\tau\_{t}}|\mathcal{F}\_{t}\right], |  |

and such that

|  |  |  |  |
| --- | --- | --- | --- |
| (A.2) |  | Xt>𝔼ℚ​[Xσ|ℱt], for all stopping times ​σ≥τt​ with ​ℙ​(σ>τt)>0.X\_{t}>\mathbb{E}^{\mathbb{Q}}\left[X\_{\sigma}|\mathcal{F}\_{t}\right],\text{ for all stopping times }\sigma\geq\tau\_{t}\text{ with }\mathbb{P}(\sigma>\tau\_{t})>0. |  |

In canonical cases, we may consider τt\tau\_{t} to be the first hitting time after time tt by a process to a specific region, for example. We note that the case where τt=t\tau\_{t}=t is not excluded, although in the following result it will imply a very specific structure for XX.

Then we have the following result.

###### Lemma A.1.

Suppose there exists a family of increasing stopping times {τt;t∈[0,T]}\{\tau\_{t};t\in[0,T]\} such that τt∈[t,T]\tau\_{t}\in[t,T] ([A.1](https://arxiv.org/html/2512.24371v1#A1.E1 "In Appendix A Results on Max-Plus Representations ‣ Utility maximisation with model-independent constraints")) and ([A.2](https://arxiv.org/html/2512.24371v1#A1.E2 "In Appendix A Results on Max-Plus Representations ‣ Utility maximisation with model-independent constraints")) hold, and a decreasing function φ:[0,T]→ℝ\varphi:[0,T]\to\mathbb{R} such that if τt=s\tau\_{t}=s for some tt, then

|  |  |  |
| --- | --- | --- |
|  | Xs≥φ​(s)≥Xu, for all ​u>s.X\_{s}\geq\varphi(s)\geq X\_{u},\quad\text{ for all }u>s. |  |

Then (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} has Max-plus representation

|  |  |  |
| --- | --- | --- |
|  | Xt=𝔼ℚ​[supt≤u≤TJu|ℱt],X\_{t}=\mathbb{E}^{\mathbb{Q}}\left[\sup\_{t\leq u\leq T}J\_{u}|\mathcal{F}\_{t}\right], |  |

where

|  |  |  |
| --- | --- | --- |
|  | Ju={Xτu,u=τu<T,XT,u=T,−∞, otherwise.J\_{u}=\begin{cases}X\_{\tau\_{u}},&u=\tau\_{u}<T,\\ X\_{T},&u=T,\\ -\infty,&\text{ otherwise}.\end{cases} |  |

Moreover, the smallest (in convex increasing order) martingale dominating (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} is given by

|  |  |  |
| --- | --- | --- |
|  | Mt=𝔼ℚ​[sup0≤u≤TJu|ℱt],M\_{t}=\mathbb{E}^{\mathbb{Q}}\left[\sup\_{0\leq u\leq T}J\_{u}|\mathcal{F}\_{t}\right], |  |

and for any constant c∈ℝc\in\mathbb{R}, the smallest (in convex increasing order) martingale dominating (Xt∨c)t∈[0,T](X\_{t}\vee c)\_{t\in[0,T]} is given by

|  |  |  |
| --- | --- | --- |
|  | Mtc=𝔼ℚ​[(sup0≤u≤TJu)∨c|ℱt],M\_{t}^{c}=\mathbb{E}^{\mathbb{Q}}\left[\left(\sup\_{0\leq u\leq T}J\_{u}\right)\vee c|\mathcal{F}\_{t}\right], |  |

that is, the Max-plus representation is given by Juc=Ju∨cJ\_{u}^{c}=J\_{u}\vee c, or equivalently

|  |  |  |
| --- | --- | --- |
|  | Ju={Xτu,u=τu<T,Xτu≥cXT∨c,u=T,−∞, otherwise.J\_{u}=\begin{cases}X\_{\tau\_{u}},&u=\tau\_{u}<T,X\_{\tau\_{u}}\geq c\\ X\_{T}\vee c,&u=T,\\ -\infty,&\text{ otherwise}.\end{cases} |  |

Observe that in the trivial case where τt=t\tau\_{t}=t, then the conditions of the lemma imply that XX is a decreasing process, and hence the Max-plus representation is trivially given by Ju=XuJ\_{u}=X\_{u} for u≤Tu\leq T.

###### Proof.

First observe that defining

|  |  |  |
| --- | --- | --- |
|  | J~u={Xu,u=τs<T, some ​s≤u,XT,u=T,−∞, otherwise.\tilde{J}\_{u}=\begin{cases}X\_{u},&u=\tau\_{s}<T,\text{ some }s\leq u,\\ X\_{T},&u=T,\\ -\infty,&\text{ otherwise}.\end{cases} |  |

then

|  |  |  |
| --- | --- | --- |
|  | Xt=𝔼ℚ​[supt≤u≤TJ~u|ℱt],X\_{t}=\mathbb{E}^{\mathbb{Q}}\left[\sup\_{t\leq u\leq T}\tilde{J}\_{u}|\mathcal{F}\_{t}\right], |  |

since if s=τts=\tau\_{t} for some t≤st\leq s then for u≥su\geq s we have Xu≤φ​(s)≤XsX\_{u}\leq\varphi(s)\leq X\_{s}, and hence Xs=𝔼ℚ​[Xτs|ℱs]≥𝔼ℚ​[Xu|ℱs]X\_{s}=\mathbb{E}^{\mathbb{Q}}\left[X\_{\tau\_{s}}|\mathcal{F}\_{s}\right]\geq\mathbb{E}^{\mathbb{Q}}\left[X\_{u}|\mathcal{F}\_{s}\right] with equality if and only if Xτs=Xu=XsX\_{\tau\_{s}}=X\_{u}=X\_{s} almost surely. In particular, supt≤u≤TJ~u=Xs\sup\_{t\leq u\leq T}\tilde{J}\_{u}=X\_{s}. On the other hand, if s≠τts\neq\tau\_{t} for some t≤st\leq s, then in particular s<τss<\tau\_{s}, and Xs=𝔼ℚ​[Xτs|ℱs]=𝔼ℚ​[J~τs|ℱs]≥𝔼ℚ​[supτs≤u≤TJ~u|ℱs]X\_{s}=\mathbb{E}^{\mathbb{Q}}\left[X\_{\tau\_{s}}|\mathcal{F}\_{s}\right]=\mathbb{E}^{\mathbb{Q}}\left[\tilde{J}\_{\tau\_{s}}|\mathcal{F}\_{s}\right]\geq\mathbb{E}^{\mathbb{Q}}\left[\sup\_{\tau\_{s}\leq u\leq T}\tilde{J}\_{u}|\mathcal{F}\_{s}\right]. Moreover, by the maximality of τt\tau\_{t}, if there exists t<st<s such that s<τts<\tau\_{t} with positive probability, then τt=τs\tau\_{t}=\tau\_{s} on {s<τt}\{s<\tau\_{t}\} since Xs=𝔼ℚ​[Xτs∧τt|ℱs]=𝔼ℚ​[Xτt|ℱs]X\_{s}=\mathbb{E}^{\mathbb{Q}}\left[X\_{\tau\_{s}\wedge\tau\_{t}}|\mathcal{F}\_{s}\right]=\mathbb{E}^{\mathbb{Q}}\left[X\_{\tau\_{t}}|\mathcal{F}\_{s}\right] on this set.

The rest of the proof now follows immediately from the fact that Xt=Jt=JtcX\_{t}=J\_{t}=J^{c}\_{t} whenever Jt>cJ\_{t}>c, and properties of max-plus martingales.

∎

To help us in the verification of some results, we will make use of the following result.

###### Lemma A.2.

Let (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} be a ℚ\mathbb{Q}-supermartingale with càdlàg paths.

1. (i)

   Suppose X=Y+ZX=Y+Z where YY and ZZ are both also càdlàg ℚ\mathbb{Q}-supermartingales such that YT,ZT≥0Y\_{T},Z\_{T}\geq 0. Suppose in addition that there exists a stopping time τ≤T\tau\leq T and an ℱτ\mathcal{F}\_{\tau}-measurable set AA such that:

   1. (a)

      Xt∧τX\_{t\wedge\tau} is a ℚ\mathbb{Q}-martingale;
   2. (b)

      Yt=0Y\_{t}=0 on AA for all t≥τt\geq\tau;
   3. (c)

      Zt=0Z\_{t}=0 on AcA^{c} for all t≥τt\geq\tau.

   Then Xt=𝔼ℚ​[supt≤u≤TJu|ℱt]X\_{t}=\mathbb{E}^{\mathbb{Q}}\left[\sup\_{t\leq u\leq T}J\_{u}|\mathcal{F}\_{t}\right], where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Ju\displaystyle J\_{u} | =JuY+JuZ,\displaystyle=J\_{u}^{Y}+J\_{u}^{Z}, |  |

   and JuYJ\_{u}^{Y} and JuZJ\_{u}^{Z} are the Max-plus representations of YY and ZZ respectively.
2. (ii)

   Let (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} be a ℚ\mathbb{Q}-supermartingale with Max-plus representation JuXJ\_{u}^{X}, and suppose ℚ¯\overline{\mathbb{Q}} is an equivalent probability measure to ℚ\mathbb{Q} with Radon-Nikodym derivative d​ℚ¯d​ℚ=MT\frac{\mathrm{d}\overline{\mathbb{Q}}}{\mathrm{d}\mathbb{Q}}=M\_{T}, where (Mt)t∈[0,T](M\_{t})\_{t\in[0,T]} is a strictly positive ℚ\mathbb{Q}-martingale.

   Suppose in addition that there exists a maximal family of stopping times {τt;t∈[0,T]}\{\tau\_{t};t\in[0,T]\} such that τt∈[t,T]\tau\_{t}\in[t,T] for each tt, τt≤τs\tau\_{t}\leq\tau\_{s} when t≤st\leq s and Xt=𝔼ℚ​[JτtX|ℱt]X\_{t}=\mathbb{E}^{\mathbb{Q}}\left[J\_{\tau\_{t}}^{X}|\mathcal{F}\_{t}\right]. If in addition

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | JτtX​Mτt−1\displaystyle J\_{\tau\_{t}}^{X}M^{-1}\_{\tau\_{t}} | ≥JuX​Mu−1,u∈[t,T],\displaystyle\geq J\_{u}^{X}M^{-1}\_{u},\quad u\in[t,T], |  |

   then (X​M−1)t∈[0,T](XM^{-1})\_{t\in[0,T]} is a ℚ¯\overline{\mathbb{Q}}-supermartingale with Max-plus representation JuX¯=1Mu​JuXJ\_{u}^{\overline{X}}=\frac{1}{M\_{u}}J\_{u}^{X}, i.e.

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Xt\displaystyle X\_{t} | =Mt​𝔼ℚ¯​[supt≤u≤T(JuX​Mu−1)|ℱt].\displaystyle=M\_{t}\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{t\leq u\leq T}\left(J\_{u}^{X}M\_{u}^{-1}\right)|\mathcal{F}\_{t}\right]. |  |

###### Proof.

1. (i)

   First observe since YY and ZZ are non-negative, we have JTY,JTZ≥0J\_{T}^{Y},J\_{T}^{Z}\geq 0, and hence JT=JTY+JTZ≥0J\_{T}=J\_{T}^{Y}+J\_{T}^{Z}\geq 0. Further, it follows from the fact that Xt∧τX\_{t\wedge\tau} is a ℚ\mathbb{Q}-martingale that both Yt∧τY\_{t\wedge\tau} and Zt∧τZ\_{t\wedge\tau} are also ℚ\mathbb{Q}-martingales. Therefore, for t≤τt\leq\tau, we have almost surely

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | JuY\displaystyle J\_{u}^{Y} | ≤supτ≤v≤TJvY,u∈[0,τ],\displaystyle\leq\sup\_{\tau\leq v\leq T}J\_{v}^{Y},\quad u\in[0,\tau], |  |

   and similarly for JuZJ\_{u}^{Z}. In addition, on AA, for u≥τu\geq\tau we have JuZ=0J\_{u}^{Z}=0, and similarly on AcA^{c} for JuYJ\_{u}^{Y}. Hence

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | supt≤u≤T(JuY+JuZ)\displaystyle\sup\_{t\leq u\leq T}(J\_{u}^{Y}+J\_{u}^{Z}) | =supt∨τ≤u≤T(JuY+JuZ)\displaystyle=\sup\_{t\vee\tau\leq u\leq T}(J\_{u}^{Y}+J\_{u}^{Z}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ={supt∨τ≤u≤TJuY, on ​A,supt∨τ≤u≤TJuZ, on ​Ac,\displaystyle=\begin{cases}\sup\_{t\vee\tau\leq u\leq T}J\_{u}^{Y},&\text{ on }A,\\ \sup\_{t\vee\tau\leq u\leq T}J\_{u}^{Z},&\text{ on }A^{c},\end{cases} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =supτ∨t≤u≤TJuY+supτ∨t≤u≤TJuZ,\displaystyle=\sup\_{\tau\vee t\leq u\leq T}J\_{u}^{Y}+\sup\_{\tau\vee t\leq u\leq T}J\_{u}^{Z}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =supt≤u≤TJuY+supt≤u≤TJuZ.\displaystyle=\sup\_{t\leq u\leq T}J\_{u}^{Y}+\sup\_{t\leq u\leq T}J\_{u}^{Z}. |  |
2. (ii)

   Since Xt=𝔼ℚ​[JτtX|ℱt]X\_{t}=\mathbb{E}^{\mathbb{Q}}\left[J\_{\tau\_{t}}^{X}|\mathcal{F}\_{t}\right] we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Mt−1​Xt\displaystyle M\_{t}^{-1}X\_{t} | =Mt−1​𝔼ℚ​[JτtX|ℱt]\displaystyle=M\_{t}^{-1}\mathbb{E}^{\mathbb{Q}}\left[J\_{\tau\_{t}}^{X}|\mathcal{F}\_{t}\right] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =𝔼ℚ¯​[JτtX​MT−1|ℱt]\displaystyle=\mathbb{E}^{\overline{\mathbb{Q}}}\left[J\_{\tau\_{t}}^{X}M\_{T}^{-1}|\mathcal{F}\_{t}\right] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =𝔼ℚ¯​[JτtX​Mτt−1|ℱt]\displaystyle=\mathbb{E}^{\overline{\mathbb{Q}}}\left[J\_{\tau\_{t}}^{X}M\_{\tau\_{t}}^{-1}|\mathcal{F}\_{t}\right] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =𝔼ℚ¯​[supt≤u≤T(JuX​Mu−1)|ℱt],\displaystyle=\mathbb{E}^{\overline{\mathbb{Q}}}\left[\sup\_{t\leq u\leq T}(J\_{u}^{X}M\_{u}^{-1})|\mathcal{F}\_{t}\right], |  |

   where in the second last step we have used the fact that M−1M^{-1} is
   a ℚ¯\overline{\mathbb{Q}}-martingale, and in the final step we have used the
   assumption that for all u∈[t,T]u\in[t,T],
   JτtX​Mτt−1≥JuX​Mu−1J\_{\tau\_{t}}^{X}M^{-1}\_{\tau\_{t}}\geq J\_{u}^{X}M^{-1}\_{u}.

∎

## References

* [1]

  B. Acciaio, M. Beiglböck, F. Penkner, W. Schachermayer, and J. Temme.
  A trajectorial interpretation of Doob’s martingale inequalities.
  The Annals of Applied Probability, 23(4):1494–1505, August 2013.
* [2]

  Anna Aksamit, Zhaoxu Hou, and Jan Obłój.
  Robust Framework for Quantifying the Value of Information in Pricing and Hedging.
  SIAM Journal on Financial Mathematics, 11(1):27–59, January 2020.
  Publisher: Society for Industrial and Applied Mathematics.
* [3]

  Peter Bank and David Besslich.
  On a stochastic representation theorem for Meyer-measurable processes.
  Annales de l’Institut Henri Poincaré, Probabilités et Statistiques, 57(3):1336–1368, July 2021.
* [4]

  Peter Bank and Nicole El Karoui.
  A stochastic representation theorem with applications to optimization and obstacle problems.
  The Annals of Probability, 32(1):1030–1067, January 2004.
* [5]

  Mathias Beiglböck, Alexander M. G. Cox, Martin Huesmann, Nicolas Perkowski, and David J. Prömel.
  Pathwise superreplication via Vovk’s outer measure.
  Finance and Stochastics, 21(4):1141–1166, October 2017.
* [6]

  Mathias Beiglböck, Pierre Henry-Labordère, and Friedrich Penkner.
  Model-independent bounds for option prices—a mass transport approach.
  Finance and Stochastics, 17(3):477–501, July 2013.
* [7]

  Sara Biagini, Bruno Bouchard, Constantinos Kardaras, and Marcel Nutz.
  Robust Fundamental Theorem for Continuous Processes.
  Mathematical Finance, 27(4):963–987, 2017.
* [8]

  Bruno Bouchard and Marcel Nutz.
  Consistent price systems under model uncertainty.
  Finance and Stochastics, 20(1):83–98, January 2016.
* [9]

  Douglas T. Breeden and Robert H. Litzenberger.
  Prices of State-Contingent Claims Implicit in Option Prices.
  The Journal of Business, 51(4):621–651, October 1978.
* [10]

  Patrick Cheridito, Matti Kiiski, David J. Prömel, and H. Mete Soner.
  Martingale optimal transport duality.
  Mathematische Annalen, 379(3):1685–1712, April 2021.
* [11]

  Alexander M. G. Cox, Zhaoxu Hou, and Jan Obłój.
  Robust pricing and hedging under trading restrictions and the emergence of local martingale models.
  Finance and Stochastics, pages 1–36, March 2016.
* [12]

  Alexander M. G. Cox and Sigrid Källblad.
  Model-Independent Bounds for Asian Options: A Dynamic Programming Approach.
  SIAM Journal on Control and Optimization, 55(6):3409–3436, January 2017.
* [13]

  Alexander M. G. Cox and Jan Obłój.
  Robust pricing and hedging of double no-touch options.
  Finance and Stochastics, 15(3):573–605, September 2011.
* [14]

  Alexander M. G. Cox and Jiajie Wang.
  Root’s barrier: Construction, optimality and applications to variance options.
  The Annals of Applied Probability, 23(3):859–894, June 2013.
* [15]

  Yan Dolinsky and Ariel Neufeld.
  Super-replication in fully incomplete markets.
  Mathematical Finance, 28(2):483–515, 2018.
* [16]

  Yan Dolinsky and H. Mete Soner.
  Martingale optimal transport and robust hedging in continuous time.
  Probability Theory and Related Fields, 160(1):391–427, October 2014.
* [17]

  Yan Dolinsky and H. Mete Soner.
  Martingale optimal transport in the Skorokhod space.
  Stochastic Processes and their Applications, 125(10):3893–3931, October 2015.
* [18]

  Nicole El Karoui and Asma Meziou.
  Constrained Optimization with Respect to Stochastic Dominance: Application to Portfolio Insurance.
  Mathematical Finance, 16(1):103–117, 2006.
* [19]

  Nicole El Karoui and Asma Meziou.
  Max-Plus Decomposition of Supermartingales and Convex Order. Application to American Options and Portfolio Insurance.
  The Annals of Probability, 36(2):647–697, 2008.
* [20]

  A. Galichon, P. Henry-Labordère, and N. Touzi.
  A stochastic control approach to no-arbitrage bounds given marginals, with an application to lookback options.
  The Annals of Applied Probability, 24(1):312–336, February 2014.
* [21]

  David G. Hobson.
  Robust hedging of the lookback option.
  Finance and Stochastics, 2(4):329–347, August 1998.
* [22]

  Zhaoxu Hou and Jan Obłój.
  Robust pricing–hedging dualities in continuous time.
  Finance and Stochastics, 22(3):511–567, July 2018.
* [23]

  Ioannis Karatzas and Steven E. Shreve.
  Methods of Mathematical Finance.
  Springer Science & Business Media, August 1998.
* [24]

  Interactive Brokers LLC.
  Options Margin Requirements.
  <https://www.interactivebrokers.com/en/trading/margin-options.php#portfolio-margin-page> [Accessed: April 2025].